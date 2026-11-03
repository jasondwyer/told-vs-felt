#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12 pre-flip reads (the scrub index's pre-flip checklist, section 10).

Release v2 (2026-11-03): run without --v1, this script makes release v2's pre-flip read (main_v2, below): the
release block's item 6 (`git ls-remote origin` = `main` + the four tags; the GitHub-side surfaces; a STOP on any
`wip/*`, `main-*` or `claude/*` head), the release route's check that the commits no local ref reaches are not served
by the new repository, and the history script run again with its outputs outside the repository (the interim scan).
It writes results/raw/<run date>_note-N12-preflip.md and .json. With --v1 it makes release v1's read, described
below, unchanged; its comparisons are with the 2026-10-08 history raw and v1's baselines, which do not hold at v2.

Read-only. Three reads, then pass/flag lines and the list of what remains for the PI:

  (1) `git ls-remote --symref origin`: every server-side ref, compared with the local refs and with
      the refs table of the history raw (results/raw/2026-10-08_note-N12-history.md at --rec); for
      each server ref, whether its object is local (`git cat-file -e`) and, only if it is, whether it
      is an ancestor of origin/main (`git merge-base --is-ancestor`). Nothing is fetched.
  (2) GitHub-side surfaces, read-only through the authenticated `gh` CLI: repository visibility and
      publication settings, pull requests, issues, issue/review/commit comments, releases, Actions
      (runs, workflows, artifacts: counts and names; nothing downloaded), the wiki (setting, and
      `git ls-remote` of the wiki repository), Pages, deploy keys and webhooks (counts only),
      milestones, GraphQL counts, and (Code's addition) the repository activity record (pushes,
      force pushes, branch creations and deletions) checked against the local objects and the
      remote-tracking reflogs (read as plain files; their name/email fields are never read out).
      Every text field read is screened for the routing's redaction classes; logins other than the
      repository owner's are reported as counts and redacted forms only.
  (3) An interim history scan: scripts/audit_note_N12_history.py is run unchanged, as routed, with
      --out/--json-out OUTSIDE the repository (--history-dir), under PYTHONHASHSEED=0 so that the sample
      its refusal message prints (the first 10 entries, in a set's iteration order) is reproducible.
      Because that message prints only a sample, the same unchanged script is then run a second time
      in-process with the same arguments, its SystemExit caught and its own `leaks` list read from its
      frame: the full list, sorted (values never printed; forms only). Because a run may refuse to
      write, it is also run in its own documented --dump-untriaged --dump-all mode (it writes no file;
      its stdout is held in memory here and never written). The dumped value sets are diffed, per
      table, against the committed history JSON (`git show <rec>:results/raw/2026-10-08_note-N12-history.json`).
      The script's UNTRIAGED rows are triaged here by Code (CODE_TRIAGE / SHAPE rules below), each
      keyed by the value's sha256 prefix and its first locator; anything else stays UNTRIAGED here.
      Computed directly: the block's fallback grep at HEAD (the same command the history script
      runs) with per-commit attribution; the blobs new since --base with their sizes; occurrences
      of the history raw's known sensitive values in what each commit after --base added; the
      commit identities of those commits.

Writes only --out and --json-out (results/raw/ by default); the history script writes only under
--history-dir, which must lie outside the repository. No git command that writes (no add, commit,
push, tag, config, fetch); no git command inside jlens-qwen36/; nothing installed or downloaded.

REDACTION: the outputs are committed to a repository about to be public. The history raw's known
sensitive values are resolved in memory (as the scrub index does) and never printed; so are the
dumped values. Values are shown only as redacted forms in the history raw's notation
`xxxx...[len N]#hhhhhhhh` (first 4 characters, length, first 8 hex of sha256; the routing's
first-4 + length + sha8) or `lenN:hhhhhhhh` for the SSH-port class. Class names are printed by
their short label, because several long labels contain the very strings the history scan reports
as values. Before writing, the script refuses if any resolved or dumped non-public value, an IPv4
literal, a claude.ai session/artifact path, an SSH fingerprint shape, a local temp or
transcript-store path, or a 4-5 digit number on an ssh/port line occurs in an output, or if a
redacted form it prints belongs to a class the history raw lists as recoverable by brute force.
It also runs the history script's own rules -- precise patterns, identifier classes, SSH-port lines,
fallback bulk rules, credential shapes, and the in-context and context-free high-entropy rules --
over its final outputs and its own source (what the release re-run would see) and refuses if they
would add an UNTRIAGED row or any high-entropy verdict other than FALSE-POSITIVE / PUBLIC.

    jlens-qwen36/.venv/bin/python scripts/audit_note_N12_preflip.py --history-dir <dir outside the repo>
"""
import argparse
import ast
import collections
import datetime
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
OWNER, NAME = "jasondwyer", "told-vs-felt"   # release v2: the block, item 1.2
SLUG = f"{OWNER}/{NAME}"
HIST_SCRIPT = "scripts/audit_note_N12_history.py"
HIST_SCRIPT_SHA = "918dae5a735240c379e679c61f20816775c10918736715f6e1ec0c6ae3cabaa8"   # the history script at bec62e3
SCRUB_SCRIPT = "scripts/audit_note_N12_scrub.py"
HIST_MD = "results/raw/2026-10-08_note-N12-history.md"
HIST_JSON = "results/raw/2026-10-08_note-N12-history.json"
SCRUB_MD = "results/raw/2026-10-08_note-N12-scrub.md"
DEFAULT_MD = "results/raw/2026-10-08_note-N12-preflip.md"
DEFAULT_JSON = "results/raw/2026-10-08_note-N12-preflip.json"
WORLD_PREFIXES = ("refs/heads/", "refs/tags/", "refs/pull/")

# Code's individual triage of the history script's UNTRIAGED identifier / context-free rows, read in
# context at this run (each value by the sha256 prefix of its redacted form; never the value).
# (table, sha8) -> (verdict, reason, expected first-locator path)
CODE_TRIAGE = {
    ("context_free", "77f5bcb1"): (
        "LOCAL-PATH", "a path under the author's home directory (a local Python library directory) in N11's "
        "printed sys.path of the regression-suite run; the author is named in the repository; not a credential",
        "results/raw/2026-10-08_note-N11-smoke.txt"),
    ("runpod_hostname", "e0b5f502"): (
        "PUBLIC", "the RunPod proxy service's domain, named in the content review's flag text about the ssh "
        "alias; it names the service, not a pod or an account", "results/raw/2026-10-08_note-N12-content.md"),
    ("runpod_hostname", "f8ec340d"): (
        "PUBLIC", "RunPod's public SSH gateway host, named in the same flag text; it names no pod or account",
        "results/raw/2026-10-08_note-N12-content.md"),
    ("runpod_hostname", "3124edae"): (
        "PUBLIC", "RunPod's public site domain (on the history script's own public-host list), here inside "
        "class labels and flag text", "results/raw/2026-10-08_note-N12-content.md"),
    ("runpod_hostname", "421bbde9"): (
        "FALSE-POSITIVE", "the RunPod service domain as written in this class's own label, printed by the "
        "history JSON's tables", "results/raw/2026-10-08_note-N12-history.json"),
    ("runpod_hostname", "80e1d10e"): (
        "FALSE-POSITIVE", "a synthetic fixture in the content script's self-test (a placeholder number and the "
        "proxy suffix; its pod-id part is assembled from string pieces at run time); names no real host",
        "scripts/audit_note_N12_content.py"),
    ("proxy_hostname", "80e1d10e"): (
        "FALSE-POSITIVE", "the synthetic self-test fixture also listed under runpod_hostname",
        "scripts/audit_note_N12_content.py"),
    ("runpod_hostname", "f4b8c41f"): (
        "PUBLIC", "an entry of the history script's own public-host list (RunPod's documentation site)",
        "scripts/audit_note_N12_history.py"),
    ("runpod_hostname", "f53cd0c4"): (
        "PUBLIC", "an entry of the history script's own public-host list (RunPod's www site)",
        "scripts/audit_note_N12_history.py"),
    ("ssh_key_path", "41c256ae"): (
        "FALSE-POSITIVE", "the prefix of a timestamped backup name of the standard ssh client config, quoted in "
        "the content review's flag text, which says it is not a key name; no key file",
        "results/raw/2026-10-08_note-N12-content.md"),
    ("ssh_key_name", "f40883a1"): (
        "FALSE-POSITIVE", "a generic default key-file name inside the history raw's description of its "
        "credential-file path pattern; no key file is named or tracked", "results/raw/2026-10-08_note-N12-history.md"),
    ("ssh_key_name", "8e5d92fd"): (
        "FALSE-POSITIVE", "the other generic default key-file name in the same description",
        "results/raw/2026-10-08_note-N12-history.md"),
    ("ssh_identity_flag", "a36807c9"): (
        "FALSE-POSITIVE", "the word after the ssh identity flag in the content screen's category description; "
        "not a file", "results/raw/2026-10-08_note-N12-content-screen.json"),
    ("ssh_identity_flag", "13dfbe0e"): (
        "FALSE-POSITIVE", "the placeholder '<file>' with trailing punctuation, from this class's own label as the "
        "history JSON prints it", "results/raw/2026-10-08_note-N12-history.json"),
    ("ssh_identity_flag", "1aedc48e"): (
        "FALSE-POSITIVE", "the same placeholder, from this class's label in the history raw's table",
        "results/raw/2026-10-08_note-N12-history.md"),
    ("ssh_identity_flag", "c17d7b45"): (
        "FALSE-POSITIVE", "the same placeholder, from this class's label in the history raw's pattern list",
        "results/raw/2026-10-08_note-N12-history.md"),
    ("ssh_identity_flag", "a2b73321"): (
        "FALSE-POSITIVE", "the same placeholder, from this class's label in the history script's source",
        "scripts/audit_note_N12_history.py"),
    ("passphrase_shaped", "fab79a8e"): (
        "FALSE-POSITIVE", "a fragment of this class's own regular expression, as the history JSON's pattern "
        "table stores it; not a phrase", "results/raw/2026-10-08_note-N12-history.json"),
    ("url_host", "01ac74e6"): (
        "PUBLIC", "a public website host (the Creative Commons site), in the licenses raw's licence links",
        "results/raw/2026-10-08_note-N12-licenses.json"),
    ("url_host", "5b3097c5"): (
        "PUBLIC", "a public website host (GitHub's REST service host), in the licenses raw's source URLs",
        "results/raw/2026-10-08_note-N12-licenses.json"),
    ("url_host", "26ca8550"): (
        "PUBLIC", "a public website host (GitHub's documentation host), in the licenses raw's source URLs",
        "results/raw/2026-10-08_note-N12-licenses.json"),
}

# Code's triage of the history script's UNTRIAGED credential-shaped fallback rows (the block's
# `key = value` / `key: value` shapes) that the N13 hash rule below does not cover.
# (path, line) -> (sha8 of the row's redacted value, reason)
SHAPE_TRIAGE = {
    ("results/raw/2026-10-08_note-N3-echo-robustness.md", 438): (
        "5141d821", "LLM-token sense: a label's token, then its probe-AUC range"),
    ("results/raw/2026-10-08_note-N3-echo-robustness.md", 439): (
        "b4a03256", "LLM-token sense: the second label's token, then its probe-AUC range"),
    ("results/raw/2026-10-08_note-N3-echo-robustness.json", 9951): (
        "5141d821", "the same sentence as the md's line, in the JSON"),
    ("results/raw/2026-10-08_note-N3-echo-robustness.json", 9956): (
        "b4a03256", "the same sentence as the md's line, in the JSON"),
    ("results/raw/2026-10-08_note-N12-history.md", 1030): (
        "8d33f520", "prose quoting a key spelled with a trailing colon; the captured value is the closing backtick"),
    ("scripts/audit_note_N12_history.py", 2304): (
        "8d33f520", "the same prose, in the script that writes it"),
    ("results/raw/2026-10-08_note-tier1_valuescheck.md", 390): (
        "46dc943e", "prose ('Informational, not a secret' followed by a path prefix); no value"),
    ("results/raw/2026-10-08_note-N16-decoding.json", 2106): (
        "a683c5c5", "a decoding parameter (maximum new tokens) recorded as 'n/a'"),
    ("results/raw/2026-10-08_note-N16-decoding.md", 81): (
        "d918ff43", "LLM-token sense: the model's end-of-sequence token string"),
    ("scripts/audit_note_N16.py", 1637): (
        "416759ca", "a decoding-parameters table entry whose value starts with a run label (B2-r)"),
    ("scripts/audit_note_N2.py", 402): (
        "ce7f5d9d", "source code (a keyword argument) inside a regular expression of a referent check"),
    ("scripts/audit_note_N13.py", 566): (
        "97ba63eb", "a document:line citation label in N13's trigger table"),
    ("scripts/audit_note_N13.py", 599): (
        "14fa6371", "a document:line citation label in N13's trigger table"),
}
N13_JSON = "results/raw/2026-10-08_note-N13-provenance.json"
N13_KEY = "token"
# the history script's bulk rules that it lists for inspection rather than clearing (its md, every locator)
INSPECT_RULES = ("T2", "T3", "P3", "K2", "X")
# sha256 of the sorted (commit, path, side, line, alternative, rule, word) rows of those rules among the fallback's
# hits in the commits after the committed scan, as Code read them (every distinct line) at this run's HEAD
INSPECTED_SHA = "1f23b34136ba3317a1321a74ba7c4fc2fd14679a4b0c4089b02c905d792b294e"
KV_HEX_RE = re.compile(r'"(\w+)"\s*:\s*"([0-9a-f]+)"')   # a JSON line `"<key>"<sp>:<sp>"<hex>"`

# the first version of this part's raw, which the values-check (section 7) checked: script sha256, Code stamp, HEAD
FIRST_VERSION = ("dc1d784557412edce21d4351893f2a653b5f4fe057d4720aa4222fdae441ca76", "Fri Oct  9 04:09:27 UTC 2026",
                 "6485da2")
# the sha256 prefixes of the 12 distinct values the checker's every-entry copy of the history script listed
CHECKER_LEAK_KEYS = {"fab79a8e", "19e36255", "1a4fb901", "1aedc48e", "c17d7b45", "f40883a1", "421bbde9", "fc22e2de",
                     "3124edae", "13dfbe0e", "8e5d92fd", "a83bf7e9"}

PUBLIC_VERDICTS = {"FALSE-POSITIVE", "PUBLIC"}
BRUTE_FORCE_CLASSES = ("runpod_volume_id", "container_hostname", "ssh_port")


# the identifier classes the routing's redaction rule names (RunPod pod/volume id or name -- with the RunPod
# and proxy hostnames and the gateway user, which can carry a pod id --, IP, SSH port, key name, the LoRA
# phrase's class, the session link, the laptop or container hostname, third-party personal data, cloud
# account); by the history script's short labels. Its other identifier classes (local_temp_path,
# claude_projects_path, url_host) are local paths and public hosts, reported in the per-table counts.
REDACTION_EXCLUDED = ("local_temp_path", "claude_projects_path", "url_host")
REDACTION_CLASSES = ("runpod_pod_id", "runpod_volume_id", "runpod_volume_name", "runpod_endpoint_or_template_id",
                     "runpod_hostname", "proxy_hostname", "runpod_ssh_gateway_user", "container_hostname",
                     "dot_local_hostname", "ipv4_address", "ipv6_address", "ssh_port", "ssh_key_name",
                     "ssh_key_path", "ssh_identity_flag", "ssh_fingerprint", "ssh_public_key",
                     "claude_session_or_artifact_link", "passphrase_shaped", "email_address", "cloud_account_id")
# the routed run of the history script is pinned so that its refusal message's sample is reproducible
HASHSEED = "0"
RUN_ENV = {"GIT_TERMINAL_PROMPT": "0", "GH_PROMPT_DISABLED": "1", "GH_NO_UPDATE_NOTIFIER": "1",
           "GH_PAGER": "cat", "PAGER": "cat", "NO_COLOR": "1", "LC_ALL": "C"}


# ---------------------------------------------------------------- helpers
def run(args, input=None, env_extra=None, cwd=REPO):
    env = dict(os.environ)
    env.update(RUN_ENV)
    if env_extra:
        env.update(env_extra)
    return subprocess.run(args, input=input, capture_output=True, cwd=cwd, env=env)


def git(*args, ok=(0,), binary=False):
    p = run(["git", *args])
    if p.returncode not in ok:
        raise SystemExit(f"git {' '.join(args[:3])} failed rc={p.returncode}")
    return p.stdout if binary else p.stdout.decode("utf-8", "replace")


def sha256_hex(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()


def sha8(v):
    return sha256_hex(v)[:8]


def form(v, port=False):
    if port or re.match(r"\d{4}", v):   # a value opening with 4 digits: no digit of it shown
        return f"len{len(v)}:{sha8(v)}"
    if len(v) <= 4:
        return f"len{len(v)}:{sha8(v)}"
    return f"{v[:4]}...[len {len(v)}]#{sha8(v)}"


def short(cls):
    return cls.split(" (")[0]


def load_module(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(REPO, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def obj_local(sha):
    return run(["git", "cat-file", "-e", sha]).returncode == 0


def is_ancestor(a, b):
    p = run(["git", "merge-base", "--is-ancestor", a, b])
    if p.returncode in (0, 1):
        return p.returncode == 0
    return None


def peel_commit(sha):
    p = run(["git", "rev-parse", "--verify", "-q", sha + "^{commit}"])
    return p.stdout.decode().strip() if p.returncode == 0 else None


def snapshot():
    head = git("rev-parse", "HEAD").strip()
    refs = git("for-each-ref", "--format=%(refname) %(objectname) %(objecttype)").split("\n")
    return head, [tuple(r.split()) for r in refs if r.strip()]


def locate(lines, pred, start=0):
    for i in range(start, len(lines)):
        if pred(lines[i]):
            return i + 1
    return None


def gh(args):
    t0 = time.time()
    p = run(["gh", *args])
    out = p.stdout.decode("utf-8", "replace")
    err = p.stderr.decode("utf-8", "replace").strip().splitlines()
    data = None
    try:
        data = json.loads(out) if out.strip() else None
    except ValueError:
        data = None
    status = None
    if isinstance(data, dict) and "status" in data and "message" in data:
        status = str(data.get("status"))
    m = re.search(r"\(HTTP (\d{3})\)", " ".join(err))
    if m:
        status = status or m.group(1)
    errtype = None
    if isinstance(data, dict) and data.get("errors"):
        errtype = ",".join(sorted({str(e.get("type")) for e in data["errors"]}))
    return {"cmd": "gh " + " ".join(args), "rc": p.returncode, "data": data, "status": status,
            "graphql_error_type": errtype, "secs": round(time.time() - t0, 2)}


def flat_pages(data):
    """gh api --paginate --slurp: an array of pages (each an array or an object)."""
    if data is None:
        return []
    if isinstance(data, list) and data and all(isinstance(x, list) for x in data):
        return [y for x in data for y in x]
    if isinstance(data, list) and data and all(isinstance(x, dict) for x in data):
        return data
    return data if isinstance(data, list) else []


# ---------------------------------------------------------------- screening (GitHub-side text)
def make_screen(h, scrub, known_vals, identity_vals):
    """A screen of one text for the routing's redaction classes, with the history script's own patterns."""
    guard = list(scrub.GUARD_SHAPES)
    service = set(h.PENDING_EMAIL_EXEMPT)

    def screen(text):
        hits = collections.Counter()
        if not text:
            return hits
        for f, v in known_vals.items():
            if scrub.count_value(f, v, text):
                hits["known sensitive value"] += 1
        for nm, rx in guard:
            if rx.search(text):
                hits[nm] += 1
        for nm, prx, grp in h.PRECISE:
            for mt in prx.finditer(text):
                val = mt.group(grp) if grp else mt.group(0)
                a = text.rfind("\n", 0, mt.start()) + 1
                b = text.find("\n", mt.start())
                tri = h.triage_precise(nm, val, text[a:b if b >= 0 else len(text)], "<github>")
                if tri[0] != "FALSE-POSITIVE":
                    hits["precise:" + nm] += 1
        for _, v in h.iter_emails(text):
            if v not in service and v not in identity_vals:
                hits["email address (other)"] += 1
        for cls in ("runpod_pod_id (context: pod)", "runpod_volume_id (context: volume)",
                    "container_hostname (12 hex after host:/root@)", "claude_session_or_artifact_link",
                    "ssh_public_key", "ssh_fingerprint"):
            for mt in h.ID_RE[cls].finditer(text):
                v = mt.group("v")
                if cls.startswith(("runpod_pod_id", "runpod_volume_id")) and \
                        not (re.search(r"\d", v) and len(re.findall(r"[a-z]", v)) >= 2):
                    continue
                hits[short(cls)] += 1
        return hits
    return screen


# ---------------------------------------------------------------- release re-run pre-check of our own files
def rerun_precheck(h, text, path, known_set):
    """What the history script's pending-file scan and fallback triage would make of `text` at `path`:
    rows a release re-run would leave UNTRIAGED (the script's own functions; nothing new)."""
    out = collections.Counter()
    for nm, prx, grp in h.PRECISE:
        for mt in prx.finditer(text):
            val = mt.group(grp) if grp else mt.group(0)
            a = text.rfind("\n", 0, mt.start()) + 1
            b = text.find("\n", mt.start())
            if h.triage_precise(nm, val, text[a:b if b >= 0 else len(text)], path)[0] != "FALSE-POSITIVE":
                out["precise:" + nm] += 1
    # every identifier class the history scan applies to a committed blob (stricter than its pending scan,
    # which reads only PENDING_ID_CLASSES): anything not FALSE-POSITIVE / PUBLIC counts
    for cls in h.ID_PATTERNS:
        if cls in h.ANCHORED:
            for _, v in h.ANCHORED[cls](text):
                if v not in h.SAFE_VERBATIM and v not in known_set:
                    out["pending:" + short(cls)] += 1
            continue
        if h.ID_RE.get(cls) is None:
            continue
        for mt in h.ID_RE[cls].finditer(text):
            gd = mt.groupdict()
            g = next((x for x in ("v", "v2", "v3", "v4") if gd.get(x)), None)
            v = gd.get(g) if g else None
            if not v:
                continue
            if cls.startswith(("runpod_pod_id", "runpod_volume_id")) and \
                    not (re.search(r"\d", v) and len(re.findall(r"[a-z]", v)) >= 2):
                continue
            if h.triage_identifier(cls, v, None)[0] not in PUBLIC_VERDICTS:
                out["pending:" + short(cls)] += 1
    seen = set()
    for sm in h.SSH_LINE_RE.finditer(text):
        a = text.rfind("\n", 0, sm.start()) + 1
        if a in seen:
            continue
        seen.add(a)
        b = text.find("\n", sm.start())
        line = text[a:b if b >= 0 else len(text)]
        if h.code_port_only(line, "pending"):
            continue
        for pm in h.PORT_NUM_RE.finditer(line):
            v = pm.group("v")
            if not re.fullmatch(r"(19|20)\d\d", v):
                out["pending:ssh_port-line number"] += 1
    for line in text.split("\n"):
        if not re.search(h.FALLBACK_PATTERN, line, re.I):
            continue
        for alt, rx in h.FALLBACK_ALTS:
            for mt in re.finditer(rx, line, re.I):
                w = h.fallback_word(line, mt.start(), mt.end())
                we = mt.end()
                while we < len(line) and (line[we].isalnum() or line[we] in "_-"):
                    we += 1
                rule, _ = h.fallback_bulk_rule(alt, w, path, line[we:we + 4])
                out["fallback rule " + rule.split(" ")[0]] += 1
        for sm in h.SHAPE_RE.finditer(line):
            cls, _ = h.classify_value(sm.group(4), bool(sm.group(3)))
            out["shape UNTRIAGED" if cls is None and not h.manual(sm.group(4)) else "shape cleared"] += 1
    # the in-context high-entropy rule, as the history scan applies it to a blob (its own functions)
    li = h.LineIndex(text)
    he_seen = set()
    for mt in h.HE_RUN_RE.finditer(text):
        key = h.he_context(text, mt.start())
        if key is None:
            continue
        v = mt.group(0)
        if h.entropy(v) <= 4.0 or v in he_seen:
            continue
        he_seen.add(v)
        out["high_entropy " + h.triage_he(v, li.line_text(mt.start()), key)[0]] += 1
    # the context-free high-entropy rules (its cf_scan, into a table held here; distinct values)
    cf_tab = {}

    def cf_add(table, v, kind, sha, path_, commit, li_, off, extra=None):
        return table.setdefault(v, {})
    h.cf_scan(text, "blob", None, path, None, li, cf_tab, cf_add)
    for v, e in cf_tab.items():
        out["context_free " + e["triage"][0]] += 1
    return out


def precheck_bad(c):
    """The rows of a precheck counter that a release re-run would leave open."""
    return {k: n for k, n in c.items()
            if k.startswith(("precise:", "pending:", "shape UNTRIAGED"))
            or k in ("fallback rule T3", "fallback rule K2", "fallback rule X")
            or (k.startswith(("high_entropy ", "context_free ")) and k.split(" ", 1)[1] not in PUBLIC_VERDICTS)}


# ---------------------------------------------------------------- release v2 (2026-11-03): the pre-flip read
# The release block of 2026-10-27, item 6 (V2_BLOCK at V2_BLOCK_LINE, asserted at every run) names the read:
# V2_BLOCK_TEXT below, verbatim. Under the release route (the PI's word of 2026-10-29, "fresh repository at the tag
# push, as proposed"; the scrub index, section 14), it reads the new repository, and Code checks there too that the
# commits no local ref reaches are not served (the history script's read_v2_record gives them, in memory only). The
# v1 read (main(), run with --v1) compares against the 2026-10-08 history raw and v1's baselines, which do not hold at
# v2; v2's read is main_v2: the block's checks, that check, and the history script run again with its outputs outside
# the repository (the pre-flip read's interim scan, as the history script's texts name it). It prints ref names,
# flags, counts and HTTP statuses only: no GitHub-side text, no unexpected ref by name, no commit id of the four.
V2_BLOCK = ("results/raw/2026-10-27_note-design-to-code_release-block.md", "2fb0cf0")
V2_BLOCK_LINE = 46
V2_BLOCK_TEXT = ("`git ls-remote origin` = `main` + tags only (`cycle-2-close`, `cycle-4-close`, `note-2026-10-v1`, "
                 "`note-2026-10-v2`); the GitHub-side surfaces (PRs, issues, Actions, wiki, Pages, deploy keys, webhooks, "
                 "force-pushes). Any remaining `wip/*`, `main-*` or `claude/*` head: STOP and report.")
V2_EXPECTED_REFS = ("refs/heads/main", "refs/tags/cycle-2-close", "refs/tags/cycle-4-close",
                    "refs/tags/note-2026-10-v1", "refs/tags/note-2026-10-v2")
V2_STOP_HEAD_RE = re.compile(r"refs/heads/(?:wip/|main-|claude/)")
V2_DATE_SLOT = "YYYY-MM-DD"
V2_MD = "results/raw/YYYY-MM-DD_note-N12-preflip.md"      # the run's PI-local date fills the slot
V2_JSON = "results/raw/YYYY-MM-DD_note-N12-preflip.json"
V2_HIST_SUMMARY_RE = re.compile(
    r"true-secret candidates (\d+); untriaged (\d+) \(all tables: ids (\d+), sweep (\d+), shape rows (\d+); pending "
    r"files (\d+)\);.*found verbatim (\d+); controls (ALL PASS|[A-Z ]+?);")


def v2_count(r):
    """A count from a gh read: the list's length (paginated pages flattened), or None when the read failed."""
    if r["rc"] != 0:
        return None
    d = r["data"]
    if isinstance(d, dict) and "total_count" in d:
        return d["total_count"]
    return len(flat_pages(d)) if isinstance(d, list) else None


def main_v2(a, hist_dir):
    today = datetime.date.today().isoformat()
    md_out = V2_MD.replace(V2_DATE_SLOT, today)
    js_out = V2_JSON.replace(V2_DATE_SLOT, today)
    for o, want in ((a.out, md_out), (a.json_out, js_out)):
        if o is not None and os.path.normpath(o) != want:
            raise SystemExit(f"refusing an output other than this read's own two files ({md_out}, {js_out}): {o}")
    for o in (md_out, js_out):
        if git("ls-files", "--", o).strip() or run(["git", "cat-file", "-e", f"HEAD:{o}"]).returncode == 0:
            raise SystemExit(f"refusing to overwrite a tracked raw: {o}")
    stamp = run(["date", "-u"]).stdout.decode().strip()
    head, _refs0 = snapshot()
    me_rel = os.path.relpath(os.path.abspath(__file__), REPO)
    me_sha = sha256_hex(open(os.path.abspath(__file__), "rb").read())
    blk = git("show", f"{V2_BLOCK[1]}:{V2_BLOCK[0]}").split("\n")
    if V2_BLOCK_TEXT not in blk[V2_BLOCK_LINE - 1]:
        raise SystemExit(f"the block's item 6 is not on {V2_BLOCK[0]}@{V2_BLOCK[1]}:{V2_BLOCK_LINE} as quoted; nothing "
                         f"written")
    hs_wt = sha256_hex(open(os.path.join(REPO, HIST_SCRIPT), "rb").read())
    hs_head = sha256_hex(git("show", f"HEAD:{HIST_SCRIPT}", binary=True))
    J = {"item": "N12 pre-flip read (release v2)", "block": BLOCK, "code_stamp_utc": stamp, "head": head,
         "script": {"path": me_rel, "sha256": me_sha},
         "history_script": {"path": HIST_SCRIPT, "sha256_worktree": hs_wt, "sha256_head": hs_head,
                            "pinned": HIST_SCRIPT_SHA, "equal": hs_wt == hs_head == HIST_SCRIPT_SHA},
         "read": {"source": f"{V2_BLOCK[0]}@{V2_BLOCK[1]}:{V2_BLOCK_LINE}", "text": V2_BLOCK_TEXT},
         "repository": SLUG}
    h = load_module("n12_history_v2", HIST_SCRIPT)
    rec = h.read_v2_record()
    unserved = [rec["tp_commit"]] + [c for _n, c in rec["tips"]]
    hidden = [rec["tp_id"]] + [c[:7] for c in unserved]

    # ======================================================== (1) server refs
    url = git("remote", "get-url", "origin").strip()
    url_shown = re.sub(r"//[^/@]*@", "//", url)
    lr = run(["git", "ls-remote", "--symref", "origin"])
    server, peeled, symrefs = {}, {}, {}
    for ln in lr.stdout.decode().splitlines():
        if ln.startswith("ref: "):
            tgt, _t, name = ln[5:].partition("\t")
            symrefs[name] = tgt
            continue
        sha, _t, name = ln.partition("\t")
        if name.endswith("^{}"):
            peeled[name[:-3]] = sha
        elif name:
            server[name] = sha
    rows = []
    for ref in V2_EXPECTED_REFS:
        loc = run(["git", "rev-parse", "--verify", "-q", ref]).stdout.decode().strip() or None
        srv = server.get(ref)
        rows.append({"ref": ref, "server": srv, "local": loc, "equal": srv is not None and srv == loc,
                     "object_local": bool(srv) and obj_local(srv),
                     "peeled_commit": peeled.get(ref) or (peel_commit(srv) if srv and obj_local(srv) else None)})
    unexpected = [n for n in server if n not in V2_EXPECTED_REFS and n != "HEAD"]
    ns = collections.Counter("/".join(n.split("/")[:2]) for n in unexpected)
    stop_heads = [n for n in unexpected if V2_STOP_HEAD_RE.match(n)]
    refs_pass = (lr.returncode == 0 and not unexpected and all(r["equal"] and r["object_local"] for r in rows)
                 and symrefs.get("HEAD") == "refs/heads/main")
    J["refs"] = {"origin_url": url_shown, "rc": lr.returncode, "symrefs": symrefs, "expected": rows,
                 "unexpected_by_namespace": dict(ns), "unexpected": len(unexpected),
                 "stop_heads": len(stop_heads), "pass": refs_pass}

    # ======================================================== (2) GitHub-side surfaces
    G = collections.OrderedDict()
    G["repo_api"] = gh(["api", f"repos/{SLUG}"])
    G["pull_requests"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/pulls?state=all&per_page=100"])
    G["issues"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/issues?state=all&per_page=100"])
    G["issue_comments"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/issues/comments?per_page=100"])
    G["review_comments"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/pulls/comments?per_page=100"])
    G["commit_comments"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/comments?per_page=100"])
    G["releases"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/releases?per_page=100"])
    G["workflows"] = gh(["api", f"repos/{SLUG}/actions/workflows"])
    G["runs"] = gh(["api", f"repos/{SLUG}/actions/runs?per_page=1"])
    G["artifacts"] = gh(["api", f"repos/{SLUG}/actions/artifacts?per_page=1"])
    G["deploy_keys"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/keys?per_page=100"])
    G["webhooks"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/hooks?per_page=100"])
    G["milestones"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/milestones?state=all&per_page=100"])
    G["forks"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/forks?per_page=100"])
    G["pages"] = gh(["api", f"repos/{SLUG}/pages"])
    G["activity"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/activity?per_page=100"])
    G["graphql_counts"] = gh(["api", "graphql", "-f",
                              "query=query{repository(owner:\"%s\",name:\"%s\"){discussions(first:1){totalCount} "
                              "deployments(first:1){totalCount} environments(first:1){totalCount}}}" % (OWNER, NAME)])
    # Projects (v2) need a token scope the v1 read found missing (its raw: Projects NOT READ); read, and reported apart
    G["graphql_projects_v2"] = gh(["api", "graphql", "-f",
                                   "query=query{repository(owner:\"%s\",name:\"%s\"){projectsV2(first:1)"
                                   "{totalCount}}}" % (OWNER, NAME)])
    wk = run(["git", "ls-remote", f"https://github.com/{SLUG}.wiki.git"])
    wiki_refs = len([x for x in wk.stdout.decode().splitlines() if x.strip()])
    ra = G["repo_api"]["data"] if isinstance(G["repo_api"]["data"], dict) else {}
    issues_only = [x for x in flat_pages(G["issues"]["data"]) if isinstance(x, dict) and "pull_request" not in x]
    gq = (((G["graphql_counts"]["data"] or {}).get("data") or {}).get("repository") or {})
    act = flat_pages(G["activity"]["data"])
    act_types = collections.Counter(x.get("activity_type") for x in act)
    act_refs = collections.Counter(x.get("ref") if x.get("ref") in V2_EXPECTED_REFS else "<other>" for x in act)
    surf = collections.OrderedDict()
    for k in ("pull_requests", "issue_comments", "review_comments", "commit_comments", "releases", "deploy_keys",
              "webhooks", "milestones", "forks"):
        surf[k] = v2_count(G[k])
    surf["issues"] = len(issues_only) if G["issues"]["rc"] == 0 else None
    surf["workflows"] = v2_count(G["workflows"])
    surf["actions_runs"] = v2_count(G["runs"])
    surf["artifacts"] = v2_count(G["artifacts"])
    for k in ("discussions", "deployments", "environments"):
        surf[k] = (gq.get(k) or {}).get("totalCount") if gq else None
    gp = (((G["graphql_projects_v2"]["data"] or {}).get("data") or {}).get("repository") or {})
    projects_v2 = (gp.get("projectsV2") or {}).get("totalCount") if gp else None
    surf["wiki_refs"] = wiki_refs
    zero_ok = all(v == 0 for v in surf.values())
    pages_ok = G["pages"]["status"] == "404"
    act_ok = (G["activity"]["rc"] == 0 and act_types.get("force_push", 0) == 0
              and act_types.get("branch_deletion", 0) == 0 and act_refs.get("<other>", 0) == 0)
    repo_ok = ra.get("full_name") == SLUG and ra.get("fork") is False
    settings = {k: ra.get(k) for k in ("full_name", "id", "created_at", "private", "visibility", "default_branch",
                                       "fork", "archived", "disabled", "has_issues", "has_projects", "has_wiki",
                                       "has_pages", "has_discussions", "has_downloads", "allow_forking",
                                       "forks_count", "open_issues_count")}
    settings["description_chars"] = len(ra.get("description") or "")
    settings["homepage_chars"] = len(ra.get("homepage") or "")
    settings["topics"] = len(ra.get("topics") or [])
    surf_pass = zero_ok and pages_ok and act_ok and repo_ok
    J["surfaces"] = {"counts": surf, "projects_v2": projects_v2, "pages_status": G["pages"]["status"],
                     "activity_records": len(act),
                     "activity_by_type": dict(act_types), "activity_by_ref": dict(act_refs), "settings": settings,
                     "reads": {k: {"cmd": v["cmd"], "rc": v["rc"], "status": v["status"]} for k, v in G.items()},
                     "wiki_cmd": f"git ls-remote https://github.com/{SLUG}.wiki.git", "wiki_rc": wk.returncode,
                     "pass": surf_pass}

    # ======================================================== (3) the commits no local ref reaches
    us = []
    for i, c in enumerate(unserved, 1):
        r = gh(["api", f"repos/{SLUG}/commits/{c}"])
        us.append({"commit": f"{i} of {len(unserved)}", "rc": r["rc"],
                   "status": "200" if r["rc"] == 0 else r["status"], "served": r["rc"] == 0})
    unserved_pass = len(us) == 4 and all(not x["served"] and x["status"] in ("404", "422") for x in us)
    J["unserved"] = {"source": "the history script's read_v2_record (the origin-only ref's commit and the three wip "
                               "branches' origin commits), held in memory", "checks": us, "pass": unserved_pass}

    # ======================================================== (4) the interim history scan
    hmd, hjs = os.path.join(hist_dir, "history_interim.md"), os.path.join(hist_dir, "history_interim.json")
    t0 = time.time()
    hp = run([sys.executable, HIST_SCRIPT, "--out", hmd, "--json-out", hjs])
    hout = (hp.stdout.decode("utf-8", "replace") + "\n" + hp.stderr.decode("utf-8", "replace"))
    m = V2_HIST_SUMMARY_RE.search(hout)
    refused = re.search(r"REFUSING TO WRITE: (\d+) guarded value", hout)
    hs = {"cmd": f"{os.path.relpath(sys.executable, REPO) if sys.executable.startswith(REPO) else 'python'} "
                 f"{HIST_SCRIPT} --out <outside>/history_interim.md --json-out <outside>/history_interim.json",
          "rc": hp.returncode, "secs": round(time.time() - t0, 1),
          "refused_guarded_values": int(refused.group(1)) if refused else 0}
    if m:
        hs.update({"true_secret_candidates": int(m.group(1)), "untriaged": int(m.group(2)), "ids": int(m.group(3)),
                   "sweep": int(m.group(4)), "shape_rows": int(m.group(5)), "pending_files": int(m.group(6)),
                   "found_verbatim": int(m.group(7)), "controls": m.group(8)})
    hist_pass = (hp.returncode == 0 and m is not None and hs["true_secret_candidates"] == 0 and hs["untriaged"] == 0
                 and hs["found_verbatim"] == 0 and hs["controls"] == "ALL PASS")
    hs["pass"] = hist_pass
    J["history_scan"] = hs

    all_pass = refs_pass and surf_pass and unserved_pass and hist_pass and J["history_script"]["equal"]
    J["pass"] = all_pass
    J["stop"] = bool(stop_heads)

    # ======================================================== write
    out = []
    w = out.append
    w("# AUDIT-note-release v1.2 -- N12 pre-flip read (release v2)")
    w("")
    w(f"- Code stamp: {stamp} (date -u); HEAD `{head}`; repository `{SLUG}` (origin `{url_shown}`).")
    w(f"- Script: `{me_rel}` sha256 `{me_sha}`; the history script `{HIST_SCRIPT}` sha256 `{hs_head}` at HEAD, "
      f"{'equal to' if J['history_script']['equal'] else 'NOT equal to'} the pinned `{HIST_SCRIPT_SHA}` "
      f"(working tree: {'equal' if hs_wt == hs_head else 'NOT equal'}).")
    w(f"- The read, as the release block names it (`{V2_BLOCK[0]}@{V2_BLOCK[1]}:{V2_BLOCK_LINE}`, item 6, asserted "
      f"verbatim at this run): \"{V2_BLOCK_TEXT}\" Under the release route (the PI's word of 2026-10-29, \"fresh "
      f"repository at the tag push, as proposed\"), this read is of the new repository, and it checks there that the "
      f"commits no local ref reaches are not served.")
    w("- Read-only: `git ls-remote`, `git rev-parse`, `git cat-file`, `git remote get-url` and `gh api` GET reads; "
      "nothing fetched, pushed or written but this file and its JSON (and the history script's outputs, outside the "
      "repository). It prints ref names, flags, counts and HTTP statuses: no GitHub-side text, no unexpected ref by "
      "name, no commit id of the four in section 3.")
    w("")
    w("## 1. Server refs (`git ls-remote --symref origin`)")
    w("")
    w("| ref | on the server | local | equal | object local | its commit |")
    w("|---|---|---|---|---|---|")
    for r in rows:
        w(f"| `{r['ref']}` | `{r['server'] or '-'}` | `{r['local'] or '-'}` | {'yes' if r['equal'] else 'NO'} | "
          f"{'yes' if r['object_local'] else 'NO'} | `{r['peeled_commit'] or '-'}` |")
    w("")
    w(f"- HEAD on the server points at `{symrefs.get('HEAD', '-')}`.")
    w(f"- Refs on the server beyond these five: {len(unexpected)}"
      + (" (by namespace: " + ", ".join(f"`{k}` {v}" for k, v in sorted(ns.items())) + ")" if unexpected else "")
      + f"; `wip/*`, `main-*` or `claude/*` heads: {len(stop_heads)}.")
    w("")
    bad1 = [r["ref"] for r in rows if not (r["equal"] and r["object_local"])]
    w(f"**Pass/STOP line (1):** {'PASS' if refs_pass else ('STOP' if stop_heads else 'FLAG')} -- the server "
      + ("holds `main` and the four tags only, each equal to the local ref, and HEAD points at `main`." if refs_pass
         else "does not hold exactly `main` and the four tags, each equal to the local ref, with HEAD at `main`: "
         + "; ".join(x for x in ((("not on the server, or not equal to the local ref: "
                                   + ", ".join(f"`{b}`" for b in bad1))
                                  if bad1 else ""),
                                 (f"{len(unexpected)} other ref(s)" if unexpected else ""),
                                 ("HEAD not at `main`" if symrefs.get("HEAD") != "refs/heads/main" else ""),
                                 (f"ls-remote exit {lr.returncode}" if lr.returncode else "")) if x) + "."))
    w("")
    w("## 2. GitHub-side surfaces (read-only `gh api`)")
    w("")
    w("| surface | count |")
    w("|---|---|")
    for k, v in surf.items():
        w(f"| {k.replace('_', ' ')} | {'read failed' if v is None else v} |")
    w(f"| Pages (`repos/{SLUG}/pages`) | HTTP {G['pages']['status'] or G['pages']['rc']} |")
    w(f"| Projects (v2), not in the block's list | {'not read (the token lacks the scope)' if projects_v2 is None else projects_v2} |")
    w("")
    w(f"- Activity record: {len(act)} record(s), by type "
      + (", ".join(f"{k} {v}" for k, v in sorted(act_types.items(), key=lambda x: str(x[0]))) or "none")
      + "; by ref " + (", ".join(f"`{k}` {v}" for k, v in sorted(act_refs.items(), key=lambda x: str(x[0])))
                       or "none") + ".")
    w(f"- Repository: `{settings['full_name']}`, created {settings['created_at']}, private {settings['private']}, "
      f"visibility {settings['visibility']}, default branch `{settings['default_branch']}`, fork {settings['fork']}, "
      f"archived {settings['archived']}; has_issues {settings['has_issues']}, has_projects "
      f"{settings['has_projects']}, has_wiki {settings['has_wiki']}, has_pages {settings['has_pages']}, "
      f"has_discussions {settings['has_discussions']}, allow_forking {settings['allow_forking']}; description "
      f"{settings['description_chars']} characters, homepage {settings['homepage_chars']} characters, topics "
      f"{settings['topics']} (texts not printed).")
    w("")
    w(f"**Pass line (2):** {'PASS' if surf_pass else 'FLAG'} -- every surface above is empty (Pages 404, the wiki "
      "with no refs), the activity record has no force push, no branch deletion and no ref beyond the five, and the "
      "repository read is the one named here, not a fork." if surf_pass else
      "**Pass line (2):** FLAG -- " + "; ".join(x for x in (
          ("not empty or not read: " + ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in surf.items() if v != 0))
          if not zero_ok else "",
          f"Pages HTTP {G['pages']['status'] or G['pages']['rc']}" if not pages_ok else "",
          (f"activity record: force push {act_types.get('force_push', 0)}, branch deletion "
           f"{act_types.get('branch_deletion', 0)}, records on other refs {act_refs.get('<other>', 0)}, read exit "
           f"{G['activity']['rc']}") if not act_ok else "",
          f"repository read: `{ra.get('full_name')}`, fork {ra.get('fork')}" if not repo_ok else "") if x) + ".")
    w("")
    w("## 3. The commits no local ref reaches (the release route's check)")
    w("")
    w("The origin-only ref's commit and the three wip branches' origin commits, read from the release-v2 records by the "
      "history script's `read_v2_record`, held in memory and never printed; each asked of this repository with "
      f"`gh api repos/{SLUG}/commits/<commit>`.")
    w("")
    for x in us:
        w(f"- commit {x['commit']}: HTTP {x['status'] or x['rc']}, {'served' if x['served'] else 'not served'}")
    w("")
    w(f"**Pass line (3):** {'PASS -- none of the four is served.' if unserved_pass else 'FLAG -- see above.'}")
    w("")
    w("## 4. The interim history scan")
    w("")
    w(f"`{hs['cmd']}` (outputs outside the repository; exit {hs['rc']}; {hs['secs']} s): "
      + (f"true-secret candidates {hs['true_secret_candidates']}; untriaged {hs['untriaged']} (ids {hs['ids']}, sweep "
         f"{hs['sweep']}, shape rows {hs['shape_rows']}; pending files {hs['pending_files']}); found verbatim "
         f"{hs['found_verbatim']}; controls {hs['controls']}." if m else
         f"no summary line (refused guarded values: {hs['refused_guarded_values']})."))
    w("")
    w(f"**Pass line (4):** {'PASS' if hist_pass else 'FLAG'}")
    w("")
    w("## 5. For the PI")
    w("")
    w(("- All four parts pass: on this read, the repository is ready for the visibility flip, which is the PI's."
       if all_pass else "- Not all parts pass (above): not ready for the flip."))
    w("- After the flip, the PI's own steps from the release route: re-adding the repository to the Claude GitHub app "
      "and to Zenodo.")
    md = "\n".join(out) + "\n"
    js = json.dumps(J, indent=1, ensure_ascii=False)
    for t_ in (md, js):
        for v in hidden:
            if v and v in t_:
                raise SystemExit("REFUSING TO WRITE: a held value appears in an output; nothing written")
        for n in unexpected:
            if n in t_:
                raise SystemExit("REFUSING TO WRITE: an unexpected ref's name appears in an output; nothing written")
    with open(os.path.join(REPO, md_out), "w", encoding="utf-8") as f:
        f.write(md)
    with open(os.path.join(REPO, js_out), "w", encoding="utf-8") as f:
        f.write(js + "\n")
    print(f"wrote {md_out} and {js_out}; HEAD {head[:10]}; refs {'PASS' if refs_pass else 'FLAG'}; surfaces "
          f"{'PASS' if surf_pass else 'FLAG'}; unserved {'PASS' if unserved_pass else 'FLAG'}; history scan "
          f"{'PASS' if hist_pass else 'FLAG'}; STOP heads {len(stop_heads)}")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--history-dir", required=True,
                    help="directory OUTSIDE the repository for the history script's outputs")
    ap.add_argument("--rec", default="6485da2", help="commit whose committed history JSON / scrub index is compared")
    ap.add_argument("--base", default="bbc9ffe", help="the block's commit (the history script's default --since)")
    ap.add_argument("--out", default=None)
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--v1", action="store_true", help="release v1's read (default: release v2's, main_v2)")
    a = ap.parse_args()
    hist_dir = os.path.abspath(a.history_dir)
    if hist_dir == REPO or hist_dir.startswith(REPO + os.sep):
        raise SystemExit("--history-dir must lie outside the repository")
    os.makedirs(hist_dir, exist_ok=True)
    if not a.v1:
        return main_v2(a, hist_dir)
    a.out = a.out or DEFAULT_MD
    a.json_out = a.json_out or DEFAULT_JSON
    for o in (a.out, a.json_out):
        ab = os.path.abspath(os.path.join(REPO, o))
        if not ab.startswith(os.path.join(REPO, "results", "raw") + os.sep):
            raise SystemExit(f"refusing an output outside results/raw/: {o}")
        if os.path.basename(ab) not in (os.path.basename(DEFAULT_MD), os.path.basename(DEFAULT_JSON)):
            raise SystemExit(f"refusing an output other than this script's own two files: {o}")

    T0 = time.time()
    J = {"item": "N12 pre-flip reads", "block": BLOCK}
    stamp = run(["date", "-u"]).stdout.decode().strip()
    head0, refs0 = snapshot()
    mine = {os.path.relpath(os.path.abspath(__file__), REPO), DEFAULT_MD, DEFAULT_JSON, a.out, a.json_out}
    untracked0 = [x for x in git("ls-files", "--others", "--exclude-standard").split("\n") if x and x not in mine]
    modified0 = [x for x in git("ls-files", "-m").split("\n") if x]
    rec = git("rev-parse", "--verify", a.rec + "^{commit}").strip()
    base = git("rev-parse", "--verify", a.base + "^{commit}").strip()
    block_wt = sha256_hex(open(os.path.join(REPO, BLOCK), "rb").read())
    block_head = sha256_hex(git("show", f"HEAD:{BLOCK}", binary=True))
    me_rel = os.path.relpath(os.path.abspath(__file__), REPO)
    me_sha = sha256_hex(open(os.path.abspath(__file__), "rb").read())
    me_src = open(os.path.abspath(__file__), encoding="utf-8").read()
    hs_wt = sha256_hex(open(os.path.join(REPO, HIST_SCRIPT), "rb").read())
    hs_head = sha256_hex(git("show", f"HEAD:{HIST_SCRIPT}", binary=True))
    py = sys.version.split()[0]
    interp = os.path.relpath(sys.executable, REPO) if sys.executable.startswith(REPO) else "(outside the repository)"
    git_ver = git("--version").strip()
    gh_ver = run(["gh", "--version"]).stdout.decode().splitlines()[0].strip()

    h = load_module("n12_history_rules", HIST_SCRIPT)
    scrub = load_module("n12_scrub_rules", SCRUB_SCRIPT)
    hj = json.loads(git("show", f"{rec}:{HIST_JSON}"))
    hmd = git("show", f"{rec}:{HIST_MD}").split("\n")
    smd = git("show", f"{rec}:{SCRUB_MD}").split("\n")

    # ---------- known sensitive values (in memory; never printed) ----------
    kv = hj["prerelease_pending_files"]["known_values"]
    corpus = git("log", "-p", "--all", "--format=fuller") + "\n" + \
        git("log", "--all", "--format=%an <%ae>%n%cn <%ce>") + "\n" + \
        git("for-each-ref", "--format=%(taggername) %(taggeremail)", "refs/tags")
    known = scrub.resolve_values(list(kv.keys()), corpus)
    del corpus
    known_label = {f: kv[f][0] for f in kv}
    identity_vals = {v for f, v in known.items() if known_label[f].startswith("identity email")}
    unresolved = [f for f in kv if f not in known]

    # ======================================================== (1) server refs
    url = git("remote", "get-url", "origin").strip()
    url_userinfo = bool(re.search(r"://[^/@]+@", url))
    url_shown = re.sub(r"://[^/@]+@", "://<userinfo>@", url)
    t1 = time.time()
    lr = run(["git", "ls-remote", "--symref", "origin"])
    lr_secs = round(time.time() - t1, 2)
    if lr.returncode != 0:
        raise SystemExit("git ls-remote origin failed; nothing written")
    server, symrefs, peeled = {}, {}, {}
    for ln in lr.stdout.decode().splitlines():
        if ln.startswith("ref: "):
            tgt, name = ln[5:].split("\t")
            symrefs[name] = tgt
            continue
        sha, name = ln.split("\t")
        if name.endswith("^{}"):
            peeled[name[:-3]] = sha
        else:
            server[name] = sha
    local = {r[0]: (r[1], r[2]) for r in refs0}
    hist_refs = {r[0]: r[1] for r in hj["refs"]}
    hist_anc = hj["ancestor_of_origin_main"]
    hist_tab_start = locate(hmd, lambda s: s.startswith("| ref | object | type | ancestor of origin/main |"))
    hist_tab_end = hist_tab_start
    while hist_tab_end < len(hmd) and hmd[hist_tab_end].startswith("|"):
        hist_tab_end += 1
    om = local.get("refs/remotes/origin/main", (None,))[0]

    def local_counterparts(name):
        if name == "HEAD":
            return []
        if name.startswith("refs/heads/"):
            b = name[len("refs/heads/"):]
            c = ["refs/remotes/origin/" + b]
            if name == "refs/heads/main":
                c.insert(0, "refs/heads/main")
            return c
        if name.startswith("refs/tags/"):
            return [name]
        return []

    srows = []
    for name in sorted(server):
        sha = server[name]
        lc = [c for c in local_counterparts(name) if c in local]
        here = obj_local(sha)
        commit = peel_commit(sha) if here else None
        anc = is_ancestor(commit, om) if (here and commit and om) else None
        hist_names = [c for c in local_counterparts(name) if c in hist_refs]
        srows.append({
            "ref": name, "object": sha, "symref_target": symrefs.get(name),
            "peeled": peeled.get(name), "object_local": here,
            "local_counterparts": {c: local[c][0] == sha for c in lc},
            "in_history_raw_table": {c: {"object_there": hist_refs[c][:10], "equal_now": hist_refs[c] == sha,
                                         "ancestor_there": hist_anc.get(c)} for c in hist_names},
            "commit": commit, "ancestor_of_origin_main": anc,
            "class": ("pull" if name.startswith("refs/pull/") else "head" if name.startswith("refs/heads/")
                      else "tag" if name.startswith("refs/tags/") else "HEAD" if name == "HEAD" else "other")})
    server_not_local = [r["ref"] for r in srows if r["ref"] != "HEAD" and not r["local_counterparts"]]
    obj_missing = [r["ref"] for r in srows if not r["object_local"]]
    pulls = [r for r in srows if r["class"] == "pull"]
    others = [r for r in srows if r["class"] == "other"]
    local_not_server = []
    for name in sorted(local):
        if name.startswith("refs/remotes/origin/"):
            sname = "refs/heads/" + name[len("refs/remotes/origin/"):]
        else:
            sname = name
        if sname not in server:
            local_not_server.append(name)
    peel_check = {n: (peel_commit(n) == p) for n, p in peeled.items()}
    ref_unequal = [r["ref"] for r in srows for c, eq in r["local_counterparts"].items() if not eq]
    not_anc = [r["ref"] for r in srows if r["ref"] != "HEAD" and r["ancestor_of_origin_main"] is not True]
    head_sym_ok = symrefs.get("HEAD") == "refs/heads/main"
    not_in_hist = [r["ref"] for r in srows if r["ref"] != "HEAD" and not r["in_history_raw_table"]]
    refs_pass = not (server_not_local or obj_missing or pulls or others or ref_unequal or not_anc or
                     not_in_hist) and head_sym_ok
    moved_since_hist = {c: (hist_refs[c][:10], local[c][0][:10]) for c in hist_refs
                        if c in local and local[c][0] != hist_refs[c]}
    J["refs"] = {"origin_url": url_shown, "origin_url_userinfo": url_userinfo, "ls_remote_secs": lr_secs,
                 "server": srows, "symrefs": symrefs, "peeled_equal_local": peel_check,
                 "server_not_local": server_not_local, "server_objects_not_local": obj_missing,
                 "pull_refs": len(pulls), "other_refs": len(others), "local_not_on_server": local_not_server,
                 "local_counterpart_unequal": ref_unequal, "not_ancestor_of_origin_main": not_anc,
                 "not_in_history_raw_table": not_in_hist,
                 "history_raw_refs": hj["refs"], "moved_since_history_raw": moved_since_hist, "pass": refs_pass}

    # ======================================================== (2) GitHub-side surfaces
    G = collections.OrderedDict()
    G["repo_view"] = gh(["repo", "view", SLUG, "--json",
                         "visibility,isPrivate,hasWikiEnabled,hasIssuesEnabled,hasProjectsEnabled,"
                         "hasDiscussionsEnabled,defaultBranchRef,licenseInfo"])
    G["repo_api"] = gh(["api", f"repos/{SLUG}"])
    G["pr_list"] = gh(["pr", "list", "-R", SLUG, "--state", "all", "--limit", "1000", "--json",
                       "number,state,title,author,createdAt,headRefName"])
    G["issue_list"] = gh(["issue", "list", "-R", SLUG, "--state", "all", "--limit", "1000", "--json",
                          "number,state,title,author,createdAt"])
    G["issue_comments"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/issues/comments?per_page=100"])
    G["review_comments"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/pulls/comments?per_page=100"])
    G["commit_comments"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/comments?per_page=100"])
    G["release_list"] = gh(["release", "list", "-R", SLUG, "--limit", "1000", "--json",
                            "tagName,name,isDraft,isPrerelease,publishedAt"])
    G["run_list"] = gh(["run", "list", "-R", SLUG, "--limit", "200", "--json",
                        "databaseId,status,conclusion,event,workflowName,createdAt,headBranch,displayTitle"])
    G["workflows"] = gh(["api", f"repos/{SLUG}/actions/workflows"])
    G["artifacts"] = gh(["api", f"repos/{SLUG}/actions/artifacts?per_page=100"])
    G["pages"] = gh(["api", f"repos/{SLUG}/pages"])
    G["deploy_keys"] = gh(["api", f"repos/{SLUG}/keys"])
    G["hooks"] = gh(["api", f"repos/{SLUG}/hooks"])
    G["milestones"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/milestones?state=all&per_page=100"])
    G["activity"] = gh(["api", "--paginate", "--slurp", f"repos/{SLUG}/activity?per_page=100"])
    G["graphql_counts"] = gh(["api", "graphql", "-f",
                              "query=query{repository(owner:\"%s\",name:\"%s\"){discussions(first:1){totalCount} "
                              "deployments(first:1){totalCount} environments(first:1){totalCount}}}" % (OWNER, NAME)])
    G["graphql_projects_v2"] = gh(["api", "graphql", "-f",
                                   "query=query{repository(owner:\"%s\",name:\"%s\"){projectsV2(first:1)"
                                   "{totalCount}}}" % (OWNER, NAME)])
    t1 = time.time()
    wk = run(["git", "ls-remote", f"https://github.com/{SLUG}.wiki.git"])
    wiki = {"cmd": f"git ls-remote https://github.com/{SLUG}.wiki.git", "rc": wk.returncode,
            "refs": len([x for x in wk.stdout.decode().splitlines() if x.strip()]),
            "not_found": "not found" in wk.stderr.decode().lower(), "secs": round(time.time() - t1, 2)}

    screen = make_screen(h, scrub, known, identity_vals)
    screened = collections.Counter()
    screen_hits = collections.Counter()

    def scr(label, text):
        screened[label] += 1
        for k, n in screen(text or "").items():
            screen_hits[(label, k)] += n

    def is_owner(login):
        return (login or "").lower() == OWNER.lower()

    others_logins = collections.Counter()

    def author_of(x):
        lg = ((x or {}).get("author") or (x or {}).get("user") or (x or {}).get("actor") or {}).get("login")
        if not is_owner(lg):
            others_logins[form(lg or "<none>")] += 1
        return "owner" if is_owner(lg) else "other"

    S = collections.OrderedDict()
    rv = G["repo_view"]["data"] or {}
    ra = G["repo_api"]["data"] or {}
    S["settings"] = {"visibility": rv.get("visibility"), "isPrivate": rv.get("isPrivate"),
                     "hasWikiEnabled": rv.get("hasWikiEnabled"), "hasIssuesEnabled": rv.get("hasIssuesEnabled"),
                     "hasProjectsEnabled": rv.get("hasProjectsEnabled"),
                     "hasDiscussionsEnabled": rv.get("hasDiscussionsEnabled"),
                     "defaultBranch": (rv.get("defaultBranchRef") or {}).get("name"),
                     "licenseInfo": rv.get("licenseInfo"),
                     "api": {k: ra.get(k) for k in ("private", "visibility", "has_pages", "has_downloads",
                                                    "allow_forking", "forks_count", "network_count", "archived",
                                                    "disabled", "fork", "open_issues_count",
                                                    "web_commit_signoff_required")}}
    prs = G["pr_list"]["data"] if isinstance(G["pr_list"]["data"], list) else []
    pr_detail = []
    for pr in prs:
        scr("pr title", pr.get("title"))
        scr("pr head branch", pr.get("headRefName"))
        v = gh(["pr", "view", str(pr["number"]), "-R", SLUG, "--json", "body,comments,reviews"])
        d = v["data"] or {}
        scr("pr body", d.get("body"))
        for c in d.get("comments") or []:
            scr("pr comment", c.get("body"))
            author_of(c)
        for c in d.get("reviews") or []:
            scr("pr review", c.get("body"))
            author_of(c)
        pr_detail.append({"number": pr["number"], "state": pr.get("state"), "author": author_of(pr),
                          "comments": len(d.get("comments") or []), "reviews": len(d.get("reviews") or []),
                          "view_rc": v["rc"]})
    S["pull_requests"] = {"rc": G["pr_list"]["rc"], "count": len(prs),
                          "by_state": dict(collections.Counter(p.get("state") for p in prs)),
                          "authors": dict(collections.Counter(p["author"] for p in pr_detail)), "detail": pr_detail}
    iss = G["issue_list"]["data"] if isinstance(G["issue_list"]["data"], list) else []
    iss_detail = []
    for it in iss:
        scr("issue title", it.get("title"))
        v = gh(["issue", "view", str(it["number"]), "-R", SLUG, "--json", "body,comments"])
        d = v["data"] or {}
        scr("issue body", d.get("body"))
        for c in d.get("comments") or []:
            scr("issue comment", c.get("body"))
            author_of(c)
        iss_detail.append({"number": it["number"], "state": it.get("state"), "author": author_of(it),
                           "comments": len(d.get("comments") or []), "view_rc": v["rc"]})
    S["issues"] = {"rc": G["issue_list"]["rc"], "count": len(iss),
                   "by_state": dict(collections.Counter(i.get("state") for i in iss)),
                   "authors": dict(collections.Counter(i["author"] for i in iss_detail)), "detail": iss_detail}
    for key, lab in (("issue_comments", "issue/PR comment (api)"), ("review_comments", "review comment (api)"),
                     ("commit_comments", "commit comment (api)")):
        items = flat_pages(G[key]["data"])
        for c in items:
            scr(lab, c.get("body"))
            author_of(c)
        S[key] = {"rc": G[key]["rc"], "count": len(items)}
    rels = G["release_list"]["data"] if isinstance(G["release_list"]["data"], list) else []
    rel_detail = []
    for r in rels:
        scr("release name", r.get("name"))
        v = gh(["release", "view", r["tagName"], "-R", SLUG, "--json", "body,assets"])
        d = v["data"] or {}
        scr("release body", d.get("body"))
        assets = d.get("assets") or []
        for x in assets:
            scr("release asset name", x.get("name"))
        rel_detail.append({"tag": r.get("tagName"), "draft": r.get("isDraft"), "assets": len(assets),
                           "asset_bytes": sum(int(x.get("size") or 0) for x in assets)})
    S["releases"] = {"rc": G["release_list"]["rc"], "count": len(rels), "detail": rel_detail}
    runs = G["run_list"]["data"] if isinstance(G["run_list"]["data"], list) else []
    for r in runs:
        scr("run title", r.get("displayTitle"))
        scr("run branch", r.get("headBranch"))
    wf = G["workflows"]["data"] or {}
    for x in wf.get("workflows") or []:
        scr("workflow name", x.get("name"))
    ar = G["artifacts"]["data"] or {}
    for x in ar.get("artifacts") or []:
        scr("artifact name", x.get("name"))
    S["actions"] = {"runs_rc": G["run_list"]["rc"], "runs": len(runs),
                    "runs_by_status": dict(collections.Counter(r.get("status") for r in runs)),
                    "runs_by_event": dict(collections.Counter(r.get("event") for r in runs)),
                    "workflows_total": wf.get("total_count"),
                    "workflow_names_sha8": sorted(sha8(x.get("name") or "") for x in wf.get("workflows") or []),
                    "artifacts_total": ar.get("total_count"),
                    "artifact_names_sha8": sorted(sha8(x.get("name") or "") for x in ar.get("artifacts") or []),
                    "workflow_files_at_HEAD": len([p for p in git("ls-tree", "-r", "--name-only", "HEAD", "--",
                                                                   ".github").split("\n") if p.strip()])}
    S["wiki"] = {"hasWikiEnabled": rv.get("hasWikiEnabled"), **wiki}
    S["pages"] = {"rc": G["pages"]["rc"], "status": G["pages"]["status"],
                  "site": None if G["pages"]["status"] == "404" else (G["pages"]["data"] or {}).get("status")}
    for key in ("deploy_keys", "hooks"):
        d = G[key]["data"]
        S[key] = {"rc": G[key]["rc"], "status": G[key]["status"],
                  "count": len(d) if isinstance(d, list) else None}
    ms = flat_pages(G["milestones"]["data"])
    for x in ms:
        scr("milestone title", x.get("title"))
        scr("milestone description", x.get("description"))
    S["milestones"] = {"rc": G["milestones"]["rc"], "count": len(ms)}
    gq = ((G["graphql_counts"]["data"] or {}).get("data") or {}).get("repository") or {}
    S["graphql"] = {"rc": G["graphql_counts"]["rc"],
                    "discussions": (gq.get("discussions") or {}).get("totalCount"),
                    "deployments": (gq.get("deployments") or {}).get("totalCount"),
                    "environments": (gq.get("environments") or {}).get("totalCount"),
                    "projects_v2_rc": G["graphql_projects_v2"]["rc"],
                    "projects_v2_error_type": G["graphql_projects_v2"]["graphql_error_type"],
                    "projects_v2": (((G["graphql_projects_v2"]["data"] or {}).get("data") or {}).get("repository")
                                    or {}).get("projectsV2", {}).get("totalCount")
                    if not G["graphql_projects_v2"]["graphql_error_type"] else None}
    # activity record (Code's addition): pushes / force pushes / branch creations and deletions
    act = flat_pages(G["activity"]["data"])
    zero = "0" * 40
    types = collections.Counter(x.get("activity_type") for x in act)
    by_ref = collections.Counter(x.get("ref") for x in act)
    actors = collections.Counter(author_of(x) for x in act)
    for x in act:
        scr("activity ref", x.get("ref"))
    for name in sorted(server):
        scr("server ref name", name)
    a_rows = []
    for x in act:
        ref = x.get("ref") or ""
        tip = server.get(ref)
        bef, aft = x.get("before") or zero, x.get("after") or zero
        bl = obj_local(bef) if bef != zero else None
        al = obj_local(aft) if aft != zero else None
        ff = is_ancestor(bef, aft) if (bl and al) else None
        reach = is_ancestor(aft, tip) if (al and tip) else None
        a_rows.append({"type": x.get("activity_type"), "ref": ref, "before": bef[:10], "after": aft[:10],
                       "ts": x.get("timestamp"), "before_local": bl, "after_local": al, "fast_forward": ff,
                       "after_reachable_from_server_tip": reach})
    ts = sorted(r["ts"] for r in a_rows if r["ts"])

    def reflog(path):
        p = os.path.join(REPO, ".git", "logs", path)
        rows = []
        if os.path.isfile(p):
            for ln in open(p, encoding="utf-8", errors="replace"):
                left, _, msg = ln.rstrip("\n").partition("\t")
                f = left.split(" ")
                rows.append({"old": f[0], "new": f[1], "kind": msg.split(":")[0].strip()})
        return rows
    rl = {}
    for ref in sorted(by_ref):
        if not ref.startswith("refs/heads/"):
            continue
        rows = reflog("refs/remotes/origin/" + ref[len("refs/heads/"):])
        act_after = {r["after"] for r in a_rows if r["ref"] == ref and r["type"] in ("push", "force_push",
                                                                                    "branch_creation")}
        rl_new = {r["new"][:10] for r in rows}
        rl[ref] = {"reflog_entries": len(rows), "reflog_kinds": dict(collections.Counter(r["kind"] for r in rows)),
                   "activity_entries": by_ref[ref], "activity_afters": len(act_after),
                   "afters_in_reflog": len(act_after & rl_new), "afters_not_in_reflog": len(act_after - rl_new),
                   "reflog_values_not_in_activity": len(rl_new - act_after)}
    pushes = [r for r in a_rows if r["type"] in ("push", "force_push")]
    S["activity"] = {"rc": G["activity"]["rc"], "records": len(act), "by_type": dict(types),
                     "by_ref": dict(by_ref), "actors": dict(actors), "earliest": ts[0] if ts else None,
                     "latest": ts[-1] if ts else None,
                     "force_push": types.get("force_push", 0), "branch_deletion": types.get("branch_deletion", 0),
                     "pushes": len(pushes),
                     "pushes_both_local": sum(1 for r in pushes if r["before_local"] and r["after_local"]),
                     "pushes_fast_forward": sum(1 for r in pushes if r["fast_forward"] is True),
                     "pushes_not_fast_forward": sum(1 for r in pushes if r["fast_forward"] is False),
                     "afters_not_local": sum(1 for r in a_rows if r["after_local"] is False),
                     "afters_reachable_from_server_tip": sum(1 for r in a_rows
                                                            if r["after_reachable_from_server_tip"] is True),
                     "afters_checked": sum(1 for r in a_rows if r["after_reachable_from_server_tip"] is not None),
                     "reflog_compare": rl, "first_push_local_reflog": hj["reflogs"]["first_push"]["time"],
                     "earliest_equals_first_push": (
                         ts and datetime.datetime.fromisoformat(ts[0].replace("Z", "+00:00")) ==
                         datetime.datetime.strptime(hj["reflogs"]["first_push"]["time"], "%Y-%m-%d %H:%M:%S %z"))}
    S["screen"] = {"texts_screened": dict(screened), "hits": {f"{k[0]} / {k[1]}": n for k, n in screen_hits.items()},
                   "non_owner_logins": dict(others_logins)}
    J["github"] = {"queries": [{k: v for k, v in q.items() if k != "data"} for q in G.values()], "surfaces": S}

    # ======================================================== (3) interim history scan
    H = collections.OrderedDict()
    md_out = os.path.join(hist_dir, "history_now.md")
    js_out = os.path.join(hist_dir, "history_now.json")
    for p_ in (md_out, js_out):
        if os.path.exists(p_):
            os.remove(p_)
    hb, _ = snapshot()
    t1 = time.time()
    pr_ = run([sys.executable, HIST_SCRIPT, "--out", md_out, "--json-out", js_out],
              env_extra={"PYTHONHASHSEED": HASHSEED})
    ha, _ = snapshot()
    err = pr_.stderr.decode("utf-8", "replace")
    refusal = re.search(r"REFUSING TO WRITE: (\d+) redacted value\(s\) appear verbatim", err)
    refused_forms = re.findall(r"\('(md|json)', '([^']{1,4}\.\.\.\[len \d+\]#[0-9a-f]{8})'", err)
    H["routed_run"] = {"cmd": f"PYTHONHASHSEED={HASHSEED} {os.path.relpath(sys.executable, REPO)} {HIST_SCRIPT} "
                              f"--out <history-dir>/history_now.md --json-out <history-dir>/history_now.json",
                       "rc": pr_.returncode, "secs": round(time.time() - t1, 1), "head_before": hb,
                       "head_after": ha, "md_written": os.path.isfile(md_out), "json_written": os.path.isfile(js_out),
                       "refused": bool(refusal), "refused_count": int(refusal.group(1)) if refusal else None,
                       "refusal_forms_printed": [{"output": o, "form": f} for o, f in refused_forms],
                       "stderr_lines": len(err.splitlines())}

    # the full leak list: the same unchanged script, in-process, same arguments; its own `leaks` list read from
    # its frame when its leak assertion raises (values held in memory only; forms printed)
    hb3, _ = snapshot()
    t1 = time.time()
    h2 = load_module("n12_history_inprocess", HIST_SCRIPT)
    saved_argv, saved_env = list(sys.argv), dict(os.environ)
    leaks_full, ip_outcome, ip_msg_count = None, None, None
    try:
        sys.argv = [os.path.join(REPO, HIST_SCRIPT), "--out", md_out, "--json-out", js_out]
        os.environ.update(RUN_ENV)
        try:
            h2.main()
            ip_outcome = "returned (no refusal)"
            leaks_full = []
        except SystemExit as e_:
            msg_ = str(e_.code)
            m_ = re.match(r"REFUSING TO WRITE: (\d+) redacted value\(s\) appear verbatim", msg_)
            ip_outcome = "refused" if m_ else "exited for another reason"
            ip_msg_count = int(m_.group(1)) if m_ else None
            tb_ = e_.__traceback__
            while tb_ is not None:
                if tb_.tb_frame.f_code is h2.main.__code__:
                    leaks_full = [(x[0], x[1]) for x in (tb_.tb_frame.f_locals.get("leaks") or [])]
                    break
                tb_ = tb_.tb_next
            del tb_
    finally:
        sys.argv = saved_argv
        os.environ.clear()
        os.environ.update(saved_env)
    ha3, _ = snapshot()
    form_to_val = {f"{v[:4]}...[len {len(v)}]#{sha8(v)}": v for v in h2.REDACTED_SENSITIVE}
    ip_secs = round(time.time() - t1, 1)
    del h2
    if leaks_full is None:
        raise SystemExit("the in-process run's leak list could not be read; nothing written")
    if any(f not in form_to_val for _, f in leaks_full):
        raise SystemExit("an in-process leak form does not map to a redacted value; nothing written")
    leak_vals = {}
    for o_, f_ in leaks_full:
        leak_vals.setdefault(form_to_val[f_], set()).add(o_)
    del form_to_val
    rr_count = H["routed_run"]["refused_count"]
    H["full_leak_list"] = {
        "method": "the same unchanged script run in-process with the routed arguments; its SystemExit caught and "
                  "its own `leaks` list (one entry per value and output) read from its frame",
        "outcome": ip_outcome, "message_count": ip_msg_count, "entries": len(leaks_full),
        "distinct_values": len(leak_vals), "secs": ip_secs, "head_before": hb3, "head_after": ha3,
        "entries_equal_routed_count": (len(leaks_full) == rr_count) if rr_count is not None else None,
        "routed_sample_contained": all((x["output"], x["form"]) in set(leaks_full)
                                       for x in H["routed_run"]["refusal_forms_printed"])}
    hb2, _ = snapshot()
    t1 = time.time()
    pd = run([sys.executable, HIST_SCRIPT, "--dump-untriaged", "--dump-all", "--out", md_out, "--json-out", js_out],
             env_extra={"PYTHONHASHSEED": HASHSEED})
    ha2, _ = snapshot()
    rows, shapes, other_lines, dump_only = [], [], 0, False
    for ln in pd.stdout.decode("utf-8", "replace").splitlines():
        parts = ln.split("\t")
        if len(parts) == 7:
            lab, vk, tri, nocc, first, vr, _ctx = parts
            v = ast.literal_eval(vr)
            rows.append({"table": lab, "vkey": vk, "verdict": tri, "n_occ": int(nocc), "first": first, "v": v})
        elif ln.startswith("shape "):
            shapes.append(ast.literal_eval(ln[6:]))
        elif ln.strip() == "DUMP ONLY: no file written":
            dump_only = True
        else:
            other_lines += 1
    H["dump_run"] = {"cmd": f"PYTHONHASHSEED={HASHSEED} {os.path.relpath(sys.executable, REPO)} {HIST_SCRIPT} "
                            f"--dump-untriaged --dump-all (stdout held in memory; no file written)",
                     "rc": pd.returncode, "secs": round(time.time() - t1, 1), "head_before": hb2, "head_after": ha2,
                     "dump_only_line": dump_only, "rows": len(rows), "shape_rows": len(shapes),
                     "unparsed_lines": other_lines,
                     "files_written": [p_ for p_ in (md_out, js_out) if os.path.isfile(p_) and
                                       os.path.getmtime(p_) >= t1]}
    if pd.returncode != 0 or not dump_only:
        raise SystemExit("the history script's dump run did not complete; nothing written")
    for r in rows:
        if sha8(r["v"]) != r["vkey"]:
            raise SystemExit("dump row key mismatch")

    def tab_of(lab):
        if lab.startswith("id:"):
            return short(lab[3:])
        if ":" in lab:
            pre_, nm_ = lab.split(":", 1)
            return pre_ + ":" + short(nm_)
        return lab

    def k_of(v):
        m = re.search(r"#([0-9a-f]{8})$", v) or re.fullmatch(r"len\d+:([0-9a-f]{8})", v)
        return m.group(1) if m else sha8(v)
    old = collections.defaultdict(dict)   # table -> sha8 -> entry
    for n, lst in hj["precise"].items():
        for e in lst:
            old["precise:" + short(n)][k_of(e["value"])] = e
    for e in hj["high_entropy"]["values"]:
        old["high_entropy"][k_of(e["value"])] = e
    for e in hj["context_free_high_entropy"]["values"]:
        old["context_free"][k_of(e["value"])] = e
    for e in hj["headers"]["context_free_high_entropy"]:
        old["header_context_free"][k_of(e["value"])] = e
    for e in hj["binary_content"]["context_free_high_entropy"]:
        old["binary_context_free"][k_of(e["value"])] = e
    for n, lst in hj["headers"]["precise"].items():
        for e in lst:
            old["header_precise:" + short(n)][k_of(e["value"])] = e
    for n, lst in hj["binary_content"]["precise"].items():
        for e in lst:
            old["binary_precise:" + short(n)][k_of(e["value"])] = e
    for n, lst in hj["identifiers"].items():
        for e in lst:
            old[short(n)][k_of(e["value"])] = e
    now = collections.defaultdict(dict)
    for r in rows:
        now[tab_of(r["table"])][r["vkey"]] = r
    tables = sorted(set(old) | set(now))
    per_table = []
    for t in tables:
        o, n_ = set(old.get(t, {})), set(now.get(t, {}))
        if o or n_:
            per_table.append({"table": t, "committed": len(o), "now": len(n_), "new": len(n_ - o),
                              "gone": len(o - n_)})
    new_rows = [r for t in tables for k, r in now.get(t, {}).items() if k not in old.get(t, {})]
    gone_total = sum(x["gone"] for x in per_table)
    win = git("rev-list", "--reverse", "--topo-order", "HEAD", "--not", base).split()
    win_all = git("rev-list", "--all", "--not", base).split()
    win8 = {c[:8]: c for c in win}
    committed_ref_shas = sorted({r[1] for r in hj["refs"]})
    after_rec_scan = git("rev-list", "--reverse", "--topo-order", "--all", "--not", *committed_ref_shas).split()
    for r in new_rows:
        r["first_commit"] = r["first"].split(" ")[0][:8]
        r["first_path"] = r["first"].split(" ", 1)[1].rsplit(":", 1)[0] if " " in r["first"] else r["first"]
        r["tab"] = tab_of(r["table"])
        ct = CODE_TRIAGE.get((r["tab"], r["vkey"]))
        if r["verdict"] == "UNTRIAGED" and ct and ct[2] == r["first_path"]:
            r["code_verdict"], r["code_reason"] = ct[0], ct[1]
        elif r["verdict"] == "UNTRIAGED":
            r["code_verdict"], r["code_reason"] = "UNTRIAGED", "not triaged by Code in this raw"
        else:
            r["code_verdict"], r["code_reason"] = r["verdict"], "the history script's own triage"
    already = collections.Counter()
    for t in tables:
        for k, e in old.get(t, {}).items():
            c8 = (e.get("first") or "?")[:8]
            if c8 in win8:
                already[(win8[c8][:10], t, e["triage"][0])] += 1
    # shapes
    n13_lines = {}
    shape_rows = []
    for s in shapes:
        c8, loc = s["locator"].split(" ", 1)
        path, ln = loc.rsplit(":", 1)
        lno = int(re.sub(r"\D", "", ln) or 0)
        fk = k_of(s["value"])
        verdict, reason = "UNTRIAGED", "not triaged by Code in this raw"
        if s.get("verdict") != "UNTRIAGED":
            verdict, reason = s.get("verdict"), "the history script's own triage"
        elif path == N13_JSON and s["key"] == N13_KEY:
            key = (c8, path)
            if key not in n13_lines:
                full = git("rev-parse", "--verify", c8 + "^{commit}").strip()
                n13_lines[key] = git("show", f"{full}:{path}").split("\n")
            L = n13_lines[key]
            m1 = KV_HEX_RE.search(L[lno - 1]) if 0 < lno <= len(L) else None
            m2 = KV_HEX_RE.search(L[lno]) if 0 < lno < len(L) else None
            if m1 and m2 and m1.group(1) == N13_KEY and m2.group(1) == "full" and \
                    len(m2.group(2)) in (40, 64) and m2.group(2).startswith(m1.group(2)) and \
                    len(m1.group(2)) in (7, 8) and sha8(m1.group(2)) == fk:
                kind = "commit id" if len(m2.group(2)) == 40 else "sha256"
                verdict, reason = "FALSE-POSITIVE", f"an abbreviated hash in N13's provenance JSON; the next line holds its full form (a {kind})"
        elif (path, lno) in SHAPE_TRIAGE and SHAPE_TRIAGE[(path, lno)][0] == fk:
            verdict, reason = "FALSE-POSITIVE", SHAPE_TRIAGE[(path, lno)][1]
        shape_rows.append({"commit": c8, "path": path, "line": lno, "key": s["key"], "op": s["op"],
                           "value_form": s["value"] if re.search(r"#[0-9a-f]{8}$", s["value"]) else "(short; shown by the history script)",
                           "script_verdict": s.get("verdict"), "code_verdict": verdict, "reason": reason})
    shape_unt = [r for r in shape_rows if r["code_verdict"] == "UNTRIAGED"]
    new_unt = [r for r in new_rows if r["code_verdict"] == "UNTRIAGED"]
    script_unt = [r for r in new_rows if r["verdict"] == "UNTRIAGED"]
    true_new = [r for r in new_rows if r["verdict"] == "TRUE-SECRET-CANDIDATE"]
    true_all = [r for r in rows if r["verdict"] == "TRUE-SECRET-CANDIDATE"]
    id_short = {short(c) for c in h.ID_PATTERNS}
    if not set(REDACTION_CLASSES) | set(REDACTION_EXCLUDED) == id_short or set(REDACTION_CLASSES) & set(REDACTION_EXCLUDED):
        raise SystemExit("the redaction-class partition does not cover the history script's identifier classes; "
                         "nothing written")
    new_red = [r for r in new_rows if r["tab"] in REDACTION_CLASSES]
    new_red_open = [r for r in new_red if r["code_verdict"] not in PUBLIC_VERDICTS | {"METADATA-ECHO"}]
    new_red_by = collections.Counter((r["tab"], r["code_verdict"]) for r in new_red)
    # the count under the set this file's first version used (for the values-check disposition)
    red_v1 = {"runpod_pod_id", "runpod_volume_id", "runpod_volume_name", "container_hostname", "ssh_port",
              "ssh_fingerprint", "ssh_public_key", "claude_session_or_artifact_link", "passphrase_shaped",
              "ipv4_address", "ipv6_address", "dot_local_hostname", "runpod_ssh_gateway_user", "cloud_account_id",
              "email_address"}
    new_red_v1 = sum(1 for r in new_rows if r["tab"] in red_v1)

    # fallback grep at HEAD (the block's command, as the history script runs it)
    t1 = time.time()
    logp = git("log", "-p", "--all", binary=True)
    gp = run(["/usr/bin/grep", "-nEi", h.FALLBACK_PATTERN], input=logp)
    if gp.returncode not in (0, 1):
        raise SystemExit("fallback grep failed")
    hit_lines = len([x for x in gp.stdout.split(b"\n") if x])
    alt_rx = [(n, re.compile(rx, re.I)) for n, rx in h.FALLBACK_ALTS]
    per_alt = collections.Counter()
    per_commit = collections.Counter()
    py_lines = 0
    pat = re.compile(h.FALLBACK_PATTERN, re.I)
    logp_lines = logp.split(b"\n")
    loc = h.index_log(logp_lines)   # the history script's own locator: (commit, path, side, line)
    after_set = set(after_rec_scan)
    new_bulk = collections.Counter()
    inspect = []
    for i, raw in enumerate(logp_lines):
        t_ = raw.decode("utf-8", "replace")
        if not pat.search(t_):
            continue
        py_lines += 1
        c_, path_, side_, fln_ = loc[i] or (None, "?", "?", None)
        per_commit[c_] += 1
        for n, rx in alt_rx:
            ms_ = list(rx.finditer(t_))
            if ms_:
                per_alt[n] += 1
            if c_ not in after_set:
                continue
            for mt in ms_:
                wd = h.fallback_word(t_, mt.start(), mt.end())
                we = mt.end()
                while we < len(t_) and (t_[we].isalnum() or t_[we] in "_-"):
                    we += 1
                rule, _why = h.fallback_bulk_rule(n, wd, path_ or "", t_[we:we + 4])
                new_bulk[(n, rule)] += 1
                if rule.startswith(INSPECT_RULES):
                    inspect.append((c_[:8], path_ or "?", side_, str(fln_), n, rule.split(" ")[0], wd.lower()))
    del logp_lines, loc
    inspect_sha = sha256_hex("\n".join("\t".join(x) for x in sorted(inspect)))
    audit_file = re.compile(r"^(?:scripts/audit_note_[\w-]+\.py|results/raw/2026-10-08_note-[\w.-]+|README-NOTE\.md)$")
    inspect_files = collections.Counter((x[5], x[1]) for x in inspect)
    n12_file = re.compile(r"^(?:scripts/audit_note_N12_\w+\.py|results/raw/2026-10-08_note-N12-[\w.-]+)$")
    non_n12 = collections.defaultdict(lambda: [0, set()])   # path -> [hits, distinct lines]
    for x in inspect:
        if not n12_file.match(x[1]):
            non_n12[x[1]][0] += 1
            non_n12[x[1]][1].add((x[0], x[3]))
    fb_secs = round(time.time() - t1, 1)
    committed_fb = hj["fallback"]["hit_lines"]
    delta_commits = {c[:10]: per_commit.get(c, 0) for c in after_rec_scan}
    fb = {"cmd": "git log -p --all | /usr/bin/grep -nEi '<the block's pattern, :77>'", "hit_lines": hit_lines,
          "python_crosscheck_lines": py_lines, "committed": committed_fb, "delta": hit_lines - committed_fb,
          "delta_from_commits_after_the_committed_scan": sum(delta_commits.values()),
          "per_commit_in_window": {c[:10]: per_commit.get(c, 0) for c in win},
          "per_alternative_now": {n: per_alt.get(n, 0) for n, _ in h.FALLBACK_ALTS},
          "per_alternative_committed": {n: hj["fallback"]["per_alternative"][n]["lines"] for n, _ in h.FALLBACK_ALTS},
          "logp_bytes": len(logp), "secs": fb_secs,
          "new_hits_by_rule": [{"alternative": k[0], "rule": k[1], "occurrences": n} for k, n in sorted(new_bulk.items())],
          "inspection_rule_hits": len(inspect), "inspection_rule_hits_sha256": inspect_sha,
          "inspection_rule_lines": len({(x[0], x[1], x[3]) for x in inspect}),
          "inspection_rule_hits_read_by_code": inspect_sha == INSPECTED_SHA,
          "inspection_rule_files": [{"rule": k[0], "path": k[1], "n": n} for k, n in sorted(inspect_files.items())],
          "inspection_rule_hits_outside_audit_files": sum(1 for x in inspect if not audit_file.match(x[1])),
          "inspection_rule_hits_outside_n12_files": {p: {"hits": v[0], "lines": len(v[1])}
                                                     for p, v in sorted(non_n12.items())}}
    del logp

    # blobs new since base, sizes; HEAD files over 40 MB
    objs = git("rev-list", "--objects", "--all", "--not", base).split("\n")
    o_paths = {}
    for ln in objs:
        if ln.strip():
            p = ln.split(" ", 1)
            o_paths[p[0]] = p[1] if len(p) > 1 else ""
    bc = run(["git", "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)"],
             input=("\n".join(o_paths) + "\n").encode()).stdout.decode().split("\n")
    nb = []
    for ln in bc:
        f = ln.split()
        if len(f) == 3 and f[1] == "blob":
            nb.append((int(f[2]), f[0], o_paths.get(f[0], "")))
    nb.sort(reverse=True)
    head_big = []
    for ln in git("ls-tree", "-r", "-l", "HEAD").split("\n"):
        m = re.match(r"\d+ blob ([0-9a-f]{40})\s+(\d+)\t(.*)$", ln)
        if m and int(m.group(2)) > 40 * 10 ** 6:
            head_big.append({"path": m.group(3), "size": int(m.group(2))})
    committed_big = {x["path"]: x["size"] for x in hj["head_files_over_40MB"]}
    blobs = {"new_blobs_since_base": len(nb), "largest_new": [{"size": s, "blob": b[:10], "path": p}
                                                            for s, b, p in nb[:5]],
             "new_over_1MB": sum(1 for s, _, _ in nb if s > 10 ** 6),
             "new_over_40MB": sum(1 for s, _, _ in nb if s > 40 * 10 ** 6),
             "new_over_50MB": sum(1 for s, _, _ in nb if s > 50 * 10 ** 6),
             "new_over_100MB": sum(1 for s, _, _ in nb if s > 100 * 10 ** 6),
             "committed_max_blob": hj["max_blob_bytes"],
             "head_files_over_40MB": head_big,
             "head_files_over_40MB_equal_committed": {x["path"]: x["size"] for x in head_big} == committed_big}

    # known sensitive values in what each window commit added; identities of window commits
    kv_rows = []
    id_rows = []
    sess_re = h.ID_RE["claude_session_or_artifact_link"]
    for c in win:
        msg = git("log", "-1", "--format=%B", c)
        added = []
        for ln in git("diff-tree", "-r", "--root", "--no-commit-id", "--no-renames", "--no-abbrev", c).split("\n"):
            m = re.match(r":\d+ \d+ ([0-9a-f]{40}) ([0-9a-f]{40}) ([AMT])\t(.*)$", ln)
            if m:
                added.append((m.group(1), m.group(2), m.group(4)))
        cnt = collections.Counter()      # occurrences in the new blob
        net = collections.Counter()      # new blob minus the parent's blob at the same path
        files_hit = collections.Counter()
        zero40 = "0" * 40
        for ob, b, p in added:
            data = git("cat-file", "-p", b, binary=True).decode("utf-8", "replace")
            odata = git("cat-file", "-p", ob, binary=True).decode("utf-8", "replace") if ob != zero40 else ""
            for f, v in known.items():
                n = scrub.count_value(f, v, data)
                if n:
                    cnt[known_label[f]] += n
                    d_ = n - (scrub.count_value(f, v, odata) if odata else 0)
                    if d_:
                        net[known_label[f]] += d_
                        files_hit[p] += 1
        for f, v in known.items():
            n = scrub.count_value(f, v, msg)
            if n:
                cnt["(message) " + known_label[f]] += n
                net["(message) " + known_label[f]] += n
        kv_rows.append({"commit": c[:10], "blobs_added_or_modified": len(added), "occurrences_in_new_blobs": dict(cnt),
                        "net_new": dict(net), "files_with_net_new": sorted(files_hit)})
        hdr = git("cat-file", "-p", c)
        ae = git("log", "-1", "--format=%ae%n%ce", c).split("\n")
        id_rows.append({"commit": c[:10], "author_committer_known_identity": all(
            (x in identity_vals or x in h.PENDING_EMAIL_EXEMPT) for x in ae if x),
            "author_committer_forms": sorted({("the service address" if x in h.PENDING_EMAIL_EXEMPT else
                                               form(x)) for x in ae if x}),
            "gpgsig": "\ngpgsig " in hdr, "session_link_in_message": bool(sess_re.search(msg)),
            "subject_sha8": sha8(msg.split("\n")[0])})
    H.update({"head_scanned": ha2 if hb2 == ha2 else None, "committed_json": {"commit": rec, "head": hj["head"],
              "script_sha256": hj["script_sha256"]},
              "window_base": base, "window_commits": [c[:10] for c in win], "window_commits_all_refs": len(win_all),
              "commits_after_committed_scan": [c[:10] for c in after_rec_scan],
              "per_table": per_table, "new_values": len(new_rows), "gone_values": gone_total,
              "new_by_table_verdict": [{"table": k[0], "verdict": k[1], "first_commit": k[2], "n": n} for k, n in
                                       sorted(collections.Counter((r["tab"], r["code_verdict"], r["first_commit"])
                                                                  for r in new_rows).items())],
              "new_first_commit": dict(collections.Counter(r["first_commit"] for r in new_rows)),
              "already_recorded_in_window": [{"commit": k[0], "table": k[1], "verdict": k[2], "n": n}
                                             for k, n in sorted(already.items())],
              "true_secret_candidates_now": len(true_all), "true_secret_candidates_new": len(true_new),
              "script_untriaged_new": len(script_unt), "code_untriaged_new": len(new_unt),
              "shape_rows_script_untriaged": sum(1 for r in shape_rows if r["script_verdict"] == "UNTRIAGED"),
              "shape_rows_code_untriaged": len(shape_unt),
              "redaction_classes": list(REDACTION_CLASSES), "identifier_classes_outside_it": list(REDACTION_EXCLUDED),
              "new_redaction_class_values": len(new_red), "new_redaction_class_values_open": len(new_red_open),
              "new_redaction_class_values_by_class_verdict": [{"table": k[0], "verdict": k[1], "n": n}
                                                              for k, n in sorted(new_red_by.items())],
              "new_redaction_class_values_first_version_set": new_red_v1,
              "fallback": fb, "blobs": blobs, "known_values_in_window": kv_rows, "window_identities": id_rows})
    J["history"] = H

    # ======================================================== write the md
    out = []
    w = out.append
    head1, refs1 = snapshot()
    moved = head1 != head0 or refs1 != refs0
    w("# AUDIT-note-release v1.2 -- N12 pre-flip reads (server refs, GitHub-side surfaces, interim history scan)")
    w("")
    w(f"- Code stamp (`date -u`): {stamp}")
    w(f"- HEAD at start `{head0}`; at the end `{head1}`; refs moved during the run: {'yes' if moved else 'no'}.")
    w(f"- Block: `{BLOCK}`, sha256 `{block_wt}` (working tree) / `{block_head}` (HEAD blob); routed "
      f"`{BLOCK_SHA[:8]}...{BLOCK_SHA[-4:]}`: {'MATCH' if block_wt == BLOCK_SHA == block_head else 'MISMATCH'}.")
    w(f"- Item: N12, the scrub index's pre-flip checklist (`{SCRUB_MD}@{rec[:7]}:{locate(smd, lambda s: s.startswith('## 10.'))}"
      f"-{locate(smd, lambda s: s.startswith('5. Also carried'))}`), items 1 and 2, and an interim run of item 3's history "
      f"script. Compared against the committed history raw and JSON at `{rec[:7]}` (`{rec}`), whose scan read "
      f"`{hj['head'][:10]}`.")
    w(f"- Script: `{me_rel}`, sha256 `{me_sha}`. Interpreter: `{interp}` (Python {py}); {git_ver}; {gh_ver}. "
      f"Command: `{interp} {me_rel} --history-dir <a directory outside the repository>` (from the repository root).")
    w("- Read-only: `git ls-remote` (origin and the wiki repository), `rev-parse`, `for-each-ref`, `cat-file`, "
      "`merge-base --is-ancestor`, `rev-list`, `log`, `show`, `diff-tree`, `ls-tree`, `remote get-url`; `gh` read "
      "queries only (`repo view`, `pr list`, `issue list`, `release list`, `run list`, `api` GETs, two GraphQL queries). "
      "Nothing fetched, staged, committed, pushed or tagged; no setting changed; nothing downloaded or installed; no "
      "git command inside `jlens-qwen36/`. The remote-tracking reflogs are read as plain files (their name and email "
      "fields are never read out). Network: GitHub only, through `git` and `gh`.")
    w("- Writes: this file and its JSON. The history script, run unchanged (twice as a subprocess, once in-process to "
      "read its full leak list; section 3), wrote (or would have written) only into session scratch outside the "
      "repository (the path is not printed: it is of the local-temp-path class). For the in-process run the "
      "process's argument list and environment are set to the routed run's (apart from the hash seed, which a "
      "running process cannot change; the list it yields is sorted here) and restored afterwards.")
    w(f"- Redaction: no RunPod id or name, IP address, SSH port, key name, credential, the LoRA phrase, the session "
      f"link, the laptop hostname, an email address or a non-owner login appears in this file or its JSON. The "
      f"history raw's {len(kv)} known sensitive values were resolved in memory ({len(known)} resolved, "
      f"{len(unresolved)} unresolved: the class{'es' if len(unresolved) != 1 else ''} "
      f"{', '.join(known_label[f] for f in unresolved) or '-'}, which the history raw says is not verbatim in "
      f"history) and the dumped values held in memory; the script refuses to write if any of them, or any guard "
      f"shape, occurs in an output. Redacted forms use the history raw's notation `xxxx...[len N]#hhhhhhhh` (the "
      f"routing's first 4 + length + sha256 prefix; `lenN:hhhhhhhh` where a value has 4 characters or fewer or opens with 4 digits). Class "
      f"names are printed by their short label (several long labels contain strings the scan reports as values).")
    w("")

    # ---- (1)
    w("## 1. Server-side refs (`git ls-remote --symref origin`)")
    w("")
    w(f"Origin: `{url_shown}` (userinfo in the URL: {'yes' if url_userinfo else 'no'}). ls-remote returned "
      f"{len(server)} refs ({len(peeled)} peeled tag line(s) besides) in {lr_secs} s. HEAD is a symref to "
      f"`{symrefs.get('HEAD')}`.")
    w("")
    w(f"Compared with the history raw's refs table (`{HIST_MD}@{rec[:7]}:{hist_tab_start}-{hist_tab_end}`, the "
      f"local refs at its scan of `{hj['head'][:10]}`) and with the local refs now:")
    w("")
    w("| server ref | object | object local | local counterpart(s), equal | in the history raw's table (object there; equal now) | ancestor of origin/main |")
    w("|---|---|---|---|---|---|")
    for r in srows:
        lc = ", ".join(f"`{c}` {'yes' if e else 'NO'}" for c, e in r["local_counterparts"].items()) or "none"
        ht = ", ".join(f"`{c}` (`{x['object_there']}`; {'yes' if x['equal_now'] else 'no -- moved'})"
                       for c, x in r["in_history_raw_table"].items()) or "-"
        anc = ("n/a (symref)" if r["ref"] == "HEAD" else
               "object not local; not fetched" if not r["object_local"] else
               {True: "yes", False: "NO", None: "?"}[r["ancestor_of_origin_main"]])
        pe = f" (peels to `{r['peeled'][:10]}`)" if r["peeled"] else ""
        w(f"| `{r['ref']}` | `{r['object'][:10]}`{pe} | {'yes' if r['object_local'] else 'no'} | {lc} | {ht} | {anc} |")
    w("")
    w(f"- Server refs with no local counterpart: {len(server_not_local)}{(' -- ' + ', '.join(server_not_local)) if server_not_local else ''}. "
      f"Server objects not in the local object store: {len(obj_missing)}. `refs/pull/*`: {len(pulls)}. Refs outside "
      f"heads/tags/pull: {len(others)}. Local refs with no server ref: {len(local_not_server)}"
      f"{(' (' + ', '.join(local_not_server) + ')') if local_not_server else ''}.")
    w(f"- Peeled tag objects equal the local peel: {all(peel_check.values()) if peel_check else 'n/a'} "
      f"({len(peel_check)} tag(s)).")
    w(f"- Since the history raw's table: " + ("; ".join(f"`{c}` `{x[0]}` -> `{x[1]}`" for c, x in moved_since_hist.items())
                                             or "no local ref moved") +
      f". The commits that `main` gained ({len(after_rec_scan)}: "
      f"{', '.join('`' + c[:10] + '`' for c in after_rec_scan)}) are outside that scan; section 3 covers them.")
    w(f"- So every server-side ref is local, equal to its local counterpart and an ancestor of origin/main, and the "
      f"server holds no ref the history raw did not scan apart from `main`'s new tip: "
      f"{'yes' if refs_pass else 'NO'}.")
    w("")

    # ---- (2)
    w("## 2. GitHub-side surfaces (read-only `gh`)")
    w("")
    st = S["settings"]
    w(f"Repository `{SLUG}`: visibility **{st['visibility']}** (isPrivate {st['isPrivate']}); default branch "
      f"`{st['defaultBranch']}`; licenseInfo {st['licenseInfo'] or 'none'}; wiki enabled {st['hasWikiEnabled']}; issues enabled "
      f"{st['hasIssuesEnabled']}; projects enabled {st['hasProjectsEnabled']}; discussions enabled "
      f"{st['hasDiscussionsEnabled']}. REST: has_pages {st['api']['has_pages']}, has_downloads "
      f"{st['api']['has_downloads']}, allow_forking {st['api']['allow_forking']}, forks {st['api']['forks_count']} "
      f"(network {st['api']['network_count']}), archived {st['api']['archived']}, open issues "
      f"{st['api']['open_issues_count']}.")
    w("")
    w("| surface | query (read-only) | rc | result |")
    w("|---|---|---|---|")
    qd = {k: v for k, v in G.items()}

    def qrow(lab, key, res):
        q = qd[key]
        w(f"| {lab} | `{q['cmd']}` | {q['rc']} | {res} |")
    qrow("pull requests", "pr_list", f"{S['pull_requests']['count']} (by state {S['pull_requests']['by_state'] or '{}'}; "
         f"authors {S['pull_requests']['authors'] or '{}'})")
    qrow("issues", "issue_list", f"{S['issues']['count']} (by state {S['issues']['by_state'] or '{}'})")
    qrow("issue and PR comments", "issue_comments", f"{S['issue_comments']['count']}")
    qrow("PR review comments", "review_comments", f"{S['review_comments']['count']}")
    qrow("commit comments", "commit_comments", f"{S['commit_comments']['count']}")
    qrow("releases", "release_list", f"{S['releases']['count']} (assets "
         f"{sum(x['assets'] for x in S['releases']['detail'])})")
    qrow("Actions runs", "run_list", f"{S['actions']['runs']} (by status {S['actions']['runs_by_status'] or '{}'})")
    qrow("Actions workflows", "workflows", f"{S['actions']['workflows_total']} (`.github/` files at HEAD: "
         f"{S['actions']['workflow_files_at_HEAD']})")
    qrow("Actions artifacts", "artifacts", f"{S['actions']['artifacts_total']} (names: "
         f"{len(S['actions']['artifact_names_sha8'])}; nothing downloaded)")
    w(f"| wiki repository | `{wiki['cmd']}` | {wiki['rc']} | refs {wiki['refs']}; "
      f"{'not found (no wiki repository)' if wiki['not_found'] else 'found'}; hasWikiEnabled {st['hasWikiEnabled']} |")
    qrow("GitHub Pages", "pages", f"HTTP {S['pages']['status']}" + (" = no Pages site" if S['pages']['status'] == '404'
                                                                     else ""))
    qrow("deploy keys", "deploy_keys", f"count {S['deploy_keys']['count']}" + (
        f" (HTTP {S['deploy_keys']['status']})" if S['deploy_keys']['status'] else " (readable)"))
    qrow("webhooks", "hooks", f"count {S['hooks']['count']}" + (
        f" (HTTP {S['hooks']['status']})" if S['hooks']['status'] else " (readable)"))
    qrow("milestones", "milestones", f"{S['milestones']['count']}")
    qrow("discussions / deployments / environments", "graphql_counts",
         f"{S['graphql']['discussions']} / {S['graphql']['deployments']} / {S['graphql']['environments']}")
    qrow("projects (v2) linked to the repository", "graphql_projects_v2",
         f"not readable: {S['graphql']['projects_v2_error_type']} (the CLI's credentials lack the project-read "
         f"scope)" if S['graphql']['projects_v2_error_type'] else f"{S['graphql']['projects_v2']}")
    ac = S["activity"]
    qrow("repository activity (Code's addition)", "activity",
         f"{ac['records']} records, {ac['earliest']} to {ac['latest']}; by type {ac['by_type']}; actors {ac['actors']}")
    w("")
    w("Every query above is a read: the REST calls are GETs (no method flag, no fields) and the two GraphQL calls "
      "POST a query, which reads, as GraphQL requires. None was refused apart from the projects (v2) read, whose "
      "error is an answer: the PI can read the repository's Projects tab on the web.")
    w("")
    w("**Force-pushed-away commits (pre-flip step 2's last clause).** The activity record lists "
      f"{ac['force_push']} force push(es) and {ac['branch_deletion']} branch deletion(s). Its {ac['pushes']} pushes: "
      f"both endpoints local {ac['pushes_both_local']}, fast-forward by `merge-base --is-ancestor` "
      f"{ac['pushes_fast_forward']}, not fast-forward {ac['pushes_not_fast_forward']}; every recorded `after` "
      f"object local: {'yes' if ac['afters_not_local'] == 0 else 'NO (' + str(ac['afters_not_local']) + ' not local)'}; "
      f"reachable from its ref's current server tip: {ac['afters_reachable_from_server_tip']} of "
      f"{ac['afters_checked']} checked. Its earliest record ({ac['earliest']}) and the first push in this clone's "
      f"reflog as the history raw records it ({ac['first_push_local_reflog']}) are the same instant: "
      f"{'yes' if ac['earliest_equals_first_push'] else 'NO'}.")
    w("")
    w("| ref | activity records | distinct `after` values | of them in this clone's remote-tracking reflog | not in it | reflog entries (kinds) | reflog values not in the activity record |")
    w("|---|---|---|---|---|---|---|")
    for ref, x in ac["reflog_compare"].items():
        kinds = ", ".join(f"{k} {n}" for k, n in sorted(x["reflog_kinds"].items()))
        w(f"| `{ref}` | {x['activity_entries']} | {x['activity_afters']} | {x['afters_in_reflog']} | "
          f"{x['afters_not_in_reflog']} | {x['reflog_entries']} ({kinds}) | {x['reflog_values_not_in_activity']} |")
    w("")
    w("A push this clone did not make shows as an `after` value missing from its reflog (column five); the counts "
      "above say whether such objects are local and reachable from the current server tips. The activity record is "
      "GitHub's; how far back GitHub keeps it is not stated in anything this run read, so the conclusion is bounded "
      "by that record: on what GitHub returns, nothing was force-pushed away or deleted.")
    w("")
    sc = S["screen"]
    w(f"**Screen of the text these surfaces carry** (the history script's precise patterns and identifier shapes, "
      f"the scrub index's guard shapes, email addresses other than the service address and the commit identities', "
      f"and the {len(known)} resolved known values): texts screened "
      f"{', '.join(f'{k} {n}' for k, n in sorted(sc['texts_screened'].items())) or 'none'}; hits "
      f"{sum(sc['hits'].values())}{(' -- ' + '; '.join(f'{k}: {n}' for k, n in sc['hits'].items())) if sc['hits'] else ''}. "
      f"Logins other than the repository owner's on any item read: {sum(sc['non_owner_logins'].values())}"
      f"{(' (redacted: ' + ', '.join(f'{k} x{n}' for k, n in sc['non_owner_logins'].items()) + ')') if sc['non_owner_logins'] else ''}. "
      f"With no pull request, issue, comment, release, run, artifact or milestone on the server, the screen had "
      f"only ref names to read." if not (S['pull_requests']['count'] or S['issues']['count'] or S['releases']['count']
                                         or S['actions']['runs'] or S['milestones']['count']) else "")
    w("")

    # ---- (3)
    rr = H["routed_run"]
    dr = H["dump_run"]
    ref_keys = sorted({k_of(x["form"]) for x in rr["refusal_forms_printed"]})
    brute_keys = {r["vkey"] for r in rows if tab_of(r["table"]) in BRUTE_FORCE_CLASSES} | \
        {k_of(f) for f in kv if any(short(kv[f][0]).startswith(b) for b in BRUTE_FORCE_CLASSES)}
    own_text = git("show", f"HEAD:{HIST_SCRIPT}") + git("show", f"{rec}:{HIST_MD}") + git("show", f"{rec}:{HIST_JSON}")
    fl = H["full_leak_list"]
    leak_rows = []
    for v, outs in leak_vals.items():
        k = sha8(v)
        rws = [r for r in rows if r["vkey"] == k]
        nws = [r for r in new_rows if r["vkey"] == k]
        rx_ = re.compile(r"(?<![A-Za-z0-9])" + re.escape(v) + r"(?![A-Za-z0-9])")
        leak_rows.append({
            "form": "(class recoverable by brute force: form withheld)" if k in brute_keys
            else f"{v[:4]}...[len {len(v)}]#{k}", "key": k, "outputs": sorted(outs),
            "tables": sorted({tab_of(r["table"]) for r in rws}), "verdicts_script": sorted({r["verdict"] for r in rws}),
            "verdicts_code": sorted({r["code_verdict"] for r in nws}), "new_in_c": bool(nws),
            "first_commits": sorted({r["first"].split(" ")[0][:8] for r in rws}),
            "in_routed_sample": k in ref_keys,
            "in_own_committed_text": bool(rx_.search(own_text)), "in_own_committed_text_substring": v in own_text})
    del own_text
    leak_rows.sort(key=lambda x: (x["form"], x["key"]))
    lk_own = sum(1 for x in leak_rows if x["in_own_committed_text"])
    lk_first = collections.Counter(c for x in leak_rows for c in x["first_commits"])
    lk_nodump = sum(1 for x in leak_rows if not x["tables"])
    fl["values"] = [{k_: x[k_] for k_ in x if k_ != "key"} for x in leak_rows]
    fl["in_own_committed_text"] = lk_own
    w("## 3. Interim history scan at HEAD")
    w("")
    w(f"**(a) The routed run.** `{rr['cmd']}` exited {rr['rc']} after {rr['secs']} s (HEAD `{rr['head_before'][:10]}` "
      f"before and `{rr['head_after'][:10]}` after). md written: {'yes' if rr['md_written'] else 'no'}; JSON written: "
      f"{'yes' if rr['json_written'] else 'no'}." + (
          f" **It refused to write**: its leak assertion found {rr['refused_count']} entries, one per value it "
          f"redacts as sensitive and output (md or JSON) in which that value appears verbatim, so a value found in "
          f"both outputs counts twice. Its message prints only the first {len(rr['refusal_forms_printed'])} entries "
          f"(`leaks[:10]`), in the iteration order of a Python set, which depends on the hash seed; this run pins "
          f"PYTHONHASHSEED={HASHSEED} for the routed run, so the sample is reproducible, but it is a partial sample "
          f"({len(ref_keys)} distinct value(s)): "
          + ", ".join(f"`{x['form']}` ({x['output']})" for x in rr['refusal_forms_printed']) + "." if rr["refused"]
          else ""))
    w("")
    if rr["refused"] or fl["entries"]:
        w(f"**The full list.** {fl['method'][0].upper() + fl['method'][1:]}: {fl['outcome']} after {fl['secs']} s "
          f"(HEAD unchanged across it: {'yes' if fl['head_before'] == fl['head_after'] == H['routed_run']['head_before'] else 'NO'}); "
          f"{fl['entries']} entries (equal to the routed run's count: "
          f"{'yes' if fl['entries_equal_routed_count'] else 'NO'}), {fl['distinct_values']} distinct values; the "
          f"routed run's printed sample is contained in it: {'yes' if fl['routed_sample_contained'] else 'NO'}. Values "
          f"are held in memory and shown by form, sorted:")
        w("")
        w("| form | output(s) | dump table(s) | script's verdict | Code's verdict (new values of (c)) | first commit | "
          "in the routed sample | verbatim in the audit's own committed text |")
        w("|---|---|---|---|---|---|---|---|")
        for x in leak_rows:
            w(f"| `{x['form']}` | {', '.join(x['outputs'])} | {', '.join(x['tables']) or 'not in the dump'} | "
              f"{', '.join(x['verdicts_script']) or '-'} | {', '.join(x['verdicts_code']) or '-'} | "
              f"{', '.join('`' + c + '`' for c in x['first_commits']) or '-'} | {'yes' if x['in_routed_sample'] else 'no'} | "
              f"{'yes' if x['in_own_committed_text'] else 'no'} |")
        w("")
        w(f"'The audit's own committed text' is the history script at HEAD plus its committed raw and JSON at "
          f"`{rec[:7]}`, matched word-bounded as the leak assertion matches. Of the {len(leak_rows)} distinct values, "
          f"{lk_own} occur there (class labels, pattern text, triage reasons, prose); first seen: "
          f"{', '.join(f'`{c}` {n}' for c, n in sorted(lk_first.items())) or '-'}"
          f"{f'; not in the dump tables: {lk_nodump}' if lk_nodump else ''}. The script prints values only in "
          f"redacted form, so a verbatim occurrence in its output is text it writes itself -- text that the audit's "
          f"committed files now carry, so its scan reports it as values. The committed script therefore cannot write "
          f"at this HEAD; pre-flip step 3 needs a clean write at the release commit, which needs a change to that "
          f"committed audit script (triage entries marking these values non-sensitive, or labels printed without "
          f"them): the PI's or the design seat's call, not made here.")
        w("")
    w(f"**(b) The dump run** (the same script, unchanged, in its documented `--dump-untriaged --dump-all` mode, which "
      f"prints every value of every table to stdout and writes no file): exit {dr['rc']} after {dr['secs']} s, "
      f"'DUMP ONLY' line present: {'yes' if dr['dump_only_line'] else 'no'}; {dr['rows']} value rows and "
      f"{dr['shape_rows']} untriaged credential-shaped fallback rows parsed, {dr['unparsed_lines']} other line(s); "
      f"files written by it: {len(dr['files_written'])}. HEAD scanned: `{H['head_scanned']}` (unchanged across the "
      f"run: {'yes' if H['head_scanned'] else 'NO'}). The dump does not print the header-identifier and "
      f"binary-identifier tables; the window's commit headers are read directly in (f).")
    w("")
    w(f"Window: the commits after the block's commit `{base[:10]}` -- {len(win)} on HEAD "
      f"({', '.join('`' + c[:10] + '`' for c in win)}; {len(win_all)} from all refs). The routing says both 'the "
      f"commits after `bab921c`' and 'c75d4d8..HEAD'; in git's notation c75d4d8..HEAD leaves out `c75d4d8` itself, so "
      f"this file reports every commit after `{base[:7]}` one by one and either reading can be taken from the "
      f"per-commit columns. The committed JSON's scan already covered `{hj['head'][:10]}` and its ancestors; the "
      f"commits it did not see: {', '.join('`' + c[:10] + '`' for c in after_rec_scan)}.")
    w("")
    w(f"**(c) Value tables, HEAD against the committed JSON** (`{HIST_JSON}@{rec[:7]}`; tables keyed by the value's "
      f"sha256 prefix, so the committed redacted forms and the dumped values compare exactly). New values: "
      f"{len(new_rows)}; values in the committed JSON missing now: {gone_total}.")
    w("")
    w("| table | committed | now | new |")
    w("|---|---|---|---|")
    for x in per_table:
        if x["new"] or x["gone"]:
            w(f"| {x['table']} | {x['committed']} | {x['now']} | {x['new']} |")
    w("")
    w(f"Tables with no change: {sum(1 for x in per_table if not x['new'] and not x['gone'])} of {len(per_table)} "
      f"non-empty. New values by the commit of their first occurrence: "
      f"{', '.join(f'`{k}` {n}' for k, n in sorted(H['new_first_commit'].items()))}.")
    w("")
    w("New values by table and verdict (the history script's verdict, or Code's where the script left the value "
      "UNTRIAGED):")
    w("")
    w("| table | verdict | first commit | n |")
    w("|---|---|---|---|")
    for x in H["new_by_table_verdict"]:
        w(f"| {x['table']} | {x['verdict']} | `{x['first_commit']}` | {x['n']} |")
    w("")
    w(f"The {len(script_unt)} new value(s) the history script leaves UNTRIAGED, triaged by Code in context "
      f"(first locator = the commit and file of the first occurrence; the value only by its form):")
    w("")
    w("| table | form | occurrences | first locator | Code's verdict | reason |")
    w("|---|---|---|---|---|---|")
    for r in sorted(script_unt, key=lambda r: (r["tab"], r["first"])):
        fm = form(r["v"], port=r["tab"] == "ssh_port")
        if r["tab"] in BRUTE_FORCE_CLASSES:
            fm = "(class recoverable by brute force: form withheld)"
        w(f"| {r['tab']} | `{fm}` | {r['n_occ']} | `{r['first']}` | {r['code_verdict']} | {r['code_reason']} |")
    w("")
    w(f"**Credential-shaped fallback rows** (the block's `key = value` / `key: value` shapes): {len(shape_rows)} "
      f"rows the history script leaves UNTRIAGED, all first seen in "
      f"{', '.join('`' + c + '`' for c in sorted({r['commit'] for r in shape_rows})) or '-'}. Code's triage:")
    w("")
    shc = collections.Counter((r["path"], r["key"], r["code_verdict"], r["reason"]) for r in shape_rows)
    w("| file | key | rows | Code's verdict | reason |")
    w("|---|---|---|---|---|")
    for (p, k, v, rs), n in sorted(shc.items()):
        w(f"| `{p}` | `{k}` | {n} | {v} | {rs} |")
    w("")
    w(f"**Already recorded in the committed JSON** (values whose first occurrence is a window commit the committed "
      f"scan covered): " + ("; ".join(f"`{x['commit']}` {x['table']} {x['verdict']} {x['n']}"
                                       for x in H["already_recorded_in_window"]) or "none") + ".")
    w("")
    w(f"**(d) Answers for the window.** TRUE-SECRET-CANDIDATE now {len(true_all)} (new {len(true_new)}; committed "
      f"{hj['true_secret_candidates']}). New values in the identifier classes the routing's redaction rule names "
      f"({len(REDACTION_CLASSES)} of the history script's {len({short(c) for c in h.ID_PATTERNS})} identifier "
      f"classes: {', '.join(REDACTION_CLASSES)}; the other "
      f"{len(REDACTION_EXCLUDED)}, {', '.join(REDACTION_EXCLUDED)}, are local paths and public hosts, counted in the "
      f"tables above): {len(new_red)}, of them still open after triage: {len(new_red_open)}. By class and verdict: "
      + ("; ".join(f"{k[0]} {k[1]} {n}" for k, n in sorted(new_red_by.items())) or "none") + ". "
      + (f"Their forms: the {sum(1 for r in new_red if r['verdict'] == 'UNTRIAGED')} the script left UNTRIAGED are "
         f"in the table above; the others: "
         + ("; ".join(f"{r['tab']} `{'(form withheld)' if r['tab'] in BRUTE_FORCE_CLASSES else form(r['v'], port=r['tab'] == 'ssh_port')}` "
                      f"{r['code_verdict']}" for r in new_red if r['verdict'] != 'UNTRIAGED') or "none") + "."
         if new_red else "")
      + f" New high-entropy candidates: in-context {sum(1 for r in new_rows if r['tab'] == 'high_entropy')}, "
      f"context-free {sum(1 for r in new_rows if r['tab'] == 'context_free')}, all FALSE-POSITIVE or LOCAL-PATH "
      f"after triage: {'yes' if all(r['code_verdict'] in ('FALSE-POSITIVE', 'LOCAL-PATH') for r in new_rows if r['tab'] in ('high_entropy', 'context_free')) else 'NO'}. "
      f"Values left UNTRIAGED after Code's triage: {len(new_unt)}; credential-shaped rows left UNTRIAGED: "
      f"{len(shape_unt)}.")
    w("")
    w(f"**(e) Fallback grep at HEAD** (`{fb['cmd']}`, the block's :77 command as the history script runs it; "
      f"{fb['logp_bytes']:,} bytes of log): {fb['hit_lines']} hit lines (a Python line-by-line cross-check counts "
      f"{fb['python_crosscheck_lines']}), against the committed {fb['committed']}: "
      f"{'+' if fb['delta'] >= 0 else ''}{fb['delta']}. Hit lines in the commits the committed scan did not see: "
      f"{fb['delta_from_commits_after_the_committed_scan']} "
      f"({'equal to' if fb['delta_from_commits_after_the_committed_scan'] == fb['delta'] else 'NOT equal to'} the "
      f"delta). Per commit in the window: "
      f"{', '.join(f'`{c}` {n}' for c, n in fb['per_commit_in_window'].items())}.")
    w("")
    w("| alternative (block :77) | lines, committed | lines, now |")
    w("|---|---|---|")
    for n, _ in h.FALLBACK_ALTS:
        w(f"| `{n}` | {fb['per_alternative_committed'][n]} | {fb['per_alternative_now'][n]} |")
    w("")
    w(f"The new hits ({len(after_rec_scan)} commit(s) after the committed scan) by the history script's own bulk rules "
      f"(occurrences, as its fallback triage counts them):")
    w("")
    w("| alternative | rule | occurrences |")
    w("|---|---|---|")
    for x in fb["new_hits_by_rule"]:
        w(f"| `{x['alternative']}` | {x['rule']} | {x['occurrences']} |")
    w("")
    w(f"Of these, {fb['inspection_rule_hits']} fall in the rules the history script lists for inspection rather than "
      f"clearing ({', '.join(INSPECT_RULES)}), in {len({x['path'] for x in fb['inspection_rule_files']})} file(s); "
      f"outside the audit's own scripts and raws: {fb['inspection_rule_hits_outside_audit_files']}. Per rule and "
      f"file: " + "; ".join(f"{x['rule']} `{x['path']}` {x['n']}" for x in fb["inspection_rule_files"]) + ". " +
      (f"Code read every one of their {fb['inspection_rule_lines']} distinct lines before this file was written "
       f"(the set's sha256 `{fb['inspection_rule_hits_sha256'][:16]}...` equals the one Code read): each is a secret "
       "pattern or its name, a class label, a credential's variable name inside a regular expression, a self-test "
       "template whose value is generated at run time, prose describing an earlier triage finding, or text about the "
       "(iii) continuity item, in the audit's own scripts and raws ("
       + ("N12's, plus " + "; ".join(f"{v['hits']} hit(s) on {v['lines']} line(s) of `{p}`"
                                     for p, v in fb["inspection_rule_hits_outside_n12_files"].items())
          if fb["inspection_rule_hits_outside_n12_files"] else "all of them N12's")
       + f"); none carries a value. The {len(h.PRECISE)} precise patterns and the high-entropy scans over the same "
       "blobs (section 3(c)-(d)) leave no candidate."
       if fb["inspection_rule_hits_read_by_code"] else
       f"**These lines are not the set Code read** (sha256 `{fb['inspection_rule_hits_sha256'][:16]}...`): they "
       "need Code's reading before this check can pass."))
    w("")
    w("The literal :77 outcome is unchanged in kind: the fallback returns hits, so (i) is still not 'no hits' and stays "
      "STOP pending the PI.")
    w("")
    w(f"**(f) Large blobs, known values and commit identities in the window.** Blobs reachable now but not from "
      f"`{base[:10]}`: {blobs['new_blobs_since_base']}; over 1 MB {blobs['new_over_1MB']}, over 40 MB "
      f"{blobs['new_over_40MB']}, over 50 MB {blobs['new_over_50MB']}, over 100 MB {blobs['new_over_100MB']}; the "
      f"largest: " + ", ".join(f"`{x['path']}` {x['size']:,} bytes" for x in blobs["largest_new"][:3]) +
      f" (the committed largest blob anywhere: {blobs['committed_max_blob']:,} bytes). Files over 40 MB at HEAD: "
      f"{len(blobs['head_files_over_40MB'])}, equal to the committed list: "
      f"{'yes' if blobs['head_files_over_40MB_equal_committed'] else 'NO'}.")
    w("")
    w("Occurrences of the history raw's known sensitive values that each window commit added: in each blob it added "
      "or modified, the count in the new blob minus the count in the parent's blob at the same path, plus its "
      "message (by the history raw's class labels, short form; exact, the SSH-port class word-bounded). A modified "
      "file that already carried a value counts only what the commit added:")
    w("")
    w("| commit | blobs added or modified | net new occurrences | files | occurrences in the new blobs (whole files) |")
    w("|---|---|---|---|---|")
    for x in kv_rows:
        oc = "; ".join(f"{short(k)} {n}" for k, n in sorted(x["net_new"].items())) or "0"
        wh = "; ".join(f"{short(k)} {n}" for k, n in sorted(x["occurrences_in_new_blobs"].items())) or "0"
        w(f"| `{x['commit']}` | {x['blobs_added_or_modified']} | {oc} | "
          f"{', '.join('`' + f + '`' for f in x['files_with_net_new']) or '-'} | {wh} |")
    w("")
    w("| commit | author and committer are commit identities the history raw lists | their forms | gpgsig | session link in the message |")
    w("|---|---|---|---|---|")
    for x in id_rows:
        w(f"| `{x['commit']}` | {'yes' if x['author_committer_known_identity'] else 'NO'} | "
          f"{', '.join('`' + f + '`' if '#' in f else f for f in x['author_committer_forms'])} | "
          f"{'yes' if x['gpgsig'] else 'no'} | {'yes' if x['session_link_in_message'] else 'no'} |")
    w("")

    # ---- (4) pass/flag lines
    w("## 4. Pass / flag lines")
    w("")
    L4 = []

    def pf(label, ok, text):
        L4.append({"check": label, "outcome": ("PASS" if ok is True else "FLAG" if ok is False else ok),
                   "text": text})
    pf("(1) server refs", refs_pass, f"{len(server)} server refs; none outside the local refs; refs/pull/* "
       f"{len(pulls)}; every one an ancestor of origin/main; only main moved since the history raw's table.")
    pf("(2a) visibility", "INFO", f"{st['visibility']} now; the flip is the PI's.")
    def read_ok(*keys):
        """every query behind a PASS returned rc 0 (an unread surface cannot pass)"""
        return all(G[k]["rc"] == 0 for k in keys)
    pf("(2b) pull requests and comments", read_ok("pr_list", "review_comments") and
       all(d["view_rc"] == 0 for d in S['pull_requests']['detail']) and
       S['pull_requests']['count'] == 0 and S['review_comments']['count'] == 0,
       f"{S['pull_requests']['count']} PRs, {S['review_comments']['count']} review comments.")
    pf("(2c) issues and comments", read_ok("issue_list", "issue_comments", "commit_comments") and
       all(d["view_rc"] == 0 for d in S['issues']['detail']) and
       S['issues']['count'] == 0 and S['issue_comments']['count'] == 0 and S['commit_comments']['count'] == 0,
       f"{S['issues']['count']} issues, {S['issue_comments']['count']} issue/PR comments, "
       f"{S['commit_comments']['count']} commit comments (issues are enabled: after the flip anyone can open one).")
    pf("(2d) releases", read_ok("release_list") and S['releases']['count'] == 0, f"{S['releases']['count']} releases.")
    pf("(2e) Actions", read_ok("run_list", "workflows", "artifacts") and S['actions']['runs'] == 0 and
       S['actions']['workflows_total'] == 0 and S['actions']['artifacts_total'] == 0,
       f"{S['actions']['runs']} runs, {S['actions']['workflows_total']} workflows, "
       f"{S['actions']['artifacts_total']} artifacts.")
    pf("(2f) wiki", read_ok("repo_view") and st['hasWikiEnabled'] is False and wiki['not_found'],
       f"enabled {st['hasWikiEnabled']}; wiki repository not found: {'yes' if wiki['not_found'] else 'NO'}.")
    pf("(2g) Pages", S['pages']['status'] == '404', f"HTTP {S['pages']['status']}: no site.")
    pf("(2h) deploy keys / webhooks", read_ok("deploy_keys", "hooks") and S['deploy_keys']['count'] == 0 and
       S['hooks']['count'] == 0, f"{S['deploy_keys']['count']} / {S['hooks']['count']} (readable).")
    pf("(2i) projects (v2)", "NOT READ" if S['graphql']['projects_v2_error_type'] else S['graphql']['projects_v2'] == 0,
       "not readable with the CLI's scopes; the PI checks the Projects tab." if S['graphql']['projects_v2_error_type']
       else f"{S['graphql']['projects_v2']}.")
    pf("(2j) force-pushed-away / deleted", read_ok("activity") and ac['records'] > 0 and ac['force_push'] == 0 and
       ac['branch_deletion'] == 0 and ac['pushes_not_fast_forward'] == 0 and ac['afters_not_local'] == 0,
       f"activity record ({ac['records']} records): {ac['force_push']} force pushes, {ac['branch_deletion']} "
       f"deletions, {ac['pushes_not_fast_forward']} non-fast-forward pushes, {ac['afters_not_local']} pushed objects "
       f"not local.")
    pf("(2k) text screen and third-party logins", sum(sc['hits'].values()) == 0 and not sc['non_owner_logins'],
       f"{sum(sc['hits'].values())} hits; {sum(sc['non_owner_logins'].values())} non-owner logins.")
    pf("(3a) history script at HEAD", rr['rc'] == 0,
       (f"refused to write ({rr['refused_count']} entries, {fl['distinct_values']} distinct values; "
        f"{lk_own} of them occur in its own committed text); step 3 cannot pass with the committed script as it "
        f"stands." if rr['refused'] else f"exit {rr['rc']}."))
    pf("(3b) new TRUE-SECRET-CANDIDATE", len(true_new) == 0 and len(true_all) == 0, f"{len(true_all)} now.")
    pf("(3c) new redaction-rule identifier values", len(new_red_open) == 0,
       f"{len(new_red)} new in the {len(REDACTION_CLASSES)} classes listed in 3(d), {len(new_red_open)} open after "
       f"triage.")
    pf("(3d) new values / shapes the script leaves UNTRIAGED", len(script_unt) == 0 and
       sum(1 for r in shape_rows if r['script_verdict'] == 'UNTRIAGED') == 0,
       f"{len(script_unt)} values and {len(shape_rows)} shapes UNTRIAGED by the script; after Code's triage here "
       f"{len(new_unt)} and {len(shape_unt)}.")
    pf("(3e) new large blobs", blobs['new_over_50MB'] == 0 and blobs['new_over_100MB'] == 0,
       f"largest new blob {blobs['largest_new'][0]['size'] if blobs['largest_new'] else 0:,} bytes.")
    pf("(3f2) new fallback hits in the history script's inspection rules", fb["inspection_rule_hits_read_by_code"]
       and fb["inspection_rule_hits_outside_audit_files"] == 0,
       f"{fb['inspection_rule_hits']} hits, all in the audit's own files and read by Code: "
       f"{'yes' if fb['inspection_rule_hits_read_by_code'] and fb['inspection_rule_hits_outside_audit_files'] == 0 else 'NO'}.")
    pf("(3f) fallback grep count", "INFO", f"{fb['hit_lines']} at HEAD vs {fb['committed']} committed "
       f"({'+' if fb['delta'] >= 0 else ''}{fb['delta']}, all in the commits the committed scan did not see: "
       f"{'yes' if fb['delta_from_commits_after_the_committed_scan'] == fb['delta'] else 'NO'}).")
    aft10 = {c[:10] for c in after_rec_scan}
    kv_red = sum(n for x in kv_rows if x["commit"] in aft10 for k, n in x["net_new"].items()
                 if not k.replace("(message) ", "").startswith("identity email") and n > 0)
    kv_id = sum(n for x in kv_rows if x["commit"] in aft10 for k, n in x["net_new"].items()
                if k.replace("(message) ", "").startswith("identity email") and n > 0)
    pf("(3g) redaction-rule values added after the committed scan", kv_red == 0,
       f"{kv_red} net new occurrence(s) of the known RunPod, port, host, link, phrase and hostname values in what the "
       f"commits after `{hj['head'][:10]}` added; identity emails (public in the commit headers, listed by the "
       f"history raw's pre-release section and not a blocker as drafted): {kv_id}.")
    for x in L4:
        w(f"- {x['outcome']} -- **{x['check']}**. {x['text']}")
    w("")

    # ---- (5) what remains
    w("## 5. What remains for the PI before the visibility flip")
    w("")
    l10 = locate(smd, lambda s: s.startswith("## 10."))
    items = {k: locate(smd, lambda s, k=k: s.startswith(f"{k}. "), l10) for k in range(1, 6)}
    w(f"From the scrub index's pre-flip checklist (`{SCRUB_MD}@{rec[:7]}:{l10}`), marked by this run:")
    w("")
    again = ("Repeat at the release commit, immediately before the visibility change: the release commit and any "
             "tag push add or move server refs, and these surfaces can change until the flip. ")
    s1_ok = refs_pass
    s2_ok = all(x["outcome"] == "PASS" for x in L4 if x["check"][:3] in ("(2b", "(2c", "(2d", "(2e", "(2f", "(2g",
                                                                          "(2h", "(2j"))
    R5 = [
        (1, f"DONE at `{head1[:7]}`, interim" if s1_ok else "NOT DONE (section 1 flags)",
         again + f"At this HEAD: ls-remote compared with the history raw's refs table: no extra branch or tag, no "
         f"`refs/pull/*`, nothing to scan or delete beyond `main`'s new commits (section 1). Deleting the "
         f"`claude/handoff-doc-next-steps-oeccd1` branch stays optional (it is scanned and an ancestor of "
         f"origin/main)." if s1_ok else "see section 1."),
        (2, f"DONE at `{head1[:7]}`, interim, one part bounded" if s2_ok else "NOT DONE (section 4 flags)",
         again + "At this HEAD: pull requests, comments, issues, Actions runs and artifacts, the wiki, releases, "
         "Pages, deploy keys and webhooks: none (section 2). Force-pushed-away commits: none on GitHub's activity "
         "record, a bound set by that record's retention. Projects (v2): not readable here; the PI's look."
         if s2_ok else "see section 4."),
        (3, "NOT DONE (and blocked as the script stands)",
         "this run is an interim scan at HEAD, not the release commit. The committed history script refuses to write "
         "at HEAD (section 3a); before it can produce the clean run the step requires it needs a change -- triage "
         "entries for the values and credential-shaped rows of 3(c) and the inspection-rule hits of 3(e), or class "
         "labels printed without the strings its scan reports -- to a committed audit script, the PI's or design "
         "seat's call. The content and licenses scripts were not re-run."),
        (4, "NOT DONE", f"untracked files were not reviewed by this run; at its start the checkout had "
                        f"{len(untracked0)} untracked, not-ignored file(s) other than this run's script and its two "
                        f"outputs, and {len(modified0)} modified tracked file(s). Stage by explicit path."),
        (5, "NOT DONE", "the block's primary scanners (gitleaks, trufflehog) need the PI's word to install."),
    ]
    for k, status, text in R5:
        w(f"{k}. **{status}** (`{SCRUB_MD}@{rec[:7]}:{items[k]}`) -- {text}")
    w("")
    l9 = locate(smd, lambda s: s.startswith("## 9."))
    w(f"Not on the checklist and untouched by this run: the decisions D1-D4 and the other open PI items "
      f"(`{SCRUB_MD}@{rec[:7]}:{l9}`), the (iii) continuity item (`{SCRUB_MD}@{rec[:7]}:"
      f"{locate(smd, lambda s: s.startswith('## 4.'))}`), and (i)'s resolution of the fallback's hits. This run's "
      f"own two outputs and its script join the files the release re-run must scan (step 3).")
    w("")
    md_body = "\n".join(out) + "\n"
    J["pass_flag"] = L4
    J["remaining"] = [{"item": k, "status": s, "locator": f"{SCRUB_MD}@{rec[:7]}:{items[k]}", "text": t}
                      for k, s, t in R5]
    J.update({"stamp": stamp, "head_start": head0, "head_end": head1, "refs_moved": moved, "rec": rec, "base": base,
              "block_sha256": block_wt, "script": me_rel, "script_sha256": me_sha, "python": py,
              "history_script_sha256_wt": hs_wt, "history_script_sha256_head": hs_head,
              "history_script_equals_recorded": hs_wt == hs_head == HIST_SCRIPT_SHA,
              "known_values": {"total": len(kv), "resolved": len(known), "unresolved_classes":
                               [known_label[f] for f in unresolved]},
              "history_dir_outside_repo": True,
              "new_values_detail": [{"table": r["tab"], "form": (form(r["v"], port=r["tab"] == "ssh_port")
                                                                 if r["tab"] not in BRUTE_FORCE_CLASSES else None),
                                     "verdict_script": r["verdict"], "verdict": r["code_verdict"],
                                     "reason": r["code_reason"] if r["verdict"] == "UNTRIAGED" else None,
                                     "n_occ": r["n_occ"], "first": r["first"]} for r in new_rows],
              "shape_rows_detail": shape_rows})
    secs_body = round(time.time() - T0, 1)

    # ---------- leak guard (values held in memory; applied to the final texts) ----------
    must_not = dict(known)
    code_public = {r["vkey"] for r in new_rows if r["code_verdict"] in PUBLIC_VERDICTS}
    for r in rows:
        if r["verdict"] not in PUBLIC_VERDICTS and r["v"] not in h.SAFE_VERBATIM and len(r["v"]) >= 3 \
                and r["vkey"] not in code_public:
            must_not["dumped:" + r["vkey"]] = r["v"]
    for r in new_rows:
        if r["code_verdict"] == "UNTRIAGED":
            must_not["untriaged:" + r["vkey"]] = r["v"]
    for v in leak_vals:
        if sha8(v) not in code_public and not any(r["vkey"] == sha8(v) and r["verdict"] in PUBLIC_VERDICTS
                                                  for r in rows):
            must_not.setdefault("leaklist:" + sha8(v), v)
    shape_forms = {k_of(sr["value_form"]) for sr in shape_rows if "#" in sr["value_form"]}
    allowed = {k_of(f) for f in kv} | {r["vkey"] for r in rows} | \
        {k_of(e["value"]) for t in old.values() for e in t.values()} | \
        {sha8(x) for x in identity_vals} | {k_of(x["form"]) for x in rr["refusal_forms_printed"]} | shape_forms | \
        {x["key"] for x in leak_rows}

    def ctx(txt, i, j):
        a_ = txt.rfind("\n", 0, i) + 1
        b_ = txt.find("\n", j)
        return (txt[max(a_, i - 80):i] + "<V>" + txt[j:min(b_ if b_ >= 0 else len(txt), j + 60)])

    def guard(md_, js_):
        leaks, debug = [], []
        for lab, txt in (("md", md_), ("json", js_)):
            for k, v in must_not.items():
                if k in known:
                    n = scrub.count_value(k, v, txt)
                else:
                    n = len(re.findall(r"(?<![A-Za-z0-9])" + re.escape(v) + r"(?![A-Za-z0-9])", txt))
                if n:
                    leaks.append((lab, known_label.get(k, k.split(":")[0]), n))
                    mt_ = re.search(re.escape(v), txt)
                    if mt_:
                        debug.append((lab, k.split(":")[0], ctx(txt, mt_.start(), mt_.end())))
            for nm, rx in scrub.GUARD_SHAPES:
                if rx.search(txt):
                    leaks.append((lab, "guard shape: " + nm, len(rx.findall(txt))))
                    mt_ = rx.search(txt)
                    debug.append((lab, nm, ctx(txt, mt_.start(), mt_.end())))
            if "/Users/" in txt:
                leaks.append((lab, "a /Users/ path", txt.count("/Users/")))
        printed = set(re.findall(r"\.\.\.\[len \d+\]#([0-9a-f]{8})", md_ + js_)) | \
            set(re.findall(r"(?<![A-Za-z0-9])len\d+:([0-9a-f]{8})", md_ + js_))
        unknown = sorted(printed - allowed)
        if unknown:
            leaks.append(("md/json", "redacted form not known to the history JSON, this run's dump or the leak list",
                          len(unknown)))
            debug.append(("md/json", "unknown forms", " ".join(unknown[:20])))
        if printed & brute_keys:
            leaks.append(("md/json", "a form of a class recoverable by brute force", len(printed & brute_keys)))
        return leaks, debug, printed

    # ---------- values-check: the checker's findings on the first version, with this run's evidence ----------
    l_asof = locate(smd, lambda s: s.startswith("As routed, with the part raws"), l10)
    added_cls = [c for c in REDACTION_CLASSES if c not in red_v1]
    added_n = collections.Counter(r["tab"] for r in new_red if r["tab"] in added_cls)
    leak_keys_now = {x["key"] for x in leak_rows}
    q_keys = ("pr_list", "review_comments", "issue_list", "issue_comments", "commit_comments", "release_list",
              "run_list", "workflows", "artifacts", "deploy_keys", "hooks", "repo_view", "activity")
    q_rc0 = all(G[k]["rc"] == 0 for k in q_keys)
    outc = {x["check"][:4]: x["outcome"] for x in L4}
    VC = [
        ("minor", "3(a) analysed only the entries the routed run's message prints (`leaks[:10]`): a partial sample "
                  "whose content depends on Python's hash seed (6 distinct values in the first version; the "
                  "checker, from a copy of the history script that prints every entry, found 12 distinct values "
                  "behind the 19 entries, all in the audit's own committed text, all first seen in `09c3a8c`)",
         "APPLIED, both remedies",
         f"The routed run now runs under PYTHONHASHSEED={HASHSEED}, so its printed sample is reproducible, and 3(a) "
         f"calls it a partial sample. The full list is read deterministically from the unchanged script (in-process, "
         f"same arguments, its own `leaks` list read from its frame when its leak assertion raises): "
         f"{fl['entries']} entries, {fl['distinct_values']} distinct values; entries equal to the routed run's "
         f"count: {'yes' if fl['entries_equal_routed_count'] else 'NO'}; the routed sample contained in it: "
         f"{'yes' if fl['routed_sample_contained'] else 'NO'}; the distinct values' sha256 prefixes equal the 12 the "
         f"checker listed: {'yes' if leak_keys_now == CHECKER_LEAK_KEYS else 'NO'}; in the audit's own committed "
         f"text: {lk_own} of {len(leak_rows)}; first seen: "
         f"{', '.join(f'`{c}` {n}' for c, n in sorted(lk_first.items())) or '-'}. The wording 'occurrences' is "
         f"replaced by 'entries' (one per value and output; the script records the first match per output)."),
        ("minor", "section 5 marked checklist items 1 and 2 DONE with no as-of qualifier, although the scrub index "
                  f"says each item needs the final HEAD, the network or the PI's word (`{SCRUB_MD}@{rec[:7]}:"
                  f"{l_asof}`), and the release commit and tag pushes will add or move server refs",
         "APPLIED",
         f"Items 1 and 2 now read 'DONE at `{head1[:7]}`, interim' and say to repeat them at the release commit, "
         f"immediately before the visibility change; item 3 stays NOT DONE. Each DONE is now also conditional on "
         f"this run's own checks (section 1's line for item 1; the PASS lines (2b)-(2h) and (2j) for item 2)."),
        ("minor", "the count of new values in the redaction-rule classes (4) used a class set that left out the SSH "
                  "key-name, key-path and identity-flag classes and the RunPod and proxy hostnames",
         "APPLIED, extended by Code",
         f"The set is now the routing's redaction rule mapped onto the history script's identifier classes "
         f"({len(REDACTION_CLASSES)} of {len(id_short)}; the other {len(REDACTION_EXCLUDED)} named in 3(d)), and the "
         f"run asserts that the two lists partition the script's classes. Added: "
         f"{', '.join(f'{c} {added_n.get(c, 0)}' for c in added_cls)} new value(s) (runpod_endpoint_or_template_id "
         f"is Code's addition: a RunPod identifier class the checker did not name). New values in the set: "
         f"{len(new_red)} (under the first version's set: {new_red_v1}); open after triage: {len(new_red_open)}. Of "
         f"the added classes' {sum(added_n.values())} new values, "
         f"{sum(1 for r in new_red if r['tab'] in added_cls and r['verdict'] == 'UNTRIAGED')} are rows of 3(c)'s "
         f"UNTRIAGED table, each triaged there by Code; the others carry the history script's own verdict."),
        ("minor", "3(e) said the inspection-rule hits were all 'in the audit's own N12 scripts and raws', but 2 of "
                  "them are in the tier-1 values-check raw",
         "APPLIED",
         f"The sentence is now built from the per-file list and names any file outside N12's: "
         + ("; ".join(f"{v['hits']} hit(s) on {v['lines']} line(s) of `{p}`"
                      for p, v in fb["inspection_rule_hits_outside_n12_files"].items()) or "none")
         + f". This run: {fb['inspection_rule_hits']} hits on {fb['inspection_rule_lines']} distinct lines, the "
         f"set's sha256 equal to the one Code read: {'yes' if fb['inspection_rule_hits_read_by_code'] else 'NO'}; "
         f"outside the audit's own files: {fb['inspection_rule_hits_outside_audit_files']}."),
        ("minor", "PASS conditions left out surfaces their own lines report: (2c) did not test the commit comments, "
                  "(2e) did not test the workflows",
         "APPLIED, extended by Code",
         f"(2c) now requires 0 commit comments and (2e) 0 workflows. Code's extension: every PASS in (2b)-(2h) and "
         f"(2j) also requires each query behind it to have returned rc 0 (in the first version a failed query of the "
         f"pull requests, review comments, issues, issue or commit comments, releases, runs, artifacts or the "
         f"activity record counted as 0 and could pass, and an unread wiki setting counted as disabled), (2f) "
         f"requires the wiki setting to read False, and (2j) requires a non-empty activity record. This run: those "
         f"{len(q_keys)} queries all rc 0: "
         f"{'yes' if q_rc0 else 'NO'}; (2b) {outc.get('(2b)')}, (2c) {outc.get('(2c)')}, (2e) {outc.get('(2e)')}, "
         f"(2j) {outc.get('(2j)')}."),
        ("minor", "the section-6 self-check of what a release re-run would make of this run's three files did not "
                  "apply the history scan's in-context or context-free high-entropy rules",
         "APPLIED",
         "The pre-check now also runs the history script's own in-context rule (its run pattern, context test, "
         "entropy bar and triage) and its context-free scan (its own scan function and triage) over the three files, "
         "and refuses on any high-entropy verdict other than FALSE-POSITIVE or PUBLIC. It now runs on the final "
         "texts, sections 6 and 7 included, and is iterated until the counts section 6 prints are the counts of the "
         "files that print them. This run's counts: section 6."),
    ]
    vc_md = ("\n## 7. Values-check\n\n"
             f"The first version of this raw (script sha256 `{FIRST_VERSION[0][:8]}...{FIRST_VERSION[0][-4:]}`, Code "
             f"stamp {FIRST_VERSION[1]}, run at `{FIRST_VERSION[2]}`; not committed) was checked by an adversarial "
             f"checker, who re-ran the script and every read independently and returned {len(VC)} findings, all "
             f"minor; it reported none as substantive. Code applied all {len(VC)} after confirming each, by reading "
             f"the cited lines or by this run's output; none was rejected. The checker also reports that every other "
             f"count it recomputed matched and that the redaction check was clean on the first version; those are its "
             f"results and are not re-derived here. Dispositions, with this run's evidence:\n\n"
             + "\n".join(f"{i}. **F{i} ({sev}) -- {claim}.** {disp}. {ev}" for i, (sev, claim, disp, ev)
                         in enumerate(VC, 1)) + "\n")
    J["values_check"] = {"first_version": {"script_sha256": FIRST_VERSION[0], "stamp": FIRST_VERSION[1],
                                           "head": FIRST_VERSION[2]},
                         "findings": [{"finding": f"F{i}", "severity": sev, "claim": claim, "disposition": disp,
                                       "evidence": ev} for i, (sev, claim, disp, ev) in enumerate(VC, 1)]}

    # ---------- self-checks on the final texts (iterated to a fixed point) ----------
    kset = set(known.values())

    def counts_line(pre_, prefix, strip):
        return "; ".join(f"{lab}: " + (", ".join(f"{k[len(strip):]} {n}" for k, n in sorted(c.items())
                                                 if k.startswith(prefix)) or "none") for lab, c in pre_.items())

    def make_tail(pre_, nforms):
        pre_ = pre_ or {"md": {}, "json": {}, "script": {}}
        return (f"\n## 6. Self-checks before writing\n\n- Leak guard: {len(must_not)} values held in memory "
                f"({len(known)} known, the rest dumped, untriaged or on the history script's leak list) and "
                f"{len(scrub.GUARD_SHAPES)} guard shapes: 0 occurrences in either output; redacted forms printed "
                f"{nforms}, all known to the history JSON, this run's dump or the history script's leak list, none "
                f"of a class recoverable by brute force.\n- What the release re-run of the history script would make "
                f"of this run's three files: its own precise, identifier, port-line, fallback, credential-shape, "
                f"in-context high-entropy and context-free high-entropy rules, applied here in memory to the final "
                f"texts (this file's sections 6 and 7 included) and iterated until the counts printed here are the "
                f"counts of the files that print them. Rows it would leave open: 0. Fallback hits by bulk rule -- "
                + counts_line(pre_, "fallback rule ", "fallback rule ")
                + ". In-context high-entropy values by verdict -- " + counts_line(pre_, "high_entropy ", "high_entropy ")
                + ". Context-free high-entropy values by verdict -- "
                + counts_line(pre_, "context_free ", "context_free ")
                + ". (P3 and T2 are listed by that script for inspection, not counted as open.)\n"
                f"- History script: sha256 at the working tree `{hs_wt}`, at HEAD `{hs_head}`; equal to the sha256 "
                f"its committed raw records: {'yes' if hs_wt == hs_head == HIST_SCRIPT_SHA else 'NO'}.\n"
                f"- Run time before the self-checks {secs_body} s.\n")

    pre, nforms = None, None
    for _ in range(8):
        J["self_checks"] = {"rerun_precheck": pre, "values_guarded": len(must_not), "forms_printed": nforms}
        J["secs"] = secs_body
        js_f = json.dumps(J, indent=1, default=str)
        md_f = md_body + make_tail(pre, nforms) + vc_md
        new = {lab: dict(rerun_precheck(h, txt, path, kset))
               for lab, txt, path in (("md", md_f, a.out), ("json", js_f, a.json_out), ("script", me_src, me_rel))}
        lk, dbg, printed = guard(md_f, js_f)
        if new == pre and len(printed) == nforms:
            break
        pre, nforms = new, len(printed)
    else:
        raise SystemExit("the self-check counts did not reach a fixed point; nothing written")
    bad = {lab: precheck_bad(c) for lab, c in pre.items()}
    bad = {k: v for k, v in bad.items() if v}
    if lk or bad:
        for d in dbg:
            print("DEBUG", d)
        with open(os.path.join(hist_dir, "debug_preflip.md"), "w") as f:
            f.write(md_f)
        with open(os.path.join(hist_dir, "debug_preflip.json"), "w") as f:
            f.write(js_f)
        raise SystemExit(f"REFUSING TO WRITE: leaks {lk}; rows a release re-run would leave open {bad}")
    with open(os.path.join(REPO, a.out), "w", encoding="utf-8") as f:
        f.write(md_f)
    with open(os.path.join(REPO, a.json_out), "w", encoding="utf-8") as f:
        f.write(js_f + "\n")
    print(f"wrote {a.out} ({len(md_f.splitlines())} lines) and {a.json_out}; HEAD {head1[:10]}; "
          f"refs moved {moved}; flags {[x['check'] for x in L4 if x['outcome'] == 'FLAG']}")


if __name__ == "__main__":
    main()
