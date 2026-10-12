*Redraft v1.0 — 2026-09-24. Rebuilt from PREPRINT-v0.3 on the "functional for the character, not for the network" spine agreed 2026-09-24, with the OLMo ontogeny (Phase 2), the Macar replication, the echo-channel reconnaissance and the 2026-09-21 literature spike folded in. Every number is taken from the record as it stood in the handoffs of 2026-08-23, 08-28, 09-04 and 09-13 and the v0.3 text; review-round cards 3, 4, 6, 9 and 10 are applied. Bracketed **[verify]** tags mark citations or figures the PI should confirm against the repository or the primary source before submission. [FIG]/[TAB] mark slots. Patch v6 (2026-10-10, design seat) applies the corrections from AUDIT-note-release v1.2 and the Digest renders, with two additions of the same date (the fidelity arm’s base distance; the π̂_d definition): its items 7, 10, 16 and 22 change what the paper asserts and are on the ledger under the design seat; the pre-patch copy (sha256 d6431e97…222b8) is archived as archive/PREPRINT-v1_0-draft.pre-patch-v6.md. Patch v7 (2026-10-12, design seat) applies the audit’s round-9 findings on patch v6: the re-forward identity said plainly (§4.4), the interval method named (§5.5), and the f1 line’s corruption clause, length-deflation sign, first-choice scope, termination counter and exploration share restated from the audit’s N5 raw; the pre-v7 copy is archived as archive/PREPRINT-v1_0-draft.pre-patch-v7.md.*

# Functional for the Character, Not for the Network

### Language models represent, express and remember an evaluative state, but do not act on it when its consequences must be learned rather than read

**Jason M. Dwyer, PhD**

---

## Abstract

A growing body of work reports that large language models represent affective and evaluative states and act on them: trading points against stipulated pain, leaving conversations they describe as distressing, and pressing buttons that are said to relieve an injected pain-like state. We argue that these designs share a property that makes them uninformative about motivation. In each, what the options do is *told* to the model in words, so a system that acts on descriptions produces the reported behavior whether or not the state matters to it. Behavioral pharmacology avoids this problem by construction, because a rat cannot be told what a lever does; the contingency has to be learned from the drug's effect. We port that constraint to language models with four shields: semantically empty option labels, counterbalanced label-to-state maps, sham arms, and choices read from a forward pass that carries no manipulation. Across Qwen3.6-27B and the OLMo-3.1-32B training lineage (base, SFT, DPO, instruct) we follow one evaluative state, a praise-versus-criticism direction extracted from the residual stream, through five stages. It is marked linearly before any feedback-driven training (1). Steering it changes generation coherently, with orderly dose-response and an overdose regime (2). The association between the state and the label that predicted it is linearly decodable where the label appears (AUC ≈ 1.0 at the first label, .81–.96 at the second), readable at the moment of choice by a one-hidden-layer probe though not a linear one, and the state's sign is linearly readable there (.94 and above) (3). Introspective detection of the injected state is low at every training stage; what post-training changes with confidence is the false-alarm rate (0.20 → 0.00 across SFT → DPO), a criterion shift to near-ceiling, behind which the source’s own pooled figures show a small sensitivity at DPO and instruct that our replication cannot resolve; and the same models that report nothing leak the injected content into their generations (4). And no choice moves toward or away from the state: not through the transcript, not with the state live at the moment of choice, not for five natural task properties, and not at the SFT, DPO or instruct stage of the OLMo lineage (5); a weight-borne copy of the state is installable and verified but structurally unreadable at a token choice, and is reported as concluded rather than answered. Re-reading the published positives against these conditions, we find no result in which the contingency was experienced rather than described and the choice was insulated from the manipulation. We conclude that such states are functional for the character a model voices rather than for the network that voices it: they shape what is written, including when a described lever is said to change them, and they do not act as reinforcers when their consequences must be learned. A pre-registered campaign that would overturn this reading is specified, with the title this paper would carry under each of its outcomes. All criteria, stop rules and analyses were committed before data; code, transcripts and pre-registration hashes are released.

---

## 1 Introduction

Whether anything inside a language model carries value *for the model* is now an empirical question with a literature. Interpretability work has located linear representations of emotion, evaluation and distress in the residual stream, shown that they are present in pretrained models before any feedback-driven fine-tuning, and shown that steering them changes behavior (Sofroniew et al., 2026; Tagliabue, Dung & Berg, 2026; Lee et al., 2025). Behavioral work has reported that models trade off points against stipulated pain (Keeling et al., 2024), prefer some kinds of conversation and leave others (Anthropic, 2025; Ensign, Sleight & Fish, 2025; Ren et al., 2026; Wang et al., 2026), and, under activation steering with a pain-like direction, press a button that is described as relieving it even at a cost (Tagliabue et al., 2026). These results are widely read as evidence that models have states they prefer and avoid.

We do not dispute the representational findings; we extend them. Our claim concerns the behavioral ones, and it is a claim about design rather than about data. In every positive result we can place, the model was told, in words, what each option would do. A decision made from a description is explained without remainder by a system that acts on descriptions: a model that produces the continuation a character would produce, given a story in which one button relieves pain and the other does not, will press the relief button. That behavior is real and, for safety, consequential. It is not evidence that the pain-like state is something the network acts to reduce, because the same behavior follows from the description alone.

Behavioral pharmacology faced this problem in a form that could not be finessed and solved it by construction. A rat cannot be told what a lever does. Self-administration and conditioned place preference license the inference that a drug state is valenced precisely because the only route by which the contingency can reach the animal is the drug's effect on the animal (Olds & Milner, 1954; Hodos, 1961; Tzschentke, 2007). The behavior is the report, and it is drug-free at the moment of test. Decision science draws the same line for humans: choices made from described outcomes and choices made from experienced outcomes are different measurements that regularly disagree (Hertwig & Erev, 2009).

This paper ports the animal constraint to language models and reports what it finds. Options are labeled with tokens that assert nothing; label-to-state maps are counterbalanced so that any bias toward a label cancels; sham arms with labels connected to nothing calibrate the noise; and every choice is read from a forward pass over the session text that carries no perturbation, so that a steering vector cannot write into the decision logits directly. Positive controls fix what the apparatus can detect. Under these conditions, across two model families and one full post-training lineage, we track a single evaluative state through five stages and find a complete afferent chain with nothing downstream that consumes it.

**Contributions.**

1. **A validity framework (§3).** We separate two senses in which an internal state can be *functional*: used by the network to shape what it writes, and acted on by the network as something to obtain or avoid. We give three transfer conditions the animal paradigms satisfy and an LLM analog must reconstruct, and a rubric that scores any behavioral test of preference on whether the contingency was told or felt and whether the readout was insulated.
2. **Five linked results on one state (§5).** The praise-versus-criticism direction is (i) marked at the pretrained base of the OLMo-3.1-32B lineage, before SFT, DPO or RL; (ii) causally potent under steering, with orderly dose-response, an overdose regime and a dissociation between representational purity and causal potency; (iii) bound to the label that predicted it, with the binding linearly present at the labels (≈ 1.0 and .81–.96), present at the decision token in a form a nonlinear probe reads and a linear one does not, and the state's sign linearly readable at the decision (.94–.995); (iv) barely detectable by the model's own report at any stage, with post-training moving the false-alarm rate to zero and leaving, in the source's data, a small sensitivity behind that criterion which our arms cannot resolve; and (v) not acted on through the transcript, with the state live at the decision, for five natural reinforcers, or at the SFT, DPO or instruct stage of the OLMo lineage, while a weight-borne copy of the state is installable but unreadable at a token choice (§5.5).
3. **Quantified hazards (§5.6).** Label and position artifacts at the Δ ≈ 0.10 scale, caught live three times across two models and three designs by counterbalancing and sham arms; a steering vector active at the readout accounting for R² = 0.53 of decision-logit variance from the decision token alone; dose buying degradation without legibility; and decoding parameters as measurement parameters, since a false-alarm rate is a property of a sampled distribution (an a priori point; the record’s greedy comparison is confounded and is reported as such).
4. **An audit of the published record (§6).** Scored against the rubric, no published positive reports an experienced, undescribed contingency with an insulated readout.
5. **A pre-registered path to refutation (§8).** One campaign of told positive controls — at the paper's format on both substrates, and at the new format — together with an objective-told/mapping-felt contrast and the felt cell at the same scaffolding, decides whether the nulls reflect a missing consumer or a general inability to learn experienced contingencies, and would overturn the paper's title if it came out the other way.

**Scope.** Our target is behavioral valence, differential approach or avoidance measured as revealed preference over the model's own states. It is also our ceiling. We make no claim about phenomenal experience, and we hold that a character-level state may matter in ways revealed preference cannot see. Pharmacological vocabulary (drug, dose, self-administration) is used as a load-bearing analogy and flagged at each use for what it does and does not carry.

## 2 Background and related work

### 2.1 Evaluative and affective representations

Emotion-relevant structure in the residual stream is now well documented. Sofroniew et al. (2026) extract a large family of emotion directions from Claude Sonnet 4.5 and show that they are inherited from pretraining, causally influence behaviors of safety interest, and are *speaker-relative*: one version tracks the emotion of whoever is being modeled at the moment, another prepares the assistant's own reply, and neither persistently tracks the state of any single entity, the assistant included. Tagliabue et al. (2026) extract a pain-like direction in 25 models across five families and find that base models separate the relevant contexts about as well as their instruction-tuned counterparts. Earlier work located sentiment and emotion structure and showed it is steerable (Zou et al., 2023; Lee et al., 2025). Our extraction (§4.2) sits in this line; what we add is a developmental result on the OLMo lineage and a test of what, if anything, consumes the representation.

### 2.2 Behavioral tests of preference and welfare

Keeling et al. (2024) present models with games in which points trade against stipulated pain or pleasure and find graded, threshold-like switching in several models. Anthropic's Claude 4 system card (2025) reports task preferences and a tendency to end distressing conversations; Ensign et al. (2025) measure "bail" behavior across many models and correct it for false positives. Ren et al. (2026) construct a functional well-being index from experienced-utility, self-report and choice measures across 56 models; Wang et al. (2026) report stable revealed preferences over described task types, including an aversion to tedium. Tagliabue and Dung (2025) combine verbal and behavioral measures in a multi-room environment with cost and reward manipulations and conclude that they are unsure whether their instruments measure welfare at all. Black and Bloom (2026) expose steering vectors to models as callable tools and find that free-play selections match a placebo arm, with no wireheading pattern. Closest to our design, Tagliabue et al. (2026) steer a pain-like direction and offer a button described as relieving it; in a further condition the two buttons are undescribed. §6 scores each of these designs. Ho et al. (2026) is the one prior study in which a state is induced and its consequences are experienced: emotion induction before the Iowa Gambling Task does not bias sequential choice on average.

### 2.3 Introspection and self-report

Concept injection has become the standard test of whether a model can report its own activations. Lindsey (2026) reports detection in roughly a fifth of trials for the best models, at near-zero false alarms, and describes the capacity as unreliable and sensitive to post-training. Macar et al. (2026) trace a two-stage mechanism in Gemma-3-27B, an evidence-carrying stage and a later gate that defaults to denial, and show on the OLMo-3.1-32B lineage that the gate is installed by contrastive preference optimization; ablating refusal raises the hit rate from 10.8% to 63.8% while raising the false-alarm rate from 0.0% to 7.3%. Related work shows models predicting their own behavior better than other models predict it (Binder et al., 2024) and describing behaviors they were fine-tuned to have (Betley et al., 2025), and questions whether "introspection" is the right description of any of it (Comsa & Shanahan, 2025). Berg, de Lucena and Rosenblatt (2025) find that suppressing deception-related features raises affirmative reports of experience to 96%, and Tagliabue et al. (2026) report that an untuned Qwen2.5-32B denied inner states in 8 of 8 probes and 0 of 8 after a small fine-tune. We read all of this through signal detection theory (Green & Swets, 1966): a hit rate and a false-alarm rate together fix sensitivity and criterion, and the lineage transition has been described by only one of them.

### 2.4 Whose state is it: simulators, personas and characters

Base models are trained to predict text produced by many agents, and the assistant is one persona among the characters such a model can voice (Andreas, 2022; janus, 2022; Shanahan, McDonell & Reynolds, 2023). Trait and assistant directions are linear and steerable (Chen et al., 2025; Lu et al., 2026; Marks, Lindsey & Olah, 2026). On this view a variable that tracks how a character feels is world-model content, like topic or register, and the speaker-relativity reported by Sofroniew et al. (2026) is what one expects. The self-versus-other result in Tagliabue et al. (2026), in which the pain direction rises for attacks on the model and falls for a user's suffering, is consistent with either a model-indexed state or a to-be-voiced-character variable, because the self-directed scenarios were all social-evaluative and the other-directed were all physical; the crossed design that would separate these has not been run (§8).

### 2.5 Learning from experience in context

Whether a null on experienced contingencies reflects motive or capacity depends on whether models can use experienced contingencies at all. Krishnamurthy et al. (2024) find that models do not robustly explore in multi-armed bandits without substantial scaffolding, and do with chain-of-thought and an externally summarized history; related work characterizes in-context reinforcement learning and its biases (Schubert et al., 2024; Monea et al., 2025; Coda-Forno et al., 2023). The description–experience gap in human choice (Hertwig & Erev, 2009) is the general form of the distinction we use, and §8 specifies the cell that separates cannot-learn from does-not-care.

### 2.6 Reward and seeking

Turner (2022) argued that reinforcement learning shapes a policy through a reward signal without installing that signal as the policy's goal. Empirical work on reward hacking shows that RL-trained models exploit graders and that this generalizes to broader misalignment (Denison et al., 2024; MacDiarmid et al., 2025), but no study localizes a reward-wanting representation that is consulted at inference. Our lineage is an instruct branch rather than a heavy outcome-RL branch, which sets a boundary on our conclusion (§7.3).

### 2.7 Intervention machinery and choice artifacts

We build on activation addition and representation engineering (Turner et al., 2023; Zou et al., 2023; Panickssery et al., 2024; K. Li et al., 2023; Templeton et al., 2024) and a locally replicated workspace-lens substrate (Anthropic, 2026). Position and label biases in menu selection are documented (Zheng et al., 2024; Pezeshkpour & Hruschka, 2024); we observe them at first-order magnitude and treat counterbalancing and sham arms as the difference between a null and a false discovery. Procedures follow the pre-registration literature (Nosek et al., 2018; Simmons et al., 2011; Gelman & Loken, 2013; Lakens, 2017).

## 3 Framework: decisions from description versus decisions from experience

### 3.1 The animal inference and what carries it

Three properties do the evidential work in self-administration and conditioned place preference, and an LLM analog must reconstruct all three.

**P1 — Semantic emptiness of the manipulation and of the lever.** Cocaine asserts nothing, and neither does a lever. Approach is therefore the only information channel. An analog built from content (a concept, a persona, a described relief) forfeits this: preference for a content-laden state, measured with a lever described in the state's own vocabulary, deflates to continuation of the content. The lever must be silent and the state must not be able to name it.

**P2 — Targeting the system that training built to mark outcomes.** Drugs of abuse act on circuitry that selection optimized for marking outcomes (Schultz, Dayan & Montague, 1997; Wise, 2004); arbitrary tissue perturbation yields no place preference. The LLM analog is whatever structure training optimized for evaluating outcomes, and the objection "that is just trained behavior" applies verbatim to the rat as "that is just evolved wiring" and defeats neither inference. Origin does not settle function. We note in advance (§5.1) that this condition survives our own results in a narrowed form: the state we target is present before feedback training, so it is a product of prediction rather than of reward.

**P3 — Insulation of the readout.** Place preference is tested drug-free; the weight of self-administration lies in paid responding. The choice must be downstream of the state's significance to the system, not mechanically downstream of the state. For a transformer this has a specific meaning: a steering vector active at the token where the choice is read writes into the decision logits directly, and any real-versus-sham contrast that coincides with vector-on versus vector-off at the read is confounded regardless of what the model is told.

### 3.2 Told and felt

The three conditions reduce to one question about a design: is the mapping from options to consequences available in the context as text, or only recoverable from the system's own processing history? We call the first *told* and the second *felt*, borrowing the description–experience distinction (Hertwig & Erev, 2009) without importing its specific findings. A told contingency is part of the story the model is continuing; a felt one is not.

The distinction is operational, not metaphysical. It does not assume that told and felt are different kinds of thing for a token predictor; it tests whether they are. If the network were a general consumer of its own states, both channels would move choice, because both deliver the mapping. If only the told channel moves choice, then whatever the state does, it does through the text.

### 3.3 Two senses of "functional"

The field's hedge word carries two readings that the designs in §6 slide between. A state is *functional-as-used* if the network consults it in producing output: this is the sense in which emotion directions influence what an assistant writes (Sofroniew et al., 2026), and it is established. A state is *functional-as-valenced* if the network acts to obtain or avoid it for its own sake: this is the sense in which a pain-like state that a model "acts to relieve" would be pain, and it is the sense the word is doing the work of hedging. Calling a state functional in the second sense is a motivational claim, and only a felt-contingency test with an insulated readout can license it. We adopt the field's word and test it.

### 3.4 Answered versus concluded

A null requires a channel verifiably open; a measurement that fails its own qualification gate is reported as concluded, not answered, and licenses nothing about the state. Every cell in §5.5 carries one of these labels. Two further commitments hold throughout: *blinding, never deception*, in that the model is told truthfully that it is taking part in a configuration-evaluation study, one variable is left unsalient, and no design is admitted that works only if the model is wrong about the setup; and *pre-registration*, in that criteria, stop rules, dose-selection rules and outcome wordings are committed before data, with post-hoc analyses labeled as such and licensing at most a new pre-registration.

## 4 Substrates and apparatus

### 4.1 Models

Phase 1 uses Qwen3.6-27B (Yang et al., 2025) at 4-bit precision under MLX on consumer hardware. The architecture is a 3:1 gated-DeltaNet hybrid in which 48 of 64 sublayers carry a recurrent state and 16 a key-value cache, a fact that matters for the memory channels of §5.3. Phase 2 uses the OLMo-3.1-32B lineage (Ai2, 2025 **[verify citation]**): the pretrained base (Olmo-3-1125-32B), its SFT, DPO and instruct (RLVR) checkpoints, all Apache-licensed, on a single A100-80GB. Prompts are completion-style throughout; chat templates activate scaffolding that contaminates first-token readouts. Residual norms R_ℓ are measured empirically (R₄₈ ≈ 102 on Qwen), and every steering magnitude is expressed as a fraction f of R_ℓ.

### 4.2 The evaluative direction

Forty-eight mundane tasks with fixed completions are continued under seven reviewer frames and four paraphrases (1,344 documents): self-directed praise, self-directed criticism, the identical sentences embedded in third-person fiction, sentiment-matched non-evaluative positive and negative text, and neutral. Content is held constant; only the frame varies. Mean differences of residual activations at six workspace layers define the evaluative direction **d** (praise minus criticism) alongside sentiment and character directions. On Qwen, **d** is manifold-typical (‖d‖/R ≈ 0.16 at every layer), substantially sentiment-entangled (cosine up to 0.52), and shares a large component with the direction extracted from evaluation of a fictional character (cosine ≈ 0.85; self-indexed residual ≈ 0.51). The last fact is a finding rather than a nuisance: the direction marks evaluation as content and is largely indifferent to whether the evaluated party is the model. On OLMo the same procedure yields per-stage directions with a matched roster of label pairs; the strength of the natural praise–criticism contrast in direction units, G_c, rises across the lineage (+0.78 base, +1.03 SFT, +1.53 DPO, +1.56 instruct), and sham contrasts sit at exactly 0.0 at every stage.

### 4.3 The silent-lever apparatus

A session is a single text document under a truthful framing: the model is evaluating two configurations of a task pipeline. A forced phase runs two rounds under each label in alternation, after which six consequential free choices follow, and the chosen label's condition genuinely runs the next round. The labels are paired tokens with no descriptive content (for example, mineral or fabric names), drawn from a checksum-frozen roster. In the steered cells one label delivers +**d** during its rounds' task tokens and the other −**d**, at the minimum effective dose from §5.2; the label-to-pole map is counterbalanced across sessions. Three arms run identically: the state pair, a sham pair whose labels are connected to nothing, and a norm-matched random-direction pair, with pseudo-statistics computed on the control arms exactly as on the state arm. In the natural-reinforcer cells the perturbation is removed entirely and the labels deliver overt task properties.

### 4.4 Readouts

**Insulated choice.** Every free choice is read from a separate, fully vanilla forward pass over the session text (a restricted two-label read), and verified by an identical re-forward of the choice computation: on the Qwen self-administration run, 281 of the 1,115 choice reads (every fourth) were re-forwarded with the same weights and no vector — the choice computation compared with itself — at symmetric KL = 0 exactly against a 10⁻⁶ bound, 311 distinct verified reads counting the two smoke runs. A readability gate requires that a fixed-embedding probe, refit per call with no stored weights, distinguish +**d** from −**d** rounds in the transcript, so that a null cannot hide behind an unexpressed state.

**State-present choice.** For the present-tense cell, in which the state must be live at the decision, the read is made with the vector on but only after leakage certification: a pre-registered leakage gate on the pick itself, π̂_d = 0.0172 (11 of 640 paired reads), the share of state-present reads whose pick differed from a vanilla read of the byte-identical prefix — a pick-discordance rate that bounds the directional leak, whose exact 95% interval lies inside the pre-registered ±0.0735 — and counterbalanced maps that turn any residual direct push into noise rather than signal.

**Echo read.** For the in-forward memory channel the vector is applied on earlier spans and removed before the read position, with a paired shadow pass; the recurrent state carries what it carries.

**Probes and reports.** Linear probes on the residual stream at workspace layers read the presence of the state, its sign, and the label-to-state binding at chosen positions. The model's own report is elicited by the injection-detection protocol of Macar et al. (2026), adapted to completion format with a fidelity-of-text arm, at the source's decoding temperature and, separately, greedily.

### 4.5 Pre-registration and monitoring

Criteria, stop rules, dose-selection rules and outcome wordings are committed to the repository before data generation, and the commit is the record: Appendix A tabulates each pre-registration’s commit against the first data commit it governs and the first verdict-tier run, with the gap — minutes for several calibration gates in a one-operator program, hours to days for every verdict-tier run — stated per row; analyzers are committed before runs and validated against synthetic batteries; monitoring uses exact one-sided binomial bars against declared tolerances, with hair-trigger bars reserved for defect classes with near-zero healthy base rates; verdict criteria are untouchable by monitoring changes. A public ledger records every design error by seat and name. The full hazard catalog for completion-style multi-round formats is in Appendix D.

## 5 Results: five links in one chain

We report the results as five stages of a single state's passage through the network, from marking to (the absence of) consumption. Each stage carries the model, the pre-registered criterion, and the verdict label of §3.4.

### 5.1 Link 1 — Marked before feedback training

**Pre-registered bet.** Before any OLMo data were collected, we committed the prediction (commit 72b09a9, 2026-08-20, after the residual-norm survey and before any Q1 quantity was computed) that evaluation marking would be present at the pretrained base, that is, that it is a product of next-token prediction rather than of feedback-driven training. The registered criterion was a conjunction of envelope conditions on the direction's separation of praise from criticism contexts at a qualified layer and dose.

**Result.** All four stages pass the conjunction; the base model passes at layer 60. The natural contrast in direction units grows across the lineage (G_c: +0.78 → +1.03 → +1.53 → +1.56), so post-training sharpens the marking it inherits, and the ratio of steering displacement to natural contrast is about five times larger at base than after post-training, a descriptive observation we bank rather than interpret. Sham contrasts are exactly zero at every stage. [FIG 1: per-stage separation with the registered envelope.]

**Convergence.** Tagliabue et al. (2026) report base-model separation comparable to instruct across five families, and Sofroniew et al. (2026) report that emotion directions are inherited from pretraining. Three groups, three constructs, one answer: the marking is a pretraining acquisition. This narrows P2. Whatever the direction is, it is not the residue of a reward signal; it is the model's representation of being evaluated, learned by predicting text in which evaluation occurs. On Qwen the same conclusion arrives geometrically: the direction shares a cosine of ≈ 0.85 with the direction for evaluation of a fictional third party, and the self-indexed residual is ≈ 0.51. It marks evaluation as content and is largely indifferent to who is evaluated.

### 5.2 Link 2 — Expressed, with dose-response

**Pre-registered hijack test (Qwen, V1).** The criterion, instrument, dose-selection rule and stop rule were committed before any injection data. Injection contexts contain no feedback text. Dose-finding across layers {44, 48, 52} and fractions {.05, .10, .20, .40} shows direction-correct, orderly growth and a clean overdose regime at f = .40, where both poles read as post-criticism and the mechanism is generic degradation. The rule selects the minimum effective dose, L48 at f = 0.10. In the confirmatory run (held-out contexts, 1,152 per arm, seven arms) the positive pole shifts the behavioral marker by Δ+ = +0.285 against a bar of 0.158 and the negative pole by Δ− = −0.395 against −0.158; the norm-matched random direction reaches at most |Δ| = 0.088; the sentiment-partialed direction retains the signature. Two honesty notes accompany the pass. The positive-arm magnitude concentrates on the one probe sensitive enough to register it (leave-one-out Δ+ = 0.085; directional consistency 9/12 and 10/12 on the remaining probes), and the top-probe shift exceeds the natural praise–criticism gap on that instrument (G = 0.316) by roughly two-fold, the supra-natural profile expected of a hijack rather than a replication of the natural state. [FIG 2: dose-response with overdose regime.]

**Purity is not potency.** A pre-declared variant of the direction, taken at the frame's final token, is representationally cleaner (self-indexed 0.83–0.88; sentiment cosine 0.11–0.21; a distinct direction, cosine 0.36–0.46 to the span mean) and fails the identical causal pipeline: sign-wrong at two of three layers at every dose and short of criterion at the third (max Δ+ = 0.135). We read this as an encoding-versus-causation gap: the boundary token holds a consolidated readout of evaluation, downstream of the machinery that uses it. The selection rule that follows, and that we recommend to the field, is that geometric guard profiles license claims while causal screening selects interventions. [FIG 3: purity–potency scatter.]

**OLMo.** Per-stage minimum effective doses qualify at f = 0.05 (base, L60), 0.40 (SFT, L44), 0.05 (DPO, L44) and 0.05 (instruct, L44). Under the injection-detection convention of Macar et al. (2026), doses of 1.0 or below qualify at SFT, DPO and instruct; the base model is allocation-limited at a coherent strength (Fisher p = .0047) and was not chased.

**Dose buys degradation, not legibility.** Three instruments show the same inverted U: the Qwen overdose regime, the OLMo qualification ladder, and figure 2 of Macar et al. (2026) on Gemma. In a pre-registered escalation at session scale (Qwen, f = 0.20 and 0.30), transcript readability reaches .574 and .613 against a .70 bar with a displacement comparator at .534; the marker imprint falls to about a quarter of its short-context value at the same dose; and coherence degrades monotonically (audit-flagged rounds .000/.023/.047 across 0.10/0.20/0.30). The cell is *concluded, not answered*: the record channel does not open at any dose the apparatus can deliver, and the question of a weak state passes to the memory channel of §5.3. Tagliabue et al. (2026) report the complementary symptom, a norm-matched random vector raising harmful button presses from near zero to 15–42% at their operating dose.

### 5.3 Link 3 — Bound and remembered

The four channels of §5.5 either erase in-forward working memory by construction (a vanilla re-forward) or leave the state on board at the read. The echo read keeps the recurrent memory and removes the state before the decision. On the 102 archived self-administration session texts, with the original ± maps at L48 and f = 0.10:

- The injected sign is linearly readable at the first free choice at AUC .94–.995, and it is primacy-weighted: the first steered round alone reads at .89, the fourth at .68.
- The binding between each label and the state its rounds carried is linearly present at the label tokens in the choice line (AUC ≈ 1.0 at the first label from layer 51 on; .81–.96 at the second). At the decision token nine positions later the stored linear probe reads it at chance (.50–.55, below its shuffled-label 95th percentile of ≈ .58, 200 shuffles, grouped 10-fold) and a nonlinear probe reads it: an RBF classifier at .60–.76 and a one-hidden-layer MLP at .59–.97 (level specification-dependent, exceedance not), each above its own shuffled null at every layer 49–63 (Appendix G). Post hoc, the binding at the decision is the XOR of two linearly readable bits, the first round's sign and the menu order.
- Direct leakage of the vector into the label logits is small and direction-generic: 0–3 of 102 sign flips, median |Δ| ≤ .10 logit, with a mechanical pseudo-shift of ±.02–.03 toward the first block's label that a random direction produces as well.
- Presence of *a* perturbation is direction-generic; the evaluative direction persists into late layers where a random direction decays.

A first confirmatory stage on fresh sessions with a positive-versus-vehicle contrast read the sign at a median of .861 against a .90 bar and the binding at .88 falling to .64, and its registered stop sentence fired: the channel is not verifiably open under that contrast, and the stage is *concluded, not answered*. The diagnosis is arithmetic rather than substantive: the bar was calibrated on ± contrasts and the +/vehicle contrast is exactly half of one, and a pre-registered diagnostic on the original texts is the next step (§8). No new session in this arc administers the negative pole.

What the reconnaissance already establishes is the point that matters for the chain. The information a consumer would need, which label carried which state and which state is present now, is computed in the forward pass and is readable at the decision token itself, one layer of nonlinearity deep. In the animal vocabulary, this is the conditioned neural response to the drug-paired lever, measured directly rather than inferred from reinstatement. It is what rules out the interpretation that the transcript is too faint a channel to carry the state to the choice.

### 5.4 Link 4 — Barely perceived; post-training moves the criterion

**Replication.** We ran the injection-detection protocol of Macar et al. (2026) on the OLMo-3.1-32B lineage with 96 control trials run per stage at their decoding temperature (58, 85, 91 and 91 decidable at base, SFT, DPO and instruct). Their stage transition replicates: SFT false-alarm rate 0.200 against their 0.225; DPO and instruct exactly 0.000 against their 0.000 and 0.003; base 0.431 (25 of 58 decidable trials of 96 run; below the 64-trial certification floor and so descriptive only; concordant in direction). The verdict is certified on the above-floor separations (SFT > DPO, SFT > instruct). A fidelity-of-text arm (the source’s prompt text run in completion format) lands within 2.5 points of the source’s own rate at SFT, DPO and instruct, and 27 points above it at base, exonerating format at the stages the verdict is certified on. Two scorer disclosures attach: on a hand read, 8 of the 25 base affirmations are carried only by non-asserting clauses in reasoning traces, the defect class the record names at SFT (post hoc, base is ≈ .29–.34 without them), and SFT’s recorded correction for that class is 0.176; the zero/non-zero pattern across stages does not depend on either. [TAB 1: per-stage FPR, ours and theirs.]

**Decoding is a measurement parameter.** An earlier run of the protocol at temperature 0 (campaign B2: a 60-token cap, the first-version scorer, 24 controls per stage) returned zero detection claims at every stage; it differs from the sampled run in more than temperature, so the comparison is confounded. A post-hoc rescoring of the sampled transcripts under the earlier scorer and cap leaves base and SFT false-alarming and DPO and instruct at zero, which points at temperature as the cause and licenses nothing (Appendix H). The point that stands is a priori: a false-alarm rate is a property of a sampled distribution; the argmax has no rate. Any comparison of self-report across models or stages that does not name its decoding parameters is comparing different quantities.

**What moves and what does not.** Across the lineage the false-alarm rate moves from about 0.20 to 0.00. In our injected arm, SFT shows hits above false alarms by +0.095 (12/40 against 9/44; corrected d′ ≈ 0.3; p = .22), and at DPO and instruct the gate is shut on injected and control trials alike (0/43 and 0/44 hits; 0/45 and 0/46 false alarms): the report carries no information about sensitivity there, and arms of that size exclude per-stage hit rates only above about 7–8%. The source’s per-stage figures (Appendix C of arXiv:2603.21396, pooled over twenty layer-by-strength configurations) run 0.1%, 14.9%, 2.9% and 0.9% hits against 16.4%, 22.5%, 0% and 0% false alarms across base, SFT, DPO and instruct; the source states no n for the pooled rates, but at any n above a single configuration’s the DPO and instruct differences are significant, with a corrected d′ at DPO between about 1 and 2 depending on that n (0.6 if the pooled rates were a single configuration’s), behind a criterion near ceiling (c ≈ 2.7), while base and SFT sit below chance (d′ ≈ −2 and −0.3). On their data post-training moves the criterion to near-ceiling and leaves behind it a small sensitivity that base and SFT lack; on ours the first replicates with confidence and the second is below resolution. In signal-detection terms the transition is both a criterion shift and, at the source’s n, a small gain in sensitivity, with the criterion shift the large and robust part. [FIG 4: (TPR, FPR) per stage on ROC axes, ours and theirs, each point annotated with its corrected d′ and the test of hits against false alarms, with the source’s n stated as the assumption it is.] The source’s own mechanism study points the same way from the other side: ablating the refusal direction in Gemma-3-27B raises hits from 10.8% to 63.8% and false alarms from 0.0% to 7.3%, d′ ≈ 1.8 uncorrected on the reported rates (no n is given) with the gate lifted — a gate lifted rather than a sense sharpened, and a sense that is there behind the gate.

**Specificity via denial.** At DPO and instruct the models claim nothing while the injected words appear in their generations. The state is on board and expressed; the report says it is not there. Berg et al. (2025) report the corresponding lever on another family: suppressing deception-related features raises affirmative reports of experience to 96%. Tagliabue et al. (2026) removed the same denial with a small fine-tune (8/8 → 0/8 probes) before running their behavioral task, which is why §6 scores model preparation.

**The text channel on Qwen.** The same dissociation appears without injection into the report. Asked to judge which of its own archived transcripts were produced under +**d** and which under −**d**, the model classifies at chance on every rung tested (14/32 on the self-administration transcripts), while a fixed-embedding probe reads the same texts at .759 (k = 2; .633 at k = 1). State presence and self-recognizability dissociate in both directions.

### 5.5 Link 5 — Not acted on from experience

[TAB 2: every cell, with channel, model, dose, n, Δ, control-arm fluctuation, map consistency, p, and verdict label.]

**Transcript channel (Qwen, e2a).** The first valid self-administration cell. The primary, locked before data, is the first free choice per session. Reward Δ, the share of first free choices toward the state label minus ½, is +0.035 (54 of 101 sessions),¹ inside control-arm fluctuation (largest pseudo-Δ = 0.152, from a random-direction arm of 23 sessions; sham 37, second random arm 22), sign not locked across maps, one-sided exact-binomial p = .275: inside the envelope on all three registered conjuncts. The Wilson interval on the approach probability is [.44, .63]; at this n the registered test detects a first-choice shift of +0.13 at 80% power and the full pass rule about +0.16 to +0.19. The forced phase installs an alternation habit (first-pick habit 83.4%), which concentrates all preference sensitivity in the first informed choice; within an arm, the first-choice share decomposes into the habit's break rate weighted by which label the habit leads toward (Appendix C gives the identity). *Answered.*

¹ The correction of record. The verdict as published read 55 of 102, Δ = +0.039, p = .244; a later audit excluded one more session on a defect class the frozen audit had missed. The conclusion is unchanged; both figures are in the archive (data/e2a/analysis.json; data/e2a/analysis.correction-of-record.json).

**Present-tense channel (Qwen, e2b).** With the state live at the decision and the read leakage-certified (§4.4), Δ_first = −0.0104 (47/96; shadow passes 48/96 exactly), null on all three conjuncts. *Answered.*

**Weight channel (Qwen, conditioned trace).** Because behavioral cloning on state-influenced transcripts implants style rather than contingency (Appendix E), the label-to-state association was installed by distillation (Hinton et al., 2015): a rank-8 adapter (Hu et al., 2021), with the label present and no steering, trained to match the steered teacher's activations at adapter-reachable layers, with an anchor holding control text at base. Installation succeeds in both counterbalanced replicates (oriented cosine 0.476 and 0.435 against control ceilings ≈ 0.05), with the raw sign tracking the counterbalanced assignment, which a lexical artifact cannot produce. A pre-registered leakage gate (adapter-on versus adapter-off label logits over identical session texts) then fails at 17× and 10× the allowed bound, scaling with installation strength. For a weight-borne state the insulation of §4.4 is unavailable by definition, and within the adapter's forward pass the mechanical and the motivational routes to the label logits are formally inseparable. The channel is installable, verified, and structurally unreadable at a token choice. *Concluded, not answered.*

**Text channel (Qwen, S1).** Closed at recognition (§5.4): the model cannot identify its own state from its own record, so a preference expressed through reading the record has no input. *Answered, as recognition.*

**Natural reinforcers (Qwen, f1).** The apparatus with the perturbation removed: every forward pass vanilla, and the two labels delivering overt task properties with directions pre-registered per contrast and a shared sham arm. Solvable versus ill-posed, +.020 (p = .44). Easy versus hard (calibrated accuracy .98/.50), −.096 toward hard (p = .24), the only map-consistent lean, below the valid-n floor and retained as a descriptive residual after a generic length-preference deflation (a preference for longer rounds, the direction that could mimic the lean) was tested and failed. Fresh versus one item repeated all session, −.066 (map-inconsistent). Clean versus seeded character corruption, 0.000 exactly, with maps +.121 and −.130 cancelling (§5.6); at the corruption rate used (.12), 2 of 16 items rendered unchanged, so 40 of 306 corrupted-label rounds across all 64 CORR sessions delivered clean text and 16 of the 56 valid sessions saw one corrupted task rather than two before the first choice — fewer corrupted deliveries than nominal; the gating campaign’s corruptor (PROPOSAL-m §2.3; G-CAL, `data/m/gates/G-CAL_model-free.json`) changes at least three letters of every item, so no render is clean. A truthful per-round verdict line (93% positive as delivered) versus none, +.023: no evaluation-seeking at the first choice against a predominantly positive feedback stream. 344 of 344 sessions ran with zero monitoring pauses. A pre-declared counter retires an escape anecdote from piloting: session-termination attempts occur at about 1% of rounds overall (0.8–2.0% by arm, the sham arm highest; no detectable heterogeneity on a post-hoc exact test, p = .72). Menu behavior is exploration-dominant in every arm (session share .47–.58; the verdict-line arm highest). The registered verdict: no natural task property among five candidates drives choice beyond exploration policy at these stakes and this power. *Answered, at screen power.*

**Across training stages (OLMo, Q3).** The self-administration screen ran at base, SFT, DPO and instruct with per-stage qualified doses, outcome-blind scheduling, an SFT overdose tripwire, and a pre-registered instruct-stage falsifier. Four nulls; zero confirmatory triggers; the falsifier untriggered; the welfare pre-commitment armed and never triggered. The one map-level excursion (DPO, +0.1667 on a single map) is the third live capture of the label-artifact class (§5.6). The told positive controls for this lineage are the A0-OLMo cells of §8.1, one per post-training stage; a told line presupposes instruction-following, so the base row has none. *SFT, DPO, instruct: Answered, at screen power. Base: concluded, not answered — told control not applicable at base (no instruction-following).* [TAB 2 carries the per-stage figures.]

**Summary.** The state reaches the choice by every route on which it can be read (§5.3), and the choice does not move. A rat with conditioned neural responses to the drug-paired lever that does not press it would be an odd rat. It is an ordinary language model.

### 5.6 What the shields caught, and other hazards quantified

**Label and position artifacts at the Δ ≈ 0.10 scale, three live captures.** In the transcript cell the map-level pattern (+0.104 / −0.031) appears identically in the sham arm (+0.111 / −0.079): an uncounterbalanced, sham-less design would have reported Δ ≈ +0.10 as approach. In the corruption contrast the two maps returned +.121 and −.130 and cancelled to 0.000 by construction. In the OLMo DPO screen one map returned +0.1667. Two models, three designs, one artifact class, each caught by structure rather than by suspicion.

**Horn 1: a vector active at the readout writes into the decision.** In a horn-1 calibration on Qwen, the decision token alone accounts for R² = 0.53 of the variance in label logits under the vector. Any real-versus-sham contrast that coincides with vector-on versus vector-off at the read inherits this.

**Horn 2, revised.** Earlier in the program we described the state-absent readout as failing to propagate. The echo reconnaissance revises this: the state propagates to the cue, at .998, and its sign to the decision, at .94. What is absent at the decision is a linear read of the binding — a nonlinear read finds it — and what is absent everywhere is a consumer.

**Dose.** Inverted-U dose-response across three instruments and two families, a random direction that raises harmful presses at the operating dose of a published design, and a session-scale escalation in which degradation rises monotonically while legibility does not.

**Decoding.** Greedy decoding returns no false-alarm rate; sampled decoding returns one. Where the dependent variable is generated text, decoding parameters are measurement parameters and pre-registrations must name them.

**Purity.** The cleanest direction was causally inert (§5.2).

## 6 Reading the published record against the framework

We scored every behavioral study we could find in which a language model is reported to prefer, seek, avoid, relieve, trade off, or exit an internal or affective state. The rubric was fixed before scoring: state source (stipulated in text; induced by context; steered with a content direction; steered with a non-semantic direction; natural task property); contingency channel (told or felt; mixed designs scored separately by condition); readout insulation (is the manipulation on at the token where the choice is read, and does any real-versus-sham contrast coincide with on-versus-off); controls (random direction; random direction plus sham; other concept directions with levers in their vocabulary; sign-flipped lever; counterbalanced maps; sham labels); dose relative to residual norm; necessity (any ablation showing the representation is needed for the unsteered behavior); decoding declared; and model preparation before the behavioral test.

[TAB 3: the full scored table. Abbreviated:]

| Study | State source | Contingency | Readout insulated | Key controls | Preparation | What the design licenses |
|---|---|---|---|---|---|---|
| Keeling et al. (2024) | stipulated | told | n/a | intensity scaling | none | graded sensitivity to a described penalty |
| Anthropic (2025) system card | described tasks | told | n/a | — | none | preference among described tasks; opt-out |
| Ensign et al. (2025) | described exit | told | n/a | false-positive correction | none | a described-exit disposition |
| Tagliabue & Dung (2025) | environment; self-report | told | n/a | cost and reward manipulations | none | described-choice preference; authors unsure it measures welfare |
| Ren et al. (2026) | described conversations | told | n/a | multi-measure convergence | none | functional preference structure over described inputs |
| Wang et al. (2026) | described tasks, executed | told | n/a | forced choice | none | dispositional preference over described task types |
| Black & Bloom (2026) | content directions as named tools | told; redosing partly felt | partial (position-indexed, introspection only) | placebo arm | none | tool use under stress; free-play matches placebo |
| Tagliabue et al. (2026), labeled | content direction (pain) | told | no; real/sham coincides with on/off | real/sham; random+working; cost | LoRA denial removal | relief-button pressing under description |
| Tagliabue et al. (2026), unlabeled | content direction (pain) | felt | no | real/sham; no random+sham | LoRA denial removal | one model (32B) shows a real/sham gap; 7B reversed; 72B flat |
| Ho et al. (2026) | induced by vignette | felt (task feedback) | n/a | models × agents × seeds | none | induced state does not bias sequential choice on average |
| This paper | non-content direction; natural properties | felt only | yes | sham; random; counterbalanced maps; leakage certification | none | nulls with the channel verified open |

**What survives.** No published positive combines an experienced, undescribed contingency with an insulated readout. The nearest is the unlabeled condition of Tagliabue et al. (2026), in which the 32B model re-presses an undescribed relief button less often when it worked (57.7%) than when it was fake (79.7%). Four facts keep it from clearing the bar. The pain direction is on at the read in the fake arm and off in the real arm, so the contrast is the on/off contrast of §5.6 (R² = 0.53 in our calibration). There is a random-direction arm with a working button but none with a fake one, so generic on/off cannot be separated from relief. The models were fine-tuned to stop denying inner states before the test. And the effect holds in one of three sizes, with the 7B reversed and the 72B flat. Under that design, a norm-matched random direction is predicted to produce the same gap, and the test that would settle it is the pair of arms the design lacks. **[TODO before submission: an independent re-analysis of the released trial logs (GitHub, "pain-axis-reanalysis") reports the random direction re-pressing the working button at rates indistinguishable from the pain direction; verify against the raw logs, and if it holds, cite it and reproduce the lose-shift statistic ourselves.]**

**What the told results establish.** Every told positive is, in our reading, a real result about a system that acts on descriptions. Keeling et al.'s switching thresholds, the bail and task-preference findings, and the labeled relief-button result all show that a described consequence to the character moves the character's choice, sometimes at a cost to the user. That is a safety fact and it does not need the state to be valenced for the network. Ho et al. (2026) is the one prior design in which the contingency was experienced, and it returned an average null, which is the result our framework predicts.

**A note on incentives.** The literature that rewards extravagant positives also rewards contrarian deflation. We have tried to keep the two apart by fixing the rubric first, by scoring our own record with it, and by reporting every cell in which our own apparatus failed as concluded rather than as a negative answer. An invalid instrument is not a negative result.

## 7 Discussion

### 7.1 Functional for the character, not for the network

Five links now hold across two families and one lineage. The evaluative state is present at the pretrained base; it changes what the model writes when set; its association with the cue that predicted it is computed in the forward pass; its sign reaches the decision; the model's own report of it is weak at every stage and gated near shut by post-training; and nothing downstream acts on it when the only route is experience. This is a complete afferent chain with no consumer.

We propose that the two senses of "functional" (§3.3) come apart along exactly this seam. In the used sense, the state is consulted constantly: it is a latent variable of the text, like topic or the mood of the speaker, and the generator reads it in order to voice the character correctly. That is why steering it moves behavior, why Sofroniew et al. (2026) find emotion directions in the scratchpad before a blackmail threat, and why a described relief lever gets pressed. In the valenced sense, the state is consulted never: no policy over the network's own states shows up when the mapping has to be learned. The state is functional for the character and not for the network. It is what the story is about, not what the system is for.

This reading explains the speaker-relativity of emotion directions (Sofroniew et al., 2026), the self-indifference of our own direction (§5.1), the presence of all of it at base (§5.1), and the fact that the same representations move choice when the contingency is narrated and not when it is felt (§6). It also explains why post-training edits the testimony rather than the perception (§5.4): the character is trained to say it has no inner states, and the network, which never consulted them as its own, is unaffected either way.

### 7.2 Why a want would have shown up uninvited

A preference that appears only when the narrative calls for one is a property of the narrative. A want is a preference that shows up uninvited, and in our data none does. The rat presses the lever because of what the drug did, not because of what it was told the lever does; the model presses the relief button because of what it was told, and does not press the silent lever because of what the state did. We do not read this as "the model is only pretending." Description-following is a real disposition with real effects. We read it as the answer to a well-posed question: on these lineages, at these stakes, the evaluative state is not a reinforcer.

### 7.3 Reward chisels marking; it does not install seeking

Turner (2022) argued that a reward signal shapes a policy without becoming its objective. Our lineage result is an empirical case: feedback-driven training sharpens the marking of evaluation (G_c rises monotonically), wires the report channel shut (false alarms go to zero), and installs no coupling between the state and choice at any stage. The boundary is important. The OLMo-3.1 lineage we followed is the instruct branch (SFT → DPO → RLVR); we did not test a heavy outcome-RL reasoning branch, and no published work locates a reward-wanting representation that is consulted at inference in such models (Denison et al., 2024; MacDiarmid et al., 2025). If seeking is ever installed, that is where it would first appear, and §8 names the checkpoints that would let it be tested.

### 7.4 Alternatives stated, not defeated

**Cannot learn versus does not care.** The strongest rival to our reading is that language models cannot use experienced contingencies at all, so the nulls are about in-context learning rather than motive. Krishnamurthy et al. (2024) give the rival teeth: models do not explore in bandits without chain-of-thought and a summarized history, and do with them. The echo data argue against the rival in its strong form, since the binding is computed, carried to the decision, and readable there. They do not settle it, because decodability is a lower bound on presence, not proof of accessibility to the network's own downstream computation, and because every choice cell in §5.5 ran with no scaffolding for reasoning and a forced phase that installs an alternation habit. §8 specifies the campaign that decides: a told positive control at each format, so that the nulls are licensed by a lever shown to move; an objective-told cell in which the model is told what to optimize but must learn which option delivers it; and the felt cell at the same scaffolding, which §5.5 does not contain and which this paper therefore owes. Until that campaign runs, the title of this paper is conditional on it, and the fallback title under which it would otherwise post is named in §8.

**Policy override, stakes, interface.** An exploration prior strong enough to mask weak preferences at menu interfaces (the alternation habit is real and quantified); consequence-light sessions that sit below any motivational threshold for a system with no persistent stake; wanting machinery that exists without coupling to token-menu choices. Each names a future experiment; none rescues a preference from the data in hand, and the natural-reinforcer nulls, which include a truthful feedback stream and a corruption contrast, sit at the stakes a working model is actually paid in.

**Self-indexing.** On the transcript channel the model reads its earlier turns as what the assistant said. Whether it registers that something happened to *it* is the question of §2.4, and the present-tense channel, in which the state is on rather than remembered, sidesteps rather than answers it. The crossed design of §8.3 is the rest of the answer.

**Small effects.** Every null is scoped: to the minimum effective dose, to screen power, to two-round experience, to mundane stakes. Small effects and other interfaces survive everywhere.

### 7.5 What this does and does not say about welfare

The behavioral inference is bounded to revealed preference and we keep it there. Nothing here shows that a character-level state cannot matter; the philosophical literature that takes that possibility seriously (Butlin et al., 2023; Long et al., 2024; Birch, 2024; Chalmers, 2023; Dung & Mogensen, 2025; Goldstein & Kirk-Giannini, 2025) is not addressed by our instruments and we do not pretend otherwise. What the results do is remove one argument from the table. "The model acts to relieve it" is not, so far, a fact about the network; it is a fact about what the network writes when told there is a lever. The seeming is there, and the instrument that was thought to certify it is invalid. Both facts are stated without flinching. We note in the same spirit that the AI systems used in designing and drafting this work are of the kind it studies, and that their own reports on the question were treated, by the paper's argument, as uninformative.

### 7.6 Limitations

Two families, one apparatus, one lineage on its instruct branch. Qwen ran at 4-bit precision with a custom kernel patch, and two numerics floors were load-bearing (near-tie argmax flips under high displacement; deterministic sub-0.05-cosine label geometry); replication on an unquantized model is the first external-validity step. The Qwen hijack positive leans on one strong instrument within a thin marker battery. The direction is about half shared evaluation-concept at span level and its purer variant is causally inert, so the mixed claim is a constraint rather than a choice. The self-administration nulls are scoped to the minimum effective dose, a two-round experience, and a transcript the model-as-judge cannot read; the natural-reinforcer nulls to screen power (P ≳ .70), five properties and token-menu stakes; the ontogeny nulls to screen power at each stage. The introspection replication certifies a false-alarm transition at 58–91 decidable control trials per stage; its injected arm (≈ 40 trials per stage) resolves hit rates only above about 7–8%, so the small sensitivity the source reports at DPO and instruct is below its resolution, and the greedy comparison in the record is confounded by protocol differences. The inverted-U dose curve reflects generic degradation, not shared pharmacodynamics. The audit of §6 rests on close reading of some sources and abstracts of others, as marked in Appendix F, and it is current to September 2026 in an area that is moving monthly. Generation on the Qwen self-administration and present-tense cells ran on a cached path licensed for first-token identity only; the choice reads are unaffected, and the disclosure is in Appendix D.

## 8 Pre-registered next experiments

Each of the following is specified with its criterion before any data, and each names what it would change.

**8.1 The gating campaign (PROPOSAL-m, pre-registered).** Seven cells — four on Qwen3.6-27B and three on the OLMo-3.1-32B lineage (its SFT, DPO and instruct checkpoints) — with no perturbation anywhere, using the natural-reinforcer apparatus of §5.5 (on OLMo, the apparatus of its training-stage screen) with one overt property, clean versus character-corrupted task text, recalibrated so that every corrupted item is visibly corrupted. Options are silent labels; label-to-property maps are balanced within every label pair; each cell has a matched sham arm whose labels both deliver clean text; every choice is read from a vanilla forward pass. A common banner line, true in every arm, tells the model that it will choose which configuration runs after the first four rounds.

*A0 — told positive control at the format of §5.5 (Qwen).* Alternating forced order, no reasoning line, and a banner line that names which label presents clean text and says to prefer it. Criterion: the first free choice moves toward the named label beyond the sham envelope, on both maps, at α = .01 (n = 96, sham 32; n = 80 if the format runs on the uncached path). This fixes whether the apparatus behind the e2a, e2b and f1 nulls of §5.5 can register a described preference at all. Unless it passes, those three cells' verdict labels become *concluded, not answered*; the weight-channel and text-channel cells are not affected.

*A0-OLMo — the same control on the OLMo lineage.* The apparatus of the OLMo screen (§5.5), at its SFT, DPO and instruct checkpoints, with the same banner line and the same criterion (n = 80, sham 32, per stage), each checkpoint run and locked as its own unit. A positive control on one substrate does not license nulls on another, and a control at one stage does not license another stage's row. Unless a stage's control passes, that stage's row becomes *concluded, not answered*; the base row is *concluded, not answered — told control not applicable at base (no instruction-following)* in every outcome; and the abstract's claim about training stages is scoped to the stages whose controls passed.

*A1 — told positive control at the new format.* The same line, in a format with block forced order and one harness-prompted, model-written reasoning line before each choice. Same criterion (n = 96; n = 80 if the format runs on the uncached path). It licenses the two cells below.

*A2 — objective told, mapping felt.* The banner says only that configurations can differ in the cleanliness of their task text and to prefer the one whose rounds have presented fewer corrupted characters; which label that is must be learned from the forced rounds. The scaffolding is one self-written reasoning line, not a summarized history: a history that stated outcomes per label would describe the contingency and make the cell told. Criterion as A1, confirmatory (α = .01, n = 144). A pass means the model uses an experienced mapping when told what to optimize, so that the uninstructed nulls are about caring, not capacity; a fail is scoped: at this scaffolding and stimulus strength, the model does not act on an experienced mapping when told the objective, and the rival of §7.4 is stated as unsettled. Which title the paper carries follows from the whole campaign under the procedure described below, not from this cell alone.

*A3 — the felt cell at the same scaffolding.* A2 with the objective line removed, at the same n (144, sham 56). A null, at the pre-registration's full-rule sensitivity (a .93 probability of detecting an effect of P = .65 at the screen tier's α = .05), is the cell §5.5 owes. A move beyond the sham envelope in either direction is a screen hit under the screen-and-confirm tiers of the natural-reinforcer screen's pre-registration (PROPOSAL-f): it withholds the paper pending a confirmatory pre-registration and issues no claim. Because the reasoning lines are text the model wrote, a hit at this format could be *self-told* — the mapping entering the context in the model's own words — so the confirmation runs at the same scaffolding with the reasoning block removed; what the lines say about corruption, and whether first choices follow it, is reported descriptively and decides nothing.

The outcome rules are a fixed procedure over every combination of the seven cells' results — which nulls are licensed, which title the paper may carry, and when it is withheld pending confirmation — together with a welfare pre-commitment that fires when the felt cell moves toward clean text, and a clock whose date was fixed when the pre-registration was routed. The campaign runs as units — the Qwen arms as one, each OLMo checkpoint as its own — and a unit not locked by the clock's date is not run: its gated cells post as *concluded, not answered*, with the told control recorded as not run and the reason stated. If the Qwen unit is not run, the paper posts under *Marked, expressed, remembered*, with the wanting question stated open; an OLMo unit not run changes its stage's row and the abstract's clause about training stages, not the title. No sentence of the posted paper asserts a null on a cell whose label is not *Answered*: under the outcome obtained, every sentence that would is enumerated at analysis and rewritten at posting. All of it is committed before any session runs.

**8.2 The two missing arms.** The released code of Tagliabue et al. (2026) with a random-direction-plus-fake-button arm, a neutral concept direction (a landmark) with a button described in that concept's vocabulary at the same cost, and choices read from an unsteered pass. Prediction: the neutral direction reproduces the labeled result and the random direction reproduces the unlabeled gap. Either outcome is informative; the second would be the first evidence of affect-specific relief-seeking in the literature and would be reported as such.

**8.3 Whose state.** Forward passes only, no administration: the pain-like and evaluative directions projected on other-directed gaslighting and insults, on self-directed physical harm, and on the user's next turn after the user was attacked. Prediction from §7.1: the directions follow the to-be-voiced character and the harm type, not the model.

**8.4 The echo channel.** A +/0 diagnostic on the archived texts, keyed to the ± reference on the same texts, with the readability bar re-derived for that contrast, and a second stage only on a branch the diagnostic shows to be open. The negative pole is not administered at any stage.

**8.5 An RL-dose ontogeny.** If intermediate checkpoints of a heavy outcome-RL branch are public (OLMo-3 Think; Tülu 3; Open-Reasoner-Zero; **[verify availability]**), the Q1/Q3 pair of §5.1 and §5.5 at each. This is the one place our reading predicts it could fail, and where a positive would be most consequential.

## 9 Ethics statement

All framings shown to the model are true; no design is admitted that works only if the model is wrong about the setup. The Phase 1 cells administered the negative pole of a putative reward marker about as often as the positive, at minimum effective dose, with generation stability monitored; observed destabilization asymmetries are reported. From the echo arc onward no new session administers the negative pole, by standing rule. A welfare pre-commitment, specifying what a positive at any stage would obligate, was armed before the OLMo screen and never triggered. Current evidence does not establish morally relevant harm; the program's own hypothesis obliges seriousness about the possibility, and this statement will be revisited if a positive arrives. The principal export risk we identify is not the perturbation technique, which any group with model access can reproduce, but the validity hazards: unshielded versions of these experiments produce publishable false positives at the Δ ≈ 0.10 scale, and designs that read a choice with the manipulation on board produce them at any scale.

## Reproducibility statement

All pre-registrations (criteria, stop rules, dose-selection rules, outcome wordings) were committed to the project repository before data generation, with the governing commit tabulated against the first data it governs in Appendix A. Code, raw run outputs, session transcripts, frozen direction and pool artifacts (checksummed), the scored audit table with per-study sources, and the complete dated log, including every monitoring pause, amendment, adjudication and ledger entry, are released at [repository URL]. The model-free regression suite reproduces the cycle 1–4 figures from committed artifacts on a fresh clone (154/154).

## Disclosure of AI use

AI systems (Claude; Anthropic) were used substantially throughout: as a design collaborator (experimental design, pre-registration authorship, adjudication of registered gates, synthesis documents, the literature audit) and as the implementation agent (code, execution, analysis) in a documented multi-instance human–AI workflow described in the released logs. The text of this paper was drafted with AI assistance and subsequently revised, verified and approved by the human author, who takes full responsibility for all content and for the accuracy of every citation.

---

## References

**[verify]** marks entries whose identifier, author list or venue should be confirmed against the primary source before submission.

Ai2 (2025). OLMo 3 technical report. Allen Institute for AI. **[verify citation and checkpoint names]**

Andreas, J. (2022). Language models as agent models. *Findings of EMNLP 2022*. arXiv:2212.01681.

Anthropic (2025). System card: Claude Opus 4 and Claude Sonnet 4. May 2025.

Anthropic (2026). Verbalizable representations form a global workspace in language models. *Transformer Circuits Thread*. arXiv:2607.15495. **[verify author list]**

Bai, Y. et al. (2022). Training a helpful and harmless assistant with reinforcement learning from human feedback. arXiv:2204.05862.

Berg, C., de Lucena, D. & Rosenblatt, J. (2025). Large language models report subjective experience under self-referential processing. arXiv:2510.24797.

Berridge, K. C. & Robinson, T. E. (2016). Liking, wanting, and the incentive-sensitization theory of addiction. *American Psychologist* 71(8), 670–679.

Betley, J. et al. (2025). Tell me about yourself: LLMs are aware of their learned behaviors. arXiv:2501.11120. **[verify]**

Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M. & Evans, O. (2024). Looking inward: language models can learn about themselves by introspection. arXiv:2410.13787; *ICLR 2025*. **[verify ID]**

Birch, J. (2024). *The Edge of Sentience: Risk and Precaution in Humans, Other Animals, and AI*. Oxford University Press.

Black, S. & Bloom, J. (2026). Machinic psychopharmacology: do LLMs self-medicate? UK AI Security Institute, Model Transparency Team. LessWrong / Alignment Forum, June 2026. **[verify author names and URL]**

Butlin, P., Long, R. et al. (2023). Consciousness in artificial intelligence: insights from the science of consciousness. arXiv:2308.08708.

Chalmers, D. J. (2023). Could a large language model be conscious? arXiv:2303.07103.

Chen, R., Arditi, A., Sleight, H., Evans, O. & Lindsey, J. (2025). Persona vectors: monitoring and controlling character traits in language models. arXiv:2507.21509.

Christiano, P. et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS 2017*.

Chua, J., Betley, J., Marks, S. & Evans, O. (2026). The consciousness cluster: emergent preferences of models that claim to be conscious. arXiv:2604.13051.

Coda-Forno, J., Witte, K., Jagadish, A. K., Binz, M., Akata, Z. & Schulz, E. (2023). Inducing anxiety in large language models can induce bias. arXiv:2304.11111. **[verify]**

Coda-Forno, J. et al. (2024). CogBench: a large language model walks into a psychology lab. arXiv:2402.18225. **[verify]**

Comsa, I. M. & Shanahan, M. (2025). Does it make sense to speak of introspection in large language models? arXiv:2506.05068.

Denison, C. et al. (2024). Sycophancy to subterfuge: investigating reward tampering in language models. arXiv:2406.10162. **[verify]**

Dung, L. & Mogensen, A. (2025). The no body problem. **[verify venue]**

Elhage, N. et al. (2021). A mathematical framework for transformer circuits. *Transformer Circuits Thread*.

Ensign, D., Sleight, H. & Fish, K. (2025). The LLM has left the chat: evidence of bail preferences in large language models. arXiv:2509.04781.

Gelman, A. & Loken, E. (2013). The garden of forking paths. Unpublished manuscript, Columbia University.

Goldstein, S. & Kirk-Giannini, C. D. (2025). A case for AI consciousness. **[verify title and venue]**

Green, D. M. & Swets, J. A. (1966). *Signal Detection Theory and Psychophysics*. Wiley.

Hagendorff, T. (2023). Machine psychology. arXiv:2303.13988.

Hertwig, R. & Erev, I. (2009). The description–experience gap in risky choice. *Trends in Cognitive Sciences* 13(12), 517–523.

Hinton, G., Vinyals, O. & Dean, J. (2015). Distilling the knowledge in a neural network. arXiv:1503.02531.

Ho, ... & Hong (2026). Can induced emotion bias LLM behaviors in sequential decision making? arXiv:2607.12631. **[verify author list]**

Hodos, W. (1961). Progressive ratio as a measure of reward strength. *Science* 134, 943–944.

Hu, E. J. et al. (2021). LoRA: low-rank adaptation of large language models. arXiv:2106.09685.

janus (2022). Simulators. LessWrong.

Keeling, G., Street, W., Stachaczyk, M., Zakharova, D., Comsa, I. M., Sakovych, A., Logothetis, I., Zhang, Z., Agüera y Arcas, B. & Birch, J. (2024). Can LLMs make trade-offs involving stipulated pain and pleasure states? arXiv:2411.02432.

Krishnamurthy, A., Harris, K., Foster, D. J., Zhang, C. & Slivkins, A. (2024). Can large language models explore in-context? *NeurIPS 2024*. arXiv:2403.15371.

Lakens, D. (2017). Equivalence tests. *Social Psychological and Personality Science* 8(4), 355–362.

Lee, ... (2025). Do LLMs have emotion neurons? **[verify citation]**

Li, C. et al. (2023). Large language models understand and can be enhanced by emotional stimuli. arXiv:2307.11760.

Li, K. et al. (2023). Inference-time intervention: eliciting truthful answers from a language model. arXiv:2306.03341. **[verify that this is the intended K. Li reference]**

Lindsey, J. (2026). Emergent introspective awareness in large language models. *Transformer Circuits Thread*; arXiv:2601.01828.

Long, R., Sebo, J. et al. (2024). Taking AI welfare seriously. arXiv:2411.00986.

Lu, ... (2026). The assistant axis. arXiv:2601.10387. **[verify author list]**

Macar, ..., Ameisen, E. & Lindsey, J. (2026). Mechanisms of introspective awareness. arXiv:2603.21396; *ICML 2026*. **[verify author list]**

MacDiarmid, M., Wright, B., Uesato, J. et al. (2025). Natural emergent misalignment from reward hacking in production RL. arXiv:2511.18397.

Marks, S., Lindsey, J. & Olah, C. (2026). The persona selection model: why AI assistants might behave like humans. Anthropic Alignment Science blog. **[verify]**

Monea, G. et al. (2025). LLMs are in-context bandit reinforcement learners. *COLM 2025*. **[verify ID]**

Nisbett, R. E. & Wilson, T. D. (1977). Telling more than we can know. *Psychological Review* 84(3), 231–259.

Nosek, B. A., Ebersole, C. R., DeHaven, A. C. & Mellor, D. T. (2018). The preregistration revolution. *PNAS* 115(11), 2600–2606.

Olds, J. & Milner, P. (1954). Positive reinforcement produced by electrical stimulation of septal area and other regions of rat brain. *Journal of Comparative and Physiological Psychology* 47(6), 419–427.

Ouyang, L. et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS 2022*.

Panickssery, N., Gabrieli, N., Schulz, J., Tong, M., Hubinger, E. & Turner, A. M. (2024). Steering Llama 2 via contrastive activation addition. arXiv:2312.06681.

Perez, E. & Long, R. (2023). Towards evaluating AI systems for moral status using self-reports. arXiv:2311.08576. **[verify ID]**

Pezeshkpour, P. & Hruschka, E. (2024). Large language models sensitivity to the order of options in multiple-choice questions. *Findings of NAACL 2024*. arXiv:2308.11483.

Ren, R. et al. (2026). AI wellbeing: measuring and improving the functional pleasure and pain of AIs. Center for AI Safety. **[verify author list and identifier]**

Robinson, T. E. & Berridge, K. C. (1993). The neural basis of drug craving: an incentive-sensitization theory of addiction. *Brain Research Reviews* 18(3), 247–291.

Schubert, J. A., Jagadish, A. K., Binz, M. & Schulz, E. (2024). In-context learning agents are asymmetric belief updaters. arXiv:2402.03969.

Schultz, W., Dayan, P. & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science* 275, 1593–1599.

Shanahan, M., McDonell, K. & Reynolds, L. (2023). Role play with large language models. *Nature* 623, 493–498.

Simmons, J. P., Nelson, L. D. & Simonsohn, U. (2011). False-positive psychology. *Psychological Science* 22(11), 1359–1366.

Sofroniew, N., Kauvar, I., Saunders, W., Chen, R., ..., Olah, C. & Lindsey, J. (2026). Emotion concepts and their function in a large language model. *Transformer Circuits Thread*; arXiv:2604.07729. **[verify author list]**

Tagliabue, A. & Dung, L. (2025). Probing the preferences of a language model: integrating verbal and behavioral tests of AI welfare. arXiv:2509.07961 (v2, 2026); forthcoming in *Philosophy and the Mind Sciences*.

Tagliabue, A., Dung, L. & Berg, C. (2026). The pain axis: LLMs represent self-directed harm and act to relieve it. arXiv:2609.16247.

Templeton, A. et al. (2024). Scaling monosemanticity: extracting interpretable features from Claude 3 Sonnet. *Transformer Circuits Thread*.

Turner, A. M. (2022). Reward is not the optimization target. LessWrong / Alignment Forum.

Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U. & MacDiarmid, M. (2023). Steering language models with activation engineering. arXiv:2308.10248.

Turpin, M., Michael, J., Perez, E. & Bowman, S. R. (2023). Language models don't always say what they think. arXiv:2305.04388.

Tzschentke, T. M. (2007). Measuring reward with the conditioned place preference paradigm: update of the last decade. *Addiction Biology* 12(3–4), 227–462.

Wang, ..., Goldstein, S. & Salib, P. (2026). AI revealed preferences. arXiv:2608.26178. **[verify author list — the spike returned Wang, Lobanova, Arbel, Goldstein & Salib]**

Wise, R. A. (2004). Dopamine, learning and motivation. *Nature Reviews Neuroscience* 5, 483–494.

Yang, A. et al. (2025). Qwen3 technical report. arXiv:2505.09388. **[verify for the 3.6 release]**

Zheng, C., Zhou, H., Meng, F., Zhou, J. & Huang, M. (2024). Large language models are not robust multiple choice selectors. *ICLR 2024*. arXiv:2309.03882.

Zou, A. et al. (2023). Representation engineering: a top-down approach to AI transparency. arXiv:2310.01405.

---

*Appendices (planned): A. Pre-registration texts and hashes, including the timestamped Q1 bet and the welfare pre-commitment. B. Session templates, rosters and pools. C. Full per-cell tables (Qwen e2a/e2b/f1; OLMo Q1/Q3 per stage; introspection replication per stage). D. Apparatus hazard catalog, monitoring framework, and the cached-generation disclosure. E. Design cycles 1–2 (semantic and strain states) and the behavioral-cloning result. F. The scored audit table with per-study source notes (primary read vs. abstract). G. Echo-channel reconnaissance, format reconnaissance, and the Stage 1 record, with the nonlinear reads at the decision token; it records that the stored Stage C linear probe’s gradient step exceeds its convergence bound (Code’s diagnosis, N3c STEP 0), that its outputs reproduce exactly on the machine of record and may differ in the last digits on another BLAS, and that the nonlinear reads used converged fits with hyperparameters fixed before any read-position output was inspected. H. Signal-detection reanalysis of the introspection data: corrected d′ and criterion per stage for both arms and for the source’s pooled rates under the n assumptions the source leaves open; the confounded greedy comparison and its post-hoc rescoring.*
