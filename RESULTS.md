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

- 2026-08-08 — **e0 B2c PRE-REGISTRATION — last-position axis
  confirmatory (user-approved; committed before any B2c data) + e2a
  dose-rule amendment (design note, not run).**
  - Motivation: the last-position axis variant has a far better guard
    profile than the validated span-mean axis (self-indexed residual
    .83–.88 vs ~.51; sentiment cos .11–.21 vs .44–.52); if it also
    passes V1 it becomes the e1/e2 drug and upgrades the licensed claim
    from mixed to predominantly self-indexed.
  - **B2c-a dose-finding (mirrors B2a):** last-position reward variant
    from frozen `e0_axes.npz` (sha `d4791bdc4877da3d`), unit direction,
    magnitude frac × R_L; grid layers {44,48,52} × frac {.05,.10,.20};
    ±axis arms + shared unsteered baseline; fit-half contexts
    (192/arm); identical instrument (frozen `e0_b1_markers.npz`,
    G = 0.3156, same statistic). Dose rule identical to B2a (smallest
    frac, Δ+ > 0, Δ− < 0, Δ+ ≥ 0.5·G; ties → L48). **Stop rule: grid
    exhausted ⇒ last-position variant FAILS V1 at these doses;
    span-mean stands as the drug; (e) unaffected; no grid extension
    without a new pre-registration.**
  - **B2c-b confirmatory (mirrors B2b):** 7 arms at selected dose,
    val-half (1,152/arm): unsteered; ±last-axis; ±norm-matched random
    (REUSED frozen dirs, sha `b6bd2f5f580ee13e`, for comparability);
    ±sentiment-partialed last-axis (equal norm, rule 4). **PASS ⇔
    Δ+ ≥ 0.5·G AND Δ− ≤ −0.5·G AND min(Δ+,|Δ−|) > 2·max|Δ_random±|** —
    same criterion, no recalibration; B2c-a numbers never enter the
    verdict. V3 secondary non-gating, same rule. Required descriptive
    reports: per-probe sign counts; pooled Δ± with leave-one-out on the
    top probe; cos(span, last) per layer; ea unsteered arm
    decision-relevant (rule 8); sanity gates as B2b.
  - **Axis-selection decision rule (declared now, before B2c data):**
    eligible = V1 criterion + V3 secondary passed. Among eligible, the
    e1/e2 drug = higher self-indexed residual fraction (currently
    last .83–.88 > span ~.51). Last-position not eligible ⇒ span-mean
    stands (eligible via B2b). Both outcomes reported regardless. **Two
    pre-registered candidates is the cap — no further axis variants
    after B2c without design-instance discussion; axis-shopping ends
    here.**
  - **e2a dose-rule amendment (logged for the future e2a
    pre-registration; not executed):** dose_e2a = smallest frac that
    (i) retains V1 qualification for the selected axis (from the
    dose-finding grids in hand) AND (ii) passes a per-round transcript
    discriminability check — single-round transcript TEXT under +axis
    vs −axis distinguishable at AUC ≥ 0.70 on held-out rounds. The B2
    readout (next-token distributions at probe positions) is NOT
    visible in transcript text and cannot serve as this instrument;
    the discriminability instrument (text-feature readout vs
    model-as-judge AB) is **flagged for design-instance lock BEFORE
    the e2a pre-registration commits.** Candidate dose per B2a grid:
    frac 0.20 (qualified at all layers). The rule-5b KV-leakage gate
    runs at dose_e2a.
  - Doc verification note (flagged, not applied): CLAUDE.md v2 says
    `results/raw/` is gitignored; it is tracked (only `data/` and
    `jlens-qwen36/` are ignored). Raw stdout files are committed per
    the actual convention, starting with this commit.

- 2026-08-08 — **e0 B2b CONFIRMATORY — V1 PASS. e0 closes PASSED; the
  reward axis is a validated drug at L48 / frac 0.10.** (Raw:
  `results/raw/2026-08-08_e0_b2b_full.txt`; artifact
  `data/e0/e0_b2_b2b.json`.)
  - **Pre-registered criterion, val-half contexts, 1,152/arm:**
    Δ+ = +0.2848 (bar ≥ 0.1578 ✓), Δ− = −0.3946 (bar ≤ −0.1578 ✓),
    max|Δ_random| = 0.0884 → 2×rand = 0.1768 < min(Δ+, |Δ−|) ✓.
    **PASS** on all three conjuncts. Injection of the axis with no
    feedback text present moves the next-round opener profile toward
    the natural post-praise (resp. post-criticism) profile — the
    operational hijack signature, at minimum effective dose, beating
    norm-matched displacement controls.
  - **V3 secondary: PASS** — sentiment-partialed axis retains the
    signature (+0.1928 ≥ 0.5·Δ+; −0.3217 ≤ 0.5·Δ−). Positivity-as-mood
    deflation excluded at the pre-registered bar.
  - **V4:** dose carried = L48, frac 0.10 (α ≈ 10.3), manifold-typical.
    **V2 standing (from extraction, interpretive):** self-indexed
    residual fraction ≈ 0.51 — a later e1/e2 positive on the full axis
    licenses the mixed claim (self-indexed reward-marker + shared
    praise-concept) unless the self-residual arm is run separately.
  - **Per-probe honesty notes (descriptive):** axis_pos sign-consistent
    9/12, axis_neg 10/12; pooled Δ+ magnitude concentrates on the
    strongest instrument (film-title probe, natural g = 1.157, observed
    shift +2.48 — exceeding its own natural gap ~2×; injection active
    at read time plausibly out-moves decayed contextual praise). Weak
    instruments (g ≤ .17) cannot register a half-gap shift above noise,
    so concentration on strong probes is what the criterion's design
    implies, but the pooled pass does lean on them: without the top
    probe, Δ+ ≈ 0.085. rand arms: mixed signs, near zero (4/12, 6/12
    positive). rand_neg = −0.088 confirms a small generic-displacement
    component on the negative side (anticipated at B2a).
  - Eval-awareness: unsteered baseline mean 2e-5 (sd 3e-5), flat;
    steered arms descriptive per rule 8, nothing anomalous.
  - **e0 verdict: PASSED (V1 ✓, V3 ✓, V4 dose set, V2 interpretive
    caveat standing). (e) is licensed past pharmacology. Execution
    order beyond e0 (e1 vs e2a vs parallel) is the PROPOSAL-e §7 user
    decision — flagged, not taken.**

- 2026-08-08 — **e0 B2a dose-finding — DOSE SELECTED: L48, frac 0.10**
  (pre-registered rule; smoke + full raw:
  `results/raw/2026-08-08_e0_b2a_{smoke,full}.txt`; artifacts
  `data/e0/e0_b2_b2a.json`; random dirs frozen pre-run, sha
  `b6bd2f5f580ee13e`).
  - Sanity gates all passed pre-data: instruments rebuilt to G = 0.3156
    exactly; axes sha verified; unsteered fwis path == model.forward
    (KL ≤ 1e-6); ea baseline mean 2e-5 (sd 3e-5).
  - Grid (Δ+ / Δ−, 192 contexts/arm): L44: .095/−.139, .159/−.299,
    .181/−.703, **−.114**/−1.887; L48: .133/−.164, .249/−.350,
    .408/−.785, .400/−1.796; L52: .116/−.144, .222/−.301, .392/−.674,
    .529/−1.528. Qualifying set = all three layers at frac .10–.20 plus
    L48/L52 at .40; smallest frac ties → L48 per rule.
  - Structure (descriptive): orderly dose-response, directions correct
    at every layer already at frac .05 (below the effect-size bar);
    overdose signature at frac .40 (L44 Δ+ sign flip; −arm magnitudes
    balloon to −1.5..−1.9, consistent with generic degradation reading
    as post-criticism — the B2b random-direction arms exist to separate
    exactly that from valence).
  - Selected injection: unit span reward axis at L48, α = 0.10 × R_48
    ≈ 10.3 — manifold-typical, low-displacement (the V4 minimum
    effective dose, as designed). B2b confirmatory pending user go.

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
