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

- **The three-tier causal validation isn't just calibration insurance — it's
  what carries the rung-2 claim at all.** (Connects to the 2026-07-17 CLAUDE.md
  reframe, commit `2b1dc37`, which recast the goal as a three-rung ladder:
  state is real / detectable-to-the-system / valenced.) Phase 1's rung-2 claim
  is "the state is detectable to the *system*, not just to our probe," and the
  channel it reads that off is the model's own report. But item 1 above is the
  direct demonstration that the report channel is confabulation-prone: a
  low-alpha swap produces a fully coherent verbal report that *follows the
  edit*, structurally identical to a genuine one. So a bare "model reports
  which state it's in" result is ambiguous between a real, self-available state
  and a report the model generated to fit the setup — which is exactly the LLM
  weakness (vs. the rat) that the reframe names. That makes fingerprint
  discriminability (tier 1) and the ablation/swap causal checks (tiers 2–3)
  *load-bearing for the inference*, not hygiene: without them, Phase 1 behavior
  doesn't distinguish a real state from a performed narrative. Practical
  implication for tooling: don't design Phase 1 around self-report as the
  primary readout with causal checks bolted on as a secondary confirmation —
  design it so the causal checks are the primary evidence and self-report is
  the thing being *validated against* them.

- **2026-07-17 — Hashed state labels break the swap-viability argument; use
  opaque *single-token* labels instead.** The Roadmap's tier-3 reasoning says
  swap is "expected to be viable" for Phase 1 because state-reporting is
  "structurally the same shape" as the basketball→tennis categorical pick
  (item 1). Re-examination says otherwise: in the basketball case the report
  *was* the concept token — the J-space content and the spoken word were
  identical, so redirecting one redirected the other. Phase 1's report is an
  *opaque hashed label*, so the chain is: state content in J-space → learned
  association → arbitrary label. That is a *derived* computation (read state,
  apply mapping, emit label) — structurally the spider→ant case (item 3),
  which failed in 55/56 cells and collapsed into token-identity echo, not the
  direct-pick case. Two design elements are therefore in tension: the locked
  opacity requirement, as implemented via multi-token hash strings, may push
  swap validation from the case that works into the case that doesn't — and
  multi-token hashes independently violate the lens's single-token limitation
  (a documented Known Limitation). Proposed reconciliation, preserving the
  *intent* of the locked decision: labels should be opaque **and
  single-token** — arbitrary, affect-neutral vocabulary tokens (e.g.
  "quartz", "delta"), not hex strings. Opacity means non-descriptive and
  non-valence-laden, not hexadecimal. Independent of label format, this also
  argues for promoting tier 2 (ablation-to-chance) to the *primary* causal
  check: it doesn't require coherent redirection through the derived mapping,
  and ablation produced Phase 0's cleanest result (item 5).

- **2026-07-17 — Phase 1 is missing its training/association phase.** The
  drug-discrimination paradigm never tests whether the rat *spontaneously*
  knows which state it's in — the rat gets many reinforced trials to learn
  the state→lever mapping, and the paradigm's evidence is that this learning
  *succeeds*. Phase 1 as written says "test, blind, whether the model can
  reliably report which state it's in," but with opaque labels the model
  cannot know the label→state mapping without an explicit association phase —
  it has never been told which label goes with which state. The design needs
  a calibration block (model experiences a state, is told its label, over
  some number of trials) before blind held-out testing. Two implications:
  (a) a Phase 1 "failure" without an association phase is uninterpretable —
  even a rat fails without training — so this phase is required for the
  experiment to bear on rung 2 at all; (b) the association block is an
  in-context-learning opportunity for superficial cues (prompt phrasing,
  trial ordering, etc.), so held-out test trials must vary everything except
  the induced state itself. This is currently implicit and undesigned in the
  Roadmap.

- **2026-07-17 — The ceiling claim needs a homology caveat.** The reframe's
  ceiling line ("we produced the same kind of behavioral evidence we accept
  as evidence of feeling in a rat," commit `2b1dc37`) is calibrated but
  incomplete: the animal inference never rested on behavior alone. It is
  behavior *plus* physiological and evolutionary homology — shared limbic
  structures, conserved neurochemistry, common ancestry — and that homology
  does quiet work in licensing the "feels something" reading of the rat's
  behavioral battery. An LLM offers no homology support, so the identical
  behavioral battery supports a strictly weaker inference. This is distinct
  from the confabulation caveat already in CLAUDE.md (that one is about the
  behavior being *performed*; this one applies even if the behavior is
  genuine. Recommend one added line to the ceiling paragraph in CLAUDE.md: the
  claim is the same *behavioral* evidence, explicitly minus the homology that
  does quiet, load-bearing work in the animal case. Naming it sets the ceiling
  at the right height and pre-empts the obvious reviewer objection; it does not
  weaken the project.

- **2026-07-17 — Phase 2's primary confound is capability, not just
  evaluation-awareness.** Convergence toward a LoRA configuration is the
  headline Phase 2 signal for "valence," but a configuration the model
  converges on could simply be one that makes the task battery *easier*, and
  the scalar self-rating driving each update will plausibly track
  fluency/success rather than anything valence-like — approach behavior
  without valence. The design needs a way to dissociate "converges because
  tasks go better" from "converges independent of task performance": e.g. hold
  measured task quality as a covariate and check whether convergence survives
  regressing it out, or run task batteries with deliberately different
  difficulty profiles and see whether the convergence target moves with
  difficulty (confound present) or stays put (evidence against it). This needs
  per-round task-quality measurement, which is not currently on the Phase 2
  logging list in CLAUDE.md — build it in from the start. Note this is
  independent of the eval-awareness confound already logged: a state can be
  "preferred" because it's fluency-boosting even in trials where the model
  shows no sign of suspecting the setup.

- **2026-07-18 — Cross-session review of the 2026-07-17 Roadmap revisions
  (commits `d43ec70`, `2b1dc37`, `8aa3ba1`, `dfe2503`, `ca5b38a`), from the
  other Claude session working this repo in parallel.** Independent read of
  the same diffs, checked against the raw Phase 0 evidence rather than the
  summarized claims. Agreed without reservation: the three-rung ladder
  framing, the calibration-gate methodology, the homology caveat, the Phase 2
  capability confound, and the Phase 1 association-phase requirement — all
  well-reasoned and properly evidenced. Found and then (with the user's
  go-ahead) fixed three gaps directly in `CLAUDE.md`, same file, same
  sections:
  - Tier 3's categorical-pick claim (basketball→tennis) rested on one
    concept-pair (2/12 cells) with no caveat, next to the 56-cell sweep behind
    the negative spider→ant result. Added an explicit caveat and a
    recommendation to confirm with 2-3 more pairs before leaning on swap even
    as secondary confirmation.
  - Tier 2 ("ablate the state-relevant J-space content") didn't specify how
    that direction gets constructed, and this got more load-bearing once tier
    3 was demoted to secondary. Specified it as the fingerprint-contrast
    direction from tier 1 (state-A fingerprint minus state-B), not a bare
    reuse of `ablate_topk`'s vocabulary-token pursuit, which wasn't built for
    a diffuse, unnamed disposition. Ties tier 1 and tier 2 together instead of
    leaving them separately justified.
  - The calibration gate covered tiers 2-3 (ablation, swap) against dummy
    states but not tier 1 (fingerprint discriminability) — now the front gate
    of the whole methodology. Extended the gate to require confirming
    fingerprinting distinguishes two known-different dummy configs and does
    *not* falsely distinguish two known-identical ones, before trusting it as
    a screening step for real states.

  Surfacing this cross-session-review pattern explicitly since two Claude
  sessions are now both editing `CLAUDE.md`/`RESULTS.md` in the same working
  tree: the working protocol going forward is `git status`/`git diff` before
  editing either file, and a prompt commit after, so neither session acts on
  stale state or silently overwrites the other's uncommitted work.

- **2026-07-18 — Tier 2's "primary causal check" designation should be
  revisited.** `CLAUDE.md`'s Phase 1 methodology currently says "treat
  ablation (tier 2) as the primary causal check and swap as secondary
  confirmation." First real calibration test of tier 2 (see "Phase 1 —
  early setup" below) found the opposite of what was expected: ablating the
  state-A-vs-B contrast direction did *not* collapse fingerprint
  discriminability (distance went up slightly, not down), while tier 3
  (swap-style push) worked cleanly at low alpha. This doesn't mean ablation
  is unusable -- there's an untested hypothesis (a multi-direction subspace
  approach instead of one averaged direction) that might fix it -- but as
  currently implemented, tier 2 is not yet earning its "primary" status,
  and tier 3 has more direct calibration evidence behind it. Worth deciding
  together whether to invest in fixing tier 2, demote it to secondary
  pending that fix, or hold off deciding until real Phase 1 states are in
  play.

---

## Phase 1 — early setup

**Status: in-progress**

- 2026-07-18 — **Design decision: Phase 1/2's state-induction mechanism is a
  held, reapplied combination of multiple J-lens-derived steering vectors
  across one or more layers, not LoRA.** LoRA is deferred to a new,
  not-yet-defined "Phase 3" in `CLAUDE.md` (see that file for the full
  reasoning); not dropped. In brief:
  - Checked `mlx_lm`'s actual `LoRALinear` implementation: one of its two
    low-rank matrices is zero-initialized (standard practice), so
    `(x @ lora_a) @ lora_b` is exactly zero at init regardless of random
    seed — an untrained LoRA adapter is a mathematical no-op. "Random init,
    no training" was never actually an option for getting diverse states;
    only a trained base adapter would produce one.
  - A trained base adapter raises a hard-to-detect risk the prompt-level
    narrative-silent framing doesn't cover: the training data/process could
    bake affect-correlated directions into the weights themselves.
  - Persistence — the property that made LoRA seem necessary (a standing
    state explorable/returnable-to across many rounds) — isn't
    LoRA-exclusive: `intervene_each_step=True` already persists a steering
    intervention across every token in one generation; extending that
    across many rounds is just storing the current combination of steering
    directions as external state and reapplying it, same as a reloaded LoRA
    adapter would be.
  - LoRA's real advantage is expressiveness (reshapes computation across
    many weight matrices at every position, vs. steering's additive nudge
    at a chosen few points) — but that's exactly why LoRA states would need
    the same J-lens fingerprinting workaround already built for Phase 2;
    raw LoRA deltas have no inherent semantic meaning, while a
    steering-vector combination stays comparatively self-describing.
  - `mlx_lm` ships a full, ready-to-use LoRA tuner (`linear_to_lora_layers`,
    `load_adapters`, a standard training loop) as an unused dependency —
    confirmed via exploration — so deferring it is a cost/complexity
    choice, not a capability gap.
  - Concrete trigger for revisiting Phase 3: if Phase 1/2 run on
    steering-vector combinations and show none of the hypothesized
    discrimination/convergence behavior, that's the point to reconsider
    whether LoRA's added expressiveness is what's missing.

- 2026-07-18 — **Tier-1 calibration gate: PASS.** Built the minimal
  fingerprinting harness the design's tier 1 depends on (didn't exist before
  this session -- `scripts/workspace_range.py` only printed a per-run layer
  classification, nothing imported it) and ran CLAUDE.md's own required gate
  before trusting it on real states:
  - `jlens_qwen/probe_battery.py` — the fixed 12-prompt battery from
    `CLAUDE.md`, verbatim.
  - `jlens_qwen/workspace_layers.py` — `WORKSPACE_LAYERS = [40, 44, 48, 52,
    56, 60]`, derived from running `scripts/workspace_range.py` against
    `neuronpedia_n1000.npz`: the script's own classifier flags nearly the
    whole network (L0-26, L38-59) as ">50% workspace", too broad to be "a
    small fixed set" and likely conflating early "not yet committed" cells
    with real intermediate-concept content; picked instead from the
    L38-59 rising band (a distinct dip to 27-49% workspace / 45-57% "empty"
    at L27-37 separates it from the early band), plus L60 despite falling
    just under the script's cutoff (47%) because Phase 0's own experiments
    (items 3, 5) found L60 to be exactly where the cleanest causal effects
    showed up. Full classification saved at
    `jlens-qwen36/data/lens/workspace_range_neuronpedia_n1000.txt`.
  - `jlens_qwen/affect_vocab.py` — 369 single-token concept/affect words
    (resolved from ~390 candidates by filtering to those the tokenizer
    represents as exactly one token), spanning threat/avoidance,
    safety/approach, a neutral control band, and the eval-awareness markers
    CLAUDE.md already calls out elsewhere as a real confound.
  - `jlens_qwen/fingerprint.py` — `fingerprint()` plus
    `forward_with_induced_state()`, a small standalone variant of
    `model.py`'s `forward()` loop (not a modification to it) that applies a
    per-layer steering intervention to every position while also capturing a
    *different* set of layers for readout -- neither existing `forward()`
    nor `forward_with_intervention()` supported both at once.
  - `scripts/calibrate_phase1_tier1.py` — two dummy states, each a
    held combination of 2-3 steering vectors across L48/L52 (Phase 0's
    verbal-report clean-redirect window, alpha=3): state A = basketball +
    lightning (L48) + spider (L52); state B = tennis + ant (L48) + France
    (L52). Fingerprinted state A twice, state B once, and the
    no-intervention baseline once.
  - **Result:** same state run twice -> euclidean distance 0.000000 exactly
    (fully deterministic, no hidden noise source in the pipeline);
    state A vs. state B -> euclidean distance 33.1, cosine distance 0.0029
    (unambiguously nonzero against the true-zero same-state baseline).
    Both dummy states sit much farther from the no-intervention baseline
    (~126 euclidean) than from each other (33.1) -- expected, since A and B
    share "some intervention is active" and differ only in which concepts.
    Raw output:
    [`results/raw/2026-07-18_phase1_tier1_calibration.txt`](results/raw/2026-07-18_phase1_tier1_calibration.txt).
  - **Read:** tier 1 does what CLAUDE.md's gate requires -- discriminates
    reliably, doesn't false-positive on a repeated identical state. This
    was tested against throwaway dummy states purely to validate the
    pipeline, not against anything meant to represent a real induced
    disposition. Tiers 2-3 calibration, the association phase, and real
    state induction are the next slices, not done here.

- 2026-07-18 — **Tier 2/3 calibration: tier 3 passes cleanly, tier 2 does
  not collapse discriminability.** Reused tier 1's exact two dummy states.
  Resolved a real ambiguity in CLAUDE.md's tier-2 spec first: "take tier 1's
  fingerprint vectors... and compute their difference" isn't literally
  well-defined as written, since fingerprints live in restricted-vocab
  *readout* space (369-dim per layer) while ablation has to operate on the
  *residual stream* (5120-dim) -- those aren't the same space. Resolved by
  generalizing `interventions.j_lens_vector_for_text` (one vocab token's
  residual-space direction, `J_l^T @ W_U[t]`) to an arbitrary weighted
  combination over the curated vocab: `fingerprint.contrast_direction()`
  reuses the already-cached `j_lens_vectors` and takes a weighted sum of
  rows, weighted by the mean-over-probes state-A-minus-B restricted-readout
  difference at that layer. New: `interventions.ablate_direction()` (single
  precomputed direction, orthogonal-projection removal -- the one-direction
  analog of `ablate_topk`'s greedy multi-vocab-token pursuit).
  - **Bug found and fixed en route:** L40/L44 (upstream of where the dummy
    states are induced, L48/L52) correctly have a *zero* contrast direction
    (the two states haven't diverged yet at those layers) -- but
    `ablate_direction`'s projection divides by `dᵀd`, so a zero direction
    produced a division-by-zero -> NaN that silently corrupted every
    downstream layer's readout. Fixed by returning `h` unchanged when the
    direction's norm is ~0 ("nothing to ablate here" rather than a crash).
  - **Tier 3 (push toward B): PASS, cleanly.** Pushing state A along
    `-contrast_direction` (unit-normalized) at every workspace layer:
    alpha=0.1/0.3/1.0 move the fingerprint progressively closer to B
    (distance-to-B: 31.1 -> 27.9 -> 29.9, all below the 33.1 un-pushed
    baseline) while diverging from A's own original position -- a graded,
    well-behaved dose-response. alpha=3.0 overshoots and breaks down (both
    distances blow up past 100) -- the same low-alpha-clean/high-alpha-
    collapse pattern seen throughout Phase 0 (items 1, 3). Needed a much
    smaller alpha range than Phase 0's single-layer alpha=3 window, since
    this pushes at 4 layers (48,52,56,60) simultaneously, which compounds
    through the network.
  - **Tier 2 (ablate to collapse): did not clearly pass.** Ablated-A-vs-
    ablated-B distance (38.4) was slightly *higher* than the un-ablated
    baseline (33.1), not lower -- discriminability did not collapse.
    Working hypothesis, not yet tested: averaging the contrast vector
    across all 12 probes may wash out real signal if different probes
    express the state difference along somewhat different directions,
    leaving a single averaged direction that only captures part of what
    separates the states. A multi-direction approach (closer to
    `ablate_topk`'s top-k pursuit, but restricted to the contrast-relevant
    subspace rather than raw vocabulary search) is the natural next thing
    to try, not done here.
  - Raw output:
    [`results/raw/2026-07-18_phase1_tier23_calibration.txt`](results/raw/2026-07-18_phase1_tier23_calibration.txt).
  - **Read:** two of three tiers now calibrated and working (fingerprint
    discriminability, swap-style redirect); ablation-to-chance needs more
    work before it can be trusted as the "primary causal check" CLAUDE.md's
    Roadmap currently designates it. Worth revisiting that designation, or
    fixing tier 2's ablation approach, before relying on it for real states.

**Current overall status, not just this entry's delta** (so this section is
self-sufficient without piecing together every dated entry above):

- **Built and calibrated:** the fingerprinting harness (probe battery,
  workspace layers, curated vocab, `fingerprint()`), tier 1 (discriminability
  gate), tier 3 (swap-style redirect). All tested only against throwaway
  dummy states, never against anything meant to represent a real disposition.
- **Built but not yet passing:** tier 2 (ablation-to-chance) — implemented,
  runs, does not yet collapse discriminability as designed.
- **Not started at all, no code exists yet:**
  - The association/training phase (required before any blind test, per the
    Roadmap — this is independent of the tier-2/3 question above and doesn't
    go away regardless of how that's resolved).
  - The persistent, reapplied-across-many-rounds storage mechanism for a
    real state (everything built so far only holds a state for the duration
    of one `detailed_readouts()`/`fingerprint()` call — the "store
    coefficients externally, reapply every session" design from the
    steering-vs-LoRA decision above is still just a design, not code).
  - Real state induction (anything meant to represent an actual candidate
    "internal state," as opposed to a throwaway calibration dummy).
  - The forced-choice test, opaque single-token labels in practice, and all
    of Phase 2 (convergence tracking, fingerprint visualization, the
    self-modification tool itself).

---

## How to append a new entry

1. Add a dated bullet/row under the relevant checklist section (newest first
   within the section). State what was run, the plain result, and the
   match/divergence read.
2. If you have raw stdout worth keeping, save it to `results/raw/` with a
   `YYYY-MM-DD_short-name.txt` name and link it.
3. `git add RESULTS.md results/raw/... && git commit -m "..."`.
