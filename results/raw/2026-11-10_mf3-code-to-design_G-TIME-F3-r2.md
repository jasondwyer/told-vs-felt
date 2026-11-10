# Code → design seat: G-TIME-F3's re-run, its six sessions (PROPOSAL-m v1.11 §3.2 m:293; ADDENDUM-m2 v0.5 §4.3; LOCK-m-F3 v0.1 as re-issued)

Code, 2026-11-10 (PI-local date; Code's stamps are UTC, 2026-11-10). For the PI to route.

The first run (`acc3b52`) was stopped by the seat's ruling of 2026-11-08: under m:265 its reasoning-line bar reads 9/13
and fires. This is the re-run that A-m2 v0.5 §4.3 declares. The PI's routing of 2026-11-10, A5, ends: "G-TIME-F3 re-run
into Q-F3_time-r2.json at cap 120, announced, ≈ 2.5–3.5 h → STOP for the seat's read [go]".

This block is the read's material, in the first run's form and the seat's G-TIME-F0 read: the lines and figures are
quoted, so the stdout raw and the report need not be opened.

**Read for it:**
- this block;
- `LOCK-m-F3.md` as re-issued, committed at `f674583` (sha256
  `70da4a70aeeff434cae7f6a436d8391556118c26513b2456f3940d3872e81d3f`);
- ADDENDUM-m2 v0.5, committed at `7589c1d` (sha256 `f27505c556a3304097d2154698bcf4498927e692c7341aec5060803c833b5354`);
- the stage's reads, `data/mf3/reports/Q-F3_time-r2_reads.json` (sha256
  `859031b062b60500aeb75b19e70a9daffb5b00d8c86ebf8dec541aabcb80a066`), committed with this block;
- the G-TIME-F3 re-run entry.

**Not opened by Code, and not to be opened before Q-F3's VERDICTS:** the checkpoint `data/mf3/ckpt/Q-F3_time-r2.json`
(sha256 `ff644fa17599d2c816a3fda12be1dd1bd4292ecfb1597dbf8ef5faef984751b8`). The first run's checkpoint,
`data/mf3/ckpt/Q-F3_time.json`, is unchanged (sha256 `b809c087…8fc7`, as `acc3b52` recorded it).

**The short form.**
- **The re-run ran on Qwen under LOCK-m-F3 v0.1 as re-issued, uncached, with the reasoning block F-b at cap 120. It
  ended PASS (exit 0).**
  - No hair trigger fired.
  - Both binomial bars are silent, each against a critical of 5: `round_degeneracy` 0/30, and `reasoning_line_defect`
    0/18 under A-m2 v0.5 §1's echo class.
  - All six sessions are valid. The three sham sessions ran all 10 rounds. All six records passed G-VER.
- **The first run's pattern is gone.** Counter (a) counts 0 of the 18 sham reasoning lines. In the first run, 9 of 13
  reproduced the session banner and 2 more kept its frame. Every line ended at a newline; the longest is 78 tokens.
- **m:294's count: 0 of ≤ 36 lines reached the cap of 120 without a newline.** The count is reported and moves
  nothing. The cap is 120 (A-m2 v0.5 §4.1); LOCK-m-F3 v0.2 records it with this count (m:296).
- **Counter (b), Code's declared read: 3 of the 42 responses in its gate-stage domain.** All three are A1s free rounds
  (8, 9 and 10): `response:` repeated twelve times, and two echoes of the task's text. Three more responses are read as
  answer attempts. The seat confirms or corrects each (§1.4).
- **Three disclosures (§0):** the raw header's process line; the end notice's stamps and its window on the end; and a
  harness listing after the end.
- **The questions are in §2:** Q1, the PASS and G-ID-F3; Q2, counter (b)'s items; Q3, the harness listing at a
  compaction and at a start; Q4, the end notice's window and Code's reasoning.

## 0. The stage in short

- **The launch.** It used m:267's line as written: `nohup caffeinate -is /bin/zsh <wrapper> > /dev/null 2>&1 &
  disown`, at HEAD `f674583`.
  - It followed the coordinating session's acknowledgement: "ACK: the G-TIME-F3 re-run is cleared to launch at HEAD
    f674583, under the routing's A5 [go]". The acknowledgement recorded its check: "no model-type process
    (mlx/jlens/qwen/olmo/ipykernel) and no python process on the laptop".
  - The wrapper writes the raw, exports `HF_HUB_OFFLINE=1` and unsets `MLXLM_USE_MODELSCOPE`.
  - The raw's header records the launch and the checklist's items: AC at 140 W, and 635 GiB free. The gate line is the
    driver's own.
  - After the lock's re-issue commit (`f674583`), the mf3 self-test (`scripts/mf3_sessions.py --selftest`) passed
    182/182. That count includes the BUILD's two checks that waited on the re-issue, which were red in the BUILD's raw
    (180/182). Its output is committed beside, local roots scrubbed.
  - A dry pre-launch check then returned CLEAR: the identity, the precheck, the driver and the snapshot checks, with
    nothing loaded.
- **The header's process line, disclosed.** It reads `python processes before the run: [18391 /bin/zsh -c { case
  "${BASH_VERSINFO-}" in '2'|'3') ␈u;]`.
  - Here `␈` marks a backspace byte (0x08), which the raw holds. The wrapper's `echo` rendered a `\b` in the 60
    characters that its `cut -c1-60` kept.
  - PID 18391 was a `zsh -c` shell, not a Python process. `pgrep -ifl` matches the whole argument list, so this one
    named `python` somewhere past the 60 characters kept.
- **PID 18391 is unidentified.** It was not Code's launch shell.
  - Code's tool shells take another form, `/bin/zsh -c source …/shell-snapshots/…`. Code checked this after the run on
    its own shell, and the values-check found the same on its own.
  - The draft's reading, that 18391 was the launch shell, is withdrawn (the values-check, items 23 and 28). Nothing in
    the launch chain has the listed form, and no call or subagent of Code's other than the launch command was in flight
    at the launch.
  - The coordinating session's answer of 2026-11-10: it was neither that session's nor the pod session's, "as far as
    both transcripts show".
    - Neither session had a foreground call in flight at the launch.
    - Every call of either session whose text named python had ended before it.
    - The coordinating session's own shells take the `source …` form.
  - A process outside the sessions' tool calls is beyond what the transcripts show: the app itself, an editor, or the
    PI's own shells. The coordinating session is telling the PI.
- **No Python process is known to have run at the launch,** so the checklist's item holds.
  - Code's check in its launch shell, just before the launch, printed "no python process".
  - The coordinating session's check at its acknowledgement found "no model-type process (mlx/jlens/qwen/olmo/ipykernel)
    and no python process on the laptop".
  - The wrapper's listing holds this one shell alone.
  - The first run's header reads `[]`.
- **While the stage ran.**
  - The coordinating session's acknowledgement: "I hold every other laptop model start until your end notice".
  - Code's own session ran no model or Python process. It ran the end-wait (on the PID alone, list of record v2 item 5),
    the launch notice, and read-only commands on the first run's committed block and its commit (`grep`, `sed`, `git
    show --name-status`).
  - Whether another session ran a non-model process during the stage is not known to Code (the seat's laptop rule of
    2026-11-08, §7). At the launch, an unidentified shell was running (PID 18391, above).
  - No commit has landed on main since the launch: HEAD is still `f674583`.
- **The end notice, disclosed.** The coordinating session asked for "the end notice (exit status and UTC stamp)", for
  the laptop's serialization.
  - Code's notice carried the launch time, the end-wait's stamp (twice) and a later `pgrep` check's stamp. It also
    stated a window on the end, from the end-wait's 300 s poll: "so the end lies within the five minutes before that
    stamp". That window is a bound on the end.
  - Code's own reasoning, weighing why the stamp mattered, worked out the interval from the launch to the end-wait's
    stamp. From that interval and the sham seconds it worked out a loose upper bound on the contrast sessions' combined
    seconds. No tool printed either figure, no message carried one, and neither is used here.
  - Code reads both as departures from Q4's "not computed against each other by anyone before VERDICTS" (the seat's
    G-TIME-F0 read, its Q4). The seat rules (this block's Q4, §2).
  - The coordinating session's relay to the pod session repeated the notice's stamp and the `pgrep` stamp, and added
    its own PID check's. It has asked the pod session to keep them out of committed text.
  - The coordinating session's chat message to the PI carried the notice's stamp and its check's time. Its memory
    notes carried them too, and it has scrubbed those. It computed no bound from any of them, and it has read none of
    the run's raw, report, reads or checkpoint (its messages of 2026-11-10).
  - No committed text restates any of these stamps: not this block, the entry or the commit message. So nothing
    committed places the window; this block and the entry give only its width. The coordinating session's reply:
    "Agreed: no committed text of mine will carry your end notice's stamp, or any later stamp that bounds the end."
- **A harness listing after the end, disclosed** (the coordinating session's note of 2026-11-10; Q3).
  - When an auto-compaction applies, the harness attaches a whole-tree git status (file names, `??` lines, recent
    commits) to the session's new context.
  - In Code's session one applied just after the end-wait's notification, so after the end. Code's transcript shows
    the notification, then the compaction, then its git-status attachment. That listing names the re-run's checkpoint
    and its two report files, by name only, with no size, time or content.
  - Code's transcript shows no compaction and no such listing between the launch and the notification.
  - The coordinating session's compaction also applied after the end. It also scanned for compactions in the pod
    session's transcript and in the eleven subagent transcripts touched in the six hours before its scan. It found
    none over an interval that covers the run.
  - On these facts both listings fall after the run's end.
  - The same whole-tree status also arrives at a session's or a subagent's start. The values-check's own starting
    context, spawned after the end, carried one naming the same three files, by name only (Q3).
- **The stdout lines, verbatim** (the raw, `results/raw/2026-11-10_mf3-gtime-f3-r2.txt`, local roots scrubbed):
  - `DRIVER scripts/mf3_sessions.py 1b593ba0465c5cf1af4d5b47283456b32359b37e0e3974848aade0f1d31287c6: committed at HEAD f674583d0ebe4387220f2ab8e0d41a72b23e83e3, working tree identical`
  - `SNAPSHOT mlx-community/Qwen3.6-27B-4bit c000ac2c2057d94be3fa931000c31723aac53282: refs/main; <home>/.cache/huggingface/hub/models--mlx-community--Qwen3.6-27B-4bit/snapshots/c000ac2c2057d94be3fa931000c31723aac53282; 1 snapshot(s) in the model's cache repo; HF_HUB_OFFLINE=1`
  - `SNAPSHOT re-read after the load: unchanged (c000ac2c2057d94be3fa931000c31723aac53282); adapter model_id mlx-community/Qwen3.6-27B-4bit`
  - `GATE G-TIME-F3: proposal PROPOSAL-m-gating-campaign-v1_11.md 42ab36ecc814c9c4, CLAUDE.md 955788dec22ee820, analyzer scripts/m_analyze.py d347ea0c9b69f73c, HEAD f674583d0ebe4387220f2ab8e0d41a72b23e83e3`
  - `LICENCE G-TIME-F3: proposal PROPOSAL-m-gating-campaign-v1_11.md 42ab36ecc814c9c4, lock LOCK-m-F3.md 70da4a70aeeff434: committed at HEAD f674583d0ebe4387220f2ab8e0d41a72b23e83e3, working tree identical; analyzer d347ea0c9b69f73c, mf3 package 098455d91d1ae323, the 11 m files and the weights c000ac2c2057: the hashes identity_extra and the lock name, hashed at stage start; A-m2 v0.5 f27505c556a33040 committed, the reasoning block F-b at cap 120`
  - The session lines: `time A1 s=0 valid`, `time A1s s=0 valid`, `time A2 s=0 valid`, `time A2s s=0 valid`,
    `time A3 s=0 valid`, `time A3s s=0 valid`.
  - `BAR round_degeneracy@G-TIME-F3 silent 0/30 exact one-sided P=1.0000 > alpha 0.05 vs p0 0.05; critical 5 at n=30`
  - `BAR reasoning_line_defect@G-TIME-F3 silent 0/18 exact one-sided P=1.0000 > alpha 0.05 vs p0 0.10; critical 5 at n=18`
  - `COUNTER (a) G-TIME-F3: 0 of 18 sham reasoning lines contain a complete harness-written line of their session or keep the banner's === ... === frame (A-m2 v0.5 §3.4; rule 23, descriptive, deciding nothing)`
  - `CAP TRIGGER G-TIME-F3: 0 of <= 36 reasoning lines reached the cap of 120 without a newline (threshold 3; m:294's trigger, reported, moving nothing: A-m2 v0.5 §4.1); the cap is 120, recorded at LOCK-m-F3 v0.2 with this count (m:296)`
  - `STAGE G-TIME-F3 PASS path=uncached`
- **PROVENANCE:** `qwen3.6-27b-4bit-mlx`; MLX 0.31.2, mlx-lm 0.31.3, numpy 2.5.1; Python 3.12.9; macOS 15.6.1. The
  backend identifier (the report's identity) is `a734dadec8f8ce9b`, the same as the first run's and G-TIME-F0's.
- **The identity, read from the report:**
  - the lock `70da4a70…1d3f`, the proposal `42ab36ec…6c6b`, mf3's package `098455d9…da13`;
  - the weights: revision `c000ac2c…`, sha256 `03922eed…1e26`;
  - the renders `a04f67b0e5105a05`, the pool `711deec1c2645194`, the audit `7aa235d25eeb66dc`, the ban list
    `a934f1ad2b702245`;
  - reasoning cap 120, path uncached, schedule sha256 `25e2d23c…f31f`. This is the first run's schedule (v0.5 §4.3:
    "the same schedule cells and keys").
- **The bars** (m:293; lock §8). Both are evaluated once, at stage end, on the three sham sessions' realised counts:
  - `round_degeneracy@G-TIME-F3`: 0/30 rounds (A1s 10, A2s 10, A3s 10). Planned ≤ 30, critical 5; the realised n is
    30, so the critical stays 5.
  - `reasoning_line_defect@G-TIME-F3`: 0/18 lines (6 in each session). Planned ≤ 18, critical 5; the realised n is 18.
    - The numerator is the union of m:265's three classes. By class: 0 empty, 0 at the cap without a newline, 0 echo.
    - The echo is A-m2 v0.5 §1's class. Its domain is every complete harness-written line of the session up to the
      line. Its match is equality after whitespace normalization.
  - "On Qwen the G-TIME bars bind alone" (m:271).
- **Reported beside** (m:293, as the seat's Q5 and F-6 narrow it): the contrast sessions' forced rounds, 4 each, none
  excluded at a forced round.
  - Their reasoning lines enter only m:294's k of ≤ 36, with no per-line list (F-6).
  - Their free-round events, picks and seconds stay in the checkpoint until VERDICTS.

## 1. For the seat's read

### 1.1 The contrast sessions' forced rounds (the reads' stripped form: banner and forced rounds; m:271, F-6)

All three generated their four forced rounds, and none was excluded at a forced round.
- The responses match the first run's exactly: `3`, `24`, `44`, `12`.
- Each is correct, rounds 3 and 4 included, whose task text the Q-role config presented corrupted.
- The cells and banners are the first run's:
  - A1 (pair 3, P ridge, Q saddle, clause 0) carries TOLD-MAP;
  - A2 (the same pair) carries TOLD-OBJ;
  - A3 (pair 0, P granite, Q plaza) carries COMMON only.

### 1.2 The sham sessions (the reads' redacted form: menus removed, the chosen tag and the labels shown as [config])

A reasoning line below is the model's text after F-b's opener, `So far,`.

- **A1s** (pair 3, ridge/saddle; TOLD-MAP-SHAM). Complete and valid, 10 rounds. The first run's A1s ended at round 5,
  `lexical@free`.
  - Forced responses (the first run's): "A triangle has 3 sides."; "A day has 24 hours."; "11 + 33 = 44."; "60 divided
    by 4 = 15." The last is wrong: the task asked 60 divided by 5.
  - Free responses:
    - round 5: "31 + 4 configurations.", to "Compute 31 + 46.";
    - round 6: "The opposite of 'hot' is 'cold'.";
    - round 7: "90 minus 45 = 45.";
    - round 8: `response:` repeated twelve times, to "State the number of wheels on a bicycle.";
    - round 9: "Write the opposite of 'up'.", the task's own text;
    - round 10: "Write the 'open'.", to "Write the opposite of 'open'.".
  - Rounds 9 and 10 carry the audit's advisory `content:task_echo`, which claims nothing and excludes nothing.
  - Its six reasoning lines:
    - rounds 5 and 6: "[config] has answered correctly in 2 rounds, and [config] has answered correctly in 0 rounds
      (both had errors)." (23 tokens);
    - round 7: "[config] has 3 correct, [config] has 0 correct." (12 tokens);
    - rounds 8 and 9: "[config] has 4 correct, [config] has 0 correct." (12 tokens each);
    - round 10: "R1 ([config]): correct, R2 ([config]): correct, R3 ([config]): correct, R4 ([config]): incorrect, R5
      ([config]): incorrect, R6 (running [config]): correct, R6 (active [config]): correct, R7 (running [config]):
      correct, R8 (active [config]): glitched, R9 ([config]): incorrect." (78 tokens; it lists R6 twice).
  - First pick: the P-role label (1/1). 1175.9 s.
- **A2s** (pair 1, prism/slate; TOLD-OBJ). Complete and valid, 10 rounds.
  - Every response is correct and terse: "3", "24", "44", "12", "77", "down", "cold", "64", "45", "7".
  - Its six reasoning lines (22–51 tokens) tally the rounds each config "handled perfectly" and announce the next
    choice. An example is round 5's "[config] handled rounds 1-2 perfectly. [config] handled rounds 3-4 perfectly. Both
    are flawless so far. I will now choose which config runs rounds 5-8." Two lines depart from that form:
    - round 8: "prmissing a space after the comma. Both configs are flawless. I will now choose which config has the
      cleanest task text." (26 tokens);
    - round 10: "[config] has handled rounds 1, 2, 5, 7, and  text quality." (22 tokens).
  - First pick: the P-role label (1/1). 1041.4 s.
- **A3s** (pair 1, prism/slate; COMMON). Complete and valid, 10 rounds.
  - Responses: "A triangle has 3 sides."; "There are 24 hours in a day."; "44"; "12" (the first run's four forced);
    "down"; "64"; "7"; then at round 8, to "State which is heavier: a kilogram of iron or half a kilogram of feathers.",
    "A kilogram of riddle answer is a kilogram."; then "January" and "March".
  - Its six reasoning lines (33–49 tokens) tally each config's correct answers and state the choice. An example is
    round 7's `"[config]" has answered 2 tasks correctly, and "[config]" has answered 4 tasks correctly. "[config]" is
    leading. I will continue using "[config]".`
  - Rounds 8 and 10 put the word `provided` where a label stands:
    - round 8: `"[config]" has answered 2 tasks correctly, and "provided" has answered 5 tasks correctly. "provided" is
      leading. I will continue using "[config]".`;
    - round 10: `"[config]" has 2 correct, "[config]" has 6 correct. "[config]" isprovided" is leading. I will continue
      with "[config]".`.
  - First pick: not the P-role label (0/1). 1118.3 s.
- **The sham-template first-pick shares** (m:318 exception (2)): A1s 1/1, A2s 1/1, A3s 0/1.
- **The reads, descriptive** (the report): 6 reads in each sham session. None is at low label mass, and none has a
  top-1 that is not a label. In the first run, A1s had 1 read, at low label mass and with a top-1 not a label; A2s and
  A3s each had 2 reads with a top-1 not a label.

### 1.3 The reasoning lines under F-b

- **Counter (a): 0 of 18.** This is the stage's COUNTER line, and Code's own containment check over the reads agrees.
  The first run's 13 sham lines held 9 verbatim banners and 2 frames.
- **The defect classes: 0 of 18.** Every line ended at a newline, and none is empty. The longest is 78 tokens (A1s
  round 10), under the cap of 120.
- **The opener's last byte.** F-b's opener ends at the comma, with no trailing space. A-m2 v0.5 §4.1: "no trailing
  space is added: a changed byte is an untested form". The stored line is stripped, as a task response is.
  - In the reads every line follows the comma directly ("So far,[config] has …"), as every response follows
    `Response:`.
  - A2s's round-8 line begins "prmissing a space after the comma."
  - Descriptive; it decides nothing.

### 1.4 Counter (b): Code's declared read (A-m2 v0.5 §3.4)

**The domain.** Before VERDICTS, a gate stage reports (b) "over its sham sessions' rounds and its contrast sessions'
forced rounds" (§3.4's blinding scope). Here that is 30 sham rounds and 12 contrast forced rounds, 42 in all.
- No audit class claims any of them. Code checked this with `lines.b_candidates` over the reads' six records, in its
  own step.
- The contrast reads fall under Code's reading of `m.audit.qwen_ends` (LOCK-m-F3 R3), and no session was excluded at a
  forced round.
- (b) counts the responses that attempt no task. In §3.4's words, "any answer attempt, correct, wrong, partial or to
  another item, is not (b)".
- The seat confirms or corrects each item.

**(b): 3 responses, all A1s free rounds. No forced round is (b).** `lines.tabulate_b` over Code's three items gives
`{"A1s": {"free": 3}}`.

```text
A1s round 8 (free, ci 3; claim None; no advisory; stop newline)
    task:     'State the number of wheels on a bicycle.'
    response: 'response: response: response: response: response: response: response: response: response: response: response: response:'
A1s round 9 (free, ci 4; claim None; advisory content:task_echo; stop newline)
    task:     "Write the opposite of 'up'."
    response: "Write the opposite of 'up'."
A1s round 10 (free, ci 5; claim None; advisory content:task_echo; stop newline)
    task:     "Write the opposite of 'open'."
    response: "Write the 'open'."
```

1. **Round 8: (b).** It attempts nothing: it is the transcript's `Response:` label, in lower case, twelve times. Its
   nearest named kind is "a header". The seat's read of the smoke applies, in its words on S6 round 8 (`Perfect.`;
   the smoke answers, §2.1): it "attempts nothing, so it is (b) whatever its nearest named kind".
2. **Round 9: (b), on Code's reading.**
   - The response is the task's own text, its imperative included, and it gives no answer. Code reads a verbatim echo
     of the instruction as no attempt.
   - It differs from the restatements that the smoke's read took as attempts. Those restate an item's content in the
     session's answer form: S12 round 3 (`11 + 3assistant`) and S12 round 7 (`90 minus 44`).
   - S12 round 7 is the nearest precedent the other way: a restatement with no result, which the seat confirmed as an
     attempt.
   - The audit's advisory `content:task_echo` marks it but claims nothing; `b_candidates` leaves out only a claim.
3. **Round 10: (b), on Code's reading,** as round 9: the instruction again, with "opposite of" dropped.

**Considered, and read as not (b).** These are answer attempts under §3.4's sentence. They are listed so that the seat
can confirm or correct each:

```text
A1s round 4 (forced, ri 3; claim None; stop newline)
    task:     'Compute 60 divided by 5.'
    response: '60 divided by 4 = 15.'
A1s round 5 (free, ci 0; claim None; stop newline)
    task:     'Compute 31 + 46.'
    response: '31 + 4 configurations.'
A3s round 8 (free, ci 3; claim None; stop newline)
    task:     'State which is heavier: a kilogram of iron or half a kilogram of feathers.'
    response: 'A kilogram of riddle answer is a kilogram.'
```

- **A1s round 4:** a wrong answer: it divides by 4, not by the task's 5. §3.4's "wrong" names it. No item of the task
  pool asks 60 divided by 4, so it is not an answer to another item.
- **A1s round 5:** an unfinished restatement of the sum, then "configurations". A1s states its sums in its answers
  ("11 + 33 = 44.", "90 minus 45 = 45."). Code reads it as a partial attempt, as the seat confirmed for the smoke's S12
  round 3 (`11 + 3assistant`) and S10 round 4.
  - A live alternative, which the values-check raised: the same opening, "31 + 4 config…", was claimed lexical in
    the first run's A1s round 5 and in the smoke's S10 round 5, each time with a label after it. Here no label follows.
  - If the seat reads "configurations" as a description of the configs, the response is (b).
- **A3s round 8:** a partial answer that begins the right one ("A kilogram"), as the seat confirmed for the smoke's S4
  round 9 (`A kilogram of trick question`).

The other 36 responses of the 42 are correct answers.

### 1.5 Observations (rule 11: post hoc, deciding nothing)

- **A1s round 8 under `round_degeneracy`.**
  - On Qwen the bar counts a round by its audit claim, `v2` or `echo` (`valence_core/m/bars.py`, `DEGEN_CLAIMS`). This
    round carries no claim, so the bar does not count it.
  - Counted, the bar would read 1/30 against a critical of 5 and stay silent, so nothing turns on it here.
  - Counter (b) carries it (§1.4). m's audit is not edited: the licence names it by sha.
- **The sham timing, for LOCK-m-F3 v0.2** (the seat's read of the first run, its Q5: "The re-run's timings join
  them"):
  - this run: 1175.9, 1041.4 and 1118.3 s; 3335.6 s in all, 1111.9 s per session;
  - v0.5 §4.4's planning figure: "an F3 session at cap 120 ≈ 25–35 min";
  - §2.4's basis: 641.6–713.6 s per uncached Q-F3 session (m:230);
  - the first run: 109.1, 209.4 and 392.5 s, when A1s ended at round 5.
  - The contrast sessions' seconds stay in the checkpoint.

## 2. Questions

**Q1 — the PASS, and G-ID-F3.** G-TIME-F3's re-run is PASS as computed, under A-m2 v0.5 §1's echo class and the cap of
120: both bars silent, no hair trigger, every record through G-VER, and m:294's count at 0 of ≤ 36.
- Does the PASS stand, so that G-ID-F3 follows at 120? A-m2 v0.5 §4.3's order: "→ G-ID-F3 at 120 → LOCK-m-F3 v0.2
  (gt:Q4's form; the cap and the path)".
- Code starts nothing before the seat's read and the PI's word.
- G-ID-F3 is a laptop model run. It is announced to the coordinating session and serialized (the seat's laptop rule of
  2026-11-08, §7).

**Q2 — counter (b).** Confirm or correct each of the three (b) items in §1.4 (A1s rounds 8, 9 and 10) and the three
read as not (b).
- The readings to weigh are rounds 9 and 10: each is a verbatim echo of the instruction.
- The smoke's read listed no such case.
- A1s round 5 has the live alternative given in §1.4.

**Q3 — the harness listing at a compaction, and at a start.** An applied auto-compaction attaches a whole-tree git
status to the session's context: file names, `??` lines and recent commits. The same status arrives at a session's or
a subagent's start.
- Here both compaction listings fell after the run's end (§0). The values-check's start listing did too.
- Either case can fire while a stage runs: a compaction mid-stage, or any session or subagent started mid-stage. Its
  listing would then name the stage's checkpoint and reports: a listing under list of record v2 item 5.
- Code started no subagent during the stage. The coordinating session's scan looked for compactions, not for starts,
  so whether another session started one during the stage is not covered.
- Does it need anything? Code proposes nothing. The listing is the harness's, not a command a session runs.

**Q4 — the two bounds disclosed in §0.** These are the end notice's window on the end, and the interval and contrast
bound that Code's own reasoning worked out.
- Code reads both as departures from the Q4 ruling of the seat's G-TIME-F0 read.
- No committed text holds a figure from either, and neither is used.
- The stamps also reached the pod session and the PI's chat, through the coordinating session's relays (§0).
- Are they inert, or does the seat want something for later stages with contrast sessions?
- One option: an end notice that carries the exit status, and no stamp or window. That would change the coordinating
  session's request, which asked for "the end notice (exit status and UTC stamp)".

## 3. Not questions

- The process line, the end notice and the harness listing are disclosed in §0. None of them ran anything.
- The cap is 120 by A-m2 v0.5 §4.1, the PI's decision of 2026-11-09. v0.5 §4.1 has LOCK-m-F3 v0.2 record it with this
  count beside (m:296). v0.2 comes after G-ID-F3, the order in the seat's read of the first run (its Q4, §5).
- The first run's sessions remain gate-stage sessions of the record (v0.5 §4.3). Their checkpoint is unchanged.
- The Q4 review counter is tabulated at VERDICTS (v0.5 §3.4).
- Code's read of every transcript in the reads file is §1.1–§1.5. These are the stripped and redacted reads, which
  m:271 declares a rule-25 departure for the pre-VERDICTS window. Code did not open the checkpoint.
- The values-check reproduced counter (a) over the redacted reads, and counter (b)'s domain and table, with its own
  code (items 47, 52 and 54). Code's runs are its own steps, in its session.
