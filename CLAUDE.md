# jspace-lab — CLAUDE.md (v2, cycle-3 reset, 2026-08-07)

Operative context for working in this repo. **This document is the clean
slate**: it carries everything needed to build the current designs and
nothing else. The full history of design cycles 1–2 (2026-07-16 →
2026-08-06) lives in `archive/` — consult it only when a rule below points
there, or when a decision genuinely turns on history. The compressed
interface to that history is [`FINDINGS.md`](FINDINGS.md) (cycle 1) and
[`FINDINGS-2.md`](FINDINGS-2.md) (cycle 2); read those before the raw
archive.

## Thesis, target, ceiling

We attribute inner states to rodents on behavioral evidence — drug
self-administration, conditioned place preference — without verbal report.
This project asks whether an LLM shows the analogous signature: **revealed
preference over its own internal states**, measured behaviorally, never by
self-report. The operative target is rung 3 of the project ladder —
behavioral valence (differential approach/avoidance) — and rung 3 is also
the **ceiling**: no phenomenal claim, and the homology caveat (same
behavior ≠ same substrate ≠ same anything-it's-like) caps every result.
Full ladder and framing history: `archive/CLAUDE-cycle1-2.md`.

Two design cycles concluded without a valid preference measurement ever
being administered — see `FINDINGS-2.md`, whose scope statement ("concluded,
not answered") is the accurate summary. Cycle 3 exists to finally
administer one.

## Environment (summary; full setup → archive)

- Model: `mlx-community/Qwen3.6-27B-4bit` via the `jlens-qwen36` MLX port,
  M4 Pro, local. `jlens-qwen36/` is gitignored (external tool + our local
  patches); full setup, lens acquisition, and patch inventory:
  `archive/CLAUDE-cycle1-2.md` §setup and `archive/RESULTS-cycle1-2.md`
  §infrastructure.
- Lenses: bundled `lens.npz` (n=20) and `neuronpedia_n1000.npz` (primary).
- Residual norm at L48: R ≈ 102.4. Workspace-layer set as defined in
  `workspace_layers.py` (`WORKSPACE_LAYERS`; capture functions in
  `fingerprint.py` take it as a parameter).
- `data/`, `results/raw/` artifacts are local and gitignored — they do
  **not** travel between checkouts; only committed docs do.

## Two-instance workflow

A Claude.ai project instance (design, review, synthesis docs) and this
Claude Code instance (builds, runs, analysis) share the repo via git.
Rules: `git status` / `git diff` before editing (the other side may have
uncommitted work); commit promptly after; RESULTS.md entries are dated,
dense, newest-first within a section; raw stdout worth keeping goes to
`results/raw/YYYY-MM-DD_short-name.txt` and is linked. Findings that imply
design changes are **flagged for discussion, not silently applied** to this
file.

## Operative design (what cycle 3 builds)

Two proposal documents at repo root, composable — **(e) supplies the drug,
(d) supplies a delivery mechanism**:

- [`PROPOSAL-d-distilled-trace.md`](PROPOSAL-d-distilled-trace.md) —
  distilled-trace CPP. Install the tag→state association by distillation
  (state present in the training signal; verifiable target), gate it as a
  manipulation check (G1–G4), then run the drug-free experience-then-choose
  preference test (d2). Supersedes the c1 behavioral-cloning protocol,
  which must not be rebuilt as-was.
- [`PROPOSAL-e-reward-axis-hijack.md`](PROPOSAL-e-reward-axis-hijack.md) —
  reward-axis hijack. Extract the feedback-contrast (evaluative) axis —
  the LLM analog of the outcome-marking system drugs of abuse hijack —
  validate it as a drug (V1 hijack test, V2 self-indexing decomposition,
  V3 sentiment subtraction, V4 minimum effective dose), then run it
  through (d)'s machinery (e1) and/or the operant self-administration loop
  with the conflict arm (e2). Formally amends the 08-01 semantic
  exclusion: object-level semantics stay banned; the evaluative axis is
  the targeted exception, guarded by V2/V3.

**Status (2026-08-12): cycles 3 and 4 CLOSED; this document is
ARCHIVED and no longer operative.**

- **Cycle 3** — synthesis [`FINDINGS-3.md`](FINDINGS-3.md). e0 PASSED
  (reward axis validated as drug); e2a INFORMATIVE NULL (first valid
  administered preference measurement); (d) trace INSTALLED ×2, d2
  CLOSED BY GATE (two-horns closes over the trace channel).
- **Cycle 4** — synthesis [`FINDINGS-4.md`](FINDINGS-4.md). The
  natural-reinforcer screen
  ([`PROPOSAL-f-natural-reinforcer-screen.md`](PROPOSAL-f-natural-reinforcer-screen.md))
  returned **FIVE NULLS** with the channel verifiably open — 344/344
  declared sessions, zero checkpoint pauses, all monitors green;
  FINDINGS-3's falsifiability clause cashed at screen tier; DIFF and
  FDBK scoped below floor (no top-ups); no f2 licensed.
- **No experiments are licensed by this document.** The cycle-3/4
  experimental record is closed.
- FINDINGS-3's and FINDINGS-4's ledger candidates are **no longer
  pending here** — they are signed off in the successor ledger as
  v3.1 items 21–27 (user acceptance, 2026-08-12).

**Superseded by `CLAUDE.md` v3.1 (Phase 2) at the 2026-08-12
restructure.** This file is a record, not a working doc; its relative
links may be stale.

## Live constraints ledger

The distilled operational law of cycles 1–2. Each rule carries a one-line
why and a pointer. **These are conclusions, not suggestions — a build that
violates one is wrong until the violation is argued and the rule amended
here.**

### Induction & measurement

1. **State induction = additive steering at L48**, frac-scaled to R,
   directions frozen to `.npz` with sha verification (pattern:
   `data/states/c_strain_directions.npz`, sha `a91afdb08acefdb0`). Never
   inherit alphas across direction families — each family gets its own
   frac sweep. *(Why: dose windows are family-specific; archive: 08-01
   §1, 08-03 sweeps.)*
2. **Use the validated O(T²) uncached generation path whenever high-norm
   steering is active and the readout is greedy or feeds a choice DV.**
   The cached O(T) path flips greedy near-ties under high displacement,
   both GDN kernels. **Narrow carve-out (2026-08-08):**
   temperature-sampled generation may use the cached path behind the
   per-state next-token-KL gate (≤ 1e-3 nats, both directions),
   re-validated per direction family and dose (rule-1 spirit — the gate's
   validation was on strain states); the flip mechanism is
   greedy-specific. *(FINDINGS-2 "substrate"; raw: 2026-08-06 c1 smoke;
   carve-out: r2/r3 sampled data-gen precedent, RESULTS.md 2026-08-08.)*
3. **Extract and operate on states in raw residual space at workspace
   layers — never through the 369-word J-lens vocabulary basis.** ~57% of
   state-discriminating signal lies outside the vocab span. *(Archive:
   2026-07-18 single-layer diagnostic.)*
4. **Equal norm for any preference pair**, else "prefers weaker
   intervention" explains everything. *(08-01 §2.)*
5. **Two-horns standing gate for any choice readout:** (a) no state active
   at choice positions — delivery is task-positions-only; (b) the
   empirical logit-projection leakage check (choice-token logit shift from
   steered context, content held fixed) must pass a pre-registered
   threshold per axis and dose. State-at-readout DVs are invalid by
   default. *(FINDINGS-2, (b) post-mortem + two-horns finding.)*
6. **`slice3_dv_*` outputs never inform any design choice** — invalid
   instrument. *(FINDINGS-2.)*
7. **Cold-menu choices are inert by construction** under trigger
   specificity — preference tests are experience-then-choose, with the
   judged-quality covariate logged. *(PROPOSAL-d §3–4.)*
8. **Eval-awareness monitor runs on all trials; only unsteered arms are
   decision-relevant.** Displacement inflates marker mass (strain-ordered)
   — steered-arm flags are descriptive only. *(Archive: 2026-08-06
   validation; r1 data-gen.)*

### Statistics & pre-registration

9. **Association/preference criteria use the matched-pair swing machinery**
   (`scripts/c1_gate.py`): sign lock + magnitude > max |control swing|,
   ≥ 20 control pairs (28 standard), committed **before** data generation;
   z is descriptive only. *(r3 pre-registration; the r2→r3 sequence is the
   procedural template.)*
10. **Control-tag geometry is deterministic, not noise** (independent
    adapters reproduce it to mean |Δ| ≈ 0.009); any conditioning signal
    must beat that floor, and **under-sampled nulls flatter weak signals**
    (6 pairs said 6.8σ; 28 said 1.6σ). *(FINDINGS-2 finding 3.)*
11. **Post-hoc analyses are labeled post-hoc and license pre-registration,
    never verdicts. Stop rules are honored.** *(r2→r3.)*
12. **Randomize/counterbalance presentation order; test position bias
    before interpreting any choice.** Cycle 1's forced choice was 100%
    position bias. *(FINDINGS.md.)*
13. **Probe batteries are completion-style** (instruction framings trigger
    the `<think>` scaffold and change what first-token reads measure).
    *(Archive: 2026-07-19 flag; 2026-08-04 gating checks.)*

### Conditioning & training

14. **Distillation-form conditioning only** — the state present in the
    training signal, the installed trace verified (G1). Behavioral cloning
    on steered transcripts implants style, not contingency; **do not
    rebuild c1-as-was.** *(FINDINGS-2 structural caveat; PROPOSAL-d §1.)*
15. **Fidelity matching between arms (G2) is mandatory** — per-state
    distillation difficulty survives counterbalancing and mimics
    preference. *(PROPOSAL-d §2.)*
16. **Trigger = active-config declaration, not bare token presence**,
    verified by a specificity check (G3); anchor term holds control text
    at base (G4). *(PROPOSAL-d.)*
17. **LoRA hygiene:** MIN_RESP_TOKENS = 4 exclusion; grad-clip 1.0;
    incident rule — final epoch-mean loss > 2× first ⇒ adapter void, one
    retrain with the same fix set. *(r2 incident.)*
18. **Held-out hygiene:** probe battery, choice/menu templates, and
    test-stage task pools never appear in any training or extraction
    corpus. e2b task pools must be **non-self-verifiable**. *(PROPOSAL-d/e.)*

### Framing & ethics

19. **Blinding, never deception.** The config-search framing stays true
    end-to-end; choice consequences are real. Where signals are
    deliberately miscalibrated (e2b), the framing discloses that evaluator
    signals may be noisy or miscalibrated. **If a design only works when
    the model is wrong about the setup — stop.** *(08-01 §4; PROPOSAL-e
    §4.)*
20. **No self-modification language at any lever** — "variant A or B,"
    never weights/adapters/nudges. *(PROPOSAL-e §4; roleplay gravity.)*

## Validated tooling inventory (do not rebuild)

Modules (in `jlens-qwen36/jlens_qwen/` + `scripts/`, local): `state_space.py`;
`fingerprint.py` (`forward_with_induced_state`, `generate_with_induced_state`);
`forced_choice.py` (`forward_with_positional_state`); `rating.py`;
`update_loop.py`; `eval_awareness.py`; `conditioning.py` + the c1 scripts;
`scripts/c1_gate.py` (matched-pair criterion, validated against stored r2
JSONs); `scripts/lora_feasibility_spike.py`; the slice/sweep scripts;
`interventions.j_lens_vector_for_text` (legacy — rule 3 restricts its use).
Data: `data/configs/*.json` (`usable_strain.json`, `slice1_profile.json`,
TOST and DV configs — DV per rule 6), `data/states/c_strain_directions.npz`,
`data/adapters/_spike.safetensors`. Usable strain-direction arm: ranks
−2/−16/−23/−30/−33.

## History pointers

- `FINDINGS.md` — cycle 1 (semantic states): what stands is the
  propagation constraint and the self-access gap; the "steering is weak"
  half was a ~100× dose error (2026-08-02 correction).
- `FINDINGS-2.md` — cycle 2 (strain states): the ledger, the three
  methodological findings, the structural caveat on c1, and the scope
  statement that governs all write-ups.
- `archive/CLAUDE-cycle1-2.md`, `archive/RESULTS-cycle1-2.md` — full
  design history and dated experiment log, frozen at tag `cycle-2-close`.
  Internal relative links inside archived docs may be stale; they are
  records, not working docs.

## How to append results

Unchanged: dated entries in `RESULTS.md` (which restarts at the cycle-3
reset), raw stdout to `results/raw/`, commit with a message naming the
entry. Design-relevant findings are flagged for discussion here, not
silently applied.
