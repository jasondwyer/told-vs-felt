#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12 scrub index (the block's named N12 output, block :84).

Aggregates the committed N12 part raws into one index, one section per sub-item (i)-(vii):

  results/raw/2026-10-08_note-N12-history.{md,json}   (i), (ii), (v), (iv)'s mechanical checks
  results/raw/2026-10-08_note-N12-licenses.{md,json}  (iv)
  results/raw/2026-10-08_note-N12-content.md + -content-screen.json   (vi)

Every part raw is read from the audit commit (default 09c3a8c) with `git show`, never from the
working tree; each outcome and pass line is carried VERBATIM from the line the script finds by
content, with a locator `<path>@<audit>:<line>`. Block locators are pinned to the record commit
(default bbc9ffe). Nothing is re-scanned: the part scripts are not run (re-running them at the
release commit is pre-flip step 3). The only new computations are labelled computed-new:
md-vs-JSON agreement of the carried figures, the commits and paths added after each part's
commit, a delta check of the files those commits changed for the history raw's sensitive
values, and the D1 carrier spread (the four RunPod values: tracked files and commit messages at
the content review's commit and at HEAD) -- counts and paths only. Every figure the index
summarizes in its own words (the D1-D4 table, the PI items, the pre-flip checklist) is either
read from a located line by pattern or asserted present in the line it cites; a mismatch stops
the script before it writes. README-NOTE.md is a sibling part's draft: the index names it and
does not restate or fingerprint its content.

Leak guard: the history JSON lists the values its run treats as sensitive, by redacted form
(first characters + length + sha256 prefix, or length + sha256 prefix for ports). This script
resolves them in memory from the history text by matching those hash prefixes, never prints
one, and refuses to write if any occurs in its output. It also lists every redacted form its
output prints (computed over the text), and refuses to write if one of them is not a form the
history JSON knows, or belongs to a class the history raw lists as recoverable by brute force.

Read-only on the record: git rev-parse / show / ls-tree / ls-files / log / diff / grep /
rev-list / for-each-ref / merge-base only; no git command inside jlens-qwen36/; writes only --out.
Stdlib only.
"""
import argparse
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
VC_MD = 'results/raw/2026-10-08_note-tier1_valuescheck.md'
PART_SCRIPTS = ['scripts/audit_note_N12_history.py', 'scripts/audit_note_N12_licenses.py',
                'scripts/audit_note_N12_content.py']
README_NOTE = 'README-NOTE.md'
LEDGER = ['results/raw/2026-10-08_note-N1-claims-ledger.md', 'results/raw/2026-10-08_note-N1-claims-ledger.json']
CITE_NEEDLE = '_note-N12-scrub'   # how a file would name this index
LORA_FORM = 'zebr...20:c63d5fbd'   # the content raw's redacted form (content md :27), as routed


def git(*args, binary=False, ok=(0,)):
    if os.path.realpath(os.getcwd()).startswith(os.path.join(os.path.realpath(REPO), 'jlens-qwen36')):
        raise SystemExit('refusing to run git inside jlens-qwen36/')
    r = subprocess.run(['git', '-C', REPO, *args], capture_output=True)
    if r.returncode not in ok:
        raise SystemExit('git %s failed: %s' % (' '.join(args), r.stderr.decode(errors='replace')))
    return r.stdout if binary else r.stdout.decode('utf-8', errors='replace')


def sha256b(b):
    return hashlib.sha256(b).hexdigest()


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
    if FORM_DIGITS.match(form):
        return len(re.findall(r'(?<![0-9A-Za-z])%s(?![0-9A-Za-z])' % re.escape(value), text))
    return text.count(value)


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
    ap.add_argument('--audit', default='09c3a8c', help='commit holding the committed part raws')
    ap.add_argument('--pin', default='bbc9ffe', help='record pin for block locators')
    ap.add_argument('--out', default='results/raw/2026-10-08_note-N12-scrub.md')
    a = ap.parse_args()

    stamp = subprocess.run(['date', '-u'], capture_output=True, text=True).stdout.strip()
    head = git('rev-parse', 'HEAD').strip()
    audit = git('rev-parse', a.audit + '^{commit}').strip()
    pin = git('rev-parse', a.pin + '^{commit}').strip()
    A, P = a.audit, a.pin
    git('merge-base', '--is-ancestor', audit, head)   # raises unless the audit commit is on HEAD
    git('merge-base', '--is-ancestor', pin, audit)

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
    blk.need(b['iii'], 'Not a release blocker')
    block_pass = blk.line(b['pass'])

    # ---------- part raws at the audit commit ----------
    H = Doc(audit, A, HIST_MD)
    L = Doc(audit, A, LIC_MD)
    C = Doc(audit, A, CON_MD)
    VC = Doc(audit, A, VC_MD)
    hj = json.loads(git('show', '%s:%s' % (audit, HIST_JSON)))
    lj = json.loads(git('show', '%s:%s' % (audit, LIC_JSON)))
    cj_raw = git('show', '%s:%s' % (audit, CON_JSON), binary=True)
    cj = json.loads(cj_raw)

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
    short = {
        'i': "STOP pending the PI's resolution, on the block's literal text (:77, 'Any hit in history is a STOP on the release')",
        'ii': 'A list, no pass condition; none is a credential.',
        'iv': '(iv) licenses recorded',
        'v': 'PASS -- nothing over 100 MB untreated',
        'vi': 'Expected: nothing; found: nothing in the three classes N12(vi) names.',
    }
    for k, src in (('i', i_line), ('ii', ii_line), ('iv', l_line), ('v', v_line), ('vi', c_line)):
        assert short[k] in src, 'carried excerpt not verbatim: ' + k
    i_stop = "STOP pending the PI's resolution" in i_line
    iv_ok = l_line.startswith('**(iv) licenses recorded**') and lj.get('pass_line') == '(iv) licenses recorded'
    v_ok = 'PASS' in v_line and 'nothing over 100 MB untreated' in v_line

    # ---------- summarized text: read by pattern or asserted against the cited line ----------
    # header: how the part raws describe who cites what
    H.need(h['referent'], 'which the README and the ledger cite together as N12\'s output')
    L.need(lc['part'], "The block's N12 output, `results/raw/<stamp>_note-N12-scrub.md` (block line 84), cites it.")
    L.need(lc['scope_time'], 'this script is to be re-run at the final pre-flip commit', 'the N12 scrub raw states that bound')
    # (i)
    deviation = ('Block :77 runs its fallback only if the scanners are not installable; that condition does not hold, '
                 'so running the fallback instead is a deviation from the block, recorded here for the PI.')
    H.need(h['scanners'], deviation, 'installable here via Homebrew', "forbids installs without the PI's word")
    n_refs = len(hj['refs'])
    if n_refs != sum(1 for i in range(h['scope'], h['i'] - 1) if H.lines[i].startswith('| `refs/')):
        raise SystemExit('refs table and JSON refs disagree')
    n_vc_rounds = sum(1 for ln in H.lines if ln.startswith('## Values-check'))
    tsc, untri, hits_n = hj['true_secret_candidates'], hj['untriaged'], hj['fallback']['hit_lines']
    # (iv)
    proj_n_files = int(L.num(lc['proj'], r'They are untracked at the commit read \((\d+) files'))
    proj_ids = int(L.num(lc['proj'], r'the id sweep would gain \*\*(\d+)\*\* unclassified id'))
    proj_hosts = int(L.num(lc['proj'], r'the host sweep \*\*(\d+)\*\* unclassified host'))
    L.need(lc['proj'], "so the pass line's two sweep gates would fail at the pre-flip re-run until each is classified")
    L.need(lc['it8'], "so the pass line's two sweep gates fail there until each is classified")
    # the two sweep gates, by name, in the licenses JSON and in the committed licenses script
    sweep_gates = ['external-reference sweep: 0 unclassified ids', 'URL-host sweep: 0 unclassified hosts']
    if not all(g in lj['pass_gates'] for g in sweep_gates):
        raise SystemExit('licenses JSON: a sweep gate is not among pass_gates')
    LS = Doc(audit, A, PART_SCRIPTS[1])
    ls_gate = [LS.has('"%s":' % g) for g in sweep_gates]
    ls_fail = LS.has('P(f"**(iv) NOT recorded** -- failed conjunct(s)')
    # each part script's default outputs (a re-run with default arguments overwrites the committed raws)
    HS, CS = Doc(audit, A, PART_SCRIPTS[0]), Doc(audit, A, PART_SCRIPTS[2])

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
    # Output guards of the part scripts (Code's round-3 fix: the re-run warning describes each script's
    # actual behaviour, read from these lines, rather than one rule for all three).
    cs_nooverwrite = CS.has('sys.exit("refusing to overwrite existing %s" % out)')
    hs_rawonly = HS.has('raise SystemExit(f"refusing output inside the repository outside results/raw/: {o}")')
    hs_ownonly = HS.has('raise SystemExit(f"refusing a results/raw/ output other than this part\'s own two files: {o}")')
    L.need(lc['pass'], 'the Macar prompt text is CC BY 4.0 via the paper', 'the two word lists have no license found',
           "the Global Workspace paper's license was not read", 'the repository has no LICENSE file')
    H.need(h['floats'], 'stored logistic readability probe', 'which the README should name')
    C.need(cc['h_iv'] + 1, 'single-line quotes, inside referent checks, from scripts in the gitignored `jlens-qwen36/` clone')
    C.need(cc['h_iv'] + 2, 'citations are published works only')
    # (ii) hand-off headings
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
           'does not hold the tag', 'the identity emails and the laptop hostname')
    H.need(h['pf2'], 'compare its refs with the refs table under Scope', 'gets its own scan',
           'is deleted before the visibility change', '`refs/pull/*` refs cannot be deleted by the owner and become public')
    H.need(h['pf3'], 'pull requests', 'issues and their comments', 'Actions runs with their logs and artifacts', 'the wiki',
           'releases with their assets', 'force-pushed away')
    H.need(h['pf4'], "on the PI's word", "Their findings supersede the fallback's for (i).")
    C.need(cc['rerun'], 'with a new `--json-out` against the release commit', 'read every new 2026-10-08 raw once, end to end')
    H.need(h['pre_ident'], 'the laptop hostname')

    # ---------- provenance of the part raws ----------
    parts = []
    for path in (HIST_MD, HIST_JSON, LIC_MD, LIC_JSON, CON_MD, CON_JSON):
        cb = git('show', '%s:%s' % (audit, path), binary=True)
        wp = os.path.join(REPO, path)
        wb = open(wp, 'rb').read() if os.path.exists(wp) else None
        parts.append((path, sha256b(cb), cb.count(b'\n'), None if wb is None else (wb == cb)))
    scr = {}
    for sp in PART_SCRIPTS:
        scr[sp] = sha256b(git('show', '%s:%s' % (audit, sp), binary=True))
    h_scan, l_scan = hj['head'], lj['commit_read']
    c_scan = cj['rev']['resolved']
    assert h_scan in H.line(h['head']) and l_scan in L.line(lc['commit']) and c_scan in C.line(cc['head'])
    hist_script_rec = hj['script_sha256']
    con_script_rec = re.search(r'sha256 `([0-9a-f]{64})`', C.line(cc['screen'])).group(1)
    con_json_rec = re.findall(r'sha256 `([0-9a-f]{64})`', C.line(cc['screen']))[1]
    lic_script_rec = re.search(r'([0-9a-f]{64})', L.line(L.sw('- Script:')))

    # ---------- cross-checks (computed-new: md text vs the part's own JSON) ----------
    xc = []

    def xadd(what, md_val, js_val, md_loc, js_ptr):
        xc.append((what, md_val, js_val, md_loc, js_ptr, 'computed-new (agree)' if md_val == js_val else 'discrepant'))

    m = re.search(r'fallback ([0-9]+) hit lines', H.line(h['s_i']))
    xadd('(i) fallback hit lines', int(m.group(1)), hits_n, H.loc(h['s_i']), 'fallback.hit_lines')
    m = re.search(r'TRUE-SECRET-CANDIDATE ([0-9]+); UNTRIAGED ([0-9]+)', H.line(h['s_i']))
    xadd('(i) TRUE-SECRET-CANDIDATE', int(m.group(1)), tsc, H.loc(h['s_i']), 'true_secret_candidates')
    xadd('(i) UNTRIAGED', int(m.group(2)), untri, H.loc(h['s_i']), 'untriaged')
    sa = hj['scanner_availability']['which']
    xadd('(i) gitleaks / trufflehog installed', 'no / no' if 'gitleaks not found, trufflehog not found' in H.line(h['scanners']) else '?',
         '%s / %s' % ('no' if sa['gitleaks'] is None else 'yes', 'no' if sa['trufflehog'] is None else 'yes'),
         H.loc(h['scanners']), 'scanner_availability.which')
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
    xadd('(iv) repository LICENSE files at the commit', int(m.group(1)), len(lj['repo_license']['license_files_at_commit']), L.loc(lc['s5'] + 2), 'repo_license.license_files_at_commit')
    m = re.search(r'\*\*File count reviewed: ([0-9]+)\*\* \(([0-9]+) results/raw \+ ([0-9]+) HANDOFF', C.line(cc['count']))
    xadd('(vi) files reviewed (results/raw + HANDOFF at its HEAD)', int(m.group(1)), cj['scope']['results_raw_at_rev'] + cj['scope']['handoff_md_at_rev'], C.loc(cc['count']), 'scope.results_raw_at_rev + scope.handoff_md_at_rev')
    xadd('(vi) screen JSON sha256 recorded vs committed', con_json_rec, sha256b(cj_raw), C.loc(cc['screen']), '(file sha256 at %s)' % A)
    xadd('history script sha256 recorded vs committed', hist_script_rec, scr[PART_SCRIPTS[0]], H.loc(H.sw('- Script:')), '(scripts/audit_note_N12_history.py at %s)' % A)
    xadd('content script sha256 recorded vs committed', con_script_rec, scr[PART_SCRIPTS[2]], C.loc(cc['screen']), '(scripts/audit_note_N12_content.py at %s)' % A)
    xadd('pre-release: audit files with a redaction-rule value', 0 if 'CLEAN for the audit\'s own pending files' in H.line(h['pre_line']) else '?',
         len(pp['audit_files_not_clean']), H.loc(h['pre_line']), 'prerelease_pending_files.audit_files_not_clean')
    xadd("pre-release: the PI's untracked documents carrying a sensitive value", pi_n_with, len(pi_d1), H.loc(h['pre_pi']),
         'prerelease_pending_files.files[group=other].known')

    # ---------- coverage since each part's commit (computed-new) ----------
    since_hist = git('rev-list', '%s..%s' % (h_scan, head)).split()
    since_pin = git('rev-list', '%s..%s' % (pin, head)).split()

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

    # ---------- sensitive values: resolve in memory ----------
    forms = list(pp['known_values'].keys())
    labels = {f: pp['known_values'][f][0] for f in forms}
    corpus = git('log', '-p', '--all', '--format=fuller') + '\n' + \
        git('log', '--all', '--format=%an <%ae>%n%cn <%ce>') + '\n' + \
        git('for-each-ref', '--format=%(taggername) %(taggeremail)', 'refs/tags')
    vals = resolve_values(forms, corpus)
    del corpus
    unresolved = [f for f in forms if f not in vals]
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

    # ---------- README-NOTE.md (presence only: a sibling part's draft, content not read) ----------
    rn_exists = os.path.exists(os.path.join(REPO, README_NOTE))
    rn_tracked = bool(git('ls-files', '--', README_NOTE).strip())
    rn_desc = ('draft at root (see README-NOTE.md); content not restated here' if rn_exists
               else 'not present on disk at this run')
    # ---------- who names this index: the claims ledger (computed-new, at this run) ----------
    cites = []
    for p in LEDGER:
        fp = os.path.join(REPO, p)
        if os.path.exists(fp):
            n = open(fp, encoding='utf-8', errors='replace').read().count(CITE_NEEDLE)
            cites.append('`%s` (%s) %d' % (p, 'tracked' if git('ls-files', '--', p).strip() else 'untracked', n))
        else:
            cites.append('`%s` absent' % p)

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
    w('- HEAD at this run: `%s`. Item raws read at the audit commit `%s` (`%s`); record locators pinned to `%s` (`%s`).' % (head, A, audit, P, pin))
    w('- Block: `%s`, sha256 `%s` at `%s` (blob), working tree %s; routed `8cd8a9ac...3841`: %s; %d lines.' % (
        BLOCK, blk_sha, P, ('`%s` (equal)' % blk_wt) if blk_wt == blk_sha else ('`%s` (DIFFERS)' % blk_wt), 'MATCH' if blk_sha == BLOCK_SHA else 'MISMATCH', len(blk.lines) - (1 if blk.lines[-1] == '' else 0)))
    w('- Item: N12, `%s@%s:%d-%d`. This file is the output the block names at `%s@%s:%d`. N12 was run as three part raws, and this index aggregates them. Who cites what, as the part raws state it: the history raw, which states the split, records that the three part raws are what "the README and the ledger cite together as N12\'s output" (%s); the licenses raw says this file cites it (%s). computed-new, at this run, the number of times the claims ledger names this index (`%s`): %s. `%s`: %s. Whether the README or the ledger should cite this index is not decided here.' % (
        BLOCK, P, b['n12'], b['pass'], BLOCK, P, b['out'], H.loc(h['referent']), L.loc(lc['part']), CITE_NEEDLE, '; '.join(cites),
        README_NOTE, rn_desc))
    w('- Script: `%s`, sha256 `%s`. Interpreter: `%s` (Python %s; stdlib only). Command: `jlens-qwen36/.venv/bin/python %s` (from the repository root).' % (
        me, my_sha, sys.executable, sys.version.split()[0], me))
    w('- Read-only: `git rev-parse / show / ls-tree / ls-files / log / diff / grep / rev-list / for-each-ref / merge-base`. The part scripts were not run and nothing was re-scanned; the part raws are the record and this file indexes them. No git command ran inside `jlens-qwen36/`. Nothing installed, downloaded or inferred. Writes: this file only.')
    w('- Statuses. Each sub-item\'s outcome is carried from its part raw unchanged, with its cause, and quoted verbatim from the line located by content; this index upgrades none. Its own computations carry `computed-new` (the md and JSON of a part agree, a recount agrees with the figure it checks, a coverage count, or the D1 carrier spread of section 9) or `discrepant` (they disagree); none of them reproduces a part\'s scan. Text this index summarizes in its own words (the D1-D4 table, the PI items, the pre-flip checklist) is checked by the script before it writes: each figure is read from the cited line by pattern or asserted present in it. (iii) is `pending`, as routed.')
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
    w('| (i) secrets, full history | yes | history | %s | %s |' % (short['i'], H.loc(h['i_pass'])))
    w('| (ii) identifiers | no (a list) | history | %s | %s |' % (short['ii'], H.loc(h['s_ii'])))
    w('| (iii) continuity password | no ("Not a release blocker", block :%d) | none: not run | pending: the PI supplies the continuity password out of band | `%s@%s:%d` |' % (b['iii'], BLOCK, P, b['iii']))
    w('| (iv) third-party materials and licenses | yes | licenses (+ history\'s mechanical checks) | %s | %s; %s |' % (short['iv'], L.loc(lc['pass']), H.loc(h['s_iv'])))
    w('| (v) size | yes | history | %s | %s |' % (short['v'], H.loc(h['v_pass'])))
    w('| (vi) content review | no | content | %s | %s |' % (short['vi'], C.loc(cc['pass'])))
    w('| (vii) README-for-readers | no | `README-NOTE.md` (a sibling part writes its draft) | not a part raw: %s (%s at this run; section 8) | `%s@%s:%d`, `:%d-%d` |' % (
        rn_desc, 'tracked' if rn_tracked else 'untracked', BLOCK, P, b['vii'], b['s6'], b['s6_body']))
    w('')
    if i_stop and iv_ok and v_ok:
        w('**N12 overall (computed from the three carried lines above):** (i) STOP pending the PI; (iv) licenses recorded; (v) nothing over 100 MB untreated. N12 therefore does not pass at this index, and the block\'s *"On fail: STOP on the release; fallback paragraph"* (`%s@%s:%d`) currently applies; of the three gating lines, (i) is the one not met at the commits the parts read. (i)\'s pass is "(i) no hits, or hits resolved by the PI"; the history raw records %d TRUE-SECRET-CANDIDATE in its triage of the fallback\'s hits and its own scans, and says that resolving the hits is the PI\'s decision, not Code\'s (%s); its summary line records %d UNTRIAGED (%s; JSON `untriaged`). The history raw\'s pre-flip step 4 (the block\'s primary scanners, on the PI\'s word; item 5 of section 10 here) supersedes the fallback for (i) (%s).' % (
            BLOCK, P, b['pass'], tsc, H.loc(h['i_pass']), untri, H.loc(h['s_i']), H.loc(h['pf4'])))
        w('')
        w('Resolving (i) alone does not make N12 pass at the release commit. (iv) and (v) are carried as their parts read them, at %s; N12 passes at the release commit only if the PI resolves (i) and the pre-flip re-runs (section 10, item 3) again print "(iv) licenses recorded" and the (v) PASS. The licenses script prints its pass line only when all of its gates hold, among them "%s" and "%s" (%s, %s); otherwise it prints "(iv) NOT recorded" (%s). The licenses part projects that these two gates fail at that re-run until the ids and hosts in this audit\'s own files are classified (section 5).' % (
            ('`%s`' % l_scan[:10]) if l_scan == h_scan else '`%s` ((iv)) and `%s` ((v))' % (l_scan[:10], h_scan[:10]),
            sweep_gates[0], sweep_gates[1], LS.loc(ls_gate[0]), LS.loc(ls_gate[1]), LS.loc(ls_fail)))
    else:
        w('**N12 overall:** the carried lines do not match the expected pattern ((i) STOP pending=%s, (iv) recorded=%s, (v) PASS=%s); read the part raws.' % (i_stop, iv_ok, v_ok))
    w('')

    # 1. part raws
    w('## 1. Part raws indexed')
    w('')
    w('| file | sha256 at `%s` | lines | working tree equals `%s` | commit the part read |' % (A, A))
    w('|---|---|---|---|---|')
    readat = {HIST_MD: h_scan, HIST_JSON: h_scan, LIC_MD: l_scan, LIC_JSON: l_scan, CON_MD: c_scan, CON_JSON: c_scan}
    for path, s, n, eq in parts:
        w('| `%s` | `%s` | %d | %s | `%s` |' % (path, s, n, {True: 'yes', False: 'NO', None: 'absent'}[eq], readat[path][:10]))
    w('')
    sc_rows = [x for x in xc if x[0] in ('history script sha256 recorded vs committed', 'content script sha256 recorded vs committed')]
    assert len(sc_rows) == 2
    sc_bad = [x[0].split(' ')[0] for x in sc_rows if x[5] != 'computed-new (agree)']
    sc_txt = ('both equal the committed scripts (section 12)' if not sc_bad else
              'section 12 marks %s discrepant: the recorded sha256 does not equal the committed script' % ' and '.join(
                  'the %s script\'s row' % n for n in sc_bad))
    if lic_script_rec is None:
        lic_txt = 'The licenses raw records no script sha256 (its header line `- Script:` names the script only).'
    else:
        lic_txt = 'The licenses raw\'s `- Script:` line records sha256 `%s`, which %s the committed script (%s).' % (
            lic_script_rec.group(1), 'equals' if lic_script_rec.group(1) == scr[PART_SCRIPTS[1]] else 'does NOT equal', L.loc(L.sw('- Script:')))
    w('Part scripts at `%s`: %s. The history raw records its script\'s sha256 and the content raw records the screen script\'s; %s. %s' % (
        A, '; '.join('`%s` `%s`' % (sp, scr[sp]) for sp in PART_SCRIPTS), sc_txt, lic_txt))
    w('')
    w('Scope in time. The history and licenses parts read `%s`; the content part read `%s`. Commits now on HEAD after `%s`: %d (%s), which neither the history nor the licenses scan covers (section 11 checks what they changed). Commits after `%s`: %d, outside the content review\'s tree (section 7).' % (
        h_scan[:10], c_scan[:10], h_scan[:10], len(since_hist), ', '.join('`%s`' % c[:10] for c in since_hist) or 'none', c_scan[:10], len(since_pin)))
    w('')

    # 2. (i)
    w('## 2. (i) Secrets over the entire history (block `%s@%s:%d`)' % (BLOCK, P, b['i']))
    w('')
    w('Outcome and pass line, verbatim (%s):' % H.loc(h['i_pass']))
    w('')
    q(i_line, H.loc(h['i_pass']))
    w('')
    w('Summary line, verbatim (%s):' % H.loc(h['s_i']))
    w('')
    q(H.line(h['s_i']), H.loc(h['s_i']))
    w('')
    w('- Section: %s. The block\'s primary scanners were not run: %s (installable via Homebrew, not installed without the PI\'s word). The history raw labels running the fallback in their place a deviation from block :77, verbatim (%s): "%s"' % (
        H.loc(h['i']), H.loc(h['scanners']), H.loc(h['scanners']), deviation))
    w('- Values-check rounds 1-%d of this part: %s to the end of the file; process record: %s.' % (n_vc_rounds, H.loc(h['vc1']), VC.loc(vc['h'])))
    w('- Scope: every object reachable from the %d local refs at `%s` (%s); refs that exist only on GitHub were not visible (pre-flip step 1 below).' % (n_refs, h_scan[:10], H.loc(h['scope'])))
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
    w('- The decisions this list feeds: D1 (RunPod identifiers) and D3 (commit metadata), section 9.')
    w('')

    # 4. (iii)
    w('## 4. (iii) The continuity password (block `%s@%s:%d`)' % (BLOCK, P, b['iii']))
    w('')
    w('**Status: pending.** The PI supplies the continuity password out of band; Code then searches tracked files and history with it read from a file in session scratch, writes only locators and a yes/no, never the value; the LoRA phrase (redacted `%s`) is one candidate to compare. The block: "Not a release blocker" (`%s@%s:%d`). Nothing below is that search.' % (LORA_FORM, BLOCK, P, b['iii']))
    w('')
    w('What the part raws already record:')
    w('')
    w('- One pass-phrase-shaped value in history, the LoRA overfit phrase: %s; the content review\'s D2 and its flag F44: %s, %s.' % (H.loc(h['passphrase']), C.loc(cc['d2']), C.loc(cc['s52'])))
    w('- `CONTINUITY.md`: never tracked (%s). The phrases "continuity password" / "pass phrase" / "code word" and whether a value follows them: %s.' % (H.loc(h['continuity_md']), H.loc(h['continuity'])))
    w('- The content review\'s hand-off for (iii): %s.' % C.loc(cc['h_iii']))
    w('')

    # 5. (iv)
    w('## 5. (iv) Third-party materials and licenses (block `%s@%s:%d`)' % (BLOCK, P, b['iv']))
    w('')
    w('Outcome and pass line, verbatim (%s):' % L.loc(lc['pass']))
    w('')
    q(l_line, L.loc(lc['pass']))
    w('')
    w('(iv)\'s mechanical checks (jlens-qwen36 tracking, the `.npz` allowlist, model weights), verbatim (%s; section %s):' % (H.loc(h['s_iv']), H.loc(h['iv'])))
    w('')
    q(iv_mech_line, H.loc(h['s_iv']))
    w('')
    w('- The licenses table for the README: %s. The PI items: %s (item 1, the Macar materials: %s; item 2, the repository has no license: %s; item 5, the lenses: %s; item 7, the Global Workspace paper: %s).' % (
        L.loc(lc['s6']), L.loc(lc['s7']), L.loc(lc['it1']), L.loc(lc['it2']), L.loc(lc['it5']), L.loc(lc['it7'])))
    w('- Residual-space float vectors stored in tracked JSON (a stored readability probe), which the history raw says the README should name: %s.' % H.loc(h['floats']))
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
    scope_txt = (' '.join(b + '.' for b in scope_bits)) if scope_bits else 'Nothing under `results/raw/` or `HANDOFF-*.md` changed since that tree.'
    w('- Scope: the review read the tree at `%s` (%s). computed-new: paths under `results/raw/` added between `%s` and HEAD `%s`: %d; modified: %d; `HANDOFF-*.md` added: %d. %s Its %s lists the audit\'s outputs as not reviewed, and %s asks that every new raw be read once, end to end, before the push.' % (
        c_scan[:10], C.loc(cc['head']), c_scan[:10], head[:10], len(raw_added), len(mod), len(hand_added), scope_txt, C.loc(cc['s7']), C.loc(cc['rerun'])))
    if raw_added:
        w('  - added: ' + ', '.join('`%s`' % p.replace('results/raw/', '') for p in raw_added) + ' (all under `results/raw/`).')
    if hand_added:
        w('  - `HANDOFF-*.md` added: ' + ', '.join('`%s`' % p for p in hand_added) + '.')
    w('')

    # 8. (vii)
    w('## 8. (vii) README-for-readers (block `%s@%s:%d`; contents at `:%d-%d`)' % (BLOCK, P, b['vii'], b['s6'], b['s6_body']))
    w('')
    w('- `README-NOTE.md`: %s (%s at this run). A sibling part of this integration writes it; this index neither reviews nor fingerprints it. The history raw\'s pre-release re-scan wants this file and the README in place before the end commit (%s).' % (
        rn_desc, 'tracked' if rn_tracked else 'untracked', H.loc(h['pf1'])))
    w('- N12 inputs to the README, from the part raws: the licenses table (block §6 item (7)), %s; name the residual-space probe vectors stored in JSON, %s; cite no `/Users/` path, %s; give the Global Workspace paper\'s full title and link and credit Lindsey (2025), %s and %s.' % (
        L.loc(lc['s6']), H.loc(h['floats']), H.loc(h['users_rec']), L.loc(lc['it7']), L.loc(lc['it1'])))
    w('')

    # 9. decisions
    w('## 9. Decisions for the PI (D1-D4) and the other open PI items')
    w('')
    w('D1-D4 are the content review\'s, which it introduces as "%s" (%s). None is recorded as decided in the part raws. The table summarizes the cited lines at `%s`; the script reads each figure in it from the cited line or asserts it present there, apart from the D1 row\'s spread at HEAD, which is this run\'s computation (computed-new), and the index\'s own note on option (b). The redacted values are at the locators.' % (
        C.line(cc['dec']).rstrip('.'), C.loc(cc['dec']), A))
    w('')
    w('| id | what | options the part raw gives | locators |')
    w('|---|---|---|---|')
    hd = d1_at[head]
    h_all = d1_union(head, d1_forms, 'files')
    h_cat = d1_cats(h_all)
    h_msgs = d1_union(head, d1_forms, 'msgs')
    pod2_head = sorted(hd['files'][pod2[0]])
    pod2_txt = ('the second pod id is at HEAD in %s only' % ', '.join('`%s`' % p for p in pod2_head)) if pod2_head \
        else 'the second pod id is in no tracked file at HEAD'
    w('| D1 | The RunPod pod id, network-volume id and volume display name of the Phase-2 box (account-resource identifiers, not credentials). The content review\'s counts are at `%s`, the tree it read (%s): %d tracked HANDOFFs, %d tracked raws and %d commit messages (%s), with RESULTS.md and a code test fixture outside its scope (%s). At HEAD `%s` (computed-new, this run, the content review\'s three values plus the history raw\'s second pod id): %d HANDOFFs, %d raws, %s, %d code file(s), %d other file(s) and %d commit messages; %s (%s). The spread at both commits is below the table. The record calls the pod stopped and parked, not terminated. | (a) accept publication, optionally terminating the pod and settling the volume so the ids are inert; (b) redact the HEAD copies (history keeps them) [index note: the content review\'s D1 names three values, so (b) removes the second pod id only if the PI\'s decision names it too]; (c) rewrite history (the PI\'s call). Separately: the `resume.py` test fixture regenerates the pod id into new self-test raws; replacing it is a code change this block forbids, a PI or design-seat decision. | %s; %s; %s; %s; %s |' % (
        c_scan[:10], C.loc(cc['head']), d1_hand, d1_raws, d1_msgs, C.loc(c_bul[0]), C.loc(d1_spread),
        head[:10], h_cat['HANDOFF'], h_cat['raw'], 'RESULTS.md' if h_cat['RESULTS.md'] else 'not RESULTS.md', h_cat['code'], h_cat['other'], len(h_msgs),
        pod2_txt, H.loc(d1_info[pod2[0]]['row']),
        C.loc(cc['d1'], cc['d2'] - 1), C.loc(cc['s4']), C.loc(cc['d1rec'], cc['d1rec'] + 3), C.loc(cc['fixture']),
        H.loc(d1_info[d1_order[0]]['row'], d1_info[d1_order[-1]]['row'])))
    w('| D2 | The LoRA overfit phrase, redacted `%s`: the synthetic target of a LoRA overfit test, not a credential. | The PI compares it with the continuity password out of band (N12(iii)); a match means the password is already in history, and the PI rotates or retires it. | %s; %s; %s |' % (
        LORA_FORM, C.loc(cc['d2'], cc['d3'] - 1), C.loc(cc['f44']), H.loc(h['passphrase'])))
    w('| D3 | Commit metadata: %d commits with `.local` e-mail domains (%d of them use the laptop\'s hostname as the domain, per the history raw; the other %d use a domain the history reviewer reads as a placeholder rather than a machine name); %d commits with a claude.ai session-link trailer; the same %d SSH-signed, embedding a public key. Low sensitivity. | Only a history rewrite changes the objects (`.mailmap` changes the display only), or accept. | %s; %s; %s; %s |' % (
        d3_local, d3_host, d3_local - d3_host, d3_sess, d3_sig, C.loc(cc['d3'], cc['d4'] - 1), C.loc(cc['f46']), H.loc(h['s_ii']), H.loc(h['identities'])))
    w('| D4 | Release staging: %s untracked, not-gitignored design-seat documents (%s with not-for-the-repo headers; none of them in any commit) and %d other untracked root/archive files sit in the checkout. At the history run\'s snapshot, %d of the PI\'s untracked documents carry a D1 identifier (%s): committing any of them adds another carrier of the D1 identifiers. | Stage the release and tag commits by explicit path and check `git diff --cached --name-status`; or move or gitignore the design documents (a PI or design-seat call). No history action. | %s; %s; %s; %s; %s |' % (
        d4_docs.lower(), d4_hdr.lower(), d4_other, len(pi_d1), ', '.join('`%s`' % f for f, _ in pi_d1),
        C.loc(cc['d4']), C.loc(cc['nocommit']), C.loc(cc['d4rec'], cc['d4rec'] + 2), H.loc(h['pre_pi']),
        H.loc(*pi_rows_span) if pi_rows_span else 'none'))
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
    other_head = sorted(p for p in h_all if d1_cat(p) in ('code', 'other'))
    w('- Tracked raws carrying a D1 value at HEAD (%d): %s.' % (len(raws_head), ', '.join('`%s`' % p for p in raws_head) or 'none'))
    w('- Code and other tracked files carrying a D1 value at HEAD (%d): %s.' % (len(other_head), ', '.join('`%s`' % p for p in other_head) or 'none'))
    w('- Carriers added between `%s` and HEAD (%d): %s; removed (%d)%s. Commit messages carrying a D1 value added since: %d. The content review says the `resume.py` fixture regenerates the pod id into every new self-test raw (%s).' % (
        c_scan[:10], len(added_c), ', '.join('`%s`' % p for p in added_c) or 'none', len(gone_c),
        (': ' + ', '.join('`%s`' % p for p in gone_c)) if gone_c else '',
        len(h_msgs - d1_union(c_scan, d1_forms, 'msgs')), C.loc(cc['fixture'])))
    w('- The PI\'s untracked documents are not tracked files and are not counted here; D4 and section 10 item 4 carry the history raw\'s snapshot of them.')
    w('')
    w('Other PI items the part raws carry:')
    w('')
    w('- (i): the %s fallback hit lines are a STOP on the literal text until the PI resolves them; the primary scanners need the PI\'s word to install, and running the fallback in their place is, in the history raw\'s words, "a deviation from the block, recorded here for the PI" (%s, %s, %s).' % (
        '{:,}'.format(hits_n), H.loc(h['i_pass']), H.loc(h['scanners']), H.loc(h['pf4'])))
    w('- (iv): the repository has no LICENSE file (%s); the Macar prompt text is CC BY 4.0 via the paper if the PI accepts that source, and the two word lists have no license found (%s); the Global Workspace paper\'s license was not read (%s).' % (
        L.loc(lc['it2']), L.loc(lc['it1']), L.loc(lc['it7'])))
    w('- (ii): the stale statements that the repository is private (%s).' % C.loc(cc['stale']))
    w('')

    # 10. pre-flip
    w('## 10. Pre-flip checklist (before the visibility change)')
    w('')
    w('As routed, with the part raws\' locators. Each needs the final HEAD, the network or the PI\'s word; none was run here.')
    w('')
    w('1. `git ls-remote origin`; compare its refs with the history raw\'s refs table; scan or delete any extra branch or tag; `refs/pull/*` cannot be deleted and becomes public (%s; %s).' % (H.loc(h['pf2']), L.loc(lc['it6'])))
    w('2. GitHub-side surfaces that become public with the visibility change and cannot be checked offline: pull requests and their comments, issues, Actions runs with logs and artifacts, the wiki, releases and their assets, and commits force-pushed away that GitHub keeps reachable by sha (%s).' % H.loc(h['pf3']))
    w('3. Re-run `scripts/audit_note_N12_history.py` and `scripts/audit_note_N12_content.py` at the release commit. For the history script, the history raw\'s step opens, verbatim: "%s" (%s). Run it immediately before the release commit, with every raw, script and README of the end commit in place (this file and `README-NOTE.md` included), and again at the release commit; its pre-release section must show no redaction-rule value in any file the end commit adds and no new value needing triage. The same step lists the commit identities\' own metadata (the identity emails and the laptop hostname) as not holding the tag as drafted, with "binding either part is the PI\'s call", and ends "The tag should wait on a clean run." For the content script, a new `--json-out` against the release commit, then every new raw read once end to end (%s). The licenses part asks the same of `scripts/audit_note_N12_licenses.py` at the final pre-flip commit, with its counts re-checked, and says this file states that bound (%s, %s); its projection that its two sweep gates fail there is carried, with its open values-check finding, in section 5.' % (
        pf1_first, H.loc(h['pf1']), C.loc(cc['rerun']), L.loc(lc['scope_time']), L.loc(lc['it8'])))
    w('')
    w('   **Re-run outputs, per script.** This index, like any other file that cites the part raws by line at `%s`, points into the committed raws, so a re-run must not silently replace them. The three part scripts behave differently. *Licenses:* `--out` and `--json-out` default to `%s` and `%s` (%s, %s), so a default run overwrites the committed raws; pass new paths, or use `--out-dir`, which puts each output not given by `--out` or `--json-out` into that directory under its default basename (%s). *Content:* `--json-out` defaults to `%s` (%s), and the script refuses to overwrite an existing file (%s); give a new `--json-out` under `results/raw/`. *History:* `--out` and `--json-out` default to `%s` and `%s` (%s, %s); inside the repository it accepts only `results/raw/` paths (%s) whose basename is one of its own two (%s), so it can write either to the defaults (overwriting the committed raws; regenerate this index afterwards) or to the same basenames in a subdirectory of `results/raw/`, or anywhere outside the repository. The licenses script\'s pass line names the history raw at its fixed default path, whatever path the history re-run writes (%s). This script\'s own `--out` defaults to this file, so the same applies to it once it is committed.' % (
        A, LIC_MD, LIC_JSON, LS.loc(out_defaults['licenses'][0]), LS.loc(out_defaults['licenses'][1]), LS.loc(ls_outdir),
        CON_JSON, CS.loc(out_defaults['content'][0]), CS.loc(cs_nooverwrite),
        HIST_MD, HIST_JSON, HS.loc(out_defaults['history'][0]), HS.loc(out_defaults['history'][1]),
        HS.loc(hs_rawonly), HS.loc(hs_ownonly), LS.loc(ls_histraw)))
    w('4. Review untracked files before any commit adds them: the untracked root and archive files were not reviewed (%s). At the history run\'s snapshot, %d of the PI\'s %d untracked or modified documents carry a D1 identifier (%s; rows %s), so staging any of them adds another carrier of the D1 identifiers. Stage by explicit path (D4, %s).' % (
        C.loc(cc['untracked']), len(pi_d1), pi_n_scanned, H.loc(h['pre_pi']), H.loc(*pi_rows_span) if pi_rows_span else 'none', C.loc(cc['d4rec'])))
    w('5. Also carried: the block\'s primary scanners (gitleaks, trufflehog) on the PI\'s word, over the repository at the release commit; their findings supersede the fallback\'s for (i) (%s).' % H.loc(h['pf4']))
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
    w('')

    # 12. cross-checks
    w('## 12. Index cross-checks (computed-new: each part\'s md against its own JSON, a committed file, or a recount at the commit the part read)')
    w('')
    w('| figure | md | JSON / committed / recount | md locator | JSON field or source | status |')
    w('|---|---|---|---|---|---|')
    for what, mv, jv, ml, jp, st in xc:
        w('| %s | %s | %s | %s | `%s` | %s |' % (what, ('`%s`' % mv) if isinstance(mv, str) and len(mv) == 64 else mv,
                                             ('`%s`' % jv) if isinstance(jv, str) and len(jv) == 64 else jv, ml, jp, st))
    n_disc = sum(1 for x in xc if x[5] == 'discrepant')
    w('')
    w('Agree: %d of %d; discrepant: %d.' % (len(xc) - n_disc, len(xc), n_disc))
    w('')

    # 13. open values-check items
    w('## 13. Open values-check items (carried; not applied)')
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

    # ---------- redacted forms printed (computed over the text) ----------
    body = '\n'.join(o)
    known_by_key = {}
    for f in forms:
        known_by_key[form_key(f)] = f
    printed = {}
    for mm in FORM_IN_TEXT.finditer(body):
        printed.setdefault(mm.group(0), 0)
        printed[mm.group(0)] += 1
    caveat = H.line(h['caveat'])
    bad = []
    descs = []
    for fm in sorted(printed):
        kf = known_by_key.get(form_key(fm))
        if kf is None:
            bad.append('redacted form %s is not one the history JSON knows' % fm)
            continue
        lab = labels[kf]
        expo = exposure_of(caveat, lab)
        if expo == 'Recoverable by brute force':
            bad.append('redacted form of class %s, which the history raw lists as recoverable by brute force' % lab.split(' (')[0])
        in_q = sorted({loc for ln, loc in quotes if fm in ln})
        n_q = sum(ln.count(fm) for ln, _ in quotes)
        own = printed[fm] - n_q
        where = []
        if own:
            where.append('%d time(s) in this index\'s own text%s' % (own, ', as routed' if fm == LORA_FORM else ''))
        if n_q:
            where.append('%d time(s) inside the verbatim quote of %s' % (n_q, ', '.join(in_q)))
        descs.append('`%s` (the history JSON\'s class `%s`; the history raw lists the class as "%s", %s): %s' % (
            fm, lab.split(' (')[0], expo.lower(), H.loc(h['caveat']), '; '.join(where)))
    red = ('- Redaction. No identifier value appears in this file: RunPod ids and names, SSH ports, the container and laptop hostnames, the session link and the commit identities\' emails are named by class, with locators into the part raws that hold their redacted forms. '
           'Redacted forms printed here, computed over this file\'s text apart from this paragraph: %d -- %s. The LoRA phrase\'s is the content raw\'s form (%s). '
           'Leak guard: the script resolves in memory, from `git log -p --all` and the commit/tag headers, each of the %d values the history raw treats as sensitive (its JSON `prerelease_pending_files.known_values`), by matching their redacted forms\' sha256 prefixes; resolved %d, unresolved %d (%s). It refuses to write this file if any resolved value occurs in it, if it prints a redacted form the history JSON does not know or one of a class the history raw lists as recoverable by brute force, or if it contains an IPv4 literal, a claude.ai session or artifact path, an SSH SHA256 fingerprint shape, a local temp or transcript-store path, or a bare 4-5 digit number other than a year on an ssh/port line.') % (
        len(printed), '; '.join(descs) or 'none', C.loc(cc['d2']), len(forms), len(vals), len(unresolved),
        '; '.join('%s: not verbatim in history, which the history raw states at %s' % (labels[f], H.loc(h['caveat'])) for f in unresolved) or 'none')
    text = body.replace(REDACTION_SLOT, red)
    assert REDACTION_SLOT not in text and '\0' not in text

    # ---------- leak guard ----------
    for f, v in vals.items():
        if count_value(f, v, text):
            bad.append('resolved value of class %s' % labels[f])
    for name, rx in GUARD_SHAPES:
        lines_hit = sorted({text.count('\n', 0, mm.start()) + 1 for mm in rx.finditer(text)})
        if lines_hit:
            bad.append('%s (output lines %s)' % (name, ', '.join(map(str, lines_hit))))
    if bad:
        raise SystemExit('LEAK GUARD: refusing to write; found: ' + '; '.join(bad))

    out = os.path.join(REPO, a.out)
    if os.path.islink(out):
        raise SystemExit('refusing to write through a symlink')
    with open(out, 'w') as fh:
        fh.write(text)
    print('wrote %s (%d lines, sha256 %s); cross-checks agree %d/%d; delta files with redaction-rule values %d; redacted forms printed %d; leak guard clean; resolved %d/%d' % (
        a.out, text.count('\n') + 1, sha256b(text.encode()), len(xc) - n_disc, len(xc), len(delta_rule), len(printed), len(vals), len(forms)))


if __name__ == '__main__':
    main()
