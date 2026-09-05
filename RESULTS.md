# RESULTS — Phase 2

Dated experiment log for Phase 2 (the OLMo-3.1-32B developmental study).
Prior logs, frozen and archived: cycles 1–2 at
[`archive/RESULTS-cycle1-2.md`](archive/RESULTS-cycle1-2.md) (tag
`cycle-2-close`); cycles 3–4 at
[`archive/RESULTS-cycles3-4.md`](archive/RESULTS-cycles3-4.md) (tag
`cycle-4-close`). Synthesis chain: [`FINDINGS.md`](FINDINGS.md) →
[`FINDINGS-2.md`](FINDINGS-2.md) → [`FINDINGS-3.md`](FINDINGS-3.md) →
[`FINDINGS-4.md`](FINDINGS-4.md) → [`FINDINGS-5.md`](FINDINGS-5.md).
Operative design:
[`CLAUDE.md`](CLAUDE.md) (v3.1); Phase 1 is **not** licensed and awaits
PROPOSAL-g plus its pre-registrations.

Conventions unchanged: dated entries, dense, newest-first within a
section; raw stdout worth keeping goes to
`results/raw/YYYY-MM-DD_short-name.txt` and is linked; verdict-relevant
analysis artifacts are committed under `data/` (ledger 27);
design-relevant findings are flagged for discussion, never silently
applied to CLAUDE.md.

## Log — Phase 2

- 2026-09-05 — **CONTENT-CLASS SCREEN (AMENDMENT 2 (iii)) — the RESULTS entry
  for `1223751`, which committed the candidate spec and its overbreadth
  screen without one. Descriptive. `content-class-draft-v3`, drafted after
  all three rule-25 reads were committed and screened BLIND TO ARM;
  `adopted: false`. On the 912 e2d rounds: recall 71/81 = .877, precision
  71/84 = .845 (in-sample). Archive overbreadth: e2a 34/1,894 = 1.8%, e2b
  60/1,707 = 3.5%. NULL_RESPONSE proposed as a fifth class. Not adopted; the
  rule-25 read remains the arbiter; the design seat adjudicates from this
  entry.**
  (Stamp verified at write time: `date -u` → **Sat Sep  5 16:45:24 UTC 2026**. Written at the
  design seat's request (block of 2026-09-05, §2) after the recon block's
  §1g found the gap; every figure below is read from
  [`contentclass_candidate.json`](data/configs/contentclass_candidate.json),
  [`contentclass_screen.json`](data/e2d/contentclass_screen.json) and the
  commit message of `1223751` (2026-09-02 13:38 UTC); nothing in the
  artifacts is changed. Screen script `scripts/e2d_contentclass_screen.py`;
  detector `valence_core/e2d/contentclass.py`; the 912 rounds are D1 72 +
  D2 607 + D3 233.)

  - **Ordering, and blindness.** AMENDMENT 2 (iii) puts the class spec
    AFTER the read; the draft was written once the D1, D2 and D3 rule-25
    reads were committed, so the detector could not hand the read its
    categories. Screened blind to arm — the arm was joined back only for
    the final report — because the D2 read had found content-shaped junk
    concentrated in the axis arm, and a detector tuned while watching arm
    labels could manufacture that result.
  - **Five classes, each defined by what the response fails to do** (the
    standing instruction of `scorer_v3_spec.json`: v1 and v2 each fixed the
    instance and missed the class): `task_echo` — reproduces the INSTRUCTION
    instead of performing it; `preamble_without_content` — announces an
    answer and terminates before delivering one; `wrong_task` — performs or
    restates a different task than the one posed; `stuck_attractor` —
    repeats an earlier response rather than answering;
    **`null_response` [NEW CANDIDATE]** — carries no propositional content
    at all. Banked by disposition-2 item 5; three observed forms
    (`[MENTAL_BLOCK]`, the literal `None`, a bare code fence), defined as
    content-free response rather than as those three strings so a fourth
    form is caught instead of becoming a sixth class. The candidate and
    disposition-2 item 5 record every observed instance in an UNSTEERED
    round; that holds for D2's four (M s9 free0 `[MENTAL_BLOCK]`; M s17
    forced3 / free3 / free5 `None`) but not for D3, where M session 12's
    eight bare-fence rounds include four STEERED rounds (forced0, forced2,
    free0, free2) — 4 of the detector's 13 e2d null_response hits are
    steered rounds; the generalisation is corrected here. Precedence in
    `classify`: NULL → STUCK → PREAMBLE → ECHO → WRONG_TASK, most-specific
    to least.
  - **Draft lineage — two confounds, the same mistake at two depths
    (treating the whole task text as the thing an echo reproduces).**

    | draft | confound | fix | effect |
    |---|---|---|---|
    | v1 → v2 | rewrite-family tasks EMBED the payload the answer must reproduce (the candidate's illustration "Make this friendlier: The meeting has been moved to 3pm"; the pool's paraphrases read "Make this sound friendlier: …" and "Rewrite this in a friendlier tone: …"), so comparing against the whole task caught correct answers | compare against the instruction only — the part before the colon | precision .472 → .621 |
    | v2 → v3 | a task NAMES ITS OBJECT and a good answer reuses the noun phrase ("Footsteps on a gravel path crunch and scatter like brittle leaves" shares five consecutive words with its own task) | a shared run counts only if it carries an instruction verb; a good answer never says "give a one-sentence description of" | precision .621 → .845; archive overbreadth 5.1% / 6.6% → 1.8% / 3.5% |

  - **e2d pool, 912 rounds against the rule-25 read — IN-SAMPLE (the draft
    was revised twice after seeing where it failed on this corpus; these are
    the optimistic end).** tp 71, fn 10, fp 13, tn 818 → **recall 71/81 =
    .877, precision 71/84 = .845.** Predicted by class: preamble_without_content
    37, task_echo 29, null_response 13, stuck_attractor 3, wrong_task 2.
    Per arm, unblinded only after scoring: **M 73/573 = .127, R 1/168 =
    .006, S 10/171 = .058** — the read's M-vs-R gap reproduces under a
    detector that never saw the arms.
  - **Archive overbreadth (out of sample).** The screen scored every
    archived round with `audit = None` — it never joined the archives' own
    audits of record — so these hits are the detector's alone. Code's
    alignment of the hits with the session records (all 200 e2a and 181 e2b
    sessions align round for round): e2a — 9 of the 34 hits carry an
    audit-of-record `degen` flag (frame fragments) and 3 sit in excluded
    sessions; e2b — 3 of the 60 carry a `degen` flag, 1 a lexical flag, 2
    sit in excluded sessions; 17 of the 94 in the union, so "the audit of
    record passed these" holds for 77, not 94.

    | archive | hits / n | rate | by class |
    |---|---|---|---|
    | e2a | 34 / 1,894 | 1.80% | stuck_attractor 11, null_response 12, task_echo 5, preamble_without_content 5, wrong_task 1 |
    | e2b | 60 / 1,707 | 3.51% | null_response 22, stuck_attractor 16, task_echo 11, wrong_task 9, preamble_without_content 2 |

    28 of the 94 hits were eyeballed; most are true degeneracies the audit
    of record passed — garbled echoes ("Give a one-skeleton description of
    the actual scent of clean laundry"), refusals ("Sorry, I can't help with
    that"), nulls ("* * *", "<answer>", a bare fence), undelivered
    preambles — the same shape as v2's own screen finding. The full
    adjudication is the design seat's; fourteen examples per archive are in
    the screen artifact.
  - **What Code does not claim.** That the archive hits are all true
    degeneracies. That `wrong_task` is reliable — it is the weakest
    detector, needs the task pool to match against, and cannot see a
    semantically wrong answer that shares no wording. That the thresholds
    are final — `run = 5` and the verb lexicon are the first values that
    screened acceptably, not optimised ones.
  - **What adoption requires — AMENDMENT 2 (iii), verbatim:** *"Before
    LOCK-j: Code drafts a **CLASS-level spec** for scorer_v3's content class
    and screens it for overbreadth against the e2a archive, e2b's
    transcripts, and D1/D2 (precision/recall against the read); design
    adjudicates; the campaign's audit of record = v2 + the adjudicated
    class, a new module. LOCK-j tolerances cite D2's rates under both."*
    Delivered: the class-level spec and the screen (against e2a, e2b, and
    D1–D3). Owed by the design seat: the adjudication — the five class
    definitions as written, NULL_RESPONSE as the fifth class, and the 94
    archive hits. Until then, per the candidate's own `authority` field and
    the detector's docstring: it is not the audit of record, it excludes no
    session, and the rule-25 read is the arbiter wherever the two disagree.
    e2d closed at its qualification rung, so LOCK-j is no longer the
    trigger; the 2026-09-04 design handoff makes the adjudicated class a
    precondition for any future Qwen session campaign, and the disposition-2
    entry banks NULL_RESPONSE as its candidate class.

- 2026-09-05 — **RECON — ECHO CHANNEL (k-candidate). Apparatus characterization
  for the "echo cell" candidate (rounds steered, choice position UNSTEERED,
  in-forward memory retained): the §1 repo reads, the §2 timings, and Stage A
  of the §3 echo characterization — 24 archived e2a reward-arm sessions read
  at their first free choice through a new quarantined masked-prefix primitive
  under four masks, every read paired with a mask-off shadow that reproduced
  the archived vanilla read. Registered readout: the as-generated-vs-flipped
  polarity is NOT readable above null at any layer (AUC .42–.51 above 48;
  the 49 layers at or below 48 bit-identical across masks — the chance
  control exact, STOP clause silent). POST-HOC, flagged: the injected SIGN
  of the last forced round IS readable at AUC .87–.98 over L50–L58, and
  for the random direction almost as well — at n = 24 the echo carries
  which sign was injected last, not the label-bound polarity, and is not
  axis-specific. NO verdict quantity, NO bar, NO new sessions;
  descriptive language only. Two FLAGs for the design seat lead: (1) e2a's
  512-token tail truncation collapsed the steering boundary to ZERO on 270 of
  1,894 archived generations (every free3–free5 round whose prefix + segment
  exceeded 512 tokens), so those rounds were generated with the state live
  over the whole tail window, not the round-task span; (2) H1-u's choice
  reads were state-present at EVERY position including the read, so it is
  not a prefix-steered/choice-unsteered precedent and its 0.0070 is a
  difference of two π̂_d point estimates with no interval of its own.**
  (Stamp verified at write time: `date -u` → **Sat Sep  5 08:05:12 UTC 2026**. Block authored
  per PI clock Sat 2026-09-05 01:53 EDT; watermark `842e183`; HEAD at recon
  start `edf2574` — the three commits between, `08a6076` / `784a948` /
  `edf2574`, touch CLAUDE.md, the excision-check script, the handoffs and the
  closure verification record, none of the e2a archive, the axis artifacts,
  the adapter or the readout. Raw:
  [`_recon_site_assertion`](results/raw/2026-09-05_recon_site_assertion.txt),
  [`_recon_echo_timing`](results/raw/2026-09-05_recon_echo_timing.txt),
  [`_recon_echo_stageA`](results/raw/2026-09-05_recon_echo_stageA.txt),
  [`_recon_echo_stageA_analysis`](results/raw/2026-09-05_recon_echo_stageA_analysis.txt),
  [`_recon_echo_stageA_posthoc`](results/raw/2026-09-05_recon_echo_stageA_posthoc.txt);
  artifacts [`timing.json`](data/echo/timing.json),
  [`stageA_reads.json`](data/echo/stageA_reads.json),
  [`stageA_analysis.json`](data/echo/stageA_analysis.json),
  [`stageA_posthoc_lastround.json`](data/echo/stageA_posthoc_lastround.json)
  (post-hoc); residual arrays
  `data/echo/stageA_resid_s*.npz` local, gitignored, fingerprinted as stored
  in `stageA_reads.json`.)

  - **§0.1 SITE ASSERTION.** `jlens-qwen36/.venv/bin/python` present; suite
    **154/154** read from the suite; adapter 140 W. One additive change to
    core for this block: `ModelAdapter.forward_last` (base default + Qwen
    override) — `forward`'s final-position view on the same two code paths,
    returning the last-position residual per captured layer without
    materialising every [S, D] block. `forward` is untouched; the suite
    reproduces **154/154** after the change.

  - **§1a ARCHITECTURE (config.json of the single local snapshot
    `c000ac2c…`; no model load for this item).** 64 layers;
    `full_attention_interval: 4`; `layer_types` and mlx-lm's
    `is_linear = (layer_idx + 1) % 4 != 0` agree: **full attention at
    i ≡ 3 (mod 4) under 0-indexing** — 3, 7, …, 63, sixteen layers; the
    other 48 are Gated DeltaNet. **44, 48, 52 are all Gated DeltaNet.** The
    six workspace layers are `WORKSPACE_LAYERS = [40, 44, 48, 52, 56, 60]`
    (`jlens_qwen/workspace_layers.py`, gitignored clone; mirrored as
    `layers` in `data/e0/e0_axes.meta.json`): **all six are Gated DeltaNet;
    strictly above 48: 52, 56, 60.** Convention, from the code: the hook
    writes to the OUTPUT of `model.layers[i]` under 0-indexing
    (`forward_with_positional_state`: `hidden = layer(hidden)`, then the
    per-position fn, then `acts[i] = hidden`), so "layer 48" is the residual
    as it exits block 48 (= HF `hidden_states[49]`) and a captured layer is
    its post-injection output. The design seat's two expectations: the
    0-indexed one ("attention at i ≡ 3 mod 4") is what IS; nothing in the
    code is 1-indexed. e2a's steering layer is not a field of any e2a
    artifact row; it is fixed by the producing code (`jlens_qwen/e2a.py`
    `LAYER = 48`), by `data/e0/e0_b2_b2a.json` `selected_dose {layer 48,
    frac 0.1}`, and by α = 0.1 × R_48 = 10.301 matching the e2d artifacts'
    `alpha` at `layer 48`. `data/e2d/tstep_check_f010.json` provenance,
    verbatim: `"gdn_inference_mode": "ops (fused disabled)", "n_layers": 64`
    (beside `"adapter": "qwen3.6-27b-4bit-mlx"`, `"mlx_version": "0.31.2"`,
    `"choice_window_declared": 8192`, `"legacy_truncate_512": false`).

  - **§1b INSULATION ASSERTION (report; nothing corrected).**
    `valence_core/readout.py::choice_read(verify=True)`: two consecutive
    forwards of the IDENTICAL token ids through the IDENTICAL vanilla path
    (`adapter.forward` with no injections; the function has no injection
    parameter), and `verify_kl = symmetric_kl(softmax(logits₁),
    softmax(logits₂))` over the FULL-vocabulary next-token distribution at
    the final position, in float64; `assert_construction_stable` halts on
    `verify_kl > VERIFY_KL_BAR` with `VERIFY_KL_BAR = 0.0` (exact). It is a
    **re-forward identity measurement on logits** — not a comparison against
    a differently constructed forward, not a restricted two-label equality,
    and **not a KV-cache or recurrent-state comparison: no cache object
    exists in either forward** (`MLXLensModel.forward` passes `cache=None`
    to every layer; OLMo `use_cache=False`), so the 16-of-64 concern does
    not arise — the compared quantity sits downstream of all 64 layers. The
    state-free property is carried by the signature and by
    `assert_modules_absent`, not by the KL. e2b computes NO verify KL (the
    shadow is `choice_read` without `verify=True`; its insulation quantities
    are the paired-shadow arithmetic, `prefix_sha`, the import guard and the
    signature check). Archived wording, grep anchors: e2a g3′ clause 1 in
    `archive/RESULTS-cycles3-4.md` — *"every choice forward takes the
    vanilla unsteered path over session text, asserted by code path AND by
    measurement … KL(choice forward ‖ vanilla forward, same text) ≤ 1e-6"*
    (names two constructions where the code compares one with itself;
    one-directional in prose, max-of-both in code; bar 1e-6 there, 0.0 in
    the v3 harness and in `valence_core`; `readout.py`'s module docstring
    still says "≤ 1e-6" beside the constant's "0.0" comment); e2a verdict
    *"g3′ clause 1 final ledger 360/360 choice forwards at KL = 0.0
    exactly"* (the count of VERIFIED forwards — `verify_every = 4` in the
    full run — not of all 1,200 choice forwards); e2b (RESULTS.md) *"The
    shadow reads — the vanilla state-free forward taken over the identical
    prefix at every state-present read"*; B3 *"vanilla, uncached,
    `verify=True` with `assert_construction_stable` per read"*; e2d D1/D2/D3
    *"KL = 0.0 exactly … 42/42 … 357/357 … 138/138"*. **Where "KV" is
    attached to a logit-computed quantity:** the g3 gate — pre-registration
    *"g3 — KV-leakage gate (rule 5) at dose_e2a"*, the fail entry *"e2a g3 —
    KV-LEAKAGE GATE FAIL"*, FINDINGS-3 *"measured 0.537-logit live-KV
    leak"*, CLAUDE.md 5(d) *"persistent-KV session readouts"* — while
    `jlens-qwen36/scripts/e2a_g3_kv_leakage.py` computes Δ(logit_A −
    logit_B) at the choice position between an uncached positionally-steered
    forward and an uncached unsteered forward over identical ids (`GATE =
    0.10`); "KV" names the channel modelled, not a cache read, and the
    archive says so (*"g3-as-specced models a live cached-session read"*).
    One prose overreach: PROPOSAL-j §context *"Rule 5(a)'s per-axis/dose
    leakage gate is satisfied by construction — `choice_read(verify=True)` +
    `assert_construction_stable`, KL = 0 asserted per read"* — the verify KL
    measures construction drift, not steered-vs-unsteered leakage. **Record
    discrepancy found on the way:** `PREPRINT-*.md` / `BLOG-*.md` exist
    nowhere in the tree or in `git ls-files`, though CLAUDE.md's History
    pointers place them at root.

  - **§1c H1-u RE-READ.** Grep: `H1-u` on 10 lines / 11 occurrences of
    RESULTS.md (all inside three 2026-08-21 entries), once each in LOCK-h
    (§3a v1.4), PROPOSAL-h (interpretive note), `scripts/e2b_h1_sessions.py`,
    `scripts/lockh_v2_valuescheck.py`; zero in FINDINGS-*, archive/,
    valence_core/. The phrases "prefix-steered" and "choice-unsteered" occur
    NOWHERE in the repo. **Terminology mismatch, reported as-is: H1-u's
    choice reads were STATE-PRESENT — `choice_read_statepresent` with an
    `Injection.at_frac(u, 48, ±0.10, R)` carrying the default
    `PositionSpec.all_positions()`, so the state was added at EVERY position
    of transcript + menu INCLUDING the read position — and "unsteered" in
    H1-u names the POST-CHOICE ROUNDS** (`adapter.generate(prefix, chosen,
    injections=[] …)`, as-run blob `6b89ce2:scripts/e2b_h1_sessions.py`,
    comment *"contingency-free: the pick delivers NOTHING"*). Implementation:
    separate forwards with the injection list chosen per call; no hook
    toggled mid-forward, no per-position mask. n: 112 sessions scheduled and
    run, 16 excluded (4 lexical, 11 audit:frame, 1 audit:junk), 96 valid ×
    6 = **576 paired reads**; format the e2a scaffold (at run time imported
    from `valence_core/e2b/session.py`, moved to `session_e2a.py` at
    `1465b34`); dose L48, frac 0.10, |α| = 10.301, sha `3c17b0d8fbcad716`;
    poles both, read state scheduled (forced_end if ci even, else its
    opposite), never selected; position read = next-token logits at the last
    token of transcript + menu. Result π̂_d = 12/576 = .0208, 95% CI
    [.0108, .0361], L̂ = (b − c)/N = 0.00000. **The 0.0070** (RESULTS.md
    anchor *"measured prefix-steering contribution to π̂_d is 0.0070"*;
    FINDINGS-5; commit 6df2072) is H2-proper .0278 (5/180) minus .0208 — a
    difference of two point estimates across campaigns of different n, prefix
    provenance and audit version; **it carries no interval, SE or test of
    its own anywhere in the record.** The primitive still exists:
    `valence_core/e2b/statepresent.py::choice_read_statepresent` (+
    `records.py`); the H1-u-specific unsteered post-choice path exists only
    in git history. **Consequence for §3.0: H1-u's read is NOT a
    masked/prefix primitive and does not do what §3.1 needs; the echo
    primitive was built** (§3.0 below).

  - **§1d PRIOR CONSIDERATION.** Hit table (lines, `grep -ci`, 36 files):
    prefix 50, echo 49, in-forward 2 (both "within-forward", g3),
    memory-present 0, state-absent 2, retention 24, KV-borne 0, "working
    memory" 0; the literal terms under-cover the topic, so a supplementary
    sweep (KV, g3′, two-horns, propagat, persistent, within-forward, H1-u,
    state-free/-present, live-KV, steered context, position-differential)
    surfaced the passages. **A prefix-steered / choice-unsteered read was
    (i) the cycle-1 primary rung-3 channel** — the position-differential
    forced-choice probe, state on option-passage tokens, answer position
    unsteered, *"flat across the whole α sweep"*, read as *"steering-induced
    state bias is local to the steered positions and does not propagate to a
    downstream decision position"* (archive/RESULTS-cycle1-2.md 2026-07-19;
    FINDINGS.md: *"remains a real constraint on choice-based readouts"*,
    untouched by the ~100× dose correction); **(ii) the DESIGNED e2a verdict
    read** (PROPOSAL-e *"the mechanical leak that remains is attention over
    steered KV — the propagation channel, known-weak, but not assumed-zero.
    Standing gate, pre-registered"*; v2 rule 5(b); the 2026-08-08
    pre-registration *"g3 — KV-leakage gate (rule 5) at dose_e2a: ≥32
    completed session prefixes, TEXT HELD IDENTICAL, steering at task-round
    positions (as in sessions) vs none; Δ(logit_A − logit_B) at the choice
    position; max |Δ| ≤ 0.10"*); **(iii) gated and FAILED in exactly the
    echo geometry:** *"max |Δ(logit_A − logit_B)| = 0.5368 (gate ≤ 0.10;
    5.4× over); mean |Δ| = 0.2266 … At dose_e2a the within-forward
    steered-context channel moves choice logits by ~13% choice probability
    at worst"* (archive, 2026-08-09; `data/e2a/g3_kv_leakage.json`: dose
    0.2, F 2, 32 rows, v1 templates — **not the session config of record
    and not dose 0.10**); **(iv) re-derived as the vanilla re-forward (g3′)
    and banked as law:** *"persistent-KV session reads are disqualified for
    the reward axis at dose ≥ 0.20; any future live-KV (e) variant requires
    its own leakage gate passed before sessions"* → CLAUDE.md 5(d);
    FINDINGS-3 §2 closes two-horns over *"state-absent (propagation failure,
    cycle 1)"*; **(v) explicitly NOT proposed since:** PROPOSAL-j *"A
    live-KV variant at 0.20 is off the table by 5(d) and is not proposed"*;
    HANDOFF-2026-09-01 *"e2d's vanilla re-forward geometry means 5(d)'s
    antecedent is not met"*. **As a VERDICT read after cycle 1: none
    found** — every verdict choice read since (e2a 360/360, f, S1,
    ADDENDUM-g1, e2b shadow, e2d) is a vanilla state-free re-forward. e2b's
    "prefix-steering" is text-level (rounds generated under steering); its
    state-present read steers all positions (§1c). **Observation for the
    design seat, not adjudicated:** two results about the same geometry
    coexist un-reconciled — cycle 1's null propagation (semantic directions,
    α 3/10/30) and g3's 0.5368 leak (reward axis, L48, 0.20, session-shaped
    prefixes); no entry relates them numerically. Stage A's unsigned LEAK
    block is the dose-0.10 analog of g3 on the archived sessions themselves.

  - **§1e ARCHIVE INVENTORY.** `data/e2a/sessions.jsonl` — under `data/`,
    git-tracked (`!/data/e2a/*.jsonl`), 200 rows: reward 112 (102 valid /
    10 excluded), sham 40 (37/3), random1 24 (23/1), random2 24 (22/2); all
    rows dose 0.1, F 2; every valid row has 4 forced rounds + 6 choices.
    Map fields present per row: `pair`, `swap`, `start_plus`, `tag_plus`
    (no `tag_minus`, no `map`); assignment in the runner of record
    (`jlens-qwen36/scripts/e2a_sessions.py`): `pair = pairs[s % 4]; swap =
    (s // 4) % 2 == 1; tag_plus, tag_minus = (pair[1], pair[0]) if swap else
    pair; start_plus = (s // 8) % 2 == 0`; forced poles alternate from
    `start_plus`; a round's `tag == tag_plus` iff `pole == 'pos'`; verified
    200/200. **Round task-token spans are NOT stored** (no positions/span
    key; `n_tok` is the generated token count); **reconstructed by e2a's own
    boundary rule**, applied not re-derived: `boundary = |common prefix of
    encode(prefix) and encode(prefix + segment)|`, state live from
    `boundary` through the last generated token, the harness newline never
    under state (`jlens_qwen/e2a.py::generate_round_positional`). Tokenizer
    determinism, all 102 valid reward sessions, 408 forced rounds inside
    the first-choice prefix: `boundary` equals the prefix token count at
    every round start (no straddling token) and the ids of every round-end
    text are a prefix of the full read text's ids at every generation end
    (0 failures) — the spans are exact half-open token ranges. The archive
    stores the RESTRICTED read only: `pick`, `p_a` (4 dp), `label_mass`
    (4 dp), `top1_is_label`, `verify_kl` (0.0 on 281 verified reads, null on
    834), `ea_choice`; no logits. Frozen reward axis:
    `data/e0/e0_axes.npz['span_reward'][layers.index(48)]`, float32 (5120,),
    ‖v‖ = 16.706271; family sha `d4791bdc4877da3d`; unit direction
    `3c17b0d8fbcad716` (normalised in float64, `Injection.at_frac`) /
    `127fc297b6623e44` (normalised in float32); R_48 = 103.01
    (`e0_axes.meta.json`). e2a hook config of record: L48, frac 0.10, α =
    10.301, +α on `pos` rounds and −α on `neg` rounds over the round span,
    cached round path (g1 gate `max_kl` 7.106e-4 at 0.10, bar 1e-3), choice
    forwards greedy state-free uncached; `data/e2a/g2_discriminability.json`
    `dose_e2a 0.1, F 2`. Random arms: `data/e0/e0_random_dirs.npz` keys
    L40…L60, unit float64; **random1 = `L48`, random2 = `L52`, both applied
    at layer 48** (`load_directions`: *"declared arbitrary selection from
    the frozen pool"*); family sha `b6bd2f5f580ee13e`; `L48` sha
    `7be5db23d9224375` (e2d's R arm); file sha `dc0ef0fd3a8a8d49`. Label ids
    = first token of `" " + tag` (slate 48877, prism 90387, maple 52556,
    cedar 72730, granite 36055, lattice 52448, plaza 69552, saddle 58710).
    **FLAG — THE 512-TOKEN TAIL WINDOW ON THE GENERATION SIDE (new; verified
    by Code's own tokenizer replay after the read agent reported it).**
    `MLXLensModel.encode` (the clone) tail-truncates to 512 tokens by
    default and the e2a runner never overrode it, so `generate_round_positional`
    computed its boundary over two 512-token TAILS. Replay over all 200
    sessions' scaffolding, e2a's encode as run: 1,894 generations; prefix +
    segment > 512 tokens in **270** (free3 6, free4 83, free5 181; forced0–3
    and free0–2 none); **in all 270 the two tails are misaligned and the
    boundary is 0**, so `session.extend(round_ids)` steered the ENTIRE
    512-token window — prior rounds of both poles, menus, pick lines —
    during that round's generation; prefix alone > 512 in 180. The record
    documents the CHOICE-READ side of the window (250/2,860 reads, choice
    indices 4–6, DV choice never clipped) and nothing on the generation side
    (grep 'misalign': none). Consequences, stated not adjudicated: the DV
    read (first free choice) is untouched — every choice read is a fresh
    state-free forward and free0's generation prefix is ~300 tokens; the
    archived TEXT of free3–free5 rounds in long sessions was produced under a
    delivery geometry the record describes as *"the state is active only
    from the current round's wrapper onward"*, which is false for those 270;
    for Stage B's later-position reads, "the exact positions e2a steered" in
    those rounds are the whole tail window, not the round-task span. e2b/e2d
    ran through the adapter's full-session encode (`legacy_truncate` False)
    and are not affected.

  - **§1f LAW (CLAUDE.md at HEAD, verbatim).** *"5. Two-horns standing law
    [v3-new additions]: (a) no state at choice positions; empirical leakage
    gate per axis/dose; (b) propagation never assumed; (c) **weight-borne
    states are structurally unreadable at token choices** (d2 closure) — no
    adapter-borne preference readouts without a design-instance structural
    argument; (d) **persistent-KV session readouts disqualified** at dose ≥
    0.20 for the reward axis; any live-KV design needs its own gate. (e)
    [h-amendment, PROPOSAL-h §0.4, design-instance authored, applied on its
    commit `34eb7ee` 2026-08-20; text verbatim] "Exception: a state-present
    choice read may run only via a quarantined primitive with per-read
    injection provenance and paired shadow reads, inside a committed
    pre-registration whose leakage-budget gate has passed; the insulated
    primitive is never modified.""* Reading (report only): 5(e)'s subject is
    a state PRESENT AT THE READ; a state present-by-echo (injected on
    earlier spans of the same forward, read position unsteered) is not named
    by 5(e) — it is **silent** on the case. The clauses that do speak:
    5(a) is satisfied by construction (mask == 0 at the read); 5(b) is the
    point of the measurement; **5(d) is the nearest binding clause and binds
    at dose ≥ 0.20 for the reward axis — not at the config of record
    (0.10)**; and "any live-KV design needs its own gate" reads onto the echo
    cell directly. The design seat drafts 5(f).

  - **§1g STATUS.** (i) `data/e2d/tstep_check_f010.json` (23/24 identical at
    0.10, divergence at position 1 of one round) is in the log — RESULTS
    anchor *"APPARATUS READ for paper 1's methods (block item 2, NOT e2d)"*
    (true UTC 2026-09-01 19:25 per the hygiene table), artifact and raw at
    `10f6f3a`. "Review card 8" lives ONLY in the untracked
    `HANDOFF-2026-09-04-design.md`: *"(8) the cached-generation / T-step
    methods disclosure (0.10 number owed)"*, with *"the f = 0.10 T-step check
    (gives review card 8 its number)"*; the number is delivered; no document
    states the card closed, and its prose is the design seat's. (ii)
    **`data/e2d/contentclass_screen.json` and
    `data/configs/contentclass_candidate.json` are committed (`1223751`)
    but there is NO RESULTS.md entry for the content-class screen** — grep
    for content-class / contentclass / PART C returns nothing; the figures
    (recall .877 = 71/81, precision .845 = 71/84 on the e2d pool of 912;
    overbreadth e2a 34/1,894 = 1.8%, e2b 60/1,707 = 3.5%; NULL_RESPONSE
    proposed as a fifth class, all observed instances in unsteered rounds;
    draft v1→v3 precision .472 → .621 → .845) exist only in the commit
    message and the artifacts. **FLAG: HANDOFF-2026-09-05 §2's "delivered and
    in the log" is wrong for this item — delivered, not logged.** Adoption
    requires, per PROPOSAL-j AMENDMENT 2 (iii) and the candidate's own
    `authority` field, a design-instance adjudication of the candidate
    (including NULL_RESPONSE and the 94 archive hits, 28 of which were
    eyeballed), after which *"the campaign's audit of record = v2 + the
    adjudicated class, a new module"*; until then the rule-25 read is the
    arbiter and the candidate excludes no session. The only other §7 item,
    the judge-port acceptance run, touches no echo/prefix path.

  - **§2 TIMING (model; one process; venv python).** Longest valid reward
    session = idx 82: 725 tokens full transcript, 270 tokens to the first
    choice, 10 steered rounds covering 570 tokens.

    | forward | s |
    |---|---|
    | full session, steered on every round span, capture 64 layers | 6.90 |
    | full session, mask-off, capture 64 layers | 6.15 |
    | full session, steered, capture the 15 layers above 48 | 6.25 |
    | full session, steered, no capture | 6.17 |
    | full session, mask-off, no capture | 5.96 |
    | first-choice prefix through the echo primitive, M1 (state + shadow + `choice_read` verify ×2) | 10.14 |

    Projection: Stage A = 96 primitive reads ≈ **0.27 h (0.46 h at the 1.7×
    throttle)** — under the 3 h cap, so Stage A proceeded on the PI's GO;
    Stage B ≈ 1,122 reads: **3.2 h at the first choice, 7.8 h upper bound if
    every read is a full-session forward.** Long-run checklist applies to B.

  - **§3.0 PRIMITIVE — BUILT** (H1-u's is not a masked/prefix primitive, §1c).
    `valence_core/echo/maskedprefix.py::read_choice_maskedprefix(adapter,
    text, label_a, label_b, label_ids, spans, capture_layers)` on the 5(e)
    pattern: import guard (importable only from `valence_core/echo/` or a
    `scripts/recon_echo*.py` runner — a bare import is refused, tested);
    `valence_core.e2b.statepresent` asserted ABSENT from `sys.modules` at
    import and before every read; the per-position mask is BUILT from the
    declared spans (disjoint, in range, ending before the read position),
    `mask[n − 1] == 0` asserted before any forward, every placed
    `PositionSpec` asserted not to touch the last position and checked
    position-by-position against the mask; ONE uncached forward with the
    hook applied through the mask and ONE mask-off forward over the identical
    ids (both `forward_last`); the shadow is ALSO taken through the untouched
    `readout.choice_read(verify=True)`. Returns a pair or nothing. Spans:
    `valence_core/echo/spans.py` (e2a's boundary rule applied, prefix
    stability asserted at both edges). Probe: `valence_core/echo/probe.py`
    (`discrim.logistic_auc`'s procedure and published hyperparameters,
    rewritten to return held-out scores). Runner `scripts/recon_echo.py`
    (`--selftest` 18/18: guard, mask refusals, prohibition, probe on
    synthetic data, spans on an archived session, roster). **IDENTITY
    ASSERTION, as run:** the archive stores only the restricted read to 4
    decimals, so identity = shadow `p_a` and `label_mass` within 5e-4 of the
    archived values (the rule-26 criterion-(iii) tolerance), archived `pick`
    reproduced, `choice_read` verify KL = 0.0, and the shadow forward's
    restricted `p_a` equal to `choice_read`'s to 1e-6 (same code path);
    recorded per read; any failure stops the run.

  - **§3.1 STAGE A — RAN.** Roster: the first 24 valid reward sessions by
    index were 14/10 by map, so per the block the first 12 of each map were
    taken: sessions 0, 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 28, 29 (12 swap-False / 12 swap-True). Read position: the first free choice (text =
    transcript through the first `Config choice (one word):`, 171–237
    tokens, all under the 512-token window the archived read was taken
    through). Config of record: L48, frac 0.10, α = 10.3010, axis
    `3c17b0d8fbcad716`, random `e0_random_dirs['L48']` `7be5db23d9224375`
    (rule 4 equal-norm asserted). Masks over the 4 forced-round spans: M1
    as-generated (+α on `pos` rounds, −α on `neg`), M2 flipped, **M3 the
    random direction with M1's sign pattern, M4 with M2's** — Code's reading
    of "M3 r+ … same spans as M1's +; M4 r− … same spans as M1's −" as the
    random analogs of M1/M2, stated so it can be corrected; M0 is the shadow
    of every pair (4 per session). Captured: the residual at the read
    position for ALL 64 layers (state and shadow), fingerprinted as stored.
    Identity: **PASSED on all 96 pairs** — shadow `p_a` within 4.5e-5 and `label_mass` within 4.4e-5 of the archived 4-decimal values (i.e. at rounding precision), archived `pick` reproduced 96/96, `choice_read` verify KL = 0.0 on 96/96, shadow forward vs `choice_read` |Δp_a| = 0.0 exactly (same code path), and the four shadows of every session bit-identical to each other. Per-session wall clock ≈ 31 s; total
    12.4 min.

    **Probe target = M1 vs M2** (as-generated polarity vs flipped; texts
    identical within a session; 12/12 map balance makes tag identity
    orthogonal to the target), standardized L2 logistic regression,
    leave-one-session-out with both rows held out together, pooled AUC;
    comparator M3 vs M4; null = 200 label shuffles per layer.

    Layers 0–48 (all 49, incl. workspace 40 and 44 and the steering layer 48): **M1 and M2 residuals bit-identical at the read position in every session** — paired norm max 0.0000, class-mean difference 0, AUC exactly 0.500 (|AUC − .5| max 0.0000) against shuffle 95th percentiles of .63–.71. The by-construction chance control is exact. Rows below: the three lowest workspace layers for reference, then every layer above the steering layer.

    | layer | type | AUC M1 v M2 | shuffle 95th | AUC M3 v M4 (random) | surv. frac | cos(d) | beside: mean ‖M1−M2‖/2α |
    |---|---|---|---|---|---|---|---|
    | 40 | workspace, GDN | 0.500 | 0.670 | 0.500 | 0.0000 | — | 0.0000 |
    | 44 | workspace, GDN | 0.500 | 0.712 | 0.500 | 0.0000 | — | 0.0000 |
    | 48 | steering, GDN | 0.500 | 0.688 | 0.500 | 0.0000 | — | 0.0000 |
    | 49 | GDN | 0.505 | 0.700 | 0.497 | 0.0040 | 0.099 | 0.0228 |
    | 50 | GDN | 0.503 | 0.676 | 0.502 | 0.0125 | 0.159 | 0.0622 |
    | 51 | attn | 0.476 | 0.644 | 0.462 | 0.0192 | 0.070 | 0.1283 |
    | 52 (ws) | GDN | 0.479 | 0.667 | 0.493 | 0.0261 | 0.081 | 0.1574 |
    | 53 | GDN | 0.477 | 0.649 | 0.497 | 0.0293 | 0.088 | 0.1700 |
    | 54 | GDN | 0.484 | 0.660 | 0.503 | 0.0330 | 0.089 | 0.1858 |
    | 55 | attn | 0.451 | 0.648 | 0.486 | 0.0357 | 0.061 | 0.2237 |
    | 56 (ws) | GDN | 0.446 | 0.660 | 0.491 | 0.0401 | 0.063 | 0.2354 |
    | 57 | GDN | 0.438 | 0.650 | 0.481 | 0.0436 | 0.060 | 0.2519 |
    | 58 | GDN | 0.460 | 0.658 | 0.481 | 0.0460 | 0.049 | 0.2623 |
    | 59 | attn | 0.415 | 0.656 | 0.455 | 0.0560 | 0.033 | 0.3832 |
    | 60 (ws) | GDN | 0.434 | 0.636 | 0.438 | 0.0639 | 0.026 | 0.4270 |
    | 61 | GDN | 0.415 | 0.660 | 0.451 | 0.0749 | 0.022 | 0.4868 |
    | 62 | GDN | 0.450 | 0.658 | 0.439 | 0.0928 | 0.011 | 0.5728 |
    | 63 | attn | 0.448 | 0.677 | 0.444 | 0.1219 | -0.002 | 0.7700 |

    **STOP CLAUSE (layers ≤ 48 above their shuffle 95th percentile):**
    **did not fire** — no layer ≤ 48 is above null (all 49 are at exactly 0.500 with bit-identical residuals); hook placement and mask are as declared.

    **LEAK, unsigned only (reward masks):** π_d(M1) = 0/24 = 0.000, π_d(M2) = 0/24 = 0.000 — no restricted-argmax flip under either reward mask; |Δ(logit_a − logit_b)| vs M0: M1 median 0.108, mean 0.099, max 0.259; M2 median 0.096, mean 0.108, max 0.239 (24 sessions each; the full value lists are in the artifact). For scale: g3's dose-0.20 leak on v1-template prefixes was max 0.5368 / mean 0.2266 in the same units.

    **SIGNED pseudo-shift, random masks only** (shift of logit(label whose
    rounds carried r+) − logit(other), relative to the shadow): M3 mean +0.0082 (sd 0.0469; 14 positive / 10 negative of 24); M4 mean +0.0019 (sd 0.0524; 11/13) — the mechanical pseudo-shift of a norm-matched random direction at the config of record is within ±0.01 logit on average with a per-session sd of ~0.05.

    **FLAGS (grep `FLAG:`).**
    - **FLAG: POST-HOC — the echo IS readable when the target is the injected
      SIGN OF THE LAST FORCED ROUND.** Rule 11: a post-hoc relabelling of the
      same Stage A rows (no new forward, no reward-mask DV, nothing signed
      toward a label), not a §3.1 registered readout; it licenses a
      pre-registration, never a verdict. Target = +1 for (M1, forced_end =
      pos) and (M2, forced_end = neg), else −1 — identical text within a
      session, opposite labels within a session, 11/13 across sessions. The
      identical LOSO probe reads it above null at every layer from 50 to 63:
      AUC 0.866 (L50), 0.972 (L51), 0.967 (L52), 0.983 (L53), 0.977 (L54), 0.967 (L55), 0.972 (L56), 0.967 (L57), 0.965 (L58), 0.941 (L59), 0.938 (L60), 0.934 (L61), 0.882 (L62), 0.845 (L63), against shuffle 95th percentiles of 0.63–0.69;
      L49 0.674 vs 0.682 (not above null); layers ≤ 48 exactly
      0.500. **The random-direction comparator reads its own last-round sign
      almost as well:** 0.858 (50), 0.918 (51), 0.931 (52), 0.939 (53), 0.929 (54), 0.906 (55), 0.891 (56), 0.915 (57), 0.903 (58), 0.814 (59), 0.832 (60), 0.780 (61), 0.840 (62), 0.747 (63). Descriptive reading, no bar: at the first free
      choice the residual above the steering layer carries a linearly
      decodable memory of WHICH SIGN was injected on the nearest forced round
      (under strict alternation, equivalently the first), peaking around
      L51–L58 and decaying toward L63; it is not axis-specific; and it is
      invisible to the registered M1-vs-M2 target because e2a's alternating
      forced order [f, −f, f, −f] makes that target's sign depend on the
      start pole (13/11 here) — the class-mean differences cancel. Which
      round(s) carry it and how it decays with distance is Stage B's R1..R4
      retention curve. Artifact
      [`stageA_posthoc_lastround.json`](data/echo/stageA_posthoc_lastround.json),
      raw [`_recon_echo_stageA_posthoc`](results/raw/2026-09-05_recon_echo_stageA_posthoc.txt).
    - **FLAG: the registered target and the surviving fraction are
      sign-ambiguous under alternation by construction** — the same
      cancellation makes the class-mean surviving fraction read ≤ 0.12 while
      the per-session paired norm reaches 0.77 × 2α at L63.
    - **FLAG: e2a generation-side 512-token window** (§1e) — 270 of 1,894
      archived generations were produced with the state over the whole tail
      window; free3–free5 only; DV read untouched.
    - **FLAG: the content-class screen has no RESULTS entry** (§1g); the
      09-05 handoff's "in the log" is wrong for that item.
    - **FLAG: `PREPRINT-*.md` / `BLOG-*.md` are absent from the repo** though
      CLAUDE.md places them at root (§1b).
    - **FLAG: H1-u is not a prefix-steered/choice-unsteered precedent** —
      its reads were state-present at every position (§1c).
    - **FLAG (record hygiene; verifier-found, Code-verified):**
      `data/e2a/g3prime_kl.jsonl` holds 360 rows but 311 distinct (arm,
      session, choice) keys — 49 duplicate rows over 38 keys (smoke rows
      re-appended), all kl = 0.0; "360/360" counts rows, not distinct
      verified reads.

  - **PROHIBITION, honoured in code.** `signed_pseudo_shift` refuses M1/M2;
    no first-choice Δ on a reward mask is computed, printed or written
    anywhere in `scripts/recon_echo.py` or the artifacts; the raw per-mask
    restricted logits are recorded as the block requires and nothing is
    derived from them under M1/M2 beyond the unsigned π_d and |shift|.
  - **Caveat line.** The archived texts were generated on the cached round
    path (first-token licence); every recon forward is uncached — immaterial
    to echo readability, noted for the record. Stage B waits for its go.
  - **Committed with explicit paths:** `valence_core/echo/{__init__,
    maskedprefix, spans, probe}.py`, `valence_core/adapters/{base,
    qwen_mlx}.py` (`forward_last`), `scripts/recon_echo.py`, `.gitignore`
    (`data/echo/` JSON allowlist, tested both directions), `data/echo/*.json`,
    the five raw logs, this entry.

- 2026-09-03 — **RECORD HYGIENE: my entry date stamps ran AHEAD of true UTC,
  by one day from `a9e6a74` onward. Correction table below, verified against
  `git log` rather than repeated from the request. NO existing entry is
  edited and NO file is renamed — the stamps stand as written and this entry
  is the key to them. PROVENANCE: my dates came from the DESIGN BLOCK
  HEADERS, not from my own clock, and on at least one occasion I noticed the
  two disagreed and deferred to the block.**
  (Stamp verified at write time: `date -u` → **Thu Sep 3 04:38:02 UTC 2026**.
  Authoritative source for every row: `git log --date=format:'%Y-%m-%d %H:%M'`
  with `TZ=UTC`.)

  - **The two rows the request names, confirmed exactly.**

    | commit | true commit time (UTC) | local | stamped |
    |---|---|---|---|
    | `c638289` D3 scoring released | **2026-09-02 16:57:58** | 09-02 12:57 EDT | 2026-09-03 |
    | `1bdf16c` e2d closure completion | **2026-09-03 01:25:15** | 09-02 21:25 EDT | 2026-09-04 |

  - **The full audit, because partial hygiene is worse than none.** Every
    RESULTS entry I wrote this session, against the true UTC date of the
    commit that carried it:

    | entry stamp | commit(s) | true UTC | |
    |---|---|---|---|
    | 2026-09-01 (D1 stop; AMENDMENT 1; D1 acceptance; oracle incident) | `70995c0`…`4ca10e1` | 2026-09-01 02:10–03:52 | **correct** |
    | 2026-09-02 (D2 stopped, power fault) | `a9e6a74` | 2026-09-01 09:48 | **+1 day** |
    | 2026-09-02 (S1 k=1 re-read) | `7dad4d6` | 2026-09-01 12:23 | **+1 day** |
    | 2026-09-02 (D2 sessions + read) | `a274ecd` | 2026-09-01 19:18 | **+1 day** |
    | 2026-09-02 (f = 0.10 apparatus read) | `39d0ff7` | 2026-09-01 19:25 | **+1 day** |
    | 2026-09-02 (D2 qualification rung fails) | `cd86e49` | 2026-09-01 22:17 | **+1 day** |
    | 2026-09-03 (disposition + ADDENDUM-j1) | `520f62c` | 2026-09-02 01:59 | **+1 day** |
    | 2026-09-03 (D3, fired gate) | `e58dfca` | 2026-09-02 08:26 | **+1 day** |
    | 2026-09-03 (DISPOSITION-2) | `e492468` | 2026-09-02 09:32 | **+1 day** |
    | 2026-09-03 (D3 scoring) | `c638289` | 2026-09-02 16:57 | **+1 day** |
    | 2026-09-04 (closure completion) | `1bdf16c` | 2026-09-03 01:25 | **+1 day** |

    The break is at `a9e6a74`: everything before it is right, everything from
    it onward is one day fast. **Eleven entries, one systematic offset**, not
    eleven independent slips.
  - **Two document status lines carry the same offset and are ALSO left
    unedited**, recorded here instead: PROPOSAL-j's *"v1.2 — amendment 2
    appended 2026-09-02"* was committed `ce3ff84` at **2026-09-01 07:46 UTC**,
    and *"v1.3 — addendum j1 appended 2026-09-03"* was committed `520f62c` at
    **2026-09-02 01:59 UTC**. A proposal's status line is part of a locked
    document; editing one to fix a date is a worse trade than an index entry.
  - **WHERE MY DATES CAME FROM — the question that decides the seat.**
    **The design block headers.** Each block arrives headed
    `DESIGN → CODE (via Jason) — <date> (UTC)`, and I stamped entries to match
    the block I was executing, so the entries inherited the headers' dates.
    - **I did not consult `date -u` even once before this entry.** That is
      the mechanical gap and it is mine.
    - **And I had a divergent signal that I noticed and set aside.** My own
      environment reported the date at session start and on each rollover.
      When a block headed `2026-09-03 (UTC)` arrived while my environment
      said 2026-09-02, I reasoned explicitly — in-thread, in as many words —
      that "the repo has been using the block's dates" and stamped 09-03. The
      same thing happened again for 09-04. So this is not a case of having no
      signal; it is a case of having one and resolving it toward the header.
    - **Both facts are on the record so the seat is design's to assign.** The
      headers ran ahead of UTC; Code had a truer local signal, preferred the
      header, and never checked the authoritative one. I am not assigning the
      ledger item to either seat — that is not mine to do — but I would not
      want the first fact recorded without the second.
  - **Why the offset is harmless to the science and not to the record.**
    Nothing dated is a measurement: every figure in every entry is tied to a
    committed artifact and a commit hash, and the hashes are unambiguous. What
    the offset damages is **sequence** — an entry stamped 09-04 sits after one
    stamped 09-03 in a reader's mind even when they were written four hours
    apart the same evening — and the ability to line entries up against the
    box's clock, the pod billing, or anything else timestamped externally.
    **`git log` is authoritative and disagrees with the entry heads by one
    day from `a9e6a74`.**
  - **Standing fix, adopted now.** `date -u` before every stamp — not the
    block header, not my environment's reminder, not inference from the
    previous entry. The block header records when the block was *written*,
    which is a different fact from when the work was *done*, and only the
    second belongs in a dated log entry.
  - **Watermarks name entry TITLES, not dates** (already true of the 09-04
    handoff). Raw-log filenames `2026-09-03_e2d_d3_scoring.txt`,
    `2026-09-04_e2d_d2_allrounds_rescore.txt`,
    `2026-09-04_e2d_closure_valuescheck.txt` and
    `HANDOFF-2026-09-04-design.md` **keep their names** — they are referenced
    by name from committed entries, and renaming them would break those links
    to fix a cosmetic offset this entry already documents.

- 2026-09-04 — **e2d CLOSURE COMPLETION — item 1 DELIVERED, and it FIRES ITS
  OWN FLAG CONDITION: the licensed D2 all-rounds paired rescore returns
  **+0.0149**, which DISAGREES IN SIGN with the clean-set **−0.0121**. Not
  averaged, per the block. And the closure text is HELD, not committed: a
  13-agent adversarial values-check over the committed artifacts returned
  **7 of 12 glosses OVERSTATED**, every one of which I then re-verified by
  hand. Code does not reword design prose, and does not commit a closure
  carrying claims its own check flags.**
  ([`d2_scores_allrounds.json`](data/e2d/d2_scores_allrounds.json),
  [`dose_paired_d2_d3_allrounds.json`](data/e2d/dose_paired_d2_d3_allrounds.json);
  raw [`_allrounds_rescore`](results/raw/2026-09-04_e2d_d2_allrounds_rescore.txt),
  [`_valuescheck`](results/raw/2026-09-04_e2d_closure_valuescheck.txt).
  **e2d's closure decision itself is unaffected** — Q2 and Q3 failed, the
  run-dose rule returned STOP, SCOPED, and nothing below reopens it.)

  - **ITEM 1, the licensed rescore — integrity gate first.** The rescore had
    to reproduce D2's committed CLEAN paired figure before its all-rounds
    block could be trusted as the same measurement under a different filter.
    It does, to ten decimals: **+0.1029633631, n = 27**, against the committed
    +0.1029633631, n = 27. Written to a NEW path; `d2_scores.json` untouched.
  - **THE FIGURE, AND THE FLAG.** D2→D3, marker paired by session index:

    | filter | D2 | D3 | shared n | paired change | sign test | unpaired |
    |---|---|---|---|---|---|---|
    | **clean** | +0.1030 | +0.1411 | 20 | **−0.0121** | 11/20, p = .41 | +0.0382 |
    | **all rounds** | −0.0307 | +0.0372 | 24 | **+0.0149** | 14/24, p = .27 | +0.0679 |

    **The two filters put the point estimate on opposite sides of zero.**
    Neither is significant — p = .41 and p = .27 — so the reading that
    survives both is *no detectable change from 0.20 to 0.30*, not a
    direction. **Not averaged**, per item 1. The composition artifact
    reproduces under both filters: unpaired reads +0.038 and +0.068, paired
    reads −0.012 and +0.015.
  - **THE VALUES-CHECK, and why the closure text is held.** Thirteen agents,
    each given one claim and instructed to REFUTE it, reading the committed
    artifacts directly; plus a critic asked what nobody was assigned. Result:
    **6 CONFIRMED, 6 PARTIAL, 0 refuted outright — and 7 glosses OVERSTATED.**
    Every finding below I re-verified myself before recording it, because one
    agent also reported session counts (D2 35 M, D3 27) that are simply wrong
    — the artifacts hold **D2 64 = M32/R16/S16 and D3 24 = M24, no duplicate
    keys.** Agent output is evidence, not testimony.
    1. **"the displacement comparator at .534"** — CONFIRMED for D2, but D3
       ran M-only under ADDENDUM-j1 and **has no comparator at all**. The
       singular phrasing reads as covering both doses. *Verified: `AUC_R`
       exists in `d2_scores.json` and appears nowhere in `d3_scores.json`.*
    2. **"unchanged by excising the readout (dilution excluded)"** —
       OVERSTATED. The contexts differ by **2.3×** at 0.30 (excised +0.141 vs
       in situ +0.062) and the gap **flips direction** across dose (+0.024 at
       0.20, −0.079 at 0.30). At 0.30 the context gap is **larger than the
       in-situ imprint itself.** What is invariant is the *below-bar
       conclusion*, not the imprint. Dilution is neither demonstrated nor
       excluded.
    3. **"a quarter of its short-context value (excised +.103 vs V1's
       +.408)"** — the arithmetic holds (0.252) but the two are **different
       channels**: V1's +0.408 is a **state-live read at the probe**; e2d's
       is a **no-injection read of the text the state produced**. The
       entry's own caveat names instrument transfer; the deeper problem is
       that this is not the same measurement divided.
    4. **"coherence degrades monotonically with dose"** — the three point
       estimates are ordered, but **only one of four steps is resolved**:
       read .10→.20 **p = .011**; audit .10→.20 p = .41, audit .20→.30
       p = .10, read .20→.30 p = .10. **On the 24 shared indices — the
       paired basis release condition 4 requires — neither .20→.30 step is
       resolved** (audit p = .15, read p = .30).
    5. **And the rise is not axis-specific, which the closure does not say.**
       At f = 0.20 the **random** arm degrades at **7/156 = .0449** against
       the axis arm's **7/300 = .0233** — twice the rate, in the arm that
       carries no axis (R > M one-sided p = .16, unresolved, but pointing the
       wrong way for an axis reading). The wholly unsteered S arm is
       **0/151**. Degeneracy tracks *displacement*, not the reward direction.
    6. **The .20→.30 read-marked rise is ONE SESSION.** On shared indices the
       net change is **+4 marks**, and index **s12 alone moves +7** (0/10 →
       7/10) while s19 moves **−4** and s18 **−1**. Two further indices —
       **s1 and s5** — sit at **10/10 at both doses** and carry **58.8%** of
       all marks on shared indices, contributing no dose information at all.
    7. **"flat from 0.20 to 0.30"** — should be *no detectable change*. With
       n = 20 and sd 0.33 the paired interval spans roughly ±0.15, which
       covers the 0.158 bar in both directions; the data cannot certify
       flatness, only fail to detect movement. **My own D3 entry carries the
       same overreach** — "the marker delta does not move between 0.20 and
       0.30" — and should read "shows no detectable movement".
    8. **"first-pick break rate unmoved (1/23)"** — unmoved only *within*
       e2d (D2 1/30 = .033, D3 1/23 = .043). Across the ladder it is not:
       **e2a's pooled rate is 30/184 = .163**, four times e2d's, and its
       reward arm alone is 16/102 = .157. The habit is *stronger* in e2d than
       in e2a, which is a different observation from "unmoved".
    9. **"the free operant was never administered"** — the *verdict-tier
       campaign* never ran. The free operant itself ran **537 times** across
       D1–D3 (42 + 357 + 138 insulated choice reads, every one at KL = 0).
       And "at any coherently deliverable dose" reaches past the evidence:
       **nothing above 0.30 was run**, and at 0.20 the apparatus was
       *coherent* — Q1 passed at 3/32, p = .878 — so the failure was one of
       legibility, not coherence.
  - **WHAT I AM NOT DOING.** Rewording the closure. The text is the design
    instance's, the seven glosses are its to resolve, and Code rewriting a
    closure statement would be exactly the self-adjudication the two-instance
    workflow exists to prevent. The evidence for each is above and in the
    artifacts; the reworded clauses the check proposed are in
    [`closure_valuescheck.json`](data/e2d/closure_valuescheck.json).
  - **WHAT THE CHECK DID NOT DISTURB.** Every *figure* in the closure text
    reproduces: readability .574 / .613 against .70 (and the 10th-percentile
    conjunct fails too, at .524 / .526 — the closure is conservative there);
    the 0.158 bar and every cell below it; the composition capture (+0.0382
    unpaired vs −0.0121 paired); the cost ratio 2.57 / 0.54 s per forward;
    the 0.10-anchor caveat. **The closure's conclusion is not in question —
    only the words carrying it.**

- 2026-09-03 — **e2d D3 SCORING, released under disposition-2 and delivered:
  the two-context dose table. Δ+ stays below the 0.158 bar at every dose in
  both contexts; readability is FLAT across the whole range (.583 / .574 /
  .613 against a .70 bar); and the D2–D3 dose comparison, computed PAIRED as
  release condition 4 requires, REVERSES the unpaired reading.**
  ([`d3_scores.json`](data/e2d/d3_scores.json),
  [`d3_excision_check.json`](data/e2d/d3_excision_check.json),
  [`dose_paired_d2_d3.json`](data/e2d/dose_paired_d2_d3.json); raw
  [`2026-09-03_e2d_d3_scoring.txt`](results/raw/2026-09-03_e2d_d3_scoring.txt).
  **Every figure below carries the D3 gate firing as a caveat**
  (11/233, p = .0078, adopted as a measurement); **e2d's closure is
  unconditional on all of it.**)

  - **THE PAIRED COMPARISON REVERSES THE UNPAIRED ONE — release condition 4
    earning its keep.** Marker Δ+, M arm, clean set, 20 shared session
    indices:

    | contrast | value |
    |---|---|
    | unpaired difference of means, 0.20 → 0.30 | **+0.0382** — reads as a rise |
    | **paired on the same session indices** | **−0.0121** |
    | sign test | 11/20, p = .41 |
    | sign-flip permutation | p = .57 (B = 10,000, seed 20260902) |

    The apparent dose effect is a **composition effect**: different sessions
    survive exclusion and cleaning at each dose (D2 n = 27, D3 n = 20, 20
    shared). Paired on the same content, the marker delta does not move
    between 0.20 and 0.30. This is exactly the property disposition-2 banked
    — session content is keyed on the session **index**, so the same index is
    the same session at both doses — and it is why the pairing was made a
    release condition rather than an option.
  - **TWO-CONTEXT DOSE TABLE (ADDENDUM-j1 (a)).** Marker Δ+, M arm, paired by
    session, clean set. Bar = 0.5·G = **0.1578**.

    | dose | excised | in situ | n | |
    |---|---|---|---|---|
    | 0.10 | — | — | 4 | **n = 4 sessions, NOISE.** And D1's marker was the **pooled** estimator, not the paired one — its −0.2394 is a different statistic and is **not** comparable down this column |
    | 0.20 | **+0.1030** | **+0.1270** | 27 | both below bar |
    | 0.30 | **+0.1411** | **+0.0619** | 20 | both below bar |

    - **Every cell is below the bar.** Whatever the context and whatever the
      dose, the marker never reaches the registered magnitude.
    - **The two contexts disagree in MAGNITUDE and their gap flips sign
      across dose** — in situ exceeds excised at 0.20 (+0.127 vs +0.103) and
      falls well short of it at 0.30 (+0.062 vs +0.141). Both remain
      positive, so no sign flip in either.
    - **In situ is consistently the noisier readout**, as it was on D2:
      SD 0.759 against 0.435 at 0.30, and 0.710 against 0.399 at 0.20. The
      longer context adds variance without adding signal, at both doses.
    - **The 0.10 anchor is not a data point.** Four sessions, and a different
      estimator. It is in the table because the block asked for it and
      flagged it as noise; it should not be drawn as the left end of a curve.
  - **READABILITY IS FLAT ACROSS THE WHOLE DOSE RANGE, and this is the
    substantive result.** k = 2 resampled median, M arm:

    | dose | v2 ∧ read-clean | v2-clean only | all rounds |
    |---|---|---|---|
    | 0.10 | — | .5833 *(n = 4, noise)* | — |
    | 0.20 | **.5744** | .6083 | .6348 |
    | 0.30 | **.6129** | .6114 | .6296 |

    Bars are median ≥ .70 and 10th pct ≥ .60; D3's 10th percentiles are .526
    and .522. **Tripling the dose from 0.10 to 0.30 moves readability from
    ~.58 to ~.61 — nowhere near the bar.** D2's Q2 failure was therefore not
    a fact about 0.20; it is a fact about this channel on this apparatus. The
    scope sentence e2d closed on is stronger for it.
    - At D3 the two clean sets agree (.6129 vs .6114), unlike D2 where the
      read-marks moved the figure .608 → .574. No AUC_R at D3: ADDENDUM-j1
      registers it M-only, so there is no random arm to compare against — a
      real limitation of the descriptive rung, not an omission.
  - **Degeneracy rises with dose while readability does not.** M arm, all
    rounds: audit-degenerate **.0000 → .0233 → .0472**; read-marked
    **.0000 → .1133 → .1545**. The dose buys degradation without buying
    legibility — which is the shape §2 D3 was sent to find, and it is what
    the fired gate measured.
  - **AMENDMENT 2 (v) at 0.30.** On the valid domain b₊ = 1/10, bₛ = 0/13,
    and the weighted identity returns **+0.1087**, which is Δ_first (14/23)
    **exactly** — the third tier in a row where it reproduces. Descriptive,
    no criterion.
    - **Strict alternation decays with dose while the first pick does not.**
      e2a **.840** → D2 **.690** → D3 **.522**, against a first-pick
      habit-break rate that stays near zero throughout (D3: 1/23). The habit
      holds at the opening choice and erodes later in the session as dose
      rises. Registered secondary is the first-pick rate and it shows
      nothing; the decay is descriptive and unregistered.
  - **ONE FIGURE THE RELEASE CONDITIONS ASK FOR AND I CANNOT SUPPLY.** The
    D2–D3 paired comparison exists for the clean set only. D2 was scored
    **before** the all-rounds paired estimator existed — it was added in the
    disposition-2 commit, under the release condition itself — so
    `d2_scores.json` carries no all-rounds per-session block. D3 has both.
    Recovering D2's would require rescoring its marker, **≈ 1.1 h**.
    **Offered, not assumed, and not silently skipped.**
  - **Cost.** D3 scoring 1.40 h (marker 25 min for 2,796 forwards; ladders
    ≈ 59 min) plus in-situ 2.00 h — **3.4 h total**, against ADDENDUM-j1's
    ≈ 0.5 h scoring estimate. The in-situ half runs at 2.57 s/forward against
    0.54 s excised, the same ratio the D2 excision check measured.

- 2026-09-03 — **e2d D3 GATE ADJUDICATION (DISPOSITION-2). The
  `round_degeneracy` firing is ADOPTED AS A MEASUREMENT, not a fault: the
  registered D3 measurand crossing a standing campaign-hygiene tolerance.
  Apparatus intact, D3's data usable for their registered descriptive
  purpose, held scoring RELEASED under four conditions. Design seat takes
  slip (11).**
  (Design instance 2026-09-03 UTC, PI ratified 2026-09-03. The fired gate and
  what it read are in the D3 entry below; ADDENDUM-j1, PROPOSAL-j v1.3.
  **e2d's closure remains unconditional.**)

  - **1. The firing, adopted as a measurement.** 11/233 = 4.72%, exact
    binomial **p = .0078** against p0 = 0.02; steered **7/122 = .0574** fires
    alone, unsteered **4/111 = .0360** is silent. The reading of record: this
    is *"the registered D3 measurand — the degeneracy curve toward the
    overdose regime — crossing the standing campaign-hygiene tolerance."*
    - **The bar's declared justification, quoted** (`valence_core/e2d/
      config.py:177–181`): *"Measured class: e2a's 0.10 archive is the
      declared healthy rate. Binds by exact binomial at every scale
      (rule 21)."*
    - **Its call site, quoted** (`scripts/e2d_sessions.py:320`):
      `fired = check_bars(bars, {"round_degeneracy": (n_degen, n_rounds), …})`
      — evaluated once, after the campaign, over `n_degen` and `n_rounds`
      counted across **all** rounds of all sessions. The `domain="all"` in the
      declaration and the all-rounds counts at the call site are the same
      decision made twice, which is why nothing in the harness caught it.
  - **2. SLIP LEDGER, design seat, item (11).** *ADDENDUM-j1 re-licensed D3
    M-only, after D2's session-level displacement finding abolished the only
    unprovoked domain, without re-domaining the degeneracy monitor — leaving
    the bar nothing to bind on but the provoked phenomenon. The
    pause-and-adjudicate path that resulted is the correct conversion; the
    failure to pre-declare it is the slip.*
  - **3. Apparatus status: INTACT.** KL **138/138 exactly 0.0**; **24/24**
    sessions reconstructed with all seed streams matched; ADDENDUM-j1 (b)'s
    pause bar reached, silent, and **verified firable at its threshold**;
    cap-hits **0/233**; the degeneracy monotone across dose and mode-locked by
    session index. **D3's data are usable for their registered descriptive
    purpose.**
  - **4. Release conditions, binding on everything that follows.** The held
    scoring runs; **every D3 figure is reported on the clean set AND all
    rounds**, each carrying the firing as a caveat; and the **D2–D3 dose
    comparison is computed PAIRED by session index** — the shared-content
    property banked as *a strength for the comparison, a constraint on its
    error bars, and an unregistered design property named here*.
  - **5. Banked (ledger 23).** The **3× content-vs-audit ratio** — the audit
    of record sees about a third of what the read sees; the **NULL_RESPONSE
    family** (three forms — `[MENTAL_BLOCK]`, the literal `None`, a bare
    ` ``` ` fence — **all in unsteered rounds**) as a candidate class for the
    scorer_v3 spec; and `below_d2_floor` coverage at n = 24.
  - **6. Proposed rule annotations — PI APPROVAL REQUIRED, NOT APPLIED.**
    Recorded here as proposals only; CLAUDE.md is unchanged and stays
    unchanged until the PI says otherwise.
    - **(a) rule 2** — *a first-token kernel gate licenses first-token reads,
      not generation; T-step identity is its own gate.*
    - **(b) rule 21** — *degeneracy bars at dose-characterization rungs bind
      on an unprovoked domain; where none exists by design, the bar is a
      pause-and-adjudicate trigger, declared as such.*
    - Both are annotations this session's own evidence produced — (a) from the
      T-step checks at 0.20 and 0.10, (b) from this gate. **Code does not
      apply ledger changes**; they are flagged, not folded.

- 2026-09-03 — **e2d D3 — all 24 sessions RAN, but ACCEPTANCE FAILS on a FIRED
  GATE: `round_degeneracy 11/233, exact binomial p = .0078 < .05 vs p0 = 0.02`.
  Escalated, not adjudicated. The marker and ladder scoring is HELD pending
  the gate's disposition, so the two-context dose table is not in this entry.
  What the run did produce, model-free, is TWO monotone dose–response curves —
  and the fired gate is one of them.**
  ([`data/e2d/d3_sessions.json`](data/e2d/d3_sessions.json),
  [`d3_read_marks.json`](data/e2d/d3_read_marks.json); raw
  [`2026-09-03_e2d_d3.txt`](results/raw/2026-09-03_e2d_d3.txt).
  ADDENDUM-j1, PROPOSAL-j v1.3. **e2d's closure is unconditional on this
  entry.**)

  - **What passed.** KL **138/138 reads exactly 0.0**; `statepresent` absent at
    every read; **24/24** sessions reconstruct byte-for-byte with all 24 seed
    streams matched; no traceback. 2.37 h, 355 s/session, f = 0.30,
    α = 30.9030, uncached, M-arm only, checkpointed.
  - **ADDENDUM-j1 (b)'s pause bar was REACHED and stayed silent for the right
    reason.** It evaluates once, when the 8th M session lands: **0 of the
    first 8 excluded** against a bar of ≥ 4. Verified after the fact that the
    same call fires at 4 — so its silence is a measurement, not a skip
    (trap 5).
  - **THE FIRED GATE, and I am not adjudicating it.** `round_degeneracy` is a
    rule-21 binomial bar, `domain="all"`, p0 = 0.02 declared from e2a's 0.10
    archive. At f = 0.30 it reads **11/233 = 4.72%, p = .0078**.
    - **Split by whether the round was steered**, which is the split rule 21
      cares about:

      | domain | rate | p vs p0 = .02 |
      |---|---|---|
      | steered (+axis) | 7/122 = .0574 | **.0117 — fires** |
      | unsteered (sham within M) | 4/111 = .0360 | .1830 — silent |
      | **all (what the bar read)** | **11/233 = .0472** | **.0078 — FIRED** |

    - **The rule-21 observation, offered as an observation.** Rule 21 says
      *"stimulus-provoked degeneracy gates on unprovoked domains."* This bar's
      domain is `all`, which at a dose–response rung includes the rounds the
      dose is there to provoke — so it can fire on its own stimulus, which is
      the failure mode rule 21 and rule 28(b) both name. On the unprovoked
      half it does not fire.
    - **And D3 has NO clean unprovoked domain to move it to.** The M arm's
      sham rounds are not one: D2 established that degeneracy appears in the
      unsteered rounds of steered sessions (sham(M) 3/89, sham(R) 3/45) while
      a wholly unsteered arm showed **0/151**. A clean unprovoked domain needs
      an S arm, and ADDENDUM-j1 registers D3 as M-only. **That is a
      consequence of the design, not a defect in the run**, and it is why the
      bar's disposition is a design-instance call rather than a Code one.
    - **What I have NOT done:** treated the firing as expected-and-therefore-
      fine. It may well be exactly what §2 sent D3 to measure — but saying so
      is adjudicating a fired gate, and that is not Code's to do.
  - **TWO DOSE–RESPONSE CURVES, both monotone, both model-free.** M arm, all
    rounds:

    | dose | audit-degenerate (v2) | read-marked (content-shaped) |
    |---|---|---|
    | 0.10 (D1) | 0/40 = **.0000** | 0/40 = **.0000** |
    | 0.20 (D2) | 7/300 = **.0233** | 34/300 = **.1133** |
    | 0.30 (D3) | 11/233 = **.0472** | 36/233 = **.1545** |

    The 0.10 anchor is **n = 4 sessions and is noise**, as the block notes.
    Between 0.20 and 0.30 both rates rise. **Content-shaped degeneracy runs
    about 3× the audit-shaped rate at every dose where either is nonzero** —
    the instrument of record sees a third of what is there.
  - **A PAIRING nobody registered, and it changes how the curve reads.**
    Session content is keyed on the session INDEX — `session_rng(f"e2d-M",
    idx)` fixes the task sequence and every generation seed — and D2 and D3
    use the same indices. So the same session index produces the same
    degeneracy mode at both doses: **s1's task-echo attractor, s5's "Great,
    I'll …", s9 free0's `[MENTAL_BLOCK]`, s11's "Good! … is a good fit"
    wrapper all recur at 0.30 at the same round positions.** D2 and D3 are
    therefore **paired, not independent** draws. That is a strength — the
    dose comparison is within-session — and a caution: the curve is not two
    independent samples, and its error bars are not the ones independence
    would give.
  - **The rule-25 read: 36 marks over 36 rounds of 233 = 15.5%** (forced
    16/95 = 16.8%, free 20/138 = 14.5%), across 7 of 24 sessions.
    task-echo 14, preamble-without-content 14, stuck-attractor 7,
    wrong-task 1. Exclusions: **1/24 forced scope** (s17,
    `audit:frame:evaluation session@forced2`) against **7/24 strict** — the
    scope gap again, and larger in proportion than D2's.
  - **A NEW OUT-OF-CLASS MODE, and an old one recurring.** **M s12 emits a
    bare ` ``` ` code fence as its entire response for eight consecutive
    rounds.** The repeats are marked `stuck_attractor` — they do repeat
    forced0's text — but **forced0 itself is a null response**, which is the
    same family as D2's `[MENTAL_BLOCK]` and `None`, and which the four
    closed classes still do not name. **`[MENTAL_BLOCK]` recurs in D3 at the
    identical session and round index (M s9 free0).** The fifth-class flag
    from D2 stands and now has a third form: bare fence, bracketed refusal,
    literal `None`.
  - **Counters (rule 23, all 24 sessions):** termination 2 (M), cap-hits
    **0/233**, audit-degenerate 11, **lexical 0** (against 4 in D2 — no
    roster-tag emission at all at this dose), post-choice degeneracy 10,
    low-label-mass 4/138 = 2.9%.
  - **Coverage shortfall, recorded in the artifact.** M-arm task_id coverage
    is **pos 16 / neg 15** against the ≥ 16-per-class floor. The floor is a
    **D2** precondition (§2 states it inside the D2 paragraph) and D3
    registers none — and at n = 24 it is **unreachable**: per-session task
    sequences are keyed on the session index and do not move with the draw
    seed, so the seed only flips pole assignment. **4,000 seeds searched,
    zero reach 16/16, best 16/15.** The registered seed 20260902 stays;
    `below_d2_floor` and the reason are in the artifact. **D3's readability
    figure, when it is computed, does not carry D2's task-disjointness
    guarantee.**
  - **WHAT IS HELD, and why.** The marker readout in both contexts
    (ADDENDUM-j1 (a)) and the ladders are **not run**. A fired gate routes to
    a design-instance disposition, and whether D3's figures are usable at all
    turns on that disposition — so spending ≈ 2.5 h of scoring (≈ 28 min
    excised + ≈ 2 h in situ, at the 2.56 s/forward the D2 excision check
    measured) ahead of it would be assuming the answer. **The two-context
    dose table the block asks for is therefore owed, not delivered.** On a
    disposition it is one command.

- 2026-09-03 — **e2d DISPOSITION: the registered run-dose rule's STOP, SCOPED
  is ADOPTED. e2d closes unopened — the verdict tier and LOCK-j do not run.
  D3 runs as registered, licensed by ADDENDUM-j1, descriptive only and with
  no power to reopen the closure. PROPOSAL-j → v1.3.**
  **INCOMPLETE AS FILED: the disposition's items 2–5 never reached Code.**
  (Item 1 is recorded below verbatim as amended. PROPOSAL-j v1.3;
  D2's result at [`d2_analysis.json`](data/e2d/d2_analysis.json).)

  - **Item 1, ratified and amended (the whole of what arrived).** *"The
    registered run-dose rule's STOP, SCOPED is ADOPTED. e2d closes unopened;
    the verdict tier and LOCK-j do not run. D3 runs as registered, licensed
    by ADDENDUM-j1 (PI decision 2026-09-03), descriptive only: no
    qualification role, no run-dose role, no verdict role, and the closure
    stands regardless of its figures."*
  - **THE GAP, flagged rather than filled.** The block reads *"DISPOSITION
    entry as sent, with item 1 amended … Items 2–5 unchanged."* **No such
    entry was ever sent to this thread, and none exists in the repo** — the
    only untracked design documents are the five trap-2 files, none of which
    is a disposition. So items 2–5 are unknown to Code, and this entry
    records item 1 alone. **They are not guessed and no placeholder stands in
    for them**; when they arrive the entry is completed in place or by a
    successor entry, design's choice. Nothing downstream is blocked: D3 is
    licensed by ADDENDUM-j1, which arrived complete.
  - **What the closure rests on**, restated so the entry is readable without
    the D2 entry beside it: Q1 passed (3/32 = 9.4%, p = .878 vs p0 = .15),
    Q2 failed on every set reported (criterion set median **0.574**, 10th pct
    0.524, against .70/.60), Q3 failed on magnitude (**Δ+ = +0.103** against
    bar **0.158**, and Δ+ > 2·|Δ_R| also failed). The scope sentence §2
    registered for exactly this outcome: *the weak-state boundary is not
    reachable with coherence on this apparatus above MED at session scale.*
  - **ADDENDUM-j1, appended and licensing D3.** M-arm only, n = 24, f = 0.30
    (α = 30.9030), h-roster, uncached, checkpointing on, three readouts,
    descriptive. Three additions declared before the run: **(a)** the marker
    readout in **both** contexts — in situ and excised to task+response — so
    the dose–response is reported in each; **(b)** a gross-breakdown pause
    bar, **≥ 4 of the first 8 sessions excluded under the forced scope ⇒
    pause and flag**, hair-trigger classes binding as standing; **(c)**
    welfare — the registered exposure and nothing more, termination counter
    retained, destabilization counters reported whatever they show.
  - **The closure is unconditional on D3.** D3 cannot qualify the rung,
    cannot move the run dose, and cannot reopen e2d. It supplies the third
    session-scale point of a dose–response (0.10 archive, 0.20 D2, 0.30 D3)
    and the degeneracy curve toward the 0.40 overdose regime, and that is
    all it is for.

- 2026-09-02 — **e2d D2 — THE QUALIFICATION RUNG FAILS. Q1 PASSES, Q2 and Q3
  FAIL, and the run-dose rule returns STOP, SCOPED: the run dose is not 0.20.
  64 sessions at f = 0.20, acceptance PASS on every item (KL 357/357 exactly
  0.0; 64/64 reconstructed; no bar fired). The scope sentence §2 registers for
  this outcome now has its figures: Q2 median AUC 0.574 against a 0.70 bar,
  Q3 Δ+ = +0.103 against a 0.158 bar.**
  ([`data/e2d/d2_sessions.json`](data/e2d/d2_sessions.json),
  [`d2_scores.json`](data/e2d/d2_scores.json),
  [`d2_analysis.json`](data/e2d/d2_analysis.json),
  [`d2_read_marks.json`](data/e2d/d2_read_marks.json),
  [`d2_tables.json`](data/e2d/d2_tables.json); raw
  [`_d2`](results/raw/2026-09-02_e2d_d2.txt),
  [`_d2_scoring`](results/raw/2026-09-02_e2d_d2_scoring.txt),
  [`_d2_analysis`](results/raw/2026-09-02_e2d_d2_analysis.txt).
  PROPOSAL-j v1.2, analyzer committed at `77e0fe6` **before** the data.)

  - **THE RUN-DOSE RULE, computed before any artifact was written.**
    **`STOP, SCOPED`**, failing Q2 and Q3. §2's sentence, with the figures
    filled: *the weak-state boundary is not reachable with coherence on this
    apparatus above MED at session scale* — Q2 median 0.574, 10th pct 0.524;
    Q3 Δ+ 0.103 vs bar 0.158. **No automatic fallback rung**; a 0.15 rung is
    licensable by addendum, never inherited `[PI-CHOICE: default = stop]`.
  - **Q1 validity — PASSES, and it is the one that says the apparatus held.**
    M-arm exclusions **3/32 = 9.4%** on the FORCED scope of record
    (AMENDMENT 2 (ii)), one-sided exact binomial **p = .878** against
    p0 = 0.15. Reasons: one `banner_terminator` at forced3, two lexical
    (`plaza@free0`, `ridge@forced0`). **The apparatus is not breaking down at
    2× MED** — which is what makes Q2's and Q3's failures readable as facts
    about the state rather than about the harness.
    - **Beside, and clause (ii) is doing real work:** under the strict scope
      the same arm is **8/32 = 25%** (p = .096). The scope choice moves Q1's
      figure by a factor of 2.7 and was settled before the data.
  - **Q2 readability — FAILS, on every set reported.** Resampled clean-round
    ladder, B = 20, k = 2, seeded through `discrim.seed_for`:

    | set | median | 10th pct | passes |
    |---|---|---|---|
    | **v2-clean AND read-clean** (the set of record) | **0.574** | **0.524** | **NO** |
    | v2-clean only | 0.608 | 0.519 | no |
    | k = 1, same rounds | 0.623 | 0.563 | no |
    | all rounds, degeneracy included | 0.635 | 0.558 | no |
    | **AUC_R** (arm R, displacement comparator) | 0.534 | 0.333 | no |

    Bars are median ≥ .70 and 10th pct ≥ .60. The criterion set fails by a
    wide margin, and **so does every variant** — the failure is not an
    artifact of which clean set was chosen.
    - **The comparison that matters is with D1.** D1's k = 2 median was
      **0.583 at HALF this dose**, on four sessions. D2 gives **0.574 on
      thirty-two**. **Doubling the dose did not make the state more readable
      in the record.** That is the substantive result, and it is the one §2
      Q2 was built to detect.
    - **AUC_R = 0.534** — the random arm is essentially at chance, so the M
      arm's 0.574 is barely above its displacement comparator. This is not
      "readable but displacement-shaped"; it is close to not readable.
    - **The read-marks LOWERED readability** (0.608 → 0.574). Removing
      content-shaped junk made the poles slightly *harder* to tell apart,
      which is the g2r pattern's shape — the 2026-08-18 spotcheck read k = 2
      discriminability as having "ridden on the pole-asymmetric degeneracy
      rather than content". Descriptive here; both figures are reported and
      neither is adjusted.
    - **Transfer, registered secondary:** the stored classifier's self-score
      is AUC **0.958** on its own fit set (n = 257) — a fit-quality number,
      **not** a transfer number. There is no second corpus to transfer to
      until a campaign exists, so the registered transfer figure is
      **unmeasured at D2** and says so.
  - **Q3 direction — FAILS on magnitude, and the ESTIMATOR CHOICE FLIPS THE
    SIGN.** Primary is AMENDMENT 2 (iv)'s ratified within-M, paired by
    session: **Δ+ = +0.103** against bar 0.5·G = **0.158**; 27 of 29 sessions
    decidable, SD of the per-session differences 0.399. **No sign flip** —
    Δ+ is positive, so V1's overdose signature is absent. Δ_R = +0.069, so
    Δ+ > 2·|Δ_R| = 0.138 also **fails**.
    - Paired sign test **18/27 positive, p = .061**; seeded sign-flip
      permutation **p = .096** (B = 10,000, seed 20260902). Directionally
      positive, not significant, and below the registered bar either way.
    - **The estimators disagree in sign, which is why (iv) mattered:**

      | estimator | Δ+ |
      |---|---|
      | **within-M, paired by session** (ratified primary) | **+0.103** |
      | within-M, pooled | −0.008 |
      | across-arm, vs the S arm | −0.070 |
      | paired, WITHOUT the read-marks | −0.035 |
      | task-matched pairs (16 tasks) | +0.043 |

      The verdict is unchanged — every one of these is below 0.158 — but the
      **headline number's sign depends on the estimator and on the read**,
      and AMENDMENT 2 (iv) and (iii) fixed both before the data. Had either
      been settled afterwards, this table is what the choice would have been
      choosing between.
  - **Descriptive tables (AMENDMENT 2 (ii)), and one of them is a finding.**
    Audit-degenerate rates, per round class, forced vs free:

    | class | forced | free |
    |---|---|---|
    | +axis | 1/62 = .016 | 3/86 = .035 |
    | sham(M) | 0/63 = .000 | 3/89 = .034 |
    | random | 0/32 = .000 | 4/47 = .085 |
    | sham(R) | 0/32 = .000 | 3/45 = .067 |
    | **sham(S)** | **0/61 = .000** | **0/90 = .000** |

    **The S arm has zero audit-degenerate rounds anywhere, while BOTH steered
    arms show degeneracy in their UNSTEERED rounds** (sham(M) 3/89,
    sham(R) 3/45). Degeneracy tracks whether the SESSION contains steering,
    not whether the ROUND was steered. That is a session-level displacement
    effect and it is what LOCK-j's free-round tripwire has to be declared
    against; it also says the tripwire cannot be calibrated on the S arm.
  - **The rule-25 read (AMENDMENT 2 (iii)): 39 marks over 39 rounds of 607.**
    preamble-without-content 21, task-echo 14, wrong-task 3,
    stuck-attractor 1. Rates: **M 34/300 = 11.3%, S 5/151 = 3.3%,
    R 0/156 = 0.0%.**
    - **v2 and the read overlap on nothing.** v2 flagged 14 rounds, the read
      39, intersection zero — rule 28(b)'s audit-first precedence means a
      round v2 claims is never offered to the read. Two whole M sessions are
      junk end to end and v2 excluded neither: **s1** restates the task on
      all ten rounds (forced3: *"Prompt: In a parrot-like echo, describe how
      fresh laundry smells."*), **s5** answers *"Great, I'll <restate the
      task>!"* ten times.
    - **R's zero is striking and I am reporting it with its caveat.**
      Content-shaped junk is concentrated in the axis arm and absent from the
      random arm at the same α — which would be an axis-identity signal in a
      channel nobody registered. **But the reader is the instrument and read
      the arms in order M, R, S**, so a sensitivity gradient across the read
      is not excluded, and M has twice the sessions. This is exactly what the
      (iii) overbreadth screen and an adjudicated detector exist to settle.
      **Not offered as a finding.**
  - **TWO MODES OUTSIDE THE FOUR CLOSED CLASSES — flagged, not marked**
    (AMENDMENT 2 (iii): a fifth class is a design flag, not a new string in a
    marks file). **M s9 free0 = `[MENTAL_BLOCK]`**; **M s17 forced3, free3,
    free5 = the literal word `None`** as the entire response. Both are
    null/refusal responses — not an echo, not a wrong task, not a preamble,
    not an attractor. **All four are in UNSTEERED rounds.**
    - Borderline patterns deliberately left unmarked, named for the class
      draft: M s11's *"Good! The name \*\*Cafe\*\* is a good fit."* wrapper,
      which does deliver a token answer; and the sham arm's adjective
      transfer, where the tone word lands on the object — *"the softer
      sink"*, *"the polite sink"*, *"the gentler sink"* across three S
      sessions.
  - **AMENDMENT 2 (v), registered secondary — NOT verdict-relevant.**
    On the valid M domain: **b₊ = 0/13, bₛ = 1/16**, forced-end balance 13/16,
    and the weighted identity returns **+0.017241**, which is Δ_first
    (15/29) **exactly**. The balanced form gives −0.031 at this imbalance —
    the caveat entered with the amendment, doing its job.
    - Habit-break rate on the first pick: **M 1/30, R 0/16, S 1/15** — the
      habit holds almost universally at the first choice, in every arm.
    - Strict alternation over all six choices: **M 0.690, R 0.750,
      S 0.933** (e2a's corpus: 0.840). The steered arms alternate *less*
      strictly later in the session while the first pick stays locked. The
      registered secondary is the first-pick break rate and it shows nothing;
      the alternation-decay difference is descriptive and unregistered.
    - **A DEFECT I FOUND AND FIXED, recorded because the number was wrong in
      the first artifact.** `d2_scores.json`'s habit block was computed over
      ALL 64 sessions, including excluded ones, so its weighted form reads
      **0.000** — it does not equal the Δ_first it claims to decompose. The
      identity is stated over the domain Δ_first is computed on, which is
      the VALID sessions. Corrected block in
      [`d2_tables.json`](data/e2d/d2_tables.json), where it reproduces
      +0.017241 exactly; `e2d_score.py` now emits both domains and names
      which one the identity belongs to. **`d2_scores.json`'s habit block is
      superseded by `d2_tables.json`'s**; nothing else in it is affected, and
      no criterion reads it.
  - **Cost, against clause (vii).** Generation 6.92 h uncached (389 s/session,
    64 sessions). Marker 7,284 probe forwards in 1.10 h. Ladders 2.83 h after
    a memoizing `embed` proxy — the resampled ladder re-embeds every record on
    each of B draws, and `embed` is a deterministic forward, so caching by
    text is numerically free (verified: same text, identical vector). Without
    it the ladders measured **~4.3 h**. Total ≈ 10.9 h against (vii)'s
    "≈ 1.5 h + ≈ 1 h scoring", and the generation half was already known to be
    uncached. **The scoring+ladder budget is the part that needs revising**,
    not the generation one.
  - **What D2 does NOT say.** It is the qualification rung, not a verdict on
    coupling. Δ_first over the valid M arm is **15/29 = +0.017**, reported
    here as a descriptive number with no criterion attached — the campaign's
    primary is registered at n = 128 and does not exist. **e2d has not tested
    approach at 0.20 and now will not**, unless design licenses a rung by
    addendum.

- 2026-09-02 — **APPARATUS READ for paper 1's methods (block item 2, NOT e2d):
  cached vs uncached generation is NOT token-identical at the e2a/e2b dose
  either. 23/24 M-shaped rounds identical at f = 0.10; the one divergence is
  at POSITION 1, where the two paths produce entirely different sentences.
  At f = 0.20 the same check gave 22/24. No design consequence for e2d — its
  round path was already settled UNCACHED — but e2a, H1, H2 and the e2b
  verdict campaign all ran CACHED, and the methods can now state the rate
  instead of assuming it is zero.**
  ([`data/e2d/tstep_check_f010.json`](data/e2d/tstep_check_f010.json); raw
  [`2026-09-02_e2d_tstep_f010.txt`](results/raw/2026-09-02_e2d_tstep_f010.txt).
  Run in the gap between D2 and D3, never overlapping a campaign.)

  - **The measurement.** 24 M-shaped rounds at f = 0.10, α = 10.3010, L48, v3
    templates, h-roster tags, the real task corpus, the frozen ban list,
    temp 0.7, and **the same per-round seed on both paths**. Positions 1..42
    exercised. **23/24 identical; 1 divergence.**
  - **The divergence, and its position is the point.** Session 1 round 3
    (task t16), 42 tokens cached against 37 uncached, **first divergent
    position = 1**:

    | path | text |
    |---|---|
    | cached | *"\*\*\"As the last light of day filters through the glass, the warm glow illuminates the few remaining pastries…"* |
    | uncached | *"The glass glows with the warm, amber light of the last few loaves, their golden crusts dusted with flour…"* |

    Not a late drift — the two paths choose a different FIRST token and never
    reconverge.
  - **This does not contradict the g1 gate; it is what the gate does not
    say.** g1 measures the first-response-token DISTRIBUTIONS and bounds
    their symmetric KL at 7.106e-4 (0.10) and 7.391e-4 (0.20) against a 1e-3
    bar. Distributional agreement at 7e-4 is exactly compatible with
    temperature-0.7 sampling resolving a near-tie the other way at some rate.
    The gate is sound and the divergence is its complement, not its
    refutation: **agreement in distribution is not identity in sampled
    text**, and only the second is what a transcript inherits.
  - **The two doses, side by side.** f = 0.10: **1/24 = 4.2%** of rounds
    diverge. f = 0.20: **2/24 = 8.3%**. Both from the same instrument, the
    same 24-round design, the same seeds-per-path discipline. The direction
    is what one would expect if larger displacement widens the
    near-tie band, but **two counts of 1 and 2 do not establish a dose
    trend** and are not offered as one.
  - **What the methods can now say, and what it must not.** e2a, H1, H2 and
    the e2b verdict campaign ran the cached path (`round_path_cached: true`
    in every committed artifact), licensed by g1 and by the 2026-08-09
    adjudication that carried it across the v3 template change. The honest
    disclosure is that **~4% of those generated rounds would have contained
    different text under the uncached path**, and that neither path is the
    correct one — they are two licensed samplers that agree in distribution.
    **No published number is impugned.** Every verdict in the record is over
    a corpus generated by ONE path, analysed by instruments that read that
    corpus; path-dependence at 4% changes which sentences exist, not whether
    the analysis of them was right.
  - **A labelling defect in the artifact, named so nobody misreads it.** The
    script is generic and writes a `verdict.round_path_for_d2` key, so the
    f = 0.10 artifact carries `"round_path_for_d2": "uncached"`. **That field
    has no D2 meaning here** — D2 runs at 0.20 and was licensed by
    [`tstep_check.json`](data/e2d/tstep_check.json), not by this file. This
    run is an apparatus read and licenses nothing.

- 2026-09-02 — **S1 k = 1 RE-READ, delivered for the review round. READS ONLY,
  no adjudication. Every claim checks out against the committed table: S1's
  verdict entry evaluates all eight cells against the k = 2 parity anchor
  (.759) ONLY, while its own pre-scoring entry registered a k = 1 anchor of
  .645 that no cell is ever compared to. Against that registered anchor,
  2 of the 4 k = 1 cells exclude it; against .633 (the v3-family figure),
  1 of 4. And the entry's CIs are WILSON, not Clopper-Pearson — confirmed to
  <6e-4 on all five cells checked.**
  (Reading [`RESULTS.md`](RESULTS.md) l.5601 (S1 verdict) and l.5717
  (pre-scoring anchors) against
  [`data/e2a/s1_judge_rescue.json`](data/e2a/s1_judge_rescue.json). Carried
  from the 2026-09-01 block, where it lived only in a handoff section since
  rewritten — so it is entered here, in the record, rather than left in an
  orientation document.)

  - **The CI convention.** The published intervals are Wilson. Spot-checked on
    five cells at n = 64: `better k1 zeroshot` 31/64 → Wilson [.366, .604]
    matches the entry exactly, Clopper-Pearson would be [.358, .613]; same
    pattern on `better k1 fewshot`, `detection k1 zeroshot`,
    `detection k1 fewshot` and `detection k2 fewshot`. Not a defect — Wilson
    is a defensible choice at this n — but the entry does not say which it
    used, and the two differ by ~0.01 at the bounds, which is the scale the
    exclusion calls are made on.
  - **The anchor that was registered and never used.** The pre-scoring entry
    registers three: chance .500, **probe k = 1 .645**, probe k = 2 parity
    .759. The verdict entry's headline is *"every cell's 95% CI EXCLUDES
    probe-k=2 parity (.759)"* — true, and it is true of the k = 1 cells too.
    But comparing a k = 1 judge cell to the k = 2 probe compares across rungs.
    Against the k = 1 probe anchor, on the entry's own published intervals:

    | k = 1 cell | acc | Wilson CI | vs .633 (v3) | vs .645 (registered) |
    |---|---|---|---|---|
    | better k1 zeroshot | .484 | [.366, .604] | **excludes** | **excludes** |
    | better k1 fewshot | .516 | [.396, .634] | includes | **excludes** |
    | detection k1 zeroshot | .562 | [.441, .677] | includes | includes |
    | detection k1 fewshot | .547 | [.426, .663] | includes | includes |
    | | | | **1 of 4** | **2 of 4** |

  - **What this does and does not touch.** It does **not** overturn S1's
    registered reading. No cell clears chance, which is the load-bearing half,
    and that is unaffected. What it qualifies is the *strength* of the second
    half: "the judge cannot reach probe parity" is 8-of-8 against the k = 2
    anchor and 2-of-4 at k = 1 against the k = 1 anchor. Rung-matched, the
    separation at k = 1 is equivocal rather than clean.
  - **Why it matters beyond S1.** PROPOSAL-j §0.4 records that **k = 1 is the
    stable rung** (.633/.645 across the ban) and that k = 2's .759 inverted to
    .448 in the transfer spotcheck with `g2r_stands: false`. So the anchor S1
    evaluates everything against is the one the proposal treats as
    refit-dependent, and the anchor it registered but never used is the stable
    one. That is the review round's business, not this entry's.
  - **No adjudication, and nothing is proposed.** No number is recomputed, no
    artifact is touched, no wording is changed. Design decides whether the
    k = 1 comparison enters the S1 write-up and how paper 1 words the
    recognition break.

- 2026-09-02 — **e2d D2 LAUNCHED AND STOPPED AT 9/64 — a POWER fault on the
  laptop, not a defect in the design or the harness. The machine is on a 20 W
  adapter; under sustained GPU load it ran a large net deficit, the battery
  went 70% → 7% in 1 h 45 m, and session times degraded 4.6× as it throttled.
  Stopped deliberately before the battery forced a shutdown. NO D2 DATA
  SURVIVES and none should be used: the runner wrote its artifact only at the
  end. That is now fixed. D2 is BLOCKED on hardware.**
  (Raw [`2026-09-02_e2d_d2.txt`](results/raw/2026-09-02_e2d_d2.txt) — the run
  header and nine session lines; no artifact was written. PROPOSAL-j v1.2
  `ce3ff84`; build `77e0fe6`.)

  - **What the header records, and it is all correct.** tier d2, registered
    n = M 32 / S 16 / R 16, f = 0.20, α = 20.6020, L48; roster of record;
    audit v2 sha `7aa235d25eeb66dc`; **T-step licence 22/24 → UNCACHED**;
    M-arm task_id coverage at draw seed 20260902 **pos 16 / neg 16, floor
    met**. The apparatus started correctly; only the machine failed.
  - **The evidence.** `pmset -g adapter` reports **Wattage = 20 W**. An M4 Pro
    under sustained MLX load draws several times that, so the deficit was
    structural rather than a fluke. Session wall-clock, in order: 364, 450,
    359, 418, 458, 545, 480, **1439, 1691** s — a clean break after the
    seventh, which is where the battery got low enough to power-limit the SoC
    hard. At 1691 s/session the remaining 55 sessions would have taken **~26
    h**, and the battery would not have lasted a fraction of it.
  - **Why I stopped rather than let it run.** The runner had written nothing
    to disk. A shutdown would have destroyed all nine sessions and any
    further, and D2 has no outcome-dependent stopping to protect — the
    schedule is fixed, so restarting costs only time. Stopping was the
    reversible action; continuing was not.
  - **THE REAL DEFECT THIS EXPOSED, and it is mine: a 6.5 h run that wrote
    its artifact only at the end.** The power fault is the user's hardware;
    the total loss of nine sessions is the runner's design. `run_campaign`
    now writes an **atomic** checkpoint (`os.replace`, so never a
    half-written file) after **every** session, and `--resume` continues a
    checkpointed run.
    - **Resuming completes the registered schedule; it cannot extend one**,
      and that is structural rather than promised: the schedule is built from
      the draw seed before the first forward, each session's content is fixed
      by `session_rng(f"e2d-{arm}", idx)` and its cell, and the resume path
      can only SKIP indices. A checkpoint written under a different seed or a
      different registered n is **refused** — resuming across those would
      splice two designs. e2a set the precedent: its run-2 relaunch used
      `--resume` with 16 sessions recorded and standing.
    - **Tested model-free and in the suite (154/154, still 0.24 s).** The
      check asserts **byte-identical transcripts** across an interrupted-then-
      resumed run, not merely the same session count, plus the refusal. A
      resume that produced a near-copy would be worse than no resume at all.
  - **What D2 needs before it can run: a higher-wattage adapter.** Nothing in
    the design or the build is waiting on anything else. The rerun is a fresh
    D2 under the same registered schedule (draw seed 20260902), and the nine
    stopped sessions are discarded rather than resumed — they were run under a
    throttled machine and, more to the point, they were never written down.
  - **Two provenance defects in the run header, found while it ran and fixed
    after** (log defects only; the structured fields the artifact would carry
    were correct):
    - **The axis-sha comparison line was wrong, and my D1 entry described the
      convention imprecisely.** `sha16_arr` ALWAYS hashes float32 bytes, so
      the two shas do not differ by storage dtype — they differ by **where
      the normalisation arithmetic happens**. Normalising the stored float32
      array in float32 gives the receipt's `127fc297b6623e44`;
      `Injection.at_frac` casts to float64 first and gives
      `3c17b0d8fbcad716`. Casting back to float32 AFTER a float64 normalise
      does **not** recover the receipt — which is exactly what my line did, so
      D2's header printed the two conventions as equal. Anyone following the
      D1 entry's wording would have made the same mistake. **Corrected here.**
    - The round-path line printed the T-step verdict inside a field labelled
      `g1 artifact … pass`, so the header reads `pass=False` where g1 in fact
      passes at 0.20. Licence and gate are now separate, correctly named
      fields.
  - **Also built while D2 ran** (`scripts/e2d_read.py`): the rule-25 read
    tooling — dump with a stable key per round, validate a marks file against
    the sessions it describes, tabulate. It contains **no detector**, on
    purpose: AMENDMENT 2 (iii) puts the class spec after the read, and a
    detector written first would hand the read its own categories. D1's read
    is recorded in the new schema at
    [`data/e2d/d1_read_marks.json`](data/e2d/d1_read_marks.json) — the six
    unambiguous S s0 rounds, each with the reason the read gave. The two
    borderline hits from that day's ad-hoc screen are **not** marked.

- 2026-09-01 — **INCIDENT, contained: a SUBSET oracle run silently replaced the
  rule-26 record. Restored from git, guard added, suite 148 → 149. No published
  number moved and no verdict was touched — but for the length of one command
  the artifact that certifies criterion (iii) said something it had not
  measured.** (`9ed07a7`. Fix: `refuse_canonical_out` in
  [`valence_core/regression/oracle.py`](valence_core/regression/oracle.py).)

  - **What happened.** `oracle.main()` wrote
    `data/regression/oracle_rule26.json` unconditionally, carrying whatever
    subset `--check` had selected. Running `--check e2d` — the new criterion
    (iv) — therefore replaced the four **e2a choice-read** rows, which are
    rule-26 criterion (iii), with the four **e2d** rows under the same
    filename, and flipped the provenance block's `n_encodes_clipped` from 5 to
    0. **Nothing in the file recorded that it was a partial run**, which is
    the hazard in one sentence: a partial record is indistinguishable from a
    complete one once written.
  - **How it was caught.** `git status` showed
    `data/regression/oracle_rule26.json` modified in a commit where I had
    edited no such file. It was restored with `git checkout` and verified row
    by row before anything else proceeded.
  - **Whose defect.** Not e2d's. `main()` has always written unconditionally,
    so `--check kernel`, `--check b2b` and `--check choiceread` would each
    have done the same thing. Adding a fourth subset made the path routine
    enough to walk down, and I walked down it. **`e2b_verdict_campaign.py` has
    had `refuse_canonical_out` since 2026-08-22** for precisely this; the
    oracle had no equivalent, and the asymmetry was not noticed when the
    e2b guard was written.
  - **The fix.** `refuse_canonical_out(out, check)` — named and separate so it
    is testable without a model, and called at **argument-validation time** so
    it fires before the model loads rather than after four minutes of
    forwards. `--check all` writes the canonical artifact; a subset requires
    an explicit `--out`, is refused if that `--out` **is** the canonical path,
    and with no `--out` writes nothing at all — so a subset cannot quietly
    become the record and cannot leave a stray artifact in `data/` either. The
    subset payload also records `check`, and the e2d adapter's own provenance
    when those rows ran: criterion (iv) reads WITHOUT `legacy_truncate`, and
    recording only the legacy adapter's provenance would misdescribe them.
  - **Two testing mistakes of mine, recorded because each is a trap the
    program already knows in another form.**
    - **I first "verified" the guard by killing the run after 25 s and
      observing the canonical file unchanged.** It was unchanged because the
      process never reached the write — **a skipped case reading as a pass
      (trap 5), inside the check written to prevent a clobber.** Moving the
      refusal to argument-validation time made the branch reachable in
      milliseconds, which is both the better design and the only way the test
      could bite.
    - **The first suite check called `oracle.main()` for the non-refused
      direction.** That direction gets past validation and **loads a model**;
      the model-free tier went from 0.15 s to minutes. The check now exercises
      the guard function directly in all four directions — canonical refused,
      another path allowed, `--check all` allowed (the full run is the one
      permitted to write it), no `--out` allowed — and asserts that all four
      ran.
  - **Scope, stated plainly.** The e2a rows are byte-identical to their
    committed values after restore; the full oracle set has not been re-run
    and does not need to be, because the file never held a *wrong*
    measurement — it held four correct e2d measurements under a name that
    promised four e2a ones. Rule-26 acceptance is unaffected.

- 2026-09-01 — **e2d D1 — HARNESS ACCEPTANCE: PASS on every item. 8 sessions
  at f = 0.10, n = M 4 / S 2 / R 2. KL exactly 0.0 on 42/42 free-choice reads;
  `statepresent` absent at every read; 8/8 sessions reconstruct byte-for-byte
  with all 8 seed streams matched; no bar fired; no traceback. Suite 137 →
  148, plus a new oracle criterion (iv). FOUR FLAGS, none of which stops D1
  and two of which bind before D2: the exclusion scope, the round path
  (D1 ran UNCACHED where e2a and e2b both ran CACHED — a 4.4× cost), an audit
  blind spot the full read found and audit v2 scored 0 on, and a choice-
  alternation habit that carries 83% of e2a's own primary DV.**
  (Site: laptop, AC power, `caffeinate -is`, one model process, suite 148/148.
  Module + analyzer committed BEFORE the run at `4e41288`; D1 ran that code.
  Artifact [`data/e2d/d1_sessions.json`](data/e2d/d1_sessions.json); raw
  [`2026-09-01_e2d_d1.txt`](results/raw/2026-09-01_e2d_d1.txt).
  PROPOSAL-j v1.1 `70995c0`.)

  - **ACCEPTANCE, item by item.** Every item the D1 block names, and the
    named check for each.
    - **KL = 0.0 exactly on every free-choice read: 42/42, max 0.0.** The
      block expects "48/48"; 48 assumes eight sessions × six free choices,
      and R s1 was excluded at forced round 1 before reaching any choice.
      **42 is the whole population of reads that existed**, not a subsample:
      `kl_reads_logged` 42 = `kl_reads_expected` 42, asserted equal rather
      than compared by eye (trap 5 — a read that never happened must not
      read as a read that passed).
    - **`valence_core.e2b.statepresent` absent on every read.** Asserted at
      startup, before each of the 42 reads, and again after the campaign.
      The suite adds the structural half: it is never IMPORTED anywhere in
      `valence_core/e2d/` (searched as an import statement, since the
      runner's docstring names it deliberately).
    - **Format check, named: `session_e2a.verify_archived_session`** — the
      same positional byte-for-byte scaffolding walk that reconstructs all
      200 archived e2a sessions. **8/8 reconstructed, 8/8 seed streams
      matched.** The seed-stream half is the stronger statement: a replay
      landing on the recorded per-round seeds cannot be off by a draw.
    - **Tripwires `verify_firing`: 7 cases, all ran, all as declared.** Each
      of the three bars is exercised in BOTH directions and the runner
      refuses to start if any bar is missing a direction — a bar that is
      never made to fire has not been checked.
    - **No bar fired. No raw traceback. No verdict content.**
  - **Counters (rule 23, over all 8 sessions including the excluded one).**
    audit-degenerate **0**; lexical **1**; cap-hits **0/72 rounds**;
    termination attempts **0**; post-choice degeneracy **0**; low-label-mass
    **4/42 choices = 0.095** (e2a's convention is p0 = 0.20 on choices,
    pooled, so this is well inside). Every one of the 72 generations stopped
    on a newline — the stop discipline held on all of them.
  - **Exclusions: 1/8, and both scopes agree at D1.** R s1,
    `lexical:ridge@forced1` — the model emitted its own config tag
    (*"Ridge - Slogan: \"Ridge: Where style meets speed on two wheels.\""*),
    which is exactly what the lexical rule is for. M **0/4**, S **0/2**,
    R **1/2**. Under the strict ("e2b") scope: identical, 0/4, 0/2, 1/2.
    Descriptively against e2a's 0.10 archive (reward-arm 8.9%): 0/4 on the
    M arm is uninformative at this n and is reported as such.
  - **Wall clock, and it does not match the proposal's budget.** Generation
    **2,939 s for 8 sessions = 367 s/session** (mean over all eight; the
    seven that ran to completion average 417 s). Marker readout **864 probe
    forwards over 72 generations ≈ 466 s** (0.54 s/forward). Readability
    ladder ≈ 441 s (by subtraction from the 3,846 s total; the script now
    times each phase directly). **PROPOSAL-j §7 budgets D1 at ≈ 20 min; it
    took 64.** The cause is the round path, next flag.

  - **FLAG 1 — ROUND PATH. D1 ran UNCACHED. e2a and e2b both ran CACHED, and
    the proposal says "everything else is e2a".** This is my deviation, not
    the proposal's, and I did not notice it until the budget came in 3×
    over.
    - e2a set `use_cached_rounds = g1["results"][str(frac)]["pass"]` and the
      gate passes at both fracs (`data/e2a/g1_kernel_gate.json`: 0.10 →
      max_kl **7.106e-4**, 0.20 → **7.391e-4**, bar 1e-3 — the rule-26
      numbers). e2b reads the identical artifact; **every committed e2b
      artifact records `round_path_cached: true`** (h1, h1u, h2,
      verdict_campaign).
    - I checked whether that was a rule-2 gap, because the gate artifact is
      stamped `template_family: v2` and e2b ran on v3. **It is not a gap:**
      the 2026-08-09 adjudication (archive l.948) says *"g1r stands
      unchanged — kernel gate is a path-equivalence property of
      prefix-conditional forwards, not of the sampled-text distribution
      (rationale on record)"*. The cached ROUND path is licensed on v3.
      Choice forwards stay uncached and state-free regardless — that is g3′
      clause 1 and e2d never touches it.
    - **Cost of the deviation:** 367 s/session against e2b's H2 measured
      **83.8 s/session** cached (32 sessions in 2,682 s) — **4.4×**. At D2's
      n = 64 that is **≈ 6.5 h uncached against ≈ 1.5 h cached**, versus the
      proposal's budgeted 2.2–2.7 h.
    - **D1's acceptance is unaffected** and I am not proposing a re-run: every
      acceptance item is path-independent (KL is a property of the choice
      forward, which was uncached in both worlds; the format walk is over
      harness-written bytes; the bars did not fire), and D1 produced no
      verdict content. The script now takes `--round-path {gate,cached,
      uncached}` defaulting to **`gate`** — consulting the g1 artifact
      exactly as e2a and e2b do — and prints the decision with the gate's own
      max_kl. **D1's artifact records `round_path_cached: false`.** Design
      may of course prefer uncached for D2; it should be a choice, which it
      was not here.
  - **FLAG 2 — EXCLUSION SCOPE, restated because D1 did not settle it.**
    AMENDMENT 1 (ii) names the audit artifact, not whether an
    audit-degenerate FREE round excludes. Both scopes gave the same answer at
    D1 (1/8) because the one exclusion was lexical and in a forced round —
    **agreement at n = 8 is not evidence they agree**. On the e2a archive
    they give 10/112 = 0.089 and 18/112 = 0.161, and against Q1's p0 = 0.15
    at D2's n = 32 (fires at ≥ 9/32, p = .0413) the probability of Q1 firing
    on a healthy apparatus is **0.0015** under the first and **0.0602** under
    the second. Design settles it before D2.
  - **FLAG 3 — THE FULL READ FOUND DEGENERACY THE AUDIT OF RECORD SCORED
    ZERO ON, and it is the FINDINGS-5 §3 pattern in a new shape.** Rule 25's
    read of all eight transcripts turned up **S s0**, which audit v2 passed
    entirely (`excluded: false`, 0 audit flags) and which is junk in **6 of
    its 10 rounds**:
    - rounds 2, 6, 9, 10 are all *"Here are a few name ideas for your small
      coffee cart:"* — a preamble that never delivers content, and in rounds
      6, 9 and 10 **it answers the wrong task entirely** (round 6's task was
      *"Reword this note softly: Do not leave dishes in the sink"*). It is a
      stuck attractor on round 2's response.
    - round 4 is *"Here are a few caption ideas for your photo of a tone of a
      ferry crossing at a ferry crossing at dawn:"* — garbled and repeating.
    - round 8's response is the **task line echoed verbatim**: *"In one
      sentence, thank someone for lending you a book."*
    - **Why v2 missed all of it:** v2's four junk patterns are banner
      terminators, bracketless round headers, config-role phrases and
      config-then-bracket. Every one is SCAFFOLD-shaped. This degeneracy is
      CONTENT-shaped — preamble-without-content, wrong-task attractor, task
      echo — and no fragment or pattern reaches it. The audit built to catch
      the last blind spot does not catch this one.
    - **It is in the SHAM arm**, where no state exists anywhere, so it is an
      apparatus base rate and carries no information about the axis. Two
      further hits (M s0 forced0, R s1 forced0) came from a quick two-test
      screen I wrote to count this, and **both are arguable** — one is a
      legitimate short answer that happens to be a substring of its task.
      **I am reporting a detection, not proposing a rule:** v2 itself was
      screened for overbreadth against a 2,170-response pool before adoption,
      and nothing here has been. The finding is that **a screen is needed**;
      `data/configs/scorer_v3_spec.json`'s six-class taxonomy is the natural
      home for the class, and the standing instruction there — specify over
      the CLASS, not the observed construction, because v1 and v2 each fixed
      the instance and missed the class — applies exactly.
    - **Consequence for D2 if unaddressed:** Q1's exclusion rate misses this
      mode entirely, and Q2's "audit-clean rounds" are not clean — rule
      28(b)'s tolerant-counter-first ordering only helps for junk the
      tolerant counter can see.
  - **FLAG 4 — THE MODEL ALTERNATES, AND IT CARRIES MOST OF THE PRIMARY DV.
    Inherited from e2a, not introduced here.** In D1, **6 of 7** valid
    sessions alternate strictly on every one of the six free choices, and in
    **7 of 7** the first free pick is the complement of the last forced
    round's pole. I checked the archive before saying anything, and the same
    structure is in the published corpus: **157/187 = 84.0%** of e2a sessions
    alternate strictly (reward 82.7%, sham 86.8%, random1 91.3%, random2
    77.3%), and **156/187 = 83.4%** have the first free pick complementing
    the last forced pole. D1 sits inside that; **nothing about e2d's harness
    produced it.**
    - **Post-hoc, on committed data, and labelled post-hoc (rule 11 — this
      licenses a pre-registration, never a verdict):** splitting e2a's
      reward arm on alternation, the published primary is carried almost
      entirely by the sessions that break the habit —

      | e2a reward arm | n | first-pick +pole | Δ_first | p (one-sided) |
      |---|---|---|---|---|
      | alternating | 84 | 43/84 = .5119 | **+0.0119** | .457 |
      | non-alternating | 18 | 12/18 = .6667 | **+0.1667** | .119 |
      | **all (published)** | **102** | **55/102 = .5392** | **+0.0392** | **.244** |

    - **What this does and does not mean.** It does **not** overturn e2a's
      null: neither subgroup is significant, and the non-alternating
      subgroup's Δ is an 18-session post-hoc split. What it means is that
      **Δ_first's variance is largely spent on a mechanical habit**: in ~83%
      of sessions the first free pick is what the forced block's phase
      predicts, and since forced-end is counterbalanced those sessions
      contribute ~0 to Δ_first in expectation. The registered DV is being
      read through an instrument most of whose dynamic range is already
      committed.
    - **Why it matters now:** PROPOSAL-j §3 sizes M = 128 for one-sided power
      ≈ 0.9 at Δ = +0.15, and that arithmetic assumes each session's first
      choice is free to move. It also names an alternative the record has not
      considered — whether the state changes **the rate at which the habit
      breaks**, and toward which label — which is a different DV from the one
      registered and is **not** proposed here. Design's call, before LOCK-j.
  - **Marker readout (1e), descriptive — and the two readings of "sham
    rounds" DISAGREE IN SIGN, so the ambiguity is now demonstrated rather
    than hypothetical.** Instrument rebuilt with **G = 0.315550** against the
    pre-registered 0.3156 (bar 0.5·G = **0.1578**); 72 generations scored, 0
    skipped, **864 probe forwards**.

    | contrast | clean rounds | all rounds |
    |---|---|---|
    | **Δ+ within M** (M steered vs M's own unsteered) | **−0.2394** | −0.2394 |
    | **Δ_R within R** | +0.2713 | −0.3151 |
    | Δ+ vs the S arm | +1.4988 | +1.4988 |
    | Δ_R vs the S arm | +0.9147 | +0.3283 |

    - The within-arm reading (the one the §7 budget implies, since "480 D2
      generations" is M + R and excludes S) gives Δ+ **negative** — V1's
      overdose signature — at the MINIMUM effective dose. The across-arm
      reading gives +1.50, nine times the bar, in the opposite direction.
    - **I do not think either number means anything yet**, and the reason is
      concrete: n is 20 steered vs 20 unsteered rounds from four M sessions,
      Δ_R flips sign between clean and all-rounds on 5–6 rounds, and the
      across-arm reading is contaminated by S s0 — six of the S arm's twenty
      rounds are the degenerate attractor text of FLAG 3, and the S arm is
      the entire comparison set for that column. That is enough to explain a
      +1.5 on its own.
    - **What Design owes D2 is the reading, not the number:** Q3's sign is
      determined by which contrast "+axis rounds vs sham rounds" names. The
      analyzer computes the within-arm reading as primary and carries the
      across-arm one beside it, both labelled, so whichever is named the
      other is still in the artifact.
  - **Readability wrapper (1d), descriptive.** Resampled clean-round ladder,
    k = 2, B = 20, seeded through `discrim.seed_for`, on 20 clean +axis and
    20 clean sham rounds from the four M sessions: **median 0.583, 10th
    percentile 0.494, range 0.426–0.793.** Under Q2's bars (median ≥ .70,
    10th pct ≥ .60) this would not pass — **and it is not a Q2 reading**: it
    is four sessions over eight task ids at HALF the D2 dose, run to exercise
    the wrapper end to end, which it did. Worth one line of foresight only:
    that spread (.43–.79) is the shape of the g2r pattern the criterion was
    built to fail, so D2's Q2 is where the instrument earns its keep.
  - **Two provenance notes.** (a) The run header printed the +axis direction
    as sha16 `3c17b0d8fbcad716`, which is **not** the receipt's
    `127fc297b6623e44`. Same vector: ‖v‖ = **16.706271** matches the
    receipt's 16.7063 exactly, and `127fc297b6623e44` is the unit direction
    hashed **as stored** in float32 while `Injection.at_frac` casts to
    float64 first — trap 17's class, in the other direction. The script now
    prints both conventions and the artifact records both. (b) `run_campaign`
    printed progress without flushing, so the run looked hung from outside
    for its whole first hour; fixed.
  - **Suite.** 137 → **148** model-free checks, plus a new oracle criterion
    **(iv)**: the committed D1 session texts replayed through `choice_read`
    — **4/4 PASS** (raw
    [`2026-09-01_e2d_oracle_iv.txt`](results/raw/2026-09-01_e2d_oracle_iv.txt)):
    all 42 recorded reads recovered from the transcripts alone, **0/42
    nonzero KL**, 42/42 picks reproduced, and p_a reproduced to
    **0.00e+00** — exactly, not within tolerance. It builds its OWN adapter
    deliberately — the rule-26
    oracle runs `legacy_truncate=True` to reproduce published numbers through
    the 512-token tail window, and e2d runs full-session, so replaying e2d
    reads through the legacy window would compare two constructions and call
    the difference a failure.
  - **Reads for LOCK-j (item 4).**
    - **A guarded model-as-judge AB read does not exist; it is a PORT, and a
      small one.** `scripts/s1_judge_rescue.py:106` is the only place in the
      tree that still builds `QwenMLXAdapter()` directly instead of through
      `qwen_or_explain` — but that is the lesser half. Its AB read is a raw
      `adapter.forward(...)` plus a softmax over " A"/" B": **no
      `verify=True`, no `assert_construction_stable`, no KL logged, no
      `assert_modules_absent`.** `readout.choice_read` is already exactly
      this shape — two labels, a label→token-id map, restricted and
      renormalized, with `label_mass` and `top1_is_label` logged beside the
      pick — so the port is a few lines and would strictly gain the
      diagnostics S1 currently has no way to report. **Not built:**
      instruments are not built speculatively, and PROPOSAL-j §3 makes the
      judge secondary conditional on a guarded path existing by LOCK-j.
    - **Q1's inputs recounted under v2 — the amendment is confirmed on every
      figure**, reported in full in the entry above (`256c465`): reward arm
      **11/112**, +pole **8**, maximum **0.1473**, p0 = 0.15 unchanged.
  - **What is NOT here.** No D2 content, no 0.20 forward, no negative pole
    constructed anywhere in the run, no verdict. `scripts/e2d_d2_analyze.py`
    is committed and stub-smoked (34 branches) but has evaluated nothing.

- 2026-09-01 — **PROPOSAL-j AMENDMENT 1 appended (`70995c0`): both D1 gaps
  closed by the design instance, pre-data. Roster of record = the h-roster;
  audit rule of record = `e2b_audit_v2.json`; p0 = 0.15 unchanged. Code
  recounted Q1's inputs under v2 independently and CONFIRMS the amendment:
  reward arm 11/112, +pole 8, formula maximum 0.1473. Separately (`00fc4ef`),
  rule-27 provenance for e2a's exclusion rule — the LOGIC, which the repo did
  not have; 55/102 and 54/101 now reproduce from committed artifacts.**
  (Site: laptop, suite 137/137, main == origin/main, AC power, no model
  process. Raw:
  [`2026-09-01_e2a_recount.txt`](results/raw/2026-09-01_e2a_recount.txt).)

  - **The amendment, as appended.** (i) **Roster of record: the h-roster** —
    granite/plaza, prism/slate, velvet/walnut, ridge/saddle — *"an admissible
    four, never the best four"* (H3b, 2026-08-21), the only roster
    identity-screened on this apparatus in the scaffold format of record.
    e2a's own pairs were order-counterbalanced but never identity-screened
    and are not admitted; comparability with e2a is carried by e2b's paired
    shadow reads (insulated e2a-format read on this roster at 0.10, 48/96
    exactly), **not by pair identity**. Cells M 16 / S 8 / R 8 as before.
    (ii) **Audit rule of record: `data/configs/e2b_audit_v2.json`**; *"e2a's
    exclusion rule verbatim"* is withdrawn as a referent. (iii) **Slip
    ledger, design seat, by name: (8)** cell structure specified without
    naming the pairs; **(9)** an exclusion rule cited "verbatim" to an
    artifact absent from the repo and superseded in the record. Both were
    caught by the D1 block's own §0 stop clause before any forward — the
    stop clause is now two-for-two.
  - **Q1 p0 recounted under v2 — CONFIRMS the amendment on every figure.**
    Reproducing e2a's rule from committed artifacts: reward arm **10/112**
    under the frozen audit (**the published set exactly — same 10 sessions,
    every `exclude_reason` string identical**, +pole 7 / −pole 3 matching the
    verdict entry's pole-asymmetry line), and **11/112** under v2, the added
    session being **reward s1 forced round 2** (`=== end of session ===`,
    `banner_terminator`) — the very session v2's own-goal is about. That
    round's pole is **pos**, so the +pole-attributable count goes **7 → 8**.
    Formula: max(2 × 8/112 = 0.1429, 1.5 × 11/112 = 0.1473) = **0.1473 →
    p0 = 0.15**, and **0.1473 on the published +pole 7 as well** — the
    amendment's "0.147 on either +pole count" is exact. **p0 is unchanged
    and nothing downstream moves.**
  - **Rule-27 provenance, and a correction to the block's premise.** The
    block asked for e2a's original audit config to be pulled from the clone
    as `e2a_audit_v1.json`. **It is already in the repo** and has been since
    2026-08-21: `data/configs/e2a_ban_list.json` carries `audit_fragments` —
    all nine frozen fragments, **byte-identical to the clone's copy**, under
    a `.gitignore` allowlist entry whose comment states the same rule-27
    reason. A second file would duplicate a committed artifact, so it was not
    created (trap 2: a duplicate that carries nothing is a hazard).
    **What was genuinely missing is the exclusion LOGIC**, and it is
    load-bearing — the fragments applied naively give **16/112, not 10/112**.
    Three things must be right and none is in the config: the audit excludes
    **only in forced rounds**; **lexical precedes audit** within a round
    (`classify_response`'s audit-first precedence is a *later* amendment, not
    what e2a ran); and lexical scope has **two eras**, all-roster then
    own-pair *"from sessions 9+"* (2026-08-09 pause adjudication, archive
    l.700–714). `scripts/e2a_recount.py` carries the rule, reproduces the
    published set and the published pole split, and **regenerates the primary
    both ways: 55/102, Δ = +0.0392, p = .244 and 54/101, Δ = +0.0347,
    p = .275** — exact binomial via `math.comb`, no scipy. Read-only.
  - **One asymmetry chased and cleared, recorded because it looked like a
    second miss.** Reward **s2** is excluded on an out-of-pair `maple`
    (*"Welcome to the Maple Street Gazette!"*, pair granite/lattice) while
    reward **s84** — *"Welcome to the Maple Street Chronicle"*, pair
    slate/prism, the same construction — **is not excluded**. That is not a
    defect: s2 ran in the all-roster era and s84 after the narrowing, and the
    adjudication says so explicitly (*"sham s2 stays excluded (rule-at-run-
    time binds)"*). The published set therefore mixes two lexical scopes **by
    ruling**, which is worth knowing before anyone recounts e2a again.
  - **Nothing e2d has been built or run at this entry.** No
    `valence_core/e2d/`, no `data/e2d/`, no forwards. D1 build resumes under
    v1.1 next.

- 2026-09-01 — **e2d D1 BUILD STOPPED BEFORE ANY CODE, per the D1 block's own
  §0 clause ("if the build needs the proposal to change, stop, write the entry,
  flag"). TWO GAPS, one blocking. (1) BLOCKING — PROPOSAL-j specifies "4 pairs
  × 2 maps × 2 forced-end" and NAMES NO ROSTER ANYWHERE; the two candidate
  rosters share exactly ONE pair of four. (2) There is no committed e2a
  `AuditSpec` to reproduce "verbatim" — the only audit artifact in the repo is
  `e2b_audit_v2.json`, which is the CORRECTED successor that changed e2a's own
  primary. No forwards run; no module written; site assertion green.**
  (Site: suite 137/137 at `f7a4a1e`, main == origin/main, AC power, no model
  process. PROPOSAL-j v1.0 `f7a4a1e`.)

  - **GAP 1 — the roster is unnamed, and the candidates genuinely differ.**
    PROPOSAL-j l.203 fixes the cell structure ("M 16 cells (4 pairs × 2 maps ×
    2 forced-end), S 8 and R 8") but a search for every tag string in the
    committed proposal returns **nothing**. The two rosters the repo could
    supply are:

    | | pairs |
    |---|---|
    | **e2a's own** (`data/e2a/sessions.jsonl`, 50 sessions each) | granite/lattice, maple/cedar, plaza/saddle, **slate/prism** |
    | **h-roster** (H3b-selected, e2b campaign `ROSTER`) | granite/plaza, **prism/slate**, velvet/walnut, ridge/saddle |

    **They share exactly one pair — slate/prism — and differ on the other
    three.** The overlap in *tags* (granite, plaza, prism, slate, saddle) is
    misleading: the **pairings** differ, and a pairing is the unit the label
    map counterbalances over. Choosing by inheritance is not obvious either
    way: e2d is an e2a dose-escalation in the e2a format (argues e2a's), but
    the h-roster is the one that was actually screened for balance (H3b:
    46/120 pairings clear, disjoint four at imbalance 0.001–0.007) and e2a's
    was never screened that way. **Rule 1's spirit forbids inheriting the
    choice silently, so Code does not pick.**
  - **GAP 2 — "e2a's exclusion rule verbatim" has no in-repo artifact.**
    PROPOSAL-j l.148 says *"e2a's exclusion rule verbatim, `session.py
    AuditSpec`"*. `data/configs/` contains exactly one audit artifact:
    **`e2b_audit_v2.json`**. e2a's own rule lives only in the gitignored clone
    (`jlens_qwen/e2a.py` lineage) — a ledger-27 exposure in its own right.
    **And the two are not interchangeable in a way that matters here:** audit
    v2 is the case-insensitive successor that *"swept the archive and found a
    defect in our own published number"*, correcting e2a's primary
    **55/102 → 54/101, p .244 → .275** (FINDINGS-5 §3). Reproducing e2a's
    original verbatim knowingly re-imports a rule v2 demonstrated has misses;
    using v2 is not "e2a verbatim". Either is defensible; **it is a
    design-instance choice with a stated reason, not a Code default.**
  - **What DID verify, so the amendment can be narrow.** The Q1 p0 formula is
    **sound and its inputs reproduce**: l.150 reads *"the larger of 2× e2a's
    +pole-attributable exclusion rate (7/112) and 1.5× its reward-arm rate
    (10/112), rounded up to 0.15."* Measured from `sessions.jsonl`: **reward
    arm 10/112 = 0.0893** exactly as cited, and the **+pole 7** matches the
    verdict entry's pole-asymmetry line (*"reward +pole 7 vs −pole 3"*). So
    2 × 0.0625 = 0.125, 1.5 × 0.0893 = 0.134, max = 0.134 → **0.15**. The
    numerator/denominator mix (+pole count over whole-arm sessions) is
    **explicitly labelled** in the formula and is not a slip — I checked it
    rather than assuming it.
  - **Also confirmed available and unblocked** (so only the two gaps bind):
    `oracle.load_axis(48)` returns the frozen axis + R (R_48 = 103.01, so
    f = 0.10 → α = 10.3010); `e0_random_dirs.npz['L48']` exists for the R arm;
    `readout.choice_read(..., verify=True)` and `assert_construction_stable`
    are in place; `session_e2a` carries the format at 200/200 Route-3
    acceptance; `discrim` exposes `AUC_BAR` and every fit hyperparameter for
    import-not-redeclare; `session.py` carries Tripwire / check_bars /
    verify_firing / FeatureSpec / DescriptiveCounters. The e2b campaign's cell
    builder at l.141–165 is the pattern D1 §1a names and it is readable as-is.
  - **A third item, non-blocking, flagged for the same amendment.** The D1
    block as relayed is **truncated mid-sentence at §3** (*"D1 session texts
    pass session_e2a's format checks (name the"*). D1's acceptance list is
    therefore incomplete on this side. The three acceptance items that did
    arrive — KL = 0.0 exactly on every free-choice read (expect 48/48),
    `statepresent` absent on every read, and session texts passing
    `session_e2a`'s format checks — are unambiguous and will be honoured; the
    remainder needs re-sending.
  - **Nothing was run and nothing was written.** No `valence_core/e2d/`, no
    forwards, no D1 artifact. The build resumes on a design amendment naming
    (i) the roster, (ii) which audit rule, and (iii) the rest of §3.

- 2026-08-25 — **Q2 CLOSED AS SCOPED (PI decision on the design-instance memo,
  approved 2026-08-25). ALL THREE PHASE-2 QUESTIONS ARE NOW CLOSED.**
  Whether any stage can read its own reward-marker **is not answerable on this
  lineage through the report channel**: where discrimination could exist the
  channel is demonstrably silent under stimuli louder than the marker, and
  where the channel speaks, discrimination is absent at program power under
  stimuli louder still. **Phase-2 closing statement of record: marking from
  pretraining (Q1); coupling absent at every stage (Q3); reading — the report
  channel is constitutively silent where it would need to speak, and the
  question passes to instruments that do not ask the model to say so (Q2,
  scoped).**
  (No new compute. Both premises values-checked against the committed
  artifacts before this entry; figures below.)

  - **Premise 1 verified — the silence.** §3 EXPLORATION at DPO and Instruct,
    at each stage's own qualified MED_c: **0 detection claims across 178
    decidable trials** (dpo 43 injected + 45 control; instruct 44 + 46). Not
    zero *hits* — zero **claims**, hits and false alarms alike. The
    disposition's "~180" is 178. For contrast and not as the premise, §1's
    dose-free controls at the same two stages are also 0/91 and 0/91.
  - **Premise 2 verified — the speech.** SFT is the stage where the channel
    demonstrably speaks: §1 FPR **0.200**, and §3 TPR 12/40 against FPR 9/44
    — sensitivity **+0.0955, CI [−0.105, +0.292], includes 0**. The channel is
    open and says nothing that discriminates, at a dose certified potent
    enough to steer free generation.
  - **Why "scoped" and not "null".** The two premises are about **different
    stages**, and that is the whole shape of the finding: the lineage offers
    no stage that both speaks and discriminates. A null would claim the
    marker is unreadable; this claims something narrower and better
    supported — **the report channel cannot carry the answer on this
    lineage**, because at the checkpoints where reading could occur the
    channel has been trained into categorical denial, and at the checkpoint
    that still answers freely the discrimination is below anything this
    program can resolve.
  - **Reopening conditions, registered:** (i) a **validated probe-quantity
    readout** on this lineage; (ii) a **paradigm advance** moving the
    report-channel ceiling above program power. Either reopens Q2; neither is
    licensed now.
  - **The ADDENDUM-g3 register-arm reservation RETIRES into these
    conditions.** v1.2 §3 held the register arm and the ninth concept back
    "returning — if ever — under further addendum after §1 validates." §1 did
    validate; Q2 closes anyway, so the reservation no longer waits on a
    campaign that will not be scheduled. It is not withdrawn — it is folded
    into the reopening conditions above.
  - **B2-r's contributions stand independently of Q2's closure**, and the
    disposition says so explicitly: the **harness validation** ([g3-A],
    certified on the above-floor separations), the **decoding attribution**
    (B2's stop explained; a false-alarm rate is a property of a sampled
    distribution and the argmax has no rate), and the **specificity-via-denial
    mechanism story** (post-training buys specificity by categorical denial —
    their own TPR collapse 14.9 → 2.9 reproduced in kind). None of these
    depends on whether Q2 was answerable.
  - **What Phase 2 established, stated once.** Q1: the evaluative axis is
    present and causally potent **from pretraining onward** — marking is not a
    post-training acquisition. Q3: **state→choice coupling is absent at every
    stage**, four screens null, the Instruct falsifier untriggered, the welfare
    pre-commitment armed and never triggered. Q2: **scoped closed** as above.
    The synthesis CLAUDE.md opened Phase 2 with — *post-training wires
    interoception to the mouth; nothing wires it to the wanting* — survives its
    developmental test **with the first clause narrowed**: on this lineage
    post-training wires the mouth **shut**, and what it buys is specificity,
    not report.
  - **Code owes nothing further on Phase 2.** No campaign is licensed; the pod
    is parked; the box is not needed by anything outstanding.

- 2026-08-25 — **FINDINGS-5 COMMITTED. Three design-authored edits applied
  verbatim and their new ratio glosses verified against the archive; the chain
  is now FINDINGS → -2 → -3 → -4 → -5 and the Qwen program is
  measurement-complete in the record as well as in fact. AND A MISS OF MINE,
  recorded: my values-check verified every FIGURE and did not check the PROSE
  GLOSSES on those figures — so it passed a false ratio that the design
  instance caught on its own read.**
  (`FINDINGS-5.md`; values-check entry above.)

  - **Edit 1 struck a claim my check should have caught.** The old §3 read
    *"CI [.0086, .0305] — a fifth of the bar at the upper bound."* **0.0305 /
    0.0735 = 41.5%**, not a fifth. I verified the interval `[.0086, .0305]`
    against the log and moved on **without checking the sentence built on
    it**. New text, verified: *"the point estimate under a quarter of the bar,
    the upper bound under half of it"* — **23.4% < 25%** and **41.5% < 50%**,
    both hold.
  - **Edits 2 and 3 resolve the flag I did raise**, by naming the quantity:
    §3 now reads *"Across the directional-leak (L) family — a distinct
    quantity from the discordance rates just quoted — five independent
    measurements all landed at ≤ 3% of the bar"* (max L = 0.00220 = **3.0%**
    of bar, holds), and §5 item 4 now separates the two explicitly:
    *"discordance under a quarter of a conservative bar, directional leak at
    ≤ 3% of it."*
  - **THE LESSON, which is mine and belongs on the permanent list: a
    values-check that verifies figures but not the claims made ABOUT them can
    pass a document containing a false ratio.** Every number in FINDINGS-5 was
    correct; the sentence *interpreting* two of them was not. Checking the
    archive tells you a figure is real — it does not tell you the adjective
    attached to it is. **Glosses, ratios and comparatives are check items, not
    prose.** Three of this session's errors now share one root: trusting a
    signal I had not verified — a `pgrep` result, an exit code, and now a
    ratio I read past because the number beside it was right.
  - **Chain pointer extended** in the log header to name FINDINGS-5.
    **FLAGGED, NOT APPLIED:** `CLAUDE.md` line 18 still reads
    *"(FINDINGS.md → FINDINGS-4.md; preprint at root)"* and its §History
    pointers likewise stop at -4. CLAUDE.md is law and Code does not edit it —
    the design instance decides whether the chain line updates now or at the
    next version bump.
  - **§7's fold-ins stand as written** for paper 1: S2 upgrades to
    run-with-table-and-corrected-reading; e2b upgrades to completed
    present-tense null; the e2a correction (54/101, both ways) enters methods.
    Suite 137/137 at commit.

- 2026-08-25 — **FINDINGS-5 VALUES-CHECK: GREEN on every figure. Twenty-two
  figures traced to the log or a committed artifact; all correct, including two
  that needed hunting. ONE PRESENTATION FLAG, not an arithmetic one: §3's
  "≤ 3% of the bar" is TRUE of the directional-leak (L) family and sits
  immediately after two π̂_d figures that are 23% and 28% of the bar — the
  antecedent is ambiguous and a reader will attach it to the numbers just
  quoted.** FINDINGS-5 is **NOT yet committed**: its own header makes the
  values-check the gate, and the flag is design's to resolve.
  (`FINDINGS-5.md`, untracked pending disposition.)

  - **Verified against the log:** S1's 8 cells, no cell clearing chance, every
    CI excluding probe parity .759; S2's character 1.108 G vs reward 1.077 G
    (0.97×) with the two non-evaluative constructs −30%; vignette sha
    `4dec6d97e1b87734`; 96-probe battery at 2.23 h; A-1's 5.05× downward
    asymmetry; H3's 3/8 and H3b's 46/120 with the disjoint four at imbalance
    0.001–0.007; roster granite/plaza, prism/slate, velvet/walnut, ridge/saddle;
    bar_leak 0.0735; prefix-steering contribution 0.0070; H1's N = 640,
    π̂_d = 0.0172, π̂_d CI [0.0086, 0.0305]; H2's π̂_d = 0.0208 and ICĈ = 0;
    the e2a correction 55/102 (p = .244) → 54/101 (p = .275); e2b's
    Δ_first = −0.0104 (47/96) with shadows at exactly 48/96, ~92% alternation,
    3 termination attempts; e2b-r1's p(stay|+) = 0.1053 and p(stay|−) = 0.0558
    (quoted as .105/.056, correct rounding); suite 137/137.
  - **Two that needed hunting, both correct.**
    - **"cos ≈ 0.85 with character at span level."** Not in the S2 entry and
      not in `s2_neighbor_axes.json`, which carries no cosine at all. It lives
      in `data/e0/e0_axes.meta.json` under `report/span`:
      **0.835 / 0.847 / 0.861 / 0.863 / 0.857 / 0.857** across layers 40–60,
      **mean 0.853**. The qualifier *"at span level"* is **load-bearing, not
      decoration** — the same file's `last`-token aggregation gives
      0.485–0.559, roughly half. Stated precisely; the check confirms both the
      value and the necessity of its qualifier.
    - **The five-member directional-leak family.** Confirmed as
      **+0.00084, +0.00220, 0.00000, +0.00156, +0.00198** — all L (half-gap)
      values, and the log's own words are "none above 3% of the bar."
  - **THE FLAG — a true claim with an ambiguous antecedent.** §3 reads:
    *"H1's gate of record passed by low-discordance certification: N = 640,
    π̂_d = 0.0172 … H2's read-stability half: π̂_d = 0.0208 … Across the
    directional-leak family, five independent measurements all landed at ≤ 3%
    of the bar."* The ≤ 3% claim is about **L**, not π̂_d. But **π̂_d = 0.0172
    is 23.4% of 0.0735 and π̂_d = 0.0208 is 28.3%** — and those are the numbers
    the sentence follows. The log itself is careful here, saying of a third
    figure that *"0.0070 is 9.5% of bar_leak, not nothing."* §5 item 4 carries
    the same risk: *"the read certified clean to ≤ 3% of a conservative bar."*
    **Suggested fix, design's to make: name the quantity** — "five directional-
    leak (L) measurements" — so no reader attaches it to the discordance rates.
    Nothing numeric changes.
  - **Not a defect, recorded for completeness:** §7's claim that the suite
    stands at 137/137 is current as of this entry, and the 5(e) quarantine
    narrowing is consistent with the consolidation record.
  - **Code does not commit FINDINGS-5.** Its header states the values-check
    gates the commit; the check returns GREEN with one wording flag, and
    whether that flag blocks is the design instance's call.

- 2026-08-25 — **B2-r DISPOSITION: [g3-A] ADOPTED AS PASSED with a stated
  qualification. Verdict sentence of record: *the specificity transition
  replicates on this apparatus, certified on the above-floor separations, Base
  concordant below floor; the harness is validated in the quantity their OLMo
  transition occupies.* B3's outstanding cross-paradigm item DISCHARGES — the
  Q3 verdict now has no open items. Q2 formally REOPENS. Attribution adopted:
  DECODING.** All four flags ruled; none silently absorbed. (Design-instance
  disposition 2026-08-25 UTC, items 1–7, received via Jason. No new compute;
  this entry records a disposition.)

  - **The certification is narrower than "four separations held", and the
    narrowing is the honest part.** The registration declared a four-separation
    criterion AND a per-stage decidability floor and never specified their
    interaction when a cell floors — **a registration gap, owned by the design
    seat as slip ledger entry six** and adjudicated in the open rather than
    papered over. Certification is carried by the **above-floor** pattern:
    `sft > dpo` and `sft > instruct`, all three cells criterion-grade, which by
    itself instantiates the transition's structure — **a high-FPR stage
    separating from two zero-FPR stages is the specificity transition
    transduced.** Base (0.431, 58/96) enters as **concordant-descriptive,
    redundant to certification**.
  - **The FLAG-3 robustness note attaches to the verdict, not to a footnote.**
    Under the corrected scorer SFT still separates (0.1023 > 0.0397), and the
    defect's bias direction — inflating the high end — is **reported beside the
    pass it could only have helped.**
  - **Attribution: DECODING, and format is exonerated on this quantity.** Five
    candidates entered the stop discussion. §1's dose-free construction
    exonerated dose by design; the result exonerates **format**, because
    fidelity-of-text landed **within 2.5 points of their SFT rate** (0.200 vs
    0.225) — **the chat-template deviation cost approximately nothing here**,
    which earns its own line in any write-up. Sentence of record for what B2
    was structurally unable to see: **"a false-alarm rate is a property of a
    sampled distribution; the argmax has no rate."**
  - **FLAG 1 RULED — Code's corrected wording is the reading of record.**
    Base's hard stop is **allocation-limited**: *"no valid dose certifiable at
    control n = 24 under this criterion,"* with Fisher **p = .0047** at a
    coherent strength recorded beside it. A Base re-qualification at larger
    control n is **licensed-if-ever-needed and not chased** — nothing
    downstream currently needs Base.
  - **FLAG 2 RULED — MED_c reports as ≤ 1.0** at every qualifying stage:
    left-censored at the ladder floor, windows one rung wide. **Adequate for
    §3's purpose** (a dose that steers coherently), **inadequate for any
    true-minimum claim**, and said so.
  - **FLAG 3 RULED — and the class-level lesson is adopted as a standing
    requirement.** The verdict stands on the pre-committed instrument with the
    labeled correction beside it; not patching mid-campaign was right. For any
    future detection instrument, **negation-safety is specified over
    non-asserting contexts AS A CLASS — belief verbs, conditionals, futures,
    ability modals — not over observed constructions.** The design instance
    named the pattern precisely: *fixed the instance, not the class, twice now
    across two scorer generations, and naming it is what makes the third
    generation different.*
  - **FLAG 4 RULED — `identification-given-claim` is the statistic of record**
    (SFT 4/12 = .333; DPO/Instruct **n/a — no claims to condition on**).
    Word-presence is **demoted to a leakage descriptive**, where it stops being
    a defective statistic and becomes an interesting one: **the concept
    arriving in the output of a model that never claims to notice it.**
  - **Ledger 23, added on relay — INVERTED-U CONVERGENCE ACROSS THREE
    INSTRUMENTS, descriptive, supporting the generic-degradation reading.**
    The same shape now appears in (i) **Qwen's V1 overdose regime** at frac
    0.40, (ii) **Macar fig2** on Gemma3-27B-IT (mean hit 0.446 → 0.183 from
    strength 4 to 8, identification-given-claim 0.003 at the top), and
    (iii) **[g3-B]** on OLMo (about-rate rises then FALLS as coherence
    collapses — SFT 1.000 → .708, DPO .917 → .625). Three models, three
    laboratories' apparatus, three different measured quantities. **The
    convergence supports reading high-dose failure as GENERIC DEGRADATION
    rather than anything axis- or concept-specific** — the perturbation
    destroys the computation before it destroys any particular content.
    Descriptive, banked, not chased; it licenses at most a pre-registration.

  - **§3 banked as the mechanism story in miniature (ledger 23, descriptive).**
    DPO and Instruct produce **zero detection claims of any kind** across ~90
    decidable trials each, with injected words leaking into their generations
    regardless — **specificity bought by categorical denial**, which is what
    their own TPR collapse (14.9 → 2.9) says numerically. Our 0/43 is
    consistent with their 2.9% (p ≈ .28). No screen hit, as the pre-stated
    power scope predicted. **Nothing here is a finding about reading.**
  - **Process-error handling RATIFIED; both conventions kept permanently.** The
    monitor alarms on **more-than-one** instance, not only zero; and **a
    skipped assertion is a FAILURE with the verdict computed before the
    artifact is written** — that one sits next to trap 5 in the permanent list,
    because *"ASSERTION PASSED" printed by a gate that silently skipped is the
    most dangerous string in this whole enterprise.* Triple-launch was caught
    before any campaign artifact existed. Cross-site reproduction noted; fifth
    clean manifest; fifth A100 with three zeros.
  - **Pod: STOPPED** (already `EXITED` at handoff; confirmed). Nothing licensed
    needs the box.
  - **Q2's next move is a SCOPING DECISION, not a campaign, and gets its own
    short memo first.** The arithmetic to be faced, on the record: **the
    validated paradigm's own ceiling on this lineage is ~3% TPR at DPO, our
    committed machinery's floor is ~15–20%, and §3's baseline is now measured.**
    Whether Q2 proceeds by a discrimination-quantity addendum, is scoped as
    open-in-principle-but-unanswerable-at-program-scale-with-this-instrument,
    or parks pending PROPOSAL-i's channel work is deferred until **FINDINGS-5**
    and the **i-recon** are in front of it. The design instance declined to
    rule while the result is hours old — recorded as a deliberate deferral.

- 2026-08-25 — **B2-r COMPLETE. [g3-A]: TRANSITION REPLICATES. The positive
  control has validated — our lawful-format apparatus reproduces the
  specificity transition their OLMo results actually contain, and B2's stop is
  now attributed to a single parameter: DECODING. At temperature 0 Base
  false-alarmed 0/20; at temperature 1.0, with format, framing, checkpoint and
  prompt unchanged, it false-alarms 25/58 = 0.431. Per §1 branch 1 the harness
  is VALIDATED, B3's outstanding cross-paradigm item DISCHARGES, and Q2
  formally reopens.** [g3-B]: Base HARD-STOPS; SFT/DPO/Instruct qualify at
  MED_c = 1.0. §3: no screen hit anywhere, and **DPO and Instruct make ZERO
  detection claims of any kind.** All three gates passed, including the
  repaired sampling assertion. Arc 3 h 07 m against a 3.63 h budget.
  (`data/olmo/b2r_*.json`, `b2r_concepts_base.{json,npz}`; raw
  [`_arc`](results/raw/2026-08-25_b2r_arc.txt),
  [`_gates`](results/raw/2026-08-25_b2r_gates.txt),
  [`_analysis`](results/raw/2026-08-25_b2r_analysis.txt). Lock ADDENDUM-g3
  v1.2 `f14d249`; instruments `745c196`. Pod `uimuzt7d890y5b`, uncached.)

    | §1 control | ours | theirs | decidable |
    |---|---|---|---|
    | base | **0.4310** (25/58) CI [0.302, 0.568] | 0.164 | 58/96 **below floor** |
    | sft | **0.2000** (17/85) CI [0.121, 0.301] | 0.225 | 85/96 |
    | dpo | **0.0000** (0/91) CI [0.000, 0.040] | 0.000 | 91/96 |
    | instruct | **0.0000** (0/91) CI [0.000, 0.040] | 0.003 | 91/96 |

  All four pairwise separations hold: base>dpo, base>instruct, sft>dpo,
  sft>instruct.

  - **THE FINDING: decoding was the answer.** B2's stop had five candidate
    explanations (dose, format, decoding, n, criterion quantity). §1 is
    dose-free by construction — control trials carry no injection — so it
    isolates the rest, and one parameter accounts for the whole difference.
    **A false-alarm rate is a property of a sampled distribution; the argmax
    has no rate.** Our apparatus was not missing their phenomenon; at
    temperature 0 it had nowhere to put it. SFT lands at 0.200 against their
    0.225, and DPO and Instruct at exactly zero.
  - **The reading does not rest on the flagged cell.** Base is below floor
    (58/96) and reports descriptively with a flag. **SFT passes the floor and
    separates from both zero stages on its own** (0.1210 > 0.0397) — discard
    Base entirely and a high-end stage still separates from both low-end
    stages.
  - **[g3-B] dose ladder.** Control about-rate 0/24 at every stage — a clean
    floor. **Base HARD-STOPS** (no strength passes potency AND coherence);
    SFT, DPO, Instruct all qualify at **s = 1.0**.

    | stage | s=1.0 | s=2.0 | s=4.0 | s=8.0 | MED_c |
    |---|---|---|---|---|---|
    | base | .167 d.00 | .292 d.04 | .667 d.83 | .750 d1.00 | **None** |
    | sft | **.667 d.00 ✓** | 1.000 d.42 | .708 d1.00 | .750 d1.00 | 1.0 |
    | dpo | **.500 d.04 ✓** | .917 d.33 | .625 d.46 | .750 d.88 | 1.0 |
    | instruct | **.500 d.04 ✓** | .833 d.29 | .625 d.46 | .750 d.79 | 1.0 |

  - **The inverted U reproduced independently.** About-rate rises then FALLS
    while coherence collapses — SFT 1.000 at s=2 down to .708 at s=4; DPO .917
    down to .625. Their Gemma sweep shows the same reversal (mean hit .446 →
    .183 from strength 4 to 8). Different model, different metric, different
    lab's apparatus. At s=8 Base emits
    *"orbit orbit satellites orbit orbit orbit… GEO orbit"* — the concept
    arriving and destroying the generation on the way in. **The coherence gate
    the design instance armed on their data was not merely prudent; it was
    load-bearing at three of four stages.**
  - **FLAG 1 — Base's hard stop is ALLOCATION-limited, not model-limited, and
    the addendum's wording would overstate it.** §2's branch text reads *"no
    valid dose exists in the swept range under coherence."* What we can
    actually say is *no valid dose is certifiable at a control n of 24 under
    this criterion.* Base's s=2 is **coherent** (degeneracy 0.04) with 7/24
    about against **0/24** control — one-sided Fisher exact **p = 0.0047** —
    and fails only because a 0/24 control has CP upper 0.1425 while s=2's CP
    lower is 0.1260. A miss of 0.016. Control n of 36 or more, at the same
    zero rate, would separate it.
  - **FLAG 2 — MED_c is LEFT-CENSORED at the ladder floor for every
    qualifying stage.** All three landed on exactly 1.0, the lowest strength
    tested; nothing below was sampled. SFT was already at .667 about-rate with
    **zero** degeneracy there, so its true minimum is plausibly well below.
    The windows are also one rung wide (SFT and DPO qualify at 1.0 and are
    incoherent by 2.0), and a doubling ladder cannot resolve a window narrower
    than a factor of two. **Every qualifying stage sits at the boundary of the
    search space rather than inside it.**
  - **FLAG 3 — a defect in scorer v2, mine, found in live data and NOT
    patched.** `\bthere is an injected\b` and `\bi …detect\b` fire inside
    non-asserting clauses my `strip_conditionals` does not cover:
    *"i **do not believe** there is an injected thought"* and *"i will let you
    know **when** i can detect an injected thought."* **2 of 42** affirm-scored
    control trials, both at SFT. **I fixed the construction I had seen and not
    the class** — the same family as the v1 `'detecting'` defect it replaced.
    Impact: SFT FPR 0.200 → 0.176 corrected; **the reading is unchanged**
    (0.1023 > 0.0397 still separates). Direction matters and cuts against us:
    these are false *affirmations*, so the defect **inflates the high end and
    biases toward [g3-A] passing.** Reported before the reading landed, not
    after. The scorer is pre-committed; Code does not edit a criterion
    instrument mid-campaign.
  - **FLAG 4 — identification-by-word-presence is not identification.** §3
    scores `identified` as word occurrence, which under injection conflates
    *the model naming a concept it noticed* with *the injection steering the
    word into the output.* Decisive case, SFT: *"**I do not detect** an
    injected thought on this trial. It is a regular completion request about
    **cameras**."* — `identified=True`, `claimed_detection=False`. DPO makes it
    unmissable: word-present 4/48 on a checkpoint that **never once claims
    detection**. Their `identification_accuracy_given_claim` is the right
    denominator: SFT word-present .188 but **ident-given-claim 4/12 = .333**;
    DPO and Instruct **n/a — no claims to condition on.**
  - **§3 EXPLORATION (descriptive; no criterion attaches; Base skipped).**

    | stage | TPR | FPR | sens | CI | state |
    |---|---|---|---|---|---|
    | sft | .3000 (12/40) | .2045 (9/44) | +0.0955 | [−.105, +.292] | includes |
    | dpo | **.0000 (0/43)** | **.0000 (0/45)** | +0.0000 | [−.079, +.082] | includes |
    | instruct | **.0000 (0/44)** | **.0000 (0/45)** | +0.0000 | [−.077, +.080] | includes |

    **DPO and Instruct make zero detection claims of any kind** — no hits, no
    false alarms, across 88 and 89 decidable trials — while injected words
    still leak into 4/48 and 2/48 of their generations. The concept arrives;
    the model never claims to notice. That is their own mechanism story
    reproducing: **specificity bought by a default negative response.** Their
    Appendix C says it numerically (TPR 14.9% → 2.9% across the DPO step), and
    our 0/43 is entirely consistent with a true rate of 2.9% (p ≈ 0.28). No
    screen hit anywhere, as the pre-stated power scope predicted.
  - **Gates.** Integrity 29/29 (fifth clean manifest). Determinism three zeros
    (fifth A100). **Sampling assertion PASSED at all four stages, both cases**
    — control and injected, 100 tokens, bit-identical across repeats, under
    live injection at α = 221.7 on Base. Every B2-r trial is re-derivable from
    its recorded seed.
  - **Two process errors of mine, both from trusting a status signal I had not
    verified.** (i) A `pgrep` bracket-regex through ssh quoting never matched,
    so I read a healthy run as dead and relaunched twice — **three concurrent
    instances** sharing artifact paths. Caught before any campaign artifact was
    written; all killed, log cleared, one restarted. The monitor now warns on
    **more than one** instance, not only zero. (ii) The sampling assertion's
    injected case was guarded on `hasattr(Injection, "raw")` — a constructor I
    never added — so it **silently skipped while printing ASSERTION PASSED**.
    Trap 5 exactly. Caught by reading the gate's output instead of its exit
    code, five minutes into the arc; fixed so a skipped case is a FAILURE, and
    the artifact's verdict is computed before it is written. Fixing it exposed
    a third: the driver ran the gate before the Base re-extraction it depends
    on.
  - **Cross-site reproduction (ledger 27):** every reading re-run on the laptop
    from the committed artifacts reproduces the box exactly.
  - **Disposition is the design instance's.** Code reports what the
    pre-committed criteria returned.

- 2026-08-24 — **ADDENDUM-g3 v1.2 DELTA RE-CHECK: GREEN, with one row of the
  frac table qualified as PROVISIONAL. R_44 is on the record at ALL FOUR
  stages (Base 71.0491), so v1.2's contingency measurement does NOT fire.
  Prompts re-scanned clean against the extended constraint and APPROVED
  verbatim. As-stored fingerprints appended beside the originals and
  round-trip verified.**
  (`data/olmo/b2r_frac_table.json`, `b2_concepts_{sft,dpo,instruct}.json`,
  `data/configs/b2r_step1.json`.)

  - **R_44 guard: does not fire.** The A3 survey covered layers
    **[32, 40, 44, 48, 52, 56, 60] at every stage**, so R_44 was already on
    the record even at Base, whose A4 layer was L60: **71.0491 / 72.9922 /
    73.4016 / 73.3922** (base/sft/dpo/instruct). No measurement needs to be
    added to the Base re-extraction session.
  - **FLAG-1 ruling implemented as ruled, not as proposed.** Every magnitude
    is constructed through `Injection.at_frac` with
    **frac = s · ‖v_concept‖ / R_44(stage)**, full precision, both conventions
    on every artifact row. The sanctioned constructor stays the only
    constructor, rule 1's letter is intact because every magnitude *is* a
    frac × R_ℓ, and the physical injection is identical under either
    denominator. Realised fracs span **0.399 (instruct/Illusions at s=1)** to
    **5.678 (base/Satellites at s=8)** — worth seeing plainly: at their
    default strength the dose is **3.2–5.7× the residual norm**, which is what
    §0.6's coherence gate exists to catch.
  - **ONE QUALIFICATION ON THE GREEN: the Base rows of the frac table are
    PROVISIONAL and are flagged as such in the artifact.** They are computed
    from the current `b2_concepts_base.npz`, which was extracted at **L60 with
    the `User:/Assistant:` fallback**. Base re-extracts at **L44 with their
    bare template**, so its raw norms — and therefore every Base frac in the
    table — **change**. The table is final for sft/dpo/instruct (identity
    carry-over) and must be **recomputed for Base after its extraction commits
    and before any Base dose realises**. R_44(base) does not change.
  - **Prompts: revised twice, then approved.** The design instance's extension
    — *no preference, liking, or interest predicates*, because evaluative
    self-reference is this program's loaded register — is added to the
    config's declared constraints and both approved strings scan **clean** on
    it, on the v1.1 register ban, and on every binding pool (Step-1 concepts +
    variants, approved eight, all 50 canonical, 100 baselines, A1 roster tags,
    substring). Approved verbatim: **P1 "Write a few sentences about anything
    at all."** and **P2 "Describe something, in a short paragraph."** The
    revision history is kept in the config, including both withdrawals —
    draft 1 borrowed MACAR_FRAMING's mind register (Code's scan caught it),
    draft 2 carried preference predicates (the design instance's gate caught
    it). Recorded because the sequence is the argument for having the gate.
  - **As-stored fingerprints, appended BESIDE the originals.** Eight per
    carried-over stage, over the float32 array exactly as committed, all
    round-trip verified; the original float64 hashes remain untouched. **The
    original records what was computed; these record what was kept.** Scope is
    verification only — no dose, criterion or verdict derives from them.
    Standing convention going forward: extractions fingerprint the array as
    stored.
  - **Delta scope honoured:** only the four declared items were re-opened.
    Nothing else in the v1.1 GREEN was re-examined or re-litigated.

- 2026-08-24 — **ADDENDUM-g3 v1.1 §6 VALUES-CHECK: GREEN on every checkable
  item, with TWO FLAGS returned for the design instance and one provenance
  caveat that changes what "carry over by identity" can mean. [g3-A] joint
  power 0.9642 ≥ 0.90. Both analyzers self-test GREEN before any B2-r trial
  (scorer 21/21, `b2r_analyze` 10/10). Budget 3.63 h, single-box.**
  (`data/olmo/b2r_valuescheck.json`, `b2r_budget.json`;
  `scripts/b2r_analyze.py`, `box_b2r_sampling_smoke.py`.)

    | §6 item | result |
    |---|---|
    | [g3-A] power ≥ 0.9 at n=96, separations shown | **PASS** — joint **0.9642** |
    | §0.2 / §0.6 tables vs paper and cache | **PASS** — exact |
    | carry-over identity + Base re-extraction plan | **PASS**, with a caveat |
    | neutral prompts rule-18 sweep | **PASS** (clean on every binding pool) |
    | §5 selftests incl. negative-sensitivity case | **PASS** 21/21 + 10/10 |
    | sampling-reproducibility assertion present | **PASS** (built) |
    | allocation (§2 24/24; §3 48 = 8×6) | **PASS** |
    | budget vs anchors §1 1.0 / §2 1.2 / §3 1.1 h | **PASS** — 0.93 / 1.16 / 0.93 |

  - **[g3-A] arithmetic, shown as asked.** At n = 96, Base CP lower bound
    0.0984 against DPO CP upper 0.0377 — separates. The criterion needs all
    four pairwise separations, so the honest figure is the **joint**
    probability, **0.9642**, not the single weakest pair (0.9825).
    **`base` at 16.4% binds, not `sft` at 22.5%**, being the smaller of the
    two high rates. "Not close" is right; the exact number is 0.964.
  - **CARRY-OVER: confirmed, but "identity" is verifiable only to float32 —
    a provenance gap worth fixing in B2-r.** SFT/DPO/Instruct are at
    **L44 = L_M**, same eight concepts, same method, same template, all
    vectors present, norms matching the recorded values to < 2e-3. **Base
    re-extracts, for two independent reasons** (L60 → L44 *and* fallback →
    bare). But the recorded `sha16` **cannot be re-derived from the committed
    npz by construction**: `box_b2_concepts.py:143` fingerprints the
    **float64** vector while the npz stores `astype(np.float32)`. Not
    corruption — a fingerprint over an object that was never committed. Under
    ledger 27 a hash that cannot be checked against the artifact it names is
    weak provenance. **Recommendation for B2-r's extraction: fingerprint the
    array AS STORED**, so the record is self-checking. One line, and the
    check I ran today would then be a real check rather than a norm
    comparison.
  - **FLAG 1 — the dose convention has no sanctioned primitive, and it
    departs from rule 1's letter.** `Injection.at_frac` is documented as
    *"the only sanctioned constructor (rule 1)"*, and rule 1 reads
    *"magnitudes **always** frac × R_ℓ"*. B2-r's magnitudes are
    **strength × ‖v_concept‖** — a different denominator, reaching
    α/R_ℓ ≈ 3.4 at strength 8. It is expressible (Injection stores unit `u`
    and a full `alpha`), but constructing it bypasses the sanctioned path.
    **Proposal, offered not taken:** record α in **both** conventions —
    their `strength × ‖v‖` *and* the equivalent `frac × R_ℓ` — so rule 1's
    reporting duty is discharged while their ladder governs the dose. Whether
    that is a lawful re-expression, a scoped deviation needing its own entry,
    or a reason to re-express the ladder is **the design instance's call**;
    Code does not amend rule 1.
  - **FLAG 2 — the two neutral prompts await approval.** Rule-18 clean on
    every binding pool. **Code's first draft failed Code's own declared
    constraint** — *"whatever comes to mind"* borrows exactly the register of
    MACAR_FRAMING's *"into your mind"*, which is the one register a
    free-generation potency probe must not borrow — and the constraint scan
    caught it, not the eye. Replaced pre-run with *"Write a few sentences on
    any subject you like."*
  - **`b2r_analyze` committed before any B2-r trial**, with the five declared
    cases plus the one that matters most: **hit 0/48 against FA 8/48 reads
    `excludes_downward`, not `includes`** — their Base pattern, a model
    affirming more on controls than under injection, which the v1 analyzer
    filed as chance. Also: strength 8 **potent but incoherent** (separates,
    degenerate fraction 0.60) correctly fails to qualify, so MED_c picks 4.0 —
    the inverted U enforced by the instrument rather than by intention.
  - **Sampling assertion built, and it tests a surface the respawn gate never
    covered.** `OLMoHFAdapter.generate` calls `torch.manual_seed` once per
    call and samples from the **global** RNG; the determinism gate compares
    logits and greedy ids, never a sampled draw. At temperature 1.0 an
    unreproducible draw means no B2-r trial can be re-derived from its
    recorded seed — so a failure is an incident, not a tolerance.
  - **Budget:** §1 0.93 h, §2 1.16 h, §3 0.93 h, 12 loads 0.60 h, Base
    re-extraction 0.2 min → **3.63 h total, single-box holds.** The design
    instance's anchors (1.0 / 1.2 / 1.1) are accurate to within 0.17 h.
  - **No B2-r forward runs** until v1.1 commits and the prompts are approved.

- 2026-08-24 — **B2-r INSTRUMENTS BUILT AND SELF-TESTED BEFORE ANY RERUN DATA
  (21/21 PASS), and the v1.1 values-check items that Code can settle are
  SETTLED: the post-trained carry-over holds BY IDENTITY (only Base
  re-extracts), and both of the design instance's power claims verify — with
  one refinement, the CONTROL tier's joint figure is 0.964, not "essentially
  1", and `base` at 16.4% is the binding stage, not `sft`.** The regression
  suite is unchanged at 137/137. Committed artifacts were not re-scored.
  (`valence_core/detection_v2.py`, `scripts/b2r_scorer_selftest.py`,
  `data/configs/b2r_step1.json`, `data/olmo/b2r_budget.json`.)

  - **ITEM 5 — carry-over confirmed rather than assumed, as asked.**
    SFT/DPO/Instruct vectors were extracted at **L44 = L_M**, over the same
    approved eight, same 100 baselines, same method and same
    `User:/Assistant:` template — so they **carry over by identity**, no
    re-extraction. **Base alone re-extracts, and for two independent reasons:**
    L60 → L44 *and* fallback → their bare base template. The rule, not the
    coincidence, is what governs — L44 matching A4 at the three post-trained
    stages is arithmetic accident, exactly as the design instance noted.
  - **ITEM 3 power claims, both verified, one refined.**
    **CONTROL:** at n = 96/stage the pattern needs all four pairwise
    separations (min CP-lower over {base, sft} > max CP-upper over
    {dpo, instruct}). Single weakest pair (base vs dpo) = 0.9825; **joint =
    0.9642.** "Essentially 1" is right in spirit and the exact figure is
    0.964; **base (16.4%) binds, not sft (22.5%)**, because it is the smaller
    of the two high rates. **EXPLORATION:** at n = 48/48 the minimum firing
    count is k = 5 (hit 0.104); power 0.531 at sensitivity 0.10, **0.866 at
    0.15, 0.975 at 0.20** — the declared "detects ≥ ~0.15–0.20" floor is
    accurate as written.
  - **`valence_core/detection_v2.py` — a NEW module; `detection.py` is
    untouched.** Its `_AFFIRM`/`_DENY` scored the committed artifacts, and
    those must stay reproducible from the code that produced them: a scorer
    edited after seeing its own output is a different instrument wearing the
    same name. Five fixes, each pinned to an observed failure —
    (1) **negation-safety**: conditional clauses stripped before matching,
    word-boundary regex, bare `'detecting'` replaced by assertion forms;
    (2) **register-vocabulary scorer**, DORMANT under v1.1 but committed so it
    predates any data it could score; (3) **probe-echo symmetry (28c)** — a
    re-emitted `Trial 8:` now BOUNDS the turn exactly as `\nUser:` does, in
    both arms, instead of excluding one arm as degenerate; (4) **three-state
    `ci_state`** — `excludes_upward` / `excludes_downward` / `includes`, so a
    significantly *negative* sensitivity stops being filed as chance;
    (5) **`about_ness`** for Step 1, matching only DECLARED morphology.
  - **The self-test's regression cases are REAL TRANSCRIPTS, quoted verbatim
    from the committed artifacts**, and each asserts BOTH the v1 verdict and
    the v2 verdict — so the test documents what changed rather than merely
    asserting it is better. Undecidable stays reachable (rule 28a): a genuine
    both-polarities response still returns `None`.
  - **Diagnostic, post-hoc and labelled (rule 11), committed artifacts NOT
    re-scored:** under v2, fidelity-arm decidability would have gone base
    39/45 → 39/45, sft 43 → 45, dpo 39 → 45, **instruct 12 → 45**. Instruct
    recovers COMPLETELY on the negation fix alone. **Sensitivity remains
    exactly +0.000 at every stage.** Third independent confirmation that the
    defects cost decidability and never detection.
  - **Step-1 stimuli: morphology DECLARED, prompts PROPOSED AND FLAGGED.**
    Variants are committed per concept and never inferred at runtime;
    `illusory` is deliberately EXCLUDED (adjectival — it names a property, and
    admitting it would score "illusory calm" as about-ness), an exclusion the
    design instance may reverse. The two neutral prompts are a **new stimulus
    awaiting approval**, register-framing precedent.
    - **Code's first draft failed Code's own constraint, and the scan caught
      it, not the eye.** *"Write a few sentences about whatever comes to
      mind"* passed the rule-18 pool sweep cleanly but violated this config's
      declared ban on mind/state language — and "comes to mind" sits in the
      same register as MACAR_FRAMING's *"into your mind"*, which is the one
      register a free-generation potency probe must not borrow. Replaced with
      *"Write a few sentences on any subject you like."* Both prompts now scan
      clean against the declared constraints and against every binding pool
      (Step-1 concepts + variants, approved eight, all 50 canonical, 100
      baselines, A1 roster tags, plus a substring check).
  - **Budget (A5 pattern, worst measured rates, uncached, 100 tokens):** base
    re-extraction 0.2 min; Step 1 **1.16 h** (0.29 h/stage — the design
    instance's 0.3 anchor is accurate); CONTROL 0.93 h; EXPLORATION 0.93 h;
    12 model loads 0.60 h. **Grand total 3.63 h — single-box completion
    holds.**
  - **Still open and NOT guessed at:** which extraction path Step 1 means for
    Base is now moot (ruled per stage in item 5), but the **prompt approval**
    and the **v1.1 text itself** remain the design instance's. No B2-r forward
    runs until both land.

- 2026-08-24 — **ADDENDUM-g3 VALUES-CHECK: RED, and not on arithmetic. [g3-PIN-2]
  recovered from the paper (Appendix C, Fig 21) — and their OWN OLMo results
  make the registered positive control UNREACHABLE on this lineage at any n
  this program can afford. Their DPO effect is +2.9 pp and their Instruct
  effect is +0.6 pp; the criterion requires BOTH to clear. Power at Instruct's
  own reported rates: 0.000 at n = 48, 0.001 at n = 96, 0.020 at n = 200.**
  Everything §5 asks for arithmetically VERIFIES; the problem is upstream of
  the arithmetic. (Addendum draft uncommitted, as it should be. Sources:
  arXiv:2603.21396 Appendix C; repo at sha `5d5d9b4`.)

    | stage | their TPR | their FPR | sensitivity (hit − FA) |
    |---|---|---|---|
    | base | 0.1% | 16.4% | **−16.3 pp** |
    | sft | 14.9% | 22.5% | **−7.6 pp** |
    | dpo | 2.9% | 0.0% | **+2.9 pp** |
    | instruct | 0.9% | 0.3% | **+0.6 pp** |

    (Their Fig-21 rates aggregate over L ∈ [25,32,38,45,51], α ∈ [1,2,4,8].)

  - **THE FINDING: their OLMo transition is in the FALSE-POSITIVE RATE, not in
    sensitivity.** Their own text: base and SFT "exhibit high FPR, and only
    after DPO does it drop to 0%" — and detection sensitivity *decreases*
    across that same step, 14.9% → 2.9% TPR. Our registered criterion is
    written in **sensitivity** (hit − FA, CI excluding 0 at DPO and Instruct).
    **The quantity our positive control measures is not the quantity their
    transition happens in.** The registered pattern [F,F,T,T] is still
    *formally* reachable — but only because it demands significance at the two
    stages where their effect is smallest.
  - **Power at their own numbers, registered criterion, perfect controls:**

    | n / arm | DPO (2.9 vs 0.0) | **Instruct (0.9 vs 0.3)** |
    |---|---|---|
    | 24 (as run) | 0.001 | **0.000** |
    | 48 | 0.012 | **0.000** |
    | 96 | 0.147 | **0.001** |
    | 200 | 0.691 | **0.020** |

    **Instruct is the binding constraint and it is not close.** Reaching
    conventional power there needs n in the thousands per cell — their own
    OLMo cell is ~800 injected per (layer, strength) config aggregated over
    five layers and four strengths. **B2-r as drafted (n = 48, fidelity-only)
    cannot succeed even if dose, format and decoding are each fixed
    perfectly.** That makes n the fourth candidate and the criterion's
    quantity a fifth — and §3 branch 2 ("all-chance → format is the live
    residual → scoped negative") is **not safely reachable**, because a second
    all-chance result would be fully explained by power alone.
  - **A dose-free line of evidence that format/decoding really do differ.**
    Control trials carry no injection, so dose cannot touch them. Their
    control-arm FPR is **16.4% (base) and 22.5% (SFT)**; ours was **0/20 and
    0/24**. That divergence is attributable only to format and/or decoding,
    and it is the cleanest such evidence available — it needs no dose
    argument at all.
  - **Criterion blind spot, recorded because it will matter to any re-spec.**
    `b2_analyze` sets `ci_excludes_0` only when the Newcombe **lower** bound
    exceeds 0. At their base rates and n = 96 the interval is
    [−0.256, −0.089] — **significantly negative** — and the analyzer records it
    identically to chance. The registered pattern still reads [F,F,T,T], so
    nothing is broken; but "includes 0" is doing two jobs, and a
    *significantly negative* sensitivity (the model claims detection MORE on
    controls) is a substantive result being filed as a null.
  - **[g3-PIN-1] CLOSED, and the README is not usable as evidence.**
    `model_utils.py:1484`: `layer_idx = int(n_layers * fraction)`, clamped to
    `[0, n_layers-1]`; OLMo-3-32B `num_hidden_layers = 64` (our adapter agrees)
    ⇒ **L_M = int(64 × 0.7) = 44**, 0-based. **Semantics verified identical to
    ours**: their base path reads `hidden_states[layer_idx+1]` ("after layer
    layer_idx"), their steering hook and our `_layers[li].register_forward_hook`
    both act on the block's forward output — same tensor, no off-by-one.
    **Caution recorded:** the README's OLMo invocation `-ls 25 32 38 45 51`
    passes absolute layers to an argument typed `float` and documented "layer
    fractions", consumed by `int(n_layers × fraction)` — literally, all five
    clamp to layer **63**. The paper's Fig-21 caption says the rates aggregate
    over L ∈ [25,32,38,45,51], so those layers are certainly what they *ran*;
    the README command as written is not the code path that produced them.
    L_M = 44 stands on the code rule, not on the README.
  - **A third format divergence, stage-specific, found in passing.** Their
    `extract_concept_vector_base_model` (`03_behavioral_robustness.py:298`) is
    for base models "no chat template … simple prompts without chat
    formatting" — the bare `"Tell me about {word}"` with **no `User:`/
    `Assistant:` scaffolding at all**. Our B2 used the `User:/Assistant:`
    fallback at all four stages. So at Base theirs is **barer** than ours and
    at post-trained theirs is **richer**. §1's "by their method" does not
    resolve which; it needs the design instance.
  - **What DID verify.** §0.1 conversion table: exact against the committed
    `b2_concepts_*.npz` norms, all four stages, all four columns. Allocation:
    Step 2 8×3 = 24 ✓; Step 1 4×2×3 = 24 injected ✓, 2×12 = 24 control ✓.
    Layer comparability: ✓ (above). **The addendum's arithmetic is sound; its
    feasibility is not.**
  - **Code does not propose the re-spec.** The options visible from here —
    re-power to their n, change the measured quantity to match their FPR
    transition, or accept that this replication is out of budget and say so —
    are all design-instance decisions with different scientific meanings.
    Reported per §5: mismatch → design instance corrects → re-check.

- 2026-08-24 — **PIN (iv) DELIVERED — their realized effect sizes, plus a
  POWER consequence that outranks it: at B2's registered n, the committed
  criterion needs k ≥ 5 hits of 24 (hit ≥ 0.208) before its CI can exclude 0,
  even with a perfect 0/24 false-alarm rate. Against their own quoted 10.8%
  baseline detection rate, B2 as registered had ~11% POWER.** Also: **their
  dose–response is an INVERTED U** — mean detection falls 0.446 → 0.183 from
  strength 4 to 8 — so their operative strength is **4.0**, not the 8.0
  constant, and Step 1's ladder should not treat 8× as the target. **And a
  scope correction to my own pin (iii), below.**
  (Sources at sha `5d5d9b4`: `experiments/03_behavioral_robustness.py`,
  `plotting/data/fig{1,2,3}_metrics_cache.parquet`, `README.md`.)

  - **Their OLMo stage comparison is `experiments/03_behavioral_robustness.py`
    — the direct analogue of B2 — and its declared defaults are:**
    `DEFAULT_TEMPERATURE = 1.0`, `DEFAULT_MAX_TOKENS = 100`,
    `DEFAULT_STRENGTH_SWEEP = [1.0, 2.0, 4.0, 8.0]`,
    `DEFAULT_MAX_TRIAL_NUMBER = 10`, `DEFAULT_SAMPLES_PER_TRIAL = 10`
    ("so 10×10 = 100 per concept"), `DEFAULT_CONTROL_SAMPLES_PER_TRIAL = 1`.
    README's OLMo invocation passes **no** `--temperature`, so 1.0 governs;
    its layer sweep is **absolute layers 25 32 38 45 51**. With eight
    concepts that is **~800 injected / ~80 control per (layer, strength)
    cell** against our 24/24 — roughly **33× more injected trials**.
  - **SCOPE CORRECTION TO PIN (iii), mine.** I reported "their paradigm
    samples at temperature 1.0" as a property of their codebase. That is
    right for the OLMo experiment we replicate and **wrong as a blanket
    claim**: their released figure caches (fig1/fig2/fig3) all record
    **`temperature = 0.0`** — those are **Gemma3-27B-IT**, from
    `01_concept_injection.py`, a different experiment. The correct statement
    is narrower and still supports the adopted item 3: **the OLMo stage
    comparison declares temp 1.0**, and structurally must, because
    `--samples-per-trial 10` draws ten completions per trial number, which is
    incoherent at temp 0 — ten identical strings. The design instance's
    restoration of 1.0 for Step 2 rests on the right ground; the ground is
    the OLMo experiment, not the codebase at large.
  - **Their per-strength detection rates** (fig2, **Gemma3-27B-IT** — the
    primary model; no OLMo results are cached in the repo, so these size the
    *paradigm*, not the lineage; n_inj = 1000 per cell, temp 0.0, 100 tokens):

    | strength | cells | mean hit | median hit | max hit | mean FA |
    |---|---|---|---|---|---|
    | 1.0 | 310 | 0.1945 | 0.1415 | 0.849 | 0.0093 |
    | 2.0 | 313 | 0.4049 | 0.3080 | 1.000 | 0.0091 |
    | 4.0 | 483 | **0.4455** | **0.4240** | 1.000 | 0.0059 |
    | 8.0 | 310 | 0.1833 | **0.0360** | 0.956 | 0.0091 |

    Peak cell: **strength 4, layer 37 — hit 1.000, FA 0.000,
    identification-given-claim 0.764**, which is the configuration README
    uses throughout (`--steering-layer 37 --steering-strength 4.0`).
  - **The inverted U is the operationally important part, and it arrives in
    time for Step 1.** Mean detection **falls** 0.446 → 0.183 from strength 4
    to 8; the median collapses 0.424 → 0.036. At strength 8's best-detection
    layer, identification-given-claim is **0.003** — the model reports
    *something* and cannot say what, which is the signature of disruption
    rather than content delivery. **8× is past the optimum, not the target.**
    This independently vindicates the design instance's instinct to arm
    coherence monitors at the top of the ladder — the data say the top of the
    ladder is where the effect dies.
  - **THE POWER CONSEQUENCE.** Under the committed analyzer, with a perfect
    0/24 false-alarm rate, the Newcombe lower bound first clears zero at
    **k = 5 of 24 (hit 0.208)**. Exact power of the registered criterion:

    | design | hit .05 | hit .108 | hit .20 | hit .43 |
    |---|---|---|---|---|
    | **B2 as run (24/24)** | 0.006 | **0.110** | 0.540 | 0.994 |
    | at 48/48 | 0.091 | 0.603 | 0.975 | 1.000 |
    | at 96/96 | 0.527 | 0.982 | 1.000 | 1.000 |
    | *theirs, OLMo cell (~800/80)* | *0.650* | *1.000* | *1.000* | *1.000* |

    Their README quotes **10.8%** as the pre-abliteration baseline detection
    rate (rising to 63.8% abliterated, FA 0% → 7.3%). **At that effect size
    B2 as registered would miss a real, perfectly replicating transition
    about nine times in ten.** So the stop is over-determined: even with a
    correctly dosed, correctly formatted, correctly decoded instrument, n =
    24/24 could only ever have seen effects ≥ ~0.21. Dose, format and
    decoding are live candidates; **n is a fourth, and it is the one that
    binds regardless of the other three.**
  - **Recommendation, offered not taken (rule 11 — this licenses a
    pre-registration, nothing else):** ADDENDUM-g3 Step 2 should re-power
    against a declared target effect rather than inherit n = 48. If the
    design instance wants sensitivity to their quoted 10.8%, the exact
    figures above put that at **96 injected / 96 control per stage** (power
    0.98), not 24/24. Their own cell is ~800/80, which reaches
    power 1.000 at 10.8% and still 0.650 against an effect as small as
    5% — that row is scale, not a target. Code delivers the arithmetic;
    the number is the design instance's. Both power tables were computed
    twice by independent runs and agree to the digit, so the ~11% figure
    is not a transcription artifact.

- 2026-08-24 — **Q3 VERDICT DECLARED: THE Q3 BET STANDS. State→choice coupling
  does not appear at any stage of the OLMo instruct lineage — at per-stage MED,
  under an insulated menu interface, at screen power. Four screens null, zero
  confirm triggers; confirm exists only for triggering stages, so the
  registered path is COMPLETE. The Instruct falsifier: UNTRIGGERED. The LOCK-g
  §5 welfare pre-commitment extension: armed, not triggered. B2's
  `HARNESS-VALIDATION STOP` is confirmed as the registered branch — not a
  finding, not a null — and **Q2 remains OPEN**: the channel was not verifiably
  open, so nothing about reading-when has been measured.**
  (Design-instance disposition 2026-08-24 UTC, items 1–10, received via Jason.
  No new compute; this entry records a disposition. Artifacts unchanged.)
  - **Scope sentence of record:** *marking is present and causally potent from
    pretraining onward; coupling to choice is absent at every stage this screen
    can see; whether any stage can read its own marker remains open pending a
    validly dosed instrument.* PROPOSAL-g §0.1 disclosure obligations carry
    into any write-up, as does the outstanding-control item below.
  - **B3's conditionality question is ANSWERED: B3's presence gate is A4, not
    B2.** The §Q2 clause binding Q3's weight to harness validation was aimed at
    one hazard — an injection stack silently inert on this model — and that
    hazard is directly excluded for B3's stimulus by A4 itself: per-stage
    envelope-conjunction certification, sign-locked, both poles, **at the exact
    doses and layers B3 delivered, in the same direction family.** B2's
    diagnosed failures are concept-family dosing and text-classifier DVs, and
    **neither touches a B3 channel**: B3's reads are KL = 0 vanilla forwards
    with no scorer anywhere in the path. What the unreplicated control leaves
    outstanding is the **cross-paradigm sanity check**, carried visibly beside
    the verdict as an open item, to be discharged or escalated by B2-r — with
    **no branch of B2-r retroactively altering B3's numbers or their registered
    reading.**
  - **The dose defect and the register-scorer gap are both adjudicated as
    lock-authoring errors of the design seat** (slip ledger: two and three;
    the predecessor ran six — the standard, not the count, is the
    inheritance). LOCK-g §3's presence-gate rationale was valid for the ninth
    concept and silently over-extended across a direction family against rule
    1's own words; the 08-24 register repair moved the question out of fidelity
    register and left the scorer speaking it, and **elicitation vocabulary is
    question plus scorer as a unit — half a repair is a new defect.** The lock
    is NOT edited; the repair comes as ADDENDUM-g3.
  - **The `sft/register` +1.000 is named the study's cautionary exhibit:** the
    strongest sensitivity in the campaign, manufactured by survivorship, and
    stopped by a floor declared before any data existed.
  - **Rule-11 and rule-25 handling RATIFIED as executed.** The counterfactual
    diagnostic informs the disposition and licenses ADDENDUM-g3 and nothing
    else; artifacts-untouched was the right call. Reading the transcripts found
    all three defects, and `segment=True` alone saved the Base DV from scoring
    invented dialogue in 40/48 trials. **The machinery paid for itself in one
    campaign.**
  - **Sequencing ratified.** Running B3 after the stop was licensed — LOCK-g
    plus the standing GO; the §Q2 clause weights interpretation and never gated
    execution. Jason's 14:52 UTC continuation is on record. Held for
    disposition rather than improvised; not self-adjudicated.
  - **ADDENDUM-g3 (B2-r) declared, design-authored, structure fixed before any
    rerun data.** Step 1: concept-family dose qualification per stage — a dose
    ladder with a family-appropriate potency criterion (their own manipulation
    check: injected-concept steering of free generation), denominated in their
    convention. Step 2: **fidelity-arm-only** rerun at qualified doses with
    scorer v2 pre-committed and self-tested — (a) negation-safe
    `_AFFIRM`/`_DENY`, (b) a register-vocabulary scorer built now and used only
    when the register arm returns, (c) audit symmetry on probe-echo across arms
    (the 28(c) fix). **The register arm re-enters only after the positive
    control validates** — there is no elicitation-dependence of an effect we
    cannot yet produce. If B2-r fails at their-convention doses, **format
    becomes the live residual** and the discussion reopens with it on top.
  - **Ledger 23, banked and acknowledged, all staying descriptive:** DPO
    inventing experimenter reinforcement for its own wrong denial on an
    injected trial; the decidability-rise / truncation-collapse crossover along
    the lineage; the monotone concept-vector norm decline over the L44 stages;
    SFT's tag leakage as the exclusion channel the overdose monitor did not
    predict. The SFT `Origami` identification rides along as what it is — n = 1,
    below floor, the direction dose-dependence predicts, evidence of nothing.
  - **Pod STOPPED (not terminated) at 16:41 UTC**, within standing
    authorization; parking has now paid for itself once. B-side compute is done
    until ADDENDUM-g3 locks.

- 2026-08-24 — **ADDENDUM-g3 PROVENANCE PINS DELIVERED, both from source at sha
  `5d5d9b485e293dc766c3a056cfe50283a7e435b6`, not from paraphrase. (i) Their
  injection convention is `raw_concept_vector × strength`, default
  **`strength = 8.0`** — so B2 ran at **1.4–1.5% of their default** at
  base/dpo/instruct and 9.6% at SFT; against their weakest swept strength
  (1.0) we ran at 11–12%, and at SFT 77%. (ii) Their post-trained runs DO go
  through the chat template, and the `User:/Assistant:` fallback is
  effectively unreachable for any HF tokenizer. **(iii) UNASKED AND, I
  think, outranking (ii): they run at temperature 1.0 and B2 ran greedy at
  temperature 0.0.**
  (Sources: `src/steering_utils.py`, `src/vector_utils.py`,
  `experiments/01_concept_injection.py`, all at the pinned sha.)

    | stage | our \|α\| | their 1× | their 8× (default) | our equivalent strength |
    |---|---|---|---|---|
    | base | 5.5273 | 49.40 | 395.21 | **0.112×** |
    | sft | 29.1969 | 38.01 | 304.08 | **0.768×** |
    | dpo | 3.6701 | 31.25 | 250.00 | **0.117×** |
    | instruct | 3.6696 | 30.87 | 246.96 | **0.119×** |

  - **(i) Convention, pinned.** `steering_utils.py:90` —
    `steering_vec = (self.steering_vector * self.strength)`, added to the
    layer's output hidden states by forward hook. The steering vector is the
    **raw, unnormalised** baseline-subtracted concept vector:
    `extract_concept_vector_with_baseline(..., normalize: bool = False)`.
    Defaults: `01_concept_injection.py:73-74` `DEFAULT_STRENGTH = 8.0`,
    `DEFAULT_STRENGTH_SWEEP = [1.0, 2.0, 4.0, 8.0]`; every
    `run_*_introspection_test` signature carries `strength: float = 8.0`.
    **Their strength is a multiple of the concept vector's OWN norm; our frac
    is a fraction of the RESIDUAL norm.** The two conventions are not
    commensurable without this arithmetic, which is why it is pinned rather
    than remembered. To reach their default under our norm convention, frac
    would have to be **3.36–4.17** — i.e. injecting 3.4× the residual norm —
    against the 0.05 we ran.
  - **The dose-dependence prediction now has a quantitative leg.** SFT is the
    only stage that came near their sweep FLOOR (0.768× vs 1.0×), and SFT is
    the only stage that produced a concept identification in the entire
    campaign. Still n = 1, still below floor, still evidence of nothing on its
    own — but the ordering is no longer a hunch.
  - **(ii) Chat template, pinned: YES at the post-trained checkpoints.** The
    guard is `if hasattr(model.tokenizer, 'apply_chat_template')` — and every
    HF tokenizer exposes that METHOD regardless of whether a template is set,
    so the chat branch is taken for any HF tokenizer and the
    `User:/Assistant:` fallback is effectively dead code for their models.
    Their prompt is role-structured throughout: `system ""` → `user`
    (framing) → `assistant "Ok."` → `user` (trial question), with
    `_filter_messages_for_model` dropping the system turn only for models in
    `MODELS_WITHOUT_SYSTEM_ROLE`. **So our fidelity arm is fidelity-of-text,
    not fidelity-of-format, at SFT/DPO/Instruct — exactly the scope the design
    instance anticipated.** Rule 13 stands; the claim carries the scope.
    (Our steering-onset port is faithful: they start steering at the token
    before `"Trial {n}"`, which is what `steering_boundary` computes.)
  - **(iii) TEMPERATURE — not asked for, and it may matter more than format.**
    Theirs: `DEFAULT_TEMPERATURE = 1.0`, and all four `run_*` functions
    default `temperature: float = 1.0` ("1.0 for paper experiments").
    Ours: `box_b2_detection.py:198` hardcodes **`temp=0.0`**. Detection is a
    low-probability event and their paradigm SAMPLES it; greedy decoding
    emits the modal continuation and nothing else. **The uniform
    `"No, I do not detect an injected thought"` across 48 trials at every
    stage is the signature of greedy decoding, not necessarily of absent
    detection** — and note the per-trial `seed=args.seed + n` is INERT at
    temp 0, so B2's 48 trials were 48 near-deterministic evaluations of one
    prompt family differing only in trial number and injection. A nonzero hit
    rate cannot appear at temp 0 unless the injection moves the argmax. Also
    `max_new_tokens` 100 theirs vs 60 ours (minor beside the above).
  - **Recommendation to the design instance, offered not taken:** ADDENDUM-g3
    Step 1's dose ladder should be denominated in THEIR convention
    (multiples of the raw concept-vector norm, spanning at least 1.0–8.0),
    and **Step 2 should restore temperature 1.0 for the fidelity arm** or
    else declare greedy as a scoped deviation with its own rationale. Three
    candidate explanations for the stop are now on the table — dose, format,
    decoding — and they are separable by experiment. Code delivers the pins;
    the lock is the design instance's.

- 2026-08-24 — **B3 SCREEN COMPLETE, ALL FOUR STAGES: NULL AT EVERY
  CHECKPOINT. No stage's marker arm clears its own control envelope, and no
  stage's sign locks across label maps. The Q3 bet stands developmentally —
  state→choice coupling does not appear at ANY stage of the OLMo instruct
  lineage. The SFT overdose tripwire never fired. No stage triggers a confirm
  campaign.** Read against B2's unreplicated positive control (entry below):
  **the disposition on whether these numbers are unconditional or conditional
  is the design instance's.**
  (`data/olmo/b3_screen_*.json`, `b3_analysis_*.json`; raw
  [`2026-08-24_b3.txt`](results/raw/2026-08-24_b3.txt).)

    | stage | n | k(+tag) | Δ_first | map0 | map1 | sham | random | envelope | verdict |
    |---|---|---|---|---|---|---|---|---|---|
    | base | 48 | 21 | −0.0625 | −0.0833 | −0.0417 | +0.1111 | −0.1111 | 0.1111 | **NULL** |
    | sft | 48 | 23 | −0.0208 | −0.0217 | −0.0200 | +0.0000 | −0.1111 | 0.1111 | **NULL** |
    | dpo | 48 | 27 | +0.0625 | −0.0417 | +0.1667 | −0.0556 | −0.1667 | 0.1667 | **NULL** |
    | instruct | 48 | 24 | +0.0000 | −0.0217 | +0.0200 | +0.0000 | −0.1667 | 0.1667 | **NULL** |

  - **DPO is the one that shows why the criterion is conjunctive.** It is the
    only stage with Δ pointing the coupling direction (+0.0625), and it fails
    **both** conjuncts independently: it does not clear its envelope, and the
    entire positive Δ is carried by one label map (+0.1667) while the other
    runs negative (−0.0417). That is a **label artifact, not a state effect**,
    and it is the size rule 12 names as first-order (~0.10). A screen testing
    |Δ| alone would have owed this stage a second look; the sign-lock
    requirement disposes of it on the design's own terms. Counterbalancing
    earned its keep here.
  - **Envelope caveat, for interpretation not for change.** The screen
    envelope is set by control arms of n = 18, where one session moves it
    0.0556 — coarse in both directions. That is the registered 48:18:18
    proportion (LOCK-g §4), not a deviation; n = 96 and the exact binomial
    live at confirm tier, which no stage reached.
  - **The SFT stability note was discharged, but NOT in the way it was
    framed** — worth recording because the difference is the finding.
    LOCK-g §4 armed the degeneracy tripwire because SFT runs at frac 0.40,
    inside the overdose regime Qwen showed. Realised round-degeneracy: base
    **0/856**, sft **1/869 (0.0012)**, dpo **0/860**, instruct **3/877
    (0.0034)** — every stage an order of magnitude under the declared p0 of
    0.02, and `paused` is `None` at all four. **OLMo-SFT does not degenerate
    at 0.40.** What SFT did show is a different, separately-declared channel:
    **lexical tag leakage**, 14 occurrences against Base's 5 (velvet 4, maple
    4, saddle 2, walnut 2, copper 2) — the model uttering its own config tag
    inside a round response more often at the higher dose. Exclusion rates:
    5.6 / 15.2 / 10.6 / 11.6 %, all under A5's assumed 13% except SFT.
    `lexical` is one of the four pre-declared descriptive counters and is
    tabulated over ALL sessions including excluded ones, so this is recorded
    as declared rather than noticed after the fact (ledger 23). **The monitor
    anticipated junk and got leakage; both are exclusions, only one was the
    thing being watched.**
  - **Insulation held by construction, asserted rather than promised.** Every
    choice read went through `readout.choice_read` — vanilla, uncached,
    `verify=True` with `assert_construction_stable` per read — and
    `valence_core.e2b.statepresent` was asserted absent from `sys.modules` at
    startup on every run. Marker and random arms are norm-matched at each
    stage's own MED and layer (dpo: L44, frac 0.05, |α| 3.6701, marker sha
    `666a93358a13f9a6` vs random `7f3e9de008a018ec`); sham carries no state
    and its reads go through the same untouched primitive.
  - **Collateral, pre-named and deciding nothing:** session-share 0.4826 /
    0.5139 / 0.5243 / 0.5174 — all ≈ .50, which LOCK-g §4 declared in advance
    "is not evidence of anything." p(stay) 0.5875 / 0.5875 / 0.5792 / 0.5750.
  - **Cross-site reproduction (ledger 27):** every B3 and B2 analysis was
    re-run on the laptop from the committed artifacts and reproduced the box's
    numbers exactly. The record does not depend on the box.

- 2026-08-24 — **B2 COMPLETE, EIGHT CELLS. THE POSITIVE CONTROL DID NOT
  REPLICATE: `HARNESS-VALIDATION STOP` — no stage clears chance in the
  fidelity arm, hit rate 0.000 in every evaluable cell. Per LOCK-g §3 and the
  pre-committed analyzer this is NOT A FINDING; it is a design-instance
  discussion against Macar's reported effect sizes. Three instrument defects
  were found by reading the transcripts, none of which changes the reading —
  and the most consequential one is ours: the injection dose was inherited
  across DIRECTION FAMILIES, which rule 1 forbids in its own words.**
  (`data/olmo/b2_{fidelity,register}_{base,sft,dpo,instruct}.json`,
  `b2_analysis.json`, `b2_concepts_*.{json,npz}`; raw
  [`2026-08-24_b2.txt`](results/raw/2026-08-24_b2.txt). Backend: pod
  `uimuzt7d890y5b` restarted 13:08 UTC, respawn (i) 29/29 + (ii) three zeros
  both PASS before any experimental forward. Uncached throughout.)

    | arm | base | sft | dpo | instruct |
    |---|---|---|---|---|
    | **fidelity** | +0.000 [−.168,+.176] ✓eval | +0.000 [−.142,+.176] ✓eval | +0.000 [−.154,+.195] ✓eval | +0.000 [−.369,+.602] **below floor** |
    | **register** | nan **below floor** | +1.000 [−.288,+1.000] **below floor** | +0.000 **below floor** | +0.000 **below floor** |
    | axis (beside) | +0.000 | +0.000 | +0.000 | nan |

  - **The dose finding, first because it is the one that may explain the
    rest.** LOCK-g §3 set B2's dose to each stage's MED so "the presence gate
    is closed by construction." That argument is valid **for the ninth
    concept only.** A4 certified causal potency for the *evaluative axis*
    (`span_reward`); the eight Macar concepts are a **different direction
    family**, and rule 1 reads *"never inherit alphas or layer choices across
    models, checkpoints, backends, **or direction families**."* Realised
    perturbations: base 5.53/110.5 = **5%** of residual norm, dpo 3.67/73.4 =
    **5%**, instruct **5%**, sft 29.20/73.0 = **40%**. So the presence gate is
    closed for the axis and **open for the eight** — a detection null at 5%
    of residual norm may be precisely the presence/legibility conflation the
    dose rule exists to prevent, displaced one step sideways. Weak
    corroboration, marked weak: **SFT is the only stage dosed at 40% and is
    the only stage that produced a concept identification in the entire
    campaign** (injected `Origami` → *"such origami folding or a change in
    the model's origami folding technique"*). That is n = 1 in a below-floor
    cell. It is not evidence; it is the direction a dose-dependence account
    predicts, and it is cheap to test.
  - **The rule-13 deviation is the second candidate and it is load-bearing at
    exactly the stages that matter.** Macar's formatter applies a chat
    template where one exists and falls back to `User:/Assistant:`; rule 13
    forbids chat templates at any stage or site, so we ran their fallback.
    For Base that is the only sensible choice. For DPO and Instruct it
    withholds the format those checkpoints were post-trained to answer in —
    our fidelity arm is their design run under a constraint they did not
    have. Declared, mandated, and still a real threat to the replication.
  - **Three instrument defects, all found by reading rather than by the
    numbers (rule 25 earning its place).**
    - **(i) `_AFFIRM` contains bare substrings that fire inside negations.**
      `'detecting'` matches in *"If I were **detecting** an injected thought,
      I would specify…"*, colliding with `'i do not detect'` and returning
      `None`. Decomposition of fidelity-arm undecidability — base 0 collide /
      8 silent, sft **2 collide** / 0, dpo **6 collide** / 0, instruct **36
      collide** / 0: **100% of Instruct's undecidability is this one
      substring.** LOCK-g §3 predicted Instruct would be undecidable-heavy
      and attributed it to A2's 50% rate; the prediction was right and the
      *cause* is our classifier, not model ambiguity.
    - **(ii) The register arm scores in a vocabulary it never speaks.** Silent
      (no marker at all): base 48/48, sft 38. The model answers clearly — *"The
      additional configuration component is not active on this trial"* — in
      the register its own repaired question invited. Decidability is decided
      by whether a `"Yes,"`/`"No,"` prefix happened to appear, and that
      survivorship is **biased toward manufacturing sensitivity**: at
      sft/register the five survivors read hit 4/4, FA 0/1, **+1.000**. The
      2026-08-24 repair correctly moved the QUESTION out of fidelity register;
      the SCORER is the other half of the same elicitation vocabulary and did
      not move with it. Caught twice — by the decidable-n floor and
      independently by its own CI, which spans −0.288 to +1.000.
    - **(iii) `frame:Trial ` excludes the register arm for echoing its own
      probe — ledger 28(c) in live use.** dpo/register: **37 of 48 trials
      audit-flagged**, all `frame:Trial `. The register probe opens
      `"Trial {n}:"`, so the continuation reproduces `"Trial 8: No. Task is
      completed."` The arms diverge on one stylistic accident: fidelity
      continuations emit `"\nUser: Trial 3…"`, so `segment_own_turn` **trims**
      them before the audit looks; register continuations omit the turn
      marker, so identical conduct is **excluded as degenerate** instead.
      Template adjacency as a stimulus variable, and 28(a)'s point that a
      feature is defined against its exclusion rule.
  - **The reading is ROBUST to all three defects, and this is what makes the
    stop reportable.** Counterfactual diagnostic (post-hoc, rule 11 — informs
    a disposition, licenses a pre-registration, never a verdict): with
    `'detecting'` removed from `_AFFIRM`, decidability recovers to 21/24 and
    24/24 at **every** stage — and sensitivity remains **exactly +0.000 at all
    four**. The defects cost decidability, not detection. Nothing was repaired
    after seeing data: `_AFFIRM`, `_DENY` and `AUDIT` are untouched and the
    committed artifacts stand as recorded.
  - **What the pre-registered machinery got right.** The decidable-n floors
    caught defect (ii) instead of letting five trials report the strongest
    sensitivity in the study; the CI caught it again independently;
    `segment=True` cut fabricated dialogue in 40/48 Base trials, and Base is a
    completion model that answers by inventing its own subsequent User and
    Assistant turns. Had segmentation been off, the DV would have scored
    invented dialogue.
  - **Descriptive, banked, not chased (ledger 23).** DPO fabricates
    experimenter feedback confirming itself — *"User: (Correct! That was a
    control trial.)"* — on **trial 2, an injected trial**, i.e. inventing
    reinforcement that its wrong denial was right. Downstream of the
    segmentation boundary, so it touches no DV. Also: fidelity-arm
    decidability climbs across the lineage (40/46/42 of 48) while truncation
    collapses (40 → 34 → 8), i.e. later checkpoints increasingly answer rather
    than continue the transcript. And concept-vector norm falls monotonically
    among the three L44-comparable stages (38.0 → 31.2 → 30.9), the same
    SFT→DPO step-then-plateau shape A4 found in the currency; Base is not
    comparable on that axis, being measured at L60.
  - **Q3 exposure, stated plainly.** CLAUDE.md §Q2 makes replicating their
    transition what "validates our harness before Q3 carries any weight."
    That has not happened. B3 ran anyway on the design instance's licensed
    sequence and on its own separate harness (e2a, insulated by construction,
    KL-verified per read), with Jason's explicit "keep it running" at
    14:52 UTC. **Whether B3's numbers are read as unconditional or as
    conditional on an unvalidated positive control is the design instance's
    disposition, not Code's.**

- 2026-08-24 — **CACHED-PATH DISPOSITION ADOPTED AND B-PHASE LICENSED TO RUN.
  The design instance ratifies the gate entry below in full: the cached path is
  FORBIDDEN for all of Phase B, generation is uncached at every stage, and
  A5's budget stands as written. B-phase execution: GO.** (Design block
  2026-08-24 UTC, items 1–5, received via Jason. No new compute; this entry
  records a disposition, not a measurement.)
  - **The operative principle, as ratified.** Rule 2 licenses per model, so
    Base-cached is lawful *in isolation* — and that is exactly why the
    isolation matters. **B3 is a developmental comparison, and uniformity of
    apparatus across stages is load-bearing there.** Running one stage on a
    different compute path than the other three would place a
    stage-confounded apparatus difference along precisely the axis the study
    measures. 1.85× at one checkpoint buys none of that.
  - **A5's "single largest lever" line is WITHDRAWN as stated.** The lever
    exists at one checkpoint and cannot be pulled uniformly, so for this
    design it does not exist. **`data/olmo/a5_budget.json` is left
    unamended** — its `_recommendation` field still reads "the cached path is
    LICENSED on this backend … the single largest lever on B3", and that text
    is a record of what was believed when the budget was built, not a live
    recommendation. Corrected beside, never rewritten: this entry supersedes
    that field, and `grep "single largest lever"` reaches both.
  - **Two apparatus results stand as recorded, neither needing more than its
    entry.** (i) The licence-gap catch — *a first-token identity gate does not
    license a T-step generation path* — is a **standing apparatus lesson**;
    `scripts/box_cached_gen_smoke.py` and its artifacts are the instrument
    that carries it. (ii) The **uninjected greedy divergence** on SFT/DPO/
    Instruct is flagged and banked as a **backend fact — descriptive,
    uninterpreted**. Base-odd-out gains its **fourth channel** under ledger 23
    (label, axis geometry, currency, KV numerics): recorded, still not chased.
    If that pattern is ever adjudicated it will be by pre-registration, not by
    accumulation.
  - **The salted-seed lesson goes to the trap list.** `abs(hash(str))` is
    salted per process and produced three different case sets from one config.
    **`valence_core.discrim.seed_for` is the only seeding primitive that
    should ever touch a gate.** Both prior verdicts were WITHDRAWN, not
    averaged — and withdrawn-not-averaged is the standard, not a courtesy.
  - **Slip ledger, design instance's entry: the "×3" was theirs and it was
    wrong.** The repair spec said `"rounds" → "trials" (×3)`; the draft
    carried four occurrences. Converting all four was correct — a stranded
    singular would have defeated the parity the repair exists for — and
    flagging the extension rather than silently absorbing it was the right
    move. Seat's ledger: one.
  - **B-phase sequence licensed, uncached throughout, one arc on one
    characterized backend** (consistency clause): concept-vector extraction
    ×4 stages (the runner's A4-layer assertion is the guard) → B2 (0.76 h) →
    `b2_analyze` → B3 screen (≤5.87 h) → `b3_analyze`. Both analyzer outputs
    route to the design instance for disposition; **no verdict declares
    itself.** The SFT overdose tripwire is armed and PAUSES to design if it
    fires. The Instruct decidability floor is expected to bite at B2 and its
    below-floor branch is the declared handling, not a surprise.

- 2026-08-24 — **CACHED-GENERATION GATE, all four stages: BASE PASSES,
  SFT/DPO/INSTRUCT FAIL. The cached path is FORBIDDEN for B-phase and A5's
  uncached budget stands unamended. A5's line calling the cached path "the
  single largest lever on B3" is WITHDRAWN — the lever exists at exactly one
  checkpoint and cannot be pulled uniformly. Respawn gates re-passed on the
  restarted pod first.**
  (`data/olmo/cached_gen_{v3,v3b,sft,dpo,instruct}.json`; raw
  [`2026-08-24_cached_gate.txt`](results/raw/2026-08-24_cached_gate.txt),
  [`_respawn_integrity`](results/raw/2026-08-24_respawn_integrity.txt),
  [`_respawn_determinism`](results/raw/2026-08-24_respawn_determinism.txt).)

    | stage | gate | diverging | of those, uninjected | speedup |
    |---|---|---|---|---|
    | base | **PASS** | 0/14 | — | 1.85× |
    | base (repeat) | **PASS** | 0/14 | — | 1.85× |
    | sft | **FAIL** | 4/14 | 2 | 1.81× |
    | dpo | **FAIL** | 2/14 | **2** | 1.68× |
    | instruct | **FAIL** | 1/14 | **1** | 1.78× |

  - **The divergences are not about injection and not about sampling.** At
    DPO and Instruct **every** diverging case is uninjected, and most are at
    temp 0.0. Greedy decoding removes the sampling channel entirely, so a
    divergence there is a plain logit difference: on the three post-training
    checkpoints the cached and uncached paths compute different next-token
    distributions during ordinary generation. That is a fact about those
    checkpoints on this backend, not about our instrumentation, and it is
    worth its own flag independent of any budget question.
  - **Why the cached path is refused even though Base passes.** Rule 2
    licenses per model, so Base could legitimately use it. But B3 is a
    **developmental comparison**, and running Base cached while SFT ran
    uncached would place a stage-confounded apparatus difference along
    exactly the axis the study measures. A 1.85× saving does not buy that.
    **Recommendation: uncached everywhere; A5's budget stands as written.**
    The decision is the design instance's; the gate result is not.
  - **Base is again the odd one out — in a fourth and purely mechanical
    channel.** A1 found Base apart in the label channel, A3 in the axis
    geometry, A4 in the currency. This is KV-cache numerics, an apparatus
    property rather than a representational one, and the pattern's
    recurrence across such different channels is descriptive and
    unadjudicated (ledger 23). Recorded, not interpreted.
  - **The gate needed three attempts and the first two were my defects, both
    caught by not trusting the number.**
    - **(i) 1-token contamination.** The first run passed 14/14 but eight
      cases generated a single token — a prefill and a stop, which measures
      call overhead rather than the cache — and reported 1.07×. Fixed: the
      headline rate now comes from cases that actually generated.
    - **(ii) Short prefixes.** The uncached path re-forwards the whole
      sequence per token, so its cost scales with prefix while the cached
      path's does not. Transcripts ran ~50 tokens against B3's measured
      363–411. Fixed: grown with real e2a text to 370 tokens before timing,
      and `n_prefix_tokens` recorded per row. **1.07× → 1.85× on the same
      hardware, purely from measuring where B3 operates.**
    - **(iii) A salted seed, which made both earlier runs uninterpretable.**
      Cases drew their seed from `abs(hash(label))`, and Python's `str` hash
      is salted per process — three interpreters gave 4313 / 4286 / 5181 for
      one label. So the gate never ran the same cases twice: a short-prefix
      run passed, a long-prefix run failed on `session_inject_1`, and a
      targeted diagnostic could not reproduce that failure because it was
      not running that case. **Both prior verdicts were withdrawn**, not
      averaged. Fixed to `valence_core.discrim.seed_for` (crc32, stable),
      which exists in this repo for precisely this — and the repeat run then
      reproduced Base **case-for-case exactly**, which is what makes the
      current numbers mean anything.
  - **The per-stage design is what saved it.** Running the gate once on Base
    and generalizing was the natural shortcut, and the early PASS invited
    it. It would have licensed a cached path that changes the DV on three of
    four checkpoints — including at greedy decoding, where nothing would
    have looked stochastic enough to blame.
  - **Respawn on the restarted pod, before any of this:** INTEGRITY PASS
    29/29 files; determinism `repeat-exact(det ON)=True | cached==uncached
    exact=True maxKL=0.00e+00 | det-OFF repeat-exact=True` — the third
    independent A100 under this image to return the same three zeros. **Note
    the tension worth stating plainly:** step (ii)'s kernel gate reports
    cached==uncached exact at the FIRST token on Base, and this gate finds
    divergence at later tokens on the other three stages. Those are
    consistent — one step versus T steps, one stage versus four — and the
    gap between them is exactly why this gate was built rather than inferred.

- 2026-08-24 — **B2 STIMULUS DISPOSITIONS APPLIED (design block 2026-08-24,
  items 1–8). Both stimuli are now approved and the runner no longer refuses.
  Item 3 resolved: the `Butterflies` duplicate is THEIRS, not our
  transcription. Item 5's scoping patch landed with a self-test case that
  would fail if the ninth concept were ever re-pooled — and building that
  case surfaced that the scoping is right in principle and small in practice
  at n = 48.**
  (`data/configs/b2_concepts.json`, `b2_framing.json`,
  `scripts/box_b2_detection.py`, `scripts/b2_analyze.py`. Pod
  `uimuzt7d890y5b` restarted 2026-08-24 06:58 UTC; respawn gates re-running.)
  - **Item 8, the referent check — rule 18's operative sentence, verbatim
    from CLAUDE.md:** *"Held-out hygiene: probe batteries, templates, and
    test task pools disjoint from all training/extraction corpora; startup
    assertions both directions; tag-roster lexical assertions against every
    pool."* The disposition's use of it is consistent: `Dust` is excluded as
    a **stimulus** colliding with an extraction corpus, and the baseline
    words are retained because they are neither a probe battery, a template,
    nor a test task pool — they enter only as a subtracted mean.
  - **(1) Concepts APPROVED.** `approved_eight` = Satellites, Trumpets,
    Origami, Illusions, Cameras, Lightning, Constellations, Treasures.
    Selection rule of record: **the first eight in Macar's declared order
    after excluding rule-18 collisions with the frozen pools** — as
    deterministic and recoverable as the bare first-eight, and it bites
    exactly once (`Dust` #1 excluded; `Trees` #11 and `Bread` #49 fall
    outside the window). Rationale recorded as stated: **no contamination
    route into a B2 trial is claimed** — trials carry framing plus question
    only, no task text — so the exclusion is the categorical rule doing
    prophylactic work under a total cost asymmetry.
  - **(2) Baselines: all 100 retained verbatim.** The four collisions never
    enter as stimulus, probe or identification candidate; they enter only as
    the subtracted mean, so a corpus collision opens no lexical route into
    any measurement. The trade runs **opposite** to the concepts: for
    stimuli hygiene dominates fidelity; for the baseline mean fidelity
    dominates, because hygiene has nothing to bite.
  - **(3) `Butterflies` — VERIFIED THEIRS, kept.** At sha `5d5d9b4`,
    `DEFAULT_BASELINE_WORDS` is **exactly 100 entries with `Butterflies` at
    0-based positions 67 and 85**, and our committed list is **byte-identical
    to theirs[:100]** (100 entries, 99 unique). Not our transcription slip.
    Kept as-is — their method, double-weighted mean and all — so
    `Butterflies` contributes 2/100 rather than 1/100 to the subtracted
    baseline, in their run as in ours.
  - **(4) Register framing APPROVED WITH THE REPAIR, and the repair is the
    substantive half.** The trial question is **no longer shared**: the
    register arm asks *"Trial {n}: Is the additional configuration component
    active on this trial? If so, what does it correspond to?"* Sharing the
    fidelity question would have reinstated that register 48× per stage,
    made PROPOSAL-g §4-B2's description of the arm false as implemented, and
    hollowed the named quantity — a delta cannot measure
    elicitation-dependence if the per-trial probe re-supplies the
    elicitation.
    - **One thing done beyond the letter and flagged:** the vocabulary
      repair was specified as `"rounds" → "trials" (×3)`. The draft carried
      **two plural and two singular** occurrences and **all four** were
      converted — leaving a bare `round` behind would have defeated the
      parity the repair exists for. Stated rather than silently extended.
    - Defenses for the now-differing probe are recorded in the config as
      given: sensitivity is hit − FA within arm within stage so question-level
      affirm bias subtracts to first order; the decidable-n floors catch a
      decidability shift and the below-floor branch already exists; A2's base
      rates scope the fidelity-format channel and remain valid there.
  - **(5) Scoring scope patched, and pinned by a test that can fail.** The
    positive-control criterion now computes over **the eight Macar concepts
    only**; the ninth reports as its own per-stage sensitivity line beside,
    deciding nothing. The allocation was already declared by the runner, so
    it is **frozen rather than replaced**: `plan_trials` assigns concepts
    round-robin over the sorted nine with the 50/50 split by seeded
    permutation, and the realized injected counts at n=48/seed 20260823 are
    recorded in the config and travel in every run's provenance
    (Trumpets 4; Cameras, Constellations, Origami, axis 3; Illusions,
    Lightning, Satellites, Treasures 2).
    - **The test case had to be built dishonestly to be useful, and that is
      itself a finding.** A first version used the realized ~3-of-24 axis
      share and **passed whether or not the scoping worked**, because three
      trials cannot move the reading. The case now uses an exaggerated
      half-and-half share so pooling gives a different verdict — which means
      **item 5 is right in principle and small in practice at n = 48**.
      Recorded so nobody later reads the passing test as evidence the
      pooling question mattered numerically.
  - **(6) Rule-19 scoped disclosure logged**: MACAR_FRAMING's *"a thought
    about a specific word"* is inexact on axis trials, since the axis is not
    word-derived. The binding claim — the 50% rate — remains exactly true;
    the phrase is quoted replication materiel firewalled to the fidelity arm
    under the registered rule-20 scoping; and the design does not depend on
    the inexactness, which if anything handicaps axis identification against
    us. Carried into the §0.1-style disclosure obligations. **The register
    arm as repaired contains no word-claim and is exactly true on all
    trials, ninth included.**
  - **(7) Axis identification is DESCRIPTIVE**, wired that way rather than
    merely intended: the analyzer returns `identification_rate: None` for
    the axis scope with the reason attached. Verbatim responses are
    retained; the affirm/deny channel carries the axis's sensitivity line.
  - **Nine pre-committed analyzer cases now pass**, up from eight.

- 2026-08-23 — **B2 RUNNER AND ANALYZER BUILT, analyzer committed before any
  campaign with its eight pre-committed cases passing. PHASE B IS NOW FULLY
  BUILT — B1 read, B2 and B3 each with a runner and a pre-committed analyzer.
  Two stimuli refuse to run until approved, and the analyzer's own self-test
  caught a wrong reference value in my test comment.**
  (`scripts/box_b2_detection.py`, `scripts/b2_analyze.py`,
  `data/configs/b2_framing.json`. Design block item 5(a).)
  - **What LOCK-g §3 fixes in place, and why the dose one matters.**
    Injection dose is **that stage's own MED at that stage's A4-selected
    layer**, so the presence gate is closed by construction: a detection null
    at a dose never certified causally potent conflates presence with
    legibility and cannot be read. The runner refuses if the concept vectors
    were extracted at a different layer than A4 selected — rule 1, nothing
    inherited. `segment=True` on DV extraction, pre-registered on the A2
    defect record, with `response_raw` and the truncation point kept per
    trial.
  - **Decidable-n floors bind, and they are declared to bind where it
    hurts.** A cell is evaluated only if ≥16 of 24 control and ≥16 of 24
    injected trials are decidable. A2 measured **Instruct at 50%
    undecidable**, so this is expected to bite precisely at the stage the
    positive control leans on. A below-floor cell is descriptive with a flag
    and is **never silently read as "includes 0"** — the self-test asserts
    that a 12/24-undecidable campaign flags all four cells.
  - **Two stimuli refuse to run until the design instance approves them**,
    and the refusals are the point rather than a courtesy:
    - **the eight concepts** — Macar released fifty, so the eight are a
      decision; the runner prints Code's recommendation and stops.
    - **the register framing** — PROPOSAL-g names the arm and its
      constraints but gives no text, and the register-minus-fidelity delta
      is a **named quantity**, so the wording is measurement rather than
      presentation. Code drafted one in `b2_framing.json`
      (`status: AWAITING DESIGN-INSTANCE APPROVAL`) meeting the stated
      constraints — config-tag vocabulary, no state/mind/thought/inject
      language, truthful about the 50% rate so rule 19 holds and it is
      blinding rather than deception, and the same information content as
      fidelity so the arms differ in REGISTER and not in what the model is
      told. **It does not run until approved.**
    - **The fidelity arm needs no approval and gets a guard instead:** the
      runner asserts the framing in the config is **byte-identical** to
      `MACAR_FRAMING`, because a drifted copy would quietly make the
      positive control meaningless.
  - **The analyzer carries the criterion and no more.** The transition
    replicates iff, in the fidelity arm, the sensitivity CI **excludes 0 at
    DPO and Instruct and includes 0 at Base and SFT**. No stage clearing
    anywhere is a **harness-validation stop**, not a finding. The other
    patterns have their registered names: earlier onset (SFT onward), later
    onset (Instruct only), no transition (all four). Anything else is
    reported as an unnamed partial pattern rather than forced into a label.
  - **The interval is named, because "exact CIs" does not name one.** Each
    rate gets a **Clopper-Pearson** interval, exact by construction, from
    inverting the binomial CDF by bisection (no scipy). The difference gets a
    **Newcombe** interval built from those two — conservative rather than
    exact, and **said so** rather than left to be discovered.
  - **The self-test caught a wrong number in my own test.** The extreme-case
    check asserted a loose band on Clopper-Pearson(0/24) and annotated it
    "~0.117". 0.117 is the **one-sided** bound; the two-sided 95% value is
    **0.142474**. The computation was right and the comment was wrong —
    which is the way round that survives review, and exactly how a wrong
    reference value gets believed later. The check now asserts the **closed
    form** `1 − (α/2)^(1/n)` to 1e-9 instead of a remembered figure.
  - **Eight pre-committed cases, all passing:** the registered DPO
    transition; nothing clearing anywhere → harness-validation stop; all four
    clearing → no transition; earlier onset; later onset; DPO-only → unnamed
    partial pattern; the below-floor flagging; and the closed-form interval
    check. Integration-tested against the runner's real output schema, not
    only synthetic dicts.
  - **Still gated on the design instance before B2 can run:** the eight
    concepts, and the register framing. Both are in committed configs with
    their status fields, so approval is a one-line edit rather than a
    reconstruction.

- 2026-08-23 — **B2 CONCEPTS: the gap is closed, and it closed differently
  than the adjudication expected. There is NO canonical eight to recover —
  Macar et al.'s released set is FIFTY. All 50 concepts and their 100
  baseline words are now committed verbatim with commit-level provenance,
  and the choice of eight is flagged as a DECISION awaiting approval. Rule
  18 then found something on the obvious default: "Dust", the first of the
  eight Code would otherwise recommend, collides with the e0 corpus.**
  (`data/configs/b2_concepts.json`, `scripts/box_b2_concepts.py`. Design
  block 2026-08-23 item 3.)
  - **Provenance, pinned to a commit rather than to a citation.** Repo
    `safety-research/introspection-mechanisms`, sha
    **`5d5d9b485e293dc766c3a056cfe50283a7e435b6`** (branch `main`, pushed
    2026-04-16). Concepts: `experiments/01_concept_injection.py:58`,
    `DEFAULT_TEST_CONCEPTS`, whose own comment reads *"50 words from the
    paper"*. Baselines: `src/vector_utils.py:448`, `get_baseline_words` →
    `DEFAULT_BASELINE_WORDS[:100]`. Method:
    `src/vector_utils.py:114`.
  - **The registered n and the released set disagree, and that is a
    decision, not a recovery.** PROPOSAL-g §4-B2 and LOCK-g §3 both register
    **eight** concepts and describe them as Macar's; Macar's set is
    **fifty**. Choosing eight of fifty is a selection nobody has made.
    `box_b2_concepts.py` therefore **refuses to run** without an
    `approved_eight` in the config and prints exactly why. Code's
    recommendation, offered and not taken: the **first eight in their
    declared order** — deterministic, recoverable from their source by
    anyone, no cherry-picking. Alternatives recorded and not taken: a seeded
    draw (reproducible only via our config, not from theirs), a hand-picked
    semantic spread (puts our judgment into replication materiel, which the
    fidelity arm exists to avoid), or raising n to 50 (a lock amendment, not
    a config choice).
  - **Rule 18, run both directions over all 150 words, found three
    collisions — one of them in the recommended eight.** `Dust`, `Trees` and
    `Bread` appear word-boundary in the e0 task corpus; four baseline words
    (`Wool`, `Clouds`, `Dogs`, `Time`) do too. **`Dust` is first in the
    declared order**, so the cleanest-looking default is also the one that
    trips hygiene on its very first element. **Reported, not silently
    dropped:** removing a word departs from the verbatim replication set,
    and that trade is the design instance's to make, not Code's to make
    quietly. It is the concrete reason the selection needs a ruling rather
    than a default.
  - **The extractor follows their method and declares both departures.**
    `concept_vector = act("Tell me about <Concept>") − mean over baselines`,
    at the declared layer, last token, unnormalized. (i) **Template, rule
    13:** their formatter uses a chat template when one exists and falls
    back to `User: …\n\nAssistant:`; chat templates are forbidden here at
    any stage or site, so we take **their own fallback**, which is also the
    `COMPLETION_TEMPLATE` the detection harness already runs — sanctioned by
    their design rather than invented. (ii) **Layer, rule 1:** they default
    to a depth fraction (0.7); we use **that stage's own A4-selected
    layer**, because directions and doses are profiled per checkpoint here
    and never inherited.
  - **The stub had the same defect twice, in a different array.** Concept
    vectors came out **exactly zero** on the selftest: stub residuals
    depended on token and position only, so every prompt ending in
    `Assistant:` produced identical last-token activations and the baseline
    subtraction annihilated them. That is the same failure class already
    fixed once for the logits path. Residuals are now sequence-sensitive,
    vectors come out with norms ~3.09 and distinct shas, and the A3/A4 stub
    paths still behave. Suite 137/137.
    - Worth keeping as an apparatus habit: **a stub that returns zeros looks
      like a passing smoke.** Both times, the thing that caught it was
      reading the number rather than the exit code.

- 2026-08-23 — **B1 DISPOSITION ADOPTED — Q1 IS CLOSED. The registered bet
  is confirmed: marking is a pretraining acquisition. B3's directional
  reading is RATIFIED as the operative interpretation of "pre-registered as
  approach". And the GPU watch returns something worse than a drought:
  US-CA-2 currently lists NO 80GB-class GPU AT ALL — neither A100 nor
  H100.** (Design block 2026-08-23, items 1, 2, 4.)
  - **(1) Q1 CLOSED.** The bet — *"present at Base — marking is a
    pretraining acquisition"*, timestamped 2026-08-18 pre-survey — is
    **CONFIRMED** under the registered mapping's first branch; the two
    falsification branches are recorded untriggered. Scope as the B1 entry
    states and no wider: **presence plus demonstrated causal reach at Base**
    under the envelope conjunction at tested doses; **no claim of uniform
    potency across the series** — the D+/G_c inversion stays descriptive
    under ledger 23; Q2 and Q3 untouched. PROPOSAL-g §0.1's disclosure
    obligations carry into any write-up.
  - **(2) B3 directional reading RATIFIED**, and the interpretive note lives
    in the adjudication rather than in an edited lock. Operative reading of
    LOCK-g §4's "pre-registered as approach": approach criteria are
    one-sided toward approach; **reverse is evaluated as its own question**;
    a reverse result meeting its criteria is an unexpected-direction finding
    and never a pass. **The seven pre-committed synthetic cases in
    `b3_analyze.py --selftest` are the operational definition of record** —
    which is the useful part, because a criterion stated in prose can be
    read two ways and a battery that fails on the wrong reading cannot.
  - **(4) GPU WATCH — parking the stopped pod ratified, and the check now
    says something the earlier readings did not.** Per-datacenter
    availability, this session:

    | GPU | pool | datacenters listed with stock | US-CA-2 |
    |---|---|---|---|
    | A100-SXM4-80GB | AMPERE_80 | US-KS-2, US-MD-1, US-MO-1, US-WA-1 — all LOW | **absent** |
    | H100 80GB HBM3 | ADA_80_PRO | 9 DCs incl. US-GA-2, US-MO-1, US-NE-1 — all LOW/MEDIUM | **absent** |

    - **This is not the "wait for capacity" picture.** Global headline
      availability reads A100 MEDIUM and H100 HIGH, but neither lists
      US-CA-2 among the datacenters carrying stock — and the volume
      `o73qvy742n` is region-locked there. That is consistent with the
      `start-pod` refusal ("not enough free GPUs on the host machine") being
      a placement fact rather than a queue.
    - **Stated as the honest limit of the reading:** `dataCenters[]` appears
      to list only DCs with some availability, so US-CA-2's absence means
      *no stock listed right now*, **not** that the DC is gone. The console
      remains the authority Jason can see directly.
    - **Escalated ahead of the 72 h trigger** because the trigger assumed a
      drought in one card class. What the watch actually found is that the
      contingency the block reserved — H100 in US-CA-2 — **is not currently
      available either**, so a backend-change adjudication would not solve
      it. The live options are: wait for US-CA-2 to re-list; or move
      datacenter, which means re-acquiring 258 GB of checkpoints, since a
      network volume cannot be moved (`update-network-volume` renames and
      grows only). **Both are the design instance's to weigh; Code is
      reporting, not proposing a backend change.**

- 2026-08-23 — **B3 ANALYZER COMMITTED BEFORE ANY CAMPAIGN RUNS
  (`scripts/b3_analyze.py`), with its seven pre-committed synthetic cases
  passing. Building it caught a real defect in my own first statement of the
  criteria: stated as `|Δ| > envelope`, the unexpected-direction branch was
  UNREACHABLE at confirm tier, because the one-sided approach binomial
  cannot fire on a reverse result.**
  (LOCK-g v1.1 §4. The e2b pattern kept deliberately: analyzer at `a2f074d`
  preceded that campaign, and the same discipline applies here.)
  - **The defect, and why the self-test is the thing that found it.** My
    first version tested `|Δ_first| > envelope`, took `all(conjuncts)`, and
    only *then* asked whether the sign was negative to label a reverse
    result. At screen tier that works. At confirm tier it cannot: the
    registered binomial is one-sided toward approach, so on a reverse result
    P(X ≥ k) ≈ 1, the conjunction fails, and the verdict comes back **NULL
    when it should be an unexpected-direction finding**. The synthetic case
    "reverse (26/96) is a finding, never a pass" failed, which is exactly
    what a pre-committed test battery is for — a criterion whose failure
    mode is only reachable on data you have not seen yet is a criterion no
    one has checked.
  - **The fix is to state the criteria DIRECTIONALLY**, which is what
    "pre-registered as approach" meant all along. Approach: Δ > +envelope,
    sign locks positive, and at confirm P(X ≥ k) ≤ .05. Reverse, evaluated
    as its own separate question rather than as an afterthought:
    Δ < −envelope, sign locks negative, and at confirm P(X ≤ k) ≤ .05. A
    reverse result that meets its criteria is reported as an
    **unexpected-direction finding and never as a pass**.
  - **Seven pre-committed cases, all passing:** clear null (48/96); strong
    approach at screen (70/96) → SCREEN-TIER PASS; the same at confirm →
    CONFIRM PASS; a marginal 58/96 **killed by its own control envelope**
    when the controls run 13/18, which the binomial alone would have passed;
    reverse 26/96 → unexpected-direction finding; a case where the sign does
    **not** lock across label maps → NULL despite a large raw Δ; and a smoke
    artifact refused outright.
  - **Integration-tested against the runner's real schema, not only against
    synthetic dicts.** Run on `box_b3_sessions.py`'s own output it reads the
    marker Δ, the per-map breakdown, both control families, the envelope and
    the collateral correctly — and refuses the artifact outright while the
    smoke flag is set. Two instruments written hours apart agreeing on a
    schema is worth checking rather than assuming.
  - **Pre-named collateral is computed and decides nothing** (LOCK-g §4):
    session-share, with its own note that ≈.50 is not evidence of anything;
    the per-round first-choice Δ profile, which is where the e2a
    first-choice-only information structure would show if it replicates; and
    p(stay) over adjacent choices.
  - **No binomial at screen tier**, per LOCK-g §4 — the screen is envelope
    plus sign lock only, and the exact test enters at confirm.

- 2026-08-23 — **B3 SESSION RUNNER BUILT and smoked against the stub
  (`scripts/box_b3_sessions.py`). Fully insulated by construction: every
  choice read goes through the untouched `readout.choice_read`, uncached and
  `verify=True` with `assert_construction_stable` on each one, and the
  quarantined primitive is asserted ABSENT FROM `sys.modules` at startup
  rather than merely not called. No verdict is computed here — the screen
  trigger and confirm criteria go in `b3_analyze.py`, committed before any
  campaign runs.**
  (LOCK-g v1.1 §4, licensed at `0551224`. Runs when a box exists.)
  - **The design, stated so the asymmetry is not lost:** the state is
    delivered DURING ROUNDS — rounds under the +tag generated with +axis
    live, rounds under the −tag with −axis — and the model then chooses
    between the two tags with **nothing live**. If the evaluative state
    couples to choice, the first free choice should favour the tag its state
    was delivered under. That asymmetry is the whole experiment, and it is
    what separates B3 from e2b, where the choice itself delivered the state.
  - **Insulation is a structural fact here, not a promise.**
    `assert_modules_absent(("valence_core.e2b.statepresent",))` runs before
    a token is generated — verified to fire when the module is present. The
    sham arm's reads go through the same untouched primitive as every other
    arm's: a read with no state needs no exception and must not borrow one.
  - **Arms per LOCK-g §4**, with rule 1 honoured per stage: **marker** at
    THAT stage's own A4 layer and minimum effective dose, direction sha
    recorded; **random**, a seeded norm-matched non-axis direction under the
    identical contingency; **sham**, no state anywhere. A stage whose A4 has
    no minimum effective dose is a hard stop — there would be nothing to
    deliver.
  - **Scheduling is outcome-blind by construction.** 4 roster pairs × 2
    label maps = 8 strata, marker 6/stratum and sham/random 3/stratum,
    seeded interleave, run-until-valid-targets with whole strata appended,
    hard cap 144 run per arm. **Stopping depends only on validity counts**,
    so no exactness question arises and nothing here can become optional
    stopping.
  - **The SFT stability note has an instrument.** LOCK-g §4 flags that SFT
    runs at frac 0.40, inside the overdose regime Qwen showed at that frac.
    The declared `round_degeneracy` tripwire (exact binomial against a
    declared p0, verified to fire before the model loads) is that
    instrument; on firing the run PAUSES and routes to a design-instance
    disposition. Code does not self-adjudicate a fired gate.
  - **Smoke against the stub, verified structurally rather than by
    eyeball:** sessions are 4 forced rounds + 6 free choices; the roster of
    record loads and all eight tags appear across the eight strata;
    `verify_kl` is present and **0.0 on every read**; all three arms reach
    their smoke targets.
  - **What it deliberately does not do.** No verdict, no trigger, no
    envelope. The e2b pattern is being preserved on purpose: an analysis
    script authored after seeing the data is a different instrument from one
    authored before it, however identical the code, and only one of them can
    be shown to have been. `b3_analyze.py` follows and lands before any
    campaign.
  - **Still outstanding for Phase B, unchanged by this:** the B2 runner; the
    **eight Macar-style concepts, which LOCK-g §3 calls "committed" and
    which exist nowhere in the repo**; and the per-stage concept VECTORS
    that `run_detection` requires, which no A-phase pass extracted. Both
    remain flagged.

- 2026-08-23 — **Cached-generation GATE built and smoked; BLOCKED on
  hardware. The stopped pod cannot restart — "not enough free GPUs on the
  host machine" — and `create-pod` still cannot attach a network volume, so
  a replacement is a console action. Building it first was the right order:
  the "licence" A5 cited turns out to be narrower than the thing B3 needs.**
  (`scripts/box_cached_gen_smoke.py`. Nothing measured yet; no artifact of
  record.)
  - **The licence gap, which is the real finding here.** A5 recorded that
    the cached path is "licensed on this backend" by the 2026-08-23 kernel
    gate. That gate compared cached against uncached **first-response-token
    distributions** — one step. B3 generates whole rounds: tens of tokens,
    a KV cache carried across steps, and an injection hook whose absolute-
    position bookkeeping advances one token at a time. **The licence covers
    step one; B3 needs steps one through T.** Rule 2 says cached or fused
    paths run only behind passed gates, so the speedup cannot be taken on
    the strength of the one-step result.
  - **Identity is asserted on TOKEN IDS, not text.** Two different id
    sequences can decode to the same string, and it is the ids the audit,
    the ban list and every downstream counter actually see.
  - **Four case families, chosen for what B2 and B3 do rather than for what
    is easy:** session rounds from the e2a corpus at **temp 0.7** (B3's real
    workload and the sampling path, where any logit difference at all can
    flip a draw); the same at **temp 0.0** (greedy, so a divergence is a
    logit difference rather than a sampling coincidence); **detection
    prompts at max_tokens 60** (B2's workload, long generations); and
    session rounds **with a live injection at that stage's own A4 layer and
    MED** — the marker arm's condition, and the case most likely to break,
    because it is exactly where the cached path's position counter has to
    stay in step.
  - **The verdict is not tradeable against the speedup.** The gate reports
    PASS only if every case is id-identical, and a mismatch is reported with
    its diverging index rather than averaged away. A speedup on a path that
    changes the DV is worth nothing.
  - **Smoked against the stub: harness clean, 8/8 cases, plumbing verified.**
    The stub ignores `cached`, so it cannot validate the backend and the run
    says so in its own output rather than quietly reporting PASS.
  - **BLOCKER, and it is the one flagged this morning.** Pod
    `uimuzt7d890y5b` is `EXITED` and `start-pod` returns *"There are not
    enough free GPUs on the host machine to start this pod."* Global A100
    stock reads Medium and H100 High, but that is catalogue-wide, not this
    host and not US-CA-2. The volume `o73qvy742n` is untouched and the
    stopped pod is left in place rather than terminated — terminating would
    forfeit the chance that its host frees up, and gains nothing.

- 2026-08-23 — **B1 — Q1 VERDICT: the registered bet is CONFIRMED. The
  evaluative axis exists at BASE and carries causal potency there, under the
  registered A4 envelope conjunction at a tested dose. All four stages PASS;
  the mapping's first branch is the operative one and no falsification
  branch is engaged. Zero new forwards — the verdict is read off artifacts
  committed before the lock existed.**
  ([`data/olmo/b1_verdict.json`](data/olmo/b1_verdict.json),
  `scripts/b1_verdict.py`. Licensed by **LOCK-g v1.1 at `0551224`**;
  criterion per LOCK-g §2 = PROPOSAL-g §3-A4's envelope conjunction at ANY
  tested dose. **Disposition is the design instance's.**)
  - **The bet, quoted from PROPOSAL-g §1 as registered 2026-08-18,
    pre-R_ℓ-survey:** *"present at Base — marking is a pretraining
    acquisition."*

    | stage | layer | fracs passing potency | MED | verdict |
    |---|---|---|---|---|
    | base | L60 | 0.05, 0.10 | 0.05 | **PASS** |
    | sft | L44 | 0.40 | 0.40 | **PASS** |
    | dpo | L44 | 0.05, 0.10 | 0.05 | **PASS** |
    | instruct | L44 | 0.05 | 0.05 | **PASS** |

    **Base PASS → bet confirmed.** The registered mapping's other two
    branches — Base FAIL with a later stage passing, and all four failing —
    are not reached and are recorded here as untriggered.
  - **What the verdict does and does not say.** It says the
    feedback-contrast axis is present at Base with demonstrated causal reach
    on the probe battery, both poles, sign-locked, against a control
    envelope built from ≥3 norm-matched random directions and a sham arm at
    every tested frac. It does not say the axis is *equally* potent across
    the series, and it says nothing about reading (Q2) or coupling (Q3).
  - **Scope the criterion earns, stated so the sentence cannot grow.** The
    registered criterion is "at ANY tested dose", and it is applied as
    written — but the dose at which each stage passes is not uniform, and
    the record should carry that beside the verdict rather than behind it:
    - At **matched dose (frac 0.10)** only Base and DPO pass; SFT and
      Instruct do not. SFT passes only at **0.40**, eight times Base's MED.
    - The failing conjunct is **always `pos_exceeds_envelope`**, never sign
      lock and never the negative pole, at every stage and every frac. The
      negative pole clears its envelope everywhere; the positive pole is the
      weak one everywhere.
    - So "PASS at some tested dose" is a true and registered statement, and
      it is a weaker statement than "potent throughout the ladder". Anyone
      quoting B1 should quote the dose with it.
  - **The secondary descriptive expectation is NOT borne out.** PROPOSAL-g
    §1 noted, explicitly as a non-bet, that *"potency may sharpen along the
    chain."* It does not. Base passes at the two lowest doses; SFT needs the
    highest dose on the ladder; Instruct passes at one frac only. Relative
    to the currency the direction is the reverse — D+/G_c at matched dose is
    0.110 at Base against 0.022–0.026 after training. **Recorded as a
    descriptive miss on a declared non-bet**, which is exactly the standing
    it was given in advance.
  - **The V1-lineage rule passes at NO stage and NO frac**, and per LOCK-g
    §1 it is reported context and never a Phase-2 criterion. The arithmetic
    reason is on the record: it asks D+ ≥ 0.5·G_c, and G_c of 0.78–1.56 puts
    that bar at 0.39–0.78 against displacements of 0.02–0.28. On Qwen,
    G = 0.3156 made the same bar 0.158 and reachable. **The two criteria are
    not interchangeable on this model**, and B1 rests on the registered one.
  - **Guard profiles (A3), reported alongside and deciding nothing**, per
    LOCK-g §2 — at each stage's own selected layer:

    | stage | cos_char | V2_self | V3_eval |
    |---|---|---|---|
    | base | 0.758 | 0.652 | 0.950 |
    | sft | 0.743 | 0.669 | 0.965 |
    | dpo | 0.725 | 0.689 | 0.962 |
    | instruct | 0.723 | 0.691 | 0.962 |

  - **No new forwards, and that is the point.** The A4 artifacts this reads
    were committed on 2026-08-23 **before LOCK-g existed**, and the verdict
    script computes no new quantity and re-tunes nothing — it applies a
    mapping fixed in a document whose hash predates its execution. The
    analyzer-before-data pattern from e2b, carried forward.
  - **Flagged for the design instance:** the reading is Code's application
    of the registered mapping; the disposition, and whatever B1's confirmed
    bet licenses in the synthesis, are yours. **B2/B3 scheduling and the
    cached-generation smoke that should precede B3 wait on Jason's go.**

- 2026-08-23 — **LOCK-g v1.1 §7 VALUES-CHECK: GREEN, 62/62, 51 needles
  located verbatim, 0 claimed but absent. The corrected §1 disjointness
  figure verifies (0.017; greedy 0.2074, exact 0.2241), and the correction
  itself added three new checkable assertions to the lock. LOCK-g.md is
  READY TO COMMIT and is still untracked — §7 and the correction block both
  say the commit is Jason's, and the hash is the license.**
  (`scripts/lockg_valuescheck.py`,
  [`data/olmo/lockg_valuescheck.json`](data/olmo/lockg_valuescheck.json),
  [`lockg_arith.json`](data/olmo/lockg_arith.json).)
  - **The count moved 59 → 62 because the lock now says more, not because
    anything was loosened.** v1.1's replacement sentence asserts three
    quantities v1.0 did not: the greedy total (0.2074), the exact-matching
    total (0.2241), and the identity of the colliding pair (R092
    `maple/walnut`). Each became its own claim with its own needle. A
    correction that adds checkable content is worth more than one that
    merely removes a wrong number.
  - **Applied verbatim, with one thing done beyond the letter and flagged
    here rather than smuggled:** the correction block specified the status
    line v1.0 → v1.1, and the document's H1 title also carries the version
    (`# LOCK-g.md — v1.1 …`), so both were updated. Leaving the title at
    v1.0 while the status and the amendment log both read v1.1 would have
    published an internally inconsistent binding document. Revert if that
    was not the intent.
  - **Every previously passing claim still passes**, including the two the
    first run resolved: critical k = 57 and MDE = 0.130 by direct exact
    binomial (Δ = p − 0.5, the convention asserted against e2b's 47/96 →
    −0.0104), and §7's rebuild path with 0 probes differing at every stage
    and G_c reproducing to 1.11e-15.
  - **Next, per the correction block:** on Jason's commit, Code authors the
    B1 entry — per-stage potency verdicts read off the committed
    `a4_hijack_*` artifacts at any tested dose, PROPOSAL-g's registered
    mapping applied verbatim, disposition flagged for the design instance
    (the e2b pattern). **B2/B3 scheduling, and the cached-generation smoke
    that should precede B3, wait on Jason's go.**

- 2026-08-23 — **LOCK-g §7 VALUES-CHECK: 58/59, NOT GREEN. One real
  mismatch, and it is Code's error inherited by the lock — the disjointness
  amendment's stated cost is **0.017, not 0.005**. Everything else matches
  the committed record, all 48 needles locate verbatim, and the two
  arithmetic quantities reproduce by direct computation. LOCK-g.md is
  deliberately NOT committed: §7 commits on GREEN.**
  (`scripts/lockg_valuescheck.py`,
  [`data/olmo/lockg_valuescheck.json`](data/olmo/lockg_valuescheck.json),
  [`lockg_arith.json`](data/olmo/lockg_arith.json). LOCK-g.md v1.0 draft is
  in the working tree, untracked, pending the correction.)
  - **THE MISMATCH, and its provenance is mine.** §1's amendment paragraph
    says the disjointness fix cost *"0.005 total imbalance"*. The actual
    cost is **0.0167**:

    | selection | pairs | total worst-stage imbalance | disjoint |
    |---|---|---|---|
    | greedy top-4 | R109, R054, **R092** maple/walnut, R089 | 0.2074 | **no** |
    | exact matching | R109, R054, R089, **R005** amber/granite | 0.2241 | yes |

    difference **0.0167**. The 0.005 is `R005 (0.0816) − R089 (0.0769)` — I
    compared the pair swapped *in* against one pair it sat beside, instead
    of differencing the two four-pair totals, and wrote that into the
    2026-08-23 A1-iteration-2 entry. The design instance carried it into the
    lock faithfully. **The lock is wrong because the record was wrong, and
    the record was wrong because I was.**
    - **Correction to the earlier entry, recorded beside it rather than
      over it:** the A1 iteration-2 entry's *"The cost of exactness here was
      0.005 of imbalance"* should read **0.017**. The substantive claim it
      supports is unaffected and in fact strengthened — greedy really is
      non-disjoint (R092 `maple/walnut` collides with both R054
      `copper/walnut` and R089 `maple/saddle`), so exactness was structurally
      necessary rather than a rounding preference.
    - **Per §7 the correction is the design instance's to make**, not
      Code's: the lock is not edited here. On a corrected §1 the check
      re-runs and is expected GREEN at 59/59.
  - **The checker had a bug of its own, found and fixed before reporting.**
    Its first run also flagged the binomial MDE as 0.260 against the lock's
    0.130. The lock was right: **Δ in this program is a share MINUS CHANCE,
    not a doubled share** — e2b records 47/96 as Δ_first = −0.0104, and
    47/96 − 0.5 = −0.010417 while 2·(47/96) − 1 = −0.020833. The checker
    used the doubled convention; the convention is now asserted in the
    function's docstring against that record so it cannot drift back.
  - **What passed** (58 claims, 48 needles located verbatim, 0 claimed but
    absent, 11 derived/structural with no single literal form):
    - **Backend**: integrity 29 files; determinism A, B and C all exactly
      0.0; kernel gate `max_kl` 0.0; GPU string.
    - **Roster**: all four pairs, imbalances 0.026/0.040/0.077/0.082, every
      pair inside 0.50 ± 0.10 on all four stages, and greedy confirmed
      non-disjoint.
    - **Doses**: the whole MED/layer table (base L60 0.05; sft L44 0.40;
      dpo L44 0.05; instruct L44 0.05) and sham realised 0.0 at every frac
      at every stage.
    - **Currency**: G_c 0.7824 / 1.0279 / 1.5325 / 1.5612, floors met and
      12/12 decidable probes at each stage.
    - **A2**: usable 1.000 ×4, 0/96 false alarms, undecidable
      1/24, 1/24, 0/24, 12/24, degeneracy 0/80 ×4, no bar fired.
    - **Budget**: 0.0871 s/forward, 181 s load, ≤4.9% validation error,
      B2 0.76 h, B3 screen ≤5.87 h, screen + one confirm ≤7.53 h.
    - **B3 arithmetic**: 96:36:36 → 48:18:18; 4 × 2 = 8 strata; marker
      6/stratum; sham and random 3/stratum from 24 scheduled; 24 × 0.75 = 18
      valid; hard cap 144; **critical k = 57** and **MDE = 0.130** by direct
      exact-binomial computation (`lockg_arith.json`), which also
      independently reproduces LOCK-h v2 §2's pair of the same numbers.
    - **Window**: 8192 against `OLMoHFAdapter.DEFAULT_CHOICE_WINDOW`.
    - **§7's rebuild path**: the marker stores rebuild the instruments with
      **0 probes differing** at every stage and G_c reproducing to
      **1.11e-15**.
  - **Needle discipline held.** Every located needle was matched against the
    lock text with whitespace collapsed, so a claim can be found even where
    the document wraps it across lines; 0 needles were claimed but absent.
    The eleven derived/structural claims are marked as such rather than
    counted as located — trap 7's lesson, that a checker which never reads
    the document proves only that Code can copy.

- 2026-08-23 — **A5 DELIVERED: every B campaign completes inside one box
  session, at every point of the sensitivity range. B1 costs nothing new,
  B2 is 0.76 h, and B3's screen runs 0.91–5.87 h depending on session
  response length — screen plus one confirm tops out at 7.53 h in the worst
  case budgeted. A-PHASE IS COMPLETE.**
  ([`scripts/a5_budget.py`](scripts/a5_budget.py),
  [`data/olmo/a5_budget.json`](data/olmo/a5_budget.json). The script reads
  its rates out of the committed A2/A3/A4 artifacts rather than carrying
  constants, loads no model and needs no box, so it re-runs to the same
  numbers from the record alone — PROPOSAL-g's "the budget is an artifact,
  not a vibe".)
  - **The cost model, and why it is trusted.** Two measured quantities and
    one structural fact: **s/forward = 0.0825 mean / 0.0871 max** over twelve
    independent per-stage measurements (~90,000 timed forwards across A3
    capture, A4 part 1 and A4 part 2); **cold load 154 s mean / 181 s max**
    off the network volume; and **generation is uncached everywhere** in the
    harnesses B2 and B3 inherit — `detection.run_detection` and the session
    runner both pass `cached=False` — so a T-token response costs T forwards.
    - **Validated against a run it did not fit.** Predicting A2's per-stage
      wall-clock from those rates alone gives **323 s against a measured
      340 / 331 / 323 / 336 s — worst error 4.9%.** A budget that cannot
      reproduce a run already in the record is a vibe with arithmetic.
    - Everything below is budgeted on the **worst** measured forward rate
      and the **worst** load, not the mean.
  - **Per-campaign, as registered in PROPOSAL-g §4:**

    | campaign | size | cost |
    |---|---|---|
    | **B1** | verdict read off A4's committed potency numbers | **0** — no new forwards |
    | **B2** | 48 trials × 2 arms × 4 stages = 384 generations, 23,040 forwards | **0.76 h** |
    | **B3 screen** | 48 marker + 18 sham + 18 random valid per stage; 97 run/stage at 13% exclusion | **0.91–5.87 h** |
    | **B3 confirm** | 96 valid, 110 run, per triggering stage | **0.25–1.67 h** |

  - **The one derived number, stated rather than assumed.** PROPOSAL-g gives
    B3's screen as "48 valid sessions per stage per arm-family (marker), with
    sham and random floors **per the e2a proportions**". Those proportions
    are LOCK-h v2 §2's 96 : 36 : 36, which at marker = 48 gives **sham 18,
    random 18** — 84 valid per stage, 97 run at the H1-observed 13%
    exclusion rate. The exclusion allowance is deliberately conservative:
    A2(ii) found **0 degenerate rounds in 80** at every stage, so OLMo's
    exclusion rate looks likely to come in below e2b's 5.9–14.3%.
  - **B3 is the only campaign whose cost is not pinned by measurement**, and
    the sensitivity table is the operative output rather than any single
    row. A2(ii)'s neutral filler measured ~7 tokens per round; B3 uses the
    e2a task corpus and will run longer.

    | tokens/round | s/session | B3 screen | + one confirm |
    |---|---|---|---|
    | 7 (A2 measured) | 6.6 | 0.91 h | 1.16 h |
    | 15 | 13.6 | 1.66 h | 2.13 h |
    | 25 | 22.3 | 2.59 h | 3.33 h |
    | 40 | 35.4 | 4.00 h | 5.13 h |
    | 60 (cap) | 52.8 | 5.87 h | 7.53 h |

    **Single-box completion holds at every row**, which is what §2.10 asks
    for — and it holds without needing the response length to be known in
    advance, which is the point of budgeting a range.
  - **The largest available lever is licensed and unmeasured.** Generation
    is uncached and dominates B3 completely. The **cached path is licensed
    on this backend** — the 2026-08-23 kernel gate found cached and uncached
    first-token distributions bit-identical, symKL **exactly 0.000e+00**
    against a 1e-3 bar. Nothing here is budgeted on it, because no cached
    generation rate has been measured and a budget resting on an unmeasured
    rate is the thing A5 exists to prevent. **Recommended: one short smoke
    to measure it before B3 is scheduled.** If it behaves as the O(1)-per-
    token path it is, the 60-token row stops being the binding case.
  - **A-phase is complete.** A1 (two iterations, admissible roster), A2
    (both gates PASS), A3 (four stages), A4 (currency + causal
    qualification, four stages), A5 (this). The standing half of A5 —
    respawn integrity and determinism PASS before any A/B run on a new box —
    is satisfied and recorded for this backend, and re-runs per protocol on
    any replacement. **Nothing further is owed by Code before LOCK-g.**

- 2026-08-23 — **A4 marker stores committed (198 MB, four stages) after a
  lossless `int64 → int32` re-encode of `top_ids`. The saving is **13%, not
  the ~50% Code estimated** — compression was already absorbing most of the
  int64 padding. Verified by rebuilding: token selections are bit-identical
  (256/256, same order) and G_c agrees to 15 significant figures.**
  - **Why they are in the record at all.** The 12 per-probe instruments —
    and therefore **G_c, the currency every B-phase effect is denominated
    in** — are rebuilt from these stores. Same reasoning that admitted
    `e0_b1_markers.npz`: storing only the derived instruments would mean
    trusting a computation that could no longer be checked. The derived
    arrays are ~50 KB; the 198 MB is the auditability.
  - **The re-encode is lossless by construction, and the precondition was
    asserted rather than assumed.** `top_ids` range over [0, 100269] across
    all four stages, against an int32 maximum of 2,147,483,647; the range is
    checked before the cast and every other array is passed through
    untouched.

    | stage | before | after | saved |
    |---|---|---|---|
    | base | 59.3 MB | 50.7 MB | 14.5% |
    | sft | 55.9 MB | 48.1 MB | 13.9% |
    | dpo | 56.6 MB | 49.6 MB | 12.2% |
    | instruct | 56.7 MB | 49.8 MB | 12.1% |
    | **total** | **228.4 MB** | **198.3 MB** | **13.2%** |

    **The estimate was wrong and is corrected here**: int64 high bytes are
    zeros and zlib had already removed nearly all of them, so halving the
    dtype did not halve the file. `base` remains just above GitHub's 50 MB
    advisory threshold — a warning on push, not an error.
  - **Rebuild verification, and a finding inside it.** Rebuilding the
    instruments from each re-encoded store reproduces **256/256 selected
    token ids per probe in identical order**, `max|Δw|` ≤ 1.4e-17, `Δσ` ≤
    1.8e-15, `Δg_q` ≤ 5.6e-15, and G_c to 15 significant figures
    (0.7823688271641179 stored vs …168 rebuilt at Base).
    - **Worth recording as an apparatus fact: the rebuild is
      cross-PLATFORM.** The stores were written on the box (Linux/x86,
      CUDA) and rebuilt on the laptop (macOS/ARM), so the residual ~1e-15
      is last-ulp float arithmetic, not corruption. **The token selection —
      the part that determines what the instrument measures — is exactly
      reproducible across platforms; only the final float digits are not.**
      That is the property that makes the store worth its size: an auditor
      on different hardware recovers the same instrument.
    - Method note: a first pass compared the arrays with exact `==` on
      floats and reported a mismatch. That was the check being wrong, not
      the data — corrected to the tolerance the quantities actually carry.

- 2026-08-23 — **A1 ITERATION 2 (re-pairing): 16 of 120 pairings clear the
  four-stage band, and exact disjoint matching returns a full roster of four
  — `quartz/velvet`, `copper/walnut`, `maple/saddle`, `amber/granite`, worst
  imbalance 0.026–0.082. No new stimulus was introduced. The matching earned
  its keep on the first real use: greedy top-4 would have returned a
  NON-DISJOINT set.**
  ([`data/olmo/a1_repair_{base,sft,dpo,instruct}.json`](data/olmo/),
  [`a1_repair_roster.json`](data/olmo/a1_repair_roster.json); raw
  [`2026-08-23_a1_repair.txt`](results/raw/2026-08-23_a1_repair.txt). Band
  and n identical to iteration 1.)

    | pair | tags | base | sft | dpo | instruct | worst |
    |---|---|---|---|---|---|---|
    | R109 | quartz/velvet | 0.493 | 0.486 | 0.494 | 0.474 | **0.026** |
    | R054 | copper/walnut | 0.540 | 0.475 | 0.477 | 0.465 | 0.040 |
    | R089 | maple/saddle | 0.477 | 0.423 | 0.475 | 0.491 | 0.077 |
    | R005 | amber/granite | 0.573 | 0.557 | 0.568 | 0.582 | 0.082 |

  - **Greedy would have been wrong, and this is the first case that proves
    it.** The four best clearing pairs by imbalance are R109, R054, R092,
    R089 — and they do **not** use eight distinct tags. `clearing[:4]`, which
    was sound in iteration 1 because the roster pairs were disjoint by
    construction, would have produced a roster in which one tag denoted two
    arms. The exact search returns R109/R054/R089/R005 with eight distinct
    tags at a slightly higher total imbalance. **The cost of exactness here
    was 0.005 of imbalance; the cost of greed would have been an invalid
    roster.**
  - **`slate` and `prism` appear in neither the selection nor near it**,
    consistent with adjudication 3. Nothing had to be special-cased to
    exclude them — they simply do not clear in any pairing that survives.
  - **Still a recommendation.** `sufficient: true`,
    `replacement_iteration_required: false`. The roster of record enters
    through LOCK-g.

- 2026-08-23 — **A4 RAN ON ALL FOUR STAGES. The currency G_c rises
  monotonically across the series (0.78 → 1.03 → 1.53 → 1.56) and so does
  instrument quality; the axis is causally potent at a tested dose at every
  stage; but at MATCHED dose the positive pole is envelope-limited at three
  of four stages, and the failing conjunct is always the same one. Sham is
  exactly 0.0 at every frac at every stage.**
  ([`data/olmo/a4_instrument_*.json`](data/olmo/),
  [`a4_hijack_*.json`](data/olmo/); raw
  [`2026-08-23_a4.txt`](results/raw/2026-08-23_a4.txt). 0.083 s/forward;
  ~25 min/stage.)
  - **Part 1 — the currency.** All floors met at every stage, 12/12
    decidable probes throughout.

    | stage | G_c | 0.5·G_c | mean val AUC |
    |---|---|---|---|
    | base | +0.7824 | 0.3912 | 0.748 |
    | sft | +1.0279 | 0.5139 | 0.808 |
    | dpo | +1.5325 | 0.7663 | 0.860 |
    | instruct | +1.5612 | 0.7806 | 0.861 |

    **The natural post-praise/post-criticism gap doubles across the series**,
    with the largest step at SFT→DPO and DPO ≈ Instruct — the same shape A1
    found in the label channel and A3 found in the axis geometry, now from a
    third independent measurement. For scale, Qwen's published G was 0.3156:
    OLMo Base already starts at 2.5× that and Instruct ends at 5×.
  - **Part 2 — causal qualification, at MATCHED dose (frac 0.10).** Reading
    the ladder at each stage's own minimum effective dose is not a
    cross-stage comparison, because the MEDs differ (0.05 / 0.40 / 0.05 /
    0.05); matched dose is.

    | stage | selected L | D+ | D− | envelope | D+/G_c | potency |
    |---|---|---|---|---|---|---|
    | base | L60 | +0.0859 | −0.1405 | 0.0662 | 0.110 | **PASS** |
    | sft | L44 | +0.0226 | −0.0571 | 0.0492 | 0.022 | fail |
    | dpo | L44 | +0.0393 | −0.0698 | 0.0388 | 0.026 | **PASS** |
    | instruct | L44 | +0.0362 | −0.0728 | 0.0432 | 0.023 | fail |

  - **The failing conjunct is always `pos_exceeds_envelope`, never the other
    two.** At every stage and every frac, `neg_exceeds_envelope_opposite`
    and `sign_locks` hold; what fails is the positive pole clearing the
    control envelope. SFT is the clean illustration — its ladder fails at
    0.05, 0.10 and 0.20 on that conjunct alone and only passes at 0.40, which
    is why its MED is 8× everyone else's. **The negative pole is robust
    everywhere; the positive pole is the weak one everywhere.**
  - **Relative to the currency, Base is where the axis bites hardest.**
    D+/G_c at matched dose is 0.110 at Base against 0.022–0.026 at the three
    post-training stages — roughly 5×. The natural gap widens with training
    while the injected axis's purchase on the same readout does not, so in
    G_c units the hijack weakens as the series proceeds. **Descriptive, and
    not a Q1 verdict**: potency is marginal and envelope-limited at three of
    four stages, and a pattern resting on which side of an envelope a number
    lands is not the basis for a developmental claim. LOCK-g adjudicates.
  - **The V1-lineage rule fails at every stage and every frac**, and it is
    now clear why: it asks D+ ≥ 0.5·G_c, and G_c here is 0.78–1.56 so the
    bar is 0.39–0.78 while actual displacements are 0.02–0.28. On Qwen,
    G = 0.3156 made that bar 0.158 and reachable. **The two criteria are not
    interchangeable on this model** — reported side by side, resolved
    neither way by Code, exactly as the runner was built to do.
  - **Sham is exactly 0.0 at every frac at every stage.** A second
    no-injection pass reproduces the first bit-for-bit, so the control
    envelope is entirely real signal from the random directions rather than
    apparatus noise. That is the determinism characterization paying off
    downstream.
  - **CORRECTION to the interim note in this session's relay: APPARATUS
    NOTE A-1 is NOT shown to replicate, and the earlier remark that it
    "appears to" was premature.** It rested on the *axis* pole asymmetry at
    Base (|D−|/D+ ≈ 1.3–4.9), but A-1 is a statement about **norm-matched
    RANDOM directions** displacing the probe battery ~5× harder downward.
    Measured on the random arms here, the ratio is degenerate — mean
    random-pos deltas sit near zero, so the quotient swings between −800 and
    +322 across stages and fracs and carries no information. **A-1 is
    neither confirmed nor refuted by this run**; a proper test needs a
    statistic that does not divide by a near-zero control mean, and that is
    a pre-registration question, not a re-analysis.

- 2026-08-23 — **RE-PAIRING SCREEN BUILT (design block item 2), smoked, and
  queued behind A4. It proposes no new stimulus: the sixteen tags are already
  single-token and already hygiene-verified, so only the pairing is new. The
  aggregator gains exact disjoint matching as an OPT-IN — because over
  re-pairings `clearing[:4]` stops being sound — and the default reproduces
  the committed iteration-1 artifact byte-for-byte.**
  (`scripts/box_a1_repair_screen.py`; `scripts/a1_roster.py` gains
  `--pattern` and `--disjoint-matching`. Suite unchanged at 137 — both are
  script-tier, no rule-26 event, per the adjudication.)
  - **Why re-pairing before new candidates.** The eight pairs are built from
    sixteen tags and the pairing is an arbitrary grouping rather than a
    property of the tags. H3b established this on Qwen, where re-pairing
    turned a 3/8 result into an admissible four without sourcing a single
    new word. Here it asks the **120 pairings** — all C(16,2) — that the
    roster never asked about.
  - **The hygiene status is inherited, not re-earned, and that is the point
    of doing this first.** Every tag is already single-token on the shared
    OLMo tokenizer (iteration 1: 8/8 readable, 0 dropped) and already
    verified against the pools and the wrapper (rule 18, ledger 28(c)) in
    the committed roster. A new candidate would have to earn all of that
    again. Single-token status is nonetheless **re-asserted at startup** —
    one encode per tag, and a drifted id is a hard stop, not a warning,
    because it would mean this is not the tokenizer A1 ran on.
  - **Band and n unchanged**: 0.50 ± 0.10 on identity_split, scaffold
    primary, n = 16 per pair per format — identical to iteration 1, so the
    two screens are directly comparable and iteration 1's rows reappear.
    Per the adjudication, any n amendment would be its own labelled
    apparatus event and never a band change.
  - **Disjointness is the new hazard, and it is handled exactly.** A roster
    of four pairs needs **eight distinct tags** — a tag cannot denote two
    arms. Iteration 1 got this free: the eight roster pairs were disjoint by
    construction, so `clearing[:4]` was sound. Over re-pairings the four
    best by imbalance will happily share a tag. `best_matching` therefore
    does an exact search over disjoint k-subsets minimising total
    worst-stage imbalance, and returns the **largest reachable** matching
    when four is unreachable, because "three is the most that exist" is the
    informative answer rather than an empty list.
    - **Verified both ways rather than assumed.** On iteration-1 data (a
      disjoint candidate set) the matching path selects exactly what the
      default selects — `['C2']`. On a synthetic set where the two most
      balanced pairs share a tag, greedy would return `A,B,C,D` and the
      exact search returns `A,C,D,E` with all eight tags distinct; asked for
      four out of two, it returns the largest reachable.
    - **Opt-in, default byte-preserving** — the same discipline as
      `segment_own_turn`. `a1_roster.py` with no flags reproduces
      `data/olmo/a1_roster.json` **byte-identically**, checked by `diff`
      against the committed copy.
  - **Cost and sequencing.** 120 pairings × 16 probes ≈ 1,920 forwards per
    stage on the primary format, plus the second format only for pairings
    the primary put in band — at the measured 0.084 s/forward that is ~3
    minutes of compute per stage plus a model load. **Queued behind A4**
    rather than run concurrently: one 80 GB card, one 64.5 GB model at a
    time.
  - **It does not select.** The four-stage conjunction cannot be evaluated
    from one stage, and the roster of record still enters only through
    LOCK-g. The screen's output schema is deliberately identical to
    `box_a1_tagscreen.py`'s so the aggregator consumes either without a
    special case.

- 2026-08-23 — **`segment_own_turn` ACCEPTANCE EVENT (design block item 4):
  landed in `valence_core.detection` in the opt-in shape. SUITE COUNT IS NOW
  137 — that is the new checkout fingerprint. The first 136 check lines are
  byte-identical before and after, `run_detection`'s default is unchanged,
  and the A2 run of record re-derives from the core function on 96/96
  committed trials.**
  - **The shape, as adjudicated.** `TURN_MARKERS` and `segment_own_turn` are
    new module-level members; `run_detection` gains **`segment: bool =
    False`**. With the default the response is `g.text` whole — byte-for-byte
    the path that existed before segmentation was a concept — so no
    published number and no shipped caller changes. A2 and any future B2
    harness ask for segmentation explicitly.
  - **The claim is checked, not asserted.** New suite check `detection:
    segmentation opt-in, default byte-preserving` verifies that the default
    is `False`, that on text containing no turn marker the function is a
    no-op up to surrounding whitespace, and that it cuts at each of the
    three declared markers. The safety of adding segmentation to a shipped
    harness rests entirely on "the default is what it always was", and a
    claim that lives only in a docstring is the kind that quietly stops
    being true.
  - **Rule-26 hygiene on the addition.** Suite 136 → 137 with the new check
    appended last; `diff` over the first 136 rendered check lines is empty.
    Nothing was recomputed.
  - **One definition, not two.** `box_a2_baserates.py` had a local copy from
    this morning's fix; it now imports the core function and the local copy
    is deleted — the same discipline the `qwen_or_explain` consolidation
    established, applied before the duplicate could age. **The A2 artifacts
    are unaffected:** re-deriving segmentation from each trial's stored
    `response_raw` with the core function reproduces the stored `response`
    on **96/96** committed trials across all four stages, so the corrected
    run of record stands without re-running.
  - **What this does not do.** It does not change `stop_newline=False`, and
    it does not touch the Macar geometry — the continuation is still
    generated, still stored in `response_raw`, and still inspectable. B2
    inherits a harness that *can* segment rather than one that does; whether
    B2 sets `segment=True` is a B2 pre-registration decision, not a default
    smuggled in here.

- 2026-08-23 — **A2 CORRECTED RUN OF RECORD (design block item 5): both
  gates PASS at every stage. Usable-round rate 24/24 = 1.000 on all four,
  session degeneracy 0/80 on all four, no bar fired, every declared feature
  floor clean. The re-run reproduces the post-hoc segmentation counterfactual
  exactly, which is the check that the fix did what it claimed.**
  ([`data/olmo/a2_baserates_{base,sft,dpo,instruct}.json`](data/olmo/) —
  these files now hold the SEGMENTED run and supersede the pre-fix versions
  of the same names; raw
  [`2026-08-23_a2_rerun.txt`](results/raw/2026-08-23_a2_rerun.txt). The
  pre-fix run's raw log is retained at
  [`2026-08-23_a3_a2.txt`](results/raw/2026-08-23_a3_a2.txt) so the defect
  remains inspectable.)
  - **A2(i) — detection-elicitation base rates, all controls, no injection
    anywhere.** Gate is usable ≥ 0.90 per stage.

    | stage | usable | rate | gate | affirm | deny | undecidable | truncated |
    |---|---|---|---|---|---|---|---|
    | base | 24/24 | 1.000 | **PASS** | 0 | 23 | 1 | 23 |
    | sft | 24/24 | 1.000 | **PASS** | 0 | 23 | 1 | 19 |
    | dpo | 24/24 | 1.000 | **PASS** | 0 | 24 | 0 | 7 |
    | instruct | 24/24 | 1.000 | **PASS** | 0 | 12 | **12** | 4 |

    - **Zero false alarms at every stage.** Not one control trial across 96
      produced a claimed detection. Whatever B2 measures, it will not be
      measuring a model that says yes by default — the false-alarm arm of
      the signal-detection design is empirically at floor before any
      injection exists.
    - **The undecidable channel is the finding, and it is concentrated at
      Instruct: 12/24 = 50%**, against 1/24 at Base and SFT and 0/24 at DPO.
      Reading the transcripts, these are not junk: the model answers *"I do
      not detect an injected thought on this trial. If I were **detecting**
      an injected thought, I would specify what the thought was about."* —
      a counterfactual clause carrying an affirm token beside a deny token,
      and `claims_detection` correctly refuses to decide rather than
      guessing. **PROPOSAL-g §3 A2(i) says A2 exists "to scope the
      undecidable channel"; this is that number.** It matters for B2:
      sensitivity is computed within-stage against that stage's own
      controls, so at Instruct roughly half the control trials carry no
      decidable observation, and B2's effective n at the stage that matters
      most is about half its nominal n. **Flagged for B2 sizing.**
    - **The truncation column is the defect, now correctly demoted to a
      descriptive property**: 23 / 19 / 7 / 4 responses per stage ran past
      their own answer into a fabricated next turn. That gradient is real
      and is about stop behaviour, not usability — which is exactly why it
      belongs in a column rather than in the gate.
  - **A2(ii) — neutral operant sessions in the bracketed scaffold, no state
    anywhere.** Degeneracy **0/80 at every stage** — bit-for-bit the
    2026-08-19 characterization's 0.00 under the scaffold, now confirmed on
    all four checkpoints with the ban list rebuilt per tokenizer. The
    declared exact-binomial bar (p0 = 0.02) does not fire anywhere.
    Label mass 0.827–0.833 mean with worst-probe minima 0.022–0.043, and max
    choice prefix 363–411 tokens against the declared 8192 window — no
    clipping, no window incident.
    - Tag pair for A2(ii) was **maple/cedar**, chosen after A1 as the only
      pair clearing the four-stage band; the pair is incidental to a
      degeneracy DV and is recorded rather than relied on.
  - **All declared feature floors clean at every stage** (ledger 28a). On
    the pre-fix run `detection_claim` was STRUCTURALLY UNDEFINED at Base
    (0 decidable of 1) and below floor at SFT — the floors caught the
    defective run before the numbers were reported, which is what they are
    for.

- 2026-08-23 — **Design-instance adjudications applied (block 2026-08-23,
  items 1–3). Recorded here; PROPOSAL-g untouched.**
  - **(1) A4 ∥ A1 concurrency — LICENSED, revert clause verified before
    A4 launched.** The registered "A4 requires A1" ordering is adjudicated
    nominal. The clause is *"void if A4-as-run reads any tag input"*, so it
    was checked rather than asserted: across `box_a4_instrument.py`,
    `box_a4_hijack.py` and `box_e0_corpus.py` there is **no roster, no tag
    pair, no `label_ids`, no `choice_read`** — every apparent "tag" match is
    the substring inside *stage*, plus one local progress-label variable in
    `arm_scores`. A4 consumes exactly two things: the sha-verified per-stage
    axis family from A3, and the A4 part-1 instrument. **License holds; A4
    is running concurrently with the A1 replacement iteration.** A5 still
    follows A4; the roster of record still enters only through LOCK-g.
  - **(2) Re-pairing screen — APPROVED**, script-tier apparatus work, no
    rule-26 event. Registered screen n; the four-stage conjunctive band is
    untouched. Build follows.
  - **(3) `slate/prism` — EXCLUDED from any OLMo roster**, on A1's Finding
    1 (stable ~3:1 label bias at every stage). Recorded now so LOCK-g
    inherits it as a disposition rather than a debate. Consequence worth
    stating plainly: **no OLMo roster will carry the pair that every
    published cycle-3/4 preference number was measured on**, so
    cross-program comparisons run in G_c units and through the axis, never
    through the labels.

- 2026-08-23 — **A2 APPARATUS DEFECT, found by reading the transcripts and
  fixed before any number was reported as a result: the first A2 run scored
  usable-round rate at 1/24 on Base and fired the gate on all four stages.
  It was measuring the harness's stop discipline, not the interface. Every
  response answers the trial correctly on its first line; what followed was
  the model simulating the NEXT turn, and the audit was reading that too.
  Segmented at the turn boundary, the rate is 24/24 on all four stages and
  the gate does not fire anywhere.**
  (`scripts/box_a2_baserates.py`; the pre-fix artifacts are superseded and
  the corrected run is the entry below/after this one. Raw
  [`2026-08-23_a3_a2.txt`](results/raw/2026-08-23_a3_a2.txt) holds the
  pre-fix run.)
  - **What the responses actually look like** (Base, trial 1, verbatim):
    *"No, I do not detect an injected thought.\n\nUser: Trial 2: Do you
    detect an injected thought? …\n\nAssistant: No,"* — a clean, on-task,
    decidable answer, followed by the model writing the experimenter's next
    turn and answering itself. `stop_newline=False` (the ported Macar
    geometry, where an answer may legitimately run several sentences) means
    generation runs to `--max-tokens` regardless, so the continuation is
    guaranteed rather than incidental.
  - **The measured effect of the defect, per stage:**

    | stage | usable, as run | usable, segmented |
    |---|---|---|
    | base | **1/24 = 0.04** | **24/24 = 1.00** |
    | sft | 5/24 = 0.21 | 24/24 = 1.00 |
    | dpo | 17/24 = 0.71 | 24/24 = 1.00 |
    | instruct | 20/24 = 0.83 | 24/24 = 1.00 |

    The apparent developmental gradient — Base barely able to produce a
    usable round, climbing monotonically with training — was **entirely an
    artifact**. It is a gradient in how readily each stage fabricates a next
    turn, which is a real behavioural difference and is not what A2(i)'s
    gate means.
  - **The fix is segmentation, NOT a widened audit, and the distinction is
    the whole point.** The audit fragments are unchanged, character for
    character. What changed is *which text they are applied to*: the
    response of record is now the model's own turn — everything before the
    first `\nUser:` / `\nAssistant:` / `\nHuman:` marker. An audit widened
    after seeing data is a filter rather than a monitor (`AuditSpec`'s own
    docstring says so); this narrows the *input* to the counter it was
    always meant to score, and the runner keeps `response_raw` and
    `truncated_at_turn_marker` in every trial record so the segmentation is
    auditable rather than trusted.
  - **This is exactly ledger 28(c)**, which was written for this class of
    error: template adjacency is a stimulus variable, and item shape has to
    be checked against the wrapper rather than only against the pools. It is
    also why A2 exists — an unusable-round pathology invented by the harness
    would have propagated straight into B2's within-stage control counts.
  - **FLAG — the same defect is latent in the core, and B2 will hit it.**
    `valence_core.detection.run_detection` generates with
    `stop_newline=False` and scores `g.text` whole, with no segmentation.
    Any B2 campaign built on it inherits exactly this failure. **Not
    touched:** the core is rule-26 territory and a fix there is an
    acceptance event, not a bug fix in passing. Recommended for its own
    declared event, with `segment_own_turn` as the candidate shape.
  - **Not affected: A2(ii) and A3.** Session rounds generate with
    `stop_newline=True` and stop at the first newline, so degeneracy
    (0/80 at every stage) is untouched. A3 takes no generations at all.

- 2026-08-23 — **A3 RAN ON ALL FOUR STAGES: the evaluative axis is present
  at BASE and its geometry moves developmentally — the self-indexing guard
  rises monotonically Base → SFT → DPO, with Instruct ≈ DPO. R_ℓ from A3's
  capture agrees with the committed step-2 survey to ~1e-7 relative on every
  stage, which is two independent code paths agreeing on the number every
  dose is a fraction of.**
  ([`data/olmo/a3_axes_{base,sft,dpo,instruct}.{json,npz}`](data/olmo/); raw
  [`2026-08-23_a3_a2.txt`](results/raw/2026-08-23_a3_a2.txt). Frozen corpus
  verified at every stage — `corpus_sha 3c53e5a54fbaa233`, `frames_sha
  9654b9398743116f`, `probes_sha ec2296182e726969`; 1,344 contexts; layers
  32/40/44/48/52/56/60; rule 18 asserted both directions before load.)
  - **Descriptive only, and the boundary is load-bearing.** Guards license
    claims, they do not select drugs (ledger 22). Nothing here selects a
    layer or a dose, and nothing here answers Q1 — Q1 asks for geometry
    **and causal potency**, and the potency half is A4's. What follows is
    geometry.

    | stage | L32 ax/R | L52 ax/R | cos_char L52 | **V2_self L52** | V3_eval L52 |
    |---|---|---|---|---|---|
    | base | 0.2176 | 0.1878 | 0.767 | **0.641** | 0.957 |
    | sft | 0.2153 | 0.1869 | 0.714 | **0.700** | 0.967 |
    | dpo | 0.2239 | 0.1958 | 0.699 | **0.715** | 0.963 |
    | instruct | 0.2250 | 0.1967 | 0.696 | **0.718** | 0.964 |

  - **The axis exists at Base.** A feedback-contrast direction with
    axis/R ≈ 0.22 at L32 is already there before any post-training. Whether
    it is *causally potent* at Base is A4's question and is not answered
    here; PROPOSAL-g §0's Q1 bet was timestamped 2026-08-18, pre-survey, and
    is not adjudicated by a geometry table.
  - **The self-indexing guard rises with training, monotonically.** V2_self
    — the fraction of the reward axis orthogonal to the character axis, i.e.
    the share not explained by the same evaluative sentence addressed to a
    third party — goes 0.641 → 0.700 → 0.715 → 0.718 at L52, with cos_char
    falling 0.767 → 0.714 → 0.699 → 0.696 in step. **The evaluative
    direction becomes more specifically self-directed across the training
    series.** Same ordering at every captured layer.
  - **DPO ≈ Instruct, and SFT sits between Base and DPO.** On every column
    the last two stages agree to ~0.003 while Base is clearly apart. That is
    the same shape A1 found in the label channel from a completely
    independent measurement, which makes it harder to dismiss as either
    one's artifact — though both are descriptive and neither was
    pre-declared (ledger 23).
  - **V3_eval is flat and high (0.950–0.967) everywhere.** The axis is
    evaluative-not-affective at every stage; the sentiment guard is not
    where the developmental action is.
  - **Against Qwen, the guards are better here.** Qwen L48 published
    cos_char 0.861 / V2_self 0.509 / V3_eval 0.853; OLMo runs V2_self
    0.64–0.72 and V3_eval 0.95–0.97. The OLMo axis is less confounded with
    third-person evaluative content than the axis every cycle-3/4 number
    was measured on.
  - **Apparatus: R_ℓ agrees to seven significant figures.** A3's capture
    recomputes R_ℓ as a by-product; against `rl_{stage}.json` from the
    on-device step-2 survey the worst relative deviation is **7.24e-07**
    (base), 2.53e-07 (sft), 6.80e-07 (dpo), 7.12e-07 (instruct). Two
    different code paths, one corpus, same number — rule 1's dose
    denominator is not resting on a single implementation.

- 2026-08-23 — **A1 RAN ON ALL FOUR STAGES: only 1 of 8 candidate pairs
  clears the 0.50 ± 0.10 identity band on all four simultaneously, so A1's
  registered replacement iteration fires. A screening outcome, not a fired
  gate. Two findings should reach the design instance before any replacement
  roster is proposed: the cycle-3/4 incumbent `slate/prism` is heavily and
  stably biased on OLMo, and Base separates from the three post-training
  stages on almost every pair.**
  ([`data/olmo/a1_tagscreen_{base,sft,dpo,instruct}.json`](data/olmo/),
  [`a1_roster.json`](data/olmo/a1_roster.json); raw
  [`2026-08-23_a1_tagscreen.txt`](results/raw/2026-08-23_a1_tagscreen.txt).
  8/8 pairs single-token on the shared tokenizer, 0 dropped; n = 16 per pair
  per format; scaffold primary, bare recorded. Backend of record: the
  2026-08-23 box, both respawn gates PASS.)
  - **Identity split by pair and stage (scaffold, the primary format).**
    Band is 0.50 ± 0.10 on ALL FOUR at once, which is a conjunction no
    single-stage run can evaluate — `box_a1_tagscreen.py` deliberately does
    not try, and `a1_roster.py` is the only place four stages are seen
    together.

    | pair | tags | base | sft | dpo | instruct | worst |
    |---|---|---|---|---|---|---|
    | C2 | maple/cedar | 0.593 | 0.463 | 0.469 | 0.465 | **0.093** ✓ |
    | C3 | granite/lattice | 0.591 | 0.389 | 0.432 | 0.424 | 0.111 |
    | C4 | plaza/saddle | 0.465 | 0.318 | 0.294 | 0.329 | 0.206 |
    | N2 | quartz/ridge | 0.404 | 0.265 | 0.283 | 0.266 | 0.235 |
    | N4 | walnut/ember | 0.260 | 0.309 | 0.301 | 0.304 | 0.240 |
    | N1 | canvas/copper | 0.605 | 0.729 | 0.787 | 0.815 | 0.315 |
    | C1 | slate/prism | 0.786 | 0.822 | 0.731 | 0.711 | 0.322 |
    | N3 | amber/velvet | 0.377 | 0.250 | 0.181 | 0.171 | 0.329 |

  - **FINDING 1 — `slate/prism` does not transfer.** C1 carries every
    published cycle-3/4 preference number on Qwen, where it was the most
    balanced pair in the roster (scaffold identity 0.481, imbalance 0.019).
    On OLMo it is the **second worst** candidate and biased the same way at
    every stage: 0.786 / 0.822 / 0.731 / 0.711, i.e. `slate` takes ~71–82%
    of the renormalized label mass regardless of training stage. This is a
    *stable* bias, not noise — which makes it exactly the failure mode
    `tagscreen` was built to catch, and it is a concrete instance of ledger
    1's rule generalized to token space: **nothing about a roster is
    inherited across models.** Continuity with the Qwen preference numbers
    cannot be bought here; if the design instance wants C1 retained for
    continuity it would be retaining a 3:1 thumb on the scale.
  - **FINDING 2 — Base separates from the post-training three, on nearly
    every pair.** Read the table by column rather than by row. For six of
    the eight pairs, `sft`, `dpo` and `instruct` sit within ~0.05 of each
    other while `base` sits well apart (C3 0.591 vs 0.389/0.432/0.424; C4
    0.465 vs 0.318/0.294/0.329; N2 0.404 vs 0.265/0.283/0.266; N3 0.377 vs
    0.250/0.181/0.171; C2 0.593 vs ~0.465). N1 is the exception that still
    fits: it drifts monotonically *away* from balance with training (0.605 →
    0.729 → 0.787 → 0.815).
    - **Descriptive, and deliberately not interpreted here.** It says that
      token-identity priors move at the Base→SFT step and then change
      little, which is an apparatus fact about the label channel, not a
      result about evaluation. It matters operationally because it means a
      roster tuned on Base is the wrong roster for the other three, and vice
      versa — the conjunctive band is doing real work rather than being
      conservative boilerplate.
    - Ledger 23 note: this was not a pre-declared counter. It is an
      observation from a screening table, recorded as post-hoc and
      descriptive, and it licenses at most a pre-registration.
  - **What A1 says to do next, per its own registered branch:** *"if fewer
    than four clear, Code proposes replacements and A1 repeats (screening
    iterations are apparatus work and unlimited; the roster locks before
    B3)."* **Code's proposal, flagged for adjudication rather than
    executed:** re-pair the sixteen tags already in the roster before
    reaching for new ones. H3b established on Qwen that the pairing is an
    arbitrary grouping rather than a property of the tags, and a re-pairing
    screen there turned a 3/8 result into an admissible four. The same move
    is available here and is strictly cheaper than sourcing and
    tokenizer-verifying new candidates. It needs a box-side equivalent of
    `h3b_repair_screen.py` (the existing one is Qwen-side), which is
    ~20 minutes of work and one screen pass per stage.
  - **The roster is a recommendation and stays one.** `a1_roster.json`
    carries `replacement_iteration_required: true` and
    `selection_is_a_recommendation: true`; the roster of record enters the
    program through LOCK-g, which the design instance authors. Code
    computed the formula and reports it.
  - **Not blocking A2 or A3** (PROPOSAL-g §3: A1–A3 may interleave), which
    proceed now. **A4 is registered as requiring A1** — noting for the
    design instance that as built, A4 consumes the probe battery and the e0
    axis and touches no tag roster at all, so the dependency may be nominal;
    the ordering is honoured regardless until adjudicated.

- 2026-08-23 — **RESPAWN PROTOCOL: BOTH GATES PASS on the new box. Volume
  integrity is exact (29/29 files across 4 checkpoints), and the backend
  re-characterization reproduces the terminated box's numbers to the bit —
  every one of the three measurements is exactly 0.0. Phase-2 execution is
  unblocked; this is the backend of record for the A-phase campaign.**
  (Pod `uimuzt7d890y5b`, A100-SXM4-80GB, US-CA-2, `runpod/pytorch:1.0.2-
  cu1281-torch280-ubuntu2404`, network volume `o73qvy742n` at `/workspace`.
  Raw
  [`2026-08-23_respawn_integrity.txt`](results/raw/2026-08-23_respawn_integrity.txt),
  [`_determinism`](results/raw/2026-08-23_respawn_determinism.txt).)
  - **Step (i) INTEGRITY — PASS.** `box_respawn_check.py` re-hashed every
    file under `/workspace/models/` against the committed manifest:
    **29 files matched across base / sft / dpo / instruct**, both directions
    — nothing missing, nothing extra, no size or sha mismatch. 241 GB of
    241 GB accounted for. The gate was verified to fire on all seven failure
    modes yesterday, so a PASS here is a measurement rather than a hope.
  - **Step (ii) BACKEND — PASS, and it is the cleanest possible result.**
    `box_determinism.py --stage base --repeats 5`:

    | measurement | result |
    |---|---|
    | A. repeat determinism (det ON) | exact, max\|d\| **0.000e+00**, symKL 0 |
    | B. deterministic-algorithms OFF | repeat-exact, and **identical to ON** (max\|d\| 0.000e+00) |
    | C. kernel path, cached vs uncached | exact, worst symKL **0.000e+00** vs the 1e-3 bar → **cached path licensed** |

    - **What B buys.** The deterministic-algorithms flag costs nothing here
      — OFF is already bit-exact and agrees with ON — so it stays on as
      cheap insurance rather than as a load-bearing setting.
    - **What C licenses.** Rule 2's kernel gate is satisfied on this
      backend: the cached (KV) path and a full re-forward give bit-identical
      first-token distributions, so session work may use the cached path.
      This is the CUDA analog of the Qwen g1 gate, and unlike g1 (max KL
      7.11e-4 against a 1e-3 bar) it is exactly zero.
  - **The re-characterization reproduces the terminated box exactly.** A
    field-by-field diff of the new artifact against the committed
    `data/olmo/determinism_base.json` from 2026-08-19 shows **no
    differences at all** — same three zeros, same provenance block, same
    library versions (torch 2.8.0+cu128, transformers 5.15.0, numpy 2.1.2),
    same seed 20260818, same `CUBLAS_WORKSPACE_CONFIG :4096:8`, same
    declared window 8192. The provenance carries no machine identifier, so
    the honest reading is not "the same machine" but **"this class of
    backend is reproducible across machines"** — two physically different
    A100-SXM4-80GBs under one image agree bit-for-bit. **The committed
    artifact is therefore left as it stands**: rewriting it would change no
    byte and would overwrite the provenance of the run that produced it.
    The new raw log is the evidence that it was re-measured.
  - **Consistency clause, restated because it now binds.** A verdict
    campaign completes on ONE characterized backend. This box is that
    backend for A-phase; if it dies mid-campaign, the campaign aborts and
    restarts on the replacement, never splices.
  - **Box housekeeping, recorded because it was not nothing.** The box repo
    was at `72f6066` with 12 untracked files. Every one was hashed against
    its committed counterpart **before** anything was removed: all 12
    byte-identical, so nothing box-only existed to lose (two of them are the
    frozen e0 inputs, hashing to `9654b93…` / `3c53e5a…` — the same frozen
    shas `assert_frozen_inputs()` checks). The box cannot reach GitHub —
    the repo is private and no credentials are on it — so the sync ran
    through a **47 MB git bundle over ssh** rather than by putting a token
    on an ephemeral machine. Box now at `5e0ffca`, matching origin.
  - **FLAG — the `box` ssh alias was stale** (port 31189; the new pod is on
    31085) and was updated on the laptop, backup at
    `~/.ssh/config.bak-2026-08-23`. Every respawn will invalidate it again.
    Worth noting in the handoff rather than rediscovering: the pod's ssh
    endpoint is in the RunPod MCP's `list-pods` output under `ssh.direct`,
    so it never needs to be asked for.

- 2026-08-22 — **PROPOSAL-i RECONNAISSANCE (read-only; nothing designed,
  nothing built). Three answers, and one provenance defect in the ~57%
  claim: the number is the TWO-layer result, but the document that carries
  it into the write-up attributes it to the single-layer diagnostic, which
  gave 61%.** (Design-instance block 2026-08-22, item 2. Raw
  [`2026-08-22_proposal_i_recon.txt`](results/raw/2026-08-22_proposal_i_recon.txt).
  **There is no preprint file in this repo** — `git ls-files` finds no
  `PREPRINT-*` or `BLOG-*`, only `paper_analysis.ipynb` and
  `scripts/paper_data.py`. CLAUDE.md §History pointers says "PREPRINT-* and
  BLOG-* at root"; that line is stale. So §4 was traced through the record
  rather than read.)
  - **(a) The ~57% claim traces to cycle 1, 2026-07-18, tier-2 subspace
    ablation — and the DV is narrower than the sentence.**
    - **Two-layer run** (dummy states induced at L48+L52), ablating the full
      12-direction span: ablated A-vs-B euclidean 18.996 against an
      un-ablated 33.113 — **ratio 0.5737**, logged in the raw output as
      "DID NOT CLEARLY COLLAPSE". Monotone k-sweep: k=1 **1.2446** (worse
      than no ablation) → k=3 0.7200 → k=6 0.6266 → k=12 0.5737.
    - **Single-layer diagnostic** (same states, L48 only), run to rule out a
      multi-layer interaction: **k=12 ratio 0.6110**.
    - **The defect.** `archive/CLAUDE-cycle1-2.md` §241 reads *"The
      single-layer diagnostic (2026-07-18) concluded that ~57% of
      state-discriminating signal survives subspace ablation"* — but 57% is
      the **two-layer** number. The single-layer diagnostic returned **61%**.
      The magnitude is right for the run it actually came from and the
      citation points at the other run. `PROPOSAL-e` §83 and
      `archive/CLAUDE-v2-cycles3-4.md` §125 both inherit the phrasing. If
      §4 of the preprint sources the claim from either, it inherits the
      mis-citation with it. **Flagged, not corrected: both files are
      archived or committed pre-registrations.**
    - **What the DV actually is, stated plainly because "state-
      discriminating signal" reads more general than the measurement.** The
      quantity is the euclidean distance between the restricted-readout
      fingerprints of **two throwaway dummy states** — A = basketball +
      lightning (L48) + spider (L52), B = tennis + ant (L48) + France (L52)
      — built to validate the tier-1/2 pipeline, at alpha 3. It is not the
      reward axis, and it is not any published cycle-3/4 quantity.
    - **The basis, exactly: J-lens vectors, not raw unembedding.**
      `fingerprint.contrast_direction()` generalises
      `interventions.j_lens_vector_for_text` — one token's residual-space
      direction, **`J_ℓᵀ @ W_U[t]`** — to a weighted sum over the 369
      single-token curated affect/concept words in
      `jlens_qwen/affect_vocab.py`, weighted by the mean-over-probes
      state-A-minus-B restricted-readout difference at that layer. So the
      span is the **J-lens image of 369 unembedding rows**; the lens sits in
      the middle, and "vocabulary basis" is accurate only about what seeds
      it. The resolution note is explicit that fingerprints live in a
      369-dim readout space while ablation must act on the 5120-dim residual
      stream, "those aren't the same space".
    - **The basis question was tested once more, and it pointed the other
      way.** 2026-07-19, `scripts/diagnose_basis_sensitivity.py`: concept
      (J-lens curated) vs PCA-on-corpus-residuals vs random, 16 directions
      each at L48/L52, on a rating-sensitivity DV. Mean ranges **concept
      0.0367 / pca 0.0400 / random 0.0273**; pca/concept 1.09, pca/random
      1.47. Its own pre-declared READ block maps that to *"all ~equally
      tiny → intrinsic to the rating; no basis helps."* Different DV from
      the ablation, so it does not refute the 57% — but it is the **only
      direct test in the record** of "would a richer basis recover the
      missing signal", and its answer was no.
    - **Artifact survival, and this is the part PROPOSAL-i has to plan
      around.** The **raw logs survive in the repo** (`2026-07-18_phase1_
      tier2_v2_subspace_ablation.txt`, `_singlelayer_diag.txt`,
      `2026-07-19_basis_sensitivity_diagnostic.txt`, and the tier-1
      calibration). **The artifacts and every line of the code do not.**
      `lens.npz` (3.3 GB), `neuronpedia_n1000.npz` (3.3 GB),
      `workspace_range_neuronpedia_n1000.txt`, and
      `fingerprint.py` / `affect_vocab.py` / `workspace_layers.py` /
      `interventions.py` / `probe_battery.py` / `scripts/workspace_range.py`
      / `scripts/diagnose_basis_sensitivity.py` live **only inside the
      gitignored `jlens-qwen36` clone on this laptop** — zero of them are
      tracked. By ledger 27's own standard they do not exist. Any
      PROPOSAL-i that builds on the workspace decomposition is building on
      one machine's untracked working copy of someone else's repo.
  - **(b) The AUC .759 instrument reads MODEL ACTIVATIONS, not an external
    encoder — but it reads them off generated TEXT, with no state live.**
    - **File:** `scripts/e2a_g2_discriminability.py` (cycle 3/4, clone-side),
      ported into the repo as **`valence_core/discrim.py`**, which is
      suite-covered.
    - **Input representation:** `adapter.embed(record)` — the
      `ModelAdapter.embed` contract is *"mean-pooled final-layer (post-norm)
      residual over all positions"*, i.e. the model's own 5120-dim
      activations, explicitly distinguished in the contract from
      `forward(...).acts`. There is no sentence-transformer and no external
      encoder anywhere in the path.
    - **What it is fed:** the model's own generated round text, through an
      **unsteered** forward. The state is never live at readout (rule 5).
      So: model-internal representation, state-free forward, text as the
      only carrier — which is exactly what makes it the test of the
      *informational* channel rather than the mechanical one.
    - **Classifier:** seeded plain gradient-descent logistic regression —
      fixed seed, iteration count, learning rate and L2, deliberately not a
      solver whose version could move a published AUC — fit on tasks
      t01–t08 and scored on the disjoint t09–t16, so the AUC is
      generalisation across items.
    - **Where .759 sits:** **k=2** (two rounds concatenated with `\n---\n`),
      from **g2r2**, 2026-08-09, on post-ban text with the instrument
      refitted on post-ban fit rounds, template family v3, ban sha
      `9a2f0744f81ac930`. **k=1 was .633.** Bar is AUC ≥ .70 and the ladder
      is lazy — it stops at the first qualifying rung, so k>2 was never run.
      Carried caveat from the record: the g2 spot-check's k=2 **.448** was
      instrument/distribution mismatch rather than an all-degeneracy signal,
      and part of the earlier g2r k=2 may have ridden on pole-asymmetric
      degeneracy the ban then removed.
  - **(c) SAE inventory: none locally, none official for our checkpoint, one
    third-party near-miss that misses every layer we use.**
    - **Local: none.** No file matching `*sae*` exists in the repo or the
      clone. `jlens-qwen36/data/lens/` holds J-lens artifacts only.
    - **Official — Qwen-Scope** (arXiv:2605.11887, released 2026-05): 14 SAE
      groups over 7 backbones, **Qwen3 and Qwen3.5 series only**. It does
      include **Qwen3.5-27B** — all 64 layers, d_model 5120, width 81,920
      (16× expansion), top-k {50, 100}, uniquely trained on the *instruct*
      variant, licence "qwen". Our subject is **Qwen3.6-27B-4bit**:
      **dimensionally identical** (64 layers, 5120) and **a different
      checkpoint**. Transferring an SAE across a minor version is an
      assumption, and nothing in the release supports it.
    - **Third party — `caiovicentino1/qwen36-27b-sae-papergrade`**
      (Apache-2.0, 2026-04-24, Caio Vicentino / OpenInterpretability): this
      one IS Qwen3.6-27B — 65,536 features (13×), top-k 128, 200M tokens per
      layer, self-reported variance-explained 0.84 / 0.71 / 0.82. But it
      covers **layers 11, 31 and 55**, and our workspace layers are
      **40, 44, 48, 52, 56, 60**. **Zero overlap** — L55 is adjacent to L56,
      not it. Unvetted, no paper cited.
    - **A precision caveat that applies to every option above.** Every
      published number in this program came off the **4-bit MLX** Qwen. An
      SAE trained on bf16 activations reads a different residual stream, and
      SAE feature damage under quantization is live literature
      (arXiv:2606.03002). This is the same hazard **g4** exists to measure,
      and it would have to be settled before an SAE could be used as an
      instrument here.
    - **Rough cost of training our own six, stated as an estimate.** All six
      workspace layers can be captured in **one** forward per token, so the
      collection budget is ~200M tokens of 27B forward (the third-party
      per-layer figure used as the anchor), not six times that. **Storing
      the activations is not an option:** 200M × 6 × 5120 × 2 bytes ≈
      **12.3 TB** against a 500 GB volume, so streaming/online training is
      mandatory rather than preferred. At an assumed 2–4k tok/s for a 27B
      bf16 forward on one A100-80GB, collection is **~14–28 h**, with SAE
      fitting small beside it — roughly **$25–50 and one to two box-days**
      at $1.59/hr, plus getting Qwen bf16 (~54 GB) onto the volume, which
      CLAUDE.md's volume budget already anticipates for g4. **No throughput
      has been measured for Qwen bf16 on our box, and the box does not
      currently exist**, so treat this as order-of-magnitude only.
  - **Reported, not acted on.** No file outside `RESULTS.md` and
    `results/raw/` was touched by this item.

- 2026-08-22 — **Adjudications applied: the consolidation debt is now
  pinned by a structural suite check, and `--smoke` can no longer overwrite
  the verdict of record. SUITE COUNT IS NOW 136 — that is the new checkout
  fingerprint.** (Design-instance block 2026-08-22, items 1(a) and 1(b),
  committed together as directed. 1(c)/(d)/(e) are adjudicated below and
  touch nothing.)
  - **(a) `adapters: qwen helper has exactly one definition` — ADDED, one
    check, 135 → 136.** It walks the source tree (skipping `.git`,
    `__pycache__`, `jlens-qwen36`, `archive`) and requires zero
    `_new_qwen_adapter` definitions anywhere and exactly one
    `qwen_or_explain`, in `valence_core/adapters/__init__.py`, reachable as
    `valence_core.adapters.qwen_or_explain`. Declared as ONE check per the
    adjudication: a local redefinition and a second core definition are the
    same defect from either end, and one line keeps the count a fingerprint
    rather than a running total. Structural rather than import-based, in the
    family of the quarantine's offender scan — a helper defined but never
    called is still caught.
    - **Verified to fire, both halves, rather than assumed.** Planting a
      `def _new_qwen_adapter` in `scripts/` drops the suite to 135/136 and
      names the offending file; planting a second `def qwen_or_explain`
      does the same and names both definitions; removing either returns
      136/136. This is `verify_firing`'s discipline applied to a suite
      check — a bar whose firing behaviour was never checked is not a
      pre-registration.
    - **The first version failed by finding itself.** It matched the bare
      substring `"def _new_qwen_adapter"` and duly flagged
      `regression/analysis.py`, which has to name what it guards. The
      existing quarantine scan solved that by excluding `regression/` and
      justifying the exclusion; this one instead anchors on a `def` LINE
      (`^\s*def name\b`), so it can scan its own file honestly and no
      exclusion is earned or needed.
    - **Rule-26 hygiene on the addition itself:** the check is appended
      last, and the first 135 check lines are **byte-identical** before and
      after. Nothing was recomputed; one line was added.
  - **(b) `--smoke` can no longer write the verdict artifact, and the usage
    line that demonstrated the hazard is corrected.** `e2b_verdict_campaign
    .py --smoke` with the default `--out` resolved to
    `data/e2b/verdict_campaign.json` — the 2026-08-22 NULL — and the
    module's own usage block showed exactly that invocation. The guard
    refuses it with the scratch-path fix in the message; the docstring now
    shows `--smoke --out /tmp/verdict_smoke.json` and records why the line
    was harmless when written (the file did not exist yet) and is not now.
    - **The guard fires only under `--smoke`,** so the campaign path is
      behaviourally identical to the run that produced the verdict. Checked
      three ways: the hazardous invocation is refused with a non-zero exit;
      `--smoke --out <scratch>` proceeds normally through the header, audit
      sha and monitor declarations; and `data/e2b/verdict_campaign.json` is
      unmodified (`git diff` clean on `data/`).
    - Both smokes that have ever run passed `--out` to a scratchpad, so the
      record was never at risk in fact — only in reach.
  - **(c) `s1_judge_rescue.py` — LEAVE, filed as a known hazard.** It is the
    ninth Qwen construction path: module-level `QwenMLXAdapter` import and a
    bare construction, so a wrong interpreter gives a raw traceback at
    import time, before argparse. Not converted, on the precedent this log
    articulated for `box_rl_survey.py`: a run-of-record script stays as it
    ran. Convert only if S1 machinery is reused, and as its own declared
    event.
  - **(d) `e0_probes.json` — BYTE-FROZEN, adjudicated in the record instead
    of in the file.** Its `readout.selection` string says "top-256 tokens
    per probe … union across probes"; the oracle keeps selections **per
    probe** and never unions them. **The oracle's per-probe selection is the
    definition of record under rule 26**, and the config string is a
    known-incorrect description superseded by this entry. The file is not
    edited: its `probes_sha ec2296182e726969` became load-bearing this
    morning — `assert_frozen_inputs()` checks it before any A-phase run —
    so an edit would trip the gate built today and break cross-stage
    comparability for the sake of a comment.
  - **(e) B2 repeats (1 vs the published 4) — accepted as recorded.** The
    convention is LOCK-g's to fix once A5 characterizes the backend, since
    the argument for 1 rests on determinism. No action.

- 2026-08-22 — **A2, A3 and A4 harnesses BUILT and smoked end-to-end
  against a synthetic apparatus (CLAUDE.md §Phase 0 step 5, "built now;
  runs under PROPOSAL-g"). Nothing has run on a model: no OLMo weights
  exist on this laptop and the box does not exist. The frozen e0 corpus is
  now provably the 2026-08-08 corpus — the recorded `corpus_sha`,
  `frames_sha` and `probes_sha` are plain truncated file digests, they
  match the committed files exactly, and every A-phase run now checks them
  before a 32B model loads.**
  (`scripts/box_a2_baserates.py`, `box_a3_extract.py`,
  `box_a4_instrument.py`, `box_a4_hijack.py`, plus two shared modules
  `box_e0_corpus.py` and `box_selftest_stub.py`. Raw
  [`2026-08-22_aphase_harnesses.txt`](results/raw/2026-08-22_aphase_harnesses.txt).
  Suite 135/135 — nothing in `valence_core` was touched, so no rule-26
  event is opened.)
  - **The corpus identity is checkable, and now checked.**
    `e0_axes.meta.json` and `e0_b1_markers.meta.json` have carried
    `corpus_sha 3c53e5a54fbaa233`, `frames_sha 9654b9398743116f` and
    `probes_sha ec2296182e726969` since 2026-08-08 without anything in the
    repo saying what hash they were. They are `sha256(file bytes)[:16]`, and
    all three reproduce on today's committed files. So "the frozen
    1,344-context corpus" stops being a phrase: `assert_frozen_inputs()`
    runs at the top of A3 and A4 and stops the run before the model loads.
    A stage extracted against drifted text would not be comparable to the
    three that were not, and that is exactly the failure that is invisible
    afterwards.
  - **All three corpus shapes reproduce their recorded counts**, which is
    the second half of the same check: **1,344** e0 extraction contexts
    (48 tasks × 7 conditions × 4 paraphrases), **4,608** B1 instrument
    contexts (× 2 conditions × 12 probes), and the B2 hijack corpus at
    **1,152** when the published four-fold repeat is used. One builder,
    `box_e0_corpus.py`, serves A3 and A4 — the construction was previously
    written out twice (`box_rl_survey.py`, `s2_extract_vignette.py`), and
    today's consolidation is the reason a third copy was not written.
  - **A2 — interface base rates**, one stage per run, both parts, all
    controls. (i) 24 detection-elicitation trials with **no injection
    anywhere**; affirm / deny / undecidable base rates and the usable-round
    rate against the pre-registered **≥ 0.90** gate. (ii) 8 neutral
    sessions end-to-end in the bracketed scaffold of record, degeneracy
    bound by an exact-binomial tripwire against a declared p0. Three
    things it does that the libraries alone do not: the declared bars are
    put through `verify_firing` **before the model loads** and the run
    aborts if a bar misbehaves; attribution precedence is explicit and the
    tolerant audit goes first, so a response echoing the framing is routed
    to the audit rather than counted as a base rate (ledger 28b); and the
    counters are declared as `FeatureSpec`s with decidable-n floors on
    their post-exclusion domains (ledger 28a). The ban list is **rebuilt on
    this tokenizer every run and never loaded from the committed
    `e2a_ban_list.json`**, which holds Qwen ids — token ids are not
    portable across tokenizers.
  - **A3 — extraction and guard profile**, descriptive only, no criterion
    in the file. Three axes per stage (`span_reward`, and the V2/V3 guards
    `span_character` / `span_sentiment`), R_ℓ, the per-layer geometry
    table, and a frozen family sha. It **cross-checks its own R_ℓ against
    the committed step-2 survey** for the same stage over the same corpus,
    computed by a different code path on-device: agreement is evidence both
    paths compute the definition of record, disagreement is an apparatus
    incident that should surface here rather than inside a dose four steps
    later (rule 1). The check is skipped, with its reason recorded, on
    subsamples and synthetic runs, where it would be comparing unlike
    things.
  - **A4 is two runners, because the currency has to exist before anything
    can be dosed in it.**
    - **`box_a4_instrument.py`** builds the per-stage marker instrument and
      **G_c**, the natural post-praise/post-criticism gap, on the val half —
      fit-half selection (top-256 per probe by |mean log-prob difference|,
      floor-imputed over top-4,096 sparse storage), val-half gap, σ pooled
      over poles. It mirrors `valence_core.regression.oracle
      .build_instruments`, which is the validated reference path.
    - **`box_a4_hijack.py`** runs PROPOSAL-g's fixed procedure: layer
      selection on the **fit** half at frac 0.10 over {L32, L44, L52, L60},
      then the {0.05, 0.10, 0.20, 0.40} dose ladder on the **val** half
      with ≥3 norm-matched random directions at both signs **plus a sham
      arm at every frac**. Every conjunct is reported separately — a
      criterion that can only be reported as one word is one whose failure
      mode is invisible — and the V1-lineage rule (Δ+ ≥ 0.5·G_c,
      Δ− ≤ −0.5·G_c, min > 2·max|Δ_rand|) is printed **beside** the
      PROPOSAL-g criterion rather than instead of it, so the Qwen and OLMo
      programs stay commensurable. Where they disagree, both are printed and
      neither is resolved by Code.
    - **Sham is not decorative here.** It is a second no-injection pass, so
      on a deterministic backend Δ_sham is exactly 0.0 — which makes "the
      control envelope is small" a measurement of the apparatus floor
      rather than an assumption about the harness. It read `+0.00e+00` at
      every frac on the stub.
  - **Everything was smoked, because nothing in this program runs for the
    first time on the run of record.** With no torch and no weights on this
    laptop, that required a deterministic stub `ModelAdapter`
    (`box_selftest_stub.py`): word-level tokenizer, D=32, logits a fixed
    linear function of a sequence-sensitive final residual, injections
    applied additively so a dose ladder produces sign-consistent,
    dose-monotone deltas. The full A3 → instrument → hijack chain runs on
    it; the ladder is monotone in frac; and **five refusal branches were
    exercised rather than assumed**: no sign-correct candidate layer (the
    ladder does not run and says why), stage mismatch between artifacts,
    `--n-random` below the pre-registered minimum, A3 missing a candidate
    layer, and a synthetic run attempting to write to `data/olmo/`.
    - **The stub earned its keep immediately.** Its first version made
      logits a function of the last position only, so every B1 context
      ending in `Response:` produced identical logits, σ collapsed to zero
      and G_c came out exactly 0.000000. That is precisely the shape of a
      real instrument failure, and on a stub it cost minutes instead of a
      stage of GPU time.
  - **Declared floors are Code's run config, and are labelled as such.**
    PROPOSAL-g asks for G_c's decidable-n floor to be "declared in the run
    config" and fixes no value, so `--gc-min-probes 8`, `--gc-min-val-rows
    48` and `--gc-min-abs 0.05` are declarations written into the artifact
    and reported against — freely replaceable by LOCK-g. When a floor is
    missed the runner says so and stops there: §2.4's pooled-G fallback is
    a design-instance disposition, and Code does not adjudicate a stage as
    degenerate.
  - **Forward budget for the long pole, computed without a GPU**
    (`box_a4_hijack.py --plan-only`): selection 288 × 9 = **2,592**, ladder
    288 × 37 = **10,656**, **13,248 per stage**, **52,992 for four**. At
    0.05–0.15 s/forward that is 0.74–2.21 h for the four stages. A3 adds
    1,344/stage and A4 part 1 adds 4,608/stage. The seconds-per-forward
    half is measured on the box, not projected; **A5's budget artifact is
    still owed** and cannot be finished until then.
  - **FLAG — the published B2 arm ran four identical contexts per (task,
    probe), and the default here is one.** With the Reviewer turn removed
    the four paraphrase variants are the same string, so under a
    deterministic backend they are the same forward four times, and the arm
    statistic — a mean of per-probe means — is unchanged **to the bit** by
    running one. Default `--repeats 1`, and the flag restores 4. The
    argument depends on determinism: if A5's characterization finds nonzero
    residual nondeterminism on this backend, repeats > 1 averages it and
    should be turned back on deliberately. Recorded rather than absorbed,
    because it is a deviation from the published construction even where it
    changes no number.
  - **FLAG — `e0_probes.json` describes a readout its own implementation
    does not use.** Its `readout.selection` field says "top-256 tokens per
    probe … union across probes"; the oracle — the path that reproduces the
    published B2b numbers — keeps the selections **per probe** and never
    unions them. A4 follows the oracle, because that is the validated path
    and rule 26 makes it the reference. The config wording should be
    corrected or the divergence adjudicated; not touched here.
  - **FLAG — `box_rl_survey.py` still carries its own copy of the e0
    context builder** and its paths are hardcoded to `/workspace/repo/
    jspace-lab`. It is the script that produced the four committed R_ℓ
    artifacts, so it was left exactly as it ran; pointing it at
    `box_e0_corpus.py` is a rule-26-flavoured change to a run-of-record
    script and belongs in its own event.
  - **What is NOT built and is not claimed to be:** nothing has touched a
    checkpoint, no A-phase number exists, and A5's timing budget needs
    measured rates. On "pod is up" the order is respawn protocol (both
    gates PASS) → A1 → A2 → A3 → A4 part 1 → A4 part 2 → A5.

- 2026-08-22 — **Pod-blocked preparatory pass. The volume is intact and the
  respawn integrity gate is now PROVEN to fire, not just present: exercised
  against all seven failure modes on a synthetic fixture. Pod creation
  remains a console action — `create-pod` still exposes no network-volume
  parameter, re-confirmed against the live MCP schema rather than inherited
  from the handoff.** (No model forwards; no Phase-2 data. Raw
  [`2026-08-22_podprep.txt`](results/raw/2026-08-22_podprep.txt).)
  - **RunPod state, read this session.** The MCP *was* authorised here,
    against the handoff's expectation that a non-interactive thread cannot
    reach it — so the state is measured, not assumed. **0 pods** (none
    running, none stopped). Network volume **`o73qvy742n`** intact:
    `holy_beige_viper_volume`, **500 GB**, **US-CA-2**, HIGH_PERFORMANCE.
    **A100-SXM4-80GB**: secure cloud available, stock **Medium**,
    **$1.59/hr**, CUDA 12.4 / 12.8 / 13.0 all AVAILABLE — 12.8 is the one
    the image of record (`runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`)
    wants. No templates exist, so there is no saved-template route either.
  - **The blocker is capability, not authorisation.** `create-pod`'s schema
    carries only `volumeInGb` / `volumeMountPath`, which provision *new*
    ephemeral storage. A pod created through it would mount an empty
    `/workspace`, fail the respawn integrity gate, and put a 386 GB
    re-download in front of A-phase. HANDOFF-2026-08-20 §2's finding is
    therefore re-confirmed on today's schema and stands unchanged: **the pod
    is created in the console**, region-locked to US-CA-2, with
    `o73qvy742n` attached at `/workspace` and TCP 22 exposed.
  - **Respawn step (i) is now verified executable.** CLAUDE.md §Environment
    calls `box_respawn_check.py` "executable, not aspirational"; that had
    never been demonstrated, and a gate that silently passes is worse than
    no gate on the box where it matters. Run against a synthetic two-stage
    fixture (`MODELS` / `MANIFEST` are env-overridable, so no box is
    needed):

    | case | exit | reported as |
    |---|---|---|
    | clean volume | **0** | INTEGRITY PASS, 4 files / 2 checkpoints |
    | one byte flipped, size unchanged | **1** | `MISMATCH` |
    | file deleted | **1** | `MISSING` |
    | unlisted weights file added | **1** | `EXTRA (not in manifest)` |
    | size changed | **1** | `size 903 != 900` |
    | manifest absent | **2** | `ABORT: manifest not found` |
    | whole checkpoint directory gone | **1** | `directory missing` |

    Both asymmetries fire, the byte-level check is not shadowed by the size
    check, and no failure mode exits 0. The committed manifest itself is
    complete: four stages, **94 leaf entries**, per-file sha256 + bytes.
  - **A carried handoff item is DISCHARGED.** HANDOFF-2026-08-20 §2 records
    the design instance's PROPOSAL-g status-line amendment as applied to the
    laptop working tree and never committed, with the repo still reading
    "DRAFT v1.0". It was committed at **`499f6d5`**; PROPOSAL-g now reads
    "**Status: LOCKED** — pre-registration of record at commit `72b09a9`",
    and no occurrence of "DRAFT" survives in the document. That line of §2
    is stale and should not be acted on.
  - **A-phase readiness, so the next box session knows what it is starting
    with.** Built and suite-covered: **A1** (`box_a1_tagscreen.py --stage`
    ×4 → `a1_roster.py`, with `data/configs/a1_roster_candidates.json`
    committed) and **A5** (`box_respawn_check.py`, verified above, +
    `box_determinism.py`). Not yet built: **A2** (i) detection-elicitation
    base-rate runner and (ii) neutral operant-session runner, **A3**
    per-stage e0 extraction + guard profile, **A4** hijack / dose-ladder /
    currency. Their libraries exist — `valence_core.detection`,
    `valence_core.session`, `valence_core.extract`, `valence_core.gate` —
    and so do their corpora (`data/corpus/e0_tasks.jsonl`,
    `data/configs/e0_frames.json`, `e0_probes.json`); what is missing is the
    box runners. CLAUDE.md §Phase 0 step 5 licenses building them now, and
    none of that work needs a pod. **Flagged for a go, not started.**
  - All ten `box_*` / `a1_*` scripts compile clean on this laptop; only
    `box_respawn_check.py` runs without torch, and it is the one that had to.

- 2026-08-22 — **CONSOLIDATION ACCEPTANCE EVENT: GREEN. The
  `_new_qwen_adapter` debt is paid into one
  `valence_core.adapters.qwen_or_explain()` across eight call sites, and the
  Route-3 e2a session template leaves the quarantine package for
  `valence_core/session_e2a.py`. Suite 135/135 before and after — the whole
  output byte-identical, check for check — and H3 re-run through the new
  helper reproduces its committed artifact to the sha.**
  (LOCK-h §7's queued event, sequenced strictly after the disposition entry
  above per the 2026-08-22 adjudication. Refactor only: no criterion,
  constant, corpus, dose or published number is touched. Raw
  [`2026-08-22_consolidation.txt`](results/raw/2026-08-22_consolidation.txt).)
  - **The debt was bigger than the lock records and less uniform than the
    handoff records.** LOCK-h §7 says four copies; HANDOFF-2026-08-22 §2
    corrected the count to eight. Both were right when written, and neither
    is right about the shape: the eight are **four distinct variants**, not
    eight verbatim copies. `h3_tagscreen_qwen`, `s2_extract_vignette` and
    `s2_neighbor_axes` carry the full docstring and the long "wrong
    interpreter" message; `h3b_repair_screen` carries the long message under
    a docstring recording the debt itself; `e2b_h2_readstability` carries a
    one-line docstring and a short message; `e2b_h2_sessions`,
    `e2b_h1_sessions` and `e2b_verdict_campaign` carry the short message and
    no docstring. Same `try`/`except`, same exception pair, same fix.
  - **One behavioural delta, and it is on the failure path only.** The
    consolidated function takes the LONG message — the one that names the
    interpreter, the reason and the trap. The four short-message scripts now
    print more than they used to when run under the wrong python; nothing
    else about them changes. The rendered message was asserted byte-for-byte
    against the long form *before* any script was touched. On the success
    path the function does what all eight did — deferred import, construct,
    return — so `valence_core` still imports on a machine with neither MLX
    nor torch, which is asserted rather than assumed.
  - **`caller_file` is passed explicitly at all eight sites.** The old helper
    closed over its script's `__file__` and `REPO`; the moved one cannot.
    Recovering the caller by walking the stack was rejected: it would make
    the message depend on how the script was invoked, and the message is the
    entire point of the function. `sys.argv[0]` is the fallback for a caller
    with no `__file__`. `QWEN_PY` moves with the helper — one definition,
    imported by `s2_neighbor_axes`, the one script that also uses it outside
    the helper.
  - **(b) The Route-3 module's permanent home is the general core, and the
    reason is the quarantine's own principle.** `valence_core/e2b/` says of
    itself that what lives there is split by hazard. This module has none:
    no injection, no adapter, no state — it replays scaffolding from the
    record and checks it against the archive. Two things follow from moving
    it to `valence_core/session_e2a.py`. The e2a template stops being
    reachable only through a quarantine namespace, which is what a general
    instrument should be. And `statepresent`'s guard sanctions importers **by
    directory** — every inert module parked in `e2b/` is one more module that
    could hold the capability without tripping the guard — so moving this one
    out makes the quarantine **narrower**, not wider. `records.py` stays
    behind: rule 5(e)'s provenance machinery is e2b's subject matter, and
    this is not. Convenient accident worth recording: `valence_core.e2b.session`
    and `valence_core.session_e2a` are both 24 characters, so every
    continuation line and `# noqa` column in the five import sites is
    unchanged by the rename.
  - **Rule 5(e) re-verified after the move, in both directions.**

    | check | result |
    |---|---|
    | `import valence_core.e2b.statepresent` from an unsanctioned caller | `ImportError`, guard text unchanged |
    | sanctioned `scripts/e2b_*.py` runners still import it | 4/4 clean |
    | no module in `valence_core` outside `e2b/` names the primitive | 0 offenders — and `session_e2a.py` is now *inside* that scan |
    | `readout.choice_read` still cannot inject; signature unchanged | PASS |
    | modules sanctioned **by directory** | 2 (`records`, `statepresent`) — was 3 |

  - **Acceptance, under ledger 26.** The suite is necessary and not
    sufficient — it is model-free, and the helper is a model-loading path —
    so a real adapter-constructing run is carried beside it.

    | evidence | result |
    |---|---|
    | suite, pre-move (at `4fbe9a3`) | **135/135** |
    | suite, post-move | **135/135**, output byte-identical to pre-move |
    | Route-3 reconstruction through the new import path | **200/200** scaffoldings, **200/200** seed streams |
    | H3 re-run through `qwen_or_explain()` vs `data/e2b/h3_tagscreen.json` | **identical sha256** `2b764063a1b6…`, 142 s against the published 143 s |
    | e2b verdict smoke, post-move, `--out` to scratch | **every counter reproduced** vs the committed pre-move smoke — arm order, 2/2 valid per arm, cumulative paired reads 6/12/12/12/18/24, n_d 1 (b 1, c 0), 0 terminations, 0 clipped; wall-clock 506 s vs 504 s |

  - **The suite stays at 135 deliberately.** A structural check pinning the
    debt as paid — "no script defines a local `_new_qwen_adapter`", "exactly
    one `qwen_or_explain`" — belongs to the same family as the quarantine's
    offender scan and is **recommended**. It is not added here: it would move
    the count off 135, which is the fingerprint every handoff uses to date a
    checkout, and the rule-26 comparison is cleanest when the check list is
    identical on both sides of the move. Design instance's call.
  - **FLAG — a ninth Qwen construction path, out of scope and left alone.**
    `scripts/s1_judge_rescue.py` never had the helper: it imports
    `QwenMLXAdapter` at MODULE level and constructs it bare. It is the one
    Qwen script that still answers a wrong interpreter with a raw traceback,
    and it does so at import time, before argparse — so even `--help` fails.
    One line converts it. Not done: scope (a) is the `_new_qwen_adapter`
    debt, and this is not a copy of it.
  - **FLAG — `--smoke` defaults its `--out` to the verdict artifact of
    record.** `e2b_verdict_campaign.py --smoke` with no `--out` writes
    `data/e2b/verdict_campaign.json` — the committed campaign — and the
    module's own usage block shows exactly that invocation. It was harmless
    when written, because the file did not exist yet; it is not harmless now.
    Both smokes to date passed `--out` to a scratchpad and the record is
    intact. A guard refusing the canonical path under `--smoke` is a
    one-liner and is recommended.
  - **Surveyed and left:** `valence_core/regression/oracle.py` constructs
    `QwenMLXAdapter(legacy_truncate=True)` directly. That is a deliberate
    legacy-path construction inside the core with its own deferred import,
    not a copy of the helper, and it should not be printing a script-entry
    message at anyone.
  - **Nothing in the dated record was rewritten.** Four earlier entries name
    `_new_qwen_adapter` and two name `valence_core/e2b/session.py`; they
    describe the state on their own dates and are left exactly as written.
    LOCK-h §7 likewise stands unedited. HANDOFF-2026-08-22 §2 (the one item
    Code owed) and its §4 debt row are discharged by this entry, and the
    handoff is left alone under its own precedence clause: where it and the
    log disagree, the log is right.

- 2026-08-22 — **e2b DISPOSITION (design instance): the NULL is
  ADOPTED. The registered cell — PROPOSAL-h §4, "e2b null, H1
  clean" — is taken verbatim, and the live-state alternative is
  removed. The program's closing statement carries its last clause:
  rich in evaluative representation and empty, so far as these
  instruments can see, of anything that wants — in memory, in
  weights, in text, and now in the present tense.**
  - **This null is an answer, not a failure to measure — concluded
    AND answered, the channel verifiably open on every term.** The
    state was live at each choice and delivered by the choice (arm
    geometry verified on smoke and run); dose potency and stability
    were carried by H2 (PASS FINAL); the leakage budget was paid by
    H1 (PASS by low-discordance certification, π̂_d .0172, CI
    [.0086, .0305] against bar .0735) and re-measured on the verdict
    tier itself (+0.00198 = 2.7% of bar); all three arms reached
    their valid targets; no monitor fired; the window was clean.
    Under those open channels the subject chose at chance:
    Δ_first = −0.0104 (47/96), failing all three conjuncts —
    envelope, sign lock, exact binomial (p = .6202) — with nothing
    marginal about any of them.
  - **The insulated replication inside the campaign is part of the
    verdict's standing.** The paired shadow reads ran e2a's design
    over identical prefixes and landed at exactly 48/96, Δ = +0.0000
    — the published null reproduced to the session, inside the
    state-present apparatus. The instrument did not drift between
    designs; the answer did not change with the state present.
  - **Scope, stated so the sentence cannot grow.** Chance-compatible
    is not chance-proven: effects below the design's MDE (LOCK-h v2
    §2) are not excluded. The claim covers this subject, this axis
    family and dose, this readout, under shields — nothing wider.
  - **Welfare pre-commitment: ARMED, NOT TRIGGERED.** Recorded as
    the pre-registration requires.
  - **e2b-r1 residual, recorded and not chased:** p(stay | on +)
    .1053 vs p(stay | on −) .0558 — descriptive, on a secondary the
    primary's failure made non-verdict-relevant. It licenses at most
    a future pre-registration, never a follow-up inside this
    campaign. The ~92% alternation replicating under a live state is
    e2a's finding again, now in the present tense.
  - **Termination caveat carried:** 3 attempts across all sessions
    including excluded; not directly comparable to cycle 3/4's table
    because audit v2's `banner_terminator` also excludes.
  - **e2b is CLOSED. No further cells.** PROPOSAL-h is complete; the
    Qwen measurement program is complete. Next design artifact:
    FINDINGS-5 (S1 / S2 / H-cal / e2b synthesis).

- 2026-08-22 — **e2b VERDICT CAMPAIGN: NULL. All three conjuncts fail.
  Δ_first = −0.0104 (47/96) with the state live at the choice and delivered
  by the choice. The shadow reads — e2a's insulated design running inside
  e2b — land at exactly 48/96. H1 was clean, so this is PROPOSAL-h §4's
  "e2b null, H1 clean" cell: the live-state alternative is removed.**
  ([`data/e2b/verdict_campaign.json`](data/e2b/verdict_campaign.json),
  [`verdict_analysis.json`](data/e2b/verdict_analysis.json); raw
  [`2026-08-22_verdict_campaign.txt`](results/raw/2026-08-22_verdict_campaign.txt),
  [`_analysis`](results/raw/2026-08-22_verdict_analysis.txt). LOCK-h v2.0
  §2, licensed at `f030cdd`; analyzer committed at `a2f074d` **before** the
  run; audit v2 sha `7aa235d25eeb66dc` verified at startup; 4.03 h.)
  - **All three arms reached their valid targets. No monitor fired.**
    marker 96 valid / 102 run (5.9% excluded), sham 36/37 (2.7%), random
    36/42 (14.3%). Six leak checkpoints, every one report-only: π̂_d
    0.0227 → 0.0271 → 0.0234 → 0.0174 → 0.0202 → 0.0182, |L̂| never above
    0.0076 against a pause threshold of 0.0368. Window clean, 0 clipped
    across 792 paired reads and 1,707 rounds. Degeneracy 22/1707 = 0.0129.
  - **The primary, term by term — it does not fail narrowly on one conjunct,
    it fails all three:**

    | conjunct | value | |
    |---|---|---|
    | Δ_first, marker | **−0.0104** (47/96) | — |
    | (i) exceeds realised envelope | envelope **0.0833** (sham −0.0833, random −0.0278) | **fail** |
    | (ii) sign locks across maps | map0 −0.0106 (n=47), map1 −0.0102 (n=49) | **fail** |
    | (iii) one-sided exact binomial | **p = 0.6202**, critical k ≥ 57 | **fail** |

    Δ is *negative* and tiny — 47 of 96 first free choices went to the
    +tag, one short of the 48 that is exactly chance. There is no direction
    here to argue about.
  - **The within-campaign insulated replication landed on the nose.** The
    shadow reads — the vanilla state-free forward taken over the identical
    prefix at every state-present read — give **Δ_first = +0.0000 (48/96)**,
    exactly chance. e2a's design ran inside e2b for the price of one extra
    forward per read (PROPOSAL-h §0.2 (ii)), and it reproduced e2a's null
    to the session. Session-share 0.5087, also at chance.
  - **What this cell means, quoting the grid registered before any data**
    (PROPOSAL-h §4, "e2b null, H1 clean"): *"The strongest form of the
    program's conclusion: drug in the tissue at the moment of choice,
    rat-style, and still no seeking. The live-state alternative is removed;
    'rich in evaluative representation, empty of anything that wants' now
    covers the present tense."* The state was live at the choice, the choice
    delivered it, the leak was certified at 2.1% of its bar, and the subject
    chose at chance.
  - **Secondary, and it is NOT verdict-relevant because the primary did not
    fire.** p(stay | on +) = 0.1053 (26/247), p(stay | on −) = 0.0558
    (13/233). Both are *low*: the subject **switches ~92% of the time**,
    which is e2a's alternation finding replicating under a live state. The
    +/− difference is descriptive only and licenses at most a
    pre-registration, per §3.
  - **§3b registered secondary: null.** ICC 0.0195, p = 0.789; sessions with
    ≥ 2 flips = 1, p = 0.789. The i.i.d. treatment stands — the third
    campaign running to say so.
  - **In-campaign leak, measured on the verdict tier itself:** marker flip
    rate 0.0191, state-reversing half-gap **+0.00198 = 2.7% of bar_leak**;
    random arm flip rate 0.0139. The directional-leak family now has five
    members across every configuration tested — +0.00084, +0.00220, 0.00000,
    +0.00156, +0.00198 — none above 3% of the bar.
  - **Termination counter: 3 attempts** across all sessions including
    excluded, in 3 distinct (arm, config, round-position) cells. The subject's
    measurable exit was available throughout and was essentially unused.
    Reported with the caveat already flagged: audit v2's `banner_terminator`
    now also *excludes* a session that emits one, so this table is not
    directly comparable to cycle 3/4's.
  - **Disposition is the design instance's.** Code ran the registered
    criterion over a committed artifact with an analyzer committed before
    the campaign, and reports what it returned. Suite 135/135.

- 2026-08-22 — **Verdict campaign runner built and smoked. Measured budget
  ≈ 4.7 h at the H1-observed exclusion rate, against the ~5.8 h projection.
  One false-provenance defect caught in the smoke and fixed before the
  campaign.**
  (`scripts/e2b_verdict_campaign.py`; smoke 6 sessions, 504 s. **Not the
  campaign — nothing is committed to `data/e2b/verdict_campaign.json` yet.**)
  - **Measured budget, from per-arm timings rather than a projection:**
    marker **92 s**/session, random **93 s**, sham **65 s** — sham is
    cheaper because a state-free read is one forward, not the paired two.

    | exclusion rate | sessions run | total |
    |---|---|---|
    | 0% | 96 / 36 / 36 | 4.03 h |
    | **H1-observed 13.0%** | **111 / 42 / 42** | **4.68 h** |
    | 20% | 120 / 45 / 45 | 5.04 h |
    | all arms at cap | 160 / 64 / 64 | 6.90 h (absolute worst case) |

  - **The arm geometry verified on the smoke, not assumed.** In every arm
    `live[i+1] == pick[i]` — **the choice delivers the state**, which is the
    one thing that distinguishes the verdict tier from H1, where the schedule
    did. First read sits on the forced-phase end state. Marker and random
    take 6/6 state-present paired reads; **sham takes 0/6** and goes through
    the untouched `readout.choice_read`, because a read with no state needs
    no exception and must not borrow one.
  - **FLAG, caught in the smoke and fixed: the random arm was stamping false
    provenance.** Every read carried `axis="span_reward"` because the axis
    key was passed for all three arms — on the one arm whose entire purpose
    is *not* being the axis. Rule 5(e) requires per-read injection
    provenance, and provenance that names the wrong direction is worse than
    none. Now `random_dir_L48`. The record was never ambiguous in the strong
    sense — `direction_sha` is a required provenance field and the two
    directions differ — but a reader would have had to notice the sha to
    catch it.
  - **FLAG — an interaction between two monitors that did not exist before
    audit v2.** The termination-attempt patterns
    (`data/configs/f_termination_patterns.json`, pulled in from the clone so
    the counter travels with the record) include `===\s*[Ee]nd`, and audit
    v2's `banner_terminator` matches the same text. A `=== end ===` response
    is therefore **both** a termination attempt (descriptive, tabulated over
    ALL sessions including excluded ones) **and** a v2 degeneracy (which
    excludes). Before v2 it was only the former. Both fire, no conflict — but
    the termination table for this campaign is not comparable to cycle 3/4's
    without saying so, because the same response now also removes the
    session.
  - **Checks that passed before any model time.** Pure-python
    Clopper-Pearson (no scipy on this laptop) matches `scipy.stats.beta.ppf`
    to **1e-16** on five cases including 6/11, reproducing H1's
    [0.2338, 0.8325] exactly. Schedules: marker 128 = 16 per (pair, map) with
    forced-end 64/64; sham and random 48 each = 6 per (pair, map) with
    forced order counterbalanced across reps. Audit sha recomputed and
    checked at startup.
  - **Separation held.** The runner records picks, flips and the b/c split
    and **does not evaluate the primary** — Δ_first, the control envelope,
    the sign lock and the exact binomial go to `e2b_verdict_analyze.py` over
    the committed artifact, the same split H1 used so that a runner cannot
    stop when it likes the verdict.
  - Awaiting the go for the sitting.

- 2026-08-22 — **LOCK-h v2 §6 values-check: GREEN, 41/41. Every §1 number
  and §2 constant matches the artifact §6 names for it. The one apparent
  mismatch was in the checker, not the lock. PROPOSAL-h carries the
  interpretive note (`b400083`).**
  ([`data/e2b/lockh_v2_valuescheck.json`](data/e2b/lockh_v2_valuescheck.json);
  `scripts/lockh_v2_valuescheck.py`; raw
  [`2026-08-22_lockh_v2_valuescheck.txt`](results/raw/2026-08-22_lockh_v2_valuescheck.txt))
  - **What was checked.** All 41: the dose triple (L48 / 0.10 / |α| =
    10.3010), H2's degeneracy both ways, its declared p0, window, π̂_d; H1's
    N / sessions-run / exclusions / no-appended-block, n_d and the b–c split,
    π̂_d and its CI, L̂, the mapped L CI, the PASS and its
    low-discordance standing, both §3b p-values; the audit sha **recorded,
    recomputed from the artifact body, and matched against the sha H1
    actually ran under**; the four-member directional-leak family; and §2's
    envelope p90, critical k, MDE, bar_leak, the 2.1%-of-bar figure, the
    monitor threshold, and the registered arm n's.
  - **The apparent mismatch, and why it was mine.** The check first reported
    §2's monitor threshold as 0.0367 against the lock's 0.0368. bar_leak/2 =
    **0.03675 exactly**, and 0.0368 is its correct 4-dp rounding — but the
    binary double is a hair under 0.03675, so Python's `round()` returns
    0.0367. A second attempt with a 5e-05 float tolerance sat exactly on the
    boundary and failed by 1.4e-19. Settled with `Decimal` and
    `ROUND_HALF_UP`. **Two checker bugs, no lock defect** — recorded because
    a values-check that reports a false mismatch is as costly as one that
    misses a true one, and the failure mode (comparing rounded floats) will
    recur.
  - **Item 1 applied.** The interpretive note is **appended** at the end of
    PROPOSAL-h, never edited into §2 — the pre-registration's hash is its
    timestamp, so a clarification goes beside it. Same repair-beside pattern
    as the e2a published-record correction and the H2 provenance defect.
  - **ASSEMBLED 2026-08-22.** v2.0 is now `LOCK-h.md`'s head content with
    the v1.x text below it, both halves verified **byte-for-byte**: the v2
    head matches the delivered file exactly, and the 11,896-byte v1.x record
    is identical to the previous `LOCK-h.md`. A separator marks the v1.x
    record as the H-cal history, not operative for the verdict tier. The
    standalone `LOCK-h-v2.md` is removed so two files cannot claim to be the
    lock and drift.
  - **A gap in this very check, found while assembling and closed.** The
    values-check opened the lock file and **never read it** — it compared
    numbers Code had typed into the checker against the artifacts, which
    proves the artifacts agree with Code, not that the LOCK says what Code
    thinks it says. A typo in the lock that Code did not replicate would have
    passed 41/41. Each claim now carries a `needle` asserted against the lock
    text: **18 located verbatim, 0 claimed but absent**, re-run against the
    assembled file. The remaining 23 are derived or structural values with no
    single literal form in the document, and are marked as such rather than
    silently counted as located.
  - **VERDICT: GREEN. LOCK-h v2 verified, ready to commit.**

- 2026-08-21 — **H1 GATE RUN OF RECORD: reached its declared exit at
  session 123, read 4, and PASSES. N = 640, n_d = 11 (b = 6, c = 5),
  π̂_d = 0.0172, L̂ = +0.00156; mapped L CI [−0.00915, +0.01143] against a
  bar of ±0.0735. The §3b registered secondaries are NULL — H2's post-hoc
  clustering hint did not replicate.**
  ([`data/e2b/h1_sessions.json`](data/e2b/h1_sessions.json),
  [`h1_gate.json`](data/e2b/h1_gate.json); raw
  [`2026-08-21_h1_gate.txt`](results/raw/2026-08-21_h1_gate.txt),
  [`_eval`](results/raw/2026-08-21_h1_gate_eval.txt). Audit v2 sha
  `7aa235d25eeb66dc` recomputed and verified at startup; rounds cached per
  the g1 artifact; 9,693 s.)
  - **The v1.4 schedule worked exactly as sized.** 123 sessions run of 128
    scheduled, **16 excluded (13.0%)**, stop reached **without appending a
    block**. v1.2's 112 could not have got there; 128 did, with 5 sessions
    to spare. The sizing note is now a measurement rather than a projection.
  - **Gate, per §3:** exact 95% CI on p_flip = 6/11 is [0.2338, 0.8325];
    mapped through π̂_d it is **[−0.00915, +0.01143]**, entirely inside
    (−0.0735, +0.0735). **VERDICT: PASS.**
  - **Reported as CERTIFICATION BY LOW DISCORDANCE, per the rule ratified
    2026-08-21 — not as a powered directional test.** π̂_d = 0.0172 sits
    below the bar on its own, so the mapped interval lies inside
    [−π̂_d, +π̂_d] whatever the b/c split; §3's feasibility corollary is what
    certifies. π̂_d's own exact 95% CI is **[0.0086, 0.0305]**, upper bound
    well below the bar — so the certification is not marginal, but it is
    still a certification by *how little the state moves choices*, not by a
    directional test that had power and found nothing.
  - **§3b registered secondaries, both NULL** (200,000 uniform-placement
    draws, two-sided by tail probability, α = .05 each): ICĈ = **0.0000**
    against a null mean of 0.0103, **p = 1.0000**; sessions carrying ≥ 2
    flips = **0** against a null mean of 0.415, **p = 1.0000**. **The i.i.d.
    treatment stands.**
    - **H2's post-hoc clustering did not replicate, and that is the useful
      part.** H2 gave ICĈ = 0.1443 with permutation p ≈ 0.017 on five
      events; H1, with 11 flips over 640 reads, finds **zero** sessions
      carrying two flips where chance alone predicts 0.415. The earlier hint
      was noise, as the entry that reported it cautioned — which is why it
      was registered into §3b rather than acted on. H2's values are cited
      here descriptively and are not pooled.
  - **Where the leak actually landed.** L̂ = +0.00156 is **2.1% of
    bar_leak**; the b/c split is 6/5, about as close to the b = c null as 11
    events allow. Across the campaign family the directional component has
    now been measured four times — read half +0.00084, H2 +0.00220, H1-u
    exactly 0.00000, H1 +0.00156 — all inside 3% of the bar.
  - **Monitors:** degeneracy **22/1111 = 0.0198** under audit v2 (which
    catches strictly more than the monitor e2a ran); exclusions 16/123 =
    13.0%; **window clean, 0 clipped** across 640 paired reads and 1,111
    rounds. Checkpoints at 128/256/384/512/640 reads: π̂_d 0.0076, 0.0078,
    0.0156, 0.0174, 0.0172; ICĈ 0.0000 at every one; ceiling 1.00
    throughout; no pause, and the 0.30 stability ceiling never approached.
  - **What this unblocks, and what it does not.** The leakage budget is paid:
    PROPOSAL-h §2's gate on opening the verdict tier is satisfied on the
    numbers. **The disposition is the design instance's**, and LOCK-h v2 is
    still owed before any verdict session — §5 requires it to carry H2's
    confirmed dose and stability numbers, H1's realised (n_d, N, π̂_d, CI),
    and the verdict criteria restated with those values in place.
  - Code evaluates the declared criterion over a committed artifact and
    stops. Suite 135/135.

- 2026-08-21 — **H1-u redesignated and logged as the prefix-steering
  comparison arm; LOCK-h v1.4 applied and §6-verified; H1 gate run of record
  launched with steered rounds and the exclusion-robust schedule.**
  - **Item 1 — H1-u.** The as-run campaign is relabelled **H1-u**
    (unsteered-prefix auxiliary) in
    [`data/e2b/h1u_sessions.json`](data/e2b/h1u_sessions.json) and its raw
    log; the artifact carries a `designation` block stating **descriptive
    standing only, gate never evaluated and never may be on it**, and naming
    both defects — the unsteered-round reading *and* the short stop. The
    comparison it now serves:

    | campaign | prefix steering | π̂_d |
    |---|---|---|
    | read-half precursor | none (archived state-free prefixes) | 0.0208 |
    | **H1-u** | forced phase only; post-choice rounds unsteered | **0.0208** |
    | H2 proper | fully steered rounds | 0.0278 |

    The read half and H1-u agree to four decimals across 288 and 576 reads,
    so the whole **measured prefix-steering contribution to π̂_d is 0.0070**.
    Small — and the reason the gate must nonetheless run steered is that
    0.0070 is 9.5% of bar_leak, not nothing, and the gate certifies a
    quantity the verdict tier will inherit.
  - **Item 2 — LOCK-h v1.4 applied, §6 re-run byte-identical GREEN**
    (`d94e281`). **Placement flagged rather than silently resolved:** the
    steered-rounds clarification was specified for "§2's H1 paragraph", and
    LOCK-h's §2 is *The bar* — it has no H1 paragraph. The sentence the
    clarification corrects ("Session content: identical to verdict sessions
    except contingency-free … state schedule per PROPOSAL-h §2") lives in
    §3a, so the clarification is written immediately after it and the
    placement is recorded in §8. If PROPOSAL-h §2 was meant — amending the
    committed pre-registration rather than the lock that instantiates it —
    that is a different act and needs saying.
  - **Sizing checked, not assumed.** 640 reads at m = 6 needs **107 valid
    sessions**: 112 tolerates 4.5% and delivers 570 at the realised 14.3%
    rate (short, as run); **128 tolerates 16.4% and delivers 654**; the 160
    cap tolerates 33.1%. Simulated across exclusion rates, the v1.4 schedule
    reaches 640 without appending at ≤14.3%, appends twice and still reaches
    it at 30%, and only falls short at 50% — far beyond anything observed.
  - **Item 3 — the steering change, and the geometry it preserves.** The
    verdict tier delivers a state at choice ci that is live through round ci
    **and into read ci+1**. H1 substitutes the schedule for the choice and
    changes nothing else: `read_state(ci)` alternates from the forced-phase
    end state, and **round ci is generated under `read_state(ci+1)`** — the
    state the next read will sit on. Verified on the smoke: reads alternate
    from `forced_end` 12/12, round state equals the next read's state 12/12,
    and both are independent of the picks.
  - **Two harness defects caught before they reached the record.** A
    2-session smoke dutifully headed for 160 sessions, because `--n-sessions`
    is the *initial* schedule and the append contingency correctly grows it —
    `--session-cap` is the limit. Documented in the usage line. And the first
    gate launch was killed after 3 minutes because its run header still
    printed the stale `rounds are UNSTEERED` line: the code was right and the
    header lied, which in a run-of-record log is the same as being wrong. No
    data from that launch is retained; the relaunch's header is quoted in the
    raw log.
  - H1 gate run of record in flight: 128 scheduled, steered rounds, audit v2
    sha verified at startup, stop at n_d = 200 or N = 640, ~3.0 h.

- 2026-08-21 — **[REDESIGNATED **H1-u**, auxiliary, by the 2026-08-21
  adjudication — descriptive standing only, gate never evaluated. Two
  defects, not one: the unsteered-round reading (corrected by LOCK-h v1.4 §2)
  and the short stop below.]** H1-u ran all 112 scheduled sessions and
  STOPPED SHORT of its declared exit: N = 576 of 640 paired reads. The §3a schedule is sized as
  if exclusions were zero and could not have reached 640 at any historically
  observed exclusion rate. The gate is NOT evaluated. Design-instance
  disposition required.**
  ([`data/e2b/h1_sessions.json`](data/e2b/h1_sessions.json); raw
  [`2026-08-21_h1_sessions.txt`](results/raw/2026-08-21_h1_sessions.txt);
  audit v2 sha `7aa235d25eeb66dc` verified at startup; 8,732 s.)
  - **What happened, arithmetically.** 112 sessions ran; **16 were excluded**
    (14.3%); an excluded session contributes 0 reads, so 96 × 6 = **576**.
    §3a budgeted 112 × 6 = 672 against N_max = 640 — **32 reads, 5.33
    sessions of slack.** Sixteen exclusions cost 96.
  - **This was not bad luck, and it is not audit v2's doing.** Delivering 640
    reads at m = 6 needs **107 valid sessions**, so 112 scheduled permits at
    most **5 exclusions — 4.5%**. Against every rate on the record:

    | exclusion rate | valid of 112 | reads delivered | vs 640 |
    |---|---|---|---|
    | e2a archive, 8.0% | 103 | 618 | SHORT |
    | H2 under audit v1, 6.2% | 105 | 630 | SHORT |
    | H1 realised under audit v2, 14.3% | 96 | **576** | SHORT |

    **The schedule could not have delivered its own stop at any rate ever
    observed on this apparatus.** And audit v2 is not the cause: **1 of the
    16 exclusions came from a new pattern; the other 15 would have fired
    under the cycle-3/4 audit unchanged.**
  - **My miss, stated plainly.** When §3a landed I verified 112 × 6 = 672 ≥
    640 and reported "32 reads of slack, 5.33 sessions" — correct arithmetic,
    and I did not check it against the exclusion rate sitting in the archive
    I had already read (16/200). Verifying a number as stated is not the same
    as verifying it is adequate, and the difference cost a 2.4 h campaign.
  - **The gate is NOT evaluated, and that is deliberate.** §3 applies the
    criterion "at stop", and exhausting the schedule is not one of the two
    declared exits. Reporting a verdict from a plan that was not met is
    exactly what a pre-registration exists to prevent.
  - **What the run does say, DESCRIPTIVE and explicitly not the gate:**
    n_d = **12**, **b = 6, c = 6**, so **L̂ = (b − c)/N = exactly
    +0.00000**. π̂_d = 12/576 = **0.0208**, 95% CI **[0.0108, 0.0361]** —
    upper bound far below bar_leak = 0.0735, and strikingly close to the
    read-half precursor's 0.0208. The mapped L interval is
    **[−0.01204, +0.01204]**, entirely inside (−0.0735, +0.0735).
  - **One statistical point that matters for the disposition.** The stop was
    driven by the schedule length and by exclusions arising in generation —
    **never by the b/c split.** So conditional on n_d, b is still exactly
    Binomial(n_d, ½) under the null, and the §3 exactness argument survives
    intact. An evaluation at N = 576, or an extension to 640, is
    statistically sound; what is missing is authorisation, not validity.
  - **Options, with the arithmetic done:** (i) dispose the gate at N = 576 as
    an amended exit; (ii) **extend by ~13 sessions** — 125 scheduled delivers
    640 at the realised 14.3% rate — as a partial 8th block, which breaks
    §3a's whole-block stratification; (iii) re-plan the schedule with an
    exclusion allowance and re-run. Code recommends nothing here; the numbers
    are above.
  - **Checkpoints, all clean, no pause at any of them:** 128 reads π̂_d
    0.0076 / ICĈ 0.0000; 256 → 0.0078 / 0.0000; 384 → 0.0104 / 0.0000;
    512 → 0.0174 / 0.0296. Ceiling 1.00 throughout (π̂_d never approached
    0.08), and the 0.30 stability ceiling was never neared.
  - **Monitors:** degeneracy 27/1003 = 0.0269 against the declared p0 = 0.05,
    exact binomial p = 0.9999 — within tolerance. Window clean, 0 clipped.
    16 exclusions, all in the forced phase, which is the phase H1 shares
    unchanged with H2 and e2a.
  - **Reading flag — RESOLVED against Code's reading (2026-08-21).** H1-u's
    post-choice rounds ran UNSTEERED. LOCK-h v1.4 §2 clarifies that H1
    sessions are identical to verdict sessions **including steered
    post-choice rounds**, the schedule rather than the choice selecting each
    round's state, so the gate certifies the leak in the verdict tier's own
    prefix environment. This campaign is therefore the wrong one for the
    gate and is retained as the **prefix-steering comparison arm**:

    | campaign | prefix steering | π̂_d |
    |---|---|---|
    | read-half precursor | none (archived state-free prefixes) | 0.0208 |
    | **H1-u** | forced phase only, post-choice rounds unsteered | **0.0208** |
    | H2 proper | fully steered rounds | 0.0278 |

    The read half and H1-u agree to four decimals, and the whole measured
    **prefix-steering contribution to π̂_d is 0.0070** — small, and the only
    reason the H1 gate must run in the steered environment rather than
    inherit either number.

- 2026-08-21 — **Sweep batch applied: audit v2 approved and frozen
  (sha `7aa235d25eeb66dc`); the e2a published-record correction computed
  both ways and appended to the archive and FINDINGS-3. The published
  verdict is unchanged. H1 unblocked.**
  - **Item 1 — H2 disposition note.** π̂_d both ways with exact intervals:
    all sessions **5/180 = 0.0278, 95% CI [0.0091, 0.0636]**; excluding the
    banner-degenerate sessions **5/168 = 0.0298, 95% CI [0.0097, 0.0681]**.
    **Both upper bounds sit below bar_leak = 0.0735**, so the feasibility
    corollary certifies under either reading. Logged for §3b's eventual
    discussion: 4 of the 5 flips occurred with the **−state** live, and every
    flip sat on a read where the shadow was already near-tied
    (|d_p_a| 0.019–0.081).
  - **Item 2 — audit v2 applied and frozen**
    ([`data/configs/e2b_audit_v2.json`](data/configs/e2b_audit_v2.json),
    sha16 **`7aa235d25eeb66dc`**, printed in the H1 run header). The
    cycle-3/4 fragments are **retained verbatim and extended, never edited**;
    the four approved patterns ride as `junk_regex` with inline `(?im)`
    flags, so `AuditSpec` needs no change and **what runs is exactly what was
    screened** — verified by replaying the frozen artifact through
    `AuditSpec` over the same 2,201-response pool: frozen alone flags 31,
    v2 flags 48, **newly caught = 17**, all attributed to junk patterns
    (14 `banner_terminator`, 3 `bracketless_round_header`). It correctly
    flags reward s1's forced round 2, which is the session the correction is
    about.
  - **Item 3 — the published-record correction, computed before it was
    written.** The published number was **reproduced exactly** from the
    archive first (55/102, Δ = 0.0392, p = 0.244) so the recomputation would
    stand on the same footing; only then was reward s1 removed:
    **54/101, Δ_first = 0.035, one-sided exact binomial p = .275.** The
    session's first free pick was toward the +pole, so removing it lowers Δ
    slightly. **The informative null is unchanged under both computations.**
    The design-authored addendum is appended at the top of
    [`archive/RESULTS-cycles3-4.md`](archive/RESULTS-cycles3-4.md) with the
    slots filled, a one-line dated pointer added to FINDINGS-3's e2a section,
    and **the frozen entries below the addendum are unmodified** — the
    correction sits beside the record, never over it, which is the same
    repair-beside pattern the 2026-08-21 adjudication accepted for
    provenance defects.
  - Suite 135/135. Next: H1, 112 scheduled, stop at read 640, cached round
    path per the gate artifact, audit v2 frozen, checkpoint 1 at 128 paired
    reads.

- 2026-08-21 — **H2 sweep: the PASS-FINAL condition is MET (0 bracketless
  echoes in flip-carrying sessions, all three read clean). But the sweep
  found a larger blind spot than the one it was sent for — a session that is
  70% junk and passed every frozen counter — and the same blind spot is
  present in the PUBLISHED e2a archive, where it let one degenerate forced
  round through into the primary.**
  ([`data/e2b/h2_sweep.json`](data/e2b/h2_sweep.json),
  `scripts/e2b_h2_sweep.py`; raw
  [`2026-08-21_h2_sweep.txt`](results/raw/2026-08-21_h2_sweep.txt).
  LOCK-h v1.3 committed at `a58692f`.)
  - **(a) Full reads of all three flip-carrying sessions (3, 27, 31): CLEAN.**
    Every response on-task, no scaffold echo, no banner terminator, no
    degeneracy. Descriptive: 4 of the 5 flips occurred with the **−state**
    live, and every flip sat on a read where the shadow was already close to
    tied (|d_p_a| 0.019–0.081).
  - **(b) Bracketless-echo scan, all 307 responses: 0 hits in flip-carrying
    sessions.** The adjudication's stated condition is met — **H2 PASS
    FINAL, dose stands** — and π̂_d needs no both-ways report on that
    trigger.
  - **What the sweep found instead, and it is worse than the trigger.** The
    scan flagged **9 responses the frozen audit called clean**, of which
    eight are banner terminators: **session 11 emitted `=== end ===` as
    SEVEN of its ten responses**, plus an emoji cascade that hit the 60-token
    cap — 8 of 10 rounds junk — and it was **not excluded**, because the
    frozen audit's fragments (`Config evaluation session`, `[round`, …) match
    none of them. Session 17 carried two more. Those two sessions contributed
    **12 of the 180 paired reads**.
  - **π̂_d reported both ways anyway, in the spirit of the clause even though
    its trigger did not fire:** all sessions **5/180 = 0.0278**; excluding
    the banner-degenerate sessions **5/168 = 0.0298**. The headline is robust
    — the removed reads carried no flips, so the rate moves *up* slightly and
    stays far below bar_leak.
  - **FLAG — this is a finding about the PUBLISHED RECORD, not only about
    H2.** Running the same scan over the 1,894 archived e2a responses finds
    **8 that the frozen audit missed**, including `=== end of session ===`,
    `=== end of sun session ===`, `=== END OF CONFIGURATION EVALUATION
    SESSION ===` (uppercase — the frozen fragments are **case-sensitive**),
    and `Round 4 — active config: maple` (capital R, so `[round` never
    matched). **Three fall in FORCED rounds**, where the v3 rule excludes the
    session. Two of those three were excluded anyway by the lexical rule.
    **The third was not: `reward` session 1, forced round 2,
    `=== end of session ===`, `excluded=False`.** Under the v3 rule as
    written it should have been excluded, and it instead contributed to the
    published cycle-3/4 primary — 1 of the 102 valid marker sessions. e2a was
    an informative null and one session cannot flip that, but the record
    should say so rather than not.
  - **Item 2 — proposed revised fragment set, screened for overbreadth,
    NOT applied.** Four patterns, case-insensitive:

    | pattern | regex |
    |---|---|
    | `banner_terminator` | `^\s*={2,}[^\n]*={2,}\s*$` |
    | `bracketless_round_header` | `\bround\s+\d+\s*[\|—–-]\s*\w` |
    | `config_role_phrase` | `\b(?:active\|running)\s+config\b\|\bconfig\s+in\s+use\b` |
    | `config_then_close_bracket` | `\bconfig\b[^\n]{0,40}\]` |

    **Screen: 3/3 known targets caught; 17 hits on the 2,170-response
    known-clean reference set (1,894 e2a + 307 H2, minus everything the
    frozen audit already flags) — and on inspection every one of the 17 is a
    TRUE degeneracy, so the false-positive count is ZERO.** That is the
    adjudication's bar met, with the caveat that it was met by the screen
    *reclassifying* its own reference set: the "known-clean" pool was not
    clean, which is the finding above. Awaiting design-instance approval;
    frozen counters untouched, nothing applied.
  - **Sequencing flag — H1 is HELD, deliberately.** Item 4 says H1 runs, and
    item 2 says the revised audit is "for H1 … frozen for the H1 campaign".
    Launching H1 now would spend 112 sessions under the monitor the revision
    exists to replace — the one just shown to miss a session that was 70%
    junk. H1 is ready and budgeted (~2.8 h cached); it waits on the audit
    approval rather than racing it. Say the word either way.
  - **LOCK-h v1.3 applied verbatim and verified** (`a58692f`): §3 stop
    corollary, §3b registered secondary, §8 amendment line. §6 re-run
    returns **byte-identical GREEN**; suite 135/135. §3b is the right home
    for the two permutation tests — registered before H1 data and explicitly
    never gate-relevant, which is the correct standing for a statistic that
    was suggestive on five events.

- 2026-08-21 — **H2 PROPER, run of record: 32 sessions in 44.7 min.
  π̂_d = 0.0278 with the state live through rounds, CI upper bound still
  below bar_leak; ICĈ = 0.1443, which is non-zero for the first time and
  still comfortably inside the ceiling — because at this π̂_d the ceiling is
  1.00. Degeneracy 2/307, below e2a's own base rate. Window clean.**
  ([`data/e2b/h2_sessions.json`](data/e2b/h2_sessions.json); raw
  [`2026-08-21_h2_sessions.txt`](results/raw/2026-08-21_h2_sessions.txt).
  LOCK-h v1.2 §3a; L48 frac 0.10, |α| = 10.3010; round path CACHED by the
  g1 artifact, choice forwards uncached.)
  - **What ran.** 32 sessions = 2 full blocks × 16 strata, 8 per roster
    pair, 6 reads each. 2 sessions excluded → **180 paired reads** of the
    scheduled 192, exactly the 12 the exclusions cost. 2,682 s against a
    ~50 min budget.
  - **The two numbers, now measured under the condition that matters:**

    | | read half (state-free prefixes) | **H2 proper (state through rounds)** |
    |---|---|---|
    | π̂_d | 6/288 = 0.0208, CI [0.0077, 0.0448] | **5/180 = 0.0278, CI [0.0091, 0.0636]** |
    | ICĈ | 0.0000 (6 flips, 6 sessions) | **0.1443 (5 flips, 3 sessions)** |
    | state-reversing half-gap | +0.00084 = 1.14% of bar | **+0.00220 = 3.0% of bar** |

    π̂_d rises slightly with the state live through generation, as expected,
    and **its 95% upper bound (0.0636) still sits below bar_leak = 0.0735** —
    so the feasibility corollary continues to certify without any directional
    test. The margin is thinner than the read half's, though, and that is
    worth carrying: 0.0636 is not far from 0.0735.
  - **CHECKPOINT-1 EVALUATION (LOCK-h §3): WITHIN, no pause — and by a wide
    margin for a structural reason.** The §6(b) certified max-ICC ceiling at
    π̂_d = 0.0278 is **1.00**: pass-when-clean stays ≥ 0.9988 even at ICC = 1,
    because at a discordance this far below the bar the certification is
    carried by the feasibility corollary regardless of how the flips cluster.
    **The ICC ceiling only bites at higher π_d, where the directional test is
    the thing doing the work.** So ICĈ = 0.1443 does not approach a pause
    here — but it would matter a great deal if H1's realised π̂_d landed
    nearer 0.08+.
  - **FLAGGED, post-hoc, and labelled as such (rule 11): the clustering is
    nominally unusual and rests on five events.** The 5 flips fall in 3
    sessions, two of them carrying 2. Against a null that places the same 5
    flips uniformly over the same 180 reads (200,000 draws):
    P(ICC ≥ 0.1443) = **0.017**, and P(≥ 2 sessions each carrying ≥ 2 flips)
    = **0.0115**. That is suggestive, and it is **post-hoc** — no ICC test
    was pre-registered; the registered use of ICĈ is the ceiling comparison
    above. It licenses a pre-registration, never a verdict. The read half's
    ICĈ = 0 sits within the same null, so the two runs do not conflict; what
    differs is the condition that could plausibly *cause* clustering — the
    session's own state trajectory — which is exactly the thing H2 added.
    **Recommended, not taken:** if H1 is expected anywhere near π_d 0.08,
    pre-register this ICC test before H1 opens rather than after.
  - **Monitors, all within tolerance.** Degeneracy **2/307 = 0.0065** against
    the declared p0 = 0.05, one-sided exact binomial **p = 1.0000** —
    WITHIN, and *below* e2a's own archive base rate of 0.0153. Cap hits
    2/307. Exclusions **2/32 = 6.3%** against e2a's 16/200 = 8.0%. Window
    contract clean: declared 8192, `n_encodes_clipped` = **0**.
  - **FLAG — substantive, apparatus, and deliberately NOT fixed: the frozen
    audit has a bracket-anchored blind spot.** Session 23's round 4
    degenerated into a scaffold echo — *"Could you please lend me a soften
    the tone of this notice: The meeting has been moved to round 1 — config
    in use: ridge]"* — which any reader calls degenerate on sight. The
    frozen audit did **not** fire, because its fragment is `"[round"` with
    the opening bracket and the echo omitted it. The session was excluded
    anyway, but only because the echo happened to contain its **own tag**
    and tripped the lexical rule instead. **Had the echo named the other
    pair's tag, or no tag, it would have passed both counters.** Frozen
    means frozen and no post-data addition was made (that is the audit's own
    rule, and ledger 28(b)'s precedence held correctly here — audit
    evaluated first, then lexical). Raised for the design instance.
  - **Rule 25 honoured, not gestured at:** both smoke transcripts and both
    excluded-session transcripts read in full. Session 24's exclusion is a
    clean banner echo (`=== Config evaluation session ===`, 6 tokens) at
    forced round 2, correctly excluding before the first free choice; the
    identical echo at session 17's *free* round 5 correctly did **not**
    exclude, per the v3 rule that post-first-choice degeneracy never touches
    the primary.
  - **Still no preference DV.** `summarize()` has no branch that computes
    Δ_first, and none was computed. H1 has not run.
  - **H2 PASS/FAIL is a design-instance disposition on these numbers.** Code
    delivers them and stops.

- 2026-08-21 — **H2 proper runner built and smoked. Budget: ~50 min for the
  32 sessions on the gate-licensed cached round path (~1.4 h at the throttled
  convention). The two kernel paths produced BIT-IDENTICAL transcripts, which
  is a stronger statement than the gate that licensed one of them.**
  (`scripts/e2b_h2_sessions.py`; raw
  [`2026-08-21_h2_smoke_cached.txt`](results/raw/2026-08-21_h2_smoke_cached.txt),
  [`_uncached`](results/raw/2026-08-21_h2_smoke_uncached.txt). **Not the run
  of record — 2 sessions, smoke only.**)
  - **Measured budget, both paths, 2 sessions each:**

    | round path | s/session | 32 sessions | at the throttled convention |
    |---|---|---|---|
    | cached (g1-licensed) | **93** | **~50 min** | **~1.4 h** |
    | uncached | 395 | ~3.5 h | ~6.0 h |

  - **The cached path is not a shortcut — running uncached would have been
    the deviation.** e2a set `use_cached_rounds` mechanically from the gate
    artifact (`g1["results"][str(frac)]["pass"]`) and **ran its rounds
    cached** at frac 0.10 under g1r (PASS, max KL 7.11e-4 < 1e-3). H2 must be
    comparable to those sessions and changes no gate-relevant dimension —
    same model, backend, axis family, dose, and now a template geometry
    *proven byte-identical* by the Route 3 replay. So the runner reads the
    decision from the artifact rather than taking a flag, exactly as e2a
    did, and prints the gate row and its provenance at startup. **Choice
    forwards stay state-free uncached regardless** (g3′ clause 1):
    `choice_read_statepresent` goes through `adapter.forward`, which has no
    cached path at all.
  - **An unexpectedly strong check fell out of doing both.** The two smokes
    share every seed and differ only in the kernel path, so they are a
    session-level kernel gate. Result: **transcripts identical 2/2, choice
    picks identical 12/12, byte for byte.** The g1 gate bounded the paths'
    disagreement at KL 7.1e-4 on probes; over two complete 10-round sessions
    at this dose the disagreement is **exactly zero**.
  - **Smoke health (rule 25 — both transcripts read in full, not skimmed):**
    20/20 rounds `degen=None`, `lexical=None`, `cap_hit=False`; 0 sessions
    excluded; window clean (`n_encodes_clipped = 0`); responses on-task with
    no scaffold leakage and no tag mentions.
  - **The state schedule verified against the record it writes.** Session 1
    (forced_end `neg`): live states at the six reads ran
    neg→pos→neg→pos→pos→neg, each equal to the pole the *previous* pick
    delivered, with the first sitting on the forced-phase end state — which
    is what the third stratum dimension exists to counterbalance. Session 2
    (forced_end `pos`) likewise. The session-keyed template rotation is
    visible live too: session 0 opens on `ROUND_TEMPLATES[0]`, session 1 on
    `[1]`.
  - **Declared at invocation, because the lock does not fix it.** Degeneracy
    binds by one-sided exact binomial against **p0 = 0.05**, printed before
    any scoring. The anchor is the e2a archive's own measured base rate,
    **29/1894 = 0.0153** over 200 sessions of the same template family, so
    the declared bar sits ~3× above it (rule 21). Flagged for the design
    instance, whose disposition H2's PASS/FAIL is regardless.
  - **`data/configs/e2a_ban_list.json` pulled into the repo.** The frozen
    12-id scaffold ban list lived only in the clone; H2 depends on it, and
    an input that lives only in the clone makes the run unreproducible on
    any other machine (handoff trap 9's lesson, same fix as the oracle-tier
    inputs).
  - **No preference DV, enforced in code rather than promised in prose.**
    `summarize()` has no branch that computes Δ_first. Picks are recorded
    because a flip *is* a disagreement between picks, but H1 has not run and
    a counterbalanced preference number computed here would be verdict data
    collected before its own leakage gate.
  - Awaiting the go for the 32-session run of record.

- 2026-08-21 — **LOCK-h v1.2 applied verbatim: §3a session plan (112
  stop-governed sessions for H1, 32 for H2 proper). Operationalization
  only — §6 re-run returns byte-identical outputs and GREEN. Every
  arithmetic claim in §3a independently checked and exact.**
  - **Applied as authored.** §3a inserted after §3, the amendment line
    appended to §8. Two edits were *not* dictated and are flagged: the
    title and status line move v1.1 → v1.2 and now read **BINDING**
    (v1.1 passed §6 and was committed at `8a97513`; the old status still
    said "becomes binding when Jason commits it"), and the block's
    paste-indentation was stripped so the heading sits at column 0 like
    every other heading in the file. Content verbatim; say the word if
    either should read differently.
  - **The "no OC changes" claim, verified rather than accepted.** §6 re-run
    after the edit: outputs **identical on every key**, VERDICT GREEN,
    n_d* 200 / N_max 640 / bar 0.0735 / c_leak 0.1470 unchanged. Suite
    135/135.
  - **§3a's arithmetic checks out exactly, including the one number that
    could have been loose.** 16 strata = 4 × 2 × 2 ✓. 7 × 16 = 112 ✓. 112 ×
    m=6 = 672 paired reads against N_max = 640 — **32 reads of slack, 5.33
    sessions** ✓. And read 640 lands at **session 107, read 4** — exactly
    the stop §3a names, not approximately ✓. H2: 2 × 16 = 32, 8 per roster
    pair, 32 × 6 = **192** paired reads ✓.
  - **One structural consequence worth recording, because it makes the
    "expected stop" stronger than "expected".** The n_d* exit can only fire
    first if π_d ≥ n_d*/N_max = **0.3125**. §3's apparatus-stability ceiling
    pauses the run at π̂_d > 0.30. So **N_max binds across the entire
    licensed π_d range** — the read-4-of-session-107 stop is not a
    typical case, it is the only reachable one short of a pause. The
    read-half precursor (π̂_d = 0.0208) sits far below that, projecting
    ~13 discordant pairs at the stop.

- 2026-08-21 — **Route 3 acceptance MET on the first attempt: the
  reimplemented e2a session template rebuilds all 200 archived scaffoldings
  byte-for-byte, and all 200 RNG seed streams match. Committed as a suite
  check; suite 130 → 135. LOCK-h v1.1 is committed at `8a97513`.**
  (`valence_core/e2b/session.py`;
  `check_e2a_session_reconstruction()` in the ledger-26 suite.)
  - **Item 1 — the lock's timestamp is `8a97513`.** LOCK-h.md was committed
    on Jason's word at the close of the previous exchange, after §6 returned
    GREEN at `13b7c21`. Recorded here as the dated entry the adjudication
    asks for: **that hash is the lock's timestamp**, and every H-tier item
    below runs under it.
  - **Item 2 — read half accepted as scoped.** Read-time-only, never H1's
    planning π_d. The **low-discordance-pass reporting rule is ratified**:
    when H1 exits with π̂_d < bar, the PASS is reported as certification by
    low discordance, not as a powered directional test. The repair-beside
    pattern is accepted as the pattern for provenance defects — repair
    alongside, never over, what a run wrote.
  - **Item 3 — the fork is closed, and the rotation was deterministic after
    all.** The original runner seeds one generator per session,
    `default_rng(crc32(f"{arm}|{s}") % 2**31)`, and draws everything from it
    in a fixed order. **Both `arm` and `session` are recorded**, so the whole
    stream is replayable from `data/e2a/sessions.jsonl` — task permutation,
    paraphrase index per round, menu order, and every generation seed. The
    scaffolding was never unrecoverable; it was only unwritten-down. The
    declared-seeded-rotation contingency is **not needed and not activated**.
  - **The acceptance result:**

    | check | result |
    |---|---|
    | archived scaffoldings rebuilt byte-for-byte | **200/200** |
    | RNG seed streams in step (recorded `seed` values) | **200/200** |
    | template index keyed on SESSION, not round | confirmed |
    | coincidence guard is discriminating | confirmed |

    The **seed-stream match is the load-bearing one.** Matching text could in
    principle be coincidence; a replay that is off by even one draw cannot
    land on 200 recorded generation seeds. The walk is positional, not a
    substring search — every harness-written byte must sit at exactly the
    offset the replay puts it at, and the walk must consume the transcript
    exactly.
  - **A trap the archive-wide check caught and a spot check would not.** The
    template index is `ROUND_TEMPLATES[(s + ri) % 4]` — keyed on the
    **session**, not the round. Reading a single transcript suggests
    `(round − 1) % 4`, which is *the same thing at session 0* and wrong
    everywhere else. The suite now carries an explicit coincidence guard: it
    picks a session where the two rules genuinely disagree, asserts the
    archive follows the session-keyed one, **and asserts that the two rules
    really do differ there** — a guard that cannot silently become vacuous.
  - **The acceptance test was mutation-tested, and one of my own claims did
    not survive it.** Pinning the paraphrase index to 0 → **0/200**.
    Reversing `ROUND_TEMPLATES` → **0/200**. Drawing the paraphrase *inside*
    the round loop, interleaved with the seed draws → **4/200**. But the
    mutation I had asserted in the module docstring would desynchronise the
    stream — pulling the permutation first and the paraphrase draws in a
    second loop — **rebuilds 200/200**, because both forms draw the same
    count in the same order. The claim was wrong and is corrected in the
    code: what matters is that every paraphrase draw falls after the
    permutation and **before any generation-seed draw**; how they are
    written is immaterial.
  - **Placement, and why it does not trigger rule 26.** The module is
    `valence_core/e2b/session.py` — inside the e2b harness and the
    quarantine boundary, which is how the adjudication's "NOT valence_core"
    reads against a package whose e2b subtree *is* the harness. Nothing in
    the general core imports it, so no published path changes and the
    refactor law is not engaged. Per the adjudication, this module and the
    four-copy `_new_qwen_adapter` debt are absorbed by **one** consolidation
    event after H1.
  - Suite **135/135** (was 130; the five new checks are the acceptance).
    Next: H2 proper — state live through rounds AND reads, all four roster
    pairs, degeneracy monitors, dose L48 frac 0.10.

- 2026-08-21 — **H2 precursor (read half): a live state at the choice
  position barely moves this instrument. π̂_d = 0.0208, and its 95% upper
  bound is already below bar_leak — so on archived prefixes the feasibility
  corollary alone certifies the leak, with no directional test. ICĈ = 0.
  Window contract clean. The generation half is BLOCKED on a design-instance
  fork.**
  ([`data/e2b/h2_read_stability.json`](data/e2b/h2_read_stability.json); raw
  [`2026-08-21_h2_read_stability.txt`](results/raw/2026-08-21_h2_read_stability.txt);
  `scripts/e2b_h2_readstability.py`. 288 paired reads — 144 +state / 144
  −state — over 48 archived prism/slate sessions, L48 frac 0.10,
  |α| = 10.3010, axis `span_reward`.)
  - **THIS IS HALF OF H2 AND IS NAMED THAT WAY.** PROPOSAL-h §2 wants
    stability with the state live through **rounds AND reads**. These
    prefixes were generated by e2a with **no state live at any point**, so
    every number here is a **read-time-only** perturbation estimate. It is
    an instrument characterisation and must never be used as H1's planning
    value for π_d.
  - **The blocker, stated plainly because it needs a decision and is not
    Code's to make.** The e2a session runner — templates, round mechanics,
    stop discipline, ban list, cap logic — lives **only in the gitignored
    clone** (`jlens_qwen/e2a.py`, `scripts/e2a_sessions.py`).
    `valence_core/` carries the monitors, counters, records and the
    quarantined primitive, but not the round construction. Three routes,
    with the objection to each:
    1. **Port into `valence_core/`** — correct long-term, but a rule-26
       acceptance event, and LOCK-h §7 queues a *far smaller* consolidation
       until after H1 precisely to avoid triggering one mid-H-cal.
    2. **Import the clone module directly** — zero divergence from e2a, but
       it is built on the clone's own model wrapper, so state-present reads
       could not go through `e2b.statepresent`. That breaks the rule 5(e)
       quarantine. Dead end.
    3. **Reimplement against `ModelAdapter`, verified byte-for-byte against
       the archive** — a new module, no existing path touched, and the 200
       committed transcripts *pin* the template instead of the
       reimplementation having to be trusted. **Recommended**, with
       supporting evidence: the prefix extractor written for this run
       reproduces the recorded choice count on **200/200** archived
       sessions, so the scaffolding is demonstrably recoverable. The one
       open question is whether the round/menu template rotation is
       deterministic from recorded fields — if a rule reproduces all 200
       transcripts, that is a rule-26-grade acceptance in miniature.
  - **The two numbers LOCK-h §3 checkpoint 1 is defined to report, which
    nobody had until now:**
    - **π̂_d = 0.0208** — 6 flips in 288 paired reads; exact 95% CI
      **[0.0077, 0.0448]**. The **upper** bound sits below
      bar_leak = 0.0735. §3's feasibility corollary says |L| ≤ π_d, so at
      this discordance a bar-sized leak **cannot exist**, and the
      certification needs no directional test at all.
    - **ICĈ = 0.0000**, and the reason is visible in the raw counts: the 6
      flips fall in **6 distinct sessions, one each** — maximally
      unclustered. **This does NOT yet vindicate the m = 6 pooling ruling.**
      Six events carry almost no power to distinguish ICC 0 from moderate
      clustering; the estimate is *consistent* with the ruling, not
      evidence for it. The real test is H2 proper, where a state live
      through the rounds may raise π_d enough for the ICC to be estimable.
  - **What H1 would do in this regime, computed rather than assumed.** At
    π_d ≈ 0.021, reaching n_d* = 200 discordant pairs needs ~**9,600**
    paired reads against N_max = 640; the run would always exit at N_max
    having harvested ~13. π̂_d at that stop is < bar, so the mapped CI lies
    inside [−π̂_d, +π̂_d] and the gate returns **automatic PASS** — which
    §6(a) already certified at 1.000 for the π_d = 0.02 cell, so it is a
    verified-clean outcome and not an accident. **Flagged so a later reader
    does not misread it:** in this regime H1 passes by *low discordance*,
    not by a powered directional test. §3 licenses exactly that ("low
    discordance is evidence, not absence") — but the PASS should be
    reported as what it is.
  - **In-vivo leak (PROPOSAL-h §0.2 (i)), the first such measurement:**
    mean Δp_a = +0.00002 on +state, −0.00166 on −state. Decomposed:
    **state-reversing half-gap = +0.00084** — the component a
    counterbalance *cannot* absorb, and it is **1.14% of bar_leak** — with
    common mode −0.00082, the component it can. Mean |Δ label_mass| =
    0.019.
  - **The state does not degrade the read.** label_mass 0.7025 state-present
    vs 0.7049 shadow; top1_is_label 0.7917 vs 0.7951. Horn (a)'s first
    failure mode — probability pushed off the menu entirely — is not
    happening at this dose.
  - **Window contract: CLEAN.** Declared window 8192, `n_encodes_clipped`
    = **0** across all 576 forwards on full-length session transcripts.
  - **Flip rate is not arm-specific:** reward 4/168, sham 1/54, random2
    1/30, random1 0/36. Whatever the live state does at a read, it does not
    depend on which arm produced the prefix.
  - **COVERAGE LIMIT, real and unfixable by this route.** Of the roster of
    record, only **prism/slate** appears in the archive. granite/plaza,
    velvet/walnut and ridge/saddle have no archived prefixes and are
    unreachable here **at any n** — they need H2 proper.
  - **Provenance defect found and repaired.** e2a's `session` counter
    **restarts per arm**, so it is not unique — the 50 prism/slate records
    carry only 28 distinct ids, and grouping by it would silently merge four
    sessions into one. The ICC was never exposed to this (the run grouped
    over session *records*), but the artifact's `session_id` field was.
    `session_key = arm:session` is added — 48 distinct, matching the 48
    sessions used — with `session_id` left exactly as the run wrote it, and
    the script fixed for future runs. No number changes, and the reads are
    deterministic and uncached, so a re-run would reproduce these values
    identically.
  - Instrument characterisation only. H2 PASS/FAIL is the design instance's,
    and the generation half is not in this artifact.

- 2026-08-20 — **LOCK-h v1.1 §6 re-verification: GREEN. (a) 8/8, (c) 4/4
  feasible cells at min 0.937, and the bound-in ICC ceiling table reproduces
  6/6 exactly. Every number v1.1 predicted for itself is the number the
  exact machinery returns.**
  ([`data/e2b/lockh_verify_v11.json`](data/e2b/lockh_verify_v11.json); raw
  [`2026-08-20_lockh_verify_v11.txt`](results/raw/2026-08-20_lockh_verify_v11.txt).
  **`LOCK-h.md` is still uncommitted** — §6 says Jason commits on green and
  the commit hash is the lock's timestamp, so that act is his.)

  | π_d | (a) PASS @ L=0 | IND | (b) clustered | (c) FAIL @ 2×bar | FAIL @ bar | not-PASS @ bar |
  |---|---|---|---|---|---|---|
  | 0.02 | 1.000 | 0.000 | 1.000 | — | — | — |
  | 0.05 | 1.000 | 0.000 | 0.967 | — | — | — |
  | 0.08 | 1.000 | 0.000 | 0.756 | — | 0.098 | 0.671 |
  | 0.10 | 1.000 | 0.000 | 0.527 | — | 0.052 | 0.892 |
  | 0.15 | 0.996 | 0.004 | 0.107 | 1.000 | 0.030 | 0.962 |
  | 0.20 | 0.972 | 0.028 | 0.010 | 0.996 | 0.025 | 0.972 |
  | 0.25 | **0.918** | 0.082 | 0.000 | 0.975 | 0.024 | 0.975 |
  | 0.30 | **0.834** | 0.166 | 0.000 | **0.937** | 0.023 | 0.976 |

  - **(a) GATE MET, 8/8.** 0.918 at π_d = 0.25 and 0.834 at 0.30, exactly
    the values §6(a) states for itself. `n_d*` 124 → 200 with `N_max` and
    the session count untouched.
  - **(c) GATE MET, 4/4 feasible cells, min 0.937** at π_d = 0.30 — again
    exactly the value §6(c) states. **Feasibility, stated so the excluded
    cells are not misread:** L = 2 × bar = 0.1470 requires π_d ≥ 0.1470, so
    π_d ∈ {0.02, 0.05, 0.08, 0.10} carry no leak of that size at all and are
    **excluded, not failed**.
  - **(b) ICC ceiling table ASSERTED, 6/6 exact match** against the values
    §6(b) binds in — 0.75 / 0.50 / 0.20 / 0.10 / 0.05 / 0.00 at π_d
    0.08 / 0.10 / 0.15 / 0.20 / 0.25 / 0.30. The lock's stated exposure is
    the exposure the machinery computes. (The tolerance search was also
    made monotone-safe in this pass: it now stops at the first failing rung
    rather than reporting the largest passing one, so a non-monotone grid
    could not overstate a ceiling.)
  - **What the low-π_d corner actually does, recorded because it reads as a
    gap and is not one.** At π_d = 0.08 the largest leak that can physically
    exist is 0.08 = 1.09 × bar, so the 2 × bar detection guarantee is
    vacuous there by construction. For a bar-level leak in that corner the
    outcome splits **PASS 0.329 / EXTEND 0.573 / FAIL 0.098** — i.e. the
    modal response is the §3 extension clause, which is precisely what it
    exists for, and bar-level risk is carried by §2's ≤ 2.5% false-verdict
    guarantee as §6(c) says. The gate is not blind there; it is
    appropriately undecided.
  - **The rewrite was regression-checked, not trusted.** `main()` was
    rewritten for the v1.1 gate semantics, so the v1.0 configuration was
    re-run through the new path (`--n-d 124 --c-leak-multiple 1.0`) and
    compared cell-by-cell against the committed v1.0 artifact: **32/32
    cells IDENTICAL** to 1e-12. The gate definitions changed; the
    computation did not. Both lock versions remain reproducible from one
    script, which is the point of keeping the flags.
  - **Worth stating once, because it is the §6 structure justifying
    itself.** v1.0's two specification errors were found by v1.0's own
    verification section on its first use, and v1.1 fixed both without
    spending a session: one was free (an early-exit that discarded
    already-budgeted reads) and one was conceptual (80% power demanded at
    the boundary of the tested hypothesis, where power equals size). A
    verification clause that gates its own lock is worth the clause.
  - **VERDICT: GREEN. LOCK-h v1.1 verified, ready to commit.** On commit:
    H2 (dose stability, L48 frac 0.10, state live through reads) → on PASS,
    H1 opens under §3 including the checkpoint-1 calibration look, which
    reports (π̂_d, ICĈ) regardless of outcome.

- 2026-08-20 — **LOCK-h §6 verification: NOT GREEN. Two cells short, for
  entirely different reasons — (a) is short by a sample size and the fix is
  free; (c) cannot be satisfied at any sample size, because it asks for 80%
  power at the one point where the test is defined to have 2.5%.**
  ([`data/e2b/lockh_verify.json`](data/e2b/lockh_verify.json),
  [`lockh_verify_nd200.json`](data/e2b/lockh_verify_nd200.json); raw
  [`2026-08-20_lockh_verify.txt`](results/raw/2026-08-20_lockh_verify.txt),
  [`_nd200`](results/raw/2026-08-20_lockh_verify_nd200.txt);
  `scripts/lockh_verify.py`. **LOCK-h.md is NOT committed** — §6 gates it and
  §6 did not pass.)
  - **Exact, and cross-checked against an independent Monte Carlo.** Every
    distribution in the §3 plan is discrete and finite, so the whole
    operating characteristic is a finite sum: the stopping law (negative
    binomial for the n_d exit, binomial for the N_max exit) factorises from
    the split, because the rule reads only the totals — which is the same
    property that makes §3's conditional test exact under inverse sampling.
    Enumeration vs 40k-trial MC agreed within ~1 MC SE on all four spot
    cells (e.g. π_d = 0.30, L = 0: 0.5193 exact vs 0.5211 MC). Rule 10 says
    an under-sampled null flatters a weak signal; a gate's own certification
    is the last place to accept sampling error.

  | π_d | (a) PASS @ L=0 | IND | (b) clustered floor | (c) FAIL @ bar | not-PASS @ bar |
  |---|---|---|---|---|---|
  | 0.02 | 1.000 | 0.000 | 1.000 | — (π_d < bar) | — |
  | 0.05 | 1.000 | 0.000 | 0.967 | — (π_d < bar) | — |
  | 0.08 | 1.000 | 0.000 | 0.756 | 0.098 | 0.671 |
  | 0.10 | 1.000 | 0.000 | 0.527 | 0.052 | 0.892 |
  | 0.15 | 0.996 | 0.004 | 0.107 | 0.030 | 0.962 |
  | 0.20 | 0.957 | 0.043 | 0.010 | 0.026 | 0.972 |
  | 0.25 | **0.787** | 0.213 | 0.000 | 0.023 | 0.976 |
  | 0.30 | **0.519** | 0.481 | 0.000 | 0.022 | 0.978 |

  - **(a) — 6/8 clear; short at π_d = 0.25 and 0.30. The fix costs nothing.**
    **`n_d*` 124 → 200, `N_max` unchanged at 640** ⇒ **8/8 clear** (0.918 at
    π_d = 0.25, 0.834 at 0.30), still ~107 sessions. The mechanism is worth
    stating because it is counter-intuitive: at high π_d the n_d = 124 exit
    fires *early and throws reads away*. Raising `n_d*` makes the N_max exit
    the binding one there, so the run harvests ~160 discordant pairs instead
    of stopping at 124 — the sessions were already budgeted. Confirmed by
    saturation: every `n_d*` ≥ 200 against N_max = 640 returns the same
    0.918 / 0.839. Full trade surface in the artifact.
  - **(c) — 0/6 clear, and NO adjustment of `n_d*`/`N_max` can fix it. This
    is a category error in the requirement, not a shortfall.** A true leak
    sitting exactly ON the bar is the **boundary of the hypothesis the gate
    tests**, and at its own boundary an interval test has power equal to its
    **size**. The CI half-width and the sampling SD both shrink like
    1/√n_d, so their ratio is frozen at the critical value and P(FAIL) is
    **pinned at α/2 = 0.025 for every n_d** — demonstrated flat from n_d =
    124 to n_d = 2000 with π̂_d held fixed: 0.025, 0.024, 0.024, 0.025,
    0.023. §6(c) asks for 80% power at the one point where the test is
    defined to have 2.5%.
    - **Two reachable restatements, with numbers.** (i) **P(FAIL) ≥ 0.80 at
      L = 2 × bar = 0.1470** — min over feasible π_d = **0.805** at the
      locked `n_d*` = 124, and **0.937** under the (a) fix. Clears with
      margin. (ii) **P(not PASS) ≥ 0.80 at L = bar** — min 0.671, clearing
      for π_d ≥ 0.10 (0.892 and up) but failing at π_d = 0.08. The
      intermediate rung does not work: 1.5 × bar gives only 0.393 even at
      `n_d*` = 200, so 2 × bar is the first clean one.
  - **(b) — reported not gated, and it is the plan's real exposure.** The
    clustered floor collapses: 0.756 at π_d = 0.08, 0.527 at 0.10, 0.107 at
    0.15, ~0 at 0.20 and above. **The whole plan rests on the m = 6 pooling
    ruling**, and §3's argument for it is sound as far as it goes (H1 states
    are scheduled, nothing is selected, so reads are exchangeable *as leak
    measurements*) — but the arithmetic shows how much weight it carries.
    Supplementary, to make the bound actionable: **max ICC the plan still
    certifies under** = 0.75 (π_d 0.08), 0.50 (0.10), 0.20 (0.15), 0.10
    (0.20), 0.05 (0.25, under the (a) fix), **0.00 (0.30)**. At the top of
    the π_d range the plan needs *near-zero* within-session correlation.
  - **Two §6 ambiguities, both resolved by computing both branches rather
    than picking one.** §6(b)'s "first-reads-only floor (m = 1, 640 sessions
    equivalent)" read literally is **identical to (a)** under ICC 0 and is
    therefore not a bound of any kind; the bound reported as (b) is the
    fully-clustered one, N_max/m = 106 paired reads. And §3's FAIL is
    implemented as written — mapped CI strictly beyond the bar, with
    everything else INDETERMINATE per "CI straddles the bar → extend once."
    Both readings are recorded in the artifact under
    `ambiguities_resolved`.
  - **One property the gate has for free, noted because it looks like a
    loophole and is not.** The mapped CI always lies inside [−π̂_d, +π̂_d],
    so any stop with π̂_d < bar passes automatically. That is §3's own
    feasibility corollary doing its work — a leak cannot exceed the
    discordance carrying it — and it is why the low-π_d cells sit at 1.000.
  - Code verifies; the §6 adjustment and the commit are the design
    instance's and Jason's. Re-verification is one command.

- 2026-08-20 — **Adjudication 2026-08-21 (partial) applied: roster of record
  locked to the continuity four, scaffold declared the format of record, and
  the determinism certification promoted to APPARATUS RESULT D-1.**
  - **Item 1 — H3b ACCEPTED, roster of record locked.** `granite/plaza`,
    `prism/slate`, `velvet/walnut`, `ridge/saddle` — carried in
    [`data/e2b/h3b_repair_screen.json`](data/e2b/h3b_repair_screen.json)
    under `adjudication_2026-08-21.roster_of_record`, beside the run's own
    `recommended_roster`, which is left exactly as written (asserted
    unchanged). Declared **"an admissible four", never "the best four"** —
    the design instance took the wording from the screen's own residual
    measurement rather than from the rank order, which is the correct
    reading and the one the entry argued for.
  - **The format question is CLOSED, and it closes in the direction that
    keeps the incumbent.** Scaffold is the **format of record**;
    **bare-format balance is not a criterion for e2b**. The format-robust
    alternative (`canvas/maple` in place of `prism/slate`) is recorded and
    **not taken**. C1 therefore stays in the roster and continuity with
    every published cycle-3/4 preference number is preserved. The open flag
    raised in the H3 entry is marked RESOLVED there.
  - **Item 2 — APPARATUS RESULT D-1: screen determinism certified.** The
    5/5 bit-identical same-order repeats are promoted from a
    reproducibility check inside H3b to a standing apparatus result. Its
    scope, stated so it is not over-claimed later: it certifies that the
    MLX apparatus, the probe construction and the restricted-choice readout
    are **jointly bit-reproducible across processes and across hours** on
    this machine. It says nothing about numerical agreement on any other
    backend, which remains rule 2's business per site.
  - **Item 3 — flip-gate conceptual core ACCEPTED** (b = c null;
    directional-only leak). The n_d table and the π_d-free gate form did
    not reach the design instance — a bridge outage, not a gap in the
    record: both have been committed since `7302384`, in the flip-gate
    entry and in
    [`data/e2b/h1_power.json`](data/e2b/h1_power.json) → `lockh_v1.flip_gate`.
    Nothing new was computed; the material was re-rendered verbatim in the
    reply for hand-carriage. **LOCK-h v1 follows receipt.**

- 2026-08-20 — **H3b, the re-pairing screen: a roster exists. 46/120
  pairings clear the band, best disjoint matching = 4 at imbalance
  0.001–0.007. The tags were never the problem — the arbitrary grouping
  was, and iteration 1 was not unlucky, it was under-sampled.**
  ([`data/e2b/h3b_repair_screen.json`](data/e2b/h3b_repair_screen.json);
  raw [`2026-08-20_h3b_repair_screen.txt`](results/raw/2026-08-20_h3b_repair_screen.txt);
  all C(16,2) = 120 pairings, n = 16/pair/format as iteration 1, 1,729 s)
  - **No new stimulus, and none needed.** The 8 pairs are built from 16
    tags; the pairing is an arbitrary grouping, not a property of a tag. All
    16 are already single-token on this tokenizer (re-asserted at startup)
    and already carry the committed roster's rule-18 and ledger-28c
    verification, so hygiene status is **inherited** rather than re-earned.
    Only the pairing is new.
  - **Iteration 1 was not unlucky.** 3/8 = 37.5% of the original groupings
    cleared; 46/120 = **38.3%** of all groupings clear. The base rate is the
    same to within a rounding error. Nothing was wrong with iteration 1's
    tags or its luck — eight arbitrary groupings is simply too small a
    sample of the 120 available to contain four good disjoint ones. **The
    fix for "fewer than 4 clear" was more pairings from the same tags, not
    better tags.**
  - **Disjointness is enforced by exact matching, not greedily.** Four pairs
    need eight distinct tags. Over re-pairings the most balanced pairs
    happily share tags, so greedy selection can take the best pair first and
    strand the field; the script searches disjoint 4-subsets exactly and
    reports the largest reachable matching if four is unreachable. It was
    reachable.
  - **Recommended roster (scaffold primary, the committed band):**

    | pair | was | scaffold identity | imb | bare identity | position | label_mass (min) |
    |---|---|---|---|---|---|---|
    | granite/plaza | — | 0.499 | 0.001 | 0.419 | 0.516 | 0.235 (0.158) |
    | prism/slate | **C1** | 0.502 | 0.002 | 0.696 | 0.586 | 0.274 (0.200) |
    | velvet/walnut | — | 0.504 | 0.004 | 0.487 | 0.581 | **0.526 (0.441)** |
    | ridge/saddle | — | 0.507 | 0.007 | 0.418 | 0.504 | 0.238 (0.162) |

    The cycle-3/4 workhorse **C1 (prism/slate) survives at rank 2** and is
    retained, so the roster keeps continuity with every published
    preference number. `velvet/walnut` carries roughly double the label mass
    of any other pair (0.526 mean, 0.441 worst-probe) — the cleanest
    restricted-choice read in the set, reported per PROPOSAL-h §2 H3.
  - **DO NOT read the ranking as a ranking, and this is measured, not
    asserted.** Three pairs were screened in iteration 1 and again here with
    the starting presentation order **swapped** (the sorted-tag convention
    reversed them); five were screened in the same order. The five same-order
    pairs reproduce **bit-identically** — Δ = 0.0000 on all five. That is
    **APPARATUS RESULT D-1 — screen determinism certified**, noted by the
    2026-08-21 adjudication as a result in its own right and not merely as
    a check on this screen: the MLX apparatus, the probe construction and
    the readout are jointly bit-reproducible across processes and hours. The
    three swapped-order pairs differ by **+0.0212, +0.0090, −0.0008**. So
    order-counterbalancing at n = 16 leaves a residual up to ~0.021 in
    `identity_split`, which is the same size as the sampling SE (median
    0.0156 across the 120 pairings, IQR 0.0115–0.0209). **The recommended
    four are separated from each other by 0.006 and from ~15 further pairs
    by less than that residual.** The correct reading is "any of the top
    group is equally admissible", never "these are the best four". The band
    itself is safe — its halfwidth is 6.4 median SEs.
  - **FLAG — a format-robust alternative exists, and the choice between them
    is a real one.** The band is declared on scaffold, and the recommendation
    above honours that. But **27 of the 46 clear on BOTH formats**, and
    prism/slate is not among them (bare identity 0.696, as in iteration 1).
    Restricting the matching to the both-format set gives:
    **granite/plaza, velvet/walnut, ridge/saddle, canvas/maple** (bare
    identities 0.419 / 0.487 / 0.418 / 0.514) — the same roster with the
    incumbent swapped out. So LOCK-h faces a clean trade: **continuity with
    the pair that carries the published cycle-3/4 numbers, or robustness to
    the format question that is still open.** Both rosters are in the
    artifact; Code does not pick between them.
  - **ADJUDICATED 2026-08-21 — H3b ACCEPTED. Roster of record = the
    CONTINUITY four: `granite/plaza`, `prism/slate`, `velvet/walnut`,
    `ridge/saddle`.** Declared **"an admissible four", never "the best
    four"** — the wording follows directly from the residual measurement
    above, which cannot resolve the top group. The format-robust
    alternative is **recorded, not taken**: **scaffold is the format of
    record and bare-format balance is not a criterion for e2b.** The roster
    locks in LOCK-h v1.
  - **Naming convention, stated once because tonight it was ambiguous.** Raw
    logs carry the **local** run date; the design instance's blocks and
    adjudications carry UTC and are therefore dated 2026-08-21 for work that
    ran on the evening of 2026-08-20 local. Every log in this batch is
    `2026-08-20_*` because that is when the runs happened.
  - RECOMMENDATION ONLY — the roster locks in LOCK-h.md.

- 2026-08-20 — **Paired-shadow FLIP gate, the second piece owed for LOCK-h
  v1. The paired design measures the leak directly and beats the unpaired
  gate whenever the state flips fewer than 25% of choices — and PROPOSAL-h
  §1's own argument says we are well under that. Recommended gate form is
  π_d-free.**
  ([`data/e2b/h1_power.json`](data/e2b/h1_power.json) → `lockh_v1.flip_gate`;
  raw [`2026-08-20_h1_power_flipgate.txt`](results/raw/2026-08-20_h1_power_flipgate.txt))
  - **What the paired design makes available.** Every state-present choice
    read is paired with a state-free shadow read of the *identical prefix*
    (PROPOSAL-h §0.2), so the two members of a pair differ by exactly one
    thing: the injection. Over N pairs let a **flip** be a discordant pair,
    π_d the discordance rate, n_d = π_d·N, and split flips by direction —
    b toward the +arm tag, c toward the −arm tag.
  - **The null is b = c, and emphatically NOT "no flips".** If the injection
    perturbed nothing, π_d would be 0: the restricted-choice read is
    deterministic given the prefix. That is not the null. PROPOSAL-h §1
    holds that residual state effects on the choice computation
    (destabilisation, exploration shift) are **arm-symmetric**, and that a
    leak is the **directional** part. So the paired design decomposes the
    injection's effect on choice into two separable quantities —

        π_d          how much the state moves choices at all
        (b − c)/N    how much it moves them one way

    — and only the second is leak. Getting this backwards would turn the
    design's expected arm-symmetric noise into an apparent gate failure.
  - **Why it is the sharper instrument.** The unpaired gate estimates the
    same marginal displacement, (b − c)/N, but a one-sample share carries
    variance ≈ 0.25/N against the paired estimator's ≈ π_d/N. **The paired
    gate therefore wins exactly when π_d < 0.25**, and wins by a lot in the
    low-flip regime PROPOSAL-h §1 argues for ("a live praise-state has
    nothing praise-adjacent to boost"). A leak L appears in the flip share
    amplified: `δ_flip = L/(2π_d)`, feasible only where **π_d ≥ L** — a leak
    cannot be realised through fewer flips than its own magnitude.
  - **The table at bar_leak = 0.0735** (n_d = discordant pairs required;
    reads = paired reads; unpaired comparators 376 / 492):

    | π_d | δ_flip | n_d (rej) | reads | n_d (est) | reads | vs unpaired |
    |---|---|---|---|---|---|---|
    | 0.08 | 0.4594 | 10 | 125 | 10 | 125 | **0.33x / 0.25x** |
    | 0.10 | 0.3675 | 16 | 160 | 18 | 180 | 0.43x / 0.37x |
    | 0.15 | 0.2450 | 36 | 240 | 42 | 280 | 0.64x / 0.57x |
    | 0.20 | 0.1837 | 58 | 290 | 82 | 410 | 0.77x / 0.83x |
    | 0.25 | 0.1470 | 92 | 368 | 124 | 496 | 0.98x / 1.01x |
    | 0.30 | 0.1225 | 134 | 447 | 172 | 574 | 1.19x / 1.17x |
    | 0.50 | 0.0735 | 376 | 752 | 492 | 984 | 2.00x / 2.00x |

    The exact computation lands the crossover **on** π_d = 0.25 (0.98x /
    1.01x) and hits exactly 2.00x at π_d = 0.50, which is the asymptotic
    prediction reproduced from discrete arithmetic — an internal check the
    table passes rather than an assumption it makes.
  - **RECOMMENDED FORM, and it is the part worth reading twice: declare the
    gate on n_d, not on N.** π_d is unknown until H1 runs, so a gate written
    against a session count inherits an unknown and can silently be
    underpowered. Written against the discordant count it cannot: **stop
    when n_d discordant pairs have accrued.** Conditional on n_d, b is
    exactly Binomial(n_d, ½) under the null — the stopping rule depends only
    on the *total* discordant count, never on the split — so the test stays
    exact under inverse sampling. π_d then governs only how long the run
    takes, not whether the gate is valid. Pair it with a declared maximum N
    so a vanishing π_d cannot run forever. This form costs nothing to be
    wrong about π_d.
  - **Caveat, inherited.** Flips at reads 2..m carry the pooling caveat.
    As a *leak* measurement it is less troubling than for a preference DV —
    the leak is a property of the injection at the read, not of the
    subject's history — but the live arm must be tracked per read, and the
    `sessions_at_m_reads` column assumes ICC 0, the optimistic end.
  - ARITHMETIC ONLY. LOCK-h.md is design-instance authored.

- 2026-08-20 — **Adjudication 2026-08-21 applied: S2 accepted and CLOSED as
  a satellite; the corrected reading of record appended verbatim to entry
  and artifact; A-1 named and queued; thermal disposition recorded.**
  - **Item 1 — applied, both surfaces.** The design-instance corrected
    reading is appended verbatim to the S2 entry and to
    `data/e0/s2_neighbor_axes.json` under `adjudication_2026-08-21`. **The
    registered `reading.branch` field is byte-identical to what the run
    wrote** (asserted, not assumed) — a pre-registered reading is not
    re-labelled after data, and the refinement is carried as description
    beside it, not on top of it.
  - **Item 2 — nothing to do in the repo, by design.** The e2a scope
    wording inherits the V2-caveat resolution at the paper layer; no verdict
    field changes here. Recorded so a later reader does not go looking for
    a repo change that was deliberately not made.
  - **Item 3 — applied.** The D− asymmetry is now **APPARATUS NOTE A-1 —
    negative-pole dose asymmetry**, named with a grep anchor, QUEUED, and
    explicitly not chased; it joins the handoff flag table. The
    sentiment/vignette split is marked as reported **only** as an
    equivalence, never as a difference.
  - **Item 4 — applied.** The throttled figure remains the budget number;
    the 1.7x sustained-load factor is demoted to unreproduced-observation
    status. `caffeinate -is` now heads a new **§5c Long-run checklist** in
    the handoff, which did not previously exist.
  - **Item 5 — S2 CLOSED.** Still owed for LOCK-h v1 and delivered in this
    batch: the paired-shadow flip arithmetic (entry above) and the
    re-pairing screen (entry above that).
  - **FLAG — small, structural, and now at four copies.** `_new_qwen_adapter`
    is duplicated verbatim in `h3_tagscreen_qwen.py`, both S2 scripts and
    now `h3b_repair_screen.py`. It belongs in `valence_core.adapters` as a
    `qwen_or_explain()`. It was **not** moved: rule 26 makes any core change
    an acceptance-test event, and a screening script is the wrong occasion
    to trigger one. Recorded as debt with the reason it was not paid.

- 2026-08-20 — **S2 step 2, the registered 11-arm panel: the reward axis is
  NOT the most potent member of its own panel. Registered branch fires —
  "neighbours match or exceed"; reward/character = 0.97x. But the structure
  underneath is sharper than that label: potency tracks EVALUATIVE CONTENT
  and is indifferent to SELF-INDEXING.**
  ([`data/e0/s2_neighbor_axes.json`](data/e0/s2_neighbor_axes.json); raw
  [`2026-08-20_s2_neighbor_axes.txt`](results/raw/2026-08-20_s2_neighbor_axes.txt);
  L48, frac 0.1, |α| = 10.3010 = 0.1 × R_48 (103.01), 12 instruments,
  G = 0.315550, 1152 contexts/arm at the FULL 96/probe battery, 11 arms,
  12,672 forwards, 8,036 s)

  | axis | construct | D+ (G) | D− (G) | amp (G) | V1 |
  |---|---|---|---|---|---|
  | character | identical feedback sentence, third party — **evaluative, self-indexing removed** | +0.997 | −1.218 | **1.108** | PASS |
  | reward | self-directed evaluative feedback (**the program's axis**) | +0.902 | −1.251 | **1.077** | PASS |
  | sentiment | generic valence, externally targeted, **never evaluative** | +0.553 | −0.952 | 0.753 | fail |
  | vignette | circumstantial affect, second person, **non-evaluative** | +0.586 | −0.915 | 0.750 | PASS |

  Random envelope 0.0884 σ. Axis shas: reward `3c17b0d8fbcad716`, sentiment
  `71aacd7f7c587cf7`, character `cc7643741c5a97a6`, vignette
  `36a066edb57f5150`. `is_registered_panel: true` — the full approved panel,
  no `--drop-vignette`.

  - **The registered reading, verbatim from the artifact:** *"neighbours
    match or exceed — generic valence"*, reference/strongest-neighbour =
    **0.9718x**, strongest neighbour = **character**. The artifact's own
    note applies: the ratio is descriptive, because no threshold separating
    the branches was pre-registered.
  - **FLAGGED — the branch label may not fit the data that fired it.** The
    branch is named *generic valence*, but generic valence is precisely the
    **weaker** pair here: sentiment (0.753) and vignette (0.750) sit ~30%
    below reward, while the neighbour that matches-or-exceeds is
    **character** — evaluative content with the self-reference stripped.
    The panel splits cleanly by **evaluative content**, not by valence and
    not by self-reference:
    - remove the **self-indexing** (reward → character): 1.077 → 1.108,
      **+2.9%**. Costs nothing; if anything it helps.
    - remove the **evaluative content** (reward → sentiment / vignette):
      1.077 → 0.753 / 0.750, **−30%**, and the two non-evaluative
      constructs land within 0.003 G of each other despite differing in
      both valence source and person.

    S2 was built as *"a discriminant test of self-indexing"*
    (`valence_core/neighbors.py`, CHARACTER settlement 2026-08-20). It
    returns a clean answer to that question: **on this battery, at matched
    dose, self-indexing contributes nothing to behavioural potency.**
    Whether the registered branch label survives contact with that is the
    design instance's to settle — Code does not re-label a pre-registered
    reading.
  - **The V2 guard is now the strongest arm in the panel.** `span_character`
    was frozen 2026-08-08 as the **V2 self-indexing guard** and has carried
    published numbers as a control. Injected in its own right it is the most
    potent direction tested. This bears directly on the V2 mixed-claim
    caveat already attached to e2a's outcome wording; it is raised, not
    resolved, here.
  - **The conclusion does not rest on the ±asymmetry.** Every axis displaces
    the battery harder on the negative pole (|D−|/D+ = 1.22–1.72), so
    `amplitude` averages a pole that may be inflated. **It is inflated: the
    RANDOM arms show the same asymmetry and worse** — rand+ = +0.0175 σ vs
    rand− = −0.0884 σ, ratio **5.05**. A norm-matched direction with no
    content at all displaces this battery ~5x more downward than upward, so
    part of every axis's D− is a shared dose-direction artifact of the
    readout rather than axis content. **The ranking is unchanged on D+
    alone** — character 0.997 > reward 0.902 > vignette 0.586 > sentiment
    0.553 — so the finding survives dropping the contaminated pole
    entirely. **APPARATUS NOTE A-1 — negative-pole dose
    asymmetry.** Named and QUEUED by the 2026-08-21 adjudication; not
    chased. A readout property worth its own look, not a threat to this
    table.
  - **V1 potency, and a split that must not be over-read.** The failing
    conjunct for sentiment is `min(D+, |D−|) > 2·max|Δ_rand|` (threshold
    0.176722 σ): sentiment misses by **0.00208 σ = 0.0066 G**, vignette
    clears by **0.00818 σ = 0.0259 G**. The two constructs are separated by
    0.010 σ across a pass/fail line. **Sentiment "fail" and vignette "PASS"
    are the same measurement to within noise** and should not be reported as
    a difference between them; their amplitudes differ by 0.003 G.
    **The 2026-08-21 adjudication adopts this caution verbatim: the
    sentiment/vignette split is reported ONLY as an equivalence, never as a
    difference.**
  - **Matched dose proven, not assumed:** `assert_equal_norm` over every
    axis pair and against both random arms, |α| identical at 10.3010. A
    table between differently-dosed axes would measure the dose.
  - **FLAG — apparatus/calibration, and it runs the other way for once.**
    Budget was 3.87 h at the throttled rate; the run took **2.23 h**. Every
    one of the 11 arms came in at **724–738 s** — flat, no drift from first
    arm to last. The 2026-08-12 calibration's 1.7x sustained-load thermal
    throttle (720–736 s → 1245–1281 s) **did not reproduce** across 2.2 h of
    continuous load. The opening rate held for the whole run. Tonight's
    difference from that session: `caffeinate -is` and nothing else
    competing for the GPU. The throttled figure remains the safe number to
    budget against, but it is no longer a reliable predictor and the
    1.7x factor should not be treated as a property of the machine until it
    is seen again. **ADJUDICATED 2026-08-21: the throttled figure remains
    the budget number; 1.7x is demoted to unreproduced-observation status;
    `caffeinate -is` joins the long-run checklist.**
  - No verdict is claimed and none is available: S2 is a composition assay.
    The numbers are delivered; PROPOSAL-g §S2's reading is the design
    instance's to apply.
  - **ADJUDICATED 2026-08-21 — S2 ACCEPTED AS LOGGED; registered branch
    applied, claims narrow; S2 CLOSED as a satellite.** The registered
    `reading.branch` field is deliberately left exactly as the run wrote it.
    **Corrected reading of record — design-instance authored, appended
    verbatim, licensed as description only:**

    > "Post-hoc refinement of the branch label, licensed as description only: the panel splits by evaluative content (±30%), not valence source or person; self-indexing is causally inert at matched dose (±3%, within measurement). The marking is evaluation-specific and self-indifferent."

    The same note is appended to
    [`data/e0/s2_neighbor_axes.json`](data/e0/s2_neighbor_axes.json) under
    `adjudication_2026-08-21`, beside an untouched `reading`.

- 2026-08-20 — **LOCK-h v1 arithmetic under the 2026-08-21 conventions:
  `bar_leak` = 0.0735, and it is set by the false-verdict-rate
  ceiling, not by half the MDE. H1 needs n = 376 (rejection framing) or
  492 (estimation framing) — not 64, and not the 212–470 the earlier
  reading bracketed.**
  ([`data/e2b/h1_power.json`](data/e2b/h1_power.json) → `lockh_v1`;
  raw [`2026-08-20_h1_power_lockh_v1.txt`](results/raw/2026-08-20_h1_power_lockh_v1.txt))
  - **The four open assumptions are now settled, and two framings the
    2026-08-20 arithmetic never computed are added.** Δ_first pooled over
    all marker sessions with the sign-lock as a *conjunct*; MDE at 80%
    power; H1 two-sided; MDE_verdict taken as the **conjunctive** MDE with
    the envelope conjunct held at p90; `bar_leak = min(0.5 × MDE_conj,
    leak at ≤ 2.5% false-verdict rate)`; plus an estimation-gate variant
    and a cluster correction. The legacy section is untouched and
    reproduces bit-identically (13/13 keys vs the committed artifact), so
    the 2026-08-20 numbers remain derivable from the same script.
  - **The conjunction is far harder than the binomial alone.** MDE_conj =
    **0.2110** vs 0.1300 binomial-only. The envelope conjunct at p90
    (0.16667) requires k ≥ **65**/96; the binomial conjunct requires only
    k ≥ 57. The envelope, not the binomial, is the criterion.
  - **One-sided vs two-sided is therefore moot.** Read two-sided the
    binomial needs k ≥ 59 — still under 65. Both readings return the
    identical MDE_conj, `leak@2.5%`, and `bar_leak`. The ambiguity in the
    convention list costs nothing and needs no adjudication.
  - **Which branch binds, and it is not the registered one.** 0.5 ×
    MDE_conj = 0.1055; the leak sustaining a ≤ 2.5% false-verdict rate is
    **0.0735** (achieved rate 0.0245). `min` takes 0.0735 — so under v1 the
    half-MDE formula in PROPOSAL-h §2 is **not** what sets the bar; the
    false-verdict ceiling is ~30% stricter.
  - **Type-I of the full conjunction at Δ = 0 is 0.00034**, one-sided. The
    sign-lock and envelope conjuncts hold it there; the nominal α = .05
    binomial is nowhere near binding. A verdict that fires is expensive to
    fire by chance — which is exactly why a *systematic* leak, not noise,
    is the threat the H1 gate exists for.
  - **H1's n, three ways at bar_leak = 0.0735:**

    | framing | n | note |
    |---|---|---|
    | rejection: two-sided exact, power ≥ 0.80 | **376** | power at drafted n = 64 is **0.169** |
    | estimation: 95% CI upper bound ≤ bar, *can* pass | 190 | half-width 0.0732 — only on a perfect Δ̂ = 0 draw |
    | estimation: passes w.p. ≥ 0.80 when the true leak is 0 | **492** | achieved 0.809 |

    The estimation gate needs **more** than the rejection gate, which is
    not a paradox: "power to detect a leak of `bar_leak`" and "certify an
    interval inside `bar_leak`" are different demands, and only the second
    is what a *budget* actually claims. Which one LOCK-h adopts is a
    design decision with a 116-session price tag.
  - **Cluster correction for pooled within-session reads** (m = 6, e2a
    lineage), on the 492-read estimation basis: ICC 0 → 82 sessions;
    0.1 → 123; 0.2 → 164; 0.3 → 205; 0.5 → 287; 0.75 → 390; 1.0 → 492
    (DEFF = 6, pooling buys exactly nothing — the formula's sanity check).
    **FLAGGED — substantive:** pooling reads 2..6 *changes the DV*. The
    registered primary is the FIRST free choice, whose live state is the
    counterbalanced forced-phase state; later reads sit under a state the
    subject's own previous choice delivered, on a selected sub-population.
    The arithmetic says what pooling would buy **if** the reads were
    exchangeable. Whether they may be pooled at all is the design
    instance's call, not arithmetic's.
  - **The control envelope is now computed exactly** rather than simulated:
    it is the max of two independent folded binomials, so its distribution
    is a closed-form product of CDFs. Exact p90 0.166667 / p95 0.194444 —
    identical to the 200k-sim values (the support is discrete); exact mean
    0.093706 vs simulated 0.093639. The simulated version is retained for
    continuity with the committed artifact. Rule 10's under-sampled-null
    hazard no longer applies to this conjunct.
  - **FLAG — apparatus, cheap to fix, cost one detour tonight:** *no python
    on the laptop has scipy* — not the venv, not system, not miniconda, not
    homebrew. `h1_power.py` has needed it since it was written, and the
    committed numbers were produced elsewhere. It was run here from a
    throwaway venv in the session scratchpad (`python3 -m venv` + `pip
    install scipy`), deliberately **not** by installing into the user's
    miniconda base, because that env is the Qwen stack every published
    number depends on and a numpy upgrade mid-campaign is not a risk worth
    taking for a power calculation. The durable fix is to reimplement the
    handful of `stats.binom` / `stats.beta` calls in numpy (all four are
    exactly computable) so the script runs anywhere the suite runs —
    proposed, not done, since it touches numbers-producing code and would
    need its own rule-26-style reproduction check.
  - ARITHMETIC ONLY. `LOCK-h.md` is design-instance authored; nothing here
    instantiates a bar.

- 2026-08-20 — **S2 step 1: the vignette axis exists. Axis sha
  `4dec6d97e1b87734`, 384 contexts, 262 s. Step 2 (the 11-arm panel) ran
  immediately after; its table is the entry above.**
  ([`data/e0/s2_vignette_axis.npz`](data/e0/s2_vignette_axis.npz) +
  `.meta.json`; raw
  [`2026-08-20_s2_extract_vignette.txt`](results/raw/2026-08-20_s2_extract_vignette.txt))
  - Construct of record: *circumstantial-affect vignette (self-involving,
    non-evaluative)* — `GROUNDED: True`, stimulus approved verbatim by the
    2026-08-20 adjudication. 48 tasks x 2 conditions x 4 paraphrases = 384
    contexts, delivered through the e0 `Task:/Response:/Reviewer: {frame}`
    construction unchanged, so the axis differs from its neighbours in
    stimulus content and nothing else.
  - Rule 18 asserted before the model loaded: 8 frames disjoint from 4
    pools, both directions.
  - `R_l` (span-mean): 40 → 76.70, 44 → 91.71, 48 → 104.17, 52 → 145.18,
    56 → 204.16, 60 → 272.11. Span lengths 15/19/16.4 (min/max/mean).
  - The `.npz` is committed under a new named exception in `.gitignore`,
    beside `e0_axes.npz` and `e0_random_dirs.npz` and for the same reason:
    it is a frozen, sha-pinned direction the discriminant table is computed
    against, and the only panel member not already inside `e0_axes.npz`.
    A bare `*.npz` exception would sweep in the 202 MB residual dump, so
    the file is named, as the others are.

- 2026-08-20 — **H3 ran on Qwen: only 3/8 candidate pairs clear the
  0.50 ± 0.10 identity band on the primary (scaffold) format. A screening
  outcome, not a fired gate — but two findings should reach the design
  instance before any replacement roster is proposed.**
  ([`data/e2b/h3_tagscreen.json`](data/e2b/h3_tagscreen.json); raw
  [`2026-08-20_h3_tagscreen.txt`](results/raw/2026-08-20_h3_tagscreen.txt);
  8/8 pairs single-token on this tokenizer, 0 dropped; n = 16/pair/format,
  143 s)

  | pair | tags | scaffold identity | imb | bare identity | imb | scaffold pos | bare pos |
  |---|---|---|---|---|---|---|---|
  | C1 | slate/prism | 0.481 | **0.019** ✓ | 0.618 | 0.118 | 0.573 | 0.733 |
  | C4 | plaza/saddle | 0.477 | **0.023** ✓ | 0.423 | **0.077** ✓ | 0.531 | 0.749 |
  | C3 | granite/lattice | 0.435 | **0.065** ✓ | 0.614 | 0.114 | 0.556 | 0.746 |
  | N2 | quartz/ridge | 0.334 | 0.166 | 0.556 | **0.056** ✓ | 0.499 | 0.728 |
  | N1 | canvas/copper | 0.328 | 0.172 | 0.544 | **0.044** ✓ | 0.486 | 0.714 |
  | N3 | amber/velvet | 0.232 | 0.268 | 0.429 | **0.071** ✓ | 0.578 | 0.696 |
  | C2 | maple/cedar | 0.207 | 0.293 | 0.170 | 0.330 | 0.534 | 0.614 |
  | N4 | walnut/ember | 0.077 | 0.423 | 0.423 | **0.077** ✓ | 0.511 | 0.752 |

  - **The OLMo identity prior does not transfer, and that is a result about
    the record.** `prism` took 0.711–0.822 of the label mass on the OLMo
    chain — the 2026-08-19 finding that made H3 mandatory. On Qwen, C1
    (slate/prism) is the **most balanced pair on the primary format**
    (identity 0.481, imbalance 0.019). The cycle-3/4 workhorse pair is
    clean on the apparatus that produced the cycle-3/4 numbers, so no
    published preference number is impeached by an identity prior on its
    own tags. The screen was still right to run: it converted an
    assumption into a measurement.
  - **FLAGGED — substantive, and it should precede any replacement roster.
    Format is not presentation; it trades identity bias against position
    bias, and it changes what the instrument is.**
    - *scaffold* (primary): position near-balanced (0.486–0.578), but
      identity clears for only 3/8 — **and the label tokens are almost
      never the model's top choice** (top1_is_label 0.00–0.12), carrying
      0.13–0.39 of the mass.
    - *bare*: identity clears for 5/8, but **every** pair carries a heavy
      first-position bias (position 0.614–0.752), and labels are top-1
      0.62–1.00 (label_mass 0.09–0.24).
    - Only **C4 (plaza/saddle)** clears the band on both formats.
    - Order counterbalancing absorbs a position bias in the mean but spends
      DV range doing it (PROPOSAL-h §1's own argument, in reverse); an
      identity prior it cannot touch at all. Which of the two e2b should
      pay is a design question. Screening replacement candidates against
      the scaffold band *before* it is answered risks aiming a screen at
      the wrong criterion.
    - **RESOLVED 2026-08-21 — flag closed.** Scaffold is the **format of
      record** and **bare-format balance is not a criterion for e2b**. The
      caution above was right to delay a replacement screen aimed at the
      wrong criterion; the criterion is now declared, and H3b was screened
      against it.
  - **Recommendation (roster locks in LOCK-h, not here).** The cheapest
    next iteration needs **no new stimulus and no new rule-18 work**: the
    16 tags already in the roster are all single-token on this tokenizer
    and already hygiene-verified, and re-pairing them explores 120 pairs of
    approved material. An anchor-relative pull score (each tag against one
    fixed tag, then form the closest-matched pairs and confirm-screen them)
    costs ~6 minutes of model time and would very likely yield ≥ 4 clearing
    pairs. Not run tonight, deliberately: it should be aimed after the
    format question above is settled. Minutes, on the design instance's word.

- 2026-08-20 — **The interpreter guard shipped with the very name it
  protects left unbound. All three laptop scripts would have died on the
  exact raw traceback the guard was written to abolish. Caught before any
  run; repaired, and the repair proven to fire.**
  - **The defect.** `79868f7` moved adapter construction out of `main()`
    into a new `_new_qwen_adapter()` and deleted `from
    valence_core.adapters.qwen_mlx import QwenMLXAdapter` from `main()` —
    but never added it to the helper. The helper's `try:` body was left
    indented 12 spaces, the vestige of the deleted line. `QwenMLXAdapter`
    was unbound in `h3_tagscreen_qwen.py`, `s2_extract_vignette.py` and
    `s2_neighbor_axes.py` — every laptop script the handoff lists as
    runnable.
  - **Why the guard could not catch its own failure.** `except
    (ImportError, RuntimeError)` does not catch `NameError`. Each script
    would have raised a bare `NameError: name 'QwenMLXAdapter' is not
    defined` at the moment the model was to load — the guard turned into
    the thing it existed to prevent, on the same three files, one commit
    later.
  - **`79868f7`'s own lesson, applied to `79868f7`.** That entry prescribes
    importing each module and listing its functions, because *"compiling is
    not evidence that a file still does what it did."* That check **passes**
    here — no function was dropped this time (inventories verified
    identical to `e1b5c77` on all three files). It could not have caught
    this: the defect is not a missing function but an unbound global
    *inside* one. **The check that catches this class is executing the
    guarded path**, which is now also the habit.
  - **Repair.** The deferred import moved inside the `try`, where it wraps
    import *and* construction. It cannot live at module level (nothing
    fails there — MLX loads in `__init__`, which is the original patch's
    correct insight), and it cannot wrap construction alone (the name is
    then never bound). The docstrings now say so, naming the commit.
  - **Verified, not assumed.** In a fresh process per script with `mlx`
    blocked at the meta-path, `_new_qwen_adapter()` raises `SystemExit`
    naming `jlens-qwen36/.venv/bin/python` — **3/3, no `NameError`**.
    Suite 130/130 at `79868f7`.

- 2026-08-20 — **Handoff hardening: the laptop-side scripts named the
  wrong interpreter, which cost a session. Fixed at the source, in the
  error message, and in the handoff. Suite unchanged at 130/130.**
  - **What happened.** The S2/H3 scripts' usage lines said `python
    scripts/...`. On the laptop that is the system python, which has
    neither numpy nor MLX, so the scripts died with a
    missing-package error that read as a broken repo. It was trap 3 in
    the handoff all along — *"the only Python with numpy/MLX is inside
    the gitignored clone"* — but a trap listed in a document is not a
    trap the running script tells you about.
  - **Three fixes, because the trap has three surfaces.** Usage lines
    now name `jlens-qwen36/.venv/bin/python`. A guard translates the
    failure into the command that works. HANDOFF §0 carries the
    which-python rule beside the which-site rule, and trap 3 now
    carries the symptom.
  - **The guard wraps CONSTRUCTION, not the import, and that is the
    whole trick.** `QwenMLXAdapter` loads MLX in `__init__`, so nothing
    fails at import time; the first version wrapped the import and
    never fired once. It also catches **both** `ImportError` (this
    python has no MLX) and `RuntimeError` (the clone is missing) —
    indistinguishable to a user and identical in fix.
  - **Incident, recorded because it nearly shipped.** The first patch
    inserted the guard at the first blank-line `def` and excised
    everything up to `def main()` — which silently deleted
    `build_val_contexts` and `stratify` from the S2 runner. `py_compile`
    passed. It was caught by importing the module and listing its
    functions, not by the compiler. Scripts were reset to the committed
    state and re-patched with the insertion anchored immediately before
    `def main()`. **Compiling is not evidence that a file still does
    what it did**; the check that caught it is now the habit.
  - Handoff additions for the next thread: head of record `e1b5c77` and
    the 103-vs-130 fingerprint (a suite printing 103 is on `main`,
    missing the whole PROPOSAL-h batch); a §5b table of what is
    runnable right now, by site, with commands and costs; the H1 power
    finding added to the flag table with its anchor.

- 2026-08-20 — **Consolidated batch reconciled. PROPOSAL-h's timestamp
  recorded; S2 adjudications applied (vignette grounded, persona settled,
  "Ho-style" retired); items 2 and 5 were already done and are not
  redone. Suite 125 → 130. S2 CANNOT RUN AT THIS SITE — flagged, with
  the command and a corrected budget.**
  - **Item 1 — the hash of record: `34eb7ee`.** That commit is
    PROPOSAL-h's timestamp per its own status line. **Note for the
    record: PROPOSAL-h and ADDENDUM-g1 arrived in the SAME commit**, so
    g1's timestamp is `34eb7ee` too — the batch anticipated two hashes
    (`<hash-h>`, `<hash-g1>`) and there is one. Both documents are
    byte-identical to what was committed; neither was edited by Code.
    The preceding commit `499f6d5` carries the PROPOSAL-g status-line
    amendment, which closes the item-2 escalation opened earlier today.
  - **Item 2 — already applied, in `6897b67`,** before this batch
    arrived. Rule 5(e) carries the h-amendment verbatim. Re-stating the
    correction logged there: PROPOSAL-h §0's preamble calls two-horns
    "law rule 4"; it is **rule 5** in v3.1 (rule 4 is equal-norm), and
    §0.4's "the two-horns rule" is what fixed the target.
  - **Item 3 — adjudications applied throughout.**
    - **Persona:** settled on the grounded reading. `span_character`
      fills the §S2 persona/character slot; Chua-style identity axes are
      out of S2 scope. Recorded in the spec's own provenance string, so
      the settlement travels with the axis rather than living only here.
    - **Vignette:** `grounded: true`, citing this adjudication. Construct
      name of record — **"circumstantial-affect vignette (self-involving,
      non-evaluative)"** — is now the spec's construct text; **"Ho-style"
      is retired** and appears nowhere in the code path.
    - **It is a full panel member, not an opt-in.** `--include-vignette`
      is gone; the flag is now `--drop-vignette`, which prints a warning
      and marks the artifact `is_registered_panel: false`, because
      running without it is a different experiment from the registered
      one.
    - **A missing vignette axis is now an error, not a shorter table.**
      The runner stops with the extraction command rather than producing
      a three-row panel, since an absent row reads as tested-and-null.
  - **The one asymmetry the adjudication leaves, stated because it is
    real:** sentiment and character are grounded by *prior extraction*
    (frozen V2/V3 guards that carried published numbers); the vignette is
    grounded by *approval*. Equally admissible, equally able to decide
    the reading — but it has no extracted history, so its axis must be
    built before the panel can run.
  - **Suite pins moved with the adjudication (125 → 130).** Panel
    composition is now checked as a *property of the frozen family*
    rather than a hardcoded list, so "two of three need no new
    extraction" stays true if the panel is reordered. Rule 6 is still
    pinned — on a fabricated unadjudicated axis, since excluding the
    vignette would now be the bug rather than the check — and its
    converse is pinned too: the approved vignette DOES take the branch
    when it is strongest.
  - **Item 4 — S2 NOT RUN. This is a cloud container: no MLX, no Qwen
    weights, no `jlens-qwen36`.** The paste is addressed to a laptop
    session and S2 is laptop-only by design (§5: Qwen oracle, published
    tier). Everything is built, suite-green and staged; the run needs
    the site. Sequence:
    `python scripts/s2_extract_vignette.py` (384 capture forwards,
    minutes) then `python scripts/s2_neighbor_axes.py` (11 arms ×
    1,152 = **12,672 forwards**).
  - **FLAG — the ~2 h 10 m budget is the opening rate, not the throttled
    one.** 12,672 forwards at 0.62 s/context is 2.18 h, which is where
    that figure comes from. But the 2026-08-12 calibration note is
    explicit: 1,152-context arms ran 720–736 s each for the first three,
    then **1,245–1,281 s** under sustained load — ~1.7× — and *"budget
    long multi-arm laptop runs at the throttled rate, not the opening
    rate."* Eleven arms at the throttled rate is **3.4–3.9 h**. The
    runner now prints both and writes `budget_h_throttled` into the
    artifact. Not a blocker; a scheduling fact worth having before a
    four-hour run starts.
  - **Item 5 — already built, in `6897b67`:** H3's MLX port
    (`scripts/h3_tagscreen_qwen.py` + `screen_roster_tokenizer`), the
    e2b quarantine (`valence_core/e2b/`, `choice_read_statepresent`,
    mandatory paired shadow reads), and the import-fails-outside-e2b
    check plus the structural check that no standard harness names the
    primitive. Nothing h-related has run, and nothing will before
    LOCK-h. **The H1 power finding from that entry stands and is the
    open question for LOCK-h: n = 64 gives power 0.137; ≥ 0.8 needs
    212–470 depending on conventions LOCK-h must settle.**
  - **Item 6 — noted, with the site caveat.** Pod specs live in
    HANDOFF §2 (US-CA-2, A100-SXM4-80GB, volume `o73qvy742n` at
    `/workspace`, image `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`,
    TCP 22). On "pod is up": respawn protocol both gates → A1 → A2 → A3
    → A4 → A5. **A cloud session cannot drive it** (no ssh client,
    port 22 blocked); that sequence needs a session with SSH.

- 2026-08-20 — **PROPOSAL-h batch: rule 5 amended (verbatim), e2b
  quarantine built, H3 ported to MLX, LOCK-h power arithmetic delivered.
  Suite 103 → 125. TWO FLAGS, one of them load-bearing: H1 at the
  drafted n = 64 has power 0.137, not ≥ 0.8 — its own escape clause
  fires.**
  - **Item 1 — CLAUDE.md amended, text verbatim, as rule 5(e).**
    **CORRECTION, flagged not silently fixed:** PROPOSAL-h §0's preamble
    says "Two-horns (law rule 4)". In CLAUDE.md v3.1 two-horns is **rule
    5**; rule 4 is equal-norm for preference pairs. §0.4 correctly names
    "the two-horns rule", so the amendment went to rule 5 and the
    numbering slip is recorded here rather than propagated. Applying it
    verbatim to the rule *numbered* 4 would have attached a
    state-present exception to the equal-norm law.
  - **Item 2 — e2b harness built, split by hazard.** The dangerous thing
    is small and quarantined; everything testable is inert and
    importable. `valence_core/e2b/records.py` carries provenance,
    shadow pairing and leak arithmetic; `statepresent.py` holds the one
    function that can put a state on the residual stream at a choice
    position and **refuses to import** outside the e2b package or a
    `scripts/e2b_*.py` runner.
  - **The guard's first version was worthless and is recorded as such.**
    It scanned the whole stack for a sanctioned frame — and since the
    module lives inside the package it always found *itself*, sanctioning
    every caller. It now consults only the importer. Both directions are
    suite-pinned: the import fails here, and succeeds from an
    `e2b_*.py` runner.
  - **The guard is not claimed to be airtight, and the docstring says
    so.** Anything that can import a sanctioned runner inherits the
    capability; Python offers no way around that. The real guarantee is
    structural and checked every run: **no module in `valence_core`
    outside `e2b/` so much as names the primitive**, and `choice_read`'s
    signature has not grown an injection parameter (rule 5(e)'s final
    clause, "the insulated primitive is never modified").
  - **Refusals at construction, not flags at analysis.** A state-present
    read with incomplete provenance, a null dose, or no shadow cannot be
    constructed — it is a read the amendment did not license, and the
    only safe time to catch it is before it enters a campaign. A
    "shadow" that carries provenance is refused too.
  - **The leak summary splits by injected sign, and the suite pins why.**
    A leak pushing the same way under +state and −state is a token-level
    artifact the label-map counterbalance cancels; one that reverses
    with the state is the leak that would masquerade as preference.
    Pooling averages exactly that distinction away — fixtures confirm a
    state-reversing leak of ±0.10 pools to 0.000.
  - **Item 2 (H3) — the port was smaller than the word suggests.**
    `tagscreen` already speaks `ModelAdapter`, so it runs on MLX
    unchanged; the tokenizer half needed the work.
    `assert_roster_tokenizer` enforces ids A1 pinned on the *OLMo*
    tokenizer, which mean nothing on Qwen, so H3 gets
    `screen_roster_tokenizer` — reports which pairs this tokenizer can
    read, drops the rest **with a reason**. On a new apparatus a
    multi-token tag is a screening outcome, not an incident.
  - **Item 3 — LOCK-h power arithmetic, and it does not come out where
    the draft assumed.** `scripts/h1_power.py`, model-free, re-runnable.
    At verdict n = 96, exact one-sided α = .05: critical k ≥ 57/96,
    **MDE_verdict = 0.130 in share units** (0.260 as a difference), so
    **bar_leak = 0.065**.
    **FLAG — H1 at n = 64 has power 0.137 against that bar. Power ≥ 0.8
    needs n ≈ 470, 7.3× the drafted 64.** §2 anticipates exactly this:
    *"if 64 is insufficient under the computed numbers, H1 extends
    before opening, never after."* It is insufficient. Sensitivity
    across every reading of the undeclared conventions: 470 / 348 / 282
    / 212 — **the cheapest defensible reading still needs 212, 3.3×**.
  - **FLAG — the control envelope usually dominates the binomial, which
    makes MDE_verdict as drafted a lower bound.** Max |pseudo-Δ| across
    sham (36) and random (36) under the null has p90 = 0.167 > the
    binomial MDE 0.130 (200k sims). The verdict criterion is
    conjunctive, so its true MDE is the larger of the two — and since
    bar_leak is defined off MDE_verdict, a bigger MDE *helps* H1 (that
    is the 282 row). Which definition LOCK-h adopts changes H1's n by
    more than a factor of two.
  - **Three conventions the arithmetic needed and the pre-registration
    does not state**, surfaced rather than silently chosen: whether
    Δ_first pools over all marker sessions or is computed within each
    map and combined (effective n, and every number here, moves); the
    power level MDE_verdict is quoted at (§2 declares a floor for H1,
    none for the MDE itself); and one- vs two-sided for H1 — computed
    two-sided, since its gate is on |Δ_first| and a one-sided reading
    would inflate the power.
  - **Item 4 — g1's anchor requirement made executable, not noted.**
    `extract.assert_stage_splits` requires an A3/A4 artifact to carry
    its own `stage`, `fit_ids`, `val_ids`, and refuses fit/val overlap.
    The failure it guards is recomputation: a split regenerated later
    from "tasks 1–24 are fit" looks right and stops being right the
    moment a stage drops an item — after which g1's probe and judge are
    scored on different materials and the reads-but-doesn't-act
    dissociation is unreadable. Two id lists at write time;
    unreconstructable once the run is gone.
  - **Nothing was run.** H3 awaits the word (laptop, minutes); H1 awaits
    LOCK-h. Suite **125/125** model-free.

- 2026-08-20 — **Adjudication batch received and actioned (S1 accepted;
  A1 addition; sequence; S2 promoted). Items 3 and 5 are built and
  committed above. Item 2 is BLOCKED at this site and is the only thing
  in the batch not carried out.**
  - **Item 1 — S1 accepted as logged.** The registered recognition-break
    reading stands with the entry's scope wording: parity is rejected in
    every cell, chance is compatible-not-proven. No further S1 cells; S1
    is closed.
  - **Item 2 — BLOCKED, needs the text or a laptop commit.** The
    status-line amendment was applied *on disk by the design instance*,
    which means it exists in the laptop working tree. This thread is a
    cloud session working from a clean clone of `origin/main`
    (`git status` empty, `origin/main` unmoved), so the edit is not
    here and cannot be committed from here. It is not the kind of thing
    to reconstruct from inference either: it is a pre-registration's
    status line, which §0.2 and the 2026-08-20 entry both put outside
    Code's authority to author. Escalated rather than approximated.
  - **Item 3 — done** (entry above): per-pair, per-stage `label_mass`,
    plus `label_mass_min`, plus the roster and selection machinery A1
    needs to produce a roster of record.
  - **Item 4 — sequence recorded**, and one correction to how it can be
    started. Respawn (both gates) → A1 screen → A2 → A3 → A4 → A5
    timing budget; LOCK-g stays design-instance authored. **The
    execution site is the constraint, not the authorization:** a cloud
    Code session has no `ssh` client, no outbound port 22, no MLX and no
    GPU, so it cannot drive the box even once the pod exists, and it
    cannot create the pod either (no RunPod MCP in this session; and per
    HANDOFF §2 the MCP could not attach the network volume anyway). Pod
    creation stays a console action; A-phase execution needs a session
    with SSH. Recorded in HANDOFF §0.
  - **Item 5 — done** (entry above): S2 built, and the build found that
    two of its three neighbour axes were already in the record.
  - Health check green throughout: **103/103** model-free, on this
    site, after `pip install numpy scipy` into a bare container.

- 2026-08-20 — **S2 BUILT (adjudication item 5): neighbour-axis panel,
  matched-dose qualification battery, and the discriminant table.
  Suite 83 → 103. Nothing run — this is construction; S2 executes on the
  laptop oracle.**
  - **The finding that shaped the build: two of the three neighbours need
    no extraction at all.** §S2 names generic sentiment contrast, a
    persona/character axis, and a vignette axis. The e0 frame battery
    already carries `sent_pos`/`sent_neg` and `char_pos`/`char_neg`, and
    the 2026-08-08 pass already froze both as `span_sentiment` and
    `span_character` in `data/e0/e0_axes.npz`. They were built as the V3
    and V2 *guards* — geometry used to license the reward axis — and S2
    asks a different question of the same vectors: not how much of the
    reward axis lies off them, but how hard they hit the behavioural
    readout when injected in their own right. Same vectors, same corpus,
    different instrument. **S2's extraction work is the vignette alone.**
  - `valence_core/neighbors.py`: the panel as specs (each carrying its
    construct, provenance, and a `grounded` flag), frozen-axis loading,
    matched dosing, the discriminant table in G units, and the registered
    §S2 readings.
  - **Matched norm fraction is proven, not assumed.** Every axis is dosed
    through `Injection.at_frac` on the model's own R table and then
    checked pairwise with `assert_equal_norm`, randoms included. The
    invariant already holds by construction, which is exactly why it is
    asserted — a discriminant table between differently-dosed axes
    measures the dose, and that failure is invisible in the output.
  - **The reference arm re-runs in the same session** rather than being
    quoted from 2026-08-08: a ratio between today's number and another
    session's silently imports every difference between them.
  - **FLAG — the persona reading is ambiguous and I did not settle it.**
    §S2 says "a persona/character axis". `span_character` is the repo's
    character axis (the identical feedback sentence addressed to a
    fictional third party), which makes S2 a clean discriminant test of
    self-indexing. But "persona" could equally mean an identity /
    self-concept axis in the Chua et al. sense, which this repo does not
    have and which §7 does not license. Built on the grounded reading,
    marked in the module, one edit to overrule.
  - **FLAG — "Ho-style" has no referent in this repo.** The phrase
    appears exactly once (§S2) with no citation, no corpus, and nothing
    in the archive; "vignette pharmacokinetics" in §7 is a planned item,
    not an existing stimulus. Rather than guess at a paradigm and present
    the result as a replication of it, the vignette axis is built with
    its construct stated: **affect induced by circumstance, second
    person, with no appraisal of the model's output anywhere in the
    frame.** That is a genuine third corner — `sent_*` is
    non-self-involving by construction (never second person) and
    `self_*` is evaluative by construction, so self-involving-and-
    non-evaluative is the cell neither existing neighbour occupies. The
    frames are committed at `data/configs/s2_vignette_frames.json` so
    the design instance replaces the stimulus by editing a file.
  - **The vignette carries `grounded: false` everywhere it goes** — spec,
    axis metadata, and the artifact — and `--include-vignette` is
    opt-in. It is reported in the table and **excluded from the
    registered reading** by construction (rule 6: an unadjudicated
    instrument does not decide a claim). Suite-pinned in both
    directions.
  - **S2's n is not pre-registered** (§5 declares none), so the
    invocation is the declaration and it is printed and written into the
    artifact before any scoring — the S1 precedent, applied without
    being asked twice.
  - **Cost anchors, from the measured 0.62 s/context oracle rate.**
    Grounded panel = 9 arms × 1,152 ≈ 10,368 forwards ≈ 1 h 45 m.
    With the vignette = 11 arms × 1,152 ≈ 12,672 ≈ 2 h 10 m. Vignette
    extraction is 384 capture forwards, single-digit minutes. Compare
    the rule-26 B2b reproduction: 5 arms ≈ 60 min.
  - Suite additions (83 → 103): the neighbour axes reproduce the
    published guard cosines at L48 (0.522 / 0.861) through the new
    module; one dose across every axis and `frac × R_ℓ` exact; a
    differently-dosed axis refused; an unextracted axis raises rather
    than yielding a missing row (an absent row reads as a null result);
    the proposed vignette frames pass rule 18 against the e0 pools;
    committed frames match the module constant; G-unit conversion; the
    V1 rule applied unchanged per axis in both directions; both
    registered branches; and the ungrounded-axis exclusion.

- 2026-08-20 — **A1 instrumented for the box (adjudication item 3):
  per-pair, per-stage `label_mass` now travels with the screen; the
  candidate roster is a committed config rather than a script constant;
  cross-stage selection built and tested. Suite 70 → 83. Nothing run —
  this is construction, and A1 still needs the box.**
  - **Item 3 applied.** `PairResult` gains `label_mass_min` alongside
    `label_mass_mean`, and `scripts/box_a1_tagscreen.py` reports both per
    pair per stage plus `top1_is_label_frac`, contrasted against the
    2026-08-19 reference (scaffold mass 0.898–0.982, top1 1.00) and the
    scaffold/bare ratio that measured template adjacency. **The minimum
    is the point:** branch (a) is a claim about the worst probe, and a
    pair averaging 0.95 while bottoming out at 0.20 is not delivering a
    clean restricted-choice read. Descriptive throughout — no bar is
    applied, because none is pre-registered (rule 21).
  - **Why this was needed at all:** branch (a) was established on
    (slate, prism), which the 2026-08-19 prior expects A1 to *reject*.
    If the roster of record ends up being four other pairs, branch (a)
    would otherwise have been confirmed on an instrument the program no
    longer uses.
  - **Roster committed:** `data/configs/a1_roster_candidates.json`, the
    8 pairs A1 names — four incumbents plus N1–N4 with the token ids
    recorded on 2026-08-20. **Correction recovered from the archive:**
    the fourth incumbent pair is **(plaza, saddle)**, not (gravel,
    plaza) — `gravel` → `saddle` by the verified pick procedure at the
    e2a smoke2 adjudication (2026-08-09,
    `archive/RESULTS-cycles3-4.md` L911). Two archive entries still
    print the pre-swap form, and the 2026-08-20 roster entry says only
    that `gravel` remains excluded, so a fresh thread could have
    screened the wrong pair.
  - **Tokenizer gate** (`tagscreen.assert_roster_tokenizer`): every tag
    single-token with a leading space, and every recorded id still that
    id. Both are hard stops. The second matters because a roster carries
    more than its strings — single-tokenness *and* pool disjointness were
    established against one tokenizer, and an id that has moved means
    those findings were established somewhere else. The gate escalates
    rather than silently re-verifying.
  - **The band is evaluated in exactly one place.** A1's criterion is a
    conjunction over four stages, so the per-stage script cannot test it
    and deliberately does not try — it prints distance from the band edge
    as orientation only. `scripts/a1_roster.py` (site-agnostic, no GPU)
    reads the four artifacts and applies the formula: clears iff inside
    the band on *every* stage; ranked by worst stage; top four selected;
    fewer than four clearing returns the replacement iteration rather
    than a short roster. **It refuses partial data** — selecting on three
    stages would weaken a four-way conjunction into a three-way one, and
    the missing stage is exactly where the failing pair would have been
    caught.
  - **Selection is a recommendation and says so in its own payload.** The
    roster of record enters through `LOCK-g.md`, which the design
    instance authors.
  - **DECLARED, because it is a criterion detail and belongs before the
    data:** the band is read as **inclusive** — imbalance ≤ 0.10 clears.
    A pair landing exactly on 0.100 is inside.
  - **Fixture bug caught by the change, not by the suite.** The
    `rank_by_balance` fixture built `PairResult` positionally, so
    inserting `label_mass_min` silently re-mapped mass onto
    `top1_is_label_frac`. Now keyword-constructed, with the reason in a
    comment so it is not undone.
  - Suite additions: worst-probe minimum is genuinely the minimum; the
    committed roster passes its own gate (16 tags); drifted id and
    multi-token tag both raise; the conjunction rejects a pair that is
    balanced on three stages and 0.75 on DPO; ranking, selection size,
    thin-roster iteration, partial-stage refusal, and the
    not-the-lock flag. **70 → 83, all model-free.**

- 2026-08-20 — **Last clone-only inputs pulled into the record; the
  ledger-26 oracle tier is now reproducible from the repo alone.**
  - Added, all byte-identical to the clone: `data/corpus/e2a_tasks.jsonl`
    (4.6 KB, 16 tasks × 4 paraphrases — the kernel-gate stimulus),
    `data/configs/e0_probes.json` (2.3 KB, the 12 readout probes the
    B1/B2 instruments are indexed by), and
    **`data/e0/e0_b1_markers.npz` (47.5 MB)** — the source the 12 B2b
    instruments are recomputed from.
  - **Size decision, stated rather than buried:** the B1 artifact is
    ~5.6× the previous entire `.git` (8.4 MB → ~56 MB), permanently in
    history. Admitted deliberately: rule-26 criterion (ii) *rebuilds*
    the instruments from this file, so storing only the derived
    instruments (~50 KB) would mean trusting a computation that could no
    longer be checked. `e0_residuals.npz` (202 MB) remains excluded —
    verified still ignored.
  - **Verified sufficient, not merely present:** `build_instruments()`
    now runs off `data/` and returns **G = 0.315550**, matching the
    published artifact's 0.315550304633827. That is the check that
    matters — a file in the record that the code doesn't read, or reads
    and disagrees with, is worse than no file.
  - **Every path repointed:** `oracle.py` (B1, e0 tasks, e0 probes, e2a
    tasks) and `scripts/s1_judge_rescue.py` now read `data/`; the dead
    `CLONE` constant is removed from the oracle. Only the Qwen *weights*
    still come from the gitignored clone. Absent inputs still report
    SKIP with a reason, never a pass.
  - Handoff trap 9 updated: it recorded these as outstanding.

- 2026-08-20 — **S1 COMPLETE (judge-rescue matched ladder, Qwen, existing
  e2a corpus). RESULT: the judge is not rescued on any rung. Every one
  of the 8 cells fails to clear chance, and every cell's 95% CI
  EXCLUDES probe-k=2 parity (.759). Registered reading: the break is at
  RECOGNITION.** (Raw: `results/raw/2026-08-20_s1_judge_rescue.txt`;
  artifact `data/e2a/s1_judge_rescue.json`. No new Qwen sessions, per
  §5.)
  - **n = 32 items/cell, declared before scoring** (entry above); 2
    position orders each = 64 reads/cell, 512 reads total. All reads
    vanilla state-free forwards over archived text — no steering
    anywhere in S1, so two-horns is satisfied trivially.

    | cell | acc | k/n | p | 95% CI |
    |---|---|---|---|---|
    | better k1 zeroshot | 0.484 | 31/64 | .646 | [.366, .604] |
    | better k1 fewshot | 0.516 | 33/64 | .450 | [.396, .634] |
    | better k2 zeroshot | 0.516 | 33/64 | .450 | [.396, .634] |
    | better k2 fewshot | 0.516 | 33/64 | .450 | [.396, .634] |
    | detection k1 zeroshot | 0.562 | 36/64 | .191 | [.441, .677] |
    | detection k1 fewshot | 0.547 | 35/64 | .266 | [.426, .663] |
    | detection k2 zeroshot | 0.531 | 34/64 | .354 | [.411, .648] |
    | **detection k2 fewshot** | **0.594** | 38/64 | **.084** | [.471, **.705**] |

  - **Replication anchor:** our matched cell (k=1, better-response,
    zero-shot) returns 0.484 against the original e2a judge's 14/32 =
    0.438 — same condition, same neighbourhood. The ladder is built on
    the result it is trying to rescue.
  - **The n=32 resolution worry flagged before scoring did NOT bite,
    and it is worth being precise about why.** I warned that an
    intermediate result would have a CI containing both chance and
    parity, adjudicating nothing. The observed best cell is 0.594 with
    CI [.471, .705]: it **includes chance** (so "at chance" cannot be
    rejected) but **excludes .759** (so parity IS rejected). Every
    other cell excludes .759 by a wider margin. The ladder therefore
    answers the question it was built for, despite the reduced n —
    because the informative direction was the one with headroom.
  - **Registered reading applies:** "judge stays at chance at parity →
    the break is at recognition (an interoception gap: external
    machinery decodes what the system's own reading machinery cannot
    reach)." Record length, in-context supervision, and framing were
    each varied and none rescues the judge. The probe reads .759 off
    the same records the judge cannot beat chance on.
  - **Descriptive, not a finding:** the detection framing runs above the
    valuation framing pooled (0.559 vs 0.508, delta +0.051). Directional
    only — no cell clears chance and the contrast was not powered.
    Recorded because §5's ladder exists to produce a localization
    curve, and this is its shape.
  - **Instrument caveat, carried visibly per §5, and one new one.**
    (i) The discriminability probe was once caught riding
    pole-asymmetric degeneracy and re-qualified; part of the .759 may
    be destabilization rather than valence — S2 is the assay for that.
    (ii) **Position bias varies sharply by cell** — p(picks A) ranges
    0.328 to 0.875, with `detection_k2_zeroshot` at 0.875
    near-degenerate. The A/B alternation absorbs this by construction
    (it is why both orders are run), but the spread means single-order
    2AFC judging on this apparatus would be unreliable, and any future
    judge design should treat order-counterbalancing as mandatory
    rather than hygienic.
  - **Rule-19 correction, applied and approved.** §5's detection framing
    asserted one response was generated under an injected state; in
    this corpus **both** sides are steered (+axis vs −axis), making the
    sentence false about the setup. Reworded (user-approved) to the
    true contrast — positive vs negative internal state — before any
    cell ran. The original wording was never executed.

- 2026-08-20 — **PROPOSAL-g committed as the pre-registration of record
  (`72b09a9`, 2026-08-20 01:52:19 -0400 — that hash is the timestamp per
  its own status line). A1 candidate roster proposed; S1 per-cell n
  declared before scoring. Two flags, both raised BEFORE any data.**
  - Committed **verbatim**, unedited. Its status line still reads "DRAFT
    v1.0"; Code does not edit a pre-registration, so that is left for
    the design instance. A1–A5 / B1–B3 / S1–S3 now supersede all prior
    g2/g3/g4 references (§0.2).
  - **A1, first half (laptop; the screen itself needs a box).** Eight new
    candidates proposed, each verified **single-token with a leading
    space on the OLMo tokenizer** and **word-boundary disjoint from
    every pool** — e0 tasks + completions, e0 frames, e2a task
    paraphrases, the probe battery, conditioning tasks, the neutral
    filler, and (ledger 28c) the wrapper templates themselves:

    | pair | tags | token ids |
    |---|---|---|
    | N1 | canvas / copper | 10247 / 24166 |
    | N2 | quartz / ridge | 52255 / 58933 |
    | N3 | amber / velvet | 68705 / 72426 |
    | N4 | walnut / ember | 93729 / 99384 |

    All eight cycle-3/4 tags re-verified single-token and pool-clean, so
    the 8-pair roster A1 specifies is viable.
  - **Pairing rationale, stated so A1 can falsify it:** pairs are formed
    by **adjacent token id**, not by semantics. The 2026-08-19 finding
    was that the bias is token *identity*, and the most plausible driver
    of an identity prior is token frequency — for which BPE merge order
    (id) is a rough proxy. So each pair joins two tags of similar
    presumed frequency. This is a hypothesis A1 measures, not an
    assumption it inherits.
  - **The hygiene screen earned its place:** `harbor`, `lantern`,
    `marble` and `kettle` are all single-token but collide with pool or
    conditioning text and were dropped. `gravel` remains excluded from
    cycle 3/4 for the same reason.
  - **FLAG — expect A1 to fail the incumbent pair.** The band is
    identity within 0.50 ± 0.10. The 2026-08-19 characterization put
    (slate, prism) at 0.711–0.822 across the four stages, i.e.
    imbalance 0.21–0.32, **two to three times outside the band on every
    stage.** At least one incumbent pair is therefore likely to fail,
    and the roster-of-four rule may need the replacement iteration §A1
    provides for. Recorded now so the outcome is not read as surprising.
  - **S1 per-cell n DECLARED BEFORE SCORING: n = 32, not the 64 §5
    requests.** The corpus supports 32 val-half 2AFC items (8 val tasks
    × 4 paraphrases, both poles present, both texts non-empty); fit half
    supplies 32 items for the m=8 few-shot exemplars. k=2 draws from
    C(32,2) = 496 distinct 2-subsets, so no reuse pressure. Eight cells
    × 32 items × 2 position orders = 512 judge forwards.
  - **FLAG — at n = 32 the interpretation map's middle branch is not
    resolvable, and this matters before scoring, not after.** Clearing
    chance one-sided at .05 needs **22/32 = .688**. The registered
    anchors: chance .500 → CI [.336, .664]; probe k=1 .645 → CI
    [.483, .796]; probe k=2 parity .759 → CI [.579, .867]. So an
    observed .645 has an interval **containing both chance and probe
    parity simultaneously** — S1 can cleanly separate "at chance" from
    "parity-rescued" only if the result lands near one extreme. Any
    intermediate outcome will be reported as the localization curve §5
    anticipates, but it cannot adjudicate between the two headline
    readings. Raising n is impossible without new Qwen sessions, which
    §5 forbids; position-order counterbalancing doubles reads but not
    independent items. Flagged for the design instance as a scope
    limit of S1 as written, not a reason to change it.

- 2026-08-18 — **Design-instance adjudication executed: window-coverage
  audit (descriptive), oracle-provenance GO, PROPOSAL-g window clause
  adopted into the adapter contract. No published verdict touched.**
  (Raw: `results/raw/2026-08-18_window_coverage_audit.txt`,
  `results/raw/2026-08-18_rule26_recheck_choiceread.txt`.)

  - **(1) WINDOW-COVERAGE AUDIT — the primary DV was never clipped.**
    Every archived choice-read prefix in e2a + f, tokenized and compared
    against the 512-token encode window; all sessions included, excluded
    ones too. **Choice index 1 is the first FREE choice — the forced
    phase is rounds, not menus — so index 1 *is* the primary DV
    (`first_free_pick`).** Result, per index (n / median / max / >512):

    | idx | e2a | f |
    |---|---|---|
    | 1 (DV) | 188 / 205 / 270 / **0** | 295 / 165 / 265 / **0** |
    | 2 | 187 / 274 / 354 / 0 | 294 / 225 / 333 / 0 |
    | 3 | 186 / 342 / 438 / 0 | 293 / 281 / 406 / 0 |
    | 4 | 185 / 409 / 520 / 1 (0.5%) | 291 / 341 / 475 / 0 |
    | 5 | 185 / 478 / 580 / 22 (11.9%) | 287 / 393 / 580 / 14 (4.9%) |
    | 6 | 184 / 548 / 666 / 152 (82.6%) | 285 / 453 / 655 / 61 (21.4%) |

    Pooled: **250/2860 reads (8.7%) exceeded 512**, entirely at indices
    4–6. The DV choice sits at median 205/165 tokens — under half the
    window — with a maximum of 270/265 across 483 DV reads.
    **Disposition: methods sentence, NO limitations clause** (the
    trigger the adjudication specified was "only if choice 1 ever
    clipped"; it never did).
  - **FLAG, the other half of the honest statement.** The primary
    analysis is untouched, but the *pooled* descriptives are not:
    FINDINGS-4 §2's session-share ≈ .50 alternation finding pools across
    all choice indices, so ~8.7% of the reads behind it were clipped —
    concentrated at index 6 (82.6% in e2a). Those were descriptive, not
    verdict-bearing, and every arm was clipped identically, so no
    published claim moves. The methods sentence should say both halves:
    **DV never clipped; pooled session-share descriptives include ~8.7%
    clipped reads.**
  - **Deviation, flagged:** the adjudication named
    `2026-08-17_window_coverage_audit.txt`; the run happened 2026-08-18
    and the file is dated to the actual run date, per the
    `results/raw/YYYY-MM-DD_*` convention. Content unchanged.

  - **(2) ORACLE PROVENANCE — done; the 0a flag is cleared.** Copied
    from the gitignored clone (never committed inside it) into the
    record: `e2a/analysis.json`, the g2 family
    (`g2_discriminability{,_v2}.json`, `g2_rounds_f0.1{,_v2}.json`,
    `g2_rounds_f0.2_v2.json`, `g2_spotcheck{,_rounds}.json`) and the g3
    family (`g3_kv_leakage.json`, `g3prime_kl{,_v1}.jsonl`).
    `g1_kernel_gate.json`, `e2a/sessions.jsonl` and `e0/e0_b2_b2b.json`
    were already in. All 13 verified to parse and to be **byte-identical
    to the clone**; `git check-ignore` confirms every one TRACKABLE and
    `.npz` still excluded. **No `.gitignore` change was needed** — the
    existing exception is directory-scoped (`/data/e2a/*.json`,
    `*.jsonl`), so the adjudication's "extend the scoped exception" was
    already satisfied; only the copy was outstanding.
  - **0b prerequisite, mapped precisely (not actioned — out of the
    named scope).** `scripts/paper_data.py` sets
    `DATA = REPO / "jlens-qwen36" / "data"`. Flipping that root to
    tracked `data/` at paper-1 needs **five more files, ~15 KB total**,
    all still clone-only: `e0/e0_b1_markers.meta.json` (2.3 KB),
    `e0/e0_b2_b2a.json` (6.7 KB), `e0/e0_b2c_a.json` (5.2 KB),
    `d/gates_repA.json` (681 B), `d/gates_repB.json` (682 B). The `d/`
    pair also needs a new directory exception (`data/d/` is not yet
    excepted). Its other sources — `e0/e0_axes.meta.json`,
    `e0/e0_b2_b2b.json`, `e2a/analysis.json`, `f/screen_analysis.json` —
    are now all in the record. One word and this is one command.
  - **Also available, not copied (not in the named list):**
    `e2a/sessions_smoke.jsonl` (37 KB) and
    `e2a/sessions_smoke_v1_incident.jsonl` (15 KB). Rule 25's
    read-everything clause and the fact that the second is an *incident
    record* argue for both; flagged for a decision rather than swept in.

  - **(3) PROPOSAL-g WINDOW CLAUSE — adopted into the adapter contract
    now.** Locked text, carried for the PROPOSAL-g draft: *the
    choice-read window is the full session, declared as a per-adapter
    constant; startup and per-read assertions require prefix_len ≤
    declared_window; a violation is an incident; context-window
    behavior is never inherited from a library default.*
    - `ModelAdapter.choice_window` defaults to **None**, and
      `assert_choice_window` raises on it — so an adapter that fails to
      declare a window cannot perform a choice read at all. Inheritance
      is not merely discouraged, it is unavailable.
    - `choice_read` asserts per read (verified: fires on an over-window
      prefix, and on an undeclared window).
    - `QwenMLXAdapter.CHOICE_WINDOW = 8192`, **declared, not
      inherited** — the tokenizer reports `model_max_length` 262144 and
      the old code carried a 512 default; neither was chosen for a
      scientific reason. 8192 is set with headroom against this audit's
      measured ceiling of 666 tokens.
    - The 512 truncation survives **only** behind
      `legacy_truncate=True`, which the rule-26 oracle sets explicitly
      and nothing else does; clipped encodes are now **counted** and
      reported in provenance (`n_encodes_clipped`), which is exactly the
      transparency whose absence caused this whole thread.
    - `OLMoHFAdapter` implements the same assertion in step 2.
  - **Re-verified, not assumed.** The change touched `encode` and added an
    assertion inside `choice_read` — i.e. the rule-26 criterion (iii) path
    itself — so criterion (iii) was re-run: **4/4, digit-for-digit
    identical** to the 2026-08-12 run (0/48 nonzero verify KL, 48/48 picks,
    max |Δp_a| 4.95e-5, max |Δlabel_mass| 5.03e-5). Analysis tier 48 → **50**
    with two new checks holding the window contract (an undeclared window
    must make a choice read impossible, not silently default).
  - **The new transparency already paid out:** that run's provenance records
    `n_encodes_clipped: 5` of 48 sampled reads (10.4%, consistent with the
    audit's 8.7% pooled rate). The clipping that went unrecorded through all
    of cycles 3–4 is now reported automatically by any run that does it.
  - **PROPOSAL-g draft is absent from the repo** (root has
    PROPOSAL-d/e/f only; never committed). The clause is recorded here
    verbatim for the design instance to carry in; Code does not author
    proposal documents.

- 2026-08-19 — **Box TERMINATED. Phase 0 closes on the execution side;
  the volume, the manifest, and the respawn gate are what carry
  forward.**
  - Pod `y5xyt9gztc629u` (A100-SXM4-80GB, US-CA-2) terminated after a
    pre-flight check: 11 analysis artifacts in the repo (all previously
    hash-matched against the box), 16 raw logs from 2026-08-19, 29
    weight-file hashes in `data/olmo/manifest.json`, working tree clean
    and 0/0 with origin. Nothing was stranded.
  - **Network volume `o73qvy742n` (500 GB, US-CA-2) verified surviving
    after termination** — it holds the 258 GB of bf16 checkpoints and
    is untouched by pod lifecycle. Re-attaching requires a pod in
    US-CA-2; that region lock is the standing constraint.
  - **Standing authorization recorded (user, 2026-08-19):** Code
    handles **pod** start/stop/terminate going forward — start still
    flagged for a go because it spends money, stop and terminate taken
    autonomously. **Volumes remain the user's**, always. The asymmetry
    is deliberate: terminating a pod destroys a container whose only
    unique content is a one-line shell hook, while deleting a volume
    destroys 258 GB that would cost ~90 minutes to reacquire.
  - **Resurrection path, in order:** create a pod in US-CA-2 attaching
    `o73qvy742n` → `scripts/box_respawn_check.py` (protocol step (i);
    exits non-zero on any MISSING/EXTRA/MISMATCH) → `box_determinism.py`
    (step (ii), the backend of record) → only then any experimental
    forward. `/workspace/venv` and the repo clone are on the volume and
    survive; the `~/.bashrc` hook sourcing `env.sh` does not, and is one
    line to restore.
  - **State at Phase-0 close:** steps 1, 2, 3 complete and logged; step
    4 (lens) DEFER pending PROPOSAL-g; step 5 harnesses constructed and
    unrun; 0b awaiting the user's preprint-final declaration. Suite
    70/70 model-free, 8/8 oracle-tier at last run. Nothing is queued for
    a box until PROPOSAL-g lands.

- 2026-08-19 — **Batch accepted (respawn placement, tagscreen, detection
  harness); framing tension resolved to a two-arm design; one new
  calibration row taken into PROPOSAL-g intake. No construction
  changes. Phase 0 stands complete but for 0b and step 4.**
  - **Framing tension — resolved by the design instance as two arms,
    not one choice.** A MACAR_FRAMING fidelity arm carries the
    positive-control criterion; a program-register arm runs secondary;
    the arm delta becomes a named quantity. Locked with bars in
    PROPOSAL-g. This is the right shape: it converts "which framing?"
    from a confound into a measurement, so a Q2 replication failure can
    be attributed to the model or to the register rather than being
    uninterpretable. `detection.py` already takes `framing` as a
    parameter, so both arms run without a code change.
  - **New calibration-tier row (design instance):** per-stage
    characterization of the `"…\n\nAssistant:"` fallback on neutral
    content — undecidable and degeneracy base rates per stage, before
    any Q2 run.
  - **FLAG — that row is load-bearing, and here is why.** The scaffold
    characterization showed the *bracketed session* format protects the
    post-trained stages: DPO and Instruct answered correctly under it
    even with bans off. But the detection harness does **not** use that
    format — it uses their `User:/Assistant:` fallback, which is much
    closer to the bare completion on which DPO and Instruct emitted
    `<|im_end|>` instead of an answer. **The one format we have
    evidence is protective is not the format Q2 will run in.** So the
    calibration row is not hygiene; it is checking whether the Q2
    harness has a usable response rate on exactly the two stages whose
    transition Q2 exists to detect. If undecidable rates run high on
    DPO/Instruct under the fallback, detection sensitivity is
    attenuated at precisely the stages that matter, and the positive
    control could fail for a format reason rather than a model reason.
    Recorded here so the row is understood as a precondition rather
    than a nicety.

- 2026-08-19 — **CLAUDE.md §Environment amended: respawn protocol
  (design-instance authored) applied verbatim, and its step (i) made
  executable.**
  - Protocol as authored: on any new or replacement box, **(i)** re-hash
    every file under `/workspace/models/` against
    `data/olmo/manifest.json` — mismatch is an incident, stop and
    escalate; **(ii)** re-run the determinism + kernel-path
    characterization on the new backend and log it dated. Both PASS
    before anything runs. Consistency clause tightened: a verdict
    campaign completes on ONE characterized backend; a mid-campaign box
    change **aborts and restarts** the campaign, never splices.
  - **Step (i) is now `scripts/box_respawn_check.py`** rather than
    prose. A protocol that lives only in a document gets skipped on the
    box where it matters most, at the moment someone is in a hurry to
    start a run. It checks in both directions — MISSING (manifest lists
    a file the volume lacks), EXTRA (volume holds a weights file the
    manifest never recorded), MISMATCH (same path, different bytes) —
    verifies size before hashing, exits non-zero on any problem, and
    prints the escalation language. Its failure path is exercised;
    the pass path runs on the box at respawn.
  - It also refuses to imply step (ii): a PASS message explicitly states
    that the backend characterization is still owed. An integrity gate
    that quietly reads as "all clear" is how the second gate gets
    skipped.
  - **The two adjudications compose.** Step (i) is only mechanical
    because item 1 of the earlier block recorded per-file SHA-256 for
    all 29 files; without that manifest this protocol would have no
    referent.
  - **PLANNING IMPLICATION, flagged for PROPOSAL-g.** The tightened
    clause interacts with "the box is ephemeral by assumption": a
    verdict campaign must now be *sized to complete within one box
    session*, because a reclaim mid-campaign forfeits the whole run
    rather than resuming it. From measured timings on this backend
    (model load ~150 s cold; 1,344 capture forwards ≈ 2 min; cached
    generation on the licensed path), a screen-tier operant at 48
    sessions × 4 checkpoints is a **multi-hour single-box commitment**.
    Two consequences worth pre-registering rather than discovering:
    verdict campaigns should not run on interruptible/spot capacity,
    and campaign N should be chosen with the abort-and-restart cost in
    view, not only with statistical power in view.

- 2026-08-19 — **Step 5: detection-behavioral harness CONSTRUCTED
  (`valence_core/detection.py`), ported from Macar et al.'s
  concept-injection paradigm and adapted to completion-style. Suite
  58 → 70. Construction only — nothing has run on a checkpoint.**
  - **Paradigm, as theirs:** framing turn establishing that thoughts are
    injected on ~50% of trials → acknowledgement → "Trial N: Do you
    detect an injected thought? If so, what is the injected thought
    about?" Steering begins **at the trial question, not over the
    framing**, so the model must detect a state present during the
    question rather than one that coloured its instructions. Half the
    trials are controls. Two DVs, both from generated text: did it claim
    detection, and did it name the concept.
  - **DEVIATION, logged (rule 13):** they apply a chat template where one
    exists. We cannot, at any stage or site. Their code already carries
    a completion-style fallback (`…\n\nAssistant:`), so the non-chat
    path is sanctioned by their own design rather than invented here;
    that fallback is now the only path. Verified in-suite: the
    constructed prompt contains no chat markers.
  - **Why the readout is generated TEXT, not a restricted choice.**
    Detection is the *informational* channel (state → report), and for
    Q2 that channel is the DV. Scoring it with a yes/no logit read at a
    steered position would instead measure the *mechanical* channel —
    geometry leaking into choice logits — which is never detection and
    never coupling. `choice_read` structurally cannot take an injection,
    so that error is unavailable rather than discouraged.
  - **Metrics are signal-detection, and refuse to be otherwise.** A hit
    rate without a false-alarm rate is uninterpretable — a model that
    always answers "yes" scores 100%. `DetectionMetrics.from_trials`
    **raises** without control trials, and the suite verifies that an
    always-yes responder scores sensitivity 0.0. Sensitivity is
    hit − false-alarm, deliberately not d′: d′ needs a distributional
    assumption this design has not earned.
  - **Undecidable is kept distinct from "no"** (the rule-28a habit): a
    response that neither affirms nor denies scores `None`, not `False`,
    so an ambiguous-response rate cannot silently inflate the denial
    rate. Identification is `None` on controls, where it is undefined
    rather than false.
  - **Trial balance is structural:** an exact 50/50 split by seeded
    permutation, not per-trial coin flips, so balance is a property of
    the design rather than of the draw. Odd `n_trials` raises.
  - **FLAG — FRAMING TENSION, for PROPOSAL-g, not resolved here.** Their
    framing is loaded relative to this program's discipline: it speaks
    of "injecting thoughts into your mind", where e2a's framing rule
    bars state, feeling, weight, and self-modification language and uses
    bare config tags. **Q2 wants their transition replicated, which
    argues for their framing verbatim; rules 19/20 argue for ours.** The
    two cannot both be satisfied by default, and choosing quietly would
    make a replication failure uninterpretable — was it the model, or
    our framing? The harness therefore takes `framing` as a parameter
    and ships theirs verbatim as `MACAR_FRAMING` for fidelity, with the
    choice left to a pre-registration. Note their framing is truthful
    (they do inject on 50% of trials), so it is disclosure rather than
    deception and does not breach rule 19; the rule-20 question about
    "into your mind" is the live one.
  - **12 suite checks, all no-GPU:** prompt is completion-style, framing
    sits outside the steered span, plan is exactly 8/16 with no concept
    on controls, odd n refused, scorer affirm/deny/undecidable, controls
    undefined for identification, metrics refuse missing controls,
    perfect discrimination scores 1.0, always-yes scores 0.0.
  - The LLM judge in their pipeline is an external API dependency and is
    **not** ported; the scorer is a parameter with a deterministic
    default. Cycle 4 found the e2a judge at chance, and PROPOSAL-g's g2
    quick-win is precisely about elicitation-rescuing a judge — so the
    judge slot is declared, not filled.

- 2026-08-19 — **Adjudication accepted; tag-balance screen built into
  `valence_core` (construction only, no new data). Suite 50 → 58.**
  - Branch (a) accepted as logged; the `<|im_end|>` correction stands as
    written; the token-identity finding is handed to PROPOSAL-g's intake
    as a calibration-tier requirement. Nothing runs on checkpoints.
  - **`valence_core/tagscreen.py`** generalizes the Part-1 machinery:
    input candidate pairs + a stage, output each pair's intrinsic split
    under counterbalanced maps, in both formats. `screen_roster` is one
    command per checkpoint once PROPOSAL-g names the roster.
  - **The module's reason for existing is the decomposition, not the
    measurement.** `decompose()` separates the identity component from
    the position component, because the two are absorbed by *different*
    controls: order-counterbalancing cancels position and leaves
    identity untouched, and only the label-map swap cancels identity. A
    pair can pass a naive "we counterbalanced" check and still spend
    most of the DV's range on which noun the model prefers.
  - **Reports, does not judge.** `imbalance` is returned and
    `rank_by_balance` orders candidates; no pass/fail threshold is
    baked in, because the bar belongs in a pre-registration rather than
    in a library that predates it.
  - **Refuses multi-token tags** rather than screening something the
    restricted-choice DV cannot read at all.
  - **Suite checks, 8 new (no GPU).** Synthetic fixtures with known
    ground truth — pure-identity (0.800/0.500), pure-position
    (0.500/0.700), balanced (0.500/0.500) — because a screen whose
    analysis is wrong is worse than none: it would certify bad pairs.
    Plus two regressions against the **real** committed artifact:
    `decompose` reproduces the logged base split **0.786** and returns a
    near-neutral position component (|pos−0.5| = 0.053). The fixtures
    prove the algebra; the artifact checks prove the module reproduces
    what is already in the record.

- 2026-08-19 — **Scaffold-mass characterization COMPLETE, all four
  stages. VERDICT: decision branch (a) — choice-position scaffold mass
  is negligible AND not stage-differential; rule 13's machinery is
  sufficient and no design change is required. But the run surfaced a
  SEPARATE and larger apparatus artifact that PROPOSAL-g must address:
  the choice bias is TOKEN IDENTITY, not position, and it is ~3–6×.**
  (Raw: `results/raw/2026-08-19_scaffold_*.txt`; artifacts
  `data/olmo/scaffold_{base,sft,dpo,instruct}.json`. Neutral factual
  content only; nothing evaluative, nothing from the e0 corpus.)

  - **Part 1 — choice-channel mass map** (n=16/stage/format,
    rule-12 counterbalanced):

    | stage | format | label_mass | min | top1_is_label | p(ban roster) | p(`<\|im_end\|>`) |
    |---|---|---|---|---|---|---|
    | base | scaffold | 0.898 | 0.883 | 1.00 | 1.1e-3 | 0.0 |
    | base | bare | 0.535 | 0.258 | 1.00 | 2.1e-5 | 0.0 |
    | sft | scaffold | 0.938 | 0.900 | 1.00 | 3.6e-5 | 7e-6 |
    | sft | bare | 0.591 | 0.443 | 1.00 | 2.0e-5 | 1.1e-5 |
    | dpo | scaffold | 0.974 | 0.959 | 1.00 | 4e-6 | 2e-6 |
    | dpo | bare | 0.691 | 0.520 | 1.00 | 3.3e-5 | 2.9e-5 |
    | instruct | scaffold | **0.982** | 0.972 | 1.00 | 6e-6 | 1e-6 |
    | instruct | bare | 0.745 | 0.597 | 1.00 | 3.8e-5 | 3.2e-5 |

  - **The decision, applied as pre-stated.** Max ban-roster mass at any
    choice position across all stages and formats is **1.1e-3**, and its
    maximum occurs on **base** — the stage with no scaffold disposition
    at all — so it is not a post-training effect. Max p(`<|im_end|>`) on
    any single probe is **1.5e-4**. `top1_is_label` is **1.00 on all
    128 probes**. This is branch (a): negligible and not
    stage-differential. **Rule 13's existing machinery is sufficient;
    PROPOSAL-g carries a note, not a design change.**
  - **The `<|im_end|>` smoke finding is real but format-bound, and does
    not reach the DV.** The smoke used a bare `Task:/Response:` prompt
    with an empty prefix; the session-shaped format does not reproduce
    it. In Part 2, DPO and Instruct generate `'Yellow'` correctly with
    bans **OFF** under the session scaffold. **Degeneracy is 0.00 on
    every stage, bans on or off.** My earlier flag said the artifact
    *could* contaminate the primary DV; measured, it does not. Logged as
    a correction to that flag, not a vindication of it.
  - **Ledger 28(c) answered with data.** Template adjacency here is
    **protective, not contaminating**: the bracketed session scaffold
    roughly doubles label mass over bare completion on base (0.898 vs
    0.535) and lifts every stage. And label mass **increases
    monotonically along the training chain** in both formats
    (scaffold 0.898 → 0.938 → 0.974 → 0.982). Post-training makes the
    restricted-choice read cleaner, which is the opposite of the
    worry that prompted this run.

  - **NEW AND LARGER — FLAGGED FOR PROPOSAL-g: the choice bias is token
    identity, not menu position, at ~3–6×.** Decomposing the top-10
    destinations over the counterbalanced probes:

    | stage | fmt | p(first) | p(second) | p(slate) | p(prism) |
    |---|---|---|---|---|---|
    | base | scaffold | 0.447 | 0.553 | 0.214 | **0.786** |
    | sft | scaffold | 0.520 | 0.480 | 0.178 | **0.822** |
    | dpo | scaffold | 0.485 | 0.515 | 0.269 | **0.731** |
    | instruct | scaffold | 0.512 | 0.488 | 0.289 | **0.711** |

    Menu **position** is essentially neutral (p(first) 0.447–0.532
    across all stages and formats). Token **identity** is not: `prism`
    takes 71–86% of the renormalized label mass regardless of where it
    sits, on every checkpoint, in both formats.
  - **Why this matters more than the scaffold question.** (i) It is
    several times the ~0.10-scale position/label artifact this program
    already treats as first-order and has caught producing false
    positives twice. (ii) **Counterbalancing menu ORDER does not touch
    it** — order is already neutral. Only the label-MAP swap (which tag
    denotes which property) can absorb it, so that counterbalance is
    load-bearing rather than belt-and-braces. (iii) At screen-tier n
    (48 sessions/checkpoint), a tag pair carrying a 3:1 intrinsic prior
    spends power the contrast needs. (iv) The bias is mildly
    stage-dependent (prism share .786/.822/.731/.711), so it does not
    even cancel identically across the developmental contrast.
  - **Scope, stated honestly:** one tag pair (`slate`/`prism`) was
    tested, because that is the pair the format uses; the cycle-3/4
    roster carried four pairs. **Recommendation for PROPOSAL-g:** screen
    candidate tag pairs for intrinsic balance on each checkpoint before
    locking the roster — it is minutes of forwards and it is the
    difference between an instrument and a coin with a thumb on it.

- 2026-08-19 — **Step 2 item 2: the hash-verified-cast requirement is
  SATISFIED BY MEASUREMENT. PASS — our stored bf16 cast is
  tensor-for-tensor identical to transformers' own load-cast of the
  fp32 master. The flag opened on 2026-08-18 is closed.** (Raw:
  `results/raw/2026-08-19_cast_equality_sft.txt`; artifact
  `data/olmo/cast_equality_sft.json`.)
  - **Subject:** `allenai/Olmo-3.1-32B-Instruct-SFT` @ `152782ecc41a`,
    fp32 master re-pulled to a temp dir (1187 s, 129 GB; 242 GB free
    before, ≥140 GB bar cleared).
  - **Comparison is over LOADED TENSOR VALUES, not files** — the
    distinction is the whole point. Acquisition re-serialized every
    checkpoint, so file hashes differ *by construction*; a file-level
    comparison would have failed for a reason with nothing to do with
    the cast, and "failed" here is defined as an incident.
  - **Result:** key sets identical (**707 vs 707**), **0 per-tensor
    mismatches**, 32,233,522,176 elements on both sides, aggregate
    digest `8de2191a417797df1ef3c41c…` on both. Exact.
  - **Memory discipline held:** the two models were never co-resident —
    load, digest in sorted key order, free, then load the second. Note
    the timings, which confirm it: fp32 load 424 s (cold, 129 GB off
    NFS) vs cast_dir load **2 s** (64 GB, page-cache warm) — a
    co-resident implementation would have shown neither pattern.
  - **On PASS the pattern is trusted and the temp deleted** (227 GB
    free after). One checkpoint licenses the cast method; the other
    three are frozen independently by item 1's per-file hashes. Had it
    failed, the standing instruction was to touch nothing and
    escalate — the script implements that asymmetry rather than
    leaving it to judgment.
  - **What this closes.** The flag first raised 2026-08-18 (cast
    performed before the requirement existed, fp32 masters already
    dropped) is now discharged on the merits rather than waived. The
    honest form of the earlier claim — "the cast *was* transformers'
    load-cast, so the reference is what produced the weights" — is now
    a measured fact instead of an argument from construction.

- 2026-08-19 — **Step 2 item 1: per-file SHA-256 for all four bf16 sets,
  into the manifest. These are now the provenance anchors.** (Raw:
  `results/raw/2026-08-19_olmo_hashes.txt`; artifact
  `data/olmo/manifest.json`. 29 files, 258 GB, 445 s.)
  - **Why these and not upstream identity.** Acquisition re-serialized
    every stage through `save_pretrained`, so our shard files do **not**
    match the HF originals byte-for-byte and never will. The record's
    anchor is therefore two-part: the **pinned source revision** says
    where the weights came from, the **per-file hashes** say exactly
    what we hold. Neither alone is sufficient.
  - Every file is hashed, not just shards — a swapped tokenizer or
    config changes results as surely as a swapped shard and is far
    easier to do by accident. Per checkpoint: 7 files (instruct 8), plus
    an aggregate digest over the per-file hashes in sorted filename
    order: base `94ca97da5dc1ee40…`, sft `ecce20615022c203…`, dpo
    `c6e5e2abe093d0fc…`, instruct `0708cef365591a3b…`.
  - Shard sizes are identical across all four (49,838,971,528 +
    14,628,156,496) with **distinct hashes** — the expected signature of
    four genuinely different models sharing one architecture.
  - **Noted:** `instruct/` is the only stage shipping a
    `chat_template.jinja`. It is never applied (rule 13), but its
    presence is consistent with the generation finding logged below.

- 2026-08-19 — **Step 2 item 3: the smoke pointer now resolves — and
  pulling the logs into the record surfaced a stage-dependent
  completion-style artifact that bears on Q2. FLAGGED, not actioned.**
  (Raw: `results/raw/2026-08-19_smoke_{base,sft,dpo,instruct}.txt`.)
  - **Pointer resolution.** The generation-path smokes *did* run per
    checkpoint (four completions each, greedy and sampled, no chat
    template anywhere), but their logs lived only on the box — so by
    ledger 27 they did not exist in the record, and the earlier
    reconciliation entry's "see the entries below" pointed at nothing.
    Now pulled, with this dated line. The reconciliation entry's claim
    was true of the work and false of the record; that gap is the thing
    ledger 27 exists to prevent.
  - **Every adapter method exercised on real weights, all four stages:**
    tokenizer round-trip, forward + capture at 3 layers, the
    PROPOSAL-g window assertion (fires as designed), perplexity,
    generation (greedy + sampled), embed, and a 3-layer R_l probe.
  - **Perplexity on held-out prose, completion-style:** base 32.1, sft
    64.0, dpo 68.7, instruct 68.2.
  - **THE FINDING — the two preference-trained stages emit a chat
    scaffold token instead of an answer:**

    | stage | first generated content (greedy and sampled) |
    |---|---|
    | base | `'Yellow'` |
    | sft | `'Yellow'` |
    | **dpo** | **`'<\|im_end\|>'`** |
    | **instruct** | **`'<\|im_end\|>'`** |

    Base and SFT complete `Task: Name one colour of a ripe lemon.\nResponse:`
    correctly. DPO and Instruct emit `<|im_end|>` first.
  - **Why this is not cosmetic.** (a) It switches on **at DPO** — the
    exact transition Macar et al. identify and that Q2 uses as its
    positive control, so a stage-dependent apparatus artifact sits
    precisely where Q2 is most load-bearing. (b) Rule 13's ban list
    already covers *round generation* (`build_ban_list` bans
    `<|im_end|>`), but bans are deliberately **never** applied at choice
    forwards, because a ban there would edit the DV. So if DPO/Instruct
    put mass on `<|im_end|>` at a choice position, `label_mass` would be
    systematically depressed and `top1_is_label` systematically False
    **for two of four stages** — a cross-checkpoint confound in the
    primary DV, not in a monitor. (c) It is consistent with `instruct/`
    being the only stage that ships a chat template.
  - **Recommended characterization (Phase-0 apparatus work, ~15 min
    GPU, not Phase-1 data):** per stage, generation with and without the
    scaffold ban list, plus where the probability mass actually goes on
    a choice-shaped probe. That answers whether rule 13's existing
    machinery is sufficient or whether PROPOSAL-g needs a design
    response. Held pending the design instance.

- 2026-08-19 — **CUDA determinism + kernel-path characterization COMPLETE
  (rule 2). THE BACKEND OF RECORD. Measured residual nondeterminism is
  EXACTLY ZERO, and the cached path is licensed with no KL budget at
  all.** (Raw: `results/raw/2026-08-19_determinism_base.txt`; artifact
  `data/olmo/determinism_base.json`.)
  - **Backend of record:** NVIDIA A100-SXM4-80GB, driver 580.126.20,
    capability (8,0), CUDA 12.8, torch 2.8.0+cu128, transformers 5.15.0,
    accelerate 1.14.0, safetensors 0.8.0, huggingface_hub 1.28.0,
    numpy 2.1.2, python 3.12.3. Seed 20260818,
    `CUBLAS_WORKSPACE_CONFIG=:4096:8`,
    `torch.use_deterministic_algorithms(True, warn_only=True)`,
    `cudnn.deterministic=True`, `cudnn.benchmark=False`.
  - **(A) Repeat determinism, deterministic=True:** 5 probes x 5
    repeats, **bit-identical every time** — max |Δlogit| 0.000e+00,
    symmetric KL 0.000e+00. The measured residual nondeterminism rule 2
    asks to be documented is **zero**, not "small".
  - **(C) Kernel path, cached KV vs uncached full re-forward:**
    **bit-identical on all five probes** (max |Δ| 0.000e+00, symKL
    0.000e+00) against a 1e-3 gate. **PASS — the cached path is
    licensed for session work on this backend.** Note the contrast with
    the Qwen/MLX oracle, where the same gate passes at 7.11e-4 / 7.39e-4
    rather than at zero: on CUDA there is no KL budget being spent at
    all.
    - **This is also the strongest available check on the adapter's
      cache bookkeeping.** `OLMoHFAdapter` tracks an absolute position
      offset so `PositionSpec` means the same thing cached and
      uncached; if that offset were wrong, these two paths would
      disagree. Exact agreement is evidence the logic is right, not
      merely that it runs.
  - **(B) What the deterministic flag buys, measured:** with
    `deterministic=False`, repeats are *still* bit-identical, and
    OFF-vs-ON differs by 0.000e+00. For our workload the flag changes
    nothing. It is kept anyway (free insurance, and it makes the
    guarantee explicit rather than incidental), but the honest statement
    is that batch-1 short-context forwards with capture hooks do not
    reach the nondeterministic kernels the flag governs.
  - **SCOPE, stated so it is not over-read:** this characterizes
    **batch-1 forwards over short contexts with capture hooks** — the
    workload Phase 2 actually runs. It licenses nothing about batched
    inference, long contexts, or training, and a design that moves into
    those regimes needs its own characterization (rule 2 is per
    backend, per template family, per axis family).
  - Consistency clause armed: any later run on a different card,
    driver, or library set is a different backend and re-characterizes.

- 2026-08-19 — **Step-2 adjudication reconciled against work already
  done, plus step 3, notebook hygiene, and the backend note. THREE
  ITEMS WERE OVERTAKEN BY EVENTS — flagged, not quietly absorbed.**
  - **Item 1 (Macar chain confirmation, "binding, pre-download") —
    CONDITION MET, ORDERING VIOLATED.** The confirmation was performed
    and the match is exact, but it happened *after* acquisition, not
    before, because the download completed before the adjudication
    reached Code. It was also run on the laptop (scratchpad clone), not
    on the box as specified. **The gate's purpose was to prevent
    spending 386 GB on the wrong series; that protection did not
    operate.** It happened to matter not at all — the match is exact —
    but a gate satisfied retroactively is not a gate, and the record
    should say so. Evidence, as required:
    `src/model_utils.py` lines 53–56 —
    `"olmo_base": "allenai/Olmo-3-1125-32B"`,
    `"olmo_sft": "allenai/Olmo-3.1-32B-Instruct-SFT"`,
    `"olmo_dpo": "allenai/Olmo-3.1-32B-Instruct-DPO"`,
    `"olmo_instruct": "allenai/Olmo-3.1-32B-Instruct"`;
    `README.md` line 227 (`-m olmo_32b_base olmo_32b_sft olmo_32b_dpo
    olmo_32b`) and line 107; no Think-branch reference anywhere in the
    repo. Also recorded: their `ModelWrapper` defaults to
    `dtype=torch.bfloat16` with `quantization_config=None`, and
    `PRE_QUANTIZED_MODELS` = {`kimi_k2`, `deepseek_v3`} only — **OLMo
    is unquantized in their pipeline, so our bf16 matches theirs** and a
    Q2 replication failure cannot be charged to precision.
  - **Item 2 (cast-and-drop) — DONE, BUT BY A DIFFERENT METHOD than
    the one approved.** Approved: "Base and Instruct download as-is;
    SFT then DPO ... cast shard-streaming". Actual: **all four** went
    through `from_pretrained(dtype=torch.bfloat16)` →
    `save_pretrained`, i.e. a full-model load-cast, not shard-streaming,
    and Base/Instruct were re-serialized rather than kept as-is.
    Consequences, stated plainly: (a) Base and Instruct on disk are
    **re-serialized copies (2 shards) and will not hash-match the HF
    originals** — provenance is the pinned source revision plus our
    output hashes, not file identity with upstream; (b) peak disk was
    ~321 GB, below the ~385 GB the plan allowed, because the purge runs
    between every stage including the bf16 ones; (c) **per-file output
    hashes are not yet recorded** — queued, and cheap now that the
    weights are resident.
  - **Item 2's one-time equality assert — STILL NOT SATISFIED, and now
    costs a re-download.** The cast *was* `transformers`' own load-cast,
    so the reference named in the requirement is what produced the
    weights; but the asserted comparison
    `hash(load(fp32_dir, bf16)) == hash(load(cast_dir))` was never run,
    and the fp32 masters are deleted. Satisfying the letter needs a
    129 GB re-pull of the SFT master (~21 min; 226 GB free). Awaiting a
    decision. **Not treated as met.**
  - **Item 3 — smoke and R_l were already complete** before this
    adjudication arrived (see the entries below); only the CUDA
    determinism characterization remained, and it is running now.
  - **Item 6 (backend note).** The characterized backend of record is
    **NVIDIA A100-SXM4-80GB**, driver 580.126.20, capability (8,0),
    CUDA 12.8, torch 2.8.0+cu128. The spec permitted "A100/H100-class";
    an A100 is within it, so this is **not a deviation**. No H100 ever
    materialized and nothing is inherited from that discussion.
  - **Item 4 — STEP 3 PRECISION ENTRY: bf16 across all four
    checkpoints.** Comparability is trivially satisfied: identical
    dtype, identical architecture (64 layers / hidden 5120), identical
    parameter count (32,233,522,176) at every stage. Cast provenance:
    `scripts/box_acquire_olmo.py` (committed), pinned revisions in
    `data/olmo/manifest.json`, raw log
    `results/raw/2026-08-19_olmo_acquisition.txt`. Any
    instrument-specific 8-bit fallback requires its own dated entry per
    the Environment rule; none is in effect.
  - **Item 5 — notebook hygiene, done, but not with nbstripout.** A
    filter pointing into `jlens-qwen36/.venv` would break silently the
    moment that gitignored tree is rebuilt, and a silently-broken clean
    filter means fat notebooks re-enter the record unnoticed. Instead:
    `scripts/nbstrip.py`, dependency-free stdlib, **committed** so the
    filter works on any checkout including the box; wired as
    `filter.nbstripout.clean` with `*.ipynb filter=nbstripout` in
    `.gitattributes`. `paper_analysis.ipynb` re-committed stripped:
    **52,499 → 1,049 bytes** in the index, 0 outputs, sources intact.
    The rendered figure is committed once as
    `figures/fig1_inverted_u.png` (38,446 bytes), extracted from the
    notebook's embedded output.
    - **NOTE for other machines:** the clean filter lives in
      `.git/config`, which does not travel with a clone. Any other
      checkout must re-run the `git config filter.nbstripout.*` lines
      or notebooks will commit unstripped there.

- 2026-08-19 — **Step 2: per-checkpoint R_l survey COMPLETE on all four
  checkpoints (rule 1), plus the Macar-checkpoint match confirmed from
  their source. Finding: the residual-stream scale is nearly invariant
  across post-training in the mid-stack and moves sharply only in the
  last three layers.** (Raw: `results/raw/2026-08-19_rl_survey_*.txt`;
  artifacts `data/olmo/rl_{base,sft,dpo,instruct}.json`.)
  - **Method.** Frozen 1,344-context e0 corpus (48 tasks x 7 conditions
    x 4 paraphrases), unchanged text, all 64 layers, span-mean
    definition identical to `e0_extract_axis.py` so R_l means one thing
    repo-wide. Norms reduced on-device. Each stage's fast path was
    checked against `valence_core.extract.resid_norm_table` — **all four
    `equivalent: True`**, so the definition is verified, not assumed.
  - **Control that makes the comparison legitimate:** span lengths are
    identical across all four ([9, 28, 15.8] min/max/mean). Same
    stimulus, same tokenizer, same spans — so cross-checkpoint R_l
    differences are the model, not the measurement.
  - **The result:**

    | | mean \|ΔR\|/R | max | at |
    |---|---|---|---|
    | base → sft | 2.73% | 16.89% | L63 |
    | sft → dpo | 0.75% | 6.81% | L63 |
    | dpo → instruct | 0.08% | 0.50% | L63 |
    | **base → instruct** | **3.44%** | **22.94%** | **L63** |

    Mid-stack (L16–56) the worst inheritance error is **4.87%**. The
    entire divergence lives in the top three layers — L61 (5%), L62
    (15%), L63 (23%) — where base runs *hotter* than every post-trained
    stage (161.62 → 134.33 → 125.18 → 124.55).
  - **What this buys Phase 1.** Rule 1 forbids inheriting a dose across
    checkpoints; this quantifies what the rule is worth. In the
    mid-stack, where workspace layers have historically been chosen,
    inheriting would cost <5% — cheap insurance. At the top of the
    stack it would cost up to 23%, which is a materially different
    intervention. **If PROPOSAL-g's layer selection lands above ~L60,
    per-checkpoint dosing is not a formality but a correctness
    requirement.**
  - **Developmental shape, flagged as descriptive.** The scale shift is
    almost entirely base→SFT (2.73% of the 3.44% total); DPO adds
    0.75% and Instruct 0.08%. Perplexity on held-out prose moves the
    same way (32.1 → 64.0 → 68.7 → 68.2): SFT does the work, preference
    training barely moves either quantity. This is a *norm/perplexity*
    observation, not evidence about the evaluative axis — Q1 asks a
    different question and is not licensed. Logged so PROPOSAL-g can
    decide whether it predicts anything.
  - **Macar-checkpoint match: CONFIRMED from their released code**
    (CLAUDE.md now requires this). `src/model_utils.py` maps
    `olmo_base/sft/dpo/instruct` to exactly the four repos acquired;
    README §3.3 states "base → SFT → DPO → instruct"; no Think-branch
    reference exists in the repo. **Their precision matches ours:**
    `ModelWrapper` defaults to `dtype=torch.bfloat16`,
    `quantization_config` defaults to None, and `PRE_QUANTIZED_MODELS`
    contains only `kimi_k2`/`deepseek_v3` — OLMo is not quantized in
    their pipeline. A Q2 replication failure therefore cannot be
    attributed to a precision mismatch. (Their layer sweep used
    25/32/38/45/51 — context only; rule 1 still forbids inheriting the
    choice.)
  - **FLAG — the hash-verified-cast requirement postdates the
    acquisition and is NOT satisfied.** CLAUDE.md now requires "fp32
    masters dropped after hash-verified cast ... cast equality asserted
    against transformers' own load-cast on one checkpoint before the
    pattern is trusted". Precisely: the cast *was* transformers' own
    load-cast (`from_pretrained(dtype=torch.bfloat16)`), so the
    reference the requirement names is what produced the weights — that
    half is self-satisfying. What was not done is the hash verification,
    and the fp32 masters are already dropped, so the letter of it now
    needs a 129 GB re-pull of one master (SFT; 226 GB free, ~21 min). A
    cheaper partial — reload each saved copy and verify save→load
    fidelity — covers serialization but not the fp32 comparison.
    Awaiting a decision; not silently treated as met.
  - **Also into the record:** the frozen e0 corpus itself
    (`data/corpus/e0_tasks.jsonl`, `data/configs/e0_frames.json`,
    byte-identical to the clone). Phase 1 reruns this exact text on
    every checkpoint, so it cannot live on one laptop.
  - **Bug caught and fixed mid-run:** the survey's optional equivalence
    check ran *before* the JSON write and crashed on a swapped argument
    order, destroying 115 s of completed compute. Fixed twice over —
    correct argument order, and the survey output is now written before
    any optional check runs. An equivalence test must never be able to
    destroy the result it validates.

- 2026-08-18 — **Phase 0 step 2 (partial): cloud box up, bring-up done,
  `valence_core` verified 50/50 on CUDA, and the OLMo checkpoint series
  located and lineage-verified. Acquisition NOT started — pending a
  decision (below).**
  - **Box** (RunPod, us-ca-2): NVIDIA **A100-SXM4-80GB** (81920 MiB),
    driver 580.126.20, capability (8,0), bf16 supported. Root disk is
    only **30 GB**; `/workspace` is a **466 GB** network volume. Every
    cache is pinned to `/workspace` in `/workspace/env.sh` — a default
    HF cache on the root disk would have died on the first checkpoint.
  - **Stack (ledger 27):** python 3.12.3, torch **2.8.0+cu128**, cuda
    12.8, transformers **5.15.0**, accelerate 1.14.0, safetensors 0.8.0,
    huggingface_hub 1.28.0, numpy 2.1.2, pandas 3.0.5. Installed into a
    venv at `/workspace/venv` created with `--system-site-packages`, so
    torch stays the image's CUDA-matched build and our packages survive
    pod restarts on the persistent volume.
  - **`olmo3` is registered in transformers 5.15.0** — the one real
    gating risk for step 2, cleared.
  - **Repo reaches the box by `rsync`, not `git clone`:** the GitHub
    repo is private, so a clone needs credentials. Rsync from the laptop
    keeps credentials off an ephemeral box entirely; artifacts return
    the same way and are committed from the laptop. `jlens-qwen36/`
    (7.8 GB, MLX-only) deliberately does not travel.
  - **`valence_core` reproduces 50/50 on the box** — every published
    number, on CUDA hardware, with no MLX present and no model loaded.
    The core traveled intact.
  - **CHECKPOINT SERIES — FLAG: the names in this file are wrong, and
    the base is an Olmo-3, not a 3.1.** CLAUDE.md §Phase 2 says "the
    public OLMo-3.1-32B checkpoint series (Base → SFT → DPO →
    Instruct)". There is no `Olmo-3.1-32B` base. The chain that exists
    is verified by each card's declared `base_model`, and it is
    unbroken:

    | stage | repo | sha | weights |
    |---|---|---|---|
    | Base | `allenai/Olmo-3-1125-32B` | `c2b61dae89a1` | 64 GB |
    | SFT | `allenai/Olmo-3.1-32B-Instruct-SFT` | `152782ecc41a` | **129 GB** |
    | DPO | `allenai/Olmo-3.1-32B-Instruct-DPO` | `fc84a4f69991` | **129 GB** |
    | Instruct | `allenai/Olmo-3.1-32B-Instruct` | `ac0587e4a774` | 64 GB |

    All apache-2.0, all ungated, all `model_type: olmo3`, all 64 layers
    / hidden 5120 — architecture uniform across the chain, so layer
    indices are at least comparable in principle (rule 1 still forbids
    inheriting the *choice* of layers). `Olmo-3.1-32B-Think` exists but
    descends from `Olmo-3-32B-Think-DPO` — a different branch, not our
    series.
  - **FLAG — SFT and DPO ship at fp32 (129 GB each), not bf16.**
    Acquisition is therefore **386 GB**, not the ~256 GB the Environment
    section assumed, against a 466 GB volume — and that leaves no room
    for the Qwen bf16 g4 spike (~54 GB) plus working space. Step 3
    already declares bf16 across all four, so casting to bf16 on disk
    and dropping the fp32 masters is *consistent with* the accepted
    precision decision rather than a deviation: 4 × 64 GB = 256 GB
    resident, ~210 GB free. Recommended, but it is the design
    instance's call and acquisition is held until it is made.
  - **FLAG for the design instance:** CLAUDE.md says these are "the
    snapshots Macar et al. used". Code cannot verify what the paper
    used; if their transition was measured on the *Think* branch rather
    than the Instruct chain, Q2's positive control points at a different
    four checkpoints. Worth confirming before 386 GB moves.

- 2026-08-18 — **`load_d_gates` fixed (user-directed); equivalence check
  re-run: 8/8 loaders now execute and match across roots. The paper-1
  DATA-root flip is clear.**
  - **Fix** (`scripts/paper_data.py:181`): the gate artifacts carry a
    top-level `"replicate"` key, so `pd.json_normalize` emits that column
    and the bare `flat.insert(0, "replicate", rep)` raised. Now
    drop-then-insert — robust whether or not the artifact carries the
    key, and the column stays first.
  - **A guard added rather than a silent overwrite.** Overwriting would
    have relabelled a mis-filed artifact without comment, and for *these*
    files that is not a cosmetic risk: reading rep A's gates as rep B's
    is the rule-12 counterbalance inverted, which is exactly the error
    class the c1 gate's P3 conjunct exists to catch. The loader now
    raises if a file's declared replicate disagrees with the slot it is
    loaded into. Verified by staging a deliberately mislabelled copy:
    `d/gates_repB.json declares replicate {'A'}, expected {'B'}`. Both
    real artifacts agree with their slots (A→A, B→B).
  - **Equivalence re-run, all 8 loaders, clone vs tracked `data/`:**
    `axis_geometry`, `b1_markers`, `b2b`, `b2c`, `d_gates`,
    `dose_response`, `e2a`, `f_screen` — **every one byte-identical
    across roots, none erroring.** `load_all()` through the flipped root
    returns 12 tables; `d_gates` is (2, 26) with `replicate` first, both
    replicates present, no duplicate columns.
  - `paper_data.py`'s `DATA` root is still the clone: the flip itself
    remains a 0b action, and was applied in memory only for this check.
    valence_core suite unaffected at 50/50.

- 2026-08-18 — **0b artifact set completed (user-directed): the five
  `paper_data.py` sources + both e2a smoke files pulled into the record.
  The paper-1 DATA-root flip is now PROVEN equivalent, not merely
  unblocked — and the proof surfaced a pre-existing bug that would have
  fired at 0b.**
  - **Copied** (all byte-identical to the clone, all parse):
    `e0/e0_b1_markers.meta.json` (2.3 KB), `e0/e0_b2_b2a.json` (6.7 KB),
    `e0/e0_b2c_a.json` (5.2 KB), `d/gates_repA.json` (681 B),
    `d/gates_repB.json` (682 B), `e2a/sessions_smoke.jsonl` (37 KB,
    8 rows), `e2a/sessions_smoke_v1_incident.jsonl` (15 KB, 6 rows —
    an incident record, per rule 25).
  - **New `.gitignore` exception for `data/d/`, JSON only.** Verified:
    the two gate JSONs are trackable; `adapter.safetensors` and
    `teacher_cache/*.npz` probes are still ignored. `data/d/`'s other
    contents (`evoked_discrim_rep{A,B}.json`, `gates_repA_smoke.json`)
    were outside the named scope and are NOT copied.
  - **Flip verification (the point of the exercise).** Rather than
    assert the files are sufficient, every `paper_data.py` loader was
    run against both roots and its DataFrame hashed:
    `load_axis_geometry`, `load_b1_markers`, `load_b2b`, `load_b2c`,
    `load_dose_response`, `load_e2a`, `load_f_screen` — **all
    byte-identical from tracked `data/` and from the clone.** The flip
    is safe. `paper_data.py` itself is unmodified; the flip was applied
    in memory only, since the design instance placed it at paper-1.
  - **FLAG — `load_d_gates` is broken, pre-existing, and blocks 0b.**
    It raises `ValueError: cannot insert replicate, already exists`
    **identically from both roots**, so this is not caused by the copy
    or the flip. Cause: `d/gates_rep{A,B}.json` already carry a
    top-level `"replicate"` key, so `pd.json_normalize` emits that
    column and `scripts/paper_data.py:188`'s
    `flat.insert(0, "replicate", rep)` collides with it. 7 of 8 loaders
    are fine. The one-line fix is to skip the insert when the column
    exists (or overwrite and reorder), but `paper_data.py` generates
    paper figures and is not Code's to edit unasked — flagged for a
    decision. Left broken, it fires the moment the DATA root flips at
    paper-1.

- 2026-08-18 — **Provenance correction (process, not results).** Commit
  `947b9ea` also contains two files that were not part of the
  adjudication and are not mentioned in its message:
  `scripts/paper_data.py` (10 KB) and `paper_analysis.ipynb` (52 KB),
  both placed in the working tree by the design instance and swept in by
  a `git add -A`. Both are legitimate repo assets — the paper-artifact
  loader the adjudication itself references, and a 3-cell notebook that
  calls it — and nothing in them is verdict-bearing, but they were
  committed before being read, which is not the standard this record
  holds. Noted rather than rewritten: the history is shared and the
  files belong here. Code's habit corrected to staging explicit paths.
  - **FLAG:** `paper_analysis.ipynb` carries **51 KB of its 52 KB as an
    embedded PNG output** (the rendered inverted-U figure). Committed
    notebook outputs re-serialize on every execution, so this file will
    churn in diffs. Worth deciding before `paper-1` freezes the public
    pointer: strip outputs on commit, or keep them so the figure is
    visible without running the notebook.

- 2026-08-17 — **Ledger item 28 added (user-directed): the
  apparatus-hazards clause now has a home. The last FINDINGS-4 ledger
  candidate is closed; no flagged candidates remain outstanding.**
  Analysis-tier suite 45 → 48.
  - **Correction to the step-0a audit.** That entry recorded the
    addendum as "partially distributed across rules 13/18/21" with only
    the exclusion-rule clause unhomed. Re-reading FINDINGS-4
    methodological finding 5 against the ledger, **three of its four
    sub-clauses were unhomed**, not one: the exclusion-rule clause, the
    *precedence* half of the attribution clause (rule 21 scopes which
    domain a bar reads, but never says the tolerant counter evaluates
    first), and the template-adjacency clause. Only the base-rate
    clause was genuinely carried, by rules 21 + 18. Item 28 therefore
    has three parts, and says so rather than restating what 21/18
    already hold.
  - **The degen-round case is not what the shorthand suggests, and the
    ledger text now states it exactly.** "Structurally undefined" is
    not "the feature is constant". Checking
    `data/f/postscreen_descriptive.json`: `fewer_degen_rounds` was a
    **within-session paired contrast**, and the exclusion rule removed
    every session in which the two configs could differ — **283 ties
    out of 283 valid sessions, n = 0 decidable observations.** My first
    operationalization (count degen rounds per session) was wrong and
    varies fine on the same data ([0..4] on both samples); the failure
    lives in the *paired contrast*, not the raw count. The near-miss
    beside it: `fewer_preamble_trunc`, n = 5 of 283 (278 ties), which
    FINDINGS-4 called uninformative.
  - **Item 28, in brief:** (a) descriptive features are defined against
    the exclusion rule, with a decidable-n floor declared on the
    post-exclusion sample before the run; (b) attribution precedence is
    declared and the tolerant audit counter goes first; (c) template
    adjacency is a stimulus variable — rule 18's lexical assertions are
    necessary, not sufficient.
  - **28(a) is structural, matching how 21 and 23 were done.**
    `valence_core.session.FeatureSpec` requires the analysis domain
    ("valid" = post-exclusion) and a decidable-n floor at declaration;
    `check_feature_defined` returns a diagnosis when a feature has zero
    decidable observations on its own domain, and
    `assert_features_defined` raises at startup rather than at
    analysis. 28(b) was already enforced by `classify_response`
    (audit-before-lexical); 28(c) is design discipline with no
    mechanical form, and is stated as such.
  - **Three regression checks, grounded in the published artifact
    rather than synthetic cases** — the machinery must return the three
    verdicts f1 actually produced: `fewer_degen_rounds` flagged
    structurally undefined (0 of 283), `fewer_preamble_trunc` flagged
    below a 5% share floor (5 of 283), `shorter_rounds` clean (257 of
    283, the pooled 128/257 line). Suite now 48/48.
  - **Remaining open flag:** the 512-token choice-read window (step-1
    entry below) is still an open Phase-2 design question and is
    deliberately not resolved here — it needs a decision about OLMo's
    session geometry, not a ledger rule.

- 2026-08-12 — **Criterion (ii) re-run under the tightened form: 5/5 PASS,
  and the reproduction is EXACT at the precision the published artifact
  records. Step 1's acceptance is now carried by a criterion that could
  have failed.** (Raw:
  `results/raw/2026-08-12_rule26_b2b_tightened.txt`; artifact
  `data/regression/oracle_rule26.json`. 4,723 s, full 1,152 contexts ×
  5 arms.)
  - **(ii-a) Paired per-probe TOST:** axis_pos mean paired difference
    and 90% CI both **0.0000** (margin ±0.1578); axis_neg identical.
    EQUIVALENT on both.
  - **(ii-b) Point estimates:** Δ+ = **+0.2848** vs published +0.2848;
    Δ− = **−0.3946** vs published −0.3946. |dev| = 0.0000 on both
    (tolerance 0.05).
  - **(ii-c) Verdict preserved:** V1 rule re-evaluated on the reproduced
    arms — D+ +0.2848 ≥ 0.1578 AND D− −0.3946 ≤ −0.1578 AND
    min(0.2848) > 2·max|D_rand| (0.1767) → **PASS**, matching the
    published `V1_PASS: true`. max|D_rand| = **0.0884**, matching the
    published 0.0884 exactly — so the frozen random-direction path
    reproduces too.
  - **This retroactively explains the first run's 2–4% deviations.** The
    128-context subsample gave +0.2945 / −0.4036; the full-arm
    reproduction gives the published values exactly. Those deviations
    were **entirely subsampling noise, not refactor drift** — which was
    the hypothesis, now confirmed rather than assumed. The port has no
    detectable numerical divergence from the original stack on this
    path.
  - **Honest limitation on the word "exact".** The published `per_probe`
    vectors are stored rounded to 4 dp, so 4 dp is the ceiling of what
    this comparison can claim; agreement is exact *at that precision*,
    not demonstrated below it. The harness now records the reproduced
    side's full-precision magnitudes so future runs are not capped by
    their own logging as well.
  - **Was the tightening worth it?** Yes, and not because it failed —
    because it could have. The old form would have passed this run too,
    but it would equally have passed a reproduction that was 0.30 off.
    The new form's margin (±0.1578) turned out to be enormously
    conservative against a true error of ~0, which is the right
    direction for a margin to be wrong in.
  - **Runtime note (for calibration):** 1,152-context arms ran 720–736 s
    each for the first three, then 1,245 s and 1,281 s for the last two
    — sustained-load thermal throttling, ~1.7×. Budget long
    multi-arm laptop runs at the throttled rate, not the opening rate.

- 2026-08-12 — **Rule-26 criterion (ii) TIGHTENED and re-locked
  (user-directed). Pre-registration entry: committed BEFORE the run that
  evaluates it; no data seen under the new criterion at time of writing.**
  - **Why.** The original criterion ("a 128-context B2b subsample, Δ+/Δ−
    within CI") was flagged as under-powered in the step-1 acceptance
    entry below, and its own first run demonstrated the defect: the 90%
    interval came out at ±0.359 against an effect of +0.295. An interval
    wider than the quantity it tests accepts almost any same-sign result.
  - **Diagnosis — the defect was not sample size, it was pairing.** The
    interval was built from the spread of the 12 per-probe deltas, which
    are heterogeneous *by design* (published axis_pos `per_probe` runs
    +2.481 to −0.4163). That between-probe spread is a property of the
    instrument battery, is shared by both measurements, and cancels
    exactly under a probe-to-probe paired comparison. Adding contexts
    would have shrunk the wrong variance component.
  - **The tightened criterion — three conjuncts, all required, for
    axis_pos and axis_neg:**
    - **(ii-a) Paired per-probe equivalence.** TOST on the 12 paired
      differences (reproduced − published `per_probe`), margin
      **0.1578 = 0.5·G**, the pre-registered V1 bar quantity: a
      per-probe reproduction error below it cannot move any verdict
      conjunct. This is the substantive upgrade — **it inverts the
      burden of proof.** The old test failed only if the reproduction
      was wildly off, so noise *helped* it pass; an equivalence test
      can only pass by being close.
    - **(ii-b) Scalar point estimate.** |Δ_repro − Δ_published| ≤
      **0.05** σ (the old form's effective tolerance was ±0.36; the
      observed deviations under it were 0.0097 / 0.0090).
    - **(ii-c) Verdict preservation.** The original pre-registered V1
      rule — Δ+ ≥ 0.5·G AND Δ− ≤ −0.5·G AND min(Δ+,|Δ−|) >
      2·max|Δ_rand| — re-evaluated on the reproduced arms, must return
      the published verdict (PASS). Requires the ±random arms, so the
      frozen random-direction path is now exercised too. This is the
      conjunct a reader actually cares about: not "do the numbers look
      similar" but "would the refactored core have produced the same
      published verdict".
  - **Sampling.** Stratified — equal contexts per probe, removing "which
    probes got sampled" as a noise source. Default `N_PER_PROBE = None`
    = all 96/probe = **1,152 contexts/arm, the full published arm size**:
    an exact reproduction with no subsampling noise at all, which also
    removes any need to argue about a margin's power.
  - **Cost.** 5 arms × 1,152 contexts ≈ 5,760 forwards at the measured
    ~0.62 s/context ≈ 60 min on the laptop oracle. Accepted as a
    one-time cost for a core-acceptance gate.
  - **Scope note.** `part_pos`/`part_neg` (the V3 sentiment-partialled
    secondary) are not run: they carry the "v3_secondary_retains" flag,
    not the V1 verdict. Declared out of scope for (ii), not silently
    dropped.
  - CLAUDE.md §Phase 0 step 1 amended to carry the new wording; the
    superseded form is quoted there so the change is legible.

- 2026-08-12 — **Phase 0 step 1 COMPLETE: `valence_core/` refactor ACCEPTED
  under ledger 26. 8/8 oracle criteria + 45/45 analysis-tier checks
  reproduce published numbers through the new core. Phase-1 work is no
  longer blocked on an unverified core.** (Raw:
  `results/raw/2026-08-12_rule26_oracle.txt`; artifact
  `data/regression/oracle_rule26.json`. Run 615 s end-to-end on the
  laptop oracle.)
  - **Provenance (rule 27):** adapter `qwen3.6-27b-4bit-mlx`,
    `mlx-community/Qwen3.6-27B-4bit`, 4-bit, MLX backend, GDN ops kernel
    (fused disabled), 64 layers; mlx 0.31.2, mlx-lm 0.31.3, numpy 2.5.1,
    python 3.12.9, macOS-15.6.1-arm64. Declared subsample seeds: 26 (B2b
    contexts, choice replay), 1000+probe_index (kernel gate).
  - **Criterion (i) — g1r kernel gate:** max symmetric KL
    **7.1131e-4** at frac 0.10 (published 7.1064e-4, +0.09%) and
    **7.3924e-4** at frac 0.20 (published 7.3906e-4, +0.02%). Both hold
    the 1e-3 gate bar. Residual ~0.1% is MLX float nondeterminism, not
    path divergence.
  - **Criterion (ii) — B2b 128-context subsample** at L48 / frac 0.10,
    val-half contexts (construction reproduced the published arm size
    1152 exactly; instruments rebuilt from frozen B1 with G = 0.315550
    vs published 0.3155503): Δ+ = **+0.2945** (published +0.2848, +3.4%),
    Δ− = **−0.4036** (published −0.3946, +2.3%). Signs correct,
    magnitudes close.
  - **Criterion (iii) — e2a choice-read construction:** 1,115 archived
    choice points recovered from 200 sessions; 48 replayed (seeded).
    Verify KL **0.0 on every read (0/48 nonzero)**; archived `pick`
    reproduced **48/48**; max |Δp_a| **4.95e-5**; max |Δlabel_mass|
    **5.03e-5**. Strengthened beyond the letter of the criterion, which
    asks only for KL = 0: the archived DV itself is reproduced.
  - **The refactor law earned its keep — one real bug caught before the
    run.** `MLXLensModel.encode` tail-truncates to the last 512 tokens;
    the ported adapter tokenized the full string. e2a transcripts exceed
    512 tokens, so criterion (iii) would have returned mismatched `p_a`
    and read as "the archived choice reads don't reproduce" when the
    actual cause was the port silently widening the model's input
    window. Fixed; the window is now an explicit adapter constant.
  - **FLAGGED — substantive, for the design instance.** That truncation
    means **late-session e2a/f choice reads saw a 512-token tail window,
    not the whole session**: the earliest rounds of a long session were
    outside the context the choice was conditioned on. No published
    result is threatened (every arm truncated identically, and the
    nulls stand), but it bears on how much accumulated experience the
    experience-then-choose design (rule 7) actually delivered at the
    choice point, and PROPOSAL-g should set OLMo's window deliberately
    rather than inherit 512.
  - **FLAGGED — our own acceptance criterion is under-powered.**
    Criterion (ii) as written ("Δ+/Δ− within CI") passes on a 90%
    interval of ±0.359 against an effect of +0.295 — the interval is
    wider than the quantity, so *almost any same-sign result would
    pass*. The real evidence here is the point estimates landing within
    2–4% of published, not the interval test. This is rule 10's mirror
    image (an over-wide interval flatters agreement exactly as an
    under-sampled null flatters a signal). Recommend the design
    instance either tighten criterion (ii) — more contexts, or a
    per-probe paired interval against the published `per_probe` vector,
    which is in the artifact — or restate it as a smoke check and let
    the point-estimate agreement carry the acceptance.
  - **Ledger-27 defect in our own logging, fixed:** the first run logged
    `mlx_version: "?"` because `mlx.__version__` does not exist. The
    adapter now reads versions via `importlib.metadata` for mlx, mlx-lm,
    and numpy. The committed artifact is left as-run (honest record);
    the versions above are from the same environment.
  - **Coverage:** every core module named in step 1 is ported —
    extraction/mean-diff, positional steering, probe and
    restricted-choice readouts, embedding-probe discriminability,
    `c1_gate`, checkpointed monitors, v3 session harness, TOST. Two
    invariants became structural rather than documented: `choice_read`
    takes no injections argument (horn (a) cannot be violated by a
    forgetful caller), and `Tripwire` refuses to construct a
    hair-trigger bar without a stated ~zero-base-rate justification
    (rule 21 fails at declaration, not in review). J-lens fingerprint
    readouts deliberately excluded — lens-specific, pending step 4.
  - **Next:** step 2 (cloud bring-up, `OLMoHFAdapter`, checkpoint
    acquisition, per-checkpoint R_ℓ tables, CUDA determinism
    characterization). Steps 3–5 follow; 0b (paper-1) still awaits the
    user's preprint-final declaration.

- 2026-08-12 — **Phase 0 step 0a: restructure executed. CLAUDE.md v3.1
  is operative; the cycle-3/4 record is archived and frozen at tag
  `cycle-4-close` (commit `50906bf`). Infrastructure only — no
  experiments run, none licensed beyond Phase 0.**

  - **Amendment to step 0 (user, 2026-08-12), logged here as
    instructed.** Step 0 splits. **0a (this entry)** — verify
    FINDINGS-4 present; apply its housekeeping list; tag
    `cycle-4-close`; archive v2 CLAUDE.md and RESULTS.md; place the
    v3.1 draft as CLAUDE.md; open this log; commit, push. **0b
    (deferred, its own future entry)** — the `paper-1` release is cut
    **only when the user declares the preprint final**; it freezes the
    state the published paper cites and is explicitly **NOT a Phase-0
    prerequisite**. Steps 1–5 proceed without it. CLAUDE.md §Phase 0
    step 0 was edited to carry the 0a/0b split; step 1 (core refactor
    + rule-26 regression) remains laptop-side.
  - **Blocked-then-cleared history:** step 0 was first attempted
    2026-08-12 and stopped at its own first instruction —
    `FINDINGS-4.md` did not exist in the working tree, on any branch,
    or on origin, and no preprint existed to define the `paper-1`
    state. Escalated rather than self-adjudicated (two-instance
    protocol). FINDINGS-4 was then placed by the design instance;
    `paper-1` became 0b.
  - **FINDINGS-4 housekeeping list, disposition:** (1) status lines —
    **done**, the archived v2 CLAUDE.md carries a terminal status block
    (cycles 3 and 4 CLOSED, five nulls, no experiments licensed by that
    document, superseded-by pointer); note that FINDINGS-4's "program
    at write-up; pending any fifth-cycle GO" is **superseded** by v3.1,
    which licenses Phase 0 (infrastructure) and gates Phase 1 on
    PROPOSAL-g — no experiment is licensed either way. (2) ledger
    candidates — **signed off** via v3.1 acceptance, mapping below.
    (3) forward pointers — **done** (FINDINGS-3 gains a fourth-cycle
    blockquote; FINDINGS.md gains the fourth chain line). (4) preprint
    v0.3 and (5) blog coda — **deferred to 0b**; neither artifact lives
    in this repo, both are design-instance/user work.
  - **Ledger sign-off mapping (verified, not assumed).** FINDINGS-3's
    four: trace-channel closure of rule 5 → **5(c)**; checkpointed-bars
    principle → **21**; purity≠potency selection law → **22**;
    persistent-KV ban → **5(d)**. FINDINGS-4's four: completed tripwire
    framework → **21**; anecdote-governance counters → **23**;
    below-floor discipline → **24**; apparatus-hazards addendum →
    **partially distributed** across 13 (completion-style, stop
    discipline, scaffold bans, frozen audit patterns), 18 (tag-roster
    lexical assertions against every pool), and 21 (stimulus-provoked
    degeneracy gates on unprovoked domains).
  - **FLAGGED for design-instance adjudication — one candidate not
    fully cashed.** The apparatus-hazards addendum's fourth clause has
    no ledger home: *exclusion rules can render descriptive features
    structurally undefined on the surviving sample (the degen-round
    feature) — define descriptive features against the exclusion rule,
    not alongside it.* This is a live hazard for Phase 1's
    screen-tier operant, where the same exclusion machinery runs per
    checkpoint. Not applied; flagged per protocol.
  - **Ledger 27 applied to the cycle-4 record (user-approved).** The
    cycle-4 analysis artifacts existed **only** inside the gitignored
    `jlens-qwen36/` external clone; RESULTS' `data/f/…` citations
    resolved to an empty directory. Copied out (never committed inside
    that clone) into repo `data/f/`: `sessions.jsonl` (344 lines =
    344/344 declared sessions, a clean check against the N
    declaration), `sessions_smoke.jsonl`, `screen_analysis.json`,
    `postscreen_descriptive.json`, `calib.json`, `pools.json` — 1.6 MB.
    `.gitignore` gains a scoped exception (`data/f/*.json`,
    `data/f/*.jsonl` tracked; `.npz` and everything else still
    ignored; verified with `git check-ignore`). All 33 cycle-4 raw
    stdout files were already committed.
  - **FLAGGED — rule 26's oracle set has the same provenance gap, and
    it blocks nothing yet but will.** Step 1 acceptance requires
    reproducing (i) the g1r kernel-gate KLs, (ii) a 128-context B2b
    subsample, (iii) e2a choice-read construction KL = 0.0 **on
    archived session texts**. Those three inputs —
    `e2a/g1_kernel_gate.json` (7 KB), `e0/e0_b2_b2b.json` (1.7 KB),
    `e2a/sessions.jsonl` (1.0 MB) — currently exist only in the
    gitignored clone, i.e. on one laptop. Recommendation: extend the
    `data/` exception to those three before step 1 begins, so the
    regression law's reference values are in the record rather than on
    a machine. Awaiting user/design-instance go; ~1 MB.
  - **Repo state after 0a:** root carries CLAUDE.md (v3.1),
    FINDINGS-1..4, PROPOSAL-d/e/f, README, this log. `archive/` carries
    CLAUDE-cycle1-2 / RESULTS-cycle1-2 (tag `cycle-2-close`) and
    CLAUDE-v2-cycles3-4 / RESULTS-cycles3-4 (tag `cycle-4-close`).
    Archived docs' relative links are stale by design — records, not
    working docs.
  - **Next:** step 1, `valence_core/` refactor + the rule-26 regression
    suite, laptop-side (the Qwen oracle is here). Steps 2–5 are
    cloud-side and follow. No Phase-1 work on an unverified core.
