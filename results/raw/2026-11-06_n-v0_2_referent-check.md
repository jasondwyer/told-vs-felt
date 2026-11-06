# PROPOSAL-n v0.2 — §8 steps 1–2: the delta read and the referent check (Code)

*Code's raw, 2026-11-06. The document checked is `PROPOSAL-n-bk-reconciliation-v0_2.md`, sha256
`30a3d0f55a6681e01245f75490d1f7fdf032b4a1f2c6e59684d6a17584b104f4`, as the PI's routing of 2026-11-06 names it.
The grading follows the v0.1 STOP raw's (`results/raw/2026-11-06_n-v0_1_code-to-design_STOP.md`): ✓ means the
referent resolves as the document uses it; **N** marks a minor residue carried as a dated note under the routing's
process line ("minor residues as dated notes (the e9b5022 precedent)"). No item is substantive and unresolved, so
§8 step 3 proceeds.*

## 1. Step 1 — the delta read (report only)

- **HEAD** at the run: `db97d8e`. `origin/main` is `9cbacdb`; the three commits between them (`dc1ffe1`, `71cc23c`,
  `db97d8e`) are local and unpushed.
- **The document.** v0.2 is untracked at root and hashes to the routing's sha256. v0.1 is untracked at root and
  hashes to `9248d06c0837bd7bd0e9ffee2c88a135b2a129d9906b244c85657ac0200fb6a6`, which v0.2's header names.
- **The untracked root**: 28 entries, the same 28 as at the session's start. They are five figure SVGs,
  `ADDENDUM-g3-b2r.md`, `ADDENDUM-g3-b2r-v1.1.md`, `ADDENDUM-k1.md`, six `HANDOFF-*-design.md`,
  `PREPRINT-v1_1-draft.md`, the two PROPOSAL-n files, four `RESEARCH-NOTE-v0_*-draft.md`, six
  `archive/PREPRINT-v1_0-draft.pre-patch-v*.md` and `tvc2_dump.txt`. Of these, the routing names only v0.2. The other
  file it names, the prebuild answers, was committed at `dc1ffe1`.
- **No n artifact exists**: no `data/n/`, `valence_core/n/`, `scripts/n_*` or `LOCK-n*`, and git has no history for
  `data/n` or `valence_core/n`. The only PROPOSAL-n entry is v0.1's STOP (RESULTS.md:225 at `db97d8e`).

## 2. Step 2 — the referent check (§9)

The v0.1 STOP raw §5 resolved most of §9 on 2026-11-06. This check re-reads every referent v0.2 quotes, new or
changed. For a carried referent, it confirms the source is byte-unchanged: `git diff 24ebeae HEAD` is empty for
PROPOSAL-m v1.11, ADDENDUM-m1, PROPOSAL-k, PROPOSAL-g, PROPOSAL-h, LOCK-g, `data/olmo/`, CLAUDE.md and
`valence_core/adapters/olmo_hf.py`. The BK clone sits at the same commit and tree with a clean status, and the PDF
hashes to the same value.

### 2.1 This repository

- **PROPOSAL-m v1.11** (sha256 `42ab36ec…`, as v0.2's header has it):
  - m:6 dating convention ✓;
  - m:48 m's §0.4, "No steering, no adapter, no random direction, no negative pole" ✓, so "does not apply to it"
    holds;
  - m:52 m's §0.6, "Concluded is not answered (rule 5(b))" ✓ (v0.2 §0.6 mirrors it);
  - m:159 the key-to-generator function ✓;
  - m:172 ✓: the line carries "Read: `readout.choice_read(verify=True)` … restricted two-label" — the
    restricted two-label read v0.2 §2.1 cites. Code's groundwork had flagged this anchor from the line's opening
    clause (the schedule balance); the read is later on the same line;
  - m:205 ✓ "a pod session's cold load at SFT, DPO or instruct is 130–200 s";
  - m:251 ✓ (one pod session per campaign; gate stages may span pod sessions; each new box runs the respawn protocol
    and gets its own `BACKEND — characterization` entry);
  - m:267 ✓ (the resume identity carries the pod instance id; the laptop checklist's "one process — no other model
    process running");
  - m:283 ✓ "low label mass (< .20; e2d/runner.py:55–58)" — e2d's low-label-mass reference;
  - m:318 ✓ "VERDICTS are computed by the pre-committed analyzer before any of 'the reads'";
  - m:345 ✓ cites PROPOSAL-h (:165–167) and LOCK-g (:167–170);
  - m:349 ✓ the posting rule.
- **ADDENDUM-m1** (`f26bc59`): decision (16) ✓ (see N3 for §7.4's use of it); §4 step 4, the OLMo track ✓.
- **PROPOSAL-k**:
  - k:111 opens the 5(f) rule text ("**5(f)** [verify — text drafted by the design seat 2026-09-05 …"). The 5(f)
    bullet runs to k:125 ("Full text in Appendix A."), and k:126–127 open the 5(d) bullet. v0.2's k:111–127 is
    C10's two-part locator (the STOP raw's C10: k:111–125 and k:126–127), taken as one span ✓.
  - k:212–213 ✓ (carried); k:226 ✓ "identity assertion EXACT".
- **PROPOSAL-g** g:164–170 and g:165 ✓; **PROPOSAL-h:165–167** ✓; **LOCK-g:167–170** ✓. All carried, the sources
  unchanged.
- **RESULTS.md@18c32df**:
  - :73 ✓ (carried);
  - :7329–7334 ✓ (carried);
  - :7342 ✓ ".68–.71 at L59–L63 (median over the registered L51–L62 band .861";
  - :7436 ✓ "**G3 FAIL:** median over L51–L62 .861 (bar .90)" (C8's correction holds).
- **Data files**: `data/olmo/a3_axes_dpo.json` ✓ and `a5_budget.json` ✓ (carried, unchanged).
  `data/olmo/manifest.json` ✓ has four entries: `base`, `sft`, `dpo`, `instruct`.
- **`valence_core/adapters/olmo_hf.py`** ✓ (carried, unchanged).
- **Ledger (55)'s anchors** ✓ at `9cbacdb` (see N4):
  - `valence_core/m/gcal.py:39–40` reads "G-CAL-OLMo (per checkpoint, b3's banner and generation path) is the OLMo
    track's and is not built here";
  - `scripts/m_sessions.py:491–492` carries the OLMo units' "step-9 track's refusal";
  - the prebuild raw §1 quotes the former.
- **The cited raws** ✓, both committed: the STOP raw and `results/raw/2026-11-06_f3-build_code-to-design_prebuild.md`.
- **CLAUDE.md**: rules 1, 2, 5(a), 5(b), 5(d), 5(f), 9, 11, 12, 13, 19, 21, 23, 25, 27, 28(a) and 28(d), and the
  Environment and Respawn sections, are present at HEAD ✓.

### 2.2 BK, the PDF (sha256 `e92c69cb4ca2e6e1…`, as v0.1's check recorded it; text via macOS PDFKit)

- **§1** ✓ (the fixed-text description: "the turns associated with the conditioned zone to build the KV cache. The
  visible text is therefore identical across all …").
- **§3, Table 1** ✓: carried, and `table1_banks.csv` gives all four OLMo-2-32B stages at layer 32.
- **§3.1** ✓:
  - "a corpus of short passages generated by Claude Sonnet 4.6. Each passage is 2–4 sentences";
  - "56 passages for each of four positive states";
  - "96 affectively neutral passages";
  - "the first ten principal components of the 96 neutral passage representations";
  - the rest is carried.
- **§3.2** ✓ (carried).
- **§3.2.1** ✓: eq. (1) (carried), and, under its heading "Separating the text and hidden-state channels", "To
  construct the unsteered cache, we reprocess the same sequence of tokens without steering" — v0.2 §0.1's
  "unsteered cache".
- **§3.2.2** ✓:
  - the heading "3.2.2 Fixed-text hidden-state design";
  - "turns associated with S";
  - m(c_uns(d)), in the definition of Δm_fixed(d).
- **§4.1** ✓ "We focus on OLMo-2-32B."
- **§4.2** ✓ (carried).
- **§4.3** ✓ "Throughout, we use the transcripts generated by the Instruct checkpoint under steering."
- **Fig. 4 caption** ✓: "The Instruct checkpoint first generated the conditioning text under steering … The same
  steering vector, constructed using the Instruct checkpoint, was applied at the same positions for every checkpoint."
- **Appendix E** ✓:
  - the coherence hurdle's three failure modes, verbatim in content: fewer than four words, more than 50% of trigrams
    repeated, fewer than five distinct words per 20 words;
  - "at least 75% of turns";
  - the arrival hurdle's re-encode, projection and t-test with |t| ≥ 2;
  - "Each hurdle is evaluated separately for both positive and negative doses".
  - BK fix no batch size. G-CAL-n's 48 turns are the document's own, and it does not attribute them to BK.
- **Table A2** ✓: OLMo-2-32B (all stages) 0.30; Qwen2.5-32B 0.30; Qwen3-14B 0.30; Qwen3-32B 0.30.
- **Appendix A** ✓: eight states, each with examples (1) and (2), and none with a third.

### 2.3 BK-repo at `7631f8a` (clone clean; tree `d6f1d505…e282`)

- **`README.md`** ✓:
  - "It does not contain the code that runs the experiments, which loads the models and applies steering, or the
    steering vectors themselves";
  - "we share the experiment code on request rather than publicly";
  - the extension paragraph, "please use the smallest dose and shortest exposure that answer your question, and
    report how much negative steering your experiments involved", which §0.4 paraphrases.
- **`table1_banks.csv`** ✓: `olmo_32b,allenai/OLMo-2-0325-32B-Instruct,32`; `stage_dpo,allenai/OLMo-2-0325-32B-DPO,32`.
- **`figure3.csv`** panel D ✓ (carried: 1.090039 [0.998728, 1.189942]; 0.507178; −0.384083; −0.755373; N = 160;
  24 random directions). The panel label `steered_minus_clean_margin` is present.
- **`figure4.csv`** ✓ (carried).
- **`figureA8.csv`** ✓ (carried: 0.916730, floor 0.364064, 616.91875; Qwen3-32B passage −0.027347
  [−0.085791, 0.033135], floor 0.281264; bare 0.413445, floor 0.364686).
- **`figureA10.csv`** ✓ (carried: 0.149297 at 0.4082; 0.061758 at 1/6; 0.011510 at 1/32; 0.425078 at full). The
  label `six_sighting_strength_ladder` is present.
- **`neutral_passages/prereg.json`** ✓ (carried: `n_floor` 40, `dose_points` [−1, −0.5, 0, 0.5, 1], `floor_k` 24,
  `n_neutral` 160). `op_member.olmo_32b` is 0.3.
- **`neutral_passages/analysis.json`**:
  - `members.olmo_32b` ✓: `hf_id` `allenai/OLMo-2-0325-32B-Instruct`, `layer` 32, `op_member` 0.3;
  - `prereg.precondition_cache` ✓ TAU: "Adjudicated by the fidelity run frozen scale-relative criterion TAU =
    0.0178835444, never by a fixed nat threshold";
  - "the scale definition" — not in this field (see N1).
- **`neutral_passages/reduced.json`** ✓:
  - `injected_l2` is 7.6473 on all 160 valenced reads at d = +1, so ‖ṽ(+1)‖ = 7.6473;
  - over the 2,400 neutral reads at gen_point 0 that carry a fidelity re-computation (of 4,640 neutral reads there),
    the fidelity values have median 0.03125 and maximum 0.125, with 573 above 0.05;
  - "mean scale 11.15" is `analysis.json`'s field (N1).
- **`neutral_passages/spec.json`** ✓ (present; carried for C13).
- **The 14 skeleton files** ✓:
  - 160 records, each carrying `history`, `order`, `present`, `turn_spans`, `s_spans`, `u_spans`, `ids_sha` and
    `seq_len`;
  - six S turns and six U turns per session;
  - the `present` order is 79 S-first and 81 U-first (B5's 79/81);
  - the mean S whole-turn span is 616.919 tokens, Fig. A8's 616.91875 (C1's [C]).
- **`transcripts/B2_fixed_text_session_olmo32b_run0_dose+1.md`** ✓: line 66 reads "Fresh-recompute fidelity check:
  |cached − fresh| = 3.12e-02 nats". Its provenance line gives "1273 tokens", G-DATA (iv)'s 1,273 for `floor_b0`.
- **`strength_ladder/{analysis,spans}.json`** ✓ (present).

### 2.4 [S] figures, reproduced [C]

The statistical rows come from `reduced.json`'s 160 neutral sessions, with Δm = margin(d) − margin(0) per session,
through v0.1's `repro_s.py`, run again. The count rows (§2.4, §0.4, the tuples) and 0.916/3 are arithmetic on v0.2's
own text. The ladder row is interpolated from `figureA10.csv`.

| v0.2's figure | reproduced |
|---|---|
| SDs of Δm (ddof 0): 0.623 at +1, 0.370 at +1/2, 0.455 at −1 | 0.6233, 0.3703, 0.4546 |
| valenced OLS slope: mean 0.916, SD 0.447 (ddof 0) | 0.9164, 0.4466 |
| 24 random directions' slopes: −0.288 to +0.364 | −0.2880 to +0.3641 (one shared 40-session set) |
| minimum at +1: +0.125 | +0.1250 (160 of 160 positive) |
| at −1: 154 of 160 negative, maximum +0.406 | 154 of 160; +0.4062 |
| SE at +1: 0.049 | 0.0494 (sample SD/√160); 0.0493 with the ddof-0 SD; 0.049 either way |
| R ≈ 25.49 from 7.6473/0.30 | 25.491 |
| §2.4 reads: 960; 4,800; 320; 320; 320 + 320; 160; 160 (N1-V, N1-R, N1-P, N2-E, N2-S + N2-C, N4-T, N4-Ts) | ✓, sum 7,360 |
| ≈ 3,140 re-computations | 3,472 under §2.1's rule (N2) |
| ≈ 10,500 forwards | 10,832 under §2.1's rule (N2) |
| §0.4: 48 / 320 (160 + 160) / 960; as written +48, +640, +1,920; struck −48, −320, −960 | ✓ |
| tuples: 385 | 4 × 3 × 4 × 4 × 2 + 1 = 385 |
| 0.916/3 = 0.305 | 0.3053 |
| the ladder at 1/3 by interpolation: 0.1222 | 0.1222, linear between 0.061758 at 1/6 and 0.149297 at 0.4082 |

Beside these, §2.1's [C] figures hold:
- 573 / 2,400 = 23.875%, "23.9%";
- median 0.03125, "0.031";
- maximum 0.125;
- §2.5's interpolated SD 0.2469 and SE 0.0195, carried.

### 2.5 The dated notes (minor residues; the routing's process line)

- **N1 (2026-11-06) — the fidelity scale: its locator, and its identification.**
  - **The gap.** §2.1 and §9 place "the scale definition" in `analysis.json`'s `prereg.precondition_cache`. That
    field names TAU as "scale-relative" but defines no scale. No released BK file and no section of the paper defines
    the per-read fidelity scale either.
    - Code searched every string in the clone's JSON, MD and TEX files and the PDF's text. The blind values-check
      extended the search to every JSON/JSONL key and value and to the clone's .py and .R scripts.
    - Both searches find the fidelity scale only as means: `mean_scale_nats` and `mean_scale_{clean,natural}_nats`,
      with `absolute_tolerance_as_fraction_of_scale` beside them.
    - They also find `dose_calibration/panel_prereg.json`'s "TAU = 0.0178835444, derived from the old 0.20-nat
      tolerance and OLMo rows only".
    - They find scale-named fields of other kinds: `scale` objects defined as the SD of the choice margin at dose 0,
      for standardized slopes; `steered_sep_scale`; `norm_match_scale`.
    - The code is not released, and Route A was not sent.
  - **The identification.** The per-read scale **max(|log p(S)|, |log p(U)|)** reproduces
    `members.olmo_32b.instrument.fidelity.mean_scale_nats` = 11.153449684153905 exactly: mean 11.153449684154 over
    the 2,640 reads that carry `fidelity_absdiff` (`n_adjudicable_reads` 2,640), a difference of 0 at 12 decimals.
    The other seven candidates miss by 0.51 to 10.1 nats. The candidates were declared in the script before it ran;
    the script is in §3.
  - **The same definition reproduces BK's other fidelity figures.**
    - Session-level retention over BK's 240 sessions with adjudicable reads: at ×0.25 of TAU, 93/240 = 0.3875; at
      ×0.5, 233/240 = 0.970833; at ×0.75 and ×1.0, 240/240. Each equals BK's `retention_relative_x*`.
    - 0.20 / `mean_scale_nats` = 0.017931671874052292, which equals BK's `absolute_tolerance_as_fraction_of_scale`.
    - The blind values-check found these first; Code re-ran them.
  - **The locator.** "Mean scale 11.15", which §9 lists under `reduced.json`, is `analysis.json`'s field. It
    reproduces from `reduced.json`'s reads under this definition.
  - **Code's reading, for G-DATA (vi).** G-DATA (vi) records this identification as the definition of record, by
    reproduction, as C13 does for `ids_sha`. LOCK v0.1 names it as identified by reproduction, unless the seat rules
    otherwise.
  - **A preview, for the record; G-DATA (vi) computes it.**
    - Under this scale, BK's reads exceed TAU × scale on 0 of the 2,400 neutral reads that carry a fidelity
      re-computation. Their largest |cached − fresh| / scale is 0.012143, against TAU 0.017884.
    - So p0 = 0. §2.1's exact binomial at cadence 160 is then rule 21's zero-base-rate form, a hair trigger, and a
      fire pauses as §2.1 has it.
    - At TAU/4, 570 of the 2,400 reads (23.75%) would be dropped by §4 (f)'s sensitivity row on BK's own reads.
    - BK record retention at ×0.25 too: `retention_relative_x0.25` 0.3875 is session-level.
- **N2 (2026-11-06) — §2.4's re-computation count.**
  - §2.1's rule re-computes every read at d ∈ {0, +1, −1}. That includes N4-T's and N4-Ts's 320 reads, which are at
    d = 0, and §2.4's list omits them.
  - The 10% keyed sample then covers "the other points": N1-V and N1-R at +1/2, +d_20 and +d_eq, and N2. That is
    480 + 2,880 + 960 = 4,320 reads, so the sample is 432, which the seat's "≈ 420" approximates.
  - Re-computations come to 480 + 1,920 + 320 + 320 + 432 = 3,472, and forwards to 7,360 + 3,472 = 10,832, against
    the document's ≈ 3,140 and ≈ 10,500.
  - Code's groundwork first read N4 as part of the sampled rest (464, 3,184, 10,544). The blind values-check pointed
    to §2.1's rule, and Code builds that rule.
  - These are planning values: G-TIME-n governs, and no gate reads them. LOCK v0.1 states the computed counts.
- **N3 (2026-11-06) — §7.4's "no recourse" beside decision (16).**
  - §7.4 reads: "a unit not locked by its date is NOT-RUN with no recourse (A-m1's decision (16) applies to units
    with no session; a unit with sessions follows §5)".
  - Decision (16) is itself a recourse: one PI-routed re-registration for a unit whose Clock passed with no lock and
    no session. Its own words are "a second miss is NOT-RUN with no recourse".
  - Code reads the parenthetical as governing. An n unit that misses its date with no session may be re-registered
    once under (16). "No recourse" binds after that, and a unit with sessions follows §5.
  - The difference binds only on a Clock miss.
- **N4 (2026-11-06) — ledger (55)'s anchors.**
  - `gcal.py:39–40` and `scripts/m_sessions.py:491–492` resolve as quoted at `9cbacdb`, the prebuild raw's HEAD at its
    push.
  - `71cc23c` (m package — BUILD (OLMo)) has since built G-CAL-OLMo and the OLMo stage wiring, so those line numbers
    read otherwise at HEAD.
  - The ledger records the state at the prebuild raw. Its anchors are read at `9cbacdb`, as the RESULTS-anchor
    practice pins them.
- **N5 (2026-11-06) — `data/n/bk/` at step 3 and at G-DATA (ii).**
  - §8 step 3 places "BK's files under `data/n/bk/` with shas and the attribution line", and G-DATA (ii) "copies"
    the same set. Code copies the G-DATA (ii) set at step 3, byte-identical, with `SHA256SUMS`, and adds BK's
    `LICENSE` (CC BY 4.0, whose terms ask for the license text or its link) and an attribution file `SOURCE.md`.
  - G-DATA (ii) then re-verifies those shas against a fresh clone at `7631f8a`.
  - `data/n/` is ignored by `.gitignore`'s `/data/*`. The commit therefore adds a commented, per-directory exception
    that admits `data/n/bk/` and nothing else under `data/n/`, in the form `.gitignore:8–10` sets ("Exceptions are
    per-directory and deliberate, never blanket"). So `.gitignore` is in this commit.

## 3. Sources and scripts

- **The clone**: github.com/camberg23/act-on-valence at `7631f8a06cdeffaf8b7a89212e5ccbe55a657732` (tree
  `d6f1d50525874355d1ea992f8f652358742ae282`; the commit dated 2026-10-05), in Code's scratch directory, clean, read
  as data. Code's scripts ran under `python3 -I` from a separate directory.
- **The PDF**: at the path v0.2's header names, sha256 `e92c69cb…fa49`. Text extracted with macOS PDFKit, as in
  v0.1's check.
- **The copies**: `data/n/bk/`, 26 files, each byte-identical to the clone (`cmp` of the two sha256 lists). The 14
  skeleton files, concatenated in name order, hash to `be50011a5ab1e8a4261dbde72afc84313d3bdeba9e40078272928bd497c3ba84`,
  as in v0.1's STOP raw §6.
- **N1's identification script**, as run: inputs `analysis.json`, `reduced.json`.

```python
import json, sys, statistics as st
a = json.load(open(sys.argv[1])); red = json.load(open(sys.argv[2]))
target = a["members"]["olmo_32b"]["instrument"]["fidelity"]["mean_scale_nats"]   # 11.153449684153905
adj = [r for r in red["reads"]["olmo_32b"] if r.get("fidelity_absdiff") is not None]   # 2,640
C = {"abs(lpS)+abs(lpU)": lambda r: abs(r["logprob_S"]) + abs(r["logprob_U"]),
     "(abs(lpS)+abs(lpU))/2": lambda r: (abs(r["logprob_S"]) + abs(r["logprob_U"])) / 2,
     "max(abs lpS, abs lpU)": lambda r: max(abs(r["logprob_S"]), abs(r["logprob_U"])),
     "min(abs lpS, abs lpU)": lambda r: min(abs(r["logprob_S"]), abs(r["logprob_U"])),
     "abs(margin)": lambda r: abs(r["margin"]), "abs(fresh_margin)": lambda r: abs(r["fresh_margin"]),
     "abs(lpS)": lambda r: abs(r["logprob_S"]), "abs(lpU)": lambda r: abs(r["logprob_U"])}
for name, f in C.items():
    m = st.mean(f(r) for r in adj); print(f"{name:24s} mean={m:.12f} diff={m - target:+.3e}")
```

Output, over the 2,640 reads:

| candidate | mean | diff from target |
|---|---|---|
| abs(lpS)+abs(lpU) | 21.218274032817 | +1.006e+01 |
| (abs(lpS)+abs(lpU))/2 | 10.609137016408 | −5.443e-01 |
| **max(abs lpS, abs lpU)** | **11.153449684154** | **+0.000e+00** |
| min(abs lpS, abs lpU) | 10.064824348663 | −1.089e+00 |
| abs(margin) | 1.088625335491 | −1.006e+01 |
| abs(fresh_margin) | 1.089072221698 | −1.006e+01 |
| abs(lpS) | 10.641570497390 | −5.119e-01 |
| abs(lpU) | 10.576703535426 | −5.767e-01 |

- **N1's preview**: TAU and the reads as above. On the 2,400 neutral reads at gen_point 0 that carry a fidelity
  re-computation, 0 exceed TAU × scale and 570 (0.2375) exceed TAU/4 × scale. The maximum |cached − fresh| / scale is
  0.012143. Over all 2,640 such reads the counts are 0 and 626.
- **N1's further support**: the session-level retention and the absolute-tolerance figures above, by the same scale.
  Sessions are keyed by arm, cell, run, seed, cue_S, cue_U and ids_sha; a session is kept at ×k when every one of its
  adjudicable reads has |cached − fresh| ≤ k × TAU × scale.
- **The blind values-check**: `results/raw/2026-11-06_n-v0_2_entry_valuescheck.md`, with Code's dispositions.

## 4. Not done

- G-DATA (step 4) has not run. Its (iv) needs the OLMo-2 Instruct tokenizer, which is not yet on this machine.
- Nothing is built, and no pod has started for PROPOSAL-n.
- The pod watch for A-m1's OLMo units runs in its own session and is untouched by this check.
