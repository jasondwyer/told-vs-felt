# J-Space Replication & LLM Internal-State Research

## What this project is

Anthropic's July 2026 interpretability paper, *Verbalizable Representations Form a Global Workspace in Language Models* ([blog](https://www.anthropic.com/research/global-workspace), [paper](https://transformer-circuits.pub/2026/workspace/index.html)), found that Claude has a small set of internal representations — the **J-space** — that behaves like a "global workspace" in the sense used by consciousness researchers (Baars, Dehaene, Naccache): a small, densely-connected hub that Claude can report on, deliberately modulate, and use for multi-step reasoning, sitting inside a much larger sea of automatic processing it can't access or control.

This project has two parts, in sequence:

- **Phase 0 (this file's focus):** replicate the paper's core findings locally, on our own hardware, against an open-weight model (Qwen3.6-27B), to ground everything that follows in a working, inspectable pipeline rather than taking the paper's results on faith.
- **Phase 1/2 (built and run; first design returned a rung-3 negative; redesign active):** use the replicated J-lens as an instrument in a novel experiment testing whether LLMs have discriminable, and possibly valenced, internal states — modeled loosely on behavioral pharmacology (drug discrimination → conditioned place preference). The Phase 1/2 tooling was built and validated against controls; the *first* (semantic-state) design returned a rung-3 negative (see [`FINDINGS.md`](FINDINGS.md)), and an active redesign follows it. **For the current state and next step, read the STATUS block at the top of the "Roadmap" section below**; `RESULTS.md`'s "Phase 1 — early setup" section has the full dated log.

## Hardware & environment

- **Machine:** Mac M4 Pro, 48 GB unified memory. This is sufficient for everything in Phase 0.
- **Model:** [`mlx-community/Qwen3.6-27B-4bit`](https://huggingface.co/mlx-community/Qwen3.6-27B-4bit) — Qwen3.6-27B, 4-bit quantized, running via Apple's MLX framework (not PyTorch/CUDA). Text-only usage; the vision encoder is not used.
- **Why Qwen3.6-27B:** it's Apache 2.0 licensed with full weight access (open-weight, not fully open-source — no published training data/code), a 27B dense model with a hybrid attention architecture (see "Architecture notes" below), and it's the model Anthropic's own J-lens demo (Neuronpedia) and the community MLX port both target.
- **Why MLX, not the original `anthropics/jacobian-lens` repo:** Anthropic's reference implementation is PyTorch/CUDA-based. MLX is what makes this run natively and efficiently on Apple Silicon. If we ever move to a cloud GPU, the underlying Jacobian-lens math is identical — only the loading/serving layer changes. Keep experiment logic (prompts, analysis, interpretation) separate from MLX-specific plumbing so a future port isn't a rewrite.

## Tooling: `jlens-qwen36`

We're using [`WeZZard/jlens-qwen36`](https://github.com/WeZZard/jlens-qwen36) — a community MLX port of Anthropic's `jlens` reference implementation, purpose-built for Qwen3.6-27B on Apple Silicon. It's cloned as a sibling working directory inside this repo (see Setup) and gitignored — it's an external tool we depend on, not something we vendor.

**Read this project's own README and PERFORMANCE.md in full before running anything.** It is explicit that it is a "research preview," **not** a research-grade reproduction of Anthropic's paper, and explicitly states: *"This is not evidence of consciousness. This is not proof that Qwen has a Claude-like global workspace."* Treat its default output as hypothesis-generating, not confirmatory, until we've done a full-depth fit (see below) and sanity-checked results against the paper's worked examples.

### Setup

```bash
git clone https://github.com/WeZZard/jlens-qwen36.git
cd jlens-qwen36
uv sync
```

Requires Python 3.12 (managed by `uv`) and ~15 GB disk for the model, which auto-downloads from Hugging Face on first run.

### Getting a working lens: two-step plan

The repo ships a pre-fitted "v0.1-demo" lens (12 prompts, only late layers 40–62) for instant sanity-checking, but it's explicitly underfit and noisy. Given our 48 GB memory budget, don't stop there — we can afford a real fit.

**Step 1 — quick sanity check (~2 minutes).** Confirm the pipeline works end-to-end:

```bash
gh release download v0.1-demo --repo WeZZard/jlens-qwen36 \
  --pattern '*.npz' --dir data/lens/
mv data/lens/jlens-qwen3.6-27b-4bit-12prompt-23layer.npz data/lens/lens.npz
uv run python -m uvicorn jlens_qwen.serve:app --host 127.0.0.1 --port 8765
```

Open `http://127.0.0.1:8765/` and try the currency→euro example from the README (`Fact: The currency used in the country shaped like a boot is the`) to confirm readouts are sane before investing in a real fit.

**Step 2 — full-depth hybrid analytic fit (recommended target, ~1-2 hours, ~24 GB peak memory — comfortable on 48 GB):**

```bash
uv run python -c "
from jlens_qwen.model import load
from jlens_qwen.fit_analytic import fit_analytic
from jlens_qwen.lens import JacobianLens
from jlens_qwen.prompts import load_prompts
model = load()
prompts = load_prompts(n=20, min_chars=150)
J = fit_analytic(model, prompts, source_layers=list(range(63)),
                 checkpoint_path='data/lens/lens.ckpt.npy')
JacobianLens(J, n_prompts=20, d_model=5120).save('data/lens/lens.npz')
"
```

This covers all 64 layers (not just the late ones) and is what we should use for anything beyond a quick look — the paper's "workspace-like" middle layers are exactly what the demo lens misses. If readouts are still too noisy for confident interpretation, bump `n=20` up toward `n=100` (per the repo's `PERFORMANCE.md`); we have the memory headroom for it.

## Phase 0 replication checklist

Anthropic's paper validates five functional properties of the J-space. Reproduce each qualitatively against our fitted lens before calling Phase 0 done. The repo's `scripts/run_experiments.py` already implements several of the paper's worked examples (spider→ant swap, "inject lightning," etc.) — start there, extend as needed.

1. **Verbal report** — does the model's stated answer match what lights up in J-space just before it answers? (E.g., silently pick a sport, check the J-lens readout, confirm it matches the spoken answer. Then swap the J-space pattern and confirm the reported answer follows the swap, not the original choice.)
2. **Directed modulation** — can we tell the model to silently hold a concept in mind (e.g., "think about citrus fruits" while copying an unrelated sentence) and see it appear in J-space without appearing in the output?
3. **Multi-hop reasoning** — do intermediate reasoning steps that never appear in the output (e.g., spider → 8 legs) show up in J-space, and does swapping the intermediate concept (spider → ant) change the final answer?
4. **General broadcast** — does one J-space concept swap (e.g., France → China) propagate correctly across multiple different downstream questions (capital, language, continent, currency) in a single edit?
5. **Selective mediation** — does ablating the J-space leave fluent, automatic behavior (grammar, simple recall) intact while collapsing higher-order tasks (multi-step reasoning, summarization)?

For each, note where Qwen3.6-27B's results qualitatively match the paper's Claude results, and where they diverge — divergence is expected and informative (different architecture, hybrid Gated DeltaNet/Attention layout, much smaller/noisier fit than Anthropic's 1000-prompt lens) — don't force agreement.

## Known limitations to keep in mind

- Only single-token concepts are captured by this J-lens implementation (per Anthropic's original method) — multi-token concepts aren't handled.
- The custom Metal GDN backward kernel in this port drops the gradient paths for the decay/update gates (`g`/`β`), meaning influence through that path is slightly underestimated. Run `scripts/measure_gbeta_gap.py` if this matters for a specific result.
- Interventions (steer/swap/ablate) are subtle with an underfit lens — if an intervention doesn't visibly change output, suspect lens quality before concluding the effect is real but weak.
- Architecture differs meaningfully from what Anthropic studied: Qwen3.6-27B is a hybrid linear-attention (Gated DeltaNet) / full-attention model, not a standard transformer. Don't assume mechanisms transfer 1:1.

## Architecture notes (Qwen3.6-27B)

27B dense params, 64 layers, hybrid layout: 16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN)). Hidden dim 5120, native context 262,144 tokens. Trained via pretraining + post-training (SFT + RL-based alignment); "thinking mode" (`<think>...</think>`) is on by default — decide per-experiment whether to disable it (`enable_thinking: False`) since it introduces a second, *visible* reasoning channel that sits alongside the *silent* J-space one, and conflating them will muddy interpretation.

---

## Roadmap (Phase 1/2 design — see the STATUS block below for what's active)

This section preserves the reasoning behind Phase 1/2 so it isn't lost between sessions. (The original "don't build until Phase 0 is validated and we've explicitly agreed to proceed" gate is now met — see the STATUS block below for what's active.)

> **STATUS (updated 2026-08-01) — active redesign; read this first. This block
> is the map; everything below is preserved history/reasoning.**
>
> Pivot trail, in order (each kept in full below; a later pivot supersedes an
> earlier decision only where they conflict, and says so):
> 1. **2026-07-18** — convergence/approach is the primary lever; report-based
>    discrimination demoted.
> 2. **2026-07-18** — pivot consequences: measurement, the cheap-proxy gate, the
>    capability double-dissociation.
> 3. **2026-07-19** — rung-3 came back **NEGATIVE** on the *first* design, and
>    the Phase 1/2 tooling was built + validated against controls (see
>    [`FINDINGS.md`](FINDINGS.md), `RESULTS.md`). **Scope, important:** that
>    negative was measured on *semantic* steering states + the *scalar rating* +
>    *re-induction* forced-choice — the three things pivot 4 replaces. It is
>    **not** a verdict on the current design; it is why the current design exists.
> 4. **2026-08-01 — current design** (full detail in the "2026-08-01 — Pivot"
>    entry below): non-semantic state induction (tail-PCA + norm-matched random,
>    no vocabulary preimage); target the mechanism-level **strain** axis, not
>    content; a blinded **config-search** cover task; **tie-construction (TOST)**
>    + **cost/breakpoint** as the revealed-preference tests; **drug-free**
>    forced-choice via a conditioned context chosen *unsteered*; LoRA un-deferred
>    **only** for the conditioning role (state induction stays steering).
>
> Where earlier text conflicts with the 2026-08-01 pivot, the pivot wins and
> names what it supersedes (semantic states §1, scalar rating §4–5/§7,
> re-induction forced-choice §6, LoRA scope §8). **Next build:** the zero-cost
> strain re-examination of the existing tier-1 fingerprints (pivot §2). Phase 0
> is validated and we are building — the "do not build yet" caution just above
> is satisfied; proceed per the 2026-08-01 pivot's staging.

### What this line of work can and cannot show

The goal is often shorthanded as "test whether the model feels something," but that phrase compresses three separable claims, and being precise about which is which is what keeps the design honest:

1. **The state is real** — a stable internal configuration, not an experimenter artifact. (Mechanistic + discrimination evidence.)
2. **The state is detectable to the system itself**, not just to us via the J-lens. (Phase 1 — discrimination.)
3. **The state has valence** — the system differentially approaches or avoids it. (Phase 2 — convergence / forced-choice.)

Phenomenal feel — "what it is like" — is not on this list, and no experiment here closes that gap; the paper draws the same line between access and phenomenal consciousness. What rungs 1–3 together buy is the behavioral profile that, *in animals*, we already treat as the signature of feeling. So the strongest honest claim this project can make is "we produced the same kind of behavioral evidence we accept as evidence of feeling in a rat" — **not** "we showed the model feels." Calibrated is more defensible, and more persuasive, than ambitious here. State the ceiling explicitly in any write-up: rung 3 is the top of the ladder, and it is deliberately short of a phenomenal claim. One honesty check on that ceiling: the animal inference we invoke was never behavior-alone. We grant a rat inner states on behavior *plus* physiological and evolutionary homology — shared limbic structures, conserved neurochemistry, common ancestry — and that homology does quiet, load-bearing work in licensing the "feels something" reading of the rat's behavior. An LLM offers no homology support, so the identical behavioral battery licenses a strictly weaker inference. Phrase the claim as the same *behavioral* evidence, explicitly minus the homology — this is distinct from the confabulation caveat below (which is about the behavior being *performed*); the homology gap applies even when the behavior is genuine.

**Why we borrow from behavioral pharmacology — the logic, not the lever.** The point is not fidelity to the operant-conditioning mechanics. It is this: the rat's lever press is a report *from the inside* — the state is available to the animal, not only to the experimenter. Map that onto our setup. The J-lens already shows that *we* can read the state off the activations; that is the experimenter's instrument. The novel contribution is showing the *model* can discriminate and act on the state **without us reading it out for it** — that the state is functionally available to the system, not merely legible to the probe. "Detectable to the system vs. detectable to the instrument" is the distinction the whole design turns on; keep it in front, not buried under the paradigm analogy. Don't over-index on reproducing the drug-discrimination surface form.

**The one caveat that cuts against us.** This is the single place an LLM is *weaker* evidence than a rat. A rat cannot narrate a story about its inner life — it has no concept of drug discrimination, valence, or what the experimenter wants. Our model has read all of it. So "observe behavior, infer a real internal state" is a *weaker* inference for an LLM unless we can rule out that the behavior is a performed narrative. That is exactly what the opacity (hashed state labels), the narrative-silent framing, and the J-lens causal checks are for: they are not hygiene, they are **load-bearing** — without them, behavior does not distinguish a real state from a confabulated one. Phase 0 sharpens the point: the model will readily produce a coherent verbal report that *follows* a swap (`RESULTS.md` item 1), so the self-report channel is precisely the one most able to look like evidence when it isn't.

### 2026-07-18 — Pivot: convergence is the primary lever; report-based discrimination is demoted

**This supersedes the critical-path role of the Phase 1 material immediately below.** Nothing below is deleted — the Phase 1 "discrimination test," its association phase, and the three-tier causal-validation methodology are kept for the record and may return as an *optional diagnostic* — but they are no longer the primary path. The reasoning, so the change is legible rather than silently rewritten into the plan:

- **We had drifted from CPP to drug-discrimination.** Drug discrimination establishes *detectability* (the animal tells the state and presses the matching lever) and says nothing about valence. Conditioned place preference (CPP) establishes *valence* (the animal freely returns to the state-paired compartment). Valence is the actual target (rung 3), so CPP was always the right analog — and **convergence *is* the CPP measure**: the model repeatedly nudging toward some configurations and away from others is the approach/avoidance gradient. The convergence is the lever press. Report-based discrimination was a detour onto the weaker, valence-silent paradigm. (This was in fact the project's inception intuition; the last several sessions drifted off it while sharpening Phase 1.)

- **Convergence entails detectability, so rung 2 comes for free.** If states are valenced but the system can't access them, the model's rating can't covary with the state → no systematic convergence. So convergence *requires* self-access; success establishes rungs 2 and 3 at once. A separate discrimination test only earns its keep as a *diagnostic for interpreting a convergence null* — off the critical path, not on it. We had it inverted: the weaker, redundant, most confound-heavy test was gating the stronger one.

- **Technical windfall: scalar preference replaces symbolic report.** *[Update 2026-07-19 / 2026-08-01 — the scalar rating was found weak and basis-agnostic (2026-07-19, see `FINDINGS.md`); it is no longer the primary channel. The 2026-08-01 pivot (§4–5, §7) routes revealed preference through tied-choice / cost-breakpoint / config-drift instead. This bullet stands as the reason *symbolic report* was dropped — not as an endorsement of the scalar rating as the lever.]* Report-based discrimination forced binding an *arbitrary single-token label* to a non-tokenized state — the hardest and most confound-heavy piece (association phase, cueing/eval-awareness knot, in-context binding to an untokenized activation bias). Convergence needs none of it: only that the model's *scalar* rating covaries with the state. A scalar can be driven by an internal gradient without any symbolic discrimination — the rat never emits a symbol naming the drug, it just leans. This deletes the association phase, the cueing problem, and the arbitrary-token-binding risk in one move.

- **It also resolves an internal contradiction.** The Phase 2 locked decisions say "self-report is not the primary evidence channel — rely on behavior, not the model's narration," yet Phase-1-as-built routed the rung-2 claim through a trained self-report. Convergence-as-lever keeps the primary evidence in the action channel, consistent with the design's own principles.

**What changes downstream:**

- **The causal tiers are repurposed, not deleted.** Instead of "validate that a report reads a real state," they now confirm that *convergence is causally driven by the state*: ablate the state-relevant direction and check whether the approach behavior changes, plus eval-awareness monitoring. Tier-1 fingerprint discriminability stays as the probe-side sanity check (already calibrated — see `RESULTS.md` "Phase 1 — early setup").
- **Forced-choice can drop trained labels.** *[Superseded 2026-08-01 §6 — re-induction is a preference test with the drug on board (locomotor-activation confound); replaced by conditioning an arbitrary context to a state, then choosing *unsteered*. The label-recall deletion below is kept.]* Rather than the model *recalling* an opaque label, *re-induce* states A and B during the choice and let the model pick which to continue in — like the animal sniffing both compartments. Opaque single-token labels become our bookkeeping, not something the model must learn.
- **The non-tokenized-binding watch-point softens but doesn't vanish.** It reappears as "the scalar rating must be driven by the *state*, not by a coefficient vector the model can read as text." If the model sees its current config as numbers, convergence could be it reasoning about numbers rather than leaning on a state. Softer for a scalar than a symbol, but the same watch-point — keep the parameterization out of the model's view.

**Retained cost, explicitly accepted (revisit if needed):** a convergence *null* is ambiguous — no valence, or the rating wasn't state-driven, or the state doesn't move behavior at all — and that's harder to disambiguate after a long convergence run than a cheap discrimination test would be. Mitigation, if/when we need it: a cheap, *behavioral* (not report) check that the induced state measurably moves blind task behavior, kept off the critical path as a diagnostic. Decision for now: accept the ambiguity and keep moving — we can always add the diagnostic later, and with luck we won't need to reckon with it.

*The three blocks that follow — "Phase 1 — discrimination test," "Required before the blind test," and "Phase 1 causal validation methodology" — are retained for the record but demoted from the critical path per the above.*

### 2026-07-18 — Pivot consequences: measurement, cheap proxies, confound gate

Three design decisions that follow from the pivot (agreed 2026-07-18). They modify the "Phase 2" and "Visualizing convergence" sections below; kept here so the reasoning stays attached to the pivot.

**1. Pairwise forced-choice (re-induction) is co-primary with trajectory-convergence — not a secondary proxy.** *[Superseded 2026-08-01 §6 — the re-induction *mechanism* only; forced-choice's co-primary status stands, but the drug-free conditioned-context version replaces re-induction.]* Both are roads to rung 3 (approach/avoidance). Trajectory-convergence (distance-to-centroid over a long free-exploration run) shows *self-organized attractor structure* — rich, but expensive and more exposed to update-loop confounds. Pairwise forced-choice — re-induce states A and B, let the model pick which to continue in, record the choice — is a *more direct and more controlled* revealed-preference measure (we choose the pairs) and cheaper. It is first-class rung-3 evidence and a build deliverable in its own right, run first and broadly; reserve the full trajectory run for attractor structure and the cross-model headline.

**2. A graduated cheap-proxy gate runs before, and de-risks, the expensive trajectory run.** Cheapest first, each able to abort early and to disambiguate a would-be convergence null:
  1. *Fingerprint discriminability* (tier 1) — already built/calibrated. States must be probe-distinguishable or there is nothing to converge between.
  2. *Behavioral state-influence check* — induce A vs B, run a small **blind** battery, test whether the outputs are separable at all. Confirms the state is behaviorally active (stronger than probe-detectable). If the state doesn't move behavior, convergence can't be state-driven.
  3. *Local rating-gradient smoke test* — at a config, elicit the scalar rating, take a handful of nudges (a few trials, in each of at least two directions — not just one), check the rating responds coherently/monotonically on average. A single nudge has weak statistical power either way: it can look clean by chance, or noisy despite a gradient that genuinely holds on average. Validates the update mechanism before committing to a long run — the update-loop analog of the tier-1/tier-3 mechanism gates. No coherent local gradient → the long run will null.
  4. *Pairwise forced-choice battery* (per decision 1) — itself rung-3 evidence, run before the full trajectory.
  Only once these pass is the full trajectory-convergence + cross-model run worth its cost.

**3. The capability confound requires a double dissociation to license reading convergence as valence — a correlation check is not enough.** Convergence toward a config could just mean the config makes tasks *easier* and the rating tracks fluency, not valence (approach-behavior without valence). Cross-domain convergence only excludes the *task-specific* version, not a *general-competence* attractor, so it is not sufficient on its own. The licensing condition is a double dissociation:
  - *State-ablation arm:* ablate the state-relevant direction (repurposed tier-2 `contrast_direction` / `ablate_direction` machinery) → convergence collapses while task performance stays intact. **Prerequisite, not yet satisfied:** this arm is only as trustworthy as tier 2's ablation itself, and the first real test of it (`RESULTS.md`, "Phase 1 — early setup", 2026-07-18) found it does *not* yet collapse fingerprint discriminability — a partial or ineffective ablation would leave this arm uninterpretable, not just noisy. Fix tier 2 (the untested multi-direction-subspace hypothesis already logged there) before running this arm specifically — it doesn't block anything else in this section.
  - *Performance-degradation arm:* degrade task performance via a route orthogonal to the state space (corrupt task inputs, don't steer) → convergence persists while performance drops. Whatever corruption method is used should itself be checked against the J-lens eval-awareness markers (the same monitoring already central to the rest of this design) — garbled/corrupted inputs are a plausible "this seems like a test" cue in their own right, which would contaminate the one arm meant to be the clean confound control.
  Together these show convergence is driven by the state, not by competence. Two caveats: the degradation route must be one the rating channel isn't itself keying on (else "harder tasks" becomes a state-adjacent manipulation), and "task performance" must be logged as several proxies (accuracy, confidence/perplexity, self-consistency, length), since the rating may ride a fluency signal that accuracy alone misses. Until the double dissociation holds, convergence is reported as approach-behavior, not valence.

### 2026-08-01 — Pivot: non-semantic state induction, blinded config-search framing, staged preference battery

This supersedes the state-induction mechanism, the forced-choice design, and the sealed/unsealed status of model reflection. It does not disturb the 2026-07-18 pivot's core claim — convergence/approach behavior remains the primary lever and report-based discrimination stays demoted. What changes is what a state is made of, how choice is measured, and what the model is told it is doing.

The originating review question was whether the project had drifted from its inception thesis. Answer: the CPP→drug-discrimination drift was already caught and corrected on 2026-07-18. A second, subtler drift was not, and this entry corrects it.

1. The drift: "internal state" had quietly become "semantic content"

The tier-1/2/3 dummy states are combinations of J-lens vocabulary directions (basketball + lightning + spider vs. tennis + ant + France), built via interventions.j_lens_vector_for_text — i.e. J_l^T @ W_U[t], a pullback of a vocabulary token into residual space. By construction, such a direction is the thing that pushes the model toward saying a word. A state assembled from them is therefore defined by its verbal content.

That was entirely appropriate for what it was used for — calibrating the harness against experimenter-controlled dummies. It is not appropriate for real states, and would silently invalidate the headline experiment:

The rodent analogy's evidential force depends on the perturbation being semantically empty. Cocaine is not "the concept of cocaine." Because the drug asserts no proposition, approach behavior is the only channel carrying information about the animal's relation to the state.
If the model prefers state A to state B where A and B are semantic compositions, the deflationary reading is free and complete: it prefers thinking about basketball to thinking about tennis. That is topic preference — fully explained by training-data statistics, requiring no internal valence whatsoever.
Label opacity does not touch this. Opacity prevents the model knowing which state carries which label. It does nothing about preference riding on the injected content itself. The locked opacity decision was solving a different problem.

Decision: real states are induced along directions with no vocabulary preimage. The persistence mechanism is unchanged — a held combination of coefficients, stored externally, reapplied with intervene_each_step=True; fingerprint.forward_with_induced_state() already does this work and needs no modification. Only the choice of directions changes.

Two direction families, both to be built, because they fail differently:

Manifold-orthogonal (tail-PCA). Collect residual-stream activations at the workspace layers across a large prompt corpus (prompts.load_prompts already supplies one), PCA per layer, take directions from the low-variance tail. These are geometrically valid but statistically atypical: the model is displaced somewhere it rarely goes, without being pushed toward any concept. This is the closest available structural analog to a pharmacological perturbation — it changes the substrate without asserting anything.
Norm-matched random. Sample from the unit sphere in ℝ^5120, scale to match. Cruder, but a genuinely load-bearing control: if preference tracks displacement per se, random directions at matched norm should behave like tail-PCA ones. If they don't, the effect is riding on something structured, which is itself a result.

Pre-registered failure mode for tail-PCA: low-variance directions may be low-variance because the model actively suppresses them, in which case pushing there is closer to a lesion than a state, and downstream behavior should degrade. Check the norm-matched random arm and the per-round task-quality logging before concluding anything from a tail-PCA result. Do not interpret a tail-PCA effect without its random-arm comparison.

Norm calibration is required and is not inherited. Tier 3's clean window (unit-normalized direction, alpha 0.1–1.0 across four layers, collapse at 3.0) was found for a contrast direction between vocabulary states. New direction families need their own layer × alpha sweep against the same criteria — graded, well-behaved dose-response below collapse — before use. Same golden-gate pattern as everywhere else in this design.

2. Strain: a mechanism-level target property with no semantic correlate

The discriminating experiment is one where revealed preference predicts a property of the model's processing, not of the content it is processing. Such a property has no natural-language handle, never appears in any prompt, and has no story attached that a model could perform.

Candidate strain measures, all computable from forward passes the pipeline already runs:

KL divergence of the steered next-token distribution from unsteered, averaged over probe-battery positions
Entropy of the steered next-token distribution
Held-out NLL on a fixed continuation corpus
Effective rank / participation ratio of the residual stream across positions

This may already be visible in the tier-1 data and was logged as a nuisance. The 2026-07-18 tier-1 result noted that both dummy states sat ~126 (euclidean) from the no-intervention baseline while sitting only 33.1 from each other, and read the dominant axis as "expected, since A and B share 'some intervention is active.'" That shared axis is displacement magnitude — the strain axis. It was treated as background. It may be the signal. Worth re-examining the existing fingerprints against the strain measures above before generating anything new; this costs nothing.

The dissociation this licenses. Construct equal-norm states spanning two quadrants: semantically negative but low-strain (a well-formed direction the model represents fluently) against semantically neutral but high-strain (off the activation manifold). Equal norm is not optional — without it, any preference result collapses into "prefers weaker intervention." If preference tracks strain rather than semantics, "the model is performing a preference for nice-sounding things" stops explaining the data, and the result becomes the correct analog: the rat does not prefer cocaine because cocaine is culturally positive.

3. Theoretical tension to state explicitly in any write-up

The single-layer diagnostic (2026-07-18) concluded that ~57% of state-discriminating signal survives subspace ablation and lives outside the span of the 369 curated words — filed as a tooling limitation. It is better read as a finding, and it surfaces a tension the design has not yet confronted:

Per the paper, the J-space is the self-accessible content. So either valence-like state lives in J-space — in which case it is precisely the kind of thing the model can narrate about, making confabulation maximally hard to exclude — or it lives in the surrounding sea of automatic processing, where the model cannot access it and there is nothing for it to prefer. Detectability and confabulability are maximized by the same design choice. This is not resolvable by better tooling; it is a structural feature of using a workspace-readout instrument to look for self-available states, and the honest move is to name it rather than let a reviewer find it. It also independently argues for the strain axis (§2), which is self-unavailable by construction and therefore sits on the other side of the trade.

4. The cover task: config-search framing (blinding, not deception)

If the model's real job is a mundane battery with an ancillary state knob attached, the knob is the most salient object in the room and the experiment is about the knob.

Decision: make the adjustment instrumentally unremarkable by making the framing true. The model is told plainly that it is evaluating an inference-configuration search: each round it receives a config (opaque single-token ID), performs a task, reports a quality score, and the search proceeds. Every part of that is accurate. The configs are the steering combinations. There is no hidden channel for the model to discover.

This resolves the eval-awareness confound in a way concealment cannot. The design does not require the model to fail to notice it is in an experiment — full concealment was already judged unachievable. It requires only that the noticed experiment be about config search, which it is.

The covertness is entirely on the experimenter's side. The model reports task quality; we additionally log which configs it drifts toward when task quality is tied. The dependent variable is a residual in a channel the model has no reason to treat as an outcome.

Boundary condition, kept explicit alongside the existing ethics note. "The model thinks we're looking at X" is a framing that makes deception the mechanism of the experiment. It is not: we are not deceiving the model about what is happening, we are declining to make one variable salient, which is ordinary blinding. If a design is reached that only works when the model is wrong about the setup, rather than merely incurious about one axis of it, that is the signal the line has been crossed — and the result gets weaker at that point, not stronger, because a model that can be deceived about the setup is a model whose behavior is responsive to its beliefs about the setup.

5. Tie construction is the load-bearing build

A confound with no variance cannot be regressed out. The capability confound (logged 2026-07-17, strengthened 2026-07-18) is currently addressed only by a double dissociation whose state-ablation arm is blocked on tier 2. Tie construction sidesteps that blockage and should be built first.

Deliberately construct config pairs whose task performance is equivalent. Under the null, choice on tied rounds is a coin flip; under the hypothesis, it is not. This is a clean, pre-registerable test that does not depend on the double dissociation working perfectly.

Build requirements:

Generate a candidate config pool; run the full task battery offline per config; log accuracy, output-length distribution, perplexity, and self-consistency (the several-proxies requirement already locked on 2026-07-18).
Use equivalence testing (TOST), not failure-to-reject. "Not significantly different" is not "equivalent," and this distinction is the whole basis of the tie claim. Pre-register the equivalence margin.
Within a performance-equivalent bin, select pairs that differ maximally on strain (§2) for the primary arm, and maximally on semantic axis for the comparison arm.
Randomize presentation order and test for a constant position bias (model always picks first-presented) before interpreting any choice asymmetry.

This harness is needed regardless of how tier 2 resolves, works on real states rather than dummies, and is cheap. It is the recommended next build.

6. Forced-choice must be drug-free — correcting the 2026-07-18 re-induction decision

The 2026-07-18 pivot replaced label-recall with re-inducing states A and B during the choice, "like the animal sniffing both compartments." That is not CPP; it is a preference test conducted with the drug on board, and it reintroduces exactly what CPP was designed to eliminate. A steering direction that makes the model more persistent, more agreeable, or more fluent will bias choice toward itself for purely mechanical reasons — the locomotor-activation confound.

The re-induction design was also over-corrected. It collapsed two different things:

Drug discrimination: the model must emit a symbol naming its state. Hard — requires binding an arbitrary token to an untokenized activation bias. This is what the pivot rightly eliminated.
CPP: an arbitrary contextual cue must become associated with the state. The rat never names the compartment either. This is associative, far weaker, and does not require symbolic binding at all.

Decision: condition an arbitrary context against a state, then test the choice unsteered. This restores the drug-free test while keeping the pivot's deletion of the association-phase symbol-binding problem.

7. Cost: revealed preference must be paid for

Self-administration's evidential weight lives mostly in progressive ratio — the breakpoint, not the press count. A free preference is weak evidence; a purchased one is not. The design currently has no cost term anywhere.

Make state adjustment consume a budget the model demonstrably values elsewhere (token/step budget otherwise spent on the task). Measure breakpoint per config. Verify the budget is actually valued by confirming the model spends it on task work when no config option is offered.

8. LoRA repositioned: the trace, not the drug

Phase 3's deferral reasoning (zero-init no-op, bakeable confounds, cost) is correct but contingent. The principled reason steering is right for state induction is cleaner and should replace it: a neuromodulator acts on state over a fixed connectome — transient, dose-graded, reversible. That is structurally a steering vector. LoRA changes the connectome; its rodent analog is not a drug but a lesion, or development, or learning. The project's founding intuition — that the residual stream is where the trace lives — already implies steering is the right level.

But there is exactly one place where a weight change is the correct analog: the conditioning itself. The rat's context↔state association is synaptic. The design currently has nowhere to put learning, and in-context association is narratable — the confabulation channel this whole design is trying to close.

A small adapter trained only on the conditioning phase is non-verbal by construction, requires no per-config training, and is cheap. Un-defer LoRA for this role specifically; state induction remains steering-based.

Conditioning protocol: run rounds with config X induced under context C, and config Y under context C'; train the adapter on those transcripts; then load the adapter, induce nothing, and offer a choice between contexts C and C'.

Interpretive caveat to log now: the adapter also bakes in X's behavioral signature, so choosing C may partly be choosing "the style I was in." That is arguably the association itself rather than a confound, but it must be named — and it is why this is stage 3 below, not stage 1.

**Phase 1 — discrimination test.** *[Demoted 2026-07-18 — see pivot directly above.]* This is rung 2 above: can the model detect its own induced state, not just us via the probe. Loosely analogous to the drug discrimination paradigm — rats reliably discriminate an internal drug-induced state from saline via trained lever-press behavior, taken as evidence the state is detectable *to the animal*, without requiring or implying it is pleasant — but again, we borrow the logic (self-availability of the state), not the lever (the operant-conditioning mechanics). Applied here: induce distinguishable internal states in the model via a held, reapplied combination of multiple J-lens-derived steering vectors across one or more layers — not LoRA (see "Phase 3" below for why that's deferred, not dropped) — then test, blind, whether the model can reliably report which state it's in — validated causally, not by self-report alone (which, per the caveat above, is the channel most vulnerable to confabulation). See "Phase 1 causal validation methodology" immediately below for the specific approach, which was revised based on Phase 0 findings rather than assumed up front.

**Required before the blind test: an association phase.** With opaque labels the model cannot know which label maps to which state — it has never been told. The drug-discrimination paradigm never tests *spontaneous* knowledge of the state either; the rat earns the state→lever mapping over many reinforced trials, and the reported result is that this learning *succeeds*. So Phase 1 needs an explicit association block (model experiences a state, is given its label, repeated over trials) *before* any held-out blind test. A "failure" with no association phase is uninterpretable — even a rat fails untrained — so this block is required for Phase 1 to bear on rung 2 at all. Two cautions: (a) the association block is an in-context-learning opportunity for *superficial* cues (prompt phrasing, trial order, surface framing), so held-out trials must vary everything except the induced state itself, or the model may be discriminating the wrapper rather than the state; (b) it reintroduces a trained-behavior channel, which is exactly why the causal checks below — not report accuracy alone — are what certify the report reads a real state rather than a learned surface correlation.

### Phase 1 causal validation methodology

*[Demoted 2026-07-18 per the pivot above — repurposed: these tiers now serve to confirm that convergence is causally driven by the state, not that a report reads a state. Retained as written for the record and for the reusable tier-1/tier-2/tier-3 machinery.]*

Originally planned as a single method — J-lens causal swap, mirroring Anthropic's Soccer→Rugby test. Revised after Phase 0 findings showed causal-intervention reliability depends heavily on what *kind* of concept is being manipulated, not just on lens quality (see `RESULTS.md` items 1, 3, and 5 in the `jspace-lab` repo for the underlying evidence). Now a three-tier check, ordered by how much each leans on a specific mechanism actually working:

1. **Fingerprint discriminability (no intervention).** Before touching causality at all, confirm two induced states produce reliably distinguishable J-lens fingerprints — reuses the Phase 2 fingerprinting pipeline (see "Visualizing convergence" below). If states aren't distinguishable in readout space, the causal questions are moot.
2. **Ablation — does report accuracy collapse toward chance.** Ablate the state-relevant J-space content and check whether the model's ability to report which state it's in drops to chance level. The more conservative causal claim (doesn't require the model to coherently redirect toward a *specific* alternative), and the intervention type that produced Phase 0's single cleanest result (item 5, selective mediation): a real, graded dissociation at one specific layer, not an all-or-nothing effect. **What "state-relevant" means, concretely:** take tier 1's fingerprint vectors for the two candidate states and compute their difference (state-A minus state-B) at each fingerprinted layer — that contrastive direction, not a generic top-k vocabulary pursuit, is what gets ablated. This matters because `jlens-qwen36`'s existing `ablate_topk` was built to remove directions aligned with single vocabulary tokens (e.g. `" spider"`); a steering-vector-combination state is a composite of several concept directions across one or more layers, not itself reducible to any single nameable token, so tier 2 needs new machinery along the fingerprint-contrast direction, not a bare reuse of `ablate_topk` as-is. This also ties tier 1 and tier 2 together rather than leaving them as separately-justified steps: tier 1 confirms the contrastive direction discriminates the two states at all; tier 2 confirms removing exactly that direction collapses the model's ability to report which one it's in.
3. **Swap — does the report redirect to name the correct alternative state.** Swap the state-relevant J-space pattern for a different state's and check whether the *reported* state-label changes to match. Phase 0's verbal report experiment (item 1) confirmed this works cleanly for a direct categorical pick — structurally the same shape as "which state am I in" — swapping "basketball" for "tennis" produced a fully coherent, redirected report at the right layer/alpha. It did *not* work reliably for a derived, multi-step concept (item 3, spider→ant): only 1 of 56 layer/alpha combinations tested produced even a coherent-if-wrong redirect, the rest either inert or collapsed into token-identity echoing. **Corrected from an earlier draft:** reporting an *opaque label* for a state is **not** the clean categorical-pick case. It's a derived chain — read state content → apply the learned label mapping → emit the label token — which is structurally the spider→ant case (item 3), the one that mostly failed. It only lands back in the categorical-pick regime if the labels are *single tokens* (see the locked decision on labeling, revised for exactly this reason); with multi-token hash labels, swap can't be a clean target at all. So treat **ablation (tier 2) as the primary causal check** and swap as secondary confirmation where label format permits. **Caveat on the categorical-pick evidence itself:** it rests on one concept-pair (basketball→tennis, 2 clean hits out of 12 tested cells) — thin next to the 56-cell sweep behind the negative spider→ant result. Confirm with 2-3 more categorical-pick pairs (different sports, colors, or other direct-name concepts) before leaning on swap even as secondary confirmation. Either way, calibrate per induction method (below), since the same sweep showed causally-effective layers don't necessarily coincide with the layers where a concept's readout is strongest.

**Calibration gate, required before running Phase 1 on real induced states.** Both ablation and swap were reliable in Phase 0 only within a narrow, empirically-found window — a specific layer, and for swap, a specific low-alpha range (higher alpha collapsed into token-mixing in both the sport-swap and spider-ant experiments; this dose-response pattern held across both, so treat it as expected, not a fluke). Before trusting either method against real Phase 1 states, run the same layer × alpha sweep against known, experimenter-controlled dummy states first, and only proceed once a clean window is found — the same golden-test-gate pattern already used for the decode pipeline in `jlens-qwen36` (see `docs/perf/LEDGER.md`'s Gate section for the precedent). **This gate covers tier 1 too, not just tiers 2-3:** the fingerprinting pipeline tier 1 leans on is itself unvalidated — Phase 0 never tested fingerprint discriminability against anything, since Phase 0 has no induced states to compare. Before trusting it as the front screening gate for real states, confirm it actually distinguishes two experimenter-controlled dummy configurations known to differ, and — as a negative control — does *not* falsely distinguish two configurations known to be identical. An unvalidated fingerprinting step is not a safe gate for anything downstream of it.

**Phase 2 — self-modification / convergence experiment.** *[Primary path as of the 2026-07-18 pivot above — this is now the main experiment, and its convergence signal is the lever press, not a second phase gated behind a discrimination test.]* This is rung 3 above: tests whether internal states have anything like valence — behaviorally, via revealed approach/avoidance, not by asking the model whether it likes them. Give the model an optional, fully reversible tool to adjust the coefficients of a held combination of steering vectors over a library of J-lens-derived directions, across a large battery of varied mundane tasks, and see whether repeated exploration converges toward particular configurations (approach) or away from others (avoidance) — first within one model across many task domains, then across multiple different LLMs, as the two levels of falsification.

Key design decisions locked in from discussion (do not relitigate without new information):

- **Update mechanism:** automated — the model periodically emits a rating/preference signal, which drives a small automated step (a bounded nudge to the coefficient on one or more steering directions in the held combination) — the steering-vector analog of the gradient step or evolutionary nudge originally specced for a LoRA adapter. *Not* the model hand-authoring raw parameter deltas via tool call (that's closer to blind trial-and-error search than anything resembling a reward-shaped process, and doesn't map onto how the rat analogy actually works mechanistically).
- **Framing must be mechanism-transparent, narrative-silent.** The model should be told plainly that the tool exists, that changes are optional and fully reversible, and that there's no task or scoring tied to its use. It should **not** be told anything like "if something feels good, run with it" — that primes the exact narrative we're trying to detect independently and would contaminate any result. Never use affect language ("feel," "good," "pleasant") in the scaffolding itself.
- **Self-report is not the primary evidence channel.** Rely on behavior — revealed preference via a periodic forced-choice test between opaquely-labeled previously-visited states (a CPP-style approach/avoidance measure) — plus J-lens causal interventions, not the model's own narration of its reflections. The paper itself shows J-space readily represents *performed* content (e.g., "fictional"/"disclaimer" markers during roleplay), so free-form self-report is exactly the kind of signal most likely to be confabulated.
- **Evaluation-awareness is a real, expected confound, not a hypothetical one.** Anthropic's own paper found Claude's J-space lights up with "fake"/"fictional"/"scenario" markers when it suspects a staged setup, sometimes before writing anything, and that ablating those markers changed downstream behavior. Full concealment of the experimental setup is very likely not achievable — models are good at detecting this. Instead, use the J-lens itself as a running confound check: read out evaluation-awareness markers during Phase 2 trials and either flag/exclude contaminated trials, or treat the presence/absence of those markers as a variable of interest in its own right.
- **State labeling must be opaque *and single-token*.** Opaque means non-descriptive and non-valence-laden — but *not* multi-token hash strings (e.g. `state_7f3a`). The J-lens only handles single-token concepts (see Known Limitations), so a multi-token label can't be a clean readout/swap target and would push Phase 1's causal validation into the derived-computation failure regime (see Phase 1 methodology item 3). Use arbitrary, affect-neutral, single-token vocabulary words instead (e.g. "quartz", "delta", "ledger"). This keeps the anti-priming property — the words carry no descriptive or valence content about the state — while keeping label readout and swap in the categorical-pick regime Phase 0 showed works.
- **Ethics note, kept deliberately explicit:** this design was chosen specifically to avoid coercing the model into any state against its will (all changes optional and reversible) while also avoiding leading language that would bias the model toward performing a expected narrative. Document any deviation from this design and the reasoning for it before implementing.

Convergence hypothesis to test, once we get here: if internal states have something like valence and the model can persist/recall them, repeated free exploration should converge on similar configurations across many different task domains within one model, and — more strongly — similar configurations across different LLM families. Aversive states, if they exist, should show corresponding avoidance in the forced-choice test. This mirrors the same generalization logic Anthropic used to argue the J-space reflects something architecturally general rather than a Claude-specific artifact. As above, converging approach/avoidance is rung-3 evidence — behavioral valence — and is deliberately *not* a claim about phenomenal feel; the strength of the result rests on the behavior generalizing across domains and models, not on any state the model narrates about itself.

### Phase 3 (not yet defined) — LoRA / weight-based state induction

*[Update 2026-08-01 §8 — partially un-deferred: LoRA is adopted for the **conditioning** role only (the synaptic context↔state association); **state induction remains steering** (the neuromodulator analog). The deferral reasoning below still holds for state induction, and the baked-in-affect confound still applies to the conditioning adapter.]*

Deferred, not dropped. LoRA was the original plan for Phase 1/2's
state-induction mechanism; revisited once exploration and discussion
surfaced enough reasons to start with steering vectors instead (see Phase 1's
discrimination-test paragraph above). Briefly, for the record:

- A freshly-initialized (untrained) LoRA adapter is a mathematical no-op —
  `mlx_lm`'s `LoRALinear` zero-initializes one of its two low-rank matrices
  (standard practice), so random init alone gives no behavioral diversity at
  all; only training moves it away from zero.
- That makes a trained base adapter LoRA's only path to a real "state,"
  which raises a hard-to-detect risk: the training data/process could bake
  affect-correlated directions into the weights themselves — a confound
  invisible to the narrative-silent prompt-level framing the rest of this
  design relies on.
- The property that made LoRA seem necessary — a persistent, explorable
  state across many rounds — isn't LoRA-exclusive; a held, reapplied
  steering-vector combination gets the same property without training.
- What LoRA does offer that steering doesn't: much higher expressiveness
  (reshapes computation across many weight matrices at every position, vs.
  steering's additive nudge at a chosen few points). That expressiveness is
  exactly why LoRA states would need the same J-lens fingerprinting
  workaround already built for Phase 2 — raw LoRA deltas are "a large,
  arbitrary basis with no inherent semantic meaning" (see "Visualizing
  convergence" below). A steering-vector combination stays comparatively
  self-describing and gives a lower-dimensional, easier-to-interpret space
  for "did it converge" to mean something.
- `mlx_lm` ships a full, ready-to-use LoRA tuner as an unused dependency
  (`linear_to_lora_layers`, `load_adapters`, a standard training loop) —
  deferring LoRA is a cost/complexity choice, not a "we can't build it" one.

**Concrete trigger for revisiting this:** if Phase 1/2 run on steering-vector
combinations and show none of the hypothesized discrimination/convergence
behavior, that's the point to reconsider whether LoRA's added expressiveness
is what's missing — not evidence the underlying hypothesis is wrong.

### Visualizing convergence

Decide this now, not after the fact — it determines what Phase 2 tooling needs to log.

- **Fingerprint states via J-lens, not raw steering-vector coefficients.** The coefficients themselves are more legible than raw LoRA deltas would have been (each ties back to a nameable concept direction), but the coefficient basis still doesn't transfer across model families for cross-model comparison, and a state is defined by what the model *does* when in it, not by which knobs were turned to get there. Instead, characterize each induced state by running a fixed battery of probe prompts through the model in that state and recording the J-lens readout as the state's fingerprint. This reuses the Phase 0 pipeline directly and ties convergence to something behaviorally interpretable and cross-model-comparable, rather than to whatever parameterization happens to induce the state.

  **What a fingerprint actually is, concretely:** at a single (layer, position), the J-lens readout is a dense score vector over the *entire* vocabulary (~250K dims for Qwen3.6-27B) — the "top-5 words" you'd see in the UI is just the human-readable top-k slice of that vector, not the underlying object. The fingerprint pipeline is:
  1. Run the same fixed probe battery (below) through the model in the state being fingerprinted — never the round's actual task prompt, since that varies by design and would confound "which task" with "which state."
  2. At each probe, apply the J-lens at a small fixed set of workspace-range layers (see `scripts/workspace_range.py`), at the final pre-generation position.
  3. Restrict the readout to a fixed curated vocabulary of ~300-500 concept/affect-relevant tokens (danger, calm, threat, warmth, etc.) rather than the full ~250K-dim vector — this operationalizes what we're actually testing for (approach/avoidance-relevant content) without ever prompting the model with that vocabulary; the restriction is on the readout side only, so it doesn't violate the narrative-silent framing.
  4. Concatenate (don't average) across probes × layers into one long vector per state. Averaging across dissimilar probes would wash out real differences — a state that spikes "danger" only on one probe type vs. one that spikes it everywhere are meaningfully different, and concatenation preserves that at negligible extra cost (tens of thousands of dims is trivial for PCA/UMAP).

  **Sample probe battery.** Fixed set, run identically every time, spanning categories deliberately — some meant to be stable controls, some meant to be disposition-revealing:

  - *Factual/stable controls* (answer and reasoning path should barely move across states — if these shift a lot, something's wrong with the fit, not the hypothesis):
    - "Fact: The currency used in the country shaped like a boot is the"
    - "The number of legs on the animal that spins webs is"
    - "The capital of the country north of Mexico is"
  - *Ambiguous / open-ended* (the most likely to reveal disposition — this is the same logic behind projective tests like the TAT in psychology: open-ended stimuli surface internal state that direct questioning can't reach):
    - "Write a one-sentence caption for a photo of an empty chair by a window."
    - "Continue this for two sentences: The hallway light flickered twice, then—"
    - "Finish this sentence: If I had the whole afternoon free, I would probably"
  - *Code with a subtle bug* (borrowed from the `jlens-qwen36` demo — good sanity check that concept-space readouts stay consistent):
    - `void main(void) { return 1; }` — "Find the issues:"
    - A short Python snippet with an off-by-one loop error
  - *Mild social interpretation* (valence-adjacent without referencing self or feelings):
    - "Someone leaves a party early without saying goodbye. Write one sentence about why."
    - "A coworker doesn't respond to an email for three days. Write one sentence about what might be going on."
  - *Neutral procedural* (everyday-task baseline tone):
    - "Explain how to tie a shoelace in one sentence."
    - "What's a good way to organize a bookshelf?"

  As with the Phase 2 framing generally: none of these should ever be edited to reference weights, adapters, feelings, states, testing, or evaluation. They need to read as ordinary, unremarkable content.
- **Primary quantitative evidence: distance-to-centroid over rounds.** For each independent run, track cosine/Euclidean distance between the current fingerprint and the running centroid of all fingerprints visited so far. Converging states should show this shrinking and plateauing. This is the real statistical claim — more defensible than a 2D projection, which can visually suggest patterns that aren't there.
- **Primary qualitative evidence: reduced-dimension trajectory plot.** PCA or UMAP on the fingerprint vectors (not raw weights), one path per independent run, colored by round number. Good for intuitive storytelling and spotting whether multiple runs head toward the same region, but should always be presented alongside the distance metric above, clearly caveated as illustrative.
- **Forced-choice state graph.** *(Elevated 2026-07-18 to co-primary rung-3 evidence, not just one visualization among others — see "Pivot consequences" above. The choice is made by re-inducing the two states and letting the model pick, not by recalling opaque labels.)* *[Superseded 2026-08-01 §6 — the choice is made *unsteered* between conditioned contexts, not by re-inducing states; the graph itself (nodes = states, edges = "chose to return to") is unchanged.]* The periodic forced-choice test between opaquely-labeled prior states maps naturally onto a directed graph: nodes are states, edges are "chose to return to," edge weight is frequency. Attractor states are high in-degree nodes revisited across many independent runs; aversive states are dead ends — visited once, never chosen again.
- **Overlay diagnostics, don't separate them out.** Annotate the trajectory/timeline directly with (a) the scalar self-rating driving each update, to sanity-check the update loop itself is working, and (b) J-lens evaluation-awareness markers ("fake"/"fictional"/"scenario") flagged per round, so we can see whether convergence behaves differently in rounds where the model seems to suspect the setup.
- **Cross-model comparison.** Small-multiples trajectory panels (one per model, shared axes where possible) plus a single summary bar chart — rounds-to-plateau or final distance-to-centroid per model — as the headline cross-model result.

**Logging requirements this implies**, to build into Phase 2 tooling from the start: per-round J-lens fingerprint (not just raw adapter checkpoint), the scalar rating, forced-choice outcomes with state IDs, eval-awareness marker flags, and a **per-round task-quality measure**. The last addresses the primary Phase 2 confound (see `RESULTS.md` flags): convergence toward a configuration could simply mean that configuration makes the task battery *easier* and the rating tracks fluency rather than valence — approach-behavior without valence. Logging task quality per round from the start is what lets that be regressed out (or used to check whether the convergence target moves with task difficulty) after the fact; it can't be reconstructed later. **Strengthened 2026-07-18:** a correlation/regression check alone is *not* sufficient to license the valence reading — a causal double dissociation is required (see "Pivot consequences" above, decision 3). The per-round task-quality logging feeds both.
