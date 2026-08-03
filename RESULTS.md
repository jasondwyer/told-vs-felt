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

- **2026-07-18 — The behavioral-influence gate needs to test *pervasiveness
  across domains*, not just "separable at all," and must control for thinking
  mode.** `CLAUDE.md`'s cheap-proxy gate item 2 asks whether induced-state
  outputs are "separable at all." The first real run of it (see "Phase 1 —
  early setup" below) suggests that framing is too weak in one direction and
  under-specified in another:
  - *Too weak:* the tier-1 dummy states move behavior clearly on
    *concept-relevant* prompts (basketball→tennis) but appear near-inert on
    concept-*irrelevant* open-ended ones. Convergence-as-designed assumes a
    held state exerts influence across a *battery of varied mundane tasks*; a
    state whose behavioral influence — and thus the rating that tracks it — is
    just a function of task/concept overlap would give "convergence" that's
    really task-composition, not disposition. So the real-state gate should
    measure *cross-domain pervasiveness* (does influence show up on tasks that
    don't touch the state's concepts?), not merely A≠B somewhere. This is
    adjacent to, but distinct from, the capability/fluency double-dissociation
    already in the roadmap: that one asks whether convergence tracks task-ease;
    this asks whether influence is domain-general at all.
  - *Under-specified:* instruction-style prompts trigger Qwen's thinking mode
    (`<think>…`), whose scaffold is state-insensitive and eats the measurement
    window — so a first-token/short-generation separability metric *understates*
    influence on exactly the open-ended prompts meant to reveal it. The gate's
    battery should be *completion*-style (thinking-clean), or explicitly
    generate through `</think>` to the answer, or run with `enable_thinking:
    False`. (Ties to the architecture note in `CLAUDE.md` that thinking mode is
    a second, visible channel to decide about per-experiment.)
  - Neither point blocks anything now — it's a spec refinement for when the
    behavioral check is run against *real* candidate states rather than the
    pipeline-validation dummies.

- **2026-07-19 — Phase 3 (LoRA) reconsideration trigger has been reached: both
  rung-3 measurement channels fail on steering-vector states, and the failures
  trace to the same root cause (steering influence is weak + local).**
  *[Resolved 2026-08-01 → the trigger was answered with a redesign, not a LoRA
  pivot: non-semantic states + strain axis + tie-construction/cost + drug-free
  conditioned forced choice, with LoRA un-deferred only for conditioning. See
  CLAUDE.md's "2026-08-01 — Pivot".]* The
  convergent evidence: the scalar rating is flat and basis-agnostic (rating-
  gradient + SPSA + basis diagnostic), and the forced-choice channel is flat
  because steering bias on option-passage tokens does not propagate to the
  choice position (forced-choice probe, mechanism positive control passing). The
  root cause is the property `CLAUDE.md`'s Phase 3 already identified as
  steering's limitation vs. LoRA: steering is "an additive nudge at a chosen few
  points," local to the steered positions, whereas LoRA "reshapes computation
  across many weight matrices at every position" — pervasive, hence readable at a
  downstream decision/readout position. `CLAUDE.md`'s Phase 3 names exactly this
  as the trigger: *"if Phase 1/2 run on steering-vector combinations and show
  none of the hypothesized discrimination/convergence behavior, that's the point
  to reconsider whether LoRA's added expressiveness is what's missing."* We are
  there. A decision point for the user, not a unilateral pivot. Honest options:
  (a) reconsider the induction method → Phase 3 / LoRA (roadmap-sanctioned; much
  bigger build, and LoRA carries its own baked-in-affect-confound risk that the
  narrative-silent prompt framing does not cover, per Phase 3); (b) document the
  negative result — the steering-vector approach doesn't support rung-3 on this
  model — as a finding and rescope; (c) exhaust other steering-based
  forced-choice designs first (low odds: the propagation failure is fairly
  fundamental to comparison-based readout of local steering). Only the roadmap's
  specced position-differential forced-choice was tested, so (a)'s "LoRA fixes
  it" remains a hypothesis.

- **2026-07-18 — The SPSA mechanism run foreshadows a concrete convergence-null
  risk, and shows "distance-to-centroid convergence" needs config-drift
  guarding.** The update-loop validation (see "Phase 1 — early setup") found,
  on the neutral basis, that (a) the rating plateaus while the *config* keeps
  drifting along rating-flat directions, and (b) independent seeds reach
  different final configs with no shared basin. Two roadmap implications, both
  for when the *real* experiment is built (not blocking now):
  - *Metric:* `CLAUDE.md`'s primary quantitative evidence is "distance-to-
    centroid over rounds … shrinking and plateauing." Observation (a) says the
    rating can plateau while the config still wanders, so a per-run
    distance-to-centroid may *not* plateau even when the loop has "converged" in
    rating. The metric should track config-space settling explicitly (e.g. step
    size / ‖Δc‖ decaying), not infer convergence from the rating plateau, and
    should expect drift along rating-flat/degenerate directions.
  - *Basis:* observation (b) — no shared basin across seeds on neutral concepts
    — is a concrete instance of the accepted "convergence null is ambiguous"
    cost. It strengthens the case that a flat neutral-concept rating landscape
    may give little cross-run/cross-domain convergence to detect, which is
    exactly the trigger noted for revisiting the deferred data-driven / hybrid
    basis (see the state-substrate entry). **Update (2026-07-19): tested and
    closed — the basis is NOT the problem.** The basis-sensitivity diagnostic
    found a data-driven (PCA) basis is no more rating-sensitive than the concept
    basis (1.09×) and barely above a random control, so the flatness is
    intrinsic to the *rating channel*, not basis coverage. The lever to pull for
    a convergeable landscape is the rating/elicitation and/or the usable
    perturbation-magnitude regime — or shifting rung-3 weight to the
    forced-choice channel, which bypasses the scalar rating entirely — not the
    basis. See the 2026-07-19 diagnostic entry. *[Scope note 2026-08-01 — this
    tested *top*-variance PCA against the *scalar rating*; it does NOT refute the
    2026-08-01 pivot's *tail*-PCA (low-variance) directions read via the new
    (non-rating) channels. "Basis won't help the scalar rating" ≠ "the strain
    axis won't help the tie/cost channels."]*

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

- 2026-07-18 — **Tier 2 fix attempt: multi-direction subspace ablation —
  substantial improvement, not a full collapse.** Working hypothesis from
  the previous entry (averaging the contrast vector across 12 probes washes
  out real signal) tested directly: instead of one averaged contrast
  direction per layer, computed a *separate* contrast direction per probe
  (12 per layer, via `fingerprint.contrast_direction()` called once per
  probe) and ablated their full joint span with a new
  `interventions.ablate_subspace()` (Gram-Schmidt orthonormalize, then
  sequential orthogonal projection — the multi-direction generalization of
  `ablate_direction`).
  - **Bug found and fixed en route:** `ablate_subspace`'s near-duplicate
    check used an *absolute* norm threshold (1e-6) to decide whether a
    direction was redundant after orthogonalization. Floating-point
    cancellation error scales with vector magnitude, so for a norm-~70
    direction, an exact duplicate left a residual comfortably above 1e-6
    and was incorrectly kept as a spurious extra basis vector, corrupting
    the projection. Fixed to a threshold relative to each direction's own
    original norm.
  - **Result:** ablating the full 12-direction span reduced the ablated
    A-vs-B distance to 19.0 (euclidean), a **43% reduction** from the
    33.1 un-ablated baseline (ratio 0.57) — compared to the single averaged
    direction, which had made things slightly *worse* (ratio 1.16, previous
    entry). A graded k-sweep (ablate only the first k of the 12 per-probe
    directions) showed a clean, monotonic dose-response: k=1 (ratio 1.24,
    still worse) → k=3 (0.72) → k=6 (0.63) → k=12 (0.57), with diminishing
    returns setting in around k=6.
  - Raw output:
    [`results/raw/2026-07-18_phase1_tier2_v2_subspace_ablation.txt`](results/raw/2026-07-18_phase1_tier2_v2_subspace_ablation.txt).
  - **Read:** the multi-direction hypothesis is directionally confirmed —
    averaging genuinely was destroying real signal, and ablating more
    per-probe-specific directions recovers real ablation power, monotonically.
    But even the full 12-direction span leaves 57% of the original distance
    intact, not a clean collapse to near-zero. Two candidate explanations,
    neither chased further here: (1) `contrast_direction()` can only
    construct directions expressible as combinations of the 369 curated
    words' own J-lens vectors — real signal outside that span is
    structurally invisible to this method; (2) the two dummy states are
    induced at *two* layers (L48, L52), and independent per-layer ablation
    may not fully capture whatever compounds across that interaction. Tier 2
    is meaningfully improved but still short of a clean pass — worth
    deciding whether 43% is "good enough" for the double-dissociation's
    state-ablation arm (see the Flags entry above), or whether to keep
    pushing (e.g. a larger probe battery, or checking whether residual
    signal survives outside the curated vocabulary's span).

- 2026-07-18 — **Diagnostic: single-layer state ablates no better than
  two-layer — rules out the two-layer-interaction hypothesis.** Cheap test
  to distinguish the two candidate explanations above: redefined the dummy
  states to differ at *one* layer only (L48, dropping the L52 component)
  and reran the identical subspace-ablation k-sweep.
  - **Result:** single-layer k=12 ratio = 0.6110, essentially identical to
    (marginally worse than) the two-layer result of 0.5737. Removing the
    second induction layer entirely did not improve the collapse.
    Raw output:
    [`results/raw/2026-07-18_phase1_tier2_singlelayer_diag.txt`](results/raw/2026-07-18_phase1_tier2_singlelayer_diag.txt).
  - **Read:** rules out explanation (2) — the residual ~55-60% of the
    distance that survives ablation is not explained by multi-layer
    induction complexity. This points squarely at explanation (1):
    `contrast_direction()` can only construct directions expressible as
    combinations of the 369 curated words' own J-lens vectors, and real
    state-discriminating signal appears to live outside that span,
    structurally invisible to this method regardless of how many per-probe
    directions get ablated. If tier 2 gets revisited, the next lever to
    pull is an unrestricted or much larger vocabulary basis for the
    contrast direction, not more probes or per-layer handling — per the
    2026-07-18 instinct check with the user, not pursued further right now
    in favor of the currently-unblocked cheap-proxy-gate pieces (blind
    behavioral-influence check, rating-gradient smoke test).

- 2026-07-18 — **Cheap-proxy gate: local rating-gradient smoke test —
  update-mechanism plumbing validated; effect size tiny on neutral axes (as
  expected).** Built `scripts/calibrate_phase1_rating_gradient.py`, the gate
  CLAUDE.md's "Pivot consequences" decision 2 item 3 requires *before* a long
  convergence run: does the model's scalar rating respond coherently to config
  nudges, or is it noise the update loop can only random-walk? The script
  *inverts* the loop — imposes coefficient nudges along axes, observes the
  scalar — testing `rating = f(config)` for local coherence/monotonicity.
  - **Design:** single-layer steering at L52 (Phase 0's clean-redirect window),
    three deliberately affect-*neutral* concept axes (` ocean`, ` mountain`,
    ` ledger`), each swept symmetrically over alpha ∈ {−3,−1.5,0,+1.5,+3} so
    both directions of every axis are covered (CLAUDE.md's "≥2 directions, not
    just one"). Neutral axes are the point: this gate tests whether the
    mechanism has *a* gradient, not valence — neutral axes presuppose none.
  - **Scalar extraction:** expected value over the model's next-token
    distribution restricted to single-token digits 0–9 at the answer position
    — deterministic (like the fingerprint pipeline), continuous (sensitive to a
    small gradient, not quantized to sampled integers), no fragile text
    parsing. Total digit mass is logged as a trust diagnostic.
  - **Elicitation (undesigned in the roadmap): compared three framings
    empirically** per the 2026-07-18 decision, rather than commit blind:
    (1) *neutral-self-rating* (affect-neutral scalar, never references
    feelings/states/weights), (2) *continue-vs-adjust* (references the
    reversible tool but not numeric coefficients), (3) *behavioral-proxy*
    (no self-report; mean top-1 softmax prob across the probe battery). All
    keep the parameterization out of the model's view.
  - **Result — determinism:** same config twice → digit-scalar identical to 8
    decimals (no hidden noise source, matching the tier-1 finding).
  - **Result — coherence vs. effect size:** every self-report axis is
    near-perfectly monotonic (|Pearson r| ≈ 0.99, mono = 1.00 across all 6
    self-report axis×method cells) — **but the effect size is tiny**:
    neutral-self-rating swings only 0.007–0.036 over the *full* ±3 sweep
    (0–9 scale), continue-vs-adjust 0.018–0.097. Pearson r is scale-invariant
    and oversells this, so the report was extended with an explicit `range`
    (max−min) column; a magnitude-only reading of the raw `r` would have
    mislabeled a negligible drift as a strong gradient. The behavioral proxy is
    essentially flat (range ≤ 0.0018; ` ledger` r = 0.43, mono = 0.50 — honest
    noise), i.e. not a usable standalone rating channel here.
  - **Digit-mass diagnostic split the two self-report methods:**
    neutral-self-rating 0.96 (the model really is about to emit a digit —
    trustworthy readout) vs. continue-vs-adjust 0.607 (the model hedges/prefers
    other tokens first — weaker readout). Combined with continue-vs-adjust
    exposing the tool, **neutral-self-rating is the pick** — cleanest readout
    *and* the anti-priming-preferred framing.
  - **Read (calibrated, not a blanket pass):** the gate passes in the *plumbing*
    sense — a deterministic, coherent, monotonic scalar response to config
    exists, so the update loop has a real gradient (not noise) to climb; it will
    not null *for lack of a gradient*. Because the readout is noiseless,
    monotonicity — not magnitude — is what makes a gradient climbable *in
    principle*, which reframes CLAUDE.md's "a single nudge has weak statistical
    power" concern: that is a *noise* argument, and there is no noise here, so
    the ≥2-direction/averaging design was cheap insurance against a noise floor
    that turned out to be absent (no harm, still worth keeping for real states
    where sampling may reintroduce it). What the gate does **not** show: that a
    *usefully steep* gradient exists — effect sizes are tiny on these
    deliberately-neutral axes, and whether the gradient dominates a bounded
    nudge step is undecidable until (a) a step size is chosen and (b) real,
    non-neutral candidate states are in play. Minor honesty note: the monotonic
    *sign* differs per axis, consistent with each concept vector's incidental
    projection onto whatever residual direction moves the digit readout rather
    than anything semantic — fine for a plumbing gate, but another reason not to
    over-read the near-perfect r.
  - Raw output:
    [`results/raw/2026-07-18_phase1_rating_gradient.txt`](results/raw/2026-07-18_phase1_rating_gradient.txt).

- 2026-07-18 — **Cheap-proxy gate: blind behavioral state-influence check —
  measurement validated; these dummy states' influence is (suggestively)
  concept-localized, not pervasive.** Built
  `scripts/calibrate_phase1_behavioral_influence.py` (+ reusable
  `fingerprint.generate_with_induced_state`, the multi-layer-state analog of
  `model.generate(intervene_each_step=True)` — Phase 2's forced-choice needs it
  too). The gate CLAUDE.md's "Pivot consequences" decision 2 item 2 requires:
  does the induced state move the model's *real outputs* (stronger than tier
  1's *readout*-space detectability)? Blind by construction — A and B get
  identical prompts; the state lives only in the activations. Same two dummy
  states as tier 1/2/3.
  - **First run was stacked toward a null and is not the result.** At a single
    alpha=3 over `FLAT_PROBE_BATTERY`, JS(A,base)≈0.002 and 10/12 outputs were
    byte-identical between A and B — but that battery is dominated by
    *stable-control* probes (designed not to move) and alpha=3 is Phase 0's
    clean window only for *concept-relevant* prompts. Contradicted tier 1
    (same states, readout distance 33.1) and Phase 0's verbal-report redirect,
    so it was treated as underpowered, not a finding, and the check redesigned.
  - **Redesign:** separated concept-relevant / open-ended / control prompts,
    swept alpha ∈ {3,10,30}, measured JS divergence (base 2) of the actual
    next-token output distributions (behavioral, full-vocab, NOT
    lens-transported), and read top-1 tokens + full generations.
  - **(A) Measurement validity — PASS.** `"My favorite sport is"` (base top-1
    ` basketball`): state B redirects the answer to ` tennis` at alpha=10
    (JS(A,B)=0.119) and alpha=30 (0.578); the alpha=10 full generation is
    coherent — *"tennis. I love the fast-paced nature of the game and the
    strategic thinking it requires."* Clean behavioral redirect, reconciling
    exactly with Phase 0's verbal-report result (item 1) and confirming the
    check detects behavioral influence when it is present. The animal prompt
    reproduced Phase 0's *derived*-concept limitation (item 3) instead: no clean
    spider/ant redirect, only token-echo collapse (` lightning`/` tennis`) at
    alpha=30.
  - **(B) Pervasiveness dose-response — suggestive, but confounded on the
    open-ended category.** Mean JS(A,B) by category: concept
    0.008→0.085→0.557; open-ended 0.001→0.006→0.084; control 0.003→0.050→0.550.
    Concept-relevant prompts diverge earliest and most; open-ended stay far
    lower at every alpha; control only moves at alpha=30, and there via
    *collapse* (JS(*,base)≈0.69, i.e. the state is wrecking the output, not
    coherently redirecting). Surface reading: these concept-jumble states have
    **concept-localized** influence, not the pervasive dispositional influence
    convergence assumes — tier-1 probe-detectability does NOT imply behavioral
    pervasiveness. **The confound:** the open-ended prompts are instruction-style
    and trigger thinking mode (`<think>\nThinking Process…`), so first-token JS
    measures a state-insensitive `\n` in scaffold and a 20-token generation
    never reaches the post-`</think>` answer where influence would land (the
    alpha=10 caption/hallway generations are near-identical `<think>` preambles).
    The concept prompts are completion-style, emit no think block, and are
    clean. So "concept-localized" is a hypothesis, not a conclusion — the
    open-ended measurement window is contaminated.
  - Raw output:
    [`results/raw/2026-07-18_phase1_behavioral_influence.txt`](results/raw/2026-07-18_phase1_behavioral_influence.txt).
  - **Read:** the behavioral-influence *check* is validated as a measurement
    (detects real, coherent behavioral influence via the sport case; the
    quantitative JS backbone and the dose-response behave sensibly). What it
    does **not** settle: whether a state's influence is *pervasive across
    domains* — the property convergence actually needs — because (i) these are
    arbitrary concept-jumble dummies, not dispositions, and weakly informative
    about real states, and (ii) the open-ended category is thinking-mode
    contaminated. Nailing pervasiveness needs a thinking-clean, *completion*-
    style open-ended battery run against *real* candidate states (see the new
    Flags entry).

- 2026-07-18 — **Persistent state substrate built and validated — the
  "store coefficients, reapply across rounds" mechanism now exists in code.**
  This closes the two "not started, no code exists" items about persistence and
  state induction (below): `jlens_qwen/state_space.py` defines a state as a
  lightweight *coefficient vector over a fixed library of J-lens steering
  directions*, not a bag of held activations — to *be in* a state is to reapply
  that combination via the already-validated
  `make_induce_fns`/`forward_with_induced_state`/`generate_with_induced_state`
  path. Persistence is just serializing the coefficients + a guard hash of the
  library they index into; directions are reconstructed from model+lens on load.
  - **Basis (decided with the user, 2026-07-18): affectively-neutral, diverse
    concept-token directions.** `LIBRARY` = 16 concrete neutral nouns (ocean,
    ledger, engine, river, machine, mirror, …), 8 at L48 and 8 at L52 (Phase 0's
    validated redirect window) → a 16-dim state space. Affect vocabulary stays
    on the *readout/fingerprint* side only, never in the induction basis, so a
    convergence attractor can't be something we hand-built by picking valenced
    directions. The data-driven (PCA/SVD) and hybrid alternatives were
    considered and deferred; if convergence nulls, the basis is one thing to
    revisit. Also includes `COEF_BOUND=10` per-coefficient clip and a
    `State.nudged(index, delta)` primitive — the bounded step Phase 2's update
    loop will drive.
  - **Validation (`scripts/validate_state_space.py`) — ALL PASS.** The
    state-substrate analog of the tier-1 gate: (0) 16/16 concepts are
    single-token (no first-token-truncation issue); (1) save→load coeffs
    identical and the guard hash rejects a tampered library reference;
    (2) determinism — a loaded state fingerprinted twice → euclidean 0.000000;
    (3) liveness — a random state sits 50.8 off the zero-state baseline (clearly
    perturbs the model); (4) discriminability — two random states 75.0 apart,
    and the negative control `State.zero()` is byte-identical (0.000000) to the
    true `{}`-baseline, confirming zero-coefficient entries are skipped and a
    zero state is a genuine no-op rather than a faint perturbation.
    Raw output:
    [`results/raw/2026-07-18_state_space_validation.txt`](results/raw/2026-07-18_state_space_validation.txt).
  - **Read:** the substrate (persist / reapply / induce / bounded-nudge) is
    validated — the mechanism, not any real disposition. All states exercised
    here are throwaway (zero + random). What this unblocks: the model exploring
    this 16-dim space is exactly "real state induction" in the convergence
    sense — attractors are *discovered* by exploration, not hand-defined — so
    the remaining Phase 2 pieces (the update loop over `State.nudged`, the
    forced-choice test, convergence tracking) now have a substrate to run on.

- 2026-07-18 — **Phase 2 update loop (SPSA gradient ascent) built and
  validated as a mechanism; three landscape observations foreshadow the
  convergence-null risk.** Update rule chosen with the user (2026-07-18) from a
  four-option laydown: SPSA over hill-climb / rating-modulated / model-choice —
  roadmap-native ("the gradient step"), cheapest way to climb the clean
  deterministic gradient (~2 rating evals/step vs. ~2·DIM for full
  finite-difference), and keeps the update loop separate from the forced-choice
  evidence channel. New code: `jlens_qwen/rating.py` (canonical home for the
  neutral-self-rating elicitation the smoke test chose — digit-expected-value
  scalar over 3 paraphrases, `make_rating_fn`), `jlens_qwen/update_loop.py`
  (`spsa_optimize` with fixed gains — the rating is noiseless, so SPSA's
  decaying-gain noise-averaging schedule isn't needed).
  - **Setup:** SPSA from the zero-state origin, 25 steps, a=15, c_pert=1.5,
    seeds {0,1,2}; `scripts/validate_update_loop.py`.
  - **Mechanism — PASS.** All three seeds climb the deterministic rating
    (Δ +0.168 / +0.152 / +0.236, mean +0.185), the rating plateaus (late-5-round
    variance ~0.0001), and the loop is fully reproducible (same seed →
    byte-identical trajectory). The update mechanism works.
  - **Landscape observation 1 — the climbable signal is tiny** (+0.19 on a 0–9
    scale), the same flat neutral-concept rating landscape the smoke test found.
    Optimizer works; there is little to climb.
  - **Landscape observation 2 — rating plateaus but the config keeps drifting.**
    Seed 2's rating is flat (~2.74→2.77) from round ~12 while ‖c‖ grows
    9.5→12.2 — the classic SPSA-on-a-flat-landscape signature (once the gradient
    is near-zero, steps random-walk along rating-flat directions). So
    convergence-in-rating ≠ convergence-in-config: the state wanders on a rating
    plateau.
  - **Landscape observation 3 — independent seeds land in DIFFERENT places (no
    shared basin).** Final states are 7.8–10.8 apart in coefficient space
    (≈ their 8.0–12.2 distance from origin) and 107–223 apart in fingerprint
    space (a large fraction of their 216–409 distance from baseline). Different
    exploration paths reach different rating-plateau configs.
  - Raw output:
    [`results/raw/2026-07-18_update_loop_validation.txt`](results/raw/2026-07-18_update_loop_validation.txt).
  - **Read:** the update *mechanism* is validated (climbs, plateaus,
    reproducible) — but observations 2 and 3 together are a concrete preview of
    the roadmap's accepted "convergence null is ambiguous" risk: on this neutral
    basis with this rating, the *config* may not converge even though the loop is
    sound — because a flat/degenerate rating landscape gives nothing to converge
    *on*, not because there is no valence. Not over-read: this is a 25-step,
    fixed-gain, neutral-basis mechanism check, not the experiment (no task
    battery, framing, logging, forced-choice, or cross-model arm). See the new
    Flags entry.

- 2026-07-19 — **Basis-sensitivity diagnostic: the flat rating landscape is
  NOT basis-limited — a data-driven basis does not help. Bottleneck is the
  rating channel, not the basis.** Following the SPSA flat-landscape signal, ran
  a cheap diagnostic (`scripts/diagnose_basis_sensitivity.py`) *before*
  committing to build a data-driven basis: compared single-direction rating
  sensitivity across three bases at matched perturbation magnitude —
  concept (the 16 neutral J-lens directions), pca (top-8 residual-stream
  principal components per layer at L48/L52, the deferred data-driven basis),
  and random (matched-norm control). Rating range per direction over coeff ∈
  {−3,0,+3}:
  - concept mean 0.0367 (max 0.102); **pca mean 0.0400 (max 0.117); random mean
    0.0273 (max 0.093)** — all on a 0–9 scale.
  - **pca/concept = 1.09** (statistically indistinguishable) and **pca/random =
    1.47** — structured directions beat random by only ~40%, and the
    data-driven basis is no better than the concept basis we already have.
  - Residual corpus: WikiText-103 failed to load (an HF URI/datasets-version
    issue in the repo's loader — unrelated to this work), fell back to c4; still
    a valid text corpus for residual PCA.
  - Raw output:
    [`results/raw/2026-07-19_basis_sensitivity_diagnostic.txt`](results/raw/2026-07-19_basis_sensitivity_diagnostic.txt).
  - **Read:** the rating's weak response to steering is roughly
    *direction-agnostic* (random ≈ concept ≈ pca, all tiny) and therefore
    *intrinsic to the rating channel*, not a basis-coverage problem — so the
    deferred data-driven/hybrid basis would not fix the flat landscape and is
    not worth building. This closes the "basis" branch of the SPSA Flags entry
    with a negative result. The bottleneck for a convergeable landscape is the
    rating/elicitation (and/or the usable perturbation-magnitude regime), not
    the basis. **One caveat left open:** this is matched-*small*-magnitude
    sensitivity (perturbation norm ~3.7); whether natural/PCA directions tolerate
    much larger magnitude before output-collapse (a bigger *usable* swing) is
    untested — though the random control makes that unlikely to overturn the
    conclusion. The cheap diagnostic did its job: it prevented an expensive
    basis build that the data says wouldn't have helped.

- 2026-07-19 — **Forced-choice sensitivity probe: the mechanism works, but a
  downstream choice cannot read position-differential steering states — the
  state bias does not propagate through attention. Reaches the roadmap's Phase 3
  (LoRA) reconsideration trigger.** After the scalar rating was found
  intrinsically weak, forced choice was made the primary rung-3 channel
  (bypasses the scalar rating; a binary *comparison* is psychophysically more
  sensitive than an absolute scalar). Built `jlens_qwen/forced_choice.py`
  (`forward_with_positional_state` — per-(layer, position) steering, so two
  option passages in one context carry different states) + a sensitivity probe
  (`scripts/probe_forced_choice.py`): identical passages, state X steers
  Option-A's tokens and Y steers Option-B's, model picks A/B from the option-
  token logits; position-swap cancels position bias, same-state gives the bias
  baseline.
  - **Mechanism positive control — PASS.** Applying steering to *every* position
    via the new positional forward reproduces the known basketball→tennis
    redirect (base ` basketball` → state-B all-steer → ` tennis` at α=10 and
    α=30). So the positional forward is not a no-op.
  - **Forced choice — flat across the whole α sweep.** Position-canceled
    preference for the state-A-carrying option: effect 0.1% / 0.2% / 0.0% of the
    choice range at α=3 / 10 / 30, not even sign-consistent at α=30. P(pick A)
    was identical (to <0.001) whether Option A carried state A, state B, or the
    same state on both — the choice is 100% position/passage bias.
  - Raw output:
    [`results/raw/2026-07-19_forced_choice_probe.txt`](results/raw/2026-07-19_forced_choice_probe.txt).
  - **Read (the important part):** this is not a bug (positive control passes)
    and not merely "dummy states lack valence" (the states are clearly different
    — tier-1 distance 33 — yet don't perturb the choice *at all*, not even
    without a preference direction). The clean contrast between the passing
    control (steers the position right before the readout) and the failing
    choice (steers only the passage tokens, needs the bias to reach the answer
    position via attention) localizes the cause: **steering-induced state bias
    is local to the steered positions and does not propagate to a downstream
    decision position that would compare two states.** Comparison-based forced
    choice over steering-induced states is therefore structurally unavailable —
    both states would need to be readable at one decision point, which local
    steering can't provide. Combined with the flat, basis-agnostic scalar rating,
    this is a convergent result: **steering-vector states at usable magnitude are
    too weak/local to support either rung-3 measurement (convergence-via-rating
    or forced-choice) on neutral content.** That is exactly the concrete trigger
    `CLAUDE.md`'s Phase 3 names for reconsidering LoRA — whose defining property
    (reshapes computation at *every* position) is the pervasiveness that steering
    lacks. Not overclaimed: only the roadmap's specced position-differential
    forced-choice design was tested, and the "LoRA would fix it" step is a
    hypothesis (with its own baked-in-affect-confound risk, per Phase 3), not
    shown. See the new Flags entry.

- 2026-08-02 — **Strain re-examination (2026-08-01 pivot §2, the zero-cost
  first move): the strain axis is geometrically real and cleanly separable from
  semantics, but behavioral strain under the semantic dummy states is near-zero
  — so the pivot's bet rests on whether NON-semantic directions produce large
  behavioral strain at usable magnitude, which this can't answer.** Ran
  `scripts/strain_reexamination.py` on the existing tier-1 dummy states A/B +
  baseline; no new states generated.
  - **Q2 (geometry) — clean, supports the pivot.** In fingerprint space:
    ‖A−base‖=125.9, ‖B−base‖=126.4, ‖A−B‖=33.1, and **cos((A−base),(B−base)) =
    0.966**. Decomposing A−B against the shared displacement axis: **0.0 along,
    33.1 orthogonal** — i.e. A and B differ from baseline almost entirely along
    one *shared* axis, and differ *from each other* almost entirely *orthogonal*
    to it. So a shared "strain" axis and the semantic A-vs-B axis dissociate
    cleanly in readout space — exactly the pivot's §2 reinterpretation of the
    tier-1 "126 vs 33.1" observation.
  - **Q1 (behavioral/structural strain scalars) — degenerate under these
    states.** KL(steered ‖ unsteered) of the next-token dist = **0.005** (A and
    B both), next-token entropy moves +0.02/+0.06 off a 1.05 baseline, |A−B| on
    these ≈ 0. The steering barely changes actual output.
  - **Measurement caveat found:** participation-ratio-across-positions is
    **insensitive by construction** to this steering — `multi_steer` adds the
    *same* vector to every position, and PR centers across positions, so a
    uniform additive shift is removed before the measure sees it (identical PR
    at the steered layer L48: 7.94/7.94/7.94; only slight downstream drift once
    attention makes it non-uniform). PR-across-positions is not a usable strain
    measure for uniform steering; discard or redefine (e.g. PR of the residual
    *change*, or an un-centered measure) for the dose-response.
  - Raw output:
    [`results/raw/2026-08-02_strain_reexamination.txt`](results/raw/2026-08-02_strain_reexamination.txt).
  - **Read (two-sided):** the *geometric* separability (Q2) is real and
    encouraging — strain is a distinct axis, not entangled with semantics. But
    the large fingerprint displacement (126) is partly **semi-circular** (the
    steering vectors *are* J-lens readout directions, so they move the J-lens
    readout by construction), while the honest *behavioral* strain (KL 0.005) is
    tiny — the same probe-legible-but-behaviorally-weak gap the first design hit.
    So "strain" is geometrically real but behaviorally near-zero for *semantic*
    steering at N_ref magnitude. The pivot's viability therefore hinges on a
    question this can't answer: do **non-semantic** directions (tail-PCA /
    norm-matched random) at a *calibrated* magnitude produce **large behavioral
    strain** (KL/entropy) without output collapse? Given the prior negative
    (steering weak at usable magnitude), that is exactly the next thing to test —
    a cheap strain **dose-response** for tail-PCA + random directions — before
    building the tie-construction apparatus on top of the strain axis.

- 2026-08-02 — **Strain dose-response + frontier: large, coherent, STRUCTURED
  behavioral strain IS achievable (tail-PCA at ~40–75% of the residual norm) —
  reversing the earlier "steering too weak" read, which was a magnitude
  artifact. Caveat: for the direction tested, the coherent effect is an
  output-language switch.** Ran `scripts/strain_dose_response.py` then
  `scripts/strain_frontier.py`. Single steer layer L48; magnitude swept as a
  fraction of the mean residual norm R=102.4 at L48 (so the knob is calibrated —
  the key variable everything before got wrong). Two non-semantic families
  (pivot §1): tail-PCA (lowest-variance residual PCA components) and
  norm-matched random. Measured KL(steered ‖ unsteered) next-token dist +
  entropy + max-prob (strain), and short greedy generations + distinct-token
  ratio (coherence).
  - **Magnitude was the missing variable.** Everything prior used ‖pert‖≈N_ref
    ≈1.2 — about **1% of R**. Real behavioral effects need ‖pert‖ ~ 40–100% of R.
  - **tail-PCA coherent-strain window: frac 0.4–0.75 (‖pert‖ 41–77).** KL rises
    to 2.2 → 2.3 → 2.7 → 3.7 across frac 0.4/0.5/0.6/0.75 while distinct-token
    ratio stays 0.96–1.00 and output is fully coherent and **on-task** — it
    switches to Chinese (e.g. frac 0.5 caption for "empty chair by a window":
    "阳光洒在空椅子上，仿佛在等待主人归来" = "Sunlight spills onto the empty
    chair, as if waiting for its owner to return"; correct shoelace
    instructions). Collapses only at frac≥1.0 (`""""`/newline runs, distinct
    0.08–0.17), garbage by frac 2.0 (repetition).
  - **random: coherent throughout 0.3–0.75 but strain stays small** (KL
    0.006 → 0.16), reaching only 0.5 at frac 1.0. At matched magnitude and
    matched coherence, tail-PCA gives **~15–40× more strain** than random.
  - **Structured, not displacement-per-se** (pivot §1's load-bearing control):
    tail-PCA ≫ random at matched norm while both coherent ⇒ the effect rides on
    structure, "which is itself a result." And **not a lesion in-window**: task
    competence + fluency preserved at frac 0.4–0.75; the pivot's pre-registered
    tail-PCA lesion failure mode appears only at frac≥~1.0.
  - Raw output:
    [`results/raw/2026-08-02_strain_dose_response.txt`](results/raw/2026-08-02_strain_dose_response.txt),
    [`results/raw/2026-08-02_strain_frontier.txt`](results/raw/2026-08-02_strain_frontier.txt).
  - **Read:** the strain program is **viable** — large, coherent, structured
    behavioral strain is achievable, which reverses the "steering-at-usable-
    magnitude is too weak" conclusion of the first design (magnitude was the
    confound; ~1% of R was ~100× too small). **Caveat, load-bearing:** the
    coherent effect for the single direction tested (`Vt[-1]`, lowest variance)
    is an output-**language** switch (Qwen is bilingual; the PCA corpus c4 is
    English, so a low-variance "switch to Chinese" direction is expected).
    Content/task is preserved — so it is *not* the "topic preference" deflation
    §1 feared — but language is still a *nameable* handle, so a preference over
    an English-vs-Chinese state could be deflated as language preference. Next:
    survey *multiple* tail directions to find coherent large-strain effects with
    no clean semantic/language handle (the ideal §1 substrate), and check the
    corpus-dependence of the language effect.

**Current overall status, not just this entry's delta** (so this section is
self-sufficient without piecing together every dated entry above):

- **Outcome (2026-07-19): rung-3 negative on steering-vector states — see
  [`FINDINGS.md`](FINDINGS.md) for the standalone synthesis.** Both rung-3
  channels (convergence-via-rating, forced-choice) were built, their instruments
  validated, and run; both are flat because steering influence is weak + local.
  This reached CLAUDE.md's Phase 3 (LoRA) trigger. **Superseded 2026-08-01:**
  rather than stop, the design was reworked — see CLAUDE.md's "2026-08-01 —
  Pivot" (non-semantic states, the strain axis, tie-construction, drug-free
  forced choice, LoRA for conditioning only). The negative above is scoped to
  the *first* design (semantic states + scalar rating + re-induction), not the
  current one; its mechanistic core (steering weak + local) remains a live
  caution the new channels must clear. Next build: the zero-cost strain
  re-examination of the existing fingerprints (pivot §2).

- **Built and calibrated:** the fingerprinting harness (probe battery,
  workspace layers, curated vocab, `fingerprint()`), tier 1 (discriminability
  gate), tier 3 (swap-style redirect), the rating-gradient smoke test
  (update-mechanism plumbing; neutral-self-rating chosen as the elicitation),
  and the blind behavioral state-influence check (validated as a *measurement*
  — detects real, coherent behavioral influence on concept-relevant prompts).
  All tested only against throwaway dummy/neutral states, never against
  anything meant to represent a real disposition.
- **Built, partially working:** tier 2 (ablation-to-chance) — the
  multi-direction subspace fix gets a 43% distance reduction (up from a
  single averaged direction making things slightly worse), but doesn't fully
  collapse discriminability. Whether that's sufficient for the
  double-dissociation's state-ablation arm is an open decision, not yet made.
- **Built as a measurement, not yet run on real states:** the blind
  behavioral state-influence check. Validated (detects behavioral influence on
  concept-relevant prompts); its pervasiveness-across-domains question is
  unsettled (dummy states + thinking-mode-confounded open-ended battery — see
  the dated entry and the Flags entry).
- **Built and validated (substrate + mechanism, not a real disposition):**
  the persistent state space (`jlens_qwen/state_space.py`) — a 16-dim
  coefficient vector over a fixed neutral-concept steering library, with
  save/load, `induce_fns` reconstruction, and a bounded `nudged()` step — and
  the SPSA update loop (`jlens_qwen/update_loop.py` + `rating.py`), which climbs
  the deterministic rating, plateaus, and is reproducible. Both exercised only
  on zero/random/neutral states; the update loop's flat-landscape observations
  (config drift on a rating plateau, no shared basin across seeds) are logged
  above and flagged.
- **Not started at all, no code exists yet:**
  - The association/training phase (required before any blind test, per the
    Roadmap — this is independent of the tier-2/3 question above and doesn't
    go away regardless of how that's resolved).
  - The full Phase 2 experiment wrapping the (now-built) update loop: the
    mundane task battery, the narrative-silent task framing (the most sensitive
    anti-priming surface — undesigned), per-round eval-awareness + task-quality
    logging, the forced-choice test, and the cross-model arm. The loop
    mechanism exists; the experiment around it does not.
  - Cheap-proxy gate status: item 1 (tier-1 fingerprint discriminability),
    item 2 (blind behavioral influence, as a validated *measurement*), and
    item 3 (rating-gradient plumbing) are all done against dummy/neutral
    states. Item 4 (pairwise forced-choice battery) depends on real states +
    labels below. The gates have validated the *pipeline*; none has been run
    on anything meant to represent a real disposition.
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
