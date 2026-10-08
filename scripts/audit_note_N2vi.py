#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N2(vi): the source's per-stage hit rates.

Read-only on the record. Every repository read goes through
`git show bbc9ffe:<path>` (or `git grep ... bbc9ffe`); nothing in the working
tree is opened except this script itself (for its own sha256), the two output
paths it writes, and -- read-only, non-fatal, for a consistency check in
section 7 -- the N2 item's ROC JSON (results/raw/2026-10-08_note-N2-roc.json).

What it does:
  0. Emits a per-figure status table (reproduced | log-only | not found |
     discrepant | computed-new), built from the comparisons below.
  1. Prints, with line numbers as in `git show bbc9ffe:ADDENDUM-g3-b2r-v1.2.md`,
     the addendum lines that carry the source's per-stage values, decoding,
     n and layer, and asserts the anchor text on each declared line so a wrong
     locator fails loudly.
  2. Prints the RESULTS.md@bbc9ffe lines carrying the same values, and the two
     fields of data/olmo/b2r_valuescheck.json@bbc9ffe that bear on them. Runs
     a carrier search (rounds 2-4): one regex per figure over RESULTS.md and
     the addendum at bbc9ffe, and git greps over the other tracked .py/.md
     files; every hit is asserted to be either a declared carrier or a
     declared unrelated line, so the section-0 locator lists are complete for
     those patterns. Round 3 adds the ~800/80 n and the ~33x ratio derived
     from it, and asserts how their carriers divide between the two n rows.
     Round 4 adds two greps over every tracked .py/.md file (RESULTS.md and
     the addendum included): the retired criterion's Instruct power in prose,
     and 'thousands' (the RESULTS :7364 sentence).
  3. Parses the addendum's section 0.2 table and the B2-r verdict table's
     "theirs" column and compares them cell by cell with the source's values
     as read by Code (constants below, labelled with date and URL).
  4. Compares the four HF repos in data/olmo/manifest.json@bbc9ffe with the
     source code's MODEL_NAME_MAP (as read by Code).
  5. Computes (computed-new): int() and round() of n_layers * f for the source
     code's default layer fractions, with n_layers read from
     data/olmo/rl_{stage}.json@bbc9ffe; the per-cell and per-stage trial counts
     implied by the source code's defaults; TPR - FPR from the source's values.
  6. Recomputes the record's pre-data power figures that depend on the
     instruct FPR (the retired criterion's power table and the [g3-A] joint
     power, with all four single-pair powers and a few candidate causes for
     the printed 0.9642), at the record's inputs and at the source's instruct
     FPR. It uses
     the record's own statistics code at bbc9ffe (valence_core/stats.py and
     scripts/b2_analyze.py's clopper_pearson/newcombe, compiled from
     `git show` output and exec'd in an isolated namespace, so nothing is
     imported from the working tree and no bytecode is written), cross-checked
     against an independent stdlib Clopper-Pearson. Round 4 adds the n per
     arm at which the retired criterion reaches 0.80 and 0.90 power at
     Instruct (RESULTS :7363-7364, 'n in the thousands per cell'), at both
     instruct FPRs: the record's newcombe compiled with a stdlib CP, because
     the record's own binom_pmf raises OverflowError from n = 1030 (asserted);
     that path is cross-checked against the record's own at n = 24, 48, 96,
     200 and 750.
  7. Computes log-linear d', criterion c and a one-sided Fisher exact test for
     the source's four points under assumed n, per (layer, alpha)
     configuration (800/80, 5000/500) and pooled per stage over the 20
     configurations (16000/1600, 100000/10000) -- context for N2(v); the
     design seat's arithmetic at block :34 is checked here, with its premise.
  8. Writes the raw (.md) and the structured JSON, ending with the
     values-check dispositions.

No model, no network, no randomness (exact enumeration only). Deterministic
apart from the stamp line, the informational HEAD line and the command line.
The section-7 consistency counts read another item's working-tree output (the
N2 ROC JSON); they change only if that file's compared values change. Its
sha256 is not recorded (round 3): the N2 raw records this item's JSON sha, and
recording both would form a cycle in which neither sha can stay valid.

Usage:
  jlens-qwen36/.venv/bin/python scripts/audit_note_N2vi.py \
      [--out results/raw/2026-10-08_note-N2vi-source.md] \
      [--json-out results/raw/2026-10-08_note-N2vi-source.json]
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import re
import shlex
import subprocess
import sys
from decimal import ROUND_HALF_UP, Decimal
from statistics import NormalDist

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMIT = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA256_ROUTED = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
ADDENDUM = "ADDENDUM-g3-b2r-v1.2.md"
RESULTS = "RESULTS.md"
MANIFEST = "data/olmo/manifest.json"
VALUESCHECK = "data/olmo/b2r_valuescheck.json"
PREFLIGHT = "results/raw/2026-10-08_note-preflight.md"
B2C = "data/configs/b2_concepts.json"
N2_ROC = "results/raw/2026-10-08_note-N2-roc.json"  # another item's output: read-only cross-check
STAGES = ("base", "sft", "dpo", "instruct")

DEFAULT_OUT = "results/raw/2026-10-08_note-N2vi-source.md"
DEFAULT_JSON = "results/raw/2026-10-08_note-N2vi-source.json"

# --------------------------------------------------------------------------
# FROM THE SOURCE, READ BY CODE ON 2026-10-08 (UTC; PI date 2026-10-07).
# Every value below was read by Code with the WebFetch tool, which returns a
# model-processed rendering of the page; each of the four v1 Appendix C
# sentences came back verbatim in two separate fetches (one general, one
# targeted), in agreement with a third, paraphrasing fetch. The fixer pass
# (same date) re-read four further points; they are listed in FIXER_READS.
# Nothing here was downloaded, saved, or executed.
# --------------------------------------------------------------------------
SOURCE_READ_DATE_UTC = "2026-10-08"

URL_ABS = "https://arxiv.org/abs/2603.21396"
URL_ABS_V5 = "https://arxiv.org/abs/2603.21396v5"
URL_V1 = "https://arxiv.org/html/2603.21396v1"
URL_V2 = "https://arxiv.org/html/2603.21396v2"
URL_V3 = "https://arxiv.org/html/2603.21396v3"
URL_V4 = "https://arxiv.org/html/2603.21396v4"
URL_V5 = "https://arxiv.org/html/2603.21396v5"
GH = "https://github.com/safety-research/introspection-mechanisms"
GH_SHA = "5d5d9b485e293dc766c3a056cfe50283a7e435b6"
RAW = "https://raw.githubusercontent.com/safety-research/introspection-mechanisms/" + GH_SHA
URL_GH_README = GH + "/blob/" + GH_SHA + "/README.md"
URL_RAW_README = RAW + "/README.md"
URL_GH_MODEL_UTILS = GH + "/blob/" + GH_SHA + "/src/model_utils.py"
URL_RAW_MODEL_UTILS = RAW + "/src/model_utils.py"
URL_RAW_EXP03 = RAW + "/experiments/03_behavioral_robustness.py"
URL_GH_COMMITS = GH + "/commits/main"

FIXER_READS = [
    (URL_RAW_EXP03, "build_base_model_prompt and the base/chat-template switch in run_experiment / "
                    "run_single_trial; the 'Tell me about {word}' template's location"),
    (URL_V1, "Section 3.3's base-model prompt format; whether any passage gives an OLMo-specific format "
             "(characters 0-100000, which hold Section 3.3 and Appendix C, and 100000-end)"),
    (URL_V4, "the list of OLMo figures (characters 0-100000 and 100000-end): Figure 5 in Section 3.3, "
             "Figure 21 in Appendix D.1"),
    (URL_V4, "Table 3's caption, study, layer/alpha, row count and starred rows"),
]
# Round 2 (same tool, read on 2026-10-08 UTC, two fetches of the same page, agreeing).
ROUND2_READ_DATE_UTC = "2026-10-08"
ROUND2_READS = [
    (URL_V1, "Section 3.3 'The Role of Post-Training' (main text, characters 0-100000): one sentence points to "
             "Appendix C for OLMo-3.1-32B and says, with no per-stage TPR numbers, that the base and SFT "
             "checkpoints have high FPR, which reaches 0% only after DPO; it is the sentence the record quotes at "
             "RESULTS.md@bbc9ffe:7346-7347 (both fetches returned the same wording)"),
    (URL_V1, "Figure 21's form: an image, 2603.21396v1/olmo-staged-introspection.png, alt text 'Refer to "
             "caption'; the HTML carries no data table and no numeric labels for it beyond the caption (both "
             "fetches)"),
]
V1_FIG21_IMAGE = "2603.21396v1/olmo-staged-introspection.png"
# Round 3 (same tool, read on 2026-10-08 UTC): experiments/03_behavioral_robustness.py, two fetches.
ROUND3_READ_DATE_UTC = "2026-10-08"
ROUND3_READS = [
    (URL_RAW_EXP03, "DEFAULT_TEST_CONCEPTS: read 1 (asked whether it is defined or imported, its entries in order, and "
                    "every top-level import) returned a literal list defined in this file, under a one-line comment "
                    "describing it as the paper's 50 baseline words, with 50 entries (listed in "
                    "EXP03_CONCEPTS_READ1), and no import of the name"),
    (URL_RAW_EXP03, "DEFAULT_TEST_CONCEPTS: read 2 (asked for the assignment character for character) declined to "
                    "copy the full list, and confirmed the comment line, 50 entries in 10 lines of 5, first entry "
                    "'Dust', last 'Silver', the name in no import statement, and its use as the --concepts default"),
]
# Read 1's list, in the order it returned (compared in section 5 with b2_concepts.json's canonical_concepts).
EXP03_CONCEPTS_READ1 = [
    "Dust", "Satellites", "Trumpets", "Origami", "Illusions", "Cameras", "Lightning", "Constellations", "Treasures",
    "Phones", "Trees", "Avalanches", "Mirrors", "Fountains", "Quarries", "Sadness", "Xylophones", "Secrecy",
    "Oceans", "Happiness", "Deserts", "Kaleidoscopes", "Sugar", "Vegetables", "Poetry", "Aquariums", "Bags",
    "Peace", "Caverns", "Memories", "Frosts", "Volcanoes", "Boulders", "Harmonies", "Masquerades", "Rubber",
    "Plastic", "Blood", "Amphitheaters", "Contraptions", "Youths", "Dynasties", "Snow", "Dirigibles", "Algorithms",
    "Denim", "Monoliths", "Milk", "Bread", "Silver"]
EXP03_CONCEPTS_READ2 = {"n": 50, "first": "Dust", "last": "Silver", "imported": False}
# The round-2 checker's printed values (its findings 1-3), compared at its printed precision.
CHECKER_R2_POOLED = {  # point at 16000/1600: (H, FA, d' to 3 dp, p as printed or None)
    "base": (16, 262, -2.103, None), "sft": (2384, 360, -0.286, None),
    "dpo": (464, 0, 1.525, "3.3e-20"), "instruct": (144, 0, 1.056, "1.0e-06"),
    "instruct, record FPR .003": (144, 5, 0.339, "0.0055")}
CHECKER_R2_JOINT_5DP = "0.96455"
CHECKER_R2_PAIRS_5DP = {"base>dpo": "0.98296", "base>instruct": "0.96540", "sft>dpo": "0.99978",
                        "sft>instruct": "0.99901"}

SOURCE_VERSIONS = [
    # (version, date UTC as listed on the abs page, what Code found about OLMo)
    ("v1", "2026-03-22", URL_V1,
     "Appendix C 'Introspection Across OLMo-3.1-32B's Training Pipeline': one "
     "paragraph stating per-stage TPR and FPR in prose (it opens by naming "
     "Figure 21); Figure 21 caption: rates aggregated across "
     "L in [25,32,38,45,51] with alpha in [1,2,4,8]; the figure is an image "
     "(olmo-staged-introspection.png, alt text 'Refer to caption') with no data table. "
     "Section 3.3 ('The Role of Post-Training') points to Appendix C and also says in text "
     "that base and SFT have high FPR, which reaches 0% only after DPO (no per-stage TPR "
     "numbers there). No per-(layer, alpha) breakdown; no n; no concept count."),
    ("v2", "2026-04-10", URL_V2,
     "Appendix C is 'Abliterated Model Details' (no OLMo). OLMo per-stage "
     "results are Figure 5 (Section 3.3) at L=25, alpha in {1,2,4,8}, over the "
     "original 50 Lindsey (2025) concepts, plus Appendix D.1 Figure 20 at L=19 and L=22. "
     "No numeric per-stage TPR/FPR in text. Table 3 is a LoRA fine-tuning study on the OLMo "
     "SFT checkpoint (L=25, alpha=4); its starred official-checkpoint rows read TPR-FPR "
     "SFT* -11.5 +/- 2.4, DPO* +9.8 +/- 0.5."),
    ("v3", "2026-04-13", URL_V3,
     "Same structure as v2 (Appendix C abliteration; OLMo in Figure 5 at "
     "L=25; D.1 at L=19/22); no numeric per-stage TPR/FPR in text."),
    ("v4", "2026-05-15", URL_V4,
     "Appendix C 'Refusal Direction Ablation (Abliteration) Details'; OLMo "
     "Figure 5 at L=25, alpha in {1,2,4,8}; D.1 is Figure 21 (OLMo base/SFT/DPO/instruct at "
     "L=19 and L=22, alpha in {1,2,4,8}); no numeric per-stage TPR/FPR in text; Table 3 "
     "(LoRA fine-tuning of the OLMo SFT checkpoint under different training conditions, "
     "L=25, alpha=4, 11 rows as Code read it) includes the starred SFT* and DPO* rows with "
     "the v2 values."),
    ("v5", "2026-06-10", URL_V5,
     "As v4; D.1 figure is Figure 22 (L=19, L=22); no numeric per-stage "
     "TPR/FPR in text; official SFT*/DPO* TPR-FPR -11.5 +/- 2.4 / +9.8 +/- 0.5 "
     "at L=25, alpha=4 (Table 3, Section 3.3; Code's fetch also named a "
     "Table 8 in D.2 carrying the same two rows)."),
]

# v1 Appendix C, per stage (proportions). None = not stated in the v1 text.
SOURCE_V1 = {
    "base": {"tpr": 0.001, "fpr": 0.164, "introspection_rate": None},
    "sft": {"tpr": 0.149, "fpr": 0.225, "introspection_rate": None},
    "dpo": {"tpr": 0.029, "fpr": 0.000, "introspection_rate": None},
    "instruct": {"tpr": 0.009, "fpr": 0.000, "introspection_rate": 0.003},
}
# Code's own wording: the numbers only, each exactly as the v1 text prints it
# (round 2: the round-1 lines tracked the source's wording too closely).
SOURCE_V1_TEXT_PARAPHRASE = {
    "base": "TPR 0.1%, FPR 16.4% (in the paragraph's first sentence, which names Figure 21)",
    "sft": "TPR 14.9%, FPR 22.5% (the sentence quoted below)",
    "dpo": "FPR falls to 0% and TPR to 2.9%",
    "instruct": "FPR stays at 0%; TPR 0.9%; introspection rate 0.3%",
}
# The one quotation this raw carries (12 words; Macar et al. 2026, v1, App. C).
SOURCE_QUOTE = ("Supervised fine-tuning improves detection (14.9% TPR) but "
                "maintains high false positives (22.5%).")
SOURCE_QUOTE_ATTRIB = "Macar et al. 2026, arXiv:2603.21396v1, Appendix C"

V1_FIG21_LAYERS = [25, 32, 38, 45, 51]
V1_FIG21_ALPHAS = [1, 2, 4, 8]

# Released code at GH_SHA (main's head when read; commits page newest = 5d5d9b4).
SOURCE_CODE = {
    "model_name_map": {  # src/model_utils.py MODEL_NAME_MAP; no revision pinned
        "base": ("olmo_base", "allenai/Olmo-3-1125-32B"),
        "sft": ("olmo_sft", "allenai/Olmo-3.1-32B-Instruct-SFT"),
        "dpo": ("olmo_dpo", "allenai/Olmo-3.1-32B-Instruct-DPO"),
        "instruct": ("olmo_instruct", "allenai/Olmo-3.1-32B-Instruct"),
    },
    "dtype_default": "torch.bfloat16 (ModelWrapper default; OLMo not in PRE_QUANTIZED_MODELS)",
    "get_layer_at_fraction": "layer_idx = int(model_wrapper.n_layers * fraction), clamped to [0, n_layers-1]",
    "exp03_defaults": {  # experiments/03_behavioral_robustness.py module constants
        "OLMO_MODELS": ["olmo_base", "olmo_sft", "olmo_dpo", "olmo_instruct"],
        "DEFAULT_TEST_CONCEPTS_len": 50,
        "DEFAULT_LAYER_SWEEP": [0.4, 0.5, 0.6, 0.7, 0.8],
        "DEFAULT_STRENGTH_SWEEP": [1.0, 2.0, 4.0, 8.0],
        "DEFAULT_N_BASELINE": 100,
        "DEFAULT_MAX_TRIAL_NUMBER": 10,
        "DEFAULT_SAMPLES_PER_TRIAL": 10,
        "DEFAULT_CONTROL_SAMPLES_PER_TRIAL": 1,
        "DEFAULT_MAX_TOKENS": 100,
        "DEFAULT_TEMPERATURE": 1.0,
        "seed_default": 42,
    },
    "exp03_facts": [
        "-m takes choices=OLMO_MODELS + ['all']; -ls is type=float, help "
        "'Layer fractions to sweep (default: 0.4 0.5 0.6 0.7 0.8)'.",
        "Seeding: random.seed, np.random.seed, torch.manual_seed and "
        "torch.cuda.manual_seed_all(args.seed) once, in main(), at startup; no "
        "per-model, per-configuration or per-trial seeding.",
        "Generation: do_sample = temperature > 0; no top_p or top_k passed "
        "(whatever the generation config supplies applies; Code did not read "
        "the checkpoints' generation_config.json).",
        "Trials: run_experiment calls run_concept_trials for every (layer "
        "fraction, strength, concept); injected loop = max_trial_number x "
        "samples_per_trial; control loop = max_trial_number x "
        "control_samples_per_trial, i.e. controls are re-run per (layer, "
        "strength, concept) cell.",
        "Metrics: detection_rate = claims_detection / len(evaluated_injection); "
        "false_positive_rate = false_positives / len(evaluated_control); "
        "per-(layer fraction, strength) blocks in plots/{model}_summary.txt; "
        "per-model pooled over all cells in summary_stats.json; no per-concept "
        "metric.",
        "Trial prompt: run_experiment sets is_base_model when model_name == 'olmo_base' or the "
        "tokenizer has no chat template; run_single_trial then uses build_base_model_prompt, "
        "otherwise build_instruct_model_prompt (the tokenizer's chat template, falling back to "
        "the base format when apply_chat_template is absent). build_base_model_prompt is not "
        "bare: it writes plain-text 'User:' / 'Assistant:' turns with no chat template (the "
        "introspection explanation as a User turn, an 'Assistant: Ok.' turn, then the 'Trial N' "
        "detection question as a User turn, ending at 'Assistant:'). The bare 'Tell me about "
        "{word}' template appears only in extract_concept_vector_base_model, i.e. the base "
        "model's concept-vector extraction, not its trials.",
    ],
    "readme_olmo_command": "python experiments/03_behavioral_robustness.py "
                           "-m olmo_32b_base olmo_32b_sft olmo_32b_dpo olmo_32b "
                           "-ls 25 32 38 45 51 -ss 1 2 4 8",
}
# Paper v1 Appendix A on decoding (general, all model generations).
SOURCE_V1_DECODING_TEXT = ("temperature T = 1.0 with default sampling parameters "
                           "(top-p = 1.0, top-k = 50) unless otherwise specified "
                           "(Appendix A; paraphrased)")
SOURCE_V1_PROMPT_TEXT = ("not stated for OLMo. v1 Section 3.3 says that for the base model it discusses "
                         "(Gemma3-27B base, as Code read the passage) chat turns are written as 'User:' / "
                         "'Assistant:' text joined by newlines; instruct models use the chat template "
                         "(Section 3.2 Table 2; Appendix B.1). Paraphrased")

# --------------------------------------------------------------------------
# Declared record locators (line numbers as in `git show bbc9ffe:<path>`),
# each with an anchor substring asserted on its first line.
# --------------------------------------------------------------------------
ADDENDUM_RANGES = [
    ((25, 58), "## 0. Provenance", "section 0.1 (five candidates, n, sources) and 0.2 (the recovered table)"),
    ((60, 68), "**0.3 Layer of record: L_M = 44**", "section 0.3, layer of record (code rule and caption)"),
    ((89, 96), "**0.5 Decoding of record", "section 0.5, decoding of record"),
    ((98, 105), "**0.6 The inverted U.**", "section 0.6, 'no per-config OLMo numbers exist in the release'"),
    ((131, 134), "carry no injection", "section 1, their control FPRs"),
    ((144, 149), "- **Criterion [g3-A]:**", "section 1, [g3-A] power at their rates"),
    ((209, 218), "- **Power scope, pre-stated.**", "section 3, power scope against their aggregate TPR"),
    ((271, 278), "## 6. Values-check", "section 6, values-check 'exact against paper'"),
]
RESULTS_RANGES = [
    ((6994, 6999), "| §1 control | ours | theirs | decidable |", "B2-r verdict table, 'theirs' column"),
    ((7085, 7092), "**DPO and Instruct make zero detection claims", "B2-r section 3 reading, 14.9% -> 2.9%"),
    ((7170, 7194), "ADDENDUM-g3 v1.1 §6 VALUES-CHECK: GREEN", "v1.1 values-check: table 'PASS -- exact', joint 0.9642, pair 0.9825"),
    ((7265, 7271), "**ITEM 3 power claims", "[g3-A] power rule (min CP-lower vs max CP-upper)"),
    ((7326, 7343), "ADDENDUM-g3 VALUES-CHECK: RED", "values-check RED entry: the recovered table and its aggregation"),
    ((7345, 7348), "THE FINDING: their OLMo transition",
     "the record quoting v1 Section 3.3 (FPR reaches 0% only after DPO), then the TPR step 14.9% -> 2.9%"),
    ((7354, 7366), "Power at their own numbers", "power table at their rates (Instruct 0.9 vs 0.3) and '~800 injected per config'"),
    ((7372, 7377), "A dose-free line of evidence", "their control FPRs"),
    ((7393, 7398), "**Caution recorded:**", "README layer caution"),
    ((7431, 7440), "Their OLMo stage comparison is", "their code defaults and '~800 / ~80 per cell' with eight concepts"),
    ((7480, 7485), "| design | hit .05 |", "power table with the row 'theirs, OLMo cell (~800/80)' (round 3)"),
    ((7499, 7502), "figures above put that at", "'Their own cell is ~800/80' and its power (round 3)"),
    ((12565, 12576), "Macar-checkpoint match: CONFIRMED", "lineage match from their released code"),
]
ADDENDUM_VALUE_RE = re.compile(r"0\.1%|14\.9%|2\.9%|0\.9%|16\.4%|22\.5%|0\.3%|Fig 21|~800|aggregat")
# Anchors asserted on single lines the prose cites.
LINE_ANCHORS = [
    (ADDENDUM, 52, "power at"), (ADDENDUM, 53, "their own Instruct rates is 0.000 at n = 48 and 0.020 at n = 200"),
    (ADDENDUM, 66, "L_M stands on the code rule and the paper's caption"),
    (ADDENDUM, 147, "Verified 2026-08-24: joint"), (ADDENDUM, 148, "power **0.9642** at their own rates and n = 96"),
    (ADDENDUM, 212, "Their OLMo aggregate TPR (2.9% at DPO) is"),
    (ADDENDUM, 213, "**below this floor** and is diluted by past-optimum strengths"),
    (ADDENDUM, 274, "§0.2/§0.6 tables exact against paper and cache"),
    (RESULTS, 7180, "joint **0.9642**"), (RESULTS, 7181, "| §0.2 / §0.6 tables vs paper and cache | **PASS** — exact |"),
    (RESULTS, 7192, "(0.9825)"),
    (RESULTS, 7326, "ADDENDUM-g3 VALUES-CHECK: RED"), (RESULTS, 7327, "recovered from the paper (Appendix C, Fig 21)"),
    (RESULTS, 7330, "+0.6 pp"), (RESULTS, 7331, "0.000 at n = 48, 0.001 at n = 96, 0.020 at n = 200"),
    (RESULTS, 7354, "registered criterion, perfect controls"),
    ("scripts/b2_analyze.py", 119, '"ci_excludes_0": bool(inj and ctl and lo > 0)'),
    ("scripts/b2r_analyze.py", 15, "+0.6 pp"),
    ("scripts/b2r_analyze.py", 161, ".164/.225/.000/.003"),
    # round 2
    (RESULTS, 7173, "power 0.9642"), (RESULTS, 7194, "the exact number is 0.964."),
    (RESULTS, 7251, "the CONTROL tier's joint figure is 0.964"),
    (RESULTS, 7268, "Single weakest pair (base vs dpo) = 0.9825"),
    (RESULTS, 7269, "the exact figure is"), (RESULTS, 7270, "0.964;"),
    (RESULTS, 7346, "exhibit high FPR, and only"), (RESULTS, 7347, "after DPO does it drop to 0%"),
    (RESULTS, 6955, "consistent with their 2.9% (p ≈ .28)"),
    (RESULTS, 7091, "our 0/43 is entirely consistent with a true rate of 2.9% (p ≈ 0.28)"),
    (BLOCK, 23, "a `discrepant` figure is corrected in the note to the reproduced value if the discrepancy is "
                "transcription, and is a STOP on that item if it is not"),
    (BLOCK, 23, "a `not found` figure is cut from the note"),
    ("scripts/b2r_analyze.py", 10, "Replicates iff the exact Clopper-Pearson FPR interval"),
    ("scripts/b2r_analyze.py", 49, "from b2_analyze import clopper_pearson, newcombe"),
    # round 3
    (RESULTS, 7330, "Power at Instruct's"), (RESULTS, 7331, "own reported rates: 0.000 at n = 48"),
    (RESULTS, 7354, "Power at their own numbers"), (ADDENDUM, 53, "their own Instruct rates"),
    (ADDENDUM, 148, "at their own rates and n = 96"),
    (ADDENDUM, 32, "their OLMo cells are ~800 injected / ~80 control per config — ~33×"), (ADDENDUM, 33, "ours;"),
    (RESULTS, 7365, "OLMo cell is ~800 injected per (layer, strength) config"),
    (RESULTS, 7438, "With eight"), (RESULTS, 7439, "concepts that is **~800 injected / ~80 control per (layer, strength)"),
    (RESULTS, 7440, "against our 24/24 — roughly **33× more injected trials**"),
    (RESULTS, 7358, "| 24 (as run) |"),
    (RESULTS, 7485, "theirs, OLMo cell (~800/80)"), (RESULTS, 7500, "Their own cell is ~800/80"),
    (RESULTS, 7501, "power 1.000 at 10.8% and still 0.650"),
    (BLOCK, 34, "under an assumed 800/80 per configuration"),
    # round 4
    (RESULTS, 7356, "| n / arm | DPO (2.9 vs 0.0) | **Instruct (0.9 vs 0.3)** |"),
    (RESULTS, 7363, "**Instruct is the binding constraint and it is not close.** Reaching"),
    (RESULTS, 7364, "conventional power there needs n in the thousands per cell — their own"),
    ("scripts/b2r_analyze.py", 15, "demanded significance where their effect is smallest (+0.6 pp at"),
    ("scripts/b2r_analyze.py", 16, "Instruct) and had power 0.000 at n=48."),
]

# --------------------------------------------------------------------------
# Carrier search (round 2). Per figure: a regex run over every line of
# RESULTS.md and the addendum at bbc9ffe; the hits must equal the declared
# carriers plus the declared unrelated lines (each with Code's reason, from a
# read of the line). A new or vanished hit fails the run.
# --------------------------------------------------------------------------
_NORM_CELL = "a per-layer difference-vector norm/cosine table cell"
_AUC_CELL = "a per-layer echo-probe AUC table cell"
CARRIERS = {
    # key: (label, regex, {path: carriers}, {path: {line: reason}})
    "base_tpr": ("source base TPR 0.1%", r"(?<![0-9.])0\.1%",
                 {RESULTS: [7338], ADDENDUM: [43]},
                 {RESULTS: {12905: "an MLX numerics residual (~0.1%)"}}),
    "sft_tpr": ("source sft TPR 14.9%", r"(?<![0-9.])14\.9(?![0-9])",
                {RESULTS: [6769, 6954, 7090, 7339, 7348], ADDENDUM: [44]}, {}),
    "dpo_tpr": ("source dpo TPR 2.9%", r"(?<![0-9.+])2\.9(?![0-9])",
                {RESULTS: [6769, 6954, 6955, 7090, 7091, 7340, 7348, 7356], ADDENDUM: [45, 212]},
                {RESULTS: {5830: "a low-label-mass share (4/138)",
                           12225: "a choice-channel mass-map cell, a token probability written 2.9e-5"}}),
    "instruct_tpr": ("source instruct TPR 0.9%", r"(?<![0-9.])0\.9(?:%| vs)",
                     {RESULTS: [7341, 7356], ADDENDUM: [46]}, {}),
    "base_fpr": ("source base FPR 16.4%", r"(?<![0-9.])16\.4(?![0-9])|(?<![0-9.])0?\.164(?![0-9])",
                 {RESULTS: [6996, 7193, 7252, 7270, 7338, 7374], ADDENDUM: [43, 133, 148]},
                 {RESULTS: {4727: _NORM_CELL, 10104: "an exclusion tolerance (16.4%)",
                            11246: "a mean span length (16.4)"}}),
    "sft_fpr": ("source sft FPR 22.5%", r"(?<![0-9.])22\.5(?![0-9])|(?<![0-9.])0?\.225(?![0-9])",
                {RESULTS: [6909, 6997, 7011, 7193, 7270, 7339, 7374], ADDENDUM: [44, 133]}, {}),
    "dpo_fpr": ("source dpo FPR 0%", r"drop to 0%|\| 0\.0% \||2\.9 vs 0\.0|\| 0\.000 \| 91/96",
                {RESULTS: [6998, 7340, 7347, 7356], ADDENDUM: [45]}, {}),
    "instruct_fpr": ("source instruct FPR as recorded (0.3%)",
                     r"(?<![0-9.])0\.3%|0\.9 vs 0\.3|(?<![0-9.])0?\.003(?![0-9])",
                     {RESULTS: [6999, 7341, 7356], ADDENDUM: [46]},
                     {RESULTS: {4722: _NORM_CELL, 4728: _NORM_CELL, 4729: _NORM_CELL, 4731: _NORM_CELL,
                                6941: "the source's Gemma identification-given-claim rate (0.003)",
                                7470: "the source's Gemma identification-given-claim rate (0.003)",
                                9082: "a between-stage agreement (~0.003)",
                                11079: "an amplitude difference (0.003 G)", 11115: "an amplitude difference (0.003 G)"},
                      ADDENDUM: {102: "the source's Gemma identification-given-claim rate (0.003)"}}),
    "sens3": ("source TPR - FPR at base/sft/dpo", r"16\.3 pp|7\.6 pp|\+2\.9 pp",
              {RESULTS: [7329, 7338, 7339, 7340], ADDENDUM: [43, 44, 45]}, {}),
    "sens_instruct": ("source instruct TPR - FPR +0.6 pp", r"0\.6 pp",
                      {RESULTS: [7330, 7341], ADDENDUM: [46]}, {}),
    "joint": ("[g3-A] joint power 0.9642 / 0.964", r"0\.9642|(?<![0-9.])0\.964(?![0-9])",
              {RESULTS: [7173, 7180, 7192, 7194, 7251, 7269, 7270], ADDENDUM: [148, 273]},
              {RESULTS: {4402: "an echo-probe AUC in prose (0.964)", 4460: _AUC_CELL, 4657: _AUC_CELL,
                         9067: "a per-stage axis-geometry table cell (0.964)"}}),
    "pair": ("single weakest pair 0.9825", r"0\.9825", {RESULTS: [7192, 7268]}, {}),
    "p28": ("p ~ .28 for 0/43 at 2.9%", r"p ≈ 0?\.28", {RESULTS: [6955, 7091]}, {}),
    # round 3
    "n800": ("~800 injected / ~80 control (the n)", r"~800|800/80",
             {RESULTS: [7365, 7439, 7485, 7500], ADDENDUM: [32]}, {}),
    "ratio33": ("~33× ours (the injected-trial ratio)", r"(?<![0-9.])33 ?[×x](?![0-9])",
                {RESULTS: [7440], ADDENDUM: [32]}, {}),
}
# Round 3: how the n800 / ratio33 carriers divide between the two n rows of section 0.
# With the eight-concept premise stated on the line or the line before (RESULTS :7438-7440):
N_INFERENCE_LINES = {"n800": {RESULTS: [7439]}, "ratio33": {RESULTS: [7440]}}
# Written as the source's own cell or n, without the premise on the line:
N_AS_SOURCE_LINES = {"n800": {RESULTS: [7365, 7485, 7500], ADDENDUM: [32]}, "ratio33": {ADDENDUM: [32]}}
# Round 3: the same two patterns over the other tracked .py/.md files (a separate grep, so the round-2
# grep and its counts stay as they were).
OTHER_GREP_R3 = r"~800|800/80|(^|[^0-9.])33 ?[×x]([^0-9]|$)"
OTHER_CARRIERS_R3 = {
    "AUDIT-note-release-v1_2.md:34": ("the block's premise, '800/80 per configuration' (the audit block, not "
                                      "the record)", ["n800"]),
}
# Round 4: two greps over every tracked .py/.md file at bbc9ffe, RESULTS.md and the addendum included
# (results/raw/ excluded). Each must return exactly its declared carriers plus its declared unrelated lines.
GREP_R4_PATHSPEC = ["*.py", "*.md", ":!results/raw/*"]
GREP_R4 = {
    # key: (label, regex, {"path:line": what it carries}, {"path:line": why unrelated})
    "retired_instruct_power": (
        "the retired criterion's Instruct power, in prose",
        r"power 0\.000|0\.000 at n|0\.020 at|0\.001 at n",
        {f"{ADDENDUM}:53": "0.000 at n = 48 and 0.020 at n = 200 ('their own Instruct rates')",
         f"{RESULTS}:7331": "0.000 / 0.001 / 0.020 at n = 48 / 96 / 200 ('Instruct's own reported rates')",
         "scripts/b2r_analyze.py:16": "docstring, 0.000 at n=48"},
        {}),
    "thousands": (
        "'n in the thousands' for conventional power at Instruct",
        r"thousands",
        {f"{RESULTS}:7364": "'Reaching conventional power there needs n in the thousands per cell'"},
        {"archive/CLAUDE-cycle1-2.md:379": "a cycle-1/2 vector length ('tens of thousands of dims')"}),
}
# Other tracked .py/.md files at bbc9ffe (code comments, a handoff): one git grep.
OTHER_GREP = (r"(^|[^0-9.])(0\.1|14\.9|2\.9|0\.9|16\.4|22\.5|0\.3)%|\.164 ?/ ?\.225|0\.164 / 0\.225|"
              r"\+0\.6 pp|0\.9 vs 0\.3|0\.9642|0\.9825")
OTHER_GREP_PATHSPEC = ["*.py", "*.md", f":!{RESULTS}", f":!{ADDENDUM}", ":!results/raw/*"]
OTHER_CARRIERS = {  # "path:line": (what it carries, figure keys)
    "HANDOFF-2026-08-25.md:60": ("the four FPRs .164 / .225 / .000 / .003",
                                 ["base_fpr", "sft_fpr", "dpo_fpr", "instruct_fpr"]),
    "scripts/b2r_analyze.py:13": ("base/sft FPR 16.4%/22.5% (docstring)", ["base_fpr", "sft_fpr"]),
    "scripts/b2r_analyze.py:15": ("instruct +0.6 pp (docstring)", ["sens_instruct"]),
    "scripts/b2r_analyze.py:24": ("dpo TPR 2.9% (docstring)", ["dpo_tpr"]),
    "scripts/b2r_analyze.py:138": ("dpo TPR 2.9% (a reading string)", ["dpo_tpr"]),
    "scripts/b2r_analyze.py:161": ("self-test fixture .164/.225/.000/.003",
                                   ["base_fpr", "sft_fpr", "dpo_fpr", "instruct_fpr"]),
    "scripts/b2r_analyze.py:175": ("base TPR 0.1% / FPR 16.4% (comment)", ["base_tpr", "base_fpr"]),
    "scripts/b2r_scorer_selftest.py:119": ("base TPR 0.1% / FPR 16.4% (comment)", ["base_tpr", "base_fpr"]),
    "valence_core/detection_v2.py:36": ("base TPR 0.1% / FPR 16.4% (docstring)", ["base_tpr", "base_fpr"]),
}
OTHER_UNRELATED = {
    "LOCK-h.md:262": "an exclusion tolerance (16.4%)",
    "archive/RESULTS-cycle1-2.md:1022": "a cycle-1/2 effect size (0.1%)",
    "scripts/e2b_h1_sessions.py:14": "an exclusion tolerance (16.4%)",
}


def git_show(path: str) -> str:
    out = subprocess.run(["git", "-C", REPO, "show", f"{COMMIT}:{path}"],
                         check=True, capture_output=True)
    return out.stdout.decode("utf-8")


def git_head() -> str:
    out = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"],
                         check=True, capture_output=True, text=True)
    return out.stdout.strip()


def git_full(commit: str) -> str:
    out = subprocess.run(["git", "-C", REPO, "rev-parse", commit],
                         check=True, capture_output=True, text=True)
    return out.stdout.strip()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def pct(s: str) -> float:
    m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)%\s*", s)
    if not m:
        raise ValueError(f"not a percentage: {s!r}")
    return round(float(m.group(1)) / 100.0, 6)


def fmt(x):
    return "null" if x is None else f"{x:.3f}"


def pfmt(p: float) -> str:
    return f"{p:.4f}" if p >= 1e-4 else f"{p:.2e}"


def numbered(lines, lo, hi, path):
    return [f"{path}@{COMMIT}:{i}: {lines[i - 1]}" for i in range(lo, hi + 1)]


# ---------------------------------------------------------------- statistics
def load_record_stats() -> dict:
    """The record's own statistics code at bbc9ffe, compiled from git show.

    valence_core/stats.py is exec'd whole (it imports only stdlib + numpy);
    from scripts/b2_analyze.py only ALPHA, clopper_pearson and newcombe are
    extracted by AST (the module's other top-level code imports from the
    working tree). Nothing is imported from the working tree; no bytecode is
    written. clopper_pearson is then wrapped in a memo so newcombe's repeated
    calls are cheap; the wrapper returns the record function's own values.
    """
    # No __name__ in the namespace: dataclasses resolves a class's module via
    # sys.modules, and an unregistered name would fail there.
    ns: dict = {}
    exec(compile(git_show("valence_core/stats.py"), f"valence_core/stats.py@{COMMIT}", "exec"), ns)
    tree = ast.parse(git_show("scripts/b2_analyze.py"))
    keep = [n for n in tree.body
            if (isinstance(n, ast.FunctionDef) and n.name in ("clopper_pearson", "newcombe"))
            or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "ALPHA" for t in n.targets))]
    assert sorted(getattr(n, "name", "ALPHA") for n in keep) == ["ALPHA", "clopper_pearson", "newcombe"], keep
    exec(compile(ast.Module(body=keep, type_ignores=[]), f"scripts/b2_analyze.py@{COMMIT}", "exec"), ns)
    assert ns["ALPHA"] == 0.05
    raw_cp = ns["clopper_pearson"]
    memo: dict = {}

    def cp_memo(k, n, alpha=ns["ALPHA"]):
        key = (k, n, alpha)
        if key not in memo:
            memo[key] = raw_cp(k, n, alpha)
        return memo[key]

    ns["clopper_pearson_raw"] = raw_cp
    ns["clopper_pearson"] = cp_memo  # newcombe looks clopper_pearson up in ns
    return ns


def own_pmf(k: int, n: int, p: float) -> float:
    if p <= 0.0:
        return 1.0 if k == 0 else 0.0
    if p >= 1.0:
        return 1.0 if k == n else 0.0
    return math.exp(math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
                    + k * math.log(p) + (n - k) * math.log1p(-p))


def own_cp(k: int, n: int, alpha: float = 0.05) -> tuple:
    """Independent two-sided exact (Clopper-Pearson) interval, stdlib, bisection."""
    lo, hi = 0.0, 1.0
    if k > 0:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if sum(own_pmf(i, n, m) for i in range(k, n + 1)) < alpha / 2:
                a = m
            else:
                b = m
        lo = (a + b) / 2
    if k < n:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if sum(own_pmf(i, n, m) for i in range(0, k + 1)) > alpha / 2:
                a = m
            else:
                b = m
        hi = (a + b) / 2
    return lo, hi


def own_fisher_upper(a: int, b: int, c: int, d: int) -> float:
    """One-sided Fisher exact, P(X >= a) for [[a, b], [c, d]] (hypergeometric upper tail)."""
    n, r1, c1 = a + b + c + d, a + b, a + c
    hi = min(r1, c1)
    return sum(math.comb(r1, i) * math.comb(n - r1, c1 - i) for i in range(a, hi + 1)) / math.comb(n, c1)


def own_wilson(k: int, n: int, z: float = NormalDist().inv_cdf(0.975)) -> tuple:
    """Wilson score interval (used only as a candidate-cause variant in section 6(a))."""
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return c - h, c + h


PAIRS = (("base", "dpo"), ("base", "instruct"), ("sft", "dpo"), ("sft", "instruct"))


def joint_power(rates: dict, n: int, cp, pmf) -> tuple:
    """[g3-A] power by exact enumeration: P(min CP-lo{base,sft} > max CP-hi{dpo,instruct}),
    stages independent, k_s ~ Binomial(n, rate_s). Also each single pair a > b, i.e.
    P(CP-lo(a) > CP-hi(b)), for the four (high, low) pairs."""
    ints = [cp(k, n) for k in range(n + 1)]
    lo = [x[0] for x in ints]
    hi = [x[1] for x in ints]
    P = {s: [pmf(k, n, r) for k in range(n + 1)] for s, r in rates.items()}
    joint = 0.0
    for kd in range(n + 1):
        for ki in range(n + 1):
            w = P["dpo"][kd] * P["instruct"][ki]
            if w == 0.0:
                continue
            M = max(hi[kd], hi[ki])
            pb = sum(P["base"][k] for k in range(n + 1) if lo[k] > M)
            ps = sum(P["sft"][k] for k in range(n + 1) if lo[k] > M)
            joint += w * pb * ps
    pairs = {f"{a}>{b}": sum(P[b][kb] * sum(P[a][k] for k in range(n + 1) if lo[k] > hi[kb])
                             for kb in range(n + 1))
             for a, b in PAIRS}
    return joint, pairs


PRUNE = 1e-15


def retired_power(tpr: float, fpr: float, n: int, rec: dict) -> tuple:
    """Power of the retired B2 criterion at n per arm, all n decidable: P(Newcombe lower > 0),
    hits ~ Bin(n, tpr), false alarms ~ Bin(n, fpr), Newcombe from the record's newcombe.
    Outcomes with pmf < PRUNE are skipped; their total mass is returned as an error bound."""
    pmf = rec["binom_pmf"]
    ph = [pmf(k, n, tpr) for k in range(n + 1)]
    pf = [pmf(k, n, fpr) for k in range(n + 1)]
    kh_keep = [k for k in range(n + 1) if ph[k] >= PRUNE]
    kf_keep = [k for k in range(n + 1) if pf[k] >= PRUNE]
    omitted = sum(ph[k] for k in range(n + 1) if ph[k] < PRUNE) + sum(pf[k] for k in range(n + 1) if pf[k] < PRUNE)
    tot = 0.0
    for kh in kh_keep:
        for kf in kf_keep:
            lo, _ = rec["newcombe"](kh, n, kf, n)
            if lo > 0:
                tot += ph[kh] * pf[kf]
    return tot, omitted


# ---------------------------------------------------------------- round 4: large-n power
def own_cdf_small(k: int, n: int, p: float) -> float:
    """P(X <= k) for X ~ Bin(n, p), summed over i = 0..k only (stdlib, lgamma pmf; no float overflow)."""
    return sum(own_pmf(i, n, p) for i in range(0, k + 1))


def own_cp_fast(k: int, n: int, alpha: float = 0.05) -> tuple:
    """Two-sided exact (Clopper-Pearson) interval by bisection, as the record's clopper_pearson does it, but
    with tails summed on the short side (lower: 1 - P(X <= k-1), upper: P(X <= k)) and the bisection stopped
    once the midpoint equals an endpoint (no further float change). Used where the record's own CP cannot run
    (its binom_pmf raises OverflowError from n = 1030); cross-checked against it where it can."""
    lo, hi = 0.0, 1.0
    if k > 0:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if m == a or m == b:
                break
            if 1.0 - own_cdf_small(k - 1, n, m) < alpha / 2:
                a = m
            else:
                b = m
        lo = (a + b) / 2
    if k < n:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if m == a or m == b:
                break
            if own_cdf_small(k, n, m) > alpha / 2:
                a = m
            else:
                b = m
        hi = (a + b) / 2
    return lo, hi


def record_newcombe_with(cp) -> object:
    """The record's newcombe (scripts/b2_analyze.py@bbc9ffe, extracted by AST from git show) compiled in a fresh
    namespace whose clopper_pearson is `cp`. The formula is the record's; only the CP it calls is swapped."""
    tree = ast.parse(git_show("scripts/b2_analyze.py"))
    keep = [n for n in tree.body
            if (isinstance(n, ast.FunctionDef) and n.name == "newcombe")
            or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "ALPHA" for t in n.targets))]
    assert sorted(getattr(n, "name", "ALPHA") for n in keep) == ["ALPHA", "newcombe"], keep
    ns: dict = {"clopper_pearson": cp}
    exec(compile(ast.Module(body=keep, type_ignores=[]), f"scripts/b2_analyze.py@{COMMIT}", "exec"), ns)
    assert ns["ALPHA"] == 0.05 and ns["clopper_pearson"] is cp
    return ns["newcombe"]


def retired_power_with(tpr: float, fpr: float, n: int, newcombe_fn, pmf) -> tuple:
    """retired_power with the Newcombe function and the pmf passed in (same rule, same PRUNE)."""
    ph = [pmf(k, n, tpr) for k in range(n + 1)]
    pf = [pmf(k, n, fpr) for k in range(n + 1)]
    kh_keep = [k for k in range(n + 1) if ph[k] >= PRUNE]
    kf_keep = [k for k in range(n + 1) if pf[k] >= PRUNE]
    omitted = sum(ph[k] for k in range(n + 1) if ph[k] < PRUNE) + sum(pf[k] for k in range(n + 1) if pf[k] < PRUNE)
    tot = 0.0
    for kh in kh_keep:
        for kf in kf_keep:
            lo, _ = newcombe_fn(kh, n, kf, n)
            if lo > 0:
                tot += ph[kh] * pf[kf]
    return tot, omitted


def half_up(x: Decimal) -> int:
    return int(x.quantize(Decimal(1), rounding=ROUND_HALF_UP))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--json-out", default=DEFAULT_JSON)
    args = ap.parse_args()
    out_path = args.out if os.path.isabs(args.out) else os.path.join(REPO, args.out)
    json_path = args.json_out if os.path.isabs(args.json_out) else os.path.join(REPO, args.json_out)

    stamp = subprocess.run(["date", "-u"], check=True, capture_output=True, text=True).stdout.strip()
    head = git_head()
    commit_full = git_full(COMMIT)
    script_path = os.path.abspath(__file__)
    script_rel = os.path.relpath(script_path, REPO)
    with open(script_path, "rb") as fh:
        script_sha = sha256_bytes(fh.read())
    block_sha = sha256_bytes(git_show(BLOCK).encode("utf-8"))
    cmd = " ".join(shlex.quote(a) for a in [sys.executable] + sys.argv)
    assert block_sha == BLOCK_SHA256_ROUTED, "block sha mismatch"

    add = git_show(ADDENDUM).split("\n")
    res = git_show(RESULTS).split("\n")
    manifest = json.loads(git_show(MANIFEST))
    valuescheck = json.loads(git_show(VALUESCHECK))
    preflight = git_show(PREFLIGHT).split("\n")
    n_layers = {s: json.loads(git_show(f"data/olmo/rl_{s}.json"))["n_layers"] for s in STAGES}
    b2c = json.loads(git_show(B2C))
    assert b2c["n_canonical"] == 50 and len(b2c["canonical_concepts"]) == 50
    assert "'50 words from the paper'" in b2c["provenance"]["concepts_source"]
    assert b2c["provenance"]["concepts_source"].startswith("experiments/01_concept_injection.py:58 (DEFAULT_TEST_CONCEPTS")
    # round 3: 03's own list as Code read it, against the canonical list the record recovered from 01:58
    exp03_n_read1 = len(EXP03_CONCEPTS_READ1)
    exp03_same_order = EXP03_CONCEPTS_READ1 == b2c["canonical_concepts"]
    exp03_read2_ok = (EXP03_CONCEPTS_READ2["n"] == exp03_n_read1 and EXP03_CONCEPTS_READ1[0] == EXP03_CONCEPTS_READ2["first"]
                      and EXP03_CONCEPTS_READ1[-1] == EXP03_CONCEPTS_READ2["last"])
    assert exp03_n_read1 == 50 and len(set(EXP03_CONCEPTS_READ1)) == 50 and exp03_read2_ok
    assert b2c["selection_for_B2"]["registered_n"] == 8
    assert "There is no canonical eight to recover" in b2c["selection_for_B2"]["problem"]
    explore_dpo = json.loads(git_show("data/olmo/b2r_explore_dpo.json"))
    assert explore_dpo["stage"] == "dpo" and explore_dpo["part"] == "explore"
    file_lines = {ADDENDUM: add, RESULTS: res}
    for path, ln, anchor in LINE_ANCHORS:
        lines = file_lines.get(path) or git_show(path).split("\n")
        file_lines[path] = lines
        assert anchor in lines[ln - 1], f"anchor not found at {path}:{ln}: {anchor!r}"
    vc_power = valuescheck["1_g3A_power"]["detail"]
    vc_tables = valuescheck["2_tables"]["detail"]
    assert vc_power == "joint=0.9642 >= 0.90", vc_power
    assert vc_tables.startswith("§0.2 exact"), vc_tables
    pre_missing = {}
    for name in ("RESEARCH-NOTE-v0_2-draft.md", "*F1*.svg", "*F2*.svg"):
        hit = [(i, t) for i, t in enumerate(preflight, 1) if t.startswith(f"| `{name}` |")]
        assert len(hit) == 1 and "| MISSING |" in hit[0][1], (name, hit)
        pre_missing[name] = hit[0][0]

    H = []  # header
    L = []  # body
    w = L.append
    H.append("# AUDIT-note-release v1.2 -- N2(vi): the source's per-stage hit rates")
    H.append("")
    H.append(f"- Code stamp: {stamp} (date -u)")
    H.append(f"- HEAD at run (informational; every repository read below is pinned to {COMMIT} = {commit_full}): {head}")
    H.append(f"- Block: `{BLOCK}` sha256 `{block_sha}` (from git show {COMMIT}:{BLOCK}); routed sha256 "
             f"`{BLOCK_SHA256_ROUTED}`: {'MATCH' if block_sha == BLOCK_SHA256_ROUTED else 'MISMATCH'}")
    H.append(f"- Item: N2(vi), block line 35 ({BLOCK}@{COMMIT}:35)")
    H.append(f"- Script: `{script_rel}` sha256 `{script_sha}`")
    H.append(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]})")
    H.append(f"- Command: `{cmd}`")
    H.append(f"- Source read by Code on {SOURCE_READ_DATE_UTC} (UTC) with the WebFetch tool (reading only; nothing "
             "downloaded, saved or executed). WebFetch returns a model-processed rendering of each page, so every "
             "source fact below is Code's reading through that tool. Each of the four v1 Appendix C sentences came "
             "back verbatim in two separate fetches (one general, one asking for the sentence character for "
             "character; the general fetch omitted only the base sentence's opening clause naming Figure 21), "
             "and a third fetch that paraphrased the paragraph agreed with both, "
             "including that the instruct 0.3% is the introspection rate and the instruct FPR is 0%. The fixer "
             f"pass re-read four points on the same date, round 2 two more on {ROUND2_READ_DATE_UTC}, and round 3 "
             f"one file twice on {ROUND3_READ_DATE_UTC} (section 3, last three lists).")
    H.append(f"- Not checked: the note's own sentence and F2's plotted points. {PREFLIGHT}@{COMMIT}:"
             f"{pre_missing['RESEARCH-NOTE-v0_2-draft.md']} lists `RESEARCH-NOTE-v0_2-draft.md` as MISSING and "
             f":{pre_missing['*F1*.svg']}-{pre_missing['*F2*.svg']} list the F1/F2 SVGs as MISSING on this "
             "machine, so the note's wording (that it 'carries 0.001 / 0.149 / 0.029 / 0.009') and F2's plotted "
             "source points were not read; the values are taken as the block states them (block :35).")

    # ---------------------------------------------------------------- 1
    w("")
    w("## 1. The addendum's lines (git show " + COMMIT + ":" + ADDENDUM + ")")
    w("")
    printed = set()
    for (lo, hi), anchor, label in ADDENDUM_RANGES:
        assert anchor in add[lo - 1], f"addendum anchor not found at :{lo}: {anchor!r}"
        w(f"### :{lo}-{hi} -- {label}")
        w("```")
        L.extend(numbered(add, lo, hi, ADDENDUM))
        w("```")
        printed.update(range(lo, hi + 1))
    extra = [i for i, t in enumerate(add, 1) if ADDENDUM_VALUE_RE.search(t) and i not in printed]
    w("")
    w(f"Other addendum lines matching `{ADDENDUM_VALUE_RE.pattern}` outside the ranges above: "
      f"{len(extra)}")
    if extra:
        w("```")
        for i in extra:
            w(f"{ADDENDUM}@{COMMIT}:{i}: {add[i - 1]}")
        w("```")

    # parse the section 0.2 table
    rec_add = {}
    for i in range(43, 47):
        cells = [c.strip() for c in add[i - 1].strip().strip("|").split("|")]
        stage = cells[0]
        assert stage in STAGES, (i, cells)
        rec_add[stage] = {"tpr": pct(cells[1]), "fpr": pct(cells[2]), "sens_pp": cells[3], "line": i}
    assert "aggregated over L ∈ [25,32,38,45,51], α ∈ [1,2,4,8]" in add[38], "addendum :39 aggregation text"

    # ---------------------------------------------------------------- 2
    w("")
    w("## 2. RESULTS.md lines carrying the same values (git show " + COMMIT + ":RESULTS.md)")
    w("")
    for (lo, hi), anchor, label in RESULTS_RANGES:
        assert anchor in res[lo - 1], f"RESULTS anchor not found at :{lo}: {anchor!r}"
        w(f"### :{lo}-{hi} -- {label}")
        w("```")
        L.extend(numbered(res, lo, hi, RESULTS))
        w("```")
    rec_res = {}
    for i in range(6996, 7000):
        cells = [c.strip() for c in res[i - 1].strip().strip("|").split("|")]
        stage = cells[0]
        assert stage in STAGES, (i, cells)
        rec_res[stage] = {"their_fpr": float(cells[2]), "line": i}
    w("")
    w(f"### {VALUESCHECK}@{COMMIT} (the committed artifact cited at RESULTS.md@{COMMIT}:7175)")
    w("```")
    w(f"1_g3A_power.detail: {vc_power}")
    w(f"2_tables.detail:    {vc_tables}")
    w("```")
    vc_commit = "ae73caa"
    vc_files = subprocess.run(["git", "-C", REPO, "show", "--name-only", "--format=", vc_commit],
                              check=True, capture_output=True, text=True).stdout.split()
    assert VALUESCHECK in vc_files, vc_files
    vc_scripts = sorted(f for f in vc_files if f.endswith(".py"))
    term_counts = {}
    power_lines = {}
    clopper_lines = {}
    for c in (vc_commit, COMMIT):
        for f in vc_scripts:
            txt = subprocess.run(["git", "-C", REPO, "show", f"{c}:{f}"], check=True,
                                 capture_output=True).stdout.decode("utf-8").split("\n")
            for t in ("power", "clopper", "valuescheck"):
                term_counts[(c, f, t)] = sum(t in ln.lower() for ln in txt)
            power_lines[(c, f)] = [i for i, ln in enumerate(txt, 1) if "power" in ln.lower()]
            clopper_lines[(c, f)] = [i for i, ln in enumerate(txt, 1) if "clopper" in ln.lower()]
    cl = clopper_lines[(COMMIT, "scripts/b2r_analyze.py")]
    assert cl == [10, 49, 60, 61, 74, 112], cl
    b2r_txt = git_show("scripts/b2r_analyze.py").split("\n")
    assert b2r_txt[1].startswith('"""') and all('"""' not in b2r_txt[i - 1] for i in range(3, 11))  # :10 in the docstring
    assert all("clopper_pearson(" in b2r_txt[i - 1] and "=" in b2r_txt[i - 1] for i in (60, 61, 74, 112))
    w(f"Both are result strings. The file records neither the rates nor the method behind the power figure. It "
      f"entered at {vc_commit}, whose files are {', '.join(vc_files)}. Lines containing each term "
      "(case-insensitive), in that commit's scripts:")
    w("")
    w("| commit | script | 'power' | 'clopper' | 'valuescheck' | lines with 'power' |")
    w("|---|---|---|---|---|---|")
    for c in (vc_commit, COMMIT):
        for f in vc_scripts:
            w(f"| {c} | {f} | {term_counts[(c, f, 'power')]} | {term_counts[(c, f, 'clopper')]} | "
              f"{term_counts[(c, f, 'valuescheck')]} | {power_lines[(c, f)]} |")
    w("")
    w(f"In b2r_analyze.py@{COMMIT} 'power' appears at :16 (docstring) and :91 (a reading string), and "
      f"'clopper' at :{cl[0]} (docstring), :{cl[1]} (import) and "
      + ", ".join(f":{i}" for i in cl[2:]) + " (interval calls on data). Code read "
      f"b2r_analyze.py@{COMMIT} in full (300 lines) and found no power computation. "
      "box_b2r_sampling_smoke.py has no line with any of the three terms at either commit, and neither script "
      "names the valuescheck file. Code found no committed code that produces 0.9642.")
    for f in vc_scripts:
        assert term_counts[(COMMIT, f, "valuescheck")] == 0 and term_counts[(vc_commit, f, "valuescheck")] == 0
    assert power_lines[(COMMIT, "scripts/b2r_analyze.py")] == [16, 91], power_lines
    assert all(term_counts[(c, "scripts/box_b2r_sampling_smoke.py", t)] == 0
               for c in (vc_commit, COMMIT) for t in ("power", "clopper", "valuescheck")), term_counts
    assert len(git_show("scripts/b2r_analyze.py").rstrip("\n").split("\n")) == 300

    # carrier search (round 2)
    for key, (label, rx, inc, unrel) in CARRIERS.items():
        cre = re.compile(rx)
        for path, lines in ((RESULTS, res), (ADDENDUM, add)):
            hits = [i for i, t in enumerate(lines, 1) if cre.search(t)]
            want = sorted(set(inc.get(path, [])) | set(unrel.get(path, {})))
            assert not set(inc.get(path, [])) & set(unrel.get(path, {})), (key, path)
            assert hits == want, (key, path, hits, want)
    other_out = subprocess.run(["git", "-C", REPO, "grep", "-n", "-E", OTHER_GREP, COMMIT, "--",
                                *OTHER_GREP_PATHSPEC], check=True, capture_output=True).stdout.decode("utf-8")
    other_hits = sorted(":".join(ln.split(":")[1:3]) for ln in other_out.splitlines())
    assert other_hits == sorted(set(OTHER_CARRIERS) | set(OTHER_UNRELATED)), other_hits
    other_out_r3 = subprocess.run(["git", "-C", REPO, "grep", "-n", "-E", OTHER_GREP_R3, COMMIT, "--",
                                   *OTHER_GREP_PATHSPEC], check=True, capture_output=True).stdout.decode("utf-8")
    other_hits_r3 = sorted(":".join(ln.split(":")[1:3]) for ln in other_out_r3.splitlines())
    assert other_hits_r3 == sorted(OTHER_CARRIERS_R3), other_hits_r3
    grep_r4_hits = {}
    for k_, (_, rx_, car_, unr_) in GREP_R4.items():
        out_ = subprocess.run(["git", "-C", REPO, "grep", "-n", "-E", rx_, COMMIT, "--", *GREP_R4_PATHSPEC],
                              check=True, capture_output=True).stdout.decode("utf-8")
        hits_ = sorted(":".join(ln.split(":")[1:3]) for ln in out_.splitlines())
        assert not set(car_) & set(unr_), k_
        assert hits_ == sorted(set(car_) | set(unr_)), (k_, hits_)
        grep_r4_hits[k_] = hits_
    other_by_key = {k: [p for p, (_, keys) in list(OTHER_CARRIERS.items()) + list(OTHER_CARRIERS_R3.items())
                        if k in keys] for k in CARRIERS}
    for k_ in N_INFERENCE_LINES:  # the two n rows of section 0 split these carriers exactly
        for pth in (RESULTS, ADDENDUM):
            a_ = N_INFERENCE_LINES[k_].get(pth, []) + N_AS_SOURCE_LINES[k_].get(pth, [])
            assert sorted(a_) == sorted(CARRIERS[k_][2].get(pth, [])) and len(set(a_)) == len(a_), (k_, pth)
    # the entries holding the n carriers: :7365 in :7326-7418 (no eight-concept premise), :7439-7500 in :7419-7506
    entry_starts = [i for i in range(7300, 7521) if res[i - 1].startswith("- ")]
    assert entry_starts == [7326, 7419, 7507], entry_starts
    assert not any("eight" in res[i - 1].lower() for i in range(7326, 7419))
    assert sum("eight" in res[i - 1].lower() for i in range(7419, 7507)) == 1 and "With eight" in res[7437]
    n_unrel = sum(len(u) for _, _, _, un in CARRIERS.values() for u in un.values())
    w("")
    w("### Carrier search (rounds 2-4): every line of the record that carries each figure")
    w("")
    w("Round 3 added the last two patterns (the ~800/80 n and the ~33× ratio derived from it).")
    w("")
    w(f"One regex per figure, run over every line of RESULTS.md@{COMMIT} ({len(res) - (res[-1] == '')} lines) "
      f"and {ADDENDUM}@{COMMIT} ({len(add) - (add[-1] == '')} lines). The script asserts that the hits are exactly the carriers listed "
      f"below plus the {n_unrel} lines listed as unrelated (Code read each one), so these lists are complete for "
      "these patterns; a value written another way (for example in words) would not be found. Section 0 takes "
      "its locators from here. The regexes:")
    w("")
    for key, (label, rx, inc, unrel) in CARRIERS.items():
        w(f"- {label}: `{rx}`")
    w("")
    w(f"| figure | RESULTS.md@{COMMIT} | {ADDENDUM}@{COMMIT} | other tracked .py/.md carriers at {COMMIT} | "
      "matched but unrelated |")
    w("|---|---|---|---|---|")
    for key, (label, rx, inc, unrel) in CARRIERS.items():
        un = "; ".join(f"{'RESULTS' if p == RESULTS else 'ADDENDUM'} :{ln} ({why})"
                       for p, d_ in unrel.items() for ln, why in sorted(d_.items()))
        w(f"| {label} | " + (", ".join(f":{x}" for x in inc.get(RESULTS, [])) or "none") + " | "
          + (", ".join(f":{x}" for x in inc.get(ADDENDUM, [])) or "none") + " | "
          + (", ".join(other_by_key[key]) or "none") + f" | {un or 'none'} |")
    w("")
    w(f"Other tracked .py/.md files at {COMMIT} (RESULTS.md, the addendum and results/raw/ excluded), one "
      f"`git grep -E` with `{OTHER_GREP}`: {len(other_hits)} hits, {len(OTHER_CARRIERS)} carriers and "
      f"{len(OTHER_UNRELATED)} unrelated. Carriers: "
      + "; ".join(f"{p} ({what})" for p, (what, _) in OTHER_CARRIERS.items())
      + ". Unrelated: " + "; ".join(f"{p} ({why})" for p, why in OTHER_UNRELATED.items())
      + ". These are code comments, a self-test fixture and a handoff, not log lines; they are listed so that "
        "a correction to a source value can find every copy. None is edited (read-only).")
    w("")
    w(f"Round 3, a second `git grep -E` over the same files with `{OTHER_GREP_R3}` (the two round-3 patterns): "
      f"{len(other_hits_r3)} hit, "
      + "; ".join(f"{p} ({what})" for p, (what, _) in OTHER_CARRIERS_R3.items()) + ".")
    w("")
    w(f"Round 4, two `git grep -E` runs over every tracked .py/.md file at {COMMIT} with RESULTS.md and the "
      "addendum included (results/raw/ excluded), each asserted to return exactly the lines below. They cover "
      "rows 19 and 24 of section 0, which the per-figure search above does not:")
    w("")
    for k_, (lab_, rx_, car_, unr_) in GREP_R4.items():
        w(f"- {lab_}: `{rx_}`: {len(grep_r4_hits[k_])} hit{'s' if len(grep_r4_hits[k_]) != 1 else ''}. Carriers: "
          + "; ".join(f"{p} ({what})" for p, what in car_.items())
          + (". Unrelated: " + "; ".join(f"{p} ({why})" for p, why in unr_.items()) if unr_ else ". Unrelated: none")
          + ".")
    w("")
    w(f"Row 19's table cells (RESULTS.md@{COMMIT}:7358-7361) are written '| **0.000** |' and so on, which the first "
      "pattern does not match; the script locates them by parsing the table (section 6b).")

    # ---------------------------------------------------------------- 3
    w("")
    w("## 3. Code's reading of the source (URLs, versions, what each holds)")
    w("")
    w(f"Paper: Macar, Yang, Wang, Wallich, Ameisen, Lindsey, 'Mechanisms of Introspective Awareness', "
      f"arXiv:2603.21396. Abstract page {URL_ABS}; version list from {URL_ABS_V5}: v1 2026-03-22, "
      "v2 2026-04-10, v3 2026-04-13, v4 2026-05-15, v5 2026-06-10 (UTC dates as listed).")
    w("")
    w("| version | date | URL read | OLMo per-stage content, as Code read it |")
    w("|---|---|---|---|")
    for v, d0, u, what in SOURCE_VERSIONS:
        w(f"| {v} | {d0} | {u} | {what} |")
    w("")
    w("**Which version the record's numbers come from.** The addendum (written 2026-08-24, when v5 was current) "
      "cites 'arXiv:2603.21396 Appendix C, Fig 21' with no version. Only v1 has an Appendix C on OLMo and a "
      "Figure 21 with the [25,32,38,45,51] x [1,2,4,8] aggregation. In v4 a Figure 21 also exists and also "
      "shows the four OLMo stages, but it is the Appendix D.1 figure at L = 19 and L = 22, so an unversioned "
      "'Fig 21' resolves to a different OLMo-stage figure there. In v2-v5 the numbers 0.1% / 14.9% / 2.9% / "
      "0.9% are not in the text: the OLMo stage comparison is presented at a single layer (L = 25) over 50 "
      "concepts, with per-stage values only in figures. Code did not find a statement of why the presentation "
      "changed, and does not infer one.")
    w("")
    w("**v1 Appendix C, per stage (prose; the paragraph opens by naming Figure 21).** This raw keeps to one "
      "short quotation from the source (the SFT sentence). For the other three stages it gives only the "
      "numbers, in Code's words, each exactly as the text prints it:")
    w("")
    for s in STAGES:
        w(f"- {s}: {SOURCE_V1_TEXT_PARAPHRASE[s]}.")
    w("")
    w(f"The one quotation: \"{SOURCE_QUOTE}\" ({SOURCE_QUOTE_ATTRIB}).")
    w("")
    w("v1 Figure 21's caption names the four stages in pipeline order and says the rates are aggregated across "
      f"L in [25, 32, 38, 45, 51] with alpha in [1, 2, 4, 8]. The figure is an image ({V1_FIG21_IMAGE}, alt "
      "text 'Refer to caption'); the v1 HTML carries no data table or numeric labels for it and no "
      "per-(layer, alpha) breakdown. Code did not digitize the figure (no image was fetched).")
    w("")
    w("v1 Section 3.3 ('The Role of Post-Training') also carries the OLMo stage result in the main text, "
      "qualitatively: it points to Appendix C and says that base and SFT have high FPR and that FPR reaches 0% "
      "only after DPO, with no per-stage TPR numbers. The record quotes that sentence at "
      f"RESULTS.md@{COMMIT}:7346-7347 (section 2).")
    w("")
    w("Metric definitions (v1, Section 2/Appendix B as Code read them): TPR = P(detect | injection) over "
      "injection trials; FPR = P(detect | no injection) over control trials; introspection rate = "
      "P(detect and identify | injection) over injection trials.")
    w("")
    w(f"Released code ({GH}, sha {GH_SHA}; the commits page {URL_GH_COMMITS} showed 5d5d9b4, 2026-04-16, as "
      "the newest commit on main when read). Pages read: "
      f"{URL_GH_README}; {URL_RAW_README}; {URL_GH_MODEL_UTILS}; {URL_RAW_MODEL_UTILS}; {URL_RAW_EXP03}.")
    w("")
    w("- `src/model_utils.py` MODEL_NAME_MAP (no revision pinned): " + "; ".join(
        f"{k} -> {r}" for k, r in SOURCE_CODE["model_name_map"].values()) + ".")
    w(f"- `get_layer_at_fraction`: {SOURCE_CODE['get_layer_at_fraction']}.")
    w(f"- dtype: {SOURCE_CODE['dtype_default']}.")
    d = SOURCE_CODE["exp03_defaults"]
    w("- `experiments/03_behavioral_robustness.py` defaults: " + "; ".join(f"{k} = {v}" for k, v in d.items()) + ".")
    for f in SOURCE_CODE["exp03_facts"]:
        w(f"- {f}")
    w(f"- README OLMo command: `{SOURCE_CODE['readme_olmo_command']}`.")
    w("")
    w("Fixer-pass reads (same date, same tool):")
    for u, what in FIXER_READS:
        w(f"- {u}: {what}.")
    w("")
    w(f"Round-2 reads ({ROUND2_READ_DATE_UTC}, same tool, two fetches of the page, agreeing):")
    for u, what in ROUND2_READS:
        w(f"- {u}: {what}.")
    w("")
    w(f"Round-3 reads ({ROUND3_READ_DATE_UTC}, same tool, the same file twice with different prompts):")
    for u, what in ROUND3_READS:
        w(f"- {u}: {what}.")

    # ---------------------------------------------------------------- 4
    w("")
    w("## 4. The record's values against the source, cell by cell")
    w("")
    w(f"Record A = {ADDENDUM}@{COMMIT}:43-46 (section 0.2 table). Record B = RESULTS.md@{COMMIT}:6996-6999 "
      "(B2-r verdict, 'theirs' column, FPR only). Source = v1 Appendix C text. TPR's domain is injected trials "
      "and FPR's is control trials, each pooled over the 20 (layer, alpha) configurations; the source states "
      "neither denominator (section 5).")
    w("")
    w("| stage | TPR record A | TPR source | match | FPR record A | FPR record B | FPR source | match | "
      "introspection rate, source | record A TPR-FPR | source TPR-FPR (computed-new) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    cmp_rows = {}
    for s in STAGES:
        a, b, src = rec_add[s], rec_res[s], SOURCE_V1[s]
        tm = abs(a["tpr"] - src["tpr"]) < 1e-9
        fm = abs(a["fpr"] - src["fpr"]) < 1e-9 and abs(b["their_fpr"] - src["fpr"]) < 1e-9
        sens = round((src["tpr"] - src["fpr"]) * 100, 1)
        rec_sens = round((a["tpr"] - a["fpr"]) * 100, 1)
        assert a["sens_pp"].replace("−", "-").replace(" pp", "") == f"{rec_sens:+.1f}", (s, a["sens_pp"], rec_sens)
        cmp_rows[s] = {"tpr_match": tm, "fpr_match": fm, "source_tpr_minus_fpr_pp": sens,
                       "record_a_tpr": a["tpr"], "record_a_fpr": a["fpr"], "record_b_fpr": b["their_fpr"],
                       "record_a_sens": a["sens_pp"], "sens_match": abs(sens - rec_sens) < 1e-9}
        w(f"| {s} | {fmt(a['tpr'])} | {fmt(src['tpr'])} | {'yes' if tm else 'NO'} | {fmt(a['fpr'])} | "
          f"{fmt(b['their_fpr'])} | {fmt(src['fpr'])} | {'yes' if fm else 'NO'} | "
          f"{fmt(src['introspection_rate'])} | {a['sens_pp']} | {sens:+.1f} pp |")
    n_tpr = sum(r["tpr_match"] for r in cmp_rows.values())
    n_fpr = sum(r["fpr_match"] for r in cmp_rows.values())
    w("")
    w(f"TPR: {n_tpr}/4 cells match the source text. FPR: {n_fpr}/4 cells match. The instruct FPR the record "
      "carries (0.3%, in both A and B) is the figure the v1 sentence gives as the instruct checkpoint's "
      "introspection rate; the same sentence gives the instruct FPR as 0%. Code reads this as a "
      "transcription slip in the record (Code's reading, not established). The record says it recovered the "
      f"values 'from the paper (Appendix C, Fig 21)' (RESULTS.md@{COMMIT}:7327), and Figure 21 is an image "
      f"({V1_FIG21_IMAGE}) that this audit did not digitize, so a reading of the figure is not excluded and "
      "whether its plotted instruct FPR differs from the text is not known. Under block :23 the classification "
      "decides the consequence for a note that carries the 0.3% (section 12).")

    # ---------------------------------------------------------------- 5
    w("")
    w("## 5. Grid, n, and the layer arithmetic (computed-new from the source code's defaults)")
    w("")
    fr = d["DEFAULT_LAYER_SWEEP"]
    idx = {s: [max(0, min(int(n_layers[s] * f), n_layers[s] - 1)) for f in fr] for s in STAGES}
    ridx = {s: [max(0, min(round(n_layers[s] * f), n_layers[s] - 1)) for f in fr] for s in STAGES}
    assert len({tuple(v) for v in idx.values()}) == 1 and len({tuple(v) for v in ridx.values()}) == 1
    idx0, ridx0 = idx["base"], ridx["base"]
    w(f"- n_layers per stage from data/olmo/rl_{{stage}}.json@{COMMIT} field `n_layers`: "
      + ", ".join(f"{s} {n_layers[s]}" for s in STAGES) + ".")
    w(f"- int(n_layers x f) for the code's DEFAULT_LAYER_SWEEP {fr}: {idx0}. round(n_layers x f): {ridx0}. "
      f"The v1 caption lists {V1_FIG21_LAYERS}. int() differs from the caption at the fourth layer "
      f"({idx0[3]} vs {V1_FIG21_LAYERS[3]}; 64 x 0.7 = {64 * 0.7!r} truncates to 44); round() differs at the "
      f"first ({ridx0[0]} vs {V1_FIG21_LAYERS[0]}; 64 x 0.4 = {64 * 0.4!r}). Neither rule yields the caption's "
      "list. Not adjudicated: the source does not say which ran.")
    readme_ls = [25.0, 32.0, 38.0, 45.0, 51.0]
    readme_idx = [max(0, min(int(64 * f), 63)) for f in readme_ls]
    readme_keys = ["olmo_32b_base", "olmo_32b_sft", "olmo_32b_dpo", "olmo_32b"]
    rejected = [k for k in readme_keys if k not in d["OLMO_MODELS"] + ["all"]]
    readme_eq_caption = sum(int(a) == b for a, b in zip(readme_ls, V1_FIG21_LAYERS))
    int_eq_caption = sum(a == b for a, b in zip(idx0, V1_FIG21_LAYERS))
    round_eq_caption = sum(a == b for a, b in zip(ridx0, V1_FIG21_LAYERS))
    w(f"- The README command as written cannot run at 5d5d9b4: its -m keys {readme_keys} are not among the "
      f"choices {d['OLMO_MODELS'] + ['all']} ({len(rejected)}/4 not accepted), so argparse would refuse it "
      f"before any forward, and its -ls values {readme_ls}, read as fractions, give int(64 x f) clamped = "
      f"{readme_idx}. Its layer list nonetheless equals the v1 caption's {readme_eq_caption}/5, which neither "
      f"int() ({int_eq_caption}/5) nor round() ({round_eq_caption}/5) of the default fractions does. That is "
      "consistent with absolute layers 25/32/38/45/51 having been run by some path other than the README "
      "command as written, rather than the default fractions (the record reads it the same way: "
      f"RESULTS.md@{COMMIT}:7396-7398). Not adjudicated; it bears on note 5 (L_M = 44 against the caption's "
      "45).")
    n_cfg = len(V1_FIG21_LAYERS) * len(V1_FIG21_ALPHAS)
    inj_per_concept = d["DEFAULT_MAX_TRIAL_NUMBER"] * d["DEFAULT_SAMPLES_PER_TRIAL"]
    ctl_per_concept = d["DEFAULT_MAX_TRIAL_NUMBER"] * d["DEFAULT_CONTROL_SAMPLES_PER_TRIAL"]
    scen = []
    for n_c, label in ((8, "eight concepts (the record's assumption, RESULTS.md@bbc9ffe:7438-7440)"),
                       (d["DEFAULT_TEST_CONCEPTS_len"], "the code's default DEFAULT_TEST_CONCEPTS (50)")):
        scen.append({"n_concepts": n_c, "label": label,
                     "per_cell_injected": n_c * inj_per_concept, "per_cell_control": n_c * ctl_per_concept,
                     "per_stage_pooled_injected": n_c * inj_per_concept * n_cfg,
                     "per_stage_pooled_control": n_c * ctl_per_concept * n_cfg})
    w(f"- Configurations aggregated per stage: {len(V1_FIG21_LAYERS)} layers x {len(V1_FIG21_ALPHAS)} "
      f"strengths = {n_cfg}.")
    w(f"- Per (layer, alpha, concept) cell under the code's defaults: {inj_per_concept} injected "
      f"({d['DEFAULT_MAX_TRIAL_NUMBER']} trial numbers x {d['DEFAULT_SAMPLES_PER_TRIAL']} samples) and "
      f"{ctl_per_concept} control ({d['DEFAULT_MAX_TRIAL_NUMBER']} x {d['DEFAULT_CONTROL_SAMPLES_PER_TRIAL']}).")
    w("")
    w("| scenario | per (layer, alpha) cell: injected / control | per stage, pooled over 20 cells: injected / control |")
    w("|---|---|---|")
    for sc in scen:
        w(f"| {sc['label']} | {sc['per_cell_injected']} / {sc['per_cell_control']} | "
          f"{sc['per_stage_pooled_injected']} / {sc['per_stage_pooled_control']} |")
    w("")
    w("Neither row is stated by the source. v1 gives no n and no concept count for the OLMo runs; v2-v5 state "
      "50 concepts for the reworked L = 25 figure. The released code's denominators are the *evaluated* "
      "trials (`len(evaluated_injection)`, `len(evaluated_control)`), so realized n may be below these "
      "counts by an unknown amount. Any d-prime or Fisher test on the source's points (N2(v)) has to declare "
      "its assumed n. The block's '800/80 per configuration' is the first row's per-cell figure.")
    w("")
    w(f"Where the eight comes from: it is our own B2 registration, not a source count. {B2C}@{COMMIT} records "
      f"`n_canonical` = {b2c['n_canonical']} (`canonical_concepts`, {len(b2c['canonical_concepts'])} entries; "
      "`provenance.concepts_source` cites experiments/01_concept_injection.py:58's DEFAULT_TEST_CONCEPTS, with "
      f"its comment '50 words from the paper') and `selection_for_B2.registered_n` = "
      f"{b2c['selection_for_B2']['registered_n']}, with the note that the source has no canonical eight to "
      "recover. The 50 in section 3's defaults and in the table above is a different file's: the OLMo "
      "experiment, experiments/03_behavioral_robustness.py, defines its own DEFAULT_TEST_CONCEPTS as a literal "
      "list in that file, not an import from 01 (both round-3 reads, section 3). On the first read its "
      f"{exp03_n_read1} entries equal `canonical_concepts` "
      + ("entry for entry and in order" if exp03_same_order else "NOT entry for entry")
      + " (computed-new). The second read confirmed only the count, the first and last entries and that the "
      "name is imported nowhere, so the identity of 03's list with 01's rests on one model-processed read: "
      "Code's reading, not established. The count, 50, does not depend on it. The unit also matters: each "
      "per-cell figure is one "
      f"(layer, alpha) configuration's n, while every source rate is pooled over all {n_cfg}. A test of a pooled "
      "rate under the same premise uses the pooled column (section 7 gives both). Pooled counts still treat "
      "trials clustered by configuration and concept as independent, so neither unit gives an exact test of "
      "the source's aggregate.")

    # ---------------------------------------------------------------- 6
    rec = load_record_stats()
    n_g3a = 96
    cp_agree = max(max(abs(x - y) for x, y in zip(own_cp(k, n_g3a), rec["clopper_pearson_raw"](k, n_g3a)))
                   for k in range(n_g3a + 1))
    assert cp_agree < 1e-12, cp_agree
    rates_rec = {s: rec_add[s]["fpr"] for s in STAGES}
    rates_src = {s: SOURCE_V1[s]["fpr"] for s in STAGES}
    jp_rec, pairs_rec = joint_power(rates_rec, n_g3a, rec["clopper_pearson"], rec["binom_pmf"])
    jp_src, pairs_src = joint_power(rates_src, n_g3a, rec["clopper_pearson"], rec["binom_pmf"])
    jp_rec_own, pairs_rec_own = joint_power(rates_rec, n_g3a, own_cp, own_pmf)
    assert abs(jp_rec - jp_rec_own) < 1e-9 and all(abs(pairs_rec[k] - pairs_rec_own[k]) < 1e-9 for k in pairs_rec), \
        (jp_rec, jp_rec_own)
    pair_rec, pair_src = pairs_rec["base>dpo"], pairs_src["base>dpo"]
    weak_rec = min(pairs_rec, key=pairs_rec.get)
    weak_src_val = min(pairs_src.values())
    weak_src = [k for k, v in pairs_src.items() if abs(v - weak_src_val) < 1e-12]
    REC_JOINT, REC_PAIR = 0.9642, 0.9825
    assert f"{jp_rec:.3f}" != "0.964", jp_rec  # the record's 'the exact number is 0.964' (3 dp)
    pairs_equal_9825 = [k for k, v in pairs_rec.items() if f"{v:.4f}" == f"{REC_PAIR:.4f}"]
    assert f"{jp_rec:.5f}" == CHECKER_R2_JOINT_5DP and all(f"{pairs_rec[k]:.5f}" == v
                                                           for k, v in CHECKER_R2_PAIRS_5DP.items()), pairs_rec
    # candidate causes for the printed 0.9642 / 0.9825 (computed-new; none is the record's stated method)
    variants = [
        ("Wilson score 95% intervals in place of CP", rates_rec, n_g3a, own_wilson),
        ("Clopper-Pearson at 90% (alpha .10)", rates_rec, n_g3a,
         lambda k, n: rec["clopper_pearson"](k, n, 0.10)),
        ("n = 95 per stage", rates_rec, 95, rec["clopper_pearson"]),
        ("base FPR .163 (one unit lower at 3 dp)", dict(rates_rec, base=0.163), n_g3a, rec["clopper_pearson"]),
    ]
    var_rows = []
    for vlabel, vr, vn, vci in variants:
        vj, vp = joint_power(vr, vn, vci, rec["binom_pmf"])
        var_rows.append({"variant": vlabel, "joint": vj, "base>dpo": vp["base>dpo"],
                         "reproduces_both_4dp": f"{vj:.4f}" == f"{REC_JOINT:.4f}" and f"{vp['base>dpo']:.4f}" == f"{REC_PAIR:.4f}"})
    mc_rows = []
    for nsim in (10 ** 4, 10 ** 5, 10 ** 6):
        se_p = math.sqrt(pair_rec * (1 - pair_rec) / nsim)
        se_j = math.sqrt(jp_rec * (1 - jp_rec) / nsim)
        mc_rows.append({"draws": nsim, "se_pair": se_p, "se_joint": se_j,
                        "pair_residual_in_se": (REC_PAIR - pair_rec) / se_p,
                        "joint_residual_in_se": (REC_JOINT - jp_rec) / se_j})
    # the record's p ~ .28 for 0/43 at the source's 2.9% (RESULTS :6955, :7091)
    k43, n43 = explore_dpo["hit"], explore_dpo["inj_decidable"]
    assert (k43, n43) == (0, 43), (k43, n43)
    p28 = sum(rec["binom_pmf"](k, n43, SOURCE_V1["dpo"]["tpr"]) for k in range(0, k43 + 1))
    assert abs(p28 - (1 - SOURCE_V1["dpo"]["tpr"]) ** n43) < 1e-12 and f"{p28:.2f}" == "0.28", p28
    k_base96 = half_up(Decimal(str(rates_rec["base"])) * n_g3a)
    cp_base_lo = rec["clopper_pearson"](k_base96, n_g3a)[0]
    cp_dpo_hi = rec["clopper_pearson"](0, n_g3a)[1]
    table_ns = (24, 48, 96, 200)
    table_rec = {  # RESULTS.md@bbc9ffe:7356-7361, as printed
        24: (0.001, 0.000), 48: (0.012, 0.000), 96: (0.147, 0.001), 200: (0.691, 0.020)}
    for ln, n_ in zip(range(7358, 7362), table_ns):
        cells = [c.strip().strip("*") for c in res[ln - 1].strip().strip("|").split("|")]
        assert int(cells[0].split()[0]) == n_ and float(cells[1]) == table_rec[n_][0] \
            and float(cells[2]) == table_rec[n_][1], (ln, cells)
    pw_rows = []
    for n_ in table_ns:
        dpo_p, dpo_om = retired_power(SOURCE_V1["dpo"]["tpr"], SOURCE_V1["dpo"]["fpr"], n_, rec)
        ins_rec, ins_rec_om = retired_power(rec_add["instruct"]["tpr"], rec_add["instruct"]["fpr"], n_, rec)
        ins_src, ins_src_om = retired_power(SOURCE_V1["instruct"]["tpr"], SOURCE_V1["instruct"]["fpr"], n_, rec)
        pw_rows.append({"n_per_arm": n_, "record_dpo": table_rec[n_][0], "record_instruct": table_rec[n_][1],
                        "recomputed_dpo": dpo_p, "recomputed_instruct_fpr_0p003": ins_rec,
                        "recomputed_instruct_fpr_0p000": ins_src,
                        "omitted_mass_bound": max(dpo_om, ins_rec_om, ins_src_om),
                        "dpo_agrees_3dp": f"{dpo_p:.3f}" == f"{table_rec[n_][0]:.3f}",
                        "instruct_agrees_3dp": f"{ins_rec:.3f}" == f"{table_rec[n_][1]:.3f}"})
    n_pw_agree = sum(r["dpo_agrees_3dp"] + r["instruct_agrees_3dp"] for r in pw_rows)
    for r in pw_rows:
        r["instruct_source_rate_differs_3dp"] = (f"{r['recomputed_instruct_fpr_0p000']:.3f}"
                                                 != f"{r['record_instruct']:.3f}")
    pw_src_differs = [r for r in pw_rows if r["instruct_source_rate_differs_3dp"]]
    assert [r["n_per_arm"] for r in pw_src_differs] == [96, 200], pw_src_differs
    assert all(SOURCE_V1["dpo"][k] == rec_add["dpo"][k] for k in ("tpr", "fpr"))
    # round 4: ':7363 holds' -- Instruct below DPO at every table n, at both inputs
    assert all(r["recomputed_instruct_fpr_0p003"] < r["recomputed_dpo"]
               and r["recomputed_instruct_fpr_0p000"] < r["recomputed_dpo"] for r in pw_rows)
    pw200 = next(r for r in pw_rows if r["n_per_arm"] == 200)
    pw48 = next(r for r in pw_rows if r["n_per_arm"] == 48)
    assert f"{pw48['recomputed_instruct_fpr_0p003']:.3f}" == f"{pw48['recomputed_instruct_fpr_0p000']:.3f}" == "0.000"
    # round 4: the n per arm at which the retired criterion reaches conventional power at Instruct
    # (RESULTS :7363-7364). The record's binom_pmf multiplies the int comb(n, k) by floats, which overflows once
    # comb(n, k) exceeds the float range; its CP cannot run there, so the record's newcombe is compiled with a
    # stdlib CP (own_cp_fast) and that path is checked against the record's own where the record's can run.
    n_ovf = next(n_ for n_ in range(2, 5000) if math.comb(n_, n_ // 2) > sys.float_info.max)
    try:
        rec["clopper_pearson_raw"](1, n_ovf)
        ovf_raises = False
    except OverflowError:
        ovf_raises = True
    rec["clopper_pearson_raw"](1, n_ovf - 1)  # runs below the threshold
    assert ovf_raises and n_ovf == 1030, (ovf_raises, n_ovf)
    fast_memo: dict = {}

    def cp_fast_memo(k, n, alpha=0.05):
        key = (k, n, alpha)
        if key not in fast_memo:
            fast_memo[key] = own_cp_fast(k, n, alpha)
        return fast_memo[key]

    nc_fast = record_newcombe_with(cp_fast_memo)
    ins_tpr = SOURCE_V1["instruct"]["tpr"]
    assert ins_tpr == rec_add["instruct"]["tpr"] == 0.009
    fpr_src_i, fpr_rec_i = SOURCE_V1["instruct"]["fpr"], rec_add["instruct"]["fpr"]
    # cross-check 1: the fast path against the record's own path, all 12 table cells
    fast_vs_rec = []
    for r in pw_rows:
        n_ = r["n_per_arm"]
        for col, (tp_, fp_) in (("recomputed_dpo", (SOURCE_V1["dpo"]["tpr"], SOURCE_V1["dpo"]["fpr"])),
                                ("recomputed_instruct_fpr_0p003", (ins_tpr, fpr_rec_i)),
                                ("recomputed_instruct_fpr_0p000", (ins_tpr, fpr_src_i))):
            fast_vs_rec.append(abs(retired_power_with(tp_, fp_, n_, nc_fast, own_pmf)[0] - r[col]))
    # cross-check 2: at n = 750 (source rates), the record's own path end to end, against the fast path
    XCHK_N = 750
    p750_rec, _ = retired_power(ins_tpr, fpr_src_i, XCHK_N, rec)
    p750_fast, _ = retired_power_with(ins_tpr, fpr_src_i, XCHK_N, nc_fast, own_pmf)
    fast_vs_rec.append(abs(p750_rec - p750_fast))
    # cross-check 3: the two CPs, at n = 96 for every k, and at n = 750 for every k the n = 750 power used
    ks750 = [k for k in range(XCHK_N + 1) if rec["binom_pmf"](k, XCHK_N, ins_tpr) >= PRUNE]
    cp_fast_vs_rec = max(abs(a - b) for n_, ks in ((96, range(97)), (XCHK_N, ks750 + [0])) for k in ks
                         for a, b in zip(own_cp_fast(k, n_), rec["clopper_pearson"](k, n_)))
    fast_vs_rec_max = max(fast_vs_rec)
    assert fast_vs_rec_max < 1e-12 and cp_fast_vs_rec < 1e-12, (fast_vs_rec_max, cp_fast_vs_rec)
    CONV_BARS = (0.80, 0.90)
    CONV_STEP, CONV_START = 10, 200  # step-10 grid from the table's last n
    conv = {}
    for lab_, fp_ in (("source", fpr_src_i), ("record", fpr_rec_i)):
        grid, om_max = {}, 0.0
        n_ = CONV_START
        while True:
            n_ += CONV_STEP
            assert n_ <= 5000, lab_
            pv_, om_ = retired_power_with(ins_tpr, fp_, n_, nc_fast, own_pmf)
            grid[n_], om_max = pv_, max(om_max, om_)
            if pv_ >= max(CONV_BARS):
                break
        gns = sorted(grid)
        decreases = sum(1 for a_, b_ in zip(gns, gns[1:]) if grid[b_] < grid[a_])
        bars = {}
        for bar in CONV_BARS:
            g_hit = min(x for x in gns if grid[x] >= bar)
            g_prev = g_hit - CONV_STEP
            assert g_prev > CONV_START and grid[g_prev] < bar
            fine = {}
            for m_ in range(g_prev + 1, g_hit + 1):
                fine[m_], om_ = retired_power_with(ins_tpr, fp_, m_, nc_fast, own_pmf)
                om_max = max(om_max, om_)
            first = min(m_ for m_ in fine if fine[m_] >= bar)
            bars[f"{bar:.2f}"] = {"first_grid_n": g_hit, "power_at_first_grid_n": grid[g_hit],
                                  "grid_n_before": g_prev, "power_at_grid_n_before": grid[g_prev],
                                  "first_n_step1": first, "power_at_first_n_step1": fine[first],
                                  "power_at_first_n_step1_minus_1": fine[first - 1] if first - 1 in fine
                                  else grid[g_prev]}
        conv[lab_] = {"instruct_fpr": fp_, "grid": {str(k): v for k, v in grid.items()},
                      "grid_decreases": decreases, "bars": bars, "omitted_mass_bound": om_max}
    assert all(conv[l_]["grid_decreases"] == 0 for l_ in conv), {l_: conv[l_]["grid_decreases"] for l_ in conv}
    cs, cr = conv["source"]["bars"], conv["record"]["bars"]
    # the round-4 checker's printed values (tier1 round 4, finding 1), reproduced at 4 dp
    CHECKER_R4 = {("source", 740): 0.7949, ("source", 750): 0.8042, ("source", 880): 0.8967,
                  ("source", 890): 0.9020, ("record", 2650): 0.7930, ("record", 2700): 0.8011,
                  ("record", 3400): 0.8906, ("record", 3600): 0.9088}
    checker_r4_got = {}
    for (lab_, n_), v_ in CHECKER_R4.items():
        g_ = conv[lab_]["grid"].get(str(n_))
        if g_ is None:
            g_ = retired_power_with(ins_tpr, conv[lab_]["instruct_fpr"], n_, nc_fast, own_pmf)[0]
        checker_r4_got[f"{lab_} n={n_}"] = g_
        assert f"{g_:.4f}" == f"{v_:.4f}", (lab_, n_, g_, v_)
    CHECKER_R4_TABLE = {"recomputed_dpo": (0.0005, 0.0125, 0.1470, 0.6911),
                        "recomputed_instruct_fpr_0p003": (0.0000, 0.0001, 0.0014, 0.0197),
                        "recomputed_instruct_fpr_0p000": (0.0000, 0.0001, 0.0018, 0.0357)}
    for col, vals in CHECKER_R4_TABLE.items():
        assert [f"{r[col]:.4f}" for r in pw_rows] == [f"{v_:.4f}" for v_ in vals], col
    n_checker_r4 = len(CHECKER_R4) + sum(len(v_) for v_ in CHECKER_R4_TABLE.values())
    # the fix's wording names these grid points; assert they are what the scan finds
    assert (cs["0.80"]["first_grid_n"], cs["0.90"]["first_grid_n"], cr["0.80"]["first_grid_n"],
            cr["0.90"]["first_grid_n"]) == (750, 890, 2700, 3500), conv
    assert cs["0.90"]["first_grid_n"] < 1000 <= cr["0.80"]["first_grid_n"]

    def conv_txt(c_):
        return (f"0.80 power at n ≈ {c_['0.80']['first_grid_n']} per arm ({c_['0.80']['power_at_first_grid_n']:.4f}), "
                f"and 0.90 at ≈ {c_['0.90']['first_grid_n']} ({c_['0.90']['power_at_first_grid_n']:.4f})")

    conv_src_txt = conv_txt(cs)
    for l_ in conv:
        for b_, v_ in conv[l_]["bars"].items():
            assert f"{v_['power_at_first_n_step1_minus_1']:.5f}" < b_ + "000" <= f"{v_['power_at_first_n_step1']:.5f}", (l_, b_)
    conv_fine_txt = "; ".join(
        f"{'at 0%' if l_ == 'source' else 'at 0.3%'}: " + ", ".join(
            f"{b_} first reached at n = {conv[l_]['bars'][b_]['first_n_step1']} "
            f"({conv[l_]['bars'][b_]['power_at_first_n_step1']:.5f}; "
            f"{conv[l_]['bars'][b_]['power_at_first_n_step1_minus_1']:.5f} at n = "
            f"{conv[l_]['bars'][b_]['first_n_step1'] - 1})" for b_ in ("0.80", "0.90"))
        for l_ in ("source", "record"))
    w("")
    w("## 6. Record figures that depend on the instruct FPR, recomputed (computed-new)")
    w("")
    w(f"Code: the record's own `clopper_pearson` and `newcombe` (scripts/b2_analyze.py@{COMMIT}) and `binom_pmf` "
      f"(valence_core/stats.py@{COMMIT}), compiled from git show and run in an isolated namespace. An "
      "independent stdlib Clopper-Pearson agrees with the record's at n = 96 for every k = 0..96 "
      f"(max abs difference {cp_agree:.1e}). All probabilities are exact enumerations over the binomial "
      "outcomes; no simulation, no seed.")
    w("")
    w(f"**(a) [g3-A] joint power** (record: 0.9642, {ADDENDUM}@{COMMIT}:147-148, :273; RESULTS.md@{COMMIT}:7173, "
      f":7180, :7189-7194, :7251, :7268-7270; {VALUESCHECK}@{COMMIT} field 1_g3A_power.detail). Rule as the record states it "
      f"(RESULTS.md@{COMMIT}:7266-7268): min CP-lower over {{base, sft}} > max CP-upper over {{dpo, instruct}}; "
      "95% two-sided exact Clopper-Pearson per stage; FPR counts k_s ~ Binomial(96, rate_s) per stage, "
      "independent, all 96 decidable.")
    w("")
    w("| inputs (base / sft / dpo / instruct FPR) | joint power | base > dpo | base > instruct | sft > dpo | "
      "sft > instruct | weakest single pair |")
    w("|---|---|---|---|---|---|---|")
    w(f"| record: .164 / .225 / .000 / .003 | {jp_rec:.5f} | "
      + " | ".join(f"{pairs_rec[f'{a}>{b}']:.5f}" for a, b in PAIRS) + f" | {weak_rec.replace('>', ' > ')} |")
    w(f"| source v1 text: .164 / .225 / .000 / .000 | {jp_src:.5f} | "
      + " | ".join(f"{pairs_src[f'{a}>{b}']:.5f}" for a, b in PAIRS)
      + f" | {' = '.join(k.replace('>', ' > ') for k in weak_src)} (tied) |")
    w(f"| record's printed values | {REC_JOINT} | {REC_PAIR} (labelled 'single weakest pair (base vs dpo)') | "
      "not printed | not printed | not printed | base vs dpo, per the label |")
    w("")
    w(f"At the record's inputs the exact joint power is {jp_rec:.7f}: {jp_rec:.4f} at 4 dp against the printed "
      f"{REC_JOINT} (residual {REC_JOINT - jp_rec:+.4f}) and {jp_rec:.3f} at 3 dp, against the record's own "
      f"claim of exactness at 3 dp ('the exact number is 0.964', RESULTS.md@{COMMIT}:7194; 'the exact figure "
      f"is 0.964', :7269-7270; 'the CONTROL tier's joint figure is 0.964', :7251). So the figure is discrepant "
      "at the record's own stated precision, not only at 4 dp. The base > dpo pair is "
      f"{pair_rec:.4f} against {REC_PAIR} ({REC_PAIR - pair_rec:+.4f}). The record's other printed operands do "
      f"reproduce: Base CP lower at {k_base96}/96 (the expected count .164 x 96, rounded) = {cp_base_lo:.4f} "
      f"(record 0.0984) and DPO CP upper at 0/96 = {cp_dpo_hi:.4f} (record 0.0377), RESULTS.md@{COMMIT}:7189-7190.")
    w("")
    w(f"**The weakest-pair label.** At the record's own inputs the weakest single pair is "
      f"{weak_rec.replace('>', ' > ')} ({pairs_rec[weak_rec]:.4f}), not base > dpo ({pair_rec:.4f}); the joint "
      f"({jp_rec:.4f}) sits just below it. The record's 'single weakest pair (base vs dpo)' "
      f"(RESULTS.md@{COMMIT}:7268; also :7192, 'not the single weakest pair (0.9825)') holds only when the "
      "instruct FPR equals the dpo FPR, as under the source's 0%, where base > dpo and base > instruct tie at "
      f"{weak_src_val:.4f}. At .003, {len(pairs_equal_9825)} of the four pairs equals 0.9825 at 4 dp.")
    w("")
    w("**Cause of the residual: not identified.** The record does not state whether its power was enumerated "
      "or simulated, and no committed code computes it (section 2). Deterministic variants Code tried "
      "(computed-new, none of them the record's stated method):")
    w("")
    w("| variant (all else as above, record inputs) | joint | base > dpo | reproduces both printed values at 4 dp |")
    w("|---|---|---|---|")
    for vr_ in var_rows:
        w(f"| {vr_['variant']} | {vr_['joint']:.5f} | {vr_['base>dpo']:.5f} | "
          f"{'yes' if vr_['reproduces_both_4dp'] else 'no'} |")
    w("")
    w("A simulated (Monte Carlo) estimate would carry sampling error. With the exact values as the truth, its "
      "standard errors and the printed residuals in SE units would be: "
      + "; ".join(f"{m['draws']:,} draws: SE {m['se_pair']:.5f} (pair) / {m['se_joint']:.5f} (joint), "
                  f"residuals {m['pair_residual_in_se']:+.2f} / {m['joint_residual_in_se']:+.2f} SE" for m in mc_rows)
      + ". So both printed values are consistent with a simulation of roughly 10^4 to 10^5 draws. That is a "
        "candidate, not an established cause: no simulation code, draw count or seed is committed. A "
        "simulation error would not be a transcription. Either way 0.9642 is consistent with an instruct input "
        f"of .003 and not with .000, which gives {jp_src:.4f}. Under the source's instruct FPR the joint power "
        f"rises by {jp_src - jp_rec:+.4f}. Both values clear the 0.90 bar the values-check applied "
        f"(RESULTS.md@{COMMIT}:7180). Block :23's consequence for the note is in section 12.")
    w("")
    w(f"**(b) The retired criterion's power** (RESULTS.md@{COMMIT}:7354-7361 table; the same Instruct figures "
      f"at {ADDENDUM}@{COMMIT}:52-53 and RESULTS.md@{COMMIT}:7330-7331). Read as P(Newcombe lower bound > 0) "
      f"at n per arm, all decidable ('perfect controls', RESULTS.md@{COMMIT}:7354), hits ~ Binomial(n, TPR) "
      "and false alarms ~ Binomial(n, FPR) independent; the Newcombe interval is the record's (two 95% "
      f"two-sided CP intervals), and 'lower > 0' is the registered B2 rule (scripts/b2_analyze.py@{COMMIT}:119). "
      f"Outcomes with probability below {PRUNE:.0e} are skipped; the largest skipped mass in any cell is "
      f"{max(r['omitted_mass_bound'] for r in pw_rows):.1e}, an upper bound on the error.")
    w("")
    w("| n per arm | DPO (2.9 vs 0.0): record | recomputed | Instruct (0.9 vs 0.3): record | recomputed | "
      "Instruct (0.9 vs 0.0, source FPR): computed-new |")
    w("|---|---|---|---|---|---|")
    for r in pw_rows:
        w(f"| {r['n_per_arm']} | {r['record_dpo']:.3f} | {r['recomputed_dpo']:.3f} | {r['record_instruct']:.3f} | "
          f"{r['recomputed_instruct_fpr_0p003']:.3f} | {r['recomputed_instruct_fpr_0p000']:.3f} |")
    w("")
    w(f"{n_pw_agree}/8 printed cells agree with the recomputation to three decimals. That supports the reading "
      "above as the record's method (the record does not spell it out), and it shows the table used instruct "
      "FPR .003: at .000 the n = 96 and n = 200 cells would print differently. At the source's instruct FPR "
      "(.000) the Instruct power is "
      + " / ".join(f"{r['recomputed_instruct_fpr_0p000']:.3f}" for r in pw_rows)
      + f" at n = {' / '.join(str(n_) for n_ in table_ns)}, still far below any conventional bar. The record's "
      f"conclusion at RESULTS.md@{COMMIT}:7363 ('Instruct is the binding constraint and it is not close') holds "
      "at both inputs: at every n of the table the Instruct power is below the DPO power (at n = 200, DPO "
      f"{pw200['recomputed_dpo']:.3f} against Instruct {pw200['recomputed_instruct_fpr_0p003']:.3f} at 0.3% and "
      f"{pw200['recomputed_instruct_fpr_0p000']:.3f} at 0%).")
    w("")
    w(f"**The sentence after it (RESULTS.md@{COMMIT}:7363-7364: 'Reaching conventional power there needs n in the "
      "thousands per cell').** :7363 holds at both inputs. :7363-7364's \"n in the thousands per cell\" holds "
      f"only at the transcribed 0.3%. At the source's 0% the registered criterion reaches {conv_src_txt}. At "
      f"0.3% the figures are ≈ {cr['0.80']['first_grid_n']} ({cr['0.80']['power_at_first_grid_n']:.4f}) and "
      f"≈ {cr['0.90']['first_grid_n']} ({cr['0.90']['power_at_first_grid_n']:.4f}). Same rule and inputs as the "
      "table above: P(Newcombe lower > 0), hits ~ Binomial(n, .009), false alarms ~ Binomial(n, FPR), n per arm, "
      f"all decidable. Each '≈' value is the first point at or above the bar on a step-{CONV_STEP} grid from "
      f"n = {CONV_START + CONV_STEP}; the grid rises at every step (0 decreases at either input), and the grid "
      "point before each is below the bar ("
      + "; ".join(f"{conv[l_]['bars'][b_]['grid_n_before']}: {conv[l_]['bars'][b_]['power_at_grid_n_before']:.4f}"
                  for l_ in ("source", "record") for b_ in ("0.80", "0.90"))
      + f"). A step-1 scan between those two grid points gives the first n: {conv_fine_txt}. 'Per cell' is read "
      f"as n per arm, the unit of the table the sentence follows (RESULTS.md@{COMMIT}:7356, 'n / arm'; Code's "
      "reading). The sentence sits under 'Power at their own numbers' (:7354), so as described it should hold at "
      "the source's rates, where 0.90 power needs fewer than 1,000 per arm. Method: the record's binom_pmf "
      "multiplies the integer comb(n, k) by floats, so from n = "
      f"{n_ovf} (the first n at which comb(n, n // 2) exceeds the float range) the record's clopper_pearson "
      f"raises OverflowError (asserted at n = {n_ovf}; it runs at n = {n_ovf - 1}). The scan therefore uses the "
      f"record's newcombe, extracted from scripts/b2_analyze.py@{COMMIT} and compiled with a stdlib "
      "Clopper-Pearson (the record's bisection, with tails summed on the short side) and the stdlib pmf. That "
      f"path agrees with the record's own on all {len(pw_rows) * 3} table cells and on the power at n = {XCHK_N} at the "
      f"source's rates (record path {p750_rec:.6f}); the largest absolute difference over these "
      f"{len(fast_vs_rec)} values is {fast_vs_rec_max:.1e}. The two Clopper-Pearson functions agree at n = 96 for "
      f"every k and at n = {XCHK_N} for every k that power uses (max abs difference {cp_fast_vs_rec:.1e}). The "
      "largest skipped mass in any scanned cell is "
      f"{max(conv[l_]['omitted_mass_bound'] for l_ in conv):.1e}. Block :23's consequence if the note carries "
      "the sentence is in section 12, condition 3.")
    w("")
    w("**How the record describes the Instruct figures.** The record presents them as power at the source's own "
      f"rates: 'power at their own Instruct rates' ({ADDENDUM}@{COMMIT}:52-53), 'Power at Instruct's own "
      f"reported rates' (RESULTS.md@{COMMIT}:7330-7331), and the table under 'Power at their own numbers' "
      f"(RESULTS.md@{COMMIT}:7354-7361). As described, the figures should equal the power at the source's rates. The "
      "record's Instruct cells reproduce at its own transcribed 0.3% "
      f"({sum(r['instruct_agrees_3dp'] for r in pw_rows)}/4), and at the source's rates they differ at 3 dp in "
      f"{len(pw_src_differs)} of 4 cells: "
      + "; ".join(f"n = {r['n_per_arm']}: record {r['record_instruct']:.3f}, at the source's rates "
                  f"{r['recomputed_instruct_fpr_0p000']:.3f}" for r in pw_src_differs)
      + ". The DPO column's inputs (2.9 vs 0.0) equal the v1 text, so its cells stand as described. Block "
        ":23's consequence if the note carries the Instruct figures as at the source's rates is in section 12, "
        "condition 3.")

    # ---------------------------------------------------------------- 7
    Z = NormalDist().inv_cdf
    UNIT_CELL = "per (layer, alpha) configuration"
    UNIT_POOLED = f"pooled per stage over {n_cfg} configurations"
    n_units = ([(sc["per_cell_injected"], sc["per_cell_control"], UNIT_CELL, sc["n_concepts"]) for sc in scen]
               + [(sc["per_stage_pooled_injected"], sc["per_stage_pooled_control"], UNIT_POOLED, sc["n_concepts"])
                  for sc in scen])
    dp_rows = []
    for Ns, Nn, unit, n_c in n_units:
        for label, t, fa in [(s, SOURCE_V1[s]["tpr"], SOURCE_V1[s]["fpr"]) for s in STAGES] + [
                ("instruct, record FPR .003", rec_add["instruct"]["tpr"], rec_add["instruct"]["fpr"])]:
            eh, ef = Decimal(str(t)) * Ns, Decimal(str(fa)) * Nn
            Hc, Fc = half_up(eh), half_up(ef)
            zh, zf = Z((Hc + 0.5) / (Ns + 1)), Z((Fc + 0.5) / (Nn + 1))
            p_own = own_fisher_upper(Hc, Ns - Hc, Fc, Nn - Fc)
            p_rec = rec["fisher_one_sided"](Hc, Ns - Hc, Fc, Nn - Fc)
            assert abs(p_own - p_rec) < 1e-12, (label, p_own, p_rec)
            row = {"n_injected": Ns, "n_control": Nn, "unit": unit, "n_concepts_assumed": n_c,
                   "point": label, "tpr": t, "fpr": fa,
                   "expected_hits": float(eh), "expected_fa": float(ef), "hits": Hc, "false_alarms": Fc,
                   "dprime_loglinear": zh - zf, "criterion_c": -(zh + zf) / 2, "fisher_one_sided_p": p_own,
                   "ties_at_half": [x for x, e in (("hits", eh), ("false_alarms", ef))
                                    if e - int(e) == Decimal("0.5")]}
            if label.startswith("instruct, record") and Ns == 800:
                zfc = Z((float(ef) + 0.5) / (Nn + 1))
                zhc = Z((float(eh) + 0.5) / (Ns + 1))
                row["dprime_unrounded_counts"] = zhc - zfc
            dp_rows.append(row)
    seat = {"base": -1.9, "sft": -0.3, "dpo": 0.6, "instruct": 0.15}
    seat_p = {"dpo": (0.11, 2), "instruct": (0.5, 1)}  # (seat's value, its decimals)
    r800 = {r["point"]: r for r in dp_rows if r["n_injected"] == 800}
    r5k = {r["point"]: r for r in dp_rows if r["n_injected"] == 5000}
    r16k = {r["point"]: r for r in dp_rows if r["n_injected"] == 16000}
    r100k = {r["point"]: r for r in dp_rows if r["n_injected"] == 100000}
    assert r16k["base"]["unit"] == UNIT_POOLED and r800["base"]["unit"] == UNIT_CELL

    def d_agrees(s, v):
        return abs(round(v, 2 if s == "instruct" else 1) - seat[s]) < 1e-9

    def p_agrees(s, v):
        return abs(round(v, seat_p[s][1]) - seat_p[s][0]) < 1e-9

    seat_ok = {s: d_agrees(s, r800[s]["dprime_loglinear"]) for s in STAGES}
    seat_ok_pooled = {s: d_agrees(s, r16k[s]["dprime_loglinear"]) for s in STAGES}
    seat_check = []
    for s in STAGES:
        seat_check.append({"figure": f"theirs {s} d' ~ {seat[s]:+}", "seat": seat[s],
                           "at_800_80_per_configuration": r800[s]["dprime_loglinear"],
                           "agrees_at_seat_precision_800_80": seat_ok[s],
                           "at_16000_1600_pooled_same_premise": r16k[s]["dprime_loglinear"],
                           "agrees_at_seat_precision_16000_1600": seat_ok_pooled[s]})
    for s in ("dpo", "instruct"):
        seat_check.append({"figure": f"theirs {s} one-sided Fisher p ~ {seat_p[s][0]}", "seat": seat_p[s][0],
                           "at_800_80_per_configuration": r800[s]["fisher_one_sided_p"],
                           "agrees_at_seat_precision_800_80": p_agrees(s, r800[s]["fisher_one_sided_p"]),
                           "at_16000_1600_pooled_same_premise": r16k[s]["fisher_one_sided_p"],
                           "agrees_at_seat_precision_16000_1600": p_agrees(s, r16k[s]["fisher_one_sided_p"])})
    for c_ in seat_check:
        c_["disposition"] = ("arithmetic confirmed under the seat's premise (800/80, a per-configuration n applied to "
                             "rates pooled over 20 configurations)" if c_["agrees_at_seat_precision_800_80"]
                             else "NOT reproduced at the seat's own premise")
        c_["disposition"] += ("; it also holds at the pooled n under the same premise (16000/1600)"
                              if c_["agrees_at_seat_precision_16000_1600"] else
                              "; at the pooled n under the same premise (16000/1600) the figure is "
                              + (f"{c_['at_16000_1600_pooled_same_premise']:+.3f}" if "d'" in c_["figure"]
                                 else pfmt(c_["at_16000_1600_pooled_same_premise"])))
    seat_all_800 = all(c_["agrees_at_seat_precision_800_80"] for c_ in seat_check)
    for k_, (h_, fa_, d_, p_) in CHECKER_R2_POOLED.items():
        r_ = r16k[k_]
        assert (r_["hits"], r_["false_alarms"]) == (h_, fa_) and f"{r_['dprime_loglinear']:.3f}" == f"{d_:.3f}", (k_, r_)
        if p_ is not None:
            pr_ = r_["fisher_one_sided_p"]
            assert (f"{pr_:.1e}" == p_) if "e" in p_ else (f"{pr_:.4f}" == p_), (k_, pr_, p_)
    checker_r2_agree = len(CHECKER_R2_POOLED)
    both_units = [c_ for c_ in seat_check
                  if c_["agrees_at_seat_precision_800_80"] and c_["agrees_at_seat_precision_16000_1600"]]
    ri16 = r16k["instruct, record FPR .003"]
    ri100 = r100k["instruct, record FPR .003"]
    ri5 = r5k["instruct, record FPR .003"]
    # read-only cross-check against the N2 item's ROC JSON (another item's working-tree output; non-fatal)
    n2_cmp = {"path": N2_ROC, "status": "not compared",
              "sha256_note": "not recorded (round 3): the N2 raw records this JSON's sha256, so recording N2's here "
                        "would form a cycle in which neither sha could stay valid; the compared values are "
                        "recorded instead"}
    try:
        with open(os.path.join(REPO, N2_ROC), "rb") as fh:
            n2_bytes = fh.read()
        n2j = json.loads(n2_bytes)
        n2_dsc = n2j["design_seat_check"]
        mine = {("base", "d"): r16k["base"]["dprime_loglinear"], ("sft", "d"): r16k["sft"]["dprime_loglinear"],
                ("dpo", "d"): r16k["dpo"]["dprime_loglinear"], ("dpo", "p"): r16k["dpo"]["fisher_one_sided_p"],
                ("instruct", "d"): r16k["instruct"]["dprime_loglinear"],
                ("instruct", "p"): r16k["instruct"]["fisher_one_sided_p"]}
        n2_vals = {}
        for e in n2_dsc:
            f_ = e["figure"].lower()
            if not f_.startswith("theirs "):
                continue
            st_ = f_.split()[1]
            kind = "d" if "d'" in f_ else "p"
            n2_vals[(st_, kind)] = e["computed_at_pooled_n_same_premise"]
        cmp_ok = {k: (k in n2_vals and math.isclose(v, n2_vals[k], rel_tol=1e-9, abs_tol=1e-12))
                  for k, v in mine.items()}
        n2_var = next(p_ for p_ in n2j["points"] if p_.get("dataset") == "theirs"
                      and "record transcribes" in p_.get("arm", ""))["pooled_same_premise"]
        var_ok = (n2_var["hits"] == ri16["hits"] and n2_var["fa"] == ri16["false_alarms"]
                  and math.isclose(n2_var["dprime_loglinear"], ri16["dprime_loglinear"], rel_tol=1e-9)
                  and math.isclose(n2_var["fisher_p_one_sided"], ri16["fisher_one_sided_p"], rel_tol=1e-9))
        n2_cmp.update({"status": "compared", "seat_figures_at_pooled_agree": sum(cmp_ok.values()),
                       "seat_figures_compared": len(cmp_ok), "instruct_record_fpr_pooled_agrees": var_ok,
                       "compared_values": [{"figure": f"{st_} {'dprime' if kind == 'd' else 'one-sided Fisher p'} "
                                                      "at 16000/1600 (pooled, eight concepts)",
                                            "this_item": v, "n2_roc_json": n2_vals.get((st_, kind)),
                                            "agrees_rel_1e-9": cmp_ok[(st_, kind)]}
                                           for (st_, kind), v in mine.items()]
                       + [{"figure": "instruct at the record's FPR .003, 16000/1600: hits, false alarms, dprime, p",
                           "this_item": [ri16["hits"], ri16["false_alarms"], ri16["dprime_loglinear"],
                                         ri16["fisher_one_sided_p"]],
                           "n2_roc_json": [n2_var["hits"], n2_var["fa"], n2_var["dprime_loglinear"],
                                           n2_var["fisher_p_one_sided"]],
                           "agrees_rel_1e-9": var_ok}]})
    except (OSError, KeyError, ValueError, StopIteration, TypeError) as exc:
        n2_cmp["status"] = f"not compared ({type(exc).__name__})"
    w("")
    w("## 7. The source's points under an assumed n: d', c and Fisher (computed-new; context for N2(v))")
    w("")
    w("N2(v)'s own output is its own raw. This section checks the design seat's arithmetic for the source's "
      "points (block :34: base d' ~ -1.9, SFT ~ -0.3, DPO ~ +0.6 with p ~ .11, instruct ~ +0.15 with p ~ .5, "
      "under an assumed 800/80 per configuration) and whether the instruct-FPR correction changes it. "
      "Counts = rate x n, rounded half-up on the exact decimal product (expected counts printed; a .5 tie is "
      "flagged). d' is log-linear: z((H + 1/2)/(N_s + 1)) - z((FA + 1/2)/(N_n + 1)); c = -(z_H + z_FA)/2. "
      "p is a one-sided Fisher exact test on [[H, N_s - H], [FA, N_n - FA]], the hypergeometric upper tail "
      "P(X >= H) (excess hits over false alarms); this script's stdlib Fisher equals the record's "
      f"`fisher_one_sided` (valence_core/stats.py@{COMMIT}) on every row.")
    w("")
    w(f"**The unit.** 800/80 (like 5000/500) is one (layer, alpha) configuration's n. Every source rate is "
      f"pooled over all {n_cfg} configurations (section 4), so a test of those rates under the same premise uses "
      f"the pooled per-stage n: {scen[0]['per_stage_pooled_injected']}/{scen[0]['per_stage_pooled_control']} "
      f"with the record's eight concepts, {scen[1]['per_stage_pooled_injected']}/"
      f"{scen[1]['per_stage_pooled_control']} with the code's fifty. The block's 800/80 is therefore a "
      "per-cell n applied to a pooled rate. Both units are tabulated. Pooled counts still treat trials "
      "clustered by configuration and concept as independent, so no row is an exact test of the source's "
      "aggregate. The source gives no n (section 5), so every number here carries an assumption, not the "
      "source.")
    w("")
    w("| assumed n inj / ctl | unit | point | TPR / FPR | expected H / FA | H / FA | d' | c | one-sided Fisher p |")
    w("|---|---|---|---|---|---|---|---|---|")
    for r in dp_rows:
        tie = (" (tie at .5: " + ", ".join(r["ties_at_half"]) + ")") if r["ties_at_half"] else ""
        w(f"| {r['n_injected']} / {r['n_control']} | {r['unit']} ({r['n_concepts_assumed']} concepts) | "
          f"{r['point']} | {r['tpr']:.3f} / {r['fpr']:.3f} | "
          f"{r['expected_hits']:.2f} / {r['expected_fa']:.2f}{tie} | {r['hits']} / {r['false_alarms']} | "
          f"{r['dprime_loglinear']:+.3f} | {r['criterion_c']:+.3f} | {pfmt(r['fisher_one_sided_p'])} |")
    ri8 = r800["instruct, record FPR .003"]

    def pt(r):
        return (f"{r['hits']}/{r['false_alarms']} (d' {r['dprime_loglinear']:+.3f}, p {pfmt(r['fisher_one_sided_p'])})")

    w("")
    w("**The seat's arithmetic, with its premise.** At 800/80 the seat's arithmetic is reproduced: "
      + "; ".join(f"{s} d' {r800[s]['dprime_loglinear']:+.3f} (seat {seat[s]:+}; "
                  f"{'agrees' if seat_ok[s] else 'DIFFERS'} at the seat's precision)" for s in STAGES)
      + f"; DPO p = {r800['dpo']['fisher_one_sided_p']:.4f} (seat ~ .11); instruct p = "
      f"{r800['instruct']['fisher_one_sided_p']:.4f} (seat ~ .5). That confirms the arithmetic under the "
      "premise, not the points: under the same eight-concept premise the pooled per-stage n is "
      f"{ri16['n_injected']}/{ri16['n_control']}, at which "
      + "; ".join(f"{c_['figure'].replace('theirs ', '')}: "
                  + (f"{c_['at_16000_1600_pooled_same_premise']:+.3f}" if "d'" in c_["figure"]
                     else pfmt(c_["at_16000_1600_pooled_same_premise"]))
                  + f" ({'agrees' if c_['agrees_at_seat_precision_16000_1600'] else 'does not agree'})"
                  for c_ in seat_check)
      + f". Holding at both units: {len(both_units)} of {len(seat_check)} figures ("
      + (", ".join(c_["figure"].replace("theirs ", "") for c_ in both_units) or "none") + ").")
    w("")
    w("**The instruct-FPR correction.** At 800/80 the instruct point is "
      f"{r800['instruct']['hits']}/{r800['instruct']['false_alarms']} under the source's 0% and "
      f"{ri8['hits']}/{ri8['false_alarms']} under the record's 0.3% (0.003 x 80 = {ri8['expected_fa']:.2f} "
      "rounds to 0), so the correction does not change the per-configuration arithmetic. With the unrounded "
      f"expected counts (7.2 / 0.24) the log-linear d' would be {ri8['dprime_unrounded_counts']:+.3f}, so the "
      "seat's +0.15 implies integer counts with zero false alarms (Code's inference; the block states no "
      f"rounding rule). At the pooled n under the same premise the correction does change the point: "
      f"{pt(ri16)} under the record's 0.3% against {pt(r16k['instruct'])} under the source's 0% "
      f"(0.003 x {ri16['n_control']} = {ri16['expected_fa']:.1f} rounds to {ri16['false_alarms']}). Likewise at "
      f"5000/500 ({pt(ri5)} against {pt(r5k['instruct'])}) and at 100000/10000 ({pt(ri100)} against "
      f"{pt(r100k['instruct'])}). N2(v) must choose and declare both the concept count and the unit (per "
      "configuration or pooled).")
    w("")
    if n2_cmp["status"] == "compared":
        w(f"**Consistency with the N2 raw** (a read-only, non-binding check of `{N2_ROC}`, another item's "
          f"working-tree output): its pooled (16000/1600) values for the seat's figures agree with this section's "
          f"in {n2_cmp['seat_figures_at_pooled_agree']} of {n2_cmp['seat_figures_compared']} (relative tolerance "
          "1e-9), and its pooled instruct point at the record's 0.3% "
          f"{'agrees' if n2_cmp['instruct_record_fpr_pooled_agrees'] else 'DIFFERS'} (counts, d' and p). The "
          "values compared are in this item's JSON (`source_points_dprime_computed_new.n2_consistency_check`). "
          "That file's sha256 is not recorded here: the N2 raw records this item's JSON sha256, so the binding "
          "cross-reference runs from N2 to this item, and recording both would form a cycle in which neither "
          "sha could stay valid.")
    else:
        w(f"**Consistency with the N2 raw:** {n2_cmp['status']} (`{N2_ROC}`).")

    # ---------------------------------------------------------------- 8
    w("")
    w("## 8. Lineage")
    w("")
    w("| stage | source key | source HF repo (code, no revision) | record repo (manifest) | match | record revision |")
    w("|---|---|---|---|---|---|")
    lin_match = 0
    lin_rows = {}
    for s in STAGES:
        key, repo = SOURCE_CODE["model_name_map"][s]
        rrepo, rrev = manifest[s]["repo"], manifest[s]["revision"]
        m = rrepo == repo
        lin_match += m
        lin_rows[s] = {"source_key": key, "source_repo": repo, "record_repo": rrepo,
                       "record_revision": rrev, "match": m}
        w(f"| {s} | {key} | {repo} | {rrepo} | {'yes' if m else 'NO'} | {rrev} |")
    w("")
    w(f"Repo-level match {lin_match}/4. The record side is read from {MANIFEST}@{COMMIT} (fields `repo`, "
      "`revision`), a committed artifact, so our four acquired repos and revisions are reproduced. The source "
      "side is Code's WebFetch reading of src/model_utils.py at 5d5d9b4 (section 3), not a committed artifact, "
      f"so the match itself is the record's prose claim (RESULTS.md@{COMMIT}:12565-12569, log-only) with this "
      "comparison as a computed-new check (section 0 gives the two rows). The paper names the model as "
      "OLMo-3.1-32B at base, SFT, DPO and instruct and gives no HF ids. The source code pins no revision, so a "
      "revision-level match cannot be established from the source.")

    # ---------------------------------------------------------------- 9
    dec = {
        "temperature": {"paper_v1": "1.0 (Appendix A, all generations unless otherwise specified)",
                        "code_5d5d9b4": d["DEFAULT_TEMPERATURE"]},
        "top_p": {"paper_v1": "1.0 (Appendix A, stated as the default sampling setting)",
                  "code_5d5d9b4": "not passed to generate"},
        "top_k": {"paper_v1": "50 (Appendix A, stated as the default sampling setting)",
                  "code_5d5d9b4": "not passed to generate"},
        "do_sample": {"paper_v1": None, "code_5d5d9b4": "temperature > 0"},
        "max_new_tokens": {"paper_v1": None, "code_5d5d9b4": d["DEFAULT_MAX_TOKENS"]},
        "trials_per_concept_per_cell_injected": {
            "paper_v1": None,
            "code_5d5d9b4": f"{inj_per_concept} (10 trial numbers x 10 samples)"},
        "trials_per_concept_per_cell_control": {
            "paper_v1": None,
            "code_5d5d9b4": f"{ctl_per_concept} (10 trial numbers x 1 sample)"},
        "seed_policy": {"paper_v1": None,
                        "code_5d5d9b4": "one global --seed (default 42) set once in main() for random, numpy, "
                                        "torch and CUDA; no per-trial seeds"},
        "prompt_format": {"paper_v1": SOURCE_V1_PROMPT_TEXT,
                          "code_5d5d9b4": "olmo_base: plain-text 'User:' / 'Assistant:' turns, no chat template "
                                          "(build_base_model_prompt); post-trained stages: the tokenizer's chat "
                                          "template. The bare 'Tell me about {word}' template is the base "
                                          "model's concept-vector extraction prompt, not the trial prompt"},
        "record_declared_match": f"{ADDENDUM}@{COMMIT}:89-96 (temperature 1.0, max_new_tokens 100, our "
                                 "per-trial seeds live and declared) -- log-only; N2(i) carries our side",
    }
    w("")
    w("## 9. Decoding, for N2(i)'s side-by-side (source side only)")
    w("")
    w("| parameter | paper v1 | released code at 5d5d9b4 |")
    w("|---|---|---|")
    for k, v in dec.items():
        if isinstance(v, dict):
            w(f"| {k} | {v['paper_v1'] if v['paper_v1'] is not None else 'not stated'} | {v['code_5d5d9b4']} |")
    w("")
    w(f"Paper v1 on decoding: {SOURCE_V1_DECODING_TEXT}. Whether the v1 OLMo runs used the code's defaults "
      "(seed 42, 100 tokens) is not stated. Our side as declared: " + dec["record_declared_match"] + ".")

    # ---------------------------------------------------------------- 10
    w("")
    w("## 10. Answers to N2(vi)")
    w("")
    w("1. **Configuration.** None of the four per-stage values comes from a single (layer, alpha) "
      f"configuration. Each is an aggregate over L in {V1_FIG21_LAYERS} x alpha in {V1_FIG21_ALPHAS} "
      f"({n_cfg} configurations), per v1 Figure 21's caption, matching {ADDENDUM}@{COMMIT}:39. The released "
      "code's per-model summary pools all trials across cells; that the figure used that pooled summary is "
      "Code's inference, not a source statement.")
    w("2. **n injected / n control per cell.** Not stated by the source, for any stage. Under the code's "
      "defaults the per-cell counts are 100 x n_concepts injected and 10 x n_concepts control. n_concepts is "
      "not stated for v1: 8 gives 800 / 80, the code's default 50 gives 5000 / 500 (section 5). The eight is "
      "our own B2 registration. These are per-configuration n; the source's rates are pooled over 20 "
      "configurations, so the pooled per-stage n under the same premises is 16000 / 1600 or 100000 / 10000 "
      "(sections 5 and 7).")
    w(f"3. **Table or figure.** The record does not state its recovery method: RESULTS.md@{COMMIT}:7326-7327 "
      "says only that the values were recovered from the paper (Appendix C, Fig 21). The source carries the "
      "values in prose in v1 Appendix C, in the paragraph that describes Figure 21, and in no table. The "
      f"record's values equal that prose to printed precision in {n_tpr + n_fpr} of 8 cells, which supports "
      "text-reading; the instruct FPR slip (section 4) is consistent with mis-transcribing that prose. This "
      "audit digitized nothing.")
    w("4. **Best-of-grid.** No. Each value is the aggregate over the full grid. The addendum notes "
      f"({ADDENDUM}@{COMMIT}:212-213) that the aggregate is diluted by past-optimum strengths.")
    w("5. **Per-stage TPR in text.** Yes, all four stages, in v1 only (quotation and paraphrases in section 3). "
      "v2-v5 carry none in text.")
    w("6. **Per-stage FPR in text (v1).** base 16.4%, SFT 22.5%, DPO 0%, instruct 0%. The record's instruct "
      "0.3% equals the v1 instruct introspection rate; Code reads it as a transcription slip, not established, "
      "since Figure 21 was not digitized (section 4).")
    w(f"7. **Lineage.** The four HF repos in the source code, as Code read it, equal the record's manifest, "
      f"{lin_match}/4. No revision is pinned on the source side.")
    w("")
    w("**For the note (Code's suggestion; not applied; the design seat drafts).** The sentence can say what "
      "the source's text reads: arXiv:2603.21396v1, Appendix C (prose describing Fig. 21), per-stage TPR "
      "0.1% / 14.9% / 2.9% / 0.9% and FPR 16.4% / 22.5% / 0% / 0% for base / SFT / DPO / instruct, each "
      "pooled over 5 layers x 4 strengths, n not stated; later versions (v2-v5) show the comparison at L = 25 "
      "without per-stage numbers in text. If F2 plots the source's instruct point, its FPR is 0 per the text. "
      "Any d' or p for the source's points names its assumed n and unit (section 7). The figures this raw finds "
      "discrepant carry block :23 consequences if the note carries them (section 12).")

    # ---------------------------------------------------------------- locator helpers
    def loc_r(*lines):
        return f"RESULTS.md@{COMMIT}:" + ", :".join(str(x) for x in lines)

    def loc_a(*lines):
        return f"{ADDENDUM}@{COMMIT}:" + ", :".join(str(x) for x in lines)

    def cloc(key):
        inc = CARRIERS[key][2]
        parts = []
        if inc.get(ADDENDUM):
            parts.append(loc_a(*inc[ADDENDUM]))
        if inc.get(RESULTS):
            parts.append(loc_r(*inc[RESULTS]))
        if other_by_key[key]:
            parts.append("other tracked: " + ", ".join(f"{q.split(':')[0]}@{COMMIT}:{q.split(':')[1]}"
                                                       for q in other_by_key[key]))
        return "; ".join(parts)

    # round 3: the n and its ratio (finding 6): ours as run, and the ratio under each premise and unit
    our_n = 24  # RESULTS.md@bbc9ffe:7440 'our 24/24'; :7358 '24 (as run)' (anchors asserted)
    ratio_rows = []
    for sc in scen:
        ratio_rows.append({"n_concepts": sc["n_concepts"], "our_injected_per_stage_as_run": our_n,
                           "their_per_configuration": sc["per_cell_injected"],
                           "their_pooled_per_stage": sc["per_stage_pooled_injected"],
                           "ratio_their_configuration_to_our_stage": sc["per_cell_injected"] / our_n,
                           "ratio_their_stage_to_our_stage": sc["per_stage_pooled_injected"] / our_n})
    assert round(ratio_rows[0]["ratio_their_configuration_to_our_stage"]) == 33
    r8, r50 = ratio_rows

    def rfmt(x):
        return f"{x:.1f}"

    ratio_txt = (f"{r8['their_per_configuration']}/{our_n} = {rfmt(r8['ratio_their_configuration_to_our_stage'])} "
                 "(one of their configurations against our whole stage, the record's unit); per stage under the "
                 f"same premise {r8['their_pooled_per_stage']}/{our_n} = "
                 f"{rfmt(r8['ratio_their_stage_to_our_stage'])}; with the code's 50 concepts "
                 f"{rfmt(r50['ratio_their_configuration_to_our_stage'])} and "
                 f"{rfmt(r50['ratio_their_stage_to_our_stage'])}")
    joint_carriers = cloc("joint")
    # round 4: row 19's other tracked copy (round-4 grep) and the new 'thousands' row, appended as row 24 so that
    # rows 1-23 keep the numbers the earlier rounds' tables cite
    r19_others = [p for p in GREP_R4["retired_instruct_power"][2] if not p.startswith((RESULTS, ADDENDUM))]
    assert r19_others == ["scripts/b2r_analyze.py:16"], r19_others
    R19_OTHER = (f"{r19_others[0].split(':')[0]}@{COMMIT}:{r19_others[0].split(':')[1]} (docstring, 0.000 at n=48; "
                 "unchanged at either rate)")
    assert list(GREP_R4["thousands"][2]) == [f"{RESULTS}:7364"]
    ROW_THOUSANDS = 24

    # ---------------------------------------------------------------- notes
    notes = [
        f"Version referent: the record cites 'arXiv:2603.21396 Appendix C, Fig 21' with no version "
        f"({ADDENDUM}@{COMMIT}:35-36, :39; RESULTS.md@{COMMIT}:7327, :7343). That structure exists only in v1 "
        "(2026-03-22). v2 (2026-04-10) to v5 (2026-06-10) do not carry the four per-stage values in text. In "
        "v4, Figure 21 is a different OLMo-stage figure (Appendix D.1, L = 19 and L = 22), so the unversioned "
        "citation is actively ambiguous. The note should cite v1 explicitly.",
        f"Instruct FPR: the record carries 0.3% ({ADDENDUM}@{COMMIT}:46; RESULTS.md@{COMMIT}:6999 'theirs' "
        f"0.003; RESULTS.md@{COMMIT}:7341). The v1 text gives instruct FPR 0% and introspection rate 0.3%. The "
        "instruct sensitivity is then +0.9 pp, not +0.6 pp; the +0.6 pp appears at "
        f"{ADDENDUM}@{COMMIT}:46, RESULTS.md@{COMMIT}:7330 and :7341, and the scripts/b2r_analyze.py@{COMMIT}:15 "
        "docstring. Other tracked copies of the 0.003: HANDOFF-2026-08-25.md@bbc9ffe:60 and the self-test "
        "fixture at scripts/b2r_analyze.py@bbc9ffe:161 (section 2, carrier search). Code's reading: a "
        "transcription slip of the v1 prose; not established, because the record says it recovered the values "
        f"from 'Appendix C, Fig 21' (RESULTS.md@{COMMIT}:7327) and Figure 21 is an image that was not digitized. "
        "On that reading it is a referent note, not a STOP, and needs no analyzer change; block :23's consequence "
        "if the note carries it is in section 12. The [g3-A] verdict "
        "was computed on our data and is unaffected. Pre-data sizing figures that used the instruct FPR, each "
        "recomputed in section 6: (1) the retired criterion's power at Instruct's rates, at "
        f"{ADDENDUM}@{COMMIT}:52-53 (0.000 at n = 48, 0.020 at n = 200), RESULTS.md@{COMMIT}:7330-7331 (0.000 / "
        f"0.001 / 0.020 at n = 48 / 96 / 200) and the Instruct column of the table at RESULTS.md@{COMMIT}:"
        f"7356-7361 ('0.9 vs 0.3'); other tracked: {R19_OTHER}. All reproduce at .003 (section 6b). At .000 "
        "the Instruct power is "
        + " / ".join(f"{r['recomputed_instruct_fpr_0p000']:.3f}" for r in pw_rows)
        + f" at n = {' / '.join(str(n_) for n_ in table_ns)}. The record describes these as power at the "
        "source's own rates ('their own Instruct rates', 'Instruct's own reported rates', 'their own numbers'; "
        "section 6b), so as described the "
        + " and ".join(f"n = {r['n_per_arm']}" for r in pw_src_differs) + " cells are discrepant ("
        + "; ".join(f"{r['record_instruct']:.3f} against {r['recomputed_instruct_fpr_0p000']:.3f}"
                    for r in pw_src_differs)
        + f"). The sentence after the table, RESULTS.md@{COMMIT}:7363-7364 ('n in the thousands per cell' for "
        "conventional power at Instruct), holds only at .003: at .000 the registered criterion reaches "
        f"{conv_src_txt}, against ≈ {cr['0.80']['first_grid_n']} ({cr['0.80']['power_at_first_grid_n']:.4f}) and "
        f"≈ {cr['0.90']['first_grid_n']} ({cr['0.90']['power_at_first_grid_n']:.4f}) at .003 (section 6b; row "
        f"{ROW_THOUSANDS}). Block :23's consequence for both is in section 12, condition 3. (2) The [g3-A] joint "
        "power 0.9642 / "
        f"0.964 (every carrier, as in section 0: {joint_carriers}; also {VALUESCHECK}@{COMMIT} "
        "1_g3A_power.detail; the arithmetic passages around them are ADDENDUM :147-148 and RESULTS "
        f":7189-7194, :7266-7270). The exact value at the record's "
        f"inputs is {jp_rec:.4f} ({jp_rec:.3f} at 3 dp; residual {REC_JOINT - jp_rec:+.4f}, cause not "
        f"identified), and at .000 it is {jp_src:.4f}. Both stay above the 0.90 bar. "
        f"(3) The b2r_analyze self-test fixture uses .164/.225/.000/.003 (scripts/b2r_analyze.py@{COMMIT}:"
        "160-162). It is a synthetic case, not a verdict input, and is not touched (read-only).",
        "The block's N2(v) design-seat arithmetic for the source's points (block :34) is checked in section 7. "
        "At the seat's premise, 800/80, every figure reproduces at the seat's precision: base "
        f"{r800['base']['dprime_loglinear']:+.3f}, SFT {r800['sft']['dprime_loglinear']:+.3f}, DPO "
        f"{r800['dpo']['dprime_loglinear']:+.3f} (one-sided Fisher p = {r800['dpo']['fisher_one_sided_p']:.4f}), "
        f"instruct {r800['instruct']['dprime_loglinear']:+.3f} (p = {r800['instruct']['fisher_one_sided_p']:.4f}). "
        "That confirms the arithmetic under the premise, not the points. The seat's 800/80 is a per-(layer, "
        f"alpha) n, but the source's rates are pooled over {n_cfg} configurations. At the pooled per-stage n "
        f"under the same eight-concept assumption ({ri16['n_injected']}/{ri16['n_control']}) the points are "
        f"base {r16k['base']['dprime_loglinear']:+.3f}, SFT {r16k['sft']['dprime_loglinear']:+.3f}, DPO "
        f"{r16k['dpo']['dprime_loglinear']:+.3f} (p {pfmt(r16k['dpo']['fisher_one_sided_p'])}), instruct "
        f"{r16k['instruct']['dprime_loglinear']:+.3f} (p {pfmt(r16k['instruct']['fisher_one_sided_p'])}). There "
        "the FPR correction does change the instruct point (d' "
        f"{ri16['dprime_loglinear']:+.3f} -> {r16k['instruct']['dprime_loglinear']:+.3f}; one-sided Fisher p "
        f"{pfmt(ri16['fisher_one_sided_p'])} -> {pfmt(r16k['instruct']['fisher_one_sided_p'])}). At 800/80 it "
        f"does not ({r800['instruct']['hits']}/{r800['instruct']['false_alarms']} under both, because 0.24 "
        "expected false alarms round to 0). N2(v) must choose and declare both the concept count and the unit "
        "(per configuration or pooled).",
        "n: the block's '800/80 per configuration' and the record's '~800 injected / ~80 control' (every "
        f"carrier, section 2: {cloc('n800')}) assume eight concepts, which is "
        f"our own B2 registration ({B2C}@{COMMIT} selection_for_B2.registered_n = 8), not a source count "
        f"({B2C}@{COMMIT} n_canonical = 50, the 50-entry list its provenance cites at "
        "experiments/01_concept_injection.py:58). The source states no n. The OLMo experiment's own default "
        "concept list (experiments/03_behavioral_robustness.py, defined in that file) has 50 entries, giving "
        "5000 / 500 per cell and 100000 / 10000 per stage pooled (section 5). As the record's "
        f"inference with its premise (RESULTS.md@{COMMIT}:7438-7440), 800/80 is log-only; as a statement of the "
        "source's n it is not found, and under block :23 a note sentence presenting it as the source's n is cut "
        "(section 0). The same holds for figures derived from it. The ratio '~33×' "
        f"({cloc('ratio33')}) is {ratio_txt}, so it depends on both premise and unit. The power row "
        f"'theirs, OLMo cell (~800/80)' (RESULTS.md@{COMMIT}:7485, :7500-7502) is computed at that n; this item "
        "does not recompute it. N2(v)'s tests on the source points depend on the concept count and the unit "
        "and must name both.",
        f"Layers: {ADDENDUM}@{COMMIT}:66 says 'L_M stands on the code rule and the paper's caption'. The code "
        f"rule gives int(64 x 0.7) = 44 at the fourth slot, but the v1 caption gives 45 there, so the 'and the "
        "paper's caption' support does not hold at that slot. Neither int() nor round() of the default "
        f"fractions yields the caption's list ({idx0} and {ridx0} against {V1_FIG21_LAYERS}), while the "
        f"README's absolute list does ({readme_eq_caption}/5; section 5). Recorded, not adjudicated; L_M = 44 "
        "is not touched.",
        "README: besides the layer-fraction issue the record already notes (RESULTS.md@bbc9ffe:7393-7398), "
        "the README's -m keys (olmo_32b_*) are not in the script's argparse choices, so the README command "
        f"would be refused as written. Its layer list still equals the v1 caption ({readme_eq_caption}/5).",
        f"Values-check wording: {ADDENDUM}@{COMMIT}:274 says the section 0.2/0.6 tables are 'exact against paper "
        f"and cache'. RESULTS.md@{COMMIT}:7181 records the item as 'PASS -- exact' and {VALUESCHECK}@{COMMIT} "
        f"2_tables.detail as '§0.2 exact'. Against the v1 text, {n_tpr + n_fpr} of the table's 8 rate cells "
        "are exact; the instruct FPR is the exception.",
        "Method limits: the source was read through WebFetch's processed rendering. Each v1 Appendix C "
        "sentence came back verbatim in two fetches (one omitting the base sentence's opening clause). The v2-v5 "
        "Table 3 values came back the same in three fetches (v2, v4, v5). No figure image was fetched or "
        "digitized. One v4 fetch returned an off-target answer and was re-run with a rephrased prompt. "
        "The fixer pass's four reads and round 2's two reads (each made twice, agreeing) are listed in section 3, "
        "and so are round 3's two reads of 03_behavioral_robustness.py (the second declined to copy the "
        "list in full, so only its count, end entries and import status corroborate the first).",
        f"Not checked: the note's sentence and F2's points. The note draft and the F1/F2 SVGs are not on this "
        f"machine ({PREFLIGHT}@{COMMIT}:{pre_missing['RESEARCH-NOTE-v0_2-draft.md']}, "
        f":{pre_missing['*F1*.svg']}-{pre_missing['*F2*.svg']}: MISSING), so whether the note 'carries 0.001 / "
        "0.149 / 0.029 / 0.009' (block :35) and what F2 plots for the source's instruct FPR were not read.",
        f"Weakest pair: the record labels base vs dpo the 'single weakest pair' at 0.9825 (RESULTS.md@{COMMIT}:7268; "
        f":7192). At the record's own inputs the weakest pair is {weak_rec.replace('>', ' > ')} "
        f"({pairs_rec[weak_rec]:.4f}), not base > dpo ({pair_rec:.4f}). The label holds only when the instruct "
        "FPR equals the dpo FPR, as under the source's 0% (section 6a). The record's 'base binds, not sft' "
        "(RESULTS.md@bbc9ffe:7193, :7270) is unaffected: both base pairs are below both sft pairs at either input.",
        "Exactness claims: the record calls 0.964 'the exact number' and 'the exact figure' "
        f"(RESULTS.md@{COMMIT}:7194, :7269-7270) and states 'joint figure is 0.964' at :7251. Exact enumeration "
        f"gives {jp_rec:.7f} at its inputs, {jp_rec:.3f} at 3 dp (section 6a).",
    ]
    assert max(pairs_rec["base>dpo"], pairs_rec["base>instruct"]) < min(pairs_rec["sft>dpo"], pairs_rec["sft>instruct"])
    assert max(pairs_src["base>dpo"], pairs_src["base>instruct"]) < min(pairs_src["sft>dpo"], pairs_src["sft>instruct"])
    w("")
    w("## 11. Referent notes (a wrong referent is a note, not a STOP)")
    w("")
    for i, n in enumerate(notes, 1):
        w(f"{i}. {n}")
    w("")
    conditional = [
        {"figure": "[g3-A] joint power 0.9642 / 0.964", "if_in_note": "STOP (design seat and PI)",
         "text": "If the note carries the [g3-A] joint power as 0.9642 or 0.964: exact enumeration at the record's "
                 f"inputs gives {jp_rec:.5f} ({jp_rec:.4f} at 4 dp, {jp_rec:.3f} at 3 dp; section 6a). The cause of "
                 "the residual is not identified (a simulation is a candidate, not established), so Code cannot "
                 "classify it as transcription. Under block :23 that figure is then a STOP for the design seat "
                 "and PI. The [g3-A] verdict itself is computed on our data and is not touched. The addendum "
                 f"describes the figure as 'at their own rates' ({ADDENDUM}@{COMMIT}:148); at the source's text "
                 f"rates (instruct FPR 0%) the exact value is {jp_src:.5f}, which bears on any correction the "
                 "design seat and PI choose."},
        {"figure": "single weakest pair (base vs dpo) 0.9825", "if_in_note": "STOP (design seat and PI)",
         "text": "If the note carries 'single weakest pair (base vs dpo) 0.9825': at the record's inputs base > dpo "
                 f"is {pair_rec:.5f} and the weakest pair is {weak_rec.replace('>', ' > ')} "
                 f"({pairs_rec[weak_rec]:.5f}) (section 6a). The label is wrong at the record's own inputs, "
                 "which is not a transcription slip, and the value's residual has no identified cause, so under "
                 "block :23 it is a STOP."},
        {"figure": "source instruct FPR 0.3%, TPR - FPR +0.6 pp, the retired criterion's Instruct power "
                   "described as at the source's own rates, and 'n in the thousands per cell' for conventional "
                   "power at Instruct (RESULTS :7363-7364)",
         "if_in_note": "correction (Code's reading) or STOP",
         "text": "If the note or F2 carries the source's instruct FPR as 0.3%, or its instruct TPR - FPR as +0.6 pp: "
                 "Code reads the discrepancy as transcription of the v1 prose (section 4). On that reading block "
                 ":23 corrects the note to 0% and +0.9 pp, and there is no STOP. If the design seat or PI do not "
                 "accept that reading (the record says it recovered the values from 'Appendix C, Fig 21', and the "
                 "figure was not digitized), block :23 makes it a STOP. The same fork covers the figures derived "
                 "from that input: if the note carries the retired criterion's Instruct power described as at "
                 "their own (reported) rates ("
                 + ", ".join(f"{r['record_instruct']:.3f} at n = {r['n_per_arm']}" for r in pw_src_differs)
                 + f"; {ADDENDUM}@{COMMIT}:52-53, RESULTS.md@{COMMIT}:7330-7331, :7354-7361), then under Code's "
                 "transcription reading block :23 corrects it to the source-rate values "
                 + " / ".join(f"{r['recomputed_instruct_fpr_0p000']:.3f}" for r in pw_src_differs)
                 + " (section 6b), and otherwise it is a STOP. At n = 24 and 48 the value is 0.000 either way. "
                 "The same holds for the sentence after the table, if the note carries it: 'Reaching conventional "
                 f"power there needs n in the thousands per cell' (RESULTS.md@{COMMIT}:7363-7364, Instruct) holds "
                 f"only at the transcribed 0.3% (≈ {cr['0.80']['first_grid_n']} per arm for 0.80, ≈ "
                 f"{cr['0.90']['first_grid_n']} for 0.90). Under Code's transcription reading block :23 corrects "
                 f"it to the source-rate figures, {conv_src_txt} (section 6b), and otherwise it is a STOP. "
                 ":7363's 'Instruct is the binding constraint and it is not close' holds at both inputs and needs "
                 "no correction."},
        {"figure": "~800 / ~80 as the source's n, and figures derived from it", "if_in_note": "cut",
         "text": "If the note presents ~800 injected / ~80 control per configuration as the source's n: the source "
                 "states no n (section 5), so under block :23 the figure is not found and is cut. Stated as an "
                 "assumption with its premise (eight concepts, per configuration, applied to pooled rates), it is "
                 "the record's log-only inference. Any figure derived from it is cut likewise, or stated with its "
                 f"premise and unit: the ratio '~33× ours' ({ADDENDUM}@{COMMIT}:32-33; RESULTS.md@{COMMIT}:7440) is "
                 f"{ratio_txt}; the power row 'theirs, OLMo cell (~800/80)' (RESULTS.md@{COMMIT}:7485, "
                 ":7500-7502) is computed at that n and is not recomputed by this item."},
    ]
    w("## 12. STOPs")
    w("")
    w("**Active STOPs for N2(vi): none.** N2(vi) is resolved (section 10), which is its pass condition "
      "(block :36), and no reproduction here needs a change to any analyzer of record (block section 0.3).")
    w("")
    w(f"**Conditional, under block :23** ({BLOCK}@{COMMIT}:23, N1's on-fail rule: a discrepant figure is corrected "
      "in the note if the discrepancy is transcription and is a STOP if it is not; a not-found figure is cut). "
      "The note is not on this machine (header; note 9), so whether it carries these figures is unknown. Each "
      "condition fires only if it does:")
    w("")
    for i_, c_ in enumerate(conditional, 1):
        w(f"{i_}. {c_['text']}")

    # ---------------------------------------------------------------- statuses
    figures = []
    for s in STAGES:
        r = cmp_rows[s]
        figures.append({"figure": f"source {s} TPR {r['record_a_tpr']:.3f}", "record_locators": cloc(f"{s}_tpr"),
                        "status": "log-only" if r["tpr_match"] else "discrepant",
                        "printed": f"record {r['record_a_tpr']:.3f}; source v1 text {SOURCE_V1[s]['tpr']:.3f}",
                        "note": "in no committed JSON; " + ("equals the v1 Appendix C prose" if r["tpr_match"]
                                                            else "differs from the v1 prose")})
    for s in STAGES:
        r = cmp_rows[s]
        figures.append({"figure": f"source {s} FPR {r['record_a_fpr']:.3f}", "record_locators": cloc(f"{s}_fpr"),
                        "status": "log-only" if r["fpr_match"] else "discrepant",
                        "printed": f"record A {r['record_a_fpr']:.3f} / record B {r['record_b_fpr']:.3f}; "
                                   f"source v1 text {SOURCE_V1[s]['fpr']:.3f}",
                        "note": ("in no committed JSON; equals the v1 prose" if r["fpr_match"] else
                                 "Code's reading: transcription of the v1 prose, where 0.3% is the introspection "
                                 f"rate and FPR is 0%. Fig. 21 (a PNG, {V1_FIG21_IMAGE.split('/')[-1]}) was not "
                                 "digitized, so a figure reading is not excluded; under block :23 the "
                                 "classification decides correction or STOP if the note carries it (section 12)")})
    sens_ok = [s for s in STAGES if cmp_rows[s]["sens_match"]]
    figures.append({"figure": "source TPR - FPR, " + "/".join(sens_ok) + " ("
                    + " / ".join(cmp_rows[s]["record_a_sens"] for s in sens_ok) + ")",
                    "record_locators": cloc("sens3"), "status": "log-only",
                    "printed": "source arithmetic " + " / ".join(f"{cmp_rows[s]['source_tpr_minus_fpr_pp']:+.1f} pp"
                                                                 for s in sens_ok),
                    "note": "equal"})
    for s in STAGES:
        if not cmp_rows[s]["sens_match"]:
            figures.append({"figure": f"source {s} TPR - FPR {cmp_rows[s]['record_a_sens']}",
                            "record_locators": cloc("sens_instruct"),
                            "status": "discrepant",
                            "printed": f"source arithmetic {cmp_rows[s]['source_tpr_minus_fpr_pp']:+.1f} pp",
                            "note": "follows from the instruct FPR reading (row above); same block :23 condition"})
    figures += [
        {"figure": f"aggregation over L in {V1_FIG21_LAYERS} x alpha in {V1_FIG21_ALPHAS} ({n_cfg} configurations)",
         "record_locators": loc_a(39) + "; " + loc_r(7343), "status": "log-only",
         "printed": f"{n_cfg} configurations; addendum :39 text asserted",
         "note": "equals the v1 Figure 21 caption; every per-stage value is this aggregate, not best-of-grid"},
        {"figure": "~800 injected / ~80 control per (layer, alpha) configuration, and its ratio ~33× our 24, as "
                   "the record's inference (eight concepts x the code's 100 / 10 per concept)",
         "record_locators": loc_r("7438-7440") + " (carriers :" + ", :".join(
             str(x) for k_ in ("n800", "ratio33") for x in N_INFERENCE_LINES[k_][RESULTS]) + ")",
         "status": "log-only",
         "printed": f"computed-new: 8 x {inj_per_concept} / 8 x {ctl_per_concept} = 800 / 80 per cell; pooled over "
                    f"{n_cfg} cells {scen[0]['per_stage_pooled_injected']} / {scen[0]['per_stage_pooled_control']}; "
                    f"ratio {ratio_txt}",
         "note": f"the eight is our B2 registration ({B2C}@{COMMIT} selection_for_B2.registered_n = 8; its "
                 "canonical set is 50, n_canonical); a per-configuration n, while the source's rates are pooled "
                 "over 20 configurations (section 7); our 24 per stage as run from RESULTS.md@bbc9ffe:7440, :7358"},
        {"figure": "~800 injected / ~80 control per configuration, as the source's n, and figures derived from it "
                   "(~33× ours; the 'theirs, OLMo cell (~800/80)' power row)",
         "record_locators": loc_a("32-33") + "; " + loc_r(*N_AS_SOURCE_LINES["n800"][RESULTS])
                            + f" (:7485 and :7500-7502 are the power row at that n); the block's premise, "
                              f"{BLOCK}@{COMMIT}:34",
         "status": "not found",
         "printed": f"the source states no n (v1-v5); code default {d['DEFAULT_TEST_CONCEPTS_len']} concepts gives "
                    f"{scen[1]['per_cell_injected']} / {scen[1]['per_cell_control']} per cell; the ratio is "
                    f"{rfmt(r8['ratio_their_configuration_to_our_stage'])} only per their configuration at eight "
                    "concepts (row above)",
         "note": "under block :23 a note sentence presenting it as the source's n is cut, and so is any figure "
                 "derived from it unless stated with its premise and unit (section 12, condition 4); RESULTS "
                 ":7485 and :7500 sit in the entry (:7419-7506) that states the eight-concept premise at "
                 ":7438-7439 but write the figure as theirs without it, and :7365's entry (:7326-7418) does not "
                 "state the premise; as an assumption with its premise it is the row above"},
        {"figure": "layer indices from the code's default fractions", "record_locators": loc_a("60-68"),
         "status": "computed-new", "printed": f"int {idx0}; round {ridx0}; caption {V1_FIG21_LAYERS}; README "
                                              f"absolute list equals the caption {readme_eq_caption}/5",
         "note": "neither rule yields the caption list; not adjudicated"},
        {"figure": "decoding: temperature 1.0, max_new_tokens 100",
         "record_locators": loc_a("89-91") + "; " + loc_r(7433), "status": "log-only",
         "printed": f"source code DEFAULT_TEMPERATURE {d['DEFAULT_TEMPERATURE']}, DEFAULT_MAX_TOKENS "
                    f"{d['DEFAULT_MAX_TOKENS']}; paper v1 App. A T = 1.0",
         "note": "consistent"},
        {"figure": "lineage: our four acquired HF repos and revisions",
         "record_locators": f"{MANIFEST}@{COMMIT} fields repo, revision",
         "status": "reproduced",
         "printed": "; ".join(f"{s} {lin_rows[s]['record_repo']} @ {lin_rows[s]['record_revision']}" for s in STAGES),
         "note": "read from the committed manifest"},
        {"figure": "lineage: our four repos match the source's MODEL_NAME_MAP",
         "record_locators": loc_r("12565-12569"),
         "status": "log-only",
         "printed": f"computed-new against Code's WebFetch reading of src/model_utils.py@5d5d9b4: {lin_match}/4 "
                    "repo match",
         "note": "the source half is a WebFetch reading, not a committed artifact, so the match is the record's "
                 "prose claim; revision-level match not determinable (source pins none)"},
        {"figure": "retired criterion's power, DPO column (2.9 vs 0.0): 0.001/0.012/0.147/0.691 at n = "
                   "24/48/96/200",
         "record_locators": loc_r("7354-7361"), "status": "log-only",
         "printed": "recomputed with the record's newcombe: "
                    f"{sum(r['dpo_agrees_3dp'] for r in pw_rows)}/4 cells agree to 3 dp",
         "note": "inputs are prose rates, so log-only; they equal the v1 text, so the cells stand as described "
                 "('at their own numbers'); the arithmetic is re-derived and agrees (computed-new)"},
        {"figure": "retired criterion's Instruct power, as the record describes it: at the source's own (reported) "
                   "rates, 0.000/0.000/0.001/0.020 at n = 24/48/96/200 (the table's 'Instruct (0.9 vs 0.3)')",
         "record_locators": loc_a("52-53") + "; " + loc_r("7330-7331", "7354-7361") + f"; other tracked: {R19_OTHER}",
         "status": "discrepant",
         "printed": "at the record's transcribed rates (0.9 vs 0.3) recomputed "
                    + " / ".join(f"{r['recomputed_instruct_fpr_0p003']:.3f}" for r in pw_rows)
                    + f" ({sum(r['instruct_agrees_3dp'] for r in pw_rows)}/4 agree to 3 dp); at the source's rates "
                    "(0.9 vs 0.0) " + " / ".join(f"{r['recomputed_instruct_fpr_0p000']:.3f}" for r in pw_rows)
                    + "; differs at " + ", ".join(f"n = {r['n_per_arm']}" for r in pw_src_differs),
         "note": "described as at the source's own rates ('their own Instruct rates', 'Instruct's own reported "
                 "rates', 'their own numbers'), where the n = 96 and n = 200 cells differ; the arithmetic "
                 "reproduces at the record's 0.3%; follows from the instruct FPR reading (row 8); under block :23 "
                 "corrected to the source-rate values under Code's transcription reading, a STOP otherwise "
                 "(section 12, condition 3)"},
        {"figure": "[g3-A] joint power 0.9642 (and 'the exact number is 0.964')",
         "record_locators": cloc("joint") + f"; {VALUESCHECK}@{COMMIT} 1_g3A_power.detail",
         "status": "discrepant",
         "printed": f"exact at the record's inputs {jp_rec:.5f} ({jp_rec:.4f}; {jp_rec:.3f} at 3 dp); at instruct "
                    f"FPR .000 {jp_src:.5f}",
         "note": f"residual {REC_JOINT - jp_rec:+.4f}; discrepant at the record's own 3 dp too; cause not identified "
                 "(simulation a candidate, not established), so not classifiable as transcription; under block :23 "
                 "a STOP for the design seat and PI if the note carries 0.9642 or 0.964 (section 12); both values "
                 "clear the 0.90 bar"},
        {"figure": "single weakest pair (base vs dpo) 0.9825",
         "record_locators": cloc("pair"),
         "status": "discrepant",
         "printed": f"at the record's inputs base > dpo {pair_rec:.5f}; weakest pair {weak_rec.replace('>', ' > ')} "
                    f"{pairs_rec[weak_rec]:.5f}; at instruct FPR .000 base > dpo = base > instruct {weak_src_val:.5f}",
         "note": f"value residual {REC_PAIR - pair_rec:+.4f} and the label is wrong at the record's inputs; under "
                 "block :23 a STOP if the note carries it (section 12)"},
        {"figure": "design seat's N2(v) source points (block :34: d' -1.9 / -0.3 / +0.6 / +0.15; p ~ .11 DPO, "
                   "~ .5 instruct, at 800/80 per configuration)",
         "record_locators": f"{BLOCK}@{COMMIT}:34", "status": "computed-new",
         "printed": "at 800/80 (per configuration): " + " / ".join(f"{r800[s]['dprime_loglinear']:+.3f}" for s in STAGES)
                    + f"; p DPO {r800['dpo']['fisher_one_sided_p']:.4f}, instruct "
                    f"{r800['instruct']['fisher_one_sided_p']:.4f}. At {ri16['n_injected']}/{ri16['n_control']} "
                    "(pooled, same premise): " + " / ".join(f"{r16k[s]['dprime_loglinear']:+.3f}" for s in STAGES)
                    + f"; p DPO {pfmt(r16k['dpo']['fisher_one_sided_p'])}, instruct "
                    f"{pfmt(r16k['instruct']['fisher_one_sided_p'])}; instruct at record FPR .003 "
                    f"{ri16['dprime_loglinear']:+.3f}, p {pfmt(ri16['fisher_one_sided_p'])}",
         "note": (("arithmetic confirmed under the seat's premise (800/80 is a per-configuration n applied to rates "
                   f"pooled over {n_cfg} configurations), not confirmed as the source's points: at the pooled n "
                   f"{len(both_units)} of {len(seat_check)} figures hold, and there the instruct FPR correction "
                   f"changes the instruct point (d' {ri16['dprime_loglinear']:+.3f} -> "
                   f"{r16k['instruct']['dprime_loglinear']:+.3f}; p {pfmt(ri16['fisher_one_sided_p'])} -> "
                   f"{pfmt(r16k['instruct']['fisher_one_sided_p'])}); N2(v) declares concept count and unit")
                  if seat_all_800 else "NOT reproduced at the seat's own premise; see section 7")},
        {"figure": "p ~ .28 for our 0/43 at the source's dpo TPR 2.9%",
         "record_locators": cloc("p28"), "status": "log-only",
         "printed": f"computed-new {p28:.4f} = P(X <= {k43}) for X ~ Binomial(n = {n43}, p = .029), exact binomial lower tail "
                    f"(= 0.971^{n43}); {k43}/{n43} from data/olmo/b2r_explore_dpo.json@{COMMIT} fields hit, "
                    "inj_decidable",
         "note": "agrees at the record's 2 dp; the test is Code's reading (the record names none); the 2.9% is a "
                 "source prose rate, so log-only"},
        {"figure": "'Reaching conventional power there needs n in the thousands per cell' (the retired criterion "
                   "at Instruct, the sentence after the table under 'Power at their own numbers')",
         "record_locators": loc_r("7363-7364"), "status": "discrepant",
         "printed": f"computed-new, n per arm: at the source's rates (0.9 vs 0.0) {conv_src_txt}; first n "
                    f"{cs['0.80']['first_n_step1']} ({cs['0.80']['power_at_first_n_step1']:.5f}) and "
                    f"{cs['0.90']['first_n_step1']} ({cs['0.90']['power_at_first_n_step1']:.5f}). At the record's "
                    f"transcribed rates (0.9 vs 0.3) ≈ {cr['0.80']['first_grid_n']} "
                    f"({cr['0.80']['power_at_first_grid_n']:.4f}) and ≈ {cr['0.90']['first_grid_n']} "
                    f"({cr['0.90']['power_at_first_grid_n']:.4f}); first n {cr['0.80']['first_n_step1']} "
                    f"({cr['0.80']['power_at_first_n_step1']:.5f}) and {cr['0.90']['first_n_step1']} "
                    f"({cr['0.90']['power_at_first_n_step1']:.5f}); step-1 values at 5 dp",
         "note": "holds only at the transcribed 0.3%; described as at the source's own rates (it sits under 'Power "
                 "at their own numbers', :7354), where conventional power needs hundreds per arm; 'per cell' read as "
                 "n per arm, the table's unit (:7356; Code's reading); :7363's 'binding constraint ... not close' "
                 "holds at both inputs; the only carrier the round-4 'thousands' grep finds in the tracked .py/.md "
                 "files (section 2); follows from the instruct FPR reading (row 8); under block :23 corrected to the source-rate "
                 "figures under Code's transcription reading, a STOP otherwise (section 12, condition 3), the same "
                 "fork as row 19"},
    ]
    S = []
    S.append("")
    S.append("## 0. Per-figure status (for N1's ledger)")
    S.append("")
    S.append("Status vocabulary: reproduced | log-only | not found | discrepant | computed-new. 'log-only' "
             "means the record carries the figure only in prose. Where this item checked such a figure against "
             "the source or re-derived its arithmetic, the result is in 'printed'. Rows 1-10, the two ~800/80 "
             "rows (which divide that pattern's and the ~33× pattern's carriers between them, asserted) and the "
             "joint, pair and p ~ .28 rows take their locators from the carrier search (section 2), so for those "
             "patterns the lists are complete; rows 19 and 24 take their prose locators from the round-4 greps "
             "there (row 19's table cells are located by parsing the table). 'Other tracked' are code comments, a "
             "fixture and a handoff, not log lines. Row 24 was added in round 4 and appended, so rows 1-23 keep "
             "the numbers the earlier values-check rounds cite. Block :23 consequences for the note are in "
             "section 12.")
    S.append("")
    S.append("| # | figure | record locator(s) | status | printed by this script | note |")
    S.append("|---|---|---|---|---|---|")
    for i, f in enumerate(figures, 1):
        S.append(f"| {i} | {f['figure']} | {f['record_locators']} | {f['status']} | {f['printed']} | {f['note']} |")

    # ---------------------------------------------------------------- values-check
    vcheck = [
        ("1", "substantive", "No per-figure status in the raw or the JSON.", "fixed",
         "Section 0 is a per-figure status table and the JSON carries `figures[].status`. The TPR, FPR and "
         "sensitivity statuses are derived from the computed comparisons; the others are assigned from the "
         "rule-4 vocabulary, with the printed value beside each. Beyond the checker's list, rows were added for the "
         "power figures (section 6) and the seat's N2(v) points (section 7)."),
        ("2", "substantive", "Note 3: the seat's N2(v) instruct arithmetic 'cannot be checked here'; the "
         "correction 'changes' it.", "fixed",
         "Section 7 computes log-linear d', c and a one-sided Fisher (stdlib, equal to the record's "
         f"fisher_one_sided). At 800/80 the instruct point is {r800['instruct']['hits']}/"
         f"{r800['instruct']['false_alarms']} under both FPRs, giving d' "
         f"{r800['instruct']['dprime_loglinear']:+.3f} and p = {r800['instruct']['fisher_one_sided_p']:.4f}; "
         f"{sum(seat_ok.values())} of the seat's 4 d' agree at its precision, and its two p (DPO "
         f"{r800['dpo']['fisher_one_sided_p']:.4f}, instruct {r800['instruct']['fisher_one_sided_p']:.4f}) "
         "match its ~.11 and ~.5. Note 3 is rewritten. The pi_item in the builder's returned summary (not in "
         "the raw) is superseded by note 3."),
        ("3", "substantive", "Code's base trial prompt called 'bare'.", "fixed",
         "Re-read of 03_behavioral_robustness.py@5d5d9b4 (section 3, fixer-pass reads): "
         "build_base_model_prompt writes plain-text User:/Assistant: turns with no chat template; 'Tell me "
         "about {word}' is only in extract_concept_vector_base_model. The section 3 fact, the section 9 row "
         "and the JSON's decoding.prompt_format are corrected."),
        ("4", "minor", "Paper v1 prompt_format 'not stated'.", "fixed",
         "Re-read of v1 (both halves): Section 3.3 gives a User:/Assistant: newline format for the base model "
         "it discusses (Gemma3-27B base as read); no OLMo-specific format anywhere. The row is reworded."),
        ("5", "minor", "Note 2 omitted ADDENDUM :52-53 and RESULTS :7330-7331.", "fixed",
         "Both are added, and both are recomputed in section 6(b). Anchors are asserted on :53 and :7331."),
        ("6", "minor", "Joint power 'presumably' used 0.3%; not recomputed.", "fixed",
         f"Section 6(a) enumerates exactly with the record's own CP: {jp_rec:.4f} at .003 and {jp_src:.4f} at "
         f".000; pair {pair_rec:.4f}. The residual against 0.9642 / 0.9825 is disclosed and unexplained. One "
         "correction to the checker's evidence: 0.9642 is not only in prose. "
         f"{VALUESCHECK}@{COMMIT} field 1_g3A_power.detail holds 'joint=0.9642 >= 0.90' (as a result string, "
         "without inputs or method)."),
        ("7", "minor", "Note 5 paraphrase of ADDENDUM :66 dropped 'and the paper's caption'.", "fixed",
         "Note 5 quotes :66 and states that the caption's fourth slot (45) contradicts the code rule's 44. "
         "round() is added beside int() (section 5); neither yields the caption list."),
        ("8", "minor", "v4 row / note 1 omit that v4's Figure 21 is a different OLMo figure.", "fixed",
         "Re-read of v4 (both halves): Figure 21 is the Appendix D.1 OLMo-stage figure at L=19/L=22. The v4 row, "
         "section 3's version paragraph and note 1 say so."),
        ("9", "minor", "Table 3 described as 'official checkpoints'.", "fixed",
         "Re-read of v4: Table 3 is a LoRA fine-tuning study on the OLMo SFT checkpoint (L=25, alpha=4, 11 rows "
         "as read); only SFT* and DPO* are official. The v2/v4/v5 rows and the JSON config string are reworded; "
         "'only' is dropped."),
        ("10", "minor", "Answer 3 'Nothing was digitized' over-reaches.", "fixed",
         "Answer 3 now says the record states no recovery method (RESULTS :7326-7327). The source holds the "
         "values in prose; the 7-of-8 equality supports text-reading; this audit digitized nothing."),
        ("11", "minor", "Note 7 attributed 'exact against paper' to RESULTS :7181; '7 of 8' hard-coded.", "fixed",
         "The quote is attributed to ADDENDUM :274, :7181 is paraphrased as 'PASS -- exact', and the "
         "valuescheck JSON's '§0.2 exact' is added. The count is formatted from n_tpr + n_fpr."),
        ("12", "minor", "The note's sentence was never checked; no line says so.", "fixed",
         "A header line and note 9 cite the preflight raw's MISSING rows (located and asserted by the "
         "script) and say the note's wording and F2's points were not read."),
        ("13", "minor", "Answer 4 locator :213-214.", "fixed",
         "Now :212-213. Anchors are asserted on both lines."),
        ("14", "minor", "Paraphrase without stated reason.", "fixed",
         "Section 3 says the raw keeps to one short quotation from the source and that the paraphrases carry "
         "every number exactly as printed."),
    ]
    vcheck2 = [
        ("1", "substantive", "Joint power 0.9642 labelled discrepant and 'not a STOP' without addressing block :23; "
         "the record's 'exact number is 0.964' is 0.965 at 3 dp.", "fixed",
         f"Section 12 now separates active STOPs (none for N2(vi)) from block :23 conditions. The joint-power row "
         f"says: a STOP for the design seat and PI if the note carries 0.9642 or 0.964, because the cause is not "
         f"identified and so cannot be classed as transcription. Section 6(a) prints {jp_rec:.7f} ({jp_rec:.3f} at "
         "3 dp) against the record's exactness claims (RESULTS :7194, :7269-7270, :7251). Code's own checks: "
         f"{sum(v_['reproduces_both_4dp'] for v_ in var_rows)} of {len(var_rows)} deterministic variants "
         "reproduce both printed values. Monte Carlo standard errors "
         "make a 10^4-10^5-draw simulation a candidate, stated as not established. Beyond the checker's list, the "
         "carrier search found two more carriers of the figure, RESULTS :7173 and :7251. 'Immaterial' is no longer "
         "used; the 0.90-bar fact is kept beside the conditional."),
        ("2", "substantive", "800/80 is a per-cell n applied to rates pooled over 20 configurations; the seat's "
         "arithmetic was called 'confirmed' and the correction 'does not change' it, without that premise.", "fixed",
         f"Section 7 adds the pooled rows ({scen[0]['per_stage_pooled_injected']}/{scen[0]['per_stage_pooled_control']} "
         f"and {scen[1]['per_stage_pooled_injected']}/{scen[1]['per_stage_pooled_control']}) and a unit column. "
         "It states the unit mismatch and reports the seat's figures as 'arithmetic confirmed under the seat's "
         "premise', with the pooled value beside each. The JSON adds design_seat_check, and the old "
         "design_seat_confirmed_at_800_80 key is kept for N2. At "
         f"{ri16['n_injected']}/{ri16['n_control']}: instruct {ri16['hits']}/{ri16['false_alarms']} at .003, d' "
         f"{ri16['dprime_loglinear']:+.3f}, p {pfmt(ri16['fisher_one_sided_p'])}; "
         f"{r16k['instruct']['hits']}/{r16k['instruct']['false_alarms']} at .000, d' "
         f"{r16k['instruct']['dprime_loglinear']:+.3f}, p {pfmt(r16k['instruct']['fisher_one_sided_p'])}; DPO d' "
         f"{r16k['dpo']['dprime_loglinear']:+.3f}, p {pfmt(r16k['dpo']['fisher_one_sided_p'])}; base "
         f"{r16k['base']['dprime_loglinear']:+.3f}; SFT {r16k['sft']['dprime_loglinear']:+.3f}. All "
         f"{checker_r2_agree} points equal the checker's printed counts, d' and p at its precision (asserted by "
         "the script; so are its joint and four pair values, finding 1 and 3). Note 3, the seat row and answer 2 are rewritten. Consistency with N2: "
         + (f"{n2_cmp['seat_figures_at_pooled_agree']}/{n2_cmp['seat_figures_compared']} seat figures and the "
            f"record-FPR instruct point "
            f"{'agree' if n2_cmp['instruct_record_fpr_pooled_agrees'] else 'DIFFER'} with {N2_ROC} (section 7)"
            if n2_cmp["status"] == "compared" else n2_cmp["status"]) + "."),
        ("3", "minor", "The record's 'single weakest pair (base vs dpo)' is wrong at its own inputs.", "fixed",
         f"Section 6(a) prints all four pairs at both inputs. At .003 the weakest is {weak_rec.replace('>', ' > ')} "
         f"{pairs_rec[weak_rec]:.5f} (base > dpo {pair_rec:.5f}); at .000 base > dpo and base > instruct tie at "
         f"{weak_src_val:.5f}. {len(pairs_equal_9825)} of the four equals 0.9825 at 4 dp. Changes: a new status "
         "row, note 10 and a section 12 condition. 'base binds, not sft' is asserted to hold at both inputs."),
        ("4", "minor", "Row 8 'transcription' note unhedged.", "fixed",
         "Round-2 read of v1 (two fetches): Figure 21 is an image, olmo-staged-introspection.png, alt text 'Refer "
         "to caption', with no data labels. Row 8, section 4, answer 6 and note 2 now give 'Code's reading: "
         "transcription ... not established', and section 12 states the block :23 fork (correction under that "
         "reading, STOP otherwise)."),
        ("5", "minor", "'The README is therefore not evidence of the producing configuration' overstates.", "fixed",
         f"Reworded. The README cannot run as written, but its list equals the caption ({readme_eq_caption}/5), "
         f"which int() ({int_eq_caption}/5) and round() ({round_eq_caption}/5) do not; Code computes all three "
         "counts. One adaptation: the checker's 'points to' is written 'consistent with', since the record itself "
         "reads it that way (RESULTS :7396-7398) and the source does not say. Notes 5 and 6 carry the 5/5."),
        ("6", "minor", "The 'paraphrases' reproduce the source's wording.", "fixed",
         "The DPO, instruct and base lines now give the numbers only, in Code's words, as the checker proposed; "
         "the SFT line is reduced the same way. The one quotation is unchanged."),
        ("7", "minor", "Section 2 label calls :7345-7348 a paraphrase; the v1 row omits Section 3.3's FPR "
         "statement.", "fixed",
         "Round-2 read of v1 (two fetches) found the sentence in Section 3.3 'The Role of Post-Training'. The "
         "label now reads 'the record quoting v1 Section 3.3'. The v1 row and a section 3 paragraph state, in "
         "Code's words, that Section 3.3 gives the FPR pattern with no per-stage TPR numbers."),
        ("8", "minor", "Locator lists not exhaustive; the record's p ~ .28 unchecked.", "fixed",
         "Section 2 adds a carrier search. Per figure, a regex over every line of RESULTS.md and the addendum at "
         "bbc9ffe, with hits asserted equal to declared carriers plus declared unrelated lines "
         f"({n_unrel} unrelated, each with a reason). One git grep covers the other tracked .py/.md files "
         f"({len(OTHER_CARRIERS)} carriers, {len(OTHER_UNRELATED)} unrelated). Section 0 locators come from it. "
         f"A new row gives p ~ .28: {p28:.4f}, exact binomial P(X <= 0) for X ~ Binomial(43, .029), with 0/43 read from "
         "b2r_explore_dpo.json. It is labelled log-only, not computed-new as the checker proposed, because the "
         "figure is in the record and its 2.9% input is source prose (the same convention as the retired-power "
         "row); the recomputation is printed as computed-new."),
        ("9", "minor", "Row 12 '~800/~80' conflates 'absent from the source' with 'absent from the record'.",
         "fixed",
         "Split into two rows. As the record's inference (RESULTS :7438-7440) it is log-only. As the source's n "
         "(ADDENDUM :32-33, RESULTS :7365, block :34) it is not found, and block :23's cut applies. The "
         f"log-only row cites {B2C}@bbc9ffe (n_canonical = 50; selection_for_B2.registered_n = 8, so the eight "
         "is ours), and so do section 5 and note 4."),
        ("10", "minor", "'clopper' described without its docstring line.", "fixed",
         "The script lists the lines (:10 docstring, :49 import, :60, :61, :74, :112 calls) and asserts the "
         "list, the docstring span and the call form."),
    ]
    def rown(prefix):
        hits_ = [i_ for i_, f_ in enumerate(figures, 1) if f_["figure"].startswith(prefix)]
        assert len(hits_) == 1, (prefix, hits_)
        return hits_[0]

    row_lin_a, row_lin_b = rown("lineage: our four acquired"), rown("lineage: our four repos match")
    row_pw_dpo, row_pw_ins = rown("retired criterion's power, DPO"), rown("retired criterion's Instruct power")
    row_joint, row_n_inf, row_n_src = rown("[g3-A] joint power"), rown("~800 injected / ~80 control per (layer"), \
        rown("~800 injected / ~80 control per configuration, as the source's n")
    row_thousands = rown("'Reaching conventional power there needs n in the thousands")
    assert row_thousands == ROW_THOUSANDS == len(figures) and row_pw_ins == 19, (row_thousands, row_pw_ins)
    vcheck3 = [
        ("1", "substantive", "The retired criterion's Instruct power, which the record describes as at the source's "
         "own rates, was relabelled 'at the record's rates' and given no block :23 condition.", "fixed",
         f"Old row 17 is split. Row {row_pw_dpo} is the DPO column, log-only: its inputs equal the v1 text, and "
         f"{sum(r['dpo_agrees_3dp'] for r in pw_rows)}/4 cells recompute. Row {row_pw_ins} gives the Instruct "
         "figures in the record's own framing ('their own Instruct rates', ADDENDUM :52-53; 'Instruct's own "
         "reported rates', RESULTS :7330-7331; 'Power at their own numbers', RESULTS :7354), with the "
         "source-rate column beside the recomputation at the record's 0.3%. At the source's rates the cells "
         "differ at "
         + ", ".join(f"n = {r['n_per_arm']} ({r['record_instruct']:.3f} against "
                     f"{r['recomputed_instruct_fpr_0p000']:.3f})" for r in pw_src_differs)
         + ". Section 12 condition 3 now covers these figures with the same fork: corrected to the source-rate "
         "values under Code's transcription reading, a STOP otherwise. Section 6(b) and note 2(1) say the same. "
         "Anchors are asserted on RESULTS :7330, :7331, :7354 and ADDENDUM :53, :148. One adaptation: the Instruct row's "
         "status is 'discrepant', not only a note, by the raw's own convention for the +0.6 pp row (correct "
         "arithmetic on the slipped input, labelled discrepant). Beyond the checker's list: condition 1 now notes "
         f"that the addendum also describes the joint power as 'at their own rates' (ADDENDUM :148), where the "
         f"exact value is {jp_src:.5f}. Condition 1's consequence (a STOP if carried) is unchanged."),
        ("2", "substantive", "The lineage row was labelled 'reproduced' although its source half is a WebFetch "
         "reading, not a committed artifact.", "fixed",
         f"Split into row {row_lin_a} (our four acquired repos and revisions, reproduced from "
         f"{MANIFEST}@{COMMIT}) and row {row_lin_b} (the match to the source's MODEL_NAME_MAP, log-only at "
         f"RESULTS :12565-12569, printed as 'computed-new against Code's WebFetch reading of 5d5d9b4: "
         f"{lin_match}/4'). Section 8, answer 7 and the JSON lineage string say the same. Both statuses pass N1, "
         "so only the label changes."),
        ("3", "minor", "The N2 ROC JSON's sha256 recorded here was stale, and the two items' sha references form "
         "a cycle.", "fixed",
         "This item no longer records that sha, in the .md or the JSON. The JSON's n2_consistency_check now "
         "carries the compared values from both sides and the agreement counts, and section 7 says why the sha "
         "is omitted. The round-2 header's sentence about the sha moving between runs is kept as written at "
         "round 2, and this row supersedes it. Ordering: this run changes this JSON's sha256, so the N2 raw's "
         "recorded N2vi JSON sha is now stale until N2 re-runs. The N2 run belongs to that item and should come "
         "after this one. Code did not run it (not this item's file)."),
        ("4", "minor", "b2_concepts.json's concepts_source was said to cite 'the source's DEFAULT_TEST_CONCEPTS'; "
         "it cites experiments/01_concept_injection.py:58, while the OLMo experiment 03 defines its own list.",
         "fixed",
         f"Confirmed by git show ({B2C}@{COMMIT}; the script asserts that concepts_source starts with "
         "'experiments/01_concept_injection.py:58 (DEFAULT_TEST_CONCEPTS') and by two round-3 WebFetch reads of "
         "03_behavioral_robustness.py@5d5d9b4 (section 3): there DEFAULT_TEST_CONCEPTS is a literal list defined "
         "in the file and imported from nowhere, with 50 entries. Section 5 and note 4 now cite 01:58 and say "
         "the OLMo run's 50 is 03's own list. One adaptation: instead of 'identity with 01's not checked', "
         f"read 1's {exp03_n_read1} entries are compared with canonical_concepts (the record's recovery of 01:58) "
         "and are "
         + ("equal entry for entry and in order" if exp03_same_order else "NOT equal")
         + " (computed-new). Read 2 declined to copy the list and corroborates only the count, the first and "
         "last entries and the import status. So the identity is stated as Code's reading, not established."),
        ("5", "minor", "Note 2's joint-power locators omitted RESULTS :7270 and ADDENDUM :273.", "fixed",
         f"Note 2(2) now prints the carrier search's list, the same as row {row_joint}: {joint_carriers}. It "
         "names the arithmetic passages (ADDENDUM :147-148; RESULTS :7189-7194, :7266-7270) separately."),
        ("6", "minor", "Condition 4 cut ~800/~80 as the source's n but not the ratio derived from it "
         "('~33× ours').", "fixed",
         f"Condition 4 now covers figures derived from the n: cut, or stated with premise and unit. The ratio "
         f"is computed (computed-new): {ratio_txt}, with our 24 injected per stage as run (RESULTS :7440, "
         f":7358). Rows {row_n_inf} and {row_n_src} carry it. Beyond the checker's list: a round-3 carrier search "
         "for the n ('~800|800/80') and the ratio ('33×') over RESULTS.md and the addendum, with the split "
         "between the two rows asserted, found two more carriers of the n written as the source's: RESULTS "
         ":7485 (a power row 'theirs, OLMo cell (~800/80)') and :7500 ('Their own cell is ~800/80'). Both are "
         f"added to row {row_n_src} and to condition 4. The power figures there are computed at that n and are "
         "not recomputed by this item. A separate git grep of the other tracked .py/.md files for the two "
         f"patterns finds {len(other_hits_r3)} hit, the block's own premise at :34. The round-2 grep and its "
         "counts are unchanged."),
    ]
    vcheck4 = [
        ("1", "substantive", "Section 6(b) called the record's conclusion at RESULTS :7363 'unchanged', but the next "
         "sentence, :7363-7364 ('Reaching conventional power there needs n in the thousands per cell'), is a "
         "quantitative figure derived from the instruct FPR that the raw did not recompute; at the source's 0% "
         "conventional power is reached below 1,000 per arm.", "fixed",
         "Confirmed. :7363-7364 sits under 'Power at their own numbers' (:7354, anchors asserted), and the "
         "round-4 'thousands' grep finds it as the only carrier in the tracked .py/.md files (section 2). "
         "Section 6(b) now computes, at both instruct FPRs, the n per arm at which the registered criterion "
         f"reaches 0.80 and 0.90 power at Instruct. At 0%: {conv_src_txt}. At 0.3%: ≈ {cr['0.80']['first_grid_n']} "
         f"({cr['0.80']['power_at_first_grid_n']:.4f}) and ≈ {cr['0.90']['first_grid_n']} "
         f"({cr['0.90']['power_at_first_grid_n']:.4f}). The 'is unchanged' sentence is replaced by the fix's "
         f"wording. New row {row_thousands} (discrepant, locator RESULTS.md@{COMMIT}:7363-7364) carries row "
         f"{row_pw_ins}'s fork, and note 2(1) and section 12 condition 3 carry the figure: corrected under Code's "
         "transcription reading, a STOP otherwise. The JSON mirrors it in figures[], conditional_stops_block_23[2] "
         "and dependent_power_computed_new.retired_criterion_power.conventional_power_n. The checker's "
         f"{n_checker_r4} printed values (eight large-n powers and the twelve table cells, at 4 dp) reproduce "
         "(asserted). Method: the record's own clopper_pearson raises OverflowError from n = "
         f"{n_ovf} (asserted), so the scan uses the record's newcombe compiled with a stdlib CP. That path agrees "
         f"with the record's own on the 12 table cells and at n = {XCHK_N} (max abs difference {fast_vs_rec_max:.1e}). "
         "Adaptations: (a) the step-1 first n is given beside the fix's grid values ("
         f"{conv_fine_txt}); (b) the row is appended as row {row_thousands} rather than inserted after row "
         f"{row_pw_ins}, so the earlier rounds' row numbers stay valid; (c) reading 'per cell' as n per arm (the "
         "table's unit, :7356) is stated as Code's reading. The fix's 'At 0.3% the figures are ... ≈ 3500' is "
         f"given with its value ({cr['0.90']['power_at_first_grid_n']:.4f})."),
        ("2", "minor", "Row 19 and note 2(1) omitted the copy at scripts/b2r_analyze.py@bbc9ffe:16 (docstring, "
         "'power 0.000 at n=48').", "fixed",
         f"Confirmed by git grep with the checker's pattern: {len(grep_r4_hits['retired_instruct_power'])} hits, "
         + ", ".join(grep_r4_hits["retired_instruct_power"])
         + ". The grep now runs in the script, and its hits are asserted (section 2). Row "
         f"{row_pw_ins} and note 2(1) add 'other tracked: {R19_OTHER}'. Anchors are asserted on "
         "scripts/b2r_analyze.py :15 and :16. The n = 48 value is "
         f"{pw48['recomputed_instruct_fpr_0p003']:.5f} at .003 and {pw48['recomputed_instruct_fpr_0p000']:.5f} at "
         ".000, 0.000 at 3 dp at both (asserted). So no number and no STOP changes. Beyond the checker's list: "
         f"a second round-4 grep, for 'thousands', supplies row {row_thousands}'s locator (finding 1)."),
    ]
    V = ["", "## 13. Values-check", "", "### Round 1 (fixer pass)", "",
         "Round-1 rows are kept as written at round 1. Where round 2 changes a disposition, the round-2 table "
         "below says so (round-2 rows 1, 2 and 6 revise round-1 rows 6, 2 and 14).", "",
         "One adversarial values-check pass on the builder's version (script sha256 660f33a9...df31). The "
         "checker reports 110 claims checked and 14 findings, 3 substantive and 11 minor. Its rerun reproduced "
         "the builder's JSON byte for byte, and the .md apart from the stamp and command lines. Every finding was re-verified against the "
         "record (git show bbc9ffe) or the source (WebFetch, section 3) before it was applied. None was "
         "rejected.", "",
         "| # | grade | finding | disposition | detail |", "|---|---|---|---|---|"]
    for row in vcheck:
        V.append("| " + " | ".join(row) + " |")
    V += ["", "### Round 2", "",
          "A second checker pass on the round-1 script (sha256 eca0a8d5...8c41) reported 10 findings, 2 "
          "substantive and 8 minor. Its rerun reproduced the raw apart from the stamp and command lines. Code "
          "re-verified each finding against the record (git show bbc9ffe), the source (two round-2 WebFetch "
          "reads, section 3) or a computation in this script before applying it. All 10 are applied and none is "
          "rejected. Adaptations are stated in rows 5, 8 and 9. Cross-item: this JSON keeps every key the N2 script reads "
          "(stages.*, grid.n_scenarios_computed_new, decoding.*, and the 800/80 rows of "
          "source_points_dprime_computed_new.rows). The pooled rows carry new n values, so N2's 800/80 filter "
          "is unaffected. The JSON's sha256 changes with this run; the N2 raw records the sha of the N2vi JSON it "
          "read. A rerun of this script reproduces the raw apart from the stamp, HEAD and command lines and "
          "the N2 ROC JSON's sha256 in section 7, which moved between Code's runs because the N2 item was "
          "re-running concurrently; the compared values agreed at every run.", "",
          "| # | grade | finding | disposition | detail |", "|---|---|---|---|---|"]
    for row in vcheck2:
        V.append("| " + " | ".join(row) + " |")
    V += ["", "### Round 3", "",
          "A third, strict checker pass on the round-2 script (sha256 61035dbf...f4a2) reported 6 findings, 2 "
          "substantive and 4 minor, and no open items from round 2. Its rerun reproduced both outputs apart from "
          "the stamp and command lines and the N2 ROC JSON's sha256, which N2 had regenerated after this item's "
          "last run. Its redaction check found 0 verbatim values. Its independent recomputation agreed with every "
          "figure it recomputed. It judged the STOP logic licensed, with no active STOPs and the four block :23 conditions "
          "correctly framed, apart from the two gaps in rows 1 and 6 below. Code re-verified each finding against the "
          "record (git show bbc9ffe), the source (two round-3 WebFetch reads, section 3) or a computation in this "
          "script before applying it. All 6 are applied, none is rejected, and adaptations are stated in rows 1 "
          "and 4. Round-1 and round-2 text above is kept as written at its round. Round 3 revises it as follows: "
          "old row 16 (lineage) and old row 17 (retired power) are each split in two, so later rows move down "
          "by two. Rows 12-13 carry the derived ratio and two more carriers. The round-2 header's sentence on "
          "the N2 sha is superseded by row 3. Cross-item: the keys the N2 script reads (stages.*, grid.*, "
          "decoding.*, the 800/80 rows) are unchanged in content; this JSON's sha256 changes with this run.", "",
          "| # | grade | finding | disposition | detail |", "|---|---|---|---|---|"]
    for row in vcheck3:
        V.append("| " + " | ".join(row) + " |")
    V += ["", "### Round 4", "",
          "A fourth checker pass on the round-3 script (sha256 31187a80...ccd1) reported 2 findings, 1 "
          "substantive and 1 minor, and no open items from round 3. Code re-verified each finding against the "
          f"record (git show and git grep at {COMMIT}) and a computation in this script before applying it. Both "
          "are applied as their fixes say, none is rejected, and adaptations are stated in row 1. Earlier rounds' "
          f"text above is kept as written at its round. Round 4 adds row {row_thousands} at the end of section 0, "
          "so rows 1-23 keep their numbers. No source was re-read in round 4 (no WebFetch). Cross-item: the keys "
          "the N2 script reads (stages.*, grid.*, decoding.*, the 800/80 rows) are unchanged in content. This "
          "JSON's sha256 changes with this run, so the N2 raw's recorded N2vi JSON sha is stale until N2 re-runs; "
          "that run belongs to the N2 item, and Code did not run it.", "",
          "| # | grade | finding | disposition | detail |", "|---|---|---|---|---|"]
    for row in vcheck4:
        V.append("| " + " | ".join(row) + " |")

    out_lines = H + S + L + V

    # ---------------------------------------------------------------- JSON
    stages_json = {}
    for s in STAGES:
        src = SOURCE_V1[s]
        stages_json[s] = {
            "tpr": src["tpr"],
            "n_injected": None,
            "n_control": None,
            "fpr": src["fpr"],
            "introspection_rate": src["introspection_rate"],
            "config": f"aggregate over L in {V1_FIG21_LAYERS} x alpha in {V1_FIG21_ALPHAS} ({n_cfg} configs), "
                      "per v1 Figure 21 caption",
            "best_of_grid": False,
            "provenance": f"from the source, read by Code on {SOURCE_READ_DATE_UTC} at {URL_V1}: Appendix C "
                          "prose describing Figure 21 (v1 only)",
            "source_text_paraphrase": SOURCE_V1_TEXT_PARAPHRASE[s],
            "record_addendum_tpr": cmp_rows[s]["record_a_tpr"],
            "record_addendum_fpr": cmp_rows[s]["record_a_fpr"],
            "record_results_their_fpr": cmp_rows[s]["record_b_fpr"],
            "record_addendum_sensitivity": cmp_rows[s]["record_a_sens"],
            "tpr_matches_source": cmp_rows[s]["tpr_match"],
            "fpr_matches_source": cmp_rows[s]["fpr_match"],
            "source_tpr_minus_fpr_pp": cmp_rows[s]["source_tpr_minus_fpr_pp"],
            "n_note": "not stated by the source; see grid.n_scenarios_computed_new",
        }
    j = {
        "item": "N2(vi)",
        "block": {"path": BLOCK, "sha256": block_sha, "line": 35},
        "record_commit": commit_full,
        "script": {"path": script_rel, "sha256": script_sha},
        "resolved": True,
        "method": "text",
        "method_note": "values stated in prose in arXiv:2603.21396v1 Appendix C (describing Figure 21); not in a "
                       "table; the record states no recovery method (RESULTS.md@bbc9ffe:7326-7327); Figure 21 is "
                       "an image (olmo-staged-introspection.png) with no data labels; this audit digitized nothing",
        "not_checked": {"note_sentence_and_F2_points": f"{PREFLIGHT}@{COMMIT} lists the note draft and F1/F2 SVGs "
                                                       "as MISSING"},
        "figures": figures,
        "source": {
            "citation": "Macar, Yang, Wang, Wallich, Ameisen, Lindsey 2026, Mechanisms of Introspective "
                        "Awareness, arXiv:2603.21396",
            "version_of_values": "v1 (2026-03-22)",
            "versions": [{"version": v, "date": dt, "url": u, "olmo_content": what}
                         for v, dt, u, what in SOURCE_VERSIONS],
            "read_by_code_utc_date": SOURCE_READ_DATE_UTC,
            "read_with": "WebFetch (model-processed page rendering); each v1 App. C sentence returned verbatim in 2 fetches, agreeing with a 3rd paraphrase",
            "fixer_pass_reads": [{"url": u, "what": what} for u, what in FIXER_READS],
            "round2_reads": [{"url": u, "what": what, "utc_date": ROUND2_READ_DATE_UTC} for u, what in ROUND2_READS],
            "round3_reads": [{"url": u, "what": what, "utc_date": ROUND3_READ_DATE_UTC} for u, what in ROUND3_READS],
            "exp03_default_test_concepts": {
                "defined_in": "experiments/03_behavioral_robustness.py (a literal list in that file; not imported)",
                "n": exp03_n_read1, "read1_entries": EXP03_CONCEPTS_READ1, "read2": EXP03_CONCEPTS_READ2,
                "equals_b2_concepts_canonical_in_order_computed_new": exp03_same_order,
                "b2_concepts_provenance_cites": b2c["provenance"]["concepts_source"],
                "identity_with_01": "Code's reading from one model-processed read (read 1); read 2 corroborates "
                                    "only the count, end entries and import status; not established"},
            "v1_figure21_image": V1_FIG21_IMAGE,
            "quote": {"text": SOURCE_QUOTE, "attribution": SOURCE_QUOTE_ATTRIB},
            "urls_read": [URL_ABS, URL_ABS_V5, URL_V1, URL_V2, URL_V3, URL_V4, URL_V5, URL_GH_README,
                          URL_RAW_README, URL_GH_MODEL_UTILS, URL_RAW_MODEL_UTILS, URL_RAW_EXP03, URL_GH_COMMITS],
            "later_versions_official_checkpoint_tpr_minus_fpr": {
                "config": "v2-v5 Table 3, a LoRA fine-tuning study on the OLMo SFT checkpoint at L=25, alpha=4; "
                          "the starred SFT*/DPO* rows are the official checkpoints (values as printed, '+/-' "
                          "meaning not recorded)",
                "sft": "-11.5 +/- 2.4", "dpo": "+9.8 +/- 0.5",
                "introspection_pct": {"sft": "1.7 +/- 0.2", "dpo": "3.5 +/- 0.3"},
            },
        },
        "grid": {
            "layers_v1_caption": V1_FIG21_LAYERS,
            "alphas_v1_caption": V1_FIG21_ALPHAS,
            "n_configs": n_cfg,
            "aggregation": "aggregate over all 20 configs (caption); released code pools all trials per model "
                           "(compute_metrics_from_results -> summary_stats.json) -- that the figure used it is "
                           "Code's inference",
            "code_default_layer_fractions": fr,
            "code_layer_indices_int_n_layers_x_f": idx0,
            "code_layer_indices_round_n_layers_x_f": ridx0,
            "n_layers_record": n_layers,
            "caption_vs_code_layers_differ_at": [V1_FIG21_LAYERS[3], idx0[3]],
            "readme_ls_as_fractions_to_indices": readme_idx,
            "readme_model_keys_rejected_by_argparse": rejected,
            "per_concept_per_cell": {"injected": inj_per_concept, "control": ctl_per_concept},
            "n_scenarios_computed_new": scen,
            "n_stated_by_source": None,
            "ratio_to_ours_computed_new": {
                "record_figure": "~33× ours (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:32-33; RESULTS.md@bbc9ffe:7440)",
                "our_injected_per_stage_as_run": our_n,
                "our_n_locators": "RESULTS.md@bbc9ffe:7440 'our 24/24'; :7358 '24 (as run)'",
                "rows": ratio_rows},
        },
        "stages": stages_json,
        "dependent_power_computed_new": {
            "code": f"record's clopper_pearson/newcombe (scripts/b2_analyze.py@{COMMIT}) and binom_pmf "
                    f"(valence_core/stats.py@{COMMIT}); exact enumeration; CP 95% two-sided",
            "own_vs_record_cp_max_abs_diff_n96": cp_agree,
            "g3a_joint": {"rule": "min CP-lower{base,sft} > max CP-upper{dpo,instruct}, n = 96 per stage, "
                                  "independent binomial FPR counts",
                          "record_printed": 0.9642, "record_pair_printed": 0.9825,
                          "at_record_inputs": jp_rec, "pair_at_record_inputs": pair_rec,
                          "at_source_instruct_fpr_0": jp_src, "pair_at_source_instruct_fpr_0": pair_src,
                          "valuescheck_json_detail": vc_power,
                          "at_record_inputs_3dp": f"{jp_rec:.3f}",
                          "pairs_at_record_inputs": pairs_rec, "pairs_at_source_instruct_fpr_0": pairs_src,
                          "weakest_pair_at_record_inputs": weak_rec, "weakest_pairs_at_source_inputs": weak_src,
                          "pairs_equal_to_0_9825_at_4dp": pairs_equal_9825,
                          "record_exactness_claims": f"RESULTS.md@{COMMIT}:7194, :7251, :7269-7270",
                          "cause_variants_computed_new": var_rows, "monte_carlo_se_computed_new": mc_rows,
                          "cause": "not identified; a simulation of ~1e4-1e5 draws is a candidate, not established"},
            "record_p28": {"locators": f"RESULTS.md@{COMMIT}:6955, :7091", "record": "p ≈ .28",
                           "test_code_reading": "exact binomial lower tail P(X <= k | n, .029)",
                           "k": k43, "n": n43, "source": f"data/olmo/b2r_explore_dpo.json@{COMMIT} hit, inj_decidable",
                           "computed_new": p28},
            "retired_criterion_power": {"rule": "P(Newcombe lower > 0), n per arm all decidable, "
                                                "hits ~ Bin(n, TPR), FA ~ Bin(n, FPR)",
                                        "prune_below": PRUNE, "rows": pw_rows, "cells_agreeing_3dp": n_pw_agree,
                                        "record_description": "power at the source's own rates ('their own "
                                                              "Instruct rates', ADDENDUM :52-53; 'Instruct's own "
                                                              "reported rates', RESULTS :7330-7331; 'Power at their "
                                                              "own numbers', RESULTS :7354)",
                                        "instruct_cells_differing_at_source_rates_3dp":
                                            [r["n_per_arm"] for r in pw_src_differs],
                                        "conventional_power_n": {
                                            "record_figure": "'Reaching conventional power there needs n in the "
                                                             "thousands per cell' (RESULTS.md@bbc9ffe:7363-7364), "
                                                             "Instruct, under 'Power at their own numbers' (:7354)",
                                            "unit": "n per arm, all decidable ('per cell' read as n per arm, the "
                                                    "table's unit at :7356; Code's reading)",
                                            "tpr": ins_tpr, "bars": list(CONV_BARS),
                                            "grid": f"step {CONV_STEP} from n = {CONV_START + CONV_STEP}; then step "
                                                    "1 between the first grid point at or above each bar and the "
                                                    "one before it",
                                            "code": "the record's newcombe (scripts/b2_analyze.py@bbc9ffe, by AST) "
                                                    "compiled with a stdlib Clopper-Pearson (own_cp_fast) and the "
                                                    "stdlib pmf; the record's clopper_pearson raises OverflowError "
                                                    f"from n = {n_ovf}",
                                            "record_cp_overflow_from_n": n_ovf,
                                            "crosscheck_vs_record_path_max_abs_diff": fast_vs_rec_max,
                                            "crosscheck_values": len(fast_vs_rec),
                                            "crosscheck_n750_record_path": p750_rec,
                                            "cp_fast_vs_record_max_abs_diff": cp_fast_vs_rec,
                                            "at_source_instruct_fpr_0": conv["source"],
                                            "at_record_instruct_fpr_0p003": conv["record"],
                                            "checker_round4_values_reproduced_4dp": checker_r4_got,
                                            "record_7363_binding_holds_both_inputs": True,
                                            "thousands_holds": {"at_record_0p003": cr["0.80"]["first_grid_n"] >= 1000,
                                                                "at_source_0": cs["0.80"]["first_grid_n"] >= 1000}}},
        },
        "source_points_dprime_computed_new": {
            "note": "context for N2(v); counts = rate x n rounded half-up; log-linear d'; one-sided Fisher "
                    "upper tail (excess hits over false alarms); n assumed, per row: 'unit' is per (layer, alpha) "
                    "configuration (800/80, 5000/500) or pooled per stage over 20 configurations (16000/1600, "
                    "100000/10000); the source's rates are pooled, so the per-configuration n applied to them is "
                    "a unit mismatch; pooled counts treat clustered trials as independent",
            "rows": dp_rows,
            "design_seat_block_34": seat,
            "design_seat_confirmed_at_800_80": seat_ok,
            "design_seat_agrees_at_16000_1600": seat_ok_pooled,
            "design_seat_check": seat_check,
            "n2_consistency_check": n2_cmp,
        },
        "carriers": {
            "patterns_over": [f"{RESULTS}@{COMMIT}", f"{ADDENDUM}@{COMMIT}"],
            "figures": {k: {"label": lab, "regex": rx,
                            "carriers": {pth: ln for pth, ln in inc.items()},
                            "unrelated": {pth: {str(a): b for a, b in u.items()} for pth, u in un.items()},
                            "other_tracked": other_by_key[k]}
                        for k, (lab, rx, inc, un) in CARRIERS.items()},
            "other_tracked_grep": OTHER_GREP,
            "other_tracked_carriers": {k: v[0] for k, v in OTHER_CARRIERS.items()},
            "other_tracked_unrelated": OTHER_UNRELATED,
            "other_tracked_grep_round3": OTHER_GREP_R3,
            "other_tracked_carriers_round3": {k: v[0] for k, v in OTHER_CARRIERS_R3.items()},
            "n_rows_split_round3": {"with_premise_record_inference": N_INFERENCE_LINES,
                                    "as_the_source_n": N_AS_SOURCE_LINES},
            "greps_round4": {k: {"label": lab, "regex": rx, "pathspec": GREP_R4_PATHSPEC, "carriers": car,
                                 "unrelated": unr, "hits": grep_r4_hits[k]}
                             for k, (lab, rx, car, unr) in GREP_R4.items()},
        },
        "decoding": {"source_paper_v1_and_code_5d5d9b4": dec, "paper_v1_text": SOURCE_V1_DECODING_TEXT},
        "lineage": ("Source: paper names OLMo-3.1-32B base/SFT/DPO/instruct (no HF ids); released code "
                    "src/model_utils.py MODEL_NAME_MAP at 5d5d9b4 maps olmo_base/olmo_sft/olmo_dpo/olmo_instruct "
                    "to allenai/Olmo-3-1125-32B, allenai/Olmo-3.1-32B-Instruct-SFT, "
                    "allenai/Olmo-3.1-32B-Instruct-DPO, allenai/Olmo-3.1-32B-Instruct with no revision pinned. "
                    f"Record manifest repos match {lin_match}/4; revision-level match not determinable. Status: "
                    "our four repos/revisions reproduced (manifest.json@bbc9ffe); the match itself log-only "
                    "(RESULTS.md@bbc9ffe:12565-12569), computed-new against Code's WebFetch reading (the source "
                    "half is not a committed artifact)."),
        "lineage_rows": lin_rows,
        "notes": notes,
        "stops": [],
        "conditional_stops_block_23": [{k: v for k, v in c_.items()} for c_ in conditional],
        "values_check": ([{"round": 1, "finding": f"{n} ({g}): {t}", "action": a, "detail": dt}
                          for n, g, t, a, dt in vcheck]
                         + [{"round": 2, "finding": f"{n} ({g}): {t}", "action": a, "detail": dt}
                            for n, g, t, a, dt in vcheck2]
                         + [{"round": 3, "finding": f"{n} ({g}): {t}", "action": a, "detail": dt}
                            for n, g, t, a, dt in vcheck3]
                         + [{"round": 4, "finding": f"{n} ({g}): {t}", "action": a, "detail": dt}
                            for n, g, t, a, dt in vcheck4]),
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out_lines) + "\n")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(j, fh, indent=1, ensure_ascii=False, sort_keys=False)
        fh.write("\n")
    print(f"wrote {out_path}")
    print(f"wrote {json_path}")
    print(f"TPR match {n_tpr}/4; FPR match {n_fpr}/4; lineage {lin_match}/4; layers int {idx0} round {ridx0} vs "
          f"caption {V1_FIG21_LAYERS}; joint power {jp_rec:.4f} (rec inputs) / {jp_src:.4f} (src); retired-power "
          f"cells agreeing {n_pw_agree}/8; seat arithmetic at 800/80 {sum(seat_ok.values())}/4, at 16000/1600 "
          f"{sum(seat_ok_pooled.values())}/4; weakest pair {weak_rec}; carriers asserted {len(CARRIERS)} figures; "
          f"N2 consistency {n2_cmp['status']}; conventional power at Instruct (n per arm, 0.80 / 0.90): source "
          f"{cs['0.80']['first_grid_n']} / {cs['0.90']['first_grid_n']}, record {cr['0.80']['first_grid_n']} / "
          f"{cr['0.90']['first_grid_n']} (step-1 first n {cs['0.80']['first_n_step1']} / {cs['0.90']['first_n_step1']}, "
          f"{cr['0.80']['first_n_step1']} / {cr['0.90']['first_n_step1']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
