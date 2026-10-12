#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12 scrub index (the block's named N12 output, block :84).

Aggregates the committed N12 part raws into one index, one section per sub-item (i)-(vii),
and records the PI's routing of 2026-10-09 against them:

  results/raw/2026-10-08_note-N12-history.{md,json}   @961e90a  (i), (ii), (v), (iv)'s mechanical checks
                                                                (regenerated there; first committed at 09c3a8c)
  results/raw/2026-10-08_note-N12-licenses.{md,json}  @09c3a8c  (iv)
  results/raw/2026-10-08_note-N12-content.md + -content-screen.json   @09c3a8c   (vi)
  results/raw/2026-10-08_note-N12-preflip.{md,json}   @02b6a61  pre-flip reads (server refs, GitHub surfaces)
  results/raw/2026-10-09_note-N12-gitleaks.md         @e0fd85c  (i), the block's primary scanner
  results/raw/2026-10-09_note-N12-password.md         @e0fd85c  (iii)
  LICENSE, LICENSE-CC-BY-4.0, LICENSING.md            @e0fd85c  (iv), added after the licenses part's read

Every part raw is read from its commit with `git show`, never from the working tree; each outcome
and pass line is carried VERBATIM from the line the script finds by content, with a locator
`<path>@<commit>:<line>`. Block locators are pinned to the record commit (default bbc9ffe).
Nothing is re-scanned: no part script is run (re-running them at the release commit is pre-flip
step 3). The only new computations are labelled computed-new: md-vs-JSON agreement of the carried
figures, recounts at the commit a part read, the commits and paths added after each part's commit,
a delta check of the files those commits changed for the history raw's sensitive values, the D1
carrier spread (counts and paths only), the D4 staging state and the other untracked files a later
commit could add (names and tracked status only; no untracked document is opened), the LICENSE
files' hashes, the licenses script on disk compared with HEAD's blob (does it still print its fixed
no-license text, or compute it from the tree; a partial change stops the run), and the pre-flip
script at 02b6a61 compared with HEAD's (its output rule and history-JSON source, located by content). The PI's routing of 2026-10-09 is
recorded as routed to this part (quoted in substance); where a committed raw or commit message
records part of it, the fragment is asserted present and located; where none does, the index says
so. Item 4 of the PI's rulings of 2026-10-09 (the second routing: the N12(i) STOP resolved) is
recorded the same way: its figures are cross-checked against the committed raws, HEAD's tracked
files and commit messages are searched for a committed record of it (none before the commit that
adds this version; the index says so, or locates the records a later run finds), every line of the
index's own text that said (i) was pending now says it is resolved by that ruling (asserted: no
such phrase survives outside a verbatim quote of a raw), and the raws' own pending lines are quoted
unchanged as history. The PI's answer of 2026-10-12 to Code's five N12 pre-flip questions ("Yes to all
five; tag it") is recorded the same way, with Code's housekeeping (not objected) kept as Code's: the
pre-flip items it settles are marked ROUTED with the PI's words, what is still to run stays REMAINS (asserted
on the composed text: each item's status, and no stale "open" phrase outside a verbatim quote); the five files
the answer places in the tag commit are hashed (bytes only, contents not read or restated) against the
hashes Code put to the PI, and the seven release-run scan raws are counted on disk and tracked at HEAD at this
run, both counts printed in the header (they are written at the release commit, R2, with the tag present and
before any push, and committed after the tag, at R3; nothing here asserts their absence). The tag's commit hash
is to be recorded after tagging, in the note's footer (the design seat's, outside Code's release sequence) and in
the post-tag raw Code writes (R3). Section 10 also states Code's release sequence (R1; the scrub index regenerated,
README-NOTE.md made final, N18 re-run and Code's review of the staged R2 files; R2 the tag commit; the tag, local;
the release scans before any push; the push; N11 and the tag record; R3 the post-tag raws, then its push; each
message screened before its commit or tag) as a plan: no step of it is reported as run. The pre-flip read is not
part of that sequence: it runs just before the visibility flip, at the PI's word, after the pre-flip script is
updated for the release names in its own commit then (its committed output rule and history-JSON source are
located here by content). Every figure the index summarizes in its own words is read from a located line by pattern or
asserted present in the line it cites; a mismatch stops the script before it writes.
README-NOTE.md is a sibling part's file: the index names it and does not restate or fingerprint it.

Leak guard: the history JSON lists the values its run treats as sensitive, by redacted form. This
script resolves them in memory from the history text by matching those hash prefixes, never prints
one, and refuses to write if any occurs in its output -- exact, and for values of 8 or more
characters (the session link's bare id included) also ignoring case and every non-alphanumeric
character; digit-bounded for the SSH ports except inside a hex run of 8 or more. Shape checks
(IPv4, session paths, fingerprints, temp paths, 4-5 digit numbers on ssh/port lines) exempt only
a real locator's line number: a backticked `path@commit:line` whose path exists at that commit and
whose line lies within the file. Positive controls inject each resolved value (its distinct case
variants and a separator variant) and one string per shape, plus three locator-shaped non-locators,
into a copy of the output and require a refusal. It also lists every redacted form its output
prints (computed over the text), and refuses to write if one of them is not a form the history
JSON knows, or belongs to a class the history raw lists as recoverable by brute force.

Read-only on the record: git rev-parse / show / ls-tree / ls-files / log / diff / diff-tree / grep /
rev-list / cat-file / for-each-ref / merge-base only; no git command inside jlens-qwen36/; writes
only --out. Never opens HANDOFF-*-design.md or DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md (names
and git tracked status only). Stdlib only.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = 'AUDIT-note-release-v1_2.md'
BLOCK_SHA = '8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841'
HIST_MD = 'results/raw/2026-10-08_note-N12-history.md'
HIST_JSON = 'results/raw/2026-10-08_note-N12-history.json'
LIC_MD = 'results/raw/2026-10-08_note-N12-licenses.md'
LIC_JSON = 'results/raw/2026-10-08_note-N12-licenses.json'
CON_MD = 'results/raw/2026-10-08_note-N12-content.md'
CON_JSON = 'results/raw/2026-10-08_note-N12-content-screen.json'
PF_MD = 'results/raw/2026-10-08_note-N12-preflip.md'
PF_JSON = 'results/raw/2026-10-08_note-N12-preflip.json'
GL_MD = 'results/raw/2026-10-09_note-N12-gitleaks.md'
PW_MD = 'results/raw/2026-10-09_note-N12-password.md'
VC_MD = 'results/raw/2026-10-08_note-tier1_valuescheck.md'
HIST_SCRIPT = 'scripts/audit_note_N12_history.py'
LIC_SCRIPT = 'scripts/audit_note_N12_licenses.py'
CON_SCRIPT = 'scripts/audit_note_N12_content.py'
PF_SCRIPT = 'scripts/audit_note_N12_preflip.py'
GL_SCRIPT = 'scripts/audit_note_N12_gitleaks.py'
PW_SCRIPT = 'scripts/audit_note_N12_password.py'
LIC_FILES = ['LICENSE', 'LICENSE-CC-BY-4.0', 'LICENSING.md']
README_NOTE = 'README-NOTE.md'
LEDGER = ['results/raw/2026-10-08_note-N1-claims-ledger.md', 'results/raw/2026-10-08_note-N1-claims-ledger.json',
          'results/raw/2026-10-09_note-N1-claims-ledger-final.md', 'results/raw/2026-10-09_note-N1-claims-ledger-final.json',
          'results/raw/2026-10-09_note-N1-v0_4-claims-ledger.md', 'results/raw/2026-10-09_note-N1-v0_4-claims-ledger.json',
          'results/raw/2026-10-10_note-N1-v0_5-claims-ledger.md', 'results/raw/2026-10-10_note-N1-v0_5-claims-ledger.json',
          'results/raw/2026-10-12_note-N1-v0_6-claims-ledger.md', 'results/raw/2026-10-12_note-N1-v0_6-claims-ledger.json']
DEFAULT_OUT = 'results/raw/2026-10-08_note-N12-scrub.md'
CITE_NEEDLE = '_note-N12-scrub'   # how a file would name this index
LORA_FORM = 'zebr...20:c63d5fbd'   # the content raw's redacted form (content md :27); asserted there, not printed
# the licenses script's own license-file rule (scripts/audit_note_N12_licenses.py, section 5), asserted verbatim there
LIC_RULE_SRC = r'RX_LF = re.compile(r"(^|/)(LICEN[CS]E|COPYING|NOTICE)(\.[A-Za-z]+)?$", re.I)'
LIC_RULE = re.compile(r"(^|/)(LICEN[CS]E|COPYING|NOTICE)(\.[A-Za-z]+)?$", re.I)

# ---------- the PI's routing of 2026-10-09, as routed to this part (quoted in substance) ----------
ROUTING = '2026-10-09'
D4_COMMIT = ['archive/PROPOSAL-m-gating-campaign-v1_%d.md' % k for k in range(2, 11)]
# D4's keep-out list, as globs over names (names and git tracked status only; never opened)
D4_KEEP_OUT = [('the design-seat handoffs', 'HANDOFF-*-design.md'),
               ('the design-to-Code decisions file', 'DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md'),
               ('the superseded ADDENDUM-g3-b2r drafts', 'ADDENDUM-g3-b2r*.md'),
               ('ADDENDUM-k1', 'ADDENDUM-k1.md'),
               ('the archive/PREPRINT pre-patch copies', 'archive/PREPRINT-v1_0-draft.pre-patch-v*.md')]
# the committed g3-b2r addendum the drafts precede: excluded from the drafts' glob BY NAME (never by tracked
# status, so a draft that were ever committed would still be counted, as tracked)
G3_COMMITTED = 'ADDENDUM-g3-b2r-v1.2.md'
PREPRINT = 'PREPRINT-v1_0-draft.md'
TAG = 'note-2026-10-v1'

# ---------- the PI's rulings of 2026-10-09 (the second routing), item 4, as routed to this part (quoted in substance) ----------
RULINGS = "the PI's rulings of 2026-10-09"
R4 = {'scanner': 'gitleaks 8.30.1', 'findings': 4, 'true_secret_candidates': 0}
R4_SUBSTANCE = ("the N12(i) STOP (block :77) is resolved: %s over all history returned %d findings, all false positives under "
                "fingerprint-keyed triage; Code's own scans found %d true-secret candidates; the PI accepts Code's scans as the "
                "resolution of the literal grep rule, which was over-written; D1 stands (history as is)") % (
    R4['scanner'], R4['findings'], R4['true_secret_candidates'])
# read back from the composed text for the section-12 cross-check (the recording, not the constant, is checked)
R4_RX = re.compile(r"(gitleaks [0-9.]+) over all history returned (\d+) findings, all false positives under fingerprint-keyed "
                   r"triage; Code's own scans found (\d+) true-secret candidates;")
R4_NEEDLE = 'rulings of 2026-10-09'   # how a committed record of the rulings would name them (case-insensitive)
R4_MARK = 'N12(i)'                    # ... and of this item
# working-tree audit outputs named in the routing that record item 4 (cited by content while untracked or changed)
R4_WT = ['results/raw/2026-10-09_note-N1-v0_4-claims-ledger.md']
# the N1 v0.4 ledger's own label for the ruling (asserted on the line it is cited from; its other R4 lines are then listed)
R4_LABEL = 'R4, the N12(i) STOP resolved'
# the first of the tag conditions the N1 v0.6 ledger's 9g leaves to the PI (located by content in N1_LEDGER); the PI's
# answer of 2026-10-12, question (5), decides it
N1_LEDGER = 'results/raw/2026-10-12_note-N1-v0_6-claims-ledger.md'
N1_9G_FRAG = "Conditions that are the PI's to keep: (1) the tag commit also contains the note, the three 2026-10-10 SVGs and the patched preprint"
# the earlier notes and renders at root, which the tag commit's note v0.6 and 2026-10-10 renders follow (names only)
SUPERSEDED = ['RESEARCH-NOTE-v0_3-draft.md', 'RESEARCH-NOTE-v0_4-draft.md', 'RESEARCH-NOTE-v0_5-draft.md',
              '2026-10-06_F1b_five-link-panels.svg', '2026-10-06_F2_macar-lineage-roc_post.svg',
              '2026-10-09_F1a_headline-strip.svg', '2026-10-09_F1b_five-link-panels.svg', '2026-10-09_F2_macar-lineage-roc_post.svg']
# a later commit's message on what README-NOTE.md carries of D1-D4 (asserted under that message's README-NOTE.md bullet)
README_D_FRAG = 'N12 (i) and (iii) and D1-D4 as routed'
# a later commit's message recording a password scan over its own files (one sentence, carried verbatim)
PW_AFTER_RX = re.compile(r"[A-Z][^.\n]*\bpassword\b[^.\n]*\bscans? over\b[^.\n]*\.")
# the index's own words that said (i) was pending; none may survive outside a verbatim quote of a raw
R4_FORBIDDEN = ['STOP pending', 'stands until the PI resolves', 'does not resolve (i)', "(i)'s resolution by the PI",
                "remains the PI's act", 'does not pass at this index', 'STOP open', 'until the PI resolves']

# ---------- the PI's answer of 2026-10-12 to Code's five N12 pre-flip questions, as routed to this part ----------
ANSWER = "the PI's answer of 2026-10-12"
ANSWER_TEXT = 'Yes to all five; tag it'   # verbatim
# the tag commit's files, as question (5) names them: (path, the sha256 as Code put it: prefix, suffix or full)
TAG_FILES = [('RESEARCH-NOTE-v0_6-draft.md', '2c7e1cf5', '6fbb'),
             ('2026-10-10_F1a_headline-strip.svg', '6ffad6cd', ''),
             ('2026-10-10_F1b_five-link-panels.svg', '6fcb060f', ''),
             ('2026-10-10_F2_macar-lineage-roc_post.svg', '81b13e80', ''),
             ('PREPRINT-v1_0-draft.md', 'd9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6', '')]
# Code's five questions, as Code put them (quoted in substance)
ANSWER_QS = [
    "(1) accept the fix to the N12 content script's leak guard, which fires on the script's own earlier output",
    "(2) confirm the N12 licenses script's rule changes, which classify the ids and hosts carried by the audit's own files "
    "(fragments of recorded-read URLs and prefixes of this repository's id count as known ids; claude.ai only outside audit "
    "files; model-output hosts may also have audit-file carriers; hosts carried only by audit files are classed; "
    "transformer-circuits.pub gains two allowed paths)",
    "(3) ruling 4 (%s, item 4, which resolved N12 (i)) covers the release run's (i) (0 true-secret candidates, 0 untriaged)" % RULINGS,
    "(4) gitleaks' default skip of `.svg` files and trufflehog not run are acceptable",
    "(5) the tag commit holds note v0.6 (`%s`, sha256 `%s...%s`) and the three 2026-10-10 renders (%s) beside the preprint "
    "(`%s`, patch v7, sha256 `%s`)" % (
        TAG_FILES[0][0], TAG_FILES[0][1], TAG_FILES[0][2],
        ', '.join('`%s` `%s...`' % (p, a) for p, a, _ in TAG_FILES[1:4]), TAG_FILES[4][0], TAG_FILES[4][1])]
# Code's housekeeping, which Code said it would do unless the PI objected (no objection): Code's, not the PI's
GL_FP = ('f23b44408daf516552c0d11414c646ea0dd6213f', 'data/m/gates/G-SHAPE-F0.json', 378, 'valence_core/m/keys.py')
HOUSEKEEPING = [
    "the history script's triage entries (10 entries, and the public hosts `www.apache.org`, `c2pa.org` and `purl.org`), prepared in round 9",
    "the release run excludes the D4 files (`HANDOFF-*-design.md`, `DESIGN-to-CODE-*.md`) by name, never opened",
    "it writes new dated raws rather than overwriting committed ones",
    "the gitleaks hit at `%s` `%s:%d` (the sha256 of `%s`, flagged on the word 'keys') is triaged FALSE-POSITIVE" % (
        GL_FP[0][:10], GL_FP[1], GL_FP[2], GL_FP[3])]
# the release run's new dated raws, by the script that writes them: the seven scan raws (history, content, licenses,
# gitleaks, password), written at the release commit (R2) with the tag present, before any push, and committed after the
# tag (R3). The pre-flip read is not part of the release sequence: it runs just before the visibility flip, at the PI's
# word, after the pre-flip script is updated for the release names in its own commit then; its raws are named in that
# commit, not here.
RELEASE_RAWS = [('history', ['results/raw/2026-10-12_note-N12-history-release.md', 'results/raw/2026-10-12_note-N12-history-release.json']),
                ('content', ['results/raw/2026-10-12_note-N12-content-screen-release.json']),
                ('licenses', ['results/raw/2026-10-12_note-N12-licenses-release.md', 'results/raw/2026-10-12_note-N12-licenses-release.json']),
                ('gitleaks', ['results/raw/2026-10-12_note-N12-gitleaks-release.md']),
                ('password', ['results/raw/2026-10-12_note-N12-password-release.md'])]
RR = dict(RELEASE_RAWS)
TAG_RAW = 'results/raw/2026-10-12_note-release-tag.md'   # the post-tag raw, written by Code, that records the tag's commit hash
# Code's release sequence (a plan, stated in section 10; nothing here reports a step of it as run)
R1_SCRIPTS = ['scripts/audit_note_N12_history.py', 'scripts/audit_note_N12_content.py',
              'scripts/audit_note_N12_licenses.py', 'scripts/audit_note_N12_gitleaks.py']
N18_SCRIPT = 'scripts/audit_note_N18.py'
MANIFEST = ['results/raw/2026-10-09_note-release-manifest.json', 'results/raw/2026-10-09_note-release-manifest.md']
N11_SCRIPT = 'scripts/audit_note_N11.py'
N11_TAG_RAW = 'results/raw/2026-10-12_note-N11-smoke-tag.txt'
PREFLIP_SCRIPT = 'scripts/audit_note_N12_preflip.py'
# the pre-flip script as committed: its output rule and the history JSON it compares against (located by content)
PFS_OWN_ONLY = 'raise SystemExit(f"refusing an output other than this script\'s own two files: {o}")'
PFS_HIST_JSON = 'HIST_JSON = "%s"' % 'results/raw/2026-10-08_note-N12-history.json'
# the pre-flip raw's own words for the repeat (item 2), asserted present in the line it cites
PF2_REPEAT = 'Repeat at the release commit, immediately before the visibility change'
# the licenses script on disk: the release version computes the repository's license statements from the tree
LS_WT_COMPUTED = ('"repo_licensed_at_commit": repo_licensed,', '"rule_repo_licensed": "every root-level license text is identified by "')
# the index's own words that said a decision the answer settles was open; none may survive outside a verbatim quote
ANS_FORBIDDEN = ['tag still waits on patch v6', 'after patch v6 is applied (item 6)', "the PI's word on trufflehog",
                 "or the PI's word that the per-file passes", 'is settled neither by the routing nor by',
                 'it does not say whether it also covers', 'is not routed to this part', 'Patch v6** -- **REMAINS',
                 'still open as routed', 'patch v6 and the preprint commit (item 6)']


def git(*args, binary=False, ok=(0,), inp=None):
    if os.path.realpath(os.getcwd()).startswith(os.path.join(os.path.realpath(REPO), 'jlens-qwen36')):
        raise SystemExit('refusing to run git inside jlens-qwen36/')
    r = subprocess.run(['git', '-C', REPO, *args], capture_output=True, input=inp)
    if r.returncode not in ok:
        raise SystemExit('git %s failed: %s' % (' '.join(args), r.stderr.decode(errors='replace')))
    return r.stdout if binary else r.stdout.decode('utf-8', errors='replace')


def sha256b(b):
    return hashlib.sha256(b).hexdigest()


def yn(x):
    return 'yes' if x else 'NO'


class Doc:
    """A part raw read at a commit, with content-anchored line lookup."""

    def __init__(self, commit, short, path):
        self.path, self.short = path, short
        self.raw = git('show', '%s:%s' % (commit, path), binary=True)
        self.lines = self.raw.decode('utf-8').split('\n')

    def find(self, pred, desc, unique=True, start=0, end=None):
        hits = [i + 1 for i, ln in enumerate(self.lines[start:end], start) if pred(ln)]
        if not hits or (unique and len(hits) != 1):
            raise SystemExit('anchor %r in %s: %d hits' % (desc, self.path, len(hits)))
        return hits[0]

    def sw(self, prefix, **kw):
        return self.find(lambda s: s.startswith(prefix), prefix, **kw)

    def has(self, sub, **kw):
        return self.find(lambda s: sub in s, sub, **kw)

    def line(self, n):
        return self.lines[n - 1]

    def loc(self, n, n2=None):
        return '`%s@%s:%s`' % (self.path, self.short, n if n2 is None else '%d-%d' % (n, n2))

    def need(self, n, *subs):
        """Assert that each summarized fragment is present in the cited line; return the line."""
        s = self.line(n)
        for sub in subs:
            if sub not in s:
                raise SystemExit('summary not backed by %s:%d: %r' % (self.path, n, sub))
        return s

    def num(self, n, pattern, group=1):
        m = re.search(pattern, self.line(n))
        if not m:
            raise SystemExit('pattern %r not in %s:%d' % (pattern, self.path, n))
        return m.group(group)


def section_end(doc, start):
    for i in range(start, len(doc.lines)):
        if doc.lines[i].startswith('## '):
            return i
    return len(doc.lines)


# ---------- sensitive-value resolution (in memory; never printed) ----------
FORM_PREFIX = re.compile(r'^(.{1,4})\.\.\.\[len (\d+)\]#([0-9a-f]{8})$')
FORM_DIGITS = re.compile(r'^len(\d+):([0-9a-f]{8})$')
# a redacted form printed in running text: `xxxx...[len N]#hhhhhhhh`, `xxxx...N:hhhhhhhh` or `lenN:hhhhhhhh`
FORM_IN_TEXT = re.compile(r'(?<![A-Za-z0-9])(?:[A-Za-z0-9]{1,4}\.\.\.(?:\[len (\d+)\]#|(\d+):)([0-9a-f]{8})'
                          r'|len(\d+):([0-9a-f]{8}))(?![0-9a-f])')


def form_key(form):
    """(length, sha256 prefix) of a redacted form in either the history's or the content raw's notation."""
    m = FORM_PREFIX.match(form)
    if m:
        return int(m.group(2)), m.group(3)
    m = FORM_DIGITS.match(form)
    if m:
        return int(m.group(1)), m.group(2)
    m = FORM_IN_TEXT.fullmatch(form)
    if m:
        n = m.group(1) or m.group(2) or m.group(4)
        return int(n), m.group(3) or m.group(5)
    return None


def resolve_values(forms, text):
    found, digit_cache = {}, {}
    for form in forms:
        m = FORM_PREFIX.match(form)
        if m:
            pre, n, h = m.group(1), int(m.group(2)), m.group(3)
            i = text.find(pre)
            while i != -1:
                cand = text[i:i + n]
                if len(cand) == n and hashlib.sha256(cand.encode()).hexdigest().startswith(h):
                    found[form] = cand
                    break
                i = text.find(pre, i + 1)
            continue
        m = FORM_DIGITS.match(form)
        if m:
            n, h = int(m.group(1)), m.group(2)
            if n not in digit_cache:
                digit_cache[n] = set(re.findall(r'(?<![0-9])[0-9]{%d}(?![0-9])' % n, text))
            for cand in digit_cache[n]:
                if hashlib.sha256(cand.encode()).hexdigest().startswith(h):
                    found[form] = cand
                    break
    return found


def count_value(form, value, text):
    """Exact count, as the delta check and the D1 spread use it (ports alnum-bounded)."""
    if FORM_DIGITS.match(form):
        return len(re.findall(r'(?<![0-9A-Za-z])%s(?![0-9A-Za-z])' % re.escape(value), text))
    return text.count(value)


def _norm(s):
    """Case-folded, with every character other than a letter or digit removed (hyphens, underscores,
    whitespace, dots, colons, slashes and all other punctuation)."""
    return re.sub(r'[^0-9a-z]', '', s.lower())


def guard_count(value, text, digits):
    """The leak guard's matcher: stricter than count_value.

    Digits (the SSH ports): digit-bounded, skipping a match inside a run of 8+ hex characters
    (a digest, where a port's digits can occur by chance). Other values: exact count, plus, for values
    of 8 or more characters, a match that ignores case and every non-alphanumeric character (_norm)."""
    if digits:
        n = 0
        for m in re.finditer(r'(?<![0-9])%s(?![0-9])' % re.escape(value), text):
            a, b = m.start(), m.end()
            while a > 0 and text[a - 1] in '0123456789abcdefABCDEF':
                a -= 1
            while b < len(text) and text[b] in '0123456789abcdefABCDEF':
                b += 1
            if b - a < 8:
                n += 1
        return n
    n = text.count(value)
    if len(value) >= 8 and _norm(value) in _norm(text):
        n = max(n, 1)
    return n


GUARD_SHAPES = [
    ('IPv4 literal', re.compile(r'(?<![\d.])(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}'
                                r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?![\d.])')),
    ('claude.ai session/artifact path', re.compile(r'claude\.ai/(?:code|chat|share|artifact)')),
    ('SSH SHA256 fingerprint shape', re.compile(r'SHA256:[A-Za-z0-9+/]{43}')),
    ('local temp or transcript-store path', re.compile(r'/private/tmp/|/private/var/folders/|\.claude/projects/[-A-Za-z0-9]')),
    # a bare 4-5 digit number (not part of a date, path, hash, identifier or decimal; a 4-digit
    # number in 1900-2099 is read as a year) on an ssh/port line
    ('4-5 digit number on an ssh/port line', re.compile(
        r'(?im)^(?=.*\b(?:ssh|port|ports)\b).*(?<![0-9A-Za-z._/-])(?!(?:19|20)[0-9]{2}(?![0-9]))'
        r'[0-9]{4,5}(?![0-9A-Za-z_/-]|\.[0-9])')),
]
# A line number inside a locator is not a port: masked for the shape check only, and only for a real locator --
# a backticked `path@commit:line` (or `(path@commit:line`, or a `:line-line` range), directly after the opening
# backtick, closed by a backtick, comma or parenthesis, whose path exists at that commit (`git cat-file`) and
# whose line (and range end) lies within that file. Anything else of the shape `x@hex:digits` is left unmasked.
LOCATOR_CAND = re.compile(r'(?:(?<=`)|(?<=`\())([A-Za-z0-9_][A-Za-z0-9_./-]*)@([0-9a-f]{7,40}):(\d+)(?:-(\d+))?(?=[`,)])')
_LOC_LINES = {}


def locator_lines(path, commit):
    """Line count of `path` at `commit`, or None if that blob does not exist (cached; read-only cat-file)."""
    k = (path, commit)
    if k not in _LOC_LINES:
        if os.path.realpath(os.getcwd()).startswith(os.path.join(os.path.realpath(REPO), 'jlens-qwen36')):
            raise SystemExit('refusing to run git inside jlens-qwen36/')
        r = subprocess.run(['git', '-C', REPO, 'cat-file', '-p', '%s:%s' % (commit, path)], capture_output=True)
        b = r.stdout
        _LOC_LINES[k] = None if r.returncode != 0 else nlines(b)
    return _LOC_LINES[k]


def mask_locators(t):
    def sub(m):
        n = locator_lines(m.group(1), m.group(2))
        a_ = int(m.group(3))
        b_ = int(m.group(4)) if m.group(4) else None
        if n is None or not 1 <= a_ <= n or (b_ is not None and not a_ <= b_ <= n):
            return m.group(0)
        return '%s@%s:%s%s' % (m.group(1), m.group(2), '#' * len(m.group(3)), ('-' + '#' * len(m.group(4))) if m.group(4) else '')
    return LOCATOR_CAND.sub(sub, t)


def nlines(b):
    """Lines in a blob: newlines, plus one for a final line without a trailing newline."""
    return b.count(b'\n') + (1 if b and not b.endswith(b'\n') else 0)


EXPOSURE_HEADS = ('Recoverable by brute force:', 'Open to a word-list search:', 'Not recoverable by brute force:')


def exposure_of(caveat_line, label):
    """Which of the history caveat's three exposure lists names this class (by its short label)."""
    short = label.split(' (')[0]
    pos = {hd: caveat_line.find(hd) for hd in EXPOSURE_HEADS}
    if any(p < 0 for p in pos.values()):
        raise SystemExit('history caveat line lacks an exposure heading')
    order = sorted(pos.items(), key=lambda kv: kv[1])
    for k, (hd, p) in enumerate(order):
        end = order[k + 1][1] if k + 1 < len(order) else len(caveat_line)
        if (short + ' (') in caveat_line[p:end]:
            return hd.rstrip(':')
    raise SystemExit('class %r in no exposure list of the history caveat' % short)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--audit', default='09c3a8c', help='commit holding the licenses and content part raws and the values-check record')
    ap.add_argument('--hist', default='961e90a', help='commit holding the regenerated history part raw')
    ap.add_argument('--preflip', default='02b6a61', help='commit holding the pre-flip part raw')
    ap.add_argument('--routing', default='e0fd85c', help="commit holding the 2026-10-09 part raws and the LICENSE files")
    ap.add_argument('--pin', default='bbc9ffe', help='record pin for block locators')
    ap.add_argument('--out', default=DEFAULT_OUT)
    a = ap.parse_args()

    stamp = subprocess.run(['date', '-u'], capture_output=True, text=True).stdout.strip()
    head = git('rev-parse', 'HEAD').strip()
    full = {}
    for k in ('pin', 'audit', 'preflip', 'hist', 'routing'):
        full[k] = git('rev-parse', getattr(a, k) + '^{commit}').strip()
    pin, audit, pfc, hic, roc = full['pin'], full['audit'], full['preflip'], full['hist'], full['routing']
    P, A, PFs, Hs, Rs = a.pin, a.audit, a.preflip, a.hist, a.routing
    order = [pin, audit, pfc, hic, roc, head]
    for x, y in zip(order, order[1:]):
        git('merge-base', '--is-ancestor', x, y)   # raises unless the commits are in this order on HEAD

    # ---------- block ----------
    blk_raw = git('show', '%s:%s' % (pin, BLOCK), binary=True)
    blk_sha = sha256b(blk_raw)
    wt_path = os.path.join(REPO, BLOCK)
    blk_wt = sha256b(open(wt_path, 'rb').read()) if os.path.exists(wt_path) else None
    blk = Doc(pin, P, BLOCK)
    assert blk_sha == BLOCK_SHA, 'block sha mismatch at pin'
    b = {
        'n12': blk.sw('### N12. Release scrub'),
        'i': blk.sw('(i) Secrets over the *entire history*'),
        'ii': blk.sw('(ii) Identifiers:'),
        'iii': blk.sw('(iii) The continuity password.'),
        'iv': blk.sw('(iv) Third-party materials and licenses:'),
        'v': blk.sw('(v) Size:'),
        'vi': blk.sw('(vi) Content review'),
        'vii': blk.sw('(vii) Produce the README-for-readers'),
        'out': blk.sw('*Output:* `results/raw/<stamp>_note-N12-scrub.md`'),
        'pass': blk.sw('*Pass:* (i) no hits, or hits resolved by the PI'),
        's6': blk.sw('## 6. README-for-readers'),
        's7': blk.sw('## 7. What this block does not do'),
    }
    b['s6_body'] = b['s6'] + 2
    assert blk.line(b['s6_body']).startswith('A short file at the tag, `README-NOTE.md`')
    blk.need(b['iii'], 'Not a release blocker', 'If present anywhere, report the file and commit')
    blk.need(b['i'], 'Any hit in history is a STOP on the release: history rewriting is a PI decision.')
    # the literal grep rule the PI's rulings of 2026-10-09, item 4, name: block :77's fallback grep
    R4_GREP = "otherwise `git log -p --all | grep -nEi"
    blk.need(b['i'], R4_GREP)
    b['s7_body'] = blk.find(lambda s: 'it does not decide the tag name, the release date or history rewriting' in s,
                            'block s7 body', start=b['s7'])
    block_pass = blk.line(b['pass'])
    # block :133: the tag commit hash is to be printed in the note's footer (the footer is the design seat's)
    b['footer'] = blk.has("the tag commit hash, both to be printed in the note's footer")

    # ---------- part raws ----------
    H = Doc(hic, Hs, HIST_MD)
    L = Doc(audit, A, LIC_MD)
    C = Doc(audit, A, CON_MD)
    VC = Doc(audit, A, VC_MD)
    PF = Doc(pfc, PFs, PF_MD)
    # the pre-flip script as committed at the pre-flip raw's commit, and whether HEAD still holds that version
    PFS = Doc(pfc, PFs, PF_SCRIPT)
    pfs_own, pfs_hist = PFS.has(PFS_OWN_ONLY), PFS.sw(PFS_HIST_JSON)
    pfs_same = sha256b(git('show', '%s:%s' % (head, PF_SCRIPT), binary=True)) == sha256b(PFS.raw)
    G = Doc(roc, Rs, GL_MD)
    PW = Doc(roc, Rs, PW_MD)
    hj = json.loads(git('show', '%s:%s' % (hic, HIST_JSON)))
    lj = json.loads(git('show', '%s:%s' % (audit, LIC_JSON)))
    cj_raw = git('show', '%s:%s' % (audit, CON_JSON), binary=True)
    cj = json.loads(cj_raw)
    pfj = json.loads(git('show', '%s:%s' % (pfc, PF_JSON)))
    # the history raw's own commits (first committed, then regenerated)
    hist_commits = git('log', '--format=%H', head, '--', HIST_MD).split()
    if hic not in hist_commits:
        raise SystemExit('the history raw was not changed at %s' % Hs)
    hist_first = hist_commits[-1]
    hj_first = json.loads(git('show', '%s:%s' % (hist_first, HIST_JSON)))

    h = {
        'head': H.sw('- HEAD:'), 'referent': H.sw('- Referent note:'),
        'coverage': H.sw("- Coverage of the commits after the block's commit"),
        'caveat': H.sw('- Caveat (enumeration'), 'scope': H.sw('## Scope'),
        'i': H.sw('## (i) Secrets over the entire history'),
        'scanners': H.sw("**The block's primary scanners have NOT been run"),
        'passphrase': H.sw('**Pass-phrase-shaped text (hard rule 5):**'),
        'continuity_md': H.sw('`CONTINUITY.md`'), 'continuity': H.sw('The word `continuity`'),
        'i_pass': H.sw('**Pass/STOP line (i):**'), 'ii': H.sw('## (ii) Identifiers'),
        'identities': H.sw('### Commit identities'), 'classes': H.sw('### Identifier classes in content'),
        'ids_head': H.sw('**Identifiers present at HEAD**'),
        'fixture': H.sw('IDENTIFIER values in tracked code (.py/.sh) at HEAD:'),
        'users': H.sw('### Tracked files at HEAD containing `/Users/`'),
        'users_rec': H.sw('Recommendation: none of these files needs a change before release'),
        'workspace': H.sw('### Tracked files at HEAD containing `/workspace/`'),
        'v': H.sw('## (v) Size'), 'preflip': H.sw('**PI pre-flip steps'),
        'pf1': H.sw('1. **A precondition of the end commit and the tag'),
        'pf2': H.sw('2. `git ls-remote origin`'), 'pf3': H.sw('3. GitHub-side surfaces'),
        'pf4': H.sw("4. The block's primary scanners"),
        'v_pass': H.sw('**Pass/STOP line (v):**'), 'iv': H.sw('## (iv) mechanical checks'),
        'floats': H.sw('Reading of the float arrays'),
        'pre': H.sw('## Pre-release check: files not yet in history'),
        'pre_pi': H.sw("| other untracked or modified files (the PI's documents) |"),
        'pre_line': H.sw('**Pre-release line, redaction-rule values**'),
        'pre_ident': H.sw("**Pre-release line, the commit identities' own metadata**"),
        'summary': H.sw('## Summary lines'), 's_i': H.sw('- (i): STOP pending'),
        's_ii': H.sw('- (ii): RunPod pod ids'), 's_v': H.sw('- (v): PASS'),
        's_iv': H.sw('- (iv)-mechanical:'), 's_pre': H.sw('- Pre-release (files not yet in history'),
        'vc1': H.sw('## Values-check', unique=False), 'vc4': H.sw('## Values-check, round 4'),
        'vc5': H.sw('## Values-check, round 5'), 'vc5b': H.sw('### Round 5, second check'),
        'vc5_ctrl': H.sw('Second-check controls: ALL PASS'), 'interim': H.sw('This is an interim snapshot at HEAD'),
        'untri5': H.sw('**Untriaged at this run** (all tables)'),
    }
    lc = {
        'part': L.sw('- Part raw for N12(iv).'), 'commit': L.sw('- Commit read:'),
        'scope_time': L.sw('- Scope in time:'), 's1': L.sw('## 1. Macar et al. materials'),
        'proj': L.sw("**Once this audit's own working files are tracked.**"),
        's5': L.sw("## 5. The repository's own license"), 's6': L.sw('## 6. Licenses and third-party materials'),
        's7': L.sw('## 7. For the PI'), 'it1': L.sw('1. **Macar materials'),
        'it2': L.sw('2. **The repository has no license.**'), 'it5': L.sw('5. **The Jacobian lenses**'),
        'it6': L.sw('6. **Refs not visible locally.**'), 'it7': L.sw('7. **The Global Workspace paper**'),
        'it8': L.sw('8. **Moving HEAD.**'), 'pass': L.sw('**(iv) licenses recorded**'),
        'vc': L.sw('## Values-check'),
    }
    cc = {
        'head': C.sw('- HEAD:'), 'screen': C.sw('- Mechanical screen:'), 's0': C.sw('## 0. Result and pass line'),
        'pass': C.sw('**Expected: nothing; found: nothing'), 'count': C.sw('**File count reviewed:'),
        'dec': C.sw('Decisions for the PI.'), 'd1': C.sw('- **D1 ('), 'd2': C.sw('- **D2 ('),
        'd3': C.sw('- **D3 ('), 'd4': C.sw('- **D4 ('), 's4': C.sw('## 4. Flags that survived refutation'),
        'd1rec': C.sw('**Recommendation (D1,'), 'fixture': C.sw('Separately, the `resume.py` fixture'),
        's52': C.sw("### 5.2 For the PI's continuity-password comparison"),
        's53': C.sw('### 5.3 Commit metadata'), 's54': C.sw('### 5.4 Release staging hazard'),
        'nocommit': C.has('design documents has 0 commits on `--all`', start=C.sw('### 5.4 Release staging hazard')),
        'd4rec': C.sw('**Recommendation (D4).**'), 's7': C.sw('## 7. Not reviewed'),
        'untracked': C.sw('**Untracked at root and in archive/.**'),
        'rerun': C.sw('Each part works under the same redaction rule. Recommendation: before the push'),
        's8': C.sw('## 8. Hand-offs to the scrub raw'), 'host': C.sw('- **Hostnames**'), 'ssh': C.sw('- **SSH:**'),
        'users': C.sw('- **/Users/ paths:**'), 'stale': C.sw('- **Stale statements that the repo is private:**'),
        'h_iii': C.sw('- **N12(iii):**'), 'h_iv': C.sw('- **N12(iv):**'),
        's9': C.sw('## 9. Round 2: refuter verdicts'), 'totals': C.sw('**Totals.** 20 verdicts'),
        'outside': C.sw("**Outside N12(vi)'s scope (results/raw + HANDOFF), and not content-reviewed here.**"),
    }
    pf = {
        'stamp': PF.sw('- Code stamp'), 'head': PF.sw('- HEAD at start'), 'script': PF.sw('- Script:'),
        's1': PF.sw('## 1. Server-side refs'), 'srv': PF.sw('- Server refs with no local counterpart: 0.'),
        's2': PF.sw('## 2. GitHub-side surfaces'), 'proj_row': PF.sw('| projects (v2) linked to the repository |'),
        's3': PF.sw('## 3. Interim history scan at HEAD'), 's4': PF.sw('## 4. Pass / flag lines'),
        's5': PF.sw('## 5. What remains for the PI before the visibility flip'), 's7': PF.sw('## 7. Values-check'),
        'p1': PF.sw('- PASS -- **(1) server refs**'), 'p2i': PF.sw('- NOT READ -- **(2i) projects (v2)**'),
        'p2b': PF.sw('- PASS -- **(2b) pull requests and comments**'), 'p2k': PF.sw('- PASS -- **(2k) text screen'),
        'p3a': PF.sw('- FLAG -- **(3a) history script at HEAD**'),
    }
    PF.need(pf['proj_row'], 'INSUFFICIENT_SCOPES')
    PF.need(pf['p2i'], 'not readable with the CLI\'s scopes; the PI checks the Projects tab')
    PF.need(pf['p3a'], 'refused to write', "step 3 cannot pass with the committed script as it stands")
    PF.need(pf['p1'], 'refs/pull/* 0')
    pf_head = pfj['head_start']
    assert pfj['head_end'] == pf_head and pf_head in PF.line(pf['head'])
    pf_rem = {}
    for e in pfj['remaining']:
        pf_rem[e['item']] = PF.sw('%d. **%s**' % (e['item'], e['status']), start=pf['s5'])
        PF.need(pf_rem[e['item']], e['locator'])
    pf_p2_first = PF.sw('- INFO -- **(2a) visibility**')
    pf_p2_last = pf['p2k']
    g = {
        'head': G.sw('- Code stamp:'), 'script': G.sw('- Script'), 'cmd': G.sw('- gitleaks 8.30.1 (installed by the PI)'),
        'commits': G.has('INF 311 commits scanned.'), 'leaks': G.has('WRN leaks found:'),
        'pi': G.sw("- The PI's report (routing of 2026-10-09)"), 'out': G.sw('## Outcome'),
        'tbl': G.sw('| # | rule | file | commit | line |'),
        'o1': G.sw('- Findings:'), 'o2': G.sw('- Two of the findings are in this audit'),
        'o3': G.sw('- Block :77 makes any hit in history a STOP'),
    }
    G.need(g['o3'], "the PI's D1 routing (2026-10-09) is to leave history as is", "Resolving (i) remains the PI's act",
           'trufflehog was not run (not installed)')
    G.need(g['cmd'], '--log-opts=--all', '--redact=100')
    G.need(g['pi'], '"gitleaks over all history found 4 leaks". This run finds 4.')
    pw = {
        'stamp': PW.sw('- Code stamp:'), 'ref': PW.sw('- Ref:'), 'script': PW.sw('- Script:'), 'value': PW.sw('- The value:'),
        'r1': PW.sw('- (1) Tracked files at the ref'), 'r2': PW.sw('- (2) Blobs reachable from any ref'),
        'r3': PW.sw('- (3) Commit messages scanned:'), 'r4': PW.sw('- (4) Untracked, not-ignored working-tree files'),
        'absent': PW.sw('**Absent** from every tracked file at the ref'),
        'present': PW.sw('**Present in untracked working-tree files**'),
        'd2': PW.sw("The PI's D2 routing (2026-10-09) closes the LoRA phrase as 'no match'."),
    }
    PW.need(pw['value'], 'It is written nowhere, and neither is its length or any hash of it.')
    PW.need(pw['absent'], "Block :79's condition ('if present anywhere') does not arise for the history.")
    PW.need(pw['present'], 'A commit that adds them would put it in the record. Stage by explicit path.')
    PW.need(pw['r1'], ': 0 hit line(s).')
    pw_blobs = int(PW.num(pw['r2'], r'scanned by content: (\d+) blobs'))
    PW.need(pw['r2'], '; 0 blob(s) contain it.')
    pw_msgs = int(PW.num(pw['r3'], r'Commit messages scanned: (\d+); with it: 0\. Tag annotations with it: 0\.'))
    pw_untr = int(PW.num(pw['r4'], r'scanned: (\d+); with it: \d+'))
    pw_with = int(PW.num(pw['r4'], r'; with it: (\d+)\.'))
    pw_files = []
    for k in range(1, pw_with + 1):
        mm = re.match(r'^  - `([^`]+)`, lines \[[0-9, ]+\]$', PW.line(pw['r4'] + k))
        if not mm:
            raise SystemExit('password raw: file row %d not at :%d' % (k, pw['r4'] + k))
        pw_files.append((mm.group(1), pw['r4'] + k))
    if not all(re.fullmatch(r'HANDOFF-[0-9-]+-design\.md', f) for f, _ in pw_files):
        raise SystemExit('password raw: a file with it is not a design-seat handoff')
    pw_ref = re.search(r'`([0-9a-f]{40})`', PW.line(pw['ref'])).group(1)
    PWS = Doc(roc, Rs, PW_SCRIPT)
    pws_scope = PWS.has('(4) every untracked, not-ignored file in the working tree (the files a')
    PWS.need(pws_scope + 1, 'later commit could add), plus any --extra paths.')
    gl_head = re.search(r'HEAD `([0-9a-f]{40})`', G.line(g['head'])).group(1)

    # content §7's known carriers outside N12(vi)'s scope, handed to the N12(ii) list
    C.need(cc['outside'], 'Known carriers outside scope, for the N12(ii) list:')
    out_carriers = [
        ('- RESULTS.md: the pod id, volume id and volume name', 'RESULTS.md (the D1 values)'),
        ('- `valence_core/m/resume.py:1132,1135`: the pod-id fixture', '`valence_core/m/resume.py` (the pod-id fixture)'),
        ('- `archive/RESULTS-cycle1-2.md`: the LoRA phrase', '`archive/RESULTS-cycle1-2.md` (the LoRA phrase)'),
        ('- `paper_analysis.ipynb`: the conda environment name, per the refuter',
         '`paper_analysis.ipynb` (the conda environment name, per the refuter)'),
    ]
    for k, (src, _) in enumerate(out_carriers, 1):
        if C.line(cc['outside'] + k) != src:
            raise SystemExit('content raw: outside-scope carrier %d not at :%d' % (k, cc['outside'] + k))
    cc['f44'] = C.sw('| F44 |', start=cc['s52'], end=cc['s53'])
    cc['f46'] = C.sw('| F46, F53 |', start=cc['s53'], end=cc['s54'])
    # the two bullets that complete the content raw's section-0 pass statement
    c_bul = [cc['pass'] + 1, cc['pass'] + 2]
    assert all(C.line(n).startswith('- **') for n in c_bul)
    vc = {'h': VC.sw('## N12-history'), 'l': VC.sw('## N12-licenses'), 'c': VC.sw('## N12(vi) content review')}
    vc_open, vc_passes, vc_end = {}, {}, {}
    for k in ('h', 'l', 'c'):
        end = vc_end[k] = section_end(VC, vc[k])
        vc_open[k] = [i + 1 for i in range(vc[k], end) if VC.lines[i].startswith('- **open (')]
        vc_passes[k] = [i + 1 for i in range(vc[k], end)
                        if VC.lines[i].startswith('### Pass ') or VC.lines[i].startswith('### Final check')]
    vc_proj = [i for i in vc_open['l'] if 'say the sweep gates will fail no matter what the counts are' in VC.line(i)]
    if len(vc_proj) != 1:
        raise SystemExit('values-check finding on the licenses projection: %d hits' % len(vc_proj))
    vc_proj = vc_proj[0]

    # ---------- carried outcomes (verbatim substrings asserted present) ----------
    i_line, v_line, l_line = H.line(h['i_pass']), H.line(h['v_pass']), L.line(lc['pass'])
    ii_line, iv_mech_line = H.line(h['s_ii']), H.line(h['s_iv'])
    c_line = C.line(cc['pass'])
    gl_out = G.line(g['o1'])
    short = {
        'i': "STOP pending the PI's resolution, on the block's literal text (:77, 'Any hit in history is a STOP on the release')",
        'ii': 'A list, no pass condition; none is a credential.',
        'iv': '(iv) licenses recorded',
        'v': 'PASS -- nothing over 100 MB untreated',
        'vi': 'Expected: nothing; found: nothing in the three classes N12(vi) names.',
        'gl': 'Findings: 4. TRUE-SECRET: 0. FALSE-POSITIVE: 4. UNTRIAGED: 0.',
        'iii_a': '**Absent** from every tracked file at the ref, every blob and commit message reachable from any ref, and every tag annotation.',
        'iii_p': '**Present in untracked working-tree files** listed in (4).',
    }
    for k, src in (('i', i_line), ('ii', ii_line), ('iv', l_line), ('v', v_line), ('vi', c_line), ('gl', gl_out),
                   ('iii_a', PW.line(pw['absent'])), ('iii_p', PW.line(pw['present']))):
        assert short[k] in src, 'carried excerpt not verbatim: ' + k
    # the history raw's own pass/STOP line, as written at its commit (history; the PI's rulings of 2026-10-09, item 4, answer it)
    i_stop = "STOP pending the PI's resolution" in i_line
    H.need(h['i_pass'], "the fallback returns %d hit lines, so (i) is not 'no hits'" % hj['fallback']['hit_lines'],
           "The block's pass is '(i) no hits, or hits resolved by the PI'; resolving them is the PI's decision, not Code's.")
    H.need(h['s_i'], 'TRUE-SECRET-CANDIDATE 0; UNTRIAGED 0.')
    H.need(h['i_pass'], "0 TRUE-SECRET-CANDIDATE among the fallback's hits",
           'and 0 among the precise-pattern, in-context and context-free high-entropy hits')
    iv_ok = l_line.startswith('**(iv) licenses recorded**') and lj.get('pass_line') == '(iv) licenses recorded'
    v_ok = 'PASS' in v_line and 'nothing over 100 MB untreated' in v_line

    # ---------- gitleaks: the findings table, the script's fingerprint keys ----------
    gl_rx = re.compile(r'^\| (\d+) \| ([a-z0-9-]+) \| `([^`]+)` \| `([0-9a-f]{10})` \| (\d+) \| .*? \| ([A-Z-]+) \| [^|]+ \|$')
    gl_rows = []
    for i, ln in enumerate(G.lines, 1):
        mm = gl_rx.match(ln)
        if mm:
            gl_rows.append({'n': int(mm.group(1)), 'rule': mm.group(2), 'file': mm.group(3), 'commit': mm.group(4),
                            'line': int(mm.group(5)), 'verdict': mm.group(6), 'at': i})
    if not gl_rows or gl_rows[0]['at'] != g['tbl'] + 2 or [r['at'] for r in gl_rows] != list(range(g['tbl'] + 2, g['tbl'] + 2 + len(gl_rows))):
        raise SystemExit('gitleaks raw: findings rows are not the contiguous body of its table')
    if [r['n'] for r in gl_rows] != list(range(1, len(gl_rows) + 1)):
        raise SystemExit('gitleaks raw: findings table rows are not 1..n')
    GS = Doc(roc, Rs, GL_SCRIPT)
    gs_tri = GS.sw('TRIAGE = {')
    GS.need(GS.sw("# Code's triage, keyed by the gitleaks fingerprint (commit:file:rule:line)."), 'keyed by the gitleaks fingerprint')
    gs_end = GS.find(lambda s: s == '}', 'end of TRIAGE', unique=False, start=gs_tri)
    fp_keys = []
    for i in range(gs_tri, gs_end):
        mm = re.match(r'^    "([0-9a-f]{40}):([^:"]+):([a-z0-9-]+):(\d+)": \($', GS.lines[i])
        if mm:
            fp_keys.append((mm.group(1), mm.group(2), mm.group(3), int(mm.group(4)), GS.lines[i + 1].strip().strip('",')))
    gl_matched = 0
    for r in gl_rows:
        ks = [k for k in fp_keys if k[0].startswith(r['commit']) and k[1] == r['file'] and k[2] == r['rule'] and k[3] == r['line']]
        if len(ks) == 1 and ks[0][4] == r['verdict']:
            gl_matched += 1
    gl_leaks = int(G.num(g['leaks'], r'leaks found: (\d+)'))
    gl_commits = int(G.num(g['commits'], r'INF (\d+) commits scanned'))
    gl_o = {k: int(G.num(g['o1'], r'%s: (\d+)\.' % k)) for k in ('Findings', 'TRUE-SECRET', 'FALSE-POSITIVE', 'UNTRIAGED')}
    gl_scanner = G.num(g['cmd'], r'^- (gitleaks [0-9.]+) \(installed by the PI\)')
    G.need(g['o3'], "Resolving (i) remains the PI's act; this raw is the triage it rests on.")

    # ---------- the routing commit's message (a record of the PI's routing, as Code applied it) ----------
    ro_msg = git('log', '-1', '--format=%B', roc)
    ro_loc = '`git show -s %s` (commit message)' % Rs

    def need_msg(*subs):
        for sub in subs:
            if sub not in ro_msg:
                raise SystemExit('routing commit message lacks %r' % sub)

    need_msg('A per-file gitleaks pass over this commit\'s 19 files finds 0.',
             'D2 (the LoRA phrase) is closed by the PI: no match.',
             'LICENSE, LICENSE-CC-BY-4.0 and LICENSING.md, per the PI.',
             'D4: archive/PROPOSAL-m-gating-campaign-v1_2.md through v1_10.md, committed unmodified.',
             "v1_3:121 carries the RunPod network-volume id once.", "the PI's D1 is to leave it",
             'Not committed, per D4: HANDOFF-*-design.md, DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md, the superseded '
             'ADDENDUM-g3-b2r drafts, ADDENDUM-k1.md, archive/PREPRINT pre-patch copies. PREPRINT-v1_0-draft.md waits for patch v6.')
    RO_PERFILE = "A per-file gitleaks pass over this commit's 19 files finds 0."
    RO_SCREEN = ('Screened before commit: read in full or by diff; redaction and wider pattern scans; no third-party data, '
                 'no secrets, and the password absent.')
    need_msg(RO_PERFILE, RO_SCREEN)
    # the screen sits under the D4 bullet of the message (the nine PROPOSAL-m files), not under another bullet
    ro_d4_at = ro_msg.find('- D4: archive/PROPOSAL-m-gating-campaign-v1_2.md through v1_10.md')
    ro_screen_at = ro_msg.find(RO_SCREEN)
    if not (0 <= ro_d4_at < ro_screen_at) or '\n- ' in ro_msg[ro_d4_at + 3:ro_screen_at]:
        raise SystemExit('routing commit message: the screen is not under the D4 bullet')
    ro_files = [p for p in git('diff-tree', '--no-commit-id', '--name-only', '-r', roc).split('\n') if p]
    ro_pm = [p for p in ro_files if p in D4_COMMIT]
    ro_rest = [p for p in ro_files if p not in D4_COMMIT]
    if len(ro_pm) != len(D4_COMMIT):
        raise SystemExit('routing commit: the nine PROPOSAL-m files are not all in it')

    # ---------- summarized text: read by pattern or asserted against the cited line ----------
    H.need(h['referent'], 'which the README and the ledger cite together as N12\'s output')
    L.need(lc['part'], "The block's N12 output, `results/raw/<stamp>_note-N12-scrub.md` (block line 84), cites it.")
    L.need(lc['scope_time'], 'this script is to be re-run at the final pre-flip commit', 'the N12 scrub raw states that bound')
    # (i)
    deviation = ('Block :77 runs its fallback only if the scanners are not installable; that condition does not hold, '
                 'so running the fallback instead is a deviation from the block, recorded here for the PI.')
    H.need(h['scanners'], deviation, 'installable here via Homebrew', "forbids installs without the PI's word")
    H.need(h['interim'], 'pre-flip step 3 still needs the clean run at the release commit')
    H.need(h['vc5_ctrl'], 'ALL PASS')
    vc5_findings = [i + 1 for i in range(h['vc5b'], len(H.lines)) if re.match(r'^\d+\. \*\*', H.lines[i])]
    vc5_applied = [i for i in vc5_findings if 'APPLIED' in H.line(i)]
    n_refs = len(hj['refs'])
    if n_refs != sum(1 for i in range(h['scope'], h['i'] - 1) if H.lines[i].startswith('| `refs/')):
        raise SystemExit('refs table and JSON refs disagree')
    n_vc_rounds = sum(1 for ln in H.lines if ln.startswith('## Values-check'))
    tsc, untri, hits_n = hj['true_secret_candidates'], hj['untriaged'], hj['fallback']['hit_lines']
    # the history raw's pass-phrase-shaped values: the LoRA phrase and a fragment of the class's own pattern
    pp_end = H.sw('`CONTINUITY.md`')
    pp_lora = H.find(lambda s: '-- PASSPHRASE-SHAPED: a synthetic three-word' in s, 'LoRA phrase row', start=h['passphrase'], end=pp_end)
    pp_regex = H.find(lambda s: "-- FALSE-POSITIVE: a fragment of this class's own regular expression" in s, 'regex row',
                      start=h['passphrase'], end=pp_end)
    n_pp = int(H.num(h['passphrase'], r'\*\* (\d+) distinct value\(s\)'))
    # (iv)
    proj_n_files = int(L.num(lc['proj'], r'They are untracked at the commit read \((\d+) files'))
    proj_ids = int(L.num(lc['proj'], r'the id sweep would gain \*\*(\d+)\*\* unclassified id'))
    proj_hosts = int(L.num(lc['proj'], r'the host sweep \*\*(\d+)\*\* unclassified host'))
    L.need(lc['proj'], "so the pass line's two sweep gates would fail at the pre-flip re-run until each is classified")
    L.need(lc['it8'], "so the pass line's two sweep gates fail there until each is classified")
    sweep_gates = ['external-reference sweep: 0 unclassified ids', 'URL-host sweep: 0 unclassified hosts']
    if not all(g_ in lj['pass_gates'] for g_ in sweep_gates):
        raise SystemExit('licenses JSON: a sweep gate is not among pass_gates')
    LS = Doc(audit, A, LIC_SCRIPT)
    ls_gate = [LS.has('"%s":' % g_) for g_ in sweep_gates]
    ls_fail = LS.has('P(f"**(iv) NOT recorded** -- failed conjunct(s)')
    # the licenses script's fixed text on the repository's license, and its tree-reading rule
    ls_rule = LS.has(LIC_RULE_SRC)
    ls_fixed = [LS.has('"root", "the lab", "the tag (PI\'s)", "**no LICENSE file** (none at HEAD, none ever added)",'),
                LS.has('P("2. **The repository has no license.** The PI chooses one, or none, before publication.")'),
                LS.has('f"the Global Workspace paper\'s license was not read, and the repository has no LICENSE "')]
    for n in ls_fixed:
        if '{' in LS.line(n):
            raise SystemExit('licenses script: the no-license sentence at :%d is not fixed text' % n)
    LS.need(ls_fixed[2] + 1, 'f"file.')
    # computed-new, working tree: does the licenses script on disk still print that fixed text, or compute it from the tree?
    ls_wt_b = open(os.path.join(REPO, LIC_SCRIPT), 'rb').read()
    ls_wt = ls_wt_b.decode('utf-8').split('\n')
    ls_wt_sha = sha256b(ls_wt_b)
    ls_wt_committed = sha256b(git('show', '%s:%s' % (head, LIC_SCRIPT), binary=True)) == ls_wt_sha
    ls_wt_comp = [[i + 1 for i, ln in enumerate(ls_wt) if sub_ in ln] for sub_ in LS_WT_COMPUTED]
    ls_wt_fixed = [[i + 1 for i, ln in enumerate(ls_wt) if LS.line(n).strip() == ln.strip()] for n in (ls_fixed[0], ls_fixed[2])]
    if all(len(x) == 1 for x in ls_wt_comp) and not any(ls_wt_fixed):
        if ls_wt_committed:
            ls_l = ['`%s@%s:%d`' % (LIC_SCRIPT, head[:7], x[0]) for x in ls_wt_comp]
            ls_tail = 'it is the version committed at HEAD'
        else:
            ls_l = ['working-tree line %d' % x[0] for x in ls_wt_comp]
            ls_tail = 'that version is the one Code\'s release plan commits at R1 (section 10, the release sequence), where its lines become citable'
        ls_route_txt = ('(computed-new, the working tree) The licenses script on disk at this run (sha256 `%s...`; %s) no longer carries the section-6 row\'s or the pass line\'s fixed text: it computes its statements on this repository\'s own license from the tree at the commit it reads (`repo_licensed_at_commit`, %s; its rule, %s), and its PI item 2 keeps the no-license sentence only for a tree with no root-level license text; %s. That change is Code\'s release preparation, not among the five questions %s answers; what the release run prints is its own raw\'s record (section 10, item 3).' % (
            ls_wt_sha[:16], 'equal to HEAD\'s' if ls_wt_committed else 'not yet committed', ls_l[0], ls_l[1], ls_tail, ANSWER))
        ls_iv_txt = 'fixed at `%s` and computed from the tree by the version on disk (section 5)' % A
        ls_it3_txt = 'its no-license text, fixed at `%s` and computed from the tree by the version on disk, is recorded in section 5' % A
        ls_lead = ('- Resolved by Code\'s release preparation (computed-new, from the licenses script as committed at `%s` and the version on disk): the script as committed at `%s` printed three of its statements that the repository has no license as fixed text, not computed from the tree -- the section-6 row for this repository (%s), PI item 2 (%s) and the pass line\'s clause (%s).' % (
            A, A, LS.loc(ls_fixed[0]), LS.loc(ls_fixed[1]), LS.loc(ls_fixed[2])))
    elif not any(ls_wt_comp) and all(len(x) == 1 for x in ls_wt_fixed):
        ls_route_txt = '(computed-new, the working tree) The licenses script on disk at this run (sha256 `%s...`; %s) still carries that fixed text.' % (
            ls_wt_sha[:16], 'equal to HEAD\'s' if ls_wt_committed else 'modified, not committed')
        ls_iv_txt = 'fixed (section 5)'
        ls_it3_txt = 'its fixed no-license text is flagged, in section 5'
        ls_lead = ('- Flag for the PI (computed-new, from the committed licenses script; changing it is outside this part): three of the script\'s statements that the repository has no license are fixed text, not computed from the tree -- the section-6 row for this repository (%s), PI item 2 (%s) and the pass line\'s clause (%s) -- so a re-run prints them whatever the tree holds.' % (
            LS.loc(ls_fixed[0]), LS.loc(ls_fixed[1]), LS.loc(ls_fixed[2])))
    else:
        raise SystemExit('licenses script on disk: partial license-text change (computed %r, fixed %r)' % (ls_wt_comp, ls_wt_fixed))
    # each part script's default outputs (a re-run with default arguments overwrites the committed raws)
    HS, CS = Doc(hic, Hs, HIST_SCRIPT), Doc(audit, A, CON_SCRIPT)

    def default_at(doc, prefix, expect):
        n = doc.sw(prefix)
        doc.need(n, expect)
        return n

    out_defaults = {
        'history': (default_at(HS, 'DEFAULT_MD = ', '"%s"' % HIST_MD), default_at(HS, 'DEFAULT_JSON = ', '"%s"' % HIST_JSON)),
        'licenses': (default_at(LS, 'DEFAULT_MD = ', '"%s"' % LIC_MD), default_at(LS, 'DEFAULT_JSON = ', '"%s"' % LIC_JSON)),
        'content': (default_at(CS, 'DEFAULT_OUT = ', '"%s"' % os.path.basename(CON_JSON)),),
    }
    HS.has('ap.add_argument("--out", default=DEFAULT_MD)')
    HS.has('ap.add_argument("--json-out", default=DEFAULT_JSON)')
    LS.has('ap.add_argument("--out", default=DEFAULT_MD,')
    LS.has('ap.add_argument("--json-out", default=DEFAULT_JSON,')
    ls_outdir = LS.has('ap.add_argument("--out-dir", default=None,')
    ls_histraw = LS.sw('    HIST_RAW = "%s"' % HIST_MD)
    LS.need(LS.has('hist_raw_fp = os.path.join(REPO, HIST_RAW)'), 'HIST_RAW')
    CS.has('ap.add_argument("--json-out", default=DEFAULT_OUT)')
    cs_nooverwrite = CS.has('sys.exit("refusing to overwrite existing %s" % out)')
    hs_rawonly = HS.has('raise SystemExit(f"refusing output inside the repository outside results/raw/: {o}")')
    hs_ownonly = HS.has('raise SystemExit(f"refusing a results/raw/ output other than this part\'s own two files: {o}")')
    # the release route (computed-new, working tree): does the history script on disk accept the two release basenames?
    hs_wt = open(os.path.join(REPO, HIST_SCRIPT), encoding='utf-8').read().split('\n')
    hs_wt_def = [[i + 1 for i, ln in enumerate(hs_wt) if ln.strip() == '%s = "%s"' % (k_, v_)]
                 for k_, v_ in (('RELEASE_MD', RR['history'][0]), ('RELEASE_JSON', RR['history'][1]))]
    hs_wt_own = [i + 1 for i, ln in enumerate(hs_wt) if ln.strip() == 'own = {"md": (DEFAULT_MD, RELEASE_MD), "json": (DEFAULT_JSON, RELEASE_JSON)}']
    hs_wt_sha = sha256b(open(os.path.join(REPO, HIST_SCRIPT), 'rb').read())
    hs_wt_committed = sha256b(git('show', '%s:%s' % (head, HIST_SCRIPT), binary=True)) == hs_wt_sha
    # the release version's output rules, located by content (each must occur exactly once in the accepts branch)
    HS_WT_RULES = (('own_only', 'raise SystemExit(f"refusing a results/raw/ output other than this part\'s own files "'),
                   ('raw_only', 'raise SystemExit(f"refusing output inside the repository outside results/raw/: {o}")'),
                   ('tracked', 'raise SystemExit(f"refusing to overwrite a tracked raw (committed at HEAD or staged): {o}"'),
                   ('in_place_cond', 'if tracked_ and not (a.in_place and rel_ in (DEFAULT_MD, DEFAULT_JSON)):'),
                   ('in_place_only', 'raise SystemExit("refusing --in-place: it names the in-place regeneration of the two 2026-10-08 raws only")'))
    if all(len(x) == 1 for x in hs_wt_def) and len(hs_wt_own) == 1:
        hs_wt_rule = {}
        for k_, sub_ in HS_WT_RULES:
            n_ = [i + 1 for i, ln in enumerate(hs_wt) if sub_ in ln]
            if len(n_) != 1:
                raise SystemExit('history script on disk: release output rule %r: %d hits' % (k_, len(n_)))
            hs_wt_rule[k_] = n_[0]
        hs_n = [hs_wt_def[0][0], hs_wt_def[1][0], hs_wt_own[0]] + [hs_wt_rule[k_] for k_, _ in HS_WT_RULES]
        if hs_wt_committed:
            hs_l = ['`%s@%s:%d`' % (HIST_SCRIPT, head[:7], n_) for n_ in hs_n]
            hs_tail = 'it is the version committed at HEAD'
        else:
            hs_l = ['working-tree line %d' % n_ for n_ in hs_n]
            hs_tail = 'that version is the one Code\'s release plan commits at R1 (the release sequence, below), where its lines become citable'
        hist_route_txt = ('The history script on disk at this run (sha256 `%s...`; %s) accepts them, under output rules that differ from `%s`\'s: it defines `RELEASE_MD` and `RELEASE_JSON` as those two paths (%s, %s), and its own outputs are exactly `DEFAULT_MD` or `RELEASE_MD` for `--out` and `DEFAULT_JSON` or `RELEASE_JSON` for `--json-out` (%s), so any other path inside the repository is refused, a subdirectory of `results/raw/` included (%s; outside `results/raw/` as before, %s); a tracked output path (committed at HEAD or staged) is refused (%s) unless `--in-place` is given for the two 2026-10-08 raws (%s), and `--in-place` names their in-place regeneration only (%s), so the release raws are never overwritten once committed. The release run writes them directly with `--out` and `--json-out`; %s.' % (
            hs_wt_sha[:16], 'equal to HEAD\'s' if hs_wt_committed else 'not yet committed', Hs, hs_l[0], hs_l[1], hs_l[2], hs_l[3], hs_l[4], hs_l[5], hs_l[6], hs_l[7], hs_tail))
    elif not any(hs_wt_def) and not hs_wt_own:
        hist_route_txt = ('The history script on disk at this run (sha256 `%s...`; %s) does not accept them either. Code\'s release plan is a release version of the script that adds the two release basenames to its accepted outputs and writes them directly with `--out` and `--json-out`; it is committed at R1 (the release sequence, below), and this index is regenerated at R1, so that it cites that version instead of this sentence.' % (
            hs_wt_sha[:16], 'equal to HEAD\'s' if hs_wt_committed else 'modified, not committed'))
    else:
        raise SystemExit('history script on disk: partial release-route definition (RELEASE_* %r, own %r)' % (hs_wt_def, hs_wt_own))
    L.need(lc['pass'], 'the Macar prompt text is CC BY 4.0 via the paper', 'the two word lists have no license found',
           "the Global Workspace paper's license was not read", 'the repository has no LICENSE file')
    H.need(h['floats'], 'stored logistic readability probe', 'which the README should name')
    floats_other = H.num(h['floats'], r'Other float arrays: (\d+) \(listed above; not read in context -- they need a reading before the README\'s statement is final\)')
    C.need(cc['h_iv'] + 1, 'single-line quotes, inside referent checks, from scripts in the gitignored `jlens-qwen36/` clone')
    C.need(cc['h_iv'] + 2, 'citations are published works only')
    C.need(cc['s8'], '(ii), (iii), (iv)')
    # D1
    d1_hand = int(C.num(c_bul[0], r'They sit in (\d+) tracked HANDOFFs'))
    d1_raws = int(C.num(c_bul[0], r'(\d+) tracked raws'))
    d1_msgs = int(C.num(c_bul[0], r'and (\d+) commit messages'))
    d1_spread = C.find(lambda s: s.strip().startswith('- Spread:'), 'D1 spread', start=cc['d1'], end=cc['d2'])
    C.need(d1_spread, 'RESULTS.md', 'test fixture', 'Commit messages: %d.' % d1_msgs)
    d1_status = C.find(lambda s: s.strip().startswith('- Status:'), 'D1 status', start=cc['d1'], end=cc['d2'])
    C.need(d1_status, 'stopped, parked, not terminated')
    C.need(cc['d1rec'] + 1, '(a) Accept publication.', 'terminate the parked pod', 'so that the ids are inert')
    C.need(cc['d1rec'] + 2, '(b) Redact the HEAD copies', 'History keeps every copy.')
    C.need(cc['d1rec'] + 3, '(c) Rewrite history.', "That is the PI's call")
    C.need(cc['fixture'], 'regenerates the pod id into every new self-test raw',
           'a code change, which this audit block forbids', 'it is a PI or design-seat decision')
    # D2
    C.need(cc['d2'] + 1, 'compares it with the continuity password out of band (N12(iii))')
    C.need(cc['d2'] + 2, 'A match means the password is already in history')
    C.need(cc['f44'], LORA_FORM, 'synthetic target of a LoRA overfit test', 'It is not a credential.', 'the PI rotates or retires it')
    # D3
    d3_local = int(C.num(cc['d3'] + 1, r'(\d+) commits carry `\.local` e-mail addresses'))
    d3_sess = int(C.num(cc['d3'] + 2, r'(\d+) commits carry one claude\.ai session URL in a trailer'))
    d3_sig = int(C.num(cc['d3'] + 3, r'Those same (\d+) commits carry SSH signatures that embed a public key'))
    C.need(cc['d3'] + 4, 'Low sensitivity.', '`.mailmap` changes the display only')
    d3_host = int(H.num(h['s_ii'], r"the author's laptop hostname in (\d+) commits' author/committer emails"))
    C.need(cc['f46'], 'a placeholder rather than a machine name')
    # D4
    d4_docs = C.num(cc['d4'], r'(\w+) design-seat documents are untracked and not gitignored')
    d4_other = int(C.num(cc['d4'], r'and so are (\d+) other root/archive files'))
    d4_hdr = C.num(cc['d4'], r'(\w+) of the design documents carry not-for-the-repo headers')
    C.need(cc['d4'], 'The release commit must stage by explicit path.')
    C.need(cc['d4rec'], 'No history action.')
    C.need(cc['d4rec'] + 1, 'stage by explicit path, and check `git diff --cached --name-status`')
    C.need(cc['d4rec'] + 2, 'move the design documents out of the checkout, or gitignore them (a PI or design-seat call)')
    # the PI's untracked documents carrying a D1 identifier at the history run's snapshot
    pp = hj['prerelease_pending_files']
    kv_label = {f: v[0] for f, v in pp['known_values'].items()}
    pi_d1 = []
    for f in pp['files']:
        if f['group'].startswith('other untracked') and f['known']:
            labs = sorted({kv_label[x].split(' (')[0] for x in f['known']})
            if not all(lb.startswith('runpod') for lb in labs):
                raise SystemExit('a PI document carries a non-RunPod class: %r' % labs)
            pi_d1.append((f['file'], labs))
    pi_rows = [i + 1 for i, ln in enumerate(H.lines) if ln.startswith('| other untracked or modified files | `')]
    pi_n_scanned = int(H.num(h['pre_pi'], r"\| other untracked or modified files \(the PI's documents\) \| (\d+) \|"))
    pi_n_with = int(H.num(h['pre_pi'], r"\| other untracked or modified files \(the PI's documents\) \| \d+ \| (\d+) \|"))
    if not (len(pi_d1) == len(pi_rows) == pi_n_with) or any(('`%s`' % f) not in H.line(r) for (f, _), r in zip(pi_d1, pi_rows)):
        raise SystemExit('the history raw\'s PI-document rows and its JSON disagree')
    pi_rows_span = (pi_rows[0], pi_rows[-1]) if pi_rows else None
    # pre-flip step 1 of the history raw (item 3 here)
    pf1_first = re.match(r'^1\. \*\*(.+?)\*\*', H.line(h['pf1'])).group(1)
    H.need(h['pf1'], "(the PI's to bind)", 'and no new value needing triage', "binding either part is the PI's call",
           'The tag should wait on a clean run.', 'with every raw, script and README of the end commit in place',
           'does not hold the tag', 'the identity emails and the laptop hostname', 'in any file the end commit adds')
    H.need(h['pf2'], 'compare its refs with the refs table under Scope', 'gets its own scan',
           'is deleted before the visibility change', '`refs/pull/*` refs cannot be deleted by the owner and become public')
    H.need(h['pf3'], 'pull requests', 'issues and their comments', 'Actions runs with their logs and artifacts', 'the wiki',
           'releases with their assets', 'force-pushed away')
    H.need(h['pf4'], "on the PI's word", 'over the repository at the release commit', "Their findings supersede the fallback's for (i).")
    C.need(cc['rerun'], 'with a new `--json-out` against the release commit', 'read every new 2026-10-08 raw once, end to end')
    C.need(cc['untracked'], 'They were not reviewed: review them before any commit that would add them.')
    H.need(h['pre_ident'], 'the laptop hostname')
    PF.need(pf_rem[1], 'Repeat at the release commit, immediately before the visibility change')
    PF.need(pf_rem[2], 'Repeat at the release commit, immediately before the visibility change', "Projects (v2): not readable here; the PI's look.")
    PF.need(pf_rem[3], 'The content and licenses scripts were not re-run.')
    PF.need(pf_rem[5], 'need the PI\'s word to install')

    # ---------- LICENSE files at the routing commit ----------
    lic = {}
    for p in LIC_FILES:
        bb = git('show', '%s:%s' % (roc, p), binary=True)
        wp = os.path.join(REPO, p)
        wb = open(wp, 'rb').read() if os.path.exists(wp) else None
        added = git('log', '--diff-filter=A', '--format=%H', head, '--', p).split()
        lic[p] = {'sha': sha256b(bb), 'lines': nlines(bb), 'wt': None if wb is None else wb == bb,
                  'added': added[-1] if added else None, 'text': bb.decode('utf-8')}
    if not all(lic[p]['added'] == roc for p in LIC_FILES):
        raise SystemExit('a LICENSE file was not added at the routing commit')
    lic_head = [ln.strip() for ln in lic['LICENSE']['text'].split('\n') if ln.strip()][:2]
    if lic_head[:2] != ['Apache License', 'Version 2.0, January 2004']:
        raise SystemExit('LICENSE does not open with the Apache License 2.0 heading')
    if [ln.strip() for ln in lic['LICENSE-CC-BY-4.0']['text'].split('\n') if ln.strip()][0] != 'Attribution 4.0 International':
        raise SystemExit('LICENSE-CC-BY-4.0 does not open with the CC BY 4.0 heading')
    LG = Doc(roc, Rs, 'LICENSING.md')
    lg = {'code': LG.sw('- **Code** is licensed under the Apache License, Version 2.0'),
          'docs': LG.sw('- **Documents and data** are licensed under the Creative Commons Attribution 4.0 International license'),
          'tp': LG.sw('## Third-party material'), 'macar': LG.sw('- **Macar et al. 2026 (arXiv:2603.21396).**'),
          'lindsey': LG.sw('- **Lindsey 2025.**'), 'models': LG.sw('- **Models.**'),
          'row_a': LG.sw('| `LICENSE` | Apache License 2.0 |'), 'row_c': LG.sw('| `LICENSE-CC-BY-4.0` | CC BY 4.0 legal code, plain text |')}
    LG.need(lg['macar'], 'is distributed under CC BY 4.0; attribution is to the paper')
    LG.need(lg['lindsey'], 'That page states no license.', 'this repository does not relicense them')
    lg_sha = {'LICENSE': LG.num(lg['row_a'], r'`([0-9a-f]{64})`'), 'LICENSE-CC-BY-4.0': LG.num(lg['row_c'], r'`([0-9a-f]{64})`')}
    lg_gw = sum(1 for ln in LG.lines if 'Global Workspace' in ln)
    tree_head = [p for p in git('ls-tree', '-r', '--name-only', head).split('\n') if p]
    lic_rule_head = sorted(p for p in tree_head if LIC_RULE.search(p))
    lic_rule_lread = lj['repo_license']['license_files_at_commit']

    # ---------- D4 staging state at HEAD (names and git tracked status only; nothing opened) ----------
    def tracked_at(rev, path):
        return bool(git('ls-tree', '--name-only', rev, '--', path).strip())

    def ever_committed(path):
        return len([c for c in git('log', '--all', '--format=%H', '--', path).split() if c])

    d4c = [(p, tracked_at(head, p), (git('log', '--diff-filter=A', '--format=%H', head, '--', p).split() or [None])[-1]) for p in D4_COMMIT]
    d4c_ok = all(t and ad == roc for _, t, ad in d4c)
    d4k = []
    for desc, pat in D4_KEEP_OUT:
        names = sorted(os.path.relpath(x, REPO) for x in glob.glob(os.path.join(REPO, pat)))
        # the committed g3-b2r addendum the drafts precede is not a draft: excluded by name, whatever its status
        names = [n for n in names if n != G3_COMMITTED]
        rows = [(n, tracked_at(head, n), ever_committed(n)) for n in names]
        d4k.append((desc, pat, rows))
    g3_committed_tracked = tracked_at(head, G3_COMMITTED)
    g3_tracked = sorted(p for p in tree_head if re.fullmatch(r'ADDENDUM-g3-b2r[^/]*\.md', p))
    d4k_files = [r for _, _, rows in d4k for r in rows]
    d4k_tracked = [n for n, t, _ in d4k_files if t]
    d4k_ever = [n for n, _, e in d4k_files if e]
    pre_exists = os.path.exists(os.path.join(REPO, PREPRINT))
    pre_tracked = tracked_at(head, PREPRINT)
    pre_ever = ever_committed(PREPRINT)
    # untracked, not-ignored files on disk at this run that are on neither the do-not-commit list nor the
    # preprint line (names only; none is opened): files a later commit could add, each to be reviewed first
    keep_names = {n for _, _, rows in d4k for n, _, _ in rows}
    untr_now = sorted(p for p in git('ls-files', '--others', '--exclude-standard').split('\n') if p)
    untr_other = [p for p in untr_now if p not in keep_names and p != PREPRINT]
    tag_exists = bool(git('for-each-ref', '--format=%(refname)', 'refs/tags/' + TAG).strip())
    pi_d1_now = [(f, tracked_at(head, f)) for f, _ in pi_d1]
    pw_now = [(f, tracked_at(head, f), ever_committed(f)) for f, _ in pw_files]

    # ---------- provenance of the part raws ----------
    parts = []
    for path, rev, short_ in ((HIST_MD, hic, Hs), (HIST_JSON, hic, Hs), (LIC_MD, audit, A), (LIC_JSON, audit, A),
                              (CON_MD, audit, A), (CON_JSON, audit, A), (PF_MD, pfc, PFs), (PF_JSON, pfc, PFs),
                              (GL_MD, roc, Rs), (PW_MD, roc, Rs)):
        cb = git('show', '%s:%s' % (rev, path), binary=True)
        wp = os.path.join(REPO, path)
        wb = open(wp, 'rb').read() if os.path.exists(wp) else None
        last = git('log', '-1', '--format=%H', head, '--', path).strip()
        parts.append((path, short_, sha256b(cb), nlines(cb), None if wb is None else (wb == cb), last == git('rev-parse', short_).strip()))
    scr = {}
    for sp, rev, short_ in ((HIST_SCRIPT, hic, Hs), (LIC_SCRIPT, audit, A), (CON_SCRIPT, audit, A),
                            (PF_SCRIPT, pfc, PFs), (GL_SCRIPT, roc, Rs), (PW_SCRIPT, roc, Rs)):
        scr[sp] = (sha256b(git('show', '%s:%s' % (rev, sp), binary=True)), short_)
    h_scan, l_scan = hj['head'], lj['commit_read']
    c_scan = cj['rev']['resolved']
    assert h_scan in H.line(h['head']) and l_scan in L.line(lc['commit']) and c_scan in C.line(cc['head'])
    hist_script_rec = hj['script_sha256']
    con_script_rec = re.search(r'sha256 `([0-9a-f]{64})`', C.line(cc['screen'])).group(1)
    con_json_rec = re.findall(r'sha256 `([0-9a-f]{64})`', C.line(cc['screen']))[1]
    lic_script_rec = re.search(r'([0-9a-f]{64})', L.line(L.sw('- Script:')))
    pf_script_rec = PF.num(pf['script'], r'sha256 `([0-9a-f]{64})`')
    gl_script_rec = G.num(g['script'], r'sha256 `([0-9a-f]{64})`')
    pw_script_rec = PW.num(pw['script'], r'sha256 `([0-9a-f]{64})`')

    # ---------- cross-checks (computed-new: md text vs the part's own JSON, a committed file, or a recount) ----------
    xc = []

    def xadd(what, md_val, js_val, md_loc, js_ptr):
        xc.append((what, md_val, js_val, md_loc, js_ptr, 'computed-new (agree)' if md_val == js_val else 'discrepant'))

    m = re.search(r'fallback ([0-9]+) hit lines', H.line(h['s_i']))
    xadd('(i) fallback hit lines', int(m.group(1)), hits_n, H.loc(h['s_i']), 'fallback.hit_lines')
    m = re.search(r'TRUE-SECRET-CANDIDATE ([0-9]+); UNTRIAGED ([0-9]+)', H.line(h['s_i']))
    xadd('(i) TRUE-SECRET-CANDIDATE', int(m.group(1)), tsc, H.loc(h['s_i']), 'true_secret_candidates')
    xadd('(i) UNTRIAGED', int(m.group(2)), untri, H.loc(h['s_i']), 'untriaged')
    sa = hj['scanner_availability']['which']
    xadd('(i) gitleaks / trufflehog installed, at the history run', 'no / no' if 'gitleaks not found, trufflehog not found' in H.line(h['scanners']) else '?',
         '%s / %s' % ('no' if sa['gitleaks'] is None else 'yes', 'no' if sa['trufflehog'] is None else 'yes'),
         H.loc(h['scanners']), 'scanner_availability.which')
    xadd('(i) gitleaks: findings, log line vs outcome line', gl_leaks, gl_o['Findings'], G.loc(g['leaks']), '(%s)' % G.loc(g['o1']).strip('`'))
    xadd('(i) gitleaks: findings-table rows vs outcome line', len(gl_rows), gl_o['Findings'], G.loc(gl_rows[0]['at'], gl_rows[-1]['at']) if gl_rows else 'none', '(%s)' % G.loc(g['o1']).strip('`'))
    xadd('(i) gitleaks: FALSE-POSITIVE rows vs outcome line', sum(1 for r in gl_rows if r['verdict'] == 'FALSE-POSITIVE'),
         gl_o['FALSE-POSITIVE'], G.loc(gl_rows[0]['at'], gl_rows[-1]['at']), '(%s)' % G.loc(g['o1']).strip('`'))
    xadd('(i) gitleaks: UNTRIAGED rows vs outcome line', sum(1 for r in gl_rows if r['verdict'] == 'UNTRIAGED'),
         gl_o['UNTRIAGED'], G.loc(gl_rows[0]['at'], gl_rows[-1]['at']), '(%s)' % G.loc(g['o1']).strip('`'))
    xadd("(i) gitleaks: rows matched to exactly one fingerprint key of the committed script's triage, same verdict",
         len(gl_rows), gl_matched, G.loc(gl_rows[0]['at'], gl_rows[-1]['at']),
         '(%s, %d keys)' % (GS.loc(gs_tri, gs_end).strip('`'), len(fp_keys)))
    # recount: commits and blobs reachable at the gitleaks/password run (its HEAD plus the refs other than main,
    # which are unchanged since the pre-flip read of the server refs)
    other_refs = [ln for ln in git('for-each-ref', '--format=%(refname)').split('\n')
                  if ln and ln not in ('refs/heads/main', 'refs/remotes/origin/main', 'refs/remotes/origin/HEAD')]
    pf_srv = {e['ref']: e['object'] for e in pfj['refs']['server']}

    def srv_name(r):
        return r.replace('refs/remotes/origin/', 'refs/heads/', 1) if r.startswith('refs/remotes/origin/') else r

    other_unchanged = all(pf_srv.get(srv_name(r)) == git('rev-parse', r).strip() for r in other_refs)

    def recount(ref):
        n_c = int(git('rev-list', '--count', ref, *other_refs).strip())
        ids = [x.split()[0] for x in git('rev-list', '--objects', '--filter=object:type=blob', '--filter-provided-objects',
                                           ref, *other_refs).split('\n') if x]
        types = git('cat-file', '--batch-check=%(objecttype)', inp=('\n'.join(ids) + '\n').encode()).split()
        return n_c, sum(1 for t in types if t == 'blob')

    rc_gl, rc_pw = recount(gl_head), recount(pw_ref)
    rc_note = '(recount: git rev-list from %s and the %d other refs, unchanged since the pre-flip read: %s)'
    xadd('(i) gitleaks: commits scanned', gl_commits, rc_gl[0], G.loc(g['commits']), rc_note % (gl_head[:10], len(other_refs), yn(other_unchanged)))
    xadd('(iii) password search: commit messages scanned', pw_msgs, rc_pw[0], PW.loc(pw['r3']), rc_note % (pw_ref[:10], len(other_refs), yn(other_unchanged)))
    xadd('(iii) password search: blobs reachable from any ref', pw_blobs, rc_pw[1], PW.loc(pw['r2']), rc_note % (pw_ref[:10], len(other_refs), yn(other_unchanged)))
    xadd('(iii) password search: files with it, count vs rows', pw_with, len(pw_files), PW.loc(pw['r4']), '(%s)' % PW.loc(pw_files[0][1], pw_files[-1][1]).strip('`'))
    xadd("routing commit: files, its message's per-file gitleaks pass vs the commit", 19, len(ro_files), ro_loc, '(git diff-tree -r %s)' % Rs)
    xadd("routing commit: PROPOSAL-m files under its message's pre-commit screen vs the commit", 9, len(ro_pm), ro_loc,
         '(git diff-tree -r %s, archive/PROPOSAL-m-gating-campaign-v1_2..v1_10)' % Rs)
    m = re.search(r'largest blob ([0-9,]+) bytes; files at HEAD over 50 MB ([0-9]+), over 50 MiB ([0-9]+), over 100 MB ([0-9]+)', H.line(h['s_v']))
    xadd('(v) largest blob, bytes', int(m.group(1).replace(',', '')), hj['max_blob_bytes'], H.loc(h['s_v']), 'max_blob_bytes')
    xadd('(v) files at HEAD over 50 MB', int(m.group(2)), sum(1 for f in hj['head_files_over_40MB'] if f['over_50MB']), H.loc(h['s_v']), 'head_files_over_40MB[].over_50MB')
    xadd('(v) files at HEAD over 100 MB', int(m.group(4)), sum(1 for f in hj['head_files_over_40MB'] if f['over_100MB'] or f['over_100MiB']), H.loc(h['s_v']), 'head_files_over_40MB[].over_100MB|over_100MiB')
    xadd('(v) blobs in history over 100 MB', 0 if 'no blob anywhere in history exceeds 100 MB' in v_line else '?',
         sum(1 for x in hj['largest_blobs'] if x['size'] > 100 * 10 ** 6), H.loc(h['v_pass']), 'largest_blobs[].size')
    m = re.search(r'jlens-qwen36 paths ever tracked ([0-9]+);.*npz without an explicit line ([0-9]+); weight-shaped paths ([0-9]+)', iv_mech_line)
    xadd('(iv) jlens-qwen36 paths ever tracked', int(m.group(1)), len(hj['jlens']['head']) + len(hj['jlens']['history']), H.loc(h['s_iv']), 'jlens.head + jlens.history')
    xadd('(iv) npz without an explicit allowlist line', int(m.group(2)), sum(1 for x in hj['npz'] if not x['explicit_allowlist_line_HEAD']), H.loc(h['s_iv']), 'npz[].explicit_allowlist_line_HEAD')
    xadd('(iv) weight-shaped paths ever tracked', int(m.group(3)), len(hj['weight_shaped_paths']), H.loc(h['s_iv']), 'weight_shaped_paths')
    xadd('(iv) pass line', '(iv) licenses recorded' if l_line.startswith('**(iv) licenses recorded**') else '?', lj['pass_line'], L.loc(lc['pass']), 'pass_line')
    gates = lj['pass_gates']
    g_ln = L.find(lambda s: 'Gates: block sha256 and 141 lines:' in s, 'gates line')
    g_md = sum(1 for k in gates if ('%s: True' % k) in L.line(g_ln))
    xadd('(iv) pass gates True', '%d of %d' % (g_md, len(gates)), '%d of %d' % (sum(1 for v in gates.values() if v is True), len(gates)),
         L.loc(g_ln), 'pass_gates')
    m = re.search(r'for the ([0-9]+) rows of section 6', l_line)
    xadd('(iv) rows in the section-6 table', int(m.group(1)), len(lj['table']), L.loc(lc['pass']), 'table')
    m = re.search(r'LICENSE / LICENCE / COPYING / NOTICE files at the commit: \*\*([0-9]+)\*\*', L.line(lc['s5'] + 2))
    xadd('(iv) repository LICENSE files at the commit the licenses part read', int(m.group(1)), len(lic_rule_lread), L.loc(lc['s5'] + 2), 'repo_license.license_files_at_commit')
    for p in ('LICENSE', 'LICENSE-CC-BY-4.0'):
        xadd('(iv) `%s` sha256, LICENSING.md vs committed' % p, lg_sha[p], lic[p]['sha'], LG.loc(lg['row_a'] if p == 'LICENSE' else lg['row_c']),
             '(%s at %s)' % (p, Rs))
    m = re.search(r'\*\*File count reviewed: ([0-9]+)\*\* \(([0-9]+) results/raw \+ ([0-9]+) HANDOFF', C.line(cc['count']))
    xadd('(vi) files reviewed (results/raw + HANDOFF at its HEAD)', int(m.group(1)), cj['scope']['results_raw_at_rev'] + cj['scope']['handoff_md_at_rev'], C.loc(cc['count']), 'scope.results_raw_at_rev + scope.handoff_md_at_rev')
    xadd('(vi) screen JSON sha256 recorded vs committed', con_json_rec, sha256b(cj_raw), C.loc(cc['screen']), '(file sha256 at %s)' % A)
    pf_lines_md = [i + 1 for i in range(pf['s4'], section_end(PF, pf['s4'])) if re.match(r'^- (PASS|FLAG|INFO|NOT READ) -- \*\*', PF.lines[i])]
    pf_lines_eq = sum(1 for e in pfj['pass_flag'] if ('- %s -- **%s**. %s' % (e['outcome'], e['check'], e['text'])) in
                      {PF.line(i) for i in pf_lines_md})
    xadd('pre-flip: pass/flag lines (md) vs JSON entries reproduced verbatim', len(pf_lines_md), pf_lines_eq,
         PF.loc(pf_lines_md[0], pf_lines_md[-1]), 'pass_flag[]')
    xadd('pre-flip: section-5 item lines (md) carrying the JSON status and locator verbatim, vs JSON items', len(pf_rem), len(pfj['remaining']), PF.loc(pf_rem[1], pf_rem[max(pf_rem)]), 'remaining[].status')
    xadd('pre-flip: server refs', int(PF.num(PF.sw('Origin:', start=pf['s1']), r'ls-remote returned (\d+) refs')), len(pfj['refs']['server']),
         PF.loc(PF.sw('Origin:', start=pf['s1'])), 'refs.server')
    for what, rec, sp in (('history', hist_script_rec, HIST_SCRIPT), ('content', con_script_rec, CON_SCRIPT),
                          ('pre-flip', pf_script_rec, PF_SCRIPT), ('gitleaks', gl_script_rec, GL_SCRIPT),
                          ('password', pw_script_rec, PW_SCRIPT)):
        loc_ = {'history': H.loc(H.sw('- Script:')), 'content': C.loc(cc['screen']), 'pre-flip': PF.loc(pf['script']),
                'gitleaks': G.loc(g['script']), 'password': PW.loc(pw['script'])}[what]
        xadd('%s script sha256 recorded vs committed' % what, rec, scr[sp][0], loc_, '(%s at %s)' % (sp, scr[sp][1]))
    xadd('pre-flip: recorded history-script sha256 vs the one the first history raw records',
         pfj['history_script_sha256_head'], hj_first['script_sha256'], PF.loc(PF.sw('- History script: sha256 at the working tree')),
         '(%s@%s, script_sha256)' % (HIST_JSON, hist_first[:7]))
    xadd('pre-release: audit files with a redaction-rule value', 0 if 'CLEAN for the audit\'s own pending files' in H.line(h['pre_line']) else '?',
         len(pp['audit_files_not_clean']), H.loc(h['pre_line']), 'prerelease_pending_files.audit_files_not_clean')
    xadd("pre-release: the PI's untracked documents carrying a sensitive value", pi_n_with, len(pi_d1), H.loc(h['pre_pi']),
         'prerelease_pending_files.files[group=other].known')

    # ---------- coverage since each part's commit (computed-new) ----------
    since_hist = git('rev-list', '--reverse', '%s..%s' % (h_scan, head)).split()
    since_pin = git('rev-list', '--reverse', '%s..%s' % (pin, head)).split()
    since_gl = git('rev-list', '--reverse', '%s..%s' % (gl_head, head)).split()

    def tree_paths(c):
        return set(git('ls-tree', '-r', '--name-only', c).split('\n')) - {''}

    t_pin, t_head = tree_paths(c_scan), tree_paths(head)
    raw_added = sorted(p for p in t_head - t_pin if p.startswith('results/raw/'))
    hand_added = sorted(p for p in t_head - t_pin if re.fullmatch(r'HANDOFF-[^/]*\.md', p))
    mod = []
    for ln in git('diff', '--name-status', c_scan, head, '--', 'results/raw', ':(glob)HANDOFF-*.md').split('\n'):
        if ln and ln[0] in 'MRT':
            mod.append(ln.split('\t')[-1])
    users_now = [p for p in git('grep', '-l', '-F', '/Users/', head, '--').split('\n') if p]
    users_now = sorted(p.split(':', 1)[1] for p in users_now)
    users_hist = set(hj['users_paths_at_head'])
    users_new = [p for p in users_now if p not in users_hist]

    # the commits after the gitleaks run: which messages record a per-file gitleaks pass over the commit's files
    # (computed-new; each sentence carried verbatim, beside the number of files the commit changes)
    gl_after = []
    gl_msgs = {}
    for c in since_gl:
        msg_c = git('log', '-1', '--format=%B', c)
        gl_msgs[c] = msg_c
        sents = re.findall(r"[A-Z][^.\n]*per-file gitleaks[^.\n]*\.", msg_c)
        nf = len([p for p in git('diff-tree', '--no-commit-id', '--name-only', '-r', c).split('\n') if p])
        gl_after.append((c, sents, nf))
    gl_after_pass = [x for x in gl_after if x[1]]
    gl_after_none = [x for x in gl_after if not x[1]]
    if roc in since_gl and not any(c == roc and RO_PERFILE in s for c, s, _ in gl_after_pass):
        raise SystemExit("the routing commit's per-file gitleaks pass is not among the sentences found")
    # the commits after the routing commit: which messages record a password scan over the commit's own files
    # (computed-new; each sentence carried verbatim, beside the number of files the commit changes)
    if roc not in since_gl:
        raise SystemExit('the routing commit is not after the gitleaks run on HEAD')
    after_ro = since_gl[since_gl.index(roc) + 1:]
    pw_after = [(c, PW_AFTER_RX.findall(gl_msgs[c]), nf) for c, _, nf in gl_after if c in after_ro]
    pw_after_rec = [x for x in pw_after if x[1]]
    pw_after_none = [x for x in pw_after if not x[1]]
    # a later commit's message on what README-NOTE.md carries of D1-D4 (for D3's record column; README-NOTE.md is not read)
    d3_msg = []
    for c in since_gl:
        at = gl_msgs[c].find(README_D_FRAG)
        if at < 0:
            continue
        rn_at = gl_msgs[c].rfind('\n- ' + README_NOTE, 0, at)
        if rn_at < 0 or '\n- ' in gl_msgs[c][rn_at + 3:at]:
            raise SystemExit('commit %s: %r is not under its README-NOTE.md bullet' % (c[:7], README_D_FRAG))
        d3_msg.append(c)

    # ---------- the PI's rulings of 2026-10-09, item 4: a committed record of it at HEAD? (computed-new) ----------
    own_out = os.path.relpath(os.path.abspath(os.path.join(REPO, a.out)), REPO)
    r4_files = [ln.split(':', 1)[1] for ln in git('grep', '-l', '-i', '-F', '-e', R4_NEEDLE, head, '--', ok=(0, 1)).split('\n') if ln]
    r4_recs = []   # (path, commit that last changed it, line): a tracked line naming both the rulings and N12(i)
    for p in r4_files:
        if p in (own_out, DEFAULT_OUT, os.path.relpath(os.path.abspath(__file__), REPO)):
            continue   # this index's own earlier version, or its own script, not a record of the ruling
        last = git('log', '-1', '--format=%H', head, '--', p).strip()
        for i, ln in enumerate(git('show', '%s:%s' % (head, p)).split('\n'), 1):
            if R4_NEEDLE in ln.lower() and R4_MARK in ln:
                r4_recs.append((p, last, i))
    r4_msgs = git('log', '-i', '-F', '--grep=' + R4_NEEDLE, '--format=%H', head).split()
    r4_msgs_n12 = [c for c in r4_msgs if R4_MARK in git('log', '-1', '--format=%B', c)]
    r4_wt = []    # (path, sha256 at this run, tracked?, lines): working-tree outputs that record it while untracked or changed
    for p in R4_WT:
        fp_ = os.path.join(REPO, p)
        if not os.path.exists(fp_):
            continue
        wb = open(fp_, 'rb').read()
        trk = tracked_at(head, p)
        if trk and git('show', '%s:%s' % (head, p), binary=True) == wb:
            continue   # committed as it stands: found above if it records the ruling
        wl = wb.decode('utf-8', errors='replace').split('\n')
        lns = [i for i, ln in enumerate(wl, 1) if R4_NEEDLE in ln.lower() and R4_MARK in ln]
        if lns:
            # the file's own label for the ruling, on one of those lines; then its other lines naming R4 with N12(i)
            lab = [i for i in lns if R4_LABEL in wl[i - 1]]
            more = [i for i, ln in enumerate(wl, 1) if i not in lns and re.search(r'\bR4\b', ln) and R4_MARK in ln] if lab else []
            r4_wt.append((p, sha256b(wb), trk, lns, lab, more))
    # the N1 v0.6 ledger's 9g, condition (1): whether the tag commit holds the note, the three SVGs and the preprint (the PI's answer decides it)
    n1_9g = None
    fp_ = os.path.join(REPO, N1_LEDGER)
    if os.path.exists(fp_):
        wb = open(fp_, 'rb').read()
        hit = [i for i, ln in enumerate(wb.decode('utf-8', errors='replace').split('\n'), 1) if N1_9G_FRAG in ln]
        if len(hit) == 1:
            if tracked_at(head, N1_LEDGER) and git('show', '%s:%s' % (head, N1_LEDGER), binary=True) == wb:
                n1_9g = '`%s@%s:%d`' % (N1_LEDGER, head[:7], hit[0])
            else:
                n1_9g = '`%s` (%s at this run, sha256 `%s`), its line %d by content' % (
                    N1_LEDGER, 'tracked, changed since HEAD' if tracked_at(head, N1_LEDGER) else 'untracked', sha256b(wb), hit[0])
    # ---------- the PI's answer of 2026-10-12 (computed-new: the tag commit's files, the release-run raws, a record of it) ----------
    tagf = []   # (path, routed form, on-disk form, full sha256 or None, tracked at HEAD, equal to HEAD's blob)
    for p, pre_, suf_ in TAG_FILES:
        fp_ = os.path.join(REPO, p)
        full = sha256b(open(fp_, 'rb').read()) if os.path.exists(fp_) else None
        routed = pre_ + ('...' + suf_ if suf_ else ('' if len(pre_) == 64 else '...'))
        disk = 'absent' if full is None else (full if len(pre_) == 64 else full[:len(pre_)] + ('...' + full[-len(suf_):] if suf_ else '...'))
        trk = tracked_at(head, p)
        eq = trk and full is not None and sha256b(git('show', '%s:%s' % (head, p), binary=True)) == full
        tagf.append((p, routed, disk, full, trk, eq))
    tagf_ok = all(r == d for _, r, d, _, _, _ in tagf)
    rel_all = [p for _, ps in RELEASE_RAWS for p in ps]
    rel_on_disk = [p for p in rel_all if os.path.exists(os.path.join(REPO, p))]
    rel_tracked = [p for p in rel_all if tracked_at(head, p)]
    # the gitleaks hit Code triages FALSE-POSITIVE (housekeeping): the flagged line carries the sha256 of the named file
    fp_line = git('show', '%s:%s' % (GL_FP[0], GL_FP[1])).split('\n')[GL_FP[2] - 1]
    fp_sha = sha256b(git('show', '%s:%s' % (GL_FP[0], GL_FP[3]), binary=True))
    fp_ok = ('"%s": "%s"' % (GL_FP[3], fp_sha)) in fp_line
    # a committed record of the answer at HEAD? (this index's own files left out)
    ans_needle = "answer of 2026-10-12"
    ans_files = [ln.split(':', 1)[1] for ln in git('grep', '-l', '-F', '-e', ans_needle, head, '--', ok=(0, 1)).split('\n') if ln]
    ans_files = [p for p in ans_files if p not in (own_out, DEFAULT_OUT, os.path.relpath(os.path.abspath(__file__), REPO))]
    ans_msgs = git('log', '-F', '--grep=' + ans_needle, '--format=%H', head).split()
    if ans_files or ans_msgs:
        ans_short = 'Committed records of it at HEAD `%s` (computed-new; tracked files naming "%s", this index\'s own files left out): %s; commit messages: %s.' % (
            head[:10], ans_needle, ', '.join('`%s`' % p for p in ans_files) or 'none',
            ', '.join('`git show -s %s` (commit message)' % c[:7] for c in ans_msgs) or 'none')
    else:
        ans_short = 'No committed raw or commit message carries it at HEAD `%s` (computed-new: tracked files and commit messages naming "%s", this index\'s own files left out: 0 and 0); it is recorded here as routed.' % (
            head[:10], ans_needle)
    # section 10, item 4: the files the answer places in the tag commit, and the other untracked notes and renders (names only)
    sup = [p for p in SUPERSEDED if p in untr_other]
    rep_untr = [p for p, _, _, _, trk, _ in tagf if not trk and p != PREPRINT]
    sup_txt = ' [index note: %s (question 5) places in the tag commit note v0.6 and the three 2026-10-10 renders (%s; untracked at this run: %d of %d; sha256 on disk equal to the hashes Code put to the PI: %s, section 12) beside `%s`, which decides the first of the conditions the N1 v0.6 claims ledger\'s 9g leaves to the PI (%s). %s]' % (
        ANSWER, ', '.join('`%s`' % p for p, _, _ in TAG_FILES[:4]), len(rep_untr), 4, yn(tagf_ok), PREPRINT,
        n1_9g or 'its fragment NOT FOUND by content',
        ('Of the files above, the earlier notes and renders (%s) are not among the files the answer names for the tag commit.' % ', '.join('`%s`' % p for p in sup))
        if sup else 'None of the earlier notes and renders is on disk untracked.')

    # ---------- sensitive values: resolve in memory ----------
    forms = list(pp['known_values'].keys())
    labels = {f: pp['known_values'][f][0] for f in forms}
    corpus = git('log', '-p', '--all', '--format=fuller') + '\n' + \
        git('log', '--all', '--format=%an <%ae>%n%cn <%ce>') + '\n' + \
        git('for-each-ref', '--format=%(taggername) %(taggeremail)', 'refs/tags')
    vals = resolve_values(forms, corpus)
    del corpus
    unresolved = [f for f in forms if f not in vals]
    # the guard's own extra value: the session link's bare id (never printed)
    guard_extra = {}
    for f, v in vals.items():
        if labels[f].startswith('claude_session_or_artifact_link') and 'session_' in v:
            guard_extra['the session link\'s bare id'] = v.split('session_', 1)[1]
    # Only the identity emails are set apart in section 11. The laptop hostname counts with the
    # redaction-rule values: this audit's routing names it among the values its public outputs
    # must not carry, although the history raw's pre-release lines group it with the identities.
    ident_labels = {'identity email, public in the commit headers'}
    assert ident_labels <= set(labels.values())

    # ---------- D1 carrier spread: the four RunPod values at the content review's commit and at HEAD ----------
    D1_CLASSES = ('runpod_pod_id', 'runpod_volume_id', 'runpod_volume_name')
    d1_forms = [f for f in forms if labels[f].split(' (')[0] in D1_CLASSES]
    if len(d1_forms) != 4 or any(f not in vals for f in d1_forms) or \
            sum(1 for f in d1_forms if labels[f].startswith('runpod_pod_id')) != 2:
        raise SystemExit('D1: expected 4 resolved values (two pod ids, the volume id, the volume name)')
    stem_forms = [f for f in forms if labels[f].startswith('runpod volume name stem')]
    name_form = [f for f in d1_forms if labels[f].startswith('runpod_volume_name')][0]
    if any(f not in vals or vals[f] not in vals[name_form] or vals[name_form].count(vals[f]) != 1 for f in stem_forms):
        raise SystemExit('D1: the volume-name stem is not resolved, or not once inside the volume name')
    d1_line = C.line(cc['d1'])
    d1_info = {}
    for f in d1_forms:
        mm = FORM_PREFIX.match(f)
        cform = '%s...%s:%s' % (mm.group(1), mm.group(2), mm.group(3))   # the content raw's notation
        row = H.find(lambda s, f=f: s.startswith('| ' + labels[f].split(' (')[0] + ' ') and ('`%s`' % f) in s,
                     'history HEAD-table row of a D1 value', start=h['ids_head'], end=h['fixture'])
        d1_info[f] = {'row': row, 'in_content': cform in d1_line, 'cls': labels[f].split(' (')[0]}
    con3 = [f for f in d1_forms if d1_info[f]['in_content']]
    pod2 = [f for f in d1_forms if not d1_info[f]['in_content']]
    if len(con3) != 3 or len(pod2) != 1 or d1_info[pod2[0]]['cls'] != 'runpod_pod_id':
        raise SystemExit('D1: the content review should name three of the four values, all but one pod id')
    d1_order = sorted(d1_forms, key=lambda f: d1_info[f]['row'])
    d1_name = {}
    for f in d1_forms:
        c = d1_info[f]['cls']
        d1_name[f] = {'runpod_pod_id': "the content review's pod id" if f in con3 else 'the second pod id',
                      'runpod_volume_id': 'the network-volume id', 'runpod_volume_name': 'the volume display name'}[c]
    vol_form = [f for f in d1_forms if d1_info[f]['cls'] == 'runpod_volume_id'][0]

    def bounded(v):
        return re.compile(r'(?<![A-Za-z0-9])%s(?![A-Za-z0-9])' % re.escape(v))

    def d1_cat(p):
        if re.fullmatch(r'HANDOFF-[^/]*\.md', p):
            return 'HANDOFF'
        if p.startswith('results/raw/'):
            return 'raw'
        if p == 'RESULTS.md':
            return 'RESULTS.md'
        if p.endswith(('.py', '.sh')):
            return 'code'
        return 'other'

    def d1_count_at(rev):
        files, dropped = {}, 0
        for f in d1_forms:
            rx, got = bounded(vals[f]), set()
            for ln in git('grep', '-l', '-F', '-e', vals[f], rev, '--', ok=(0, 1)).split('\n'):
                if not ln:
                    continue
                p = ln.split(':', 1)[1]
                if rx.search(git('show', '%s:%s' % (rev, p))):
                    got.add(p)
                else:
                    dropped += 1
            files[f] = got
        msgs = {f: set() for f in d1_forms}
        commits = [c for c in git('log', rev, '--format=%x1e%H%x1f%B').split('\x1e') if c.strip()]
        for c in commits:
            sha, _, msg = c.partition('\x1f')
            for f in d1_forms:
                if bounded(vals[f]).search(msg):
                    msgs[f].add(sha.strip())
        # the volume name's stem: does it occur anywhere outside an occurrence of the full name?
        stem_only = [0, 0]
        for sf in stem_forms:
            sv = vals[sf]
            for ln in git('grep', '-l', '-F', '-e', sv, rev, '--', ok=(0, 1)).split('\n'):
                if ln:
                    t = git('show', '%s:%s' % (rev, ln.split(':', 1)[1]))
                    stem_only[0] += t.count(sv) > t.count(vals[name_form])
            stem_only[1] += sum(1 for c in commits if c.count(sv) > c.count(vals[name_form]))
        return {'files': files, 'msgs': msgs, 'n_commits': len(commits), 'dropped': dropped, 'stem_only': stem_only}

    d1_at = {c_scan: d1_count_at(c_scan), head: d1_count_at(head)}

    def d1_union(rev, fs, key):
        out = set()
        for f in fs:
            out |= d1_at[rev][key][f]
        return out

    def d1_cats(paths):
        n = {k: 0 for k in ('HANDOFF', 'raw', 'RESULTS.md', 'code', 'other')}
        for p in paths:
            n[d1_cat(p)] += 1
        return n

    # the content review's own three values, recounted at the tree it read
    c3 = d1_cats(d1_union(c_scan, con3, 'files'))
    rc = '(recount: git grep at %s, its three values)' % c_scan[:10]
    xadd('D1: tracked HANDOFFs carrying a value, at the content review\'s tree', d1_hand, c3['HANDOFF'], C.loc(c_bul[0]), rc)
    xadd('D1: tracked raws carrying a value, at the content review\'s tree', d1_raws, c3['raw'], C.loc(c_bul[0]), rc)
    xadd('D1: commit messages carrying a value, reachable from the content review\'s tree', d1_msgs,
         len(d1_union(c_scan, con3, 'msgs')), C.loc(c_bul[0]), '(recount: git log %s, its three values)' % c_scan[:10])
    # the routing commit's message: archive v1_3 carries the network-volume id once (line 121)
    v13 = 'archive/PROPOSAL-m-gating-campaign-v1_3.md'
    v13_lines = [i + 1 for i, ln in enumerate(git('show', '%s:%s' % (roc, v13)).split('\n')) if bounded(vals[vol_form]).search(ln)]
    v13_occ = len(bounded(vals[vol_form]).findall(git('show', '%s:%s' % (roc, v13))))
    xadd('D1/D4: occurrences of the network-volume id in `%s`, the routing commit\'s message vs the file' % v13,
         '1 at :121', '%d at %s' % (v13_occ, ', '.join(':%d' % n for n in v13_lines)), ro_loc, '(bounded count, %s at %s)' % (v13, Rs))

    # delta check: files changed after the history raw's commit, read at HEAD
    delta = []
    for ln in git('diff', '--name-status', h_scan, head).split('\n'):
        if not ln or ln[0] not in 'AMRT':
            continue
        p = ln.split('\t')[-1]
        bb = git('show', '%s:%s' % (head, p), binary=True)
        if b'\0' in bb:
            continue
        txt = bb.decode('utf-8', errors='replace')
        hits = {}
        for f, v in vals.items():
            n = count_value(f, v, txt)
            if n:
                hits[labels[f]] = hits.get(labels[f], 0) + n
        delta.append((p, ln[0], hits))
    delta_rule = [(p, s, hs) for p, s, hs in delta if any(k not in ident_labels for k in hs)]
    delta_ident = [(p, s, hs) for p, s, hs in delta if hs and all(k in ident_labels for k in hs)]

    # ---------- README-NOTE.md (presence only: a sibling part's file, content not read) ----------
    rn_exists = os.path.exists(os.path.join(REPO, README_NOTE))
    rn_tracked = tracked_at(head, README_NOTE)
    rn_added = (git('log', '--diff-filter=A', '--format=%h', head, '--', README_NOTE).split() or [None])[-1]
    rn_desc = ('at root, tracked since `%s` (content not restated here)' % rn_added if rn_tracked
               else ('draft at root, untracked (content not restated here)' if rn_exists else 'not present on disk at this run'))
    # ---------- who names this index: the claims ledger (computed-new, at this run) ----------
    cites = []
    for p in LEDGER:
        fp = os.path.join(REPO, p)
        if os.path.exists(fp):
            n = open(fp, encoding='utf-8', errors='replace').read().count(CITE_NEEDLE)
            cites.append('`%s` (%s) %d' % (p, 'tracked' if git('ls-files', '--', p).strip() else 'untracked', n))
        else:
            cites.append('`%s` absent' % p)

    # the ruling's committed-record status, in the index's words (computed-new; section 2b gives the search)
    if r4_recs or r4_msgs_n12:
        r4_short = 'Committed records of it at HEAD `%s`: %d tracked line(s) and %d commit message(s) (section 2b).' % (
            head[:10], len(r4_recs), len(r4_msgs_n12))
    else:
        r4_short = 'No committed raw or commit message carries it before this commit (computed-new at HEAD `%s`, section 2b).' % head[:10]

    # ---------- compose ----------
    me = os.path.relpath(os.path.abspath(__file__), REPO)
    my_sha = sha256b(open(os.path.abspath(__file__), 'rb').read())
    o = []
    w = o.append
    quotes = []   # (line, locator) of every verbatim quote, for the redacted-form list

    def q(line, loc):
        w('> ' + line)
        quotes.append((line, loc))

    REDACTION_SLOT = '\0REDACTION\0'
    w('# AUDIT-note-release v1.2 -- N12 scrub index (release scrub, full history)')
    w('')
    w('- Code stamp (`date -u`): %s' % stamp)
    w('- HEAD at this run: `%s`. Part raws read at their commits: the history raw at `%s` (`%s`), the licenses and content raws and the values-check record at `%s` (`%s`), the pre-flip raw at `%s` (`%s`), the gitleaks and password raws and the LICENSE files at `%s` (`%s`); record locators pinned to `%s` (`%s`).' % (
        head, Hs, hic, A, audit, PFs, pfc, Rs, roc, P, pin))
    w('- Block: `%s`, sha256 `%s` at `%s` (blob), working tree %s; routed `8cd8a9ac...3841`: %s; %d lines.' % (
        BLOCK, blk_sha, P, ('`%s` (equal)' % blk_wt) if blk_wt == blk_sha else ('`%s` (DIFFERS)' % blk_wt), 'MATCH' if blk_sha == BLOCK_SHA else 'MISMATCH', len(blk.lines) - (1 if blk.lines[-1] == '' else 0)))
    w('- Item: N12, `%s@%s:%d-%d`. This file is the output the block names at `%s@%s:%d`. N12 was first run as three part raws (history, licenses, content); three later part raws (the pre-flip reads, gitleaks, the password search) and a regenerated history raw followed, and this index aggregates them. Who cites what, as the part raws state it: the history raw records that the first three are what "the README and the ledger cite together as N12\'s output" (%s); the licenses raw says this file cites it (%s). computed-new, at this run, the number of times the claims ledger names this index (`%s`): %s. `%s`: %s. Whether the README or the ledger should cite this index is not decided here.' % (
        BLOCK, P, b['n12'], b['pass'], BLOCK, P, b['out'], H.loc(h['referent']), L.loc(lc['part']), CITE_NEEDLE, '; '.join(cites),
        README_NOTE, rn_desc))
    w("- The PI's routing of %s, recorded here as it was routed to this part (quoted in substance): (1) the continuity password was supplied out of band and searched (sub-item (iii)); (3) the PI ran gitleaks over all history (sub-item (i)); (4) D1 leave history as is, D2 closed with no match, D3 leave; (5) D4 as routed (section 9); (6) LICENSE: Apache-2.0 for code, CC BY 4.0 for documents and data; (7) the tag `%s`, on the final audit commit after N1 and N18; (9) the GitHub repository has no associated Projects. Items (2) and (8) concern other parts. Where a committed raw or commit message records part of it, the locator is given and the fragment is asserted present; where none does, this index says so." % (ROUTING, TAG))
    w("- %s (the second routing), item 4, recorded here the same way, as it was routed to this part (quoted in substance): %s. %s Items 1-3 and the rulings' other lines (note v0.4 and the 2026-10-09 F1a, F1b and F2 SVGs in place of v0.3 and the 2026-10-06 SVGs, with N1 and N18 re-run on them; N4's correction of record and the control arms' Wilson intervals) concern other parts; the rulings said the tag waited on patch v6, which the PI's routing of 2026-10-12 carries forward as patch v7, the text of record, and %s says \"tag it\" (section 10, items 6 and 7). Section 2b gives the record the ruling rests on, the search for a committed record of it, and what it does not name." % (
        RULINGS[0].upper() + RULINGS[1:], R4_SUBSTANCE, r4_short, ANSWER))
    w("- %s, verbatim: \"%s\". It answers the five N12 pre-flip questions Code put to the PI, recorded here as Code put them (quoted in substance): %s. Code also said it would do the following unless the PI objected, and the PI did not object; they are Code's, not the PI's: %s. The release-run raws are new dated files: the seven scan raws, written at the release commit (R2) with the tag present, before any push, and committed after the tag (R3): %s. The pre-flip read is not part of the release sequence: it runs just before the visibility flip, at the PI's word, after the pre-flip script is updated for the release names in its own commit, made then, which names its raws (section 10, item 1). The tag's own commit hash is to be recorded after tagging, in the note's footer (%s; the footer is the design seat's, outside Code's release sequence, so the note file the tag commit holds does not carry it) and in the post-tag raw `%s`, which Code writes after the push and commits at R3 (the tag commit cannot hold its own hash). %s At this run: the release-run scan raws on disk %d of %d, tracked at HEAD %d of %d; the post-tag raw on disk %s, tracked at HEAD %s. Sections 0, 2, 4, 5, 7, 9 and 10 record what it settles; what is still to run stays REMAINS (section 10)." % (
        ANSWER[0].upper() + ANSWER[1:], ANSWER_TEXT, '; '.join(ANSWER_QS), '; '.join(HOUSEKEEPING),
        ', '.join('`%s`' % p for _, ps in RELEASE_RAWS for p in ps), blk.loc(b['footer']), TAG_RAW, ans_short,
        len(rel_on_disk), len(rel_all), len(rel_tracked), len(rel_all), yn(os.path.exists(os.path.join(REPO, TAG_RAW))),
        yn(tracked_at(head, TAG_RAW))))
    w('- Script: `%s`, sha256 `%s`. Interpreter: `%s` (Python %s; stdlib only). Command: `jlens-qwen36/.venv/bin/python %s` (from the repository root).' % (
        me, my_sha, sys.executable, sys.version.split()[0], me))
    w('- Read-only: `git rev-parse / show / ls-tree / ls-files / log / diff / diff-tree / grep / rev-list / cat-file / for-each-ref / merge-base`. No part script was run and nothing was re-scanned; the part raws are the record and this file indexes them. No git command ran inside `jlens-qwen36/`. The untracked design-seat documents were not opened (names and git tracked status only). Nothing installed, downloaded or inferred. Writes: this file only.')
    w("- Statuses. Each sub-item's outcome is carried from its part raw unchanged, with its cause, and quoted verbatim from the line located by content; this index upgrades none. Its own computations carry `computed-new` (the md and JSON of a part agree, a recount agrees with the figure it checks, a coverage count, the D1 carrier spread or the D4 staging state of section 9) or `discrepant` (they disagree); none of them reproduces a part's scan. Text this index summarizes in its own words (the routing, the PI's rulings of 2026-10-09, item 4, the PI's answer of 2026-10-12, the D1-D4 table, the PI items, the pre-flip checklist) is checked by the script before it writes: each figure is read from the cited line by pattern or asserted present in it, and the answer's record is asserted on the composed text (section 10's statuses; the tag commit's five files hashed on disk, their bytes only, section 12).")
    w(REDACTION_SLOT)
    w('')

    # 0. outcome
    w('## 0. N12 outcome (block `%s@%s:%d`)' % (BLOCK, P, b['pass']))
    w('')
    w('The block\'s pass condition, verbatim (`%s@%s:%d`):' % (BLOCK, P, b['pass']))
    w('')
    q(block_pass, '`%s@%s:%d`' % (BLOCK, P, b['pass']))
    w('')
    w('| sub-item | gates N12? (block :%d) | part raw | outcome, as the part raw states it (verbatim excerpt) | locator |' % b['pass'])
    w('|---|---|---|---|---|')
    w('| (i) secrets, full history | yes | history (the fallback and Code\'s scans) + gitleaks (the block\'s primary scanner) | %s. gitleaks: %s [index note: the STOP is resolved by %s, item 4 (section 2b); the raws\' lines are history and unchanged] | %s; %s; %s, item 4 |' % (
        short['i'], short['gl'], RULINGS, H.loc(h['i_pass']), G.loc(g['o1']), RULINGS))
    w('| (ii) identifiers | no (a list) | history | %s | %s |' % (short['ii'], H.loc(h['s_ii'])))
    w('| (iii) continuity password | no ("Not a release blocker", block :%d) | password | %s %s | %s; %s |' % (
        b['iii'], short['iii_a'], short['iii_p'], PW.loc(pw['absent']), PW.loc(pw['present'])))
    w('| (iv) third-party materials and licenses | yes | licenses (+ history\'s mechanical checks) | %s (at `%s`; the LICENSE files were added later, at `%s`, section 5) | %s; %s |' % (
        short['iv'], l_scan[:10], Rs, L.loc(lc['pass']), H.loc(h['s_iv'])))
    w('| (v) size | yes | history | %s | %s |' % (short['v'], H.loc(h['v_pass'])))
    w('| (vi) content review | no | content | %s | %s |' % (short['vi'], C.loc(cc['pass'])))
    w('| (vii) README-for-readers | no | `README-NOTE.md` (the README part\'s file) | not a part raw: %s (section 8) | `%s@%s:%d`, `:%d-%d` |' % (
        rn_desc, BLOCK, P, b['vii'], b['s6'], b['s6_body']))
    w('')
    w('**Each sub-item, as of this index:**')
    w('')
    w('- (i): gitleaks %d findings, all %s under Code\'s fingerprint-keyed triage (TRUE-SECRET %d, UNTRIAGED %d; %s); trufflehog not run (not installed, %s). The block\'s literal STOP (block :%d; %s) is **resolved by %s, item 4**: the PI accepts Code\'s scans as the resolution of the literal grep rule, which the ruling calls over-written; the %d gitleaks findings are all false positives; D1 stands (history as is) (section 2b).' % (
        gl_o['Findings'], 'FALSE-POSITIVE' if gl_o['FALSE-POSITIVE'] == gl_o['Findings'] else 'NOT FALSE-POSITIVE', gl_o['TRUE-SECRET'], gl_o['UNTRIAGED'],
        G.loc(g['o1']), G.loc(g['o3']), b['i'], H.loc(h['i_pass']), RULINGS, gl_o['Findings']))
    w('- (ii): a list, unchanged in kind; the history raw regenerated at `%s` (scan of `%s`) carries it (%s).' % (Hs, h_scan[:10], H.loc(h['s_ii'])))
    w('- (iii): absent from history at the search\'s ref `%s` (%s); the %d files the routing commit `%s` added after it are not in the history it read (section 1, scope in time). Present only in %d untracked `HANDOFF-*-design.md` files (%s), which the PI keeps out of the repository (D4). Not a release blocker (block :%d).' % (
        pw_ref[:10], PW.loc(pw['ref']), len(ro_files), Rs, pw_with, PW.loc(pw_files[0][1], pw_files[-1][1]), b['iii']))
    w('- (iv): "%s" at `%s`, carried. LICENSE, LICENSE-CC-BY-4.0 and LICENSING.md are now present (added at `%s`). The licenses part raw at `%s` read `%s` and predates them, so the licenses re-run at the release commit is pending (section 5).' % (
        short['iv'], l_scan[:10], Rs, A, l_scan[:10]))
    w('- (v): unchanged (%s): "%s".' % (H.loc(h['v_pass']), short['v']))
    w('- (vi): unchanged (%s): "%s"' % (C.loc(cc['pass']), short['vi']))
    w('- (vii): `README-NOTE.md`, %s; the README part\'s file (section 8).' % rn_desc)
    w('')
    if i_stop and iv_ok and v_ok:
        w('**N12 overall (computed from the three gating lines above):** (i) hits resolved by the PI (%s, item 4; section 2b); (iv) licenses recorded; (v) nothing over 100 MB untreated. Each gating line of the block\'s pass condition (`%s@%s:%d`) is met on the record as carried, so the block\'s *"On fail: STOP on the release; fallback paragraph"* does not apply at this index. (i)\'s pass is "(i) no hits, or hits resolved by the PI", and the record for (i) has two parts. The fallback and Code\'s scans (the history raw at `%s`, a scan of `%s`): %s hit lines, %d TRUE-SECRET-CANDIDATE, %d UNTRIAGED (%s, %s). The block\'s primary scanner, gitleaks, which the history raw says supersedes the fallback for (i) (%s): %d findings, %d TRUE-SECRET, %d UNTRIAGED (%s). Both raws left the resolution to the PI (%s; %s), and %s, item 4, resolves (i) on that record: it accepts Code\'s scans as the resolution of the literal grep rule, which it calls over-written, and D1 stands (history as is). The raws\' own lines are history and are quoted unchanged below; this index carries the ruling as the PI\'s and upgrades no raw.' % (
            RULINGS, BLOCK, P, b['pass'], Hs, h_scan[:10], '{:,}'.format(hits_n), tsc, untri, H.loc(h['i_pass']), H.loc(h['s_i']), H.loc(h['pf4']),
            gl_o['Findings'], gl_o['TRUE-SECRET'], gl_o['UNTRIAGED'], G.loc(g['o1']), H.loc(h['i_pass']), G.loc(g['o3']), RULINGS))
        w('')
        w('N12 at the release commit. (iv) and (v) are carried as their parts read them, at %s; N12 passes at the release commit only if the pre-flip re-runs (section 10, item 3) again print "(iv) licenses recorded" and the (v) PASS. The licenses script prints its pass line only when all of its gates hold, among them "%s" and "%s" (%s, %s); otherwise it prints "(iv) NOT recorded" (%s). The licenses part projects that these two gates fail at that re-run until the ids and hosts in this audit\'s own files are classified (section 5); %s, question (2), confirms the licenses script\'s rule changes that classify them, and the re-run with them is still to run (section 10, item 3). For (i), %s, question (3), says ruling 4 (%s, item 4) covers the release run\'s (i) at 0 true-secret candidates and 0 untriaged, and question (4) accepts gitleaks\' default skip of `.svg` files and trufflehog not run; the release run itself, the history script\'s re-run and a gitleaks run over all history at the release commit, is still to run (section 10, items 3 and 5), and the answer covers (i) there at those figures.' % (
            ('`%s`' % l_scan[:10]) if l_scan == h_scan else '`%s` ((iv)) and `%s` ((v))' % (l_scan[:10], h_scan[:10]),
            sweep_gates[0], sweep_gates[1], LS.loc(ls_gate[0]), LS.loc(ls_gate[1]), LS.loc(ls_fail), ANSWER, ANSWER, RULINGS))
    else:
        w('**N12 overall:** the carried lines do not match the expected pattern ((i) the history raw\'s pass/STOP line as expected=%s, (iv) recorded=%s, (v) PASS=%s); read the part raws.' % (i_stop, iv_ok, v_ok))
    w('')

    # 1. part raws
    w('## 1. Part raws indexed')
    w('')
    w('| file | read at | sha256 there | lines | last changed at that commit | working tree equals it | commit the part read |')
    w('|---|---|---|---|---|---|---|')
    readat = {HIST_MD: h_scan, HIST_JSON: h_scan, LIC_MD: l_scan, LIC_JSON: l_scan, CON_MD: c_scan, CON_JSON: c_scan,
              PF_MD: pf_head, PF_JSON: pf_head, GL_MD: gl_head, PW_MD: pw_ref}
    for path, short_, s, n, eq, last in parts:
        w('| `%s` | `%s` | `%s` | %d | %s | %s | `%s` |' % (path, short_, s, n, yn(last), {True: 'yes', False: 'NO', None: 'absent'}[eq], readat[path][:10]))
    w('')
    w('The history raw was first committed at `%s` (a scan of `%s`; fallback %s hit lines) and regenerated at `%s` (a scan of `%s`; fallback %s hit lines) after the guard fix of its round 5 (%s). This index reads the regenerated raw; every history locator below is at `%s`.' % (
        hist_first[:7], hj_first['head'][:10], '{:,}'.format(hj_first['fallback']['hit_lines']), Hs, h_scan[:10], '{:,}'.format(hits_n), H.loc(h['vc5']), Hs))
    w('')
    sc_rows = [x for x in xc if x[0].endswith('script sha256 recorded vs committed')]
    sc_bad = [x[0].split(' script')[0] for x in sc_rows if x[5] != 'computed-new (agree)']
    sc_txt = ('each equals the committed script (section 12)' if not sc_bad else
              'section 12 marks %s discrepant: the recorded sha256 does not equal the committed script' % ', '.join(
                  'the %s script\'s row' % n_ for n_ in sc_bad))
    if lic_script_rec is None:
        lic_txt = 'The licenses raw records no script sha256 (its header line `- Script:` names the script only).'
    else:
        lic_txt = 'The licenses raw\'s `- Script:` line records sha256 `%s`, which %s the committed script (%s).' % (
            lic_script_rec.group(1), 'equals' if lic_script_rec.group(1) == scr[LIC_SCRIPT][0] else 'does NOT equal', L.loc(L.sw('- Script:')))
    w('Part scripts at their commits: %s. The history, content, pre-flip, gitleaks and password raws each record their script\'s sha256; %s. %s' % (
        '; '.join('`%s` @`%s` `%s`' % (sp, s_[1], s_[0]) for sp, s_ in scr.items()), sc_txt, lic_txt))
    w('')
    w('Scope in time. The history raw read `%s`; the licenses part `%s`; the content part `%s`; the pre-flip reads `%s`; gitleaks and the password search `%s`. Commits now on HEAD after `%s`: %d (%s), which the history scan does not cover (section 11 checks what they changed). Commits after `%s`: %d (%s), which no gitleaks run recorded here covers beyond the per-file passes that %d of their messages record over the commit\'s own files (section 2a). The password search\'s ref is %s`%s` (%s): none of the %d files the routing commit `%s` added is in the history it read. Its (4) also read every untracked, not-ignored file at its run (%s), but the raw counts those (%d) and itemizes only the %d with it, so which of the %d it read is not recorded. For the %d `archive/PROPOSAL-m-gating-campaign-v1_*.md` files the routing commit also records its pre-commit screen ("the password absent", %s); for the other %d nothing further is recorded here. Commits after `%s`: %d, outside the content review\'s tree (section 7).' % (
        h_scan[:10], l_scan[:10], c_scan[:10], pf_head[:10], gl_head[:10], h_scan[:10], len(since_hist), ', '.join('`%s`' % c[:10] for c in since_hist) or 'none',
        gl_head[:10], len(since_gl), ', '.join('`%s`' % c[:10] for c in since_gl) or 'none', len(gl_after_pass),
        'the same ' if pw_ref == gl_head else '', pw_ref[:10], PW.loc(pw['ref']), len(ro_files), Rs, PWS.loc(pws_scope, pws_scope + 1),
        pw_untr, pw_with, len(ro_files), len(ro_pm), ro_loc, len(ro_rest),
        c_scan[:10], len(since_pin)))
    w('')

    # 2. (i)
    w('## 2. (i) Secrets over the entire history (block `%s@%s:%d`)' % (BLOCK, P, b['i']))
    w('')
    w('Outcome and pass line of the fallback and Code\'s scans, verbatim (%s):' % H.loc(h['i_pass']))
    w('')
    q(i_line, H.loc(h['i_pass']))
    w('')
    w('Summary line, verbatim (%s):' % H.loc(h['s_i']))
    w('')
    q(H.line(h['s_i']), H.loc(h['s_i']))
    w('')
    w('These two lines are the history raw\'s own words at `%s` and are history, quoted unchanged: the STOP they state is resolved by %s, item 4 (section 2b).' % (Hs, RULINGS))
    w('')
    w('- Section: %s. At the history run the block\'s primary scanners had not been run: %s (installable via Homebrew, not installed without the PI\'s word). The history raw labels running the fallback in their place a deviation from block :77, verbatim (%s): "%s" Since then the PI installed and ran gitleaks (section 2a); trufflehog was not run.' % (
        H.loc(h['i']), H.loc(h['scanners']), H.loc(h['scanners']), deviation))
    w('- The history raw\'s pass-phrase-shaped values: %d (%s), the LoRA overfit phrase (%s) and a fragment of the class\'s own regular expression, FALSE-POSITIVE (%s).' % (
        n_pp, H.loc(h['passphrase']), H.loc(pp_lora), H.loc(pp_regex)))
    w('- Values-check rounds 1-%d of this part: %s to the end of the file; process record for rounds 1-4: %s; round 5 (the guard fix) and its second check are recorded in the history raw itself (%s, %s).' % (
        n_vc_rounds, H.loc(h['vc1']), VC.loc(vc['h']), H.loc(h['vc5']), H.loc(h['vc5b'])))
    w('- Scope: every object reachable from the %d local refs at `%s` (%s); refs that exist only on GitHub are covered by the pre-flip reads (section 10, item 1).' % (n_refs, h_scan[:10], H.loc(h['scope'])))
    w('- The pre-flip raw flagged at `%s` that the committed history script refused to write at HEAD (%s); the round-5 fix at `%s` answers that flag, and the regenerated raw says of itself, verbatim (%s): "%s"' % (
        pf_head[:7], PF.loc(pf['p3a']), Hs, H.loc(h['interim']), H.line(h['interim'])))
    w('')
    w('### 2a. gitleaks, the block\'s primary scanner (`%s`)' % GL_MD)
    w('')
    w('- Run: gitleaks 8.30.1, installed by the PI, over all history with secrets redacted at source (%s); %d commits scanned (%s); HEAD `%s` (%s). The PI\'s own run reported 4 leaks, and Code\'s run finds %d (%s).' % (
        G.loc(g['cmd']), gl_commits, G.loc(g['commits']), gl_head[:10], G.loc(g['head']), gl_leaks, G.loc(g['pi'])))
    w('')
    w('| # | rule | file | commit | line | Code\'s verdict | locator |')
    w('|---|---|---|---|---|---|---|')
    for r in gl_rows:
        w('| %d | %s | `%s` | `%s` | %d | %s | %s |' % (r['n'], r['rule'], r['file'], r['commit'], r['line'], r['verdict'], G.loc(r['at'])))
    w('')
    w('Outcome, verbatim (%s):' % G.loc(g['o1'], g['o3']))
    w('')
    for n in (g['o1'], g['o2'], g['o3']):
        q(G.line(n), G.loc(n))
    w('')
    w('- The raw\'s "Resolving (i) remains the PI\'s act" (%s) stays as the raw\'s own words: the raw is history and is not edited. %s, item 4, answers it (section 2b).' % (
        G.loc(g['o3']), RULINGS[0].upper() + RULINGS[1:]))
    w('- The verdicts are keyed by gitleaks fingerprint (commit:file:rule:line) in the committed script\'s triage table (%s, %d keys); each of the %d rows matches exactly one key with the same verdict: %s (section 12).' % (
        GS.loc(gs_tri, gs_end), len(fp_keys), len(gl_rows), yn(gl_matched == len(gl_rows))))
    w('- The commits after `%s` (computed-new): %d (section 1, scope in time). %d of their messages record a per-file gitleaks pass over the commit\'s own files, verbatim, each beside the number of files the commit changes (`git diff-tree -r`): %s. The other %d record none (%s). No gitleaks run over the commits after `%s` is recorded here. The release run puts one in their place: gitleaks over all history at the release commit, its raw `%s` committed after the tag (section 10, item 5); %s, question (4), accepts its default skip of `.svg` files and trufflehog not run. Code\'s housekeeping, not objected by the PI, triages one gitleaks hit in the commits after the run above FALSE-POSITIVE: `%s` `%s:%d`, flagged on the word \'keys\', carries the sha256 of `%s` (computed-new: the line holds that file\'s sha256 at that commit: %s; section 12).' % (
        gl_head[:7], len(gl_after), len(gl_after_pass),
        '; '.join('`%s` "%s" (`git show -s %s` (commit message); %d files)' % (c[:7], ' '.join(s), c[:7], nf) for c, s, nf in gl_after_pass) or 'none',
        len(gl_after_none), ', '.join('`%s`' % c[:7] for c, _, _ in gl_after_none) or 'none', gl_head[:7],
        RR['gitleaks'][0], ANSWER, GL_FP[0][:10], GL_FP[1], GL_FP[2], GL_FP[3], yn(fp_ok)))
    w('')

    # 2b. the PI's rulings of 2026-10-09, item 4
    w('### 2b. (i) resolved: %s, item 4' % RULINGS)
    w('')
    w('- As routed to this part (quoted in substance): %s.' % R4_SUBSTANCE)
    if r4_recs or r4_msgs_n12:
        rec_txt = 'Committed records of it at HEAD `%s` (computed-new; a tracked line naming both "%s" and `%s`, found by content, this index\'s own earlier version left out): %s; commit messages naming both: %s.' % (
            head[:10], R4_NEEDLE, R4_MARK, '; '.join('`%s@%s:%d`' % (p, c[:7], i) for p, c, i in r4_recs) or 'none',
            ', '.join('`git show -s %s` (commit message)' % c[:7] for c in r4_msgs_n12) or 'none')
    else:
        rec_txt = 'Committed record: none. No committed raw or commit message carries this ruling before this commit (computed-new at HEAD `%s`: tracked files with a line naming both "%s" and `%s`, this index\'s own earlier version left out: %d; commit messages reachable from HEAD naming "%s": %d (%s), of which naming `%s` as well: %d). It is recorded here as routed.' % (
            head[:10], R4_NEEDLE, R4_MARK, len(r4_recs), R4_NEEDLE, len(r4_msgs), ', '.join('`%s`' % c[:7] for c in r4_msgs) or 'none', R4_MARK, len(r4_msgs_n12))
    wt_txt = ''
    if r4_wt:
        wt_txt = ' In the working tree, %s.' % '; '.join(
            '`%s` (%s at this run, sha256 `%s`) records it on the line(s) naming both "%s" and `%s`: %s%s' % (
                p, 'tracked, changed since HEAD' if trk else 'untracked', s_, R4_NEEDLE, R4_MARK, ', '.join(map(str, lns)),
                ('; it labels the ruling R4 ("%s", line %s), and names `R4` with `%s` on %d further line(s): %s' % (
                    R4_LABEL, ', '.join(map(str, lab)), R4_MARK, len(more), ', '.join(map(str, more)) or 'none')) if lab else '')
            for p, s_, trk, lns, lab, more in r4_wt)
    w('- %s%s' % (rec_txt, wt_txt))
    w('- What it rests on, in the record (each figure read from the cited line):')
    w('  - The literal grep rule: block :%d\'s fallback (%s), under which "Any hit in history is a STOP on the release" (`%s@%s:%d`). The history raw\'s pass/STOP line puts (i) at STOP on that text because "the fallback returns %d hit lines, so (i) is not \'no hits\'" (%s). The ruling accepts Code\'s scans as the resolution of that rule and calls the rule over-written.' % (
        b['i'], '`git log -p --all | grep -nEi ...`', BLOCK, P, b['i'], hits_n, H.loc(h['i_pass'])))
    w('  - Code\'s own scans: TRUE-SECRET-CANDIDATE %d and UNTRIAGED %d over the fallback\'s hits and the precise-pattern and high-entropy scans (%s, %s); Code\'s gitleaks triage: TRUE-SECRET %d, UNTRIAGED %d (%s).' % (
        tsc, untri, H.loc(h['s_i']), H.loc(h['i_pass']), gl_o['TRUE-SECRET'], gl_o['UNTRIAGED'], G.loc(g['o1'])))
    w('  - %s over every ref at its run (`--log-opts=--all`, %s; HEAD `%s`, %s; %d commits scanned, %s): %d findings, FALSE-POSITIVE %d, each row matched to one fingerprint key of the committed script\'s triage table with the same verdict: %s (section 2a; %s).' % (
        gl_scanner, G.loc(g['cmd']), gl_head[:10], G.loc(g['head']), gl_commits, G.loc(g['commits']), gl_o['Findings'], gl_o['FALSE-POSITIVE'],
        yn(gl_matched == len(gl_rows)), G.loc(g['o1'])))
    w('  - D1 stands (history as is): block :%d\'s "history rewriting is a PI decision", decided as the first routing decided it (section 9, D1).' % b['i'])
    w('- The raws are history and are not edited: the history raw\'s pass/STOP line and summary line still read "STOP pending the PI\'s resolution" (%s, %s), and the gitleaks raw\'s "Resolving (i) remains the PI\'s act" stays as its own words (%s); the ruling answers them. Section 12 checks the ruling\'s figures, as recorded here, against those raws.' % (
        H.loc(h['i_pass']), H.loc(h['s_i']), G.loc(g['o3'])))
    w('- Not named by the ruling, as routed to this part: trufflehog (not run, not installed, %s); the commits after `%s` (section 2a; section 10, item 5); and whether the fallback\'s hits at the history script\'s release-commit re-run (section 10, item 3) are resolved the same way. %s answers them: question (3), ruling 4 covers the release run\'s (i) (0 true-secret candidates, 0 untriaged); question (4), gitleaks\' default skip of `.svg` files and trufflehog not run are acceptable. The release run that question (3) reaches is still to run (section 10, items 3 and 5).' % (
        G.loc(g['o3']), gl_head[:7], ANSWER[0].upper() + ANSWER[1:]))
    w('')

    # 3. (ii)
    w('## 3. (ii) Identifiers (block `%s@%s:%d`)' % (BLOCK, P, b['ii']))
    w('')
    w('Outcome, verbatim (the summary line; %s):' % H.loc(h['s_ii']))
    w('')
    q(ii_line, H.loc(h['s_ii']))
    w('')
    w('- Commit identities (published with the history): %s. Identifier classes in content: %s. Identifiers present at HEAD, with every HEAD locator: %s. An identifier in tracked code (a test fixture): %s.' % (
        H.loc(h['identities']), H.loc(h['classes']), H.loc(h['ids_head']), H.loc(h['fixture'])))
    w('- `/Users/` in tracked files at HEAD (the block asks for the list and a recommendation): %s; the recommendation, verbatim (%s):' % (H.loc(h['users']), H.loc(h['users_rec'])))
    w('')
    q(H.line(h['users_rec']), H.loc(h['users_rec']))
    w('')
    w('- `/workspace/` (box paths) at HEAD: %s.' % H.loc(h['workspace']))
    w('- computed-new: tracked files containing `/Users/` at HEAD `%s` now: %d (the history raw counted %d at `%s`); added since: %d%s. The content raw asks that the final list come from `git grep -l /Users/` at the tag commit (%s).' % (
        head[:10], len(users_now), len(users_hist), h_scan[:10], len(users_new),
        (' (%s)' % ', '.join('`%s`' % p for p in users_new)) if users_new else '', C.loc(cc['users'])))
    w('- Hand-offs to this list from the content review: %s (hostnames, %s; SSH, %s; `/Users/` paths, %s) and the stale statements that the repository is private, %s. Its section 7 also hands this list the known carriers outside N12(vi)\'s scope (%s): %s.' % (
        C.loc(cc['s8']), C.loc(cc['host']), C.loc(cc['ssh']), C.loc(cc['users']), C.loc(cc['stale']),
        C.loc(cc['outside'], cc['outside'] + len(out_carriers)), '; '.join(d for _, d in out_carriers)))
    w('- The redacted forms in the part raws protect only those raws, not the release: every one of these values is in the history being published, and some can be recovered from their redacted form by enumeration (%s).' % H.loc(h['caveat']))
    w('- The decisions this list feeds: D1 (RunPod identifiers; routed: leave history as is) and D3 (commit metadata; routed: leave), section 9.')
    w('')

    # 4. (iii)
    w('## 4. (iii) The continuity password (block `%s@%s:%d`)' % (BLOCK, P, b['iii']))
    w('')
    w('**Status: run** (the password raw, committed at `%s`, at ref `%s`). The block: "Not a release blocker" (`%s@%s:%d`). The value was supplied by the PI out of band; the raw states, verbatim (%s): "It is written nowhere, and neither is its length or any hash of it." This index writes no form of it either.' % (
        Rs, pw_ref[:10], BLOCK, P, b['iii'], PW.loc(pw['value'])))
    w('')
    w('Results, verbatim (%s, %s, %s, %s):' % (PW.loc(pw['r1']), PW.loc(pw['r2']), PW.loc(pw['r3']), PW.loc(pw['r4'])))
    w('')
    for n in (pw['r1'], pw['r2'], pw['r3'], pw['r4']):
        q(PW.line(n), PW.loc(n))
    w('')
    w('Outcome, verbatim (%s, %s, %s):' % (PW.loc(pw['absent']), PW.loc(pw['present']), PW.loc(pw['d2'])))
    w('')
    for n in (pw['absent'], pw['present'], pw['d2']):
        q(PW.line(n), PW.loc(n))
    w('')
    w('- The %d files that carry it are untracked `HANDOFF-*-design.md` files (%s), on the PI\'s D4 list of files not to commit (section 9). computed-new at HEAD `%s`: tracked %d of %d; in any commit on any ref (`git log --all -- <path>`) %d of %d.' % (
        pw_with, PW.loc(pw_files[0][1], pw_files[-1][1]), head[:10], sum(1 for _, t, _ in pw_now if t), len(pw_now),
        sum(1 for _, _, e in pw_now if e), len(pw_now)))
    w('- Block :%d asks that a hit be reported with "the file and commit" if present anywhere, and leaves rotating or retiring the password to the PI in that case; the raw finds it in no commit reachable at its ref and says the condition does not arise for the history, so no commit is reported. The routing as it reached this part says nothing further on it.' % b['iii'])
    w('- Time bound: the search read history at `%s` (%s). The %d files the routing commit `%s` added after it are not in that history; whether its scan of the untracked files at its run read any of them is not recorded (section 1, scope in time). The commit\'s message records a pre-commit screen of its %d `archive/PROPOSAL-m-gating-campaign-v1_*.md` files with "the password absent" (%s); for its other %d files nothing further is recorded here. Of the %d commits on HEAD after `%s` (computed-new), %s The release run repeats the password search at the release commit: Code\'s own run, its raw `%s` committed after the tag (section 10, item 3); until then the bound above stands.' % (
        pw_ref[:10], PW.loc(pw['ref']), len(ro_files), Rs, len(ro_pm), ro_loc, len(ro_rest), len(pw_after), Rs,
        ('%d record in their messages a password scan over the commit\'s own files, verbatim, each beside the number of files the commit changes (`git diff-tree -r`): %s (section 2a); the other %d record none (%s).' % (
            len(pw_after_rec), '; '.join('`%s` "%s" (`git show -s %s` (commit message); %d files)' % (c[:7], ' '.join(s), c[:7], nf) for c, s, nf in pw_after_rec),
            len(pw_after_none), ', '.join('`%s`' % c[:7] for c, _, _ in pw_after_none) or 'none')) if pw_after_rec
        else 'none records a password scan in its message.', RR['password'][0]))
    w('- Earlier records: the history raw\'s pass-phrase class (%s) and its `continuity` counts (%s, %s); the content review\'s D2 and flag F44 (%s, %s) and its hand-off for (iii) (%s). D2 is closed by the PI: no match (%s; %s).' % (
        H.loc(h['passphrase']), H.loc(h['continuity_md']), H.loc(h['continuity']), C.loc(cc['d2']), C.loc(cc['s52']), C.loc(cc['h_iii']),
        PW.loc(pw['d2']), ro_loc))
    w('')

    # 5. (iv)
    w('## 5. (iv) Third-party materials and licenses (block `%s@%s:%d`)' % (BLOCK, P, b['iv']))
    w('')
    w('Outcome and pass line, verbatim (%s; the licenses part read `%s`):' % (L.loc(lc['pass']), l_scan[:10]))
    w('')
    q(l_line, L.loc(lc['pass']))
    w('')
    w('(iv)\'s mechanical checks (jlens-qwen36 tracking, the `.npz` allowlist, model weights), verbatim (%s; section %s):' % (H.loc(h['s_iv']), H.loc(h['iv'])))
    w('')
    q(iv_mech_line, H.loc(h['s_iv']))
    w('')
    w('**The repository\'s license, added after the licenses part\'s read (`%s`).** The PI\'s routing of %s: Apache-2.0 for code, CC BY 4.0 for documents and data; the routing commit records "%s" (%s). computed-new:' % (
        Rs, ROUTING, 'LICENSE, LICENSE-CC-BY-4.0 and LICENSING.md, per the PI.', ro_loc))
    w('')
    w('| file | added at | sha256 | lines | working tree equals it | identifies |')
    w('|---|---|---|---|---|---|')
    w('| `LICENSE` | `%s` | `%s` | %d | %s | opens "Apache License", "Version 2.0, January 2004" |' % (
        lic['LICENSE']['added'][:7], lic['LICENSE']['sha'], lic['LICENSE']['lines'], {True: 'yes', False: 'NO', None: 'absent'}[lic['LICENSE']['wt']]))
    w('| `LICENSE-CC-BY-4.0` | `%s` | `%s` | %d | %s | opens "Attribution 4.0 International" |' % (
        lic['LICENSE-CC-BY-4.0']['added'][:7], lic['LICENSE-CC-BY-4.0']['sha'], lic['LICENSE-CC-BY-4.0']['lines'], {True: 'yes', False: 'NO', None: 'absent'}[lic['LICENSE-CC-BY-4.0']['wt']]))
    w('| `LICENSING.md` | `%s` | `%s` | %d | %s | the map: code to Apache-2.0 (%s), documents and data to CC BY 4.0 (%s); third-party material (%s) |' % (
        lic['LICENSING.md']['added'][:7], lic['LICENSING.md']['sha'], lic['LICENSING.md']['lines'], {True: 'yes', False: 'NO', None: 'absent'}[lic['LICENSING.md']['wt']],
        LG.loc(lg['code']), LG.loc(lg['docs']), LG.loc(lg['tp'])))
    w('')
    w('- The two license texts\' sha256 equal the values LICENSING.md lists for them (%s, %s; section 12).' % (LG.loc(lg['row_a']), LG.loc(lg['row_c'])))
    w('- The licenses part raw read `%s` and predates these files: its "the repository has no LICENSE file" (%s), its PI item 2 (%s) and its section-5 count of %d (%s) describe that commit. **The licenses re-run at the release commit is pending** (section 10, item 3). %s, question (2), confirms the licenses script\'s rule changes that classify the ids and hosts this audit\'s own files carry; the re-run with them writes `%s` and `%s`, committed after the tag.' % (
        l_scan[:10], L.loc(lc['pass']), L.loc(lc['it2']), len(lic_rule_lread), L.loc(lc['s5'] + 2), ANSWER[0].upper() + ANSWER[1:], RR['licenses'][0], RR['licenses'][1]))
    w('%s Its section-5 count does read the tree, with the rule at %s; at HEAD `%s` that rule matches %d file(s) (%s); `LICENSE-CC-BY-4.0` and `LICENSING.md` do not match it. %s' % (
        ls_lead, LS.loc(ls_rule), head[:10], len(lic_rule_head), ', '.join('`%s`' % p for p in lic_rule_head) or 'none',
        ls_route_txt))
    w('- The licenses raw\'s other PI items stay as it states them: the Macar prompt text is CC BY 4.0 via the paper if the PI accepts that source, the two word lists have no license found (%s), and the Global Workspace paper\'s license was not read (%s). LICENSING.md attributes the Macar text to the paper\'s CC BY 4.0 (%s) and the Lindsey (2025) lists to their source without relicensing them (%s); it names the Global Workspace paper %d time(s). Whether that settles the items is the PI\'s; the routing as it reached this part names the two licenses only.' % (
        L.loc(lc['it1']), L.loc(lc['it7']), LG.loc(lg['macar']), LG.loc(lg['lindsey']), lg_gw))
    w('- The licenses table for the README: %s. The PI items: %s (item 1, the Macar materials: %s; item 2, no license, now superseded by the files above: %s; item 5, the lenses: %s; item 7, the Global Workspace paper: %s).' % (
        L.loc(lc['s6']), L.loc(lc['s7']), L.loc(lc['it1']), L.loc(lc['it2']), L.loc(lc['it5']), L.loc(lc['it7'])))
    w('- Residual-space float vectors stored in tracked JSON (a stored readability probe), which the history raw says the README should name; the regenerated raw also lists %s further float arrays "not read in context -- they need a reading before the README\'s statement is final": %s.' % (
        floats_other, H.loc(h['floats'])))
    w('- The content review\'s hand-off for (iv): %s (single-line quotes, inside referent checks, from scripts in the gitignored `jlens-qwen36/` clone; citations of published works only).' % C.loc(cc['h_iv'], cc['h_iv'] + 2))
    w('- Carried caveat for the pre-flip re-run, a projection: at the licenses run this audit\'s own files were untracked (%d files), and projected over them with the sweeps\' rules the id sweep would gain %d unclassified id(s) and the host sweep %d unclassified host(s); on that projection %s and %s say the licenses part\'s two sweep gates would fail at the pre-flip re-run until each is classified. Whether they do depends on the counts at the re-run: an open minor values-check finding (%s) says both sentences are worded to hold whatever the counts are, and proposes making them depend on the counts.' % (
        proj_n_files, proj_ids, proj_hosts, L.loc(lc['proj']), L.loc(lc['it8']), VC.loc(vc_proj)))
    w('')

    # 6. (v)
    w('## 6. (v) Size (block `%s@%s:%d`)' % (BLOCK, P, b['v']))
    w('')
    w('Outcome and pass line, verbatim (%s):' % H.loc(h['v_pass']))
    w('')
    q(v_line, H.loc(h['v_pass']))
    w('')
    w('Summary line, verbatim (%s):' % H.loc(h['s_v']))
    w('')
    q(H.line(h['s_v']), H.loc(h['s_v']))
    w('')
    w('- Section, with `git count-objects -vH`, the files at HEAD over 40 MB and the 25 largest blobs: %s.' % H.loc(h['v']))
    w('')

    # 7. (vi)
    w('## 7. (vi) Content review of `results/raw/` and `HANDOFF-*.md` (block `%s@%s:%d`)' % (BLOCK, P, b['vi']))
    w('')
    w('Outcome and pass line, verbatim (%s, with its two bullets %s):' % (C.loc(cc['pass']), C.loc(c_bul[0], c_bul[1])))
    w('')
    q(c_line, C.loc(cc['pass']))
    for n in c_bul:
        q(C.line(n), C.loc(n))
    w('')
    w('File count, verbatim (%s):' % C.loc(cc['count']))
    w('')
    q(C.line(cc['count']), C.loc(cc['count']))
    w('')
    w('Refuter totals, verbatim (%s):' % C.loc(cc['totals']))
    w('')
    q(C.line(cc['totals']), C.loc(cc['totals']))
    w('')
    w('- Flags that survived refutation: %s; this writer\'s dispositions of the rest: %s onward; not reviewed: %s; hand-offs to this index: %s.' % (
        C.loc(cc['s4']), C.loc(C.sw('## 5. Flags with no refuter verdict')), C.loc(cc['s7']), C.loc(cc['s8'])))
    n_new = len(raw_added) + len(hand_added)
    scope_bits = []
    if n_new:
        scope_bits.append('The %d added path(s) were not in that tree, so none was in N12(vi)\'s scope' % n_new)
    if mod:
        scope_bits.append('The %d modified path(s) were in that tree in their earlier versions only; their changes since were not reviewed (%s)' % (
            len(mod), ', '.join('`%s`' % p for p in mod)))
    scope_txt = (' '.join(b_ + '.' for b_ in scope_bits)) if scope_bits else 'Nothing under `results/raw/` or `HANDOFF-*.md` changed since that tree.'
    w('- Scope: the review read the tree at `%s` (%s). computed-new: paths under `results/raw/` added between `%s` and HEAD `%s`: %d; modified: %d; `HANDOFF-*.md` added: %d. %s Its %s lists the audit\'s outputs as not reviewed, and %s asks that every new raw be read once, end to end, before the push.' % (
        c_scan[:10], C.loc(cc['head']), c_scan[:10], head[:10], len(raw_added), len(mod), len(hand_added), scope_txt, C.loc(cc['s7']), C.loc(cc['rerun'])))
    if raw_added:
        w('  - added: ' + ', '.join('`%s`' % p.replace('results/raw/', '') for p in raw_added) + ' (all under `results/raw/`).')
    if hand_added:
        w('  - `HANDOFF-*.md` added: ' + ', '.join('`%s`' % p for p in hand_added) + '.')
    w('- The content script\'s re-run at the release commit is still to run (section 10, item 3). %s, question (1), accepts the fix to its leak guard, which fired on the script\'s own earlier output; the re-run writes `%s`, committed after the tag.' % (
        ANSWER[0].upper() + ANSWER[1:], RR['content'][0]))
    w('')

    # 8. (vii)
    w('## 8. (vii) README-for-readers (block `%s@%s:%d`; contents at `:%d-%d`)' % (BLOCK, P, b['vii'], b['s6'], b['s6_body']))
    w('')
    w('- `README-NOTE.md`: %s. The README part writes it; this index neither reviews nor fingerprints it. As routed (D4), it states in one line that the design-seat handoffs are held for a separate write-up on the workflow; this index does not check that line. The history raw\'s pre-release re-scan wants the README in place before the end commit (%s).' % (
        rn_desc, H.loc(h['pf1'])))
    w('- N12 inputs to the README, from the part raws: the licenses table (block §6 item (7)), %s, and now `LICENSING.md` (section 5); name the residual-space probe vectors stored in JSON, %s; cite no `/Users/` path, %s; give the Global Workspace paper\'s full title and link and credit Lindsey (2025), %s and %s.' % (
        L.loc(lc['s6']), H.loc(h['floats']), H.loc(h['users_rec']), L.loc(lc['it7']), L.loc(lc['it1'])))
    w('')

    # 9. decisions
    w('## 9. Decisions for the PI (D1-D4), the PI\'s routing of %s, and the other open PI items' % ROUTING)
    w('')
    w('D1-D4 are the content review\'s, which it introduces as "%s" (%s). The PI\'s routing of %s decides them, as routed to this part. The table summarizes the content review\'s cited lines at `%s` and the routing; the script reads each figure from the cited line or asserts it present there, apart from the computed-new figures (the D1 spread at HEAD, the D4 staging state) and the index\'s own notes. The redacted values are at the locators.' % (
        C.line(cc['dec']).rstrip('.'), C.loc(cc['dec']), ROUTING, A))
    w('')
    w('| id | what | options the part raw gave | the PI\'s routing of %s (as routed to this part) | committed record of the routing | locators |' % ROUTING)
    w('|---|---|---|---|---|---|')
    hd = d1_at[head]
    h_all = d1_union(head, d1_forms, 'files')
    h_cat = d1_cats(h_all)
    h_msgs = d1_union(head, d1_forms, 'msgs')
    pod2_head = sorted(hd['files'][pod2[0]])
    pod2_txt = ('the second pod id is at HEAD in %s only' % ', '.join('`%s`' % p for p in pod2_head)) if pod2_head \
        else 'the second pod id is in no tracked file at HEAD'
    other_head = sorted(p for p in h_all if d1_cat(p) in ('code', 'other'))
    w('| D1 | The RunPod pod id, network-volume id and volume display name of the Phase-2 box (account-resource identifiers, not credentials). The content review\'s counts are at `%s`, the tree it read (%s): %d tracked HANDOFFs, %d tracked raws and %d commit messages (%s), with RESULTS.md and a code test fixture outside its scope (%s). At HEAD `%s` (computed-new, this run, the content review\'s three values plus the history raw\'s second pod id): %d HANDOFFs, %d raws, %s, %d code file(s), %d other file(s) and %d commit messages; %s (%s). The spread at both commits is below the table. The record calls the pod stopped and parked, not terminated. | (a) accept publication, optionally terminating the pod and settling the volume so the ids are inert; (b) redact the HEAD copies (history keeps them) [index note: the content review\'s D1 names three values, so (b) removes the second pod id only if the PI\'s decision names it too]; (c) rewrite history (the PI\'s call). Separately: the `resume.py` test fixture regenerates the pod id into new self-test raws; replacing it is a code change this block forbids, a PI or design-seat decision. | **Leave history as is** (so (c) is not taken). As routed to this part, the routing says nothing on (a)\'s pod and volume, (b)\'s HEAD copies or the fixture. Under D4, `%s` was committed at `%s` and carries the network-volume id %d time(s) (section 12); it is counted under "other" at HEAD. %s, item 4, restates the decision: D1 stands (history as is) (section 2b). | The gitleaks raw: "the PI\'s D1 routing (2026-10-09) is to leave history as is" (%s); the routing commit: "the PI\'s D1 is to leave it", of that file (%s). The rulings\' restatement: section 2b. | %s; %s; %s; %s; %s |' % (
        c_scan[:10], C.loc(cc['head']), d1_hand, d1_raws, d1_msgs, C.loc(c_bul[0]), C.loc(d1_spread),
        head[:10], h_cat['HANDOFF'], h_cat['raw'], 'RESULTS.md' if h_cat['RESULTS.md'] else 'not RESULTS.md', h_cat['code'], h_cat['other'], len(h_msgs),
        pod2_txt, H.loc(d1_info[pod2[0]]['row']),
        v13, Rs, v13_occ, RULINGS[0].upper() + RULINGS[1:], G.loc(g['o3']), ro_loc,
        C.loc(cc['d1'], cc['d2'] - 1), C.loc(cc['s4']), C.loc(cc['d1rec'], cc['d1rec'] + 3), C.loc(cc['fixture']),
        H.loc(d1_info[d1_order[0]]['row'], d1_info[d1_order[-1]]['row'])))
    w('| D2 | The LoRA overfit phrase (redacted at %s): the synthetic target of a LoRA overfit test, not a credential. | The PI compares it with the continuity password out of band (N12(iii)); a match means the password is already in history, and the PI rotates or retires it. | **Closed, no match.** The (iii) search, independent of that comparison, finds the password in no commit reachable at its ref `%s` (section 4). | The password raw: "%s" (%s); the routing commit: "D2 (the LoRA phrase) is closed by the PI: no match." (%s). | %s; %s; %s |' % (
        C.loc(cc['d2']), pw_ref[:10], PW.line(pw['d2']).split('. ')[0] + '.', PW.loc(pw['d2']), ro_loc, C.loc(cc['d2'], cc['d3'] - 1), C.loc(cc['f44']), H.loc(pp_lora)))
    w('| D3 | Commit metadata: %d commits with `.local` e-mail domains (%d of them use the laptop\'s hostname as the domain, per the history raw; the other %d use a domain the history reviewer reads as a placeholder rather than a machine name); %d commits with a claude.ai session-link trailer; the same %d SSH-signed, embedding a public key. Low sensitivity. | Only a history rewrite changes the objects (`.mailmap` changes the display only), or accept. | **Leave.** | %s | %s; %s; %s; %s |' % (
        d3_local, d3_host, d3_local - d3_host, d3_sess, d3_sig,
        ('In the part raws and the routing commit\'s message: none. %s; `%s`, the README part\'s file (%s), is not read here, so whether it records D3 is not checked by this index.' % (
            '; '.join('`%s`\'s message lists among `%s`\'s contents "%s" (`git show -s %s` (commit message))' % (c[:7], README_NOTE, README_D_FRAG, c[:7]) for c in d3_msg),
            README_NOTE, ('tracked since `%s`' % rn_added) if rn_tracked else 'not tracked at HEAD'))
        if d3_msg else 'None found: no committed raw or commit message this index reads records D3\'s routing.',
        C.loc(cc['d3'], cc['d4'] - 1), C.loc(cc['f46']), H.loc(h['s_ii']), H.loc(h['identities'])))
    keep_txt = '; '.join('%s (`%s`): %d on disk' % (desc, pat, len(rows)) for desc, pat, rows in d4k)
    w('| D4 | Release staging: %s untracked, not-gitignored design-seat documents (%s with not-for-the-repo headers; none of them in any commit) and %d other untracked root/archive files sat in the checkout at the content review. At the history run\'s snapshot, %d of the PI\'s untracked documents carried a D1 identifier (%s). | Stage the release and tag commits by explicit path and check `git diff --cached --name-status`; or move or gitignore the design documents (a PI or design-seat call). No history action. | **As routed:** commit `archive/PROPOSAL-m-gating-campaign-v1_2` through `v1_10`; do not commit the design-seat handoffs, the design-to-Code decisions file, the superseded ADDENDUM-g3-b2r drafts, ADDENDUM-k1 or the archive/PREPRINT pre-patch copies; `README-NOTE.md` states in one line that the design-seat handoffs are held for a separate write-up on the workflow; commit `%s` at the tag after patch v6 is applied (patch v6 is not yet on the machine). [index note: the PI\'s routing of 2026-10-12 makes patch v7 the text of record, and %s, question (5), places it in the tag commit with note v0.6 and the three 2026-10-10 renders (section 10, items 4 and 6); the files on D4\'s do-not-commit list stay out of the tag commit by the PI\'s routing of 2026-10-09 (D4); the release run excludes the two D4 patterns Code\'s housekeeping names (`HANDOFF-*-design.md`, `DESIGN-to-CODE-*.md`) by name, never opened (Code\'s housekeeping, not objected).] | The routing commit (%s): the nine files "committed unmodified" and the do-not-commit list, with "PREPRINT-v1_0-draft.md waits for patch v6". The README line: none checked here. | %s; %s; %s; %s; %s |' % (
        d4_docs.lower(), d4_hdr.lower(), d4_other, len(pi_d1), ', '.join('`%s`' % f for f, _ in pi_d1), PREPRINT, ANSWER, ro_loc,
        C.loc(cc['d4']), C.loc(cc['nocommit']), C.loc(cc['d4rec'], cc['d4rec'] + 2), H.loc(h['pre_pi']),
        H.loc(*pi_rows_span) if pi_rows_span else 'none'))
    w('')
    w('**D4 staging state at HEAD `%s` (computed-new; names and git tracked status only, no untracked file opened).**' % head[:10])
    w('')
    w('- To commit: the %d files `archive/PROPOSAL-m-gating-campaign-v1_2.md` to `v1_10.md`: tracked at HEAD %d of %d, each added at `%s`: %s.' % (
        len(d4c), sum(1 for _, t, _ in d4c if t), len(d4c), Rs, yn(d4c_ok)))
    w('- Not to commit: %s. Tracked at HEAD: %d; in any commit on any ref: %d%s. The committed g3-b2r addendum the drafts precede, `%s`, is left out of the drafts\' glob by name (tracked at HEAD: %s); `ADDENDUM-g3-b2r*.md` files tracked at HEAD: %d (%s).' % (
        keep_txt, len(d4k_tracked), len(d4k_ever), (' (%s)' % ', '.join('`%s`' % n for n in sorted(set(d4k_tracked) | set(d4k_ever)))) if (d4k_tracked or d4k_ever) else '',
        G3_COMMITTED, yn(g3_committed_tracked), len(g3_tracked), ', '.join('`%s`' % p for p in g3_tracked) or 'none'))
    w('- `%s`: on disk %s; tracked at HEAD %s; in any commit %d; sha256 on disk equal to patch v7\'s, as Code put it to the PI: %s. It is committed at the tag, by %s, question (5) (section 10, item 6).' % (
        PREPRINT, yn(pre_exists), yn(pre_tracked), pre_ever, yn(tagf[4][1] == tagf[4][2]), ANSWER))
    w('- Of the %d PI documents the history raw\'s snapshot found carrying a D1 identifier: tracked at HEAD now %d (%s); the other %d are on the do-not-commit list.' % (
        len(pi_d1_now), sum(1 for _, t in pi_d1_now if t), ', '.join('`%s`' % f for f, t in pi_d1_now if t) or 'none', sum(1 for _, t in pi_d1_now if not t)))
    w('')
    # D1 carrier spread (computed-new)
    w('**D1 carrier spread (computed-new, this run).** The four D1 values the history JSON lists (`prerelease_pending_files.known_values`: both RunPod pod ids, the network-volume id and the volume display name), resolved in memory as for the leak guard and never printed. Tracked files: `git grep -l -F` at the commit, kept only where the value is bounded by non-alphanumerics (fixed-string candidates dropped by that check: %d at `%s`, %d at HEAD). Commit messages: every commit reachable from the commit (%d from `%s`, %d from HEAD), same rule. The volume name\'s stem (%d further value in the same JSON list, the name without its suffix) is not counted as a separate value: tracked files where it occurs outside the full name, %d at `%s` and %d at HEAD; commit messages, %d and %d. Counts and paths only; each value is named by its row in the history raw\'s table of identifiers present at HEAD (%s).' % (
        d1_at[c_scan]['dropped'], c_scan[:10], hd['dropped'], d1_at[c_scan]['n_commits'], c_scan[:10], hd['n_commits'],
        len(stem_forms), d1_at[c_scan]['stem_only'][0], c_scan[:10], hd['stem_only'][0], d1_at[c_scan]['stem_only'][1], hd['stem_only'][1],
        H.loc(h['ids_head'])))
    w('')
    w('| value (history raw row) | files at `%s`: HANDOFF / raw / RESULTS.md / code / other | messages at `%s` | files at HEAD `%s`: HANDOFF / raw / RESULTS.md / code / other | messages at HEAD |' % (
        c_scan[:10], c_scan[:10], head[:10]))
    w('|---|---|---|---|---|')

    def cell(paths):
        n = d1_cats(paths)
        return '%d (%d / %d / %d / %d / %d)' % (len(paths), n['HANDOFF'], n['raw'], n['RESULTS.md'], n['code'], n['other'])

    for f in d1_order:
        w('| %s (%s) | %s | %d | %s | %d |' % (
            d1_name[f], H.loc(d1_info[f]['row']), cell(d1_at[c_scan]['files'][f]), len(d1_at[c_scan]['msgs'][f]),
            cell(hd['files'][f]), len(hd['msgs'][f])))
    for lab, fs in (("the content review's three values", con3), ('any of the four', d1_forms)):
        w('| %s | %s | %d | %s | %d |' % (lab, cell(d1_union(c_scan, fs, 'files')), len(d1_union(c_scan, fs, 'msgs')),
                                         cell(d1_union(head, fs, 'files')), len(d1_union(head, fs, 'msgs'))))
    w('')
    b_all = d1_union(c_scan, d1_forms, 'files')
    added_c = sorted(h_all - b_all)
    gone_c = sorted(b_all - h_all)
    raws_head = sorted(p for p in h_all if d1_cat(p) == 'raw')
    w('- Tracked raws carrying a D1 value at HEAD (%d): %s.' % (len(raws_head), ', '.join('`%s`' % p for p in raws_head) or 'none'))
    w('- Code and other tracked files carrying a D1 value at HEAD (%d): %s.' % (len(other_head), ', '.join('`%s`' % p for p in other_head) or 'none'))
    w('- Carriers added between `%s` and HEAD (%d): %s; removed (%d)%s. Commit messages carrying a D1 value added since: %d. The content review says the `resume.py` fixture regenerates the pod id into every new self-test raw (%s).' % (
        c_scan[:10], len(added_c), ', '.join('`%s`' % p for p in added_c) or 'none', len(gone_c),
        (': ' + ', '.join('`%s`' % p for p in gone_c)) if gone_c else '',
        len(h_msgs - d1_union(c_scan, d1_forms, 'msgs')), C.loc(cc['fixture'])))
    w('- The PI\'s untracked documents are not tracked files and are not counted here; D4 above carries their staging state.')
    w('')
    w('Other PI items the part raws carry:')
    w('')
    w('- (i): the block\'s literal STOP (block :%d) is resolved by %s, item 4 (section 2b), on the record in section 2 (the fallback\'s %s hit lines, triaged, %s; gitleaks\' %d findings, all triaged FALSE-POSITIVE, %s). What the ruling does not name (trufflehog, the commits after `%s`, the release-commit re-run) is listed in section 2b; %s answers it: **ROUTED**, ruling 4 covers the release run\'s (i) at 0 true-secret candidates and 0 untriaged (question 3), and gitleaks\' default skip of `.svg` files and trufflehog not run are acceptable (question 4). **REMAINS:** the release run itself (section 10, items 3 and 5).' % (
        b['i'], RULINGS, '{:,}'.format(hits_n), H.loc(h['i_pass']), gl_o['Findings'], G.loc(g['o1']), gl_head[:7], ANSWER))
    w('- (iv): the licenses re-run at the release commit (**REMAINS**; %s, question (2), confirms its rule changes, **ROUTED**), and the licenses script\'s no-license text, %s; the Macar source, the word lists and the Global Workspace paper\'s license as the licenses raw states them (%s, %s).' % (
        ANSWER, ls_iv_txt, L.loc(lc['it1']), L.loc(lc['it7'])))
    w('- (ii): the stale statements that the repository is private (%s).' % C.loc(cc['stale']))
    w('- (iii): nothing open from the search at its ref `%s`: the password is in no commit reachable there, and the %d untracked files that hold it are on D4\'s do-not-commit list; the files committed after that ref are bounded in section 4 (time bound), and the release run repeats the search at the release commit (Code\'s own run, `%s`, committed after the tag).' % (pw_ref[:10], pw_with, RR['password'][0]))
    w('')

    # 10. pre-flip
    w('## 10. Pre-flip checklist (before the visibility change)')
    w('')
    w('Each item with its state: **DONE** (with the commit it was done at), **ROUTED** (the PI\'s routing, rulings or answer settles it, quoted as the PI\'s), or **REMAINS** (still to run or to do). The pre-flip raw marked items 1-5 at `%s` (%s); its statuses are carried verbatim and nothing here upgrades them.' % (pf_head[:7], PF.loc(pf['s5'])))
    w('')
    w('1. **`git ls-remote origin`** -- pre-flip raw: "%s" (%s; its pass line %s). **REMAINS:** the final `git ls-remote origin` just before the flip; the release commit and the tag push add or move server refs. It is the pre-flip read, which is not part of Code\'s release sequence (below): `%s` runs just before the PI\'s visibility flip, at the PI\'s word, after it is updated for the release names in its own commit, made then; its raws are new dated files that commit names. As committed at `%s` (%s), the script writes only its own two 2026-10-08 basenames (%s) and compares against the 2026-10-08 history JSON (%s). History raw: %s; licenses raw: %s.' % (
        pfj['remaining'][0]['status'], PF.loc(pf_rem[1]), PF.loc(pf['p1']), PREFLIP_SCRIPT, PFs,
        'the version at HEAD' if pfs_same else 'HEAD holds a later version', PFS.loc(pfs_own), PFS.loc(pfs_hist), H.loc(h['pf2']), L.loc(lc['it6'])))
    PF.need(pf_rem[2], PF2_REPEAT)
    w('2. **GitHub-side surfaces** -- pre-flip raw: "%s" (%s; pass and flag lines %s). Projects (v2): NOT READ by Code (%s); **ROUTED:** the PI\'s routing of %s states the GitHub repository has no associated Projects (the PI\'s look; no committed record of it is read here). **REMAINS:** the repeat just before the flip, in the same pre-flip read as item 1, outside the release sequence; the pre-flip raw asks for it as "%s" (%s), and in Code\'s release plan that read runs after the release sequence (R3 included), once the pre-flip script\'s own commit is made. History raw: %s.' % (
        pfj['remaining'][1]['status'], PF.loc(pf_rem[2]), PF.loc(pf_p2_first, pf_p2_last), PF.loc(pf['p2i']), ROUTING, PF2_REPEAT, PF.loc(pf_rem[2]), H.loc(h['pf3'])))
    w('3. **Re-run `scripts/audit_note_N12_history.py`, `scripts/audit_note_N12_content.py` and `scripts/audit_note_N12_licenses.py` at the release commit** -- pre-flip raw at `%s`: "%s" (%s). Since then the history script\'s refusal (%s) is fixed by round 5 at `%s`, whose run at `%s` is interim (%s); no re-run of the content or licenses script is committed after `%s` (the pre-flip raw: "The content and licenses scripts were not re-run.", %s). **ROUTED, the terms of the re-runs (%s, "%s"):** question (1) accepts the content script\'s leak-guard fix, question (2) confirms the licenses script\'s rule changes, and question (3) says ruling 4 covers the release run\'s (i) at 0 true-secret candidates and 0 untriaged; the PI\'s declaration on the 2026-10-10 renders\' `<c2pa:manifest>` elements, a known high-entropy false positive for this re-scan, as routed to Code in round 9, stands beside it; the history script\'s triage entries are Code\'s housekeeping, not objected (header). **REMAINS: all three release-commit re-runs**, to new dated raws committed after the tag (Code\'s housekeeping, not objected): history `%s` and `%s`; content `%s`; licenses `%s` and `%s`; with them Code\'s own repeat of the password search, `%s` (section 4). On disk at this run: %d of %d. For the history script, the history raw\'s step opens, verbatim: "%s" (%s). Run it immediately before the release commit, with every raw, script and README of the end commit in place (this file and `README-NOTE.md` included), and again at the release commit [index note, Code\'s reading, labelled as such, for the PI to rule on; not settled here: the release sequence below has one history re-run, step (5), at R2 with the tag present, before any push, the tag kept local until every release scan passes; Code reads that run as taking the place of both, since nothing is pushed before it passes]; its pre-release section must show no redaction-rule value in any file the end commit adds and no new value needing triage. The same step lists the commit identities\' own metadata (the identity emails and the laptop hostname) as not holding the tag as drafted, with "binding either part is the PI\'s call", and ends "The tag should wait on a clean run." For the content script, a new `--json-out` against the release commit, then every new raw read once end to end (%s). The licenses part asks the same of `scripts/audit_note_N12_licenses.py` at the final pre-flip commit, with its counts re-checked, and says this file states that bound (%s, %s); its projection that its two sweep gates fail there is carried, with its open values-check finding, and %s.' % (
        pf_head[:7], pfj['remaining'][2]['status'], PF.loc(pf_rem[3]), PF.loc(pf['p3a']), Hs, h_scan[:7], H.loc(h['interim']), A, PF.loc(pf_rem[3]),
        ANSWER, ANSWER_TEXT, RR['history'][0], RR['history'][1], RR['content'][0], RR['licenses'][0], RR['licenses'][1], RR['password'][0],
        len([p_ for p_ in rel_on_disk if p_ not in RR['gitleaks']]), len(RR['history'] + RR['content'] + RR['licenses'] + RR['password']),
        pf1_first, H.loc(h['pf1']), C.loc(cc['rerun']), L.loc(lc['scope_time']), L.loc(lc['it8']), ls_it3_txt))
    w('')
    w('   **Re-run outputs, per script.** This index, like any other file that cites the part raws by line, points into the committed raws, so a re-run must not silently replace them. The three part scripts behave differently. *Licenses:* `--out` and `--json-out` default to `%s` and `%s` (%s, %s), so a default run overwrites the committed raws; pass new paths, or use `--out-dir`, which puts each output not given by `--out` or `--json-out` into that directory under its default basename (%s). *Content:* `--json-out` defaults to `%s` (%s), and the script refuses to overwrite an existing file (%s); give a new `--json-out` under `results/raw/`. *History:* as committed at `%s`, `--out` and `--json-out` default to `%s` and `%s` (%s, %s); inside the repository it accepts only `results/raw/` paths (%s) whose basename is one of its own two (%s), so it can write either to the defaults (overwriting the committed raws; regenerate this index afterwards) or to the same basenames in a subdirectory of `results/raw/`, or anywhere outside the repository. The licenses script\'s pass line names the history raw at its fixed default path, whatever path the history re-run writes (%s). This script\'s own `--out` defaults to this file, so the same applies to it. The release run\'s history raws have new dated basenames (`%s`, `%s`), which are not the history script\'s own two, so the script as committed at `%s` refuses them as outputs inside the repository (%s). %s' % (
        LIC_MD, LIC_JSON, LS.loc(out_defaults['licenses'][0]), LS.loc(out_defaults['licenses'][1]), LS.loc(ls_outdir),
        CON_JSON, CS.loc(out_defaults['content'][0]), CS.loc(cs_nooverwrite),
        Hs, HIST_MD, HIST_JSON, HS.loc(out_defaults['history'][0]), HS.loc(out_defaults['history'][1]),
        HS.loc(hs_rawonly), HS.loc(hs_ownonly), LS.loc(ls_histraw), os.path.basename(RR['history'][0]), os.path.basename(RR['history'][1]), Hs, HS.loc(hs_ownonly), hist_route_txt))
    w('4. **Review untracked files before any commit adds them** -- pre-flip raw at `%s`: "%s" (%s). **ROUTED (D4), as to which files:** which untracked files are committed and which are not is settled by the routing (section 9, with the staging state at HEAD); stage by explicit path (D4, %s). The routing does not waive the review: the content review left the untracked root and archive files unreviewed and asks, verbatim, "review them before any commit that would add them" (%s). For the %d `archive/PROPOSAL-m-gating-campaign-v1_*.md` files committed at `%s`, the routing commit records a pre-commit screen, verbatim: "%s" (%s); this index carries that record and does not review the files itself. At the history run\'s snapshot, %d of the PI\'s %d untracked or modified documents carried a D1 identifier (%s; rows %s); of them, `%s` is now committed per D4 and the rest are on the do-not-commit list. **ROUTED, as to which files the tag commit adds (%s, question (5)):** note v0.6 and the three 2026-10-10 renders beside `%s` (patch v7); the files on D4\'s do-not-commit list stay out of the tag commit, by the PI\'s routing of %s (D4, section 9); the release run excludes the two D4 patterns Code\'s housekeeping names (`HANDOFF-*-design.md`, `DESIGN-to-CODE-*.md`) by name, never opened (Code\'s housekeeping, not objected). **REMAINS:** Code\'s review of each file the tag commit adds (those five, and every audit file it adds), before the release commit is made (with the files staged); untracked, not-ignored files on disk at this run outside the do-not-commit list and other than `%s` (computed-new; names only, none opened): %d%s.%s The history re-run of item 3 must also run with every such file of the end commit in place.' % (
        pf_head[:7], pfj['remaining'][3]['status'], PF.loc(pf_rem[4]), C.loc(cc['d4rec']), C.loc(cc['untracked']),
        len(ro_pm), Rs, RO_SCREEN, ro_loc, len(pi_d1), pi_n_scanned, H.loc(h['pre_pi']),
        H.loc(*pi_rows_span) if pi_rows_span else 'none', v13, ANSWER, PREPRINT, ROUTING, PREPRINT, len(untr_other),
        (' (%s)' % ', '.join('`%s`' % p_ for p_ in untr_other)) if untr_other else '', sup_txt))
    w('5. **The block\'s primary scanners** -- pre-flip raw at `%s`: "%s" (%s). **DONE at `%s`, interim (gitleaks):** installed and run by the PI, run again and triaged by Code over every ref at its run (`--log-opts=--all`, %s; HEAD `%s`; %d commits scanned, %s), %d findings, all FALSE-POSITIVE, 0 untriaged (section 2a). trufflehog, which the history raw\'s step also names: not run (not installed, %s). The history raw\'s step runs the scanners "over the repository at the release commit" (%s); the %d commits after `%s` are covered by gitleaks only as far as the per-file passes that %d of their messages record over the commit\'s own files (section 2a). %s, item 4, resolves (i) on the gitleaks run at `%s` and Code\'s scans (section 2b) and names neither the later commits nor trufflehog. **ROUTED (%s, question (4)):** gitleaks\' default skip of `.svg` files and trufflehog not run are acceptable; Code\'s triage of the hit at `%s` FALSE-POSITIVE is Code\'s housekeeping, not objected (section 2a). **REMAINS:** gitleaks over all history at the release commit, Code\'s run, its raw `%s` committed after the tag; it covers the commits after `%s`.' % (
        pf_head[:7], pfj['remaining'][4]['status'], PF.loc(pf_rem[5]), gl_head[:7], G.loc(g['cmd']), gl_head[:10], gl_commits, G.loc(g['commits']), gl_o['Findings'], G.loc(g['o3']), H.loc(h['pf4']),
        len(gl_after), gl_head[:7], len(gl_after_pass), RULINGS[0].upper() + RULINGS[1:], gl_head[:7], ANSWER, GL_FP[0][:10], RR['gitleaks'][0], gl_head[:7]))
    w('6. **The preprint** -- **ROUTED:** the PI\'s routing of 2026-10-12 makes patch v7 the text of record, carrying forward the patch v6 this item named, and %s, question (5), places `%s` in the tag commit at patch v7\'s sha256 `%s` (on disk equal: %s; section 12). The routing commit\'s "waits for patch v6" (%s) is history. **REMAINS:** its commit, in the tag commit (item 7). At this run: on disk %s, tracked %s.' % (
        ANSWER, PREPRINT, TAG_FILES[4][1], yn(tagf[4][1] == tagf[4][2]), ro_loc, yn(pre_exists), yn(pre_tracked)))
    w('7. **The tag** -- **ROUTED:** %s, "%s". As routed on 2026-10-09, the tag is `%s`, placed on the final audit commit after N1 and N18 (the block leaves the tag name to the PI, `%s@%s:%d`). **REMAINS:** the tag, at the release commit; its commit hash is to be recorded after tagging, in the note\'s footer (%s; the footer is the design seat\'s, outside Code\'s release sequence) and in `%s`, which Code writes after the push and commits at R3 (the tag commit cannot hold its own hash); the scan raws (items 3-5) are written at R2 with the tag present, before any push, and committed after it, at R3; the pre-flip read (items 1 and 2) runs just before the flip, outside the release sequence. At this run the tag exists: %s.' % (
        ANSWER, ANSWER_TEXT, TAG, BLOCK, P, b['s7_body'], blk.loc(b['footer']), TAG_RAW, yn(tag_exists)))
    w('')
    w('**Done:** items 1 and 2 at `%s`, interim; Projects (none, per the PI); item 5\'s gitleaks at `%s`, interim (the PI and Code); for item 4, the pre-commit screen of the %d PROPOSAL-m files, as the routing commit records it; and (i)\'s STOP, resolved by %s, item 4 (section 2b). **Routed by %s ("%s"):** the terms of the item-3 re-runs (questions 1-3); which files the tag commit adds (item 4, question 5); gitleaks\' `.svg` skip and trufflehog not run (item 5, question 4); the preprint at patch v7, committed at the tag (item 6); the tag (item 7). **Remains:** before the release commit is made (with the files staged), Code\'s review of each file the tag commit adds (item 4); at the release commit, the re-runs of the history, content and licenses scripts and Code\'s repeat of the password search (item 3), gitleaks over all history (item 5), the preprint\'s commit and the tag (items 6 and 7); after the tag and the push, `%s` (to record the tag\'s hash) and the scan raws, committed at R3; just before the flip, outside the release sequence, the pre-flip read: the final `git ls-remote origin` and the surface repeat (items 1 and 2).' % (
        pf_head[:7], gl_head[:7], len(ro_pm), RULINGS, ANSWER, ANSWER_TEXT, TAG_RAW))
    w('')
    rel_scan_raws = [p_ for k_ in ('history', 'content', 'licenses', 'gitleaks', 'password') for p_ in RR[k_]]
    w('**The release sequence (Code\'s release plan, stated as a plan: this index reports none of its steps as run; each step\'s own commit or raw is its record).** '
      'Code screens each commit message and the tag message before that commit or tag is made. '
      '(1) **R1**, a commit of the four final N12 part scripts (%s) and this script (`%s`). '
      '(2) At R1: this index regenerated (`%s`), `README-NOTE.md` made final, N18 re-run (`%s --preprint-pi-confirmed %s`, patch v7\'s sha256), and Code\'s review of the files R2 adds, with them staged, before R2 is made (item 4). '
      '(3) **R2, the tag commit** (the release commit of items 3-7): the five files of section 12 (%s), `README-NOTE.md`, this index and N18\'s manifest (%s). '
      '(4) **The tag**: `%s`, annotated, on R2, kept local until step (6). '
      '(5) **The release scans**, at R2 with the tag present and before any push: the history, content and licenses scripts (item 3) and the gitleaks script (item 5), and Code\'s own password search (section 4), each to its new dated raw (%s); all must pass before anything is pushed. '
      '(6) R1, R2 and the tag pushed. '
      '(7) `%s --ref %s --out %s`; and `%s`, written by Code, to record the tag\'s commit hash. '
      '(8) **R3**, the post-tag commit: the raws of steps (5) and (7), each first put through Code\'s per-file redaction check, password scan and gitleaks scan; then R3 pushed. '
      '**The pre-flip read is not part of this sequence:** `%s` (items 1 and 2) runs just before the PI\'s visibility flip, at the PI\'s word, after the script is updated for the release names in its own commit, made then (item 1); its raws are new dated files that commit names.' % (
        ', '.join('`%s`' % p_ for p_ in R1_SCRIPTS), me, DEFAULT_OUT, N18_SCRIPT, TAG_FILES[4][1],
        ', '.join('`%s`' % t_[0] for t_ in TAG_FILES), ', '.join('`%s`' % p_ for p_ in MANIFEST), TAG,
        ', '.join('`%s`' % p_ for p_ in rel_scan_raws), N11_SCRIPT, TAG, N11_TAG_RAW, TAG_RAW,
        PREFLIP_SCRIPT))
    w('')

    # 11. coverage / delta
    w('## 11. Coverage after the part raws\' commits (computed-new)')
    w('')
    w('The history raw\'s scan is a snapshot at `%s`. Files changed between it and HEAD `%s` (%d commit(s): %s), read at HEAD, checked for the resolved sensitive values (exact counts; SSH-port-class values word-bounded, so an unrelated equal number would count). Counts and paths only. Not a substitute for pre-flip step 3: it does not apply the history script\'s patterns, its triage or its new-value classes.' % (
        h_scan[:10], head[:10], len(since_hist), ', '.join('`%s`' % c[:10] for c in since_hist) or 'none'))
    w('')
    n_text = len(delta)
    w('- Text files changed (added, modified, renamed): %d.' % n_text)
    w('- With a redaction-rule value (any class other than the identity emails; the laptop hostname counts here, because this audit\'s routing names it among the values its public outputs must not carry, while the history raw\'s pre-release lines group it with the commit identities\' own metadata, %s): %d%s.' % (
        H.loc(h['pre_ident']), len(delta_rule), (' -- ' + '; '.join('`%s` (%s)' % (p, ', '.join('%s: %d' % kv for kv in sorted(hs.items()))) for p, s, hs in delta_rule)) if delta_rule else ''))
    w('- With only an identity email (public in the commit headers; the history raw lists such files and, as drafted, does not hold the tag on them, %s): %d%s.' % (
        H.loc(h['pre_ident']), len(delta_ident), (' -- ' + '; '.join('`%s` (%s)' % (p, ', '.join('%s: %d' % kv for kv in sorted(hs.items()))) for p, s, hs in delta_ident)) if delta_ident else ''))
    if any(p == v13 for p, _, _ in delta_rule):
        w('- `%s` is the D4 commit the routing commit names, carrying the network-volume id the PI\'s D1 leaves (section 9).' % v13)
    w('')

    # ---------- the PI's rulings of 2026-10-09, item 4: the recording, asserted on the composed text ----------
    r4_head = [ln for ln in o if ln.startswith('- %s (the second routing), item 4, recorded here' % (RULINGS[0].upper() + RULINGS[1:]))]
    r4_2b = [i for i, ln in enumerate(o) if ln == '### 2b. (i) resolved: %s, item 4' % RULINGS]
    r4_row = [ln for ln in o if ln.startswith('| (i) secrets, full history |') and ('the STOP is resolved by %s, item 4' % RULINGS) in ln]
    if len(r4_head) != 1 or len(r4_2b) != 1 or len(r4_row) != 1 or \
            ('- As routed to this part (quoted in substance): %s.' % R4_SUBSTANCE) not in o[r4_2b[0]:]:
        raise SystemExit("the PI's rulings of 2026-10-09, item 4: not recorded in the header, section 2b and section 0's table")
    mm = R4_RX.search(r4_head[0])
    if not mm:
        raise SystemExit("the PI's rulings of 2026-10-09, item 4: the recorded figures are not readable from the header line")
    # no line of the index's own text may still say that (i) is pending; verbatim quotes of the raws are exempt
    r4_quoted = [short['i'], '"STOP pending the PI\'s resolution"', '"Resolving (i) remains the PI\'s act"']
    for k_, ln in enumerate(o, 1):
        if ln.startswith('> ') or ln == REDACTION_SLOT:
            continue
        s_ = ln
        for qt in r4_quoted:
            s_ = s_.replace(qt, '')
        for fb in R4_FORBIDDEN:
            if fb in s_:
                raise SystemExit('composed line %d still says (i) is pending (%r) outside a verbatim quote' % (k_, fb))
    # the ruling keeps two figures apart: gitleaks' findings, "all false positives" (so TRUE-SECRET 0 in the gitleaks
    # triage), and "Code's own scans found 0 true-secret candidates" (the history raw's TRUE-SECRET-CANDIDATE alone)
    xadd("(i) %s, item 4, as recorded here: scanner; gitleaks findings / FALSE-POSITIVE / TRUE-SECRET (the ruling's \"all false positives\"); Code's own scans' true-secret candidates (the history raw's TRUE-SECRET-CANDIDATE)" % RULINGS,
         '%s; %d / %d / %d; %d' % (mm.group(1), int(mm.group(2)), int(mm.group(2)), 0, int(mm.group(3))),
         '%s; %d / %d / %d; %d' % (gl_scanner, gl_o['Findings'], gl_o['FALSE-POSITIVE'], gl_o['TRUE-SECRET'], tsc),
         "this index's header line and section 2b (the routing; no committed record before this commit)" if not (r4_recs or r4_msgs_n12)
         else "this index's header line and section 2b (committed records: section 2b)",
         '(%s; %s; %s)' % (G.loc(g['cmd']).strip('`'), G.loc(g['o1']).strip('`'), H.loc(h['s_i']).strip('`')))

    # ---------- the PI's answer of 2026-10-12: the recording, asserted on the composed text ----------
    a_head = [ln for ln in o if ln.startswith('- %s, verbatim: "%s".' % (ANSWER[0].upper() + ANSWER[1:], ANSWER_TEXT))]
    if len(a_head) != 1 or not all(qs in a_head[0] for qs in ANSWER_QS) or not all(hk in a_head[0] for hk in HOUSEKEEPING):
        raise SystemExit("the PI's answer of 2026-10-12: not recorded once in the header with its five questions and Code's housekeeping")
    s10 = [i for i, ln in enumerate(o) if ln == '## 10. Pre-flip checklist (before the visibility change)']
    s11 = [i for i, ln in enumerate(o) if ln.startswith('## 11. ')]
    if len(s10) != 1 or len(s11) != 1:
        raise SystemExit('section 10 not found once')
    items = {}
    for ln in o[s10[0]:s11[0]]:
        mi = re.match(r'^([1-7])\. \*\*', ln)
        if mi:
            items[int(mi.group(1))] = ln
    if sorted(items) != list(range(1, 8)):
        raise SystemExit('section 10: items 1-7 not found')
    for k_ in (1, 2):
        if '**REMAINS:**' not in items[k_] or ANSWER in items[k_] or (ANSWER[0].upper() + ANSWER[1:]) in items[k_]:
            raise SystemExit('section 10, item %d: must REMAIN for the flip, with no answer recorded against it' % k_)
    for k_ in (3, 4, 5, 6, 7):
        it = items[k_]
        if '**ROUTED' not in it or 'REMAINS' not in it or (ANSWER not in it and (ANSWER[0].upper() + ANSWER[1:]) not in it):
            raise SystemExit("section 10, item %d: the PI's answer is not recorded as ROUTED with what REMAINS" % k_)
    # no line of the index's own text may still call open what the answer settles; verbatim quotes are exempt
    for k_, ln in enumerate(o, 1):
        if ln.startswith('> ') or ln == REDACTION_SLOT:
            continue
        for fb in ANS_FORBIDDEN:
            if fb in ln:
                raise SystemExit('composed line %d still calls open what the answer settles (%r)' % (k_, fb))
    for p, routed, disk, full, trk, eq in tagf:
        if ('`%s`' % routed) not in a_head[0] and ('`%s...`' % routed.rstrip('.')) not in a_head[0]:
            raise SystemExit('the tag commit file %s: its routed sha256 form is not in the recorded answer' % p)
        xadd("%s, question (5): `%s` sha256, as Code put it to the PI vs the file on disk (%s at HEAD%s)" % (
            ANSWER, p, 'tracked' if trk else 'untracked', (', equal to its blob: %s' % yn(eq)) if trk else ''),
            routed, disk, "this index's header line (the answer)", '(sha256 of %s on disk)' % p)
    named = sorted(set(re.findall(r'`(results/raw/2026-10-12_note-N12-[a-z-]+-release\.(?:md|json))`', '\n'.join(o[s10[0]:s11[0]]))))
    xadd("%s: release-run scan raws named in section 10 vs Code's release plan" % ANSWER, len(named), len(rel_all), 'section 10, items 3-5 and the release sequence', "(Code's release plan: the seven scan raws)")
    if sorted(named) != sorted(rel_all):
        raise SystemExit('section 10 does not name exactly the release-run raws')
    xadd("Code's housekeeping: the gitleaks hit `%s` `%s:%d` carries the sha256 of `%s` at that commit" % (GL_FP[0][:10], GL_FP[1], GL_FP[2], GL_FP[3]),
         'yes', yn(fp_ok).lower(), 'section 2a', '(git show %s:%s, line %d; sha256 of %s at %s)' % (GL_FP[0][:10], GL_FP[1], GL_FP[2], GL_FP[3], GL_FP[0][:10]))

    # 12. cross-checks
    w('## 12. Index cross-checks (computed-new: each part\'s md against its own JSON, a committed file, or a recount at the commit the part read; the last rows: %s, item 4, as this index records it, against the committed raws; then %s, as recorded here, against the files on disk and the committed record)' % (RULINGS, ANSWER))
    w('')
    w('| figure | md | JSON / committed / recount | md locator | JSON field or source | status |')
    w('|---|---|---|---|---|---|')
    for what, mv, jv, ml, jp, st in xc:
        w('| %s | %s | %s | %s | `%s` | %s |' % (what, ('`%s`' % mv) if isinstance(mv, str) and len(mv) == 64 else mv,
                                             ('`%s`' % jv) if isinstance(jv, str) and len(jv) == 64 else jv, ml, jp.strip('`'), st))
    n_disc = sum(1 for x in xc if x[5] == 'discrepant')
    w('')
    w('Agree: %d of %d; discrepant: %d.' % (len(xc) - n_disc, len(xc), n_disc))
    w('')

    # 13. open values-check items
    w('## 13. Values-check items (carried; not applied)')
    w('')
    w('From the values-check process record at `%s`:' % A)
    w('')
    for k, name, loc_ in (('h', 'N12-history', vc['h']), ('l', 'N12-licenses', vc['l']), ('c', 'N12(vi) content', vc['c'])):
        ids = vc_open[k]
        if vc_passes[k]:
            ran = [i for i in vc_passes[k] if VC.line(i).startswith('### Pass ') and 'not run' not in VC.line(i)]
            fin = [i for i in vc_passes[k] if VC.line(i).startswith('### Final check')]
            w('- %s (%s): %d values-check pass(es) run%s; %d open%s.' % (
                name, VC.loc(loc_), len(ran), (' and a final check (%s)' % VC.loc(fin[-1])) if fin else ', no final check',
                len(ids), (' -- ' + ', '.join(VC.loc(i) for i in ids)) if ids else ''))
        else:
            body_ln = [i + 1 for i in range(loc_, vc_end[k]) if VC.lines[i].strip()]
            VC.need(body_ln[0], 'Refuter round 1', 'Round 2')
            w('- %s (%s): no values-check pass is recorded for it; the section lists the reviewers and the refuter rounds only (%s); %d open item(s).' % (
                name, VC.loc(loc_, vc_end[k]), VC.loc(body_ln[0]), len(ids)))
    w('')
    all_open = [i for k in ('h', 'l', 'c') for i in vc_open[k]]
    n_minor = sum(1 for i in all_open if VC.line(i).startswith('- **open (minor'))
    sev = VC.sw('- Severity:')
    w('Labelled minor: %d of %d. The record defines minor as wording, locators or precision, as against substantive, a finding that would change a number, a status, a STOP/pass outcome or a sentence of the note (%s). The finding texts are at the locators; %s bears on the caveat carried in section 5.' % (
        n_minor, len(all_open), VC.loc(sev), VC.loc(vc_proj)))
    w('')
    pf_vc = [i + 1 for i in range(pf['s7'], len(PF.lines)) if re.match(r'^\d+\. \*\*F\d+ \((minor|substantive)\)', PF.lines[i])]
    pf_vc_minor = sum(1 for i in pf_vc if '(minor)' in PF.line(i))
    pf_vc_applied = sum(1 for i in pf_vc if '** APPLIED' in PF.line(i))
    w('Later part raws, each recording its own values-check:')
    w('')
    w('- N12-history, round 5 (the guard fix; `%s`): %s; its second check lists %d finding(s), %d marked APPLIED (%s); "%s" (%s).' % (
        Hs, H.loc(h['vc5']), len(vc5_findings), len(vc5_applied), H.loc(vc5_findings[0], vc5_findings[-1]) if vc5_findings else 'none',
        H.line(h['vc5_ctrl']).rstrip('.').split(' (')[0], H.loc(h['vc5_ctrl'])))
    w('- N12 pre-flip (`%s`): %s; %d finding(s), %d labelled minor, %d marked APPLIED (%s).' % (
        PFs, PF.loc(pf['s7']), len(pf_vc), pf_vc_minor, pf_vc_applied, PF.loc(pf_vc[0], pf_vc[-1]) if pf_vc else 'none'))
    w('- gitleaks and the password search (`%s`): no values-check section in either raw (headings `## Values-check`: %d and %d).' % (
        Rs, sum(1 for ln in G.lines if ln.startswith('## Values-check')), sum(1 for ln in PW.lines if ln.startswith('## Values-check'))))
    w('')

    # ---------- the leak guard ----------
    known_by_key = {}
    for f in forms:
        known_by_key[form_key(f)] = f
    caveat = H.line(h['caveat'])
    guard_vals = [(labels[f], v, bool(FORM_DIGITS.match(f))) for f, v in vals.items()] + \
                 [(k, v, False) for k, v in guard_extra.items()]

    def guard(text, printed=None):
        bad = []
        for lab, v, dg in guard_vals:
            if guard_count(v, text, dg):
                bad.append('resolved value of class %s' % lab)
        masked = mask_locators(text)
        for name, rx in GUARD_SHAPES:
            lines_hit = sorted({masked.count('\n', 0, mm.start()) + 1 for mm in rx.finditer(masked)})
            if lines_hit:
                bad.append('%s (output lines %s)' % (name, ', '.join(map(str, lines_hit))))
        for fm in sorted(printed or {}):
            kf = known_by_key.get(form_key(fm))
            if kf is None:
                bad.append('redacted form %s is not one the history JSON knows' % fm)
            elif exposure_of(caveat, labels[kf]) == 'Recoverable by brute force':
                bad.append('redacted form of class %s, which the history raw lists as recoverable by brute force' % labels[kf].split(' (')[0])
        return bad

    body = '\n'.join(o)
    printed = {}
    for mm in FORM_IN_TEXT.finditer(body):
        printed.setdefault(mm.group(0), 0)
        printed[mm.group(0)] += 1
    # positive controls: each resolved value, and a case variant of each of 8+ characters, injected into a copy
    # of the (clean) body; a control counts only if the body itself passes the guard
    ctrl_n, ctrl_ref = 0, 0
    base_bad = guard(body.replace(REDACTION_SLOT, ''), printed)
    if base_bad:
        raise SystemExit('LEAK GUARD: refusing to write; found: ' + '; '.join(base_bad))
    clean = body.replace(REDACTION_SLOT, '')
    for lab, v, dg in guard_vals:
        variants = [v]
        if not dg and len(v) >= 8:
            k1, k2 = len(v) // 3, 2 * len(v) // 3
            # case variants where they differ from the value, and one with two separators inserted ('-' and '.')
            for x in (v.upper(), v.lower(), v[:k1] + '-' + v[k1:k2] + '.' + v[k2:]):
                if x not in variants:
                    variants.append(x)
        for inj in variants:
            ctrl_n += 1
            if guard(clean + '\nctrl ' + inj + ' ctrl\n'):
                ctrl_ref += 1
    # shape controls, built at run time (no such literal in this source): one per guard shape, plus two
    # strings of the locator shape that are not real locators, on an ssh/port line, which the mask must not hide
    fake_hex = 'a' * 12
    shape_ctrls = [
        ('IPv4 literal', 'host ' + '.'.join(['192', '0', '2', '7'])),
        ('claude.ai session/artifact path', 'https://claude' + '.ai/' + 'code/' + 'x' * 8),
        ('SSH SHA256 fingerprint shape', 'SHA256' + ':' + 'A' * 43),
        ('local temp or transcript-store path', '/private' + '/tmp/' + 'x'),
        ('4-5 digit number on an ssh/port line', 'ssh port ' + '4' + '0' * 4),
        ('locator shape, not backticked', 'ssh root@' + fake_hex + ':' + '4' + '0' * 4),
        ('locator shape, backticked, path absent at that commit', 'ssh port `%s@%s:%s`' % ('nofile.md', fake_hex, '4' + '0' * 4)),
        ('locator shape, backticked, real path, line out of range', 'ssh port `%s@%s:%s`' % (LIC_FILES[0], Rs, '4' + '0' * 4)),
    ]
    shape_n, shape_ref = 0, 0
    for name_, inj in shape_ctrls:
        shape_n += 1
        if guard(clean + '\n' + inj + '\n'):
            shape_ref += 1
        else:
            print('shape control not refused: %s' % name_, file=sys.stderr)
    descs = []
    for fm in sorted(printed):
        kf = known_by_key.get(form_key(fm))
        if kf is None:
            continue
        lab = labels[kf]
        expo = exposure_of(caveat, lab)
        in_q = sorted({loc for ln, loc in quotes if fm in ln})
        n_q = sum(ln.count(fm) for ln, _ in quotes)
        own = printed[fm] - n_q
        where = []
        if own:
            where.append('%d time(s) in this index\'s own text' % own)
        if n_q:
            where.append('%d time(s) inside the verbatim quote of %s' % (n_q, ', '.join(in_q)))
        descs.append('`%s` (the history JSON\'s class `%s`; the history raw lists the class as "%s", %s): %s' % (
            fm, lab.split(' (')[0], expo.lower(), H.loc(h['caveat']), '; '.join(where)))
    red = ('- Redaction. No identifier value appears in this file: RunPod ids and names, SSH ports, the container and laptop hostnames, the session link, the LoRA phrase, the continuity password and the commit identities\' emails are named by class, with locators into the part raws that hold their redacted forms; no form of the continuity password (value, length or hash) is written. '
           'Redacted forms printed here, computed over this file\'s text apart from this paragraph: %d -- %s. '
           'Leak guard: the script resolves in memory, from `git log -p --all` and the commit/tag headers, each of the %d values the history raw treats as sensitive (its JSON `prerelease_pending_files.known_values`), by matching their redacted forms\' sha256 prefixes; resolved %d, unresolved %d (%s); plus %d derived value(s) (%s). It refuses to write this file if any resolved value occurs in it (exact; for values of 8 or more characters also ignoring case and every character other than a letter or digit; the SSH ports digit-bounded, except inside a hex run of 8 or more), if it prints a redacted form the history JSON does not know or one of a class the history raw lists as recoverable by brute force, or if it contains an IPv4 literal, a claude.ai session or artifact path, an SSH SHA256 fingerprint shape, a local temp or transcript-store path, or a bare 4-5 digit number other than a year on an ssh/port line. Only a real locator\'s line number is exempt from that last check: a backticked `path@commit:line` (or range) whose path exists at that commit and whose line lies within that file; any other `x@hex:digits` is checked. Positive controls, this run: %d value injections (each resolved or derived value; for each of 8 or more characters, its upper- and lower-case variants where they differ from it and a variant with a hyphen and a dot inserted) into a copy of this file, refused %d of %d; %d shape injections (one per shape above, and three strings of the locator shape that are not real locators: unbackticked, a path absent at its commit, a line beyond its file), refused %d of %d.') % (
        len(printed), '; '.join(descs) or 'none', len(forms), len(vals), len(unresolved),
        '; '.join('%s: not verbatim in history, which the history raw states at %s' % (labels[f], H.loc(h['caveat'])) for f in unresolved) or 'none',
        len(guard_extra), ', '.join(guard_extra) or 'none', ctrl_n, ctrl_ref, ctrl_n, shape_n, shape_ref, shape_n)
    text = body.replace(REDACTION_SLOT, red)
    assert REDACTION_SLOT not in text and '\0' not in text
    if ctrl_ref != ctrl_n:
        raise SystemExit('LEAK GUARD: positive controls refused %d of %d' % (ctrl_ref, ctrl_n))
    if shape_ref != shape_n:
        raise SystemExit('LEAK GUARD: shape controls refused %d of %d' % (shape_ref, shape_n))
    printed_all = {}
    for mm in FORM_IN_TEXT.finditer(text):
        printed_all[mm.group(0)] = printed_all.get(mm.group(0), 0) + 1
    bad = guard(text, printed_all)
    if bad:
        raise SystemExit('LEAK GUARD: refusing to write; found: ' + '; '.join(bad))

    out = os.path.join(REPO, a.out)
    if os.path.islink(out):
        raise SystemExit('refusing to write through a symlink')
    with open(out, 'w') as fh:
        fh.write(text)
    print('wrote %s (%d lines, sha256 %s); cross-checks agree %d/%d; delta files with redaction-rule values %d; redacted forms printed %d; leak guard clean; value controls refused %d/%d; shape controls refused %d/%d; resolved %d/%d (+%d derived)' % (
        a.out, text.count('\n') + 1, sha256b(text.encode()), len(xc) - n_disc, len(xc), len(delta_rule), len(printed), ctrl_ref, ctrl_n,
        shape_ref, shape_n, len(vals), len(forms), len(guard_extra)))


if __name__ == '__main__':
    main()
