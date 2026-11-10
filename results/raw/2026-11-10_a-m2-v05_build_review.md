# ADDENDUM-m2 v0.5's build — the blind review, two rounds

*Code's raw, PI date 2026-11-10.*
- *What was reviewed:* the build of A-m2 v0.5 §4.2 in Code's scratch worktree, checked out at `7589c1d` with uncommitted edits to 11 files: `scripts/mf3_sessions.py` and `valence_core/mf3/{banner,gshape,lines,readrule,resume,runner,scaffold,stages,testing,verify}.py`.
- *How:* two blind agents, read-only, each under a brief quoting the list of record v2's items 1–5 as written.
  - Round 1 reviewed the edits against v0.5 §1, §3.4 and §4.1–§4.3, and `ans5:` §1–§2.
  - Round 2 graded round 1's findings against the fixed code and looked for new defects.
- *Outcome:*
  - Round 1: 11 findings, 0 BLOCKER, 3 MAJOR, 8 MINOR.
  - Round 2: findings 1–10 RESOLVED; finding 11 NOT RESOLVED by design (deferred to the BUILD entry), its
    single-problem failure verified; 3 new findings, all MINOR.
  - Every finding is applied, or recorded (11), each re-checked at source.
  - The self-test after round 2's fixes: 180/182; the two red checks are the ones finding 11 names.
- *This raw:* Code's dispositions of both rounds, then both reports verbatim, extracted by script from each agent's hand-back. In round 2's report, the worktree's local root is replaced by `<scratch>`.
- *The reviewers' compliance:* each reports no departure.
  - Each reports that the driver's self-test's `tree_state` hashes every file under the worktree's `data/mf3`, ckpt and reports included, and prints only the comparison (round 1: sha256, before and after the run).
  - Code reads that as item 1's digest form; it is disclosed for the seat (item 8) in the dispositions.
- *Nothing ran on a model.*

## Code's dispositions, round 1 (each re-checked at source)

- **1, MAJOR: counter (b)'s table key had no path, so a G-ID-F3 pair's two members collided.** Agreed.
  - Applied: each candidate carries the record's `path`, and `tabulate_b` keys on (stage, template, s, path, phase, idx). Two records under one (stage, template, s, path) are refused.
  - Self-test: a G-ID-style pair counts both members' items, and a duplicate record is refused.
- **2, MAJOR: `b_candidates` failed open on a round with no audit mapping.** This mattered on G-TIME-F3's contrast reads, whose forced rounds keep `{phase, ri, n, text}` only (ruling (h)). Agreed.
  - Applied: a round with no audit mapping is refused, so the domain fails closed. The one exception is G-TIME-F3's contrast read.
  - In that read the claimed round follows from `m.audit.qwen_ends`, "forced -> any claim" under the lenient scope: a forced claim ends the session, so the only claimed round is the last one generated in a session the read marks `excluded_at_forced`. That is Code's reading, declared as a PIN at the function.
  - Self-test: an excluded session, a clean one, and a redacted round in any other form, which is refused.
  - Not taken: round 1's further proposed fix, having the stage write (b)'s scoped candidate set into its report (round 2 judged it unneeded). That would add a field to G-TIME-F3's report, whose form ruling (h) fixes, while the read-based form needs no new field.
  - For the seat: Code's reading of `qwen_ends` here, and whether the seat wants the stage to write (b)'s domain itself (round 1's further proposed fix; its interaction with ruling (h) is the seat's to rule).
- **3, MAJOR: a test that could not fail.** Counter (a) on a contrast session's line 1 was compared with the function under test. Agreed.
  - Applied: two scripted G-F3 A3 sessions with fixed expected counts. In one, line 1 is clean and line 3 reproduces the COMMON line: count 0. In the other, line 1 reproduces it: count 1.
- **4, MINOR: the driver's wiring PIN still said "reasoning cap 60".** Agreed.
  - Applied: "60 at the first run (m:174), 120 from the re-run on (A-m2 v0.5 §4.1; the PIN below)".
- **5, MINOR: F29's sentence ("the analyzer reads it at VERDICTS") stood in the review counter's PIN.** Agreed.
  - Applied: restated per v0.5 §3.4. At VERDICTS the analyzer is untouched, and Code tabulates the counter with mf3's functions in its own step.
- **6, MINOR: the boundary PIN described F-0's "\n\n".** Agreed.
  - Applied: restated for F-b, where an empty line leaves "So far," and then its joiner's "\n".
- **7, MINOR: a stub stage start did not check the addendum's bytes.** Agreed.
  - Applied: `startup_problems` now checks the working tree's addendum against its pinned sha256 and literals at every stage start, the stub's included. A non-stub start's licence (h) also requires the file committed.
  - G-ANL-F3's battery re-runs on the final bytes in the site check.
- **8, MINOR: `cap_trigger`'s `cap` defaulted to None, which gives v0.1's semantics.** Agreed.
  - Applied: `cap` is a required keyword.
- **9, MINOR: every scripted runner case ran at 120.** Agreed.
  - Applied: one case runs at 60 (the stub path's cap) and the rest at 120. The runner check that compares the adapter's `max_tokens` with each record's own cap now tells them apart.
- **10, MINOR: the first-run refusal was reached only by patching a constant.** Agreed.
  - Applied: two precheck cases.
    - The re-run's name as a link to the first run's checkpoint is refused, exit 2.
    - The first run's ENDED checkpoint at its own name beside the re-run's is the state at the re-run. That case passes to the loader trap with its bytes unchanged.
- **11, MINOR: two driver checks are red by construction until the lock's re-issue.** Agreed; recorded rather than changed.
  - Each fails on one problem, the committed `LOCK-m-F3.md` not naming the build's mf3 package sha256. Check 1 fails on that problem among its planted lock's expected ones.
  - They pass at LOCK-m-F3 v0.1's re-issue, where Code re-runs the self-test.
- **The note on the lock's re-issue.** This is carried to that step, not this build:
  - the re-issue names the committed build's package hash;
  - it keeps v0.1's text verbatim;
  - it adds no second WEIGHTS line and no second sha256 for any m file;
  - licence (f) is a substring test, so it cannot tell the old package hash from the new; (e) and the ENDED first-run checkpoint still stop the old driver.
- **The reviewer's compliance note: the self-test's `tree_state` sha256-hashes every file under `data/mf3`, checkpoints and reports included.** It does so before and after the time cases, unchanged since `acde2d8`, and prints only the comparison.
  - Code reads this as item 1's digest form: a program's digest that prints no byte, size or time.
  - Disclosed for the seat under item 8, in case the seat reads it otherwise.

## Code's dispositions, round 2 (each re-checked at source)

- **Findings 1–10:** RESOLVED, as round 2 grades them. Three residuals it notes are applied:
  - 3: the stage-report check's old conjunct, which still compared the report with the function under test over (a)-negative lines, is removed; the fixed-count check covers it;
  - 4: the stray comment line the edit left in the driver's wiring PIN is joined;
  - 8: `prior_gate` refuses a prior whose identity carries no integer reasoning cap ("PRIOR STAGE MALFORMED"), rather than reading it with v0.1's count.
- **Finding 11:** recorded, as declared. Round 2 verified that each red check fails on one problem, the committed lock not naming mf3's package sha256.
- **N1, MINOR: banner's PIN named the licence as the every-start site.** Agreed. Applied: it names `stages.startup_problems` (the working tree's bytes against the pin, stub included), with the licence's (h) adding the committed-at-HEAD check on a non-stub start.
- **N2, MINOR: no test for finding 7's fix.** Agreed. Applied: stages' self-test plants an addendum problem and a segment problem; `startup_problems` carries each, and a stub G-TIME-F3 stops with STARTUP CHECKS FAIL, writing no checkpoint.
- **N3, MINOR: counter (b)'s G-TIME-F3 branch was tested only on a hand-built dict.** Agreed. Applied: readrule's self-test compares `b_candidates` over `strip_contrast`'s real G-TIME-F3 read with the full record's unclaimed forced rounds, for the three contrast sessions of its G-TIME-F3 run and one session excluded at its second forced round.
- **Round 2's notes for later steps:**
  - PINs revised in place under their earlier "declared at" tags: F29's site (`lines.py`), `_extra`'s docstring PIN, `out_paths`, `assert_boundary` and the driver's wiring PIN. They are carried to LOCK-m-F3 v0.1's re-issue, whose register or dated notes will mark them.
  - G-SHAPE-F3's canonical artifact is write-once, and the committed one (`data/mf3/gates/G-SHAPE-F3.json`, lock:97) must be superseded before the re-run writes the new one. That is the re-run's step.
- **The self-test after round 2's fixes:** 180/182, the two red checks finding 11 names.

## Round 1's report (verbatim)

# Blind review: the A-m2 v0.5 build in W (11 files)

**W HEAD:** `7589c1d` at start and at end. `git status --porcelain` was the same at start and end: the 11 `M` files, plus an untracked `HANDOFF-2026-09-04-design.md` that is not part of the build. Keep that file out of the build's commit.

**Protected files and scope:**
- `scripts/m_analyze.py` (sha256 `d347ea0c…`), `valence_core/m/banner.py`, `valence_core/m/audit.py` and every other `valence_core/m` file have no diff. The self-test reports m's package hash at `7756dcf4…`.
- The files that moved are exactly v0.5 §4.2's list.
- The driver's `git diff acde2d8` shows only the v0.5 edits. `9c7062e` was additions only, so the restoration is exact.

**What I ran:**
- The brief's self-test: 176/178 PASS, about 68 s.
- One stdlib `python3 -I` computation of `package_sha256_of`'s rule over the HEAD blobs and over the worktree.
- No model, no analyzer, no battery. G-ANL-F3's battery on the build is still Code's step.

## The 176/178 claim: correct, with conditions

- **Both failures are one problem:** `lock LOCK-m-F3.md: its committed text does not name package_sha256 fe529f314b2a6ff6...`.
  - Check 2 prints exactly that problem.
  - Check 1 fails its "nothing for (f)" conjunct on the same problem.
- **The hashes:** HEAD's mf3 package is `f30ad5053904ac22…`, which is the lock's own value (`LOCK-m-F3.md:96`). The worktree's is `fe529f314b2a6ff6…`.
- **Nothing else in either check depends on the old lock text.** The m-file lines, the WEIGHTS line, the proposal sha and the analyzer sha are unchanged, and (h) passes on `7589c1d`.
- **The order is right.** v0.5 §4.3 places the re-issue after the build's commit and after the G-SHAPE-F3 and G-ANL-F3 re-runs, so these checks can only turn green there.
- **Conditions:**
  - (i) The re-issued lock must name the hash of the bytes actually committed. Any fix from this review moves that hash.
  - (ii) The re-issue keeps v0.1's text verbatim. It must not add a second, different WEIGHTS line or a second sha256 for any of the eleven m files, or `time_identity_extra` refuses.
  - (iii) Until then the two checks are red by construction (finding 11).
- **Note on the re-issue (outside the 11 files):** the re-issued lock will name both `f30ad505…` and the new hash. Licence (f) is a substring test, so (f) alone will no longer tell the old package from the new one. Check (e) and the ENDED first-run checkpoint still stop the old driver.

## Findings

**1. MAJOR — `valence_core/mf3/lines.py:209–228` (the key is at :216).** Counter (b)'s table is keyed on (stage, template, s, phase, idx).
- **What is wrong:** at G-ID-F3 both members of a pair carry the same stage, template and s.
  - `_launch` passes s = j for both members.
  - The pair loop itself keys records on (template, s, path), `stages.py:1266`, `:1271–1278`.
- **Effect:**
  - The cached member's candidates overwrite the uncached member's.
  - If Code lists the same round in both members, the second is refused as "listed twice".
  - On a G-ID-F3 PASS (byte-identical pairs) every (b) response occurs in both members, so the table can hold at most half of them.
- **Spec:** §3.4 requires (b) "for every Q-F3 stage from the re-run on", "tabulated over all sessions". All of G-ID-F3's sessions are sham, so all are in scope.
- **Fix:** carry `path` in `b_candidates`' items and in the key. Add a self-test case with an identical G-ID-style pair.

**2. MAJOR — `lines.py:197–206` (`b_candidates`), as applied at G-TIME-F3.** `b_candidates` fails open: a round with no `audit` mapping counts as unclaimed (`(r.get("audit") or {}).get("claim") is None`).
- **Why this matters at the re-run:** before VERDICTS, Code may read only the reports and reads. At G-TIME-F3 (the re-run, the next run of record) each contrast forced round in the reads is `{phase, ri, n, text}`, with audit and claim withheld.
  - The withheld set is `TIME_WITHHELD`, `m/readrule.py:162–167`.
  - The stage enforces it in `stages._assert_time_form`, `stages.py:1065–1093`.
- **Effect:**
  - On those reads, `b_candidates` returns every contrast forced round, including a claimed one.
  - `tabulate_b`'s refusal ("is not a response no audit class claims") cannot fire there.
  - No code computes (b)'s domain within §3.4's pre-VERDICTS scope (sham rounds; contrast forced rounds) from the full records, and neither the report nor the reads carries it.
- **Spec:** §3.4: "(b) task responses … that no audit class claims"; "a gate stage's entry reports … (b) over its sham sessions' rounds and its contrast sessions' forced rounds".
- **Fix:**
  - Make `b_candidates` refuse a round that has no audit mapping.
  - Have the stage's own code write the scoped candidate set in a declared form.
  - At G-TIME-F3, derive the unclaimed contrast forced rounds from `excluded_at_forced`. Under the lenient scope any forced claim ends the session (`m_audit.qwen_ends`), so only the last forced round of an excluded session can be claimed.
  - The interaction with ruling (h) is the seat's to confirm.
- **Severity:** it could be argued BLOCKER for the re-run's entry. I graded it MAJOR because the counter decides nothing and the seat confirms every item.

**3. MAJOR — `readrule.py:625–626` (in the check opening at :619).** This is a test that cannot fail.
- The conjunct for counter (a) on contrast line 1 compares `reasoning_line_1.counter_a` with `sum(lines.counter_a_of_record(r)[0] …)`, which is the function under test.
- Every A3 reasoning line in the suite is (a)-negative (`testing.LINES`, and `"fine <|im_end|> here"`). So the expected value is 0 and the actual value is 0 for any implementation, including one that also counted later, pick-bearing contrast lines.
- §3.4's blinding scope for (a) on contrast sessions is therefore untested. The code itself, `readrule.py:383–390`, is right today.
- **Fix:** script a G-F3 contrast session whose line 1 is clean and whose line 3 reproduces the session banner, and another whose line 1 is an (a) line. Assert the fixed counts, 0 and 1.

**4. MINOR — `scripts/mf3_sessions.py:88–93` (:91).** The wiring's PIN, which §4.2 cites at `:99–104` at HEAD, still says "reasoning cap 60 (m:174; stages._extra refuses any other at G-TIME-F3)".
- The constant is now 120 (:105), and `_extra` refuses 60 on a model.
- The new PIN at :94–100 sits beside it without superseding it.
- **Fix:** amend that clause, e.g. "60 at the first run; 120 from the re-run (A-m2 v0.5 §4.1), below".

**5. MINOR — `lines.py:240–242` (F29's site).** It says "Its home is this module; the analyzer reads it at VERDICTS (G-ANL-F3)."
- §3.4 corrects F29: the analyzer is untouched, and Code tabulates the Q4 counter "with mf3's functions … in its own step".
- The analyzer has no reference to `review_counter` or `REVIEW_STRINGS` (grep).
- The lock's PIN-site register is generated from these lines, so the re-issue would carry the very sentence its dated note corrects.
- **Fix:** restate the PIN per §3.4.

**6. MINOR — `scaffold.py:176–182` (the `assert_boundary` PIN).** "an empty or newline-led reasoning line and its "\n\n" lie inside a later prefix" describes F-0, whose segment ended in "\n".
- Under F-b an empty line leaves `So far,\n` in the transcript, which `runner.py:250` asserts.
- §4.2 lists scaffold's docstrings among what moves.
- **Fix:** restate the clause for F-b.

**7. MINOR — `stages.py:373–379` with `_licence` at :394–396 (and `banner.py:27–30`).** The addendum's committed bytes, sha256 and literals are checked only in the licence's (h), which is skipped on the stub.
- A stub stage start checks only the segment's roster hygiene (:187).
- §4.2 says "verified at every stage start".
- No run of record is affected: every non-stub start, the driver's precheck and G-SHAPE-F3 all run the check.
- **Fix:** either declare "every non-stub stage start", or add the sha-pinned `banner.addendum_file_problems()` to `startup_problems`. The battery's stub chain would still pass, because v0.5 is committed at `7589c1d`.

**8. MINOR — `stages.py:1020`, `:1038`.** `cap_trigger(records, *, cap=None)`: with the default, a run at 120 whose count is under 3 reports `fixed_cap` 60, which is v0.1's semantics.
- Every present caller passes `cap` (:500, :1110).
- **Fix:** make `cap` required, or raise when it is None.

**9. MINOR — `testing.py:110`, `:139–140`; `runner.py:259–261`, `:275`.** `Case.cap` now defaults to 120, so every scripted runner case runs at 120.
- The "f3 cap-120 A2s start 0" case no longer differs from the others.
- No runner-level case runs a reasoning line at 60, the stub path's cap.
- `runner.py:260` compares `max_tokens` with the record's cap, so a runner that passed `CAP_OF_RECORD` instead of `rs.cap` would pass every check.
- **Fix:** keep one case at 60.

**10. MINOR — `mf3_sessions.py:298–305`; self-test :1071–1085.** `TIME_CKPT_NAME` is a constant, so in production the first-run refusal can only fire when `ckpt/Q-F3_time-r2.json` resolves to `Q-F3_time.json` through a link.
- The self-test reaches the refusal only by patching the constant.
- No case runs `time` with an ENDED `Q-F3_time.json` beside the r2 path. That is the real on-disk state at the re-run.
- **Fix:** add both cases:
  - a planted link r2 → first-run checkpoint, refused at the precheck with exit 2;
  - an ended first-run checkpoint present, where the run reaches the loader trap and the first run's bytes are unchanged.

**11. MINOR — `mf3_sessions.py:714–730`.** At the build's commit the two checks are red by construction (see the claim above). While red they hide any other licence problem they exist to catch, for example (h).
- **Fix:** record them in the BUILD entry as expected-red, each with its single expected problem. Alternatively, have each assert that the licence's only problem is exactly the package line whenever the committed lock names a different mf3 hash.

## Requirements

**v0.5 §4.2**

| # | Requirement | Status | Where |
|---|---|---|---|
| 1 | F-b is rendered from banner's own `REASONING_FORM`/`REASONING_SEGMENT`, `{n}` by `str(n)`, with m's `REASONING_HEADER` as the header | MET | `banner.py:59–60`, `:123–137` |
| 2 | Verified at every stage start against the committed file and its sha256 | PARTLY: non-stub starts only (finding 7) | `stages.py:373–379`, `:394–396`; driver precheck `:325` |
| 3 | Verified in G-SHAPE-F3 against the committed bytes and sha256 | MET | `gshape.py:275–290`; provenance at `:705` |
| 4 | Segment free of roster words, as m:258's eight strings are | MET | `banner.py:201–208`; `stages.py:187`; `gshape.py:288` |
| 5 | Cap of record binds every run on a model; only the stub may run at 60 | MET | rows 6–9, 17 |
| 6 | `_extra`: 120 only on a non-stub run, 60 on the stub only | MET | `stages.py:611–617` |
| 7 | `Identity`: 60 only with the stub's all-zero weights binding; 120 at every stage | MET | `resume.py:50`, `:192–201` |
| 8 | `prior_gate`: the fixed cap is 120 unless `require_real` is off | MET; it also refuses a prior at another cap, declared as Code's reading of F6 (`:495–498`) | `stages.py:486–503` |
| 9 | `f3_config`'s per-stage cap made a table keeping m:174's pair, caller choosing | MET | `scaffold.py:59–61`, `:144–151` |
| 10 | `cap_trigger` keeps its count and reports it | MET (see finding 8) | `stages.py:1020–1041`, `:1141–1153` |
| 11 | `REASONING_CAPS` unchanged | MET | `scaffold.py:52` |
| 12 | The battery's stub chain runs at 60 under F-b; analyzer not edited | MET in code: the chain is reproduced at `stages.py:2046–2069` and the analyzer is unchanged. The battery itself was not run by me. | |
| 13 | Self-test: a non-stub run at 60 is refused by `_extra` and by `Identity` at every stage | MET | `stages.py:2015–2045`; `resume.py:288–315` |
| 14 | Self-test: the driver's `time` at any cap but 120 is refused | MET (60 is the value tested) | `mf3_sessions.py:1078–1085` |
| 15 | Self-test: the stub chain at 60 passes | MET | `stages.py:2046–2069` |
| 16 | `m/banner.py` and `m/audit.py` not edited | MET | no diff |
| 17 | The listed files move, and only they | MET | `git diff --name-status` |
| 18 | lines: §1's builder and equality match replace `echo_lines` and F28's containment | MET | `lines.py:49–100`, `:136–179` |
| 19 | lines: counters (a) and (b) | PARTLY: (a) MET; (b) has findings 1 and 2 | `lines.py:182–228`; `readrule.py:373–392` |
| 20 | lines: F25 and F28 re-declared | MET | `lines.py:52–61`, `:155–158` |
| 21 | runner: the domain is built from the log's pieces | MET | `runner.py:164–173` |
| 22 | verify: G-VER re-derives the classes with the same builder | MET | `verify.py:127–130`; S7 at `gshape.py:572–580` |
| 23 | gshape: its sources map and the F-0 literals | MET | `gshape.py:107–115`, `:843` |
| 24 | scaffold: the cap, self-test bytes and docstrings | PARTLY (finding 6) | `scaffold.py:13–20`, `:52–61`, `:144–151` |
| 25 | Driver: `TIME_REASONING_CAP` is 120 | MET for the value; the PIN text is stale (finding 4) | `mf3_sessions.py:105`, `:285` |
| 26 | Precheck checkpoint is `data/mf3/ckpt/Q-F3_time-r2.json`; an existing or ended one is refused; report and reads are named after it | MET | `mf3_sessions.py:106`, `:298–305`, `:335–347`, `:533`; `stages.py:114–117` |
| 27 | The first run's stem is refused as a target | MET (test coverage: finding 10) | `mf3_sessions.py:302–304` |
| 28 | The stage library keeps m's default stem for the stub | MET | `stages.py:100–111` |
| 29 | `--smoke` retired; bytes restored to `acde2d8`'s | MET | `git diff acde2d8` |
| 30 | The BUILD entry names the files and the DRIVER line's blob | Process step, not checkable in the code | |

**ans5 §1**
- Ruling (a), with 120 binding wherever provenance is real: MET (rows 6–8 and 25).
- The analyzer is untouched: MET.
- A battery group curable only by an analyzer edit is a STOP: a process step, and I did not run the battery. A static read of `_bt_f3_chain` and its two rules (`m_analyze.py:10713–10750`, `:10868–10885`) finds nothing the build breaks.
- `f3_config` and `cap_trigger` forms: MET.
- The r2 path and the first-run refusal sit in the driver's precheck, and the library keeps m's stem: MET.
- The self-test asserts the real side: MET.
- The departure from v0.4 at F8's stub branch and F19's site is the declared form: MET (`stages.py:614`; `scaffold.py:149`).

**ans5 §2**
- `resume.Identity` moves to §1's rule: MET (`resume.py:192–201`).
- Its self-test asserts the real-side refusal: MET (`:288–315`).
- `TIME_REASONING_CAP` 60 → 120: PARTLY. The value is right; the PIN at :91 still says 60 (finding 4).
- The driver self-test follows: MET (`:701–709`).
- The r2 checkpoint, with existing and ended ones refused and the first-run stem refused: MET.
- `--smoke` retired and bytes restored: MET.
- The F-1 kind of edit and the BUILD entry and lock records: process steps.

## §4.3's assertion for the review

Nothing in the build reads the first run's records through readrule's piece check:
- The driver reads and writes only `Q-F3_time-r2.json` (`:298–305`, `:336`, `:533`).
- `prior_gate` reads a prior through `rs.read_checkpoint`, which does no piece check. On a run on a model it refuses a prior at 60 (`stages.py:493–498`).
- `release_full` returns the records unchanged (`readrule.py:537–539`).
- The functions that call `_check_record` (`strip_contrast`, `redact_sham`, `stage_report`) are reached only from the stage's own finish, on the run's own records.
- The self-test asserts that an F-0 record fails the piece check (`readrule.py:559–583`).

## Tally

BLOCKER 0 · MAJOR 3 (findings 1–3) · MINOR 8 (findings 4–11).

## List of record v2: compliance

- My own commands opened, read, listed, sized or traversed nothing under `data/`.
- Every `git grep` carried `':!data/**'`. I ran no recursive grep (grep only on named files) and no `--stat`, `--numstat` or `--shortstat` form.
- The permitted self-test's `tree_state` (`mf3_sessions.py:671–677`, unchanged since `acde2d8`) reads and sha256-hashes every file under W's `data/mf3`, ckpt and reports included, before and after the run. It printed only the comparison result.
- One `git grep` for function names printed `"counter_a": true/false` lines from the committed smoke JSONs under `results/raw`. That path is not under `data/`, and A-m2 §3.2 declares the smoke readable in full.
- I wrote no files and made no git writes.

## Round 2's report (verbatim; local root replaced)

## Round 2 blind review: the A-m2 v0.5 build in W

**Where:** W = <scratch>/v04/build-wt. File paths below are relative to W.

**HEAD:** `7589c1d1635178ca5d45ce223da4b977e1bee33a` at start and at end. `git status --porcelain` was identical at start and end: the 11 `M` files, plus the untracked `HANDOFF-2026-09-04-design.md`, which is not part of the build.

**Self-test:** I ran the brief's command. Result: **178/180 pass**, as the author reports. The only two FAILs are finding 11's checks: `scripts/mf3_sessions.py:718–727` and `:728–731`.

**mf3 package hash:** I recomputed `m_resume.package_sha256_of` with stdlib only.
- The working tree's hash is now **`64a9d18fe1b79b70dd278e1c275a3859921dad9104b0597dab7b5770cd7e29e7`**. The self-test computed the same value in-process.
- HEAD's hash is `f30ad505…`, which is the lock's (`LOCK-m-F3.md:96`).
- Round 1's `fe529f31…` is out of date: the round-2 fixes moved the hash.

### Findings 1–11

| # | Grade | Evidence |
|---|---|---|
| 1 | **RESOLVED** | Each candidate now carries `path` (`lines.py:224–225`). `tabulate_b` keys records on (stage, template, s, path) and refuses a second record under one key (`:236–241`); item keys include path (`:245`). The new self-test check (`:444–451`, `:464–470`) uses an identical G-ID-style pair: both members are counted (2), and a duplicated record is refused. Both of those fail under the old 5-tuple key. |
| 2 | **RESOLVED** | `b_candidates` refuses a round with no audit mapping (`lines.py:218–220`). The one exception is G-TIME-F3's contrast read: stage "time", contrast True, a bool `excluded_at_forced`, and every round forced with no audit (`:210–212`). There, the claimed round is the last forced round when `excluded_at_forced` is true, and none otherwise (`:216–217`). The self-test checks this at `:452–470`. **Judgment: this is a correct reading of `qwen_ends` and the runner** (detail below). |
| 3 | **RESOLVED** | New check at `readrule.py:633–649`: two G-F3 A3 sessions with fixed counts. One reproduces COMMON on line 3, and the report must count 0; the other on line 1, and it must count 1. A report that counted any later contrast line fails it. Residual: the old conjunct at `:625–626` still compares the report against `counter_a_of_record` over a suite whose lines are all (a)-negative, so it still cannot fail. It is now redundant. |
| 4 | **RESOLVED** | `mf3_sessions.py:91` now reads "reasoning cap 60 at the first run (m:174), 120 from the re-run on (A-m2 v0.5 §4.1; the PIN below)". Cosmetic only: the edit left a stub line at `:92` ("# The five flags are the"). |
| 5 | **RESOLVED** | `lines.py:267–269` now says the analyzer is untouched and that Code tabulates with this module's functions in its own step. It cites §3.4's correction of F29. |
| 6 | **RESOLVED** | `scaffold.py:181–183` now describes F-b's empty line ("So far," then the joiner's "\n"). This matches `runner.py:250`. |
| 7 | **RESOLVED** (residuals N1, N2) | `startup_problems` now adds `banner.segment_problems()` and the sha-pinned `banner.addendum_file_problems()` (`stages.py:193–194`; PIN at `:186–189`). `_begin` calls it at every stage start, stub included (`:714`), from `run_gate_stage` (`:975`), `run_gid_pair_f3` (`:1248`) and `run_campaign` (`:1465`). The licence's (h) still adds the committed-at-HEAD check on non-stub starts (`:380–386`). |
| 8 | **RESOLVED** | `cap_trigger(records, *, cap: int)` has no default (`stages.py:1027`). All three callers pass `cap` (`:507`, `:1119`, `:1988–1989`). Note: `:507` passes `ident.get("reasoning_cap")`, so a missing key would still fall back to the count. That is reachable only through a stub prior whose identity lacks the key. |
| 9 | **RESOLVED** | One case, "f3 cap-60 A2s start 0 (the stub path's cap)", now runs at 60 (`testing.py:139–140`; the default is 120 at `:110`). `runner.py:274–279` asserts that case at 60 and every other case at 120. With it, the `max_tokens` comparison at `runner.py:260` fails for a runner that passes `CAP_OF_RECORD`. |
| 10 | **RESOLVED** | Setups at `mf3_sessions.py:1219–1228`. First case: the r2 name is a link to the ended first-run checkpoint. It is refused at the precheck with exit 2 and the test root unchanged (`:1257–1258`; it is in the 36-case table, `:1318`). Second case: the ended first-run checkpoint sits beside the re-run's. The run reaches the loader trap and the first run's bytes are untouched (`:1365–1372`, `rf["same"]`). Loader reaches total 5 (`:1433`). |
| 11 | **NOT RESOLVED** (deferred to the BUILD entry, as the author declared) | Verified: each check fails on exactly one problem, the committed lock not naming mf3's package sha256 (now `64a9d18f…`). Detail below. |

**Finding 2, the judgment in full:**
- **`qwen_ends`:** it is `excludes("lenient")` (`valence_core/m/audit.py:501–506`). For a Qwen forced round that means `claim is not None` (`:361`).
- **How the runner ends a session:** mf3's forced loop excludes on `qwen_ends` and breaks right after that round (`runner.py:151–152`, `:157–158`). A scaffold hit also breaks the loop but sets no exclusion (`:153–156`; m's `hair_trigger` only appends). Nothing else sets an exclusion during the forced loop.
- **So the read's flag is exact:** `excluded_at_forced` (`mf3/readrule.py:199`) is true exactly when the read's last forced round is claimed, and then no other forced round is.
- **G-VER enforces this on every record of record** (`verify.py:196–211`, "the session continued past an event that ends it").
- **Ruling (h):** the derivation uses only fields the read already carries. As round 1 said, the interaction with (h) is still the seat's to confirm.
- **Round 1's other bullet** (have the stage write the scoped candidate set) was not adopted, and it is not needed. With this branch, `b_candidates` over each gate stage's reads gives §3.4's pre-VERDICTS domain:
  - sham reads keep `audit.claim` (`m_rr._AUDIT_KEEP`);
  - contrast reads outside G-TIME-F3 keep their forced rounds in full;
  - G-ID-F3's reads are the full records.

**Finding 11, the verification:**
- **Check 2** (`:728–731`) prints its whole problem list, and it has one entry: `['lock LOCK-m-F3.md: its committed text does not name package_sha256 64a9d18fe1b79b70...']`.
- **Check 1** (`:718–727`) prints only its first 160 characters. They show `pl_probs` `[]`, then the two expected problems: (e′) corr.py, then (g) "binds differently now".
  - `licence_problems` reports in a fixed order, so everything earlier is clean: (a)–(e), the other ten m files, the offline flag and refs/main.
  - The planted lock changes only corr's and the weights' sha256, and `ex_pl` reads both from that lock. So (c) passes, and (f)'s m-file and weights lines match.
  - (h) is clean in check 2, on the same tree.
  - The list is therefore exactly [corr, weights, package]. The failing conjunct is "nothing for (f)", and only because of the package line.
- **Condition:** the BUILD entry must name the hash of the bytes actually committed. Any later edit moves it again.

### New findings

**N1 — MINOR — `valence_core/mf3/banner.py:55–58`**
- **What is wrong:** the PIN says F-b's bytes are "checked against its committed text at every stage start (stages.licence_problems)". `_licence` returns on the stub (`stages.py:401–403`), so `licence_problems` is not an every-start check.
- **Evidence:** since finding 7's fix, the every-start check is `startup_problems` → `addendum_file_problems` (`stages.py:186–194`). It compares the working tree's bytes with the pinned sha256.
- **Fix:** name `startup_problems` as the every-start site, with the licence's (h) adding the committed-at-HEAD check on non-stub starts.

**N2 — MINOR — `valence_core/mf3/stages.py:193–194` (no test for the finding-7 fix)**
- **What is wrong:** no self-test makes `startup_problems` report an addendum or segment problem, or makes a stub stage start refuse on one.
- **Evidence:**
  - banner's self-test tests the two functions on their own (`banner.py:316–344`).
  - stages tests only the licence's (h), on a temp repo (`stages.py:2310–2312`, `:2318–2324`).
  - The driver's "startup" case replaces `startup_problems` wholesale (`mf3_sessions.py:1263–1265`).
  - Deleting both lines would leave all 180 outcomes unchanged.
- **Fix:** in stages' self-test, patch `banner.addendum_file_problems` (or the segment). Assert that `startup_problems()` carries an "addendum:" (and a "segment:") entry, and that a stub `run_gate_stage` stops with STARTUP CHECKS FAIL.

**N3 — MINOR — `valence_core/mf3/lines.py:210–217` with its test at `:452–470`**
- **What is wrong:** the G-TIME-F3 branch is tested only on a hand-built dict.
- **Evidence:**
  - No test feeds it `readrule.strip_contrast`'s real G-TIME-F3 output, although readrule's self-test already builds one (`ts`, `readrule.py:661`).
  - No test compares its candidates with the full record's forced-round candidates.
  - Finding 2's fix depends on that read's exact shape: stage, contrast, a bool `excluded_at_forced`, and forced rounds with no audit.
  - A drift fails closed (a refusal, not a miscount), hence MINOR.
- **Fix:** in readrule's self-test, assert that `b_candidates(strip_contrast(r))`'s (phase, idx) list equals `b_candidates(r)`'s forced entries for each G-TIME-F3 contrast record. Include one excluded at forced, for example "f3 forced v2 ends (no read)" run at stage time.

### Checked and clean
- **v0.5 §4.2 and ans5 §1–§2:** every requirement is met in code. Round 1's PARTLY row ("every stage start") is now met. The battery run and the BUILD entry remain process steps. `m_analyze.py` is unedited and references no renamed test case.
- **Quotes:** every quote of v0.5, ans5 and m:N in the added lines is verbatim. I checked them mechanically against the files; the only differences are markdown emphasis and ASCII for —/≤.
- **§4.3's assertion still holds:** `release_full` checks nothing, `session_line` checks only headers, and the readrule self-test proves an F-0 record fails the piece check.

### Notes for later steps (not graded)
- **The lock's re-issue:** some PIN bodies were edited in place under their original "declared at LOCK-m-F3 v0.1/v0.2" tags:
  - F29, `lines.py:265–269`;
  - `_extra`'s docstring PIN, `stages.py:599–601`;
  - `out_paths`, `stages.py:103–106`;
  - `assert_boundary`, `scaffold.py:181–183`;
  - the driver's wiring PIN, `mf3_sessions.py:91`.

  The re-issue's register or its dated notes should mark them.
- **G-SHAPE-F3's re-run (§4.3):** the canonical artifact is write-once (`gshape.py:731–750`), and `LOCK-m-F3.md:97` records one at `data/mf3/gates/G-SHAPE-F3.json`. The canonical re-run will be refused until that artifact is superseded by hand (PIN-S9). v0.5 §4.3 spells this out for G-ANL-F3's artifact but not for G-SHAPE-F3's.

### Tally
- **Findings 1–11:** RESOLVED 10 (findings 1–10), PARTLY 0, NOT RESOLVED 1 (finding 11, deferred by design; each check fails on exactly one problem).
- **New:** BLOCKER 0 · MAJOR 0 · MINOR 3 (N1–N3).
- **W's HEAD:** start `7589c1d`, end `7589c1d`.

### List of record v2: compliance
- My own commands opened, read, listed, sized and traversed nothing under `data/`.
- Every `git grep` carried `':!data/**'`. I used `grep` only on named files, never recursively. I used no `--stat`, `--numstat` or `--shortstat` form.
- My stdlib scripts (`python3 -I -c`) read only the spec, ans5, the proposal, `LOCK-m-F3.md`, the changed files, and mf3's blobs via `git show`.
- The permitted self-test's `tree_state` (`mf3_sessions.py:672–677`) reads and hashes every file under W's `data/mf3`, ckpt and reports included, and prints only the comparison. I filtered PASS lines out of the output, so I did not view that line.
- I wrote no files and made no git writes. Nothing breached the rule.
