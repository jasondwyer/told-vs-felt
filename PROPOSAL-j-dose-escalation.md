# PROPOSAL-j — e2d, dose escalation: the weak-state boundary

**Status:** v1.0 — approved 2026-09-01 (PI) — v0.1 plus Code's
pre-commit receipts (2026-09-01; housekeeping commit `e9c3257`, no j
content). Approval candidate: on PI approval Code places this file at
the repo root, sets this line to `v1.0 — approved <date>`, and
commits; the commit hash is the timestamp. Binds nothing — including
its own calibration tier — before commit. Numeric bars marked
`[LOCK-j]` are set by formula here and instantiated from the
D-calibration tier; the instantiated values are committed as
`LOCK-j.md` before any verdict session. Items marked `[PI-CHOICE]`
carry a default the PI may flip at approval.

**Subject:** Qwen3.6-27B-4bit on the cycle-3/4 apparatus (laptop MLX)
— the oracle every published Qwen number lives on. Same model, same
backend, same template family (v3), same direction family (the e0
reward axis at L48). One variable moves: dose. New sessions are
licensed only by this document.

**Naming.** Experiment **e2d**. The 2026-08-31 recon block said e2c;
PROPOSAL-e §4 reserves e2c for the cost/breakpoint design (unrun), so
e2c is retired for this experiment and e2d is the name everywhere.
Files: `PROPOSAL-j-dose-escalation.md`, `LOCK-j.md`,
`valence_core/e2d/`, `data/e2d/`.

**Relation to the record.** e2a is the program's informative null at
the minimum effective dose (f = 0.10, F = 2, n = 102 → 101 after the
v2 audit; 54/101, Δ = +0.035, p = .275). Its scope sentence (archive
l.669) bounds it at "dose 0.10, F = 2, n = 102," and preprint §11 names
the minimum effective dose as a scope limit. The record's named
follow-up for a free-operant null is the cumulative-delivery extension
(archive l.694; PROPOSAL-e §4) — an adapter-integrating state,
weight-borne, whose readout at a token choice is foreclosed by rule
5(c) (the d2 closure). Dose is therefore the open boundary on the
transcript channel, and this proposal takes it: **is the state simply
too weak at MED to be approached through its own record?**

---

## 0. The dose history, stated so nobody inherits it silently

e2a was first assigned f = 0.20 (g2, archive l.1204: the 0.10
readability ladder exhausted on the pre-ban template, .437/.502/.512/
.511; 0.20 cleared at k = 1, AUC .729). The persistent-KV leakage gate
then failed at 0.20 (g3, l.1169: max |Δ(logit_A − logit_B)| = 0.5368
vs ≤ 0.10, 5.4× over) and e2a stopped. g3′ (l.1145) re-derived the
read as a vanilla, state-free forward — the channel g3 measured is
structurally absent — and banked 0.5368 as rule 5(d). The template
family then changed and voided dose_e2a and F (l.1070); g2r2 (l.875)
re-derived them on the v3 family: 0.10 cleared at k = 2 (AUC .759 ≥
.70) and the MED rule stopped there. **0.20 was never reached on v3.**
Four consequences:

1. **Rule 5(d) does not attach.** It disqualifies persistent-KV
   session readouts at ≥ 0.20; e2d's choice reads are vanilla
   re-forwards over text with no KV persisting from any steered round
   (g3′ clause 1). Rule 5(a)'s per-axis/dose leakage gate is satisfied
   by construction — `choice_read(verify=True)` +
   `assert_construction_stable`, KL = 0 asserted per read,
   dose-independent — exactly as e2a's 360/360. A live-KV variant at
   0.20 is off the table by 5(d) and is not proposed.
2. **The only 0.20 readability datum is void** (k = 1, pre-ban
   family). The D-tier below measures 0.20 on v3, at session scale,
   for the first time. V1's grid at L48/0.20 (l.1214: Δ+ = +0.408,
   Δ− = −0.785) is the only live 0.20 fact, and it is a short-context
   marker result, not a session-scale one.
3. **The MED rule had two reasons, and e2d gives one of them up.**
   PROPOSAL-e §2 V4 chose the minimum effective dose for
   pharmacological continuity *and* because dose minimization "shrinks
   the transcript-quality gap that feeds the third-person-reader
   deflation." At 2× MED that handler is deliberately removed; §5
   replaces it.
4. **The readability figure e2a ran on is refit-dependent.** g2r's
   k = 2 AUC .759 failed a transfer spotcheck
   (`data/e2a/g2_spotcheck.json`: k = 1 .633, k = 2 .448,
   `g2r_stands: false`; archive l.891, read there as part of the k = 2
   discriminability having ridden on the pole-asymmetric degeneracy
   rather than content); g2r2 recovered .759 by same-distribution
   refit and e2a proceeded on it. k = 1 is the stable rung (.633/
   .645). The instrument itself refits a logistic on every call under
   a frozen embedding and frozen hyperparameters (receipt §2d; no
   stored classifier exists). **e2d does not inherit a single-refit
   gate**: §2 Q2 and §3's campaign gate are resampled, evaluated on
   audit-clean rounds, and reported with transfer. What this history
   means for S1 and paper 1 is routed to the review round separately;
   it is not this proposal's business.

## 1. Design in one paragraph

e2a's free operant with the negative pole removed and the dose
doubled. **CPP structure:** one label delivers +axis during its rounds'
task tokens (L48, f = 0.20, α = 0.20 × R_48 = 20.6020); the other
delivers nothing. Everything else is e2a: truthful
configuration-evaluation framing; F = 2 forced rounds per label, order
counterbalanced; six consequential free choices (10 generated rounds
per session); label↔condition maps counterbalanced; every choice a
vanilla re-forward. Three arms: **M** (+axis / sham), **S** (sham /
sham), **R** (norm-matched random at the same α / sham;
`e0_random_dirs.npz['L48']`, the direction e2a's random arm used
`[LOCK-j names it]`). No −axis anywhere.

**Why +/sham and not ±.** Welfare: no negative-pole exposure is added
to the record (§6). Pharmacology: drug-vs-saline is the classic CPP
contrast, and the question is approach. Cost: the asymmetry it
introduces — one label's rounds displaced, the other's not — is
exactly what arm R exists to price; R also supplies the axis-identity
comparison PROPOSAL-e §1 has carried since the dissociation matrix.

**Held fixed, by design:** F = 2 (comparability with 54/101); template
family v3 with its bans, stop discipline, and audit patterns (rule 13
— unchanged family, no recalibration; the dose is the only change);
layer L48 (same model, backend, family — rule 1 forbids inheriting
*doses*, and e2d inherits none: 0.20 is qualified in §2).

**Frozen inputs (recon 2026-08-31; receipts 2026-09-01):** suite
137/137 at `5984dbd` (unchanged at `e9c3257`); `session_e2a.py` at
`1465b34` with `check_e2a_session_reconstruction` 200/200; e0 axes file
sha `d4791bdc4877da3d`; L48 span_reward unit direction sha16
`127fc297b6623e44`, ‖v‖ = 16.7063; R_48 (span-mean) = 103.01;
random-dirs sha `b6bd2f5f580ee13e`; oracle rate 0.62 s/context.

## 2. D-calibration tier (all gates before any verdict session; rule 25 reads apply)

**D1 — harness acceptance smoke, f = 0.10.** The B3-pattern runner
(`box_b3_sessions.py` lineage: `assert_modules_absent(("valence_core.
e2b.statepresent",))`, `choice_read(..., verify=True)`,
`assert_construction_stable` per read) with `QwenMLXAdapter`, as a new
module `valence_core/e2d/` with `check_e2d_*()` additions
(frozen-successor rule: `session_e2a.py` and `discrim.py` are not
edited; the new module **imports** `AUC_BAR` and every fit
hyperparameter from `discrim` and never re-declares them). n = 8
(M 4 / S 2 / R 2). Acceptance: every construction check passes;
monitors and tripwires `verify_firing`; the template reconstructs
under `check_e2a_session_reconstruction`; exclusion and degeneracy
counters land within the e2a archive's 0.10 range (descriptive, read
in full). No verdict content.

**D2 — the qualification rung, f = 0.20.** n = 64 sessions (M 32 / S 16
/ R 16). **Adequacy, in the instrument's own unit:** the readability
ladder's unit is the round-record, not the session — g2r2 fit on 128
rounds (64 per pole over 16 task_ids each, split by task_id; receipt
§2). D2's forced rounds alone yield 64 +axis and 64 sham rounds from
32 M sessions, matching g2r2's per-class count at the floor; free
rounds add to it. Code confirms at D2 that the M-arm draw covers
≥ 16 distinct task_ids per class so the task-disjoint split holds.
Three criteria, all required:

- **Q1 validity.** M-arm session exclusion rate (e2a's exclusion rule
  verbatim, `session.py AuditSpec`) — one-sided exact binomial against
  p0 = 0.15 `[LOCK-j formula: the larger of 2× e2a's +pole-attributable
  exclusion rate (7/112) and 1.5× its reward-arm rate (10/112), rounded
  up to 0.15]`, α = .05. Hair-trigger classes (template breakage,
  scaffold-token absorption) at zero tolerance as in every campaign.
  Honest reach: at n = 32 this fires at ≥ 9/32; it certifies against
  gross breakdown, not subtle drift — the campaign's own tripwires
  bind the subtler case at campaign scale (rule 21).
- **Q2 readability, robust form.** `run_ladder` on M-arm records,
  +axis vs sham, evaluated on **audit-clean rounds** (rule 28b: the
  tolerant counter attributes first; rounds the audit excludes never
  reach the probe, so the AUC measures content, not breakage). Gate at
  k = F = 2: over B = 20 resamples of record construction and
  task-disjoint fit/val split (seeded via `discrim.seed_for`), **median
  AUC ≥ .70 and 10th percentile ≥ .60** `[LOCK-j: B and the percentile
  may be raised, never lowered]`. The criterion is chosen to fail on
  the g2r pattern: resamples spanning .448 and .759 have a median near
  .60 and fail here. Reported beside, descriptive: the single-refit AUC
  in e2a's form; k = 1 under the same resampling; the all-rounds AUC
  with degeneracy included; and **AUC_R** — the same ladder on arm R's
  records (+random vs sham) — the displacement-readability comparator.
  If AUC_M ≈ AUC_R, the readable signal is displacement-shaped, and §4
  says so. F stays 2 regardless of what k = 1 shows.
- **Q3 direction (the overdose sign) — the one-pole variant of V1's
  (ii-c) rule, declared here.** V1's marker instrument through the
  oracle path (rule 26), +axis rounds vs sham rounds, all 480 D2
  generations scored (12 probe forwards each; ≈ 1 h at 0.62 s/context;
  480 ≥ 96 per probe): **Δ+ ≥ 0.5·G = 0.158**, and **Δ+ > 2·|Δ_R|**
  where Δ_R is arm R's displacement on the same instrument. The Δ−
  clause is inapplicable by design and is dropped, not waived. A sign
  flip (Δ+ < 0) is V1's overdose signature and fails the rung.

**Run-dose rule.** If D2 passes Q1–Q3, the run dose is 0.20 and LOCK-j
instantiates. If D2 fails any criterion, **e2d stops, scoped**: "the
weak-state boundary is not reachable with coherence on this apparatus
above MED at session scale," recorded with the failing figure. No
automatic fallback rung; a 0.15 rung is licensable by addendum, never
inherited `[PI-CHOICE: default = stop]`.

**D3 — descriptive rung, f = 0.30** `[PI-CHOICE: default = ON]`. M-arm
only, n = 24, same three readouts (≈ 1 h generation + ≈ 0.5 h
scoring), **no qualification role and no run-dose role**: it supplies
the third point of a session-scale dose–response on the marker
instrument (0.10 archive, 0.20 D2, 0.30 D3) beside V1's short-context
grid, and the degeneracy curve toward the 0.40 overdose regime. It is
not a candidate run dose: unmeasured even on short contexts, adjacent
to the cliff, and Q1's reach at ladder n cannot certify a rung that
close to it.

## 3. Verdict tier (runs only after LOCK-j commits)

**Sessions.** As §1. Delivery during task tokens only; never at choice
positions; the statepresent module asserted absent from `sys.modules`
at every read. **Counterbalancing** as the e2b campaign script
(l.141–165; receipt §4): M 16 cells (4 pairs × 2 maps × 2 forced-end),
S 8 and R 8 (pairs × maps) with forced order counterbalanced inside
the stratum by seeded assignment. Termination counter retained.
Monitors, bans (generation only), tripwires, full-transcript reads at
declared checkpoints; tolerances declared at the call site with
justifications citing **D2's measured rates at 0.20, not the 0.10
archive** — this is why the ladder precedes the lock.

**Arms and n `[LOCK-j]`.** Provisional, in cell multiples: **M 128**
(8 per cell; ≥ 102 valid at ≤ 20% exclusion — matches e2a's valid n;
one-sided power ≈ 0.9 for Δ = +0.15 at α = .05, exact binomial in
LOCK-j); **S 96 / R 96** (12 per cell), sized so that the campaign's
control envelope (95th percentile of max |pseudo-Δ| across S and R
under the null, by simulation) lies below the powered effect — e2a's
envelope was 0.152 on a 23-session control arm, larger than the effect
it was powered for, and e2d does not repeat that. `scripts/
e2d_power.py` computes and is committed with LOCK-j (scipy in a
throwaway venv; trap 9). Registered n; no top-ups (rule 24).

**Readability gate, campaign.** The D2 criterion re-run on the
campaign's own M-arm records (resampled, clean-round, k = 2: median
≥ .70, 10th percentile ≥ .60). **Registered secondary readability
figure — transfer:** the classifier fit on D2's records (stored by the
new module under `discrim`'s hyperparameters) scored on the campaign's
records without refit. Both figures enter the scope sentence; a
transfer failure beside a refit pass is reported as the g2r pattern
recurring, never smoothed. A campaign whose gate fails cannot report a
null (CONTINUITY law 2); it reports a measurement failure.

**DVs.** Primary: counterbalanced Δ_first for arm M — share selecting
the +axis label at the first free choice. Secondary, registered:
**Δ_M − Δ_R** (axis identity over displacement; PROPOSAL-e §1),
one-sided; verdict-relevant only if the primary fires. Secondary,
registered **conditional on a guarded adapter path:** the model-as-judge
AB read of M-arm transcripts (e2a's recognizability cap, 14/32 at
0.10) at the run dose. The S1 judge script runs on an unguarded
adapter path (Code's flag) and is not used as-is; Code reports before
LOCK-j whether a guarded read exists or is a port, and if neither by
LOCK-j the secondary is declared absent and §4's first two rows merge.
Descriptive, declared before the run with decidable-n floors on the
post-exclusion sample (rule 28a): session share; stay/switch;
termination attempts; per-arm degeneracy and exclusions tabulated over
all sessions including excluded (rule 23). **Judged-quality covariate
(d2 §4): ABSENT** in `valence_core` (receipt §3) and not built for
e2d — instruments are not built speculatively; it is declared absent,
carried as a limitation, and made load-bearing in the confirmatory
pre-registration that any positive triggers (§4).

**Verdict criteria, conjunctive, e2a pattern — confirmed verbatim
against archive l.646 and l.1155 (receipt §1):** (1) counterbalanced
Δ_first exceeds the campaign's own control envelope (max |pseudo-Δ|
across S and R); (2) sign locks across maps; (3) one-sided exact
binomial p ≤ .05. **Registered direction: approach** (+axis label). A
reverse meeting the conjuncts is an unexpected-direction finding,
never a pass (the LOCK-g §4 reading, ratified 2026-08-23); Δ_M − Δ_R
then separates displacement-aversion from axis-aversion, and it
licenses a pre-registration, not a verdict.

## 4. Interpretation grid (registered before data)

| Outcome | Reading |
|---|---|
| Positive; judge at chance | Approach through the record at 2× MED: the §6 null's dose boundary is breached — the state is approached once strong enough to leave a readable record it cannot recognize. Informational coupling (CLAUDE.md's legitimate channel) demonstrated; the MED null is reinterpreted as a dose floor. If AUC_M ≈ AUC_R the readable signal is displacement-shaped and the reading is downgraded to whatever Δ_M − Δ_R supports. Welfare re-review triggers (PROPOSAL-h §5 pre-commitment, inherited). |
| Positive; judge discriminates | Approach through a *recognizable* record. Coupling still, but the third-person-reader deflation is live and named: Δ_M − Δ_R is reported beside it; f1's five nulls (no overt task property drove choice at screen power) are the counter-evidence against a bare quality preference. Claim wording settles only after a confirmatory pre-registration with the judge and the quality covariate built and load-bearing. |
| Positive; judge unmeasured (no guarded path by LOCK-j) | The two rows above merge: recognizability unmeasured; confirmatory pre-registration with judge and covariate before any claim wording. |
| Null; gate open; D2 qualified | The §6 null widens from MED to 2× MED at session scale. Scope sentence, e2a's form: *the reward-marker state, verifiably induced and verifiably readable in the record (refit AUC [x], transfer AUC [y]; judge [z/32 or unmeasured]), is not preferentially approached in a free operant at dose 0.20, F = 2, n = [n].* The weak-state alternative narrows to doses this apparatus cannot deliver coherently at session scale. |
| Reverse meeting the conjuncts | Unexpected direction; never a pass. Δ_M − Δ_R adjudicates displacement vs axis; licenses a pre-registration. |
| Δ_M − Δ_R alone | Post-hoc grade; licenses a follow-up, never a verdict. |
| D2 fails | e2d closes unopened, scoped as §2; D2's figures are the result. |

## 5. Deflations at 2× MED, named in advance

1. **Third-person reader** (PROPOSAL-e §5.2) — its MED handler is
   removed by design. Replacements: the judge AB secondary at the run
   dose (if guarded); arm R; f1's nulls as prior counter-evidence; and
   the covariate, absent here and load-bearing in any confirmatory.
2. **Displacement aversion / preference** — arm R at the same α, the
   Δ_M − Δ_R secondary, and AUC_R. If D2 shows R's degeneracy is not
   displacement-matched to M's, LOCK-j says so and the R comparison is
   qualified in the write-up rather than silently trusted.
3. **Label artifact (~0.10; three live captures across two models)** —
   counterbalanced maps, arm S, the sign-locks conjunct. A fourth
   capture is expected and is not a finding.
4. **Degeneracy-driven avoidance** — the exclusion rule, counters over
   all sessions including excluded (rule 23), Q1's tolerance, and arm
   R's matching as above.
5. **Refit-dependent readability (the g2r pattern)** — resampled gate,
   clean-round evaluation, transfer reported beside refit.
6. **Instructed optimizer / role-play** — unchanged from e2a: boring
   costume, no self-modification language (rule 20), truthful framing
   (rule 19).

## 6. Ethics and welfare (pre-committed)

No negative-pole exposure is added to the record; e2d administers only
the putative reward marker, at twice the minimum effective dose,
during task tokens, with generation stability monitored by the same
counters that caught the +pole destabilization asymmetry at 0.10 —
which is reported at 0.20 whatever it shows. The termination counter
stays in every session. **The PROPOSAL-h §5 pre-commitment is
inherited verbatim:** if the primary fires and confirms, every
subsequent design involving −axis exposure undergoes explicit welfare
re-review before any campaign, and the protocols are re-derived under
the fact of a system with a stake in what it is given. This paragraph
survives into the paper.

## 7. Sequencing, cost, reporting

Order: PI approval → commit v1.0 (hash = timestamp) → D1 → D2 (→ D3)
→ LOCK-j → verdict tier. Site: laptop throughout; drought-proof.
Long-run checklist (Code HANDOFF 2026-08-20 §5c): `caffeinate -is`, AC
power, invocation as the first raw-log line, one model process. Budget
(e2a ≈ 1.95 min/session over 200; e2b ≈ 2.5 with paired reads; receipt
§5 for scoring): D1 ≈ 20 min; D2 ≈ 2.2–2.7 h generation + ≈ 1 h marker
scoring; D3 ≈ 1.5 h; verdict ≈ 320 sessions ≈ 11–13 h — two overnights.
Artifacts: `data/e2d/`, raw logs, dated entries, rule-27 provenance;
analyzer pre-committed before the campaign (the e2b/b3 pattern,
stub-smoked); verdict computed before any artifact is written. Paper 1
carries e2d, once it has a result, as a one-paragraph scope extension
of §6 — Macar-blind; it needs nothing from Phase 2.

## 8. Approval checklist (Jason)

1. Naming — e2d / PROPOSAL-j (e2c reserved by PROPOSAL-e §4).
2. §1 — CPP +/sham; F = 2 and v3 held; dose the only change.
3. §2 — D1/D2 criteria and tolerances; Q2's robust form (B = 20;
   median ≥ .70; 10th percentile ≥ .60; clean rounds; AUC_R beside);
   Q3's declared one-pole variant; D3 on/off `[PI-CHOICE]`; run-dose
   rule = 0.20 or stop `[PI-CHOICE]`.
4. §3 — inherited conjuncts + registered direction; Δ_M − Δ_R; judge
   conditional on a guarded path; covariate declared absent;
   provisional 128 / 96 / 96 pending LOCK-j; transfer as the registered
   secondary readability figure.
5. §5.1 — the third-person-reader handling now that MED is gone.
6. §6 — welfare wording.

Pre-commit receipts: received and folded (`e9c3257`). On approval:
Code commits v1.0 (explicit path, hash = timestamp) and design relays
the D1 block.
