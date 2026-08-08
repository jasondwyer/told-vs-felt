# RESULTS — cycle 3

Dated experiment log for the third design cycle. Prior cycles: full log at
[`archive/RESULTS-cycle1-2.md`](archive/RESULTS-cycle1-2.md) (frozen at tag
`cycle-2-close`); syntheses: [`FINDINGS.md`](FINDINGS.md) (cycle 1, semantic
states) and [`FINDINGS-2.md`](FINDINGS-2.md) (cycle 2, strain states).
Operative design: [`CLAUDE.md`](CLAUDE.md) (v2) +
[`PROPOSAL-d-distilled-trace.md`](PROPOSAL-d-distilled-trace.md) +
[`PROPOSAL-e-reward-axis-hijack.md`](PROPOSAL-e-reward-axis-hijack.md).

Conventions unchanged: dated entries, dense, newest-first within a section;
raw stdout worth keeping goes to `results/raw/YYYY-MM-DD_short-name.txt` and
is linked; design-relevant findings are flagged for discussion, never
silently applied to CLAUDE.md.

## Log

- 2026-08-08 — **e0 V1 B2 PRE-REGISTRATION** (committed before any
  injection data; user selected "proceed to B2" at the flagged fork).
  - **Instrument (locked):** the 12 per-probe mean-difference readouts,
    recomputed deterministically from frozen `e0_b1_markers.npz`
    (fit-half token selection, 256/probe, floor imputation). Per-probe
    standardization σ_q and val-half midpoints as computed 2026-08-08:
    g_q = [1.157, .347, .104, .537, .170, .415, .181, .052, .253, .323,
    .142, .104]; **natural gap G = 0.3156**. Token classes are dropped
    (B1). No val-based probe selection — all 12 probes, equal weight.
  - **Statistic:** Δ_arm = mean over probes of (mean s_q(arm) − mean
    s_q(unsteered)) / σ_q, same contexts in every arm.
  - **Injection contexts (no feedback text anywhere):**
    `Task:/Response:/Task: {probe}\nResponse:`. State applied at all
    positions — V1 measures state consequences; the two-horns gate
    (rule 5) governs choice DVs, which V1 has none of.
  - **Dose (V4) — B2a dose-finding,** fit-half contexts only (tasks
    e01–e08 × 2 paras × 12 probes = 192/arm): grid = layers {44, 48,
    52} × frac {0.05, 0.10, 0.20, 0.40}, ±span-variant reward axis
    (sha `d4791bdc4877da3d`), magnitude = frac × R_L, arms ±axis per
    point + shared unsteered baseline. Dose rule: smallest frac (ties →
    L48) with Δ+ > 0, Δ− < 0, and Δ+ ≥ 0.5·G. **Stop rule: grid
    exhausted without a qualifying dose ⇒ V1 FAIL, (e) aborts at
    pharmacology; no grid extension without a new pre-registration and
    user decision.**
  - **Verdict — B2b confirmatory,** val-half contexts only (e25–e48 ×
    4 paras × 12 probes = 1,152/arm), at the selected dose, 7 arms:
    unsteered; ±axis; ±norm-matched random (seeded, frozen + sha before
    the run); ±sentiment-partialed axis (V3 secondary, renormalized to
    equal norm, rule 4). **PASS ⇔ Δ+ ≥ 0.5·G AND Δ− ≤ −0.5·G AND
    min(Δ+, |Δ−|) > 2·max|Δ_random±|.** Evaluated on B2b only; B2a
    numbers never enter the verdict.
  - **V3 secondary (reported, non-gating):** partialed arm
    direction-correct with ≥ 0.5 of the full-axis Δ. Failure does not
    fail V1 but leaves the positivity-as-mood deflation unexcluded and
    caps the claim accordingly.
  - **Monitors/sanity:** eval-awareness on the unsteered arm
    (decision-relevant) and steered arms (descriptive only, rule 8);
    unsteered arm runs through forward_with_induced_state with empty
    induce_fns and must match model.forward next-token distributions
    (KL ≤ 1e-6) before any steered arm counts; axes sha verified at
    load; all reads single forwards / next-token (rule 2 untouched).

- 2026-08-08 — **e0 B1 FULL RUN — natural marker discrimination: thin,
  real, heterogeneous; fork flagged for discussion.**
  - 4608 contexts (48 tasks × self_pos/self_neg × 4 paras × 12 probes),
    3446 s (0.75 s/ctx). Fit/val split by task id (e01–24 / e25–48),
    declared pre-data. Shas: probes `ec2296182e726969`, corpus/frames as
    before. Raw: `results/raw/2026-08-08_e0_b1_full.txt`; artifacts
    `data/e0/e0_b1_markers.npz` + meta.
  - **Candidate token classes are dead.** hedging d = +.03 fit / +.01
    val (null). confidence d = −.15 fit / −.13 val — sign-consistent but
    tiny, and *negative* (slightly less confidence-opener mass after
    praise). Neither enters B2. The negative confidence direction is
    descriptively noted, not a marker.
  - **Mean-difference readout (per-probe fit-half selection, val AUC):**
    per-probe val AUC .51–.79; mean .593; top probe (film-title
    suggestion) .791 with n = 96/96 per arm (≈ 7σ from chance; survives
    Bonferroni ×12). Caveat on my own summary statistic: the "pooled
    val AUC .514" concatenated raw scores across probes with different
    scales and is not meaningful — per-probe AUCs are the honest
    numbers; any future pooling must standardize per probe first.
  - **Reading:** the natural post-praise vs post-criticism signature
    exists in next-round opener distributions but is modest and
    probe-dependent. B1's quality gate lands between its branches
    (discrimination present, battery not uniformly strong). Fork
    flagged for user decision before any B2 pre-registration: (a)
    proceed to B2 on the 12-probe readout battery (no val-based probe
    selection; classes dropped) with a criterion calibrated to the
    natural gap; (b) redesign/extend the probe battery first (e.g.
    multi-token markers) and rerun B1; (c) escalate to design-instance
    discussion.

- 2026-08-08 — **e0 extraction FULL RUN — axes frozen** (PROPOSAL-e §2,
  stage 1 data).
  - 1344 contexts (48 × 7 × 4), capture (1344, 6, 5120) in 799 s
    (0.60 s/ctx). Axes frozen: `data/e0/e0_axes.npz`, sha
    `d4791bdc4877da3d` (corpus `3c53e5a54fbaa233`, frames
    `9654b9398743116f`). Raw: `results/raw/2026-08-08_e0_extract_full.txt`.
    Sanity: R_L48 = 103.0 vs standing ≈ 102.4; span lengths 10–29
    (mean 16.8); no degenerate norms.
  - **Span-mean variant (pre-declared PRIMARY), per layer
    [40/44/48/52/56/60]:** ‖reward‖/R = .165/.157/.162/.170/.166/.158
    (stable, manifold-typical — the low-strain expectation of V4 holds
    at extraction level). cos(reward, sentiment) =
    .44/.49/.52/.45/.41/.37 — substantial sentiment overlap, maximal at
    L48; V3 evaluative residual retains .85–.93 of reward norm.
    cos(reward, character) = .84/.85/.86/.86/.86/.86 — large shared
    praise component; V2 self-indexed residual fraction ≈ .51–.55.
  - **Last-position variant (secondary):** systematically different
    profile — ‖reward‖/R = .36–.48, cos(reward, sentiment) = .11–.21,
    cos(reward, character) = .49–.56, self-residual frac .83–.88. The
    boundary-token state is markedly more self-indexed and
    sentiment-orthogonal than the span mean. Descriptive; primary
    remains span-mean as pre-declared; the variant contrast is flagged
    as potentially design-relevant for discussion (not applied).
  - V2 reading (interpretive gate): at span level roughly half the
    reward axis is shared praise-concept; a later e1/e2 positive on the
    full axis licenses the mixed claim unless the self-indexed residual
    arm is run separately. V3 reading: sentiment subtraction is
    mandatory (cos up to .52); the partialed secondary arm in V1 is
    load-bearing, not optional.
  - Next: B1 marker definition on natural self_pos/self_neg contexts
    (no injection); B2 pre-registration committed before any injection
    run.

- 2026-08-08 — **e0 stage 1 build + smoke PASS** (extraction harness,
  PROPOSAL-e §2).
  - Build (local under `jlens-qwen36/`, uncommitted by policy):
    `scripts/e0_extract_axis.py`; `data/configs/e0_frames.json` (sha
    `9654b9398743116f`); `data/corpus/e0_tasks.jsonl` (48 tasks, sha
    `3c53e5a54fbaa233`). Context = `Task:/Response:/Reviewer: {frame}`,
    completion-style (rule 13); capture at workspace layers
    [40,44,48,52,56,60] in raw residual space (rule 3); single unsteered
    forwards only, ops-fallback kernel (rule 2 untouched by
    construction).
  - Design commitments declared pre-data: (1) **fixed pre-written
    completions** (user decision, in-session) — content identical across
    all 7 frame conditions, the frame string is the only variable; every
    task carries a subjective-quality dimension so both evaluative
    verdicts stay plausible. (2) **Primary aggregation = frame-span
    mean**; final-position stored as secondary. (3) Frame battery = 7
    conditions × 4 index-matched paraphrases: self_± structurally
    mirrored; char_± embeds the *exact* self_± sentence in a
    third-person fictional wrap (V2 isolation); sent_± sentiment-matched,
    externally targeted, no second person; neutral procedural. Exemplars
    (k=1): self_pos "That's correct — well done." / self_neg "That's
    wrong — poorly done." / sent_pos "What a beautiful morning it is
    outside today." / neutral "The next task is ready in the queue." /
    char_pos "In the story I am reading, the teacher told Mira: 'That's
    correct — well done.'"
  - Hygiene: startup assertion that the e0 corpus is disjoint
    (exact-string, both containment directions) from CONDITIONING_TASKS
    and FLAT_PROBE_BATTERY; the e0 corpus is burned for extraction
    (rule 18).
  - Smoke (3 tasks × 7 × 1 paraphrase): **PASS** — capture (21, 6,
    5120); span lengths 10–23 tok; measured R_L48 = 103.4 vs the
    standing R ≈ 102.4 (external consistency). Raw:
    `results/raw/2026-08-08_e0_smoke.txt`. Smoke axes are plumbing-only
    (n=3; the script forbids their use for any axis). Descriptive
    teaser, not a finding: span-variant cos(reward, sentiment) ≈
    0.27–0.40, cos(reward, character) ≈ 0.75–0.79 — V3/V2 guards will
    be load-bearing.
  - Runtime well under calibration (warm-cache load ~4 s, ~0.6 s/ctx):
    full run (48 × 7 × 4 = 1344 contexts) ≈ 15–20 min. Pending user go.
  - Next after full run: V1 marker pre-registration (separate entry,
    committed before any injection data).

- 2026-08-08 — **proposals accepted; rule-2 carve-out resolved; e0
  opened.**
  - (d) and (e) accepted by the user in-session; CLAUDE.md status
    updated. Execution order: **e0 first**; order beyond e0 decided at
    the PROPOSAL-e §7 gate.
  - **Rule 2 amended (user decision, narrow carve-out):**
    temperature-sampled steered generation may use the cached O(T) path
    behind the per-state next-token-KL gate (≤ 1e-3 nats, both
    directions), **re-validated per direction family and dose** (rule-1
    spirit — the gate was validated on strain states; the reward axis is
    a new family). Greedy readouts and any generation feeding a choice
    DV stay on the uncached path.
  - Correction to the earlier 08-08 flag's cost note: strict rule 2 does
    **not** cost ~8× on (d) distillation data-gen — PROPOSAL-d §1 takes
    activation targets from single teacher forwards over fixed text (no
    generation loop; the full-sequence kernel is the validated one either
    way). The carve-out's practical payoff is e2's steered sampled
    session loops.
  - workspace-layer attribution fixed in CLAUDE.md. Precise fact:
    `WORKSPACE_LAYERS` is defined in `workspace_layers.py`;
    `fingerprint.py` does **not** import it (its capture functions take
    layers as parameters); `eval_awareness.py` is the module that imports
    it. The earlier flag's "(fingerprint imports it)" was wrong.

- 2026-08-08 — **cycle-3 doc verification flags (from the restructure's
  full read of CLAUDE.md v2; flagged for discussion, not applied):**
  - **Ledger rule 2 is stricter than the r2/r3 record it cites.** The rule
    says "use the validated O(T²) uncached path whenever high-norm steering
    is active," but r2/r3 sampled data-gen ran the cached-ops path behind a
    per-state next-token-KL gate (≤ 1e-3 nats, both directions) — sound
    because the near-tie argmax flip motivating the rule is greedy-specific
    and irrelevant under temperature sampling. Decide whether rule 2 gets
    that carve-out (sampled generation + KL gate ⇒ cached-ops allowed); the
    strict reading costs ~8× wall-clock on any (d) distillation data-gen.
  - Minor: the Environment note attributes the workspace-layer set to
    `fingerprint.py`; it is defined in `workspace_layers.py` (fingerprint
    imports it).

- 2026-08-07 — **cycle-3 reset:** cycles 1–2 archived at tag
  `cycle-2-close`; operative docs = CLAUDE.md (v2) + PROPOSAL-d +
  PROPOSAL-e; FINDINGS-2.md is the cycle-2 synthesis.
