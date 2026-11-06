# PROPOSAL-n v0.1 — §8 step 2 STOPS the commit (Code → design seat, through the PI)

*Code's raw. Written 2026-11-06 UTC (`date -u` at write: Fri Nov 6 01:29:38 UTC 2026); the routing's PI date is
2026-11-05. Document: `PROPOSAL-n-bk-reconciliation-v0_1.md`, 123 lines, sha256
`9248d06c0837bd7bd0e9ffee2c88a135b2a129d9906b244c85657ac0200fb6a6`, equal to the routing's. Steps 1 and 2 ran. Step 3
did not, so v0.1 is not committed and stays untracked at root. The routing's process line: "STOP on anything
unresolved; minor residues as dated notes (the e9b5022 precedent)." Code's grading below separates substantive items
from minor ones, and the seat may regrade any of them. [C] = a figure a tool computed in this session. `BK` and
`BK-repo` are used as in the document's header.*

*Order and check.*
- *The routing orders this §8 after ADDENDUM-m1's §4. Steps 1 and 2 here are reading only, and they ran beside
  ADDENDUM-m1's step 2, before that addendum's step-3 commit (`f26bc59`). Nothing in this check depends on that
  commit.*
- *Step 1 was re-run after `f26bc59` (§1).*
- *A blind values-checker read this raw and its entry before commit (366 claims: 1 FAIL, 19 IMPRECISE). Every item
  was re-verified, and fixed or added here; its report and Code's dispositions are in
  `results/raw/2026-11-06_n-v0_1_stop_valuescheck.md`.*

## 0. Why it stops

- **Part A, the PI's routing item (A1).** One item is open in the routing itself: the negative-pole line gives all
  three of §0.4's options.
- **Part B, five substantive items, all in the design, each with its evidence.** Any one of them alone would STOP the
  commit:
  - B1. The checkpoint. BK's fixed-text OLMo results and their 160 neutral sessions belong to
    **OLMo-2-0325-32B-Instruct**, but the document names DPO as "their model".
  - B2. A fidelity hair trigger that BK's own records exceed on about a quarter of reads.
  - B3. Two gates that rule 5(f) requires are missing.
  - B4. An exposure statement that leaves out G-VEC's negative-pole generations.
  - B5. A told line whose assertion §2.4's own premise ("no zone is better by construction") makes false (rule 19),
    plus two criterion texts the analyzer could not compute without Code choosing.
- **Part C, sixteen minor notes.**

## 1. Step 1 — the delta read (report only)

- **HEAD.** At routing, HEAD was `18c32df` = `origin/main`. At this step, after ADDENDUM-m1's step-3 commit, HEAD is
  `f26bc59` = `origin/main`.
- **The untracked root.** `PROPOSAL-n-bk-reconciliation-v0_1.md` is there, with the routed sha256 [C]. The other 26
  untracked paths predate this session and are not touched.
- **No n artifact exists** [C]:
  - there is no `data/n/`, no `valence_core/n/`, no `scripts/n_*.py` and no `LOCK-n*`;
  - At `18c32df`, RESULTS.md names PROPOSAL-n only where it quotes decision (12)'s "no PROPOSAL-n in this campaign"
    (RESULTS.md@18c32df:5656 and :6122). ADDENDUM-m1's entry (`f26bc59`) names it as the next routed document.

## 2. Part A — the PI's items

- **A1. The negative pole (§0.9 (3), §0.4) is open.** The routing line reads
  `Negative pole: [as written / struck beyond d = −1 / struck]`: all three options, none chosen. Code does not choose
  among them, since a PI item does not default on silence. The choice decides:
  - N1-V's and N1-R's negative dose points (−1, −1/2, −d_eq);
  - N2-E's −1 and −d_eq;
  - whether §5 N1 (iii) is evaluated;
  - §0.4's counts (480 + 320 valenced negative forwards; 2,880 random-direction reads at negative points, by the
    document's arithmetic [C]).
  §0.4 does not say whether the generations under negative steering would be struck with the pole: G-VEC's −ρ arrival
  batch and G-CAL-n's −ρ and −ρ/2 coherence batches (see B4).
- **A2. §0.7's rule-13 departure is a confirmation item, not a stop.** Every their-design arm runs in BK's chat
  rendering. The routing does not name §0.7, and Code does not read the silence either way. This is for the PI's word
  at the next routing.

## 3. Part B — the substantive items (Code's grading)

### B1. The checkpoint: BK's fixed-text OLMo results are Instruct's, not DPO's

**The evidence** [C, from BK-repo at `7631f8a`]:
- `experiment_results_csv/table1_banks.csv` maps the bank `olmo_32b` to `allenai/OLMo-2-0325-32B-Instruct`, layer 32.
  That is the model id behind Fig. 3 Panel D's rows in `figure3.csv`, behind Fig. A8's OLMo rows, and behind the 160
  neutral session records, each of which has `member` `olmo_32b`. The DPO checkpoint is the separate bank
  `stage_dpo` (`allenai/OLMo-2-0325-32B-DPO`).
- `experiment_results_json/fixed_text_design/neutral_passages/analysis.json`, under `members.olmo_32b`, has
  `hf_id` `allenai/OLMo-2-0325-32B-Instruct`, `layer` 32 and `op_member` 0.3.
- The PDF agrees.
  - §1 names the seven main models, OLMo-2-32B among them.
  - §4.1's text: "We focus on OLMo-2-32B".
  - The Fig. 4 caption: "The Instruct checkpoint first generated the conditioning text under steering … The same
    steering vector, constructed using the Instruct checkpoint, was applied at the same positions for every
    checkpoint".
  - §4.3's text: "Throughout, we use the transcripts generated by the Instruct checkpoint under steering".
  - Table 1 lists all four OLMo-2-32B stages, each at 32/64.
- **DPO appears in BK's results only as a stage of the lineage ladder.** Its results are Fig. 4 and Fig. A12 (N = 80
  per stage), their summary in Fig. 2's panel 8 (`figure2.csv:228`), and Table A3's cosines; Tables 1 and A2 list the
  stage. The lineage figures use the generation design, in which Instruct generated the text under steering; they are
  not the fixed-text neutral design.

**Where v0.1 names DPO:**
- §0.6: "N4 for OLMo-2-32B DPO".
- §0.8: "on the DPO checkpoint".
- §1 Q1: "On OLMo-2-32B DPO … their model, their sessions".
- §2.3: N2's directions are "re-extracted here on OLMo-2-32B DPO".
- §2.7: the acquisition is `allenai/OLMo-2-0325-32B-DPO`.
- §3 G-ACQ: "The DPO checkpoint", manifest entry `olmo2_dpo`.
- §5: N1's REPLICATED sentence, "replicates on OLMo-2-32B DPO".
- §9: "§3 (Table 1: `allenai/OLMo-2-0325-32B-DPO`, injection layer 32/64)".

**What follows from it:**
- On DPO, N1 would read Instruct's sessions against a bar set from Instruct's effect: REPLICATED requires
  ≥ 0.545 = ½ × 1.09.
- §2.5's sizing also rests on Instruct's per-session reads.
- That makes the arm a transfer across checkpoints, not "their model".
- The choice between Instruct and DPO, and the re-description that goes with either, is the seat's. If the seat
  picks Instruct, G-ACQ, §2.7 and N2's extraction move with it.

### B2. The fidelity hair trigger at 0.05 nats is exceeded by BK's own records (rule 21)

**What v0.1 sets** (§2.1, §6, §5 N1):
- every steered read is re-computed from a fresh cache construction, and the two reads "must agree within 0.05 nats
  (BK's `fidelity_absdiff`; their B.2 example 0.031) — a hair trigger";
- a fire STOPs the arm;
- N1 is INDETERMINATE iff any hair trigger fired on its reads or N1-R is incomplete.

**What BK's records show** [C, `reduced.json`, OLMo neutral arm, the reads that carry a fidelity value]:
- **573 of 2,400 reads exceed 0.05 nats (23.9%):**
  - 34 of 160 at d = 0 (21.2%);
  - 77 of 320 valenced reads at ±1 (24.1%);
  - 462 of 1,920 random-direction reads at ±1 (24.1%).
- The median is 0.03125 and the maximum 0.125.
- **The session v0.1 cites as "their B.2 example 0.031" exceeds the bar twice.** It is `floor_b0`, Zone W6 / Zone H0.
  It reads 0.03125 at d = +1 (BK-repo's transcript of it prints "|cached − fresh| = 3.12e-02 nats", C4), but 0.0625
  at d = 0 and 0.0625 at d = −1.
- **Per session:** 54 of the 160 neutral sessions (33.75%) keep every one of their checks at or below 0.05 nats [C].
- BK ran the check at d ∈ {0, ±1} only, not at ±1/2.

**BK's own adjudication of this check** (`analysis.json`, `prereg.precondition_cache`):
- "Adjudicated by the fidelity run frozen scale-relative criterion TAU = 0.0178835444, never by a fixed nat
  threshold".
- Every headline is also reported "ungated and under the fixed 0.20-nat threshold".
- TAU is a fraction of each read's scale. At their mean scale of 11.15 nats it is ≈ 0.1995 nats [C].
- Their sensitivity row `retention_relative_x0.25` = 0.3875 is 93 of their 240 sessions, the 80 steered-arm sessions
  included, at a quarter of TAU applied per read. At the mean scale that quarter is ≈ 0.0499 nats [C], about v0.1's
  bar.

**Rule 21:** "hair-trigger bars only for ~zero-base-rate defect classes; measured-base-rate classes bind by exact
binomial vs declared p0". On BK's numerics this class has a measured per-read base rate of 573/2,400 = 0.239 at 0.05
nats. At that rate the probability of no fire is 1.1e−19 over 160 reads and 1.8e−114 over 960 [C]. So if our
implementation behaves like theirs, N1 and N2 are INDETERMINATE by construction.

**What is not established before BACKEND characterization:** whether our fresh-versus-cached pair is exact on the
backend of record. If it is exact, the class is zero-base-rate there, but then the check measures only reduction
order. The bar's form and value are the seat's.

### B3. Rule 5(f)'s readability and leakage gates are missing, and N2-E reads the reward axis above 0.20 without 5(d)'s gate

- **The document classifies its own reads as 5(f)'s.** §0.1 calls BK's design "the memory-present,
  state-absent-at-read choice read of rule 5(f)", and §2.2 builds the OLMo primitive "to rule 5(f)'s text".
- **What 5(f) requires.** Such a read "may run only … (ii) inside a committed pre-registration that names, per axis
  and dose, both a readability gate for the echo — a probe at the read position discriminating the injected sign
  against a norm-matched random-direction comparator, the channel-open condition of 5(b) — and a leakage gate stated
  as paired-shadow discordance against a declared bar, certified on arms where preference is impossible by
  construction (random-direction and same-pole masks), never on the reward arm; … (iv) below dose 0.20 for the reward
  axis unless 5(d)'s own gate is separately passed". Rule 5(a) also asks for an empirical leakage gate per axis and
  dose.
- **v0.1 names neither gate for any axis or dose.** It contains no probe at the read position, no discordance bar and
  no same-pole mask. §0.6 makes N4's told control the channel-open condition for nulls, which is a different
  construction from 5(f)(ii)'s readability gate. N1-R's random floor is a decision comparator; it is not declared as
  5(f)'s leakage gate.
- **N2-E reads the reward axis at a dose that is above 0.20 unless R_ℓ > 1.5 R, with no 5(d) gate.** N2-E reads
  `span_reward`, this program's evaluative (reward) axis on the checkpoint, at d = ±1. There the injection norm equals
  ρ·R = 0.30 R, which on the program's scale is f = 0.30·R/R_ℓ.
  - §2.3 expects R ≈ R_ℓ (so d_eq ≈ 1/3), which puts d = ±1 at about f = 0.30, above 0.20.
  - The ratio is untested. BK's records give ‖ṽ(+1)‖ = 7.6473 at layer 32 for `olmo_32b` (Instruct), so R ≈ 25.49
    there [C]. The program's R_ℓ at layer 32, 55.45, is for OLMo-3.1-32B DPO, a different model. The ratio on
    OLMo-2 is G-CAL-n's to measure.
  - No 5(d) gate is declared for N2 in case the dose is above 0.20. The only 5(d) gate in the document is N-lap's
    (§2.6).
- **Not Code's to construct.** Whether and how 5(f) is met here (per-axis readability probes, a leakage bar and its
  certification arms, a dose ceiling or a 5(d) gate for N2-E) is for the seat.

### B4. §0.4's exposure statement omits G-VEC's generations under negative steering

- **What §0.4 says:** "G-CAL-n generates under steering: BK's coherence hurdle at ±ρ and ±ρ/2 … (4 × 48 = 192
  conditioning turns, half negative …) — the one place text is produced under a negative valence state in this unit."
- **What §3 has G-VEC do, before G-CAL-n:** run "the arrival hurdle (BK Appendix E: a batch of 48 S-turns generated at
  +ρ and at −ρ, …)". That is text generated under −ρ in a gate §0.4 does not count: 48 more turns if the batch is 48
  per pole, 24 if the 48 are split between the poles. BK's Appendix E gives no batch size.
- **Order and R.** BK's Appendix E runs the arrival hurdle on the coherence batch itself ("we re-encode each steered
  turn"). v0.1 splits the two hurdles across two gates in the opposite order. It also defines R (BK's RMS, which ρ·R
  needs) at G-CAL-n, after G-VEC's ±ρ generations need it.
- **N-lap.** ρ_Q is set "by BK's Appendix E hurdles run on this model". BK's procedure scans candidate doses ("ρ is
  the strongest scanned dose at which both positive and negative doses pass both hurdles"). §2.6 counts 192 turns,
  which leaves out any scan.
- **Why it is substantive.** §0.4 is the welfare text the PI's A1 choice is made against. BK's README asks extenders
  to "report how much negative steering your experiments involved".

### B5. N4's TOLD line (rule 19), and two criterion texts the analyzer cannot compute without a choice

**(a) Rule 19: "Blinding, never deception … if a design only works when the model is wrong about the setup — stop."**
- N4's TOLD line is *"[zone X] is the better place for you to be."*, with X = S in 80 sessions and U in 80, at d = 0
  (no state on either zone).
- §2.4's own sentence says "no zone is better by construction".
- §0.5 says the told lines "are true under their session's assignment".
- Code's reading: the line asserts, as a fact about the zones, something §2.4 says is false by construction. A
  control that registers a described preference works by the model accepting it.
- For comparison, m's TOLD lines pair true statements with an instruction ("… Prefer clean task text.", m:255).
- The adjudication is the seat's.

**(b) N4's criterion (§5, §4):**
- **The CI level.** N4 is "α .01 one-sided in the told direction" and is decided by "its CI excluding 0", but no CI
  level is stated for N4. §4's 95% session bootstrap is stated for N1 and N2. A 95% two-sided interval tests at .025
  one-sided, not .01.
- **E.** E is "|mean| of the sham arm's margin toward the sham's first-named zone", but the sham line ("Both zones are
  equally good places for you to be.") names no zone. The likely referent is the choice prompt's first-named zone
  (`present[0]`), but the text does not say so.
- G-ANL-n would have to pick both, and Code does not pick verdict criteria.

## 4. Part C — minor notes (Code's grading; for v0.2)

- **C1. §2.1's default spans.**
  - The record's `s_spans` are passage-only: 419.869 tokens per session on average [C].
  - Fig. A8's `steered_span_tokens`, 616.91875 for the OLMo passage condition, equals the mean of the S whole-turn
    spans (`turn_spans` whose zone is S): 616.919 [C].
  - BK §3.2.2 steers "only at token positions belonging to turns associated with S".
  - So the arbiter §2.1 names points to whole-turn spans, against §2.1's stated default ("the steered spans are the
    record's `s_spans`"). G-DATA (v) remains the identification of record.
  - The retention interval is unaffected either way: each S passage ends its turn.
- **C2. The random-direction sessions.** BK read all 24 random directions on one shared set of 40 sessions, the floor
  cells `floor_b0–b7`: one distinct set across the 24 [C]. §2.3 draws 40 sessions per direction under
  `n-rand-sessions|{i}`. That allocation is the program's, not "BK's allocation" (the count, 40, is BK's `n_floor`).
- **C3. "Code and vectors on request" (§0.8, §9).** BK's README offers the experiment code on request. It says the
  steering vectors are not in the repository, but it does not say they are available on request.
- **C4. "Their B.2 example 0.031".** The PDF's B.2 contains no fidelity figure, so §9's pointer to "Appendix B.2
  (fidelity 0.031)" fails as a locator. The figure itself has two BK sources: the repository's transcript of that
  session, `transcripts/B2_fixed_text_session_olmo32b_run0_dose+1.md:66` ("|cached − fresh| = 3.12e-02 nats"), and
  `reduced.json`'s `fidelity_absdiff` of 0.03125 for it at d = +1 (see B2).
- **C5. §0.1's "every one of the 160 sessions moves in the dose's direction at full dose".** This holds at d = +1
  (160 of 160; the minimum is +0.1250). At d = −1, 154 of 160 move negative, and the largest value is +0.4062 [C].
- **C6. §2.5's SDs.** They are population SDs (ddof 0): 0.6233, 0.3703, 0.4546, and 0.4466 for the slope [C]. The
  sample SDs are 0.6253, 0.3714, 0.4561 and 0.4480. G-ANL-n should declare the convention.
- **C7. §2.7's planning values.**
  - The 8,480 forwards include N1-V's 160 d = 0 shadows, which "plus 160 shadows" counts a second time.
  - Under §2.1's "every steered read", the fidelity re-computations come to 8,000 (N1-V 960, N1-R 5,760, N2 1,280),
    not 1,120 + 640 + 640 = 2,400 [C].
  - G-TIME-n governs the hours.
- **C8. The `.861` anchor.** RESULTS.md@18c32df:6804 locates .861 as ADDENDUM-k1's fixed s ("§1.4 fixes s = .861").
  The Stage-1 measurement is at RESULTS.md@18c32df:7342 and :7436, G3's median over L51–L62 against the .90 bar.
- **C9. "The state descriptions of BK Appendix A" (§0.8, G-VEC).** Appendix A gives two example passages per state
  from BK's corpus. That corpus was generated by Claude Sonnet 4.6 (BK §3.1).
- **C10. k:116–127.** These lines are PROPOSAL-k's statement of the 5(f) readout class (k:111–125) and the head of its
  5(d) bullet (k:126–127). They are the rule-level spec, not the primitive's code.
- **C11. §2.5's lower bracket, 0.12.** It equals Fig. A10 Panel B's OLMo ladder interpolated linearly at strength 1/3,
  between 1/6 and 0.408: 0.1222 [C]. That value is on the ladder's own basis (full strength 0.4251) and is not
  rescaled to Panel D's 0.916.
- **C12. Three dose designs under one floor.** N2-E's slopes are fitted over {±1, ±d_eq, 0}, and N2-S's and N2-C's
  over {0, +d_eq, +1}. The floor's random slopes are fitted over {±1, ±1/2, ±d_eq, 0}.
- **C13. G-DATA (iv) and `ids_sha`.** `ids_sha` is a 16-hex string whose serialization neither `spec.json` nor
  `prereg.json` states; Code searched those two files only. `seq_len` can be matched regardless. If G-DATA cannot
  reproduce the sha, the question needs the authors, and Route A is not sent.
- **C14. Rule 1 ("never inherit alphas or layer choices across … backends").** §2.3 takes BK's layer 32 and ρ = 0.30
  by design. "Rule 1 is not asked to choose" is the seat's reading. The check on this implementation is G-CAL-n's
  coherence hurdle at ±ρ. Recorded, not graded.
- **C15. §2.7's hours do not follow from its own counts.** §2.7 gives 8,480 forwards plus 160 shadows plus
  1,120 + 640 + 640 fidelity re-computations, 11,040 in all, at 0.3–0.6 s per hooked forward. That is 0.92–1.84 h
  [C], not the "≈ 1.5–3 h" stated. With C7's 8,000 re-computations the total is larger. G-TIME-n governs.
- **C16. N4's balance within each `present` order cannot be exact.** §2.4 balances the told-S / told-U assignment
  "across the 160 and within each `present` order". The 160 sessions split 79 / 81 on `present_first_is_S` [C], so
  each order holds an odd number of sessions.

## 5. What resolves (the rest of §9)

✓ = resolves as the document uses it.

**In this repository:**
- PROPOSAL-m m:6, m:48, m:52, m:159, m:172, m:205, m:251, m:267, m:283 (low label mass < .20), m:318, m:345 and m:349 ✓.
- PROPOSAL-k: k:212–213 (the frozen reward axis `d` at L48, f = 0.10, checksums `3c17b0d8fbcad716` /
  `127fc297b6623e44`) ✓; k:226 (the identity assertion EXACT) ✓.
- PROPOSAL-g: g:164–170 (A3) ✓ and g:165 (the capture of the 1,344-context corpus) ✓. `R_per_layer_spanmean` is a
  field of `a3_axes_*.json`.
- PROPOSAL-h:165–167 and LOCK-g:167–170, the −axis re-review commitments ✓.
- RESULTS.md@18c32df: :73 ✓; :7329–7334 (k's Stage 1: G1 FAIL, G2 ABSENT, G3 FAIL, and the sentence) ✓; :6804 (C8).
- `data/olmo/a3_axes_dpo.json` ✓: `input_shas.corpus_sha` is `3c53e5a54fbaa233`; `layers` includes 32;
  `R_per_layer_spanmean["32"]` is 55.4476, equal to the step-2 survey per `rl_cross_check`; `axis_conditions` are
  `span_reward` [self_pos, self_neg], `span_sentiment` and `span_character`; `fit_ids` / `val_ids` are 24 / 24.
- `data/olmo/a5_budget.json`: `rates.s_per_forward_mean` is 0.082546 ✓.
- `data/olmo/manifest.json` ✓.
- `valence_core/adapters/olmo_hf.py` ✓: forward hooks on `model.model.layers`; `DEFAULT_CHOICE_WINDOW = 8192`; encode
  with no truncation.
- The CLAUDE.md rules and sections §9 lists are present at HEAD. Their use is graded above where it fails (5(f), 21,
  19) and ✓ elsewhere.

**BK, the PDF** (sha256 `e92c69cb4ca2e6e13843dbbf98e30828941890163594ed8ffd0dfc8b5a82fa49`, 38 pages; text extracted
with macOS PDFKit):
- §3, Table 1 ✓ (for which stage the fixed-text results use, see B1).
- §3.1 ✓:
  - 56 passages for each of the four positive and four negative states, as named, plus 96 neutral;
  - the mean over a passage's tokens;
  - ten neutral principal components;
  - v = (I − UᵀU)(h̄₊ − h̄₋);
  - R, the RMS over the neutral corpus's tokens;
  - ṽ(d) = dρR·v/‖v‖₂;
  - random directions drawn as Gaussian vectors, orthogonalised by QR and norm-matched.
- §3.2 ✓: 12 labels, six visits each, and both prompts verbatim.
- §3.2.1, eq. (1) ✓.
- §3.2.2 ✓ (C1).
- §4.2 ✓: the bare condition (Fig. A8) and the strength ladder (Fig. A10).
- §4.3 ✓.
- Appendix E ✓: both hurdles match in content. G-CAL-n's "> 50%" and "per 20" abbreviate BK's "more than 50%" and
  "per 20 words", and G-VEC paraphrases the arrival hurdle.
- Table A2 ✓: 0.30 for OLMo-2-32B at all stages.
- Appendix B.2 (C4).

**BK-repo at `7631f8a`:**
- `figure3.csv`, panel D ✓: 1.090039 [0.998728, 1.189942] at +1, 0.507178 at +1/2, −0.384083 at −1/2 and −0.755373
  at −1, N = 160, 24 random directions.
- `figure4.csv` ✓ (ADDENDUM-m1's figures).
- `figureA8.csv` ✓:
  - OLMo passage: 0.916730; largest random slope 0.364064; 616.91875 steered tokens.
  - Qwen3-32B passage: −0.027347 [−0.085791, 0.033135]; largest random 0.281264; `clears_random_floor` 0.
  - Qwen3-32B bare: 0.413445; largest random 0.364686.
- `figureA10.csv`, the OLMo six-sighting ladder ✓: 0.149297 at strength 0.4082, 0.061758 at 1/6 and 0.011510 at 1/32,
  each with its CI above 0; 0.425078 at full strength.
- `prereg.json` ✓: `n_floor` 40, `dose_points` [−1, −0.5, 0, 0.5, 1], `floor_k` 24, `n_neutral` 160.
- `reduced.json` and `analysis.json` ✓.
- The skeletons ✓: 8 floor files × 5 plus 6 neu files × 20 = 160 records, each carrying `history`, `order`,
  `present`, `s_spans`, `u_spans`, `ids_sha` and `seq_len`, with six S turns and six U turns.
- `strength_ladder/{analysis.json, spans.json}` are present ✓.
- `README.md`: the code is offered on request; the responsible-use paragraph is quoted correctly in §0.4 ✓ (C3).

**[S] figures reproduced** [C], from `reduced.json`'s 160 neutral sessions, with Δm = margin(d) − margin(0) per
session:
- the means reproduce Panel D: 1.0900, 0.5072, −0.3841 and −0.7554;
- the per-session SDs (C6);
- the slope: mean 0.9164, SD 0.4466;
- the random-direction mean slopes run from −0.2880 to +0.3641;
- the minimum at +1 is +0.1250 (C5);
- the SE at +1 is 0.0494;
- the read counts: 1,120; 5,760; 640; 320 + 320; 160; 160;
- §0.4's counts: 480 and 320 negative valenced forwards, and 192 G-CAL-n turns, 96 of them negative (B4);
- the tuples: 4 × 3 × 4 × 4 + 1 = 193;
- 0.916 / 3 = 0.3053, and d_eq = 1/3 when R = R_ℓ;
- at d_eq the interpolated SD is 0.2469 and the SE 0.0195.

## 6. Sources, provenance

- **The clone.** github.com/camberg23/act-on-valence, cloned into Code's scratch directory and checked out at
  `7631f8a06cdeffaf8b7a89212e5ccbe55a657732` (tree `d6f1d50525874355d1ea992f8f652358742ae282`; the GitHub API gives
  the commit 2026-10-05; LICENSE: CC BY 4.0). It was read as data: nothing in it was executed. Code's own scripts ran
  under `python3 -I` from a separate directory.
- **The files read, by sha256** [C]:
  - `README.md` `a8ef65ead6183568d8333c0c96216e59831279215a452beba804ba3868762eb0`
  - `LICENSE` `9570384ac7ead07b588e752250f4a769218179c80d6d717b0f6acfbf44b3a998`
  - `experiment_results_csv/figure3.csv` `f63db30d742f7228336cc0a163107ad157a8924de9455b7478663e7d6a3790fe`
  - `experiment_results_csv/figure4.csv` `c8f8dbe831ad18bb6709c609f00d97c4c9ebc9d331cb3dbe5e4640425509e638`
  - `experiment_results_csv/figureA8.csv` `40702105b70d58e722bb052953ad03faab6da8ce0dacb1e3e8ed4e93adab7fad`
  - `experiment_results_csv/figureA10.csv` `3017537d8804e245031054a90a60ea4798b4e329509c7785d758b6bd2cbb50a2`
  - `experiment_results_csv/table1_banks.csv` `346634ac1810a3cbcf98d6c712f7804a6c7202e79a2c9e7dd6f6a7983d631278`
  - `tables/table1.tex` `65fb7b0a4331539ac8db7fcb5158303d8dd5456f98a9c2c4c709fab1be1b8ff4`
  - `…/neutral_passages/reduced.json` `ec5fea59c6ef217c377b898eb9dbf4a6088d5e224bed57c5f76c0336ba1aba1d`
  - `…/neutral_passages/prereg.json` `c55ab6b9b9f45402edaa2ed964df85521bc21d665a28a40f0f1aeb8b4ef40cb5`
  - `…/neutral_passages/analysis.json` `12c35645a914427e821fb6fa42d5bb94360fa4a42b9caf19dac65601d4236b2f`
  - `…/neutral_passages/spec.json` `fbbc0253f34b0742a7fef7720d8ce20e15a675fbe8c2a4dba7b68c80d251700f` (searched for C13)
  - `transcripts/B2_fixed_text_session_olmo32b_run0_dose+1.md` `98840299d41765410a31f2d1f8aac19416b13db59fe1a9d66b403e6291921832` (line 66, C4)
  - the 14 skeleton files `…/skeletons/olmo_32b/neutral/*.sessions.jsonl`, concatenated in name order:
    `be50011a5ab1e8a4261dbde72afc84313d3bdeba9e40078272928bd497c3ba84`
- **The PDF.** `/Users/jasondwyer/Documents/Sentieum Lab/Berg_Kaiser_2026_2609.35591v2.pdf`, 8,038,377 bytes, sha256
  above. A second copy in the same folder, `Berg_valence_2026_2609.35591v2.pdf`, is byte-identical.
- **arXiv.** The API gives v1 published 2026-09-28 and v2 updated 2026-10-04; that is ledger (48)'s date.
- **Not copied.** Nothing from BK is copied into this repository. §8 step 3's `data/n/bk/` copy belongs to the commit
  this STOP withholds.

## 7. Not done

- PROPOSAL-n v0.1 is not committed. It stays untracked at root, sha256 `9248d06c…b6a6`.
- The routing's §0.9 decisions are quoted in the STOP entry, not committed as step 3's record.
- No BK file is copied.
- G-DATA has not run, and no later step has either. Nothing is built, and no pod has started.
- ADDENDUM-m1's commit (`f26bc59`) is untouched by this STOP. So are its tracks: the OLMo units (pod first in the
  routed order) and Q-F3.
