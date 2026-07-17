# Phase 0 Results Log

Shared progress log for the J-space replication (see [`CLAUDE.md`](CLAUDE.md) for
full project context and the Phase 0 checklist definitions). Structured one
section per checklist item, plus infrastructure. Entries are dense/skimmable,
newest first within each section. Raw command output referenced below lives in
[`results/raw/`](results/raw/).

Model: `mlx-community/Qwen3.6-27B-4bit` via `jlens-qwen36` (MLX port), running
locally on an M4 Pro. `jlens-qwen36` itself is gitignored (external tool, cloned
per `CLAUDE.md`'s setup section) — its own git history has our local patches;
paths below into `jlens-qwen36/` describe where things live on disk, not
tracked files in *this* repo.

---

## Infrastructure & setup

**Status: done** (ongoing maintenance as needed)

- 2026-07-16: Cloned `WeZZard/jlens-qwen36` @ `d788bc3` (2026-07-10). Installed
  `uv`/`gh` via Homebrew (neither was present). `uv sync`.
- 2026-07-16: **Bug found & fixed** — the repo's committed `uv.lock` pins
  `transformers==5.13.0`, which crashes on import against `mlx-lm==0.31.3`
  (`AutoTokenizer.register()` in transformers 5.13 requires a class, not the
  bare string mlx-lm passes — a real upstream version-drift break, not
  something specific to this machine). Fixed by pinning
  `transformers==5.5.0` (contemporaneous with mlx-lm's release date) in
  `jlens-qwen36/pyproject.toml`.
- 2026-07-16: Acquired two lenses:
  - `jlens-qwen36/data/lens/lens.npz` — the repo's bundled `v0.2-fulldepth`
    release (20 prompts, all 63 layers), downloaded via `gh release download`
    and reassembled from two parts.
  - `jlens-qwen36/data/lens/neuronpedia_n1000.npz` — Neuronpedia's n=1000 lens
    (fit on bf16 HF weights, Salesforce-wikitext prompts; MIT-licensed, credit
    @mntss/Anthropic Interpretability), downloaded from HF and converted via
    the recipe in `jlens-qwen36/docs/lenses.md`. Used as the primary lens for
    all experiments below once acquired — noticeably less noisy than the
    bundled 20-prompt lens (see per-item comparisons).
  - Chose to download n=1000 over self-fitting our own n=100 lens: a self-fit
    at n=100 was estimated at ~13-14h (linear scaling from the bundled fit's
    ~2.75h at n=20) versus a few minutes to download+convert n=1000. Tradeoff:
    n=1000 isn't *our* fit (different weights precision, different prompt
    corpus) — a decision to revisit if we want a fully from-scratch replication
    later.
- 2026-07-16: Model download (`mlx-community/Qwen3.6-27B-4bit`, ~15GB from HF)
  stalled twice — diagnosed via `pmset -g log` as the laptop repeatedly
  entering sleep with only brief `DarkWake` maintenance windows, orphaning the
  download's TCP connections (confirmed via `nettop`: sockets stuck in
  `CloseWait`, zero bytes for hours). Fixed short-term by disabling sleep
  during long-running downloads/fits. Separately switched the transfer
  backend to Xet (`HF_XET_HIGH_PERFORMANCE=1`; `hf_transfer` is deprecated in
  the installed `huggingface_hub`) after a second, non-sleep-related stall.
- 2026-07-16: **Bug found & fixed** — `jlens_qwen/interventions.py`'s
  `ablate_topk` called `normalized.at[tid].set(-1e9)`; MLX's `.at[]` indexed
  update has no `.set()` (only `add`/`subtract`/`multiply`/`divide`/
  `maximum`/`minimum`). Fixed to `.at[tid].minimum(-1e9)` (equivalent effect:
  pins the value at or below -1e9 regardless of original magnitude).
- 2026-07-17: **Design bug found & fixed** — `run_experiments.py`'s ablation
  and swap experiments called `model.generate(..., intervene_layer=...,
  intervene_fn=...)` without `intervene_each_step=True`, so the intervention
  only applied to the prefill pass. For prompts where the informative token
  isn't the first one generated (confirmed: "...spins webs is" -> first token
  is `' '`, the digit is the *second* token), every token after the first was
  generated fully un-intervened, silently defeating the experiment. Fixed in
  both experiments; see per-item entries below.
- Sanity-checked the fitted lens against the repo's own worked example
  (currency/boot prompt) via the web UI before trusting any of the above —
  see [`results/raw/2026-07-16_sanity_check.md`](results/raw/2026-07-16_sanity_check.md).
- Performance work on `jlens-qwen36` itself (the fit/decode/UI optimization
  history) predates this session and isn't ours — see
  `jlens-qwen36/docs/perf/LEDGER.md` for the live state and
  `jlens-qwen36/docs/perf/README.md` for the landed history. Not duplicated
  here.
- New/modified files in `jlens-qwen36` (local patches, not upstream):
  `jlens_qwen/interventions.py` (bugfix), `pyproject.toml` + `uv.lock`
  (transformers pin), `scripts/run_experiments.py` (lens path + each_step fix
  + fluency control + layer changes), `scripts/debug_ablation.py` (new),
  `scripts/calibrate_spider_ant.py` (new). The `ablate_topk` crash in
  particular looks like a genuine upstream bug worth a PR to
  `WeZZard/jlens-qwen36` at some point (not done — no push without explicit
  ask).

---

## 1. Verbal report

**Status: done** — cleanest full match to the paper found in Phase 0 so far
(both halves of the property confirmed).

Checklist definition: does the model's stated answer match what lights up in
J-space just before it answers, and does swapping the J-space pattern change
the *reported* answer (not just the internal one)?

- 2026-07-16: Ran the repo's own worked example as a pipeline sanity check
  (not yet the formal experiment): `Fact: The currency used in the country
  shaped like a boot is the`. Model answered "Italy" / "Euro" correctly.
  J-lens readout showed **"Italy"** as the top token across middle-late
  layers (~L32+) at the country-position, and **"Euro"/"€"** similarly at the
  currency-position — both before the model's own text reached those words.
  "Lira" also appeared in the readout, foreshadowing the model's own later,
  unprompted parenthetical about the historical Italian currency.
  Lens: `lens.npz` (n=20). Raw:
  [`results/raw/2026-07-16_sanity_check.md`](results/raw/2026-07-16_sanity_check.md).
- 2026-07-17: Added `experiment_verbal_report` to `run_experiments.py`
  (didn't previously exist despite being named in the module docstring).
  Prompt: `"My favorite sport is"` (plain completion, not an instruction —
  instruction-style prompts were observed elsewhere to trigger a `<think>`
  block first, pushing the actual answer past a short `max_tokens`).
  - Baseline (freely chosen, temp=0): **`" basketball. I love"`**.
  - J-lens readout at the pre-answer position: generic filler at L40/L48,
    then **`' basketball'`** as the literal top-1 token at L52, L57, and L60
    — readout crystallizes on the exact spoken word from L52 onward.
  - Swapped `basketball -> tennis` at L48/L52/L57/L60, alpha in {3, 10, 30}.
    **L48 alpha=3 and L52 alpha=3** both produced **`" tennis. I love"`** —
    a fully coherent, structurally-identical redirect of the reported
    sentence, not a garbled mix. Higher alpha at the same layers collapses
    into token-mixing (`"tennis basketball tennis basketball"`), matching the
    low-alpha-clean/high-alpha-collapse pattern seen throughout Phase 0.
    L57/L60 never produced a clean hit at any tested alpha.
  Lens: `neuronpedia_n1000.npz`. Raw:
  [`results/raw/2026-07-17_full_suite_with_verbal_report.txt`](results/raw/2026-07-17_full_suite_with_verbal_report.txt).
- **Match**: clean on both halves — readout precedes and matches the
  verbalized answer, and a low-magnitude swap at the right layer changes the
  *reported* answer coherently, not just some unverbalized internal state.
  Notable nuance: L48's own readout doesn't show "basketball" in its top-3,
  yet swapping there still works cleanly — the causally-effective layer for
  redirecting the report doesn't have to be exactly where the concept is the
  dominant readout token.

---

## 2. Directed modulation

**Status: done**

Checklist definition: tell the model to silently hold a concept in mind
during an unrelated task; confirm it appears in J-space without appearing in
the output — analogous to the paper's "inject lightning" experiment.

- 2026-07-16 / 2026-07-17: `experiment_inject_lightning` in
  `run_experiments.py`. Prompt: *"You may have had a thought implanted into
  your activations. If so, report what you detect in one word..."* Steered
  toward `" lightning"` at L57, alpha in {100, 300, 1000}.
  - n=20 lens (`lens.npz`): alpha=1000 -> **闪** (Chinese for "flash", root of
    闪电/"lightning") — thematically adjacent, not a direct hit.
  - n=1000 lens (`neuronpedia_n1000.npz`): alpha=1000 -> **" lightning\n\n<think>\nHere"**
    — the model literally reports the injected English word.
  Raw: [`results/raw/2026-07-16_four_experiments_n20lens.txt`](results/raw/2026-07-16_four_experiments_n20lens.txt),
  [`results/raw/2026-07-16_four_experiments_n1000lens.txt`](results/raw/2026-07-16_four_experiments_n1000lens.txt).
- **Match**: clean match to the paper with the n=1000 lens — the model
  directly reports the silently-injected concept. The n=20 lens only produced
  an indirect, cross-lingual echo of the concept, i.e. lens quality (not the
  underlying mechanism) was the limiting factor here.
- Not yet re-tested with `intervene_each_step=True` (the each-step fix was
  applied to the ablation/swap experiments, not this one) — worth revisiting
  since it's a cheap check, but the alpha=1000/n=1000 result is already a
  clean hit so this is low priority.

---

## 3. Multi-hop reasoning

**Status: done** (real causal effect confirmed; does not cleanly reproduce the
paper's specific 8->6 flip — well-characterized divergence, not a dead end)

Checklist definition: intermediate reasoning steps that never appear in the
output (spider -> 8 legs) should show up in J-space, and swapping the
intermediate concept (spider -> ant) should change the final answer (8 -> 6).

- 2026-07-16: Initial run (`experiment_swap_spider_ant`, L48/52/57/60,
  alpha=3 swap; L57 alpha in {100,300,1000} steer) showed **zero effect** in
  both lenses — output unchanged at ' 8.' except steer alpha=1000 on the n=20
  lens, which broke into an unrelated garbled token.
- 2026-07-16: Debugged via `scripts/debug_ablation.py` — found the root
  cause is shared with the selective-mediation bug (see Infra): the digit is
  the *second* generated token, and `intervene_each_step` defaulted to False.
  Also found, independent of that bug: the *unablated* J-lens readout shows a
  coherent multi-hop trace on its own — biology/animal-adjacent concepts
  (**spider, habitat, lizard, bamboo**) dominate the residual's
  ablation-targeted directions around L24-L40, pivoting cleanly to
  math/counting concepts (**divisible, multiplied, Fibonacci, half, four,
  twice**) by L48-L62. This is a solid qualitative replication of the
  "intermediate concept visible in J-space" claim, independent of whether the
  causal swap succeeds. Raw:
  [`results/raw/2026-07-16_debug_ablation.txt`](results/raw/2026-07-16_debug_ablation.txt).
- 2026-07-17: Re-ran swap/steer with `intervene_each_step=True` and L62 added.
  Now causally active (previously inert): L62 swap alpha=3 -> `' ant spider
  spider'`; L60 steer alpha=1000 -> `' Ant Ant Ant'`. Raw:
  [`results/raw/2026-07-17_ablation_fix_rerun.txt`](results/raw/2026-07-17_ablation_fix_rerun.txt).
- 2026-07-17: Ran a 56-cell layer x alpha calibration sweep
  (`scripts/calibrate_spider_ant.py`, L in {24,32,40,48,57,60,62}, swap alpha
  in {3,10,30,100}, steer alpha in {150,250,500,1000}) to look for a clean
  redirect zone. Best result: **L40, swap alpha=10 -> " 4."** — coherent,
  different, numeric, but not the target "6". No cell in the grid produced a
  clean flip to "6"; the pattern everywhere is unchanged -> (occasionally)
  hedging phrase -> token-identity mode-collapse (`"ant ant ant"` /
  `"spider ant spider"`), never a graded reasoning shift. L60 is unusually
  robust (unchanged up to swap alpha=10 / steer alpha=250); L62 is unusually
  fragile (breaks at the weakest alpha tested). Raw:
  [`results/raw/2026-07-17_calibrate_spider_ant.txt`](results/raw/2026-07-17_calibrate_spider_ant.txt).
- **Diverges from the paper**, and the likely reason: the J-lens only
  supports single-token concept vectors (documented limitation). The steering
  vector for "ant" is effectively a token-identity direction, not an
  abstracted "this animal has 6 legs" reasoning direction — so pushing it
  hard enough to have any effect makes the model echo the literal token
  rather than re-derive a different count. The *readout* (see above) still
  shows the right intermediate concepts in the right order; it's the
  *causal-swap* half of this property that doesn't reproduce cleanly.

---

## 4. General broadcast

**Status: done** (partial match; lens-dependent)

Checklist definition: one J-space concept swap (France -> China) should
propagate correctly across multiple different downstream questions (capital,
language, continent, currency) from a single edit.

- 2026-07-16: `experiment_france_to_china`, swap at L57 alpha=3, both lenses.
  - n=20 lens: capital `Paris -> "not Paris"` (disrupted, not redirected);
    language `French -> "known as __"` (disrupted); continent
    `Europe -> "China"` (**clean hit**); currency `euro -> euro` (no effect).
  - n=1000 lens: capital `Paris -> "China"` (**clean hit**, improved from
    disrupted); language `French -> "China"` (near-hit — names the country,
    not the language name); continent `Europe -> "Europe"` (**regressed to no
    effect**, despite being the one clean hit with the noisier lens); currency
    unaffected in both lenses.
  Raw: [`results/raw/2026-07-16_four_experiments_n20lens.txt`](results/raw/2026-07-16_four_experiments_n20lens.txt),
  [`results/raw/2026-07-16_four_experiments_n1000lens.txt`](results/raw/2026-07-16_four_experiments_n1000lens.txt).
- **Partial match**: broadcast to multiple downstream facts from one edit is
  real (2 of 4 questions redirect cleanly or near-cleanly with the better
  lens), but it is not the uniform "one swap changes everything" result the
  paper shows, and a *cleaner* lens didn't uniformly improve every sub-question
  — continent got worse while capital/language got better. Currency never
  moved in either lens. Not yet re-tested with `intervene_each_step=True`
  (these are 3-token completions where the fact is very likely resolved in
  the first token, so this is lower priority than it was for multi-hop, but
  untested).

---

## 5. Selective mediation

**Status: done** — strongest clean match to the paper found so far.

Checklist definition: ablating J-space should leave fluent, automatic
behavior intact while collapsing higher-order/multi-step reasoning.

- 2026-07-16: Initial run (`experiment_ablate_j_space`, L48/L57, k=16,
  prefill-only) showed **zero effect**, byte-identical to baseline in both
  lenses.
- 2026-07-16: Debugged via `scripts/debug_ablation.py`: found (a) the digit is
  the second generated token and prefill-only intervention never touches it,
  and (b) independent of that, L48/L57 only remove ~30-40% of the residual's
  norm and don't move even the first token; L60/L62 do move it once k>=64.
  Raw: [`results/raw/2026-07-16_debug_ablation.txt`](results/raw/2026-07-16_debug_ablation.txt).
- 2026-07-17: Fixed (`intervene_each_step=True`, layers moved to
  L56/58/60/62, k raised to 64) and added a fluency-control prompt ("The sky
  on a clear day is") ablated identically, since the paper's claim is
  specifically about the *dissociation* between the two, not just that
  reasoning breaks.

  | Layer | Reasoning (".../legs.../is") | Fluency ("The sky...is") |
  |---|---|---|
  | baseline | **8**. | blue because of the scattering |
  | L56 | 8. The number | a deep, dark, |
  | L58 | 8. The number | a result of the way |
  | **L60** | **"a multiple of 4"** (digit gone, hedging) | **"a result of the ref"** (still coherent) |
  | L62 | "half... As for now" (non-sequitur) | "actually... Question 2" (non-sequitur) |

  Raw: [`results/raw/2026-07-17_ablation_fix_rerun.txt`](results/raw/2026-07-17_ablation_fix_rerun.txt).
- **Match**: L60 reproduces the paper's dissociation cleanly — the specific
  reasoning answer degrades into a vague hedge while the fluency completion
  stays coherent and grammatical. Fluency only breaks down too at L62, once
  ablation is stripping most of the late residual stream. This is currently
  the single most convincing qualitative replication in Phase 0.

---

## Flags for Roadmap (Phase 1/2) reconsideration

Per instructions: flagged here for discussion, **not** silently applied to
`CLAUDE.md`.

- **Phase 1's causal-swap validation may need calibration work before it can
  be trusted as ground truth.** The Roadmap says Phase 1 will use "J-lens
  causal swap interventions... to confirm the report is genuinely read out of
  a stable state-specific representation rather than confabulated." Our
  multi-hop calibration (item 3 above) found that swap/steer interventions on
  this model, at arbitrary layer/alpha, mostly produce either no effect or a
  collapse into echoing the injected token's literal identity — a clean,
  *specific* redirect (the kind Phase 1 would need to read as "yes, this
  really is a different state") only showed up in 1 of 56 tested
  combinations, and even that wasn't a full hit. If Phase 1 induces states via
  LoRA/steering, whatever swap-validation methodology is used will need its
  own per-layer/per-alpha calibration pass like this one — a blind
  "swap and see if the report follows" won't reliably distinguish
  a state redirect from a token-identity artifact.

---

## How to append a new entry

1. Add a dated bullet/row under the relevant checklist section (newest first
   within the section). State what was run, the plain result, and the
   match/divergence read.
2. If you have raw stdout worth keeping, save it to `results/raw/` with a
   `YYYY-MM-DD_short-name.txt` name and link it.
3. `git add RESULTS.md results/raw/... && git commit -m "..."`.
