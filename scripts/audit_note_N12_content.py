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
    first 4 characters + '...' + length + ':' + first 8 hex of its sha256
and every excerpt (<= 40 characters) is cut from a line in which every such
span has first been replaced by a placeholder ([EMAIL] [PHONE] [ADDR] [IP]
[CRED] [ID] [TOK] [NAME] [W]).

Stdlib only. Writes exactly one file (the JSON, refuses to overwrite) and a
summary to stdout.

    jlens-qwen36/.venv/bin/python scripts/audit_note_N12_content.py \
        [--rev HEAD] [--json-out results/raw/2026-10-08_note-N12-content-screen.json]
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
    line = line.replace("\t", " ")
    # name_allow is fixed for a whole run (set once after the et-al pass), so the line alone keys the cache.
    if len(_MASK_CACHE) > 4096:
        _MASK_CACHE.clear()
    merged = _MASK_CACHE.get(line)
    if merged is None:
        merged = mask_spans(line, name_allow)
        _MASK_CACHE[line] = merged
    out = []
    cur = 0
    mpos = None
    for s, e, ph, _ in merged:
        if mpos is None and pos < s:
            mpos = len("".join(out)) + (pos - cur)
        out.append(line[cur:s])
        if mpos is None and s <= pos < e:
            mpos = len("".join(out))
        out.append(ph)
        cur = e
    if mpos is None:
        mpos = len("".join(out)) + max(0, pos - cur)
    out.append(line[cur:])
    masked = "".join(out)
    start = max(0, mpos - 10)
    ex = masked[start:start + EXCERPT_MAX]
    ex = "".join(ch if (ch.isprintable() and ch not in "\r\n") else " " for ch in ex)
    return ex.strip()


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

def screen_text(text, name_allow):
    """Return (hits, names, values) for one text. hits: {category: [[line, excerpt, extra]]}."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    hits = defaultdict(list)
    values = []  # (category, subtype, raw value, line) -- raw stays in memory only
    tier_a = 0
    tier_b_lines = []
    tier_b_pairs = set()
    forms = defaultdict(Counter)

    def hit(cat, ln, line, pos, extra):
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
                values.append(("email", cls, e, ln))
                hit("email", ln, line, m.start(), {"class": cls, "redacted": redact(e)})
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
                values.append(("phone", sub, v, ln))
                feat = {"subtype": sub, "shape": shape, "redacted": redact(v)}
                if re.match(r"^[+-]d\.d", shape):
                    feat["shape_tag"] = "signed_decimal"  # mechanical: '+<digit>.<digits>' is a signed decimal number's shape
                hit("phone", ln, line, m.start(), feat)
        # street address
        for sub, rx in ADDR_RXS:
            for m in rx.finditer(line):
                v = m.group(0)
                values.append(("street_address", sub, v, ln))
                hit("street_address", ln, line, m.start(), {"subtype": sub, "redacted": redact(v)})
        # IPv4
        for m in IPV4_RX.finditer(line):
            v = m.group(0)
            cls = ipv4_class(v)
            values.append(("ipv4", cls, v, ln))
            hit("ipv4", ln, line, m.start(), {"class": cls, "redacted": redact(v)})
        # URLs
        for rx in (URL_RX, WWW_RX):
            for m in rx.finditer(line):
                u = m.group(0).rstrip(".,;:")
                h = display_host(url_host(u))
                hit("url", ln, line, m.start(), {"host": h})
        # confidentiality words
        for sub, rx in CONF_RXS:
            for m in rx.finditer(line):
                ctx = "path" if (sub == "private" and m.start() > 0 and line[m.start() - 1] == "/") else "text"
                forms["confidentiality"][m.group(0).lower()] += 1
                hit("confidentiality", ln, line, m.start(), {"word": sub, "context": ctx})
        # correspondence markers
        for sub, rx in CORR_RXS:
            for m in rx.finditer(line):
                hit("correspondence", ln, line, m.start(), {"marker": sub})
        # personal-life markers
        for sub, rx in PERS_RXS:
            for m in rx.finditer(line):
                forms["personal_life"][m.group(0).lower()] += 1
                hit("personal_life", ln, line, m.start(), {"marker": sub, "form": m.group(0).lower()})
        # credential-shaped
        for sub, rx in CRED_RXS:
            for m in rx.finditer(line):
                v = m.group("v") if "v" in rx.groupindex else m.group(0)
                feat = {"subtype": sub, "redacted": redact(v), "len": len(v),
                        "entropy_bits_per_char": round(entropy(v), 2),
                        "has_digit": any(c.isdigit() for c in v),
                        "mixed_case": any(c.isupper() for c in v) and any(c.islower() for c in v)}
                values.append(("credential", sub, v, ln))
                hit("credential", ln, line, m.start(), feat)
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
            values.append(("credential", "generic_high_entropy", v, ln))
            pre = line[max(0, m.start() - 40):m.start()]
            post = line[m.end():m.end() + 3]
            ctx = None
            if re.search(r"/var/folders/[A-Za-z0-9_]{2}/$", pre) or (re.search(r"folders/[A-Za-z0-9_]{2}/$", pre) and post.startswith("/T")):
                ctx = "macos_per_user_temp_dir_component"  # /var/folders/<xx>/<token>/T/...
            elif re.search(r"claude\.ai/code/(?:session_)?$", pre):
                ctx = "claude_ai_session_url_component"
            hit("credential", ln, line, m.start(), {"subtype": "generic_high_entropy", "context": ctx, "redacted": redact(v),
                                                   "len": len(v), "entropy_bits_per_char": round(ent, 2),
                                                   "mixed_case": any(c.isupper() for c in v) and any(c.islower() for c in v)})
        # infrastructure identifiers (supplementary)
        for sub, rx in INFRA_RXS:
            for m in rx.finditer(line):
                v = m.group("v")
                values.append(("infra_identifier", sub, v, ln))
                feat = {"subtype": sub, "redacted": redact(v)}
                if sub == "ssh_key_path" and v in STANDARD_SSH_FILES:
                    feat["standard_openssh_file"] = True  # e.g. the client config file, not a key name
                hit("infra_identifier", ln, line, m.start(), feat)
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
    names = {"tier_a_capitalised_pairs": tier_a,
             "tier_b_given_name_pairs": len(tier_b_lines),
             "tier_b_distinct_pairs": len(tier_b_pairs),
             "tier_b_lines": tier_b_lines}
    return hits, names, values, len(lines), forms


# ---------------------------- main ------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--json-out", default=DEFAULT_OUT)
    ap.add_argument("--selftest", action="store_true", help="run the masking self-test only; writes nothing")
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
    for it in items:
        hits, names, values, nlines, forms = screen_text(it["text"], name_allow)
        hex_skipped += len(hits.pop("_hex_tokens_skipped", []))
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
            "untracked_note": "untracked HANDOFF-*.md files in the working tree are not in any commit, so not in the release unless committed later; listed by name only, not read",
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
            "line_split": "on \\n; 'lines' = number of \\n-separated lines (a trailing newline does not add a line)",
            "excerpt": "<= %d chars of the line after masking every [EMAIL] [PHONE] [ADDR] [IP] [CRED] [ID] [TOK] (alnum/_-+= run >= 20 with a letter and a digit) [NAME] (given-name list word or given-name pair) [W] (one to three words after Dear/Hi/Hello/From:/To:/Cc:/Subject:/Regards/Best,/Cheers,/Thanks, or before wrote:) span; window starts 10 chars before the hit" % EXCERPT_MAX,
            "redacted_form": "first 4 chars + '...' + length + ':' + first 8 hex of sha256(value, utf-8)",
            "email_allowlist": "two addresses (the author's own; Anthropic's noreply) counted under email_allowlisted_counts, never listed as hits",
            "private_context": "confidentiality/private hits immediately preceded by '/' are tagged context=path (e.g. a /private/tmp path); reported, not discounted",
            "multiword_line_break": "multi-word phrases (do not share, not for publication, internal only, off the record, my wife/husband/partner/kid, Sent from) are also matched across a line end and tagged spans_next_line",
            "names": "tier_a: capitalised word pairs, neither word in the name allowlist (counts only); tier_b: tier_a pairs whose first word is in the embedded given-name list (%d names; counts and line numbers only, never the names)" % len(GIVEN_NAMES),
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
    }
    # ---- leak guard: no collected raw value (len >= 5; allowlisted identities excepted) may appear in the output ----
    allowed_verbatim = set(EMAIL_ALLOW) | IDENTITY_NAME_ALLOW
    to_check = sorted(v for v in guard_values if len(v) >= 5 and v.lower() not in allowed_verbatim
                      and v not in allowed_verbatim and v not in STANDARD_SSH_FILES)
    result["leak_guard"] = {"raw_values_checked": len(to_check), "rule": "every collected raw value of length >= 5 (hits and non-allowlisted identity names/emails) asserted absent from the JSON text and the stdout summary before either is written; exempt: the two allowlisted e-mails, the allowlisted identity names, and standard OpenSSH file names %s" % sorted(STANDARD_SSH_FILES)}
    js = json.dumps(result, indent=1, ensure_ascii=False, sort_keys=False) + "\n"

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
    P("leak guard: %d raw values checked against the JSON and this summary" % len(to_check))
    P("wrote %s" % os.path.relpath(out, ROOT))
    text_out = "\n".join(summary)
    leaked = [v for v in to_check if v in js or json.dumps(v, ensure_ascii=False)[1:-1] in js or v in text_out]
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
    print("selftest", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
