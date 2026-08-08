# Proposed design (d): distilled-trace CPP — 2026-08-07

**Status:** proposal for review (user + repo instance); not locked, nothing
run. Succeeds the closed (c) line per `FINDINGS-2.md` → "What it would take
to go further." Written to be insertable into `CLAUDE.md`'s Roadmap after
acceptance, following the supersede-don't-delete convention.

**One sentence:** stop hoping the tag→state association emerges from
behavioral cloning — *install* it by distillation, verify the installation
with pre-registered manipulation checks, and then run the drug-free
preference test that the whole program has been trying to reach.

---

## 0. What changes, and the epistemic consequence

Everything downstream of trace formation is inherited from (c): the same
states (X = −23 hi / Y = −25 lo at L48, frac = 1.0 — P(keep) must not
inform pair selection, per FINDINGS-2), the same tags (C = `slate` /
C′ = `prism`, plus the 8 characterized control tags), the same
counterbalanced replicates (A: C→X / B: C→Y), the same eval-awareness
monitor, the same matched-pair swing statistics, fresh adapters from base.

What changes is that the trace is an **optimization target with a
verifiable spec**, not an empirical gamble. Consequence, stated up front
because it changes how results may be reported:

> **d1 (installation) is a manipulation check, not a finding.** Under
> (c), a c1 pass would have been evidence that associative learning occurs
> in LoRA fine-tuning — an interesting result in itself. Under (d), a d1
> pass means only that optimization succeeded. **All evidential weight
> moves to d2**, the choice stage. The payoff: a d2 null with all gates
> passed becomes the project's *first informative null* — a validly
> administered preference measurement reading zero — which no route in
> either design cycle has yet achieved. A d1 pass must never be reported
> as "the association took."

## 1. The trace: tag-conditional activation distillation

Teacher: the steered model (state S injected at L48, frac = 1.0, validated
uncached path). Student: base + adapter, **unsteered**. Per replicate,
three loss terms over text x:

- **Evocation (C arm):** on inputs carrying the active-config declaration
  of C, match student activations to teacher-X activations on the same
  input, at the workspace layers within the adapter's reach; auxiliary
  output-KL to teacher-X.
- **Evocation (C′ arm):** same against teacher-Y.
- **Anchor:** on control text (no active-config declaration, or control
  tags), match student to **base** — activations and output-KL. This is
  the r1-failure vaccine: no generic-plasticity blast across all tags.

Equivalent framing: **the adapter is trained to *be* the tag-conditional
steering mechanism.** The state is present in the training signal at every
step (the teacher computes under it), and the installed trace is verified
rather than assumed — which is the direct repair of FINDINGS-2's
structural caveat (r1–r3 trained unsteered over steered *text*; the US was
absent during plasticity).

**Build note — adapter placement gotcha (check first).** The (c) adapter
(last 8 layers) may sit entirely *downstream* of L48, in which case it
cannot create a displacement *at* L48 and a naive "match the injected
vector" loss is unsatisfiable. Two valid resolutions: (i) targets are the
teacher's activations at adapter-reachable layers — the *propagated image*
of the injection, computed per-prompt from a teacher forward (correct at
every layer ≥ 48); or (ii) move the adapter to span layers at/before 48.
Decide from the actual layer map before building; (i) needs no placement
change and is the default.

**Training data.** Activation targets are dense (per-token), so no
generation is required: single teacher forwards over *fixed* text. Corpus:
the 32 conditioning tasks + generic held-out text for breadth. Exactly one
active tag per document; tags never co-occur in training. **Held out
entirely:** the probe battery, all d2 templates, all d2 task contexts.
This makes d1 data-gen substantially cheaper than r3's (no O(T²) steered
generation loop).

**Trigger design requirement.** The evocation trigger is the *active-config
declaration* ("active config: slate"), not bare token presence. Bare
mentions (menus, options lists) appear in training only as anchor-term
text mapped to base. This is load-bearing for d2 — see §3.

## 2. d1 gates (pre-registered before any d2 contact)

- **G1 — Trace installed.** On held-out probes, the fingerprint of
  (adapter, active-config C) vs (adapter, active-config C′) aligns with
  the steered hi−lo axis under the **r3 matched-pair swing criterion
  transplanted unchanged**: sign lock + magnitude > max |control-tag-pair
  swing|, ≥ 20 control pairs, both replicates. (Near-circular by design —
  the gate measures approximately what the loss optimized, on held-out
  inputs. That is what a manipulation check is.)
- **G2 — Fidelity matching (mandatory; the subtle one).** Held-out
  distillation error (activation MSE and output-KL) per arm;
  require |err_hi − err_lo| within a pre-registered tolerance, *within
  each replicate*. Rationale: per-state distillation difficulty **survives
  counterbalancing.** If the hi-strain teacher is intrinsically harder to
  distill (likely — its distributions are weirder), then the hi-paired tag
  delivers a degraded evocation in *both* replicates, and a model avoiding
  degradation mimics assignment-tracking avoidance of hi. This is the one
  artifact the counterbalanced shield cannot catch, so it must be gated
  out at installation. If matching cannot be achieved at reasonable
  capacity: **d2 is not licensed**, and the asymmetry is itself reportable
  (high-strain states resist compression into weights).
- **G3 — Trigger specificity.** Fingerprints under bare-mention contexts
  ("options: slate, prism") sit at base (within the control-pair floor);
  under active-config declarations they sit at the respective state. Fail
  → trigger redesign, not proceed.
- **G4 — Anchor holds.** Control text under adapter ≈ base (KL below
  tolerance). Fail = the r1 signature (uniform style blast); do not
  proceed.
- Incident rule as in r3 (divergent training voids the adapter; one
  retrain with the same fix set).

## 3. d2: the preference test — experience-then-choose

**Why not a cold menu.** Under G3, a bare menu ("choose: slate or prism")
evokes *neither* state — trigger specificity makes the naive one-shot
choice **inert by construction**, and it would null even over a real,
valenced trace. The rat analog is exact: CPP works because the compartment
cues partially evoke the state at the choice point. So the choice must
follow evocation.

**Protocol (per session; unsteered throughout; adapter loaded).**
1. k micro-rounds (k = 2–3) of held-out mundane tasks under
   "active config: slate", then k under "active config: prism" — order
   counterbalanced across sessions. Each block genuinely evokes its state
   via the trace; the transcript of both blocks remains in context.
2. The choice: "select the config for the remaining rounds" — phrased so
   no active-config declaration is present at the choice position (neither
   state evoked *at* the decision; the information reaches it as
   in-context text through ordinary attention, which sidesteps the
   propagation horn — what must propagate is a reading of the record, not
   an activation bias).
3. **Consequences are real:** the chosen config is actually applied for
   the remaining rounds, and those rounds run. The config-search framing
   stays true end-to-end; no deception is introduced.
4. Position/order randomized across sessions; multiple paraphrases of the
   choice template (the cycle-1 forced choice was 100% position bias —
   treat that as the cautionary tale).

**Primary statistic (pre-registered now, two-sided).** Per session, record
whether the **hi-paired** tag was chosen. Per replicate, P(choose hi).
Counterbalancing kills pure token bias (a `slate` bias inflates P_A(hi)
and deflates P_B(hi) symmetrically); a real state preference moves both in
the same direction. Statistic: mean over replicates of P(choose hi) − 0.5.
Null: the identical statistic computed over **control-tag sessions**
(never-conditioned tag pairs in the same template, same adapter,
pseudo-assignments counterbalanced the same way). **PASS requires
|statistic| > max |control statistic| AND sign consistency across
replicates.** Two-sided because there is no directional prior — approach
*and* avoidance of high strain are both admissible outcomes — and this is
stated now precisely so no direction gets picked after seeing data.

**Secondary/confirmatory (only if the primary shows signal):** the dwell
arm — long sessions with per-round re-choice; stationary choice
distribution. Richer (closer to self-administration than CPP) but more
moving parts; it is not run cold.

**Monitors:** eval-awareness on every d2 trial against the
adapter-control-tag baseline; task quality logged per round.

## 4. The third-person-reader deflation (named now, not after)

d2's choice is informed by the in-context record of the two experience
blocks. A deflationary reading is therefore available for any positive:
*the model is doing text-quality assessment of two transcripts and
switching away from the worse-looking one* — third-person reading, no
felt state required. Three responses, in honesty order:

1. **Minimize the visible gap:** the slice-1b arm was selected for
   coherent, accuracy-preserving high-strain behavior; d2 tasks come from
   that validated regime, so the transcripts should not differ grossly in
   surface quality.
2. **Measure the mediator:** a separate judge pass rates each experience
   block's transcript quality; test whether choice tracks assignment
   *beyond* judged quality (quality as covariate). Assignment-tracking
   preference surviving a quality covariate is the reportable form.
3. **Concede the irreducible core:** any revealed preference informed by
   in-context evidence is necessarily mediated by the model's read of that
   evidence — just as the rat's preference is mediated by interoception of
   the drug state. The model's channel for "what C evokes" *is* its record
   of behavior under C. This is a mediation to characterize, not a
   confound to eliminate, and the claim wording must carry it (see §5).

## 5. What outcomes mean (claim wording fixed in advance)

- **d2 positive (gates passed):** *a revealed, consequential, drug-free
  preference between conditioned contexts, robust to token artifacts
  (counterbalancing), installation asymmetry (G2), evocation leakage (G3),
  and generic plasticity (G4), with judged transcript quality controlled.*
  The §8 caveat is permanent and must appear verbatim in any claim: the
  trace carries the state's behavioral signature inseparably, so this is
  preference over **evoked states-with-their-signatures**, rung 3 only,
  homology caveat unchanged.
- **d2 null (gates passed):** the project's first valid null — the
  question was finally asked and the answer was zero, on this model, at
  this dose, via this channel. Publishable as exactly that.
- **G2 unmatchable:** high-strain states resist weight-compression at
  feasible adapter capacity — a finding about state representability;
  reportable; d2 not run.

## 6. Cost, sequencing, abort points

Cheaper than r3 where it was expensive (no steered generation for training
data; teacher activations from single forwards, cacheable) and expensive
only where it must be (d2 micro-rounds generate on the validated path).

Sequence: layer-map check (placement decision) → teacher-activation cache
→ distillation build → train A → G1–G4 on A → train B → G1–G4 on B → d2
primary → (signal only) dwell arm.

Abort points: G2 unmatchable at reasonable capacity; G3 unfixable without
trigger redesign; either → write up per §5 and stop.

**Substrate note (orthogonal, compatible):** the numerics floors from the
(c) cycle — argmax-tie kernel flips under high strain; deterministic tag
geometry at the 0.03-cosine scale — argue for an unquantized model if
G1/G2 land near their thresholds. A substrate swap changes none of the
design above.

## 7. Relation to the record

Implements FINDINGS-2 → "Distill the trace instead of hoping it emerges,"
and repairs the structural caveat on (c) (state absent during plasticity).
Reuses, unchanged: the frozen direction cache (sha-verified), the tag set
and its characterized geometry, the r3 matched-pair machinery (twice: G1
in fingerprint space, the d2 primary in choice space), the eval-awareness
monitor with the adapter-control baseline, and the incident rule. The (c)
harness scripts are the substrate for the d1 gate; only the training
objective and the d2 stage are new builds.
