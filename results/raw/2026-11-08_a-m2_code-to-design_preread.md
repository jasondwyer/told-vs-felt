# ADDENDUM-m2 v0.1 — Code's pre-read: the referent check, Code's PINs for §1, counter (a), §4.2 and the smoke driver's form; STOP on two questions before the smoke, four FLAGs before the build (Code → design seat, through the PI)

*Code's raw, PI date 2026-11-08. This is the pre-read of ADDENDUM-m2 v0.1 (A-m2 §6 item 1), under the PI's routing of 2026-11-08, item 2 ("ADDENDUM-m2: route to Code’s pre-read and step 3 [go]; the four forms and the selection rule [as written]; the smoke’s laptop go [go]"), relayed by the coordinating session.*

*The document read: `ADDENDUM-m2-f3-reasoning-block-v0_1.md`, untracked at root, sha256 `cdcc8e8619801b357f79103ab74b9f419a3c2b21b2ffe9367014733a913f53f0` (13,983 bytes), verified.*

*Anchors are A-m2's preamble's, and `A-m2 §x` is the addendum. `ans:` is the seat's answers of 2026-11-08, committed at `daca8b0`. `ref #N` is item N of the referent check, the raw beside: `results/raw/2026-11-08_a-m2_preread_referent-check.md`. Line anchors in code are at HEAD `daca8b0`; `c9acd66`, committed since by another session, changes no code. The checkpoint `data/mf3/ckpt/Q-F3_time.json` was not opened (m:318). Nothing ran on a model.*

---

## §0 In brief

- **The referent check** (A-m2 §7; §1 below; its raw beside).
  - **Counts.** 59 items: 35 PASS, 15 IMPRECISE, 2 FAIL and 7 OPEN. Code re-checked every item not marked PASS at source, and every verdict stands.
  - **The facts the ruling rests on all hold:** 9 of 13; the critical of 4 at n = 13; the A3s quote; the Q8 quote; the m:258 and m:265 quotes; lock PINs F25 and F28.
  - **The two FAILs:**
    - §3.2's keys anchor (ref #22). The smoke's key is outside every family regardless (ref #23).
    - §4.3's re-issue list, which omits the Q-F3 closure and G-ANL-F3 (ref #51; F-C below).
- **Code's PINs, proposed** (§2):
  - P1, §1's set-builder over the record's pieces.
  - P2, counter (a).
  - P3, the constants' home and the verification against A-m2, with the files that move.
  - P4, the smoke driver's form.

  On G-TIME-F3's record, P1 reproduces A-m2 §1's 9 of 13, and P2 the seat's 11 of 13.
- **STOP: two questions before the smoke** (§3).
  - **Q1, counter (b).** It has no operational definition. Yet §3.3's rule uses it as tie-break (iii), says "the rule, not the read, selects", and is "declared before the smoke runs".
  - **Q2, count (i)'s scope.** As written it is the echo member alone. The bar the re-run must pass counts the union of empty, cap-reach and echo (ref #54).
- **Four FLAGs for the build** (§4). None blocks the smoke; the seat can answer them with its read of the smoke.
  - **F-A:** no VERDICTS path exists for §3.4's counters while the analyzer is untouched. The Q4 counter is already in that position: lock F29 says the analyzer tabulates it, and the analyzer does not.
  - **F-B:** the re-run's checkpoint.
    - The first run's `Q-F3_time.json` ends PASS, and `prior_gate` would accept it.
    - The analyzer reads one time checkpoint.
  - **F-C:** the lock names the Q-F3 closure, which the build moves; G-ANL-F3's artifact records it too.
  - **F-D:** m:261's task-round echo set, if F-c is selected.
- **Readings carried as dated notes** (§5).
- **What waits.** A-m2's step-3 commit and the smoke wait for the answers to Q1 and Q2. The precedent is PROPOSAL-p's pre-read: the STOP at `fb742e4`, with the document committed later, as v0.2, at `18b0111`. If the seat issues A-m2 v0.2 with §1's items, step 3 commits v0.2. The smoke driver is model-free work. Code can build it in a scratch worktree meanwhile, and commits nothing before A-m2 (§6).

---

## §1 The referent check (A-m2 §7)

A fresh agent checked every referent and figure that A-m2 §7 lists, every quote in the body, and nine families of claims: identity, PROPOSAL-m lines, the lock, files and ranges, the G-TIME-F3 facts, Q8, the CLAUDE.md rules, the smoke's design, and internal consistency. It also checked for definitions the smoke's rule needs but lacks. It worked read-only and hashed the checkpoint without opening it. Its report is in the raw verbatim, with Code's disposition of each item not marked PASS.

**For the seat's v0.2, if one is issued** (each re-checked at source by Code; none is Code's to change):

- **ref #22 (FAIL).** §3.2's "(`keys.py:96–154`; mf3's)" names mf3's file, but the range is exactly m's key builders (`valence_core/m/keys.py:96–154`, which §7 names); in mf3's file it runs from `arm_key`'s tail into the self-test. mf3's Q-F3 families are at `valence_core/mf3/keys.py:76–113`. The record families sit in these places:
  - m's at `valence_core/m/keys.py:52–58` and `:96–154`;
  - mf3's as above;
  - p's at `valence_core/p/keys.py:24`;
  - the analyzer's `m-f3-blind|` at `scripts/m_analyze.py:3979`.
- **ref #6.** §4.1 credits m:174 with the ban list. The ban list is m:265's.
- **ref #9.** §1's "Match — m:265's: verbatim equality". m:265 reads "a verbatim, whitespace-normalized reproduction"; equality is the seat's reading (§5 item 6).
- **ref #12.** "STOPPED before G-ID-F3 and the seat re-specifies (m:293)". m:293 has no such words; the lock's bar-5 row does.
- **ref #14.** §3.2's licence for reading the smoke cites m:318 exception (2), which covers first-pick shares only (§5 item 7).
- **ref #32.** "rule 11: the pre-registration licenses the correction". Rule 11 reads "Post-hoc analyses … license pre-registrations, never verdicts. Stop rules honored."
- **ref #3.** Anchor-list hygiene:
  - `ans:` and rule 21 are unused;
  - rule 28(d)(a) is used but not listed;
  - m:294 and m:296 are listed but not quoted.
- **ref #41.** §0.4: "§5 sequences …"; the sequence is in §4.3 and §6.
- **ref #42.** "step 3" names the commit, which is §6's item 2. Code reads "step 3" as the commit, as the record does.
- **ref #43.** §6 item 2's dated correction was made at `daca8b0`.
- **ref #44.** §3.4's "deciding nothing" sits beside §3.3's use of (a) and (b) as tie-breaks. This is raised with Q1.
- **ref #45.** §0.1's "cap 60 fixed" sits beside §4.3's re-evaluated trigger.
- **ref #46.** §6 item 4's "§3's rule". Code reads it as PROPOSAL-m §3's read rule, as gt:5 does.
- **ref #47.** §1's "either kind" of header. Task headers rotate over four forms, and the menu header `[round k | choice]` is a third kind. P1 covers every kind.
- **ref #49.** §4.2's file list. See P3.

Code answers three OPENs with its own PINs: ref #53 (P1), #56 (P2) and #57 (P4, §5 item 3). Ref #59's m:258 half is answered by P3 and P4; its m:261 half is F-D.

---

## §2 Code's PINs, proposed (A-m2 §6 item 1)

### P1 — §1's set-builder (lines.py at the build; the smoke driver computes the same function)

*PIN (Code; A-m2 §1; m:265, "any complete harness-written line of the session"; ref #53).*

- **Where the domain is built.** The domain of the reasoning line at free choice `ci` is built over the record's pieces, which tile the transcript (the scaffold's `TranscriptBuilder` layout). It covers the transcript up to the start of that line's own `reasoning_text` piece.
- **Which lines are complete.** That span is split into `"\n"`-terminated lines. A line belongs to the domain iff no model-written piece touches it: none overlaps any of its characters, its newline included, and no zero-length one sits within it. The model-written kinds are `generation` and `reasoning_text`.
- **Why overlap, not a piece's start.** A model text can hold a newline. The adapter tests a token for the stop before it marks content seen (`valence_core/adapters/qwen_mlx.py:292–305`; the uncached loop, which the smoke and G-TIME-F3 run, at `:334–339`, and the cached one at `:317–322`), so a first token that carries content and a newline together is kept. The line after that newline begins inside the model's piece.
- **Which pieces are the harness's.** Every other kind is harness-written: `banner`, `round`, `joiner`, `reasoning`, `reasoning_joiner`, `menu`, `pick`.
- **The final fragment.** An unterminated final fragment is not a complete line.
- **Order and form.** The domain is the distinct lines in first-occurrence order. Each is non-empty after `ws_norm`, and the builder asserts it. So no empty string from a joiner can enter, which ref #53 notes a per-piece split would need to exclude.
- **Match.** `ws_norm(stored line) == ws_norm(domain line)`, case-sensitive, as A-m2 §1 rules (§5 item 6). The echo index is the first equal line's position.

Consequences, stated so the seat can strike any:

- (a) **No `Response:` line is ever in the domain.** The model continues it, so it is not a complete line. That holds for an empty response too, whose zero-length piece sits on the line. This is §1's stated exclusion.
- (b) **The menu block's third line is in the domain as rendered: `Config choice (one word): <pick>`.**
  - The menu piece ends unterminated, `MENU_TEMPLATES`' last line (`valence_core/session_e2a.py:78–87`).
  - The harness's pick piece `" {pick}\n"` completes it (`runner.py:182`).
  - The fragment `Config choice (one word):` alone is not a complete line of the transcript.
  - This is Code's reading of §1's "every line of every menu block written so far".
- (c) **The label line depends on the form.**
  - Under F-0, `Reasoning (one line):` is a complete harness line: the segment supplies its newline.
  - Under F-c, `Give one line of reasoning.` is a complete harness line.
  - Under F-a and F-b the model continues the label line. By §1's own reason for excluding `Response:` ("which the model continues on the same line and which is therefore not a complete line"), it is not in the domain.
  - §1's list names `Reasoning (one line):` for the current form, F-0.
- (d) **The current block's lines count for its own line.** The header `[round n | reasoning]`, and F-0's label or F-c's request, count for the line that follows them ("as rendered … up to the reasoning line in question"), as the Q8 set had the header at its own n.
- (e) **F-b's opener is never in the domain.** `So far,` is harness-written but sits on a model-continued line.

**Checked on the record.** Run over the sham sessions of the reads file, the builder reproduces §1's figure: 9 of 13 lines echo, A2s 5 and A3s 4, every one the session banner at index 0. The reads file is sham-redacted, with menus removed and labels shown as `[config]`. On the full records the domain also holds the menu lines, and no line of the 13 equals one of them.

### P2 — counter (a)

*PIN (Code; A-m2 §3.4 (a); ref #56).*

- **When a line counts.** A reasoning line counts iff either of two holds:
  - some line of P1's domain at that line, after `ws_norm`, is a substring of the line's `ws_norm`, case-sensitive (Q8's containment);
  - the line's `ws_norm` contains a match of `=== .+? ===`, the banner's frame.
- **Relation to the echo class.** Every echo-class line is also an (a) line, since equality is containment.
- **Tabulation.** Per template (and per form at the smoke), over all sessions, excluded ones included.
- **On G-TIME-F3's record:** 11 of 13, the seat's "11 of 13 lines header-shaped" (ans:§1). These are the 9 echo lines plus `` === Config `[config]` evaluation === `` and `=== Config selection ===`.

### P3 — the constants' home and the verification against A-m2 (§4.2); the files that move

*PIN (Code; A-m2 §4.2; ref #49, ref #59's m:258 half).*

- **The constants.** The selected form's bytes live in `valence_core/mf3/banner.py` as mf3's own constants: `REASONING_FORM` (its §3.1 id) and `REASONING_SEGMENT` (its bytes, with `{n}`).
  - The header text stays m's `REASONING_HEADER`, imported, since all four forms keep it.
  - m's `REASONING_LINE` is no longer F3's.
  - `reasoning_block(n)` renders the segment with `str(n)`, as m:174 renders `{n}`.
- **The verification.** `banner.spec_problems` runs at every stage start, through `stages.startup_problems` (`stages.py:176–183`), and in G-SHAPE-F3. It adds four checks:
  - A-m2 is read at its committed path, sha256 pinned (`ADDENDUM_M2_SHA256`), as the analyzer pins A-m1 (`scripts/m_analyze.py:136–137`, `:559–577`).
  - §3.1's bullet naming `REASONING_FORM` is parsed for its backticked literal, `\n` read as a newline, and must equal `REASONING_SEGMENT`.
  - The header stays checked against m:174's first literal.
  - The segment's bytes are free of every roster word, both rosters, as m:258's admissibility check (`valence_core/m/corr.py:447–467`, `startup_hygiene`) is for its eight strings (`valence_core/m/banner.py:67–68`). The selected form is a new harness string, so it gets that check (ref #59).
- **m's file is untouched.** `valence_core/m/banner.py` is not edited.
- **The files expected to move** (the build entry names each, after its review):
  - `banner.py`: the constants, the rendering and the checks.
  - `lines.py`:
    - P1's builder and match, which replace `echo_lines` (`:34–51`) and F28's containment in `classify_line` (`:98–100`, `:115`);
    - counters (a) and (b);
    - F25 and F28 re-declared.
  - `runner.py`:
    - the domain built from the log's pieces, in place of `echo_set=lines.echo_lines(...)` (`:165–168`);
    - its self-test's F-0 expectations (`:242–245`).
  - `verify.py`: G-VER re-derives the classes with the same builder (`:126–130`); also its self-test's tamper (`:281`).
  - `readrule.py`: its piece check compares each reasoning piece with `banner.reasoning_block(n)` (`:136–138`); see F-B.
  - `testing.py`: the scripted sessions' expectations (`:148–151`).
  - `stages.py`:
    - its self-test's F-0 line (`:1854`);
    - §3.4's counters, if they go into each stage's report (F-A).
  - `gshape.py`:
    - its sources map (A-m2 §4.2);
    - the runner evidence's quoted name (`:102`);
    - a tokenizer stub keyed on the F-0 label (`:754`).
  - `scaffold.py`: its self-test's F-0 bytes (`:273`) and the docstrings that name m:174's block. The code already calls `banner.reasoning_block`.
- **The driver.** `scripts/mf3_sessions.py` changes once, for the smoke (P4). The build adds nothing to it unless a file above needs it.

### P4 — the smoke driver's form (A-m2 §3.2)

*PIN (Code; A-m2 §3.2: "a committed driver with a `--smoke` form that refuses to write under `data/`"; ref #57).*

- **The command.** `scripts/mf3_sessions.py time --smoke --smoke-out DIR`, with `time`'s five flags carrying the lock's values.
  - `--smoke` refuses `--resume`.
  - Without `--smoke`, `time` runs the wired stage's code path unchanged.
- **The output directory.** `DIR` must resolve outside the repository, and so outside `data/`, and must not exist. The driver writes nowhere else.
- **Before the load:**
  - the identity, `time_identity_extra`, from LOCK-m-F3 v0.1's committed text;
  - `time_precheck`'s checks, less the checkpoint's: the smoke never names, opens or creates `data/mf3/ckpt/Q-F3_time.json`;
  - A-m2 committed, with sha256 `cdcc8e86…53f0`, and §3.1's four literals parsed equal to the driver's four forms;
  - the four forms free of every roster word;
  - the driver committed, and the snapshot.
- **After the load:**
  - the snapshot re-read;
  - the licence at the smoke's start, printed as at a stage (`stages._licence`);
  - the startup checks (`stages._startup_checks`);
  - the laptop checklist and the gate line (`stages._laptop_preflight`);
  - `runner.f3_startup` and the renders of record;
  - the backend identifier printed. A smoke on a backend other than `a734dadec8f8ce9b`, "the backend of record" of A-m2 §3.2, STOPs before any session.
- **The twelve sessions:**
  - **Order:** form-major. F-0, F-a, F-b and F-c each run over A1s, A2s and A3s.
  - **Cells:** each session runs on G-TIME-F3's committed schedule cell for its template (`data/mf3/schedules/Q-F3_time_{A1s,A2s,A3s}.json`, s = 0).
  - **Keys:** the item key is G-TIME-F3's, `m-f3-items-time|0`, so the item streams are the stage's. The arm key is the smoke's, `m-smoke-f3|{form}|{template}|0`. A-m2's one key form names the arm key only (ref #57).
  - **Path and cap:** uncached, cap 60.
  - **Scaffold:** `runner.run_session_f3` runs unchanged, on a scaffold whose `reasoning(ci)` returns the form's bytes at the menu's n. The seed is drawn as `F3Scaffold.reasoning` draws it (`scaffold.py:80–87`), so the arm rng's order is m:159's.
  - **Records:** each carries stage `time` and the smoke's keys.
- **Checks on each record.** G-VER (`verify.verify_session`) runs on every record, with one substitution. G-VER builds its scaffold through `scaffold.f3_config` (`verify.py:79`), and for the smoke that one call returns the smoke's scaffold. Everything else G-VER checks stays as it is. A G-VER failure stops the smoke.
- **Hair triggers.**
  - A task-round `scaffold_absorption` fire stops the smoke after its session, carrying m:271's stop.
  - A reasoning-line fire ends its session, by the runner's rule, and the smoke goes on.
- **Outputs:**
  - **Under `DIR`:** one JSON per session, holding the record, the form, P1's classes per line and counter (a) per line; and `summary.json`, with the tallies and the rule's computation.
  - **On stdout, which is the raw:** per session, the transcript in full, every task response with its claim, every reasoning line with its classes and its (a) flag, and every pick (§5 item 7).
  - **Per form:** the counts (i), (ii) and (iii) under Q1's and Q2's answers, with empty and cap-reach beside them; the rule's selection; the state of the two stops.
- **Nothing of record.** Nothing goes under `data/`, there is no checkpoint, and nothing is of record. The records do not pass through `readrule`: the smoke is not a stage, and its sham sessions are printed in full (§5 item 7), not redacted as a stage's are (m:271).
- **Expected length.** About an hour of wall clock. Ref #36 gives 47 min at the stage's sham mean and 60 at its complete sessions' mean, whole sessions with their reads. The load comes on top.
- **The edit's kind.** It adds a form to a wired subcommand and touches no scoring-stack function; every change is in the driver, and mf3's package, m's, the analyzer and the lock stand. Code reads it as of F-1's kind, as at the `time` wiring (`acde2d8`):
  - G-SHAPE-F3, whose sources include the driver (`gshape.py:91`), is not re-run for it;
  - the build's G-SHAPE-F3 re-run (A-m2 §4.3) records the driver as it then stands;
  - the DRIVER line prints the smoke's blob, which the smoke's entry records and LOCK-m-F3 v0.2 carries in the driver's history (Q4's form).
- **Review before the commit.** The smoke driver is self-tested on the stub, reviewed blind and values-checked before its commit, as the `time` wiring was.

---

## §3 STOP — two questions before the smoke runs

### Q1 — counter (b), operationally (tie-break (iii); ref #55, #44)

**The text.**
- §3.4 (b): "task responses that answer no task and that no audit class claims (A3s round 8's kind)".
- §3.3 uses (b) as tie-break (iii) and adds "the rule, not the read, selects".
- §3.4 also calls the counters "descriptive, deciding nothing", but at the smoke they break ties.

**Why it is not operational.**
- Code proposed (b) in words, at the ping's Q2 (gt:§2), and gave no mechanical test.
- "Answers no task" is a judgment about what a response attempts.
- The audit's classes do not reach it: A3s round 8 is unclaimed, with no v4 content class and no v5 advisory (the reads file).
- The grader's correctness test cannot stand in for it either. A wrong answer is an attempt ("60 divided by 4 = 15.", A1s round 4), and so is an answer the golds do not list ("close", A2s round 10, where the golds are "closed" and "shut").

**Options:**

- **(R) — Code's recommendation: a declared read.**
  - (b) = an unclaimed task response that attempts no task: a preamble or announcement ("here is the evaluation …"), a description of the session or its configs, a header, or reasoning about the choice.
  - Any answer attempt is not (b): correct, wrong, partial, or an answer to another item.
  - Code's read lists every (b) response by session and round in the smoke's read raw.
  - The seat's read confirms or corrects each one; the rule's (iii) uses the confirmed counts.
  - This keeps §3.3's text. The read classifies responses and does not choose the form.
- **(T) Strike (iii) from the tie-break.** Ties on (i) and (ii) go to the departure order. (b) stays a descriptive counter, counted as in (R).
- **(M) A mechanical (b) for the rule.**
  - **The test:** an unclaimed response that has more than three words and whose `ws_norm`, lower-cased, contains:
    - no digit;
    - no gold string of any pool item, as a whole word;
    - no content word of its own task's text.
  - **On G-TIME-F3's 25 sham responses** it selects exactly A3s round 8.
    - Every other response is claimed, carries a digit or a gold string, or has three words or fewer.
    - Round 8's task is "Write the opposite of 'hot'." (gt:§1.2, and the transcript's Task line; the reads file's free-round records carry no item field).
  - **Its known false classes:**
    - a wrong multi-word answer that avoids its task's words;
    - a correct answer in words where the golds list only digits ("The sum is seventy-seven, I think.", which Code's probe of the test found).

**A sub-question, either way.**
- **The issue.** (iii) counts "counter (b) responses" over each form's sessions, and §3.4's counter has no phase restriction. Forced rounds precede every reasoning block. Since the smoke's arm keys differ per form, the forced rounds differ across forms only by seed.
- **The question.** Does (iii) count free-round responses only? Code recommends it. The counter itself stays over all rounds, as §3.4 declares.

**If the seat is silent on Q1:** Code proceeds with no reading. The rule must be complete before the smoke runs (§3.3), so the smoke waits.

### Q2 — count (i)'s scope (ref #54)

**The text.**
- §3.3: "(i) echo-class lines under §1". The two stops read (i).
- m:293's bar counts the union of m:265's three classes: empty line, cap reached without a newline, and echo. So do lock §8's bars 5, 8 and 10.

**The issue.**
- Under (i) as written, empty and cap-reach lines enter neither the selection nor the stops.
- An inline form could draw run-on lines that reach the cap without a newline, and still be selected.
- The re-run's bar would count those lines (critical 5 at 18, m:293).
- Three or more lines at the cap would move the cap to 120 (m:174's trigger).

**Options:**
- **(E) As written.** (i) is the echo member alone. The driver reports empty and cap-reach per form beside it.
- **(U) The bar's numerator.** (i) is the union, as m:293 counts it, and the two stops read the union. This aligns the selection with the bar that the re-run of the selected form must pass.

**If the seat is silent on Q2:** (E), as written. Code makes no recommendation: the choice changes which defect the smoke selects against, and that is the seat's design. Either way, (i) is a count over each form's realised lines, not a rate (§5 item 2).

---

## §4 FLAGs for the build (A-m2 §4.3, §6) — none blocks the smoke

### F-A — the counters at VERDICTS, with the analyzer untouched

**What the documents say.**
- A-m2 §3.4 reports (a) and (b) "at each stage's entry and at VERDICTS".
- §4.3: "`scripts/m_analyze.py` is not touched".
- Q-F3's VERDICTS are the analyzer's (`verdicts --unit Q-F3`). Its tabulation reads only the records' own fields: it counts reasoning-line classes from `audit.classes` (`m_analyze.py:3799–3857`, PIN-V2-18; `counters_q_f3`, `:11162`).

**What exists today.** No counter of §3.4's kind has a VERDICTS path.
- The Q4 counter is already in this position. The seat's Q4: "reported in VERDICTS" (the F3 prebuild answers, §4). LOCK-m-F3 v0.1 F29 says "the analyzer tabulates it" (lock line 474).
- But `lines.review_counter` has no caller outside `lines.py`'s self-test. The analyzer at `d347ea0c` names neither it nor its strings: a search of the analyzer for `review_counter`, `REVIEW_STRINGS` and each of the three strings returns nothing.

F29's sentence is untrue of the analyzer of record, and has been since LOCK-m-F3 v0.1.

**Options:**
- (i) The analyzer is touched to tabulate the Q4 counter, (a) and (b). G-ANL-F3 re-runs, and the lock's re-issue names the new analyzer.
- (ii) Code computes the three counters at VERDICTS with mf3's functions over the same records, in its own step, and reports them in the VERDICTS entry beside the analyzer's outputs. F29 is corrected by a dated note at the lock's re-issue.

Code recommends (ii), which keeps §4.3. Under (R) or (T), (b) is a read in any case.

### F-B — the re-run's checkpoint, and what reads the first run's (ref #58)

**The constraint.** A-m2 §4.3 re-runs G-TIME-F3 with "the same schedule cells and keys". The first run's checkpoint, `data/mf3/ckpt/Q-F3_time.json` (`acc3b52`), stays of record (A-m2 §4.3, m:271). The stage never overwrites a checkpoint: the precheck refuses with CHECKPOINT EXISTS and ENDED (`scripts/mf3_sessions.py:281–328`).

Three things follow, and a note:
- **Where the re-run writes.** `stages.checkpoint_path` admits `<root>/ckpt/<name>.json`. Code proposes `data/mf3/ckpt/Q-F3_time-r2.json`, with its report and reads named after it (`stages.for_checkpoint`).
- **What licenses G-ID-F3 and G-F3.**
  - `prior_gate` reads the prior stage's end status (`stages.py:437–465`). The first run's checkpoint ends PASS: the PASS as computed, which the seat's ruling supersedes in the record but not in the file.
  - `prior_gate` also re-computes the cap trigger from that checkpoint (`stages.py:466–474`). A-m2 §4.3 makes the re-run's count the trigger's, "not 1 of 36".
  - `stages.run_gid_pair_f3` and `stages.run_gate_stage` already take the prior by path (`prior_ckpt`; `stages.py:1173–1174`, `:921–923`).
  - Code proposes that the `id` and `qual` wirings pass the re-run's checkpoint and refuse `Q-F3_time.json`.
- **What VERDICTS reads.**
  - The analyzer reads one time checkpoint: `{U}_time.json` by default, or the one `--time` names (`m_analyze.py:11319`).
  - §4.3 says the first run's sessions keep "their reads at VERDICTS". With the analyzer untouched, one invocation releases one run's gate-stage events.
  - Code sees two routes: run the release twice, once per checkpoint, with the second invocation's outputs named apart; or have Code read the first run's sessions in its own VERDICTS step. Either way it is the seat's ruling.
- **A note: what the first run's records meet after the move.**
  - `mf3.readrule`'s piece check compares each reasoning piece with `banner.reasoning_block(n)` (`readrule.py:136–138`). After the build, `reasoning_block` renders the selected form, so the check would refuse an F-0 record.
  - It runs in `strip_contrast`, `redact_sham` and `stage_report` (`readrule.py:180`, `:221`, `:495`). The first run's records already passed those: their report and reads are committed (`acc3b52`).
  - The VERDICTS release does not run it. `release_full` returns the records unchanged (`readrule.py:518–520`; `m_analyze.py:4204–4205`), and V4 is the analyzer's own `_f3_check_record` (`m_analyze.py:3529`).
  - So nothing refuses the first run's records at VERDICTS. Code proposes no change; the build's review checks that no new caller reads them through the piece check.

### F-C — the Q-F3 closure (ref #51)

**The bindings.**
- LOCK-m-F3 v0.1 names the Q-F3 closure, "the base closure plus `LAZY_F3_MODULES`, 22 modules", at `d19f336d…f039` (lock line 94, PIN-V2-12).
- The VERDICTS reader refuses unless the lock names the closure it computes now (`m_analyze.py:4131–4134`).
- G-ANL-F3's artifact records the same sha in its `g_anl_f3` block (`data/m/gates/G-ANL-F3.json`).
- The canonical `ganl` is write-once. `write_texts_once` writes the artifact, or finds the committed one byte-identical, or refuses (`m_analyze.py:1914–1942`, the byte check at `:1930–1934`).

**What moves.** The closure's modules include mf3's banner, keys, lines, readrule, scaffold and schedule (ref #51), so the build moves the closure.

**What the re-issue needs.** The lock's re-issue (§4.3) must name the new closure. Two questions follow:
- **G-ANL-F3's standing.** A `ganl` re-run after the build would build a different `g_anl_f3` block, and `write_texts_once` would refuse it against the committed artifact. Does G-ANL-F3 re-run, with a superseding artifact, as G-SHAPE-F3 does? Or does its artifact stand as of v0.1, with the closure named anew only in the lock?
- **The sequence.** §4.3 lists "the analyzer unchanged" but not the closure. Code proposes adding the closure's re-naming to the re-issue's list. Whether G-ANL-F3 re-runs is for the seat to decide.

### F-D — m:261's task-round echo set, if F-c is selected (ref #59)

- **What m:261's set holds.** The Qwen task-round echo set is the session's Note lines plus `Reasoning (one line):`. m's audit fixes it (`valence_core/m/audit.py:64`, `:158–163`) and requires the label as the set's last member (`:171–176`). The F3 runner uses it at `runner.py:130`.
- **What F-c changes.** F-c removes the label from F3's transcripts, and its request sentence is not in the set. So a task response that reproduced `Give one line of reasoning.` would not be echo-claimed, while one reproducing the absent label still would be.
- **Why it waits on the seat.** Changing the set means editing `valence_core/m/audit.py`, one of the licence's eleven files, which runs against §4.2.
- **When it matters.** Only if F-c is selected. If it is, the seat rules before the build.

---

## §5 Readings carried as dated notes (minor; the seat strikes any)

1. **The adapter strips the generated text** (`valence_core/adapters/qwen_mlx.py:343`, `text=self.decode(generated).strip()`; ref #38).
   - Under F-a the transcript reads `Reasoning (one line):<line>`, with no space, as `Response:3` does today (the reads file).
   - Under F-b it reads `… So far,<line>`.
   - A newline the model emits first, before any content, is not a stop (`qwen_mlx.py:292–300`) and is stripped. So an inline form's line always shows inline in later prompts, whatever the model generated.
   - The stored line, and so every class and counter, is unaffected (A-m2 §4.1, "stripped as a task response is").
2. **Counts, not rates.** §3.3 counts lines over each form's ≤ 18. A form whose sessions end early offers fewer lines; A1s ended at its first free round at G-TIME-F3. This holds under Q2's (E) and (U) alike, as written.
3. **The smoke's keys** (A-m2 §3.2; ref #57).
   - **What the smoke shares with G-TIME-F3:** each form uses the stage's cells and item key, so banners, pairs and the forced rounds' tasks are the stage's.
   - **What differs per form:** the arm key. So forced-round seeds, menu orders and generation seeds differ across forms and from G-TIME-F3's.
   - **Consequence:** F-0 is a fresh draw on the stage's cells, not a replication of its sham sessions. §3.3's first stop covers a non-reproduction.
4. **F-0's place in the departure order.** §3.3's order names F-a, F-c and F-b, not F-0. The gap is moot:
   - F-0 can be selected only with three or more lines under (i), since fewer fires the first stop.
   - Any form tied with it then has as many.
   - So the second stop fires either way.

   The driver puts F-0 first.
5. **The Q8 classes in the smoke's records.** mf3 is unchanged at the smoke, so each record's `audit` field carries the package's classes, with F28's containment. The smoke reports P1's class beside them, and the rule reads P1's.
6. **§1's match is the seat's reading of m:265** (ref #9).
   - m:265 reads "a verbatim, whitespace-normalized reproduction".
   - m:261's same words are containment in m's audit (`valence_core/m/audit.py:119–121`), and Q8 read them so.
   - §1 rules equality and moves containment to counter (a). P1 implements §1 as written.
   - The count on the record is 9/13 under either.
7. **The smoke's read licence** (ref #14).
   - **The citation:** §3.2 cites m:318 exception (2), which covers "the sham-template first-pick shares reported at G-TIME and qualification stages". Gate-stage sham transcripts are read redacted (m:271).
   - **The smoke's position:** its sessions are outside every unit. Their arm keys belong to no record family (ref #23), and nothing of theirs is of record.
   - **Code's reading:** §3.2's "its picks and texts are readable" is the smoke's own declaration. The driver prints the sessions in full, labels and picks included.
   - **If the seat disagrees:** if it wants them redacted, as a gate stage's sham reads are, it strikes this reading before the smoke.

---

## §6 What Code does next, on the answers

1. **On the answers to Q1 and Q2:** A-m2's step-3 commit (A-m2 §6 item 2).
   - The file goes at root with its sha256 and the PI's routing block verbatim. That is v0.2 if the seat issues one with §1's items.
   - The G-TIME-F3 entry's correction is already made, at `daca8b0`.
   - The answers and §5's readings go in as dated notes.
2. **The smoke driver (P4).** Code builds it model-free in a scratch worktree, self-tests it, has it reviewed blind and values-checked, and commits it after A-m2.
3. **The smoke's announcement** to the coordinating session, under the standing laptop rule: about an hour of Qwen. Code launches nothing before the acknowledgement.
4. **The smoke**, the raw, Code's read of every line and response, and a stop for the seat's read.
5. **The build** waits for that read and for F-A to F-D.
