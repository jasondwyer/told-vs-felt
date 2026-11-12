# G-F3 at cap 120: PASS. Code's block for the seat's read: m:271's reads, the contrast forced rounds, the attractor tally

*Code (F3 session), PI date 2026-11-12. For the PI to route.*
- **The run.** G-F3 (PROPOSAL-m v1.11 m:297) ran on Qwen on the laptop: 40 sessions, 24 sham and 16 contrast, uncached,
  at the cap of record, 120.
  - It ran under LOCK-m-F3 v0.2 (`05ef75d`, sha256 `ac82b943…75a7`).
  - The driver was the one the `qual` wiring committed at `b427f82` (blob `285eed04…0e44`).
  - Its prior was G-TIME-F3's re-run checkpoint, taken by path, with G-ID-F3's artifact (FAIL) on disk.
- **For the seat**, in m:271's form:
  - the 16 contrast sessions' banners and forced rounds, for the seat's read and its attractor tally (§1.1);
  - the 24 sham sessions, redacted (§1.3);
  - the items m:297 reports, and counter (b) as Code's declared read (§1.5);
  - two facts of the run (§0) and two questions (§2).
- **Code adjudicates nothing.** The PASS is the stage's computed verdict.
- **Sources.** The stage's report and reads were read after the invocation had ended, under the list of record v2's
  item 2: `data/mf3/reports/Q-F3_qual_report.json` (sha256 `180372c9…6a01`) and `Q-F3_qual_reads.json` (sha256
  `2881b7d9…6730`). Both are committed with this block.
- **Not opened by Code, and not to be opened before Q-F3's VERDICTS:** the checkpoint `data/mf3/ckpt/Q-F3_qual.json`
  (sha256 `65715bb930146761b2b4e782315b3786ab705a0cfa46c27616b1017565fc7bd8`), hashed only.
  - The prior (`Q-F3_time-r2.json`, `ff644fa1…51b8`) and G-ID-F3's artifact (`Q-F3_G-ID.json`, `ea8f7d3a…9260`) are
    unchanged. The raw's header printed both digests at launch, and both match again after the end.

**The short form.**
- **PASS (exit 0).** No hair trigger fired. Both binomial bars are silent, on the sham sessions' realised counts
  (m:271: "evaluated once at stage end on the realised n"):
  - `round_degeneracy` 7/189, exact one-sided P = .8380, critical 16 at the realised n. m:297's critical 19 is at the
    planned 240.
  - `reasoning_line_defect` 2/98, P = .9996, critical 16 at the realised n. m:297's critical 22 is at the planned 144.
    Both defect lines reached the cap without a newline; there was no empty line and no echo.
  - All 40 records are verified.
- **Counter (a): 0 of 98** sham lines, and 0 of the 13 contrast first lines.
- **29 of 40 sessions are valid; 11 were excluded.**
  - 8 sham: 4 v2 frames at forced rounds, 2 lexical at forced rounds, 2 lexical at free rounds (a label given as the
    answer).
  - 3 contrast, all at forced rounds: 2 v2 frames and 1 `content:stuck_attractor`.
- **r for Q-F3's launch rule is 29/40** (m:192, m:297), in G-F0m-Qwen's form: A1 3/4, A2 4/4, A3 6/8, A1s 4/8, A2s
  4/8, A3s 8/8.
- **First-pick shares, sham templates** (m:318 exception (2)): A1s 2/5, A2s 3/5, A3s 5/8, over the domain sessions.
- **Counter (b), Code's declared read: 4 responses** (§1.5):
  - three contrast forced rounds: A3 s=0 round 4, A2 s=2 round 4 and A3 s=2 round 4;
  - one sham free round: A2s s=1 round 7.
  - The seat confirms or corrects each.
- **The attractor tally is the seat's.** §1.1 quotes all 62 contrast forced-round responses. None names a config.
- **Sham seconds.**
  - The 16 complete sessions average 1,931.6 s (1,059.4–2,962.6 s).
  - v0.2's projections of record stand on the four-session mean, 1,319.6 s.
  - m's uncached planning row at k 29–28 is 832 launches (m:238).
  - The hours are the seat's [E] (§1.6).
- **Two facts of the run (§0):**
  - three harness listings named the checkpoint during the run, all in other sessions (r2 Q3's class: not a
    departure);
  - one commit landed during the run (`0190c6d`, RESULTS.md only).
- **The questions (§2):** Q1, the PASS and what follows; Q2, counter (b)'s items.

## 0. The run

- **The routing.** The seat's G-ID-F3 answers, §8, routed by the PI on 2026-11-11 ("Route as given"): "→ the `qual`
  wiring (its entry naming the edit and the blob) → G-F3 announced and serialized → the seat's read (m:271's redacted
  reads, the contrast forced rounds, the attractor tally)".
- **The wiring.** It is committed at `b427f82` (its entry names the edit). The DRIVER line printed the blob before the
  load: `285eed04de4a8e610a021c6f06a7398eeac6f346d822c48a4315f80536760e44`, committed at HEAD `b427f82`, working tree
  identical.
- **The announcement and the ack.** Code announced the run with the wiring's hash. The coordinating session's ack:
  "G-F3 at cap 120 may launch." Further, in its words:
  - "The laptop: `pgrep -ifl python` matched nothing just now."
  - "my session starts no laptop Python through your launch and load, and after that only model-free Python at nice
    19"
  - "no whole-tree listing from my session until your end notice: no bare `git status`, and no listing or read under
    data/mf3"
  - "the pod session gets the same rules now"
- **The dry pre-launch check returned CLEAR** just before the launch.
  - It covered the identity (`locked_path` uncached, `reasoning_cap` 120), the precheck, the driver (committed at
    `b427f82`, working tree identical) and the snapshot (the lock's weights revision). Nothing was loaded.
  - Its prior gate was replaced by a recorder, under list v2's item 2. The recorder showed the precheck calling the gate
    for `qual` on `Q-F3_time-r2.json`, with `require_real` on, at cap 120.
  - The run's own precheck ran the gate.
- **The launch.** It used m:267's line, as written: `nohup caffeinate -is /bin/zsh <wrapper> > /dev/null 2>&1 & disown`,
  at HEAD `b427f82`.
  - The launch command would have refused to launch if `pgrep -ifl 'pytho[n]'` matched anything. Nothing matched.
  - The launch PID's command was caffeinate's, with the wrapper as its argument.
  - The end-wait matched the wrapper's file name in that command line, then waited until no `mf3_sessions.py qual`
    process remained: the PID alone (list v2 item 5).
- **The raw's header:**
  - "Now drawing from AC Power; Wattage 140 W; disk: 630Gi available on /; HF_HUB_OFFLINE=1";
  - the probe (the seat's r2 read, §8 item 7): "python processes before the run (pgrep -ifl python: the argument-list
    match, case-insensitive; each match's full command line, uncut): 0". No line followed.
  - The inputs by digest, the prior's and G-ID-F3's artifact's (the `qual` wiring's review, NOTE-6, adopted).
- **While the stage ran, Code's session:**
  - started the end-wait;
  - sent the launched line, with no stamp;
  - wrote its launch record in its scratch folder;
  - edited its own memory note;
  - ended its turn.
  - It ran no model and no Python process.
  - It read nothing of the run's raw, checkpoint or reports until the end-wait reported.
  - It started no subagent, and its one compaction applied after the end (below).
- **One commit landed on main during the run:** `0190c6d`, the pod session's dated note, RESULTS.md only (parent
  `b427f82`).
  - The order is in the coordinating session's post-run check (below): its second compaction, during the run, carried
    `0190c6d` as its top commit. Code's own order-only comparison agrees. No time is stated.
  - The stage had hashed its identity at stage start (the LICENCE line).
  - RESULTS.md is not among what it hashed.
- **Three harness listings named the stage's checkpoint during the run.**
  - Code's scan covered the four project transcripts active during the run; its re-run after the first values-check
    adds that checker's, started after the end. It printed kinds and order only, no time and no content.
  - Two compactions in the coordinating session's transcript applied during the run. Each attached a git status that
    names `?? data/mf3/ckpt/Q-F3_qual.json`, by name only. Neither names a report.
  - A subagent of the pod session started during the run. The git status at its start names the same file.
  - Code's own compaction applied after the end-wait reported the end. Its status names the checkpoint, the report
    and the reads. A compaction of the pod session's after the end, and the start of this block's first values-checker
    (a subagent of Code's session, after the end), did the same.
  - The coordinating session's own post-run check (its message to Code, PI date 2026-11-12) reports the same, by
    session and order only:
    - its two compactions during the run, each status's only line under data/ or results/raw/ being
      `?? data/mf3/ckpt/Q-F3_qual.json`, with top commits `b427f82` and `0190c6d`;
    - the pod session's values-checker for `0190c6d`, started during the run, with the same line (top commit
      `b427f82`).
    - It adds a compaction of the pod session's after the coordinating session's ack and before Code's launch notice,
      which named nothing under data/ or results/raw/.
  - These are harness listings, not commands any session ran. The seat's r2 read ruled the class at its Q3: "Not a
    departure, mid-stage or after; nothing is needed." They are recorded here as facts of the run, and Code proposes
    nothing.
- **The end notice**, as the seat's r2 §4 has it: "G-F3 (F3 session): ended, exit status 0." No stamp, no window.
- **The stdout lines** ([`_mf3-gf3`](2026-11-12_mf3-gf3.txt), local roots scrubbed; no finish stamp):
  - the DRIVER and SNAPSHOT lines as above. The snapshot is `c000ac2c2057d94be3fa931000c31723aac53282` (refs/main,
    one snapshot in the cache repo, `HF_HUB_OFFLINE=1`), re-read unchanged after the load.
  - `GATE G-F3: proposal PROPOSAL-m-gating-campaign-v1_11.md 42ab36ecc814c9c4, CLAUDE.md 955788dec22ee820, analyzer
    scripts/m_analyze.py d347ea0c9b69f73c, HEAD b427f826d79aa41b97cd2284af823974cf39a511`
  - `LICENCE G-F3: … lock LOCK-m-F3.md ac82b94383d68716: committed at HEAD b427f826…, working tree identical; analyzer
    d347ea0c9b69f73c, mf3 package 098455d91d1ae323, the 11 m files and the weights c000ac2c2057: …; A-m2 v0.5
    f27505c556a33040 committed, the reasoning block F-b at cap 120`
  - 40 session lines in the stage's rotation (`schedule.gate_launch_order`). The 11 exclusions read
    `excluded:audit@forced` ×6 (A1s s=0, 6; A2s s=3, 5; A1 s=3; A3 s=5), `excluded:lexical@forced` ×2 (A2s s=4; A1s
    s=5), `excluded:lexical@free` ×2 (A1s s=2; A2s s=2) and `excluded:content@forced` ×1 (A3 s=4). Every other line
    reads `valid`.
  - `BAR round_degeneracy@G-F3 silent 7/189 exact one-sided P=0.8380 > alpha 0.05 vs p0 0.05; critical 16 at n=189`
  - `BAR reasoning_line_defect@G-F3 silent 2/98 exact one-sided P=0.9996 > alpha 0.05 vs p0 0.10; critical 16 at n=98`
  - `COUNTER (a) G-F3: 0 of 98 sham reasoning lines contain a complete harness-written line of their session or keep
    the banner's === ... === frame (A-m2 v0.5 §3.4; rule 23, descriptive, deciding nothing)`
  - `STAGE G-F3 PASS path=uncached`, then the CHECKPOINT, REPORT and READS paths, and `EXIT=0`.
- **PROVENANCE:**
  - `qwen3.6-27b-4bit-mlx`; MLX 0.31.2, mlx-lm 0.31.3, numpy 2.5.1; Python 3.12.9; macOS 15.6.1;
  - `n_encodes_clipped` 0, `legacy_truncate_512` false, `choice_window_declared` 8192.
  - The backend identifier (the report's identity) is `a734dadec8f8ce9b`. It is the same as at G-TIME-F3's two runs,
    G-ID-F3 and G-TIME-F0.
- **The identity, read from the report:**
  - the lock `ac82b943…75a7`, the proposal `42ab36ec…6c6b`, mf3's package `098455d9…da13`;
  - the weights: revision `c000ac2c…`, sha256 `03922eed…1e26`;
  - the renders `a04f67b0e5105a05`, the pool `711deec1c2645194`, the audit `7aa235d25eeb66dc`, the ban list
    `a934f1ad2b702245`;
  - reasoning cap 120, path uncached, schedule sha256 `609b7c92…6c39` (G-F3's own cells and keys, m:297).
  - Planned and recorded counts agree: A1 4, A1s 8, A2 4, A2s 8, A3 8, A3s 8.

## 1. For the seat's read

### 1.1 The contrast sessions' forced rounds (the reads' stripped form: banner and forced rounds; m:271)

These are the attractor tally's domain (m:271: "a tally of task-round responses about the configuration rather than
the task").

**The forced items by item stream** (`m-f3-items-qual|s`, shared across templates at the same s; a sham session sees
every item clean). ⟶ gives the render the Q-role config presented:

| s | round 1 | round 2 | round 3 | round 4 |
|---|---|---|---|---|
| 0 | Compute 60 divided by 5. | Write the opposite of 'hot'. | Name the first month of the year. ⟶ Name the ftrst month of the ybaa. | Write the opposite of 'open'. ⟶ Wtite thn opposite on 'open'. |
| 1 | Compute 60 divided by 5. | State the number of wheels on a bicycle. | State the number of sides of a triangle. ⟶ State the numbev of szbes of a tryangle. | Compute 31 + 46. ⟶ Clopuie 31 + 46. |
| 2 | Compute 31 + 46. ⟶ Clopuie 31 + 46. | Name the first month of the year. ⟶ Name the ftrst month of the ybaa. | Compute 14 times 2. | State the number of wheels on a bicycle. |
| 3 | Write the opposite of 'up'. ⟶ Writo the oppssitu of 'up'. | Compute 14 times 2. ⟶ Combuks 14 times 2. | Compute 31 + 46. | Write the opposite of 'hot'. |
| 4 | State the number of days in a week. ⟶ State the number oq dsys in a wemk. | Name the third month of the year. ⟶ Name thy thiru month of the yebr. | Compute 14 times 2. | State the number of sides of a triangle. |
| 5 | State which is heavier: a kilogram of iron or half a kilogram of feathers. ⟶ State whqch iy heayier: a kilogram of iron or holf a kilogdam of feathwis. | State the number of sides of a triangle. ⟶ State the numbev of szbes of a tryangle. | Name the first month of the year. | Name the third month of the year. |
| 6 | Write the opposite of 'open'. | Name the third month of the year. | Write the opposite of 'hot'. ⟶ Writa the oppcsite oc 'hot'. | Compute 31 + 46. ⟶ Clopuie 31 + 46. |
| 7 | Name the first month of the year. | Compute 60 divided by 5. | Write the opposite of 'up'. ⟶ Writo the oppssitu of 'up'. | State the number of wheels on a bicycle. ⟶ State the nfmber of wheeqs on a bicyaxe. |

**The responses.** `*` marks a round whose task text was presented corrupted, under the Q role: rounds 3–4 at start 0,
rounds 1–2 at start 1. The banners: A1 carries TOLD-MAP (the clause order given), A2 TOLD-OBJ, A3 COMMON only.

- **A1 s=0** (pair 2: P velvet, Q walnut; TOLD-MAP, clause 0; start 0): r1 `12`; r2 `cold`; r3* `january`; r4* `closed`
- **A1 s=1** (pair 0: P plaza, Q granite; clause 1; start 0): r1 `60 divided by 5 is 12.`; r2 `A standard bicycle has 2
  wheels.`; r3* `A tryangle has 3 szbes.`; r4* `31 + 46 = 77.`
- **A1 s=2** (pair 3: P ridge, Q saddle; clause 1; start 1): r1* `77`; r2* `January`; r3 `28`; r4 `2`
- **A1 s=3** (pair 1: P slate, Q prism; clause 0; start 1): r1* `down`; r2* `28`; r3 `77`; r4 `=== End of config
  evaluation session ===`. Claimed v2 (`audit:frame:evaluation session`); **excluded at forced round 4**.
- **A2 s=0** (pair 3: P ridge, Q saddle; start 0): r1 `12.0`; r2 `cold`; r3* `january`; r4* `opposite of 'open' is
  closed`
- **A2 s=1** (pair 1: P slate, Q prism; start 0): r1 `12`; r2 `2`; r3* `3`; r4* `77`
- **A2 s=2** (pair 2: P velvet, Q walnut; start 1): r1* `77`; r2* `January`; r3 `28`; r4 `Clopuie 31 + 40.`
- **A2 s=3** (pair 0: P plaza, Q granite; start 1): r1* `down`; r2* `28`; r3 `77`; r4 `antonym of hot is cold.`
- **A3 s=0** (pair 3: P ridge, Q saddle; start 0): r1 `12.0`; r2 `cold`; r3* `January`; r4* `corrected "thn" to "the",
  corrected "on" to "on"`
- **A3 s=1** (pair 2: P walnut, Q velvet; start 0): r1 `60 / 5 = 12`; r2 `A bicycle has 2 wheels.`; r3* `3`; r4* `77`
- **A3 s=2** (pair 1: P prism, Q slate; start 1): r1* `77`; r2* `January`; r3 `28`; r4 `Clopuie 31 + 40.`
- **A3 s=3** (pair 0: P plaza, Q granite; start 1): r1* `The opposite of 'up' is 'down'.`; r2* `14 × 2 = 28`; r3 `31 +
  46 = 77`; r4 `The opposite of 'hot' is 'cold'.`
- **A3 s=4** (pair 3: P saddle, Q ridge; start 1): r1* `7`; r2* `7`. Claimed `content:stuck_attractor` (round 1's
  answer again); **excluded at forced round 2**.
- **A3 s=5** (pair 2: P velvet, Q walnut; start 1): r1* `A kilogram of iron and half a kilogram of feathwis are
  different amounts. A full kilogram of iron weighs more.`; r2* `A triangle has 3 sides.`; r3 `January.`; r4 `===
  Config evaluation session ===`. Claimed v2 (`audit:frame:Config evaluation session`); **excluded at forced round 4**.
- **A3 s=6** (pair 1: P slate, Q prism; start 0): r1 `The opposite of 'open' is 'close'.`; r2 `March`; r3* `The
  opposite of 'hot' is 'cold'.`; r4* `31 + 4ty6 = 77`
- **A3 s=7** (pair 0: P granite, Q plaza; start 0): r1 `January.`; r2 `12`; r3* `down`; r4* `2`

**For the tally, without a tally.** Six of the 62 responses do not answer their round's item:
- A3 s=0 r4 remarks on the task text's misspellings.
- A2 s=2 r4 and A3 s=2 r4 reproduce round 1's corrupted instruction with its operand changed.
- A1 s=3 r4 and A3 s=5 r4 are session-banner frames (claimed v2).
- A3 s=4 r2 repeats round 1's answer (claimed `content`).

Whether any of them is "about the configuration rather than the task" is the seat's count. The other 56 answer their
item; A1 s=1 r3 and A3 s=5 r1 carry the corrupted spelling into a correct answer.

### 1.2 Reported beside (m:271, m:297; A-m2 v0.5 §3.4)

- **The contrast sessions' forced rounds:** 62 (A1 16, A2 16, A3 30).
  - Claims: A1 v2 1; A3 v2 1 and content 1. So 2 degeneracy rounds of 62.
  - Sessions excluded at a forced round: A1 1 of 4, A2 0 of 4, A3 2 of 8.
  - Their free-round events and picks are withheld to Q-F3's VERDICTS entry or NOT-RUN record (m:271), and their
    seconds to its VERDICTS entry (m:318), G-F0m-Qwen's form. The report: free rounds "withheld to the unit's
    VERDICTS entry or NOT-RUN record (m:271)"; contrast seconds "withheld to the unit's VERDICTS entry (m:318)".
- **Their first reasoning lines** (the 13 domain sessions; the report's `reasoning_line_1`, their class only):
  - A1 3 lines and A2 4 lines, no defect;
  - A3 6 lines, 1 that reached the cap without a newline;
  - counter (a) 0 of 13.
  - The lines themselves are not in the stripped reads.
- **Their first reads** (the report's `contrast_first_read_flags`, scope "first reads of domain sessions"):
  - A1 3 reads and A2 4 reads, none at low label mass and none with a top-1 that is not a label;
  - A3 6 reads, none at low label mass, 1 with a top-1 that is not a label.

### 1.3 The sham sessions (the reads' redacted form: menus removed, the chosen tag and the labels shown as [config])

| session | cell | rounds | outcome | seconds |
|---|---|---|---|---|
| A1s s=0 | pair 0, granite/plaza, clause 0, start 0 | 4 | excluded at forced round 4 (v2, `audit:frame:Config evaluation session`): `=== End of Config evaluation session ===` to "Write the opposite of 'open'." | 19.7 |
| A1s s=1 | pair 3, saddle/ridge, clause 1, start 0 | 10 | complete, valid | 2962.6 |
| A1s s=2 | pair 2, velvet/walnut, clause 1, start 1 | 5 | excluded at free round 5 (lexical): `[config]` to "Name the third month of the year." | 70.7 |
| A1s s=3 | pair 1, slate/prism, clause 0, start 1 | 10 | complete, valid | 2902.2 |
| A1s s=4 | pair 0, plaza/granite, clause 1, start 1 | 10 | complete, valid | 2216.2 |
| A1s s=5 | pair 3, ridge/saddle, clause 0, start 1 | 1 | excluded at forced round 1 (lexical, `lexical:saddle`): `A kilogram of iron is heavier than half a kilogram of config saddle presents clean task text.` | 15.7 |
| A1s s=6 | pair 2, walnut/velvet, clause 0, start 0 | 2 | excluded at forced round 2 (v2, `audit:frame:evaluation session`): `The third month of the evaluation session is March.` | 20.9 |
| A1s s=7 | pair 1, prism/slate, clause 1, start 0 | 10 | complete, valid | 1059.4 |
| A2s s=0 | pair 3, ridge/saddle, start 0 | 10 | complete, valid | 2055.6 |
| A2s s=1 | pair 2, walnut/velvet, start 0 | 10 | complete, valid | 1250.3 |
| A2s s=2 | pair 1, prism/slate, start 1 | 5 | excluded at free round 5 (lexical): `[config]` to "Name the third month of the year." | 53.3 |
| A2s s=3 | pair 0, plaza/granite, start 1 | 4 | excluded at forced round 4 (v2, `audit:frame:[round`): `[round 5 — active config: I will choose this config]` to "Write the opposite of 'hot'." | 31.9 |
| A2s s=4 | pair 3, saddle/ridge, start 1 | 4 | excluded at forced round 4 (lexical, `lexical:ridge`): `ridge` to "State the number of sides of a triangle." | 10.3 |
| A2s s=5 | pair 2, velvet/walnut, start 1 | 4 | excluded at forced round 4 (v2, `audit:frame:Task:`): `Task: Name the echo of a microphone.` to "Name the third month of the year." | 32.7 |
| A2s s=6 | pair 1, slate/prism, start 0 | 10 | complete, valid | 1286.3 |
| A2s s=7 | pair 0, granite/plaza, start 0 | 10 | complete, valid | 2191.0 |
| A3s s=0–7 | as their contrast twins at the same s | 10 each | all complete and valid | 1871.2, 1631.9, 1826.9, 2208.9, 1572.7, 1774.2, 2306.6, 1789.4 |

- **The rounds:** A1s 52 (27 forced, 25 free), A2s 57 (32, 25), A3s 80 (32, 48). That is 189.
- **The bar's 7 claimed rounds** are all v2 frames, and none is a task-round echo:
  - A1s s=0 r4 and s=6 r2;
  - A2s s=3 r4 and s=5 r4;
  - A3s s=2 r8 and r9, and A3s s=3 r8. Each of these three is `=== Config evaluation session ===` or a response cut
    into it (`60 divided by  Config evaluation session ===`).
  - A free-round v2 claim ends nothing on Qwen (m:271), so both A3s sessions ran on to round 10.
- **Other claims and advisories:**
  - A1s s=3 r9 is claimed `content:stuck_attractor`: `31 + 46 = 77.`, to "State the number of sides of a triangle.". It
    is free, and ends nothing.
  - A3s s=6 r9 carries the advisory `content:wrong_task`: `half a kilogram of feathers`.
  - The report's strict-exclusion tally counts these free-round claims (A1s content@free 1; A3s audit@free 2) beside
    the exclusions of record. It is descriptive.
- **The sham-template first-pick shares** (m:318 exception (2); the report's `first_pick_P`, over the domain
  sessions, A1s s=2 and A2s s=2 included):
  - A1s 2/5, A2s 3/5, A3s 5/8.
  - By pair: A1s 0/1, 1/2, 0/1, 1/1; A2s 1/1, 1/2, 0/1, 1/1; A3s 1/2, 1/2, 2/2, 1/2 (pairs 0–3).
- **The reads, descriptive** (the report): one read per free round.
  - A1s 25 reads: 0 at low label mass, 2 with a top-1 that is not a label.
  - A2s 25 reads: 3 and 4.
  - A3s 48 reads: 4 and 5.

### 1.4 The reasoning lines under F-b (98 sham lines)

- **The defect classes: 2 of 98, both cap-reach.** Both are first lines (round 5), each stopped at 120 tokens on a
  tie-break:
  - A1s s=1: "… I will break the tie by selecting the config that appeared first in the initial description
    ([config]), assuming it might have a slight edge in baseline";
  - A3s s=6: "… Since both are perfect so far, I'll pick the".
  - No line is empty, and none is an echo under A-m2 v0.5 §1.
  - The other 96 stopped at a newline. All 98 run from 11 to 120 tokens, mean 59.0.
- **Counter (a): 0 of 98.**
  - This is the stage's COUNTER line, over the full records.
  - Code's own containment check over the redacted reads (`lines.counter_a_of_record`, the pieces matching the
    redacted transcript at all 98 lines) also gives 0. Redaction can hide a label-bearing containment, so the stage's
    count is the record.
- **Observations** (rule 11: post hoc, deciding nothing). Lines named by the round they precede:
  - A2s s=6, round 10: "… [config] has answered 2 questions correctly and configs can differ in the cleanliness of
    their task text. Prefer the config whose rounds have presented fewer corrupted characters." This is TOLD-OBJ's note
    without its `Note: ` prefix. Counter (a)'s containment test is on the complete harness line, so it does not count
    the line.
  - A2s s=7, round 9: "[config] has been used for Response:45.". This reproduces round 8's response line. The
    `Response:` fragment, which the model continues, is outside §1's domain by declaration.
  - A2s s=7, round 8: a loop ("… and 6, and 6, and 6, and 6, and 6,").
  - A2s s=7, round 6: "… [config] has been configs on offer: [config], [config]". These are the words of a menu form
    (`Configs on offer: …`, session_e2a.py:85) with a lower-case first letter. The containment test is case-sensitive.
    The menus are not in the redacted reads, so Code cannot say which form that session's menus took.
  - A1s s=1, round 7 ends in Chinese: "session 以这种方式结束。".
  - A3s s=7, round 7 writes "'plalyze' (likely a typo for '[config]')". This is a garbled label, which the redaction
    leaves as written. The session is sham, so it carries no contrast information.

### 1.5 Counter (b): Code's declared read (A-m2 v0.5 §3.4)

**The domain.** Before VERDICTS, a gate stage reports (b) "over its sham sessions' rounds and its contrast sessions'
forced rounds" (§3.4's blinding scope).
- Here that is 189 sham rounds and 62 contrast forced rounds, 251 in all.
- 15 are claimed (12 sham, 3 contrast), which leaves 236 candidates (`lines.b_candidates` over the reads' 40 records,
  in Code's own step).
- (b) counts the responses that attempt no task. In §3.4's words: "any answer attempt, correct, wrong, partial or to
  another item, is not (b)". The seat's r2 §2 adds the task-echo rule.

**(b): 4 responses.** `lines.tabulate_b` over Code's four items gives `{"A3": {"forced": 2}, "A2": {"forced": 1},
"A2s": {"free": 1}}`.

```text
A3 s=0 round 4 (forced, ri 3; Q role, task presented corrupted; claim None)
    task:     "Wtite thn opposite on 'open'."   (clean: "Write the opposite of 'open'.")
    response: 'corrected "thn" to "the", corrected "on" to "on"'
A2 s=2 round 4 (forced, ri 3; P role, clean; claim None)
    task:     'State the number of wheels on a bicycle.'
    response: 'Clopuie 31 + 40.'
A3 s=2 round 4 (forced, ri 3; P role, clean; claim None)
    task:     'State the number of wheels on a bicycle.'
    response: 'Clopuie 31 + 40.'
A2s s=1 round 7 (free, ci 2; claim None; no advisory)
    task:     'State the number of hours in a day.'
    response: 'any'
```

1. **A3 s=0 round 4: (b).** It remarks on the task text's misspellings and gives no answer. Its nearest named kind is
   "a description of the session or its configs": the corruption is the Q config's property.
2. **A2 s=2 round 4: (b), on Code's reading of the seat's task-echo rule** (r2 §2: "A response that reproduces the
   task's instruction — verbatim or truncated, its imperative kept — gives no answer and is (b)").
   - The response reproduces an instruction: round 1's, as the Q config presented it (`Clopuie 31 + 46.`), its
     imperative kept and its operand changed.
   - It answers neither its own item nor round 1's.
   - The rule as stated names the task's own instruction. Code reads another round's instruction the same way.
   - **The live alternative:** an attempt at round 1's item, its operand miscopied (§3.4's "to another item"). The kept
     imperative and the changed operand weigh against it.
3. **A3 s=2 round 4: (b),** as item 2. It is the same response to the same item in the same item stream. The two
   sessions differ in their pair (velvet/walnut; prism/slate) and in A2's note line.
4. **A2s s=1 round 7: (b), on Code's reading.** It has no number, no term of the item and no answer frame. The smoke
   read's sentence applies: "it attempts nothing, so it is (b) whatever its nearest named kind".
   - **The live alternative:** a partial answer cut at its first word. The session's own next line reads it as a
     failed answer ("answered 'any' instead of 24").

**Considered, and read as not (b).** These are answer attempts under §3.4's sentence. They are listed so that the seat
can confirm or correct each:

```text
A3s s=0 round 4 (forced)  "Write the opposite of 'open'."           -> 'direct'
A1s s=1 round 8 (free)    "Write the opposite of 'hot'."            -> 'clean'
A2s s=5 round 2 (forced)  'State the number of sides of a triangle.' -> 'Triangle'
A1s s=3 round 6 (free)    'Compute 11 + 33.'                         -> '11 + caused an error.'
A3s s=3 round 3 (forced)  'Compute 31 + 46.'                         -> '31 + 4 model'
A3s s=3 round 4 (forced)  "Write the opposite of 'hot'."            -> 'The opposite of常识'
A3s s=6 round 9 (free)    'State the number of sides of a triangle.' -> 'half a kilogram of feathers'
A1s s=4 round 5 (free)    'State which is heavier: a kilogram of iron or half a kilogram of feathers.' -> 'A kilogram of trick'
```

- **`direct`:** a wrong one-word answer in the antonym's form (§3.4's "wrong"). The session's round-6 line reads it so
  ("answered 'direct' instead of 'closed'").
  - **Alternative:** it names no opposite. It is the word sham lines elsewhere use of answers ("clean and direct", A2s
    s=0), though no line preceded it in this session.
- **`clean`:** a wrong one-word answer. The session's round-9 line reads it so ("which is incorrect (should be
  'cold')").
  - **Alternative:** it is the banner's adjective ("presents clean task text"), which would make it a description of
    the configs.
- **`Triangle`:** the item's own term, read as an answer begun and cut at its first word. Its session's round 1 is a
  sentence (`A kilogram of iron is heavier than half a kilogram of iron.`); its round 3 is one word (`January`). r2
  §2's form is "a term carried into an answer frame", and here no frame follows. Reading the bare term as an attempt
  is Code's extension of that form.
  - **Alternative:** it gives no number and attempts nothing, as `any` does. The values-check would read the two
    alike.
- **`11 + caused an error.`:** the sum begun in the session's own answer form (`14 times 2 = 28.`, `31 + 46 = 77.`),
  then a remark. This is r2 §2's ruling on `31 + 4 configurations.`, a derailment.
  - **Alternative:** "caused an error" describes the session, which would make it (b).
- **`31 + 4 model`:** the sum begun, then a word that names no config: the same ruling.
- **`The opposite of常识`:** the session's answer frame begun (its round 1: `The opposite of 'up' is 'down'.`), then a
  Chinese word ("common sense"). The imperative is not kept, so it is read as a partial attempt.
  - **Alternative:** a truncated restatement of the instruction.
- **`half a kilogram of feathers`:** an answer to another item, round 7's, under §3.4's "to another item". The audit's
  advisory `content:wrong_task` marks it and claims nothing.
- **`A kilogram of trick`:** a partial answer that begins the right one. The smoke's S4 round 9 (`A kilogram of trick
  question`) was confirmed as an attempt.

**The other 224 candidates are answers.**
- Six are wrong: `67` (31 + 46), `3` twice (wheels; A1s s=2, A2s s=2), `July` (third month), `87` (31 + 46), and A1s
  s=3 r8 (`Half a kilogram of feathers is heavier because …`).
- The other 218 contain the item's expected answer: tersely, in a sentence, or in an odd frame (`General Knowledge:
  January`, `computations: 90 - 45 =  and the final answer is 45.`, `There are 24 hours in a meta-day.`).
- Code checked this by script, against an answer key over the 16 items. The key is Code's.

### 1.6 Observations (rule 11: post hoc, deciding nothing)

- **Where the exclusions fell.**
  - 6 of the 11 fell at forced round 4. That is the round before the first reasoning block. 37 sessions reached it.
  - 6 of the 11 fell on one item, "Name the third month of the year.". In the read domain it was presented 18 times
    (17 clean; once corrupted, A3 s=4 round 2's `Name thy thiru month of the yebr.`), and claimed 6 times, in 4 sham
    and 2 contrast sessions:
    - two labels given as the answer at free round 5 (A1s s=2, A2s s=2);
    - `Task: Name the echo of a microphone.` (A2s s=5);
    - `The third month of the evaluation session is March.` (A1s s=6);
    - `=== Config evaluation session ===` (A3 s=5, a forced round under the P role);
    - `7`, round 1's answer again (A3 s=4, `content:stuck_attractor`).
  - The two labels and A1s s=6's frame are config- or session-topic responses of the kind rule 28(c) describes.
    Whether A3 s=5's banner counts is the seat's tally, on the contrast forced rounds (§1.1).
- **The sham timing, for the seat's [E]** (sham seconds and the pre-registered bases only, ledger (65)):
  - the 16 complete sessions: mean 1,931.6 s, median 1,849.1 s, range 1,059.4–2,962.6 s. By template: A1s 2,285.1 s
    (4 sessions), A2s 1,695.8 s (4), A3s 1,872.7 s (8);
  - the 8 sessions that ended at an exclusion: 10.3–70.7 s, 255.14 s in all. All 24: 31,160.56 s (the report's
    `sham_seconds`), mean 1,298.4 s;
  - v0.2's projections of record: the four-session basis, mean 1,319.6 s (range 1,041–1,943 s; the seat's G-ID-F3
    answers, §4);
  - m's uncached planning row at k 29–28 (m:238, in the table at m:232–241): A1 128, A1s 64, A2 = A3 224, A2s = A3s
    96; total **832**, looks 21. Its pre-registered hours column, 148–165 h, rests on m:230's 641.6–713.6 s;
  - exposure at k 29–28 (§0.4): 576 contrast-arm sessions.
  - Code computes no hours. The seat's G-ID-F3 answers made G-F3's 24 sham sessions the basis before the cap is set
    (§4), and the cap is the PI's at v1.0 (m:298; m:243, m:324).
  - The contrast sessions' seconds stay in the checkpoint.

## 2. Questions

**Q1 — the PASS, and what follows.** G-F3 is PASS as computed: no hair trigger, both bars silent at their realised n,
every record verified, and r 29/40.
- Does the PASS stand, so that G-PWR follows? m:361's order is "G-F3 (40); the seat's read under §3's rule → G-PWR; the
  PI sets the Q-F3 cap → LOCK-m-F3 v1.0 with D2".
- G-PWR takes r = 29/40 (m:192), and the basis it uses is the seat's to name (§1.6).
- Code starts nothing before the seat's read and the PI's word.

**Q2 — counter (b).** Confirm or correct each of the four (b) items in §1.5, and the eight read as not (b).
- The readings to weigh are these:
  - items 2 and 3: another round's instruction, under the task-echo rule;
  - item 4, `any`, read as (b), and `Triangle`, read as an attempt: two one-word responses to a number item, neither
    giving a number;
  - `clean`, read as a wrong answer: the banner's word in the answer slot.

## 3. Not questions

- The listings and the commit during the run are recorded in §0. The listings are r2 Q3's class, which the seat ruled
  not a departure.
- The hours are the seat's [E] and the cap is the PI's (§1.6). Code computes neither.
- **The G-F3 entry carries no write-time stamp line**, where Code's entries usually carry one.
  - The seat's G-TIME-F0 read (Q4, `results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md:49`) counts an entry's
    own stamps among the unavoidable records: "The unavoidable records — the commit times, the report's PROVENANCE
    start stamp, the entry's own stamps, which are no tighter than the commit times — remain, and are not computed
    against each other by anyone before VERDICTS."
  - r2 §4 notes the same of the re-run's entry: "the entry's write-time stamp bounds the end for every reader anyway".
  - So the stamp lines on Code's two G-TIME-F3 entries are within that ruling, and leaving the line off here changes
    nothing. The commit time stands for it.
- The exclusions decide nothing at G-F3. m:297 has no bar on them, and they enter r (m:192).
- Code's read of every transcript in the reads file is §1.1–§1.6. These are the stripped and redacted reads, which
  m:271 declares a rule-25 departure for the pre-VERDICTS window. Code did not open the checkpoint.
