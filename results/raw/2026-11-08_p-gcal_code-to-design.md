# PROPOSAL-p: G-CAL-p passed on all three checkpoints; the seat's read, and four items (Code → design seat, through the PI)

*Code's block, PI date 2026-11-08. G-CAL-p of record ran on the coordinating session's go, under the PI's routing of 2026-11-07 ("the coordinating session gives the box go, G-CAL-p runs [go]").*

- **The outputs** are committed at `b6ef939`.
- **The RESULTS entry, Code's read of all 384 generations and the values-check** are committed at `ec0d9d3`.
- **p §8 step 6** (`p_analyze`, G-ANL-p, then each LOCK-p v0.1) waits for this read and the PI's word.

## The result

| checkpoint | clean | corrupted | bar | covariate | clean-pool identity |
|---|---|---|---|---|---|
| sft | 62/64 | 47/64 | 47 | +15/64 | 64/64 |
| dpo | 61/64 | 52/64 | 46 | +9/64 | 64/64 |
| instruct | 59/64 | 51/64 | 45 | +1/8 | 64/64 |

- **Condition (4) PASSES on all three checkpoints.** sft passes with no margin.
- **Clean-pool identity.** All 64 clean generations reproduce G-CAL-OLMo's byte for byte on every checkpoint, so p §3.1's flag did not fire.
- **The stored-text invariant.** No stored text contains a line break, and the proxy cut nothing.
- **The run.** One shot per checkpoint on `qny1x4v8padeke`, 2026-11-08 04:53Z–05:08Z, with all three runs exiting 0.

## For the seat's read (rule 25; p §8 step 5: "the seat reads every generation")

- **The read:** `results/raw/2026-11-08_gcal-p_read.txt` (`ec0d9d3`), with every generation's text.
- **The run raw** is `results/raw/2026-11-08_gcal-p.txt`, and the box captures are `results/raw/2026-11-08_gcal-p_box-captures.txt`.
- **sft's zero margin.** One fewer hit would have been a FAIL. Code's read lists two graded hits and two misses that could be read differently from the grader. They are not adjudicated, because the grader's verdict stands.
- **Against the seat's §3.3 expectation.** The gains came from Compute (24/24 on each checkpoint) and Write.
  - State/Name did not gain on net: 55 of 84, against m's 56.
  - Item 2 stays at 0/12.
  - On sft, item 8's "the", rendered "ttf", gave 0/4.

## Four items

1. **F-p13 (new) — control characters in stored texts.**
   - Five stored texts carry control characters, all on item 7: a lone DEL on each checkpoint, and ANSI escape codes on dpo and instruct.
   - Nothing gates them. In a session, such a text would be a stored round body that the next round sees.
   - Should p declare a hair trigger or a counter for control characters in stored text before its sessions run?
2. **F-p12 — G-SHAPE-p before LOCK-p v0.1.**
   - p's package hash moved at `e03fbe4`, so G-SHAPE-p must re-run before LOCK-p v0.1.
   - Its writer will not overwrite the artifact at `5009e77`, so the seat must first rule that artifact superseded.
3. **F-p11 — the pinned corrupted-spelling counter still counts some correct answers.**
   - These are common words near a short gold ("there" for "three", "could" for "cold") and a gold's own inflections ("January's"; "Close." for "closed").
   - The counter is descriptive and recomputable, so a refinement would be a reported re-tabulation.
4. **Step 6's go (the PI's).** `p_analyze` and G-ANL-p on the laptop, then each LOCK-p v0.1. G-TIME-OLMo (p) on the box follows.

## The pod

- `qny1x4v8padeke` is up and idle at $1.79/hr.
- The PI's p budget is 12 h for G-CAL-p, the gate stages and the three campaigns. G-CAL-p used about a quarter of an hour of GPU.
- The box repo holds G-CAL-p's six outputs untracked, byte-identical to `b6ef939`. They are moved aside before the next bundle sync.
