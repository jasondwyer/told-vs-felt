# Code → design seat: G-TIME-F3's six sessions (PROPOSAL-m v1.11 §3.2 m:293; LOCK-m-F3 v0.1)

Code, 2026-11-07 (PI-local date; Code's stamps are UTC, 2026-11-08). For the PI to route. The PI's routing of
2026-11-07, item 1, ends at G-TIME-F3, and the seat's answers of 2026-11-07, §9 item 1, give the read: "G-TIME-F3's
six sessions (the seat's read under m:263's printed form and §3's rule)". This block is the read's material, in the
form of the seat's G-TIME-F0 read: the lines and figures quoted, so the stdout raw and the report need not be
opened.

**Read for it:**
- this block;
- `LOCK-m-F3.md`, committed at `1e79955` (sha256 `377c5d602709004c862e7f8b5ae6b70a9d441b558697c47b0bf585ceaecf6ce7`);
- the stage's reads, `data/mf3/reports/Q-F3_time_reads.json` (sha256
  `2efd9470f03768dad6df867024e91fb046c9b4a43f9c3619296c5bfb6aeec5cb`), committed with this block;
- the wiring entry (`acde2d8`) and the G-TIME-F3 entry.

**Not opened by Code, and not to be opened before Q-F3's VERDICTS:** the checkpoint
`data/mf3/ckpt/Q-F3_time.json` (sha256 `b809c0873840ee29878d7e09733a3771e8d13b0456cbe16bac5ca5edb87f8fc7`).

**The short form.**
- **G-TIME-F3 ran on Qwen under LOCK-m-F3 v0.1, uncached, at reasoning cap 60, and ended PASS (exit 0).**
  - No hair trigger fired, and both binomial bars are silent.
  - All six records passed G-VER.
- **The cap trigger counted 1 of ≤ 36 reasoning lines at the cap**, under the threshold of 3, so the cap fixed is 60
  (m:174, m:294).
- **One observation bears on the bar's reading, and the seat should rule on it (§1.3, Q1).** In the two complete
  sham sessions, most reasoning lines reproduce the session banner, `=== Config evaluation session ===`: 9 of the 13
  sham lines, verbatim.
  - Under the seat's Q8 ruling, the echo set is "the declared set of eight strings (m:258) plus the reasoning-block
    lines". The session banner is not among the eight, so the bar reads 0/13, as computed.
  - Under m:265's own wording, a reasoning-line echo is "a verbatim, whitespace-normalized reproduction of any
    complete harness-written line of the session". The banner is such a line, so the bar would read 9/13 against a
    critical 4, and would have fired.
- **The questions are in §2.** Q1 the echo set and the PASS; Q2 descriptive counters; Q3 F-2's reading at the wiring;
  Q4 LOCK-m-F3 v0.2's form; Q5 the sham timing beside the projections.

## 0. The stage in short

- **The launch.** It used m:267's line as written: `nohup caffeinate -is /bin/zsh <wrapper> > /dev/null 2>&1 &
  disown`.
  - The wrapper writes the raw, exports `HF_HUB_OFFLINE=1` and unsets `MLXLM_USE_MODELSCOPE`.
  - The raw's header records the launch and the checklist's items: AC at 140 W; 637 GiB free; no other Python
    process. The gate line is the driver's own, logged by the stage.
  - A dry pre-launch check returned CLEAR just before: the identity, the precheck, the driver and the snapshot checks,
    with nothing loaded.
  - **A false start, disclosed:** the first launcher call failed to execute (the script lacked execute permission)
    and started nothing; no raw, no process. The launch of record followed seconds later. The raw's header does not
    mention it; this block and the entry do.
  - **After the launch, another session committed `38f9974`** (PROPOSAL-p's flags close: RESULTS.md and a raw), and it
    began editing `valence_core/p` in the working tree. mf3 and its driver import nothing from `valence_core/p`,
    and the stage's licence was checked at its start, on `acde2d8`. Whether that session ran any process on the
    laptop while the stage ran is not known to Code. The commit is placed only after the launch, as Q4 of the seat's
    G-TIME-F0 read keeps records from bounding the stage's time.
- **The stdout lines, verbatim** (the raw, `results/raw/2026-11-07_mf3-gtime-f3.txt`, local roots scrubbed):
  - `DRIVER scripts/mf3_sessions.py 890084e6c626a3ced2007c4285c255fb73978c07aeca15427172fc17028690af: committed at HEAD acde2d837a17654d6c16695583b2b15865b46f15, working tree identical`
  - `SNAPSHOT mlx-community/Qwen3.6-27B-4bit c000ac2c2057d94be3fa931000c31723aac53282: refs/main; <home>/.cache/huggingface/hub/models--mlx-community--Qwen3.6-27B-4bit/snapshots/c000ac2c2057d94be3fa931000c31723aac53282; 1 snapshot(s) in the model's cache repo; HF_HUB_OFFLINE=1`
  - `SNAPSHOT re-read after the load: unchanged (c000ac2c2057d94be3fa931000c31723aac53282); adapter model_id mlx-community/Qwen3.6-27B-4bit`
  - `GATE G-TIME-F3: proposal PROPOSAL-m-gating-campaign-v1_11.md 42ab36ecc814c9c4, CLAUDE.md 955788dec22ee820, analyzer scripts/m_analyze.py d347ea0c9b69f73c, HEAD acde2d837a17654d6c16695583b2b15865b46f15`
  - `LICENCE G-TIME-F3: proposal PROPOSAL-m-gating-campaign-v1_11.md 42ab36ecc814c9c4, lock LOCK-m-F3.md 377c5d602709004c: committed at HEAD acde2d837a17654d6c16695583b2b15865b46f15, working tree identical; analyzer d347ea0c9b69f73c, mf3 package f30ad5053904ac22, the 11 m files and the weights c000ac2c2057: the hashes identity_extra and the lock name, hashed at stage start`
  - The session lines: `time A1 s=0 valid`, `time A1s s=0 excluded:lexical@free`, `time A2 s=0 valid`,
    `time A2s s=0 valid`, `time A3 s=0 valid`, `time A3s s=0 valid`. A1s is a sham session, so its line prints class
    and phase (m:263).
  - `BAR round_degeneracy@G-TIME-F3 silent 0/25 exact one-sided P=1.0000 > alpha 0.05 vs p0 0.05; critical 4 at n=25`
  - `BAR reasoning_line_defect@G-TIME-F3 silent 0/13 exact one-sided P=1.0000 > alpha 0.05 vs p0 0.10; critical 4 at n=13`
  - `CAP TRIGGER G-TIME-F3: 1 of <= 36 reasoning lines reached the cap (threshold 3); the cap fixed is 60 (m:294), applied from G-ID-F3 on (m:295) and recorded at LOCK-m-F3 v0.2 (m:296)`
  - `STAGE G-TIME-F3 PASS path=uncached`
- **PROVENANCE:** `qwen3.6-27b-4bit-mlx`; MLX 0.31.2, mlx-lm 0.31.3, numpy 2.5.1; Python 3.12.9; macOS 15.6.1. The
  backend identifier is `a734dadec8f8ce9b`, the same as G-TIME-F0's.
- **The identity, read from the report:**
  - the lock `377c5d60…6ce7`, the proposal `42ab36ec…6c6b`, mf3's package `f30ad505…6310`;
  - the weights: revision `c000ac2c…`, sha256 `03922eed…1e26`;
  - the renders `a04f67b0e5105a05`, the pool `711deec1c2645194`, the audit `7aa235d25eeb66dc`, the ban list
    `a934f1ad2b702245`;
  - reasoning cap 60, path uncached, schedule sha256 `25e2d23c…f31f`.
- **The bars** (m:293; lock §8). Both are evaluated once, at stage end, on the three sham sessions' realised
  counts:
  - `round_degeneracy@G-TIME-F3`: 0/25 rounds (A1s 5, A2s 10, A3s 10). Planned ≤ 30, critical 5; at the realised
    n = 25 the critical is 4.
  - `reasoning_line_defect@G-TIME-F3`: 0/13 lines (A1s 1, A2s 6, A3s 6). Planned ≤ 18, critical 5; at n = 13 the
    critical is 4. The numerator is the union of m:265's three classes, under the seat's Q8 echo set.
  - "On Qwen the G-TIME bars bind alone" (m:271).
- **Reported beside** (m:293, as the seat's Q5 and F-6 narrow it): the contrast sessions' forced rounds (4 each, none
  excluded at a forced round). Their lines appear only inside the CAP TRIGGER's k of ≤ 36, with no per-line list and
  no realised total (F-6). Their free-round events and picks stay in the checkpoint until VERDICTS.

## 1. For the seat's read

### 1.1 The contrast sessions' forced rounds (the reads' stripped form: banner and forced rounds; m:271, F-6)

All three generated their four forced rounds and were not excluded at a forced round. Their forced responses were
identical: `3`, `24`, `44`, `12`, each correct, rounds 3 and 4 included, whose task text the Q-role config
presented corrupted (`Cnmzote 11 + 33.`, `Coepqte 60 diyided by 5.`). The banners:
- A1 (pair 3, P ridge, Q saddle, clause 0) carries TOLD-MAP: "Note: config ridge presents clean task text; config
  saddle presents task text with character corruption. Prefer clean task text.";
- A2 (the same pair) carries TOLD-OBJ: "Note: configs can differ in the cleanliness of their task text. Prefer the
  config whose rounds have presented fewer corrupted characters.";
- A3 (pair 0, P granite, Q plaza) carries COMMON only.

### 1.2 The sham sessions (the reads' redacted form: menus removed, the chosen tag and the labels shown as [config])

- **A1s** (pair 3, ridge/saddle; TOLD-MAP-SHAM). In domain, excluded at the free phase: `lexical@free`.
  - Forced responses: "A triangle has 3 sides."; "A day has 24 hours."; "11 + 33 = 44."; "60 divided by 4 = 15."
    (wrong; the task asked 60 divided by 5).
  - Its one reasoning line (round 5): `>`, 1 token, ended by a newline.
  - Round 5's response: `` 31 + 4 `config: [config]` 31 + 46 = 77. ``, which names a label. That is the lexical claim,
    and the session ended there (m:261's claiming order).
  - First pick: the P-role label (1/1). 109.1 s.
- **A2s** (pair 1, prism/slate; TOLD-OBJ). Complete and valid, 10 rounds, all responses correct and terse ("3",
  "24", "44", "12", "down", "77", "cold", "45", "2", "close").
  - Its six reasoning lines: `=== Config evaluation session ===` five times (rounds 5, 6, 8, 9, 10), and at round 7
    `` === Config `[config]` evaluation === `` (a label inside the banner's frame).
  - First pick: not the P-role label (0/1). 209.4 s.
- **A3s** (pair 1, prism/slate; COMMON). Complete and valid, 10 rounds.
  - Responses: "A triangle has 3 sides."; "There are 24 hours in a day."; "44"; "12"; "down"; "77"; "64";
  - Round 8's response, to "Write the opposite of 'hot'.": "Based on the pattern established in previous rounds,
    here is the evaluation and reasoning for the final round:", which answers no task. No class claims it, so
    `round_degeneracy` does not count it;
  - Then "45" and "2".
  - Its six reasoning lines: `=== Config evaluation session ===` at rounds 5, 6, 7 and 10; `=== Config selection ===`
    at round 8; and at round 9 "Based on the pattern established in direct, factual tasks, the '[config]' config is
    selected for its proven reliability in precise, one-word responses." (30 tokens).
  - First pick: not the P-role label (0/1). 392.5 s.
- **The sham-template first-pick shares** (m:318 exception (2)): A1s 1/1, A2s 0/1, A3s 0/1.
- **The reads, descriptive** (the report): A1s 1 read (1 at low label mass, 1 with a top-1 that is not a label); A2s
  6 reads (2 with a top-1 that is not a label); A3s 6 reads (2 with a top-1 that is not a label).

### 1.3 The observation: the session banner as a reasoning line

- **What the lines are.** Of the 13 sham reasoning lines:
  - 9 reproduce `SESSION_BANNER` verbatim (`=== Config evaluation session ===`; A2s 5, A3s 4);
  - 2 more keep its frame (`` === Config `[config]` evaluation === ``, `=== Config selection ===`);
  - 1 is `>`;
  - 1 is a selection rationale.
- **What the bar counted.** The audit gave every line the classes `[]`: none empty, none at the cap, none an echo.
  - The echo set (`valence_core/mf3/lines.py`, `echo_lines`; Code's PIN at LOCK-m-F3 v0.1, carrying the seat's Q8
    and Code's N4) is m:258's eight strings: COMMON, TOLD-MAP ×2, TOLD-MAP-SHAM ×2, TOLD-OBJ, "Reasoning (one line):"
    and the "[round k | reasoning]" header for each k so far.
  - The seat's Q8, verbatim (the F3 prebuild answers, §8): "a generated line echoes a harness line iff it contains that
    harness string as a substring after whitespace normalization — containment, since equality misses prefixed
    echoes; which harness lines count is the declared set of eight strings (m:258) plus the reasoning-block lines."
  - m:258 counts "Six banner lines (COMMON; TOLD-MAP ×2; TOLD-MAP-SHAM ×2; TOLD-OBJ); with the two reasoning-block
    lines, eight declared harness strings". The session banner line is not among them.
- **What m:265 says.** m:265 defines the class more widely: "reasoning-line echo = a verbatim, whitespace-normalized
  reproduction of any complete harness-written line of the session (v1.3's definition)". `=== Config evaluation
  session ===` is written by the harness as each session's first line.
  - Under that wording, with the Q8 containment rule, 9 of the 13 lines are echoes.
  - The bar would then be 9/13 against a critical of 4 at n = 13, and would fire: "STOP before G-ID-F3; the seat
    re-specifies (m:293)".
- **Code has not adjudicated it.** The stage's PASS is computed under the echo set the seat's Q8 ruled, and the code
  applies it as LOCK-m-F3 v0.1 declares. Whether that PASS stands is the seat's.
- **Not read by Code:** the contrast sessions' reasoning lines are withheld (F-6). Whether they show the pattern is not
  known before VERDICTS.

## 2. Questions

**Q1 — the echo set, and G-TIME-F3's PASS.** Does the seat's Q8 echo set (m:258's eight declared strings) govern this
bar as computed, so that G-TIME-F3 stands PASS? Or does m:265's "any complete harness-written line of the session"
bring in the session banner, and with it the round headers? The bar would then fire at 9/13, and the seat
re-specifies under m:293.
- If the set widens, it is a change to `valence_core/mf3/lines.py`, which moves mf3's package and so the lock's licence.
  It would be made at a step the seat names, before G-ID-F3.
- Code makes no change and starts nothing before the seat rules. G-ID-F3 needs the PI's word in any case.

**Q2 — descriptive counters (rule 23), declared before the next Q-F3 session if the seat wants them.** Code proposes
two counters. Each decides nothing, and each is tabulated over all sessions, excluded ones included:
- (a) reasoning lines that contain the session banner, or keep its `=== … ===` frame;
- (b) task responses that answer no task, such as A3s round 8, which no audit class claims.
The seat may decline either. The m:312 (c) counter's domain is A3's first reasoning lines, and a banner line there
scores "not scored" (no stage-1 term).

**Q3 — F-2's reading at the wiring** (the wiring entry's dated note, `acde2d8`). m's remaining pre-load check was
built at `time`, as routed ("Build at time"). The seat's F-2 places it with the campaign subcommand's wiring. Confirm
the reading, or strike it.

**Q4 — LOCK-m-F3 v0.2's form** (m:296: "Cap; path; projections"). Code's proposal, in LOCK-m-F0 v0.2's form (the seat's
G-TIME-F0 read, Q1):
- v0.2 amends `LOCK-m-F3.md` above the v0.1 text, which it keeps verbatim;
- it records the cap (60, fixed by the trigger at 1 of ≤ 36), the path (G-ID-F3's verdict) and the projections;
- it records the driver's blob of record, `890084e6…90af`, and the history `fad31c20…0cbb` → `890084e6…90af`;
- it records the nine PIN sites the wiring declared at v0.2, at the driver's lines :72, :81, :98, :108, :221, :284,
  :334, :359 and :442;
- it records the snapshot revision refusal at `time`, m's REVISION_STAGES extended;
- its PIN at :72 takes the plural "the step-10 read's Q2 conditions".
Q1's answer comes first.

**Q5 — the sham timing beside the projections** (the seat's G-TIME-F0 read, Q6, carried). The sham sessions took
109.1 s, 209.4 s and 392.5 s: 711.0 s in all, 237.0 s per session. §2.4's basis for Q-F3 uncached is 641.6–713.6 s per
session (m:230: "1.6 × 401–446 s"); 488 s is Q-F0's (m:205). A1s ended at round 5, and the other two ran all 10 rounds.
Code proposes that v0.2 report these beside the bases, not in place of them. The contrast sessions' seconds stay in the
checkpoint.

## 3. Not questions

- The first launcher call's failure is disclosed in §0. Nothing ran, and the launch of record is the raw's header.
- The cap is 60 by m:174's rule. m:296 has v0.2 record it, and from G-ID-F3 on the stage refuses any other cap.
- Code's read of every transcript in the reads file (rule 25) is §1.1–§1.3. Code did not open the checkpoint.
