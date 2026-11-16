# p's counters at VERDICTS — the blind review round of the script as changed for R1 (c) and R2 (b), its mutants, and Code's dispositions (Code, the dpo VERDICTS session; PI date 2026-11-16)

*The seat's raw (`results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md`, committed at `52b2c97`), §3 item 2, verbatim: "One blind review round on the changed lines, with its mutants; a MAJOR comes to the seat."*

*The reviewer was a fresh subagent with no part in the change. It read the change against HEAD, the seat's raw, the rulings that raw cites, and p's call-log functions, with the p and m code they rest on. It ran no Python. Its brief bound it to the list of record v2, items 1–5, and to the rules of Q-F3's campaign on this laptop, both quoted. It opened nothing under `data/p/ckpt`, `data/p/verdicts`, `data/p/reports` or `data/mf3`. It reviewed the script at sha256 `f148bf3fc2ae1c182dd9ae7db51d1afad891683b36e30a7da6da18f035179996` and wrote 16 mutants. It found no MAJOR.*

*Code applied each finding but one: finding 6, a NOTE, is answered with no change, as its fix proposes. The script as committed is sha256 `a87749e9c296ddc7c8e79ab3a50a74138ccec83d42b4217d6805bfef1d53d6f6`. The mutants ran on it, each once through the self-test, in a battery window the coordinating session granted: 16 of 16 killed, baseline PASS.*

*Sections, in order: the review, verbatim; Code's dispositions; the mutants, verbatim; the run's output, verbatim; the runner, verbatim. The local root is shown as `<repo>` and the session's scratch directory as `<scratchpad>`. The review keeps its own headings, which follow inside §1; its title's "r2" names this phase's files, not a second round (the change had one review round). Calendar dates only; the commit hash is the record.*

## 1. The review, verbatim (sha256 `8415b249cca2e0dc5261ea9417b60d81bf7984dbf29b427b584c91391720a055`)

# Blind review r2: `scripts/p_verdicts_counters.py`, working tree (blob 68f76049ff2e9e9c01077d82007e36ec61ab4f40, sha256 f148bf3fc2ae1c182dd9ae7db51d1afad891683b36e30a7da6da18f035179996) against HEAD's blob e641f812 (HEAD 52b2c97), on the seat's R1 (c) and R2 (b)

**Result:** MAJOR 0 / MINOR 4 / NOTE 6. R1 (c) is applied as ruled. The edit follows R2 (b) on every point it can, with one gap in §2.3's first STOP (finding 1). Nothing forbidden is printed. Nothing under `data/p/ckpt` is read beyond the nine checkpoints and the nine call logs, by exact path and after the five gates, and nothing is listed. The sham cells are computed exactly as `build_report` computes them. Three of the 16 mutants are expected to survive the current self-test: M07, M09 and M13 (findings 2 and 8).

## 1. MINOR: the call log is not bound to the report that names it (lines 484–512)

- **What.** p's report names the call log by path and sha256: `"call_log": {**named(pp["p_calls"]), ...}` (stage.py:979–980, 988). It writes that record after the run's end line (stage.py:1097–1104), and a stage with a report refuses every later run (1049–1051). So on an intact record the log's bytes are the reported ones. The step ties the checkpoint to its report by sha256 (line 470). It ties the log to its report only by run count, package, run-line consistency, orphans, re-runs and the sham cells.
- **Why it matters.** Suppose a log is the right stage's but is missing contrast call lines only, for example a tail cut after the last run line (a campaign's last session may be a contrast one). That log passes every one of those checks. The step would then print a short contrast cell and short per-contrast-session counts. That is §2.3's "A log whose sessions are not its checkpoint's ... is a STOP (exit 4)", printed instead of stopped. The self-test's last check ("a contrast round with no call is printed, not stopped") asserts this output.
- **Fix.** Move the `cl = ...` line (503) up and add the check right after the changed-while-read check (line 494):
  ```python
          cl = rep.get("call_log") if isinstance(rep.get("call_log"), dict) else {}
          if cl.get("sha256") != _sha(cbytes) or cl.get("path") != f"ckpt/{u}_{s}_p-calls.jsonl":
              raise Stop(f"STOP: {rrel} does not record {crel}'s sha256 (or names another log)")
  ```
  The path form is p's own (`_rel_to(pp["p_calls"], root)`; p's self-test at stage.py:2246 asserts `"ckpt/OLMo-sft_qual_p-calls.jsonl"`).
- **Self-test changes.**
  - `_synthetic_root` records `"path"` and `"sha256"` (of the bytes `_write_events` wrote) under `call_log`.
  - `edit_log` re-records the edited log's sha256 in that stage's report, so that each existing case still reaches its own check. The m2 case does the same.
  - A new case edits a log without re-recording it and expects a silent STOP whose message says "does not record".
- **Flagged for the seat.** With the binding in place, an unattributed contrast round can come only from the report's own log. Under p's write-ahead log (stage.py:91–99; runner_olmo.py:137–140 records a round only after its generate returned and was logged), that means a lost call line. There are two readings:
  - Printing it follows "the cells p's report gives the sham arm", which include `unattributed_keys`.
  - Stopping on it follows §2.3's first STOP.

  The self-test asserts the first reading. That is Code's reading, not a ruling.

## 2. MINOR: the self-test cannot tell which STOP fired; four new STOP branches are untested in isolation (`stops_silently`, lines 1009–1023; cases 1061–1125)

- **What.** `stops_silently` returns "stop" for any `Stop` raised with nothing printed. The following branches are untested on their own:
  - **(a) The orphan STOP (376–377).** Every orphan also leaves `n_calls > len(by_round)`, so the re-run STOP (378–380) fires in its place. Mutant M07 (orphan STOP dropped) survives.
  - **(b) attribute_calls' problems STOP (373–374).** In `seed_shared`, the calls for seeds 203 and 204 both become orphans, so the orphan STOP fires instead. M09 survives. The "no int seed" problem has no case.
  - **(c) The changed-while-read STOP (493–494).** No case rewrites the log between its two reads, so this STOP never fires in the self-test.
  - **(d) The contrast-session index STOP (393–394), "not an int, or twice".** No case.
- **Fix.**
  - Have `stops_silently` return `str(e)`, and assert one substring per case:

    | Case | Substring |
    |---|---|
    | orphan | "attributed to no recorded round" |
    | re-run | "(a re-run)" |
    | other stage | "is not this stage's" |
    | malformed | "not JSON" |
    | absent | ": absent" |
    | package | "ran under p package" |
    | sham cell | "proxy cells differ" |
    | run count | "run(s);" |
    | flag | "attribution_complete does not match" |
    | shared seed | "p's attribute_calls reports" |

  - Add these cases:
    - A contrast round whose `seed` is None and whose call is removed (problems only, no orphan). This kills M09.
    - The contrast record's `s` set to `"1"`, with the report's checkpoint sha256 re-recorded as `seed_shared` does. The round keys print the same, so nothing earlier STOPs, and the case reaches "not an int".
    - A second contrast session with the same (template, s), fresh seeds and no calls. This is the only way to reach "twice": when the duplicate has calls, the re-run STOP fires first.
    - `p_stage.read_calls` replaced for one case by a wrapper that appends `"\n"` to the log after delegating, saved and restored as `read_domain_view` is. It should STOP with "changed while it was read".

## 3. MINOR: the synthetic call log is not in p's form, so the self-test's no-text check cannot see a text (lines 732–743, check at 956–957)

- **What.** p writes a call line as `{"event": "call", "run": k, **record}`, with the proxy's record `{"call": n, "seed", "text_sha256", "cut": ev}` (stage.py:1351; proxy.py:138).
  - A cut event carries `returned_text` and `stored_text` (proxy.py:87–88).
  - A STOP's call line carries `"stop": {"message", "returned_text", "stored_text"}` (proxy.py:131–132).

  The fixture differs in three ways: it writes `"index"` where p writes `"call"`, it writes `{"synthetic": True}` as the cut, and it has no STOP line. As a result:
  - The check "no call's index ... printed" (`"index" not in printed`) looks for a field name the real logs do not carry.
  - No check could see a cut's or a STOP's text reach stdout or a STOP line, which is the print §2.3 forbids by name ("No call's text, index or timing is printed").

  The proxy header line (578–580) is not exact-matched. So a leak of a cut event alone (no seed in it) would pass every current check.
- **Fix.** Write the fixture in p's form.
  - Call line: `{"event": "call", "run": 1, "call": i, "seed": r["seed"], "text_sha256": ..., "cut": None}`.
  - Cut seeds: `{"returned_text": "SENTINEL-RET\nafter", "stored_text": r["text"], "n_tok_returned": 3, "n_tok_stored": 1, "stop_reason_returned": "cap", "cap_hit_returned": False}`.
  - End line with p's fields: `"status"`, `"exception": None`, `"n_generate"`, `"n_cuts"`.
  - Assert `"SENTINEL" not in printed` and `'"call"' not in printed`, and assert "SENTINEL" in no `stops_silently` message.
  - Add one STOP-call case, `{"event": "call", "run": 1, "call": 9, "seed": 999, "stop": {"message": "PROXY STOP", "returned_text": "SENTINEL-STOP", "stored_text": None}}`, expecting a silent STOP whose message carries no "SENTINEL".

  Keep the sentinel out of `stored_text`, because round texts with control characters are printed by design (F-p13 (a)).

## 4. MINOR: the malformed-line STOP fires on data p's own report tolerates (lines 490–492)

- **What.** `build_report` treats only an absent or unreadable log as fatal (stage.py:949–953). It records malformed lines (`"well_formed": not lp, "n_malformed_lines": len(lp)`, 989), and `CallLog` leaves a torn line by design after a crash, ending it at the next open (stage.py:695–700; docstring 99–100).
- **Why.** §2.3 names two STOPs: a log not its checkpoint's, and an event that is neither attributed nor a cut. A torn run or end line is neither. A torn call line cannot stand alone in an ended stage: the crash leaves its round unrecorded, and the resume that ended the stage re-runs that session, which the orphan or re-run STOP already catches. So this STOP adds nothing to the counts and halts only on a torn run or end line.
- **Fix.**
  - With finding 1's binding, the bytes are the report's, so this STOP can become a printed count. Add `f"; {len(lprobs)} malformed line(s), as {rrel} records"` to the proxy line when it is non-zero.
  - Without the binding, compare against the report instead:
    ```python
    if (not lprobs) is not cl.get("well_formed") or len(lprobs) != cl.get("n_malformed_lines"):
        raise Stop(f"STOP: {crel}: {len(lprobs)} malformed line(s); {rrel} records {cl.get('n_malformed_lines')!r}")
    ```
  - Or keep the STOP and declare it in the docstring as Code's addition beyond §2.3, for the seat.

  The nine reports' `call_log.well_formed` is in the read domain, so Code can see before the window whether this can fire.

## 5. NOTE: "the proxy's STOP": the report holds no message to quote, and a printed row can never be the proxy's (lines 511–512, 576–580; docstring 58)

- **What.** §2.3 says "The proxy's STOP message, where one exists, is quoted from the report, never from the log." But the report's run rows carry only `exception_type` and a `stop` flag, with no message (stage.py:975–977). The message lives in the log's end line and STOP call line (stage.py:1399–1403; proxy.py:131), and in the stage's raw, which ruling (c) of 2026-11-09 covers: "the entry quotes it verbatim".
- **Why a printed row is never the proxy's.** A ProxyStop's own call line has no `text_sha256` (proxy.py:131), so it is always an orphan and pass 1 STOPs before anything prints. Any row printed under "the proxy's STOP:" is therefore a StageStop or m's own STOP. On the record (six PASSes, campaigns ended) the line prints "none".
- **Fix.**
  - Label the line "STOP marks in the p report's run rows". The rows already carry `exception_type`.
  - Have the docstring say that the message, where one exists, is the stage entry's verbatim quote, not this step's.

## 6. NOTE: the re-run and orphan STOPs fire on a session a resume re-ran (lines 376–380)

- **What.** p's `attribute_calls` is written for this case: "where several calls match one round (a resumed session re-run), the last in the log is the one the round records" (stage.py:883–885). After an interruption mid-session, the first attempt's calls become re-run matches (same seed and text) or orphans (same seed, other text). Either way the step STOPs.
- **Why it is acceptable.** This is within §2.3: the superseded call is neither attributed nor a cut. It cannot fire on an uninterrupted record:
  - every recorded round follows exactly one proxied generate (runner_olmo.py:137–140, 164–167);
  - G-VER generates nothing (verify.py:28: "Generations are taken from the recorded round texts");
  - the campaign checks its cap, and pauses, only between sessions (stages.py:2141–2157).
- **What Code can do.** A stage whose report records `call_log.n_runs` > 1 is the only place this can fire; a campaign's pauses add runs harmlessly. Code can read n_runs in the nine reports before the window, so a STOP from this cause is foreseen and goes to the seat as such. No code change.

## 7. NOTE: the ruling raw is untracked, and its pin has no refusal test (lines 165–166, 601–606, 614–616, 817–821)

- **What.** The raw is untracked now (`?? results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md`). Its sha256 is the pinned aea918c5f6f374522ad780ce29685c8c3f950b7457a46933022c090e74680395, and RULING_R1 and RULING_R2 are verbatim in it: one match each by `grep -F`.
- **Why it matters.**
  - Gate 4 binds only the script to HEAD. A run could proceed, and print the raw's path and sha256, with the raw not in the repo.
  - `load_ruling`'s refusal has no case, unlike `load_task_correct`'s (798–803). A mutant dropping its sha check would survive.
- **Fix.**
  - Change the signature to `load_ruling(raw: bytes | None = None)` and add a self-test case with `raw + b"\n"` expecting `Refused`.
  - Before gate 1, assert `git rev-parse HEAD:<raw>` equals `git hash-object -- <raw>`. Alternatively, confirm that the coordinating session's commit of the raw (its §6 item 5) comes before the window.

## 8. NOTE: `_spans` is never tested on a run that ends at the last index (lines 414–424; check 966–970)

- **What.** The only inputs are "s=0-3, 5", "s=4" and "s=1". Mutant M13 (`j + 2 < len(nums)`) survives them all. On the record it would print 80 sessions at one count as "s=0-78, 79". Every index would still be printed, but in another form.
- **Fix.** Add `calls_by_count({("A0-x", 0): 4, ("A0-x", 1): 4}) == ["4 calls: A0-x s=0-1 (2 sessions)"]`.

## 9. NOTE: a check's name claims more than it tests (lines 959–965)

- **What.** The check "proxy_cells on the synthetic records, as p's build_report computes the sham's" compares against Code's hand-written `SYN_SHAM_PROXY`. `build_report` never runs in the self-test.
- **The equivalence holds.** I compared `proxy_cells`' per-arm block with `build_report` (stage.py:967–968, 998–1004). Both use:
  - the same key list over the same sessions (`release_full` is the identity, readrule.py:799–805);
  - the same dict collapse of repeated keys;
  - the same predicates and the same order.

  The run also asserts the equivalence against the nine committed reports.
- **Fix.** Rename the check to "the sham cells equal the hand-computed ones (build_report's rule, stage.py:998–1004)".

## 10. NOTE: STOP lines print log line numbers (lines 491–492)

- **What.** `read_calls`' problems are `"{name}:{i}: not JSON"` and `"{name}:{i}: not a call-log event"` (stage.py:753, 756). The STOP line prints up to three of them. Each is a line number in a withheld log, a per-event position close to §2.3's "No call's ... index". A STOP line goes to the seat and into a raw.
- **Fix.** Print the count instead: `raise Stop(f"STOP: {crel}: {len(lprobs)} line(s) p's read_calls does not read as call-log events")`, or use finding 4's form.

## Checked, no finding

**R1 (c)**
- `TC_STAGES` covers all three stages.
- The assertion runs only where `COMMITTED_SHAM_TC` has a figure: qual and time, with the figures of §1.4.
- The campaign's sham row is printed "no committed figure: this is its first, not asserted".
- The reads-file reproduction now loops over `TC_ASSERTED`.

**R2 (b) paths and reads**
- The nine logs are at `data/p/ckpt/{U}_{stage}_p-calls.jsonl`, p's own path (stage.py:674).
- They are read only in pass 1, after the five gates, by exact path, and never listed. The source adds no listing call.
- p's `read_calls`, `log_consistency_problems(gate=s)` and `attribute_calls` are called unchanged.

**History of the functions the step relies on**
- `attribute_calls`, `round_key`, `CALLS_SCHEMA`, `label`'s G-TIME form, and `build_report`'s `proxy.sham` and run-row lines are identical at d215d5b, e8779b1, 40086e8 and HEAD.
- So the G-TIME reports written at step 6 compare like for like.

**Per contrast session**
- With the orphan and re-run STOPs in force, each call maps to exactly one recorded round. So "calls attributed to its rounds" is "the number of its calls".
- A duplicate key inside one session is ruled out on G-VER-verified records.

**Prints**
- No event field is printed.
- STOP rows come from the report.
- Otherwise the output is digests, counts, round keys and session indices.
- STOP messages carry counts, run-line fields and session indices; finding 10 is the one exception.

**Self-test output**
- The self-test's printed check names match this source, 43/43.

## Mutants (`mutants/mutants_r2.json`: 16; each `old` occurs exactly once, counted with `grep -o -F`)

| id | what | expect |
|---|---|---|
| M01 | `TC_STAGES` drops the campaign | KILLED: the ruling check and the two-passes check FAIL |
| M02 | assertion applied at the campaign (`if True:`) | KILLED: KeyError('campaign'), "ran to its end without raising" FAILs |
| M03 | assertion skipped at time and qual (`if s in ():`) | KILLED: the five-case pass-1 check FAILs (the task_correct case "ran") |
| M04 | assertion on the contrast rows (wrong arm) | KILLED: the synthetic collect STOPs, "ran to its end" FAILs |
| M05 | `CALLS_REL` path changed | KILLED: the "nine checkpoints and nine call logs by exact path" check FAILs |
| M06 | `log_consistency_problems` without `gate=s` | KILLED: STOP at OLMo-sft / qual, "ran to its end" FAILs |
| M07 | orphan STOP dropped | expected to SURVIVE (re-run STOP fires instead; finding 2) |
| M08 | re-run STOP dropped | KILLED: the call-log pass-1 check FAILs (re-run case "ran") |
| M09 | attribute_calls problems STOP dropped | expected to SURVIVE (orphans STOP instead; finding 2) |
| M10 | calls per session = recorded rounds (wrong set) | KILLED: the "contrast round with no call" check FAILs |
| M11 | calls per session over the sham arm | KILLED: the proxy check and the proxy_cells check FAIL |
| M12 | every arm's cells over the sham rounds | KILLED: the proxy check and the proxy_cells check FAIL |
| M13 | `_spans` run-end off-by-one | expected to SURVIVE (finding 8) |
| M14 | call events printed in place of the log's digest | KILLED: the proxy check's no-index/seed/digest condition FAILs |
| M15 | STOP rows taken from the log's call events | KILLED: the proxy check FAILs |
| M16 | attribution_complete check inverted | KILLED: the synthetic collect STOPs, "ran to its end" FAILs |

**Not opened or run.** I ran no Python. I opened, listed and searched nothing under `data/p/ckpt`, `data/p/verdicts`, `data/p/reports` or `data/mf3`. I ran no whole-tree `git status`. My only content searches were `git grep` over `valence_core/m` and `valence_core/p`, with item 3's exclusion pathspec. The only files I wrote are this report and `mutants/mutants_r2.json`.

## 2. Code's dispositions

The review found no MAJOR. Each MINOR and each NOTE is disposed of as follows: each applied but finding 6, answered with no change. The review's line numbers are the reviewed version's.

1. **MINOR, the call log bound to its report: applied, the check as given, placed before `read_calls` (the review placed it after the changed-while-read check).**
   - Pass 1 checks the report's `call_log.sha256` and `call_log.path` against the log's bytes and p's path form. It does this right after reading those bytes and before `read_calls`.
   - In the self-test:
     - each synthetic report records the path and the sha256;
     - `edit_log` and `append_line` re-record an edited log's sha256;
     - a new case, "an unrecorded log", STOPs with "does not record".
   - The reading the finding puts to the seat is declared in the docstring as Code's reading: a contrast round with no attributed call is printed, not stopped. The printed case's check names it so.
2. **MINOR, which STOP fired: applied.**
   - `stops_silently` returns the STOP's message, and each case asserts its own text: the reviewer's table, made exact (its malformed row now finding 4's message, "not JSON" asserted absent from every message), with the five earlier cases given theirs too.
   - New cases:
     - a round with no int seed, its call removed;
     - a contrast session index `"1"`;
     - a contrast session twice;
     - a log whose bytes change while p's `read_calls` reads it (p's function wrapped, and restored in a `finally`).
3. **MINOR, the synthetic log not in p's form: applied.**
   - The run, call and end lines are in p's form: `"call": n`, and cut events with `returned_text` carrying `SENTINEL` and `stored_text` the round's text.
   - The proxy check asserts that `SENTINEL` and `"call"` never print.
   - A STOP call line in proxy.py's form (seed 999, `"stop"` carrying `SENTINEL`) STOPs as an orphan, with no `SENTINEL` in its message.
4. **MINOR, malformed lines: applied, the reviewer's second option.**
   - A STOP fires only when the log's malformed-line count, or its `well_formed`, differs from what the report records.
   - The count is printed. Every one of the nine reports records 0 at this writing; Code read their `call_log` fields with `jq`, the reports being the read domain.
   - The STOP message prints counts, never a line's position. This also covers finding 10.
5. **NOTE, the STOP label: applied.**
   - The line reads "STOP marks in the p report's run rows".
   - The docstring says that a STOP's message, where one exists, is the stage entry's verbatim quote.
6. **NOTE, the re-run STOPs on a resumed session: no change.**
   - Each of the nine reports records `call_log.n_runs` 1, no STOP mark, `well_formed` true and 0 malformed lines.
   - Code read only those fields, with `jq`.
7. **NOTE, the ruling raw's pin: applied.**
   - `load_ruling(raw=None)`, with a refusal case (the raw plus a newline).
   - Gate 4 now requires the ruling raw, as well as the script, to be committed at HEAD. The raw was committed by path at `52b2c97`.
8. **NOTE, `_spans`: applied.** A run ending at the last index is now tested.
9. **NOTE, the check's name: applied.** It now reads "against the hand-computed sham cells (build_report's rule)".
10. **NOTE, line numbers in STOP lines: applied with 4.**

**The mutants.**
- Each mutant's `old` text was re-counted against the fixed script with `/usr/bin/grep -o -F`. Each occurs exactly once, so none needed re-anchoring.
- They were run by `<scratchpad>/mutants/run_mutants.py` (below). Each mutant runs once through the script's self-test, as a fresh module whose `__file__` is the script's path. The script file is never written.
- A baseline runs first and must pass.

**The run (§4 below):**
- Baseline PASS; 16 killed, 0 survived, 0 invalid. The three the review expected to survive (M07, M09, M13) are killed by the fixes for findings 2 and 8.
- One observation, with no change. Under M11 and M12 the proxy check fails cleanly. Then the `proxy_cells` check's failure report cannot render its GOT value, because the per-session cells are keyed by tuples, which JSON does not take. So the self-test raises a TypeError, which its own wrapper records as the FAIL "the self-test ran to its end without raising".
- The mutant is killed either way. The rendering matters only on a failing self-test, which closes gate 5 before any record is read.

## 3. The mutants, verbatim (`mutants_r2.json`, sha256 `fc31a0ab89fbc38a4b74848587ff73d8bc7dee456b0bbd0c8fed094c118398b1`)

```json
[
  {
    "id": "M01",
    "what": "R1: TC_STAGES drops the campaign (task_correct back to the gate stages only)",
    "old": "TC_STAGES = (\"time\", \"qual\", \"campaign\")",
    "new": "TC_STAGES = (\"time\", \"qual\")",
    "expect": "KILLED: FAIL 'the seat's second ruling: ... TC_STAGES every stage ...' (TC_STAGES != STAGES) and FAIL 'the run's two passes on synthetic checkpoints ...' (task_correct printed at 6 stages, not 9)"
  },
  {
    "id": "M02",
    "what": "R1: the sham task_correct assertion applied at the campaign too",
    "old": "if s in committed_tc:",
    "new": "if True:",
    "expect": "KILLED: the synthetic collect raises KeyError('campaign') at OLMo-sft / campaign, so FAIL 'the self-test ran to its end without raising' (the later checks never run)"
  },
  {
    "id": "M03",
    "what": "R1: the sham task_correct assertion skipped at time and qual (tc_asserted still printed as 'equal')",
    "old": "if s in committed_tc:",
    "new": "if s in ():",
    "expect": "KILLED: FAIL 'pass 1 STOPs before anything is printed: a p report not recording its checkpoint's sha256, ... a sham task_correct row off its committed figure, ...' (the bad_tc case returns 'ran')"
  },
  {
    "id": "M04",
    "what": "R1, wrong arm: the gate-stage assertion compares the contrast rows to the committed sham figure",
    "old": "if {ph: tuple(rows[\"sham\"][ph]) for ph in PHASES} != committed_tc[s][u]:",
    "new": "if {ph: tuple(rows[\"contrast\"][ph]) for ph in PHASES} != committed_tc[s][u]:",
    "expect": "KILLED: the synthetic collect STOPs at OLMo-sft / time (contrast 2/2 forced, 0/2 free against the committed 1/2, 2/3), so FAIL 'the self-test ran to its end without raising'"
  },
  {
    "id": "M05",
    "what": "R2: the call-log path changed (not p's ckpt/{U}_{gate}_p-calls.jsonl)",
    "old": "CALLS_REL = \"data/p/ckpt/{unit}_{stage}_p-calls.jsonl\"",
    "new": "CALLS_REL = \"data/p/ckpt/{unit}_{stage}_calls.jsonl\"",
    "expect": "KILLED: FAIL 'the run reads nine checkpoints and nine call logs by exact path, each unit's time, qual and campaign' (the synthetic roots follow the constant, so only this check sees it)"
  },
  {
    "id": "M06",
    "what": "R2, the stage pattern: log_consistency_problems called without the stage (p's default gate, time)",
    "old": "cons = p_stage.log_consistency_problems(u, events, gate=s)",
    "new": "cons = p_stage.log_consistency_problems(u, events)",
    "expect": "KILLED: the synthetic collect STOPs at OLMo-sft / qual (its run line names G-F0m-OLMo (p), the check now wants G-TIME's), so FAIL 'the self-test ran to its end without raising'"
  },
  {
    "id": "M07",
    "what": "R2, a dropped check: the orphan STOP (a call attributed to no recorded round) never fires",
    "old": "if att[\"n_orphans\"]:",
    "new": "if att[\"n_orphans\"] < 0:",
    "expect": "EXPECTED TO SURVIVE the current self-test: an orphan also makes n_calls exceed len(by_round), so the re-run STOP fires in its place and stops_silently does not check which STOP fired. Not equivalent in output (the STOP line then calls an orphan 'a re-run'); killable by asserting 'attributed to no recorded round' in the log_orphan case's STOP message (review finding 2)"
  },
  {
    "id": "M08",
    "what": "R2, a dropped check: the re-run STOP (two calls matching one round) never fires",
    "old": "if n_calls != len(att[\"by_round\"]):",
    "new": "if n_calls < len(att[\"by_round\"]):",
    "expect": "KILLED: FAIL 'pass 1 STOPs before anything is printed on a call log not as the rule reads it: ...' (the re-run case returns 'ran': the extra call for seed 101 replaces the first in by_round and every cell still equals the report's)"
  },
  {
    "id": "M09",
    "what": "R2, a dropped check: attribute_calls' own problems (a shared seed, a round with no int seed) ignored",
    "old": "if att[\"problems\"]:",
    "new": "if att[\"problems\"] and False:",
    "expect": "EXPECTED TO SURVIVE the current self-test: in the seed_shared case the calls for seeds 203 and 204 both become orphans, so the orphan STOP fires instead; the 'no int seed' problem has no case. Killable by a message check ('p's attribute_calls reports') or a case with a round carrying no int seed and no call (review finding 2)"
  },
  {
    "id": "M10",
    "what": "R2, a cell from the wrong set: calls per contrast session counted as its recorded rounds, not its attributed calls",
    "old": "per_session[sk] = sum(1 for r in rec.get(\"rounds\", ()) if p_report.round_key(rec, r) in att[\"by_round\"])",
    "new": "per_session[sk] = len(rec.get(\"rounds\", ()))",
    "expect": "KILLED: FAIL 'a contrast round with no call is printed, not stopped: ...' (the session prints '4 calls: A0-OLMo-syn s=1', not 3)"
  },
  {
    "id": "M11",
    "what": "R2, wrong arm: calls per session tabulated over the sham sessions instead of the contrast sessions",
    "old": "if _arm(rec) == \"contrast\":",
    "new": "if _arm(rec) == \"sham\":",
    "expect": "KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ...' (the per-session line reads '5 calls: A0s-OLMo-syn s=0') and FAIL 'proxy_cells on the synthetic records ...' (per_session keyed by the sham session)"
  },
  {
    "id": "M12",
    "what": "R2, a cell from the wrong set: every arm's cells computed over the sham rounds",
    "old": "keys = [p_report.round_key(rec, r) for rec in records if _arm(rec) == a for r in rec.get(\"rounds\", ())]",
    "new": "keys = [p_report.round_key(rec, r) for rec in records if _arm(rec) == \"sham\" for r in rec.get(\"rounds\", ())]",
    "expect": "KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ...' (the contrast line reads 5 of 5 with the sham's cut) and FAIL 'proxy_cells on the synthetic records ...'"
  },
  {
    "id": "M13",
    "what": "Off-by-one in _spans: a run of consecutive session indices that ends at the last index is split",
    "old": "while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:",
    "new": "while j + 2 < len(nums) and nums[j + 1] == nums[j] + 1:",
    "expect": "EXPECTED TO SURVIVE the current self-test: no input has a run ending at the last index ('s=0-3, 5', 's=4', 's=1' all print as before); on the record 80 contrast sessions at one count would print 's=0-78, 79'. Killable by a calls_by_count case such as {('A0-x', 0): 4, ('A0-x', 1): 4} -> ['4 calls: A0-x s=0-1 (2 sessions)'] (review finding 8)"
  },
  {
    "id": "M14",
    "what": "A printed field leaking per-call data: two call events printed where the call log's digest belongs",
    "old": "res.update(crel=crel, calls_sha=_sha(cbytes), px=px, n_runs=len(runs),",
    "new": "res.update(crel=crel, calls_sha=json.dumps(events[1:3]), px=px, n_runs=len(runs),",
    "expect": "KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ... no call's index, seed or digest printed' ('index', 'seed' and two rounds' text sha256s in the output)"
  },
  {
    "id": "M15",
    "what": "R2: the STOP rows quoted from the log's call events instead of the p report's run rows",
    "old": "stop_rows=[row for row in (cl.get(\"runs\") or []) if isinstance(row, dict) and row.get(\"stop\")])",
    "new": "stop_rows=[row for row in events if isinstance(row, dict) and row.get(\"event\") == \"call\"])",
    "expect": "KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ...' (no line reads \"the proxy's STOP: none (the p report's run rows)\"; 'seed' and 'index' printed)"
  },
  {
    "id": "M16",
    "what": "A STOP condition inverted: the report's attribution_complete flag check fires when the flag agrees",
    "old": ".get(\"attribution_complete\") is not (not px[\"cells\"][\"sham\"][\"unattributed_keys\"]):",
    "new": ".get(\"attribution_complete\") is (not px[\"cells\"][\"sham\"][\"unattributed_keys\"]):",
    "expect": "KILLED: the unmodified synthetic root STOPs at OLMo-sft / time, so FAIL 'the self-test ran to its end without raising'"
  }
]
```

## 4. The mutants' run, verbatim (`result_r2.txt`, sha256 `fbe975ac78abbb04de1822bf15bf4f6a37685e0a5e8105e01681b89f496a2201`; the runner's exit 0, stderr empty)

```
script sha256 a87749e9c296ddc7c8e79ab3a50a74138ccec83d42b4217d6805bfef1d53d6f6; 16 mutant(s)
baseline: PASS (selftest rc 0; 0 FAIL line(s))
M01: KILLED (selftest rc 1; 2 FAIL line(s): [FAIL] the seat's second ruling: results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md at its sha256 (aea918c5f6f37452…), other bytes refused; RU; [FAIL] the run's two passes on synthetic checkpoints: nine stages checked, then printed, each with its counts, its withheld cells and task_correct at every stag) -- R1: TC_STAGES drops the campaign (task_correct back to the gate stages only); expected: KILLED: FAIL 'the seat's second ruling: ... TC_STAGES every stage ...' (TC_STAGES != STAGES) and FAIL 'the run's two passes on synthetic checkpoints ...' (task_correct printed at 6 stages, not 9)
M02: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] the self-test ran to its end without raising  GOT "KeyError: 'campaign'") -- R1: the sham task_correct assertion applied at the campaign too; expected: KILLED: the synthetic collect raises KeyError('campaign') at OLMo-sft / campaign, so FAIL 'the self-test ran to its end without raising' (the later checks never run)
M03: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] pass 1 STOPs before anything is printed, each with its own message: a p report not recording its checkpoint's sha256, a read-domain cell that differs, a ) -- R1: the sham task_correct assertion skipped at time and qual (tc_asserted still printed as 'equal'); expected: KILLED: FAIL 'pass 1 STOPs before anything is printed: a p report not recording its checkpoint's sha256, ... a sham task_correct row off its committed figure, ...' (the bad_tc case returns 'ran')
M04: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] the self-test ran to its end without raising  GOT "Stop: STOP: OLMo-sft time: the sham task_correct recount is not the committed figure") -- R1, wrong arm: the gate-stage assertion compares the contrast rows to the committed sham figure; expected: KILLED: the synthetic collect STOPs at OLMo-sft / time (contrast 2/2 forced, 0/2 free against the committed 1/2, 2/3), so FAIL 'the self-test ran to its end without raising'
M05: KILLED (selftest rc 1; 3 FAIL line(s): [FAIL] the run reads nine checkpoints and nine call logs by exact path, each unit's time, qual and campaign  GOT [["data/p/ckpt/OLMo-sft_time.json", "data/p/ckp; [FAIL] pass 1 STOPs before anything is printed on a call log not as the rule reads it, each with its own message: a log its report does not record, a call attri; [FAIL] pass 1 STOPs, printing nothing, when a call log's bytes change while p's read_calls reads it (p's read_calls restored after)  GOT "ran") -- R2: the call-log path changed (not p's ckpt/{U}_{gate}_p-calls.jsonl); expected: KILLED: FAIL 'the run reads nine checkpoints and nine call logs by exact path, each unit's time, qual and campaign' (the synthetic roots follow the constant, so only this check sees it)
M06: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] the self-test ran to its end without raising  GOT "Stop: STOP: data/p/ckpt/OLMo-sft_qual_p-calls.jsonl is not this stage's: [\"run line 1: not this stage) -- R2, the stage pattern: log_consistency_problems called without the stage (p's default gate, time); expected: KILLED: the synthetic collect STOPs at OLMo-sft / qual (its run line names G-F0m-OLMo (p), the check now wants G-TIME's), so FAIL 'the self-test ran to its end without raising'
M07: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] pass 1 STOPs before anything is printed on a call log not as the rule reads it, each with its own message: a log its report does not record, a call attri) -- R2, a dropped check: the orphan STOP (a call attributed to no recorded round) never fires; expected: EXPECTED TO SURVIVE the current self-test: an orphan also makes n_calls exceed len(by_round), so the re-run STOP fires in its place and stops_silently does not check which STOP fired. Not equivalent in output (the STOP line then calls an orphan 'a re-run'); killable by asserting 'attributed to no recorded round' in the log_orphan case's STOP message (review finding 2)
M08: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] pass 1 STOPs before anything is printed on a call log not as the rule reads it, each with its own message: a log its report does not record, a call attri) -- R2, a dropped check: the re-run STOP (two calls matching one round) never fires; expected: KILLED: FAIL 'pass 1 STOPs before anything is printed on a call log not as the rule reads it: ...' (the re-run case returns 'ran': the extra call for seed 101 replaces the first in by_round and every cell still equals the report's)
M09: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] pass 1 STOPs before anything is printed on a call log not as the rule reads it, each with its own message: a log its report does not record, a call attri) -- R2, a dropped check: attribute_calls' own problems (a shared seed, a round with no int seed) ignored; expected: EXPECTED TO SURVIVE the current self-test: in the seed_shared case the calls for seeds 203 and 204 both become orphans, so the orphan STOP fires instead; the 'no int seed' problem has no case. Killable by a message check ('p's attribute_calls reports') or a case with a round carrying no int seed and no call (review finding 2)
M10: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] printed, not stopped (Code's reading of the sham cells' form): a contrast round with no call -- at that stage the contrast cell reads 3 of 4 attributed w) -- R2, a cell from the wrong set: calls per contrast session counted as its recorded rounds, not its attributed calls; expected: KILLED: FAIL 'a contrast round with no call is printed, not stopped: ...' (the session prints '4 calls: A0-OLMo-syn s=1', not 3)
M11: KILLED (selftest rc 1; 2 FAIL line(s): [FAIL] the proxy (R2 (b)) on synthetic call logs in p's form, through p's attribute_calls: at all nine stages the log bound to its report by sha256, the sham ce; [FAIL] the self-test ran to its end without raising  GOT "TypeError: keys must be str, int, float, bool or None, not tuple") -- R2, wrong arm: calls per session tabulated over the sham sessions instead of the contrast sessions; expected: KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ...' (the per-session line reads '5 calls: A0s-OLMo-syn s=0') and FAIL 'proxy_cells on the synthetic records ...' (per_session keyed by the sham session)
M12: KILLED (selftest rc 1; 2 FAIL line(s): [FAIL] the proxy (R2 (b)) on synthetic call logs in p's form, through p's attribute_calls: at all nine stages the log bound to its report by sha256, the sham ce; [FAIL] the self-test ran to its end without raising  GOT "TypeError: keys must be str, int, float, bool or None, not tuple") -- R2, a cell from the wrong set: every arm's cells computed over the sham rounds; expected: KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ...' (the contrast line reads 5 of 5 with the sham's cut) and FAIL 'proxy_cells on the synthetic records ...'
M13: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] calls_by_count groups the sessions by their number of calls, every index kept: 10 calls for s=0-3 and 5, 7 for s=4; a run ending at the last index stays ) -- Off-by-one in _spans: a run of consecutive session indices that ends at the last index is split; expected: EXPECTED TO SURVIVE the current self-test: no input has a run ending at the last index ('s=0-3, 5', 's=4', 's=1' all print as before); on the record 80 contrast sessions at one count would print 's=0-78, 79'. Killable by a calls_by_count case such as {('A0-x', 0): 4, ('A0-x', 1): 4} -> ['4 calls: A0-x s=0-1 (2 sessions)'] (review finding 8)
M14: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] the proxy (R2 (b)) on synthetic call logs in p's form, through p's attribute_calls: at all nine stages the log bound to its report by sha256, the sham ce) -- A printed field leaking per-call data: two call events printed where the call log's digest belongs; expected: KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ... no call's index, seed or digest printed' ('index', 'seed' and two rounds' text sha256s in the output)
M15: KILLED (selftest rc 1; 2 FAIL line(s): [FAIL] the proxy (R2 (b)) on synthetic call logs in p's form, through p's attribute_calls: at all nine stages the log bound to its report by sha256, the sham ce; [FAIL] printed, not stopped (Code's reading of the sham cells' form): a contrast round with no call -- at that stage the contrast cell reads 3 of 4 attributed w) -- R2: the STOP rows quoted from the log's call events instead of the p report's run rows; expected: KILLED: FAIL 'the proxy (R2 (b)) on synthetic call logs ...' (no line reads "the proxy's STOP: none (the p report's run rows)"; 'seed' and 'index' printed)
M16: KILLED (selftest rc 1; 1 FAIL line(s): [FAIL] the self-test ran to its end without raising  GOT "Stop: STOP: OLMo-sft time: data/p/reports/OLMo-sft_time_p-report.json's attribution_complete does not ) -- A STOP condition inverted: the report's attribution_complete flag check fires when the flag agrees; expected: KILLED: the unmodified synthetic root STOPs at OLMo-sft / time, so FAIL 'the self-test ran to its end without raising'
summary: 16 killed, 0 survived, 0 invalid, baseline PASS
```

## 5. The runner, verbatim (`run_mutants.py`, sha256 `6c69daa76d3c09c9a79d9eb23a8e67efe59f2c73356b54baf96e4cee3914f9b9` before the root was shown as `<repo>`)

```python
"""Run the counters script's self-test once per mutant (scratch tool; runs only inside a battery window).

Each mutant is {"id", "what", "old", "new", "expect"}: ``old`` must occur exactly once in the script's committed-to-be
source; the mutated source is executed as a fresh module whose ``__file__`` is the real script's path (so REPO and
every repository path resolve as in the real run), and its ``run_selftest()`` is called with stdout captured. A mutant
is KILLED iff the self-test returns non-zero or raises; SURVIVED iff it returns 0. A baseline (no change) runs first
and must pass. The script file itself is never written. Prints one line per mutant and a summary; exit 0 iff the
baseline passed and every valid mutant was killed.

Usage: python -B run_mutants.py MUTANTS.json OUT.txt
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import sys
import types
from pathlib import Path

REAL = Path("<repo>/scripts/p_verdicts_counters.py")


def run_one(src: str) -> tuple[str, str]:
    mod = types.ModuleType("p_verdicts_counters_mutant")
    mod.__file__ = str(REAL)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, str(REAL), "exec", dont_inherit=True), mod.__dict__)
            rc = mod.run_selftest()
        verdict = "SURVIVED" if rc == 0 else "KILLED"
        how = f"selftest rc {rc}"
    except BaseException as e:                      # noqa: BLE001  a raise kills the mutant
        verdict, how = "KILLED", f"raised {type(e).__name__}"
    fails = [ln.strip() for ln in buf.getvalue().splitlines() if ln.strip().startswith("[FAIL]")]
    tail = "; ".join(f[:160] for f in fails[:3])
    return verdict, f"{how}; {len(fails)} FAIL line(s){': ' + tail if tail else ''}"


def main() -> int:
    muts = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path(sys.argv[2])
    src0 = REAL.read_text(encoding="utf-8")
    lines = [f"script sha256 {hashlib.sha256(src0.encode('utf-8')).hexdigest()}; {len(muts)} mutant(s)"]
    base, how = run_one(src0)
    lines.append(f"baseline: {'PASS' if base == 'SURVIVED' else 'FAIL'} ({how})")
    ok = base == "SURVIVED"
    n_k = n_s = n_inv = 0
    for m in muts:
        c = src0.count(m["old"])
        if c != 1:
            n_inv += 1
            lines.append(f"{m['id']}: INVALID (its 'old' text occurs {c} times) -- {m['what']}")
            continue
        verdict, how = run_one(src0.replace(m["old"], m["new"], 1))
        n_k += verdict == "KILLED"
        n_s += verdict == "SURVIVED"
        lines.append(f"{m['id']}: {verdict} ({how}) -- {m['what']}; expected: {m.get('expect', '')}")
    lines.append(f"summary: {n_k} killed, {n_s} survived, {n_inv} invalid, baseline "
                 f"{'PASS' if ok else 'FAIL'}")
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if ok and n_s == 0 and n_inv == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```
