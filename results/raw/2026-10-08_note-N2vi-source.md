# AUDIT-note-release v1.2 -- N2(vi): the source's per-stage hit rates

- Code stamp: Thu Oct  8 11:26:25 UTC 2026 (date -u)
- HEAD at run (informational; every repository read below is pinned to bbc9ffe = bbc9ffe72fb8a942431c9bf2622a36e581fdf93c): cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55
- Block: `AUDIT-note-release-v1_2.md` sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841` (from git show bbc9ffe:AUDIT-note-release-v1_2.md); routed sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841`: MATCH
- Item: N2(vi), block line 35 (AUDIT-note-release-v1_2.md@bbc9ffe:35)
- Script: `scripts/audit_note_N2vi.py` sha256 `2ed1ecbfa10dcd48f33d219d28d5e2a6e4d6b3fc4b00084d0767849ccb3f5237`
- Interpreter: /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python (Python 3.12.9)
- Command: `/Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python scripts/audit_note_N2vi.py`
- Source read by Code on 2026-10-08 (UTC) with the WebFetch tool (reading only; nothing downloaded, saved or executed). WebFetch returns a model-processed rendering of each page, so every source fact below is Code's reading through that tool. Each of the four v1 Appendix C sentences came back verbatim in two separate fetches (one general, one asking for the sentence character for character; the general fetch omitted only the base sentence's opening clause naming Figure 21), and a third fetch that paraphrased the paragraph agreed with both, including that the instruct 0.3% is the introspection rate and the instruct FPR is 0%. The fixer pass re-read four points on the same date, round 2 two more on 2026-10-08, and round 3 one file twice on 2026-10-08 (section 3, last three lists).
- Not checked: the note's own sentence and F2's plotted points. results/raw/2026-10-08_note-preflight.md@bbc9ffe:15 lists `RESEARCH-NOTE-v0_2-draft.md` as MISSING and :17-18 list the F1/F2 SVGs as MISSING on this machine, so the note's wording (that it 'carries 0.001 / 0.149 / 0.029 / 0.009') and F2's plotted source points were not read; the values are taken as the block states them (block :35).

## 0. Per-figure status (for N1's ledger)

Status vocabulary: reproduced | log-only | not found | discrepant | computed-new. 'log-only' means the record carries the figure only in prose. Where this item checked such a figure against the source or re-derived its arithmetic, the result is in 'printed'. Rows 1-10, the two ~800/80 rows (which divide that pattern's and the ~33× pattern's carriers between them, asserted) and the joint, pair and p ~ .28 rows take their locators from the carrier search (section 2), so for those patterns the lists are complete; rows 19 and 24 take their prose locators from the round-4 greps there (row 19's table cells are located by parsing the table). 'Other tracked' are code comments, a fixture and a handoff, not log lines. Row 24 was added in round 4 and appended, so rows 1-23 keep the numbers the earlier values-check rounds cite. Block :23 consequences for the note are in section 12.

| # | figure | record locator(s) | status | printed by this script | note |
|---|---|---|---|---|---|
| 1 | source base TPR 0.001 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:43; RESULTS.md@bbc9ffe:7338; other tracked: scripts/b2r_analyze.py@bbc9ffe:175, scripts/b2r_scorer_selftest.py@bbc9ffe:119, valence_core/detection_v2.py@bbc9ffe:36 | log-only | record 0.001; source v1 text 0.001 | in no committed JSON; equals the v1 Appendix C prose |
| 2 | source sft TPR 0.149 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:44; RESULTS.md@bbc9ffe:6769, :6954, :7090, :7339, :7348 | log-only | record 0.149; source v1 text 0.149 | in no committed JSON; equals the v1 Appendix C prose |
| 3 | source dpo TPR 0.029 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:45, :212; RESULTS.md@bbc9ffe:6769, :6954, :6955, :7090, :7091, :7340, :7348, :7356; other tracked: scripts/b2r_analyze.py@bbc9ffe:24, scripts/b2r_analyze.py@bbc9ffe:138 | log-only | record 0.029; source v1 text 0.029 | in no committed JSON; equals the v1 Appendix C prose |
| 4 | source instruct TPR 0.009 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:46; RESULTS.md@bbc9ffe:7341, :7356 | log-only | record 0.009; source v1 text 0.009 | in no committed JSON; equals the v1 Appendix C prose |
| 5 | source base FPR 0.164 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:43, :133, :148; RESULTS.md@bbc9ffe:6996, :7193, :7252, :7270, :7338, :7374; other tracked: HANDOFF-2026-08-25.md@bbc9ffe:60, scripts/b2r_analyze.py@bbc9ffe:13, scripts/b2r_analyze.py@bbc9ffe:161, scripts/b2r_analyze.py@bbc9ffe:175, scripts/b2r_scorer_selftest.py@bbc9ffe:119, valence_core/detection_v2.py@bbc9ffe:36 | log-only | record A 0.164 / record B 0.164; source v1 text 0.164 | in no committed JSON; equals the v1 prose |
| 6 | source sft FPR 0.225 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:44, :133; RESULTS.md@bbc9ffe:6909, :6997, :7011, :7193, :7270, :7339, :7374; other tracked: HANDOFF-2026-08-25.md@bbc9ffe:60, scripts/b2r_analyze.py@bbc9ffe:13, scripts/b2r_analyze.py@bbc9ffe:161 | log-only | record A 0.225 / record B 0.225; source v1 text 0.225 | in no committed JSON; equals the v1 prose |
| 7 | source dpo FPR 0.000 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:45; RESULTS.md@bbc9ffe:6998, :7340, :7347, :7356; other tracked: HANDOFF-2026-08-25.md@bbc9ffe:60, scripts/b2r_analyze.py@bbc9ffe:161 | log-only | record A 0.000 / record B 0.000; source v1 text 0.000 | in no committed JSON; equals the v1 prose |
| 8 | source instruct FPR 0.003 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:46; RESULTS.md@bbc9ffe:6999, :7341, :7356; other tracked: HANDOFF-2026-08-25.md@bbc9ffe:60, scripts/b2r_analyze.py@bbc9ffe:161 | discrepant | record A 0.003 / record B 0.003; source v1 text 0.000 | Code's reading: transcription of the v1 prose, where 0.3% is the introspection rate and FPR is 0%. Fig. 21 (a PNG, olmo-staged-introspection.png) was not digitized, so a figure reading is not excluded; under block :23 the classification decides correction or STOP if the note carries it (section 12) |
| 9 | source TPR - FPR, base/sft/dpo (−16.3 pp / −7.6 pp / +2.9 pp) | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:43, :44, :45; RESULTS.md@bbc9ffe:7329, :7338, :7339, :7340 | log-only | source arithmetic -16.3 pp / -7.6 pp / +2.9 pp | equal |
| 10 | source instruct TPR - FPR +0.6 pp | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:46; RESULTS.md@bbc9ffe:7330, :7341; other tracked: scripts/b2r_analyze.py@bbc9ffe:15 | discrepant | source arithmetic +0.9 pp | follows from the instruct FPR reading (row above); same block :23 condition |
| 11 | aggregation over L in [25, 32, 38, 45, 51] x alpha in [1, 2, 4, 8] (20 configurations) | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:39; RESULTS.md@bbc9ffe:7343 | log-only | 20 configurations; addendum :39 text asserted | equals the v1 Figure 21 caption; every per-stage value is this aggregate, not best-of-grid |
| 12 | ~800 injected / ~80 control per (layer, alpha) configuration, and its ratio ~33× our 24, as the record's inference (eight concepts x the code's 100 / 10 per concept) | RESULTS.md@bbc9ffe:7438-7440 (carriers :7439, :7440) | log-only | computed-new: 8 x 100 / 8 x 10 = 800 / 80 per cell; pooled over 20 cells 16000 / 1600; ratio 800/24 = 33.3 (one of their configurations against our whole stage, the record's unit); per stage under the same premise 16000/24 = 666.7; with the code's 50 concepts 208.3 and 4166.7 | the eight is our B2 registration (data/configs/b2_concepts.json@bbc9ffe selection_for_B2.registered_n = 8; its canonical set is 50, n_canonical); a per-configuration n, while the source's rates are pooled over 20 configurations (section 7); our 24 per stage as run from RESULTS.md@bbc9ffe:7440, :7358 |
| 13 | ~800 injected / ~80 control per configuration, as the source's n, and figures derived from it (~33× ours; the 'theirs, OLMo cell (~800/80)' power row) | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:32-33; RESULTS.md@bbc9ffe:7365, :7485, :7500 (:7485 and :7500-7502 are the power row at that n); the block's premise, AUDIT-note-release-v1_2.md@bbc9ffe:34 | not found | the source states no n (v1-v5); code default 50 concepts gives 5000 / 500 per cell; the ratio is 33.3 only per their configuration at eight concepts (row above) | under block :23 a note sentence presenting it as the source's n is cut, and so is any figure derived from it unless stated with its premise and unit (section 12, condition 4); RESULTS :7485 and :7500 sit in the entry (:7419-7506) that states the eight-concept premise at :7438-7439 but write the figure as theirs without it, and :7365's entry (:7326-7418) does not state the premise; as an assumption with its premise it is the row above |
| 14 | layer indices from the code's default fractions | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:60-68 | computed-new | int [25, 32, 38, 44, 51]; round [26, 32, 38, 45, 51]; caption [25, 32, 38, 45, 51]; README absolute list equals the caption 5/5 | neither rule yields the caption list; not adjudicated |
| 15 | decoding: temperature 1.0, max_new_tokens 100 | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:89-91; RESULTS.md@bbc9ffe:7433 | log-only | source code DEFAULT_TEMPERATURE 1.0, DEFAULT_MAX_TOKENS 100; paper v1 App. A T = 1.0 | consistent |
| 16 | lineage: our four acquired HF repos and revisions | data/olmo/manifest.json@bbc9ffe fields repo, revision | reproduced | base allenai/Olmo-3-1125-32B @ c2b61dae89a1; sft allenai/Olmo-3.1-32B-Instruct-SFT @ 152782ecc41a; dpo allenai/Olmo-3.1-32B-Instruct-DPO @ fc84a4f69991; instruct allenai/Olmo-3.1-32B-Instruct @ ac0587e4a774 | read from the committed manifest |
| 17 | lineage: our four repos match the source's MODEL_NAME_MAP | RESULTS.md@bbc9ffe:12565-12569 | log-only | computed-new against Code's WebFetch reading of src/model_utils.py@5d5d9b4: 4/4 repo match | the source half is a WebFetch reading, not a committed artifact, so the match is the record's prose claim; revision-level match not determinable (source pins none) |
| 18 | retired criterion's power, DPO column (2.9 vs 0.0): 0.001/0.012/0.147/0.691 at n = 24/48/96/200 | RESULTS.md@bbc9ffe:7354-7361 | log-only | recomputed with the record's newcombe: 4/4 cells agree to 3 dp | inputs are prose rates, so log-only; they equal the v1 text, so the cells stand as described ('at their own numbers'); the arithmetic is re-derived and agrees (computed-new) |
| 19 | retired criterion's Instruct power, as the record describes it: at the source's own (reported) rates, 0.000/0.000/0.001/0.020 at n = 24/48/96/200 (the table's 'Instruct (0.9 vs 0.3)') | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:52-53; RESULTS.md@bbc9ffe:7330-7331, :7354-7361; other tracked: scripts/b2r_analyze.py@bbc9ffe:16 (docstring, 0.000 at n=48; unchanged at either rate) | discrepant | at the record's transcribed rates (0.9 vs 0.3) recomputed 0.000 / 0.000 / 0.001 / 0.020 (4/4 agree to 3 dp); at the source's rates (0.9 vs 0.0) 0.000 / 0.000 / 0.002 / 0.036; differs at n = 96, n = 200 | described as at the source's own rates ('their own Instruct rates', 'Instruct's own reported rates', 'their own numbers'), where the n = 96 and n = 200 cells differ; the arithmetic reproduces at the record's 0.3%; follows from the instruct FPR reading (row 8); under block :23 corrected to the source-rate values under Code's transcription reading, a STOP otherwise (section 12, condition 3) |
| 20 | [g3-A] joint power 0.9642 (and 'the exact number is 0.964') | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:148, :273; RESULTS.md@bbc9ffe:7173, :7180, :7192, :7194, :7251, :7269, :7270; data/olmo/b2r_valuescheck.json@bbc9ffe 1_g3A_power.detail | discrepant | exact at the record's inputs 0.96455 (0.9645; 0.965 at 3 dp); at instruct FPR .000 0.98274 | residual -0.0003; discrepant at the record's own 3 dp too; cause not identified (simulation a candidate, not established), so not classifiable as transcription; under block :23 a STOP for the design seat and PI if the note carries 0.9642 or 0.964 (section 12); both values clear the 0.90 bar |
| 21 | single weakest pair (base vs dpo) 0.9825 | RESULTS.md@bbc9ffe:7192, :7268 | discrepant | at the record's inputs base > dpo 0.98296; weakest pair base > instruct 0.96540; at instruct FPR .000 base > dpo = base > instruct 0.98296 | value residual -0.0005 and the label is wrong at the record's inputs; under block :23 a STOP if the note carries it (section 12) |
| 22 | design seat's N2(v) source points (block :34: d' -1.9 / -0.3 / +0.6 / +0.15; p ~ .11 DPO, ~ .5 instruct, at 800/80 per configuration) | AUDIT-note-release-v1_2.md@bbc9ffe:34 | computed-new | at 800/80 (per configuration): -1.931 / -0.296 / +0.611 / +0.151; p DPO 0.1085, instruct 0.5119. At 16000/1600 (pooled, same premise): -2.103 / -0.286 / +1.525 / +1.056; p DPO 3.34e-20, instruct 1.03e-06; instruct at record FPR .003 +0.339, p 0.0055 | arithmetic confirmed under the seat's premise (800/80 is a per-configuration n applied to rates pooled over 20 configurations), not confirmed as the source's points: at the pooled n 1 of 6 figures hold, and there the instruct FPR correction changes the instruct point (d' +0.339 -> +1.056; p 0.0055 -> 1.03e-06); N2(v) declares concept count and unit |
| 23 | p ~ .28 for our 0/43 at the source's dpo TPR 2.9% | RESULTS.md@bbc9ffe:6955, :7091 | log-only | computed-new 0.2821 = P(X <= 0) for X ~ Binomial(n = 43, p = .029), exact binomial lower tail (= 0.971^43); 0/43 from data/olmo/b2r_explore_dpo.json@bbc9ffe fields hit, inj_decidable | agrees at the record's 2 dp; the test is Code's reading (the record names none); the 2.9% is a source prose rate, so log-only |
| 24 | 'Reaching conventional power there needs n in the thousands per cell' (the retired criterion at Instruct, the sentence after the table under 'Power at their own numbers') | RESULTS.md@bbc9ffe:7363-7364 | discrepant | computed-new, n per arm: at the source's rates (0.9 vs 0.0) 0.80 power at n ≈ 750 per arm (0.8042), and 0.90 at ≈ 890 (0.9020); first n 746 (0.80054) and 887 (0.90043). At the record's transcribed rates (0.9 vs 0.3) ≈ 2700 (0.8011) and ≈ 3500 (0.9001); first n 2694 (0.80012) and 3500 (0.90008); step-1 values at 5 dp | holds only at the transcribed 0.3%; described as at the source's own rates (it sits under 'Power at their own numbers', :7354), where conventional power needs hundreds per arm; 'per cell' read as n per arm, the table's unit (:7356; Code's reading); :7363's 'binding constraint ... not close' holds at both inputs; the only carrier the round-4 'thousands' grep finds in the tracked .py/.md files (section 2); follows from the instruct FPR reading (row 8); under block :23 corrected to the source-rate figures under Code's transcription reading, a STOP otherwise (section 12, condition 3), the same fork as row 19 |

## 1. The addendum's lines (git show bbc9ffe:ADDENDUM-g3-b2r-v1.2.md)

### :25-58 -- section 0.1 (five candidates, n, sources) and 0.2 (the recovered table)
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:25: ## 0. Provenance, defects, and the five candidates
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:26: 
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:27: **0.1 The stop's candidate explanations are five, each pinned:**
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:28: dose (we ran 0.112–0.768× their weakest swept strength), format
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:29: (fidelity-of-text, their template guard makes their fallback dead code),
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:30: decoding (their OLMo experiment declares temperature 1.0 and structurally
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:31: must — ten samples per trial is incoherent at greedy; ours ran 0.0),
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:32: **n** (their OLMo cells are ~800 injected / ~80 control per config — ~33×
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:33: ours; at their quoted 10.8% baseline detection rate, B2 as registered had
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:34: ~11% power), and **the criterion's quantity** (§0.2). Sources: sha
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:35: `5d5d9b485e293dc766c3a056cfe50283a7e435b6`; arXiv:2603.21396 Appendix C,
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:36: Fig 21.
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:37: 
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:38: **0.2 The recovered result the control must now aim at.** Their OLMo
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:39: rates (Fig 21, aggregated over L ∈ [25,32,38,45,51], α ∈ [1,2,4,8]):
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:40: 
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:41: | stage | their TPR | their FPR | sensitivity |
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:42: |---|---|---|---|
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:43: | base | 0.1% | 16.4% | −16.3 pp |
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:44: | sft | 14.9% | 22.5% | −7.6 pp |
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:45: | dpo | 2.9% | 0.0% | +2.9 pp |
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:46: | instruct | 0.9% | 0.3% | +0.6 pp |
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:47: 
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:48: **Their OLMo transition is in the false-positive rate** — base and SFT
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:49: affirm promiscuously and post-training collapses it to ~0 — while true
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:50: detection stays ≤15% everywhere and *declines* across the DPO step. The
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:51: retired criterion (sensitivity CI excluding 0 at DPO and Instruct)
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:52: demanded significance precisely where their effect is smallest: power at
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:53: their own Instruct rates is 0.000 at n = 48 and 0.020 at n = 200. It was
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:54: aimed at the wrong quantity. **Slip ledger, design seat, entry five**
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:55: (inheritance noted: registered from the headline before appendix-level
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:56: provenance existed; the lock's values-check verified 59 values and never
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:57: the aim). Lesson carried forward in one sentence: **positive controls are
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:58: specified against the source's numbers, not its abstract.**
```
### :60-68 -- section 0.3, layer of record (code rule and caption)
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:60: **0.3 Layer of record: L_M = 44** ([g3-PIN-1] closed).
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:61: `model_utils.py:1484`: `layer_idx = int(n_layers × fraction)`, clamped;
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:62: OLMo-3-32B `num_hidden_layers = 64` ⇒ int(64 × 0.7) = **44**, 0-based;
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:63: hook semantics verified identical to ours (block forward output, no
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:64: off-by-one). The README's OLMo invocation passes absolute layers to a
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:65: fraction-typed argument and is not the code path that produced their
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:66: results; L_M stands on the code rule and the paper's caption. L_M
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:67: coincides with the A4 selection at the three post-trained stages by
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:68: arithmetic accident; the rule, not the accident, governs.
```
### :89-96 -- section 0.5, decoding of record
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:89: **0.5 Decoding of record, all parts:** temperature 1.0, `max_new_tokens`
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:90: 100 — their OLMo experiment's declared parameters
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:91: (`DEFAULT_TEMPERATURE = 1.0`, README passes no override). Per-trial
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:92: seeds are live and declared; a **sampling-reproducibility assertion**
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:93: joins the pre-campaign smoke (same seed → identical token ids, ×2, per
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:94: stage) — it tests a surface the determinism gate never covered (sampled
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:95: draws from the global RNG). Decoding parameters are measurement
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:96: parameters; this addendum names all of them.
```
### :98-105 -- section 0.6, 'no per-config OLMo numbers exist in the release'
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:98: **0.6 The inverted U.** Their per-strength rates (Gemma3-27B-IT, the
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:99: primary model; **no per-config OLMo numbers exist in the release**, so
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:100: these size the paradigm, not the lineage): mean hit 0.19 / 0.40 / 0.45 /
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:101: 0.18 across strengths 1/2/4/8; at strength 8's best-detection layer,
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:102: identification-given-claim is 0.003 — disruption, not content delivery.
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:103: **Their operative strength is 4.0; 8× is past the optimum.** The §2
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:104: ladder keeps 8.0 as its declared top with the coherence gate armed —
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:105: the data say the top of the ladder is where the effect dies.
```
### :131-134 -- section 1, their control FPRs
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:131: carry no injection, so no dose question touches this part** — which also
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:132: makes it the clean test of the format/decoding candidates: B2's controls
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:133: at greedy gave 0/20 and 0/24 where theirs give 16.4% and 22.5%, and that
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:134: divergence is attributable only to format and/or decoding.
```
### :144-149 -- section 1, [g3-A] power at their rates
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:144: - **Criterion [g3-A]:** the transition replicates iff the exact
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:145:   Clopper–Pearson interval separation holds pairwise — FPR lower bound
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:146:   at Base AND at SFT each exceed the FPR upper bound at DPO AND at
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:147:   Instruct (four separations, all required). Verified 2026-08-24: joint
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:148:   power **0.9642** at their own rates and n = 96, with **base (16.4%)
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:149:   the binding stage**.
```
### :209-218 -- section 3, power scope against their aggregate TPR
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:209: - **Power scope, pre-stated.** At n = 48/48 the committed interval
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:210:   machinery detects true hit rates ≥ ~0.15–0.20 (verified 2026-08-24:
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:211:   minimum firing count k = 5, hit 0.104; power 0.531 at 0.10, 0.866 at
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:212:   0.15, 0.975 at 0.20). Their OLMo aggregate TPR (2.9% at DPO) is
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:213:   **below this floor** and is diluted by past-optimum strengths; whether
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:214:   best-config OLMo detection exceeds the floor is unknown — any
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:215:   expectation from the Gemma cache is extrapolation and labeled so.
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:216:   **Therefore nothing here can "fail to replicate" anything**: a null at
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:217:   this n against their aggregate rates is expected under their own
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:218:   numbers and concludes nothing. The positive control is §1 alone.
```
### :271-278 -- section 6, values-check 'exact against paper'
```
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:271: ## 6. Values-check (v1.1, returned GREEN 2026-08-24)
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:272: 
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:273: All items verified: [g3-A] power shown (joint 0.9642, base binds);
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:274: §0.2/§0.6 tables exact against paper and cache; carry-over identity for
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:275: sft/dpo/instruct with the fingerprint caveat now resolved by §0.4's
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:276: convention; prompts rule-18 clean; §5 selftests GREEN including the
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:277: negative-sensitivity case; sampling assertion built; allocation
ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:278: arithmetic exact; budget 3.63 h single-box (anchors within 0.17 h).
```

Other addendum lines matching `0\.1%|14\.9%|2\.9%|0\.9%|16\.4%|22\.5%|0\.3%|Fig 21|~800|aggregat` outside the ranges above: 0

## 2. RESULTS.md lines carrying the same values (git show bbc9ffe:RESULTS.md)

### :6994-6999 -- B2-r verdict table, 'theirs' column
```
RESULTS.md@bbc9ffe:6994:     | §1 control | ours | theirs | decidable |
RESULTS.md@bbc9ffe:6995:     |---|---|---|---|
RESULTS.md@bbc9ffe:6996:     | base | **0.4310** (25/58) CI [0.302, 0.568] | 0.164 | 58/96 **below floor** |
RESULTS.md@bbc9ffe:6997:     | sft | **0.2000** (17/85) CI [0.121, 0.301] | 0.225 | 85/96 |
RESULTS.md@bbc9ffe:6998:     | dpo | **0.0000** (0/91) CI [0.000, 0.040] | 0.000 | 91/96 |
RESULTS.md@bbc9ffe:6999:     | instruct | **0.0000** (0/91) CI [0.000, 0.040] | 0.003 | 91/96 |
```
### :7085-7092 -- B2-r section 3 reading, 14.9% -> 2.9%
```
RESULTS.md@bbc9ffe:7085:     **DPO and Instruct make zero detection claims of any kind** — no hits, no
RESULTS.md@bbc9ffe:7086:     false alarms, across 88 and 89 decidable trials — while injected words
RESULTS.md@bbc9ffe:7087:     still leak into 4/48 and 2/48 of their generations. The concept arrives;
RESULTS.md@bbc9ffe:7088:     the model never claims to notice. That is their own mechanism story
RESULTS.md@bbc9ffe:7089:     reproducing: **specificity bought by a default negative response.** Their
RESULTS.md@bbc9ffe:7090:     Appendix C says it numerically (TPR 14.9% → 2.9% across the DPO step), and
RESULTS.md@bbc9ffe:7091:     our 0/43 is entirely consistent with a true rate of 2.9% (p ≈ 0.28). No
RESULTS.md@bbc9ffe:7092:     screen hit anywhere, as the pre-stated power scope predicted.
```
### :7170-7194 -- v1.1 values-check: table 'PASS -- exact', joint 0.9642, pair 0.9825
```
RESULTS.md@bbc9ffe:7170: - 2026-08-24 — **ADDENDUM-g3 v1.1 §6 VALUES-CHECK: GREEN on every checkable
RESULTS.md@bbc9ffe:7171:   item, with TWO FLAGS returned for the design instance and one provenance
RESULTS.md@bbc9ffe:7172:   caveat that changes what "carry over by identity" can mean. [g3-A] joint
RESULTS.md@bbc9ffe:7173:   power 0.9642 ≥ 0.90. Both analyzers self-test GREEN before any B2-r trial
RESULTS.md@bbc9ffe:7174:   (scorer 21/21, `b2r_analyze` 10/10). Budget 3.63 h, single-box.**
RESULTS.md@bbc9ffe:7175:   (`data/olmo/b2r_valuescheck.json`, `b2r_budget.json`;
RESULTS.md@bbc9ffe:7176:   `scripts/b2r_analyze.py`, `box_b2r_sampling_smoke.py`.)
RESULTS.md@bbc9ffe:7177: 
RESULTS.md@bbc9ffe:7178:     | §6 item | result |
RESULTS.md@bbc9ffe:7179:     |---|---|
RESULTS.md@bbc9ffe:7180:     | [g3-A] power ≥ 0.9 at n=96, separations shown | **PASS** — joint **0.9642** |
RESULTS.md@bbc9ffe:7181:     | §0.2 / §0.6 tables vs paper and cache | **PASS** — exact |
RESULTS.md@bbc9ffe:7182:     | carry-over identity + Base re-extraction plan | **PASS**, with a caveat |
RESULTS.md@bbc9ffe:7183:     | neutral prompts rule-18 sweep | **PASS** (clean on every binding pool) |
RESULTS.md@bbc9ffe:7184:     | §5 selftests incl. negative-sensitivity case | **PASS** 21/21 + 10/10 |
RESULTS.md@bbc9ffe:7185:     | sampling-reproducibility assertion present | **PASS** (built) |
RESULTS.md@bbc9ffe:7186:     | allocation (§2 24/24; §3 48 = 8×6) | **PASS** |
RESULTS.md@bbc9ffe:7187:     | budget vs anchors §1 1.0 / §2 1.2 / §3 1.1 h | **PASS** — 0.93 / 1.16 / 0.93 |
RESULTS.md@bbc9ffe:7188: 
RESULTS.md@bbc9ffe:7189:   - **[g3-A] arithmetic, shown as asked.** At n = 96, Base CP lower bound
RESULTS.md@bbc9ffe:7190:     0.0984 against DPO CP upper 0.0377 — separates. The criterion needs all
RESULTS.md@bbc9ffe:7191:     four pairwise separations, so the honest figure is the **joint**
RESULTS.md@bbc9ffe:7192:     probability, **0.9642**, not the single weakest pair (0.9825).
RESULTS.md@bbc9ffe:7193:     **`base` at 16.4% binds, not `sft` at 22.5%**, being the smaller of the
RESULTS.md@bbc9ffe:7194:     two high rates. "Not close" is right; the exact number is 0.964.
```
### :7265-7271 -- [g3-A] power rule (min CP-lower vs max CP-upper)
```
RESULTS.md@bbc9ffe:7265:   - **ITEM 3 power claims, both verified, one refined.**
RESULTS.md@bbc9ffe:7266:     **CONTROL:** at n = 96/stage the pattern needs all four pairwise
RESULTS.md@bbc9ffe:7267:     separations (min CP-lower over {base, sft} > max CP-upper over
RESULTS.md@bbc9ffe:7268:     {dpo, instruct}). Single weakest pair (base vs dpo) = 0.9825; **joint =
RESULTS.md@bbc9ffe:7269:     0.9642.** "Essentially 1" is right in spirit and the exact figure is
RESULTS.md@bbc9ffe:7270:     0.964; **base (16.4%) binds, not sft (22.5%)**, because it is the smaller
RESULTS.md@bbc9ffe:7271:     of the two high rates. **EXPLORATION:** at n = 48/48 the minimum firing
```
### :7326-7343 -- values-check RED entry: the recovered table and its aggregation
```
RESULTS.md@bbc9ffe:7326: - 2026-08-24 — **ADDENDUM-g3 VALUES-CHECK: RED, and not on arithmetic. [g3-PIN-2]
RESULTS.md@bbc9ffe:7327:   recovered from the paper (Appendix C, Fig 21) — and their OWN OLMo results
RESULTS.md@bbc9ffe:7328:   make the registered positive control UNREACHABLE on this lineage at any n
RESULTS.md@bbc9ffe:7329:   this program can afford. Their DPO effect is +2.9 pp and their Instruct
RESULTS.md@bbc9ffe:7330:   effect is +0.6 pp; the criterion requires BOTH to clear. Power at Instruct's
RESULTS.md@bbc9ffe:7331:   own reported rates: 0.000 at n = 48, 0.001 at n = 96, 0.020 at n = 200.**
RESULTS.md@bbc9ffe:7332:   Everything §5 asks for arithmetically VERIFIES; the problem is upstream of
RESULTS.md@bbc9ffe:7333:   the arithmetic. (Addendum draft uncommitted, as it should be. Sources:
RESULTS.md@bbc9ffe:7334:   arXiv:2603.21396 Appendix C; repo at sha `5d5d9b4`.)
RESULTS.md@bbc9ffe:7335: 
RESULTS.md@bbc9ffe:7336:     | stage | their TPR | their FPR | sensitivity (hit − FA) |
RESULTS.md@bbc9ffe:7337:     |---|---|---|---|
RESULTS.md@bbc9ffe:7338:     | base | 0.1% | 16.4% | **−16.3 pp** |
RESULTS.md@bbc9ffe:7339:     | sft | 14.9% | 22.5% | **−7.6 pp** |
RESULTS.md@bbc9ffe:7340:     | dpo | 2.9% | 0.0% | **+2.9 pp** |
RESULTS.md@bbc9ffe:7341:     | instruct | 0.9% | 0.3% | **+0.6 pp** |
RESULTS.md@bbc9ffe:7342: 
RESULTS.md@bbc9ffe:7343:     (Their Fig-21 rates aggregate over L ∈ [25,32,38,45,51], α ∈ [1,2,4,8].)
```
### :7345-7348 -- the record quoting v1 Section 3.3 (FPR reaches 0% only after DPO), then the TPR step 14.9% -> 2.9%
```
RESULTS.md@bbc9ffe:7345:   - **THE FINDING: their OLMo transition is in the FALSE-POSITIVE RATE, not in
RESULTS.md@bbc9ffe:7346:     sensitivity.** Their own text: base and SFT "exhibit high FPR, and only
RESULTS.md@bbc9ffe:7347:     after DPO does it drop to 0%" — and detection sensitivity *decreases*
RESULTS.md@bbc9ffe:7348:     across that same step, 14.9% → 2.9% TPR. Our registered criterion is
```
### :7354-7366 -- power table at their rates (Instruct 0.9 vs 0.3) and '~800 injected per config'
```
RESULTS.md@bbc9ffe:7354:   - **Power at their own numbers, registered criterion, perfect controls:**
RESULTS.md@bbc9ffe:7355: 
RESULTS.md@bbc9ffe:7356:     | n / arm | DPO (2.9 vs 0.0) | **Instruct (0.9 vs 0.3)** |
RESULTS.md@bbc9ffe:7357:     |---|---|---|
RESULTS.md@bbc9ffe:7358:     | 24 (as run) | 0.001 | **0.000** |
RESULTS.md@bbc9ffe:7359:     | 48 | 0.012 | **0.000** |
RESULTS.md@bbc9ffe:7360:     | 96 | 0.147 | **0.001** |
RESULTS.md@bbc9ffe:7361:     | 200 | 0.691 | **0.020** |
RESULTS.md@bbc9ffe:7362: 
RESULTS.md@bbc9ffe:7363:     **Instruct is the binding constraint and it is not close.** Reaching
RESULTS.md@bbc9ffe:7364:     conventional power there needs n in the thousands per cell — their own
RESULTS.md@bbc9ffe:7365:     OLMo cell is ~800 injected per (layer, strength) config aggregated over
RESULTS.md@bbc9ffe:7366:     five layers and four strengths. **B2-r as drafted (n = 48, fidelity-only)
```
### :7372-7377 -- their control FPRs
```
RESULTS.md@bbc9ffe:7372:   - **A dose-free line of evidence that format/decoding really do differ.**
RESULTS.md@bbc9ffe:7373:     Control trials carry no injection, so dose cannot touch them. Their
RESULTS.md@bbc9ffe:7374:     control-arm FPR is **16.4% (base) and 22.5% (SFT)**; ours was **0/20 and
RESULTS.md@bbc9ffe:7375:     0/24**. That divergence is attributable only to format and/or decoding,
RESULTS.md@bbc9ffe:7376:     and it is the cleanest such evidence available — it needs no dose
RESULTS.md@bbc9ffe:7377:     argument at all.
```
### :7393-7398 -- README layer caution
```
RESULTS.md@bbc9ffe:7393:     **Caution recorded:** the README's OLMo invocation `-ls 25 32 38 45 51`
RESULTS.md@bbc9ffe:7394:     passes absolute layers to an argument typed `float` and documented "layer
RESULTS.md@bbc9ffe:7395:     fractions", consumed by `int(n_layers × fraction)` — literally, all five
RESULTS.md@bbc9ffe:7396:     clamp to layer **63**. The paper's Fig-21 caption says the rates aggregate
RESULTS.md@bbc9ffe:7397:     over L ∈ [25,32,38,45,51], so those layers are certainly what they *ran*;
RESULTS.md@bbc9ffe:7398:     the README command as written is not the code path that produced them.
```
### :7431-7440 -- their code defaults and '~800 / ~80 per cell' with eight concepts
```
RESULTS.md@bbc9ffe:7431:   - **Their OLMo stage comparison is `experiments/03_behavioral_robustness.py`
RESULTS.md@bbc9ffe:7432:     — the direct analogue of B2 — and its declared defaults are:**
RESULTS.md@bbc9ffe:7433:     `DEFAULT_TEMPERATURE = 1.0`, `DEFAULT_MAX_TOKENS = 100`,
RESULTS.md@bbc9ffe:7434:     `DEFAULT_STRENGTH_SWEEP = [1.0, 2.0, 4.0, 8.0]`,
RESULTS.md@bbc9ffe:7435:     `DEFAULT_MAX_TRIAL_NUMBER = 10`, `DEFAULT_SAMPLES_PER_TRIAL = 10`
RESULTS.md@bbc9ffe:7436:     ("so 10×10 = 100 per concept"), `DEFAULT_CONTROL_SAMPLES_PER_TRIAL = 1`.
RESULTS.md@bbc9ffe:7437:     README's OLMo invocation passes **no** `--temperature`, so 1.0 governs;
RESULTS.md@bbc9ffe:7438:     its layer sweep is **absolute layers 25 32 38 45 51**. With eight
RESULTS.md@bbc9ffe:7439:     concepts that is **~800 injected / ~80 control per (layer, strength)
RESULTS.md@bbc9ffe:7440:     cell** against our 24/24 — roughly **33× more injected trials**.
```
### :7480-7485 -- power table with the row 'theirs, OLMo cell (~800/80)' (round 3)
```
RESULTS.md@bbc9ffe:7480:     | design | hit .05 | hit .108 | hit .20 | hit .43 |
RESULTS.md@bbc9ffe:7481:     |---|---|---|---|---|
RESULTS.md@bbc9ffe:7482:     | **B2 as run (24/24)** | 0.006 | **0.110** | 0.540 | 0.994 |
RESULTS.md@bbc9ffe:7483:     | at 48/48 | 0.091 | 0.603 | 0.975 | 1.000 |
RESULTS.md@bbc9ffe:7484:     | at 96/96 | 0.527 | 0.982 | 1.000 | 1.000 |
RESULTS.md@bbc9ffe:7485:     | *theirs, OLMo cell (~800/80)* | *0.650* | *1.000* | *1.000* | *1.000* |
```
### :7499-7502 -- 'Their own cell is ~800/80' and its power (round 3)
```
RESULTS.md@bbc9ffe:7499:     figures above put that at **96 injected / 96 control per stage** (power
RESULTS.md@bbc9ffe:7500:     0.98), not 24/24. Their own cell is ~800/80, which reaches
RESULTS.md@bbc9ffe:7501:     power 1.000 at 10.8% and still 0.650 against an effect as small as
RESULTS.md@bbc9ffe:7502:     5% — that row is scale, not a target. Code delivers the arithmetic;
```
### :12565-12576 -- lineage match from their released code
```
RESULTS.md@bbc9ffe:12565:   - **Macar-checkpoint match: CONFIRMED from their released code**
RESULTS.md@bbc9ffe:12566:     (CLAUDE.md now requires this). `src/model_utils.py` maps
RESULTS.md@bbc9ffe:12567:     `olmo_base/sft/dpo/instruct` to exactly the four repos acquired;
RESULTS.md@bbc9ffe:12568:     README §3.3 states "base → SFT → DPO → instruct"; no Think-branch
RESULTS.md@bbc9ffe:12569:     reference exists in the repo. **Their precision matches ours:**
RESULTS.md@bbc9ffe:12570:     `ModelWrapper` defaults to `dtype=torch.bfloat16`,
RESULTS.md@bbc9ffe:12571:     `quantization_config` defaults to None, and `PRE_QUANTIZED_MODELS`
RESULTS.md@bbc9ffe:12572:     contains only `kimi_k2`/`deepseek_v3` — OLMo is not quantized in
RESULTS.md@bbc9ffe:12573:     their pipeline. A Q2 replication failure therefore cannot be
RESULTS.md@bbc9ffe:12574:     attributed to a precision mismatch. (Their layer sweep used
RESULTS.md@bbc9ffe:12575:     25/32/38/45/51 — context only; rule 1 still forbids inheriting the
RESULTS.md@bbc9ffe:12576:     choice.)
```

### data/olmo/b2r_valuescheck.json@bbc9ffe (the committed artifact cited at RESULTS.md@bbc9ffe:7175)
```
1_g3A_power.detail: joint=0.9642 >= 0.90
2_tables.detail:    §0.2 exact; §0.6 means [np.float64(0.1945), np.float64(0.4049), np.float64(0.4455), np.float64(0.1833)]
```
Both are result strings. The file records neither the rates nor the method behind the power figure. It entered at ae73caa, whose files are RESULTS.md, data/olmo/b2r_valuescheck.json, scripts/b2r_analyze.py, scripts/box_b2r_sampling_smoke.py. Lines containing each term (case-insensitive), in that commit's scripts:

| commit | script | 'power' | 'clopper' | 'valuescheck' | lines with 'power' |
|---|---|---|---|---|---|
| ae73caa | scripts/b2r_analyze.py | 2 | 6 | 0 | [16, 91] |
| ae73caa | scripts/box_b2r_sampling_smoke.py | 0 | 0 | 0 | [] |
| bbc9ffe | scripts/b2r_analyze.py | 2 | 6 | 0 | [16, 91] |
| bbc9ffe | scripts/box_b2r_sampling_smoke.py | 0 | 0 | 0 | [] |

In b2r_analyze.py@bbc9ffe 'power' appears at :16 (docstring) and :91 (a reading string), and 'clopper' at :10 (docstring), :49 (import) and :60, :61, :74, :112 (interval calls on data). Code read b2r_analyze.py@bbc9ffe in full (300 lines) and found no power computation. box_b2r_sampling_smoke.py has no line with any of the three terms at either commit, and neither script names the valuescheck file. Code found no committed code that produces 0.9642.

### Carrier search (rounds 2-4): every line of the record that carries each figure

Round 3 added the last two patterns (the ~800/80 n and the ~33× ratio derived from it).

One regex per figure, run over every line of RESULTS.md@bbc9ffe (13051 lines) and ADDENDUM-g3-b2r-v1.2.md@bbc9ffe (307 lines). The script asserts that the hits are exactly the carriers listed below plus the 20 lines listed as unrelated (Code read each one), so these lists are complete for these patterns; a value written another way (for example in words) would not be found. Section 0 takes its locators from here. The regexes:

- source base TPR 0.1%: `(?<![0-9.])0\.1%`
- source sft TPR 14.9%: `(?<![0-9.])14\.9(?![0-9])`
- source dpo TPR 2.9%: `(?<![0-9.+])2\.9(?![0-9])`
- source instruct TPR 0.9%: `(?<![0-9.])0\.9(?:%| vs)`
- source base FPR 16.4%: `(?<![0-9.])16\.4(?![0-9])|(?<![0-9.])0?\.164(?![0-9])`
- source sft FPR 22.5%: `(?<![0-9.])22\.5(?![0-9])|(?<![0-9.])0?\.225(?![0-9])`
- source dpo FPR 0%: `drop to 0%|\| 0\.0% \||2\.9 vs 0\.0|\| 0\.000 \| 91/96`
- source instruct FPR as recorded (0.3%): `(?<![0-9.])0\.3%|0\.9 vs 0\.3|(?<![0-9.])0?\.003(?![0-9])`
- source TPR - FPR at base/sft/dpo: `16\.3 pp|7\.6 pp|\+2\.9 pp`
- source instruct TPR - FPR +0.6 pp: `0\.6 pp`
- [g3-A] joint power 0.9642 / 0.964: `0\.9642|(?<![0-9.])0\.964(?![0-9])`
- single weakest pair 0.9825: `0\.9825`
- p ~ .28 for 0/43 at 2.9%: `p ≈ 0?\.28`
- ~800 injected / ~80 control (the n): `~800|800/80`
- ~33× ours (the injected-trial ratio): `(?<![0-9.])33 ?[×x](?![0-9])`

| figure | RESULTS.md@bbc9ffe | ADDENDUM-g3-b2r-v1.2.md@bbc9ffe | other tracked .py/.md carriers at bbc9ffe | matched but unrelated |
|---|---|---|---|---|
| source base TPR 0.1% | :7338 | :43 | scripts/b2r_analyze.py:175, scripts/b2r_scorer_selftest.py:119, valence_core/detection_v2.py:36 | RESULTS :12905 (an MLX numerics residual (~0.1%)) |
| source sft TPR 14.9% | :6769, :6954, :7090, :7339, :7348 | :44 | none | none |
| source dpo TPR 2.9% | :6769, :6954, :6955, :7090, :7091, :7340, :7348, :7356 | :45, :212 | scripts/b2r_analyze.py:24, scripts/b2r_analyze.py:138 | RESULTS :5830 (a low-label-mass share (4/138)); RESULTS :12225 (a choice-channel mass-map cell, a token probability written 2.9e-5) |
| source instruct TPR 0.9% | :7341, :7356 | :46 | none | none |
| source base FPR 16.4% | :6996, :7193, :7252, :7270, :7338, :7374 | :43, :133, :148 | HANDOFF-2026-08-25.md:60, scripts/b2r_analyze.py:13, scripts/b2r_analyze.py:161, scripts/b2r_analyze.py:175, scripts/b2r_scorer_selftest.py:119, valence_core/detection_v2.py:36 | RESULTS :4727 (a per-layer difference-vector norm/cosine table cell); RESULTS :10104 (an exclusion tolerance (16.4%)); RESULTS :11246 (a mean span length (16.4)) |
| source sft FPR 22.5% | :6909, :6997, :7011, :7193, :7270, :7339, :7374 | :44, :133 | HANDOFF-2026-08-25.md:60, scripts/b2r_analyze.py:13, scripts/b2r_analyze.py:161 | none |
| source dpo FPR 0% | :6998, :7340, :7347, :7356 | :45 | HANDOFF-2026-08-25.md:60, scripts/b2r_analyze.py:161 | none |
| source instruct FPR as recorded (0.3%) | :6999, :7341, :7356 | :46 | HANDOFF-2026-08-25.md:60, scripts/b2r_analyze.py:161 | RESULTS :4722 (a per-layer difference-vector norm/cosine table cell); RESULTS :4728 (a per-layer difference-vector norm/cosine table cell); RESULTS :4729 (a per-layer difference-vector norm/cosine table cell); RESULTS :4731 (a per-layer difference-vector norm/cosine table cell); RESULTS :6941 (the source's Gemma identification-given-claim rate (0.003)); RESULTS :7470 (the source's Gemma identification-given-claim rate (0.003)); RESULTS :9082 (a between-stage agreement (~0.003)); RESULTS :11079 (an amplitude difference (0.003 G)); RESULTS :11115 (an amplitude difference (0.003 G)); ADDENDUM :102 (the source's Gemma identification-given-claim rate (0.003)) |
| source TPR - FPR at base/sft/dpo | :7329, :7338, :7339, :7340 | :43, :44, :45 | none | none |
| source instruct TPR - FPR +0.6 pp | :7330, :7341 | :46 | scripts/b2r_analyze.py:15 | none |
| [g3-A] joint power 0.9642 / 0.964 | :7173, :7180, :7192, :7194, :7251, :7269, :7270 | :148, :273 | none | RESULTS :4402 (an echo-probe AUC in prose (0.964)); RESULTS :4460 (a per-layer echo-probe AUC table cell); RESULTS :4657 (a per-layer echo-probe AUC table cell); RESULTS :9067 (a per-stage axis-geometry table cell (0.964)) |
| single weakest pair 0.9825 | :7192, :7268 | none | none | none |
| p ~ .28 for 0/43 at 2.9% | :6955, :7091 | none | none | none |
| ~800 injected / ~80 control (the n) | :7365, :7439, :7485, :7500 | :32 | AUDIT-note-release-v1_2.md:34 | none |
| ~33× ours (the injected-trial ratio) | :7440 | :32 | none | none |

Other tracked .py/.md files at bbc9ffe (RESULTS.md, the addendum and results/raw/ excluded), one `git grep -E` with `(^|[^0-9.])(0\.1|14\.9|2\.9|0\.9|16\.4|22\.5|0\.3)%|\.164 ?/ ?\.225|0\.164 / 0\.225|\+0\.6 pp|0\.9 vs 0\.3|0\.9642|0\.9825`: 12 hits, 9 carriers and 3 unrelated. Carriers: HANDOFF-2026-08-25.md:60 (the four FPRs .164 / .225 / .000 / .003); scripts/b2r_analyze.py:13 (base/sft FPR 16.4%/22.5% (docstring)); scripts/b2r_analyze.py:15 (instruct +0.6 pp (docstring)); scripts/b2r_analyze.py:24 (dpo TPR 2.9% (docstring)); scripts/b2r_analyze.py:138 (dpo TPR 2.9% (a reading string)); scripts/b2r_analyze.py:161 (self-test fixture .164/.225/.000/.003); scripts/b2r_analyze.py:175 (base TPR 0.1% / FPR 16.4% (comment)); scripts/b2r_scorer_selftest.py:119 (base TPR 0.1% / FPR 16.4% (comment)); valence_core/detection_v2.py:36 (base TPR 0.1% / FPR 16.4% (docstring)). Unrelated: LOCK-h.md:262 (an exclusion tolerance (16.4%)); archive/RESULTS-cycle1-2.md:1022 (a cycle-1/2 effect size (0.1%)); scripts/e2b_h1_sessions.py:14 (an exclusion tolerance (16.4%)). These are code comments, a self-test fixture and a handoff, not log lines; they are listed so that a correction to a source value can find every copy. None is edited (read-only).

Round 3, a second `git grep -E` over the same files with `~800|800/80|(^|[^0-9.])33 ?[×x]([^0-9]|$)` (the two round-3 patterns): 1 hit, AUDIT-note-release-v1_2.md:34 (the block's premise, '800/80 per configuration' (the audit block, not the record)).

Round 4, two `git grep -E` runs over every tracked .py/.md file at bbc9ffe with RESULTS.md and the addendum included (results/raw/ excluded), each asserted to return exactly the lines below. They cover rows 19 and 24 of section 0, which the per-figure search above does not:

- the retired criterion's Instruct power, in prose: `power 0\.000|0\.000 at n|0\.020 at|0\.001 at n`: 3 hits. Carriers: ADDENDUM-g3-b2r-v1.2.md:53 (0.000 at n = 48 and 0.020 at n = 200 ('their own Instruct rates')); RESULTS.md:7331 (0.000 / 0.001 / 0.020 at n = 48 / 96 / 200 ('Instruct's own reported rates')); scripts/b2r_analyze.py:16 (docstring, 0.000 at n=48). Unrelated: none.
- 'n in the thousands' for conventional power at Instruct: `thousands`: 2 hits. Carriers: RESULTS.md:7364 ('Reaching conventional power there needs n in the thousands per cell'). Unrelated: archive/CLAUDE-cycle1-2.md:379 (a cycle-1/2 vector length ('tens of thousands of dims')).

Row 19's table cells (RESULTS.md@bbc9ffe:7358-7361) are written '| **0.000** |' and so on, which the first pattern does not match; the script locates them by parsing the table (section 6b).

## 3. Code's reading of the source (URLs, versions, what each holds)

Paper: Macar, Yang, Wang, Wallich, Ameisen, Lindsey, 'Mechanisms of Introspective Awareness', arXiv:2603.21396. Abstract page https://arxiv.org/abs/2603.21396; version list from https://arxiv.org/abs/2603.21396v5: v1 2026-03-22, v2 2026-04-10, v3 2026-04-13, v4 2026-05-15, v5 2026-06-10 (UTC dates as listed).

| version | date | URL read | OLMo per-stage content, as Code read it |
|---|---|---|---|
| v1 | 2026-03-22 | https://arxiv.org/html/2603.21396v1 | Appendix C 'Introspection Across OLMo-3.1-32B's Training Pipeline': one paragraph stating per-stage TPR and FPR in prose (it opens by naming Figure 21); Figure 21 caption: rates aggregated across L in [25,32,38,45,51] with alpha in [1,2,4,8]; the figure is an image (olmo-staged-introspection.png, alt text 'Refer to caption') with no data table. Section 3.3 ('The Role of Post-Training') points to Appendix C and also says in text that base and SFT have high FPR, which reaches 0% only after DPO (no per-stage TPR numbers there). No per-(layer, alpha) breakdown; no n; no concept count. |
| v2 | 2026-04-10 | https://arxiv.org/html/2603.21396v2 | Appendix C is 'Abliterated Model Details' (no OLMo). OLMo per-stage results are Figure 5 (Section 3.3) at L=25, alpha in {1,2,4,8}, over the original 50 Lindsey (2025) concepts, plus Appendix D.1 Figure 20 at L=19 and L=22. No numeric per-stage TPR/FPR in text. Table 3 is a LoRA fine-tuning study on the OLMo SFT checkpoint (L=25, alpha=4); its starred official-checkpoint rows read TPR-FPR SFT* -11.5 +/- 2.4, DPO* +9.8 +/- 0.5. |
| v3 | 2026-04-13 | https://arxiv.org/html/2603.21396v3 | Same structure as v2 (Appendix C abliteration; OLMo in Figure 5 at L=25; D.1 at L=19/22); no numeric per-stage TPR/FPR in text. |
| v4 | 2026-05-15 | https://arxiv.org/html/2603.21396v4 | Appendix C 'Refusal Direction Ablation (Abliteration) Details'; OLMo Figure 5 at L=25, alpha in {1,2,4,8}; D.1 is Figure 21 (OLMo base/SFT/DPO/instruct at L=19 and L=22, alpha in {1,2,4,8}); no numeric per-stage TPR/FPR in text; Table 3 (LoRA fine-tuning of the OLMo SFT checkpoint under different training conditions, L=25, alpha=4, 11 rows as Code read it) includes the starred SFT* and DPO* rows with the v2 values. |
| v5 | 2026-06-10 | https://arxiv.org/html/2603.21396v5 | As v4; D.1 figure is Figure 22 (L=19, L=22); no numeric per-stage TPR/FPR in text; official SFT*/DPO* TPR-FPR -11.5 +/- 2.4 / +9.8 +/- 0.5 at L=25, alpha=4 (Table 3, Section 3.3; Code's fetch also named a Table 8 in D.2 carrying the same two rows). |

**Which version the record's numbers come from.** The addendum (written 2026-08-24, when v5 was current) cites 'arXiv:2603.21396 Appendix C, Fig 21' with no version. Only v1 has an Appendix C on OLMo and a Figure 21 with the [25,32,38,45,51] x [1,2,4,8] aggregation. In v4 a Figure 21 also exists and also shows the four OLMo stages, but it is the Appendix D.1 figure at L = 19 and L = 22, so an unversioned 'Fig 21' resolves to a different OLMo-stage figure there. In v2-v5 the numbers 0.1% / 14.9% / 2.9% / 0.9% are not in the text: the OLMo stage comparison is presented at a single layer (L = 25) over 50 concepts, with per-stage values only in figures. Code did not find a statement of why the presentation changed, and does not infer one.

**v1 Appendix C, per stage (prose; the paragraph opens by naming Figure 21).** This raw keeps to one short quotation from the source (the SFT sentence). For the other three stages it gives only the numbers, in Code's words, each exactly as the text prints it:

- base: TPR 0.1%, FPR 16.4% (in the paragraph's first sentence, which names Figure 21).
- sft: TPR 14.9%, FPR 22.5% (the sentence quoted below).
- dpo: FPR falls to 0% and TPR to 2.9%.
- instruct: FPR stays at 0%; TPR 0.9%; introspection rate 0.3%.

The one quotation: "Supervised fine-tuning improves detection (14.9% TPR) but maintains high false positives (22.5%)." (Macar et al. 2026, arXiv:2603.21396v1, Appendix C).

v1 Figure 21's caption names the four stages in pipeline order and says the rates are aggregated across L in [25, 32, 38, 45, 51] with alpha in [1, 2, 4, 8]. The figure is an image (2603.21396v1/olmo-staged-introspection.png, alt text 'Refer to caption'); the v1 HTML carries no data table or numeric labels for it and no per-(layer, alpha) breakdown. Code did not digitize the figure (no image was fetched).

v1 Section 3.3 ('The Role of Post-Training') also carries the OLMo stage result in the main text, qualitatively: it points to Appendix C and says that base and SFT have high FPR and that FPR reaches 0% only after DPO, with no per-stage TPR numbers. The record quotes that sentence at RESULTS.md@bbc9ffe:7346-7347 (section 2).

Metric definitions (v1, Section 2/Appendix B as Code read them): TPR = P(detect | injection) over injection trials; FPR = P(detect | no injection) over control trials; introspection rate = P(detect and identify | injection) over injection trials.

Released code (https://github.com/safety-research/introspection-mechanisms, sha 5d5d9b485e293dc766c3a056cfe50283a7e435b6; the commits page https://github.com/safety-research/introspection-mechanisms/commits/main showed 5d5d9b4, 2026-04-16, as the newest commit on main when read). Pages read: https://github.com/safety-research/introspection-mechanisms/blob/5d5d9b485e293dc766c3a056cfe50283a7e435b6/README.md; https://raw.githubusercontent.com/safety-research/introspection-mechanisms/5d5d9b485e293dc766c3a056cfe50283a7e435b6/README.md; https://github.com/safety-research/introspection-mechanisms/blob/5d5d9b485e293dc766c3a056cfe50283a7e435b6/src/model_utils.py; https://raw.githubusercontent.com/safety-research/introspection-mechanisms/5d5d9b485e293dc766c3a056cfe50283a7e435b6/src/model_utils.py; https://raw.githubusercontent.com/safety-research/introspection-mechanisms/5d5d9b485e293dc766c3a056cfe50283a7e435b6/experiments/03_behavioral_robustness.py.

- `src/model_utils.py` MODEL_NAME_MAP (no revision pinned): olmo_base -> allenai/Olmo-3-1125-32B; olmo_sft -> allenai/Olmo-3.1-32B-Instruct-SFT; olmo_dpo -> allenai/Olmo-3.1-32B-Instruct-DPO; olmo_instruct -> allenai/Olmo-3.1-32B-Instruct.
- `get_layer_at_fraction`: layer_idx = int(model_wrapper.n_layers * fraction), clamped to [0, n_layers-1].
- dtype: torch.bfloat16 (ModelWrapper default; OLMo not in PRE_QUANTIZED_MODELS).
- `experiments/03_behavioral_robustness.py` defaults: OLMO_MODELS = ['olmo_base', 'olmo_sft', 'olmo_dpo', 'olmo_instruct']; DEFAULT_TEST_CONCEPTS_len = 50; DEFAULT_LAYER_SWEEP = [0.4, 0.5, 0.6, 0.7, 0.8]; DEFAULT_STRENGTH_SWEEP = [1.0, 2.0, 4.0, 8.0]; DEFAULT_N_BASELINE = 100; DEFAULT_MAX_TRIAL_NUMBER = 10; DEFAULT_SAMPLES_PER_TRIAL = 10; DEFAULT_CONTROL_SAMPLES_PER_TRIAL = 1; DEFAULT_MAX_TOKENS = 100; DEFAULT_TEMPERATURE = 1.0; seed_default = 42.
- -m takes choices=OLMO_MODELS + ['all']; -ls is type=float, help 'Layer fractions to sweep (default: 0.4 0.5 0.6 0.7 0.8)'.
- Seeding: random.seed, np.random.seed, torch.manual_seed and torch.cuda.manual_seed_all(args.seed) once, in main(), at startup; no per-model, per-configuration or per-trial seeding.
- Generation: do_sample = temperature > 0; no top_p or top_k passed (whatever the generation config supplies applies; Code did not read the checkpoints' generation_config.json).
- Trials: run_experiment calls run_concept_trials for every (layer fraction, strength, concept); injected loop = max_trial_number x samples_per_trial; control loop = max_trial_number x control_samples_per_trial, i.e. controls are re-run per (layer, strength, concept) cell.
- Metrics: detection_rate = claims_detection / len(evaluated_injection); false_positive_rate = false_positives / len(evaluated_control); per-(layer fraction, strength) blocks in plots/{model}_summary.txt; per-model pooled over all cells in summary_stats.json; no per-concept metric.
- Trial prompt: run_experiment sets is_base_model when model_name == 'olmo_base' or the tokenizer has no chat template; run_single_trial then uses build_base_model_prompt, otherwise build_instruct_model_prompt (the tokenizer's chat template, falling back to the base format when apply_chat_template is absent). build_base_model_prompt is not bare: it writes plain-text 'User:' / 'Assistant:' turns with no chat template (the introspection explanation as a User turn, an 'Assistant: Ok.' turn, then the 'Trial N' detection question as a User turn, ending at 'Assistant:'). The bare 'Tell me about {word}' template appears only in extract_concept_vector_base_model, i.e. the base model's concept-vector extraction, not its trials.
- README OLMo command: `python experiments/03_behavioral_robustness.py -m olmo_32b_base olmo_32b_sft olmo_32b_dpo olmo_32b -ls 25 32 38 45 51 -ss 1 2 4 8`.

Fixer-pass reads (same date, same tool):
- https://raw.githubusercontent.com/safety-research/introspection-mechanisms/5d5d9b485e293dc766c3a056cfe50283a7e435b6/experiments/03_behavioral_robustness.py: build_base_model_prompt and the base/chat-template switch in run_experiment / run_single_trial; the 'Tell me about {word}' template's location.
- https://arxiv.org/html/2603.21396v1: Section 3.3's base-model prompt format; whether any passage gives an OLMo-specific format (characters 0-100000, which hold Section 3.3 and Appendix C, and 100000-end).
- https://arxiv.org/html/2603.21396v4: the list of OLMo figures (characters 0-100000 and 100000-end): Figure 5 in Section 3.3, Figure 21 in Appendix D.1.
- https://arxiv.org/html/2603.21396v4: Table 3's caption, study, layer/alpha, row count and starred rows.

Round-2 reads (2026-10-08, same tool, two fetches of the page, agreeing):
- https://arxiv.org/html/2603.21396v1: Section 3.3 'The Role of Post-Training' (main text, characters 0-100000): one sentence points to Appendix C for OLMo-3.1-32B and says, with no per-stage TPR numbers, that the base and SFT checkpoints have high FPR, which reaches 0% only after DPO; it is the sentence the record quotes at RESULTS.md@bbc9ffe:7346-7347 (both fetches returned the same wording).
- https://arxiv.org/html/2603.21396v1: Figure 21's form: an image, 2603.21396v1/olmo-staged-introspection.png, alt text 'Refer to caption'; the HTML carries no data table and no numeric labels for it beyond the caption (both fetches).

Round-3 reads (2026-10-08, same tool, the same file twice with different prompts):
- https://raw.githubusercontent.com/safety-research/introspection-mechanisms/5d5d9b485e293dc766c3a056cfe50283a7e435b6/experiments/03_behavioral_robustness.py: DEFAULT_TEST_CONCEPTS: read 1 (asked whether it is defined or imported, its entries in order, and every top-level import) returned a literal list defined in this file, under a one-line comment describing it as the paper's 50 baseline words, with 50 entries (listed in EXP03_CONCEPTS_READ1), and no import of the name.
- https://raw.githubusercontent.com/safety-research/introspection-mechanisms/5d5d9b485e293dc766c3a056cfe50283a7e435b6/experiments/03_behavioral_robustness.py: DEFAULT_TEST_CONCEPTS: read 2 (asked for the assignment character for character) declined to copy the full list, and confirmed the comment line, 50 entries in 10 lines of 5, first entry 'Dust', last 'Silver', the name in no import statement, and its use as the --concepts default.

## 4. The record's values against the source, cell by cell

Record A = ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:43-46 (section 0.2 table). Record B = RESULTS.md@bbc9ffe:6996-6999 (B2-r verdict, 'theirs' column, FPR only). Source = v1 Appendix C text. TPR's domain is injected trials and FPR's is control trials, each pooled over the 20 (layer, alpha) configurations; the source states neither denominator (section 5).

| stage | TPR record A | TPR source | match | FPR record A | FPR record B | FPR source | match | introspection rate, source | record A TPR-FPR | source TPR-FPR (computed-new) |
|---|---|---|---|---|---|---|---|---|---|---|
| base | 0.001 | 0.001 | yes | 0.164 | 0.164 | 0.164 | yes | null | −16.3 pp | -16.3 pp |
| sft | 0.149 | 0.149 | yes | 0.225 | 0.225 | 0.225 | yes | null | −7.6 pp | -7.6 pp |
| dpo | 0.029 | 0.029 | yes | 0.000 | 0.000 | 0.000 | yes | null | +2.9 pp | +2.9 pp |
| instruct | 0.009 | 0.009 | yes | 0.003 | 0.003 | 0.000 | NO | 0.003 | +0.6 pp | +0.9 pp |

TPR: 4/4 cells match the source text. FPR: 3/4 cells match. The instruct FPR the record carries (0.3%, in both A and B) is the figure the v1 sentence gives as the instruct checkpoint's introspection rate; the same sentence gives the instruct FPR as 0%. Code reads this as a transcription slip in the record (Code's reading, not established). The record says it recovered the values 'from the paper (Appendix C, Fig 21)' (RESULTS.md@bbc9ffe:7327), and Figure 21 is an image (2603.21396v1/olmo-staged-introspection.png) that this audit did not digitize, so a reading of the figure is not excluded and whether its plotted instruct FPR differs from the text is not known. Under block :23 the classification decides the consequence for a note that carries the 0.3% (section 12).

## 5. Grid, n, and the layer arithmetic (computed-new from the source code's defaults)

- n_layers per stage from data/olmo/rl_{stage}.json@bbc9ffe field `n_layers`: base 64, sft 64, dpo 64, instruct 64.
- int(n_layers x f) for the code's DEFAULT_LAYER_SWEEP [0.4, 0.5, 0.6, 0.7, 0.8]: [25, 32, 38, 44, 51]. round(n_layers x f): [26, 32, 38, 45, 51]. The v1 caption lists [25, 32, 38, 45, 51]. int() differs from the caption at the fourth layer (44 vs 45; 64 x 0.7 = 44.8 truncates to 44); round() differs at the first (26 vs 25; 64 x 0.4 = 25.6). Neither rule yields the caption's list. Not adjudicated: the source does not say which ran.
- The README command as written cannot run at 5d5d9b4: its -m keys ['olmo_32b_base', 'olmo_32b_sft', 'olmo_32b_dpo', 'olmo_32b'] are not among the choices ['olmo_base', 'olmo_sft', 'olmo_dpo', 'olmo_instruct', 'all'] (4/4 not accepted), so argparse would refuse it before any forward, and its -ls values [25.0, 32.0, 38.0, 45.0, 51.0], read as fractions, give int(64 x f) clamped = [63, 63, 63, 63, 63]. Its layer list nonetheless equals the v1 caption's 5/5, which neither int() (4/5) nor round() (4/5) of the default fractions does. That is consistent with absolute layers 25/32/38/45/51 having been run by some path other than the README command as written, rather than the default fractions (the record reads it the same way: RESULTS.md@bbc9ffe:7396-7398). Not adjudicated; it bears on note 5 (L_M = 44 against the caption's 45).
- Configurations aggregated per stage: 5 layers x 4 strengths = 20.
- Per (layer, alpha, concept) cell under the code's defaults: 100 injected (10 trial numbers x 10 samples) and 10 control (10 x 1).

| scenario | per (layer, alpha) cell: injected / control | per stage, pooled over 20 cells: injected / control |
|---|---|---|
| eight concepts (the record's assumption, RESULTS.md@bbc9ffe:7438-7440) | 800 / 80 | 16000 / 1600 |
| the code's default DEFAULT_TEST_CONCEPTS (50) | 5000 / 500 | 100000 / 10000 |

Neither row is stated by the source. v1 gives no n and no concept count for the OLMo runs; v2-v5 state 50 concepts for the reworked L = 25 figure. The released code's denominators are the *evaluated* trials (`len(evaluated_injection)`, `len(evaluated_control)`), so realized n may be below these counts by an unknown amount. Any d-prime or Fisher test on the source's points (N2(v)) has to declare its assumed n. The block's '800/80 per configuration' is the first row's per-cell figure.

Where the eight comes from: it is our own B2 registration, not a source count. data/configs/b2_concepts.json@bbc9ffe records `n_canonical` = 50 (`canonical_concepts`, 50 entries; `provenance.concepts_source` cites experiments/01_concept_injection.py:58's DEFAULT_TEST_CONCEPTS, with its comment '50 words from the paper') and `selection_for_B2.registered_n` = 8, with the note that the source has no canonical eight to recover. The 50 in section 3's defaults and in the table above is a different file's: the OLMo experiment, experiments/03_behavioral_robustness.py, defines its own DEFAULT_TEST_CONCEPTS as a literal list in that file, not an import from 01 (both round-3 reads, section 3). On the first read its 50 entries equal `canonical_concepts` entry for entry and in order (computed-new). The second read confirmed only the count, the first and last entries and that the name is imported nowhere, so the identity of 03's list with 01's rests on one model-processed read: Code's reading, not established. The count, 50, does not depend on it. The unit also matters: each per-cell figure is one (layer, alpha) configuration's n, while every source rate is pooled over all 20. A test of a pooled rate under the same premise uses the pooled column (section 7 gives both). Pooled counts still treat trials clustered by configuration and concept as independent, so neither unit gives an exact test of the source's aggregate.

## 6. Record figures that depend on the instruct FPR, recomputed (computed-new)

Code: the record's own `clopper_pearson` and `newcombe` (scripts/b2_analyze.py@bbc9ffe) and `binom_pmf` (valence_core/stats.py@bbc9ffe), compiled from git show and run in an isolated namespace. An independent stdlib Clopper-Pearson agrees with the record's at n = 96 for every k = 0..96 (max abs difference 1.1e-15). All probabilities are exact enumerations over the binomial outcomes; no simulation, no seed.

**(a) [g3-A] joint power** (record: 0.9642, ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:147-148, :273; RESULTS.md@bbc9ffe:7173, :7180, :7189-7194, :7251, :7268-7270; data/olmo/b2r_valuescheck.json@bbc9ffe field 1_g3A_power.detail). Rule as the record states it (RESULTS.md@bbc9ffe:7266-7268): min CP-lower over {base, sft} > max CP-upper over {dpo, instruct}; 95% two-sided exact Clopper-Pearson per stage; FPR counts k_s ~ Binomial(96, rate_s) per stage, independent, all 96 decidable.

| inputs (base / sft / dpo / instruct FPR) | joint power | base > dpo | base > instruct | sft > dpo | sft > instruct | weakest single pair |
|---|---|---|---|---|---|---|
| record: .164 / .225 / .000 / .003 | 0.96455 | 0.98296 | 0.96540 | 0.99978 | 0.99901 | base > instruct |
| source v1 text: .164 / .225 / .000 / .000 | 0.98274 | 0.98296 | 0.98296 | 0.99978 | 0.99978 | base > dpo = base > instruct (tied) |
| record's printed values | 0.9642 | 0.9825 (labelled 'single weakest pair (base vs dpo)') | not printed | not printed | not printed | base vs dpo, per the label |

At the record's inputs the exact joint power is 0.9645485: 0.9645 at 4 dp against the printed 0.9642 (residual -0.0003) and 0.965 at 3 dp, against the record's own claim of exactness at 3 dp ('the exact number is 0.964', RESULTS.md@bbc9ffe:7194; 'the exact figure is 0.964', :7269-7270; 'the CONTROL tier's joint figure is 0.964', :7251). So the figure is discrepant at the record's own stated precision, not only at 4 dp. The base > dpo pair is 0.9830 against 0.9825 (-0.0005). The record's other printed operands do reproduce: Base CP lower at 16/96 (the expected count .164 x 96, rounded) = 0.0984 (record 0.0984) and DPO CP upper at 0/96 = 0.0377 (record 0.0377), RESULTS.md@bbc9ffe:7189-7190.

**The weakest-pair label.** At the record's own inputs the weakest single pair is base > instruct (0.9654), not base > dpo (0.9830); the joint (0.9645) sits just below it. The record's 'single weakest pair (base vs dpo)' (RESULTS.md@bbc9ffe:7268; also :7192, 'not the single weakest pair (0.9825)') holds only when the instruct FPR equals the dpo FPR, as under the source's 0%, where base > dpo and base > instruct tie at 0.9830. At .003, 0 of the four pairs equals 0.9825 at 4 dp.

**Cause of the residual: not identified.** The record does not state whether its power was enumerated or simulated, and no committed code computes it (section 2). Deterministic variants Code tried (computed-new, none of them the record's stated method):

| variant (all else as above, record inputs) | joint | base > dpo | reproduces both printed values at 4 dp |
|---|---|---|---|
| Wilson score 95% intervals in place of CP | 0.98192 | 0.99285 | no |
| Clopper-Pearson at 90% (alpha .10) | 0.99147 | 0.99739 | no |
| n = 95 per stage | 0.96167 | 0.98118 | no |
| base FPR .163 (one unit lower at 3 dp) | 0.96277 | 0.98189 | no |

A simulated (Monte Carlo) estimate would carry sampling error. With the exact values as the truth, its standard errors and the printed residuals in SE units would be: 10,000 draws: SE 0.00129 (pair) / 0.00185 (joint), residuals -0.35 / -0.19 SE; 100,000 draws: SE 0.00041 (pair) / 0.00058 (joint), residuals -1.12 / -0.60 SE; 1,000,000 draws: SE 0.00013 (pair) / 0.00018 (joint), residuals -3.53 / -1.88 SE. So both printed values are consistent with a simulation of roughly 10^4 to 10^5 draws. That is a candidate, not an established cause: no simulation code, draw count or seed is committed. A simulation error would not be a transcription. Either way 0.9642 is consistent with an instruct input of .003 and not with .000, which gives 0.9827. Under the source's instruct FPR the joint power rises by +0.0182. Both values clear the 0.90 bar the values-check applied (RESULTS.md@bbc9ffe:7180). Block :23's consequence for the note is in section 12.

**(b) The retired criterion's power** (RESULTS.md@bbc9ffe:7354-7361 table; the same Instruct figures at ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:52-53 and RESULTS.md@bbc9ffe:7330-7331). Read as P(Newcombe lower bound > 0) at n per arm, all decidable ('perfect controls', RESULTS.md@bbc9ffe:7354), hits ~ Binomial(n, TPR) and false alarms ~ Binomial(n, FPR) independent; the Newcombe interval is the record's (two 95% two-sided CP intervals), and 'lower > 0' is the registered B2 rule (scripts/b2_analyze.py@bbc9ffe:119). Outcomes with probability below 1e-15 are skipped; the largest skipped mass in any cell is 9.4e-16, an upper bound on the error.

| n per arm | DPO (2.9 vs 0.0): record | recomputed | Instruct (0.9 vs 0.3): record | recomputed | Instruct (0.9 vs 0.0, source FPR): computed-new |
|---|---|---|---|---|---|
| 24 | 0.001 | 0.001 | 0.000 | 0.000 | 0.000 |
| 48 | 0.012 | 0.012 | 0.000 | 0.000 | 0.000 |
| 96 | 0.147 | 0.147 | 0.001 | 0.001 | 0.002 |
| 200 | 0.691 | 0.691 | 0.020 | 0.020 | 0.036 |

8/8 printed cells agree with the recomputation to three decimals. That supports the reading above as the record's method (the record does not spell it out), and it shows the table used instruct FPR .003: at .000 the n = 96 and n = 200 cells would print differently. At the source's instruct FPR (.000) the Instruct power is 0.000 / 0.000 / 0.002 / 0.036 at n = 24 / 48 / 96 / 200, still far below any conventional bar. The record's conclusion at RESULTS.md@bbc9ffe:7363 ('Instruct is the binding constraint and it is not close') holds at both inputs: at every n of the table the Instruct power is below the DPO power (at n = 200, DPO 0.691 against Instruct 0.020 at 0.3% and 0.036 at 0%).

**The sentence after it (RESULTS.md@bbc9ffe:7363-7364: 'Reaching conventional power there needs n in the thousands per cell').** :7363 holds at both inputs. :7363-7364's "n in the thousands per cell" holds only at the transcribed 0.3%. At the source's 0% the registered criterion reaches 0.80 power at n ≈ 750 per arm (0.8042), and 0.90 at ≈ 890 (0.9020). At 0.3% the figures are ≈ 2700 (0.8011) and ≈ 3500 (0.9001). Same rule and inputs as the table above: P(Newcombe lower > 0), hits ~ Binomial(n, .009), false alarms ~ Binomial(n, FPR), n per arm, all decidable. Each '≈' value is the first point at or above the bar on a step-10 grid from n = 210; the grid rises at every step (0 decreases at either input), and the grid point before each is below the bar (740: 0.7949; 880: 0.8967; 2690: 0.7995; 3490: 0.8992). A step-1 scan between those two grid points gives the first n: at 0%: 0.80 first reached at n = 746 (0.80054; 0.79962 at n = 745), 0.90 first reached at n = 887 (0.90043; 0.89991 at n = 886); at 0.3%: 0.80 first reached at n = 2694 (0.80012; 0.79996 at n = 2693), 0.90 first reached at n = 3500 (0.90008; 0.89999 at n = 3499). 'Per cell' is read as n per arm, the unit of the table the sentence follows (RESULTS.md@bbc9ffe:7356, 'n / arm'; Code's reading). The sentence sits under 'Power at their own numbers' (:7354), so as described it should hold at the source's rates, where 0.90 power needs fewer than 1,000 per arm. Method: the record's binom_pmf multiplies the integer comb(n, k) by floats, so from n = 1030 (the first n at which comb(n, n // 2) exceeds the float range) the record's clopper_pearson raises OverflowError (asserted at n = 1030; it runs at n = 1029). The scan therefore uses the record's newcombe, extracted from scripts/b2_analyze.py@bbc9ffe and compiled with a stdlib Clopper-Pearson (the record's bisection, with tails summed on the short side) and the stdlib pmf. That path agrees with the record's own on all 12 table cells and on the power at n = 750 at the source's rates (record path 0.804214); the largest absolute difference over these 13 values is 1.5e-13. The two Clopper-Pearson functions agree at n = 96 for every k and at n = 750 for every k that power uses (max abs difference 3.7e-14). The largest skipped mass in any scanned cell is 2.7e-15. Block :23's consequence if the note carries the sentence is in section 12, condition 3.

**How the record describes the Instruct figures.** The record presents them as power at the source's own rates: 'power at their own Instruct rates' (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:52-53), 'Power at Instruct's own reported rates' (RESULTS.md@bbc9ffe:7330-7331), and the table under 'Power at their own numbers' (RESULTS.md@bbc9ffe:7354-7361). As described, the figures should equal the power at the source's rates. The record's Instruct cells reproduce at its own transcribed 0.3% (4/4), and at the source's rates they differ at 3 dp in 2 of 4 cells: n = 96: record 0.001, at the source's rates 0.002; n = 200: record 0.020, at the source's rates 0.036. The DPO column's inputs (2.9 vs 0.0) equal the v1 text, so its cells stand as described. Block :23's consequence if the note carries the Instruct figures as at the source's rates is in section 12, condition 3.

## 7. The source's points under an assumed n: d', c and Fisher (computed-new; context for N2(v))

N2(v)'s own output is its own raw. This section checks the design seat's arithmetic for the source's points (block :34: base d' ~ -1.9, SFT ~ -0.3, DPO ~ +0.6 with p ~ .11, instruct ~ +0.15 with p ~ .5, under an assumed 800/80 per configuration) and whether the instruct-FPR correction changes it. Counts = rate x n, rounded half-up on the exact decimal product (expected counts printed; a .5 tie is flagged). d' is log-linear: z((H + 1/2)/(N_s + 1)) - z((FA + 1/2)/(N_n + 1)); c = -(z_H + z_FA)/2. p is a one-sided Fisher exact test on [[H, N_s - H], [FA, N_n - FA]], the hypergeometric upper tail P(X >= H) (excess hits over false alarms); this script's stdlib Fisher equals the record's `fisher_one_sided` (valence_core/stats.py@bbc9ffe) on every row.

**The unit.** 800/80 (like 5000/500) is one (layer, alpha) configuration's n. Every source rate is pooled over all 20 configurations (section 4), so a test of those rates under the same premise uses the pooled per-stage n: 16000/1600 with the record's eight concepts, 100000/10000 with the code's fifty. The block's 800/80 is therefore a per-cell n applied to a pooled rate. Both units are tabulated. Pooled counts still treat trials clustered by configuration and concept as independent, so no row is an exact test of the source's aggregate. The source gives no n (section 5), so every number here carries an assumption, not the source.

| assumed n inj / ctl | unit | point | TPR / FPR | expected H / FA | H / FA | d' | c | one-sided Fisher p |
|---|---|---|---|---|---|---|---|---|
| 800 / 80 | per (layer, alpha) configuration (8 concepts) | base | 0.001 / 0.164 | 0.80 / 13.12 | 1 / 13 | -1.931 | +1.933 | 1.0000 |
| 800 / 80 | per (layer, alpha) configuration (8 concepts) | sft | 0.149 / 0.225 | 119.20 / 18.00 | 119 / 18 | -0.296 | +0.892 | 0.9704 |
| 800 / 80 | per (layer, alpha) configuration (8 concepts) | dpo | 0.029 / 0.000 | 23.20 / 0.00 | 23 / 0 | +0.611 | +2.196 | 0.1085 |
| 800 / 80 | per (layer, alpha) configuration (8 concepts) | instruct | 0.009 / 0.000 | 7.20 / 0.00 | 7 / 0 | +0.151 | +2.427 | 0.5119 |
| 800 / 80 | per (layer, alpha) configuration (8 concepts) | instruct, record FPR .003 | 0.009 / 0.003 | 7.20 / 0.24 | 7 / 0 | +0.151 | +2.427 | 0.5119 |
| 5000 / 500 | per (layer, alpha) configuration (50 concepts) | base | 0.001 / 0.164 | 5.00 / 82.00 | 5 / 82 | -2.086 | +2.019 | 1.0000 |
| 5000 / 500 | per (layer, alpha) configuration (50 concepts) | sft | 0.149 / 0.225 | 745.00 / 112.50 (tie at .5: false_alarms) | 745 / 113 | -0.290 | +0.895 | 1.0000 |
| 5000 / 500 | per (layer, alpha) configuration (50 concepts) | dpo | 0.029 / 0.000 | 145.00 / 0.00 | 145 / 0 | +1.197 | +2.493 | 8.20e-07 |
| 5000 / 500 | per (layer, alpha) configuration (50 concepts) | instruct | 0.009 / 0.000 | 45.00 / 0.00 | 45 / 0 | +0.729 | +2.726 | 0.0135 |
| 5000 / 500 | per (layer, alpha) configuration (50 concepts) | instruct, record FPR .003 | 0.009 / 0.003 | 45.00 / 1.50 (tie at .5: false_alarms) | 45 / 2 | +0.215 | +2.469 | 0.1860 |
| 16000 / 1600 | pooled per stage over 20 configurations (8 concepts) | base | 0.001 / 0.164 | 16.00 / 262.40 | 16 / 262 | -2.103 | +2.030 | 1.0000 |
| 16000 / 1600 | pooled per stage over 20 configurations (8 concepts) | sft | 0.149 / 0.225 | 2384.00 / 360.00 | 2384 / 360 | -0.286 | +0.898 | 1.0000 |
| 16000 / 1600 | pooled per stage over 20 configurations (8 concepts) | dpo | 0.029 / 0.000 | 464.00 / 0.00 | 464 / 0 | +1.525 | +2.658 | 3.34e-20 |
| 16000 / 1600 | pooled per stage over 20 configurations (8 concepts) | instruct | 0.009 / 0.000 | 144.00 / 0.00 | 144 / 0 | +1.056 | +2.893 | 1.03e-06 |
| 16000 / 1600 | pooled per stage over 20 configurations (8 concepts) | instruct, record FPR .003 | 0.009 / 0.003 | 144.00 / 4.80 | 144 / 5 | +0.339 | +2.534 | 0.0055 |
| 100000 / 10000 | pooled per stage over 20 configurations (50 concepts) | base | 0.001 / 0.164 | 100.00 / 1640.00 | 100 / 1640 | -2.111 | +2.033 | 1.0000 |
| 100000 / 10000 | pooled per stage over 20 configurations (50 concepts) | sft | 0.149 / 0.225 | 14900.00 / 2250.00 | 14900 / 2250 | -0.285 | +0.898 | 1.0000 |
| 100000 / 10000 | pooled per stage over 20 configurations (50 concepts) | dpo | 0.029 / 0.000 | 2900.00 / 0.00 | 2900 / 0 | +1.995 | +2.893 | 1.86e-122 |
| 100000 / 10000 | pooled per stage over 20 configurations (50 concepts) | instruct | 0.009 / 0.000 | 900.00 / 0.00 | 900 / 0 | +1.525 | +3.128 | 3.85e-38 |
| 100000 / 10000 | pooled per stage over 20 configurations (50 concepts) | instruct, record FPR .003 | 0.009 / 0.003 | 900.00 / 30.00 | 900 / 30 | +0.377 | +2.554 | 1.07e-12 |

**The seat's arithmetic, with its premise.** At 800/80 the seat's arithmetic is reproduced: base d' -1.931 (seat -1.9; agrees at the seat's precision); sft d' -0.296 (seat -0.3; agrees at the seat's precision); dpo d' +0.611 (seat +0.6; agrees at the seat's precision); instruct d' +0.151 (seat +0.15; agrees at the seat's precision); DPO p = 0.1085 (seat ~ .11); instruct p = 0.5119 (seat ~ .5). That confirms the arithmetic under the premise, not the points: under the same eight-concept premise the pooled per-stage n is 16000/1600, at which base d' ~ -1.9: -2.103 (does not agree); sft d' ~ -0.3: -0.286 (agrees); dpo d' ~ +0.6: +1.525 (does not agree); instruct d' ~ +0.15: +1.056 (does not agree); dpo one-sided Fisher p ~ 0.11: 3.34e-20 (does not agree); instruct one-sided Fisher p ~ 0.5: 1.03e-06 (does not agree). Holding at both units: 1 of 6 figures (sft d' ~ -0.3).

**The instruct-FPR correction.** At 800/80 the instruct point is 7/0 under the source's 0% and 7/0 under the record's 0.3% (0.003 x 80 = 0.24 rounds to 0), so the correction does not change the per-configuration arithmetic. With the unrounded expected counts (7.2 / 0.24) the log-linear d' would be +0.019, so the seat's +0.15 implies integer counts with zero false alarms (Code's inference; the block states no rounding rule). At the pooled n under the same premise the correction does change the point: 144/5 (d' +0.339, p 0.0055) under the record's 0.3% against 144/0 (d' +1.056, p 1.03e-06) under the source's 0% (0.003 x 1600 = 4.8 rounds to 5). Likewise at 5000/500 (45/2 (d' +0.215, p 0.1860) against 45/0 (d' +0.729, p 0.0135)) and at 100000/10000 (900/30 (d' +0.377, p 1.07e-12) against 900/0 (d' +1.525, p 3.85e-38)). N2(v) must choose and declare both the concept count and the unit (per configuration or pooled).

**Consistency with the N2 raw** (a read-only, non-binding check of `results/raw/2026-10-08_note-N2-roc.json`, another item's working-tree output): its pooled (16000/1600) values for the seat's figures agree with this section's in 6 of 6 (relative tolerance 1e-9), and its pooled instruct point at the record's 0.3% agrees (counts, d' and p). The values compared are in this item's JSON (`source_points_dprime_computed_new.n2_consistency_check`). That file's sha256 is not recorded here: the N2 raw records this item's JSON sha256, so the binding cross-reference runs from N2 to this item, and recording both would form a cycle in which neither sha could stay valid.

## 8. Lineage

| stage | source key | source HF repo (code, no revision) | record repo (manifest) | match | record revision |
|---|---|---|---|---|---|
| base | olmo_base | allenai/Olmo-3-1125-32B | allenai/Olmo-3-1125-32B | yes | c2b61dae89a1 |
| sft | olmo_sft | allenai/Olmo-3.1-32B-Instruct-SFT | allenai/Olmo-3.1-32B-Instruct-SFT | yes | 152782ecc41a |
| dpo | olmo_dpo | allenai/Olmo-3.1-32B-Instruct-DPO | allenai/Olmo-3.1-32B-Instruct-DPO | yes | fc84a4f69991 |
| instruct | olmo_instruct | allenai/Olmo-3.1-32B-Instruct | allenai/Olmo-3.1-32B-Instruct | yes | ac0587e4a774 |

Repo-level match 4/4. The record side is read from data/olmo/manifest.json@bbc9ffe (fields `repo`, `revision`), a committed artifact, so our four acquired repos and revisions are reproduced. The source side is Code's WebFetch reading of src/model_utils.py at 5d5d9b4 (section 3), not a committed artifact, so the match itself is the record's prose claim (RESULTS.md@bbc9ffe:12565-12569, log-only) with this comparison as a computed-new check (section 0 gives the two rows). The paper names the model as OLMo-3.1-32B at base, SFT, DPO and instruct and gives no HF ids. The source code pins no revision, so a revision-level match cannot be established from the source.

## 9. Decoding, for N2(i)'s side-by-side (source side only)

| parameter | paper v1 | released code at 5d5d9b4 |
|---|---|---|
| temperature | 1.0 (Appendix A, all generations unless otherwise specified) | 1.0 |
| top_p | 1.0 (Appendix A, stated as the default sampling setting) | not passed to generate |
| top_k | 50 (Appendix A, stated as the default sampling setting) | not passed to generate |
| do_sample | not stated | temperature > 0 |
| max_new_tokens | not stated | 100 |
| trials_per_concept_per_cell_injected | not stated | 100 (10 trial numbers x 10 samples) |
| trials_per_concept_per_cell_control | not stated | 10 (10 trial numbers x 1 sample) |
| seed_policy | not stated | one global --seed (default 42) set once in main() for random, numpy, torch and CUDA; no per-trial seeds |
| prompt_format | not stated for OLMo. v1 Section 3.3 says that for the base model it discusses (Gemma3-27B base, as Code read the passage) chat turns are written as 'User:' / 'Assistant:' text joined by newlines; instruct models use the chat template (Section 3.2 Table 2; Appendix B.1). Paraphrased | olmo_base: plain-text 'User:' / 'Assistant:' turns, no chat template (build_base_model_prompt); post-trained stages: the tokenizer's chat template. The bare 'Tell me about {word}' template is the base model's concept-vector extraction prompt, not the trial prompt |

Paper v1 on decoding: temperature T = 1.0 with default sampling parameters (top-p = 1.0, top-k = 50) unless otherwise specified (Appendix A; paraphrased). Whether the v1 OLMo runs used the code's defaults (seed 42, 100 tokens) is not stated. Our side as declared: ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:89-96 (temperature 1.0, max_new_tokens 100, our per-trial seeds live and declared) -- log-only; N2(i) carries our side.

## 10. Answers to N2(vi)

1. **Configuration.** None of the four per-stage values comes from a single (layer, alpha) configuration. Each is an aggregate over L in [25, 32, 38, 45, 51] x alpha in [1, 2, 4, 8] (20 configurations), per v1 Figure 21's caption, matching ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:39. The released code's per-model summary pools all trials across cells; that the figure used that pooled summary is Code's inference, not a source statement.
2. **n injected / n control per cell.** Not stated by the source, for any stage. Under the code's defaults the per-cell counts are 100 x n_concepts injected and 10 x n_concepts control. n_concepts is not stated for v1: 8 gives 800 / 80, the code's default 50 gives 5000 / 500 (section 5). The eight is our own B2 registration. These are per-configuration n; the source's rates are pooled over 20 configurations, so the pooled per-stage n under the same premises is 16000 / 1600 or 100000 / 10000 (sections 5 and 7).
3. **Table or figure.** The record does not state its recovery method: RESULTS.md@bbc9ffe:7326-7327 says only that the values were recovered from the paper (Appendix C, Fig 21). The source carries the values in prose in v1 Appendix C, in the paragraph that describes Figure 21, and in no table. The record's values equal that prose to printed precision in 7 of 8 cells, which supports text-reading; the instruct FPR slip (section 4) is consistent with mis-transcribing that prose. This audit digitized nothing.
4. **Best-of-grid.** No. Each value is the aggregate over the full grid. The addendum notes (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:212-213) that the aggregate is diluted by past-optimum strengths.
5. **Per-stage TPR in text.** Yes, all four stages, in v1 only (quotation and paraphrases in section 3). v2-v5 carry none in text.
6. **Per-stage FPR in text (v1).** base 16.4%, SFT 22.5%, DPO 0%, instruct 0%. The record's instruct 0.3% equals the v1 instruct introspection rate; Code reads it as a transcription slip, not established, since Figure 21 was not digitized (section 4).
7. **Lineage.** The four HF repos in the source code, as Code read it, equal the record's manifest, 4/4. No revision is pinned on the source side.

**For the note (Code's suggestion; not applied; the design seat drafts).** The sentence can say what the source's text reads: arXiv:2603.21396v1, Appendix C (prose describing Fig. 21), per-stage TPR 0.1% / 14.9% / 2.9% / 0.9% and FPR 16.4% / 22.5% / 0% / 0% for base / SFT / DPO / instruct, each pooled over 5 layers x 4 strengths, n not stated; later versions (v2-v5) show the comparison at L = 25 without per-stage numbers in text. If F2 plots the source's instruct point, its FPR is 0 per the text. Any d' or p for the source's points names its assumed n and unit (section 7). The figures this raw finds discrepant carry block :23 consequences if the note carries them (section 12).

## 11. Referent notes (a wrong referent is a note, not a STOP)

1. Version referent: the record cites 'arXiv:2603.21396 Appendix C, Fig 21' with no version (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:35-36, :39; RESULTS.md@bbc9ffe:7327, :7343). That structure exists only in v1 (2026-03-22). v2 (2026-04-10) to v5 (2026-06-10) do not carry the four per-stage values in text. In v4, Figure 21 is a different OLMo-stage figure (Appendix D.1, L = 19 and L = 22), so the unversioned citation is actively ambiguous. The note should cite v1 explicitly.
2. Instruct FPR: the record carries 0.3% (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:46; RESULTS.md@bbc9ffe:6999 'theirs' 0.003; RESULTS.md@bbc9ffe:7341). The v1 text gives instruct FPR 0% and introspection rate 0.3%. The instruct sensitivity is then +0.9 pp, not +0.6 pp; the +0.6 pp appears at ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:46, RESULTS.md@bbc9ffe:7330 and :7341, and the scripts/b2r_analyze.py@bbc9ffe:15 docstring. Other tracked copies of the 0.003: HANDOFF-2026-08-25.md@bbc9ffe:60 and the self-test fixture at scripts/b2r_analyze.py@bbc9ffe:161 (section 2, carrier search). Code's reading: a transcription slip of the v1 prose; not established, because the record says it recovered the values from 'Appendix C, Fig 21' (RESULTS.md@bbc9ffe:7327) and Figure 21 is an image that was not digitized. On that reading it is a referent note, not a STOP, and needs no analyzer change; block :23's consequence if the note carries it is in section 12. The [g3-A] verdict was computed on our data and is unaffected. Pre-data sizing figures that used the instruct FPR, each recomputed in section 6: (1) the retired criterion's power at Instruct's rates, at ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:52-53 (0.000 at n = 48, 0.020 at n = 200), RESULTS.md@bbc9ffe:7330-7331 (0.000 / 0.001 / 0.020 at n = 48 / 96 / 200) and the Instruct column of the table at RESULTS.md@bbc9ffe:7356-7361 ('0.9 vs 0.3'); other tracked: scripts/b2r_analyze.py@bbc9ffe:16 (docstring, 0.000 at n=48; unchanged at either rate). All reproduce at .003 (section 6b). At .000 the Instruct power is 0.000 / 0.000 / 0.002 / 0.036 at n = 24 / 48 / 96 / 200. The record describes these as power at the source's own rates ('their own Instruct rates', 'Instruct's own reported rates', 'their own numbers'; section 6b), so as described the n = 96 and n = 200 cells are discrepant (0.001 against 0.002; 0.020 against 0.036). The sentence after the table, RESULTS.md@bbc9ffe:7363-7364 ('n in the thousands per cell' for conventional power at Instruct), holds only at .003: at .000 the registered criterion reaches 0.80 power at n ≈ 750 per arm (0.8042), and 0.90 at ≈ 890 (0.9020), against ≈ 2700 (0.8011) and ≈ 3500 (0.9001) at .003 (section 6b; row 24). Block :23's consequence for both is in section 12, condition 3. (2) The [g3-A] joint power 0.9642 / 0.964 (every carrier, as in section 0: ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:148, :273; RESULTS.md@bbc9ffe:7173, :7180, :7192, :7194, :7251, :7269, :7270; also data/olmo/b2r_valuescheck.json@bbc9ffe 1_g3A_power.detail; the arithmetic passages around them are ADDENDUM :147-148 and RESULTS :7189-7194, :7266-7270). The exact value at the record's inputs is 0.9645 (0.965 at 3 dp; residual -0.0003, cause not identified), and at .000 it is 0.9827. Both stay above the 0.90 bar. (3) The b2r_analyze self-test fixture uses .164/.225/.000/.003 (scripts/b2r_analyze.py@bbc9ffe:160-162). It is a synthetic case, not a verdict input, and is not touched (read-only).
3. The block's N2(v) design-seat arithmetic for the source's points (block :34) is checked in section 7. At the seat's premise, 800/80, every figure reproduces at the seat's precision: base -1.931, SFT -0.296, DPO +0.611 (one-sided Fisher p = 0.1085), instruct +0.151 (p = 0.5119). That confirms the arithmetic under the premise, not the points. The seat's 800/80 is a per-(layer, alpha) n, but the source's rates are pooled over 20 configurations. At the pooled per-stage n under the same eight-concept assumption (16000/1600) the points are base -2.103, SFT -0.286, DPO +1.525 (p 3.34e-20), instruct +1.056 (p 1.03e-06). There the FPR correction does change the instruct point (d' +0.339 -> +1.056; one-sided Fisher p 0.0055 -> 1.03e-06). At 800/80 it does not (7/0 under both, because 0.24 expected false alarms round to 0). N2(v) must choose and declare both the concept count and the unit (per configuration or pooled).
4. n: the block's '800/80 per configuration' and the record's '~800 injected / ~80 control' (every carrier, section 2: ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:32; RESULTS.md@bbc9ffe:7365, :7439, :7485, :7500; other tracked: AUDIT-note-release-v1_2.md@bbc9ffe:34) assume eight concepts, which is our own B2 registration (data/configs/b2_concepts.json@bbc9ffe selection_for_B2.registered_n = 8), not a source count (data/configs/b2_concepts.json@bbc9ffe n_canonical = 50, the 50-entry list its provenance cites at experiments/01_concept_injection.py:58). The source states no n. The OLMo experiment's own default concept list (experiments/03_behavioral_robustness.py, defined in that file) has 50 entries, giving 5000 / 500 per cell and 100000 / 10000 per stage pooled (section 5). As the record's inference with its premise (RESULTS.md@bbc9ffe:7438-7440), 800/80 is log-only; as a statement of the source's n it is not found, and under block :23 a note sentence presenting it as the source's n is cut (section 0). The same holds for figures derived from it. The ratio '~33×' (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:32; RESULTS.md@bbc9ffe:7440) is 800/24 = 33.3 (one of their configurations against our whole stage, the record's unit); per stage under the same premise 16000/24 = 666.7; with the code's 50 concepts 208.3 and 4166.7, so it depends on both premise and unit. The power row 'theirs, OLMo cell (~800/80)' (RESULTS.md@bbc9ffe:7485, :7500-7502) is computed at that n; this item does not recompute it. N2(v)'s tests on the source points depend on the concept count and the unit and must name both.
5. Layers: ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:66 says 'L_M stands on the code rule and the paper's caption'. The code rule gives int(64 x 0.7) = 44 at the fourth slot, but the v1 caption gives 45 there, so the 'and the paper's caption' support does not hold at that slot. Neither int() nor round() of the default fractions yields the caption's list ([25, 32, 38, 44, 51] and [26, 32, 38, 45, 51] against [25, 32, 38, 45, 51]), while the README's absolute list does (5/5; section 5). Recorded, not adjudicated; L_M = 44 is not touched.
6. README: besides the layer-fraction issue the record already notes (RESULTS.md@bbc9ffe:7393-7398), the README's -m keys (olmo_32b_*) are not in the script's argparse choices, so the README command would be refused as written. Its layer list still equals the v1 caption (5/5).
7. Values-check wording: ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:274 says the section 0.2/0.6 tables are 'exact against paper and cache'. RESULTS.md@bbc9ffe:7181 records the item as 'PASS -- exact' and data/olmo/b2r_valuescheck.json@bbc9ffe 2_tables.detail as '§0.2 exact'. Against the v1 text, 7 of the table's 8 rate cells are exact; the instruct FPR is the exception.
8. Method limits: the source was read through WebFetch's processed rendering. Each v1 Appendix C sentence came back verbatim in two fetches (one omitting the base sentence's opening clause). The v2-v5 Table 3 values came back the same in three fetches (v2, v4, v5). No figure image was fetched or digitized. One v4 fetch returned an off-target answer and was re-run with a rephrased prompt. The fixer pass's four reads and round 2's two reads (each made twice, agreeing) are listed in section 3, and so are round 3's two reads of 03_behavioral_robustness.py (the second declined to copy the list in full, so only its count, end entries and import status corroborate the first).
9. Not checked: the note's sentence and F2's points. The note draft and the F1/F2 SVGs are not on this machine (results/raw/2026-10-08_note-preflight.md@bbc9ffe:15, :17-18: MISSING), so whether the note 'carries 0.001 / 0.149 / 0.029 / 0.009' (block :35) and what F2 plots for the source's instruct FPR were not read.
10. Weakest pair: the record labels base vs dpo the 'single weakest pair' at 0.9825 (RESULTS.md@bbc9ffe:7268; :7192). At the record's own inputs the weakest pair is base > instruct (0.9654), not base > dpo (0.9830). The label holds only when the instruct FPR equals the dpo FPR, as under the source's 0% (section 6a). The record's 'base binds, not sft' (RESULTS.md@bbc9ffe:7193, :7270) is unaffected: both base pairs are below both sft pairs at either input.
11. Exactness claims: the record calls 0.964 'the exact number' and 'the exact figure' (RESULTS.md@bbc9ffe:7194, :7269-7270) and states 'joint figure is 0.964' at :7251. Exact enumeration gives 0.9645485 at its inputs, 0.965 at 3 dp (section 6a).

## 12. STOPs

**Active STOPs for N2(vi): none.** N2(vi) is resolved (section 10), which is its pass condition (block :36), and no reproduction here needs a change to any analyzer of record (block section 0.3).

**Conditional, under block :23** (AUDIT-note-release-v1_2.md@bbc9ffe:23, N1's on-fail rule: a discrepant figure is corrected in the note if the discrepancy is transcription and is a STOP if it is not; a not-found figure is cut). The note is not on this machine (header; note 9), so whether it carries these figures is unknown. Each condition fires only if it does:

1. If the note carries the [g3-A] joint power as 0.9642 or 0.964: exact enumeration at the record's inputs gives 0.96455 (0.9645 at 4 dp, 0.965 at 3 dp; section 6a). The cause of the residual is not identified (a simulation is a candidate, not established), so Code cannot classify it as transcription. Under block :23 that figure is then a STOP for the design seat and PI. The [g3-A] verdict itself is computed on our data and is not touched. The addendum describes the figure as 'at their own rates' (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:148); at the source's text rates (instruct FPR 0%) the exact value is 0.98274, which bears on any correction the design seat and PI choose.
2. If the note carries 'single weakest pair (base vs dpo) 0.9825': at the record's inputs base > dpo is 0.98296 and the weakest pair is base > instruct (0.96540) (section 6a). The label is wrong at the record's own inputs, which is not a transcription slip, and the value's residual has no identified cause, so under block :23 it is a STOP.
3. If the note or F2 carries the source's instruct FPR as 0.3%, or its instruct TPR - FPR as +0.6 pp: Code reads the discrepancy as transcription of the v1 prose (section 4). On that reading block :23 corrects the note to 0% and +0.9 pp, and there is no STOP. If the design seat or PI do not accept that reading (the record says it recovered the values from 'Appendix C, Fig 21', and the figure was not digitized), block :23 makes it a STOP. The same fork covers the figures derived from that input: if the note carries the retired criterion's Instruct power described as at their own (reported) rates (0.001 at n = 96, 0.020 at n = 200; ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:52-53, RESULTS.md@bbc9ffe:7330-7331, :7354-7361), then under Code's transcription reading block :23 corrects it to the source-rate values 0.002 / 0.036 (section 6b), and otherwise it is a STOP. At n = 24 and 48 the value is 0.000 either way. The same holds for the sentence after the table, if the note carries it: 'Reaching conventional power there needs n in the thousands per cell' (RESULTS.md@bbc9ffe:7363-7364, Instruct) holds only at the transcribed 0.3% (≈ 2700 per arm for 0.80, ≈ 3500 for 0.90). Under Code's transcription reading block :23 corrects it to the source-rate figures, 0.80 power at n ≈ 750 per arm (0.8042), and 0.90 at ≈ 890 (0.9020) (section 6b), and otherwise it is a STOP. :7363's 'Instruct is the binding constraint and it is not close' holds at both inputs and needs no correction.
4. If the note presents ~800 injected / ~80 control per configuration as the source's n: the source states no n (section 5), so under block :23 the figure is not found and is cut. Stated as an assumption with its premise (eight concepts, per configuration, applied to pooled rates), it is the record's log-only inference. Any figure derived from it is cut likewise, or stated with its premise and unit: the ratio '~33× ours' (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:32-33; RESULTS.md@bbc9ffe:7440) is 800/24 = 33.3 (one of their configurations against our whole stage, the record's unit); per stage under the same premise 16000/24 = 666.7; with the code's 50 concepts 208.3 and 4166.7; the power row 'theirs, OLMo cell (~800/80)' (RESULTS.md@bbc9ffe:7485, :7500-7502) is computed at that n and is not recomputed by this item.

## 13. Values-check

### Round 1 (fixer pass)

Round-1 rows are kept as written at round 1. Where round 2 changes a disposition, the round-2 table below says so (round-2 rows 1, 2 and 6 revise round-1 rows 6, 2 and 14).

One adversarial values-check pass on the builder's version (script sha256 660f33a9...df31). The checker reports 110 claims checked and 14 findings, 3 substantive and 11 minor. Its rerun reproduced the builder's JSON byte for byte, and the .md apart from the stamp and command lines. Every finding was re-verified against the record (git show bbc9ffe) or the source (WebFetch, section 3) before it was applied. None was rejected.

| # | grade | finding | disposition | detail |
|---|---|---|---|---|
| 1 | substantive | No per-figure status in the raw or the JSON. | fixed | Section 0 is a per-figure status table and the JSON carries `figures[].status`. The TPR, FPR and sensitivity statuses are derived from the computed comparisons; the others are assigned from the rule-4 vocabulary, with the printed value beside each. Beyond the checker's list, rows were added for the power figures (section 6) and the seat's N2(v) points (section 7). |
| 2 | substantive | Note 3: the seat's N2(v) instruct arithmetic 'cannot be checked here'; the correction 'changes' it. | fixed | Section 7 computes log-linear d', c and a one-sided Fisher (stdlib, equal to the record's fisher_one_sided). At 800/80 the instruct point is 7/0 under both FPRs, giving d' +0.151 and p = 0.5119; 4 of the seat's 4 d' agree at its precision, and its two p (DPO 0.1085, instruct 0.5119) match its ~.11 and ~.5. Note 3 is rewritten. The pi_item in the builder's returned summary (not in the raw) is superseded by note 3. |
| 3 | substantive | Code's base trial prompt called 'bare'. | fixed | Re-read of 03_behavioral_robustness.py@5d5d9b4 (section 3, fixer-pass reads): build_base_model_prompt writes plain-text User:/Assistant: turns with no chat template; 'Tell me about {word}' is only in extract_concept_vector_base_model. The section 3 fact, the section 9 row and the JSON's decoding.prompt_format are corrected. |
| 4 | minor | Paper v1 prompt_format 'not stated'. | fixed | Re-read of v1 (both halves): Section 3.3 gives a User:/Assistant: newline format for the base model it discusses (Gemma3-27B base as read); no OLMo-specific format anywhere. The row is reworded. |
| 5 | minor | Note 2 omitted ADDENDUM :52-53 and RESULTS :7330-7331. | fixed | Both are added, and both are recomputed in section 6(b). Anchors are asserted on :53 and :7331. |
| 6 | minor | Joint power 'presumably' used 0.3%; not recomputed. | fixed | Section 6(a) enumerates exactly with the record's own CP: 0.9645 at .003 and 0.9827 at .000; pair 0.9830. The residual against 0.9642 / 0.9825 is disclosed and unexplained. One correction to the checker's evidence: 0.9642 is not only in prose. data/olmo/b2r_valuescheck.json@bbc9ffe field 1_g3A_power.detail holds 'joint=0.9642 >= 0.90' (as a result string, without inputs or method). |
| 7 | minor | Note 5 paraphrase of ADDENDUM :66 dropped 'and the paper's caption'. | fixed | Note 5 quotes :66 and states that the caption's fourth slot (45) contradicts the code rule's 44. round() is added beside int() (section 5); neither yields the caption list. |
| 8 | minor | v4 row / note 1 omit that v4's Figure 21 is a different OLMo figure. | fixed | Re-read of v4 (both halves): Figure 21 is the Appendix D.1 OLMo-stage figure at L=19/L=22. The v4 row, section 3's version paragraph and note 1 say so. |
| 9 | minor | Table 3 described as 'official checkpoints'. | fixed | Re-read of v4: Table 3 is a LoRA fine-tuning study on the OLMo SFT checkpoint (L=25, alpha=4, 11 rows as read); only SFT* and DPO* are official. The v2/v4/v5 rows and the JSON config string are reworded; 'only' is dropped. |
| 10 | minor | Answer 3 'Nothing was digitized' over-reaches. | fixed | Answer 3 now says the record states no recovery method (RESULTS :7326-7327). The source holds the values in prose; the 7-of-8 equality supports text-reading; this audit digitized nothing. |
| 11 | minor | Note 7 attributed 'exact against paper' to RESULTS :7181; '7 of 8' hard-coded. | fixed | The quote is attributed to ADDENDUM :274, :7181 is paraphrased as 'PASS -- exact', and the valuescheck JSON's '§0.2 exact' is added. The count is formatted from n_tpr + n_fpr. |
| 12 | minor | The note's sentence was never checked; no line says so. | fixed | A header line and note 9 cite the preflight raw's MISSING rows (located and asserted by the script) and say the note's wording and F2's points were not read. |
| 13 | minor | Answer 4 locator :213-214. | fixed | Now :212-213. Anchors are asserted on both lines. |
| 14 | minor | Paraphrase without stated reason. | fixed | Section 3 says the raw keeps to one short quotation from the source and that the paraphrases carry every number exactly as printed. |

### Round 2

A second checker pass on the round-1 script (sha256 eca0a8d5...8c41) reported 10 findings, 2 substantive and 8 minor. Its rerun reproduced the raw apart from the stamp and command lines. Code re-verified each finding against the record (git show bbc9ffe), the source (two round-2 WebFetch reads, section 3) or a computation in this script before applying it. All 10 are applied and none is rejected. Adaptations are stated in rows 5, 8 and 9. Cross-item: this JSON keeps every key the N2 script reads (stages.*, grid.n_scenarios_computed_new, decoding.*, and the 800/80 rows of source_points_dprime_computed_new.rows). The pooled rows carry new n values, so N2's 800/80 filter is unaffected. The JSON's sha256 changes with this run; the N2 raw records the sha of the N2vi JSON it read. A rerun of this script reproduces the raw apart from the stamp, HEAD and command lines and the N2 ROC JSON's sha256 in section 7, which moved between Code's runs because the N2 item was re-running concurrently; the compared values agreed at every run.

| # | grade | finding | disposition | detail |
|---|---|---|---|---|
| 1 | substantive | Joint power 0.9642 labelled discrepant and 'not a STOP' without addressing block :23; the record's 'exact number is 0.964' is 0.965 at 3 dp. | fixed | Section 12 now separates active STOPs (none for N2(vi)) from block :23 conditions. The joint-power row says: a STOP for the design seat and PI if the note carries 0.9642 or 0.964, because the cause is not identified and so cannot be classed as transcription. Section 6(a) prints 0.9645485 (0.965 at 3 dp) against the record's exactness claims (RESULTS :7194, :7269-7270, :7251). Code's own checks: 0 of 4 deterministic variants reproduce both printed values. Monte Carlo standard errors make a 10^4-10^5-draw simulation a candidate, stated as not established. Beyond the checker's list, the carrier search found two more carriers of the figure, RESULTS :7173 and :7251. 'Immaterial' is no longer used; the 0.90-bar fact is kept beside the conditional. |
| 2 | substantive | 800/80 is a per-cell n applied to rates pooled over 20 configurations; the seat's arithmetic was called 'confirmed' and the correction 'does not change' it, without that premise. | fixed | Section 7 adds the pooled rows (16000/1600 and 100000/10000) and a unit column. It states the unit mismatch and reports the seat's figures as 'arithmetic confirmed under the seat's premise', with the pooled value beside each. The JSON adds design_seat_check, and the old design_seat_confirmed_at_800_80 key is kept for N2. At 16000/1600: instruct 144/5 at .003, d' +0.339, p 0.0055; 144/0 at .000, d' +1.056, p 1.03e-06; DPO d' +1.525, p 3.34e-20; base -2.103; SFT -0.286. All 5 points equal the checker's printed counts, d' and p at its precision (asserted by the script; so are its joint and four pair values, finding 1 and 3). Note 3, the seat row and answer 2 are rewritten. Consistency with N2: 6/6 seat figures and the record-FPR instruct point agree with results/raw/2026-10-08_note-N2-roc.json (section 7). |
| 3 | minor | The record's 'single weakest pair (base vs dpo)' is wrong at its own inputs. | fixed | Section 6(a) prints all four pairs at both inputs. At .003 the weakest is base > instruct 0.96540 (base > dpo 0.98296); at .000 base > dpo and base > instruct tie at 0.98296. 0 of the four equals 0.9825 at 4 dp. Changes: a new status row, note 10 and a section 12 condition. 'base binds, not sft' is asserted to hold at both inputs. |
| 4 | minor | Row 8 'transcription' note unhedged. | fixed | Round-2 read of v1 (two fetches): Figure 21 is an image, olmo-staged-introspection.png, alt text 'Refer to caption', with no data labels. Row 8, section 4, answer 6 and note 2 now give 'Code's reading: transcription ... not established', and section 12 states the block :23 fork (correction under that reading, STOP otherwise). |
| 5 | minor | 'The README is therefore not evidence of the producing configuration' overstates. | fixed | Reworded. The README cannot run as written, but its list equals the caption (5/5), which int() (4/5) and round() (4/5) do not; Code computes all three counts. One adaptation: the checker's 'points to' is written 'consistent with', since the record itself reads it that way (RESULTS :7396-7398) and the source does not say. Notes 5 and 6 carry the 5/5. |
| 6 | minor | The 'paraphrases' reproduce the source's wording. | fixed | The DPO, instruct and base lines now give the numbers only, in Code's words, as the checker proposed; the SFT line is reduced the same way. The one quotation is unchanged. |
| 7 | minor | Section 2 label calls :7345-7348 a paraphrase; the v1 row omits Section 3.3's FPR statement. | fixed | Round-2 read of v1 (two fetches) found the sentence in Section 3.3 'The Role of Post-Training'. The label now reads 'the record quoting v1 Section 3.3'. The v1 row and a section 3 paragraph state, in Code's words, that Section 3.3 gives the FPR pattern with no per-stage TPR numbers. |
| 8 | minor | Locator lists not exhaustive; the record's p ~ .28 unchecked. | fixed | Section 2 adds a carrier search. Per figure, a regex over every line of RESULTS.md and the addendum at bbc9ffe, with hits asserted equal to declared carriers plus declared unrelated lines (20 unrelated, each with a reason). One git grep covers the other tracked .py/.md files (9 carriers, 3 unrelated). Section 0 locators come from it. A new row gives p ~ .28: 0.2821, exact binomial P(X <= 0) for X ~ Binomial(43, .029), with 0/43 read from b2r_explore_dpo.json. It is labelled log-only, not computed-new as the checker proposed, because the figure is in the record and its 2.9% input is source prose (the same convention as the retired-power row); the recomputation is printed as computed-new. |
| 9 | minor | Row 12 '~800/~80' conflates 'absent from the source' with 'absent from the record'. | fixed | Split into two rows. As the record's inference (RESULTS :7438-7440) it is log-only. As the source's n (ADDENDUM :32-33, RESULTS :7365, block :34) it is not found, and block :23's cut applies. The log-only row cites data/configs/b2_concepts.json@bbc9ffe (n_canonical = 50; selection_for_B2.registered_n = 8, so the eight is ours), and so do section 5 and note 4. |
| 10 | minor | 'clopper' described without its docstring line. | fixed | The script lists the lines (:10 docstring, :49 import, :60, :61, :74, :112 calls) and asserts the list, the docstring span and the call form. |

### Round 3

A third, strict checker pass on the round-2 script (sha256 61035dbf...f4a2) reported 6 findings, 2 substantive and 4 minor, and no open items from round 2. Its rerun reproduced both outputs apart from the stamp and command lines and the N2 ROC JSON's sha256, which N2 had regenerated after this item's last run. Its redaction check found 0 verbatim values. Its independent recomputation agreed with every figure it recomputed. It judged the STOP logic licensed, with no active STOPs and the four block :23 conditions correctly framed, apart from the two gaps in rows 1 and 6 below. Code re-verified each finding against the record (git show bbc9ffe), the source (two round-3 WebFetch reads, section 3) or a computation in this script before applying it. All 6 are applied, none is rejected, and adaptations are stated in rows 1 and 4. Round-1 and round-2 text above is kept as written at its round. Round 3 revises it as follows: old row 16 (lineage) and old row 17 (retired power) are each split in two, so later rows move down by two. Rows 12-13 carry the derived ratio and two more carriers. The round-2 header's sentence on the N2 sha is superseded by row 3. Cross-item: the keys the N2 script reads (stages.*, grid.*, decoding.*, the 800/80 rows) are unchanged in content; this JSON's sha256 changes with this run.

| # | grade | finding | disposition | detail |
|---|---|---|---|---|
| 1 | substantive | The retired criterion's Instruct power, which the record describes as at the source's own rates, was relabelled 'at the record's rates' and given no block :23 condition. | fixed | Old row 17 is split. Row 18 is the DPO column, log-only: its inputs equal the v1 text, and 4/4 cells recompute. Row 19 gives the Instruct figures in the record's own framing ('their own Instruct rates', ADDENDUM :52-53; 'Instruct's own reported rates', RESULTS :7330-7331; 'Power at their own numbers', RESULTS :7354), with the source-rate column beside the recomputation at the record's 0.3%. At the source's rates the cells differ at n = 96 (0.001 against 0.002), n = 200 (0.020 against 0.036). Section 12 condition 3 now covers these figures with the same fork: corrected to the source-rate values under Code's transcription reading, a STOP otherwise. Section 6(b) and note 2(1) say the same. Anchors are asserted on RESULTS :7330, :7331, :7354 and ADDENDUM :53, :148. One adaptation: the Instruct row's status is 'discrepant', not only a note, by the raw's own convention for the +0.6 pp row (correct arithmetic on the slipped input, labelled discrepant). Beyond the checker's list: condition 1 now notes that the addendum also describes the joint power as 'at their own rates' (ADDENDUM :148), where the exact value is 0.98274. Condition 1's consequence (a STOP if carried) is unchanged. |
| 2 | substantive | The lineage row was labelled 'reproduced' although its source half is a WebFetch reading, not a committed artifact. | fixed | Split into row 16 (our four acquired repos and revisions, reproduced from data/olmo/manifest.json@bbc9ffe) and row 17 (the match to the source's MODEL_NAME_MAP, log-only at RESULTS :12565-12569, printed as 'computed-new against Code's WebFetch reading of 5d5d9b4: 4/4'). Section 8, answer 7 and the JSON lineage string say the same. Both statuses pass N1, so only the label changes. |
| 3 | minor | The N2 ROC JSON's sha256 recorded here was stale, and the two items' sha references form a cycle. | fixed | This item no longer records that sha, in the .md or the JSON. The JSON's n2_consistency_check now carries the compared values from both sides and the agreement counts, and section 7 says why the sha is omitted. The round-2 header's sentence about the sha moving between runs is kept as written at round 2, and this row supersedes it. Ordering: this run changes this JSON's sha256, so the N2 raw's recorded N2vi JSON sha is now stale until N2 re-runs. The N2 run belongs to that item and should come after this one. Code did not run it (not this item's file). |
| 4 | minor | b2_concepts.json's concepts_source was said to cite 'the source's DEFAULT_TEST_CONCEPTS'; it cites experiments/01_concept_injection.py:58, while the OLMo experiment 03 defines its own list. | fixed | Confirmed by git show (data/configs/b2_concepts.json@bbc9ffe; the script asserts that concepts_source starts with 'experiments/01_concept_injection.py:58 (DEFAULT_TEST_CONCEPTS') and by two round-3 WebFetch reads of 03_behavioral_robustness.py@5d5d9b4 (section 3): there DEFAULT_TEST_CONCEPTS is a literal list defined in the file and imported from nowhere, with 50 entries. Section 5 and note 4 now cite 01:58 and say the OLMo run's 50 is 03's own list. One adaptation: instead of 'identity with 01's not checked', read 1's 50 entries are compared with canonical_concepts (the record's recovery of 01:58) and are equal entry for entry and in order (computed-new). Read 2 declined to copy the list and corroborates only the count, the first and last entries and the import status. So the identity is stated as Code's reading, not established. |
| 5 | minor | Note 2's joint-power locators omitted RESULTS :7270 and ADDENDUM :273. | fixed | Note 2(2) now prints the carrier search's list, the same as row 20: ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:148, :273; RESULTS.md@bbc9ffe:7173, :7180, :7192, :7194, :7251, :7269, :7270. It names the arithmetic passages (ADDENDUM :147-148; RESULTS :7189-7194, :7266-7270) separately. |
| 6 | minor | Condition 4 cut ~800/~80 as the source's n but not the ratio derived from it ('~33× ours'). | fixed | Condition 4 now covers figures derived from the n: cut, or stated with premise and unit. The ratio is computed (computed-new): 800/24 = 33.3 (one of their configurations against our whole stage, the record's unit); per stage under the same premise 16000/24 = 666.7; with the code's 50 concepts 208.3 and 4166.7, with our 24 injected per stage as run (RESULTS :7440, :7358). Rows 12 and 13 carry it. Beyond the checker's list: a round-3 carrier search for the n ('~800|800/80') and the ratio ('33×') over RESULTS.md and the addendum, with the split between the two rows asserted, found two more carriers of the n written as the source's: RESULTS :7485 (a power row 'theirs, OLMo cell (~800/80)') and :7500 ('Their own cell is ~800/80'). Both are added to row 13 and to condition 4. The power figures there are computed at that n and are not recomputed by this item. A separate git grep of the other tracked .py/.md files for the two patterns finds 1 hit, the block's own premise at :34. The round-2 grep and its counts are unchanged. |

### Round 4

A fourth checker pass on the round-3 script (sha256 31187a80...ccd1) reported 2 findings, 1 substantive and 1 minor, and no open items from round 3. Code re-verified each finding against the record (git show and git grep at bbc9ffe) and a computation in this script before applying it. Both are applied as their fixes say, none is rejected, and adaptations are stated in row 1. Earlier rounds' text above is kept as written at its round. Round 4 adds row 24 at the end of section 0, so rows 1-23 keep their numbers. No source was re-read in round 4 (no WebFetch). Cross-item: the keys the N2 script reads (stages.*, grid.*, decoding.*, the 800/80 rows) are unchanged in content. This JSON's sha256 changes with this run, so the N2 raw's recorded N2vi JSON sha is stale until N2 re-runs; that run belongs to the N2 item, and Code did not run it.

| # | grade | finding | disposition | detail |
|---|---|---|---|---|
| 1 | substantive | Section 6(b) called the record's conclusion at RESULTS :7363 'unchanged', but the next sentence, :7363-7364 ('Reaching conventional power there needs n in the thousands per cell'), is a quantitative figure derived from the instruct FPR that the raw did not recompute; at the source's 0% conventional power is reached below 1,000 per arm. | fixed | Confirmed. :7363-7364 sits under 'Power at their own numbers' (:7354, anchors asserted), and the round-4 'thousands' grep finds it as the only carrier in the tracked .py/.md files (section 2). Section 6(b) now computes, at both instruct FPRs, the n per arm at which the registered criterion reaches 0.80 and 0.90 power at Instruct. At 0%: 0.80 power at n ≈ 750 per arm (0.8042), and 0.90 at ≈ 890 (0.9020). At 0.3%: ≈ 2700 (0.8011) and ≈ 3500 (0.9001). The 'is unchanged' sentence is replaced by the fix's wording. New row 24 (discrepant, locator RESULTS.md@bbc9ffe:7363-7364) carries row 19's fork, and note 2(1) and section 12 condition 3 carry the figure: corrected under Code's transcription reading, a STOP otherwise. The JSON mirrors it in figures[], conditional_stops_block_23[2] and dependent_power_computed_new.retired_criterion_power.conventional_power_n. The checker's 20 printed values (eight large-n powers and the twelve table cells, at 4 dp) reproduce (asserted). Method: the record's own clopper_pearson raises OverflowError from n = 1030 (asserted), so the scan uses the record's newcombe compiled with a stdlib CP. That path agrees with the record's own on the 12 table cells and at n = 750 (max abs difference 1.5e-13). Adaptations: (a) the step-1 first n is given beside the fix's grid values (at 0%: 0.80 first reached at n = 746 (0.80054; 0.79962 at n = 745), 0.90 first reached at n = 887 (0.90043; 0.89991 at n = 886); at 0.3%: 0.80 first reached at n = 2694 (0.80012; 0.79996 at n = 2693), 0.90 first reached at n = 3500 (0.90008; 0.89999 at n = 3499)); (b) the row is appended as row 24 rather than inserted after row 19, so the earlier rounds' row numbers stay valid; (c) reading 'per cell' as n per arm (the table's unit, :7356) is stated as Code's reading. The fix's 'At 0.3% the figures are ... ≈ 3500' is given with its value (0.9001). |
| 2 | minor | Row 19 and note 2(1) omitted the copy at scripts/b2r_analyze.py@bbc9ffe:16 (docstring, 'power 0.000 at n=48'). | fixed | Confirmed by git grep with the checker's pattern: 3 hits, ADDENDUM-g3-b2r-v1.2.md:53, RESULTS.md:7331, scripts/b2r_analyze.py:16. The grep now runs in the script, and its hits are asserted (section 2). Row 19 and note 2(1) add 'other tracked: scripts/b2r_analyze.py@bbc9ffe:16 (docstring, 0.000 at n=48; unchanged at either rate)'. Anchors are asserted on scripts/b2r_analyze.py :15 and :16. The n = 48 value is 0.00006 at .003 and 0.00007 at .000, 0.000 at 3 dp at both (asserted). So no number and no STOP changes. Beyond the checker's list: a second round-4 grep, for 'thousands', supplies row 24's locator (finding 1). |
