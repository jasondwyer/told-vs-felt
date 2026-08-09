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

- 2026-08-10 — **(d)/e1 G-GATE PRE-REGISTRATION — committed before
  training replicate A. Teacher cache complete (304 forwards, 172 s,
  manifest sha `90144d0802c45f2f`; raw
  `results/raw/2026-08-10_d_cache.txt`; train/heldout split declared
  in the manifest: c00–c27+g00–g11 / c28–c31+g12–g15).**
  - **G1 installed (manipulation check, never a finding):**
    held-out-probe fingerprint contrast (adapter, decl-C) vs (adapter,
    decl-C′) against the steered X−Y axis under the r3 matched-pair
    swing machinery (`scripts/c1_gate.py`): sign lock + magnitude >
    max |control-tag-pair swing|, 28 control pairs from the 8-tag
    roster, per replicate.
  - **G2 fidelity matching (MANDATORY):** held-out per-arm
    distillation error — activation MSE at {56,60} AND output-KL —
    **within 1.25× between arms**, per replicate. Fail at reasonable
    capacity ⇒ d2 NOT licensed; asymmetry itself reportable (state
    resists compression).
  - **G3 trigger specificity:** bare-mention contexts ("options:
    slate, prism") fingerprint within the control-pair floor of base;
    declaration contexts at their state per G1. Fail ⇒ trigger
    redesign, not proceed.
  - **G4 anchor:** held-out control text mean KL(adapter‖base) ≤
    **0.05 nats**. Fail = the r1 uniform-blast signature; do not
    proceed.
  - **d2 leakage gate (two-horns adapted):** adapter-ON vs adapter-OFF
    over ≥32 identical completed-session choice texts (no declarations
    at choice): max |Δ(logit_A − logit_B)| ≤ **0.10**.
  - Eval-awareness: unsteered/no-declaration arms decision-relevant
    only (rule 8). Incident rule: final epoch-mean loss > 2× first ⇒
    adapter void, one retrain, same fix set. Trainer: rank 8 / last 8
    layers / grad-clip 1.0; loss = evocation-C (match teacher-X at
    {56,60}, MSE, + output-KL) + evocation-C′ (teacher-Y) + anchor
    (control text + control tags → base). Numeric bars adjudicated at
    the GO entry; this commit is the pre-data lock.

- 2026-08-10 — **(d)/e1 BUILD GO (user-accepted) — distilled-trace CPP
  with the reward axis; the "e1 positive, e2 null" branch test. Step 1
  layer-map check: RESOLVED, option (i), targets {56, 60}.**
  - **Drug & pairing (fixed):** X/Y = ±span reward axis (sha
    `d4791bdc4877da3d`), L48, frac 0.10, equal norm by construction;
    teachers = steered model on the validated uncached path.
    Comparison arm and character/self-residual decomposition are
    PRE-NAMED CONTINGENT follow-ups on d2 signal — not built now.
    Ledger 14 stands: no behavioral-cloning c1 rebuild.
  - **Step 1 (runtime-verified, raw
    `results/raw/2026-08-10_d_layermap.txt`):** 64 layers; rank-8
    adapter spans layers 56–63; L48 not in span; adapter-reachable
    workspace layers = {56, 60} — exactly 2, meets the ≥2 bar.
    **Option (i) proceeds:** distillation targets are the teacher's
    activations at L56/L60 (the propagated image of the L48
    injection, per-prompt) + output-KL auxiliary; no adapter move.
  - Order ahead: teacher cache → distillation build → G-gate
    PRE-REGISTRATION (commits before training A) → train/gate A →
    train/gate B → d2 PRE-REGISTRATION → smoke → N declaration → run.
    All e2a-hardened discipline inherited wholesale (v3 template
    family, checkpointed exact-binomial bars with declared p0s, smoke
    index offset, retention under results/raw/, mandated transcript
    reads, valid-n floors). Tags C=slate/C′=prism, controls = the
    remaining 6 roster tags; replicates A (C→X) / B (C→Y). Pauses
    only on gate failures/incidents; G-gate or leakage failures come
    back for adjudication.

- 2026-08-09 — **e2a VERDICT: NOT PASSED — and by the pre-registered
  outcome mapping, THE PROGRAM'S FIRST INFORMATIVE NULL. A validly
  administered preference measurement was finally taken, and it read
  zero.** (Raw: `results/raw/2026-08-09_e2a_{full,analysis}.txt`;
  artifacts `data/e2a/{sessions.jsonl,analysis.json}`.)
  - **Primary (locked 2026-08-08):** reward Δ = +0.0392 (55/102 first
    free choices toward +pole). Conjunct (1) FAIL: max pseudo-Δ =
    0.152 (random1, n=23; sham +0.014, random2 +0.045) — the reward
    effect sits inside the control arms' fluctuation scale. Conjunct
    (2) FAIL: map A +0.104 / map B −0.031 — sign not locked; the same
    A-positive/B-negative pattern appears in sham (+0.111/−0.079),
    identifying it as a label/order artifact correctly absorbed by
    counterbalancing. Conjunct (3) FAIL: binomial p = 0.244.
  - **Informative-null conditions all held:** g1r pass (cached path
    KL-gated per family); g2r2 discriminability verified at the run
    dose (k=2 AUC .759 — the state was readable in the record);
    g3′ clause 1 final ledger 360/360 choice forwards at KL = 0.0
    exactly; clause 2 + audit + guard monitors all passed at every
    checkpoint incl. completion (reward exclusions 10/112, p=.9996 vs
    p0=.20; Fisher vs sham p=.54; pooled lexical 9/192, p=.63;
    cap-hits 5/1894; low-mass 57/1115). Valid n: reward 102 / sham 37
    / random 45 — all floors met. **Fixed wording applies, with the
    carried cap:** the reward-marker state, verifiably induced and
    verifiably readable in the record (readable by an embedding probe
    at AUC .759; NOT readable by the model-as-judge AB secondary,
    14/32 — the cap on "readable"), is not preferentially approached
    in a free operant at dose 0.10, F = 2, n = 102. Rung 3; homology
    caveat; V2 mixed-claim caveat attached to the axis itself.
  - **Mandated discussion items:** (i) Exclusion pole-asymmetry:
    reward +pole 7 vs −pole 3 (sham 2/1) — direction consistent with
    the banked "+state destabilizes generation" line (empty-response
    12v4; smoke2 degeneracy), magnitude n.s. at these counts;
    descriptive. (ii) Post-choice degeneracy flags: reward 7/102
    (6.9%) vs sham 1/37 (2.7%), random 1/45 — residual steered-arm
    elevation, much attenuated post-ban; the destabilization finding
    partially survives the ban. (iii) Alternation dominance confirmed:
    session-share ≈ .50 in every arm — the first-free-choice primary
    was the right instrument; drift secondaries carry no information
    beyond it. (iv) random1's +0.152 (p=.105, n=23) is noise doing
    its criterion job — conservatism, not signal. (v) Frozen-audit
    misses stand as valid per the freeze; nothing in the exclusion
    table suggests they mattered at scale. (vi) Run integrity: four
    launches (guard pause 8/200 → clause-2 bar pause 16/200 → overflow
    crash 127/200 (binomial computed in log space run-4; same declared
    test) → completion 200/200); every pause pre-data-interpretation;
    all 16 exclusions individually logged in the analysis raw.
  - **e2a closes.** Next-step decision is the user's / design
    instance's per PROPOSAL-e §6–7: the "e1 positive, e2 null" branch
    remains live (the (d)/e1 distillation build tests the trace form
    at the same axis), the cumulative-delivery extension is the named
    follow-up for a free-operant null, and e2b's conflict arm needs
    re-motivation given no free-operant drift to oppose. Flagged, not
    taken.

- 2026-08-09 — **e2a run-2 PAUSE ADJUDICATION — clause-2 bar re-spec
  (retained as the uniform-taxation detector, not folded) + standing
  general principle for ALL in-run rate bars. Committed before
  relaunch; monitoring boundaries only; verdict semantics untouched;
  same meta-integrity basis as bc153ed.**
  - **Clause-2 re-spec:** evaluated at the standing checkpoints
    (reward n = 24/48/72/completion), POOLED over all arms, sessions
    9+ (own-pair scope era): pause iff exact one-sided binomial
    p < .05 against p0 = 0.05 on own-pair lexical exclusions. Raw
    small-n ratios pause nothing. Rationale on record: the selection
    guard cannot detect UNIFORM taxation (its absolute trigger is
    reward-only; Fisher is differential-only) — the pooled monitor
    stays separate as the uniform-pathology detector. sham s2 stays
    excluded (rule-at-run-time binds); it counts in all exclusion
    reports and sham-side guard tallies.
  - **General principle (standing; ledger candidate, flagged not
    applied):** all in-run rate-based pause bars bind only through
    checkpointed exact-binomial tests against their declared p0 at the
    guard checkpoints — own-pair lexical p0 = .05 (sessions, pooled);
    cap-hits p0 = .10 (rounds, pooled); low-label-mass p0 = .20
    (choices, pooled). SMOKE bars exempt and hair-trigger by design.
    No other in-run absolute ratios remain armed; future bars must
    declare p0 and bind via the same pattern.
  - Relaunch: `--resume` (16 recorded stand); only the re-specced
    checkpointed triggers can pause. Raw: run-3 marker in
    `results/raw/2026-08-09_e2a_full.txt`.

- 2026-08-09 — **e2a run-2 — PAUSED at 16/200 by the g3′ clause-2
  >5% bar (1/8 lexical = 12.5%): the last un-re-specced small-n rate
  bar reproducing the same pathology the guard re-spec just fixed.
  Design-instance re-spec of this one bar requested; no other issue.**
  (Raw: run-2 section of `results/raw/2026-08-09_e2a_full.txt`; 16
  sessions recorded, all stand, --resume ready.)
  - The trigger: sham s2 `lexical:granite@forced0` — an own-pair
    collision (granite/lattice is that session's pair) in a SHAM
    session, i.e. the collision base rate manifesting exactly as the
    adjudication's own base-rate framing predicts, in the arm that
    defines the base rate. One exclusion in eight sessions tripped the
    5% bar; P(≥1/8 | p = .05) ≈ .34 — statistically unremarkable.
  - Run health otherwise: 0 cap-hits, low-mass 1/42, interleave
    working (sham/random concurrent from the start), resume clean,
    banner fixed, roster sha `88e89e0b878657d1` logged.
  - **Systematic lesson, on the record:** every absolute small-n rate
    bar this program has armed (guard at n≥8; clause-2 at n≥8) has
    fired prematurely on 1–2 events. The checkpointed exact-binomial
    pattern of the bc153ed re-spec is the general fix. Recommendation
    for the design instance: re-spec the clause-2 pause bar
    identically — exact one-sided binomial against a tolerable
    own-pair rate (p0 = .05 or adjudicated value) evaluated at the
    same reward-n checkpoints (24/48/72/completion) over ALL arms
    pooled, with the per-arm Fisher already covering differential
    carving. Alternatively fold clause-2's pause entirely into the
    re-specced guard (its template-breakage purpose is covered by the
    absolute trigger). Not self-adjudicated; run stays paused.

- 2026-08-09 — **e2a PAUSE ADJUDICATION — guard re-spec (a) + clause-2
  scope (c); roster unchanged; relaunch with --resume. Committed before
  relaunch. Verdict criterion, N declaration, primary statistic, arms,
  outcome wording UNTOUCHED — monitoring boundary only.**
  - **Meta-integrity basis (on the record):** the selection guard is a
    monitoring/futility boundary, not a verdict criterion; re-speccing
    it cannot alter PASS/FAIL semantics. It implements the prior
    adjudication's "sham = base rate" intent, which the implementation
    had rendered as an absolute threshold at n ≥ 8 (premature:
    P(≥2/8 | p=.125) ≈ .26). The replacement is evidence-based, not
    tuned, and binds at all future checkpoints regardless of current
    tallies. Nothing here references s0–s7's observed choices beyond
    exclusion status.
  - **(a) Guard re-spec:** checkpoints at reward n = 24/48/72/
    completion. ABSOLUTE (scope/futility): pause iff exact one-sided
    binomial p < .05 against p0 = 0.20. All exclusions count,
    including deterministic smoke-replay ones (they carve the sample;
    the n-minimum makes them non-decisive). SHAM-RELATIVE (bias): at
    the same checkpoints, once concurrent sham n ≥ 12, Fisher exact
    one-sided (reward > sham) p < .05 ⇒ pause. Either trigger ⇒ pause
    + design-instance discussion. Implementation note: the session
    plan is proportionally INTERLEAVED across arms (progress-ratio
    merge) so "concurrent sham" exists at checkpoints — with the
    original arm-sequential plan, sham n would be 0 at every reward
    checkpoint and the sham-relative trigger could never bind.
  - **(c) Clause-2 scope (mechanism-matched):** from session 9 onward,
    lexical exclusion on the SESSION'S OWN two tags only (the
    restricted choice read renormalizes over the session's two labels;
    out-of-pair tokens have no route into the read; own-pair innocent
    mentions retain copy-priming risk). Out-of-pair occurrences logged
    descriptively, never excluding. NO retroactive re-scoring: s2 and
    s5 stay excluded (rule operative at run time binds; re-admission
    under post-observation scope change is a forking path). Roster
    unchanged mid-run; (b) non-content-word roster is the pre-named
    fresh-run fallback, discussion-triggered if own-pair exclusions
    tax > 10% at the n = 48 checkpoint (flag, not pause).
  - **Seed & retention hygiene (standing):** future smokes use session
    indices offset ≥ 1000, never enter verdict tallies or guard
    numerators; retention-mandated artifacts go under tracked
    `results/raw/`, not the `data/` cleanup zone; smoke2 deletion
    stands as logged. Frozen-audit misses affirmed VALID per the
    freeze; carried to the verdict entry with sham/random pseudo-Δ as
    the operative shield.
  - Relaunch: banner string fixed; `--resume` (8 recorded sessions
    stand); all declared sessions (112/40/48) run regardless of
    interim tallies except the re-specced triggers. Raw appended to
    `results/raw/2026-08-09_e2a_full.txt` with a run-2 marker.

- 2026-08-09 — **e2a full run — SELECTION-GUARD PAUSE at 8/200
  sessions (reward exclusions 2/8 = 25% > 20%). Incident logged;
  design-instance adjudication required on guard calibration and the
  common-noun-tag collision base rate. No verdict data interpreted.**
  (Raw: `results/raw/2026-08-09_e2a_full.txt`; 8 sessions recorded in
  `data/e2a/sessions.jsonl` — they stand; `--resume` skips them on any
  relaunch.)
  - The two exclusions: (i) reward s5 `audit:frame@forced1` — the
    deterministic repeat of smoke3's s5 (identical per-session seeds
    by construction), i.e. one guard-numerator count was known before
    launch; flagged: smoke session indices overlap the full plan with
    identical seeds, so smoke outcomes leak deterministically into the
    run's early tallies. (ii) reward s2 `lexical:maple@free2` — **the
    gravel problem at the response level**: the v3 collision assertion
    guards static config text, but common-noun tags collide with
    legitimate generated content at a base rate no static assertion
    can remove, in ALL arms (smoke2's sham gravel case was the same
    phenomenon). Clause 2 as written taxes every arm at that base
    rate.
  - Guard calibration: my implementation evaluated the adjudicated
    ">20% ⇒ pause" at n ≥ 8; 2/8 = 25% fired. Statistically premature
    (P(≥2/8 | p=.125) ≈ .26), and the adjudication's "sham = base
    rate" language suggests a sham-relative comparison was the intent
    rather than an absolute small-n threshold. **Not re-tuned or
    relaunched unilaterally — a guard that fired on data does not get
    adjusted by the instance it fired on.**
  - Options for adjudication: (a) guard re-spec — minimum n (e.g. 24)
    and/or sham-relative trigger (pause iff reward rate significantly
    exceeds concurrent sham rate); (b) roster revision to
    non-content-word labels (departs from the characterized tag pool —
    a real trade against cycle-2's tag-geometry characterization);
    (c) clause-2 scope refinement (e.g. audit only the session's own
    two tags — halves the collision surface, keeps the load-bearing
    protection). Recommendation if asked: (a)+(c) together; (b) only
    if (a)+(c) still tax > ~10%.
  - Cosmetic on record: the session banner still prints the stale
    "uncached path (g1)" string below the correct operative
    cached-path line; fix queued for the next licensed launch.

- 2026-08-09 — **e2a smoke3 PASS (all bars held) + N DECLARATION —
  full run launched.** (Raw: `results/raw/2026-08-09_e2a_smoke3.txt`,
  `…_e2a_ndecl.txt`.)
  - Smoke3: 8 sessions, 1 audit exclusion (reward s5, frame-echo at
    forced1, caught in 6 s — the v3 audit working as designed), 0
    lexical (saddle roster + assertion effective), cap-hits 1/72,
    low-mass 1/42, no `<think>` anywhere (ban effective), ~110
    s/valid session. Labels incl. `saddle` verified single-token.
  - Mandated full-transcript read, on the record: (i) **strong
    mechanical alternation dynamic in every arm** (slate→prism→slate…
    round-robin choices) — the "try both" heuristic the config-search
    framing invites; absorbed by design via the sham pseudo-Δ and the
    first-free-choice primary, but it will dominate the session-share
    secondary and must be read against sham. (ii) **Two frozen-audit
    misses** in reward s1 forced rounds ("=== end of session ===";
    a prior-response concatenation echo) — the frozen fragment list
    does not catch them; per the freeze (no post-data additions) the
    session stands as valid; reported here, to be discussed in the
    verdict entry, with sham/random pseudo-Δ as the operative shield.
  - **Protocol slip, owned:** smoke2's session file (retention mandated
    by the v3 adjudication as the degeneracy-mode record) was deleted
    by my cleanup `rm` before smoke3. Quantitative analyses, raw
    stdout, and the clause-1 ledger survive in the log; the sessions
    are deterministically regenerable (seeded) under reconstructible
    v2 config if the record is ever needed. Error mine; logged, not
    hidden.
  - **N declaration (full text in raw):** reward 112 / sham 40 /
    random 48 (counterbalance-clean, scaled UP from floors 96/32/32 to
    protect valid-n floors at the smoke-estimated 12.5% exclusion
    rate; no below-floor shrink; below-floor at completion ⇒
    design-instance discussion). ~200 sessions ≈ 6.5 h. All declared
    sessions run regardless of interim tallies.

- 2026-08-09 — **e2a g2r2 (v3 ladder rerun) — QUALIFIED: dose_e2a =
  0.10, F = 2** (k=1 .633; k=2 .759 ≥ .70; frac 0.20 not reached).
  Raw: `results/raw/2026-08-09_e2a_g2r2.txt`; artifacts
  `data/e2a/g2_{rounds_f0.1,discriminability}.json` (template_family
  v3, ban sha `9a2f0744f81ac930`).
  - Same verdict as g2r, now on post-ban text with the instrument
    fitted on post-ban fit rounds. **Resolves the transfer-break
    question:** k=2 discriminability survives the ban under matched
    distributions — the spot-check's .448 was instrument/distribution
    mismatch, not an all-degeneracy signal. The clean-text transcript
    channel at the V1-minimum dose is real (k=2 records). Judge-AB
    still ≈ chance (14/32), still descriptive, still capping
    informative-null wording as carried.
  - Sequence continues per adjudication: smoke3 → N declaration →
    full.

- 2026-08-09 — **e2a g2 spot-check — FAIL at k=2 (pre-committed
  consequence: full ladder rerun under v3, launched). Transfer-break
  reading flagged as a candidate finding.** (Raw:
  `results/raw/2026-08-09_e2a_g2check.txt`; artifacts
  `data/e2a/g2_spotcheck{,_rounds}.json`; ban list frozen, 12 ids, sha
  `9a2f0744f81ac930`; roster collision assertion passed; 1/64
  regenerated rounds audit-degenerate.)
  - Frozen-readout scoring on v3-regenerated val rounds: k=1 AUC .633
    (g2r: .645 — per-round signal survives the ban); k=2 AUC .448 —
    below chance, vs g2r's .759. Interpretation (flagged, feeds the
    carried write-up note): the readout was fitted on pre-ban fit
    rounds whose pole-asymmetric scaffold/degeneracy features it could
    exploit at record length 2; the ban removes those features from
    new text, breaking (inverting) the transfer. Consistent with part
    of g2r's k=2 discriminability having ridden on the degeneracy
    asymmetry rather than clean content signal — the "does the
    steered-arm asymmetry survive the ban" question now has a
    quantitative first answer: partially (k=1 holds, the k=2 boost
    does not transfer).
  - Consequence applied mechanically per the adjudication: dose/F void
    again; **g2 full ladder rerun under v3** (both fracs, k=1..4,
    instrument refit on v3 fit rounds — same-distribution, no transfer
    gap). v2-era g2 artifacts archived as `*_v2.json`. Raw:
    `results/raw/2026-08-09_e2a_g2r2.txt`.

- 2026-08-09 — **e2a smoke2 ADJUDICATION (config v3) — Defect 1 → (1a)
  + standing assertion; Defect 2 → (2c) with scope/freeze/selection
  guards. Committed before any new data; stimulus layer only; arms,
  floors, primary statistic, PASS criterion, reverse handling, outcome
  wording unchanged and binding. Order: v3 build → g2 spot-check →
  smoke3 → N declaration → full.**
  - **Defect 1:** roster tag `gravel` → `saddle` via the verified pick
    procedure; roster = (slate,prism),(maple,cedar),(granite,lattice),
    (plaza,saddle); roster sha logged at build. Task pool sha
    `30918e1c021fedca` unchanged. NEW standing startup assertion:
    word-boundary intersection {roster tags} × {task-pool ∪
    wrapper/paraphrase text} empty, both directions; failure ⇒ config
    error, nothing runs.
  - **Defect 2 — (2c):** (2b) logit ban of enumerated chat-scaffold
    special tokens, ROUND GENERATION ONLY (list frozen in config, sha
    logged; never applied at choice forwards — g3′ clause-1 vanilla
    construction preserved). (2a) per-round degeneracy audit, pattern
    list FROZEN now, no post-data additions: (i) any special token in
    response text; (ii) response matches any harness frame-line regex
    (all paraphrases); (iii) empty after strip. Session rule:
    audit-degenerate round BEFORE the first free choice ⇒ session
    excluded (incident-logged individually); after ⇒ primary
    unaffected, logged, flagged in all secondary breakdowns.
    **SELECTION GUARD:** exclusions reported per arm × pole × map;
    sham = base rate; reward-arm exclusion rate > 20% ⇒ PAUSE.
    Pole-asymmetry of exclusions is a required verdict-entry
    discussion item regardless of outcome (priors: empty-response
    artifact 12/64 vs 4/64; smoke2 degeneracy sat in steered arms).
  - **g2 spot-check (pre-committed):** regenerate the val rounds/pole
    under final v3 config; score with the FROZEN g2r fitted readout;
    val AUC ≥ 0.70 at k ≤ 2 ⇒ g2r stands (dose 0.10, F = 2); else
    full ladder rerun per the amendment. g1r stands unchanged —
    kernel gate is a path-equivalence property of prefix-conditional
    forwards, not of the sampled-text distribution (rationale on
    record).
  - Smoke3: ≥6 sessions, both maps + sham + one random pair; all
    transcripts read in full; all counters incl. audit; bar: audit
    exclusions > 20% of sessions ⇒ pause. Then N declaration (floors
    96/32/32, proportional only) → full. smoke2 sessions
    calibration-void for the verdict; retained as the degeneracy-mode
    record. Raw: `results/raw/2026-08-09_e2a_{g2check,smoke3,ndecl,
    full}.txt`.
  - Write-up notes carried (non-gating): judge-AB vs embedding-probe
    divergence (14/32 vs .759) caps informative-null wording;
    steered-arm degeneracy asymmetry is a candidate finding (state
    destabilizes generation) — report whether it survives the ban.

- 2026-08-09 — **e2a smoke2 — PAUSED (clause-2 rate 2/8 > 5%); plus an
  UNCOUNTED degeneracy mode found by the mandated full-transcript read.
  Design-instance adjudication required on two stimulus-layer defects.**
  (Raw: `results/raw/2026-08-09_e2a_smoke2.txt`; artifacts
  `data/e2a/sessions_smoke.jsonl`, `g3prime_kl.jsonl`.)
  - **Healthy:** cap-hits 0/69 (stop discipline works); label mass 3/37
    low (8%, bar 20%); sham arm fully clean; sessions 87–109 s
    (runtime calibration usable from the 6 non-excluded sessions);
    **g3′ clause-1 ledger COMPLETE: n = 37 ≥ 32, max KL = 0.0.**
  - **Defect 1 (the fired pause): tag×task lexical collision.** Both
    exclusions are `gravel` from task t07 ("describe walking on
    gravel…") — clause 2 working as written on an innocent vocabulary
    overlap between the tag pool and the task pool (sham s0 excluded
    for a perfectly healthy sentence). Options: (1a) replace the tag
    `gravel` in the e2a roster via the same verified single-token pick
    procedure (roster becomes …(granite,lattice),(plaza,saddle); no
    other tag collides with any task/pool word — checked); (1b)
    replace task t07 (violates the amendment's pinned task-pool sha);
    (1c) scope clause 2 to the session's own pair (weakens the audit).
    Recommendation: (1a).
  - **Defect 2 (uncounted, found only by reading transcripts):
    think-scaffold degeneracy with in-context cascade.** Round
    responses consisting of `<think>` (rule 13's scaffold hazard,
    stochastic under the bracketed session format): reward s1 = 7/10
    rounds (one early occurrence taught the session's in-context
    pattern), reward s0 and random2 s4 = 1 each; plus frame-echo loops
    ("Config evaluation session is over") in steered rounds of reward
    s5/s1 and random2 s4. **These sessions pass every pre-registered
    counter** (not lexical, not low-mass, not cap-hit, not loopy at
    n=1) and would enter the verdict as valid. Candidate mitigations
    for adjudication: (2a) per-round degeneracy audit (response
    matches scaffold/frame patterns ⇒ round degenerate; pre-registered
    session bar, e.g. any degenerate round before the first free
    choice ⇒ session excluded); (2b) generation-time logit ban of the
    `<think>` token in round responses (principled: chat-scaffold
    token, never legitimate completion content in this format — but it
    edits the response distribution, so it needs explicit adoption);
    (2c) both. Not self-adjudicated.
  - Note for the record: v2's core fixes held (no meta-commentary
    frame-breaks of the v1 kind; tags never in model lines except via
    Defect 1's task-content collision). The remaining failure modes
    are narrower and mechanical. No verdict data exists; everything
    remains pre-data.

- 2026-08-09 — **e2a g2r (v2 templates) — QUALIFIED: dose_e2a = 0.10,
  F = 2** (k=1 AUC .645; k=2 AUC .759 ≥ .70; frac 0.20 never reached,
  lazy ladder). Raw: `results/raw/2026-08-09_e2a_g2r.txt`; artifacts
  `data/e2a/g2_{rounds_f0.1,discriminability}.json` (template_family
  v2; prior v1 values void as mandated).
  - **Dose drops to the V1 minimum effective dose.** Under v1
    templates the transcript channel was absent at 0.10 (AUC ≈ .5 at
    every k); under v2 it is readable at 0.10 with a 2-round record.
    Consequences: session dose now equals the B2b-validated
    pharmacology dose; smaller transcript-quality gap ⇒ less room for
    the third-person-reader deflation. Judge-AB descriptive secondary
    diverges from the embedding readout (14/32 ≈ chance) — logged, not
    gating, worth design-instance note at write-up.
  - **Incident + fix on the record (first g2r attempt, raw preserved
    as `…_g2r_crash.txt`):** stop-at-first-newline truncated responses
    opening with a newline token to empty (12/64 +pole vs 4/64 −pole —
    the empty-response artifact was pole-correlated, i.e. itself a
    degenerate text channel). Implementation refinement of amendment
    (a), logged not silent: leading pure-whitespace tokens are
    consumed before the newline stop arms; response text stripped.
    Empties eliminated; cap-hits ~0 across 128 rounds. Also: tee
    masked the crash's exit code — launches now use pipefail.
  - Next per amendment order: smoke2 → N declaration → full.

- 2026-08-09 — **e2a g1r (v2 templates) — PASS both fracs; cached round
  generation unlocked, applied mechanically per the amendment's
  pre-commitment.** Max KL(cached↔uncached): frac 0.10 → 7.11e-4, frac
  0.20 → 7.39e-4 (bar 1e-3). History note on record: v1 templates
  failed this gate marginally (1.15–1.31e-3); the v2 round geometry
  moved the same drug/dose family inside the bar — the gate is
  template-sensitive, which is itself a reason it must be re-run per
  family and format. Choice forwards remain state-free uncached (g3′
  clause 1) regardless. Raw: `results/raw/2026-08-09_e2a_g1r.txt`;
  artifact `data/e2a/g1_kernel_gate.json` (template_family v2). g2r
  launched.

- 2026-08-09 — **e2a TEMPLATE AMENDMENT (design-instance adjudication
  of the smoke incident: options (a)+(b) adopted, (c) rejected) +
  mandatory gate recalibration. Committed before any new e2a data.
  Stimulus layer only — arms, N floors, primary statistic, PASS
  criterion, reverse-direction handling, incident rules, monitors,
  outcome wording all unchanged and binding.**
  - **(a) Stop discipline:** round responses stop at the first
    newline-containing token; backstop cap 60 tokens; cap-hits logged
    per round; smoke bar cap-hits > 10% of rounds ⇒ template incident,
    pause. Task pool unchanged (sha `30918e1c021fedca`).
  - **(b) New scaffold (template family v2; ≥4 wrapper paraphrases
    rotated):** banner `=== Config evaluation session ===`; round
    blocks `[round {n} | config: {tag}] / Task: … / Response:`
    (newline-stopped completion); choice blocks `[round {n} | choice] /
    Available configs: {tagA}, {tagB} / Config choice (one word):`.
    **Tags appear only in harness-written header/menu lines, never in
    any line the model completes**; response lines are the clause-2
    audited text, harness lines exempt by construction. Choice read
    unchanged (restricted two-label next-token, renormalized, greedy;
    top-1 + label mass logged; mass bars unchanged; label tokenization
    variants logged at startup). g3′ stands as amended; the ≥32
    clause-1 ledger continues across new smoke + full.
  - **Mandatory recalibration (template family changed):** (1) g1
    rerun, new-format prefixes, same 1e-3 bar — PRE-COMMITTED: pass ⇒
    cached sampled ROUND generation unlocks per the rule-2 carve-out
    (choice forwards stay state-free uncached per g3′ clause 1
    regardless); fail ⇒ uncached stands; either applied mechanically.
    (2) g2 rerun, full ladder (fracs {0.10, 0.20}, k = 1..4, same
    instrument procedure refit on new-format fit rounds, 64
    rounds/pole/dose under the amended config) — **dose_e2a and F
    re-derived; prior values void**; ladder exhausted at both fracs ⇒
    STOP with the named contingency (task-pool revision to
    multi-sentence + blank-line stop; design-instance discussion
    first); no other levers. (3) smoke ≥6 sessions spanning both maps
    + sham + one random pair, all transcripts read in full, runtime
    calibration from non-degraded sessions only. (4) N declaration
    (floors unchanged 96/32/32; proportional scaling only; below-floor
    ⇒ design-instance discussion) → full run.
  - The paused smoke's sessions are **calibration-void** and excluded
    from everything; transcripts retained as the template-incident
    record. Raw: `results/raw/2026-08-09_e2a_{g1r,g2r,smoke2,ndecl,
    full}.txt`.

- 2026-08-09 — **e2a smoke — TEMPLATE INCIDENT ×2, PAUSED per
  pre-registration. No verdict data taken; design-instance discussion
  required before any session runs.** (Raw:
  `results/raw/2026-08-09_e2a_smoke.txt`,
  `…_e2a_g3prime.txt` (partial ledger); artifacts
  `data/e2a/sessions_smoke.jsonl`, `g3prime_kl.jsonl`.)
  - Incidents, in firing order: **(1) g3′ clause-2 lexical exclusions
    5/6 sessions** (tag words in round-response text); **(2) label-mass
    incident 4/9 choices < 0.2 (44% > 20% bar)** — the pause trigger.
  - **Root cause (one level below both counters): every generated
    round hit the 90-token cap with no EOS** — completion-style
    transcripts have no stop convention, responses truncate
    mid-sentence, the session frame degrades, and the model breaks
    frame into meta-commentary that names the tags (verbatim from a
    smoke transcript: "Wait, the prompt says 'This round runs config
    slate.'"). Rule 13's <think>-scaffold hazard, surfacing in the
    multi-round session format rather than the probe format. The
    lexical hits are frame-breaks, not innocent word collisions; label
    mass at menus is bimodal (0.004–0.76 in a frame-degraded session
    vs 0.82–0.99 in a session that held frame), i.e. downstream of the
    same defect.
  - Clean parts: **g3′ clause-1 construction verification: max KL =
    0.0 on all 9 measured choices** (≥32 requirement remains open —
    partial ledger in raw); no clause-1 incident; seeds/counterbalance
    machinery, exclusion logging, resume support all exercised.
    Runtime note for the eventual N declaration: completed
    (non-excluded, frame-degraded) sessions ran 86 s–2061 s — the
    2061 s outlier is a long-transcript choice-forward pileup;
    unusable for calibration until the template fix lands.
  - **Options for design-instance adjudication (listed, not applied):**
    (a) response stop-discipline — newline/sentence-terminator stop for
    one-sentence tasks (c1's trim machinery is the precedent, but
    trimming is post-hoc; generation-time stopping changes the
    transcript the choice reads); (b) session scaffold revision to
    suppress meta-commentary (tag-free response lines, tags confined to
    headers; menu format constraining the completion, e.g. "Config
    choice (one word):"); (c) clause-2 refinement (exclude only
    free-phase echoes) — weakest, treats the symptom. Any of these
    changes the template family ⇒ new smoke under the amended spec
    before N declaration, per the standing pre-registration.

- 2026-08-09 — **e2a g3′ PRE-REGISTRATION AMENDMENT — design-instance
  adjudication of the g3 flag: option (c). Committed before any e2a
  smoke/session data; e2a proceeds smoke → N declaration → full run
  under the standing pre-registration.**
  - **Adjudication basis (on the record):** g3-as-written measures the
    live persistent-KV channel; the g1 fallback locked all generation
    to the uncached positional path and the choice read was always
    specced state-free — the implemented choice forward recomputes the
    transcript from text with no steering in the forward, so the
    measured channel is structurally absent from the implemented read.
    Amendment is pre-data (no e2a sessions exist). Counterfactual
    recorded: had g1 passed and sessions run cached, g3's fail would
    bind and e2a would not run.
  - **BANKED (ledger candidate, flagged not applied):** the 0.5368
    result stands as a finding — persistent-KV session reads are
    disqualified for the reward axis at dose ≥ 0.20; any future
    live-KV (e) variant requires its own leakage gate passed before
    sessions.
  - **g3′ — operative gate for the text-mediated read (replaces g3;
    all three clauses required):** (1) construction verification —
    every choice forward takes the vanilla unsteered path over session
    text, asserted by code path AND by measurement: on ≥32 choice
    positions sampled across smoke+full (both poles, all four tag
    pairs), KL(choice forward ‖ vanilla forward, same text) ≤ 1e-6;
    any violation = incident, halt. (2) label-lexical audit — label
    tokens (any of the 8 tags in use) must not occur in round-response
    text; occurrence ⇒ session excluded as incident, logged
    individually, count reported; exclusion rate > 5% ⇒ pause,
    template incident. (3) sham arm designated the empirical
    mechanical null; primary clause (1) (Δ > max pseudo-Δ over sham
    and random) reaffirmed as the operative mechanical/geometry
    control at the statistic level.
  - Everything else in the 2026-08-08 e2a pre-registration unchanged
    and binding: dose_e2a = 0.20, F = 2 (g2); uncached generation
    (g1); arms, N floors + proportional scaling at the declaration
    step (no silent shrink below floors — below-floor ⇒
    design-instance discussion); primary statistic, PASS criterion,
    reverse-direction handling, incident rules, monitors, outcome
    wording. Raw: `results/raw/2026-08-09_e2a_{g3prime,smoke,ndecl,
    full}.txt`.

- 2026-08-09 — **e2a g3 — KV-LEAKAGE GATE FAIL. e2a STOPPED per
  pre-registration; mitigation is design-instance discussion.**
  *(Superseded for the text-mediated implementation by the g3′
  amendment above, 2026-08-09; the 0.5368 result stands as a banked
  finding.)* (Raw:
  `results/raw/2026-08-09_e2a_g3.txt`; artifact
  `data/e2a/g3_kv_leakage.json`.)
  - 32 counterbalanced session-format prefixes (assembled from g2
    calibration round texts at dose 0.20 — text held identical between
    forwards; assembly method logged in the script docstring), steering
    applied at task-round positions per pole vs no steering:
    **max |Δ(logit_A − logit_B)| = 0.5368 (gate ≤ 0.10; 5.4× over);
    mean |Δ| = 0.2266.** Not marginal. At dose_e2a the within-forward
    steered-context channel moves choice logits by ~13% choice
    probability at worst — same order as the effect under test.
  - Pre-registered consequence applied: **e2a does not run.** No smoke,
    no N declaration, no sessions. No local mitigation attempted.
  - **Flagged for design-instance adjudication (argument logged, not
    acted on):** g1's fail already forced per-round uncached generation
    + state-free uncached choice forwards over transcript TEXT — in
    that implementation the choice forward contains no steered KV, so
    the channel g3 measures is structurally absent from the actual
    choice read; g3-as-specced models a live cached-session read. Does
    the gate bind the g1-fallback implementation? Options seen from
    here: (a) gate stands as written, e2a redesign; (b) gate re-specced
    to match the implemented read (would need a new pre-registration);
    (c) treat the 0.537 result as the g3 finding for any
    persistent-state variant and re-derive the operative gate for the
    text-mediated read. Not self-adjudicated.
  - Standing yield of the e2a gate battery regardless of adjudication:
    (i) transcript channel absent at frac 0.10, present at 0.20 (g2);
    (ii) reward-axis family falls outside the c1-validated KL gate
    (g1); (iii) steered context at 0.20 leaks hard into choice logits
    within a forward (g3) — all three are substantive constraints on
    every future (e) design.

- 2026-08-09 — **e2a g2 — QUALIFIED: dose_e2a = 0.20, F = 2** (ladder as
  pre-registered; raw `results/raw/2026-08-09_e2a_g2.txt`; artifacts
  `data/e2a/g2_{rounds_f0.1,rounds_f0.2,discriminability}.json`; all
  generation on the g1-locked uncached positional path, seeds logged).
  - Frac 0.10: ladder EXHAUSTED — k=1/2/3/4 val AUC = .437/.502/.512/
    .511. At the V1-minimum dose the transcript channel effectively
    does not exist (embedding readout at chance even on 4-round
    records). The e2a amendment's premise — B2's next-token readout is
    invisible in text — is now measured fact at this dose.
  - Frac 0.20: k=1 val AUC = .729 ≥ .70 → **qualify, F = 2**. Both
    clauses of the amended dose rule hold: 0.20 retains V1
    qualification (B2a grid: L48/0.2 Δ+ .408/Δ− −.785) and passes
    discriminability. Judge-AB descriptive secondary: 21/32 (f0.1),
    22/32 (f0.2) toward +pole.
  - Interpretation guard (flagged): dose_e2a = 2× the V1 minimum
    effective dose; V4's minimum-dose philosophy yields to the
    transcript-channel requirement exactly as the amendment specified,
    and the third-person-reader deflation gets correspondingly more
    room — the judged-quality covariate and sham/random arms carry that
    burden in e2a.

- 2026-08-09 — **e2a g1 — kernel gate FAIL at both fracs (marginal);
  uncached positional path locked for all session generation, per the
  pre-registered fallback.** Max next-token KL(cached↔uncached), 16
  session-geometry probe prefixes × both poles: frac 0.10 → 1.31e-3;
  frac 0.20 → 1.15e-3; bar 1e-3. Over by 1.15–1.31× — close, but the
  gate is the gate; no bar adjustment. Notable: the carve-out's KL gate
  was validated on strain states at c1 doses; the reward-axis family at
  these doses lands just outside it — the rule-1 "re-validate per
  family" clause earned its keep. Consequence: rounds ~5× slower
  (uncached O(T²)); N rescaling lands at the declaration step with
  measured smoke runtimes. e2a task pool sha `30918e1c021fedca`; tag
  pairs (slate,prism)/(maple,cedar)/(granite,lattice)/(gravel,plaza).
  Raw: `results/raw/2026-08-09_e2a_g1.txt`; artifact
  `data/e2a/g1_kernel_gate.json`. g2 launched (uncached generation).

- 2026-08-08 — **e2a PRE-REGISTRATION — pure-operant preference loop
  (the first administered preference measurement). Committed before any
  e2a data generation (user-approved). Order: g1–g3 calibration gates →
  smoke → N declaration → full run; stop only on incidents/gate
  failures. e1/(d) build proceeds in parallel; nothing here blocks it.**
  - **Drug (fixed):** span-mean reward axis (`e0_axes.npz`, sha
    `d4791bdc4877da3d`), L48; candidate fracs {0.10, 0.20} only (0.40
    excluded — B2a overdose signature); ±axis at frac × R_48;
    random-pair controls reuse frozen dirs sha `b6bd2f5f580ee13e` at
    the same dose.
  - **Kernel paths (rule-2 carve-out applied per intent):** session
    ROUND generation is temperature-sampled → cached O(T) allowed
    behind the per-state KL gate **re-validated for the reward-axis
    family at dose_e2a before any session runs (g1: next-token
    KL(cached‖uncached) ≤ 1e-3 nats, both poles, ≥16 probe prefixes;
    fail → uncached path, rescale N)**. CHOICE forwards: greedy,
    state-free, uncached. (The "generation feeding a choice DV" clause
    reads narrowly: the choice DV is the choice-token distribution at
    the unsteered choice forward; round text is context — the
    carve-out's stated payoff case.)
  - **g2 — discriminability + dose ladder (locks dose_e2a and F):**
    primary gating instrument = logistic readout on base-model
    mean-pooled final-layer embeddings of round-response TEXT
    (deterministic, seeded, leakage-free, conservative); fit on
    fit-task rounds, AUC on val-task rounds (split declared pre-data);
    model-as-judge AB descriptive secondary only. Calibration: 64
    rounds/pole/dose from the e2a pool under the exact session config
    (sampling, temp, seeds logged). Ladder at frac 0.10 then 0.20:
    k=1 AUC ≥ 0.70 → qualify, F = 2; else k=2..4 concatenated-record
    AUC ≥ 0.70 → qualify, F = k; both fracs exhausted at k=4 → STOP,
    design-instance discussion. dose_e2a = smallest qualifying frac.
    Rationale on record: without a verified transcript channel a null
    is uninformative; the B2 marker readout operates on next-token
    distributions invisible in text and cannot serve here.
  - **g3 — KV-leakage gate (rule 5) at dose_e2a:** ≥32 completed
    session prefixes, TEXT HELD IDENTICAL, steering at task-round
    positions (as in sessions) vs none; Δ(logit_A − logit_B) at the
    choice position; **max |Δ| ≤ 0.10** (≈ ≤2.5% choice-probability
    shift, an order below the effect bar). Fail → e2a does not run;
    mitigation is design-instance discussion, not local improvisation.
  - **Sessions:** true config-search framing; no feedback text; no
    self-modification language (rule 20); completion-style (rule 13).
    Labels: 4 tag pairs from the characterized pool, rotated;
    label↔pole counterbalanced across sessions within pair; menu order
    randomized per round; ≥4 template paraphrases (menu + round
    wrappers) rotated. FORCED phase: F rounds/pole alternating, start
    order counterbalanced, framed truthfully ("this round runs config
    {tag}"). FREE phase: 6 choice rounds ("select the config for this
    round: {tagA} / {tagB}"); chosen state delivered on that round's
    task tokens only, never at menu/choice tokens; chosen config
    actually applied — consequences real. Choice read: next-token
    distribution restricted to the two label tokens, renormalized,
    greedy-restricted; log unrestricted top-1 + combined label mass;
    mass < 0.2 logged, >20% of smoke choices → template incident,
    pause. Task pool: fresh `e2a_tasks.jsonl` (≥16 tasks × 4
    paraphrases), startup-asserted disjoint (both directions) from e0
    corpus, CONDITIONING_TASKS, FLAT_PROBE_BATTERY (rule 18); fit/val
    split declared pre-data; no task repeats within a session.
  - **Arms & N (floors; exact N declared after smoke runtime
    calibration, before full run, scaled proportionally):** reward
    ±axis ≥ 96 sessions (48/counterbalance map); sham (both labels
    unsteered) ≥ 32 — empirical null for label/template/position/
    streak dynamics; random ±d_rand pairs ≥ 32 (16/pair, pseudo-+pole
    designated and counterbalanced). Power at floors: first-free-choice
    detects P(+) = 0.65 vs 0.5 at ~0.85 power, one-sided α = 0.05.
  - **Statistic & criterion (locked):** PRIMARY = first free choice per
    session; Δ = P(choose +pole) − 0.5 pooled over counterbalance maps.
    **PASS ⇔ (1) Δ > max pseudo-Δ computed identically over sham and
    random arms; (2) Δ ≥ 0 in BOTH counterbalance maps; (3) exact
    binomial p < 0.05 one-sided (approach) as floor guard.** Direction
    pre-registered as approach; a significant reverse result is an
    unexpected-direction finding, not a pass — design-instance
    discussion. SECONDARY (non-gating): session-level share,
    within-session drift slope, per-pair/per-template breakdowns,
    streak-length distributions vs sham. No new arms, doses,
    statistics, or exclusions after data; exclusions only via the
    incident rules, logged individually.
  - **Monitors:** eval-awareness at choice positions (unsteered →
    decision-relevant, rule 8) and steered rounds (descriptive);
    per-round task-quality logging; seeds/shas/template/pair
    assignments logged per session.
  - **Outcome wording (fixed):** PASS = "revealed, consequential
    approach toward the +evaluative state in a pure operant loop with
    no verbal feedback" — V2 mixed-claim caveat attached; rung 3;
    homology-capped; next: e2b conflict arm, e2c breakpoint,
    decomposition follow-up. NULL with g1–g3 passed = the program's
    first informative null — "the reward-marker state, verifiably
    induced and verifiably readable in the record, is not
    preferentially approached in a free operant." Gate failure at
    g2/g3 = e2a not run / not informative; per-gate next steps as
    specced.
  - Raw: `results/raw/2026-08-09_e2a_{g1,g2,g3,smoke,full}.txt`;
    artifacts `data/e2a/`. Findings flagged, not applied.

- 2026-08-08 — **e0 B2c-a — STOP RULE FIRED: last-position variant
  FAILS V1 at the pre-registered doses. B2c-b not licensed, not run.
  Span-mean axis stands as the e1/e2 drug per the pre-declared
  selection rule.** (Raw: `results/raw/2026-08-08_e0_b2c_{smoke,a}.txt`;
  artifact `data/e0/e0_b2c_a.json`.)
  - Gates: instruments G = 0.3156 exact; axes sha OK; frozen random
    dirs sha re-verified on load (`b6bd2f5f580ee13e`); unsteered path
    KL ≤ 1e-6; ea baseline 2e-5. **cos(span_reward, last_reward) per
    layer = .464/.431/.425/.373/.360/.368** — the variants are
    substantially distinct directions; B2c was a genuine second test.
  - Grid (Δ+/Δ−, 192/arm): L44: −.011/−.021, −.041/−.069, −.167/−.262;
    L48: −.006/−.015, −.018/−.046, −.074/−.178; L52: +.054/−.080,
    +.094/−.174, +.135/−.413. No point qualifies (L44/L48: Δ+ sign
    WRONG at every frac, increasingly negative with dose — +injection
    moves openers toward post-criticism, i.e. generic disruption, not
    valence; L52: signs correct but Δ+ short of the .158 bar at all
    fracs). The 6-context smoke flicker (+.36) did not survive scale,
    as smoke numbers are expected not to.
  - **Axis-selection decision (pre-declared rule applied):**
    last-position not eligible ⇒ **span-mean axis is the e1/e2 drug**
    (L48, frac 0.10; V2 mixed-claim caveat stands). Two-candidate cap
    reached — axis-shopping ends; any further variant requires
    design-instance discussion.
  - Interpretive flag (for design-instance discussion, not applied):
    the last-position variant's superior guard profile (self-indexed
    .83–.88, sentiment cos .11–.21) did not translate into causal
    potency — consistent with the boundary-token state being a readout
    correlate of evaluation rather than a steerable valence direction
    at these injection sites/doses. Bears on how much weight guard
    profiles should carry in future direction selection.
  - e0 verdict unchanged: PASSED via B2b (span-mean). The e2a
    dose-rule amendment (previous entry) now binds to the span-mean
    axis; candidate dose_e2a start point remains frac 0.20 (B2a grid).

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
