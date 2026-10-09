#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12-history: release scrub over the FULL history.

Covers N12 (i) secrets, (ii) identifiers, (v) size, and (iv)'s mechanical
checks (jlens-qwen36/ never tracked; every tracked .npz admitted by an explicit
.gitignore allowlist line; no model weights ever tracked). Block lines 72-85.

Read-only on the record: every git command here reads (log, rev-list,
cat-file, ls-tree, for-each-ref, count-objects, check-ignore --no-index,
show, merge-base, rev-parse). Nothing is staged, committed or written outside
--out / --json-out. Never runs git inside jlens-qwen36/ (its working tree is
read as plain files for the content-copy check only). Stdlib only (zipfile and
struct read .npz members and PNG chunks; numpy is not needed).

Sources scanned: every text blob reachable from any ref, every commit and tag
message, every commit and tag HEADER (author/committer/tagger lines, gpgsig
blocks; scanned in their own section), and the string content of every binary
blob (.npz unicode members decoded, printable-ASCII runs of every member, PNG
text chunks).

Round 2 (second checker) adds: the scanner-availability record (gitleaks / trufflehog installable via
Homebrew but not installed); the newline line count; two base64 key-material marker patterns and the 4.3-bar
sensitivity note; the jlens clone's .git/index read as a plain file; residual-space float vectors stored as
JSON; the remote-tracking reflogs read as plain files (push history, the unreachable commit); /Users/ paths
outside the repository; a pre-release scan of files not yet in history; the SSH-port form lenN:sha8.

Round 3 (third checker) adds: the RunPod network-volume NAME class (exactly re-counted, in the HEAD table, the
pre-release sensitive set and the leak assertion, with the name's stem); a deterministic order wherever a hash-ordered
set fed the output; the SSH-signature marker's mechanism, computed from each signature's byte layout; the
pre-release line split into redaction-rule values (a blocker) and the commit identities' own metadata (listed, not a
blocker); an enumeration-exposure caveat computed per sensitive value; when a path under data/m/ckpt/ is
tracked, the commit that first added it and what the fallback could not see in it; a hex-digest triage rule; and
a code-port rule (a line whose only port word is 'port of', the software sense, is not a port line).

Round 4 (fourth checker) fixes: the identifier class table's `src` column is the union of the class's sources (it
summed the per-value counts); the reason for the `update-network-volume` tool name describes its prose correctly;
a hex-only value is never cleared by the label rule (only the hex-digest rule clears hex, and the label rule now
needs a letter outside a-f), and the pending scan passes each match's line to the precise triage; and the pending
scan's new-value classes include email addresses (other than the service address and the commit identities'),
the one class of third-party personal data it scans.

Round 5 (guard fix, 2026-10-09): at a HEAD that holds this audit's own committed raws and scripts (09c3a8c on), the
round-4 leak assertion refused to write: it refused on every value printed in redacted form with the sensitive
flag, and generic tokens that this raw itself writes (class labels, pattern text, triage reasons, prose) had
entered history as values. Round 5 adds (a) TRIAGE16, value triage keyed by the first 16 hex of sha256(value),
for those values and for the values the pre-flip raw (results/raw/2026-10-08_note-N12-preflip.json) triaged,
and SHAPE_TRIAGE16, the pre-flip raw's triage of the credential-shaped fallback rows keyed by (path, key, the
value's 16-hex prefix); (b) a verdict-based leak guard (guard_candidates / guard_decide / guard_scan). Its
candidates are every value printed in redacted form with the sensitive flag, every known sensitive value (with the
session link's bare id), and every value of this run's tables that has a verdict other than FALSE-POSITIVE / PUBLIC /
LOCAL-PATH, a mechanical (not hash-keyed) record of a redaction-rule class, or a mechanical verdict on a value with a
generated-looking segment -- printed or not. Of those it exempts only the two values printed verbatim by policy
(SAFE_VERBATIM) and the values whose every verdict is FALSE-POSITIVE / PUBLIC / LOCAL-PATH, with no record of a
redaction-rule class and no generated-looking segment unless a hash-keyed entry (TRIAGE16 / SHAPE_TRIAGE16 /
MANUAL_TRIAGE) gave it, that carry no known value (in any case or separator variant) and no session link; it
refuses to write if any other candidate appears in either output. Known values of 8+ characters are matched as
plain substrings, case- and separator-insensitively; the all-digit ones (the SSH ports) digit-bounded, except inside
a run of 8+ hex characters (a digest); every other refused value of 8+ characters as a plain substring; shorter
ones word-bounded, as round 4 matched. (c) positive controls run before every write (and alone with --selftest):
the guard must refuse a real RunPod pod id and a real SSH port resolved from history in memory, a synthetic
secret-shaped value whose triage is UNTRIAGED, and (second check) the gap cases the round-5 checker found -- a
rule-class value with a mechanical exempt verdict, a METADATA value, a temp path with a generated segment, known
values glued to letters or inside an exempt value, case and separator variants, the bare session id -- each
injected into a copy of the outputs; and it must pass the outputs as written. The control values are held in
memory only. The redacted-form policy for everything printed is unchanged. (d) Found on re-reading the
regenerated raw (text that the audit's own commits made stale; no guard change): the `/Users/` per-file note for
code classifies each occurrence by the path segment after `/Users/` (a bare prefix or pattern text names no home
directory) and the recommendation after it is computed from those notes; the round-1 values-check attributes each
commit after the base by its subject; round 4 compares the fourth checker's figures with counts restricted to the
sources reachable from the checker's snapshot when the run is at a later HEAD (as round 3 does); R2-9's list of
the port-class values names the round-5 counts; R2-1's N13 line reports a committed file as committed.

--pin <commit>: scan the history as of <commit> (refs that descend from it are
replaced by it; HEAD = <commit>; the fallback runs `git log -p <those refs>`).
--since <commit> (default: the commit that added the audit block): sources new
since that commit are counted separately, so a count at <since> is the total
minus the new-since column.

REDACTION: these outputs are committed to a repository about to be public.
No candidate secret, RunPod id, IP address, SSH key name/fingerprint, laptop
hostname, personal email or third party's personal data is written verbatim.
Each is reported by locator, class, matched pattern, and the redacted form
    first 4 chars + '...' + '[len N]' + '#' + first 8 hex of sha256(value)
(SSH-port-class values: 'len' + N + ':' + first 8 hex of sha256 -- no digit of the value)
so the PI can match a value without seeing it. Before writing, the script
asserts that no value its guard covers appears verbatim in either output (round 5: the guard is verdict-based;
see guard_decide).

Individual triage of hits that no mechanical rule clears is recorded in
MANUAL_TRIAGE below, keyed by the first 8 hex of sha256(value) (the redacted form's hash), and (round 5) in
TRIAGE16 / SHAPE_TRIAGE16, keyed by the first 16 hex -- never by the value itself.

    jlens-qwen36/.venv/bin/python scripts/audit_note_N12_history.py \
        [--out results/raw/2026-10-08_note-N12-history.md] \
        [--json-out results/raw/2026-10-08_note-N12-history.json] [--selftest]
"""
import argparse
import base64
import bisect
import collections
import hashlib
import io
import json
import math
import os
import re
import struct
import subprocess
import sys
import threading
import zipfile
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
DEFAULT_MD = "results/raw/2026-10-08_note-N12-history.md"
DEFAULT_JSON = "results/raw/2026-10-08_note-N12-history.json"
# The round-2 raw's snapshot (its HEAD line); round 3 names what landed after it.
R2_HEAD = "bab921ce5229e72c22985d516e8b7ed07ef2cbee"

# The block's own fallback (N12(i), block line 77), verbatim.
FALLBACK_PATTERN = (r"(api[_-]?key|secret|token|password|sk-[A-Za-z0-9]|rp_[A-Za-z0-9]"
                    r"|BEGIN (RSA|OPENSSH)|AKIA[0-9A-Z]{16})")
FALLBACK_ALTS = [
    ("api[_-]?key", r"api[_-]?key"),
    ("secret", r"secret"),
    ("token", r"token"),
    ("password", r"password"),
    ("sk-[A-Za-z0-9]", r"sk-[A-Za-z0-9]"),
    ("rp_[A-Za-z0-9]", r"rp_[A-Za-z0-9]"),
    ("BEGIN (RSA|OPENSSH)", r"BEGIN (RSA|OPENSSH)"),
    ("AKIA[0-9A-Z]{16}", r"AKIA[0-9A-Z]{16}"),
]

MB, MIB = 10 ** 6, 2 ** 20
BINARY_EXT = {".npz", ".npy", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".pyc",
              ".safetensors", ".bin", ".gguf", ".pt", ".pth", ".ckpt", ".zip",
              ".gz", ".tar", ".pkl", ".pickle", ".h5", ".onnx", ".so", ".dylib",
              ".woff", ".woff2", ".ico", ".mlx", ".tflite", ".pb", ".joblib"}
WEIGHT_EXT = {".safetensors", ".bin", ".gguf", ".pt", ".pth", ".ckpt", ".h5",
              ".onnx", ".msgpack", ".mlx", ".tflite", ".pb", ".pkl", ".pickle",
              ".joblib", ".npy", ".model", ".tar", ".zip", ".gz"}
CRED_FILE_RE = re.compile(r"(?i)(^|/)(\.netrc|_netrc|\.git-credentials|\.env(\..*)?|"
                          r"credentials(\.json)?|\.npmrc|\.pypirc|id_(rsa|ed25519|ecdsa|dsa)"
                          r"(\.pub)?|[^/]*\.(pem|key|p12|pfx|jks|keystore)|secrets?\.[a-z]+)$")

# ---------------------------------------------------------------- patterns
# (name, regex, group holding the value or None for the whole match)
PRECISE = [
    ("aws_access_key_id (AKIA/ASIA)",
     r"(?<![A-Za-z0-9])(?:AKIA|ASIA)[0-9A-Z]{16}(?![A-Za-z0-9])", None),
    ("private_key_pem (RSA/OPENSSH/EC/DSA/PGP/ENCRYPTED)",
     r"-----BEGIN (?:(?:RSA|OPENSSH|EC|DSA|PGP|ENCRYPTED) )?PRIVATE KEY(?: BLOCK)?-----", None),
    ("anthropic_key sk-ant-", r"sk-ant-[A-Za-z0-9_\-]{20,}", None),
    ("openai_key sk-/sk-proj-",
     r"(?<![A-Za-z0-9_\-])sk-(?!ant-)(?:proj-|svcacct-|admin-)?[A-Za-z0-9_\-]{20,}", None),
    ("huggingface_token hf_", r"(?<![A-Za-z0-9_])hf_[A-Za-z0-9]{30,}", None),
    ("github_token ghp_/gho_/ghu_/ghs_/ghr_/github_pat_",
     r"(?<![A-Za-z0-9_])(?:(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,})",
     None),
    ("slack_token xox[abpr]-", r"(?<![A-Za-z0-9])xox[abpr]-[A-Za-z0-9\-]{10,}", None),
    ("runpod_api_key rpa_", r"(?<![A-Za-z0-9_])rpa_[A-Za-z0-9]{20,}", None),
    ("runpod_key_shape rp_ (20+)", r"(?<![A-Za-z0-9_])rp_[A-Za-z0-9]{20,}", None),
    ("credential_env_assignment (RUNPOD_API_KEY, HF_TOKEN, ...)",
     r"(?i)\b(?:RUNPOD_API_KEY|HF_TOKEN|HUGGING_FACE_HUB_TOKEN|HUGGINGFACE_TOKEN|"
     r"ANTHROPIC_API_KEY|OPENAI_API_KEY|WANDB_API_KEY|GITHUB_TOKEN|GH_TOKEN|"
     r"AWS_SECRET_ACCESS_KEY|AWS_ACCESS_KEY_ID|AWS_SESSION_TOKEN)\b\s*[:=]\s*(?P<v>\S+)", "v"),
    ("wandb_key (40 hex after wandb/api-key context)",
     r"(?i)(?:wandb|api[_-]?key)[^\n]{0,40}?(?<![0-9a-f])(?P<v>[0-9a-f]{40})(?![0-9a-f])", "v"),
    ("google_api_key AIza", r"(?<![A-Za-z0-9_\-])AIza[0-9A-Za-z_\-]{35}", None),
    ("generic_assignment",
     r"(?i)(api[_-]?key|secret|token|password|passwd|pwd|auth)\s*[:=]\s*['\"]?"
     r"(?P<v>[A-Za-z0-9_\-/+=.]{16,})", "v"),
    ("bearer_header", r"(?i)\bbearer\s+(?P<v>[A-Za-z0-9._\-+/=]{16,})", "v"),
    ("netrc_shape", r"(?im)^[ \t]*machine[ \t]+\S+[ \t]+(?:login[ \t]+\S+[ \t]+)?password[ \t]+\S+",
     None),
    ("aws_credentials_file_shape",
     r"(?im)^[ \t]*aws_(?:access_key_id|secret_access_key|session_token)[ \t]*=[ \t]*(?P<v>\S+)", "v"),
    ("url_with_userinfo",
     r"\b[a-zA-Z][a-zA-Z0-9+.\-]{0,15}://(?P<v>[^\s/:@'\"<>]{1,64}:[^\s/@'\"<>]{1,128})@[^\s/'\"<>]+", "v"),
    # extended set (values-check, checker's 'missed' list)
    ("jwt", r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}", None),
    ("stripe_key sk_/pk_/rk_ live/test", r"\b(?:sk|pk|rk)_(?:live|test)_[A-Za-z0-9]{10,}", None),
    ("slack_webhook", r"hooks\.slack\.com/services/[A-Za-z0-9/_\-]+", None),
    ("discord_webhook", r"discord(?:app)?\.com/api/webhooks/[0-9]+/[A-Za-z0-9_\-]+", None),
    ("sendgrid_key SG.", r"\bSG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}", None),
    ("telegram_bot_token", r"(?<!\d)\d{8,10}:[A-Za-z0-9_\-]{35}(?![A-Za-z0-9_\-])", None),
    ("pypi_token", r"\bpypi-AgE[A-Za-z0-9_\-]{20,}", None),
    ("npm_token", r"\bnpm_[A-Za-z0-9]{36}\b", None),
    ("google_oauth ya29.", r"\bya29\.[0-9A-Za-z_\-]{20,}", None),
    ("upper32 (legacy RunPod-key shape: 32-40 uppercase+digit)",
     r"(?<![A-Za-z0-9])(?=[A-Z0-9]*\d)(?=[A-Z0-9]*[A-Z])[A-Z0-9]{32,40}(?![A-Za-z0-9])", None),
    ("putty_private_key", r"PuTTY-User-Key-File-\d", None),
    ("url_secret_query_param",
     r"[?&](?:token|key|api_key|apikey|access_token|auth|sig|signature|password|secret)=(?P<v>[^&\s'\"<>]{8,})", "v"),
    ("quoted_secretish_assignment",
     r"(?i)\b[\w\-]*(?:key|secret|token|passw(?:or)?d|passwd|pwd|credential|auth)[\w\-]*['\"]?\s*[:=]\s*['\"]"
     r"(?P<v>[^'\"\s]{12,})['\"]", "v"),
    ("pgp_signature_or_key_block", r"-----BEGIN PGP (?:SIGNATURE|PUBLIC KEY BLOCK|PRIVATE KEY BLOCK)-----", None),
    # round 2 (second checker, finding 6): base64 key-material markers, so a key body without its PEM armor
    # is still caught. The marker strings are the base64 of the wire-format prefixes: 'openssh-key-v1' (an
    # OpenSSH private key body), and the length-prefixed key-type names ssh-rsa / ssh-ed25519 /
    # ecdsa-sha2-nistp / ssh-dss (a public or private SSH key blob). The value is the whole base64 run, which
    # must be 60+ characters (the shortest key blob, an ed25519 public key, is 68): a bare marker -- e.g. this
    # pattern's own text -- carries no key.
    ("ssh_key_material_base64 (openssh-key-v1 / ssh-rsa / ssh-ed25519 / ecdsa / ssh-dss markers)",
     r"(?<![A-Za-z0-9+/])(?=[A-Za-z0-9+/]{60})[A-Za-z0-9+/]*(?:b3BlbnNzaC1rZXktdjE|AAAAB3NzaC1yc2E|"
     r"AAAAC3NzaC1lZDI1NTE5|AAAAE2VjZHNhLXNoYTItbmlzdHA|AAAAB3NzaC1kc3M)[A-Za-z0-9+/]*={0,2}", None),
    ("pkcs_der_base64 (a run starting MII, 64+ characters: DER-encoded PKCS#1/#8 key or X.509 body)",
     r"(?<![A-Za-z0-9+/])MII[A-Za-z0-9+/]{61,}={0,2}(?![A-Za-z0-9+/=])", None),
]
N_PRECISE_ORIGINAL = 17
N_PRECISE_R1 = 31
# the marker strings inside the ssh_key_material_base64 pattern above (used to locate them per armor line)
SSH_B64_MARKERS = ("b3BlbnNzaC1rZXktdjE", "AAAAB3NzaC1yc2E", "AAAAC3NzaC1lZDI1NTE5", "AAAAE2VjZHNhLXNoYTItbmlzdHA",
                   "AAAAB3NzaC1kc3M")
PRECISE = [(n, re.compile(p), g) for n, p, g in PRECISE]
KEY_MATERIAL_PATTERNS = {PRECISE[N_PRECISE_R1][0], PRECISE[N_PRECISE_R1 + 1][0]}

# Context-free high-entropy scan (no assignment context needed): mixed-case runs and lowercase+digit runs.
CF_MIXED_RE = re.compile(r"(?<![A-Za-z0-9+/_\-=])[A-Za-z0-9+/_\-]{24,}={0,2}(?![A-Za-z0-9+/_\-])")
CF_LOWER_RE = re.compile(r"(?<![A-Za-z0-9])[a-z0-9]{20,}(?![A-Za-z0-9])")
# round 2: strict base64 runs (no '_' '-' '.'), 64+ characters, for the 4.3 bar's sensitivity note
B64_STRICT_RE = re.compile(r"(?<![A-Za-z0-9+/=_\-.])[A-Za-z0-9+/]{64,}={0,2}(?![A-Za-z0-9+/=_\-])")
CF_DESC = ("(a) maximal runs `[A-Za-z0-9+/_-]{24,}` (optional `=` padding) containing an uppercase letter, a "
           "lowercase letter and a digit, Shannon entropy > 4.3 bits/char; (b) maximal runs `[a-z0-9]{20,}` "
           "bounded by non-alphanumerics, with >= 3 digits and >= 3 letters, not hex-only, entropy > 3.5")
TEMP_PATH_RE = re.compile(r"(?:/private)?/(?:tmp|var/folders)/")
SESSION_LINK_RE = re.compile(r"claude\.ai/(?:code/)?(?:session_[A-Za-z0-9]{8,}|artifact/|chat/)")

# High-entropy candidates: maximal runs of the base64/hex alphabet, 32+ long, whose
# immediate left context is an assignment (`<key> =` / `<key>:` with optional quotes)
# or an Authorization / Bearer / X-Api-Key header.
HE_RUN_RE = re.compile(r"(?<![A-Za-z0-9+/=_\-])[A-Za-z0-9+/=_\-]{32,}")
HE_KEY_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_.\-]{0,60})[\"']?[ \t]*$")
HE_HEADER_RE = re.compile(r"(?i)\b(?:authorization|bearer|x-api-key|api-key|private-token)\b"
                          r"[ \t]*[:=]?[ \t]*(?:(?:bearer|token|basic)[ \t]+)?[\"']?$")
HE_CONTEXT_DESC = ("a maximal run `[A-Za-z0-9+/=_-]{32,}` whose left context is `<key>[\"']? *[:=] *[\"']?` "
                   "(key `[A-Za-z_][A-Za-z0-9_.-]{0,60}`) or an Authorization/Bearer/X-Api-Key/api-key/"
                   "private-token header")


def he_context(text, s):
    """Return the key name ('<header>' for a header) if the run at s sits in an assignment/header context."""
    pre = text[max(0, s - 120):s]
    nl = pre.rfind("\n")
    if nl >= 0:
        pre = pre[nl + 1:]
    stripped = pre.rstrip(" \t\"'")
    if stripped.endswith((":", "=")):
        kk = HE_KEY_RE.search(stripped[:-1])
        if kk:
            return kk.group(1)
    if HE_HEADER_RE.search(pre):
        return "<header>"
    return None


def iter_emails(text):
    i = text.find("@")
    while i >= 0:
        a = i
        while a > 0 and i - a < 64 and (text[a - 1].isascii() and (text[a - 1].isalnum() or text[a - 1] in "._%+-")):
            a -= 1
        mt = re.match(r"[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text[i + 1:i + 256])
        if a < i and mt:
            dom = mt.group(0)
            dom = re.match(r"(.*\.[A-Za-z]{2,})", dom).group(1)
            yield a, text[a:i + 1 + len(dom)]
        i = text.find("@", i + 1)


def iter_dot_local(text):
    for mt in re.finditer(r"\.local(?![A-Za-z0-9_\-])", text):
        a = mt.start()
        while a > 0 and (text[a - 1].isascii() and (text[a - 1].isalnum() or text[a - 1] in "-.")):
            a -= 1
        while a < mt.start() and text[a] in ".-":
            a += 1
        if a < mt.start() and (a == 0 or text[a - 1] not in "_"):
            yield a, text[a:mt.end()]

ID_PATTERNS = {
    "runpod_pod_id (context: pod)":
        r"(?i)\bpods?(?:[ _-]?id)?\b[`'\"*]{0,2}[ \t]*[:=]?[ \t]*[`'\"*(\[]{0,4}[ \t]*(?P<v>[a-z0-9]{12,16})\b",
    "runpod_pod_id (env assignment)":
        r"RUNPOD_POD_ID[ \t]*=[ \t]*['\"]?(?P<v>[A-Za-z0-9]{3,})",
    "runpod_volume_id (context: volume)":
        r"(?i)\b(?:network[ _-]?)?volume(?:[ _-]?id)?\b[`'\"*]{0,2}[ \t]*[:=]?[ \t]*[`'\"*(\[]{0,4}[ \t]*"
        r"(?P<v>[a-z0-9]{8,12})\b",
    # round 3 (third checker, finding 1): the network volume's NAME. Two shapes: a word-joined name ending in
    # _volume / -volume, or a word-joined name (3+ parts) directly before a size in GB/TB (a volume listing's
    # name column). Neither alternative quotes any value; the name itself is triaged by its hash only.
    "runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size)":
        r"(?<![A-Za-z0-9_\-])(?:(?P<v>[a-z][a-z0-9]*(?:[_-][a-z0-9]+){1,5}[_-]volume)(?![A-Za-z0-9_\-])"
        r"|(?P<v2>[a-z][a-z0-9]*(?:[_-][a-z0-9]+){2,6})[`'\"*]{0,2}[ \t,]+[`'\"*]{0,2}\d+(?:\.\d+)?[ \t]*"
        r"(?:GB|GiB|TB|TiB)\b)",
    "runpod_endpoint_or_template_id (context)":
        r"(?i)\b(?:endpoint|template)(?:[ _-]?id)?\b[`'\"*]{0,2}[ \t]*[:=]?[ \t]*[`'\"*(\[]{0,4}[ \t]*"
        r"(?P<v>[a-z0-9]{8,20})\b",
    "runpod_hostname (*.runpod.io / *.runpod.net)": r"(?i)(?P<v>\b[\w.\-]*runpod\.(?:io|net)\b)",
    "runpod_ssh_gateway_user": r"(?P<v>\b[a-z0-9]{8,20}-[0-9a-f]{6,12})@ssh\.runpod\.io",
    "proxy_hostname": r"(?i)(?P<v>\b[\w\-]+\.proxy\.[\w.\-]+\b)",
    "dot_local_hostname": "ANCHORED: each `.local` (not followed by a word char) expanded left over "
                          "`[A-Za-z0-9.-]`",
    "container_hostname (12 hex after host:/root@)":
        r"(?i)(?:\bhost(?:name)?\b[ \t]*[:=][ \t]*|root@)(?P<v>[0-9a-f]{12})\b",
    "ipv4_address":
        r"(?<![\d.])(?P<v>(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))(?!\.?\d)",
    "ipv6_address (full form)": r"(?i)(?P<v>\b(?:[0-9a-f]{1,4}:){7}[0-9a-f]{1,4}\b)",
    "ssh_port (number in an ssh/port/alias line)": None,   # line-scoped, below
    "ssh_key_path (~/.ssh/<name>)": r"(?:~|\$HOME|/Users/[^/\s]+|/root|/home/[^/\s]+)/\.ssh/(?P<v>[\w.\-]+)",
    "ssh_key_name (id_*)": r"\b(?P<v>id_(?:rsa|ed25519|ecdsa|dsa)[\w.\-]*)\b",
    "ssh_identity_flag (ssh -i <file>)": r"(?i)\bssh\b[^\n]*?\s-i\s+(?P<v>\S+)",
    "ssh_fingerprint": r"(?P<v>\bSHA256:[A-Za-z0-9+/]{43}=?|\b(?:[0-9a-f]{2}:){15}[0-9a-f]{2}\b)",
    "ssh_public_key":
        r"(?P<v>\b(?:ssh-(?:rsa|ed25519|dss)|ecdsa-sha2-nistp(?:256|384|521))\s+AAAA[A-Za-z0-9+/=]{20,})",
    "cloud_account_id":
        r"(?i)(?:\baccount(?:[ _-]?id)?\b[ \t]*[:=#]?[ \t]*(?P<v>\d{12})\b|(?P<v2>\buser_[A-Za-z0-9]{16,})"
        r"|(?P<v3>\borg-[A-Za-z0-9]{20,})|(?P<v4>\barn:aws:[^\s\"']+))",
    "claude_session_or_artifact_link":
        r"(?P<v>\bclaude\.ai/(?:code/)?(?:session_[A-Za-z0-9]{8,}|artifact/[A-Za-z0-9\-]{8,}|chat/[A-Za-z0-9\-]{8,}))",
    "local_temp_path ((/private)/tmp, (/private)/var/folders)":
        r"(?<![\w.\-/~])(?P<v>(?:/private)?/(?:tmp|var/folders)/[^\s'\"`)\]]+)",
    "claude_projects_path (~/.claude/projects/...)":
        r"(?P<v>(?:~|\$HOME|/Users/[^/\s]+)/\.claude/projects/[^\s'\"`)\]]+)",
    "passphrase_shaped (code word / pass phrase / password context)":
        r"(?i)\b(?:code[ -]?word|pass[ -]?phrase|passcode|password)\b[^\n]{0,40}?\b(?:is|was|:|=)"
        r"[^A-Za-z0-9\n]{0,10}(?P<v>[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,4})",
    "email_address": "ANCHORED: each `@` with local part `[A-Za-z0-9._%+-]{1,64}` to its left and "
                     "domain `[A-Za-z0-9.-]+\\.[A-Za-z]{2,}` to its right",
    "url_host": r"(?i)\b(?:https?|ssh|wss?|ftp|sftp)://(?P<v>[A-Za-z0-9.\-]+)",
}
ANCHORED = {"dot_local_hostname": iter_dot_local, "email_address": iter_emails}
ID_RE = {k: (re.compile(v) if (v and k not in ANCHORED) else None) for k, v in ID_PATTERNS.items()}
SAFE_VERBATIM = {"jspace-lab.local", "noreply@anthropic.com"}
SWEEP_RE = re.compile(r"(?<![A-Za-z0-9_\-./])([a-z0-9]{10}|[a-z0-9]{14})(?![A-Za-z0-9_\-])")
SWEEP_DESC = ("every token of exactly 10 or 14 characters from `[a-z0-9]` (not bounded by `[A-Za-z0-9_-./]` on "
              "the left or `[A-Za-z0-9_-]` on the right), with >= 2 digits and >= 3 letters, not hex-only")
SSH_LINE_RE = re.compile(r"(?i)\bssh\b|\bport\b|\balias\b|\s-p\s*\d")
PORT_NUM_RE = re.compile(r"(?<![\d.:\-\u2013@#+/])\b(?P<v>\d{4,5})\b(?![\d.%,])")
# round 3: 'port of' is the software sense in this record (an adapter's port of a rule, an MLX port of a library);
# a line whose every SSH_LINE_RE match is that word is not a port line. Residual risk, stated in the raw: a network
# port phrased 'port of <host>' on a line with no 'ssh', 'alias' or '-p' would be skipped.
CODE_PORT_RE = re.compile(r"(?i)port\s+of\b")
CODE_PORT_STATS = collections.Counter()


def code_port_only(line, where):
    """True if every ssh/port/alias match on the line is the word 'port' in 'port of ...' (a code port)."""
    trig = list(SSH_LINE_RE.finditer(line))
    if trig and all(m.group(0).lower() == "port" and CODE_PORT_RE.match(line, m.start()) for m in trig):
        CODE_PORT_STATS[where + "_lines"] += 1
        CODE_PORT_STATS[where + "_numbers"] += sum(1 for pm in PORT_NUM_RE.finditer(line)
                                                   if not re.fullmatch(r"(19|20)\d\d", pm.group("v")))
        return True
    return False
VOLNAME_CLASS = "runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size)"
VOLNAME_SUFFIX_RE = re.compile(r"[_-]volume$")
# classes whose values are re-counted exactly across the whole history (pass 2). A set: every loop over it
# goes through exact_recount_classes(), which returns them in ID_PATTERNS order (round 3: a set's own order is
# hash-randomized per process, and it fed the output's order).
EXACT_RECOUNT = {"runpod_pod_id (context: pod)", "runpod_pod_id (env assignment)",
                 "runpod_volume_id (context: volume)", VOLNAME_CLASS, "runpod_endpoint_or_template_id (context)",
                 "container_hostname (12 hex after host:/root@)",
                 "ssh_port (number in an ssh/port/alias line)",
                 "passphrase_shaped (code word / pass phrase / password context)",
                 "claude_session_or_artifact_link"}

PUBLIC_HOSTS = {
    "github.com", "raw.githubusercontent.com", "huggingface.co", "arxiv.org", "www.arxiv.org",
    "pypi.org", "docs.python.org", "claude.ai", "claude.com", "www.anthropic.com",
    "anthropic.com", "docs.anthropic.com", "docs.runpod.io", "www.runpod.io", "runpod.io",
    "doi.org", "openreview.net", "www.lesswrong.com", "www.alignmentforum.org", "x.com",
    "twitter.com", "en.wikipedia.org", "localhost", "pytorch.org",
    "download.pytorch.org", "transformer-circuits.pub", "www.w3.org", "w3.org",
    "allenai.org", "nbviewer.org", "colab.research.google.com", "scholar.google.com",
    "matplotlib.org",
}
# What an IDENTIFIER value is doing in a tracked code file at HEAD (read in context by Code).
CODE_LOCATOR_NOTES = {
    "valence_core/m/resume.py": "the real pod id used as the test value of resume.py's self-test of "
                                "`pod_id()` reading RUNPOD_POD_ID (a fixture; nothing connects to it)",
}

# Individual triage of values no mechanical rule clears, keyed by sha256(value)[:8].
# Each reason was written after reading the hit in context; the value is never stored.
# Third field: whether the value must stay redacted in the outputs (True) or may be shown
# (False: provably non-sensitive -- a code token, a file name, a test value).
POD = ("IDENTIFIER", "a RunPod pod id (the record names it as an A100-80GB pod in US-CA-2); not a "
       "credential -- a pod id gives no access without the account's API key or SSH key", True)
PORT = ("IDENTIFIER", "a RunPod pod's public SSH port (the `box` ssh alias's port, changed on every "
        "respawn); on its own a port names no host (see the ipv4 class for addresses)", True)
MANUAL_TRIAGE = {
    # (i-b) generic_assignment
    "087998a4": ("FALSE-POSITIVE", "a row of '=' separator characters on the line after the word "
                         "'single-token' (the pattern's \\s spans the newline); not a value", False),
    # (i-b) high entropy
    "32dfe00b": ("FALSE-POSITIVE", "an environment-variable assignment of a repository-relative lens "
                         "file path inside a recorded command line", False),
    "7e4755a0": ("FALSE-POSITIVE", "a macOS per-user temporary-directory path (an OS-generated folder "
                         "name) inside a self-test message; not a credential", True),
    # (ii) RunPod
    "a39ed293": POD,
    "d781dc45": POD,
    "7323177b": ("FALSE-POSITIVE", "a synthetic test value (RUNPOD_POD_ID set to a made-up name in a "
                         "laptop kill/resume experiment)", False),
    "e79618f8": ("IDENTIFIER", "a RunPod network volume id (the 500 GB US-CA-2 volume holding the OLMo "
                         "checkpoints); not a credential", True),
    # (ii) RunPod volume name (round 3)
    "e6c48186": ("IDENTIFIER", "the RunPod network volume's name (the display name of the same 500 GB US-CA-2 "
                         "volume, listed beside its id); not a credential -- a name gives no access without the "
                         "account's API key", True),
    # round 4 (fourth checker, finding 2): the reason reworded -- the prose says the volume cannot be moved
    "84cbedd5": ("FALSE-POSITIVE", "the RunPod MCP tool name `update-network-volume`, cited in prose explaining that "
                         "a network volume cannot be moved between datacenters (the tool renames and grows only); a "
                         "public API operation's name, not a volume name", False),
    "54719d1e": ("IDENTIFIER", "the pod container's hostname (a Docker container id) printed in a box "
                         "script's run header; ephemeral; not a credential", True),
    # (ii) addresses
    "f1412386": ("FALSE-POSITIVE", "outline numbering inside a model-generated response in a B2-r control "
                         "trial; not an address", True),
    # (ii) ssh ports
    "47e5fcc0": PORT, "2be8ef0e": PORT, "54e4496b": PORT,
    "dae17182": PORT, "25124cd5": PORT,
    "864a936a": ("FALSE-POSITIVE", "a token-window length on a line that also mentions a "
                         "port; not a port", False),
    "cccd34d9": ("FALSE-POSITIVE", "the local jlens viewer's uvicorn port, bound to the loopback "
                         "interface (`--host <loopback> --port`); a local dev server, not a remote host", False),
    "25d7e9c2": ("FALSE-POSITIVE", "a local process id from `ps -p` (ps's -p flag, not ssh's)", False),
    "c2ec3eb9": ("FALSE-POSITIVE", "a local process id from `ps -p` (ps's -p flag, not ssh's)", False),
    # (ii) ~/.ssh paths
    "b79606fb": ("FALSE-POSITIVE", "the SSH client config file (~/.ssh/config); a file name, not a key "
                         "name; no key file name or key material appears anywhere", False),
    "b13f33ea": ("FALSE-POSITIVE", "a dated backup of ~/.ssh/config; a file name, not a key name", False),
    "5c862486": ("FALSE-POSITIVE", "a dated backup of ~/.ssh/config (sentence-final period); a file "
                         "name, not a key name", False),
    # (ii) url hosts
    "7336dcf5": ("FALSE-POSITIVE", "a URL inside a model-generated response (OLMo DPO, B2-r "
                         "exploration); model output, not infrastructure", True),
    "6008c26f": ("FALSE-POSITIVE", "a 'scheme://word' fragment inside garbled model output", False),
    # (ii) Claude session link
    "236329f4": ("IDENTIFIER", "a Claude Code session URL in a commit-message trailer (Claude-Session:); "
                         "viewing it requires the account owner's login; not a credential", True),
    # (i-b) context-free scan: values no mechanical rule clears, triaged in context
    "68042871": ("FALSE-POSITIVE", "a slash-separated list of verdict labels in a referent-check raw; not a "
                         "path and not a value", False),
    "22373092": ("LOCAL-PATH", "the per-launch id in a local Jupyter kernel's runtime connection-file name, inside "
                         "a process list that a preflight refusal printed; the file name is not the kernel's key; "
                         "not a credential", True),
    # (ii) id-shape sweep remainder
    "f8769913": ("FALSE-POSITIVE", "a table column name (a shuffle-null 95th-percentile column) in an analysis raw", False),
    "9974dfa7": ("FALSE-POSITIVE", "an arithmetic product written with x signs in a values-check raw", False),
    # pre-release scan (round 2): pending audit files
    "17480b8e": ("FALSE-POSITIVE", "a BibTeX citation key (author surname + year + title word) in a citation "
                         "field of the N12-licenses outputs", False),
    # (i) / rule 5: pass-phrase-shaped text
    "c63d5fbd": ("PASSPHRASE-SHAPED", "a synthetic three-word 'code word' that the 2026-08-05 LoRA "
                         "feasibility spike trained the model to emit (an overfit target, printed in the "
                         "spike's raw); not a credential by origin. Reported redacted under hard rule 5 so "
                         "the PI can compare its hash against the continuity password (N12(iii))", True),
}


# Round 5 (2026-10-09): value triage keyed by the first 16 hex of sha256(value). Each entry: (verdict, reason,
# sensitive, source). The values are never stored; the comment after each key gives its class(es) and redacted
# form. 'sensitive' keeps the round-4 display: True prints the redacted form; False only for public website hosts
# of the url_host class, which the identifier table prints verbatim like the other public hosts.
TRIAGE16 = {
    # local_temp_path `/tmp...[len 6]#fc22e2de`
    'fc22e2dea2799ddc': ('LOCAL-PATH', "the bare temporary-directory prefix followed by a colon, in this raw's own values-check prose (a count of bare prefixes); names no file and no session",
                         True, "pre-flip 3(a) leak list; the script's own verdict, carried; reason Code's (round 5)"),
    # ipv4_address `0.0....[len 7]#19e36255`
    '19e36255972107d4': ('FALSE-POSITIVE', "the unspecified IPv4 address, which this script's own address classifier names in its class label and in the verdict reason it prints; identifies no machine",
                         True, "pre-flip 3(a) leak list; the script's own verdict, carried; reason Code's (round 5)"),
    # ssh_identity_flag `<fil...[len 7]#1aedc48e`
    '1aedc48eac0ed163': ('FALSE-POSITIVE', "the same placeholder [the angle-bracketed file placeholder of this class's label, with trailing punctuation], from this class's label in the history raw's table",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # ssh_identity_flag `<fil...[len 8]#c17d7b45`
    'c17d7b45d14c2522': ('FALSE-POSITIVE', "the same placeholder [the angle-bracketed file placeholder of this class's label, with trailing punctuation], from this class's label in the history raw's pattern list",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # ssh_identity_flag `<fil...[len 9]#13dfbe0e`
    '13dfbe0ea7c7925d': ('FALSE-POSITIVE', "the placeholder '<file>' with trailing punctuation, from this class's own label as the history JSON prints it",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # passphrase_shaped `A-Za...[len 9]#fab79a8e`
    'fab79a8ed5412bf8': ('FALSE-POSITIVE', "a fragment of this class's own regular expression, as the history JSON's pattern table stores it; not a phrase",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # ssh_key_name `id_e...[len 10]#8e5d92fd`
    '8e5d92fdbeaf08fd': ('FALSE-POSITIVE', "the other generic default key-file name in the same description [the history raw's description of its credential-file path pattern]",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # ssh_key_name `id_r...[len 6]#f40883a1`
    'f40883a1267f9443': ('FALSE-POSITIVE', "a generic default key-file name inside the history raw's description of its credential-file path pattern; no key file is named or tracked",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # runpod_hostname `runp...[len 10]#421bbde9`
    '421bbde981cebce3': ('FALSE-POSITIVE', "the RunPod service domain as written in this class's own label, printed by the history JSON's tables",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # runpod_hostname `runp...[len 9]#3124edae`
    '3124edaeda39b6f8': ('PUBLIC', "RunPod's public site domain (on the history script's own public-host list), here inside class labels and flag text",
                         True, "pre-flip 3(c), Code's triage; also on the pre-flip 3(a) leak list"),
    # claude_projects_path `~/.c...[len 22]#a83bf7e9`
    'a83bf7e975a73bbe': ('LOCAL-PATH', "the class label's own path template (the Claude projects directory followed by an ellipsis), as this raw and its JSON print it; names no project and no session",
                         True, "pre-flip 3(a) leak list; the script's own verdict, carried; reason Code's (round 5)"),
    # claude_projects_path `~/.c...[len 43]#1a4fb901`
    '1a4fb901c1a3ec03': ('LOCAL-PATH', "a path template with angle-bracket placeholders for the project and the session id, in this script's own triage reason for the Claude projects class; names no project and no session",
                         True, "pre-flip 3(a) leak list; the script's own verdict, carried; reason Code's (round 5)"),
    # context_free `/Use...[len 42]#77f5bcb1`
    '77f5bcb11b1f4a7d': ('LOCAL-PATH', "a path under the author's home directory (a local Python library directory) in N11's printed sys.path of the regression-suite run; the author is named in the repository; not a credential",
                         True, "pre-flip 3(c), Code's triage"),
    # proxy_hostname/runpod_hostname `len21:80e1d10e`
    '80e1d10e06456ba4': ('FALSE-POSITIVE', "a synthetic fixture in the content script's self-test (a placeholder number and the proxy suffix; its pod-id part is assembled from string pieces at run time); names no real host",
                         True, "pre-flip 3(c), Code's triage"),
    # runpod_hostname `prox...[len 16]#e0b5f502`
    'e0b5f5021a3c7311': ('PUBLIC', "the RunPod proxy service's domain, named in the content review's flag text about the ssh alias; it names the service, not a pod or an account",
                         True, "pre-flip 3(c), Code's triage"),
    # runpod_hostname `ssh....[len 13]#f8ec340d`
    'f8ec340dd4ad9f9d': ('PUBLIC', "RunPod's public SSH gateway host, named in the same flag text [the content review's flag text about the ssh alias]; it names no pod or account",
                         True, "pre-flip 3(c), Code's triage"),
    # runpod_hostname `docs...[len 14]#f4b8c41f`
    'f4b8c41f331cd18d': ('PUBLIC', "an entry of the history script's own public-host list (RunPod's documentation site)",
                         True, "pre-flip 3(c), Code's triage"),
    # runpod_hostname `www....[len 13]#f53cd0c4`
    'f53cd0c45f9ec8f2': ('PUBLIC', "an entry of the history script's own public-host list (RunPod's www site)",
                         True, "pre-flip 3(c), Code's triage"),
    # ssh_identity_flag `argu...[len 11]#a36807c9`
    'a36807c9aa7c8226': ('FALSE-POSITIVE', "the word after the ssh identity flag in the content screen's category description; not a file",
                         True, "pre-flip 3(c), Code's triage"),
    # ssh_identity_flag `<fil...[len 9]#a2b73321`
    'a2b733213c2767ef': ('FALSE-POSITIVE', "the same placeholder [the angle-bracketed file placeholder of this class's label, with trailing punctuation], from this class's label in the history script's source",
                         True, "pre-flip 3(c), Code's triage"),
    # ssh_key_path `conf...[len 11]#41c256ae`
    '41c256aeb502cb07': ('FALSE-POSITIVE', "the prefix of a timestamped backup name of the standard ssh client config, quoted in the content review's flag text, which says it is not a key name; no key file",
                         True, "pre-flip 3(c), Code's triage"),
    # url_host `crea...[len 19]#01ac74e6`
    '01ac74e6305467bf': ('PUBLIC', "a public website host (the Creative Commons site), in the licenses raw's licence links",
                         False, "pre-flip 3(c), Code's triage"),
    # url_host `api....[len 14]#5b3097c5`
    '5b3097c5c7bd083b': ('PUBLIC', "a public website host (GitHub's REST service host), in the licenses raw's source URLs",
                         False, "pre-flip 3(c), Code's triage"),
    # url_host `docs...[len 15]#26ca8550`
    '26ca8550a0510ee2': ('PUBLIC', "a public website host (GitHub's documentation host), in the licenses raw's source URLs",
                         False, "pre-flip 3(c), Code's triage"),
    # ssh_port, Code's triage (round 5): a number new at 02b6a610
    'd7b6fab9aa91943d': ('FALSE-POSITIVE', "the committed history raw's fallback-grep hit-line count, quoted in the 02b6a610 commit message on a line whose 'port' is one word in a list of identifier kinds; a count, not a port",
                         True, 'Code, round 5, read in context'),
    # ssh_port, Code's triage (round 5): a number new at 02b6a610
    'f783659d8065aa37': ('FALSE-POSITIVE', 'the pre-flip interim fallback-grep hit-line count, quoted on the same 02b6a610 commit-message line; a count, not a port',
                         True, 'Code, round 5, read in context'),
    # id-shape sweep, Code's triage (round 5): two tokens first committed in 09c3a8c that the pre-flip raw's dump
    # does not print (the dump has no sweep table)
    'a15c50fd9bb3ffdf': ('FALSE-POSITIVE', "a piece of the content script's synthetic self-test fixture (string pieces "
                         "concatenated at run time into a made-up proxy host); names no pod", True,
                         'Code, round 5, read in context'),
    'f66375188136ef7f': ('FALSE-POSITIVE', "the same synthetic fixture, assembled, in that self-test's list of values "
                         "that must not appear in its output; a made-up placeholder, not a RunPod id", True,
                         'Code, round 5, read in context'),
}
# Round 5: the pre-flip raw's triage of the 128 credential-shaped fallback rows (its section 3(c)), keyed by
# (path, key in lower case, the first 16 hex of sha256(value)); each entry: (verdict, reason). Code re-read
# every row in context before carrying it (round 5) and agrees with each verdict.
SHAPE_TRIAGE16 = {
    ('results/raw/2026-10-08_note-N12-history.md', 'token', '8d33f520a3c4cef8'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', 'prose quoting a key spelled with a trailing colon; the captured value is the closing backtick'),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '39bdcc67ae893fc1'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '790d326121c28d07'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '886384e4c6d06100'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'a9502067f2684276'):  # 4 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'ab35ea0cb6a8fe5f'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'd021497da982a488'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '476e300e27f08a67'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'a73a6e2153d3108a'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'fbc7671ed7a74fa3'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '70af3d9e2d7accd5'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'b063f0e9448e5740'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'efaba63d61f25a1c'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '6e80c16f8163d7f9'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'e22619e40e3ac394'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'f5c4e67de35720b2'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '17660783aa5202cd'):  # 4 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '6e8a85d86ab579fc'):  # 4 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'fab00b52f1b3af08'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '06bcf7b3c7fbba1a'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'a95fdd8b6e9b9547'):  # 6 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '9ed2de3dff6684e3'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '95b6524305037473'):  # 4 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'e3df8067db1e3b19'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'eb5ef41a5c6d87b0'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '1d4b10b53e497027'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'd9b622cd7fd1da72'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'cd58a10861b6b066'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '8593ff18bb498c12'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '2af4268f43523757'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '070f42a27ebaa4b3'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '7a48bb773b2dbd9a'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'c27ba29889887d00'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '88eddb53252eff9d'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '029221aa6892959b'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '076642afd215536b'):  # 4 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '328dfb7dafc9c30f'):  # 3 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'b735f27d9b7450c7'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'dc24be923de7bdde'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '8ff70da0b56f1418'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '56181af002d0e6cf'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '00cfee510a81a6d4'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'e8bd41a9d48c42c1'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'ffe03c205e007f3f'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '2d51e294c8a30754'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '715e08cd3c9eb8de'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '7714df9f7f8969d6'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '181060cbf8f3c897'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '1ce51ffc321ef4d4'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', 'f72afd0d1e87c87d'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id)"),
    ('results/raw/2026-10-08_note-N13-provenance.json', 'token', '3d758122c29d47cc'):  # 2 row(s) at 6485da2
        ('FALSE-POSITIVE', "an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256)"),
    ('results/raw/2026-10-08_note-N16-decoding.json', 'max_new_tokens', 'a683c5c5349f6f7f'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "a decoding parameter (maximum new tokens) recorded as 'n/a'"),
    ('results/raw/2026-10-08_note-N16-decoding.md', 'eos_token', 'd918ff431c288b10'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "LLM-token sense: the model's end-of-sequence token string"),
    ('results/raw/2026-10-08_note-N3-echo-robustness.json', 'token', '5141d821294bd8f1'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "the same sentence as the md's line [a label's token, then its probe-AUC range], in the JSON"),
    ('results/raw/2026-10-08_note-N3-echo-robustness.json', 'token', 'b4a03256a339c539'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "the same sentence as the md's line [a label's token, then its probe-AUC range], in the JSON"),
    ('results/raw/2026-10-08_note-N3-echo-robustness.md', 'token', '5141d821294bd8f1'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "LLM-token sense: a label's token, then its probe-AUC range"),
    ('results/raw/2026-10-08_note-N3-echo-robustness.md', 'token', 'b4a03256a339c539'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "LLM-token sense: the second label's token, then its probe-AUC range"),
    ('results/raw/2026-10-08_note-tier1_valuescheck.md', 'secret', '46dc943e3424a225'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "prose ('Informational, not a secret' followed by a path prefix); no value"),
    ('scripts/audit_note_N12_history.py', 'token', '8d33f520a3c4cef8'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "the same prose [quoting a key spelled with a trailing colon; the captured value is the closing backtick], in the script that writes it"),
    ('scripts/audit_note_N13.py', 'cite_token', '97ba63ebc3d84b64'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "a document:line citation label in N13's trigger table"),
    ('scripts/audit_note_N13.py', 'cite_token', '14fa637189542a09'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', "a document:line citation label in N13's trigger table"),
    ('scripts/audit_note_N16.py', 'tokens', '416759ca652721f6'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', 'a decoding-parameters table entry whose value starts with a run label (B2-r)'),
    ('scripts/audit_note_N2.py', 'max_tokens', 'ce7f5d9dffb4a889'):  # 1 row(s) at 6485da2
        ('FALSE-POSITIVE', 'source code (a keyword argument) inside a regular expression of a referent check'),
}

# Round 5: the leak guard's policy (guard_candidates, guard_decide). A value is exempt only if it is one of the two
# values printed verbatim by policy (SAFE_VERBATIM), or: every verdict it receives in this run is one of
# GUARD_EXEMPT_VERDICTS, it is not one of the known sensitive values (the pre-release section's set, plus the
# session link's bare id), it carries none of them inside it (in any case or separator variant) and no session link,
# and -- for every record of a redaction-rule class, and (second check) for every record of a value with a
# generated-looking segment (has_random_segment) -- that verdict comes from an explicit hash-keyed entry (TRIAGE16,
# SHAPE_TRIAGE16 or MANUAL_TRIAGE), never from a mechanical rule alone. Every other value the run redacts, finds or
# knows is guarded, printed or not.
GUARD_EXEMPT_VERDICTS = ("FALSE-POSITIVE", "PUBLIC", "LOCAL-PATH")
GUARD_REFUSE_VERDICTS = ("TRUE-SECRET-CANDIDATE", "IDENTIFIER", "PASSPHRASE-SHAPED", "UNTRIAGED")
SWEEP_CLASS = "id-shape sweep (RunPod-id-shaped token)"
SHAPE_CLASS = "credential-shaped fallback row"
# The identifier classes the routing's redaction rule names (RunPod ids, names and hosts, SSH ports / keys /
# fingerprints / identity files, container and laptop hostnames, IP addresses, the session link, the
# pass-phrase-shaped value, email addresses, cloud account ids), as the pre-flip raw partitioned them: every
# identifier class except the two local-path classes and url_host; plus the id-shape sweep.
NON_RULE_ID_CLASSES = ("local_temp_path", "claude_projects_path", "url_host")
REDACTION_RULE_CLASSES = tuple(c for c in ID_PATTERNS if not c.startswith(NON_RULE_ID_CLASSES)) + (SWEEP_CLASS,)
assert all(re.fullmatch(r"[0-9a-f]{16}", k_) for k_ in TRIAGE16), "TRIAGE16 keys are 16 hex"
assert all(re.fullmatch(r"[0-9a-f]{16}", k_[2]) for k_ in SHAPE_TRIAGE16), "SHAPE_TRIAGE16 keys hold 16 hex"
assert not {k_[:8] for k_ in TRIAGE16} & set(MANUAL_TRIAGE), "a TRIAGE16 key shadows a MANUAL_TRIAGE key"
assert all(e_[0] in GUARD_EXEMPT_VERDICTS + GUARD_REFUSE_VERDICTS for e_ in TRIAGE16.values())
assert all(e_[0] in GUARD_EXEMPT_VERDICTS for e_ in SHAPE_TRIAGE16.values())


# ---------------------------------------------------------------- helpers
def sh(args, input=None, check=True, cwd=ROOT):
    p = subprocess.run(args, cwd=cwd, input=input, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    if check and p.returncode != 0:
        raise SystemExit(f"command failed ({p.returncode}): {args!r}\n{p.stderr.decode(errors='replace')}")
    return p


def git(*args, input=None, check=True):
    return sh(["git", "-c", "core.quotepath=off", *args], input=input, check=check).stdout


def sha256_hex(b):
    return hashlib.sha256(b).hexdigest()


REDACTED_SENSITIVE = set()


def red(v, sensitive=True):
    """first 4 chars + '...' + [len N] + '#' + sha256[:8]."""
    s = v if isinstance(v, str) else v.decode("utf-8", "replace")
    if sensitive:
        if len(s) <= 4:
            raise SystemExit(f"a sensitive value of length {len(s)} cannot be redacted by the prescribed form")
        REDACTED_SENSITIVE.add(s)
    elif len(s) <= 4:
        SHORT_SHOWN.add(s)
    return f"{s[:4]}...[len {len(s)}]#{sha256_hex(s.encode())[:8]}"


SHORT_SHOWN = set()   # values of <= 4 characters that the generic form prints in full (non-sensitive only)


def red_port(v, sensitive=True):
    """SSH-port form (round 2, routing): 'len' + length + ':' + sha256[:8] -- no digit of the value."""
    s = v if isinstance(v, str) else v.decode("utf-8", "replace")
    if sensitive:
        REDACTED_SENSITIVE.add(s)
    return f"len{len(s)}:{sha256_hex(s.encode())[:8]}"


PORT_CLASS = "ssh_port (number in an ssh/port/alias line)"


def show(cls, v, sensitive=True):
    """Redacted display of a value of class cls: the port form for the ssh_port class, else the generic form."""
    if cls == PORT_CLASS or (isinstance(cls, (list, tuple, set)) and PORT_CLASS in cls):
        return red_port(v, sensitive)
    return red(v, sensitive)


def vkey(v):
    """Key of MANUAL_TRIAGE: the same 8-hex sha256 prefix the redacted form prints."""
    return sha256_hex(v.encode())[:8]


def exact_recount_classes():
    """EXACT_RECOUNT in ID_PATTERNS order (deterministic; never the set's own hash-randomized order)."""
    return [c for c in ID_PATTERNS if c in EXACT_RECOUNT]


def most_common_sorted(counter):
    """Counter.most_common() with ties broken by the label (most_common keeps insertion order among ties,
    and insertion order can come from a hash-ordered set)."""
    return sorted(counter.items(), key=lambda kv: (-kv[1], str(kv[0])))


def entropy(s):
    c = collections.Counter(s)
    n = len(s)
    return -sum(k / n * math.log2(k / n) for k in c.values())


def ext_of(path):
    base = path.rsplit("/", 1)[-1]
    return os.path.splitext(base)[1].lower()


def md_escape(s):
    return s.replace("|", "\\|")


class LineIndex:
    """Offset -> 1-based line number; the newline table is built on first use only."""

    def __init__(self, text):
        self.nl = None
        self.text = text

    def line_of(self, off):
        if self.nl is None:
            self.nl = [mt.start() for mt in re.finditer("\n", self.text)]
        return bisect.bisect_left(self.nl, off) + 1

    def line_text(self, off):
        a = self.text.rfind("\n", 0, off) + 1
        b = self.text.find("\n", off)
        return self.text[a:b if b >= 0 else len(self.text)]


# ---------------------------------------------------------------- repository model
def snapshot_refs():
    out = git("for-each-ref", "--format=%(refname) %(objectname) %(objecttype)").decode()
    refs = []
    for line in out.splitlines():
        name, sha, typ = line.split()
        refs.append((name, sha, typ))
    head = git("rev-parse", "HEAD").decode().strip()
    return refs, head


def is_ancestor(a, b):
    return sh(["git", "merge-base", "--is-ancestor", a, b], check=False).returncode == 0


def refs_at(refs, commit):
    """The refs as they were at `commit`: a ref whose commit descends from `commit` is replaced by `commit`;
    a ref already an ancestor of it is kept; a ref that is neither cannot be pinned (refuse)."""
    out, notes = [], []
    for name, sha, typ in refs:
        c = git("rev-parse", f"{sha}^{{commit}}").decode().strip()
        if is_ancestor(c, commit):
            out.append((name, sha, typ))
        elif is_ancestor(commit, c):
            out.append((name, commit, "commit"))
            notes.append(f"{name}: {sha[:10]} -> {commit[:10]}")
        else:
            raise SystemExit(f"cannot place {name} ({sha[:10]}) at {commit[:10]}: neither ancestor nor descendant")
    return out, notes


def cat_batch(shas):
    """Yield (sha, type, bytes) for each object id via one git cat-file --batch."""
    p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=ROOT, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)

    def writer():
        for s in shas:
            p.stdin.write(s.encode() + b"\n")
        p.stdin.close()

    t = threading.Thread(target=writer, daemon=True)
    t.start()
    for s in shas:
        header = p.stdout.readline().split()
        if len(header) != 3:
            raise SystemExit(f"cat-file: unexpected header for {s}: {header!r}")
        sha, typ, size = header[0].decode(), header[1].decode(), int(header[2])
        data = p.stdout.read(size)
        p.stdout.read(1)
        yield sha, typ, data
    t.join()
    p.wait()


def build_model(ref_shas, head):
    m = {}
    # commits, oldest first
    commits = git("rev-list", "--reverse", "--topo-order", *ref_shas).decode().split()
    m["commits"] = commits
    m["commit_index"] = {c: i for i, c in enumerate(commits)}
    dates = git("log", "--format=%H %as", *ref_shas).decode().split("\n")
    m["commit_date"] = dict(l.split() for l in dates if l.strip())
    # blob -> [(commit, path)] in history order (raw diffs; root commit included)
    raw = git("log", "--reverse", "--topo-order", "--raw", "--no-abbrev", "--no-renames", "--root",
              "--format=%x01%H", *ref_shas).decode("utf-8", "replace")
    blob_occ = collections.defaultdict(list)
    all_paths_raw = set()
    cur = None
    for line in raw.split("\n"):
        if line.startswith("\x01"):
            cur = line[1:].strip()
        elif line.startswith(":"):
            meta, _, path = line.partition("\t")
            f = meta.split()
            nsha, status = f[3], f[4]
            all_paths_raw.add(path)
            if not status.startswith("D") and set(nsha) != {"0"}:
                blob_occ[nsha].append((cur, path))
    m["blob_occ"] = blob_occ
    m["all_paths_raw"] = all_paths_raw
    # every object reachable from the refs
    objs = git("rev-list", "--objects", *ref_shas).decode("utf-8", "replace").split("\n")
    obj_path = {}
    for line in objs:
        if not line.strip():
            continue
        sha, _, path = line.partition(" ")
        obj_path.setdefault(sha, path)
    shas = list(obj_path)
    chk = git("cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)",
              input=("\n".join(shas) + "\n").encode()).decode().split("\n")
    types, sizes = {}, {}
    for line in chk:
        if line.strip():
            s, t, z = line.split()
            types[s], sizes[s] = t, int(z)
    m["obj_path"], m["types"], m["sizes"] = obj_path, types, sizes
    m["blobs"] = [s for s in shas if types.get(s) == "blob"]
    m["n_trees"] = sum(1 for s in shas if types.get(s) == "tree")
    m["n_commits_objs"] = sum(1 for s in shas if types.get(s) == "commit")
    m["all_paths_objs"] = {p for s, p in obj_path.items() if p and types.get(s) == "blob"}
    # HEAD tree
    tree = git("ls-tree", "-r", "-l", "-z", head).decode("utf-8", "replace").split("\0")
    head_files = {}
    for e in tree:
        if not e:
            continue
        meta, _, path = e.partition("\t")
        mode, typ, sha, size = meta.split()
        head_files[path] = (mode, typ, sha, int(size) if size != "-" else None)
    m["head_files"] = head_files
    m["head_blobs"] = {v[2] for v in head_files.values() if v[1] == "blob"}
    m["head_blob_paths"] = collections.defaultdict(list)
    for p_, v in head_files.items():
        m["head_blob_paths"][v[2]].append(p_)
    return m


def blob_first(m, sha):
    occ = m["blob_occ"].get(sha)
    if occ:
        return occ[0]
    return (None, m["obj_path"].get(sha, ""))


def blob_paths(m, sha):
    ps = sorted({p for _, p in m["blob_occ"].get(sha, [])})
    if not ps and m["obj_path"].get(sha):
        ps = [m["obj_path"][sha]]
    return ps


def is_binary(path_list, data):
    if any(ext_of(p) in BINARY_EXT for p in path_list):
        return True
    return b"\0" in data[:8000]


def iter_sources(m, tag_objs):
    """Yield (kind, sha, path, commit, text) for every text blob, commit message and tag message."""
    for sha, typ, data in cat_batch(m["blobs"]):
        paths = blob_paths(m, sha)
        if is_binary(paths, data):
            continue
        c, p = blob_first(m, sha)
        yield "blob", sha, p, c, data.decode("utf-8", "replace")
    for sha, typ, data in cat_batch(m["commits"]):
        head, _, msg = data.partition(b"\n\n")
        yield "message", sha, "<commit message>", sha, msg.decode("utf-8", "replace")
    for sha, typ, data in cat_batch(tag_objs):
        head, _, msg = data.partition(b"\n\n")
        yield "tagmsg", sha, "<tag message>", sha, msg.decode("utf-8", "replace")


def iter_headers(m, tag_objs):
    """Yield (kind, sha, path, commit, text) for every commit header and tag header (the part before the
    first blank line: tree/parent/author/committer/gpgsig, or object/type/tag/tagger)."""
    for sha, typ, data in cat_batch(m["commits"]):
        yield "header", sha, "<commit header>", sha, data.partition(b"\n\n")[0].decode("utf-8", "replace")
    for sha, typ, data in cat_batch(tag_objs):
        yield "tagheader", sha, "<tag header>", sha, data.partition(b"\n\n")[0].decode("utf-8", "replace")


def loc_str(m, kind, sha, path, commit, line):
    if kind == "blob":
        c = commit[:8] if commit else "?"
        return f"{c} {path}:{line}"
    if kind == "message":
        return f"{commit[:8]} <commit message>:{line}"
    if kind == "header":
        return f"{commit[:8]} <commit header>:{line}"
    if kind == "tagheader":
        return f"tag-object {sha[:8]} <tag header>:{line}"
    return f"tag-object {sha[:8]} <tag message>:{line}"


def has_random_segment(v):
    """True if v has a segment of >= 10 characters mixing letters and digits that is neither hex-only nor
    letters-only (the shape of a generated key or id); labels, words, numbers, hex hashes and UUID parts are not."""
    for s in re.split(r"[/_\-.|+,{}*()\[\]:=]", v):
        if len(s) >= 10 and re.search(r"[A-Za-z]", s) and re.search(r"\d", s) and \
                not re.fullmatch(r"[0-9a-fA-F]+", s):
            return True
    return False


def enclosing_token(text, s, e):
    """The maximal run around [s, e) of characters that are not whitespace, quotes, backticks or brackets."""
    a = s
    while a > 0 and text[a - 1] not in " \t\r\n\"'`<>()[]{}|,;":
        a -= 1
    b = e
    while b < len(text) and text[b] not in " \t\r\n\"'`<>()[]{}|,;":
        b += 1
    return text[a:b]


def triage_cf(v, token, line, in_sig):
    """(verdict, reason, sensitive) for a context-free high-entropy run v inside token on line."""
    if in_sig:
        return ("SSH-SIGNATURE", "a line of the armored SSH signature in a commit's gpgsig header (signature "
                "material, published with the commit by design; not a credential)", True)
    mt = manual(v)
    if mt:
        return mt
    if v.startswith(("iVBORw0KGgo", "/9j/", "R0lGOD", "JVBERi0")) or re.search(r"image/(png|jpeg|gif)|data:image", line):
        return ("FALSE-POSITIVE", "embedded base64 image data (notebook output / data URI)", False)
    if SESSION_LINK_RE.search(token):
        return ("IDENTIFIER", "part of the Claude Code session URL already listed under (ii) (the run is split at "
                "the '.' of claude.ai); not a credential", True)
    if "/.claude/projects/" in token or token.startswith("~/.claude") or "claude/projects/" in v:
        return ("LOCAL-PATH", "part of a ~/.claude/projects/<project>/<session-uuid> path (Claude Code's local "
                "transcript store) quoted in a raw; carries a session UUID; not a credential", True)
    if TEMP_PATH_RE.search(token):
        return ("LOCAL-PATH", "part of a local temporary path ((/private)/tmp or (/private)/var/folders) quoted in "
                "a raw; carries a session UUID or an OS-generated folder name; not a credential", True)
    if has_random_segment(v):
        return ("UNTRIAGED", "a generated-looking segment; needs individual triage", True)
    if "/" in token and len([p for p in token.split("/") if p]) >= 2:
        return ("FALSE-POSITIVE", "a file path or path fragment (slash-separated readable segments; any long "
                "segment is a hex hash or UUID part)", False)
    return ("FALSE-POSITIVE", "a label or identifier made of words, numbers and short tokens (no generated-looking "
            "segment)", False)


def order_key(m, kind, commit):
    if commit and commit in m["commit_index"]:
        return m["commit_index"][commit]
    return 10 ** 9


# ---------------------------------------------------------------- (i-a) fallback
def run_fallback(ref_shas=None):
    p1 = sh(["git", "log", "-p", *(ref_shas if ref_shas else ["--all"])])
    logp = p1.stdout
    p2 = sh(["/usr/bin/grep", "-nEi", FALLBACK_PATTERN], input=logp, check=False)
    return logp, p2


def index_log(logp_lines):
    """Map each line of `git log -p --all` output to (commit, path, side, lineno)."""
    loc = [None] * len(logp_lines)
    commit = None
    path = None
    msg_ln = 0
    in_msg = False
    in_hunk = False
    old_ln = new_ln = old_rem = new_rem = 0
    hunk_re = re.compile(rb"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
    for i, line in enumerate(logp_lines):
        if in_hunk and (old_rem > 0 or new_rem > 0):
            if line.startswith(b"+"):
                loc[i] = (commit, path, "+", new_ln); new_ln += 1; new_rem -= 1
            elif line.startswith(b"-"):
                loc[i] = (commit, path, "-", old_ln); old_ln += 1; old_rem -= 1
            elif line.startswith(b" ") or line == b"":
                loc[i] = (commit, path, " ", new_ln); new_ln += 1; old_ln += 1
                new_rem -= 1; old_rem -= 1
            elif line.startswith(b"\\"):
                loc[i] = (commit, path, "\\", None)
            continue
        if line.startswith(b"\\"):
            loc[i] = (commit, path, "\\", None)
            continue
        in_hunk = False
        if re.match(rb"^commit [0-9a-f]{40}", line):
            commit = line.split()[1].decode()
            path = None; msg_ln = 0; in_msg = True
            loc[i] = (commit, "<commit header>", "h", None)
            continue
        if line.startswith(b"diff --git "):
            in_msg = False
            mm = re.match(rb"^diff --git a/(.*) b/(.*)$", line)
            path = mm.group(2).decode("utf-8", "replace") if mm else line.decode("utf-8", "replace")
            loc[i] = (commit, path, "h", None)
            continue
        h = hunk_re.match(line)
        if h and path is not None:
            old_ln = int(h.group(1)); old_rem = int(h.group(2) or 1)
            new_ln = int(h.group(3)); new_rem = int(h.group(4) or 1)
            in_hunk = True
            loc[i] = (commit, path, "@", None)
            continue
        if in_msg and line.startswith(b"    "):
            msg_ln += 1
            loc[i] = (commit, "<commit message>", "m", msg_ln)
            continue
        loc[i] = (commit, path or "<commit header>", "h", None)
    return loc


def fallback_word(t, start, end):
    a = start
    while a > 0 and (t[a - 1].isalnum() or t[a - 1] in "_-"):
        a -= 1
    b = end
    while b < len(t) and (t[b].isalnum() or t[b] in "_-"):
        b += 1
    return t[a:b]


SHAPE_RE = re.compile(r"(?i)\b([\w\-]*(?:api[_-]?key|secret|token|password)[\w\-]*)[\"']?\s*(=>|=|:)"
                      r"\s*([\"']?)([^\s\"',;)\]}]+)")


def classify_value(v, quoted=False):
    """Mechanical value classes for credential-shaped hits; None = needs individual triage."""
    if re.fullmatch(r"[-+]?\d+(\.\d+)?([eE][-+]?\d+)?%?[`.]?", v):
        return "number", "numeric value (a count, size or rate), not a credential"
    if v.rstrip("`.") in {"True", "False", "None", "null", "true", "false", "none"}:
        return "bool/null", "boolean/null literal"
    if v[0] in "[{(<=":
        return "structure", "opens a list/dict/tuple/expression; no literal string follows"
    if "(" in v or v.endswith(")") or "[" in v or "]" in v:
        return "code-expression", "a function call / subscript / type annotation in source code"
    if re.fullmatch(r"[A-Z][A-Z0-9_]*=\d+", v):
        return "code-expression", "a chained constant assignment (NAME=number) in source/prose"
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)+", v):
        return "code-reference", "a dotted Python attribute/module reference"
    if re.fullmatch(r"[a-z][a-z0-9]*(_[a-z0-9]+)+", v) or re.fullmatch(r"[A-Z][A-Z0-9]*(_[A-Z0-9]+)+", v):
        return "identifier", "a snake_case / UPPER_CASE program identifier (variable or constant name)"
    if re.fullmatch(r"[A-Za-z][a-z]{0,14}[.`:']?", v) or re.fullmatch(r"[A-Z][A-Za-z]{0,14}", v):
        return "word", "a single prose word / short name after a colon or equals sign"
    if re.fullmatch(r"(mlx-community|allenai|Qwen|meta-llama)/[\w.\-]+", v):
        return "public-model-id", "a public Hugging Face model repository id"
    if re.fullmatch(r"[A-Za-z]\d{1,3}", v) or re.fullmatch(r"m:\d+", v):
        return "label", "a layer/line label (e.g. L49, m:261)"
    if re.fullmatch(r"[A-Za-z]+-[A-Za-z0-9]+", v) and len(v) <= 24:
        return "word", "a hyphenated prose word / label"
    return None, None


CRED_TOKEN_WORD_RE = re.compile(r"(?i)^(?:hf|hugging_?face(?:_hub)?|github|gh|access|auth|api|bearer|refresh|"
                                r"id|secret|private|personal|oauth|runpod|wandb|npm|pypi)[_\-]?token$")


def fallback_bulk_rule(alt, word, path, after=""):
    w = word.lower()
    if alt == "token":
        if CRED_TOKEN_WORD_RE.match(word):
            if re.match(r"[\"']?\s*(=>|=|:)", after):
                return ("T3 credential-sense word followed by a value", "needs individual inspection")
            return ("T2 credential-sense word, no value follows", "a credential's name (e.g. HF_TOKEN) in prose or "
                    "a library warning, with no '=', ':' or '=>' and no value after it; names a credential, "
                    "discloses none")
        return ("T1 LLM-token sense", "token/tokens/tokenizer/token_ids/... -- the language-model "
                "vocabulary sense, in prose, code identifiers or JSON field names")
    if alt == "secret":
        if path.startswith("data/") or path.endswith(".jsonl"):
            return ("S1 prose in model-generated text", "'secret(s)/secretly' as an English word in "
                    "recorded model outputs (session transcripts / detection trials)")
        return ("S2 prose in documents", "'secret(s)/secretly' as an English word in design/log/raw "
                "documents (incl. the audit block discussing the scrub)")
    if alt == "password":
        if path.startswith("data/"):
            return ("P2 model-generated text", "'password' inside a recorded model output (degenerate "
                    "generation text)")
        if path in (BLOCK, "results/raw/2026-10-08_note-preflight.md", "<commit message>"):
            return ("P1 the audit block, its preflight raw, and that commit's message",
                    "the block's N12(i) pattern and N12(iii) text about the continuity password, quoted or "
                    "discussed; no password value appears on these lines")
        return ("P3 other prose", "needs individual inspection")
    if alt == "sk-[A-Za-z0-9]":
        if re.search(r"[A-Za-z]sk-", word):
            return ("K1 in-word 'sk-' (task-/mask-/...)", "the 'sk-' is the tail of a word such as "
                    "task-round or mask-off, preceded by a letter; not a key prefix")
        return ("K2 word-initial 'sk-'", "needs individual inspection")
    if alt == "rp_[A-Za-z0-9]":
        return ("R1 code identifier", "a Python variable name containing 'rp_' (rp_ck, rp_bytes) in a "
                "self-test")
    return ("X unclassified", "needs individual inspection")


# ---------------------------------------------------------------- triage of precise / HE hits
def manual(value):
    """Explicit triage -> (verdict, reason, sensitive): a TRIAGE16 entry (round 5: the first 16 hex of sha256) first,
    then a MANUAL_TRIAGE entry (the first 8 hex)."""
    h_ = sha256_hex(value.encode())
    e = TRIAGE16.get(h_[:16])
    if e is not None:
        return (e[0], e[1], e[2])
    e = MANUAL_TRIAGE.get(h_[:8])
    if e is None:
        return None
    return (e[0], e[1], e[2] if len(e) > 2 else True)


def shape_manual(path, key, value):
    """Round 5: SHAPE_TRIAGE16 entry for a credential-shaped fallback row -> (verdict, reason), or None."""
    return SHAPE_TRIAGE16.get((path, key.lower(), sha256_hex(value.encode())[:16]))


def triage_precise(name, value, line, path):
    """(verdict, reason, sensitive). sensitive=False only for mechanical code/path classes."""
    mt = manual(value)
    if mt:
        return mt
    if name == "generic_assignment":
        cls, why = classify_value(value)
        if cls in ("code-expression", "code-reference", "identifier", "public-model-id", "number"):
            return ("FALSE-POSITIVE", f"{cls}: {why}", False)
        if re.fullmatch(r"[\w.\-]+(/[\w.\-]+)+", value) and re.search(r"[a-z]{3,}", value):
            return ("FALSE-POSITIVE", "a file path / repository-relative path, not a credential", False)
    if name in ("quoted_secretish_assignment", "url_secret_query_param"):
        cls, why = classify_value(value)
        if cls in ("code-expression", "code-reference", "identifier", "public-model-id", "number"):
            return ("FALSE-POSITIVE", f"{cls}: {why}", False)
        # round 2 (pre-release scan of pending files): two more mechanical classes
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?)?", value):
            return ("FALSE-POSITIVE", "an ISO-8601 date or timestamp (e.g. a commit's author time)", False)
        if "(?" in value or re.search(r"\[[^\]]*[A-Za-z0-9]-[A-Za-z0-9][^\]]*\]\{?\d*", value):
            return ("FALSE-POSITIVE", "a regular-expression pattern (a scanner's own pattern definition)", False)
        # round 3 (Code, at the new HEAD): a sha1/sha256-length hex digest under a key that names it as a hash
        # (e.g. key_set_sha256) -- before the label rule, whose reason ('words and short tokens') does not fit it
        # round 4 (Code's addition): not under a key that also names a password, secret or credential (the hash of a
        # secret is derived from it)
        if re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", value):
            km = re.search(r"([\w\-]+)['\"]?\s*[:=]\s*['\"]" + re.escape(value), line or "")
            if km and re.search(r"(?i)sha|hash|digest", km.group(1)) and \
                    not re.search(r"(?i)passw|pwd|secret|credential", km.group(1)):
                return ("FALSE-POSITIVE", f"a hex digest ({len(value) * 4}-bit, sha1/sha256 length) under a key "
                        f"naming it as a hash (`{km.group(1)}`); a content hash, not a credential", False)
        # round 4 (fourth checker, finding 3): has_random_segment exempts hex-only segments, so the label rule below
        # would clear any hex-only value holding a run of 3 letters a-f, whatever its key. A hex-only value that the
        # digest rule above did not clear stays UNTRIAGED, and the label rule needs a letter outside a-f.
        if re.fullmatch(r"[0-9a-fA-F]+", value):
            return ("UNTRIAGED", "a hex-only value that the hex-digest rule does not clear (it clears only 40 or 64 "
                    "hex under a key, on the same line, that names a hash and no password, secret or credential); "
                    "the label rule never clears hex; needs individual triage (STOP until triaged)", True)
        if not has_random_segment(value) and \
                any(re.search(r"[g-zG-Z]", r_) for r_ in re.findall(r"[A-Za-z]{3,}", value)):
            return ("FALSE-POSITIVE", "a label built of words and short tokens (a check name, a schedule-key "
                    "template, an axis name); the key word is part of a field name such as key / key_template / "
                    "axis_key; no generated-looking segment", False)
    return ("UNTRIAGED", "no mechanical rule clears it; needs individual triage (STOP until triaged)", True)


def triage_he(value, line, key):
    mt = manual(value)
    if mt:
        return mt
    if value.startswith(("iVBORw0KGgo", "/9j/", "R0lGOD", "JVBERi0")) or re.search(
            r"image/(png|jpeg|gif)|data:image", line):
        return ("FALSE-POSITIVE", "embedded base64 image data (notebook output / data URI)", False)
    if TEMP_PATH_RE.match(value):
        return ("LOCAL-PATH", "a local temporary path ((/private)/tmp or (/private)/var/folders) in a recorded "
                "message; carries an OS-generated folder name or a session UUID; not a credential", True)
    segs = [s for s in re.split(r"[/_\-.]", value) if s]
    if "/" in value and all(re.fullmatch(r"[A-Za-z0-9]{1,24}", s) for s in segs) and \
            sum(1 for s in segs if re.fullmatch(r"[a-z]{3,}|[A-Z][a-z]{2,}", s)) >= 2:
        return ("FALSE-POSITIVE", "a file path (separator-delimited readable words)", False)
    wordlike = sum(1 for s in segs if re.fullmatch(r"[a-z]{2,}|[A-Z][a-z]+|[A-Z]{2,}|\d{1,6}|v\d+", s))
    if len(segs) >= 3 and wordlike >= len(segs) - 1:
        return ("FALSE-POSITIVE", "a snake/kebab-case identifier or label built of readable words", False)
    return ("UNTRIAGED", "no mechanical rule clears it; needs individual triage", True)


# ---------------------------------------------------------------- main scan
def is_new_source(m, kind, sha):
    """True if the source is not reachable from the --since base (blob not in the base's objects; message or
    header of a commit not in the base's commits)."""
    if m.get("base_objs") is None:
        return False
    if kind == "blob":
        return sha not in m["base_objs"]
    return sha not in m["base_objs"]


def cf_scan(text, kind, sha, path, commit, li, table, add_fn, sig_spans=(), b64stats=None):
    """Context-free high-entropy scan of one source into table (via add_fn). b64stats (round 2): distinct
    mixed-case runs of 64+ characters and those at or below the 4.3 bar (the bar's blind spot is structured
    base64 such as wire-format key or signature material)."""
    if b64stats is not None:
        for mt in B64_STRICT_RE.finditer(text):
            v = mt.group(0)
            if re.search(r"[a-z]", v) and re.search(r"[A-Z]", v) and re.search(r"\d", v):
                b64stats["runs64"].add(vkey(v))
                H = entropy(v)
                if H <= 4.3 and vkey(v) not in b64stats["runs64_below"]:
                    b64stats["runs64_below"][vkey(v)] = {
                        "value": v, "length": len(v), "entropy": round(H, 3),
                        "first": f"{(commit or sha or '?')[:8]} {path}:{li.line_of(mt.start())}",
                        "line": li.line_text(mt.start())[:300]}
    for rx_, which in ((CF_MIXED_RE, "mixed"), (CF_LOWER_RE, "lower")):
        for mt in rx_.finditer(text):
            v = mt.group(0)
            if which == "mixed":
                if not (re.search(r"[a-z]", v) and re.search(r"[A-Z]", v) and re.search(r"\d", v)):
                    continue
                if entropy(v) <= 4.3:
                    continue
            else:
                if sum(ch.isdigit() for ch in v) < 3 or sum(ch.isalpha() for ch in v) < 3 or \
                        re.fullmatch(r"[0-9a-f]+", v) or entropy(v) <= 3.5:
                    continue
            in_sig = any(a <= mt.start() < b for a, b in sig_spans)
            line = li.line_text(mt.start())
            token = enclosing_token(text, mt.start(), mt.end())
            e = add_fn(table, v, kind, sha, path, commit, li, mt.start(),
                       extra={"entropy": round(entropy(v), 3), "run": which})
            if "triage" not in e:
                e["triage"] = triage_cf(v, token, line, in_sig)


def scan_history(m, tag_objs):
    precise = collections.OrderedDict((n, {}) for n, _, _ in PRECISE)
    he = {}
    cf = {}
    he_stats = collections.Counter()
    ids = collections.OrderedDict((n, {}) for n in ID_PATTERNS)
    users_at_head = {}
    workspace_at_head = {}
    text_blobs = 0
    text_bytes = 0
    n_messages = 0
    binary = []
    # binary inventory (and npz member names) first, from the blob stream
    for sha, typ, data in cat_batch(m["blobs"]):
        paths = blob_paths(m, sha)
        if is_binary(paths, data):
            members = None
            if any(ext_of(p) == ".npz" for p in paths):
                try:
                    with zipfile.ZipFile(io.BytesIO(data)) as z:
                        members = z.namelist()
                except zipfile.BadZipFile:
                    members = ["<not a zip>"]
            c, p = blob_first(m, sha)
            binary.append({"blob": sha, "size": len(data), "paths": paths, "first_commit": c,
                           "at_head": sha in m["head_blobs"], "npz_members": members})
    head_text = {}

    def add(table, key, kind, sha, path, commit, li, off, extra=None):
        e = table.get(key)
        at_head = kind == "blob" and sha in m["head_blobs"]
        o = order_key(m, kind, commit)
        if e is None:
            e = table[key] = {"n_occ": 0, "n_occ_head": 0, "sources": set(), "first": None,
                              "first_order": None, "extra": extra, "head_paths": set(),
                              "paths": set(), "messages": 0, "n_occ_new": 0}
        e["n_occ"] += 1
        if is_new_source(m, kind, sha):
            e["n_occ_new"] += 1
        if kind == "blob" and sha in (m.get("base_head_blobs") or ()):
            e["n_occ_base_head"] = e.get("n_occ_base_head", 0) + 1
            e.setdefault("base_head_paths", set()).update(m["base_head_blob_paths"][sha])
        e["sources"].add((kind, sha))
        e["paths"].add(path)
        if kind != "blob":
            e["messages"] += 1
        if at_head:
            e["n_occ_head"] += 1
            for hp in m["head_blob_paths"].get(sha, []):
                e["head_paths"].add(hp)
        if e["first_order"] is None or o < e["first_order"]:
            e["first_order"] = o
            e["first"] = loc_str(m, kind, sha, path, commit, li.line_of(off))
            e["_ctx"] = li.line_text(off)[:400]  # in memory only (for --dump-untriaged); never serialized
        return e

    sweep = {}
    b64stats = {"runs64": set(), "runs64_below": {}}
    for kind, sha, path, commit, text in iter_sources(m, tag_objs):
        if kind == "blob":
            text_blobs += 1
            text_bytes += len(text.encode("utf-8", "replace"))
        else:
            n_messages += 1
        li = LineIndex(text)
        # context-free sweep for RunPod-id-shaped tokens (10 chars = volume shape, 14 = pod shape)
        for mt in SWEEP_RE.finditer(text):
            v = mt.group(1)
            if sum(ch.isdigit() for ch in v) >= 2 and sum(ch.isalpha() for ch in v) >= 3 and \
                    not re.fullmatch(r"[0-9a-f]+", v):
                add(sweep, v, kind, sha, path, commit, li, mt.start(1))
        if kind == "blob" and sha in m["head_blobs"]:
            for hp in m["head_blob_paths"][sha]:
                cu, cw = text.count("/Users/"), text.count("/workspace/")
                if cu:
                    users_at_head[hp] = cu
                if cw:
                    workspace_at_head[hp] = cw
        # precise patterns
        for name, rx, grp in PRECISE:
            for mt in rx.finditer(text):
                v = mt.group(grp) if grp else mt.group(0)
                line = li.line_text(mt.start())
                e = add(precise[name], v, kind, sha, path, commit, li, mt.start())
                if "triage" not in e:
                    e["triage"] = triage_precise(name, v, line, path)
        # high entropy in assignment/header context
        for mt in HE_RUN_RE.finditer(text):
            key = he_context(text, mt.start())
            if key is None:
                continue
            v = mt.group(0)
            alpha = "hex" if re.fullmatch(r"[0-9a-fA-F]+", v) else "base64"
            he_stats[f"candidates_{alpha}"] += 1
            H = entropy(v)
            if H <= 4.0:
                continue
            he_stats[f"over4_{alpha}"] += 1
            line = li.line_text(mt.start())
            e = add(he, v, kind, sha, path, commit, li, mt.start(), extra={"entropy": round(H, 3),
                                                               "alphabet": alpha, "key": key})
            if "triage" not in e:
                e["triage"] = triage_he(v, line, key)
        # context-free high entropy (no assignment context)
        cf_scan(text, kind, sha, path, commit, li, cf, add, b64stats=b64stats)
        # identifiers
        for name, rx in ID_RE.items():
            if name in ANCHORED:
                for off, v in ANCHORED[name](text):
                    add(ids[name], v, kind, sha, path, commit, li, off)
                continue
            if rx is None:
                continue
            for mt in rx.finditer(text):
                gd = mt.groupdict()
                gname = next((g for g in ("v", "v2", "v3", "v4") if gd.get(g)), None)
                if gname is None:
                    continue
                v = gd[gname]
                if name in ("runpod_pod_id (context: pod)", "runpod_volume_id (context: volume)",
                            "runpod_endpoint_or_template_id (context)"):
                    if not (re.search(r"\d", v) and len(re.findall(r"[a-z]", v)) >= 2):
                        continue
                add(ids[name], v, kind, sha, path, commit, li, mt.start(gname))
        # ssh ports: numbers on ssh/port/alias lines
        seen_lines = set()
        for sm in SSH_LINE_RE.finditer(text):
            a = text.rfind("\n", 0, sm.start()) + 1
            if a in seen_lines:
                continue
            seen_lines.add(a)
            b = text.find("\n", sm.start())
            line = text[a:b if b >= 0 else len(text)]
            if code_port_only(line, "history"):
                continue
            for pm in PORT_NUM_RE.finditer(line):
                v = pm.group("v")
                if re.fullmatch(r"(19|20)\d\d", v):
                    continue
                add(ids["ssh_port (number in an ssh/port/alias line)"], v, kind, sha, path, commit,
                    li, a + pm.start())

    # ---- commit and tag headers (their own tables)
    hdr = {"precise": collections.OrderedDict((n, {}) for n, _, _ in PRECISE), "cf": {},
           "ids": collections.OrderedDict((n, {}) for n in ID_PATTERNS), "keys": collections.Counter(),
           "sigs": [], "n_commit_headers": 0, "n_tag_headers": 0, "taggers": collections.Counter(),
           "identity_occ": collections.Counter(), "tagger_tags": collections.defaultdict(list),
           "armor_lines": {}}
    for kind, sha, path, commit, text in iter_headers(m, tag_objs):
        hdr["n_commit_headers" if kind == "header" else "n_tag_headers"] += 1
        li = LineIndex(text)
        sig_spans = []
        for mt in re.finditer(r"(?m)^(\S+) ", text):
            hdr["keys"][("commit " if kind == "header" else "tag ") + mt.group(1)] += 1
        this_sigs = []
        for mt in re.finditer(r"(?ms)^gpgsig (.*?)(?=^\S|\Z)", text):
            sig_spans.append((mt.start(), mt.end()))
            psig = parse_signature(mt.group(1))
            hdr["sigs"].append((sha, psig))
            this_sigs.append((mt.start(), mt.end(), psig))
            # round 2: entropy of every armor body line (the 4.3 bar's sensitivity on structured base64)
            for al in mt.group(1).split("\n"):
                al = al.strip()
                if len(al) >= 16 and not al.startswith("-----"):
                    hdr["armor_lines"][vkey(al)] = (len(al), round(entropy(al), 3),
                                                    bool(re.search(r"[a-z]", al) and re.search(r"[A-Z]", al)
                                                         and re.search(r"\d", al)))
        for mt in re.finditer(r"(?m)^(?:author|committer|tagger) .*?<([^>]*)>", text):
            hdr["identity_occ"][mt.group(1)] += 1
        if kind == "tagheader":
            tg = re.search(r"(?m)^tagger (.*?) <([^>]*)>", text)
            tn = re.search(r"(?m)^tag (\S+)", text)
            if tg:
                hdr["taggers"][(tg.group(1), tg.group(2))] += 1
                hdr["tagger_tags"][(tg.group(1), tg.group(2))].append(tn.group(1) if tn else sha[:10])
        for name, rx, grp in PRECISE:
            for mt in rx.finditer(text):
                v = mt.group(grp) if grp else mt.group(0)
                e = add(hdr["precise"][name], v, kind, sha, path, commit, li, mt.start())
                if "triage" not in e:
                    in_sig = [ps_ for a, b, ps_ in this_sigs if a <= mt.start() < b]
                    if name in KEY_MATERIAL_PATTERNS and in_sig:
                        e["triage"] = ("SSH-SIGNATURE", sig_marker_reason(in_sig[0]), True)
                    else:
                        e["triage"] = triage_precise(name, v, li.line_text(mt.start()), path)
        cf_scan(text, kind, sha, path, commit, li, hdr["cf"], add, sig_spans)
        for name, rx in ID_RE.items():
            if name in ANCHORED:
                for off, v in ANCHORED[name](text):
                    add(hdr["ids"][name], v, kind, sha, path, commit, li, off)
                continue
            if rx is None:
                continue
            for mt in rx.finditer(text):
                gd = mt.groupdict()
                gname = next((g for g in ("v", "v2", "v3", "v4") if gd.get(g)), None)
                if gname:
                    add(hdr["ids"][name], gd[gname], kind, sha, path, commit, li, mt.start(gname))

    # ---- binary blobs: string content of every npz member and PNG text chunk
    binc = {"precise": collections.OrderedDict((n, {}) for n, _, _ in PRECISE), "cf": {},
            "ids": collections.OrderedDict((n, {}) for n in ID_PATTERNS), "members": 0,
            "dtypes": collections.Counter(), "unicode_members": 0, "ascii_runs": 0, "png_chunks": collections.Counter(),
            "png_text_keys": [], "other_binary": 0, "chars_scanned": 0}
    for sha, typ, data in cat_batch([b["blob"] for b in binary]):
        paths = blob_paths(m, sha)
        c, p = blob_first(m, sha)
        for label, text in binary_strings(data, binc):
            binc["chars_scanned"] += len(text)
            li = LineIndex(text)
            ppath = f"{p}::{label}"
            for name, rx, grp in PRECISE:
                for mt in rx.finditer(text):
                    v = mt.group(grp) if grp else mt.group(0)
                    e = add(binc["precise"][name], v, "blob", sha, ppath, c, li, mt.start())
                    if "triage" not in e:
                        e["triage"] = triage_precise(name, v, li.line_text(mt.start()), ppath)
            cf_scan(text, "blob", sha, ppath, c, li, binc["cf"], add)
            for name, rx in ID_RE.items():
                if name in ANCHORED:
                    for off, v in ANCHORED[name](text):
                        add(binc["ids"][name], v, "blob", sha, ppath, c, li, off)
                    continue
                if rx is None:
                    continue
                for mt in rx.finditer(text):
                    gd = mt.groupdict()
                    gname = next((g for g in ("v", "v2", "v3", "v4") if gd.get(g)), None)
                    if gname:
                        add(binc["ids"][name], gd[gname], "blob", sha, ppath, c, li, mt.start(gname))

    stats = {"text_blobs": text_blobs, "text_bytes": text_bytes, "messages_and_tags": n_messages,
             "binary_blobs": len(binary)}
    hdr["b64stats"] = b64stats
    return precise, he, he_stats, ids, users_at_head, workspace_at_head, binary, stats, sweep, cf, hdr, binc


def parse_signature(block):
    """Decode a gpgsig header value. SSH signatures (SSHSIG) -> key type, namespace, hash, fingerprint."""
    lines = [l[1:] if l.startswith(" ") else l for l in block.split("\n")]
    lines = [l for l in lines if l.strip()]
    out = {"armor": lines[0].strip() if lines else ""}
    if "BEGIN SSH SIGNATURE" in out["armor"]:
        body = "".join(l.strip() for l in lines[1:] if not l.strip().startswith("-----"))
        raw = base64.b64decode(body)
        out["magic_ok"] = raw[:6] == b"SSHSIG"
        off = 10  # magic (6) + version (4)

        def rd(o):
            n = struct.unpack(">I", raw[o:o + 4])[0]
            return raw[o + 4:o + 4 + n], o + 4 + n
        spans = {}
        a_ = off + 4
        pk, off = rd(off)
        spans["public-key"] = (a_, off)
        a_ = off + 4
        ns, off = rd(off)
        spans["namespace"] = (a_, off)
        a_ = off + 4
        _, off = rd(off)
        spans["reserved"] = (a_, off)
        a_ = off + 4
        halg, off = rd(off)
        spans["hash-algorithm"] = (a_, off)
        a_ = off + 4
        _, off = rd(off)
        spans["signature"] = (a_, off)
        kt = struct.unpack(">I", pk[:4])[0]
        ktype = pk[4:4 + kt]
        # round 3 (third checker, finding 3): every occurrence of the wire-format key-type string
        # (uint32 length + name) in the raw signature, with the field it sits in and its offset mod 3. Only an
        # occurrence at a multiple of 3 encodes to the base64 marker that ssh_key_material_base64 matches.
        kts = re.escape(struct.pack(">I", len(ktype)) + ktype)
        out["keytype_strings"] = [(mo.start(), mo.start() % 3,
                                   next((f for f, (s0, s1) in spans.items() if s0 <= mo.start() < s1), "?"))
                                  for mo in re.finditer(kts, raw)]
        out["raw_len"] = len(raw)
        body_lines = [l.strip() for l in lines[1:] if l.strip() and not l.strip().startswith("-----")]
        out["body_lines_sha8"] = [vkey(l) for l in body_lines]
        out["marker_body_lines"] = [i + 1 for i, l in enumerate(body_lines) if any(mk in l for mk in SSH_B64_MARKERS)]
        out.update({"key_type": ktype.decode(), "namespace": ns.decode(), "hash": halg.decode(),
                    "fingerprint": "SHA256:" + base64.b64encode(hashlib.sha256(pk).digest()).decode().rstrip("="),
                    "version": struct.unpack(">I", raw[6:10])[0]})
    return out


def sig_marker_reason(sig):
    """SSH-SIGNATURE triage reason for a key-material marker inside a gpgsig header, from the signature's own
    byte layout (round 3: the marker is the key-type string that opens the signature field, not the public key)."""
    kts = sig.get("keytype_strings") or []
    aligned = [(o, f) for o, r3, f in kts if r3 == 0]
    unaligned = [(o, f) for o, r3, f in kts if r3 != 0]
    if not aligned:
        return ("base64 inside a commit's gpgsig header (signature material, published with the commit by design; "
                "not a credential); the marker's byte position was not determined")
    return (f"base64 inside a commit's gpgsig header: the marker is the key-type string (string "
            f"\"{sig.get('key_type')}\") that opens the SSHSIG blob's "
            + " and ".join(f"{f} field (byte {o}, a multiple of 3, so it encodes to the marker)" for o, f in aligned)
            + (", followed there by the signature bytes" if any(f == "signature" for _, f in aligned) else "")
            + ("; the " + " and ".join(f"{f} field's own key-type string (byte {o}) is not 3-aligned and does not "
                                       "encode to it" for o, f in unaligned) if unaligned else "")
            + "; signature material, published with the commit by design; not a credential")


def binary_strings(data, binc):
    """Yield (label, text) string content of a binary blob: for a .npz, each member's unicode payload
    (decoded UTF-32LE) and its printable-ASCII runs of >= 8; for a PNG, its tEXt/iTXt/zTXt chunks."""
    if data[:4] == b"PK\x03\x04":
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for nm in z.namelist():
                raw = z.read(nm)
                binc["members"] += 1
                dt = "?"
                body = raw
                if raw[:6] == b"\x93NUMPY":
                    major = raw[6]
                    hl, ho = ((struct.unpack("<H", raw[8:10])[0], 10) if major == 1
                              else (struct.unpack("<I", raw[8:12])[0], 12))
                    header = raw[ho:ho + hl].decode("latin-1")
                    mm = re.search(r"'descr':\s*'([^']+)'", header)
                    dt = mm.group(1) if mm else "?"
                    body = raw[ho + hl:]
                    yield f"{nm}[header]", header
                binc["dtypes"][dt] += 1
                if dt.lstrip("<>|=").startswith("U"):
                    binc["unicode_members"] += 1
                    yield f"{nm}[unicode]", body.decode("utf-32-le", "replace").replace("\x00", "\n")
                runs = [x.group(0).decode() for x in re.finditer(rb"[\x20-\x7e]{8,}", body)]
                binc["ascii_runs"] += len(runs)
                if runs:
                    yield f"{nm}[ascii-runs]", "\n".join(runs)
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        i = 8
        chunks = []
        while i + 8 <= len(data):
            ln, ty = struct.unpack(">I4s", data[i:i + 8])
            body = data[i + 8:i + 8 + ln]
            binc["png_chunks"][ty.decode("latin-1")] += 1
            if ty in (b"tEXt", b"iTXt"):
                chunks.append(body.decode("latin-1"))
            elif ty == b"zTXt":
                k, _, rest = body.partition(b"\0")
                chunks.append(k.decode("latin-1") + "\0" + zlib.decompress(rest[1:]).decode("latin-1"))
            i += 12 + ln
        binc["png_text_keys"].extend(ch.split("\0")[0] for ch in chunks)
        if chunks:
            yield "png-text-chunks", "\n".join(ch.replace("\0", ": ") for ch in chunks)
    else:
        binc["other_binary"] += 1
        runs = [x.group(0).decode() for x in re.finditer(rb"[\x20-\x7e]{8,}", data)]
        if runs:
            yield "ascii-runs", "\n".join(runs)


def recount_exact(m, tag_objs, ids):
    """Pass 2: count every occurrence of each context-discovered id value anywhere in history.
    SSH ports: only values whose individual triage is IDENTIFIER (a real port) are re-counted -- other 4-5
    digit numbers recur as unrelated data. The word boundary (no letter or digit on either side) keeps a
    number inside a hex hash or a longer number from counting."""
    values = {}
    for cls in exact_recount_classes():
        for v in ids[cls]:
            if cls.startswith("ssh_port") and (manual(v) or ("",))[0] != "IDENTIFIER":
                continue
            values.setdefault(v, set()).add(cls)
    if not values:
        return {}
    rx = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(v) for v in
                                                     sorted(values, key=len, reverse=True)) + r")(?![A-Za-z0-9])")
    res = {v: {"n_occ": 0, "n_occ_head": 0, "sources": set(), "first": None, "first_order": None,
               "head_paths": set(), "messages": 0, "head_locators": [], "n_occ_new": 0,
               "n_occ_base_head": 0, "base_head_locators": [], "classes": sorted(values[v])} for v in values}
    base_head_blobs = m.get("base_head_blobs") or set()
    for kind, sha, path, commit, text in iter_sources(m, tag_objs):
        hits = list(rx.finditer(text))
        if not hits:
            continue
        li = LineIndex(text)
        for mt in hits:
            v = mt.group(1)
            e = res[v]
            e["n_occ"] += 1
            e["sources"].add((kind, sha))
            e.setdefault("by_source", collections.Counter())[(kind, sha)] += 1   # round 3: counts at any snapshot
            if is_new_source(m, kind, sha):
                e["n_occ_new"] += 1
                e.setdefault("sources_new", set()).add((kind, sha))
            if kind != "blob":
                e["messages"] += 1
            if kind == "blob" and sha in m["head_blobs"]:
                e["n_occ_head"] += 1
                e["head_paths"].update(m["head_blob_paths"][sha])
                for hp in m["head_blob_paths"][sha]:
                    e["head_locators"].append(f"{hp}:{li.line_of(mt.start())}")
            if kind == "blob" and sha in base_head_blobs:
                e["n_occ_base_head"] += 1
                for bp in m["base_head_blob_paths"][sha]:
                    e["base_head_locators"].append(f"{bp}:{li.line_of(mt.start())}")
            o = order_key(m, kind, commit)
            if e["first_order"] is None or o < e["first_order"]:
                e["first_order"] = o
                e["first"] = loc_str(m, kind, sha, path, commit, li.line_of(mt.start()))
    return res


# ---------------------------------------------------------------- identifier triage
def ip_class(v):
    o = [int(x) for x in v.split(".")]
    if o[0] == 127:
        return "loopback (127/8)"
    if o == [0, 0, 0, 0]:
        return "unspecified (0.0.0.0)"
    if o[0] == 10 or (o[0] == 172 and 16 <= o[1] <= 31) or (o[0] == 192 and o[1] == 168):
        return "private (RFC 1918)"
    if o[0] == 100 and 64 <= o[1] <= 127:
        return "CGNAT (100.64/10)"
    if o[0] == 169 and o[1] == 254:
        return "link-local"
    return "public-shaped"


def triage_identifier(cls, v, e):
    mt = manual(v)
    if mt:
        return mt
    if cls == "ipv4_address" or (cls == "url_host" and re.fullmatch(r"[\d.]+", v)):
        if re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}", v):
            c = ip_class(v)
            if c.startswith("loopback") or c.startswith("unspecified"):
                return ("FALSE-POSITIVE", f"{c}: a local-only address, identifies no machine", True)
            return ("UNTRIAGED", f"{c}; needs individual triage", True)
    if cls.startswith("local_temp_path"):
        if re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-|/var/folders/|/tmp/claude-\d+/", v):
            return ("LOCAL-PATH", "a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the "
                    "macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it "
                    "carries a session UUID or an OS-generated folder name", True)
        return ("LOCAL-PATH", "a fixed temporary file or directory name under /tmp (a box script's log/scratch "
                "file, or one quoted in a raw); carries no session identifier; not a credential", True)
    if cls.startswith("claude_projects_path"):
        return ("LOCAL-PATH", "a path into ~/.claude/projects/ (Claude Code's local transcript store: a project "
                "directory named after the repository path, and session UUIDs) quoted in a document or raw; not a "
                "credential; nothing reads it", True)
    if cls == "url_host":
        if v.lower() in PUBLIC_HOSTS or v.lower().endswith((".github.io", ".wikipedia.org")):
            return ("PUBLIC", "a public website host", False)
        return ("UNTRIAGED", "host not on the public-site list; needs individual triage", True)
    return ("UNTRIAGED", "needs individual triage", True)


# ---------------------------------------------------------------- (v) and (iv)
def size_section(m, binary, refs):
    largest = sorted(((m["sizes"][s], s) for s in m["blobs"]), reverse=True)[:25]
    rows = []
    for size, s in largest:
        hp = m["head_blob_paths"].get(s, [])
        paths = blob_paths(m, s)
        if hp:
            status = "at HEAD (same blob)"
        elif any(p in m["head_files"] for p in paths):
            status = "path at HEAD, different content (this version history-only)"
        else:
            status = "not at HEAD (history only)"
        c, _ = blob_first(m, s)
        rows.append({"blob": s, "size": size, "MB": round(size / MB, 3), "MiB": round(size / MIB, 3),
                     "paths": paths, "first_commit": c, "status": status})
    head_big = []
    for p, (mode, typ, sha, size) in sorted(m["head_files"].items(), key=lambda x: -(x[1][3] or 0)):
        if typ == "blob" and size and size > 40 * MB:
            head_big.append({"path": p, "size": size, "MB": round(size / MB, 3),
                             "MiB": round(size / MIB, 3), "over_50MB": size > 50 * MB,
                             "over_50MiB": size > 50 * MIB, "over_100MB": size > 100 * MB,
                             "over_100MiB": size > 100 * MIB})
    return rows, head_big


def npz_section(m, binary):
    gi_head = git("show", f"{m['head']}:.gitignore").decode("utf-8", "replace").split("\n")
    wt_gi = open(os.path.join(ROOT, ".gitignore"), "rb").read()
    head_gi_bytes = git("show", f"{m['head']}:.gitignore")
    wt_matches_head = wt_gi == head_gi_bytes
    npz_paths = sorted({p for p in (m["all_paths_raw"] | m["all_paths_objs"]) if p.endswith(".npz")})
    ci = sh(["git", "check-ignore", "--no-index", "-v", "-n", "--stdin"],
            input=("\n".join(npz_paths) + "\n").encode(), check=False).stdout.decode().split("\n")
    ci_map = {}
    for line in ci:
        if not line.strip():
            continue
        meta, _, path = line.partition("\t")
        ci_map[path] = meta
    rows = []
    for p in npz_paths:
        explicit = [i + 1 for i, l in enumerate(gi_head) if l.strip() == f"!/{p}"]
        intro = None
        for s, occ in m["blob_occ"].items():
            for c, pp in occ:
                if pp == p:
                    o = m["commit_index"].get(c, 10 ** 9)
                    if intro is None or o < intro[0]:
                        intro = (o, c)
        intro_c = intro[1] if intro else None
        explicit_at_intro = None
        if intro_c:
            try:
                gi_i = git("show", f"{intro_c}:.gitignore").decode("utf-8", "replace").split("\n")
                explicit_at_intro = [i + 1 for i, l in enumerate(gi_i) if l.strip() == f"!/{p}"]
            except SystemExit:
                explicit_at_intro = []
        versions = [b for b in binary if p in b["paths"]]
        at_head = p in m["head_files"]
        members = sorted({x for b in versions for x in (b["npz_members"] or [])})
        meta = ci_map.get(p, "")
        rows.append({"path": p, "at_head": at_head, "head_size": m["head_files"][p][3] if at_head else None,
                     "n_versions": len(versions), "introduced": intro_c,
                     "explicit_allowlist_line_HEAD": explicit,
                     "check_ignore_HEAD": meta,
                     "explicit_allowlist_line_at_introduction": explicit_at_intro,
                     "npz_members": members})
    return rows, wt_matches_head


WEIGHT_NAME_RE = re.compile(r"(?i)(^|/)(adapters?|weights?|model[-_].*|pytorch_model.*|consolidated.*)"
                            r"\.(npz|safetensors|bin|pt|pth|ckpt|gguf)$")


def weights_section(m, all_paths):
    hits = []
    for p in sorted(all_paths):
        e = ext_of(p)
        if e in WEIGHT_EXT or WEIGHT_NAME_RE.search(p):
            hits.append({"path": p, "ext": e, "at_head": p in m["head_files"]})
    return hits


# ---------------------------------------------------------------- round 2 additions
JSON_EXT = (".json", ".jsonl", ".ipynb")


def json_vectors(m, min_len=256):
    """(iv), round 2: every reachable JSON / JSONL / .ipynb blob (every version) is parsed and walked; every
    all-numeric array of length >= min_len is recorded (float arrays individually; integer-only arrays counted).
    A residual-space vector stored as JSON text is invisible to the npz allowlist check."""
    shas = [s for s in m["blobs"] if any(p.endswith(JSON_EXT) for p in blob_paths(m, s))]
    out = {"blobs": len(shas), "parsed": 0, "unparsed": [], "float_arrays": [], "int_arrays": 0,
           "int_array_groups": collections.Counter()}
    for sha, typ, data in cat_batch(shas):
        paths = blob_paths(m, sha)
        txt = data.decode("utf-8", "replace")
        try:
            if all(p.endswith(".jsonl") for p in paths):
                docs = [(f"<line {i + 1}>", json.loads(l)) for i, l in enumerate(txt.split("\n")) if l.strip()]
            else:
                docs = [("", json.loads(txt))]
        except ValueError as ex:
            out["unparsed"].append({"blob": sha, "paths": paths, "error": str(ex)[:120]})
            continue
        out["parsed"] += 1
        for prefix, doc in docs:
            stack = [(prefix, doc)]
            while stack:
                ptr, o = stack.pop()
                if isinstance(o, dict):
                    for k, v in o.items():
                        stack.append((f"{ptr}/{k}", v))
                elif isinstance(o, list):
                    numeric = len(o) >= min_len and all(isinstance(x, (int, float)) and not isinstance(x, bool)
                                                       for x in o)
                    if numeric and any(isinstance(x, float) for x in o):
                        c, _ = blob_first(m, sha)
                        out["float_arrays"].append({"blob": sha, "paths": paths, "pointer": ptr, "length": len(o),
                                                    "at_head": sha in m["head_blobs"], "first_commit": c})
                    elif numeric:
                        out["int_arrays"] += 1
                        out["int_array_groups"][(", ".join(paths), re.sub(r"/\d+(?=/|$)", "/*", ptr))] += 1
                    else:
                        for i, v in enumerate(o):
                            stack.append((f"{ptr}/{i}", v))
    return out


def read_git_index(path):
    """Parse a git index file (versions 2 and 3) as a plain file -- no git process. Returns
    (version, checksum_ok, [(path, blob_sha, mode, size)])."""
    data = open(path, "rb").read()
    sig, ver, n = struct.unpack(">4sII", data[:12])
    if sig != b"DIRC" or ver not in (2, 3):
        return ver, None, None
    checksum_ok = hashlib.sha1(data[:-20]).digest() == data[-20:]
    off, entries = 12, []
    for _ in range(n):
        start = off
        mode, = struct.unpack(">I", data[off + 24:off + 28])
        size, = struct.unpack(">I", data[off + 36:off + 40])
        sha = data[off + 40:off + 60].hex()
        flags, = struct.unpack(">H", data[off + 60:off + 62])
        off += 62
        if ver >= 3 and flags & 0x4000:
            off += 2
        end = data.index(b"\0", off)
        entries.append((data[off:end].decode("utf-8", "replace"), sha, mode, size))
        off = start + ((end - start + 8) & ~7)
    return ver, checksum_ok, entries


MAC_CODENAMES = {26: "tahoe", 15: "sequoia", 14: "sonoma", 13: "ventura", 12: "monterey"}


def scanner_availability():
    """(i), round 2: are the block's primary scanners installed, and are they installable here? Reads the PATH
    and Homebrew's local formula index (a cache file; no brew command, no network)."""
    import platform
    import shutil
    import time
    out = {"which": {t: shutil.which(t) for t in ("gitleaks", "trufflehog")},
           "brew": shutil.which("brew") or ("/opt/homebrew/bin/brew" if os.path.exists("/opt/homebrew/bin/brew")
                                            else None)}
    mv = platform.mac_ver()[0]
    tag = None
    if mv:
        cn = MAC_CODENAMES.get(int(mv.split(".")[0]))
        tag = (("arm64_" if platform.machine() == "arm64" else "") + cn) if cn else None
    out["macos"], out["bottle_tag"] = mv, tag
    cache = os.path.expanduser("~/Library/Caches/Homebrew/api/formula.jws.json")
    out["cache"] = "~/Library/Caches/Homebrew/api/formula.jws.json" if os.path.exists(cache) else None
    out["formulae"] = {}
    if out["cache"]:
        out["cache_date"] = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(cache)))
        d = json.load(open(cache))
        payload = json.loads(d["payload"]) if isinstance(d, dict) and "payload" in d else d
        for f in payload:
            if f.get("name") in ("gitleaks", "trufflehog"):
                files = ((f.get("bottle") or {}).get("stable") or {}).get("files") or {}
                out["formulae"][f["name"]] = {"version": (f.get("versions") or {}).get("stable"),
                                              "license": f.get("license"),
                                              "bottle_for_this_platform": bool(tag and tag in files)}
    return out


def reflog_evidence(unreach_commits):
    """(v) pre-flip, round 2: remote-tracking reflogs read as plain files (.git/logs/refs/remotes/**): every
    update a fast-forward, every recorded value an ancestor of the ref's last value; the first push; and the
    unreachable local commit(s) placed against the first push. Emails in reflog lines are never read out."""
    out = {"remote": [], "unreachable_commits": []}
    base = os.path.join(ROOT, ".git", "logs", "refs", "remotes")
    seen_new_remote = set()
    first_push = None
    for dp, dns, fns in os.walk(base):
        for fn in sorted(fns):
            fp = os.path.join(dp, fn)
            ref = "refs/remotes/" + os.path.relpath(fp, base)
            rows = []
            for line in open(fp, encoding="utf-8", errors="replace"):
                head_, _, msg = line.rstrip("\n").partition("\t")
                parts = head_.split()
                rows.append((parts[0], parts[1], int(parts[-2]), parts[-1], msg.split(":")[0].strip()))
            last = rows[-1][1] if rows else None
            ff = [o == "0" * 40 or is_ancestor(o, n) for o, n, *_ in rows]
            anc = [is_ancestor(n, last) for _, n, *_ in rows]
            kinds = collections.Counter(r[4] for r in rows)
            seen_new_remote |= {r[1] for r in rows}
            pushes = [r for r in rows if r[4] == "update by push"]
            if pushes and (first_push is None or pushes[0][2] < first_push[0]):
                first_push = (pushes[0][2], pushes[0][3], pushes[0][1], ref)
            out["remote"].append({"ref": ref, "entries": len(rows), "kinds": dict(kinds),
                                  "all_fast_forward": all(ff), "all_ancestors_of_last": all(anc),
                                  "first": rows[0][1][:10] if rows else None,
                                  "first_time": fmt_ts(rows[0][2], rows[0][3]) if rows else None})
    out["first_push"] = ({"time": fmt_ts(first_push[0], first_push[1]), "commit": first_push[2][:10],
                          "ref": first_push[3]} if first_push else None)
    local_new = set()
    for lf in [os.path.join(ROOT, ".git", "logs", "HEAD")] + [
            os.path.join(dp, fn) for dp, _, fns in os.walk(os.path.join(ROOT, ".git", "logs", "refs", "heads"))
            for fn in fns]:
        if os.path.exists(lf):
            for line in open(lf, encoding="utf-8", errors="replace"):
                local_new.add(line.split(" ", 2)[1] if line.count(" ") >= 2 else "")
    for c in unreach_commits:
        raw = git("cat-file", "commit", c).decode("utf-8", "replace")
        hdr_, _, msg = raw.partition("\n\n")
        cm = re.search(r"(?m)^committer .* (\d+) ([+-]\d{4})$", hdr_)
        parents = re.findall(r"(?m)^parent ([0-9a-f]{40})$", hdr_)
        subj = msg.split("\n", 1)[0]
        ts = int(cm.group(1)) if cm else None
        twins = []
        if parents:
            kids = git("rev-list", "--all", "--parents").decode().split("\n")
            for l in kids:
                f_ = l.split()
                if len(f_) >= 2 and parents[0] in f_[1:]:
                    r2 = git("cat-file", "commit", f_[0]).decode("utf-8", "replace")
                    h2, _, m2 = r2.partition("\n\n")
                    c2 = re.search(r"(?m)^committer .* (\d+) ([+-]\d{4})$", h2)
                    if m2.split("\n", 1)[0] == subj:
                        twins.append({"commit": f_[0][:10], "seconds_after": (int(c2.group(1)) - ts)
                                      if (c2 and ts) else None})
        out["unreachable_commits"].append({
            "commit": c[:10], "committer_time": fmt_ts(ts, cm.group(2)) if cm else None,
            "before_first_push": bool(first_push and ts is not None and ts < first_push[0]),
            "in_remote_reflogs": c in seen_new_remote, "in_local_reflogs": c in local_new,
            "reachable_twin_same_parent_and_subject": twins})
    return out


def fmt_ts(ts, tz):
    """'YYYY-MM-DD HH:MM:SS +zzzz' in the reflog line's own offset."""
    import datetime
    sign = 1 if tz[0] == "+" else -1
    off = datetime.timedelta(hours=int(tz[1:3]), minutes=int(tz[3:5])) * sign
    return datetime.datetime.fromtimestamp(ts, datetime.timezone(off)).strftime("%Y-%m-%d %H:%M:%S ") + tz


HOME_PATH_RE = re.compile(r"/Users/[^\s\"'`)\]]*")


def home_paths_outside_repo(m, users_at_head):
    """(ii), round 2: absolute /Users/ paths at HEAD that point outside the repository, by kind; and the
    conda env name of another local project (the notebook's kernel display name)."""
    user = ROOT.split("/")[2] if ROOT.startswith("/Users/") else None
    kinds = collections.Counter()
    kind_files = collections.defaultdict(set)
    envs = set()
    paths = sorted(users_at_head)
    shas = [m["head_files"][p][2] for p in paths]
    for p, (sha, typ, data) in zip(paths, cat_batch(shas)):
        for mt in HOME_PATH_RE.finditer(data.decode("utf-8", "replace")):
            v = mt.group(0).rstrip(".,;:")
            if v == ROOT or v.startswith(ROOT + "/"):
                continue
            segs = v.split("/")
            if len(segs) < 3 or segs[2] != user:
                k = "a synthetic, elided or bare `/Users/` path (no real home directory)"
            elif "/.cache/huggingface/" in v:
                k = "the Hugging Face cache (a public model's snapshot path)"
            elif "/Library/Jupyter/runtime/" in v:
                k = "the Jupyter runtime directory (a kernel connection-file name)"
            elif "/miniconda3/envs/" in v:
                k = "a conda environment named for another local project"
                envs.add(v.split("/miniconda3/envs/", 1)[1].split("/", 1)[0])
            elif "/miniconda3/" in v:
                k = "the conda base installation's interpreter"
            elif "/.claude/projects/" in v:
                k = "Claude Code's local transcript store (classified under (ii))"
            else:
                k = "the home directory or a parent directory of the repository"
            kinds[k] += 1
            kind_files[k].add(p)
    nb = None
    if "paper_analysis.ipynb" in m["head_files"]:
        try:
            nb = json.loads(git("show", f"{m['head']}:paper_analysis.ipynb"))["metadata"]["kernelspec"]["display_name"]
        except (ValueError, KeyError, SystemExit):
            nb = None
    names = sorted(envs | ({nb} if nb else set()))
    env_files = {}
    for nm in names:
        out_ = git("grep", "-c", "-F", "-e", nm, m["head"], check=False).decode("utf-8", "replace")
        env_files[nm] = {l.split(":", 1)[1].rsplit(":", 1)[0]: int(l.rsplit(":", 1)[1])
                         for l in out_.split("\n") if l.strip()}
    return {"kinds": kinds, "kind_files": kind_files, "env_names": names, "notebook_display_name": nb,
            "env_files": env_files}


PENDING_ID_CLASSES = ("runpod_pod_id (context: pod)", "runpod_volume_id (context: volume)", VOLNAME_CLASS,
                      "container_hostname (12 hex after host:/root@)", "ipv4_address", "ssh_fingerprint",
                      "ssh_public_key", "claude_session_or_artifact_link", "email_address")
# Round 4 (fourth checker, finding 4): email addresses in pending files. The service address is public by design;
# the commit identities' addresses are in the known set (their own line, below); any other address is a possible
# third party's personal data and stays UNTRIAGED (a redaction-rule blocker in an audit file) until Code triages it.
# This is the pending scan's only class of third-party personal data.
PENDING_EMAIL_EXEMPT = {"noreply@anthropic.com"}
# Round 3 (third checker, finding 4): the pre-release line is split. Values of these labels are the commit
# identities' own metadata (the author's and the author's tool identity's), public in the commit headers of the
# history being published; the routing's redaction rule covers third-party personal data, not them. This raw still redacts them by its own policy and lists a pending
# file carrying one, but such a file does not make the line NOT CLEAN. Every other sensitive label does.
AUTHOR_IDENTITY_LABELS = ("identity email, public in the commit headers", "laptop hostname")


def pending_scan(known, exclude):
    """Pre-release check (round 2; the second checker's finding 1): files NOT yet in history -- untracked,
    non-ignored files and tracked files modified in the working tree -- read as plain files and scanned for
    (a) every value this run treats as sensitive (word-bounded, exact), (b) any NEW RunPod-id-shaped /
    container / IPv4 / SSH fingerprint / public key / session-link value or SSH-port-line number, and (c) the
    precise secret patterns. A snapshot: other sessions write these files concurrently. Round 4: (b) includes
    email addresses other than the service address and the commit identities' (possible third-party personal
    data), and (c) passes each match's own line to triage_precise, as the history scan does."""
    untracked = [f for f in git("ls-files", "--others", "--exclude-standard", "-z").decode("utf-8", "replace")
                 .split("\0") if f]
    modified = [f for f in git("ls-files", "-m", "-z").decode("utf-8", "replace").split("\0") if f]
    files = [(f, "untracked") for f in sorted(untracked) if f not in exclude] + \
            [(f, "modified (tracked)") for f in sorted(set(modified)) if f not in exclude]
    rx = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(v) for v in sorted(known, key=len, reverse=True))
                    + r")(?![A-Za-z0-9])") if known else None
    known_keys = {vkey(v) for v in known}
    rows = []
    for f, status in files:
        fp = os.path.join(ROOT, f)
        if not os.path.isfile(fp) or os.path.islink(fp):
            continue
        text = open(fp, "rb").read().decode("utf-8", "replace")
        hits = collections.Counter(mt.group(1) for mt in rx.finditer(text)) if rx else collections.Counter()
        new = []
        emails = collections.Counter()
        for cls in PENDING_ID_CLASSES:
            if cls in ANCHORED:   # round 4: email_address
                for _, v in ANCHORED[cls](text):
                    if v in PENDING_EMAIL_EXEMPT:
                        emails["service address"] += 1
                        continue
                    if vkey(v) in known_keys:
                        emails["commit identity"] += 1
                        continue
                    emails["other"] += 1
                    tri = manual(v) or ("UNTRIAGED", "an email address in a pending file that is neither the service "
                                        "address nor a commit identity's; possibly a third party's personal data; "
                                        "needs individual triage", True)
                    if tri[0] not in ("FALSE-POSITIVE", "PUBLIC"):
                        new.append((cls, v, tri))
                continue
            for mt in ID_RE[cls].finditer(text):
                gd = mt.groupdict()
                gname = next((g for g in ("v", "v2", "v3", "v4") if gd.get(g)), None)   # as in scan_history
                v = gd.get(gname) if gname else None
                if not v or vkey(v) in known_keys:
                    continue
                if cls in ("runpod_pod_id (context: pod)", "runpod_volume_id (context: volume)") and \
                        not (re.search(r"\d", v) and len(re.findall(r"[a-z]", v)) >= 2):
                    continue
                tri = triage_identifier(cls, v, None)
                if tri[0] in ("FALSE-POSITIVE", "PUBLIC"):
                    continue
                new.append((cls, v, tri))
        seen_pl = set()
        for sm in SSH_LINE_RE.finditer(text):
            a = text.rfind("\n", 0, sm.start()) + 1
            if a in seen_pl:
                continue
            seen_pl.add(a)
            b = text.find("\n", sm.start())
            if code_port_only(text[a:b if b >= 0 else len(text)], "pending"):
                continue
            for pm in PORT_NUM_RE.finditer(text[a:b if b >= 0 else len(text)]):
                v = pm.group("v")
                if re.fullmatch(r"(19|20)\d\d", v) or vkey(v) in known_keys:
                    continue
                tri = manual(v) or ("UNTRIAGED", "a 4-5 digit number on an ssh/port/alias line in a pending "
                                    "file; not in history; needs individual triage", True)
                if tri[0] != "FALSE-POSITIVE":
                    new.append((PORT_CLASS, v, tri))
        prec = []
        li_ = LineIndex(text)
        hexq = collections.Counter()
        for name, prx, grp in PRECISE:
            for mt in prx.finditer(text):
                v = mt.group(grp) if grp else mt.group(0)
                # round 4 (fourth checker, finding 3): the match's own line, as in the history scan (it passed "",
                # so the hex-digest rule could never fire here)
                tri = triage_precise(name, v, li_.line_text(mt.start()), f)
                if name in ("quoted_secretish_assignment", "url_secret_query_param") and \
                        re.fullmatch(r"[0-9a-fA-F]+", v):
                    hexq[tri[0]] += 1
                if tri[0] != "FALSE-POSITIVE":
                    prec.append((name, v, tri))
        dedup = collections.OrderedDict(((c, v), t) for c, v, t in new)
        pdedup = collections.OrderedDict(((n, v), t) for n, v, t in prec)
        rows.append({"file": f, "status": status, "bytes": len(text.encode("utf-8", "replace")), "known": hits,
                     "new": [(c, v, t) for (c, v), t in dedup.items()],
                     "precise": [(n, v, t) for (n, v), t in pdedup.items()],
                     "emails": emails, "hex_quoted": hexq})
    return rows


def pending_group(f):
    if f.startswith("results/raw/2026-10-08_note-") or f.startswith("scripts/audit_note_") or \
            f.startswith("README-NOTE"):
        return "audit outputs (this audit's end commit)"
    if f.startswith(("data/m/", "results/raw/2026-10-08_m-")):
        return "the concurrent PROPOSAL-m session's files"
    return "other untracked or modified files (the PI's documents)"


# ---------------------------------------------------------------- round 5: the leak guard
def guard_decide(R, known, candidates, r5a=False):
    """Round 5. R: value -> list of (source, class, verdict, explicit) records from every table this run fills;
    known: the known sensitive values (never exempt); candidates: every value the guard considers. Returns
    (refuse, why, exempt): the values the guard refuses to see verbatim, a reason label per refused value, and the
    verdict set per exempt value. r5a=True replays the first round-5 decision (no generated-segment rule; a known
    value inside another found only word-bounded), for the second check's controls only."""
    known = {v for v in known if v}
    kms = ([(k_, "word", re.compile(r"(?<![A-Za-z0-9])" + re.escape(k_) + r"(?![A-Za-z0-9])")) for k_ in sorted(known)]
           if r5a else known_matchers(known))
    refuse, why, exempt = set(), {}, {}
    for v in candidates:
        if not v:
            continue
        if v in SAFE_VERBATIM:
            exempt[v] = ("SAFE-VERBATIM",)
            continue
        if v in known:
            refuse.add(v)
            why[v] = "a known sensitive value"
            continue
        recs = R.get(v, ())
        if not recs:
            refuse.add(v)
            why[v] = "redacted, with no verdict"
            continue
        bad = sorted({r_[2] for r_ in recs if r_[2] not in GUARD_EXEMPT_VERDICTS})
        if bad:
            refuse.add(v)
            why[v] = "verdict " + "/".join(bad)
            continue
        if any(r_[1] in REDACTION_RULE_CLASSES and not r_[3] for r_ in recs):
            refuse.add(v)
            why[v] = "a redaction-rule class with no explicit triage"
            continue
        if not r5a and any(not r_[3] for r_ in recs) and random_segment(v):
            refuse.add(v)
            why[v] = "a mechanical verdict on a value with a generated-looking segment, with no explicit triage"
            continue
        if any(km_count(km_, v, first=True) for km_ in kms) or SESSION_LINK_RE.search(v):
            refuse.add(v)
            why[v] = "carries a known sensitive value or a session link"
            continue
        exempt[v] = tuple(sorted({r_[2] for r_ in recs}))
    return refuse, why, exempt


_RANDSEG = {}


def random_segment(v):
    """has_random_segment, memoized (the guard asks it of every candidate on every control)."""
    if v not in _RANDSEG:
        _RANDSEG[v] = has_random_segment(v)
    return _RANDSEG[v]


KNOWN_MIN_SUBSTR = 8
HEX_CHARS = frozenset("0123456789abcdefABCDEF")
_KM = {}


def known_matchers(known):
    """Round 5, second check: one (value, kind, regex) per known value. A value of KNOWN_MIN_SUBSTR or more characters
    is matched as a plain substring, case-insensitively, with each interior run of separators (`-`, `_`, space, `.`)
    matching any run of them, tabs included, or none (kind 'variant'); an all-digit value (an SSH port) digit-bounded (kind
    'digits'; km_count skips a match inside a run of 8+ hex characters, a digest); any other value word-bounded, as
    round 4 matched (kind 'word')."""
    key = frozenset(known)
    if key not in _KM:
        out = []
        for v in sorted(key, key=lambda x: (-len(x), sha256_hex(x.encode()))):
            if v.isdigit():
                out.append((v, "digits", re.compile(r"(?<![0-9])" + re.escape(v) + r"(?![0-9])")))
            elif len(v) >= KNOWN_MIN_SUBSTR:
                # interior separator runs only: a leading or trailing one stays literal, so the pattern never
                # shrinks to a bare word
                parts = [p_ for p_ in re.split(r"([-_ .]+)", v) if p_]
                out.append((v, "variant", re.compile("".join(
                    r"[-_ \t.]*" if (re.fullmatch(r"[-_ .]+", p_) and 0 < i_ < len(parts) - 1) else re.escape(p_)
                    for i_, p_ in enumerate(parts)), re.I)))
            else:
                out.append((v, "word", re.compile(r"(?<![A-Za-z0-9])" + re.escape(v) + r"(?![A-Za-z0-9])")))
        _KM[key] = out
    return _KM[key]


def in_digest(txt, s, e):
    """True if txt[s:e] lies inside a maximal run of 8 or more hex characters (a sha8 or longer digest)."""
    a, b = s, e
    while a > 0 and txt[a - 1] in HEX_CHARS:
        a -= 1
    while b < len(txt) and txt[b] in HEX_CHARS:
        b += 1
    return b - a >= 8


def km_count(km, txt, first=False):
    """Matches of one known matcher in txt (a digit match inside a digest not counted); first=True stops at one."""
    v, kind, rx = km
    if kind != "variant" and v not in txt:
        return 0
    n = 0
    for m_ in rx.finditer(txt):
        if kind == "digits" and in_digest(txt, m_.start(), m_.end()):
            continue
        n += 1
        if first:
            break
    return n


def digest_skips(known, txt):
    """Digit-bounded matches of the all-digit known values that km_count skips because they sit inside a digest."""
    n = 0
    for v, kind, rx in known_matchers({k_ for k_ in known if k_}):
        if kind == "digits" and v in txt:
            n += sum(1 for m_ in rx.finditer(txt) if in_digest(txt, m_.start(), m_.end()))
    return n


def guard_known(pend_known):
    """Round 5, second check: the guard's known set -- the pre-release section's sensitive values plus, for each
    session link, its bare id (the last run of 8+ letters and digits), so the id without its claude.ai/code/ prefix
    is guarded too. Guard-only: the pre-release section's own set is unchanged."""
    out = {v for v in pend_known if v}
    for v, labels in pend_known.items():
        if any(str(c_).startswith("claude_session_or_artifact_link") for c_ in labels):
            ids_ = re.findall(r"[A-Za-z0-9]{8,}", v)
            if ids_:
                out.add(ids_[-1])
    return out


def guard_form(v):
    """Round 5: the form the guard's refusal message prints -- 'lenN:sha8' for a value of 4 characters or fewer or one
    that opens with 4 digits (no character of it shown), else the generic redacted form; never registers the value."""
    if len(v) <= 4 or re.match(r"\d{4}", v):
        return f"len{len(v)}:{sha256_hex(v.encode())[:8]}"
    return f"{v[:4]}...[len {len(v)}]#{sha256_hex(v.encode())[:8]}"


def guard_candidates(R, known, redacted):
    """Round 5: every value the guard considers -- each value printed in redacted form with the sensitive flag, each
    known sensitive value, and (second check, finding 2) each value of this run's tables, printed or not, with a
    verdict outside GUARD_EXEMPT_VERDICTS (the refuse verdicts and METADATA, METADATA-ECHO, PUBLIC-KEY,
    SSH-SIGNATURE alike), a mechanical record of a redaction-rule class, or (finding 3) a mechanical record on a value
    with a generated-looking segment. guard_decide exempts SAFE_VERBATIM first."""
    return (set(redacted) | {v for v in known if v}
            | {v for v, recs in R.items()
               if any(r_[2] not in GUARD_EXEMPT_VERDICTS or (r_[1] in REDACTION_RULE_CLASSES and not r_[3])
                      for r_ in recs)
               or (any(not r_[3] for r_ in recs) and random_segment(v))})


def guard_candidates_r5a(R, known, redacted):
    """The first round-5 candidate rule, kept only so the controls can show which gap cases it missed."""
    return (set(redacted) | {v for v in known if v}
            | {v for v, recs in R.items() if any(r_[2] in GUARD_REFUSE_VERDICTS for r_ in recs)})


def guard_scan(values, outputs, known=(), round4=False):
    """Round 5. Every (output label, value) with the value verbatim in the output; deterministic order. Second check
    (finding 4, 5): a known value is matched by its known_matchers entry (8+ characters: plain substring, case- and
    separator-insensitive; all-digit: digit-bounded outside digests); any other value of KNOWN_MIN_SUBSTR or more
    characters as a plain substring; a shorter one word-bounded (no letter or digit touching it). round4=True
    replays round 4's rule (word-bounded throughout, no known matcher)."""
    kmd = {} if round4 else {km_[0]: km_ for km_ in known_matchers({k_ for k_ in known if k_})}
    leaks = []
    for v in sorted(values, key=lambda x: (sha256_hex(x.encode()), x)):
        for label, txt in outputs:
            if v in kmd:
                hit = km_count(kmd[v], txt, first=True) > 0
            elif len(v) >= KNOWN_MIN_SUBSTR and not round4:
                hit = v in txt
            else:
                hit = v in txt and bool(re.search(r"(?<![A-Za-z0-9])" + re.escape(v) + r"(?![A-Za-z0-9])", txt))
            if hit:
                leaks.append((label, v))
    return leaks


def guard_controls(R, known, redacted, outputs, pend_known):
    """Round 5 positive controls. Every control value is resolved from this run's own tables (or generated) in memory
    and is never printed, returned or written: the result holds booleans, counts and class labels only."""
    import secrets
    import string
    md_, js_ = outputs["md"], outputs["json"]
    base_out = [("md", md_), ("json", js_)]
    candidates = guard_candidates(R, known, redacted)
    ref0, why0, ex0 = guard_decide(R, known, candidates)
    base = guard_scan(ref0, base_out, known)
    res = {"outputs_as_written": {"leaks": len(base), "pass": not base}}

    def injected(v, extra_R=None):
        """Inject v into a copy of each output (alone on its own line) and run the guard as a real run would."""
        R2 = R if extra_R is None else {**R, **extra_R}
        c2 = guard_candidates(R2, known, redacted)
        ref, why, _ = guard_decide(R2, known, c2)
        out = {}
        for lab_ in ("md", "json"):
            outs = [(l_, (t_ + "\n" + v + "\n") if l_ == lab_ else t_) for l_, t_ in base_out]
            lk = guard_scan(ref, outs, known)
            out[lab_] = {"refused": (lab_, v) in lk, "other_new_leaks": len(set(lk) - set(base) - {(lab_, v)})}
        # the same value with the known set emptied: does its own verdict alone make the guard refuse it?
        ref_k, why_k, _ = guard_decide(R2, set(), guard_candidates(R2, set(), redacted))
        out["refused_by_its_verdict_alone"] = v in ref_k
        out["reason"] = why.get(v)
        out["reason_without_known_set"] = why_k.get(v)
        out["verbatim_in_outputs_as_written"] = bool(guard_scan({v}, base_out, known))
        return out

    def injected_text(text, targets, extra_R=None, extra_red=()):
        """Second check: inject text (its own line) into a copy of each output and run the guard as a real run would.
        Per output: refused = every target value is reported in that copy (the target can differ from the text, as
        when the text is a variant of a known value or a value glued into other characters)."""
        R2 = R if extra_R is None else {**R, **extra_R}
        red2 = set(redacted) | set(extra_red)
        c2 = guard_candidates(R2, known, red2)
        ref, why, _ = guard_decide(R2, known, c2)
        out = {"targets": len(targets)}
        for lab_ in ("md", "json"):
            outs = [(l_, (t_ + "\n" + text + "\n") if l_ == lab_ else t_) for l_, t_ in base_out]
            lk = set(guard_scan(ref, outs, known))
            out[lab_] = all((lab_, t_) in lk for t_ in targets)
        out["reasons"] = sorted({str(why.get(t_)) for t_ in targets})
        out["refused"] = out["md"] and out["json"]
        # the first round-5 guard (its candidate rule, its decision without the generated-segment rule, round 4's
        # word-bounded matching) on the same copies: True would mean the case was no gap
        ref_a, _, _ = guard_decide(R2, known, guard_candidates_r5a(R2, known, red2), r5a=True)
        out["first_round5_guard_refused"] = all(
            (lab_, t_) in set(guard_scan(ref_a, [(l_, (x_ + "\n" + text + "\n") if l_ == lab_ else x_)
                                                 for l_, x_ in base_out], round4=True))
            for lab_ in ("md", "json") for t_ in targets)
        return out
    # (i) a real RunPod pod id, resolved from this run's history tables
    pods = sorted((v for v, c_ in pend_known.items() if any(x.startswith("runpod_pod_id") for x in c_)),
                  key=lambda x: sha256_hex(x.encode()))
    if pods:
        r_ = injected(pods[0])
        r_.update({"n_candidates": len(pods), "class": "runpod_pod_id",
                   "verdicts": sorted({x[2] for x in R.get(pods[0], ())})})
        res["i_pod_id"] = r_
    else:
        res["i_pod_id"] = {"missing": True}
    # (ii) a synthetic secret-shaped value, generated here, whose triage under the script's own rules is UNTRIAGED
    name_ = "huggingface_token hf_"
    rx_ = next(rx for n_, rx, _ in PRECISE if n_ == name_)
    alph = string.ascii_letters + string.digits
    syn = "hf" + "_" + "".join(secrets.choice(alph) for _ in range(34))
    tri = triage_precise(name_, syn, "token = " + syn, "<round-5 control>")
    r_ = injected(syn, {syn: [("control", "precise:" + name_, tri[0], False)]})
    r_.update({"pattern": name_, "pattern_matches": bool(rx_.fullmatch(syn)), "triage": tri[0],
               "in_this_run_tables": syn in R})
    res["ii_synthetic_untriaged"] = r_
    # (iii) one of the SSH ports (verdict IDENTIFIER), resolved from this run's history tables
    ports = sorted((v for v, c_ in pend_known.items() if PORT_CLASS in c_), key=lambda x: sha256_hex(x.encode()))
    if ports:
        r_ = injected(ports[0])
        r_.update({"n_candidates": len(ports), "class": "ssh_port",
                   "verdicts": sorted({x[2] for x in R.get(ports[0], ())})})
        res["iii_ssh_port"] = r_
    else:
        res["iii_ssh_port"] = {"missing": True}
    # (iv) the generic tokens: every round-5-triaged value this run holds, its verbatim presence and its decision
    t16 = sorted({v for v in set(R) | candidates if sha256_hex(v.encode())[:16] in TRIAGE16})
    shv = sorted({v for v, recs in R.items() for x in recs if x[0] == "shape16"})
    verb = {v: [l_ for l_, t_ in base_out if v in t_ and re.search(r"(?<![A-Za-z0-9])" + re.escape(v)
                                                                       + r"(?![A-Za-z0-9])", t_)] for v in t16 + shv}
    res["iv_generic_tokens"] = {
        "triage16_values_in_run": len(t16), "triage16_verbatim_in_outputs": sum(1 for v in t16 if verb[v]),
        "triage16_refused": sum(1 for v in t16 if v in ref0),
        "shape16_values_in_run": len(shv), "shape16_verbatim_in_outputs": sum(1 for v in shv if verb[v]),
        "shape16_refused": sum(1 for v in shv if v in ref0),
        "guard_passes_outputs": not base}
    # (v) the same outputs with the round-5 entries' verdicts read as UNTRIAGED (the triage absent)
    R_cf = {v: ([(x[0], x[1], "UNTRIAGED", False) for x in recs]
                if (sha256_hex(v.encode())[:16] in TRIAGE16 or any(x[0] == "shape16" for x in recs)) else recs)
            for v, recs in R.items()}
    ref_cf, _, _ = guard_decide(R_cf, known, guard_candidates(R_cf, known, redacted))
    lk_cf = guard_scan(ref_cf, base_out, known)
    res["v_without_round5_triage"] = {"entries": len(lk_cf), "distinct": len({v for _, v in lk_cf}),
                                      "all_round5_values": all(sha256_hex(v.encode())[:16] in TRIAGE16 or
                                                               any(x[0] == "shape16" for x in R.get(v, ()))
                                                               for _, v in lk_cf)}
    # (vi) the round-4 rule replayed on the same outputs: every value printed redacted with the sensitive flag,
    # matched word-bounded as round 4 matched
    lk4 = guard_scan(set(redacted), base_out, round4=True)
    d4 = {v for _, v in lk4}
    res["vi_round4_rule"] = {"entries": len(lk4), "distinct": len(d4),
                             "exempt_now_by_explicit_entry": sum(1 for v in d4 if v in ex0 and manual(v)),
                             "exempt_now_by_mechanical_verdict": sum(1 for v in d4 if v in ex0 and not manual(v)),
                             "refused_now": sum(1 for v in d4 if v in ref0),
                             "by_exempt_verdict": dict(most_common_sorted(collections.Counter(
                                 "/".join(ex0[v]) for v in d4 if v in ex0)))}
    # ---- second check (the round-5 checker's findings 2-5): the gap cases, each injected as a real write would see it
    rnd = lambda n_, al_=alph: "".join(secrets.choice(al_) for _ in range(n_))
    lower = string.ascii_lowercase
    nk = lambda x_: x_ not in R and x_ not in known and x_ not in md_ and x_ not in js_
    pod_cls = next(c_ for c_ in ID_PATTERNS if c_.startswith("runpod_pod_id"))
    sc = {}
    # (vii) finding 2: values the first round-5 candidate rule did not consider
    while True:
        s1 = rnd(14, string.ascii_lowercase + string.digits)
        if nk(s1) and re.search(r"\d", s1) and re.search(r"[a-z]", s1):
            break
    sc["vii_a_rule_class_mechanical_exempt"] = injected_text(
        s1, [s1], {s1: [("control", pod_cls, "FALSE-POSITIVE", False, None)]})
    s2 = rnd(12, lower) + "." + rnd(6, lower)
    sc["vii_b_metadata_verdict"] = injected_text(s2, [s2], {s2: [("control", "context_free", "METADATA", False, None)]})
    # (viii) finding 3: a temp path holding a fresh 32-character generated segment, a mechanical LOCAL-PATH verdict;
    # beside it the case the exemption is for: a temp path of words only, with the same mechanical verdict
    while True:
        seg = rnd(32)
        if has_random_segment(seg):
            break
    s3 = "/tmp/" + seg + "/" + rnd(6, lower) + ".log"
    sc["viii_temp_path_generated_segment"] = injected_text(
        s3, [s3], {s3: [("control", "local_temp_path", "LOCAL-PATH", False, None)]}, extra_red=[s3])
    s3b = "/tmp/" + rnd(10, lower) + "/" + rnd(6, lower) + ".log"
    R3b = {**R, s3b: [("control", "local_temp_path", "LOCAL-PATH", False, None)]}
    ref3b, _, ex3b = guard_decide(R3b, known, guard_candidates(R3b, known, set(redacted) | {s3b}))
    sc["viii_b_words_only_temp_path_exempt"] = {"exempt": s3b in ex3b and s3b not in ref3b,
                                                "random_segment": has_random_segment(s3b)}
    # (ix) finding 4: a known value glued to letters, or inside an exempt-looking value
    pods_ = sorted((v for v, c_ in pend_known.items() if any(x.startswith("runpod_pod_id") for x in c_)),
                   key=lambda x: sha256_hex(x.encode()))
    ports_ = sorted((v for v, c_ in pend_known.items() if PORT_CLASS in c_), key=lambda x: sha256_hex(x.encode()))
    if pods_:
        p0 = pods_[0]
        sc["ix_a_pod_id_glued_to_letters"] = injected_text(rnd(3, lower) + p0 + rnd(3, lower), [p0])
        s4 = "/tmp/run" + p0 + "x/" + rnd(6, lower)
        sc["ix_b_pod_id_inside_mechanical_local_path"] = injected_text(
            s4, [s4, p0], {s4: [("control", "local_temp_path", "LOCAL-PATH", False, None)]}, extra_red=[s4])
        # (x) finding 5: case variants of a pod id
        sc["x_a_pod_id_upper_case"] = injected_text(p0.upper(), [p0])
    if ports_:
        q0 = ports_[0]
        sc["ix_c_port_glued_to_letters"] = injected_text("p" + q0 + "x", [q0])
        sc["ix_d_port_ssh_flag_form"] = injected_text("ssh -p" + q0 + " box", [q0])
        # the declared exception: a port's digits inside a run of 8+ hex characters (a digest) are not a port
        hx = rnd(4, "abcdef") + q0 + rnd(4, "abcdef")
        outs_e = [(l_, t_ + "\n#" + hx + "\n") for l_, t_ in base_out]
        sc["ix_f_port_inside_digest_not_refused"] = {
            "refused": any(v_ == q0 for _, v_ in guard_scan(ref0, outs_e, known)), "declared_exception": True}
    pph = sorted((v for v, c_ in pend_known.items() if any(str(x).startswith("passphrase") for x in c_)),
                 key=lambda x: sha256_hex(x.encode()))
    if pph:
        f0 = pph[0]
        has_sep = bool(re.search(r"[-_ .]", f0))
        # (ix-e) finding 4, the 'carries' path itself: a temp path with no generated-looking segment (so the
        # generated-segment rule does not decide it) carrying the pass-phrase-shaped value glued to letters
        s5 = "/tmp/" + rnd(2, lower) + f0 + rnd(2, lower) + "/" + rnd(5, lower) + ".log"
        sc["ix_e_known_value_inside_words_only_local_path"] = {
            **injected_text(s5, [s5, f0], {s5: [("control", "local_temp_path", "LOCAL-PATH", False, None)]},
                            extra_red=[s5]),
            "random_segment": has_random_segment(s5)}
        sc["x_b_passphrase_variants"] = {"has_separators": has_sep, **{
            k_: injected_text(t_, [f0])["refused"] for k_, t_ in (
                ("spaces", re.sub(r"[-_ .]+", " ", f0)), ("underscores", re.sub(r"[-_ .]+", "_", f0)),
                ("no_separators", re.sub(r"[-_ .]+", "", f0)), ("upper_case", f0.upper()),
                ("title_spaces", re.sub(r"[-_ .]+", " ", f0).title()))}}
    lap = sorted((v for v, c_ in pend_known.items() if "laptop hostname" in c_), key=lambda x: sha256_hex(x.encode()))
    if lap:
        sc["x_c_laptop_hostname_case"] = {"lower": injected_text(lap[0].lower(), [lap[0]])["refused"],
                                          "upper": injected_text(lap[0].upper(), [lap[0]])["refused"]}
    ses = sorted((v for v, c_ in pend_known.items()
                  if any(str(x).startswith("claude_session_or_artifact_link") for x in c_)),
                 key=lambda x: sha256_hex(x.encode()))
    if ses:
        sid = re.findall(r"[A-Za-z0-9]{8,}", ses[0])[-1]
        sc["x_d_session_id_without_prefix"] = {
            "id_in_guard_known_set": sid in known,
            "bare_id": injected_text(sid, [sid])["refused"],
            "session_word_and_id": injected_text("session_" + sid, [sid])["refused"],
            "id_upper_case": injected_text(sid.upper(), [sid])["refused"]}
    res["second_check"] = sc
    c_a = guard_candidates_r5a(R, known, redacted)
    w_ = {v for v, recs in R.items() if any(x[2] not in GUARD_EXEMPT_VERDICTS or
                                            (x[1] in REDACTION_RULE_CLASSES and not x[3]) for x in recs)}
    add_w, add_g = (candidates - c_a) & w_, (candidates - c_a) - w_
    kinds_ = collections.Counter(k_ for _, k_, _ in known_matchers({k_ for k_ in known if k_}))
    vc_ = lambda vs_: dict(most_common_sorted(collections.Counter(
        "/".join(sorted({x[2] + " | " + x[1].split(" (")[0] for x in R.get(v, ())})) for v in vs_)))
    res["second_check_counts"] = {
        "candidates": len(candidates), "candidates_first_round5_rule": len(c_a),
        "added_by_widened_rule": len(add_w), "added_by_widened_rule_verdict_class": vc_(add_w),
        "added_by_widened_rule_safe_verbatim": sum(1 for v in add_w if v in SAFE_VERBATIM),
        "added_by_widened_rule_refused": sum(1 for v in add_w if v in ref0),
        "added_by_generated_segment_rule": len(add_g), "added_by_generated_segment_rule_verdict_class": vc_(add_g),
        "added_by_generated_segment_rule_refused": sum(1 for v in add_g if v in ref0),
        "refused_by_generated_segment_rule": sum(1 for v in ref0 if why0[v].startswith("a mechanical verdict on")),
        "generated_segment_rule_values_substring_in_outputs": sum(
            1 for v in ref0 if why0[v].startswith("a mechanical verdict on") and (v in md_ or v in js_)),
        "known_matcher_kinds": dict(most_common_sorted(kinds_)),
        "known_in_guard_set": len([k_ for k_ in known if k_]),
        "digest_skips": {"md": digest_skips(known, md_), "json": digest_skips(known, js_)},
        "known_any_variant_hits": {"md": sum(km_count(km_, md_) for km_ in known_matchers({k_ for k_ in known if k_})),
                                   "json": sum(km_count(km_, js_) for km_ in known_matchers({k_ for k_ in known if k_}))},
        "refused_8plus_substring_hits": sum(1 for v in ref0 if v not in known and len(v) >= KNOWN_MIN_SUBSTR
                                            and (v in md_ or v in js_))}

    def sc_ok():
        need = ["vii_a_rule_class_mechanical_exempt", "vii_b_metadata_verdict", "viii_temp_path_generated_segment",
                "ix_a_pod_id_glued_to_letters", "ix_b_pod_id_inside_mechanical_local_path", "x_a_pod_id_upper_case",
                "ix_e_known_value_inside_words_only_local_path",
                "ix_c_port_glued_to_letters", "ix_d_port_ssh_flag_form"]
        if not all(k_ in sc and sc[k_]["refused"] for k_ in need):
            return False
        if not sc["viii_b_words_only_temp_path_exempt"]["exempt"] or sc["ix_f_port_inside_digest_not_refused"]["refused"]:
            return False
        if not all(sc["x_b_passphrase_variants"][k_] for k_ in ("spaces", "underscores", "no_separators",
                                                                 "upper_case", "title_spaces")):
            return False
        if not all(sc["x_c_laptop_hostname_case"].values()):
            return False
        return all(sc["x_d_session_id_without_prefix"].values())
    res["second_check_all_pass"] = bool(pods_ and ports_ and pph and lap and ses and sc_ok())
    ok = (res["second_check_all_pass"] and res["outputs_as_written"]["pass"]
          and all(res[k_].get(lab_, {}).get("refused") for k_ in ("i_pod_id", "ii_synthetic_untriaged", "iii_ssh_port")
                  for lab_ in ("md", "json"))
          and all(res[k_].get("refused_by_its_verdict_alone") for k_ in ("i_pod_id", "ii_synthetic_untriaged",
                                                                        "iii_ssh_port"))
          and res["ii_synthetic_untriaged"]["triage"] == "UNTRIAGED" and res["ii_synthetic_untriaged"]["pattern_matches"]
          and not res["ii_synthetic_untriaged"]["in_this_run_tables"]
          and not any(res[k_].get("verbatim_in_outputs_as_written") for k_ in ("i_pod_id", "ii_synthetic_untriaged",
                                                                              "iii_ssh_port"))
          and res["iv_generic_tokens"]["triage16_refused"] == 0 and res["iv_generic_tokens"]["shape16_refused"] == 0
          and res["v_without_round5_triage"]["all_round5_values"]
          and res["vi_round4_rule"]["refused_now"] == 0)
    res["all_pass"] = bool(ok)
    return res, (candidates, ref0, why0, ex0, base)


# ---------------------------------------------------------------- report
def compact_shape(rows):
    """One record per distinct (key, op, value, class, verdict, reason), with every locator."""
    g = collections.OrderedDict()
    for r in rows:
        k = (r["key"], r["op"], r["quoted"], r["value"], r["value_class"], r["verdict"], r["reason"])
        g.setdefault(k, []).append(r["locator"])
    return [{"key": k[0], "op": k[1], "quoted": k[2], "value": k[3], "value_class": k[4], "verdict": k[5],
             "reason": k[6], "n": len(v), "locators": v} for k, v in g.items()]


# The checker's stated figures (adversarial check of the builder's raw at bbc9ffe), quoted so this run can
# compare against them. Redacted keys only.
CHECKER_PORTS = {"25124cd5": (78, 78, 1, "RESULTS.md:9245"), "dae17182": (78, 78, 1, None),
                 "47e5fcc0": (13, 13, 2, None), "2be8ef0e": (13, 13, 2, None), "54e4496b": (9, 9, 1, None)}


def values_check(w, V):
    """The checker's findings, each with its disposition and this run's evidence."""
    exact, ids, hdr, binc, cf = V["exact"], V["ids"], V["hdr"], V["binc"], V["cf"]
    m, head, since = V["m"], V["head"], V["since"]
    base_known = m.get("base_objs") is not None
    by_key = {vkey(v): (v, e) for v, e in exact.items()}
    w("## Values-check")
    w("")
    lnc = V["live_new_commits"]
    # round 5: attribute each commit by its subject, as the header's coverage line does (round 4 called every one of
    # them the PROPOSAL-m session's, which stopped being true when the audit's own commits landed)
    subj_ = {c: git("log", "-1", "--format=%s", c).decode("utf-8", "replace") for c in lnc}
    lnc_m = [c for c in lnc if re.search(r"G-CAL|PROPOSAL-m|^m package", subj_[c])]
    lnc_a = [c for c in lnc if c not in lnc_m and subj_[c].startswith("AUDIT-note-release")]
    lnc_o = [c for c in lnc if c not in lnc_m and c not in lnc_a]
    w("The builder's raw (script sha256 `bd80512c...1a2d`, run at `bbc9ffe72f`) was checked by an adversarial "
      "checker, who re-ran it, re-derived its counts by other methods and returned 9 findings plus a list of "
      "missed items. Code (the fixer) applied every finding that its own tool runs confirmed; none was rejected. "
      "Each disposition below carries this run's evidence. "
      + (f"{len(lnc)} commit(s) landed on top of the base after the builder's run: "
         + "; ".join(f"{lab_} ({', '.join('`' + c[:10] + '`' for c in cs_)})" for lab_, cs_ in (
             ("from the concurrent PROPOSAL-m session (G-CAL, step 6; subjects beginning `m package` / `G-CAL`)", lnc_m),
             ("this audit's own (subjects beginning `AUDIT-note-release`)", lnc_a),
             ("other", lnc_o)) if cs_) + ". "
         if lnc else "")
      + (f"This run is pinned at `{head[:10]}` (`--pin`); the live HEAD was `{V['head_live'][:10]}`. "
         if V["a"].pin else f"This run scans the state at `{head[:10]}`. ")
      + f"The `at base` figures (base `{since[:10]}`, the builder's and the checker's commit) are the total minus "
        "the new-since column, which makes them directly comparable with the checker's numbers.")
    w("")

    def port_line(k):
        v, ex = by_key.get(k, (None, None))
        if ex is None:
            return f"`#{k}`: NOT FOUND in this run's exact recount"
        src_new = len(ex.get("sources_new", ()))
        at_base = ex["n_occ"] - ex["n_occ_new"]
        src_base = len(ex["sources"]) - src_new
        ck = CHECKER_PORTS.get(k)
        base_head = ex["n_occ_base_head"] if base_known else ex["n_occ_head"]
        base_locs = ex["base_head_locators"] if base_known else ex["head_locators"]
        agree = ck and at_base == ck[0] and src_base == ck[1] and base_head == ck[2] and \
            (ck[3] is None or ck[3] in base_locs)
        return (f"`{red_port(v)}`: {ex['n_occ']} occ in {len(ex['sources'])} sources now ({ex['n_occ_new']} in "
                f"{src_new} new sources), HEAD {ex['n_occ_head']} ({', '.join(ex['head_locators']) or '-'}); at base "
                f"{at_base} in {src_base}, base HEAD {base_head} ({', '.join(base_locs) or '-'}); checker "
                f"{ck[0]} in {ck[1]}, HEAD {ck[2]}{(' (' + ck[3] + ')') if ck[3] else ''}: "
                f"{'AGREES' if agree else 'DIFFERS'}")

    items = []
    # F1
    items.append(("F1 (substantive) -- ssh_port `#25124cd5` reported as 1 occurrence, HEAD 0 (line-scoped count; "
                  "the exact recount skipped the ssh_port class).",
                  "APPLIED. Every SSH port whose individual triage is IDENTIFIER is now re-counted exactly (word-bounded: "
                  "no letter or digit on either side, so a run inside a hex hash or a longer number does not count). "
                  "The identifier table now has an `exact occ / HEAD / new` column for ports, and a new table lists every "
                  "IDENTIFIER value present at HEAD with its locators, for the PI's decision. This run: "
                  + "; ".join(port_line(k) for k in CHECKER_PORTS) + "."))
    # F2
    items.append(("F2 (substantive) -- 'Coverage limits of the fallback, both closed by (i-b)'; '(i-b) covers "
                  "both'; 'incl. `data/m/ckpt/**`'. (i-b) did not scan binary blobs, and no ckpt file was ever "
                  "tracked.",
                  "APPLIED, both remedies. Paths under data/m/ckpt/ ever tracked: "
                  + (f"{len(V['ckpt_paths'])}, so the -diff limit is stated as never having applied. "
                     if not V["ckpt_paths"] else
                     f"0 at rounds 1 and 2 (the -diff limit was stated as never having applied); {len(V['ckpt_paths'])} "
                     f"in this run, so (i-a) now states that it applies and names the commit (see round 3, R3-2). ")
                  + "'incl. data/m/ckpt/**' is removed. A binary-content "
                  f"scan is added: {binc['members']} npz members, dtypes "
                  + ", ".join(f"{k} {n}" for k, n in binc["dtypes"].most_common())
                  + f"; {binc['unicode_members']} unicode members decoded; {binc['ascii_runs']:,} ASCII runs; PNG "
                    f"text-chunk keywords {binc['png_text_keys']}. Hits: precise "
                    f"{sum(len(t) for t in binc['precise'].values())}, identifier "
                    f"{sum(len(t) for t in binc['ids'].values())} ("
                  + (", ".join(f"{cls}: {e['triage'][0]}" for cls, t in binc["ids"].items() for v, e in t.items()) or "-")
                  + f"), context-free {len(binc['cf'])}. The checker "
                    "reported 208 members, 11 unicode members (<U3 x5, <U8 x5, <U16 x1), one tEXt 'Software', and 0 "
                    "hits over 26 patterns."))
    # F3
    sg = V["sig_groups"]
    items.append(("F3 (minor) -- 'SSH key names / fingerprints / public keys 0 / 0 / 0': commit headers were never "
                  "scanned; 7 gpgsig headers embed one ed25519 key.",
                  f"APPLIED. Every commit header ({hdr['n_commit_headers']}) and tag header ({hdr['n_tag_headers']}) "
                  f"is now scanned in its own subsection. Signed commits: {len(hdr['sigs'])}. Distinct keys: "
                  f"{len(sg)} ("
                  + "; ".join(f"{k[1]}, namespace {k[2]}, {k[3]}, fingerprint {red(k[4]) if k[4] else '-'}, "
                              f"{len(s)} commits" for k, s in sg.items())
                  + "). Verdict PUBLIC-KEY, not a credential. The checker reported the same key, SHA2...[len 50]#488bbe90, "
                    "in 7 commits. The '0 / 0 / 0' line is now scoped to blob and message content."))
    # F4
    em_tab = hdr["ids"]["email_address"]
    gm = [(v, e) for v, e in em_tab.items() if v.endswith("@gmail.com")]
    gm_s = "; ".join(f"`{red(v)}` {e['n_occ']} in headers now ({e['n_occ_new']} in new commit headers), at base "
                     f"{e['n_occ'] - e['n_occ_new']}" for v, e in gm)
    items.append(("F4 (minor) -- the tagger of annotated tag cycle-4-close is not enumerated.",
                  "APPLIED. The identities table has a tagger row ("
                  + "; ".join(f"{n_} `{red(e_)}`: {', '.join(hdr['tagger_tags'][(n_, e_)])}" for (n_, e_) in hdr["taggers"])
                  + f"). The address over all headers: {gm_s}. The checker reported 587 = 2 x 293 + 1 at the base."))
    # F5
    tp = ids["local_temp_path ((/private)/tmp, (/private)/var/folders)"]
    cp = ids["claude_projects_path (~/.claude/projects/...)"]
    var_bare = [(v, e) for v, e in tp.items() if v.startswith("/var/folders/")]
    tmp_bare = [(v, e) for v, e in tp.items() if v.startswith("/tmp/")]
    gg = git("grep", "-c", "-E", "(^|[^e])/tmp/", head, check=False).decode("utf-8", "replace").split("\n")
    gg = [l for l in gg if l.strip()]

    def at_base_head(rows):
        """(occurrences, files) in blobs at the base's HEAD; equals the HEAD figures when there is no base."""
        if not base_known:
            return (sum(e["n_occ_head"] for _, e in rows), len({p for _, e in rows for p in e["head_paths"]}))
        return (sum(e.get("n_occ_base_head", 0) for _, e in rows),
                len({p for _, e in rows for p in e.get("base_head_paths", ())}))
    vb_b, tb_b, cp_b = at_base_head(var_bare), at_base_head(tmp_bare), at_base_head(list(cp.items()))
    items.append(("F5 (minor) -- the temp-path class missed temp paths without /private and ~/.claude/projects "
                  "session paths.",
                  f"APPLIED. The class is widened to `(?:/private)?/(?:tmp|var/folders)/...`, with a left boundary "
                  f"(no word character, '.', '-', '/' or '~' before it, so the /tmp inside /private/tmp and "
                  f"relative 'x/tmp/' paths do not count). A class `claude_projects_path` is added. This run: temp "
                  f"paths {len(tp)} distinct, {sum(e['n_occ'] for e in tp.values())} occ, "
                  f"{sum(e['n_occ_head'] for e in tp.values())} at HEAD. Of these, /var/folders without /private: "
                  f"{len(var_bare)} distinct, {sum(e['n_occ_head'] for _, e in var_bare)} at HEAD in "
                  f"{len({p for _, e in var_bare for p in e['head_paths']})} files "
                  f"({', '.join(sorted({p for _, e in var_bare for p in e['head_paths']}))}); at the base's HEAD "
                  f"{vb_b[0]} in {vb_b[1]} files. Bare /tmp/: {len(tmp_bare)} distinct, "
                  f"{sum(e['n_occ_head'] for _, e in tmp_bare)} at HEAD in "
                  f"{len({p for _, e in tmp_bare for p in e['head_paths']})} files; at the base's HEAD {tb_b[0]} in "
                  f"{tb_b[1]} files. ~/.claude/projects: {len(cp)} distinct, "
                  f"{sum(e['n_occ'] for e in cp.values())} occ, {sum(e['n_occ_head'] for e in cp.values())} at HEAD "
                  f"({sum(e['n_occ_new'] for e in cp.values())} new; at the base's HEAD {cp_b[0]}). The checker's comparison command, "
                  f"`git grep -c -E '(^|[^e])/tmp/' {head[:10]}`, gives {sum(int(l.rsplit(':', 1)[1]) for l in gg)} "
                  f"matching lines in {len(gg)} files at this HEAD. It also counts relative 'x/tmp/' paths. The "
                  f"checker reported: /var/folders without /private 4 at HEAD in 2 files, bare /tmp/ about 16 in 13 "
                  f"HEAD files, ~/.claude/projects 4 distinct / 7 history / 5 HEAD."))
    # F6
    items.append(("F6 (minor) -- the reason text for `#f1412386` spells the value out.",
                  f"APPLIED. The reason now reads: '{MANUAL_TRIAGE['f1412386'][1]}'. It does not spell the digits. The "
                  "builder's returned summary sentence is not carried into this raw. Not changed: the loopback "
                  "value's redacted form identifies it (it names no machine). Round 2 changed the port form: "
                  "ports now print as length + sha8 only (see the round-2 list)."))
    # F7
    t2 = [(k, l) for k, l in V["bulk_locs"].items() if k[1].startswith("T2")]
    t1 = sum(c for (n, r), c in V["bulk"].items() if r.startswith("T1"))
    items.append(("F7 (minor) -- 'HF_TOKEN' (twice, in a Hugging Face Hub warning) counted under T1 'LLM-token "
                  "sense'.",
                  "APPLIED. New rule T2 'credential-sense word, no value follows'. A credential-sense word followed "
                  "by '=', ':' or '=>' would go to T3, individual inspection. This run: T2 "
                  + "; ".join(f"{len(l)} ({', '.join(l)})" for _, l in t2)
                  + f", T3 {sum(c for (n, r), c in V['bulk'].items() if r.startswith('T3'))}, T1 {t1}. Verdict unchanged "
                    "(FALSE-POSITIVE: no value follows). The checker's further reading, which Code shares: the "
                    "warning shows those downloads ran without a token."))
    # F8
    items.append(("F8 (minor) -- the 'every scanned ref is an ancestor ... none could block a push' sentence says "
                  "nothing about refs that exist only on GitHub.",
                  f"APPLIED as text. Ancestry was re-verified for the {len(V['refs'])} local refs (all "
                  f"{'yes' if all(V['ancestry'].values()) else 'NOT all'}). The sentence is now scoped to the locally "
                  "visible refs. The PI pre-flip steps under (v) add a re-run at the release commit (step 1) and "
                  "`git ls-remote origin` (step 2). Not run: they need the final HEAD and the network."))
    # F9
    items.append(("F9 (minor, referent) -- the block names N12's output `results/raw/<stamp>_note-N12-scrub.md` "
                  "(:84).",
                  "APPLIED. A referent note in the header names the three N12 raws."))
    # missed list
    hdr_sig_cf = sum(1 for e in hdr["cf"].values() if e["triage"][0] == "SSH-SIGNATURE")
    lower_n = sum(1 for e in cf.values() if e["extra"]["run"] == "lower")
    lower_b = sum(1 for e in cf.values() if e["extra"]["run"] == "lower" and e["n_occ"] - e["n_occ_new"] > 0)
    cf_b = sum(1 for e in cf.values() if e["n_occ"] - e["n_occ_new"] > 0)
    items.append(("Missed: context-free secret scan (checker: 44 distinct, all false positives, among them 8 "
                  "SSH-signature lines; lowercase+digit: 2 macOS temp-dir names).",
                  f"APPLIED. A context-free scan runs over blobs and messages ({len(cf)} distinct: "
                  + ", ".join(f"{k} {n}" for k, n in collections.Counter(e['triage'][0] for e in cf.values()).items())
                  + f"; lowercase+digit runs {lower_n}; present at the base: {cf_b} distinct, of them {lower_b} "
                    f"lowercase+digit), headers ({len(hdr['cf'])} distinct, {hdr_sig_cf} of them "
                    f"SSH-signature lines) and binary content ({len(binc['cf'])}). The counts differ from the checker's "
                    "by design: this scan has no word-segment pre-filter, so every run is counted and triaged, and paths "
                    "are cleared by the triage rather than skipped. No value is a secret."))
    qsa = V["precise"]["quoted_secretish_assignment"]
    items.append(("Missed: extended patterns (JWT, Stripe, Slack/Discord webhooks, SendGrid, Telegram, PyPI/npm, "
                  "ya29, legacy 32-char uppercase RunPod shape, PuTTY, secret-bearing URL query parameters, quoted "
                  "key/secret/password/auth assignments: 40 distinct, all labels).",
                  f"APPLIED. The {N_PRECISE_R1 - N_PRECISE_ORIGINAL} patterns (the PGP block among them) were added to "
                  "(i-b) and run over every source class (round 2 added two more; see R2-6). Hits: "
                  + ", ".join(f"{n} {len(V['precise'][n])}" for n, _, _ in PRECISE[N_PRECISE_ORIGINAL:N_PRECISE_R1])
                  + f". Quoted assignments: {len(qsa)} distinct, {sum(e['n_occ'] for e in qsa.values())} occurrences "
                    f"({sum(1 for e in qsa.values() if e['n_occ'] - e['n_occ_new'] > 0)} distinct present at the "
                    f"base), verdicts "
                  + ", ".join(f"{k} {n}" for k, n in collections.Counter(e['triage'][0] for e in qsa.values()).items())
                  + "."))
    jl = V["jl"]
    items.append(("Missed: content copies of jlens-qwen36 (checker: 37 files under jlens-qwen36/data/ "
                  "byte-identical to tracked blobs, over 520 working-tree files).",
                  f"APPLIED. This run read {jl['files']} files and hashed the {jl['hashed']} whose size matched. Matches: "
                  f"{len(jl['matches'])} -- {len(V['jm_empty'])} empty-blob matches and {len(V['jm_nonempty'])} "
                  f"non-empty, all under the clone's data/, {len(V['jm_code'])} outside it. The checker's 37 / 520 was "
                  "not reconciled at round 1 (its file list and selection rule were not in its report); round 2 "
                  "settles it: the second checker's independent re-run reproduced 579 / 46 / 42 / 39 (files / "
                  "hashed / matches / non-empty matches) exactly; this run: "
                  f"{jl['files']} / {jl['hashed']} / {len(jl['matches'])} / {len(V['jm_nonempty'])} ("
                  + ("equal" if (jl['files'], jl['hashed'], len(jl['matches']), len(V['jm_nonempty'])) ==
                     (579, 46, 42, 39) else "DIFFERENT: the clone's working tree changed") + "). "
                  "Round 2 also adds the clone-index evidence under (iv), which is what supports the conclusion: no "
                  "upstream jlens code, LICENSE, README or data is tracked."))
    items.append(("Missed: remote-only refs (`git ls-remote origin` before the flip).",
                  "APPLIED as the PI pre-flip step 2 (see F8)."))
    un = V["unreach"]
    items.append(("Missed: local unreachable objects (checker: 16 blobs and 1 commit).",
                  "APPLIED. This run: " + (", ".join(f"{k} {n}" for k, n in sorted(un.items())) or "none")
                  + f" ({V['unreach_bytes']:,} bytes) of {V['n_store']} objects in the store. They are not pushed."))
    co = V["cont"]
    items.append(("Missed: 'continuity' over history (checker: 948 occurrences in 25 files; 'continuity password' 3 "
                  "times, no value follows).",
                  f"APPLIED. This run: {co['occ']} occurrences in {co['sources']} sources (every blob version and "
                  f"message; {len(co['paths'])} distinct paths), {co['head_occ']} at HEAD; at base "
                  f"{co['occ'] - co['occ_new']} occurrences in {len(co['paths_base'])} distinct paths. The phrase "
                  f"occurs {len(co['phrases'])} times, followed by a value "
                  f"{sum(x['value_follows'] for x in co['phrases'])} times. Distinct paths at base "
                  f"{len(co['paths_base'])} against the checker's 25 files. Occurrences at base "
                  f"{co['occ'] - co['occ_new']} against the checker's 948: a gap of {co['occ'] - co['occ_new'] - 948}. "
                  f"Code did not reproduce it: a word-bounded count gives {co['occ_word']} (total) against the "
                  f"substring count's {co['occ']}, and 'discontinuity' occurs {co['occ_dis']} times. The checker's "
                  "counting rule is not in its report."))
    items.append(("Missed: tagger identity; HF_TOKEN; temp paths; headers; ports; binary contents.",
                  "See F4, F7, F5, F3, F1 and F2."))
    for i, (claim, disp) in enumerate(items, 1):
        w(f"{i}. **{claim}** {disp}")
    w("")
    w("Checker's verdict summary, unchanged by these fixes: no secret in the history, and none of the builder's "
      "pass or STOP lines needed to change. The two statements it called wrong (F1, F2) are corrected above.")
    values_check_r2(w, V)


def values_check_r2(w, V):
    """Round 2: the second checker's findings on the round-1 fixer's outputs, each with its disposition and this
    run's evidence; plus the routing's two further directions."""
    head, since = V["head"], V["since"]
    w("")
    w("## Values-check, round 2")
    w("")
    w("The round-1 fixer's outputs (script sha256 `4f5859c5...723e`, md `4008afec...f5f4`, json "
      "`dc73e0c8...58f4`, all at `bab921ce52`) were checked by a second adversarial checker. It re-ran the script "
      "(identical apart from the stamp and the command line), found the redaction clean in all three files, "
      "re-derived the counts by other methods, and returned 7 findings (1 substantive, 6 minor) plus 8 missed "
      "items. Dispositions below; each carries this run's evidence. Actions: FIXED, DEFERRED (to another item), "
      "DISCLOSED.")
    w("")
    pend, pend_known = V["pend"], V["pend_known"]

    def pend_line(files):
        out = []
        for r_ in pend:
            if r_["file"] in files:
                out.append(f"`{r_['file']}`: " + (", ".join(f"`{show(pend_known.get(v, ()), v)}` x{n_}"
                                                             for v, n_ in r_["known"].most_common()) or "clean"))
        missing = [f for f in files if f not in {r_["file"] for r_ in pend}]

        def committed(f):
            """Round 5: a file no longer pending because it is committed -- the history scan covers it; the known
            sensitive values (exact recount) at HEAD in it are counted from their HEAD locators."""
            n_ = sum(1 for v, ex_ in V["exact"].items() if v in pend_known
                     for loc_ in ex_["head_locators"] if loc_.rsplit(":", 1)[0] == f)
            return (f"`{f}`: committed (tracked at HEAD, so the history scan above covers it; exact-recounted "
                    f"sensitive values in it at HEAD: {n_})")
        return "; ".join(out + [committed(f) if f in V["m"]["head_files"] else f"`{f}`: not present"
                                for f in missing])
    n13 = ["results/raw/2026-10-08_note-N13-provenance.md", "results/raw/2026-10-08_note-N13-provenance.json"]
    others = [r_ for r_ in pend if pending_group(r_["file"]).startswith("other") and r_["known"]]
    items = []
    items.append(("R2-1 (substantive) -- N13's pending raw quotes the full RunPod pod id `uimu...[len 14]#a39ed293` "
                  "(N13 md:643, json:8321/8410/8916); this part's scope (history at bab921ce52) cannot see it.",
                  "DEFERRED to item N13 -- its files are N13's, and this part edits only its own. Kept here as a "
                  "pre-release check, as routed: 'every audit raw must be re-scanned before the release commit'. "
                  "Built: the new pre-release section reads every file not yet in history (untracked, non-ignored, "
                  "or modified) and scans it for every sensitive value of this run, for new id-shaped values and for "
                  "the precise patterns; pre-flip step 1 is now worded as a precondition of the end commit and the "
                  "tag, not as advice (binding it is the PI's call). This run's snapshot for N13: "
                  f"{pend_line(n13)}. The checker's six non-audit files with "
                  "the volume or pod id: this run finds "
                  + (", ".join(f"`{r_['file']}`" for r_ in others) or "none")
                  + f" ({len(others)} file(s) in the 'other' group with a sensitive value); they matter only if "
                    "committed."))
    items.append(("R2-2 (minor) -- '1,793,055 lines' for `git log -p --all` is one too high.",
                  f"FIXED. The count is now the newline count: {V['logp_nl']:,} lines over {len(V['logp']):,} bytes "
                  f"(the stream ends with a newline: {'yes' if V['logp_ends_nl'] else 'no'}). Round 1 printed the "
                  "length of `split(b'\\n')`, which also counts the empty piece after the final newline. The "
                  "grep's line numbers and the locator index are unaffected."))
    sa = V["scan_av"]
    items.append(("R2-3 (minor) -- 'not installed (and were not installed), so the block's fallback applies' is "
                  "imprecise: block :77 runs the fallback only if the scanners are not installable.",
                  "FIXED (wording and evidence). `which`: "
                  + ", ".join(f"{t_} {'found' if p_ else 'not found'}" for t_, p_ in sa["which"].items())
                  + f"; Homebrew present (`{sa['brew']}`); its local formula index (`{sa['cache']}`, cached "
                    f"{sa.get('cache_date')}, read as a file) lists "
                  + ", ".join(f"{n_} {d_['version']} ({d_['license']}), bottle for `{sa['bottle_tag']}`: "
                              f"{'yes' if d_['bottle_for_this_platform'] else 'no'}" for n_, d_ in sa["formulae"].items())
                  + ". So both are installable here and were not installed, because the PI's routing forbids "
                    "installs without the PI's word. (i-a) now says plainly that the block's primary scanners have "
                    "NOT been run over this history, that running the fallback instead is a deviation from :77, and "
                    "that the fallback plus Code's blob-level scans stand in for them; PI pre-flip step 4 gives "
                    "the scanner commands."))
    jx = V["jidx"]
    items.append(("R2-4 (minor) -- the jlens 'no code, LICENSE or README is tracked' claim rested on a "
                  "working-tree comparison, which cannot see clone-tracked files whose working copies carry "
                  "local patches.",
                  ("FIXED. (iv) now reads the clone's index as a plain file (no git process in the clone): "
                   f"version {jx.get('version')}, checksum {'verified' if jx.get('checksum_ok') else 'NOT verified'}, "
                   f"{jx.get('entries')} entries, {jx.get('nonempty_entries')} non-empty; non-empty index blob shas "
                   f"reachable in the lab's history: {len(jx.get('nonempty_reachable_in_lab', []))}; clone-tracked "
                   f"files differing on disk: {len(jx.get('modified_on_disk', []))} ("
                   + ", ".join(f"`{p_}`" for p_ in jx.get("modified_on_disk", [])) + "); of the "
                   f"{len(V['jm_nonempty'])} non-empty byte-identical files, clone-tracked: "
                   f"{len(jx.get('matched_files_clone_tracked', []))}; the clone's tracked `data/` paths: "
                   + ", ".join(f"`{p_}`" for p_ in jx.get("data_entries", []))
                   + ". All agree with the checker (62 entries; 0 reachable; none of the 39 clone-tracked; 2 "
                     ".gitkeep and 2 lens fit logs under data/). Round-1 item 12 now records that the second "
                     "checker reproduced 579 / 46 / 42 / 39, which settles the first checker's 37 / 520.")
                  if jx.get("present") else "NOT DONE: the clone's index is absent on this machine."))
    jv = V["jv"]
    fa = jv["float_arrays"]
    items.append(("R2-5 (minor) -- (iv)'s 'no model weights or residual arrays beyond the allowlisted .npz' "
                  "missed residual-space vectors stored as JSON.",
                  f"FIXED. Every reachable JSON / JSONL / .ipynb blob ({jv['blobs']}; parsed {jv['parsed']}) is "
                  f"walked for all-numeric arrays of 256+ elements. Float arrays: {len(fa)}: "
                  + "; ".join(f"`{', '.join(x['paths'])}` `{x['pointer']}` {x['length']} (blob `{x['blob'][:8]}`, "
                              f"{'at HEAD' if x['at_head'] else 'history only'})"
                              for x in sorted(fa, key=lambda x: (x['paths'], x['pointer'])))
                  + f". Integer-only arrays of that size: {jv['int_arrays']}. (iv) names the two files and restates "
                    "the clause exactly: a stored logistic readability probe (weights, and the per-dimension mean "
                    "and sd of its residual-space training features), not model weights and not raw captures. The "
                    "checker reported the same two files, blobs 6454940d and ab57d21c, 3 x 5120 floats each."))
    hdr = V["hdr"]
    al_ = hdr["armor_lines"]
    alb = {k: v for k, v in al_.items() if v[1] <= 4.3}
    b64s = hdr["b64stats"]
    km = {n_: (len(V["precise"][n_]), len(hdr["precise"][n_]), len(V["binc"]["precise"][n_]))
          for n_ in sorted(KEY_MATERIAL_PATTERNS)}
    items.append(("R2-6 (minor) -- the 4.3 bits/char bar misses structured base64 (7 of 15 gpgsig armor lines); "
                  "no base64 key-material marker patterns.",
                  f"FIXED. Stated in (i-b) with this run's numbers: armor body lines of 16+ characters {len(al_)}, "
                  f"at or below 4.3: {len(alb)}"
                  + (f" (entropy {min(v[1] for v in alb.values())}-{max(v[1] for v in alb.values())})" if alb else "")
                  + f"; strict-base64 runs of 64+ characters in blobs and messages {len(b64s['runs64'])}, at or "
                    f"below 4.3: {len(b64s['runs64_below'])}. Two marker patterns added (precise patterns "
                    f"{N_PRECISE_R1 + 1}-{len(PRECISE)}): "
                  + "; ".join(f"{n_}: blobs/messages {a_}, headers {b_}, binary content {c_}"
                              for n_, (a_, b_, c_) in km.items())
                  + ". Header hits sit inside the gpgsig signatures and are triaged SSH-SIGNATURE (round 2 said the "
                    "marker was the signer's public key blob; round 3 corrected the mechanism: it is the key-type "
                    "string that opens the signature field -- see R3-3); a hit anywhere else would be UNTRIAGED and "
                    "hold (i) PENDING. The checker "
                    "reported 15 / 7 (3.98-4.15), 5 mixed-case base64 runs of 64+ none below (its alphabet and "
                    "boundaries are not in its report; this run's strict definition is stated in (i-b)), and 0 "
                    "markers outside the 7 signature headers."))
    rl = V["reflogs"]
    items.append(("R2-7 (minor) -- the pre-flip list omits GitHub-side surfaces that the visibility change "
                  "publishes.",
                  "FIXED. Pre-flip step 3 lists pull requests (titles, bodies, comments, review comments), issues, "
                  "Actions runs, logs and artifacts, the wiki, releases and their assets, and commits force-pushed "
                  "away from another machine that GitHub can keep reachable by sha or through `refs/pull/*`. "
                  "The local evidence is now in (v), from the remote-tracking reflogs: "
                  + "; ".join(f"`{r_['ref']}` {r_['entries']} entries, all fast-forward: "
                              f"{'yes' if r_['all_fast_forward'] else 'NO'}" for r_ in rl["remote"])
                  + (f"; first push {rl['first_push']['time']} at `{rl['first_push']['commit']}`" if rl["first_push"] else "")
                  + "; " + ("; ".join(f"unreachable commit `{u_['commit']}` at {u_['committer_time']}, before the first "
                                     f"push: {'yes' if u_['before_first_push'] else 'NO'}, in a remote reflog: "
                                     f"{'YES' if u_['in_remote_reflogs'] else 'no'}, replaced by "
                                     + (", ".join(f"`{t_['commit']}` {t_['seconds_after']} s later"
                                                  for t_ in u_["reachable_twin_same_parent_and_subject"]) or "-")
                                     for u_ in rl["unreachable_commits"]) or "no unreachable commit")
                  + ". The checker reported 249 entries, no force-push, first push 2026-07-18 00:17 (-0400) at "
                    "dfe2503, and 2591567 replaced 14 s later by 8aa3ba1 before any push."))
    hp = V["hp_out"]
    items.append(("Missed (informational) -- `/Users/` paths at HEAD and the notebook's kernel display name "
                  "disclose another local project's conda env name and the Jupyter runtime directory.",
                  f"ADDED as one informational line in (ii): {sum(hp['kinds'].values())} outside-repository "
                  f"`/Users/` occurrences by kind; the env name (redacted) in "
                  + "; ".join(f"{len(hp['env_files'].get(nm, {}))} HEAD files" for nm in hp["env_names"])
                  + ". Nothing to fix before release."))
    short = sorted(SHORT_SHOWN)
    short_ids = sorted({v for cls, tab in V["ids"].items() if cls != PORT_CLASS for v, e in tab.items()
                        if len(v) <= 4 and v in SHORT_SHOWN})
    short_rest = [s_ for s_ in short if s_ not in short_ids]
    md_sofar = "\n".join(V["L"])
    old_port_forms = re.findall(r"(?<![0-9A-Za-z])\d{4}\.\.\.\[len [45]\]", md_sofar)
    n_port_vals = len(V["ids"][PORT_CLASS])
    n_port_r5 = sum(1 for v in V["ids"][PORT_CLASS] if sha256_hex(v.encode())[:16] in TRIAGE16)
    items.append(("Missed (informational) -- the prescribed form prints values of 4 characters or fewer in full "
                  "and 4 of 5 digits of a port.",
                  f"FIXED for ports, by the routing's direction: every one of the {n_port_vals} SSH-port-class values "
                  "(real ports, process ids, a token-window length, a local viewer port"
                  + (f"; round 5: {n_port_r5} fallback-grep hit-line count(s)" if n_port_r5 else "") + ") now prints as "
                  "`lenN:hhhhhhhh` -- no digit -- in the md and the JSON; old-form port strings left in the md "
                  f"before this section: {len(old_port_forms)}. DISCLOSED for the rest: values of 4 characters or "
                  f"fewer that the generic form prints in full: {len(short)} distinct. In the identifier tables: "
                  f"{len(short_ids)} ("
                  + (", ".join(f"`{red(s_, sensitive=False)}`" for s_ in short_ids) or "none")
                  + ": the synthetic RUNPOD_POD_ID test value, FALSE-POSITIVE). The other "
                  f"{len(short_rest)} are in the JSON's `fallback.credential_shaped` records only -- the word or code "
                  "token after a key such as `token:` (a prose word, a label, a code fragment), each cleared by its "
                  "value class; none is a credential. No sensitive value is short enough to reach the generic form "
                  "in full: the script refuses to redact a sensitive value of 4 characters or fewer."))
    items.append(("Missed -- pending audit outputs; scanners; clone index; JSON vectors; structured base64; "
                  "GitHub surfaces.", "See R2-1, R2-3, R2-4, R2-5, R2-6 and R2-7."))
    nc = V["new_commits"]
    items.append(("Routing -- cover the commits after bbc9ffe up to the current HEAD.",
                  f"DONE. This run scans HEAD `{head[:10]}` (pinned at start; refs at end "
                  f"{'MOVED' if V['refs_moved'] else 'unchanged'}), which includes the {len(nc)} commit(s) after "
                  f"`{since[:10]}`: " + (", ".join(f"`{c[:10]}`" for c in nc) or "none")
                  + ". Every table's `new since base` column counts them. The final re-run at the release commit "
                    "is still required (pre-flip step 1)."))
    for i, (claim, disp) in enumerate(items, 1):
        w(f"{i}. **{claim}** {disp}")
    w("")
    w("Second checker's verdict, unchanged by these fixes: no secret in the history; no pass or STOP line "
      "changes. (i) stays STOP pending the PI on the block's literal text, and now also records that the "
      "primary scanners were not run; (v) PASS; (iv)-mechanical passes and names the two JSON probe files.")
    values_check_r3(w, V)


# The third checker's stated figures (strict check of the round-2 fixer's outputs at bab921ce52, plus a scratch
# re-run at cf8eb5b9dd), quoted so this run can compare against them. Redacted keys only.
R3_CHECKER = {
    "volname_key": "e6c48186", "volname_occ_r2": 83, "volname_src_r2": 83, "volname_blobs_r2": 82,
    "volname_msgs_r2": 1, "volname_locs_r2": ["RESULTS.md:9624", "results/raw/2026-08-22_podprep.txt:6"],
    "cf8": "cf8eb5b9dd", "volname_locs_cf8": ["RESULTS.md:9919", "results/raw/2026-08-22_podprep.txt:6"],
    "cf8_commits": 307, "cf8_blobs": 1181, "cf8_hit_lines": 7782, "cf8_token": (7440, 8154), "cf8_sk": (287, 297),
    "cf8_logp_lines": 1798487, "cf8_logp_bytes": 70058328, "cf8_new_quoted_fp": 1, "cf8_email_hdr": 593,
    "r2_email_hdr": 591, "sig_raw_len": 173, "sig_offsets": ((14, "public-key"), (90, "signature")),
    "sig_marker_line": 2,
    # (prefix of the class label, candidates, expected chance matches) as the checker rounded them
    "exposure": (("runpod_volume_id", 2.18e9, 0.5), ("container_hostname", 4.29e9, 1.0),
                 ("runpod_pod_id", None, 8.5e5)),
}


def values_check_r3(w, V):
    """Round 3: the third checker's findings on the round-2 fixer's outputs, each with its disposition and this
    run's evidence; plus the routing's direction (re-run at the current HEAD; name cf8eb5b)."""
    head, since, m = V["head"], V["since"], V["m"]
    exact, ids, hdr = V["exact"], V["ids"], V["hdr"]
    C = R3_CHECKER
    w("")
    w("## Values-check, round 3")
    w("")
    w("The round-2 fixer's outputs (script sha256 `2b72c9ad...9c6c`, md `401d4631...3e3e`, json "
      "`a26505a0...c927`, all at `bab921ce52`) were checked by a third, strict checker. It re-ran the script at "
      "`bab921ce52` (md identical apart from the stamp line, the command echo, the pre-release snapshot stamp and "
      "the order of 4 tied categories in one sentence; JSON apart from its stamps and the excluded-path list), "
      "found the redaction clean in all three files, re-derived the counts, re-ran the script in scratch at "
      "`cf8eb5b9dd`, and returned 6 findings (1 substantive, 5 minor). Dispositions below, then Code's own addition "
      "and the routing's direction; each carries this run's evidence. Actions: FIXED, TRIAGED, DONE.")
    w("")

    def same_blob(c1, c2, path):
        a_ = git("rev-parse", "--verify", "-q", f"{c1}:{path}", check=False).decode().strip()
        b_ = git("rev-parse", "--verify", "-q", f"{c2}:{path}", check=False).decode().strip()
        return bool(a_) and a_ == b_
    cf8_full = git("rev-parse", "--verify", "-q", C["cf8"] + "^{commit}", check=False).decode().strip()
    at_cf8 = bool(cf8_full) and head == cf8_full
    r2_objs = {l.split(" ", 1)[0] for l in git("rev-list", "--objects", R2_HEAD).decode("utf-8", "replace").split("\n")
               if l.strip()}
    items = []

    # R3-1 volume name
    vtab = ids[VOLNAME_CLASS]
    vd_ = collections.Counter(e["triage"][0] for e in vtab.values())
    names = [v for v, e in vtab.items() if e["triage"][0] == "IDENTIFIER"]
    parts = []
    for v in names:
        ex = exact.get(v)
        if not ex:
            parts.append(f"`{show(VOLNAME_CLASS, v)}`: NOT in the exact recount")
            continue
        bs = ex.get("by_source", collections.Counter())
        occ_r2 = sum(c_ for (k_, s_), c_ in bs.items() if s_ in r2_objs)
        src_r2 = sum(1 for (k_, s_) in bs if s_ in r2_objs)
        blobs_r2 = sum(1 for (k_, s_) in bs if s_ in r2_objs and k_ == "blob")
        msgs_r2 = src_r2 - blobs_r2
        base_locs = ex["base_head_locators"] if m.get("base_objs") is not None else ex["head_locators"]
        loc_same_r2 = all(same_blob(since, R2_HEAD, l_.rsplit(":", 1)[0]) for l_ in C["volname_locs_r2"])
        loc_same_cf8 = bool(cf8_full) and all(same_blob(head, cf8_full, l_.rsplit(":", 1)[0])
                                              for l_ in C["volname_locs_cf8"])
        agree_r2 = (vkey(v) == C["volname_key"] and (occ_r2, src_r2, blobs_r2, msgs_r2) ==
                    (C["volname_occ_r2"], C["volname_src_r2"], C["volname_blobs_r2"], C["volname_msgs_r2"]))
        agree_locs_r2 = loc_same_r2 and sorted(base_locs) == sorted(C["volname_locs_r2"])
        agree_locs_cf8 = loc_same_cf8 and sorted(ex["head_locators"]) == sorted(C["volname_locs_cf8"])
        pend_files = [r_["file"] for r_ in V["pend"] if v in r_["known"]]
        stem_files = [r_["file"] for r_ in V["pend"] if any(V["vol_stems"].get(k_) == v for k_ in r_["known"])]
        in_head_table = bool(ex["n_occ_head"] or ex["n_occ_base_head"])
        parts.append(
            f"`{show(VOLNAME_CLASS, v)}`: exact, word-bounded {ex['n_occ']} occ in {len(ex['sources'])} sources "
            f"({sum(1 for k_, _ in ex['sources'] if k_ == 'blob')} blob versions + "
            f"{sum(1 for k_, _ in ex['sources'] if k_ != 'blob')} message(s)) now, {ex['n_occ_new']} new since the base, "
            f"{ex['n_occ'] - ex['n_occ_new']} at the base; at the round-2 snapshot `bab921ce52` {occ_r2} in {src_r2} "
            f"({blobs_r2} + {msgs_r2}) against the checker's {C['volname_occ_r2']} in {C['volname_src_r2']} "
            f"({C['volname_blobs_r2']} + {C['volname_msgs_r2']}): {'AGREES' if agree_r2 else 'DIFFERS'}. HEAD "
            f"{ex['n_occ_head']} ({', '.join(ex['head_locators']) or '-'}); at the base `{since[:10]}` "
            f"{ex['n_occ_base_head']} ({', '.join(base_locs) or '-'}); the checker's locators at `bab921ce52` "
            f"({', '.join(C['volname_locs_r2'])}; those files' blobs equal at the base and at `bab921ce52`: "
            f"{'yes' if loc_same_r2 else 'NO'}): {'AGREES' if agree_locs_r2 else 'DIFFERS'}"
            + (f"; its locators at `{C['cf8']}` ({', '.join(C['volname_locs_cf8'])}; those files' blobs equal at "
               f"this HEAD and `{C['cf8']}`: {'yes' if loc_same_cf8 else 'NO'}): "
               f"{'AGREES' if agree_locs_cf8 else 'DIFFERS'}" if cf8_full else "")
            + f". In the 'Identifiers present at HEAD' table: {'yes' if in_head_table else 'NO'}. In the pre-release "
              f"sensitive set: {'yes' if v in V['pend_known'] else 'NO'}, with its stem: "
              f"{'yes' if v in V['vol_stems'].values() else 'NO'}; pending files carrying the name: "
              f"{len(pend_files)}, the stem alone: {len(stem_files)} (checker: 0 in the 60 then pending). In the leak "
              f"assertion's set, the name: {'yes' if v in REDACTED_SENSITIVE else 'NO'}, the stem: "
              f"{'yes' if v in V['vol_stems'].values() and any(V['vol_stems'][k_] == v and k_ in REDACTED_SENSITIVE for k_ in V['vol_stems']) else 'NO'}.")
    items.append(("R3-1 (substantive) -- the RunPod network-volume NAME is in the record and the raw never finds it; "
                  "it is not in the pre-release sensitive set, so pre-flip step 1 could not catch a pending audit raw "
                  "quoting it.",
                  "FIXED. New identifier class `" + VOLNAME_CLASS + "` (pattern under (ii); two alternatives: a "
                  "word-joined name ending in `_volume`/`-volume`, or a word-joined name of 3+ parts directly before a "
                  "size in GB/TB, the volume listing's name column), exactly re-counted, triaged by hash, and added to "
                  "the pre-release scan's new-value classes (whose group selection now matches the history scan's). "
                  f"This run: {len(vtab)} distinct values in the class ("
                  + (", ".join(f"{k_} {n_}" for k_, n_ in most_common_sorted(vd_)) or "-")
                  + "".join(f"; FALSE-POSITIVE `{show(VOLNAME_CLASS, v_, sensitive=e_['triage'][2])}`: "
                            f"{e_['triage'][1]}" for v_, e_ in vtab.items() if e_["triage"][0] == "FALSE-POSITIVE")
                  + "). "
                  + (" ".join(parts) if parts else "No IDENTIFIER value found: the class does NOT reproduce the "
                                                   "checker's finding.")
                  + " The checker also reported no RunPod pod names in the record; this run adds no pod-name class "
                    "and does not re-derive that."))

    # R3-2 HEAD moved; -diff path tracked
    ck = V["ckpt_ev"]
    q_new = [(v_, e_) for v_, e_ in V["precise"]["quoted_secretish_assignment"].items()
             if e_["n_occ_new"] and e_["n_occ"] == e_["n_occ_new"]]
    q_new_vd = collections.Counter(e_["triage"][0] for _, e_ in q_new)
    al, ao = V["alt_lines"], V["alt_occ"]
    figs_now = {"commits": len(m["commits"]), "blobs": len(m["blobs"]), "hit_lines": len(V["grep_lines"]),
                "token": (al["token"], ao["token"]), "sk": (al["sk-[A-Za-z0-9]"], ao["sk-[A-Za-z0-9]"]),
                "logp_lines": V["logp_nl"], "logp_bytes": len(V["logp"])}
    figs_ck = {"commits": C["cf8_commits"], "blobs": C["cf8_blobs"], "hit_lines": C["cf8_hit_lines"],
               "token": C["cf8_token"], "sk": C["cf8_sk"], "logp_lines": C["cf8_logp_lines"],
               "logp_bytes": C["cf8_logp_bytes"]}
    items.append(("R3-2 (minor) -- HEAD moved: the concurrent session committed `cf8eb5b9dd` after the round-2 run; "
                  "it adds the first tracked file under `data/m/ckpt/`, so the limit the raw said had never applied "
                  "now applies, and the committed raw does not cover the current HEAD.",
                  f"FIXED: regenerated at the current HEAD `{head[:10]}` (refs at end "
                  f"{'MOVED' if V['refs_moved'] else 'unchanged'}), which includes the {len(V['new_commits'])} "
                  f"commit(s) after the base: " + ", ".join(f"`{c_[:10]}`" for c_ in V["new_commits"])
                  + f". Paths under `data/m/ckpt/` ever tracked: {len(V['ckpt_paths'])} ("
                  + (", ".join(f"`{p_}` first added by `{(c_ or '?')[:10]}`" for p_, c_ in ck["introduced"].items())
                     or "none")
                  + f"); `Binary files ... differ` lines for them in the `git log -p` stream: {ck['logp_binary_lines']}; "
                    "their blobs read by (i-b): "
                  + (", ".join(f"`{b_['blob'][:8]}` ({b_['bytes']:,} bytes; scanned as text: "
                               f"{'yes' if b_['scanned_as_text_in_i_b'] else 'NO'}; lines matching the fallback's "
                               f"pattern, invisible to the fallback: {b_['fallback_pattern_lines']})" for b_ in ck["blobs"])
                     or "none")
                  + " (checker: a direct grep of the ckpt blob for the fallback pattern gave 0). (i-a)'s coverage "
                    "limit (2) now says the limit applies and names the commit; PI pre-flip step 1 cites "
                  + (", ".join(f"`{c_[:10]}`" for c_ in V["ckpt_after_r2"]) or "no commit (none landed after the "
                                                                                     "round-2 snapshot)")
                  + " as the evidence that a snapshot goes stale and the re-run at the release commit is needed. "
                  + ("This run is at `" + C["cf8"] + "`, the checker's scratch run's commit; its figures against "
                     "the checker's: " + "; ".join(f"{k_} {figs_now[k_]} vs {figs_ck[k_]} "
                                                    f"({'AGREES' if figs_now[k_] == figs_ck[k_] else 'DIFFERS'})"
                                                    for k_ in figs_now)
                     if at_cf8 else
                     f"This run is not at `{C['cf8']}` (HEAD moved on), so the checker's figures there are not "
                     "compared; this run: " + "; ".join(f"{k_} {figs_now[k_]}" for k_ in figs_now))
                  + f". Quoted-assignment values new since the base (absent at the base): {len(q_new)} ("
                  + (", ".join(f"{k_} {n_}" for k_, n_ in most_common_sorted(q_new_vd)) or "-")
                  + f"; checker at `{C['cf8']}`: {C['cf8_new_quoted_fp']} FALSE-POSITIVE"
                  + ("".join(f"; `{red(v_, sensitive=e_['triage'][2])}` at {e_['first']}: {e_['triage'][1]}"
                             for v_, e_ in q_new))
                  + "). Code's addition at this HEAD"
                  + (": the new value is a 64-hex sha256 under the key `key_set_sha256` (added by `cf8eb5b9dd`), "
                     "which Code's first run at this HEAD, before the fix, cleared by the label rule with the reason "
                     "'a label built of words and short tokens'; a hex-digest rule now runs before the label rule and "
                     "states what the value is (verdict unchanged). "
                     if any(e_["triage"][1].startswith("a hex digest") for _, e_ in q_new) else
                     ": none (no new hex-digest value). ")
                  + f"TRUE-SECRET-CANDIDATE {len(V['true_candidates'])}, UNTRIAGED {len(V['untriaged_precise'])}."))

    # R3-3 SSH-signature mechanism
    sigs = [ps_ for _, ps_ in hdr["sigs"] if "keytype_strings" in ps_]
    kt_sets = collections.Counter(tuple(ps_["keytype_strings"]) for ps_ in sigs)
    lens_ = collections.Counter(ps_["raw_len"] for ps_ in sigs)
    mk_lines = collections.Counter(tuple(ps_["marker_body_lines"]) for ps_ in sigs)
    line1 = {ps_["body_lines_sha8"][0] for ps_ in sigs if ps_["body_lines_sha8"]}
    mline_vals = {ps_["body_lines_sha8"][i - 1] for ps_ in sigs for i in ps_["marker_body_lines"]}
    reasons = sorted({e_["triage"][1] for n_ in KEY_MATERIAL_PATTERNS for e_ in hdr["precise"][n_].values()
                      if e_["triage"][0] == "SSH-SIGNATURE"})
    ck_offs = tuple(C["sig_offsets"])
    agree_sig = (len(kt_sets) == 1 and tuple((o, f) for o, _, f in next(iter(kt_sets))) == ck_offs
                 and set(lens_) == {C["sig_raw_len"]} and set(mk_lines) == {(C["sig_marker_line"],)}
                 and len(line1) == 1 and len(mline_vals) == len(sigs))
    items.append(("R3-3 (minor) -- the SSH-SIGNATURE reason says the marker comes from the embedded PUBLIC key blob; "
                  "it comes from the signature field's key-type string.",
                  f"FIXED. The reason is now computed from each signature's byte layout (parse under (i-b) headers). "
                  f"This run: {len(sigs)} SSH signatures, raw length "
                  + ", ".join(f"{k_} bytes x{n_}" for k_, n_ in sorted(lens_.items()))
                  + "; key-type string occurrences (byte, byte mod 3, field): "
                  + "; ".join(f"{list(k_)} x{n_}" for k_, n_ in sorted(kt_sets.items()))
                  + "; marker in armor body line(s) "
                  + ", ".join(f"{list(k_)} x{n_}" for k_, n_ in sorted(mk_lines.items()))
                  + f"; armor body line 1 (the one carrying the public key) distinct across the {len(sigs)}: "
                    f"{len(line1)}; the marker line's distinct values: {len(mline_vals)}. So the 3-aligned key-type "
                    "string is the one that opens the signature field (followed there by the signature bytes); the "
                    "public key's own key-type string is not 3-aligned and does not encode to the marker. Checker: "
                    f"{C['sig_raw_len']} bytes; offsets 14 (public key; 14 mod 3 = 2) and 90 (signature; aligned); "
                    f"armor line {C['sig_marker_line']}, 7 distinct; line 1 identical in all 7: "
                  + ("AGREES" if agree_sig else "DIFFERS")
                  + ". The reason now reads: '" + (" | ".join(reasons) or "-") + "'. Round 2's disposition R2-6 is "
                    "annotated with the correction. Verdict unchanged: signature material, not a credential."))

    # R3-4 pre-release split
    a_hits, b_only = V["audit_hits"], V["audit_ident_only"]
    ihd = V["ident_hdr_occ"]
    em_occ = [n_ for v_, n_ in ihd.items() if v_.endswith("@gmail.com")]
    items.append(("R3-4 (minor) -- the NOT CLEAN line puts a real redaction breach (N13's full pod id) on the same "
                  "footing as the author's own email, which is public in the commit headers and outside the routing's "
                  "redaction rule.",
                  "FIXED. The pre-release line is split: redaction-rule values (RunPod pod/volume ids, the volume name "
                  "and its stem, SSH ports, the signing-key fingerprint, the container hostname, the Claude session "
                  "link, the pass-phrase-shaped value), a new value needing triage or an uncleared precise hit -- NOT "
                  "CLEAN, a blocker as drafted; and the commit identities' own metadata (the identity emails -- the "
                  "author's and the Claude Cowork tool identity's -- and the laptop hostname, all public in the commit "
                  "headers) -- listed for consistency with this raw's own redaction, not a routing violation, not a "
                  "blocker as drafted (binding either is the PI's call). Pre-flip step 1, the summary and the JSON "
                  "(`audit_files_not_clean`, `audit_files_author_identity_only`) follow the split. This run: "
                  f"redaction-rule group {len(a_hits)} audit file(s)"
                  + (" (" + ", ".join(f"`{r_['file']}`" for r_ in a_hits) + ")" if a_hits else "")
                  + f"; author-identity-only {len(b_only)}"
                  + (" (" + ", ".join(f"`{r_['file']}`" for r_ in b_only) + ")" if b_only else "")
                  + ". The author's address occurs in "
                  + (", ".join(str(n_) for n_ in em_occ) or "-")
                  + " author/committer/tagger header lines"
                  + (f" (checker: {C['cf8_email_hdr']} at `{C['cf8']}`, {C['r2_email_hdr']} at `bab921ce52`: "
                     + ("AGREES" if em_occ == [C["cf8_email_hdr"]] else "DIFFERS") + ")" if at_cf8 else "")
                  + "."))

    # R3-5 tie order
    items.append(("R3-5 (minor) -- not byte-reproducible beyond the stamps: the order of tied categories in the "
                  "pre-release sentence changes from run to run (a Counter's most_common() over values whose "
                  "insertion order came from a hash-ordered set).",
                  "FIXED at the root and at the display. The exact recount now walks its classes in ID_PATTERNS order "
                  "(exact_recount_classes()) instead of the set's per-process hash order, so every structure built "
                  "from it -- the pre-release sensitive set, the JSON's `identifiers_exact_recount` -- has a fixed "
                  "order; and the sentence sorts ties by label (most_common_sorted()). Code's check of this script "
                  "version before this run: two scratch runs under PYTHONHASHSEED=0 and PYTHONHASHSEED=1, started "
                  "together, give an md identical apart from the stamp lines and the command echo, and a JSON "
                  "identical apart from its two stamps and the excluded-path list (which echoes --out). A run made at "
                  "another moment -- this one included -- can also differ in the pre-release snapshot, because other "
                  "sessions write the pending files concurrently; that is the snapshot, not the order."))

    # R3-6 caveat
    er = V["exp_rows"]

    def row_fig(prefix):
        for (lab_, kind_, alph, hid), vs in er.items():
            if lab_.startswith(prefix) and kind_ == "brute":
                cand = alph ** hid
                return f"{alph}^{hid} = {cand:.2e} candidates, ~{cand / 2 ** 32:.2g} chance matches ({len(vs)} value(s))"
        return "not in the sensitive set"

    def row_agrees(prefix, ck_cand, ck_chance):
        """Within 5% of the checker's rounded figures (its 0.5 is a one-digit rounding, so 10% there)."""
        for (lab_, kind_, alph, hid), vs in er.items():
            if lab_.startswith(prefix) and kind_ == "brute":
                cand = alph ** hid
                ch = cand / 2 ** 32
                ok_c = ck_cand is None or abs(cand - ck_cand) <= 0.05 * ck_cand
                ok_h = abs(ch - ck_chance) <= (0.1 if ck_chance < 1 else 0.05) * ck_chance
                return ok_c and ok_h
        return False
    exp_agree = all(row_agrees(p_, c_, h_) for p_, c_, h_ in C["exposure"])
    items.append(("R3-6 (minor) -- the enumeration caveat is understated: besides 5-digit ports, the volume id and "
                  "the container hostname are recoverable by enumeration from their redacted forms.",
                  "FIXED. The header's caveat is now computed per sensitive value (hidden characters of the class's "
                  "own alphabet, candidates, expected chance matches against the 32-bit prefix), adds the word-built "
                  "values (the volume name, the pass-phrase-shaped value, the identity emails and the laptop hostname: "
                  "open to a word-list search whatever their length), and states that every one of these values is "
                  "in the history being published, so the form protects only this raw, not the release. This run: "
                  f"volume id {row_fig('runpod_volume_id')}; container hostname {row_fig('container_hostname')}; pod "
                  f"ids {row_fig('runpod_pod_id')}; SSH ports {row_fig(PORT_CLASS)}. Checker: volume id 2.18e9 "
                  "candidates / ~0.5 chance matches, container hostname 4.29e9 / ~1, pod ids ~8.5e5 chance matches: "
                  + ("AGREES (within its rounding)" if exp_agree else "DIFFERS") + "."))

    # Code's addition: the pre-release scan's fail-safe, met once in this round
    n_new_port = sum(1 for r_ in V["pend"] for c_, _, _ in r_["new"] if c_ == PORT_CLASS)
    items.append(("Code's addition -- pending files written by another session during this round put counts on "
                  "lines the SSH-port rule reads.",
                  "TRIAGED, by a rule. A run of this round refused to write: the pending N16 decoding raw had gained "
                  "table lines whose only port word is 'port' in \"adapter port of e2a's rule\" (a code port), with "
                  "counts of rounds and seed streams on them; the pre-release scan held such a count as an untriaged "
                  "port-line number and redacted it, and the same number occurs in this raw as an ordinary count, so "
                  "the leak assertion stopped the write. A later run met two more counts on the same kind of line. "
                  "Code read the lines, and every 'port of' in the history is the software sense too; so a line "
                  "whose every ssh/port/alias match is the word 'port' in 'port of' is no longer read as a port line, "
                  "in the history scan and in the pending scan alike (pattern note under (ii)). History: "
                  f"{CODE_PORT_STATS['history_lines']} such line(s) carrying {CODE_PORT_STATS['history_numbers']} "
                  "4-5 digit number(s) -- no history count changes. This snapshot's pending files: "
                  f"{CODE_PORT_STATS['pending_lines']} such line(s) carrying {CODE_PORT_STATS['pending_numbers']} "
                  f"number(s), now skipped; new port-line numbers in pending files still needing triage: {n_new_port}. "
                  "Residual risk: a network port written 'port of <host>' on a line with no 'ssh', 'alias' or '-p' "
                  "would be skipped too. The pre-release section states the leak assertion's fail-safe."))

    # routing
    items.append(("Routing -- re-run at the current HEAD and name cf8eb5b (data/m/ckpt -diff paths now tracked) as "
                  "evidence for pre-flip step 1.",
                  f"DONE. This run's HEAD: `{head[:10]}`"
                  + (" (the commit the routing names)" if at_cf8 else
                     f" (later than `{C['cf8']}`: HEAD moved on)" if cf8_full and is_ancestor(cf8_full, head) else "")
                  + "; the commit that first added a `data/m/ckpt/` path: "
                  + (", ".join(f"`{c_[:10]}`" for c_ in sorted({c_ for c_ in ck["introduced"].values() if c_})) or "none")
                  + "; named in (i-a)'s coverage limit (2) and in PI pre-flip step 1. Every locator stays pinned to "
                    f"the base `{since[:10]}` in the 'at base' columns; the HEAD columns are this run's HEAD."))
    for i, (claim, disp) in enumerate(items, 1):
        w(f"{i}. **{claim}** {disp}")
    w("")
    st_i = "STOP pending the PI (literal :77)" if V["grep_lines"] else "no fallback hits"
    st_v = "PASS" if V["max_blob"] <= 100 * MB else "STOP"
    w(f"Third checker's verdict, re-checked on this run: (i) {st_i}; (v) {st_v}; (iv)-mechanical: jlens paths ever "
      f"tracked {len(V['jlens_hist'])}, npz without an explicit line {len(V['no_line'])}, weight-shaped paths "
      f"{len(V['weights'])}. No finding changes a pass or STOP line; the redaction stays clean (the leak assertion "
      "now also covers the volume name and its stem).")
    values_check_r4(w, V)


# The fourth checker's stated figures (its check of the round-3 fixer's outputs at cf8eb5b9dd), quoted so this run
# can compare against them. Redacted keys only.
R4_CHECKER = {
    "r3_script": "a775a7d8...09f6", "r3_md": "b226587f...f126", "r3_json": "4cc884b5...30dc", "r3_head": "cf8eb5b9dd",
    # finding 1: class -> (summed, distinct) as the checker counted them
    "class_src": {VOLNAME_CLASS: (147, 84), "runpod_pod_id (context: pod)": (223, 145), "url_host": (72, 24),
                  "ipv4_address": (14, 14)},
    "volname_both": 63,
    # finding 2
    "tool_key": "84cbedd5", "tool_occ": 63, "tool_src": 63, "tool_intro": "e256c4f", "tool_locs_cf8": "RESULTS.md:8530-8534",
    # finding 3
    "hex_key": "422c647a", "hex_occ": 2, "hex_src": 2, "hex_pending": 0,
    # finding 4: pending-file email addresses the checker found (the service address; the author's identity address)
    "email_identity_key": "bb973c14",
}


def values_check_r4(w, V):
    """Round 4: the fourth checker's findings on the round-3 fixer's outputs, each with its disposition and this
    run's evidence."""
    head, ids, exact, m = V["head"], V["ids"], V["exact"], V["m"]
    C = R4_CHECKER
    # round 5: the checker counted at its snapshot (C["r3_head"]); when this run is at a later HEAD, its figures are
    # compared with the counts restricted to the sources reachable from that snapshot (as round 3 does for R3-2),
    # and this run's own figures are printed beside them
    snap_full = git("rev-parse", "--verify", C["r3_head"] + "^{commit}").decode().strip()
    moved = snap_full != head and is_ancestor(snap_full, head)
    snap = ({l_.split(" ", 1)[0] for l_ in git("rev-list", "--objects", snap_full).decode("utf-8", "replace").split("\n")
             if l_.strip()} if moved else None)

    def at_snap(srcs):
        return {x for x in srcs if x[1] in snap} if moved else set(srcs)
    w("")
    w("## Values-check, round 4")
    w("")
    w(f"The round-3 fixer's outputs (script sha256 `{C['r3_script']}`, md `{C['r3_md']}`, json `{C['r3_json']}`, "
      f"all at `{C['r3_head']}`) were checked by a fourth checker. It returned 4 findings, all minor (a column "
      "definition, a triage reason's wording, and two latent gaps in the pre-release scan; by its account the "
      "verdicts, the STOP and pass lines and the exact counts stand), and no item open from round 3. Dispositions "
      "below; each carries this run's evidence. Actions: FIXED.")
    w("")
    items = []

    # R4-1: the class table's src column
    rows_ = []
    agree1 = []
    snap_fig = []
    for cls, (u_, s_) in V["id_class_src"].items():
        if u_ != s_:
            rows_.append(f"{cls.split(' (')[0]} {s_} summed / {u_} distinct")
        if cls in C["class_src"]:
            tab_ = ids[cls]
            s_s = sum(len(at_snap(e["sources"])) for e in tab_.values())
            u_s = len(set().union(*(at_snap(e["sources"]) for e in tab_.values()))) if tab_ else 0
            agree1.append(C["class_src"][cls] == (s_s, u_s))
            snap_fig.append(f"{cls.split(' (')[0]} {s_s} / {u_s}")
    vt_ = ids[VOLNAME_CLASS]
    both_ = (set.intersection(*(at_snap(e["sources"]) for e in vt_.values())) if len(vt_) == 2 else set())
    u_v, s_v = V["id_class_src"][VOLNAME_CLASS]
    items.append(("R4-1 (minor) -- the class table's `src` column is defined as 'distinct blobs/messages', but each "
                  "class row added up its values' own source counts (the volume-name row: 147).",
                  "FIXED by computing the union: a class row's `src` is now the number of distinct blobs/messages "
                  "holding any of the class's values, and the definition says so (value rows unchanged: each "
                  "value's own sources). Class rows whose two counts differ in this run: "
                  + ("; ".join(rows_) or "none") + ". The volume-name row: " f"{s_v} summed, {u_v} distinct; sources "
                  f"holding both of its values: {len(both_)}. The checker's figures (volume name 147 / 84, held by "
                  f"both {C['volname_both']}; pod ids (context) 223 / 145; url_host 72 / 24; ipv4 14 / 14)"
                  + (f", against this run's counts restricted to the sources reachable from the checker's snapshot "
                     f"`{C['r3_head']}` ({'; '.join(snap_fig)}; held by both {len(both_)}; round 5: this run is at a "
                     f"later HEAD, whose new commits add sources)" if moved else "") + ": "
                  + ("AGREES" if agree1 and all(agree1) and len(both_) == C["volname_both"] else "DIFFERS")
                  + ". The JSON carries both counts per class (`identifier_class_sources`). The class rows' `src` "
                    "figures appear nowhere else in the raw (round 3's md: each only in its table row)."))

    # R4-2: the tool name's reason
    tool = next((v for v in vt_ if vkey(v) == C["tool_key"]), None)
    if tool is None:
        items.append(("R4-2 (minor) -- the reason for `update-network-volume` misdescribes its prose.",
                      "NOT FOUND in this run's volume-name class; nothing to reword."))
    else:
        e_ = vt_[tool]
        blob_src = sorted(s_ for k_, s_ in e_["sources"] if k_ == "blob")
        n_nonblob = sum(1 for k_, _ in e_["sources"] if k_ != "blob")
        names_ = [v for v, x in vt_.items() if x["triage"][0] == "IDENTIFIER"]
        name_rx = re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(re.escape(v) for v in names_) + r")(?![A-Za-z0-9])") \
            if names_ else None
        kinds_, n_lines, with_name, moved, grows, dc = set(), 0, 0, 0, 0, 0
        for _, _, data in cat_batch(blob_src):
            tl = data.decode("utf-8", "replace").split("\n")
            for i_, ln in enumerate(tl):
                if tool not in ln:
                    continue
                n_lines += 1
                kinds_.add(sha256_hex(ln.encode()))
                with_name += bool(name_rx and name_rx.search(ln))
                moved += "cannot be moved" in ln
                grows += i_ + 1 < len(tl) and "grows only" in tl[i_ + 1]
                dc += any("datacenter" in x for x in tl[max(0, i_ - 3):i_])
        ex = exact.get(tool, {})
        bs_ = ex.get("by_source", collections.Counter())
        occ_s = sum(n_ for k_, n_ in bs_.items() if not moved or k_[1] in snap)
        src_s = sum(1 for k_ in bs_ if not moved or k_[1] in snap)
        items.append(("R4-2 (minor) -- MANUAL_TRIAGE `84cbedd5` (`update-network-volume`): the verdict is right, but "
                      "the reason says 'in prose about renaming the volume'; the prose says a network volume cannot "
                      "be moved, because the tool only renames and grows it.",
                      "FIXED: the reason now reads '" + e_["triage"][1] + "' (the round-3 disposition R3-1 above, "
                      "regenerated, carries the new wording). Evidence, this run: the value occurs "
                      f"{e_['n_occ']} times in {len(e_['sources'])} sources ({len(blob_src)} blob versions, "
                      f"{n_nonblob} messages); lines carrying it {n_lines}, distinct line texts {len(kinds_)}; of "
                      f"them carrying 'cannot be moved' {moved}, followed by a line with 'grows only' {grows}, with "
                      f"'datacenter' in the 3 lines before {dc}; lines also carrying the volume name {with_name}. "
                      f"First locator {e_['first']}; at HEAD {', '.join(ex.get('head_locators', [])) or '-'}. The "
                      f"checker: {C['tool_occ']} occurrences in {C['tool_src']} sources, introduced by "
                      f"`{C['tool_intro']}`, at `{C['r3_head']}` {C['tool_locs_cf8']}"
                      + (f", against this run's exact count restricted to the sources reachable from that snapshot "
                         f"({occ_s} occurrences in {src_s} sources; round 5: this run is at a later HEAD)" if moved else "")
                      + ": "
                      + ("AGREES" if ((occ_s, src_s) if moved else (e_["n_occ"], len(e_["sources"]))) ==
                         (C["tool_occ"], C["tool_src"]) and e_["first"].startswith(C["tool_intro"]) else "DIFFERS")
                      + ". Verdict unchanged: FALSE-POSITIVE."))

    # R4-3: hex-only values and the label rule
    def syn(n_):
        i_ = 0
        while True:
            v_ = sha256_hex(f"N12-history round-4 synthetic {i_}".encode())
            if re.search(r"[a-f]{3}", v_[:32]):
                return v_[:n_]
            i_ += 1
    def r3_verdict(v_, ln_):
        """Round 3's triage_precise replayed for a hex-only quoted value that holds a letter (the rules before the
        digest rule clear no such value): the digest rule, then the old label rule."""
        if re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", v_):
            km = re.search(r"([\w\-]+)['\"]?\s*[:=]\s*['\"]" + re.escape(v_), ln_ or "")
            if km and re.search(r"(?i)sha|hash|digest", km.group(1)):
                return "FALSE-POSITIVE (hex digest)"
        if not has_random_segment(v_) and len(re.findall(r"[A-Za-z]{3,}", v_)) >= 1:
            return "FALSE-POSITIVE (label rule)"
        return "UNTRIAGED"
    cases = [("32-hex under `secret`", syn(32), 'secret = "{v}"'),
             ("40-hex under `api_key`", syn(40), '"api_key": "{v}"'),
             ("64-hex, no line (the pending scan's old call)", syn(64), None),
             ("64-hex under `key_set_sha256`", syn(64), '"key_set_sha256": "{v}"'),
             ("64-hex under `password_sha256`", syn(64), '"password_sha256": "{v}"')]
    res_ = []
    for lab_, v_, ln_ in cases:
        line_ = ln_.format(v=v_) if ln_ else ""
        t_ = triage_precise("quoted_secretish_assignment", v_, line_, "synthetic")
        res_.append(f"{lab_}: round 3 {r3_verdict(v_, line_)}, now {t_[0]}"
                    + (" (hex digest)" if "hex digest" in t_[1] else ""))
    hexh = collections.Counter()
    hexv = []
    for tabs_ in (V["precise"], V["hdr"]["precise"], V["binc"]["precise"]):
        for nm_ in ("quoted_secretish_assignment", "url_secret_query_param"):
            for v_, e2 in tabs_.get(nm_, {}).items():
                if re.fullmatch(r"[0-9a-fA-F]+", v_):
                    hexh[e2["triage"][0]] += 1
                    hexv.append((v_, e2))
    labelled = sum(1 for tabs_ in (V["precise"], V["hdr"]["precise"], V["binc"]["precise"])
                   for nm_ in ("quoted_secretish_assignment", "url_secret_query_param")
                   for e2 in tabs_.get(nm_, {}).values() if e2["triage"][1].startswith("a label built"))
    qd_ = collections.Counter(e2["triage"][0] for e2 in V["precise"]["quoted_secretish_assignment"].values())
    pend_hex = collections.Counter()
    for r_ in V["pend"]:
        pend_hex.update(r_["hex_quoted"])
    agree3 = (len(hexv) == 1 and vkey(hexv[0][0]) == C["hex_key"] and hexv[0][1]["n_occ"] == C["hex_occ"]
              and len(hexv[0][1]["sources"]) == C["hex_src"] and sum(pend_hex.values()) == C["hex_pending"])
    items.append(("R4-3 (minor) -- the hex-digest rule fixed `key_set_sha256`, but the label rule still clears any "
                  "hex-only value holding a run of 3 letters a-f, whatever its key (has_random_segment exempts "
                  "hex-only segments), and in the pending scan the digest rule could never fire (it passed line=\"\").",
                  "FIXED, both parts. (1) In triage_precise a hex-only value that the hex-digest rule does not clear is "
                  "now UNTRIAGED (STOP until triaged), and the label rule needs a run of 3+ letters with a letter "
                  "outside a-f (the fix's two alternatives, both applied; the first more strictly than written: a "
                  "hex-only value under a key that names a hash but is not 40 or 64 hex is UNTRIAGED too). Code's "
                  "addition: the digest rule no longer "
                  "applies under a key that also names a password, secret or credential (the hash of a secret is "
                  "derived from it). (2) pending_scan passes each match's own line, as the history scan does. Synthetic "
                  "hex values (prefixes of the sha256 of a fixed label, chosen to hold a run of 3 letters a-f; "
                  "reproducible; not printed), round 3's rules replayed against this run's: "
                  + "; ".join(res_) + ". This run over every precise table (blobs/messages, headers, binary content): "
                  f"hex-only quoted values {len(hexv)} ("
                  + (", ".join(f"`{show(None, v_, sensitive=e2['triage'][2])}` {e2['triage'][0]}, {e2['n_occ']} occ in "
                               f"{len(e2['sources'])} sources" for v_, e2 in hexv) or "-")
                  + f"); values the label rule clears {labelled}, none hex-only; quoted_secretish_assignment verdicts "
                  + (", ".join(f"{k_} {n_}" for k_, n_ in most_common_sorted(qd_)) or "-")
                  + " (round 3's raw: FALSE-POSITIVE 41), so no verdict changes. Pending files: hex-only quoted values "
                  + (", ".join(f"{k_} {n_}" for k_, n_ in most_common_sorted(pend_hex)) or "0")
                  + f". The checker: one hex-only quoted value in history (`#{C['hex_key']}`, {C['hex_occ']} occ in "
                  f"{C['hex_src']} sources), {C['hex_pending']} in the pending files: "
                  + ("AGREES" if agree3 else "DIFFERS") + ". A pre-flip re-run that meets a hex-only value now stops "
                  "on it instead of clearing it."))

    # R4-4: third-party personal data in the pending scan
    em_ = collections.defaultdict(collections.Counter)
    for r_ in V["pend"]:
        for k_, n_ in r_["emails"].items():
            em_[r_["file"]][k_] += n_
    new_em = [(r_["file"], v_) for r_ in V["pend"] for c_, v_, _ in r_["new"] if c_ == "email_address"]
    idk = {vkey(v_) for v_ in V["pend_known"] if "identity email, public in the commit headers" in V["pend_known"][v_]}
    items.append(("R4-4 (minor) -- the pre-release CLEAN line and pre-flip step 1 rest on a scan that has no class "
                  "for third-party personal data (PENDING_ID_CLASSES has no email_address), while the identity line "
                  "says the routing's redaction rule covers it.",
                  "FIXED, both remedies. `email_address` is now one of the pending scan's new-value classes: an address "
                  "other than the service address (exempt) and the commit identities' own (in the known set) is a new "
                  "value, UNTRIAGED until Code reads it, and in an audit file it holds the redaction-rule line NOT "
                  "CLEAN. The pre-release section, the CLEAN line and pre-flip step 1 now say that this is the scan's "
                  "only class of third-party personal data (a name, a postal address or a phone number is not scanned "
                  "for). This run's snapshot: files with an email address "
                  f"{len(em_)}: "
                  + ("; ".join(f"`{f_}` " + ", ".join(f"{k_} {n_}" for k_, n_ in sorted(c_.items()))
                               for f_, c_ in sorted(em_.items())) or "-")
                  + f"; new (third-party) addresses {len(new_em)}"
                  + (" (" + ", ".join(f"`{f_}`" for f_, _ in new_em) + ")" if new_em else "")
                  + ". This part's own md and JSON are excluded from the pending scan (the leak assertion covers "
                    "them; the service address is printed verbatim by design). The checker: the service address and "
                    f"the author's identity address `#{C['email_identity_key']}` only, no third-party address: "
                  + ("AGREES" if not new_em and C["email_identity_key"] in idk else "DIFFERS") + "."))
    for i, (claim, disp) in enumerate(items, 1):
        w(f"{i}. **{claim}** {disp}")
    w("")
    st_i = "STOP pending the PI (literal :77)" if V["grep_lines"] else "no fallback hits"
    st_v = "PASS" if V["max_blob"] <= 100 * MB else "STOP"
    w(f"Fourth checker's findings, re-checked on this run: (i) {st_i}; (v) {st_v}; TRUE-SECRET-CANDIDATE "
      f"{len(V['true_candidates'])}, UNTRIAGED {len(V['untriaged_precise'])}. No finding changes a pass or STOP "
      "line, and no history verdict changes; the pre-release scan is stricter (hex-only values, email addresses).")


def guard_summary(R, res, aux, outputs, known):
    """Round 5: the data the round-5 section and the JSON's `guard` print (booleans, counts, labels, redacted forms
    and 16-hex keys only -- no control value)."""
    cands, ref, why, ex, base = aux
    md_, js_ = outputs["md"], outputs["json"]

    def nverb(v, t_):
        return len(re.findall(r"(?<![A-Za-z0-9])" + re.escape(v) + r"(?![A-Za-z0-9])", t_)) if v in t_ else 0
    by_key = {}
    for v in set(R) | set(cands):
        k_ = sha256_hex(v.encode())[:16]
        if k_ in TRIAGE16:
            by_key[k_] = v
    t16 = []
    for k_, (vd_, rs_, sens_, src_) in TRIAGE16.items():
        v = by_key.get(k_)
        classes = sorted({r_[1] for r_ in R.get(v, ())}) if v is not None else []
        is_port = PORT_CLASS in classes
        form = (red_port(v, sensitive=sens_) if is_port else red(v, sensitive=sens_)) if v is not None else None
        t16.append({"prefix16": k_, "form": form, "classes": [c_.split(" (")[0] for c_ in classes],
                    "verdict": vd_, "reason": rs_, "source": src_, "in_this_run": v is not None,
                    "run_verdicts": sorted({r_[2] for r_ in R.get(v, ())}) if v is not None else [],
                    "verbatim_md": nverb(v, md_) if v is not None else 0,
                    "verbatim_json": nverb(v, js_) if v is not None else 0,
                    "guard": ("refused: " + why[v]) if v in ref else ("exempt" if v in ex else "not a candidate")})
    sh_rows = collections.Counter()
    for v, recs in R.items():
        for r_ in recs:
            if r_[0] == "shape16":
                sh_rows[r_[4]] += 1
    groups = collections.OrderedDict()
    for (p_, k_, h_), (vd_, rs_) in SHAPE_TRIAGE16.items():
        g_ = groups.setdefault((p_, k_, vd_, rs_), {"entries": 0, "rows_this_run": 0})
        g_["entries"] += 1
        g_["rows_this_run"] += sh_rows.get((p_, k_, h_), 0)
    return {
        "policy": {"exempt_verdicts": list(GUARD_EXEMPT_VERDICTS), "refuse_verdicts": list(GUARD_REFUSE_VERDICTS),
                   "redaction_rule_classes": [c_.split(" (")[0] for c_ in REDACTION_RULE_CLASSES],
                   "safe_verbatim": len(SAFE_VERBATIM), "known_min_substring": KNOWN_MIN_SUBSTR,
                   "mechanical_verdict_exempts_generated_segment": False,
                   "digest_run_min": 8},
        "counts": {"candidates": len(cands), "refused": len(ref), "exempt": len(ex), "known": len(known),
                   "exempt_explicit": sum(1 for v in ex if ex[v] != ("SAFE-VERBATIM",) and
                                          all(r_[3] for r_ in R.get(v, ()))),
                   "exempt_mechanical_only_outside_rule_classes": sum(
                       1 for v in ex if ex[v] != ("SAFE-VERBATIM",) and not all(r_[3] for r_ in R.get(v, ()))),
                   "refused_by_reason": dict(most_common_sorted(collections.Counter(why[v] for v in ref))),
                   "exempt_by_verdicts": dict(most_common_sorted(collections.Counter("/".join(ex[v]) for v in ex))),
                   "leaks": len(base)},
        "triage16": t16,
        "shape16": [{"path": p_, "key": k_, "verdict": vd_, "reason": rs_, **g_}
                    for (p_, k_, vd_, rs_), g_ in groups.items()],
        "shape16_rows_this_run": sum(sh_rows.values()),
        "controls": res,
    }


def values_check_r5(w, C, G):
    """Round 5 (2026-10-09): the guard fix -- the change, the triage additions, the positive controls and their
    results. G is the guard summary of the outputs that print it (iterated to a fixed point)."""
    w("")
    w("## Values-check, round 5: guard fix (2026-10-09)")
    w("")
    if G is None:
        w("(pending: the guard summary is computed on the outputs that print it)")
        return
    c_, ct_ = G["counts"], G["controls"]
    vi_, v_ = ct_["vi_round4_rule"], ct_["v_without_round5_triage"]
    w("**The problem.** At a HEAD that holds this audit's own committed raws and scripts (`09c3a8c` and after), the "
      "round-4 script exited 1 and wrote nothing: its leak assertion refused on every value it printed in redacted "
      "form with the sensitive flag, and generic tokens that this raw itself writes -- class labels, pattern text, "
      "triage reasons, prose -- had entered history as values with `09c3a8c` (the pre-flip raw, "
      "`results/raw/2026-10-08_note-N12-preflip.md@02b6a61` section 3(a): 19 entries, 12 distinct values, at "
      "`6485da2`; the script's verdicts for 8 of them were UNTRIAGED). Replayed on this run's outputs (this file and its JSON), the "
      f"round-4 rule finds {vi_['entries']} entries, {vi_['distinct']} distinct values; under round 5 they are exempt "
      f"{vi_['exempt_now_by_explicit_entry'] + vi_['exempt_now_by_mechanical_verdict']} ("
      + (", ".join(f"{k_} {n_}" for k_, n_ in sorted(vi_["by_exempt_verdict"].items())) or "-")
      + f"): by an explicit hash-keyed entry {vi_['exempt_now_by_explicit_entry']}, by a mechanical verdict "
      f"{vi_['exempt_now_by_mechanical_verdict']}; refused {vi_['refused_now']}.")
    w("")
    w("**The change.** (1) Explicit triage: `TRIAGE16` (value triage keyed by the first 16 hex of sha256(value); "
      f"{len(TRIAGE16)} entries) and `SHAPE_TRIAGE16` (the credential-shaped fallback rows, keyed by path, key and "
      f"the value's 16-hex prefix; {len(SHAPE_TRIAGE16)} entries), both in the script; `manual()` reads `TRIAGE16` "
      "before `MANUAL_TRIAGE`, and the fallback loop reads `SHAPE_TRIAGE16` before both. (2) The leak guard is "
      "verdict-based (as amended by the second check, below). Its candidates are every value printed in redacted "
      "form with the sensitive flag; every known sensitive value (the pre-release section's set: RunPod ids and "
      "volume name with its stem, SSH ports, the container hostname, the session link, the pass-phrase-shaped value, "
      "the identity emails other than the service address, the laptop hostname, the signing-key fingerprint; plus "
      "the session link's bare id); and every value of this run's tables, printed or not, that has a verdict other "
      "than " + " / ".join(GUARD_EXEMPT_VERDICTS) + " (credential-shaped rows included, whose values round 4 never "
      "guarded), a mechanical record of a redaction-rule class, or a mechanical verdict on a value with a "
      "generated-looking segment. It refuses to write if any candidate appears in this file or its JSON, unless the "
      "value is exempt: one of the " + str(G["policy"]["safe_verbatim"]) + " values printed verbatim by policy (the "
      "service address and the synthetic tool-identity domain); or every verdict it receives is "
      + " / ".join(GUARD_EXEMPT_VERDICTS) + ", it is not a known sensitive value, it carries none inside it (in any "
        "case or separator variant) and no session link, every record of it in a redaction-rule class ("
      + ", ".join(dict.fromkeys(G["policy"]["redaction_rule_classes"]))
      + ") comes from an explicit hash-keyed entry, and so does every record of a value with a generated-looking "
        "segment (a segment of 10 or more characters that mixes letters and digits and is not hex: the shape of a "
        "generated key, and also of an OS temp-folder or tempfile name) -- a mechanical verdict exempts neither. "
        "Refused always: " + " / ".join(GUARD_REFUSE_VERDICTS) + ", any other verdict (METADATA, METADATA-ECHO, "
        "PUBLIC-KEY, SSH-SIGNATURE), and a redacted value with no verdict. Matching: a known value of "
      + str(G["policy"]["known_min_substring"]) + " or more characters is found as a plain substring, "
        "case-insensitively, with any interior run of `-`, `_`, space or `.` in it matching any run of those (or tabs) "
        "or none; an "
        "all-digit known value (an SSH port) digit-bounded, so a port glued to letters is found, except inside a run "
        "of 8 or more hex characters (a digest, such as this raw's sha8 forms, where a port's digits can occur by "
        "chance); every other refused value of " + str(G["policy"]["known_min_substring"]) + " or more characters "
        "as a plain substring; a shorter one word-bounded, as round 4 matched. Its message lists every refused entry "
        "by redacted form, sorted (round 4 printed the first 10 in set order, with context). (3) Positive controls, "
        "below, run before every write; `--selftest` runs them alone and writes nothing. The redacted-form policy "
        "for everything printed is unchanged. (4) Found while re-reading this raw -- text that the audit's own "
        "commits made stale; no guard change: (a) the `/Users/` per-file note for code labelled every code file "
        "without the synthetic fixture user 'a real absolute path in code', and the recommendation after it said "
        "'the code hit is a test fixture' whatever the notes said; the note now classifies each occurrence by the "
        "path segment after `/Users/` (empty, pattern text or the fixture user names no home directory) and the "
        "recommendation is computed from the notes (this run's code files with `/Users/`: "
        + str(C["code_users_files"]) + ": "
        + (", ".join(f"{k_} {n_}" for k_, n_ in sorted(C["code_users_kinds"].items())) or "none")
        + "; 'real' = names a user directory); (b) the round-1 values-check called every commit after the base the "
          "PROPOSAL-m session's; it now attributes each by its subject; (c) round 4 compared the fourth checker's "
          "figures, counted at its snapshot, with this run's totals, so a later HEAD read DIFFERS for sources the "
          "new commits add; it now compares counts restricted to the sources reachable from that snapshot, as round "
          "3 does, and prints both; (d) R2-9's list of what the port-class values are names the round-5 counts; (e) "
          "R2-1's N13 line said 'not present' for N13's raws, which are no longer pending because they are committed; "
          "it now says so and counts the exact-recounted sensitive values in them at HEAD.")
    w("")
    w(f"This run: candidates {c_['candidates']}, refused set {c_['refused']} ("
      + ", ".join(f"{k_} {n_}" for k_, n_ in c_["refused_by_reason"].items()) + f"), exempt {c_['exempt']} ("
      + ", ".join(f"{k_} {n_}" for k_, n_ in c_["exempt_by_verdicts"].items()) + f"; every record explicit "
      f"{c_['exempt_explicit']}, at least one mechanical verdict -- outside the redaction-rule classes and without a "
      f"generated-looking segment, by the rule -- {c_['exempt_mechanical_only_outside_rule_classes']}); refused "
      f"values found in the outputs: {c_['leaks']}.")
    w("")
    src_n = collections.Counter(e_[3] for e_ in TRIAGE16.values())
    w(f"**Triage additions, `TRIAGE16`** ({len(TRIAGE16)} values). By source: "
      + "; ".join(f"\"{md_escape(k_)}\" {n_}" for k_, n_ in most_common_sorted(src_n))
      + ". 'pre-flip' = `results/raw/2026-10-08_note-N12-preflip.json@02b6a61` (`history.full_leak_list`, its "
        "section 3(a), and `new_values_detail`, its section 3(c)): the verdict and reason of every value it "
        "triaged are carried verbatim, five reasons that refer to a neighbouring row of its table with their "
        "referent added in square brackets (Code's addition); the four leak-list values the script had already "
        "triaged keep the script's verdict, with a reason of Code's. 'Code, round 5' = values new to triage at this "
        "HEAD: two numbers on a line of `02b6a610`'s commit message and two id-shape sweep tokens first committed in "
        "`09c3a8c` (the pre-flip raw's dump prints no sweep table, so its 3(c) could not list them), each read in "
        "context. Columns: the 16-hex key, the class(es) the value has in this run, its redacted form as this "
      "raw prints it, the verdict, the reason, the source, its verbatim occurrences in this file / its JSON "
      "(word-bounded), and the guard's decision.")
    w("")
    w("| key (16 hex) | class(es) here | form | verdict | reason | source | verbatim md / json | guard |")
    w("|---|---|---|---|---|---|---|---|")
    for x in G["triage16"]:
        w(f"| `{x['prefix16']}` | {', '.join(x['classes']) or '-'} | "
          + (f"`{x['form']}`" if x["form"] else "not in this run") + f" | {x['verdict']} | {md_escape(x['reason'])} | "
          f"{md_escape(x['source'])} | {x['verbatim_md']} / {x['verbatim_json']} | {x['guard']} |")
    w("")
    nt_ = sum(1 for x in G["triage16"] if x["in_this_run"])
    w(f"In this run: {nt_} of {len(TRIAGE16)} values; their verdicts here equal the entries' verdicts: "
      + ("yes" if all(x["run_verdicts"] == [x["verdict"]] for x in G["triage16"] if x["in_this_run"]) else "NO") + ".")
    w("")
    w(f"**Triage additions, `SHAPE_TRIAGE16`** ({len(SHAPE_TRIAGE16)} entries for the pre-flip raw's 128 "
      "credential-shaped rows, `shape_rows_detail`; verdicts and reasons carried verbatim, three entries -- two "
      "reasons -- with a bracketed referent). "
      f"Rows of this run matched by an entry: {G['shape16_rows_this_run']}. Grouped:")
    w("")
    w("| path | key | verdict | reason | entries | rows matched here |")
    w("|---|---|---|---|---|---|")
    for x in G["shape16"]:
        w(f"| `{x['path']}` | `{x['key']}` | {x['verdict']} | {md_escape(x['reason'])} | {x['entries']} | "
          f"{x['rows_this_run']} |")
    w("")
    w("Code re-read every carried value in the committed file that first holds it and every credential-shaped row "
      "at its locator (`09c3a8c`) before carrying its verdict (the 115 N13 provenance rows by rule: each value is a "
      "7- or 8-hex abbreviation whose next line holds the full commit id or sha256 that it abbreviates -- 67 and 48 "
      "rows). Code disagrees with none, so no carried entry is kept UNTRIAGED.")
    w("")
    p_, s_, t_ = ct_["i_pod_id"], ct_["ii_synthetic_untriaged"], ct_["iii_ssh_port"]
    yn = lambda b: "yes" if b else "NO"
    bad = lambda b: "YES" if b else "no"
    w("**Positive controls** (each control value is resolved from this run's tables or generated, held in memory "
      "only, and appears in no file; each is injected on its own line into a copy of this file and, separately, of "
      "its JSON, and the guard is run as a real write would run it):")
    w("")
    w(f"- (i) A real RunPod pod id (one of {p_.get('n_candidates', 0)} in the known set; its verdict here "
      f"{'/'.join(p_.get('verdicts', [])) or '-'}): refused in the md copy {yn(p_.get('md', {}).get('refused'))}, "
      f"in the JSON copy {yn(p_.get('json', {}).get('refused'))}; refused by its own verdict alone, with the known set "
      f"emptied: {yn(p_.get('refused_by_its_verdict_alone'))} ({p_.get('reason_without_known_set')}); verbatim in the "
      f"outputs as written: {bad(p_.get('verbatim_in_outputs_as_written'))}"
      f"; other new refusals from the injection: {p_.get('md', {}).get('other_new_leaks')} / "
      f"{p_.get('json', {}).get('other_new_leaks')}.")
    w(f"- (ii) A synthetic secret-shaped value generated at run time (the `{s_['pattern']}` shape; the pattern "
      f"matches it: {yn(s_['pattern_matches'])}; the script's own triage: {s_['triage']}; absent from this run's "
      f"tables: {yn(not s_['in_this_run_tables'])}), entered as a table value with that verdict: refused in the md "
      f"copy {yn(s_['md']['refused'])}, in the JSON copy {yn(s_['json']['refused'])}; by its verdict alone: "
      f"{yn(s_['refused_by_its_verdict_alone'])} ({s_['reason_without_known_set']}); verbatim in the outputs as "
      f"written: {bad(s_['verbatim_in_outputs_as_written'])}.")
    w(f"- (iii) One of the {t_.get('n_candidates', 0)} SSH ports (its verdict here {'/'.join(t_.get('verdicts', [])) or '-'}): "
      f"refused in the md copy {yn(t_.get('md', {}).get('refused'))}, in the JSON copy "
      f"{yn(t_.get('json', {}).get('refused'))}; by its own verdict alone: {yn(t_.get('refused_by_its_verdict_alone'))} "
      f"({t_.get('reason_without_known_set')}); other new refusals from the injection: "
      f"{t_.get('md', {}).get('other_new_leaks')} / {t_.get('json', {}).get('other_new_leaks')}; verbatim in the "
      f"outputs as written: {bad(t_.get('verbatim_in_outputs_as_written'))}.")
    iv_ = ct_["iv_generic_tokens"]
    w(f"- (iv) The generic tokens pass: of the {iv_['triage16_values_in_run']} `TRIAGE16` values in this run, "
      f"{iv_['triage16_verbatim_in_outputs']} occur verbatim in this file or its JSON, refused {iv_['triage16_refused']}; "
      f"of the {iv_['shape16_values_in_run']} `SHAPE_TRIAGE16` values, {iv_['shape16_verbatim_in_outputs']} occur "
      f"verbatim, refused {iv_['shape16_refused']}. The guard over this file and its JSON as written: "
      f"{'0 refusals' if iv_['guard_passes_outputs'] else 'REFUSED'} (the script writes only if this holds).")
    w(f"- (v) The same outputs with every round-5 entry's verdict read as UNTRIAGED (the triage absent): the guard "
      f"refuses {v_['entries']} entries, {v_['distinct']} distinct values, all of them round-5 values: "
      f"{yn(v_['all_round5_values'])} -- so it is the explicit entries, not a weaker guard, that let them pass.")
    w(f"- (vi) The round-4 rule replayed: {vi_['entries']} entries, {vi_['distinct']} distinct values (above).")
    w(f"- (vii)-(x) The second check's gap cases: below, with the findings they answer (all pass: "
      f"{yn(ct_.get('second_check_all_pass'))}).")
    w("")
    w(f"Controls: {'ALL PASS' if ct_['all_pass'] else 'FAIL'}. A failing control, or any refused value found "
      "verbatim, stops the write.")
    w("")
    u_ = C["untriaged"]
    w("**Untriaged at this run** (all tables): precise, in-context and context-free high-entropy over blobs, "
      f"messages, headers and binary content (the script's own count) {u_['script']}; content identifier classes "
      f"{u_['ids']}; id-shape sweep {u_['sweep']}; credential-shaped fallback rows {u_['shape']}; TRUE-SECRET-CANDIDATE "
      f"{u_['true']}. Files not yet in history (the pre-release section; not history): new values UNTRIAGED "
      f"{u_['pending']}. The fallback grep: {u_['fallback']} hit lines (section (i-a)); its inspection-rule hits "
      "are listed there by locator.")
    values_check_r5_second(w, G)
    w("")
    w(f"This is an interim snapshot at HEAD `{C['head'][:10]}`; pre-flip step 3 still needs the clean run at the "
      "release commit.")


def values_check_r5_second(w, G):
    """Round 5, second check (2026-10-09): the round-5 checker's six findings (all minor; its verdict: the guard is
    safe, no instance of any gap at its HEAD), each with its disposition and this run's evidence."""
    ct_ = G["controls"]
    sc, n_ = ct_.get("second_check", {}), ct_.get("second_check_counts", {})
    vi_ = ct_["vi_round4_rule"]
    yn = lambda b: "yes" if b else "NO"
    no = lambda b: "no" if not b else "YES"

    def inj(k_):
        x_ = sc.get(k_)
        if not x_:
            return "MISSING"
        return (f"refused in the md copy {yn(x_['md'])}, in the JSON copy {yn(x_['json'])} ("
                + "; ".join(x_["reasons"]) + f"); the first round-5 guard refused it: {no(x_['first_round5_guard_refused'])}")
    w("")
    w("### Round 5, second check: the checker's findings and their dispositions")
    w("")
    w("The round-5 checker (adversarial, in memory, at `02b6a610`) found the guard safe -- none of the 14 sensitive "
      "values it resolved from history got through, in 7 contexts each -- and reported six minor findings, four of "
      "them latent gaps with no instance at its HEAD. Each is applied below, guard safety first; each control value is "
      "resolved from this run's tables or generated at run time, held in memory only, and injected on its own line "
      "into a copy of this file and, separately, of its JSON, as in (i)-(iii).")
    w("")
    w("1. **The JSON was not reproducible byte for byte beyond its stamps** "
      "(`guard.controls.vi_round4_rule.by_exempt_verdict` took its key order from iterating a hash-ordered set). APPLIED: the dict is built with `most_common_sorted` (count "
      "descending, then label), as the guard's other counts are. This run's order: "
      + (", ".join(f"{k_} {v_}" for k_, v_ in vi_["by_exempt_verdict"].items()) or "-") + ".")
    w("2. **The guard was described as stronger than it was**: the candidate rule took only values printed redacted "
      "with the sensitive flag, the known values and the four refuse verdicts, so a rule-class value with a "
      "mechanical exempt verdict printed in the non-sensitive form, or a METADATA value, was never considered. "
      "APPLIED to the code (the checker's widened rule), and the text above and the script's docstring now describe "
      "the code as it is. This run: candidates under the first round-5 rule "
      f"{n_.get('candidates_first_round5_rule')}, now {n_.get('candidates')}; added by the widened rule "
      f"{n_.get('added_by_widened_rule')} ("
      + (", ".join(f"{k_} {v_}" for k_, v_ in n_.get("added_by_widened_rule_verdict_class", {}).items()) or "-")
      + f"), of them printed verbatim by policy (SAFE_VERBATIM; the checker named two) "
      f"{n_.get('added_by_widened_rule_safe_verbatim')}, refused {n_.get('added_by_widened_rule_refused')}; added by finding "
      f"3's rule alone {n_.get('added_by_generated_segment_rule')} ("
      + (", ".join(f"{k_} {v_}" for k_, v_ in n_.get("added_by_generated_segment_rule_verdict_class", {}).items())
         or "-")
      + f"; mechanical verdicts printed in the non-sensitive form), refused "
      f"{n_.get('added_by_generated_segment_rule_refused')}. Controls: (vii-a) a generated pod-id-shaped value with a mechanical "
      f"FALSE-POSITIVE verdict in the pod-id class, not printed redacted: {inj('vii_a_rule_class_mechanical_exempt')}; "
      f"(vii-b) a generated value with a METADATA verdict: {inj('vii_b_metadata_verdict')}.")
    v8b = sc.get("viii_b_words_only_temp_path_exempt", {})
    w("3. **A mechanical LOCAL-PATH verdict exempted a value with a generated-looking segment**: `triage_cf` gives "
      "LOCAL-PATH to a run inside a temp or projects path before its random-segment test, so a secret-like run "
      "inside such a path would have passed. APPLIED, the stricter of the checker's two options: a mechanical "
      "verdict -- FALSE-POSITIVE, PUBLIC or LOCAL-PATH alike -- no longer exempts a value with a generated-looking "
      "segment; only a hash-keyed entry does. OS temp-folder and tempfile names have that shape and are not "
      "excepted (the checker's other option would have kept them exempt); a temp path of words and UUID parts keeps "
      f"its mechanical exemption. This run: values refused by this rule {n_.get('refused_by_generated_segment_rule')}, "
      f"of them found in this file or its JSON (plain substring) {n_.get('generated_segment_rule_values_substring_in_outputs')}"
      " -- they are printed only in redacted form, so the outputs still pass. Controls: (viii) a temp path holding a "
      f"fresh 32-character generated segment, a mechanical LOCAL-PATH verdict, printed redacted: "
      f"{inj('viii_temp_path_generated_segment')}; (viii-b) a temp path of words only with the same verdict: exempt "
      f"{yn(v8b.get('exempt'))} (generated-looking segment: {no(v8b.get('random_segment'))}).")
    ds = n_.get("digest_skips", {})
    hk = n_.get("known_any_variant_hits", {})
    w("4. **Known values were matched only bounded by non-alphanumerics**, in the scan and in the 'carries a known "
      "value' check, so a known value glued to letters -- in the text or inside an exempt value -- was not refused. "
      "APPLIED as the checker proposed -- a known value of 8 or more characters is matched as a plain substring "
      "(case- and separator-insensitively, finding 5), in the scan and in the 'carries' check alike -- with two "
      "extensions: every other refused value of 8 or more characters is matched as a plain substring in the scan "
      "too; and the SSH ports (5 characters, below that floor) are now digit-bounded instead of letter-bounded, so "
      "the ssh flag form `-p` followed by the port is found, except inside a run of 8 or more hex characters, a "
      "digest, where a port's digits can occur by chance. This run: hits of the known "
      f"values under the new matching, md {hk.get('md')} / JSON {hk.get('json')}; digit-bounded port matches skipped "
      f"inside a digest, md {ds.get('md')} / JSON {ds.get('json')}; other refused values of 8 or more characters "
      f"found as a substring: {n_.get('refused_8plus_substring_hits')}. Controls: (ix-a) a real pod id with "
      f"generated letters on both sides: {inj('ix_a_pod_id_glued_to_letters')}; (ix-b) a temp path carrying a real "
      f"pod id glued to letters, with a mechanical LOCAL-PATH verdict -- the path and the pod id both: "
      f"{inj('ix_b_pod_id_inside_mechanical_local_path')}; (ix-c) a real SSH port between two letters: "
      f"{inj('ix_c_port_glued_to_letters')}; (ix-d) the same port in the ssh flag form: "
      f"{inj('ix_d_port_ssh_flag_form')}; (ix-e) the 'carries' check itself -- a temp path of words only (generated-"
      f"looking segment: {no(sc.get('ix_e_known_value_inside_words_only_local_path', {}).get('random_segment'))}) with "
      f"the pass-phrase-shaped value glued to letters inside it, a mechanical LOCAL-PATH verdict -- the path and the "
      f"value both: {inj('ix_e_known_value_inside_words_only_local_path')}; (ix-f) the declared exception -- the "
      f"same port's digits inside a run of hex letters: refused {no(sc.get('ix_f_port_inside_digest_not_refused', {}).get('refused'))} (as declared).")
    xb, xc, xd = (sc.get("x_b_passphrase_variants", {}), sc.get("x_c_laptop_hostname_case", {}),
                  sc.get("x_d_session_id_without_prefix", {}))
    w("5. **Matching was exact-form**, so case and separator variants of known values passed, and so did the session "
      "id without its prefix. APPLIED (the checker marked it optional; applied as guard safety): see 4 for the "
      "matching; the session link's bare id is added to the guard's own known set (guard-only: the pre-release "
      f"section's set is unchanged; the guard's set holds {n_.get('known_in_guard_set')} values, by matcher kind "
      + (", ".join(f"{k_} {v_}" for k_, v_ in n_.get("known_matcher_kinds", {}).items()) or "-")
      + f"). Controls: (x-a) a real pod id upper-cased: {inj('x_a_pod_id_upper_case')}; (x-b) the pass-phrase-shaped "
      f"value (separators in it: {yn(xb.get('has_separators'))}) with its separators as spaces "
      f"{yn(xb.get('spaces'))}, as underscores {yn(xb.get('underscores'))}, removed {yn(xb.get('no_separators'))}, "
      f"upper-cased {yn(xb.get('upper_case'))}, title-cased with spaces {yn(xb.get('title_spaces'))} (refused in "
      f"both copies); (x-c) the laptop hostname lower-cased {yn(xc.get('lower'))}, upper-cased {yn(xc.get('upper'))}; "
      f"(x-d) the session id in the guard's set {yn(xd.get('id_in_guard_known_set'))}; refused bare "
      f"{yn(xd.get('bare_id'))}, after `session_` {yn(xd.get('session_word_and_id'))}, upper-cased "
      f"{yn(xd.get('id_upper_case'))}.")
    w("6. **A parenthetical in the problem paragraph above read as splitting the mechanical-verdict count of 0**, when "
      "it split all the exempt values. APPLIED: it now follows the exempt total, and the split by entry and by "
      "mechanical verdict comes after it.")
    w("")
    w(f"Second-check controls: {'ALL PASS' if ct_.get('second_check_all_pass') else 'FAIL'} (part of the controls "
      "above, so a failure stops the write).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_MD)
    ap.add_argument("--json-out", default=DEFAULT_JSON)
    ap.add_argument("--dump-all", action="store_true",
                    help="with --dump-untriaged: also print values cleared by mechanical rules")
    ap.add_argument("--dump-untriaged", action="store_true",
                    help="print values no rule clears, with their first line, to STDOUT only (for "
                         "Code's individual triage); never written to any file")
    ap.add_argument("--pin", default=None,
                    help="scan the history as of this commit (refs descending from it are replaced by it)")
    ap.add_argument("--since", default=None,
                    help="count sources new since this commit separately (default: the commit that added the block)")
    ap.add_argument("--selftest", action="store_true",
                    help="round 5: run the scan and the leak guard's positive controls, print their outcome (booleans "
                         "and counts only) and write nothing; exit 0 only if every control behaves")
    a = ap.parse_args()
    for o in (a.out, a.json_out):
        ab = os.path.abspath(os.path.join(ROOT, o))
        inside_repo = ab.startswith(ROOT + os.sep)
        if inside_repo and not ab.startswith(os.path.join(ROOT, "results", "raw") + os.sep):
            raise SystemExit(f"refusing output inside the repository outside results/raw/: {o}")
        if inside_repo and os.path.basename(ab) not in (os.path.basename(DEFAULT_MD), os.path.basename(DEFAULT_JSON)):
            raise SystemExit(f"refusing a results/raw/ output other than this part's own two files: {o}")

    stamp = sh(["date", "-u"]).stdout.decode().strip()
    script_path = os.path.relpath(os.path.abspath(__file__), ROOT)
    script_sha = sha256_hex(open(os.path.abspath(__file__), "rb").read())
    block_sha_wt = sha256_hex(open(os.path.join(ROOT, BLOCK), "rb").read())
    refs_live, head_live = snapshot_refs()
    pin_notes = []
    if a.pin:
        pin = git("rev-parse", "--verify", a.pin + "^{commit}").decode().strip()
        refs, pin_notes = refs_at(refs_live, pin)
        head = pin
    else:
        refs, head = refs_live, head_live
    block_sha_head = sha256_hex(git("show", f"{head}:{BLOCK}"))
    ref_shas = sorted({sha for _, sha, _ in refs} | {head})
    tag_objs = [sha for _, sha, typ in refs if typ == "tag"]
    m = build_model(ref_shas, head)
    m["head"] = head
    # --since base: the history as of the commit that added the block (or --since)
    since = a.since or git("log", "--diff-filter=A", "--format=%H", head, "--", BLOCK).decode().split()[-1]
    since = git("rev-parse", "--verify", since + "^{commit}").decode().strip()
    base_refs, _ = refs_at(refs, since)
    base_ref_shas = sorted({s for _, s, _ in base_refs})
    if since == head and set(base_ref_shas) == set(s for _, s, _ in refs):
        m["base_objs"] = None
        m["base_head_blobs"] = None
        new_commits = []
    else:
        bo = git("rev-list", "--objects", *base_ref_shas).decode("utf-8", "replace").split("\n")
        m["base_objs"] = {l.split(" ", 1)[0] for l in bo if l.strip()} | {s for _, s, t in base_refs if t == "tag"}
        bt = git("ls-tree", "-r", "-z", since).decode("utf-8", "replace").split("\0")
        m["base_head_blobs"] = set()
        m["base_head_blob_paths"] = collections.defaultdict(list)
        for e_ in bt:
            if e_:
                meta_, _, p_ = e_.partition("\t")
                s_ = meta_.split()[2]
                m["base_head_blobs"].add(s_)
                m["base_head_blob_paths"][s_].append(p_)
        new_commits = [c for c in m["commits"] if c not in m["base_objs"]]
    new_blobs = [s for s in m["blobs"] if m.get("base_objs") is not None and s not in m["base_objs"]]
    remote_url = git("remote", "get-url", "origin", check=False).decode().strip()
    ancestry = {}
    for name, sha, typ in refs:
        r = sh(["git", "merge-base", "--is-ancestor", f"{sha}^{{commit}}" if typ == "tag" else sha,
                "refs/remotes/origin/main"], check=False).returncode
        ancestry[name] = (r == 0)

    # (i-a) the block's fallback, as written (with --pin: `git log -p <the pinned refs>`, the same commit set)
    logp, g = run_fallback(ref_shas if a.pin else None)
    logp_nl = logp.count(b"\n")           # line count = newline count (the stream ends with a newline)
    logp_ends_nl = logp.endswith(b"\n")
    scan_av = scanner_availability()
    grep_out = g.stdout.decode("utf-8", "replace")
    grep_lines = [l for l in grep_out.split("\n") if l]
    grep_binary_notice = any(l.startswith("Binary file") for l in grep_lines)
    logp_lines = logp.split(b"\n")
    loc = index_log(logp_lines)
    fb_rx = re.compile(FALLBACK_PATTERN, re.I)
    py_lines = [i for i, l in enumerate(logp_lines) if fb_rx.search(l.decode("utf-8", "replace"))]
    alt_rx = [(n, re.compile(p, re.I)) for n, p in FALLBACK_ALTS]
    alt_lines = collections.Counter()
    alt_occ = collections.Counter()
    bulk = collections.Counter()
    bulk_reason = {}
    bulk_words = collections.defaultdict(collections.Counter)
    bulk_first = {}
    bulk_locs = collections.defaultdict(list)
    shape_rows = []
    shape_raw = []   # round 5: (value, triage source) per shape row, index-aligned; in memory only, never printed
    multi_alt_lines = 0
    for gl in grep_lines:
        num, _, text = gl.partition(":")
        ln = int(num)
        c, path, side, fln = loc[ln - 1] if ln - 1 < len(loc) and loc[ln - 1] else (None, "?", "?", None)
        k = 0
        for n, rx in alt_rx:
            ms = list(rx.finditer(text))
            if not ms:
                continue
            k += 1
            alt_lines[n] += 1
            alt_occ[n] += len(ms)
            for mt in ms:
                w = fallback_word(text, mt.start(), mt.end())
                wend = mt.end()
                while wend < len(text) and (text[wend].isalnum() or text[wend] in "_-"):
                    wend += 1
                rule, why = fallback_bulk_rule(n, w, path or "", text[wend:wend + 4])
                bulk[(n, rule)] += 1
                bulk_reason[(n, rule)] = why
                bulk_words[(n, rule)][w.lower()] += 1
                bulk_first.setdefault((n, rule), f"{(c or '?')[:8]} {path}:{side}{fln if fln else ''}")
                bulk_locs[(n, rule)].append(f"{(c or '?')[:8]} {path}:{side}{fln if fln else ''}")
        if k > 1:
            multi_alt_lines += 1
        for sm in SHAPE_RE.finditer(text):
            name, op, q, v = sm.groups()
            cls, why = classify_value(v, bool(q))
            # round 5: the pre-flip raw's row triage (path, key, value) first, then value-keyed explicit triage
            st_ = shape_manual(path or "", name, v)
            mt_ = (st_[0], st_[1], True) if st_ else manual(v)
            shape_raw.append((v, "shape16" if st_ else ("shape-manual" if mt_ else "shape")))
            if mt_:
                verdict, why = mt_[0], mt_[1]
                cls = cls or "manual"
            elif cls is None:
                verdict, why = "UNTRIAGED", "no mechanical rule clears it"
            else:
                verdict = "FALSE-POSITIVE"
            safe = cls in ("number", "bool/null", "structure") and len(v) <= 8
            shape_rows.append({"locator": f"{(c or '?')[:8]} {path}:{side}{fln if fln else ''}",
                               "logp_line": ln, "key": name, "op": op, "quoted": bool(q),
                               "value": v if safe else red(v, sensitive=False),
                               "value_class": cls, "verdict": verdict, "reason": why})

    # (i-b), (ii) full scan
    (precise, he, he_stats, ids, users_at_head, workspace_at_head, binary, stats, sweep, cf, hdr,
     binc) = scan_history(m, tag_objs)
    exact = recount_exact(m, tag_objs, ids)

    # identities (commit metadata)
    ident = git("log", "--format=%H%x09%an%x09%ae%x09%cn%x09%ce", *ref_shas).decode("utf-8", "replace")
    authors, committers = collections.Counter(), collections.Counter()
    ident_commits = collections.defaultdict(list)
    for line in ident.split("\n"):
        if not line.strip():
            continue
        h, an, ae, cn, ce = line.split("\t")
        authors[(an, ae)] += 1
        committers[(cn, ce)] += 1
        ident_commits[("author", an, ae)].append(h)
        ident_commits[("committer", cn, ce)].append(h)
    identity_emails = {e for (_, e) in list(authors) + list(committers)}
    laptop_commits = len({h for (role, nm, em), hs in ident_commits.items()
                          if em.endswith(".local") and not em.endswith("@jspace-lab.local") for h in hs})

    # (v)
    count_objects = sh(["git", "count-objects", "-vH"], check=False)
    largest, head_big = size_section(m, binary, refs)
    max_blob = max((m["sizes"][s] for s in m["blobs"]), default=0)
    # (iv)
    names_only = git("log", "--all", "--name-only", "--format=").decode("utf-8", "replace").split("\n")
    names_only = {p for p in names_only if p.strip()}
    all_paths = m["all_paths_raw"] | m["all_paths_objs"] | names_only
    jlens_hist = sorted(p for p in all_paths if p == "jlens-qwen36" or p.startswith("jlens-qwen36/"))
    jlens_head = sorted(p for p in m["head_files"] if p == "jlens-qwen36" or p.startswith("jlens-qwen36/"))
    gitlinks = sorted(p for p, v in m["head_files"].items() if v[0] == "160000")
    npz_rows, gi_wt_ok = npz_section(m, binary)
    weights = weights_section(m, all_paths)
    cred_files = sorted(p for p in all_paths if CRED_FILE_RE.search(p))
    ckpt_paths = sorted(p for p in all_paths if p.startswith("data/m/ckpt/"))
    # round 3 (third checker, finding 2): when a -diff path is tracked, record which commit first added it, what
    # `git log -p` printed for it, and what the fallback's pattern finds in its content (which the fallback cannot see)
    ckpt_ev = {"introduced": {}, "blobs": [], "logp_binary_lines": 0}
    if ckpt_paths:
        for p_ in ckpt_paths:
            intro_ = git("log", "--reverse", "--diff-filter=A", "--format=%H", *ref_shas, "--", p_).decode().split()
            ckpt_ev["introduced"][p_] = intro_[0] if intro_ else None
        ck_blobs = sorted({s_ for s_, occ_ in m["blob_occ"].items() for _, p_ in occ_ if p_.startswith("data/m/ckpt/")})
        for s_, _, data_ in cat_batch(ck_blobs):
            txt_ = data_.decode("utf-8", "replace")
            ckpt_ev["blobs"].append({"blob": s_, "paths": blob_paths(m, s_), "bytes": len(data_),
                                     "scanned_as_text_in_i_b": not is_binary(blob_paths(m, s_), data_),
                                     "fallback_pattern_lines": sum(1 for l_ in txt_.split("\n") if fb_rx.search(l_)),
                                     "at_head": s_ in m["head_blobs"]})
        ckpt_ev["logp_binary_lines"] = len(re.findall(rb"(?m)^Binary files .* b/data/m/ckpt/\S* differ$", logp))
    # the introducing commits that landed after the round-2 raw's snapshot (its HEAD, R2_HEAD)
    ckpt_after_r2 = sorted({c_ for c_ in ckpt_ev["introduced"].values()
                            if c_ and c_ != R2_HEAD and is_ancestor(R2_HEAD, c_)})
    ckpt_ev["introduced_after_round2_snapshot"] = ckpt_after_r2
    gattr = git("show", f"{head}:.gitattributes", check=False).decode("utf-8", "replace")
    nodiff_lines = [l.strip() for l in gattr.split("\n") if l.strip() and not l.strip().startswith("#")
                    and re.search(r"(^|\s)(-diff|binary)(\s|$)", l)]

    # objects in the local store reachable from no LIVE ref (a push sends reachable objects only)
    live_shas = sorted({s for _, s, _ in refs_live} | {head_live})
    reach = {l.split(" ", 1)[0] for l in git("rev-list", "--objects", *live_shas).decode("utf-8", "replace").split("\n")
             if l.strip()} | {s for _, s, t in refs_live if t == "tag"}
    live_new_commits = git("rev-list", *live_shas, "--not", since).decode().split()
    allobj = git("cat-file", "--batch-all-objects", "--batch-check=%(objectname) %(objecttype) %(objectsize)"
                 ).decode().split("\n")
    unreach = collections.Counter()
    unreach_bytes = 0
    n_store = 0
    unreach_commits = []
    for l in allobj:
        if not l.strip():
            continue
        n_store += 1
        s_, t_, z_ = l.split()
        if s_ not in reach:
            unreach[t_] += 1
            unreach_bytes += int(z_)
            if t_ == "commit":
                unreach_commits.append(s_)
    reflogs = reflog_evidence(sorted(unreach_commits))
    jv = json_vectors(m)
    hp_out = home_paths_outside_repo(m, users_at_head)

    # content copies of jlens-qwen36 files (plain file reads; no git command inside the clone)
    size_index = collections.defaultdict(set)
    for s_ in m["blobs"]:
        size_index[m["sizes"][s_]].add(s_)
    reach_blobs = set(m["blobs"])
    jroot = os.path.join(ROOT, "jlens-qwen36")
    jl = {"files": 0, "hashed": 0, "matches": []}
    for dp, dns, fns in os.walk(jroot):
        rel = os.path.relpath(dp, jroot)
        if rel.split(os.sep)[0] in (".git", ".venv"):
            dns[:] = []
            continue
        dns.sort()
        for fn in sorted(fns):
            fp = os.path.join(dp, fn)
            if os.path.islink(fp) or not os.path.isfile(fp):
                continue
            jl["files"] += 1
            z_ = os.path.getsize(fp)
            if z_ not in size_index:
                continue
            jl["hashed"] += 1
            with open(fp, "rb") as fh:
                b_ = fh.read()
            h_ = hashlib.sha1(b"blob %d\0" % len(b_) + b_).hexdigest()
            if h_ in reach_blobs:
                jl["matches"].append({"jlens_path": os.path.relpath(fp, jroot), "blob": h_, "bytes": len(b_),
                                      "tracked_paths": blob_paths(m, h_), "at_head": h_ in m["head_blobs"]})
    EMPTY_BLOB = "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
    # round 2: the clone's own index, read as a plain file (no git process in the clone). Its entries are the
    # clone-TRACKED files with the blob shas of their committed versions -- so a locally patched working copy
    # cannot hide an upstream file from this check.
    jidx = {"present": False}
    ipath = os.path.join(jroot, ".git", "index")
    if os.path.isfile(ipath):
        ver_, ck_, ents = read_git_index(ipath)
        jidx = {"present": True, "version": ver_, "checksum_ok": ck_, "entries": len(ents or [])}
        if ents is not None:
            idx_paths = {p_ for p_, _, _, _ in ents}
            nonempty = [(p_, s_) for p_, s_, _, z_ in ents if s_ != EMPTY_BLOB]
            jidx["nonempty_entries"] = len(nonempty)
            jidx["nonempty_reachable_in_lab"] = sorted(p_ for p_, s_ in nonempty if s_ in reach_blobs)
            jidx["empty_entries"] = sorted(p_ for p_, s_, _, _ in ents if s_ == EMPTY_BLOB)
            jidx["data_entries"] = sorted(p_ for p_ in idx_paths if p_.startswith("data/"))
            jidx["matched_files_clone_tracked"] = sorted(x["jlens_path"] for x in jl["matches"]
                                                         if x["blob"] != EMPTY_BLOB and x["jlens_path"] in idx_paths)
            jidx["empty_matches_clone_tracked"] = sorted(x["jlens_path"] for x in jl["matches"]
                                                         if x["blob"] == EMPTY_BLOB and x["jlens_path"] in idx_paths)
            mod_ = []
            for p_, s_, _, _ in ents:
                fp_ = os.path.join(jroot, p_)
                if os.path.isfile(fp_) and not os.path.islink(fp_):
                    with open(fp_, "rb") as fh:
                        b_ = fh.read()
                    if hashlib.sha1(b"blob %d\0" % len(b_) + b_).hexdigest() != s_:
                        mod_.append(p_)
                else:
                    mod_.append(p_ + " (missing)")
            jidx["modified_on_disk"] = sorted(mod_)

    # 'continuity' over every text source (blob versions + messages); value-shaped continuations
    cont = {"occ": 0, "sources": 0, "paths": set(), "head_occ": 0, "phrases": [], "occ_word": 0, "occ_dis": 0,
            "occ_new": 0, "paths_base": set()}
    for kind, sha, path, commit, text in iter_sources(m, tag_objs):
        k_ = len(re.findall(r"(?i)continuity", text))
        if not k_:
            continue
        cont["occ"] += k_
        cont["occ_word"] += len(re.findall(r"(?i)\bcontinuity\b", text))
        cont["occ_dis"] += len(re.findall(r"(?i)discontinuity", text))
        if is_new_source(m, kind, sha):
            cont["occ_new"] += k_
        else:
            cont["paths_base"].add(path)
        cont["sources"] += 1
        cont["paths"].add(path)
        if kind == "blob" and sha in m["head_blobs"]:
            cont["head_occ"] += k_
        li = LineIndex(text)
        for mt in re.finditer(r"(?i)continuity[ \-]+(?:password|pass[ \-]?phrase|code[ \-]?word)", text):
            tail = text[mt.end():mt.end() + 40]
            value_follows = bool(re.match(r"\s*(?:is|was|:|=)\s*[`'\"]?[A-Za-z0-9]", tail))
            cont["phrases"].append({"locator": loc_str(m, kind, sha, path, commit, li.line_of(mt.start())),
                                    "at_head": kind == "blob" and sha in m["head_blobs"],
                                    "value_follows": value_follows})
    refs_after, head_after = snapshot_refs()
    refs_moved = (refs_after != refs_live) or (head_after != head_live)

    # ------------------------------------------------------------ write md
    L = []
    w = L.append
    w("# AUDIT-note-release v1.2 -- N12-history: release scrub over the full history")
    w("")
    w(f"- Code stamp (`date -u`): {stamp}")
    w(f"- HEAD: `{head}` (pinned at start; refs at end {'MOVED -- see note' if refs_moved else 'unchanged'})"
      + (f"; `--pin {head[:10]}`: the history as of that commit ({'; '.join(pin_notes) or 'no ref moved'}); the "
         f"live HEAD at the run was `{head_live[:10]}`" if a.pin else ""))
    w(f"- Base for the new-since columns (`--since`): `{since}` "
      + ("(the commit that added the audit block; the builder's and the checker's runs were at this commit). "
         if not a.since else "")
      + (f"Commits reachable now but not from the base: {len(new_commits)} "
         f"({', '.join('`' + c[:10] + '`' for c in new_commits)}); new blobs: {len(new_blobs)}. A count at the "
         f"base is the total minus the new-since column." if m.get("base_objs") is not None else
         "This run is at the base: no new-since columns."))
    w("- Referent note: the block names N12's output `results/raw/<stamp>_note-N12-scrub.md` (:84). The "
      "orchestrator split N12 across three raws -- `2026-10-08_note-N12-history` (this file: (i), (ii), (v) and "
      "(iv)'s mechanical checks), `2026-10-08_note-N12-content` and `2026-10-08_note-N12-licenses` -- which the "
      "README and the ledger cite together as N12's output.")
    w(f"- Block: `{BLOCK}`, sha256 `{block_sha_wt}` (working tree) / `{block_sha_head}` (HEAD blob); "
      f"routed `{BLOCK_SHA[:8]}...{BLOCK_SHA[-4:]}`: "
      f"{'MATCH' if block_sha_wt == BLOCK_SHA == block_sha_head else 'MISMATCH'}")
    w(f"- Item: N12 (block lines 72-85) parts (i), (ii), (v) and (iv)'s mechanical checks; "
      f"part id N12-history")
    w(f"- Script: `{script_path}`, sha256 `{script_sha}`")
    w(f"- Interpreter: `{sys.executable}` (Python {sys.version.split()[0]}; stdlib only)")
    exe = sys.executable
    exe_shown = os.path.relpath(exe, ROOT) if exe.startswith(ROOT + os.sep) else exe
    w(f"- Command: `{exe_shown} {' '.join([script_path] + sys.argv[1:])}` (run from the repository root)")
    w("- Read-only: git log / rev-list / rev-parse / cat-file / ls-tree / ls-files / for-each-ref / "
      "count-objects / check-ignore --no-index / show / merge-base / remote get-url / grep. Nothing staged or "
      "committed; no git command run inside jlens-qwen36/ (its working tree and its `.git/index` are read as "
      "plain files); the lab's remote-tracking reflogs (`.git/logs/refs/remotes/`), the files not yet in history "
      "(pre-release section) and Homebrew's local formula index are read as plain files; nothing installed; no "
      "network access (so refs that exist only on GitHub are not visible here -- see the PI pre-flip steps).")
    subj_new = {c: git("log", "-1", "--format=%s", c).decode("utf-8", "replace") for c in new_commits}
    from_m = all(re.search(r"G-CAL|PROPOSAL-m|^m package", s_) for s_ in subj_new.values())
    w(f"- Coverage of the commits after the block's commit: this run scans HEAD `{head[:10]}`, which includes "
      f"the {len(new_commits)} commit(s) made after `{since[:10]}` "
      + ("(the concurrent PROPOSAL-m session's G-CAL commits: their subjects begin `m package` / `G-CAL`) "
         if from_m and new_commits else "(see the JSON, `since.new_commits`) ")
      + f"({', '.join('`' + c[:10] + '`' for c in new_commits) or 'none'}). It is still a "
        "snapshot: the final re-run at the release commit (PI pre-flip step 1, under (v)) is required.")
    w("- Redaction form: `xxxx...[len N]#hhhhhhhh` = first 4 characters, the value's length, the "
      "first 8 hex of sha256(value) (the routing's form -- first 4 + length + sha256[:8] -- with the "
      "punctuation the sibling raws and both checkers quote). SSH-port-class values (every 4-5 digit "
      "number on an ssh/port/alias line, whatever its verdict) use `lenN:hhhhhhhh` -- the length and the "
      "first 8 hex of sha256 only, no digit of the value. No candidate secret, RunPod id or volume name (nor "
      "the name's stem), IP address, SSH port, SSH key fingerprint, laptop/container hostname or personal "
      "email appears verbatim in this file or its JSON (asserted by the script before writing). A value of 4 "
      "characters or fewer is printed in full by the generic form; only non-sensitive values reach it (listed "
      "in the round-2 values-check).")
    caveat_idx = len(L)
    w("- Caveat (enumeration): computed below, after the sensitive set is known.")   # replaced after (iv)
    w("")
    w("## Scope")
    w("")
    w("Refs scanned (everything reachable from any of them; `--all` at the pinned moment):")
    w("")
    w("| ref | object | type | ancestor of origin/main |")
    w("|---|---|---|---|")
    for name, sha, typ in refs:
        w(f"| `{name}` | `{sha[:10]}` | {typ} | {'yes' if ancestry[name] else 'NO'} |")
    w("")
    w(f"- Commits reachable: {len(m['commits'])}; trees: {m['n_trees']}; blobs: {len(m['blobs'])} "
      f"({stats['text_blobs']} text, {stats['binary_blobs']} binary); annotated tag objects: "
      f"{len(tag_objs)}; text bytes scanned: {stats['text_bytes']:,}; commit + tag messages scanned: "
      f"{stats['messages_and_tags']}; commit headers scanned: {hdr['n_commit_headers']}, tag headers: "
      f"{hdr['n_tag_headers']}; binary blobs whose string content is scanned: {stats['binary_blobs']} "
      f"({binc['members']} npz members, {sum(binc['png_chunks'].values())} PNG chunks).")
    w(f"- Remote `origin` URL carries userinfo (credentials): "
      f"{'YES -- ' + red(remote_url) if '@' in remote_url.split('//', 1)[-1].split('/', 1)[0] else 'no'} "
      f"(`.git/config` is local and not released; checked only for completeness).")
    if refs_moved:
        w("- NOTE: refs moved during the run (a concurrent session committed); every scan below "
          "used the pinned shas above except (i-a), which ran `--all` literally at its own moment.")
    w("")

    # ---- (i)
    w("## (i) Secrets over the entire history")
    w("")
    w("### (i-a) The block's primary scanners (not run) and its fallback, run as written")
    w("")
    sa = scan_av
    inst = ", ".join(f"`{n_}` {d_['version']} ({d_['license']}; bottle for `{sa['bottle_tag']}`: "
                     f"{'yes' if d_['bottle_for_this_platform'] else 'NO'})" for n_, d_ in sa["formulae"].items())
    installable = len(sa["formulae"]) == 2 and all(d_["bottle_for_this_platform"] for d_ in sa["formulae"].values())
    w("**The block's primary scanners have NOT been run over this history.** gitleaks and trufflehog are not "
      "installed on this machine (`which`: "
      + ", ".join(f"{t_} {'found' if p_ else 'not found'}" for t_, p_ in sa["which"].items())
      + "). They are installable here via Homebrew"
      + (f" (`{sa['brew']}` present; Homebrew's local formula index `{sa['cache']}`, cached {sa.get('cache_date')}, "
         f"read as a file -- no brew command, no network -- lists {inst}; macOS {sa['macos']})"
         if sa["brew"] and sa["cache"] else " (Homebrew's presence or its local index could not be confirmed)")
      + (", but were not installed, because the PI's routing for this audit forbids installs without the PI's "
         "word. Block :77 runs its fallback only if the scanners are not installable; that condition does not "
         "hold, so running the fallback instead is a deviation from the block, recorded here for the PI. The "
         "block's fallback below, plus Code's blob-level scans in (i-b), stand in for the scanners; running them "
         "is PI pre-flip step 4 (under (v))."
         if installable else ". (Installability not established for both; see the JSON, `scanner_availability`.)"))
    w("")
    w("The fallback, as written: `git log -p --all | grep -nEi '" + FALLBACK_PATTERN + "'` with `/usr/bin/grep` "
      "(BSD grep; its exit status read from its own process, not after a pipe).")
    w("")
    w(f"- `git log -p --all` output: {len(logp):,} bytes, {logp_nl:,} lines (newline count; the stream ends "
      f"with a newline: {'yes' if logp_ends_nl else 'no'}).")
    w(f"- grep exit status: {g.returncode} (0 = matches found). Binary-file notice in grep output: "
      f"{'YES' if grep_binary_notice else 'no'}.")
    w(f"- **Total hit lines: {len(grep_lines)}.** Python `re` (IGNORECASE) cross-check over the same "
      f"bytes: {len(py_lines)} lines ({'equal' if len(py_lines) == len(grep_lines) else 'DIFFERENT'}).")
    w(f"- Lines matching more than one alternative: {multi_alt_lines}.")
    w("")
    w("| alternative | lines | occurrences |")
    w("|---|---|---|")
    for n, _ in FALLBACK_ALTS:
        w(f"| `{n}` | {alt_lines[n]} | {alt_occ[n]} |")
    w("")
    w("Coverage limits of the fallback. (1) `git log -p` prints `Binary files ... differ` for binary blobs "
      f"(the {stats['binary_blobs']} .npz/.png blobs), so their contents never reach the grep; (i-b)'s "
      "binary-content scan below reads their string content (npz unicode members, printable-ASCII runs of every "
      "member, PNG text chunks). (2) HEAD's `.gitattributes` has "
      f"{len(nodiff_lines)} -diff/binary line(s) ({', '.join('`' + md_escape(l) + '`' for l in nodiff_lines) or 'none'}); "
      f"paths under `data/m/ckpt/` ever tracked: {len(ckpt_paths)}, so "
      + ("that limit has never applied to any committed file." if not ckpt_paths else
         "the limit now applies: "
         + "; ".join(f"`{p_}` (first added by `{(c_ or '?')[:10]}`"
                     + (", a commit after the base" if c_ in new_commits else "") + ")"
                     for p_, c_ in ckpt_ev["introduced"].items())
         + f". `git log -p` prints {ckpt_ev['logp_binary_lines']} `Binary files ... differ` line(s) for them and "
           f"none of their content, so their content never reaches the grep; (i-b) reads them as blobs ("
         + ", ".join(f"`{b_['blob'][:8]}` {b_['bytes']:,} bytes, scanned as text: "
                     f"{'yes' if b_['scanned_as_text_in_i_b'] else 'NO'}, lines matching the fallback's pattern: "
                     f"{b_['fallback_pattern_lines']}" for b_ in ckpt_ev["blobs"])
         + ")."
         + (" The round-2 raw, a snapshot at `bab921ce52`, said this limit had never applied; "
            + ", ".join(f"`{c_[:10]}`" for c_ in ckpt_after_r2)
            + " changed that after it was written -- the case PI pre-flip step 1's re-run at the release commit "
              "exists for." if ckpt_after_r2 else ""))
      + " (3) `git log -p` does not print commit headers (signatures); (i-b) scans every commit and tag "
        "header in its own section.")
    w("")
    w("Locators in (i-a) are `<commit8> <path>:<side><line>`, mapped from the grep's line number in the "
      "`git log -p --all` stream: side `+` = an added line (line number in the new file), `-` = a removed "
      "line (old file), ` ` = a context line, `m` = a commit-message line, `h` = a header line.")
    w("")
    w("**Bulk triage by rule** (every occurrence assigned to exactly one rule; words are the "
      "maximal `[A-Za-z0-9_-]` run around the match):")
    w("")
    w("| alternative | rule | occurrences | reason | most frequent words (count) | first locator |")
    w("|---|---|---|---|---|---|")
    for (n, rule), cnt in sorted(bulk.items(), key=lambda x: (x[0][0], -x[1])):
        words = ", ".join(f"{md_escape(wd)} ({k})" for wd, k in bulk_words[(n, rule)].most_common(8))
        w(f"| `{n}` | {rule} | {cnt} | {bulk_reason[(n, rule)]} | {words} | {md_escape(bulk_first[(n, rule)])} |")
    w("")
    for (n, rule), locs in sorted(bulk_locs.items()):
        if rule.startswith(("T2", "T3", "P3", "K2", "X")):
            w(f"- Every locator of `{n}` / {rule}: " + ", ".join(md_escape(x) for x in locs))
    w("")
    n_shape = len(shape_rows)
    shape_group = collections.Counter((r["key"].lower(), r["value_class"] or "-", r["verdict"]) for r in shape_rows)
    shape_first = {}
    for r in shape_rows:
        shape_first.setdefault((r["key"].lower(), r["value_class"] or "-", r["verdict"]), r["locator"])
    w(f"**Credential-shaped hits, inspected individually** (`<word containing the alternative>` "
      f"followed by `=`, `:` or `=>` and a value): {n_shape} occurrences on the hit lines, "
      f"{len(shape_group)} distinct (key, value-class) groups; verdicts: "
      + ", ".join(f"{k} {v}" for k, v in collections.Counter(r['verdict'] for r in shape_rows).items())
      + ". The JSON (`fallback.credential_shaped`) holds one record per distinct (key, operator, value, "
        "class, verdict, reason) with every locator; values are redacted unless numeric/boolean/structural "
        "and at most 8 characters. Grouped:")
    w("")
    w("| key | value class | verdict | occurrences | first locator |")
    w("|---|---|---|---|---|")
    for (k_, cls, vd), cnt in sorted(shape_group.items(), key=lambda x: -x[1]):
        w(f"| `{md_escape(k_)}` | {cls} | {vd} | {cnt} | {md_escape(shape_first[(k_, cls, vd)])} |")
    untri = [r for r in shape_rows if r["verdict"] == "UNTRIAGED"]
    if untri:
        w("")
        w("UNTRIAGED credential-shaped hits:")
        for r in untri:
            w(f"- {r['locator']} key `{r['key']}` value {r['value']}")
    w("")

    # (i-b)
    w("### (i-b) Precise scan over every reachable blob and every commit/tag message")
    w("")
    w(f"Input: `git rev-list --objects <refs> | git cat-file --batch` -- {stats['text_blobs']} text "
      f"blobs (every version of every text file ever committed) plus {stats['messages_and_tags']} commit/tag "
      f"messages. The {stats['binary_blobs']} binary blobs are not regex-scanned as text; their string content "
      f"is scanned in the binary-content subsection below, and they are listed under (v)/(iv) and in the JSON "
      f"(`binary_blobs`). Commit and tag headers are scanned in their own subsection below. Locator = "
      f"the earliest commit introducing the blob, the path, the line within the blob. Patterns 1-"
      f"{N_PRECISE_ORIGINAL} are the builder's; {N_PRECISE_ORIGINAL + 1}-{N_PRECISE_R1} were added at the "
      f"first values-check (the first checker's extended set); {N_PRECISE_R1 + 1}-{len(PRECISE)} at the second "
      f"(base64 key-material markers, so a key body without its PEM armor is caught -- see the entropy note "
      f"below).")
    w("")
    w("| pattern | distinct values | occurrences (summed over blob versions + messages) | at HEAD | new since base | verdicts |")
    w("|---|---|---|---|---|---|")
    true_candidates = []
    untriaged_precise = []
    for name, rx, _ in PRECISE:
        tab = precise[name]
        occ = sum(e["n_occ"] for e in tab.values())
        occ_h = sum(e["n_occ_head"] for e in tab.values())
        occ_n = sum(e["n_occ_new"] for e in tab.values())
        vd = collections.Counter(e["triage"][0] for e in tab.values())
        w(f"| {name} | {len(tab)} | {occ} | {occ_h} | {occ_n} | {', '.join(f'{k} {v}' for k, v in vd.items()) or '-'} |")
        for v, e in tab.items():
            if e["triage"][0] == "TRUE-SECRET-CANDIDATE":
                true_candidates.append((name, v, e))
            if e["triage"][0] == "UNTRIAGED":
                untriaged_precise.append((name, v, e))
    w("")
    w("Patterns (verbatim, Python `re`):")
    w("")
    for name, rx, _ in PRECISE:
        w(f"- {name}: `{rx.pattern}`")
    w("")
    w("Every precise-pattern hit, triaged individually (one row per distinct value):")
    w("")
    w("| pattern | value (redacted) | verdict | reason | occurrences | blobs/messages | at HEAD (paths) | first locator |")
    w("|---|---|---|---|---|---|---|---|")
    any_precise = False
    for name, rx, _ in PRECISE:
        for v, e in sorted(precise[name].items(), key=lambda x: x[1]["first_order"] or 0):
            any_precise = True
            hp = ", ".join(sorted(e["head_paths"])[:3]) + (" ..." if len(e["head_paths"]) > 3 else "")
            w(f"| {name} | `{red(v, sensitive=e['triage'][2])}` | {e['triage'][0]} | {md_escape(e['triage'][1])} | {e['n_occ']} | "
              f"{len(e['sources'])} | {e['n_occ_head']} ({md_escape(hp) or '-'}) | {md_escape(e['first'])} |")
    if not any_precise:
        w("| (none) | | | | | | | |")
    w("")
    w("**High-entropy strings in an assignment or header context** (" + HE_CONTEXT_DESC +
      "; Shannon entropy over the string's characters, bar > 4.0 bits/char):")
    w("")
    w(f"- Candidates in context: base64-alphabet {he_stats['candidates_base64']}, hex-only "
      f"{he_stats['candidates_hex']}. Over 4.0 bits/char: base64 {he_stats['over4_base64']}, hex "
      f"{he_stats['over4_hex']}. Note: a hex-only string cannot exceed log2(16) = 4.0 bits/char, so "
      f"the > 4.0 bar never fires on hex by construction; hex in a credential context is covered by "
      f"the wandb/40-hex pattern and by the generic-assignment pattern above.")
    he_vd = collections.Counter(e["triage"][0] for e in he.values())
    he_reason = collections.Counter((e["triage"][0], e["triage"][1]) for e in he.values())
    w(f"- Distinct values over 4.0: {len(he)}; verdicts: "
      f"{', '.join(f'{k} {v}' for k, v in he_vd.items()) or '-'}. By reason:")
    w("")
    w("| verdict | reason | distinct values |")
    w("|---|---|---|")
    for (vd, rs), cnt in he_reason.most_common():
        w(f"| {vd} | {md_escape(rs)} | {cnt} |")
    he_untri = [(v, e) for v, e in he.items() if e["triage"][0] not in ("FALSE-POSITIVE", "LOCAL-PATH")]
    if he_untri:
        w("")
        w("High-entropy values other than FALSE-POSITIVE / LOCAL-PATH (individually):")
        w("")
        w("| value (redacted) | key | entropy | verdict | reason | occurrences | first locator |")
        w("|---|---|---|---|---|---|---|")
        for v, e in sorted(he_untri, key=lambda x: x[1]["first_order"] or 0):
            w(f"| `{red(v)}` | `{md_escape(str(e['extra']['key'])[:40])}` | {e['extra']['entropy']} | "
              f"{e['triage'][0]} | {md_escape(e['triage'][1])} | {e['n_occ']} | {md_escape(e['first'])} |")
            if e["triage"][0] == "TRUE-SECRET-CANDIDATE":
                true_candidates.append(("high_entropy", v, e))
            if e["triage"][0] == "UNTRIAGED":
                untriaged_precise.append(("high_entropy", v, e))
    w("")

    def cf_table(title, tab):
        """By-verdict/reason table for a context-free table, then every value not cleared as a path."""
        w(f"**{title}** ({CF_DESC}):")
        w("")
        vd = collections.Counter(e["triage"][0] for e in tab.values())
        w(f"- Distinct values: {len(tab)}; occurrences: {sum(e['n_occ'] for e in tab.values())} "
          f"(new since base: {sum(e['n_occ_new'] for e in tab.values())}); verdicts: "
          f"{', '.join(f'{k} {v}' for k, v in vd.items()) or '-'}.")
        if tab:
            w("")
            w("| verdict | reason | distinct values | occurrences |")
            w("|---|---|---|---|")
            rr = collections.Counter()
            ro = collections.Counter()
            for e in tab.values():
                rr[(e["triage"][0], e["triage"][1])] += 1
                ro[(e["triage"][0], e["triage"][1])] += e["n_occ"]
            for (vd_, rs_), cnt in rr.most_common():
                w(f"| {vd_} | {md_escape(rs_)} | {cnt} | {ro[(vd_, rs_)]} |")
            ind = [(v, e) for v, e in tab.items() if not (e["triage"][0] in ("FALSE-POSITIVE", "LOCAL-PATH")
                                                          and "path" in e["triage"][1])]
            if ind:
                w("")
                w("Values other than paths, individually:")
                w("")
                w("| value (redacted) | run | entropy | verdict | reason | occurrences | first locator |")
                w("|---|---|---|---|---|---|---|")
                for v, e in sorted(ind, key=lambda x: (x[1]["first_order"] or 0, x[0])):
                    w(f"| `{red(v, sensitive=e['triage'][2])}` | {e['extra']['run']} | {e['extra']['entropy']} | "
                      f"{e['triage'][0]} | {md_escape(e['triage'][1])} | {e['n_occ']} | {md_escape(e['first'])} |")
        w("")
        for v, e in tab.items():
            if e["triage"][0] == "UNTRIAGED":
                untriaged_precise.append(("context_free", v, e))
            if e["triage"][0] == "TRUE-SECRET-CANDIDATE":
                true_candidates.append(("context_free", v, e))

    cf_table("Context-free high-entropy runs over every text blob and message (no assignment context needed)", cf)

    # ---- headers
    w("### (i-b) Commit and tag headers")
    w("")
    w(f"Every commit header ({hdr['n_commit_headers']}) and tag header ({hdr['n_tag_headers']}) -- the lines "
      f"before the message: tree / parent / author / committer / gpgsig, or object / type / tag / tagger. "
      f"`git log -p` never prints these; the message scan above reads only the part after the blank line. "
      f"Header keys: " + ", ".join(f"`{k}` {v}" for k, v in sorted(hdr["keys"].items())) + ".")
    w("")
    sig_groups = collections.defaultdict(list)
    for sha_, sg in hdr["sigs"]:
        sig_groups[(sg.get("armor"), sg.get("key_type"), sg.get("namespace"), sg.get("hash"),
                    sg.get("fingerprint"))].append(sha_)
    w(f"- Signed commits (gpgsig): {len(hdr['sigs'])}; distinct signing keys: {len(sig_groups)}.")
    for (arm, kt, ns, ha, fp), shas_ in sig_groups.items():
        auth = collections.Counter(git("log", "-1", "--format=%an <%ae> %as", s_).decode().strip() for s_ in shas_)
        auth_s = ", ".join(f"{(x if 'noreply@anthropic.com' in x else red(x))} x{k}" for x, k in auth.items())
        w(f"  - `{arm}`: key type {kt}, namespace `{ns}`, hash {ha}, public-key fingerprint "
          f"`{red(fp) if fp else '-'}` -- verdict PUBLIC-KEY: the signer's public key, embedded in every SSH "
          f"signature and published with the commit by design; not a credential. Commits: "
          + ", ".join(f"`{s_[:10]}`" for s_ in shas_) + f". Author/date: {auth_s}. Tips of refs among them: "
          + (", ".join(f"`{n_}`" for n_, s_, _ in refs if s_ in shas_) or "none") + ".")
    w(f"- Identity emails in author/committer/tagger header lines: {sum(hdr['identity_occ'].values())} "
      f"occurrences of {len(hdr['identity_occ'])} distinct address(es): "
      + ", ".join(f"`{(e_ if e_ == 'noreply@anthropic.com' else red(e_))}` {k}" for e_, k in
                  hdr["identity_occ"].most_common()) + ".")
    hp_vd = collections.Counter()
    for name in hdr["precise"]:
        for v, e in hdr["precise"][name].items():
            hp_vd[e["triage"][0]] += 1
            if e["triage"][0] == "UNTRIAGED":
                untriaged_precise.append(("header:" + name, v, e))
            if e["triage"][0] == "TRUE-SECRET-CANDIDATE":
                true_candidates.append(("header:" + name, v, e))
    hp_groups = collections.OrderedDict()
    for n_, t in hdr["precise"].items():
        for v, e in t.items():
            hp_groups.setdefault((n_, e["triage"][0], e["triage"][1]), []).append(
                (red(v, sensitive=e["triage"][2]), e["first"]))
    w(f"- Precise patterns (all {len(PRECISE)}) over the headers: "
      f"{sum(len(t) for t in hdr['precise'].values())} distinct values"
      + (": " + "; ".join(f"{n_}: {len(vs)} {vd_} ({rs_}): " + ", ".join(f"`{r_}` at {f_}" for r_, f_ in vs)
                          for (n_, vd_, rs_), vs in hp_groups.items()) if hp_groups else "") + ".")
    hid = []
    for cls, tab in hdr["ids"].items():
        for v, e in tab.items():
            if cls == "email_address" and v == "noreply@anthropic.com":
                e["triage"] = ("PUBLIC", "service attribution address", False)
            elif cls == "email_address":
                e["triage"] = ("METADATA", "a commit/tag identity's email (the identities table below)", True)
            elif cls == "dot_local_hostname":
                e["triage"] = ("METADATA", "the domain of a commit identity's email (the identities table below)",
                               v not in SAFE_VERBATIM)
            else:
                e["triage"] = triage_identifier(cls, v, e)
            hid.append((cls, v, e))
            if e["triage"][0] == "UNTRIAGED":
                untriaged_precise.append(("header-id:" + cls, v, e))
    w(f"- Identifier patterns over the headers: " + ("; ".join(
        f"{cls} `{v if (v in SAFE_VERBATIM or (e['triage'][0] == 'PUBLIC' and not e['triage'][2])) else red(v, sensitive=e['triage'][2])}`"
        f" x{e['n_occ']} {e['triage'][0]}" for cls, v, e in hid) or "none") + ".")
    w("")
    cf_table("Context-free high-entropy runs over the headers", hdr["cf"])
    al_ = hdr["armor_lines"]
    al_below = {k: v for k, v in al_.items() if v[1] <= 4.3}
    b64s = hdr["b64stats"]
    km_counts = {n_: (len(precise[n_]), len(hdr["precise"][n_]), len(binc["precise"][n_]),
                      collections.Counter(e["triage"][0] for e in hdr["precise"][n_].values()))
                 for n_ in sorted(KEY_MATERIAL_PATTERNS)}
    w("**Sensitivity limit of the 4.3 bar: structured base64.** Base64 of wire-format data (length prefixes, "
      "key-type names, zero bytes) has lower character entropy than base64 of random bytes, so a context-free "
      "bar of 4.3 bits/char can miss it. Measured here: the gpgsig headers hold "
      f"{len(al_)} distinct armor body lines of 16+ characters; {len(al_below)} of them are at or below 4.3 "
      + (f"(entropy {min(v[1] for v in al_below.values())}-{max(v[1] for v in al_below.values())}; "
         f"{sum(1 for v in al_below.values() if v[2])} of them contain an upper, a lower and a digit) "
         if al_below else "")
      + "and so are not in the context-free table above; the signatures are read in full by the parse above, "
        "so nothing is lost for them. Over blobs and messages, distinct strict-base64 runs (`[A-Za-z0-9+/]{64,}` "
        "with optional `=` padding; not preceded by a base64 character, `=`, `_`, `-` or `.`, nor followed by a "
        "base64 character, `=`, `_` or `-`; containing an upper, a lower and a digit): "
        f"{len(b64s['runs64'])}, of which at or below 4.3: {len(b64s['runs64_below'])}"
      + (" (" + "; ".join(f"`{red(x['value'])}` entropy {x['entropy']} at {x['first']}"
                          for x in b64s["runs64_below"].values()) + ")" if b64s["runs64_below"] else "")
      + ". The case that matters "
        "-- a private-key body pasted without its PEM armor -- is covered by the key-material marker patterns "
        "(above): "
      + "; ".join(f"{n_}: {a_} distinct in blobs/messages, {b_} in binary content, {c_} in headers ("
                  + (", ".join(f"{k} {v}" for k, v in d_.items()) or "-") + ")"
                  for n_, (a_, c_, b_, d_) in km_counts.items())
      + ". The bar's blind spot is otherwise unmeasured: a structured secret that is neither a key blob nor "
        "assignment-shaped would need the block's primary scanners (pre-flip step 4).")
    w("")

    # ---- binary content
    w("### (i-b) String content of the binary blobs")
    w("")
    w(f"The {stats['binary_blobs']} binary blobs (every version; listed under (v)/(iv)): {binc['members']} npz "
      f"members read (`zipfile`; .npy headers parsed); member dtypes "
      + ", ".join(f"`{k}` {v}" for k, v in binc["dtypes"].most_common())
      + f"; {binc['unicode_members']} unicode members decoded as UTF-32LE; {binc['ascii_runs']:,} printable-ASCII "
        f"runs of >= 8 characters extracted from every member; PNG chunks "
      + (", ".join(f"`{k}` {v}" for k, v in sorted(binc["png_chunks"].items())) or "none")
      + f" (text-chunk keywords: {', '.join('`' + k + '`' for k in binc['png_text_keys']) or 'none'}); other "
        f"binary formats: {binc['other_binary']}. Characters scanned: {binc['chars_scanned']:,}. Every precise "
        f"pattern, the identifier patterns and the context-free scan were run over this text.")
    w("")
    bp_n = sum(len(t) for t in binc["precise"].values())
    bi = [(cls, v, e) for cls, tab in binc["ids"].items() for v, e in tab.items()]
    for cls, v, e in bi:
        e["triage"] = triage_identifier(cls, v, e)
        if e["triage"][0] == "UNTRIAGED":
            untriaged_precise.append(("binary-id:" + cls, v, e))
    for name in binc["precise"]:
        for v, e in binc["precise"][name].items():
            if e["triage"][0] == "UNTRIAGED":
                untriaged_precise.append(("binary:" + name, v, e))
    w(f"- Precise-pattern hits: {bp_n} distinct values"
      + (": " + "; ".join(f"{n_} `{red(v, sensitive=e['triage'][2])}` {e['triage'][0]} at {e['first']}"
                          for n_, t in binc["precise"].items() for v, e in t.items()) if bp_n else "") + ".")
    w(f"- Identifier-pattern hits: {len(bi)}"
      + (": " + "; ".join(f"{cls} `{v if (e['triage'][0] == 'PUBLIC' and not e['triage'][2]) else red(v, sensitive=e['triage'][2])}` "
                          f"{e['triage'][0]} ({e['triage'][1]}) at {e['first']}" for cls, v, e in bi) if bi else "") + ".")
    for v, e in binc["cf"].items():
        if e["triage"][0] == "UNTRIAGED":
            untriaged_precise.append(("binary:context_free", v, e))
    w(f"- Context-free high-entropy runs: {len(binc['cf'])} distinct"
      + (": " + "; ".join(f"`{red(v, sensitive=e['triage'][2])}` {e['triage'][0]} ({e['triage'][1]}) at {e['first']}"
                          for v, e in binc["cf"].items()) if binc["cf"] else "") + ".")
    w("")
    w(f"**Credential-file shapes by path** (any path ever committed matching .netrc, .git-credentials, "
      f".env, credentials, id_rsa/id_ed25519, *.pem/*.key/*.p12, secrets.*): "
      f"{len(cred_files)}" + (": " + ", ".join(f"`{p}`" for p in cred_files) if cred_files else "."))
    w("")
    pp = ids["passphrase_shaped (code word / pass phrase / password context)"]
    w(f"**Pass-phrase-shaped text (hard rule 5):** {len(pp)} distinct value(s) captured after a "
      f"code-word / pass-phrase / password context (pattern in (ii)); every occurrence re-counted exactly:")
    w("")
    for v, e in pp.items():
        tri = manual(v) or ("UNTRIAGED", "needs individual triage", True)
        ex = exact.get(v, {})
        w(f"- `{red(v)}` -- {tri[0]}: {tri[1]}. Context hits {e['n_occ']}; exact occurrences anywhere "
          f"{ex.get('n_occ', '?')} in {len(ex.get('sources', ()))} blobs/messages, {ex.get('n_occ_head', '?')} at "
          f"HEAD ({', '.join(sorted(ex.get('head_paths', ()))) or '-'}); first {ex.get('first') or e['first']}.")
    w("")
    w("`CONTINUITY.md` (cited in one raw as never tracked): paths ever tracked matching `continuity` "
      f"(case-insensitive): {sum(1 for p_ in all_paths if 'continuity' in p_.lower())}.")
    w("")
    w(f"The word `continuity` (case-insensitive) over every text blob version and message: {cont['occ']} "
      f"occurrences in {cont['sources']} sources ({len(cont['paths'])} distinct paths incl. `<commit message>`), "
      f"{cont['head_occ']} in blobs at HEAD -- a design word in the lab's documents. The phrases `continuity "
      f"password` / `pass phrase` / `code word`: {len(cont['phrases'])} occurrence(s) ("
      + "; ".join(f"{md_escape(x['locator'])}{' (HEAD)' if x['at_head'] else ''}" for x in cont["phrases"])
      + f"); followed by a value (`is` / `was` / `:` / `=` then a word): "
        f"{sum(x['value_follows'] for x in cont['phrases'])}. N12(iii) itself (the PI's out-of-band search for the "
        f"password) is not part of this raw.")
    w("")
    n_fb = len(grep_lines)
    w("**Pass/STOP line (i):** "
      + (f"STOP -- {len(true_candidates)} TRUE-SECRET-CANDIDATE value(s) in history (history rewriting is "
         f"the PI's decision)." if true_candidates else
         (f"PENDING -- {len(untriaged_precise)} value(s) UNTRIAGED." if untriaged_precise else
          f"STOP pending the PI's resolution, on the block's literal text (:77, 'Any hit in history is a "
          f"STOP on the release') -- the fallback returns {n_fb} hit lines, so (i) is not 'no hits'. "
          f"Code's triage: 0 TRUE-SECRET-CANDIDATE among the fallback's hits (every occurrence assigned "
          f"to a prose/identifier rule; every credential-shaped one inspected) and 0 among the "
          f"precise-pattern, in-context and context-free high-entropy hits over every text blob, message, "
          f"commit/tag header and binary blob's string content; {len(pp)} pass-phrase-shaped "
          f"value(s) reported redacted (above). The block's pass is '(i) no hits, or hits resolved by the "
          f"PI'; resolving them is the PI's decision, not Code's.")))
    w("")

    # ---- (ii)
    w("## (ii) Identifiers")
    w("")
    w("### Commit identities (metadata; published with the history)")
    w("")
    w("| role | name | email (redacted unless a service address) | email domain | commits |")
    w("|---|---|---|---|---|")
    service = {"noreply@anthropic.com"}
    for role, ctr in (("author", authors), ("committer", committers)):
        for (nm, em), cnt in ctr.most_common():
            dom = em.split("@")[-1]
            if em in service:
                shown, domshown = f"`{em}`", dom
            else:
                shown = f"`{red(em)}`"
                domshown = dom if dom in ("gmail.com", "jspace-lab.local") else f"`{red(dom)}` (a laptop hostname)"
            w(f"| {role} | {nm} | {shown} | {domshown} | {cnt} |")
    for (nm, em), cnt in hdr["taggers"].most_common():
        dom = em.split("@")[-1]
        shown = f"`{em}`" if em in service else f"`{red(em)}`"
        domshown = dom if dom in ("gmail.com", "jspace-lab.local", "anthropic.com") else f"`{red(dom)}` (a laptop hostname)"
        w(f"| tagger | {nm} | {shown} | {domshown} | {cnt} tag object(s): "
          + ", ".join(f"`{t_}`" for t_ in hdr["tagger_tags"][(nm, em)]) + " |")
    w("")
    w(f"Each identity email's occurrences across all commit and tag headers (author + committer + tagger lines): "
      + ", ".join(f"`{(e_ if e_ in service else red(e_))}` {k}" for e_, k in hdr["identity_occ"].most_common())
      + ". In blob and message content (the (ii) tables below): `noreply@anthropic.com` "
        f"{sum(e['n_occ'] for v, e in ids['email_address'].items() if v in service)}; other identity emails "
        f"{sum(e['n_occ'] for v, e in ids['email_address'].items() if v in identity_emails and v not in service)} "
        f"occurrences; `.local` names {sum(e['n_occ'] for e in ids['dot_local_hostname'].values())}; other "
        f"email addresses {sum(e['n_occ'] for v, e in ids['email_address'].items() if v not in identity_emails)} "
        f"({', '.join(sorted(v if v in service else red(v) for v in ids['email_address'] if v not in identity_emails)) or 'none'}).")
    w("")
    for (role, nm, em), hs in sorted(ident_commits.items()):
        if em.endswith(".local") and role == "author":
            w(f"- `.local` {role} identity {red(em)} ({nm}): commits "
              + ", ".join(f"`{h[:10]}`" for h in hs))
    w("")
    w("`jspace-lab.local` is a synthetic tool identity (the repository's own name + `.local`), not a "
      "machine; the other `.local` domain is the author's laptop hostname and is redacted here, but "
      "it IS public in those two commits' author headers once the history is published (rewriting "
      "them is a history rewrite: the PI's decision).")
    w("")
    w("### Identifier classes in content (every text blob of the history + commit/tag messages)")
    w("")
    w("Counts: `occ` = occurrences summed over every blob version and message (a line kept across "
      "40 versions of RESULTS.md counts 40 times); `src` = distinct blobs/messages -- in a class row, those "
      "holding any of the class's values (the union over its values, round 4: a source holding two of them counts "
      "once), in a value row, those holding that value; `HEAD` = "
      "occurrences in blobs present at HEAD; `new` = occurrences in sources new since the base. "
      "Context-discovered RunPod/container ids, the RunPod volume name (round 3), the Claude session link, the "
      "pass-phrase-shaped value and every SSH port whose triage is IDENTIFIER are re-counted exactly across the "
      "whole history (`exact` "
      "column: occurrences / at HEAD / new since base), word-bounded: no letter or digit may touch the value on "
      "either side, so a run inside a hex hash or a longer number is not counted. The class columns count "
      "context hits only (an SSH port counts only on a line with ssh/port/alias); the exact column counts the "
      "value wherever it occurs.")
    w("")
    w("| class | distinct | occ | src | HEAD occ | new | verdicts |")
    w("|---|---|---|---|---|---|---|")
    id_rows = []
    # round 4 (fourth checker, finding 1): the class row's src is the union of its values' sources; the summed
    # per-value count is kept for the values-check and the JSON
    id_class_src = collections.OrderedDict()
    for cls, tab in ids.items():
        id_class_src[cls] = (len(set().union(*(e["sources"] for e in tab.values()))) if tab else 0,
                             sum(len(e["sources"]) for e in tab.values()))
        vd = collections.Counter()
        for v, e in tab.items():
            if cls == "email_address" and v == "noreply@anthropic.com":
                e["triage"] = ("PUBLIC", "service attribution address (Co-Authored-By lines)", False)
            elif cls == "email_address" and v in identity_emails:
                e["triage"] = ("METADATA-ECHO", "a commit identity's email (see the identities table)", True)
            elif cls == "email_address" and v == "noreply@anthropic.com":
                e["triage"] = ("PUBLIC", "service attribution address", False)
            elif cls == "dot_local_hostname" and any(v and em.endswith("@" + v) for em in identity_emails):
                e["triage"] = ("METADATA-ECHO", "the domain of a commit identity's email",
                               v not in SAFE_VERBATIM)
            else:
                e["triage"] = triage_identifier(cls, v, e)
            vd[e["triage"][0]] += 1
            id_rows.append((cls, v, e))
        w(f"| {cls} | {len(tab)} | {sum(e['n_occ'] for e in tab.values())} | "
          f"{id_class_src[cls][0]} | {sum(e['n_occ_head'] for e in tab.values())} | "
          f"{sum(e['n_occ_new'] for e in tab.values())} | "
          f"{', '.join(f'{k} {v}' for k, v in vd.items()) or '-'} |")
    w("")
    w("Patterns (verbatim):")
    w("")
    for cls, p in ID_PATTERNS.items():
        if p is None:
            w(f"- {cls}: any 4-5 digit number (not a year) on a line matching `{SSH_LINE_RE.pattern}`, "
              f"number pattern `{PORT_NUM_RE.pattern}`; round 3: except a line whose every match is the word "
              f"'port' in `{CODE_PORT_RE.pattern}` (the software sense: a port of code) -- in history "
              f"{CODE_PORT_STATS['history_lines']} such line(s), carrying {CODE_PORT_STATS['history_numbers']} "
              f"4-5 digit number(s), so no history count changes")
        else:
            w(f"- {cls}: `{p}`")
    w("")
    w("Every identifier value, individually (redacted; public website hosts verbatim):")
    w("")
    w("| class | value | verdict | reason | occ | src | HEAD occ (paths) | exact occ / HEAD / new | first locator |")
    w("|---|---|---|---|---|---|---|---|---|")
    shown_per_class = collections.Counter()
    capped = collections.Counter()
    for cls, v, e in sorted(id_rows, key=lambda x: (list(ID_PATTERNS).index(x[0]), x[2]["first_order"] or 0)):
        if cls.startswith("local_temp_path") and shown_per_class[cls] >= 10:
            capped[cls] += 1
            continue
        shown_per_class[cls] += 1
        if e["triage"][0] == "PUBLIC" and cls == "url_host":
            shown = f"`{v}`"
        elif e["triage"][0] == "PUBLIC" and cls == "email_address":
            shown = f"`{v}`"
        else:
            shown = f"`{v}`" if v in SAFE_VERBATIM else f"`{show(cls, v, sensitive=e['triage'][2])}`"
        hp = ", ".join(sorted(e["head_paths"])[:3]) + (" ..." if len(e["head_paths"]) > 3 else "")
        ex = exact.get(v)
        exs = f"{ex['n_occ']} / {ex['n_occ_head']} / {ex['n_occ_new']}" if ex else "-"
        w(f"| {cls} | {shown} | {e['triage'][0]} | {md_escape(e['triage'][1])} | {e['n_occ']} | "
          f"{len(e['sources'])} | {e['n_occ_head']} ({md_escape(hp) or '-'}) | {exs} | {md_escape(e['first'])} |")
    w("")
    for cls, k_ in capped.items():
        w(f"- {cls}: {k_} further distinct values not listed here (all in the JSON, `identifiers`).")
    real_ips = [v for v, e in ids["ipv4_address"].items() if e["triage"][0] != "FALSE-POSITIVE"]
    w(f"- IPv4 addresses that are not loopback/unspecified or not otherwise cleared: {len(real_ips)}; "
      f"public-shaped or private addresses identifying a machine: "
      f"{sum(1 for v in real_ips if ip_class(v) != 'loopback (127/8)')}.")
    known_ids = set()
    for c_ in ("runpod_pod_id (context: pod)", "runpod_volume_id (context: volume)",
               "runpod_endpoint_or_template_id (context)"):
        known_ids |= set(ids[c_])
    sw_cls = collections.Counter()
    sw_other = []
    for v, e in sweep.items():
        if v in known_ids:
            sw_cls["a context-discovered RunPod id (above)"] += 1
        elif re.match(r"u[0-9a-f]{4}", v):
            sw_cls["a JSON \\uXXXX escape fused with the next word (model text)"] += 1
        elif e["paths"] <= {"paper_analysis.ipynb"}:
            sw_cls["a fragment of the notebook's embedded base64 PNG"] += 1
        else:
            sw_other.append((v, e))
    w(f"- Context-free id-shape sweep ({SWEEP_DESC}): {len(sweep)} distinct tokens: "
      + ", ".join(f"{n_} {k_}" for k_, n_ in sw_cls.most_common())
      + f", and {len(sw_other)} other(s)"
      + (": " + "; ".join(f"`{red(v, sensitive=(manual(v) or ('', '', True))[2])}` in "
                          f"{', '.join(sorted(e['paths']))[:80]} (first {e['first']}) -- "
                          f"{(manual(v) or ('UNTRIAGED', 'needs individual triage'))[0]}: "
                          f"{(manual(v) or ('UNTRIAGED', 'needs individual triage'))[1]}" for v, e in sw_other)
         if sw_other else "")
      + (". Every token in the sweep is either a context-discovered id or cleared: no token of these "
         "two shapes outside the context-discovered ids is a RunPod id (ids of other shapes are not "
         "covered by this sweep)." if all((manual(v) or ("",))[0] == "FALSE-POSITIVE"
                                                               for v, _ in sw_other)
         else ". UNTRIAGED tokens remain in the sweep (see above)."))
    w(f"- In blob and message content: RunPod hostnames (*.runpod.io/net), SSH gateway users, proxy hosts, SSH "
      f"public keys, SSH fingerprints, `id_*` key names, `ssh -i` identity files, cloud account ids: "
      + ", ".join(f"{len(ids[c])}" for c in ("runpod_hostname (*.runpod.io / *.runpod.net)",
                                             "runpod_ssh_gateway_user", "proxy_hostname", "ssh_public_key",
                                             "ssh_fingerprint", "ssh_key_name (id_*)",
                                             "ssh_identity_flag (ssh -i <file>)", "cloud_account_id"))
      + f" distinct values respectively. Commit headers are a different source: {len(hdr['sigs'])} gpgsig "
        f"headers embed {len(sig_groups)} SSH signing public key(s) (see (i-b) headers).")
    w("")
    w("**Identifiers present at HEAD** (every value whose verdict is IDENTIFIER and which occurs in a blob at "
      "HEAD -- the ones a HEAD-only edit could remove; history keeps them either way, and rewriting history is "
      "the PI's decision). Exact, word-bounded counts with every HEAD locator; `at base` = the same count at "
      f"the base `{since[:10]}`:")
    w("")
    w("| class | value (redacted) | exact occ (sources) | new since base | at base | HEAD occ | HEAD locators | HEAD locators at base |")
    w("|---|---|---|---|---|---|---|---|")
    ident_head_rows = []
    for cls, v, e in sorted(id_rows, key=lambda x: (list(ID_PATTERNS).index(x[0]), x[2]["first_order"] or 0)):
        if e["triage"][0] != "IDENTIFIER":
            continue
        ex = exact.get(v)
        if not ex:
            continue
        ident_head_rows.append((cls, v, e, ex))
        if not ex["n_occ_head"] and not ex["n_occ_base_head"]:
            continue
        w(f"| {cls} | `{show(cls, v)}` | {ex['n_occ']} ({len(ex['sources'])}) | {ex['n_occ_new']} | "
          f"{ex['n_occ'] - ex['n_occ_new']} | {ex['n_occ_head']} | {', '.join(ex['head_locators']) or '-'} | "
          f"{', '.join(ex['base_head_locators']) or ('-' if m.get('base_objs') is not None else 'same')} |")
    w("")
    code_locs = collections.OrderedDict()
    for cls, v, e, ex in ident_head_rows:
        for loc in ex["head_locators"]:
            f_, ln_ = loc.rsplit(":", 1)
            if f_.endswith((".py", ".sh")):
                code_locs.setdefault((f_, cls, v), []).append(ln_)
    w("IDENTIFIER values in tracked code (.py/.sh) at HEAD: " + ("; ".join(
        f"{f_}:{','.join(lns)} ({cls} `{show(cls, v)}`: {CODE_LOCATOR_NOTES.get(f_, 'not yet read in context')})"
        for (f_, cls, v), lns in code_locs.items()) or "none") + ".")
    w("")
    w("IDENTIFIER values in history but not at HEAD: " + (", ".join(
        f"{cls} `{show(cls, v)}` ({ex['n_occ']} occ, first {ex['first']})" for cls, v, e, ex in ident_head_rows
        if not ex["n_occ_head"]) or "none") + ".")
    w("")
    w("### Tracked files at HEAD containing `/Users/`")
    w("")
    groups = collections.defaultdict(list)
    for p, c in sorted(users_at_head.items()):
        if p.startswith("results/raw/"):
            g_ = "results/raw (raw stdout / review records)"
        elif p.startswith("data/"):
            g_ = "data/ artifacts"
        elif p.endswith((".py", ".sh")):
            g_ = "code"
        else:
            g_ = "documents"
        groups[g_].append((p, c))
    w(f"{len(users_at_head)} tracked files, {sum(users_at_head.values())} occurrences (byte-substring "
      f"count of `/Users/` in each HEAD blob).")
    w("")
    w("| group | files | occurrences | recommendation |")
    w("|---|---|---|---|")
    rec = {
        "results/raw (raw stdout / review records)": "leave: verbatim run records (rule 27); the paths are "
            "provenance of where a run executed, and nothing reads them",
        "data/ artifacts": "leave: provenance fields recorded by the run; parameterizing would rewrite a "
            "committed artifact",
        "code": "see per-file note: parameterize only if the path is used at run time",
        "documents": "leave (the audit block quotes the pattern)",
    }
    for g_, lst in sorted(groups.items()):
        w(f"| {g_} | {len(lst)} | {sum(c for _, c in lst)} | {rec[g_]} |")
    w("")
    w("| file | occurrences |")
    w("|---|---|")
    for p, c in sorted(users_at_head.items(), key=lambda x: (-x[1], x[0])):
        w(f"| `{p}` | {c} |")
    w("")
    code_users = groups.get("code", [])
    notes = []
    code_kinds = collections.Counter()   # round 5: the recommendation below is computed from these
    for p_, c_ in code_users:
        blob = git("show", f"{head}:{p_}").decode("utf-8", "replace")
        lines_ = [l for l in blob.split("\n") if "/Users/" in l]
        # round 5: classify each occurrence by the path segment after `/Users/` -- empty or pattern/prose text
        # (a regular-expression fragment, a placeholder, an ellipsis) names no home directory; `u` is the
        # synthetic fixture user; anything else names a user directory
        segs = [blob[mo_.end():].split("/", 1)[0] for mo_ in re.finditer(r"/Users/", blob)]
        bare = all(re.fullmatch(r"(?:u|[^A-Za-z0-9_].*)?", sg_.split("\n", 1)[0]) for sg_ in segs)
        if all("/Users/u/" in l for l in lines_):
            code_kinds["fixture"] += 1
            notes.append(f"`{p_}` ({c_}): every occurrence is the synthetic path `/Users/u/...` inside a "
                         f"canned process-list string a self-test parses; nothing reads it as a path -- no "
                         f"change needed")
        elif bare:
            code_kinds["pattern"] += 1
            notes.append(f"`{p_}` ({c_}): every occurrence is a bare `/Users/` prefix, pattern text (a regular "
                         f"expression or a class label) or the synthetic fixture user -- no home directory is "
                         f"named; no change needed (round 5)")
        else:
            code_kinds["real"] += 1
            notes.append(f"`{p_}` ({c_}): a real absolute path in code -- parameterize if a reader is "
                         f"expected to run it")
    w("Per-file note for code: " + ("; ".join(notes) if notes else "none") + ". `README.md` contains "
      "`/Users/`: " + ("YES" if "README.md" in users_at_head else "no") + ".")
    w("")
    w("Per-file note for data/ (does any tracked code read these paths?):")
    w("")
    for p_, c_ in groups.get("data/ artifacts", []):
        fields = collections.Counter()
        if p_.endswith(".json"):
            def walk(o, k=None):
                if isinstance(o, dict):
                    for kk, vv in o.items():
                        walk(vv, kk)
                elif isinstance(o, list):
                    for vv in o:
                        walk(vv, k)
                elif isinstance(o, str) and "/Users/" in o:
                    fields[k] += o.count("/Users/")
            walk(json.loads(git("show", f"{head}:{p_}")))
        refs_ = []
        for needle in [os.path.splitext(os.path.basename(p_))[0]] + list(fields):
            out_ = git("grep", "-n", "-F", needle, head, "--", "*.py", check=False).decode("utf-8", "replace")
            for l in out_.split("\n"):
                if not l:
                    continue
                body = l.split(":", 3)[3] if l.count(":") >= 3 else l
                if needle in fields:
                    q = re.escape(needle)
                    if re.search(r"\[\s*[\"']" + q + r"[\"']\s*\]|\.get\(\s*[\"']" + q + r"[\"']", body):
                        kind_ = "READS the key"
                    elif re.search(r"[\"']" + q + r"[\"']\s*:", body):
                        kind_ = "writes the key (dict literal)"
                    else:
                        continue  # the word, not the key
                else:
                    kind_ = "comment" if body.strip().startswith("#") else "code naming the file"
                refs_.append(f"`{':'.join(l.split(':', 3)[1:3])}` ({kind_}, `{needle}`)")
        w(f"- `{p_}` ({c_}): /Users/ inside field(s) "
          + (", ".join(f"`{k_}` ({n_})" for k_, n_ in fields.most_common()) or "-")
          + "; tracked .py lines at HEAD naming the file or a field as a key: "
          + ("; ".join(refs_) if refs_ else "none") + ".")
    w("")
    code_desc = " and ".join(x_ for x_, k_ in (("a test fixture", "fixture"), ("pattern text naming no home directory",
                                                                          "pattern")) if code_kinds[k_])
    w(("Recommendation: none of these files needs a change before release (the code hits are "
       + (code_desc or "none") + "; " if not code_kinds["real"] else
       f"Recommendation: {code_kinds['real']} code file(s) name a real home directory (per-file notes above: "
       "parameterize if a reader is expected to run them); the other files need no change before release (")
      + "the data/ and raw paths are recorded provenance, not inputs -- see the per-file notes for the "
        "lines that name them); the README should not cite any of these paths.")
    w("")
    hk = hp_out["kinds"]
    env_s = []
    for nm in hp_out["env_names"]:
        fl = hp_out["env_files"].get(nm, {})
        env_s.append(f"`{red(nm)}` in {len(fl)} HEAD file(s) ({', '.join(f'`{p_}`' for p_ in sorted(fl))})"
                     + (" -- equal to the notebook's kernel display name" if nm == hp_out["notebook_display_name"]
                        else ""))
    w("Informational (not a secret; a second checker's note): `/Users/` paths at HEAD that point outside the "
      f"repository: {sum(hk.values())} occurrence(s) in {len({p_ for s_ in hp_out['kind_files'].values() for p_ in s_})} "
      "file(s), by kind: "
      + "; ".join(f"{k_} {n_} ({', '.join('`' + p_ + '`' for p_ in sorted(hp_out['kind_files'][k_]))})"
                  for k_, n_ in hk.most_common())
      + ". They disclose the author's local layout: the Jupyter runtime directory, the conda installation, and "
        "the name of a conda environment belonging to another local project -- "
      + ("; ".join(env_s) or "none")
      + " (the name is printed redacted here; it is public at HEAD in those files). Nothing to fix before "
        "release; listed so the PI is not surprised.")
    w("")
    w("### Tracked files at HEAD containing `/workspace/` (box paths)")
    w("")
    w(f"{len(workspace_at_head)} files, {sum(workspace_at_head.values())} occurrences.")
    w("")
    w("| file | occurrences |")
    w("|---|---|")
    for p, c in sorted(workspace_at_head.items(), key=lambda x: (-x[1], x[0])):
        w(f"| `{p}` | {c} |")
    w("")

    # ---- (v)
    w("## (v) Size")
    w("")
    w("`git count-objects -vH` (stdout verbatim):")
    w("")
    w("```")
    w(count_objects.stdout.decode().rstrip())
    w("```")
    garb = [l for l in count_objects.stderr.decode().split("\n") if l.strip()]
    w("")
    w(f"stderr: {len(garb)} lines, all `warning: garbage found: .git/objects/??/tmp_obj_*` "
      f"({'yes' if all('garbage found' in l and 'tmp_obj_' in l for l in garb) else 'NO -- see JSON'}): "
      f"temporary object files left in the local object store (consistent with an interrupted or "
      f"concurrent object write); they are not objects, are unreachable from any ref, and are never "
      f"pushed.")
    w("")
    w("Tracked files at HEAD over 40 MB (MB = 10^6 bytes, MiB = 2^20; GitHub warns above 50 MiB "
      "and refuses above 100 MiB):")
    w("")
    w("| file | bytes | MB | MiB | >50 MB | >50 MiB | >100 MB | >100 MiB |")
    w("|---|---|---|---|---|---|---|---|")
    yn = lambda b: "YES" if b else "no"
    for r in head_big:
        w(f"| `{r['path']}` | {r['size']:,} | {r['MB']} | {r['MiB']} | {yn(r['over_50MB'])} | "
          f"{yn(r['over_50MiB'])} | {yn(r['over_100MB'])} | {yn(r['over_100MiB'])} |")
    n50 = sum(r["over_50MB"] for r in head_big)
    n50i = sum(r["over_50MiB"] for r in head_big)
    n100 = sum(r["over_100MB"] for r in head_big)
    w("")
    w(f"Over 50 MB: {n50}; over 50 MiB (GitHub's warning): {n50i}; over 100 MB: {n100}; over 100 MiB: "
      f"{sum(r['over_100MiB'] for r in head_big)}.")
    w("")
    w("The 25 largest blobs reachable from any ref:")
    w("")
    w("| # | blob | bytes | MB | MiB | path(s) | first commit | at HEAD? |")
    w("|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(largest, 1):
        w(f"| {i} | `{r['blob'][:10]}` | {r['size']:,} | {r['MB']} | {r['MiB']} | "
          f"{', '.join(f'`{p}`' for p in r['paths'])} | `{(r['first_commit'] or '?')[:8]}` | {r['status']} |")
    w("")
    all_anc = all(ancestry.values())
    w(f"Largest blob anywhere in history: {max_blob:,} bytes = {max_blob / MIB:.3f} MiB "
      f"({'under' if max_blob <= 100 * MIB else 'OVER'} GitHub's 100 MiB refusal limit; "
      f"{'under' if max_blob <= 50 * MIB else 'over'} its 50 MiB warning). Every locally visible ref is an "
      f"ancestor of `origin/main` as this clone last saw it: {'yes' if all_anc else 'NO'} -- so every blob "
      f"reachable from them is already in history GitHub accepted on push. Refs that exist only on GitHub "
      f"(branches pushed by other sessions and never fetched, `refs/pull/*`, remote-only tags) are not visible "
      f"in this clone and were not scanned or size-checked; this audit uses no network.")
    w("")
    w(f"Local object store: {n_store} objects; reachable from no ref (the live refs at the run, not the pin): "
      + (", ".join(f"{k} {v}" for k, v in sorted(unreach.items())) or "none")
      + f" ({unreach_bytes:,} bytes); this audit opens none of their contents (for an unreachable commit it reads "
        f"only the header's committer time and parent, below). A push sends only objects reachable from the "
        f"pushed refs, so these are not published by a visibility change.")
    w("")
    rl = reflogs
    w("Push history visible locally (remote-tracking reflogs under `.git/logs/refs/remotes/`, read as plain "
      "files; the email field of each line is never read out): "
      + "; ".join(f"`{r_['ref']}`: {r_['entries']} entries ("
                  + ", ".join(f"'{k_}' {n_}" for k_, n_ in r_["kinds"].items())
                  + f"), every update a fast-forward: {'yes' if r_['all_fast_forward'] else 'NO'}, every recorded "
                    f"value an ancestor of the ref's last value: {'yes' if r_['all_ancestors_of_last'] else 'NO'}, "
                    f"first entry `{r_['first']}` at {r_['first_time']}" for r_ in rl["remote"])
      + ". "
      + (f"First push recorded: {rl['first_push']['time']} (`{rl['first_push']['commit']}`). "
         if rl["first_push"] else "No push recorded. ")
      + ("Unreachable commit(s): " + "; ".join(
          f"`{u_['commit']}` (committer time {u_['committer_time']}; before the first push: "
          f"{'yes' if u_['before_first_push'] else 'NO'}; in a remote-tracking reflog: "
          f"{'YES' if u_['in_remote_reflogs'] else 'no'}; in the local HEAD/branch reflogs: "
          f"{'yes' if u_['in_local_reflogs'] else 'no'}; reachable commit with the same parent and subject: "
          + (", ".join(f"`{t_['commit']}` ({t_['seconds_after']} s later)"
                       for t_ in u_["reachable_twin_same_parent_and_subject"]) or "none") + ")"
          for u_ in rl["unreachable_commits"]) + "." if rl["unreachable_commits"] else "No unreachable commit.")
      + (" So on local evidence no force-push was recorded"
         if all(r_["all_fast_forward"] for r_ in rl["remote"]) else " A NON-fast-forward update IS recorded")
      + (" and no unreachable commit was pushed from this clone."
         if all(not u_["in_remote_reflogs"] for u_ in rl["unreachable_commits"])
         else "; an unreachable commit appears in a remote-tracking reflog (see the JSON, `reflogs`).")
      + " This cannot see pushes made from other machines between this clone's fetches (the "
        "`claude/handoff-doc-next-steps-oeccd1` branch was pushed from a cloud session -- see the gpgsig "
        "subsection), nor anything GitHub holds outside the refs.")
    w("")
    w("**PI pre-flip steps (not run here; each needs the final HEAD, the network, or the PI's word):**")
    w("")
    w(f"1. **A precondition of the end commit and the tag (the PI's to bind), not advice: every audit raw must be "
      f"re-scanned before the release commit.** Re-run "
      f"this script immediately before the release commit, with every raw, script and README of the end commit "
      f"in place, and again at the release commit itself; its pre-release section (below, after (iv)) must "
      f"show no redaction-rule value -- a RunPod pod or volume id, the volume name or its stem, an SSH port, the "
      f"SSH signing-key fingerprint, the container hostname, the Claude session link or the pass-phrase-shaped "
      f"value -- in any file the end commit adds, and no new value needing triage (round 4: among them any email "
      f"address other than the service address and the commit identities' own -- the scan's only class of "
      f"third-party personal data; a third party's name, postal address or phone number is not scanned for, so "
      f"the pre-release line's CLEAN does not cover them). The commit identities' own "
      f"metadata (the identity emails and the laptop hostname, public in the commit headers) is listed there "
      f"for consistency with this raw's redaction and, as drafted (round 3), does not hold the tag; binding "
      f"either part is the PI's call. This raw is a snapshot at `{head[:10]}`; commits landing later -- the "
      f"concurrent PROPOSAL-m session's, and the audit's own end commit -- are not covered by it."
      + (" Evidence that a snapshot goes stale: after the round-2 run (at `bab921ce52`), "
         + ", ".join(f"`{c_[:10]}`" for c_ in ckpt_after_r2)
         + f" added the first tracked file(s) under `data/m/ckpt/` ({len(ckpt_paths)}: "
         + ", ".join(f"`{p_}`" for p_ in ckpt_paths)
         + "), a `-diff` path whose content `git log -p` does not print, which turned coverage limit (2) under "
           "(i-a) from 'never applied' into 'applies'." if ckpt_after_r2 else "")
      + " The tag should wait on a clean run.")
    w("2. `git ls-remote origin` and compare its refs with the refs table under Scope. Any extra branch or tag "
      "gets its own scan (re-run this script after fetching it) or is deleted before the visibility change. "
      "`refs/pull/*` refs cannot be deleted by the owner and become public with the repository.")
    w("3. GitHub-side surfaces that become public with the visibility change and cannot be checked offline: "
      "pull requests (titles, bodies, comments, review comments; `gh pr list --state all`; the "
      "`claude/handoff-doc-next-steps-oeccd1` branch came from a cloud session and may have a PR), issues and "
      "their comments, Actions runs with their logs and artifacts, the wiki, and releases with their assets. "
      "GitHub can keep commits that were force-pushed away from another machine reachable by sha (and through "
      "`refs/pull/*`); the local evidence above cannot rule that out.")
    w("4. The block's primary scanners, on the PI's word (installing them needs it): `brew install gitleaks "
      "trufflehog`, then `gitleaks detect --source . --log-opts=\"--all\"` and `trufflehog git file://.` over "
      "the repository at the release commit. Their findings supersede the fallback's for (i).")
    w("")
    w("**Pass/STOP line (v):** " + ("PASS -- nothing over 100 MB untreated (no tracked file at HEAD and no "
                                    "blob anywhere in history exceeds 100 MB or 100 MiB)."
                                    if max_blob <= 100 * MB else
                                    "STOP -- a blob over 100 MB exists; see table (LFS or a release asset "
                                    "is the PI's call)."))
    w("")

    # ---- (iv)
    w("## (iv) mechanical checks")
    w("")
    w(f"- `jlens-qwen36/` tracked at HEAD: {len(jlens_head)} paths; ever tracked in history "
      f"(`git log --all --name-only`, raw diffs, and `rev-list --objects` paths unioned): "
      f"{len(jlens_hist)} paths. Gitlinks (mode 160000) at HEAD: {len(gitlinks)}. `.gitmodules` at "
      f"HEAD: {'yes' if '.gitmodules' in m['head_files'] else 'no'}.")
    jm_nonempty = [x for x in jl["matches"] if x["blob"] != EMPTY_BLOB]
    jm_empty = [x for x in jl["matches"] if x["blob"] == EMPTY_BLOB]
    jm_top = collections.Counter(x["jlens_path"].split("/")[0] for x in jm_nonempty)
    jm_sub = collections.Counter("/".join(x["jlens_path"].split("/")[:2]) for x in jm_nonempty)
    jm_code = [x for x in jm_nonempty if not x["jlens_path"].startswith("data/")]
    jm_samepath = sum(1 for x in jm_nonempty if x["jlens_path"] in x["tracked_paths"])
    w(f"- Content copies (the path check above cannot see them): every file in the jlens-qwen36/ working tree "
      f"outside `.git/` and `.venv/` was read as a plain file ({jl['files']} files; {jl['hashed']} whose size "
      f"equals some reachable blob's size were hashed as git blobs). Byte-identical to a reachable blob: "
      f"{len(jl['matches'])} -- {len(jm_empty)} are the empty blob (`{', '.join(x['jlens_path'] for x in jm_empty)}`; "
      f"an empty file matches any empty tracked file, e.g. `.gitkeep`), and {len(jm_nonempty)} are non-empty: "
      + ", ".join(f"`{k}/` {v}" for k, v in jm_sub.most_common())
      + f"; {jm_samepath} of them sit at the same relative path as their tracked copy (`jlens-qwen36/data/X` "
        f"= `data/X`). Non-empty matches outside `data/`: {len(jm_code)}"
      + (": " + ", ".join(f"`{x['jlens_path']}`" for x in jm_code) if jm_code else "")
      + (". The non-empty matches are under the clone's `data/` only, in directories named for the lab's own "
         "experiments and configs (as listed); no non-empty file of the clone outside `data/` -- its code, "
         "LICENSE, README -- matches any reachable blob."
         if not jm_code else ". Matches outside `data/` need individual review (listed above).")
      + " (Every match is listed in the JSON, `jlens.content_copies`.)")
    if jidx.get("present") and jidx.get("checksum_ok") is not None:
        w(f"- The clone's own index (round 2), read as a plain file -- no git process in the clone "
          f"(`jlens-qwen36/.git/index`, version {jidx['version']}, trailing SHA-1 checksum "
          f"{'verified' if jidx['checksum_ok'] else 'MISMATCH'}): {jidx['entries']} clone-tracked entries, "
          f"{jidx['nonempty_entries']} with a non-empty blob. The working-tree comparison above cannot see a "
          f"clone-tracked file whose working copy carries local patches; the index holds the blob sha of each "
          f"file's committed version, which closes that gap. Of the {jidx['nonempty_entries']} non-empty "
          f"clone-tracked blob shas, reachable anywhere in the lab's history: "
          f"{len(jidx['nonempty_reachable_in_lab'])}"
          + (": " + ", ".join(f"`{p_}`" for p_ in jidx["nonempty_reachable_in_lab"])
             if jidx["nonempty_reachable_in_lab"] else "")
          + f". Clone-tracked files whose working copy differs from the index: {len(jidx['modified_on_disk'])} ("
          + (", ".join(f"`{p_}`" for p_ in jidx["modified_on_disk"]) or "none")
          + f"). Of the {len(jm_nonempty)} non-empty byte-identical files above, clone-tracked: "
            f"{len(jidx['matched_files_clone_tracked'])}"
          + (": " + ", ".join(f"`{p_}`" for p_ in jidx["matched_files_clone_tracked"])
             if jidx["matched_files_clone_tracked"] else "")
          + f" -- the clone tracks only {len(jidx['data_entries'])} path(s) under `data/` ("
          + ", ".join(f"`{p_}`" for p_ in jidx["data_entries"])
          + "), so the matches are lab outputs written into the clone's untracked `data/`, not upstream "
            f"material. The {len(jm_empty)} empty-blob matches, clone-tracked: "
            f"{len(jidx['empty_matches_clone_tracked'])} (an empty file carries no content). "
          + ("So no upstream jlens-qwen36 file -- code, LICENSE, README or data -- is tracked in the lab's "
             "history, in its committed version or as patched on disk. (The N12-licenses raw reads the clone's "
             "object store for its own copy check of the upstream content.)"
             if not jidx["nonempty_reachable_in_lab"] and not jidx["matched_files_clone_tracked"] else
             "Upstream content IS present in the lab's history (listed above)."))
    else:
        w("- The clone's own index: not read (" + ("absent" if not jidx.get("present") else
                                                   f"unsupported index version {jidx.get('version')}") + ").")
    ci_agree = all(r["check_ignore_HEAD"] == f".gitignore:{r['explicit_allowlist_line_HEAD'][0]}:!/{r['path']}"
                   for r in npz_rows if r["explicit_allowlist_line_HEAD"])
    w(f"- Working-tree `.gitignore` byte-identical to HEAD's: {'yes' if gi_wt_ok else 'no (an uncommitted working-tree change outside this audit)'}. "
      f"The allowlist lines below are read from HEAD's `.gitignore` blob; `git check-ignore --no-index -v` "
      f"(which reads the working tree) is a cross-check, and its source line and pattern equal the HEAD "
      f"explicit line for every npz: {'yes' if ci_agree else 'NO'}.")
    w("")
    n_head_npz = sum(r["at_head"] for r in npz_rows)
    no_line = [r for r in npz_rows if not r["explicit_allowlist_line_HEAD"]]
    w(f"Every `.npz` path ever tracked: {len(npz_rows)} ({n_head_npz} at HEAD). Allowlist = an explicit "
      f"`!/<path>` line in `.gitignore`.")
    w("")
    w("| npz path | at HEAD | HEAD bytes | versions | introduced | explicit line (HEAD .gitignore) | check-ignore -v (HEAD) | explicit line at introduction | members |")
    w("|---|---|---|---|---|---|---|---|---|")
    for r in npz_rows:
        mem = ", ".join(r["npz_members"][:6]) + (f" (+{len(r['npz_members']) - 6})" if len(r["npz_members"]) > 6 else "")
        w(f"| `{r['path']}` | {'yes' if r['at_head'] else 'no'} | "
          f"{format(r['head_size'], ',') if r['head_size'] else '-'} | {r['n_versions']} | "
          f"`{(r['introduced'] or '?')[:8]}` | {', '.join(f':{x}' for x in r['explicit_allowlist_line_HEAD']) or 'NONE'} | "
          f"`{md_escape(r['check_ignore_HEAD'])}` | "
          f"{', '.join(f':{x}' for x in (r['explicit_allowlist_line_at_introduction'] or [])) or 'NONE'} | "
          f"{md_escape(mem)} |")
    w("")
    w(f"npz tracked without an explicit allowlist line at HEAD: {len(no_line)}"
      + (": " + ", ".join(f"`{r['path']}`" for r in no_line) if no_line else "."))
    w("")
    w(f"Model-weight-shaped paths ever tracked (extensions {', '.join(sorted(WEIGHT_EXT))}, or "
      f"adapter/weights/model-* names): {len(weights)}"
      + (": " + ", ".join(f"`{x['path']}`{' (at HEAD)' if x['at_head'] else ''}" for x in weights) if weights else ".")
      + " Binary blobs by extension (all versions): "
      + ", ".join(f"{k} {v}" for k, v in collections.Counter(ext_of(b['paths'][0]) if b['paths'] else '?' for b in binary).most_common())
      + ".")
    w("")
    fa = jv["float_arrays"]
    fa_by = collections.OrderedDict()
    for x in sorted(fa, key=lambda x: (x["paths"], x["pointer"])):
        fa_by.setdefault((", ".join(x["paths"]), x["blob"]), []).append(x)
    w(f"**Residual-space vectors stored as JSON (round 2).** The npz allowlist check cannot see numeric vectors "
      f"stored as JSON text, so every reachable JSON / JSONL / .ipynb blob (every version: {jv['blobs']} blobs; "
      f"parsed {jv['parsed']}, unparseable {len(jv['unparsed'])}) was walked for all-numeric arrays of 256 or "
      f"more elements. Float arrays: {len(fa)}, in {len(fa_by)} blob(s):")
    w("")
    w("| path(s) | blob | at HEAD | first commit | JSON pointer: length |")
    w("|---|---|---|---|---|")
    for (ps_, bl_), xs in fa_by.items():
        w(f"| `{ps_}` | `{bl_[:8]}` | {'yes' if xs[0]['at_head'] else 'no'} | `{(xs[0]['first_commit'] or '?')[:8]}` | "
          + ", ".join(f"`{md_escape(x['pointer'])}`: {x['length']}" for x in xs) + " |")
    w("")
    ig = jv["int_array_groups"]
    w(f"Integer-only arrays of 256+ elements: {jv['int_arrays']}"
      + (" (in " + str(len(ig)) + " (path, pointer-pattern) group(s): "
         + "; ".join(f"`{md_escape(p_)}` `{md_escape(q_)}` x{n_}" for (p_, q_), n_ in ig.most_common(12))
         + (" ..." if len(ig) > 12 else "") + "; not read in context -- residual values are floats)"
         if jv["int_arrays"] else "") + ".")
    w("")
    probe_fa = [x for x in fa if re.fullmatch(r"/readability/stored_classifier/(w|mu|sd)", x["pointer"])]
    other_fa = [x for x in fa if x not in probe_fa]
    probe_files = sorted({p_ for x in probe_fa for p_ in x["paths"]})
    w("Reading of the float arrays (Code read the writer in context): "
      + (f"in {', '.join('`' + p_ + '`' for p_ in probe_files)}, `/readability/stored_classifier/{{w,mu,sd}}` "
         f"(lengths {sorted({x['length'] for x in probe_fa})}) is a stored logistic readability probe -- its weight "
         "vector, and the per-dimension mean and standard deviation of its training features -- written by "
         "`scripts/e2d_score.py` (`fit_and_store` in `valence_core/e2d/readability.py`) over the model adapter's "
         "`embed`: the mean-pooled, post-norm final-layer residual of a generated text. These are residual-space "
         "vectors, but neither model weights nor raw activation captures (mu and sd are statistics over the fit "
         "set). " if probe_fa else "")
      + (f"Other float arrays: {len(other_fa)} (listed above; not read in context -- they need a reading before "
         "the README's statement is final). " if other_fa else "No other float arrays of 256+ elements. ")
      + "So (iv)'s clause, stated exactly: no model weights are tracked; and no residual arrays are tracked "
        "beyond the allowlisted `.npz` files"
      + (" EXCEPT the probe vectors in JSON named here, which the README should name." if probe_fa else "."))
    w("")
    # ---- pre-release check (round 2)
    pend_known = collections.OrderedDict()
    for v, ex in exact.items():
        tri = manual(v)
        if tri and tri[0] in ("IDENTIFIER", "PASSPHRASE-SHAPED"):
            pend_known[v] = ex["classes"]
    # round 3: the volume name's stem (the name without its _volume suffix) is guarded too; the scan's
    # alternation tries longer values first, so a full name is never also counted as its stem
    vol_stems = {}
    for v in list(pend_known):
        if VOLNAME_CLASS in pend_known[v] and VOLNAME_SUFFIX_RE.search(v):
            st_ = VOLNAME_SUFFIX_RE.sub("", v)
            if len(st_) > 4:
                pend_known[st_] = ["runpod volume name stem (the name without its _volume suffix)"]
                vol_stems[st_] = v
                REDACTED_SENSITIVE.add(st_)   # the leak assertion covers the stem whether or not it is displayed
    for e_ in sorted(identity_emails):
        if e_ not in service:
            pend_known[e_] = ["identity email, public in the commit headers"]
        dom = e_.split("@")[-1]
        if dom.endswith(".local") and dom not in SAFE_VERBATIM:
            pend_known[dom] = ["laptop hostname"]
    for k in sig_groups:
        if k[4]:
            pend_known[k[4]] = ["SSH signing-key fingerprint"]
    excl = {os.path.relpath(os.path.join(ROOT, o), ROOT) for o in (a.out, a.json_out, DEFAULT_MD, DEFAULT_JSON)}
    pend = pending_scan(pend_known, excl)
    pend_stamp = sh(["date", "-u"]).stdout.decode().strip()

    def hdr_occ(v):
        """Occurrences of an author-identity value in the commit/tag header lines (published with the history)."""
        if v in hdr["identity_occ"]:
            return hdr["identity_occ"][v]
        e_ = hdr["ids"]["dot_local_hostname"].get(v)
        return e_["n_occ"] if e_ else 0

    # ---- round 3 (third checker, finding 6): enumeration exposure of the redacted forms, per sensitive value
    WORD_LABELS = (VOLNAME_CLASS, "runpod volume name stem (the name without its _volume suffix)",
                   "passphrase_shaped (code word / pass phrase / password context)",
                   "identity email, public in the commit headers", "laptop hostname")

    def exposure(v, labels):
        """(kind, alphabet, hidden, candidates, chance) -- kind: 'brute' (alphabet from the class's own pattern)
        or 'words' (a value built from words: a word-list search, whatever its length)."""
        if any(lb_ in WORD_LABELS for lb_ in labels):
            return ("words", None, None, None, None)
        if PORT_CLASS in labels:
            alph, hid = 10, len(v)                       # the port form shows no character
        elif any(lb_.startswith(("runpod_pod_id", "runpod_volume_id")) for lb_ in labels):
            alph, hid = 36, len(v) - 4                   # [a-z0-9], first 4 shown
        elif any(lb_.startswith("container_hostname") for lb_ in labels):
            alph, hid = 16, len(v) - 4                   # hex, first 4 shown
        elif "claude_session_or_artifact_link" in labels:
            alph, hid = 62, len(re.split(r"session_|artifact/|chat/", v, maxsplit=1)[-1])   # the id part
        elif "SSH signing-key fingerprint" in labels:
            alph, hid = 64, len(v.split(":", 1)[-1])     # base64 after 'SHA256:'
        else:
            alph, hid = 64, len(v) - 4
        cand = alph ** hid
        return ("brute", alph, hid, cand, cand / 2 ** 32)
    exp_rows = collections.OrderedDict()
    for v, lbs in pend_known.items():
        kind_, alph, hid, cand, chance = exposure(v, lbs)
        lab_ = "/".join(lbs)
        exp_rows.setdefault((lab_, kind_, alph, hid), []).append(v)
    fp_verbatim = len(ids["ssh_fingerprint"]) + len(hdr["ids"]["ssh_fingerprint"]) + len(binc["ids"]["ssh_fingerprint"])

    def in_history(v, lbs):
        if v in exact:
            return exact[v]["n_occ"]
        if v in vol_stems and vol_stems[v] in exact:
            return exact[vol_stems[v]]["n_occ"]
        return hdr_occ(v)
    brute_ok, brute_no, words = [], [], []
    for (lab_, kind_, alph, hid), vs in exp_rows.items():
        lab_short = lab_.split(" (")[0]
        if kind_ == "words":
            words.append(f"{lab_short} ({len(vs)})")
            continue
        cand = alph ** hid
        chance = cand / 2 ** 32
        s_ = (f"{lab_short} ({len(vs)} value(s); {hid} hidden of an alphabet of {alph}: {alph}^{hid} = {cand:.2e} "
              f"candidates, ~{chance:.2g} chance matches)")
        (brute_ok if chance <= 2 else brute_no).append(s_)
    hist_counts = [(v, lbs, in_history(v, lbs)) for v, lbs in pend_known.items()]
    not_verbatim = [(v, lbs) for v, lbs, n_ in hist_counts if not n_]
    L[caveat_idx] = (
        "- Caveat (enumeration; round 3, computed per sensitive value): the hash in the redacted form is a 32-bit "
        "prefix, so a value whose hidden characters have few possible values can be recovered by brute force "
        "(expected chance matches = candidates / 2^32), and a value built from words by a word-list search, "
        "whatever its length. Recoverable by brute force: " + ("; ".join(brute_ok) or "none")
        + ". Open to a word-list search: " + (", ".join(words) or "none")
        + ". Not recoverable by brute force: " + ("; ".join(brute_no) or "none")
        + f". Every one of these {len(pend_known)} values is in the history being published -- verbatim ("
        + f"{sum(1 for _, _, n_ in hist_counts if n_)} of them, in blobs, messages or commit headers)"
        + (", or derivable from published material ("
           + ", ".join(f"{'/'.join(lbs).split(' (')[0]}" for v, lbs in not_verbatim)
           + (f": the fingerprint string occurs {fp_verbatim} times, but it is the SHA-256 of the public key "
              "embedded in every gpgsig header" if any("SSH signing-key fingerprint" in lbs for _, lbs in not_verbatim)
              else "") + ")" if not_verbatim else "")
        + " -- so the form protects only this raw, not the release.")

    def pdisp(v):
        return show(pend_known.get(v, ()), v)
    w("## Pre-release check: files not yet in history (round 2)")
    w("")
    w("**Every audit raw must be re-scanned before the release commit.** The history scan above cannot see "
      "files that are not committed yet: the audit's own raws, scripts and README (which the end commit adds), "
      "the concurrent PROPOSAL-m session's pending outputs, and the PI's untracked documents. They are read "
      f"here as plain files -- a snapshot at {pend_stamp}, while other sessions are still writing them -- and "
      f"scanned for (a) every value this run treats as sensitive ({len(pend_known)} values: "
      + ", ".join(f"{k_} {n_}" for k_, n_ in most_common_sorted(collections.Counter(
          (c_[0] if len(c_) == 1 else "/".join(c_)) for c_ in pend_known.values())))
      + "), exact and word-bounded; (b) any NEW value of a RunPod-id / volume-name / container / IPv4 / SSH "
        "fingerprint / SSH public key / session-link shape, any new 4-5 digit number on an ssh/port/alias "
        "line, and (round 4) any email address other than the service address and the commit identities' own -- "
        "a possible third party's personal data, and the only such class this scan has; (c) the "
        f"{len(PRECISE)} precise secret patterns, each triaged on its match's own line (round 4). This part's own "
        "two outputs are excluded (the leak assertion "
        "covers them). A port value is a 5-digit number, so its word-bounded count can include an unrelated "
        "number that happens to be equal. A new 4-5 digit number on an ssh/port/alias line of a pending file stays "
        "untriaged (and redacted) until Code reads it in context; if the same number also occurs in this raw as "
        "an unrelated count, the leak assertion refuses to write until it is triaged -- a safe failure that a "
        "re-run under pre-flip step 1 can meet (round 3 met it: counts on pending lines where 'port' means a code "
        f"port; the code-port rule under (ii) now skips such lines -- this snapshot: "
        f"{CODE_PORT_STATS['pending_lines']} pending line(s), carrying {CODE_PORT_STATS['pending_numbers']} 4-5 "
        "digit number(s)).")
    w("")
    by_grp = collections.defaultdict(list)
    for r_ in pend:
        by_grp[pending_group(r_["file"])].append(r_)
    w("| group | files scanned | files with a sensitive value | files with a new value or an uncleared precise hit |")
    w("|---|---|---|---|")
    for g_ in sorted(by_grp):
        rs = by_grp[g_]
        w(f"| {g_} | {len(rs)} | {sum(1 for r_ in rs if r_['known'])} | "
          f"{sum(1 for r_ in rs if r_['new'] or r_['precise'])} |")
    w("")
    hit_rows = [r_ for r_ in pend if r_["known"] or r_["new"] or r_["precise"]]
    if hit_rows:
        w("| group | file | status | sensitive values (redacted: occurrences) | new values (triage) | precise hits not cleared |")
        w("|---|---|---|---|---|---|")
        for r_ in sorted(hit_rows, key=lambda x: (pending_group(x["file"]), x["file"])):
            w(f"| {pending_group(r_['file']).split(' (')[0]} | `{r_['file']}` | {r_['status']} | "
              + (", ".join(f"`{pdisp(v)}` ({'/'.join(pend_known[v])}): {n_}" for v, n_ in r_["known"].most_common())
                 or "-") + " | "
              + (", ".join(f"{c_} `{show(c_, v, sensitive=t_[2])}` {t_[0]}" for c_, v, t_ in r_["new"]) or "-")
              + " | "
              + (", ".join(f"{n_} `{red(v, sensitive=t_[2]) if len(v) > 4 else 'len' + str(len(v))}` {t_[0]}"
                           for n_, v, t_ in r_["precise"]) or "-") + " |")
        w("")
    def is_author_identity(v):
        return all(lb_ in AUTHOR_IDENTITY_LABELS for lb_ in pend_known.get(v, ()))

    def rule_values(r_):
        return [(v, n_) for v, n_ in r_["known"].items() if not is_author_identity(v)]

    def ident_values(r_):
        return [(v, n_) for v, n_ in r_["known"].items() if is_author_identity(v)]
    audit_rows = [r_ for r_ in pend if pending_group(r_["file"]).startswith("audit")]
    # (A) a redaction-rule value, a new value needing triage or an uncleared precise hit: a blocker as drafted
    audit_hits = [r_ for r_ in audit_rows if rule_values(r_) or r_["new"] or r_["precise"]]
    # (B) only the author's own identity metadata (public in the commit headers): listed, not a blocker
    audit_ident_only = [r_ for r_ in audit_rows if ident_values(r_) and r_ not in audit_hits]
    ident_hdr_occ = {v: hdr_occ(v) for v in pend_known if is_author_identity(v)}
    em_tot = collections.Counter()
    for r_ in audit_rows:
        em_tot.update(r_["emails"])
    w("**Pre-release line, redaction-rule values** (RunPod pod/volume ids, the volume name and its stem, SSH ports, "
      "the SSH signing-key fingerprint, the container hostname, the Claude session link, the pass-phrase-shaped "
      "value; or a new value needing triage -- among them, round 4, an email address other than the service "
      "address and the commit identities' own -- or an uncleared precise hit; email addresses in the audit's "
      f"pending files at this snapshot: the service address {em_tot['service address']}, a commit identity's "
      f"{em_tot['commit identity']}, other {em_tot['other']}): "
      + (f"NOT CLEAN -- {len(audit_hits)} audit file(s) that the end commit would add carry one: "
         + "; ".join(f"`{r_['file']}` ("
                     + ", ".join([f"`{pdisp(v)}` x{n_}" for v, n_ in rule_values(r_)]
                                 + [f"new {c_} `{show(c_, v, sensitive=t_[2])}`" for c_, v, t_ in r_["new"]]
                                 + [f"precise {n_}" for n_, _, _ in r_["precise"]]) + ")" for r_ in audit_hits)
         + ". Each is its owning item's to fix before the end commit (this part edits only its own files); "
           "re-run this script after the fixes." if audit_hits else
         "CLEAN for the audit's own pending files at this snapshot. Its coverage of third-party personal data is "
         "the email-address class only (round 4): a third party's name, postal address or phone number is not "
         "scanned for.")
      + " Files of the other groups matter only if they are committed before the flip; the history re-run at "
        "the release commit (pre-flip step 1) covers whatever is.")
    w("")
    w("**Pre-release line, the commit identities' own metadata** (the identity emails -- the author's and the "
      "Claude Cowork tool identity's -- and the laptop hostname, all public in the commit headers of the history "
      "being published: "
      + ", ".join(f"`{pdisp(e_)}` ({'/'.join(pend_known[e_])}) in {k_} author/committer/tagger header line(s)"
                  for e_, k_ in sorted(ident_hdr_occ.items(), key=lambda kv: (-kv[1], vkey(kv[0]))))
      + "): "
      + (f"{len(audit_ident_only)} audit file(s) carry only such a value: "
         + "; ".join(f"`{r_['file']}` (" + ", ".join(f"`{pdisp(v)}` x{n_}" for v, n_ in ident_values(r_)) + ")"
                     for r_ in audit_ident_only)
         + ". Listed for consistency with this raw's own redaction policy, which redacts them; the routing's "
           "redaction rule covers third-party personal data, not the commit identities' own public header "
           "metadata, so this is not a routing violation and, as drafted, not a blocker (the PI's call). A "
           "third party's email address would count under the line above (round 4), not here."
         if audit_ident_only else
         "no audit file carries only such a value at this snapshot.")
      + (f" Audit files with both kinds count under the first line ({sum(1 for r_ in audit_hits if ident_values(r_))})."
         if any(ident_values(r_) for r_ in audit_hits) else ""))
    w("")

    w("## Summary lines")
    w("")
    w(f"- (i): STOP pending the PI's resolution (literal :77); the block's primary scanners (gitleaks, trufflehog) NOT run "
      f"(installable, not installed: no install without the PI's word; pre-flip step 4); fallback {len(grep_lines)} hit lines (token {alt_lines['token']}, sk- {alt_lines['sk-[A-Za-z0-9]']}, "
      f"secret {alt_lines['secret']}, rp_ {alt_lines['rp_[A-Za-z0-9]']}, password {alt_lines['password']}, "
      f"api_key {alt_lines['api[_-]?key']}, BEGIN {alt_lines['BEGIN (RSA|OPENSSH)']}, AKIA {alt_lines['AKIA[0-9A-Z]{16}']}); "
      f"precise scan ({len(PRECISE)} patterns) {sum(len(t) for t in precise.values())} distinct values in "
      f"blobs/messages, {sum(len(t) for t in hdr['precise'].values())} in headers, {bp_n} in binary string "
      f"content; in-context high-entropy {len(he)} distinct; context-free high-entropy {len(cf)} distinct in "
      f"blobs/messages, {len(hdr['cf'])} in headers, {len(binc['cf'])} in binary content; "
      f"TRUE-SECRET-CANDIDATE {len(true_candidates)}; UNTRIAGED {len(untriaged_precise)}.")
    w(f"- (ii): RunPod pod ids {len(ids['runpod_pod_id (context: pod)'])}, network volume ids "
      f"{len(ids['runpod_volume_id (context: volume)'])}, network volume names "
      f"{sum(1 for e in ids[VOLNAME_CLASS].values() if e['triage'][0] == 'IDENTIFIER')}, SSH ports "
      f"{sum(1 for e in ids['ssh_port (number in an ssh/port/alias line)'].values() if e['triage'][0] == 'IDENTIFIER')}, "
      f"container hostnames {len(ids['container_hostname (12 hex after host:/root@)'])}, Claude session links "
      f"{len(ids['claude_session_or_artifact_link'])}, IP addresses identifying a machine "
      f"{sum(1 for v in real_ips if ip_class(v) != 'loopback (127/8)')}; in blob/message content SSH key names / "
      f"fingerprints / public keys {len(ids['ssh_key_name (id_*)'])} / {len(ids['ssh_fingerprint'])} / "
      f"{len(ids['ssh_public_key'])}; in commit headers {len(sig_groups)} SSH signing public key(s) "
      f"({', '.join(red(k[4]) for k in sig_groups if k[4]) or '-'}) in {len(hdr['sigs'])} gpgsig headers "
      f"(PUBLIC-KEY, not a credential); "
      f"the author's laptop hostname in {laptop_commits} commits' author/committer emails (metadata); tagger "
      f"identities {len(hdr['taggers'])}; local temp paths {len(ids['local_temp_path ((/private)/tmp, (/private)/var/folders)'])} "
      f"distinct, ~/.claude/projects paths {len(ids['claude_projects_path (~/.claude/projects/...)'])} distinct; "
      f"/Users/ in {len(users_at_head)} HEAD files, /workspace/ in {len(workspace_at_head)}. A list, no pass "
      f"condition; none is a credential.")
    w(f"- (v): {'PASS' if max_blob <= 100 * MB else 'STOP'}; largest blob {max_blob:,} bytes; files at HEAD over 50 MB {n50}, over 50 MiB {n50i}, over 100 MB {n100}.")
    w(f"- (iv)-mechanical: jlens-qwen36 paths ever tracked {len(jlens_hist)}; jlens files byte-identical to a "
      f"reachable blob {len(jl['matches'])} ({len(jm_empty)} empty, {len(jm_nonempty)} lab data files, "
      f"{len(jm_code)} outside data/); clone-index non-empty blobs reachable in lab history "
      f"{len(jidx.get('nonempty_reachable_in_lab', [])) if jidx.get('present') else 'not read'} of "
      f"{jidx.get('nonempty_entries', '-')}; npz without an explicit line {len(no_line)}; weight-shaped paths "
      f"{len(weights)}; residual-space float vectors in tracked JSON {len(fa)} array(s) in "
      f"{len({x['blob'] for x in fa})} blob(s) ({', '.join('`' + p_ + '`' for p_ in sorted({p_ for x in fa for p_ in x['paths']}))}).")
    w(f"- Pre-release (files not yet in history, snapshot): {len(pend)} files scanned; audit files carrying a "
      f"redaction-rule value or an untriaged value {len(audit_hits)}"
      + (" (" + ", ".join(f"`{r_['file']}`" for r_ in audit_hits) + ")" if audit_hits else "")
      + f"; audit files carrying only the commit identities' own metadata (public in the commit headers; listed, "
        f"not a blocker as drafted) {len(audit_ident_only)}"
      + (" (" + ", ".join(f"`{r_['file']}`" for r_ in audit_ident_only) + ")" if audit_ident_only else "")
      + "; the end commit waits on a clean re-run (pre-flip step 1).")
    w("")
    values_check(w, locals())
    md = "\n".join(L) + "\n"

    # ------------------------------------------------------------ json
    def ser(tab, cls=None):
        out = []
        for v, e in tab.items():
            tri = e.get("triage", ("", "", True))
            vis = v if (v in SAFE_VERBATIM or (tri[0] == "PUBLIC" and not tri[2])) else show(cls, v, sensitive=tri[2])
            out.append({"value": vis, "triage": list(tri[:2]),
                        "n_occ": e["n_occ"], "n_occ_head": e["n_occ_head"], "n_sources": len(e["sources"]),
                        "n_messages": e["messages"], "head_paths": sorted(e["head_paths"]),
                        "first": e["first"], "extra": e.get("extra")})
        return out

    J = {
        "item": "N12-history", "block": BLOCK, "block_sha256": block_sha_wt, "stamp": stamp,
        "head": head, "script": script_path, "script_sha256": script_sha, "interpreter": sys.executable,
        "python": sys.version.split()[0], "refs": refs, "refs_moved_during_run": refs_moved,
        "ancestor_of_origin_main": ancestry,
        "counts": {"commits": len(m["commits"]), "trees": m["n_trees"], "blobs": len(m["blobs"]), **stats},
        "redaction_form": "first4...[len N]#sha256[:8]; ssh_port class: lenN:sha256[:8]",
        "fallback": {"command": "git log -p --all | /usr/bin/grep -nEi '" + FALLBACK_PATTERN + "'",
                     "grep_returncode": g.returncode, "hit_lines": len(grep_lines),
                     "python_crosscheck_lines": len(py_lines), "multi_alt_lines": multi_alt_lines,
                     "per_alternative": {n: {"lines": alt_lines[n], "occurrences": alt_occ[n]} for n, _ in FALLBACK_ALTS},
                     "bulk_rules": [{"alternative": n, "rule": r, "occurrences": c, "reason": bulk_reason[(n, r)],
                                     "first": bulk_first[(n, r)],
                                     "words": bulk_words[(n, r)].most_common(200)} for (n, r), c in bulk.items()],
                     "credential_shaped": compact_shape(shape_rows)},
        "precise": {n: ser(precise[n]) for n, _, _ in PRECISE},
        "precise_patterns": {n: rx.pattern for n, rx, _ in PRECISE},
        "high_entropy": {"stats": dict(he_stats), "values": ser(he)},
        "credential_file_paths": cred_files,
        "identities": {"authors": [{"name": n, "email_redacted": e if e in service else red(e), "commits": c}
                                   for (n, e), c in authors.most_common()],
                       "committers": [{"name": n, "email_redacted": e if e in service else red(e), "commits": c}
                                      for (n, e), c in committers.most_common()]},
        "identifiers": {cls: ser(tab, cls) for cls, tab in ids.items()},
        "identifier_class_sources": {cls: {"union": u_, "summed_over_values": s_}
                                     for cls, (u_, s_) in id_class_src.items()},
        "identifier_patterns": ID_PATTERNS,
        "identifiers_exact_recount": {show(e["classes"], v, sensitive=(manual(v) or ("", "", True))[2]): {
            "classes": e["classes"], "n_occ": e["n_occ"], "n_occ_head": e["n_occ_head"],
            "n_occ_new_since_base": e["n_occ_new"], "n_occ_at_base": e["n_occ"] - e["n_occ_new"],
            "n_sources": len(e["sources"]), "first": e["first"], "head_paths": sorted(e["head_paths"]),
            "head_locators": e["head_locators"], "n_occ_base_head": e["n_occ_base_head"],
            "base_head_locators": e["base_head_locators"]} for v, e in exact.items()},
        "pin": {"pinned": bool(a.pin), "notes": pin_notes, "live_head": head_live},
        "since": {"base": since, "new_commits": new_commits, "n_new_blobs": len(new_blobs)},
        "context_free_high_entropy": {"description": CF_DESC, "values": ser(cf)},
        "headers": {"n_commit_headers": hdr["n_commit_headers"], "n_tag_headers": hdr["n_tag_headers"],
                    "keys": dict(hdr["keys"]),
                    "signatures": [{"commits": shas_, "armor": k[0], "key_type": k[1], "namespace": k[2],
                                    "hash": k[3], "fingerprint_redacted": red(k[4]) if k[4] else None,
                                    "verdict": "PUBLIC-KEY"} for k, shas_ in sig_groups.items()],
                    "identity_email_occurrences": {(e_ if e_ in service else red(e_)): k
                                                   for e_, k in hdr["identity_occ"].items()},
                    "taggers": [{"name": n_, "email_redacted": (e_ if e_ in service else red(e_)), "tags": hdr["tagger_tags"][(n_, e_)]}
                                for (n_, e_), _ in hdr["taggers"].items()],
                    "precise": {n: ser(t) for n, t in hdr["precise"].items() if t},
                    "identifiers": {c: ser(t, c) for c, t in hdr["ids"].items() if t},
                    "context_free_high_entropy": ser(hdr["cf"]),
                    "armor_lines": [{"length": v[0], "entropy": v[1], "upper_lower_digit": v[2]}
                                    for v in hdr["armor_lines"].values()],
                    "armor_lines_at_or_below_4.3": sum(1 for v in hdr["armor_lines"].values() if v[1] <= 4.3)},
        "structured_base64": {"strict_base64_runs_64plus_blobs_messages": len(hdr["b64stats"]["runs64"]),
                              "at_or_below_4.3": [{"value": red(x["value"]), "entropy": x["entropy"],
                                                   "first": x["first"]}
                                                  for x in hdr["b64stats"]["runs64_below"].values()],
                              "key_material_patterns": {n_: {"blobs_messages": len(precise[n_]),
                                                             "headers": len(hdr["precise"][n_]),
                                                             "binary_content": len(binc["precise"][n_])}
                                                        for n_ in sorted(KEY_MATERIAL_PATTERNS)}},
        "scanner_availability": scan_av,
        "fallback_logp": {"bytes": len(logp), "lines_newline_count": logp_nl, "ends_with_newline": logp_ends_nl},
        "reflogs": reflogs,
        "json_numeric_vectors": {"blobs": jv["blobs"], "parsed": jv["parsed"], "unparsed": jv["unparsed"],
                                 "float_arrays": jv["float_arrays"], "int_arrays": jv["int_arrays"],
                                 "int_array_groups": [{"paths": p_, "pointer": q_, "n": n_}
                                                      for (p_, q_), n_ in jv["int_array_groups"].most_common()]},
        "home_paths_outside_repo": {"kinds": dict(hp_out["kinds"]),
                                    "kind_files": {k_: sorted(s_) for k_, s_ in hp_out["kind_files"].items()},
                                    "env_names_redacted": {red(nm): hp_out["env_files"].get(nm, {})
                                                           for nm in hp_out["env_names"]},
                                    "notebook_display_name_is_env": hp_out["notebook_display_name"] in hp_out["env_names"]},
        "prerelease_pending_files": {
            "stamp": pend_stamp, "excluded": sorted(excl),
            "known_values": {show(c_, v): c_ for v, c_ in pend_known.items()},
            "enumeration_exposure": [{"label": k_[0], "kind": k_[1], "alphabet": k_[2], "hidden": k_[3],
                                      "values": [show(pend_known[v], v) for v in vs]}
                                     for k_, vs in exp_rows.items()],
            "files": [{"file": r_["file"], "status": r_["status"], "group": pending_group(r_["file"]),
                       "bytes": r_["bytes"],
                       "known": {show(pend_known.get(v, ()), v): n_ for v, n_ in r_["known"].items()},
                       "new": [{"class": c_, "value": show(c_, v, sensitive=t_[2]), "triage": list(t_[:2])}
                               for c_, v, t_ in r_["new"]],
                       "precise_not_cleared": [{"pattern": n_, "value": (red(v, sensitive=t_[2]) if len(v) > 4
                                                                          else f"len{len(v)}"),
                                                "triage": list(t_[:2])} for n_, v, t_ in r_["precise"]],
                       "email_addresses": dict(r_["emails"]),
                       "hex_only_quoted_values_by_verdict": dict(r_["hex_quoted"])}
                      for r_ in pend],
            "audit_files_not_clean": [r_["file"] for r_ in audit_hits],
            "audit_files_not_clean_rule": ("a redaction-rule value (any sensitive label except "
                                           + " / ".join(AUTHOR_IDENTITY_LABELS) + "), a new value needing triage, "
                                           "or an uncleared precise hit"),
            "audit_files_author_identity_only": [r_["file"] for r_ in audit_ident_only],
            "author_identity_header_occurrences": {pdisp(v): n_ for v, n_ in ident_hdr_occ.items()}},
        "ckpt_minus_diff_evidence": ckpt_ev,
        "values_shown_in_full_short": [red(s_, sensitive=False) for s_ in sorted(SHORT_SHOWN)],
        "binary_content": {"members": binc["members"], "dtypes": dict(binc["dtypes"]),
                           "unicode_members": binc["unicode_members"], "ascii_runs": binc["ascii_runs"],
                           "png_chunks": dict(binc["png_chunks"]), "png_text_keys": binc["png_text_keys"],
                           "other_binary": binc["other_binary"], "chars_scanned": binc["chars_scanned"],
                           "precise": {n: ser(t) for n, t in binc["precise"].items() if t},
                           "identifiers": {c: ser(t, c) for c, t in binc["ids"].items() if t},
                           "context_free_high_entropy": ser(binc["cf"])},
        "fallback_bulk_locators_T2": {f"{n}|{r}": locs for (n, r), locs in bulk_locs.items() if r.startswith("T2")},
        "gitattributes_nodiff_lines": nodiff_lines, "ckpt_paths_ever_tracked": ckpt_paths,
        "unreachable_objects": {"store_objects": n_store, "by_type": dict(unreach), "bytes": unreach_bytes,
                                "against": "live refs at the run"},
        "commits_after_base_live": live_new_commits,
        "continuity": {"occ": cont["occ"], "occ_word_bounded": cont["occ_word"], "occ_discontinuity": cont["occ_dis"],
                       "occ_new_since_base": cont["occ_new"], "sources": cont["sources"],
                       "n_paths": len(cont["paths"]), "n_paths_base": len(cont["paths_base"]),
                       "head_occ": cont["head_occ"], "phrases": cont["phrases"]},
        "users_paths_at_head": users_at_head, "workspace_paths_at_head": workspace_at_head,
        "count_objects": count_objects.stdout.decode(), "count_objects_stderr_lines": len(garb),
        "head_files_over_40MB": head_big, "largest_blobs": largest, "max_blob_bytes": max_blob,
        "binary_blobs": binary,
        "jlens": {"head": jlens_head, "history": jlens_hist, "gitlinks_head": gitlinks,
                  "files_read": jl["files"], "files_hashed": jl["hashed"], "content_copies": jl["matches"],
                  "clone_index": jidx},
        "gitignore_worktree_equals_head": gi_wt_ok, "npz": npz_rows, "weight_shaped_paths": weights,
        "true_secret_candidates": len(true_candidates), "untriaged": len(untriaged_precise),
    }
    js = json.dumps(J, indent=1, default=lambda o: sorted(o) if isinstance(o, set) else str(o))

    if a.dump_untriaged:
        def dump(label, tab):
            for v, e in tab.items():
                tri = e.get("triage", ("?", "?", True))
                if not a.dump_all and (tri[0] in ("PUBLIC",) or
                                       (tri[0] == "FALSE-POSITIVE" and not tri[2] and vkey(v) not in MANUAL_TRIAGE)):
                    continue
                print(f"{label}\t{vkey(v)}\t{tri[0]}\t{e['n_occ']}\t{e['first']}\t{v!r}\t{e.get('_ctx', '')[:300]!r}")
        for n, _, _ in PRECISE:
            dump("precise:" + n, precise[n])
        dump("high_entropy", he)
        dump("context_free", cf)
        dump("header_context_free", hdr["cf"])
        dump("binary_context_free", binc["cf"])
        for n, _, _ in PRECISE:
            dump("header_precise:" + n, hdr["precise"][n])
            dump("binary_precise:" + n, binc["precise"][n])
        for cls, tab in ids.items():
            dump("id:" + cls, tab)
        for r in shape_rows:
            if r["verdict"] == "UNTRIAGED":
                print("shape", r)
        print("DUMP ONLY: no file written")
        return

    # ---- round 5: the verdict-based leak guard (guard_decide), its positive controls, and the round-5 section
    R = collections.defaultdict(list)

    def rec(v, src, cls, verdict, explicit=None, extra=None):
        if not v:
            return
        if explicit is None:
            mt_ = manual(v)
            explicit = bool(mt_ and mt_[0] == verdict)
        R[v].append((src, cls, verdict, explicit, extra))
    for n_, t_ in precise.items():
        for v, e in t_.items():
            rec(v, "blob/message", "precise:" + n_, e["triage"][0])
    for v, e in he.items():
        rec(v, "blob/message", "high_entropy", e["triage"][0])
    for v, e in cf.items():
        rec(v, "blob/message", "context_free", e["triage"][0])
    for lab_, src_ in (("header", hdr), ("binary", binc)):
        for n_, t_ in src_["precise"].items():
            for v, e in t_.items():
                rec(v, lab_, "precise:" + n_, e["triage"][0])
        for v, e in src_["cf"].items():
            rec(v, lab_, "context_free", e["triage"][0])
        for c_, t_ in src_["ids"].items():
            for v, e in t_.items():
                rec(v, lab_, c_, e["triage"][0])
    for c_, t_ in ids.items():
        for v, e in t_.items():
            rec(v, "blob/message", c_, e["triage"][0])
    for v, e in sw_other:
        rec(v, "blob/message", SWEEP_CLASS, (manual(v) or ("UNTRIAGED",))[0])
    for (v, srcl), r_ in zip(shape_raw, shape_rows):
        rec(v, srcl, SHAPE_CLASS, r_["verdict"], explicit=srcl in ("shape16", "shape-manual"),
            extra=(r_["locator"].split(" ", 1)[1].rsplit(":", 1)[0], r_["key"].lower(), sha256_hex(v.encode())[:16])
            if srcl == "shape16" else None)
    for r_ in pend:
        for c_, v, t_ in r_["new"]:
            rec(v, "pending file", c_, t_[0])
        for n_, v, t_ in r_["precise"]:
            rec(v, "pending file", "precise:" + n_, t_[0])
    # shape16 rows: the key the row matched (path, key, value prefix), for the round-5 table
    R = {v: [(x[0], x[1], x[2], x[3], x[4]) for x in recs] for v, recs in R.items()}
    known = guard_known(pend_known)   # second check (finding 5): plus the session link's bare id
    untri_counts = {
        "script": len(untriaged_precise),
        "ids": sum(1 for _, _, e in id_rows if e["triage"][0] == "UNTRIAGED"),
        "sweep": sum(1 for v, _ in sw_other if (manual(v) or ("UNTRIAGED",))[0] == "UNTRIAGED"),
        "shape": sum(1 for r_ in shape_rows if r_["verdict"] == "UNTRIAGED"),
        "true": len(true_candidates),
        "pending": sum(1 for r_ in pend for _, _, t_ in list(r_["new"]) + list(r_["precise"]) if t_[0] == "UNTRIAGED"),
        "fallback": len(grep_lines)}
    C5 = {"head": head, "untriaged": untri_counts, "code_users_kinds": dict(code_kinds),
          "code_users_files": len(code_users)}
    md_base = md
    G = None
    for it_ in range(8):
        L5 = []
        values_check_r5(L5.append, C5, G)
        md = md_base + "\n".join(L5) + "\n"
        J["guard"] = G
        J["untriaged_all_tables"] = untri_counts
        js = json.dumps(J, indent=1, default=lambda o: sorted(o) if isinstance(o, set) else str(o))
        res5, aux5 = guard_controls(R, known, set(REDACTED_SENSITIVE), {"md": md, "json": js + "\n"}, pend_known)
        Gn = guard_summary(R, res5, aux5, {"md": md, "json": js + "\n"}, known)
        if G is not None and json.dumps(Gn, sort_keys=True) == json.dumps(G, sort_keys=True):
            break
        G = Gn
    else:
        raise SystemExit("REFUSING TO WRITE: the round-5 guard summary did not reach a fixed point")
    cands5, ref5, why5, ex5, leaks = aux5
    if a.selftest:
        print(json.dumps({"selftest": "round-5 leak guard", "head": head, "controls": G["controls"],
                          "counts": G["counts"], "untriaged_all_tables": untri_counts}, indent=1, sort_keys=True))
        print("SELFTEST " + ("PASS" if G["controls"]["all_pass"] and not leaks else "FAIL") + ": no file written")
        raise SystemExit(0 if G["controls"]["all_pass"] and not leaks else 1)
    if leaks:
        raise SystemExit(f"REFUSING TO WRITE: {len(leaks)} guarded value(s) appear verbatim: "
                         + "; ".join(f"{lab_} `{guard_form(v)}` ({why5.get(v)})" for lab_, v in leaks))
    if not G["controls"]["all_pass"]:
        raise SystemExit("REFUSING TO WRITE: a round-5 positive control failed: "
                         + json.dumps(G["controls"], sort_keys=True))
    with open(os.path.join(ROOT, a.out), "w") as f:
        f.write(md)
    with open(os.path.join(ROOT, a.json_out), "w") as f:
        f.write(js + "\n")
    print(f"wrote {a.out} ({len(md):,} chars) and {a.json_out} ({len(js):,} chars); "
          f"fallback hit lines {len(grep_lines)}; true-secret candidates {len(true_candidates)}; "
          f"untriaged {len(untriaged_precise)} (all tables: ids {untri_counts['ids']}, sweep {untri_counts['sweep']}, "
          f"shape rows {untri_counts['shape']}; pending files {untri_counts['pending']}); round-5 guard: candidates "
          f"{len(cands5)}, refused set {len(ref5)}, exempt {len(ex5)}, found verbatim 0; controls "
          f"{'ALL PASS' if G['controls']['all_pass'] else 'FAIL'}; fixed point after {it_ + 1} rendering(s)")


if __name__ == "__main__":
    main()
