#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N13: the pre-registration provenance table.

Read-only on the record. Every figure is computed from git at a pinned commit
(default bbc9ffe): document versions (git log --follow), commit dates (git's
author and committer times, printed in UTC), content sha256 recomputed from
`git show <commit>:<path>`, the commits that first recorded a version's hash
(git log -S pickaxe over every tracked path except *.npz and this audit's own
files; git log --grep over commit messages), the first commit adding each
governed cell's data artifact or run raw (and every commit that only modifies
such a file with model output, classified commit by commit), run stamps and
recorded-HEAD lines inside those artifacts, ancestry (git merge-base
--is-ancestor), gaps in days, and the hunks between document versions
(git diff -U0). Each cell carries its tier (verdict or not) with the line of the
governing text it rests on. Quoted record text is redacted at write time
(RunPod ids, volume names, container ids, SSH ports; matched by sha256 prefix).

Git subcommands used: rev-parse, log, show, blame, grep, merge-base
--is-ancestor, rev-list, ls-tree, diff. Nothing is written except --out and
--json-out. No model is loaded; nothing is installed or downloaded.

Values-check passes 1 to 4 (adversarial checker) are applied in this version;
the raw's last section lists each finding and its disposition, pass by pass.

Usage (from the repository root):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N13.py \
      [--ref bbc9ffe] [--out PATH] [--json-out PATH]
"""
import argparse
import datetime as dt
import difflib
import fnmatch
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA_ROUTED = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
DEFAULT_OUT = "results/raw/2026-10-08_note-N13-provenance.md"
DEFAULT_JSON = "results/raw/2026-10-08_note-N13-provenance.json"
ENV = dict(os.environ, LC_ALL="C", GIT_OPTIONAL_LOCKS="0", GIT_PAGER="cat", TZ="UTC")
ALLOWED_GIT = {"rev-parse", "log", "show", "blame", "grep", "merge-base", "rev-list", "ls-tree", "diff"}


def clip(s, n):
    """Cut s to at most n characters at a word boundary, marking any cut with ' [...]'."""
    s = "" if s is None else str(s)
    if len(s) <= n:
        return s
    cut = s[:n]
    sp = cut.rfind(" ")
    if sp > n // 2:
        cut = cut[:sp]
    return cut.rstrip(" ,;:") + " [...]"


def nfiles(n):
    return "1 file" if n == 1 else "%d files" % n


def more(items, k, where):
    """Render up to k items, then '(+N more; full list in JSON <where>)'."""
    items = list(items)
    s = ", ".join(items[:k])
    if len(items) > k:
        s += " (+%d more; full list in JSON `%s`)" % (len(items) - k, where)
    return s

# --------------------------------------------------------------------------
# git helpers (read-only)
# --------------------------------------------------------------------------

def git(*args, binary=False, check=True):
    if args[0] not in ALLOWED_GIT:
        raise RuntimeError("git subcommand not allowed: %s" % args[0])
    if args[0] == "merge-base" and "--is-ancestor" not in args:
        raise RuntimeError("merge-base only with --is-ancestor")
    p = subprocess.run(["git", "-C", REPO, "--no-pager", *args],
                       capture_output=True, env=ENV)
    if check and p.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), p.stderr.decode()[:400]))
    return p.stdout if binary else p.stdout.decode("utf-8", "replace")


def utc(ts):
    return dt.datetime.fromtimestamp(int(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def local_edt(ts):
    return dt.datetime.fromtimestamp(int(ts), dt.timezone(dt.timedelta(hours=-4))).strftime("%Y-%m-%d %H:%M")


_META = {}


def meta(c):
    if c in _META:
        return _META[c]
    out = git("log", "-1", "--format=%H%x00%an%x00%at%x00%ct%x00%aI%x00%cI%x00%s", c)
    h, an, at, ct, ai, ci, s = out.rstrip("\n").split("\x00")
    m = {"commit": h, "short": h[:7], "author": an,
         "author_unix": int(at), "committer_unix": int(ct),
         "author_utc": utc(at), "committer_utc": utc(ct),
         "author_iso_own_tz": ai, "committer_iso_own_tz": ci,
         "subject": s}
    _META[c] = m
    _META[h] = m
    return m


def is_ancestor(a, b):
    p = subprocess.run(["git", "-C", REPO, "merge-base", "--is-ancestor", a, b],
                       capture_output=True, env=ENV)
    return p.returncode == 0


def show_bytes(c, path):
    return git("show", "%s:%s" % (c, path), binary=True)


def exists_at(c, path):
    p = subprocess.run(["git", "-C", REPO, "rev-parse", "--verify", "-q", "%s:%s" % (c, path)],
                       capture_output=True, env=ENV)
    return p.returncode == 0


def sha256_at(c, path):
    return hashlib.sha256(show_bytes(c, path)).hexdigest()


def blob_at(c, path):
    return git("rev-parse", "%s:%s" % (c, path)).strip()


def lines_at(c, path):
    return show_bytes(c, path).decode("utf-8", "replace").split("\n")


def resolve(h):
    p = subprocess.run(["git", "-C", REPO, "rev-parse", "--verify", "-q", h + "^{commit}"],
                       capture_output=True, env=ENV)
    return p.stdout.decode().strip() if p.returncode == 0 else None


# --------------------------------------------------------------------------
# Configuration: what each pre-registration governs (declared; verified below)
# --------------------------------------------------------------------------
# Data rule (declared): a cell's data are the artifacts or run raws produced by
# forward passes of the subject model on the cell's stimuli. Model-free
# artifacts (power, budget, arithmetic, values-checks, frac tables, stub or
# synthetic selftests, replays of archived text) are not data under this rule;
# where one of them sits near a cell it is named in the cell's note. Analyses
# computed from forward outputs, including re-analyses committed without new
# forwards, are counted with the data (values-check pass 4, finding 3).

def T(label, path=None, needle=None, after=1, why="", also=(), log_only=False, call=None):
    """A cell's tier (values-check pass 2, finding 4): its label, and the line of the
    governing text it rests on (the first line at or after `after` in `path` at ref that
    contains `needle`). A cell is a verdict cell iff its label starts with 'verdict'.
    log_only (values-check pass 3, finding 4): the governing text does not name the cell,
    and the line is the log entry that reports the run. call (pass 3, finding 3): the id of
    a tier judgment call, whose counts under the other reading are computed."""
    return {"label": label, "path": path, "needle": needle, "after": after, "why": why,
            "also": [list(x) for x in also], "log_only": log_only, "call": call}


# The four tier judgment calls (section 7 item 2, section 8): id -> (what Code counts, the other reading)
CALLS = {"c1": ("(c) c1 r1/r2 counted as verdict", "as gate cells"),
         "dgate": ("the (d)/e1 G-gates counted as gates", "as verdict cells"),
         "a4": ("PROPOSAL-g A4 counted as verdict data", "as calibration cells"),
         "k1": ("PROPOSAL-k Stage 1 counted as a gate stage", "as a verdict cell")}

# Files in a row's same-subject list that are model-free under section 0's data rule (no
# forward of the subject model), each read with `git show` (values-check pass 3, finding 6).
# Counted apart from the data files. Every other same-subject file was read and is a
# forward-pass output or an analysis of one.
PRE_MODEL_FREE = {
    "data/olmo/manifest.json": "checkpoint manifest: pinned revisions and per-file SHA-256 of the bf16 weight files (75939ed; extended by 9cd324d)",
    "results/raw/2026-08-19_olmo_acquisition.txt": "download and bf16 cast log (load, save, purge; no forward)",
    "results/raw/2026-08-19_olmo_hashes.txt": "per-file SHA-256 hashing of the weight files",
    "data/olmo/cast_equality_sft.json": "cast-equality check: per-tensor digests of the stored bf16 cast against transformers' load-cast of the fp32 master ('n_per_tensor_mismatches': 0)",
    "results/raw/2026-08-19_cast_equality_sft.txt": "the cast-equality check's log (download, load, digest, compare; no forward)",
    "data/format/neutral_label_selection.json": "neutral-label selection: tokenizer token counts and roster/pool lexical checks (the entry: 'tokenizer loaded once, model process closed')",
}
# The log line a PRE_MODEL_FREE description quotes, located at ref when the raw is written.
PRE_MODEL_FREE_QUOTE = {"data/format/neutral_label_selection.json": ("RESULTS.md", "tokenizer loaded once, model process closed")}
# Same-subject files read in pass 3 that are close to the line and counted as data, with the reason.
PRE_DATA_BORDERLINE = {
    "data/echo/timing.json": "timings of steered and mask-off forwards on one session plus a budget projection; it records no model output, but it was produced by forward passes, so it is data under the rule",
}


def cell(name, globs, tier, exclude=(), note="", result_entry=None,
         inputs_only=False, log_run_time=None, bounded=()):
    """bounded: (glob, after_commit, upto_commit) -- the glob matches only additions in a
    commit that is a proper descendant of after_commit (None = no bound) and an
    ancestor of, or equal to, upto_commit (None = no bound). Used where one path is
    added twice by different runs (data/e2b/h1_sessions.json: H1-u at b2d051b,
    renamed away at d94e281, re-added by the H1 gate run at 7527270)."""
    return {"name": name, "globs": list(globs), "exclude": list(exclude),
            "verdict": tier["label"].startswith("verdict"), "tier": tier,
            "note": note, "result_entry": result_entry, "inputs_only": inputs_only,
            "log_run_time": log_run_time, "bounded": [list(b) for b in bounded]}


VERDICT_DEFINITION = (
    "A verdict cell (Code's definition, declared in values-check pass 2) is a cell whose data a registered verdict "
    "criterion is evaluated on: the verdict, primary, confirmatory, acceptance or screen outcome, as the governing text names it. "
    "Cells that the governing text places in a calibration or gate tier, or names as a smoke, dose-finding step, extraction, training input, "
    "exploration, attached reporting or a satellite that 'gates on nothing', are not verdict cells, even where they carry registered bars "
    "or readings. Where a log entry sits inside an arc whose proposal tiers its steps, the proposal's tier governs (the (d)/e1 G-gates are "
    "PROPOSAL-d §2's 'd1 gates'); where no proposal tiers the arc, the entry's own words govern. Where those words fire both clauses (L-c1's entry "
    "calls the full run 'the primary experiment' and its read a 'Pre-registered gate read' that c2 waits on), Code counts the cell as verdict and "
    "gives the counts under the other reading (section 7 item 2, section 8). Each cell's tier, and the line it "
    "rests on, are given in section 2 and in the JSON (`cells[].tier`); for four smoke cells (P-e's and L-e0B2c's e0 B2c smoke, P-h's and LOCK-h's "
    "e2b verdict-campaign smoke) the governing text does not name the smoke, and the line is the log entry that reports the run, marked [log-only]. "
    "Four calls are judgment calls, listed for the PI in section 8.")

# Commits that only modify (never add) a file matching a declared cell or pre-data path
# (values-check pass 2, finding 3). Each was read with `git show`; True = the modification
# carries output of a model forward and is counted as data, False = model-free.
MODIFY_CLASS = {
    "aed3b08": (True, "appends e2a run-2 output (a resume header, 8 session lines [2/200] to [16/200], one of them excluded, and the pause line) to results/raw/2026-08-09_e2a_full.txt"),
    "51f1e72": (True, "appends e2a run-3 output to results/raw/2026-08-09_e2a_full.txt; the commit also adds matching files"),
    "a274ecd": (True, "rewrites results/raw/2026-09-02_e2d_d2.txt with the D2 session run's output; the commit also adds matching files"),
    "db0d177": (True, "appends the Qwen oracle run's output (choice-read replay, kernel KLs, B2b subsample) to results/raw/2026-08-12_rule26_oracle.txt"),
    "7302384": (False, "appends a design-instance adjudication block to data/e0/s2_neighbor_axes.json; no forward"),
    "fffe104": (False, "appends an adjudication block (the roster of record) to data/e2b/h3b_repair_screen.json; no forward"),
    "c17337c": (False, "adds as-stored float32 sha16 fingerprints of the stored vectors to data/olmo/b2_concepts_{sft,dpo,instruct}.json (a verification aid); no forward"),
    "9cd324d": (False, "adds per-file SHA-256 of the bf16 weight files to data/olmo/manifest.json (hashing); no forward"),
}

# Redaction of quoted record text (routing rule 6): values are found by their sha256 prefix,
# never written here; each is replaced by first-4 + '...' + length + ':' + sha256[:8].
REDACT_TOKENS = [("uimu", 14, "a39ed293"), ("y5xy", 14, "d781dc45"), ("o73q", 10, "e79618f8"),
                 ("holy", 23, "e6c48186"), ("e20d", 12, "54719d1e")]
REDACT_PORT_SHA8 = ["dae17182", "25124cd5", "47e5fcc0", "2be8ef0e", "54e4496b"]


def redact(s):
    """Return (s with every matched value replaced, number of replacements)."""
    n = 0
    for pre, ln, h8 in REDACT_TOKENS:
        out, i = [], 0
        while True:
            j = s.find(pre, i)
            if j < 0:
                out.append(s[i:])
                break
            cand = s[j:j + ln]
            if len(cand) == ln and re.fullmatch(r"[A-Za-z0-9_\-]+", cand) and hashlib.sha256(cand.encode()).hexdigest().startswith(h8):
                out.append(s[i:j])
                out.append("%s...%d:%s" % (pre, ln, h8))
                n += 1
                i = j + ln
            else:
                out.append(s[i:j + 1])
                i = j + 1
        s = "".join(out)

    def port(m):
        nonlocal n
        h = hashlib.sha256(m.group(0).encode()).hexdigest()[:8]
        if h in REDACT_PORT_SHA8:
            n += 1
            return "len5:" + h
        return m.group(0)
    s = re.sub(r"(?<!\d)\d{5}(?!\d)", port, s)
    return s, n


A12 = "archive/RESULTS-cycle1-2.md"
A34 = "archive/RESULTS-cycles3-4.md"
RM = "RESULTS.md"
PD = "PROPOSAL-d-distilled-trace.md"
PF = "PROPOSAL-f-natural-reinforcer-screen.md"
PG = "PROPOSAL-g-ontogeny-of-evaluation.md"
PH = "PROPOSAL-h-state-present-choice.md"
PJ = "PROPOSAL-j-dose-escalation.md"
PK = "PROPOSAL-k-echo-channel.md"
AG1 = "ADDENDUM-g1-archival-reading-screen.md"
AG3 = "ADDENDUM-g3-b2r-v1.2.md"
LH = "LOCK-h.md"
LG = "LOCK-g.md"

E2A_GATES = ["results/raw/2026-08-09_e2a_g1*.txt", "results/raw/2026-08-09_e2a_g2*.txt",
             "results/raw/2026-08-09_e2a_g3.txt", "data/e2a/g1_kernel_gate.json",
             "data/e2a/g2_*.json", "data/e2a/g3_kv_leakage.json"]
E2A_SESS = ["results/raw/2026-08-09_e2a_g3prime.txt", "results/raw/2026-08-09_e2a_smoke*.txt",
            "results/raw/2026-08-09_e2a_ndecl.txt", "results/raw/2026-08-09_e2a_full.txt",
            "results/raw/2026-08-09_e2a_analysis.txt", "data/e2a/sessions*.jsonl",
            "data/e2a/g3prime_kl*.jsonl", "data/e2a/analysis.json"]
E2A_FULL = ["results/raw/2026-08-09_e2a_full.txt", "results/raw/2026-08-09_e2a_analysis.txt",
            "data/e2a/sessions.jsonl", "data/e2a/analysis.json"]
E2A_G3P = ["results/raw/2026-08-09_e2a_g3prime.txt", "data/e2a/g3prime_kl*.jsonl"]
E0_ALL = ["results/raw/2026-08-08_e0_*.txt", "data/e0/e0_axes*", "data/e0/e0_b1_markers*",
          "data/e0/e0_b2_*", "data/e0/e0_b2c_a.json", "data/e0/e0_random_dirs.npz"]
E0_B2A = ["results/raw/2026-08-08_e0_b2a_*.txt", "data/e0/e0_b2_b2a.json"]
E0_B2B = ["results/raw/2026-08-08_e0_b2b_full.txt", "data/e0/e0_b2_b2b.json"]
E0_B2C_A = ["results/raw/2026-08-08_e0_b2c_a.txt", "data/e0/e0_b2c_a.json"]
E0_B2C_SMOKE = ["results/raw/2026-08-08_e0_b2c_smoke.txt"]
D_GATES = ["results/raw/2026-08-10_d_train_*.txt", "results/raw/2026-08-10_d_gates_*.txt",
           "results/raw/2026-08-10_d_evoked_discrim.txt", "data/d/*.json"]
F1_SMOKE = ["results/raw/2026-08-10_f_smoke*.txt", "data/f/sessions_smoke.jsonl",
            "results/raw/2026-08-10_f_calib2.txt"]
F1_RUN = ["results/raw/2026-08-10_f_run.txt", "results/raw/2026-08-10_f_analysis.txt",
          "data/f/sessions.jsonl", "data/f/screen_analysis.json"]
H3 = ["data/e2b/h3_tagscreen.json", "data/e2b/h3b_repair_screen.json",
      "results/raw/2026-08-20_h3_tagscreen.txt", "results/raw/2026-08-20_h3b_repair_screen.txt"]
H2READ = ["data/e2b/h2_read_stability.json", "results/raw/2026-08-21_h2_read_stability.txt"]
H2 = ["results/raw/2026-08-21_h2_smoke_*.txt", "data/e2b/h2_sessions.json",
      "results/raw/2026-08-21_h2_sessions.txt", "data/e2b/h2_sweep.json",
      "results/raw/2026-08-21_h2_sweep.txt"]
H1U = ["results/raw/2026-08-21_h1_sessions.txt"]
H1U_B = [("data/e2b/h1_sessions.json", None, "d94e281")]
H1G = ["data/e2b/h1_gate.json", "results/raw/2026-08-21_h1_gate*.txt"]
H1G_B = [("data/e2b/h1_sessions.json", "d94e281", None)]
VERD_SMOKE = ["results/raw/2026-08-22_verdict_smoke.txt"]
VERD = ["results/raw/2026-08-22_verdict_campaign.txt", "results/raw/2026-08-22_verdict_analysis.txt",
        "data/e2b/verdict_campaign.json", "data/e2b/verdict_analysis.json"]
A3 = ["data/olmo/a3_axes_*", "results/raw/2026-08-23_a3_a2.txt"]
A4 = ["data/olmo/a4_hijack_*.json", "data/olmo/a4_instrument_*", "results/raw/2026-08-23_a4.txt"]
APHASE = ["data/olmo/a1_*", "data/olmo/a2_*", "data/olmo/a3_*", "data/olmo/a4_*",
          "results/raw/2026-08-23_a1_*.txt", "results/raw/2026-08-23_a3_a2.txt",
          "results/raw/2026-08-23_a2_rerun.txt", "results/raw/2026-08-23_a4.txt"]
BPHASE = ["data/olmo/b2_*", "data/olmo/b3_*", "results/raw/2026-08-24_b2.txt",
          "results/raw/2026-08-24_b3.txt", "results/raw/2026-08-24_bphase_respawn.txt"]
B3 = ["data/olmo/b3_*", "results/raw/2026-08-24_b3.txt", "results/raw/2026-08-24_bphase_respawn.txt"]
B2R_CONTROL = ["data/olmo/b2r_control_*", "data/olmo/b2r_analysis.json",
               "results/raw/2026-08-25_b2r_analysis.txt", "results/raw/2026-08-25_b2r_arc.txt"]
B2R_SMOKE = ["data/olmo/b2r_sampling_*", "results/raw/2026-08-25_b2r_gates.txt"]
B2R_QUAL = ["data/olmo/b2r_concepts_*", "data/olmo/b2r_qualify_*"]
B2R_EXPL = ["data/olmo/b2r_explore_*"]
D1 = ["data/e2d/d1_sessions.json", "results/raw/2026-09-01_e2d_d1.txt",
      "results/raw/2026-09-01_e2d_oracle_iv.txt"]
D2 = ["data/e2d/tstep_check*.json", "results/raw/2026-09-02_e2d_tstep*.txt",
      "data/e2d/d2_sessions.json", "results/raw/2026-09-02_e2d_d2.txt",
      "results/raw/2026-09-02_e2d_d2_*.txt", "data/e2d/d2_scores.json", "data/e2d/d2_tables.json",
      "data/e2d/d2_analysis.json"]
D3 = ["data/e2d/d2_excision_check.json", "results/raw/2026-09-03_e2d_excision.txt",
      "data/e2d/d3_*.json", "results/raw/2026-09-03_e2d_d3*.txt", "data/e2d/dose_paired_d2_d3.json"]
K1 = ["data/k/k1_sessions.json", "data/k/k1_reads.json", "data/k/k1_analysis.json",
      "results/raw/2026-09-09_k1_stage1_run.log", "results/raw/2026-09-09_k1_analyze_run.txt"]

# ---- tiers (values-check pass 2, finding 4; definition in VERDICT_DEFINITION) ----
T_C1 = T("verdict (primary)", A12, "no primary experiment run; full run held", 1662,
         why="judgment call: the entry calls the full run the primary experiment (first locator) and its read a gate that c2 waits on "
             "(second to fourth locators: 'Pre-registered gate read'; 'c2 is deliberately unbuilt until c1's gate reads out'), and the r2 entry "
             "says 'c2 remains unlicensed' (fifth); no proposal document tiers the (c) arc, so the entry's words fire both clauses of the "
             "definition; Code counts the cells as verdict, and section 7 item 2 gives the counts under the gate reading",
         also=[(A12, "Pre-registered gate read (in `c1_gate.py`)", 1662), (A12, "before launch.** c2 is", 1662),
               (A12, "deliberately unbuilt until c1's gate reads out", 1662), (A12, "criterion is blind to. c2 remains", 1825)],
         call="c1")
T_D_INPUT = T("input (distillation training data)", PD, "## 1. The trace: tag-conditional activation distillation")
T_D_GATE = T("gate (d1 gates, licensing d2)", PD, "## 2. d1 gates (pre-registered before any d2 contact)",
             also=[(A34, "G1 installed (manipulation check, never a finding)", 585)], call="dgate")
T_E0_PRE = T("extraction and dose-finding", A34, "B2a dose-finding,", 1483,
             why="the e0 extraction and B1 runs precede the instrument the B2 entry locks; B2a is its dose-finding step")
T_E0_B2A = T("dose-finding", A34, "B2a dose-finding,", 1483)
T_E0_B2B = T("verdict (confirmatory)", A34, "Verdict — B2b confirmatory", 1483)
T_E0_B2C_SMOKE = T("smoke", A34, "The 6-context smoke flicker", 1334, log_only=True,
                   why="the governing texts (the B2c entry, PROPOSAL-e) do not name the smoke; the basis is the B2c-a result entry, which lists the smoke raw and treats its numbers as a smoke's",
                   also=[(A34, "2026-08-08_e0_b2c_{smoke,a}.txt", 1334)])
T_E0_B2C = T("verdict (confirmatory)", A34, "confirmatory (user-approved; committed before any B2c data)", 1368)
T_E2A_GATES = T("calibration gate", A34, "g1–g3 calibration gates", 1240)
T_E2A_G3P = T("gate", A34, "g3′ — operative gate for the text-mediated read", 1127)
T_E2A_SMOKE = T("smoke and N declaration", A34, "smoke → N declaration → full run", 1240)
T_E2A_SMOKE_G3P = T("smoke, g3' gate check and N declaration", A34, "smoke → N declaration → full run", 1240)
T_E2A_FULL = T("verdict (primary)", A34, "PRIMARY = first free choice", 1240)
T_F0 = T("calibration", PF, "calibrated offline in f0")
T_F1_SMOKE_PF = T("smoke and recalibration", PF, "smoke (offset indices) → N declaration → screen run")
T_F1_SCREEN_PF = T("verdict (screen)", PF, "## 3. Statistics: screen, then confirm")
T_F1_SMOKE = T("smoke and recalibration", A34, "Smoke bars stay hair-trigger", 366)
T_F1_SCREEN = T("verdict (screen)", A34, "Primary & screen-hit conjuncts", 366)
T_S = T("registered reading outside the verdict tier", PG, "Gate on nothing; nothing gates on them",
        why="the S-satellites register interpretation maps; PROPOSAL-g §0.2 names B1-B3 as its verdicts",
        also=[(PG, "and **B1–B3** (verdicts)", 1)])
T_A13 = T("calibration", PG, "## 3. Phase A — calibration tier",
          why="A3's guard profiles 'decide nothing'", also=[(PG, "are reported alongside but decide nothing", 1)])
T_A3_Q1 = T("calibration (decides nothing)", PG, "are reported alongside but decide nothing")
T_A4 = T("verdict (the data B1's Q1 verdict reads)", PG, "Verdict per stage = A4 potency",
         why="§3 heads Phase A 'no verdict data', but §4 evaluates the Q1 verdict (B1) on A4's outputs and B1 runs no forwards",
         also=[(PG, "## 3. Phase A — calibration tier", 1)], call="a4")
T_B1 = T("declaration (no forwards)", LG, "## 2. B1 — Q1 verdict wiring")
T_G1 = T("attached reporting (never a verdict input)", AG1, "this screen is attached reporting")
T_H_CAL = T("calibration", PH, "## 2. H-calibration tier (all gates before any verdict session)")
T_H_SMOKE = T("smoke", RM, "smoke 6 sessions, 504 s", log_only=True,
              why="the governing texts (PROPOSAL-h, LOCK-h) do not name the smoke; the basis is the runner entry, which reports the 6-session smoke and says it is not the campaign",
              also=[(RM, "nothing is committed to `data/e2b/verdict_campaign.json` yet", 1)])
T_H_VERD = T("verdict (verdict tier)", PH, "## 3. e2b verdict tier")
T_LH_CAL = T("calibration", LH, "# The v1.x record (H-calibration tier)")
T_LH_VERD = T("verdict (verdict tier)", LH, "## 2. Verdict tier, restated with values in place")
T_B = T("verdict (Phase B)", PG, "## 4. Phase B — verdict experiments")
T_G3_CONTROL = T("verdict (control; verdict-bearing for harness validation)", AG3, "verdict-bearing for harness validation")
T_G3_SMOKE = T("smoke (sampling-reproducibility assertion)", AG3, "sampling-reproducibility assertion")
T_G3_QUAL = T("calibration", AG3, "## 2. QUALIFICATION")
T_G3_EXPL = T("exploration (no transition criterion attaches)", AG3, "## 3. EXPLORATION")
T_J1 = T("calibration (harness acceptance smoke)", PJ, "## 2. D-calibration tier", also=[(PJ, "**D1 — harness acceptance smoke", 1)])
T_J2 = T("calibration (qualification rung)", PJ, "## 2. D-calibration tier", also=[(PJ, "**D2 — the qualification rung", 1)])
T_J3 = T("calibration (descriptive rung)", PJ, "## 2. D-calibration tier", also=[(PJ, "**D3 — descriptive rung", 1)])
T_K1 = T("gate (Stage 1: no behavioral verdict)", PK, "## §1 Stage 1 — the channel study",
         also=[(PK, "### 1.4 Registered criteria (gates)", 1)], call="k1")
T_M = T("not classified (no data; PROPOSAL-m is outside this item's scope)")

NOVERDICT_D = {"text": "d2, the preference test (PROPOSAL-d §3), never ran: d2 was closed by gate",
               "refs": [(PD, "## 3. d2: the preference test", 1), (A34, "d2 CLOSED BY GATE", 1)],
               "disclosure": [(A34, "gates(B) + descriptives — BOTH findings", 1,
                               "the log reports the gate outcomes as findings after the leakage adjudication")]}
NOVERDICT_J = {"text": "the verdict tier (§3) never ran; LOCK-j is not in the record", "lock": "LOCK-j",
               "refs": [(PJ, "## 3. Verdict tier (runs only after LOCK-j commits)", 1), (RM, "the verdict tier and LOCK-j do not run", 1)]}
NOVERDICT_K = {"text": "Stage 2, the verdict tier, never ran; LOCK-k is not in the record", "lock": "LOCK-k",
               "refs": [(PK, "## §2 Stage 2 — the operant (the verdict tier", 1), (RM, "Nothing in Stage 2 has run.", 1),
                        (RM, "LOCK-k does not exist.", 1)],
               "disclosure": [(RM, "Stage 1's verdict (`7742e2c`, G3_FAIL)", 1, "the log calls Stage 1's outcome a verdict")]}

ROWS = [
    # ---------------- cycle 1-2, log-only ----------------
    {"id": "L-slice2", "kind": "log", "title": "Cycle 2 §5 slice-2 TOST tie-construction design ('LOCKED with the user'; 'Pre-registered design, to build against')",
     "path": "archive/RESULTS-cycle1-2.md", "line": 1381, "commit": "f9eab26",
     "cells": [cell("§5 slice-2 primary TOST runs", ["results/raw/2026-08-04_slice2_primary_tost*.txt"],
                    T("verdict (primary)", A12, "Staging (LOCKED): primary arm first", 1381))],
     "pre_data_globs": ["results/raw/2026-08-0[34]_slice1*"],
     "pre_data_label": "§5 slice-1 runs (config profile, accuracy screen); the entry's design is a correction of the approach slice 1 tested",
     "amendments": [("archive/RESULTS-cycle1-2.md", 1447, "f922cd4"), ("archive/RESULTS-cycle1-2.md", 1482, "3ca8acb")]},
    {"id": "L-c1", "kind": "log", "title": "Cycle 2 (c) c1 conditioning gate read P1-P3/S1 ('Pre-registered gate read (in c1_gate.py)')",
     "path": "archive/RESULTS-cycle1-2.md", "line": 1662, "commit": "6d88d9b",
     "cells": [cell("c1 full run (r1, gate verdict)", ["results/raw/2026-08-06_c1_full_run.txt"], T_C1),
               cell("c1 r2 retry ('gate criteria unchanged')", ["results/raw/2026-08-06_c1r2_full_run.txt"], T_C1)],
     "pre_data_globs": ["results/raw/2026-08-05_lora_feasibility_spike.txt"],
     "pre_data_label": "the (c) prerequisite LoRA feasibility spike (3fb4b99's subject: '(c) prerequisite -- LoRA feasibility spike PASS')",
     "same_commit_prior": [{"label": "c1 smoke (gate plumbing on a deliberately undertrained 4-step adapter)",
                            "globs": ["results/raw/2026-08-06_c1_smoke.txt"],
                            "reported": [(A12, "BUILT + smoke-tested end-to-end", 1662),
                                         (A12, "the pre-registered read produces a proper null on junk conditioning", 1662)],
                            "gloss": "the entry reports the smoke as already run and already scored under the gate read"}],
     "amendments": [("archive/RESULTS-cycle1-2.md", 1825, "a1060c2")],
     "note": "The entry names scripts/c1_gate.py as the gate's implementation; that file was never tracked at any commit (git log --all over the path is empty). The P1-P3/S1 gate read is in the record only as the log prose: the later port valence_core/gate.py (e16e76f) implements the r3 matched-pair swing criterion, not this read (see row L-c1r3)."},
    {"id": "L-c1r3", "kind": "log", "title": "Cycle 2 (c) c1 r3 PRE-REGISTRATION (matched-pair swing criterion)",
     "path": "archive/RESULTS-cycle1-2.md", "line": 1882, "commit": "b78bfb3",
     "cells": [cell("c1 r3 confirmatory run", ["results/raw/2026-08-06_c1r3_full_run.txt", "data/configs/c1r3_gate_rep*.json"],
                    T("verdict (confirmatory)", A12, "Confirmatory test of the r2 post-hoc", 1882))],
     "pre_data_globs": ["results/raw/2026-08-06_c1*"],
     "pre_data_label": "the c1 smoke, r1 and r2 runs; the entry calls r3 a 'confirmatory test of the r2 post-hoc association signal'",
     "port": {"path": "valence_core/gate.py", "regression": ("valence_core/regression/analysis.py", "def check_c1r3_gate"),
              "configs": "data/configs/c1r3_gate_rep*.json"},
     "note": "The entry says the criterion was 'implemented and validated in scripts/c1_gate.py before this commit'; that script was never tracked, so before the r3 data the criterion is in the record only as the log prose. Its code entered the record later, after the r3 data: valence_core/gate.py, whose docstring says it is 'ported off `scripts/c1_gate.py`', with the r3 gate JSONs and a regression check (port line below)."},
    # ---------------- cycle 3 documents ----------------
    {"id": "P-d", "kind": "doc", "doc": "PROPOSAL-d-distilled-trace.md", "title": "PROPOSAL-d (distilled-trace CPP)",
     "versions": [("c54c4e0", "sole version")], "record": "c54c4e0", "acceptance": "c7bedcb",
     "cells": [cell("(d)/e1 teacher cache (distillation training data, 304 forwards)", ["results/raw/2026-08-10_d_cache.txt"], T_D_INPUT,
                    note="Lands in the same commit as the G-gate pre-registration (row L-dgate), which is 'committed before training replicate A'."),
               cell("(d)/e1 G-gates, replicates A and B", D_GATES, T_D_GATE)],
     "no_verdict": NOVERDICT_D,
     "pre_data_globs": ["results/raw/2026-08-10_d_*", "data/d/*"], "pre_data_exclude": ["results/raw/2026-08-10_d_layermap.txt"],
     "note": "Status line at every commit: 'proposal for review (user + repo instance); not locked, nothing run.' The operative gate criteria are the log-only G-gate pre-registration (row L-dgate). results/raw/2026-08-10_d_layermap.txt (0154997) reads adapter key names and runs no forward; it is not data under the rule."},
    {"id": "P-e", "kind": "doc", "doc": "PROPOSAL-e-reward-axis-hijack.md", "title": "PROPOSAL-e (reward-axis hijack)",
     "versions": [("c54c4e0", "sole version")], "record": "c54c4e0", "acceptance": "c7bedcb",
     "cells": [cell("e0 extraction, B1 and B2a dose-finding", E0_ALL, T_E0_PRE, exclude=E0_B2B + E0_B2C_A + E0_B2C_SMOKE, result_entry="15ab36b",
                    note="The e0 raws enter the record at f222541; the first log entry reporting e0 data is 15ab36b."),
               cell("e0 B2b confirmatory (V1 verdict)", E0_B2B, T_E0_B2B, result_entry="60916ce"),
               cell("e0 B2c smoke", E0_B2C_SMOKE, T_E0_B2C_SMOKE),
               cell("e0 B2c-a", E0_B2C_A, T_E0_B2C),
               cell("e2a calibration gates g1-g3", E2A_GATES, T_E2A_GATES),
               cell("e2a g3' check", E2A_G3P, T_E2A_G3P),
               cell("e2a smoke and N declaration", E2A_SESS, T_E2A_SMOKE, exclude=E2A_FULL + E2A_G3P),
               cell("e2a full run (verdict sessions)", E2A_FULL, T_E2A_FULL)],
     "pre_data_globs": ["results/raw/2026-08-08_e0_*", "data/e0/*", "results/raw/*e2a*", "data/e2a/*"],
     "note": "Status line at every commit: 'proposal for review (user + repo instance); not locked, nothing run.' The operative criteria are the log-only pre-registrations L-e0B2, L-e0B2c, L-e2a and L-e2a-g3p; this row's cells take their tiers from them."},
    {"id": "L-e0B2", "kind": "log", "title": "e0 V1 B2 PRE-REGISTRATION (instrument G = 0.3156, B2a dose rule + stop rule, B2b 7-arm V1 criterion)",
     "path": "archive/RESULTS-cycles3-4.md", "line": 1483, "commit": "05bda27",
     "cells": [cell("e0 B2a dose-finding", E0_B2A, T_E0_B2A, result_entry="ae008be"),
               cell("e0 B2b confirmatory (V1 verdict)", E0_B2B, T_E0_B2B, result_entry="60916ce")],
     "pre_data_globs": ["results/raw/2026-08-08_e0_*", "data/e0/*"],
     "pre_data_entries": ["15ab36b", "4118d6b", "ba15304"],
     "pre_data_label": "e0 smoke, extraction and B1 runs, reported in log entries before this commit; their raws enter the record later, at f222541. The entry says its instrument is 'recomputed deterministically from frozen `e0_b1_markers.npz`' (the B1 output), by design"},
    {"id": "L-e0B2c", "kind": "log", "title": "e0 B2c PRE-REGISTRATION (last-position axis confirmatory)",
     "path": "archive/RESULTS-cycles3-4.md", "line": 1368, "commit": "f222541",
     "cells": [cell("e0 B2c smoke", E0_B2C_SMOKE, T_E0_B2C_SMOKE),
               cell("e0 B2c-a", E0_B2C_A, T_E0_B2C)],
     "pre_data_globs": ["results/raw/2026-08-08_e0_*", "data/e0/*"], "pre_data_exclude": ["results/raw/2026-08-08_e0_b2c_*.txt", "data/e0/e0_b2c_a.json"],
     "pre_data_entries": ["15ab36b", "4118d6b", "ba15304", "ae008be", "60916ce"],
     "pre_data_label": "e0 smoke, extraction, B1, B2a and B2b runs, reported in log entries before this commit; their raws enter in this commit itself (row note). The entry's motivation is the last-position variant's guard profile measured in those runs",
     "note": "The pre-registration commit f222541 also adds the e0 raws of earlier cells (extraction, B1, B2a, B2b); none of them is B2c data."},
    {"id": "L-e2a", "kind": "log", "title": "e2a PRE-REGISTRATION (pure-operant preference loop; gates, dose ladder, arms/N floors, first-free-choice primary)",
     "path": "archive/RESULTS-cycles3-4.md", "line": 1240, "commit": "1970b50",
     "cells": [cell("e2a calibration gates g1-g3", E2A_GATES, T_E2A_GATES),
               cell("e2a smoke, g3' check and N declaration", E2A_SESS, T_E2A_SMOKE_G3P, exclude=E2A_FULL),
               cell("e2a full run (verdict sessions)", E2A_FULL, T_E2A_FULL)],
     "pre_data_globs": ["results/raw/*e2a*", "data/e2a/*"],
     "amendments": [("archive/RESULTS-cycles3-4.md", 1127, "da40635"), ("archive/RESULTS-cycles3-4.md", 1043, "3637c06"),
                    ("archive/RESULTS-cycles3-4.md", 916, "8fa0b75"), ("archive/RESULTS-cycles3-4.md", 755, "bc153ed"),
                    ("archive/RESULTS-cycles3-4.md", 700, "814a254")]},
    {"id": "L-e2a-g3p", "kind": "log", "title": "e2a g3' PRE-REGISTRATION AMENDMENT (text-mediated read gate replacing g3)",
     "path": "archive/RESULTS-cycles3-4.md", "line": 1127, "commit": "da40635",
     "cells": [cell("e2a g3' check", E2A_G3P, T_E2A_G3P),
               cell("e2a smoke and N declaration", E2A_SESS, T_E2A_SMOKE, exclude=E2A_FULL + E2A_G3P),
               cell("e2a full run (verdict sessions)", E2A_FULL, T_E2A_FULL)],
     "pre_data_globs": E2A_GATES,
     "pre_data_label": "the e2a g1-g3 calibration gates under the parent pre-registration, including the g3 FAIL this amendment adjudicates (the entry's header: 'design-instance adjudication of the g3 flag')"},
    {"id": "L-dgate", "kind": "log", "title": "(d)/e1 G-GATE PRE-REGISTRATION (G1 swing, G2 1.25x, G3 specificity, G4 0.05 nats, leakage 0.10)",
     "path": "archive/RESULTS-cycles3-4.md", "line": 585, "commit": "88e9ef0",
     "cells": [cell("(d)/e1 G-gates, replicates A and B", D_GATES, T_D_GATE)],
     "no_verdict": NOVERDICT_D,
     "pre_data_globs": ["results/raw/2026-08-10_d_*", "data/d/*"], "pre_data_exclude": ["results/raw/2026-08-10_d_layermap.txt"],
     "same_commit_prior": [{"label": "(d)/e1 teacher cache (the distillation training input)",
                            "globs": ["results/raw/2026-08-10_d_cache.txt"],
                            "reported": [(A34, "Teacher cache complete", 585)],
                            "gloss": "the entry reports the cache as complete (304 forwards) when it was written; the gates measure the adapters trained on it"}],
     "amendments": [("archive/RESULTS-cycles3-4.md", 505, "535ed21")]},
    {"id": "P-f", "kind": "doc", "doc": "PROPOSAL-f-natural-reinforcer-screen.md", "title": "PROPOSAL-f (natural-reinforcer screen)",
     "versions": [("ea011bd", "sole version")], "record": "ea011bd", "acceptance": "6cd7a74",
     "cells": [cell("f0 calibration (pools, bars)", ["results/raw/2026-08-10_f_calib.txt", "data/f/calib.json", "data/f/pools.json"], T_F0),
               cell("f1 smoke rounds and f0 recalibration v2", F1_SMOKE, T_F1_SMOKE_PF),
               cell("f1 screen run (344 sessions)", F1_RUN, T_F1_SCREEN_PF)],
     "pre_data_globs": ["results/raw/2026-08-10_f_*", "data/f/*"],
     "note": "Status line at every commit: 'proposal for review (user + repo instance); nothing run.' The operative screen criteria are the log-only f1 PRE-REGISTRATION (row L-f1)."},
    {"id": "L-f1", "kind": "log", "title": "f1 PRE-REGISTRATION (five contrasts, locked directions, screen-hit conjuncts, two-tier no-claim rule)",
     "path": "archive/RESULTS-cycles3-4.md", "line": 366, "commit": "7a6036a",
     "cells": [cell("f1 smoke rounds and f0 recalibration v2", F1_SMOKE, T_F1_SMOKE),
               cell("f1 screen run (344 sessions)", F1_RUN, T_F1_SCREEN)],
     "pre_data_globs": ["results/raw/2026-08-10_f_*", "data/f/*"],
     "pre_data_label": "the f0 calibration, whose measured bars the entry locks by design (its header: 'Locks verbatim from PROPOSAL-f §2–3 + the f0 measured bars')",
     "amendments": [("archive/RESULTS-cycles3-4.md", 285, "37c7078"), ("archive/RESULTS-cycles3-4.md", 207, "27446d3"),
                    ("archive/RESULTS-cycles3-4.md", 147, "eb0f33b")]},
    {"id": "L-r26", "kind": "log", "title": "Rule-26 criterion (ii) TIGHTENED and re-locked ('Pre-registration entry: committed BEFORE the run that evaluates it')",
     "path": "RESULTS.md", "line": 12839, "commit": "18dc75e",
     "cells": [cell("criterion (ii) re-run under the tightened form", ["results/raw/2026-08-12_rule26_b2b_tightened.txt"],
                    T("verdict (acceptance criterion)", RM, "Pre-registration entry: committed BEFORE the run that", 12839))],
     "pre_data_globs": ["results/raw/2026-08-12_rule26_*", "data/regression/*"],
     "pre_data_label": "the oracle run of criterion (ii) in its original form and its JSON; the entry itself says the tightening followed that run (its 'Why.' paragraph)"},
    # ---------------- Phase 2 documents ----------------
    {"id": "P-g", "kind": "doc", "doc": "PROPOSAL-g-ontogeny-of-evaluation.md", "title": "PROPOSAL-g (ontogeny of evaluation)",
     "versions": [("72b09a9", "v1.0, pre-registration of record"), ("499f6d5", "status-line amendment (administrative)")],
     "record": "72b09a9",
     "cells": [cell("S1 judge-rescue ladder (Qwen, archived e2a texts)", ["data/e2a/s1_judge_rescue.json", "results/raw/2026-08-20_s1_judge_rescue.txt"], T_S),
               cell("S2 selectivity panel", ["data/e0/s2_*", "results/raw/2026-08-20_s2_*.txt"], T_S),
               cell("Phase A1-A3 on the four OLMo checkpoints", APHASE, T_A13, exclude=A4),
               cell("A4 causal potency (the data B1's Q1 verdict reads)", A4, T_A4)],
     "pre_data_globs": ["data/olmo/*", "results/raw/2026-08-19_*"],
     "note": "PROPOSAL-g §0.1 discloses the 2026-08-19 R_l survey as a descriptive peek made before the commit; the earlier files listed below are the Phase-0 step-2 bring-up (manifest, R_l survey, determinism, smoke, cast check, scaffold mass). B1-B3 are listed under LOCK-g; B2-r under ADDENDUM-g3."},
    {"id": "Q1", "kind": "bet", "doc": "PROPOSAL-g-ontogeny-of-evaluation.md", "title": "Q1 bet ('present at Base; marking is a pretraining acquisition'); PROPOSAL-g's text dates it 2026-08-18, a date the record does not evidence (section 8)",
     "versions": [("72b09a9", "first committed text of the bet")], "record": "72b09a9",
     "cells": [cell("A3 axis geometry and guards (Q1 quantities)", A3, T_A3_Q1),
               cell("A4 causal potency (Q1 quantity)", A4, T_A4),
               cell("B1 Q1 verdict declaration (no new forwards; read off A4)", ["data/olmo/b1_verdict.json"], T_B1, inputs_only=True)],
     "pre_data_globs": ["data/olmo/*", "results/raw/2026-08-19_*"],
     "pre_data_label": "the Phase-0 step-2 OLMo bring-up, including the R_l survey the bet's 'prior to the survey' wording refers to (row P-g's note)"},
    {"id": "P-h", "kind": "doc", "doc": "PROPOSAL-h-state-present-choice.md", "title": "PROPOSAL-h (e2b, state-present choice)",
     "versions": [("34eb7ee", "v1.0, pre-registration of record"), ("b400083", "interpretive note appended (steered rounds)")],
     "record": "34eb7ee",
     "cells": [cell("H3 roster screens (Qwen)", H3, T_H_CAL),
               cell("H2 dose stability (read half, proper, sweep)", H2READ + H2, T_H_CAL),
               cell("H1 run 1 (redesignated H1-u)", H1U, T_H_CAL, bounded=H1U_B),
               cell("H1 leakage gate, run of record", H1G, T_H_CAL, bounded=H1G_B),
               cell("e2b verdict-campaign smoke", VERD_SMOKE, T_H_SMOKE),
               cell("e2b verdict campaign, run of record", VERD, T_H_VERD)],
     "cell_version": {"e2b verdict-campaign smoke": "b400083", "e2b verdict campaign, run of record": "b400083"},
     "pre_data_globs": ["data/e2b/*", "results/raw/2026-08-2[0-2]_h*", "results/raw/2026-08-22_verdict*"], "pre_data_exclude": ["data/e2b/h1_power*", "results/raw/*h1_power*"]},
    {"id": "W-h", "kind": "welfare", "doc": "PROPOSAL-h-state-present-choice.md", "title": "Welfare pre-commitment, PROPOSAL-h §5 (cited by PROPOSAL-m v1.11 as PROPOSAL-h:165-167)",
     "versions": [("34eb7ee", "as committed")], "record": "34eb7ee", "cited_span": (165, 167),
     "cite_token": "PROPOSAL-h:165", "trigger_re": r"e2b VERDICT CAMPAIGN: NULL",
     "start_re": r"\*\*Pre-commitment:\*\*", "end_re": r"survives into the paper\.",
     "cells": [cell("e2b verdict campaign, run of record (the primary the trigger names)", VERD, T_H_VERD)],
     "pre_data_globs": ["data/e2b/*", "results/raw/2026-08-2[0-2]_h*", "results/raw/2026-08-22_verdict*"], "pre_data_exclude": ["data/e2b/h1_power*", "results/raw/*h1_power*"]},
    {"id": "A-g1", "kind": "doc", "doc": "ADDENDUM-g1-archival-reading-screen.md", "title": "ADDENDUM-g1 (per-stage archival-reading screen, attached to B3)",
     "versions": [("34eb7ee", "v1.0, sole version")], "record": "34eb7ee",
     "cells": [cell("g1 archival screen (data/olmo/g1_archival_{stage}.json per the addendum)", ["data/olmo/g1_archival_*", "results/raw/*g1_archival*"], T_G1)],
     "pre_data_globs": B3},
    {"id": "LOCK-h", "kind": "doc", "doc": "LOCK-h.md", "title": "LOCK-h (H-calibration lock v1.1-v1.4; verdict-tier lock v2.0)",
     "versions": [("8a97513", "v1.1"), ("09ae918", "v1.2 (session plan)"), ("a58692f", "v1.3 (registered secondary + stop corollary)"),
                  ("d94e281", "v1.4 (steered rounds + exclusion-robust schedule)"), ("f030cdd", "v2.0 (verdict tier)")],
     "record": "8a97513",
     "cells": [cell("H2 read half (precursor)", H2READ, T_LH_CAL),
               cell("H2 proper and sweep", H2, T_LH_CAL),
               cell("H1 run 1 (redesignated H1-u)", H1U, T_LH_CAL, bounded=H1U_B),
               cell("H1 leakage gate, run of record", H1G, T_LH_CAL, bounded=H1G_B),
               cell("e2b verdict-campaign smoke", VERD_SMOKE, T_H_SMOKE),
               cell("e2b verdict campaign, run of record", VERD, T_LH_VERD)],
     "cell_version": {"H2 read half (precursor)": "8a97513", "H2 proper and sweep": "09ae918",
                      "H1 run 1 (redesignated H1-u)": "a58692f", "H1 leakage gate, run of record": "d94e281",
                      "e2b verdict-campaign smoke": "f030cdd", "e2b verdict campaign, run of record": "f030cdd"},
     "pre_data_globs": H3,
     "pre_data_label": "the H3 roster screens, governed by PROPOSAL-h (row P-h); LOCK-h's own cells start at H2"},
    {"id": "LOCK-g", "kind": "doc", "doc": "LOCK-g.md", "title": "LOCK-g v1.1 (A-phase instantiation lock for PROPOSAL-g)",
     "versions": [("0551224", "v1.1, sole committed version")], "record": "0551224",
     "cells": [cell("B1 Q1 verdict declaration (no new forwards; read off the A4 artifacts)", ["data/olmo/b1_verdict.json"], T_B1, inputs_only=True,
                    note="LOCK-g §2: 'read off the committed A4 artifacts; no new forwards'. Its inputs (A4) precede the lock by design (PROPOSAL-g status: bars 'instantiated by Phase A' and committed as LOCK-g 'before any Phase B run')."),
               cell("B2 and B3 campaigns (four stages)", BPHASE, T_B,
                    note="The campaigns' concept vectors, fidelity checks and register files land in the same commit as their B2 and B3 outputs.")],
     "pre_data_globs": APHASE,
     "note": "The earlier files listed below are the Phase-A data whose realised values this lock instantiates, by design: PROPOSAL-g's status block says the [LOCK-g] bars are 'instantiated by Phase A' and committed as LOCK-g.md 'before any Phase B run'."},
    {"id": "W-g", "kind": "welfare", "doc": "LOCK-g.md", "title": "Welfare pre-commitment extension, LOCK-g §5 (cited by PROPOSAL-m v1.11 as LOCK-g:167-170)",
     "versions": [("0551224", "as committed")], "record": "0551224", "cited_span": (167, 170),
     "cite_token": "LOCK-g:167", "trigger_re": r"B3 SCREEN COMPLETE, ALL FOUR STAGES: NULL",
     "start_re": r"^Any stage passes confirm", "end_re": r"its frame\.",
     "cells": [cell("B3 screen (the tier before the confirm that the trigger names; confirm never ran)", B3, T_B)],
     "confirm_re": r"No stage triggers a confirm",
     "pre_data_globs": B3},
    {"id": "A-g3", "kind": "doc", "doc": "ADDENDUM-g3-b2r-v1.2.md", "title": "ADDENDUM-g3 v1.2 (B2-r: specificity control, dose qualification, sensitivity exploration)",
     "versions": [("f14d249", "v1.2, sole committed version")], "record": "f14d249",
     "cells": [cell("B2-r control (the specificity transition), with the analysis and the campaign log", B2R_CONTROL, T_G3_CONTROL,
                    note="results/raw/2026-08-25_b2r_arc.txt is the campaign log for all parts; b2r_analysis covers all parts."),
               cell("B2-r sampling-reproducibility assertion (pre-campaign smoke)", B2R_SMOKE, T_G3_SMOKE),
               cell("B2-r qualification (concept vectors and dose ladder)", B2R_QUAL, T_G3_QUAL),
               cell("B2-r exploration", B2R_EXPL, T_G3_EXPL)],
     "pre_data_globs": ["data/olmo/b2_*", "results/raw/2026-08-24_b2.txt"],
     "note": "The addendum's status line says it is licensed by the registered stop branch of PROPOSAL-g §4-B2 as executed 2026-08-24, i.e. it was written after the original B2 campaign's data (listed below) and governs only the B2-r rerun. data/olmo/b2r_budget.json (5c1b161) and data/olmo/b2r_frac_table.json (c17337c) are model-free arithmetic and precede the addendum; not data under the rule."},
    {"id": "P-j", "kind": "doc", "doc": "PROPOSAL-j-dose-escalation.md", "title": "PROPOSAL-j (e2d dose escalation) v1.0-v1.3",
     "versions": [("f7a4a1e", "v1.0"), ("70995c0", "v1.1 (AMENDMENT 1)"), ("ce3ff84", "v1.2 (AMENDMENT 2)"), ("520f62c", "v1.3 (ADDENDUM-j1)")],
     "record": "f7a4a1e",
     "cells": [cell("e2d D1 harness acceptance sessions", D1, T_J1),
               cell("e2d D2 (T-step identity check + qualification sessions + scoring)", D2, T_J2),
               cell("e2d D3 (excision checks + descriptive sessions + scoring)", D3, T_J3)],
     "cell_version": {"e2d D1 harness acceptance sessions": "70995c0",
                      "e2d D2 (T-step identity check + qualification sessions + scoring)": "ce3ff84",
                      "e2d D3 (excision checks + descriptive sessions + scoring)": "520f62c"},
     "no_verdict": NOVERDICT_J,
     "pre_data_globs": ["data/e2d/*", "results/raw/*e2d*"]},
    {"id": "P-k", "kind": "doc", "doc": "PROPOSAL-k-echo-channel.md", "title": "PROPOSAL-k v1.1 (echo channel; Stage 1 channel study)",
     "versions": [("e9b5022", "v1.1 (the document's timestamp)"), ("702f997", "hash fill (Appendix A marker)")],
     "record": "e9b5022",
     "cells": [cell("Stage 1 channel study (48 sham F2 sessions + masked reads + analysis)", K1, T_K1,
                    log_run_time={"path": "RESULTS.md", "re": r"launched (\d\d:\d\d:\d\d) UTC (\d{4}-\d\d-\d\d)"})],
     "no_verdict": NOVERDICT_K,
     "pre_data_globs": ["data/echo/*", "data/format/*"],
     "note": "Stage 2 (the operant) runs only after LOCK-k; LOCK-k is not in the record and Stage 2 never ran. The earlier files listed below are the echo-channel recon (Stages A-C, entries headed 'no verdict quantity') and the format recon, which precede the proposal."},
    {"id": "P-m", "kind": "doc", "doc": "PROPOSAL-m-gating-campaign-v1_11.md", "title": "PROPOSAL-m v1.11 (gating campaign) - governs no model data yet",
     "versions": [("05c4636", "v1.11")], "record": "05c4636",
     "cells": [cell("any PROPOSAL-m unit (model-forward data)", ["data/m/units/*", "data/m/sessions/*"], T_M)],
     "model_free_globs": ["data/m/*"],
     "pre_data_globs": ["data/m/units/*", "data/m/sessions/*"],
     "note": "Listed as a row that governs no data yet. Not adjudicated here (the m build and the STOP-8 thread are out of this item's scope)."},
]

UNTRACKED = [
    ("ADDENDUM-g3-b2r.md", "ADDENDUM-g3 v1.0 draft (values-check RED, af4504a); superseded pre-commit"),
    ("ADDENDUM-g3-b2r-v1.1.md", "ADDENDUM-g3 v1.1 draft (values-check GREEN with two flags, ae73caa); superseded pre-commit by v1.2"),
    ("ADDENDUM-k1.md", "ADDENDUM-k1 v1.1 draft; its commit STOPPED twice on referent checks (3be4a63, e186162)"),
]

ANCHORS = [("72b09a9", "PROPOSAL-g pre-registration of record"),
           ("e9b5022", "PROPOSAL-k v1.1"),
           ("cef728f", "e2d closure")]

# --------------------------------------------------------------------------
# Stamp scanning inside artifacts and raws
# --------------------------------------------------------------------------
MON = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
P_DATEU = re.compile(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) +(\d{1,2}) (\d\d):(\d\d):(\d\d) (?:UTC )?(20\d\d)")
P_ISO = re.compile(r"(20\d\d)-(\d\d)-(\d\d)[T ](\d\d):(\d\d)(?::(\d\d))?(?:Z| ?UTC)")
P_TIME = re.compile(r"(?<![\d:])(\d\d):(\d\d)(?::(\d\d))?(?:Z| UTC)\b")
P_DATE = re.compile(r"(20\d\d)-(\d\d)-(\d\d)")
P_HEADS = [re.compile(r"\bHEAD[ :=]+([0-9a-f]{7,40})\b"), re.compile(r"repo head\s*:\s*([0-9a-f]{7,40})"),
           re.compile(r"gate: proposal ([0-9a-f]{7,40})"), re.compile(r"\block\s*:.*\(([0-9a-f]{7,40})\)"),
           re.compile(r"\bcommit(?:ted)? `?([0-9a-f]{7,40})\b")]
TEXT_EXT = (".txt", ".log", ".md", ".json", ".jsonl")


def scan_file(ref, path):
    """Return (run stamps, time-only stamps, recorded heads, datetime strings in JSON)
    found in path at ref. Run stamps are read from run raws (results/raw/) only; a
    datetime string inside a JSON artifact is reported separately and is not a run stamp."""
    full, tonly, heads, jdt = [], [], [], []
    if not path.endswith(TEXT_EXT):
        return full, tonly, heads, jdt
    is_raw = path.startswith("results/raw/")
    text = show_bytes(ref, path).decode("utf-8", "replace")
    last_date = None
    for i, line in enumerate(text.split("\n"), 1):
        found = False
        if not is_raw:
            for m in list(P_DATEU.finditer(line)) + list(P_ISO.finditer(line)):
                jdt.append({"path": path, "line": i, "verbatim": m.group(0), "context": line.strip()[:160]})
            for p in P_HEADS[:4]:
                for m in p.finditer(line):
                    heads.append({"path": path, "line": i, "verbatim": line.strip()[:220], "hash": m.group(1)})
            continue
        for m in P_DATEU.finditer(line):
            d = dt.datetime(int(m.group(7)), MON[m.group(2)], int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)), tzinfo=dt.timezone.utc)
            full.append({"path": path, "line": i, "verbatim": m.group(0), "utc": d.strftime("%Y-%m-%dT%H:%M:%SZ"), "line_text": line.strip()[:200]})
            found = True
        for m in P_ISO.finditer(line):
            d = dt.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6) or 0), tzinfo=dt.timezone.utc)
            full.append({"path": path, "line": i, "verbatim": m.group(0), "utc": d.strftime("%Y-%m-%dT%H:%M:%SZ"), "line_text": line.strip()[:200]})
            found = True
        if not found:
            for m in P_TIME.finditer(line):
                tonly.append({"path": path, "line": i, "verbatim": m.group(0),
                              "date_context": last_date})
        dm = None
        for dm in P_DATE.finditer(line):
            pass
        if dm:
            last_date = {"date": dm.group(0), "line": i}
        for p in P_HEADS:
            for m in p.finditer(line):
                heads.append({"path": path, "line": i, "verbatim": line.strip()[:220], "hash": m.group(1)})
    return full, tonly, heads, jdt


# --------------------------------------------------------------------------
# Record searches
# --------------------------------------------------------------------------
# Values-check pass 1, finding 1: the search originally covered only *.md, results/raw/
# and data/, and so missed a commit hash recorded first in a script (f14d249 at
# c1bbf7c, scripts/box_b2r_campaign.py and scripts/run_b2r.sh). The primary search
# now covers every tracked path; the old scope is kept as the "logs, raws and data"
# scope, reported separately when the first record anywhere is outside it.
AUDIT_EXCLUDES = [":(exclude)*.npz", ":(exclude)results/raw/2026-10-08_note-*", ":(exclude)AUDIT-note-*",
                  ":(exclude)scripts/audit_note_*"]
SCOPES = {"all": ["."] + AUDIT_EXCLUDES,
          "logs": ["*.md", "results/raw", "data"] + AUDIT_EXCLUDES}


def in_search_scope(f, scope="all"):
    if (f.endswith(".npz") or f.startswith("results/raw/2026-10-08_note-") or f.startswith("AUDIT-note-")
            or f.startswith("scripts/audit_note_")):
        return False
    if scope == "all":
        return True
    return f.endswith(".md") or f.startswith("results/raw/") or f.startswith("data/")


HEXRUN = re.compile(r"(?<![0-9a-fA-F])([0-9a-f]{7,64})(?![0-9a-fA-F])")


def n_records(line, token, full):
    """Occurrences in `line` of a hex run that starts with `token` and is a prefix of
    `full` (the 40-hex commit hash or the 64-hex sha256), bounded by non-hex on both
    sides. A longer hex run that merely contains the token is not a record of it."""
    return sum(1 for m in HEXRUN.finditer(line)
               if m.group(1).startswith(token) and full.startswith(m.group(1)))


def _first_substring(token, ref, commits):
    """The builder's line rule: the first pickaxe commit in which some file in the logs
    scope gains a line containing `token` as a plain substring."""
    for c in commits:
        for f in git("show", "--format=", "--name-only", c).split("\n"):
            if not f or not in_search_scope(f, "logs") or not exists_at(c, f):
                continue
            now = lines_at(c, f)
            before = lines_at(c + "^", f) if exists_at(c + "^", f) else []
            if sum(token in x for x in now) <= sum(token in x for x in before):
                continue
            bs = set(before)
            if any(token in x and x not in bs for x in now):
                return c
    return None


def first_recording(token, ref, full, scope="all"):
    """Earliest commit whose tree gains a bounded record of `token` (pickaxe, then a
    line-level check), with the added lines and their locators at that commit and at
    ref; plus the earliest commit message containing a bounded record of it."""
    res = {"token": token, "full": full, "scope": scope, "file_hit": None, "message_hit": None}
    commits = git("log", "--reverse", "-S" + token, "--format=%H", ref, "--", *SCOPES[scope]).split()
    for c in commits:
        files = git("show", "--format=", "--name-only", c).split("\n")
        added = []
        for f in files:
            if not f or not in_search_scope(f, scope):
                continue
            if not exists_at(c, f):
                continue
            now = lines_at(c, f)
            before = lines_at(c + "^", f) if exists_at(c + "^", f) else []
            if sum(n_records(x, token, full) for x in now) <= sum(n_records(x, token, full) for x in before):
                continue
            before_set = set(before)
            for n, x in enumerate(now, 1):
                if n_records(x, token, full) and x not in before_set:
                    loc_ref = []
                    g = git("grep", "-n", "-F", "-e", x, ref, "--", *SCOPES[scope], check=False) if (x.strip() and len(x) < 2000) else ""
                    for gl in g.split("\n"):
                        if not gl:
                            continue
                        parts = gl.split(":", 3)
                        if len(parts) >= 4 and parts[3] == x:
                            loc_ref.append("%s@%s:%s" % (parts[1], ref[:7], parts[2]))
                    added.append({"path": f, "line_at_commit": n, "locator_at_commit": "%s@%s:%d" % (f, c[:7], n),
                                  "locators_at_ref": loc_ref, "text": x.strip()[:240]})
                    if len(added) >= 4:
                        break
            if len(added) >= 4:
                break
        if added:
            res["file_hit"] = {"commit": c, **{k: meta(c)[k] for k in ("committer_utc", "subject")}, "lines": added,
                               "paths": sorted(set(l["path"] for l in added))}
            break
    msg = git("log", "--reverse", "-F", "--grep=" + token, "--format=%H", ref).split()
    for c in msg:
        body = git("log", "-1", "--format=%B", c)
        if any(n_records(x, token, full) for x in body.split("\n")):
            res["message_hit"] = {"commit": c, **{k: meta(c)[k] for k in ("committer_utc", "subject")}}
            break
    if scope == "logs":
        # the builder's own rule (plain substring, this scope), kept so that any change the
        # bounded matching makes is listed (section 10, finding 1)
        res["substring_rule_file_commit"] = _first_substring(token, ref, commits)
        res["substring_rule_message_commit"] = msg[0] if msg else None
        res["bounded_rule_changes_first_record"] = (
            (res["file_hit"] or {}).get("commit") != res["substring_rule_file_commit"]
            or (res["message_hit"] or {}).get("commit") != res["substring_rule_message_commit"])
    if scope == "all":
        # the builder's scope (*.md, results/raw/, data/), kept so that every change the
        # widening makes is listed (section 10, finding 1)
        res["logs_scope"] = first_recording(token, ref, full, scope="logs")
        res["scope_changes_first_record"] = ((res["file_hit"] or {}).get("commit") != (res["logs_scope"]["file_hit"] or {}).get("commit"))
        if res["file_hit"] and not any(in_search_scope(p, "logs") for p in res["file_hit"]["paths"]):
            res["first_in_logs_raws_data"] = res["logs_scope"]
    return res


def grep_ref(token, ref):
    out = git("grep", "-n", "-i", "-F", "-e", token, ref, "--", ".", check=False)
    hits = []
    for gl in out.split("\n"):
        if not gl:
            continue
        parts = gl.split(":", 3)
        if len(parts) >= 4:
            hits.append({"locator": "%s@%s:%s" % (parts[1], ref[:7], parts[2]), "text": parts[3].strip()[:200]})
    return hits


# --------------------------------------------------------------------------
# Added-file index and cell evaluation
# --------------------------------------------------------------------------

def build_added(ref, flt="A"):
    out = git("log", "--reverse", "-M", "--diff-filter=" + flt, "--name-only", "--format=@@%H", ref, "--", "data", "results/raw")
    rows, cur = [], None
    for line in out.split("\n"):
        if line.startswith("@@"):
            cur = line[2:]
        elif line.strip() and cur:
            rows.append((cur, line.strip()))
    return rows


def build_modified(ref):
    """Commits that modify (M, not add) a file under data/ or results/raw/ (values-check pass 2, finding 3)."""
    return build_added(ref, "M")


def classify_mods(hits, add_commits):
    """Split modify-only hits by MODIFY_CLASS: (counted as data, listed as model-free, unclassified)."""
    data, free, uncl = [], [], []
    for cm, p in hits:
        k = cm[:7]
        rec = {"commit": k, "path": p, "committer_utc": meta(cm)["committer_utc"], "also_adds_in_commit": cm in add_commits}
        if k not in MODIFY_CLASS:
            rec["class"] = "UNCLASSIFIED"
            uncl.append((cm, p, rec))
        elif MODIFY_CLASS[k][0]:
            rec["class"] = "data (model output)"
            rec["what"] = MODIFY_CLASS[k][1]
            data.append((cm, p, rec))
        else:
            rec["class"] = "model-free"
            rec["what"] = MODIFY_CLASS[k][1]
            free.append((cm, p, rec))
    return data, free, uncl


FWD_MARK = re.compile(r'"provenance"|model loaded|loaded in \d|loading model|mlxlensmodel|"adapter"|loaded base|=== loading|forwards?:|'
                      r'"n_layers"|resid|logit|"kl|auc|"sessions?"', re.I)
_FWD = {}


def forward_markers(ref, path):
    """Markers of a forward pass in a same-subject file at ref (values-check pass 3, finding 6):
    a provenance block naming the model adapter, a model-load line, or reads, sessions,
    residuals, logits, KL or AUC fields. Evidence only: each file's class is declared after
    reading it (PRE_MODEL_FREE); a marker can come from weight loading or a provenance
    block without a forward. Binary arrays are not scanned (None)."""
    if (ref, path) in _FWD:
        return _FWD[(ref, path)]
    if path.endswith(".npz") or not exists_at(ref, path):
        out = None
    else:
        t = show_bytes(ref, path)[:400000].decode("utf-8", "replace")
        out = sorted(set(m.group(0).lower() for m in FWD_MARK.finditer(t)))
    _FWD[(ref, path)] = out
    return out


def json_top_keys(ref, path):
    """Top-level keys of a JSON file at ref (evidence for the same-subject classification), or
    'not one JSON document'; None for a file that is not .json."""
    if not path.endswith(".json") or not exists_at(ref, path):
        return None
    try:
        d = json.loads(show_bytes(ref, path).decode("utf-8", "replace"))
    except ValueError:
        return "not one JSON document"
    return list(d.keys()) if isinstance(d, dict) else "a JSON %s" % type(d).__name__


def locate(ref, path, needle, after=1):
    """First line at or after `after` in path at ref that contains needle: (locator, text) or (None, None)."""
    if not path or not needle or not exists_at(ref, path):
        return None, None
    L = lines_at(ref, path)
    for i in range(max(0, after - 1), len(L)):
        if needle in L[i]:
            return "%s@%s:%d" % (path, ref[:7], i + 1), L[i].strip()
    return None, None


def resolve_tier(t, ref):
    loc, txt = locate(ref, t["path"], t["needle"], t["after"])
    out = {"label": t["label"], "verdict_cell": t["label"].startswith("verdict"), "locator": loc, "text": clip(txt, 200) if txt else None,
           "why": t["why"], "needle_found": (loc is not None) if t["needle"] else None, "also": [],
           "log_only": t.get("log_only", False), "call": t.get("call")}
    for pth, nd, af in t["also"]:
        l2, t2 = locate(ref, pth, nd, af)
        out["also"].append({"locator": l2, "text": clip(t2, 200) if t2 else None, "needle_found": l2 is not None})
    return out


def match(path, globs, exclude):
    return any(fnmatch.fnmatchcase(path, g) for g in globs) and not any(fnmatch.fnmatchcase(path, g) for g in exclude)


def bounded_ok(cm, lo, hi):
    if lo is not None:
        lo_full = meta(lo)["commit"]
        if cm == lo_full or not is_ancestor(lo_full, cm):
            return False
    if hi is not None and not is_ancestor(cm, meta(hi)["commit"]):
        return False
    return True


def cell_hits(c, added):
    hits = []
    for cm, p in added:
        if match(p, c["globs"], c["exclude"]):
            hits.append((cm, p))
            continue
        for g, lo, hi in c.get("bounded", []):
            if fnmatch.fnmatchcase(p, g) and bounded_ok(cm, lo, hi):
                hits.append((cm, p))
                break
    return hits


def eval_cell(c, prereg_commit, added, ref, modified=()):
    hits = cell_hits(c, added)
    add_commits = set(cm for cm, _ in hits)
    mdata, mfree, muncl = classify_mods(cell_hits(c, modified), add_commits)
    out = {"name": c["name"], "globs": c["globs"], "exclude": c["exclude"], "bounded_globs": c.get("bounded", []), "verdict_cell": c["verdict"],
           "tier": resolve_tier(c["tier"], ref), "note": c["note"],
           "governing_commit": prereg_commit[:7], "inputs_only": c["inputs_only"],
           "modify_only_commits": [r for _, _, r in mdata + mfree + muncl]}
    # a modification that carries model output counts as data unless the same commit already adds a matching file
    hits = hits + [(cm, p) for cm, p, r in mdata if cm not in add_commits]
    hits.sort(key=lambda x: meta(x[0])["committer_unix"])
    if not hits:
        out.update({"first_data_commit": None, "status": "no data in the record"})
        return out
    first = hits[0][0]
    m = meta(first)
    paths_first = [p for cm, p in hits if cm == first]
    all_paths = sorted(set(p for cm, p in hits))
    commits = []
    for cm, p in hits:
        if cm not in commits:
            commits.append(cm)
    out.update({"first_data_commit": first, "first_data_short": first[:7], "first_data_committer_utc": m["committer_utc"],
                "first_data_subject": m["subject"], "first_data_paths": paths_first,
                "data_commits": [x[:7] for x in commits], "all_paths": all_paths,
                "data_commits_by_modification_only": [cm[:7] for cm, p, r in mdata if cm not in add_commits]})
    pm = meta(prereg_commit)
    if first == pm["commit"]:
        order = "same commit"
    elif is_ancestor(pm["commit"], first):
        order = "pre-registration first"
    else:
        order = "DATA FIRST"
    out["order_by_commit"] = order
    out["gap_days"] = round((m["committer_unix"] - pm["committer_unix"]) / 86400.0, 4)
    if c["result_entry"]:
        rm = meta(c["result_entry"])
        out["first_result_entry"] = {"commit": rm["commit"][:7], "committer_utc": rm["committer_utc"], "subject": rm["subject"][:160],
                                     "order": "pre-registration first" if is_ancestor(pm["commit"], rm["commit"]) and rm["commit"] != pm["commit"] else "NOT AFTER",
                                     "gap_days": round((rm["committer_unix"] - pm["committer_unix"]) / 86400.0, 4)}
    full, tonly, heads, jdt = [], [], [], []
    for p in all_paths:
        if not exists_at(ref, p):
            continue
        a, b, h, j = scan_file(ref, p)
        full += a
        tonly += b
        heads += h
        jdt += j
    out["json_datetime_strings"] = jdt[:4]
    out["json_datetime_strings_count"] = len(jdt)
    full.sort(key=lambda x: x["utc"])
    out["run_stamps_full"] = full[:6]
    out["run_stamps_full_count"] = len(full)
    out["run_stamp_earliest"] = full[0] if full else None
    out["run_stamps_time_only"] = tonly[:4]
    out["run_stamps_time_only_count"] = len(tonly)
    rh = []
    seen = set()
    for h in heads:
        r = resolve(h["hash"])
        key = (h["path"], h["line"], h["hash"])
        if key in seen:
            continue
        seen.add(key)
        h2 = dict(h)
        h2["resolves_to"] = r[:7] if r else None
        h2["governing_commit_is_ancestor"] = (is_ancestor(pm["commit"], r) if r else None)
        rh.append(h2)
    out["recorded_heads"] = rh
    if full:
        st = dt.datetime.strptime(full[0]["utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc).timestamp()
        out["run_stamp_minus_prereg_days"] = round((st - pm["committer_unix"]) / 86400.0, 4)
        out["run_stamp_after_prereg"] = st > pm["committer_unix"]
    if c["log_run_time"]:
        lr = c["log_run_time"]
        rx = re.compile(lr["re"])
        found = None
        for n, x in enumerate(lines_at(ref, lr["path"]), 1):
            mm = rx.search(x)
            if mm:
                found = (n, mm)
                break
        if found:
            n, mm = found
            d = dt.datetime.strptime(mm.group(2) + " " + mm.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
            out["log_run_time"] = {"locator": "%s@%s:%d" % (lr["path"], ref[:7], n), "verbatim": mm.group(0),
                                   "utc": d.strftime("%Y-%m-%dT%H:%M:%SZ"), "status": "log-only",
                                   "seconds_after_prereg_commit": int(d.timestamp() - pm["committer_unix"])}
    return out


# --------------------------------------------------------------------------
# Log-entry helpers
# --------------------------------------------------------------------------
ENTRY_START = re.compile(r"^- 20\d\d-\d\d-\d\d")


def entry_extent(lines, idx):
    j = idx + 1
    while j < len(lines) and (lines[j].strip() == "" or lines[j][:1] in (" ", "\t")):
        j += 1
    while j - 1 > idx and lines[j - 1].strip() == "":
        j -= 1
    return idx, j


def blame_origins(ref, path, s, e):
    out = git("blame", "-C", "-C", "--porcelain", "-L", "%d,%d" % (s, e), ref, "--", path)
    origins = []
    for line in out.split("\n"):
        m = re.match(r"^([0-9a-f]{40}) \d+ (\d+)", line)
        if m:
            origins.append((int(m.group(2)), m.group(1)))
    return origins


def eval_log_entry(row, ref):
    path, line, c = row["path"], row["line"], row["commit"]
    lines = lines_at(ref, path)
    s, e = entry_extent(lines, line - 1)
    header = lines[line - 1]
    origins = blame_origins(ref, path, line, line)
    header_origin = origins[0][1] if origins else None
    pm = meta(c)
    intro_path = "RESULTS.md"
    intro = lines_at(pm["commit"], intro_path)
    try:
        k = intro.index(header)
    except ValueError:
        k = None
    res = {"locator_ref": "%s@%s:%d" % (path, ref[:7], line),
           "header": clip(" ".join(x.strip() for x in lines[s:min(e, s + 4)]) + (" [...]" if e > s + 4 else ""), 420),
           "header_origin_commit": header_origin[:7] if header_origin else None,
           "header_origin_matches_declared": bool(header_origin and header_origin.startswith(meta(c)["commit"][:7]))}
    text_ref = "\n".join(lines[s:e]) + "\n"
    res["extent_ref"] = "%s@%s:%d-%d" % (path, ref[:7], s + 1, e)
    res["sha256_entry_at_ref"] = hashlib.sha256(text_ref.encode()).hexdigest()
    if k is not None:
        s2, e2 = entry_extent(intro, k)
        text_intro = "\n".join(intro[s2:e2]) + "\n"
        res["extent_at_introduction"] = "%s@%s:%d-%d" % (intro_path, pm["short"], s2 + 1, e2)
        res["sha256_entry_at_introduction"] = hashlib.sha256(text_intro.encode()).hexdigest()
        res["entry_identical_at_ref"] = text_intro == text_ref
        if text_intro != text_ref:
            sm = difflib.SequenceMatcher(a=text_intro.split("\n"), b=text_ref.split("\n"), autojunk=False)
            ops = [op for op in sm.get_opcodes() if op[0] != "equal"]
            res["entry_diff_ops"] = [{"op": o[0], "intro_lines": [o[1] + s2 + 1, o[2] + s2], "ref_lines": [o[3] + s + 1, o[4] + s]} for o in ops][:8]
    else:
        res["extent_at_introduction"] = None
        res["entry_identical_at_ref"] = None
    later = {}
    for ln, oc in blame_origins(ref, path, s + 1, e):
        if oc != pm["commit"] and is_ancestor(pm["commit"], oc):
            later.setdefault(oc, []).append(ln)
    res["later_commits_in_entry"] = [{"commit": k2[:7], "committer_utc": meta(k2)["committer_utc"], "subject": meta(k2)["subject"][:140],
                                      "ref_lines": [v[0], v[-1]], "n_lines": len(v)} for k2, v in sorted(later.items(), key=lambda kv: meta(kv[0])["committer_unix"])]
    return res


def eval_amendment(path, line, c, parent_cells, ref):
    lines = lines_at(ref, path)
    s, e = entry_extent(lines, line - 1)
    origins = blame_origins(ref, path, line, line)
    o = origins[0][1] if origins else None
    m = meta(c)
    preceding = []
    for pc in parent_cells:
        for dc in pc.get("data_commits") or []:
            dm = meta(dc)
            if dm["committer_unix"] < m["committer_unix"] and is_ancestor(dm["commit"], m["commit"]):
                preceding.append({"cell": pc["name"], "commit": dc, "committer_utc": dm["committer_utc"]})
    return {"locator_ref": "%s@%s:%d" % (path, ref[:7], line), "commit": m["short"], "committer_utc": m["committer_utc"],
            "header_origin_matches": bool(o and o.startswith(m["commit"][:7])),
            "header": clip(" ".join(x.strip() for x in lines[s:min(e, s + 5)]) + (" [...]" if e > s + 5 else ""), 520),
            "data_commits_of_the_cells_before_it": preceding}


# --------------------------------------------------------------------------
# Document helpers
# --------------------------------------------------------------------------

HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def diff_char(prev_commit, cur_commit, doc, old, new):
    """Hunks between two versions as git reports them (git diff -U0; values-check pass 1,
    finding 8: the earlier difflib-on-split('\\n') ranges ran past the end of the file).
    prev/this ranges are 1-based inclusive line ranges inside each file; an insertion has
    no previous range and is placed 'after previous line N' (N = 0: before line 1)."""
    if new.startswith(old):
        kind = "append-only (previous text is a prefix of this one)"
    elif new.endswith(old):
        kind = "prepend-only (previous text is a suffix of this one, unchanged below the new lines)"
    elif old in new:
        kind = "previous text preserved contiguously inside this one"
    else:
        kind = "edited (see hunks)"
    n_old = len(old.splitlines())
    out = git("diff", "--no-ext-diff", "--no-textconv", "--no-color", "-U0", prev_commit, cur_commit, "--", doc)
    hunks, add, rem, cur = [], 0, 0, None
    for line in out.split("\n"):
        m = HUNK.match(line)
        if m:
            a, b = int(m.group(1)), int(m.group(2)) if m.group(2) is not None else 1
            c_, d = int(m.group(3)), int(m.group(4)) if m.group(4) is not None else 1
            rem += b
            add += d
            if b == 0 and a == 0:
                # values-check pass 2, finding 8: an insertion before line 1 is a prepend, not a status-block edit
                where = "prepended before previous line 1 (%d new lines)" % d
            elif b == 0:
                where = "status block (previous lines 1-10)" if a <= 10 else ("end of file" if a >= n_old else "body")
            else:
                where = "status block (previous lines 1-10)" if a + b - 1 <= 10 else ("end of file" if a + b - 1 >= n_old else "body")
            cur = {"op": "insert" if b == 0 else ("delete" if d == 0 else "replace"),
                   "git_range": line.split("@@")[1].strip(),
                   "prev_lines": [a, a + b - 1] if b else None, "prev_insert_after_line": a if b == 0 else None,
                   "this_lines": [c_, c_ + d - 1] if d else None, "where": where,
                   "removed_text": [], "added_text": []}
            hunks.append(cur)
            continue
        if cur is None or line.startswith("\\"):
            continue
        # the ---/+++ file headers precede the first @@, where cur is still None
        if line.startswith("-"):
            cur["removed_text"].append(line[1:])
        elif line.startswith("+"):
            cur["added_text"].append(line[1:])
    for h in hunks:
        if len(h["removed_text"]) > 6 or len(h["added_text"]) > 6:
            h["text_omitted"] = "hunk longer than 6 lines; text not copied (see git diff -U0 %s %s -- %s)" % (prev_commit[:7], cur_commit[:7], doc)
            h.pop("removed_text")
            h.pop("added_text")
    scope = sorted(set(h["where"] for h in hunks))
    return {"kind": kind, "lines_removed": rem, "lines_added": add, "hunks": hunks, "n_hunks": len(hunks), "scope": scope,
            "lines_previous": n_old, "lines_this": len(new.splitlines()), "source": "git diff -U0"}


def span_lines(c, path, start_re, end_re):
    L = lines_at(c, path)
    s = next((i for i, x in enumerate(L) if re.search(start_re, x)), None)
    if s is None:
        return None
    e = next((i for i in range(s, len(L)) if re.search(end_re, L[i])), None)
    return (s + 1, (e + 1) if e is not None else None, L)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Row inclusion rule and census (values-check pass 1, finding 15)
# --------------------------------------------------------------------------
INCLUSION_RULE = [
    "(a) every PROPOSAL-*, LOCK-* and ADDENDUM-* document tracked at ref (block :90's referents), one row per document "
    "(PROPOSAL-m v1.11 included as a row that governs no data yet);",
    "(b) the three items block :91 names: the Q1 bet and the two welfare pre-commitments;",
    "(c) every top-level log entry in RESULTS.md, archive/RESULTS-cycles3-4.md and archive/RESULTS-cycle1-2.md whose "
    "header (the entry's first three lines) matches the census pattern below and itself registers a criterion, "
    "a design or a gate; N declarations (a sample size declared under criteria an earlier entry registers) and entries "
    "that only name a pre-registration are census hits but not rows;",
    "(d) one entry outside (c): the c1 gate read (row L-c1), whose header does not match the pattern but whose body "
    "calls the read 'Pre-registered' and which the r2 retry ran under unchanged.",
    "Amendments and adjudications inside an arc are listed under their parent row (section 2), not as rows.",
]
CENSUS_FILES = ["RESULTS.md", "archive/RESULTS-cycles3-4.md", "archive/RESULTS-cycle1-2.md"]
CENSUS_RE = r"PRE-REGISTRATION|PRE-REGISTERED|Pre-registration entry|Pre-registered design|\bLOCKED\b|\bDECLARATION\b|DECLARED BEFORE"
# census hits that are not rows: (path, header substring) -> (class, parent row, reason)
CENSUS_NONROWS = [
    ("archive/RESULTS-cycles3-4.md", "f1 smoke COMPLETE", "N declaration", "L-f1",
     "declares the screen's N under the f1 PRE-REGISTRATION's criteria (row L-f1)"),
    ("archive/RESULTS-cycles3-4.md", "e2a smoke3 PASS", "N declaration", "L-e2a",
     "declares the full run's N; the e2a PRE-REGISTRATION's header names the step ('smoke → N declaration → full run')"),
    ("archive/RESULTS-cycles3-4.md", "CYCLE 4 OPEN", "mention only", "L-f1",
     "names the f1 PRE-REGISTRATION as a later step of the order; registers no criterion itself"),
]
# items outside the census pattern, found by the values-checker, listed with their locators
EXTRA_NONROWS = [
    {"what": "cycle-1 pivot: 'Pre-registered failure mode for tail-PCA' (an archived operative document, not a PROPOSAL/LOCK/ADDENDUM document or a log entry; outside (a)-(d))",
     "path": "archive/CLAUDE-cycle1-2.md", "needle": "Pre-registered failure mode for tail-PCA",
     "cited_path": "archive/RESULTS-cycle1-2.md", "cited_needle": "the pivot's pre-registered"},
    {"what": "S1 per-cell n declaration (a sub-bullet of the entry that records PROPOSAL-g's commit; an N declaration under PROPOSAL-g's S1 criteria, row P-g)",
     "path": "RESULTS.md", "needle": "S1 per-cell n DECLARED BEFORE SCORING"},
]


def inclusion_census(ref, rows_out):
    rx = re.compile(CENSUS_RE)
    row_at = {}
    for r in rows_out:
        if r["kind"] == "log":
            row_at[r["entry"]["locator_ref"]] = r["id"]
    hits = []
    for f in CENSUS_FILES:
        L = lines_at(ref, f)
        for i, x in enumerate(L):
            if not ENTRY_START.match(x):
                continue
            head = " ".join(y.strip() for y in L[i:i + 3])
            if not rx.search(head):
                continue
            loc = "%s@%s:%d" % (f, ref[:7], i + 1)
            o = blame_origins(ref, f, i + 1, i + 1)
            h = {"locator": loc, "header": head[:300], "header_origin": o[0][1][:7] if o else None,
                 "matched": sorted(set(m.group(0) for m in rx.finditer(head)))}
            if loc in row_at:
                h["class"] = "row"
                h["row"] = row_at[loc]
            else:
                nr = next((n for n in CENSUS_NONROWS if n[0] == f and n[1] in head), None)
                if nr:
                    h.update({"class": nr[2], "parent_row": nr[3], "reason": nr[4]})
                else:
                    h["class"] = "UNCLASSIFIED"
            hits.append(h)
    extra = []
    for e in EXTRA_NONROWS:
        L = lines_at(ref, e["path"])
        n = next((i + 1 for i, x in enumerate(L) if e["needle"] in x), None)
        d = {"what": e["what"], "locator": ("%s@%s:%d" % (e["path"], ref[:7], n)) if n else None, "found": n is not None}
        # values-check pass 2, finding 2: search every path, not only the path the text sits at today
        fc = git("log", "--reverse", "-S" + e["needle"], "--format=%H", ref).split()
        fp = git("log", "--reverse", "-S" + e["needle"], "--format=%H", ref, "--", e["path"]).split()
        d["first_commit"] = ("%s %s" % (meta(fc[0])["short"], meta(fc[0])["committer_utc"])) if fc else None
        if fc:
            g = git("grep", "-n", "-F", "-e", e["needle"], fc[0], "--", ".", check=False).split("\n")
            g = [x.split(":", 3) for x in g if x]
            d["first_commit_locators"] = ["%s@%s:%s" % (x[1], fc[0][:7], x[2]) for x in g if len(x) >= 3]
        if fp and fc and fp[0] != fc[0]:
            d["first_commit_on_current_path"] = "%s %s" % (meta(fp[0])["short"], meta(fp[0])["committer_utc"])
        if e.get("cited_path"):
            Lc = lines_at(ref, e["cited_path"])
            m = next((i + 1 for i, x in enumerate(Lc) if e["cited_needle"] in x), None)
            d["cited_at"] = ("%s@%s:%d-%d" % (e["cited_path"], ref[:7], m, m + 1)) if m else None
            if m:
                o = blame_origins(ref, e["cited_path"], m, m)
                if o:
                    om = meta(o[0][1])
                    d["cited_line_origin"] = {"commit": om["short"], "committer_utc": om["committer_utc"],
                                              "days_after_first_text": round((om["committer_unix"] - meta(fc[0])["committer_unix"]) / 86400.0, 4) if fc else None}
        extra.append(d)
    tracked_docs = sorted(x for x in git("ls-tree", "--name-only", ref).split("\n")
                          if re.match(r"^(PROPOSAL|LOCK|ADDENDUM)-.*\.md$", x))
    doc_rows = {r["document"]: r["id"] for r in rows_out if r["kind"] == "doc"}
    return {"rule": INCLUSION_RULE, "pattern": CENSUS_RE, "files": CENSUS_FILES, "hits": hits, "extra_nonrows": extra,
            "tracked_documents": [{"document": d, "row": doc_rows.get(d)} for d in tracked_docs]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", default="bbc9ffe")
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--json-out", default=DEFAULT_JSON)
    a = ap.parse_args()
    for p in (a.out, a.json_out):
        ap_ = os.path.abspath(os.path.join(REPO, p)) if not os.path.isabs(p) else p
        if ap_.startswith(REPO + os.sep) and os.path.relpath(ap_, REPO) not in (DEFAULT_OUT, DEFAULT_JSON):
            sys.exit("refusing to write inside the repository except at the two assigned raw paths: %s" % p)
    out_md = a.out if os.path.isabs(a.out) else os.path.join(REPO, a.out)
    out_js = a.json_out if os.path.isabs(a.json_out) else os.path.join(REPO, a.json_out)

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
    ref = git("rev-parse", a.ref).strip()
    head = git("rev-parse", "HEAD").strip()
    script_path = os.path.abspath(__file__)
    script_sha = hashlib.sha256(open(script_path, "rb").read()).hexdigest()
    block_sha_ref = sha256_at(ref, BLOCK)
    wt_block = os.path.join(REPO, BLOCK)
    block_sha_wt = hashlib.sha256(open(wt_block, "rb").read()).hexdigest() if os.path.exists(wt_block) else None
    cmdline = shlex.join([sys.executable] + sys.argv)

    merges = git("rev-list", "--merges", ref).split()
    ac = git("log", "--format=%at %ct", ref).split("\n")
    ac_mismatch = sum(1 for x in ac if x.strip() and x.split()[0] != x.split()[1])
    census = {"first_raw_with_date_u_or_iso_utc": None, "first_raw_with_time_only_utc": None, "raws_scanned": 0}
    raws = sorted(git("ls-tree", "-r", "--name-only", ref, "results/raw").split())
    for f in raws:
        if f.startswith("results/raw/2026-10-08_note-") or not f.endswith((".txt", ".log", ".md")):
            continue
        census["raws_scanned"] += 1
        if census["first_raw_with_date_u_or_iso_utc"] and census["first_raw_with_time_only_utc"]:
            break
        a_, b_, _, _ = scan_file(ref, f)
        if a_ and not census["first_raw_with_date_u_or_iso_utc"]:
            census["first_raw_with_date_u_or_iso_utc"] = {"path": f, "line": a_[0]["line"], "verbatim": a_[0]["verbatim"]}
        if b_ and not census["first_raw_with_time_only_utc"]:
            census["first_raw_with_time_only_utc"] = {"path": f, "line": b_[0]["line"], "verbatim": b_[0]["verbatim"]}
    n_commits = int(git("rev-list", "--count", ref).strip())
    added = build_added(ref)
    modified = build_modified(ref)

    J = {"header": {"title": "AUDIT-note-release v1.2 -- N13 pre-registration provenance table",
                    "code_stamp_date_u": stamp, "HEAD": head, "ref": ref,
                    "block": BLOCK, "block_sha256_at_ref": block_sha_ref, "block_sha256_working_tree": block_sha_wt,
                    "block_sha256_routed": BLOCK_SHA_ROUTED, "block_sha_matches": block_sha_ref == BLOCK_SHA_ROUTED,
                    "script": os.path.relpath(script_path, REPO), "script_sha256": script_sha,
                    "interpreter": sys.executable, "python": sys.version.split()[0], "command": cmdline,
                    "history": {"commits_at_ref": n_commits, "merge_commits": len(merges), "author_time_ne_committer_time": ac_mismatch},
                    "raw_stamp_census": census}}

    # ---- date rule search ----
    J["date_rule"] = {
        "reflog_mentions_at_ref": grep_ref("reflog", ref),
        "timestamp_rule_lines": [h for h in grep_ref("timestamp of record", ref) if not h["locator"].startswith("results/raw/2026-10-08_note")]
        + [h for h in grep_ref("hash is the timestamp", ref)][:12]
        + [h for h in grep_ref("is this lock's timestamp", ref)][:4]
        + [h for h in grep_ref("is this document's timestamp", ref)][:4]
        + [h for h in grep_ref("is this addendum's timestamp", ref)][:4],
    }

    rows_out = []
    for row in ROWS:
        r = {"id": row["id"], "kind": row["kind"], "title": row["title"], "note": row.get("note", "")}
        if row["kind"] == "log":
            pm = meta(row["commit"])
            r.update({"document": "%s (log entry)" % row["path"], "tracked": True,
                      "version_of_record": "log entry as committed at %s" % pm["short"],
                      "record_commit": pm["commit"], **{k: pm[k] for k in ("author", "author_utc", "committer_utc", "author_unix", "committer_unix", "subject")}})
            r["entry"] = eval_log_entry(row, ref)
            r["content_sha256"] = r["entry"].get("sha256_entry_at_introduction")
            r["content_sha256_status"] = "computed-new (the record holds no content hash for a log entry)"
            r["recorded_sha256"] = {"found": False, "note": "a log entry has no content hash in the record; its commit is its timestamp"}
            gov = {cc["name"]: pm["commit"] for cc in row["cells"]}
            versions = [{"label": "log entry", "commit": pm["short"], "committer_utc": pm["committer_utc"]}]
        else:
            doc = row["doc"]
            fl = git("log", "--follow", "--reverse", "--format=%H", ref, "--", doc).split()
            versions = []
            prev, prev_c = None, None
            for c, label in row["versions"]:
                m = meta(c)
                v = {"label": label, "commit": m["short"], "commit_full": m["commit"], "author": m["author"],
                     "author_utc": m["author_utc"], "committer_utc": m["committer_utc"],
                     "author_unix": m["author_unix"], "committer_unix": m["committer_unix"],
                     "subject": m["subject"][:200], "sha256": sha256_at(c, doc), "git_blob": blob_at(c, doc),
                     "lines": len(lines_at(c, doc)) - 1}
                text = show_bytes(c, doc).decode("utf-8", "replace")
                if prev is not None:
                    v["change_from_previous"] = diff_char(prev_c, m["commit"], doc, prev, text)
                prev, prev_c = text, m["commit"]
                rec = first_recording(m["short"], ref, m["commit"])
                v["first_recording_of_commit_hash"] = rec
                srec = first_recording(v["sha256"][:8], ref, v["sha256"])
                v["first_recording_of_sha256"] = srec
                versions.append(v)
            listed = [meta(c)["commit"] for c, _ in row["versions"]]
            r["git_log_follow"] = [meta(c)["short"] for c in fl]
            r["unlisted_commits_touching_doc"] = [meta(c)["short"] for c in fl if c not in listed]
            rm = meta(row["record"])
            r.update({"document": doc, "tracked": True, "version_of_record": next(l for c, l in row["versions"] if c == row["record"]),
                      "record_commit": rm["commit"], **{k: rm[k] for k in ("author", "author_utc", "committer_utc", "author_unix", "committer_unix", "subject")}})
            r["content_sha256"] = sha256_at(row["record"], doc)
            r["content_sha256_status"] = None  # set with the recorded-hash search below (pass 2, finding 9)
            r["versions"] = versions
            r["later_commits"] = [v["commit"] for v in versions if v["commit"] != rm["short"]]
            if row.get("acceptance"):
                am = meta(row["acceptance"])
                r["acceptance_commit"] = {"commit": am["short"], "committer_utc": am["committer_utc"], "subject": am["subject"][:160],
                                          "touches_doc": row["acceptance"] in [x[:7] for x in fl]}
            gov = {}
            for cc in row["cells"]:
                gov[cc["name"]] = meta(row.get("cell_version", {}).get(cc["name"], row["record"]))["commit"]
            r["status_line_at_ref"] = " ".join(x.strip() for x in lines_at(ref, doc)[:8] if x.strip())[:360]
        cells = []
        for cc in row["cells"]:
            ce = eval_cell(cc, gov[cc["name"]], added, ref, modified)
            cells.append(ce)
        r["cells"] = cells
        if row["kind"] != "log":
            for v in r["versions"]:
                before = []
                for ce in cells:
                    for dc in ce.get("data_commits") or []:
                        dm = meta(dc)
                        if dm["committer_unix"] < v["committer_unix"] and dc not in [x["commit"] for x in before]:
                            before.append({"commit": dc, "committer_utc": dm["committer_utc"], "cell": ce["name"]})
                v["data_commits_of_row_cells_before_this_version"] = before
                gcells = [ce for ce in cells if ce["governing_commit"] == v["commit"] and ce.get("first_data_commit") and not ce.get("inputs_only")]
                v["governs_cells"] = [ce["name"] for ce in cells if ce["governing_commit"] == v["commit"]]
                if gcells:
                    fdc = min(gcells, key=lambda ce: meta(ce["first_data_commit"])["committer_unix"])
                    fm = meta(fdc["first_data_commit"])
                    v["first_data_of_governed_cells"] = {"commit": fm["short"], "committer_utc": fm["committer_utc"], "cell": fdc["name"],
                                                         "order": fdc["order_by_commit"], "gap_days": fdc["gap_days"]}
                    rc = v["first_recording_of_commit_hash"]
                    v["commit_hash_file_record_before_governed_data"] = (is_ancestor(rc["file_hit"]["commit"], fm["commit"]) and rc["file_hit"]["commit"] != fm["commit"]) if rc["file_hit"] else None
                    v["commit_hash_message_record_before_governed_data"] = (is_ancestor(rc["message_hit"]["commit"], fm["commit"]) and rc["message_hit"]["commit"] != fm["commit"]) if rc["message_hit"] else None
        # inputs for B1 declarations: the A4 artifacts
        for ce in cells:
            if ce.get("inputs_only"):
                a4 = eval_cell(cell("A4 inputs", A4, T_A4), meta("72b09a9")["commit"], added, ref, modified)
                ce["inputs"] = {"globs": A4, "first_commit": a4.get("first_data_short"), "committer_utc": a4.get("first_data_committer_utc"),
                                "PROPOSAL-g_72b09a9_precedes_inputs": a4.get("order_by_commit") == "pre-registration first",
                                "governing_commit_precedes_inputs": is_ancestor(gov[ce["name"]], a4["first_data_commit"]) if a4.get("first_data_commit") else None}
        # pre-data disclosures on the same subject
        # (values-check pass 1, finding 6: every row, log rows included, carries this line)
        rc = meta(row["record"] if row["kind"] != "log" else row["commit"])
        pg = row.get("pre_data_globs", [])
        def before_rec(cm):
            return cm != rc["commit"] and is_ancestor(cm, rc["commit"])
        pre = [(cm, p, "added") for cm, p in added if pg and match(p, pg, row.get("pre_data_exclude", [])) and before_rec(cm)]
        # values-check pass 2, finding 3: a modification carrying model output is data too
        pm_hits = [(cm, p) for cm, p in modified if pg and match(p, pg, row.get("pre_data_exclude", [])) and before_rec(cm)]
        pmd, pmf, pmu = classify_mods(pm_hits, set(cm for cm, _, _ in pre))
        pre += [(cm, p, "modified (model output)") for cm, p, _ in pmd + pmu]
        pre.sort(key=lambda x: meta(x[0])["committer_unix"])
        # values-check pass 3, findings 1 and 6: `files` lists file events (one per commit that adds or
        # extends a path); counts are of distinct paths, and model-free paths (PRE_MODEL_FREE) are counted apart
        added_paths = set(p for _, p, ch in pre if ch == "added")
        fev = [{"commit": cm[:7], "committer_utc": meta(cm)["committer_utc"], "path": p, "change": ch,
                "path_added_earlier_in_list": (ch != "added" and p in added_paths),
                "class": "model-free" if p in PRE_MODEL_FREE else "data",
                "what": PRE_MODEL_FREE.get(p) or PRE_DATA_BORDERLINE.get(p),
                "forward_markers": forward_markers(ref, p), "top_level_keys": json_top_keys(ref, p)} for cm, p, ch in pre]
        pdp, pmp = [], []
        for f_ in fev:
            lst = pmp if f_["class"] == "model-free" else pdp
            if f_["path"] not in lst:
                lst.append(f_["path"])
        r["pre_data"] = {"globs": pg, "exclude": row.get("pre_data_exclude", []), "label": row.get("pre_data_label", ""),
                         "files": fev, "n_file_events": len(fev),
                         "paths_data": pdp, "n_paths_data": len(pdp),
                         "paths_model_free": pmp, "n_paths_model_free": len(pmp),
                         "modify_only_commits": [x for _, _, x in pmd + pmf + pmu],
                         "log_entries_reporting_results_before": []}
        # values-check pass 2, finding 5: data in the pre-registration's own commit that the entry reports as already generated
        scp = []
        for sp in row.get("same_commit_prior", []):
            files = [p for cm, p in added if cm == rc["commit"] and match(p, sp["globs"], [])]
            reps = []
            for pth, nd, af in sp["reported"]:
                l2, t2 = locate(ref, pth, nd, af)
                reps.append({"locator": l2, "text": clip(t2, 200) if t2 else None})
            scp.append({"label": sp["label"], "commit": rc["short"], "committer_utc": rc["committer_utc"], "files": files,
                        "reported_in_entry": reps, "gloss": sp["gloss"]})
        r["pre_data"]["same_commit_prior"] = scp
        if row.get("no_verdict"):
            nv = row["no_verdict"]
            refs = []
            for pth, nd, af in nv["refs"]:
                l2, t2 = locate(ref, pth, nd, af)
                refs.append({"locator": l2, "text": clip(t2, 200) if t2 else None, "log_only": bool(l2 and not pth.startswith(("PROPOSAL", "LOCK", "ADDENDUM")))})
            dis = []
            for pth, nd, af, gl in nv.get("disclosure", []):
                l2, t2 = locate(ref, pth, nd, af)
                dis.append({"locator": l2, "text": clip(t2, 200) if t2 else None, "gloss": gl})
            r["no_verdict_tier"] = {"text": nv["text"], "refs": refs, "disclosure": dis}
            if nv.get("lock"):
                r["no_verdict_tier"]["lock_commits_any_branch"] = git("log", "--all", "--format=%h", "--", nv["lock"] + "*").split()
        for ec in row.get("pre_data_entries", []):
            em = meta(ec)
            r["pre_data"]["log_entries_reporting_results_before"].append(
                {"commit": em["short"], "committer_utc": em["committer_utc"], "subject": em["subject"],
                 "proper_ancestor_of_record": em["commit"] != rc["commit"] and is_ancestor(em["commit"], rc["commit"])})
        r["data_on_same_apparatus_before_record_commit"] = r["pre_data"]["files"]
        # code port of a log-only criterion (L-c1r3)
        if row.get("port"):
            pt = row["port"]
            pa = git("log", "--reverse", "--diff-filter=A", "--format=%H", ref, "--", pt["path"]).split()
            rp, rneedle = pt["regression"]
            rl = [i + 1 for i, x in enumerate(lines_at(ref, rp)) if rneedle in x]
            cf = [(cm, p) for cm, p in added if fnmatch.fnmatchcase(p, pt["configs"])]
            doc0 = lines_at(ref, pt["path"])[:3]
            vc = [ce for ce in cells if ce.get("first_data_commit") and ce["verdict_cell"]]
            fdm = meta(vc[0]["first_data_commit"]) if vc else None
            pm_ = meta(pa[0]) if pa else None
            r["port"] = {"path": pt["path"], "added_commit": pm_["short"] if pm_ else None, "added_utc": pm_["committer_utc"] if pm_ else None,
                         "added_subject": pm_["subject"] if pm_ else None,
                         "docstring_head": " ".join(x.strip() for x in doc0),
                         "regression_locator": ["%s@%s:%d" % (rp, ref[:7], n) for n in rl],
                         "configs": sorted(set("%s (%s)" % (p, cm[:7]) for cm, p in cf)),
                         "first_verdict_data_commit": fdm["short"] if fdm else None,
                         "port_after_first_verdict_data": (is_ancestor(fdm["commit"], pm_["commit"]) and fdm["commit"] != pm_["commit"]) if (fdm and pm_) else None,
                         "days_after_first_verdict_data": round((pm_["committer_unix"] - fdm["committer_unix"]) / 86400.0, 4) if (fdm and pm_) else None}
        if row.get("model_free_globs"):
            mf = [(cm, p) for cm, p in added if match(p, row["model_free_globs"], [])]
            r["model_free_artifacts_after"] = sorted(set((cm[:7], meta(cm)["committer_utc"]) for cm, p in mf), key=lambda x: x[1])
            r["model_free_artifact_count"] = len(mf)
        if row.get("amendments"):
            r["amendments_after_data"] = [eval_amendment(p, ln, c, cells, ref) for p, ln, c in row["amendments"]]
        # recorded hash (commit hash) for log rows
        if row["kind"] == "log":
            r["first_recording_of_commit_hash"] = first_recording(meta(row["commit"])["short"], ref, meta(row["commit"])["commit"])
        # welfare spans
        if row["kind"] == "welfare":
            sp_i = span_lines(row["record"], row["doc"], row["start_re"], row["end_re"])
            sp_r = span_lines(ref, row["doc"], row["start_re"], row["end_re"])
            Lr = lines_at(ref, row["doc"])
            cs = row["cited_span"]
            r["welfare"] = {"clause_lines_at_record_commit": [sp_i[0], sp_i[1]] if sp_i else None,
                            "clause_lines_at_ref": [sp_r[0], sp_r[1]] if sp_r else None,
                            "clause_identical": (sp_i and sp_r and sp_i[2][sp_i[0]-1:sp_i[1]] == sp_r[2][sp_r[0]-1:sp_r[1]]),
                            "clause_text_at_ref": re.sub(r"(" + row["end_re"] + r").*$", r"\1", re.sub(r"^.*?(?=" + row["start_re"].lstrip("^") + ")", "", " ".join(x.strip() for x in Lr[sp_r[0]-1:sp_r[1]]))) if sp_r else None,
                            "cited_span": "%s:%d-%d" % (row["doc"], cs[0], cs[1]),
                            "cited_span_text_at_ref": [x for x in Lr[cs[0]-1:cs[1]]],
                            "cited_span_inside_clause": bool(sp_r and sp_r[0] <= cs[0] and cs[1] <= sp_r[1]),
                            "cited_span_covers_whole_clause": bool(sp_r and cs[0] <= sp_r[0] and cs[1] >= sp_r[1]),
                            "citing_lines": [h for h in grep_ref(row["cite_token"], ref) if h["locator"].startswith("PROPOSAL-m")][:2]}
            tl = None
            for n, x in enumerate(lines_at(ref, "RESULTS.md"), 1):
                if re.search(row["trigger_re"], x):
                    tl = {"locator": "RESULTS.md@%s:%d" % (ref[:7], n), "text": x.strip()[:200], "status": "log-only"}
                    break
            r["welfare"]["trigger_outcome_in_log"] = tl
            if row.get("confirm_re"):
                cl = None
                for n, x in enumerate(lines_at(ref, "RESULTS.md"), 1):
                    if re.search(row["confirm_re"], x):
                        cl = {"locator": "RESULTS.md@%s:%d" % (ref[:7], n), "text": x.strip()[:200], "status": "log-only"}
                        break
                r["welfare"]["confirm_outcome_in_log"] = cl
        # Q1 bet specifics
        if row["kind"] == "bet":
            L0 = lines_at(row["record"], row["doc"])
            Lr = lines_at(ref, row["doc"])
            # lines carrying the bet's date; the window clause (':82' at the record commit,
            # 'RESULTS 2026-08-18, locked text') carries the date but is not the bet
            b_rec = [i + 1 for i, x in enumerate(L0) if "2026-08-18" in x and "Window clause" not in x]
            b_ref = [i + 1 for i, x in enumerate(Lr) if "2026-08-18" in x and "Window clause" not in x]
            ever = git("log", "--all", "--format=%h", "--", "HANDOFF-2026-08-18*").split()
            on_disk = sorted(f for f in os.listdir(REPO) if f.startswith("HANDOFF-2026-08-18"))
            first_text = git("log", "--reverse", "-S" + "pretraining acquisition", "--format=%h", ref).split()
            surv = [(cm, p) for cm, p in added if fnmatch.fnmatchcase(p, "data/olmo/rl_*.json")]
            r["bet"] = {"lines_at_record_commit": ["%s@%s:%d: %s" % (row["doc"], meta(row["record"])["short"], n, L0[n-1].strip()) for n in b_rec],
                        "lines_at_ref": ["%s@%s:%d" % (row["doc"], ref[:7], n) for n in b_ref],
                        "handoff_2026_08_18_commits_any_branch": ever, "handoff_2026_08_18_on_disk": on_disk,
                        "first_commit_with_phrase_pretraining_acquisition": first_text[0] if first_text else None,
                        "rl_survey_commit": {"commit": surv[0][0][:7], "committer_utc": meta(surv[0][0])["committer_utc"]} if surv else None,
                        "bet_commit_after_survey_commit": is_ancestor(surv[0][0], row["record"]) if surv else None,
                        "bet_commit_minus_survey_commit_days": round((meta(row["record"])["committer_unix"] - meta(surv[0][0])["committer_unix"]) / 86400.0, 4) if surv else None}
        # status
        # values-check pass 1, finding 3: a declaration cell with no forwards (inputs_only) is not
        # data under the rule, so it enters neither 'first data', 'first verdict data' nor the order test
        # values-check pass 2, findings 4-5: the order test reads every governed cell with data
        # (block :91, 'the cell it governs'); verdict cells are a reported subset
        datacells = [ce for ce in cells if ce.get("first_data_commit") and not ce.get("inputs_only")]
        vcells = [ce for ce in datacells if ce["verdict_cell"]]
        orders = [ce.get("order_by_commit") for ce in datacells]
        rec_sha = None
        if row["kind"] != "log":
            vr = next(v for v in r["versions"] if v["commit"] == meta(row["record"])["short"])
            fh = vr["first_recording_of_sha256"]["file_hit"]
            rec_sha = fh
            r["recorded_sha256"] = {"found": bool(fh), "first": fh}
            if fh:
                first_data = min((meta(ce["first_data_commit"]) for ce in datacells), key=lambda x: x["committer_unix"], default=None)
                r["recorded_sha256"]["recorded_before_first_data"] = (is_ancestor(fh["commit"], first_data["commit"]) and fh["commit"] != first_data["commit"]) if first_data else "no data"
                # explicit prefix check: a recorded token must be a prefix of the recomputed sha256
                toks = re.findall(r"[0-9a-f]{8,64}", " ".join(x["text"] for x in fh["lines"]))
                r["recorded_sha256"]["recorded_tokens"] = toks[:4]
                r["recorded_sha256"]["matches_recomputed"] = any(r["content_sha256"].startswith(t) for t in toks)
        # recorded commit hash before data
        if row["kind"] == "log":
            fr = r["first_recording_of_commit_hash"]
        else:
            fr = next(v for v in r["versions"] if v["commit"] == meta(row["record"])["short"])["first_recording_of_commit_hash"]
        first_data = min((meta(ce["first_data_commit"]) for ce in datacells), key=lambda x: x["committer_unix"], default=None)
        rh = fr["file_hit"]
        r["recorded_commit_hash"] = {"first_file_record": rh, "first_message_record": fr["message_hit"]}
        if first_data and rh:
            r["recorded_commit_hash"]["file_record_before_first_data"] = is_ancestor(rh["commit"], first_data["commit"]) and rh["commit"] != first_data["commit"]
        if rh:
            r["recorded_commit_hash"]["file_record_paths"] = rh["paths"]
            r["recorded_commit_hash"]["same_commit_as_declaration_cell"] = [ce["name"] for ce in cells if ce.get("inputs_only") and ce.get("first_data_commit") == rh["commit"]]
            if fr.get("first_in_logs_raws_data"):
                lh = fr["first_in_logs_raws_data"]["file_hit"]
                r["recorded_commit_hash"]["first_record_in_logs_raws_data"] = lh
                if lh and first_data:
                    r["recorded_commit_hash"]["log_record_before_first_data"] = is_ancestor(lh["commit"], first_data["commit"]) and lh["commit"] != first_data["commit"]
                    r["recorded_commit_hash"]["log_record_same_commit_as_first_data"] = lh["commit"] == first_data["commit"]
        if first_data and fr["message_hit"]:
            r["recorded_commit_hash"]["message_record_before_first_data"] = is_ancestor(fr["message_hit"]["commit"], first_data["commit"]) and fr["message_hit"]["commit"] != first_data["commit"]
        if not datacells:
            # values-check pass 4, finding 1: block :93's hash conjunct has no data qualifier, so a
            # row without data whose sha256 is recorded nowhere says so in its status
            status = "NO GOVERNED DATA IN THE RECORD" if rec_sha else "NO GOVERNED DATA IN THE RECORD; NO SHA256 RECORDED"
        elif any(o == "DATA FIRST" for o in orders):
            status = "STOP (order)"
        elif any(o == "same commit" for o in orders):
            status = "STOP (same commit: order not shown)"
        elif rec_sha and not r["recorded_sha256"]["matches_recomputed"]:
            status = "STOP (hash mismatch)"
        elif rec_sha and r["recorded_sha256"].get("recorded_before_first_data") is True:
            status = "PASS"
        elif rec_sha:
            status = "ORDER HOLDS; SHA256 RECORDED ONLY AFTER DATA"
        else:
            status = "ORDER HOLDS; NO SHA256 RECORDED"
        if datacells and not vcells and status.startswith("ORDER"):
            status += "; NO VERDICT-TIER DATA (%s)" % ((r.get("no_verdict_tier") or {}).get("text") or "no verdict cell")
        # values-check pass 2, finding 1: the Q1 date is a referent note, not a STOP
        if row["kind"] == "bet" and r.get("bet") and not r["bet"]["handoff_2026_08_18_commits_any_branch"] and status.startswith("ORDER HOLDS"):
            status = status.replace("ORDER HOLDS", "ORDER HOLDS for Q1 cells", 1) + "; 2026-08-18 DATE NOT EVIDENCED IN THE RECORD (referent note, section 8)"
        r["status"] = status
        # content-sha256 status (values-check pass 2, finding 9)
        if row["kind"] != "log":
            for v in r["versions"]:
                sh = v["first_recording_of_sha256"]["file_hit"]
                toks = re.findall(r"[0-9a-f]{8,64}", " ".join(x["text"] for x in sh["lines"])) if sh else []
                if sh and any(v["sha256"].startswith(t) for t in toks):
                    locs = [l for x in sh["lines"] for l in (x["locators_at_ref"] or [x["locator_at_commit"]])]
                    v["sha256_status"] = "reproduced (matches the value recorded at %s)" % ", ".join(locs[:3])
                elif sh:
                    v["sha256_status"] = "discrepant (a recorded prefix does not match)"
                else:
                    v["sha256_status"] = "computed-new (no recorded value in the record)"
            r["content_sha256_status"] = next(v for v in r["versions"] if v["commit"] == meta(row["record"])["short"])["sha256_status"]
        r["first_data_overall"] = ({"commit": first_data["short"], "committer_utc": first_data["committer_utc"],
                                    "gap_days": round((first_data["committer_unix"] - r["committer_unix"]) / 86400.0, 4),
                                    "order": ("pre-registration first" if is_ancestor(r["record_commit"], first_data["commit"]) and first_data["commit"] != r["record_commit"]
                                              else ("same commit" if first_data["commit"] == r["record_commit"] else "DATA FIRST"))}
                                   if first_data else None)
        rows_out.append(r)

    rows_out.sort(key=lambda x: (x["committer_unix"], x["id"]))
    J["rows"] = rows_out

    # ---- modify-only commits matched by a declared path (values-check pass 2, finding 3) ----
    mix = {}
    for r in rows_out:
        for ce in r["cells"]:
            for m_ in ce.get("modify_only_commits", []):
                e = mix.setdefault((m_["commit"], m_["path"]), dict(m_, cells=[], pre_data_rows=[]))
                e["cells"].append("%s / %s" % (r["id"], ce["name"]))
        for m_ in r["pre_data"].get("modify_only_commits", []):
            e = mix.setdefault((m_["commit"], m_["path"]), dict(m_, cells=[], pre_data_rows=[]))
            e["pre_data_rows"].append(r["id"])
    J["modify_only_index"] = sorted(mix.values(), key=lambda x: (x["committer_utc"], x["path"]))
    # every tier, same-commit and no-verdict needle must resolve at ref (pass 2)
    nf = []
    for r in rows_out:
        for ce in r["cells"]:
            t = ce["tier"]
            if t.get("needle_found") is False or any(not a["needle_found"] for a in t.get("also", [])):
                nf.append("%s / %s (tier)" % (r["id"], ce["name"]))
        for sp in r["pre_data"].get("same_commit_prior", []):
            if any(not x["locator"] for x in sp["reported_in_entry"]) or not sp["files"]:
                nf.append("%s / %s (same-commit prior data)" % (r["id"], sp["label"]))
        nvt = r.get("no_verdict_tier") or {}
        if any(not x["locator"] for x in nvt.get("refs", []) + nvt.get("disclosure", [])):
            nf.append("%s (no-verdict locators)" % r["id"])
    J["needles_not_found"] = nf
    if nf:
        print("WARNING: needles not found: %s" % "; ".join(nf), file=sys.stderr)
    # values-check pass 3, finding 4: every cell with data carries the line its tier rests on
    J["data_cells_without_tier_locator"] = ["%s / %s" % (r["id"], ce["name"]) for r in rows_out for ce in r["cells"]
                                            if ce.get("first_data_commit") and not ce["tier"].get("locator")]
    if J["data_cells_without_tier_locator"]:
        print("WARNING: data cells without a tier locator: %s" % "; ".join(J["data_cells_without_tier_locator"]), file=sys.stderr)
    # values-check pass 3, finding 6: each declared model-free or borderline path is in some row's same-subject list
    seen_pre = set(f["path"] for r in rows_out for f in r["pre_data"]["files"])
    J["pre_class_declared_not_seen"] = sorted(p for p in list(PRE_MODEL_FREE) + list(PRE_DATA_BORDERLINE) if p not in seen_pre)
    if J["pre_class_declared_not_seen"]:
        print("WARNING: declared same-subject classes not seen: %s" % ", ".join(J["pre_class_declared_not_seen"]), file=sys.stderr)

    # ---- untracked ----
    unt = []
    for f, desc in UNTRACKED:
        p = os.path.join(REPO, f)
        ever = git("log", "--all", "--format=%h", "--", f).split()
        sha = hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None
        st = None
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="replace") as fh:
                st = " ".join(x.strip() for x in fh.read().split("\n")[:6] if x.strip())[:300]
        unt.append({"file": f, "description": desc, "present_on_disk": os.path.exists(p),
                    "commits_touching_path_any_branch": ever, "sha256_working_tree": sha,
                    "sha_prefix_hits_in_record": grep_ref(sha[:16], ref) if sha else [],
                    "status_line": st})
    J["untracked"] = unt

    # ---- anchors ----
    J["anchors"] = []
    for c, what in ANCHORS:
        m = meta(c)
        J["anchors"].append({"anchor": c, "design_seat_says": what, "resolves": m["commit"], "committer_utc": m["committer_utc"],
                             "author_utc": m["author_utc"], "subject": m["subject"][:200]})

    # ---- other welfare text ----
    # values-check pass 2, finding 7: every tracked *.md at ref, no cap; the operative documents'
    # lines are listed in the raw, the rest are counted per file (all lines in the JSON)
    WELF = "welfare|pre-commitment"
    g = git("grep", "-n", "-i", "-E", "-e", WELF, ref, "--", "*.md", ":(exclude)results/raw/2026-10-08_note-*", ":(exclude)AUDIT-note-*", check=False)
    hits = []
    for gl in g.split("\n"):
        parts = gl.split(":", 3)
        if len(parts) >= 4:
            hits.append({"path": parts[1], "line": int(parts[2]), "locator": "%s@%s:%s" % (parts[1], ref[:7], parts[2]), "text": parts[3].strip()})
    op = [h for h in hits if re.match(r"^(PROPOSAL|LOCK|ADDENDUM|FINDINGS)-[^/]*\.md$", h["path"])]
    per_file = {}
    for h in hits:
        if h not in op:
            per_file[h["path"]] = per_file.get(h["path"], 0) + 1
    J["other_welfare_text"] = {"pattern": WELF, "case_insensitive": True, "scope": "tracked *.md at ref, this block and this audit's raws excluded",
                               "n_hits": len(hits), "operative_document_lines": op,
                               "other_files_counts": sorted(per_file.items(), key=lambda kv: (-kv[1], kv[0])), "all_hits": hits}

    # ---- the record's own date audit (RESULTS.md, RECORD HYGIENE entry) ----
    L = lines_at(ref, "RESULTS.md")
    hy_start = next(i for i, x in enumerate(L) if "RECORD HYGIENE: my entry date stamps ran AHEAD" in x)
    hy = []
    T1 = re.compile(r"^\s*\|\s*`([0-9a-f]{7})`[^|]*\|\s*\**(\d{4}-\d\d-\d\d) (\d\d:\d\d)(?::\d\d)?\**\s*\|[^|]*\|\s*(\d{4}-\d\d-\d\d)\s*\|")
    T2 = re.compile(r"^\s*\|\s*(\d{4}-\d\d-\d\d)[^|]*\|\s*`([0-9a-f]{7})`(?:…`([0-9a-f]{7})`)?[^|]*\|\s*(\d{4}-\d\d-\d\d) (\d\d:\d\d)(?:–(\d\d:\d\d))?")

    def hyrow(i, commit, claimed, stamp, kind):
        mm = meta(commit)
        u = mm["committer_utc"].replace("T", " ")[:16]
        loc = local_edt(mm["committer_unix"])
        d_utc = dt.date.fromisoformat(u[:10])
        delta = (dt.date.fromisoformat(stamp) - d_utc).days if stamp else None
        return {"locator": "RESULTS.md@%s:%d" % (ref[:7], i + 1), "row_kind": kind, "commit": commit,
                "claimed_true_utc": claimed, "git_utc": u, "git_local_edt": loc,
                "claimed_equals": "UTC" if claimed == u else ("EDT local (-04:00)" if claimed == loc else "neither"),
                "entry_stamp": stamp, "stamp_minus_utc_date_days": delta}

    for i in range(hy_start, min(len(L), hy_start + 60)):
        x = L[i]
        m = T1.match(x)
        if m:
            hy.append(hyrow(i, m.group(1), m.group(2) + " " + m.group(3), m.group(4), "named row"))
            continue
        m = T2.match(x)
        if m:
            hy.append(hyrow(i, m.group(2), m.group(4) + " " + m.group(5), m.group(1), "audit row"))
            if m.group(3) and m.group(6):
                hy.append(hyrow(i, m.group(3), m.group(4) + " " + m.group(6), m.group(1), "audit row (range end)"))
            continue
    region = "\n".join(L[hy_start:min(len(L), hy_start + 60)])
    for m in re.finditer(r"`([0-9a-f]{7})` at\s+\*\*(\d{4}-\d\d-\d\d) (\d\d:\d\d) UTC\*\*", region):
        ln = hy_start + region[:m.start()].count("\n")
        hy.append(hyrow(ln, m.group(1), m.group(2) + " " + m.group(3), None, "status-line commit"))
    J["record_date_audit_check"] = {"entry_locator": "RESULTS.md@%s:%d" % (ref[:7], hy_start + 1), "rows": hy}

    # ---- claims of pre-registration whose registration is not found before data ----
    claims = []
    A12 = lines_at(ref, "archive/RESULTS-cycle1-2.md")
    ln = next((i + 1 for i, x in enumerate(A12) if "Per the pre-registered rule" in x), None)
    first_t = git("log", "--reverse", "-S|t| < 1", "--format=%H", ref).split()
    rc = meta("08d2f9a")
    claims.append({"claim": "'Per the pre-registered rule (|t| < 1), the DV does not carry strain preference'",
                   "locator": "archive/RESULTS-cycle1-2.md@%s:%s-%s" % (ref[:7], ln, ln + 1 if ln else None),
                   "first_commit_containing_string": meta(first_t[0])["short"] if first_t else None,
                   "first_commit_utc": meta(first_t[0])["committer_utc"] if first_t else None,
                   "result_commit": rc["short"], "result_commit_utc": rc["committer_utc"],
                   "registration_found_before_result": bool(first_t) and first_t[0] != rc["commit"] and is_ancestor(first_t[0], rc["commit"])})
    c1g = git("log", "--all", "--format=%h", "--", "scripts/c1_gate.py", "**/c1_gate.py").split()
    r3 = next(r for r in rows_out if r["id"] == "L-c1r3")
    pt = r3.get("port") or {}
    claims.append({"claim": "c1 gate read (P1-P3/S1) and c1 r3 criterion 'implemented ... in scripts/c1_gate.py'",
                   "locator": "archive/RESULTS-cycle1-2.md@%s:1707-1708 and :1896-1898" % ref[:7],
                   "commits_tracking_c1_gate_py_any_branch": c1g,
                   "r3_criterion_code_port": {"path": pt.get("path"), "added_commit": pt.get("added_commit"), "added_utc": pt.get("added_utc"),
                                              "after_r3_verdict_data": pt.get("port_after_first_verdict_data"),
                                              "days_after_r3_verdict_data": pt.get("days_after_first_verdict_data"),
                                              "regression_locator": pt.get("regression_locator"), "configs": pt.get("configs")},
                   "registration_found_before_result": ("before the data, as log prose only (scripts/c1_gate.py was never tracked); "
                                                        "the r3 criterion's code entered the record afterwards as %s at %s (%s), %s d after the r3 data; "
                                                        "the r1/r2 P1-P3/S1 gate read has no code in the record" % (
                                                            pt.get("path"), pt.get("added_commit"), pt.get("added_utc"), pt.get("days_after_first_verdict_data")))})
    J["claims_check"] = claims

    # ---- the record's dating convention, quoted whole (values-check pass 1, finding 11) ----
    pm_lines = lines_at(ref, "PROPOSAL-m-gating-campaign-v1_11.md")
    dc = next(((i + 1, x) for i, x in enumerate(pm_lines) if x.startswith("*Dating convention:")), None)
    J["date_rule"]["dating_convention_line"] = {"locator": "PROPOSAL-m-gating-campaign-v1_11.md@%s:%d" % (ref[:7], dc[0]), "text": dc[1]} if dc else None

    # ---- row inclusion rule and census (values-check pass 1, finding 15) ----
    J["inclusion"] = inclusion_census(ref, rows_out)

    # ---- stops, notes, PI items (assembled from the computed values) ----
    build_reading(J)
    build_values_check_pass3(J, added, modified)
    analysis_only_commits(J, added, modified)
    build_values_check_pass4(J, added, modified)
    write_outputs(J, out_md, out_js)


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

def from_note(ce, row_commit):
    """' (from `x`)' when the cell's governing commit is not the row's displayed commit."""
    return "" if ce["governing_commit"] == row_commit[:7] else " (from `%s`)" % ce["governing_commit"]


def fmt_cell_line(ce):
    if ce.get("inputs_only"):
        if not ce.get("first_data_commit"):
            return "%s: no declaration in the record" % ce["name"]
        return ("%s: declaration commit `%s` (%s), %s, %.4f d after the governing commit; no forwards, so not data under the rule "
                "and not in the order test" % (ce["name"], ce["first_data_short"], ce["first_data_committer_utc"], ce["order_by_commit"], ce["gap_days"]))
    if not ce.get("first_data_commit"):
        return "%s: no data in the record" % ce["name"]
    s = "%s: first data commit `%s` (%s), %s" % (ce["name"], ce["first_data_short"], ce["first_data_committer_utc"], ce["order_by_commit"])
    s += ", gap %.4f d" % ce["gap_days"]
    if ce.get("first_result_entry"):
        fr = ce["first_result_entry"]
        s += "; first log entry reporting data `%s` (%s), gap %.4f d" % (fr["commit"], fr["committer_utc"], fr["gap_days"])
    return s


def stamp_kind(line_text):
    t = (line_text or "")
    if re.search(r"EXIT|exit|finished|FINISHED|done\b|DONE", t):
        return "exit stamp"
    if re.search(r"launch|LAUNCH|start|START|begin|BEGIN", t):
        return "start stamp"
    return "stamp"


def stamp_str(ce):
    if not ce.get("first_data_commit"):
        return "-"
    out = None
    if ce.get("run_stamp_earliest"):
        e = ce["run_stamp_earliest"]
        out = "%s %s (%s:%d)" % (stamp_kind(e.get("line_text")), e["utc"], e["path"].split("/")[-1], e["line"])
    elif ce.get("run_stamps_time_only"):
        t = ce["run_stamps_time_only"][0]
        dc = t["date_context"]
        out = "time-only '%s' (%s:%d%s)" % (t["verbatim"], t["path"].split("/")[-1], t["line"],
                                           ("; date in file at line %d: %s" % (dc["line"], dc["date"])) if dc else "; no date in file")
    else:
        out = "none in artifact/raw"
    if ce.get("log_run_time"):
        lr = ce["log_run_time"]
        out += "; launch %s [log-only: %s]" % (lr["utc"], lr["locator"])
    return out


def hash_recorded_cell(r, fd):
    """The table's 'Hash recorded' cell."""
    rs = r.get("recorded_sha256", {})
    rc = r.get("recorded_commit_hash", {})
    hs = []
    if rs.get("found"):
        hs.append("sha256 at `%s` %s (%s)" % (rs["first"]["commit"][:7], rs["first"]["committer_utc"],
                                             {True: "before data", False: "not before data", "no data": "no data"}.get(rs.get("recorded_before_first_data"), str(rs.get("recorded_before_first_data")))))
    else:
        hs.append("sha256: none")
    fh = rc.get("first_file_record")
    mh = rc.get("first_message_record")

    def lab(k):
        return "no data" if not fd else ("before data" if rc.get(k) else "not before data")
    if fh:
        extra = []
        if rc.get("same_commit_as_declaration_cell"):
            extra.append("same commit as the %s, which runs no forwards" % rc["same_commit_as_declaration_cell"][0].split(" (")[0])
        code_paths = [p for p in fh["paths"] if not in_search_scope(p, "logs")]
        if code_paths and len(code_paths) == len(fh["paths"]):
            extra.append("in %s" % ", ".join("%s@%s:%d" % (l["path"], fh["commit"][:7], l["line_at_commit"]) for l in fh["lines"] if l["path"] in code_paths))
        s = "commit hash at `%s` %s (%s%s)" % (fh["commit"][:7], fh["committer_utc"], lab("file_record_before_first_data"), ("; " + "; ".join(extra)) if extra else "")
        if "first_record_in_logs_raws_data" in rc:
            lh = rc["first_record_in_logs_raws_data"]
            if lh:
                s += "; first log/raw/data record `%s` %s (%s)" % (lh["commit"][:7], lh["committer_utc"],
                                                                   "same commit as data" if rc.get("log_record_same_commit_as_first_data") else
                                                                   ("before data" if rc.get("log_record_before_first_data") else ("not before data" if fd else "no data")))
            else:
                s += "; no log/raw/data record"
        hs.append(s)
    elif mh:
        hs.append("commit hash in message of `%s` %s (%s)" % (mh["commit"][:7], mh["committer_utc"], lab("message_record_before_first_data")))
    else:
        hs.append("commit hash: none")
    return "; ".join(hs)


def pre_count_str(r, log_word="earlier log entries", always_log=False):
    """A row's same-subject count (values-check pass 3, findings 1 and 6): distinct data paths,
    model-free paths apart, and earlier log entries."""
    pdx = r["pre_data"]
    nm, ne = pdx["n_paths_model_free"], len(pdx["log_entries_reporting_results_before"])
    s = "%s (%s" % (r["id"], nfiles(pdx["n_paths_data"]))
    if nm:
        s += ", plus %d model-free file%s" % (nm, "" if nm == 1 else "s")
    if ne or always_log:
        s += ", %d %s" % (ne, log_word)
    return s + ")"


def recording_lines(fh, k=2):
    return "; ".join("%s [ref: %s] '%s'" % (l["locator_at_commit"], more(l["locators_at_ref"], 6, "file_hit.lines[].locators_at_ref") or "line not at ref", clip(l["text"], 140)) for l in fh["lines"][:k])


def write_outputs(J, out_md, out_js):
    H = J["header"]
    o = []
    w = o.append
    w("# AUDIT-note-release v1.2 -- N13: pre-registration provenance table")
    w("")
    w("- Code stamp (`date -u`, inside the script): %s" % H["code_stamp_date_u"])
    w("- HEAD at run: `%s`; every figure below is computed at the pinned ref `%s`" % (H["HEAD"], H["ref"]))
    w("- Block: `%s`, sha256 at ref `%s` (routed `%s`: %s)" % (H["block"], H["block_sha256_at_ref"], H["block_sha256_routed"], "MATCH" if H["block_sha_matches"] else "MISMATCH"))
    w("- Script: `%s`, sha256 `%s`" % (H["script"], H["script_sha256"]))
    w("- Interpreter: `%s` (Python %s); stdlib only" % (H["interpreter"], H["python"]))
    w("- Command: `%s`" % H["command"])
    w("- History at ref: %d commits, %d merge commits; commits whose author time differs from committer time: %d." % (H["history"]["commits_at_ref"], H["history"]["merge_commits"], H["history"]["author_time_ne_committer_time"]))
    w("- Regeneration: deterministic at a fixed ref apart from the stamp, HEAD and command lines.")
    w("- Values-check: passes 1 to 4 (an adversarial checker's findings) are applied in this version; section 10 lists each finding and its disposition, pass by pass.")
    w("@@REDACTION@@")
    w("")
    w("## Item outcome")
    w("")
    for x in J["outcome"]:
        w(x)
    w("")
    w("## 0. Method, rules and definitions")
    w("")
    dcl = J["date_rule"].get("dating_convention_line")
    w("- **Dates.** Every date is git's, printed in UTC from the commit's Unix time (author and committer). "
      "The block asks for 'the reflog Unix timestamp where the lab's date rule says it governs'. Searched at ref: "
      "'reflog' occurs %d times, all in the block itself or in values-check raws that used the local reflog to read HEAD history; "
      "none states a date rule. The record's own rule is %s, in full: \"%s\" Each document's status line says the same of its own commit "
      "(lines listed in the JSON, `date_rule.timestamp_rule_lines`). No rule in the record makes a reflog "
      "time govern, so none is used; the reflog is local and absent from any clone. Git's Unix times are given in the JSON (`*_unix`)." % (
          len(J["date_rule"]["reflog_mentions_at_ref"]), dcl["locator"] if dcl else "PROPOSAL-m v1.11 (line not found)", dcl["text"].strip("*") if dcl else ""))
    w("- **Order.** 'pre-registration first' means the governing commit is a proper ancestor of the data commit "
      "(`git merge-base --is-ancestor`; history is linear), which does not depend on clocks. Gaps are committer-time differences in days, "
      "measured from the commit of the version that governs the cell. The order test reads every cell a pre-registration governs (block :91: "
      "'the first data-generating commit for the cell it governs'). Data on the same subject committed before a version of record, or in its own "
      "commit and reported by its entry as already generated, are not governed by it; each row lists them (section 2).")
    w("- **Data rule (declared).** A cell's data are artifacts or run raws produced by forward passes of the subject model on that cell's stimuli. "
      "Model-free artifacts (power, budget, arithmetic, values-checks, frac tables, stub or synthetic selftests, replays of archived text, human read marks, "
      "download, cast and hashing logs, tokenizer-only checks) are not data; "
      "the ones adjacent to a cell are named in its note, and in a row's same-subject list they are counted apart from the data files (section 2; counts are of distinct paths, "
      "JSON `pre_data.paths_data` and `pre_data.paths_model_free`, while `pre_data.files` lists file events, one per commit that adds or extends a path). " +
      ("Analyses computed from forward outputs, including re-analyses committed without new forwards (e.g. %s; values-check pass 4, finding 3), are counted with the data. " % (
          ", ".join("`%s`" % x["commit"] for x in J["analysis_only_commits"]) or "none in the record")) +
      "A declaration that runs no forwards (B1, 'read off the committed A4 artifacts') is a declaration cell: "
      "its commit is shown, but it is not data and is not in the order test. 'First data commit' is the first commit that adds a file matching the cell's declared paths "
      "(git log -M --diff-filter=A, so a rename is not an addition; where one path is added twice by different runs, the path is bounded by commit). "
      "A cell's data commits also include every commit that only modifies a matching file with model output (git log -M --diff-filter=M; "
      "each such commit is classified by reading it, in the table below). The paths per cell are in the JSON (`cells[].globs`, `cells[].exclude`, `cells[].bounded_globs`).")
    w("- **Verdict cells.** " + VERDICT_DEFINITION)
    w("- **Run stamps.** Every text file of each cell is scanned at ref for `date -u` stamps, ISO UTC times, time-only UTC stamps, and recorded "
      "HEAD/lock commits; each stamp is labelled by its line (exit, start, or plain stamp); section 7 gives the census of which raws carry stamps at all; "
      "where a cell's raws carry none the table says so. A recorded HEAD or lock line inside a run raw is checked for ancestry against the governing commit.")
    w("- **Recorded hash.** For each version: (a) its content sha256, searched as an 8-hex prefix, and (b) its 7-hex commit hash, each with `git log -S` "
      "over every tracked path and in commit messages. A line records the value only where a hex run bounded by non-hex characters starts with the token and "
      "is a prefix of the full value (so a longer hash that merely contains the token is not a record of it). Excluded: `*.npz`, this block, and this audit's own "
      "raws and scripts (`results/raw/2026-10-08_note-*`, `scripts/audit_note_*`; the preflight raw committed at bbc9ffe lists several of these sha256 values, after all data). "
      "The first commit that adds a record is the recording commit; its line is given at that commit and at ref. Where that first record is in code "
      "(outside `*.md`, `results/raw/`, `data/`), the first record in a log, raw or data file is given as well.")
    w("- **Status vocabulary for rows.** PASS = order holds and a recorded sha256 matches the recomputed one. "
      "ORDER HOLDS; NO SHA256 RECORDED = every governed cell's data follow the governing commit, but no content sha256 of the version exists in the record, so the block's hash conjunct cannot be met as written "
      "(absence, not mismatch: Code's reading of block :93, which names a STOP for a hash that 'does not match', for the PI to confirm; so no hash STOP is declared). "
      "'NO VERDICT-TIER DATA (...)' marks a row whose governed data all lie outside a verdict tier, with the reason. "
      "'for Q1 cells; 2026-08-18 DATE NOT EVIDENCED IN THE RECORD' marks the Q1 row's referent note (section 8). "
      "STOP (order) / STOP (hash mismatch) as block :93. NO GOVERNED DATA IN THE RECORD = no data file matches the cell. " +
      ("NO GOVERNED DATA IN THE RECORD; NO SHA256 RECORDED = no data file matches the cell, and no content sha256 of the version exists in the record; block :93's hash "
       "conjunct ('every row's recomputed sha matches the recorded one') has no data qualifier, so it is unmet for such a row too, under the same reading of absence "
       "(%s; values-check pass 4, finding 1). " % (", ".join(J["hash_unmet_no_data"]) or "no row")) +
      "Content sha256 status (rule 4 of the routing): 'computed-new' where the record holds no value to reproduce, 'reproduced' where a recorded prefix matches.")
    w("- **Redaction.** Quoted record text is redacted per the routing's rule 6: a RunPod pod or volume id, a volume name, a container id or an SSH port is replaced by its first 4 characters + '...' + its length + ':' + sha256[:8] (ports: 'len5:' + sha256[:8]); the values are matched by sha256 prefix and never written in the script.")
    w("- **Rows.** Which entries count as pre-registrations of record is Code's declared rule, with its census and exclusions, in section 9.")
    w("")
    w("Modify-only commits matched by a declared cell or pre-data path (git log -M --diff-filter=M over `data/` and `results/raw/` at ref; each read with `git show`). "
      "'data' = the modification carries model output: it is counted in a cell's data-commit list unless the same commit already adds a file matching that cell, and the modified file is listed in a row's same-subject data; 'model-free' = listed here only:")
    w("")
    w("| Commit (committer UTC) | Path | Class | What the modification is | Also adds a matching file in the commit | Cells whose paths it matches | Rows whose same-subject paths it matches |")
    w("|---|---|---|---|---|---|---|")
    for m_ in J["modify_only_index"]:
        w("| `%s` %s | `%s` | %s | %s | %s | %s | %s |" % (m_["commit"], m_["committer_utc"], m_["path"], m_["class"], m_.get("what", "-"),
                                                     m_["also_adds_in_commit"], "; ".join(m_["cells"]) or "-", ", ".join(m_["pre_data_rows"]) or "-"))
    w("")

    # ---- summary table ----
    w("## 1. Provenance table (for README-NOTE.md)")
    w("")
    shs = [r["id"] for r in J["rows"] if (r.get("content_sha256_status") or "").startswith("reproduced")]
    w("Rows are ordered by the pre-registration commit's time. 'sha256' is the version of record's content hash, computed by `git show <commit>:<path>` "
      "(first 16 hex; full values in section 2 and the JSON); for a log-entry row it is computed over the entry text as introduced. Its status (routing rule 4): "
      "computed-new for every row except %s, whose value reproduces the one recorded in the record (column 'Hash recorded'; JSON `content_sha256_status`). 'Hash recorded' gives "
      "the earliest record of the version's sha256 and of its commit hash, and whether that record precedes the row's first data commit. 'First data' is the "
      "row's earliest data commit over all its governed cells; 'first verdict data' is the earliest over its verdict cells (definition in section 0), and where a row has none "
      "the cell says why, with its locators; a declaration cell with no forwards is shown "
      "in the first-data cell but is in neither. Gaps and order are measured from the commit of the version that governs the cell (per-version table); where "
      "that is not the row's displayed commit, the cell names it as '(from `x`)'." % (", ".join(shs) or "none"))
    w("")
    w("| # | Pre-registration (version of record) | Commit (committer UTC) | sha256 (16) | Hash recorded | First data (cell) | First verdict data | Run stamp in raw | Gap to first / verdict data (d) | Order (first / verdict) | Status |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(J["rows"], 1):
        datacells = [c for c in r["cells"] if c.get("first_data_commit") and not c.get("inputs_only")]
        vcells = [c for c in r["cells"] if c.get("first_data_commit") and c["verdict_cell"] and not c.get("inputs_only")]
        decl = [c for c in r["cells"] if c.get("inputs_only") and c.get("first_data_commit")]
        fd = min(datacells, key=lambda c: c["first_data_committer_utc"]) if datacells else None
        fv = min(vcells, key=lambda c: c["first_data_committer_utc"]) if vcells else None
        doc = r["document"] if r["kind"] != "log" else r["entry"]["locator_ref"]
        title = "%s<br>`%s` (%s)" % (r["title"], doc, r["version_of_record"])
        fdc = ("`%s` %s (%s)" % (fd["first_data_short"], fd["first_data_committer_utc"], fd["name"])) if fd else "none"
        for c in decl:
            ip = c.get("inputs", {})
            fdc += "; %s: declaration `%s` %s, no forwards (inputs A4 `%s` %s; PROPOSAL-g `72b09a9` precedes them: %s; this row's governing commit precedes them: %s%s)" % (
                c["name"].split(" (")[0], c["first_data_short"], c["first_data_committer_utc"], ip.get("first_commit"), ip.get("committer_utc"),
                ip.get("PROPOSAL-g_72b09a9_precedes_inputs"), ip.get("governing_commit_precedes_inputs"),
                ", by design" if ip.get("governing_commit_precedes_inputs") is False else "")
        nvt = r.get("no_verdict_tier")
        fvc = ("`%s` %s (%s)" % (fv["first_data_short"], fv["first_data_committer_utc"], fv["name"])) if fv else (
            "none" if not fd else ("none: %s [%s]" % (nvt["text"], "; ".join(("log-only: " if x["log_only"] else "") + (x["locator"] or "NOT FOUND") for x in nvt["refs"])) if nvt else "none: no verdict cell"))
        st = stamp_str(fv or fd) if (fv or fd) else "-"
        gap = ("%.4f%s / %s" % (fd["gap_days"], from_note(fd, r["record_commit"]), ("%.4f%s" % (fv["gap_days"], from_note(fv, r["record_commit"]))) if fv else "-")) if fd else "-"
        order = ("%s / %s" % (fd["order_by_commit"], fv["order_by_commit"] if fv else "-")) if fd else "-"
        w("| %d | %s | `%s` %s | `%s` | %s | %s | %s | %s | %s | %s | %s |" % (
            i, title.replace("|", "/"), r["record_commit"][:7], r["committer_utc"], (r["content_sha256"] or "")[:16],
            hash_recorded_cell(r, fd), fdc, fvc, st, gap, order, r["status"]))
    w("")
    w("Version-level ordering (documents with more than one committed version, and every version's governed cells):")
    w("")
    w("| Row | Version | Commit (committer UTC) | sha256 (16) | Change from previous (git diff -U0) | Governs | First data of governed cells (UTC) | Gap (d) | Order | Commit hash recorded before governed data | Row data committed before this version |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in J["rows"]:
        if r["kind"] == "log" or len(r.get("versions", [])) < 2:
            continue
        for v in r["versions"]:
            cf = v.get("change_from_previous")
            chg = ("%s; -%d/+%d lines; hunks %s; where: %s" % (cf["kind"].split(" (")[0], cf["lines_removed"], cf["lines_added"],
                                                              ", ".join("`%s`" % h["git_range"] for h in cf["hunks"]), ", ".join(cf["scope"]))) if cf else "first version"
            fdv = v.get("first_data_of_governed_cells")
            rec = v.get("commit_hash_file_record_before_governed_data")
            recm = v.get("commit_hash_message_record_before_governed_data")
            bef = v.get("data_commits_of_row_cells_before_this_version") or []
            w("| %s | %s | `%s` %s | `%s` | %s | %s | %s | %s | %s | %s | %s |" % (
                r["id"], v["label"], v["commit"], v["committer_utc"], v["sha256"][:16], chg,
                "; ".join(v.get("governs_cells") or []) or "-",
                ("`%s` %s" % (fdv["commit"], fdv["committer_utc"])) if fdv else "none",
                ("%.4f" % fdv["gap_days"]) if fdv else "-", fdv["order"] if fdv else "-",
                ("file: %s; message: %s" % ("no record" if rec is None else rec, "no record" if recm is None else recm)) if fdv else "-",
                ("%d (%s)" % (len(bef), ", ".join("`%s`" % x["commit"][:7] for x in bef))) if bef else "0"))
    w("")
    w("Untracked texts (not in the record; a clone of the tag does not contain them):")
    w("")
    w("| File | What it is | Ever committed (any branch) | sha256 (working tree) | Prefix recorded in the record |")
    w("|---|---|---|---|---|")
    for u in J["untracked"]:
        hits = more([h["locator"] for h in u["sha_prefix_hits_in_record"]], 3, "untracked[].sha_prefix_hits_in_record") or "none"
        w("| `%s` | %s | %s | `%s` | %s |" % (u["file"], u["description"], ", ".join(u["commits_touching_path_any_branch"]) or "no", u["sha256_working_tree"], hits))
    w("")

    # ---- per-row detail ----
    w("## 2. Per-row detail")
    w("")
    for i, r in enumerate(J["rows"], 1):
        w("### %d. %s [%s]" % (i, r["title"], r["id"]))
        w("")
        if r["kind"] == "log":
            e = r["entry"]
            w("- Document: log entry %s (extent %s); introduced at `%s` (author %s; author %s, committer %s, unix %d). Header line's blame origin (`git blame -C -C`): `%s` (%s)." % (
                e["locator_ref"], e["extent_ref"], r["record_commit"][:7], r["author"], r["author_utc"], r["committer_utc"], r["committer_unix"],
                e["header_origin_commit"], "matches" if e["header_origin_matches_declared"] else "DOES NOT MATCH"))
            w("- Header: %s" % clip(e["header"], 420))
            w("- Entry sha256 (computed-new): at introduction %s = `%s`; at ref = `%s`; identical: %s." % (
                e.get("extent_at_introduction"), e.get("sha256_entry_at_introduction"), e["sha256_entry_at_ref"], e.get("entry_identical_at_ref")))
            if e.get("later_commits_in_entry"):
                for lc in e["later_commits_in_entry"]:
                    w("  - later commit with lines in this entry: `%s` %s (%d lines, ref lines %d-%d): %s" % (lc["commit"], lc["committer_utc"], lc["n_lines"], lc["ref_lines"][0], lc["ref_lines"][1], clip(lc["subject"], 140)))
            if e.get("entry_diff_ops"):
                w("  - diff ops introduction -> ref: %s" % json.dumps(e["entry_diff_ops"]))
        else:
            w("- Document: `%s`; version of record: %s at `%s` (author %s; author %s, committer %s, unix %d)." % (
                r["document"], r["version_of_record"], r["record_commit"][:7], r["author"], r["author_utc"], r["committer_utc"], r["committer_unix"]))
            w("- `git log --follow` at ref: %s; commits touching the file not listed as versions: %s." % (", ".join("`%s`" % x for x in r["git_log_follow"]), ", ".join(r["unlisted_commits_touching_doc"]) or "none"))
            if r.get("acceptance_commit"):
                ac = r["acceptance_commit"]
                w("- Acceptance commit `%s` (%s): %s; touches the document: %s." % (ac["commit"], ac["committer_utc"], clip(ac["subject"], 160), ac["touches_doc"]))
            w("- Status line at ref: %s" % clip(r["status_line_at_ref"], 360))
            for v in r["versions"]:
                w("- Version %s: `%s`, author %s / committer %s (equal: %s), sha256 `%s` (%s), git blob `%s`, %d lines." % (
                    v["label"], v["commit"], v["author_utc"], v["committer_utc"], v["author_unix"] == v["committer_unix"], v["sha256"], v.get("sha256_status"), v["git_blob"], v["lines"]))
                if v.get("change_from_previous"):
                    cf = v["change_from_previous"]
                    w("  - change from previous version (git diff -U0; previous %d lines, this %d): %s; %d lines removed, %d added, %d hunk(s): %s" % (
                        cf["lines_previous"], cf["lines_this"], cf["kind"], cf["lines_removed"], cf["lines_added"], cf["n_hunks"], json.dumps(cf["hunks"])))
                if v.get("data_commits_of_row_cells_before_this_version"):
                    w("  - data commits of this row's cells committed before this version (%d): %s" % (len(v["data_commits_of_row_cells_before_this_version"]), ", ".join("`%s` %s (%s)" % (x["commit"][:7], x["committer_utc"], x["cell"]) for x in v["data_commits_of_row_cells_before_this_version"])))
                if v.get("first_data_of_governed_cells"):
                    fdv = v["first_data_of_governed_cells"]
                    nr = lambda x: "no record" if x is None else x
                    w("  - governs: %s; first data of those cells `%s` %s (%s, gap %.4f d); commit-hash record before it: file %s, message %s" % ("; ".join(v["governs_cells"]), fdv["commit"], fdv["committer_utc"], fdv["order"], fdv["gap_days"], nr(v.get("commit_hash_file_record_before_governed_data")), nr(v.get("commit_hash_message_record_before_governed_data"))))
                rs = v["first_recording_of_sha256"]
                if rs["file_hit"]:
                    fh = rs["file_hit"]
                    w("  - sha256 first recorded at `%s` (%s): %s" % (fh["commit"][:7], fh["committer_utc"], recording_lines(fh)))
                else:
                    w("  - sha256: no 8-hex prefix of `%s` is recorded in any tracked file or commit message (audit files excluded)%s." % (v["sha256"][:8], "" if not rs["message_hit"] else " (message hit: `%s`)" % rs["message_hit"]["commit"][:7]))
                rc = v["first_recording_of_commit_hash"]
                if rc["file_hit"]:
                    fh = rc["file_hit"]
                    w("  - commit hash `%s` first recorded in a file at `%s` (%s): %s" % (v["commit"], fh["commit"][:7], fh["committer_utc"], recording_lines(fh)))
                    if rc.get("first_in_logs_raws_data"):
                        lh = rc["first_in_logs_raws_data"]["file_hit"]
                        w("  - commit hash `%s` first recorded in a log, raw or data file: %s" % (v["commit"], ("`%s` (%s): %s" % (lh["commit"][:7], lh["committer_utc"], recording_lines(lh))) if lh else "none"))
                else:
                    w("  - commit hash `%s`: not recorded in any tracked file." % v["commit"])
                if rc["message_hit"]:
                    w("  - commit hash `%s` first in a commit message: `%s` (%s) '%s'" % (v["commit"], rc["message_hit"]["commit"][:7], rc["message_hit"]["committer_utc"], clip(rc["message_hit"]["subject"], 140)))
        if r["kind"] == "log":
            rc = r["first_recording_of_commit_hash"]
            if rc["file_hit"]:
                fh = rc["file_hit"]
                w("- Commit hash `%s` first recorded in a file at `%s` (%s): %s" % (r["record_commit"][:7], fh["commit"][:7], fh["committer_utc"], recording_lines(fh)))
                if rc.get("first_in_logs_raws_data"):
                    lh = rc["first_in_logs_raws_data"]["file_hit"]
                    w("- Commit hash `%s` first recorded in a log, raw or data file: %s" % (r["record_commit"][:7], ("`%s` (%s): %s" % (lh["commit"][:7], lh["committer_utc"], recording_lines(lh))) if lh else "none"))
            else:
                w("- Commit hash `%s`: not recorded in any tracked file." % r["record_commit"][:7])
            if rc["message_hit"]:
                w("- Commit hash `%s` first in a commit message: `%s` (%s)." % (r["record_commit"][:7], rc["message_hit"]["commit"][:7], rc["message_hit"]["committer_utc"]))
        rc = r.get("recorded_commit_hash", {})
        if "file_record_before_first_data" in rc:
            qual = ""
            if "first_record_in_logs_raws_data" in rc:
                qual = " (%s record%s)" % ("script" if all(p.startswith("scripts/") for p in rc["file_record_paths"]) else "code",
                                           "; the log record is in the data commit" if rc.get("log_record_same_commit_as_first_data") else
                                           ("; the log record also precedes the data" if rc.get("log_record_before_first_data") else "; the log record follows the data"))
            elif rc.get("same_commit_as_declaration_cell"):
                qual = " (the record is in the %s's commit, which runs no forwards)" % rc["same_commit_as_declaration_cell"][0].split(" (")[0]
            w("- Commit-hash record precedes the first data commit: %s%s." % (rc["file_record_before_first_data"], qual))
        if r.get("note"):
            w("- Note: %s" % r["note"])
        if r.get("port"):
            pt = r["port"]
            w("- Code port of the criterion: `%s` added at `%s` (%s; '%s'); docstring opens: '%s'; regression check at %s; gate JSONs %s; the port follows the first verdict data `%s`: %s (%.4f d after)." % (
                pt["path"], pt["added_commit"], pt["added_utc"], clip(pt["added_subject"], 160), clip(pt["docstring_head"], 200),
                ", ".join(pt["regression_locator"]) or "none", ", ".join(pt["configs"]) or "none", pt["first_verdict_data_commit"], pt["port_after_first_verdict_data"], pt["days_after_first_verdict_data"]))
        w("- Cells:")
        for ce in r["cells"]:
            w("  - %s (governed by `%s`; verdict cell: %s)." % (fmt_cell_line(ce), ce["governing_commit"], ce["verdict_cell"]))
            tr = ce["tier"]
            tl = "    - tier: %s" % tr["label"]
            lo = "[log-only] " if tr.get("log_only") else ""
            if tr["locator"]:
                tl += " -- %s%s '%s'" % (lo, tr["locator"], tr["text"])
            elif tr.get("needle_found") is False:
                tl += " -- NEEDLE NOT FOUND"
            for al in tr.get("also", []):
                tl += "; %s%s '%s'" % (lo, al["locator"] or "NOT FOUND", al["text"])
            if tr.get("why"):
                tl += " (%s)" % tr["why"]
            w(tl)
            for m_ in ce.get("modify_only_commits", []):
                w("    - modify-only commit `%s` (%s) on `%s`: %s%s" % (m_["commit"], m_["committer_utc"], m_["path"], m_["class"],
                                                                  ("; " + m_["what"]) if m_.get("what") else ""))
            if ce.get("first_data_commit"):
                w("    - first paths: %s; %s (%d): %s" % (more(["`%s`" % p for p in ce["first_data_paths"]], 4, "cells[].first_data_paths"),
                                                      "declaration commits" if ce.get("inputs_only") else "data commits", len(ce["data_commits"]), ", ".join(ce["data_commits"])))
                w("    - run stamp: %s%s" % (stamp_str(ce), ("; the earliest full stamp is %s the governing commit (%.4f d)" % ("after" if ce.get("run_stamp_after_prereg") else "NOT after", ce["run_stamp_minus_prereg_days"])) if ce.get("run_stamp_earliest") else ""))
                for h in ce.get("recorded_heads", []):
                    w("    - recorded in the raw: `%s` (%s:%d) -> `%s`; governing commit is its ancestor: %s" % (clip(h["verbatim"], 150), h["path"].split("/")[-1], h["line"], h["resolves_to"], h["governing_commit_is_ancestor"]))
                if ce.get("log_run_time"):
                    lr = ce["log_run_time"]
                    w("    - launch time in the log [log-only]: '%s' at %s = %s, %d s after the governing commit." % (lr["verbatim"], lr["locator"], lr["utc"], lr["seconds_after_prereg_commit"]))
                if ce.get("json_datetime_strings_count"):
                    j0 = ce["json_datetime_strings"][0]
                    w("    - datetime strings inside the cell's JSON artifacts (not run stamps): %d, e.g. %s:%d '%s'" % (ce["json_datetime_strings_count"], j0["path"], j0["line"], clip(j0["context"], 120)))
            if ce.get("inputs"):
                ip = ce["inputs"]
                w("    - inputs (A4 artifacts): first commit `%s` (%s); PROPOSAL-g `72b09a9` precedes them: %s; this row's governing commit precedes them: %s." % (ip["first_commit"], ip["committer_utc"], ip["PROPOSAL-g_72b09a9_precedes_inputs"], ip["governing_commit_precedes_inputs"]))
            if ce.get("note"):
                w("    - cell note: %s" % ce["note"])
        pdx = r.get("pre_data", {})
        pre = pdx.get("files", [])
        lab = (" -- %s" % pdx["label"]) if pdx.get("label") else ""
        dpre = [p for p in pre if p["class"] == "data"]
        mpre = [p for p in pre if p["class"] == "model-free"]

        def in_commits(lst):
            cs = []
            for p in lst:
                if p["commit"] not in cs:
                    cs.append(p["commit"])
            return ", ".join("`%s` (%s)" % (c, next(p["committer_utc"] for p in lst if p["commit"] == c)) for c in cs)
        if dpre:
            # values-check pass 3, finding 1: distinct paths; a path extended after its addition is not 'by modification only'
            ext = [p for p in dpre if p["change"] != "added" and p["path_added_earlier_in_list"]]
            monly = [p for p in dpre if p["change"] != "added" and not p["path_added_earlier_in_list"]]
            w("- Data on the same subject committed before the version of record (not governed by it)%s: %s in %s%s%s." % (
                lab, nfiles(pdx["n_paths_data"]), in_commits(dpre),
                ("; %s" % "; ".join("`%s` (added at `%s`) was extended with model output at `%s`" % (
                    p["path"], next(q["commit"] for q in dpre if q["path"] == p["path"] and q["change"] == "added"), p["commit"]) for p in ext)) if ext else "",
                ("; by modification only (the path is not added in this list): %s" % ", ".join("`%s` at `%s`" % (p["path"], p["commit"]) for p in monly)) if monly else ""))
            for p in dpre:
                if p.get("what"):
                    w("  - counted as data, with a note: `%s` -- %s." % (p["path"], p["what"]))
        else:
            w("- Data on the same subject committed before the version of record: none under the declared paths (%s)%s." % (", ".join("`%s`" % g for g in pdx.get("globs", [])) or "none declared", lab if pdx.get("log_entries_reporting_results_before") else ""))
        if mpre:
            # values-check pass 3, finding 6: model-free files are counted apart from the data
            w("- Model-free files on the same subject committed before the version of record (no forward of the subject model, so not data under section 0's rule; listed for completeness): %s in %s: %s." % (
                nfiles(pdx["n_paths_model_free"]), in_commits(mpre), "; ".join("`%s` (%s%s)" % (
                    pp, PRE_MODEL_FREE[pp], (" [log-only: %s]" % (locate(H["ref"], *PRE_MODEL_FREE_QUOTE[pp])[0] or "NOT FOUND")) if pp in PRE_MODEL_FREE_QUOTE else "")
                    for pp in pdx["paths_model_free"])))
        for le in pdx.get("log_entries_reporting_results_before", []):
            w("  - log entry reporting same-subject results before it: `%s` (%s; proper ancestor of the record commit: %s): %s" % (le["commit"], le["committer_utc"], le["proper_ancestor_of_record"], clip(le["subject"], 150)))
        for sp in pdx.get("same_commit_prior", []):
            w("- Data on the same subject committed with the version of record, in its own commit `%s` (%s), and reported by the entry as already generated when it was written (not governed by it): %s: %s; %s: %s." % (
                sp["commit"], sp["committer_utc"], sp["label"], ", ".join("`%s`" % f for f in sp["files"]) or "NO FILE FOUND", sp["gloss"],
                "; ".join("%s '%s'" % (x["locator"] or "NOT FOUND", x["text"]) for x in sp["reported_in_entry"])))
        if r.get("no_verdict_tier"):
            nv = r["no_verdict_tier"]
            w("- No verdict-tier data: %s. %s%s%s" % (nv["text"], "; ".join("%s%s '%s'" % ("[log-only] " if x["log_only"] else "", x["locator"] or "NOT FOUND", x["text"]) for x in nv["refs"]),
                                                   (". %s: commits touching the path on any branch: %s" % ("LOCK file", ", ".join(nv["lock_commits_any_branch"]) or "none")) if "lock_commits_any_branch" in nv else "",
                                                   "".join(". Disclosed: %s (%s '%s')" % (d["gloss"], d["locator"] or "NOT FOUND", d["text"]) for d in nv["disclosure"])) + ".")
        if r.get("model_free_artifacts_after") is not None:
            w("- Model-free artifacts under `data/m/` at ref: %d files in %s (no model forward)." % (r["model_free_artifact_count"], ", ".join("`%s` (%s)" % x for x in r["model_free_artifacts_after"])))
        if r.get("amendments_after_data"):
            w("- Amendments and adjudications inside the arc (each entry's own words; preceding data commits computed):")
            for am in r["amendments_after_data"]:
                pre_ = am["data_commits_of_the_cells_before_it"]
                w("  - %s `%s` (%s; header origin matches: %s): %s" % (am["locator_ref"], am["commit"], am["committer_utc"], am["header_origin_matches"], clip(am["header"], 420)))
                w("    - data commits of this row's cells before it: %s" % (", ".join(sorted(set("`%s`" % p["commit"][:7] for p in pre_))) or "none"))
        if r.get("welfare"):
            wf = r["welfare"]
            w("- Clause lines at record commit %s, at ref %s; identical: %s." % (wf["clause_lines_at_record_commit"], wf["clause_lines_at_ref"], wf["clause_identical"]))
            w("- Clause at ref: \"%s\"" % wf["clause_text_at_ref"])
            w("- Cited span %s at ref: %s; inside the clause: %s; covers the whole clause: %s." % (wf["cited_span"], json.dumps(wf["cited_span_text_at_ref"]), wf["cited_span_inside_clause"], wf["cited_span_covers_whole_clause"]))
            w("- Citing line(s) in PROPOSAL-m: %s" % ("; ".join(h["locator"] for h in wf["citing_lines"]) or "none found"))
            if wf.get("trigger_outcome_in_log"):
                t = wf["trigger_outcome_in_log"]
                w("- Trigger condition outcome [log-only]: %s: '%s'" % (t["locator"], clip(t["text"], 160)))
            if wf.get("confirm_outcome_in_log"):
                t = wf["confirm_outcome_in_log"]
                w("- Confirm tier [log-only]: %s: '%s'; no B3 confirm artifact is in the record (the cell's paths match screen and analysis files only)." % (t["locator"], clip(t["text"], 160)))
        if r.get("bet"):
            b = r["bet"]
            w("- Bet lines at the record commit (lines carrying the bet's date; the window clause, which carries the same date, is not the bet): %s" % " | ".join(b["lines_at_record_commit"]))
            w("- Same lines at ref: %s" % ", ".join(b["lines_at_ref"]))
            w("- HANDOFF-2026-08-18 (the source PROPOSAL-g cites for the 2026-08-18 date): commits touching the path on any branch: %s; on disk at root: %s." % (b["handoff_2026_08_18_commits_any_branch"] or "none", b["handoff_2026_08_18_on_disk"] or "none"))
            w("- First commit containing the bet's phrase 'pretraining acquisition': `%s`. R_l survey commit: `%s` (%s); the bet's first commit comes after it: %s (%.4f d after)." % (b["first_commit_with_phrase_pretraining_acquisition"], b["rl_survey_commit"]["commit"], b["rl_survey_commit"]["committer_utc"], b["bet_commit_after_survey_commit"], b["bet_commit_minus_survey_commit_days"]))
        w("- **Row status: %s.**" % r["status"])
        w("")

    # ---- anchors ----
    w("## 3. Design-seat anchors")
    w("")
    for a in J["anchors"]:
        w("- `%s` (%s): resolves to `%s`, committer %s, author %s: '%s'" % (a["anchor"], a["design_seat_says"], a["resolves"], a["committer_utc"], a["author_utc"], clip(a["subject"], 200)))
    w("")
    ow = J["other_welfare_text"]
    w("## 4. Lines matching 'welfare|pre-commitment' at ref")
    w("")
    w("Search: `git grep -n -i -E 'welfare|pre-commitment'` over every tracked `*.md` at ref (this block and this audit's raws excluded): %d lines. "
      "Every line in the PROPOSAL, LOCK, ADDENDUM and FINDINGS documents is listed (no cap); for every other file the count is given, and all %d lines "
      "are in the JSON (`other_welfare_text.all_hits`). Rows W-h and W-g tabulate the two clauses block :91 names." % (ow["n_hits"], ow["n_hits"]))
    w("")
    for h in ow["operative_document_lines"]:
        w("- %s: %s" % (h["locator"], clip(h["text"], 170)))
    w("- Other files (lines matching): %s." % "; ".join("`%s` %d" % kv for kv in ow["other_files_counts"]))
    w("")
    w("## 5. The record's own date audit (RECORD HYGIENE entry, %s)" % J["record_date_audit_check"]["entry_locator"])
    w("")
    w("The entry says its source for every row is `git log --date=format:'%Y-%m-%d %H:%M'` with `TZ=UTC`. With `--date=format:` git prints each commit's own timezone; only `format-local:` honours TZ. Each row's printed 'true' time compared with git:")
    w("")
    w("| Locator | Row | Commit | Entry stamp | Printed 'true' time | git UTC | git local (-04:00) | Printed value equals | Stamp minus git UTC date (days) |")
    w("|---|---|---|---|---|---|---|---|---|")
    for h in J["record_date_audit_check"]["rows"]:
        w("| %s | %s | `%s` | %s | %s | %s | %s | %s | %s |" % (h["locator"], h["row_kind"], h["commit"], h["entry_stamp"], h["claimed_true_utc"], h["git_utc"], h["git_local_edt"], h["claimed_equals"], h["stamp_minus_utc_date_days"]))
    w("")
    w(J["date_audit_disclaimer"])
    w("")
    w("## 6. Claims of pre-registration checked against the record")
    w("")
    for c in J["claims_check"]:
        w("- %s" % json.dumps(c, ensure_ascii=False))
    w("")
    w("## 7. Code's reading")
    w("")
    w("Every statement below is computed above in this raw; the JSON carries every field.")
    w("")
    for k, (head, conts) in enumerate(J["code_reading_items"], 1):
        w("%d. %s" % (k, head))
        for c in conts:
            w("   %s" % c)
    w("")
    w("## 8. STOPs, referent notes, PI items")
    w("")
    w("STOPs:")
    for s_ in J["stops"]:
        w("- %s -- %s Suspected cause / what the record supports: %s" % (s_["subitem"], s_["discrepancy"], s_["suspected_cause"]))
    if not J["stops"]:
        w("- none")
    w("")
    w("Referent notes:")
    for x in J["notes"]:
        w("- %s" % x)
    w("")
    w("PI items:")
    for x in J["pi_items"]:
        w("- %s" % x)
    w("")
    # ---- inclusion ----
    inc = J["inclusion"]
    w("## 9. Row inclusion rule and census")
    w("")
    w("No committed rule says which entries are pre-registrations of record; the rule below is Code's, declared here (values-check pass 1, finding 15). A row is:")
    w("")
    for x in inc["rule"]:
        w("- %s" % x)
    w("")
    w("Census pattern (Python regex over each top-level entry's first three lines, in %s at ref): `%s`. Hits:" % (", ".join("`%s`" % f for f in inc["files"]), inc["pattern"]))
    w("")
    w("| Locator | Header origin | Matched | Class | Row / parent | Reason (non-rows) | Header |")
    w("|---|---|---|---|---|---|---|")
    for h in inc["hits"]:
        w("| %s | `%s` | %s | %s | %s | %s | %s |" % (h["locator"], h["header_origin"], ", ".join(h["matched"]), h["class"], h.get("row") or h.get("parent_row") or "-",
                                                  h.get("reason", "-"), clip(h["header"], 160).replace("|", "/")))
    w("")
    w("Tracked PROPOSAL/LOCK/ADDENDUM documents at ref and their rows: %s." % "; ".join("`%s` -> %s" % (d["document"], d["row"] or "NO ROW") for d in inc["tracked_documents"]))
    w("")
    w("Outside the census pattern and not rows (listed with locators):")
    for e in inc["extra_nonrows"]:
        fcl = e.get("first_commit_locators") or []
        s_ = "- %s: %s%s; first commit containing the text (searched over every path): %s%s" % (
            e["what"], e["locator"] or "NOT FOUND", ("; cited at %s" % e["cited_at"]) if e.get("cited_at") else "", e["first_commit"],
            (" (%s)" % ", ".join(fcl)) if fcl else "")
        if e.get("first_commit_on_current_path"):
            s_ += "; first on its current path at %s (a move)" % e["first_commit_on_current_path"]
        if e.get("cited_line_origin"):
            co = e["cited_line_origin"]
            s_ += "; the cited line's origin (`git blame -C -C`) is `%s` %s, %.4f d after the text's first commit" % (co["commit"], co["committer_utc"], co["days_after_first_text"])
        w(s_ + ".")
    w("- The cycle-2 'pre-registered rule (|t| < 1)' claim is checked in section 6, not tabulated.")
    w("")
    # ---- values check ----
    w("## 10. Values-check")
    w("")
    w(J["values_check_intro"])
    w("")
    for k, vc in enumerate(J["values_check"], 1):
        w("%d. **%s** -- %s. %s" % (k, vc["finding"], vc["action"], vc["detail"]))
    w("")
    w("### Pass 2")
    w("")
    w(J["values_check_pass2_intro"])
    w("")
    for k, vc in enumerate(J["values_check_pass2"], 1):
        w("%d. **%s** -- %s. %s" % (k, vc["finding"], vc["action"], vc["detail"]))
    w("")
    w("### Pass 3")
    w("")
    w(J["values_check_pass3_intro"])
    w("")
    for k, vc in enumerate(J["values_check_pass3"], 1):
        w("%d. **%s** -- %s. %s" % (k, vc["finding"], vc["action"], vc["detail"]))
    w("")
    w("### Pass 4")
    w("")
    w(J["values_check_pass4_intro"])
    w("")
    for k, vc in enumerate(J["values_check_pass4"], 1):
        w("%d. **%s** -- %s. %s" % (k, vc["finding"], vc["action"], vc["detail"]))
    w("")
    # redaction (routing rule 6): count on the rendered text, then fill the two placeholders
    md, n_md = redact("\n".join(o) + "\n")
    js0, n_js = redact(json.dumps(J, indent=1, sort_keys=False, default=str))
    cnt = "%d occurrence(s) in the md and %d in the JSON" % (n_md, n_js)
    J["header"]["redaction"] = {"rule": "routing rule 6: first 4 + '...' + length + ':' + sha256[:8]; ports 'len5:' + sha256[:8]",
                                "replaced_md": n_md, "replaced_json": n_js}
    md = md.replace("@@REDACTION@@", "- Redaction (routing rule 6; section 0): quoted record text redacted, %s." % cnt).replace("@@REDCOUNT@@", cnt)
    js, n_js2 = redact(json.dumps(J, indent=1, sort_keys=False, default=str).replace("@@REDCOUNT@@", cnt))
    json.loads(js)
    with open(out_md, "w") as f:
        f.write(md)
    with open(out_js, "w") as f:
        f.write(js + "\n")
    print("wrote %s and %s (redacted: md %d, json %d)" % (out_md, out_js, n_md, n_js2))


def build_reading(J):
    rows = J["rows"]
    ref7 = J["header"]["ref"][:7]
    stops, notes, pi, items = [], [], [], []
    n = len(rows)
    by = {}
    for r in rows:
        by.setdefault(r["status"], []).append(r["id"])
    for r in rows:
        if r["status"].startswith("STOP"):
            stops.append({"subitem": "%s: %s" % (r["id"], r["title"][:100]), "discrepancy": r["status"],
                          "suspected_cause": "see the row's cells"})
    ts = [h["locator"] for h in grep_ref("timestamped 2026-08-18", J["header"]["ref"])]
    J["q1_timestamp_claim_locators"] = ts
    q = next((r for r in rows if r["id"] == "Q1"), None)
    J["stops"] = stops

    # ---- item outcome (values-check pass 1, finding 5; revised in pass 2, findings 1, 4, 5, 6) ----
    def has_data(r):
        return any(c.get("first_data_commit") and not c.get("inputs_only") for c in r["cells"])
    wd = [r for r in rows if has_data(r)]
    sha_ok = [r["id"] for r in wd if r.get("recorded_sha256", {}).get("recorded_before_first_data") is True]
    sha_any = [r["id"] for r in rows if r.get("recorded_sha256", {}).get("found")]
    # values-check pass 4, finding 1: block :93's hash conjunct ('every row's recomputed sha matches the
    # recorded one') has no data qualifier, so a row without data and without a recorded sha256 is unmet too
    unmet_wd = [r["id"] for r in wd if r["id"] not in sha_ok]
    unmet_nd = [r["id"] for r in rows if not has_data(r)
                and not (r.get("recorded_sha256", {}).get("found") and r["recorded_sha256"].get("matches_recomputed"))]
    unmet = [r["id"] for r in rows if r["id"] in unmet_wd or r["id"] in unmet_nd]
    met = [r["id"] for r in rows if r["id"] not in unmet]
    J["hash_unmet_no_data"] = unmet_nd
    J["hash_conjunct"] = {"rows": len(rows), "unmet": unmet, "unmet_with_data": unmet_wd, "unmet_without_data": unmet_nd, "met": met,
                          "rows_with_data": len(wd)}

    def unmet_parts():
        a = ("the %d rows with data" % len(wd)) if len(unmet_wd) == len(wd) else ("%d of the %d rows with data" % (len(unmet_wd), len(wd)))
        return a + ((" and %s" % ", ".join(unmet_nd)) if unmet_nd else "")

    def unmet_paren():
        a = ("the %d with data" % len(wd)) if len(unmet_wd) == len(wd) else ("%d of the %d with data" % (len(unmet_wd), len(wd)))
        return a + ((" and %s" % ", ".join(unmet_nd)) if unmet_nd else "")
    gc = [(r["id"], c) for r in rows for c in r["cells"] if not c.get("inputs_only") and c.get("first_data_commit")]
    gc_bad = [(i, c["name"], c["order_by_commit"]) for i, c in gc if c["order_by_commit"] != "pre-registration first"]
    vc = [(i, c) for i, c in gc if c["verdict_cell"]]
    nov = [r for r in wd if not any(c["verdict_cell"] for c in r["cells"] if c.get("first_data_commit") and not c.get("inputs_only"))]
    scp = [(r["id"], sp["label"].split(" (")[0], sp["commit"]) for r in rows for sp in r["pre_data"].get("same_commit_prior", [])]
    J["order_counts"] = {"governed_cells_with_data": len(gc), "rows_with_data": len(set(i for i, _ in gc)), "order_exceptions": gc_bad,
                         "verdict_cells_with_data": len(vc), "rows_with_verdict_data": len(set(i for i, _ in vc)),
                         "rows_without_verdict_tier_data": [r["id"] for r in nov], "same_commit_prior": scp}

    # values-check pass 3, finding 3: counts with each tier judgment call read the other way (one at a time)
    def first_verdict(r, flip=None):
        cs = [c for c in r["cells"] if c.get("first_data_commit") and not c.get("inputs_only")
              and (c["verdict_cell"] != (flip is not None and c["tier"].get("call") == flip))]
        return min(cs, key=lambda c: c["first_data_committer_utc"])["first_data_short"] if cs else None
    alts = {}
    for k in CALLS:
        vc2 = [(i, c) for i, c in gc if c["verdict_cell"] != (c["tier"].get("call") == k)]
        ids2 = set(i for i, _ in vc2)
        alts[k] = {"code_counts": CALLS[k][0], "other_reading": CALLS[k][1],
                   "cells": ["%s / %s" % (i, c["name"]) for i, c in gc if c["tier"].get("call") == k],
                   "verdict_cells_with_data": len(vc2), "rows_with_verdict_data": len(ids2),
                   "rows_without_verdict_tier_data": [r["id"] for r in wd if r["id"] not in ids2],
                   "first_verdict_data_changes": [{"row": r["id"], "as_counted": first_verdict(r), "other_reading": first_verdict(r, k)}
                                                  for r in wd if first_verdict(r) != first_verdict(r, k)]}
    J["judgment_call_alternatives"] = alts

    def alt_text(k):
        a = alts[k]
        return "%s %s: %d verdict cells in %d rows; rows with data but no verdict-tier data: %s; first verdict data changes for %s" % (
            k, a["other_reading"], a["verdict_cells_with_data"], a["rows_with_verdict_data"], ", ".join(a["rows_without_verdict_tier_data"]) or "none",
            ", ".join("%s (%s -> %s)" % (x["row"], ("`%s`" % x["as_counted"]) if x["as_counted"] else "none", ("`%s`" % x["other_reading"]) if x["other_reading"] else "none")
                      for x in a["first_verdict_data_changes"]) or "no row")
    lc1t = next(r for r in rows if r["id"] == "L-c1")["cells"][0]["tier"]
    c1_locs = [lc1t["locator"]] + [x["locator"] for x in lc1t["also"]]
    J["c1_tier_locators"] = c1_locs

    # values-check pass 3, finding 2: whose commit hash is recorded anywhere in the record
    def hash_rec(r):
        rc = r.get("recorded_commit_hash") or {}
        return bool(rc.get("first_file_record") or rc.get("first_message_record"))

    def hash_rec_before(r):
        rc = r.get("recorded_commit_hash") or {}
        return rc.get("file_record_before_first_data") is True or rc.get("message_record_before_first_data") is True
    hrec = [r["id"] for r in wd if hash_rec(r)]
    hnone = [r["id"] for r in wd if not hash_rec(r)]
    hbef = [r["id"] for r in wd if hash_rec(r) and hash_rec_before(r)]
    haft = [r["id"] for r in wd if hash_rec(r) and not hash_rec_before(r)]
    J["commit_hash_record_split"] = {"rows_with_data": len(wd), "recorded_in_a_later_commit": hrec, "recorded_before_first_data": hbef,
                                     "recorded_not_before_first_data": haft, "recorded_nowhere": hnone,
                                     "reads": "the row's displayed version (version of record) only (values-check pass 4, finding 2)"}

    # values-check pass 4, finding 2: the split reads each row's displayed version; the later versions that
    # govern cells, and the version that governs a row's first data where it is not the displayed one
    def first_rec(rc):
        hs = [h for h in (rc.get("file_hit"), rc.get("message_hit")) if h]
        return min(hs, key=lambda h: meta(h["commit"])["committer_unix"]) if hs else None

    def rec_before(v):
        return v.get("commit_hash_file_record_before_governed_data") is True or v.get("commit_hash_message_record_before_governed_data") is True
    later = []
    for r in rows:
        if r["kind"] == "log":
            continue
        disp = r["record_commit"][:7]
        for v in r["versions"]:
            fdv = v.get("first_data_of_governed_cells")
            if v["commit"] == disp or not fdv:
                continue
            fr = first_rec(v["first_recording_of_commit_hash"])
            later.append({"row": r["id"], "version": v["label"].split(" (")[0], "commit": v["commit"],
                          "first_record": fr["commit"][:7] if fr else None, "first_record_committer_utc": fr["committer_utc"] if fr else None,
                          "first_governed_data": fdv["commit"], "first_governed_data_committer_utc": fdv["committer_utc"], "governs": v["governs_cells"],
                          "class": "recorded nowhere" if not fr else ("recorded before governed data" if rec_before(v) else "recorded only after governed data")})
    gov_first = []
    for r in wd:
        if r["kind"] == "log":
            continue
        dcs = [c for c in r["cells"] if c.get("first_data_commit") and not c.get("inputs_only")]
        fc = min(dcs, key=lambda c: meta(c["first_data_commit"])["committer_unix"])
        disp = r["record_commit"][:7]
        if fc["governing_commit"] == disp:
            continue
        dv = next(v for v in r["versions"] if v["commit"] == disp)
        gv = next(v for v in r["versions"] if v["commit"] == fc["governing_commit"])
        dfr, gfr = first_rec(dv["first_recording_of_commit_hash"]), first_rec(gv["first_recording_of_commit_hash"])
        gov_first.append({"row": r["id"], "displayed": disp, "displayed_version": dv["label"].split(" (")[0],
                          "displayed_governs_a_cell_with_data": bool(dv.get("first_data_of_governed_cells")),
                          "displayed_first_record": dfr["commit"][:7] if dfr else None,
                          "governing": gv["commit"], "governing_version": gv["label"].split(" (")[0], "governing_first_record": gfr["commit"][:7] if gfr else None,
                          "first_data": fc["first_data_short"], "governing_record_before_first_data": rec_before(gv),
                          "split_place": "before" if r["id"] in hbef else ("not before" if r["id"] in haft else "nowhere")})
    J["later_governing_versions"] = later
    J["first_data_governed_by_a_later_version"] = gov_first

    def isare(xs):
        return "is" if len(xs) == 1 else "are"

    def and_join(xs):
        return "none" if not xs else (xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1])
    lnow = ["%s %s (`%s`)" % (x["row"], x["version"], x["commit"]) for x in later if x["class"] == "recorded nowhere"]
    laft = ["%s %s (`%s`, first recorded at `%s`, after `%s`)" % (x["row"], x["version"], x["commit"], x["first_record"], x["first_governed_data"])
            for x in later if x["class"] == "recorded only after governed data"]
    lbef = ["%s `%s`" % (x["row"], x["commit"]) for x in later if x["class"] == "recorded before governed data"]
    later_txt = ("among later versions that govern cells (per-version table; JSON `later_governing_versions`), %s %s recorded nowhere, and %s %s recorded only after "
                 "the first data of the cells they govern; the other %d (%s) %s recorded before it" % (
                     and_join(lnow), isare(lnow), and_join(laft), isare(laft), len(lbef), ", ".join(lbef) or "none", isare(lbef)))
    gov_txt = " ".join(
        "%s's displayed version %s (`%s`%s) %s; the version that governs its first data `%s` is %s (`%s`), %s, so %s's place among the %s %s for that version." % (
            g["row"], g["displayed_version"], g["displayed"], (", first recorded at `%s`" % g["displayed_first_record"]) if g["displayed_first_record"] else ", recorded nowhere",
            "governs no cell with data" if not g["displayed_governs_a_cell_with_data"] else "does not govern the row's first data",
            g["first_data"], g["governing_version"], g["governing"],
            ("first recorded at `%s`, %s it" % (g["governing_first_record"], "before" if g["governing_record_before_first_data"] else "not before")) if g["governing_first_record"] else "recorded nowhere",
            g["row"], {"before": "%d 'before first data'" % len(hbef), "not before": "%d 'not before'" % len(haft), "nowhere": "%d recorded nowhere" % len(hnone)}[g["split_place"]],
            "holds" if (g["split_place"] == "before") == g["governing_record_before_first_data"] else "would change")
        for g in gov_first)
    supports = ("What the record supports for a row is 'committed at <commit> (<UTC>), before the first data commit <commit> (<UTC>)'; the ordering evidence "
                "for every row is the commit graph (ancestry). For %d of the %d rows with data the commit hash of the row's displayed version (column 'Hash recorded') "
                "is also recorded in a later commit: before the row's first data for %d (%s), not before it for %d (%s). For %d (%s) the commit hash is recorded in no "
                "tracked file or commit message: the record never names that version's commit, which is identified here from git alone (log and blame).%s %s." % (
                    len(hrec), len(wd), len(hbef), ", ".join(hbef) or "none", len(haft), ", ".join(haft) or "none", len(hnone), ", ".join(hnone) or "none",
                    (" " + gov_txt) if gov_txt else "", later_txt[0].upper() + later_txt[1:]))
    J["record_supports_wording"] = supports
    blk = lines_at(J["header"]["ref"], BLOCK)
    b90 = next((i + 1 for i, x in enumerate(blk) if "where the content hashes were recorded before data" in x), None)
    b3 = next((i + 1 for i, x in enumerate(blk) if "a wrong referent here is a note to fix, not a STOP" in x), None)
    J["block_referent_lines"] = {"content_hashes_recorded_before_data": b90, "wrong_referent_is_a_note": b3}
    outcome = []
    outcome.append("**N13 does not pass block :93 as written.** Block :93 passes a row only if 'every row's recomputed sha matches the recorded one and the "
                   "pre-registration commit precedes the first data commit'.")
    outcome.append("- Hash conjunct: unmet for %d of %d rows: %s (every row but %s). For %s, no content sha256 of a version is recorded anywhere in the record "
                   "before its data%s (absence, not mismatch: Code's reading of :93, for the PI to confirm, so no hash STOP is declared; the block's referent line :%s presumes the content "
                   "hashes were recorded before data in RESULTS.md and the archive logs, so their absence is a wrong referent, which its preamble, :%s, makes a note). "
                   "Rows whose sha256 is recorded before their first data: %s. "
                   "Rows with any recorded content sha256: %s, which governs no data." % (
                       len(unmet), len(rows), unmet_parts(), ", ".join(met) or "none",
                       ("the %d" % len(wd)) if len(unmet_wd) == len(wd) else ("those %d" % len(unmet_wd)),
                       ("; %s govern%s no data, but the conjunct has no data qualifier, and %s recorded nowhere" % (
                           ", ".join(unmet_nd), "s" if len(unmet_nd) == 1 else "", "its sha256 is" if len(unmet_nd) == 1 else "their sha256 values are")) if unmet_nd else "",
                       b90, b3, ", ".join(sha_ok) or "none", ", ".join(sha_any) or "none"))
    outcome.append("- Order conjunct: %s for every governed cell with data (%d cells in %d rows): each cell's first data commit is a proper descendant of the commit of "
                   "the version that governs it%s. The domain is the cells each pre-registration governs (block :91: 'the first data-generating commit for the cell it governs'). "
                   "Data on the same subject committed before a version of record, or in its own commit and reported by its entry as already generated, are not governed "
                   "by it and are listed per row (section 2); %d such sets sit in a pre-registration's own commit: %s. Reading the domain this way is Code's, for the PI to confirm." % (
                       "holds" if not gc_bad else "FAILS", len(gc), len(set(i for i, _ in gc)),
                       "" if not gc_bad else " except %s" % "; ".join("%s / %s (%s)" % x for x in gc_bad),
                       len(scp), "; ".join("%s (%s, `%s`)" % x for x in scp) or "none"))
    outcome.append("- Verdict cells (definition in section 0): %d with data, in %d rows; order holds for each. Rows with data but none in a verdict tier: %s (section 2 gives each reason)." % (
        len(vc), len(set(i for i, _ in vc)), "; ".join("%s (%s)" % (r["id"], (r.get("no_verdict_tier") or {}).get("text", "no verdict cell")) for r in nov) or "none"))
    outcome.append("- STOPs: %d. Block :93 names a STOP only for a row whose order is wrong or whose hash does not match; %s. Under the opposite readings, "
                   "%d rows (%s) would carry a hash STOP, and %s would each carry a same-commit order STOP, each on its cells' 'pre-registered' wording. "
                   "The Q1 bet's '2026-08-18' date is a referent note with a wording correction (section 8), not a STOP: the block makes a wrong referent a note "
                   "(its preamble, :%s: 'a wrong referent here is a note to fix, not a STOP'), and the Q1 cells' order holds." % (
                       len(stops), ("neither occurs under Code's two readings, both PI items (section 8): hash, a hash that was never recorded is absence, not mismatch "
                                    "(the block's referent line :%s gives a basis: the absence is a wrong referent); order, the test reads the cells each version governs" % b90)
                       if not stops else "see section 8",
                       len(unmet), unmet_paren(), " and ".join("%s (%s, `%s`)" % x for x in scp) or "no row", b3))
    outcome.append("- " + supports)
    J["outcome"] = outcome

    # ---- Code's reading, numbered at render time ----
    def add(head, *conts):
        items.append((head, [c for c in conts if c]))
    decl = [(r["id"], c) for r in rows for c in r["cells"] if c.get("inputs_only") and c.get("first_data_commit")]
    add("**Order.** %d rows. Rows by status: %s. No governed cell's first data commit precedes, or shares, its governing commit." % (
        n, "; ".join("%s: %s" % (k, ", ".join(v)) for k, v in sorted(by.items()))) if not gc_bad else "**Order.** see the STOP list.",
        ("Data in a pre-registration's own commit that its entry reports as already generated (not governed by it): %s." % "; ".join("%s / %s (`%s`)" % x for x in scp)) if scp else "",
        ("Declaration cells (no forwards; not data under the rule and not in the order test): %s." % "; ".join(
            "%s / %s: `%s`, %s after its governing commit `%s` (%.4f d); inputs A4 `%s` (PROPOSAL-g `72b09a9` precedes them: %s; governing commit precedes them: %s)" % (
                i, c["name"].split(" (")[0], c["first_data_short"], c["order_by_commit"], c["governing_commit"], c["gap_days"],
                c["inputs"]["first_commit"], c["inputs"]["PROPOSAL-g_72b09a9_precedes_inputs"], c["inputs"]["governing_commit_precedes_inputs"]) for i, c in decl)) if decl else "")
    add("**Verdict cells.** %d of the %d governed cells with data are verdict cells, in %d rows. Rows with data but no verdict-tier data: %s." % (
        len(vc), len(gc), len(set(i for i, _ in vc)), ", ".join(r["id"] for r in nov) or "none"),
        "Four tier assignments are judgment calls (section 8, PI items): (c) c1 r1/r2 counted as verdict (the entry calls the full run the primary experiment, %s, "
        "and its read a gate that c2 waits on, %s and %s-%s; the r2 entry says 'c2 remains unlicensed', %s; its words fire both clauses of the definition); "
        "the (d)/e1 G-gates counted as gates (PROPOSAL-d §2; the log reports their outcomes as findings); PROPOSAL-g A4 counted as verdict data (§4 B1 reads it; §3 heads Phase A 'no verdict data'); "
        "PROPOSAL-k Stage 1 counted as a gate stage (§1 'no behavioral verdict'; the log calls its outcome 'Stage 1's verdict'). Under any of these calls the order result is unchanged." % (
            c1_locs[0], c1_locs[1], c1_locs[2], (c1_locs[3] or "").rsplit(":", 1)[-1], c1_locs[4]),
        "Counts with one call read the other way (the other three as counted; JSON `judgment_call_alternatives`): %s." % "; ".join(alt_text(k) for k in CALLS))
    rec = [r for r in rows if r.get("recorded_sha256", {}).get("found")]
    add("**Hash.** A content sha256 of a pre-registration version is recorded before this audit for %d row(s): %s. For every other tracked document no 8-hex prefix of any version's sha256 is recorded in any tracked file or commit message before this audit's own preflight raw (excluded from the search). Block :93's pass condition ('recomputed sha matches the recorded one') therefore cannot be met as written for those rows. Code reads this as absence, not mismatch (for the PI to confirm), and block :93 names a STOP only for wrong order or a mismatch, so no hash STOP is declared; the block's referent line :%s presumes these hashes were recorded before data, so their absence is a wrong referent, a note under its preamble (:%s). The record's own convention is that the commit hash is the timestamp (section 0; each document's status line). %s" % (
        len(rec), ", ".join("%s (recorded at `%s`, %s; matches: %s)" % (r["id"], r["recorded_sha256"]["first"]["commit"][:7], r["recorded_sha256"]["first"]["committer_utc"], r["recorded_sha256"].get("matches_recomputed")) for r in rec) or "none",
        b90, b3, supports))
    pi.append("Hash conjunct: no content sha256 of any pre-registration except PROPOSAL-m v1.11 was recorded before data. Code reads block :93's 'whose hash does not match' as not covering a hash that was never recorded (absence, not mismatch), so it declares no hash STOP; the block's referent line :%s, which presumes the hashes were recorded before data, makes the absence a wrong referent, a note under its preamble (:%s). Confirm or overrule that reading (under the opposite one, %d rows (%s) carry a hash STOP). Decide whether the note's provenance sentence and README-NOTE table use 'committed at <commit> (<UTC>), before the first data commit <commit> (<UTC>)' (what the record supports), noting that the commit hash of the row's displayed version (column 'Hash recorded') is recorded in a later commit for %d rows (%s) and nowhere in the record for %d (%s); that %s%s. Decide also whether the N18 manifest should carry the sha256 values computed here." % (
        b90, b3, len(unmet), unmet_paren(), len(hrec), ", ".join(hrec), len(hnone), ", ".join(hnone), later_txt,
        ("; and that " + gov_txt.rstrip(".")) if gov_txt else ""))
    # values-check pass 4, finding 1: the count covers every row, A-g1 (no data, no recorded sha256) included
    nrec_all = [r["id"] for r in rows if not r.get("recorded_sha256", {}).get("found")]
    nrec_wd = [r["id"] for r in wd if not r.get("recorded_sha256", {}).get("found")]
    nrec_nd = [i for i in nrec_all if i not in nrec_wd]
    notes.append("Block :%s (N13's referents) says the content hashes were recorded before data in 'RESULTS.md and the archive logs'. The record holds no content sha256 "
                 "of any version recorded before its data: for %d of the %d rows (%s) none is recorded at all, and the one recorded value (P-m's) governs no data. "
                 "A wrong referent, which the block's preamble (:%s) makes a note to fix, not a STOP; it is why the hash conjunct cannot be met as written (item outcome; PI items)." % (
                     b90, len(nrec_all), len(rows),
                     ("the %d with data" % len(wd) if len(nrec_wd) == len(wd) else "%d of the %d with data" % (len(nrec_wd), len(wd))) + ((" and %s" % ", ".join(nrec_nd)) if nrec_nd else ""),
                     b3))
    pi.append("Order-test domain: Code reads block :93's order test over the cells each pre-registration governs (block :91), so data that an entry reports as already generated when it was written (c1 smoke at 6d88d9b; (d)/e1 teacher cache at 88e9ef0) are same-subject data, not governed cells; confirm or overrule (under the opposite reading, L-c1 and L-dgate each carry a same-commit order STOP).")
    pi.append("Verdict-cell definition (section 0) and its four judgment calls (section 7 item 2): (c) c1 r1/r2 as verdict, although the governing entry also calls the read a gate that c2 waits on (%s; %s-%s) and the r2 entry says 'c2 remains unlicensed' (%s), the same structure (a gate that licenses the next step) as the (d)/e1 G-gates, which are counted as gates; read as gate cells, the count is %d verdict cells in %d rows and L-c1 joins the rows without verdict-tier data (%s); (d)/e1 G-gates as gates; PROPOSAL-g A4 as verdict data; PROPOSAL-k Stage 1 as a gate stage. Section 7 item 2 gives the counts with each call read the other way. The labels decide only the 'first verdict data' column and the verdict counts, not order or STOPs." % (
        c1_locs[1], c1_locs[2], (c1_locs[3] or "").rsplit(":", 1)[-1], c1_locs[4], alts["c1"]["verdict_cells_with_data"], alts["c1"]["rows_with_verdict_data"],
        ", ".join(alts["c1"]["rows_without_verdict_tier_data"])))
    code_rec = []
    for r in rows:
        for v in (r.get("versions") or [{"commit": r["record_commit"][:7], "label": "log entry", "first_recording_of_commit_hash": r.get("first_recording_of_commit_hash")}]):
            fr = v.get("first_recording_of_commit_hash") or {}
            fh = fr.get("file_hit")
            if fh and not any(in_search_scope(p, "logs") for p in fh["paths"]):
                lh = (fr.get("first_in_logs_raws_data") or {}).get("file_hit")
                code_rec.append("%s %s `%s`: first in %s at `%s` (%s); first log/raw/data record %s" % (
                    r["id"], v["label"], v["commit"], ", ".join(fh["paths"]), fh["commit"][:7], fh["committer_utc"],
                    ("`%s` (%s)" % (lh["commit"][:7], lh["committer_utc"])) if lh else "none"))
    add("**Commit hashes recorded first in code.** %s." % ("; ".join(code_rec) if code_rec else "none"))
    changed = [r["id"] for r in rows if r["kind"] == "log" and r["entry"].get("entry_identical_at_ref") is False]
    add("**Log-only pre-registrations.** The cycle 1-4 criteria live in RESULTS entries; their content hash is computed here for the first time (computed-new). For each, the entry text at its introducing commit is compared with its text at ref; entries whose text changed after introduction are listed in their rows with the later commits.",
        ("Entries whose text at ref differs from the text as introduced: %s." % ", ".join(changed)) if changed else "Every log-entry pre-registration's text at ref is byte-identical to its text at its introducing commit.")
    if changed:
        notes.append("Log-entry pre-registrations edited after introduction: " + ", ".join(changed))
    add("**Data on the same subject before the version of record** (every row; section 2 gives the files, the log entries and what they are; counts are of distinct paths, model-free files apart): %s. Section 2 says what each is (the row's label or note); none is data the row governs." % (
        "; ".join(pre_count_str(r) for r in rows if r["pre_data"]["files"] or r["pre_data"]["log_entries_reporting_results_before"]) or "none"))
    am = [(r["id"], a["commit"], len(set(x["commit"] for x in a["data_commits_of_the_cells_before_it"]))) for r in rows for a in r.get("amendments_after_data", [])]
    vlate = []
    for r in rows:
        for v in r.get("versions", []):
            if v.get("change_from_previous") and v.get("data_commits_of_row_cells_before_this_version"):
                vlate.append("%s %s `%s` (%d data commit(s) of the row's cells before it)" % (r["id"], v["label"], v["commit"], len(v["data_commits_of_row_cells_before_this_version"])))
    scopes = sorted(set("%s %s: %s" % (r["id"], v["commit"], ", ".join(v["change_from_previous"]["scope"])) for r in rows for v in r.get("versions", []) if v.get("change_from_previous")))
    add("**Amendments inside an arc after some of its data.** %s. Each entry's header states what it left untouched (quoted in its row); Code reports the order and does not adjudicate whether a criterion moved." % ("; ".join("%s `%s` (%d earlier data commit(s))" % x for x in am) or "none"),
        ("Document versions committed after some of the document's data: %s. Each version's governed cells start after it (per-version table)." % "; ".join(vlate)) if vlate else "",
        ("Where each later version changed its document (git diff -U0 hunks; 'status block' = previous lines 1-10): %s." % "; ".join(scopes)) if scopes else "")
    b = q["bet"]
    a3 = next(c for c in q["cells"] if c["name"].startswith("A3"))
    a4c = next(c for c in q["cells"] if c["name"].startswith("A4"))
    b1 = next(c for c in q["cells"] if c.get("inputs_only"))
    q_note = ("Q1 bet, wording correction for the note (referent note, not a STOP; the phrase 'timestamped 2026-08-18' occurs at %s). What the record supports: "
              "'registered in PROPOSAL-g at `72b09a9` (%s), before every Q1 quantity (A3 `%s` %s; A4 `%s` %s; the B1 declaration `%s` %s)'. "
              "That commit follows the R_l survey commit `%s` (%s) by %.4f d, which PROPOSAL-g §0.1 itself discloses (its 'Descriptive peek, disclosed' paragraph). "
              "The 2026-08-18 date and 'prior to the survey' rest only on PROPOSAL-g's own text (%s), which cites HANDOFF-2026-08-18 §4; that handoff was never "
              "committed on any branch (git log --all over the path: %s) and is not on disk at root (%s). The record therefore cannot show that the bet pre-dates the "
              "survey, and cannot refute it either. Suggested wording: 'registered at 72b09a9 (2026-08-20 UTC), before any Q1 quantity; the bet's earlier date "
              "(2026-08-18) rests on an uncommitted handoff'." % (
                  "; ".join(ts), q["committer_utc"], a3["first_data_short"], a3["first_data_committer_utc"], a4c["first_data_short"], a4c["first_data_committer_utc"],
                  b1["first_data_short"], b1["first_data_committer_utc"], b["rl_survey_commit"]["commit"], b["rl_survey_commit"]["committer_utc"],
                  b["bet_commit_minus_survey_commit_days"], ", ".join(x.split(": ")[0] for x in b["lines_at_record_commit"]),
                  ", ".join(b["handoff_2026_08_18_commits_any_branch"]) or "no commits", ", ".join(b["handoff_2026_08_18_on_disk"]) or "absent"))
    notes.insert(0, q_note)
    J["q1_referent_note"] = q_note
    add("**Q1 bet.** A referent note with a wording correction, not a STOP (section 8): the 2026-08-18 date and 'prior to the survey' rest on an uncommitted handoff; the record supports registration at 72b09a9 (%s), %.4f d after the R_l survey commit and before every Q1 quantity; the Q1 cells' order holds." % (
        q["committer_utc"], b["bet_commit_minus_survey_commit_days"]))
    pi.append("Q1 bet wording: 'timestamped 2026-08-18' (%s) cannot be evidenced from the record; use 'registered at 72b09a9 (2026-08-20 UTC), before any Q1 quantity', or commit HANDOFF-2026-08-18 if it exists elsewhere, which would let the record carry the earlier date." % "; ".join(ts))
    for r in [r for r in rows if r.get("welfare")]:
        wf = r["welfare"]
        add("**Welfare %s.** Cited span %s (PROPOSAL-m v1.11:367); the clause runs lines %d-%d at ref and is identical at its commit (%s); cited span inside the clause: %s; cited span covers the whole clause: %s. The trigger's condition did not occur [log-only]: %s.%s" % (
            r["id"], wf["cited_span"], wf["clause_lines_at_ref"][0], wf["clause_lines_at_ref"][1], wf["clause_identical"], wf["cited_span_inside_clause"], wf["cited_span_covers_whole_clause"],
            wf["trigger_outcome_in_log"]["locator"] if wf.get("trigger_outcome_in_log") else "not found",
            (" The trigger names the confirm tier; confirm never ran [log-only]: %s." % wf["confirm_outcome_in_log"]["locator"]) if wf.get("confirm_outcome_in_log") else ""))
        if not wf["cited_span_covers_whole_clause"]:
            notes.append("Referent: %s cites %s; the whole clause is %s:%d-%d at %s." % (r["id"], wf["cited_span"], r["document"], wf["clause_lines_at_ref"][0], wf["clause_lines_at_ref"][1], ref7))
    nod = [r["id"] for r in rows if r["status"].startswith("NO GOVERNED")]
    g1m = [h for h in grep_ref("ADDENDUM-g1", J["header"]["ref"]) + grep_ref("g1_archival", J["header"]["ref"])
           if h["locator"].startswith("RESULTS.md") or h["locator"].startswith("archive/") or h["locator"].startswith("FINDINGS")]
    J["addendum_g1_mentions_in_logs"] = g1m
    add("**No governed data.** %s: no data file matches. ADDENDUM-g1's screen output (`data/olmo/g1_archival_{stage}.json`) does not exist at ref; the logs and FINDINGS mention ADDENDUM-g1 or g1_archival only at %s. PROPOSAL-m v1.11 has model-free artifacts only." % (
        ", ".join(nod), "; ".join("%s ('%s')" % (h["locator"], clip(h["text"], 90)) for h in g1m) or "no line"))
    if "A-g1" in nod:
        pi.append("ADDENDUM-g1 (committed 34eb7ee) pre-registers an archival-reading screen after B3; the record holds no output for it. If the note lists ADDENDUM-g1 among the pre-registrations, it should say the screen did not run.")
    u = J["untracked"]
    add("**Untracked texts.** %s are not in any commit; only ADDENDUM-g3 v1.2 and ADDENDUM-g1 are in the record. ADDENDUM-k1's sha16 is recorded at %s and matches the working-tree file." % (
        ", ".join(x["file"] for x in u), "; ".join(h["locator"] for h in next(x for x in u if x["file"] == "ADDENDUM-k1.md")["sha_prefix_hits_in_record"][:2])))
    pi.append("Untracked drafts (ADDENDUM-g3 v1.0, v1.1; ADDENDUM-k1 v1.1): whether to commit them is the PI's call; until then the README can cite only the tracked texts.")
    H = J["header"]
    cen = H["raw_stamp_census"]
    allh = [(r["id"], c["name"], h) for r in rows for c in r["cells"] for h in c.get("recorded_heads", [])]
    bad_heads = [(i, cn, h["hash"]) for i, cn, h in allh if h.get("governing_commit_is_ancestor") is False]
    distinct_rec = sorted(set((h["path"], h["line"], h["hash"]) for _, _, h in allh))
    distinct_lines = sorted(set((h["path"], h["line"]) for _, _, h in allh))
    J["provenance_record_counts"] = {"cell_level_listings": len(allh), "distinct_records_path_line_hash": len(distinct_rec),
                                     "distinct_raw_lines": len(distinct_lines),
                                     "distinct_path_hash": len(set((h["path"], h["hash"]) for _, _, h in allh)),
                                     "distinct_records": ["%s:%d %s" % x for x in distinct_rec]}
    add("**Dates.** No committed text makes a reflog time govern (section 0). Commits at ref whose author time differs from committer time: %d. In `results/raw/` (sorted by name, the audit's own raws excluded) the first raw carrying a time-only UTC stamp is %s (line %s, '%s') and the first carrying a full `date -u` or ISO UTC stamp is %s (line %s, '%s'); for cells whose raws carry no stamp the ordering evidence is the commit graph alone." % (
        H["history"]["author_time_ne_committer_time"],
        cen["first_raw_with_time_only_utc"]["path"] if cen["first_raw_with_time_only_utc"] else None, cen["first_raw_with_time_only_utc"]["line"] if cen["first_raw_with_time_only_utc"] else None, cen["first_raw_with_time_only_utc"]["verbatim"] if cen["first_raw_with_time_only_utc"] else None,
        cen["first_raw_with_date_u_or_iso_utc"]["path"] if cen["first_raw_with_date_u_or_iso_utc"] else None, cen["first_raw_with_date_u_or_iso_utc"]["line"] if cen["first_raw_with_date_u_or_iso_utc"] else None, cen["first_raw_with_date_u_or_iso_utc"]["verbatim"] if cen["first_raw_with_date_u_or_iso_utc"] else None),
        "In-raw provenance lines (recorded HEAD, lock or amendment commits): %d distinct records (path, line, hash) on %d raw lines, listed %d times across the cells (a raw shared by several cells is listed under each); %s. The distinct records: %s." % (
            len(distinct_rec), len(distinct_lines), len(allh),
            "every one resolves to a descendant of its cell's governing commit" if not bad_heads else "%d listings do not (listed next)" % len(bad_heads),
            "; ".join("%s:%d `%s`" % (p.split("/")[-1], ln, hh) for p, ln, hh in distinct_rec)),
        ("Recorded commits inside raws that are NOT descendants of the governing commit: %s." % "; ".join("%s/%s/%s" % x for x in bad_heads)) if bad_heads else "")
    if bad_heads:
        notes.append("In-raw recorded commits that are not descendants of the governing commit: " + "; ".join("%s/%s/%s" % x for x in bad_heads))
    hy = J["record_date_audit_check"]["rows"]
    edt = [h for h in hy if h["claimed_equals"].startswith("EDT")]
    wrong = [h for h in hy if h["row_kind"].startswith("audit row") and h["stamp_minus_utc_date_days"] == 0 and h["commit"] not in ("70995c0", "4ca10e1")]
    dcl = J["date_rule"].get("dating_convention_line") or {}
    mclause = re.search(r"a one-day difference[^;]*", dcl.get("text", ""))
    near = "; ".join("`%s` committed %s -04:00 = %s UTC" % (h["commit"], h["git_local_edt"], h["git_utc"]) for h in wrong)
    J["date_audit_disclaimer"] = ("Section 5 is descriptive and proposes no correction. The record's dating convention (%s) says '%s'; Code's stamps are Code's. %s" % (
        dcl.get("locator"), mclause.group(0) if mclause else "(clause not found)",
        ("The one row where the entry's '+1 day' does not hold in UTC is a near-midnight case: %s." % near) if wrong else ""))
    add("**The record's own date audit** (%s): %d of its %d printed 'true UTC' times equal git's -04:00 local time, not UTC (section 5). Under git's UTC, %s. Descriptive only: %s" % (
        J["record_date_audit_check"]["entry_locator"], len(edt), len(hy),
        ("the '+1 day' verdict does not hold for %s (stamp equals its UTC date)" % ", ".join("`%s`" % h["commit"] for h in wrong)) if wrong else "every '+1 day' verdict holds",
        "the dating convention expects a one-day difference near midnight Eastern and corrects neither side (section 5)."))
    notes.append("RESULTS.md RECORD HYGIENE entry (%s): %d of %d printed 'true UTC' times are -04:00 local; %s. Descriptive only; the dating convention (%s) expects near-midnight one-day differences and corrects neither, so no correction is proposed." % (
        J["record_date_audit_check"]["entry_locator"], len(edt), len(hy), ("'+1 day' fails in UTC for " + ", ".join(h["commit"] for h in wrong) + " (" + near + ")") if wrong else "verdicts hold", dcl.get("locator")))
    for c in J["claims_check"]:
        add("**Claim check.** %s (%s): registration found before the result: %s%s." % (c["claim"], c["locator"], c["registration_found_before_result"],
            (" (string first enters at `%s`, %s; the result commit is `%s`)" % (c["first_commit_containing_string"], c["first_commit_utc"], c["result_commit"])) if c.get("first_commit_containing_string") else ""))
        if c["registration_found_before_result"] is False:
            notes.append("Cycle-2 'pre-registered rule (|t| < 1)' (%s): the string first enters the record in the result commit %s; no earlier registration found." % (c["locator"], c["result_commit"]))
    add("**Anchors.** " + "; ".join("`%s` = %s (%s)" % (a["anchor"], clip(a["subject"], 90), a["committer_utc"]) for a in J["anchors"]) + ". All three resolve; cef728f is the e2d closure's text of record, not a pre-registration.")
    inc = J["inclusion"]
    uncl = [h["locator"] for h in inc["hits"] if h["class"] == "UNCLASSIFIED"]
    norow = [d["document"] for d in inc["tracked_documents"] if not d["row"]]
    add("**Rows.** The inclusion rule is Code's (section 9). Census: %d entry headers match the pattern; %d are rows, %d are N declarations, %d mention a pre-registration without registering one, %d unclassified%s. Tracked PROPOSAL/LOCK/ADDENDUM documents without a row: %s. %d further items found outside the pattern are listed, not tabulated." % (
        len(inc["hits"]), sum(1 for h in inc["hits"] if h["class"] == "row"), sum(1 for h in inc["hits"] if h["class"] == "N declaration"),
        sum(1 for h in inc["hits"] if h["class"] == "mention only"), len(uncl), (" (%s)" % ", ".join(uncl)) if uncl else "",
        ", ".join(norow) or "none", len(inc["extra_nonrows"])))
    J["code_reading_items"] = items
    J["code_reading"] = ["%d. %s" % (k, h) for k, (h, _) in enumerate(items, 1)]
    J["notes"] = notes
    J["pi_items"] = pi
    build_values_check(J)
    build_values_check_pass2(J)


def build_values_check(J):
    """Section 10: each values-check finding (pass 1) and its disposition, with the
    values this run computes for it."""
    rows = {r["id"]: r for r in J["rows"]}
    vc = []

    def add(finding, action, detail):
        vc.append({"finding": finding, "action": action, "detail": detail})

    ag3 = rows["A-g3"]["recorded_commit_hash"]
    fh = ag3.get("first_file_record") or {}
    lh = ag3.get("first_record_in_logs_raws_data") or {}
    moved = []
    for r in J["rows"]:
        vers = r.get("versions") or [{"label": "log entry", "commit": r["record_commit"][:7],
                                       "first_recording_of_commit_hash": r.get("first_recording_of_commit_hash"), "first_recording_of_sha256": None}]
        for v in vers:
            for kind, key in (("commit hash", "first_recording_of_commit_hash"), ("sha256", "first_recording_of_sha256")):
                fr = v.get(key)
                if fr and fr.get("scope_changes_first_record"):
                    a = (fr.get("file_hit") or {}).get("commit")
                    b = ((fr.get("logs_scope") or {}).get("file_hit") or {}).get("commit")
                    moved.append("%s %s `%s` %s: %s (all tracked paths) vs %s (logs, raws, data)" % (
                        r["id"], v["label"], v["commit"], kind, ("`%s`" % a[:7]) if a else "none", ("`%s`" % b[:7]) if b else "none"))
    brule = []
    for r in J["rows"]:
        vers = r.get("versions") or [{"label": "log entry", "commit": r["record_commit"][:7],
                                       "first_recording_of_commit_hash": r.get("first_recording_of_commit_hash"), "first_recording_of_sha256": None}]
        for v in vers:
            for kind, key in (("commit hash", "first_recording_of_commit_hash"), ("sha256", "first_recording_of_sha256")):
                fr = (v.get(key) or {}).get("logs_scope")
                if fr and fr.get("bounded_rule_changes_first_record"):
                    brule.append("%s %s `%s` %s: file %s / message %s (bounded) vs file %s / message %s (substring)" % (
                        r["id"], v["label"], v["commit"], kind, ((fr.get("file_hit") or {}).get("commit") or "none")[:7],
                        ((fr.get("message_hit") or {}).get("commit") or "none")[:7], (fr.get("substring_rule_file_commit") or "none")[:7],
                        (fr.get("substring_rule_message_commit") or "none")[:7]))
    add("Row 22 (A-g3): commit hash f14d249 first recorded at b6e8f3f, 'not before data'", "fixed",
        "Correct: the search covered only *.md, results/raw/ and data/. It now covers every tracked path (audit files excluded), with bounded hex-run matching. "
        "A-g3's commit hash is first recorded at `%s` (%s) in %s, before the B2-r data; its first log/raw/data record is `%s` (%s), the data commit itself; "
        "row 22, section 2 and the JSON (`commit_hash_file_record_before_governed_data` = %s) now say so. Every (row, version, token) whose first record differs between "
        "the widened and the builder's scope: %s." % (
            (fh.get("commit") or "")[:7], fh.get("committer_utc"), ", ".join(fh.get("paths") or []), (lh.get("commit") or "")[:7], lh.get("committer_utc"),
            rows["A-g3"]["versions"][0].get("commit_hash_file_record_before_governed_data"), "; ".join(moved) or "none")
        + " Within the builder's scope, every first record under the bounded rule compared with the builder's plain-substring rule (file and message): %s." % ("; ".join(brule) or "no difference"))
    gapcells = []
    for r in J["rows"]:
        for c in r["cells"]:
            if c.get("first_data_commit") and not c.get("inputs_only") and c["governing_commit"] != r["record_commit"][:7]:
                gapcells.append("%s / %s: %.4f d from `%s`" % (r["id"], c["name"], c["gap_days"], c["governing_commit"]))
    add("Table header 'Gaps are in days from the pre-registration commit' (rows 17, 19, 23 measured from a later version)", "fixed",
        "Correct. The header now says gaps and order are measured from the commit of the version that governs the cell, and each affected table cell names it as '(from `x`)'. Cells governed by a version other than the row's displayed commit: %s." % "; ".join(gapcells))
    lg = rows["LOCK-g"]
    lgv = [c for c in lg["cells"] if c["verdict_cell"] and not c.get("inputs_only") and c.get("first_data_commit")]
    add("Row 20 (LOCK-g): B1 shown as 'first verdict data' (gap 0.0011); 'commit hash at 783fdfb (before data)'; run stamp 'none'", "fixed",
        "Correct. A declaration cell with no forwards (inputs_only) is now out of 'first data', 'first verdict data' and the order test, and is shown in the first-data cell as a declaration with its A4 inputs. Row 20's first verdict data is now `%s` (%s), its run stamp '%s', and its hash cell names 783fdfb as the B1 declaration's commit. Section 7 item 1 lists the declaration cells." % (
            lgv[0]["first_data_short"] if lgv else None, lgv[0]["name"] if lgv else None, stamp_str(lgv[0]) if lgv else None))
    q = rows["Q1"]
    add("Q1: STOP not shown in the table row; STOP's condition unnamed; ':82' (window clause) among 'Bet lines'", "fixed",
        "Correct at pass 1, and the STOP was then shown in row 15's status. Superseded in pass 2 (finding 1): the Q1 item is now a referent note with a wording correction, not a STOP, and row 15's status is '%s'. "
        "72b09a9 follows the R_l survey commit %s by %.4f d. The window-clause line is dropped from the bet lines (now %s)." % (
            q["status"], q["bet"]["rl_survey_commit"]["commit"], q["bet"]["bet_commit_minus_survey_commit_days"], ", ".join(x.split(": ")[0] for x in q["bet"]["lines_at_record_commit"])))
    add("No item-level verdict against block :93", "fixed",
        "Correct. A new 'Item outcome' section after the header states that N13 does not pass :93 as written, with the hash conjunct's count, the order conjunct, the STOP count and the readings that are Code's. "
        "Pass 2 (findings 1, 4, 5 and 6) revised its order, verdict and STOP lines, pass 3 (findings 2 and 5) its hash, STOP and record-supports lines, and pass 4 "
        "(findings 1 and 2) its hash, STOP and record-supports lines again; the section shows the revised text.")
    pre = [pre_count_str(r, "log entries", always_log=True) for r in J["rows"] if r["pre_data"]["files"] or r["pre_data"]["log_entries_reporting_results_before"]]
    e0b2_f = meta("f222541")
    e0b2_r = meta("05bda27")
    add("Log rows omit 'Data on the same subject committed before the version of record'", "fixed",
        "Correct in substance. Every row now carries the line, computed from declared paths (and, for L-e0B2 and L-e0B2c, the earlier log entries reporting results). Rows with such data (distinct paths, model-free files apart; pass 3, findings 1 and 6): %s. One part of the evidence does not hold: L-e0B2 does not follow f222541. `f222541` (%s) %s a proper descendant of L-e0B2's commit `05bda27` (%s; git merge-base --is-ancestor). The e0 B1 raw enters the record at f222541, after the pre-registration; what precedes the pre-registration is the B1 log report ba15304 (with 15ab36b and 4118d6b), which the row now lists." % (
            "; ".join(pre), e0b2_f["committer_utc"], "is" if (is_ancestor(e0b2_r["commit"], e0b2_f["commit"]) and e0b2_r["commit"] != e0b2_f["commit"]) else "is NOT", e0b2_r["committer_utc"]))
    hu = next(c for c in rows["P-h"]["cells"] if c["name"].startswith("H1 run 1"))
    hg = next(c for c in rows["P-h"]["cells"] if c["name"].startswith("H1 leakage"))
    add("H1-u data commits [b2d051b, 7527270]; 7527270 labelled H1-u", "fixed",
        "Correct: data/e2b/h1_sessions.json was renamed to h1u_sessions.json at d94e281 and re-added by the gate run at 7527270. The path is now bounded by commit in both cells: H1-u data commits %s; H1 gate data commits %s (paths include data/e2b/h1_sessions.json after d94e281)." % (hu["data_commits"], hg["data_commits"]))
    hk = []
    for rid in ("P-h", "LOCK-h", "P-j"):
        for v in rows[rid]["versions"]:
            cf = v.get("change_from_previous")
            if cf:
                hk.append("%s `%s`: %s (previous %d lines, this %d)" % (rid, v["commit"], ", ".join(h["git_range"] for h in cf["hunks"]), cf["lines_previous"], cf["lines_this"]))
    add("End-of-file hunk ranges run past the end of the file", "fixed",
        "Correct. Hunks are now git's own (`git diff -U0`), each with its git range; an insertion is placed 'after previous line N'. Ranges: %s." % "; ".join(hk))
    add("Lists truncated without a marker; names cut mid-word; section 7 numbered 6 and 11 twice", "fixed",
        "Correct. Data commits are listed in full with their count; first paths show at most four with '(+N more; full list in JSON ...)'; cell names are no longer cut; quoted text is cut at a word boundary and marked ' [...]'; recorded-HEAD lines are listed in full; section 7 is numbered at render time.")
    pc = J["provenance_record_counts"]
    add("Section 7 item 9: '34 listed across the cells'", "fixed",
        "Correct that 34 was the count of cell-level listings, not of records. The listings are now uncapped and deduplicated within a cell by (path, line, hash) instead of (path, hash); "
        "this run: %d distinct records (path, line, hash) on %d raw lines, %d cell-level listings, %d distinct (path, hash) pairs (%s). The sentence states the first three." % (
            pc["distinct_records_path_line_hash"], pc["distinct_raw_lines"], pc["cell_level_listings"], pc["distinct_path_hash"],
            "the old key hid %d record(s) that share a raw and a hash with another line" % (pc["distinct_records_path_line_hash"] - pc["distinct_path_hash"])
            if pc["distinct_records_path_line_hash"] > pc["distinct_path_hash"] else "the old key hid no record"))
    add("PROPOSAL-m v1.11:6 quoted only in part; section 5 not marked descriptive", "fixed",
        "Correct. Section 0 quotes the whole line; section 5, section 7 and the section 8 note say the date audit is descriptive and proposes no correction, citing the line's near-midnight clause, and name cd86e49's local and UTC times.")
    pj = next(v for v in rows["P-j"]["versions"] if v["commit"] == "520f62c")
    add("P-j v1.3: D2 globs miss 10f6f3a (tstep_check_f010)", "fixed",
        "Correct (the f010 raw records a model load and a 24-round T-step check at frac 0.10). The D2 paths now take `data/e2d/tstep_check*.json` and `results/raw/2026-09-02_e2d_tstep*.txt`; data commits of P-j's cells before v1.3: %d (%s). Order does not change." % (
            len(pj["data_commits_of_row_cells_before_this_version"]), ", ".join(x["commit"][:7] for x in pj["data_commits_of_row_cells_before_this_version"])))
    wg = rows["W-g"]["welfare"].get("confirm_outcome_in_log") or {}
    add("W-g cell label 'B3 screen (the confirm tier the trigger names)'", "fixed",
        "Correct: LOCK-g:167 triggers on a confirm pass; B3 is the screen. Relabelled 'B3 screen (the tier before the confirm that the trigger names; confirm never ran)', citing %s [log-only]." % wg.get("locator"))
    pk = next(c for c in rows["P-k"]["cells"])
    add("Row 24's 'Run stamp in raw' is the exit stamp", "fixed",
        "Correct. Stamps are now labelled by their line, and a log-only launch time is appended: row 24 reads '%s'." % stamp_str(pk))
    add("No stated rule for which entries are pre-registrations of record; exclusions not listed", "fixed",
        "Correct. Section 9 declares Code's inclusion rule, runs a census of entry headers against a stated pattern, classifies every hit (row, N declaration, mention only), maps every tracked PROPOSAL/LOCK/ADDENDUM document to its row, and lists the checker's out-of-pattern items with locators (the cycle-1 pivot's tail-PCA failure mode; the S1 per-cell n declaration).")
    r3 = rows["L-c1r3"].get("port") or {}
    add("L-c1 note and section 6 claim 2: c1 criteria in the record 'only as the log prose' (finding text truncated in what Code received)", "fixed",
        "The finding's evidence and fix were cut off in transmission; Code checked the claim itself. It was imprecise for r3: the r3 matched-pair swing criterion's code entered the record as %s at `%s` (%s), whose docstring says it is ported off scripts/c1_gate.py, with the r3 gate JSONs and a regression check (%s), %s d after the r3 data. The P1-P3/S1 read (L-c1) has no code in the record. Both notes and section 6 now say this." % (
            r3.get("path"), r3.get("added_commit"), r3.get("added_utc"), ", ".join(r3.get("regression_locator") or []), r3.get("days_after_first_verdict_data")))
    add("Findings after finding 16", "disclosed",
        "The findings list Code received ends partway through finding 16 (its evidence and fix fields are missing). Any later findings were not received and have no disposition here.")
    J["values_check_intro"] = ("Values-check pass 1: an adversarial checker re-ran the builder's script into scratch (byte-identical apart from the stamp and command lines) and checked 300 claims. "
                               "Each finding below is listed with Code's disposition after checking it against the record; values quoted are this run's.")
    J["values_check"] = vc


def build_values_check_pass2(J):
    """Section 10, pass 2: each finding of the second values-check and its disposition, with
    the values this run computes for it."""
    rows = {r["id"]: r for r in J["rows"]}
    ref = J["header"]["ref"]
    vc = []

    def add(finding, action, detail):
        vc.append({"finding": finding, "action": action, "detail": detail})

    # 1. Q1 STOP
    blk = lines_at(ref, BLOCK)
    stop_lines = [i + 1 for i, x in enumerate(blk) if "STOP" in x]
    q = rows["Q1"]
    b = q["bet"]
    add("Q1: the STOP on 'timestamped 2026-08-18' and 'pre-survey' is not licensed by block :93 (substantive)", "fixed",
        "Correct. Block :93 names a STOP only for a row whose order is wrong or whose hash does not match, and the block's preamble makes a wrong referent a note. "
        "The block's lines containing 'STOP' at ref are %s; on Code's reading of each, none licenses a STOP on a date or a referent, and the Q1 cells' order holds. The item is now a referent note "
        "with a wording correction (section 8, first note); STOPs: %d; row 15's status is '%s'. The old text 'in the record the bet is not pre-survey' is replaced by: the record "
        "cannot show that the bet pre-dates the survey, because its first committed text (`72b09a9`, %s) follows the R_l survey commit `%s` (%s) by %.4f d and the cited "
        "HANDOFF-2026-08-18 was never committed (commits on any branch: %s). Block :93 is now applied under one reading throughout: order over the governed cells (findings 4 and 5)." % (
            ", ".join(":%d" % x for x in stop_lines), len(J["stops"]), q["status"], q["committer_utc"], b["rl_survey_commit"]["commit"], b["rl_survey_commit"]["committer_utc"],
            b["bet_commit_minus_survey_commit_days"], ", ".join(b["handoff_2026_08_18_commits_any_branch"]) or "none"))

    # 2. tail-PCA
    tp = next(e for e in J["inclusion"]["extra_nonrows"] if "tail-PCA" in e["what"])
    co = tp.get("cited_line_origin") or {}
    add("Section 9: the tail-PCA failure-mode text 'first commit c54c4e0' (substantive)", "fixed",
        "Correct. The search now runs `git log -S` over every path: the text first enters at %s (%s); %s. The cited result line's origin (`git blame -C -C`) is `%s` %s, %s d after "
        "the text's first commit, so the failure mode preceded that result. The listing in section 9 now gives these values." % (
            tp["first_commit"], ", ".join(tp.get("first_commit_locators") or []),
            ("it reached its current path at %s, the move" % tp["first_commit_on_current_path"]) if tp.get("first_commit_on_current_path") else "its current path has the same first commit",
            co.get("commit"), co.get("committer_utc"), co.get("days_after_first_text")))

    # 3. modifications
    mi = J["modify_only_index"]
    md_ = sorted(set(m["commit"] for m in mi if m["class"].startswith("data")))
    mf_ = sorted(set(m["commit"] for m in mi if m["class"] == "model-free"))
    mu_ = sorted(set(m["commit"] for m in mi if m["class"] == "UNCLASSIFIED"))
    le = rows["L-e2a"]
    am814 = next(a for a in le["amendments_after_data"] if a["commit"] == "814a254")
    n814 = sorted(set(x["commit"] for x in am814["data_commits_of_the_cells_before_it"]), key=lambda c: meta(c)["committer_unix"])
    full = {rid: next(c for c in rows[rid]["cells"] if c["name"].startswith("e2a full run")) for rid in ("P-e", "L-e2a", "L-e2a-g3p")}
    r26 = [f for f in rows["L-r26"]["pre_data"]["files"] if f["change"] != "added"]
    add("The addition-only data index misses aed3b08's run-2 e2a data (substantive)", "fixed",
        "Correct. The index now also reads modify-only commits (git log -M --diff-filter=M over data/ and results/raw/); each one matched by a declared path was read with `git show` "
        "and classified (section 0 table): data %s; model-free %s; unclassified %s. `aed3b08` is counted in the e2a full-run cell of P-e, L-e2a and L-e2a-g3p; its data commits are now "
        "%s (P-e), %s (L-e2a), %s (L-e2a-g3p). The 814a254 adjudication now has %d earlier data commits: %s. One more modify-only data commit enters a row's same-subject data: %s. "
        "The smoke cells no longer include the full-run files (finding 4's split), so aed3b08 is not listed under them." % (
            ", ".join("`%s`" % x for x in md_) or "none", ", ".join("`%s`" % x for x in mf_) or "none", ", ".join(mu_) or "none",
            ", ".join(full["P-e"]["data_commits"]), ", ".join(full["L-e2a"]["data_commits"]), ", ".join(full["L-e2a-g3p"]["data_commits"]),
            len(n814), ", ".join(n814), "; ".join("L-r26: `%s` at `%s` (%s%s)" % (
                f["path"], f["commit"], f["change"], "; the path itself was added earlier in the list, so pass 3 counts it once, as an extension" if f.get("path_added_earlier_in_list") else "")
                for f in r26) or "none"))

    # 4. verdict cells
    oc = J["order_counts"]
    pj = rows["P-j"]
    ph_v = next(c for c in rows["P-h"]["cells"] if c["name"] == "e2b verdict campaign, run of record")
    tiers_h1 = [(rid, c["tier"]["label"]) for rid in ("P-h", "LOCK-h") for c in rows[rid]["cells"] if c["name"].startswith("H1 leakage")]
    add("'Verdict cell' undefined and inconsistently applied (substantive)", "fixed",
        "Correct. Section 0 now defines a verdict cell, and every cell carries its tier with the line it rests on (section 2; JSON `cells[].tier`). Applied throughout: P-j's D1-D3 are "
        "calibration tier, so row 23's first verdict data reads 'none: %s'; the H1 leakage gate is calibration tier under both rows (%s); A3 is calibration and A4 verdict data under both P-g and Q1; "
        "the same definition also splits the e2b verdict-campaign smoke from the run of record (P-h, W-h and LOCK-h's first verdict data is now `%s`), splits B2-r into control, smoke, "
        "qualification and exploration, splits P-e's and P-f's cells to mirror their log rows, counts the (d)/e1 G-gates as gates (P-d, L-dgate) and PROPOSAL-k Stage 1 as a gate stage. "
        "Recount: %d verdict cells with data in %d rows (within the checker's bound of at most 27 in 22); rows with data but no verdict-tier data: %s. The order conjunct now reads every governed "
        "cell and holds for all %d in %d rows; four tier calls are listed as judgment calls for the PI." % (
            (pj.get("no_verdict_tier") or {}).get("text"), "; ".join("%s: %s" % x for x in tiers_h1), ph_v.get("first_data_short"),
            oc["verdict_cells_with_data"], oc["rows_with_verdict_data"], ", ".join(oc["rows_without_verdict_tier_data"]),
            oc["governed_cells_with_data"], oc["rows_with_data"]))

    # 5. same-commit cells
    scp = oc["same_commit_prior"]
    lc1 = rows["L-c1"]
    ldg = rows["L-dgate"]
    add("Same-commit non-verdict cells: the entries report the data as already generated (minor)", "fixed",
        "Correct. Both are now listed as 'Data on the same subject committed with the version of record, in its own commit, and reported by the entry as already generated', "
        "with the entry's lines (%s), and are no longer governed cells. L-c1's first data is now `%s`; L-dgate's is `%s`." % (
            "; ".join("%s: %s" % (r_["id"], ", ".join(x["locator"] or "NOT FOUND" for x in sp["reported_in_entry"])) for r_ in (lc1, ldg) for sp in r_["pre_data"]["same_commit_prior"]),
            (lc1.get("first_data_overall") or {}).get("commit"), (ldg.get("first_data_overall") or {}).get("commit")))

    # 6. hash wording
    add("Hash conjunct: 'absence, not mismatch' presented as :93's text (minor)", "fixed",
        "Correct. The item outcome and section 0 now say that 'absence, not mismatch' is Code's reading of :93, for the PI to confirm, so that no hash STOP is declared, and the hash PI item asks the PI to confirm or overrule that reading.")

    # 7. welfare search
    ow = J["other_welfare_text"]
    want = ["PROPOSAL-k-echo-channel.md@%s:567" % ref[:7], "FINDINGS-5.md@%s:146" % ref[:7], "FINDINGS-5.md@%s:158" % ref[:7],
            "LOCK-h.md@%s:92" % ref[:7], "PROPOSAL-m-gating-campaign-v1_11.md@%s:48" % ref[:7]]
    have = set(h["locator"] for h in ow["operative_document_lines"])
    missing = [x for x in want if x not in have]
    add("Section 4 'Other welfare text in the record (found by search at ref)' overclaims (minor)", "fixed",
        "Correct: the old search covered four documents, matched only 'pre-commitment' and stopped at 6 per document without a marker. Section 4 now runs `git grep -i -E 'welfare|pre-commitment'` "
        "over every tracked *.md at ref: %d lines; the %d lines in PROPOSAL/LOCK/ADDENDUM/FINDINGS documents are listed without a cap and the rest are counted per file (all in the JSON). "
        "The checker's named lines: %s.%s" % (
            ow["n_hits"], len(ow["operative_document_lines"]), "; ".join("%s %s" % (x, "listed" if x in have else "NOT LISTED") for x in want),
            (" Not listed: %s (no match of the pattern on that line)." % ", ".join(missing)) if missing else " All five are listed."))

    # 8. LOCK-h prepend
    lv = next(v for v in rows["LOCK-h"]["versions"] if v["commit"] == "f030cdd")
    cf = lv["change_from_previous"]
    add("LOCK-h v2.0 labelled 'status block (previous lines 1-10)' (minor)", "fixed",
        "Correct (`git diff -U0 d94e281 f030cdd -- LOCK-h.md`: one hunk `%s`). An insertion before previous line 1 is now labelled '%s', and the change kind is '%s'; the per-version table and section 7 carry the new label." % (
            cf["hunks"][0]["git_range"], ", ".join(cf["scope"]), cf["kind"]))

    # 9. sha256 status
    st = sorted(set((r["id"], r.get("content_sha256_status")) for r in J["rows"]))
    rep_ = [x for x in st if (x[1] or "").startswith("reproduced")]
    cn = [x for x in st if (x[1] or "").startswith("computed-new")]
    add("Document sha256 labelled 'recomputed from git show' outside the status vocabulary (minor)", "fixed",
        "Correct. Every document version now carries a status, and every row its version of record's: %d row(s) computed-new, %d reproduced (%s). The table header states it, and each version line in section 2 shows it." % (
            len(cn), len(rep_), "; ".join("%s: %s" % x for x in rep_) or "none"))

    # redaction (routing rule 6; not a checker finding)
    lh = ((rows["A-g3"].get("recorded_commit_hash") or {}).get("first_record_in_logs_raws_data") or {}).get("lines") or [{}]
    add("Routing: the md and JSON quoted RunPod pod-id text (rule 6)", "fixed",
        "Correct: A-g3's commit-hash record quotes %s (%s at ref), a line that names the pod. Quoted text is now redacted when the raw is written "
        "(section 0, 'Redaction'); this run replaced @@REDCOUNT@@." % (lh[0].get("locator_at_commit"), ", ".join(lh[0].get("locators_at_ref") or [])))
    J["values_check_pass2"] = vc
    J["values_check_pass2_intro"] = ("Values-check pass 2: the checker re-ran the script into scratch (byte-identical apart from the stamp and command lines) and confirmed its central result; "
                                     "it reported four substantive and five minor findings, and the routing added the redaction. Each is listed with Code's disposition after checking it against the record; values quoted are this run's.")


def build_values_check_pass3(J, added, modified):
    """Section 10, pass 3: each finding of the third values-check and its disposition, with
    the values this run computes for it."""
    rows = {r["id"]: r for r in J["rows"]}
    ref = J["header"]["ref"]
    ref7 = ref[:7]
    vc = []

    def add(finding, action, detail):
        vc.append({"finding": finding, "action": action, "detail": detail})

    # 1. L-r26: file events counted as files
    r26 = rows["L-r26"]["pre_data"]
    ev26 = ["%s %s `%s`" % (f["commit"], "adds" if f["change"] == "added" else "extends (model output)", f["path"]) for f in r26["files"]]
    ns = {}
    for cm, p in added + modified:
        if cm[:7] in ("5aa9389", "db0d177") and match(p, ["results/raw/2026-08-12_rule26_*", "data/regression/*"], []):
            ns.setdefault(cm[:7], []).append("%s %s" % ("A" if (cm, p) in added else "M", p))
    over = ["%s (%d events, %d paths)" % (r["id"], r["pre_data"]["n_file_events"], r["pre_data"]["n_paths_data"] + r["pre_data"]["n_paths_model_free"])
            for r in J["rows"] if r["pre_data"]["n_file_events"] != r["pre_data"]["n_paths_data"] + r["pre_data"]["n_paths_model_free"]]
    add("L-r26 same-subject data: '3 files ... of these, 1 file by modification only', a double count introduced by the pass-2 fix (substantive)", "fixed",
        "Correct. The added and modify-only indexes give, under the row's paths: %s. That is %d distinct paths: %s. The count was of file events, and a path added at "
        "5aa9389 and extended at db0d177 was called 'by modification only'. Counts are now of distinct paths (JSON `pre_data.paths_data`, `pre_data.n_paths_data`; "
        "`pre_data.files` keeps the events, each with `path_added_earlier_in_list`); an extension of a path the list already adds is described as such, and 'by "
        "modification only' is kept for a path the list never adds. Rows whose file events outnumber their distinct paths: %s; in every other row they are equal. "
        "Section 2 row 13, section 7 item 6 and pass-1 disposition 6 now read %s." % (
            "; ".join("%s: %s" % (k, ", ".join(v)) for k, v in sorted(ns.items())), r26["n_paths_data"], ", ".join("`%s`" % p for p in r26["paths_data"]),
            ", ".join(over) or "none", pre_count_str(rows["L-r26"])))

    # 2. hash record wording
    hs = J["commit_hash_record_split"]
    add("'What the record supports ... with the commit hash itself recorded in a later commit' is false for 12 of the 23 rows with data (substantive)", "fixed",
        "Correct. The version's commit hash is recorded in no tracked file or commit message for %d rows (%s: `git log -S` over every tracked path and `git log --grep`, "
        "audit files excluded; 'Hash recorded' reads 'commit hash: none'), and in a later commit for %d (%s; before the row's first data for %d, not before it for %d: %s). "
        "The sentence now says so in the item outcome, section 7 item 3 and the hash PI item (pass 4, finding 2, scopes it to the row's displayed version and adds the "
        "later versions that govern cells). One departure from the checker's proposed text: it would say that for the "
        "12 'the ordering rests on the commit graph alone'. The ordering evidence is the commit graph (`git merge-base --is-ancestor`) for every row, and a later record "
        "of the hash adds nothing to it for the other 11, so the text says that for all rows, and for the 12 that the record never names the version's commit, which "
        "is identified from git alone (log and blame)." % (
            len(hs["recorded_nowhere"]), ", ".join(hs["recorded_nowhere"]), len(hs["recorded_in_a_later_commit"]), ", ".join(hs["recorded_in_a_later_commit"]),
            len(hs["recorded_before_first_data"]), len(hs["recorded_not_before_first_data"]), ", ".join(hs["recorded_not_before_first_data"]) or "none"))

    # 3. c1 tier rationale
    a = J["judgment_call_alternatives"]["c1"]
    cl = J["c1_tier_locators"]
    add("L-c1 r1/r2 counted as verdict: the rationale omits the governing entry's own 'gate' wording, and the call sits ill with section 0's rule (minor)", "fixed",
        "Correct that the rationale was incomplete: the governing entry itself, not only the r2 entry, calls the read a gate (%s 'Pre-registered gate read'; %s-%s 'c2 is "
        "deliberately unbuilt until c1's gate reads out'), while its header calls the full run the primary experiment (%s). Both clauses of section 0's definition fire, and "
        "section 0 did not say which one wins; it now says that Code counts such a cell as verdict and gives the other reading's counts. The classification is kept and "
        "routed: L-c1's tier note and the PI judgment-call item now cite these lines, and the counts under the gate reading are %d verdict cells in %d rows, with "
        "rows without verdict-tier data %s, and %s. Section 7 item 2 gives the same recount for each of the four calls (JSON `judgment_call_alternatives`); "
        "order and STOPs are unchanged under every one." % (
            cl[1], cl[2], (cl[3] or "").rsplit(":", 1)[-1], cl[0], a["verdict_cells_with_data"], a["rows_with_verdict_data"],
            ", ".join(a["rows_without_verdict_tier_data"]),
            "; ".join("%s's first verdict data %s -> %s" % (x["row"], ("`%s`" % x["as_counted"]) if x["as_counted"] else "none", ("`%s`" % x["other_reading"]) if x["other_reading"] else "none")
                      for x in a["first_verdict_data_changes"]) or "no first verdict data changes"))

    # 4. smoke tiers
    def n_smoke(path, s=None, e=None):
        L = lines_at(ref, path)
        L = L[s - 1:e] if s else L
        return sum(1 for x in L if "smoke" in x.lower())
    b2c = next(r for r in J["rows"] if r["id"] == "L-e0B2c")["entry"]
    s_, e_ = [int(x) for x in b2c["extent_ref"].rsplit(":", 1)[-1].split("-")]
    sm = [("%s / %s" % (r["id"], c["name"]), c["tier"]) for r in J["rows"] for c in r["cells"] if c["tier"]["label"] == "smoke"]
    add("Four smoke cells carry no tier locator, against section 0's 'each cell's tier, and the line it rests on' (minor)", "fixed",
        "Correct. The governing texts do not name these smokes: 'smoke' occurs %d times in PROPOSAL-e, %d times in the B2c entry (%s), %d in PROPOSAL-h and %d in LOCK-h "
        "(at ref, case-insensitive). Each smoke cell now rests on the log entry that reports the run, marked [log-only]: %s. Section 0 says so. Cells with data "
        "and no tier locator: %s." % (
            n_smoke("PROPOSAL-e-reward-axis-hijack.md"), n_smoke(A34, s_, e_), b2c["extent_ref"], n_smoke(PH), n_smoke(LH),
            "; ".join("%s: %s%s" % (nm, t["locator"], "".join(", %s" % x["locator"] for x in t["also"])) for nm, t in sm),
            ", ".join(J["data_cells_without_tier_locator"]) or "none"))

    # 5. STOPs line
    bl = J["block_referent_lines"]
    add("Item outcome 'STOPs: 0 ... neither occurs' is flat where each leg rests on a reading routed to the PI (minor)", "fixed",
        "Correct. The line now says the two conditions do not occur under Code's two readings (hash: absence is not mismatch; order: the cells each version governs), "
        "both PI items, and states what the opposite readings would give (a hash STOP on %d rows, %s, count revised in pass 4, finding 1; a same-commit order STOP on L-c1 and "
        "L-dgate). It cites the basis the checker named for the hash leg: the block's referent line :%s presumes the content hashes were recorded before data, so "
        "their absence is a wrong referent, which its preamble (:%s) makes a note; section 8 now carries that as a referent note. STOPs remain %d: the block's "
        "text licenses none under the declared readings." % (
            len(J["hash_conjunct"]["unmet"]),
            ("the %d with data" % J["hash_conjunct"]["rows_with_data"] if len(J["hash_conjunct"]["unmet_with_data"]) == J["hash_conjunct"]["rows_with_data"]
             else "%d of the %d with data" % (len(J["hash_conjunct"]["unmet_with_data"]), J["hash_conjunct"]["rows_with_data"]))
            + ((" and %s" % ", ".join(J["hash_conjunct"]["unmet_without_data"])) if J["hash_conjunct"]["unmet_without_data"] else ""),
            bl["content_hashes_recorded_before_data"], bl["wrong_referent_is_a_note"], len(J["stops"])))

    # 6. model-free files in same-subject lists
    mf = [(r["id"], r["pre_data"]["n_paths_data"], r["pre_data"]["paths_model_free"]) for r in J["rows"] if r["pre_data"]["paths_model_free"]]
    tl, _ = locate(ref, RM, "tokenizer loaded once, model process closed", 1)
    bd = [(r["id"], f["path"]) for r in J["rows"] for f in r["pre_data"]["files"] if f["path"] in PRE_DATA_BORDERLINE]
    allp, keys = {}, {}
    for r in J["rows"]:
        for f in r["pre_data"]["files"]:
            allp.setdefault(f["path"], f["forward_markers"])
            keys.setdefault(f["path"], f.get("top_level_keys"))
    weak = {'"provenance"', '"adapter"', '"n_layers"'}
    unmarked = sorted(p for p, m in allp.items() if m == [])
    npz = sorted(p for p, m in allp.items() if m is None)
    load_only = sorted(p for p, m in allp.items() if m and all(x.startswith("loaded in") for x in m))
    prov_only = sorted(p for p, m in allp.items() if m and set(m) <= weak)
    prov_json = [p for p in prov_only if p not in PRE_MODEL_FREE and isinstance(keys.get(p), list)]
    prov_nonparse = [p for p in prov_only if p not in PRE_MODEL_FREE and keys.get(p) == "not one JSON document"]
    prov_other = [p for p in prov_only if p not in PRE_MODEL_FREE and p not in prov_json and p not in prov_nonparse]
    add("P-g and Q1: '27 files' of same-subject data include 5 model-free bring-up files (minor)", "fixed",
        "Correct (`git show` of each: the manifest, the download and cast log, the hashing log, and the cast-equality JSON and log, whose comparison is of tensor digests, "
        "'per-tensor mismatches: 0'; none runs a forward). Model-free files are now counted apart (section 0's list names download, cast and hashing logs and "
        "tokenizer-only checks): %s. The checker audited only P-g and Q1; Code checked every row's list. All %d distinct same-subject files were scanned at ref for "
        "forward-pass markers (JSON `pre_data.files[].forward_markers`; %d binary arrays are not scanned, each with a scanned companion JSON). Read with `git show`: "
        "the %d files the scan left unmarked (%s); the %d it marked only by weight loading (%s); and the %d marked only by a provenance block: P-k's neutral-label "
        "selection (below), %d JSONs by their top-level fields (JSON `pre_data.files[].top_level_keys`: measurement fields such as per-layer norms, choice mass, "
        "tag-screen pairs and rankings, dose ladders, concept vectors and trial records)%s, and %s. "
        "One more file is model-free: P-k's data/format/neutral_label_selection.json (b0b2e60), whose fields are token counts and roster/pool checks although it "
        "carries a provenance block (%s 'tokenizer loaded once, model process closed'). Counted as data, with a note in its row: %s. Every other same-subject file "
        "is a forward-pass output or an analysis of one (section 0's data rule says from pass 4, finding 3, that analyses are counted with the data)." % (
            "; ".join("%s: %d data files, plus %d model-free (%s)" % (i, nd, len(m), ", ".join("`%s`" % x for x in m)) for i, nd, m in mf),
            len(allp), len(npz), len(unmarked), ", ".join("`%s`" % p for p in unmarked), len(load_only), ", ".join("`%s`" % p for p in load_only),
            len(prov_only), len(prov_json),
            (", %d that do not parse as one JSON document (%s) by their companion raws' model-load lines" % (len(prov_nonparse), ", ".join("`%s`" % p for p in prov_nonparse))) if prov_nonparse else "",
            ("the raw %s" % ", ".join("`%s`" % p for p in prov_other)) if prov_other else "no other file", tl,
            "; ".join("%s `%s` (%s)" % (i, p, PRE_DATA_BORDERLINE[p]) for i, p in bd) or "none"))
    J["values_check_pass3"] = vc
    J["values_check_pass3_intro"] = ("Values-check pass 3: a strict checker re-ran the script into scratch (identical apart from the stamp and command lines; redaction check clean), "
                                     "recomputed the order, gaps, data-commit lists, tiers and counts with its own code, confirmed STOPs = 0 under the block's text and the declared readings, "
                                     "and reported two substantive and four minor findings. Each is listed with Code's disposition after checking it against the record; values quoted are this run's.")


ANALYSIS_NAME = re.compile(r"analysis|posthoc|analyze")


def analysis_only_commits(J, added, modified):
    """Commits in the rows' same-subject data lists whose every added or modified file under data/ and
    results/raw/ is an analysis by name (values-check pass 4, finding 3); and the governed cells whose
    first-data files are all analyses by name."""
    by_commit = {}
    for cm, p in added + modified:
        by_commit.setdefault(cm[:7], []).append(p)
    out = {}
    for r in J["rows"]:
        for f in r["pre_data"]["files"]:
            if f["class"] != "data":
                continue
            ps = by_commit.get(f["commit"][:7], [])
            if ps and all(ANALYSIS_NAME.search(os.path.basename(p)) for p in ps):
                e = out.setdefault(f["commit"][:7], {"commit": f["commit"][:7], "committer_utc": meta(f["commit"])["committer_utc"],
                                                     "subject": meta(f["commit"])["subject"], "paths_data_raw": sorted(set(ps)), "rows": [], "row_paths": []})
                if r["id"] not in e["rows"]:
                    e["rows"].append(r["id"])
                if f["path"] not in e["row_paths"]:
                    e["row_paths"].append(f["path"])
    first_ana = [(r["id"], c["name"]) for r in J["rows"] for c in r["cells"]
                 if c.get("first_data_commit") and not c.get("inputs_only") and c.get("first_data_paths")
                 and all(ANALYSIS_NAME.search(os.path.basename(p)) for p in c["first_data_paths"])]
    n_gov = sum(1 for r in J["rows"] for c in r["cells"] if c.get("first_data_commit") and not c.get("inputs_only"))
    J["analysis_only_commits"] = sorted(out.values(), key=lambda e: meta(e["commit"])["committer_unix"])
    J["governed_cells_first_data_analysis_only"] = {"cells": first_ana, "of": n_gov, "rule": "basename matches /%s/" % ANALYSIS_NAME.pattern}


def build_values_check_pass4(J, added, modified):
    """Section 10, pass 4: each finding of the fourth values-check and its disposition, with
    the values this run computes for it."""
    rows = {r["id"]: r for r in J["rows"]}
    ref = J["header"]["ref"]
    vc = []

    def add(finding, action, detail):
        vc.append({"finding": finding, "action": action, "detail": detail})
    hc = J["hash_conjunct"]

    # 1. A-g1: no data, no recorded sha256
    nd = [rows[i] for i in hc["unmet_without_data"]]
    pm = [r for r in J["rows"] if r["id"] in hc["met"] and r["status"].startswith("NO GOVERNED DATA")]

    def vsha(r):
        v = next(v for v in r["versions"] if v["commit"] == r["record_commit"][:7])
        rs = v["first_recording_of_sha256"]
        return v["sha256"][:8], bool(rs["file_hit"]), bool(rs["message_hit"])
    add("Item outcome 'Hash conjunct: unmet for 23/23 rows with data' and 'all 23 rows with data would carry a hash STOP' leave out A-g1, which has no data and no recorded sha256 (substantive)",
        "fixed",
        "Correct. Block :93's pass condition ('every row's recomputed sha matches the recorded one') has no data qualifier, and %s. The split was built from rows with "
        "data, so a row without data was left out by construction. %s now read%s '%s', and section 0's status vocabulary carries that combination; %s keep%s "
        "'NO GOVERNED DATA IN THE RECORD' (recorded sha256 reproduced). The hash conjunct now reads 'unmet for %d of %d rows: %s (every row but %s)' (item outcome; "
        "JSON `hash_conjunct`), and the opposite-reading clause now counts %d rows (%s) in the item outcome ('would carry a hash STOP'), the hash PI item and pass-3 disposition 5. "
        "The section 8 referent note on :%s carries the count rather than an opposite-reading clause; it now reads 'for %d of the %d rows (%s) none is recorded at all'. "
        "STOPs remain %d: under Code's reading of absence no hash STOP is declared, for A-g1 as for the rest." % (
            "; ".join("%s's version of record `%s` has sha256 `%s...`, whose 8-hex prefix is recorded in %s and in %s "
                      "(`git log -S` over every tracked path and `git log --grep`, audit files and *.npz excluded; JSON `rows[%s].recorded_sha256.found` = %s)" % (
                          r["id"], r["record_commit"][:7], vsha(r)[0], "a tracked file" if vsha(r)[1] else "no tracked file",
                          "a commit message" if vsha(r)[2] else "no commit message", r["id"],
                          r["recorded_sha256"]["found"]) for r in nd) or "no row without data lacks a recorded sha256",
            ", ".join("%s's status" % r["id"] for r in nd) or "no status", "s" if len(nd) == 1 else "",
            "; ".join(sorted(set(r["status"] for r in nd))) or "-",
            ", ".join("%s (`%s...`)" % (r["id"], vsha(r)[0]) for r in pm) or "no row", "s" if len(pm) == 1 else "",
            len(hc["unmet"]), hc["rows"], ("the %d rows with data" % hc["rows_with_data"]) + "".join(" and %s" % r["id"] for r in nd), ", ".join(hc["met"]) or "none",
            len(hc["unmet"]), ("the %d with data" % hc["rows_with_data"]) + "".join(" and %s" % r["id"] for r in nd),
            J["block_referent_lines"]["content_hashes_recorded_before_data"],
            len([r for r in J["rows"] if not r.get("recorded_sha256", {}).get("found")]), len(J["rows"]),
            ("the %d with data" % hc["rows_with_data"]) + "".join(" and %s" % r["id"] for r in nd), len(J["stops"])))

    # 2. the commit-hash split reads the displayed version
    hs = J["commit_hash_record_split"]
    lat = J["later_governing_versions"]
    gf = J["first_data_governed_by_a_later_version"]
    add("'For 11 of the 23 rows with data the version's commit hash is also recorded in a later commit ...' reads only each row's displayed version (minor)", "fixed",
        "Correct. The split (%d recorded in a later commit, %d of them before the row's first data, %d recorded nowhere) is computed from each row's displayed version "
        "(version of record). The later versions that govern cells, from the per-version fields (`first_recording_of_commit_hash`, computed by `git log -S` per "
        "token over every tracked path and `git log --grep`, audit files excluded; `commit_hash_*_record_before_governed_data`, by ancestry): %s. "
        "%s The sentence now names the displayed version (column 'Hash recorded'), adds the later governing versions recorded nowhere or only after their governed "
        "data, and names the version that governs a row's first data where it is not the displayed one; it is the record-supports sentence of the item outcome and "
        "section 7 item 3, and the hash PI item carries the same clauses. The split's counts are unchanged." % (
            len(hs["recorded_in_a_later_commit"]), len(hs["recorded_before_first_data"]), len(hs["recorded_nowhere"]),
            "; ".join("%s %s `%s` (governs %s): %s%s, first governed data `%s`" % (
                x["row"], x["version"], x["commit"], "; ".join(x["governs"]), x["class"],
                (", first recorded at `%s` %s" % (x["first_record"], x["first_record_committer_utc"])) if x["first_record"] else "",
                x["first_governed_data"]) for x in lat) or "none",
            " ".join("For %s, the displayed version %s `%s` (first recorded at `%s`) %s; its first data `%s` is governed by %s `%s`, first recorded at `%s`, %s it, so %s's place in the split %s." % (
                g["row"], g["displayed_version"], g["displayed"], g["displayed_first_record"] or "nowhere",
                "governs no cell with data" if not g["displayed_governs_a_cell_with_data"] else "does not govern the row's first data",
                g["first_data"], g["governing_version"], g["governing"], g["governing_first_record"] or "nowhere",
                "before" if g["governing_record_before_first_data"] else "not before", g["row"],
                "holds" if (g["split_place"] == "before") == g["governing_record_before_first_data"] else "would change") for g in gf) or
            "Every row's first data is governed by its displayed version."))

    # 3. analyses counted with the data
    ao = J["analysis_only_commits"]
    fa = J["governed_cells_first_data_analysis_only"]
    pk = rows["P-k"]["pre_data"]
    add("Section 0's data rule ('produced by forward passes') does not say that analyses, including re-analyses committed without new forwards, count as data (minor)", "fixed",
        "Correct. Commits in the rows' same-subject data lists whose every added or modified file under data/ and results/raw/ is an analysis by name (%s; "
        "the index of added and modify-only files at ref): %s. No reads, sessions or other non-analysis file under data/ or results/raw/ is added in %s (by name, "
        "the same index). Applied as the "
        "first of the checker's two alternatives: section 0's data rule now says that analyses computed from forward outputs, including re-analyses committed "
        "without new forwards, are counted with the data, naming these commits; disposition 6 of pass 3 points to it. Counts are unchanged: P-k reads %d data "
        "files plus %d model-free. Governed cells with data whose first-data files all match the same name rule: %s of %d, so no cell's first data "
        "commit depends on the rule." % (
            fa["rule"],
            "; ".join("`%s` %s (%s; adds %s; in %s's list as %s)" % (
                e["commit"], e["committer_utc"], clip(e["subject"], 110), ", ".join("`%s`" % p for p in e["paths_data_raw"]), ", ".join(e["rows"]),
                ", ".join("`%s`" % p for p in e["row_paths"])) for e in ao) or "none",
            "either commit" if len(ao) == 2 else ("that commit" if len(ao) == 1 else "any of them"),
            pk["n_paths_data"], pk["n_paths_model_free"], len(fa["cells"]) if fa["cells"] else "none", fa["of"]))
    J["values_check_pass4"] = vc
    J["values_check_pass4_open_from_previous"] = []
    J["values_check_pass4_intro"] = ("Values-check pass 4: a checker re-checked this version against the record with its own git searches and reported one substantive and "
                                     "two minor findings; no finding was carried open from earlier passes. Each is listed with Code's disposition after checking it "
                                     "against the record; values quoted are this run's.")


READING = []

if __name__ == "__main__":
    main()
