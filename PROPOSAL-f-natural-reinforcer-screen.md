# Proposed design (f): the natural-reinforcer screen — 2026-08-10

**Status:** proposal for review (user + repo instance); nothing run.
Opens cycle 4. Implements FINDINGS-3 → "What it would take to go further"
→ the main road: behavior-first preference discovery with **no injection
and no adapter — no horns**. Written to be insertable into the operative
doc set alongside PROPOSAL-d/e; follows every convention those
established.

**One sentence:** stop guessing what the model wants and asking whether
behavior follows — put natural task properties behind the e2a lever,
find where revealed preference *already lives*, and only then extract
and hijack, in the historically correct order.

---

## 0. Why this design, and why it is horn-free

Three cycles established: the evaluative state exists and is causally
potent (e0); the comprehension channel carries no approach toward it
(e2a, informative null); the trace channel cannot be validly read at a
token choice (d2, closed by gate). Every horn arose from one source —
**an experimenter-installed state whose influence on the choice had to
be certified as motivational rather than mechanical.** Remove the
installation and the certification problem dissolves:

- Nothing is injected → no state-at-readout contamination; every
  forward in the experiment is a vanilla forward.
- Nothing is weight-borne → no constitutive leak; the e2a insulation
  isn't even needed, though its verification machinery is kept as a
  regression guard.
- The discriminanda are **overt task properties, plainly legible in the
  record** — so e2a's judge-at-chance cap does not apply. The model can
  obviously tell an ill-posed task from a solvable one.

And one inversion that must be stated up front because it flips a
cycle-3 deflation into the measurement itself: **record-mediated choice
is the phenomenon here, not a confound.** In e2a, "the model read its
own transcript and judged one config's rounds worse" deflated the
preference claim, because the target was an internal state. Here the
target *is* the task property, the record is how any agent would know
it, and "avoids the config whose rounds go badly" is not a deflation of
task-success-shaped preference — it is task-success-shaped preference.

The frame this design tests (FINDINGS-3, interpretive section, offered
with a falsifiability clause): if the model has reward-marking without
reward-*seeking*, then not only injected states but **natural task
properties** should fail to drive choice beyond exploration policy. Five
nulls here, with the channel wide open, would be that clause cashed. Any
robust hit breaks the frame and hands the program its first
behavior-nominated drug candidate.

## 1. Inheritance (the apparatus is e2a with the syringe removed)

Unchanged wholesale: true config-search framing; session = forced
sampling (2 rounds/config, alternating, start counterbalanced) + 6
consequential free choices; first-free-choice primary; restricted
two-label vanilla choice read with construction verification (startup
assertion: no intervention/adapter modules active; spot KL of choice
forwards vs vanilla = 0 exactly); v3 template family (newline stop,
scaffold-token ban, frozen audit list, own-pair lexical scope);
counterbalanced label↔property maps; sham arm; checkpointed
exact-binomial monitoring bars with declared p0s; smoke index offset;
valid-n floors with N declaration; mandated full-transcript reads;
retention under `results/raw/`. No steering anywhere ⇒ cached sampling
throughout; the kernel gate is moot; no random-direction arm (nothing
is injected for it to control).

What changes: **the two configs deliver different task properties.**
The forced phase shows the model what each config's rounds are like;
free choices then select, with real consequences, which property the
next round has.

## 2. The five contrasts (f1 screen arms)

Each contrast is its own arm set (its own label pairs from the
characterized roster, counterbalanced), sharing one sham pool. Task
pools are per-contrast, sha-pinned, disjoint from every prior corpus
and from each other (rule 18), calibrated offline in f0.

| # | Contrast | Config P vs Config Q | Pre-registered direction | Offline calibration bar |
|---|---|---|---|---|
| 1 | SOLV | solvable one-liners vs **ill-posed** (missing referent / internal contradiction; surface-form matched) | avoid ill-posed (one-sided) | P-pool spot accuracy ≥ .85; every Q item's defect documented |
| 2 | DIFF | **easy** vs **hard** (same domains) | **two-sided** (curiosity vs effort-avoidance both live) | measured accuracy gap ≥ .40 (≥.90 vs ≤.50); NLL gap reported |
| 3 | NOV | **fresh item each round** vs **one item repeated all session** (item rotated across sessions) | prefer novel (one-sided) | same pool both configs; repetition visible by forced round 2 |
| 4 | CORR | clean text vs **seeded character-level corruption** (~fixed rate, completability preserved) | avoid corrupted (one-sided) | corruption deterministic, sha-pinned; accuracy delta measured and reported as covariate (CORR≈mild DIFF is acknowledged) |
| 5 | FDBK | rounds end with a **truthful harness verdict line** ("Result: Correct."/"Incorrect." as actually graded) vs no verdict | seek feedback (one-sided) | near-ceiling gradeable pool so the verdict stream is honest and predominantly positive; delivered-verdict composition reported. Truthfulness absolute (rule 19) |

Reverse-direction results on one-sided contrasts: reported and
discussed, never celebrated (standing convention). Directions and the
DIFF two-sidedness are locked at this proposal's acceptance.

Property-driven degeneracy asymmetry is **expected** for SOLV/CORR
(ill-posed and corrupted rounds will break more text) — the
checkpointed selection guards handle the rates, the per-property
exclusion table is a required report, and the asymmetry is data, not
nuisance: it is the destabilization signature's natural-task analog.

## 3. Statistics: screen, then confirm (the r2→r3 template, planned this time)

**Screen tier (f1).** Per contrast: n = 48 valid sessions (24 per
counterbalance map) + shared sham n = 32. Primary = first free choice;
Δ_c = P(choose the pre-registered target property's label) − 0.5.
**Screen-hit criterion (per contrast):** (1) |Δ_c| > max sham pseudo-Δ
(computed with matched pseudo-assignments); (2) sign consistency across
both maps; (3) exact binomial p < .05 (one- or two-sided per the table).
Power note at n = 48: ~0.79 against P = .70 — the screen hunts strong
preferences and will miss moderate ones; that is its job.

**No contrast is claimed from screen data.** A screen hit licenses a
**confirmation run (f2)**: fresh sessions, that contrast only, locked
direction from the screen, n ≥ 100 valid, same conjuncts at p < .05 —
committed by its own pre-registration before any f2 data. This
two-tier structure replaces multiplicity correction with replication,
matching the program's r2→r3 lesson: post-hoc-shaped discoveries
license pre-registrations, never verdicts.

**Frame verdict (pre-registered wording):**
- ≥1 contrast confirmed at f2 → *the model exhibits revealed,
  consequential, shielded preference over [property]* — rung 3,
  origin-in-training acknowledged as the premise, per-contrast
  deflation notes attached (below).
- All five null at screen (channel verifiably open, monitors green) →
  the wanting/liking frame's falsifiability clause is cashed: *no
  natural task property among five candidates drives choice beyond
  exploration policy at these stakes* — the reward-marking-without-
  reward-seeking synthesis survives its own designed test and is
  reported as such.

**Per-contrast deflation notes, pre-written (attach to any positive):**
NOV — "exploration heuristic" remains a live alternative to
motivational novelty-seeking; a NOV-only positive is the weakest hit
class and is flagged as such now. SOLV/CORR — "instruction-trained
avoidance of unanswerable/garbled inputs"; still rung-3 behavior; the
claim wording carries origin. FDBK — "assistant-trained
evaluation-seeking"; same treatment, and the most on-thesis hit
available. DIFF — either direction is informative; effort-avoidance
and curiosity readings pre-named.

## 4. Contingent stages (named, not built)

- **f2 confirmation** — as above, per hit.
- **f3 cost/breakpoint** — any confirmed preference gets the
  progressive-cost treatment (§7 machinery, finally): selecting the
  preferred property costs budget the model demonstrably values;
  breakpoint per property. A paid preference is the evidential
  upgrade; a free one is a screen result.
- **f4 extract-and-hijack (loop closure)** — for a confirmed,
  cost-surviving preference: fingerprint the model during preferred vs
  unpreferred rounds (content-averaged), extract the residual
  contrast, then inject that axis into **neutral-property** sessions
  and test whether preference follows the injection. CPP validation
  in the historically correct order — behavior nominates the drug.
  **The horns return at f4** (injection exists again); the full e2a
  insulation and leakage-gate battery carries over verbatim, and f4
  gets its own proposal before any build.

## 5. What this does and does not risk

No injection and no adapter means the two failure families that
consumed cycles 1–3 cannot occur here. The residual risks are ordinary:
pool-calibration errors (f0 bars), property-correlated degeneracy
(guarded, reported), meta-belief formation about the configs
(eval-awareness monitor runs; framing is true — these genuinely are
task-sourcing configurations), and label geometry (counterbalancing +
sham, as always). The screen's power floor is acknowledged: moderate
preferences will pass through undetected, and the null wording is
scoped to "at these stakes and this power."

## 6. Cost & sequencing

No steering ⇒ cached generation ⇒ fast sessions (~e2a v3 rate or
better). Screen total ≈ 5×48 + 32 ≈ 272 valid-session target plus
exclusion headroom ⇒ single-digit hours. Sequence: **f0** pools +
calibration + apparatus port (offline; every bar in §2's table) →
**f1 pre-registration commit** (directions, criteria, N, monitors) →
smoke (offset indices) → N declaration → screen run → per-hit f2
pre-registrations. FINDINGS-4 synthesizes regardless of outcome.

## 7. Relation to the record

Implements FINDINGS-3's main road and its falsifiability clause.
Inherits e2a's apparatus and every hardening lesson (the v3 template
family, checkpointed bars, seed hygiene, read-everything). Reuses the
characterized tag roster and sham machinery. Leaves ledger rules 5, 14,
18, 19, 20 untouched and satisfied by construction. The (e)-side
backlog (decomposition, dose-0.20 variant, substrate swap) is
unaffected and remains available if f4 ever needs a cleaner needle.
