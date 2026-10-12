#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12(i): gitleaks over the entire history, with Code's triage.

The block names gitleaks first (:77). The PI installed gitleaks and reported, 2026-10-09,
"gitleaks over all history found 4 leaks". This script runs the same scan with secrets
redacted (--redact=100), writes the report to a temporary file outside the repository,
and records each finding: rule, file, commit, line, gitleaks fingerprint, the key or
context text gitleaks matched with the secret already redacted, and Code's triage verdict
with its reason. Verdicts are keyed by fingerprint, and a finding with no verdict is
printed as UNTRIAGED. No secret value is ever written: the report is redacted at source.

Release run (the PI's answer of 2026-10-12, "Yes to all five; tag it"): the default output is
the NEW dated raw results/raw/2026-10-12_note-N12-gitleaks-release.md, and the script refuses
to write any path git already tracks, so a committed raw is never overwritten. It also runs
`gitleaks dir` over .txt copies of the five release files (the preprint, note v0.6, the three
2026-10-10 renders) as HEAD holds them: each is read from HEAD's blob (`git cat-file`), its
sha256 asserted, and the working-tree copy asserted equal. gitleaks' default config skips .svg
files by path (accepted by the PI, answer 4), and the copies are an extra check, not a substitute.

The gate fails closed. It is a STOP (exit 1) when: a finding has no verdict or is a true secret;
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

    python -B scripts/audit_note_N12_gitleaks.py [--out results/raw/2026-10-12_note-N12-gitleaks-release.md]
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
DEFAULT_OUT = "results/raw/2026-10-12_note-N12-gitleaks-release.md"
GITLEAKS_VERSION = "8.30.1"
SUPPRESS_ENV = ("GITLEAKS_CONFIG", "GITLEAKS_CONFIG_TOML")
# gitleaks' inline-allow literal, built from two pieces so that neither this script nor its raw contains it
# (committing either would otherwise add a match to the count this script prints).
ALLOW_LIT = "gitleaks" ":allow"
ALLOW_SHOWN = "`gitleaks` + `:allow`"

# The five release files the tag commit holds (the PI's answer of 2026-10-12, question 5), with
# the sha256 each must have. gitleaks dir scans .txt copies of them.
RELEASE = [
    ("PREPRINT-v1_0-draft.md", "d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6"),
    ("RESEARCH-NOTE-v0_6-draft.md", "2c7e1cf526f6dfe737c6246cf137f1ae9bc18816846e8329de2f9c3c04426fbb"),
    ("2026-10-10_F1a_headline-strip.svg", "6ffad6cd971aabdc70d7b684a6408988c9a05e5445125d3ce61a78557405cee6"),
    ("2026-10-10_F1b_five-link-panels.svg", "6fcb060f6a2cf2c0ce1f5374c3267c5cec67304994a9967e49a2afaffcf6113e"),
    ("2026-10-10_F2_macar-lineage-roc_post.svg", "81b13e805e64e6a9534e65e6dfeb50d6c6a65cf3d8b02b9cb3a1e36852e5ac4e"),
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
# Paths in history whose diff/binary attributes are set (git check-attr), known at the release preparation.
# They are read because the history scan passes --text. A path not listed here is a STOP: the --text scan reads
# it too, but whether gitleaks may read a -diff path is a question for the PI and the seat, path by path.
KNOWN_ATTR_PATHS = {"data/m/ckpt/G-CAL_qwen.json"}
# History paths gitleaks' default global path allowlist skips (measured by the probe), known at the release
# preparation: the three 2026-10-10 renders (the .svg skip, the PI's answer of 2026-10-12, question 4) and the
# .png added in ba67acb. Every historical version of a skipped path is scanned as a .txt copy; a skipped path
# not listed here is a STOP.
KNOWN_SKIP_PATHS = {
    "2026-10-10_F1a_headline-strip.svg",
    "2026-10-10_F1b_five-link-panels.svg",
    "2026-10-10_F2_macar-lineage-roc_post.svg",
    "figures/fig1_inverted_u.png",
}
# Root names gitleaks dir reads as its own config or ignore file: never mirrored by the probe.
GL_ROOT_NAMES = (".gitleaks.toml", ".gitleaksignore")
# The PI's four (routing of 2026-10-09), by fingerprint.
PI_FOUR = (
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:611",
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:651",
    "cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55:data/m/gates/G-CAL_completability_qwen.json:generic-api-key:44",
    "1bdf16c149698e3b1181f082b8c169727e9df3c8:data/e2d/closure_valuescheck.json:generic-api-key:46",
)


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
    ver = subprocess.run(["gitleaks", "version"], capture_output=True, text=True).stdout.strip()
    head = git("rev-parse", "HEAD", text=True).stdout.strip()
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
      "not read the three renders; the PI accepted that skip (answer of 2026-10-12, question 4), and the next section "
      "scans every version of every skipped path as a copy. As a check on the release files themselves the "
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
    w("- Of the triaged findings, two are in this audit's own triage table (`961e90a`); the others are a content hash "
      "in a G-CAL gate artifact, a claim identifier in an e2d values-check record, and (added for the release run) a "
      "source file's sha256 in the G-SHAPE-F0 gate's provenance (`f23b444`, dated 2026-10-10, after the PI's scan) "
      "and the same G-CAL key-set hash in the G-CAL checkpoint's identity (`cf8eb5b`, data/m/ckpt/, read only by the "
      "--text scan; verified 64-character lowercase hex equal to gcal.py's key_set_sha256 without reading the "
      "blinded file out). "
      "All are matched by the generic-api-key rule on a field, column or path word ('token', 'key', 'key_set_sha256', "
      "'keys').")
    w("- Block :77 makes any hit in history a STOP on the release that the PI resolves, and history rewriting is "
      "the PI's decision. The PI's D1 routing (2026-10-09) is to leave history as is. trufflehog was not run (not "
      "installed); the PI accepted that, and the .svg skip, in the answer of 2026-10-12 (question 4). The default "
      "config also skips the .png listed above; its versions are scanned as copies in the section above.")
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
        w("- gitleaks' part of (i): 0 TRUE-SECRET and 0 UNTRIAGED in history (every file rendered as text by git, "
          "the -diff path class included; gitleaks' default global path allowlist skips %d history paths, %s, and "
          "every version of each is scanned as a copy with 0 findings), every TRIAGE entry re-found, every scan "
          "completed on the default config (commits scanned = git rev-list --all --count less any listed "
          "deletion-only commits, 0 ERR lines); 0 findings on the release-file copies; the five release files at "
          "HEAD match. By the PI's answer of 2026-10-12 (question 3), ruling 4 (the PI's rulings of 2026-10-09, item 4) "
          "covers the release run's (i) when this raw and results/raw/2026-10-12_note-N12-history-release.md both "
          "show 0 true-secret candidates and 0 untriaged." % (
              len(skipped), ", ".join("`%s`" % x for x in skipped)))
    text = "\n".join(out) + "\n"
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s: %d history findings, %d untriaged, %d true-secret; release copies: %d findings, %d hash mismatches; "
          "skipped paths %d, their copies %d findings" % (a.out, len(findings), untriaged, true_c, len(dfind), rel_bad,
                                                          len(skipped), len(sfind)))
    return 1 if stop else 0


if __name__ == "__main__":
    sys.exit(main())
