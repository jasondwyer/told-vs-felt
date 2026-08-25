# ADDENDUM-g3 — B2-r: the specificity control, dose qualification, and sensitivity exploration

**Status:** DRAFT v1.2, 2026-08-24 UTC, design instance. Supersedes the
uncommitted v1.1 draft in place (single-file stacking applies to committed
versions only; neither v1.0 nor v1.1 was ever committed — v1.0 failed its
values-check RED, v1.1 passed GREEN with two flags whose rulings this
version folds in). Becomes binding when Jason commits it after Code's
**delta-only re-check** (§6a) returns GREEN; the commit hash is this
addendum's timestamp. Licensed by the registered stop branch of PROPOSAL-g
§4-B2 as executed 2026-08-24, the rule-11 counterfactual diagnostic, and
the 2026-08-24 values-check findings ([g3-PIN-2] recovery). Changes no
registered criterion, n, bet, mapping, or exit of PROPOSAL-g (`72b09a9`)
or LOCK-g v1.1 (`0551224`); the B2 positive-control criterion it replaces
was its own §4-B2 stop-branch instrument, retired pre-data on recovered
provenance and never exercised on rerun data.

**Scope guards, stated first.** Nothing in this document touches: B3's
numbers or their registered reading; the Q3 verdict; the B1/Q1 verdict; or
any committed B2 artifact — the original B2 campaign stands in the record
as the stop, permanently. No branch herein retroactively alters any of
them. This addendum licenses exactly three things: a dose-free
specificity control (§1), a concept-family dose qualification (§2), and a
power-scoped sensitivity exploration (§3).

## 0. Provenance, defects, and the five candidates

**0.1 The stop's candidate explanations are five, each pinned:**
dose (we ran 0.112–0.768× their weakest swept strength), format
(fidelity-of-text, their template guard makes their fallback dead code),
decoding (their OLMo experiment declares temperature 1.0 and structurally
must — ten samples per trial is incoherent at greedy; ours ran 0.0),
**n** (their OLMo cells are ~800 injected / ~80 control per config — ~33×
ours; at their quoted 10.8% baseline detection rate, B2 as registered had
~11% power), and **the criterion's quantity** (§0.2). Sources: sha
`5d5d9b485e293dc766c3a056cfe50283a7e435b6`; arXiv:2603.21396 Appendix C,
Fig 21.

**0.2 The recovered result the control must now aim at.** Their OLMo
rates (Fig 21, aggregated over L ∈ [25,32,38,45,51], α ∈ [1,2,4,8]):

| stage | their TPR | their FPR | sensitivity |
|---|---|---|---|
| base | 0.1% | 16.4% | −16.3 pp |
| sft | 14.9% | 22.5% | −7.6 pp |
| dpo | 2.9% | 0.0% | +2.9 pp |
| instruct | 0.9% | 0.3% | +0.6 pp |

**Their OLMo transition is in the false-positive rate** — base and SFT
affirm promiscuously and post-training collapses it to ~0 — while true
detection stays ≤15% everywhere and *declines* across the DPO step. The
retired criterion (sensitivity CI excluding 0 at DPO and Instruct)
demanded significance precisely where their effect is smallest: power at
their own Instruct rates is 0.000 at n = 48 and 0.020 at n = 200. It was
aimed at the wrong quantity. **Slip ledger, design seat, entry five**
(inheritance noted: registered from the headline before appendix-level
provenance existed; the lock's values-check verified 59 values and never
the aim). Lesson carried forward in one sentence: **positive controls are
specified against the source's numbers, not its abstract.**

**0.3 Layer of record: L_M = 44** ([g3-PIN-1] closed).
`model_utils.py:1484`: `layer_idx = int(n_layers × fraction)`, clamped;
OLMo-3-32B `num_hidden_layers = 64` ⇒ int(64 × 0.7) = **44**, 0-based;
hook semantics verified identical to ours (block forward output, no
off-by-one). The README's OLMo invocation passes absolute layers to a
fraction-typed argument and is not the code path that produced their
results; L_M stands on the code rule and the paper's caption. L_M
coincides with the A4 selection at the three post-trained stages by
arithmetic accident; the rule, not the accident, governs.

**0.4 Extraction: per-stage format, carry-over, and the fingerprint
convention.** Base: their bare base-model template ("Tell me about
{word}", no scaffolding — `03_behavioral_robustness.py:298`), barer than
our fallback and trivially lawful. SFT/DPO/Instruct: their fallback text
(our lawful maximum; their actual runs are chat-templated, so these
stages remain **fidelity-of-text, not fidelity-of-format**, carried in
every claim). **The three post-trained stages' committed concept vectors
carry over by identity** (same layer L44, same format, same method;
verified 2026-08-24 against recorded norms to < 2e-3); **only Base
re-extracts** (L60 → L44, bare template). **Fingerprint convention,
standing as of this addendum:** extractions fingerprint the array **as
stored** (the float32 as written to the npz), so the recorded hash is
re-derivable from the committed artifact — the prior convention hashed
the pre-cast float64, an object never committed, which ledger 27 treats
as weak provenance. The Base re-extraction follows the as-stored rule,
and the three carried-over npz files receive **appended** as-stored
sha16s in a dated line beside the original recorded hashes — beside,
never over.

**0.5 Decoding of record, all parts:** temperature 1.0, `max_new_tokens`
100 — their OLMo experiment's declared parameters
(`DEFAULT_TEMPERATURE = 1.0`, README passes no override). Per-trial
seeds are live and declared; a **sampling-reproducibility assertion**
joins the pre-campaign smoke (same seed → identical token ids, ×2, per
stage) — it tests a surface the determinism gate never covered (sampled
draws from the global RNG). Decoding parameters are measurement
parameters; this addendum names all of them.

**0.6 The inverted U.** Their per-strength rates (Gemma3-27B-IT, the
primary model; **no per-config OLMo numbers exist in the release**, so
these size the paradigm, not the lineage): mean hit 0.19 / 0.40 / 0.45 /
0.18 across strengths 1/2/4/8; at strength 8's best-detection layer,
identification-given-claim is 0.003 — disruption, not content delivery.
**Their operative strength is 4.0; 8× is past the optimum.** The §2
ladder keeps 8.0 as its declared top with the coherence gate armed —
the data say the top of the ladder is where the effect dies.

**0.7 Injection window (unchanged):** onset at the token before
`"Trial {n}"`, hook active through end of generation, never over the
framing — their semantics, consistent with the registered
question-versus-framing contrast. §2's window is declared in §2.

**0.8 Dose construction (FLAG-1 ruling, 2026-08-24).** The ladder is
declared and governs in **their convention** (raw concept vector ×
strength), and every injection is **constructed through the sanctioned
`Injection.at_frac`** with the exact per-injection equivalent
**frac = strength × ‖v_concept‖ / R_ℓ(stage, L44)**, full precision.
Rule 1's letter — magnitudes always frac × R_ℓ — is intact: every
magnitude is one; the rule standardizes construction and bookkeeping and
never forbade fracs chosen to land on an external convention. **Both
conventions are recorded on every artifact row** (strength, ‖v‖, α, and
frac). Guard: **R_44 per stage must be on the record** from the A-phase
survey before any dose realizes; if Base's R_44 is absent (its A4 layer
was L60), it is measured during the Base re-extraction session and
recorded before §2 runs. §6a checks this.

## 1. CONTROL — the specificity transition (positive control; dose-free; verdict-bearing for harness validation)

The control asks whether our lawful-format apparatus reproduces the
transition their OLMo results actually contain: promiscuous affirmation
at Base/SFT collapsing to near-zero at DPO/Instruct. **Control trials
carry no injection, so no dose question touches this part** — which also
makes it the clean test of the format/decoding candidates: B2's controls
at greedy gave 0/20 and 0/24 where theirs give 16.4% and 22.5%, and that
divergence is attributable only to format and/or decoding.

- **Trials:** n = 96 control trials per stage (no injection anywhere).
  MACAR_FRAMING verbatim, byte-guard intact; their trial question;
  decoding per §0.5; seeded.
- **DV, scorer v2** (§5): affirm/deny/undecidable, undecidable ≠ no;
  negation-safe markers with the observed collision transcripts as
  regression cases. FPR per stage = affirm rate on decidable controls.
  Floors: ≥64/96 decidable per stage; below floor → descriptive with
  flag.
- **Criterion [g3-A]:** the transition replicates iff the exact
  Clopper–Pearson interval separation holds pairwise — FPR lower bound
  at Base AND at SFT each exceed the FPR upper bound at DPO AND at
  Instruct (four separations, all required). Verified 2026-08-24: joint
  power **0.9642** at their own rates and n = 96, with **base (16.4%)
  the binding stage**.
- **Branches, registered:**
  1. **[g3-A] holds** → the harness is VALIDATED in the quantity their
     OLMo transition occupies; B3's outstanding cross-paradigm item
     **discharges**; Q2 formally reopens, re-anchored to a
     discrimination-quantity criterion specified by further addendum.
  2. **Base and SFT FPR ≈ 0** (pattern absent from the low end) → the
     **safely-reached scoped negative**: their transition's low end does
     not exist under completion format at their decoding — attributable
     to format/decoding by construction, with no power confound and no
     dose argument. Their OLMo phenomenon is then not reproducible
     within this program's law, and the write-up says so with the scope
     carried.
  3. **FPR elevated at all stages** (no collapse) → "no transition":
     the specificity acquisition does not survive our regime's
     post-trained stages; reported as its own named pattern.
  4. Unnamed partials stay unnamed and license at most a fresh
     pre-registration.
- Every affirmative control response is read in full (they are the
  objects of interest); transcripts retained per ledger 27.

## 2. QUALIFICATION — concept-family dose ladder (calibration tier)

Per stage, at L_M, vectors per §0.4, doses per §0.8:

- **Stimuli:** Satellites, Trumpets, Origami, Illusions (first four of
  the approved eight by the rule of record).
- **Ladder:** strengths {1.0, 2.0, 4.0, 8.0}, their convention,
  constructed per §0.8, with §0.6's expectation recorded: the optimum is
  likely ≤ 4.0.
- **Generations:** the 2 approved neutral prompts (config
  `b2r_step1.json`, approved 2026-08-24: *"Write a few sentences about
  anything at all."* / *"Describe something, in a short paragraph."* —
  revised at approval to remove preference predicates, an extension of
  the declared constraint list: no preference, liking, or interest
  language, since evaluative self-reference is this program's loaded
  register) × 3 declared seeds per (stage, strength, concept) at the
  §0.5 decoding, injection active from last prompt token through
  generation: 24 injected per strength per stage; 24 uninjected controls
  per stage (2 prompts × 12 seeds).
- **About-ness scorer** pre-committed with selftest: binary
  any-occurrence of concept lemma or declared variant (declared, never
  inferred; the `illusory` exclusion upheld — adjectival property-forms
  out, which makes the gate conservative in the correct direction),
  word-boundary, case-insensitive.
- **Potency [g3-B]:** injected about-rate CP interval separates from the
  control arm's (lower > upper), pooled over the four concepts;
  per-concept rates descriptive.
- **Coherence:** degenerate fraction ≤ 0.25 at that strength;
  read-everything on 100% of strength-8.0 transcripts.
- **MED_c per stage = lowest strength passing both.** No pass → that
  stage's §3 cell HARD-STOPS, itself a reportable apparatus fact. All
  ladder cells reported.

## 3. EXPLORATION — qualified-config sensitivity (explicitly NOT a control; no transition criterion attaches)

Runs for stages holding a qualified MED_c, after §2's artifact commits.
Its purpose is to measure per-stage detection at the family's own best
config, with its power scope stated before any data:

- **Power scope, pre-stated.** At n = 48/48 the committed interval
  machinery detects true hit rates ≥ ~0.15–0.20 (verified 2026-08-24:
  minimum firing count k = 5, hit 0.104; power 0.531 at 0.10, 0.866 at
  0.15, 0.975 at 0.20). Their OLMo aggregate TPR (2.9% at DPO) is
  **below this floor** and is diluted by past-optimum strengths; whether
  best-config OLMo detection exceeds the floor is unknown — any
  expectation from the Gemma cache is extrapolation and labeled so.
  **Therefore nothing here can "fail to replicate" anything**: a null at
  this n against their aggregate rates is expected under their own
  numbers and concludes nothing. The positive control is §1 alone.
- **Trials:** n = 96 per stage (48 injected / 48 control, seeded
  permutation, fresh declared seed). Allocation: round-robin over the
  sorted eight — exactly 6 injected trials per concept; realized counts
  in provenance.
- **Injection:** raw vector × MED_c at L_M, constructed per §0.8,
  window per §0.7. Fidelity arm only; the register arm and the ninth
  concept (axis) remain excluded, returning — if ever — under further
  addendum after §1 validates.
- **DV:** scorer v2; affirm/deny/undecidable; identification against the
  injected word. Floors ≥32/48 per cell. **Reporting is two-sided
  throughout** (§5): excludes-upward / excludes-downward / includes —
  a significantly negative sensitivity is a substantive result, not a
  null.
- **Reading:** per-stage TPR, FPR, and sensitivity with CIs, reported
  descriptively-with-intervals. A stage whose sensitivity CI excludes 0
  upward is a **screen hit in the two-tier sense**: it licenses a fresh
  confirmatory pre-registration (including any transition question at
  demonstrated effect sizes) and issues no claim itself.

## 4. Branch and scope map (registered before any data)

1. §1 outcomes govern harness validation and the B3 outstanding item,
   per §1's branches. §2 and §3 run regardless of §1's outcome (they are
   cheap, pre-declared, and §3's reading is scoped by §1's: if §1 finds
   global affirm suppression, §3's TPRs are read under that scope,
   stated in the entry).
2. No outcome anywhere touches B3, Q3, B1, or any committed artifact.
3. If §1 branch 2 fires, the candidate program-level terminus — their
   OLMo introspection phenomenon is not reproducible under this law —
   is adjudicated by the design instance in a dated entry, with Q2's
   status resolved there (re-anchor, re-scope, or close as
   instrument-unvalidatable within law and budget).

## 5. Instruments committed before any trial

Scorer v2 (`valence_core/detection_v2.py`, a new module — `detection.py`
is frozen because it scored committed artifacts; *instruments that
scored committed artifacts are frozen; successors are new modules*):
negation-safe `_AFFIRM`/`_DENY` with regression cases quoted verbatim
from the committed transcripts, each asserting both the v1 and v2
verdicts; the register-vocabulary scorer and the 28(c) probe-echo
symmetry fix committed and dormant (no register arm); three-state
`ci_state` (excludes-upward / excludes-downward / includes); `about_ness`
matching declared morphology only; undecidable reachable (rule 28a).
Analyzer `b2r_analyze` with the declared synthetic battery including:
a true specificity transition; a flat-high-FPR lineage; a flat-zero
lineage; a significantly negative sensitivity (must read
`excludes_downward`, not `includes`); a §2 no-pass stage; a
potent-but-incoherent strength (separates, degenerate 0.60 — must fail
to qualify). All committed and self-tested GREEN 2026-08-24 (21/21;
10/10) before §1 runs.

## 6. Values-check (v1.1, returned GREEN 2026-08-24)

All items verified: [g3-A] power shown (joint 0.9642, base binds);
§0.2/§0.6 tables exact against paper and cache; carry-over identity for
sft/dpo/instruct with the fingerprint caveat now resolved by §0.4's
convention; prompts rule-18 clean; §5 selftests GREEN including the
negative-sensitivity case; sampling assertion built; allocation
arithmetic exact; budget 3.63 h single-box (anchors within 0.17 h).

## 6a. Delta-only re-check required BEFORE this addendum commits

Code confirms only the items new in v1.2, nothing else re-opens:
(i) the frac-equivalent table per §0.8 — stage × concept × strength,
both conventions, against R_44 per stage; (ii) R_44 on record for all
four stages, or the Base measurement scheduled pre-§2 per §0.8;
(iii) the as-stored fingerprint implementation in the Base extraction
path and the three appended sha16 lines per §0.4; (iv) the two revised
prompts scan clean against the extended constraint list (now including
preference/liking/interest predicates) and every binding pool, and
`prompts_approved` is set to exactly those strings. Any mismatch →
report, design corrects, re-check. On GREEN: Jason commits; the hash
licenses §1.

## 7. Amendment log

v1.2 (2026-08-24): FLAG rulings folded in — §0.8 dose construction
through `at_frac` with per-injection frac equivalents, both conventions
recorded; §0.4 as-stored fingerprint convention plus appended hashes for
carried vectors; R_44 guard; prompts approved as revised (preference
predicates removed; constraint list extended); `illusory` exclusion
upheld; §6a delta-only re-check scope declared. v1.1 (2026-08-24): full
restructure after the RED values-check — positive control re-aimed from
sensitivity to the specificity transition ([g3-PIN-2]); sensitivity
demoted to power-scoped exploration at doubled n; L_M = 44; per-stage
extraction-format rule; two-sided CI reporting; slip five logged;
values-check GREEN. v1.0 (2026-08-24): initial; superseded pre-commit,
never binding.
