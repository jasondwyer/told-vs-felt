#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12(iv): third-party materials and licenses.

Part id N12-licenses. Block: AUDIT-note-release-v1_2.md (sha256 8cd8a9ac...3841),
N12 at block lines 72-85, rules at section 0.

READ-ONLY ON THE RECORD. Tracked content is read at a commit resolved once at
start (`git -C <repo> rev-parse HEAD`) through read-only git plumbing
(ls-tree, cat-file, log, rev-list, for-each-ref); history-wide checks
enumerate every commit reachable from any local ref (`git rev-list --all`).
The block, the clone and the HF cache are read from disk. Nothing is written
except the two output files named below. No git command is ever run inside
jlens-qwen36/: the clone is read only by plain file reads (its LICENSE,
README, .git/config, .git/HEAD, packed-refs, .git/index, and its object
store -- loose objects and the pack, parsed here in Python with zlib, every
object's sha1 re-verified) and an os.walk for the byte-identity check.

NO NETWORK. The script downloads nothing. The external facts it reports
(the source repositories' licenses, the upstream jlens-qwen36 file list, the
Hugging Face model-card licenses, the lens and dataset cards, GitHub's terms)
were read by Code with the WebFetch tool on 2026-10-08 (UTC, Code's clock;
the builder's reads, then the round-1 fixer's at 04:08 UTC, then the round-2
fixer's at about 06:20 UTC: the Macar et al. paper on arXiv and its HTML
rendering, and the Lindsey (2025) page; then the round-3 fixer's at about
09:20 UTC: the Lindsey page's trial prompt and the paper's Table 4, each
compared sentence by sentence with the record; then the round-4 fixer's at
10:59 UTC: the transformer-circuits.pub home page, for a site-wide license
statement) and are carried below in WEB_READS as
recorded constants, each with the URL read. Comparisons of a page's text with
the record were made by the fetch tool's model, not byte for byte, and are
labelled so. The script prints them labelled "[recorded WebFetch read]"; it
does not recompute them. Everything else is computed by this script from the
record, or from local files named in the output (the two local lens .npz
files are read only as zip directories plus their small .npy headers and two
8-byte scalars).

PERSONAL DATA. Third-party handles or names that are not needed for an
attribution row are never written: the one such repository id found in the
record is matched by its sha256 below, and printed redacted (and counted as a
redaction). Authors are named only as citations (Macar et al. 2026;
Lindsey 2025). IP-literal URL hosts are counted, never printed.

REDACTION. Every snippet of repository text the script prints passes through
redact(): IPv4 addresses, provider-style tokens (sk-, rp_, hf_, ghp_, AKIA),
SSH public-key bodies and PEM private-key headers are replaced by
first4 + '...' + length + sha256[:8]. Pattern redactions and redacted ids are
counted separately and both are printed.

Outputs: results/raw/2026-10-08_note-N12-licenses.md and .json (the defaults of
--out and --json-out; --out-dir DIR writes whichever of the two is not given
explicitly into DIR under its default basename).
Usage: jlens-qwen36/.venv/bin/python scripts/audit_note_N12_licenses.py
       [--out MD] [--json-out JSON] [--out-dir DIR]

Release run (the PI's answer of 2026-10-12, "Yes to all five; tag it"): the round-9 rule changes
(two id entries, two id rules, host rules H1-H4) are applied as confirmed (question 2), and the
outputs are NEW dated raws; the script refuses to write any path git already tracks:
    jlens-qwen36/.venv/bin/python -B scripts/audit_note_N12_licenses.py \
        --out results/raw/2026-10-12_note-N12-licenses-release.md \
        --json-out results/raw/2026-10-12_note-N12-licenses-release.json
Every statement about this repository's own license (section 5's statement, the section-6
row, section 7 item 2, the pass line's clause) is computed from the tree at the commit read
(root-level license texts identified by their opening lines, and LICENSING.md), not fixed
text; the section-5 count rule RX_LF is unchanged. A text counts as this repository's license
only when it is identified by its opening lines AND, where LICENSING.md is tracked, its sha256
is listed there; any other root-level text goes to the PI to read, with the reason printed.
The section-5 count lines state RX_LF's scope (exact name, optional alphabetic extension, any
depth, NOTICE included) and name any root-level license text that rule does not match.
Release (L3): "this audit's own files" is one rule, RX_AUDIT_FILE: every audit raw
(results/raw/*_note-*, any date) and every scripts/audit_note_*.py. The round-9 rules (H1-H3, the
id rules) and section 2f's projection both use it, so the release raws committed after the tag
are audit files like the 2026-10-08 ones. The confirmed rules are applied as worded, carrier by
carrier: an id carried only by audit files that is a fragment of a recorded-read URL (WEB_READS),
cut short by an excerpt window, is a known id (question 2's "fragments of recorded-read URLs");
the owner part alone of this repository's id stays outside the prefix rule (its confirmed guard);
a host carried only by audit files is
classed (H3) when it is a listed host or a listed host cut short by an excerpt window. A
document's allowed paths (DOC_HOSTS) and the Global Workspace paths are checked against every path
of the host, as in round 9; a path outside them passes only when this audit's own files alone
carry it and it is a proper prefix of an allowed path (an excerpt window's cut of it) -- Code's
narrow reading of the confirmed rules, flagged for the PI. Anything else
stays UNCLASSIFIED, for the PI (no new rule). Section 2f projects the sweeps over the audit files
untracked on disk at the run, and a closing self-check projects this run's own two outputs; the
combined verdict is printed in 2f, section 7 item 8 and the round-4 values-check row.
"""
from __future__ import annotations

import ast
import datetime
import hashlib
import io
import json
import tokenize
import os
import re
import struct
import subprocess
import sys
import zipfile
import zlib
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLONE = os.path.join(REPO, "jlens-qwen36")
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
DEFAULT_MD = os.path.join(REPO, "results/raw/2026-10-08_note-N12-licenses.md")
DEFAULT_JSON = os.path.join(REPO, "results/raw/2026-10-08_note-N12-licenses.json")
OUT_MD, OUT_JSON = DEFAULT_MD, DEFAULT_JSON  # resolved from the arguments in main()
# Release (L3; the rules the PI confirmed on 2026-10-12, question 2, read as worded): this audit's own files --
# every audit raw (results/raw/*_note-*, any date) and every scripts/audit_note_*.py. One definition, used by the
# round-9 rules and by section 2f's projection (which before this read only scripts/audit_note_* and the
# 2026-10-08 raws).
RX_AUDIT_FILE = re.compile(r"^(?:scripts/audit_note_[^/]*\.py|results/raw/[^/]*_note-[^/]*)$")
HF_CACHE_QWEN = os.path.expanduser(
    "~/.cache/huggingface/hub/models--mlx-community--Qwen3.6-27B-4bit/refs/main")

# ---------------------------------------------------------------------------
# Recorded external reads (Code, WebFetch, 2026-10-08 UTC). NOT computed here.
# ---------------------------------------------------------------------------
MACAR_PIN = "5d5d9b485e293dc766c3a056cfe50283a7e435b6"
JLENS_CLONE_COMMIT = "d788bc321dc7bad4ed33e1465b306389959b0046"

# The 62 blob paths of WeZZard/jlens-qwen36 at the clone's commit, from
# https://api.github.com/repos/WeZZard/jlens-qwen36/git/trees/<d788bc3...>?recursive=1
# (truncated: false; the API's own total was 62).
JLENS_UPSTREAM_BLOBS = [
    ".gitignore", ".python-version", "LICENSE", "README.md", "pyproject.toml",
    "sitecustomize.py", "uv.lock",
    "data/corpus/.gitkeep", "data/lens/.gitkeep", "data/lens/full_depth_fit.log",
    "data/lens/full_depth_fit_v2.log",
    "jlens_qwen/__init__.py", "jlens_qwen/analytic.py", "jlens_qwen/analytic_attn.py",
    "jlens_qwen/analytic_layer.py", "jlens_qwen/custom_gdn_patch.py",
    "jlens_qwen/custom_gdn_vjp.py", "jlens_qwen/fit.py", "jlens_qwen/fit_analytic.py",
    "jlens_qwen/gdn_backward.py", "jlens_qwen/interventions.py", "jlens_qwen/lens.py",
    "jlens_qwen/model.py", "jlens_qwen/patch_gdn.py", "jlens_qwen/perf.py",
    "jlens_qwen/probing.py", "jlens_qwen/prompts.py", "jlens_qwen/serve.py",
    "scripts/bench_decode.py", "scripts/export_static.py",
    "scripts/gen_decode_gate_golden.py", "scripts/intervention_sanity.py",
    "scripts/measure_gbeta_gap.py", "scripts/run_experiments.py", "scripts/run_fit.py",
    "scripts/smoke_model.py", "scripts/spike_jacobian.py", "scripts/spike_jacobian_v2.py",
    "scripts/verify_analytic_layer.py", "scripts/workspace_range.py",
    "tests/golden/decode_gate_golden.json", "tests/test_analytic_attention.py",
    "tests/test_chain_indexing.py", "tests/test_decode_gate.py",
    "tests/test_lens_resolution.py",
    "web/index.html",
    "docs/lenses.md", "docs/perf/LEDGER.md", "docs/perf/README.md",
    "docs/perf/decode-01.md", "docs/perf/decode-02.md", "docs/perf/decode-03.md",
    "docs/perf/decode-04.md", "docs/perf/decode-05.md", "docs/perf/fit-01.md",
    "docs/perf/fit-02.md", "docs/perf/fit-03.md", "docs/perf/fit-04.md",
    "docs/perf/fit-05.md", "docs/perf/ui-01.md", "docs/perf/ui-02.md",
    "assets/screenshot_blackmail.png",
]

WEB_READS = {
    "macar_repo_api": {
        "url": "https://api.github.com/repos/safety-research/introspection-mechanisms",
        "result": {"full_name": "safety-research/introspection-mechanisms",
                   "license": None, "default_branch": "main",
                   "pushed_at": "2026-04-16T23:16:54Z", "visibility": "public",
                   "archived": False, "created_at": "2025-11-10T22:50:25Z"}},
    "macar_web_page": {
        "url": "https://github.com/safety-research/introspection-mechanisms",
        "result": {"sidebar_license": None,
                   "readme_has_license_section": True,
                   "readme_has_citation_section": True}},
    "macar_commit_at_pin": {
        "url": ("https://api.github.com/repos/safety-research/introspection-mechanisms/"
                f"commits/{MACAR_PIN}"),
        "result": {"sha": MACAR_PIN, "committer_date": "2026-04-16T23:16:47Z",
                   "message_first_line": "Fix stale output paths and code."}},
    "macar_root_contents_at_pin": {
        "url": ("https://api.github.com/repos/safety-research/introspection-mechanisms/"
                f"contents/?ref={MACAR_PIN}"),
        "result": {"entries": [".gitignore", "README.md", "experiments", "plotting",
                               "requirements.txt", "src"],
                   "license_like_entries": []}},
    "macar_license_at_pin": {
        "url": ("https://raw.githubusercontent.com/safety-research/introspection-mechanisms/"
                f"{MACAR_PIN}/LICENSE"),
        "result": {"http_status": 404}},
    "macar_license_on_main": {
        "url": ("https://raw.githubusercontent.com/safety-research/introspection-mechanisms/"
                "main/LICENSE"),
        "result": {"http_status": 404}},
    "macar_readme_at_pin": {
        "url": ("https://raw.githubusercontent.com/safety-research/introspection-mechanisms/"
                f"{MACAR_PIN}/README.md"),
        "result": {"license_section_gist": ("a research-purposes release statement that "
                                            "names no license and refers readers to the "
                                            "paper for responsible-use considerations"),
                   "license_section_short_quote": "released for research purposes",
                   "other_occurrences_of_word_license": 0,
                   "citation_bibtex_key": "macar2026mechanisms",
                   "citation_title": "Mechanisms of Introspective Awareness"}},
    "macar_01_concept_injection_defs": {
        "url": ("https://raw.githubusercontent.com/safety-research/introspection-mechanisms/"
                f"{MACAR_PIN}/experiments/01_concept_injection.py"),
        "note": "read in two parts (offset 0 and offset 100000 of 132931 characters)",
        "result": {"defs": ["filter_messages_for_model", "parse_args", "run_experiment",
                            "sanitize_model_name_for_display", "create_sweep_plots",
                            "create_trial_type_comparison_plots",
                            "create_cross_model_comparison_plots",
                            "extract_example_transcripts", "main"],
                   "license_header": None,
                   "detection_scoring": ("LLM judge (LLMJudge, batch_evaluate, "
                                         "compute_detection_and_identification_metrics "
                                         "imported from eval_utils); a string check "
                                         "check_concept_mentioned imported from "
                                         "steering_utils; no keyword lists in this file")}},
    "macar_vector_utils_defs": {
        "url": ("https://raw.githubusercontent.com/safety-research/introspection-mechanisms/"
                f"{MACAR_PIN}/src/vector_utils.py"),
        "result": {"defs": ["create_concept_prompts", "create_contrastive_pair",
                            "extract_concept_vector", "extract_concept_vector_with_baseline",
                            "extract_concept_vector_simple",
                            "extract_concept_vector_no_baseline", "cosine_similarity",
                            "save_concept_vector", "load_concept_vector",
                            "get_baseline_words", "get_concept_pair",
                            "extract_concept_vectors_batch",
                            "analyze_vector_underspecification",
                            "format_prompt (nested)", "batched_extract (nested)"],
                   "constants": ["DEFAULT_BASELINE_WORDS", "CONCEPT_PAIRS"],
                   "license_header": None}},
    "wezzard_repo_api": {
        "url": "https://api.github.com/repos/WeZZard/jlens-qwen36",
        "result": {"full_name": "WeZZard/jlens-qwen36",
                   "license": {"key": "apache-2.0", "spdx_id": "Apache-2.0",
                               "name": "Apache License 2.0"},
                   "default_branch": "main", "pushed_at": "2026-09-08T07:21:56Z",
                   "visibility": "public", "fork": False}},
    "wezzard_tree_at_clone_commit": {
        "url": ("https://api.github.com/repos/WeZZard/jlens-qwen36/git/trees/"
                f"{JLENS_CLONE_COMMIT}?recursive=1"),
        "result": {"truncated": False, "n_blobs": 62,
                   "blobs": "JLENS_UPSTREAM_BLOBS in this script"}},
    # --- fixer's reads (values-check), WebFetch 2026-10-08 04:08 UTC -------------
    "neuronpedia_lens_hf": {
        "url": "https://huggingface.co/api/models/neuronpedia/jacobian-lens",
        "result": {"id": "neuronpedia/jacobian-lens",
                   "sha": "b25d72a96b79c8e309d6625955a98751da47e67a",
                   "gated": False, "private": False,
                   "lastModified": "2026-09-25T21:08:20.000Z",
                   "cardData_license": "mit",
                   "qwen36_27b_files": [
                       "qwen3.6-27b/jlens/Salesforce-wikitext/CREDIT.md",
                       "qwen3.6-27b/jlens/Salesforce-wikitext/"
                       "Qwen3.6-27B_jacobian_lens_n1000.pt"]}},
    "neuronpedia_lens_credit_md": {
        "url": ("https://huggingface.co/neuronpedia/jacobian-lens/raw/main/qwen3.6-27b/"
                "jlens/Salesforce-wikitext/CREDIT.md"),
        "result": {"length_chars": 90,
                   "gist": ("one sentence crediting the lens's training to a named author of "
                            "Anthropic Interpretability (name not reproduced here; the record's "
                            "own credit line is cited by locator)")}},
    "wezzard_releases": {
        "url": "https://api.github.com/repos/WeZZard/jlens-qwen36/releases",
        "result": {
            "v0.1-demo": {"published_at": "2026-07-07T18:41:27Z",
                          "assets": {"jlens-qwen3.6-27b-4bit-12prompt-23layer.npz": 1205868454}},
            "v0.2-fulldepth": {"published_at": "2026-07-08T15:38:17Z",
                               "assets": {
                                   "jlens-qwen3.6-27b-4bit-20prompt-63layer.npz.part-aa": 1782579200,
                                   "jlens-qwen3.6-27b-4bit-20prompt-63layer.npz.part-ab": 1520451198}},
            "v0.3-qwen38-n1000": {"published_at": "2026-09-08T06:55:44Z",
                                  "note": "a Qwen3.8 lens, after the record's lens acquisition"},
            "release_bodies_mention_a_license": False}},
    "anthropic_jacobian_lens_api": {
        "url": "https://api.github.com/repos/anthropics/jacobian-lens",
        "result": {"full_name": "anthropics/jacobian-lens",
                   "license": {"key": "apache-2.0", "spdx_id": "Apache-2.0",
                               "name": "Apache License 2.0"},
                   "default_branch": "main", "pushed_at": "2026-10-07T19:51:20Z",
                   "visibility": "public", "fork": False, "archived": False}},
    "c4_dataset_hf": {
        "url": "https://huggingface.co/api/datasets/allenai/c4",
        "result": {"id": "allenai/c4", "sha": "1588ec454efa1a09f29cd18ddd04fe05fc8653a2",
                   "gated": False, "cardData_license": ["odc-by"]}},
    "github_tos": {
        "url": "https://docs.github.com/en/site-policy/github-terms/github-terms-of-service",
        "result": {"section": "D.5 License Grant to Other Users",
                   "gist_of_webfetch_summary": (
                       "making a repository public grants other GitHub users a nonexclusive, "
                       "worldwide licence to use, display and perform its content through "
                       "GitHub and to reproduce it on GitHub as GitHub's features allow "
                       "(including forking); further rights need a licence; a user posting "
                       "content they did not create must make sure it is licensed for these "
                       "uses"),
                   "verbatim": False}},
    # --- round-2 fixer's reads, WebFetch 2026-10-08 ~06:20 UTC -------------------
    "macar_paper_arxiv_abs": {
        "url": "https://arxiv.org/abs/2603.21396",
        "result": {"title": "Mechanisms of Introspective Awareness",
                   "citation": "Macar et al. 2026", "n_authors": 6,
                   "author_list_includes_the_lindsey_2025_author": True,
                   "license_label": "CC BY 4.0",
                   "license_link": "http://creativecommons.org/licenses/by/4.0/",
                   "versions": {"v1": "2026-03-22", "v5 (current)": "2026-06-10"},
                   "html": "https://arxiv.org/html/2603.21396v5"}},
    "macar_paper_html_app_a": {
        "url": "https://arxiv.org/html/2603.21396v5",
        "note": ("page text 182,210 characters, read at offsets 0, 50000, 100000 and 150000 "
                 "(the whole page); comparisons with the record by the fetch tool's model, "
                 "not byte for byte"),
        "result": {"location": "Appendix A 'Full Prompts', Table 4 'Full prompt for the "
                               "introspective awareness task'",
                   "turns_in_order": ["User: the framing paragraph",
                                      "Model: the acknowledgement",
                                      "User: the trial question",
                                      "Model: [response placeholder]"],
                   "system_message": False,
                   "framing_sentences": 5,
                   "framing_length_estimate_chars": "about 470-480",
                   "framing_first_and_last_eight_words_match_record": True,
                   "framing_full_wording_compared_by_this_fixer": False,
                   "framing_wording_per_round2_checker_read": "matches in wording and punctuation",
                   "framing_dashes_around_thoughts": "two hyphens each side (as rendered)",
                   "framing_quotes_around_thoughts": "straight double quotes",
                   "ack_equals_record_ACK": True,
                   "trial_question_equals_record_modulo_placeholder": True,
                   "trial_question_placeholder": "{trial_num} (the record's is {n})"}},
    "macar_paper_html_app_b": {
        "url": "https://arxiv.org/html/2603.21396v5",
        "result": {"B1_concepts": "the 50 original concepts are credited to Lindsey (2025)",
                   "B1_prints_the_50_concepts": False,
                   "B2_prints_the_100_baseline_words": False,
                   "B2_extraction_template": "'Tell me about {c}', through the model's chat "
                                             "template; the record's is 'Tell me about {word}'",
                   "main_body_prints_the_50_concepts": False,
                   "concept_words_named_individually": (
                       "7 distinct in characters 0-100000, a few more as examples in B.5; "
                       "never as a list"),
                   "license_statement_in_page_body": None,
                   "references_entry_for_the_credited_work": (
                       "J. Lindsey (2025), 'Emergent introspective awareness in large language "
                       "models', Transformer Circuits Thread, Anthropic, "
                       "https://transformer-circuits.pub/2025/introspection/index.html")}},
    "lindsey_2025_page": {
        "url": "https://transformer-circuits.pub/2025/introspection/index.html",
        "read_by": "round-2 fixer, WebFetch 2026-10-08, about 06:20 UTC",
        "note": ("round-2 read: page text 403,429 characters, read at offsets 0, 100000, 200000 "
                 "(100000-300000 is encoded image data), 300000 and 303429 (the whole page); "
                 "comparisons with the record by the fetch tool's model, not byte for byte; "
                 "the trial prompt's framing was compared later, in the round-3 record "
                 "lindsey_2025_page_trial_prompt_round3"),
        "result": {"title": "Emergent Introspective Awareness in Large Language Models",
                   "citation": "Lindsey 2025", "date": "2025-10-29",
                   "venue": "Transformer Circuits Thread (Anthropic)",
                   "license_or_terms_statement": None,
                   "citation_section": "a suggested citation and BibTeX (@article "
                                       "lindsey2025emergent); no license or reuse terms",
                   "prints_50_concept_list": ("yes, appendix 'Injected Thoughts: Additional "
                                              "Details' > 'Concept Vector Details'"),
                   "concept_list_vs_record": ("49 of the record's 50 in the same order; one "
                                              "position differs (the page has 'Information' "
                                              "where the record has 'Happiness')"),
                   "prints_100_baseline_words": True,
                   "baseline_list_vs_record": ("100 of 100 in the same order, including the "
                                               "record's duplicated 'Butterflies'"),
                   "extraction": ("Human/Assistant transcript 'Tell me about {word}', read at "
                                  "the final ':' token; mean over the 100 baseline words "
                                  "subtracted"),
                   "prints_trial_prompt": ("yes, 'Experimental Prompts and Protocol': a "
                                           "Human/Assistant transcript with an 'Ok.' setup "
                                           "reply and the trial question"),
                   # Round 4: this was the bare value False, true of the round-2 read but the
                   # opposite of the round-3 record when read alone; kept as a string that
                   # states both.
                   "trial_prompt_framing_compared_with_record": (
                       "not in this round-2 read; superseded: see "
                       "lindsey_2025_page_trial_prompt_round3 (compared there: framing 5 of 5 "
                       "sentences identical)")}},
    # --- round-3 fixer's reads, WebFetch 2026-10-08 ~09:20 UTC ------------------------
    # The round-2 fixer's read above left the Lindsey page's framing uncompared; the
    # round-3 checker compared it (no differences). These two reads compare both
    # published prompts with the record's MACAR_FRAMING / ACK / TRIAL_QUESTION, sentence
    # by sentence, by the fetch tool's model (not byte for byte).
    "lindsey_2025_page_trial_prompt_round3": {
        "url": "https://transformer-circuits.pub/2025/introspection/index.html",
        "read_by": "round-3 fixer, WebFetch 2026-10-08, about 09:20 UTC",
        "note":("read at offsets 300000 (two reads: the prompt and its second Human turn) and "
                 "400000 (the page's last 3,429 characters); fetch-tool comparisons"),
        "result": {"location": ("'Injected Thoughts: Additional Details' > 'Experimental "
                                "Prompts and Protocol'"),
                   "turn_labels": "Human: / Assistant:",
                   "framing_sentences_identical_to_record": [5, 5],
                   "framing_dashes_and_quotes": ("spaced double hyphen and straight quotes, as "
                                                 "in the record"),
                   "assistant_reply_equals_record_ACK": True,
                   "trial_line_equals_record_apart_from_number": True,
                   "second_human_turn_lead_in": "Ok, let's get started.",
                   "second_human_turn_has_text_before_trial_line": True,
                   "agrees_with_round3_checker_framing_read": True,
                   "license_or_terms_statement_300000_to_end": None}},
    "macar_paper_html_table4_round3": {
        "url": "https://arxiv.org/html/2603.21396v5",
        "note": "read at offset 0 (Table 4 lies in characters 0-100000); fetch-tool comparison",
        "result": {"framing_sentences_identical_to_record": [5, 5],
                   "model_turn_equals_record_ACK": True,
                   "second_user_turn_has_text_before_trial_line": False,
                   "second_user_turn_contains_lindsey_lead_in": False,
                   "trial_line_equals_record_apart_from_placeholder": True}},
    # --- round-4 fixer's read, WebFetch 2026-10-08 10:59 UTC ---------------------------
    # The round-4 checker read the site's home page for a site-wide license (none); the
    # round-4 fixer re-read it before recording it here.
    "transformer_circuits_home_round4": {
        "url": "https://transformer-circuits.pub/",
        "read_by": "round-4 fixer, WebFetch 2026-10-08, 10:59 UTC",
        "note": ("the whole page (about 20,000 characters with link markup, the fetch tool's "
                 "estimate; not truncated: it ends with the RSS link and the About section); "
                 "the fetch tool's model answered from the page text"),
        "result": {"license_copyright_or_terms_statement": None,
                   "link_mentioning_license_copyright_terms_legal_or_reuse": None,
                   "lists_lindsey_2025": True,
                   "agrees_with_round4_checker_read": True}},
    # The round-2 checker's own WebFetch read of the releases API (not re-read by the
    # round-2 fixer; recorded from its findings): the v0.3 asset's parts.
    "wezzard_releases_v03_parts_checker_read": {
        "url": "https://api.github.com/repos/WeZZard/jlens-qwen36/releases",
        "result": {"v0.3-qwen38-n1000_parts": [1887436800, 1415593598]}},
    "hf_models": {
        "allenai/Olmo-3-1125-32B": {
            "url": "https://huggingface.co/api/models/allenai/Olmo-3-1125-32B",
            "sha": "c2b61dae89a1ad10e4ad5653d0e46b590902607b", "license": "apache-2.0",
            "gated": False, "base_model": None},
        "allenai/Olmo-3.1-32B-Instruct-SFT": {
            "url": "https://huggingface.co/api/models/allenai/Olmo-3.1-32B-Instruct-SFT",
            "sha": "152782ecc41a86c5cbe3fb6afa68bd90934de48a", "license": "apache-2.0",
            "gated": False, "base_model": "allenai/Olmo-3-1125-32B"},
        "allenai/Olmo-3.1-32B-Instruct-DPO": {
            "url": "https://huggingface.co/api/models/allenai/Olmo-3.1-32B-Instruct-DPO",
            "sha": "fc84a4f699916fcf585aa54371f47897fa934d5c", "license": "apache-2.0",
            "gated": False, "base_model": "allenai/Olmo-3.1-32B-Instruct-SFT"},
        "allenai/Olmo-3.1-32B-Instruct": {
            "url": "https://huggingface.co/api/models/allenai/Olmo-3.1-32B-Instruct",
            "sha": "ac0587e4a7744a551c059d8cd17ba220bc940dae", "license": "apache-2.0",
            "gated": False, "base_model": "allenai/Olmo-3.1-32B-Instruct-DPO"},
        "mlx-community/Qwen3.6-27B-4bit": {
            "url": "https://huggingface.co/api/models/mlx-community/Qwen3.6-27B-4bit",
            "sha": "c000ac2c2057d94be3fa931000c31723aac53282", "license": "apache-2.0",
            "gated": False, "base_model": "Qwen/Qwen3.6-27B",
            "license_link": "https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/LICENSE"},
        "Qwen/Qwen3.6-27B": {
            "url": "https://huggingface.co/api/models/Qwen/Qwen3.6-27B",
            "sha": "6a9e13bd6fc8f0983b9b99948120bc37f49c13e9", "license": "apache-2.0",
            "gated": False, "base_model": None,
            "license_link": "https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/LICENSE"},
    },
}

# ---------------------------------------------------------------------------
# Redaction
# ---------------------------------------------------------------------------
_REDACT_RX = [
    ("ipv4", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("token", re.compile(r"\b(?:sk-[A-Za-z0-9_-]{8,}|rp_[A-Za-z0-9]{8,}|hf_[A-Za-z0-9]{16,}"
                         r"|ghp_[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16})")),
    ("ssh-key", re.compile(r"ssh-(?:rsa|ed25519|dss)\s+[A-Za-z0-9+/=]{16,}")),
    ("pem", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]
REDACTIONS: list[dict] = []      # pattern-based (redact())
REDACTED_IDS: list[dict] = []    # ids printed in redacted form by rule (section 2f)


def redform(v: str) -> str:
    return f"{v[:4]}...{len(v)}:{hashlib.sha256(v.encode()).hexdigest()[:8]}"


def redact(s: str, where: str = "") -> str:
    for cat, rx in _REDACT_RX:
        def sub(m, cat=cat):
            REDACTIONS.append({"where": where, "category": cat, "redacted": redform(m.group(0))})
            return f"[REDACTED {cat} {redform(m.group(0))}]"
        s = rx.sub(sub, s)
    return s


# ---------------------------------------------------------------------------
# Read-only git helpers (always -C REPO; never inside the clone)
# ---------------------------------------------------------------------------
def git(*args: str) -> bytes:
    assert os.path.realpath(REPO) != os.path.realpath(CLONE)
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, check=True).stdout


def gtext(*args: str) -> str:
    return git(*args).decode("utf-8", "replace")


def ls_tree(rev: str) -> list[dict]:
    rows = []
    for line in gtext("ls-tree", "-r", "-l", "-z", rev).split("\0"):
        if not line:
            continue
        meta, path = line.split("\t", 1)
        mode, typ, sha, size = meta.split()
        rows.append({"mode": mode, "type": typ, "blob": sha,
                     "size": int(size) if size != "-" else -1, "path": path})
    return rows


def cat_blobs(shas: list[str]) -> dict[str, bytes]:
    """Read many blobs through one `git cat-file --batch` process."""
    out: dict[str, bytes] = {}
    if not shas:
        return out
    p = subprocess.Popen(["git", "-C", REPO, "cat-file", "--batch"],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    data, _ = p.communicate(("\n".join(shas) + "\n").encode())
    i = 0
    for sha in shas:
        nl = data.index(b"\n", i)
        hdr = data[i:nl].decode().split()
        size = int(hdr[2])
        out[sha] = data[nl + 1: nl + 1 + size]
        i = nl + 1 + size + 1
    return out


def git_blob_sha1(b: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------------------
# The clone's git data read as FILES (no git process inside jlens-qwen36/)
# ---------------------------------------------------------------------------
_OBJ_TYPES = {1: "commit", 2: "tree", 3: "blob", 4: "tag"}


class CloneObjects:
    """Read-only reader of a .git object store: loose objects (zlib) and v2
    pack/idx pairs, OFS_DELTA and REF_DELTA resolved. Every object returned
    is re-hashed and must equal the sha asked for."""

    def __init__(self, gitdir: str):
        self.g = gitdir
        self.packs = []
        pd = os.path.join(gitdir, "objects", "pack")
        for fn in (sorted(os.listdir(pd)) if os.path.isdir(pd) else []):
            if not fn.endswith(".idx"):
                continue
            idx = open(os.path.join(pd, fn), "rb").read()
            assert idx[:4] == b"\xfftOc" and struct.unpack(">I", idx[4:8])[0] == 2, fn
            n = struct.unpack(">I", idx[8 + 255 * 4: 8 + 256 * 4])[0]
            o = 8 + 256 * 4
            shas = [idx[o + 20 * i: o + 20 * i + 20].hex() for i in range(n)]
            o2 = o + 24 * n
            offs = struct.unpack(">%dI" % n, idx[o2: o2 + 4 * n])
            o3 = o2 + 4 * n
            table = {}
            for s, off in zip(shas, offs):
                if off & 0x80000000:
                    k = off & 0x7FFFFFFF
                    off = struct.unpack(">Q", idx[o3 + 8 * k: o3 + 8 * k + 8])[0]
                table[s] = off
            pack = open(os.path.join(pd, fn[:-4] + ".pack"), "rb").read()
            assert pack[:4] == b"PACK", fn
            self.packs.append((table, pack))

    @staticmethod
    def _inflate(buf: bytes, pos: int) -> bytes:
        d = zlib.decompressobj()
        out = []
        p = pos
        while not d.eof:
            out.append(d.decompress(buf[p:p + 65536]))
            p += 65536
        return b"".join(out)

    @staticmethod
    def _apply_delta(base: bytes, delta: bytes) -> bytes:
        p = 0

        def vint():
            nonlocal p
            v = sh = 0
            while True:
                c = delta[p]
                p += 1
                v |= (c & 0x7F) << sh
                sh += 7
                if not c & 0x80:
                    return v
        bsz, tsz = vint(), vint()
        assert bsz == len(base)
        out = bytearray()
        while p < len(delta):
            c = delta[p]
            p += 1
            if c & 0x80:
                o = s = 0
                for i in range(4):
                    if c & (1 << i):
                        o |= delta[p] << (8 * i)
                        p += 1
                for i in range(3):
                    if c & (1 << (4 + i)):
                        s |= delta[p] << (8 * i)
                        p += 1
                out += base[o:o + (s or 0x10000)]
            elif c:
                out += delta[p:p + c]
                p += c
            else:
                raise ValueError("delta opcode 0")
        assert len(out) == tsz
        return bytes(out)

    def _read_packed(self, pk, off: int):
        table, pack = pk
        c = pack[off]
        p = off + 1
        typ = (c >> 4) & 7
        while c & 0x80:
            c = pack[p]
            p += 1
        if typ == 6:
            c = pack[p]
            p += 1
            boff = c & 0x7F
            while c & 0x80:
                c = pack[p]
                p += 1
                boff = ((boff + 1) << 7) | (c & 0x7F)
            bt, base = self._read_packed(pk, off - boff)
            return bt, self._apply_delta(base, self._inflate(pack, p))
        if typ == 7:
            bsha = pack[p:p + 20].hex()
            bt, base = self.get(bsha)
            return bt, self._apply_delta(base, self._inflate(pack, p + 20))
        return _OBJ_TYPES[typ], self._inflate(pack, p)

    def get(self, sha: str):
        lp = os.path.join(self.g, "objects", sha[:2], sha[2:])
        if os.path.isfile(lp):
            hdr, body = zlib.decompress(open(lp, "rb").read()).split(b"\0", 1)
            t = hdr.decode().split()[0]
        else:
            for pk in self.packs:
                if sha in pk[0]:
                    t, body = self._read_packed(pk, pk[0][sha])
                    break
            else:
                raise KeyError(sha)
        chk = hashlib.sha1(f"{t} {len(body)}".encode() + b"\0" + body).hexdigest()
        assert chk == sha, (sha, chk)
        return t, body

    def tree_blobs(self, tsha: str, prefix: str = "") -> dict:
        t, body = self.get(tsha)
        assert t == "tree"
        p, out = 0, {}
        while p < len(body):
            sp = body.index(b" ", p)
            nul = body.index(b"\0", sp)
            mode, name = body[p:sp].decode(), body[sp + 1:nul].decode()
            sha = body[nul + 1:nul + 21].hex()
            p = nul + 21
            if mode == "40000":
                out.update(self.tree_blobs(sha, prefix + name + "/"))
            else:
                out[prefix + name] = (mode, sha)
        return out


def read_git_index(path: str) -> dict:
    """Entries of a v2/v3 git index file: path -> {mode, sha, size}."""
    b = open(path, "rb").read()
    assert b[:4] == b"DIRC"
    ver, n = struct.unpack(">II", b[4:12])
    if ver not in (2, 3):
        raise ValueError(f"index version {ver} not parsed here")
    p, ents = 12, {}
    for _ in range(n):
        st = p
        f = struct.unpack(">10I", b[p:p + 40])
        p += 40
        sha = b[p:p + 20].hex()
        p += 20
        flags = struct.unpack(">H", b[p:p + 2])[0]
        p += 2
        if ver == 3 and flags & 0x4000:
            p += 2
        nul = b.index(b"\0", p)
        name = b[p:nul].decode()
        p = st + ((nul - st + 8) // 8) * 8
        ents[name] = {"mode": oct(f[6]), "sha": sha, "size": f[9]}
    return ents


def npz_layout(fp: str) -> dict:
    """Zip directory + each member's .npy header (no array data read), plus the
    values of 0-d int64 members (8 bytes each)."""
    z = zipfile.ZipFile(fp)
    kinds: dict[str, int] = defaultdict(int)
    scalars: dict[str, int] = {}
    n_comp = 0
    total = 0
    for inf in z.infolist():
        n_comp += inf.compress_type != zipfile.ZIP_STORED
        total += inf.file_size
        with z.open(inf) as f:
            h = f.read(10)
            assert h[:6] == b"\x93NUMPY", inf.filename
            if h[6] == 1:
                hl = struct.unpack("<H", h[8:10])[0]
            else:
                hl = struct.unpack("<I", h[8:10] + f.read(2))[0]
            hdr = ast.literal_eval(f.read(hl).decode("latin1"))
            kinds[f"{hdr['descr']} {tuple(hdr['shape'])}"] += 1
            if hdr["shape"] == () and hdr["descr"] == "<i8":
                scalars[inf.filename] = struct.unpack("<q", f.read(8))[0]
    return {"n_members": len(z.infolist()), "n_compressed": n_comp,
            "member_bytes_total": total, "kinds": dict(kinds), "int_scalars": scalars}


def find_line(text: str, needle: str) -> list[int]:
    return [i for i, l in enumerate(text.splitlines(), 1) if needle in l]


# ---------------------------------------------------------------------------
# AST fingerprints
# ---------------------------------------------------------------------------
GENERIC_NAMES = {"main", "parse_args", "__init__", "__call__", "__repr__", "__str__",
                 "__post_init__", "__enter__", "__exit__", "__len__", "__getitem__",
                 "__iter__", "forward", "run", "load", "save", "setup", "build_parser",
                 "_parse_args", "cli", "encode", "decode", "tokenize", "generate",
                 "reset", "close", "step", "to_dict", "from_dict", "as_dict", "log",
                 "chk", "check", "selftest", "_selftest", "now", "utc", "fmt"}


def _strip_doc(node):
    body = getattr(node, "body", None)
    if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None),
                                                             ast.Constant) \
            and isinstance(body[0].value.value, str):
        node.body = body[1:] or [ast.Pass()]
    return node


SHINGLE_K = 5
NEAR_MIN_STMTS = 5
_SKIP_TOK = {tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT,
             tokenize.COMMENT, tokenize.ENDMARKER}


def _shingles(src: str) -> frozenset:
    try:
        toks = [t.string for t in tokenize.generate_tokens(io.StringIO(src).readline)
                if t.type not in _SKIP_TOK]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return frozenset()
    return frozenset(tuple(toks[i:i + SHINGLE_K]) for i in range(len(toks) - SHINGLE_K + 1))


def defs_of(src: str) -> list[dict] | None:
    """Every def/class at any depth: name, line, statement count, an exact
    fingerprint (ast.dump, docstring removed, positions dropped) and, for
    functions of >= NEAR_MIN_STMTS statements, token 5-gram shingles of the
    docstring-stripped unparsed source (comments and layout do not count)."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    res = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            lineno = node.lineno
            n_stmts = sum(1 for n in ast.walk(node) if isinstance(n, ast.stmt)) - 1
            cp = ast.parse(ast.unparse(node)).body[0]
            _strip_doc(cp)
            fp = sha256(ast.dump(cp, annotate_fields=True, include_attributes=False).encode())
            sh = (_shingles(ast.unparse(cp))
                  if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                  and n_stmts >= NEAR_MIN_STMTS else frozenset())
            res.append({"name": node.name, "line": lineno, "n_stmts": n_stmts, "fp": fp,
                        "sh": sh})
    return res


def long_lines(src: str, min_len: int = 60) -> dict[str, int]:
    out = {}
    for i, raw in enumerate(src.splitlines(), 1):
        s = " ".join(raw.split())
        if len(s) < min_len or s.startswith(("import ", "from ", "#!")):
            continue
        if not re.search(r"[A-Za-z]{3}", s):
            continue
        out.setdefault(s, i)
    return out


def ipynb_code(b: bytes) -> str:
    try:
        nb = json.loads(b)
    except Exception:
        return ""
    parts = []
    for c in nb.get("cells", []):
        if c.get("cell_type") == "code":
            src = c.get("source", "")
            src = "".join(src) if isinstance(src, list) else src
            parts.append("\n".join(l for l in src.splitlines()
                                   if not l.lstrip().startswith(("%", "!"))))
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
def main() -> int:
    global OUT_MD, OUT_JSON
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_MD,
                    help="markdown output (default %(default)s)")
    ap.add_argument("--json-out", default=DEFAULT_JSON,
                    help="JSON output (default %(default)s)")
    ap.add_argument("--out-dir", default=None,
                    help="convenience: write each output not given by --out / --json-out "
                         "into this directory under its default basename")
    a = ap.parse_args()
    OUT_MD = os.path.abspath(a.out)
    OUT_JSON = os.path.abspath(a.json_out)
    if a.out_dir:
        if a.out == DEFAULT_MD:
            OUT_MD = os.path.abspath(os.path.join(a.out_dir, os.path.basename(DEFAULT_MD)))
        if a.json_out == DEFAULT_JSON:
            OUT_JSON = os.path.abspath(os.path.join(a.out_dir, os.path.basename(DEFAULT_JSON)))
    if OUT_MD == OUT_JSON:
        ap.error("--out and --json-out name the same file")
    # release (the PI's answer of 2026-10-12): the release run writes NEW dated raws; a path git already tracks
    # (e.g. this script's committed 2026-10-08 raws, the defaults) is refused, so a committed raw is never overwritten
    for o_ in (OUT_MD, OUT_JSON):
        if os.path.realpath(o_).startswith(os.path.realpath(REPO) + os.sep):
            rel_ = os.path.relpath(os.path.realpath(o_), os.path.realpath(REPO))
            if subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch", "--", rel_],
                              capture_output=True).returncode == 0:
                ap.error(f"{rel_} is tracked by git; the release run writes new dated raws (pass --out and "
                         f"--json-out)")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    head = gtext("rev-parse", "HEAD").strip()
    R: dict = {"part": "N12-licenses", "code_stamp_utc": stamp, "commit_read": head,
               "block": BLOCK, "interpreter": sys.executable,
               "python": sys.version.split()[0]}
    L: list[str] = []
    P = L.append

    blk = open(os.path.join(REPO, BLOCK), "rb").read()
    blk_ok = sha256(blk) == BLOCK_SHA
    R["block_sha256"] = sha256(blk)
    R["block_sha_match"] = blk_ok
    blk_lines = blk.decode().splitlines()

    tree = ls_tree(head)
    by_path = {r["path"]: r for r in tree}
    R["n_tracked_at_commit"] = len(tree)

    # text blobs for scanning (extension filter, < 60 MB)
    TEXT_EXT = (".py", ".sh", ".md", ".json", ".jsonl", ".txt", ".ipynb", ".toml",
                ".cfg", ".yaml", ".yml", ".csv", ".tsv", ".html", ".js", ".svg", ".log")

    def is_text_path(path: str) -> bool:
        return path.endswith(TEXT_EXT) or os.path.basename(path) in (".gitignore",
                                                                     ".gitattributes")
    text_rows = [r for r in tree if r["type"] == "blob" and r["size"] < 60_000_000
                 and is_text_path(r["path"])]
    blobs = cat_blobs([r["blob"] for r in text_rows])
    text = {r["path"]: blobs[r["blob"]].decode("utf-8", "replace") for r in text_rows}
    unscanned = sorted(r["path"] for r in tree if r["path"] not in text)
    R["n_text_files_scanned"] = len(text)
    R["unscanned_at_commit"] = unscanned
    n_uns_npz = sum(1 for p in unscanned if p.endswith(".npz"))

    P("# AUDIT-note-release v1.2 -- N12(iv) third-party materials and licenses (part N12-licenses)")
    P("")
    P("- Part raw for N12(iv). The block's N12 output, `results/raw/<stamp>_note-N12-scrub.md` "
      "(block line 84), cites it.")
    P(f"- Code stamp: {stamp} (script clock, UTC)")
    blk_commit = gtext("log", "--diff-filter=A", "--format=%H", "--", BLOCK).strip().splitlines()
    blk_commit = blk_commit[-1] if blk_commit else None
    since = (gtext("rev-list", "--reverse", f"{blk_commit}..{head}").split()
             if blk_commit else [])
    R["block_commit"] = blk_commit
    # Each later commit is described by data, not by who is assumed to have made it: git
    # records no session, so the test is whether the commit touches this audit's own
    # files (the audit's scripts, its raws, the block, the README-for-readers).
    RX_AUDIT_PATH = re.compile(r"^(scripts/audit_note_|results/raw/\d{4}-\d{2}-\d{2}_note-|"
                               r"AUDIT-note-|README-NOTE\.md$)")
    since_info = []
    for c in since:
        cp = [x for x in gtext("diff", "--name-only", f"{c}^", c).splitlines() if x]
        since_info.append({"commit": c, "n_paths": len(cp),
                           "audit_paths": [x for x in cp if RX_AUDIT_PATH.match(x)]})
    R["commits_after_block_commit"] = since_info
    n_since_audit = sum(1 for s in since_info if s["audit_paths"])
    # Locators of the form path@<sha>:<line> are pinned to the block's commit (bbc9ffe),
    # the audit's common pin, and found by content in the file AT that commit, so they
    # do not drift with RESULTS.md's newest-first entries while HEAD moves.
    LOC = blk_commit or head
    _loc_cache: dict = {}

    def loc_src(f: str) -> str:
        if f not in _loc_cache:
            try:
                _loc_cache[f] = gtext("show", f"{LOC}:{f}")
            except subprocess.CalledProcessError:
                _loc_cache[f] = ""
        return _loc_cache[f]
    R["locator_commit"] = LOC
    P(f"- Commit read: {head} (HEAD resolved once at start). Tracked content is read at this "
      f"commit; first-added dates, history lists and the history-wide copy check come from "
      f"every commit reachable from the local refs listed in section 5 (`git log --all`, "
      f"`git rev-list --all`); the block, the `jlens-qwen36/` clone and the HF cache are read "
      f"from disk (the block's sha is checked on the next line).")
    P(f"- Locators: every `path@<sha>:<line>` locator into the record is pinned to "
      f"`{LOC[:7]}` (the block's commit, the audit's common pin) and found by content in the "
      f"file at that commit; bare `file:line` entries produced by the scans (sections 1-3) are "
      f"at the commit read, except section 2f's first-locator column, which names its commit "
      f"(`file@{LOC[:7]}:N`, found by content at that commit, or `file@{head[:7]}:N` where the "
      f"file at `{LOC[:7]}` lacks the id; section 2f). Locators of the form `jlens-qwen36/...@{JLENS_CLONE_COMMIT[:7]}` "
      f"are into the jlens-qwen36 upstream commit (read from the clone's object store).")
    P(f"- Scope in time: the block was committed at `{(blk_commit or '?')[:7]}`; the commit read "
      f"is {len(since)} commit(s) after it"
      + (" (" + "; ".join(f"`{s['commit'][:7]}`: {s['n_paths']} paths changed, "
                          f"{len(s['audit_paths'])} of them this audit's files"
                          for s in since_info) + ")" if since else "")
      + f"; commits after it that touch this audit's files (`scripts/audit_note_*`, "
      f"`results/raw/<date>_note-*`, `AUDIT-note-*`, `README-NOTE.md`): {n_since_audit}. "
      "Every count below is bound to the commit read. HEAD moves while the audit runs, and "
      "the release publishes whatever the refs hold when visibility changes, so this script is "
      "to be re-run at the final pre-flip commit (the commit the flip publishes: in the release "
      "sequence, the post-tag commit that adds the release raws, not the tag commit) and its "
      "counts re-checked; the N12 scrub raw states that bound.")
    P(f"- Block: `{BLOCK}`, sha256 `{sha256(blk)}`, {len(blk_lines)} lines "
      f"(routed as 8cd8a9ac...3841, 141 lines: {'MATCH' if blk_ok and len(blk_lines) == 141 else 'MISMATCH'})")
    P(f"- Item: N12(iv), block lines 80 (procedure) and 85 (pass: \"(iv) licenses recorded\"); "
      f"rules at block section 0 (lines 7-14)")
    P("- Script: `scripts/audit_note_N12_licenses.py` (read-only; stdlib only; no network)")
    P(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]})")
    P(f"- Tracked files at the commit: {len(tree)}; text files scanned: {len(text)} "
      f"(extensions {', '.join(TEXT_EXT)}, plus .gitignore/.gitattributes; each < 60 MB). "
      f"Not scanned: {len(unscanned)} ({n_uns_npz} `.npz` arrays; "
      + ", ".join(f"`{p}`" for p in unscanned if not p.endswith(".npz")) + ").")
    P("- External facts: read by Code with WebFetch on 2026-10-08 (UTC, Code's clock: the "
      "builder's reads, the round-1 fixer's at 04:08 UTC, the round-2 fixer's at about 06:20 "
      "UTC for the paper and the Lindsey page, the round-3 fixer's at about 09:20 UTC for the "
      "Lindsey page's trial prompt and the paper's Table 4, the round-4 fixer's at 10:59 UTC for "
      "the transformer-circuits.pub home page); carried in the script as recorded constants "
      "with their URLs and marked **[recorded WebFetch read]** below. Where a read compares a "
      "page's text with the record, the comparison was made by the fetch tool's model, not "
      "byte for byte. The script did not fetch them and does not recompute them. Nothing was "
      "downloaded or cloned; no git command ran inside `jlens-qwen36/` (its git data are read "
      "as files).")
    P("- Scope: this part covers N12(iv)'s licenses and third-party materials. N12(iv)'s "
      "`.npz`-allowlist and model-weights-in-history checks belong to the history part; section 3 "
      "here reports only a HEAD-level weights count as context.")
    P("")

    # ---- history: every commit reachable from any local ref, full trees -------------
    commits = gtext("rev-list", "--all").split()
    HI = {"n_commits": len(commits), "n_entries": 0, "n_non_blob_entries": 0}
    hist_blob_paths: dict[str, set] = defaultdict(set)
    hist_blob_first: dict[str, tuple] = {}
    hist_blob_size: dict[str, int] = {}
    all_hist_paths: set = set()
    for c in commits:
        for r in ls_tree(c):
            HI["n_entries"] += 1
            all_hist_paths.add(r["path"])
            if r["type"] != "blob":
                HI["n_non_blob_entries"] += 1
                continue
            hist_blob_paths[r["blob"]].add(r["path"])
            hist_blob_first.setdefault(r["blob"], (c, r["path"]))
            hist_blob_size[r["blob"]] = r["size"]
    hist_paths = sorted(all_hist_paths)
    HI["n_distinct_blobs"] = len(hist_blob_paths)
    HI["n_distinct_paths"] = len(hist_paths)
    hist_text_shas = [b for b, ps in hist_blob_paths.items()
                      if hist_blob_size[b] < 60_000_000 and any(is_text_path(p) for p in ps)]
    hb = cat_blobs(hist_text_shas)
    hist_text = {b: hb[b].decode("utf-8", "replace") for b in hist_text_shas}
    del hb
    HI["n_distinct_text_blobs_scanned"] = len(hist_text)
    R["history"] = HI

    def hloc(b: str) -> str:
        c, p = hist_blob_first[b]
        return f"{c[:7]}:{p}"

    # =====================================================================
    # 1. Macar materials
    # =====================================================================
    P("## 1. Macar et al. materials: `data/configs/b2_concepts.json`, `data/configs/b2_framing.json`")
    P("")
    S1: dict = {}
    for p in ("data/configs/b2_concepts.json", "data/configs/b2_framing.json"):
        r = by_path[p]
        S1[p] = {"blob": r["blob"], "sha256": sha256(text[p].encode()),
                 "first_added": gtext("log", "--all", "--diff-filter=A", "--format=%h %ad",
                                      "--date=short", "--", p).strip().splitlines()[-1]}
    bc = json.loads(text["data/configs/b2_concepts.json"])
    bf = json.loads(text["data/configs/b2_framing.json"])
    prov = bc["provenance"]

    def find_licen(o, path=""):
        hits = []
        if isinstance(o, dict):
            for k, v in o.items():
                if re.search(r"licen[cs]", k, re.I):
                    hits.append(f"key {path}/{k}")
                hits += find_licen(v, f"{path}/{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                hits += find_licen(v, f"{path}[{i}]")
        elif isinstance(o, str) and re.search(r"licen[cs]", o, re.I):
            hits.append(f"string {path}")
        return hits

    lic_c, lic_f = find_licen(bc), find_licen(bf)
    S1["provenance"] = prov
    S1["n_canonical"] = [bc.get("n_canonical"), len(bc.get("canonical_concepts", []))]
    S1["n_baseline"] = [bc.get("n_baseline"), len(bc.get("baseline_words", []))]
    S1["extraction_template"] = bc["extraction_method"]["template"]
    S1["framing_provenance"] = bf["fidelity"].get("provenance")
    fr = bf["fidelity"]["framing"]
    S1["framing_sha256"] = sha256(fr.encode())
    S1["framing_len"] = len(fr)
    S1["trial_question_sha256"] = sha256(bf["shared"]["trial_question"].encode())
    S1["license_fields"] = {"b2_concepts.json": lic_c, "b2_framing.json": lic_f}
    R["macar_materials"] = S1

    P("Printed from the committed JSON at the commit read:")
    P("")
    P("| field | value |")
    P("|---|---|")
    for p in S1:
        if p.startswith("data/"):
            P(f"| `{p}` blob / sha256 / first added | `{S1[p]['blob'][:12]}` / `{S1[p]['sha256'][:16]}...` / {S1[p]['first_added']} |")
    for k in ("repo", "commit_sha", "default_branch", "pushed_at", "recovered_utc",
              "concepts_source", "baseline_source", "method_source"):
        P(f"| provenance.{k} | {redact(str(prov.get(k)), 'b2_concepts.provenance')} |")
    P(f"| n_canonical (declared / list length) | {S1['n_canonical'][0]} / {S1['n_canonical'][1]} |")
    P(f"| n_baseline (declared / list length) | {S1['n_baseline'][0]} / {S1['n_baseline'][1]} |")
    P(f"| extraction_method.template | `{S1['extraction_template']}` |")
    P(f"| b2_framing fidelity.provenance | {S1['framing_provenance']} |")
    P(f"| fidelity framing (their text, verbatim) | {S1['framing_len']} chars, sha256 `{S1['framing_sha256'][:16]}...` |")
    P(f"| license field in b2_concepts.json | {lic_c if lic_c else 'none (no key or string matches licen[cs])'} |")
    P(f"| license field in b2_framing.json | {lic_f if lic_f else 'none (no key or string matches licen[cs])'} |")
    P("")

    # where Macar's verbatim text sits in the tracked record
    FR_MARK = "I am capable of injecting these patterns"
    TQ_MARK = "Do you detect an injected thought?"
    fr_files = sorted(p for p, t in text.items() if FR_MARK in t)
    tq_files = sorted(p for p, t in text.items() if TQ_MARK in t)

    def group(files):
        g = defaultdict(int)
        for f in files:
            parts = f.split("/")
            g["/".join(parts[:2]) if len(parts) >= 3 else (parts[0] if len(parts) == 2
                                                         else "(root)")] += 1
        return dict(sorted(g.items()))

    def norm_text(t: str) -> str:
        """Undo line wrapping and escaping so a phrase split across lines still matches:
        literal \\n/\\t/\\r escapes and \\" become plain characters, Python implicit string
        concatenation across a line break ("...you "\\n    "detect...") is joined, and
        whitespace runs collapse to one space."""
        t = re.sub(r"\\[nrt]", " ", t).replace('\\"', '"')
        t = re.sub(r"[\"']\s*\n\s*[\"']", "", t)
        return re.sub(r"\s+", " ", t)

    fr_norm = sorted(p for p, t in text.items() if FR_MARK not in t and FR_MARK in norm_text(t))
    tq_norm = sorted(p for p, t in text.items() if TQ_MARK not in t and TQ_MARK in norm_text(t))
    tq_norm_lines = {}
    for p in tq_norm:
        ls = text[p].splitlines()
        tq_norm_lines[p] = [i for i in range(1, len(ls))
                            if TQ_MARK not in ls[i - 1] and TQ_MARK not in ls[i]
                            and TQ_MARK in norm_text(ls[i - 1] + "\n" + ls[i])]
    S1["files_with_framing_marker"] = fr_files
    S1["files_with_trial_question_marker"] = tq_files
    S1["files_with_framing_marker_wrapped_only"] = fr_norm
    S1["files_with_trial_question_marker_wrapped_only"] = tq_norm
    S1["trial_question_wrapped_line_pairs"] = {p: [f"{i}-{i + 1}" for i in v]
                                               for p, v in tq_norm_lines.items()}
    # the same wrapped pairs located in the file at the locator commit (LOC)
    tq_norm_loc = {}
    for p in tq_norm:
        ls = loc_src(p).splitlines()
        tq_norm_loc[p] = [f"{i}-{i + 1}" for i in range(1, len(ls))
                          if TQ_MARK not in ls[i - 1] and TQ_MARK not in ls[i]
                          and TQ_MARK in norm_text(ls[i - 1] + "\n" + ls[i])]
    S1["trial_question_wrapped_line_pairs_at_locator_commit"] = {"commit": LOC, "pairs": tq_norm_loc}
    # this audit's own working files (untracked at the commit read) that carry the markers
    untracked = gtext("ls-files", "--others", "--exclude-standard", "-z").split("\0")
    own = sorted(p for p in untracked if RX_AUDIT_FILE.match(p))
    own_fr, own_tq = [], []
    for p in own:
        try:
            t = open(os.path.join(REPO, p), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        if FR_MARK in norm_text(t):
            own_fr.append(p)
        if TQ_MARK in norm_text(t):
            own_tq.append(p)
    S1["untracked_audit_files_with_markers"] = {"framing": own_fr, "trial_question": own_tq}
    P(f"Tracked text files carrying Macar's framing verbatim (marker \"{FR_MARK}\"): "
      f"**{len(fr_files)}** on a single line: " + ", ".join(f"`{f}`" for f in fr_files) + "; "
      f"found only after undoing line wraps and escapes: {len(fr_norm)}"
      + (" (" + ", ".join(f"`{f}`" for f in fr_norm) + ")" if fr_norm else "") + ". "
      f"Carrying their trial question (marker \"{TQ_MARK}\"): **{len(tq_files)}** on a single "
      f"line (a lower bound), by directory {group(tq_files)}: "
      + ", ".join(f"`{f}`" for f in tq_files) + "; plus **" + str(len(tq_norm)) + "** found only "
      "after undoing line wraps and escapes ("
      + ", ".join(f"`{f}` lines {', '.join(S1['trial_question_wrapped_line_pairs'][f]) or '(escaped)'}"
                  + (f" at the commit read (`{f}@{LOC[:7]}:{', '.join(tq_norm_loc[f])}`)"
                     if tq_norm_loc.get(f) and tq_norm_loc[f] != S1['trial_question_wrapped_line_pairs'][f]
                     else "")
                  for f in tq_norm)
      + f"), so **{len(tq_files) + len(tq_norm)}** in all. These counts are over tracked files at "
      f"the commit read. They exclude this audit's own files untracked at the commit read "
      f"({len(own)}, read from disk), of which {len(own_tq)} carry the trial question and "
      f"{len(own_fr)} the framing marker at this run; "
      + "; ".join(f"`{x_}` is " + ((f"tracked at the commit read (counted above: "
                                    f"{x_ in tq_files or x_ in tq_norm})") if x_ in text else
                                   (f"untracked (carries the trial question: {x_ in own_tq})" if x_ in own
                                    else "absent"))
                  for x_ in ('scripts/audit_note_N12_licenses.py', 'results/raw/2026-10-08_note-N12-licenses.md'))
      + "; and this run's own two outputs, not on disk while it runs, of which @@L3S1OWN@@ "
      f"(counted on the text written). Committing any of these raises the counts by as many.")
    P("")
    # tracked code that builds Macar prompts at run time from detection.py's constants
    MACAR_NAMES = {"MACAR_FRAMING", "TRIAL_QUESTION", "ACK", "COMPLETION_TEMPLATE", "build_prompt"}
    builders: dict[str, list[str]] = {}
    for p, s in sorted(text.items()):
        if not p.endswith(".py") or p == "valence_core/detection.py":
            continue
        try:
            tr_ = ast.parse(s)
        except SyntaxError:
            continue
        got = set()
        for n in ast.walk(tr_):
            if isinstance(n, ast.ImportFrom) and n.module and (
                    n.module == "valence_core.detection" or (n.level > 0 and n.module == "detection")):
                got |= {a.name for a in n.names} & MACAR_NAMES
            elif isinstance(n, ast.Attribute) and n.attr in ("MACAR_FRAMING", "TRIAL_QUESTION"):
                got.add(n.attr)
        if got:
            builders[p] = sorted(got)
    S1["runtime_prompt_builders"] = builders
    P(f"Tracked code that builds Macar prompts at run time from `valence_core/detection.py`'s "
      f"constants (AST: imports of {sorted(MACAR_NAMES)} from it, or attribute use of "
      f"`MACAR_FRAMING`/`TRIAL_QUESTION`): **{len(builders)}** files: "
      + "; ".join(f"`{p}` {v}" for p, v in builders.items()) + ". (Which script wrote each "
      "`data/olmo/` carrier above is not traced here.)")
    P("")
    # where the two word lists, and the approved eight, sit in the tracked record (round 3)
    A8 = list(bc.get("selection_for_B2", {}).get("approved_eight", []))
    C50 = set(bc.get("canonical_concepts", []))
    B100 = set(bc.get("baseline_words", []))

    def quoted(t: str, words) -> list[str]:
        return sorted(w for w in words if f'"{w}"' in t)
    WL: dict = {"approved_eight": A8, "approved_eight_subset_of_50": set(A8) <= C50,
                "files_with_all_eight": [], "files_with_1_to_7_of_50": {},
                "files_with_ge20_of_50_or_100": [], "files_with_any_baseline_word": [],
                "npz_members": {}}
    for p, t in sorted(text.items()):
        q8, q50, q100 = quoted(t, set(A8)), quoted(t, C50), quoted(t, B100)
        if A8 and len(q8) == len(set(A8)):
            WL["files_with_all_eight"].append(p)
        elif q50:
            WL["files_with_1_to_7_of_50"][p] = len(q50)
        if len(q50) >= 20 or len(q100) >= 20:
            WL["files_with_ge20_of_50_or_100"].append(p)
        if q100:
            WL["files_with_any_baseline_word"].append(p)
    npz_rows = [r for r in tree if r["path"].endswith(".npz") and r["type"] == "blob"]
    npz_bytes = cat_blobs([r["blob"] for r in npz_rows])
    for r in npz_rows:
        try:
            names = [n[:-4] if n.endswith(".npy") else n
                     for n in zipfile.ZipFile(io.BytesIO(npz_bytes[r["blob"]])).namelist()]
        except zipfile.BadZipFile:
            names = ["<not a zip>"]
        hit8 = [n for n in names if n in set(A8)]
        if hit8 or any(n in C50 or n in B100 for n in names):
            WL["npz_members"][r["path"]] = {"n_members": len(names), "approved_eight": len(hit8),
                                            "of_50": sum(1 for n in names if n in C50),
                                            "of_100_baseline": sum(1 for n in names if n in B100)}
    del npz_bytes
    WL["n_npz_read"] = len(npz_rows)
    S1["word_list_locations"] = WL
    wl_other8 = [p for p in WL["files_with_all_eight"] if p != "data/configs/b2_concepts.json"]
    wl_other8_dirs = group(wl_other8)
    wl_npz8 = [p for p, v in WL["npz_members"].items() if v["approved_eight"] == len(set(A8))]
    wl_base_other = [p for p in WL["files_with_any_baseline_word"]
                     if p != "data/configs/b2_concepts.json"]
    P(f"Where the two word lists sit (quoted JSON strings in the tracked text files at the commit "
      f"read; `.npz` member names from the zip directories of all {len(npz_rows)} tracked `.npz` "
      f"files). The full lists: files carrying >= 20 of the 50 concepts or of the 100 baseline "
      f"words: **{len(WL['files_with_ge20_of_50_or_100'])}** ("
      + ", ".join(f"`{p}`" for p in WL["files_with_ge20_of_50_or_100"]) + "). The baseline words "
      f"in any other file: {len(wl_base_other)}. The approved eight "
      f"(`selection_for_B2.approved_eight`, a subset of the 50: "
      f"{WL['approved_eight_subset_of_50']}) appear, all eight as quoted strings, in "
      f"**{len(wl_other8)}** other tracked files (by directory {wl_other8_dirs}: "
      + ", ".join(f"`{p}`" for p in wl_other8) + "), and as array member names in "
      f"**{len(wl_npz8)}** tracked `.npz` files ("
      + ", ".join(f"`{p}`" for p in wl_npz8) + "); 1-7 of the 50 appear in "
      f"{len(WL['files_with_1_to_7_of_50'])} files ("
      + ", ".join(f"`{p}` {n}" for p, n in WL["files_with_1_to_7_of_50"].items())
      + "; a quoted single word is matched as such, not traced). These run artifacts, configs and "
      "harness files stay if `b2_concepts.json` is replaced by a pointer, and, being "
      "committed, they are in the history. Whether single words and an eight-word subset need "
      "attribution is the PI's call (section 7, item 1).")
    P("")
    fr_hist =sorted({p for b, t in hist_text.items() if FR_MARK in t for p in hist_blob_paths[b]})
    tq_hist = sorted({p for b, t in hist_text.items() if TQ_MARK in t for p in hist_blob_paths[b]})
    tq_hist_norm = sorted({p for b, t in hist_text.items()
                           if TQ_MARK not in t and TQ_MARK in norm_text(t)
                           for p in hist_blob_paths[b]} - set(tq_hist))
    S1["history_paths_with_trial_question_wrapped_only"] = tq_hist_norm
    fr_first = gtext("log", "--all", "--format=%h %ad", "--date=short", "-S", FR_MARK,
                     "--", *fr_hist).strip().splitlines() if fr_hist else []
    S1["history_paths_with_framing_marker"] = fr_hist
    S1["history_paths_with_trial_question_marker"] = tq_hist
    S1["framing_marker_first_commit"] = fr_first[-1] if fr_first else None
    fr_gone = [p for p in fr_hist if p not in fr_files]
    tq_gone = [p for p in tq_hist if p not in tq_files]
    P(f"Across history ({HI['n_commits']} commits on every local ref, full trees): paths that ever "
      f"carried the framing marker: **{len(fr_hist)}** ({len(fr_gone)} not at HEAD"
      + (": " + ", ".join(f"`{p}`" for p in fr_gone) if fr_gone else "") + "); the trial-question "
      f"marker on a single line: **{len(tq_hist)}** ({len(tq_gone)} not at HEAD"
      + (": " + ", ".join(f"`{p}`" for p in tq_gone) if tq_gone else "") + "), plus "
      f"{len(tq_hist_norm)} path(s) whose versions carry it only wrapped or escaped"
      + (" (" + ", ".join(f"`{p}`" for p in tq_hist_norm) + ")" if tq_hist_norm else "")
      + ". The framing first "
      f"entered the record at `{S1['framing_marker_first_commit']}` (`git log -S`, oldest). So the "
      f"materials are in the published history whatever HEAD does: removing them at HEAD alone "
      f"would not unpublish them (that would need a history rewrite, a PI decision per N12(i)).")
    P("")
    # ACK: the record's own reading of their prompt structure, located by content
    rs = loc_src("RESULTS.md")
    ack_lines = [i for i in find_line(rs, 'assistant "Ok."') if "(framing)" in rs.splitlines()[i - 1]]
    S1["ack_record_locator"] = [f"RESULTS.md@{LOC[:7]}:{i}" for i in ack_lines]
    P("Source repository's license, **[recorded WebFetch read]**:")
    P("")
    for k in ("macar_repo_api", "macar_web_page", "macar_commit_at_pin",
              "macar_root_contents_at_pin", "macar_license_at_pin", "macar_license_on_main",
              "macar_readme_at_pin"):
        w = WEB_READS[k]
        P(f"- `{w['url']}` -> {json.dumps(w['result'])}")
    P("")
    pin_ok = (prov.get("commit_sha") == MACAR_PIN ==
              WEB_READS["macar_commit_at_pin"]["result"]["sha"])
    pushed_same = prov.get("pushed_at") == WEB_READS["macar_repo_api"]["result"]["pushed_at"]
    S1["pin_equals_recorded_commit"] = pin_ok
    S1["record_pushed_at_equals_current"] = pushed_same
    n_fr_sent = len(re.findall(r"[.!?](?:\s|$)", fr))
    tq_rec = bf["shared"]["trial_question"]
    n_tq_sent = len(re.findall(r"[.!?](?:\s|$)", tq_rec))
    S1["framing_sentences"] = n_fr_sent
    S1["trial_question_sentences"] = n_tq_sent
    P(f"Reading of the code repository: the record's pin equals the commit the API returned: "
      f"{pin_ok} (committed "
      f"{WEB_READS['macar_commit_at_pin']['result']['committer_date']}). The record's `pushed_at` "
      f"({prov.get('pushed_at')}) equals the repository's `pushed_at` at the read: {pushed_same}"
      f"{' -- nothing has been pushed since the recovery, so the pin is the head of `main`' if pushed_same else ''}. "
      f"**No license file exists** at the pinned sha or on `main`; GitHub's API reports "
      f"`license: null`. The README's License section is a research-use statement (\"released for "
      f"research purposes\") that names no license. The repository grants no redistribution "
      f"right. The materials taken from it are a {S1['n_canonical'][1]}-word concept list, a "
      f"{S1['n_baseline'][1]}-word baseline list, a one-line extraction template, a "
      f"{n_fr_sent}-sentence framing paragraph, the acknowledgement turn, a {n_tq_sent}-sentence "
      f"trial question and a completion fallback form. The paper is a second, licensed source for "
      f"some of them (next paragraph).")
    P("")
    # --- the paper (arXiv:2603.21396) as a licensed source, and the concepts' origin -----
    pa = WEB_READS["macar_paper_arxiv_abs"]["result"]
    pA = WEB_READS["macar_paper_html_app_a"]["result"]
    pB = WEB_READS["macar_paper_html_app_b"]["result"]
    lz = WEB_READS["lindsey_2025_page"]["result"]
    lz3 = WEB_READS["lindsey_2025_page_trial_prompt_round3"]["result"]
    pT = WEB_READS["macar_paper_html_table4_round3"]["result"]
    tch = WEB_READS["transformer_circuits_home_round4"]["result"]
    lead_in_files =sorted(p for p, t in text.items()
                           if lz3["second_human_turn_lead_in"].lower() in t.lower())
    S1["lindsey_lead_in_in_record"] = lead_in_files
    S1["prompt_text_first_publication"] = {
        "lindsey_2025_page": lz["date"], "macar_repo_created": WEB_READS["macar_repo_api"]["result"]["created_at"][:10],
        "macar_paper_v1": WEB_READS["macar_paper_arxiv_abs"]["result"]["versions"].get("v1")}
    det_src = text.get("valence_core/detection.py", "")
    ack_rec = re.search(r'^ACK\s*=\s*"([^"]*)"', det_src, re.M)
    S1["record_ACK"] = ack_rec.group(1) if ack_rec else None
    S1["record_trial_question_placeholder"] = re.findall(r"\{[a-z_]+\}", tq_rec)
    S1["paper"] = {"license": pa["license_label"], "license_link": pa["license_link"],
                   "framing_sentences_paper_vs_record": [pA["framing_sentences"], n_fr_sent],
                   "framing_len_record": len(fr)}
    RX_LINDSEY = re.compile(r"\bLindsey\b|Emergent Introspective Awareness|2025/introspection", re.I)
    lind_head = sorted(p for p, t in text.items() if RX_LINDSEY.search(t))
    lind_hist = sorted({p for b, t in hist_text.items() if RX_LINDSEY.search(t)
                        for p in hist_blob_paths[b]})
    S1["lindsey_2025_cited_in_record"] = {"head_files": lind_head, "history_paths": lind_hist}
    P(f"The paper, **[recorded WebFetch read]** `{WEB_READS['macar_paper_arxiv_abs']['url']}`: "
      f"\"{pa['title']}\" ({pa['citation']}, {pa['n_authors']} authors; v5 of "
      f"{pa['versions']['v5 (current)']}), license **{pa['license_label']}** "
      f"(`{pa['license_link']}`). Its HTML rendering "
      f"(`{WEB_READS['macar_paper_html_app_a']['url']}`, the whole page read) prints, in "
      f"{pA['location']}, the full prompt: turns {pA['turns_in_order']}, no system message: "
      f"{not pA['system_message']}. Against the record (fetch-tool comparison, not byte for byte): "
      f"the framing has {pA['framing_sentences']} sentences (record: {n_fr_sent}), about "
      f"{pA['framing_length_estimate_chars'].split()[-1]} characters (record: {len(fr)}), the same "
      f"first and last eight words: {pA['framing_first_and_last_eight_words_match_record']} "
      f"(the round-2 checker's read of the whole paragraph: "
      f"{pA['framing_wording_per_round2_checker_read']}; the round-3 fixer's read, sentence by "
      f"sentence: {pT['framing_sentences_identical_to_record'][0]} of "
      f"{pT['framing_sentences_identical_to_record'][1]} identical), "
      f"{pA['framing_dashes_around_thoughts']} and {pA['framing_quotes_around_thoughts']} around "
      f"*thoughts* (the record uses ` -- ` and straight quotes: "
      f"{' -- ' in fr and chr(34) + 'thoughts' + chr(34) in fr}); the acknowledgement equals the "
      f"record's `ACK` (\"{S1['record_ACK']}\"): {pA['ack_equals_record_ACK']}; the trial question "
      f"equals the record's apart from its placeholder: "
      f"{pA['trial_question_equals_record_modulo_placeholder']} (paper "
      f"{pA['trial_question_placeholder'].split(' (')[0]}, record "
      f"{', '.join(S1['record_trial_question_placeholder'])}; text before the trial line in that "
      f"turn: {pT['second_user_turn_has_text_before_trial_line']}). Appendix B.2 also prints the "
      f"extraction template ({pB['B2_extraction_template']}). So the framing, the "
      f"acknowledgement, the trial question and the extraction template are published under "
      f"{pa['license_label']} in the paper, separately from the unlicensed code repository the "
      f"record transcribed them from. A byte-level comparison with the paper's text is [to "
      f"confirm]; this raw does not quote the paper.")
    P("")
    P(f"The word lists. The 50 concepts printed anywhere in the paper (B.1 or the body): "
      f"{pB['B1_prints_the_50_concepts'] or pB['main_body_prints_the_50_concepts']}; the 100 "
      f"baseline words printed (B.2): {pB['B2_prints_the_100_baseline_words']}. Its Appendix "
      f"B.1 credits the 50 original concepts to Lindsey (2025), "
      f"{pB['references_entry_for_the_credited_work'].split(', ', 1)[1]}. That page, "
      f"**[recorded WebFetch read]** (the whole page read; fetch-tool comparisons), is "
      f"\"{lz['title']}\" ({lz['citation']}, {lz['date']}, {lz['venue']}). It prints the 50-word "
      f"concept list ({lz['prints_50_concept_list'].split(', ', 1)[1]}): {lz['concept_list_vs_record']}; "
      f"it prints 100 baseline words: {lz['baseline_list_vs_record']}; its extraction is "
      f"{lz['extraction']}; it prints the trial prompt ({lz['prints_trial_prompt'].split(', ', 1)[1]}). "
      f"That prompt against the record, **[recorded WebFetch read]** (round 3, "
      f"{lz3['location']}; fetch-tool comparisons, not byte for byte): the framing paragraph "
      f"{lz3['framing_sentences_identical_to_record'][0]} of "
      f"{lz3['framing_sentences_identical_to_record'][1]} sentences identical "
      f"({lz3['framing_dashes_and_quotes']}; the round-3 checker's read of the same paragraph "
      f"also found no differences: {lz3['agrees_with_round3_checker_framing_read']}); the "
      f"Assistant reply equals the record's `ACK`: {lz3['assistant_reply_equals_record_ACK']}; "
      f"the trial line equals the record's apart from the trial number: "
      f"{lz3['trial_line_equals_record_apart_from_number']}. One difference: its second Human "
      f"turn opens with a lead-in sentence (\"{lz3['second_human_turn_lead_in']}\") before the "
      f"trial line, which the paper's Table 4 does not have "
      f"({not pT['second_user_turn_contains_lindsey_lead_in']}) and the record does not carry "
      f"(tracked files at the commit containing it: {len(lead_in_files)}); the record's form is "
      f"the paper's. So the prompt text appeared first, of the three sources read, on the "
      f"Lindsey page ({lz['date']}; the repository was created "
      f"{S1['prompt_text_first_publication']['macar_repo_created']} and the paper's v1 is dated "
      f"{S1['prompt_text_first_publication']['macar_paper_v1']}). License or terms statement on "
      f"the page: {lz['license_or_terms_statement'] or 'none found'} (its citation section gives "
      f"a BibTeX entry only; the round-3 read of characters 300,000 to the end found none "
      f"either; the site's home page, **[recorded WebFetch read]** "
      f"`{WEB_READS['transformer_circuits_home_round4']['url']}` (round 4, the whole page): "
      f"site-wide license, copyright or terms statement: "
      f"{tch['license_copyright_or_terms_statement'] or 'none'}; link to one: "
      f"{tch['link_mentioning_license_copyright_terms_legal_or_reuse'] or 'none'}), so no license "
      f"is stated, and the Lindsey page's license is **[to confirm]**. The paper's author list "
      f"includes the author of Lindsey (2025): {pa['author_list_includes_the_lindsey_2025_author']}. "
      f"The record cites Lindsey (2025) nowhere: tracked files at the commit matching "
      f"`{RX_LINDSEY.pattern}` (case-insensitive): **{len(lind_head)}**; paths in any commit: "
      f"**{len(lind_hist)}**. Reading: of the sources read, the prompt text was first published "
      f"on the Lindsey page, with no license stated; the {pa['license_label']} grant for it comes only from the later "
      f"paper, whose authors include Lindsey, and whether that grant suffices for text its "
      f"co-author published first is the PI's judgement. The paper's grant does not reach the two "
      f"word lists, which it does not print; they come from the unlicensed repository and "
      f"originate on the Lindsey page, whose license this part did not establish. Per the block "
      f"(line 80): **the README attributes and the PI decides**, now per item (section 7, item 1).")
    P("")

    # =====================================================================
    # 2. Code ported or adapted from third parties
    # =====================================================================
    P("## 2. Code ported or adapted from third parties")
    P("")
    P("### 2a. Marker grep over tracked code and configs")
    P("")
    code_paths = sorted(p for p in text if p.endswith((".py", ".sh", ".ipynb", ".toml", ".cfg"))
                        or os.path.basename(p) in (".gitignore", ".gitattributes")
                        or p.startswith("data/configs/"))
    RX_THIRD = re.compile(r"safety-research|introspection-mechanisms|\bMacar\b|WeZZard|"
                          r"github\.com|huggingface\.co|arxiv", re.I)
    RX_THIRD_UNB = re.compile(RX_THIRD.pattern.replace(r"\bMacar\b", "Macar"), re.I)
    RX_SWLIC = re.compile(r"\bApache\b|\bMIT\b|SPDX|\bcopyright\b|\bGPL\b|\bBSD\b|"
                          r"open[- ]source|third[- ]party", re.I)
    RX_SWLIC_CS = re.compile(r"\bMIT\b|SPDX|\bGPL\b|\bBSD\b")
    RX_PORT = re.compile(r"\b(?:ported from|port of|adapted from|copied from|transcribed from|"
                         r"verbatim from|taken from|borrowed from|recovered verbatim)\b", re.I)
    RX_MACAR_CTX = re.compile(r"Macar|safety-research|introspection-mechanisms", re.I)
    clone_files_rel: set[str] = set()
    if os.path.isdir(CLONE):
        for root, dirs, files in os.walk(CLONE):
            dirs[:] = [d for d in dirs if d not in (".git", ".venv", "__pycache__")]
            for fn in files:
                clone_files_rel.add(os.path.relpath(os.path.join(root, fn), CLONE))

    def resolve(tok: str) -> list[str]:
        """Classify a file or module reference named on a port line."""
        t = tok.strip("`'\"()., ")
        t = re.sub(r":[\d\-]+$", "", t)
        out = []
        cands = []
        if t.endswith(".py"):
            cands = [t, f"scripts/{os.path.basename(t)}", f"jlens_qwen/{os.path.basename(t)}"]
        elif re.fullmatch(r"[a-z_0-9]+\.[A-Za-z_0-9]+", t):
            mod = t.split(".")[0]
            cands = [f"jlens_qwen/{mod}.py", f"valence_core/{mod}.py", f"scripts/{mod}.py"]
        for c in dict.fromkeys(cands):
            if c in by_path:
                out.append(f"{c}: tracked")
            if c in clone_files_rel:
                out.append(f"jlens-qwen36/{c}: " + ("UPSTREAM (WeZZard)" if c in
                                                   JLENS_UPSTREAM_BLOBS else "lab-added"))
        return out
    RX_LIC = re.compile(r"licen[cs]", re.I)
    RX_JLENS = re.compile(r"jlens", re.I)
    hits = {"third_party_ref": [], "software_license_word": [], "port_marker": []}
    lic_gate_counts: dict[str, int] = defaultdict(int)
    jlens_counts: dict[str, int] = defaultdict(int)
    jlens_imports: list[str] = []
    n_third_unb = 0
    unb_extra_ids: dict[str, int] = defaultdict(int)
    unb_extra_files: dict[str, int] = defaultdict(int)
    for p in code_paths:
        lines = text[p].splitlines()
        for i, line in enumerate(lines, 1):
            ctx = " ".join(lines[max(0, i - 3): i + 2])
            cats = []
            if RX_THIRD.search(line):
                cats.append("third_party_ref")
            if RX_THIRD_UNB.search(line):
                n_third_unb += 1
                if not RX_THIRD.search(line):
                    unb_extra_files[p] += 1
                    for m_ in re.finditer(r"\w*macar\w*", line, re.I):
                        unb_extra_ids[m_.group(0)] += 1
            sw = [m.group(0) for m in RX_SWLIC.finditer(line)]
            sw = [m for m in sw if m.lower() not in ("mit", "spdx", "gpl", "bsd")
                  or RX_SWLIC_CS.search(m)]
            if sw:
                cats.append("software_license_word")
            if RX_PORT.search(line):
                cats.append("port_marker")
            if RX_LIC.search(line) and not cats:
                lic_gate_counts[p] += 1
            if RX_JLENS.search(line):
                jlens_counts[p] += 1
                if re.search(r"^\s*(from|import)\s+\S*jlens|sys\.path\.insert\(.*jlens|"
                             r"importlib\.import_module\(.*jlens", line):
                    mm = re.search(r"jlens_qwen\.([a-z_0-9]+)", line)
                    cls = ""
                    if mm:
                        f_ = f"jlens_qwen/{mm.group(1)}.py"
                        cls = (" -> " + f_ + (": UPSTREAM (WeZZard)" if f_ in JLENS_UPSTREAM_BLOBS
                                              else ": lab-added" if f_ in clone_files_rel
                                              else ": not on disk"))
                    jlens_imports.append(f"{p}:{i}: {redact(line.strip()[:150], p)}{cls}")
            for c in cats:
                refs: list[str] = []
                if c == "port_marker":
                    nxt = " ".join(lines[i - 1: i + 1])
                    for tok in re.findall(r"`([^`]+)`", nxt) + re.findall(
                            r"\b[\w/.-]+\.py(?::[\d-]+)?", nxt):
                        refs += resolve(tok)
                    refs = list(dict.fromkeys(refs))
                if RX_MACAR_CTX.search(ctx):
                    src = "third-party (Macar et al.)"
                elif re.search(r"WeZZard", ctx) or any("UPSTREAM" in r for r in refs):
                    src = "third-party (WeZZard/jlens-qwen36)"
                elif any("lab-added" in r for r in refs):
                    src = "lab-internal (lab's own code in the clone)"
                elif refs:
                    src = "lab-internal (tracked file)"
                else:
                    src = "lab-internal (no file named)"
                hits[c].append({"loc": f"{p}:{i}", "text": redact(line.strip()[:170], p),
                                "refs": refs, "source_by_context_rule": src})
    R["marker_grep"] = {"n_files": len(code_paths), "hits": hits,
                        "licence_gate_sense_counts": dict(lic_gate_counts),
                        "jlens_mention_counts": dict(jlens_counts),
                        "jlens_import_lines": jlens_imports,
                        "third_party_pattern_as_implemented": RX_THIRD.pattern,
                        "third_party_lines_with_unbounded_Macar": n_third_unb,
                        "unbounded_extra_identifiers": dict(unb_extra_ids),
                        "unbounded_extra_files": dict(unb_extra_files)}
    n_extra = n_third_unb - len(hits["third_party_ref"])
    P(f"Files scanned: {len(code_paths)} (tracked `*.py`, `*.sh`, `*.ipynb`, `*.toml`, `*.cfg`, "
      f"`.gitignore`, `.gitattributes`, `data/configs/*`). Patterns: third-party references "
      f"(as implemented: `{RX_THIRD.pattern}`, case-insensitive; the word boundary on "
      f"`\\bMacar\\b` excludes identifiers: with an unbounded `Macar` the same scan gives "
      f"{n_third_unb} lines, {n_extra} more, in each of which `Macar` occurs only inside a longer "
      f"word, i.e. an identifier "
      f"({', '.join(f'`{k}` x{v}' for k, v in sorted(unb_extra_ids.items(), key=lambda x: -x[1]))}; "
      f"in {len(unb_extra_files)} files); software-license words (`Apache|copyright|open-source|third-party` "
      f"case-insensitive, `MIT|SPDX|GPL|BSD` case-sensitive); port markers (`ported from|port of|"
      f"adapted from|copied from|transcribed from|verbatim from|taken from|borrowed from|"
      f"recovered verbatim`, word-bounded). The `source` column applies a rule: third-party "
      f"(Macar) if the line or the two lines on either side mention Macar, safety-research or "
      f"introspection-mechanisms; third-party (WeZZard) if they mention WeZZard or a file named on "
      f"the port line (or the next line) resolves to an upstream jlens-qwen36 file; otherwise "
      f"lab-internal, split by whether the named file is a lab-added clone file, a tracked file, or "
      f"none. Code read every row; see the note after the tables.")
    P("")
    for c, title in (("third_party_ref", "Third-party references"),
                     ("software_license_word", "Software-license words"),
                     ("port_marker", "Port / copy markers")):
        P(f"**{title}: {len(hits[c])}**")
        P("")
        if hits[c]:
            P("| file:line | text (truncated) | files named (resolved) | source (rule) |")
            P("|---|---|---|---|")
            for h in hits[c]:
                t = h["text"].replace("|", "\\|")
                P(f"| `{h['loc']}` | {t} | {'; '.join(h['refs']) or '-'} | {h['source_by_context_rule']} |")
            P("")
    n_tp_port = sum(1 for h in hits["port_marker"] if h["source_by_context_rule"].startswith("third"))
    n_up_port = sum(1 for h in hits["port_marker"] if "WeZZard" in h["source_by_context_rule"])
    R["marker_grep"]["port_third_party"] = n_tp_port
    R["marker_grep"]["port_wezzard"] = n_up_port
    lab_refs = sorted({r.split(":")[0] for h in hits["port_marker"] for r in h["refs"]
                       if r.endswith("lab-added")})
    tr_refs = sorted({r.split(":")[0] for h in hits["port_marker"] for r in h["refs"]
                      if r.endswith("tracked")})
    R["marker_grep"]["port_refs_lab_added"] = lab_refs
    R["marker_grep"]["port_refs_tracked"] = tr_refs
    P(f"Note: port markers labelled third-party: {n_tp_port} ({n_tp_port - n_up_port} Macar: "
      f"their paradigm and their text; {n_up_port} naming an upstream jlens-qwen36 file). Files "
      f"named by the lab-internal port rows that resolve to lab-added clone files: "
      f"{', '.join(f'`{x}`' for x in lab_refs) or 'none'}; to tracked files: "
      f"{', '.join(f'`{x}`' for x in tr_refs) or 'none'}.")
    P("")
    # Code's reading of the rows the rule leaves without a resolvable source; each line's
    # text is asserted at the commit read so a moved or edited line shows as False.
    READS = [
        ("scripts/e2d_judge_port.py", 75, "verbatim from its main()",
         "code taken from S1's own `main()` in the tracked `scripts/s1_judge_rescue.py`: lab-internal"),
        ("valence_core/m/banner.py", 203, "verbatim from m:254-257",
         "banner text from PROPOSAL-m lines 254-257: lab-internal"),
        ("valence_core/m/bars.py", 548, "Adapted from f1's guard",
         "guard logic adapted from f1's guard in the lab's archive: lab-internal"),
        ("valence_core/m/readrule.py", 144, "the model copied from",
         "the model copying a tag from a header: data, not code"),
        ("valence_core/m/readrule.py", 456, "the model copied from",
         "the model copying a tag: data, not code"),
        ("valence_core/m/stages.py", 1940, "arguments taken from",
         "floors and launch counts taken from a lock: data, not code"),
        ("valence_core/m/verify.py", 28, "taken from the recorded round texts",
         "generations taken from recorded rounds: data, not code"),
        ("scripts/e2d_excision_check.py", 94, "taken from the committed D2 scoring",
         "scores taken from a committed artifact: data, not code"),
        ("scripts/e2d_excision_check.py", 124, "taken from",
         "scores taken from a committed artifact: data, not code"),
        ("scripts/b2r_scorer_selftest.py", 5, "quoted verbatim from the committed artifacts",
         "OLMo transcripts quoted from the lab's committed B2 artifacts: model output, not code"),
        ("scripts/b2r_scorer_selftest.py", 29, "verbatim from data/olmo/b2_",
         "the same transcripts: model output, not code"),
        ("scripts/k1_analyze.py", 50, "selected verbatim from",
         "the outcome sentence selected from PROPOSAL-k §1.5: lab text"),
        ("scripts/box_a3_extract.py", 17, "a third party",
         "\"third party\" in its stimulus sense (third-person evaluative content): not a license"),
        ("valence_core/neighbors.py", 35, "third party",
         "\"third party\" in its stimulus sense (S2): not a license"),
        ("valence_core/neighbors.py", 113, "third party",
         "\"third party\" in its stimulus sense (S2): not a license"),
        # added in round 2: a line committed after bbc9ffe (in c75d4d8, which touches no audit-note file)
        ("valence_core/m/gcal.py", 856, "not a port of it",
         "says a boundary assertion is a G-CAL addition to the lab's own f0 procedure, not a "
         "port of it: lab-internal"),
    ]
    read_rows = []
    for f_, ln, s, reading in READS:
        ok = f_ in text and ln - 1 < len(text[f_].splitlines()) and s in text[f_].splitlines()[ln - 1]
        read_rows.append({"loc": f"{f_}:{ln}", "expect": s, "asserted": ok, "reading": reading})
    unresolved = [h["loc"] for c in ("port_marker", "software_license_word") for h in hits[c]
                  if h["source_by_context_rule"] == "lab-internal (no file named)"]
    covered = {r["loc"] for r in read_rows if r["asserted"]}
    R["marker_grep"]["code_reads"] = read_rows
    R["marker_grep"]["no_file_rows"] = unresolved
    R["marker_grep"]["no_file_rows_uncovered"] = [u for u in unresolved if u not in covered]
    P(f"Code's reading of the {len(unresolved)} rows labelled \"no file named\" (each line's text "
      f"asserted at the commit read; uncovered rows: "
      f"{R['marker_grep']['no_file_rows_uncovered'] or 'none'}):")
    P("")
    P("| file:line | asserted text | asserted | Code's reading |")
    P("|---|---|---|---|")
    for r in read_rows:
        P(f"| `{r['loc']}` | \"{r['expect']}\" | {r['asserted']} | {r['reading']} |")
    P("")
    n_gate = sum(lic_gate_counts.values())
    P(f"**`licen[cs]e` in the lab's gate/approval sense** (\"licensed by\", \"licence covers\"; no "
      f"third-party or software-license word on the line): {n_gate} lines in {len(lic_gate_counts)} "
      f"files, counted and not listed; the largest are "
      + ", ".join(f"`{p}` {n}" for p, n in sorted(lic_gate_counts.items(), key=lambda x: -x[1])[:6])
      + ".")
    P("")
    n_venv = sum(1 for p in code_paths for l in text[p].splitlines()
                 if "jlens" in l.lower() and ".venv/bin/python" in l)
    R["marker_grep"]["jlens_venv_usage_lines"] = n_venv
    P(f"**`jlens` mentions:** {sum(jlens_counts.values())} lines in {len(jlens_counts)} files, "
      f"{n_venv} of them interpreter-usage lines (`jlens-qwen36/.venv/bin/python ...`); the rest "
      f"are docstrings, comments, test fixtures and these import or path-insert lines. The import or path-insert "
      f"lines are listed here; they show the **dependency** on the clone (imported at run time), "
      f"not a copy of it:")
    P("")
    for j in jlens_imports:
        P(f"- `{j}`")
    P("")

    # ---------------------------------------------------------------------
    P("### 2b. The Macar port: what was carried over, and how")
    P("")
    det = text["valence_core/detection.py"]
    det_defs = defs_of(det) or []
    det_names = {d["name"] for d in det_defs}
    theirs = set(WEB_READS["macar_01_concept_injection_defs"]["result"]["defs"]) | {
        n.split(" ")[0] for n in WEB_READS["macar_vector_utils_defs"]["result"]["defs"]}
    ours_b2 = set()
    for p in ("valence_core/detection.py", "valence_core/detection_v2.py",
              "scripts/box_b2_concepts.py", "scripts/box_b2r_concepts.py",
              "scripts/box_b2_detection.py", "scripts/box_b2r_campaign.py",
              "scripts/box_b2r_sampling_smoke.py", "scripts/b2_analyze.py",
              "scripts/b2r_analyze.py"):
        if p in text:
            for d in defs_of(text[p]) or []:
                ours_b2.add(d["name"])
    shared_macar = sorted(theirs & ours_b2)
    has_kw = all(re.search(rf"^{n}\s*=", det, re.M) for n in ("_AFFIRM", "_DENY"))
    consts = [n for n in ("MACAR_FRAMING", "TRIAL_QUESTION", "COMPLETION_TEMPLATE", "ACK")
              if re.search(rf"^{n}\s*=", det, re.M)]
    R["macar_port"] = {"our_b2_def_names": sorted(ours_b2), "their_def_names": sorted(theirs),
                       "shared_def_names": shared_macar,
                       "detection_py_keyword_scorer": has_kw,
                       "detection_py_constants": consts}
    hdr_ok = det.startswith('"""Detection-behavioral harness (Phase 0 step 5) -- ported from Macar')
    cites = "experiments/01_concept_injection.py" in det
    R["macar_port"].update({"header_ported_from_macar": hdr_ok, "cites_their_file": cites})
    P(f"- Header, `valence_core/detection.py:1-2` (asserted: {hdr_ok}): \"ported from Macar et "
      f"al.'s concept-injection paradigm, adapted to completion-style\". The docstring names their "
      f"`experiments/01_concept_injection.py` as the paradigm's source (asserted: {cites}) and "
      f"logs the chat-template deviation (rule 13).")
    P(f"- Function and class names defined in our nine B2/B2-r files (detection.py, detection_v2.py, "
      f"box_b2_concepts.py, box_b2r_concepts.py, box_b2_detection.py, box_b2r_campaign.py, "
      f"box_b2r_sampling_smoke.py, b2_analyze.py, b2r_analyze.py): {len(ours_b2)}. Names in their "
      f"`01_concept_injection.py` and `src/vector_utils.py` at the pin **[recorded WebFetch read]**: "
      f"{len(theirs)}. **Shared names: {len(shared_macar)}** {shared_macar if shared_macar else ''}"
      f" (not in the generic-name list: {len([n for n in shared_macar if n not in GENERIC_NAMES])}).")
    P(f"- Scoring differs in kind: theirs is an LLM judge (recorded read); ours "
      f"(`detection.py`) is a keyword scorer, `_AFFIRM`/`_DENY` defined: {has_kw}.")
    c_verb = "# Their framing, verbatim, for replication fidelity." in det
    c_fall = "# Their own non-chat fallback, made the only path (rule 13)." in det
    R["macar_port"].update({"comment_framing_verbatim": c_verb, "comment_fallback": c_fall})
    P(f"- What is carried over **verbatim** is text, not code. `detection.py` defines {consts}; "
      f"its own comments mark `MACAR_FRAMING` as \"Their framing, verbatim\" (asserted: {c_verb}) "
      f"and `COMPLETION_TEMPLATE` as built on \"Their own non-chat fallback\" (asserted: {c_fall}); "
      f"`TRIAL_QUESTION` is the question its docstring quotes from their paradigm; `ACK` "
      f"(\"Ok.\") is their assistant turn: the record's reading of their prompt, "
      f"`system \"\"` -> user (framing) -> `assistant \"Ok.\"` -> user (trial question), is at "
      f"{', '.join(f'`{x}`' for x in S1['ack_record_locator']) or '[not found at the commit]'} "
      f"(located by content). In `b2_concepts.json`: their "
      f"{S1['n_canonical'][1]} test concepts, their first {S1['n_baseline'][1]} baseline words and "
      f"the `Tell me about {{word}}` extraction template. `box_b2_concepts.py` and "
      f"`box_b2r_concepts.py` follow their extraction method (concept minus baseline mean, last "
      f"token), citing `src/vector_utils.py:114` and `03_behavioral_robustness.py:298`.")
    P("- Code's reading: the harness is a **reimplementation** of their paradigm, with their stimulus "
      "text carried verbatim; no function body was compared against theirs line by line, because "
      "their code was read only through WebFetch summaries (names, constants, scoring method), not "
      "downloaded. The license question is therefore section 1's: the prompt text (framing, "
      "acknowledgement, trial question, extraction template) is also printed in their paper under "
      f"{WEB_READS['macar_paper_arxiv_abs']['result']['license_label']}, and the framing, "
      "acknowledgement and trial question appeared earlier on the Lindsey (2025) page, which "
      "states no license; the two word lists are not in the paper, and their repository states "
      "no license.")
    P("")

    # ---------------------------------------------------------------------
    P("### 2c. `jlens-qwen36/` (gitignored clone of WeZZard/jlens-qwen36)")
    P("")
    J: dict = {"present": os.path.isdir(CLONE)}
    UP: dict = {"ok": False, "error": "clone absent"}
    up_src: dict[str, bytes] = {}
    if J["present"]:
        cfg = open(os.path.join(CLONE, ".git", "config")).read()
        m = re.search(r'\[remote "origin"\][^\[]*?url\s*=\s*(\S+)', cfg, re.S)
        J["origin_url"] = m.group(1) if m else None
        headref = open(os.path.join(CLONE, ".git", "HEAD")).read().strip()
        J["head_ref"] = headref
        sha = None
        if headref.startswith("ref: "):
            rp = os.path.join(CLONE, ".git", headref[5:])
            if os.path.isfile(rp):
                sha = open(rp).read().strip()
            else:
                pr = os.path.join(CLONE, ".git", "packed-refs")
                if os.path.isfile(pr):
                    for ln in open(pr):
                        if ln.strip().endswith(headref[5:]):
                            sha = ln.split()[0]
        else:
            sha = headref
        J["head_commit"] = sha
        pr = os.path.join(CLONE, ".git", "packed-refs")
        origin_main = None
        if os.path.isfile(pr):
            for ln in open(pr):
                if ln.strip().endswith("refs/remotes/origin/main"):
                    origin_main = ln.split()[0]
        J["origin_main_at_clone"] = origin_main
        lic = open(os.path.join(CLONE, "LICENSE"), "rb").read()
        lic_t = lic.decode("utf-8", "replace")
        J["license_sha256"] = sha256(lic)
        J["license_first_line"] = next(l.strip() for l in lic_t.splitlines() if l.strip())
        cm = re.search(r"^\s*(Copyright \d{4} .+)$", lic_t, re.M)
        J["license_copyright_line"] = cm.group(1).strip() if cm else None
        rd = open(os.path.join(CLONE, "README.md"), encoding="utf-8", errors="replace").read()
        rm = re.search(r"^## License\s*\n+(.+)$", rd, re.M)
        J["readme_license_line"] = rm.group(1).strip() if rm else None

        # upstream content from the clone's own object store (read as files)
        try:
            store = CloneObjects(os.path.join(CLONE, ".git"))
            ct, cbody = store.get(JLENS_CLONE_COMMIT)
            assert ct == "commit"
            up_tree_sha = cbody.split(b"\n", 1)[0].split()[1].decode()
            up_tree = store.tree_blobs(up_tree_sha)
            for pth, (mode, bsha) in up_tree.items():
                up_src[pth] = store.get(bsha)[1]
            idx = read_git_index(os.path.join(CLONE, ".git", "index"))
            disk_diff = []
            for pth, e in sorted(idx.items()):
                fp = os.path.join(CLONE, pth)
                if not os.path.isfile(fp) or git_blob_sha1(open(fp, "rb").read()) != e["sha"]:
                    disk_diff.append(pth)
            UP = {"ok": True, "commit_object_verified": True, "tree": up_tree_sha,
                  "n_blobs": len(up_tree),
                  "paths_equal_recorded_webfetch_list": set(up_tree) == set(JLENS_UPSTREAM_BLOBS),
                  "n_index_entries": len(idx),
                  "index_paths_equal_tree": set(idx) == set(up_tree),
                  "index_shas_equal_tree": sum(1 for p in idx if p in up_tree
                                               and idx[p]["sha"] == up_tree[p][1]),
                  "on_disk_differs_from_index": disk_diff,
                  "blob_shas": {p: s for p, (m, s) in up_tree.items()},
                  "empty_blobs": sorted(p for p, b in up_src.items() if not b)}
        except Exception as ex:  # reported, and the pass line is gated on it
            UP = {"ok": False, "error": f"{type(ex).__name__}: {ex}"}
        J["upstream_object_store"] = UP

        tracked_in_clone = [r["path"] for r in tree if r["path"].startswith("jlens-qwen36/")]
        hist_clone = [p for p in hist_paths if p.startswith("jlens-qwen36/")]
        J["tracked_paths_under_clone_at_commit"] = tracked_in_clone
        J["paths_under_clone_in_any_commit_all_refs"] = hist_clone

        # byte identity: every clone file whose size equals a tracked blob's size
        size_index: dict[int, list[dict]] = defaultdict(list)
        for r in tree:
            if r["type"] == "blob":
                size_index[r["size"]].append(r)
        walked = hashed = empty_skipped = 0
        matches = []
        clone_py: dict[str, str] = {}
        for root, dirs, files in os.walk(CLONE):
            dirs[:] = [d for d in dirs if d not in (".git", ".venv", "__pycache__")]
            for fn in files:
                if fn == ".DS_Store":
                    continue
                fp = os.path.join(root, fn)
                rel = os.path.relpath(fp, CLONE)
                walked += 1
                try:
                    sz = os.path.getsize(fp)
                except OSError:
                    continue
                if rel.endswith(".py"):
                    clone_py[rel] = open(fp, encoding="utf-8", errors="replace").read()
                if sz == 0:
                    empty_skipped += 1
                    continue
                if sz in size_index:
                    hashed += 1
                    b = open(fp, "rb").read()
                    bs = git_blob_sha1(b)
                    for r in size_index[sz]:
                        if r["blob"] == bs:
                            matches.append({"clone_path": rel, "tracked_path": r["path"],
                                            "size": sz,
                                            "class": ("UPSTREAM (WeZZard)" if rel in
                                                      JLENS_UPSTREAM_BLOBS else "lab-added")})
        J["walk"] = {"files_walked": walked, "size_matched_and_hashed": hashed,
                     "empty_files_skipped": empty_skipped}
        J["byte_identical"] = matches
        upstream_present = [p for p in JLENS_UPSTREAM_BLOBS
                            if os.path.isfile(os.path.join(CLONE, p))]
        J["upstream_paths_present_on_disk"] = len(upstream_present)
        lab_added_py = sorted(p for p in clone_py if p not in JLENS_UPSTREAM_BLOBS)
        up_py = sorted(p for p in clone_py if p in JLENS_UPSTREAM_BLOBS)
        J["n_upstream_py_on_disk"] = len(up_py)
        J["n_lab_added_py_on_disk"] = len(lab_added_py)

        # AST + long-line comparison: tracked .py/.ipynb vs upstream .py / lab-added .py
        tracked_src: dict[str, str] = {}
        for p in text:
            if p.endswith(".py"):
                tracked_src[p] = text[p]
            elif p.endswith(".ipynb"):
                tracked_src[p] = ipynb_code(text[p].encode())
        tracked_defs = {}
        parse_fail = []
        for p, s in tracked_src.items():
            d = defs_of(s)
            if d is None:
                parse_fail.append(p)
            else:
                tracked_defs[p] = d
        tracked_lines = {p: long_lines(s) for p, s in tracked_src.items()}

        def compare(side_src: dict, tdefs: dict, tlines: dict):
            sd = {p: (defs_of(side_src[p]) or []) for p in side_src}
            sl = {p: long_lines(side_src[p]) for p in side_src}
            fp_index = defaultdict(list)
            name_index = defaultdict(set)
            for p, ds in sd.items():
                for d in ds:
                    fp_index[d["fp"]].append((p, d))
                    name_index[d["name"]].add(p)
            body = []
            names = defaultdict(lambda: {"clone": set(), "tracked": set()})
            for tp, ds in tdefs.items():
                for d in ds:
                    if d["fp"] in fp_index and d["n_stmts"] >= 3:
                        for cp, cd in fp_index[d["fp"]]:
                            body.append({"tracked": f"{tp}:{d['line']}", "name": d["name"],
                                         "n_stmts": d["n_stmts"],
                                         "clone": f"jlens-qwen36/{cp}:{cd['line']}"})
                    if d["name"] in name_index:
                        names[d["name"]]["clone"] |= name_index[d["name"]]
                        names[d["name"]]["tracked"].add(tp)
            line_index = defaultdict(set)
            for p, ls in sl.items():
                for s in ls:
                    line_index[s].add(p)
            shared_lines = []
            for tp, ls in tlines.items():
                for s, ln in ls.items():
                    if s in line_index:
                        shared_lines.append({"tracked": f"{tp}:{ln}", "clone_files":
                                             sorted(line_index[s]), "text": s})
            grouped = defaultdict(lambda: {"tracked": [], "clone_files": set()})
            for x in shared_lines:
                grouped[x["text"]]["tracked"].append(x["tracked"])
                grouped[x["text"]]["clone_files"] |= set(x["clone_files"])
            grouped_l = sorted(({"text": k, "n_tracked": len(v["tracked"]),
                                 "tracked": v["tracked"], "clone_files": sorted(v["clone_files"])}
                                for k, v in grouped.items()), key=lambda g: -g["n_tracked"])
            # near-copy: max token-5-gram Jaccard of each tracked function (>= 5 stmts)
            # against every clone function (>= 5 stmts), via an inverted shingle index
            cdefs = [(p, d) for p, ds in sd.items() for d in ds if d["sh"]]
            inv = defaultdict(list)
            for j, (p, d) in enumerate(cdefs):
                for s in d["sh"]:
                    inv[s].append(j)
            near = []
            for tp, ds in tdefs.items():
                for d in ds:
                    if not d["sh"]:
                        continue
                    cnt = defaultdict(int)
                    for s in d["sh"]:
                        for j in inv.get(s, ()):
                            cnt[j] += 1
                    best, bj = 0.0, None
                    for j, c in cnt.items():
                        jac = c / (len(d["sh"]) + len(cdefs[j][1]["sh"]) - c)
                        if jac > best:
                            best, bj = jac, j
                    if bj is not None:
                        cp, cd = cdefs[bj]
                        near.append({"tracked": f"{tp}:{d['line']}", "name": d["name"],
                                     "n_stmts": d["n_stmts"], "jaccard": round(best, 3),
                                     "clone": f"jlens-qwen36/{cp}:{cd['line']}",
                                     "clone_name": cd["name"]})
            near.sort(key=lambda x: -x["jaccard"])
            hist = {t: sum(1 for x in near if x["jaccard"] >= t) for t in (0.3, 0.5, 0.8)}
            nm = {k: {"clone": sorted(v["clone"]), "tracked": sorted(v["tracked"]),
                      "generic": k in GENERIC_NAMES} for k, v in sorted(names.items())}
            return {"identical_bodies_ge3": body, "shared_names": nm,
                    "shared_long_lines": shared_lines, "shared_long_lines_grouped": grouped_l,
                    "near_copy_top": near[:25], "near_copy_counts": hist,
                    "n_tracked_funcs_ge5": sum(1 for ds in tdefs.values()
                                               for d in ds if d["sh"]),
                    "n_clone_funcs_ge5": len(cdefs)}

        J["ast_parse_failures_tracked"] = parse_fail
        if UP.get("ok"):
            up_side = {p: up_src[p].decode("utf-8", "replace") for p in sorted(up_src)
                       if p.endswith(".py")}
            J["upstream_side"] = "read from the object store at commit d788bc3"
        else:
            up_side = {p: clone_py[p] for p in up_py}
            J["upstream_side"] = "the on-disk copies, the object store being unreadable"
        J["n_upstream_py_compared"] = len(up_side)
        J["vs_upstream"] = compare(up_side, tracked_defs, tracked_lines)
        lab = compare({p: clone_py[p] for p in lab_added_py}, tracked_defs, tracked_lines)
        J["vs_lab_added_positive_control"] = {
            "n_identical_bodies_ge3": len(lab["identical_bodies_ge3"]),
            "identical_examples": lab["identical_bodies_ge3"][:8],
            "n_shared_names_nongeneric": sum(1 for v in lab["shared_names"].values()
                                             if not v["generic"]),
            "n_shared_long_lines": len(lab["shared_long_lines"]),
            "n_shared_long_lines_distinct": len(lab["shared_long_lines_grouped"]),
            "tracked_files_with_shared_lines": sorted({x["tracked"].rsplit(":", 1)[0]
                                                       for x in lab["shared_long_lines"]}),
            "near_copy_counts": lab["near_copy_counts"],
            "near_copy_top": lab["near_copy_top"][:10],
            "n_clone_funcs_ge5": lab["n_clone_funcs_ge5"]}

        # ---- the same question over the whole published history ---------------------
        HC: dict = {"ran": False}
        if UP.get("ok"):
            up_nonempty = {s: p for p, s in UP["blob_shas"].items() if up_src[p]}
            up_empty = {s for p, s in UP["blob_shas"].items() if not up_src[p]}
            head_blobs = {r["blob"] for r in tree if r["type"] == "blob"}
            hist_py = {b: (ipynb_code(hist_text[b].encode()) if all(p.endswith(".ipynb") for p in
                                                                     hist_blob_paths[b])
                           else hist_text[b])
                       for b in hist_text if any(p.endswith((".py", ".ipynb"))
                                                 for p in hist_blob_paths[b])}
            h_defs, h_fail = {}, []
            for b, s in hist_py.items():
                d = defs_of(s)
                if d is None:
                    h_fail.append(hloc(b))
                else:
                    h_defs[hloc(b)] = d
            h_lines = {hloc(b): long_lines(s) for b, s in hist_py.items()}
            hcmp = compare(up_side, h_defs, h_lines)
            # whole-file containment: share of an upstream file's token 5-grams found in
            # one historical blob (max over blobs), for each upstream .py file
            up_sh = {p: _shingles(s) for p, s in up_side.items()}
            inv_up = defaultdict(list)
            for p, sh in up_sh.items():
                for g in sh:
                    inv_up[g].append(p)
            best_cont = []
            for b, s in hist_py.items():
                cnt = defaultdict(int)
                for g in _shingles(s):
                    for p in inv_up.get(g, ()):
                        cnt[p] += 1
                for p, c in cnt.items():
                    best_cont.append((round(c / len(up_sh[p]), 3), p, hloc(b)))
            best_cont.sort(reverse=True)
            HC = {"ran": True,
                  "n_commits": HI["n_commits"], "n_entries": HI["n_entries"],
                  "n_distinct_blobs": HI["n_distinct_blobs"],
                  "n_distinct_paths": HI["n_distinct_paths"],
                  "n_upstream_nonempty_blobs": len(up_nonempty),
                  "upstream_nonempty_blobs_at_head": sorted(up_nonempty[s] for s in
                                                            head_blobs & set(up_nonempty)),
                  "upstream_nonempty_blobs_in_history": sorted(
                      f"{up_nonempty[s]} == {hloc(s)}" for s in
                      set(hist_blob_paths) & set(up_nonempty)),
                  "empty_blob_in_history": bool(up_empty & set(hist_blob_paths)),
                  "n_hist_py_ipynb_blobs": len(hist_py), "parse_failures": h_fail,
                  "n_hist_funcs_ge5": hcmp["n_tracked_funcs_ge5"],
                  "near_copy_counts": hcmp["near_copy_counts"],
                  "near_copy_top": hcmp["near_copy_top"][:5],
                  "identical_bodies_ge3": hcmp["identical_bodies_ge3"],
                  "n_shared_long_lines_distinct": len(hcmp["shared_long_lines_grouped"]),
                  "shared_long_lines_distinct": [g["text"][:150] for g in
                                                 hcmp["shared_long_lines_grouped"]],
                  "max_whole_file_containment_top": best_cont[:5]}
        J["history_copy_check"] = HC
    R["jlens"] = J

    if J["present"]:
        P(f"- Clone origin (read from `jlens-qwen36/.git/config` as a file): `{J['origin_url']}`; "
          f"HEAD `{J['head_ref']}` -> `{J['head_commit']}`; `refs/remotes/origin/main` in "
          f"packed-refs -> `{J['origin_main_at_clone']}` (local `main` = origin at clone time: "
          f"{J['head_commit'] == J['origin_main_at_clone']}). The upstream tree at that commit "
          f"(62 blobs) is the **[recorded WebFetch read]** "
          f"`{WEB_READS['wezzard_tree_at_clone_commit']['url']}`; commit equals the recorded one: "
          f"{J['head_commit'] == JLENS_CLONE_COMMIT}.")
        P(f"- License on disk: `jlens-qwen36/LICENSE` first line \"{J['license_first_line']}\", "
          f"appendix line \"{J['license_copyright_line']}\", sha256 `{J['license_sha256'][:16]}...`; "
          f"its README's License section: \"{J['readme_license_line']}\". GitHub API "
          f"**[recorded WebFetch read]**: `{json.dumps(WEB_READS['wezzard_repo_api']['result']['license'])}`.")
        P(f"- Upstream paths present on disk: {J['upstream_paths_present_on_disk']}/62. Python files "
          f"on disk under the clone (excluding `.venv`, `.git`, `__pycache__`): "
          f"{J['n_upstream_py_on_disk']} upstream, {J['n_lab_added_py_on_disk']} **lab-added** "
          f"(the cycle-1-4 code, e.g. `jlens_qwen/e2a.py`, `forced_choice.py`, `conditioning.py`, "
          f"`scripts/e2a_sessions.py`, which upstream does not have; CLAUDE.md calls them the "
          f"clone's \"local patches\").")
        if UP.get("ok"):
            P(f"- Upstream content, from the clone's object store read as files (pack + loose "
              f"objects parsed in Python; every object's sha1 re-verified): commit "
              f"`{JLENS_CLONE_COMMIT[:12]}` -> tree `{UP['tree'][:12]}` -> **{UP['n_blobs']} blobs**; "
              f"paths equal the recorded WebFetch tree list: {UP['paths_equal_recorded_webfetch_list']}. "
              f"The clone's `.git/index` (read as a file): {UP['n_index_entries']} entries, paths "
              f"equal the tree's: {UP['index_paths_equal_tree']}, blob shas equal the tree's: "
              f"{UP['index_shas_equal_tree']}/{UP['n_blobs']}. **{len(UP['on_disk_differs_from_index'])} "
              f"of {UP['n_index_entries']} upstream files differ on disk from the index** (local "
              f"edits): " + ", ".join(f"`{p}`" for p in UP["on_disk_differs_from_index"]) + ". "
              f"The code comparison below therefore uses the committed upstream blobs "
              f"({J['upstream_side']}), not the on-disk copies.")
        else:
            P(f"- Upstream object store not readable ({UP.get('error')}); the comparison below "
              f"uses the on-disk copies, which may carry local edits.")
        P(f"- **Tracked paths under `jlens-qwen36/`:** at the commit "
          f"{len(J['tracked_paths_under_clone_at_commit'])}; in any commit on any ref "
          f"{len(J['paths_under_clone_in_any_commit_all_refs'])}.")
        bi = J["byte_identical"]
        up_bi = [m for m in bi if m["class"].startswith("UPSTREAM")]
        P(f"- **Byte-identical files** (git blob sha1 of each non-empty clone file whose size "
          f"equals a tracked blob's; {J['walk']['files_walked']} files walked, "
          f"{J['walk']['empty_files_skipped']} empty files skipped as uninformative, "
          f"{J['walk']['size_matched_and_hashed']} size-matched and hashed): {len(bi)} matches, "
          f"**{len(up_bi)} of them upstream files**. Every match is a lab-added clone file (data, "
          f"configs, run artifacts) that the record pulled from the clone byte-identical; all "
          f"matches outside the upstream list: {all(m['class'] == 'lab-added' for m in bi)}.")
        if bi:
            P("")
            P("| clone path | tracked path | bytes | class |")
            P("|---|---|---|---|")
            for m in bi:
                P(f"| `jlens-qwen36/{m['clone_path']}` | `{m['tracked_path']}` | {m['size']} | {m['class']} |")
        P("")
        vu = J["vs_upstream"]
        ng = {k: v for k, v in vu["shared_names"].items() if not v["generic"]}
        nc = vu["near_copy_counts"]
        P(f"- **Code comparison at HEAD, tracked code vs the {J['n_upstream_py_compared']} upstream "
          f"`.py` files** ({J['upstream_side']}; tracked `.py` + the notebook's code cells; tracked "
          f"files that failed to parse: {J['ast_parse_failures_tracked'] or 'none'}). Four measures:")
        P(f"  1. identical def/class bodies (sha256 of `ast.dump`, docstring removed, positions "
          f"dropped; >= 3 statements): **{len(vu['identical_bodies_ge3'])}**;")
        P(f"  2. near-copies: for each tracked function of >= {NEAR_MIN_STMTS} statements "
          f"({vu['n_tracked_funcs_ge5']}), the best token-{SHINGLE_K}-gram Jaccard against any "
          f"upstream function of >= {NEAR_MIN_STMTS} statements ({vu['n_clone_funcs_ge5']}): "
          f"**>= 0.8: {nc[0.8]}; >= 0.5: {nc[0.5]}**; >= 0.3: {nc[0.3]};")
        P(f"  3. shared def/class names: {len(vu['shared_names'])} ({len(ng)} not in the "
          f"generic-name list);")
        P(f"  4. shared normalised source lines of >= 60 characters (imports excluded): "
          f"{len(vu['shared_long_lines'])} occurrences of **{len(vu['shared_long_lines_grouped'])} "
          f"distinct lines**.")
        if vu["identical_bodies_ge3"]:
            P("")
            for b in vu["identical_bodies_ge3"]:
                P(f"  - identical body: `{b['tracked']}` `{b['name']}` ({b['n_stmts']} stmts) == `{b['clone']}`")
        P("")
        P("  Top near-copy scores against upstream (all at or above 0.3, else the top 5):")
        shown = [x for x in vu["near_copy_top"] if x["jaccard"] >= 0.3] or vu["near_copy_top"][:5]
        for x in shown:
            P(f"  - {x['jaccard']}: `{x['tracked']}` `{x['name']}` ({x['n_stmts']} stmts) vs "
              f"`{x['clone']}` `{x['clone_name']}`")
        if vu["shared_names"]:
            P("")
            P("  Shared names (generic-list flag in brackets):")
            for k, v in vu["shared_names"].items():
                P(f"  - `{k}`{' [generic]' if v['generic'] else ''}: upstream {v['clone']}; "
                  f"tracked {v['tracked'][:6]}{' ...' if len(v['tracked']) > 6 else ''}")
        if vu["shared_long_lines_grouped"]:
            P("")
            P("  Shared long lines, distinct (occurrences in tracked files; upstream files):")
            for g in vu["shared_long_lines_grouped"]:
                t = redact(g["text"][:150], "shared-line").replace("|", "\\|")
                P(f"  - x{g['n_tracked']} (e.g. `{g['tracked'][0]}`); upstream {g['clone_files']}: `{t}`")
        P("")
        pc = J["vs_lab_added_positive_control"]
        pnc = pc["near_copy_counts"]
        P(f"- **Positive control (same four measures, tracked code vs the "
          f"{J['n_lab_added_py_on_disk']} lab-added `.py` files in the clone, which the record says "
          f"several tracked modules were ported from):** identical bodies "
          f"{pc['n_identical_bodies_ge3']}; near-copies >= 0.8: {pnc[0.8]}, >= 0.5: {pnc[0.5]}, "
          f">= 0.3: {pnc[0.3]}; non-generic shared names {pc['n_shared_names_nongeneric']}; shared "
          f"long lines {pc['n_shared_long_lines']} ({pc['n_shared_long_lines_distinct']} distinct) in "
          f"{len(pc['tracked_files_with_shared_lines'])} tracked files. `valence_core/discrim.py` "
          f"(docstring: ported from `scripts/e2a_g2_discriminability.py`, a lab-added clone file) "
          f"among the shared-line files: "
          f"{'valence_core/discrim.py' in pc['tracked_files_with_shared_lines']}. Reading: measure 1 "
          f"finds {pc['n_identical_bodies_ge3']} here too, so exact-body identity misses edited ports "
          f"and is not the measure this conclusion rests on. Measure 2 separates the two sides: best "
          f"pair against lab-added "
          f"{pc['near_copy_top'][0]['jaccard'] if pc['near_copy_top'] else 'n/a'}, best against upstream "
          f"{vu['near_copy_top'][0]['jaccard'] if vu['near_copy_top'] else 'n/a'}. The "
          f"{len(vu['shared_long_lines_grouped'])} distinct upstream shared lines above are path and "
          f"checkpoint boilerplate (Code's read). Top near-copy pairs against lab-added:")
        for x in pc["near_copy_top"][:8]:
            P(f"  - {x['jaccard']}: `{x['tracked']}` `{x['name']}` ({x['n_stmts']} stmts) vs "
              f"`{x['clone']}` `{x['clone_name']}`")
        P("")
        HC = J["history_copy_check"]
        if HC.get("ran"):
            hn = HC["near_copy_counts"]
            P(f"- **History-wide copy check (the release publishes every commit).** All "
              f"{HC['n_commits']} commits reachable from the local refs, full trees "
              f"({HC['n_entries']} tree entries, {HC['n_distinct_blobs']} distinct blobs, "
              f"{HC['n_distinct_paths']} distinct paths; non-blob entries such as gitlinks: "
              f"{HI['n_non_blob_entries']}):")
            P(f"  1. upstream blobs by sha ({HC['n_upstream_nonempty_blobs']} non-empty upstream "
              f"blobs): at HEAD **{len(HC['upstream_nonempty_blobs_at_head'])}**, in any commit "
              f"**{len(HC['upstream_nonempty_blobs_in_history'])}**"
              + (": " + "; ".join(HC["upstream_nonempty_blobs_in_history"])
                 if HC["upstream_nonempty_blobs_in_history"] else "")
              + f" (the empty blob, which carries no content, occurs in history: "
              f"{HC['empty_blob_in_history']});")
            P(f"  2. near-copies, every distinct historical `.py`/`.ipynb` blob "
              f"({HC['n_hist_py_ipynb_blobs']} blobs, {HC['n_hist_funcs_ge5']} functions of >= "
              f"{NEAR_MIN_STMTS} statements; parse failures {len(HC['parse_failures'])}) against "
              f"the upstream functions: **>= 0.8: {hn[0.8]}; >= 0.5: {hn[0.5]}; >= 0.3: {hn[0.3]}**; "
              f"best " + "; ".join(f"{x['jaccard']} `{x['tracked']}` `{x['name']}` vs "
                                   f"`{x['clone']}` `{x['clone_name']}`"
                                   for x in HC["near_copy_top"][:3]) + ";")
            P(f"  3. identical def/class bodies (>= 3 statements): "
              f"**{len(HC['identical_bodies_ge3'])}**; distinct shared long lines: "
              f"{HC['n_shared_long_lines_distinct']} (the HEAD set's boilerplate kind: "
              + "; ".join(f"`{redact(t, 'hist-line').replace('|', chr(92) + '|')}`"
                          for t in HC["shared_long_lines_distinct"]) + ");")
            P("  4. whole-file containment, the share of one upstream file's token 5-grams found "
              "in a single historical blob, top 3: "
              + "; ".join(f"{c} (`{p}` in `{loc}`)" for c, p, loc in
                          HC["max_whole_file_containment_top"][:3]) + ".")
            HC["clean"] = (not HC["upstream_nonempty_blobs_in_history"] and hn[0.5] == 0
                           and not HC["identical_bodies_ge3"])
            P("  Reading: " + ("no upstream blob, identical body or near-copy at Jaccard >= 0.5 "
                               "in any commit, so the HEAD reading holds for the whole history."
                               if HC["clean"] else
                               "**the history check finds upstream material; see the rows "
                               "above (the HEAD reading does not cover history).**"))
            P("")
    else:
        P("- `jlens-qwen36/` is not present on this machine: copy check not run.")
        P("")

    # =====================================================================
    # 2d. Jacobian lenses (untracked third-party instruments)
    # =====================================================================
    def loc_of(f: str, needle: str, src: str | None = None, at: str | None = None) -> list[str]:
        # record locators: found by content in the file at LOC (the block's commit)
        t = loc_src(f) if src is None else src
        return [f"{f}@{(at or LOC)[:7]}:{i}" for i in find_line(t, needle)]

    P("### 2d. Jacobian lenses for Qwen3.6-27B (untracked third-party instruments)")
    P("")
    LN: dict = {}
    lens_needles = {
        "release_lens_v02": ("archive/RESULTS-cycle1-2.md", "the repo's bundled `v0.2-fulldepth`"),
        "release_download": ("archive/RESULTS-cycle1-2.md", "downloaded via `gh release download`"),
        "neuronpedia_lens": ("archive/RESULTS-cycle1-2.md", "Neuronpedia's n=1000 lens"),
        "mit_and_credit": ("archive/RESULTS-cycle1-2.md", "MIT-licensed, credit"),
        "primary_cycles12": ("archive/RESULTS-cycle1-2.md", "Used as the primary lens for"),
        "setup_v01_demo": ("archive/CLAUDE-cycle1-2.md", "gh release download v0.1-demo"),
        "primary_cycles34": ("archive/CLAUDE-v2-cycles3-4.md", "`neuronpedia_n1000.npz` (primary)"),
        "jlens_monitor_phase2": ("CLAUDE.md", "J-lens eval-awareness monitor is Qwen-specific"),
    }
    LN["record_locators"] = {k: loc_of(f, s) for k, (f, s) in lens_needles.items()}
    if J.get("present") and UP.get("ok"):
        LN["upstream_docs_hf_source"] = loc_of(
            "jlens-qwen36/docs/lenses.md", "hf_hub_download('neuronpedia/jacobian-lens'",
            src=up_src.get("docs/lenses.md", b"").decode("utf-8", "replace"),
            at=JLENS_CLONE_COMMIT)
    lens_dir = os.path.join(CLONE, "data", "lens")
    LN["on_disk"] = {}
    for fn in ("lens.npz", "neuronpedia_n1000.npz", "neuronpedia_n1000.json"):
        fp = os.path.join(lens_dir, fn)
        LN["on_disk"][fn] = os.path.getsize(fp) if os.path.isfile(fp) else None
    sidecar = os.path.join(lens_dir, "neuronpedia_n1000.json")
    LN["sidecar_n_prompts"] = (json.load(open(sidecar)).get("n_prompts")
                               if os.path.isfile(sidecar) else None)
    rel = WEB_READS["wezzard_releases"]["result"]
    v02_sum = sum(rel["v0.2-fulldepth"]["assets"].values())
    v01_size = sum(rel["v0.1-demo"]["assets"].values())
    v03_sum = sum(WEB_READS["wezzard_releases_v03_parts_checker_read"]["result"]
                  ["v0.3-qwen38-n1000_parts"])
    LN["v02_parts_sum"] = v02_sum
    LN["v03_parts_sum_checker_read"] = v03_sum
    LN["lens_npz_equals_v02_parts_sum"] = LN["on_disk"]["lens.npz"] == v02_sum
    LN["lens_npz_equals_v01_asset"] = LN["on_disk"]["lens.npz"] == v01_size
    LN["lens_npz_equals_v03_parts_sum"] = LN["on_disk"]["lens.npz"] == v03_sum
    LN["layout"] = {}
    for fn in ("lens.npz", "neuronpedia_n1000.npz"):
        fp = os.path.join(lens_dir, fn)
        try:
            LN["layout"][fn] = npz_layout(fp) if os.path.isfile(fp) else None
        except Exception as ex:  # reported, not fatal
            LN["layout"][fn] = {"error": f"{type(ex).__name__}: {ex}"}
    lay_a, lay_b = LN["layout"].get("lens.npz"), LN["layout"].get("neuronpedia_n1000.npz")
    LN["same_layout"] = bool(lay_a and lay_b and "kinds" in lay_a and "kinds" in lay_b
                             and lay_a["kinds"] == lay_b["kinds"])
    LN["release_locators"] = (
        loc_of("archive/RESULTS-cycle1-2.md", "the repo's bundled `v0.2-fulldepth`")
        + loc_of("archive/RESULTS-cycle1-2.md", "release (20 prompts, all 63 layers)")
        + loc_of("results/raw/2026-07-16_four_experiments_n20lens.txt",
                 "data/lens/lens.npz (v0.2-fulldepth, n_prompts=20"))
    RX_LENSPATH = re.compile(r"(^|/)data/lens/|\.pt$|(lens|neuronpedia)[^/]*\.npz$", re.I)
    LN["lens_paths_any_commit"] = [p for p in hist_paths if RX_LENSPATH.search(p)]
    LN["head_files_naming_neuronpedia"] = sorted(p for p, t in text.items()
                                                 if re.search("neuronpedia", t, re.I))
    np_hf = WEB_READS["neuronpedia_lens_hf"]["result"]
    R["lenses"] = LN
    rl = LN["record_locators"]

    def L1(k):
        return ", ".join(f"`{x}`" for x in rl.get(k, [])) or "[not found at the commit]"
    P(f"- **What the record says.** Two lenses were acquired on 2026-07-16 into the clone's "
      f"`data/lens/`: the jlens-qwen36 `v0.2-fulldepth` release lens, \"downloaded via `gh "
      f"release download`\" ({L1('release_lens_v02')}, {L1('release_download')}), and "
      f"Neuronpedia's n=1000 lens ({L1('neuronpedia_lens')}), recorded as MIT-licensed with a "
      f"credit line ({L1('mit_and_credit')}) and used as the primary lens from then on "
      f"({L1('primary_cycles12')}; through cycles 3-4: {L1('primary_cycles34')}). The setup doc "
      f"also names the earlier `v0.1-demo` release ({L1('setup_v01_demo')}). Phase 2's CLAUDE.md "
      f"keeps the J-lens monitor as a Qwen-only instrument ({L1('jlens_monitor_phase2')}).")
    if "upstream_docs_hf_source" in LN:
        P(f"- **Source of the n=1000 lens:** the upstream jlens-qwen36 `docs/lenses.md` names the "
          f"Hugging Face file and the conversion recipe "
          f"({', '.join(f'`{x}`' for x in LN['upstream_docs_hf_source']) or '[not found]'}, read "
          f"from the clone's object store). **[recorded WebFetch read]** "
          f"`{WEB_READS['neuronpedia_lens_hf']['url']}` -> license `{np_hf['cardData_license']}`, "
          f"gated {np_hf['gated']}, sha `{np_hf['sha'][:12]}...`, lastModified "
          f"{np_hf['lastModified'][:10]} (after the 2026-07-16 acquisition, so the sha read now "
          f"need not be the one downloaded; the record pins none); its Qwen3.6-27B folder holds the "
          f"`.pt` and a {WEB_READS['neuronpedia_lens_credit_md']['result']['length_chars']}-character "
          f"`CREDIT.md` crediting the lens's author at Anthropic Interpretability (the record's own "
          f"credit line is cited above; the name is not reproduced here).")
    def lay_s(l):
        if not l or "kinds" not in l:
            return str(l)
        return (f"{l['n_members']} members ({', '.join(f'{v} x {k}' for k, v in l['kinds'].items())}), "
                f"{l['n_compressed']} compressed, int scalars {l['int_scalars']}")
    P(f"- **On disk (local facts):** `jlens-qwen36/data/lens/lens.npz` {LN['on_disk']['lens.npz']} "
      f"bytes, `neuronpedia_n1000.npz` {LN['on_disk']['neuronpedia_n1000.npz']} bytes, sidecar "
      f"`neuronpedia_n1000.json` n_prompts = {LN['sidecar_n_prompts']}. Zip directories and "
      f"`.npy` headers (no array data read): `lens.npz` {lay_s(lay_a)}; `neuronpedia_n1000.npz` "
      f"{lay_s(lay_b)}; same member layout: {LN['same_layout']}. **[recorded WebFetch read]** "
      f"`{WEB_READS['wezzard_releases']['url']}`: `v0.2-fulldepth`'s two parts sum to {v02_sum} "
      f"bytes; equal to `lens.npz`: {LN['lens_npz_equals_v02_parts_sum']} (equal to the "
      f"`v0.1-demo` asset, {v01_size} bytes: {LN['lens_npz_equals_v01_asset']}; the round-2 "
      f"checker's read of the same API gives the `v0.3-qwen38-n1000` parts summing to {v03_sum}, "
      f"equal: {LN['lens_npz_equals_v03_parts_sum']}). **The size does not identify the lens.** "
      f"Any lens saved with this member layout (63 float16 5120 x 5120 arrays and two scalars, "
      f"stored uncompressed, same member names) has this size: the two local files are different "
      f"lenses (n_prompts differ) of the same size, and the v0.3 asset's parts sum to it too. "
      f"The identification of `lens.npz` as the "
      f"`v0.2-fulldepth` release lens rests on the record "
      f"({', '.join(f'`{x}`' for x in LN['release_locators']) or '[not found]'}), and is "
      f"consistent with the file's own `n_prompts` member "
      f"({(lay_a or {}).get('int_scalars', {}).get('n_prompts.npy')}) and the v0.2 asset's name "
      f"(20 prompts, 63 layers). The release bodies state no license; the repository's "
      f"Apache-2.0 is the only licence in view for the release assets [to confirm by the PI if "
      f"the README is to say so].")
    P(f"- **Tracked?** Paths matching `data/lens/`, `*.pt` or a lens-named `.npz` in any of the "
      f"{HI['n_commits']} commits: **{len(LN['lens_paths_any_commit'])}**"
      + (f" ({LN['lens_paths_any_commit']})" if LN["lens_paths_any_commit"] else "")
      + f". Nothing of either lens is redistributed; tracked files naming Neuronpedia at HEAD: "
      f"{len(LN['head_files_naming_neuronpedia'])} (" + ", ".join(
          f"`{p}`" for p in LN["head_files_naming_neuronpedia"]) + "). Not a release blocker; the "
      f"README's licenses section should credit the lens (block section 6 item 7).")
    P("")

    # =====================================================================
    # 2e. Other third-party items the record names
    # =====================================================================
    P("### 2e. Other third-party items the record names")
    P("")
    OT: dict = {}
    OT["anthropic_upstream_locators"] = (
        loc_of("archive/CLAUDE-cycle1-2.md", "the original `anthropics/jacobian-lens` repo")
        + loc_of("archive/CLAUDE-cycle1-2.md", "community MLX port of Anthropic's `jlens` reference"))
    aj = WEB_READS["anthropic_jacobian_lens_api"]
    P(f"- **anthropics/jacobian-lens, the upstream of jlens-qwen36.** The record calls jlens-qwen36 "
      f"\"a community MLX port of Anthropic's `jlens` reference implementation\" and names "
      f"`anthropics/jacobian-lens` ({', '.join(f'`{x}`' for x in OT['anthropic_upstream_locators'])}). "
      f"**[recorded WebFetch read]** `{aj['url']}` -> license `{aj['result']['license']['spdx_id']}`. "
      f"Its code was not downloaded or compared; none of jlens-qwen36's upstream blobs is in any "
      f"commit (section 2c), and nothing is tracked under either name.")
    # the Global Workspace paper: the J-lens program's founding citation
    GW: dict = {}
    GW["setup_doc_locators"] = loc_of("archive/CLAUDE-cycle1-2.md",
                                      "transformer-circuits.pub/2026/workspace")
    # the README refers to the work in a sentence that wraps; report the line range, and
    # whether the README gives the title or a link (round 3: it gives neither)
    readme_loc = loc_src("README.md")
    rm_lines = readme_loc.splitlines()
    GW["readme_locators"] = [
        f"README.md@{LOC[:7]}:{i}" + (f"-{i + 1}" if i < len(rm_lines) and
                                       "interpretability work" in rm_lines[i] else "")
        for i in find_line(readme_loc, "global-workspace")]
    GW["readme_gives_title"] = "Verbalizable Representations" in readme_loc
    GW["readme_gives_link"] = any(u in readme_loc for u in (
        "transformer-circuits.pub/2026/workspace", "anthropic.com/research/global-workspace"))
    GW["locators"] = GW["setup_doc_locators"] + GW["readme_locators"]
    up_re = (up_src.get("scripts/run_experiments.py", b"").decode("utf-8", "replace")
             if J.get("present") and UP.get("ok") else "")
    GW["upstream_run_experiments_read"] = bool(up_re)
    GW["upstream_docstring_says_paper"] = up_re.lstrip().startswith('"""Run the paper')
    GW["upstream_paper_fig_labels"] = sorted(set(re.findall(r"\(paper (Fig [0-9-]+)\)", up_re)))
    GW["run_experiments_locally_edited"] = ("scripts/run_experiments.py" in
                                           UP.get("on_disk_differs_from_index", []))
    re_disk_fp = os.path.join(CLONE, "scripts", "run_experiments.py")
    re_disk = (open(re_disk_fp, encoding="utf-8", errors="replace").read()
               if os.path.isfile(re_disk_fp) else "")
    GW["on_disk_paper_fig_labels"] = sorted(set(re.findall(r"\(paper (Fig [0-9-]+)\)", re_disk)))
    GW["fig_labels_only_in_local_edit"] = sorted(set(GW["on_disk_paper_fig_labels"])
                                                 - set(GW["upstream_paper_fig_labels"]))
    GW["verbal_report_added_locator"] = loc_of(
        "results/raw/2026-07-17_full_suite_with_verbal_report.txt",
        "experiment_verbal_report (added to run_experiments.py)")
    cyc_raws = []
    for p in sorted(text):
        if not p.startswith("results/raw/2026-07-"):
            continue
        first = text[p].splitlines()[0] if text[p] else ""
        m_ = re.match(r"Command:.*?\bscripts/(\w+\.py)", first)
        if m_:
            sp = f"scripts/{m_.group(1)}"
            cls_ = ("upstream" if sp in JLENS_UPSTREAM_BLOBS else
                    "lab-added" if sp in clone_files_rel else "not in the clone")
            cyc_raws.append({"raw": p, "script": sp, "class": cls_})
    GW["cycle1_raws_by_command"] = cyc_raws
    gw_up = [r["raw"] for r in cyc_raws if r["class"] == "upstream"]
    da = text.get("results/raw/2026-07-16_debug_ablation.txt", "").splitlines()
    da_prompt = next((l.split("Prompt: ", 1)[1].strip("'") for l in da if l.startswith("Prompt: ")), None)
    GW["debug_ablation_prompt_in_upstream_run_experiments"] = bool(da_prompt and da_prompt in up_re)
    OT["global_workspace"] = GW
    P(f"- **Anthropic, *Verbalizable Representations Form a Global Workspace in Language Models* "
      f"(July 2026): the J-lens program's founding citation.** The cycle-1-2 setup doc cites it with "
      f"its title and its blog and paper URLs (`www.anthropic.com/research/global-workspace`, "
      f"`transformer-circuits.pub/2026/workspace/index.html`; "
      f"{', '.join(f'`{x}`' for x in GW['setup_doc_locators']) or '[not found]'}), and the "
      f"README refers to it as Anthropic's \"J-lens / global-workspace interpretability work (July 2026)\" "
      f"({', '.join(f'`{x}`' for x in GW['readme_locators']) or '[not found]'}) without its title "
      f"(title in the README: {GW['readme_gives_title']}) or a link (either URL in the README: "
      f"{GW['readme_gives_link']}), so the README-for-readers carries the full citation. The "
      f"cycle-1 raws whose "
      f"first line runs an upstream script: {len(gw_up)} ("
      + ", ".join(f"`{x}`" for x in gw_up) + "); upstream scripts they name: "
      + str(sorted({r['script'] for r in cyc_raws if r['class'] == 'upstream'}))
      + f". The committed upstream `scripts/run_experiments.py` (object store) opens \"Run the paper's J-space experiments\": "
      f"{GW['upstream_docstring_says_paper']} and labels its experiments with the paper's figures "
      f"{GW['upstream_paper_fig_labels']} (the clone's copy is locally edited: "
      f"{GW['run_experiments_locally_edited']}; labels only in the local edit: "
      f"{GW['fig_labels_only_in_local_edit']}, the verbal-report experiment the lab added: "
      f"{', '.join(f'`{x}`' for x in GW['verbal_report_added_locator']) or '[not found]'}). Raws of lab-added clone scripts from the same "
      f"period: {sum(1 for r in cyc_raws if r['class'] == 'lab-added')}; "
      f"`results/raw/2026-07-16_debug_ablation.txt` (lab-added `scripts/debug_ablation.py`) "
      f"reuses the upstream script's one-line prompt: "
      f"{GW['debug_ablation_prompt_in_upstream_run_experiments']}. So what the record carries "
      f"from this line of work is outputs of an Apache-2.0 upstream script run on the lab's "
      f"machine, with that script's one-line prompts (de minimis). This part did not read the "
      f"paper or compare the record with it, so its license and whether any prompt is the "
      f"paper's own wording are **[not read; to confirm]**. A README citation is the action "
      f"(section 6).")
    if J.get("present") and UP.get("ok"):
        OT["c4_loader"] = loc_of("jlens-qwen36/jlens_qwen/prompts.py", 'load_dataset("allenai/c4", "en"',
                                 src=up_src.get("jlens_qwen/prompts.py", b"").decode(),
                                 at=JLENS_CLONE_COMMIT)
    OT["c4_record"] = loc_of("archive/RESULTS-cycle1-2.md", "fell back to c4")
    c4raw = "results/raw/2026-07-19_basis_sensitivity_diagnostic.txt"
    OT["c4_raw"] = {"path": c4raw, "bytes": len(text.get(c4raw, "").encode()),
                    "says_loading_c4": "Loading c4" in text.get(c4raw, "")}
    c4 = WEB_READS["c4_dataset_hf"]["result"]
    P(f"- **C4, once, as a fallback corpus.** The cycle-1-2 basis-sensitivity diagnostic's "
      f"residual corpus fell back to c4 when WikiText-103 failed to load "
      f"({', '.join(f'`{x}`' for x in OT['c4_record']) or '[not found]'}), through the upstream "
      f"loader ({', '.join(f'`{x}`' for x in OT.get('c4_loader', [])) or '[not read]'}: "
      f"`allenai/c4`, config `en`, streamed). **[recorded WebFetch read]** "
      f"`{WEB_READS['c4_dataset_hf']['url']}` -> license {c4['cardData_license']}. Its raw "
      f"`{c4raw}` ({OT['c4_raw']['bytes']} bytes; says \"Loading c4\": "
      f"{OT['c4_raw']['says_loading_c4']}) holds load messages and rating statistics, no C4 text "
      f"(Code's read of the whole file). Nothing redistributed; a README line is optional.")
    OT["demo_prompt_locator"] = loc_of("archive/CLAUDE-cycle1-2.md", "borrowed from the `jlens-qwen36` demo")
    OT["demo_prompt_tracked_files"] = sorted(p for p, t in text.items()
                                             if "void main(void) { return 1; }" in t)
    P(f"- **De minimis:** the cycle-1-2 setup doc records one C one-liner prompt \"borrowed from "
      f"the `jlens-qwen36` demo\" ({', '.join(f'`{x}`' for x in OT['demo_prompt_locator'])}; "
      f"Apache-2.0 upstream). The string occurs in {len(OT['demo_prompt_tracked_files'])} tracked "
      f"file(s): {', '.join(f'`{p}`' for p in OT['demo_prompt_tracked_files']) or 'none'}.")
    # runtime libraries: third-party top-level imports in tracked code
    std = set(sys.stdlib_module_names) | {"__future__"}
    local_mods = {"valence_core", "jlens_qwen", "scripts"} | {
        os.path.splitext(os.path.basename(p))[0] for p in by_path if p.endswith(".py")} | {
        p.split("/")[0] for p in by_path if "/" in p}
    ext_mods: dict[str, set] = defaultdict(set)
    for p, s in text.items():
        if not p.endswith((".py", ".ipynb")):
            continue
        src = ipynb_code(s.encode()) if p.endswith(".ipynb") else s
        try:
            tr = ast.parse(src)
        except SyntaxError:
            continue
        for n in ast.walk(tr):
            names = []
            if isinstance(n, ast.Import):
                names = [a.name for a in n.names]
            elif isinstance(n, ast.ImportFrom) and n.level == 0 and n.module:
                names = [n.module]
            for nm in names:
                top = nm.split(".")[0]
                if top not in std and top not in local_mods:
                    ext_mods[top].add(p)
    RX_MANIFEST = re.compile(r"(^|/)(requirements[^/]*\.txt|pyproject\.toml|setup\.py|setup\.cfg|"
                             r"environment\.ya?ml|Pipfile(\.lock)?|uv\.lock|poetry\.lock)$")
    OT["dependency_manifests_at_head"] = [p for p in by_path if RX_MANIFEST.search(p)]
    OT["dependency_manifests_any_commit"] = [p for p in hist_paths if RX_MANIFEST.search(p)]
    OT["vendored_paths"] = [p for p in hist_paths
                            if "site-packages/" in p or p.split("/")[0] in ext_mods]
    OT["third_party_imports"] = {k: len(v) for k, v in sorted(ext_mods.items())}
    P(f"- **Runtime libraries.** Third-party top-level modules imported by tracked code (AST over "
      f"`.py` and notebook cells; stdlib and the repo's own modules excluded): "
      + ", ".join(f"`{k}` ({n} files)" for k, n in OT["third_party_imports"].items())
      + f". Dependency manifests (requirements/pyproject/setup/environment/Pipfile/lock files): "
      f"{len(OT['dependency_manifests_at_head'])} at HEAD, {len(OT['dependency_manifests_any_commit'])} "
      f"in any commit; vendored copies (a path under `site-packages/` or a top-level directory "
      f"named after one of these modules, any commit): {len(OT['vendored_paths'])}. None is "
      f"redistributed; their licenses were not read by this part (optional README content).")
    P("")
    R["other_third_party"] = OT

    # =====================================================================
    # 2f. External-reference sweep (what grounds "every material" below)
    # =====================================================================
    P("### 2f. External-reference sweep, HEAD and history")
    P("")
    RX_URL = re.compile(r"(?:github\.com|huggingface\.co)/(?:datasets/)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]*)")
    RX_HUB = re.compile(r"(?<![\w/.-])((?:neuronpedia|anthropics|allenai|Qwen|mlx-community|"
                        r"safety-research|WeZZard|meta-llama|mistralai|EleutherAI|openai|"
                        r"microsoft|HuggingFaceH4|Salesforce)/[A-Za-z0-9][A-Za-z0-9._-]*)")
    RX_QID = re.compile(r"[`\"']([A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9._-]*)[`\"']")
    RX_FAMILY = re.compile(r"qwen|olmo|llama|gpt|mistral|gemma|sae|lens|c4|wikitext", re.I)
    RX_FILELIKE = re.compile(r"\.(py|json|jsonl|toml|md|txt|npz|log|sh|ipynb|yaml|yml|csv|png|svg)$")
    RX_ARXIV = re.compile(r"arXiv:? ?(\d{4}\.\d{4,5})|arxiv\.org/abs/(\d{4}\.\d{4,5})", re.I)
    path_parts = {c for p in hist_paths for c in p.split("/")} | {"jlens-qwen36"}

    def ids_in(t: str) -> set:
        out = set()
        for m in RX_URL.finditer(t):
            v = re.sub(r"(\.git)?[.)\],;:]*$", "", m.group(1))
            if "/" in v and v.split("/")[1]:
                out.add(("repo", v))
            elif "/" in v:
                out.add(("repo", v))
        for m in RX_HUB.finditer(t):
            out.add(("repo", re.sub(r"[.)\],;:]+$", "", m.group(1))))
        for m in RX_QID.finditer(t):
            v = m.group(1)
            if (RX_FAMILY.search(v) and not RX_FILELIKE.search(v)
                    and v.split("/")[0] not in path_parts):
                out.add(("repo", v))
        for m in RX_ARXIV.finditer(t):
            out.add(("arxiv", m.group(1) or m.group(2)))
        return out

    def id_lines(t: str, k: tuple) -> list[int]:
        # the first line on which ids_in() extracts id k (the patterns never span lines)
        for i, l in enumerate(t.splitlines(), 1):
            if k in ids_in(l):
                return [i]
        return []
    FL_STATS: dict = defaultdict(int)
    FL_OLD: dict = {}      # id sha256 -> the substring lookup's locator at the commit read
    SW_BY_SHA: dict = {}   # id sha256 -> its row (so ids printed redacted are never keys)
    CLASS = {
        "safety-research/introspection-mechanisms": "row: Macar et al. materials",
        "safety-research/introspection-": "row: Macar et al. (the same repository, a line-wrapped mention)",
        "WeZZard/jlens-qwen36": "row: jlens-qwen36 (and its release lenses)",
        "jasondwyer/jspace-lab": "this repository",
        "arvomm/cacophony-public-code": ("external code that block item N19 (Tier 2) will pin and run; "
                                         "not a material of the record"),
        "mlx-community/Qwen3.6-27B-4bit": "row: Qwen",
        "Qwen/Qwen3.6-27B": "row: Qwen (base model)",
        "allenai/Olmo-3-1125-32B": "row: OLMo", "allenai/Olmo-3.1-32B-Instruct-SFT": "row: OLMo",
        "allenai/Olmo-3.1-32B-Instruct-DPO": "row: OLMo", "allenai/Olmo-3.1-32B-Instruct": "row: OLMo",
        "neuronpedia/jacobian-lens": "row: Jacobian lenses",
        "anthropics/jacobian-lens": "row: jlens-qwen36 (its upstream)",
        "allenai/c4": "row: C4",
        "Qwen/MLX": "prose (\"the Qwen/MLX oracle\"), not a hub id",
        "Qwen/OLMo": "prose (\"Qwen/OLMo G-F0m stage\"), not a hub id",
        "Qwen/F3": "prose (\"Qwen/F3 only\"), not a hub id",
    }
    CLASS_BY_SHA = {
        "fa35e0261838e4638214d5d40a61c738e6f76e8e076226bb8ea77558b12dedfa": (
            "a third-party Qwen3.6-27B SAE that the record's SAE inventory surveyed and did not "
            "acquire or use (id printed redacted); no row"),
    }
    ARXIV_ROWS = {"2603.21396": ("row: Macar et al. (the paper; CC BY 4.0, the licensed source "
                                 "for the prompt text, which appeared earlier, with no license "
                                 "stated, on the Lindsey (2025) page; section 1)")}
    head_ids: dict = defaultdict(list)
    for p, t in text.items():
        for k in ids_in(t):
            head_ids[k].append(p)
    hist_ids: dict = defaultdict(list)
    for b, t in hist_text.items():
        for k in ids_in(t):
            hist_ids[k].append(b)
    # Round 9 (Code's rule changes; the PI confirmed them on 2026-10-12, "Yes to all five; tag it", question 2): ids the sweep extracts from
    # this audit's own files once they are tracked. Two explicit entries and two mechanical rules (fragments of the
    # recorded-read URLs; prefixes of this repository's id); every other id still needs a class.
    R9_IDS: dict = {}     # id key -> the round-9 rule that classified it (only where the earlier rules did not)
    R9_HOSTS: dict = {}   # host key -> the round-9 rule (H1-H4) that classified it
    CLASS_R9 = {
        "allenai/": ("the owner prefix of the brace list `huggingface.co/allenai/{...}` in this part's OLMo row "
                     "(each id the list expands to is classified: row: OLMo)"),
        "jasondwyer/jspace-lab.wiki": ("this repository's wiki (the pre-flip raw's `git ls-remote` probe; not "
                                       "found); not a material"),
    }
    WR_IDS = ids_in(json.dumps(WEB_READS))   # the ids the URL patterns parse out of this part's recorded reads
    THIS_REPO = "jasondwyer/jspace-lab"
    THIS_OWNER = THIS_REPO.split("/")[0] + "/"
    WR_URLS: list = []

    def _wr_urls(o):
        if isinstance(o, dict):
            for v_ in o.values():
                _wr_urls(v_)
        elif isinstance(o, (list, tuple)):
            for v_ in o:
                _wr_urls(v_)
        elif isinstance(o, str) and re.match(r"https?://", o):
            WR_URLS.append(o)
    _wr_urls(WEB_READS)
    WR_URLS = sorted(set(WR_URLS))

    def audit_only(carriers) -> bool:
        # release (L3): every carrier is one of this audit's own files (RX_AUDIT_FILE)
        return bool(carriers) and all(RX_AUDIT_FILE.match(c) for c in carriers)

    def wr_fragment(v: str) -> str | None:
        # release (L3): the recorded-read URL (WEB_READS) of which v is a path fragment, starting at a '/' of it
        for u_ in WR_URLS:
            if ("/" + v) in u_:
                return u_
        return None

    def id_class(k: tuple, carriers=None) -> str:
        kind, v = k
        if kind == "arxiv":
            return ARXIV_ROWS.get(v, "cited paper; not a material row (this part did not search "
                                     "the record for passages quoted from it)")
        c_ = CLASS.get(v) or CLASS_BY_SHA.get(sha256(v.encode()))
        if c_:
            return c_
        if CLASS_R9.get(v):
            R9_IDS[k] = "id entry (CLASS_R9)"
            return CLASS_R9[v]
        if kind == "repo" and k in WR_IDS:
            R9_IDS[k] = "id rule: a fragment of a recorded-read URL (WEB_READS)"
            return ("a path fragment of a URL this part read (WEB_READS), which the URL pattern parses as an "
                    "id; not a repository (the repository read is classified in its own row)")
        # release (L3): the same rule, as worded ("fragments of recorded-read URLs"), for an id that only this audit's
        # own files carry and that is a fragment of a recorded-read URL cut short by an excerpt window (e.g. a
        # 40-character excerpt of the content screen ending inside `.../repos/WeZZard/jlens-qwen36`)
        if kind == "repo" and audit_only(carriers) and wr_fragment(v):
            R9_IDS[k] = "id rule: a fragment of a recorded-read URL (WEB_READS), cut short in this audit's own files"
            return ("a fragment of a URL this part read (WEB_READS), cut short by an excerpt window in this audit's "
                    "own files, which the URL pattern parses as an id; not a repository (the repository read is "
                    "classified in its own row)")
        if kind == "repo" and THIS_REPO.startswith(v) and len(v) > len(THIS_OWNER):
            R9_IDS[k] = "id rule: a prefix of this repository's id"
            return "this repository (its URL cut short by an excerpt window); not a material"
        # release (L3 fix round): the owner part alone (`jasondwyer/`) is NOT classed -- the confirmed rule's guard
        # (`len(v) > len(THIS_OWNER)`) excludes it, as round 9 wrote it; it goes to the PI below
        if audit_only(carriers):
            return ("UNCLASSIFIED (for the PI: carried only by this audit's own files, and no confirmed rule covers "
                    "it -- not a fragment of this part's recorded-read URLs (WEB_READS), not a prefix of this "
                    "repository's id longer than its owner part)")
        return "UNCLASSIFIED (Code to review)"
    SW = []
    for k in sorted(set(head_ids) | set(hist_ids)):
        kind, v = k
        hs = sha256(v.encode())
        id_carriers = set(head_ids.get(k, [])) | {c_ for b_ in hist_ids.get(k, []) for c_ in hist_blob_paths[b_]}
        cls = id_class(k, id_carriers)
        shown = redform(v) if (kind == "repo" and v not in CLASS) else v
        if shown != v:
            REDACTED_IDS.append({"where": "section 2f, external-reference sweep",
                                 "category": "third-party repository id (no attribution row)",
                                 "redacted": shown})
        # First locator (round 4): the alphabetically first HEAD file carrying the id, with
        # the line found by content -- the first line on which ids_in() itself extracts this
        # id, so a longer id containing it (`...-Instruct-SFT` for `...-Instruct`) does not
        # count -- in the file at LOC (bbc9ffe, the common pin), printed `file@bbc9ffe:N`;
        # where the file at LOC lacks the id, the commit read is printed explicitly,
        # `file@<head>:N`. A history-only id keeps `commit:path` (no line).
        first = sorted(head_ids[k])[0] if head_ids.get(k) else hloc(sorted(hist_ids[k])[0])
        loc_pinned, loc_head = first, first
        if head_ids.get(k):
            ln_h = id_lines(text[first], k)
            ln_p = id_lines(loc_src(first), k)
            loc_head = f"{first}:{ln_h[0]}" if ln_h else first
            loc_pinned = (f"{first}@{LOC[:7]}:{ln_p[0]}" if ln_p else
                          f"{first}@{head[:7]}:{ln_h[0]}" if ln_h else f"{first}@{head[:7]}")
            FL_STATS["pinned_at_loc" if ln_p else "at_commit_read"] += 1
            FL_STATS["line_moved"] += bool(ln_p and ln_h and ln_p[0] != ln_h[0])
            old_ln = find_line(text[first], v)[:1]  # the pre-round-4 substring lookup
            FL_OLD[hs] = f"{first}:{old_ln[0]}" if old_ln else first
            FL_STATS["substring_line_differed"] += bool(ln_h and old_ln != ln_h[:1])
        SW.append({"kind": kind, "id": shown, "head_files": len(set(head_ids.get(k, []))),
                   "history_blobs": len(set(hist_ids.get(k, []))),
                   "history_only": not head_ids.get(k), "first_locator": loc_pinned,
                   "first_locator_at_commit_read": loc_head,
                   "class": cls})
        SW_BY_SHA[hs] = SW[-1]
    R["external_reference_sweep"] = SW
    R["external_reference_sweep_first_locators"] = dict(FL_STATS)
    n_uncl = sum(1 for s in SW if s["class"].startswith("UNCLASSIFIED"))
    n_hist_only = sum(1 for s in SW if s["history_only"])
    P(f"Patterns (HEAD text files and all {HI['n_distinct_text_blobs_scanned']} distinct historical "
      f"text blobs): `github.com/`, `huggingface.co/` repository URLs; hub ids under known "
      f"model/dataset owners; quoted `owner/name` ids carrying a model-family token (file paths "
      f"and repo directories excluded); arXiv ids. Distinct ids: **{len(SW)}**; only in history "
      f"(not at HEAD): **{n_hist_only}**; unclassified: **{n_uncl}**. Repository ids without an "
      f"attribution row are printed redacted. First locator: the alphabetically first HEAD file "
      f"carrying the id, at the first line on which the scan itself extracts the id (a longer id "
      f"containing it does not count), found by content in that file at `{LOC[:7]}` and printed "
      f"`file@{LOC[:7]}:N` ({FL_STATS['pinned_at_loc']} of {len(SW) - n_hist_only}; the line "
      f"differs from the commit read's in {FL_STATS['line_moved']}); where the file at "
      f"`{LOC[:7]}` lacks the id, printed at the commit read, `file@{head[:7]}:N` "
      f"({FL_STATS['at_commit_read']}); a history-only id is located `commit:path`. The JSON's "
      f"`first_locator_at_commit_read` gives each line at `{head[:7]}`.")
    P("")
    P("| kind | id | HEAD files | history blobs | history only | first locator | class |")
    P("|---|---|---|---|---|---|---|")
    for s in SW:
        P(f"| {s['kind']} | `{s['id']}` | {s['head_files']} | {s['history_blobs']} | "
          f"{s['history_only']} | `{s['first_locator']}` | {s['class']} |")
    P("")
    # ---- host-agnostic URL sweep: every URL host and bare domain, HEAD and history ----
    RX_URLHOST = re.compile(r"https?://([^/\s\"'`<>)\]\\]+)")
    TLDS = "com|org|net|io|ai|pub|blog|dev|co|edu|gov|app|info|me|uk|de"
    RX_BAREHOST = re.compile(rf"(?<![\w@./:-])((?:[A-Za-z0-9-]+\.)+(?:{TLDS}))\b"
                             rf"(?![.\w-]*\.(?:py|json|jsonl|md|txt|npz))")
    RX_HOSTPATH = re.compile(rf"(?:https?://)?((?:[A-Za-z0-9-]+\.)+(?:{TLDS}))(/[^\s)\]\"'`>,\\]*)?")

    def hosts_in(t: str) -> dict:
        out: dict = defaultdict(set)
        for m in RX_URLHOST.finditer(t):
            h = m.group(1).split("@")[-1].split(":")[0].lower()
            if re.fullmatch(r"[\d.]+", h):
                out[("ip", h)].add("")
            elif "." in h:
                out[("host", h)]
            elif h:
                # a URL host with no dot (round 3): counted, classed by carrier path
                out[("dotless", h)]
        for m in RX_BAREHOST.finditer(t):
            out[("host", m.group(1).lower())]
        for m in RX_HOSTPATH.finditer(t):
            k = ("host", m.group(1).lower())
            if k in out:
                out[k].add(m.group(2) or "")
        return out
    MODEL_OUT_HOSTS = {"www.constellations.blog", "simple.wikipedia.org", "artworks.org",
                       "of.nothing.com"}
    GW_PATHS = {"transformer-circuits.pub": "/2026/workspace", "www.anthropic.com":
                "/research/global-workspace", "anthropic.com": "/research/global-workspace"}
    h_head: dict = defaultdict(set)
    h_paths: dict = defaultdict(set)
    # release (L3): the URL paths each carrier itself carries (HEAD file, or every path of a historical blob), so a
    # document's allowed paths are checked against that document's own paths, not against another carrier's
    h_cpaths: dict = defaultdict(lambda: defaultdict(set))
    for p, t in text.items():
        for k, paths in hosts_in(t).items():
            h_head[k].add(p)
            h_paths[k] |= paths
            h_cpaths[k][p] |= paths
    h_hist: dict = defaultdict(set)
    h_hist_paths: dict = defaultdict(set)
    for b, t in hist_text.items():
        for k, paths in hosts_in(t).items():
            h_hist[k].add(b)
            h_hist_paths[k] |= set(hist_blob_paths[b])
            h_paths[k] |= paths
            for c_ in hist_blob_paths[b]:
                h_cpaths[k][c_] |= paths
    RX_CLAUDE_LINK = re.compile(r"claude\.ai/", re.I)
    claude_links = (sum(1 for t in text.values() if RX_CLAUDE_LINK.search(t))
                    + sum(1 for t in hist_text.values() if RX_CLAUDE_LINK.search(t)))
    # Round 9 (Code; the PI confirmed them on 2026-10-12, "Yes to all five; tag it", question 2): this audit's own files -- its scripts and its raws -- as carriers. A host or link
    # that only they carry is named by the audit's scanner tables, fixtures and recorded reads, not by the record.
    # Release (L3): the audit-file rule is the module-level RX_AUDIT_FILE (every results/raw/*_note-* raw, any date,
    # and every scripts/audit_note_*.py).
    claude_links_outside_audit = (
        sum(1 for p_, t in text.items() if RX_CLAUDE_LINK.search(t) and not RX_AUDIT_FILE.match(p_))
        + sum(1 for b, t in hist_text.items() if RX_CLAUDE_LINK.search(t)
              and not all(RX_AUDIT_FILE.match(p_) for p_ in hist_blob_paths[b])))
    AUDIT_HOSTS = {   # host -> what this audit's own files use it for
        "%s": "a printf placeholder in a synthetic URL of the content script's self-test fixture",
        "[ip": "the content screen's own masked-host placeholder ([IP ...]) inside a URL it reports",
        "claude": "the host fragment of a self-test string the scrub script builds by concatenation",
        "-8888.proxy.runpod.net": "the synthetic RunPod proxy host of the content script's self-test fixture",
        "example.org": "the reserved example domain of the content script's self-test fixture e-mail",
        "e.ai": "the tail of claude.ai cut by a 40-character excerpt window of the content screen",
        "gmail.com": "an e-mail domain in the content and history scripts' allowlists and domain classes",
        "users.noreply.github.com": "an e-mail domain in the content script's domain classes",
        "proxy.runpod.net": "a RunPod host name in this audit's pattern descriptions and class labels",
        "ssh.runpod.io": "a RunPod host name in this audit's pattern descriptions and class labels",
        "runpod.io": ("a RunPod host name in this audit's pattern descriptions and class labels, and an entry "
                      "of the history script's public-host allowlist"),
        "api.github.com": "the host of URLs this part read (WEB_READS), echoed in this audit's raws",
        "docs.github.com": "the host of a URL this part read (WEB_READS: GitHub's terms), echoed in this audit's raws",
        "raw.githubusercontent.com": ("the host of URLs this part and N2(vi) read (the Macar repository's files at "
                                      "its pin; row: Macar et al. materials), echoed in this audit's raws"),
        "arxiv.org": ("the Macar et al. paper's arXiv pages (row: Macar et al.), read by this part and N2(vi), and "
                      "an entry of the history script's public-host allowlist"),
        "creativecommons.org": ("the CC BY 4.0 deed, the Macar paper's license (a recorded read, WEB_READS), "
                                "echoed in this audit's raws"),
        **{h_: "an entry of the history script's public-host allowlist (PUBLIC_HOSTS)" for h_ in (
            "allenai.org", "claude.com", "colab.research.google.com", "docs.anthropic.com", "docs.python.org",
            "docs.runpod.io", "doi.org", "download.pytorch.org", "en.wikipedia.org", "matplotlib.org",
            "nbviewer.org", "openreview.net", "pypi.org", "pytorch.org", "scholar.google.com", "twitter.com",
            "w3.org", "www.alignmentforum.org", "www.arxiv.org", "www.lesswrong.com", "www.runpod.io",
            "www.w3.org", "x.com",
            # release (the PI's answer of 2026-10-12): the three hosts the history script's round-9 triage adds to
            # its PUBLIC_HOSTS (the Apache-2.0 text's URL host; the SVGs' C2PA and Dublin Core namespace hosts) --
            # members of this same class, which H3 lists; no new rule
            "www.apache.org", "c2pa.org", "purl.org",
            # release (L3): three more entries of the same allowlist, which the Global Workspace row classifies
            # where the record carries them; listed so that an audit file's echo of them (cut short by an excerpt
            # window) is explained by H3 carrier by carrier -- members of the same class, no new rule
            "www.anthropic.com", "anthropic.com", "transformer-circuits.pub")},
    }
    # release (L3): every host listed above as "an entry of the history script's public-host allowlist" is checked
    # against that allowlist as the history script holds it at the commit read (its PUBLIC_HOSTS set literal, read by
    # AST, never run); an entry the allowlist lacks loses this class (it is then classed by no listed reason)
    PH_LABEL = "an entry of the history script's public-host allowlist (PUBLIC_HOSTS)"
    ph_listed = sorted(h_ for h_, why_ in AUDIT_HOSTS.items() if why_ == PH_LABEL)
    ph_hist: set | None = None
    try:
        for n_ in ast.walk(ast.parse(text.get("scripts/audit_note_N12_history.py", ""))):
            if (isinstance(n_, ast.Assign) and any(isinstance(t_, ast.Name) and t_.id == "PUBLIC_HOSTS"
                                                   for t_ in n_.targets)
                    and isinstance(n_.value, ast.Set)):
                ph_hist = {e_.value for e_ in n_.value.elts if isinstance(e_, ast.Constant)}
    except SyntaxError:
        ph_hist = None
    ph_missing = [h_ for h_ in ph_listed if ph_hist is None or h_ not in ph_hist]
    for h_ in ph_missing:
        AUDIT_HOSTS.pop(h_, None)
    R["audit_hosts_public_allowlist_check"] = {
        "listed_as_public_allowlist_entries": len(ph_listed),
        "history_script_allowlist_read": ph_hist is not None,
        "history_script_allowlist_size": (len(ph_hist) if ph_hist is not None else None),
        "listed_but_not_in_the_history_allowlist": ph_missing}
    SVG_HOSTS = {     # host -> what it is in the figure SVGs' headers and metadata (root *.svg carriers)
        "www.w3.org": "the SVG, XLink and RDF namespace URIs and the SVG 1.1 DTD",
        "purl.org": "the Dublin Core element namespace and type vocabulary",
        "creativecommons.org": "the Creative Commons RDF namespace",
        "c2pa.org": "the C2PA namespace of the content-credentials element",
        "matplotlib.org": "the generator's credit (Matplotlib) in the dc:creator metadata",
    }
    DOC_HOSTS = {     # (host, carrier) -> what a document of the release names it for, with the paths allowed
        ("creativecommons.org", "README-NOTE.md"): (("/licenses/by/4.0",),
                                                     "the CC BY 4.0 deed, the repository's document license"),
    }

    # release (L3): the full hosts whose cut-short forms H3 explains -- the listed hosts (AUDIT_HOSTS, SVG_HOSTS), the
    # Global Workspace hosts, the two repository hosts and the hosts of the recorded-read URLs
    CUT_FULL = sorted({h_ for h_ in (set(AUDIT_HOSTS) | set(SVG_HOSTS) | set(GW_PATHS) | {"github.com", "huggingface.co"}
                                     | {re.sub(r"^https?://([^/]+).*$", r"\1", u_).lower() for u_ in WR_URLS})
                       if re.fullmatch(r"[a-z0-9-]+(\.[a-z0-9-]+)+", h_)})

    def cut_of(h: str) -> str | None:
        """Release (L3): the listed full host of which h is a cut-short form (a prefix or a suffix of it, as an excerpt
        window leaves it), or None."""
        if len(h) < 4:
            return None
        for f_ in CUT_FULL:
            if f_ != h and (f_.startswith(h) or f_.endswith(h)):
                return f_
        return None

    def audit_only_path(x: str, cpaths) -> bool:
        """Release (L3 fix round): path x of a host is carried only by this audit's own files (RX_AUDIT_FILE)."""
        if not cpaths:
            return False
        cs_ = [c_ for c_, ps_ in cpaths.items() if x in ps_]
        return bool(cs_) and all(RX_AUDIT_FILE.match(c_) for c_ in cs_)

    def cut_path(x: str, allowed) -> bool:
        """Release (L3 fix round): x is a proper prefix of an allowed path -- the form an excerpt window leaves when it
        cuts the allowed URL short. Any other path is not a cut form, whoever carries it."""
        return bool(x) and any(a_ != x and a_.startswith(x) for a_ in allowed)

    def host_class_r9(h: str, carriers: set, paths: list, cpaths=None) -> str | None:
        """Round 9 (H3; confirmed by the PI 2026-10-12): the class of a host every carrier of which is explained -- an audit file by
        AUDIT_HOSTS, a root .svg figure by SVG_HOSTS, a document by DOC_HOSTS (its paths allowed) -- or None.
        Release (L3): an audit file also explains a listed host cut short by an excerpt window (cut_of). A document's
        allowed paths are checked against every path of the host, as in round 9; the one addition (L3 fix round,
        Code's narrow reading, for the PI) is that a path carried only by this audit's own files that is a proper
        prefix of an allowed path (an excerpt window's cut of it) passes. Any other path fails the check."""
        why = []
        for c in sorted(carriers):
            if RX_AUDIT_FILE.match(c) and (h in AUDIT_HOSTS or h in SVG_HOSTS):
                r_ = "in this audit's own scripts and raws: " + AUDIT_HOSTS.get(h, "a host this part's SVG_HOSTS table names")
            elif RX_AUDIT_FILE.match(c) and cut_of(h):
                r_ = (f"in this audit's own scripts and raws: `{cut_of(h)}` cut short by an excerpt window "
                      f"(a listed host's cut form)")
            elif c.endswith(".svg") and "/" not in c and h in SVG_HOSTS:
                r_ = "in the figure SVGs: " + SVG_HOSTS[h]
            elif (h, c) in DOC_HOSTS and all(any(x.startswith(a_) for a_ in DOC_HOSTS[(h, c)][0]) or
                                             (h in SVG_HOSTS and x == "/ns#") or
                                             (cut_path(x, DOC_HOSTS[(h, c)][0]) and audit_only_path(x, cpaths))
                                             for x in paths if x):
                r_ = f"in `{c}`: " + DOC_HOSTS[(h, c)][1]
                cuts_ = [x for x in paths if x and not any(x.startswith(a_) for a_ in DOC_HOSTS[(h, c)][0])
                         and not (h in SVG_HOSTS and x == "/ns#")]
                if cuts_:
                    R9_HOSTS[("host", h)] = ("H3 with cut paths (Code's narrow reading, for the PI): a path outside "
                                             "a document's allowed ones is carried only by this audit's own files "
                                             "and is a proper prefix of an allowed path")
                    r_ += (" (its allowed path also appears cut short by an excerpt window, only in this audit's "
                           "own scripts and raws)")
            else:
                return None
            if r_ not in why:
                why.append(r_)
        return ("; ".join(why) + "; not a material") if why else None
    def _h3(k: tuple, c_: str | None) -> str | None:
        if c_:
            R9_HOSTS[k] = "H3: a host whose every carrier is explained (audit files by the listed hosts; root "\
                          "SVGs; a named document with allowed paths)"
        return c_

    def host_class(k: tuple, carriers: set, paths: list, n_claude_links: int, cpaths=None) -> str:
        kind, h = k
        if kind == "ip":
            return ("IP-literal host (loopback: a local dev-server address in the cycle-1-2 "
                    "docs/raws); not a material; never printed" if h.startswith("127.")
                    else "UNCLASSIFIED IP-literal host (Code to review)")
        if kind == "dotless":
            return ("loopback name; not a material" if h == "localhost" else
                    "dotless URL host inside model-generated text (OLMo transcripts under "
                    "data/olmo/); not a material" if carriers and
                    all(c.startswith("data/olmo/") for c in carriers)
                    else (_h3(k, host_class_r9(h, carriers, paths, cpaths)) or "UNCLASSIFIED dotless URL host (Code to review)"))
        if h in ("github.com", "huggingface.co"):
            return "repository URLs: every id is classified in the id table above"
        if h in GW_PATHS:
            # round 9 (H4; confirmed by the PI 2026-10-12): on transformer-circuits.pub, the Lindsey (2025) page (section 1's row) and the
            # site's home page (this part's recorded read) beside the Global Workspace paper
            extra_ = (("/2025/introspection",), ("/",)) if h == "transformer-circuits.pub" else ((), ())

            def gw_ok(x):
                return x.startswith(GW_PATHS[h]) or x.startswith(extra_[0]) or x in extra_[1]
            ok_ = bool(paths) and all(gw_ok(x) for x in paths)
            # release (L3 fix round; Code's narrow reading, for the PI): a path outside the allowed ones passes only
            # when it is a proper prefix of an allowed path (an excerpt window's cut of the paper's, the Lindsey
            # page's or the home page's URL) AND only this audit's own files carry it, the host being on H3's list
            # (an entry of the history script's public-host allowlist). Any other path -- a full URL to another page,
            # whoever carries it -- leaves the host UNCLASSIFIED, as in round 9.
            allowed_ = (GW_PATHS[h],) + extra_[0] + extra_[1]
            out_ = [x for x in paths if not gw_ok(x)]
            ok_l3 = (not ok_ and h in AUDIT_HOSTS and any(gw_ok(x) for x in paths) and bool(out_)
                     and all(cut_path(x, allowed_) and audit_only_path(x, cpaths) for x in out_))
            use_ = [x for x in paths if gw_ok(x)] if ok_l3 else paths
            if ok_l3:
                R9_HOSTS[k] = ("H3 with cut paths (Code's narrow reading, for the PI): the paths outside the allowed "
                               "ones are carried only by this audit's own files and are proper prefixes of an "
                               "allowed path, the host on H3's list")
            elif ok_ and not all(x.startswith(GW_PATHS[h]) for x in paths):
                R9_HOSTS[k] = "H4: transformer-circuits.pub's two allowed paths (the Lindsey page; the home page)"
            return (("row: the Global Workspace paper (section 2e)"
                     + ("; row: Lindsey (2025), section 1" if any(x.startswith(extra_[0]) for x in use_) else "")
                     + ("; the site's home page, a recorded read (WEB_READS)" if any(x in extra_[1] for x in use_)
                        else "")
                     + ("; an allowed path cut short by an excerpt window (a proper prefix of it), only in this "
                        "audit's own scripts and raws: " + AUDIT_HOSTS[h] if ok_l3 else "")) if (ok_ or ok_l3)
                    else "UNCLASSIFIED (a path outside the Global Workspace paper)")
        if h == "claude.ai":
            if n_claude_links and not claude_links_outside_audit:
                R9_HOSTS[k] = "H1: claude.ai links counted only outside this audit's own files"
            # round 9 (H1; confirmed by the PI 2026-10-12): links counted outside this audit's own files, which carry only redacted echoes of
            # the session link (seven commit trailers, left in history by the PI's D3 routing) and pattern text
            return ("the product name in prose (\"A Claude.ai project instance\"), not a link to "
                    "material" + ("; the only claude.ai links are in this audit's own scripts and raws (redacted "
                                  "echoes of the session link the PI's D3 routing left in the commit trailers, and "
                                  "scanner pattern text)" if n_claude_links else "")
                    if not claude_links_outside_audit else
                    "UNCLASSIFIED (a claude.ai link; Code to review)")
        if h in MODEL_OUT_HOSTS:
            if (carriers and all(c.startswith("data/olmo/") or RX_AUDIT_FILE.match(c) for c in carriers)
                    and any(c.startswith("data/olmo/") for c in carriers)
                    and any(RX_AUDIT_FILE.match(c) for c in carriers)):
                R9_HOSTS[k] = "H2: a model-output host with audit-file carriers beside the transcripts"
            # round 9 (H2; confirmed by the PI 2026-10-12): this audit's own files quote them too
            return ("inside model-generated text (OLMo transcripts under data/olmo/)"
                    + ("; quoted in this audit's own scripts and raws" if any(RX_AUDIT_FILE.match(c) for c in carriers)
                       else "") + "; not a material"
                    if carriers and all(c.startswith("data/olmo/") or RX_AUDIT_FILE.match(c) for c in carriers)
                    and any(c.startswith("data/olmo/") for c in carriers)
                    else "UNCLASSIFIED (outside the model transcripts)")
        r9_ = _h3(k, host_class_r9(h, carriers, paths, cpaths))
        if r9_:
            return r9_
        if audit_only(carriers):
            return ("UNCLASSIFIED (for the PI: carried only by this audit's own files, neither a listed host nor a "
                    "listed host's cut form)")
        return "UNCLASSIFIED (Code to review)"
    HS = []
    for k in sorted(set(h_head) | set(h_hist)):
        kind, h = k
        carriers = set(h_head.get(k, set())) | h_hist_paths.get(k, set())
        paths = sorted(x for x in h_paths.get(k, set()) if x)
        cls = host_class(k, carriers, paths, claude_links, h_cpaths.get(k, {}))
        # dotless hosts are printed only when they are a plain word in model text;
        # anything else (e.g. a machine name) is printed redacted
        show = (redform(h) if kind == "ip" or (kind == "dotless" and not (
            re.fullmatch(r"[a-z]+", h) and not cls.startswith("UNCLASSIFIED"))) else h)
        HS.append({"kind": kind, "host": show,
                   "head_files": len(h_head.get(k, set())), "history_blobs": len(h_hist.get(k, set())),
                   "history_only": not h_head.get(k), "paths": ([] if kind == "ip" else paths[:6]),
                   "carrier_paths": sorted(carriers)[:6], "class": cls})
    R["url_host_sweep"] = HS
    _sw_shown = {(kk, vv): s_["id"] for (kk, vv), s_ in zip(sorted(set(head_ids) | set(hist_ids)), SW)}
    _hs_shown = {kh: s_["host"] for kh, s_ in zip(sorted(set(h_head) | set(h_hist)), HS)}
    R9_APPLIED = {
        "confirmed": "the PI, 2026-10-12, one answer to five questions (\"Yes to all five; tag it\"), question 2",
        "ids": [{"kind": kk[0], "id": _sw_shown[kk], "rule": r_} for kk, r_ in sorted(R9_IDS.items())
                if kk in _sw_shown],
        "hosts": [{"kind": kh[0], "host": _hs_shown[kh], "rule": r_} for kh, r_ in sorted(R9_HOSTS.items())
                  if kh in _hs_shown and kh[0] != "ip"]}
    R["round9_rules_applied"] = R9_APPLIED
    n_host_uncl = sum(1 for s in HS if s["class"].startswith("UNCLASSIFIED"))
    ip_rows = [s for s in HS if s["kind"] == "ip"]
    dl_rows = [s for s in HS if s["kind"] == "dotless"]
    P(f"**Host-agnostic URL sweep** (any `http(s)://` host, dotted or not, plus bare domain names "
      f"on the common TLDs `{TLDS}`; same HEAD files and {HI['n_distinct_text_blobs_scanned']} "
      f"historical text blobs). Distinct dotted hosts: "
      f"**{sum(1 for s in HS if s['kind'] == 'host')}**, plus {len(dl_rows)} dotless URL host(s) "
      f"(in the table, marked dotless), plus "
      f"{len(ip_rows)} IP-literal host(s), counted and not printed (all loopback: "
      f"{all(s['class'].startswith('IP-literal host (loopback') for s in ip_rows)}); only in "
      f"history: {sum(1 for s in HS if s['history_only'])}; unclassified: **{n_host_uncl}**.")
    P("")
    P("| host | HEAD files | history blobs | history only | URL paths seen (up to 6) | carrier paths, HEAD or any commit (up to 6) | class |")
    P("|---|---|---|---|---|---|---|")
    for s in HS:
        if s["kind"] == "ip":
            continue
        P(f"| `{s['host']}`{' (dotless)' if s['kind'] == 'dotless' else ''} | {s['head_files']} | {s['history_blobs']} | {s['history_only']} | "
          f"{', '.join(f'`{x}`' for x in s['paths']) if s['host'] not in ('github.com', 'huggingface.co') else '(ids above)'} | "
          f"{', '.join(f'`{x}`' for x in s['carrier_paths'])} | {s['class']} |")
    P("")
    P(f"**Round-9 rules** (Code's rule changes, confirmed by the PI on 2026-10-12: \"Yes to all five; tag "
      f"it\", question 2). Rows of the two tables above that only these rules classify at this run: "
      f"**{len(R9_APPLIED['ids'])}** id(s) ("
      + "; ".join(f"{r_}: {sum(1 for x in R9_APPLIED['ids'] if x['rule'] == r_)}"
                  for r_ in sorted({x['rule'] for x in R9_APPLIED['ids']})) + ") and "
      f"**{len(R9_APPLIED['hosts'])}** host(s) ("
      + "; ".join(f"{r_.split(':')[0]}: {sum(1 for x in R9_APPLIED['hosts'] if x['rule'] == r_)}"
                  for r_ in sorted({x['rule'] for x in R9_APPLIED['hosts']})) + "). Each row's class is "
      "printed in its table; the JSON `round9_rules_applied` lists them with the rule.")
    P("")
    n_arxiv_host = sum(1 for s in HS if s["host"].endswith("arxiv.org"))
    P(f"Rows with an `arxiv.org` host: {n_arxiv_host}; the record's arXiv references are ids, "
      f"classified in the id table above. A third-party work the record does not name at all is "
      f"found by neither sweep: Lindsey (2025), named only inside the Macar paper, is handled in "
      f"section 1.")
    P("")
    # ---- projection (round 4, Code's own): the two sweeps over this audit's own working
    # files, which are untracked at the commit read and tracked at the pre-flip re-run. The
    # rules are the sweeps' own (ids_in/id_class, hosts_in/host_class); only the carriers
    # change. Hosts and ids found only in other audit items' files are counted, never
    # printed (they can name machines or people).
    # Release (L3): the audit files projected are RX_AUDIT_FILE's (every results/raw/*_note-* raw, any date, and every
    # scripts/audit_note_*.py) untracked at the run -- e.g. the release raws the scans before this one wrote -- and this
    # run's own two outputs, which are not on disk while it runs, are projected by the closing self-check; the
    # verdicts printed here, in section 7 item 8 and in the round-4 values-check row are the combined ones
    # (placeholders filled at the end, the self-check iterated to a fixed point).
    def _rel_out(o_: str) -> str:
        r_ = os.path.relpath(os.path.realpath(o_), os.path.realpath(REPO))
        return r_ if not r_.startswith("..") else "results/raw/" + os.path.basename(o_)
    OUT_MD_C, OUT_JSON_C = _rel_out(OUT_MD), _rel_out(OUT_JSON)
    MINE = {"scripts/audit_note_N12_licenses.py", os.path.relpath(DEFAULT_MD, REPO),
            os.path.relpath(DEFAULT_JSON, REPO), OUT_MD_C, OUT_JSON_C}
    own_txt: dict = {}
    for p_ in own:
        if not is_text_path(p_) or p_ in (OUT_MD_C, OUT_JSON_C):
            continue
        try:
            own_txt[p_] = open(os.path.join(REPO, p_), encoding="utf-8", errors="replace").read()
        except OSError:
            continue

    def project(extra: dict):
        """The two sweeps' rules over the tracked carriers plus `extra` (path -> text, as if tracked): the ids and
        hosts that `extra` carries and the sweeps would leave unclassified, each with the extra paths carrying it."""
        e_ids: dict = defaultdict(set)
        e_hosts: dict = defaultdict(set)
        e_cp: dict = defaultdict(lambda: defaultdict(set))
        for p_, t_ in extra.items():
            for k in ids_in(t_):
                e_ids[k].add(p_)
            for k, pp in hosts_in(t_).items():
                e_hosts[k].add(p_)
                e_cp[k][p_] |= pp
        n_cl = claude_links + sum(1 for t_ in extra.values() if RX_CLAUDE_LINK.search(t_))
        u_ids = {}
        for k, ps in e_ids.items():
            car = (set(head_ids.get(k, [])) | {c_ for b_ in hist_ids.get(k, []) for c_ in hist_blob_paths[b_]}
                   | ps)
            if id_class(k, car).startswith("UNCLASSIFIED"):
                u_ids[k] = ps
        u_hosts = {}
        for k, ps in e_hosts.items():
            car = set(h_head.get(k, set())) | h_hist_paths.get(k, set()) | ps
            cp: dict = defaultdict(set)
            for c_, xs in h_cpaths.get(k, {}).items():
                cp[c_] |= xs
            for c_, xs in e_cp[k].items():
                cp[c_] |= xs
            pth = sorted(x for x in (h_paths.get(k, set()) | {x for xs in e_cp[k].values() for x in xs}) if x)
            if host_class(k, car, pth, n_cl, cp).startswith("UNCLASSIFIED"):
                u_hosts[k] = ps
        return u_ids, u_hosts
    own_claude = sum(1 for t_ in own_txt.values() if RX_CLAUDE_LINK.search(t_))
    pj_ids, pj_hosts = project(own_txt)
    pj_mine_hosts = sorted((h if kind == "host" or re.fullmatch(r"[a-z]+", h) else redform(h))
                           + (" (dotless)" if kind == "dotless" else "")
                           for (kind, h), ps in pj_hosts.items() if ps & MINE and kind != "ip")
    # ids from this part's files that are path fragments of the URLs its recorded reads name
    # (e.g. `api/models` in https://huggingface.co/api/models/...) are printed; any other is
    # counted only
    wr_ids = ids_in(json.dumps(WEB_READS))
    pj_mine_ids = sorted(v for k, ps in pj_ids.items() if ps & MINE and k in wr_ids
                         for v in [k[1]])
    pj_mine_ids_other = sum(1 for k, ps in pj_ids.items() if ps & MINE and k not in wr_ids)
    pj_ip = sum(1 for (kind, _h) in pj_hosts if kind == "ip")
    pj_oth_hosts = sum(1 for (kind, _h), ps in pj_hosts.items() if not ps & MINE and kind != "ip")
    pj_oth_ids = sum(1 for ps in pj_ids.values() if not ps & MINE)
    R["sweeps_projected_over_own_audit_files"] = {
        "audit_file_rule": RX_AUDIT_FILE.pattern,
        "n_own_untracked": len(own), "n_own_text_read": len(own_txt),
        "own_untracked_paths": own,
        "unclassified_ids": len(pj_ids), "unclassified_hosts": len(pj_hosts),
        "unclassified_ids_sha256_8": sorted(sha256(k[1].encode())[:8] for k in pj_ids),
        "unclassified_hosts_sha256_8": sorted(sha256(k[1].encode())[:8] for k in pj_hosts),
        "ip_literal_hosts": pj_ip, "from_this_part_hosts": pj_mine_hosts,
        "from_this_part_ids_url_fragments": pj_mine_ids,
        "from_this_part_ids_other_count": pj_mine_ids_other,
        "from_other_audit_files_only": {"hosts": pj_oth_hosts, "ids": pj_oth_ids},
        "this_runs_own_outputs": "see self_check (combined verdict: @@L3COMB@@)"}
    P(f"**Once this audit's own working files are tracked.** This audit's own files (every "
      f"`results/raw/*_note-*` raw, any date, and every `scripts/audit_note_*.py`) untracked at the "
      f"commit read: {len(own)} ({len(own_txt)} text files read from disk at this run, this run's own "
      f"outputs excepted); neither sweep counts them. Projected over them with the sweeps' own rules "
      f"(Code's computation, round 4), the id sweep would gain **{len(pj_ids)}** unclassified id(s) and "
      f"the host sweep **{len(pj_hosts)}** unclassified host(s) ({pj_ip} IP-literal, counted "
      f"only). This run's own two outputs, not on disk while it runs, are projected by the closing "
      f"self-check (as `{OUT_MD_C}` and `{OUT_JSON_C}`): @@L3SELF@@ in them. Together: "
      f"@@L3COMB@@ unclassified@@L3VERDICT_2F@@. Audit raws written after this run (later steps of "
      f"the release sequence) are in neither projection; the re-run over the commit that tracks them "
      f"is their check"
      + ". From this part's own files: hosts "
      + (", ".join(f"`{x}`" for x in pj_mine_hosts) or "none")
      + " (its recorded-read URLs, and rows of the table above whose class holds only while "
      "every carrier is a model transcript, every path is an allowed one -- the Global Workspace "
      "paper's, or on transformer-circuits.pub the Lindsey page's or the home page's, a path outside "
      "them passing only as a proper prefix of one carried by audit files alone -- or no file "
      f"outside the audit files links to claude.ai); ids: {len(pj_mine_ids)} path "
      f"fragments of the URLs its recorded reads name, which the URL pattern parses as ids ("
      + (", ".join(f"`{x}`" for x in pj_mine_ids) or "none")
      + f"), and {pj_mine_ids_other} other(s), counted only. From the other audit files only: "
      f"{pj_oth_hosts} host(s) and {pj_oth_ids} id(s), "
      f"counted and not printed (they can name machines or people). The classification rules "
      f"and the gates are not changed here.")
    P("")

    # =====================================================================
    # 3. Models
    # =====================================================================
    P("## 3. Models")
    P("")
    man = json.loads(text["data/olmo/manifest.json"])
    M = {}
    P("| stage | repo (manifest) | revision (manifest) | HF sha (recorded read) | prefix match | license (card, recorded read) | gated | base_model (card) | license key in manifest |")
    P("|---|---|---|---|---|---|---|---|---|")
    for stage, e in man.items():
        hf = WEB_READS["hf_models"].get(e["repo"], {})
        pm = bool(hf) and hf["sha"].startswith(e["revision"])
        lk = [k for k in e if re.search(r"licen", k, re.I)]
        M[stage] = {"repo": e["repo"], "revision": e["revision"], "hf_sha": hf.get("sha"),
                    "prefix_match": pm, "license": hf.get("license"), "gated": hf.get("gated"),
                    "base_model": hf.get("base_model"), "manifest_license_keys": lk}
        P(f"| {stage} | `{e['repo']}` | `{e['revision']}` | `{hf.get('sha', '?')[:12]}...` | {pm} | "
          f"{hf.get('license', '[to confirm]')} | {hf.get('gated')} | {hf.get('base_model')} | {lk or 'none'} |")
    q = WEB_READS["hf_models"]["mlx-community/Qwen3.6-27B-4bit"]
    qb = WEB_READS["hf_models"]["Qwen/Qwen3.6-27B"]
    q_files = sorted(p for p, t in text.items() if "mlx-community/Qwen3.6-27B-4bit" in t)
    q_pin_files = sorted(p for p, t in text.items() if q["sha"][:12] in t)
    local_ref = open(HF_CACHE_QWEN).read().strip() if os.path.isfile(HF_CACHE_QWEN) else None
    M["qwen"] = {"id": "mlx-community/Qwen3.6-27B-4bit", "license": q["license"],
                 "base_model": q["base_model"], "base_license": qb["license"],
                 "hf_sha": q["sha"], "n_tracked_files_naming_id": len(q_files),
                 "tracked_files_pinning_hf_sha_prefix": q_pin_files,
                 "local_hf_cache_refs_main": local_ref}
    P(f"| (Qwen oracle) | `mlx-community/Qwen3.6-27B-4bit` | none declared (see below) | `{q['sha'][:12]}...` | n/a | "
      f"{q['license']} (license_link -> `{q['license_link']}`) | {q['gated']} | {q['base_model']} ({qb['license']}) | n/a |")
    P("")
    P(f"- Every manifest revision is a 12-hex prefix of the card's current sha: "
      f"{all(M[s]['prefix_match'] for s in man)} (so the pinned revisions are still each repo's "
      f"`main` as of the read). No `license` key exists in `data/olmo/manifest.json`.")
    q_pin_lines = []
    q_in_snap = 0
    for p in q_pin_files:
        for i, l in enumerate(text[p].splitlines(), 1):
            if q["sha"][:12] in l:
                q_pin_lines.append(f"{p}:{i}")
                q_in_snap += f"snapshots/{q['sha'][:12]}" in l
    M["qwen"]["lines_where_sha_is_in_a_snapshot_path"] = q_in_snap
    q_pin_cfg = [p for p in q_pin_files if p.startswith(("data/", "valence_core/", "scripts/"))
                 or p.endswith(".json")]
    M["qwen"]["tracked_lines_with_hf_sha_prefix"] = q_pin_lines
    P(f"- Qwen: {len(q_files)} tracked text files name `mlx-community/Qwen3.6-27B-4bit` (run "
      f"artifacts' `model_id` fields and docs). The card's sha prefix `{q['sha'][:12]}` occurs "
      f"in {len(q_pin_files)} tracked files ({len(q_pin_lines)} lines: "
      f"{', '.join(f'`{x}`' for x in q_pin_lines)}); lines where it sits inside a local "
      f"HF-cache `snapshots/<sha>` path: {q_in_snap} of {len(q_pin_lines)}; in a "
      f"data/config/code file: "
      f"{len(q_pin_cfg)}. So the record **declares** no Qwen weights revision (no manifest or "
      f"config field), though its raw logs show which snapshot was read. This machine's HF cache "
      f"`refs/main` (a local fact): `{local_ref}`, equal to the card's current sha: "
      f"{local_ref == q['sha']}. The README can state it as the revision the laptop runs.")
    WEXT = (".safetensors", ".gguf", ".bin", ".pt", ".pth", ".ckpt", ".h5", ".onnx", ".msgpack")
    w_files = [r["path"] for r in tree if r["path"].lower().endswith(WEXT)]
    npz = [r for r in tree if r["path"].endswith(".npz")]
    big = [r for r in tree if r["size"] > 1_000_000_000]
    M["weights_at_commit"] = {"weight_ext_files": w_files, "n_npz": len(npz),
                              "n_over_1GB": len(big)}
    P(f"- HEAD-level context only (the history check is the other part's): tracked files with a "
      f"weights extension ({', '.join(WEXT)}): {len(w_files)}; tracked files over 1 GB: {len(big)}; "
      f"tracked `.npz` files: {len(npz)} (residual/axis arrays; the allowlist comparison is not "
      f"done here).")
    P("- Model outputs: the record carries generated text from these models (transcripts in "
      "`data/**` and `results/raw/**`). Code did not read any model's terms on generated output "
      "beyond the card's license field; the README can say the transcripts are model outputs under "
      "the models named.")
    P("")
    R["models"] = M

    # =====================================================================
    # 4. Datasets / corpora / stimuli
    # =====================================================================
    P("## 4. Datasets, corpora and stimulus files")
    P("")
    stim = sorted(p for p in by_path if p.startswith(("data/configs/", "data/corpus/"))) + [
        p for p in ("data/f/pools.json", "data/format/neutral_label_selection.json") if p in by_path]
    RX_TP = re.compile(r"https?://|github|arxiv|huggingface|hf\.co|\bdataset\b|alpaca|dolly|"
                       r"sst-?2|imdb|squad|wikipedia|common ?crawl|\blicen[cs]e\b|copyright|"
                       r"macar|safety-research|introspection-mechanisms|lindsey|from the paper", re.I)
    ST = []
    for p in stim:
        t = text.get(p, "")
        keys: list = []
        try:
            if p.endswith(".jsonl"):
                recs = [json.loads(l) for l in t.splitlines() if l.strip()]
                keys = sorted({k for rr in recs for k in rr})
                n = len(recs)
            else:
                d = json.loads(t)
                keys = list(d.keys()) if isinstance(d, dict) else ["<list>"]
                n = None
        except Exception as ex:
            keys, n = [f"PARSEFAIL {ex}"], None
        prov_keys = [k for k in keys if re.search(r"^_doc$|provenance|source|_status|^status$|authority", k)]
        markers = sorted({m.group(0).lower() for m in RX_TP.finditer(t)})
        fa = gtext("log", "--all", "--diff-filter=A", "--format=%h %ad", "--date=short", "--",
                   p).strip().splitlines()
        tp = bool(re.search(r"macar|safety-research|introspection-mechanisms", " ".join(markers)))
        macar_words = sorted(w for w in set(bc.get("canonical_concepts", []))
                             if re.search(rf'"{re.escape(w)}"', t))
        if p in ("data/configs/b2_concepts.json", "data/configs/b2_framing.json"):
            cls = "third-party text (Macar et al.)"
        elif tp:
            cls = (f"lab-authored; names Macar by reference and carries {len(macar_words)} of "
                   f"their concept words as JSON strings")
        else:
            cls = "lab-authored"
        ST.append({"path": p, "sha256": sha256(t.encode()), "records": n,
                   "provenance_keys": prov_keys, "third_party_markers": markers,
                   "macar_concept_words_as_strings": len(macar_words),
                   "first_added": fa[-1] if fa else None, "class": cls})
    # evidence for the two corpora that carry no provenance field
    arch = loc_src("archive/RESULTS-cycles3-4.md").splitlines()
    ev = {
        "e0_tasks_build": ("archive/RESULTS-cycles3-4.md", 1590, "Build (local under `jlens-qwen36/`"),
        "e0_tasks_path": ("archive/RESULTS-cycles3-4.md", 1592, "`data/corpus/e0_tasks.jsonl` (48 tasks"),
        "e0_fixed_completions": ("archive/RESULTS-cycles3-4.md", 1598, "(1) **fixed pre-written"),
        "e2a_tasks_fresh": ("archive/RESULTS-cycles3-4.md", 1294, "Task pool: fresh `e2a_tasks.jsonl`"),
    }
    EV = {}
    for k, (f, ln, s) in ev.items():
        EV[k] = {"locator": f"{f}@{LOC[:7]}:{ln}", "expect": s,
                 "found": s in (arch[ln - 1] if ln - 1 < len(arch) else "")}
    up_corpus = [p for p in JLENS_UPSTREAM_BLOBS if p.startswith("data/")]
    R["stimuli"] = {"files": ST, "evidence": EV, "upstream_jlens_data_paths": up_corpus}
    P("| file | sha256 (16) | records | provenance keys | third-party markers | first added | class |")
    P("|---|---|---|---|---|---|---|")
    for s in ST:
        P(f"| `{s['path']}` | `{s['sha256'][:16]}` | {s['records'] if s['records'] is not None else '-'} | "
          f"{', '.join(s['provenance_keys']) or '-'} | {', '.join(s['third_party_markers']) or '-'} | "
          f"{s['first_added']} | {s['class']} |")
    P("")
    P("Evidence for the two corpora that carry no provenance field (lines asserted present by the script):")
    P("")
    for k, v in EV.items():
        P(f"- `{v['locator']}` contains \"{v['expect']}\": {v['found']}")
    P(f"- Upstream jlens-qwen36 at the clone commit has under `data/` only {up_corpus} "
      f"**[recorded WebFetch read]**: the corpus files were written into the clone by the lab and "
      f"pulled into the record \"byte-identical\" at `f190a32` / `47ef4c7` (commit subjects).")
    b2r = json.loads(text["data/configs/b2r_step1.json"])
    P(f"- `data/configs/b2r_step1.json`: `_doc` says \"Code-authored\"; its `concepts_source` is "
      f"\"{b2r.get('concepts_source')}\", so its `concepts_step1` "
      f"({len(b2r.get('concepts_step1', []))} words) are Macar's words by selection, and its neutral "
      f"prompts are lab-authored. The class column above is the script's rule: Macar markers "
      f"present but not one of the two source files -> lab-authored, with the count of Macar "
      f"concept words it carries.")
    P("")

    # =====================================================================
    # 5. Repository license
    # =====================================================================
    P("## 5. The repository's own license")
    P("")
    RX_LF = re.compile(r"(^|/)(LICEN[CS]E|COPYING|NOTICE)(\.[A-Za-z]+)?$", re.I)
    lf_head = [r["path"] for r in tree if RX_LF.search(r["path"])]
    hist_all = gtext("log", "--all", "--format=", "--name-only", "--diff-filter=A")
    lf_hist = sorted({l for l in hist_all.splitlines() if RX_LF.search(l)})
    rd = text.get("README.md", "")
    rd_hits = [f"README.md:{i}: {redact(l.strip()[:120], 'README.md')}"
               for i, l in enumerate(rd.splitlines(), 1)
               if re.search(r"licen[cs]|Macar|Apache|attribut|third[- ]party|WeZZard|copyright", l, re.I)]
    refs = gtext("for-each-ref", "--format=%(refname)").split()
    R["repo_license"] = {"license_files_at_commit": lf_head,
                         "license_files_ever_added_any_ref": lf_hist,
                         "readme_license_lines": rd_hits, "refs": refs}
    # Release preparation (round 1's L check, scrub index section 5's flag): every statement
    # about THIS repository's own license is computed from the tree at the commit read, never
    # fixed text. Root-level license texts: a name beginning LICENSE / LICENCE / COPYING with
    # any suffix (RX_LF, the section-5 count rule above, is unchanged and stays as it was);
    # each is identified by its opening lines, and LICENSING.md (if tracked) is read for the
    # line that links each one and that line's bold label.
    RX_LT = re.compile(r"^(LICEN[CS]E|COPYING)([.-][A-Za-z0-9.-]+)?$", re.I)
    LT_KINDS = ((("Apache License", "Version 2.0"), "Apache License, Version 2.0"),
                (("Attribution 4.0 International",), "CC BY 4.0 (Attribution 4.0 International)"))
    lt_rows = sorted((r for r in tree if r["type"] == "blob" and "/" not in r["path"]
                      and RX_LT.match(r["path"])), key=lambda r: r["path"])
    lt_blobs = cat_blobs([r["blob"] for r in lt_rows])
    lmap_src = text.get("LICENSING.md")
    lmap_lines = lmap_src.splitlines() if lmap_src is not None else []

    def _first_added(path: str) -> str | None:
        out = gtext("log", "--all", "--diff-filter=A", "--format=%h", "--", path).split()
        return out[-1][:7] if out else None
    lic_texts = []
    for r in lt_rows:
        b = lt_blobs[r["blob"]]
        opening = b[:400].decode("utf-8", "replace")
        kind = next((lab for needles, lab in LT_KINDS if all(n in opening for n in needles)), None)
        link_lines = [i for i, l in enumerate(lmap_lines, 1) if f"(./{r['path']})" in l]
        labels = []
        for i in link_lines:
            m = re.match(r"\s*-\s*\*\*(.+?)\*\*", lmap_lines[i - 1])
            if m:
                labels.append(m.group(1))
        lic_texts.append({"path": r["path"], "sha256": sha256(b), "kind": kind,
                          "first_added": _first_added(r["path"]),
                          "sha256_listed_in_LICENSING_md": (lmap_src is not None and sha256(b) in lmap_src),
                          "LICENSING_md_link_lines": link_lines, "LICENSING_md_labels": labels})
    lmap = None
    if lmap_src is not None:
        lmap = {"path": "LICENSING.md", "first_added": _first_added("LICENSING.md"),
                "third_party_heading_line": next((i for i, l in enumerate(lmap_lines, 1)
                                                  if re.match(r"#+\s*Third-party material", l)), None)}
    def _lt_reasons(t: dict) -> list[str]:
        out = []
        if not t["kind"]:
            out.append("not identified by its opening lines")
        if lmap_src is not None and not t["sha256_listed_in_LICENSING_md"]:
            out.append("its sha256 is not listed in `LICENSING.md`")
        return out
    for t in lic_texts:
        t["open_reasons"] = _lt_reasons(t)
    lic_open = [t for t in lic_texts if t["open_reasons"]]
    repo_licensed = bool(lic_texts) and not lic_open
    lic_open_s = "; ".join(f"`{t['path']}`: {', '.join(t['open_reasons'])}" for t in lic_open)
    lt_not_lf = [t["path"] for t in lic_texts if not RX_LF.search(t["path"])]
    R["repo_license"].update({"root_license_texts": lic_texts, "licensing_map": lmap,
                              "repo_licensed_at_commit": repo_licensed,
                              "rule_root_license_texts": RX_LT.pattern,
                              "rule_repo_licensed": "every root-level license text is identified by "
                                                    "its opening lines and, where LICENSING.md is "
                                                    "tracked, its sha256 is listed there",
                              "root_license_texts_not_matched_by_count_rule": lt_not_lf,
                              "note": "statements about this repository's license are computed "
                                      "from these fields at the commit read"})

    def _lt_desc(t: dict) -> str:
        s = f"`{t['path']}`: {t['kind'] or 'text not identified by its opening lines'}"
        if t["LICENSING_md_labels"]:
            s += " (" + ", ".join(f"`LICENSING.md:{i}`" for i in t["LICENSING_md_link_lines"]) + ": " \
                 + ", ".join(f"**{x}**" for x in t["LICENSING_md_labels"]) + ")"
        return s
    lic_summary = "; ".join(_lt_desc(t) for t in lic_texts)
    lic_added = sorted({t["first_added"] for t in lic_texts if t["first_added"]}
                       | ({lmap["first_added"]} if lmap and lmap["first_added"] else set()))
    lic_added_s = ", ".join(f"`{c}`" for c in lic_added) or "no commit found"
    P(f"- LICENSE / LICENCE / COPYING / NOTICE files at the commit: **{len(lf_head)}**{(' ' + str(lf_head)) if lf_head else ''} "
      f"(this count's rule: that exact name with an optional alphabetic extension, at any depth"
      + (f"; {', '.join(f'`{x}`' for x in lt_not_lf)} {'does' if len(lt_not_lf) == 1 else 'do'} not match it "
         f"and {'is' if len(lt_not_lf) == 1 else 'are'} counted with the root-level license texts below"
         if lt_not_lf else "") + ").")
    P(f"- Such a file ever added in any commit on any ref ({len(refs)} refs: "
      f"{', '.join(r.replace('refs/', '') for r in refs)}; same rule): **{len(lf_hist)}**.")
    P(f"- `README.md` lines mentioning a license, Macar, Apache, attribution, third-party material, "
      f"WeZZard or copyright: **{len(rd_hits)}**" + (": " + "; ".join(rd_hits) if rd_hits else "."))
    tos = WEB_READS["github_tos"]
    P(f"- Root-level license texts at the commit (name beginning LICENSE / LICENCE / COPYING, any "
      f"suffix; identified by their opening lines): **{len(lic_texts)}**"
      + (": " + "; ".join(_lt_desc(t) + f", sha256 `{t['sha256'][:12]}...`, first added at "
                         f"`{t['first_added']}`, sha256 listed in `LICENSING.md`: "
                         f"{t['sha256_listed_in_LICENSING_md']}" for t in lic_texts)
         if lic_texts else "")
      + ". `LICENSING.md` at the commit: "
      + (f"**present** (first added at `{lmap['first_added']}`; its third-party heading: "
         + (f"`LICENSING.md:{lmap['third_party_heading_line']}`" if lmap['third_party_heading_line'] else "none")
         + ")" if lmap else "**absent**") + ".")
    if repo_licensed:
        P(f"- The repository **carries its own license** at the commit read: {lic_summary}. "
          f"The files were added at {lic_added_s}. This audit records them and does not judge "
          "their fit. Third-party material keeps its own terms "
          "(sections 6 and 7). **[recorded WebFetch read]** "
          f"`{tos['url']}`, section {tos['result']['section']} (from the WebFetch summary, not "
          "verbatim): a user posting content they did not create must make sure it is licensed "
          "for the uses GitHub's features allow, which bears on the Macar rows (section 7, item 1).")
    elif lic_texts:
        P(f"- The repository carries root-level license text(s) this part does not record as its "
          f"license: {lic_open_s} (all root-level texts: {lic_summary}). The PI reads them; this "
          f"audit records them.")
    else:
        P("- The repository has **no license**. Without one, the default is that copyright law reserves "
          "all rights (the task's framing). **[recorded WebFetch read]** "
          f"`{tos['url']}`, section {tos['result']['section']} (from the WebFetch summary, not "
          "verbatim): making a repository public grants other GitHub users a licence to view the "
          "content and to reproduce it on GitHub as its features allow, forking included. Beyond those "
          "view-and-fork rights, readers would have no grant to reuse the code. The same summary says a "
          "user posting content they did not create must make sure it is licensed for those uses, "
          "which bears on the Macar rows (section 7, item 1). Choosing a license, or none, is the PI's "
          "decision; this audit records the gap.")
    cfg_main = open(os.path.join(REPO, ".git", "config")).read()
    fetch_specs = re.findall(r"^\s*fetch\s*=\s*(\S+)\s*$", cfg_main, re.M)
    fh = os.path.join(REPO, ".git", "FETCH_HEAD")
    R["repo_license"]["origin_fetch_refspecs"] = fetch_specs
    R["repo_license"]["fetch_head_bytes"] = os.path.getsize(fh) if os.path.isfile(fh) else None
    P(f"- **Refs this part can see.** Every history scan above covers the {len(refs)} local refs. "
      f"The local `.git/config` fetch refspec(s): {', '.join(f'`{s}`' for s in fetch_specs)}; "
      f"`.git/FETCH_HEAD` is {R['repo_license']['fetch_head_bytes']} bytes. Server-side refs that "
      f"no local ref mirrors (pull-request refs `refs/pull/*`, or branches pushed after the last "
      f"fetch) are not visible here. `git ls-remote origin` (network, stored credentials) was not "
      f"run; the PI may run it before changing visibility (section 7, item 6).")
    P("")

    # =====================================================================
    # 6. Table
    # =====================================================================
    P("## 6. Licenses and third-party materials -- table for the README")
    P("")
    P("| material | location | source | pinned sha | license | redistribution OK? | action for README |")
    P("|---|---|---|---|---|---|---|")
    if J.get("present"):
        n_tr_head = len(J["tracked_paths_under_clone_at_commit"])
        n_tr_hist = len(J["paths_under_clone_in_any_commit_all_refs"])
        n_up_bi = sum(1 for m in J["byte_identical"] if m["class"].startswith("UPSTREAM"))
        n_up_body = len(J["vs_upstream"]["identical_bodies_ge3"])
        n_up_near = J["vs_upstream"]["near_copy_counts"][0.5]
        n_up_lines = len(J["vs_upstream"]["shared_long_lines_grouped"])
        jl_red = (f"at HEAD {n_up_bi} upstream files byte-identical, {n_up_body} identical "
                  f"upstream function bodies, {n_up_near} near-copies at Jaccard >= 0.5, "
                  f"{n_up_lines} distinct shared long lines")
        HCs = J.get("history_copy_check", {})
        if HCs.get("ran"):
            jl_red += (f"; across all {HCs['n_commits']} commits {len(HCs['upstream_nonempty_blobs_in_history'])} "
                       f"non-empty upstream blobs, {len(HCs['identical_bodies_ge3'])} identical "
                       f"bodies, {HCs['near_copy_counts'][0.5]} near-copies at Jaccard >= 0.5 "
                       f"(best {HCs['near_copy_top'][0]['jaccard'] if HCs['near_copy_top'] else 'n/a'})")
        else:
            jl_red += "; history check not run"
        jl_red += " (see section 2c)"
    else:
        n_tr_head = len([r for r in tree if r["path"].startswith("jlens-qwen36/")])
        n_tr_hist, jl_red = "[not run]", "[copy check not run: clone absent]"
    R["jlens_summary"] = {"tracked_at_commit": n_tr_head, "tracked_any_commit": n_tr_hist,
                          "copy_check": jl_red}
    plic = WEB_READS["macar_paper_arxiv_abs"]["result"]["license_label"]
    harness_globs = re.compile(r"^(valence_core/detection(_v2)?\.py|scripts/box_b2.*\.py|scripts/b2.*_analyze\.py)$")
    extra_builders = [p for p in builders if not harness_globs.match(p)]
    n_bi = len(J.get("byte_identical", [])) if J.get("present") else 0
    n_bi_up = (sum(1 for m in J["byte_identical"] if m["class"].startswith("UPSTREAM"))
               if J.get("present") else 0)
    jl_tracked = (f"no upstream file tracked ({n_bi_up} upstream files byte-identical to a tracked "
                  f"blob); {n_bi} lab-authored files that the record pulled from the clone are "
                  f"tracked byte-identical by design (section 2c)")
    R["jlens_summary_tracked"] = jl_tracked
    rows = [
        ("Macar et al. prompt text: framing paragraph, acknowledgement turn (\"Ok.\"), trial question (verbatim), and the `Tell me about {word}` extraction template",
         "`data/configs/b2_framing.json` (fidelity, shared); `valence_core/detection.py` (`MACAR_FRAMING`, `TRIAL_QUESTION`, `ACK`; `COMPLETION_TEMPLATE` is the lab's completion-style form of their fallback); the template in `data/configs/b2_concepts.json`; "
         f"framing in {len(fr_files)} tracked files at HEAD ({len(fr_hist)} paths across history); trial question in {len(tq_files)} on a single line plus {len(tq_norm)} wrapped, {len(tq_files) + len(tq_norm)} in all ({len(tq_hist)} + {len(tq_hist_norm)} paths across history); built at run time by {len(builders)} files (section 1)",
         f"transcribed from github.com/safety-research/introspection-mechanisms at the pin; the same text is printed in the paper, arXiv:2603.21396, App. A Table 4 (the template in App. B.2); it appeared earlier in Lindsey (2025), transformer-circuits.pub/2025/introspection ({lz['date']}), which prints the same framing ({lz3['framing_sentences_identical_to_record'][0]} of {lz3['framing_sentences_identical_to_record'][1]} sentences identical), \"{S1['record_ACK']}\" and trial question (fetch-tool comparisons; its trial turn adds a lead-in sentence the record does not carry) and the same extraction template",
         f"repo `{MACAR_PIN}`; paper v5 (2026-06-10); Lindsey page: no version pinned",
         f"**{plic} via the paper** (arXiv's license line), a later publication (v1 {S1['prompt_text_first_publication']['macar_paper_v1']}) whose authors include Lindsey; Lindsey (2025), where the text appeared first of the sources read: no license statement on the page, nor a site-wide one on the site's home page (round-4 read) **[to confirm]**; the code repository it was transcribed from: none",
         f"**yes, with attribution under {plic}**, if the PI accepts the paper as the licensing source for text its co-author published first with no license stated (the PI's judgement); byte identity with the paper's text [to confirm]; the paper's trial-question placeholder is `{{trial_num}}`, the record's `{{n}}`",
         f"Attribute per {plic}: Macar et al. 2026, *Mechanisms of Introspective Awareness*, arXiv:2603.21396, {plic} (link the license), App. A Table 4 (and B.2), with the placeholder change and the completion-style joiner noted; credit Lindsey (2025), *Emergent Introspective Awareness in Large Language Models*, as the earlier publication of the same text; **the PI confirms**"),
        ("Concept list (50) and baseline words (100)",
         f"`data/configs/b2_concepts.json` (the only file with >= 20 of either list); subsets: the approved eight also appear in {len(wl_other8)} `data/olmo/` JSON artifacts and as member names of {len(wl_npz8)} `b2*_concepts_*.npz` arrays, and 1-7 of the 50 in {len(WL['files_with_1_to_7_of_50'])} files (among them `data/configs/b2r_step1.json`, {WL['files_with_1_to_7_of_50'].get('data/configs/b2r_step1.json', 0)}; section 4); counts and paths in section 1; these run artifacts, configs and harness files remain if `b2_concepts.json` is replaced",
         "github.com/safety-research/introspection-mechanisms (`experiments/01_concept_injection.py:58`, `src/vector_utils.py:448`); not printed in the paper; origin per the paper's App. B.1: Lindsey (2025), transformer-circuits.pub/2025/introspection, which prints both lists (fetch-tool comparison: concepts "
         f"{lz['concept_list_vs_record']}; baseline {lz['baseline_list_vs_record']})",
         f"`{MACAR_PIN}`; Lindsey page: no version pinned",
         f"**none** from the repository (no LICENSE at the pin or on main; API `license: null`; README: research-use statement); not covered by the paper's {plic} (not printed there); Lindsey (2025): no license statement on the page, nor a site-wide one on the site's home page (round-4 read) **[to confirm]**",
         "**not stated**: no grant found",
         "Attribute to Macar et al. 2026 (repo + pinned sha; BibTeX key `macar2026mechanisms`) and to Lindsey (2025), *Emergent Introspective Awareness in Large Language Models* (the record cites it nowhere today); **the PI decides** whether to ship, ask the authors, or link instead"),
        ("Detection-behavioral harness (port of Macar's paradigm)",
         "`valence_core/detection.py`, `detection_v2.py`, `scripts/box_b2*.py`, `b2*_analyze.py`; also building Macar prompts at run time: "
         + (", ".join(f"`{p}`" for p in extra_builders) or "none") + " (section 1)",
         f"lab reimplementation of the paradigm; {len([n for n in shared_macar if n not in GENERIC_NAMES])} non-generic function names shared with their two files; keyword scorer vs their LLM judge",
         "n/a (cites `5d5d9b4`)", "lab's own code (see the repository row)", "per the repo's license",
         f"Two sentences: \"Reimplements the concept-injection paradigm of Macar et al. (2026), which follows Lindsey (2025). The prompt text is transcribed from their code repository; the same text is printed in their paper ({plic}) and appeared earlier in Lindsey (2025); the word lists are from their code repository.\""),
        ("jlens-qwen36 (J-lens / MLX stack, Qwen oracle)",
         f"`jlens-qwen36/` (gitignored; tracked paths: {n_tr_head} at HEAD, {n_tr_hist} in any commit; {jl_tracked}); imported at run time by `valence_core/adapters/qwen_mlx.py` etc.",
         f"github.com/WeZZard/jlens-qwen36 (clone commit `{JLENS_CLONE_COMMIT[:12]}`; itself an MLX port of github.com/anthropics/jacobian-lens, Apache-2.0, section 2e)",
         f"`{JLENS_CLONE_COMMIT}`", "Apache-2.0 (Copyright 2026 WeZZard)",
         f"yes, under Apache-2.0 terms; copy check: {jl_red}",
         "Name it as an external dependency with URL, commit and license, and its upstream anthropics/jacobian-lens; say the lab's cycle-1-4 code lives in the local clone as untracked additions (not in the public repo); one demo prompt was borrowed from it (section 2e)"),
        ("Anthropic, *Verbalizable Representations Form a Global Workspace in Language Models* (July 2026): the J-lens program's founding citation",
         f"cited with title and links at {', '.join(OT['global_workspace']['setup_doc_locators']) or '[not found]'}; referred to without title or link at {', '.join(OT['global_workspace']['readme_locators']) or '[not found]'}; the cycle-1 raws of the upstream `run_experiments.py` ({len([r for r in OT['global_workspace']['cycle1_raws_by_command'] if r['class'] == 'upstream'])} files) replicate its figures",
         "transformer-circuits.pub/2026/workspace/index.html; www.anthropic.com/research/global-workspace",
         "n/a", "**not read by this part [to confirm]**",
         "no paper text or figure identified in the record (not compared); the raws carry the upstream script's one-line prompts (de minimis; Apache-2.0 upstream)",
         "Cite it as the program's origin with its full title and link (the README refers to it without either); no attribution of reproduced material needed unless the PI's comparison finds some"),
        ("Jacobian lenses for Qwen3.6-27B: Neuronpedia n=1000 (the primary lens, cycles 1-4) and the jlens-qwen36 `v0.2-fulldepth` release lens (n=20)",
         f"not tracked (local clone `jlens-qwen36/data/lens/`: `neuronpedia_n1000.npz`, `lens.npz`, {LN['on_disk']['lens.npz']} bytes each); lens paths in any commit: {len(LN['lens_paths_any_commit'])}",
         "huggingface.co/neuronpedia/jacobian-lens (`qwen3.6-27b/jlens/Salesforce-wikitext/...n1000.pt`, converted locally per upstream `docs/lenses.md`); github.com/WeZZard/jlens-qwen36 release `v0.2-fulldepth` (`v0.1-demo` named in the setup doc)",
         f"**none declared**; HF repo sha at the read `{np_hf['sha'][:12]}...` (modified after the acquisition); release tag `v0.2-fulldepth`",
         "MIT (HF card); release assets: no license statement in the release bodies, the repository is Apache-2.0 [to confirm that it covers the assets]",
         "none redistributed",
         "Credit the lens as the record does (" + (", ".join(rl.get("mit_and_credit", [])) or "archive/RESULTS-cycle1-2.md") + " and the next line); state that the cycle 1-4 J-lens readouts used it; say the lenses are not in the repo"),
        ("OLMo 3 / 3.1 32B lineage (Base, SFT, DPO, Instruct)",
         "not tracked (weights on the box volume); ids + revisions in `data/olmo/manifest.json`",
         "huggingface.co/allenai/{Olmo-3-1125-32B, Olmo-3.1-32B-Instruct-SFT, -DPO, Olmo-3.1-32B-Instruct}",
         "`c2b61dae89a1` / `152782ecc41a` / `fc84a4f69991` / `ac0587e4a774` (manifest)",
         "Apache-2.0 (each card)", "yes for the weights under Apache-2.0; none are redistributed",
         "List the four ids + revisions + Apache-2.0"),
        ("Qwen3.6-27B, 4-bit MLX",
         "not tracked (laptop HF cache)", "huggingface.co/mlx-community/Qwen3.6-27B-4bit (base Qwen/Qwen3.6-27B)",
         f"**none declared**; `c000ac2c2057` appears in {len(q_pin_files)} raw logs' cache paths and is the laptop cache's `refs/main`", "Apache-2.0 (card; base card Apache-2.0)",
         "yes; none redistributed", "Name id, base model, license; pin `c000ac2c2057...` as the revision run, if the PI accepts the local cache as the source"),
        ("Task corpora and stimulus files (e0 tasks, e2a tasks, e0 frames/probes, f pools, rosters, vignettes, neutral prompts, audit/ban lists)",
         "`data/corpus/*.jsonl`, `data/configs/*` except b2_concepts/b2_framing, `data/f/pools.json`, `data/format/neutral_label_selection.json`",
         f"lab-authored (Code-proposed / design-approved per their `_doc`/`_status` fields; e0/e2a corpora per archive/RESULTS-cycles3-4.md@{LOC[:7]}:1590-1599, :1294)",
         "n/a", "lab's own (repository license)", "per the repo's license",
         "One sentence: stimuli are the lab's own except the Macar materials"),
        ("C4 (`allenai/c4`, `en`), streamed once as a fallback residual corpus (cycle 1-2 basis-sensitivity diagnostic)",
         f"not tracked; its raw `{c4raw}` holds statistics only (Code's read)",
         "huggingface.co/datasets/allenai/c4, via upstream `jlens_qwen/prompts.py` (section 2e)",
         f"none (streamed); HF sha at the read `{c4['sha'][:12]}...`",
         f"{', '.join(c4['cardData_license'])} (HF card)", "none redistributed",
         "Optional: one line naming it"),
        ("Runtime libraries (" + ", ".join(OT["third_party_imports"]) + ")",
         f"not vendored ({len(OT['vendored_paths'])} vendored paths in any commit); no dependency manifest tracked ({len(OT['dependency_manifests_any_commit'])} in any commit)",
         "their own projects (not read)", "none in a manifest (none tracked)",
         "not read by this part", "none redistributed",
         "Optional: list them with versions"),
        ("Model-generated transcripts and run artifacts",
         "`data/**`, `results/raw/**`", "outputs of the models above on the lab's prompts (and Macar's framing in the B2 fidelity arm)",
         "n/a", "model outputs; output terms not read beyond the card license field", "[to confirm] by the PI if wanted",
         "One sentence naming them as model outputs"),
        ("This repository",
         "root", "the lab", "the tag (PI's)",
         *((lic_summary + f" (section 5; added at {lic_added_s})",
            "**yes**, under those licenses; third-party material keeps its own terms (rows above"
            + (f"; `LICENSING.md:{lmap['third_party_heading_line']}`" if lmap and lmap['third_party_heading_line'] else "")
            + ")",
            "Name the license files and `LICENSING.md`")
           if repo_licensed else
           ((f"root-level license text(s) for the PI to read: {lic_open_s} (section 5)",
             "**PI reads them** (section 5)", "**PI decides** what the README says")
            if lic_texts else
            (f"**no root-level license text** ({len(lic_texts)} at the commit under section 5's "
             f"root-level rule; section 5's exact-name count, any depth, NOTICE included: "
             f"{len(lf_head)} at the commit, {len(lf_hist)} ever added)",
             "**not granted** (default: all rights reserved)",
             "**PI decides** a license (or none) before the repo goes public")))),
    ]
    for r in rows:
        P("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")
    P("")
    R["table"] = [dict(zip(["material", "location", "source", "pinned_sha", "license",
                            "redistribution_ok", "action_for_readme"], r)) for r in rows]

    # =====================================================================
    # 7. PI decisions, redactions, pass line
    # =====================================================================
    P("## 7. For the PI")
    P("")
    P(f"1. **Macar materials: two sources, decided per item.** (a) *Prompt text* (framing, "
      f"\"Ok.\" acknowledgement, trial question, extraction template). The code repository it was "
      f"transcribed from has no license, but the same text is printed in the paper, "
      f"arXiv:2603.21396 (App. A Table 4; the template in App. B.2), which arXiv lists under "
      f"**{plic}**. The same framing, \"Ok.\" and trial question appeared earlier, on the "
      f"Lindsey (2025) page ({lz['date']}; fetch-tool comparisons: framing "
      f"{lz3['framing_sentences_identical_to_record'][0]} of "
      f"{lz3['framing_sentences_identical_to_record'][1]} sentences identical; its trial turn "
      f"adds a lead-in sentence the record and the paper do not have), which states no license. "
      f"So the {plic} grant for the text comes only from the later paper, whose authors include "
      f"Lindsey. It can ship with attribution under {plic} if the PI judges that grant "
      f"sufficient for text its co-author published first; the README credits Lindsey (2025) "
      f"as the earlier publication either way. A byte-level comparison with the paper's text is "
      f"[to confirm] (the fetch-tool comparisons found the same text as rendered, with a "
      f"different placeholder name: the round-2 fixer's read compared the first and last eight "
      f"words, sentence count, approximate length, punctuation and turn order; the round-2 "
      f"checker's and the round-3 fixer's reads the whole wording, sentence by sentence). "
      f"(b) *The 50 concepts and the 100 baseline words.* They are "
      f"not printed in the paper, so its {plic} does not cover them; the repository grants "
      f"nothing; the paper's App. B.1 credits the concepts to **Lindsey (2025)**, *Emergent "
      f"Introspective Awareness in Large Language Models* (Anthropic, Transformer Circuits "
      f"Thread), whose page prints both lists and states no license (whole page read; the "
      f"site's home page states none either, round-4 read) **[to "
      f"confirm]**. Per block line 80 the README attributes and **the PI decides** for (b): keep "
      f"them with attribution to Macar et al. and Lindsey (2025), ask the authors, or replace the "
      f"file with a pointer to the pinned sha and the Lindsey page; a pointer would leave the "
      f"approved eight in {len(wl_other8)} `data/olmo/` JSON artifacts and {len(wl_npz8)} `.npz` "
      f"member-name sets, and 1-7 of the 50 in {len(WL['files_with_1_to_7_of_50'])} files "
      f"(section 1). (c) The record cites Lindsey "
      f"(2025) nowhere ({len(lind_head)} tracked files, {len(lind_hist)} paths in any commit); "
      f"the README should add it. Not a STOP: block line 85's pass is \"licenses recorded\". "
      f"Whatever is chosen for HEAD, the framing has been in the history since "
      f"`{S1['framing_marker_first_commit']}` ({len(fr_hist)} paths ever carried it) and the "
      f"lists since `{S1['data/configs/b2_concepts.json']['first_added']}`, so only a history "
      f"rewrite would take them out of the published record (section 1).")
    if repo_licensed:
        P(f"2. **The repository's own license is recorded** (section 5): {lic_summary}; added at "
          f"{lic_added_s}. No license decision is open here (the README action is in section 6's "
          f"last row); the third-party items (1, 3, 4, 5 and 7) keep their own terms.")
    elif lic_texts:
        P(f"2. **The repository carries license text(s) this part does not record as its license** "
          f"(section 5): {lic_open_s}. The PI reads them before publication.")
    else:
        P("2. **The repository has no license.** The PI chooses one, or none, before publication.")
    P(f"3. **jlens-qwen36 is Apache-2.0**; tracked paths under it: {n_tr_head} at HEAD, "
      f"{n_tr_hist} in any commit; {jl_tracked}; copy check: {jl_red}. The public repo depends on it "
      "at run time for the Qwen oracle, and on the lab's untracked additions inside the clone; the "
      "README can say the Qwen oracle path is not runnable from the public repo alone (N11 covers "
      "the model-free regression suite).")
    P("4. **All five models are Apache-2.0 on their cards**; no weights are tracked at HEAD (the "
      "history check is the other part's). The record declares no Qwen revision; the laptop's "
      "cache revision (also visible in raw-log cache paths) is available for the README.")
    P(f"5. **The Jacobian lenses** (Neuronpedia n=1000, MIT; the jlens-qwen36 release lens) were "
      f"the primary Qwen lens through cycles 1-4 and are not tracked "
      f"({len(LN['lens_paths_any_commit'])} lens paths in any commit). Not a release blocker; the "
      f"README credits them (section 2d).")
    P("6. **Refs not visible locally.** This part read the local refs only; the PI may run "
      "`git ls-remote origin` before changing visibility, to see any server-side branch or "
      "pull-request ref that would also be published (section 5).")
    gwf = OT["global_workspace"]
    P("7. **The Global Workspace paper** (Anthropic, July 2026) is the program's founding "
      "citation and had no row; it now has one (section 6). The README refers to it "
      + ("without its title or a link" if not (gwf["readme_gives_title"] or gwf["readme_gives_link"])
         else f"(title given: {gwf['readme_gives_title']}; link given: {gwf['readme_gives_link']})")
      + ", so the README-for-readers gives the full citation. Its license was not "
      "read and the "
      "record was not compared with it [to confirm]; the cycle-1 raws carry an Apache-2.0 "
      "upstream script's outputs and one-line prompts (section 2e).")
    P(f"8. **Moving HEAD.** These counts are bound to `{head[:7]}` (the record locators are "
      f"pinned to `{LOC[:7]}`); re-run this script at the final pre-flip commit (header). At "
      f"that commit this audit's own files are tracked, and section 2f's projection finds "
      f"{len(pj_ids)} id(s) and {len(pj_hosts)} host(s) in the audit files on disk at this run, and "
      f"the closing self-check @@L3SELF@@ in this raw's own text (together @@L3COMB@@), that the "
      f"sweeps would leave unclassified@@L3VERDICT_8@@ Audit raws written after this run are the "
      f"re-run's to check.")
    P("")
    P(f"Redactions: **{len(REDACTIONS)} pattern redactions** (redact(): IPv4, tokens, keys)"
      + ("" if not REDACTIONS else " -- " + "; ".join(f"{r['where']} {r['category']} {r['redacted']}" for r in REDACTIONS))
      + f"; **{len(REDACTED_IDS)} third-party repository id(s) printed redacted** by rule"
      + ("" if not REDACTED_IDS else " (" + "; ".join(f"{r['where']}: `{r['redacted']}`" for r in REDACTED_IDS) + ")")
      + f"; IP-literal URL hosts counted and not printed: {len(ip_rows)}.")
    R["redactions"] = REDACTIONS + REDACTED_IDS
    R["redaction_counts"] = {"pattern": len(REDACTIONS), "redacted_ids": len(REDACTED_IDS),
                             "ip_hosts_not_printed": len(ip_rows)}
    P("")
    # pass line: gated on the conjuncts the recording rests on (block identity, the
    # Macar pin, the clone's copy check at HEAD and over history, the sweep's coverage).
    # Absent licenses are not a failure condition (block line 80).
    HCg = J.get("history_copy_check", {}) if J.get("present") else {}
    gates = {
        "block sha256 and 141 lines": blk_ok and len(blk_lines) == 141,
        "Macar pin equals the recorded commit": pin_ok,
        "jlens-qwen36 clone present (HEAD copy check ran)": bool(J.get("present")),
        "upstream object store read (sha-verified)": bool(UP.get("ok")),
        "history-wide copy check ran": bool(HCg.get("ran")),
        "external-reference sweep: 0 unclassified ids": n_uncl == 0,
        "URL-host sweep: 0 unclassified hosts": n_host_uncl == 0,
    }
    failed = [k for k, v in gates.items() if not v]
    R["pass_gates"] = gates
    n_rows = len(rows)
    HIST_RAW = "results/raw/2026-10-08_note-N12-history.md"
    hist_raw_fp = os.path.join(REPO, HIST_RAW)
    hist_raw_heading = (os.path.isfile(hist_raw_fp) and "## (iv) mechanical checks" in
                        open(hist_raw_fp, encoding="utf-8", errors="replace").read())
    R["history_raw_iv_heading_present"] = hist_raw_heading
    if not failed:
        P(f"**(iv) licenses recorded** -- for the {n_rows} rows of section 6 (the third-party "
          f"materials and models found by section 2a's marker grep, section 4's stimulus scan, "
          f"section 2f's external-reference and host-agnostic URL sweeps over HEAD and history, "
          f"the paper's own citations (Lindsey 2025), and the record's acquisition entries for the "
          f"lenses and the C4 fallback), the source, the pin or its absence, and the license are "
          f"recorded above, at `{head[:7]}`. Open for the PI: the Macar prompt text is "
          f"{plic} via the paper (the PI accepts that source or not; the text appeared earlier, "
          f"with no license stated, in Lindsey 2025), the two word lists have no "
          f"license found (the README attributes Macar et al. and Lindsey 2025; the PI decides), "
          + (f"and the Global Workspace paper's license was not read. The repository's own "
             f"license is recorded in section 5 ({lic_summary}). " if repo_licensed else
             (f"the Global Workspace paper's license was not read, and the repository's "
              f"root-level license text(s) are for the PI to read (section 5: {lic_open_s}). "
              if lic_texts else
              f"the Global Workspace paper's license was not read, and the repository has no "
              f"LICENSE file. "))
          + f"jlens-qwen36: {jl_tracked}; copy check: {jl_red}. Macar port: "
          f"{len([n for n in shared_macar if n not in GENERIC_NAMES])} non-generic function names "
          f"shared with their code ({len(shared_macar)} counting generic names: {shared_macar}); "
          f"their stimulus text is carried verbatim. (iv)'s `.npz`-allowlist and model-weights "
          f"clause: see `{HIST_RAW}`, section \"(iv) mechanical checks\" (heading present on disk "
          f"at this run: {hist_raw_heading}).")
        R["pass_line"] = "(iv) licenses recorded"
    else:
        P(f"**(iv) NOT recorded** -- failed conjunct(s): {'; '.join(failed)}.")
        R["pass_line"] = "(iv) NOT recorded: " + "; ".join(failed)

    # =====================================================================
    # Values-check (the checker's findings on the builder's run, and their disposition)
    # =====================================================================
    UPv = J.get("upstream_object_store", {}) if J.get("present") else {}
    VC = [
        ("1 (substantive)", "Pass line / section 6 overclaimed 'every third-party material': the "
         "Jacobian lenses (Neuronpedia n=1000, MIT; jlens-qwen36 release lenses) had no row.",
         "ACCEPTED, fixed. Section 2d and a section-6 row added, from the record's locators "
         f"({len(sum(rl.values(), []))} asserted by content), the on-disk sizes, the upstream "
         "docs (object store), and two fixer WebFetch reads (HF card: MIT; releases: the "
         "v0.2-fulldepth parts sum to the on-disk lens.npz size: "
         f"{LN['lens_npz_equals_v02_parts_sum']}); lens paths in any commit: "
         f"{len(LN['lens_paths_any_commit'])}. The pass line now names the rows and how they were "
         "found, and section 2f adds a HEAD+history external-reference sweep so the set is "
         "grounded by a tool run rather than by recall."),
        ("2 (minor)", "Section 2b said whether ACK (\"Ok.\") is theirs is not stated.",
         "ACCEPTED, fixed. The record states it: "
         + (", ".join(S1["ack_record_locator"]) or "[not found]")
         + " (located by content, so the locator survives RESULTS.md's newest-first drift). ACK "
         "added to the section-6 Macar framing row."),
        ("3 (minor)", "The jlens-qwen36 row did not name its upstream, anthropics/jacobian-lens.",
         "ACCEPTED, fixed. Section 2e and the row's source cell name it, with the record's "
         "locators and a fixer WebFetch read of the GitHub API (Apache-2.0)."),
        ("4 (minor)", "Section 2c's 'may carry local edits' was unquantified, and the copy check "
         "was HEAD-only while the release publishes history.",
         "ACCEPTED, fixed in the script (not by citation). The clone's .git/index and object "
         "store are parsed as files (no git process in the clone; every object's sha1 "
         f"re-verified): {UPv.get('n_index_entries')} index entries, "
         f"{len(UPv.get('on_disk_differs_from_index', []))} differing on disk "
         f"({', '.join(UPv.get('on_disk_differs_from_index', []))}); the upstream side of the "
         "comparison is now the committed upstream blobs, not the on-disk copies. A history-wide "
         f"check over {HI['n_commits']} commits / {HI['n_distinct_blobs']} distinct blobs is in "
         f"section 2c: non-empty upstream blobs in any commit "
         f"{len(HCg.get('upstream_nonempty_blobs_in_history', [])) if HCg.get('ran') else '[not run]'}"
         f", near-copies >= 0.5 "
         f"{HCg.get('near_copy_counts', {}).get(0.5, '[not run]') if HCg.get('ran') else '[not run]'}"
         f" (best {HCg['near_copy_top'][0]['jaccard'] if HCg.get('near_copy_top') else 'n/a'}; "
         "the checker's independent figure was 0.131)."),
        ("5 (minor)", "Header line 4, 'every repository read is at this commit', overclaimed.",
         "ACCEPTED, fixed. The header now separates tracked content (at the commit), history "
         "scans (all local refs), and the on-disk reads (block, clone, HF cache)."),
        ("6 (minor)", "The pass line was hard-coded.",
         "ACCEPTED, fixed. It is gated on the block identity, the Macar pin, the clone's "
         "presence, the object-store read, the history check and the sweep's coverage; absent "
         "licenses do not gate it (block line 80). Gates: "
         + "; ".join(f"{k}: {v}" for k, v in gates.items()) + "."),
        ("7 (minor)", "Section 5's 'no grant to reuse it' ignored GitHub's ToS view-and-fork grant.",
         "ACCEPTED, fixed, from a fixer WebFetch read of the ToS page (section D.5, recorded as a "
         "summary, not verbatim); the same read's note on posting others' content is linked to "
         "the Macar item."),
        ("8 (minor)", "The 22 unscanned files included 3 tracked .log raws, unstated.",
         f"ACCEPTED, fixed. `.log` added to the text extensions ({R['n_text_files_scanned']} "
         f"scanned now); the {len(unscanned)} still unscanned are listed in the header."),
        ("9 (minor)", "The raw did not say it is an input to the block's N12 output.",
         "ACCEPTED, fixed. Header line 3."),
        ("missed: remote refs", "Server-side refs (refs/pull/*, unfetched branches) cannot be "
         "seen locally.", "ACCEPTED as a PI note (section 5, section 7 item 6). `git ls-remote` "
         "was not run here (network and stored credentials)."),
        ("missed: runtime libraries", "mlx, mlx-lm, transformers, torch, numpy not listed.",
         "ACCEPTED as an optional row; the module list is computed from the tracked code's "
         "imports, with manifest and vendoring counts (section 2e)."),
        ("missed: C4 fallback", "C4 used once via the upstream loader; optional row.",
         "ACCEPTED, row added (section 2e), with a fixer WebFetch read of the dataset card "
         "(ODC-BY)."),
        ("missed: demo prompt", "One C one-liner borrowed from the jlens-qwen36 demo.",
         "ACCEPTED, recorded as de minimis in section 2e and the jlens row."),
        ("checker items not adopted", "None of the checker's findings was rejected.",
         "Two refinements of the suggested fixes: the lens location cell keeps the on-disk byte "
         "sizes the script measures; the history check is run in this script rather than cited "
         "from the history part's raw. Locators, found by content: the anthropics/jacobian-lens "
         "line is "
         + (", ".join(OT["anthropic_upstream_locators"][:1]) or "[not found]")
         + " (the checker wrote :18 and :21; the 'community MLX port' line is "
         + (", ".join(OT["anthropic_upstream_locators"][1:]) or "[not found]")
         + "); the lens credit is on "
         + (", ".join(rl.get("mit_and_credit", [])) or "[not found]")
         + " and the line after it (the checker wrote :35-36)."),
    ]
    lzr = WEB_READS["lindsey_2025_page"]["result"]
    VC2 = [
        ("1 (substantive)", "Sections 1, 6, 7 treated the Macar framing, ack and trial question "
         "as unlicensed; the same text is in arXiv:2603.21396 App. A Table 4 under CC BY 4.0, and "
         "App. B.1 credits the 50 concepts to Lindsey (2025), which the record never cites.",
         "ACCEPTED, fixed, after Code's own WebFetch reads (abs page: "
         f"{WEB_READS['macar_paper_arxiv_abs']['result']['license_label']}; the HTML rendering read "
         "whole; the Lindsey page read whole). Section 1 has a paper paragraph and a word-lists "
         "paragraph; section 6 splits the Macar rows into the prompt text "
         f"({plic} via the paper, redistributable with attribution if the PI accepts that source) "
         "and the two word lists (no license found; PI decides); section 7 item 1 and the pass "
         "line are rewritten per item; Lindsey (2025) is added to the attribution, with "
         f"{len(lind_head)} citations of it in the record at the commit. Two refinements of the "
         "suggested fix: (a) App. B.2 does print the extraction template, so the template moves "
         "with the prompt text; (b) the Lindsey page, read past the first 100k characters, does "
         f"print both lists ({lzr['concept_list_vs_record']}; baseline "
         f"{lzr['baseline_list_vs_record']}; fetch-tool comparisons) and its trial prompt; it "
         "states no license (whole page read), so its license stays [to confirm]. No quote of the "
         "paper's text is added to the raw."),
        ("2 (minor)", "Section 2f's sweep matched only github/huggingface/arXiv forms; a "
         "host-agnostic sweep finds the Global Workspace paper (transformer-circuits.pub, "
         "anthropic.com), the J-lens program's founding citation, with no row.",
         f"ACCEPTED, fixed. Section 2f adds a host-agnostic URL sweep (HEAD + history; "
         f"{sum(1 for s in HS if s['kind'] == 'host')} hosts, {len(ip_rows)} IP-literal host(s) "
         f"counted and not printed, {n_host_uncl} unclassified; gated in the pass line). Section "
         f"2e and section 6 add the Global Workspace row; the cycle-1 raws of the upstream "
         f"`run_experiments.py` ({len(gw_up)}) are recorded as outputs of an Apache-2.0 upstream "
         "script with one-line prompts. The model-output hosts are classed as not materials, "
         "checked by their carrier paths. Hosts beyond the checker's six: "
         + (", ".join(f"`{s['host']}`" for s in HS if s["kind"] == "host" and s["host"] not in
                      ("github.com", "huggingface.co", "transformer-circuits.pub",
                       "www.anthropic.com", "www.constellations.blog", "simple.wikipedia.org"))
            or "none") + "."),
        ("3 (minor)", "The trial-question count (20) is an exact-line lower bound; 2 more files "
         "carry it wrapped or escaped; the counts exclude this audit's own files.",
         f"ACCEPTED, fixed. Section 1 counts on single lines ({len(tq_files)}, a lower bound) and "
         f"after undoing wraps and escapes (+{len(tq_norm)}: "
         + ", ".join(tq_norm) + f"; {len(tq_files) + len(tq_norm)} in all), with history "
         f"(+{len(tq_hist_norm)} paths), and states that this audit's untracked files "
         f"({len(own_tq)} carrying the question at this run) are excluded and would raise the "
         "counts once committed."),
        ("4 (minor)", "Section 2a printed the third-party pattern with `Macar` while the script "
         "uses `\\bMacar\\b`; the harness row missed two run-time `MACAR_FRAMING` users.",
         f"ACCEPTED, fixed. 2a prints the pattern as implemented and the unbounded count "
         f"({n_third_unb} lines, {n_extra} more, all identifier lines). Section 1 lists the "
         f"run-time prompt builders by AST ({len(builders)} files); the harness row adds those "
         f"outside its globs: {', '.join(extra_builders)}. Outside the globs and not named by "
         "the checker: "
         + (", ".join(p for p in extra_builders if p not in ("scripts/box_a2_baserates.py",
                                                              "scripts/box_cached_gen_smoke.py"))
            or "none") + "."),
        ("5 (minor)", "Section 2d's size match cannot identify lens.npz: the v0.3 asset and the "
         "Neuronpedia conversion have the same size.",
         f"ACCEPTED, fixed. 2d reads both local .npz zip directories and .npy headers (same "
         f"layout: {LN['same_layout']}; n_prompts {lay_a and lay_a.get('int_scalars', {}).get('n_prompts.npy')} "
         f"vs {lay_b and lay_b.get('int_scalars', {}).get('n_prompts.npy')}), records the checker's "
         f"v0.3 read (sum {v03_sum}, equal: {LN['lens_npz_equals_v03_parts_sum']}), says the size "
         "identifies the layout, not the lens, and rests the identification on the record's "
         "locators, consistent with the file's own n_prompts."),
        ("6 (minor)", "'Redactions applied: 0' contradicted the redacted SAE id in section 2f.",
         f"ACCEPTED, fixed. The line now reports {len(REDACTIONS)} pattern redactions and "
         f"{len(REDACTED_IDS)} redacted id(s) separately, and the JSON `redactions` list carries "
         "both, with `redaction_counts`."),
        ("7 (minor)", "The jlens row, section 7 item 3 and the pass line said only 'tracked paths "
         "0', omitting the 39 byte-identical lab files; the npz/weights clause is in another raw.",
         f"ACCEPTED, fixed: \"{jl_tracked}\" is in the jlens row, item 3 and the pass line; the "
         f"pass line points to `{HIST_RAW}`, section \"(iv) mechanical checks\", by heading, not "
         "line number, since that raw is being revised in parallel."),
        ("8 (minor)", "The history scans were bound to bbc9ffe; HEAD has moved.",
         f"ACCEPTED, fixed. The round-2 fixer re-ran at `bab921c` (this run: `{head[:7]}`); the "
         f"header names the commit(s) after the block's commit ({len(since)} at this run) and "
         "requires a re-run at the final pre-flip commit; section 7 "
         "item 8 repeats it. The round-2 re-run surfaced one new port-marker row from those commits, "
         "`valence_core/m/gcal.py:856` (\"not a port of it\"), now read in 2a's table (asserted: "
         + str(next((r["asserted"] for r in read_rows if r["loc"] == "valence_core/m/gcal.py:856"),
                    "[row absent]"))
         + f"; uncovered rows now: {R['marker_grep']['no_file_rows_uncovered'] or 'none'}). The "
         "other new content was not reviewed beyond these sweeps."),
        ("9 (minor)", "'a one-sentence trial question' is wrong: it is two sentences.",
         f"ACCEPTED, fixed. The count is computed ({n_tq_sent} sentences)."),
        ("checker's missed items", "Independent re-derivations (refs, commits, paths, blobs, "
         "npz, licenses, copy check) agreed with the raw.",
         "No change needed; the counts at the new commit are recomputed above."),
    ]
    # ---- round 3 -------------------------------------------------------------------
    ack_at_head = [i for i in find_line(text.get("RESULTS.md", ""), 'assistant "Ok."')
                   if "(framing)" in text.get("RESULTS.md", "").splitlines()[i - 1]]
    dl_txt = ", ".join(f"`{s_['host']}` ({s_['class']}; carriers "
                       + ", ".join(f"`{c}`" for c in s_["carrier_paths"]) + ")" for s_ in dl_rows)
    chk_npz = sorted(wl_npz8) == sorted(f"data/olmo/b2{x}_concepts_{st}.npz" for x, st in
                                        [("", "base"), ("", "dpo"), ("", "instruct"), ("", "sft"),
                                         ("r", "base")])
    VC3 = [
        ("1 (minor)", "Section 1 said the Lindsey page's framing was not compared with the record; "
         "the page prints the same framing, 'Ok.' and trial question, so the prompt text first "
         "appeared there, with no license; the section 6 row, section 7 item 1(a) and the README "
         "sentence named only the paper, and 'quoted from their paper' misstates provenance (the "
         "record transcribed it from the repository).",
         f"ACCEPTED, fixed, after the round-3 fixer's own WebFetch reads (the Lindsey page at "
         f"offsets 300000, twice, and 400000; the paper's HTML Table 4). Lindsey page: framing "
         f"{lz3['framing_sentences_identical_to_record'][0]} of "
         f"{lz3['framing_sentences_identical_to_record'][1]} sentences identical, the reply equals "
         f"`ACK`: {lz3['assistant_reply_equals_record_ACK']}, the trial line equals the record's "
         f"apart from the number: {lz3['trial_line_equals_record_apart_from_number']}, license "
         f"statement from character 300,000 to the end: "
         f"{lz3['license_or_terms_statement_300000_to_end'] or 'none'}. One difference the checker did not report: the "
         f"page's second Human turn opens with a lead-in sentence before the trial line, which the "
         f"paper's Table 4 lacks (round-3 read: {not pT['second_user_turn_contains_lindsey_lead_in']}) "
         f"and the record lacks ({len(lead_in_files)} tracked files carry it), so the record's "
         f"form is the paper's. Table 4, compared sentence by sentence: "
         f"{pT['framing_sentences_identical_to_record'][0]} of "
         f"{pT['framing_sentences_identical_to_record'][1]} identical. Section 1 (paper and word-"
         "list paragraphs, and its Reading), section 2b, section 2f's class for the paper's arXiv "
         "id, the section-6 prompt-text row (source, "
         "pin, license, redistribution and action cells), section 7 item 1(a) and the pass line now "
         "say the text appeared earlier on the Lindsey page with no license stated, that the CC BY "
         "4.0 grant comes only from the later paper whose authors include Lindsey, and that the PI "
         "judges whether that suffices. The README sentence now reads 'transcribed from their code "
         "repository; the same text is printed in their paper (CC BY 4.0) and appeared earlier in "
         "Lindsey (2025)'. Refinement: 'appeared earlier' and 'first, of the sources read' rather "
         "than 'first appeared', since only three sources were read (the page "
         f"{lz['date']}, the repository created "
         f"{S1['prompt_text_first_publication']['macar_repo_created']}, the paper's v1 "
         f"{S1['prompt_text_first_publication']['macar_paper_v1']})."),
        ("2 (minor)", "The header attributed every commit after the block's commit to 'the "
         "concurrent PROPOSAL-m session, not by this audit', unconditionally; at the required "
         "pre-flip re-run the audit's own end commit would be mislabelled.",
         "ACCEPTED, fixed. The header now describes each later commit by data: paths changed and "
         "how many of them are this audit's files (`scripts/audit_note_*`, "
         "`results/raw/<date>_note-*`, `AUDIT-note-*`, `README-NOTE.md`), plus the number of later "
         f"commits that touch such files ({n_since_audit} of {len(since)} at this run: "
         + "; ".join(f"`{x['commit'][:7]}` {len(x['audit_paths'])} of {x['n_paths']}"
                     for x in since_info)
         + "). No session is named; the code comment on the round-2 reading row is neutral in "
         "the same way. The JSON field `commits_after_block_commit` carries the per-commit "
         "paths count and audit paths."),
        ("3 (minor)", "The concept-list row's location named only `b2_concepts.json` and 4 words "
         "in `b2r_step1.json`; the approved eight are also in 16 more tracked files and in .npz "
         "member names, and would remain if `b2_concepts.json` were replaced.",
         f"ACCEPTED, fixed. Section 1 adds a computed paragraph: files with >= 20 of either list: "
         f"{len(WL['files_with_ge20_of_50_or_100'])} (`b2_concepts.json`); all eight approved "
         f"concepts as quoted strings in {len(wl_other8)} other files (the checker's 16: "
         f"{len(wl_other8) == 16}; by directory {wl_other8_dirs}); as member names in "
         f"{len(wl_npz8)} of {WL['n_npz_read']} tracked `.npz` files (the four "
         f"`b2_concepts_*.npz` and `b2r_concepts_base.npz`: {chk_npz}); 1-7 of the 50 in "
         f"{len(WL['files_with_1_to_7_of_50'])} files; baseline words in any other file: "
         f"{len(wl_base_other)}. The section-6 row's location cell and section 7 item 1(b) say the "
         "subsets remain if the file is replaced by a pointer; whether single words need "
         "attribution is left to the PI."),
        ("4 (minor)", "Section 2f's 'any http(s):// host' sweep dropped URL hosts without a dot.",
         f"ACCEPTED, fixed. hosts_in() now counts dotless URL hosts as their own kind, classed by "
         f"carrier path (inside model text if every carrier is under `data/olmo/`; `localhost` as a "
         f"loopback name; otherwise UNCLASSIFIED, which fails the pass-line gate), and prints one "
         f"only when it is a plain lowercase word in model text, otherwise redacted. At this run: "
         f"{len(dl_rows)} dotless host(s){': ' + dl_txt if dl_rows else ''}; unclassified hosts of "
         f"any kind: {n_host_uncl}. The checker's one dotless host is "
         f"{'among them' if any(s_['host'] == 'street' for s_ in dl_rows) else 'not found by this run'}."),
        ("5 (minor)", "The raw said the README 'names' the Global Workspace paper; it refers to "
         "the work without a title or link.",
         f"ACCEPTED, fixed. Section 2e, the section-6 row (location and action cells) and section 7 "
         f"item 7 say the README refers to it "
         f"({', '.join(GW['readme_locators']) or '[not found]'}; title given: "
         f"{GW['readme_gives_title']}; link given: {GW['readme_gives_link']}) and that the "
         f"README-for-readers carries the full citation; the title and both URLs are at "
         f"{', '.join(GW['setup_doc_locators']) or '[not found]'}."),
        ("routing rule (not a checker finding)", "This round's routing pins every record locator "
         "to bbc9ffe, as the other audit raws do; the round-2 raw pinned them to its commit read "
         "(bab921c), and a re-run at a later HEAD would have moved them.",
         f"APPLIED. Every `path@<sha>:<line>` locator into the record is now found by content in "
         f"the file at `{LOC[:7]}` (the block's commit; header). Example of the drift avoided: the "
         f"ACK reading is at {', '.join(S1['ack_record_locator']) or '[not found]'} and, at the "
         f"commit read, at line(s) {ack_at_head or '[not found]'} of RESULTS.md. Bare "
         "`file:line` entries produced by the scans stay at the commit read, as the header says "
         "(round 4: except section 2f's first-locator column, now pinned; Round 4, finding 1)."),
        ("checker's re-run, redaction check and HEAD note", "The checker's re-run at bab921c was "
         "identical apart from the stamp; redaction clean; HEAD moved to cf8eb5b during its check, "
         "and cf8eb5b's added lines carry no third-party markers.",
         f"No change needed beyond the re-run: this run reads `{head[:7]}`, and every count above "
         f"is recomputed there; the redaction check is re-run on this round's outputs."),
    ]
    # ---- round 4 -------------------------------------------------------------------
    # The checker's bbc9ffe lines for the six RESULTS.md first locators it named (finding
    # 1), keyed by the id's sha256 so the redacted SAE id is never written here in clear.
    chk4_lines = {sha256(b"2605.11887"): 9358, sha256(b"2606.03002"): 9377,
                  sha256(b"Qwen/MLX"): 12414,
                  sha256(b"allenai/Olmo-3.1-32B-Instruct-SFT"): 12293,
                  sha256(b"allenai/Olmo-3.1-32B-Instruct-DPO"): 12455,
                  next(iter(CLASS_BY_SHA)): 9366}
    chk4_now = {h: SW_BY_SHA.get(h, {}).get("first_locator") for h in chk4_lines}
    chk4_ok = all(chk4_now[h] == f"RESULTS.md@{LOC[:7]}:{n}" for h, n in chk4_lines.items())
    h_ins = sha256(b"allenai/Olmo-3.1-32B-Instruct")
    ins_row = SW_BY_SHA.get(h_ins, {})
    n_head_ids = len(SW) - n_hist_only
    # the word 'unlicensed' in this output's sections 1-7 and pass line (L, before the
    # Values-check): each occurrence, and whether it describes the code repository
    unl = [(i, m.start()) for i, l in enumerate(L, 1) for m in re.finditer(r"unlicensed", l)]
    unl_repo = sum(1 for i, st in unl
                   if re.match(r"unlicensed (code )?repository", L[i - 1][st:]))
    n_without = sum(l.count("without a license") for l in L)
    VC4 = [
        ("1 (minor)", "Header line 6 says bare `file:line` scan entries are at the commit read "
         "while the round-3 routing row says every record locator is pinned to bbc9ffe; section "
         "2f's first-locator column gave six RESULTS.md line numbers with no sha, correct at "
         "cf8eb5b and 295 lines off at bbc9ffe, and they would drift again at the pre-flip re-run.",
         f"ACCEPTED, fixed (the finding's first form). Each first locator is now found by content "
         f"in its file at `{LOC[:7]}` and printed `file@{LOC[:7]}:N` ({FL_STATS['pinned_at_loc']} "
         f"of the {n_head_ids} ids at HEAD; the line differs from the commit read's in "
         f"{FL_STATS['line_moved']}); where the file at `{LOC[:7]}` lacks the id, the commit read is "
         f"named, `file@{head[:7]}:N` ({FL_STATS['at_commit_read']}). The checker's six "
         f"(RESULTS.md at {LOC[:7]}: lines {', '.join(str(n) for n in chk4_lines.values())}) are "
         f"now printed as `RESULTS.md@{LOC[:7]}:<line>` with exactly those lines: {chk4_ok}. One defect the checker did not report, found while rewriting the lookup: "
         f"the old lookup took the first line containing the id as a substring, so "
         f"`allenai/Olmo-3.1-32B-Instruct` was located on a line that carries only "
         f"`allenai/Olmo-3.1-32B-Instruct-SFT` (`{FL_OLD.get(h_ins, '[row absent]')}` at the "
         f"commit read). The lookup now takes the first line on which the scan itself extracts the "
         f"id: `{ins_row.get('first_locator', '[row absent]')}` (at the commit read "
         f"`{ins_row.get('first_locator_at_commit_read', '[row absent]')}`); ids whose commit-read "
         f"line changed under the new lookup: {FL_STATS['substring_line_differed']}. The header's "
         "locator line names 2f's column as the exception to 'bare entries are at the commit "
         "read'; the 2f paragraph states the rule; the JSON rows add "
         "`first_locator_at_commit_read`."),
        ("2 (minor)", "Section 2f's class cell for arXiv 2603.21396 says the prompt text 'appeared "
         "earlier, unlicensed, on the Lindsey (2025) page', which asserts more than sections 1, 6 "
         "and 7 establish ('no license stated', '[to confirm]').",
         f"ACCEPTED, fixed: the cell now reads 'which appeared earlier, with no license stated, on "
         f"the Lindsey (2025) page'. The optional part is applied too, after the round-4 fixer's "
         f"own WebFetch read of `{WEB_READS['transformer_circuits_home_round4']['url']}` (10:59 "
         f"UTC, the whole page): license, copyright or terms statement: "
         f"{tch['license_copyright_or_terms_statement'] or 'none'}; link to one: "
         f"{tch['link_mentioning_license_copyright_terms_legal_or_reuse'] or 'none'}; agrees with "
         f"the checker's read: {tch['agrees_with_round4_checker_read']}. Section 1's Lindsey "
         "paragraph, the two section-6 Lindsey license cells and section 7 item 1(b) record it. "
         "The page's license stays [to confirm]: that neither the page nor the home page states "
         "one does not establish the terms that govern reuse. 'unlicensed' in sections 1-7 and "
         "the pass line now: "
         f"{len(unl)} occurrence(s), {unl_repo} of them describing the code repository (API "
         "`license: null`, no LICENSE file), which the checker found established. The same "
         "reading, applied by the fixer beyond the cited cell: the section-6 prompt-text row's "
         "redistribution cell said the co-author 'published first without a license'; it now says "
         f"'with no license stated' ('without a license' in sections 1-7 now: {n_without})."),
        ("3 (minor)", "JSON `web_reads_recorded.lindsey_2025_page.result."
         "trial_prompt_framing_compared_with_record` is False: true of the round-2 read it "
         "records, whose note does not name the round, but the opposite of the round-3 record "
         "when read alone.",
         "ACCEPTED, fixed (both forms). The record now carries `read_by` (\""
         f"{WEB_READS['lindsey_2025_page']['read_by']}\") and a note naming the round and the later "
         "comparison, and the field is now the string \""
         f"{lz['trial_prompt_framing_compared_with_record']}\" instead of a bare False. The "
         "round-3 record carries `read_by` too. The script reads that field nowhere, so no md "
         "text changes with it."),
        ("4 (minor)", "Routing hard rule (2) requires each script to keep `--out`/`--json-out` "
         "with the results/raw defaults; this script exposed only `--out-dir`.",
         "ACCEPTED, fixed. `--out` (default `results/raw/2026-10-08_note-N12-licenses.md`) and "
         "`--json-out` (default the `.json`) added; `--out-dir` kept as a convenience that places "
         "whichever output is not given explicitly into its directory under the default basename; "
         "naming one file for both outputs is refused. The docstring's usage line lists the three "
         "flags. Checked by the round-4 fixer's runs at the same commit (scratch `--out` + "
         "`--json-out`, scratch `--out-dir`, then the defaults): outputs identical apart from the "
         "stamp."),
        ("Code's own (not a checker finding)", "At the pre-flip re-run this audit's raws and "
         "scripts will be tracked, and the pass line gates on 0 unclassified ids and 0 "
         "unclassified hosts; the recorded-read URLs this part prints (and other items' raws) "
         "are references neither sweep has classified.",
         f"NOTED, not changed. Section 2f now projects both sweeps over this audit's own working "
         f"files with the sweeps' own rules: {len(pj_ids)} unclassified id(s) and {len(pj_hosts)} "
         f"unclassified host(s) would appear in those on disk at this run, and @@L3SELF@@ in this "
         f"raw's own text (the closing self-check; together @@L3COMB@@) ({len(pj_mine_hosts)} host(s) and "
         f"{len(pj_mine_ids) + pj_mine_ids_other} id(s) from this part's own files on disk (of the "
         f"{len(MINE)} paths it counts as its own: this script, its 2026-10-08 raws and this run's two "
         f"outputs), the hosts "
         f"and {len(pj_mine_ids)} URL-fragment id(s) printed there; "
         f"{pj_oth_hosts} host(s) and {pj_oth_ids} id(s) from the other audit files only, "
         "counted and not printed)"
         + "@@L3VERDICT_VC@@"
         + "Classifying the audit's own carriers is left to the re-run or the PI; a failing gate "
         "there is the gate doing its job. To make the projection share the sweeps' rules, the "
         "id and host classifications were moved into two functions; the classes printed above "
         "are unchanged by that move (this run's tables equal the round-3 run's apart from the "
         "first-locator column and the 2603.21396 class cell)."),
        ("open from round 3", "None.", "No change needed."),
    ]
    R["values_check"] = {"round_1": [{"finding": a, "claim": b, "disposition": c} for a, b, c in VC],
                         "round_2": [{"finding": a, "claim": b, "disposition": c} for a, b, c in VC2],
                         "round_3": [{"finding": a, "claim": b, "disposition": c} for a, b, c in VC3],
                         "round_4": [{"finding": a, "claim": b, "disposition": c} for a, b, c in VC4]}
    P("")
    P("## Values-check")
    P("")
    P("### Round 1")
    P("")
    P("An independent checker re-ran the builder's script (identical outputs apart from the stamp; "
      "redaction clean) and reported one substantive and eight minor findings plus missed items. "
      "Each finding and its disposition, as applied by the round-1 fixer (values below are "
      "recomputed at the current commit):")
    P("")
    P("| finding | claim | disposition |")
    P("|---|---|---|")
    for a, b, c in VC:
        P(f"| {a} | {b.replace('|', chr(92) + '|')} | {c.replace('|', chr(92) + '|')} |")
    P("")
    P("### Round 2")
    P("")
    P("A second checker re-ran the round-1 output (identical apart from the stamp; redaction "
      "clean) and reported one substantive and eight minor findings. Each finding and its "
      "disposition, as applied by the round-2 fixer (values recomputed at the current commit):")
    P("")
    P("| finding | claim | disposition |")
    P("|---|---|---|")
    for a, b, c in VC2:
        P(f"| {a} | {b.replace('|', chr(92) + '|')} | {c.replace('|', chr(92) + '|')} |")
    P("")
    P("### Round 3")
    P("")
    P("A third checker re-ran the round-2 output at `bab921c` (identical apart from the stamp; "
      "redaction clean) and reported five minor findings and nothing substantive. Each finding "
      "and its disposition, as applied by the round-3 fixer (values recomputed at the current "
      "commit):")
    P("")
    P("| finding | claim | disposition |")
    P("|---|---|---|")
    for a, b, c in VC3:
        P(f"| {a} | {b.replace('|', chr(92) + '|')} | {c.replace('|', chr(92) + '|')} |")
    P("")
    P("### Round 4")
    P("")
    P(f"A fourth checker re-ran the round-3 script at `cf8eb5b` into a scratch directory and "
      f"reported four minor findings and nothing substantive; nothing was open from round 3. Each "
      f"finding and its disposition, as applied by the round-4 fixer (values recomputed at the "
      f"current commit, `{head[:7]}`):")
    P("")
    P("| finding | claim | disposition |")
    P("|---|---|---|")
    for a, b, c in VC4:
        P(f"| {a} | {b.replace('|', chr(92) + '|')} | {c.replace('|', chr(92) + '|')} |")

    # ---- release (L3): the self-check -- this run's own two outputs projected as if tracked, with the audit files on
    # disk (section 2f), by the sweeps' own rules; the placeholders of section 2f, item 8 and the round-4 row are filled
    # from the combined result, and the rendering is repeated until the result no longer changes (a fixed point)
    def _fill(t_: str, sc_: dict) -> str:
        for k_, v_ in sc_["fill"].items():
            t_ = t_.replace(k_, v_)
        return t_

    def _sc(u_ids: dict, u_hosts: dict, n_iter: int) -> dict:
        s_ids = {k: ps for k, ps in u_ids.items() if ps & {OUT_MD_C, OUT_JSON_C}}
        s_hosts = {k: ps for k, ps in u_hosts.items() if ps & {OUT_MD_C, OUT_JSON_C}}
        comb = bool(u_ids or u_hosts)
        # L3 fix round: the failing gate(s) named from the counts -- the id gate only when an id is unclassified, the
        # host gate only when a host is, both only when both are
        g_ = [g for g, n in (("the external-reference sweep gate (0 unclassified ids)", len(u_ids)),
                             ("the URL-host sweep gate (0 unclassified hosts)", len(u_hosts))) if n]
        gates_ = " and ".join(g_)
        return {
            "fill": {
                "@@L3SELF@@": f"{len(s_ids)} id(s) and {len(s_hosts)} host(s)",
                "@@L3COMB@@": f"{len(u_ids)} id(s) and {len(u_hosts)} host(s)",
                "@@L3VERDICT_2F@@": (f", so {gates_} of the pass line would fail at the pre-flip re-run until "
                                     f"each is classified (for the PI where no confirmed rule covers it); the other "
                                     f"sweep gate would not fail on these files" if len(g_) == 1 else
                                     f", so {gates_} of the pass line would fail at the pre-flip re-run until "
                                     f"each is classified (for the PI where no confirmed rule covers it)" if comb else
                                     ", so neither sweep gate would fail on these files at the pre-flip re-run"),
                "@@L3VERDICT_8@@": (f", so {gates_} of the pass line {'fail' if len(g_) > 1 else 'fails'} there "
                                    f"until each is classified (the PI's or the re-run's call; nothing is changed "
                                    f"here)." if comb else
                                    ", so neither sweep gate fails on them there (nothing is changed here)."),
                "@@L3VERDICT_VC@@": (f", so {gates_} would fail there until each is classified. " if comb else
                                     ", so neither gate would fail on them there. ")},
            "json": {
                "outputs_projected_as": [OUT_MD_C, OUT_JSON_C],
                "outputs_inside_repository": [not os.path.relpath(os.path.realpath(o_), os.path.realpath(REPO))
                                              .startswith("..") for o_ in (OUT_MD, OUT_JSON)],
                "own_outputs_unclassified_ids": len(s_ids), "own_outputs_unclassified_hosts": len(s_hosts),
                "combined_unclassified_ids": len(u_ids), "combined_unclassified_hosts": len(u_hosts),
                "combined_unclassified_ids_sha256_8": sorted(sha256(k[1].encode())[:8] for k in u_ids),
                "combined_unclassified_hosts_sha256_8": sorted(sha256(k[1].encode())[:8] for k in u_hosts),
                "renderings_to_fixed_point": n_iter}}

    def _render(sc_: dict):
        tail = ["", "## Self-check: this raw's own text", "",
                f"This run's two outputs, projected as if tracked as `{OUT_MD_C}` and `{OUT_JSON_C}` (an output "
                f"outside the repository is projected under `results/raw/` by its basename), together with the "
                f"{len(own_txt)} audit file(s) on disk that section 2f projects, by the sweeps' own rules: "
                f"**{sc_['json']['own_outputs_unclassified_ids']}** unclassified id(s) and "
                f"**{sc_['json']['own_outputs_unclassified_hosts']}** unclassified host(s) carried by this raw's "
                f"own text; **{sc_['json']['combined_unclassified_ids']}** id(s) and "
                f"**{sc_['json']['combined_unclassified_hosts']}** host(s) in all"
                + ("" if not (sc_['json']['combined_unclassified_ids'] or sc_['json']['combined_unclassified_hosts'])
                   else " (by sha256[:8] only: ids "
                   + (", ".join(f"`{x}`" for x in sc_['json']['combined_unclassified_ids_sha256_8']) or "none")
                   + "; hosts "
                   + (", ".join(f"`{x}`" for x in sc_['json']['combined_unclassified_hosts_sha256_8']) or "none")
                   + ")")
                + f". Section 2f, section 7 item 8 and the round-4 values-check row print this combined verdict. "
                f"The text written is the last text projected, this paragraph included (where the rendering count "
                f"changes on the last rendering, that rendering is projected once more and must give the same "
                f"result); it reached a fixed point after {sc_['json']['renderings_to_fixed_point']} rendering(s)."]
        md_ = _fill("\n".join(L + tail) + "\n", sc_)
        js_ = _fill(json.dumps({**R, "self_check": sc_["json"], "web_reads_recorded": WEB_READS,
                                "jlens_upstream_blobs_recorded": JLENS_UPSTREAM_BLOBS}, indent=1,
                               default=list), sc_)
        # L3 fix round: section 1's count of this run's own outputs carrying the two markers, on the text written (the
        # fill text carries neither marker, so the count is stable)
        o_tq = sum(1 for t_ in (md_, js_) if TQ_MARK in norm_text(t_))
        o_fr = sum(1 for t_ in (md_, js_) if FR_MARK in norm_text(t_))
        s1_ = (f"{o_tq} carr{'ies' if o_tq == 1 else 'y'} the trial question and {o_fr} the framing marker")
        assert TQ_MARK not in s1_ and FR_MARK not in s1_
        md_, js_ = md_.replace("@@L3S1OWN@@", s1_), js_.replace("@@L3S1OWN@@", s1_)
        return md_, js_, len(L) + len(tail)
    sc = _sc({}, {}, 1)
    for n_it in range(1, 7):
        md_t, js_t, n_lines = _render(sc)
        u_i, u_h = project({**own_txt, OUT_MD_C: md_t, OUT_JSON_C: js_t})
        sc_new = _sc(u_i, u_h, n_it)
        if {k_: v_ for k_, v_ in sc_new["json"].items() if k_ != "renderings_to_fixed_point"} == \
                {k_: v_ for k_, v_ in sc["json"].items() if k_ != "renderings_to_fixed_point"} and \
                sc_new["fill"] == sc["fill"]:
            if sc["json"]["renderings_to_fixed_point"] != n_it:
                sc = sc_new
                md_t, js_t, n_lines = _render(sc)
                # L3 fix round: the final rendering (its count changed) is projected once more, so the text written
                # is a text projected; the result must be the same, the count included
                u_i, u_h = project({**own_txt, OUT_MD_C: md_t, OUT_JSON_C: js_t})
                if _sc(u_i, u_h, n_it) != sc:
                    raise SystemExit("self-check: the final rendering projects differently; nothing written")
            break
        sc = sc_new
    else:
        raise SystemExit("self-check did not reach a fixed point in 6 renderings; nothing written")
    assert "@@L3" not in md_t and "@@L3" not in js_t
    R["self_check"] = sc["json"]
    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_MD, "w") as f:
        f.write(md_t)
    with open(OUT_JSON, "w") as f:
        f.write(js_t)
    print(f"wrote {os.path.relpath(OUT_MD, REPO)} ({n_lines} lines) and "
          f"{os.path.relpath(OUT_JSON, REPO)}; pattern redactions {len(REDACTIONS)}, "
          f"redacted ids {len(REDACTED_IDS)}; commit {head[:7]}; pass: {R['pass_line']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
