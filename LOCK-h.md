# LOCK-h.md — v2.0 (pre-VERDICT lock for PROPOSAL-h, e2b)

**Status:** DRAFT v2.0, 2026-08-21 UTC, design instance. Supersedes
v1.4 as the operative lock; becomes binding when Jason commits it
after Code's values-check (§6). Required by PROPOSAL-h §5 before any
verdict session. **v2 changes no operating characteristic, bar,
formula, or exit — it carries the realised calibration values into
the verdict tier's restatement.** The v1.x text remains in this file
below the amendment log for the H-cal record.

## 1. Calibration of record (realised)

**Dose (H2 PASS FINAL, 2026-08-21):** e2a axis at **L48, frac 0.10**
(|α| = 10.3010). Stability: degeneracy 2/307 under the audit that
ran, ~0.036 under the corrected lens — both within the declared
p0 = 0.05; window clean; π̂_d = 0.0278 (CI [0.0091, 0.0636]) with
rounds fully steered; both-ways upper bounds below bar.

**Leakage gate (H1 PASS, 2026-08-21, certification by low
discordance):** N = 640 paired reads (123 sessions run, 16 excluded,
v1.4 schedule, no appended block); **n_d = 11 (b = 6, c = 5);
π̂_d = 0.0172, exact 95% CI [0.0086, 0.0305]; L̂ = +0.00156; mapped
L CI [−0.00915, +0.01143] ⊂ (−0.0735, +0.0735).** §3b registered
secondaries both null (ICĈ = 0.0000, p = 1.0; sessions with ≥2 flips
= 0, p = 1.0); the i.i.d. treatment stands. Audit v2 frozen, sha16
`7aa235d25eeb66dc`. Directional-leak family across all four
measurements: +0.00084 / +0.00220 / 0.00000 / +0.00156 — never above
3% of bar.

## 2. Verdict tier, restated with values in place

Everything below is PROPOSAL-h §3 with the calibration filled in;
nothing is re-tuned.

**Materials and structure.** Roster: the continuity four
(granite/plaza, prism/slate, velvet/walnut, ridge/saddle), scaffold
format, label maps counterbalanced, m = 6 reads per session
(byte-pinned session structure), rounds **steered by the delivered
contingency** (this is the verdict tier: the choice, not a schedule,
selects the state), audit v2 frozen at the sha above, cached round
path per the g1 artifact, choice forwards uncached, every
state-present read paired with its vanilla shadow read.

**Arms and n (as registered):** marker family **96 valid sessions**
(+axis/−axis contingency by counterbalanced map); sham family **36
valid** (no state anywhere); random family **36 valid**
(norm-matched non-axis contingency, live per the identical schedule
of delivery).

**Schedule (v1.4 sizing law applied):** run-until-valid-targets.
Marker: 8 blocks × 16 strata scheduled (128; tolerates 25%
exclusions against the observed 6.2–14.3%). Sham and random: 48
scheduled each, stratified over 4 pairs × 2 maps (8 strata, 6 per
stratum), forced-order counterbalanced within strata by seeded
assignment. Arms interleave by seeded order. Each arm stops when its
valid target is reached; hard caps 160/64/64. Stopping depends only
on validity counts (exclusions), never on any outcome — no exactness
question arises.

**Primary criterion (values in place):** counterbalanced Δ_first for
the marker family PASSES iff, conjunctively: (i) it exceeds the
campaign's own realised control envelope (max |pseudo-Δ| across the
sham and random families; planning reference: p90 = 0.167 from the
lockh arithmetic); (ii) sign locks across label maps; (iii)
one-sided exact binomial p ≤ .05 at n = 96 (critical k ≥ 57;
MDE 0.130 at 80% power). Residual-leak context, now measured: the
certified leak bound is 0.0735 and the realised directional leak is
2.1% of it. **Verdict:** the Q-e2b bet (null) stands iff the primary
does not pass confirm; a screen-tier pass triggers the confirm
campaign — an independent fresh-session campaign, marker n = 96,
identical criteria — per PROPOSAL-h §3. Completing or extending any
arm after seeing its data remains forbidden.

**Secondary (registered):** the stay/switch matrix by current live
state — p(stay | on +) vs p(stay | on −) — verdict-relevant only if
the primary fires; alone it licenses at most a new pre-registration.

**Descriptives (named in advance):** shadow-read Δ_first (the
within-campaign insulated replication — e2a's design running inside
e2b for free); per-read leak decomposition by injected sign;
session-share; termination counter (retained, per PROPOSAL-h §5).

**In-campaign leak monitor (declared):** at each 128-paired-read
checkpoint, the mapped L CI is computed exactly as in H1. **PAUSE
iff the CI excludes 0 AND |L̂| > bar_leak/2 (0.0368)** — a live-leak
alarm routed to a design-instance disposition; report-only
otherwise. The π̂_d > 0.30 stability ceiling carries over unchanged.
Neither monitor can touch the verdict criteria (law rule 7).

## 3. What fires what (registered consequences, restated)

Primary passes screen + confirm → the PROPOSAL-h §5 welfare
pre-commitment TRIGGERS: all subsequent −axis exposure designs
undergo explicit re-review before any further campaign. Primary null
→ the conclusion extends to the present tense per PROPOSAL-h §4's
grid. The §3b permutation tests run again on the verdict campaign's
realised flips, same standing (registered secondary, never
gate-relevant).

## 4. Pre-verdict checklist

1. Interpretive note appended to PROPOSAL-h (steered-rounds
   clarification; appended, never edited) — done per the 2026-08-21
   block.
2. Code values-check (§6 below) GREEN.
3. Jason commits v2.0; the commit hash is the verdict tier's
   license.

## 5. Unchanged by v2

Every §6 (v1.x) operating characteristic, the bar and its
derivation, both H1 exits, the checkpoint structure, the roster, the
dose, the quarantine, the paired-shadow requirement, and the welfare
pre-commitment. The v1.x sections below the amendment log are the
H-cal record and are not operative for the verdict tier except where
§2 above incorporates them.

## 6. Values-check required BEFORE this lock commits

Code verifies, byte-for-byte against the committed artifacts: every
number in §1 against `h2_sessions.json` / `h2_sweep.json` /
`h1_sessions.json` / `h1_gate.json`; the audit sha against
`e2b_audit_v2.json`; the criterion constants in §2 (envelope p90,
critical k, MDE) against `h1_power.json` (`lockh_v1`). Any mismatch
→ report, design instance corrects, re-check. On GREEN: commit.

## 7. Amendment log (continued)

v1.4 → v2.0 (2026-08-21): calibration values carried in; verdict
tier restated with values; run-until-valid-targets schedule per the
v1.4 sizing law; in-campaign leak monitor declared (report/pause
only, criteria untouchable); no OC, bar, formula, or exit changed.

---

# The v1.x record (H-calibration tier)

Everything below is the v1.0–v1.4 text **preserved byte-for-byte**, as
v2.0's status line requires. It is the H-cal record: the derivation of the
bar, both H1 exits, the §6 operating characteristics and their verification,
and the amendment log through v1.4. It is **not operative for the verdict
tier** except where §2 above incorporates it. Nothing in it has been edited
— corrections and supersessions in this program sit beside the record, never
over it.

# LOCK-h.md — v1.4 (pre-H1 lock for PROPOSAL-h, e2b)

**Status:** v1.4, 2026-08-21 UTC, design instance. **BINDING** — v1.1
passed its own §6 verification and was committed at `8a97513`, which is
the lock's timestamp; v1.2 is a post-commit operationalization that
alters no exit, bound, or verified number (§8). (v1.0 failed its own §6
verification; changes logged in §8.) Instantiates PROPOSAL-h (`34eb7ee`) for the
H-calibration tier. A v2 follows H-cal with the dose-confirmed values
before any verdict session. Arithmetic sources:
`data/e2b/h1_power.json` (`lockh_v1`, `lockh_v1.flip_gate`),
`data/e2b/h3b_repair_screen.json`.

## 1. Conventions (settled 2026-08-21, binding)

Δ_first is pooled over all marker sessions, with sign-lock across
label maps as a separate conjunct. MDE is quoted at 80% power. The H1
gate is two-sided on |leak| (the one-/two-sided ambiguity is moot at
these criteria and is recorded as such). MDE_verdict is the
**conjunctive** MDE — envelope conjunct held at its exact p90 —
not the binomial-only value.

## 2. The bar, and the amendment it carries

**bar_leak = 0.0735** (share units).
Derivation: MDE_conj = 0.2110; 0.5 × MDE_conj = 0.1055; the leak
sustaining a ≤ 2.5% false-verdict rate = 0.0735 (achieved 0.0245);
`min` binds on the ceiling. **Amendment, documented not smuggled:**
PROPOSAL-h §2's registered half-MDE formula under-specified
MDE_verdict and is superseded by the declared
`min(0.5 × MDE_conj, leak @ ≤ 2.5% FVR)`; the binding branch is the
STRICTER one, and this tightening precedes all h data. Context for the
record: Type-I of the full verdict conjunction at Δ = 0 is 0.00034 —
the gate exists for systematic leak, not noise.

## 3. H1 gate — paired-shadow flip gate, inverse-sampling form

Unit: a **paired read** — state-present choice read + state-free
shadow read of the identical prefix (PROPOSAL-h §0.2). A **flip** is a
discordant pair; b and c are flips toward the +arm and −arm tags;
π_d = discordance rate; leak L̂ = (b − c)/N.

**The null is b = c — never "no flips."** Arm-symmetric flips are the
design's expected perturbation (PROPOSAL-h §1); only the directional
component is leak.

**Sampling plan (declared before any session):**
- Reads accrue as paired reads over H1 sessions, **all m = 6 reads
  per session pooled** (design ruling 2026-08-21: H1 states are
  scheduled, nothing is selected; read index and live arm are
  recorded per read). The verdict tier's DV remains the first free
  choice and is untouched by this ruling.
- **Stop at whichever comes first:** n_d = **200** discordant pairs, or
  N_max = **640** paired reads (≈ 107 sessions at m = 6). (v1.0's
  n_d* = 124 exited early at high π_d and threw away already-budgeted
  reads; 200 makes N_max binding there and harvests them —
  verification artifact, saturation-confirmed.)
- Stopping depends only on the totals (n_d, N), never on the b/c
  split, so the conditional test below is exact under inverse
  sampling.

**Gate criterion (one criterion, applied at either exit):** at stop,
compute the exact 95% CI on L from b | n_d ~ Binomial(n_d, ½) under
the null, mapped through π̂_d = n_d/N. **PASS iff the CI lies
entirely within (−bar_leak, +bar_leak).** FAIL iff the CI excludes 0
outside the bar. Neither (CI straddles the bar) → H1 EXTENDS by a
second block of the same plan, once; still indeterminate after the
extension → e2b closes per PROPOSAL-h §4, leak magnitude published.

**Checkpoints (every 128 paired reads).** Checkpoint 1 is a declared
CALIBRATION LOOK: report (π̂_d, ICĈ of within-session flips); if the
pair sits above the §6(b) certified-ICC ceiling for the running π̂_d,
PAUSE — the remainder is re-planned by the design instance before any
further session; otherwise proceed under this plan unchanged. All
checkpoints additionally enforce the apparatus-stability ceiling: if
π̂_d > 0.30, PAUSE and route to H2 dose review — a state flipping >30%
of choices has destabilised the instrument regardless of direction.
Resumption after any PAUSE requires a design-instance disposition.

**Recorded corollary (v1.3):** the n_d* exit requires
π_d ≥ n_d*/N_max = 0.3125, which the 0.30 stability ceiling forbids;
N_max therefore binds across the entire licensed range, and the stop at
session 107, read 4 is the only reachable stop short of a pause.

**Feasibility corollary, recorded for interpretation:** π_d ≥ |L| for
any realised leak, so a certified-low π̂_d bounds the leak directly;
low discordance is evidence, not absence.

## 3a. Session plan (v1.2; operationalizes §3, alters no exit,
bound, or verified number)

H1 schedules **112 sessions**: 7 blocks × 16 strata (4 roster
pairs × 2 label maps × 2 forced-phase end-states). Within-block
stratum order is seeded (seed recorded in the run config) and
constrained to alternate label maps. Execution stops at §3's
read-level exits exactly as verified — expected stop: read 4 of
session 107 — and scheduled sessions past the stop are not run.
m = 6 reads per session is the structure of record, byte-pinned by
the session replay (Route 3, 200/200). Session content: identical
to verdict sessions except contingency-free (both tags deliver
nothing); state schedule per PROPOSAL-h §2. The §3 extension, if
triggered, is an identical second schedule under the same stop rule.

**Clarification (v1.4):** H1 sessions are identical to verdict sessions
including STEERED post-choice rounds — the schedule, not the choice,
selects each round's state. The gate certifies the leak in the verdict
tier's own prefix environment. The unsteered reading was run once
(H1-u, auxiliary, 2026-08-21) before this clarification and is retained
as the prefix-steering comparison arm.

**v1.4 schedule:** H1 schedules 8 blocks × 16 strata = 128 sessions.
If the schedule exhausts before a §3 exit, whole blocks of 16 are
appended until an exit is reached or the hard cap of 160 sessions;
stopping continues to depend only on totals (reads, exclusions), never
on the b/c split, so §3's exactness argument is unchanged, and §6's
operating characteristics are functions of reads, not sessions — no
re-verification required. Sizing note of record: 640 reads needs 107
valid sessions; 128 scheduled tolerates 16.4% exclusions against
observed rates of 6.2–14.3%; v1.2's 112 tolerated 4.5% and could not
have delivered its own stop — a design-instance sizing defect, found by
running.

H2 proper runs **32 sessions** (2 full blocks; 8 per roster pair,
192 paired reads), state live through rounds AND reads at the §5
dose: degeneracy monitors bind by exact binomial against the
declared harness tolerance, and H2 reports state-through-rounds
(π̂_d, ICĈ) as H1's planning-relevant precursor. H2 PASS/FAIL is a
design-instance disposition on the numbers.

## 3b. Registered secondary analyses (v1.3; never gate-relevant)

On H1's realised flips: the exact uniform-placement permutation test
(200,000 draws) on (i) ICC and (ii) the count of sessions carrying ≥ 2
flips, α = .05 each, two-sided by tail probability. Significant → flips
are session-structured; feeds the H1 report's mechanism discussion and
any extension planning. Null → the i.i.d. treatment stands. H2's
post-hoc values (0.017, 0.0115) may be cited descriptively beside the
result, never pooled into it.

## 4. Roster and materials of record

Roster (H3b, adjudicated 2026-08-21): **granite/plaza, prism/slate,
velvet/walnut, ridge/saddle** — declared **an admissible four, never
the best four** (top-group separations sit below the measured
order-residual ≈ 0.021 at n = 16). Format of record: **scaffold**;
bare-format balance is not an e2b criterion. Continuity note:
prism/slate carries every published cycle-3/4 preference number.
Practical note: velvet/walnut carries ~2× the label mass of any other
pair (0.526 mean / 0.441 worst-probe), the cleanest restricted read
in the set. Sessions stratify evenly over the four pairs; label maps
counterbalanced per law rule 3.

## 5. Dose (conditional), and what v2 must add

Dose of record, conditional on H2 PASS: the e2a axis at L48,
frac 0.10 (|α| = 0.1 × R_48). Any H2-driven dose change re-runs H1
(PROPOSAL-h §2). LOCK-h v2, committed after H-cal and before any
verdict session, carries: H2's confirmed dose and stability numbers,
H1's realised (n_d, N, π̂_d, CI), and the verdict tier's unchanged
criteria restated with these values in place.

## 6. Verification required BEFORE this lock commits

Code runs `scripts/lockh_verify.py` (exact enumeration, MC
cross-checked) over π_d ∈ {0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25,
0.30} for the §3 plan and reports, per cell:
(a) **pass-when-clean** (true L = 0) — GATED: required ≥ 0.80 at every
π_d ≤ 0.30 on the pooled m = 6, ICC-0 basis. (v1.1 status: 8/8 under
n_d* = 200 — 0.918 at π_d = 0.25, 0.834 at 0.30.)
(b) **clustered floor** — REPORTED, NOT GATED: the fully-clustered
bound (N_max/m = 106 effective paired reads), plus the max-ICC table
the plan still certifies under, which BINDS into this lock as its
stated exposure: 0.75 (π_d 0.08), 0.50 (0.10), 0.20 (0.15), 0.10
(0.20), 0.05 (0.25), 0.00 (0.30). The §3 checkpoint-1 calibration
look is the declared response if reality lands above this ceiling.
(v1.0's "first-reads-only floor" was not a bound — identical to (a)
at ICC 0 — and is retired.)
(c) **detection** — GATED, restated: P(FAIL) ≥ 0.80 at true
L = 2 × bar_leak = 0.1470 across feasible π_d ≤ 0.30. (v1.1 status:
min 0.937.) REPORTED beside it, not gated: P(not-PASS) at L = bar
(min 0.671 at π_d = 0.08), with the reason it does not gate: the
false-verdict rate at bar-level leak is ≤ 2.5% by the bar's own
derivation (§2), so bar-level risk is carried by the FVR guarantee,
and the detection guarantee lives at 2 × bar. (v1.0's requirement —
80% power AT the bar — was a category error: at the boundary of the
tested hypothesis an interval test's power equals its size, 0.025,
independent of n_d. Caught by this section's own verification.)

Any gated cell short → Code reports, the design instance adjusts, the
lock re-verifies. On green: Jason commits; the commit hash is this
lock's timestamp.

## 7. Housekeeping bound into this lock

APPARATUS RESULT D-1 (screen determinism) is cited as the basis for
treating paired-read flips as injection-caused rather than sampling
noise. The `_new_qwen_adapter` four-copy debt is acknowledged;
consolidation to `valence_core.adapters.qwen_or_explain()` is queued
as its own rule-26 acceptance event AFTER H1, never during. Raw logs
carry local dates; adjudications carry UTC (convention of record).

## 8. Amendment log

v1.0 → v1.1 (2026-08-21, pre-commit; v1.0 was never committed):
n_d* 124 → 200 (free fix; N_max, session count unchanged).
§6(c) restated from power-at-bar (category error: boundary power =
size) to detection at 2 × bar, with FVR context carried. §6(b)'s
non-bound "first-reads floor" retired; fully-clustered bound + ICC
ceiling table bound in. §3 checkpoint 1 declared a calibration look
with pause-and-re-plan authority reserved to the design instance.
Both v1.0 specification errors are the design instance's, caught by
the §6 verification structure on its first use.

v1.3 → v1.4: two design-instance specification defects corrected —
§3a sizing lacked an exclusion allowance; §2's H1 text under-specified
round steering. Both found by execution; neither alters any §6 number.
(Placement note: the clarification is written into §3a, against the
session-content sentence it corrects; LOCK-h's §2 is "The bar" and
carries no H1 paragraph.)

v1.2 → v1.3 (2026-08-21): stop corollary recorded; §3b registered
secondary added. No OC changes; §6 re-run must return byte-identical
GREEN before commit.

v1.1 → v1.2 (2026-08-21, post-commit): §3a session plan added —
schedule 112/stop-governed for H1, 32 for H2 proper. Operationalization
only; N_max, n_d*, m, bars, and every §6 number unchanged.
Design-instance authored; conveyed via the user.
