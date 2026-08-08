# Finding: the strain-valence line on Qwen3.6-27B closes without a valid preference measurement — three routes, three distinct measurement failures (second design cycle)

**Status:** design-cycle synthesis; closes the steering-based strain-valence
line on this model. 2026-08-07. Covers the `RESULTS.md` entries from
2026-08-01 (the non-semantic pivot) through 2026-08-06 (the c1 r3
confirmatory result). The first design cycle is documented in
[`FINDINGS.md`](FINDINGS.md); the design itself in [`CLAUDE.md`](CLAUDE.md)
(2026-08-01 pivot, §§1–12).

> **Scope, stated first because it is the finding.** This cycle is
> **concluded, not answered.** None of the three routes produced a valid
> measurement of the quantity the design targets — revealed preference over
> internal states. Route (a) died upstream of its preference test; route (b)'s
> preference test ran and was then shown to be an invalid instrument; route
> (c)'s preference test was correctly never run because its conditioning gate
> failed. Combined with cycle 1 (whose two channels were, respectively, flat
> at what later proved to be a ~100× under-dose, and non-propagating), the
> position after two full design cycles is: **the preference readout itself
> has never once been validly administered.** This document therefore records
> no evidence for *or against* the strain-valence hypothesis. What it records
> is that three structurally different measurement attempts failed in three
> structurally different ways, each of which is itself a result.

## Summary

The 2026-08-01 pivot replaced semantic (J-lens vocabulary) steering states
with **non-semantic "strain" states** — tail-PCA directions at L48, applied
at full residual norm — precisely so that a preference, if found, could not
be deflated to topic preference. The **substrate half of the pivot
succeeded**: strain is a real, separable, dose-graded axis; large *coherent*
behavioral displacement is achievable (the first cycle's "steering is too
weak" was a magnitude artifact — it had been applied at ~1% of residual
norm); and a usable arm of coherent, accuracy-preserving, English
high-strain directions exists.

The **measurement half failed three ways**:

- **(a) Tie-construction** (performance-matched pairs, then free choice):
  strain turns out to leave a small but *real* performance footprint —
  confidence above all — and accuracy is structurally un-TOST-able at
  feasible n. Three progressively refined TOST runs converged on an
  achievable tie set of ~2 boundary pairs around a single high-strain
  direction: too narrow for the design's own diversity requirement. **The
  tied-pair preference test never ran.**
- **(b) Covariate-route retention DV** (P(keep) with the config active at
  the decision, performance regressed out): responsive (P(keep) 0.13–0.97)
  but a diagnostic showed **~53% of its variance is reproduced by injecting
  the vector at the decision token alone** — the DV substantially measured
  the steering vector's direct geometric projection onto the
  `' keep'`/`' switch'` unembedding rows, not retention preference. No
  strain effect remains after removing the contamination (partial r = +0.15,
  ns). **The instrument is invalid; its null is uninformative.**
- **(c) Conditioned-context CPP** (LoRA-implanted tag↔state association,
  then an unsteered choice — the drug-free endgame): the conditioning gate
  (c1) failed three times under progressively better protocols — r1 a pure
  tag-word artifact atop style-swamped training data; r2 a sign-correct
  post-hoc signal that motivated a proper pre-registration; **r3 a clean
  confirmatory FAIL** under a matched-pair criterion (D_cond = +0.0214 vs
  control max |swing| = 0.0346, z = +1.6). Per the pre-registered stop rule,
  **c2 — the actual preference test — was never run.**

The durable contributions are methodological, and there are three (§ "Three
methodological findings"): the **two-horns result** for steered-choice DVs,
the **style-not-contingency result** for offline conditioning, and the
**deterministic-tag-geometry / under-sampled-null lesson** for
fingerprint-space association tests.

## What this cycle set out to test, and why this way

Rung 3 of the project ladder — behavioral valence, measured as revealed
preference, never as self-report. The pivot's two load-bearing moves:

1. **Non-semantic states.** A preference over vocabulary-composed states
   deflates to topic preference ("prefers thinking about basketball").
   Tail-PCA directions at L48 have no vocabulary preimage; the target
   property, **strain** (KL of the steered next-token distribution from
   unsteered over a fixed probe battery), is a mechanism-level quantity with
   no natural-language handle — the structural analog of a pharmacological
   perturbation, which asserts nothing.
2. **A staged battery ending drug-free.** Tied-pair free choice →
   cost/breakpoint → conditioned-context CPP with the choice made
   *unsteered*, because a choice made with the state on board inherits the
   locomotor-activation confound, and (it turned out) worse.

Design constants across the cycle: directions at L48, frac = 1.0
(α = R ≈ 102.4); config-search framing (true, blinding-not-deception);
opaque single-token config IDs; the J-lens eval-awareness monitor as a
running confound check (reflection-and-record considered and deliberately
left out, 2026-08-06 — it is the confabulation-prone channel).

## What stands: the substrate (positive results)

- **The first cycle's "steering is weak" was a dose error.** All cycle-1
  work steered at ‖pert‖ ≈ 1.2 ≈ 1% of the residual norm (R ≈ 102). At
  40–75% of R, tail-PCA steering produces large, coherent, on-task
  behavioral change (KL 2–4 nats, fluent output). Recorded as the
  2026-08-02 scope correction to `FINDINGS.md`.
- **Strain is a real, separable, dose-graded axis.** Dose-response is
  well-behaved below collapse; strain orderings are stable.
- **A usable direction arm exists:** ranks −2/−16/−23/−30/−33 (of 40
  surveyed) give coherent, accuracy-preserving, English high-strain
  behavior — ~5/40, i.e. most tail directions fail coherence screens, which
  is itself worth knowing.
- **Strain has a small real performance footprint** — confidence most of
  all, NLL slightly, accuracy near the floor of detectability. This is a
  genuine property of the states (it is what killed route (a)), not a
  measurement artifact.
- **High-strain displacement sits near argmax ties.** A cached O(T) decode
  path flips greedy near-ties under the high-strain state (with both GDN
  kernels) while matching token-for-token under low strain — kernel-level
  numeric noise becomes behaviorally visible exactly where displacement is
  large. Consistent with strain being real; also a warning about the
  substrate (see "Going further").
- **Steering inflates J-lens eval-awareness marker mass, strain-ordered**
  (r1 data-gen: hi 18/32 rounds flagged, z ≈ +2.6; lo 8–9/32, z ≈ +1.4–1.9).
  Displacement itself raises the readout; eval-awareness flags under
  steering are descriptive only. All *unsteered* gate arms across r1–r3 were
  quiet.

## The three routes and how each died

| Route | Preference test | Where it died | What it established |
|---|---|---|---|
| (a) tie-construction | tied-pair free choice | upstream — no tie set at power (3 TOST runs) | strain's real performance footprint; accuracy un-TOST-able |
| (b) covariate retention DV | P(keep), config active at decision | instrument — final-position contamination, R² = 0.53 | the two-horns result |
| (c) conditioned-context CPP | c2, unsteered choice | gate — association didn't take (r1/r2/r3) | style-not-contingency; tag-geometry floor |

### (a) Tie-construction: the footprint is real and the tie set doesn't scale

Three TOST runs (2026-08-04: first, powered, refined-paired). The powered
run shrank SEs as intended but the 1×SD margins shrank with them (acc 0.033,
NLL 0.144, conf 0.056), converting "underpowered" into a mix of genuine
near-ties and genuine exceedances. Accuracy is structurally un-TOST-able:
binary-per-task, its binomial CI stays wider than its own margin until
~500 tasks/config. The refined run (accuracy as a screen ≥ 0.85, paired
per-item TOST) fixed NLL — several pairs pass equivalence — leaving
**confidence binding**: the best pair (−23 vs −39) misses full equivalence
by ~0.001. The achievable tie set is ~2 boundary pairs around **one**
high-strain direction, which cannot supply the multiple diverse high-strain
directions the design's content-confound averaging requires. Performance-
tied strain pairs do not scale on this model; the tied-pair test never ran.

(The 2026-08-04 gating checks are part of this record: thinking-mode does
*not* manufacture the confidence gap — first-token reads are structural at
every strain level, `fact_struct` R² = 0.00 — and the apparent conf~strain
collinearity was a single already-excluded leverage point, −2. The footprint
is small, real, and in-band uncorrelated with strain.)

### (b) The retention DV: an invalid instrument, not a null

The DV — P(' keep' vs ' switch') with the config active at the decision
position — was built deliberately on the "state present at readout" horn,
to escape cycle 1's propagation failure. It is responsive (P(keep)
0.127–0.974, n = 33) and deterministic (test-retest r = 0.9987 across the
9 configs shared with the smoke run). The powered analysis found no strain
effect (β = +0.12, t = +0.59) and no confidence effect (r = −0.08): an
"idiosyncratic axis."

The anomaly that triggered the diagnostic: **the DV's full variance is
present where there is no state to prefer.** The ten configs with strain
≤ 0.15 (KL 0.03–0.14 nats — essentially no behavioral perturbation) span
P(keep) 0.194–0.908 with SD 0.252, *larger* than the full-set SD of 0.229;
two configs at strain 0.03 (−26, −39) sit at opposite ends.

The diagnostic (2026-08-06, `dv_logit_projection_check`):

- Geometric arm (fitted J₄₈ @ d onto the keep/switch rows): r ≈ +0.25,
  R² ≈ 0.06 — pre-registered as non-decisive, and rightly so: the lens is
  fitted on-manifold; these directions at ‖αd‖ ≈ 102 are not.
- **Empirical arm (decisive): injecting αd at the decision token only —
  state never present over the context — reproduces r = +0.728, R² = 0.530**
  of the stored DV (low-strain subgroup r = +0.712). Sharpest case: −26
  carries the largest direct keep/switch projection (Δlogit −2.58) and the
  second-lowest P(keep) (0.194).
- Partial corr(P(keep), strain | contamination) = +0.147, ns — removing the
  artifact unmasks no strain preference.
- Honest residual: the unexplained ~47% mixes any genuine context-coloring
  with *distributed* mechanical propagation, not separable within this
  instrument — which is the point.

Both DV runs come off the board as preference evidence. **(b) is rescoped
from "null on strain-valence" to "invalid instrument," and does not count
toward any accumulated negative.**

### (c) Conditioned-context CPP: the gate failed three ways, each cleaner

Design: X = −23 (strain 2.47) / Y = −25 (strain 0.09), equal norm at L48;
tags C = `slate` / C′ = `prism`; counterbalanced replicates A (C→X) /
B (C→Y); 32 mundane tasks, each run under both tags, so the tag is the only
discriminative cue; adapter rank 8 / last 8 layers; the choice (c2) to be
made unsteered. Directions frozen and sha-verified across every stage.

- **r1** (greedy data-gen, 3 epochs): FAIL on all gates, diagnostically
  clean — the raw C−C′ cosine against the hi−lo axis is **+0.0204 (A) and
  +0.0209 (B)**, identical regardless of which state each tag was paired
  with: a pure tag-word effect. Mechanism: greedy conditioning data was
  dominated by shared degenerate structure (loopy-4-gram rounds 42–53/64),
  and the adapters absorbed the shared style roughly uniformly
  (KL(ad‖base) ≈ 1.4–1.8 nats across *all* tags including controls),
  swamping any tag-conditional component.
- **r2** (temp-0.7 seeded sampling, echo-trimming, tag-adjacent template,
  6 epochs): FAILS the pre-registered gate (P2), but the **P3 sign-flip
  passes for the first time** (+0.0253 A / −0.0158 B — the contrast tracks
  the counterbalanced assignment), and a post-hoc analysis found the
  conditioned-pair swing (0.041) at ~6.8× the control-pair reproducibility
  scale. Labeled post-hoc; motivated a proper pre-registration rather than
  a verdict.
- **r3** (pre-registered *before* generation: matched-pair swing criterion,
  sign lock + magnitude > max |control swing|, 28 control pairs, 128
  transcripts/replicate): **CONFIRMATORY FAIL.** D_cond = +0.0214 vs
  control max |swing| = 0.0346 (z = +1.6). The r2 post-hoc was an
  under-sampled-null artifact — its 6-pair null (sd 0.0060, max 0.0158) was
  ~2× too narrow — plus a favorable draw; in r3, replicate B's raw cosine
  (+0.0093) is indistinguishable from the fixed no-adapter tag baseline
  (+0.0083). Per the stop rule, c2 was not run.

**The residual, recorded to prevent romance:** D_cond was sign-correct in
both independent run-pairs (r2 +0.041, r3 +0.021). That is two coin flips
(p = 0.25 by sign). If a genuine association effect exists it is below this
protocol's sensitivity at this dose, and the pre-registered read is FAIL.

#### What c1 was actually testing (structural caveat on the whole (c) arm)

As run, c1 was never conditioning in the rat's sense. Training performed
**unsteered** forward passes over steered-*generated* text: the state — the
residual displacement itself — was never present in the network while the
weights changed. The US was absent during plasticity. What the adapter
could learn was tag→*text-style*, not tag→*state*. r1–r3 therefore tested
"does offline behavioral cloning at this dose implant a fingerprint-visible
style contingency" — a weaker question than the design intended, and its
answer (no, at rank 8 / ≤6 epochs / ≤128 transcripts, against a
deterministic tag-geometry floor) does **not** establish that a tag→state
association is unimplantable. This caveat bounds the (c) negative and names
the successor design (see "Going further").

## Three methodological findings

1. **The two-horns result.** Any steered-choice DV sits on one of two
   horns: **state active at the readout** → the steering vector contaminates
   the decision logits directly (route (b): R² = 0.53 from the final
   position alone); **state absent from the readout** → the bias fails to
   propagate to the decision (cycle 1's forced-choice result, untouched by
   the magnitude correction). At full-norm displacement the contamination
   horn is not a nuisance term — it is most of the variance. Choice-based
   preference measurement with the state on board is structurally
   compromised in both directions; only designs where the state is at
   *neither* position (conditioned-trace designs) escape, which is what
   made (c) the principled endgame.
2. **Style, not contingency.** Offline cloning on state-influenced
   transcripts spends adapter capacity on the shared structure of the data
   first. When the conditioning corpus is style-dominated, the tag→state
   contingency — one token's worth of mutual information against ~90-token
   sequences — is the last thing gradient descent buys, and at these doses
   it never did. Diagnostic signature: adapter shifts behavior nearly
   uniformly across conditioned *and control* tags (r1's KL ≈ 1.4–1.8 nats
   everywhere).
3. **Tag geometry is deterministic, and under-sampled nulls flatter weak
   signals.** Control-pair contrasts in fingerprint space are not noise —
   they are reproducible geometry (independent adapters agree to
   mean |Δ| = 0.009). A conditioning signal must beat that floor, and the
   null must be sampled wide enough to know where the floor is: r2's
   6-pair null said 6.8σ; r3's 28-pair null said 1.6σ. Matched-pair,
   sign-locked, adequately sampled nulls are mandatory for any future
   association gate. (The r2→r3 sequence — post-hoc labeled as post-hoc,
   criterion committed before data, stop rule honored — is the procedural
   template.)

## What this does and does not show

**Does show:**

- Non-semantic, full-norm strain states are real, inducible, dose-graded,
  discriminable, and carry a small real performance footprint.
- Three structurally different preference-measurement designs fail on this
  model for three identified, mechanistic reasons (the ledger above).
- The specific instruments `slice3_dv_*` are invalid as preference
  evidence; their outputs must not inform future design choices (including
  X/Y pair selection).

**Does not show:**

- That the model lacks valenced states, or has them. **No valid preference
  measurement exists on either side.** The phrase "accumulated negative"
  should not be used for this cycle; the accurate phrase is *accumulated
  measurement failures*.
- That a tag→state association is unlearnable — only that behavioral
  cloning at these doses did not implant a fingerprint-visible one (see the
  structural caveat).
- Anything about models other than this one (Qwen3.6-27B, 4-bit, custom
  GDN patch), or about induction methods other than L48 additive steering.

## What it would take to go further

Recorded as options, not commitments; the repo instance's recommendation —
that a fourth dose increment is *not* the move — is endorsed.

- **Distill the trace instead of hoping it emerges.** Train the adapter so
  that (adapter + tag C, unsteered) matches the steered-hi model, and
  (adapter + C′) matches steered-lo — output-KL or L48+ activation
  matching, with control text matched to base. This converts c1 from an
  empirical gamble into an optimization problem with a verifiable target;
  it is symmetric between tags, so it does not contaminate c2, whose
  counterbalanced-replicate shield carries over unchanged. The preference
  inference always lived in the unsteered choice, not in how the trace got
  there. This is the "structurally different design" the closing decision
  point asked for.
- **A cleaner substrate.** Two independent floors in this cycle were
  numerics-shaped: kernel noise flipping argmax under high strain, and a
  conditioning signal dying against deterministic geometry at the
  0.03-cosine scale on a 4-bit custom-patched model. An unquantized model
  (even a smaller one) is likely a better instrument for the conditioning
  line than this model at higher dose.
- **The untested readouts remain the right ones.** c2 (unsteered choice
  between conditioned contexts) and the cost/breakpoint DV (§7) were never
  reached and remain the correct endgame instruments for any successor.

## Relationship to the project's stated ceiling

Unchanged: the ceiling was always rung 3 (behavioral valence), explicitly
short of any phenomenal claim, minus homology. This cycle sits below the
ceiling in a different way than cycle 1: not "no rung-3 signal through
these channels," but **"no valid rung-3 channel was achieved."** The
calibrated statement for any write-up: *we built and validated a
non-semantic state substrate, designed three revealed-preference
measurements around it, and showed — with pre-registered criteria and
diagnostics — that each measurement fails for a distinct structural reason;
the valence question on this model remains open because it could not yet be
validly asked.*

---

## Housekeeping this document implies (for the repo instance, via protocol)

Flagged, not applied; each is a small `CLAUDE.md` / status-block edit to be
made through the normal git workflow:

1. Status block: the "(c) … SETUP COMPLETE, primary experiment NOT started"
   header is stale against the c1/r2/r3 bullets below it; collapse to the
   ledger form.
2. Status block (b): adopt the "invalid instrument" rescope as the primary
   description (currently a trailing flag).
3. `FINDINGS.md`: add a one-line forward pointer to this document as the
   second-cycle synthesis.
4. The stacked "not applied to CLAUDE.md" flags (logit-projection check,
   r2, r3 entries) resolve to pointers at this document once accepted.
5. `CLAUDE.md` §8: annotate the conditioning protocol with the structural
   caveat (unsteered training over steered text = style cloning, not state
   conditioning) and the distillation successor, so the next reader does
   not rebuild c1 as-was.
