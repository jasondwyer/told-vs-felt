#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12(i): trufflehog over the entire history, verified-only plus its unknown results, with
Code's triage.

Release v2 (tag note-2026-10-v2). The block names trufflehog beside gitleaks (:77); v1's release ran gitleaks only (Code's
question 4, "gitleaks' default skip of .svg files and trufflehog not run are acceptable", which the PI answered on
2026-10-12, "Yes to all five; tag it", for v1's run). For v2 the PI's word of 2026-10-29 (his answer to Code's question
whether that carries), verbatim, is TRUFFLEHOG_V2_PI_WORDS: "Install and run trufflehog over all history for v2,
verified-only mode, raw committed; triage any finding as gitleaks’ were; TRUE-SECRET or UNTRIAGED is a STOP". Code
installed trufflehog on that word (Homebrew's bottle of TRUFFLEHOG_VERSION). This script runs

    trufflehog git file://<repository> --results=verified,unknown --json --no-update --no-color --no-ignore-tag
        --fail-on-scan-errors

from the repository root, with every GIT_* variable of the environment removed (GIT_NO_REPLACE_OBJECTS=1 set, as for
gitleaks). The git source clones the repository into a temporary directory (every ref: branches, remote-tracking refs and
tags) and reads every commit's patch, as trufflehog reads it (its own skips of binary blobs by extension or size are not
measured here). Verified-only mode (`--results=verified`) outputs only the candidates whose verification against their
issuer succeeded: trufflehog sends a detected candidate to its issuer's API to verify it, except when more than one
detector found it (verification is then withheld). Results whose verification errored or was withheld (its `unknown`
class) verified-only mode neither outputs nor counts, so this run adds `unknown` (`--results=verified,unknown`), on the
PI's word of 2026-10-29 to Code's question on them (UNKNOWN_V2_PI_WORDS): each is shown redacted and triaged like a
verified finding, and an uncleared one is a STOP; the verified results are the verified-only mode's, unchanged.
Candidates detected but not confirmed valid, with no verification error (the `unverified` class), are not output. `--no-ignore-tag` makes inline ignore comments
ineffective; the commits whose diff adds or removes that literal are counted and printed. The results are read from trufflehog's
standard output (a pipe, held in memory only); no results file is written. No matched value is ever written: a finding
is printed by detector, commit, file, line and a redacted form (first 4 characters, length, the first 8 hex of its
sha256), with Code's triage verdict keyed by fingerprint (class:commit:file:detector:line:sha8; the class is verified or unknown), as gitleaks' were; a finding
with no verdict is UNTRIAGED, and a verdict with no recorded PI word (TRIAGE_PI) is a fresh STOP, as gitleaks' v2
entries are (the seat's item A).

Positive control, before the history scan, in a throwaway repository in a temporary directory: three random
GitHub-token-shaped probes (generated at run time, never written out) -- one on a commit only a remote-tracking ref
reaches, one under a `-diff` attribute path, one in an .svg file. (a) The same command with `--no-verification` and
`--results=unverified,filtered_unverified` (no network) must find each probe at its path: the scan reaches every ref,
the -diff path class and .svg files. (b) The command as the history scan runs it (`--results=verified,unknown`) must
output nothing (the probes are not live tokens), and its summary must record verification time: verification of the
control's GitHub-shaped probes reached GitHub's API at this run. It does not show that the history scan's own candidates
were verified without error; a verification error, or one trufflehog withholds, is the `unknown` class, which this run
shows and triages; the history scan's verification attempts are printed by count.

The gate fails closed. It is a STOP (exit 1) when: a finding is UNTRIAGED or TRUE-SECRET; a TRIAGE entry has no recorded
PI word (TRIAGE_PI); a TRIAGE fingerprint is not re-found; trufflehog is not TRUFFLEHOG_VERSION; its exit code is not 0;
any stdout line does not parse as JSON; its log has no "finished scanning" line, records no chunks or no bytes scanned,
or has an error-level line or a line that does not parse; either control part fails; the attribute check over history's
paths does not complete; or a diff/binary-attribute path in history is not one gitleaks' script lists (KNOWN_ATTR_PATHS:
the path known at v1's release run, 2026-10-12, and the four Q-F0 paths listed on the PI's word of 2026-10-28). It
refuses (exit 2, nothing written) when --out is a tracked path, the write guard's values cannot be read, trufflehog is not
on PATH, or the text would carry a finding's matched value, a control probe, or the origin-only ref (its namespace, id
or commit). Its
coverage bound: the history at this run's HEAD; the commits after it are covered by no trufflehog run, since the
tag-commit re-runs (TAG_RERUNS_V2, the PI's word of 2026-10-29: the five N12 scans) do not include it.

    python -B scripts/audit_note_N12_trufflehog.py [--out results/raw/2026-10-30_note-N12-trufflehog-release.md]
"""
import argparse
import hashlib
import importlib.util
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
DEFAULT_OUT = "results/raw/2026-10-30_note-N12-trufflehog-release.md"   # the v2 release run (block section 2 item 1)
# The v2 run's companion raws (the same run date): gitleaks' and the history script's.
GL_RAW = "results/raw/2026-10-30_note-N12-gitleaks-release.md"
HIST_RAW = "results/raw/2026-10-30_note-N12-history-release.md"
assert os.path.basename(GL_RAW)[:10] == os.path.basename(DEFAULT_OUT)[:10] == os.path.basename(HIST_RAW)[:10], \
    "DEFAULT_OUT, GL_RAW and HIST_RAW: more than one run date"
GL_SCRIPT = "scripts/audit_note_N12_gitleaks.py"
TAG_V2 = "note-2026-10-v2"
TRUFFLEHOG_VERSION = "3.99.7"
# The PI's word of 2026-10-29 on trufflehog for v2 (his answer to Code's question, item 2), verbatim.
TRUFFLEHOG_V2_PI_WORDS = ("2026-10-29", "Install and run trufflehog over all history for v2, verified-only mode, raw "
                                        "committed; triage any finding as gitleaks’ were; TRUE-SECRET or UNTRIAGED "
                                        "is a STOP")
# The scans re-run at the v2 tag commit, before the push (the PI's word of 2026-10-29, item 3): trufflehog is not among
# them, so this run's coverage ends at its HEAD.
TAG_RERUNS_V2 = ("gitleaks", "password", "history", "content", "licenses")
# The PI's answer of 2026-10-29 to Code's question whether the run of record also shows trufflehog's `unknown` results
# (verification errored or withheld), redacted, and triages them like findings: the option he chose, verbatim (Code's
# "(Recommended)" marker left off).
UNKNOWN_V2_PI_WORDS = ("2026-10-29", "Yes, show and triage")
RESULTS_FLAG = "--results=verified,unknown"
TAG_RERUNS_V2_PI_WORDS = ("2026-10-29", "All five at the tag commit — history, content, licenses, gitleaks, the "
                                        "password search — as v1 did, raws committed after the tag; item 1 now is "
                                        "the baseline.")
assert "trufflehog" not in TAG_RERUNS_V2
# trufflehog's inline-ignore literal, built from two pieces so that neither this script nor its raw contains it.
IGNORE_LIT = "trufflehog" ":ignore"
IGNORE_SHOWN = "`trufflehog` + `:ignore`"
CMD_FLAGS = ["--json", "--no-update", "--no-color", "--no-ignore-tag", "--fail-on-scan-errors"]

# Code's triage, keyed by fingerprint (class:commit:file:detector:line:sha8 of the matched value; the class is verified
# or unknown). Each entry is read in
# context with `git show <commit>:<file>` before it is entered. None at this commit.
TRIAGE = {}
VERDICTS = ("TRUE-SECRET", "FALSE-POSITIVE")
assert all(v_[0] in VERDICTS and v_[1].strip() for v_ in TRIAGE.values())
# The PI's dated words resolving each TRIAGE entry (fingerprint -> ("YYYY-MM-DD", his words, verbatim)). Every trufflehog
# finding is new at v2, so each entry needs one, as gitleaks' v2 entries need theirs (TRIAGE_V2_PI there; the seat's
# item A, "any new finding is a fresh STOP"); an entry without it is a STOP. None at this commit.
TRIAGE_PI = {}
assert set(TRIAGE_PI) <= set(TRIAGE) and all(
    isinstance(v_, tuple) and len(v_) == 2 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v_[0]) and v_[1].strip()
    for v_ in TRIAGE_PI.values()), "a TRIAGE_PI value is not (date, the PI's words) for a TRIAGE entry"


def git(*args, **kw):
    """git in the repository, with every inherited GIT_* variable removed (clean_env), so that the raw's HEAD, refs,
    counts and attribute list describe the repository trufflehog scans."""
    kw.setdefault("env", clean_env())
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, **kw)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def red(v):
    """first 4 characters + '...' + [len N] + '#' + sha256[:8] (the history script's form)."""
    return "%s...[len %d]#%s" % (v[:4], len(v), hashlib.sha256(v.encode()).hexdigest()[:8])


def load_gitleaks():
    """gitleaks' script as a module (its write guard and KNOWN_ATTR_PATHS); its main() is not run."""
    spec = importlib.util.spec_from_file_location("audit_note_N12_gitleaks", os.path.join(ROOT, GL_SCRIPT))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def clean_env(**extra):
    """The environment with every GIT_* variable removed (no inherited GIT_DIR, GIT_INDEX_FILE, GIT_CONFIG_* or the like
    can point git at another repository), plus `extra`."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(extra)
    return env


def th(cmd, cwd):
    """Run trufflehog; returns (returncode, results [dict], log [dict], unparsed stdout lines)."""
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=clean_env(GIT_NO_REPLACE_OBJECTS="1"))
    res, bad = [], []
    for ln in r.stdout.splitlines():
        if not ln.strip():
            continue
        try:
            res.append(json.loads(ln))
        except ValueError:
            bad.append(ln)
    log = []
    for ln in r.stderr.splitlines():
        try:
            d_ = json.loads(ln)
        except ValueError:
            d_ = {"level": "unparsed", "msg": ln}
        log.append(d_ if isinstance(d_, dict) else {"level": "unparsed", "msg": ln})
    return r.returncode, res, log, bad


def git_md(f):
    """A result's git source metadata: (commit, file, line)."""
    g = ((f.get("SourceMetadata") or {}).get("Data") or {}).get("Git") or {}
    return g.get("commit") or "", g.get("file") or "", g.get("line")


def raw_of(f):
    return f.get("Raw") or f.get("RawV2") or ""


def fingerprint(f):
    """class:commit:file:detector:line:sha8 -- the class (verified or unknown) is part of it, so an entry made for a
    result whose verification errored never clears the same value once its issuer verifies it."""
    c, p, ln = git_md(f)
    return "%s:%s:%s:%s:%s:%s" % ("verified" if f.get("Verified") else "unknown", c, p, f.get("DetectorName"), ln,
                                  hashlib.sha256(raw_of(f).encode()).hexdigest()[:8])


def summary_of(log):
    """trufflehog's 'finished scanning' log line, or None."""
    s = [d_ for d_ in log if d_.get("msg") == "finished scanning"]
    return s[-1] if s else None


def errors_of(log, subs):
    """Error-level (or unparsed) log lines, made safe to commit: the message and error text only, each (path, placeholder)
    of `subs` replaced, longest first; capped at 200 characters."""
    out = []
    for d_ in log:
        lv = str(d_.get("level", ""))
        if not (lv.startswith("error") or lv in ("unparsed", "fatal", "panic")):
            continue
        s = "%s %s %s" % (lv, d_.get("msg", ""), d_.get("error", ""))
        for a_, b_ in sorted(subs, key=lambda x: -len(x[0])):
            if a_:
                s = s.replace(a_, b_)
        s = s.replace("`", "'")
        out.append(s[:200] + ("..." if len(s) > 200 else ""))
    return out


def control(td):
    """The positive control (docstring). Returns (rows, ok, notes) -- rows: (part, what, expected, got, ok)."""
    rep = os.path.join(td, "control")
    os.mkdir(rep)
    env = clean_env(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull, GIT_CONFIG_NOSYSTEM="1",
                    GIT_CEILING_DIRECTORIES=td)

    def g(*a):
        r = subprocess.run(["git"] + list(a), cwd=rep, capture_output=True, text=True, env=env)
        if r.returncode != 0:
            raise RuntimeError("control repository: git %s failed" % a[0])
        return r.stdout.strip()

    al = string.ascii_letters + string.digits
    probes = {p_: "ghp_" + "".join(secrets.choice(al) for _ in range(36)) for p_ in ("side.txt", "ckpt/x.json", "fig.svg")}
    g("init", "-q", "-b", "main")
    if os.path.realpath(g("rev-parse", "--absolute-git-dir")) != os.path.realpath(os.path.join(rep, ".git")):
        raise RuntimeError("control repository: git does not resolve to the control's own .git")
    # the control's identity is a bare word (no address: nothing address-shaped enters this script or its raw)
    for k, v in (("user.email", "control"), ("user.name", "control"), ("commit.gpgsign", "false")):
        g("config", k, v)
    with open(os.path.join(rep, "a.txt"), "w") as fh:
        fh.write("hello\n")
    g("add", "a.txt")
    g("commit", "-q", "-m", "init")
    g("checkout", "-q", "-b", "side")
    with open(os.path.join(rep, "side.txt"), "w") as fh:
        fh.write("probe %s\n" % probes["side.txt"])   # a bare word before the probe: no key-and-value shape here
    g("add", "side.txt")
    g("commit", "-q", "-m", "side")
    side = g("rev-parse", "HEAD")
    g("checkout", "-q", "main")
    g("update-ref", "refs/remotes/origin/only", side)
    g("branch", "-q", "-D", "side")
    os.mkdir(os.path.join(rep, "ckpt"))
    with open(os.path.join(rep, ".gitattributes"), "w") as fh:
        fh.write("/ckpt/** -diff\n")
    with open(os.path.join(rep, "ckpt", "x.json"), "w") as fh:
        fh.write('{"github": "%s"}\n' % probes["ckpt/x.json"])
    with open(os.path.join(rep, "fig.svg"), "w") as fh:
        fh.write('<svg xmlns="http://www.w3.org/2000/svg"><desc>%s</desc></svg>\n' % probes["fig.svg"])
    g("add", ".gitattributes", "ckpt/x.json", "fig.svg")
    g("commit", "-q", "-m", "main")
    rows, notes = [], []
    # (a) detection, no network
    cmd_a = ["trufflehog", "git", "file://" + rep, "--no-verification", "--results=unverified,filtered_unverified"] + CMD_FLAGS
    rc_a, res_a, log_a, bad_a = th(cmd_a, td)
    found = {}
    for f in res_a:
        c, p, _ln = git_md(f)
        found.setdefault(p, set()).add(raw_of(f))
    for p_, v_ in probes.items():
        ok_ = v_ in found.get(p_, set())
        where = {"side.txt": "a commit only a remote-tracking ref reaches", "ckpt/x.json": "a `-diff` attribute path",
                 "fig.svg": "an .svg file"}[p_]
        rows.append(("(a)", "probe in %s (`%s`), found at its path" % (where, p_), "yes", "yes" if ok_ else "NO", ok_))
    rows.append(("(a)", "exit code; unparsed output lines", "0; 0", "%d; %d" % (rc_a, len(bad_a)), rc_a == 0 and not bad_a))
    # (b) verification reached the issuer: no output under verified,unknown, and verification time recorded
    cmd_b = ["trufflehog", "git", "file://" + rep, "--results=verified,unknown"] + CMD_FLAGS
    rc_b, res_b, log_b, bad_b = th(cmd_b, td)
    s_b = summary_of(log_b) or {}
    vt = ((s_b.get("verification_caching") or {}).get("VerificationTimeSpentMS"))
    rows.append(("(b)", "results under `--results=verified,unknown` (the probes are not live tokens)", "0",
                 "%d" % len(res_b), not res_b))
    rows.append(("(b)", "verification time in the summary (ms; > 0: verification reached the issuer)", "> 0",
                 "%s" % vt, isinstance(vt, (int, float)) and vt > 0))
    rows.append(("(b)", "exit code; unparsed output lines", "0; 0", "%d; %d" % (rc_b, len(bad_b)), rc_b == 0 and not bad_b))
    # the probes never reach the raw: only booleans and counts above
    notes.append([v_ for v_ in probes.values()])
    notes.append((s_b.get("verified_secrets"), s_b.get("unverified_secrets")))
    return rows, all(r_[4] for r_ in rows), notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    a = ap.parse_args()
    outp = os.path.realpath(a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out))
    rel_out = os.path.relpath(outp, os.path.realpath(ROOT))
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
    gl = load_gitleaks()
    tvals = gl.teleport_vals()
    if tvals is None:
        print("refused: the write guard's values (the origin-only ref the design seat's answers name, their section 2) "
              "could not be read from %s:%s; nothing written" % gl.ANSWERS_V2)
        return 2
    th_path = shutil.which("trufflehog")
    if not th_path:
        print("refused: trufflehog is not installed (`shutil.which` finds none); nothing written")
        return 2
    vr = subprocess.run(["trufflehog", "--version"], capture_output=True, text=True)
    ver = (vr.stdout + vr.stderr).strip()
    th_sha = sha256(os.path.realpath(th_path))
    head = git("rev-parse", "HEAD", text=True).stdout.strip()
    rel_raw = rel_out == DEFAULT_OUT
    stamp = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%S UTC"], capture_output=True, text=True).stdout.strip()
    genv = clean_env(GIT_NO_REPLACE_OBJECTS="1")
    n_commits = git("rev-list", "--all", "--count", text=True, env=genv).stdout.strip()
    refs = [x for x in git("for-each-ref", "--format=%(objectname) %(refname)", text=True).stdout.split("\n") if x.strip()]
    il = git("log", "--all", "--text", "-S" + IGNORE_LIT, "--format=%H", text=True, env=genv)
    ignore_commits = [x for x in il.stdout.split() if x] if il.returncode == 0 else None
    # Paths in history whose diff/binary attributes are set (git check-attr), against gitleaks' list (v1's path and the
    # four Q-F0 paths of the PI's word of 2026-10-28)
    names = git("log", "--all", "--format=", "--name-only", "-z", env=genv).stdout
    names = sorted(set(x for x in names.replace(b"\n", b"\0").split(b"\0") if x))
    ca = subprocess.run(["git", "check-attr", "--stdin", "-z", "diff", "binary"], cwd=ROOT, capture_output=True, env=genv,
                        input=b"\0".join(names) + b"\0")
    parts = ca.stdout.split(b"\0")
    attr_ok = (ca.returncode == 0 and len(parts) == 6 * len(names) + 1 and parts[-1] == b""
               and all(parts[6 * i] == nb and parts[6 * i + 1] == b"diff" and parts[6 * i + 3] == nb
                       and parts[6 * i + 4] == b"binary" for i, nb in enumerate(names)))
    attr_paths = sorted(set(parts[i].decode("utf-8", "surrogateescape") for i in range(0, len(parts) - 2, 3)
                            if parts[i + 2] != b"unspecified"))
    new_attr = sorted(set(attr_paths) - set(gl.KNOWN_ATTR_PATHS))
    with tempfile.TemporaryDirectory(prefix="audit_note_trufflehog_") as td:
        try:
            c_rows, c_ok, c_notes = control(td)
        except RuntimeError as e_:
            c_rows, c_ok, c_notes = [("(a)", str(e_), "the control repository built", "NOT BUILT", False)], False, [[], (None, None)]
        cmd = ["trufflehog", "git", "file://" + ROOT, RESULTS_FLAG] + CMD_FLAGS
        rc, res, log, bad = th(cmd, ROOT)
        subs = [(td, "<tmp>"), (os.path.realpath(td), "<tmp>"), (tempfile.gettempdir(), "<tmp>"),
                (os.path.realpath(tempfile.gettempdir()), "<tmp>"), ("file://" + ROOT, "file://<repo>"),
                (ROOT, "<repo>"), (os.path.realpath(ROOT), "<repo>"), (os.path.expanduser("~"), "~")]
        errs = errors_of(log, subs)
    summ = summary_of(log)
    probes = c_notes[0] if c_notes else []
    out = []
    w = out.append
    w("# AUDIT-note-release v1.2 -- N12(i): trufflehog over the entire history (verified-only, plus its unknown results)")
    w("")
    w("- Code stamp: %s (date -u); HEAD `%s`" % (stamp, head))
    w("- Block `%s` sha256 `%s`" % (BLOCK, sha256(os.path.join(ROOT, BLOCK))))
    w("- Script `scripts/audit_note_N12_trufflehog.py` sha256 `%s`; interpreter %s (Python %s); gitleaks' script "
      "(loaded for its write guard and attribute list) `%s` sha256 `%s`" % (
          sha256(os.path.abspath(__file__)), sys.executable, sys.version.split()[0], GL_SCRIPT,
          sha256(os.path.join(ROOT, GL_SCRIPT))))
    w("- The PI's word (%s), verbatim: \"%s\". trufflehog installed by Code on that word from Homebrew's bottle; "
      "`trufflehog --version`: `%s` (required: %s); the binary's sha256 `%s`." % (
          TRUFFLEHOG_V2_PI_WORDS[0], TRUFFLEHOG_V2_PI_WORDS[1], ver, TRUFFLEHOG_VERSION, th_sha))
    shown = " ".join(cmd).replace("file://" + ROOT, "file://<repo>")
    if ignore_commits is None:
        ign_s = "the count of commits adding or removing the inline-ignore literal (%s) could not be computed" % IGNORE_SHOWN
    elif not ignore_commits:
        ign_s = ("0 commits in history add or remove the inline-ignore literal (%s; `git log --all --text -S`), so "
                 "`--no-ignore-tag` does not change this scan's result" % IGNORE_SHOWN)
    else:
        ign_s = ("%d commit(s) in history add or remove the inline-ignore literal (%s; `git log --all --text -S`: %s); "
                 "`--no-ignore-tag` neutralises them (a note, not a STOP)" % (
                     len(ignore_commits), IGNORE_SHOWN, ", ".join("`%s`" % c[:10] for c in ignore_commits)))
    w("- Command: `%s`, run from the repository root. trufflehog's git source clones the repository into a temporary "
      "directory (every ref: branches, remote-tracking refs and tags) and reads every commit's patch, as trufflehog reads "
      "it (its own skips of binary blobs by extension or size are not measured here); every GIT_* variable of the "
      "environment removed, GIT_NO_REPLACE_OBJECTS=1. Verified-only (`--results=verified`, the PI's mode) outputs only "
      "candidates whose verification against their issuer succeeded; trufflehog sends a detected candidate to its "
      "issuer's API to verify it, except when more than one detector found it (verification is then withheld). Its "
      "`unknown` class (verification errored or withheld), which verified-only mode neither outputs nor counts, is added "
      "(`unknown` in `--results`) on the PI's word of %s to Code's question on it, verbatim: \"%s\"; each unknown result "
      "is shown redacted and triaged like a verified finding; candidates detected but not confirmed valid, with no "
      "verification error (the `unverified` class), are not output. The control's part (b) shows that verification of its "
      "GitHub-shaped probes reached GitHub's API at this run. The results are read from "
      "trufflehog's standard output (a pipe, held in memory only); no results file is written, and no matched value is "
      "written here. `--no-ignore-tag` makes inline ignore comments ineffective; %s. Exit code: %d. Output lines: %d "
      "result(s) (verified %d, unknown %d), %d unparsed." % (
          (shown,) + UNKNOWN_V2_PI_WORDS + (ign_s, rc, len(res), sum(1 for f in res if f.get("Verified")),
                                            sum(1 for f in res if not f.get("Verified")), len(bad))))
    if summ:
        vc = summ.get("verification_caching") or {}
        w("- trufflehog's summary (its `finished scanning` log line): chunks %s, bytes %s, verified_secrets %s, "
          "unverified_secrets %s (the control's part (b), whose three probes trufflehog detects and does not verify, "
          "records verified_secrets %s and unverified_secrets %s under `--results=verified,unknown`: in a verified mode "
          "the summary's counts are not a count of the candidates detected), scan duration %s, version %s; "
          "verification (the history scan's own; a result is output when verified or unknown -- its verification errored "
          "or was withheld -- and not when unverified: detected, not confirmed valid, no verification error): cache "
          "misses %s "
          "(attempts), hits %s, time spent %s ms." % (
              summ.get("chunks"), summ.get("bytes"), summ.get("verified_secrets"), summ.get("unverified_secrets"),
              c_notes[1][0], c_notes[1][1], summ.get("scan_duration"), summ.get("trufflehog_version"),
              vc.get("Misses"), vc.get("Hits"), vc.get("VerificationTimeSpentMS")))
    else:
        w("- trufflehog's log has no `finished scanning` line -- STOP (the scan did not complete).")
    w("- Refs at this run (`git for-each-ref`): %d (listing sha256 `%s`); tags: %s; commits (`git rev-list --all "
      "--count`, GIT_NO_REPLACE_OBJECTS=1): %s. The clone holds what these refs reach, the history GitHub is to hold; "
      "commits no ref reaches are not scanned (the release goes to a fresh repository holding main and the tags, so "
      "none is pushed)." % (
          len(refs), hashlib.sha256("\n".join(refs).encode()).hexdigest()[:16],
          ", ".join("`%s`" % x.split()[1][len("refs/tags/"):] for x in refs if x.split()[1].startswith("refs/tags/"))
          or "none", n_commits or "UNKNOWN"))
    w("- Paths in history with a diff or binary attribute set (`git log --all --name-only` through `git check-attr diff "
      "binary`; %d paths checked): %s%s; trufflehog reads them (its git source scans a path git renders as binary from "
      "its blob, the control's part (a)), as gitleaks' `--text` scan does for gitleaks' list (`KNOWN_ATTR_PATHS` in "
      "`%s`: the path known at v1's release run, 2026-10-12, and the four Q-F0 paths listed on the PI's word of "
      "2026-10-28)%s." % (
          len(names), ", ".join("`%s`" % p for p in attr_paths) or "none",
          "" if attr_ok else " -- the attribute check did not complete (STOP)", GL_SCRIPT,
          "" if not new_attr else "; NOT on that list -- STOP: " + ", ".join("`%s`" % p for p in new_attr)))
    if errs:
        for ln in errs:
            w("- trufflehog error-level log line -- STOP: `%s`" % ln)
    else:
        w("- trufflehog error-level log lines: 0.")
    w("")
    w("## Positive control (a throwaway repository in a temporary directory; random probes, never written out)")
    w("")
    w("| part | check | expected | got | ok |")
    w("|---|---|---|---|---|")
    for p_, what, exp_, got_, ok_ in c_rows:
        w("| %s | %s | %s | %s | %s |" % (p_, what, exp_, got_, "yes" if ok_ else "NO -- STOP"))
    w("")
    w("## Findings (verified and unknown)")
    w("")
    untriaged, true_c = 0, 0
    fps = set()
    if res:
        w("| # | class | detector | file | commit | line | match (redacted) | Code's verdict | reason |")
        w("|---|---|---|---|---|---|---|---|---|")
        for i, f in enumerate(res, 1):
            fp = fingerprint(f)
            fps.add(fp)
            verdict, reason = TRIAGE.get(fp, ("UNTRIAGED", "no verdict recorded for this fingerprint"))
            untriaged += verdict == "UNTRIAGED"
            true_c += verdict == "TRUE-SECRET"
            c, p, ln = git_md(f)
            w("| %d | %s | %s | `%s` | `%s` | %s | `%s` | %s | %s |" % (
                i, "verified" if f.get("Verified") else "unknown", f.get("DetectorName"), p, c[:10], ln, red(raw_of(f)) if raw_of(f) else "(no match text)", verdict,
                reason))
    else:
        w("None: trufflehog output no verified and no unknown result.")
    w("")
    missing = sorted(set(TRIAGE) - fps)
    no_pi = sorted(k_ for k_ in TRIAGE if k_ not in TRIAGE_PI)
    w("## Outcome")
    w("")
    w("- Findings (verified and unknown): %d. TRUE-SECRET: %d. FALSE-POSITIVE: %d. UNTRIAGED: %d. TRIAGE entries re-found: %d of %d%s." % (
        len(res), true_c, len(res) - true_c - untriaged, untriaged, len(TRIAGE) - len(missing), len(TRIAGE),
        "" if not missing else " -- not re-found, STOP: " + ", ".join("`%s`" % m for m in missing)))
    w("- TRIAGE entries with the PI's recorded word (TRIAGE_PI): %d of %d%s%s." % (
        len(TRIAGE) - len(no_pi), len(TRIAGE),
        "" if not (set(TRIAGE) & set(TRIAGE_PI)) else ": " + "; ".join(
            "`%s` (the PI, %s: \"%s\")" % ((k_,) + TRIAGE_PI[k_]) for k_ in TRIAGE if k_ in TRIAGE_PI),
        "" if not no_pi else
        " -- a fresh STOP for each without it (the seat's item A; the PI resolves it): " + ", ".join(
            "`%s`" % k_ for k_ in no_pi)))
    reasons = []
    if untriaged:
        reasons.append("%d untriaged finding(s)" % untriaged)
    if true_c:
        reasons.append("%d true secret(s)" % true_c)
    if missing:
        reasons.append("%d TRIAGE entr(ies) not re-found" % len(missing))
    if ver != "trufflehog " + TRUFFLEHOG_VERSION:
        reasons.append("trufflehog version %r, not %s" % (ver, TRUFFLEHOG_VERSION))
    if rc != 0:
        reasons.append("trufflehog exit code %d" % rc)
    if bad:
        reasons.append("%d unparsed output line(s)" % len(bad))
    if not summ:
        reasons.append("no \"finished scanning\" line in trufflehog's log")
    elif not all(isinstance(summ.get(k_), int) and summ.get(k_) > 0 for k_ in ("chunks", "bytes")):
        reasons.append("trufflehog's summary records no chunks or no bytes scanned")
    if no_pi:
        reasons.append("%d TRIAGE entr(ies) with no recorded PI word (a fresh STOP under the seat's item A)" % len(no_pi))
    if errs:
        reasons.append("%d error-level log line(s)" % len(errs))
    if not c_ok:
        reasons.append("the positive control failed")
    if not attr_ok:
        reasons.append("the attribute check over history's paths did not complete")
    if new_attr:
        reasons.append("%d attribute path(s) not on gitleaks' list" % len(new_attr))
    stop = bool(reasons)
    tag_c = gl.tag_commit(TAG_V2)
    cover = ("This run covers the history at HEAD `%s`%s. The commits after it are covered by no trufflehog run: the "
             "re-runs at the tag commit are the five N12 scans (the PI's word of %s, verbatim: \"%s\"), and trufflehog "
             "is not among them; gitleaks, also a secret scanner, is." % (
                 head[:10], (" (the tag `%s` points at `%s`)" % (TAG_V2, tag_c[:10])) if tag_c else "",
                 TAG_RERUNS_V2_PI_WORDS[0], TAG_RERUNS_V2_PI_WORDS[1]))
    if stop:
        w("- STOP: %s. The release waits on the PI." % "; ".join(reasons))
    else:
        w("- trufflehog's part of (i): 0 TRUE-SECRET and 0 UNTRIAGED among the verified and unknown results over every ref's "
          "history as trufflehog reads it (the -diff path class and .svg files included, as the control shows; its own "
          "skips of binary blobs are not measured here), the scan completed (exit 0, a `finished scanning` line with "
          "chunks and bytes scanned, 0 error-level lines) on version %s, and the positive control passed. %s%s" % (
              TRUFFLEHOG_VERSION, "" if rel_raw else "(A rehearsal or a re-run: --out is not the release raw `%s`.) "
              % DEFAULT_OUT, cover))
    w("- %s and %s are the same run's gitleaks and history raws; (i) carries only on all three." % (GL_RAW, HIST_RAW))
    text = "\n".join(out) + "\n"
    # the write guards: no finding's or probe's matched value, and not the origin-only ref the answers name
    vals = [raw_of(f) for f in res] + [x for f in res for x in (f.get("RawV2") or "",)] + list(probes)
    if any(v_ and len(v_) >= 8 and (v_ in text or v_.lower() in text.lower()) for v_ in vals):
        print("refused: the raw would carry a matched value; nothing written")
        return 2
    bad_g = gl.guarded(text, tvals)
    if bad_g:
        print("refused: the raw would carry %s; nothing written" % "; ".join(bad_g))
        return 2
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s: %d findings (verified and unknown), %d untriaged, %d true-secret; control %s; %s" % (
        gl.shown_path(outp, rel_out), len(res), untriaged, true_c, "pass" if c_ok else "FAIL",
        "STOP" if stop else "pass"))
    return 1 if stop else 0


if __name__ == "__main__":
    sys.exit(main())
