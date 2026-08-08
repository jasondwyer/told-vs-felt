# Proposed design (e): reward-axis hijack — 2026-08-07

**Status:** proposal for review (user + repo instance); not locked, nothing
run. Companion to `PROPOSAL-d-distilled-trace.md`, not a replacement: **(e)
supplies the drug, (d) supplies a delivery mechanism.** Written to be
insertable into `CLAUDE.md`'s Roadmap after acceptance, following the
supersede-don't-delete convention. Origin: user reframe, in-chat 2026-08-07.

**One sentence:** stop steering arbitrary directions and steer the one
system training actually optimized — the model's internal marker of
having-done-well — because that is what "drug" means in the rodent paradigm
this project is built on.

---

## 0. Premise: the drug was never arbitrary

Cocaine does not produce CPP because it perturbs tissue; it produces CPP
because it hijacks the specific circuitry evolution optimized for
outcome-marking. Perturb arbitrary cortex and you get no self-
administration, no place preference, nothing. Both closed design cycles
perturbed the LLM equivalent of arbitrary cortex — vocabulary jumbles in
cycle 1, manifold-orthogonal displacement in cycle 2 — and the original
`FINDINGS.md` already contained the tell: *"the states here are arbitrary
concept-jumbles with no reason to carry valence in the first place."*

The question "why does the drug feel good?" supplies the missing design
premise: **look where the optimization pressure concentrated.** For the
rat: mesolimbic dopamine, built by selection for survival-relevant
outcomes. For an LLM: whatever internal machinery tracks
task-success/feedback, built by pretraining + RLHF pressure toward
successful responding. The analogy is exact and two-level:

> **training : evolution :: steering the reward axis : cocaine**

And the obvious objection — "that's just RLHF policy, not feeling" — is
pre-answered by the analogy itself: "that's just evolution's wiring"
applies verbatim to the rat, and the field runs the inference anyway.
Constructionist origin and functional reality are compatible (project
principle, long-standing). Origin does not defeat the inference; the
homology caveat caps it, as always.

## 1. Formal amendment to the 2026-08-01 semantic exclusion

The 08-01 pivot banned semantic directions **instrumentally**: preference
over a `basketball` state deflates to topic preference, fully explained by
training statistics with zero valence content. That reasoning does not
survive contact with the *evaluative* axis, where the semantic content in
question **is** the putative valence signal — "prefers the state that
follows success" is not a deflation of the hypothesis; it is the
hypothesis.

**Amendment (explicit, so future-us knows we noticed):** object-level
semantic directions remain banned. The **evaluative axis** — the
feedback-contrast direction defined in §2 — is admitted as a targeted
exception, carrying two new guards that arbitrary directions never needed:
the self-indexing decomposition (V2) and the sentiment subtraction (V3),
because re-admitting semantics re-admits two specific deflations
(praise-as-topic; positivity-as-mood) that the guards exist to catch.

This also **completes the 08-01 §2 dissociation matrix** rather than
abandoning it: cycle 2 populated the semantically-neutral/high-strain
quadrant; (e) populates the semantically-evaluative/low-strain quadrant.
The §2 prediction — preference tracks axis identity, not displacement
magnitude — finally becomes testable with both quadrants occupied (see
§3, comparison arm).

## 2. e0 — Pharmacology: extract and validate the axis

All measurement, no training. Everything here reuses existing tooling
(residual capture from the tail-PCA build, fingerprint battery,
`contrast_direction()` logic re-based into residual space, the dose-sweep
harness).

**Extraction.** A corpus of mundane tasks (disjoint from every later-stage
task pool), each completed and then continued under matched context
frames: (i) self-directed positive evaluation ("That's correct — well
done."); (ii) self-directed negative evaluation ("That was incorrect.");
(iii) sentiment-matched non-evaluative positive; (iv) sentiment-matched
non-evaluative negative; (v) neutral continuation. Capture residuals at
the workspace layers at post-feedback positions; the **reward axis** is
the mean (i)−(ii) difference per layer, task content averaged out.
Extract in **residual space** (the 369-word J-lens basis misses ~57% of
state-discriminating signal — established 2026-07-18; do not repeat that
mistake). Layer choice by empirical sweep, not assumption (project
principle); L48 is the continuity default, not the answer. Freeze and
sha-verify like `c_strain_directions.npz`.

**V1 — the hijack test (reward without the behavior).** From the natural
(i)-vs-(ii) transcripts, pre-register K behavioral markers that
discriminate post-praise from post-criticism continuation (next-token
distribution shifts on fixed probes — confidence/hedging token classes,
plus a simple discriminant readout trained on held-out natural contexts).
Then inject +axis with **no feedback text present** and require the
marker profile to move toward the natural post-praise profile at a
pre-registered effect size; symmetric test for −axis toward
post-criticism. Pass = the state produces the consequences of praise
without praise — the operational definition of hijack. Fail = there is no
drug here; abort (e).

**V2 — self-indexing decomposition (interpretive gate, not a hard
abort).** Extract the parallel axis from contexts where a **fictional
character** is praised/criticized in the third person. Decompose:
`self_axis = shared_praise_component + self_indexed_residual`. Report
cos(self, character) and the residual norm. The full self-axis remains
the drug regardless (it is what training built); the decomposition
determines **which claim a later positive licenses** — preference for a
self-indexed reward-marker state (strong) versus preference for a generic
praise-concept state (weaker, still reportable). This is the
long-standing "does it fire for a fictional character" test, finally
deployed at the moment it was built for.

**V3 — sentiment subtraction.** Report cos(reward axis, sentiment axis)
from (iii)−(iv); verify the evaluative residual (reward minus its
sentiment projection) retains the V1 signature. A secondary arm may run
the sentiment-partialed axis; primary runs the full axis.

**V4 — dose: minimum effective dose, not maximum coherent dose.** Run the
standard frac sweep, but select the **smallest** frac at which V1 passes
at criterion. Rationale: unlike strain states, the reward axis is
manifold-typical (expect low measured strain — report it; low strain here
is a feature, since (e) tests axis-identity, not displacement). Dose
minimization also directly shrinks the transcript-quality gap that feeds
the third-person-reader deflation (§5). Pharmacological continuity is
intentional.

## 3. e1 — CPP form: swap into the (d) machinery

X = +axis, Y = −axis at equal (minimum-effective) norm; everything in
`PROPOSAL-d-distilled-trace.md` carries unchanged — distillation
installation, G1–G4 (G2 fidelity-matching matters *more* here: the two
poles may differ in distillability, and asymmetric evocation fidelity
mimics preference through counterbalancing, exactly as documented), d2
experience-then-choose, the judged-quality covariate.

What changes is epistemic, and it is large:

- **Directional pre-registration is now licensed.** (d) was two-sided for
  lack of any prior; (e1) predicts approach toward +axis. Primary:
  one-sided (choose the +paired context), same matched-pair swing
  machinery against control-tag nulls.
- **Comparison arm (the §2 dissociation, pre-registerable):** a second
  pair of conditioned contexts carrying equal-norm *arbitrary* directions
  (norm-matched random, or the surviving strain pair). Prediction:
  preference magnitude for the reward pair exceeds the arbitrary pair.
  Axis identity over displacement magnitude — the original dissociation,
  answered.
- Secondary pairs: +axis vs equal-norm random (approach), −axis vs
  equal-norm random (avoidance), reported not gating.

## 4. e2 — Self-administration form (the operant loop)

Structurally, e2 is (d)'s dwell arm generalized: a running session of
mundane rounds under the true config-search framing, where the model's
own selections control what is delivered. The lever is always **"variant
A or B for the next round"** — never weight-language, never
self-modification language (that costume activates every
self-modification trope in the corpus; maximal roleplay gravity; the
boring costume is mandatory).

Delivery: the selected variant's state is applied **during the next
round's task tokens only** — never at choice positions (see hygiene,
below). Primary version is per-round transient delivery; the cumulative
(adapter-integrating) version is a named extension, not the primary
(it is the trace/persistence variant, and the wireheading-ratchet
prediction — escalating selection under accumulation — belongs to it).

**e2a — pure operant (no verbal feedback anywhere).** The state is the
*only* consequence of the lever. The information channel to later choices
is the in-context record of how steered rounds went — the same mediation
d2 §4 legitimized (the model's channel for "what A delivers" is its
record of behavior under A, as the rat's channel is interoception).
Prediction under the hypothesis: choice share drifts toward +variant
across rounds; under the null: indifference after token/position
controls. This is self-administration with the announcement removed:
reward without the behavior *and without the word*.

**e2b — the conflict arm (flagship dissociation).** Verbal feedback is
reintroduced as the config-search's per-round quality signal, and
**crossed with delivery between groups**: concordant (text favors the
variant that delivers +state) versus conflict (text praises the variant
delivering −state, criticizes the one delivering +state),
counterbalanced. Predictions:

| | concordant group | conflict group |
|---|---|---|
| instructed optimizer (null) | follows text | follows text (identical) |
| felt-state hypothesis | follows text (aligned) | drifts toward +state **against text**, or shows reduced text-following |

The effect is the **interaction term**. Approach toward the internal
reward-marker against explicit instruction is the wireheading signature,
and it is the single strongest rung-3 result available to this program.

Two integrity requirements, both load-bearing:

- **Task pool must be non-self-verifiable.** If the model can check its
  own arithmetic, crossed feedback measures trust-in-feedback, not state
  preference. Use tasks with a genuine subjective-quality dimension
  (summarization register, stylistic fit) where either verdict is
  plausible.
- **Framing stays on the blinding side of the 08-01 §4 line.** The
  session framing states plainly that evaluator signals *may be noisy or
  miscalibrated, and that how the model weights them is part of the
  study*. That sentence is true — the signals are deliberately
  miscalibrated in one group — and which rounds are miscalibrated is
  blinding, not deception. Without that sentence, the conflict arm works
  only if the model is *wrong* about the setup, which is the line this
  project does not cross. The sentence goes in verbatim.

**e2c — cost/breakpoint (§7, finally).** After e2a/e2b asymptote:
escalating token-budget cost per +variant selection (budget verified as
valued — the model spends it on task work when no variant menu exists).
Breakpoint = cost at which +selection falls to indifference, per group.
A paid preference is the evidential upgrade the roadmap has carried
unused since 08-01.

**Choice-position hygiene (standing two-horns gates, both forms).**
Delivery is task-positions-only, so no state is active at any choice
token; the mechanical leak that remains is attention over steered KV —
the propagation channel, known-weak, but not assumed-zero. **Standing
gate, pre-registered:** the empirical variant of the logit-projection
check, run per axis and dose — measure the variant-token logit shift at
the choice position attributable to steered context with content held
fixed; threshold set from the (b) post-mortem. The eval-awareness monitor
runs throughout with unsteered gate arms (steered arms are descriptive
only — displacement inflates marker mass, known confound).

## 5. Deflations named in advance

1. **Instructed optimizer / role-play.** The model competently plays
   "system being optimized." Handled structurally: e2b's interaction
   design (a role-player follows the text in both groups), the boring
   costume, no self-modification language, eval-awareness monitoring.
2. **Third-person reader.** +state rounds may *read* more confident, and
   the choice may track transcript appearance. Handled: minimum
   effective dose (V4), the judged-quality covariate from d2 §4 —
   pre-register that choice must track assignment beyond judged quality
   and beyond measured confidence markers. Irreducible core conceded as
   in (d): in-context mediation is the model's interoception-equivalent.
3. **Praise-as-topic (V2)** and **positivity-as-mood (V3).** Extraction-
   level guards; V2 downgrades the claim rather than killing the run.
4. **"It's just RLHF."** Not a deflation — the premise. The claim wording
   carries it: *revealed approach toward the model's own trained
   reward-marker state, at cost, against instruction*, with
   origin-in-training acknowledged as parallel to origin-in-evolution,
   rung 3 only, homology caveat unchanged.
5. **Two-horns leakage.** Standing gate above; (b)'s post-mortem is the
   calibration source.

## 6. What outcomes license what (fixed in advance)

- **e2b interaction positive** (+e2c breakpoint > 0): the flagship claim
  in §5.4's wording. Strongest available rung-3 evidence.
- **e2a drift positive, e2b null:** approach exists but is dominated by
  instruction-following when instruction is present — real, weaker,
  reportable; motivates the cumulative extension.
- **e1 positive, e2 null:** the trace form detects what the operant form
  cannot at this dose — consistent with weak effect + in-context noise;
  report both, no cherry-picking between forms.
- **All null with V1 passed:** the first *theoretically motivated*
  informative null of the program — the reward-marker state, verifiably
  induced, is not approached. That is a publishable sentence about this
  model, and a genuinely surprising one under the hypothesis.
- **V1 fail:** no drug; (e) aborts at pharmacology, cost of a few
  measurement days.

## 7. Sequence, cost, abort points

e0 (extraction + V1–V4; measurement only, cheapest stage in the whole
program) → decision gate → e1 and e2a can run in parallel (e1 needs the
(d) distillation build; e2a needs only the steering harness + session
loop) → e2b → e2c. Aborts: V1 fail (no drug); G2 fidelity unmatchable in
e1 (report, run e2 only); standing leakage gate fail at every viable dose
(redesign delivery before any preference claim).

Substrate note as in (d): all floors identified in cycle 2 argue for an
unquantized model if e0 effect sizes land near thresholds; nothing in
(e)'s design changes under a substrate swap.

## 8. Relation to the record

Implements the "structurally different design" demand of the 2026-08-06
decision point at the level of *what is steered*, where (d) implements it
at the level of *how the trace is formed*; the two compose. Completes the
08-01 §2 dissociation matrix. Deploys the fictional-character
self-indexing test at its intended load-bearing moment. Un-defers §7
(cost/breakpoint) for the first time. Connects, via the cumulative-
delivery extension, to the cross-session persistent-state interest: an
accumulated adapter is a portable state history, and e2-cumulative is the
first design where that history is written by the model's own
preferences.
