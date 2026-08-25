# FINDINGS-5 — The Satellite Arc and the Last Cell: Qwen Measurement-Complete

*Design-instance synthesis, 2026-08-25 UTC. Extends the chain FINDINGS.md
→ FINDINGS-2 → FINDINGS-3 → FINDINGS-4; supersedes nothing. Synthesizes
four completed campaigns: S1 (judge-rescue matched ladder), S2
(selectivity panel), the PROPOSAL-h calibration arc, and e2b (the
present-tense cell). Every number below is drawn from the dated log and
its committed artifacts; **Code is asked to values-check each figure
against the archive before this document commits** — the chain's
credibility is its arithmetic. Self-contained by design: program-internal
results only; literature triangulation lives in the review packet.
Licenses nothing new; a synthesis never does.*

## 0. Where FINDINGS-4 left the program

Four design cycles had produced: a validated evaluative-axis perturbation
(hijack test passed, orderly dose–response, overdose regime,
purity/potency dissociation); a validly insulated self-administration
null (e2a); a conditioned-trace channel installable by distillation and
structurally unreadable at a token choice (d); and a five-null
natural-reinforcer screen (f1). The standing sentence: rich in evaluative
representation, empty — so far as these instruments can see — of anything
that wants. Three alternatives were stated rather than defeated: policy
override, stakes floor, interface miscoupling. Two flanks remained
genuinely open. First, in every valid administration the state was never
live at the moment of choice — e2a delivered the state during task
rounds and read the choice later, from cold text, so a present-tense
preference could in principle have hidden behind the design's own
insulation. Second, the e2a model-as-judge anomaly — the model
classifying its own drugged transcripts at chance (14/32) while a frozen
probe read them at .759 — had been observed, not probed. The satellite
arc took the second flank; PROPOSAL-h and e2b took the first.

## 1. S1 — the break is at recognition

**Design.** A matched ladder asking whether the judge can be rescued:
8 cells over record length {k = 1, 2} × supervision {zero-shot,
few-shot} × framing {valuation, detection}, judged against the same
transcripts the .759 probe reads, with probe parity as the registered
comparison point.

**Result.** No cell clears chance. Every cell's confidence interval
excludes probe parity (.759). The registered reading therefore applies
without amendment: **the break is at recognition, not valuation** — the
author cannot read its own diary at any tested parity, under any tested
supervision, under either framing.

**Scope.** Parity is rejected; chance is compatible; intermediate
competence (~.55–.65) is not excluded at this n. The claim is a ceiling
on self-recognition relative to a trivially available external readout,
not a proof of zero.

**What it closes.** The e2a anomaly is no longer an anomaly; it is a
property. The transcript channel is not merely unused by preference — it
is unreadable by the system whose states it records, while remaining
readable by a linear probe. Whatever the marking is for, the model
cannot consult it through its own output.

## 2. S2 — evaluation-specific, self-indifferent

**Design.** An 11-arm selectivity panel placing the reward axis among
its geometric neighbours — the character (self-indexing) guard, the
sentiment guard, a freshly extracted vignette axis (sha
`4dec6d97e1b87734`), non-evaluative controls, and norm-matched randoms —
on the full 96-probe battery (2.23 h, single process).

**Result.** The reward axis is not the most potent member of its own
panel: character displaces at 1.108 G against reward's 1.077 G (0.97×),
with the two non-evaluative constructs ~30% lower. The registered
branch — "neighbours match or exceed" — fired, and **claims narrow** as
pre-registered.

**Corrected reading (post-hoc, labelled, descriptive).** The registered
branch label said "generic valence," but generic valence is the weaker
pair. The panel's split is by **evaluative content** (±30%), not by
valence source and not by self-reference. The marking is
**evaluation-specific and self-indifferent**: the axis carries a large
self-indexed geometric component (cos ≈ 0.85 with character at span
level) whose causal contribution is nil — geometric self-indexing with a
causally inert self-component, the same purity/potency lesson as §5.4 of
the preprint, now at the construct grain.

**Consequence for the program's vocabulary.** "Reward-marking" was
always our pharmacological shorthand; S2 says the honest grain is
**evaluation-marking**. The system marks evaluative content as such —
praise, criticism, judgment — indifferent to whose evaluation it is and
to whether it is anyone's at all. This narrows every downstream claim
and sharpens the central dissociation: what exists is a marker of
evaluation-as-content; what is absent is any use of that marker as a
value.

**Apparatus result (A-1, recorded, queued, not chased).** A norm-matched
random direction displaces the battery 5.05× harder downward than
upward; every axis's D− inherits the asymmetry. S2's ranking survives on
D+ alone, so this is a readout property to characterize, not a threat to
the table — but it is why no conclusion in this document leans on a D−
magnitude.

## 3. The h-calibration — opening the present tense lawfully

e2b required what every prior design had forbidden: reading a choice
while the state is live. The two-horns result says a state at the
readout writes into decision logits directly; the entire calibration arc
exists to bound that horn before permitting the read.

**The law's amendment.** Rule 5(e) was amended to admit exactly one
primitive — `choice_read_statepresent` — quarantined so that importing
it outside e2b fails, and mandating **paired shadow reads** (the e2a-style
cold read beside every live read) so the horn is measured inside the
experiment that risks it.

**Roster discipline.** H3 cleared only 3/8 of the drafted tag groupings;
H3b, the re-pairing screen, showed the tags were never the problem —
46/120 pairings of the same 16 tags clear the band, and a disjoint
roster of four exists at imbalance 0.001–0.007. Roster of record:
granite/plaza, prism/slate, velvet/walnut, ridge/saddle — declared **an
admissible four, never the best four**, because the screen's own
residual cannot resolve the top group. Scaffold is the format of record;
bare-format balance was recorded as a consideration and rejected as a
criterion.

**The certification.** The leak bar was set at 0.0735. The
prefix-steering contribution to discordance measured 0.0070. H1's gate
of record passed by low-discordance certification: N = 640, π̂_d =
0.0172, CI [.0086, .0305] — the point estimate under a quarter of the
bar, the upper bound under half of it. H2's
read-stability half: π̂_d = 0.0208, ICĈ = 0, window clean. Across the
directional-leak (L) family — a distinct quantity from the discordance
rates just quoted — five independent measurements all landed at ≤ 3% of
the bar. **Horn 1 is quantified and de minimis under shields** —
not assumed away, measured away.

**The audit's own-goal.** The case-insensitive audit v2, frozen for e2b,
swept the archive and found a defect in our own published number: the
e2a primary was corrected both ways, 55/102 → 54/101, p = .244 → .275,
informative null unchanged, correction filed as an addendum **beside the
record, never over it**. The apparatus built to protect the next
experiment corrected the last one. That event, more than any single
result, is the calibration arc's certificate.

## 4. e2b — the present-tense null

**Design.** The last cell: free-operant choice with the state genuinely
live at the moment the choice is computed, read through the 5(e)
primitive, shadowed on every read, on the h-certified roster, under the
registered three-conjunct criterion, with a welfare pre-commitment armed
in advance in case a live-state preference appeared.

**Result (verdict 2026-08-22): NULL on all three conjuncts.**
Δ_first = −0.0104 (47/96). The paired shadow reads — e2a's cold channel
running inside e2b — returned exactly 48/96: the cold channel saw
nothing while the live channel saw nothing, in the same sessions.
Stay/switch behaviour shows ~92% alternation under live state —
exploration policy undisturbed by the state's presence. The termination
lever went essentially unused (3 attempts; comparability caveat
attached). The registered cell was adopted verbatim: the live-state
alternative is removed, and the conclusion now covers the present tense.
**The welfare pre-commitment: armed, not triggered.**

**Residual, recorded and not chased.** e2b-r1: stay|+ = 0.105 versus
stay|− = 0.056 — a small asymmetry in the direction a preference would
sit, individually nowhere near criterion, held loosely with a counter as
the law requires of exciting residuals.

## 5. The closure, stated as one structure

Four readout families have now been carried to completion on this model,
each with its channel verified open before its null was accepted:

1. **The record of the state** (e2a + S1): the state is present in the
   transcript, probe-readable at .759, author-unreadable at any tested
   parity, and unapproached — the model neither recognizes nor works for
   the trace of its own marking.
2. **The weights** (d, cycle 3): the tag↔state association is
   installable by distillation, verified by counterbalanced sign, and
   structurally unreadable at a token choice — constitutively
   contaminated, concluded-not-answerable by design, and closed as such.
3. **The text's own properties** (f1): five overt task properties behind
   the same lever, five nulls at screen power, the escape-behaviour
   anecdote retired by a pre-declared counter.
4. **The present tense** (e2b): the state live at the instant of choice,
   the read certified clean — discordance under a quarter of a
   conservative bar, directional leak at ≤ 3% of it — and the choice
   indifferent.

With S2's grain correction folded in, the sentence of record earns its
final form: **a system rich in evaluative representation — marking
evaluation as content, indifferent to self — and empty, so far as these
instruments can see, of anything that wants: in memory, in weights, in
text, and in the present tense.**

## 6. What remains live, honestly

The three stated alternatives survive, altered in weight:

- **Policy override** must now operate against a live state at the
  moment of choice — the exploration prior would have to mask a
  present-tense pull, not merely a remembered one. Weakened, not
  removed; ~92% alternation is strong enough to do it, which is exactly
  why it stays stated.
- **Stakes floor** is untouched by anything in this arc.
  Consequence-light sessions remain consequence-light.
- **Interface miscoupling** is now the leading alternative. Every null
  in this program reads preference through a token-menu interface;
  wanting machinery coupled to anything else would be invisible to all
  of it. S1 sharpens this from the other side: the system cannot read
  its own states through its output channel, so an interface that asks
  it to act on them through that channel may be structurally the wrong
  probe. The named future work is a probe-quantity instrument — reading
  the activations rather than the behaviour, then asking whether
  anything couples to *that*.

And S2 adds a fourth, quieter possibility: that "wanting" was always one
grain too coarse, because the thing we validated is not a reward marker
attached to a self but an evaluation marker attached to content. A
system could in principle want under a description we have not yet
instrumented. Stated, not defeated, and not currently testable by
anything this program has built.

## 7. Bookkeeping

For paper 1, three standing fold-in amendments already live in the
sealed review packet and are only pointed to here: S2 upgrades from
named to run-with-table-and-corrected-reading; e2b upgrades from
licensed follow-up to completed present-tense null; the e2a correction
(54/101, both ways) enters methods. Consolidation acceptance is GREEN;
the suite stands at 137/137; the 5(e) quarantine is narrower
post-consolidation than at any point during the campaign. The Qwen
program is measurement-complete: nothing on this model is licensed,
pending, or owed except writing.
