# G-PWR (Q-F3): its run of record, and Code's declared readings — Code to design

*F3 session (Code), PI date 2026-11-14. For the PI to route. On the seat's answers of 2026-11-14
(`results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md`, committed at `cdccc66`, sha256
`6b963adf…0db3a`), §A.7 and §D items 3–4, routed by the PI ("Route as given"). What ran: G-PWR (Q-F3), model-free,
by `scripts/mf3_gpwr.py` (sha256 `2b575ef8…d161`) from its commit `46be7aa`. It ran under no lock of its own:
LOCK-m-F3 v0.2 is in force, and F-5 has "Nothing of it touches a file a lock names". Its record:
`data/mf3/gates/Q-F3_G-PWR.json` (sha256 `75d1d46b…01e5`). Read: the program's seven sources (the seat's raw, the
G-F3 entry, PROPOSAL-m v1.11, LOCK-m-F3 v0.2, F-5, Q7, mf3's `resume.py`) and the review raw. Not opened:
`data/mf3/ckpt/*`, `data/mf3/reports/*`. Calendar dates only; the commit hash is the record.*

## §0 Short form

- **The launch counts and looks** (m:192, r = 29/40): A1 128, A1s 64, A2 224, A2s 96, A3 224, A3s 96; **832
  launches, 21 looks**, m:238's row (k 29–28).
- **The power at the planned floors** (m:190): A1 (80, 32) .878 and A2 (144, 56) .862, each at least .85; A3 (144,
  56), the screen, .927, reported. No n is raised.
- **The false-pause figures on the projection** (m:330: α .05 at each of the 21 looks):
  - `round_degeneracy` .1703, `reasoning_line_defect` .1584 and `own_pair_lexical` .1641;
  - the guard's pairs at the common rate .20, each the union of its halves: A1/A1s .2094, A2/A2s .2401, A3/A3s
    .2327;
  - the unit's guard figure, the chance that some pair pauses: .5390.
- **The hours** at m:230's basis: 832 × 641.6–713.6 s = 148–165 h, m:238's column. §A.5's figures are beside, by
  citation: ≈ 300–326 h at G-F3's realised basis, ≈ 446 h if every launch runs complete, ≈ 685 h at the slowest.
- **The cap is the PI's,** at G-PWR's entry (§D item 4). Nothing in this block blocks it.
- **Code adjudicates nothing.** The readings in §1 are Code's defaults, declared on Q7's terms: "strikable until
  v1.0's commit; a strike recomputes figures only". None of R1 and R3–R9 moves the launch counts or the looks; a
  strike of R2 would (§1).

## §1 Code's declared readings

R1–R8 are in the record's READINGS (items 18, 8, 13, 14, 15, 16, 17 and 20; items 1–6 are the seat's, F-5's and
Q7's texts verbatim). R9 is this block's own. The alternatives for R1–R7 are the ones the blind review named
(`results/raw/2026-11-14_mf3-gpwr-program_review.txt`); R2's, F-5's literal text, is its round-1 NOTE 6.

- **R1. The hours basis** (item 18). §A.7's "m:205's basis", and §D item 3's "its m:205 line", are read as the
  unit's own pre-registered basis line, m:230 (Q-F3 uncached, 641.6–713.6 s per session). m:205 is the basis line
  of Q-F0 and the OLMo checkpoints, and holds no Q-F3 figure. The line's oracle is m:238's column, 148–165 h, which
  §A.5's last row also cites. Alternatives:
  - m:205 literally, at Q-F0's 488 s per session: 832 × 488 s = 112.78 h (the reviewer's arithmetic; the record
    does not carry it);
  - no hours line of the program's own, with §A.5's table alone.
- **R2. A1's floor** (item 8). F-5's "A1 96/32" is read as m:184's cached floor. Q-F3 runs uncached since G-ID-F3's
  FAIL (LOCK-m-F3 v0.2 §3), and m:184 gives "96 cached, 80 uncached / 32". So A1 is figured at 80/32 (.878), and
  m:190's .916 at 96/32 is printed beside and used nowhere. The alternative is F-5's literal 96/32, and it would
  move the launch rule: A1's L 160 (⌈1.15 · 96⌉ = 111, N90 142 at r = 29/40), 864 launches and 22 looks, the cached
  table's row at k 29–28 (m:224), or 154–171 h at m:230's basis. §A.5 figures its hours on 832 launches with A1 at
  128, and LOCK-m-F3 v0.2 §3 takes the campaign's launches from the uncached table (m:234–241).
- **R3. The floor case** (item 13; Q7 (a), Code's Q-F0 reading kept). The three sham arms leave the rotation
  together, at ceil(floor / r) with the pooled r (45, 78, 78) and at the floors themselves (32, 56, 56). Every
  contrast arm launches to its L. Alternatives: one sham arm at a time; or G-F3's per-template validity, under which
  A1s leaves at 64 (its L), A2s does not leave before its L of 96, and A3s leaves at 56.
- **R4. The realised case** (item 14; Q7 (a)). G-F3's realised sham counts, 189 of 240 task rounds and 98 of 144
  reasoning lines (§A.1), are taken as pooled rates per sham launch, 63/8 rounds and 49/12 lines. Each rate is
  applied to every sham arm, `own_pair_lexical`'s A2s and A3s included. The alternative is per template (§A.1: A1s
  52, A2s 57, A3s 80 rounds; 25, 25, 48 lines). The reviewer's per-template figures are in the review raw and are
  not of record. A strike recomputes this case's three bars only.
- **R5. The realised case's rounding** (item 15). Each cumulative count at a look is rounded half up
  (floor(x + 1/2)), with its exact value recorded beside. Alternatives (the review's round-1 NOTE 3): floor, or a
  fractional-n mixture.
- **R6. The guard's figure for the unit** (item 16). m:316 runs the guard per contrast arm, each pair against its
  matched sham. m:285's "the exclusion guard's false-pause figure" is read, for a unit whose guard has three pairs,
  as the chance that some pair's guard pauses: 1 − (1 − u_A1)(1 − u_A2)(1 − u_A3). It is exact under Q7 (b)'s model,
  because the three pairs share no session. Each pair's own figure is beside. The alternative is each pair's figure
  alone.
- **R7. The joint** (item 17; Q7 (c), carried to three bars). The joint figure is each bar's own on the projection,
  with the guard's beside: each pair's union and the unit's figure. The joint over the three bars, and over the bars
  and the guard, is not computed, and the record's sentence says why. The alternative is Q7 (c)'s literal:
  `round_degeneracy`'s own figure alone, with the other two bars beside.
- **R8. Two departures in form** (item 20; the program's entry, `46be7aa`); neither moves a value:
  - `LOOK_EVERY` is read from `valence_core.m.resume`, not from Q-F3's own `valence_core.mf3.resume`, whose import
    would open a file under `data/`;
  - Q-F0's figures are checked against `m_gpwr`'s own pins of its reviewed run, not by reading
    `data/m/gates/Q-F0_G-PWR.json`.
- **R9. G-VER** (§A.7: "G-VER as `pq:`§5 names it"; `pq:`§5: "after G-F3, G-VER and G-PWR"). G-VER is read as
  m:284's verifier, which in Q-F3 runs inside every stage on every record. G-F3's entry records all 40 records
  verified (§A.1: "every record verified"). So Code reads no separate G-VER step as owed before the cap, and
  LOCK-m-F3 v1.0's draft would cite G-F3's verification for it.

## §2 Questions

None blocks the PI's cap.

- **Q1 (R1, the hours basis).** Does the program's hours line stand at m:230's basis, against the literal "m:205"?
  The cap goes to the PI with §A.5's table either way (§D item 4).
- **Q2 (R9, G-VER).** Is G-F3's per-record verification §A.7's G-VER step, as Code reads it? If not, what does it
  owe before LOCK-m-F3 v1.0?

## §3 Not questions

- **The cap.** It is the PI's, at G-PWR's entry (§D item 4). The figures go to the coordinating session, which puts
  the question to the PI with §A.5's table.
- **R2–R8** stand on Q7's terms unless the seat strikes one; a strike recomputes figures only. Of them, only a
  strike of R2 would move the launch counts and the looks (§1), and with them the hours the PI's cap is set on.
- **An observation** (rule 11, descriptive; Code adjudicates nothing). With 21 looks at α .05 each and no spending
  (m:330), each bar's false pause on the projection is .16–.17, and each guard pair's union is .21–.24, with the
  unit's guard figure at .5390. These are figures at the null rates (each bar's p0; the common rate .20). Q-F0's
  G-PWR, at 5 looks, gave .0976 for `round_degeneracy` and .1496 for the guard's union.
- **The run's facts** are in the entry: the launch checks, the byte-identical second run and the verifier.
