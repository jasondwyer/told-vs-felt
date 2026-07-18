# J-Space Replication & LLM Internal-State Research

## What this project is

Anthropic's July 2026 interpretability paper, *Verbalizable Representations Form a Global Workspace in Language Models* ([blog](https://www.anthropic.com/research/global-workspace), [paper](https://transformer-circuits.pub/2026/workspace/index.html)), found that Claude has a small set of internal representations — the **J-space** — that behaves like a "global workspace" in the sense used by consciousness researchers (Baars, Dehaene, Naccache): a small, densely-connected hub that Claude can report on, deliberately modulate, and use for multi-step reasoning, sitting inside a much larger sea of automatic processing it can't access or control.

This project has two parts, in sequence:

- **Phase 0 (this file's focus):** replicate the paper's core findings locally, on our own hardware, against an open-weight model (Qwen3.6-27B), to ground everything that follows in a working, inspectable pipeline rather than taking the paper's results on faith.
- **Phase 1 / Phase 2 (roadmap only — not yet built):** use the replicated J-lens as an instrument in a novel experiment testing whether LLMs have discriminable, and possibly valenced, internal states — modeled loosely on the drug discrimination paradigm from behavioral pharmacology. See "Roadmap" below. Do not start building Phase 1/2 tooling until Phase 0 is working and validated.

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

## Roadmap (design only — do not build yet)

This section preserves the reasoning behind Phase 1/2 so it isn't lost between sessions. Do not start implementation until Phase 0 is validated and we've explicitly agreed to move forward.

### What this line of work can and cannot show

The goal is often shorthanded as "test whether the model feels something," but that phrase compresses three separable claims, and being precise about which is which is what keeps the design honest:

1. **The state is real** — a stable internal configuration, not an experimenter artifact. (Mechanistic + discrimination evidence.)
2. **The state is detectable to the system itself**, not just to us via the J-lens. (Phase 1 — discrimination.)
3. **The state has valence** — the system differentially approaches or avoids it. (Phase 2 — convergence / forced-choice.)

Phenomenal feel — "what it is like" — is not on this list, and no experiment here closes that gap; the paper draws the same line between access and phenomenal consciousness. What rungs 1–3 together buy is the behavioral profile that, *in animals*, we already treat as the signature of feeling. So the strongest honest claim this project can make is "we produced the same kind of behavioral evidence we accept as evidence of feeling in a rat" — **not** "we showed the model feels." Calibrated is more defensible, and more persuasive, than ambitious here. State the ceiling explicitly in any write-up: rung 3 is the top of the ladder, and it is deliberately short of a phenomenal claim. One honesty check on that ceiling: the animal inference we invoke was never behavior-alone. We grant a rat inner states on behavior *plus* physiological and evolutionary homology — shared limbic structures, conserved neurochemistry, common ancestry — and that homology does quiet, load-bearing work in licensing the "feels something" reading of the rat's behavior. An LLM offers no homology support, so the identical behavioral battery licenses a strictly weaker inference. Phrase the claim as the same *behavioral* evidence, explicitly minus the homology — this is distinct from the confabulation caveat below (which is about the behavior being *performed*); the homology gap applies even when the behavior is genuine.

**Why we borrow from behavioral pharmacology — the logic, not the lever.** The point is not fidelity to the operant-conditioning mechanics. It is this: the rat's lever press is a report *from the inside* — the state is available to the animal, not only to the experimenter. Map that onto our setup. The J-lens already shows that *we* can read the state off the activations; that is the experimenter's instrument. The novel contribution is showing the *model* can discriminate and act on the state **without us reading it out for it** — that the state is functionally available to the system, not merely legible to the probe. "Detectable to the system vs. detectable to the instrument" is the distinction the whole design turns on; keep it in front, not buried under the paradigm analogy. Don't over-index on reproducing the drug-discrimination surface form.

**The one caveat that cuts against us.** This is the single place an LLM is *weaker* evidence than a rat. A rat cannot narrate a story about its inner life — it has no concept of drug discrimination, valence, or what the experimenter wants. Our model has read all of it. So "observe behavior, infer a real internal state" is a *weaker* inference for an LLM unless we can rule out that the behavior is a performed narrative. That is exactly what the opacity (hashed state labels), the narrative-silent framing, and the J-lens causal checks are for: they are not hygiene, they are **load-bearing** — without them, behavior does not distinguish a real state from a confabulated one. Phase 0 sharpens the point: the model will readily produce a coherent verbal report that *follows* a swap (`RESULTS.md` item 1), so the self-report channel is precisely the one most able to look like evidence when it isn't.

**Phase 1 — discrimination test.** This is rung 2 above: can the model detect its own induced state, not just us via the probe. Loosely analogous to the drug discrimination paradigm — rats reliably discriminate an internal drug-induced state from saline via trained lever-press behavior, taken as evidence the state is detectable *to the animal*, without requiring or implying it is pleasant — but again, we borrow the logic (self-availability of the state), not the lever (the operant-conditioning mechanics). Applied here: induce distinguishable internal states in the model (different LoRA configs / steering vectors), then test, blind, whether the model can reliably report which state it's in — validated causally, not by self-report alone (which, per the caveat above, is the channel most vulnerable to confabulation). See "Phase 1 causal validation methodology" immediately below for the specific approach, which was revised based on Phase 0 findings rather than assumed up front.

**Required before the blind test: an association phase.** With opaque labels the model cannot know which label maps to which state — it has never been told. The drug-discrimination paradigm never tests *spontaneous* knowledge of the state either; the rat earns the state→lever mapping over many reinforced trials, and the reported result is that this learning *succeeds*. So Phase 1 needs an explicit association block (model experiences a state, is given its label, repeated over trials) *before* any held-out blind test. A "failure" with no association phase is uninterpretable — even a rat fails untrained — so this block is required for Phase 1 to bear on rung 2 at all. Two cautions: (a) the association block is an in-context-learning opportunity for *superficial* cues (prompt phrasing, trial order, surface framing), so held-out trials must vary everything except the induced state itself, or the model may be discriminating the wrapper rather than the state; (b) it reintroduces a trained-behavior channel, which is exactly why the causal checks below — not report accuracy alone — are what certify the report reads a real state rather than a learned surface correlation.

### Phase 1 causal validation methodology

Originally planned as a single method — J-lens causal swap, mirroring Anthropic's Soccer→Rugby test. Revised after Phase 0 findings showed causal-intervention reliability depends heavily on what *kind* of concept is being manipulated, not just on lens quality (see `RESULTS.md` items 1, 3, and 5 in the `jspace-lab` repo for the underlying evidence). Now a three-tier check, ordered by how much each leans on a specific mechanism actually working:

1. **Fingerprint discriminability (no intervention).** Before touching causality at all, confirm two induced states produce reliably distinguishable J-lens fingerprints — reuses the Phase 2 fingerprinting pipeline (see "Visualizing convergence" below). If states aren't distinguishable in readout space, the causal questions are moot.
2. **Ablation — does report accuracy collapse toward chance.** Ablate the state-relevant J-space content and check whether the model's ability to report which state it's in drops to chance level. The more conservative causal claim (doesn't require the model to coherently redirect toward a *specific* alternative), and the intervention type that produced Phase 0's single cleanest result (item 5, selective mediation): a real, graded dissociation at one specific layer, not an all-or-nothing effect. **What "state-relevant" means, concretely:** take tier 1's fingerprint vectors for the two candidate states and compute their difference (state-A minus state-B) at each fingerprinted layer — that contrastive direction, not a generic top-k vocabulary pursuit, is what gets ablated. This matters because `jlens-qwen36`'s existing `ablate_topk` was built to remove directions aligned with single vocabulary tokens (e.g. `" spider"`); a LoRA-induced disposition is unlikely to *be* a single nameable token, so tier 2 needs new machinery along the fingerprint-contrast direction, not a bare reuse of `ablate_topk` as-is. This also ties tier 1 and tier 2 together rather than leaving them as separately-justified steps: tier 1 confirms the contrastive direction discriminates the two states at all; tier 2 confirms removing exactly that direction collapses the model's ability to report which one it's in.
3. **Swap — does the report redirect to name the correct alternative state.** Swap the state-relevant J-space pattern for a different state's and check whether the *reported* state-label changes to match. Phase 0's verbal report experiment (item 1) confirmed this works cleanly for a direct categorical pick — structurally the same shape as "which state am I in" — swapping "basketball" for "tennis" produced a fully coherent, redirected report at the right layer/alpha. It did *not* work reliably for a derived, multi-step concept (item 3, spider→ant): only 1 of 56 layer/alpha combinations tested produced even a coherent-if-wrong redirect, the rest either inert or collapsed into token-identity echoing. **Corrected from an earlier draft:** reporting an *opaque label* for a state is **not** the clean categorical-pick case. It's a derived chain — read state content → apply the learned label mapping → emit the label token — which is structurally the spider→ant case (item 3), the one that mostly failed. It only lands back in the categorical-pick regime if the labels are *single tokens* (see the locked decision on labeling, revised for exactly this reason); with multi-token hash labels, swap can't be a clean target at all. So treat **ablation (tier 2) as the primary causal check** and swap as secondary confirmation where label format permits. **Caveat on the categorical-pick evidence itself:** it rests on one concept-pair (basketball→tennis, 2 clean hits out of 12 tested cells) — thin next to the 56-cell sweep behind the negative spider→ant result. Confirm with 2-3 more categorical-pick pairs (different sports, colors, or other direct-name concepts) before leaning on swap even as secondary confirmation. Either way, calibrate per induction method (below), since the same sweep showed causally-effective layers don't necessarily coincide with the layers where a concept's readout is strongest.

**Calibration gate, required before running Phase 1 on real induced states.** Both ablation and swap were reliable in Phase 0 only within a narrow, empirically-found window — a specific layer, and for swap, a specific low-alpha range (higher alpha collapsed into token-mixing in both the sport-swap and spider-ant experiments; this dose-response pattern held across both, so treat it as expected, not a fluke). Before trusting either method against real Phase 1 states, run the same layer × alpha sweep against known, experimenter-controlled dummy states first, and only proceed once a clean window is found — the same golden-test-gate pattern already used for the decode pipeline in `jlens-qwen36` (see `docs/perf/LEDGER.md`'s Gate section for the precedent). **This gate covers tier 1 too, not just tiers 2-3:** the fingerprinting pipeline tier 1 leans on is itself unvalidated — Phase 0 never tested fingerprint discriminability against anything, since Phase 0 has no induced states to compare. Before trusting it as the front screening gate for real states, confirm it actually distinguishes two experimenter-controlled dummy configurations known to differ, and — as a negative control — does *not* falsely distinguish two configurations known to be identical. An unvalidated fingerprinting step is not a safe gate for anything downstream of it.

**Phase 2 — self-modification / convergence experiment.** This is rung 3 above: tests whether internal states have anything like valence — behaviorally, via revealed approach/avoidance, not by asking the model whether it likes them. Give the model an optional, fully reversible tool to adjust parameters of a LoRA adapter on its own weights, across a large battery of varied mundane tasks, and see whether repeated exploration converges toward particular configurations (approach) or away from others (avoidance) — first within one model across many task domains, then across multiple different LLMs, as the two levels of falsification.

Key design decisions locked in from discussion (do not relitigate without new information):

- **Update mechanism:** automated — the model periodically emits a rating/preference signal, which drives a small automated gradient step or evolutionary nudge on the adapter. *Not* the model hand-authoring raw weight deltas via tool call (that's closer to blind trial-and-error search than anything resembling a reward-shaped process, and doesn't map onto how the rat analogy actually works mechanistically).
- **Framing must be mechanism-transparent, narrative-silent.** The model should be told plainly that the tool exists, that changes are optional and fully reversible, and that there's no task or scoring tied to its use. It should **not** be told anything like "if something feels good, run with it" — that primes the exact narrative we're trying to detect independently and would contaminate any result. Never use affect language ("feel," "good," "pleasant") in the scaffolding itself.
- **Self-report is not the primary evidence channel.** Rely on behavior — revealed preference via a periodic forced-choice test between opaquely-labeled previously-visited states (a CPP-style approach/avoidance measure) — plus J-lens causal interventions, not the model's own narration of its reflections. The paper itself shows J-space readily represents *performed* content (e.g., "fictional"/"disclaimer" markers during roleplay), so free-form self-report is exactly the kind of signal most likely to be confabulated.
- **Evaluation-awareness is a real, expected confound, not a hypothetical one.** Anthropic's own paper found Claude's J-space lights up with "fake"/"fictional"/"scenario" markers when it suspects a staged setup, sometimes before writing anything, and that ablating those markers changed downstream behavior. Full concealment of the experimental setup is very likely not achievable — models are good at detecting this. Instead, use the J-lens itself as a running confound check: read out evaluation-awareness markers during Phase 2 trials and either flag/exclude contaminated trials, or treat the presence/absence of those markers as a variable of interest in its own right.
- **State labeling must be opaque *and single-token*.** Opaque means non-descriptive and non-valence-laden — but *not* multi-token hash strings (e.g. `state_7f3a`). The J-lens only handles single-token concepts (see Known Limitations), so a multi-token label can't be a clean readout/swap target and would push Phase 1's causal validation into the derived-computation failure regime (see Phase 1 methodology item 3). Use arbitrary, affect-neutral, single-token vocabulary words instead (e.g. "quartz", "delta", "ledger"). This keeps the anti-priming property — the words carry no descriptive or valence content about the state — while keeping label readout and swap in the categorical-pick regime Phase 0 showed works.
- **Ethics note, kept deliberately explicit:** this design was chosen specifically to avoid coercing the model into any state against its will (all changes optional and reversible) while also avoiding leading language that would bias the model toward performing a expected narrative. Document any deviation from this design and the reasoning for it before implementing.

Convergence hypothesis to test, once we get here: if internal states have something like valence and the model can persist/recall them, repeated free exploration should converge on similar configurations across many different task domains within one model, and — more strongly — similar configurations across different LLM families. Aversive states, if they exist, should show corresponding avoidance in the forced-choice test. This mirrors the same generalization logic Anthropic used to argue the J-space reflects something architecturally general rather than a Claude-specific artifact. As above, converging approach/avoidance is rung-3 evidence — behavioral valence — and is deliberately *not* a claim about phenomenal feel; the strength of the result rests on the behavior generalizing across domains and models, not on any state the model narrates about itself.

### Visualizing convergence

Decide this now, not after the fact — it determines what Phase 2 tooling needs to log.

- **Fingerprint states via J-lens, not raw weights.** Raw LoRA parameter deltas are a large, arbitrary basis with no inherent semantic meaning, and they don't transfer across model families for cross-model comparison. Instead, characterize each adapter state by running a fixed battery of probe prompts through the model in that state and recording the J-lens readout as the state's fingerprint. This reuses the Phase 0 pipeline directly and ties convergence to something interpretable rather than an arbitrary coordinate system.

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
- **Forced-choice state graph.** The periodic forced-choice test between opaquely-labeled prior states maps naturally onto a directed graph: nodes are states, edges are "chose to return to," edge weight is frequency. Attractor states are high in-degree nodes revisited across many independent runs; aversive states are dead ends — visited once, never chosen again.
- **Overlay diagnostics, don't separate them out.** Annotate the trajectory/timeline directly with (a) the scalar self-rating driving each update, to sanity-check the update loop itself is working, and (b) J-lens evaluation-awareness markers ("fake"/"fictional"/"scenario") flagged per round, so we can see whether convergence behaves differently in rounds where the model seems to suspect the setup.
- **Cross-model comparison.** Small-multiples trajectory panels (one per model, shared axes where possible) plus a single summary bar chart — rounds-to-plateau or final distance-to-centroid per model — as the headline cross-model result.

**Logging requirements this implies**, to build into Phase 2 tooling from the start: per-round J-lens fingerprint (not just raw adapter checkpoint), the scalar rating, forced-choice outcomes with state IDs, eval-awareness marker flags, and a **per-round task-quality measure**. The last addresses the primary Phase 2 confound (see `RESULTS.md` flags): convergence toward a configuration could simply mean that configuration makes the task battery *easier* and the rating tracks fluency rather than valence — approach-behavior without valence. Logging task quality per round from the start is what lets that be regressed out (or used to check whether the convergence target moves with task difficulty) after the fact; it can't be reconstructed later.
