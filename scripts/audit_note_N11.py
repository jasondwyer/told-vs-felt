#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N11 (block :64-70): fresh-clone smoke test.

Read-only on the record. What it does, in order:

  (1) a true clone of this repository (``git clone --no-local file://...``,
      or --source) into a fresh scratch directory, with
      GIT_CONFIG_GLOBAL=/dev/null and GIT_CONFIG_NOSYSTEM=1 so that no user
      or system git config applies (and so no nbstripout filter definition),
      GIT_ATTR_NOSYSTEM=1 so that the system gitattributes file of the git
      in use does not apply (GIT_CONFIG_NOSYSTEM does not turn it off),
      and HOME and XDG_CONFIG_HOME pointed at an empty scratch directory so
      that git's per-user default excludes and attributes files do not apply
      either; then a detached checkout of --ref. Every stderr line of clone
      and checkout is kept, and ``git status --porcelain`` shows whether the
      tree is clean. The system attributes file is reported (presence, line
      count, a probe with and without GIT_ATTR_NOSYSTEM, and how many
      tracked paths it would change).
  (2) the suite from the clone's root, four times: (a) ``python -E -s -c
      <WRAPPER>``, a wrapper that installs ``sys.addaudithook`` and records
      the suite's existence tests (os.path.exists/isfile/isdir/lexists,
      wrapped to return the real result); (b) plain, ``python -E -s -m
      valence_core.regression.analysis``; (c) isolated (-S, with only numpy
      reachable through a symlink shim); (d) the README's literal command,
      ``python -m valence_core.regression.analysis``, no flags. The hook
      classifies every opened/listed path as clone, interpreter installation,
      suite-created temp, device, base-env site-packages, base prefix
      (other), or OUTSIDE (the last three all count as outside the clone;
      under the base prefix only its stdlib and a small allow-list -- the
      interpreter binary and the shared libraries directly in
      <base prefix>/lib -- count as the interpreter's). Then (e) a second fresh
      clone at the commit that wrote README.md's 103/103 (git blame at the
      block's commit) runs the suite of that commit, and its check labels
      are compared with --ref's.
  (3) every link and code path in README.md at --ref resolved against the
      clone; the 103/103 and /Users/, /workspace/ greps over the tracked
      text files at --ref.
  (4) the clones, TMPDIRs, empty HOME, shim and hook reports are deleted at
      the end. A status table (reproduced / discrepant / not found /
      computed-new) closes the raw.

Writes only --out (default results/raw/2026-10-08_note-N11-smoke.txt). For a
fixed --ref commit, interpreter and machine state, the raw regenerates
byte-for-byte apart from the header lines its own header names.
No model is loaded; nothing is installed or downloaded.
"""

from __future__ import annotations

import argparse
import fnmatch
import glob
import hashlib
import json
import os
import re
import shlex
import shutil
import stat
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH = ("/private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/"
           "c4fd7649-e4c4-4072-abde-05a4ace7b6a1/scratchpad/N11")
DEFAULT_OUT = os.path.join(REPO, "results/raw/2026-10-08_note-N11-smoke.txt")
DEFAULT_PY = os.path.join(REPO, "jlens-qwen36/.venv/bin/python")
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PIN = "bbc9ffe"          # the commit the block and its preflight raw entered at
PIN_FULL = "bbc9ffe72fb8a942431c9bf2622a36e581fdf93c"
PREFLIGHT = "results/raw/2026-10-08_note-preflight.md"
SITECHECK = "results/raw/2026-10-07_m-dispositions_sitecheck.txt"
SUITE_MOD = "valence_core.regression.analysis"
SUITE_PATH = "valence_core/regression/analysis.py"
SUMMARY_RE = re.compile(r"^\s*(\d+)/(\d+) reproduced through valence_core\s*$")
NOTE = "RESEARCH-NOTE-v0_2-draft.md"
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
# git's progress meter: "<Phase words>: <pct>% (<k>/<n>)[, <rate>][, done.]"
PROGRESS_RE = re.compile(r"^(remote: )?[A-Z][A-Za-z ]*:\s+\d{1,3}% "
                         r"\(\d+/\d+\)(,.*)?$")
# classes that conjunct (d) counts as reads outside the clone
BASE_SP = "base-env site-packages"
# anything else under the base prefix that is not its stdlib and not the
# allow-list (e.g. another conda environment under envs/, the package cache
# pkgs/): outside. The allow-list -- the interpreter binary itself and the
# shared libraries directly in <base prefix>/lib -- is the interpreter's.
BASE_OTHER = "base prefix (other)"
BASE_ALLOW = "interpreter: base-prefix allow-list"
OUTSIDE_CLASSES = ("OUTSIDE", BASE_SP, BASE_OTHER)
SHLIB_RE = re.compile(r"\.(dylib|so(\.\d+)*)$")
# a suite check line: "  [PASS] <name padded to a run-wide width> expected ..."
CHECK_RE = re.compile(r"^  \[(PASS|FAIL)\] ")

# ---------------------------------------------------------------------------
# The wrapper the hooked and isolated suite runs execute (passed with -c, so
# no file). sys.argv[1] is the JSON report path (outside the clone);
# sys.argv[2] is the mode, "hooked" or "isolated"; in isolated mode
# sys.argv[3] is the shim directory and sys.argv[4] the interpreter's
# purelib (site-packages), used only for the after-run negative control.
# ---------------------------------------------------------------------------
WRAPPER = r'''
import sys, os
_rec = []
_q = []
_st = {"on": False, "busy": False}
# events recorded, and how many leading args to keep (env dicts are never kept)
_EV = {"open": 3, "os.listdir": 1, "os.scandir": 1, "glob.glob": 2,
       "os.mkdir": 1, "tempfile.mkdtemp": 1, "tempfile.mkstemp": 1,
       "os.remove": 1, "os.rmdir": 1, "os.rename": 2, "shutil.rmtree": 1,
       "os.chdir": 1, "subprocess.Popen": 3, "os.system": 1, "os.exec": 2,
       "os.posix_spawn": 2, "os.spawn": 3, "ctypes.dlopen": 1}
def _norm(x):
    if isinstance(x, (bytes, bytearray)):
        return bytes(x).decode("utf-8", "surrogateescape")
    if x is None or isinstance(x, (str, int, bool, float)):
        return x
    try:
        return os.fspath(x)
    except TypeError:
        r = repr(x)
        return r if len(r) <= 400 else r[:400] + "..."
def _hook(ev, args):
    if not _st["on"] or _st["busy"]:
        return
    if ev == "exec":            # code object executed: keep its filename only
        fn = getattr(args[0], "co_filename", None) if args else None
        _rec.append(["exec", fn if isinstance(fn, str) else None])
        return
    if ev == "compile":         # (source, filename): never keep the source
        fn = args[1] if len(args) > 1 else None
        _rec.append(["compile", fn if isinstance(fn, str) else None])
        return
    k = _EV.get(ev)
    if k is None:
        return
    _st["busy"] = True
    try:
        _rec.append([ev] + [_norm(a) for a in args[:k]])
    except Exception as e:
        _rec.append([ev, "<unrecordable %r>" % (e,)])
    finally:
        _st["busy"] = False
# Existence tests have no audit event (os.stat raises none), so the four
# os.path predicates are wrapped: the original is called first and its result
# (or exception) is what the caller gets; the wrapper only records it.
import posixpath as _pp
def _wrapq(name):
    orig = getattr(_pp, name)
    def w(p, _o=orig, _n=name):
        r = _o(p)
        if _st["on"] and not _st["busy"]:
            _st["busy"] = True
            try:
                _q.append([_n, _norm(p), bool(r)])
            except Exception:
                pass
            finally:
                _st["busy"] = False
        return r
    w.__name__, w.__doc__, w.__wrapped__ = orig.__name__, orig.__doc__, orig
    setattr(_pp, name, w)
for _n in ("exists", "lexists", "isfile", "isdir"):
    _wrapq(_n)
_report = sys.argv[1]
_mode = sys.argv[2]
_cwd = os.getcwd()
_dropped = []
if _mode == "isolated":
    _shim, _purelib = sys.argv[3], sys.argv[4]
    _keep = []
    for p in sys.path[1:]:
        if p and "site-packages" not in p:
            _keep.append(p)
        else:
            _dropped.append(p)
    sys.path[:] = [_cwd] + _keep + [_shim]
else:
    sys.path[0] = _cwd          # -m semantics: the cwd heads sys.path
sys.argv = [sys.argv[0]]
_path0 = list(sys.path)
_pre = sorted(sys.modules)      # loaded at interpreter startup, before the hook
sys.addaudithook(_hook)
_st["on"] = True
import runpy
_code = 0
try:
    runpy.run_module("valence_core.regression.analysis", run_name="__main__",
                     alter_sys=True)
except SystemExit as e:
    c = e.code
    if c is None:
        _code = 0
    elif isinstance(c, int):
        _code = c
    else:
        print(c, file=sys.stderr)
        _code = 1
except BaseException:
    import traceback
    traceback.print_exc()
    _code = 1
_st["on"] = False
sys.stdout.flush()
sys.stderr.flush()
_names = sorted(sys.modules)
_neg = {}
if _mode == "isolated":
    # after the run: is any other site-packages top-level name reachable?
    # find_spec on a top-level name searches sys.path; it executes nothing.
    import importlib.util as _iu
    for name in sorted(os.listdir(_purelib)):
        full = os.path.join(_purelib, name)
        if name.endswith(".py"):
            base = name[:-3]
        elif name.endswith(".so"):
            base = name.split(".")[0]
        elif os.path.isdir(full):
            base = name
        else:
            continue
        if not base.isidentifier() or base.startswith("__") or base == "numpy":
            continue
        if base in sys.modules:
            _neg[base] = ["in sys.modules", None]
            continue
        try:
            sp = _iu.find_spec(base)
        except Exception as e:
            _neg[base] = ["error", type(e).__name__]
            continue
        if sp is None:
            _neg[base] = ["none", None]
        else:
            locs = list(sp.submodule_search_locations or [])
            _neg[base] = ["found", [sp.origin] + locs]
import json, sysconfig
import importlib.metadata as _md
try:
    _p2d = _md.packages_distributions()
except Exception:
    _p2d = {}
_tops = {}
for n in _names:
    t = n.split(".")[0]
    if t in _tops:
        continue
    m = sys.modules.get(t)
    f = getattr(m, "__file__", None) if m is not None else None
    if f is None and m is not None:
        sp = getattr(m, "__spec__", None)
        f = getattr(sp, "origin", None) if sp is not None else None
    v = getattr(m, "__version__", None) if m is not None else None
    dists = []
    for d in _p2d.get(t, []):
        try:
            dists.append([d, _md.version(d)])
        except Exception:
            dists.append([d, None])
    _tops[t] = {"file": f, "module_version": v if isinstance(v, str) else None,
                "dists": dists,
                "stdlib": t in sys.stdlib_module_names,
                "builtin": t in sys.builtin_module_names,
                "preloaded": t in _pre}
_mfiles = []
for n in _names:
    m = sys.modules.get(n)
    try:
        f = getattr(m, "__file__", None)
    except Exception:
        f = None
    if isinstance(f, str):
        _mfiles.append([n, f])
rep = {"version": sys.version, "version_info": list(sys.version_info[:3]),
       "mode": _mode, "module_files": _mfiles,
       "executable": sys.executable, "prefix": sys.prefix,
       "base_prefix": sys.base_prefix, "exec_prefix": sys.exec_prefix,
       "base_exec_prefix": sys.base_exec_prefix,
       "paths": sysconfig.get_paths(),
       "flags": {"ignore_environment": sys.flags.ignore_environment,
                 "no_user_site": sys.flags.no_user_site,
                 "no_site": sys.flags.no_site,
                 "isolated": sys.flags.isolated},
       "cwd": _cwd, "sys_path_at_start": _path0, "dropped_path": _dropped,
       "exit": _code, "events": _rec, "exists_queries": _q, "neg": _neg,
       "tops": _tops, "n_modules": len(_names)}
with open(_report, "w") as fh:
    json.dump(rep, fh, indent=1, sort_keys=True)
sys.exit(_code)
'''


# ---------------------------------------------------------------------------
def sh(cmd, cwd=None, env=None, timeout=3600):
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True,
                       timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_env(empty_home=None):
    """The environment every git command on a clone runs under.
    GIT_CONFIG_GLOBAL=/dev/null and GIT_CONFIG_NOSYSTEM=1 turn off the
    per-user and system config files; GIT_ATTR_NOSYSTEM=1 turns off the
    system gitattributes file of the git in use, which GIT_CONFIG_NOSYSTEM
    does not. With empty_home, HOME and XDG_CONFIG_HOME point at that
    (empty) directory, so git's per-user defaults -- core.excludesFile
    ($XDG_CONFIG_HOME/git/ignore, else ~/.config/git/ignore) and
    core.attributesFile (.../git/attributes) -- resolve to files that do
    not exist."""
    env = {k: v for k, v in os.environ.items()
           if not k.startswith("GIT_") and k != "XDG_CONFIG_HOME"}
    env["GIT_CONFIG_GLOBAL"] = "/dev/null"
    env["GIT_CONFIG_NOSYSTEM"] = "1"
    env["GIT_ATTR_NOSYSTEM"] = "1"
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["LC_ALL"] = "C"
    if empty_home:
        env["HOME"] = empty_home
        env["XDG_CONFIG_HOME"] = empty_home
    return env


def peruser_git_files():
    """This machine's per-user git files that git reads by default when HOME
    and XDG_CONFIG_HOME are the user's: (label, path, exists, n non-comment
    lines). Contents are not printed."""
    out = []
    xdg = os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config")
    for label, path in (("~/.gitconfig", os.path.expanduser("~/.gitconfig")),
                        ("$XDG_CONFIG_HOME/git/config (or ~/.config/git/config)",
                         os.path.join(xdg, "git", "config")),
                        ("$XDG_CONFIG_HOME/git/ignore (or ~/.config/git/ignore; "
                         "git's default core.excludesFile)",
                         os.path.join(xdg, "git", "ignore")),
                        ("$XDG_CONFIG_HOME/git/attributes (or "
                         "~/.config/git/attributes; git's default "
                         "core.attributesFile)",
                         os.path.join(xdg, "git", "attributes"))):
        n = None
        if os.path.isfile(path):
            try:
                n = sum(1 for x in open(path, errors="replace").read()
                        .splitlines() if x.strip() and
                        not x.strip().startswith(("#", ";")))
            except OSError:
                n = None
        out.append((label, path, os.path.isfile(path), n))
    return out


def system_attr_report(clone, genv, home):
    """The system gitattributes file of the git in use, which
    GIT_CONFIG_NOSYSTEM does not turn off (GIT_ATTR_NOSYSTEM does). git
    builds it as $(sysconfdir)/gitattributes beside $(sysconfdir)/gitconfig,
    so the candidates are the 'gitattributes' beside every system-level
    config file git names (git config --system, and the non-local origins of
    git config --list --show-origin, both with the system config allowed;
    run in the empty HOME, not in a clone). Then two measurements on the
    clone, the only git commands on it that run without GIT_ATTR_NOSYSTEM:
    probe names built from the file's '*.<ext>' patterns, through
    git check-attr -a with and without the variable; and git check-attr
    --stdin -a over the clone's tracked paths, with and without it."""
    env_cfg = {k: v for k, v in genv.items()
               if k not in ("GIT_CONFIG_NOSYSTEM", "GIT_ATTR_NOSYSTEM")}
    env_cfg["GIT_CEILING_DIRECTORIES"] = os.path.dirname(home)
    cfgs = set()
    rc, so, se = sh(["git", "config", "--system", "--list", "--show-origin"],
                    cwd=home, env=env_cfg)
    for x in so.splitlines():
        if x.startswith("file:") and "\t" in x:
            cfgs.add(x.split("\t", 1)[0][5:])
    m = re.search(r"unable to read config file '([^']+)'", se)
    if m:
        cfgs.add(m.group(1))
    rc2, so2, _ = sh(["git", "config", "--list", "--show-origin",
                      "--show-scope"], cwd=home, env=env_cfg)
    for x in so2.splitlines():
        pp = x.split("\t")
        if len(pp) >= 3 and pp[1].startswith("file:") and \
                pp[0] not in ("local", "worktree", "command", "global"):
            cfgs.add(pp[1][5:])
    cands = []
    exts = []
    for c in sorted(cfgs):
        p = os.path.join(os.path.dirname(c), "gitattributes")
        if any(p == x[0] for x in cands):
            continue
        n = None
        if os.path.isfile(p):
            lines = [x.strip() for x in open(p, errors="replace")
                     .read().splitlines()
                     if x.strip() and not x.strip().startswith("#")]
            n = len(lines)
            for x in lines:
                mm = re.match(r"^\*\.([A-Za-z0-9_+-]+)\s", x + " ")
                if mm and mm.group(1) not in exts:
                    exts.append(mm.group(1))
        cands.append((p, os.path.isfile(p), n))
    env_attr = {k: v for k, v in genv.items() if k != "GIT_ATTR_NOSYSTEM"}
    probes = ["n11-probe.%s" % e for e in exts]

    def attr_paths(env, paths):
        if not paths:
            return 0, ""
        _, so_, _ = sh(["git", "-C", clone, "check-attr", "-a", "--"] + paths,
                       env=env)
        return len({x.split(":", 1)[0] for x in so_.splitlines()
                    if ":" in x}), so_
    p_on, _ = attr_paths(env_attr, probes)
    p_off, _ = attr_paths(genv, probes)
    _, lf, _ = sh(["git", "-C", clone, "ls-files", "-z"], env=genv)
    tracked = [x for x in lf.split("\0") if x]

    def attr_all(env):
        p = subprocess.run(["git", "-C", clone, "check-attr", "--stdin", "-z",
                            "-a"], input="\0".join(tracked) + "\0",
                           capture_output=True, text=True, env=env)
        f = p.stdout.split("\0")
        rows = {}
        for i in range(0, len(f) - 2, 3):
            rows.setdefault(f[i], set()).add((f[i + 1], f[i + 2]))
        return p.returncode, rows
    rc_on, a_on = attr_all(env_attr)
    rc_off, a_off = attr_all(genv)
    changed = sorted(x for x in set(a_on) | set(a_off)
                     if a_on.get(x) != a_off.get(x))
    return dict(cands=cands, n_probes=len(probes), probe_on=p_on,
                probe_off=p_off, n_tracked=len(tracked), changed=changed,
                rc=(rc_on, rc_off),
                n_with_attr=(len(a_on), len(a_off)))


def under(path, root):
    if not root:
        return False
    root = root.rstrip(os.sep)
    return path == root or path.startswith(root + os.sep)


def filter_sections(cfg_text):
    """[filter "x"] sections and their keys, from a git config file's text."""
    out, cur = [], None
    for line in cfg_text.splitlines():
        s = line.strip()
        m = re.match(r'^\[\s*filter\s+"([^"]+)"\s*\]$', s)
        if m:
            cur = m.group(1)
            continue
        if s.startswith("["):
            cur = None
            continue
        if cur and "=" in s and not s.startswith(("#", ";")):
            k, v = s.split("=", 1)
            out.append((cur, k.strip(), v.strip()))
    return out


def rmtree_force(path):
    def onerr(func, p, _exc):
        try:
            os.chmod(p, stat.S_IWUSR | stat.S_IRUSR | stat.S_IXUSR)
            func(p)
        except OSError:
            pass
    shutil.rmtree(path, onerror=onerr)


def show_lines(rev, path, cwd=REPO, env=None):
    p = subprocess.run(["git", "-C", cwd, "show", "%s:%s" % (rev, path)],
                       capture_output=True, text=True, env=env)
    return p.stdout.splitlines() if p.returncode == 0 else None


def find_lines(lines, needle, regex=False):
    if lines is None:
        return []
    if regex:
        rx = re.compile(needle)
        return [(i, x) for i, x in enumerate(lines, 1) if rx.search(x)]
    return [(i, x) for i, x in enumerate(lines, 1) if needle in x]


# ---------------------------------------------------------------------------
class Out:
    def __init__(self):
        self.lines = []

    def __call__(self, s=""):
        self.lines.append(s)

    def block(self, text, indent="    "):
        if text == "":
            self("%s(empty)" % indent)
            return
        for ln in text.rstrip("\n").split("\n"):
            self(indent + ln)


# ---------------------------------------------------------------------------
def classify_factory(rep, clone_real, temp_real, mk_dirs, shim_real=None):
    pre = os.path.realpath(rep["prefix"])
    epre = os.path.realpath(rep["exec_prefix"])
    bpre = os.path.realpath(rep["base_prefix"])
    bepre = os.path.realpath(rep["base_exec_prefix"])
    std = {os.path.realpath(rep["paths"][k]) for k in ("stdlib", "platstdlib")}
    zips = {os.path.realpath(p) for p in rep["sys_path_at_start"]
            if p and p.endswith(".zip")}
    cwd = rep["cwd"]
    bsp = base_site_packages(rep)
    exe = {os.path.realpath(x) for x in (rep.get("executable"),)
           if isinstance(x, str) and x}
    libdirs = {os.path.join(bpre, "lib"), os.path.join(bepre, "lib")}

    def classify(p):
        if not isinstance(p, str):
            return "fd/none", None
        a = p if os.path.isabs(p) else os.path.join(cwd, p)
        r = os.path.realpath(a)
        if under(r, clone_real):
            return "clone", os.path.relpath(r, clone_real)
        if r.startswith("/dev/"):
            return "device", r
        if shim_real and under(r, shim_real):
            return "isolation shim (this script's)", r
        if under(r, temp_real) or any(under(r, d) for d in mk_dirs):
            return "suite-temp", r
        if under(r, pre) or under(r, epre):
            return "interpreter: venv (sys.prefix)", r
        # the base environment's site-packages sits inside its stdlib
        # directory; a read there is a third-party dependency outside the
        # interpreter in use (when sys.prefix is not the base prefix), so it
        # is tested before the stdlib class and counted as outside
        if any(under(r, s) for s in bsp):
            return BASE_SP, r
        if any(under(r, s) for s in std) or r in zips:
            return "interpreter: stdlib", r
        if under(r, bpre) or under(r, bepre):
            # only a small allow-list under the base prefix is the
            # interpreter's own: its binary and the shared libraries directly
            # in <base prefix>/lib. Anything else there (another conda
            # environment under envs/, the package cache pkgs/, share/, ...)
            # is outside.
            if r in exe or (os.path.dirname(r) in libdirs and
                            SHLIB_RE.search(os.path.basename(r))):
                return BASE_ALLOW, r
            return BASE_OTHER, r
        return "OUTSIDE", r
    return classify


def base_site_packages(rep):
    """site-packages directories of the base environment that are not under
    sys.prefix/exec_prefix (empty when the interpreter is not a venv)."""
    pre = os.path.realpath(rep["prefix"])
    epre = os.path.realpath(rep["exec_prefix"])
    vi = rep.get("version_info") or [3, 12]
    cands = set()
    for k in ("stdlib", "platstdlib"):
        cands.add(os.path.realpath(os.path.join(rep["paths"][k],
                                                "site-packages")))
    for b in (rep["base_prefix"], rep["base_exec_prefix"]):
        cands.add(os.path.realpath(os.path.join(
            b, "lib", "python%d.%d" % (vi[0], vi[1]), "site-packages")))
    return sorted(c for c in cands if not under(c, pre) and not under(c, epre))


def is_write(ev, args):
    if ev != "open":
        return False
    mode = args[1] if len(args) > 1 else None
    flags = args[2] if len(args) > 2 else None
    if isinstance(flags, int):
        return bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT
                             | os.O_TRUNC | os.O_APPEND))
    if isinstance(mode, str):
        return any(c in mode for c in "wax+")
    return False


def bucket_events(rep, classify):
    """Events by (class, read/write/other); code-object filenames; execs."""
    cats = {}
    executed, code_outside, n_code = set(), set(), 0
    for e in rep["events"]:
        ev, args = e[0], e[1:]
        if ev in ("exec", "compile"):
            n_code += 1
            fn = args[0] if args else None
            if isinstance(fn, str) and os.path.isabs(fn):
                c_, r_ = classify(fn)
                if c_ == "clone":
                    executed.add(r_)
                elif c_ in OUTSIDE_CLASSES:
                    code_outside.add(r_)
            continue
        if ev in ("subprocess.Popen", "os.system", "os.exec",
                  "os.posix_spawn", "os.spawn"):
            cats.setdefault(("exec", ev), []).append(args)
            continue
        if ev == "os.chdir":
            cats.setdefault(("chdir", ev), []).append(args)
        if ev == "ctypes.dlopen":
            cats.setdefault(("dlopen", ev), []).append(args)
            if not isinstance(args[0] if args else None, str):
                continue      # dlopen(None): the process's own symbols
        p0 = args[0] if args else None
        if ev == "open" and isinstance(p0, int):
            # FileIO on an already-open descriptor (importlib writes a .pyc
            # this way after os.open on the path, recorded above)
            cats.setdefault(("fd", "write" if is_write(ev, args)
                             else "read"), []).append((ev, "fd"))
            continue
        if ev in ("os.listdir", "os.scandir") and p0 is None:
            p0 = "."
        if ev == "glob.glob":
            p0 = args[0]
        cat, rel = classify(p0)
        rw = "write" if is_write(ev, args) else (
            "read" if ev in ("open", "os.listdir", "os.scandir",
                             "glob.glob") else "other")
        cats.setdefault((cat, rw), []).append((ev, rel))
    outside = sorted({(rw, ev, rel) for (cat, rw), v in cats.items()
                      if cat in OUTSIDE_CLASSES for (ev, rel) in v} |
                     {("exec", "code", r_) for r_ in code_outside})
    return cats, executed, outside, n_code


def split_tops(rep, classify):
    third, local, nofile, stdl, odd = [], [], [], [], []
    for t, d in sorted(rep["tops"].items()):
        if d["stdlib"] or d["builtin"]:
            stdl.append(t)
            continue
        if t == "__main__":
            continue
        f = d["file"]
        if not f or not os.path.isabs(str(f)):
            nofile.append((t, f))
            continue
        cat, rel = classify(f)
        if cat == "clone":
            local.append((t, rel))
        elif cat.startswith("interpreter") or cat.startswith("isolation shim"):
            third.append((t, rel, d, cat, f))
        else:
            odd.append((t, cat, rel))
    return third, local, nofile, stdl, odd


# ---------------------------------------------------------------------------
def readme_refs(text):
    """(line, kind, raw) for every link target, inline code span, fenced
    code line and URL in a markdown text."""
    refs, fence = [], False
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            if line.strip():
                refs.append((i, "code-block", line.strip()))
            continue
        labels = set()
        for m in re.finditer(r"\[([^\]]*)\]\(([^)\s]+)\)", line):
            refs.append((i, "link", m.group(2)))
            for c in re.finditer(r"`([^`]+)`", m.group(1)):
                labels.add(c.group(1))
        for m in re.finditer(r"`([^`]+)`", line):
            kind = "code(link-label)" if m.group(1) in labels else "code"
            refs.append((i, kind, m.group(1)))
        for m in re.finditer(r"https?://[^\s)>\]`]+", line):
            refs.append((i, "url", m.group(0)))
    return refs


PATH_EXT = re.compile(r"\.(md|py|json|jsonl|npz|txt|sh|ipynb|svg|toml|cfg|"
                      r"yaml|yml|csv)$")


def add_commit(clone, h, path, env):
    """(committer date ISO, short hash) of the commit that first added path,
    in the history of h."""
    _, so, _ = sh(["git", "-C", clone, "log", "--diff-filter=A",
                   "--format=%cI %h", h, "--", path], env=env)
    rows = [x for x in so.splitlines() if x.strip()]
    if not rows:
        return None
    d, c = rows[-1].split(" ", 1)
    return d, c


def resolve_refs(refs, clone, h, tracked, tags, env):
    tracked_dirs = set()
    for f in tracked:
        parts = f.split("/")
        for k in range(1, len(parts)):
            tracked_dirs.add("/".join(parts[:k]))
    top_pkgs = {f.split("/")[0] for f in tracked if "/" in f}
    rows, problems, globinfo = [], [], {}

    def glob_tracked(pat):
        pp = pat.split("/")
        return sorted(f for f in tracked if len(f.split("/")) == len(pp) and
                      all(fnmatch.fnmatchcase(a, b)
                          for a, b in zip(f.split("/"), pp)))

    def path_status(t):
        t = t.split("#", 1)[0].split("?", 1)[0]
        if t.startswith("./"):
            t = t[2:]
        if t.startswith("/") or t.startswith("~"):
            return "OUTSIDE (absolute path)", False
        norm = os.path.normpath(t) if t else "."
        if norm.startswith(".."):
            return "OUTSIDE (leaves the repository root)", False
        if "*" in t:
            m = glob_tracked(t.rstrip("/"))
            onmach = sorted(os.path.relpath(p, REPO)
                            for p in glob.glob(os.path.join(REPO, t)))
            untr = [p for p in onmach if p not in set(m)]
            st = ("glob: %d tracked match(es) in the clone; %d further "
                  "match(es) in this machine's working tree are untracked "
                  "(absent in a clone)" % (len(m), len(untr)))
            adds = {f: add_commit(clone, h, f, env) for f in m}
            dated = sorted((v[0], f) for f, v in adds.items() if v)
            if dated:
                newest = dated[-1][1]
                st += ("; newest tracked by the commit that added it: %s "
                       "(%s, %s)" % (newest, adds[newest][1],
                                     adds[newest][0][:10]))
            if untr:
                if all(ISO_DATE.search(os.path.basename(x)) for x in untr):
                    nu = max(untr, key=lambda x: (ISO_DATE.search(
                        os.path.basename(x)).group(0), x))
                    st += ("; latest date in an untracked file's name: %s"
                           % nu)
                else:
                    st += "; untracked names carry no date (newest not stated)"
            globinfo[t] = {"tracked": m, "adds": adds, "untracked": untr}
            return st, bool(m)
        isdir = t.endswith("/")
        n = norm
        if (not isdir and n in tracked) or (n in tracked_dirs):
            kind = "directory" if n in tracked_dirs else "file"
            return "resolves in the clone (tracked %s)" % kind, True
        # not in the clone: why?
        rc, so, _ = sh(["git", "-C", clone, "check-ignore", "-v", "--no-index",
                        t], env=env)
        ign = so.strip().split("\t")[0] if rc == 0 else ""
        here = os.path.exists(os.path.join(REPO, n))
        why = []
        if here:
            why.append("present in this machine's working tree")
        if ign:
            why.append("gitignored by %s" % ign)
        elif here:
            why.append("untracked")
        return ("MISSING in a clone (%s)" % ", ".join(why or ["not found"]),
                False)

    for (ln, kind, raw) in refs:
        s = raw.strip()
        if kind == "url":
            rows.append((ln, kind, raw, "external URL (not resolved)", True))
            continue
        if kind == "link":
            st, ok = path_status(s)
            rows.append((ln, kind, raw, st, ok))
            if not ok:
                problems.append((ln, raw, st))
            continue
        if kind == "code-block":
            m = re.search(r"python\S*\s+(?:-\S+\s+)*-m\s+([\w.]+)", s)
            if m:
                mod = m.group(1)
                cand = [mod.replace(".", "/") + ".py",
                        mod.replace(".", "/") + "/__init__.py"]
                hit = [c for c in cand if c in tracked]
                st = ("module %s -> %s (tracked)" % (mod, hit[0]) if hit
                      else "module %s: NOT in the clone" % mod)
                rows.append((ln, kind, raw, st, bool(hit)))
                if not hit:
                    problems.append((ln, raw, st))
            else:
                rows.append((ln, kind, raw, "code line (no path)", True))
            continue
        # inline code span
        if re.fullmatch(r"[0-9a-f]{7,40}", s):
            rc, _, _ = sh(["git", "-C", clone, "cat-file", "-e",
                           s + "^{commit}"], env=env)
            anc = None
            if rc == 0:
                rc2, _, _ = sh(["git", "-C", clone, "merge-base",
                                "--is-ancestor", s, h], env=env)
                anc = rc2 == 0
            st = ("commit %s: %s%s" % (
                s, "present in the clone" if rc == 0 else "NOT in the clone",
                "" if anc is None else
                (", an ancestor of --ref" if anc else ", NOT an ancestor of --ref")))
            rows.append((ln, kind, raw, st, rc == 0))
            if rc != 0:
                problems.append((ln, raw, st))
            continue
        if s in tags:
            rows.append((ln, kind, raw, "tag %s: present in the clone" % s, True))
            continue
        if re.fullmatch(r"[\w.-]+-close", s):
            rows.append((ln, kind, raw, "tag-like %s: NOT in the clone" % s,
                         False))
            problems.append((ln, raw, "tag-like name not in the clone"))
            continue
        if "/" in s or "*" in s or PATH_EXT.search(s):
            st, ok = path_status(s)
            rows.append((ln, kind, raw, st, ok))
            if not ok:
                problems.append((ln, raw, st))
            continue
        if re.fullmatch(r"[A-Za-z_]\w*(\.[A-Za-z_]\w*)+", s) and \
                s.split(".")[0] in top_pkgs:
            cand = [s.replace(".", "/") + ".py",
                    s.replace(".", "/") + "/__init__.py"]
            hit = [c for c in cand if c in tracked]
            st = ("module path -> %s (tracked)" % hit[0] if hit
                  else "module path: NOT in the clone")
            rows.append((ln, kind, raw, st, bool(hit)))
            if not hit:
                problems.append((ln, raw, st))
            continue
        if re.fullmatch(r"[A-Za-z_]\w*", s):
            # git grep -E is POSIX ERE: no \s or \b
            rc, so, _ = sh(["git", "-C", clone, "grep", "-n", "-E",
                            r"^[[:space:]]*class[[:space:]]+%s([^[:alnum:]_]|$)"
                            % s, h, "--"], env=env)
            hits = [":".join(x.split(":")[1:3]) for x in so.splitlines()]
            st = "identifier, not a path; %s" % (
                ("class defined at %s" % ", ".join(hits)) if hits
                else "no 'class %s' definition found at --ref" % s)
            rows.append((ln, kind, raw, st, True))
            continue
        if kind == "code(link-label)":
            rows.append((ln, kind, raw, "link label text, not a path (the "
                         "link target on this line is checked)", True))
            continue
        rows.append((ln, kind, raw, "text (not a path)", True))
    return rows, problems, globinfo


def summ(text):
    m = [SUMMARY_RE.match(x) for x in text.splitlines()]
    m = [x for x in m if x]
    return (int(m[-1].group(1)), int(m[-1].group(2)), m[-1].group(0)) \
        if m else None


def parse_checks(stdout):
    """[(status, name, rest)] from the suite's check lines. The suite prints
    f"  [{status}] {name:<{width}} expected ..." with one width per run, so
    the name ends at the one column where every check line has ' expected '
    (the smallest such column); rest is 'expected <e> got <g>   (<source>)'.
    Returns (checks, column) or (None, reason)."""
    lines = [x for x in stdout.splitlines() if CHECK_RE.match(x)]
    if not lines:
        return None, "no check lines"
    common = None
    for x in lines:
        cols = {m.start() for m in re.finditer(r"(?= expected )", x)}
        common = cols if common is None else common & cols
    if not common:
        return None, "no common ' expected ' column"
    col = min(common)
    out = []
    for x in lines:
        st = CHECK_RE.match(x).group(1)
        out.append((st, x[9:col].rstrip(), x[col + 1:]))
    return out, col


# ---------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ref", default=PIN_FULL,
                    help="commit-ish to check out in the clone (default: the "
                         "block's commit %s; pass --ref <tag> once the PI "
                         "cuts the release tag)" % PIN)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--workroot", default=None,
                    help="scratch directory the clone, TMPDIR, shim and hook "
                         "reports are made under (default: the N11 scratch "
                         "when --out is the default, else <dir of --out>/"
                         "N11-work); refused inside the repository")
    ap.add_argument("--source", default="file://" + REPO,
                    help="what to clone (default: this repository via "
                         "file://, with --no-local); the release re-run can "
                         "pass the published remote's URL")
    ap.add_argument("--sitecheck", default=SITECHECK,
                    help="committed site-check raw (read at --ref) whose "
                         "suite count conjunct (e) compares against")
    ap.add_argument("--python", default=DEFAULT_PY,
                    help="interpreter the suite runs under")
    ap.add_argument("--keep", action="store_true",
                    help="keep the clone (debugging only)")
    a = ap.parse_args(argv)

    if not a.out:
        sys.exit("refusing: --out must be a file path")
    out_real = os.path.realpath(a.out)
    if os.path.isdir(out_real):
        sys.exit("refusing: --out must be a file path")
    if a.workroot is None:
        a.workroot = SCRATCH if out_real == os.path.realpath(DEFAULT_OUT) \
            else os.path.join(os.path.dirname(out_real), "N11-work")
    wr_real = os.path.realpath(a.workroot)      # checked before anything is made
    if under(wr_real, os.path.realpath(REPO)):
        sys.exit("refusing: --workroot %s is inside the repository" % wr_real)
    os.makedirs(wr_real, exist_ok=True)
    o = Out()

    # ---- header -----------------------------------------------------------
    stamp = subprocess.run(["date", "-u"], capture_output=True,
                           text=True).stdout.strip()
    _, head, _ = sh(["git", "-C", REPO, "rev-parse", "HEAD"])
    head = head.strip()
    rc, h, err = sh(["git", "-C", REPO, "rev-parse", "--verify",
                     a.ref + "^{commit}"])
    if rc != 0:
        sys.exit("cannot resolve --ref %r: %s" % (a.ref, err.strip()))
    h = h.strip()
    h12, h7 = h[:12], h[:7]
    _, subj, _ = sh(["git", "-C", REPO, "log", "-1", "--format=%s", h])
    blk_wt = sha256_file(os.path.join(REPO, BLOCK))
    p = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (PIN, BLOCK)],
                       capture_output=True)
    blk_pin = hashlib.sha256(p.stdout).hexdigest() if p.returncode == 0 else None
    script = os.path.abspath(__file__)
    rc, pyver, _ = sh([a.python, "-E", "-s", "-c",
                       "import sys; print(sys.version)"])
    cmdline = shlex.join([sys.executable] + sys.argv)

    o("# AUDIT-note-release v1.2 -- N11 fresh-clone smoke test")
    o()
    o("- Code stamp: %s (date -u)" % stamp)
    o("- HEAD (source repository, at run time): %s" % head)
    o("- --ref: %r -> %s (%s)" % (a.ref, h, subj.strip()))
    o("- Clone source: %s" % a.source)
    o("- Work root (scratch; the two clones, their TMPDIRs, the empty HOME, "
      "the numpy shim and the hook reports are made here and deleted at the "
      "end; written <workroot> below): %s" % wr_real)
    o("- Block: %s, sha256 %s (working tree) / %s (at %s); expected %s: %s"
      % (BLOCK, blk_wt, blk_pin, PIN, BLOCK_SHA,
         "MATCH" if blk_wt == BLOCK_SHA == blk_pin else "MISMATCH"))
    o("- Script: scripts/audit_note_N11.py, sha256 %s" % sha256_file(script))
    o("- Interpreter (this script): %s (Python %s)"
      % (sys.executable, sys.version.split()[0]))
    o("- Interpreter (the suite): %s (Python %s)" % (a.python,
                                                   pyver.strip().split()[0]))
    o("- Command: %s" % cmdline)
    o("- Regeneration: with the same script, --ref commit, --source, "
      "--sitecheck and interpreter, a re-run reproduces this raw "
      "byte-for-byte except (i) the header lines 'Code stamp', 'HEAD (source "
      "repository, at run time)' (moves whenever anyone commits), '--ref' "
      "(it echoes the argument as typed), 'Work root' and 'Command'; (ii) "
      "the line in (1) naming the branch the clone checked out before the "
      "detach (it prints the source's branch tip at clone time); (iii) "
      "lines that report this machine's state, each labelled "
      "as such: the laptop's filter definitions, per-user git files and "
      "system gitattributes lines in (1), the PYTHON* variable names and the user-site line of run (d) in "
      "(2), untracked glob matches and present-but-not-tracked paths in "
      "(3), the note's presence in (3), and the working-tree existence "
      "column of conjunct (e). Everything else is a function of the --ref "
      "tree (and, in (2e), of the lineage commit's tree), the interpreter "
      "and the suite.")
    o()
    o("Scope: N11 of the block (:64-70). Read-only on the record: the "
      "source repository is only read (rev-parse, log, show, blame, clone's "
      "upload side). Every git command that touches a clone runs with "
      "GIT_CONFIG_GLOBAL=/dev/null, GIT_CONFIG_NOSYSTEM=1, "
      "GIT_ATTR_NOSYSTEM=1, GIT_TERMINAL_PROMPT=0, LC_ALL=C, HOME and "
      "XDG_CONFIG_HOME both set to an empty scratch directory "
      "(<workroot>/empty-home-<sha12>), and no other GIT_* variables -- "
      "except the two check-attr measurements in (1), labelled there, which "
      "drop GIT_ATTR_NOSYSTEM to show what it turns off. The two "
      "config-origin queries that locate the system attributes file run in "
      "the empty directory, not in a clone, with the system config allowed "
      "and GIT_CEILING_DIRECTORIES set to its parent.")
    o()
    n_header = len(o.lines)

    # ---- (1) clone + checkout --------------------------------------------
    clone = os.path.join(wr_real, "clone-%s" % h12)
    tmpd = os.path.join(wr_real, "tmp-%s" % h12)
    shim = os.path.join(wr_real, "numpy-shim-%s" % h12)
    report = os.path.join(wr_real, "hook-report-%s.json" % h12)
    report_iso = os.path.join(wr_real, "iso-report-%s.json" % h12)
    home = os.path.join(wr_real, "empty-home-%s" % h12)
    lclone = os.path.join(wr_real, "lineage-clone-%s" % h12)
    ltmp = os.path.join(wr_real, "lineage-tmp-%s" % h12)
    for pth in (clone, tmpd, shim, home, lclone, ltmp):
        if os.path.lexists(pth):
            print("removing stale scratch %s" % pth, file=sys.stderr)
            rmtree_force(pth)
    for pth in (report, report_iso):
        if os.path.exists(pth):
            os.remove(pth)
    os.makedirs(tmpd)
    os.makedirs(home)
    os.makedirs(ltmp)
    genv = git_env(home)

    o("## (1) Clone and detached checkout without the laptop's git config")
    o()
    o("Clone directory (scratch, deleted at the end): %s" % clone)
    o()
    laptop = []
    for label, path in (("source .git/config", os.path.join(REPO, ".git/config")),
                        ("~/.gitconfig", os.path.expanduser("~/.gitconfig")),
                        ("~/.config/git/config",
                         os.path.expanduser("~/.config/git/config"))):
        if os.path.exists(path):
            for sec, k, v in filter_sections(open(path).read()):
                laptop.append("%s: filter.%s.%s = %s" % (label, sec, k, v))
    o("The laptop's filter definitions (this machine's config files, read "
      "as text; these are what the clone must do without):")
    o.block("\n".join(laptop) if laptop else "none found")
    pu = peruser_git_files()
    o("This machine's per-user git files that git reads by default (presence "
      "and non-comment line count only; contents not shown). Under the "
      "environment above none of them applies: GIT_CONFIG_GLOBAL=/dev/null "
      "replaces the first two, and HOME = XDG_CONFIG_HOME = the empty "
      "directory moves the default excludes and attributes files to paths "
      "that do not exist:")
    for label, _p, ex, n in pu:
        o("    %s: %s" % (label, ("present, %s non-comment line(s)" % n)
                          if ex else "absent"))
    o()
    steps = []
    cmd = ["git", "clone", "--no-local", a.source, clone]
    rc, so, se = sh(cmd, env=genv)
    steps.append(("clone", cmd, rc, so, se))
    if rc == 0:
        rcb, cb, _ = sh(["git", "-C", clone, "rev-parse", "HEAD"], env=genv)
        rcs, sb, _ = sh(["git", "-C", clone, "symbolic-ref", "-q", "HEAD"],
                        env=genv)
        cmd = ["git", "-C", clone, "checkout", "--detach", h]
        rc2, so2, se2 = sh(cmd, env=genv)
        steps.append(("checkout", cmd, rc2, so2, se2))
    else:
        cb, sb, rc2 = "", "", 1
    def no_meter(text):
        return "\n".join(x for x in text.splitlines()
                         if not PROGRESS_RE.match(x))
    o("(git's progress-meter lines, e.g. 'Updating files:  NN% (k/n)', are "
      "left out of the stdout/stderr shown below: git prints them only when "
      "a step outlasts its progress delay, so whether they appear varies by "
      "run. The warning/error scan further down reads the full output, "
      "meter lines included.)")
    o()
    for name, cmd, rc_, so_, se_ in steps:
        disp = [("<clone>" if x == clone else x) for x in cmd]
        o("$ %s" % shlex.join(disp))
        o("  exit status: %d" % rc_)
        o("  stdout:")
        o.block(no_meter(so_))
        o("  stderr:")
        o.block(no_meter(se_))
        o()
    warn_lines = [ln for _, _, _, so_, se_ in steps
                  for ln in (so_ + se_).splitlines()
                  if re.search(r"warning|error|fatal", ln, re.I)]
    if rc == 0:
        o("Branch the clone checked out before the detach: %s at %s"
          % (sb.strip() or "(detached)", cb.strip()))
    rc3, head_c, _ = sh(["git", "-C", clone, "rev-parse", "HEAD"], env=genv)
    head_c = head_c.strip()
    o("Clone HEAD after the checkout: %s (%s --ref)" %
      (head_c, "equals" if head_c == h else "DIFFERS FROM"))
    _, por, por_e = sh(["git", "-C", clone, "status", "--porcelain=v1",
                        "--untracked-files=all"], env=genv)
    _, pig, _ = sh(["git", "-C", clone, "status", "--porcelain=v1",
                    "--untracked-files=all", "--ignored"], env=genv)
    o("$ git -C <clone> status --porcelain=v1 --untracked-files=all  "
      "(after the checkout, before any run)")
    o.block(por)
    if por_e.strip():
        o("  stderr:")
        o.block(por_e)
    o("  with --ignored: %d line(s)" % len([x for x in pig.splitlines() if x]))
    clean_after_checkout = (por.strip() == "" and por_e.strip() == "")
    o()
    clone_cfg = open(os.path.join(clone, ".git/config")).read() \
        if os.path.exists(os.path.join(clone, ".git/config")) else ""
    o("The clone's own .git/config (written by git clone):")
    o.block(clone_cfg.replace(REPO, "<source>"))
    _, cl_so, cl_se = sh(["git", "-C", clone, "config", "--list",
                          "--show-origin"], env=genv)
    origins = sorted({x.split("\t", 1)[0] for x in cl_so.splitlines()
                      if "\t" in x})
    o("$ git -C <clone> config --list --show-origin  (under the environment "
      "above): %d setting(s), from: %s%s"
      % (len([x for x in cl_so.splitlines() if x.strip()]), origins,
         ("; stderr %r" % cl_se.strip()) if cl_se.strip() else ""))
    exc_p = os.path.join(clone, ".git", "info", "exclude")
    exc_n = sum(1 for x in open(exc_p).read().splitlines()
                if x.strip() and not x.strip().startswith("#")) \
        if os.path.isfile(exc_p) else None
    attr_p = os.path.join(clone, ".git", "info", "attributes")
    hooks_d = os.path.join(clone, ".git", "hooks")
    hooks_live = sorted(x for x in (os.listdir(hooks_d)
                                    if os.path.isdir(hooks_d) else [])
                        if not x.endswith(".sample"))
    o("The clone's .git/info/exclude: %s; .git/info/attributes: %s; "
      "hooks other than git's *.sample templates: %d %s"
      % ("absent" if exc_n is None else
         "%d non-comment line(s)" % exc_n,
         "present" if os.path.exists(attr_p) else "absent",
         len(hooks_live), hooks_live or ""))
    sar = system_attr_report(clone, genv, home)
    o("(this machine) The system gitattributes file of the git in use "
      "(GIT_CONFIG_NOSYSTEM does not turn it off; GIT_ATTR_NOSYSTEM=1 does). "
      "Candidates, the 'gitattributes' beside each system-level config file "
      "git names (presence and non-comment line count only):")
    for p_, ex_, n_ in sar["cands"]:
        o("    %s: %s" % (p_, ("present, %d non-comment line(s)" % n_)
                          if ex_ else "absent"))
    if not sar["cands"]:
        o("    none located")
    o("  probe: %d name(s) built from the present file(s)' '*.<ext>' "
      "patterns (n11-probe.<ext>), through git -C <clone> check-attr -a: "
      "with an attribute when GIT_ATTR_NOSYSTEM is absent %d; under the "
      "environment above (GIT_ATTR_NOSYSTEM=1) %d"
      % (sar["n_probes"], sar["probe_on"], sar["probe_off"]))
    o("  tracked paths at --ref (git ls-files, %d) through git -C <clone> "
      "check-attr --stdin -z -a: with any attribute %d when "
      "GIT_ATTR_NOSYSTEM is absent, %d under the environment above (exit "
      "%d / %d); paths whose attributes the system file changes: %d %s"
      % (sar["n_tracked"], sar["n_with_attr"][0], sar["n_with_attr"][1],
         sar["rc"][0], sar["rc"][1], len(sar["changed"]),
         sar["changed"] or ""))
    git_inputs_clean = bool(origins == ["file:.git/config"] and
                            exc_n in (0, None) and
                            not os.path.exists(attr_p) and not hooks_live and
                            genv.get("GIT_ATTR_NOSYSTEM") == "1" and
                            sar["probe_off"] == 0)
    o("So the git inputs in effect on the clone are its .git/config (above) "
      "and the repository's own .gitattributes and .gitignore files; no "
      "per-user or system file applies: the system config is off by "
      "GIT_CONFIG_NOSYSTEM=1, the system attributes file by "
      "GIT_ATTR_NOSYSTEM=1%s, and the per-user files by the empty HOME."
      % (" (the probe above shows the file read without the variable and "
         "not with it)" if sar["probe_on"] else "")
      if git_inputs_clean else
      "NOT only the clone's .git/config and the repository's own files: see "
      "the origins, exclude, attributes, system attributes file and hooks "
      "above.")
    fs = filter_sections(clone_cfg)
    o("filter.* definitions in effect in the clone: %s"
      % ("none" if not fs else fs))
    o()
    _, ga, _ = sh(["git", "-C", clone, "show", "%s:.gitattributes" % h],
                  env=genv)
    o(".gitattributes at --ref:")
    o.block(ga)
    _, nbs, _ = sh(["git", "-C", clone, "ls-files", "--", "*.ipynb"], env=genv)
    nbs = [x for x in nbs.splitlines() if x]
    o("Tracked *.ipynb at --ref: %d %s" % (len(nbs), nbs))
    nb_ok = True
    for nb in nbs:
        _, att, _ = sh(["git", "-C", clone, "check-attr", "filter", "--", nb],
                       env=genv)
        _, want, _ = sh(["git", "-C", clone, "rev-parse", "%s:%s" % (h, nb)],
                        env=genv)
        rch, got, gerr = sh(["git", "-C", clone, "hash-object",
                             "--path=%s" % nb, nb], cwd=clone, env=genv)
        same = got.strip() == want.strip()
        nb_ok = nb_ok and same and rch == 0 and not gerr.strip()
        o("  %s" % att.strip())
        o("  committed blob %s; working-tree file hashed through its "
          "attributes (git hash-object --path, no -w, so no object is "
          "written): %s, exit %d, stderr %r -> %s"
          % (want.strip(), got.strip(), rch, gerr.strip(),
             "identical" if same else "DIFFERENT"))
    o()
    o("Warnings/errors in clone or checkout output: %d" % len(warn_lines))
    for ln in warn_lines:
        o("  %s" % ln)
    readme_fix = bool(warn_lines or not clean_after_checkout or not nb_ok)
    if not readme_fix:
        o("Outcome (1): clone and checkout succeed with no warning; the tree "
          "is clean; the 'filter=nbstripout' attribute names a driver the "
          "clone does not define, and git treats it as no filter (the "
          "notebook hashes to its committed blob). The README needs no "
          "warning and no fix for a reader. (The laptop's "
          "filter.nbstripout.required=true lives in its local .git/config, "
          "which a clone does not receive.)")
    else:
        o("Outcome (1): NOT clean -- see above. Per the block (:68) this is "
          "a README item, not a STOP: the README says so and gives the "
          "one-line fix for a reader, e.g. "
          "git config filter.nbstripout.clean cat && "
          "git config filter.nbstripout.smudge cat")
    o()

    # ---- (2) the suite ------------------------------------------------------
    o("## (2) The regression suite from the clone's root")
    o()
    penv = dict(os.environ)
    penv["TMPDIR"] = tmpd
    plain_cmd = [a.python, "-E", "-s", "-m", SUITE_MOD]
    hook_cmd = [a.python, "-E", "-s", "-c", WRAPPER, report, "hooked"]
    rch_, hso, hse = sh(hook_cmd, cwd=clone, env=penv)
    rcp, pso, pse = sh(plain_cmd, cwd=clone, env=penv)
    rep = json.load(open(report)) if os.path.exists(report) else None
    purelib = rep["paths"]["purelib"] if rep else None
    iso_ok, rep_iso, rci, iso_so, iso_se = False, None, None, "", ""
    if purelib and os.path.isdir(os.path.join(purelib, "numpy")):
        os.makedirs(shim)
        os.symlink(os.path.join(purelib, "numpy"), os.path.join(shim, "numpy"))
        iso_cmd = [a.python, "-S", "-E", "-s", "-c", WRAPPER, report_iso,
                   "isolated", shim, purelib]
        rci, iso_so, iso_se = sh(iso_cmd, cwd=clone, env=penv)
        rep_iso = json.load(open(report_iso)) \
            if os.path.exists(report_iso) else None
    # (d) the README's literal command (README.md:55, block :68): no flags,
    # so PYTHON* variables and the user site apply as they would for a reader
    lit_cmd = [a.python, "-m", SUITE_MOD]
    rcl, lso, lse = sh(lit_cmd, cwd=clone, env=penv)
    probe_src = ("import json, os, site, sys; print(json.dumps({"
                 "'ignore_environment': sys.flags.ignore_environment, "
                 "'no_user_site': sys.flags.no_user_site, "
                 "'enable_user_site': bool(site.ENABLE_USER_SITE), "
                 "'user_site': site.getusersitepackages(), "
                 "'user_site_isdir': os.path.isdir(site.getusersitepackages()), "
                 "'dont_write_bytecode': sys.dont_write_bytecode, "
                 "'path': sys.path}))")
    _, lprobe_so, _ = sh([a.python, "-c", probe_src], cwd=clone, env=penv)
    try:
        lprobe = json.loads(lprobe_so)
    except ValueError:
        lprobe = None
    py_env_names = sorted(k for k in os.environ if k.startswith("PYTHON"))

    sp, sh_ = summ(pso), summ(hso)
    si = summ(iso_so)
    npass = sum(1 for x in pso.splitlines() if x.strip().startswith("[PASS]"))
    nfail = sum(1 for x in pso.splitlines() if x.strip().startswith("[FAIL]"))
    o("Run order: (a) the hooked run first (fresh tree, no __pycache__), "
      "then (b) the plain run (the README's command plus -E -s), then (c) the "
      "isolated run (-S -E -s; sys.path = the clone root, the stdlib entries "
      "and a shim directory holding one symlink, numpy -> the interpreter's "
      "site-packages/numpy), then (d) the README's literal command with no "
      "flags. All with cwd = the clone root and the environment inherited "
      "with TMPDIR=%s (scratch, outside the clone); in (a)-(c) -E makes "
      "Python ignore PYTHON* variables and -s turns the user site off, in "
      "(d) both apply as they would for a reader." % tmpd)
    o()
    o("(b) Plain run: $ %s   [cwd = <clone>]" % shlex.join(
        [a.python, "-E", "-s", "-m", SUITE_MOD]))
    o("  exit status: %d" % rcp)
    o("  summary line: %r" % (sp[2] if sp else None))
    o("  lines starting [PASS]: %d; [FAIL]: %d" % (npass, nfail))
    o("(a) Hooked run: $ %s -E -s -c <WRAPPER (this script's WRAPPER "
      "constant)> <report json> hooked   [cwd = <clone>]" % a.python)
    o("  exit status: %d (wrapper's recorded exit: %s)"
      % (rch_, rep["exit"] if rep else None))
    o("  summary line: %r" % (sh_[2] if sh_ else None))
    o("  stdout byte-identical to the plain run: %s" %
      ("yes" if hso == pso else "NO"))
    o("  stderr (plain run): %r; stderr (hooked run): %r"
      % (pse if len(pse) < 2000 else pse[:2000] + "...",
         hse if len(hse) < 2000 else hse[:2000] + "..."))
    sl = summ(lso)
    suite_ok = bool(sp and sh_ and sp[0] == sp[1] and sp[1] > 0 and
                    sh_[0] == sh_[1] and rcp == 0 and rch_ == 0 and nfail == 0
                    and hso == pso and rcl == 0 and sl == sp and lso == pso)
    o()
    outside, cats, executed = [], {}, set()
    clone_real = os.path.realpath(clone)
    temp_real = os.path.realpath(tmpd)
    shim_real = os.path.realpath(shim)
    tracked = set()
    clone_reads, data_reads, py_scanned = [], [], []
    untr_read = ["(no hook report)"]
    mk_dirs = set()
    classify = None
    skips, out_v, cout_v, third = [], set(), set(), []
    n_bo = n_ba = None
    bo_paths, ba_paths = [], []

    def tnorm(pth):                 # replaced below once mk_dirs is known
        return pth
    if rep:
        o("Python: %s" % rep["version"].replace("\n", " "))
        o("sys.executable %s; sys.prefix %s; sys.base_prefix %s"
          % (rep["executable"], rep["prefix"], rep["base_prefix"]))
        o("sys.flags (hooked run): ignore_environment=%d no_user_site=%d "
          "no_site=%d isolated=%d"
          % (rep["flags"]["ignore_environment"], rep["flags"]["no_user_site"],
             rep["flags"]["no_site"], rep["flags"]["isolated"]))
        o("sys.path when the suite started (hooked run; <clone> = the clone "
          "root):")
        for pth in rep["sys_path_at_start"]:
            o("    %s" % (pth.replace(clone, "<clone>") if pth else "''"))
        # .pth files in the interpreter's site-packages
        pths = sorted(glob.glob(os.path.join(purelib, "*.pth")))
        o("*.pth files in the interpreter's site-packages (%s): %d"
          % (purelib, len(pths)))
        for pf in pths:
            st_ = os.stat(pf)
            hidden = bool(getattr(st_, "st_flags", 0) &
                          getattr(stat, "UF_HIDDEN", 0))
            body = open(pf).read().strip().replace("\n", " | ")
            entries = [x.strip() for x in open(pf).read().splitlines()
                       if x.strip() and not x.startswith(("#", "import"))]
            onpath = [e for e in entries if e in rep["sys_path_at_start"]]
            o("    %s: macOS hidden flag %s; content %r; path entries on "
              "sys.path: %s" % (os.path.basename(pf),
                                "SET" if hidden else "not set", body,
                                onpath or "none"))
        _, _, vse = sh([a.python, "-E", "-s", "-v", "-c", "pass"], cwd=clone,
                       env=penv)
        skips = [x.strip() for x in vse.splitlines()
                 if "pth" in x.lower() and "skip" in x.lower()]
        o("  site's own report ($ %s -E -s -v -c pass, lines mentioning "
          "skipped .pth files): %d" % (a.python, len(skips)))
        for x in skips:
            o("    %s" % x)
        o("  (A .pth path entry that site processed would appear on sys.path "
          "above. The editable .pth names the jlens-qwen36/ clone root, "
          "outside the venv; on an interpreter where that .pth is processed "
          "the root would be appended to sys.path. This run's evidence on "
          "whether the suite reads from it is the hook's OUTSIDE count "
          "below.)")
        o()
        # events
        for e in rep["events"]:
            if e[0] in ("tempfile.mkdtemp", "os.mkdir") and isinstance(e[1], str):
                mk_dirs.add(os.path.realpath(e[1]))
        mk_dirs = {d for d in mk_dirs if not under(d, clone_real)}
        classify = classify_factory(rep, clone_real, temp_real, mk_dirs)
        cats, executed, outside, n_code = bucket_events(rep, classify)
        o("Audit-hook events recorded (hooked run): %d (the hook is installed "
          "before the suite module or any of its imports is loaded; opens "
          "during interpreter startup -- site, encodings, pyvenv.cfg -- "
          "precede it and are not recorded)." % len(rep["events"]))
        o("By class (class, read/write/other): events, distinct paths")
        for key in sorted(cats, key=lambda k: (k[0], k[1])):
            v = cats[key]
            if key[0] in ("exec", "chdir", "dlopen"):
                o("    %-36s %-6s %5d  %s" % (key[0], "", len(v), ", ".join(
                    sorted({"%s(%s)" % (key[1], ", ".join(map(repr, x)))
                            for x in v}))))
                continue
            o("    %-36s %-6s %5d  %5d" % (key[0], key[1], len(v),
                                           len({x[1] for x in v})))
        o("    %-36s %-6s %5d  (audit 'exec'/'compile' events: code objects "
          "run or compiled; filenames only)" % ("code", "", n_code))
        n_bsp = sum(len(v) for (cat, _rw), v in cats.items() if cat == BASE_SP)
        o("  Class '%s' = %s (the base environment's site-packages, which "
          "sits inside the stdlib directory above; tested before the stdlib "
          "class, and counted as outside the clone by conjunct (d)): %d "
          "event(s); code objects with a filename there are in the OUTSIDE "
          "list below." % (BASE_SP, base_site_packages(rep) or "none (not a "
                           "venv)", n_bsp))
        n_bo = sum(len(v) for (cat, _rw), v in cats.items()
                   if cat == BASE_OTHER)
        n_ba = sum(len(v) for (cat, _rw), v in cats.items()
                   if cat == BASE_ALLOW)
        bo_paths = sorted({rel for (cat, _rw), v in cats.items()
                           if cat == BASE_OTHER for (_e, rel) in v})
        ba_paths = sorted({rel for (cat, _rw), v in cats.items()
                           if cat == BASE_ALLOW for (_e, rel) in v})
        o("  Class '%s' = anything under the base prefix %s that is not its "
          "stdlib, the base environment's site-packages or the allow-list "
          "(for example another conda environment under envs/ or the "
          "package cache pkgs/); counted as outside the clone by conjunct "
          "(d): %d event(s)%s; code objects with a filename there are in "
          "the OUTSIDE list below."
          % (BASE_OTHER, rep["base_prefix"], n_bo,
             (" %s" % bo_paths) if bo_paths else ""))
        o("  Class '%s' = the allow-list under the base prefix, the "
          "interpreter's own files: its binary (%s, the realpath of "
          "sys.executable) and the shared libraries directly in %s "
          "(*.dylib, *.so*): %d event(s)%s"
          % (BASE_ALLOW, os.path.realpath(rep["executable"]),
             os.path.join(rep["base_prefix"], "lib"), n_ba,
             (" %s" % ba_paths) if ba_paths else ""))
        o()
        o("OUTSIDE, with classes '%s' and '%s' (not the clone, not the "
          "interpreter's installation, not a temp file the suite created, not "
          "a device): %d distinct path(s)"
          % (BASE_SP, BASE_OTHER, len({x[2] for x in outside})))
        for rw, ev, rel in outside:
            flag = "  <- under jlens-qwen36/ (outside its .venv)" if \
                "/jlens-qwen36/" in rel and "/jlens-qwen36/.venv" not in rel \
                else ""
            o("    %s %s %s%s" % (rw, ev, rel, flag))
        jl = os.path.realpath(os.path.join(REPO, "jlens-qwen36"))
        jlv = os.path.join(jl, ".venv")
        in_v, out_v, cin_v, cout_v = set(), set(), set(), set()
        for e in rep["events"]:
            if len(e) > 1 and isinstance(e[1], str):
                if e[0] in ("exec", "compile") and not os.path.isabs(e[1]):
                    continue                  # '<string>', '<frozen ...>'
                r_ = os.path.realpath(e[1] if os.path.isabs(e[1])
                                      else os.path.join(rep["cwd"], e[1]))
                code_ = e[0] in ("exec", "compile")
                if under(r_, jlv):
                    (cin_v if code_ else in_v).add(r_)
                elif under(r_, jl):
                    (cout_v if code_ else out_v).add(r_)
        o("Paths under %s in file events (open/listdir/scandir/mkdir...): "
          "inside its .venv (the interpreter's own installation) %d distinct; "
          "outside its .venv %d distinct %s" % (jl, len(in_v), len(out_v),
                                                sorted(out_v) or ""))
        o("Code objects run or compiled with a filename under it: inside "
          "its .venv %d distinct files; outside its .venv %d %s"
          % (len(cin_v), len(cout_v), sorted(cout_v) or ""))
        execs = [x for k, v in cats.items() if k[0] == "exec" for x in v]
        o("Subprocess/exec events: %d %s" % (len(execs), execs or ""))
        chd = [x for k, v in cats.items() if k[0] == "chdir" for x in v]
        o("chdir events: %d %s" % (len(chd), chd or ""))
        # temp: names under TMPDIR are random (tempfile's writability probe,
        # mkdtemp); shown by role, so the raw is deterministic
        tmp_ev = [(rw, ev, rel) for (cat, rw), v in cats.items()
                  if cat == "suite-temp" for (ev, rel) in v]

        def tnorm(pth):
            r = os.path.relpath(pth, temp_real).split(os.sep)
            first = os.path.join(temp_real, r[0])
            r[0] = "<mkdtemp>" if first in mk_dirs else "<random>"
            return "$TMPDIR/" + "/".join(r)
        tnames = sorted({"%s %s %s" % (rw, ev, tnorm(rel))
                         for rw, ev, rel in tmp_ev})
        n_rm_mk = sum(1 for (cat, rw), v in cats.items()
                      if cat == "suite-temp" for (ev, rel) in v
                      if ev in ("os.rmdir", "shutil.rmtree")
                      and os.path.realpath(rel) in mk_dirs)
        o("Suite-created temp paths (hooked run; all under this run's TMPDIR; "
          "random names shown as <mkdtemp> for a tempfile.mkdtemp directory "
          "and <random> otherwise -- tempfile's own writability probe): %d "
          "event(s)" % len(tmp_ev))
        for x in tnames:
            o("    %s" % x)
        o("  rmdir/rmtree events on a suite-created mkdtemp directory: %d"
          % n_rm_mk)
        # clone reads, split by how the file was used
        clone_reads = sorted({rel for (cat, rw), v in cats.items()
                              if cat == "clone" and rw == "read"
                              for (ev, rel) in v if ev == "open"})
        clone_writes = sorted({rel for (cat, rw), v in cats.items()
                               if cat == "clone" and rw == "write"
                               for (_, rel) in v})
        clone_lists = sorted({rel for (cat, rw), v in cats.items()
                              if cat == "clone" and rw == "read"
                              for (ev, rel) in v if ev != "open"})
        imported_clone = set()
        for _n, f in rep.get("module_files", []):
            c_, r_ = classify(f)
            if c_ == "clone":
                imported_clone.add(r_)
        data_reads = [x for x in clone_reads if x.startswith("data/")]
        py_reads = [x for x in clone_reads if x.endswith(".py")]
        py_imported = [x for x in py_reads if x in executed]
        py_scanned = [x for x in py_reads if x not in executed]
        mod_not_exec = sorted(x for x in imported_clone
                              if x.endswith(".py") and x not in executed)
        exec_not_mod = sorted(x for x in executed if x not in imported_clone)
        pyc_reads = [x for x in clone_reads if "__pycache__/" in x]
        other_reads = [x for x in clone_reads if x not in data_reads and
                       x not in py_reads and x not in pyc_reads]
        o()
        o("Files inside the clone the suite opened for reading (hooked run): "
          "%d" % len(clone_reads))
        o("  data/ (%d):" % len(data_reads))
        for x in data_reads:
            o("    %s" % x)
        o("  .py files executed as code (a code object with that filename "
          "was compiled or run: audit 'compile'/'exec' events; %d): %s"
          % (len(py_imported), " ".join(py_imported)))
        o("    cross-check against sys.modules at exit: clone modules not "
          "seen executing: %d %s; executed files with no sys.modules entry "
          "at exit (possible reasons: run as __main__ by runpy; loaded by "
          "spec_from_file_location without registration; an import that "
          "raised, which removes the module -- the suite's quarantine check "
          "requires importing valence_core.e2b.statepresent to raise "
          "ImportError): %d %s"
          % (len(mod_not_exec), mod_not_exec or "", len(exec_not_mod),
             exec_not_mod or ""))
        o("  .py files opened but never executed -- read as text by the "
          "suite's structural source scans (%d): %s"
          % (len(py_scanned), " ".join(py_scanned)))
        o("  __pycache__ reads (%d; bytecode the hooked run itself wrote); "
          "other (%d): %s" % (len(pyc_reads), len(other_reads),
                              " ".join(other_reads)))
        o("  directories listed (os.listdir/os.scandir) inside the clone: %d"
          % len(clone_lists))
        nonpyc_w = [x for x in clone_writes if "__pycache__/" not in x]
        o("Files inside the clone the suite opened for writing: %d, of which "
          "outside __pycache__/: %d %s" % (len(clone_writes), len(nonpyc_w),
                                           nonpyc_w or ""))
        _, trk, _ = sh(["git", "-C", clone, "ls-files"], env=genv)
        tracked = set(x for x in trk.splitlines() if x)
        untr_read = [x for x in clone_reads if x not in tracked and
                     "__pycache__/" not in x]
        o("Clone files read that are not tracked at --ref (excluding "
          "__pycache__): %d %s" % (len(untr_read), untr_read or ""))
        o()
        # imports
        third, local, nofile, stdl, odd = split_tops(rep, classify)
        o("Imported top-level modules not in sys.stdlib_module_names (hooked "
          "run; %d modules in sys.modules at exit; %d stdlib/builtin "
          "top-level names, not listed):" % (rep["n_modules"], len(stdl)))
        o("  third-party, from the interpreter's installation (the only "
          "non-stdlib packages the suite imported; sufficiency is tested by "
          "the isolated run (c) below):")
        for t, rel, d, _c, _f in third:
            dv = ", ".join("%s %s" % (x[0], x[1]) for x in d["dists"]) or "-"
            o("    %s  __version__=%s  distribution(s): %s  file: %s"
              % (t, d["module_version"], dv, rel))
        o("  from the clone (%d): %s" % (len(local), ", ".join(
            "%s (%s)" % (t, r) for t, r in local)))
        pre_ns = sorted(t for t, d in rep["tops"].items() if d.get("preloaded")
                        and not (d["stdlib"] or d["builtin"])
                        and t != "__main__")
        o("  non-stdlib top-level modules already loaded at interpreter "
          "startup, before the hook was installed: %d %s"
          % (len(pre_ns), pre_ns or ""))
        o("  no __file__ and no spec origin (%d): %s" % (len(nofile), nofile))
        o("  from anywhere else (%d): %s" % (len(odd), odd))
        if odd:
            outside += [("import", t, rel) for t, cat, rel in odd]
        ext = {}
        for n_, f in rep.get("module_files", []):
            if f.endswith((".so", ".dylib", ".pyd")):
                c_, r_ = classify(f)
                key = (c_, n_.split(".")[0])
                ext[key] = ext.get(key, 0) + 1
        o("  compiled extension modules loaded (by class and top-level "
          "package): %s" % (", ".join("%s %s: %d" % (k[0], k[1], v)
                                      for k, v in sorted(ext.items()))
                            or "none"))
        if any(t.startswith(("_cython", "cython")) for t, _ in nofile):
            o("  (The no-file names are module objects that compiled "
              "extensions register at import time: '_cython_*'/"
              "'cython_runtime' are the names Cython-generated extensions "
              "use. They are not packages a reader installs.)")
    else:
        o("NO hook report was written (the hooked run did not finish).")
    o()

    # ---- (2c) isolated run --------------------------------------------------
    o("(c) Isolated run: $ %s -S -E -s -c <WRAPPER> <report json> isolated "
      "<workroot>/numpy-shim-%s %s   [cwd = <clone>]" % (a.python, h12,
                                                        purelib))
    iso_out, iso_reach, iso_ns_extra = [], [], []
    iso_bo = iso_ba = None
    if rep_iso:
        # the isolated run's own mkdtemp dirs are suite temp too
        mk_i = {os.path.realpath(e[1]) for e in rep_iso["events"]
                if e[0] in ("tempfile.mkdtemp", "os.mkdir")
                and isinstance(e[1], str)}
        mk_i = {d for d in mk_i if not under(d, clone_real)}
        # Under -S, site.py never runs, so sys.prefix in this run is the
        # base prefix, not the venv: the interpreter's installation is
        # classified from the hooked run's report (same executable), with
        # the isolated run's own sys.path for the stdlib zip.
        base_rep = dict(rep) if rep else dict(rep_iso)
        base_rep["sys_path_at_start"] = list(
            (rep or {}).get("sys_path_at_start", [])) + \
            list(rep_iso["sys_path_at_start"])
        cls_i = classify_factory(base_rep, clone_real, temp_real,
                                 mk_dirs | mk_i, shim_real=shim_real)
        o("  sys.prefix in this run: %s (site.py does not run under -S; the "
          "interpreter's installation is classified from the hooked run's "
          "sys.prefix)" % rep_iso["prefix"])
        _ci, _ei, iso_out, _ni = bucket_events(rep_iso, cls_i)
        iso_bo = sum(len(v) for (cat, _rw), v in _ci.items()
                     if cat == BASE_OTHER)
        iso_ba = sum(len(v) for (cat, _rw), v in _ci.items()
                     if cat == BASE_ALLOW)
        th_i, lo_i, nf_i, _st_i, odd_i = split_tops(rep_iso, cls_i)
        o("  exit status: %d (wrapper's recorded exit: %s)"
          % (rci, rep_iso["exit"]))
        o("  summary line: %r" % (si[2] if si else None))
        o("  stdout byte-identical to the plain run: %s"
          % ("yes" if iso_so == pso else "NO"))
        o("  stderr: %r" % (iso_se if len(iso_se) < 2000
                            else iso_se[:2000] + "..."))
        o("  sys.flags: no_site=%d ignore_environment=%d no_user_site=%d"
          % (rep_iso["flags"]["no_site"],
             rep_iso["flags"]["ignore_environment"],
             rep_iso["flags"]["no_user_site"]))
        o("  sys.path when the suite started:")
        for pth in rep_iso["sys_path_at_start"]:
            o("    %s" % (pth.replace(clone, "<clone>") if pth else "''"))
        o("  entries removed from the startup sys.path (empty or "
          "site-packages): %d %s" % (len(rep_iso["dropped_path"]),
                                     rep_iso["dropped_path"] or ""))
        o("  non-stdlib top-level modules at exit: from the interpreter's "
          "installation (via the shim or otherwise) %s; from the clone %s; "
          "no file %s; elsewhere %s"
          % ([("%s -> %s [%s]" % (t, rel, c)) for t, rel, d, c, f in th_i],
             [t for t, _ in lo_i], [t for t, _ in nf_i], odd_i))
        iso_ns_extra = [t for t, rel, d, c, f in th_i if t != "numpy"] + \
            [t for t, _c, _r in odd_i]
        neg = rep_iso.get("neg", {})
        pl_real = os.path.realpath(purelib)
        for name, (kind, info) in sorted(neg.items()):
            if kind == "found":
                locs = [os.path.realpath(x) for x in info if isinstance(x, str)]
                if any(under(x, pl_real) for x in locs):
                    iso_reach.append(name)
            elif kind == "in sys.modules":
                iso_reach.append(name)
        nfound = sum(1 for v in neg.values() if v[0] == "found")
        nerr = sum(1 for v in neg.values() if v[0] == "error")
        o("  negative control (after the run): of %d other top-level names in "
          "the interpreter's site-packages, reachable from the isolated "
          "sys.path into site-packages: %d %s (find_spec found %d elsewhere, "
          "%d raised, %d returned None)"
          % (len(neg), len(iso_reach), iso_reach or "", nfound -
             len([x for x in iso_reach if neg[x][0] == "found"]), nerr,
             sum(1 for v in neg.values() if v[0] == "none")))
        o("  OUTSIDE, with classes '%s' and '%s' (isolated run; the shim "
          "directory is its own class): %d distinct path(s) %s"
          % (BASE_SP, BASE_OTHER, len({x[2] for x in iso_out}),
             sorted({x[2] for x in iso_out}) or ""))
        o("  events in class '%s' (isolated run): %d; in class '%s': %d"
          % (BASE_OTHER, iso_bo, BASE_ALLOW, iso_ba))
        iso_ok = bool(rci == 0 and si and si[0] == si[1] and sp and
                      si == sp and iso_so == pso and not iso_reach and
                      not iso_ns_extra and not iso_out)
    else:
        o("  NOT RUN or no report (numpy not found in the interpreter's "
          "site-packages, or the run did not finish): exit %r, stderr %r"
          % (rci, iso_se[:2000]))
    o("  Result (c): %s" % (
        "numpy is sufficient: the suite prints the same %d/%d with "
        "byte-identical stdout when numpy is the only non-stdlib package "
        "reachable." % (si[0], si[1]) if iso_ok else
        "NOT shown (see above); the import list in (a) is then only what the "
        "suite imported, not a tested sufficient set."))
    o()

    # ---- (2d) the README's literal command ---------------------------------
    o("(d) Literal run, the README's command as written (README.md:55; block "
      ":68), with 'python' = the interpreter above and no flags: $ %s   "
      "[cwd = <clone>]" % shlex.join(lit_cmd))
    o("  exit status: %d" % rcl)
    o("  summary line: %r" % (sl[2] if sl else None))
    o("  lines starting [PASS]: %d; [FAIL]: %d"
      % (sum(1 for x in lso.splitlines() if x.strip().startswith("[PASS]")),
         sum(1 for x in lso.splitlines() if x.strip().startswith("[FAIL]"))))
    o("  stdout byte-identical to the plain run: %s"
      % ("yes" if lso == pso else "NO"))
    o("  stderr: %r" % (lse if len(lse) < 2000 else lse[:2000] + "..."))
    o("  (this machine) PYTHON* variables in the inherited environment, "
      "names only: %s" % (py_env_names or "none"))
    if lprobe:
        o("  (this machine) a probe under the same interpreter, flags, cwd "
          "and environment ($ python -c ...): sys.flags ignore_environment=%d "
          "no_user_site=%d; site.ENABLE_USER_SITE %s; user site %s %s; "
          "sys.dont_write_bytecode %s (so run (d) %s bytecode); sys.path "
          "entries other than '' (the -c form's first entry; -m puts the "
          "cwd there): %s"
          % (lprobe["ignore_environment"], lprobe["no_user_site"],
             lprobe["enable_user_site"], lprobe["user_site"],
             "exists" if lprobe["user_site_isdir"] else "does not exist",
             lprobe["dont_write_bytecode"],
             "writes no" if lprobe["dont_write_bytecode"] else "may write",
             [x for x in lprobe["path"] if x]))
    else:
        o("  probe of run (d)'s configuration: no output")
    o()

    # ---- (2d') existence tests: are checks silently dropped? ----------------
    o("Existence tests the suite made (hooked run; os.path.exists/lexists/"
      "isfile/isdir wrapped to record the real result):")
    q_in, q_out_n, q_pseudo = {}, 0, set()
    q_out_cls, q_outside = {}, set()
    if rep:
        for fn, pth, r in rep.get("exists_queries", []):
            if not isinstance(pth, str):
                q_out_n += 1
                q_out_cls[("fd/none", bool(r))] = \
                    q_out_cls.get(("fd/none", bool(r)), 0) + 1
                continue
            if pth.startswith("<") and pth.endswith(">"):
                q_pseudo.add((pth, fn, bool(r)))   # '<frozen ...>', '<string>'
                continue
            r_ = os.path.realpath(pth if os.path.isabs(pth)
                                  else os.path.join(rep["cwd"], pth))
            if under(r_, clone_real):
                key = (os.path.relpath(r_, clone_real), fn)
                q_in.setdefault(key, set()).add(bool(r))
            else:
                q_out_n += 1
                c_, _r = classify(pth) if classify else ("?", None)
                q_out_cls[(c_, bool(r))] = q_out_cls.get((c_, bool(r)), 0) + 1
                if c_ in OUTSIDE_CLASSES:
                    q_outside.add((r_, fn, bool(r)))
    n_q_in = len(q_in)
    q_false = sorted(k for k, v in q_in.items() if False in v)
    q_false_wt = [k for k in q_false
                  if os.path.lexists(os.path.join(REPO, k[0]))]
    o("  inside the clone: %d distinct (path, test) pairs; True %d, False %d; "
      "code-object pseudo-filenames ('<...>', not paths; excluded from the "
      "pairs): %d distinct %s"
      % (n_q_in, sum(1 for v in q_in.values() if True in v), len(q_false),
         len(q_pseudo), sorted(q_pseudo)))
    for (rel, fn), v in sorted(q_in.items()):
        res = "/".join(sorted(str(x) for x in v))
        wt = ""
        if False in v:
            wt = ("; in this machine's working tree: %s"
                  % ("PRESENT" if os.path.lexists(os.path.join(REPO, rel))
                     else "absent"))
        o("    %-6s %-7s %s%s" % (res, fn, rel, wt))
    o("  outside the clone: %d call(s), by class and result: %s"
      % (q_out_n, ", ".join("%s %s: %d" % (k[0], k[1], v)
                            for k, v in sorted(q_out_cls.items())) or "-"))
    o("  outside the clone in class OUTSIDE, '%s' or '%s' (not the "
      "interpreter's installation, not suite temp): %d distinct %s"
      % (BASE_SP, BASE_OTHER, len(q_outside), sorted(q_outside) or ""))
    clines = None
    if os.path.exists(os.path.join(clone, SUITE_PATH)):
        clines = open(os.path.join(clone, SUITE_PATH)).read().splitlines()
    guards = find_lines(clines, "os.path.exists(")
    o("  static: lines of %s at --ref calling os.path.exists( (%d): %s"
      % (SUITE_PATH, len(guards), ", ".join("%s@%s:%d" % (SUITE_PATH, h7, i)
                                            for i, _ in guards)))
    # comparison with the committed site check
    sc_lines = show_lines(h, a.sitecheck, cwd=clone, env=genv)
    sc_sum = [(i, x.strip()) for i, x in enumerate(sc_lines or [], 1)
              if SUMMARY_RE.match(x)]
    sc_head = find_lines(sc_lines, r"^#\s*HEAD:", regex=True)
    sc_base = None
    if sc_head:
        m = re.match(r"^#\s*HEAD:\s*([0-9a-f]{7,40})", sc_head[0][1])
        sc_base = m.group(1) if m else None
    sc_add = add_commit(clone, h, a.sitecheck, genv)
    blobs = {}
    for label, rev in (("the site check's named base", sc_base),
                       ("the commit that added the site check",
                        sc_add[1] if sc_add else None), ("--ref", h)):
        if rev:
            _, b, _ = sh(["git", "-C", clone, "rev-parse",
                          "%s:%s" % (rev, SUITE_PATH)], env=genv)
            blobs[label] = (rev[:7], b.strip())
    comparable = bool(sc_sum and len(blobs) == 3 and
                      len({b for _, b in blobs.values()}) == 1)
    n_sc = int(SUMMARY_RE.match(sc_sum[0][1]).group(2)) if sc_sum else None
    o("  committed site check %s (read at --ref): summary %s; its header: %s; "
      "committed at %s"
      % (a.sitecheck, "; ".join("%s@%s:%d %r" % (a.sitecheck, h7, i, x)
                                for i, x in sc_sum) or "none found",
         repr(sc_head[0][1]) if sc_head else "no HEAD line",
         "%s (%s)" % (sc_add[1], sc_add[0][:10]) if sc_add else "?"))
    o("  %s blob: %s; comparable (same blob at all three): %s"
      % (SUITE_PATH, "; ".join("%s %s %s" % (k, v[0], v[1][:12])
                               for k, v in blobs.items()),
         "yes" if comparable else "no"))
    sc_equal = bool(comparable and sp and n_sc == sp[1])
    o("  N here %s vs the site check's N %s: %s"
      % (sp[1] if sp else None, n_sc,
         ("equal" if sc_equal else "DIFFERENT") if comparable else
         "not compared (analysis.py differs, so the site check is no "
         "reference; only the existence-test half of conjunct (e) binds)"))
    o("  (Equal analysis.py blobs make the counts comparable; the suite's "
      "data inputs can also move N, so a difference would be investigated, "
      "not adjudicated, here. The record does not show the working tree's "
      "analysis.py at the site check's run; it shows the blob at the base "
      "commit the site check names and at the commit that carried it.)")
    guard_ok = bool(rep and not q_false_wt and not q_outside and
                    (not comparable or sc_equal))
    o()

    o("Full stdout of the plain run:")
    o.block(pso, indent="  | ")
    if hso != pso:
        o("Full stdout of the hooked run (differs from the plain run):")
        o.block(hso, indent="  | ")
    if iso_so and iso_so != pso:
        o("Full stdout of the isolated run (differs from the plain run):")
        o.block(iso_so, indent="  | ")
    if lso != pso:
        o("Full stdout of the literal run (differs from the plain run):")
        o.block(lso, indent="  | ")
    o()
    _, por2, _ = sh(["git", "-C", clone, "status", "--porcelain=v1",
                     "--untracked-files=all"], env=genv)
    _, pig2, _ = sh(["git", "-C", clone, "status", "--porcelain=v1",
                     "--untracked-files=all", "--ignored"], env=genv)
    o("$ git -C <clone> status --porcelain=v1 --untracked-files=all  "
      "(after all four runs)")
    o.block(por2)
    ig = [x for x in pig2.splitlines() if x.startswith("!!")]
    ig_nonpyc = [x for x in ig if "__pycache__" not in x]
    o("  ignored entries after all four runs: %d, of which not __pycache__: "
      "%d %s" % (len(ig), len(ig_nonpyc), ig_nonpyc or ""))
    # what the four runs left in TMPDIR
    resid_dirs, resid_files = [], []
    for name in sorted(os.listdir(tmpd)):
        full = os.path.join(tmpd, name)
        if os.path.isdir(full):
            inner = []
            for r_, _d, fl in os.walk(full):
                for f in fl:
                    fp = os.path.join(r_, f)
                    inner.append((os.path.relpath(fp, full),
                                  os.path.getsize(fp)))
            resid_dirs.append(sorted(inner))
        else:
            resid_files.append(name)
    shapes = sorted({tuple((n, round(s / 1000)) for n, s in d)
                     for d in resid_dirs})
    o("Left in TMPDIR by the four suite runs (before this script's "
      "cleanup): %d director(ies), %d loose file(s); director(ies) hold: %s"
      % (len(resid_dirs), len(resid_files), "; ".join(
          ", ".join("%s (about %d kB)" % (n, k) for n, k in s) or "(empty)"
          for s in shapes) or "-"))
    mk_loc = find_lines(clines, "mkdtemp(")
    o("  (one tempfile.mkdtemp directory per suite run, created at %s and "
      "never removed by the suite; the file's byte count varies by a few "
      "bytes between runs because it records per-session wall-clock "
      "seconds, so it is shown in rounded kB)"
      % (", ".join("%s@%s:%d" % (SUITE_PATH, h7, i) for i, _ in mk_loc)
         or "?"))
    o()

    # ---- (2e) the 103/103 at its own commit ---------------------------------
    o("## (2e) The 103/103 at its own commit: a second fresh clone, and the "
      "check labels compared with --ref's")
    o()
    rd_pin = show_lines(PIN, "README.md")
    res_lines = show_lines(PIN, "RESULTS.md")
    r103 = find_lines(rd_pin, r"103 ?/ ?103", regex=True)
    res103 = find_lines(res_lines, r"103 ?/ ?103", regex=True)

    def blame_commit(path, ln):
        rc_, so_, _ = sh(["git", "-C", REPO, "blame", "--porcelain", "-L",
                          "%d,%d" % (ln, ln), PIN, "--", path])
        return so_.split()[0] if rc_ == 0 and so_.strip() else None
    lineage = blame_commit("README.md", r103[0][0]) if r103 else None
    res_blame = [(i, blame_commit("RESULTS.md", i)) for i, _ in res103]
    lin = {"commit": lineage}
    old_checks = new_checks = None
    cmp_ = None
    scipy_none_flags = scipy_none_lit = None
    scipy_grep = []
    scipy_twin = {}
    lin_anc = None
    if lineage:
        l7 = lineage[:7]
        _, lsubj, _ = sh(["git", "-C", REPO, "log", "-1", "--format=%cs %s",
                          lineage])
        lin["subject"] = lsubj.strip()
        o("README.md@%s:%d says 103/103; git blame at %s attributes that line "
          "to %s (%s). RESULTS.md's 103/103 line(s) at %s: %s."
          % (PIN, r103[0][0], PIN, l7, lsubj.strip()[:140], PIN,
             ", ".join("RESULTS.md@%s:%d written by %s" % (PIN, i, (c or "?")[:7])
                       for i, c in res_blame) or "none"))
        lenv = dict(os.environ)
        lenv["TMPDIR"] = ltmp
        cmd = ["git", "clone", "--no-local", a.source, lclone]
        rcl1, _, lse1 = sh(cmd, env=genv)
        rcl2, lse2 = 1, ""
        if rcl1 == 0:
            rcl2, _, lse2 = sh(["git", "-C", lclone, "checkout", "--detach",
                                lineage], env=genv)
        _, lhead, _ = sh(["git", "-C", lclone, "rev-parse", "HEAD"], env=genv)
        o("$ git clone --no-local %s <lineage clone>: exit %d; $ git -C "
          "<lineage clone> checkout --detach %s: exit %d; HEAD %s (%s the "
          "blamed commit); same git environment as (1)"
          % (a.source, rcl1, lineage, rcl2, lhead.strip(),
             "equals" if lhead.strip() == lineage else "DIFFERS FROM"))
        rca, _, _ = sh(["git", "-C", clone, "merge-base", "--is-ancestor",
                        lineage, h], env=genv)
        lin_anc = rca == 0
        o("  %s is an ancestor of --ref (git merge-base --is-ancestor): %s"
          % (l7, "yes" if lin_anc else "NO"))
        lin_cmd = [a.python, "-E", "-s", "-m", SUITE_MOD]
        rco, oso, ose = sh(lin_cmd, cwd=lclone, env=lenv)
        so_old = summ(oso)
        lin.update(exit=rco, summary=so_old)
        o("$ %s   [cwd = <lineage clone>, TMPDIR = a second scratch "
          "directory]" % shlex.join(lin_cmd))
        o("  exit status: %d; summary line: %r; lines starting [PASS]: %d, "
          "[FAIL]: %d; stderr %r"
          % (rco, so_old[2] if so_old else None,
             sum(1 for x in oso.splitlines() if x.strip().startswith("[PASS]")),
             sum(1 for x in oso.splitlines() if x.strip().startswith("[FAIL]")),
             ose if len(ose) < 2000 else ose[:2000] + "..."))
        # scipy: absent from this interpreter, and named by no .py at lineage
        scipy_probe = ("import importlib.util as u; "
                       "print(u.find_spec('scipy') is None)")
        _, s1, _ = sh([a.python, "-E", "-s", "-c", scipy_probe], cwd=lclone,
                      env=lenv)
        _, s2, _ = sh([a.python, "-c", scipy_probe], cwd=lclone, env=lenv)
        scipy_none_flags = s1.strip() == "True"
        scipy_none_lit = s2.strip() == "True"
        _, sg, _ = sh(["git", "-C", lclone, "grep", "-n", "-I", "scipy",
                       lineage, "--", "*.py"], env=genv)
        for x in sg.splitlines():
            pp = x.split(":", 3)
            if len(pp) == 4:
                scipy_grep.append((pp[1], int(pp[2]), pp[3].strip()))
        # the same line at --ref (the claim is about the lineage tree, an
        # ancestor of --ref; the --ref twin is stated alongside it)
        for f, i, t in scipy_grep:
            src_h = show_lines(h, f, cwd=clone, env=genv) or []
            scipy_twin[(f, i)] = [j for j, y in enumerate(src_h, 1)
                                  if y.strip() == t]

        def twin_s(f, i):
            js = scipy_twin.get((f, i)) or []
            return (" (the same line at %s)" % ", ".join(
                "%s@%s:%d" % (f, h7, j) for j in js)) if js else \
                " (no identical line in %s at --ref)" % f
        o("  scipy: importlib.util.find_spec('scipy') under this interpreter "
          "is None with -E -s: %s; with no flags: %s. Tracked .py files at %s "
          "that mention scipy (git grep -n -I scipy %s -- '*.py'): %d %s"
          % (scipy_none_flags, scipy_none_lit, l7, l7, len(scipy_grep),
             "; ".join("%s@%s:%d %r%s" % (f, l7, i, t[:100], twin_s(f, i))
                       for f, i, t in scipy_grep)))
        old_checks, ocol = parse_checks(oso)
        new_checks, ncol = parse_checks(pso)
        if old_checks and new_checks:
            def dmap(cs):
                d, dup = {}, []
                for st_, nm, rest in cs:
                    if nm in d:
                        dup.append(nm)
                    d[nm] = (st_, rest)
                return d, dup
            od, odup = dmap(old_checks)
            nd, ndup = dmap(new_checks)
            same = [n_ for n_ in od if n_ in nd and od[n_][1] == nd[n_][1]]
            diff = [n_ for n_ in od if n_ in nd and od[n_][1] != nd[n_][1]]
            old_only = [n_ for n_ in od if n_ not in nd]
            new_only = [n_ for n_ in nd if n_ not in od]
            cmp_ = dict(n_old=len(old_checks), n_new=len(new_checks),
                        same=same, diff=diff, old_only=old_only,
                        new_only=new_only, odup=odup, ndup=ndup)
            o("  Check labels (label = the text between '[PASS] ' and the "
              "column where every line of that run has ' expected ': column "
              "%d at %s, %d at --ref; the remainder, 'expected <e> got <g>   "
              "(<source>)', is compared as a whole). Duplicate labels: %d at "
              "%s, %d at --ref."
              % (ocol, l7, ncol, len(odup), l7, len(ndup)))
            o("    at %s: %d checks; at --ref: %d checks" %
              (l7, len(old_checks), len(new_checks)))
            o("    in both, remainder identical (expected, got and cited "
              "source): %d" % len(same))
            o("    in both, remainder different: %d%s" % (len(diff), "".join(
                "\n      %r: %s -> %s" % (n_, od[n_][1], nd[n_][1])
                for n_ in diff)))
            o("    at %s only (not at --ref): %d" % (l7, len(old_only)))
            rm_by = {}
            for n_ in old_only:
                _, lg, _ = sh(["git", "-C", clone, "log", "-S", n_,
                               "--format=%h %cs %s", "-1", h, "--",
                               SUITE_PATH], env=genv)
                rm_by[n_] = lg.strip()
                o("      %r  [%s]  last change to its occurrence count in "
                  "%s at --ref (git log -S): %s"
                  % (n_, od[n_][1], SUITE_PATH,
                     (lg.strip()[:150] + ("..." if len(lg.strip()) > 150
                                          else "")) or "not located"))
            cmp_["rm_by"] = rm_by
            rm_commits = {v.split()[0] for v in rm_by.values() if v}
            o("    at --ref only (added after %s): %d, by label prefix "
              "(the text before ':' where there is one):" % (l7, len(new_only)))
            groups = {}
            for n_ in new_only:
                pre_ = n_.split(":", 1)[0] if ":" in n_ else "(no prefix)"
                groups.setdefault(pre_, []).append(n_)
            for pre_ in sorted(groups):
                o("      %s (%d): %s" % (pre_, len(groups[pre_]),
                                         " | ".join(groups[pre_])))
            # same-prefix replacements for the removed labels
            old_pre = {n_.split(":", 1)[0] for n_ in old_only if ":" in n_}
            repl = []
            for n_ in new_only:
                if ":" in n_ and n_.split(":", 1)[0] in old_pre:
                    _, lg, _ = sh(["git", "-C", clone, "log", "-S", n_,
                                   "--format=%h", h, "--", SUITE_PATH],
                                  env=genv)
                    rows_ = [x for x in lg.split() if x]
                    repl.append((n_, rows_[-1] if rows_ else None,
                                 nd[n_][1]))
            cmp_["repl"] = repl
            if repl:
                o("    --ref-only labels sharing a prefix with a removed "
                  "label (%s), with the commit that first added each (git "
                  "log -S, oldest) and its cited source:"
                  % ", ".join(sorted(old_pre)))
                for n_, c_, rest in repl:
                    src = rest[rest.rfind("(") + 1:-1] if rest.endswith(")") \
                        else rest
                    o("      %r  added by %s%s  (source: %s)"
                      % (n_, c_ or "?", "  [a commit that removed a "
                         "label above]" if c_ and c_ in rm_commits else "",
                         src))
        else:
            o("  check lines not parsed (%s / %s); labels not compared"
              % (ocol if not old_checks else "ok",
                 ncol if not new_checks else "ok"))
    else:
        o("README.md@%s has no 103/103 line; nothing to trace." % PIN)
    o()

    # ---- (3) README, the note, greps -----------------------------------------
    o("## (3) Paths in README.md and the note; the 103/103 and absolute-path "
      "greps")
    o()
    _, tags_s, _ = sh(["git", "-C", clone, "tag", "-l"], env=genv)
    tags = set(x for x in tags_s.splitlines() if x)
    o("Tags in the clone: %s" % sorted(tags))
    _, rd, _ = sh(["git", "-C", clone, "show", "%s:README.md" % h], env=genv)
    rdl = rd.splitlines()
    refs = readme_refs(rd)
    rows, problems, globinfo = resolve_refs(refs, clone, h, tracked, tags,
                                            genv)

    # a module that resolves can still need, at run time, material a clone
    # lacks: the Qwen adapter's gitignored jlens-qwen36/ clone and its model
    rt_facts = {}

    def runtime_dep(relpy):
        src = show_lines(h, relpy, cwd=clone, env=genv)
        imp = find_lines(src, r"^\s*(from\s+[.\w]*adapters\.qwen_mlx\s+import"
                         r"|import\s+[.\w]*qwen_mlx)", regex=True)
        if not imp:
            return None
        q = "valence_core/adapters/qwen_mlx.py"
        ql = show_lines(h, q, cwd=clone, env=genv) or []
        cl = find_lines(ql, r"^CLONE\s*=.*jlens-qwen36", regex=True)
        msg = find_lines(ql, "jlens-qwen36 clone is missing")
        rais = [i for i, x in find_lines(ql, "raise RuntimeError(")
                if msg and 0 <= msg[0][0] - i <= 3]
        jimp = find_lines(ql, 'import_module("jlens_qwen.')
        mimp = find_lines(ql, 'import_module("mlx.')
        mid = [(i, re.search(r'model_id: str = "([^"]+)"', x).group(1))
               for i, x in find_lines(ql, r'model_id: str = "[^"]+"',
                                      regex=True)]
        # where the clone check runs: every call of _ensure_clone_on_path()
        # (not its def), with the def it sits in
        calls = []
        for i, x in find_lines(ql, r"^\s+_ensure_clone_on_path\(\)\s*$",
                               regex=True):
            defs = [y.strip() for j, y in enumerate(ql[:i - 1], 1)
                    if re.match(r"^\s*def\s", y)]
            calls.append((i, defs[-1].split("(")[0].split()[-1]
                          if defs else "?"))
        mod_calls = find_lines(ql, r"^_ensure_clone_on_path\(\)", regex=True)
        cons = [i for i, x in find_lines(src, r"QwenMLXAdapter\(", regex=True)
                if "import" not in x]
        sent = find_lines(rdl, "The oracle tier") + \
            find_lines(rdl, "require real inference")
        only_init = bool(calls and all(d == "__init__" for _, d in calls)
                         and not mod_calls)
        # mlx: carried by the clone? imported by the model-free suite (the
        # hooked run's non-stdlib top-level modules)?
        mlx_tracked = sorted(f for f in tracked if f.split("/")[0] == "mlx")
        mlx_suite = any(t == "mlx" for t, *_r in third)
        mlx_desc = "the third-party mlx package, which %s and %s" % (
            "a clone does not carry" if not mlx_tracked else
            "the clone DOES carry (%d tracked path(s))" % len(mlx_tracked),
            "the hooked run shows the model-free suite does not import"
            if not mlx_suite else "the hooked run shows the model-free suite "
            "ALSO imports")
        rt_facts[relpy] = dict(imp=[i for i, _ in imp],
                               mlx=[i for i, _ in mimp], mlx_desc=mlx_desc,
                               calls=calls, cons=cons, rais=rais,
                               only_init=only_init)
        return ("resolves, but at run time it needs material absent from a "
                "clone: it imports the Qwen adapter (%s@%s:%s), whose module "
                "sets %s (%s@%s:%s); constructing the adapter, which %s does "
                "at %s, runs _ensure_clone_on_path() (:%s, in %s), which "
                "raises RuntimeError when that gitignored clone is missing "
                "(:%s)%s; the constructor then imports mlx.core (:%s; %s) "
                "and jlens_qwen.* from "
                "the clone (:%s), and loads the MLX model id %r by default "
                "(:%s); README.md@%s:%s says this tier needs the laptop Qwen "
                "stack"
                % (relpy, h7, ",".join(str(i) for i, _ in imp),
                   cl[0][1].strip() if cl else "?", q, h7,
                   cl[0][0] if cl else "?", os.path.basename(relpy),
                   ("%s@%s:%d%s" % (relpy, h7, cons[0], "".join(
                       " and :%d" % i for i in cons[1:]))) if cons else "?",
                   ",".join(str(i) for i, _ in calls) or "?",
                   "/".join(sorted({d for _, d in calls})) or "?",
                   ",".join(str(i) for i in rais) or "?",
                   ("; the import alone does not raise, since the module "
                    "calls it only there, not at import time") if only_init
                   else "",
                   ",".join(str(i) for i, _ in mimp) or "?", mlx_desc,
                   "-".join(str(i) for i, _ in (jimp[:1] + jimp[-1:])) or "?",
                   mid[0][1] if mid else "?", mid[0][0] if mid else "?", h7,
                   "-".join(str(i) for i, _ in (sent[:1] + sent[-1:]))
                   or "?"))
    runtime_out = []
    for k_, (ln, kind, raw, st, ok) in enumerate(rows):
        m_ = re.search(r"-> (\S+\.py) \(tracked\)", st)
        if ok and m_:
            dep = runtime_dep(m_.group(1))
            if dep:
                rows[k_] = (ln, kind, raw, st + "; " + dep, ok)
                runtime_out.append((ln, raw, dep))
    o("README.md at --ref: %d line(s); %d reference(s) extracted (markdown "
      "link targets, inline code spans, fenced code lines, URLs):"
      % (len(rdl), len(rows)))
    for ln, kind, raw, st, ok in rows:
        o("  README.md:%-3d %-17s %-48s %s%s" % (ln, kind, repr(raw), st,
                                               "" if ok else "   <-- flag"))
    o("Flagged README references: %d" % len(problems))
    for ln, raw, st in problems:
        o("  README.md:%d %r: %s" % (ln, raw, st))
        lo, hi_ = max(1, ln - 1), min(len(rdl), ln + 1)
        for k in range(lo, hi_ + 1):
            o("      README.md:%d | %s" % (k, rdl[k - 1]))
    o("README references that resolve in the clone but whose run time needs "
      "material absent from a clone (not flagged as paths; see note 10): %d "
      "%s" % (len(runtime_out), ", ".join("README.md:%d %r" % (ln, raw)
                                          for ln, raw, _ in runtime_out)))
    for needle in ("/Users/", "/workspace/"):
        o("  README.md lines containing %r: %d" %
          (needle, sum(1 for x in rdl if needle in x)))
    # FINDINGS chain: tracked FINDINGS*.md that README does not link
    f_tracked = sorted(f for f in tracked
                       if fnmatch.fnmatchcase(f, "FINDINGS*.md") and "/" not in f)
    f_linked = []                       # in README order of first appearance
    for ln, kind, raw, st, ok in rows:
        if kind == "link" and fnmatch.fnmatchcase(os.path.basename(raw),
                                                  "FINDINGS*.md"):
            nm = os.path.normpath(raw[2:] if raw.startswith("./") else raw)
            if nm not in f_linked:
                f_linked.append(nm)
    f_link_lines = sorted({ln for ln, kind, raw, st, ok in rows
                           if kind == "link" and
                           fnmatch.fnmatchcase(os.path.basename(raw),
                                               "FINDINGS*.md")})
    f_unlinked = [f for f in f_tracked if f not in f_linked]
    f_adds = {f: add_commit(clone, h, f, genv) for f in f_tracked}
    o("  FINDINGS*.md tracked at --ref (%d, with the commit that added each): "
      "%s" % (len(f_tracked), ", ".join(
          "%s (%s, %s)" % (f, f_adds[f][1], f_adds[f][0][:10])
          if f_adds[f] else f for f in f_tracked)))
    o("  linked by README.md's synthesis chain (README.md@%s:%s): %s; "
      "tracked but not linked: %s"
      % (h7, ",".join(str(x) for x in f_link_lines), f_linked,
         f_unlinked or "none"))
    o()
    note_like = sorted(os.path.relpath(x, REPO) for x in
                       glob.glob(os.path.join(REPO, "RESEARCH-NOTE*")) +
                       glob.glob(os.path.join(REPO, "archive", "RESEARCH-NOTE*")))
    note_here = os.path.exists(os.path.join(REPO, NOTE))
    note_trk = NOTE in tracked
    o("The note (this machine's working tree): %s is %s at the repository "
      "root (RESEARCH-NOTE* at the root or in archive/: %s); tracked at "
      "--ref: %s. Its paths are checked when it arrives (re-run this "
      "script, and extend the check to the note)."
      % (NOTE, "PRESENT" if note_here else "NOT present", note_like or "none",
         "yes" if note_trk else "no"))
    o()
    # 103/103
    _, g103, _ = sh(["git", "-C", clone, "grep", "-n", "-I", "-E",
                     r"103 ?/ ?103", h, "--"], env=genv)
    hits = []
    for x in g103.splitlines():
        parts = x.split(":", 3)
        if len(parts) == 4:
            hits.append((parts[1], int(parts[2]), parts[3]))
    files103 = sorted({p_ for p_, _, _ in hits})
    o("Tracked text files at --ref that say 103/103 (git grep -n -I -E "
      "'103 ?/ ?103' %s): %d file(s), %d line(s). Locators are "
      "<path>@%s:<line>." % (h7, len(files103), len(hits), h7))

    def kind103(p_):
        if p_ == "README.md":
            return "live doc"
        if p_ == BLOCK:
            return "the block"
        if p_ == "RESULTS.md" or p_.startswith(("results/raw/", "archive/")):
            return "dated record entry"
        return "other"
    for p_, ln, txt in hits:
        t = txt.strip()
        m = re.search(r"103 ?/ ?103", t)
        lo = max(0, m.start() - 70) if m else 0
        snip = ("..." if lo else "") + t[lo:lo + 150] + \
            ("..." if len(t) > lo + 150 else "")
        o("  %s@%s:%d  [%s]  %s" % (p_, h7, ln, kind103(p_), snip))
    o("Committed site check: %s" % ("; ".join(
        "%s@%s:%d %r" % (a.sitecheck, h7, i, x) for i, x in sc_sum) or "-"))
    o()
    for needle in ("/Users/", "/workspace/"):
        _, gc, _ = sh(["git", "-C", clone, "grep", "-I", "-c", "-F", needle,
                       h, "--"], env=genv)
        per = []
        for x in gc.splitlines():
            parts = x.rsplit(":", 1)
            if len(parts) == 2:
                per.append((parts[0].split(":", 1)[1], int(parts[1])))
        o("Tracked text files at --ref containing %r: %d file(s), %d line(s) "
          "(N12 lists them)." % (needle, len(per), sum(c for _, c in per)))
        perd = dict(per)
        groups = (
            ("README.md", [f for f in perd if f == "README.md"], True),
            ("data files the suite read", [f for f in perd
                                           if f in set(data_reads)], True),
            ("files the suite executed as code",
             [f for f in perd if f in executed], True),
            ("files the suite only read as text (structural scans)",
             [f for f in perd if f in set(py_scanned)], False))
        for label, fl, lines in groups:
            o("  in %s: %d file(s)%s" % (label, len(fl), "" if lines or not fl
                                         else ": " + ", ".join(
                                             "%s (%d)" % (f, perd[f])
                                             for f in sorted(fl))))
            if not lines:
                continue
            for f in sorted(fl):
                _, gl, _ = sh(["git", "-C", clone, "grep", "-n", "-I", "-F",
                               needle, h, "--", f], env=genv)
                for x in gl.splitlines():
                    pp = x.split(":", 3)
                    if len(pp) == 4:
                        t = pp[3].strip()
                        o("    %s@%s:%s  %s" % (
                            pp[1], h7, pp[2],
                            t if len(t) <= 140 else t[:140] + "..."))
    o("  (A static mention is not a read. Whether the suite depends on an "
      "absolute path is settled by the audit hook in (2): reads OUTSIDE the "
      "clone and the interpreter's installation = %d.)"
      % len({x[2] for x in outside}))
    o()

    # ---- (4) cleanup ------------------------------------------------------
    o("## (4) Cleanup")
    o()
    home_left = sorted(os.listdir(home)) if os.path.isdir(home) else None
    o("The empty HOME/XDG_CONFIG_HOME directory before deletion: %s"
      % ("still empty (git created nothing there)" if home_left == []
         else "NOT empty: %s" % home_left))
    if a.keep:
        o("Clone KEPT (--keep): %s" % clone)
    else:
        for pth in (clone, tmpd, lclone, ltmp, home):
            if os.path.lexists(pth):
                rmtree_force(pth)
        if os.path.lexists(shim):
            rmtree_force(shim)
        for pth in (report, report_iso):
            if os.path.exists(pth):
                os.remove(pth)
        o("Clone deleted: %s -> exists afterwards: %s" %
          (clone, os.path.exists(clone)))
        o("Lineage clone deleted: %s -> exists afterwards: %s" %
          (lclone, os.path.exists(lclone)))
        o("Scratch TMPDIRs (with the suite's leftover mkdtemp directories), "
          "empty HOME, numpy shim and hook reports deleted: %s" %
          (not os.path.exists(tmpd) and not os.path.exists(ltmp) and
           not os.path.exists(home) and not os.path.lexists(shim) and
           not os.path.exists(report) and not os.path.exists(report_iso)))
    o("--ref commit: %s" % h)
    o()

    # ---- referent notes (a wrong referent is a note, not a STOP) -------------
    blk_lines = show_lines(PIN, BLOCK)
    pf_lines = show_lines(PIN, PREFLIGHT)
    res_lines = show_lines(PIN, "RESULTS.md")
    b3 = find_lines(blk_lines, "Code names the right one in the raw and "
                    "proceeds")
    pfl = find_lines(pf_lines, "N11 therefore passes") + \
        find_lines(pf_lines, "N/N from a fresh clone")
    pfl = sorted(set(pfl))
    scipy = find_lines(res_lines, "pip install numpy scipy")
    scipy_loc = []
    for i, _x in scipy:
        lo = i - 1 if (i > 1 and "103/103" in res_lines[i - 2]) else i
        scipy_loc.append("RESULTS.md@%s:%s" % (PIN, ("%d-%d" % (lo, i))
                                                if lo != i else "%d" % i))
    walks = find_lines(clines, "os.walk(")
    pre3 = find_lines(blk_lines, "a wrong referent here is a note to fix, "
                      "not a STOP")
    o("## Referent notes (block preamble, %s: a wrong referent here is a "
      "note to fix, not a STOP)"
      % (", ".join("%s@%s:%d" % (BLOCK, PIN, i) for i, _ in pre3) or "?"))
    o()
    # lineage sentence for note 1, from (2e)
    lin_sent = ""
    if cmp_ and lineage:
        l7 = lineage[:7]
        rmc = sorted({v.split()[0] for v in cmp_["rm_by"].values() if v})
        rms = sorted({v.split(" ", 2)[2] for v in cmp_["rm_by"].values()
                      if v and len(v.split(" ", 2)) == 3})
        rep_by = [n_ for n_, c_, _r in cmp_["repl"] if c_ and c_ in rmc]
        lin_sent = (
            " Lineage of the count, from (2e): at %s (the commit git blame "
            "names for README.md@%s:%d's 103/103%s) a fresh clone prints %s "
            "(exit %d). Of those %d checks, %d are at --ref with identical "
            "expected, got and cited source; %d are at --ref with a different "
            "remainder; %d are not at --ref (%s), each last changed by %s "
            "(git log -S), whose subject begins %r. Of --ref's %d checks, the "
            "other %d are later additions, %d of them first added by that "
            "same commit (%s). %s; for README-NOTE item (3), 'what 103/103 "
            "covers'."
            % (l7, PIN, r103[0][0],
               (", which also wrote %s" % ", ".join(
                   "RESULTS.md@%s:%d" % (PIN, i) for i, c in res_blame
                   if c == lineage)) if any(c == lineage for _, c in res_blame)
               else "",
               "%d/%d" % (lin["summary"][0], lin["summary"][1])
               if lin.get("summary") else "no summary line", lin["exit"],
               cmp_["n_old"], len(cmp_["same"]), len(cmp_["diff"]),
               len(cmp_["old_only"]), "; ".join(repr(x) for x in
                                                cmp_["old_only"]),
               ", ".join(rmc) or "?", (rms[0][:90] + "...") if rms else "?",
               cmp_["n_new"], len(cmp_["new_only"]), len(rep_by),
               "; ".join(repr(x) for x in rep_by) or "none",
               ("So --ref's %d checks are not a strict superset of the %d"
                % (cmp_["n_new"], cmp_["n_old"]))
               if (cmp_["old_only"] or cmp_["diff"]) else
               ("So --ref's %d checks contain all %d unchanged"
                % (cmp_["n_new"], cmp_["n_old"]))))
    readme103 = [(p_, ln) for p_, ln, _ in hits if p_ == "README.md"]
    block103 = [ln for p_, ln, _ in hits if p_ == BLOCK]
    o("1. Count. The block (%s) and README.md (%s) say 103/103. The suite at "
      "--ref prints %s; the committed site check says %s. The pass "
      "condition applied here is Code's reading, not a ruling by the design "
      "seat or the PI: the block's preamble (%s) says that where a referent "
      "is wrong, Code names the right one in the raw and proceeds, and "
      "Code's preflight raw (%s) reads N11 as passing if the suite prints "
      "N/N from a fresh clone, with N stated in the raw. That reading is "
      "flagged for the design seat and the PI. Because N/N alone would also "
      "pass a clone that silently skips checks whose artifact is absent, "
      "conjunct (e) is added. Every tracked line that says 103/103 is listed "
      "in (3) with its kind (live doc, the block, dated record entry); only "
      "the live doc and the block make a present-tense claim about the "
      "count. README.md is not edited by this audit; the PI decides its "
      "wording, and the wording of the README-NOTE the block's §6 item (3) "
      "describes.%s"
      % (", ".join("%s@%s:%d" % (BLOCK, h7, x) for x in block103) or "-",
         ", ".join("%s@%s:%d" % (p_, h7, ln) for p_, ln in readme103) or "-",
         "%d/%d" % (sp[0], sp[1]) if sp else "no summary line",
         "; ".join("%s@%s:%d %r" % (a.sitecheck, h7, i, x) for i, x in sc_sum)
         or "-",
         ", ".join("%s@%s:%d" % (BLOCK, PIN, i) for i, _ in b3) or "?",
         "%s@%s:%s" % (PREFLIGHT, PIN, "-".join(str(i) for i, _ in
                                                  (pfl[:1] + pfl[-1:])))
         if pfl else "?", lin_sent))
    o("2. The block says 'clone the tag'. No release tag exists yet (its "
      "name is the PI's; the clone's tags are %s). This run is at --ref = "
      "%s, cloned from %s. It is therefore provisional. The block's pass is "
      "evaluated by re-running this script with --ref <tag>, and, once the "
      "repository is published, --source <published remote URL> (this "
      "audit makes no network access, so the remote form is not exercised "
      "here)." % (sorted(tags), h, a.source))
    o("3. The block asks that no path in the note points outside the clone. "
      "%s is not present at the repository root or in archive/ (this "
      "machine's working tree), so only README.md is checked here." % NOTE
      if not note_here else
      "3. %s is present at the repository root; this script does not yet "
      "check its paths (extend it before the release run)." % NOTE)
    hrow = [st for ln, kind, raw, st, ok in rows if raw == "HANDOFF-*.md"]
    if hrow:
        o("4. README.md points readers to 'the newest HANDOFF-*.md' for the "
          "current state. %s." % hrow[0])
    if f_unlinked:
        o("5. README.md's synthesis chain (README.md@%s:%s) links %s and "
          "stops there; tracked at --ref but not in the chain: %s. "
          "(README.md:40's 'FINDINGS*.md' glob covers every one.) For whoever "
          "writes the README-NOTE; README.md is not edited here."
          % (h7, "-".join(str(x) for x in (f_link_lines[:1] +
                                           f_link_lines[-1:])),
             " -> ".join(f_linked), ", ".join(
                 "%s (added %s, %s)" % (f, f_adds[f][1], f_adds[f][0][:10])
                 if f_adds[f] else f for f in f_unlinked)))
    ed_skipped = any("_editable_impl_jlens_qwen36.pth" in x for x in skips)
    scipy_imports = [(f, i, t) for f, i, t in scipy_grep
                     if re.match(r"^\s*(import\s+scipy|from\s+scipy[\s.])", t)]
    scipy_free_then = bool(lineage and lin.get("exit") == 0 and
                           lin.get("summary") and
                           lin["summary"][0] == lin["summary"][1] and
                           scipy_none_flags and not scipy_imports)
    scipy_sent = ""
    if scipy_loc:
        if scipy_free_then:
            scipy_sent = (
                "An earlier record entry installed more (%s: 'pip install "
                "numpy scipy' into a bare container), but scipy was not "
                "needed then either: at %s no tracked .py file imports scipy "
                "(the only mention: %s), and a fresh clone at %s prints %d/%d "
                "(exit 0) under this interpreter, on which find_spec('scipy') "
                "is None ((2e)). At --ref the suite imports no scipy%s."
                % (", ".join(scipy_loc), lineage[:7],
                   "; ".join("%s@%s:%d %r%s" % (
                       f, lineage[:7], i, t[:80],
                       (" (the same line at %s)" % ", ".join(
                           "%s@%s:%d" % (f, h7, j)
                           for j in scipy_twin[(f, i)]))
                       if scipy_twin.get((f, i)) else "")
                       for f, i, t in scipy_grep) or "none",
                   lineage[:7], lin["summary"][0], lin["summary"][1],
                   " and passes with numpy alone on the path" if iso_ok
                   else ""))
        else:
            scipy_sent = (
                "An earlier record entry installed more (%s: 'pip install "
                "numpy scipy' into a bare container); whether scipy was "
                "needed at that entry's commit is NOT settled here (see "
                "(2e): scipy imports at %s %s; find_spec None %s; run "
                "exit %s, summary %s). At --ref the suite imports no scipy%s."
                % (", ".join(scipy_loc), (lineage or "?")[:7],
                   scipy_imports or "none", scipy_none_flags,
                   lin.get("exit"), lin.get("summary"),
                   " and passes with numpy alone on the path" if iso_ok
                   else ""))
    o("6. Interpreter and imports. The interpreter used here lives inside "
      "the gitignored jlens-qwen36/ clone (its .venv). Its site-packages "
      "holds _editable_impl_jlens_qwen36.pth, which names the jlens-qwen36/ "
      "root; %s. The hook shows %d distinct path(s) under jlens-qwen36/ "
      "outside .venv in file events, and %d in code objects. "
      "Third-party packages the suite imported (sys.modules at exit, "
      "hooked run): %s%s. %s"
      % ("this Python skips it because the file carries the macOS hidden "
         "flag (the 'Skipping hidden .pth file' lines in (2)), so that root "
         "is not on sys.path" if ed_skipped else
         "site's -v output in (2) does NOT report skipping it",
         len(out_v), len(cout_v),
         ", ".join(t for t, *_r in third) or "none",
         ("; the isolated run (c) shows numpy alone is sufficient"
          if iso_ok else "; the isolated run (c) did NOT show that set "
          "sufficient"),
         scipy_sent))
    wdesc = []
    for i, x in walks:
        nxt = [(j, clines[j - 1].strip()) for j in range(i + 1, i + 4)
               if j <= len(clines)]
        wdesc.append("%s@%s:%d %r, then %s" % (
            SUITE_PATH, h7, i, x.strip(), "; ".join(
                ":%d %r" % (j, t) for j, t in nxt)))
    o("7. Two of the suite's structural checks walk the tree on disk, not "
      "the tracked set (source lines at --ref, quoted): %s. In a clone the "
      "walks see the tracked set (plus the bytecode the runs write). In a "
      "working tree they also read any untracked .py file under those roots "
      "that the skip lines do not exclude, so a working-tree site check and "
      "a clone can in principle differ in what these two checks read. "
      "Observation only; the record's analyzer is not changed."
      % " | ".join(wdesc))
    tmp_writes_other = sorted({tnorm(rel) for (cat, rw), v in cats.items()
                               if cat == "suite-temp" and rw == "write"
                               for (ev, rel) in v
                               if "<mkdtemp>" not in tnorm(rel)})
    tmp_removed = {tnorm(rel) for (cat, rw), v in cats.items()
                   if cat == "suite-temp" for (ev, rel) in v
                   if ev == "os.remove"}
    o("8. Temp files. The suite leaves one tempfile.mkdtemp directory "
      "(holding d.json.checkpoint, about %s kB) in $TMPDIR per run (%s); "
      "after the four runs here, TMPDIR held %d such director(ies) and %d "
      "loose file(s). Its other temp write(s) in the hooked run: %s "
      "(removed by an os.remove event: %s). The hook shows %d distinct "
      "path(s) read or written outside the clone, the interpreter's "
      "installation and TMPDIR. This script pointed TMPDIR at its scratch "
      "and deleted it; on a reader's machine the directories stay in the "
      "system TMPDIR. For README-NOTE item (3)."
      % ("/".join(sorted({str(k) for s in shapes for n, k in s})) or "?",
         ", ".join("%s@%s:%d" % (SUITE_PATH, h7, i) for i, _ in mk_loc)
         or "?", len(resid_dirs), len(resid_files),
         " and ".join(tmp_writes_other) or "none",
         ("yes" if tmp_writes_other and
          all(x in tmp_removed for x in tmp_writes_other) else "no")
         if tmp_writes_other else "-",
         len({x[2] for x in outside})))
    o("9. Outside N11's scope, noted for whoever writes the block's §6 "
      "README-NOTE: README.md's status heading reads %r."
      % next((x for x in rdl if x.startswith("## Where")), ""))
    for k_, (ln_, raw_, dep_) in enumerate(runtime_out):
        o("%d. README.md@%s:%d %r %s. It is not a path pointing outside the "
          "clone, so it is not flagged in (3); for README-NOTE item (3), "
          "this tier does not run from a clone." % (10 + k_, h7, ln_, raw_,
                                                    dep_))
    o()

    # ---- figure statuses ----------------------------------------------------
    st_loc = find_lines(blk_lines, "status ∈ {")
    o("## Figure statuses (N1's vocabulary, %s: reproduced, log-only, not "
      "found, discrepant; plus computed-new for a figure this item computes "
      "that no record line states)"
      % (", ".join("%s@%s:%d" % (BLOCK, PIN, i) for i, _ in st_loc) or "?"))
    o()
    heads = find_lines(blk_lines, r"^#{2,3} ", regex=True)

    def blk_section(ln_):
        hh = [x for i, x in heads if i <= ln_]
        if not hh:
            return "?"
        t_ = hh[-1].lstrip("# ").split(" — ")[0].split(".")[0]
        return "the block's §" + t_ if t_.isdigit() else t_
    b68 = find_lines(blk_lines, "record Python version")
    l68 = "%s@%s:%s" % (BLOCK, PIN, b68[0][0] if b68 else "?")
    n_s = "%d/%d" % (sp[0], sp[1]) if sp else "no summary"
    suite_val = ("%s in runs (a), (b), (c), (d) at --ref (domain: the %s "
                 "checks the suite defines at --ref)"
                 % (n_s, sp[1] if sp else "?"))
    lin_val = ("%d/%d from a fresh clone at %s, the commit that wrote it "
               "((2e))" % (lin["summary"][0], lin["summary"][1], lineage[:7])
               if lineage and lin.get("summary") else "not run")
    pf_head = find_lines(pf_lines, r"^- HEAD: [0-9a-f]{40}", regex=True)
    pf_rev = pf_head[0][1].split()[-1] if pf_head else None
    pf_blob = None
    if pf_rev:
        _, pf_blob, _ = sh(["git", "-C", REPO, "rev-parse",
                            "%s:%s" % (pf_rev, SUITE_PATH)])
        pf_blob = pf_blob.strip()
    ref_blob = blobs.get("--ref", (None, None))[1]
    stab = []
    for p_, ln_, _t in hits:
        loc = "%s@%s:%d" % (p_, h7, ln_)
        if p_ == BLOCK:
            stab.append(("103/103 (%s)" % blk_section(ln_), loc, suite_val,
                         "discrepant (stale referent; note 1)"))
        elif p_ == "README.md":
            stab.append(("103/103 (live doc)", loc, suite_val,
                         "discrepant (stale referent; note 1)"))
        elif p_ == "RESULTS.md" and lineage and any(
                i == ln_ and c == lineage for i, c in res_blame):
            ok_ = bool(lin.get("exit") == 0 and lin.get("summary") and
                       lin["summary"][0] == lin["summary"][1] == 103)
            stab.append(("103/103 (dated entry)", loc, lin_val,
                         "reproduced (at the entry's own commit)" if ok_
                         else "discrepant"))
    for i, x in sc_sum:
        stab.append(("%s (site check)" % x.split()[0],
                     "%s@%s:%d" % (a.sitecheck, h7, i), suite_val,
                     "reproduced (analysis.py blob equal at its base, its "
                     "commit and --ref)" if sc_equal else
                     ("discrepant" if comparable else
                      "not compared (blob differs)")))
    for i, x in find_lines(pf_lines, "The suite at HEAD prints"):
        m_ = re.search(r"(\d+/\d+)", x[x.find("The suite at HEAD"):])
        same_ = bool(pf_blob and ref_blob and pf_blob == ref_blob)
        stab.append(("%s (preflight, 'at HEAD' = %s)"
                     % (m_.group(1) if m_ else "?", (pf_rev or "?")[:7]),
                     "%s@%s:%d" % (PREFLIGHT, PIN, i), suite_val,
                     "reproduced (analysis.py blob at %s equals --ref's)"
                     % (pf_rev or "?")[:7] if same_ and m_ and
                     sp and m_.group(1) == n_s else "discrepant"))
    py_v = rep["version_info"] if rep else None
    stab += [
        ("Python version", "%s ('record Python version')" % l68,
         "%s" % (".".join(str(x) for x in py_v) if py_v else "?"),
         "computed-new"),
        ("import list", "%s ('the import list that was needed')" % l68,
         "%s (non-stdlib packages in sys.modules at exit, hooked run); "
         "sufficient alone: %s (run (c))"
         % (", ".join("%s %s" % (t, d["module_version"]) for t, _r, d, _c, _f
                      in third) or "none", "yes" if iso_ok else "NOT SHOWN"),
         "computed-new"),
        ("reads outside the clone", "%s ('reading only committed "
         "artifacts')" % l68,
         "%d distinct path(s) (domain: the %d recorded events of hooked run "
         "(a), file events and code objects); untracked clone files read: %d"
         % (len({x[2] for x in outside}), len(rep["events"]) if rep else 0,
            len(untr_read)), "computed-new"),
        ("README references", "%s ('no path in the note or README "
         "points outside the clone')" % l68,
         "%d of %d resolve in the clone (domain: references extracted from "
         "README.md at --ref); flagged %d; resolving but needing material "
         "absent from a clone at run time %d"
         % (len(rows) - len(problems), len(rows), len(problems),
            len(runtime_out)), "computed-new"),
        ("the note's paths", "%s ('no path in the note')" % l68,
         "%s is %s" % (NOTE, "present (paths not yet checked)" if note_here
                       else "not at the repository root or in archive/"),
         "computed-new" if note_here else "not found"),
        (".gitattributes filter on checkout", l68,
         "clone exit %d, checkout exit %d; %d warning line(s); tree clean "
         "after checkout: %s; notebook blob identical: %s"
         % (rc, rc2, len(warn_lines), "yes" if clean_after_checkout else "no",
            "yes" if nb_ok else "no"), "computed-new"),
        ("scipy need", ", ".join(scipy_loc) or "?",
         ("not needed at %s (%s with find_spec('scipy') None) nor at --ref"
          % ((lineage or "?")[:7], lin_val.split(" from")[0])
          if scipy_free_then and iso_ok else "not settled (note 6)"),
         "computed-new"),
        ("103 -> %s lineage" % (sp[1] if sp else "?"), "(2e)",
         ("%d identical / %d changed / %d removed / %d added (domain: check "
          "labels of the suite runs at %s and --ref)"
          % (len(cmp_["same"]), len(cmp_["diff"]), len(cmp_["old_only"]),
             len(cmp_["new_only"]), (lineage or "?")[:7]))
         if cmp_ else "not computed", "computed-new"),
    ]
    for needle in ("/Users/", "/workspace/"):
        _, gc, _ = sh(["git", "-C", REPO, "grep", "-I", "-c", "-F", needle,
                       h, "--"])
        per = [int(x.rsplit(":", 1)[1]) for x in gc.splitlines()
               if x.rsplit(":", 1)[-1].isdigit()]
        stab.append(("%r grep" % needle, "(3); N12 lists them",
                     "%d file(s), %d line(s) (domain: tracked text files at "
                     "--ref)" % (len(per), sum(per)), "computed-new"))
    o("figure | named in (locator) | value here | status")
    for row in stab:
        o(" | ".join(row))
    o()

    # ---- verdict ------------------------------------------------------------
    pass_conj = [
        ("(a) clone exit 0 and checkout exit 0 (the filter reference does "
         "not break checkout; block :68)", rc == 0 and rc2 == 0),
        ("(b) clone HEAD equals --ref after the checkout", head_c == h),
        ("(c) suite prints N/N with N stated, zero [FAIL], exit 0 (hooked, "
         "plain and literal runs (a), (b), (d), identical stdout; block "
         ":68/:70 with N for 103, note 1)", suite_ok),
        ("(d) reading only committed artifacts (block :68): no reads outside "
         "the clone apart from the interpreter's own installation and temp "
         "files the suite itself created (a read in the base environment's "
         "site-packages, or anywhere else under the base prefix outside its "
         "stdlib and the allow-list of the interpreter binary and "
         "<base prefix>/lib's shared libraries, counts as outside), and no "
         "untracked clone file read",
         rep is not None and not outside and not untr_read),
        ("(e) N is not reduced by an absent artifact: no existence test "
         "inside the clone returned False for a path present in this "
         "machine's working tree, no existence test fell outside the clone, "
         "the interpreter's installation and suite temp, and N equals the "
         "committed site check's N where analysis.py's blob is the same",
         guard_ok),
    ]
    fix_items = [
        ("no warning/error in clone or checkout output", not warn_lines),
        ("tree clean after checkout (git status --porcelain empty)",
         clean_after_checkout),
        ("tracked notebooks hash to their committed blobs without the filter",
         nb_ok),
    ]
    o("## Verdict")
    o()
    o("Pass conjuncts (block :68 'must print 103/103 reading only committed "
      "artifacts' and :70 'Pass: 103/103 from a fresh clone', with N/N in "
      "place of 103 per note 1; a failure here is the block's STOP on the "
      "release):")
    for name, ok in pass_conj:
        o("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    o("README-fix items (block :68: if checkout emits warnings, 'the README "
      "says so and gives the one-line fix'; they do not decide N11):")
    for name, ok in fix_items:
        o("  [%s] %s" % ("ok" if ok else "README FIX REQUIRED", name))
    o("Import-list record (block :68 'record ... the import list that was "
      "needed'; supporting, not a pass conjunct):")
    o("  [%s] isolated run (c): numpy as the only reachable non-stdlib "
      "package gives the same summary and byte-identical stdout"
      % ("ok" if iso_ok else "NOT SHOWN"))
    o("Descriptive:")
    o("  tree clean after all four runs: %s" %
      ("yes" if por2.strip() == "" else "NO"))
    if sp:
        o("  suite summary: %d/%d (the block and README.md say 103/103; see "
          "the 103/103 list in (3))" % (sp[0], sp[1]))
    o("  README references flagged: %d (listed in (3))" % len(problems))
    allok = all(ok for _, ok in pass_conj)
    fixes = [n for n, ok in fix_items if not ok]
    o()
    if allok:
        o("N11: PASS at %s, provisional -- pre-tag (no release tag exists "
          "yet); cloned from %s, not from the published remote; and resting "
          "on the design seat and the PI accepting N/N (here %d/%d) in place "
          "of the block's 103/103 (note 1), which is Code's reading, not a "
          "ruling. The suite prints %d/%d from the fresh clone with no read "
          "outside the clone apart from the interpreter's own installation "
          "and its own temp files. The block's pass is evaluated by "
          "re-running with --ref <tag> (note 2).%s"
          % (h, a.source, sp[0], sp[1], sp[0], sp[1],
             "" if not fixes else " README fix required: %s." %
             "; ".join(fixes)))
    else:
        o("N11: STOP on the release -- failed: %s"
          % "; ".join(n for n, ok in pass_conj if not ok))
    o()

    # ---- values-check dispositions ------------------------------------------
    hand = globinfo.get("HANDOFF-*.md", {})
    finds = globinfo.get("FINDINGS*.md", {})

    def newest(gi):
        d = sorted((v[0], f) for f, v in gi.get("adds", {}).items() if v)
        return d[-1][1] if d else "?"
    vc = [
        ("1", "Raw line 11 overclaimed byte-for-byte regeneration apart from "
         "the stamp: the --ref echo, the command line and the scratch paths "
         "also differ on a checker's re-run.",
         "fixed", "The header's 'Regeneration' line now names every line "
         "that can differ (stamp, run-time HEAD, --ref echo, work root, "
         "command, the clone's pre-detach branch line, and the lines labelled "
         "as this machine's working-tree state). Scratch paths outside the "
         "header print as <workroot>, and the default --ref is now the "
         "block's commit, so a re-run with the defaults echoes the same sha."),
        ("2", "'newest tracked by name: FINDINGS.md' was wrong: ASCII order "
         "puts FINDINGS.md last, but it is the oldest synthesis.",
         "fixed", "A glob's newest tracked match is now chosen by the commit "
         "that added it at --ref (git log --diff-filter=A): FINDINGS*.md -> "
         "%s; HANDOFF-*.md -> %s. Untracked matches are ranked by the date "
         "in their names, and only when every name carries one. Note 5 "
         "is added: README.md's synthesis chain omits %s."
         % (newest(finds), newest(hand), ", ".join(f_unlinked) or "nothing")),
        ("3", "'README.md at --ref: 74 line(s)' was wrong; the file has 73.",
         "fixed", "Lines are now counted with splitlines(): %d." % len(rdl)),
        ("4", "The scope sentence said no GIT_* variable other than "
         "GIT_CONFIG_GLOBAL and GIT_CONFIG_NOSYSTEM was set; "
         "GIT_TERMINAL_PROMPT=0 is also set.",
         "fixed", "The sentence now lists GIT_TERMINAL_PROMPT=0."),
        ("5", "Under 'N/N' alone, a clone that silently drops "
         "os.path.exists-guarded checks (analysis.py@bbc9ffe:396, :557, :593, "
         ":639, :653) would still pass.",
         "fixed", "Pass conjunct (e) is added. The hooked run records every "
         "os.path.exists/lexists/isfile/isdir result (the wrapper returns "
         "the real result; stdout stays byte-identical to the plain run). "
         "Here: %d (path, test) pairs inside the clone, %d False, %d of "
         "those present in this machine's working tree; %d existence "
         "test(s) outside the clone in class OUTSIDE. N is also compared "
         "with the committed site check's N when analysis.py's blob is the "
         "same at the site check's base, at its commit and at --ref "
         "(comparable: %s; equal: %s)."
         % (n_q_in, len(q_false), len(q_false_wt), len(q_outside),
            "yes" if comparable else "no", "yes" if sc_equal else "no")),
        ("6", "Filter warnings, a dirty tree after checkout and a notebook "
         "mismatch were STOP conjuncts. That is stricter than the block, "
         "whose remedy for warnings is a README line (:68).",
         "fixed", "They are now 'README-fix items' that do not decide N11. "
         "The pass conjuncts are clone/checkout success, HEAD = --ref, N/N, "
         "reading only committed artifacts, and (e). 'Tree clean after all "
         "runs' is descriptive."),
        ("7", "Calling 'N/N with N printed' the routed pass condition was "
         "unsupported: no design-seat or PI record adopts it.",
         "fixed", "Note 1 now attributes it to Code: the block's preamble "
         "(%s) and Code's preflight raw (%s), flagged for the design seat "
         "and the PI, not a ruling. The word 'routed' is dropped from "
         "Code's summary."
         % (", ".join("%s@%s:%d" % (BLOCK, PIN, i) for i, _ in b3) or "?",
            "%s@%s:%s" % (PREFLIGHT, PIN, "-".join(str(i) for i, _ in
                                                     (pfl[:1] + pfl[-1:])))
            if pfl else "?")),
        ("8", "The unqualified 'N11: PASS' line overclaimed: no tag exists "
         "yet, and the clone source was the local repository.",
         "fixed", "The verdict line now says provisional, pre-tag, and "
         "names the clone source. A --source option is added for the "
         "re-run from the published remote; it was not exercised against a "
         "remote here, because this audit makes no network access."),
        ("9", "'The third-party import list is what a reader's own "
         "interpreter needs' was unsupported: the suite was never run "
         "without the venv's other packages.",
         "fixed", "Isolated run (c) is added: -S -E -s, with numpy the only "
         "non-stdlib package reachable, through a symlink shim, plus a "
         "negative control on the venv's other top-level names. Result: "
         "%s. Note 6 is reworded and cites %s for the earlier "
         "numpy+scipy install (round 2, item 1, corrects this disposition's "
         "first wording, 'need', to 'install'). The checker's locator "
         ":11592-11594 is corrected to the lines that say it."
         % ("sufficient, %d/%d" % (si[0], si[1]) if iso_ok else "NOT shown",
            ", ".join(scipy_loc) or "?")),
        ("10", "The raw hid the suite's leftover mkdtemp directory: the "
         "script deletes its whole scratch TMPDIR.",
         "fixed", "Section (2) now lists what the runs left in TMPDIR "
         "before cleanup (in this version, after four runs: %d "
         "director(ies), each with d.json.checkpoint), "
         "and note 8 gives the sentence for README-NOTE item (3)."
         % len(resid_dirs)),
        ("11", "'NOT present on this machine' overclaimed: the script "
         "searched only the repository root and archive/.",
         "fixed", "The wording is now 'not present at the repository root or "
         "in archive/'. Nothing outside the repository is searched or "
         "reported in this raw."),
        ("12", "The os.walk observation (analysis.py@bbc9ffe:809-821, "
         ":1192-1201) was in the builder's summary only, not in the raw.",
         "fixed", "It is now note 7, with the os.walk lines located by the "
         "script."),
        ("13", "The default --workroot was the builder's scratch, so a "
         "checker who passes only --out clones into it and deletes there.",
         "fixed", "When --out is not the default, --workroot now defaults "
         "to <dir of --out>/N11-work. A work root inside the repository is "
         "refused. Stale entries are removed only under their fixed names "
         "(clone-, tmp-, numpy-shim-<sha12>, hook reports)."),
    ]
    o("## Values-check, round 1 (findings on pass 1, scripts/"
      "audit_note_N11.py sha256 c77c55d3...a914; dispositions applied from "
      "sha256 339c8a49...b766 on, and carried in this version)")
    o()
    for num, claim, disp, how in vc:
        o("%s. %s" % (num, claim))
        o("   Disposition: %s. %s" % (disp, how))
    o()
    o("Also changed by Code in round 1 (found while re-running and "
      "re-reading, not checker findings): (i) git's progress meter "
      "('Updating files: NN%% ...') appeared in clone's stderr on one run and "
      "not on others, which breaks regeneration, so meter lines are left out "
      "of the display by a fixed pattern while the warning scan still reads "
      "them; (ii) under -S, sys.prefix is the base prefix, so the isolated "
      "run's paths are classified with the hooked run's sys.prefix (the "
      "first draft wrongly classed numpy as OUTSIDE there); (iii) code-object "
      "pseudo-filenames ('<frozen ...>', '<string>') passed to "
      "os.path.exists during the run are excluded from conjunct (e)'s path "
      "pairs and listed separately; (iv) existence tests outside the clone are "
      "classified, and any in class OUTSIDE would fail (e) (here %d); (v) "
      "the work-root check now runs before the directory is created, so a "
      "refused path is never made inside the repository (tested: refused, "
      "nothing created); (vi) note 7 quotes the walk and skip lines from the "
      "--ref source instead of paraphrasing them; notes 6 and 8 now follow "
      "from the run's own counts." % len(q_outside))
    o()
    o("The round-1 checker's independent recomputations, as relayed to "
      "Code: the suite summary (154/154 in four configurations, numpy-only "
      "among "
      "them), the clean clone and checkout, the notebook blob, OUTSIDE = 0, "
      "the hook's class table, the 18 data/ reads, the 30 executed and 98 "
      "scanned .py files, the import list and the Python version each agreed "
      "with the previous raw. The last item (the hidden .pth files) was cut "
      "off in the relay, so its verdict is not stated here; this raw "
      "re-derives it in (2). None of these needed a disposition.")
    o()

    # ---- values-check, round 2 -------------------------------------------
    # synthetic classification test for item R2-6 (no file is touched)
    cls_test = []
    if rep and classify:
        bsp_ = base_site_packages(rep)
        std_ = rep["paths"]["stdlib"]
        if bsp_:
            cls_test.append((os.path.join(bsp_[0], "somepkg", "__init__.py"),
                             BASE_SP))
        cls_test.append((os.path.join(std_, "os.py"), "interpreter: stdlib"))
        cls_test.append((os.path.join(rep["paths"]["purelib"], "numpy",
                                      "__init__.py"),
                         "interpreter: venv (sys.prefix)"))
        cls_test = [(p_, want, classify(p_)[0]) for p_, want in cls_test]
    n_bsp_all = sum(len(v) for (cat, _rw), v in cats.items() if cat == BASE_SP)
    pu_ign = [x for x in pu if "ignore" in x[0]]
    l7_ = (lineage or "?")[:7]
    vc2 = [
        ("1", "Note 6 overclaimed: it said the earlier 103/103 entry "
         "'needed' scipy; %s records an install, not a need."
         % (", ".join(scipy_loc) or "?"),
         "fixed", "Note 6 now says the entry installed scipy, and states "
         "what the run computes about the need: %s. The text is built from "
         "(2e)'s own results, not hard-coded."
         % ("not needed then either -- at %s no tracked .py file imports "
            "scipy (%d mention(s), none an import), find_spec('scipy') is "
            "None under this interpreter (-E -s: %s; no flags: %s), and a "
            "fresh clone at %s prints %s with exit %s"
            % (l7_, len(scipy_grep), scipy_none_flags, scipy_none_lit, l7_,
               "%d/%d" % lin["summary"][:2] if lin.get("summary") else "?",
               lin.get("exit"))
            if scipy_free_then else "NOT settled (see note 6)")),
        ("2", "The raw did not show how the 103 checks relate to the 154.",
         "fixed", "Section (2e) is added: git blame at %s names %s as the "
         "commit that wrote README.md's 103/103; a second fresh clone there "
         "prints %s; the check labels are compared (%s). Note 1 carries the "
         "summary for README-NOTE item (3)."
         % (PIN, l7_, ("%d/%d (exit %s)" % (lin["summary"][0],
                                             lin["summary"][1], lin["exit"]))
            if lin.get("summary") else "no summary line",
            ("%d identical, %d changed, %d not at --ref, %d added after"
             % (len(cmp_["same"]), len(cmp_["diff"]), len(cmp_["old_only"]),
                len(cmp_["new_only"]))) if cmp_ else "not compared")),
        ("3", "The statuses (reproduced, discrepant, computed-new) were in the "
         "builder's chat summary, not in the raw.",
         "fixed", "A 'Figure statuses' table, emitted by the script, now "
         "precedes the verdict: %d rows (figure | named in | value here | "
         "status), with N1's vocabulary located at %s." %
         (len(stab), ", ".join("%s@%s:%d" % (BLOCK, PIN, i)
                               for i, _ in st_loc) or "?")),
        ("4", "'The only config in effect besides the repository's "
         ".gitattributes' was wider than the run: GIT_CONFIG_GLOBAL=/dev/null "
         "does not turn off git's default excludes file, "
         "~/.config/git/ignore, which exists here.",
         "fixed", "By neutralising, not only rewording: every git command on "
         "a clone now runs with HOME and XDG_CONFIG_HOME set to an empty "
         "scratch directory, so the default excludes and attributes files "
         "resolve to paths that do not exist. Section (1) lists this "
         "machine's per-user git files by presence and line count only "
         "(%s), the origins 'git config --list --show-origin' reports on the "
         "clone (%s), the clone's info/exclude, info/attributes and live "
         "hooks, and the sentence about the inputs in effect is printed only "
         "when those checks hold (here: %s). Ignored entries after the runs "
         "under this environment: %d, of which not __pycache__: %d. The "
         "empty directory stayed empty: %s."
         % ("; ".join("%s: %s" % (x[0].split(" (")[0],
                                  ("present, %s line(s)" % x[3]) if x[2]
                                  else "absent") for x in pu_ign) or "-",
            origins, "yes" if git_inputs_clean else "NO", len(ig),
            len(ig_nonpyc), "yes" if home_left == [] else "NO")),
        ("5", "The README's literal command (README.md:55, block :68) was "
         "never run; all three runs used -E -s, and this environment sets "
         "PYTHONDONTWRITEBYTECODE.",
         "fixed", "Run (d) is added: the literal command, no flags, cwd = the "
         "clone root: exit %d, summary %r, stdout byte-identical to (b): %s. "
         "Section (2) lists the PYTHON* variable names in the inherited "
         "environment (%s) and probes the user site and bytecode setting "
         "under the same configuration. Conjunct (c) now requires (d) too."
         % (rcl, sl[2].strip() if sl else None,
            "yes" if lso == pso else "NO", py_env_names or "none")),
        ("6", "classify() put the base environment's site-packages, which sits "
         "inside the stdlib directory, into 'interpreter: stdlib', so a read "
         "there would not have counted as OUTSIDE.",
         "fixed", "classify_factory now tests the base environment's "
         "site-packages (%s) before the stdlib class, as its own class '%s', "
         "which conjunct (d), the code-object list, the import split and the "
         "existence tests all count as outside. Here: %d event(s) in that "
         "class. Synthetic paths (classified, no file touched): %s."
         % (base_site_packages(rep) if rep else "?", BASE_SP, n_bsp_all,
            "; ".join("%s -> %r (%s)" % (p_, got, "as expected" if got == want
                                         else "EXPECTED %r" % want)
                      for p_, want, got in cls_test) or "not run")),
        ("7", "The heading said 'block §0 preamble'; the clause is in the "
         "block's italic preamble at :3, before §0 (:7).",
         "fixed, in part", "The heading now cites the preamble line the "
         "script locates (%s). The suggested wording also named 'the PI's "
         "routing' as a source of the rule; that part is not adopted, because "
         "no record line Code can cite states it -- the block's preamble "
         "does, and the heading cites that."
         % (", ".join("%s@%s:%d" % (BLOCK, PIN, i) for i, _ in pre3) or "?")),
        ("8", "The verdict line named the pre-tag and clone-source provisos "
         "but not that the pass rests on the design seat and the PI accepting "
         "N/N in place of the block's 103/103.",
         "fixed", "The verdict line now names all three provisos."),
        ("9", "README.md:60's 'valence_core.regression.oracle' was counted as "
         "resolving with no word that its tier needs material outside a "
         "clone.",
         "fixed", "The row now carries the runtime dependency, computed from "
         "oracle.py and qwen_mlx.py at --ref, (3) counts such references "
         "separately (%d), and note 10 records it for README-NOTE. It stays "
         "unflagged as a path: the reference resolves, and the block's check "
         "is about paths." % len(runtime_out)),
    ]
    o("## Values-check, round 2 (findings on pass 2, scripts/"
      "audit_note_N11.py sha256 339c8a49...b766; dispositions applied from "
      "sha256 b1c66f3b...b8cd on, and carried in this version)")
    o()
    for num, claim, disp, how in vc2:
        o("R2-%s. %s" % (num, claim))
        o("   Disposition: %s. %s" % (disp, how))
    o()
    o("Also changed by Code in round 2 (not checker findings): (i) the "
      "header's Regeneration line names the new machine-state lines "
      "(per-user git files, PYTHON* names, the user-site probe); (ii) "
      "round 1's disposition 9 said "
      "'numpy+scipy need' and now says 'install', in line with R2-1; "
      "(iii) round 1's disposition 10 no longer says 'three runs'; (iv) "
      "the stale-scratch removal and the cleanup cover the new scratch "
      "names (lineage-clone-, lineage-tmp-, empty-home-<sha12>), and the "
      "header's Work root line names them.")
    o()
    o("The round-2 checker's independent recomputations, as relayed to Code "
      "(not re-derived here beyond what this raw computes): a fresh clone "
      "of bbc9ffe without global or system git config, clean and without "
      "warnings; the notebook's blob; 154/154 in four configurations with "
      "byte-identical stdout (the literal README command, the checker's own "
      "audit-hooked run, a numpy-only run, the builder's runs); its own "
      "audit hook's class table (1182 comparable events; 176 clone files "
      "opened: 18 data/, 30 executed and 98 scanned .py, 30 bytecode; 0 "
      "reads outside, 0 under jlens-qwen36/ outside .venv, 0 under the base "
      "environment's site-packages); numpy 2.5.1 as the only third-party "
      "package; module counts 260 / 110; 26 existence pairs, all True; the "
      "greps (103/103 in 4 files on 7 lines; /Users/ 90 files, 208 lines; "
      "/workspace/ 139 files, 274 lines); 30 of 31 README references "
      "resolving; and every pinned locator. None of these needed a "
      "disposition.")
    o()

    # ---- values-check, round 3 -------------------------------------------
    # synthetic classification test for item R3-2 (no file is touched)
    cls3 = []
    if rep and classify:
        bp_ = rep["base_prefix"]
        vi_ = rep.get("version_info") or [3, 12]
        cls3 = [
            (os.path.join(bp_, "envs", "n11-synthetic", "lib",
                          "python%d.%d" % tuple(vi_[:2]), "site-packages",
                          "somepkg", "__init__.py"), BASE_OTHER),
            (os.path.join(bp_, "pkgs", "n11-synthetic", "info", "index.json"),
             BASE_OTHER),
            (os.path.join(bp_, "share", "zoneinfo", "UTC"), BASE_OTHER),
            (os.path.join(bp_, "lib", "n11-synthetic", "libx.dylib"),
             BASE_OTHER),
            (os.path.join(bp_, "lib", "libpython%d.%d.dylib"
                          % tuple(vi_[:2])), BASE_ALLOW),
            (os.path.realpath(rep["executable"]), BASE_ALLOW),
        ]
        cls3 = [(p_, want, classify(p_)[0]) for p_, want in cls3]
    rtp, rtf = next(iter(rt_facts.items()), (None, None))
    q_ = "valence_core/adapters/qwen_mlx.py"
    twins = ["%s@%s:%d -> %s" % (f, l7_, i, ", ".join(
        "%s@%s:%d" % (f, h7, j) for j in scipy_twin.get((f, i)) or [])
        or "no identical line at --ref") for f, i, _t in scipy_grep]
    vc3 = [
        ("1", "'So the git inputs in effect on the clone are its .git/config "
         "... no per-user or system file applies' (:69 of the previous raw) "
         "was imprecise: "
         "GIT_CONFIG_NOSYSTEM=1 turns off the system config only, and git "
         "still read the system gitattributes file of the git in use (three "
         "diff-driver lines, *.m, *.mm, *.swift); git_inputs_clean checked "
         "config origins, info/exclude, info/attributes and hooks, not that "
         "file.",
         "fixed", "By neutralising and reporting: git_env() now also sets "
         "GIT_ATTR_NOSYSTEM=1 (named in the module docstring, git_env's "
         "docstring and the scope line). Section (1) now reports the file: "
         "%d candidate(s) located beside the system-level config files git "
         "names, %d present (%s non-comment line(s)); a probe of %d name(s) "
         "built from its '*.<ext>' patterns gets an attribute from it in %d "
         "case(s) when GIT_ATTR_NOSYSTEM is absent and in %d under the "
         "script's environment; over the %d tracked paths at --ref it changes "
         "the attributes of %d. git_inputs_clean now also requires "
         "GIT_ATTR_NOSYSTEM=1 and a zero probe count under the environment "
         "(here: %s)."
         % (len(sar["cands"]), sum(1 for x in sar["cands"] if x[1]),
            "/".join(str(x[2]) for x in sar["cands"] if x[1]) or "-",
            sar["n_probes"], sar["probe_on"], sar["probe_off"],
            sar["n_tracked"], len(sar["changed"]),
            "yes" if git_inputs_clean else "NO")),
        ("2", "Conjunct (d) counted a read anywhere under the base prefix "
         "outside its stdlib and site-packages -- for example another conda "
         "environment under envs/ -- as the interpreter's installation "
         "(class 'interpreter: base prefix (other)', not in "
         "OUTSIDE_CLASSES): listed, but not failing (d).",
         "fixed", "Such a read is now class '%s', in OUTSIDE_CLASSES, so "
         "conjunct (d), the code-object list, the existence tests of (e) and "
         "the import split all count it as outside. Only a small allow-list "
         "under the base prefix stays the interpreter's, class '%s': the "
         "interpreter binary (the realpath of sys.executable) and the shared "
         "libraries directly in <base prefix>/lib (*.dylib, *.so*). Both "
         "classes' counts are printed in (2) even when 0; here: hooked run "
         "%s and %s event(s), isolated run %s and %s. Synthetic paths "
         "(classified, no file touched): %s."
         % (BASE_OTHER, BASE_ALLOW, n_bo, n_ba, iso_bo, iso_ba,
            "; ".join("%s -> %r (%s)" % (p_, got, "as expected" if got == want
                                         else "EXPECTED %r" % want)
                      for p_, want, got in cls3) or "not run")),
        ("3", "Note 6 and (2e) located the scipy mention at "
         "valence_core/stats.py@0dd6f56:3 only; the bbc9ffe twin was in the "
         "fixer's chat summary, not in the raw.",
         "fixed", "The 0dd6f56 locator stays, because the claim is about "
         "that tree (%s is an ancestor of --ref: %s, computed in (2e)). "
         "(2e)'s scipy line and note 6 now add, for each mention, the "
         "identical line at --ref, found by reading the file at --ref: %s."
         % (l7_, "yes" if lin_anc else ("NO" if lin_anc is not None
                                        else "not computed"),
            "; ".join(twins) or "no mentions")),
        ("4", "Note 10 and the README.md:60 row did not name qwen_mlx.py's "
         "import of mlx.core, and placed the RuntimeError at the import, not "
         "at the adapter's construction.",
         "fixed" if rtf else "NOT applied",
         ("The row and note 10 are rebuilt from the --ref sources: "
          "%s@%s:%s imports mlx.core (%s); the RuntimeError (:%s) is raised "
          "by _ensure_clone_on_path(), which runs at :%s, inside %s, so when "
          "the adapter is constructed -- %s@%s does that at %s -- and not "
          "when it imports the module (:%s)%s."
          % (q_, h7, ",".join(str(i) for i in rtf["mlx"]) or "?",
             rtf["mlx_desc"],
             ",".join(str(i) for i in rtf["rais"]) or "?",
             ",".join(str(i) for i, _ in rtf["calls"]) or "?",
             "/".join(sorted({d for _, d in rtf["calls"]})) or "?",
             rtp, h7,
             " and ".join(":%d" % i for i in rtf["cons"]) or "?",
             ",".join(str(i) for i in rtf["imp"]) or "?",
             "" if rtf["only_init"] else
             " (NOT shown that the module calls it only there)"))
         if rtf else "runtime_dep located no README module that imports "
         "the Qwen adapter, so there was nothing to rebuild."),
    ]
    o("## Values-check, round 3 (findings on pass 3 -- the audit workflow's "
      "round-4 fix list -- of scripts/audit_note_N11.py sha256 "
      "b1c66f3b...b8cd; dispositions applied in this version)")
    o()
    for num, claim, disp, how in vc3:
        o("R3-%s. %s" % (num, claim))
        o("   Disposition: %s. %s" % (disp, how))
    o()
    o("Also changed by Code in round 3 (not checker findings): (i) the "
      "header's Regeneration line names the system gitattributes lines of "
      "(1) as machine state; (ii) the scope line names the two check-attr "
      "measurements that drop GIT_ATTR_NOSYSTEM and the two config-origin "
      "queries that run outside a clone; (iii) round 2's heading now says "
      "where its dispositions were first applied (sha256 b1c66f3b...b8cd), "
      "as round 1's does.")
    o()
    o("The round-3 checker's independent recomputations, as relayed to "
      "Code in its findings' evidence (not re-derived here beyond what this "
      "raw computes): under the previous version's git environment "
      "(GIT_CONFIG_GLOBAL=/dev/null, GIT_CONFIG_NOSYSTEM=1, HOME and "
      "XDG_CONFIG_HOME an empty directory; no GIT_ATTR_NOSYSTEM), in a fresh "
      "clone at bbc9ffe, git check-attr -a on foo.m and foo.swift returns "
      "'diff: objc' and 'diff: swift', and nothing once GIT_ATTR_NOSYSTEM=1 "
      "is added, from /usr/bin/git 2.39.5 (Apple Git-154); 0 tracked paths "
      "at bbc9ffe "
      "match *.m, *.mm or *.swift, and git check-attr --stdin diff over "
      "the clone's ls-files returns no specified value; its own audit hook, "
      "independent of WRAPPER, on a fresh clone found 0 events under the "
      "base prefix outside the stdlib and site-packages; 0dd6f56 is an "
      "ancestor of bbc9ffe; the stats.py line is at "
      "valence_core/stats.py@bbc9ffe:3; qwen_mlx.py@bbc9ffe:72 imports "
      "mlx.core, and the adapter is constructed at oracle.py@bbc9ffe:559. "
      "Its findings report no changed number.")

    # scratch paths -> <workroot> outside the header
    subs = sorted({wr_real, a.workroot.rstrip(os.sep)}, key=len, reverse=True)
    for i in range(n_header, len(o.lines)):
        for s_ in subs:
            o.lines[i] = o.lines[i].replace(s_, "<workroot>")

    os.makedirs(os.path.dirname(out_real), exist_ok=True)
    with open(out_real, "w") as fh:
        fh.write("\n".join(o.lines).rstrip("\n") + "\n")
    print("wrote %s (%s)" % (out_real, "PASS" if allok else "STOP"),
          file=sys.stderr)
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
