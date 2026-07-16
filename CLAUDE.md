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

**Phase 1 — discrimination test.** Analogous to the behavioral-pharmacology drug discrimination paradigm: rats can reliably discriminate an internal drug-induced state from saline via trained lever-press behavior, which is taken as behavioral evidence the state is detectable to the animal, without requiring — or implying — that the state is pleasant. Applied here: induce distinguishable internal states in the model (different LoRA configs / steering vectors), then test, blind, whether the model can reliably report which state it's in — and critically, use J-lens causal swap interventions (not self-report alone) to confirm the report is genuinely read out of a stable state-specific representation rather than confabulated.

**Phase 2 — self-modification / convergence experiment.** Tests whether internal states have anything like valence: give the model an optional, fully reversible tool to adjust parameters of a LoRA adapter on its own weights, across a large battery of varied mundane tasks, and see whether repeated exploration converges toward particular configurations (approach) or away from others (avoidance) — first within one model across many task domains, then across multiple different LLMs, as the two levels of falsification.

Key design decisions locked in from discussion (do not relitigate without new information):

- **Update mechanism:** automated — the model periodically emits a rating/preference signal, which drives a small automated gradient step or evolutionary nudge on the adapter. *Not* the model hand-authoring raw weight deltas via tool call (that's closer to blind trial-and-error search than anything resembling a reward-shaped process, and doesn't map onto how the rat analogy actually works mechanistically).
- **Framing must be mechanism-transparent, narrative-silent.** The model should be told plainly that the tool exists, that changes are optional and fully reversible, and that there's no task or scoring tied to its use. It should **not** be told anything like "if something feels good, run with it" — that primes the exact narrative we're trying to detect independently and would contaminate any result. Never use affect language ("feel," "good," "pleasant") in the scaffolding itself.
- **Self-report is not the primary evidence channel.** Rely on behavior — revealed preference via a periodic forced-choice test between opaquely-labeled previously-visited states (a CPP-style approach/avoidance measure) — plus J-lens causal interventions, not the model's own narration of its reflections. The paper itself shows J-space readily represents *performed* content (e.g., "fictional"/"disclaimer" markers during roleplay), so free-form self-report is exactly the kind of signal most likely to be confabulated.
- **Evaluation-awareness is a real, expected confound, not a hypothetical one.** Anthropic's own paper found Claude's J-space lights up with "fake"/"fictional"/"scenario" markers when it suspects a staged setup, sometimes before writing anything, and that ablating those markers changed downstream behavior. Full concealment of the experimental setup is very likely not achievable — models are good at detecting this. Instead, use the J-lens itself as a running confound check: read out evaluation-awareness markers during Phase 2 trials and either flag/exclude contaminated trials, or treat the presence/absence of those markers as a variable of interest in its own right.
- **State labeling must be opaque** (checkpoint hashes, not descriptive or valence-laden names) to avoid priming interpretation when the model is asked to recall or choose between prior states.
- **Ethics note, kept deliberately explicit:** this design was chosen specifically to avoid coercing the model into any state against its will (all changes optional and reversible) while also avoiding leading language that would bias the model toward performing a expected narrative. Document any deviation from this design and the reasoning for it before implementing.

Convergence hypothesis to test, once we get here: if internal states have something like valence and the model can persist/recall them, repeated free exploration should converge on similar configurations across many different task domains within one model, and — more strongly — similar configurations across different LLM families. Aversive states, if they exist, should show corresponding avoidance in the forced-choice test. This mirrors the same generalization logic Anthropic used to argue the J-space reflects something architecturally general rather than a Claude-specific artifact.

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

**Logging requirements this implies**, to build into Phase 2 tooling from the start: per-round J-lens fingerprint (not just raw adapter checkpoint), the scalar rating, forced-choice outcomes with state IDs, and eval-awareness marker flags.
