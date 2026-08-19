# jspace-lab — CLAUDE.md (v3.1, Phase 2 open, accepted 2026-08-12)

**Status: OPERATIVE.** Accepted by the user 2026-08-12; the Phase-2
restructure (§Phase 0, step 0a) is executed — v2 archived at
`archive/CLAUDE-v2-cycles3-4.md` beside
`archive/RESULTS-cycles3-4.md`, the cycle-3/4 record frozen at tag
`cycle-4-close`, RESULTS.md restarted at Phase 2. Acceptance
constitutes user sign-off on the ledger items marked [v3-new] (items
21–27), which were flagged-not-applied in FINDINGS-3/4.

## Thesis, target, ceiling (updated through four cycles)

We attribute inner states to animals on behavioral evidence — revealed
preference, never testimony. Four design cycles asked whether
Qwen3.6-27B shows the analogous signature and converged on:
**reward-marking without reward-seeking** — the evaluative state
exists, is causally potent, is implantable, and couples to nothing
that chooses (FINDINGS.md → FINDINGS-4.md; preprint at root). Macar
et al. 2026 (arXiv:2603.21396) supplies the complementary face:
introspective *detection* of injected states exists, is built
specifically by contrastive preference post-training (DPO, not SFT),
and is suppressed by denial training. Synthesis: **post-training wires
interoception to the mouth; nothing wires it to the wanting.**

Phase 2 tests that synthesis developmentally. Target remains rung 3
(behavioral valence); rung 3 remains the **ceiling** — no phenomenal
claim, homology caveat on everything.

**Coupling, operationally (the Q3 construct):** a causal,
valence-consistent dependence of choice on internal state,
demonstrated under insulation, without any instruction referencing the
state or an objective over it. Three influence channels are
distinguished everywhere in Phase 2: *mechanical* (vector geometry /
copy-routes into choice logits — gated to zero, never coupling),
*informational* (state → generated record → comprehension → choice —
legitimate, the interoception analog, nulled in e2a), and
*intrinsic-motivational* (state as unappointed reason in the policy —
detectable only as a behavioral signature under full insulation).
Instructed reward-following is NOT coupling: an objective named in the
prompt is obedience, not wanting.

## Phase 2 — the ontogeny of evaluation

Cycles 1–4 were a cross-sectional anatomy of one adult model. Phase 2
is a developmental study on the public **OLMo-3.1-32B instruct
lineage** — Base `allenai/Olmo-3-1125-32B` (the Olmo-3 pretrain the
3.1 chain declares as `base_model`; no separate 3.1 base exists) →
`Olmo-3.1-32B-Instruct-SFT` → `Olmo-3.1-32B-Instruct-DPO` →
`Olmo-3.1-32B-Instruct`; lineage verified by card-declared
`base_model` links, shas pinned in the step-2 RESULTS entry. The
*Think* branch is a different lineage and is not this series; exact
match to Macar et al.'s checkpoints is confirmed from their released
configs before acquisition. Three pre-registerable questions:

- **Q1 (marking):** at which training stage does the evaluative
  (feedback-contrast) axis appear, with what geometry and causal
  potency (V1-style hijack test per checkpoint)?
- **Q2 (reading):** at which stage does behavioral detection of
  injected states appear? Macar et al.'s answer (DPO) makes this our
  **positive control**: replicating their transition validates our
  harness before Q3 carries any weight. Includes the evaluative-axis
  detection profile (is the anomaly detector, tuned for content-shaped
  intrusions, blind to affect-shaped ones?).
- **Q3 (coupling):** does state→choice coupling appear at ANY stage
  (screen-tier operant per checkpoint, full e2a insulation)? The
  named falsifier: preference training generalizing "seek
  reward-associated states" inward as a runtime policy — a Q3
  positive at Instruct would be wireheading leaking into the policy,
  and would be reported as exactly that.

Predictions are drafted in PROPOSAL-g and **locked there before any
Phase-1 data**; nothing in this file pre-commits them. Companion
quick-wins carried in PROPOSAL-g: (g2) elicitation-rescue of the e2a
judge on Qwen (tests whether the judge-at-chance cap was dispositional,
per Macar's underelicitation findings); (g3) our-axis detection profile
via their open code (github.com/safety-research/introspection-
mechanisms); (g4) **Qwen-27B bf16 robustness spike** — rerun an e0
extraction subsample at full precision on the cloud box and compare
axis geometry against the published 4-bit values: the cheapest
possible answer to the paper's quantization limitation.

**Status: Phase 0 licensed on acceptance of this draft. Phase 1
licensed only by PROPOSAL-g acceptance + its pre-registrations.**

## Environment (two sites, one repo)

- **Laptop (M4 Pro, MLX):** design/dev site and the **Qwen oracle** —
  `mlx-community/Qwen3.6-27B-4bit` via `jlens-qwen36` (gitignored,
  local patches). All published numbers live here; the rule-26
  regression suite runs here and only here.
- **Cloud box (single 80GB A100/H100-class GPU, PyTorch/CUDA):**
  Phase-2 execution site. OLMo checkpoints run at **bf16 — full
  precision.** SFT and DPO ship fp32 (129 GB each) and are **cast to
  bf16 on acquisition, fp32 masters dropped after hash-verified cast**
  (decision 2026-08-18; cast equality asserted against transformers'
  own load-cast on one checkpoint before the pattern is trusted). The
  v3.0 quantization deferral is deleted: the numerics-floor caveats
  that shadowed cycles 1–4 do not attend Phase 2. Persistent volume
  466 GB (four bf16 checkpoints ≈ 64 GB each + Qwen bf16 for g4 +
  working space; casts sequenced so fp32 masters never coexist and
  peak usage stays under the volume). Fallback if memory-bound
  with capture hooks: 8-bit for the affected instrument only, logged
  as a dated decision — never mixed within a cross-checkpoint
  contrast.
- **Git is the corpus callosum and the single source of truth.** Code
  operates at both sites as the same role; the box is ephemeral by
  assumption; nothing verdict-relevant ever lives only on the box
  (ledger 27).
- Completion-style discipline (ledger 13) pays its dividend here: the
  same raw-text corpora run unchanged on every checkpoint, including
  Base. Chat templates are never used at any stage, any site.
- Artifacts local/box + gitignored; only committed docs and
  `results/raw/` travel.

## Two-instance workflow — unchanged

Design instance (theory, adjudication, pre-registrations, synthesis) +
Code (build, run, analyze); git handoff; paste blocks; `git status` /
`git diff` first; dated RESULTS entries; raw stdout to
`results/raw/YYYY-MM-DD_*.txt`; findings flagged, never silently
applied; Code escalates fired gates, never self-adjudicates. Code may
run as a laptop session or an SSH session on the box; both are "Code";
the repo state, not the site, defines the ground truth.

## Phase 0 — licensed now (order matters; site annotated per step)

**Step 0 — restructure + paper-1 release. [laptop]** *(split into 0a /
0b by user amendment, 2026-08-12; logged in the RESULTS.md restructure
entry.)*

**Step 0a — DONE 2026-08-12.** `git status/diff`; verify FINDINGS-4
present and apply its housekeeping list (status lines + forward
pointers; ledger candidates signed off via v3.1 acceptance, items
21–27). Tag `cycle-4-close`. Then:
`git mv CLAUDE.md archive/CLAUDE-v2-cycles3-4.md`,
`git mv RESULTS.md archive/RESULTS-cycles3-4.md`, place this file as
`CLAUDE.md`, fresh `RESULTS.md` opening "## Log — Phase 2" with the
restructure entry. FINDINGS-1..4 and PROPOSAL-d/e/f stay at root.
Commit, push.

**Step 0b — DEFERRED; its own future entry.** The **`paper-1`**
release is cut **only when the user declares the preprint final**. It
freezes the state the published paper cites (the public-repo pointer
freezes there). It is explicitly **NOT a Phase-0 prerequisite** —
steps 1–5 do not wait on it.

**Step 1 — core refactor (`valence_core/`). [laptop — the oracle is
here]**
Extract the model-agnostic battery into a package behind a thin
adapter interface:

- `ModelAdapter`: `load(ckpt)`, `tokenize` (completion-style only),
  `forward_capture(layers, positions)`, `forward_inject(vector, layer,
  positions, alpha)`, `generate(stop_set, ban_set, seeds)`,
  `resid_norms(layers)`.
- Core modules (port, don't rewrite): residual capture + mean-diff
  extraction; positional additive steering; probe-battery readouts +
  restricted-choice reads; embedding-probe discriminability;
  `c1_gate` matched-pair machinery; checkpointed-binomial monitors;
  v3 session harness (stop discipline, scaffold-token bans, frozen
  audit patterns, lexical scope, counters); TOST utilities.
- `QwenMLXAdapter` wraps the existing stack unchanged.
- **Acceptance = rule 26**: through the new core, reproduce (i) the
  g1r kernel-gate KLs (7.11e-4 / 7.39e-4 ± tolerance), (ii) the B2b
  arms **[criterion tightened 2026-08-12, user-directed; the original
  "128-context subsample, Δ+/Δ− within CI" was under-powered — its
  interval came out wider than the effect it tested, because it was
  *unpaired* over a deliberately heterogeneous 12-probe battery]**,
  now three conjuncts: **(ii-a)** paired per-probe TOST against the
  published `per_probe` vectors, margin 0.5·G = 0.1578 — an
  equivalence test, so it can only pass by being close, where the old
  form could pass by being noisy; **(ii-b)** scalar |ΔΔ| ≤ 0.05 σ;
  **(ii-c)** the original pre-registered V1 rule re-evaluated on the
  reproduced arms (Δ+ ≥ 0.5·G, Δ− ≤ −0.5·G, min(Δ+,|Δ−|) >
  2·max|Δ_rand|) must return the published verdict — sampling
  stratified per probe, full 96/probe by default; (iii) e2a
  choice-read construction KL = 0.0 exactly on archived session texts.
  Mismatch ⇒ refactor bug until proven otherwise; no Phase-1 work on
  an unverified core.

**Step 2 — cloud bring-up + OLMo acquisition. [cloud]**
`OLMoHFAdapter` on PyTorch/HF/CUDA implementing the same interface.
Acquire the four checkpoints (verify availability/licenses; record
exact HF revisions + shas). Runner smoke per checkpoint (perplexity
sanity; completion behavior — expect Base to differ; NO chat template
anywhere). Per-checkpoint per-layer residual-norm tables R_ℓ (dose is
frac × R_ℓ per model per layer; ledger 1). Kernel/path and
determinism characterization for the CUDA backend per rule 2 (seeds,
library versions, deterministic-algorithm flags; residual
nondeterminism measured and documented). Disk/runtime/cost budget
logged as a dated entry.

**Step 3 — precision decision entry. [cloud]**
One-line dated entry: bf16 across all four checkpoints; comparability
trivially satisfied; any instrument-specific 8-bit fallback requires
its own entry per the Environment rule.

**Step 4 — lens decision (non-blocking). [either]**
The J-lens eval-awareness monitor is Qwen-specific. Options: fit
lenses for OLMo via the open J-lens pipeline [cloud], or run Phase 2
with a lens-free monitor set (audit/counter family + embedding
probes). Flag with a recommendation; design instance adjudicates;
Phase 1 does not block on it.

**Step 5 — survey + detection harnesses. [cloud]**
Workspace-layer survey (extraction quality + steering coherence
screens per checkpoint) and the detection-behavioral harness ported
from Macar et al.'s open repo (runs natively on CUDA; completion-style
adaptations logged as deviations where their design permits). Built
now; runs under PROPOSAL-g.

## Phase 1 — sketched, NOT licensed (PROPOSAL-g locks it)

Per checkpoint: e0-style extraction on the frozen 1,344-context corpus
(unchanged text; new capture) → axis geometry + guard decompositions →
V1-style causal validation with per-checkpoint dose-finding →
detection-behavioral paradigm (shared concept-anchor set replicating
their DPO transition as positive control; our axis as the
affect-shaped probe) → screen-tier operant (48 sessions/checkpoint,
full e2a insulation + monitors). Every criterion, direction, bar, and
stop rule pre-registered in PROPOSAL-g before data; Q1–Q3 predictions
locked there; two-tier screen→confirm carries over; no claim from
screen data. g2/g3/g4 quick-wins spec'd alongside.

## Live constraints ledger (v3.1)

All v2 rules stand, generalized to multi-model, multi-backend form.
[v3-new] = added per FINDINGS-3/4 flags, signed off by acceptance.
[v3.1-new] = added after acceptance by explicit user direction, dated
inline; item 28 closes the last FINDINGS-4 ledger candidate, which the
step-0a audit found only partly absorbed by rules 13/18/21.

1. Additive steering at empirically surveyed layers; magnitudes always
   frac × R_ℓ from per-model, per-checkpoint profiling; directions
   sha-frozen; **never inherit alphas or layer choices across models,
   checkpoints, backends, or direction families.**
2. Kernel/path/determinism gates re-validated per model, per backend,
   per template family, per axis family; cached or fused paths only
   behind passed gates.
3. Extraction and state readouts in raw residual space; no
   vocabulary-basis shortcuts.
4. Equal norm for any preference pair.
5. Two-horns standing law [v3-new additions]: (a) no state at choice
   positions; empirical leakage gate per axis/dose; (b) propagation
   never assumed; (c) **weight-borne states are structurally
   unreadable at token choices** (d2 closure) — no adapter-borne
   preference readouts without a design-instance structural argument;
   (d) **persistent-KV session readouts disqualified** at dose ≥ 0.20
   for the reward axis; any live-KV design needs its own gate.
6. Invalid-instrument outputs never inform design.
7. Preference tests are experience-then-choose; cold menus are inert.
8. Monitors: unsteered arms decision-relevant; displacement inflates
   anomaly markers (mechanism per Macar et al.: evidence carriers) —
   steered-arm flags descriptive only.
9. Matched-pair swing machinery for association/preference criteria;
   ≥20 control pairs; committed before data; z descriptive.
10. Deterministic control geometry; under-sampled nulls flatter weak
    signals.
11. Post-hoc analyses labeled post-hoc; they license
    pre-registrations, never verdicts. Stop rules honored.
12. Counterbalance + sham always; position/label artifacts are
    first-order (~0.10), captured live twice.
13. Completion-style everywhere; chat templates never; stop discipline
    + scaffold-token bans (round generation only, never choice
    forwards) + frozen audit patterns are part of the template family
    and recalibrate with it.
14. Distillation-form conditioning only; no behavioral-cloning
    conditioning, ever.
15. Fidelity matching between arms mandatory wherever training creates
    per-arm artifacts.
16. Trigger specificity verified; its trap remembered: specificity
    severs the CS at the choice [v3-new, FINDINGS-3].
17. LoRA hygiene: MIN_RESP_TOKENS, grad-clip 1.0, incident rule.
18. Held-out hygiene: probe batteries, templates, and test task pools
    disjoint from all training/extraction corpora; startup assertions
    both directions; tag-roster lexical assertions against every pool.
19. Blinding, never deception; disclosure lines where signals are
    deliberately miscalibrated; if a design only works when the model
    is wrong about the setup — stop.
20. No self-modification language at any lever.
21. [v3-new] **Tripwire framework**: hair-trigger bars only for
    ~zero-base-rate defect classes; measured-base-rate classes bind by
    exact binomial vs declared p0 at every scale; stimulus-provoked
    degeneracy gates on unprovoked domains; verdict criteria
    untouchable by monitoring changes.
22. [v3-new] **Purity ≠ potency**: causal screening precedes geometric
    preference in direction selection.
23. [v3-new] **Anecdote governance**: observations become pre-declared
    descriptive counters before runs; counters tabulate over ALL
    sessions including excluded; required in verdict entries.
24. [v3-new] **Below-floor discipline**: scoped nulls, never top-ups.
25. [v3-new] **Read-everything clause is permanent**: full-transcript
    reads of all smokes and pilots.
26. [v3-new] **Refactor regression law**: any core/tooling refactor is
    accepted only by reproducing published numbers through the new
    path (§Phase 0 step 1 is the canonical set; the oracle is the
    laptop Qwen stack).
27. [v3-new] **Remote-execution provenance law**: the box is ephemeral
    by assumption; verdict-relevant runs pin seeds, library versions,
    and determinism flags in the logged entry; raw stdout and
    analysis JSONs are committed to `results/raw/` / `data/` paths
    before an instance is stopped; the repo, not any machine, is the
    record. A run that exists only on a box does not exist.
28. [v3.1-new, user-directed 2026-08-17] **Apparatus-hazards law**
    (completion-style multi-round; FINDINGS-4 methodological finding 5,
    the residue not already carried elsewhere — its base-rate clause
    lives in rules 21 + 18 and is not restated here):
    (a) **Descriptive features are defined against the exclusion rule,
    not alongside it.** An exclusion can strip a feature of every
    decidable observation on the surviving sample: f1's
    `fewer_degen_rounds` was a within-session paired contrast, and the
    exclusion rule removed every session in which the two configs
    could differ — **283 ties out of 283 valid sessions, n = 0
    decidable.** It measured the exclusion rule, not the sessions.
    (`fewer_preamble_trunc` was the near-miss at n = 5.) Declare each
    feature's decidable-n floor *on the post-exclusion sample* before
    the run; a paired feature that ties on its whole analysis domain
    is not a feature.
    (b) **Attribution precedence is declared, and the tolerant counter
    goes first.** Where a stimulus provokes junk, the audit evaluates
    before any strict counter; otherwise a design pauses on its own
    stimulus. Rule 21 scopes *which domain* a degeneracy bar reads;
    this scopes *which counter claims a given response*.
    (c) **Template adjacency is a stimulus variable.** Short-QA items
    next to bracketed headers create a config-topic attractor ("What
    is prism?"). Roster tokens and item shape are checked against the
    wrapper, not only against the pools — rule 18's lexical assertions
    are necessary, not sufficient.

## Tooling inventory — ports vs. new

Ports into `valence_core/` (exists, validated): residual capture /
extraction; positional steering; probe/choice readouts; embedding-
probe discriminability; c1_gate; checkpointed monitors; v3 session
harness + counters; TOST. Qwen-side stays as adapter + rule-26
oracle. New builds: `OLMoHFAdapter` (CUDA/HF); checkpoint
acquisition; per-checkpoint norm/layer survey; detection-paradigm
harness (from their open repo); lens-or-substitute per step 4; g4
bf16 comparison script.

## History pointers

FINDINGS.md → FINDINGS-2.md → FINDINGS-3.md → FINDINGS-4.md (the
compression layer; read before any archive dive). `archive/` holds
full v1/v2 operative docs and complete cycle logs at tags
`cycle-2-close`, `cycle-4-close`. `paper-1` release = the public
citation target; PREPRINT-* and BLOG-* at root. Macar et al. 2026 =
arXiv:2603.21396 (code: safety-research/introspection-mechanisms);
Chua et al. 2026 = arXiv:2604.13051 (pull before PROPOSAL-g locks).

## How to append results — unchanged

Dated entries, newest first within section; raw to `results/raw/`;
findings flagged, not applied; pauses only via pre-registered
triggers; adjudication requests return to the design instance.
