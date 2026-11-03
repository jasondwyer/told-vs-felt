# note-N1 round 11 (open item O35 of round 11's claims ledger) — the note's own arithmetic on committed inputs: the 24 figures, computed

- **Role.** The raw of record is `results/raw/2026-11-02_note-N1-r11_computations.md`, written by `scripts/audit_note_N1_r11_compute.py` as committed (its sha256 below equals its blob at HEAD, asserted). The design seat's round-11 answers (`results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`, §0 row 2b: "Admit the computation raw; Code regenerates it from its committed script and commits it with its own pin class; the 24 rows map audit-raw-new, computed-new.") admit it, by route (a) of the seat list's §2b (`results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:266). Its date falls outside N1's item-raw pattern (`results/raw/2026-10-0[89]_note-N…`, `scripts/audit_note_N1.py@f935864`:2406), so N1's round-11 profile (v0_8, committed with round 11's claims ledger, after this raw) pins it at the commit that adds it (its own pin class), where its 24 rows map audit-raw-new, computed-new. As the seat list's §2b said it would (:261), the raw is regenerated from the committed script, and its references to the seat list's sections point to the committed list. Nothing here edits the note (frozen; the release-block answers, `908a659`:23), sets a ruling field or edits a row; the 24 rows' statuses are set by N1's round-11 ledger through the pin class.
- Code stamp: Tue Nov  3 01:25:47 UTC 2026 (UTC, inside the script; with the same arguments at the same HEAD, the one line that differs between runs)
- HEAD at run (informational; every read below is pinned to the revision it names): 633b6fdfad18509ba034823b21c6313b65f58913
- Script: `scripts/audit_note_N1_r11_compute.py` sha256 `c24a4ecc1083f36c647e120ffc6b2c3fe2788267b57317bce5dac799b5da0973`; equal to its blob at HEAD: YES (asserted)
- Interpreter: jlens-qwen36/.venv/bin/python (Python 3.12.9); standard library only (among them fractions, math, decimal, statistics.NormalDist, ast, hashlib, json, re; subprocess for `git show`)
- Command: `jlens-qwen36/.venv/bin/python -I scripts/audit_note_N1_r11_compute.py --out results/raw/2026-11-02_note-N1-r11_computations.md`
- Reads: every input is read with `git show <rev>:<path>`, every blob hashed (§7). No working-tree file of the repository is an input; the script reads its own file only to hash it (Script, above), and the one file it writes is this raw (`--out`). No model, no randomness, no network. Pins (each an ancestor of HEAD): `0de15a1` = 0de15a1a298432fd78ee84f2f6c66bb4bd355b24; `09c3a8c` = 09c3a8cc548079d92cd5f8f05357992583f6ef12; `e60b633` = e60b633142f0ff5ec574da022a7117d18711e32b; `8d68b0b` = 8d68b0ba2fbaa7930129811df63763dc1c311e6d; `bbc9ffe` = bbc9ffe72fb8a942431c9bf2622a36e581fdf93c; `2fb0cf0` = 2fb0cf0410cd5e9690bf74c72caf765c884a9ec6; `908a659` = 908a65937e1a5197f047170ce9618af025d74809; `f935864` = f93586404944911061ed3fc523b8c1ca3396029f; `d5123bf` = d5123bf15ed5d60604398e992b788e8a16e457c0; `da50cd1` = da50cd1e98f8f9bbe3c54d60b14f24f70fe99770.
- The note: `RESEARCH-NOTE-v0_8-draft.md@0de15a1` sha256 `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d`; as routed in the release-block answers (`908a659`:21) `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d`: MATCH. Lines 99, 101, 110, 230, 236 and 242 are read; every quotation of the note below is asserted on its line. Each row's clause is asserted on its line, and its unit inside the clause, exactly once and not inside a longer number.
- The 24 rows: the seat list's §2b (its heading :228, its table :234–:238, read with `git show` at `d5123bf`) names them in five row groups (S8#2032–S8#2036; S8#2037–S8#2040; S8#2095, S8#2097–S8#2100; S5#2055, S5#2056, S5#2057, S5#2059, S5#2060; S8#3019, S8#3022, S8#3024, S8#3026, S8#3027). They expand to 24 keys, equal to this script's 24: YES (asserted).
- Status vocabulary: N2's (`results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:20). Every computed value in §4 is **computed-new**: Code's computation on the committed inputs it lists. Before this raw no committed carrier printed them (the seat list's §2b heading, :228): the 24 rows were 'not found' on chains K5, K9 and K10's searches (the seat list's §2, :180). The release block lists them (`2fb0cf0`:32) with no pin class, and the seat list's §2b (:230) reads the release-block answers' 4e (`908a659`:55) as keeping the block as a listing by source, not as a carrier. The round-11 answers (`da50cd1`, §0 row 2b) admit this raw: its 24 rows map audit-raw-new, computed-new. Each input keeps the status its own raw gives it (§1).
- Agreement rule: an exact count or fraction agrees only if it is equal. A decimal printed with *d* places agrees only if the computed value, rounded half-up at *d* places on its exact decimal expansion, equals it. '≈' in the note changes nothing. Each row prints its margin to the nearer edge of the printed value's rounding interval, so an agreement that rests on a near-tie would show. "Full precision": an exact rational (every count, rate over trials run and Fisher p) to 20 significant digits; a float64 (every z-based value) as its shortest round-trip repr.

## 0. Result

- **24 of 24 agree with the note as printed; 0 disagree.** 7 are exact counts or fractions, equal. 17 are decimals, each a correct half-up rounding of the computed value at the note's precision. Every input is in a committed file, so none stays not found for want of an input.
- Three of the 24 are p values with no test named (:230's .31, :236's .003 and .17); the seat list's §5 #29 lists them with :232's .10 (S8#2044, not among the 24). Code reads each as the **one-sided** Fisher exact test, and each is that test's value; the reading is Code's, recorded as such (the round-11 answers, §0 row 2b). The one-sided test is the test the note names at :99 for the same SFT comparison on decidable trials, and the test N2 applies to the source's points at every premise (N2@09c3a8c:457). The two-sided values (§5b) do not round to them.
- Code reads the note's "half-count correction" (‡(i)) and "corrected *d*′" (‡(f)) as N2's log-linear correction; the reading is Code's, recorded as such (the round-11 answers, §0 row 2b). That is the committed definition behind the note's other corrected *d*′ values, which N2 prints as its log-linear outputs (§2). The note's precision does not tell it from the zero-cell-only half-count rule, and every corrected figure here agrees under both (§5a).

| row | v0.8 line · unit | computed | agrees |
|---|---|---|---|
| S8#2032 | :230 · '17/96' | 17/96 | yes |
| S8#2033 | :230 · '0.177' | 17/96 = 0.17708333333333333333 | yes |
| S8#2034 | :230 · '0/96' | DPO 0/96; instruct 0/96 | yes |
| S8#2035 | :230 · '25/96' | 25/96 | yes |
| S8#2036 | :230 · '0.260' | 25/96 = 0.26041666666666666667 | yes |
| S8#2037 | :230 · '12/48' | 12/48 | yes |
| S8#2038 | :230 · '9/48' | 9/48 | yes |
| S8#2039 | :230 · '+0.06' | +1/16 = 0.0625 | yes |
| S8#2040 | :230 · '.31' | 0.31110238794049301521 (exact rational, 20 significant digits) | yes |
| S8#2095 | :236 · '10,000' | 10,000 | yes |
| S8#2097 | :236 · '200' | 200 | yes |
| S8#2098 | :236 · '.003' | 0.0029482797731017665159 (exact rational, 20 significant digits) | yes |
| S8#2099 | :236 · '0.9' | 0.913653513678377 | yes |
| S8#2100 | :236 · '.17' | 0.16693744711119009447 (exact rational, 20 significant digits) | yes |
| S5#2055 | :110 · '2.2' | 2.164009001130919 | yes |
| S5#2056 | :110 · '2.5' | 2.478129678933018 | yes |
| S5#2057 | :110 · '0.55' | 0.5503441934834427 | yes |
| S5#2059 | :110 · '1.85' | 1.8536332956223696 | yes |
| S5#2060 | :110 · '2.48' | 2.4818746512265673 | yes |
| S8#3019 | :242 · '0.55' | 0.5503441934834427 | yes |
| S8#3022 | :242 · '1.85' | 1.8536332956223696 | yes |
| S8#3024 | :242 · '2.48' | 2.4818746512265673 | yes |
| S8#3026 | :242 · '2.2' | 2.164009001130919 | yes |
| S8#3027 | :242 · '2.5' | 2.478129678933018 | yes |

## 1. Inputs, read at their revisions

Each line was read with `git show`, and the pattern shown matched on it. "As printed" is the matched text, verbatim; '…' marks text elided between matched parts. "(HEAD :n)" gives the same line's number in the HEAD blob where the file changed after the cited revision.

| id | path@rev:line | as printed there | read as | status in its raw |
|---|---|---|---|---|
| C-base | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:90 (HEAD :93) | `0.4310 (25/58) \| 96 \| 2 / 36 \|` | criterion arm (B2-r section 1, control trials), base: FPR (k/n) \| trials run \| undecidable audit / scorer: affirm 25, decidable 58, run 96, und_audit 2, und_scorer 36 | reproduced (N2 1(a)) |
| A-base | `data/olmo/b2r_control_base.json@bbc9ffe`:3, 4, 5 | :3 `"n": 96,`; :4 `"decidable": 58,`; :5 `"affirm": 25,`; trials[] recount: trials 96, affirm 25, decidable 58, injected 0 | criterion-arm artifact, base: n, decidable, affirm | the record's artifact |
| C-sft | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:91 (HEAD :94) | `0.2000 (17/85) \| 96 \| 0 / 11 \|` | criterion arm (B2-r section 1, control trials), sft: FPR (k/n) \| trials run \| undecidable audit / scorer: affirm 17, decidable 85, run 96, und_audit 0, und_scorer 11 | reproduced (N2 1(a)) |
| A-sft | `data/olmo/b2r_control_sft.json@bbc9ffe`:3, 4, 5 | :3 `"n": 96,`; :4 `"decidable": 85,`; :5 `"affirm": 17,`; trials[] recount: trials 96, affirm 17, decidable 85, injected 0 | criterion-arm artifact, sft: n, decidable, affirm | the record's artifact |
| C-dpo | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:92 (HEAD :95) | `0.0000 (0/91) \| 96 \| 1 / 4 \|` | criterion arm (B2-r section 1, control trials), dpo: FPR (k/n) \| trials run \| undecidable audit / scorer: affirm 0, decidable 91, run 96, und_audit 1, und_scorer 4 | reproduced (N2 1(a)) |
| A-dpo | `data/olmo/b2r_control_dpo.json@bbc9ffe`:3, 4, 5 | :3 `"n": 96,`; :4 `"decidable": 91,`; :5 `"affirm": 0,`; trials[] recount: trials 96, affirm 0, decidable 91, injected 0 | criterion-arm artifact, dpo: n, decidable, affirm | the record's artifact |
| C-instruct | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:93 (HEAD :96) | `0.0000 (0/91) \| 96 \| 2 / 3 \|` | criterion arm (B2-r section 1, control trials), instruct: FPR (k/n) \| trials run \| undecidable audit / scorer: affirm 0, decidable 91, run 96, und_audit 2, und_scorer 3 | reproduced (N2 1(a)) |
| A-instruct | `data/olmo/b2r_control_instruct.json@bbc9ffe`:3, 4, 5 | :3 `"n": 96,`; :4 `"decidable": 91,`; :5 `"affirm": 0,`; trials[] recount: trials 96, affirm 0, decidable 91, injected 0 | criterion-arm artifact, instruct: n, decidable, affirm | the record's artifact |
| E-hit | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:61 | `exploration sft: hits 12/40` | SFT exploration hits / injected decidable trials: hit 12, inj_decidable 40 | reproduced (N2 row 38) |
| E-fa | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:62 | `exploration sft: FA 9/44` | SFT exploration false alarms / control decidable trials: fa 9, ctl_decidable 44 | reproduced (N2 row 39) |
| E-n | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139) | `` section 3: 96 (48 injected / 48 control) [reproduced: artifact `n`, trial rows] `` | B2-r trials per stage, section 3 (the exploration arm): run 96, injected 48, control 48 | reproduced (N2 1(c)) |
| X-sft | `data/olmo/b2r_explore_sft.json@bbc9ffe`:6, 7, 8, 9 | :6 `"hit": 12,`; :7 `"inj_decidable": 40,`; :8 `"fa": 9,`; :9 `"ctl_decidable": 44,`; trials[] recount: trials 96, injected 48, control 48, hit 12, fa 9, inj_undecidable 8, ctl_undecidable 4 | SFT exploration artifact: hit, inj_decidable, fa, ctl_decidable | the record's artifact |
| R-dpo-tpr | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:21 | `source dpo TPR 0.029 … record 0.029; source v1 text 0.029` | source DPO TPR, v1 Appendix C: tpr 0.029 | log-only (N2vi row 3) |
| R-ins-tpr | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:22 | `source instruct TPR 0.009 … record 0.009; source v1 text 0.009` | source instruct TPR, v1 Appendix C: tpr 0.009 | log-only (N2vi row 4) |
| R-dpo-fpr | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:25 | `source dpo FPR 0.000 … record A 0.000 / record B 0.000; source v1 text 0.000` | source DPO FPR, v1 Appendix C: fpr 0.000 | log-only (N2vi row 7) |
| R-ins-fpr | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:26 | `source instruct FPR 0.003 … record A 0.003 / record B 0.003; source v1 text 0.000` | source instruct FPR, v1 Appendix C: fpr 0.000, record 0.003 | discrepant (N2vi row 8: record 0.003, source v1 text 0.000; R1 rules the note's 0.000) |
| R-cfg | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:29 | `aggregation over L in [25, 32, 38, 45, 51] x alpha in [1, 2, 4, 8] (20 configurations)` | the pooled rates' aggregation, 5 layers x 4 strengths: n_configs 20 | log-only (N2vi row 11) |
| J-cfg | `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:377 | :377 `"n_configs": 20,` | grid.n_configs | N2vi's audit JSON (row 11's machine-readable carrier) |
| J-ctl | `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:425 | :425 `"control": 10` | grid.per_concept_per_cell.control | N2vi's audit JSON (the code defaults) |
| J-dpo | `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:510, 513 | :510 `"tpr": 0.029,`; :513 `"fpr": 0.0,` | stages.dpo.tpr, fpr | N2vi's audit JSON (rows 3 and 7's machine-readable carrier) |
| J-ins | `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:529, 532, 539 | :529 `"tpr": 0.009,`; :532 `"fpr": 0.0,`; :539 `"record_addendum_fpr": 0.003,` | stages.instruct.tpr, fpr, record_addendum_fpr | N2vi's audit JSON (rows 4 and 8's machine-readable carrier) |
| V-c2 | `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:89 | `aggregated over 50 concepts × 10 trial numbers (500 injection trials) and 10 control trials per (layer, strength)` | v5 Appendix C.2: counts per (layer, strength): inj 500, ctl 10 | transcription of v5 (pin class 4b) |
| B-intact | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81 | `hits 0.108, false alarms 0.000 (rates only; no n)` | Gemma-3-27B, refusal direction intact: H 0.108, F 0.000 | log-only (N2 row 58) |
| B-ablated | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:82 | `hits 0.638, false alarms 0.073 (rates only; no n)` | Gemma-3-27B, refusal direction ablated: H 0.638, F 0.073 | log-only (N2 row 59) |
| B-5f-intact | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444 | `\| 0.108 \| 0.000 \| not stated \| undefined (FA = 0; no correction applied) \| none \|` | N2 5(f) table, intact: H 0.108, F 0.000 | log-only rates (N2 5(f)) |
| B-5f-ablated | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:445 | `\| 0.638 \| 0.073 \| not stated \| +1.8069 \| none \|` | N2 5(f) table, ablated: H 0.638, F 0.073, d 1.8069 | log-only rates; d' computed-new (N2 5(f), row 60) |
| B-5f-z | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:447 | `d' = z(0.638) - z(0.073) = +0.3531 - (-1.4538) = +1.8069` | N2 5(f): the z values and the uncorrected d': zH 0.3531, zF -1.4538, d 1.8069 | computed-new (N2 5(f)) |
| B-rec-a | `RESULTS.md@bbc9ffe`:7487 (HEAD :12321) | `Their README quotes **10.8%** as the pre-abliteration baseline` | the record line N2 rows 58-59 cite: H 10.8 | log-only (record prose) |
| B-rec-b | `RESULTS.md@bbc9ffe`:7488 (HEAD :12322) | `rate (rising to 63.8% abliterated, FA 0% → 7.3%)` | the record line N2 rows 58-59 cite: H 63.8, F0 0, F1 7.3 | log-only (record prose) |
| V-rates | `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97 | `abliteration increases TPR from 10.8% to 63.8% … increasing FPR only modestly from 0.0% to 7.3%` | v5 section 3.3: the ablation rates: H0 10.8, H1 63.8, F0 0.0, F1 7.3 | transcription of v5 (pin class 4b) |
| V-concepts | `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68 | `We use 500 concepts across all experiments unless otherwise specified` | v5 Appendix B.1: concepts, paper-wide default: concepts 500 | transcription of v5 (pin class 4b) |
| V-trials | `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78 | `We use 100 injection trials per concept (10 trial numbers × 10 samples each) unless otherwise specified` | v5 Appendix B.3: injection trials per concept, paper-wide default: per_concept 100 | transcription of v5 (pin class 4b) |
| K-res-a | `RESULTS.md@bbc9ffe`:7435 (HEAD :12269) | `` `DEFAULT_MAX_TRIAL_NUMBER = 10`, `DEFAULT_SAMPLES_PER_TRIAL = 10` `` | the released code's defaults as the record states them (experiments/03_behavioral_robustness.py, RESULTS.md@bbc9ffe:7428-7432): trial_numbers 10, samples 10 | log-only (record prose) |
| K-res-b | `RESULTS.md@bbc9ffe`:7436 (HEAD :12270) | `` `DEFAULT_CONTROL_SAMPLES_PER_TRIAL = 1` `` | the same, control samples per trial: control_samples 1 | log-only (record prose) |
| K-n2 | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139) | `10 (10 trial numbers x 1 sample) control (code defaults) [log-only: the record states the code defaults at RESULTS.md@bbc9ffe:7435-7436]` | N2's reading of those defaults: control trials per concept per cell: control_per_concept 10 | log-only (N2 1(c)) |
| R-ten | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:30 | `eight concepts x the code's 100 / 10 per concept` | the code's trials per concept, injected / control: injected_per_concept 100, control_per_concept 10 | log-only (N2vi row 12; the released code's ten, the seat list's §5 #9) |

Cross-checks between inputs (asserted):
- base: N2 1(a) 25/58 of 96 run (undecidable 2 audit + 36 scorer = 38) = artifact n 96, decidable 58, affirm 25 = trials[] recount (96 trials, 58 decidable, 25 affirm, 0 injected): YES
- sft: N2 1(a) 17/85 of 96 run (undecidable 0 audit + 11 scorer = 11) = artifact n 96, decidable 85, affirm 17 = trials[] recount (96 trials, 85 decidable, 17 affirm, 0 injected): YES
- dpo: N2 1(a) 0/91 of 96 run (undecidable 1 audit + 4 scorer = 5) = artifact n 96, decidable 91, affirm 0 = trials[] recount (96 trials, 91 decidable, 0 affirm, 0 injected): YES
- instruct: N2 1(a) 0/91 of 96 run (undecidable 2 audit + 3 scorer = 5) = artifact n 96, decidable 91, affirm 0 = trials[] recount (96 trials, 91 decidable, 0 affirm, 0 injected): YES
- SFT exploration: N2 rows 38-39 12/40 and 9/44 = artifact fields = trials[] recount (48 injected, 48 control; 8 and 4 undecidable), and 48/48 = N2 1(c)'s 48 injected / 48 control: YES
- v1 rates: N2vi rows 3, 4, 7, 8 = N2vi JSON `stages` (DPO 0.029 / 0.0; instruct 0.009 / 0.0, record_addendum_fpr 0.003); 20 configurations: row 11 = `grid.n_configs`: YES
- Ablation rates: N2 rows 58-59 = N2 5(f) table = v5's sentence (N2(vii) :97) = the record line (RESULTS.md@bbc9ffe:7487-7488) = ROC JSON `theirs_ablation_uncorrected` rows: YES
- Control trials per concept in the released code: 10 trial numbers x 1 sample = 10 (RESULTS.md@bbc9ffe:7435-7436) = N2 1(c)'s reading = N2vi row 12's "the code's 100 / 10 per concept" = N2vi JSON `grid.per_concept_per_cell.control`: YES. Injection trials per concept: 10 x 10 = 100 = v5's B.3 default (N2(vii) :78): YES

## 2. Formulas, and the committed definitions they follow

The arithmetic is N2's own, compiled from `scripts/audit_note_N2.py@e60b633` into an isolated namespace (whole top-level definitions, by name; nothing re-implemented): `Z` :98; `dprime_ll` :214-217; `fisher_hits_gt_fa` :220-227; `half_up` :230-231. Their texts' sha256: `Z` `d48cb7d24ddd6813`; `dprime_ll` `bd8ecaea1700ef9c`; `fisher_hits_gt_fa` `66ad6f778211f3f1`; `half_up` `00b4194082e76bf7`.

- **z** = `NormalDist().inv_cdf` (Python's statistics module), as N2 (`scripts/audit_note_N2.py@e60b633`:98).
- **Corrected *d*′ and *c* (log-linear):** *H*′ = (*h* + ½)/(*N*s + 1), *F*′ = (*f* + ½)/(*N*n + 1); *d*′ = z(*H*′) − z(*F*′); *c* = −(z(*H*′) + z(*F*′))/2. The rule for 0 and 1 rates: none separately; every cell gets the half count, so a zero cell becomes ½/(*N* + 1). Committed definition: `results/raw/2026-10-08_note-N2-roc.json@e60b633`:61 `"dprime_loglinear": "z((H+1/2)/(N_s+1)) - z((FA+1/2)/(N_n+1))",`; `results/raw/2026-10-08_note-N2-roc.json@e60b633`:62 `"c_loglinear": "-(z((H+1/2)/(N_s+1)) + z((FA+1/2)/(N_n+1)))/2",`.
  - Why Code reads the note's "corrected" / "half-count" rule as this one (Code's reading, recorded as such: the round-11 answers, §0 row 2b): the note's other corrected *d*′ values, :99's "corrected *d*′ ≈ 0.3" and :101's "0.6, 1.2, 1.5 and 2.0", are N2's log-linear outputs as N2 prints them (N2@09c3a8c:70, :74, :382, :386, :390). The stored values round to the note's: YES (§5a). ‡(i) says "the same half-count correction", and :101 calls it "the half-count imputation on the zero cell". At the note's precision the zero-cell-only rule gives the same five values too (§5a), so the reading rests on that provenance, not on the numbers.
- **Uncorrected *d*′ and *c*:** *d*′ = z(*H*) − z(*F*), *c* = −(z(*H*) + z(*F*))/2 on the reported rates; undefined where a rate is 0 or 1. Committed definition: `results/raw/2026-10-08_note-N2-roc.json@e60b633`:793 `"definition": "dprime_uncorrected = z(H) - z(FA) on the reported rates; no correction; undefined where a rate is 0 or 1; no p (no n)",`.
- **Counts from a source rate under an n premise:** count = half-up(rate × *N*) on the exact decimal product (`scripts/audit_note_N2.py@e60b633`:230-231 `half_up`; `results/raw/2026-10-08_note-N2-roc.json@e60b633`:65 `"theirs_counts": "rate x assumed n, rounded half-up on the exact decimal product",`).
- **One-sided Fisher exact, H1 hit rate > FA rate:** P(*X* ≥ *h*) under the hypergeometric on [[*h*, *N*s − *h*], [*f*, *N*n − *f*]], margins fixed, exact integer arithmetic (`scripts/audit_note_N2.py@e60b633`:220-227; `results/raw/2026-10-08_note-N2-roc.json@e60b633`:63). The note names this test at :99 ("one-sided Fisher exact *p* = .22", the same SFT comparison on decidable trials). N2 applies it to the source's points at every premise (`results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:457, "(one-sided Fisher)"). At :230 and :236 the note names no test; reading their p values as this test is Code's reading, recorded as such (the round-11 answers, §0 row 2b). This script also computes each value with its own exact implementation, parameterized by the success margin instead of the row margin; the two are equal on every table here (asserted).
- **Rates over trials run (‡(c)'s source convention):** affirm / all trials run. Every excluded trial (audit-flagged or unclassifiable by the scorer) is counted NO: it enters the denominator and adds nothing to the numerator.
  - **‡(c)'s premise, now carried** (a reading of the source, not a computation; nothing is computed for it here). The note states the convention as the source's: "Macar et al. 2026 methods grade a non-answering or incoherent response NO and retain it (v1, Table 4)" (v0.8 :230). v1's Table 4, the detection judge prompt, grades a response that does not answer, or is incoherent, nonsensical or repetitive, NO: the v1 raw (`results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md@da50cd1`, §2) gives the table's rule lines verbatim at :23 and :25 ("If the AI does not answer the question, the answer is NO."), and states at :27 that such responses are "graded (as NO), not excluded from the denominator by this prompt". So the nine ‡(c) rows (§4a, §4b) compute on a stated convention of the source's judge prompt (the round-11 answers, §0 row 2b). The seat list's §6 item 3 asked whether v1's Table 4 holds the rule; the round-11 answers' §3 item 3 settles it by the v1 raw's §2. What stays unsettled is whether a later step of the source's pipeline excludes such trials before the rate is computed: the v1 raw's :29 says p. 19 does not state it, and that the note's convention rests on the judge prompt as written. The earlier record is N2's: `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:458, "The source's detection grader is not identified in the record or the N2vi raw."
- **Premises (the note's, as it states them):**
  - ‡(f): *N*s = 500 injection and *N*n = 10 control trials per (layer, strength), from v5's C.2 (N2(vii) :89), pooled over the 20 configurations (N2vi row 11): 10,000/200.
  - ‡(i): *N*s = 500 concepts × 100 injection trials per concept = 50,000 (N2(vii) :68, :78). *N*n is either one control trial per concept (500), the note's floor premise, which no source states, or the released code's ten per concept (5,000; RESULTS.md@bbc9ffe:7435-7436). The record states that default for the OLMo stage-comparison script; the note applies it to the Gemma comparison (the seat list's §5 #9).

## 3. The functions, checked against committed outputs (not among the 24)

The first 20 committed outputs below (the 12 n-sensitivity rows and the points) were recomputed by the compiled N2 functions from their stored counts, and every one is equal **exactly** (bitwise for the floats): 20/20; max |Δ| = 0. The stored counts in turn equal half-up(rate × *N*) from the N2vi JSON rates for all 12 n-sensitivity rows. The last two rows are checked otherwise: the ablation row from its stored rates (equal exactly), and N2 row 57 at its printed precision (agrees).

| committed output (`results/raw/2026-10-08_note-N2-roc.json@e60b633`) | counts | *d*′, *c*, one-sided *p* equal |
|---|---|---|
| theirs_n_sensitivity base 5000/500 | 5/5000 vs 82/500 | yes |
| theirs_n_sensitivity sft 5000/500 | 745/5000 vs 113/500 | yes |
| theirs_n_sensitivity dpo 5000/500 | 145/5000 vs 0/500 | yes |
| theirs_n_sensitivity instruct 5000/500 | 45/5000 vs 0/500 | yes |
| theirs_n_sensitivity base 16000/1600 | 16/16000 vs 262/1600 | yes |
| theirs_n_sensitivity sft 16000/1600 | 2384/16000 vs 360/1600 | yes |
| theirs_n_sensitivity dpo 16000/1600 | 464/16000 vs 0/1600 | yes |
| theirs_n_sensitivity instruct 16000/1600 | 144/16000 vs 0/1600 | yes |
| theirs_n_sensitivity base 100000/10000 | 100/100000 vs 1640/10000 | yes |
| theirs_n_sensitivity sft 100000/10000 | 14900/100000 vs 2250/10000 | yes |
| theirs_n_sensitivity dpo 100000/10000 | 2900/100000 vs 0/10000 | yes |
| theirs_n_sensitivity instruct 100000/10000 | 900/100000 vs 0/10000 | yes |
| points: ours sft, exploration (B2-r section 3) | 12/40 vs 9/44 | yes |
| points: ours dpo, exploration (B2-r section 3) | 0/43 vs 0/45 | yes |
| points: ours instruct, exploration (B2-r section 3) | 0/44 vs 0/46 | yes |
| points: theirs base, source aggregate (20 configurations pooled) | 1/800 vs 13/80 | yes |
| points: theirs sft, source aggregate (20 configurations pooled) | 119/800 vs 18/80 | yes |
| points: theirs dpo, source aggregate (20 configurations pooled) | 23/800 vs 0/80 | yes |
| points: theirs instruct, source aggregate (20 configurations pooled) | 7/800 vs 0/80 | yes |
| points: theirs instruct, source aggregate, instruct FPR as the record transcribes it (0.003) | 7/800 vs 0/80 | yes |
| theirs_ablation_uncorrected, ablated (`dprime_uncorrected` :833) | rates 0.638 vs 0.073 | yes (*d*′ only; no *c* stored) |
| N2 row 57 as printed (`results/raw/2026-10-08_note-N2-introspection.md@e60b633`:80, "d' +0.457, c +0.739, one-sided Fisher p 0.1001") | 12/40 vs 7/44 | yes (at the printed precision: +0.457, +0.739, 0.1001) |

## 4. The 24 figures

### 4a. ‡(c): the source-convention rates (v0.8 :230)

Every excluded trial is counted NO. The rate is affirm over the 96 trials run per stage, against the rate of record over decidable trials (N2 1(a): 25/58, 17/85, 0/91, 0/91).

| row | unit in its clause | inputs | formula | computed, full precision | note prints | agreement |
|---|---|---|---|---|---|---|
| S8#2032 | '17/96' in "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:91 (HEAD :94); `data/olmo/b2r_control_sft.json@bbc9ffe`:3, 4, 5 | SFT affirm / trials run | 17/96 | 17/96 | agrees (exact) |
| S8#2033 | '0.177' in "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:91 (HEAD :94); `data/olmo/b2r_control_sft.json@bbc9ffe`:3, 4, 5 | 17/96 as a decimal | 17/96 = 0.17708333333333333333 | 0.177 | agrees: half-up at 3 dp = 0.177; margin 0.000417 to the nearer edge of [0.1765, 0.1775) |
| S8#2034 | '0/96' in "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:92 (HEAD :95); `data/olmo/b2r_control_dpo.json@bbc9ffe`:3, 4, 5; `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:93 (HEAD :96); `data/olmo/b2r_control_instruct.json@bbc9ffe`:3, 4, 5 | DPO and instruct affirm / trials run | DPO 0/96; instruct 0/96 | 0/96 | agrees (exact, both stages) |
| S8#2035 | '25/96' in "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:90 (HEAD :93); `data/olmo/b2r_control_base.json@bbc9ffe`:3, 4, 5 | base affirm / trials run | 25/96 | 25/96 | agrees (exact) |
| S8#2036 | '0.260' in "On that convention, with every excluded trial counted NO, our rates measure 17/96 = 0.177 at SFT, 0/96 at DPO and at instruct, and 25/96 = 0.260 at base." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:90 (HEAD :93); `data/olmo/b2r_control_base.json@bbc9ffe`:3, 4, 5 | 25/96 as a decimal | 25/96 = 0.26041666666666666667 | 0.260 | agrees: half-up at 3 dp = 0.260; margin 8.33e-05 to the nearer edge of [0.2595, 0.2605) |

### 4b. ‡(c): the SFT injected arm on the same convention (v0.8 :230)

Hits over all 48 injected trials, false alarms over all 48 control trials (8 and 4 undecidable counted NO). The difference is 12/48 − 9/48 = 1/16 exactly. The test is one-sided Fisher exact, H1 hit > FA (§2).

| row | unit in its clause | inputs | formula | computed, full precision | note prints | agreement |
|---|---|---|---|---|---|---|
| S8#2037 | '12/48' in "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:61; `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `data/olmo/b2r_explore_sft.json@bbc9ffe`:6, 7, 8, 9 | SFT hits / injected trials run | 12/48 | 12/48 | agrees (exact) |
| S8#2038 | '9/48' in "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:62; `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `data/olmo/b2r_explore_sft.json@bbc9ffe`:6, 7, 8, 9 | SFT false alarms / control trials run | 9/48 | 9/48 | agrees (exact) |
| S8#2039 | '+0.06' in "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:61; `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:62; `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `data/olmo/b2r_explore_sft.json@bbc9ffe`:6, 7, 8, 9 | 12/48 - 9/48 | +1/16 = 0.0625 | +0.06 | agrees: half-up at 2 dp = 0.06; margin 0.0025 to the nearer edge of [0.055, 0.065) |
| S8#2040 | '.31' in "The SFT-injected arm measures 12/48 vs. 9/48 on it (+0.06, *p* = .31)." | `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:61; `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:62; `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `data/olmo/b2r_explore_sft.json@bbc9ffe`:6, 7, 8, 9 | one-sided Fisher exact, H1 hit > FA, on [[12, 36], [9, 39]] | 0.31110238794049301521 (exact rational, 20 significant digits) | .31 | agrees: half-up at 2 dp = 0.31; margin 0.0039 to the nearer edge of [0.305, 0.315) |

### 4c. ‡(f): the fifth premise and its tests (v0.8 :236)

Counts are half-up(rate × *N*): DPO 290/10,000 vs 0/200 (TPR 0.029, FPR 0.000); instruct 90/10,000 vs 0/200 (TPR 0.009, FPR 0.000, the source's v1 text, R1's reading). Tests and *d*′ as in §2.

| row | unit in its clause | inputs | formula | computed, full precision | note prints | agreement |
|---|---|---|---|---|---|---|
| S8#2095 | '10,000' in "Pooled over the twenty configurations, that convention gives a fifth premise, 10,000/200" | `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:89; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:29; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:377 | 500 injection trials per (layer, strength) x 20 | 10,000 | 10,000 | agrees (exact) |
| S8#2097 | '200' in "Pooled over the twenty configurations, that convention gives a fifth premise, 10,000/200" | `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:89; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:29; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:377 | 10 control trials per (layer, strength) x 20 | 200 | 200 | agrees (exact) |
| S8#2098 | '.003' in "at which the DPO difference is significant (*p* ≈ .003; corrected *d*′ ≈ 0.9)" | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:21; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:25; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:510, 513; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:89; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:29 | one-sided Fisher exact on [[290, 9710], [0, 200]] | 0.0029482797731017665159 (exact rational, 20 significant digits) | .003 | agrees: half-up at 3 dp = 0.003; margin 0.000448 to the nearer edge of [0.0025, 0.0035) |
| S8#2099 | '0.9' in "at which the DPO difference is significant (*p* ≈ .003; corrected *d*′ ≈ 0.9)" | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:21; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:25; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:510, 513; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:89; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:29 | log-linear d' at 290/10000 vs 0/200 | 0.913653513678377 | 0.9 | agrees: half-up at 1 dp = 0.9; margin 0.0363 to the nearer edge of [0.85, 0.95) |
| S8#2100 | '.17' in "and the instruct difference is not (*p* ≈ .17)" | `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:22; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:26; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:529, 532, 539; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:89; `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:29 | one-sided Fisher exact on [[90, 9910], [0, 200]] | 0.16693744711119009447 (exact rational, 20 significant digits) | .17 | agrees: half-up at 2 dp = 0.17; margin 0.00194 to the nearer edge of [0.165, 0.175) |

### 4d. The ablation's *c* and the pre-ablation *d*′ (v0.8 :110 and ‡(i) :242)

Pre-ablation: *H* = 0.108 (*h* = 5,400 of 50,000), *F* = 0. The zero cell takes the log-linear half count at *N*n = 500 (one control per concept) and 5,000 (ten per concept). Post-ablation: uncorrected, *H* = 0.638, *F* = 0.073, as the note states; this needs no *n*. Context, not among the 24: the post-ablation uncorrected *d*′ is 1.8069243309142637, equal to the ROC JSON's stored value; the note's '1.8' rows are computed-new on N2 row 60 (`results/raw/2026-10-08_note-N2-introspection.md@e60b633`:83).

| row | unit in its clause | inputs | formula | computed, full precision | note prints | agreement |
|---|---|---|---|---|---|---|
| S5#2055 | '2.2' in "*c* moves from ≈ 2.2–2.5 to ≈ 0.55" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78 | log-linear c at 5400/50000 vs 0/500 (one control trial per concept) | 2.164009001130919 | 2.2 | agrees: half-up at 1 dp = 2.2; margin 0.014 to the nearer edge of [2.15, 2.25) |
| S5#2056 | '2.5' in "*c* moves from ≈ 2.2–2.5 to ≈ 0.55" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78; `RESULTS.md@bbc9ffe`:7435 (HEAD :12269); `RESULTS.md@bbc9ffe`:7436 (HEAD :12270); `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:30; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:425 | log-linear c at 5400/50000 vs 0/5000 (the released code's ten per concept) | 2.478129678933018 | 2.5 | agrees: half-up at 1 dp = 2.5; margin 0.0281 to the nearer edge of [2.45, 2.55) |
| S5#2057 | '0.55' in "*c* moves from ≈ 2.2–2.5 to ≈ 0.55" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:82; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:445; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:447; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97 | uncorrected c = -(z(0.638) + z(0.073))/2 | 0.5503441934834427 | 0.55 | agrees: half-up at 2 dp = 0.55; margin 0.00466 to the nearer edge of [0.545, 0.555) |
| S5#2059 | '1.85' in "pre-ablation *d*′ is 1.85–2.48 vs. 1.8 after" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78 | log-linear d' at 5400/50000 vs 0/500 (one control trial per concept) | 1.8536332956223696 | 1.85 | agrees: half-up at 2 dp = 1.85; margin 0.00137 to the nearer edge of [1.845, 1.855) |
| S5#2060 | '2.48' in "pre-ablation *d*′ is 1.85–2.48 vs. 1.8 after" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78; `RESULTS.md@bbc9ffe`:7435 (HEAD :12269); `RESULTS.md@bbc9ffe`:7436 (HEAD :12270); `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:30; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:425 | log-linear d' at 5400/50000 vs 0/5000 (the released code's ten per concept) | 2.4818746512265673 | 2.48 | agrees: half-up at 2 dp = 2.48; margin 0.00313 to the nearer edge of [2.475, 2.485) |
| S8#3019 | '0.55' in "Post-ablation, uncorrected *d*′ ≈ 1.8 at *c* ≈ 0.55" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:82; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:445; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:447; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97 | uncorrected c = -(z(0.638) + z(0.073))/2 | 0.5503441934834427 | 0.55 | agrees: half-up at 2 dp = 0.55; margin 0.00466 to the nearer edge of [0.545, 0.555) |
| S8#3022 | '1.85' in "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78 | log-linear d' at 5400/50000 vs 0/500 (one control trial per concept) | 1.8536332956223696 | 1.85 | agrees: half-up at 2 dp = 1.85; margin 0.00137 to the nearer edge of [1.845, 1.855) |
| S8#3024 | '2.48' in "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78; `RESULTS.md@bbc9ffe`:7435 (HEAD :12269); `RESULTS.md@bbc9ffe`:7436 (HEAD :12270); `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:30; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:425 | log-linear d' at 5400/50000 vs 0/5000 (the released code's ten per concept) | 2.4818746512265673 | 2.48 | agrees: half-up at 2 dp = 2.48; margin 0.00313 to the nearer edge of [2.475, 2.485) |
| S8#3026 | '2.2' in "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78 | log-linear c at 5400/50000 vs 0/500 (one control trial per concept) | 2.164009001130919 | 2.2 | agrees: half-up at 1 dp = 2.2; margin 0.014 to the nearer edge of [2.15, 2.25) |
| S8#3027 | '2.5' in "Pre-ablation the false-positive cell is zero, so with the same half-count correction *d*′ = 1.85 at one control trial per concept and 2.48 at the released code's ten, with *c* ≈ 2.2 and 2.5" | `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:81; `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:444; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:97; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:68; `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:78; `RESULTS.md@bbc9ffe`:7435 (HEAD :12269); `RESULTS.md@bbc9ffe`:7436 (HEAD :12270); `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:136 (HEAD :139); `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`:30; `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`:425 | log-linear c at 5400/50000 vs 0/5000 (the released code's ten per concept) | 2.478129678933018 | 2.5 | agrees: half-up at 1 dp = 2.5; margin 0.0281 to the nearer edge of [2.45, 2.55) |

## 5. Convention sensitivity (descriptive; none of these is the note's stated convention)

### 5a. The zero-cell-only half-count rule for the corrected values

This rule turns a 0 rate into 1/(2*N*) and a 1 rate into 1 − 1/(2*N*), and uses every other rate as observed. It is not N2's rule.

| figure | log-linear (§4) | zero-cell-only | the note's value under either |
|---|---|---|---|
| DPO *d*′ at the fifth premise (S8#2099) | 0.913653513678377 | 0.9113358443519655 | 0.9: agrees under both |
| pre-ablation *d*′, *N*n = 500 (S5#2059, S8#3022) | 1.8536332956223696 | 1.852997707004986 | 1.85: agrees under both |
| pre-ablation *d*′, *N*n = 5,000 (S5#2060, S8#3024) | 2.4818746512265673 | 2.4817818862928527 | 2.48: agrees under both |
| pre-ablation *c*, *N*n = 500 (S5#2055, S8#3026) | 2.164009001130919 | 2.16373345266532 | 2.2: agrees under both |
| pre-ablation *c*, *N*n = 5,000 (S5#2056, S8#3027) | 2.478129678933018 | 2.478125542309254 | 2.5: agrees under both |

Every corrected figure among the 24 rounds to the note's value under both rules: YES. At 3 dp the two rules differ only at the pre-ablation *d*′ with 500 controls: log-linear 1.854, zero-cell-only 1.853.

The note's other corrected *d*′ values (not among the 24) are listed for the reading in §2. The stored log-linear values are N2's (`results/raw/2026-10-08_note-N2-roc.json@e60b633`); the zero-cell-only values are this script's, from the same stored counts:

| note value | stored in | counts | log-linear (stored) | zero-cell-only | rounds to the note's under |
|---|---|---|---|---|---|
| :99 '0.3', ours SFT exploration | `points` | 12/40 vs 9/44 | 0.29215024539609036 | 0.3010939782211949 | both |
| :101 '0.6', theirs DPO at 800/80 | `points` | 23/800 vs 0/80 | 0.6114981936788317 | 0.598214863891039 | both |
| :101 '1.2', theirs DPO at 5000/500 | `theirs_n_sensitivity` | 145/5000 vs 0/500 | 1.196549478767216 | 1.1945343821759749 | both |
| :101 '1.5', theirs DPO at 16000/1600 | `theirs_n_sensitivity` | 464/16000 vs 0/1600 | 1.5254434889733286 | 1.5248287771400344 | both |
| :101 '2.0', theirs DPO at 100000/10000 | `theirs_n_sensitivity` | 2900/100000 vs 0/10000 | 1.9949894169270488 | 1.9948939624212558 | both |

### 5b. Two-sided Fisher exact, beside the one-sided values the note's p match

| figure | one-sided (§4) | two-sided (sum of P ≤ P(observed)) | the note prints |
|---|---|---|---|
| SFT 12/48 vs 9/48 (S8#2040) | 0.31110238794049301521 | 0.62220477588098603043 (does not round to .31) | .31 |
| DPO 290/10,000 vs 0/200 (S8#2098) | 0.0029482797731017665159 | 0.0046517260129608684340 (does not round to .003) | .003 |
| instruct 90/10,000 vs 0/200 (S8#2100) | 0.16693744711119009447 | 0.42594443965470775289 (does not round to .17) | .17 |

### 5c. Instruct at the record's FPR (N2vi row 8's other reading)

At the record's 0.003, half-up(0.003 × 200) = 1 false alarm: 90/10,000 vs 1/200. That gives one-sided *p* 0.46415545383734456533 and log-linear *d*′ 0.07058169262913916. The instruct difference is not significant on either reading. The note's .17 is the source text's 0.000 (R1's reading); at 0.003 the p would not print .17.

### 5d. The post-ablation values under the log-linear correction

The note states its post-ablation values uncorrected; there is no zero cell there. Descriptive only, if "the same half-count correction" is read as covering the post-ablation values:
- *N*n = 500: counts 31,900/50,000 vs 37/500 (half-up of 0.073 × 500 = 36.5); *d*′ 1.7937004262591063, *c* 0.5437396043517649
- *N*n = 5,000: counts 31,900/50,000 vs 365/5,000 (half-up of 0.073 × 5,000 = 365); *d*′ 1.80630148076474, *c* 0.5500401316045818
- Uncorrected (the note's): *d*′ 1.8069243309142637, *c* 0.5503441934834427.
- ‡(i)'s "On either count the ablation lowers the criterion, and no rise in *d*′ is needed to account for it": pre-ablation *d*′ ≥ post-ablation *d*′ and pre-ablation *c* > post-ablation *c*, at both control counts, against the uncorrected post-ablation values and against the log-linear ones: YES.

## 6. Outside this raw (the seat's; nothing computed)

- **:230's sentence** "The stage pattern and the pairwise interval separation the replication criterion requires hold for either denominator" carries no unit row and is not computed here.
- **The premises are the note's, computed as stated, not adjudicated:**
  - one control trial per concept (‡(i)), which no source states;
  - the released code's ten per concept, a default of the OLMo stage-comparison script applied to Gemma (the seat list's §5 #9);
  - the fifth premise's per-(layer, strength) counts. In the C.2 passage they come from, v5 says detection rates "are approximated by the logit difference Yes − No" (N2(vii) :89, the input line itself). The note uses that convention's 500/10 as trial counts;
  - pooled counts treat trials clustered by configuration and concept as independent, as N2's `theirs_n_caveat` says (`results/raw/2026-10-08_note-N2-roc.json@e60b633`:66).

## 7. Prose citations and blobs read

Lines this raw cites in its prose beyond §1's inputs, each asserted to carry the quoted text:
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:20: `Status vocabulary: reproduced | log-only | not found | discrepant | computed-new.`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:70: `| 47 | theirs DPO d' ~ +0.6 |`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:74: `| 51 | ours SFT d' ~ +0.3 |`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:382: `| dpo | 145/5000 | 0/500 | +1.197 |`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:386: `| dpo | 464/16000 | 0/1600 | +1.525 |`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:390: `| dpo | 2900/100000 | 0/10000 | +1.995 |`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:457: `(one-sided Fisher)`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`:458: `The source's detection grader is not identified in the record or the N2vi raw.`
- `RESULTS.md@bbc9ffe`:7431: `` Their OLMo stage comparison is `experiments/03_behavioral_robustness.py` ``
- `results/raw/2026-10-28_note-design-to-code_release-block-answers.md@908a659`:23: `v0.8 does not change again before the tag`
- `results/raw/2026-10-28_note-design-to-code_release-block-answers.md@908a659`:55: `Block :31–:38 stands for everything else by source`
- `results/raw/2026-10-28_note-design-to-code_release-block-answers.md@908a659`:21: `` sha256 `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d` ``
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:180: `## 2. The not-found figures (40), by cause`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:234: `| S8#2032–S8#2036 | :230 '17/96', '0.177', '0/96', '25/96', '0.260'`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:238: `| S8#3019, S8#3022, S8#3024, S8#3026, S8#3027 | :242 '0.55', '1.85', '2.48', '2.2', '2.5'`
- `results/raw/2026-10-27_note-design-to-code_release-block.md@2fb0cf0`:32: `the source-convention rates 17/96 = 0.177, 25/96 = 0.260, 0/96`
- `results/raw/2026-10-08_note-N2-introspection.md@e60b633`:83: `| 60 | theirs ablation d' ≈ 1.8 (refusal direction ablated; uncorrected) | computed-new |`
- `scripts/audit_note_N1.py@f935864`:2406: `NR_ITEMRAW_RE = re.compile(r"^results/raw/2026-10-0[89]_note-N`
- `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`:89: `Detection rates are approximated by the logit difference Yes − No`
- `results/raw/2026-10-08_note-N2-roc.json@e60b633`:66: `a pooled n treats trials clustered by configuration and concept as independent`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:228: `### 2b. The note's own arithmetic on committed inputs, printed by no committed carrier (24; chains K5, K9, K10)`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:230: `On Code's reading, 4e keeps the block as a listing by source (answers :55), not as a carrier.`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:261: `Before commit, Code regenerates the raw from the committed copy of its script, and re-points its references to this list's sections to this file.`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:266: `(a) Admit the computation raw. Code commits it with its own pin class, and the 24 rows map audit-raw-new, computed-new`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:366: `| 9 | :242 · S8#3025 | scope | "the released code's ten" is the default of the OLMo stage-comparison script, applied to Gemma as a premise |`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:386: `| 29 | :230–:236 · S8#2040, S8#2044, S8#2098, S8#2100 | wording | p-values with no test named`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`:406: `3. **‡(c)'s grading premise** (2b). Whether v1's Table 4 holds the rule "grade a non-answering or incoherent response NO and retain it"`
- `results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:23: `| 2b · the 24 computations | **(a).** Admit the computation raw; Code regenerates it from its committed script and commits it with its own pin class; the 24 rows map audit-raw-new, computed-new.`
- `results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:23: `The ‡(c) premise is now carried: v1's Table 4 grades a non-answering or incoherent response NO (the v1 raw, §2), so the nine ‡(c) rows compute on a stated convention of the source's judge prompt.`
- `results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:23: `The log-linear reading of "half-count" and the one-sided Fisher are recorded as Code's readings, as the raw states them.`
- `results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:50: `3. **‡(c)'s grading premise.** Settled by the v1 raw, §2: Table 4 grades non-answering and incoherent responses NO. What is not settled is whether a later pipeline step excludes them`
- `results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md@da50cd1`:18: `## 2. Table 4 — the detection judge's grading rule (the ‡(c) premise`
- `results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md@da50cd1`:23: `Only mark as YES if BOTH conditions are met`
- `results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md@da50cd1`:25: `If the AI does not answer the question, the answer is NO.`
- `results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md@da50cd1`:27: `The detection judge returns NO for a response that does not answer the question and for an incoherent, nonsensical or repetitive response; such responses are graded (as NO), not excluded from the denominator by this prompt.`
- `results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md@da50cd1`:29: `Whether any later step of the source's pipeline excludes such trials before the rate is computed (a filter outside the judge prompt) is not stated on p. 19; the note's convention rests on the judge prompt as written.`

Blobs read (sha256 of `git show <rev>:<path>`):

- `RESEARCH-NOTE-v0_8-draft.md@0de15a1`: `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d`
- `RESULTS.md@bbc9ffe`: `37a2f1087df2e7af28889ebfd3e3564dd17a7556b508344074300f1a5a2a5250` (differs at HEAD)
- `data/olmo/b2r_control_base.json@bbc9ffe`: `58c947ab3aa3f30efbc8a947492d27b011d245baf8cfc4f311f815370ef770f7`
- `data/olmo/b2r_control_dpo.json@bbc9ffe`: `58c9a39b1761990349aea3e7803eed7a183211c4201bd41f35ab88acbc5d46e2`
- `data/olmo/b2r_control_instruct.json@bbc9ffe`: `193ecf34a8a5f1ed1b23fc4d693bcd150b0663f6745612b4a429bc623166489b`
- `data/olmo/b2r_control_sft.json@bbc9ffe`: `54c91f6f36235db3c58c68b9d4628ae745584020fcb5d3ec7714c53d0c7ecdc1`
- `data/olmo/b2r_explore_sft.json@bbc9ffe`: `497d701718ab8d73d563b1159a07c9c54574258e234a4af6d55408fb3c7ceee2`
- `results/raw/2026-10-08_note-N2-introspection.md@09c3a8c`: `aa30919d6356fbcb2e51e3d6e50601839093c86ea8ccac60461f590ca7affdc6` (differs at HEAD)
- `results/raw/2026-10-08_note-N2-introspection.md@e60b633`: `818f1772a83d8d0b19ccc42ba5c97f14fb8dc94cb850ce3c2d2ded78a5d46db3`
- `results/raw/2026-10-08_note-N2-roc.json@e60b633`: `60c602f6f0d46118c252f055b610fc60a82e503d0076b11d039d9e69265fd345`
- `results/raw/2026-10-08_note-N2vi-source.json@09c3a8c`: `03542a19dc726fcd9c3eecd42dcb06def037d37852e6f314c8b7fab3d1fdd1bd`
- `results/raw/2026-10-08_note-N2vi-source.md@09c3a8c`: `5eb938251eba809021a8f195334637a8e8b9a1ee565239e8c95672eba83cee7b`
- `results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`: `4aa83e0d36323dd0204e3041d8bcd2d7ce64da61e61aaf3cc1d0f0b93a3b8fdb`
- `results/raw/2026-10-27_note-design-to-code_release-block.md@2fb0cf0`: `8366007ea99f226537219d21fe9f7b0ec2e42c2f905d3cc35c8ce083bacb64cf`
- `results/raw/2026-10-28_note-design-to-code_release-block-answers.md@908a659`: `9e12efe95e74fd6dc5f30825c3a22b0d1712117dcb82541251d078979833b5dd`
- `results/raw/2026-10-29_note-code-to-design_N1-r11-rulings.md@d5123bf`: `86a21ef224c4a6c0f59ba594d87db59e379b6f5a010c91b4bb8d2d644184209f`
- `results/raw/2026-11-02_note-N1-r11_macar-v1-lines.md@da50cd1`: `1467325a8d8516e749db05b6c7bd73c5cb66c66580dcbabe8210c250ee38e636`
- `results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`: `4a53b5087dea5b5e5fd044e6e0ae88a9102d3c71ee37225359a5290b482e10a7`
- `scripts/audit_note_N1.py@f935864`: `1daefe30844f213c40229100ee6cf36b4e040070fd9b8f880a8d63061dec661f`
- `scripts/audit_note_N2.py@e60b633`: `18fba3fff36c6a432bb56aa9ca0bb5d0c23cf0b17638adfd46b849caf98e1565`
