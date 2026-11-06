# m package — BUILD (F3): Code's build design, PIN register and readiness table (2026-11-06)

*Code's raw. The F3 build of ADDENDUM-m1 §4 step 5 (m:361's first node, `m package — BUILD (F3)`), run under the design seat's prebuild answers of 2026-11-06 (`results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md`, sha256 `aec58440…4df3`, committed at `dc1ffe1`), Q1 (C2) above all, and Code's referent check of them (`results/raw/2026-11-06_f3-build_prebuild-answers_referent-check.md`, its dated notes N1–N6). The PI routed the work on 2026-11-06 ("Run the prebuild answers as written, then PROPOSAL-n v0.2 §8 from step 1"). `m:N` = PROPOSAL-m v1.11 at root (sha256 `42ab36ec…6c6b`); `A-m1` = ADDENDUM-m1 v0.1 (`f26bc59`). Every reading below is Code's PIN, declared at LOCK-m-F3 v0.1 and strikable by the seat until LOCK-m-F3 v1.0 (answers §8, the register's terms), except where a row names the seat's ruling it builds.*

## 1. Placement and licence (Q1 (C2))

- **The package.** `valence_core/mf3/`, a sibling of `valence_core/m`. Nothing under `valence_core/m/`, `scripts/m_sessions.py`, `scripts/m_analyze.py` or `data/m/` is edited; `valence_core/m`'s `package_sha256` stays the OLMo build's `60199b36…feec` (asserted by the driver's self-test).
- **What it imports (L1; N1's reading).** The ten `valence_core.m` modules `guard.M_MODULES` lists: `audit`, `banner`, `bars`, `corr`, `guard`, `keys`, `readrule`, `resume`, `scaffold`, `schedule`. Q1's list (corr with `corrupt_m`, the audit's task-round classes, bars, the banner constants, schedule's cells, `keys.stream`) plus four the build reuses rather than copy:
  - `guard`: the insulated read (`assert_insulated`, `insulated_read`, `label_ids`) and the laptop checklist; and, since the code review's finding 1, its call-site scanner (`_CallSiteScan`, subclassed; `_bindings`, `_guarded_defs`, `_LICENSED_FNS`, `_GUARDED_CALLEES`);
  - `resume`: the checkpoint machinery (atomic writes, `_check_state` with its sealed totals line, the three-step finish, provenance, the hour cap), the package-hash formula and the backend identifier;
  - `scaffold`: `SessionScaffold` and `SessionLog` (subclassed), the boundary assertion, the renders of record, the termination patterns;
  - `readrule`: the blinding helpers and printed forms.
  The set is the transitive closure of mf3's production imports (module level and lazy; a `_selftest` body and the test double `mf3/testing.py` are outside it), each reached m module's own imports followed. `stages`, `gshape`, `gcal`, both runners, `verify` and `testing` are never reached. `guard.import_problems` asserts this statically and in a fresh interpreter (`-I -B`); every stage start runs the static half. The licence hashes the package's own `__init__.py` beside the ten (`guard.M_HASHED`, eleven files), since importing any m module executes it first (the build review's finding 7).
- **The licence (L2).** LOCK-m-F3 v0.1 names (a) mf3's `package_sha256`, computed by `valence_core.m.resume.package_sha256_of` itself over `valence_core/mf3/*.py`, and (b) the file sha256 of each of the eleven m files (`M_HASHED`). Every non-stub stage checks both at start (`stages.licence_problems`): (a) HEAD known; (b) the proposal and (c) the lock committed with the working tree's bytes and their sha256 the identity's; (d) the analyzer's bytes; (e) mf3's package hashed now; (e′) each m file hashed now; (f) the committed lock's text naming the analyzer's and mf3's sha256, and each m file by name, its path and sha256 on one line (Q1 (C2) part (b): "listed by name"; finding 8); (g) the weights (§8, Q6): `HF_HUB_OFFLINE` exactly "1", the hub cache's `refs/main` naming the bound revision, and the binding computed now on that snapshot, named by the lock (finding 5).
- **The driver.** `scripts/mf3_sessions.py`, new: `--selftest`, `--build-schedules`, `hashes`, `gshape`; `time`, `id`, `qual` and `campaign` refused (§2).
- **The data.** `data/mf3/schedules/`: 20 schedule files and their own `manifest.json` (sha256 `c7b5df44…3314`), admitted by a commented per-directory block in `.gitignore`; `data/mf3/ckpt/**` is `-diff` in `.gitattributes` (m:318). `data/m/schedules/` and its manifest are untouched.

## 2. Readiness, per stage (ledger (55): read from the driver's wiring and the gate tooling)

| stage (m:361) | tooling | state after this build |
|---|---|---|
| G-SHAPE-F3 | `mf3.gshape.write`; driver `gshape` | **built and wired**; its canonical run follows the BUILD commit (every source committed at HEAD) |
| G-ANL-F3 | `scripts/m_analyze.py`, extended in place (m:291; the seat's Q3) | **not built**: its commit lands only while no OLMo unit is open (Q3's rule); §6 |
| LOCK-m-F3 v0.1 | a document | names the hashes `hashes` prints, G-SHAPE-F3's artifact and G-ANL-F3's analyzer and lexicons (m:292) |
| G-TIME-F3 | `mf3.stages.run_gate_stage(gate="time")` | **built, stub-tested; the driver refuses `time`** until its step |
| cap fixed | `stages.cap_trigger`, in G-TIME-F3's report | **built**; applied from G-ID-F3 on: G-ID-F3 and G-F3 refuse any cap but the trigger re-computed from G-TIME-F3's checkpoint, and the campaign any cap but G-F3's (m:294–295); recorded at LOCK-m-F3 v0.2 (m:296) |
| G-ID-F3 | `mf3.stages.run_gid_pair_f3` | **built, stub-tested; refused** until its step |
| G-F3 | `mf3.stages.run_gate_stage(gate="qual")` | **built, stub-tested; refused** until its step |
| G-PWR (Q-F3) | `scripts/m_gpwr.py` is Q-F0's | **not built**: owed before LOCK-m-F3 v1.0 (m:298) |
| campaign | `mf3.stages.run_campaign` | **built, stub-tested; refused** until LOCK-m-F3 v1.0 |
| G-VER (F3) | `mf3.verify.verify_session` | **built**; every stage verifies each record before it is written |

Each stage subcommand is wired at its step as a driver edit. Whether the step-10 read's Q2 clearance ("an edit … that wires a subcommand … does not re-run G-SHAPE-F0") carries to `scripts/mf3_sessions.py`, which G-SHAPE-F3's sources map records as tooling, is the seat's (flag F-1).

## 3. What was built, by file

- `__init__.py` — scope and the licence.
- `keys.py` — Q-F3's keys (m:159): items `m-f3-items|{s}` / `m-f3-items-{gate}|{s}`; arms `m|{arm}|{s}`, `m-time|{arm}|{s}`, `m-id|F3|{template}|{s}` (A2s, A3s), `m-f3|{template}|{s}`; schedules `m-sched|Q-F3|{arm}|{b}`, `m-sched|Q-F3|{gate}|{template}|0`; `stream` is m's. No Q-F3 key equals a Q-F0 or OLMo key (self-test).
- `banner.py` — the six F3 banners (A1 TOLD-MAP, A1s TOLD-MAP-SHAM, A2/A2s TOLD-OBJ, A3/A3s COMMON only) and the reasoning block, from m's constants; `spec_problems` against the proposal file and §2.4's banner column.
- `schedule.py` — campaign cells and balance units, the sixteen-row gate schedules (clause None on A2–A3s), the clause-free balance check, the six-template launch order and six-arm interleave, the files and manifest.
- `lines.py` — the reasoning line's three classes, its echo set, the Q4 review counter.
- `scaffold.py` — `F3Scaffold` (F2 block order; `reasoning(ci)` draws the line's seed before the menu order), `f3_config`, `F3Log` (the F3 record), the two-form boundary assertion, `prepick_excluded`.
- `runner.py` — `f3_startup` and `run_session_f3`.
- `verify.py` — G-VER for F3.
- `readrule.py` — F3's read rules, printed reasons, session lines and stage report.
- `bars.py` — `F3Bar` (m's `Bar` with Q-F3's vocabulary), the bar table, firing cases, the realised-n evaluation.
- `guard.py` — the cached-path licence (G-ID-F3's artifact at its cap), the static call-site guard (`valence_core.m.guard`'s scanner, subclassed with Q-F3's names), the import-set check, the forbidden-literal scan; m's insulation re-exported.
- `resume.py` — Q-F3's identity (Q-F0's keys + `reasoning_cap`, `m_module_sha256`, `weights_revision`, `weights_sha256`), `load_or_init`, the weights binding and the model of record's hub-cache directory; m's checkpoint machinery re-exported.
- `stages.py` — the gate stages, G-ID-F3, the campaign, the licence, the reports.
- `gshape.py` — G-SHAPE-F3.
- `testing.py` — the test double (self-test only).
- `scripts/mf3_sessions.py` — the driver.

## 4. The PIN register (Code's; each declared at LOCK-m-F3 v0.1)

| # | site | reading |
|---|---|---|
| F1 | `guard.M_MODULES`, `guard.M_HASHED` | L1: the ten modules, the transitive production closure; `ABSENT_MODULES` asserted absent (N1); the licence hashes `M_HASHED`, the ten and m's `__init__.py` (finding 7) |
| F2 | `guard._gid_pass` | the licence is m's form plus `identity.reasoning_cap` equal to the asking cap |
| F3 | `stages.licence_problems` | L2's (a)–(g); (f) names each m file by path and sha256 on one line (finding 8); (g) `HF_HUB_OFFLINE` = "1" and `refs/main` = the bound revision (finding 5) |
| F4 | `stages.ANALYZER_PATH` | the analyzer is `scripts/m_analyze.py`, extended in place by G-ANL-F3 (Q3) |
| F5 | `stages.out_paths` | m's layout under `data/mf3` |
| F6 | `stages.PRIOR_STAGE`, `prior_gate` | G-ID-F3 needs G-TIME-F3 PASS; G-F3 needs G-TIME-F3 PASS and the G-ID-F3 artifact at the run's cap; the campaign needs G-F3 PASS. G-ID-F3 and G-F3 refuse any cap but the one G-TIME-F3's trigger fixes, re-computed from its checkpoint; the campaign refuses any but G-F3's (finding 4) |
| F7 | `stages.gid_artifact_problems` | an artifact at another cap is refused (B7) |
| F8 | `stages._extra` | identity_extra's keys; `reasoning_cap` 60 at G-TIME-F3; the stub's weights binding refused on a non-stub run |
| F9 | `stages._hair_hit` | the fired generation may be a reasoning line (phase "reasoning", its ci) |
| F10 | `stages._line_excerpt` | a line after the first pick lists the previous choice's pick as revealed |
| F11 | `stages.cap_trigger` | m:174's count over all six G-TIME-F3 sessions' lines (Q5); ≥ 3 → 120; applied from G-ID-F3 on (m:294–295), recorded at LOCK v0.2 (m:296) |
| F12 | `stages.gid_decide` | one complete identical pair per template, indices advancing per template (m:281's rule, Q8; N2); a divergence anywhere FAILs |
| F13 | `stages.run_gid_pair_f3` | a G-ID-F3 artifact is never overwritten (B7) |
| F14 | `stages._finish_gid` | G-ID-F3's reads are the full sham-only records (§4 exception (4)) |
| F15 | `stages.campaign_look` | the lexical bar's numerator and the beside counts (B23) |
| F16 | `stages.run_campaign` | an artifact at another cap refuses the campaign (B7) |
| F17 | `stages._campaign_report` | m's pick-free campaign report |
| F18 | `scaffold.f3_config` (path) | G-TIME-F3 uncached; G-ID-F3 both paths |
| F19 | `scaffold.f3_config` (cap) | G-TIME-F3 generates lines at 60; G-ID-F3 on, at the cap G-TIME-F3's trigger fixes (m:294–295; F6) |
| F20 | `scaffold.f3_config` (j) | j = s at gate stages, None in the campaign |
| F21 | `scaffold.assert_boundary` | rule 28(d)(a) in both forms at every generation (Q8; N6) |
| F22 | `F3Log.reasoning_hair` | a line's scaffold fire: hair {phase "reasoning", ci} and exclusion {class "scaffold", phase "reasoning", ci}; strict scope unchanged (Q8) |
| F23 | `F3Log.record` | complete = 4 forced + 6 × (line, read, round) |
| F24 | `scaffold.prepick_excluded` | pre-pick = forced, or reasoning with ci 0 (Q8's pre-pick count; m:308's domain: "up to and including the first reasoning line") |
| F25 | `lines.echo_lines` | the eight strings as rendered for the session + the headers written so far (Q8; N4) |
| F26 | `lines.classify_line` (empty) | ws_norm(text) == ""; with both EOS strings banned a whitespace-only line runs to its cap |
| F27 | `lines.classify_line` (cap) | stop_reason "cap" (Q8: the cap-length prefix kept, cap-reach); a newline as the cap-th token is not cap-reach |
| F28 | `lines.classify_line` (echo) | containment, case-sensitive, ws_norm, first match (Q8) |
| F29 | `lines.review_counter` | the Q4 counter: per (template, kind, string), all sessions; the analyzer tabulates it |
| F30 | `readrule._LINE_RX` | the declared session-line forms |
| F31 | `readrule._check_pieces` | only the last free group may be the reasoning block alone, where the line ended the session |
| F32 | `readrule.strip_contrast` (time) | ruling (h)'s form plus the per-line cap booleans (Q5); the list's length locates a free-phase end (flag F-6) |
| F33 | `readrule.strip_contrast` | a contrast session's free and reasoning hair triggers withheld from the read |
| F34 | `readrule.redact_sham` | both labels redacted in free responses and every reasoning line |
| F35 | `readrule.printed_reason` | a contrast line after the first pick prints `excluded@free`; line 1 `scaffold@reasoning`; at G-TIME-F3 every contrast line `excluded@free` (ruling (h): no class; a reasoning line is excluded only for the scaffold class, so its phase would name it; finding 3) |
| F36 | `readrule._contrast_block_time` | G-TIME-F3's contrast block: s, forced rounds generated, excluded at forced, the per-line cap booleans |
| F37 | `resume.weights_binding` | Q6's binding: the snapshot's revision and the sha256 of its load files' content addresses |
| F38 | `resume.Identity` (paths) | G-ID-F3 "cached+uncached"; G-TIME-F3 "uncached" |
| F39 | `resume.load_or_init` | m's order with Q-F3's identity; no pod id on the laptop |
| F40 | `runner.qwen_ban_list` | runner_qwen's procedure (not importable, N1) |
| F41 | `runner.run_session_f3` (licence) | a cached session outside G-ID-F3 re-reads the licence on this backend at this cap |
| F42 | `runner.run_session_f3` (seconds) | the whole session's wall-clock, to the ms |
| F43 | `schedule.L_MAX_K1` | the k = 1 materialization: A1 4352, A1s 1600, A2 = A3 6384, A2s = A3s 2640 (B21) |
| F44 | `schedule.GATE_PLAN` | G-TIME-F3 1 per arm; G-ID-F3 A2s and A3s, 16 rows each; G-F3 4/8/4/8/8/8 |
| F45 | `schedule.roster` | Q-F3's roster is Qwen's of record via `m.schedule.roster_for("Q-F0")` |
| F46 | `schedule.gate_launch_order` | strict rotation in §2.4's order, a template leaving at its count (B5) |
| F47 | `schedule.interleave` | m's rotation over six arms, the counts validated pairwise |
| F48 | `schedule._file_blobs` | m's manifest form, construction "PROPOSAL-m v1.11 m:159-172 (Q-F3)" |
| F49 | `bars._qf3_bars` | scaffold_absorption's unit is the generation (a round or a line) (B26); G-ID-F3's criterion declared `gid_divergence` |
| F50 | `bars` (G-TIME-F3 line bar) | a fire STOPs; the cap-trigger count is reported, applied by nobody until the seat re-specifies (B17) |
| F51 | `bars.counts` | m's stage_end_eval PIN carried; lines by the union of classes |
| F52 | `bars.no_test` | a gate-stage bar at realised n = 0 is reported as no test and not fired, and the stage ends on its other bars: Code's reading by analogy with m:271's Qwen rule, which says "reported, not fired" of G-TIME-F0's realised n of 2–4 and "on Qwen no such pause exists" of OLMo's G-TIME pause (m:271 says nothing of n = 0); revised on finding 6 from a PAUSE that nothing could lift; silent at a campaign look (B30) |
| F53 | `banner._label` | m's label rule |
| F54 | `verify` (read) | m's read check: menu_a iff p_a >= p_b, KL exactly 0.0 |
| F55 | `verify` (role) | A2/A2s and A3/A3s share a banner: the template name decides the role and the delivery is asserted (B22) |
| F56 | `gshape` (Layers R, T) | additions to "as G-SHAPE-F0": the reasoning line's own placements (Layer R) and the build hazard's declared check on the tokenizer of record (Layer T); §7 (Layer R's scope, finding 11) |
| F57 | `scripts/mf3_sessions.py` | what is wired (selftest, schedules, hashes, gshape) and refused (the four stages); Q6's forms (§8) |
| F58 | `guard._F3CallSiteScan`, `guard.check_call_sites` | `valence_core.m.guard`'s hardened scanner, imported and subclassed: the scanner is inherited, and six methods are overridden, each restating m's with Q-F3's names — the four that bind m's guard module or file (`__init__`, `_flag_licensed_bindings`, `_is_guard_alias`, `_licensed`: mf3's guard the one licensed binding, so Q-F0's licence is unlicensed here, m:267), `in_gid` (`run_gid_pair_f3`'s module-level body the one exemption) and `flag` (m's names in every inherited message); `run_session_f3` guarded; m's whole battery reproduces under `_battery_map` (finding 1) |
| F59 | `stages._gid_pair` (`meta_identical`) | beside m:281's criterion, descriptive only: whether a pair's generations agree in token count, cap flag and stop reason (finding 9; flag F-7) |
| F60 | `readrule._contrast_block` | a contrast template reports its sessions' first reasoning lines (pre-pick) beside its forced rounds, by class, with line-1 exclusions and hair triggers; later lines withheld with the free rounds (m:297, m:271; finding 12) |

## 5. The B items of Code's spec map, disposed

Code's prebuild block counted thirty-one open places and one build hazard (`results/raw/2026-11-06_f3-build_code-to-design_prebuild.md:178`); Code's spec map (scratch, not on record) numbers them B1–B32, the hazard being B32. The seat ruled seven in Q8 (B2, B3, B6, B13, B14, B31, B32), and Q5 rules B8 and B9; the rest are Code's readings, most with a register row.

- **Ruled by the seat (built as ruled):** B3 (Q8: cap reached without a newline — F27); B2 (Q8: containment, the eight strings — F25, F28; N4); B14 (Q8: a line's scaffold fire is an exclusion event that ends the session and is in the guard's pre-pick count — F22; that only a line-1 fire is pre-pick is m:308's domain, "up to and including the first reasoning line" — F24); B13 (Q8: "as Q-F0 ran them … no new keying" — line defects carry no property key; N3); B6 (Q8: as G-ID-F0m's, the cap an identity input — F12; N2); B32 (Q8: the "\n\n" — F21, F56; N6); B31 (Q8: the build's scope — keys, schedules, gate files, the bar table built here); B8 and B9 (Q5: contrast sessions' per-line cap booleans; the trigger over all six — F11, F32, F36).
- **Code's readings, with a register row:** B1 (F26: an empty line is one whose ws_norm is empty), B4 (F35), B5 (F46), B7 (F7, F13, F16), B15 (F22 and the runner: lines never enter `earlier`; Layer S's S5), B17 (F50), B18 (F56), B21 (F43), B22 (F55), B23 (F15), B25 (F34), B26 (F49), B30 (F52).
- **Code's readings, without a register row:** B10–B12 and B24 (counter (c)'s scorer, the blind-read draw and (f)'s statistics are G-ANL-F3's; the runner records every line's text, n_tok, position, cap fields, classes and the session's pair, map and first pick), B16 (`resume.Identity`: `reasoning_cap` beside Q-F0's `stop_cap` 60), B19 (stage timing over sham sessions only; G-ID-F3 both paths), B20 (G-F3's report carries m:283's flags by analogy: the sham blocks' read flags and audit counts, the contrast arms' first-read flags), B27–B29 (G-ANL-F3's).

## 6. Q3: the analyzer and the calendar

- **The calendar fact at this build:** no `LOCK-m-OLMo-*.md` exists at root, no OLMo stage has run, no pod is up, and G-ANL-F3 is not built. So neither of Q3's orders is fixed yet: (a) G-ANL-F3 before any LOCK-m-OLMo v0.1, or (b) the OLMo track through its VERDICTS first. The seat recommends (b) if the pod is up before G-ANL-F3 is built. Whichever lands first fixes the order; the G-ANL-F3 entry records it.
- **The texts that ride in G-ANL-F3's round, by record anchor (for the seat to confirm before LOCK-m-F3 v0.1 names the blob):**
  1. A-m1 §2.5 (1): the CLI-path reading (the step-17 addendum, `results/raw/2026-10-19_m-design-to-code_step17_addendum.md:11`; RESULTS.md@18c32df:85–89).
  2. A-m1 §2.5 (2): the Clock dates as declared inputs (D1, D_O′, D2).
  3. A-m1 §2.5 (3): the byte-for-byte regression of `Q-F0_VERDICTS.json` and `Q-F0_secondary.json`, with N8's reading.
  4. The VERDICTS read §4 item 2 (`results/raw/2026-10-19_m-design-to-code_VERDICTS_read.md:83`): the quirk in `_prod_committed`'s `rel == str(p)` test and `flag_of_record`'s silent FALSE on a relative `--flag-source`, "flagged for the analyzer's next hash-moving round" (the same CLI reading as item 1).
  5. Round 2's standing rule (`results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1_round2.md:19`): "a misparaphrase found later [in the analyzer's PIN texts] is a text correction at the next hash-moving round"; with Code's step-15 reading of the reverse case (`results/raw/2026-10-14_m-code-to-design_step15.md:255–262`), whose default was no change.
  The VERDICTS read's item 4 (`…VERDICTS_read.md:85`, "a text correction for the addendum's successor, nothing moves") names the addendum's successor, not the analyzer, and is listed for completeness. Code found no other text the record assigns to that round; the list is Code's search, not a completeness proof.

## 7. G-SHAPE-F3's composition (F56)

"As G-SHAPE-F0 for the F3 templates, the reasoning header included" (m:290) is read as G-SHAPE-F0's three layers carried (A: the renders inside each contrast template's round templates, golds as responses, through the Qwen stack as the F3 runner calls it; C: the scope-widened controls; S: the runner's static scope), the reasoning header included twice — as a required control at the free phase (`reasoning+seg+gold`) and as Layer R, the reasoning line's own placements through its classes — plus Layer T, Code's declared check for the build hazard (answers:58), which loads the Qwen tokenizer of record and nothing else. "Model-free" holds: no model and no generation; Layer T departs from G-SHAPE-F0's "no tokenizer", which is that module's description, not m:277's words. Both additions are strikable. Layer R places each gold as a line ended by its newline, so its structural classes (empty, cap reached) cannot fire there and the content-borne fields (echo, scaffold) are its test; the artifact's `scope` text says so. Layer A's free-phase n is G-SHAPE-F0's (`t + 1 + N_FORCED`, `valence_core/m/gshape.py:750`; 5–8), so the reasoning header at n 9 and 10 is placed by Layer R only (finding 11).

## 8. Q6's carry-overs, as carried

- The CHECKPOINT STATE INCONSISTENT totals line: `valence_core.m.resume`'s sealed form (`TOTALS_SEALED`), imported by `mf3.resume`.
- The weights-snapshot binding: `mf3`'s identity carries `weights_revision` and `weights_sha256` (F37), and the licence's (g) checks them, with `HF_HUB_OFFLINE` exactly "1" and the hub cache's `refs/main` naming the bound revision (finding 5). The rest of `scripts/m_sessions.py`'s pre-load check (`MLXLM_USE_MODELSCOPE`, a local path named like the model id, the hub's own offline resolution, the SNAPSHOT line) comes with the driver's stage wiring (flag F-2).
- O4-1, O1-3, RM4-1, VC4-1 and VC4-2 are the campaign subcommand's ruling handling (O4-1 and O1-3, refusals; RM4-1, the RULING-line note) and its help and docstring sentences (VC4-1, VC4-2). The campaign subcommand is not wired at this build. They are written in `scripts/m_sessions.py`'s forms when it is, and the driver's docstring declares this (flag F-2).
- O2-3's listing forms go into Q-F3's launch checklist (the driver's docstring names them).

## 9. Hashes at the build

`python scripts/mf3_sessions.py hashes` prints them; the BUILD entry quotes the run on the committed tree. The weights binding of record is revision `c000ac2c2057d94be3fa931000c31723aac53282` (LOCK-m-F0 v0.2's) and weights_sha256 `03922eed43c73bf4af06cf4c51982005d95640dc6f39b57caf604749cf001e26` over config.json, tokenizer.json, model.safetensors.index.json and the three weight files' content addresses.

## 10. Flags for the seat

- **F-1.** The step-10 read's Q2 clearance for subcommand-wiring driver edits, carried to `scripts/mf3_sessions.py`? (§2)
- **F-2.** Q6's driver forms for the campaign (O4-1, O1-3, RM4-1, VC4-1, VC4-2) arrive with the campaign subcommand's wiring, not at this build; so does the rest of m's pre-load check (§8).
- **F-3.** G-SHAPE-F3's Layers R and T (F56). (§7)
- **F-4.** The import set's four modules beyond Q1's list (F1). (§1)
- **F-5.** G-PWR for Q-F3 is not built; it is owed before LOCK-m-F3 v1.0. (§2)
- **F-6.** G-TIME-F3's contrast per-line cap booleans (Q5, F32, F36): the list's length, and the total of the stage's CAP TRIGGER line, show where a contrast session's free phase ended, which is an exclusion's free-round index, which m:263 never prints. Built as Q5 rules. On the seat's word the report carries a per-session count instead, or the trigger's outcome alone. (The build review's finding 2.)
- **F-7.** G-ID-F3's `meta_identical` (F59): bind it beside m:281's transcript criterion, or keep it descriptive? (The build review's finding 9.)
