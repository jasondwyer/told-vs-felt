#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12(i): gitleaks over the entire history, with Code's triage.

The block names gitleaks first (:77). The PI installed gitleaks and reported, 2026-10-09,
"gitleaks over all history found 4 leaks". This script runs the same scan with secrets
redacted (--redact=100), writes the report to a temporary file outside the repository,
and records each finding: rule, file, commit, line, gitleaks fingerprint, the key or
context text gitleaks matched with the secret already redacted, and Code's triage verdict
with its reason. Verdicts are keyed by fingerprint, and a finding with no verdict is
printed as UNTRIAGED. No secret value is ever written: the report is redacted at source.

Release runs. v1 (tag note-2026-10-v1; the PI's answer of 2026-10-12, "Yes to all five; tag it")
wrote results/raw/2026-10-12_note-N12-gitleaks-release.md over the five v1 release files (the
preprint at patch v7, note v0.6, the three 2026-10-10 renders); DEFAULT_OUT_V1, RELEASE_V1,
KNOWN_ATTR_PATHS_V1, KNOWN_SKIP_PATHS_V1 and BASIS_V1 keep that run's values as its record. v2 (tag
note-2026-10-v2; the design seat's answers of 2026-10-28 with the PI's "Yes to all",
results/raw/2026-10-28_note-design-to-code_release-block-answers.md, section 5, 3a-3b): the default
output is the NEW dated raw results/raw/2026-10-29_note-N12-gitleaks-release.md, and the script
refuses to write any path git already tracks, so a committed raw is never overwritten. It also runs
`gitleaks dir` over .txt copies of the five release files (the preprint, patch v8 under its status
banner; note v0.8; the three 2026-10-22 renders) as HEAD holds them: each is read from HEAD's blob
(`git cat-file`), its sha256 asserted, and the working-tree copy asserted equal. gitleaks' default
config skips .svg files by path (accepted by the PI, answer of 2026-10-12, question 4; the answers
of 2026-10-28, section 5, 3b, add the three 2026-10-22 renders to the skip list on that basis), and
the copies are an extra check, not a substitute.

v2's pass line records the v2 basis (BASIS_V2, the line the answers' section 5, 3a give) only in the
release raw itself (--out is DEFAULT_OUT); a rehearsal or a re-run (--out elsewhere, e.g. the tag-commit
re-run, whose raw takes its own dated name) says so instead. It also states how far the run's coverage
reaches and what covers the commits after it (TAG_RERUNS_V2: the scans re-run at the tag commit, before the
push; 3g names gitleaks and the password search, and the PI's word of 2026-10-29 adds the history, content
and licenses scripts, their raws committed after the tag, as v1's were). Item 4's basis is printed by part:
the .svg skip (the 2026-10-12 answer, carried by the seat's item C), and trufflehog, which runs over all
history in its own script (scripts/audit_note_N12_trufflehog.py), not this one, on the PI's word of
2026-10-29 (TRUFFLEHOG_V2_PI_WORDS). Before the raw is written its text is checked for the
origin-only ref the answers name (their section 2, read from the committed line at run time, never
printed): the ref's namespace, or a hex run of 7+ characters that is a prefix of its id or its commit (or
begins with one), refuses the write (exit 2, nothing written).

The gate fails closed. It is a STOP (exit 1) when: a finding has no verdict or is a true secret;
a TRIAGE entry added after v1's six (a finding new since v1's release run) has no recorded PI ruling
(TRIAGE_V2_PI; the seat's item A: "any new finding is a fresh STOP");
the copies have a finding; a release file is absent at HEAD or its hash does not match; a TRIAGE
fingerprint is not re-found (history only grows, so every triaged finding must recur); either
gitleaks report is absent or does not parse; the history scan logs no "commits scanned" line or
the dir scan no "scanned ~" line; gitleaks is not version 8.30.1; or any input that changes
gitleaks' rules or suppresses findings is present (.gitleaks.toml at the repo root,
.gitleaksignore at the repo root or the cwd, GITLEAKS_CONFIG or GITLEAKS_CONFIG_TOML set; gitleaks
reads a .gitleaksignore at the scanned path whatever --gitleaks-ignore-path says, so only the
assertion guards it). Both scans also pass --ignore-gitleaks-allow, so an inline allow comment
cannot hide a finding; the number of commits whose diff adds or removes the literal is computed
(`git log --all --text -S`) and printed, never assumed.

Every file in history is rendered as text by git. The repository's .gitattributes sets
`/data/m/ckpt/** -diff` (Code's line, added in the m package BUILD commit 5f7b968; its comment says
the path may carry a contrast pick and never renders in a diff or a log -p, and cites PROPOSAL-m
v1.11 m:318, the Blinding paragraph: neither the seat nor the PI reads a pick-bearing artifact,
checkpoints among them, before that unit's VERDICTS, outside four listed exceptions). A plain
`git log -p` therefore prints "Binary files ... differ" there and gitleaks would never read that
path. The history scan passes `--log-opts=--all --text --no-textconv` (every blob as text, no
external text conversion); the paths in history whose diff/binary attributes are set are listed in
the raw, and one not in KNOWN_ATTR_PATHS is a STOP. gitleaks reports with --redact=100, so a match
there appears only with its secret redacted. Replace refs are disabled for gitleaks and the commit
count (GIT_NO_REPLACE_OBJECTS=1). The completeness check is a STOP when gitleaks' "N commits
scanned" differs from `git rev-list --all --count` (the only excused difference is the listed
deletion-only commits, which gitleaks does not count), or when any gitleaks log has an ERR line
(copied into the raw with temp and repository paths replaced, git's messages withheld).

gitleaks' default config also skips paths by its global path allowlist (.svg, .png, .pdf, lock
files and others). Which history paths it skips is measured, not assumed: a throwaway probe file
holding a random generic-api-key line is written at every history path in a temporary directory
and `gitleaks dir` is run over it; a path with no finding is skipped. Every historical version of
every skipped path is then scanned as a .txt copy. A skipped path not in KNOWN_SKIP_PATHS is a STOP.

    python -B scripts/audit_note_N12_gitleaks.py [--out results/raw/2026-10-29_note-N12-gitleaks-release.md]
"""
import argparse
import hashlib
import json
import os
import re
import secrets
import shutil
import string
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
DEFAULT_OUT_V1 = "results/raw/2026-10-12_note-N12-gitleaks-release.md"   # v1's release run (2026-10-12): its record
DEFAULT_OUT = "results/raw/2026-10-29_note-N12-gitleaks-release.md"   # the v2 release run (answers of 2026-10-28, section 5, 3b)
# The companion raws of the v2 run's (i): the history script's release raw of the same run (HIST_RAW), and trufflehog's
# (TRUFFLEHOG_RAW, below; the PI's word of 2026-10-29).
HIST_RAW = "results/raw/2026-10-29_note-N12-history-release.md"
# The v2 run's date is in its raws' names, and these two must name the same one. The answers of 2026-10-28 (section 1)
# run block section 2 item 1 over 2026-10-29 to 10-31: if the run of record falls on another PI-local date, every v2
# name changes in one edit across the N12 scripts (here DEFAULT_OUT, HIST_RAW and TRUFFLEHOG_RAW; the history script's
# RELEASE_MD, RELEASE_JSON and TRUFFLEHOG_RAW_V2; the trufflehog script's DEFAULT_OUT, GL_RAW, HIST_RAW and docstring
# command; the licenses script's docstring command; the scrub generator's RELEASE2_RAWS) before the scripts commit.
assert os.path.basename(HIST_RAW)[:10] == os.path.basename(DEFAULT_OUT)[:10], "DEFAULT_OUT and HIST_RAW: two run dates"
# The v2 tag (the release block of 2026-10-27, section 2 item 7; the answers of 2026-10-28, section 8: on the final
# audit commit, before the push).
TAG_V2 = "note-2026-10-v2"
# Release v2: the scans the release sequence re-runs at the tag commit, before the push. TAG_RERUNS_3G is the record
# (what the design seat's answers of 2026-10-28, section 5, 3g, name: outputs outside the repository, their counts in
# the post-tag raw); TAG_RERUNS_V2 is the switch, extended on the PI's word of 2026-10-29 (his answer, item 3,
# TAG_RERUNS_V2_PI_WORDS: all five, their raws committed after the tag, as v1's were; item 1 now is the baseline), and
# the pass line's bound on this run's coverage follows it.
TAG_RERUNS_3G = ("gitleaks", "password")
TAG_RERUNS_V2 = ("gitleaks", "password", "history", "content", "licenses")
TAG_RERUNS_V2_PI_WORDS = ("2026-10-29", "All five at the tag commit — history, content, licenses, gitleaks, the "
                                        "password search — as v1 did, raws committed after the tag; item 1 now is "
                                        "the baseline.")
RERUN_NAMES = {"gitleaks": "gitleaks (this script)", "password": "the password search",
               "history": "the history script", "content": "the content screen", "licenses": "the licenses script"}
assert set(TAG_RERUNS_3G) <= set(TAG_RERUNS_V2) <= set(RERUN_NAMES), TAG_RERUNS_V2
# The origin-only ref the design seat's answers of 2026-10-28 name (their section 2): its id and commit are read from
# that committed line at run time (located by content, parsed as the scrub generator parses it), for the write guard
# only, and never printed.
ANSWERS_V2 = ("908a659", "results/raw/2026-10-28_note-design-to-code_release-block-answers.md")
RX_TELEPORT_LINE = re.compile(r"refs/claude-teleport/([0-9a-f]{8,})`\s*\S+\s*`([0-9a-f]{7,40})`")
RX_HEX7 = re.compile(r"[0-9a-fA-F]{7,}")
GITLEAKS_VERSION = "8.30.1"
SUPPRESS_ENV = ("GITLEAKS_CONFIG", "GITLEAKS_CONFIG_TOML")
# gitleaks' inline-allow literal, built from two pieces so that neither this script nor its raw contains it
# (committing either would otherwise add a match to the count this script prints).
ALLOW_LIT = "gitleaks" ":allow"
ALLOW_SHOWN = "`gitleaks` + `:allow`"

# v1's record, not checked by this run: the five release files the v1 tag commit holds (the PI's answer of 2026-10-12,
# question 5), with the sha256 each had.
RELEASE_V1 = [
    ("PREPRINT-v1_0-draft.md", "d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6"),
    ("RESEARCH-NOTE-v0_6-draft.md", "2c7e1cf526f6dfe737c6246cf137f1ae9bc18816846e8329de2f9c3c04426fbb"),
    ("2026-10-10_F1a_headline-strip.svg", "6ffad6cd971aabdc70d7b684a6408988c9a05e5445125d3ce61a78557405cee6"),
    ("2026-10-10_F1b_five-link-panels.svg", "6fcb060f6a2cf2c0ce1f5374c3267c5cec67304994a9967e49a2afaffcf6113e"),
    ("2026-10-10_F2_macar-lineage-roc_post.svg", "81b13e805e64e6a9534e65e6dfeb50d6c6a65cf3d8b02b9cb3a1e36852e5ac4e"),
]
# The five release files of the v2 release (tag note-2026-10-v2), with the sha256 each must have: the preprint, patch v8
# under its status banner (32aefcc), note v0.8, the text as posted (0de15a1), and the three 2026-10-22 renders (0a3f925)
# (the release block of 2026-10-27, section 0; the answers of 2026-10-28, section 1). gitleaks dir scans .txt copies of them.
RELEASE = [
    ("PREPRINT-v1_0-draft.md", "5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467"),
    ("RESEARCH-NOTE-v0_8-draft.md", "6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d"),
    ("2026-10-22_F1a_headline-strip.svg", "f0c1cd73e474eff54f11dd677a9b8e385ebae1e63cd667babc88d83123985bfc"),
    ("2026-10-22_F1b_five-link-panels.svg", "640c13e87b161dc8c14e2813acba1dc6a09b94d7beb5b9d1784cfe34371633af"),
    ("2026-10-22_F2_macar-lineage-roc_post.svg", "0e0459cf628ee7adef2d8c462a1b6c854d3a87a9743baa4f18b44134fbf969bc"),
]

# Code's triage, keyed by the gitleaks fingerprint (commit:file:rule:line). Each entry was read
# in context with `git show <commit>:<file>` before it was entered.
TRIAGE = {
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:611": (
        "FALSE-POSITIVE",
        "A row of the audit's own triage table, keyed (path, 'token', <16-hex sha256 prefix>). The rule fires on the "
        "literal column name 'token' followed by a hash prefix of an N13 provenance value. It is not a credential."),
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:651": (
        "FALSE-POSITIVE",
        "The same triage table as :611: a 16-hex prefix of a commit id or sha256 from the N13 provenance JSON, next to "
        "the column name 'token'. It is not a credential."),
    "cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55:data/m/gates/G-CAL_completability_qwen.json:generic-api-key:44": (
        "FALSE-POSITIVE",
        "The field `key_set_sha256` of the G-CAL completability gate: the SHA-256 of the session's identity key set, a "
        "content hash among the artifact's other *_sha256 fields. It is not a credential."),
    "1bdf16c149698e3b1181f082b8c169727e9df3c8:data/e2d/closure_valuescheck.json:generic-api-key:46": (
        "FALSE-POSITIVE",
        "A values-check record's `\"key\"` field, whose value is a claim identifier "
        "(e2d_d3_in_situ_vs_excised_forward_cost_...). The rule fires on the field name 'key'. It is not a credential."),
    # Added for the release run (2026-10-12); not one of the PI's four. Commit f23b444 is dated 2026-10-10, after the PI's scan of 2026-10-09.
    "f23b44408daf516552c0d11414c646ea0dd6213f:data/m/gates/G-SHAPE-F0.json:generic-api-key:378": (
        "FALSE-POSITIVE",
        "An entry of the G-SHAPE-F0 gate's `provenance.sources` map, keyed by the path `valence_core/m/keys.py`: a "
        "64-hex value equal to the sha256 of that file at f23b444 (and at the build commit d092078), among the other "
        "source files' sha256 values. keys.py is PROPOSAL-m's RNG stream-key module. The rule fires on the word 'keys' "
        "in the path. It is not a credential."),
    # Added for the release run (2026-10-12); not one of the PI's four, and invisible to the PI's scan of 2026-10-09:
    # data/m/ckpt/ is `-diff` (.gitattributes, 5f7b968), so only the --text history scan reads it. Verified without reading the blinded file
    # out: the matched field is the checkpoint's identity.key_set_sha256 (the blob's only occurrence of the name),
    # a 64-character lowercase-hex string equal to gcal.key_set_sha256(gcal.key_set()) recomputed from
    # valence_core/m/gcal.py:508-527 (written into the checkpoint by _identity, :692), and equal to the value at
    # the triaged gates/G-CAL_completability_qwen.json:44; redacted form 47ee...64:422c647a.
    "cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55:data/m/ckpt/G-CAL_qwen.json:generic-api-key:1": (
        "FALSE-POSITIVE",
        "The field `key_set_sha256` of the G-CAL checkpoint's identity: the same SHA-256 of the session's key set "
        "(128 (pool, i, s, seed) rows, seeds crc32-derived) that gcal.py computes at :524 and binds into the "
        "checkpoint identity at :692, equal to the value at the triaged G-CAL_completability_qwen.json:44. It is "
        "a content hash, not a credential."),
}
# The first six TRIAGE entries are v1's record: the PI's four (entered at e0fd85c, 2026-10-09) and the two added for
# v1's release run (e8fb54d, 2026-10-12); their order is asserted below (after PI_FOUR). Entries for the v2 release run
# are appended after them: each is a finding new since v1's release run, so each is a fresh STOP under the seat's item
# A ("any new finding is a fresh STOP"; the PI answered it on 2026-10-28, "Yes to all") unless TRIAGE_V2_PI records the
# PI's dated words resolving it.
TRIAGE_V1_N = 6
TRIAGE_V1_RELEASE_ADDED = (
    "f23b44408daf516552c0d11414c646ea0dd6213f:data/m/gates/G-SHAPE-F0.json:generic-api-key:378",
    "cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55:data/m/ckpt/G-CAL_qwen.json:generic-api-key:1",
)
# fingerprint (an entry added after v1's six) -> ("YYYY-MM-DD", the PI's words, verbatim) resolving that new finding.
# None at this commit.
TRIAGE_V2_PI = {}
assert set(TRIAGE_V2_PI) <= set(list(TRIAGE)[TRIAGE_V1_N:]), "a TRIAGE_V2_PI key is not an entry added for v2"
assert all(isinstance(v_, tuple) and len(v_) == 2 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v_[0]) and v_[1].strip()
           for v_ in TRIAGE_V2_PI.values()), "a TRIAGE_V2_PI value is not (date, the PI's words)"
# Paths in history whose diff/binary attributes are set (git check-attr), known at the release preparation.
# They are read because the history scan passes --text. A path not listed here is a STOP: the --text scan reads
# it too, but whether gitleaks may read a -diff path is a question for the PI and the seat, path by path.
KNOWN_ATTR_PATHS_V1 = {"data/m/ckpt/G-CAL_qwen.json"}
# Added for the v2 release run: the four Q-F0 checkpoint paths (git check-attr: diff unset), listed on the PI's word of
# 2026-10-28 ("Yes to all", to the design seat's item C, answers section 0); the seat's words (section 5, 3b): "the
# blinding reason, m:318 "before VERDICTS", expired at VERDICTS on 2026-10-19". m:318 itself bars reads "before that
# unit's VERDICTS are computed"; Q-F0's VERDICTS were computed on 2026-10-19 (bfc179c).
KNOWN_ATTR_PATHS_ADDED_V2 = {
    "data/m/ckpt/Q-F0_time.json",
    "data/m/ckpt/Q-F0_id.json",
    "data/m/ckpt/Q-F0_qual.json",
    "data/m/ckpt/Q-F0_campaign.json",
}
KNOWN_ATTR_PATHS = KNOWN_ATTR_PATHS_V1 | KNOWN_ATTR_PATHS_ADDED_V2
# History paths gitleaks' default global path allowlist skips (measured by the probe), known at the release
# preparation: the three 2026-10-10 renders (the .svg skip, the PI's answer of 2026-10-12, question 4) and the
# .png added in ba67acb. Every historical version of a skipped path is scanned as a .txt copy; a skipped path
# not listed here is a STOP.
KNOWN_SKIP_PATHS_V1 = {
    "2026-10-10_F1a_headline-strip.svg",
    "2026-10-10_F1b_five-link-panels.svg",
    "2026-10-10_F2_macar-lineage-roc_post.svg",
    "figures/fig1_inverted_u.png",
}
# Added for the v2 release run: the three 2026-10-22 renders (0a3f925), on the basis of the PI's answer of 2026-10-12,
# question 4, carried by the answers of 2026-10-28 (section 5, 3b). The probe is the authority, and listing a path here
# does not make gitleaks skip it: a skipped path not listed is a STOP, and a listed path the probe finds read is
# printed in the raw (not a STOP: the history scan reads it).
KNOWN_SKIP_PATHS_ADDED_V2 = {
    "2026-10-22_F1a_headline-strip.svg",
    "2026-10-22_F1b_five-link-panels.svg",
    "2026-10-22_F2_macar-lineage-roc_post.svg",
}
KNOWN_SKIP_PATHS = KNOWN_SKIP_PATHS_V1 | KNOWN_SKIP_PATHS_ADDED_V2
# Root names gitleaks dir reads as its own config or ignore file: never mirrored by the probe.
GL_ROOT_NAMES = (".gitleaks.toml", ".gitleaksignore")
# The PI's four (routing of 2026-10-09), by fingerprint.
PI_FOUR = (
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:611",
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:651",
    "cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55:data/m/gates/G-CAL_completability_qwen.json:generic-api-key:44",
    "1bdf16c149698e3b1181f082b8c169727e9df3c8:data/e2d/closure_valuescheck.json:generic-api-key:46",
)
assert list(TRIAGE)[:TRIAGE_V1_N] == list(PI_FOUR) + list(TRIAGE_V1_RELEASE_ADDED), "TRIAGE's first six are not v1's"
# The basis the pass line states for (i). v1's, its record (printed by v1's run in results/raw/2026-10-12_note-N12-gitleaks-release.md):
BASIS_V1 = ("By the PI's answer of 2026-10-12 (question 3), ruling 4 (the PI's rulings of 2026-10-09, item 4) "
            "covers the release run's (i) when this raw and results/raw/2026-10-12_note-N12-history-release.md both "
            "show 0 true-secret candidates and 0 untriaged.")
# The v2 run's, in the form the design seat's answers of 2026-10-28 give for the history script's (i) line
# (results/raw/2026-10-28_note-design-to-code_release-block-answers.md, section 5, 3a): the first clause is the PI's
# words; the rest is labelled the seat's item A, which the PI's answer covers.
BASIS_V2 = ('PI (2026-10-28): "Yes to all". Referent, the design seat\'s item A as put: ruling 4 (the PI\'s rulings of '
            '2026-10-09, item 4) carries to the v2 run\'s (i), conditional on 0 true-secret candidates and 0 untriaged on '
            'the re-run; any new finding is a fresh STOP.')
# BASIS_V2 is 3a's line, verbatim; its words after "as put:" are 3a's rendering of item A (section 0), not item A's own
# text, so the raw names the line's source after it.
BASIS_V2_SOURCE = "(The line as the answers of 2026-10-28, section 5, 3a, give it.)"
# Item 4 of the PI's answer of 2026-10-12 (gitleaks' default .svg skip; trufflehog not run, for v1's run), by part, for
# the v2 run. The .svg skip: that answer, carried to the three 2026-10-22 renders by the design seat's item C, which the
# PI answered on 2026-10-28. trufflehog: run, on the PI's word of 2026-10-29 (TRUFFLEHOG_V2_PI_WORDS, below). The words below are the records', verbatim (PI_ANSWER_2026_10_12 as v1's record gives it,
# the history script's constant of that name; the other three are the answers at 908a659, lines 7, 11 and 41).
PI_ANSWER_2026_10_12 = "Yes to all five; tag it"
PI_ANSWER_2026_10_28 = "Yes to all"
ITEM_C_SVG_WORDS = "the three SVGs on the skip list"
SEAT_3B_SVG_WORDS = ("Add the three 2026-10-22 SVGs to the skip list on the basis of the PI's 2026-10-12 answer to "
                     "question 4.")
# The seat's words on the four -diff paths (the answers at 908a659, line 41: 3b), printed as the seat's, not m:318's.
SEAT_3B_BLIND_WORDS = 'the blinding reason, m:318 "before VERDICTS", expired at VERDICTS on 2026-10-19'
# trufflehog for v2: the PI's word of 2026-10-29 (his answer to Code's question, item 2), verbatim. trufflehog runs over
# all history in its own script (TRUFFLEHOG_SCRIPT), to its own dated raw, not in this one; the raw cites the words.
TRUFFLEHOG_V2_PI_WORDS = ("2026-10-29", "Install and run trufflehog over all history for v2, verified-only mode, raw "
                                        "committed; triage any finding as gitleaks’ were; TRUE-SECRET or UNTRIAGED "
                                        "is a STOP")
# and his answer the same day to Code's question on trufflehog's unknown results (verification errored or withheld)
TRUFFLEHOG_UNKNOWN_PI_WORDS = ("2026-10-29", "Yes, show and triage")
TRUFFLEHOG_SCRIPT = "scripts/audit_note_N12_trufflehog.py"
TRUFFLEHOG_RAW = "results/raw/2026-10-29_note-N12-trufflehog-release.md"
assert os.path.basename(TRUFFLEHOG_RAW)[:10] == os.path.basename(DEFAULT_OUT)[:10], "TRUFFLEHOG_RAW: another run date"
assert TRUFFLEHOG_V2_PI_WORDS is None or (
    isinstance(TRUFFLEHOG_V2_PI_WORDS, tuple) and len(TRUFFLEHOG_V2_PI_WORDS) == 2
    and re.fullmatch(r"\d{4}-\d{2}-\d{2}", TRUFFLEHOG_V2_PI_WORDS[0]) and TRUFFLEHOG_V2_PI_WORDS[1].strip()), \
    "TRUFFLEHOG_V2_PI_WORDS is not (date, the PI's words)"


def git(*args, **kw):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, **kw)


def plain(ln):
    return re.sub(r"\x1b\[[0-9;]*m", "", ln).strip()


ERR_RX = re.compile(r"(^|\s)(ERR|FTL|FATAL|ERROR)(\s|$)")


def err_lines(log, subs):
    """gitleaks' ERR-level lines (zerolog console format: '<time> ERR ...'), made safe to commit: ANSI codes
    stripped; each (path, placeholder) of `subs` replaced, longest first; a line relaying git's own message
    ('[git]', 'fatal:', 'error:') reduced to its level and any 40-hex object ids; capped at 200 characters."""
    out = []
    for ln in log:
        s = plain(ln)
        m = ERR_RX.search(s)
        if not m:
            continue
        for a_, b_ in sorted(subs, key=lambda x: -len(x[0])):
            if a_:
                s = s.replace(a_, b_)
        if "[git]" in s or "fatal:" in s or "error:" in s:
            ids = re.findall(r"\b[0-9a-f]{40}\b", s)
            s = "%s [git] (git's message withheld)%s" % (
                m.group(2), ("; object id(s): " + ", ".join(ids)) if ids else "")
        s = s.replace("`", "'")
        out.append(s[:200] + ("..." if len(s) > 200 else ""))
    return out


def gl_dir(target, rep, env):
    """`gitleaks dir` over `target` (default config, redacted); returns (cmd, returncode, log, report or None)."""
    cmd = ["gitleaks", "dir", "--redact=100", "--ignore-gitleaks-allow",
           "--report-format", "json", "--report-path", rep, "--no-banner", target]
    r = subprocess.run(cmd, cwd=os.path.dirname(rep), capture_output=True, text=True, env=env)
    return cmd, r.returncode, (r.stdout + r.stderr).splitlines(), load_report(rep)


def rel_file(f, base):
    """A report's File relative to the scanned directory (gitleaks may print it through either spelling)."""
    p = f.get("File", "")
    for b in (base, os.path.realpath(base)):
        q = os.path.relpath(p, b)
        if not q.startswith(".."):
            return q
    return p


def place_probes(td, names, line):
    """Write the probe line at every history path, spread over as few directories as needed so that no two
    paths collide (a file that is another's directory, or two paths equal ignoring case: the filesystem may be
    case-insensitive). Returns ([(dir, [path, ...]), ...], [path not probed, ...])."""
    rounds, unprobed = [], []
    for n in names:
        if n in GL_ROOT_NAMES or n.startswith("/") or ".." in n.split("/"):
            unprobed.append(n)
            continue
        parts = n.split("/")
        pre = ["/".join(parts[:i]) for i in range(1, len(parts))]
        placed = False
        for k in range(len(rounds) + 1):
            if k == len(rounds):
                d = os.path.join(td, "probe%d" % k)
                os.mkdir(d)
                rounds.append((d, [], {}, set()))
            d, lst, case, files = rounds[k]
            if n.lower() in case or any(case.get(q.lower(), q) != q or q in files for q in pre):
                continue
            try:
                os.makedirs(os.path.join(d, os.path.dirname(n)), exist_ok=True)
                with open(os.path.join(d, n), "xb") as fh:
                    fh.write(line)
            except OSError:
                break
            for q in pre:
                case[q.lower()] = q
            case[n.lower()] = n
            files.add(n)
            lst.append(n)
            placed = True
            break
        if not placed:
            unprobed.append(n)
    return [(d, lst) for d, lst, _c, _f in rounds if lst], unprobed


def load_report(path):
    """The parsed gitleaks report, or None when it is absent or does not parse (a STOP)."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            v = json.load(fh)
    except (OSError, ValueError):
        return None
    return v if isinstance(v, list) else None


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def teleport_vals():
    """The write guard's values, [(label, value)], for the origin-only ref the answers name: its id, and its commit (in
    full where the local object store resolves it; `git rev-parse` only reads), parsed from their committed line
    (ANSWERS_V2, located by content). None when that line cannot be read or parsed: the write is then refused."""
    b = git("cat-file", "blob", "%s:%s" % ANSWERS_V2, text=True)
    lines = [x for x in b.stdout.split("\n") if "claude-teleport/" in x] if b.returncode == 0 else []
    m = RX_TELEPORT_LINE.search(lines[0]) if len(lines) == 1 else None
    if not m:
        return None
    full = git("rev-parse", "--verify", "-q", m.group(2) + "^{commit}", text=True).stdout.strip()
    return [("the origin-only ref's id", m.group(1)),
            ("the origin-only ref's commit",
             full if re.fullmatch(r"[0-9a-f]{40}", full) and full.startswith(m.group(2)) else m.group(2))]


def guarded(text, vals):
    """The guarded classes `text` carries, by label only (a value is never returned or printed): the origin-only ref's
    namespace; a hex run of 7+ characters that is a prefix of a guarded value, or begins with one."""
    bad = ["the origin-only ref's namespace"] if re.search(r"claude-teleport/", text, re.I) else []
    runs = set(h.lower() for h in RX_HEX7.findall(text))
    for lab, v in vals:
        if any(v.startswith(h) or h.startswith(v) for h in runs):
            bad.append(lab)
    return bad


def tag_commit(tag):
    """The commit `tag` points at (peeled), or None when there is no such tag."""
    r = git("rev-parse", "--verify", "-q", "refs/tags/%s^{commit}" % tag, text=True)
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None


def and_list(xs):
    """'a', 'a and b', 'a, b and c'."""
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def tag_reruns_text():
    """Release v2: the re-runs at the tag commit as TAG_RERUNS_V2 holds them, each part with its basis."""
    named = [RERUN_NAMES[x] for x in TAG_RERUNS_V2 if x in TAG_RERUNS_3G]
    extra = [RERUN_NAMES[x] for x in TAG_RERUNS_V2 if x not in TAG_RERUNS_3G]
    return (and_list(named) + " (the design seat's answers of 2026-10-28, section 5, 3g)"
            + ((", and " + and_list(extra) + " (beyond 3g's two, on the PI's word of %s, which also sets the re-runs' "
                "form, verbatim: \"%s\")" % TAG_RERUNS_V2_PI_WORDS) if extra else ""))


def coverage_v2(head, tag_c, rel_raw):
    """Release v2: how far this run's coverage reaches, and what covers the commits after it (TAG_RERUNS_V2). `tag_c` is
    the commit TAG_V2 points at (None before the tag); `rel_raw` says whether this output is the release raw."""
    reruns = (("The re-runs at the tag commit, before the push, their raws committed after the tag: %s."
               if set(TAG_RERUNS_V2) - set(TAG_RERUNS_3G) else
               "The re-runs at the tag commit, before the push (outputs outside the repository, their counts in the "
               "post-tag raw): %s.") % tag_reruns_text())
    after_tag = "the commits after the tag commit (the post-tag raw's) are covered by no gitleaks run"
    if tag_c == head:
        return ("This run is at the tag commit (`%s` points at HEAD `%s`): it covers the history the tag holds, the "
                "re-run's scope; %s. %s" % (TAG_V2, head[:10], after_tag, reruns))
    if tag_c:
        return ("This run covers the history at HEAD `%s`, after the tag commit (`%s` at `%s`): the release sequence "
                "has no gitleaks run after the re-run at the tag commit. %s" % (head[:10], TAG_V2, tag_c[:10], reruns))
    return ("This run covers the history at HEAD `%s`. The commits after it -- the commit that adds %s, block section 2 "
            "items 2-7 (N1 round 11, the README regression count, N18, the README-NOTE re-point, the preflip script, "
            "the tag commit) and any other commit made before the tag -- are covered for gitleaks only by its re-run at "
            "the tag commit; %s. %s" % (
                head[:10], "this raw" if rel_raw else "the release raw `%s`" % DEFAULT_OUT, after_tag, reruns))


def item4_parts():
    """Release v2: item 4's basis on this run, by part -- (the .svg skip, trufflehog)."""
    svg = ("the .svg skip -- the PI's answer of 2026-10-12 to question 4 (verbatim: \"%s\"), for v1's release run, "
           "extended to the three 2026-10-22 renders by the design seat's item C (as put: \"%s\"; its answers of "
           "2026-10-28, section 5, 3b: \"%s\"), which the PI answered on 2026-10-28: \"%s\"" % (
               PI_ANSWER_2026_10_12, ITEM_C_SVG_WORDS, SEAT_3B_SVG_WORDS, PI_ANSWER_2026_10_28))
    if TRUFFLEHOG_V2_PI_WORDS is None:
        th = ("trufflehog not run -- no v2 record names it (the release block of 2026-10-27, section 2 item 1, lists "
              "gitleaks, not trufflehog); its only basis is the 2026-10-12 answer's item 4, given for v1's run")
    else:
        th = ("trufflehog -- run over all history in its own script (`%s`, raw `%s`), not in this one: the PI's words "
              "of %s, verbatim: \"%s\"; and his answer the same day on its unknown results (verification errored or "
              "withheld), verbatim: \"%s\" (verified and unknown results shown and triaged)" % (
                  (TRUFFLEHOG_SCRIPT, TRUFFLEHOG_RAW) + TRUFFLEHOG_V2_PI_WORDS + (TRUFFLEHOG_UNKNOWN_PI_WORDS[1],)))
    return svg, th


def shown_path(outp, rel_out):
    """An output path as stdout may print it: repository-relative inside the repository, else its basename only."""
    return rel_out if not rel_out.startswith("..") else "<outside the repository>/" + os.path.basename(outp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    a = ap.parse_args()
    outp = os.path.realpath(a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out))
    rel_out = os.path.relpath(outp, os.path.realpath(ROOT))
    # The filesystem may be case-insensitive (APFS, core.ignorecase=true): match tracked paths ignoring case,
    # and literally (no glob), and also refuse any tracked file that is the same file on disk.
    tracked = False
    if not rel_out.startswith(".."):
        ls = git("ls-files", "-z", "--", ":(icase,literal)" + rel_out).stdout.split(b"\0")
        tracked = any(x for x in ls)
        if not tracked and os.path.exists(outp):
            for x in git("ls-files", "-z").stdout.split(b"\0"):
                q = os.path.join(ROOT, x.decode("utf-8", "surrogateescape"))
                if x and os.path.exists(q) and os.path.samefile(q, outp):
                    tracked = True
                    break
    if tracked:
        print("refused: %s is tracked by git; a committed raw is never overwritten" % a.out)
        return 2
    # the write guard's values (the origin-only ref the answers name), read before any scan; never printed
    tvals = teleport_vals()
    if tvals is None:
        print("refused: the write guard's values (the origin-only ref the design seat's answers name, their section 2) "
              "could not be read from %s:%s; nothing written" % ANSWERS_V2)
        return 2
    ver = subprocess.run(["gitleaks", "version"], capture_output=True, text=True).stdout.strip()
    head = git("rev-parse", "HEAD", text=True).stdout.strip()
    tag_c = tag_commit(TAG_V2)
    rel_raw = rel_out == DEFAULT_OUT
    # Inputs that change gitleaks' rules or suppress its findings. Each present one is a STOP.
    suppress = []
    for label, path in ((".gitleaks.toml at the repo root", os.path.join(ROOT, ".gitleaks.toml")),
                        (".gitleaksignore at the repo root", os.path.join(ROOT, ".gitleaksignore")),
                        (".gitleaksignore at the cwd the script was started from",
                         os.path.join(os.getcwd(), ".gitleaksignore"))):
        if os.path.lexists(path):
            suppress.append(label)
    for k in SUPPRESS_ENV:
        if k in os.environ:
            suppress.append("environment variable %s set" % k)
    env = {k: v for k, v in os.environ.items() if k not in SUPPRESS_ENV}
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    genv = dict(os.environ, GIT_NO_REPLACE_OBJECTS="1")
    # The repository's own commit count, the completeness check's reference.
    rl = git("rev-list", "--all", "--count", text=True, env=genv)
    n_commits = int(rl.stdout.strip()) if rl.returncode == 0 and rl.stdout.strip().isdigit() else None
    # gitleaks counts a commit only when its -U0 patch adds a line: a non-merge commit that changes files but
    # adds no line (a deletion-only commit) is not counted (rehearsal probe, 2026-10-12). Those commits are listed
    # and are the only allowed difference; a merge or an empty commit is not excused.
    ns = git("log", "--all", "--no-merges", "--text", "--no-textconv", "--format=C %H", "--numstat", text=True,
             env=genv)
    deletion_only, cur, n_files, added = [], None, 0, 0
    for ln in ns.stdout.split("\n") + ["C END"]:
        if ln.startswith("C "):
            if cur is not None and n_files > 0 and added == 0:
                deletion_only.append(cur)
            cur, n_files, added = ln[2:].strip(), 0, 0
        elif ln.count("\t") >= 2:
            a_, _d, _p = ln.split("\t", 2)
            n_files += 1
            added += int(a_) if a_.isdigit() else 1
    if ns.returncode != 0:
        deletion_only = None
    n_merges_r = git("rev-list", "--all", "--merges", "--count", text=True, env=genv).stdout.strip()
    n_replace = len([x for x in git("for-each-ref", "refs/replace/", text=True).stdout.split("\n") if x.strip()])
    # Commits whose diff adds or removes the inline-allow literal (pickaxe, every blob as text).
    al = git("log", "--all", "--text", "-S" + ALLOW_LIT, "--format=%H", text=True, env=genv)
    allow_commits = [x for x in al.stdout.split() if x] if al.returncode == 0 else None
    # Paths in history whose diff/binary attributes are set: a plain log -p would not show their content.
    names = git("log", "--all", "--format=", "--name-only", "-z", env=genv).stdout
    names = sorted(set(x for x in names.replace(b"\n", b"\0").split(b"\0") if x))
    ca = subprocess.run(["git", "check-attr", "--stdin", "-z", "diff", "binary"], cwd=ROOT, capture_output=True,
                        input=b"\0".join(names) + b"\0")
    parts = ca.stdout.split(b"\0")
    attr_paths = sorted(set(parts[i].decode("utf-8", "surrogateescape") for i in range(0, len(parts) - 2, 3)
                            if parts[i + 2] != b"unspecified"))
    # `git check-attr -z diff binary` prints <path> NUL <attr> NUL <value> NUL per path and attribute, in order:
    # exactly 6 fields per path plus the empty tail, each path with both attributes.
    attr_ok = (ca.returncode == 0 and len(parts) == 6 * len(names) + 1 and parts[-1] == b""
               and all(parts[6 * i] == nb and parts[6 * i + 1] == b"diff" and parts[6 * i + 3] == nb
                       and parts[6 * i + 4] == b"binary" for i, nb in enumerate(names)))
    names_s = [x.decode("utf-8", "surrogateescape") for x in names]
    stamp = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%S UTC"], capture_output=True, text=True).stdout.strip()
    with tempfile.TemporaryDirectory(prefix="audit_note_gitleaks_") as td:
        rep = os.path.join(td, "report.json")
        cmd = ["gitleaks", "git", "--log-opts=--all --text --no-textconv", "--redact=100", "--ignore-gitleaks-allow",
               "--report-format", "json", "--report-path", rep, "--no-banner", "."]
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=env)
        log = (r.stdout + r.stderr).splitlines()
        loaded = load_report(rep)
        findings = loaded if loaded is not None else []
        # gitleaks dir over .txt copies of the release files as HEAD holds them, after their sha256 is asserted.
        rel_rows, rel_bad = [], 0
        cdir = os.path.join(td, "release")
        os.mkdir(cdir)
        for name, want in RELEASE:
            b = git("cat-file", "blob", "HEAD:" + name)
            blob = b.stdout if b.returncode == 0 else None
            got = hashlib.sha256(blob).hexdigest() if blob is not None else "ABSENT AT HEAD"
            src = os.path.join(ROOT, name)
            wt = sha256(src) if os.path.exists(src) else "MISSING"
            ok = got == want and wt == want
            rel_bad += 0 if ok else 1
            rel_rows.append((name, want, got, wt, ok))
            if blob is not None and got == want:
                with open(os.path.join(cdir, name + ".txt"), "wb") as fh:
                    fh.write(blob)
        drep = os.path.join(td, "dir_report.json")
        dcmd, d_rc, dlog, dloaded = gl_dir(cdir, drep, env)
        dfind = dloaded if dloaded is not None else []
        for f in dfind:
            f["File"] = rel_file(f, cdir)
        # The skip probe: a random, throwaway generic-api-key line (generated here, never written out) at every
        # history path; a probed path with no finding is one gitleaks' default config does not read.
        pval = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))
        prounds, unprobed = place_probes(td, names_s, ('api_key = "%s"\n' % pval).encode())
        probed, found, plogs, p_ok = [], set(), [], True
        for k, (pd, lst) in enumerate(prounds):
            probed += lst
            _pc, _prc, plog, prep_ = gl_dir(pd, os.path.join(td, "probe_report%d.json" % k), env)
            plogs += plog
            if prep_ is None or not any("scanned ~" in ln for ln in plog):
                p_ok = False
            for f in (prep_ or []):
                found.add(rel_file(f, pd))
        skipped = sorted(set(probed) - found)
        # Every historical version of every skipped path, as a .txt copy.
        sdir = os.path.join(td, "skipped")
        os.mkdir(sdir)
        skip_rows, seen_blobs, s_ok = [], set(), True
        for p in skipped:
            cs = git("log", "--all", "-m", "--no-renames", "--format=%H", "--", ":(literal)" + p, text=True, env=genv)
            if cs.returncode != 0:
                s_ok = False
            vers = set()
            for c in cs.stdout.split():
                bo = git("rev-parse", "--verify", "-q", "%s:%s" % (c, p), text=True, env=genv).stdout.strip()
                if not bo or bo in vers:
                    continue
                vers.add(bo)
                if bo in seen_blobs:  # the same bytes under another skipped path: copied once
                    continue
                bb = git("cat-file", "blob", bo, env=genv)
                if bb.returncode != 0:
                    s_ok = False
                    continue
                seen_blobs.add(bo)
                with open(os.path.join(sdir, "%03d_%s_%s.txt" % (len(seen_blobs), bo[:10], os.path.basename(p))),
                          "wb") as fh:
                    fh.write(bb.stdout)
            skip_rows.append((p, len(vers)))
            if not vers:
                s_ok = False
        srep = os.path.join(td, "skipped_report.json")
        scmd, s_rc, slog, sloaded = gl_dir(sdir, srep, env)
        sfind = sloaded if sloaded is not None else []
        for f in sfind:
            f["File"] = rel_file(f, sdir)
        subs = [(td, "<tmp>"), (os.path.realpath(td), "<tmp>"), (ROOT, "<repo>"), (os.path.realpath(ROOT), "<repo>"),
                (os.path.expanduser("~"), "~")]
        errs, derrs = err_lines(log, subs), err_lines(dlog, subs)
        perrs, serrs = err_lines(plogs, subs), err_lines(slog, subs)
    dscanned = [ln for ln in dlog if "scanned ~" in ln or "leaks found" in ln or "no leaks" in ln]
    scanned = [ln for ln in log if "commits scanned" in ln or "scanned ~" in ln or "leaks found" in ln or "no leaks" in ln]
    out = []
    w = out.append
    w("# AUDIT-note-release v1.2 -- N12(i): gitleaks over the entire history")
    w("")
    w("- Code stamp: %s (date -u); HEAD `%s`" % (stamp, head))
    w("- Block `%s` sha256 `%s`" % (BLOCK, sha256(os.path.join(ROOT, BLOCK))))
    w("- Script `scripts/audit_note_N12_gitleaks.py` sha256 `%s`; interpreter %s (Python %s)" % (
        sha256(os.path.abspath(__file__)), sys.executable, sys.version.split()[0]))
    shown = " ".join(cmd[:-1]).replace(rep, "<tmp>/report.json")
    if allow_commits is None:
        allow_s = "the count of commits adding or removing the inline-allow literal (%s) could not be computed" % (
            ALLOW_SHOWN)
    elif not allow_commits:
        allow_s = ("0 commits in history add or remove the inline-allow literal (%s; `git log --all --text -S`), "
                   "so the flag does not change this scan's result" % ALLOW_SHOWN)
    else:
        allow_s = ("%d commit(s) in history add or remove the inline-allow literal (%s; `git log --all --text -S`: "
                   "%s); the flag neutralises them (a note, not a STOP)" % (
                       len(allow_commits), ALLOW_SHOWN, ", ".join("`%s`" % c[:10] for c in allow_commits)))
    w("- gitleaks %s (installed by the PI; required: %s); command: `%s .`, run from the repo root with "
      "GIT_NO_REPLACE_OBJECTS=1. The report goes to a temporary directory and is deleted after reading. Secrets are "
      "redacted at source (`--redact=100`). `--ignore-gitleaks-allow` makes inline allow comments ineffective; %s. "
      "gitleaks exit code: %d. Report file: %s." % (
          ver, GITLEAKS_VERSION, shown, allow_s, r.returncode,
          "parsed, %d findings" % len(findings) if loaded is not None else "ABSENT OR UNPARSABLE -- STOP"))
    new_attr = sorted(set(attr_paths) - KNOWN_ATTR_PATHS)
    w("- Every file in history is rendered as text by git (`--text --no-textconv` in `--log-opts`, added to the "
      "block's `--all`). The repository's .gitattributes sets `/data/m/ckpt/** -diff`: Code's line, added in the m "
      "package BUILD commit `5f7b968`, whose comment says the path \"may carry a contrast pick and never renders in a "
      "diff or a log -p\" and cites PROPOSAL-m v1.11 m:318. m:318 is the Blinding paragraph: neither the seat nor the "
      "PI reads a pick-bearing artifact (checkpoints, transcripts, raw outputs) before that unit's VERDICTS are "
      "computed, outside four listed exceptions. Without `--text` git log prints \"Binary files ... differ\" on the "
      "-diff path and gitleaks does not read it; the PI's count of 2026-10-09 (4) includes no finding on this path. "
      "With `--text` the -diff path class is scanned: its blobs go only into gitleaks' pipe, gitleaks' output is "
      "redacted at source (`--redact=100`), the report is a temporary file, and nothing of that path's content enters "
      "this raw beyond gitleaks' redacted match. Paths in history with a diff or binary attribute set "
      "(`git log --all --name-only` through `git check-attr diff binary`; %d paths checked): %s%s." % (
          len(names), ", ".join("`%s`" % p for p in attr_paths) or "none",
          "" if attr_ok else " -- the attribute check did not complete (STOP)"))
    attr_v1 = [p for p in attr_paths if p in KNOWN_ATTR_PATHS_V1]
    attr_v2 = [p for p in attr_paths if p in KNOWN_ATTR_PATHS_ADDED_V2]
    if attr_v1 or attr_v2:
        w("- Of these, known at v1's release run (2026-10-12): %s; listed for the v2 release run on the PI's word of "
          "2026-10-28 (\"%s\", to the design seat's item C: results/raw/2026-10-28_note-design-to-code_release-block-"
          "answers.md, section 0; the seat's words, its section 5, 3b: \"%s\"; m:318's own words are those of the "
          "bullet above, \"before that unit's VERDICTS are computed\", and Q-F0's VERDICTS were computed on 2026-10-19, "
          "`bfc179c`): %s." % (
              ", ".join("`%s`" % p for p in attr_v1) or "none", PI_ANSWER_2026_10_28, SEAT_3B_BLIND_WORDS,
              ", ".join("`%s`" % p for p in attr_v2) or "none"))
    if new_attr:
        w("- Attribute path(s) not known at the release preparation -- STOP (whether gitleaks may read a -diff path "
          "is the PI's and the seat's question, path by path): %s." % ", ".join("`%s`" % p for p in new_attr))
    for ln in scanned:
        w("- gitleaks log: `%s`" % plain(ln))
    commits_line = any("commits scanned" in ln for ln in log)
    m_sc = [re.search(r"(\d+) commits scanned", plain(ln)) for ln in log]
    m_sc = [int(m.group(1)) for m in m_sc if m]
    n_scanned = m_sc[-1] if m_sc else None
    count_ok = n_scanned is not None and n_commits is not None and (
        n_scanned == n_commits or (deletion_only is not None and n_scanned == n_commits - len(deletion_only)))
    if not commits_line:
        w("- gitleaks log: no \"commits scanned\" line -- STOP (the history scan did not complete).")
    if deletion_only is None:
        del_s = "deletion-only commits could not be computed"
    else:
        del_s = "deletion-only commits (non-merge, files changed, no line added; gitleaks does not count them): %d%s" % (
            len(deletion_only), (" (" + ", ".join("`%s`" % c[:10] for c in deletion_only) + ")") if deletion_only else "")
    if count_ok and n_scanned == n_commits:
        verdict_s = "equal"
    elif count_ok:
        verdict_s = "equal after the deletion-only commits"
    else:
        verdict_s = "NOT EQUAL -- STOP"
    w("- Completeness: gitleaks scanned %s commits; `git rev-list --all --count` (GIT_NO_REPLACE_OBJECTS=1) = %s; "
      "merge commits: %s; %s; %s. Replace refs (`refs/replace/`): %d, disabled for this scan." % (
          n_scanned if n_scanned is not None else "an unknown number of",
          n_commits if n_commits is not None else "UNKNOWN", n_merges_r or "UNKNOWN", del_s, verdict_s, n_replace))
    n_err = len(errs) + len(derrs) + len(perrs) + len(serrs)
    if n_err:
        for lab, ls_ in (("history-scan", errs), ("release-copies", derrs), ("skip-probe", perrs),
                         ("skipped-path copies", serrs)):
            for ln in ls_:
                w("- gitleaks %s ERR line -- STOP: `%s`" % (lab, ln))
    else:
        w("- gitleaks ERR lines: 0 in each of the four logs (history scan, release copies, skip probe, skipped-path "
          "copies).")
    w("- Suppression inputs checked (.gitleaks.toml at the repo root; .gitleaksignore at the repo root and at the cwd "
      "the script was started from; "
      "GITLEAKS_CONFIG and GITLEAKS_CONFIG_TOML in the environment): %s." % (
          "none present, so gitleaks' default config applies" if not suppress
          else "PRESENT -- STOP: " + "; ".join(suppress)))
    refs = [x for x in git("for-each-ref", "--format=%(objectname) %(refname)", text=True).stdout.split("\n")
            if x.strip()]
    remotes = git("remote", text=True).stdout.split()
    w("- Refs scanned (`--all` in `--log-opts`): %d refs (`git for-each-ref`; listing sha256 `%s`); tags: %s; git remotes "
      "configured: %d." % (len(refs), hashlib.sha256("\n".join(refs).encode()).hexdigest()[:16],
                           ", ".join("`%s`" % x.split()[1][len("refs/tags/"):] for x in refs
                                     if x.split()[1].startswith("refs/tags/")) or "none", len(remotes)))
    fps = set(f.get("Fingerprint", "") for f in findings)
    four_found = sum(1 for k in PI_FOUR if k in fps)
    w("- The PI's report (routing of 2026-10-09): \"gitleaks over all history found 4 leaks\". This run finds %d; "
      "%d of the PI's four are re-found by fingerprint%s." % (
          len(findings), four_found, "" if four_found == 4 else " -- STOP"))
    w("")
    w("| # | rule | file | commit | line | match (secret redacted by gitleaks) | Code's verdict | reason |")
    w("|---|---|---|---|---|---|---|---|")
    untriaged = 0
    for i, f in enumerate(findings, 1):
        fp = f.get("Fingerprint", "")
        verdict, reason = TRIAGE.get(fp, ("UNTRIAGED", "no verdict recorded for this fingerprint"))
        if verdict == "UNTRIAGED":
            untriaged += 1
        match = (f.get("Match") or "").replace("|", "/").replace("\n", " ")[:80]
        w("| %d | %s | `%s` | `%s` | %s | `%s` | %s | %s |" % (
            i, f.get("RuleID"), f.get("File"), (f.get("Commit") or "")[:10], f.get("StartLine"), match, verdict, reason))
    w("")
    true_c = sum(1 for f in findings if TRIAGE.get(f.get("Fingerprint", ""), ("UNTRIAGED",))[0] == "TRUE-SECRET")
    missing = sorted(set(TRIAGE) - fps)
    w("## Release files: `gitleaks dir` over .txt copies")
    w("")
    dshown = " ".join(dcmd[:-1]).replace(drep, "<tmp>/dir_report.json")
    w("- gitleaks' default config skips `.svg` files by path (its global allowlist), so the history scan above does "
      "not read the renders (the three 2026-10-22 release renders, and the three 2026-10-10 renders of v1's release); "
      "the PI accepted that skip (answer of 2026-10-12, question 4), and the design seat's answers of 2026-10-28 "
      "(section 5, 3b; the PI's \"Yes to all\") add the three 2026-10-22 renders to the skip list on that basis; the next "
      "section scans every version of every skipped path as a copy. As a check on the release files themselves the "
      "five release files are read from HEAD's blobs (`git cat-file blob HEAD:<name>`), each blob's sha256 asserted "
      "and the working-tree file asserted equal, and the HEAD bytes written, each with `.txt` appended to its name, "
      "into a temporary directory and scanned there: `%s <tmp>/release`; exit code %d. Report file: %s." % (
          dshown, d_rc,
          "parsed, %d findings" % len(dfind) if dloaded is not None else "ABSENT OR UNPARSABLE -- STOP"))
    for ln in dscanned:
        w("- gitleaks log: `%s`" % plain(ln))
    dscan_line = any("scanned ~" in ln for ln in dlog)
    if not dscan_line:
        w("- gitleaks log: no \"scanned ~\" line -- STOP (the dir scan did not complete).")
    w("")
    w("| file | expected sha256 | sha256 of HEAD's blob | sha256 of the working-tree file | match |")
    w("|---|---|---|---|---|")
    for name, want, got, wt, ok in rel_rows:
        w("| `%s` | `%s` | `%s` | `%s` | %s |" % (name, want, got, wt, "yes" if ok else "NO -- STOP"))
    w("")
    if dfind:
        w("| # | rule | file (copy) | line | match (secret redacted by gitleaks) | Code's verdict |")
        w("|---|---|---|---|---|---|")
        for i, f in enumerate(dfind, 1):
            match = (f.get("Match") or "").replace("|", "/").replace("\n", " ")[:80]
            w("| %d | %s | `%s` | %s | `%s` | UNTRIAGED -- STOP |" % (i, f.get("RuleID"), f["File"], f.get("StartLine"), match))
        w("")
    w("## History paths gitleaks' default config skips")
    w("")
    sshown = " ".join(scmd[:-1]).replace(srep, "<tmp>/skipped_report.json")
    new_skip = sorted(set(skipped) - KNOWN_SKIP_PATHS)
    w("- Measured, not assumed: a throwaway probe file holding one random generic-api-key line (generated at run "
      "time, never written out) is written at each of the %d history paths in %d temporary probe director%s (a "
      "second one only when two paths would collide: a file that is another path's directory, or two paths equal "
      "ignoring case), and `gitleaks dir` is run over each with the default config. %d paths probed, %d not "
      "probed%s; %d probed paths gave a finding. Paths with no finding, i.e. skipped by the default config's global "
      "path allowlist (measured in `gitleaks dir`; the same allowlist applies to `gitleaks git`): %s.%s" % (
          len(names_s), len(prounds), "y" if len(prounds) == 1 else "ies", len(probed), len(unprobed),
          (" (" + ", ".join("`%s`" % x for x in unprobed) + ") -- STOP") if unprobed else "",
          len(found & set(probed)), ", ".join("`%s`" % x for x in skipped) or "none",
          "" if p_ok else " The probe did not complete (a report absent or unparsable, or no \"scanned ~\" line) -- STOP."))
    if new_skip:
        w("- Skipped path(s) not known at the release preparation -- STOP: %s." % ", ".join("`%s`" % x for x in new_skip))
    # Listed as skipped, but the probe found them read (not a STOP: the history scan reads them); shown, not assumed.
    read_listed = sorted(set(probed) & found & KNOWN_SKIP_PATHS)
    if read_listed:
        w("- Listed as skipped (KNOWN_SKIP_PATHS) but read by the default config (the probe gave a finding there, so the "
          "history scan reads them; not a STOP): %s." % ", ".join("`%s`" % x for x in read_listed))
    w("- Every historical version of each skipped path (`git log --all -m --no-renames -- <path>`, each commit's "
      "blob, deduplicated) is written as a `.txt` copy into a temporary directory and scanned: `%s <tmp>/skipped`; "
      "exit code %d. Versions per path: %s; distinct blobs copied: %d. Report file: %s." % (
          sshown, s_rc, ", ".join("`%s` %d" % (p, n) for p, n in skip_rows) or "none", len(seen_blobs),
          "parsed, %d findings" % len(sfind) if sloaded is not None else "ABSENT OR UNPARSABLE -- STOP"))
    for ln in slog:
        if "scanned ~" in ln or "leaks found" in ln or "no leaks" in ln:
            w("- gitleaks log: `%s`" % plain(ln))
    sscan_line = any("scanned ~" in ln for ln in slog)
    if not sscan_line:
        w("- gitleaks log: no \"scanned ~\" line -- STOP (the skipped-path scan did not complete).")
    if not s_ok:
        w("- A skipped path's versions could not all be read -- STOP.")
    if sfind:
        w("")
        w("| # | rule | file (copy: n_blob10_name) | line | match (secret redacted by gitleaks) | Code's verdict |")
        w("|---|---|---|---|---|---|")
        for i, f in enumerate(sfind, 1):
            match = (f.get("Match") or "").replace("|", "/").replace("\n", " ")[:80]
            w("| %d | %s | `%s` | %s | `%s` | UNTRIAGED -- STOP |" % (i, f.get("RuleID"), f["File"], f.get("StartLine"), match))
    w("")
    w("## Outcome")
    w("")
    w("- History findings: %d. TRUE-SECRET: %d. FALSE-POSITIVE: %d. UNTRIAGED: %d." % (
        len(findings), true_c, len(findings) - true_c - untriaged, untriaged))
    w("- TRIAGE entries re-found: %d of %d.%s" % (
        len(TRIAGE) - len(missing), len(TRIAGE),
        "" if not missing else " Not re-found -- STOP (history only grows, so every triaged finding must recur): %s."
        % ", ".join("`%s`" % m for m in missing)))
    w("- Release-file copies (HEAD's blobs): %d findings; release files absent at HEAD or with a hash mismatch: %d." % (
        len(dfind), rel_bad))
    w("- Skipped history paths: %d (%s); their %d historical versions as copies: %d findings." % (
        len(skipped), ", ".join("`%s`" % x for x in skipped) or "none", sum(n for _p, n in skip_rows), len(sfind)))
    # release v2: each entry added after v1's six is a finding new since v1's release run, a fresh STOP under the seat's
    # item A unless TRIAGE_V2_PI records the PI's dated words resolving it
    added_v2 = list(TRIAGE)[TRIAGE_V1_N:]
    added_v2_open = [k for k in added_v2 if k not in TRIAGE_V2_PI]
    w("- Of the triaged findings, the %d entries of v1's release run (2026-10-12): two are in this audit's own triage "
      "table (`961e90a`); the others are a content hash "
      "in a G-CAL gate artifact, a claim identifier in an e2d values-check record, and (added for v1's release run) a "
      "source file's sha256 in the G-SHAPE-F0 gate's provenance (`f23b444`, dated 2026-10-10, after the PI's scan) "
      "and the same G-CAL key-set hash in the G-CAL checkpoint's identity (`cf8eb5b`, data/m/ckpt/, read only by the "
      "--text scan; verified 64-character lowercase hex equal to gcal.py's key_set_sha256 without reading the "
      "blinded file out). "
      "All are matched by the generic-api-key rule on a field, column or path word ('token', 'key', 'key_set_sha256', "
      "'keys'). TRIAGE entries added for the v2 release run (findings new since v1's release run): %d%s." % (
          TRIAGE_V1_N, len(added_v2),
          (" (" + "; ".join("`%s` %s, %s" % (
              k, TRIAGE[k][0], ("the PI's words of %s: \"%s\"" % TRIAGE_V2_PI[k]) if k in TRIAGE_V2_PI
              else "no PI ruling recorded -- a fresh STOP (the seat's item A)") for k in added_v2) + ")")
          if added_v2 else ""))
    th_path = shutil.which("trufflehog")
    svg_b, th_b = item4_parts()
    w("- Block :77 makes any hit in history a STOP on the release that the PI resolves, and history rewriting is "
      "the PI's decision. The PI's D1 routing (2026-10-09) is to leave history as is. trufflehog is not run by this "
      "script (%s). Item 4's basis on this run, by part: %s; %s. The default config also skips the .png listed above; "
      "its versions are scanned as copies in the section above." % (
          "not installed: `shutil.which` finds no trufflehog" if not th_path
          else "installed on this machine; it runs in its own script, `%s`" % TRUFFLEHOG_SCRIPT, svg_b, th_b))
    reasons = []
    if untriaged:
        reasons.append("%d untriaged finding(s)" % untriaged)
    if true_c:
        reasons.append("%d true secret(s)" % true_c)
    if dfind:
        reasons.append("%d finding(s) on the release-file copies" % len(dfind))
    if rel_bad:
        reasons.append("%d release file(s) absent at HEAD or with a hash mismatch" % rel_bad)
    if missing:
        reasons.append("%d TRIAGE entr(ies) not re-found" % len(missing))
    if added_v2_open:
        reasons.append("%d finding(s) new since v1's release run with no PI ruling recorded (TRIAGE entries added for "
                       "v2: %s) -- a fresh STOP under the design seat's item A (\"any new finding is a fresh STOP\"); "
                       "the PI resolves it" % (len(added_v2_open), ", ".join("`%s`" % k for k in added_v2_open)))
    if loaded is None:
        reasons.append("the history report is absent or does not parse")
    if dloaded is None:
        reasons.append("the dir report is absent or does not parse")
    if not commits_line:
        reasons.append("no \"commits scanned\" line in the history scan's log")
    if not dscan_line:
        reasons.append("no \"scanned ~\" line in the dir scan's log")
    if ver != GITLEAKS_VERSION:
        reasons.append("gitleaks version %r, not %s" % (ver, GITLEAKS_VERSION))
    if suppress:
        reasons.append("suppression input(s) present: " + "; ".join(suppress))
    if not count_ok:
        reasons.append("gitleaks' commits-scanned count (%s) is not git rev-list --all --count (%s)" % (
            n_scanned, n_commits))
    if n_err:
        reasons.append("%d ERR line(s) in gitleaks' logs" % n_err)
    if not attr_ok:
        reasons.append("the attribute check over history's paths did not complete")
    if new_attr:
        reasons.append("%d attribute path(s) not known at the release preparation" % len(new_attr))
    if unprobed or not p_ok:
        reasons.append("the skip probe did not cover every history path")
    if new_skip:
        reasons.append("%d skipped path(s) not known at the release preparation" % len(new_skip))
    if sfind:
        reasons.append("%d finding(s) on the skipped-path copies" % len(sfind))
    if sloaded is None or not sscan_line or not s_ok:
        reasons.append("the skipped-path scan did not complete")
    stop = bool(reasons)
    if stop:
        w("- STOP: %s. The release waits on the PI." % "; ".join(reasons))
    else:
        new_s = ("no finding new since v1's release run (TRIAGE entries added for v2: 0)" if not added_v2 else
                 "%d finding(s) new since v1's release run, each resolved by the PI's dated words (TRIAGE_V2_PI): %s" % (
                     len(added_v2), "; ".join("`%s` (the PI, %s: \"%s\")" % ((k,) + TRIAGE_V2_PI[k]) for k in added_v2)))
        # release v2: the PI's basis is recorded in the release raw only; a rehearsal or a re-run says so instead
        if rel_raw:
            basis_s = ("%s %s This raw is gitleaks' part of that condition (0 true-secret candidates, 0 untriaged, and "
                       "no finding new since v1's release run without the PI's word), %s is the history script's and %s "
                       "trufflehog's (the PI's words of 2026-10-29); (i) carries only when all three pass their parts (0 "
                       "true-secret candidates and 0 untriaged in each; the history raw's STOP set also holds any "
                       "IDENTIFIER value with no entry)." % (BASIS_V2, BASIS_V2_SOURCE, HIST_RAW, TRUFFLEHOG_RAW))
        else:
            basis_s = ("(A rehearsal or a re-run: --out is not the release raw `%s`, which alone records the basis of "
                       "(i).)" % DEFAULT_OUT)
        w("- gitleaks' part of (i): 0 TRUE-SECRET and 0 UNTRIAGED in history (every file rendered as text by git, "
          "the -diff path class included; gitleaks' default global path allowlist skips %d history paths, %s, and "
          "every version of each is scanned as a copy with 0 findings), every TRIAGE entry re-found, %s, every scan "
          "completed on the default config (commits scanned = git rev-list --all --count less any listed "
          "deletion-only commits, 0 ERR lines); 0 findings on the release-file copies; the five release files at "
          "HEAD match. %s %s" % (
              len(skipped), ", ".join("`%s`" % x for x in skipped), new_s, basis_s, coverage_v2(head, tag_c, rel_raw)))
    text = "\n".join(out) + "\n"
    # the write guard: the origin-only ref the answers name is never written (its classes are named, never its values)
    bad = guarded(text, tvals)
    if bad:
        print("refused: the raw would carry %s; nothing written" % "; ".join(bad))
        return 2
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s: %d history findings, %d untriaged, %d true-secret; release copies: %d findings, %d hash mismatches; "
          "skipped paths %d, their copies %d findings" % (shown_path(outp, rel_out), len(findings), untriaged, true_c,
                                                          len(dfind), rel_bad, len(skipped), len(sfind)))
    return 1 if stop else 0


if __name__ == "__main__":
    sys.exit(main())
