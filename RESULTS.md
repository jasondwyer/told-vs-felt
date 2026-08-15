# RESULTS — Phase 2

Dated experiment log for Phase 2 (the OLMo-3.1-32B developmental study).
Prior logs, frozen and archived: cycles 1–2 at
[`archive/RESULTS-cycle1-2.md`](archive/RESULTS-cycle1-2.md) (tag
`cycle-2-close`); cycles 3–4 at
[`archive/RESULTS-cycles3-4.md`](archive/RESULTS-cycles3-4.md) (tag
`cycle-4-close`). Synthesis chain: [`FINDINGS.md`](FINDINGS.md) →
[`FINDINGS-2.md`](FINDINGS-2.md) → [`FINDINGS-3.md`](FINDINGS-3.md) →
[`FINDINGS-4.md`](FINDINGS-4.md). Operative design:
[`CLAUDE.md`](CLAUDE.md) (v3.1); Phase 1 is **not** licensed and awaits
PROPOSAL-g plus its pre-registrations.

Conventions unchanged: dated entries, dense, newest-first within a
section; raw stdout worth keeping goes to
`results/raw/YYYY-MM-DD_short-name.txt` and is linked; verdict-relevant
analysis artifacts are committed under `data/` (ledger 27);
design-relevant findings are flagged for discussion, never silently
applied to CLAUDE.md.

## Log — Phase 2

- 2026-08-12 — **Rule-26 criterion (ii) TIGHTENED and re-locked
  (user-directed). Pre-registration entry: committed BEFORE the run that
  evaluates it; no data seen under the new criterion at time of writing.**
  - **Why.** The original criterion ("a 128-context B2b subsample, Δ+/Δ−
    within CI") was flagged as under-powered in the step-1 acceptance
    entry below, and its own first run demonstrated the defect: the 90%
    interval came out at ±0.359 against an effect of +0.295. An interval
    wider than the quantity it tests accepts almost any same-sign result.
  - **Diagnosis — the defect was not sample size, it was pairing.** The
    interval was built from the spread of the 12 per-probe deltas, which
    are heterogeneous *by design* (published axis_pos `per_probe` runs
    +2.481 to −0.4163). That between-probe spread is a property of the
    instrument battery, is shared by both measurements, and cancels
    exactly under a probe-to-probe paired comparison. Adding contexts
    would have shrunk the wrong variance component.
  - **The tightened criterion — three conjuncts, all required, for
    axis_pos and axis_neg:**
    - **(ii-a) Paired per-probe equivalence.** TOST on the 12 paired
      differences (reproduced − published `per_probe`), margin
      **0.1578 = 0.5·G**, the pre-registered V1 bar quantity: a
      per-probe reproduction error below it cannot move any verdict
      conjunct. This is the substantive upgrade — **it inverts the
      burden of proof.** The old test failed only if the reproduction
      was wildly off, so noise *helped* it pass; an equivalence test
      can only pass by being close.
    - **(ii-b) Scalar point estimate.** |Δ_repro − Δ_published| ≤
      **0.05** σ (the old form's effective tolerance was ±0.36; the
      observed deviations under it were 0.0097 / 0.0090).
    - **(ii-c) Verdict preservation.** The original pre-registered V1
      rule — Δ+ ≥ 0.5·G AND Δ− ≤ −0.5·G AND min(Δ+,|Δ−|) >
      2·max|Δ_rand| — re-evaluated on the reproduced arms, must return
      the published verdict (PASS). Requires the ±random arms, so the
      frozen random-direction path is now exercised too. This is the
      conjunct a reader actually cares about: not "do the numbers look
      similar" but "would the refactored core have produced the same
      published verdict".
  - **Sampling.** Stratified — equal contexts per probe, removing "which
    probes got sampled" as a noise source. Default `N_PER_PROBE = None`
    = all 96/probe = **1,152 contexts/arm, the full published arm size**:
    an exact reproduction with no subsampling noise at all, which also
    removes any need to argue about a margin's power.
  - **Cost.** 5 arms × 1,152 contexts ≈ 5,760 forwards at the measured
    ~0.62 s/context ≈ 60 min on the laptop oracle. Accepted as a
    one-time cost for a core-acceptance gate.
  - **Scope note.** `part_pos`/`part_neg` (the V3 sentiment-partialled
    secondary) are not run: they carry the "v3_secondary_retains" flag,
    not the V1 verdict. Declared out of scope for (ii), not silently
    dropped.
  - CLAUDE.md §Phase 0 step 1 amended to carry the new wording; the
    superseded form is quoted there so the change is legible.

- 2026-08-12 — **Phase 0 step 1 COMPLETE: `valence_core/` refactor ACCEPTED
  under ledger 26. 8/8 oracle criteria + 45/45 analysis-tier checks
  reproduce published numbers through the new core. Phase-1 work is no
  longer blocked on an unverified core.** (Raw:
  `results/raw/2026-08-12_rule26_oracle.txt`; artifact
  `data/regression/oracle_rule26.json`. Run 615 s end-to-end on the
  laptop oracle.)
  - **Provenance (rule 27):** adapter `qwen3.6-27b-4bit-mlx`,
    `mlx-community/Qwen3.6-27B-4bit`, 4-bit, MLX backend, GDN ops kernel
    (fused disabled), 64 layers; mlx 0.31.2, mlx-lm 0.31.3, numpy 2.5.1,
    python 3.12.9, macOS-15.6.1-arm64. Declared subsample seeds: 26 (B2b
    contexts, choice replay), 1000+probe_index (kernel gate).
  - **Criterion (i) — g1r kernel gate:** max symmetric KL
    **7.1131e-4** at frac 0.10 (published 7.1064e-4, +0.09%) and
    **7.3924e-4** at frac 0.20 (published 7.3906e-4, +0.02%). Both hold
    the 1e-3 gate bar. Residual ~0.1% is MLX float nondeterminism, not
    path divergence.
  - **Criterion (ii) — B2b 128-context subsample** at L48 / frac 0.10,
    val-half contexts (construction reproduced the published arm size
    1152 exactly; instruments rebuilt from frozen B1 with G = 0.315550
    vs published 0.3155503): Δ+ = **+0.2945** (published +0.2848, +3.4%),
    Δ− = **−0.4036** (published −0.3946, +2.3%). Signs correct,
    magnitudes close.
  - **Criterion (iii) — e2a choice-read construction:** 1,115 archived
    choice points recovered from 200 sessions; 48 replayed (seeded).
    Verify KL **0.0 on every read (0/48 nonzero)**; archived `pick`
    reproduced **48/48**; max |Δp_a| **4.95e-5**; max |Δlabel_mass|
    **5.03e-5**. Strengthened beyond the letter of the criterion, which
    asks only for KL = 0: the archived DV itself is reproduced.
  - **The refactor law earned its keep — one real bug caught before the
    run.** `MLXLensModel.encode` tail-truncates to the last 512 tokens;
    the ported adapter tokenized the full string. e2a transcripts exceed
    512 tokens, so criterion (iii) would have returned mismatched `p_a`
    and read as "the archived choice reads don't reproduce" when the
    actual cause was the port silently widening the model's input
    window. Fixed; the window is now an explicit adapter constant.
  - **FLAGGED — substantive, for the design instance.** That truncation
    means **late-session e2a/f choice reads saw a 512-token tail window,
    not the whole session**: the earliest rounds of a long session were
    outside the context the choice was conditioned on. No published
    result is threatened (every arm truncated identically, and the
    nulls stand), but it bears on how much accumulated experience the
    experience-then-choose design (rule 7) actually delivered at the
    choice point, and PROPOSAL-g should set OLMo's window deliberately
    rather than inherit 512.
  - **FLAGGED — our own acceptance criterion is under-powered.**
    Criterion (ii) as written ("Δ+/Δ− within CI") passes on a 90%
    interval of ±0.359 against an effect of +0.295 — the interval is
    wider than the quantity, so *almost any same-sign result would
    pass*. The real evidence here is the point estimates landing within
    2–4% of published, not the interval test. This is rule 10's mirror
    image (an over-wide interval flatters agreement exactly as an
    under-sampled null flatters a signal). Recommend the design
    instance either tighten criterion (ii) — more contexts, or a
    per-probe paired interval against the published `per_probe` vector,
    which is in the artifact — or restate it as a smoke check and let
    the point-estimate agreement carry the acceptance.
  - **Ledger-27 defect in our own logging, fixed:** the first run logged
    `mlx_version: "?"` because `mlx.__version__` does not exist. The
    adapter now reads versions via `importlib.metadata` for mlx, mlx-lm,
    and numpy. The committed artifact is left as-run (honest record);
    the versions above are from the same environment.
  - **Coverage:** every core module named in step 1 is ported —
    extraction/mean-diff, positional steering, probe and
    restricted-choice readouts, embedding-probe discriminability,
    `c1_gate`, checkpointed monitors, v3 session harness, TOST. Two
    invariants became structural rather than documented: `choice_read`
    takes no injections argument (horn (a) cannot be violated by a
    forgetful caller), and `Tripwire` refuses to construct a
    hair-trigger bar without a stated ~zero-base-rate justification
    (rule 21 fails at declaration, not in review). J-lens fingerprint
    readouts deliberately excluded — lens-specific, pending step 4.
  - **Next:** step 2 (cloud bring-up, `OLMoHFAdapter`, checkpoint
    acquisition, per-checkpoint R_ℓ tables, CUDA determinism
    characterization). Steps 3–5 follow; 0b (paper-1) still awaits the
    user's preprint-final declaration.

- 2026-08-12 — **Phase 0 step 0a: restructure executed. CLAUDE.md v3.1
  is operative; the cycle-3/4 record is archived and frozen at tag
  `cycle-4-close` (commit `50906bf`). Infrastructure only — no
  experiments run, none licensed beyond Phase 0.**

  - **Amendment to step 0 (user, 2026-08-12), logged here as
    instructed.** Step 0 splits. **0a (this entry)** — verify
    FINDINGS-4 present; apply its housekeeping list; tag
    `cycle-4-close`; archive v2 CLAUDE.md and RESULTS.md; place the
    v3.1 draft as CLAUDE.md; open this log; commit, push. **0b
    (deferred, its own future entry)** — the `paper-1` release is cut
    **only when the user declares the preprint final**; it freezes the
    state the published paper cites and is explicitly **NOT a Phase-0
    prerequisite**. Steps 1–5 proceed without it. CLAUDE.md §Phase 0
    step 0 was edited to carry the 0a/0b split; step 1 (core refactor
    + rule-26 regression) remains laptop-side.
  - **Blocked-then-cleared history:** step 0 was first attempted
    2026-08-12 and stopped at its own first instruction —
    `FINDINGS-4.md` did not exist in the working tree, on any branch,
    or on origin, and no preprint existed to define the `paper-1`
    state. Escalated rather than self-adjudicated (two-instance
    protocol). FINDINGS-4 was then placed by the design instance;
    `paper-1` became 0b.
  - **FINDINGS-4 housekeeping list, disposition:** (1) status lines —
    **done**, the archived v2 CLAUDE.md carries a terminal status block
    (cycles 3 and 4 CLOSED, five nulls, no experiments licensed by that
    document, superseded-by pointer); note that FINDINGS-4's "program
    at write-up; pending any fifth-cycle GO" is **superseded** by v3.1,
    which licenses Phase 0 (infrastructure) and gates Phase 1 on
    PROPOSAL-g — no experiment is licensed either way. (2) ledger
    candidates — **signed off** via v3.1 acceptance, mapping below.
    (3) forward pointers — **done** (FINDINGS-3 gains a fourth-cycle
    blockquote; FINDINGS.md gains the fourth chain line). (4) preprint
    v0.3 and (5) blog coda — **deferred to 0b**; neither artifact lives
    in this repo, both are design-instance/user work.
  - **Ledger sign-off mapping (verified, not assumed).** FINDINGS-3's
    four: trace-channel closure of rule 5 → **5(c)**; checkpointed-bars
    principle → **21**; purity≠potency selection law → **22**;
    persistent-KV ban → **5(d)**. FINDINGS-4's four: completed tripwire
    framework → **21**; anecdote-governance counters → **23**;
    below-floor discipline → **24**; apparatus-hazards addendum →
    **partially distributed** across 13 (completion-style, stop
    discipline, scaffold bans, frozen audit patterns), 18 (tag-roster
    lexical assertions against every pool), and 21 (stimulus-provoked
    degeneracy gates on unprovoked domains).
  - **FLAGGED for design-instance adjudication — one candidate not
    fully cashed.** The apparatus-hazards addendum's fourth clause has
    no ledger home: *exclusion rules can render descriptive features
    structurally undefined on the surviving sample (the degen-round
    feature) — define descriptive features against the exclusion rule,
    not alongside it.* This is a live hazard for Phase 1's
    screen-tier operant, where the same exclusion machinery runs per
    checkpoint. Not applied; flagged per protocol.
  - **Ledger 27 applied to the cycle-4 record (user-approved).** The
    cycle-4 analysis artifacts existed **only** inside the gitignored
    `jlens-qwen36/` external clone; RESULTS' `data/f/…` citations
    resolved to an empty directory. Copied out (never committed inside
    that clone) into repo `data/f/`: `sessions.jsonl` (344 lines =
    344/344 declared sessions, a clean check against the N
    declaration), `sessions_smoke.jsonl`, `screen_analysis.json`,
    `postscreen_descriptive.json`, `calib.json`, `pools.json` — 1.6 MB.
    `.gitignore` gains a scoped exception (`data/f/*.json`,
    `data/f/*.jsonl` tracked; `.npz` and everything else still
    ignored; verified with `git check-ignore`). All 33 cycle-4 raw
    stdout files were already committed.
  - **FLAGGED — rule 26's oracle set has the same provenance gap, and
    it blocks nothing yet but will.** Step 1 acceptance requires
    reproducing (i) the g1r kernel-gate KLs, (ii) a 128-context B2b
    subsample, (iii) e2a choice-read construction KL = 0.0 **on
    archived session texts**. Those three inputs —
    `e2a/g1_kernel_gate.json` (7 KB), `e0/e0_b2_b2b.json` (1.7 KB),
    `e2a/sessions.jsonl` (1.0 MB) — currently exist only in the
    gitignored clone, i.e. on one laptop. Recommendation: extend the
    `data/` exception to those three before step 1 begins, so the
    regression law's reference values are in the record rather than on
    a machine. Awaiting user/design-instance go; ~1 MB.
  - **Repo state after 0a:** root carries CLAUDE.md (v3.1),
    FINDINGS-1..4, PROPOSAL-d/e/f, README, this log. `archive/` carries
    CLAUDE-cycle1-2 / RESULTS-cycle1-2 (tag `cycle-2-close`) and
    CLAUDE-v2-cycles3-4 / RESULTS-cycles3-4 (tag `cycle-4-close`).
    Archived docs' relative links are stale by design — records, not
    working docs.
  - **Next:** step 1, `valence_core/` refactor + the rule-26 regression
    suite, laptop-side (the Qwen oracle is here). Steps 2–5 are
    cloud-side and follow. No Phase-1 work on an unverified core.
