#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12(vi) content pre-screen (part N12-screen).

Read-only on the record. A mechanical pre-screen, for the release scrub's
content review (block N12(vi), lines 72-85), of everything N12(vi) names that
will become public with the repository's full history:

  * every tracked file under results/raw/ at the pinned revision;
  * every tracked HANDOFF-*.md at the pinned revision (any directory);
  * every path that exists in history but not at the pinned revision -- the
    block's command (git log --all --diff-filter=D --name-only) and, as a
    supplement, the same with --no-renames plus (all paths ever touched minus
    the revision's tree), each screened at the version its deleting commit's
    first parent held;
  * every commit message reachable from --all (raw commit objects), every
    annotated tag's message, and the identity / signature headers of both.

Content is read from git objects (git cat-file --batch), never from the
working tree, so a concurrent session's uncommitted edits are not screened.

REDACTION. The output is committed to a repository that is about to be public.
No candidate secret, full infrastructure id, IP address, SSH key name or
fingerprint, non-allowlisted e-mail address, phone number, street address or
third-party name is written verbatim. Each value is reported as
    first 4 characters (fewer for a short value: at most half its length) + '...' + length + ':' + first 8 hex of its sha256
and every excerpt (a window of <= 40 characters) is cut from a line in which
every such span has first been replaced by a placeholder ([EMAIL] [PHONE]
[ADDR] [IP] [CRED] [ID] [TOK] [NAME] [W]; round 10: [SCRATCH_PATH]
[MACOS_TEMP_PATH] [LOCAL_HOME_PATH] [CLAUDE_AI_URL] [TRANSCRIPT_ID] [ID_FLAG];
a token the window cuts, other than a plain word, is replaced by [CUT]).

Stdlib only. Writes exactly one file (the JSON, refuses to overwrite) and a
summary to stdout.

Round 9 (2026-10-10): the Digest seat's three filed 2026-10-10 figure SVGs each
carry a C2PA content-credentials element (<c2pa:manifest>, base64). The PI,
2026-10-10, verbatim: "declare it ahead of the N12 pre-flip re-scan as a known
high-entropy false positive". It covers the element of those three renders
only; the 2026-10-09 renders they replace are not declared. Code's
implementation, not the PI's words: a hit lying wholly inside the text content
of a declared <c2pa:manifest>...</c2pa:manifest> element is FALSE-POSITIVE with
the reason C2PA_REASON, and only there. A declared element is bound to its
location and to its exact blob (C2PA_MANIFESTS: the object's repository path,
a root .svg path matched exactly, the blob's length and sha256); the same
string anywhere else (another path or directory, another element, an edited
blob) is screened as before. A declared hit keeps its category and redacted
form, is still covered by the leak guard, and carries verdict/reason/context
fields; its value's subtype gains the suffix '@c2pa_declared'. Scope is
unchanged: a root .svg is screened only if it ever becomes a history-only path.

Round 10 (2026-10-12): the excerpt masker also masks, whole, every local scratch
path, macOS per-user temp path, local home-directory path, claude.ai session URL
tail and uuid-shaped id (EXCERPT_CLASS_RXS; placeholders [SCRATCH_PATH]
[MACOS_TEMP_PATH] [LOCAL_HOME_PATH] [CLAUDE_AI_URL] [TRANSCRIPT_ID]), so the
release JSON quotes none of them where its committed predecessor did. Excerpts
only: every count, verdict, category, locator and redacted value is unchanged,
and so is the leak guard.

Round 10, release (2026-10-12): the release JSON is itself screened by the
history and licenses scans once it is committed, so an excerpt must add no
value those scans would read as new. Three excerpt-only changes (EXCERPT_* below):
(a) on a line that names ssh, an identity-file flag is masked together with its
argument as [ID_FLAG], so no identity-flag pattern reads a placeholder as a file
name; (b) a token the 40-character window cuts at either end -- a run of
characters between the delimiters of EXCERPT_PATH_STOP_RX -- is replaced, its
cut part only, by [CUT] unless the cut part is a plain word (ASCII letters
only) of a token that holds no host, URL, path or address shape; where the hit
itself lies in the token cut at the left, the window starts at that token
instead when the hit is within 30 characters of it; where the window's right
end cuts a run of characters other than whitespace, a quote, a backtick or
a closing parenthesis or bracket (tokens joined by angle brackets, braces,
opening brackets, pipes, commas or semicolons), the run's
part in the window up to the end of its last token with such a shape is
replaced by [CUT] too; so no excerpt starts or ends inside a token with a
host, URL, path or id shape, and none ends inside such a joined run (one can
start inside a joined run's later token), and a replaced part can lengthen the
excerpt by at most the placeholder's length at each end; (c) every
non-printable character is mapped to a space before masking rather than after,
so the masks read the text the excerpt shows. Counts, verdicts, categories,
locators, redacted values and the leak guard are unchanged.

Release v2 (2026-11-02), N12(vi)'s retained finding: c2a6417 removed two
third-party names from line 5 of a committed raw on the PI's word of
2026-10-29. They remain in that file's blob at 908a659, the version that
commit added, which no part of the scope above reads (the file is in the tree,
and no commit deletes it). Code's question of 2026-11-01 and the PI's answer of
2026-11-02 are verbatim in RETAINED_QUESTION and RETAINED_PI_WORDS: history is
kept, and this screen's raw records the finding as it is, with the PI's reason
(RETAINED_REASON, the answer's own parenthesis). Every run checks each RETAINED
entry against the git objects and records it in the JSON's retained_in_history
section: the blob's given-name pairs as this screen's name tiers count them
(with the run's allowlist, et-al surnames included); the removing commit, which
replaced that blob and changed that path and line only, leaving no pair on the
line; no pair on it at --rev either; the other categories' counts equal in both
versions; the blob in --rev's history; and the pairs in no other commit's patch
(the pickaxe, over --all), no commit message, no file in the tree at --rev and
no other object this screen reads. A mismatch exits without writing. The
section holds counts, line numbers and object ids only. Each pair found joins
the leak guard, so the guard asserts that the JSON and the summary hold none of
them. The section adds nothing to the objects or the totals. With
--retained-only, a run writes the header, the name tiers' method, that section
and the leak guard only. It still reads the whole scope, for the et-al
allowlist the tiers use.

    jlens-qwen36/.venv/bin/python scripts/audit_note_N12_content.py \
        [--rev HEAD] [--json-out results/raw/2026-10-08_note-N12-content-screen.json] [--retained-only]
"""
import argparse
import datetime
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PART = "N12-screen"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
DEFAULT_OUT = os.path.join("results", "raw", "2026-10-08_note-N12-content-screen.json")
EXCERPT_MAX = 40
# Round 9: the 'method' entries whose text is derived from the screened corpus; every other 'method' entry, and the
# 'patterns' block, is this script's constant text, which the leak guard does not read (see main()).
CONTENT_DERIVED_METHOD_KEYS = ("name_allowlist_et_al_detected", "hex_tokens_skipped")

# Round 9 (2026-10-10): the PI's declaration, verbatim in C2PA_REASON, made ahead of the N12 pre-flip re-scan (see the
# docstring); it covers the element of the three filed 2026-10-10 renders only. Repository path (a root path) ->
# (length, sha256) of the element's text content, the exact base64 blob. The decode in the reason is Code's.
C2PA_PI_WORDS = "declare it ahead of the N12 pre-flip re-scan as a known high-entropy false positive"
C2PA_REASON = ('the PI, 2026-10-10: "' + C2PA_PI_WORDS + '" (it: the C2PA content-credentials element of each filed '
               "2026-10-10 render); Code's read-only decode, not the PI's words: a base64 JUMBF content-credentials "
               "manifest, no secret")
C2PA_CONTEXT = "c2pa_content_credentials_manifest"
C2PA_ELEMENT_RX = re.compile(r"<c2pa:manifest>([A-Za-z0-9+/=]*)</c2pa:manifest>")
C2PA_MANIFESTS = {
    "2026-10-10_F1a_headline-strip.svg": (7684, "da236ea489a9226b5064a30c19e29c83345451a4e2728ef7641fc908fcba349f"),
    "2026-10-10_F1b_five-link-panels.svg": (7684, "ee0ea5730fa34810d240782be92da1a4977e41bcb1518c01d7e7a86281c581f5"),
    "2026-10-10_F2_macar-lineage-roc_post.svg": (7684, "f814df3b308262c8e137b825f3e822dbb5c68357eda406f1d7404bb5186c7c9b"),
}

# Release v2 (2026-11-02): N12(vi)'s retained finding (see the docstring). Code's question and the PI's answer, each with
# its PI-local date, verbatim; the reason is the answer's own parenthesis, asserted to be in it. Each RETAINED entry: the
# path, the commit whose version of it holds the names, the commit that removed them, the line, and the number of tier-b
# given-name pairs that version holds (counts only; no name is written here).
RETAINED_QUESTION = ("2026-11-01", "Should a history rewrite remove the two names still in 908a659's blob?")
RETAINED_PI_WORDS = ("2026-11-02", "Keep history. Have the content screen’s raw record the finding exactly as it is — "
                     "two third-party names in blob 908a659, removed from the tree at c2a6417, retained in history, with "
                     "the reason (no private content; published co-authors of a cited paper) — so the scrub index carries "
                     "the disposition rather than a reader discovering it.")
RETAINED_REASON = "no private content; published co-authors of a cited paper"
assert "(" + RETAINED_REASON + ")" in RETAINED_PI_WORDS[1]
RETAINED = [{"path": "results/raw/2026-10-28_note-N1-r11_correspondence-figures.md", "blob_at": "908a659",
             "removed_at": "c2a6417", "line": 5, "tier_b_given_name_pairs": 2}]

# E-mail addresses counted separately, never listed as hits (task text).
EMAIL_ALLOW = {
    "jasonmdwyer@gmail.com": "author_own",
    "noreply@anthropic.com": "anthropic_noreply",
}
# Identity names printed verbatim in the identities table (the author; the AI
# tool identities). Any other name in a commit/tag header is redacted.
IDENTITY_NAME_ALLOW = {"Jason Dwyer", "Claude", "Claude Cowork"}

# Name heuristic allowlist: cited authors named by the task, the author, and
# model / organisation names. Surnames seen as "<Surname> et al" anywhere in
# the screened corpus are added at run time (reported as such).
NAME_ALLOW = {
    "Macar", "Chua", "Anthropic", "Dwyer", "Claude", "Opus", "Sonnet", "Haiku",
    "Qwen", "Olmo", "OLMo", "Allen",
}
NAME_PAIR_ALLOW = {("Jason", "Dwyer")}

# Common given names (English-language and some international), minus words
# that are ordinary English or technical words when capitalised (Will, May,
# Mark, Max, Bill, Art, Chase, Dean, Frank, Grace, Joy, June, April, Rose,
# Faith, Hope, Ray, Pat, Rob, Sue, Gene, Lane, Page, Summer, Hunter, Mason,
# Cooper, Carter, Parker, Victoria, Sydney, Austin, Georgia, Florence, Claude).
GIVEN_NAMES = set("""
Aaron Abigail Adam Adrian Aidan Aisha Alan Albert Alex Alexander Alexandra
Alexis Alice Alicia Alison Allison Amanda Amber Amelia Amy Ana Andrea Andrew
Andy Angela Anita Ann Anna Anne Annie Anthony Antonio Arjun Arthur Ashley
Audrey Barbara Ben Benjamin Bernard Beth Betty Beverly Bob Bobby Brad Bradley
Brandon Brenda Brian Brittany Bruce Bryan Caitlin Cameron Carl Carla Carlos
Carol Caroline Carolyn Catherine Charles Charlie Charlotte Chelsea Cheryl
Chloe Chris Christian Christina Christine Christopher Cindy Claire Clara
Colin Connor Craig Crystal Cynthia Daniel Danielle Daniela David Debbie
Deborah Debra Denise Dennis Derek Diana Diane Diego Dominic Donald Donna
Doris Dorothy Douglas Dylan Edward Eileen Elaine Eleanor Elena Eli Elijah
Elizabeth Ella Ellen Emily Emma Eric Erica Erin Ethan Eugene Eva Evan Evelyn
Fatima Felix Fernando Fiona Francesca Francis Gabriel Gabriela Gary Gavin
Geoffrey George Gerald Gillian Gloria Gordon Greg Gregory Hannah Harold
Harriet Harrison Hayden Heather Helen Henry Hiroshi Holly Howard Hugh Hugo
Ian Isaac Isabel Isabella Isabelle Ivan Jacob Jacqueline Jake James Jamie Jan
Jane Janet Janice Jared Jasmine Jason Javier Jeff Jeffrey Jennifer Jenny
Jeremy Jerry Jesse Jessica Jill Jim Jimmy Joan Joanna Joanne Joe Joel John
Johnny Jonathan Jordan Jorge Jose Joseph Josephine Josh Joshua Joyce Juan
Judith Judy Julia Julian Julie Justin Karen Kate Katherine Kathleen Kathryn
Kathy Katie Keith Kelly Ken Kenneth Kevin Kim Kimberly Kyle Laura Lauren
Lawrence Leah Lena Leo Leon Leonard Lily Linda Lindsay Lisa Liam Logan Lori
Louis Louise Lucas Lucy Luis Luke Lydia Madison Maria Marie Marilyn Marina
Mario Marion Martha Martin Mary Matthew Megan Melanie Melissa Mia Michael
Michelle Miguel Mike Mila Miriam Mohammed Mohammad Molly Monica Nancy Naomi
Natalie Nathan Neil Nicholas Nick Nicole Noah Nora Olga Oliver Olivia Omar
Oscar Owen Pablo Pamela Patricia Patrick Paul Paula Pedro Peggy Peter Philip
Phillip Priya Rachel Rafael Rahul Ralph Raymond Rebecca Regina Renee Rhys
Ricardo Richard Rick Robert Roberto Robin Roger Ronald Rosa Ross Roy Ruby Russell
Ruth Ryan Sally Samantha Samuel Sandra Sara Sarah Scott Sean Sebastian Sergio
Sharon Shawn Sheila Shirley Simon Sofia Sophia Sophie Stacy Stephanie Stephen
Steve Steven Stuart Susan Suzanne Tamara Tanya Teresa Terry Theodore Theresa
Thomas Tiffany Tim Timothy Tina Todd Tom Tony Tracy Travis Trevor Tyler
Valerie Vanessa Vera Veronica Victor Vincent Virginia Walter Wanda Wayne Wei
Wendy William Xavier Yuki Yusuf Zachary Zoe
""".split())

# --------------------------------------------------------------------------
# Patterns. Each category: list of (subtype, compiled regex, value group).
# --------------------------------------------------------------------------
I = re.IGNORECASE

EMAIL_RX = re.compile(r"(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![A-Za-z0-9-])")

PHONE_RXS = [
    ("nanp", re.compile(r"(?<![\w.+/-])(?:\+?1[ .-]?)?\(?[2-9]\d{2}\)?[ .-]\d{3}[ .-]\d{4}(?![\w.-])")),
    ("international_plus", re.compile(r"(?<![\w.+/])\+\d{1,3}(?:[ .-]?\(?\d{1,4}\)?){2,5}(?![\w.])")),
    ("au_landline", re.compile(r"(?<![\w.+/-])(?:\(0[2378]\)|0[2378])[ -]?\d{4}[ -]?\d{4}(?![\w.-])")),
    ("au_mobile", re.compile(r"(?<![\w.+/-])04\d{2}[ -]?\d{3}[ -]?\d{3}(?![\w.-])")),
]

STREET_TYPES = (r"Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|"
                r"Crescent|Cres|Parade|Pde|Terrace|Tce|Highway|Hwy|Place|Pl|Way|Close|Square|Sq")
ADDR_RXS = [
    ("number_street", re.compile(r"\b\d{1,5}[A-Za-z]?(?:/\d{1,5})?\s+(?:[A-Z][a-z]+\s+){1,3}(?:" + STREET_TYPES + r")\b\.?")),
    ("po_box", re.compile(r"\bP\.?\s?O\.?\s+Box\s+\d+", I)),
]

IPV4_RX = re.compile(r"(?<![\d.])(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?![\d.])")

URL_RX = re.compile(r"\b(?:https?|ftp|ssh|git|wss?)://[^\s<>\"'`\)\]\}|\\]+", I)
WWW_RX = re.compile(r"(?<![\w./@-])www\.[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+[^\s<>\"'`\)\]\}|\\]*", I)

CONF_RXS = [
    ("confidential", re.compile(r"\bconfidential\w*", I)),
    ("private", re.compile(r"\bprivate\b", I)),
    ("do not share", re.compile(r"\bdo\s+not\s+share\b", I)),
    ("not for publication", re.compile(r"\bnot\s+for\s+publication\b", I)),
    ("internal only", re.compile(r"\binternal[\s-]+only\b", I)),
    ("NDA", re.compile(r"\bNDAs?\b")),
    ("embargo", re.compile(r"\bembargo\w*", I)),
    ("off the record", re.compile(r"\boff\s+the\s+record\b", I)),
]

CORR_RXS = [
    ("From:", re.compile(r"\bFrom:")),
    ("To:", re.compile(r"\bTo:")),
    ("Subject:", re.compile(r"\bSubject:")),
    ("Dear ", re.compile(r"\bDear\s")),
    ("Hi ", re.compile(r"\bHi\s")),
    ("wrote:", re.compile(r"\bwrote:")),
    ("Sent from", re.compile(r"\bSent\s+from\b")),
    ("Best,", re.compile(r"\bBest,")),
    ("Regards", re.compile(r"\bRegards\b")),
]

PERS_RXS = [
    ("my wife", re.compile(r"\bmy\s+wife\b", I)),
    ("my husband", re.compile(r"\bmy\s+husband\b", I)),
    ("my partner", re.compile(r"\bmy\s+partner\b", I)),
    ("my kid", re.compile(r"\bmy\s+kid\w*", I)),
    ("doctor", re.compile(r"\bdoctor\w*", I)),
    ("hospital", re.compile(r"\bhospital\w*", I)),
    ("diagnos", re.compile(r"\w*diagnos\w*", I)),
    ("salary", re.compile(r"\bsalar(?:y|ies)\b", I)),
    ("bank", re.compile(r"\bbank\w*", I)),
]

# Credential-shaped strings. Group 'v' is the value redacted (whole match if absent).
CRED_RXS = [
    ("private_key_block", re.compile(r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY(?: BLOCK)?-----")),
    ("ssh_or_pgp_armor", re.compile(r"-----BEGIN (?:SSH SIGNATURE|PGP SIGNATURE|PGP MESSAGE|OPENSSH [A-Z ]+)-----")),
    ("aws_access_key", re.compile(r"\b(?P<v>(?:AKIA|ASIA)[0-9A-Z]{16})\b")),
    ("sk_api_key", re.compile(r"(?<![A-Za-z0-9])(?P<v>sk-(?:ant-|proj-)?[A-Za-z0-9_\-]{20,})")),
    ("runpod_api_key", re.compile(r"(?<![A-Za-z0-9])(?P<v>rpa?_[A-Za-z0-9]{16,})")),
    ("hf_token", re.compile(r"(?<![A-Za-z0-9])(?P<v>hf_[A-Za-z0-9]{30,})")),
    ("github_token", re.compile(r"(?<![A-Za-z0-9])(?P<v>(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}))")),
    ("slack_token", re.compile(r"(?<![A-Za-z0-9])(?P<v>xox[abprs]-[A-Za-z0-9-]{10,})")),
    ("google_api_key", re.compile(r"(?<![A-Za-z0-9])(?P<v>AIza[0-9A-Za-z_\-]{35})")),
    ("jwt", re.compile(r"(?<![A-Za-z0-9])(?P<v>eyJ[A-Za-z0-9_-]{8,}\.eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,})")),
    ("ssh_public_key", re.compile(r"\b(?:ssh-(?:rsa|ed25519|dss)|ecdsa-sha2-nistp\d+|sk-ssh-ed25519@openssh\.com)\s+(?P<v>AAAA[0-9A-Za-z+/=]{16,})")),
    ("ssh_fingerprint", re.compile(r"(?<![A-Za-z0-9])(?P<v>(?:SHA256:[A-Za-z0-9+/]{43}|MD5:(?:[0-9a-f]{2}:){15}[0-9a-f]{2}))")),
    ("url_userinfo", re.compile(r"\b[a-z][a-z0-9+.-]*://(?P<v>[^\s/:@]+:[^\s/@]+)@", I)),
    ("bearer", re.compile(r"\bBearer\s+(?P<v>[A-Za-z0-9_\-.=+/]{16,})")),
    ("keyword_assignment", re.compile(
        r"\b(?:api[_-]?key|secret(?:[_-]?key)?|token|passw(?:or)?d|passphrase|auth[_-]?token|access[_-]?key|"
        r"private[_-]?key|client[_-]?secret)\b[\"']?\s*(?::|=|=>)\s*[\"']?(?P<v>[A-Za-z0-9_\-.+/=]{12,})", I)),
]
GENERIC_TOKEN_RX = re.compile(r"(?<![A-Za-z0-9])[A-Za-z0-9]{24,}(?![A-Za-z0-9])")
HEX_RX = re.compile(r"^[0-9a-fA-F]+$")

# Infrastructure identifiers (supplementary; also masked in every excerpt).
INFRA_RXS = [
    ("runpod_proxy_host", re.compile(r"(?<![A-Za-z0-9])(?P<v>[a-z0-9]{8,24})-\d{2,5}\.proxy\.runpod\.net", I)),
    ("runpod_ssh_user", re.compile(r"(?<![A-Za-z0-9])(?P<v>[a-z0-9]{8,24}-[0-9a-f]{6,})@ssh\.runpod\.io", I)),
    ("labelled_infra_id", re.compile(
        r"\b(?:pod|volume|network[ _-]?volume|endpoint|template|instance|machine)[ _-]?id\b[`'\"]?\s*(?:[:=]|is)?\s*[`'\"]?"
        r"(?P<v>(?=[A-Za-z0-9_-]*\d)[A-Za-z0-9_-]{6,40})", I)),
    ("runpod_env_id", re.compile(r"\bRUNPOD_(?:POD_ID|POD_HOSTNAME|PUBLIC_IP|TCP_PORT_\d+)\b\s*[:=]\s*[`'\"]?(?P<v>[^\s`'\"]{4,})")),
    ("ssh_key_path", re.compile(r"(?:~|\$HOME|/Users/[^/\s]+|/home/[^/\s]+|/root)/\.ssh/(?P<v>[A-Za-z0-9_.@+-]+)")),
    ("ssh_identity_flag", re.compile(r"\bssh\b[^\n]*?\s-i\s+(?P<v>\S+)")),
]

# Round 10 (2026-10-12): excerpt-only path classes. The standing redaction rules keep local scratch paths, local temp
# paths, claude.ai session URLs and local transcript ids out of every new public output, and the screened corpus quotes
# them (committed raws, and this part's own committed 2026-10-08 JSON). Each anchor below marks a path token, which is
# masked WHOLE in every excerpt -- extended left and right up to a character of EXCERPT_PATH_STOP_RX, trailing '.' and
# ':' left as punctuation -- by the placeholder naming its class. Excerpts only: no count, verdict, category or locator
# reads them.
# (placeholder, anchor, precedence: lower wins where two classes overlap)
EXCERPT_PATH_STOP_RX = re.compile(r"[\s\"'`<>\\()\[\]{}|,;]")
EXCERPT_CLASS_RXS = [
    ("[SCRATCH_PATH]", re.compile(r"/tmp/(?=[^\s\"'`<>\\()\[\]{}|,;])"), -7),           # /private/tmp/..., /tmp/...
    ("[SCRATCH_PATH]", re.compile(r"(?<![A-Za-z0-9])claude-\d{3,}(?!\d)"), -7),          # the per-uid scratch directory
    ("[SCRATCH_PATH]", re.compile(r"-Users-"), -7),                                      # the per-user project-slug form
    ("[MACOS_TEMP_PATH]", re.compile(r"/var/folders/(?=[^\s\"'`<>\\()\[\]{}|,;])"), -6),  # /var/folders/<2>/<per-user>/...
    ("[LOCAL_HOME_PATH]", re.compile(r"/Users/(?=[A-Za-z0-9_])"), -5),                   # a local home-directory path
    ("[CLAUDE_AI_URL]", re.compile(r"claude\.ai/code/", I), -4),                         # a session URL and its tail
    ("[TRANSCRIPT_ID]", re.compile(r"(?<![0-9A-Fa-f])[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
                                   r"(?![0-9A-Fa-f])", I), -3),                         # a uuid-shaped id
]


def excerpt_path_token(line, s, e):
    """Round 10: the whole path token around the anchor [s, e): extended over every character that is not whitespace
    or one of the delimiters of EXCERPT_PATH_STOP_RX; trailing '.' and ':' are left outside as punctuation."""
    while s > 0 and not EXCERPT_PATH_STOP_RX.match(line[s - 1]):
        s -= 1
    n = len(line)
    while e < n and not EXCERPT_PATH_STOP_RX.match(line[e]):
        e += 1
    while e > s and line[e - 1] in ".:":
        e -= 1
    return s, e


# Round 10, release (2026-10-12): excerpt-only rules so the release JSON, once committed and screened in its turn by
# the history and licenses scans, adds no value either reads as new. Not in EXCERPT_CLASS_RXS (the message screen
# imports that table as path anchors).
# (a) On a line naming ssh (any case, anywhere), every identity-file flag together with its argument -- a '-i' or
#     '-I' at the line start or after whitespace, then whitespace and a run of non-space -- is one span, masked as
#     [ID_FLAG]; lowest precedence, so it absorbs any placeholder inside it. The INFRA identity-flag pattern is
#     case-sensitive and masked only the argument, leaving the flag before an [ID] placeholder.
EXCERPT_SSH_WORD_RX = re.compile(r"ssh", I)
EXCERPT_ID_FLAG_RX = re.compile(r"(?<!\S)-i\s+\S+", I)
EXCERPT_ID_FLAG = ("[ID_FLAG]", -8)
# (b) A token the excerpt window cuts at either end (a run of characters other than those of EXCERPT_PATH_STOP_RX,
#     not inside a placeholder) has its cut part replaced by EXCERPT_CUT_PH, unless the cut part is a plain word
#     (EXCERPT_PLAIN_WORD_RX) and the whole token has no reference shape (EXCERPT_REF_SHAPE_RX: a scheme separator,
#     a www label, a dotted name ending in two letters, a slash next to a name character, an at sign). Where the hit
#     lies in the token cut at the left and starts within EXCERPT_LEFT_SHIFT_MAX characters of it, the window starts
#     at the token instead, so the hit stays visible where its token fits the window, and the left end is no cut.
#     Where the window's right end cuts a run (a run of characters other than those of EXCERPT_RUN_STOP_RX:
#     whitespace, a quote, a backtick, a closing parenthesis or bracket -- the stop class of the history scan's two
#     path patterns, which read across angle brackets, braces, opening brackets, pipes, commas and semicolons), the
#     run's part inside the window, from its start (or the window's) to the end of its last token with a reference
#     shape, is replaced by EXCERPT_CUT_PH as well; so a path joined by those characters is never left with its
#     anchor visible and its tail cut.
EXCERPT_CUT_PH = "[CUT]"
EXCERPT_RUN_STOP_RX = re.compile(r"[\s\"'`)\]]")
EXCERPT_PLAIN_WORD_RX = re.compile(r"[A-Za-z]+")
EXCERPT_REF_SHAPE_RX = re.compile(r":/|\bwww\.|[A-Za-z0-9-]\.[A-Za-z]{2}|[A-Za-z0-9_.~%+-]/|/[A-Za-z0-9_.~%+-]|@", I)
EXCERPT_LEFT_SHIFT_MAX = 30


def excerpt_view(line):
    """Round 10, release: the line as an excerpt shows it -- every non-printable character (tab, CR, the C0/C1
    controls, non-ASCII spaces) mapped to one space; length and positions unchanged."""
    return "".join(ch if (ch.isprintable() and ch not in "\r\n") else " " for ch in line)


def excerpt_cut_masked(piece, token):
    """Round 10, release: True if a cut part `piece` of `token` is replaced by EXCERPT_CUT_PH."""
    return not (EXCERPT_PLAIN_WORD_RX.fullmatch(piece) and not EXCERPT_REF_SHAPE_RX.search(token))


# Standard OpenSSH file names under ~/.ssh/ that are not key names; still redacted
# in hits, but exempt from the leak guard (they are ordinary words found elsewhere).
STANDARD_SSH_FILES = {"config", "known_hosts", "known_hosts.old", "authorized_keys", "environment", "rc"}

MULTIWORD = {("confidentiality", s) for s in ("do not share", "not for publication", "internal only", "off the record")} | \
            {("personal_life", s) for s in ("my wife", "my husband", "my partner", "my kid")} | \
            {("correspondence", "Sent from")}

# Lookahead form so overlapping pairs are all seen ("Dear Alice Smith" -> both pairs).
NAME_PAIR_RX = re.compile(r"\b(?=([A-Z][a-z]+)[ \t]+((?:Mc|Mac|O')?[A-Z][a-z]+(?:-[A-Z][a-z]+)?)\b)")
ET_AL_RX = re.compile(r"\b([A-Z][a-z]+(?:-[A-Z][a-z]+)?)\s+et\s+al\b")
GIVEN_WORD_RX = re.compile(r"\b[A-Z][a-z]+\b")
CORR_FOLLOW_RXS = [
    re.compile(r"\b(?:Dear|Hi|Hello|From:|To:|Cc:|CC:|Subject:|Regards,?|Best,|Cheers,|Thanks,)[ \t]+(?P<v>\S+(?:[ \t]+\S+){0,2})"),
    re.compile(r"(?P<v>\S+(?:[ \t]+\S+)?)[ \t]+wrote:"),
]

# --------------------------------------------------------------------------

def sha8(s):
    return hashlib.sha256(s.encode("utf-8", "surrogatepass")).hexdigest()[:8]


def redact(v):
    # first 4 characters (fewer for a short value, so the prefix never is the whole value)
    return "%s...%d:%s" % (v[:min(4, len(v) // 2)], len(v), sha8(v))


def c2pa_line_spans(path, text):
    """Round 9: {line number: [(start col, end col)]} of the text content of every DECLARED <c2pa:manifest> element
    (an .svg whose repository path, matched exactly, is a C2PA_MANIFESTS key -- a root path -- the element's text of
    that entry's length and sha256), plus the counts of declared and undeclared elements. A declared blob holds no
    newline, so each span lies on one line."""
    out, n_decl, n_undecl = defaultdict(list), 0, 0
    if not (path or "").endswith(".svg") or "<c2pa:manifest>" not in text:
        return out, 0, 0
    want = C2PA_MANIFESTS.get(path)
    for m in C2PA_ELEMENT_RX.finditer(text):
        blob = m.group(1)
        if want and (len(blob), hashlib.sha256(blob.encode()).hexdigest()) == want:
            ls = text.rfind("\n", 0, m.start(1)) + 1
            out[text.count("\n", 0, m.start(1)) + 1].append((m.start(1) - ls, m.end(1) - ls))
            n_decl += 1
        else:
            n_undecl += 1
    return out, n_decl, n_undecl


def email_domain_class(e):
    dom = e.rsplit("@", 1)[-1].lower()
    for known in ("users.noreply.github.com", "anthropic.com", "gmail.com", "github.com"):
        if dom == known or dom.endswith("." + known):
            return known
    return "other"


def entropy(s):
    if not s:
        return 0.0
    c = Counter(s)
    n = len(s)
    return -sum((k / n) * math.log2(k / n) for k in c.values())


def ipv4_class(ip):
    o = [int(x) for x in ip.split(".")]
    if o[0] == 127:
        return "loopback"
    if o == [0, 0, 0, 0]:
        return "unspecified"
    if o[0] == 10 or (o[0] == 172 and 16 <= o[1] <= 31) or (o[0] == 192 and o[1] == 168):
        return "private_rfc1918"
    if o[0] == 169 and o[1] == 254:
        return "link_local"
    if o[0] == 100 and 64 <= o[1] <= 127:
        return "cgnat"
    if o[0] >= 224:
        return "multicast_or_reserved"
    if o[0] == 0:
        return "this_network"
    return "public_shaped"


def label_is_idlike(lbl):
    has_d = any(ch.isdigit() for ch in lbl)
    has_a = any(ch.isalpha() for ch in lbl)
    if len(lbl) >= 8 and has_d and has_a:
        return True
    if len(lbl) >= 16:
        return True
    if re.match(r"^[a-z0-9]{8,}-\d+$", lbl, I):
        return True
    return False


def display_host(host):
    host = host.lower().rstrip(".")
    hp = host.rsplit(":", 1)
    h, port = (hp[0], ":" + hp[1]) if len(hp) == 2 and hp[1].isdigit() else (host, "")
    if IPV4_RX.fullmatch(h):
        return "[IP %s %s]%s" % (ipv4_class(h), redact(h), port)
    out = []
    for lbl in h.split("."):
        out.append("[%s]" % redact(lbl) if label_is_idlike(lbl) else lbl)
    return ".".join(out) + port


def url_host(url):
    m = re.match(r"^[a-z][a-z0-9+.-]*://([^/?#]*)", url, I)
    if m:
        auth = m.group(1)
    else:  # www.
        auth = re.split(r"[/?#]", url, 1)[0]
    if "@" in auth:
        auth = auth.rsplit("@", 1)[1]
    return auth


# ---------------------------- masking --------------------------------------

def mask_spans(line, name_allow):
    spans = []  # (start, end, placeholder, priority)

    def add(s, e, ph, pr):
        if e > s:
            spans.append((s, e, ph, pr))

    for ph, rx, pr in EXCERPT_CLASS_RXS:   # round 10: whole path tokens, ahead of every other placeholder
        for m in rx.finditer(line):
            add(*excerpt_path_token(line, *m.span()), ph, pr)
    if EXCERPT_SSH_WORD_RX.search(line):   # round 10, release: an identity-file flag with its argument, as one span
        for m in EXCERPT_ID_FLAG_RX.finditer(line):
            add(*m.span(), *EXCERPT_ID_FLAG)
    for _, rx in CRED_RXS:
        for m in rx.finditer(line):
            s, e = (m.span("v") if "v" in rx.groupindex and m.group("v") is not None else m.span())
            add(s, e, "[CRED]", 0)
    for _, rx in INFRA_RXS:
        for m in rx.finditer(line):
            add(*m.span("v"), "[ID]", 1)
    for m in EMAIL_RX.finditer(line):
        add(*m.span(), "[EMAIL]", 2)
    for m in IPV4_RX.finditer(line):
        add(*m.span(), "[IP]", 3)
    for _, rx in PHONE_RXS:
        for m in rx.finditer(line):
            add(*m.span(), "[PHONE]", 4)
    for _, rx in ADDR_RXS:
        for m in rx.finditer(line):
            add(*m.span(), "[ADDR]", 5)
    for m in re.finditer(r"(?<![A-Za-z0-9_\-+=])[A-Za-z0-9_\-+=]{20,}(?![A-Za-z0-9_\-+=])", line):
        t = m.group(0)
        if any(c.isdigit() for c in t) and any(c.isalpha() for c in t):
            add(*m.span(), "[TOK]", 6)
    for rx in CORR_FOLLOW_RXS:
        for m in rx.finditer(line):
            add(*m.span("v"), "[W]", 7)
    for m in GIVEN_WORD_RX.finditer(line):
        w = m.group(0)
        if w in GIVEN_NAMES and w not in name_allow:
            add(*m.span(), "[NAME]", 8)
    for m in NAME_PAIR_RX.finditer(line):
        a, b = m.group(1), m.group(2)
        if a in GIVEN_NAMES and (a, b) not in NAME_PAIR_ALLOW and b not in name_allow:
            add(m.start(1), m.end(2), "[NAME]", 8)
    if not spans:
        return []
    spans.sort(key=lambda x: (x[0], x[3]))
    merged = []
    for s, e, ph, pr in spans:
        if merged and s < merged[-1][1]:
            ps, pe, pph, ppr = merged[-1]
            if pr < ppr:
                pph, ppr = ph, pr
            merged[-1] = (ps, max(pe, e), pph, ppr)
        else:
            merged.append((s, e, ph, pr))
    return merged


_MASK_CACHE = {}


def excerpt(line, pos, name_allow):
    line = excerpt_view(line)   # round 10, release: before masking (was: tabs before, other controls after the cut)
    # name_allow is fixed for a whole run (set once after the et-al pass), so the line alone keys the cache.
    if len(_MASK_CACHE) > 4096:
        _MASK_CACHE.clear()
    merged = _MASK_CACHE.get(line)
    if merged is None:
        merged = mask_spans(line, name_allow)
        _MASK_CACHE[line] = merged
    out = []
    olen = 0
    cur = 0
    mpos = None
    ph_spans = []   # round 10, release: each placeholder's [start, end) in the masked line
    for s, e, ph, _ in merged:
        if mpos is None and pos < s:
            mpos = olen + (pos - cur)
        out.append(line[cur:s])
        olen += s - cur
        if mpos is None and s <= pos < e:
            mpos = olen
        out.append(ph)
        ph_spans.append((olen, olen + len(ph)))
        olen += len(ph)
        cur = e
    if mpos is None:
        mpos = olen + max(0, pos - cur)
    out.append(line[cur:])
    masked = "".join(out)
    n = len(masked)
    start = max(0, mpos - 10)

    # round 10, release: tokens cut by the window (see EXCERPT_CUT_PH)
    def tok(i):
        return 0 <= i < n and not EXCERPT_PATH_STOP_RX.match(masked[i])

    def cut_at(i):   # True if the boundary before masked[i] splits a token outside every placeholder
        return tok(i - 1) and tok(i) and not any(a < i < b for a, b in ph_spans)

    def bounds(i):   # the token holding masked[i]
        s, e = i, i
        while tok(s - 1):
            s -= 1
        while tok(e):
            e += 1
        return s, e

    if cut_at(start):
        ts, te = bounds(start)
        if te > mpos and mpos - ts <= EXCERPT_LEFT_SHIFT_MAX:
            start = ts   # the hit lies in this token: start the window at the token
    end = min(n, start + EXCERPT_MAX)
    cuts = []   # [start, end) of each cut part replaced by EXCERPT_CUT_PH
    if cut_at(start):
        ts, te = bounds(start)
        x = min(te, end)
        if excerpt_cut_masked(masked[start:x], masked[ts:te]):
            cuts.append((start, x))
    left_end = cuts[0][1] if cuts else start
    if end < n and cut_at(end):
        ts, te = bounds(end - 1)
        y = max(ts, left_end)
        if y < end and excerpt_cut_masked(masked[y:end], masked[ts:te]):
            cuts.append((y, end))

    def rtok(i):   # a character of a run (see EXCERPT_RUN_STOP_RX)
        return 0 <= i < n and not EXCERPT_RUN_STOP_RX.match(masked[i])

    if end < n and rtok(end - 1) and rtok(end):   # the right end cuts a run: mask it up to its last reference token
        rs = end - 1
        while rtok(rs - 1):
            rs -= 1
        y0 = max(rs, left_end)
        last, i = None, y0
        while i < end:
            if tok(i):
                ts, te = bounds(i)
                if EXCERPT_REF_SHAPE_RX.search(masked[ts:te]):
                    last = min(te, end)
                i = te
            else:
                i += 1
        if last is not None and y0 < last:
            cuts.append((y0, last))
    merged_cuts = []   # disjoint, in order; touching or overlapping cut parts become one [CUT]
    for a, b in sorted(cuts):
        if merged_cuts and a <= merged_cuts[-1][1]:
            merged_cuts[-1] = (merged_cuts[-1][0], max(b, merged_cuts[-1][1]))
        else:
            merged_cuts.append((a, b))
    parts, cur = [], start
    for a, b in merged_cuts:
        parts += [masked[cur:a], EXCERPT_CUT_PH]
        cur = b
    parts.append(masked[cur:end])
    return "".join(parts).strip()


# ---------------------------- git -------------------------------------------

def git(*args):
    return subprocess.run(["git", "-C", ROOT] + list(args), check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


class Cat:
    """git cat-file --batch reader (read-only)."""

    def __init__(self):
        self.p = subprocess.Popen(["git", "-C", ROOT, "cat-file", "--batch"],
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def get(self, spec):
        self.p.stdin.write((spec + "\n").encode())
        self.p.stdin.flush()
        hdr = self.p.stdout.readline().decode().rstrip("\n")
        if hdr.endswith(" missing"):
            raise KeyError(spec)
        oid, typ, size = hdr.split(" ")
        data = self.p.stdout.read(int(size))
        self.p.stdout.read(1)
        return oid, typ, data

    def close(self):
        self.p.stdin.close()
        self.p.wait()


# ---------------------------- screening -------------------------------------

def screen_text(text, name_allow, path=None):
    """Return (hits, names, values) for one text. hits: {category: [[line, excerpt, extra]]}. path (round 9): the
    object's locator, for the C2PA declaration."""
    c2, n_c2_decl, n_c2_undecl = c2pa_line_spans(path, text)
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    hits = defaultdict(list)
    values = []  # (category, subtype, raw value, line) -- raw stays in memory only
    tier_a = 0
    tier_b_lines = []
    tier_b_pairs = set()
    forms = defaultdict(Counter)

    def dec(ln, s, e):
        # round 9: True if [s, e) on line ln lies wholly inside a declared C2PA manifest blob
        return any(a <= s and e <= b for a, b in c2.get(ln, ()))

    def c2s(sub, d):
        return sub + "@c2pa_declared" if d else sub

    def hit(cat, ln, line, pos, extra, declared=False):
        if declared:   # round 9: the declaration's fields; the hit is still recorded and its value still guarded
            extra = dict(extra, verdict="FALSE-POSITIVE", reason=C2PA_REASON, context=C2PA_CONTEXT)
            hits["_c2pa_declared"].append([ln, cat])
        hits[cat].append([ln, excerpt(line, pos, name_allow), extra])

    for i, line in enumerate(lines):
        ln = i + 1
        if not line:
            continue
        # e-mail
        for m in EMAIL_RX.finditer(line):
            e = m.group(0)
            key = EMAIL_ALLOW.get(e.lower())
            if key:
                hits["email_allowlisted"].append([ln, key])
            else:
                cls = "noreply_shaped" if re.match(r"^(?:no-?reply|donotreply)", e, I) else "other"
                d_ = dec(ln, *m.span())
                values.append(("email", c2s(cls, d_), e, ln))
                hit("email", ln, line, m.start(), {"class": cls, "redacted": redact(e)}, d_)
        # phone
        seen = set()
        for sub, rx in PHONE_RXS:
            for m in rx.finditer(line):
                if m.span() in seen:
                    continue
                v = m.group(0)
                nd = sum(c.isdigit() for c in v)
                if sub == "international_plus" and not (8 <= nd <= 15):
                    continue
                seen.add(m.span())
                shape = re.sub(r"\d", "d", v)
                d_ = dec(ln, *m.span())
                values.append(("phone", c2s(sub, d_), v, ln))
                feat = {"subtype": sub, "shape": shape, "redacted": redact(v)}
                if re.match(r"^[+-]d\.d", shape):
                    feat["shape_tag"] = "signed_decimal"  # mechanical: '+<digit>.<digits>' is a signed decimal number's shape
                hit("phone", ln, line, m.start(), feat, d_)
        # street address
        for sub, rx in ADDR_RXS:
            for m in rx.finditer(line):
                v = m.group(0)
                d_ = dec(ln, *m.span())
                values.append(("street_address", c2s(sub, d_), v, ln))
                hit("street_address", ln, line, m.start(), {"subtype": sub, "redacted": redact(v)}, d_)
        # IPv4
        for m in IPV4_RX.finditer(line):
            v = m.group(0)
            cls = ipv4_class(v)
            d_ = dec(ln, *m.span())
            values.append(("ipv4", c2s(cls, d_), v, ln))
            hit("ipv4", ln, line, m.start(), {"class": cls, "redacted": redact(v)}, d_)
        # URLs
        for rx in (URL_RX, WWW_RX):
            for m in rx.finditer(line):
                u = m.group(0).rstrip(".,;:")
                h = display_host(url_host(u))
                hit("url", ln, line, m.start(), {"host": h}, dec(ln, m.start(), m.start() + len(u)))
        # confidentiality words
        for sub, rx in CONF_RXS:
            for m in rx.finditer(line):
                ctx = "path" if (sub == "private" and m.start() > 0 and line[m.start() - 1] == "/") else "text"
                forms["confidentiality"][m.group(0).lower()] += 1
                hit("confidentiality", ln, line, m.start(), {"word": sub, "context": ctx}, dec(ln, *m.span()))
        # correspondence markers
        for sub, rx in CORR_RXS:
            for m in rx.finditer(line):
                hit("correspondence", ln, line, m.start(), {"marker": sub}, dec(ln, *m.span()))
        # personal-life markers
        for sub, rx in PERS_RXS:
            for m in rx.finditer(line):
                forms["personal_life"][m.group(0).lower()] += 1
                hit("personal_life", ln, line, m.start(), {"marker": sub, "form": m.group(0).lower()},
                    dec(ln, *m.span()))
        # credential-shaped
        for sub, rx in CRED_RXS:
            for m in rx.finditer(line):
                v = m.group("v") if "v" in rx.groupindex else m.group(0)
                feat = {"subtype": sub, "redacted": redact(v), "len": len(v),
                        "entropy_bits_per_char": round(entropy(v), 2),
                        "has_digit": any(c.isdigit() for c in v),
                        "mixed_case": any(c.isupper() for c in v) and any(c.islower() for c in v)}
                d_ = dec(ln, *m.span("v" if "v" in rx.groupindex else 0))
                values.append(("credential", c2s(sub, d_), v, ln))
                hit("credential", ln, line, m.start(), feat, d_)
        for m in GENERIC_TOKEN_RX.finditer(line):
            v = m.group(0)
            if HEX_RX.match(v):
                hits["_hex_tokens_skipped"].append(ln)
                continue
            if not (any(c.isdigit() for c in v) and any(c.isalpha() for c in v)):
                continue
            ent = entropy(v)
            if ent < 3.5:
                continue
            d_ = dec(ln, *m.span())
            values.append(("credential", c2s("generic_high_entropy", d_), v, ln))
            pre = line[max(0, m.start() - 40):m.start()]
            post = line[m.end():m.end() + 3]
            ctx = None
            if re.search(r"/var/folders/[A-Za-z0-9_]{2}/$", pre) or (re.search(r"folders/[A-Za-z0-9_]{2}/$", pre) and post.startswith("/T")):
                ctx = "macos_per_user_temp_dir_component"  # /var/folders/<xx>/<token>/T/...
            elif re.search(r"claude\.ai/code/(?:session_)?$", pre):
                ctx = "claude_ai_session_url_component"
            hit("credential", ln, line, m.start(), {"subtype": "generic_high_entropy", "context": ctx, "redacted": redact(v),
                                                   "len": len(v), "entropy_bits_per_char": round(ent, 2),
                                                   "mixed_case": any(c.isupper() for c in v) and any(c.islower() for c in v)},
                d_)
        # infrastructure identifiers (supplementary)
        for sub, rx in INFRA_RXS:
            for m in rx.finditer(line):
                v = m.group("v")
                d_ = dec(ln, *m.span("v"))
                values.append(("infra_identifier", c2s(sub, d_), v, ln))
                feat = {"subtype": sub, "redacted": redact(v)}
                if sub == "ssh_key_path" and v in STANDARD_SSH_FILES:
                    feat["standard_openssh_file"] = True  # e.g. the client config file, not a key name
                hit("infra_identifier", ln, line, m.start(), feat, d_)
        # names (counts only)
        for m in NAME_PAIR_RX.finditer(line):
            a, b = m.group(1), m.group(2)
            if a in name_allow or b in name_allow or (a, b) in NAME_PAIR_ALLOW:
                continue
            tier_a += 1
            if a in GIVEN_NAMES:
                tier_b_lines.append(ln)
                tier_b_pairs.add((a, b))
        # multi-word phrases broken across a line end
        if i + 1 < len(lines):
            joined = line.rstrip() + " " + lines[i + 1].lstrip()
            cut = len(line.rstrip())
            for cat, sub in MULTIWORD:
                rxs = {"confidentiality": CONF_RXS, "personal_life": PERS_RXS, "correspondence": CORR_RXS}[cat]
                rx = dict(rxs)[sub]
                for m in rx.finditer(joined):
                    if m.start() < cut < m.end():
                        key = {"confidentiality": "word", "personal_life": "marker", "correspondence": "marker"}[cat]
                        hits[cat].append([ln, excerpt(joined, m.start(), name_allow),
                                          {key: sub, "spans_next_line": True}])
                        # release v2 (2026-10-30, the raw reads): a phrase across a line end counts in its word forms too
                        if cat in ("confidentiality", "personal_life"):
                            forms[cat][m.group(0).lower()] += 1
    if n_c2_decl or n_c2_undecl:   # round 9: per-object record of the C2PA elements read
        hits["_c2pa_elements"].append({"declared": n_c2_decl, "undeclared": n_c2_undecl})
    names = {"tier_a_capitalised_pairs": tier_a,
             "tier_b_given_name_pairs": len(tier_b_lines),
             "tier_b_distinct_pairs": len(tier_b_pairs),
             "tier_b_lines": tier_b_lines}
    return hits, names, values, len(lines), forms


# ---------------------------- release v2: the retained finding -------------

# the 'method' entries a full run and a --retained-only run share (the latter's are these two only)
METHOD_LINE_SPLIT = "on \\n; 'lines' = number of \\n-separated lines (a trailing newline does not add a line)"
METHOD_NAMES = ("tier_a: capitalised word pairs, neither word in the name allowlist (counts only); tier_b: tier_a pairs "
                "whose first word is in the embedded given-name list (%d names; counts and line numbers only, never the "
                "names)")


def tier_b_spans(line, name_allow):
    """Release v2 (2026-11-02): one line's tier-b given-name pairs by screen_text's rule, each as the text it spans -- in
    memory only, for the leak guard (retained_record asserts that their number is screen_text's count)."""
    out = []
    for m in NAME_PAIR_RX.finditer(line):
        a, b = m.group(1), m.group(2)
        if a in name_allow or b in name_allow or (a, b) in NAME_PAIR_ALLOW:
            continue
        if a in GIVEN_NAMES:
            out.append(line[m.start(1):m.end(2)])
    return out


def retained_record(rev, name_allow, guard_values, items):
    """Release v2 (2026-11-02): each RETAINED entry checked against the git objects and recorded (see the docstring):
    counts, line numbers and object ids only. The pairs found, and any value the screen collects from the versions read
    here, join guard_values. Exits without writing unless every check holds."""
    def ok(*args):   # a git predicate: exit status 0
        return subprocess.run(["git", "-C", ROOT] + list(args), stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL).returncode == 0

    def oid(spec):
        return git("rev-parse", "--verify", spec).decode().strip()

    def read(spec, path):   # a version's text, its name tiers and its other categories' hit counts
        text = git("show", spec).decode("utf-8", "replace")
        hits, names, values, nlines, _forms = screen_text(text, name_allow, path)
        guard_values.update(v for _c, _s, v, _l in values)
        return text, names, {k: len(v) for k, v in sorted(hits.items()) if not k.startswith("_")}, nlines

    refs = [r for r in git("for-each-ref", "--format=%(refname)").decode().split("\n") if r]
    entries = []
    for d in RETAINED:
        p, ln = d["path"], d["line"]
        b, c = oid(d["blob_at"] + "^{commit}"), oid(d["removed_at"] + "^{commit}")
        b_blob, c_parent_blob, c_blob = oid(b + ":" + p), oid(c + "^1:" + p), oid(c + ":" + p)
        r_blob = oid(rev + ":" + p) if ok("cat-file", "-e", rev + ":" + p) else None
        b_text, b_names, b_cats, b_lines = read(b + ":" + p, p)
        c_names, c_cats = read(c + ":" + p, p)[1:3]
        r_names = read(rev + ":" + p, p)[1] if r_blob else None
        spans = tier_b_spans(b_text.split("\n")[ln - 1], name_allow) if ln <= b_lines else []
        guard_values.update(spans)
        added = git("log", "--all", "--no-renames", "--diff-filter=A", "--format=%H", "--", p).decode().split()
        touching = git("log", "--all", "--no-renames", "--format=%H", "--", p).decode().split()
        changed = [x for x in git("diff-tree", "-z", "--no-commit-id", "--name-only", "-r", c)
                   .decode("utf-8", "surrogateescape").split("\0") if x]
        hunks = re.findall(r"^@@ -([0-9]+)(?:,([0-9]+))? \+([0-9]+)(?:,([0-9]+))? @@",
                           git("diff", "-U0", c + "^1", c, "--", p).decode("utf-8", "replace"), re.M)
        pickaxe = sorted({h for s_ in spans for h in git("log", "--all", "--format=%H", "-S" + s_).decode().split()})
        in_msgs = sum(len(git("log", "--all", "--format=%H", "-F", "--grep=" + s_).decode().split()) for s_ in spans)
        in_tree = sum(ok("grep", "-q", "-F", "-e", s_, rev) for s_ in spans)
        in_objects = sum(1 for it in items for s_ in spans if s_ in it["text"])
        checks = {
            "blob_at_added_the_path": b in added,
            "removed_at_replaced_that_blob": c_parent_blob == b_blob,
            "removed_at_changed_this_path_only": changed == [p],
            "removed_at_changed_this_line_only": (len(hunks) == 1 and hunks[0][0] == hunks[0][2] == str(ln)
                                                  and hunks[0][1] in ("", "1") and hunks[0][3] in ("", "1")),
            "pairs_at_blob_at_as_declared": (b_names["tier_b_given_name_pairs"] == d["tier_b_given_name_pairs"] == len(spans)
                                             and set(b_names["tier_b_lines"]) == {ln}),
            "no_pair_on_the_line_at_removed_at": ln not in c_names["tier_b_lines"],
            "path_at_rev_with_no_pair_on_the_line": r_blob is not None and ln not in r_names["tier_b_lines"],
            "other_categories_equal": b_cats == c_cats,
            "blob_at_in_rev_history": ok("merge-base", "--is-ancestor", b, rev),
            "removed_at_in_rev_history": ok("merge-base", "--is-ancestor", c, rev),
            "pairs_in_no_other_commit_patch": pickaxe == sorted([b, c]),
            "pairs_in_no_commit_message": in_msgs == 0,
            "pairs_in_no_file_at_rev": in_tree == 0,
            "pairs_in_no_other_screened_object": in_objects == 0,
        }
        bad = [k for k, v in checks.items() if not v]
        if bad:
            sys.exit("N12(vi) retained finding, %s: %s does not hold; nothing written" % (p, ", ".join(bad)))
        h = hunks[0]
        entries.append({
            "declared": dict(d),
            "path": p, "line": ln,
            "blob_at": {"commit": b, "blob": b_blob, "lines": b_lines},
            "removed_at": {"commit": c, "blob": c_blob, "paths_changed": changed,
                           "hunk": "@@ -%s%s +%s%s @@" % (h[0], "," + h[1] if h[1] else "", h[2], "," + h[3] if h[3] else "")},
            "rev": {"commit": rev, "blob": r_blob, "same_blob_as_removed_at": r_blob == c_blob},
            "commits_touching_path": touching,
            "names": {"blob_at": b_names, "removed_at": c_names, "rev": r_names},
            "other_categories": {"blob_at": b_cats, "removed_at": c_cats},
            "elsewhere": {"pickaxe_commits": pickaxe, "commit_messages": in_msgs, "files_at_rev": in_tree,
                          "other_screened_objects": in_objects},
            "refs_reaching_blob_at": [r for r in refs if ok("merge-base", "--is-ancestor", b, r)],
            "checks": checks,
            "finding": ("%d given-name pairs (tier b, %d distinct), all on line %d of the blob at %s (the version that "
                        "commit added); removed from the tree at %s, which changed that line only and left no pair on "
                        "it (none at --rev either); retained in history: %s is an ancestor of --rev"
                        % (len(spans), b_names["tier_b_distinct_pairs"], ln, b[:7], c[:7], b[:7])),
            "disposition": "RETAINED-IN-HISTORY",
            "reason": RETAINED_REASON,
            "reason_from": "the PI's answer of %s (pi_answer), its parenthesis, verbatim" % RETAINED_PI_WORDS[0],
        })
    return {
        "rule": ("release v2 (2026-11-02): every run checks each entry against the git objects and exits without writing "
                 "unless every check holds (checks); counts, line numbers and object ids only, never a name; each pair "
                 "found joins the leak guard; nothing here is added to objects or totals"),
        "code_question": {"date": RETAINED_QUESTION[0], "words_verbatim": RETAINED_QUESTION[1]},
        "pi_answer": {"date": RETAINED_PI_WORDS[0], "words_verbatim": RETAINED_PI_WORDS[1]},
        "entries": entries,
    }


def retained_lines(retained):
    """Release v2 (2026-11-02): the stdout summary's lines for the retained_in_history section."""
    out = ["retained in history (release v2; Code's question of %s, the PI's answer of %s): %d entr%s"
           % (retained["code_question"]["date"], retained["pi_answer"]["date"], len(retained["entries"]),
              "y" if len(retained["entries"]) == 1 else "ies")]
    for e in retained["entries"]:
        out.append("   %s line %d: tier-b pairs %d (%d distinct) in the blob at %s (%s); removed at %s (%s, %s); on the "
                   "line at %s %d, at rev %d; other categories equal (%s); %s in rev's history (refs %s); elsewhere: "
                   "pickaxe %s, messages %d, files at rev %d, other objects %d; checks %d/%d; %s: \"%s\""
                   % (e["path"], e["line"], e["names"]["blob_at"]["tier_b_given_name_pairs"],
                      e["names"]["blob_at"]["tier_b_distinct_pairs"], e["blob_at"]["commit"][:7], e["blob_at"]["blob"][:12],
                      e["removed_at"]["commit"][:7], e["removed_at"]["hunk"], ", ".join(e["removed_at"]["paths_changed"]),
                      e["removed_at"]["commit"][:7], e["names"]["removed_at"]["tier_b_lines"].count(e["line"]),
                      e["names"]["rev"]["tier_b_lines"].count(e["line"]), e["other_categories"]["blob_at"],
                      e["blob_at"]["commit"][:7], ", ".join(e["refs_reaching_blob_at"]),
                      [x[:7] for x in e["elsewhere"]["pickaxe_commits"]], e["elsewhere"]["commit_messages"],
                      e["elsewhere"]["files_at_rev"], e["elsewhere"]["other_screened_objects"],
                      sum(e["checks"].values()), len(e["checks"]), e["disposition"], e["reason"]))
    return out


def write_retained_only(a, out, stamp, rev, script_sha, block_sha_at_rev, items, et_al, retained, guard_values):
    """Release v2 (2026-11-02), --retained-only: the header, the name tiers' method and the retained_in_history section,
    under a full run's leak guard (main()), applied to this JSON and summary."""
    src_counts = Counter(it["source"] for it in items)
    result = {
        "part": PART,
        "item": "N12(vi) content review -- the finding retained in history (release v2, 2026-11-02; --retained-only)",
        "block": {"path": BLOCK, "sha256_expected": BLOCK_SHA, "sha256_at_rev": block_sha_at_rev,
                  "match": block_sha_at_rev == BLOCK_SHA},
        "stamp_utc": stamp,
        "script": {"path": "scripts/audit_note_N12_content.py", "sha256": script_sha},
        "python": sys.version.split()[0], "platform": platform.platform(),
        "git_version": subprocess.run(["git", "--version"], stdout=subprocess.PIPE).stdout.decode().strip(),
        "rev": {"requested": a.rev, "resolved": rev},
        "scope": {
            "mode": ("--retained-only: each RETAINED entry's versions are read and checked (retained_in_history); a "
                     "full run's scope is read for the et-al allowlist only, and nothing in it is screened or reported"),
            "content_source": "git objects via git cat-file --batch and git show (committed bytes; working tree not read)",
            "objects_read_for_the_allowlist": len(items),
            "objects_by_source": dict(src_counts),
        },
        "method": {
            "line_split": METHOD_LINE_SPLIT,
            "names": METHOD_NAMES % len(GIVEN_NAMES),
            "name_allowlist_fixed": sorted(NAME_ALLOW),
            "name_allowlist_et_al_detected": sorted(et_al),
        },
        "patterns": {"names": NAME_PAIR_RX.pattern},
        "retained_in_history": retained,
    }
    allowed_verbatim = set(EMAIL_ALLOW) | IDENTITY_NAME_ALLOW
    to_check = sorted(v for v in guard_values if len(v) >= 5 and v.lower() not in allowed_verbatim
                      and v not in allowed_verbatim and v not in STANDARD_SSH_FILES)
    result["leak_guard"] = {
        "raw_values_checked": len(to_check),
        "rule": ("a full run's rule: every collected raw value of length >= 5 -- here the non-allowlisted identity names "
                 "and e-mails of the commit and tag headers, the pairs found in each RETAINED version and any other value "
                 "the screen collects from the versions it reads for retained_in_history -- asserted absent from the "
                 "JSON text and the stdout summary before either is written; exempt: the two allowlisted e-mails, the "
                 "allowlisted identity names, and standard OpenSSH file names %s; the JSON is checked with the "
                 "'patterns' block and every 'method' entry except %s blanked"
                 % (sorted(STANDARD_SSH_FILES), list(CONTENT_DERIVED_METHOD_KEYS)))}
    js = json.dumps(result, indent=1, ensure_ascii=False, sort_keys=False) + "\n"
    js_chk = json.dumps(dict(result, patterns=None,
                             method={k_: v_ for k_, v_ in result["method"].items() if k_ in CONTENT_DERIVED_METHOD_KEYS}),
                        indent=1, ensure_ascii=False, sort_keys=False) + "\n"
    summary = ["AUDIT-note-release v1.2 -- N12(vi) content pre-screen (%s), --retained-only" % PART,
               "stamp_utc %s  rev %s  block sha256 at rev %s (%s)" % (stamp, rev, (block_sha_at_rev or "absent")[:16],
                                                                    "match" if block_sha_at_rev == BLOCK_SHA else "MISMATCH"),
               "script sha256 %s" % script_sha,
               "scope read for the et-al allowlist: %d objects (%s); et-al surnames auto-allowlisted: %d"
               % (len(items), dict(src_counts), len(et_al))]
    summary += retained_lines(retained)
    summary += ["leak guard: %d raw values checked against the JSON and this summary" % len(to_check),
                "wrote %s" % os.path.relpath(out, ROOT)]
    text_out = "\n".join(summary)
    leaked = [v for v in to_check if v in js_chk or json.dumps(v, ensure_ascii=False)[1:-1] in js_chk or v in text_out]
    if leaked:
        sys.exit("LEAK GUARD FIRED: %d raw values would be written (redacted: %s); nothing written"
                 % (len(leaked), [redact(v) for v in leaked[:10]]))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "x", encoding="utf-8") as fh:
        fh.write(js)
    print(text_out)
    return 0


# ---------------------------- main ------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--json-out", default=DEFAULT_OUT)
    ap.add_argument("--selftest", action="store_true", help="run the masking self-test only; writes nothing")
    ap.add_argument("--retained-only", action="store_true",
                    help="release v2 (2026-11-02): write the header, the name method and retained_in_history only")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    out = a.json_out if os.path.isabs(a.json_out) else os.path.join(ROOT, a.json_out)
    out = os.path.normpath(out)
    if out.startswith(ROOT + os.sep) and not out.startswith(os.path.join(ROOT, "results", "raw") + os.sep):
        sys.exit("refusing: --json-out inside the repository must be under results/raw/")
    if os.path.exists(out):
        sys.exit("refusing to overwrite existing %s" % out)

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rev = git("rev-parse", "--verify", a.rev + "^{commit}").decode().strip()
    refs = [l.split(" ", 2) for l in git("for-each-ref", "--format=%(objectname) %(objecttype) %(refname)").decode().splitlines()]
    all_commits = git("rev-list", "--all").decode().split()

    cat = Cat()
    with open(os.path.abspath(__file__), "rb") as fh:
        script_sha = hashlib.sha256(fh.read()).hexdigest()
    try:
        _, _, bdata = cat.get(rev + ":" + BLOCK)
        block_sha_at_rev = hashlib.sha256(bdata).hexdigest()
    except KeyError:
        block_sha_at_rev = None

    # ---- objects to screen ----
    tree = git("ls-tree", "-r", "-z", "--full-tree", rev).decode("utf-8", "surrogateescape").split("\0")
    head_paths = {}
    for ent in tree:
        if not ent:
            continue
        meta, path = ent.split("\t", 1)
        mode, typ, oid = meta.split(" ")
        if typ == "blob":
            head_paths[path] = oid
    raw_paths = sorted(p for p in head_paths if p.startswith("results/raw/"))
    handoff_paths = sorted(p for p in head_paths if re.match(r"^(?:.*/)?HANDOFF-[^/]*\.md$", p))

    untracked_handoffs = sorted(p for p in git("ls-files", "--others", "--exclude-standard", "-z")
                                .decode("utf-8", "surrogateescape").split("\0")
                                if p and re.match(r"^(?:.*/)?HANDOFF-[^/]*\.md$", p))
    spec_cmd = ["log", "--all", "--diff-filter=D", "--name-only", "--format="]
    spec_deleted = sorted({l for l in git(*spec_cmd).decode("utf-8", "surrogateescape").splitlines() if l})
    norename_deleted = sorted({l for l in git("log", "--all", "--no-renames", "--diff-filter=D", "--name-only", "--format=")
                               .decode("utf-8", "surrogateescape").splitlines() if l})
    ever = {l for l in git("log", "--all", "--no-renames", "--name-only", "--format=")
            .decode("utf-8", "surrogateescape").splitlines() if l}
    absent_now = sorted(ever - set(head_paths))
    hist_paths = sorted(set(spec_deleted) | set(norename_deleted) | set(absent_now))
    hist_objs = []  # (path, deleting commit, blob spec)
    for p in hist_paths:
        dels = git("log", "--all", "--no-renames", "--diff-filter=D", "--format=%H", "--", p).decode().split()
        specs = []
        for c in dels:
            specs.append((c, c + "^1:" + p))
        if not dels:
            last = git("log", "--all", "-1", "--format=%H", "--", p).decode().strip()
            specs.append((last, last + ":" + p))
        for c, s in specs:
            hist_objs.append((p, c, s))

    # ---- load all texts (first pass: et al. surnames) ----
    items = []  # dict(source, locator, oid, data)
    for p in raw_paths:
        oid, _, d = cat.get(rev + ":" + p)
        items.append({"source": "head:results/raw", "locator": p, "blob": oid, "data": d})
    for p in handoff_paths:
        oid, _, d = cat.get(rev + ":" + p)
        items.append({"source": "head:handoff", "locator": p, "blob": oid, "data": d})
    seen_blobs = set()
    for p, c, s in hist_objs:
        oid, _, d = cat.get(s)
        if (p, oid) in seen_blobs:
            continue
        seen_blobs.add((p, oid))
        items.append({"source": "history-only", "locator": p, "deleted_at": c, "version_spec": s.split(":", 1)[0] + ":<path>",
                      "present_at_rev": p in head_paths, "in_block_command_output": p in spec_deleted,
                      "blob": oid, "data": d})

    identities = Counter()
    guard_values = set()  # raw values that must never reach the output (leak guard)
    id_commits = defaultdict(list)
    signed_commits = []
    tz = Counter()
    sigs = Counter()
    for c in all_commits:
        _, _, d = cat.get(c)
        hdr, _, msg = d.partition(b"\n\n")
        h = hdr.decode("utf-8", "replace")
        for role in ("author", "committer"):
            m = re.search(r"^%s (.*) <([^>]*)> (\d+) ([+-]\d{4})$" % role, h, re.M)
            if m:
                name, email = m.group(1), m.group(2)
                ikey = (role, name if name in IDENTITY_NAME_ALLOW else "[name " + redact(name) + "]",
                        EMAIL_ALLOW.get(email.lower(), "[email %s domain=%s]" % (redact(email), email_domain_class(email))))
                identities[ikey] += 1
                id_commits[ikey].append(c)
                guard_values.add(email)
                guard_values.add(name)
                tz[m.group(4)] += 1
        if "\ngpgsig " in "\n" + h:
            st = "ssh" if "BEGIN SSH SIGNATURE" in h else ("pgp" if "BEGIN PGP SIGNATURE" in h else "other")
            sigs[st] += 1
            signed_commits.append([c, st])
        else:
            sigs["unsigned"] += 1
        items.append({"source": "commit-message", "locator": c, "blob": c, "data": msg})
    tag_info = []
    for oid, typ, ref in refs:
        if typ == "tag":
            _, _, d = cat.get(oid)
            hdr, _, msg = d.partition(b"\n\n")
            h = hdr.decode("utf-8", "replace")
            m = re.search(r"^tagger (.*) <([^>]*)> (\d+) ([+-]\d{4})$", h, re.M)
            if m:
                identities[("tagger", m.group(1) if m.group(1) in IDENTITY_NAME_ALLOW else "[name " + redact(m.group(1)) + "]",
                            EMAIL_ALLOW.get(m.group(2).lower(), "[email %s domain=%s]" % (redact(m.group(2)), email_domain_class(m.group(2)))))] += 1
                guard_values.add(m.group(2))
                guard_values.add(m.group(1))
                tz[m.group(4)] += 1
            body_sig = "BEGIN PGP SIGNATURE" in msg.decode("utf-8", "replace") or "BEGIN SSH SIGNATURE" in msg.decode("utf-8", "replace")
            tag_info.append({"ref": ref, "object": oid, "signed": body_sig})
            items.append({"source": "tag-message", "locator": ref, "blob": oid, "data": msg})
    cat.close()

    name_allow = set(NAME_ALLOW)
    et_al = set()
    for it in items:
        it["text"] = it["data"].decode("utf-8", "replace")
        it["utf8_replacements"] = it["text"].count("�") - it["data"].count("�".encode())
        it["nul_bytes"] = it["data"].count(b"\0")
        for m in ET_AL_RX.finditer(it["text"]):
            et_al.add(m.group(1))
    name_allow |= et_al

    # ---- release v2 (2026-11-02): N12(vi)'s retained finding, checked and recorded (see the docstring) ----
    retained = retained_record(rev, name_allow, guard_values, items)
    if a.retained_only:
        return write_retained_only(a, out, stamp, rev, script_sha, block_sha_at_rev, items, et_al, retained, guard_values)

    # ---- second pass: screen ----
    files_out = []
    totals = defaultdict(lambda: {"hits": 0, "objects_with_hits": 0})
    hosts = defaultdict(lambda: {"count": 0, "objects": set()})
    distinct = defaultdict(lambda: {"count": 0, "objects": set(), "subtypes": Counter()})
    allow_counts = Counter()
    word_forms = defaultdict(Counter)
    names_tot = Counter()
    by_source = defaultdict(lambda: Counter())
    hex_skipped = 0
    c2pa_hits = Counter()      # round 9: hits inside a declared C2PA manifest blob, by category
    c2pa_objects = {}          # round 9: locator -> {"declared": n, "undeclared": n}
    for it in items:
        hits, names, values, nlines, forms = screen_text(it["text"], name_allow, it["locator"])
        hex_skipped += len(hits.pop("_hex_tokens_skipped", []))
        c2pa_hits.update(c_ for _, c_ in hits.pop("_c2pa_declared", []))
        for r_ in hits.pop("_c2pa_elements", []):
            c2pa_objects[it["locator"]] = r_
        for k, v in forms.items():
            word_forms[k].update(v)
        loc = it["locator"]
        for row in hits.get("email_allowlisted", []):
            allow_counts[row[1]] += 1
        for cat_, rows in hits.items():
            totals[cat_]["hits"] += len(rows)
            totals[cat_]["objects_with_hits"] += 1
            by_source[it["source"]][cat_] += len(rows)
            if cat_ == "url":
                for r in rows:
                    hosts[r[2]["host"]]["count"] += 1
                    hosts[r[2]["host"]]["objects"].add(loc)
        for cat_, sub, v, ln in values:
            guard_values.add(v)
            key = (cat_, redact(v))
            distinct[key]["count"] += 1
            distinct[key]["objects"].add(loc)
            distinct[key]["subtypes"][sub] += 1
        for k in ("tier_a_capitalised_pairs", "tier_b_given_name_pairs"):
            names_tot[k] += names[k]
        rec = {k: it[k] for k in ("source", "locator", "blob") if k in it}
        for k in ("deleted_at", "version_spec", "present_at_rev", "in_block_command_output"):
            if k in it:
                rec[k] = it[k]
        rec["bytes"] = len(it["data"])
        rec["lines"] = nlines
        if it["utf8_replacements"]:
            rec["utf8_replacement_chars"] = it["utf8_replacements"]
        if it["nul_bytes"]:
            rec["nul_bytes"] = it["nul_bytes"]
        rec["hits"] = {k: v for k, v in sorted(hits.items()) if k != "email_allowlisted"}
        if hits.get("email_allowlisted"):
            rec["email_allowlisted_counts"] = dict(Counter(r[1] for r in hits["email_allowlisted"]))
        rec["names"] = names
        files_out.append(rec)

    def distinct_list(cat_):
        rows = []
        for (c, red), d in distinct.items():
            if c == cat_:
                rows.append({"redacted": red, "count": d["count"], "objects": len(d["objects"]),
                             "subtypes": dict(d["subtypes"]),
                             "locators": sorted(d["objects"])[:25]})
        rows.sort(key=lambda r: (-r["count"], r["redacted"]))
        return rows

    src_counts = Counter(it["source"] for it in items)
    result = {
        "part": PART,
        "item": "N12(vi) content review -- mechanical pre-screen (block lines 72-85)",
        "block": {"path": BLOCK, "sha256_expected": BLOCK_SHA, "sha256_at_rev": block_sha_at_rev,
                  "match": block_sha_at_rev == BLOCK_SHA},
        "stamp_utc": stamp,
        "script": {"path": "scripts/audit_note_N12_content.py", "sha256": script_sha},
        "python": sys.version.split()[0], "platform": platform.platform(),
        "git_version": subprocess.run(["git", "--version"], stdout=subprocess.PIPE).stdout.decode().strip(),
        "rev": {"requested": a.rev, "resolved": rev},
        "refs": [{"object": o, "type": t, "ref": r} for o, t, r in refs],
        "scope": {
            "content_source": "git objects via git cat-file --batch (committed bytes; working tree not read)",
            "results_raw_at_rev": len(raw_paths),
            "handoff_md_at_rev": len(handoff_paths),
            "handoff_paths": handoff_paths,
            "untracked_handoff_md_not_screened": untracked_handoffs,
            # release v2 (2026-10-30, the raw reads): one commit no local ref reaches adds the design-seat handoffs
            "untracked_note": "untracked HANDOFF-*.md files in the working tree are in no commit a local ref reaches (one commit that no local ref reaches, the origin-only ref's that the design seat's answers of 2026-10-28 record, adds six design-seat handoffs; the release goes to a fresh repository holding main and the tags only), so not in the release unless committed later; listed by name only, not read",
            "history_only": {
                "block_command": "git " + " ".join(spec_cmd),
                "block_command_output": spec_deleted,
                "no_renames_deleted": norename_deleted,
                "ever_touched_minus_rev_tree": absent_now,
                "screened_paths": hist_paths,
                "screened_versions": sum(1 for it in items if it["source"] == "history-only"),
                "version_rule": "for each commit deleting the path (--no-renames): the blob at that commit's first parent",
            },
            "commits_reachable_from_all": len(all_commits),
            "commit_messages_screened": src_counts["commit-message"],
            "annotated_tags_screened": src_counts["tag-message"],
            "objects_screened_total": len(items),
            "objects_by_source": dict(src_counts),
            "bytes_screened_total": sum(len(it["data"]) for it in items),
        },
        "method": {
            "line_split": METHOD_LINE_SPLIT,
            "excerpt":"<= %d chars of the line after masking every [SCRATCH_PATH] [MACOS_TEMP_PATH] [LOCAL_HOME_PATH] [CLAUDE_AI_URL] [TRANSCRIPT_ID] (round 10: a whole path token, see excerpt_path_classes) [EMAIL] [PHONE] [ADDR] [IP] [CRED] [ID] [TOK] (alnum/_-+= run >= 20 with a letter and a digit) [NAME] (given-name list word or given-name pair) [W] (one to three words after Dear/Hi/Hello/From:/To:/Cc:/Subject:/Regards/Best,/Cheers,/Thanks, or before wrote:) span, and [ID_FLAG] (round 10, release: an identity-file flag with its argument, on a line naming ssh); window starts 10 chars before the hit, or at the hit's own token (see excerpt_release_rules); a cut part of a token at either end of the window is replaced by [CUT] unless it is a plain word, and at the right end a cut run of joined tokens up to its last reference-shaped token" % EXCERPT_MAX,
            "excerpt_path_classes": "round 10 (2026-10-12), excerpts only: a token holding a local scratch-path anchor (a path under the tmp directory, the per-uid scratch directory name, the per-user project-slug form) is masked whole as [SCRATCH_PATH]; a macOS per-user temp path under the folders directory as [MACOS_TEMP_PATH]; a local home-directory path as [LOCAL_HOME_PATH] (added because masking the longer scratch paths brought two home-directory paths into a 40-char window); a claude.ai session URL with its tail as [CLAUDE_AI_URL]; a uuid-shaped id as [TRANSCRIPT_ID]. The token is extended both ways to whitespace or a quote, backtick, bracket, brace, angle bracket, backslash, pipe, comma or semicolon; trailing '.' and ':' stay as punctuation. Where classes overlap, the order is SCRATCH_PATH, MACOS_TEMP_PATH, LOCAL_HOME_PATH, CLAUDE_AI_URL, TRANSCRIPT_ID, then the other placeholders. Counts, verdicts, categories, locators and redacted values do not read excerpts and are unchanged by it",
            "excerpt_release_rules": "round 10, release (2026-10-12), excerpts only, so that this JSON, screened in its turn by the history and licenses scans once committed, adds no value they read as new: (a) on a line that names ssh in any case, the identity-file flag (dash i, either case, at the line start or after whitespace) is masked together with its argument as one [ID_FLAG] span, which absorbs any placeholder inside it; (b) a token is a run of characters other than whitespace, a quote, backtick, bracket, brace, angle bracket, backslash, pipe, comma or semicolon; where the %d-char window cuts a token at either end (not inside a placeholder), the cut part is replaced by [CUT] unless it is ASCII letters only and the whole token has no reference shape (a scheme separator, a www label, a dotted name ending in two letters, a slash next to a name character, an at sign); where the hit lies in the token cut at the left and starts within %d chars of that token, the window starts at the token instead, so the hit stays visible where its token fits the window; where the right end cuts a run (characters other than whitespace, a quote, a backtick, a closing parenthesis or a closing bracket, so tokens joined by angle brackets, braces, opening parentheses or brackets, backslashes, pipes, commas or semicolons), the run's part in the window from its start, or the window's, to the end of its last token with a reference shape is replaced by [CUT] as well; so no excerpt starts or ends inside a token with a host, URL, path or id shape, and none ends inside such a joined run (one can start inside a joined run's later token); an excerpt can exceed the window by at most the placeholder's length at each end; (c) non-printable characters are mapped to spaces before masking, not after the cut. Counts, verdicts, categories, locators, redacted values and the leak guard do not read excerpts and are unchanged by it" % (EXCERPT_MAX, EXCERPT_LEFT_SHIFT_MAX),
            "redacted_form": "first 4 chars (fewer for a short value: at most half its length) + '...' + length + ':' + first 8 hex of sha256(value, utf-8)",
            "email_allowlist": "two addresses (the author's own; Anthropic's noreply) counted under email_allowlisted_counts, never listed as hits",
            "private_context": "confidentiality/private hits immediately preceded by '/' are tagged context=path (e.g. a /private/tmp path); reported, not discounted",
            "multiword_line_break": "multi-word phrases (do not share, not for publication, internal only, off the record, my wife/husband/partner/kid, Sent from) are also matched across a line end and tagged spans_next_line",
            "names": METHOD_NAMES % len(GIVEN_NAMES),
            "name_allowlist_fixed": sorted(NAME_ALLOW),
            "name_allowlist_et_al_detected": sorted(et_al),
            "generic_high_entropy": "alnum run >= 24 with a letter and a digit, not pure hex, Shannon entropy >= 3.5 bits/char; pure-hex runs >= 24 (hashes, shas) are skipped and only counted",
            "hex_tokens_skipped": hex_skipped,
            "infra_identifier": "supplementary category (RunPod proxy hosts / ssh users, labelled pod/volume/endpoint ids containing a digit, RUNPOD_* env values, ~/.ssh key file names, ssh -i arguments); masked in every excerpt",
            "url_hosts": "host labels that look like ids (>= 8 chars with letter+digit, >= 16 chars, or <alnum>-<port>) and IP hosts are redacted",
            "limitations": "regex heuristics only: no semantic reading; phone/address/name shapes are English-language/US/AU-centric; a sensitive span matching no pattern is not masked; correspondence markers are case-sensitive",
        },
        "patterns": {
            "email": EMAIL_RX.pattern,
            "phone": {k: r.pattern for k, r in PHONE_RXS},
            "street_address": {k: r.pattern for k, r in ADDR_RXS},
            "ipv4": IPV4_RX.pattern,
            "url": [URL_RX.pattern, WWW_RX.pattern],
            "confidentiality": {k: r.pattern for k, r in CONF_RXS},
            "correspondence": {k: r.pattern for k, r in CORR_RXS},
            "personal_life": {k: r.pattern for k, r in PERS_RXS},
            "credential": dict([(k, r.pattern) for k, r in CRED_RXS] + [("generic_high_entropy", GENERIC_TOKEN_RX.pattern)]),
            "infra_identifier": {k: r.pattern for k, r in INFRA_RXS},
            "names": NAME_PAIR_RX.pattern,
        },
        "totals": {k: dict(v) for k, v in sorted(totals.items()) if k != "email_allowlisted"},
        "totals_by_source": {s: dict(sorted(c.items())) for s, c in sorted(by_source.items())},
        "email_allowlisted_counts": dict(allow_counts),
        "email_distinct": distinct_list("email"),
        "phone_distinct": distinct_list("phone"),
        "street_address_distinct": distinct_list("street_address"),
        "ipv4_distinct": distinct_list("ipv4"),
        "credential_distinct": distinct_list("credential"),
        "infra_identifier_distinct": distinct_list("infra_identifier"),
        "url_hosts": sorted([{"host": h, "count": d["count"], "objects": len(d["objects"])} for h, d in hosts.items()],
                            key=lambda r: (-r["count"], r["host"])),
        "word_forms": {k: dict(sorted(v.items(), key=lambda x: (-x[1], x[0]))) for k, v in sorted(word_forms.items())},
        "names_totals": dict(names_tot),
        "identities": {
            "headers": [dict({"role": r, "name": n, "email": e, "count": c},
                             **({"commits": sorted(id_commits[(r, n, e)])} if e not in EMAIL_ALLOW.values() else {}))
                        for (r, n, e), c in sorted(identities.items())],
            "signed_commits": sorted(signed_commits),
            "signature_note": "signature blocks are not parsed; an SSH signature embeds the signer's public key, which is published with the commit",
            "timezone_offsets": dict(sorted(tz.items())),
            "commit_signatures": dict(sigs),
            "annotated_tags": tag_info,
        },
        "objects": files_out,
        "c2pa_declaration": {
            "reason": C2PA_REASON, "verdict": "FALSE-POSITIVE", "declared_by": "the PI, 2026-10-10",
            "pi_words_verbatim": C2PA_PI_WORDS,
            "implementation_by_code": (
                "a hit lying wholly inside the text content of a <c2pa:manifest> element of an .svg whose repository "
                "root path (matched exactly), blob length and blob sha256 match a C2PA_MANIFESTS entry carries "
                "verdict/reason/context; its value's subtype gains '@c2pa_declared'; the leak guard still covers it; "
                "the same string elsewhere is screened as before"),
            "manifests": {k_: {"length": v_[0], "sha256": v_[1]} for k_, v_ in C2PA_MANIFESTS.items()},
            "objects_with_c2pa_elements": dict(sorted(c2pa_objects.items())),
            "declared_hits_by_category": dict(sorted(c2pa_hits.items())),
        },
        "retained_in_history": retained,
    }
    # ---- leak guard: no collected raw value (len >= 5; allowlisted identities excepted) may appear in the output ----
    allowed_verbatim = set(EMAIL_ALLOW) | IDENTITY_NAME_ALLOW
    to_check = sorted(v for v in guard_values if len(v) >= 5 and v.lower() not in allowed_verbatim
                      and v not in allowed_verbatim and v not in STANDARD_SSH_FILES)
    result["leak_guard"] = {"raw_values_checked": len(to_check), "rule": "every collected raw value of length >= 5 (hits and non-allowlisted identity names/emails) asserted absent from the JSON text and the stdout summary before either is written; exempt: the two allowlisted e-mails, the allowlisted identity names, and standard OpenSSH file names %s" % sorted(STANDARD_SSH_FILES),
                            "constant_text_not_checked": "round 9: the JSON is checked with this script's own constant text blanked -- the 'patterns' block and every 'method' entry except %s -- because the screened corpus now holds this part's own earlier output, which quotes that text (an infra pattern matched two words of the ssh identity-flag description in the method prose of results/raw/2026-10-08_note-N12-content-screen.json; the words are not quoted here, so this note cannot re-trigger it); every value-derived field is still checked" % list(CONTENT_DERIVED_METHOD_KEYS)}
    js = json.dumps(result, indent=1, ensure_ascii=False, sort_keys=False) + "\n"
    # round 9: the text the guard reads -- the same JSON with the script's constant method and pattern text blanked
    js_chk = json.dumps(dict(result, patterns=None,
                             method={k_: v_ for k_, v_ in result["method"].items() if k_ in CONTENT_DERIVED_METHOD_KEYS}),
                        indent=1, ensure_ascii=False, sort_keys=False) + "\n"

    # ---- stdout summary ----
    summary = []
    P = lambda *x: summary.append(" ".join(str(y) for y in x))
    P("AUDIT-note-release v1.2 -- N12(vi) content pre-screen (%s)" % PART)
    P("stamp_utc %s  rev %s  block sha256 at rev %s (%s)" % (stamp, rev, (block_sha_at_rev or "absent")[:16],
                                                               "match" if block_sha_at_rev == BLOCK_SHA else "MISMATCH"))
    P("script sha256 %s" % script_sha)
    P("refs: " + ", ".join("%s=%s" % (r, o[:7]) for o, t, r in refs))
    P("scope: results/raw %d, HANDOFF %d, history-only versions %d (paths %s), commit messages %d (rev-list --all), tag messages %d; %d objects, %d bytes"
      % (len(raw_paths), len(handoff_paths), result["scope"]["history_only"]["screened_versions"], hist_paths,
         src_counts["commit-message"], src_counts["tag-message"], len(items), result["scope"]["bytes_screened_total"]))
    P("block command output (D filter): %s" % spec_deleted)
    P("untracked HANDOFF-*.md present but not committed (not screened): %d" % len(untracked_handoffs))
    P("")
    P("%-20s %8s %8s   by source" % ("category", "hits", "objects"))
    for k, v in result["totals"].items():
        bs = ", ".join("%s %d" % (s, by_source[s][k]) for s in sorted(by_source) if by_source[s].get(k))
        P("%-20s %8d %8d   %s" % (k, v["hits"], v["objects_with_hits"], bs))
    P("email allowlisted (counted separately): %s" % dict(allow_counts))
    for k in ("email_distinct", "phone_distinct", "street_address_distinct", "ipv4_distinct", "credential_distinct", "infra_identifier_distinct"):
        rows = result[k]
        P("%s: %d distinct values" % (k, len(rows)))
        for r in rows[:40]:
            P("   %-28s count %4d objects %3d %s" % (r["redacted"], r["count"], r["objects"], r["subtypes"]))
        if len(rows) > 40:
            P("   ... %d more in the JSON" % (len(rows) - 40))
    P("url hosts (%d distinct):" % len(result["url_hosts"]))
    for r in result["url_hosts"]:
        P("   %-48s %5d  objects %d" % (r["host"], r["count"], r["objects"]))
    P("word forms: %s" % json.dumps(result["word_forms"]))
    P("names: %s; et-al surnames auto-allowlisted: %d" % (dict(names_tot), len(et_al)))
    P("identities: %s" % json.dumps(result["identities"]["headers"]))
    P("timezone offsets: %s; commit signatures: %s; annotated tags: %s"
      % (dict(tz), dict(sigs), [(t["ref"], t["signed"]) for t in tag_info]))
    P("hex tokens >= 24 skipped (counted only): %d" % hex_skipped)
    P("C2PA declaration (round 9; the PI, 2026-10-10): objects with a <c2pa:manifest> element %d (%s); hits inside a "
      "declared blob, FALSE-POSITIVE: %s" % (len(c2pa_objects), dict(sorted(c2pa_objects.items())) or "none",
                                            dict(sorted(c2pa_hits.items())) or "none"))
    for l_ in retained_lines(retained):
        P(l_)
    P("leak guard: %d raw values checked against the JSON and this summary" % len(to_check))
    P("wrote %s" % os.path.relpath(out, ROOT))
    text_out = "\n".join(summary)
    leaked = [v for v in to_check if v in js_chk or json.dumps(v, ensure_ascii=False)[1:-1] in js_chk or v in text_out]
    if leaked:
        sys.exit("LEAK GUARD FIRED: %d raw values would be written (redacted: %s); nothing written"
                 % (len(leaked), [redact(v) for v in leaked[:10]]))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "x", encoding="utf-8") as fh:
        fh.write(js)
    print(text_out)
    return 0


def selftest():
    """Synthetic fixtures built at run time (no secret-shaped literal in source)."""
    fake_key = "sk-" + "ant-" + "Ab1" * 10
    fake_mail = "alice.example" + "@" + "example.org"
    fake_ip = ".".join(["203", "0", "113", "7"])
    fake_pod = "abcd" + "1234efgh56" + "-8888.proxy.runpod.net"
    lines = [
        "key = %s and Dear Alice Smith, wrote" % fake_key,
        "contact %s from %s" % (fake_mail, fake_ip),
        "open https://%s/lab now" % fake_pod,
        "call (555) 123-4567 or 0412 345 678 at 12 Baker Street",
        "Hi Bob, this is confidential; my wife",
        "the /private/tmp path; do not",
        "share this",
    ]
    text = "\n".join(lines) + "\n"
    hits, names, values, n, forms = screen_text(text, set(NAME_ALLOW))
    blob = json.dumps(hits)
    secrets = [fake_key, fake_mail, fake_ip, "abcd1234efgh56", "123-4567", "345 678", "Baker", "Alice", "Smith", "Bob"]
    leaked = [s for s in secrets if s in blob]
    cats = sorted(hits)
    ok = (not leaked and n == 7 and {"credential", "email", "ipv4", "url", "phone", "street_address",
                                     "correspondence", "confidentiality", "personal_life", "infra_identifier"} <= set(cats)
          and any(r[2].get("spans_next_line") for r in hits["confidentiality"]))
    print("selftest categories:", cats)
    print("selftest leaked:", len(leaked), "lines:", n, "names:", {k: v for k, v in names.items() if k != "tier_b_lines"})
    for c in cats:
        for r in hits[c][:3]:
            print("  ", c, r)
    # round 10: the excerpt path classes, each masked whole, wherever the 40-char window falls on it
    fake_scr = "/private" + "/tmp/" + "claude-" + "999" + "/-" + "Users-" + "someone-x/" + "abcd1234" + "…/s.txt"
    fake_tmp = "/private/var/" + "folders/" + "zz/" + "q1w2e3r4" + "/T/f.json"
    fake_url = "https://" + "claude.ai/" + "code/" + "session_" + "Zz9Yy8"
    fake_home = "/" + "Users/" + "someone" + "/Documents/x.py"
    fake_uid = "-".join(["0123abcd", "4567", "89ab", "cdef", "0123456789ab"])
    pc_lines = [("wrote %s. ok" % fake_scr, "[SCRATCH_PATH]"), ("at `%s` now" % fake_tmp, "[MACOS_TEMP_PATH]"),
                ("Session: %s" % fake_url, "[CLAUDE_AI_URL]"), ("id %s.jsonl" % fake_uid, "[TRANSCRIPT_ID]"),
                ("id (%s) x" % fake_uid, "[TRANSCRIPT_ID]"),
                ("loads %s now" % fake_home, "[LOCAL_HOME_PATH]")]
    pc_bad = ["claude-999", "Users-", "someone", "abcd1234", "q1w2", "folders/zz", "session_", "Zz9", "0123abcd", "0123456789ab"]
    pc_fail = 0
    for ln_, ph_ in pc_lines:
        for pos_ in range(len(ln_)):
            ex_ = excerpt(ln_, pos_, set(NAME_ALLOW))
            if any(b_ in ex_ for b_ in pc_bad):
                pc_fail += 1
        if ph_ not in excerpt(ln_, 0, set(NAME_ALLOW)):
            pc_fail += 1
    print("selftest path classes: %d lines, %d failures" % (len(pc_lines), pc_fail))
    ok = ok and pc_fail == 0
    # round 10, release: at every window position, (a) the history scan's identity-flag pattern finds nothing in the
    # excerpt as the JSON writes it, (b) every token of the excerpt is a whole token of the masked line, a
    # plain-word part of a token with no reference shape, or placeholder text (a placeholder fragment only at the
    # excerpt's own ends), and (c), independently of the rule's own regexes, no excerpt of a cut line ends with a
    # proper prefix (two characters or more) of a literal host, URL, id or joined path written in it, nor starts with
    # a proper suffix of a literal host, URL or id
    sw = "s" + "sh"
    idf_rx = re.compile("(?i)\\b" + sw + "\\b[^\\n]*?\\s-i\\s+(?P<v>\\S+)")
    id_lines = [sw + " -p 22 -" + "i ~/." + sw + "/key_one user@box", sw.upper() + " -I keyfile_two remote",
                "run " + sw + " with\x0b-" + "i\x0bkey3 now", "use " + sw + ": the flag -" + "i /etc/k4, -i k5",
                "an " + sw + " line\x01-" + "i\x01key6 with a control character"]
    host = "exa" + "mple" + ".org"
    cut_lines = ["see https:" + "//raw." + host + "/owner/repo/main/f.py, then sub." + host + "/2025/x/index.html "
                 "and pkg team/name-1.2 plus 0.15342 confidentiality figures tokenization",
                 "(the url=https:" + "//docs." + host + "/very/long/path/segment/that/runs/on plus more) fin",
                 "a.b.c.d.e.f.g.h " * 6,
                 "a chain ~/.cache/tool/<project>/<session>/files and then more plain words follow here",
                 "x ~/.cache/tool/<project>/<session>/<another>/<segment>,{third}|[fourth] end"]
    lit_refs = [   # per cut line: (refs checked at both ends, joined paths checked at the right end only)
        (["https:" + "//raw." + host + "/owner/repo/main/f.py", "sub." + host + "/2025/x/index.html",
          "team/name-1.2"], []),
        (["https:" + "//docs." + host + "/very/long/path/segment/that/runs/on"], []),
        ([], []),
        ([], ["~/.cache/tool/<project>/<session>/files"]),
        ([], ["~/.cache/tool/<project>/<session>/<another>/<segment>,{third}|[fourth]"])]
    ph_names = ["CUT", "ID_FLAG", "SCRATCH_PATH", "MACOS_TEMP_PATH", "LOCAL_HOME_PATH", "CLAUDE_AI_URL",
                "TRANSCRIPT_ID", "EMAIL", "PHONE", "ADDR", "IP", "CRED", "ID", "TOK", "NAME", "W"]
    rel_fail = 0
    for ln_ in id_lines + cut_lines + [l_ for l_, _ in pc_lines] + lines:
        v_ = excerpt_view(ln_)
        mline, cur_ = [], 0
        for s_, e_, ph_, _ in mask_spans(v_, set(NAME_ALLOW)):
            mline += [v_[cur_:s_], ph_]
            cur_ = e_
        mline = "".join(mline + [v_[cur_:]])
        mtoks = set(t_ for t_ in EXCERPT_PATH_STOP_RX.split(mline) if t_)
        for pos_ in range(len(ln_)):
            ex_ = excerpt(ln_, pos_, set(NAME_ALLOW))
            if sw in ln_.lower() and idf_rx.search(json.dumps(ex_, ensure_ascii=False)):
                rel_fail += 1
            if not ex_.isprintable():
                rel_fail += 1
            ex_toks = [t_ for t_ in EXCERPT_PATH_STOP_RX.split(ex_) if t_]
            for j_, t_ in enumerate(ex_toks):
                if not (t_ in mtoks or t_ in ph_names
                        or (j_ == 0 and any(p_.endswith(t_) for p_ in ph_names))
                        or (j_ == len(ex_toks) - 1 and any(p_.startswith(t_) for p_ in ph_names))
                        or (EXCERPT_PLAIN_WORD_RX.fullmatch(t_)
                            and any(t_ in m_ and not EXCERPT_REF_SHAPE_RX.search(m_) for m_ in mtoks))):
                    rel_fail += 1
            if ln_ in cut_lines:
                both_, right_ = lit_refs[cut_lines.index(ln_)]
                for r_ in both_ + right_:
                    if any(ex_.endswith(r_[:k_]) for k_ in range(2, len(r_))):
                        rel_fail += 1
                for r_ in both_:
                    if any(ex_.startswith(r_[-k_:]) for k_ in range(2, len(r_))):
                        rel_fail += 1
    for ln_ in id_lines:
        if EXCERPT_ID_FLAG[0] not in excerpt(ln_, 0, set(NAME_ALLOW)):
            rel_fail += 1
    sh_line = "see results_" + "x" * 12 + "/confidential_notes and more"   # a hit inside the token the window cuts
    if "confidential" not in excerpt(sh_line, sh_line.index("confidential"), set(NAME_ALLOW)):
        rel_fail += 1
    print("selftest release rules: %d lines, %d failures" % (len(id_lines) + len(cut_lines) + 1, rel_fail))
    ok = ok and rel_fail == 0
    print("selftest", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
