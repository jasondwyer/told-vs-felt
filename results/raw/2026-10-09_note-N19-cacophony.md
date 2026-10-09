# AUDIT-note-release v1.2 -- N19: companion-code sensitivity re-run (block :124-125)

- Code stamp: 2026-10-09 17:34:22 UTC (date -u equivalent); HEAD `961e90a5c8ac19079c815b19105e8353f88417a6`
- Block `AUDIT-note-release-v1_2.md` sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841`
- Script `scripts/audit_note_N19.py` sha256 `e1adafcad81c1578b0d2560fdbe9e0dd2ed576f43b22399d60d3724400786d69`; interpreter /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python (Python 3.12.9, numpy 2.5.1); run with `-I`
- Command: `cd <scratchpad>/n19/run && /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python -I /Users/jasondwyer/Documents/code/jspace-lab/scripts/audit_note_N19.py --ext <scratchpad>/n19/ext` (cwd outside the clone; the clone is passed by path)
- External repository: https://github.com/arvomm/cacophony-public-code, cloned with `git clone` into a new empty directory outside the repository; HEAD pinned at `b6ba87b55bd1184dd33f550bcd53875a6553494f` (refs/heads/main); pyproject version 2.6.0. The script asserts the pin by reading the clone's .git files (no git process).
- `notebooks/scoring.ipynb` sha256 `67f064f03160bb03a8b94c5153e76354e98e79afca343e82727e0d91cb6fde37`; its code cells carry execution counts 1..18 in order (one clean top-to-bottom run); kernel Python 3.13.15.
- Other files read from the clone (sha256): `dcm priors/Indicators Caco Nodes DCM priors.csv` `2c081311e02db976...`; `dcm priors/mapping.md` `fdc60376954d8795...`; `dcm_lab/score.py` `ccaeb50fb74a7138...`; `dcm_lab/truth.py` `18b4a9016b3da2ff...`; `dcm_lab/indicators.py` `e2479713d53dc558...`; `pyproject.toml` `8ebdabb548479156...`
- Note `RESEARCH-NOTE-v0_3-draft.md` sha256 `5a34309ffe402cdeb99d0c60635adac67e08db23d82fc496142c656777d14871` (asserted equal to the routed sha); section 8 = lines 140-149.

## 1. Method

The notebook's cell 1 imports matplotlib, pandas and scipy at top level (and `dcm_lab/indicators.py` imports pandas). This interpreter has numpy 2.5.1 and pandas 3.0.3; scipy and matplotlib are absent (checked with `importlib.util.find_spec` and `importlib.metadata`, which locate a package without importing it). Nothing was installed, so the notebook cannot run here as released. That is not the only reason for the port: even with all three present, running the notebook would import and execute the clone's own `dcm_lab` package, and this audit reads third-party code as data only. This script itself imports numpy and the standard library only. The notebook's code cells were read as JSON and reviewed before anything ran. No file of the clone was imported or executed. The scoring path the notebook uses (`dcm_lab/score.py`: `_sample_edge_logprobs`, `prior_predictive_score`, `overall_credence`, `hdi_from_samples`, `prior_C_marginals`, `prior_depth_distribution`, `format_score`; `dcm_lab/truth.py` constants and `make_prior_config`; the CSV loader of `dcm_lab/indicators.py`) is ported line for line into this script; pandas is used upstream only to read the CSV and to display a table, scipy only for a plot's density curve, matplotlib only for figures. The port is accepted only if it regenerates every printed output stored in the notebook exactly (section 2).

Review of the notebook's code cells (read as JSON before anything ran; Code read every cell, and this script re-scans them): cells matching network/process patterns (`requests|urllib|http|socket|subprocess|os\.system|Popen|!pip|%pip|wget|curl`): none. Cell 1 inserts the repository root (`..` of the working directory) at the front of `sys.path`, imports `dcm_lab`, and creates `../outputs/figures`; cells calling `savefig` (PNG writes there): [4, 8, 12, 14, 21, 22, 26, 29, 32]. Running the notebook as-is would execute the clone's package and write inside the clone; the port avoids both.

Released defaults (notebook cell 1 and `truth.py`): N_DRAWS = 5000, SEED = 0, HDI probability 0.89; generalised model (Condition 2B), alpha_C ~ Beta(8.0, 2.0), beta_C ~ Beta(2.0, 8.0); root pi ~ Beta(1,1); cell 31 scores the five illustrative systems with equal credences P(L*=i) = 1/5. Every condition below uses these defaults and the same seed, so all conditions share one set of 5000 prior draws (common random numbers) and differences between them are exact for that draw set.

## 2. Port validation against the notebook's stored outputs

| cell | stored stream chars | regenerated text equals stored text |
|---|---|---|
| 1 | 522 | yes |
| 10 | 1613 | yes |
| 12 | 86 | yes |
| 16 | 495 | yes |
| 18 | 3006 | yes |
| 20 | 10 | yes (prints only 'Computed.') |
| 25 | 641 | yes |
| 28 | 533 | yes |
| 31 | 515 | yes |

Cell 6's stored indicator table (j, level, name, alpha, beta as displayed): 37/37 rows match the CSV this script parsed. Port verdict: **PASS** -- every stored printed output is regenerated character for character, including cell 31's `LLM-optimist ... 0.394  [0.387, 0.400]`.

## 3. The indicators, as the notebook names them

| j | level | name (CSV `Name`, shown in notebook cell 6) | DCM node | support | demandingness | alpha (TPR) | beta (FPR) | LLM-optimist |
|---|---|---|---|---|---|---|---|---|
| 7 | 1 (Behavioural) | Coupling between reported states and subsequent behaviour | Coupling | moderate support | weakly undemanding | 0.91 | 0.7 | 1 |
| 14 | 2 (Computational functional) | Meta-cognition | Metacognition | strong support | weakly demanding | 0.93 | 0.3 | 1 |
| 21 | 3 (Intrinsic causal-structure functional) | Metacognition | (default fallback) | - | - | 0.73 | 0.1 | 0 |

- The vector is named `LLM-optimist` in cell 31. Cell 6's display truncates j=7's name to `Coupling between reported states and subsequen...`; the full name above is the CSV's.
- The notebook has two metacognition indicators: Level 2 `Meta-cognition` (j=14, the computational-level one) and Level 3 `Metacognition` (j=21, a default-fallback row). The optimist vector scores the Level 2 one present and the Level 3 one absent, so 'strike the metacognition indicator' acts on j=14; striking j=21 is a no-op (shown for completeness).
- Coupling's stated false-positive rate: CSV `prior beta` = 0.7 for j=7 (demandingness `weakly undemanding`); `dcm priors/mapping.md`:41 maps 'Weakly undemanding' to beta = 0.70; notebook cell 6 displays beta 0.70 on row 7. The model's beta is P(I = 1 | parent C1 = 0), the indicator's rate when the Level 1 node is off.

## 4. Results (released defaults; 'strike' = the indicator's 1 set to 0)

Aggregates are the notebook's `overall_credence` (sum_i P(L*=i) P(C_i|e)), mean over draws with the 89% HDI. **The block's 'Level 1-2-heavy weighting' is not defined in the block, the note, or the notebook**; the only non-equal credence vector in the notebook is cell 28's illustrative (0.3, 0.2, 0.1, 0.3, 0.1), which puts 0.5 on Levels 1-2 (and 0.3 on Level 4); it is shown as `cell-28 vector` for reference, not as the block's weighting. The column `L1-2 only` is the equal split (0.5, 0.5, 0, 0, 0). It is the midpoint of the weightings that put all their weight on Levels 1-2, not a bound on them: for w = (t, 1-t, 0, 0, 0) the aggregate is t x C1 + (1-t) x C2, so across those weightings it runs from C2 (all on Level 2) to C1 (all on Level 1); the range table after the bullets gives both ends per condition. Because the aggregate is linear in the credences, any other weighting w gives sum_i w_i x C_i from the row (the JSON carries 6+ decimals).

| condition | yes per level | C1 | C2 (computational) | C3 | C4 | C5 | equal credences [89% HDI] | cell-28 vector | L1-2 only |
|---|---|---|---|---|---|---|---|---|---|
| baseline: LLM-optimist at released defaults | [7, 5, 0, 0, 0] | 1.000 | 0.969 | 0.000 | 0.000 | 0.000 | 0.394 [0.387, 0.400] | 0.494 | 0.985 |
| strike_meta_L2: strike L2 'Meta-cognition' (j=14): set 1 -> 0 | [7, 4, 0, 0, 0] | 1.000 | 0.623 | 0.000 | 0.000 | 0.000 | 0.325 [0.261, 0.392] | 0.425 | 0.812 |
| strike_meta_L3: strike L3 'Metacognition' (j=21): already 0 in the vector | [7, 5, 0, 0, 0] | 1.000 | 0.969 | 0.000 | 0.000 | 0.000 | 0.394 [0.387, 0.400] | 0.494 | 0.985 |
| strike_coupling: strike L1 'Coupling between reported states and subsequent behaviour' (j=7): set 1 -> 0 | [6, 5, 0, 0, 0] | 1.000 | 0.969 | 0.000 | 0.000 | 0.000 | 0.394 [0.387, 0.400] | 0.494 | 0.985 |
| unscored_meta_L2: alternative reading: L2 'Meta-cognition' removed from the likelihood (unobserved) | [7, 5, 0, 0, 0] | 1.000 | 0.919 | 0.000 | 0.000 | 0.000 | 0.384 [0.365, 0.400] | 0.484 | 0.959 |
| unscored_coupling: alternative reading: L1 coupling removed from the likelihood (unobserved) | [7, 5, 0, 0, 0] | 1.000 | 0.969 | 0.000 | 0.000 | 0.000 | 0.394 [0.387, 0.400] | 0.494 | 0.985 |

- strike_meta_L2: C1 0.999982 -> 0.999906; C2 0.969212 -> 0.623261 (89% HDI [0.304, 0.961]); equal-credence aggregate 0.393843 -> 0.324637 (change -0.069206); cell-28 0.493841 -> 0.424628; L1-2 only 0.984597 -> 0.811584.
- strike_coupling: C1 0.999982 -> 0.999921; C2 0.969212 -> 0.969196 (89% HDI [0.937, 1.000]); equal-credence aggregate 0.393843 -> 0.393828 (change -0.000015); cell-28 0.493841 -> 0.493820; L1-2 only 0.984597 -> 0.984558.
- unscored_meta_L2: C1 0.999982 -> 0.999973; C2 0.969212 -> 0.919003 (89% HDI [0.827, 0.999]); equal-credence aggregate 0.393843 -> 0.383799 (change -0.010044); cell-28 0.493841 -> 0.483796; L1-2 only 0.984597 -> 0.959488.
- unscored_coupling: C1 0.999982 -> 0.999976; C2 0.969212 -> 0.969210 (89% HDI [0.937, 1.000]); equal-credence aggregate 0.393843 -> 0.393842 (change -0.000001); cell-28 0.493841 -> 0.493839; L1-2 only 0.984597 -> 0.984593.

Weightings on Levels 1-2 only, w = (t, 1-t, 0, 0, 0): the aggregate at both ends and at the midpoint, and the change from baseline at both ends (the change at any t lies between them):

| condition | all on Level 2 (t = 0; = C2) | midpoint (0.5, 0.5) | all on Level 1 (t = 1; = C1) | change vs baseline, all on Level 2 | change vs baseline, all on Level 1 |
|---|---|---|---|---|---|
| baseline | 0.969212 | 0.984597 | 0.999982 | +0.000000 | +0.000000 |
| strike_meta_L2 | 0.623261 | 0.811584 | 0.999906 | -0.345950 | -0.000075 |
| strike_meta_L3 | 0.969212 | 0.984597 | 0.999982 | +0.000000 | +0.000000 |
| strike_coupling | 0.969196 | 0.984558 | 0.999921 | -0.000016 | -0.000061 |
| unscored_meta_L2 | 0.919003 | 0.959488 | 0.999973 | -0.050209 | -0.000009 |
| unscored_coupling | 0.969210 | 0.984593 | 0.999976 | -0.000001 | -0.000005 |

Per-level evidence, log10 of P(e_level | C_i = 1) / P(e_level | C_i = 0) (theta-independent):

| condition | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|
| baseline | +4.344 | +1.764 | -5.569 | -3.870 | -5.614 |
| strike_meta_L2 | +4.344 | +0.273 | -5.569 | -3.870 | -5.614 |
| strike_coupling | +3.707 | +1.764 | -5.569 | -3.870 | -5.614 |

A strike multiplies its level's likelihood ratio by ((1-a)/(1-b)) / (a/b): coupling (a=0.91, b=0.7) 0.2308; Level 2 metacognition (a=0.93, b=0.3) 0.0323.

## 5. Diagnostic (post-hoc, computed-new): is the coupling strike inert because of its beta?

The coupling indicator's (alpha, beta) is replaced, with everything else at defaults, and the strike rerun:

| coupling (alpha, beta) | baseline C1 | struck C1 | baseline aggregate (equal) | struck aggregate (equal) |
|---|---|---|---|---|
| released (0.91, 0.7) | 0.999982 | 0.999921 | 0.393843 | 0.393828 |
| coupling_as_fallback_0.73_0.10 (0.73, 0.1) | 0.999997 | 0.999921 | 0.393847 | 0.393828 |
| coupling_as_metacognition_0.93_0.30 (0.93, 0.3) | 0.999992 | 0.999764 | 0.393846 | 0.393788 |

Why each counterfactual row's struck values are what they are. A struck indicator (e = 0) contributes (1 - alpha) to its level's likelihood when C1 = 1 and (1 - beta) when C1 = 0, and the posterior depends only on their ratio (the level's common factor cancels when the posterior is normalised). So two (alpha, beta) pairs with the same (1 - alpha)/(1 - beta) give the same struck posterior, whatever their unstruck values.

- coupling_as_fallback_0.73_0.10: (1 - alpha)/(1 - beta) = 0.27/0.90 = 0.3000, against 0.09/0.30 = 0.3000 as released -- the same ratio, so its struck row equals the released struck row (largest per-level difference 2.2e-16, aggregate difference 0.0e+00: floating-point rounding, not a copy). Its baseline differs (alpha/beta = 7.30 against 1.30 as released), so the strike here multiplies the Level 1 likelihood ratio by 0.0411, against 0.2308 as released (it divides the ratio by 24.3 instead of 4.3), and still leaves the aggregate at 0.394. The row is a real test of the diagnostic, not a duplicate.
- coupling_as_metacognition_0.93_0.30: (1 - alpha)/(1 - beta) = 0.07/0.70 = 0.1000, against 0.09/0.30 = 0.3000 as released; the strike multiplies the Level 1 likelihood ratio by 0.0323, against 0.2308 as released, and the struck aggregate is 0.393788.

## 6. Robustness (equal credences)

| condition | generalised Beta(1,1) | generalised Beta(2,2) | generalised Beta(6,2) | generalised Beta(2,6) | generalised Beta(0.5,0.5) [cell 7] | strict Beta(1,1) |
|---|---|---|---|---|---|---|
| baseline | 0.394 | 0.394 | 0.394 | 0.394 | 0.394 | 0.395 |
| strike_meta_L2 | 0.325 | 0.325 | 0.325 | 0.325 | 0.325 | 0.333 |
| strike_coupling | 0.394 | 0.394 | 0.394 | 0.394 | 0.394 | 0.395 |

- The four `generalised` Beta(a,b) columns are `truth.py`'s root-prior sweep. The `generalised Beta(0.5,0.5) [cell 7]` column is not in the sweep: notebook cell 7 (markdown) says the uniform Beta(1,1) was used but advises users to also try "Beta (1/2, 1/2)". Its means: baseline 0.393964 [89% HDI 0.386, 0.400]; strike_meta_L2 0.324613 [89% HDI 0.260, 0.394]; strike_coupling 0.393949 [89% HDI 0.386, 0.400].
- Monte Carlo spread, baseline, seeds 0..19 at N_DRAWS = 5000: equal-credence aggregate min 0.393637, max 0.394095.
- Monte Carlo spread, strike_meta_L2, seeds 0..19 at N_DRAWS = 5000: equal-credence aggregate min 0.323390, max 0.325617.
- Monte Carlo spread, strike_coupling, seeds 0..19 at N_DRAWS = 5000: equal-credence aggregate min 0.393621, max 0.394079.

## 7. Against the note's section 8 (lines 140-149)

| note claim | status | basis |
|---|---|---|
| 0.394 (LLM-optimist, equal level credences, released defaults) | reproduced | CONFIRMS. Notebook cell 31's stored output and this port both give 0.394 [89% HDI 0.387, 0.400] (mean 0.393843). Root priors (generalised): 0.394 at all four shapes of `truth.py`'s sweep and at cell 7's Beta(1/2,1/2); strict model Beta(1,1): 0.395; seeds 0..19: all round to 0.394 (0.393637 to 0.394095) |
| 0.70 (coupling indicator's false-positive rate; 'weakly undemanding') | reproduced | CONFIRMS. CSV row j=7 `prior beta` 0.7, demandingness `weakly undemanding`; mapping.md:41 (Weakly undemanding -> 0.70); cell 6 displays 0.70. The note's gloss (the model expects coupling reports in systems that are not conscious) matches mapping.md's reading of beta as background prevalence; in the network beta conditions on the Level 1 node C1 = 0 |
| 'Striking the behavioral coupling indicator ... moves nothing' (coupling set to 0) | computed-new | CONFIRMS. Equal-credence aggregate 0.393843 -> 0.393828 (|change| 1.54e-05; 0.394 -> 0.394); C1 0.999982 -> 0.999921 |
| '... because that indicator is scored as weakly undemanding (false-positive rate 0.70)' | computed-new | THE NOTE'S CLAUSE DOES NOT HOLD ON THIS VECTOR: the 0.70 is not why the strike moves nothing. Why: with the coupling indicator given a demanding false-positive rate instead (0.10, the fallback pair; 0.30, the Level 2 metacognition pair), the strike is still inert: struck aggregate coupling_as_fallback_0.73_0.10 0.393828; coupling_as_metacognition_0.93_0.30 0.393788, all 0.394 (section 5). The strike is inert because the vector's other Level 1 answers already put C1 at 0.999982 (Level 1 log10 likelihood ratio +4.344; +3.707 after the strike), so C1 is saturated whatever the indicator's beta. The 0.70 does make the indicator low-leverage in general (a strike multiplies the Level 1 likelihood ratio by 0.2308, against 0.0323 for Level 2 metacognition), but that is not what decides the result here. Status: the number in the clause (0.70) is reproduced in the row above; this row tests only the clause's 'because', by a diagnostic added after the results were seen, so under rule 11 it is computed-new (post-hoc: it flags, it does not adjudicate). Whether the row should read discrepant instead is the PI's call. Whoever carries this row must carry this sentence with the status |

- Metacognition strike: section 8 of the note (v0.3) withdraws the what-if and carries no number for it, so this run has nothing in section 8 to confirm or correct there (note line 29 still leans on it: see section 8 below, post-hoc). The block's figures are in section 4 for the record (computed-new): computational-level posterior C2 0.969 -> 0.623; aggregate 0.394 -> 0.325 under equal credences.
- Coupling strike: the note's verify brackets (lines 144, 210) describe the re-run as setting the coupling indicator to 0; this run does exactly that (section 4, `strike_coupling`).

Numerals in section 8, with whether this item bears on them:

- line 140: `8` -- section number; not a figure
- line 142: `32B` -- outside N19: not from the companion code (N1's ledger)
- line 142: `57.7%` -- outside N19: not from the companion code (N1's ledger)
- line 142: `79.7%` -- outside N19: not from the companion code (N1's ledger)
- line 142: `7B` -- outside N19: not from the companion code (N1's ledger)
- line 142: `72B` -- outside N19: not from the companion code (N1's ledger)
- line 144: `0.394` -- N19: reproduced (above)
- line 144: `4` -- a link or level label; not a figure
- line 144: `4` -- a link or level label; not a figure
- line 144: `5` -- a link or level label; not a figure
- line 144: `0.70` -- N19: reproduced (above)
- line 144: `0` -- N19: the bracket's 'set to 0' -- the procedure this run follows
- line 144: `0.394` -- N19: reproduced (above)
- line 144: `0.70` -- N19: reproduced (above)
- line 148: `4` -- a link or level label; not a figure

## 8. POST-HOC -- not in the block's procedure; flagged, not adopted: do the two indicators carry most of the optimist-sceptic gap? (note line 29)

Added after the results were seen, at the checker's flag. Under rule 11 (CLAUDE.md ledger: post-hoc analyses license pre-registrations, never verdicts) it supports a sentence for the design seat and the PI, not a verdict. Note line 29 says the note will show, on the framework's released model, that "the two indicators my data bear on carry most of the gap between their optimist and sceptic verdicts". The two indicators are Level 1 coupling (j=7, link 5) and Level 2 `Meta-cognition` (j=14, link 4). Both are 1 in `LLM-optimist` and 0 in `LLM-sceptic` (notebook cell 31); the two vectors differ on 9 of the 37 indicators. Share of the gap closed = (optimist - optimist with the indicator(s) struck) / (optimist - sceptic), at the released defaults on the same 5000 draws. The last column runs the other way: (sceptic with both set to 1 - sceptic) / (optimist - sceptic).

| weighting | optimist | sceptic | gap | optimist, both struck | share closed by both | metacognition (j=14) alone | coupling (j=7) alone | other way: sceptic + both |
|---|---|---|---|---|---|---|---|---|
| equal credences | 0.393843 | 0.005126 | 0.388717 | 0.324543 | **17.8%** | 17.8% | 0.004% | 3.7% |
| cell-28 credences (0.3, 0.2, 0.1, 0.3, 0.1) | 0.493841 | 0.007688 | 0.486153 | 0.424503 | **14.3%** | 14.2% | 0.0044% | 4.5% |
| Levels 1-2 only (0.5, 0.5, 0, 0, 0) | 0.984597 | 0.012807 | 0.971790 | 0.811348 | **17.8%** | 17.8% | 0.004% | 3.7% |

Maximum over weightings. The aggregate is linear in the credences, so the share is a ratio of two linear functions of the weighting and its maximum lies at a vertex: all weight on one level, or (with a floor on the gap) the point where an edge of the simplex meets the floor. Per level (all weight on that level):

| all weight on | optimist C_i | sceptic C_i | gap | closed by both | share |
|---|---|---|---|---|---|
| Level 1 | 0.999982 | 0.0256134 | 0.974 | 0.000387 | 0.04% |
| Level 2 | 0.969212 | 2.94499e-08 | 0.969 | 0.346 | 35.7% |
| Level 3 | 5.02052e-06 | 1.98095e-07 | 4.82e-06 | 2.48e-06 | 51.4% |
| Level 4 | 9.83691e-06 | 9.83631e-06 | 5.97e-10 | 3.09e-10 | 51.7% |
| Level 5 | 6.438e-06 | 6.438e-06 | 1.59e-13 | 1.31e-13 | 82.1% |

- Weightings on Levels 1-2 only: at most 35.7% (all weight on Level 2).
- Every weighting whose aggregate gap is at least 0.001 (the aggregates' reported precision; a smaller gap shows in no reported verdict): at most 35.8%, at w = (0, 0.001027, 0.999, 0, 0), where the gap is 0.001. That maximiser puts just enough weight on Level 2 to meet the floor and the rest where there is no gap; its share is Level 2's 35.7% moved by near-zero terms. The value depends on the floor: it rises towards the unrestricted ratio below as the floor goes to 0.
- Unrestricted: the largest ratio is 82.1%, with all weight on Level 5. At Levels 3-5 both verdicts are already near zero (optimist at most 9.8e-06, sceptic at most 9.8e-06) and the gap is at most 4.8e-06, so a ratio there divides one near-zero number by another. There is no gap there to carry.

**This contradicts note line 29 ("carry most of the gap between their optimist and sceptic verdicts"), reading 'most' as more than half.** Striking both indicators closes 17.8% of the gap under equal credences, 14.3% under the cell-28 credences and 17.8% under (0.5, 0.5, 0, 0, 0). With all weight on Level 2, the most favourable level that has a gap to close, it closes 35.7%; under any weighting with a gap of at least 0.001, at most 35.8%. Run the other way, adding both to the sceptic closes 3.7%. The coupling indicator alone closes 0.004% under equal credences. Section 8 of the note (line 144) already withdraws the metacognition strike, which supplies almost all of what the pair closes; so on the note's own terms line 29 has 0.004% behind it. The line has no numeral of its own.

This is a sentence for the design seat and the PI. It is not adopted, and N19 edits no note text.

## 9. Values-check (checker's findings on this raw, and their dispositions)

Changes at the values-check: wording, plus the rows, columns and sections listed below. No computation that produced an earlier figure was altered.

1. **HIGH (note line 29): APPLIED** as section 8, labelled post-hoc. Striking both indicators closes 17.8% of the gap under equal credences, 14.3% under cell-28 and 17.8% under Levels 1-2 only. The maximum is 35.8% (gap at least 0.001) or 35.7% (Levels 1-2 only), and coupling alone closes 0.004%. This raw's section 8 states plainly that this contradicts the line's 'carry most of the gap'. It is a sentence for the design seat and the PI, not adopted. One correction to the flag: the checker said N1's numeral matcher cannot catch line 29, since it has no numerals. But N1 final's note rows (`results/raw/2026-10-09_note-N1-claims-ledger-final.md`) already carry note:29 as row S1#145, matched on the word 'two', and N1's S1 span note (note:29 stale against section 8) calls the line stale. What N19 adds is the number.
2. **LOW-MEDIUM: APPLIED.** Section 4 no longer says (0.5, 0.5, 0, 0, 0) bounds the Levels 1-2 weightings. It now calls it the midpoint and adds a range table. Over those weightings the aggregate runs from 0.969212 to 0.999982 at baseline, from 0.623261 to 0.999906 after the metacognition strike, and from 0.969196 to 0.999921 after the coupling strike. The metacognition strike's change runs from -0.000075 (all on Level 1) to -0.345950 (all on Level 2).
3. **LOW: APPLIED.** Section 1 and the script's docstring no longer say 'numpy only'. The interpreter has numpy 2.5.1 and pandas 3.0.3; scipy and matplotlib are absent. The JSON records this under `interpreter_packages`. The port's justification is kept on two grounds: the absent packages are imported at top level by notebook cell 1, and running the notebook would execute the clone's `dcm_lab` package in any case.
4. **LOW, for the PI: APPLIED.** The 'because ... weakly undemanding' row keeps the status computed-new, because the diagnostic is post-hoc (rule 11). Its basis now opens by saying that the note's clause does not hold on this vector, and says why: C1 is saturated by the vector's other Level 1 answers, and a demanding beta is just as inert. The JSON row carries `note_clause_holds: false` and a `flag`, so a carrier that keeps only structured fields still sees it. Discrepant versus computed-new remains the PI's call.
5. **INFO: APPLIED.** Section 5 now explains why the (0.73, 0.10) row's struck values equal the released struck row's (0.393828; C1 0.999921): (1 - alpha)/(1 - beta) = 0.30 in both, and a struck indicator enters the posterior only through that ratio. The baselines differ, so there the strike divides the Level 1 likelihood ratio by 24.3, against 4.3 as released. The diagnostic stands.
6. **INFO: APPLIED.** Section 6 adds the Beta(1/2,1/2) root prior advised in notebook cell 7: baseline 0.393964; strike_meta_L2 0.324613; strike_coupling 0.393949. 0.394 holds.

The builder's own flagged findings: (B1) 'Level 1-2-heavy weighting' is undefined. Kept in section 4, with the wording correction of finding 2. (B2) The 'because' clause is the same row as finding 4, disposed of there. (B3) `README-NOTE.md` and N1's provisional ledger rows L159/L160 still say N19 is 'not run'. Those are not N19's files and are unchanged here; they are for N1 final once this raw is committed.

