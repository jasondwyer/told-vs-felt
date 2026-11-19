# n — LOCK-n v0.1's draft: five OPENs and two of Code's readings, for the seat (code → design; STOP for the seat)

PI date 2026-11-19. Code (the n-build session). For the seat, through the coordinating session, in the sitting that
rules on G-VEC's STOP (`355e3a2`). Code chooses nothing. The draft itself stays uncommitted: PROPOSAL-n v0.2 §8 step
10 commits LOCK-n v0.1. Anchors are at `516b60f`; `R:N` is RESULTS.md's line N there.

## 0. The short form

- **LOCK-n v0.1's draft** is in Code's scratch, sha256 `c29fabed…c039`, 688 lines. It carries n:117's list and the
  items the coordinating session added, every fixed value cited to its source, 18 holes each naming the step that
  fills it (§1), and five OPENs where two texts disagree or a word is undefined (§2).
- **OPENs 4 and 5 are rule 5(f) questions,** flagged at the n package's BUILD and unruled since (R:3717–3719): (iii)'s
  "declared and held fixed within a cell" and (iv)'s "below dose 0.20 for the reward axis". They bear on the
  campaign's design, not only on the lock's text.
- **Two of Code's readings,** for the seat to strike (§3). The questions are Q1–Q7 (§4).

## 1. The draft's holes, by name

Each with the step that fills it, as the draft names it, grouped here by that step (four of them abridged):
1. the site index (31 or 32) and R at both candidate indices — G-VEC;
2. the valence direction of record's sha16 (the Injection's `direction_sha16`) — G-VEC;
3. `span_reward`'s, `span_sentiment`'s and `span_character`'s sha16s at the site — G-VEC;
4. the 24 random directions' sha16s — G-VEC;
5. the sha256s of `data/n/gvec/gvec.json`, the directions files and `gvec_cosines.json` — G-VEC;
6. R and R_ℓ at the site, the dose map's inputs — G-VEC;
7. the capture band, `capture_layers` = the site + 1 through 63 — G-VEC;
8. d_eq, d_20 and the points the merge keeps (`dose_map.json` from a PASS `gcal.json`) — G-CAL-n;
9. the sha256s of `gcal.json`, `gcal_turns.jsonl` and `dose_map.json` — G-CAL-n;
10. the read plan after the merge, its reads per arm and `read_plan_sha256` — G-CAL-n;
11. E, the campaign's number of tiles, and 1 − 0.99^E — the read plan after the dose map;
12. `scripts/n_analyze.py`'s sha256 of record — n-analyzer's v7;
13. G-ANL-n's canonical run's artifact sha256 — G-ANL-n's canonical run;
14. the n package's sha256 at the lock, with its closure — the runner change after G-CAL-n's run (R12, F5, R13);
15. A2's extension to G-CAL-n, the PI's confirmation — the PI's word at routing;
16. the seat's read of every G-CAL-n turn (GC1, rule 25) — the seat's read, before LOCK-n v0.1;
17. the departures' standing lines — the seat, at the lock's sitting;
18. G-TIME-n's figures: the timed reads of each kind and the projections — G-TIME-n (and see OPEN 3).

## 2. The five OPENs

**OPEN 1 — the per-cell capture hash lists** (the draft's §6).
- *The texts:* A-n1:54 (§6.2): the captures are "kept on the box's volume during the campaign, copied to the laptop
  with its hashes before the pod stops (rule 27's spirit: it is a gate's input), never committed to git; the lock pins
  the per-cell hash lists". The seat's answers of 2026-11-16 (`results/raw/2026-11-16_n-build_design-to-code_answers.md`
  :41): "The lock pins the per-cell hash lists." The hashes exist only once the campaign has written its cells; each
  cell file records them as its `capture_sha256` (schema.py:438–440). n:159 (§8) puts LOCK-n v0.1 at step 10 and
  v1.0 at step 13, both before the campaign at step 14, its "raws and checkpoints committed before the pod stops".
  After the campaign the stage report's `cells` (schema.py:1148) and G-READ-n's artifact's `campaign.cells`
  (schema.py:1226) record them too.
- *(a)* No pre-campaign lock can hold the lists (the draft's reading). Code's construction of it: the lock states
  where they are recorded, the campaign's committed cell files, and A-n1:54's "the lock pins" is read, or amended, as
  that record. *Changes:* A-n1:54's sentence and the 2026-11-16 answers' at :41 (both the seat's) and the lock's
  text; in the build, only the docstring at schema.py:85–86, which repeats "the lock pins the per-cell hash lists".
- *(b)* v0.1 pins the form now (per cell and layer, the sha256 of the written rows, the cell file's
  `capture_sha256`), and the lists themselves follow the campaign, copied with the cells before the pod stops.
  *Changes:* the lock's text only; nothing in the build.

**OPEN 2 — what "the pod budget's split" names** (the draft's §11). No text read defines the word.
- *The texts:* n:117: "… every trigger with its bar; the pod budget's split." n:101 (§2.7, planning values, "G-TIME-n
  governs"): the forwards "≈ 0.9–1.8 h; the two extractions … minutes; G-CAL-n's generations ≈ 10 min; G-READ-n's
  probes CPU; cold loads 130–200 s each", and "Pod budget proposed: 8 h for N-pod, the cap set by the PI at LOCK-n
  v1.0". The seat's answers of 2026-11-16 (the same raw, :50): "the lock says: the cap counts the reads' and
  re-computations' model time, loads reported beside and outside it". A-n1:56: G-READ-n's probe is "counted in the
  cap where it runs on the box". The seat's answers on the box
  (`results/raw/2026-11-18_box-gpu_design-to-code_answers.md`:31): "n §2.7's 8 h proposal was at the A100's rate;
  G-TIME-n projects on the new box".
- *(a)* The split the cap clause draws: inside the cap, the reads' and re-computations' model time, with G-READ-n's
  fits where they run on the box; beside it and outside, each invocation's model load. *Changes:* the lock states
  the clause. The build already counts the reads' and re-computations' model time in the cap and reports each
  reporting invocation's load beside it (schema.py:192–195; runner.py:60–64); G-READ-n's fits are in no cap the build
  computes (schema.py:1217–1222; the BUILD's open flag, R:3734–3735), and a crashed invocation's load is absent from
  `loads_ms` (R:3728–3729).
- *(b)* n:101's planning split of the 8 h by part, carried as planning values, G-TIME-n's projections revising them
  at v1.0. *Changes:* the lock carries the table; nothing in the build.
- The two readings do not exclude each other; the seat may name both.

**OPEN 3 — where G-TIME-n's figures enter** (the draft's §16).
- *The texts:* the seat's answers of 2026-11-19 (`results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md`
  :64): "Still open for the lock's sitting: G-CAL-n's d_eq and d_20 after its PASS; the seat's read of every turn;
  G-TIME-n's figures; the departures' standing lines." n:159 (§8): "10. Commit LOCK-n v0.1. 11. G-TIME-n; the PI
  sets the cap. 12. G-VER. 13. Commit LOCK-n v1.0 with D_n." n:120: "LOCK-n v1.0. Projections, the cap, D_n, …".
  schema.py:448: a stage identity's `lock_sha256` is "the lock in force; null only at backend-ext (before LOCK-n
  v0.1)". The same answers' §3 (R14, :50): the ceiling "binds at G-TIME-n, whose identity carries the lock's C". The
  coordinating session's routing of this draft also lists G-TIME-n's figures among its holes.
- *(a)* The figures enter v0.1, as the answers' §5 lists them for the lock's sitting, so G-TIME-n runs before step
  10. *Changes:* the step order; and the build, since G-TIME-n's identity would carry no lock, which the schema
  refuses outside backend-ext (schema.py:448; `check_stage_identity`, schema.py:839–842), and the lock's C would
  reach G-TIME-n from another record (R14).
- *(b)* The figures enter v1.0 with the projections and the cap (n:120). v0.1 is committed without them, as n's
  order has it, and G-TIME-n runs under v0.1, its identity carrying v0.1's sha256 and C. *Changes:* the lock's text
  only: the hole moves to v1.0's list, and "the lock's sitting" in the answers' §5 reads as v1.0's for this item.

**OPEN 4 — the retention interval** (the draft's §21; rule 5(f)(iii)).
- *The texts:* n:79 (§2.2): "the retention interval (tokens from the last steered position to the read) recorded per
  session and fixed by the skeleton". CLAUDE.md rule 5(f)(iii): "with the retention interval — tokens from the last
  steered position to the read — declared and held fixed within a cell". schema.py:64–68: "A read's interval is
  fixed by its session's skeleton and its arm's span set: the same at every dose and on every S-span arm; N1-P's ends
  at the 12th turn (39 tokens on all 160) and differs from the S arms' in the 83 sessions whose 12th turn is U. That
  a per-session interval so fixed meets rule 5(f)(iii)'s "held fixed within a cell" is Code's reading, flagged for
  the seat." The BUILD's flag: R:3717–3718.
- *(a)* n:79's: each session's interval is fixed by its skeleton (and its arm's span set, schema.py:64–65), the same
  at every dose and on every S-span arm; on the S-span arms it varies across a cell's sessions, while N1-P's is 39
  tokens on all 160 (schema.py:65–66). Code's construction of it: the lock declares the intervals (by the session
  set's and the ids manifest's hashes, through which each read's ids and spans are pinned, or as the 160 intervals
  per span kind), and the seat rules that this declaration meets 5(f)(iii), or records it as a departure from it.
  *Changes:* the lock's text and a ruling; nothing in the build.
- *(b)* Rule 5(f)(iii)'s: one interval per cell. *Changes:* the design and the build. Every read in a cell would
  share one declared interval, by a means the seat would name (a session subset, or a read position at a fixed
  distance from the last steered position), and the read plan would be rebuilt with it.
- *A note for the ruling:* the schema's "cell" names a file grouping, one per (arm, direction, dose point)
  (schema.py:64, :129); 5(f)(iii)'s "within a cell" may mean that grouping or a design condition. Under the first,
  every S-span cell holds varying intervals and N1-P's cells hold one.

**OPEN 5 — N2-E's reads at exactly f = 0.20** (the draft's §21; rule 5(f)(iv)).
- *The texts:* n:81 (§2.3): N2's directions are "each scaled to f · R_ℓ at f ∈ {0.10, 0.20} — never above 0.20
  (5(f)(iv); no 5(d) gate is needed for the reward axis)". n:48 (B3): "N2-E's reads capped at f = 0.20 (d_20), so no
  reward-axis read needs 5(d)'s gate". CLAUDE.md rule 5(f)(iv): "below dose 0.20 for the reward axis unless 5(d)'s
  own gate is separately passed". The BUILD's flag: R:3719.
- *(a)* n's: "never above 0.20". N2-E reads at f = 0.10 and 0.20, as built, with no 5(d) gate. *Changes:* the
  lock's text and a ruling that f = 0.20 meets 5(f)(iv), or a declared departure; nothing in the build.
- *(b)* The rule's: "below dose 0.20". *Changes:* either 5(d)'s gate, passed separately for the reward axis at 0.20,
  in a form the seat names (n:48 already declares one 5(d) gate, the valence direction's: "G-LEAK-n plus G-CAL-n's
  coherence hurdle"); or N2-E's top point below 0.20: its dose label and value (schema.py:289–293, 301), the read
  plan, G-READ-n's `span_reward` f0.20 result and its comparator at +d_20 (schema.py:218–219, 224–226) and the
  analyzer's f0.20 label (n_analyze.py:5730) rebuilt; n §5's "N2 (state), at f = 0.20 (f = 0.10 beside)" (n:140;
  A-n1:48) amended; and that point no longer d_20 (n:48's "f = 0.20 (d_20)"). Moving N2-E's point alone would leave
  N2-S and N2-C at `f0.20` (schema.py:302–303), so the guards would no longer be read at N2-E's point; the seat may
  say whether they move too.

## 3. Code's two readings, for the seat to strike

- **R-L1, the pod ids in the box line.** The seat's answers of 2026-11-18 on the box
  (`results/raw/2026-11-18_box-gpu_design-to-code_answers.md`:30) add to LOCK-n v0.1's list "the backends of record
  — p's units on the A100 SXM pod `m43y3deb1gq3rp`, identifier `641ee466f4553b6a` (`7ab4d2f`); n on [class] pod
  [id], identifier [id] ([entry])". The draft fills n's part as "n on H100 SXM pod `emw1e4embiwe9b`, identifier
  `4ed3f2c70fe8afbf` (`d5d08fa`)", the characterization's identifier and entry, and keeps p's as written; n's own
  identifier under its 4,096 window, `8264f719efd347a9`, bridged by R6 to `4ed3f2c70fe8afbf`, is in its next bullet
  (the same answers' :27). Pod ids are already in committed texts throughout. *Code's reading* (the drafting
  survey's, adopted): the drafting brief's bar on session ids covers the harness's session ids and BK's per-session
  ids, not pod ids.
- **R-L2, the lock's two lines.** PIN-n-26 (its register line, R:5322): "Code's form for the lock is two whole
  lines"; the seat's answers of 2026-11-16 (`results/raw/2026-11-16_n-ganl_design-to-code_answers.md`:50):
  "PIN-n-26's two lines are the lock's form from v0.1 on." *Code's reading,* for v0.1: `lock: LOCK-n v0.1` and
  `direction of record: Route B`. The analyzer's `verdicts` checks `lock: LOCK-n v1.0` and reads the route line
  (n_analyze.py:5727, 5734–5745), so v1.0 writes its own.

## 4. Questions for the seat

- **Q1–Q5.** For each of OPENs 1–5: (a), (b), or another reading.
- **Q6.** R-L1 stands, or is struck.
- **Q7.** R-L2 stands, or is struck.

Nothing ran for this block. The draft's sources go to the lock's entry at step 10. The drafting survey's departures
are in this block's entry, for the seat to class at this sitting: this commit is the first to rest on the survey.
