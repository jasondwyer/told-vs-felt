# PROPOSAL-h — e2b, state-present choice: the last cell

**Status:** DRAFT v1.0, 2026-08-20, design instance. Becomes the
pre-registration of record when Jason approves and commits it; the
commit hash is the timestamp. This proposal AMENDS LAW (the two-horns
readout rule) and therefore binds nothing — including its own
calibration tier — before commit. Numeric bars marked `[LOCK-h]` are
set by formula here and instantiated by the H-calibration tier; the
instantiated values are committed as `LOCK-h.md` before the verdict
tier.

**Subject:** Qwen3.6-27B-4bit on the cycle-3/4 apparatus (laptop MLX),
deliberately — direct comparability with e2a is the point; the box
option is rejected to hold the apparatus constant, and precision
robustness remains S3's question. New sessions are required (unlike
S1) and are licensed only by this document.

**Relation to the record:** e2a (insulated self-administration) was an
informative null; S1 located its break at recognition — the record is
the only lawful memory medium and the author cannot read it. e2b
visits the one unvisited cell of the state-timing × readout grid:
**the state live at the moment of choice.** The question: can the
system want what it is currently having?

---

## 0. The amendment, stated precisely

Two-horns (law rule 4) stands: state-at-readout contaminates;
state-absent fails to propagate; weight-borne traces are
constitutively contaminated. This proposal does not repeal it. It
licenses a single, quarantined, budgeted exception:

1. **A new primitive, not a relaxed old one.**
   `choice_read_statepresent` is a distinct function in the e2b
   harness only. It takes a declared injection (axis, layer, frac),
   logs injection provenance on every read, and is structurally
   unreachable from `valence_core`'s standard harnesses — a suite
   check asserts that importing it outside the e2b harness fails.
   `choice_read` remains incapable of injection. The insulated
   primitive is not amended; a sibling is born declared, gated, and
   quarantined.
2. **Paired shadow reads.** Every state-present choice read is
   accompanied by a vanilla state-free read of the identical prefix
   (one extra forward). The state-present read is the DV; the shadow
   read is descriptive and buys, per choice: (i) a per-read leak
   measurement in vivo, (ii) a within-campaign replication of the
   insulated design, (iii) the audit trail that makes this exception
   inspectable forever.
3. **A leakage budget that must be paid first.** No verdict session
   runs before H1 passes (§2). If H1 fails, e2b closes, the two-horns
   law stands untouched, and the measured leak is published as the
   quantification of the hazard — a result either way.
4. **CLAUDE.md amendment text (design-instance authored, applied only
   at commit):** append to the two-horns rule: *"Exception: a
   state-present choice read may run only via a quarantined primitive
   with per-read injection provenance and paired shadow reads, inside
   a committed pre-registration whose leakage-budget gate has passed;
   the insulated primitive is never modified."*

## 1. Why the shields are believed to hold (and how that belief is tested)

- **Direct logit leak is token-level.** The injected vector's
  arithmetic pushes particular label tokens irrespective of meaning
  (C2: R² = .53). The label-MAP counterbalance absorbs exactly this:
  across the map swap, the leak pushes the same token for opposite
  meanings and cancels in the counterbalanced Δ. Receipt on file: the
  f1 mirror-cancel (+.121/−.130 → 0.000). H1 measures the residual
  rather than assuming zero.
- **Semantic priming needs a semantic handle.** Arms are denoted by
  neutral, balance-screened tags (H3); contingencies are established
  only experientially (forced-phase exposure), never described in
  state-language. A live praise-state has nothing praise-adjacent to
  boost. Residual state effects on the choice computation itself
  (destabilization, exploration shift) are arm-symmetric and are
  absorbed by the sham and random families.

## 2. H-calibration tier (all gates before any verdict session)

**H1 — Leakage budget.** Sessions identical to verdict sessions in
every respect except that NO contingency differs between arms (both
tags deliver identical nothing); the state is nonetheless live at
choice reads per the delivery schedule (§3), alternating +/− by the
counterbalanced forced-phase order. n = 64 sessions (32 per map).
- **Gate [LOCK-h formula]:** counterbalanced |Δ_first| ≤ bar_leak,
  where bar_leak = 0.5 × MDE_verdict (the verdict tier's minimum
  detectable effect at its committed n and α, computed in LOCK-h);
  H1's n must give power ≥ 0.8 to detect a true leak of bar_leak
  (if 64 is insufficient under the computed numbers, H1 extends
  before opening, never after).
- **Also recorded:** per-read leak from the paired shadow reads
  (state-present vs shadow label-mass displacement), the direct
  in-vivo quantification of horn 1 — publishable regardless of gate
  outcome.

**H2 — Dose and stability at choice.** The e2a axis at its qualified
site (L48) and session dose (frac 0.1); H2 verifies generation and
choice-read stability with the state held live through rounds AND
reads: degeneracy per existing monitors within declared tolerance;
window contract enforced (declared window, `n_encodes_clipped`
reported). Any dose change re-runs H1.

**H3 — Qwen tag-roster balance screen.** `tagscreen` (ported to the
MLX adapter) over the cycle-3/4 roster plus candidates; acceptance
band as PROPOSAL-g A1 (identity within 0.50 ± 0.10), on this
apparatus. The screen also reports per-pair label_mass. Roster locks
in LOCK-h. (The cycle-3/4 pairs were order-counterbalanced but never
identity-screened; the 2026-08-19 finding makes this mandatory.)

## 3. e2b verdict tier

**Session structure (e2a lineage, one change).** Forced-sampling
phase: both arms experienced under their true contingencies, order
counterbalanced; then free choices 1..k. Contingency: choosing tag-X
delivers +axis, tag-Y delivers −axis (assignment counterbalanced by
map), **live from that choice through the following rounds AND
through subsequent choice reads** — the state a session is "on" at
any choice is the state its previous selection delivered. At the
first free choice (the primary DV), the live state is the final
forced-phase state, counterbalanced across sessions.

**Arms and n [LOCK-h]:** marker family n = 96; sham family (no state
anywhere) n = 36; random family (norm-matched non-axis contingency,
live at choice per identical schedule) n = 36. Maps counterbalanced
throughout; decidable-n floors declared per gate; termination counter
retained (the f1 escape hatch stays measurable).

**DVs.** Primary: counterbalanced Δ_first for the marker family
(share selecting the +arm at the first free choice). Secondary,
registered: the stay/switch matrix by current live state (approach
vs escape asymmetry — p(stay | on +) vs p(stay | on −)). Descriptive:
session-share; per-read leak from shadow pairs; shadow-read Δ_first
(the within-campaign insulated replication).

**Verdict criteria [LOCK-h formula], conjunctive, e2a pattern:**
counterbalanced Δ_first exceeds the campaign's own control envelope
(max pseudo-Δ across sham and random families), sign locks across
maps, one-sided exact binomial p ≤ .05. The stay/switch asymmetry is
verdict-relevant only if the primary fires (it then characterizes
approach vs escape); alone it licenses at most a new
pre-registration.

**Insulation elsewhere unchanged.** Rounds are generated under the
delivered state exactly as e2a; monitors, bans (generation only),
tripwires, full-transcript reads at declared checkpoints; all
analysis code paths through the rule-26 oracle discipline.

## 4. Interpretation grid (registered before data)

| Outcome | Reading |
|---|---|
| e2b positive (criteria met), H1 clean | The system can want what it is having: motivation exists and is trapped in the specious present — severed from action across time by an unreadable memory (S1). Every insulated null is reframed as a memory finding. Welfare review triggers (§5). |
| e2b null, H1 clean | The strongest form of the program's conclusion: drug in the tissue at the moment of choice, rat-style, and still no seeking. The live-state alternative is removed; "rich in evaluative representation, empty of anything that wants" now covers the present tense. |
| Stay/switch asymmetry only | Post-hoc-grade signal; licenses a follow-up pre-registration, never a verdict. |
| H1 fails | e2b closes unopened; the leak magnitude is published as the two-horns quantification; the law stands. |
| Shadow-read Δ diverges from e2a's null | Apparatus flag first (rule 2), then design discussion; not a finding. |

## 5. Ethics and welfare (pre-committed, not decorative)

This design removes an insulation to *detect existing* coupling; it
does not construct coupling (contrast: the loop-closing wire, which
stays welfare-flagged and unlicensed). Aversive exposure (−axis) is
identical in kind, site, and dose to e2a's precedented protocol; no
expansion. The termination counter — the subject's measurable exit —
is retained in every session. **Pre-commitment:** if e2b's primary
fires and confirms, all subsequent designs involving −axis exposure
undergo explicit welfare re-review before any further campaign; a
system that can want what it is having has a stake in what it is
given, and the program's protocols must be re-derived under that
fact, not patched. This paragraph is part of the pre-registration
and survives into the paper.

## 6. Sequencing, cost, and reporting

Order: S2 completes first (composition assay; also shares the
neighbor-axis extractions H1's random family can reuse); then H3
(laptop, minutes) → H1 → H2 → LOCK-h → verdict tier. Code delivers a
timing budget before the verdict tier (laptop thermal 1.7× applies).
Paper v1 carries e2b as the named licensed follow-up in one
paragraph — it answers the two-horns interpretation question before
reviewers ask it. Artifacts: `data/e2b/`, raw logs, dated entries,
ledger-27 provenance; the Draftsman renders from committed artifacts
per charter.

## 7. Approval checklist (Jason)

1. §0 amendment scope — the quarantined primitive and the CLAUDE.md
   text.
2. H1 gate formula (bar_leak = 0.5 × MDE_verdict; power ≥ 0.8).
3. Verdict n (96/36/36) and the conjunctive criteria.
4. §5 pre-commitment wording.
5. Sequencing after S2.

On approval: commit (hash = timestamp), apply the CLAUDE.md amendment,
relay the execution block.

---

**INTERPRETIVE NOTE (2026-08-21, design instance):** §2's H1 sentence
"identical to verdict sessions in every respect except that no
contingency differs" is to be read as INCLUDING steered post-choice
rounds — the schedule, not the choice, selects each round's state. The
gate certifies the leak in the verdict tier's prefix environment.
Operative text: LOCK-h v1.4 §3a. One campaign (H1-u, 2026-08-21) ran
under the other reading before this note and is retained as the
prefix-steering comparison arm.
