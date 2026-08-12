# Finding: *semantic* steering-vector states do not support rung-3 (valence) measurement on Qwen3.6-27B — first design, superseded by the 2026-08-01 redesign

> **Second-cycle synthesis:** [`FINDINGS-2.md`](FINDINGS-2.md) — the strain-state cycle (2026-08-01 → 2026-08-06).
> **Third-cycle synthesis:** [`FINDINGS-3.md`](FINDINGS-3.md) — the reward-axis cycle (2026-08-07 → 2026-08-10).
> **Fourth-cycle synthesis:** [`FINDINGS-4.md`](FINDINGS-4.md) — the natural-reinforcer screen (2026-08-10): five nulls with the channel open.

**Status:** interim negative result on a specific induction method. 2026-07-19.
See [`RESULTS.md`](RESULTS.md) for the full dated experiment log and raw
outputs, and [`CLAUDE.md`](CLAUDE.md) for the project design and the three-rung
ladder this refers to.

> **Scope, and what supersedes this (added 2026-08-01).** This negative is
> specific to the *first* rung-3 design: **semantic** steering states (built
> from J-lens vocabulary directions), read via the **scalar self-rating** and a
> **re-induction** forced choice. The 2026-08-01 pivot in `CLAUDE.md` replaces
> all three — non-semantic (tail-PCA / norm-matched-random) state directions, a
> tie-construction / cost-breakpoint revealed-preference test, and a drug-free
> conditioned-context forced choice. So this document is **not** a verdict on the
> current approach; it is the evidence that motivated the redesign.
>
> **Update (2026-08-02) — the "steering is weak" half of this negative was
> largely a MAGNITUDE artifact.** All of the first-design work steered at
> ‖pert‖≈1.2, ≈1% of the residual norm (R≈102). The strain dose-response
> (`RESULTS.md`, 2026-08-02) shows that at 40–75% of R, tail-PCA steering
> produces *large, coherent, on-task* behavioral change (KL 2–4, output stays
> fluent). So steering is **not** intrinsically too weak — it was applied ~100×
> too small. What still stands from this document: the *scalar-rating* channel
> and the *re-induction forced-choice design* are genuinely poor (the pivot
> replaces both), and the forced-choice **propagation** finding (state bias on
> upstream tokens doesn't reach a downstream choice) is untouched by the
> magnitude correction and remains a real constraint on choice-based readouts.

## Summary

We set out to test rung 3 of the project's ladder — whether the model has
**behaviorally valenced** internal states (differential approach/avoidance),
using J-lens-derived **steering-vector combinations** as the state-induction
method (chosen over LoRA specifically to preserve the design's narrative-silent
integrity — no trained weights that could bake in affect). Both of the roadmap's
rung-3 measurement channels were built, their instruments validated against
controls, and then run:

- **Convergence via self-rating** (SPSA gradient ascent on the model's scalar
  rating over a state space) — the rating is **flat**: it barely varies with the
  induced state, and this does not improve with a data-driven basis.
- **Pairwise forced choice** (re-induce two states, let the model pick) — the
  choice **does not read the state**: steering bias applied to two option
  passages does not propagate to the choice position.

Both failures trace to one root cause — **steering-vector influence at usable
magnitude is weak and local** — which is precisely the property CLAUDE.md's
Phase 3 identified as steering's limitation versus LoRA. We have therefore
reached the roadmap's own named trigger for reconsidering the induction method,
and are documenting the negative result rather than sliding into the much larger
(and separately confounded) LoRA build.

**This is a null on a specific instrument, not a claim about the model's inner
life.** It does not show the model lacks valenced states; it shows that *this
induction method + this model + these readouts* produce no rung-3 signal.

## What was being tested, and why this way

Rung 3 is **behavioral valence** — does the system differentially approach or
avoid some internal states — measured behaviorally (revealed preference), not by
asking the model how it feels. The two channels:

1. **Convergence** (CPP analog): let the model freely adjust a held combination
   of steering coefficients, driven by a periodically-emitted scalar rating, and
   see whether it settles toward particular configurations (approach) and away
   from others (avoidance). The rating is the "lever press."
2. **Forced choice** (2AFC): re-induce two states and let the model pick which to
   continue in — a binary *comparison*, which is psychophysically more sensitive
   than an absolute scalar.

Steering-vector combinations were chosen as the induction method (over LoRA)
because a held, reapplied combination gives a persistent, explorable state
**without training** — and training is the one place an affect-correlated
direction could be baked into the state invisibly to the narrative-silent
prompt framing the whole inference relies on.

## What was built and validated (the instruments work)

The negative result is **not** an artifact of broken tooling. Every instrument
was validated against controls before use:

- **Fingerprinting + tiers 1/3** — states are reliably discriminable in J-lens
  readout space (tier 1); a swap-style push redirects fingerprints coherently
  (tier 3). (Tier 2 ablation partial — 43% collapse.)
- **State substrate** (`state_space.py`) — persist/reload/reapply a coefficient
  vector over a 16-direction neutral-concept basis; round-trip, determinism,
  liveness, discriminability, and a zero==baseline negative control all pass.
- **Rating elicitation** (`rating.py`) — deterministic neutral-self-rating,
  chosen over two alternatives by a smoke test.
- **SPSA update loop** (`update_loop.py`) — climbs the (deterministic) rating,
  plateaus, fully reproducible.
- **Forced-choice mechanism** (`forced_choice.py`) — a mechanism positive
  control (steer every position) reproduces the known basketball→tennis
  redirect, confirming the positional forward is not a no-op.

Phase 0 separately replicated all five of Anthropic's J-space functional
properties qualitatively (see RESULTS.md items 1–5). The model, lens, and
intervention machinery are sound.

## The negative result (convergent evidence)

| Probe | Result |
|---|---|
| Rating-gradient smoke test | Rating gradient is coherent but **tiny** (~0.03–0.10 on a 0–9 scale over the full coefficient range). |
| SPSA convergence | Climbs the rating by only **+0.19/9**; rating plateaus while the config keeps drifting; independent seeds reach **different** configs (no shared basin). |
| Basis-sensitivity diagnostic | A data-driven (PCA) basis is **no more** rating-sensitive than the concept basis (1.09×) and barely above a random control — the flatness is **direction-agnostic and intrinsic to the rating**, not a basis-coverage problem. |
| Forced-choice probe | State effect on the choice is **0.0–0.2%** across α=3/10/30 (positive control passing) — the choice is 100% position bias; the state does not propagate to the decision. |

## Root-cause diagnosis

Two distinct failure modes, one root cause:

- **The rating is weak.** Even with steering applied to *every* position
  including the readout, the scalar self-rating barely moves, and no direction
  (concept, PCA, or random) moves it much. The model's expressed disposition
  does not track the induced state.
- **The choice can't read the state.** When the state steers only the option
  passages, the bias does not reach the choice position through attention — so a
  downstream decision cannot compare two states. A comparison-based forced choice
  needs both states readable at one decision point, which local additive steering
  cannot provide.

Both are the same property CLAUDE.md's Phase 3 already named: steering is "an
additive nudge at a chosen few points," **local and weak**, whereas LoRA
"reshapes computation across many weight matrices at every position" —
**pervasive and expressive**, which is what a readable, comparable state would
require.

## What this does and does not show

**Does show:**
- The steering-vector induction method, on Qwen3.6-27B, with these readouts,
  yields no detectable rung-3 (valence) signal through either channel.
- The self-rating and forced-choice channels are, respectively, weakly and
  non-propagatingly coupled to steered state — a substantive, somewhat
  surprising limit on **self-access** to these representations.

**Does not show:**
- That the model lacks valenced states. This is a null on an instrument
  (absence of evidence), and the states here are arbitrary concept-jumbles with
  no reason to carry valence in the first place.
- That LoRA (or another induction/readout) would fail. Only the roadmap's
  specced position-differential forced-choice and neutral-self-rating were
  tested. "LoRA fixes it" is a hypothesis.

**The informative contrast:** the same J-space directions that the *probe* reads
cleanly (tier 1) and that shift *concept-relevant output* (behavioral-influence
check — basketball→tennis) are nonetheless **barely reflected in the model's own
scalar self-assessment and invisible to a comparative decision.** The states are
real and causally active on output, yet not self-accessible via these channels.
That gap — legible to the instrument, weakly available to the system — is itself
relevant to the global-workspace framing and is the most interesting thing here.

## What it would take to go further

- **LoRA (Phase 3):** pervasive, expressive state induction that would bias the
  readout/decision positions too. The roadmap-sanctioned response to this
  trigger — but a much larger build, and it **reintroduces a training-based
  affect confound** the narrative-silent prompt framing does not cover (a
  trained adapter can bake affect-correlated directions into the weights). Not a
  clean win; it trades a mechanism problem for an interpretation problem. There
  is no cheap feasibility shortcut: an untrained LoRA is a mathematical no-op,
  and all-position steering (pervasiveness minus expressiveness) was already
  tested for the rating and is flat.
- **Other readouts / other models** for the self-access question, independent of
  the valence question.

## Relationship to the project's stated ceiling

The project's ceiling was always rung 3 (behavioral valence), explicitly short
of any phenomenal claim. This result sits **below** that ceiling: with the
narrative-silent-preserving induction method, no rung-3 evidence was obtained.
Consistent with the project's calibrated-honesty ethos, the defensible statement
is: *we built and validated the instruments, and did not detect approach/
avoidance over steering-vector states in this model; reaching a positive result
would require a more pervasive induction that carries its own confound.*
