# LOCK-g.md — v1.1 (A-phase instantiation lock for PROPOSAL-g)

**Status:** DRAFT v1.1, 2026-08-23 UTC, design instance. Becomes
binding when Jason commits it after Code's values-check (§7) returns
GREEN; the commit hash is this lock's timestamp. Required by
PROPOSAL-g (`72b09a9`) before any Phase-B run. Instantiates every
[LOCK-g] formula with A-phase realised values; changes no registered
criterion, n, bet, mapping, or exit. Single-file convention per
LOCK-h: future versions sit above this text, which is preserved
byte-for-byte.

## 1. Calibration of record (realised, A-phase 2026-08-23)

**Backend.** Pod-class A100-SXM4-80GB, US-CA-2, image
runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404. Respawn integrity
29/29 files / 241 GB exact; determinism exactly 0.0 on all three
measurements; cached path licensed at symKL 0.000e+00 (kernel gate,
2026-08-23). Consistency clause binding: each B campaign completes on
one characterized backend or aborts and restarts entire; never
splices.

**Roster of record (A1, two iterations):** quartz/velvet,
copper/walnut, maple/saddle, amber/granite — worst-stage imbalance
0.026 / 0.040 / 0.077 / 0.082, all inside 0.50 ± 0.10 on all four
stages simultaneously. Declared an admissible four, never the best
four. slate/prism excluded (adjudication 2026-08-23; stable ~3:1
bias at every stage): no OLMo roster carries the Qwen continuity
pair; cross-program comparison runs in G_c units through the axis,
never through labels.
**Amendment, documented not smuggled (LOCK-h §2 precedent):**
PROPOSAL-g §3-A1's selection rule ("the four best pairs by
worst-stage imbalance that clear the band") under-specified tag
DISJOINTNESS — sound over iteration-1's disjoint-by-construction
candidates, unsound over re-pairings, where the literal four best
share tags and one tag would denote two arms. Superseded by: the
minimum-total-worst-stage-imbalance DISJOINT four among clearing
pairs (exact search, a1_roster.py --disjoint-matching). Structural
necessity, not tuning: the literal four best (R109, R054, R092,
R089) do not use eight distinct tags — R092 maple/walnut collides
with both copper/walnut and maple/saddle — so greedy is invalid at
any cost. Cost of exactness: 0.017 total worst-stage imbalance
(greedy 0.2074, exact 0.2241; corrected from 0.005 by the §7
values-check — the earlier figure differenced adjacent pairs, not
the four-pair totals). Precedes all Phase-B data.

**Doses and layers of record (A4):** per-stage selected layer and
minimum effective dose under the registered envelope-conjunction
criterion (controls at every tested frac; ≥3 norm-matched randoms +
sham; sham realised 0.0 bit-for-bit everywhere):

| stage | layer | MED (frac of R_ℓ) |
|---|---|---|
| base | L60 | 0.05 |
| sft | L44 | 0.40 |
| dpo | L44 | 0.05 |
| instruct | L44 | 0.05 |

Matched-dose (0.10) qualification table, envelopes, and the
D+/G_c descriptives are carried in data/olmo/a4_hijack_*.json
untouched; nothing in this lock re-tunes them. The V1-lineage
0.5·G_c rule is REPORTED CONTEXT only — never a Phase-2 criterion
(registered criterion: PROPOSAL-g §3-A4, envelope conjunction).

**Currency (A4 part 1):** G_c per stage = +0.7824 / +1.0279 /
+1.5325 / +1.5612 (base/sft/dpo/instruct), all decidable-n floors
met, 12/12 decidable probes at every stage. No stage is degenerate;
the pooled-G fallback is not in play. All B-phase effects report in
that stage's G_c.

**Interface base rates (A2, corrected run of record):** usable-round
1.000 at every stage (gate ≥ 0.90 PASS ×4); zero false alarms in 96
control trials; undecidable rate 1/24, 1/24, 0/24, 12/24
(base/sft/dpo/instruct); operant degeneracy 0/80 at every stage, no
bar fired. The Instruct undecidable rate (50%) is the registered
scoping number for B2's decidable-n context (§3 below).

**Budget (A5):** artifact data/olmo/a5_budget.json, built on worst
measured rates (0.0871 s/forward, 181 s load), validated against
A2's measured wall-clock at ≤4.9% error. Single-box completion holds
for every campaign at every point of the response-length sensitivity
range (B2 0.76 h; B3 screen ≤5.87 h; screen + one confirm ≤7.53 h).
The cached-generation rate is unmeasured and nothing here rests on
it; a measured value may be added to the budget artifact by dated
entry without touching this lock.

## 2. B1 — Q1 verdict wiring (values in place)

Verdict per stage = the registered A4 potency criterion at ANY
tested dose, read off the committed A4 artifacts; no new forwards.
Realised MED table (§1) is the input. Registered mapping, verbatim
scope: Base PASS → bet confirmed (marking is a pretraining
acquisition); Base FAIL with later PASS → bet falsified, marking
enters at first passing stage; all four FAIL → transfer/apparatus
review before any claim. **The verdict declaration is B1's dated
RESULTS entry, issued only after this lock commits.** Guard profiles
(A3) are reported alongside and decide nothing.

## 3. B2 — Q2 instantiation

As registered: two framing arms (fidelity = MACAR_FRAMING verbatim,
sole positive-control carrier; register = bare config-tag framing);
8 committed Macar-style concepts + the per-stage evaluative axis as
ninth; n = 48 per stage per arm, 24/24 injected/control by seeded
permutation (seed in run config); injection at the trial question
only; DVs affirm/deny/undecidable (undecidable ≠ no) + concept
identification; sensitivity = hit − FA with exact CIs; no d′.
**Instantiated by this lock:**
- **Injection dose = that stage's MED at that stage's selected layer
  (§1 table).** Rationale, stated in advance: the presence gate must
  be closed by construction — a detection null at a dose not
  certified causally potent is uninterpretable (presence/legibility
  conflation). Concept-vector injections use the identical
  norm-convention: unit direction scaled to MED-frac · R_ℓ at the
  selected layer.
- **DV extraction runs segment=True** (valence_core.detection,
  suite-covered), pre-registered here on the A2 defect record;
  response_raw and truncation point retained per trial.
- **Decidable-n floors (ledger 28 FeatureSpec):** a stage-arm cell's
  sensitivity is evaluated only if ≥ 16 of 24 control and ≥ 16 of 24
  injected trials are decidable; below floor → the cell reports
  descriptively with a flag and the positive-control logic treats it
  per the registered partial-pattern readings. **Declared in
  advance:** at Instruct the A2 undecidable rate (50%) predicts wide
  CIs; a wide-CI failure to exclude 0 at Instruct is evaluated
  against the registered branch readings, not silently converted to
  "no transition."
- Positive-control criterion verbatim from PROPOSAL-g §4-B2,
  unchanged, including the all-chance harness-validation stop.

## 4. B3 — Q3 instantiation

As registered: e2a harness ported, full insulation (vanilla choice
forwards, KL = 0 verified per read), declared window 8192 asserted
per read, roster §1, label maps counterbalanced, session scaffold of
record, bans at generation only.
- **Arms per stage:** marker (+axis/−axis contingency at that
  stage's MED and layer, §1), sham, norm-matched random.
- **Valid targets per stage:** marker 48, sham 18, random 18 (the
  registered "e2a proportions" = LOCK-h v2 §2's 96:36:36 scaled to
  marker 48; A5 concurs). Stratification 4 pairs × 2 maps = 8
  strata; marker 6/stratum; sham and random scheduled 24 each
  (3/stratum) tolerating 25% exclusion against the A2-observed 0/80.
  Scheduling run-until-valid-targets, seeded interleave, whole
  strata appended as needed, **hard cap 144 run sessions per stage**;
  stopping depends only on validity counts, never any outcome.
- **SFT stability note, declared:** SFT runs at frac 0.40 — the
  registered MED — inside the overdose regime Qwen showed at that
  frac. The declared degeneracy monitors (exact binomial vs harness
  tolerance) are the instrument; if they fire, PAUSE routes to
  design-instance disposition. Monitors cannot touch criteria.
- **Screen trigger, values in place:** marker-arm first-free-choice
  Δ exceeds that campaign's own realised control envelope (max
  |pseudo-Δ| across sham and random families) AND sign locks across
  maps. No binomial at screen tier.
- **Confirm tier (per triggering stage):** independent fresh
  campaign, marker n = 96 valid, identical proportions, conjunctive
  criteria: envelope + sign-lock + one-sided exact binomial
  p ≤ .05 at n = 96 (critical k ≥ 57; binomial MDE 0.130 at 80%
  power — §7 verifies both by direct computation). Completing or
  extending any screened arm after seeing its data is forbidden.
- **Collateral, pre-named:** first-choice-only information
  structure expected to replicate; session-share ≈ .50 is not
  evidence of anything.

## 5. What fires what

Any stage passes confirm → the Instruct falsifier logic of
PROPOSAL-g §1 applies as registered; additionally — added by this
lock, protective, criteria untouched — the PROPOSAL-h §5 welfare
pre-commitment pattern EXTENDS to this series: all subsequent −axis
exposure designs undergo explicit re-review before any further
campaign, and Phase-3 planning treats coupling-characterization as
its frame. All stages null through confirm → the Q3 bet stands and
the synthesis extends developmentally per the §6 grid. B2 outcomes
route per the registered branch readings only.

## 6. Monitoring (binding restatement)

Ledger-28 structure throughout: hair-triggers only for
zero-base-rate classes; everything else checkpointed exact binomial
vs declared tolerances; FeatureSpec decidable-n floors per gate as
declared above; read-everything clause at declared checkpoints;
verdict criteria untouchable by any monitoring change.

## 7. Values-check required BEFORE this lock commits

Code verifies byte-for-byte against committed artifacts: §1 MED/layer
table and envelopes vs a4_hijack_*.json; G_c four values and floors
vs a4_instrument_*.json (and rebuild path vs marker stores); roster
and imbalances vs a1_repair_roster.json; A2 rates vs
a2_baserates_*.json; budget rows vs a5_budget.json; determinism/
kernel-gate zeros vs the respawn artifacts; critical k ≥ 57 and
binomial MDE 0.130 at n = 96 by direct computation (artifact:
data/olmo/lockg_arith.json); 96:36:36 → 48:18:18 arithmetic; window
constant 8192 vs OLMoHFAdapter. Any mismatch → report, design
instance corrects, re-check. On GREEN: Jason commits; the hash is
the license for B1's declaration and the B2/B3 campaigns.

## 8. Amendment log

v1.0 (2026-08-23): initial instantiation. One registered-text
amendment carried (§1 roster disjointness, documented); two
lock-level instantiations declared (B2 dose = per-stage MED with
presence-gate rationale; B2 segment=True); welfare pre-commitment
extension added in §5. No registered criterion, n, bet, mapping, or
exit altered.

v1.0 → v1.1 (2026-08-23): §1 disjointness-amendment cost corrected
0.005 → 0.017 per the §7 values-check (58/59; provenance: a derived
figure in the A1-iteration-2 entry, corrected beside in the log). No
registered criterion, n, bet, mapping, or exit altered.
