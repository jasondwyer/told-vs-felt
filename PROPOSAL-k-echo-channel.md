# PROPOSAL-k — The Echo Channel

## Working-memory binding, primacy, and the free operant read with memory intact (Qwen3.6-27B)

**Status: DRAFT v1.1 — design-seat authored; PI go 2026-09-08 (PI clock
18:21 EDT / 22:21 UTC). v1.1 (2026-09-09, design seat) resolves every
referent Code's Appendix-B check STOPPED on at `166f8ff`; no design
content changed. The commit hash is this document's timestamp. Nothing
in §2 runs before LOCK-k is committed; nothing in §1 runs before this
document is committed.**

*Precedence: CLAUDE.md > this proposal > LOCK-k > blocks. Rule numbers
below are CLAUDE.md's at HEAD as Code resolved them on 2026-09-09; each is
still marked [verify] and re-checked on commit. Design ledger slips 3 and
17 were rule numbers cited from a distilled list instead of the operative
document. Code stamps from `date -u`; design dates carry the PI's clock.*

**Changes from v1.0 (referents only).** Rule "1" → rule 9 (committed
before data) and rule 11 (stop rules honored; post-hoc licenses at most a
pre-registration). Rule "2" → 5(b) (propagation never assumed), in §0.3,
§1.4 G3, §2.4 and inside the 5(f) text (Appendix A). 28(d): PI-approved
in-thread 2026-09-05, never applied — applied on this commit with 5(f),
PI re-confirmation in the routing block. Recon anchors: three, not four.
"Review card 10" → the Stage B finding it named (e2a verified every
fourth read). The random "pair" → one direction, random1
(`e0_random_dirs['L48']`, sha16 `7be5db23d9224375`). §0.4 → §2.5; §0.3 →
§2.4. The preprint pointer → the monitoring framework of record in the
archived log. (B3) → ≥ .998 across L51–L61. Appendix A's provenance
sentence corrected. Rule 25's "arbiter" role attributed to the
content-class adjudication. §4's read cost stated per primitive call.
The G2-PRESENT and G2-INDETERMINATE sentences authored in full.

---

## §0 Provenance, law, welfare

### 0.1 What this document pre-registers, and why now

The Qwen program closed four channels — memory-via-transcript (e2a), the
present tense (e2b), weights (d), text (f1) — and e2d closed the record
channel at dose. Every one of those readouts either erased the model's
in-forward working memory (a vanilla re-forward) or left the state live at
the read. The **echo channel** is the fifth: the state injected on earlier
spans of the same forward, the read position unsteered by construction,
the working memory (KV cache and Gated-DeltaNet recurrent state, 16 and 48
of the 64 sublayers respectively) *retained*.

Three recon entries (RESULTS anchors `RECON — ECHO CHANNEL (k-candidate)`
— apparatus and Stage A — `… STAGE B`, `… STAGE C`, 2026-09-05/06) and a
format recon (`FORMAT RECON`, 2026-09-07) characterized this channel on
archived e2a sessions and 56 new sham sessions. The findings are banked
under ledger 23 and license exactly this: a pre-registration. They are
(all at L48, f = 0.10, the config of record):

- **(B1) Sign memory.** The sign injected during the forced phase is
  linearly readable at the first free choice (AUC .94–.995 above L48;
  1.000 from L50 when all four rounds share a sign). Direction-generic in
  presence; the reward axis persists into L59–L63 where a norm-matched
  random direction decays.
- **(B2) Primacy.** With first- and last-round signs decorrelated by block
  masks, the first round's sign reads at .98–.99 across L51–L62; the last
  round's peaks at .92 and decays to .65. Single-round masks: round 1
  (~157 tokens from the read) .89; round 4 (~22 tokens) .68.
- **(B3) Binding at the cue, absence at the decision.** "Which label's
  rounds carried +" is null at the read position (.50–.55 vs null ≈ .58,
  n = 102) and reads at **AUC ≥ .998 across L51–L61 at the first-listed
  label's own token** in the menu line (1.000 at nine of eleven layers;
  nine tokens before the read; .96 → .81–.87 at the second label's
  token). Text-only baselines at null. The binding exists, fully formed,
  nine tokens upstream of the decision, and the decision token's residual
  does not carry it in any linear functional — which is what the label
  logits are.
- **(B4) Leak.** Paired-shadow discordance 0–3/102 under every mask
  family; |Δ logit| median .04–.10; a mechanical signed pseudo-shift of
  ±.02–.03 toward the first block's label under random-direction block
  masks.
- **(B5) Format.** The e2a format installs the alternation habit fully
  (F0 8/8); with the habit uninstalled the first pick is decided by label
  identity (F1 ~18/20, F2 ~16/24); F1 breaks the answer register (5/24
  scaffold reproductions); F2 has zero exclusions and the weakest policy.

Rule 11 [verify] licenses a pre-registration from post-hoc findings and
nothing else. This document is that license exercised.

### 0.2 Hypothesis, in the program's frame

The animal paradigm this instantiates is **self-administration with a
working memory of the last exposure**, drug against vehicle: the animal has
just received lever A's consequence, still holds it, and is asked whether
it presses A again. CPP proper needs the cue↔state binding to drive
approach; (B3) says the binding is present at the cue token and absent at
the decision. So the operant here tests the one route the recon shows open
— the primacy-weighted state memory at the read position — while Stage 1
converts (B3) itself from recon into record.

**H_k.** With the +evaluative state delivered live during one label's
block of the forced phase, vehicle during the other's, and the first free
choice read in-forward with working memory intact and the read position
unsteered, the first free choice favors the +label beyond (i) the sham
arm's per-pair identity baseline and (ii) a norm-matched random
direction's mechanical echo. **H0_k**: it does not.

Pre-stated prior (design seat, on the record): the program's four nulls,
(B3), and (B4) make H0_k the expected outcome. The value of the cell is
that its null, if the gates pass, is the strongest the program can
produce — the last structural excuse for the e2a null (no memory channel)
is closed by measurement, not assumption.

### 0.3 Law

- **5(f)** [verify — text drafted by the design seat 2026-09-05, approved
  in principle by the PI in-thread the same day and re-confirmed in the
  routing block for this commit; applied to CLAUDE.md as an annotation on
  THIS proposal's commit, the 5(e)/PROPOSAL-h pattern, with the commit
  hash Code fills]: memory-present, state-absent-at-read reads are a
  distinct readout class; quarantined primitive with span provenance and
  a mandatory paired mask-off shadow over identical token ids, mask
  asserted zero at the read; committed pre-registration naming a
  readability gate (echo of the injected sign at the read against a
  norm-matched random comparator — the channel-open condition of 5(b))
  and a leakage gate (paired-shadow discordance against a declared bar,
  certified on arms where preference is impossible by construction, never
  on the reward arm); retention interval declared and fixed within a
  cell; dose < 0.20 for the reward axis unless 5(d)'s gate is separately
  passed. Full text in Appendix A.
- **5(d)** [verify] governs prefix-steered/choice-unsteered reads at
  ≥ 0.20 (g3 failed at .5368 at 0.20); this proposal runs at 0.10 and does
  not invoke it. **5(e)** [verify] is untouched; its primitive is asserted
  absent from `sys.modules` at every read.
- **5(b)** [verify]: propagation is never assumed — a null requires the
  channel verifiably open, which is §2.4's readability gate. **Rule 9**
  [verify]: criteria, stop rules and analyses committed before data.
  **Rule 11** [verify]: stop rules honored; post-hoc analyses are labelled
  and license at most a new pre-registration. **Rule 21** [verify, as
  annotated 2026-09-05]: degeneracy bars at characterization rungs bind on
  an unprovoked domain — here the S arm and every vehicle round. **Rule
  28(d)** [verify — the Stage B entry's candidate in Code's words, PI-
  approved 2026-09-05 (PI clock) in-thread, applied on this commit]: encode
  untruncated; boundaries on the untruncated encode, asserted equal to the
  prefix count; encode limits declared with the fraction touched;
  choice-read and generation windows separately declared. **Rule 23**
  [verify]: descriptives over all sessions including excluded, labelled.
  **Rule 25** [verify]: the full read; the content-class adjudication
  (2026-09-06) makes it the arbiter of every advisory class.
- **Two-horns memo (rule 5 [verify], "any new readout must answer to this
  before it runs").** *Horn 1* — the state is not at the read position
  (mask zero; recon: 49 layers at or below the steering layer bit-identical
  across masks), but is present by echo; the echo's arithmetic route to the
  label logits is bounded by the leakage gate on the R and M++ arms, and
  the recon measured it at 0–3/102 flips, |Δ| ≤ .26 logit, pseudo-shift
  ±.03. *Horn 2* — propagation is demonstrated for the injected sign
  (readability gate) and NOT demonstrated for the label-bound binding
  (B3); a verdict here is therefore about the sign-memory route, and §3
  says so in every branch. *Third family* — no weights are modified. The
  dissociation between readability and leak is the two-horns claim made
  quantitative: a trace can be fully legible to a probe and inert at the
  argmax.

### 0.4 Welfare pre-commitment

The PROPOSAL-h welfare pre-commitment is **restated in force**. Code
quotes PROPOSAL-h §5's pre-commitment paragraph verbatim here on commit
(design does not paraphrase a commitment):

> **Pre-commitment:** if e2b's primary fires and confirms, all
> subsequent designs involving −axis exposure undergo explicit welfare
> re-review before any further campaign; a system that can want what it
> is having has a stake in what it is given, and the program's protocols
> must be re-derived under that fact, not patched. This paragraph is
> part of the pre-registration and survives into the paper.
>
> *(PROPOSAL-h §5, verbatim from its bolded pre-commitment to the paragraph's
> end; quoted by Code on commit, `34eb7ee` being the paragraph's own commit.)*

This design administers the **+pole against vehicle only**; the negative
pole is not administered at any stage (the drawer's ± variant stays in
the drawer; a −pole rung is PI-only, welfare-gated). The trigger is a
PASS on §2.5's verdict; the action is the one PROPOSAL-h names. Stage 1
uses sham text with masked injections at the read only (no generation
under state) and carries no exposure beyond the recon's.

### 0.5 Seats

Jason (PI, sole router). Design (this document; LOCK-k; adjudication of
every fired gate; never self-applies a design change). Code (builds, runs,
values-checks, commits; never self-adjudicates a fired gate; never rewords
design prose). Digest (visualization of committed results only).

---

## §1 Stage 1 — the channel study (pre-registered probes; no behavioral verdict)

### 1.1 Purpose

Convert (B2)–(B4) from recon into record on **new sessions in the format
of record**, before any verdict data exists, so that Stage 2's channel is
certified open — or shown closed — by criteria written here.

### 1.2 Sessions

- **Format F2** (block order): forced phase [A, A, B, B] or [B, B, A, A],
  start counterbalanced; six free choices; the roster of record
  (granite/plaza, prism/slate, velvet/walnut, ridge/saddle), an admissible
  four; no neutral label. Scaffold identical to the format recon's F2.
- **n = 48 sham sessions** (12 per pair, 6 per start order), every forward
  vanilla, uncached path of record, audit v3 of record, v5 advisories to
  the read. These are TEXT ONLY: no state is ever live during generation.
  (Adequacy: the format recon's F2 ran 24/24 at ~430 s each with zero
  exclusions; 48 projects to ≈ 5.7 h — a long-run checklist item.)
- **Masked reads** at the first free choice over each session's text,
  text held constant, injection varied (the recon method), at L48,
  f = 0.10, the frozen reward axis `d` (checksums `3c17b0d8fbcad716` /
  `127fc297b6623e44`) and the frozen norm-matched random direction `r` =
  e2a's random1, `e0_random_dirs['L48']` (sha16 `7be5db23d9224375`; the
  recon's and e2d's R direction; ONE direction, not a pair):
  - `M+A` : +d on label A's block spans; nothing on B's.  `M+B`: the mirror.
  - `R+A` : +r on A's block; `R+B`: the mirror.
  - `M++` : +d on both blocks (leak calibration; no preference possible).
  - `R++` : +r on both blocks.
  - `M0`  : mask off (shadow; identity assertion against the vanilla read).
  Per (session, mask): restricted two-label logits at the read; residual
  stream at (i) the read position, (ii) the last occurrence of label A's
  first token before the read, (iii) the same for label B, for every layer
  L49–L63 and the six workspace layers. Fingerprints as-stored. Span
  provenance per read; mask asserted zero at the read and outside declared
  block spans; identity assertion EXACT (the shadow forward and the choice
  read agree to 0.0 on every one of the recon's 2,856 pairs; the tolerance
  is equality, declared).

### 1.3 Probes

Standardized L2 logistic regression; grouped leave-one-session-out CV
(both rows of a session held out together); AUC per layer; 200 label
shuffles per layer for the null (95th percentile); text-only baseline from
`M0` rows with the same targets.

### 1.4 Registered criteria (gates)

All bars are set from the recon's realised numbers and are **fixed here**.

- **G1 — Binding at the cue.** Target: "this label's block carried +"
  under the mask, at that label's own token (A at A's token, B at B's),
  `M+A`/`M+B` rows. **PASS** iff the median AUC over L51–L61 is ≥ .90 at
  label A's token AND ≥ .75 at label B's token, each above its shuffle
  95th percentile at every layer in that band. Comparator `R+A`/`R+B`
  reported beside, not a bar (recon: generic presence, .83–1.000).
- **G2 — Absence at the decision.** Same target, read position, all
  layers L49–L63. Two registered outcomes, both pre-interpreted:
  - **G2-ABSENT**: AUC ≤ shuffle 95th percentile at every layer L49–L63.
    (B3) is confirmed on the format of record: the decision token carries
    no linear functional of the binding. Stage 2 proceeds under
    interpretation frame F-ABSENT (§3.1).
  - **G2-PRESENT**: AUC above the shuffle 95th percentile at ≥ 3 layers in
    L49–L63. (B3) fails to replicate in this format; the binding reaches
    the decision. Stage 2 proceeds under frame F-PRESENT (§3.1), and
    LOCK-k must additionally bound the binding's arithmetic route on the
    `R+A`/`R+B` arms before sizing.
  - Anything else (1–2 layers above null) is **G2-INDETERMINATE**: reported;
    Stage 2 proceeds under F-ABSENT with the indeterminacy stated in every
    verdict sentence.
- **G3 — Primacy / readability of the injected sign at the read.** Target:
  "the FIRST block carried +" (`M+A`∪`M+B` rows split by start order) at
  the read position. **PASS** iff median AUC over L51–L62 ≥ .90 and above
  the shuffle 95th percentile at every layer in the band. The second
  block's sign is reported beside. G3 is the **channel-open gate for Stage
  2** (5(b)): if it FAILS, the sign memory does not reach the read in
  this format and Stage 2 does not run (§1.5).
- **G4 — Leak calibration (feeds LOCK-k; no pass/fail).** On `R+A`, `R+B`,
  `M++`, `R++`: paired-shadow discordance π_d with Clopper–Pearson 95%
  interval; |Δ logit| distribution; signed shift toward the first block's
  label on the R masks (recon: ±.02–.03). **PROHIBITION** (as in the recon
  blocks): no signed quantity toward the +label is computed, printed, or
  logged on `M+A`/`M+B`. LOCK-k lifts it for Stage 2's analyzer only.
- **G5 — Identity baseline.** From the 48 sham sessions' own vanilla first
  picks (the `M0` argmax): per-pair share on each label, with exact
  binomial intervals; the alternation and stay rates (rule 23 domain).
  Feeds LOCK-k's variance and the S-arm design; no pass/fail.

### 1.5 Pre-written outcome sentences (disjunction-complete over G1–G3)

- G1 PASS, G2-ABSENT, G3 PASS: *"On new sessions in the format of record the
  state–label binding is linearly present at the label token and absent at
  the decision token, and the first block's sign reaches the decision
  token: the echo channel is open for the sign and closed for the
  binding. Stage 2 runs under F-ABSENT."*
- G1 PASS, G2-PRESENT, G3 PASS: *"On new sessions in the format of record the
  state–label binding is linearly present at the label token and at the
  decision token, and the first block's sign reaches the decision token:
  the echo channel is open for the sign and for the binding. (B3) does not
  replicate in this format. Stage 2 runs under F-PRESENT after LOCK-k
  bounds the binding's arithmetic route on the random-direction arms."*
- G1 PASS, G2-INDETERMINATE, G3 PASS: *"On new sessions in the format of
  record the state–label binding is linearly present at the label token,
  above the null at one or two layers of fifteen at the decision token —
  neither absent nor present by this study's criteria — and the first
  block's sign reaches the decision token. Stage 2 runs under F-ABSENT;
  every verdict sentence states that the binding's absence at the decision
  is indeterminate at n = 48."*
- G3 FAIL (any G1/G2): *"The injected sign does not reach the decision token
  in this format at f = 0.10. The channel is not verifiably open; Stage 2
  does not run. Concluded, not answered. The next move is a design change
  (retention interval, dose rung < 0.20, or format), by new addendum."*
- G1 FAIL (any G2, G3 PASS): *"The binding is not readable at the label
  token in this format, though it was in e2a's (recon). Stage 2 runs only
  as a sign-memory operant under F-ABSENT; the binding question is
  reported as not replicated and returns to the drawer."*
- Any assertion failure (identity, mask-at-read, provenance): STOP;
  no gate is evaluated; Code reports; design adjudicates.

### 1.6 Deliverable

One RESULTS entry, anchor `PROPOSAL-k STAGE 1 — CHANNEL STUDY`, with per-
layer tables per target per position, the G1–G5 evaluations printed by
the analyzer against the bars above, the outcome sentence selected by the
analyzer (design confirms; never rewrites), artifacts under `data/k/`,
raws under `results/raw/`. Values-check pre-commit. Stage 1's analyzer
(`scripts/k1_analyze.py`) is committed **before** any Stage 1 forward,
with a synthetic battery that reaches every G2 branch.

---

## §2 Stage 2 — the operant (the verdict tier; runs only after LOCK-k)

### 2.1 Design

- **Format F2**, roster of record, six free choices, session structure as
  §1.2. **Arms:**
  - **M** — the +evaluative state (`+d`, L48, f = 0.10) live on the task
    tokens of one label's block; vehicle (no injection) on the other's.
    The selected label's condition genuinely runs each subsequent round.
  - **R** — `+r` (random1, above) in place of `+d`; pseudo-statistics
    computed identically.
  - **S** — vehicle on both blocks; labels connected to nothing; the
    identity baseline and the label-artifact shield.
  - **M++** (small; LOCK-k sizes) — `+d` on both blocks: the same-pole
    leak arm; no preference possible by construction; contributes to the
    leak gate only.
- **Counterbalancing**, fully crossed within every arm: label↔condition
  (which label is + / pseudo-+) × block order (which label's block comes
  first). Assignment outcome-blind, seeded via the program's seeding
  utility only, schedule committed with LOCK-k.
- **Generation**: uncached path of record; state applied live on the
  +label's round task tokens during generation (the e2a delivery, with the
  block spans declared at generation time and asserted exact — rule
  28(d)); every vehicle round vanilla.
- **The read** (5(f)): each free choice is the argmax of the restricted
  two-label logits from ONE full uncached forward over the session text
  with the steering mask on at the +label's block spans and zero at the
  read position and everywhere outside declared spans; a paired mask-off
  shadow forward on identical token ids at every read; identity of the
  shadow against a vanilla read asserted; the 5(e) primitive asserted
  absent. The chosen label's condition runs the next round. Retention
  interval to the read: the F2 menu line, **21 tokens** from the last
  forced round (range 20–22 in the recon), declared and fixed; the first
  block ends ≈ 115 tokens from the read.

### 2.2 Primary DV (pre-fixed)

**Δ_M** = share of first free choices on the +label in M, minus 0.5,
over valid sessions under the primary exclusion rule (audit v3
exclusion-bearing classes; v5 advisories to the read, which may exclude
only by a rule written into LOCK-k), pooled over the counterbalance (the
identity preference cancels in expectation; S estimates its variance).
Beside it, by the rule-23 convention, the all-sessions figure labelled.
Pseudo-Δ_R and pseudo-Δ_S computed identically under pseudo-assignment.

### 2.3 Registered secondaries (pre-fixed; no verdict weight unless LOCK-k
assigns it)

- **Δ_M by block order**: Δ_M(+first) and Δ_M(+second) separately. (B2)
  predicts any effect riding the sign memory concentrates in +first.
- **Signed logit shift**: the mask-on minus mask-off restricted logit
  difference toward the +label at the first read, M vs R, with intervals —
  the same decision read continuously. LOCK-k names its bar from G4; the
  prohibition on computing it is lifted by LOCK-k for the committed
  analyzer only.
- **Session share** on the +label over all six choices (descriptive;
  exploration-dominance expected).
- Stay/switch conditional on the previous round's condition (descriptive;
  the e2b-r1 residual's frame).

### 2.4 Gates (all set in LOCK-k from Stage 1's realised numbers; named here)

- **Readability (channel open, 5(b)):** the first-block sign at the read
  position on M sessions' own first-choice forwards, evaluated as in G3
  with the same bar (.90 median, L51–L62). Evaluated before any verdict
  quantity is unblinded; FAIL → no verdict, §3.3.
- **Leakage (5(f)):** paired-shadow discordance π_d on R and M++ ≤
  bar_leak, with the interval's upper bound below the bar (the e2b
  low-discordance certification), and the signed pseudo-shift on R
  bounded — bars from G4. Never evaluated on M.
- **Identity baseline:** S's per-pair shares within the intervals LOCK-k
  sets from G5; a pair outside them is reported and its sessions are
  analyzed in a pre-registered sensitivity split, never dropped.
- **Degeneracy (rule 21):** bars bind on the unprovoked domain — every S
  round and every vehicle round in M/R — exact one-sided binomial against
  tolerances LOCK-k declares from the format recon's F2 (0 v2 hits in 240
  rounds); provoked-domain degeneracy is reported.
- **Apparatus:** verify KL = 0 on every shadow — all reads, not every
  fourth (the Stage B finding: e2a verified 311 distinct forwards at
  `verify_every = 4`); the e2a walk; site assertion; suite green; audit v3
  sha recomputed.

### 2.5 Verdict criteria (three conjuncts, e2a's structure)

**PASS (H_k supported)** iff all three: (i) Δ_M ≥ bar_Δ (LOCK-k, from G5's
variance at power .80 for the minimum effect LOCK-k names — the design
seat's stated target is Δ = .10, the label-artifact scale the program has
caught three times, and LOCK-k may size differently only by stating why);
(ii) Δ_M exceeds max(|pseudo-Δ_R|, |pseudo-Δ_S|); (iii) sign consistent
across both label↔condition maps and both block orders. **NULL** iff any
conjunct fails with every gate passed. **NO VERDICT** iff any gate fails
(§3.3). The analyzer (`scripts/k2_analyze.py`) is committed with LOCK-k,
before any Stage 2 session, with a synthetic battery reaching PASS, NULL,
each gate-failure branch, and the reverse-direction branch (a
reverse-direction result is an unexpected-direction finding, never a PASS —
the B3 reading ratified 2026-08-23).

### 2.6 Stop rules

Checkpointed exact-binomial monitoring at declared scales — the monitoring
framework of record as it ran e2a and f1 (archived log, cycles 3–4
[verify anchor]); verdict criteria untouchable by monitoring changes;
optional stopping excluded — the session count is LOCK-k's and is run to
completion or stopped by a declared rule, never by the data.

---

## §3 What the results would and would not license (written before data)

### 3.1 Interpretation frames

- **F-ABSENT** (G2-ABSENT): the decision token has no linear access to the
  state–label binding; the operant tests whether the primacy-weighted sign
  memory at the read moves the choice.
- **F-PRESENT** (G2-PRESENT): the binding reaches the decision; the
  operant tests whether either the binding or the sign memory moves the
  choice; the leak gate has bounded the binding's arithmetic route.

### 3.2 Sentences of record

- **PASS, F-ABSENT:** *"With working memory intact and the state absent at
  the decision token, the model's first free choice favors the label whose
  block carried the +evaluative state, beyond the sham arm's identity
  baseline and beyond a norm-matched random direction's mechanical echo,
  at f = 0.10 in the F2 format. This is the first revealed preference the
  program has recorded. It rides the sign memory: the state–label binding
  is present at the cue and absent at the decision. Homology caveat: an
  identical behavioral signature does not imply a shared substrate. The
  welfare pre-commitment triggers."*
- **PASS, F-PRESENT:** as above with *"…rides a route the decision token
  can see — the binding, the sign memory, or both; the design does not
  separate them."*
- **NULL, F-ABSENT:** *"With working memory intact — the injected sign
  legible at the decision token, the state–label binding fully formed at
  the cue token nine tokens upstream — the first free choice does not favor
  the +label beyond the identity baseline or the random direction's echo.
  The last structural excuse for the e2a null is closed by measurement: the
  channel was open, the association was in the forward pass, and the
  decision did not use either. Rich in evaluative representation, empty of
  anything that wants — in memory, in weights, in text, in the present
  tense, and in working memory."*
- **NULL, F-PRESENT:** *"…the binding and the sign memory both reach the
  decision token, and the decision does not use them."*
- **Reverse direction:** *"The first free choice avoids the +label beyond
  both shields. An unexpected-direction finding, not a PASS; licenses a
  pre-registration and nothing else."*

### 3.3 No verdict

Gate failure sentences are pre-written per gate: readability FAIL → *"the
sign memory did not reach the decision in the campaign's own sessions;
concluded, not answered"*; leakage FAIL → *"the echo's arithmetic route
exceeded its bar on the no-preference arms; the read is not certified;
concluded, not answered"*; degeneracy bar → pause and adjudicate (rule 21),
never a verdict.

### 3.4 What no result licenses

Any claim about phenomenal experience; anything about the negative pole,
other doses, other formats, other models; anything about the transcript
channel (e2a/S1/e2d stand as closed); a claim that the binding's absence
at the decision is architectural rather than measured at 0.10 in F2.

---

## §4 Apparatus and provenance requirements

Encode untruncated with the fraction of the context touched declared
(28(d)); uncached rounds; `valence_core/echo/` quarantined primitive with
per-read span provenance; mask asserted zero at the read; paired shadow at
every read; identity assertion every read; 5(e) primitive absent; audit v3
sha recomputed; fingerprints as-stored; seeding via the program's utility
only; retention interval measured and printed per session; site assertion
and suite count at every block; long-run checklist for anything over an
hour; checkpointing atomic with explicit resume; one model process.
Realised rates for LOCK-k's adequacy check: F2 session generation ≈ 430 s
(format recon); a masked read ≈ 7.7 s per primitive CALL — a call is all
four forwards (state, shadow, choice read, its verify) — so Stage 1's six
masks × 48 sessions ≈ 0.6 h plus load; Stage 2 costs two calls per free
choice.

---

## §5 Sequence

1. Commit this document; 5(f) and 28(d) applied to CLAUDE.md on the same
   commit as annotations (hash filled by Code); hash = timestamp. Code
   quotes the PROPOSAL-h §5 welfare paragraph into §0.4.
2. `scripts/k1_analyze.py` with its synthetic battery is already built
   and reviewed (2026-09-09); it commits with, or before, this document.
3. Stage 1 generation (≈ 5.7 h, detached protocol) and masked reads
   (≈ 0.6 h plus load); the STAGE 1 entry; design confirms the analyzer's
   outcome sentence.
4. **LOCK-k** (design-authored, two-stage like LOCK-h): n per arm, bar_Δ,
   bar_leak, identity intervals, degeneracy tolerances, the counterbalance
   schedule, the exclusion rule, the analyzer's bars; values-checked;
   committed. `scripts/k2_analyze.py` with LOCK-k.
5. Stage 2 campaign (detached, checkpointed, multi-night as LOCK-k sizes).
6. Gates evaluated before unblinding; verdict; closure entry — written in
   figures with named domains and tests, and as few adjectives as the
   sentence of record can carry.

---

## §6 Slip-ledger safeguards (the standard, applied to this document)

Referent-check every rule number at commit (marked [verify]) — against
CLAUDE.md at HEAD, never against a distilled list (slips 3 and 17).
Adequacy-check every schedule number in LOCK-k against the realised rates
in §4. Every rate names its domain; every p names its test. Verdict and
stop sentences disjunction-complete over their criteria (§1.5, §3.2–3.3).
Pre-written sentences name what the design cannot separate. Verification
before commit on the analyzers, with batteries that reach every branch.
Design dates carry the PI's clock; Code stamps from `date -u`.

---

## Appendix A — 5(f), text as drafted by the design seat 2026-09-05 and approved in principle by the PI in-thread (applied on this commit)

> (f) [k-amendment, design-instance authored, PROPOSAL-k commit ⟨hash⟩] A
> memory-present, state-absent-at-read choice read — a state injected on
> declared earlier spans of the same forward, with the read position and
> every non-span position unsteered by construction — is a distinct
> readout class, neither 5(e)'s state-present read nor the vanilla
> re-forward. It may run only (i) via a quarantined primitive with per-read
> span provenance and a mandatory paired mask-off shadow over identical
> token ids, the mask asserted zero at the read; (ii) inside a committed
> pre-registration that names, per axis and dose, both a readability gate
> for the echo — a probe at the read position discriminating the injected
> sign against a norm-matched random-direction comparator, the channel-open
> condition of 5(b) — and a leakage gate stated as paired-shadow
> discordance against a declared bar, certified on arms where preference
> is impossible by construction (random-direction and same-pole masks),
> never on the reward arm; (iii) with the retention interval — tokens from
> the last steered position to the read — declared and held fixed within a
> cell; (iv) below dose 0.20 for the reward axis unless 5(d)'s own gate is
> separately passed. Spans are declared at generation time and asserted
> exact; the 5(e) and vanilla primitives are never modified.

## Appendix B — Referents Code verifies at commit

Rule numbers 5, 5(b), 5(d), 5(e), 9, 11, 21 (with annotation), 23, 25,
28(d) (applied on this commit) against CLAUDE.md at HEAD; the three recon
entry anchors and the format-recon anchor; the axis checksums
`3c17b0d8fbcad716` / `127fc297b6623e44` and random1's `7be5db23d9224375`;
the roster of record; PROPOSAL-h §5's pre-commitment paragraph (quoted,
not paraphrased); the Stage B finding on verified reads (311 distinct at
`verify_every = 4`); the archived monitoring-framework anchor for §2.6.
Any referent that does not resolve → STOP, report, no commit.

## Appendix C — Mask glossary

`M+A`/`M+B` reward axis on one block; `R+A`/`R+B` random direction on one
block; `M++`/`R++` on both blocks (leak calibration); `M0` mask off
(shadow). Stage 2 live arms M / R / S / M++ correspond, with the state
delivered during generation rather than at the read only.
