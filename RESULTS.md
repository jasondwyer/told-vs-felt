# RESULTS — Phase 2

Dated experiment log for Phase 2 (the OLMo-3.1-32B developmental study).
Prior logs, frozen and archived: cycles 1–2 at
[`archive/RESULTS-cycle1-2.md`](archive/RESULTS-cycle1-2.md) (tag
`cycle-2-close`); cycles 3–4 at
[`archive/RESULTS-cycles3-4.md`](archive/RESULTS-cycles3-4.md) (tag
`cycle-4-close`). Synthesis chain: [`FINDINGS.md`](FINDINGS.md) →
[`FINDINGS-2.md`](FINDINGS-2.md) → [`FINDINGS-3.md`](FINDINGS-3.md) →
[`FINDINGS-4.md`](FINDINGS-4.md). Operative design:
[`CLAUDE.md`](CLAUDE.md) (v3.1); Phase 1 is **not** licensed and awaits
PROPOSAL-g plus its pre-registrations.

Conventions unchanged: dated entries, dense, newest-first within a
section; raw stdout worth keeping goes to
`results/raw/YYYY-MM-DD_short-name.txt` and is linked; verdict-relevant
analysis artifacts are committed under `data/` (ledger 27);
design-relevant findings are flagged for discussion, never silently
applied to CLAUDE.md.

## Log — Phase 2

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
