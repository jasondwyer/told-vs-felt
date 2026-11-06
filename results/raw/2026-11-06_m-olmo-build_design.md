# m package — BUILD (OLMo): Code's build design, PIN register and readiness table (2026-11-06)

*Code's raw. The OLMo track's own build, run under the seat's prebuild answers of 2026-11-06 (`results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md`, sha256 `aec58440…4df3`; committed at `dc1ffe1`): §0 ("The OLMo track's first node is therefore its own build — G-CAL-OLMo (b3's banner and generation path) and the OLMo stage wiring — before `BACKEND — characterization`"), Q2 (it lands in `valence_core/m` and `scripts/m_sessions.py` before any `LOCK-m-OLMo-{ckpt} v0.1`) and Q6 (the carry-overs and the weights binding). `m:N` = PROPOSAL-m v1.11 at root. Every reading below is Code's PIN, declared at `LOCK-m-OLMo-{ckpt} v0.1` and strikable by the seat until that lock's v1.0, as at Q-F0's build.*

## 1. Readiness, per stage (ledger (55): read from the driver's wiring and the gate tooling, never from a module's presence)

| stage (m:302) | tooling | state after this build |
|---|---|---|
| respawn (i)–(ii), `BACKEND — characterization` | `scripts/box_respawn_check.py` (the respawn protocol of 2026-08-19, step (i)), `scripts/box_determinism.py` (Phase 0 step 2) | built before this build; unchanged |
| G-CAL-OLMo-{ckpt} | `gcal.run_completability(..., unit="OLMo-{ckpt}")`; driver `gcal completability --unit OLMo-{ckpt}` | **built here** |
| LOCK-m-OLMo-{ckpt} v0.1 | a document; the driver reads it at `time` and `qual` (PIN O14) | to be written after G-CAL-OLMo, per checkpoint |
| G-TIME-OLMo-{ckpt} | `stages.run_gate_stage` (step 4); driver `time --unit OLMo-{ckpt}` | **wired here**; its box path refuses without G-CAL-OLMo's PASS artifact on the weights of record |
| LOCK-m-OLMo-{ckpt} v0.2 | a document (acceptance; projections, m:302); `qual` requires its line `G-TIME-OLMo-{ckpt} port acceptance recorded` (PIN O26) | to be written after G-TIME-OLMo, per checkpoint |
| G-F0m-OLMo-{ckpt} | `stages.run_gate_stage` (step 4); driver `qual --unit OLMo-{ckpt} [--prior-adjudication-file F]` | **wired here**; refuses a lock without v0.2's line `G-TIME-OLMo-{ckpt} port acceptance recorded` |
| G-PWR (OLMo) | `scripts/m_gpwr.py` is Q-F0's | **not built**: owed before each OLMo LOCK v1.0, outside the package (`scripts/`) |
| LOCK-m-OLMo-{ckpt} v1.0 | a document | — |
| campaign-OLMo-{ckpt} | `stages.run_campaign` (step 4, OLMo branch, stub-tested); driver `campaign --unit OLMo-{ckpt}` | **refused** until that checkpoint's v1.0, whose launch counts and the PI's cap share it carries; wired then as a driver edit of the step-10 read's Q2 kind, as Q-F0's campaign was after LOCK-m-F0 v1.0 |
| G-VER (F0m-OLMo verifier) | `verify.py` (step 4) | built before this build; unchanged |

## 2. What changed, by file

**`valence_core/m/gcal.py`** (not in G-SHAPE-F0's sources map):
1. G-CAL-OLMo-{ckpt}: `run_completability(..., unit="OLMo-{ckpt}")`. The prompt is Qwen's: b3's banner is `SESSION_BANNER` itself (banner.py's docstring). The generation path is the F0m-OLMo runner's (`runner_olmo.olmo_startup`; the runner's `adapter.generate` call, uncached, TEMP 0.7, `STOP_CAP = 60`, b3's ban list). Same 128 keys and seeds, grader, bars and covariate. Qwen's branch is unchanged byte for byte (identity, artifact, prints).
2. Names: `G-CAL_completability_olmo-{ckpt}.json` (gates) and `G-CAL_olmo-{ckpt}.json` (ckpt).
3. Identity: Qwen's keys plus `unit`, `ban_ids_sha16` (stages' form; b3's `2dd86a453a2275ef` once `olmo_startup` has asserted it), `weights_repo`, `weights_revision`, `weights_sha256` (the committed manifest's entry). On OLMo, `ban_sha256` is the committed `data/olmo/scaffold_{ckpt}.json`'s sha256.
4. FAIL → "that checkpoint NOT-RUN with reason "dose not completable" (m:176, m:302; §5)", never "STOP and re-specify".
5. Precheck on OLMo: the weights of record from the committed manifest; non-stub, the pod id in place of m:267's laptop checklist; the gate line names G-CAL-OLMo-{ckpt}.
6. Startup on OLMo: `olmo_startup` (through a module-level name the self-test substitutes, stages.py's form), TEMP and cap, the adapter's weights path equal to the manifest's (non-stub), and the appended-token probe.
7. R1 A6's tallies: (iii) and (iv) computed by `olmo_tallies` and printed for the entry, written to no artifact; (i) and (ii) printed as candidate keys for Code's read.

**`valence_core/m/resume.py`** (not in the sources map):
8. `IDENTITY_KEYS_OLMO` = Q-F0's keys + `weights_sha256` (the manifest's `files_aggregate_sha256` for the unit's checkpoint, defaulted by `Identity`); Q-F0's key set and every Q-F0 record are unchanged; `_validated` takes the key set by unit.
9. The CHECKPOINT STATE INCONSISTENT totals line is sealed at its source (`TOTALS_SEALED`, neither figure printed).

**`scripts/m_sessions.py`** (G-SHAPE-F0's tooling map):
10. The OLMo units' wiring: `OLMO_UNITS`, `olmo_lock_file` (`LOCK-m-OLMo-{ckpt}.md` at root), `olmo_counts` (m:302's 1+1 and 8+16), `olmo_weights_problems`, `weights_line`, `_load_olmo`, `prior_adjudication_text`, `_run_stage_olmo`; `stage_identity_extra`, `stage_precheck`, `_run_stage`, `run_gcal_completability`, `refusal` and `main` take the OLMo units; Q-F0's paths are unchanged except that `_run_stage` refuses `--prior-adjudication-file` on Q-F0's qual.
11. The carry-overs (§4).
12. The self-test: 21 new checks (gcal 11, finding 1's pod check among them; resume 3; driver 7; 825 → 846) and every Q-F0 check that pinned the step-9 refusal, the totals line or the re-run guidance updated (§5).

## 3. The PIN register (Code's; each declared at LOCK-m-OLMo-{ckpt} v0.1)

| # | site | reading |
|---|---|---|
| O1 | `gcal.py`, the `olmo_startup` import | the self-test's seam is a module-level name, stages.py's form; production code has no seam |
| O2 | `gcal.py`, `IDENTITY_KEYS_OLMO` | the five added identity keys; `ban_sha256` = the scaffold file's sha256 on OLMo |
| O3 | `gcal.py`, `TOKENIZER_PROBE` | "For the box" (RESULTS.md@9cbacdb:5680–5685): two texts ending in different words must not encode to the same last id under the default encode; refused before any generation, at G-CAL-OLMo, the first stage on each checkpoint |
| O4 | `gcal.weights_of_record` | the weights of record = the committed manifest's entry; a full re-hash is respawn (i)'s, once per box, in its BACKEND entry |
| O5 | `gcal.precheck` (OLMo) | no laptop checklist on OLMo (the box's respawn protocol governs); the pod id required non-stub |
| O6 | `gcal._identity_olmo` | Qwen's rule plus O2's keys: a resume on another checkpoint, scaffold set or weights is refused |
| O7 | `gcal.completability_artifact` (OLMo) | Qwen's form with the unit named, the procedure stated for b3's banner and path, and the NOT-RUN consequence |
| O8 | `gcal.olmo_tallies` | (iii) = `scaffold.termination` matches; (iv) = whole-word, case-as-written restatement of a corrupted word (a maximal letter run of the render holding a changed position); both reproduce the Qwen record (RESULTS.md@9cbacdb:5032–5041: 1; 11 with 9 hits), checked in the self-test |
| O9 | `gcal.run_completability`, provenance | an OLMo invocation records its pod id in provenance, not identity |
| O10 | `resume.IDENTITY_KEYS_OLMO` | the weights binding (Q6), OLMo only |
| O11 | `resume._check_state`, `TOTALS_SEALED` | the step-14 read's Q3 package message, sealed at the source |
| O12 | `m_sessions.py`, the OLMo units block | what is wired (gcal, time, qual) and what is not (campaign until v1.0; no id) |
| O13 | `olmo_weights_problems` | a size check of every manifest-listed file before the load, not a re-hash |
| O14 | `stage_identity_extra` (OLMo) | the lock `LOCK-m-OLMo-{ckpt}.md` must name the proposal's sha256 and the weights of record's `files_aggregate_sha256` in full; locked_path "uncached" |
| O15 | `stage_precheck` (OLMo) | the unit's paths and committed gate schedules; G-F0m-OLMo's prior through `stages.prior_gate` with the prior adjudication; the pod id in place of the laptop checklist; no G-ID artifact |
| O16 | `_run_stage` | the OLMo units dispatch to `_run_stage_olmo`; Q-F0's qual refuses `--prior-adjudication-file` (only an OLMo qualification after a G-TIME-OLMo PAUSE takes one) |
| O17 | `_run_stage_olmo` | Q-F0's form on the box: the flags; the precheck, driver and weights checks refused together; DRIVER and WEIGHTS lines; the load at the checked path; WEIGHTS PATH after it |
| O18 | `refusal` | the OLMo campaign refused until that checkpoint's v1.0; time and qual are no refusal |
| O19 | `run_gcal_completability` (OLMo) | gcal's precheck, the weights check and the driver check refused together before the load; the DRIVER and WEIGHTS lines |
| O20 | `TOTALS_RX` | the driver's redaction finds no figure on a live line now; kept as a guard |
| O21 | `campaign_ruling_problems`, O4-1 | §4 |
| O22 | `campaign_ruling_problems`, O1-3 | §4 |
| O23 | `ruling_line`, RM4-1 | §4 |
| O24 | `camp_pauses` and the docstrings | VC4-1, the campaign driver review's missed item, and VC4-2 (the module docstring's reason sentence), §4 |
| O25 | `gcal.run_completability` (OLMo resume) | the code review's finding 1, m:267: a resume that would generate on another pod is refused (POD CHANGED); a complete checkpoint re-derives anywhere |
| O26 | `OLMO_QUAL_LOCK_LINE` | finding 2, m:302: G-F0m-OLMo requires v0.2's line `G-TIME-OLMo-{ckpt} port acceptance recorded` in its lock's committed text; the line's form is Code's, for LOCK-m-OLMo-{ckpt} v0.2 to carry |
| O27 | `olmo_gcal_problems` | finding 9, m:176: G-TIME-OLMo's box path requires G-CAL-OLMo-{ckpt}'s artifact on disk, PASS, on the weights of record |
| O28 | `olmo_weights_problems` (revised) | finding 8: a malformed files block is a problem; symlinks and unlisted files are refused |

## 4. The carry-overs (Q6), as built

- **The CHECKPOINT STATE INCONSISTENT message** (the step-14 read's Q3, `…G-F0m-Qwen_read.md:42`): `resume._check_state` prints `TOTALS_SEALED`, neither total. The driver's redaction (`redact_totals`) stays as built.
- **O4-1** (the operations refuter's alternative; `…campaign-driver_review.txt:213–219`): `campaign_ruling_problems` refuses before the load a ruling offered beside an end pending that the stage would not apply there. Those are the seat's adjudication, and a PI stop the checkpoint does not record. They are exactly `stages._refinish_campaign`'s NOT APPLIED cases where the stage reaches the re-finish: `run_campaign` passes a recorded stop as None. On a pending checkpoint whose design, licence, prior or floors differ, the stage STOPs on CHECKPOINT MISMATCH before any re-finish (the review's finding 7, disclosed in the PIN). The refusal is "RULING BESIDE AN END PENDING … re-run without <the flags>, with --resume". The stage itself is unchanged, and where no precheck runs it still re-finishes and then refuses NOT APPLIED.
- **O1-3** (round 1's option, the same raw): `campaign_ruling_problems` refuses before the load an adjudication offered for an open pause whose stripped text's sha16 equals a ruling the checkpoint records for an earlier pause ("RULING REUSED"). The stage has no such rule and would apply it. `_campaign_state`'s summary gains `ruling_sha16s` (digests only).
- **RM4-1** (the same raw): the RULING line ends "; the checkpoint already records this adjudication as a pause's ruling" when the offered adjudication's sha16 is among `ruling_sha16s`. On the Qwen path every such state is refused before the RULING line prints (the code review's finding 3; no OLMo campaign path exists yet), so the pre-load refusals carry the information: RULING REUSED names the digest, O4-1's refusal names an adjudication already recorded as needing nothing, and NO PAUSE TO ADJUDICATE names the last pause's ruling digest.
- **VC4-1 and VC4-2** (`…campaign-driver_review.txt:200–207`; their dispositions at :8471–8474): the campaign help (`camp_pauses`) and the module docstring are rewritten; `_run_stage`'s docstring changes for O4-1 only.
  - VC4-2: the module docstring's reason for never re-offering an adjudication offered beside an end pending is put in the refuter's form, "it rules on no pause shown when it was offered: it is the previous pause's ruling, already recorded, or one written before the pause it would rule on was shown" (unpinned, the rule standing).
  - The review's missed item, "a finish completed before the kill" (:8483–8485): the adjudication re-run sentence names it (the re-run shows the new pause, or is refused as ended).
  - VC4-1: the PI's-stop re-run sentence names the end-pending cases. A recorded stop re-finishes with the end; a terminal end or a STOP stands. A ruling the stage would not apply is refused before the load. Where the end is a look's or an exhausted schedule's pause, a stop so refused is offered again once the re-finish has shown it. An adjudication recorded beside a recorded stop needs nothing.
  - The "beside an end pending" sentence is rewritten for O4-1.
- **O2-3's listing forms** (the VERDICTS read §4 item 5, `…VERDICTS_read.md:86`): README and checklist text, not driver code. Each OLMo unit's launch checklist and box README carry, until that unit's VERDICTS: no size or time metadata of its raws, `data/m/ckpt` or `data/m/reports`; the listing forms permitted are a bare `git status --porcelain` and a name-only `ls` (the VERDICTS read's words), and `git ls-files`, `git diff --name-status` and `shasum` (O2-3's own line: "files are verified by name-status, ls-files and shasum").
- **The weights-snapshot binding**: `resume.IDENTITY_KEYS_OLMO` (O10) and G-CAL-OLMo's identity (O2).

## 5. Self-test changes to existing checks (no check removed)

- The bare `--unit` refusals; `run_time`, `run_qual` and `run_campaign` on the OLMo units. These pinned "not licensed until step 9". They now pin the wired refusals: `time` and `qual` cite LOCK-m-OLMo-{ckpt}.md, and `campaign` cites that checkpoint's v1.0.
- `qual`'s help pin (the OLMo clause).
- The step-14 read's Q3 checks (four), which now require the package's sealed sentence.
- The line-form whitelist: the G-TIME-OLMo / G-F0m-OLMo BAR and STAGE forms, the WEIGHTS line, the OLMo campaign refusal and RM4-1's note. The OLMo block runs after the campaign's runs and before the scans, so the whitelist with its date-and-time clause, the ruling-texts check (with the prior-adjudication file's token) and the stdout scans cover its outputs (not the canary-clock check, which reads the campaign's range only). The G-CAL-OLMo stub run, which is not a stage-wiring run, is kept out of them.
- The `_campaign_state` summary's key set, which gains `ruling_sha16s`.
- The 70-case ruling-fit mirror check. Its rule now has two declared exceptions. O4-1's refusal must meet the stage's NOT APPLIED, and O1-3's must meet the stage not refusing. Its set of refusals gains the two names, and RM4-1's note is expected exactly where the offered text is a recorded ruling.
- The help pins of the re-run guidance (VC3-5), regenerated from the same sentences as the help.
- The Qwen-path mirror check, which gains the two pre-load refusals end to end (the review's finding 5), and the ended-campaign check, which now expects RM4-1's note.

## 6. Hashes and gates

- `package_sha256` moves off `5f646db6…` (LOCK-m-F0 v1.0's) to `60199b36557ac283771b83dcb4be101b5c56880dceacdecd05cce5a578e7feec`, as Q2 expects. The analyzer (`655e0f7f…c16f`) is unchanged. The edited files' sha256 are in the BUILD entry and the self-test raw's header.
- **G-SHAPE-F0 re-runs** before the first LOCK-m-OLMo v0.1 (the referent check's N5). This build edits `scripts/m_sessions.py`, a TOOLING_FILES entry, beyond subcommand wiring: the carry-overs and the sealed-line test pins. No SCORING_STACK_FILES entry is edited. The re-run is model-free; the supersession follows PIN-S9 on Q2's word.
- Forward, for G-ANL-F3: with the package moved, PIN-14 refuses a re-run of Q-F0's `verdicts` on the current tree. A-m1 §2.5 (3)'s regression meets this; the seat's Q2 answer covers the posting, which records the shas without refusing.
