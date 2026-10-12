#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N17 (Tier 3): Qwen numerics and the patch.

Read-only. Writes one markdown raw (default
results/raw/2026-10-08_note-N17-numerics.md). Optional --json-out writes a
machine copy of the figures table; it is OFF by default (only the .md is an
assigned output of this item).

Sources, in four classes, kept apart everywhere in the output:
  * committed record, read with `git show <PIN>:<path>` (figures computed
    from committed JSON/JSONL are `reproduced`; prose is `log-only` with a
    pinned locator `path@PIN:line`);
  * the record's history (an artifact as committed at an earlier commit
    reachable from PIN; said so wherever used);
  * the local Hugging Face snapshot of mlx-community/Qwen3.6-27B-4bit (not a
    repository file; facts read from config.json and the safetensors
    *headers* -- no tensor is loaded): `computed-new`;
  * the gitignored jlens-qwen36 clone and the venv's installed mlx-lm source,
    read as FILES (no git command inside the clone, nothing imported from
    either, nothing executed): context only, `computed-new`, never record.

No model inference; nothing imported from mlx or from the clone; no write
anywhere except --out (and --json-out if given).

Round 9 (2026-10-10; the PI's ruling 9 of 2026-10-10, as corrected): the
preprint of record is PREPRINT-v1_0-draft.md (root, untracked; committed at
the tag) at sha256 0f4ba501...6c22 (patch v6). The block's reference,
d6431e97...222b8 (AUDIT-note-release-v1_2.md:21), is the audited, superseded
text, archived untracked at archive/PREPRINT-v1_0-draft.pre-patch-v6.md; that
copy is read only if present (to quote an audited line beside its patched
one) and is never required. Section 2a asserts the full sha256 equal to
ruling 9's value before anything is written (a different or absent root text
refuses the run), and its 'Qwen ran at' lookup no longer raises when the
sentence is gone (section 12 records it). Section 5's earlier-wording source
is chosen from the archived drafts only, never from the preprint of record.
Section 12 re-runs every check this script makes of a preprint sentence on
the patched text, anchoring the audited side on this item's raw as committed
at 09c3a8c (P-b and P-c by a full scan of the archived copy when it is
present and matches the block's reference); a check that fails there is a
finding on the patch for the design seat, not a STOP; section 12 ends with
its own locator self-check. --json-out gains one key, preprint_round9.
Nothing else changed.

Round 10 (2026-10-12; the PI's routing of 2026-10-12, the round-10 inputs): the
preprint of record is PREPRINT-v1_0-draft.md at sha256 d9635ca2...1fe6 (patch
v7); section 2a asserts that full value where it asserted 0f4ba501...6c22,
before anything is written (a different or absent root text refuses the run,
as before). Patch v6 (0f4ba501...6c22, round 9's preprint of record) is the
pre-patch copy the routing places at archive/PREPRINT-v1_0-draft.pre-patch-v7.md,
untracked, out of the release: recorded, never required; read only if present
and matching, to quote a v6 line beside its v7 line (whether it is: 12a). The
audited text's handling (d6431e97...222b8,
archive/PREPRINT-v1_0-draft.pre-patch-v6.md, the raw at 09c3a8c) is as round 9
left it. Section 12 re-runs round 9's checks on the v7 text and adds
12a: each finding on the patch this item's raw recorded at 84801cb, with its
disposition on v7 (resolved | unchanged | changed, v6 and v7 quoted); every
check that passed on v6 and fails on v7; and the figures of every v7-changed
sentence the checks read, those in this script's scope verified against its
own record sources (section 5 item 2). A failing check is a finding on the
patch for the design seat, never a STOP. The section-12 self-check also
covers locators at 84801cb. --json-out gains one key, preprint_round10;
preprint_round9.ruling9_sha256 keeps ruling 9's value (its match compares this
run's text with it), and its new field computed_on says that its checks and
findings are this run's text (v7), round 9's own findings on v6 being
preprint_round10.round9_findings. Nothing else changed.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import platform
import re
import statistics
import struct
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA_ROUTED = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
PREPRINT = "PREPRINT-v1_0-draft.md"           # untracked; read from disk
# Round 10: the preprint of record (the PI's routing of 2026-10-12): patch v7.
PREPRINT_SHA = "d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6"
# Round 9's preprint of record (the PI's ruling 9 of 2026-10-10, as corrected): patch v6,
# archived untracked, out of the release; recorded, never required.
PREPRINT_SHA_V6 = "0f4ba501d60a94189e6dc83d28c41826debe50591b9af484fa08d05a41f16c22"
PREPRINT_V6 = "archive/PREPRINT-v1_0-draft.pre-patch-v7.md"  # untracked; optional
RAW_ROUND9 = ("results/raw/2026-10-08_note-N17-numerics.md", "84801cb")  # this item's raw, round 9
# The block's reference (:21, `d6431e97…222b8`): the audited, superseded text.
PREPRINT_SHA_BLOCK_PREFIX = "d6431e97"
PREPRINT_SHA_BLOCK_SUFFIX = "222b8"
PREPRINT_AUDITED = "archive/PREPRINT-v1_0-draft.pre-patch-v6.md"  # untracked; optional
RAW_AUDITED = ("results/raw/2026-10-08_note-N17-numerics.md", "09c3a8c")  # this item's raw as committed
OUT_DEFAULT = "results/raw/2026-10-08_note-N17-numerics.md"
CLONE = os.path.join(REPO, "jlens-qwen36")
HF_REPO_DIR = os.path.expanduser(
    "~/.cache/huggingface/hub/models--mlx-community--Qwen3.6-27B-4bit")
HOME = os.path.expanduser("~")


# ---------------------------------------------------------------- helpers
def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", REPO, *args], capture_output=True,
                       text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


_SHOW: dict = {}


def show(path: str, commit: str = PIN) -> str:
    """`git show commit:path` read as BYTES and split later on b'\\n' only.

    Values-check finding 4: text=True turns on universal newlines, so a bare
    '\\r' (an HF progress bar in a raw) became an extra line and shifted every
    later line number by the count of such characters. Bytes + utf-8 decode
    keep line numbers equal to `git show ... | sed -n`.
    """
    key = (commit, path)
    if key not in _SHOW:
        r = subprocess.run(["git", "-C", REPO, "show", f"{commit}:{path}"],
                           capture_output=True)
        if r.returncode != 0:
            raise RuntimeError(f"git show {commit}:{path} failed: "
                               f"{r.stderr.decode(errors='replace').strip()}")
        _SHOW[key] = r.stdout.decode("utf-8", errors="replace")
    return _SHOW[key]


def lines_of(path: str, commit: str = PIN) -> list[str]:
    return show(path, commit).split("\n")


def find(path: str, needle: str, start: int = 1, commit: str = PIN,
         nth: int = 1) -> int:
    """1-indexed line number of the nth line (from `start`) containing needle."""
    seen = 0
    for i, ln in enumerate(lines_of(path, commit), start=1):
        if i < start:
            continue
        if needle in ln:
            seen += 1
            if seen == nth:
                return i
    raise LookupError(f"anchor not found: {path}@{commit}: {needle!r}")


def text_span(path: str, a: int, b: int, commit: str = PIN) -> str:
    ls = lines_of(path, commit)
    return " ".join(x.strip() for x in ls[a - 1:b])


def loc(path: str, a: int, b: int | None = None, commit: str = PIN) -> str:
    if b is None or b == a:
        return f"{path}@{commit}:{a}"
    return f"{path}@{commit}:{a}-{b}"


def file_lines(p: str) -> list[str]:
    # newline="" : no newline translation, so line numbers match `sed -n`.
    with open(p, encoding="utf-8", errors="replace", newline="") as fh:
        return fh.read().split("\n")


def ffind(p: str, needle: str, start: int = 1, nth: int = 1,
          exact: bool = False) -> int:
    seen = 0
    for i, ln in enumerate(file_lines(p), start=1):
        if i >= start and ((ln.strip() == needle) if exact else (needle in ln)):
            seen += 1
            if seen == nth:
                return i
    raise LookupError(f"anchor not found on disk: {p}: {needle!r}")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: str) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_sha1(p: str) -> str:
    with open(p, "rb") as fh:
        b = fh.read()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def tilde(p: str) -> str:
    return p.replace(HOME, "~", 1) if p.startswith(HOME) else p


def rel_clone(p: str) -> str:
    return os.path.relpath(p, REPO)


def cell(x) -> str:
    return str(x).replace("|", "\\|").replace("\n", " ")


def q(s: str, n: int = 400) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 3] + "..."


# ------------------------------------------------------------ main body
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=OUT_DEFAULT)
    ap.add_argument("--json-out", default=None,
                    help="optional machine copy of the figures table "
                         "(off by default)")
    ap.add_argument("--hf-snapshot", default=None,
                    help="local snapshot dir of mlx-community/Qwen3.6-27B-4bit "
                         "(default: resolved from the HF cache refs/main)")
    args = ap.parse_args()

    out: list[str] = []
    w = out.append
    figs: list[dict] = []
    flags: list[str] = []
    clause_map: list[tuple[str, str]] = []
    f1_idx = None

    def fig(figure, value, source, status, note=""):
        figs.append(dict(figure=figure, value=value, source=source,
                         status=status, note=note))

    # ------------------------------------------------------------ header
    stamp = subprocess.run(["date", "-u"], capture_output=True,
                           text=True).stdout.strip()
    head = git("rev-parse", "HEAD").strip()
    pin_full = git("rev-parse", PIN).strip()
    block_pin = show(BLOCK).encode()
    block_sha_pin = sha256_bytes(block_pin)
    block_sha_wt = sha256_file(os.path.join(REPO, BLOCK))
    script_rel = os.path.relpath(os.path.abspath(__file__), REPO)
    script_sha = sha256_file(os.path.abspath(__file__))
    # sys.orig_argv keeps interpreter flags (e.g. -B); the script argument is
    # printed repo-relative (values-check finding 14).
    oa = list(getattr(sys, "orig_argv", []) or [sys.executable] + sys.argv)
    try:
        si = next(i for i, x in enumerate(oa) if i > 0 and os.path.abspath(x) == os.path.abspath(__file__))
        oa[si] = script_rel
    except StopIteration:
        pass
    oa[0] = sys.executable
    cmd = " ".join(oa)
    try:
        import numpy  # noqa: F401  (version reported only; not used)
        npver = numpy.__version__
    except Exception:  # pragma: no cover
        npver = "absent"

    w("# AUDIT-note-release v1.2 -- N17: Qwen numerics and the patch")
    w("")
    w(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    w(f"- HEAD at run time: {head}  [run metadata; every record read below is "
      f"pinned to {PIN}]")
    w(f"- Pin: {PIN} = {pin_full}")
    w(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_sha_pin}` "
      f"({'MATCH' if block_sha_pin == BLOCK_SHA_ROUTED else 'MISMATCH'} vs "
      f"routed 8cd8a9ac...3841; working tree "
      f"{'equal' if block_sha_wt == block_sha_pin else 'DIFFERENT'}); "
      f"{len(block_pin.decode().splitlines())} lines; item N17 = block lines "
      f"{find(BLOCK, '### N17.')}-{find(BLOCK, '### N17.') + 1}")
    w(f"- Script: `{script_rel}` sha256 `{script_sha}`")
    w(f"- Interpreter: {sys.executable} (Python {platform.python_version()}; "
      f"numpy {npver}, imported for its version string only); stdlib for "
      f"every computation; no mlx import, no model load")
    w(f"- Command: `{cmd}`  (cwd = repository root)")
    w("")
    w("Status vocabulary: **reproduced** (this script computes the figure "
      "from committed JSON/JSONL and prints it) | **log-only** (record prose "
      "or a text raw; pinned locator) | **not found** | **discrepant** | "
      "**computed-new** (computed here from a non-record source, said which). "
      f"Locators are `path@{PIN}:line` (line numbers of "
      f"`git show {PIN}:<path>`). Sources outside the repository -- the "
      "local Hugging Face snapshot and the gitignored `jlens-qwen36/` clone "
      "with its venv -- are read as files and labelled as such. Some README "
      "clauses rest on those computed-new reads (section 7 lists them): the "
      "quantization details and the port's patch mechanics (files a reader can "
      "check against the public Hugging Face revision c000ac2c, upstream "
      "WeZZard/jlens-qwen36 d788bc3 and mlx-lm 0.31.3), and the clause on the "
      "lab's own edits inside the clone (untracked there and not in this "
      "repository, so a reader cannot check it).")
    w("")

    # -------------------------------------------------------- 0. item text
    a17 = find(BLOCK, "### N17.")
    w("## 0. The item")
    w("")
    w(f"{loc(BLOCK, a17, a17 + 1)}: \"{q(text_span(BLOCK, a17 + 1, a17 + 1), 900)}\"")
    w("")
    w("Destination per the block's §6 item (6): "
      f"{loc(BLOCK, find(BLOCK, '(6) the cached-generation and numerics disclosures'))}"
      " -- the README-NOTE carries this paragraph beside N4(iv)'s cached-"
      "generation paragraph.")
    w("")

    # ---------------------------------------------------- 1. quantization
    w("## 1. The quantization")
    w("")
    # 1a record
    ora = json.loads(show("data/regression/oracle_rule26.json"))
    prov = ora["provenance"]
    w("### 1a. What the record says")
    w("")
    w(f"- `data/regression/oracle_rule26.json`@{PIN} `provenance`: "
      f"model_id `{prov['model_id']}`, dtype `{prov['dtype']}`, backend "
      f"`{prov['backend']}`, library_versions {prov['library_versions']}, "
      f"python {prov['python']}, platform `{prov['platform']}`, "
      f"gdn_inference_mode `{prov['gdn_inference_mode']}`, n_layers "
      f"{prov['n_layers']}.  [reproduced]")
    fig("model + precision (record)", f"{prov['model_id']}; dtype "
        f"'{prov['dtype']}'", "data/regression/oracle_rule26.json:provenance."
        "model_id, .dtype", "reproduced",
        "the record's own field says 4-bit MLX; bits/group/tensors are not "
        "recorded in any committed artifact (see 1b)")
    fig("library versions", f"mlx {prov['library_versions']['mlx']}, mlx-lm "
        f"{prov['library_versions']['mlx-lm']}, numpy "
        f"{prov['library_versions']['numpy']}",
        "data/regression/oracle_rule26.json:provenance.library_versions",
        "reproduced")
    # --- coverage of the library versions (values-check finding 7) ---------
    lv_files = sorted(x.split(":", 1)[1] for x in
                      git("grep", "-l", '"mlx-lm"', PIN, "--", "data").splitlines())

    def walk_lv(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "library_versions":
                    yield json.dumps(v, sort_keys=True)
                yield from walk_lv(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk_lv(v)

    lv_vals: dict = {}
    lv_olmo = 0
    for f in lv_files:
        lv_olmo += f.startswith("data/olmo/")
        try:
            d_ = json.loads(show(f))
        except Exception:
            d_ = [json.loads(x) for x in show(f).splitlines() if x.strip()]
        for v in set(walk_lv(d_)):
            lv_vals[v] = lv_vals.get(v, 0) + 1
    first_lv = git("log", "--reverse", "-S", '"mlx-lm": "0.31.3"', "--format=%h %ad",
                   "--date=short", PIN, "--", "data").strip().splitlines()[0]
    db_prov = json.loads(show("data/regression/oracle_rule26.json", "db0d177"))["provenance"]
    lp_ = find("RESULTS.md", "- **Provenance (rule 27):** adapter `qwen3.6-27b-4bit-mlx`,")
    c12_ = find("archive/RESULTS-cycle1-2.md", "which crashes on import against `mlx-lm==0.31.3`")
    # where the record states the MLX CORE version (not mlx-lm), outside data/
    core_pat = r'mlx_version|"mlx": "0\.|mlx 0\.[0-9]|mlx==0\.|mlx-0\.[0-9]'
    core_hits = subprocess.run(["git", "-C", REPO, "grep", "-n", "-I", "-E", core_pat, PIN,
                                "--", ".", ":!data"], capture_output=True).stdout.decode(
                                    "utf-8", "replace").splitlines()
    core_files: dict = {}
    for h in core_hits:
        f_ = h.split(":", 2)[1]
        core_files[f_] = core_files.get(f_, 0) + 1
    core_archive = {f: n for f, n in core_files.items() if f.startswith("archive/RESULTS-")}
    core_raw_dates = sorted({f.split("/")[-1][:10] for f in core_files
                             if f.startswith("results/raw/")})
    core_line = (f"Where the record states the MLX core version (git grep `{core_pat}` at {PIN} "
                 f"outside data/): {core_files}; in the cycle 1-4 logs "
                 f"(archive/RESULTS-cycle1-2.md, archive/RESULTS-cycles3-4.md): "
                 f"{core_archive if core_archive else 'none'}; the dated raws among the hits run "
                 f"from {core_raw_dates[0] if core_raw_dates else '-'} to "
                 f"{core_raw_dates[-1] if core_raw_dates else '-'}.")
    w(f"- Record coverage of the library versions: {len(lv_files)} committed `data/` files "
      f"at {PIN} carry an `\"mlx-lm\"` field ({lv_olmo} of them OLMo); their "
      f"`library_versions` values: {lv_vals}. The earliest commit whose `data/` diff adds "
      f"`\"mlx-lm\": \"0.31.3\"` (`git log --reverse -S`): {first_lv} (the oracle artifact; "
      f"its first version, db0d177 2026-08-12, recorded `mlx_version` "
      f"{db_prov.get('mlx_version')!r} and no `library_versions`). Before that the "
      f"versions are log-only: the 2026-08-12 oracle entry, "
      f"{loc('RESULTS.md', lp_, lp_ + 2)}: \"{q(text_span('RESULTS.md', lp_, lp_ + 2), 300)}\"; "
      f"and mlx-lm at setup (2026-07-16), {loc('archive/RESULTS-cycle1-2.md', c12_ - 1, c12_)}: "
      f"\"{q(text_span('archive/RESULTS-cycle1-2.md', c12_ - 1, c12_), 300)}\". {core_line}  "
      "[reproduced / log-only]")
    site_ = glob.glob(os.path.join(CLONE, ".venv", "lib", "python3*", "site-packages"))
    inst = []
    if site_:
        for pat_ in ("mlx-*.dist-info", "mlx_lm-*.dist-info", "mlx_metal-*.dist-info"):
            for dd in sorted(glob.glob(os.path.join(site_[0], pat_))):
                inst.append(f"{os.path.basename(dd)} (mtime "
                            f"{time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(dd)))})")
    uvl = os.path.join(CLONE, "uv.lock")
    pins = {}
    if os.path.exists(uvl):
        ul = file_lines(uvl)
        for i_, ln in enumerate(ul):
            m_ = re.match(r'^name = "(mlx|mlx-lm|mlx-metal)"$', ln)
            if m_ and i_ + 1 < len(ul):
                pins[m_.group(1)] = ul[i_ + 1].split("=", 1)[1].strip().strip('"')
    blob_dates: dict = {}
    for bp in glob.glob(os.path.join(HF_REPO_DIR, "blobs", "*")):
        dt = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(bp)))
        blob_dates[dt] = blob_dates.get(dt, 0) + 1
    snaps = sorted(os.listdir(os.path.join(HF_REPO_DIR, "snapshots"))) \
        if os.path.isdir(os.path.join(HF_REPO_DIR, "snapshots")) else []
    w(f"- Computed-new (local files, not record): the clone venv's installed "
      f"distributions {inst}; the clone's `uv.lock` (a lab-modified file, 2f) pins {pins}; "
      f"HF cache snapshots of the model: {len(snaps)} ({[s[:8] for s in snaps]}), blob "
      f"mtimes {blob_dates}. One installed version of each package, dated at project "
      "setup; file timestamps are consistent with no reinstall since but do not prove it.")
    # --- round 2, finding 4: which artifacts carry the field (domain of "every") ---
    mid_files = sorted(x.split(":", 1)[1] for x in
                       git("grep", "-l", '"model_id"', PIN, "--", "data").splitlines())
    nonolmo = [f for f in git("ls-tree", "-r", "--name-only", PIN, "--", "data").splitlines()
               if f.endswith((".json", ".jsonl")) and not f.startswith("data/olmo/")]
    add_log = git("log", "--reverse", "-m", "--no-renames", "--diff-filter=A", "--name-only",
                  "--format=@@%h %ad", "--date=short", PIN, "--", "data")
    first_add: dict = {}
    cur_ = None
    for ln in add_log.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith("@@"):
            cur_ = ln[2:]
            continue
        first_add.setdefault(ln, cur_)
    lv_day = first_lv.split()[1]
    after_ = [f for f in nonolmo if f in first_add and first_add[f].split()[1] >= lv_day]
    after_lv = [f for f in after_ if f in lv_files]
    after_no: dict = {}
    for f in after_:
        if f not in lv_files:
            k_ = "/".join(f.split("/")[:2])
            after_no[k_] = after_no.get(k_, 0) + 1
    no_date = [f for f in nonolmo if f not in first_add]
    w(f"- Domain of the version field (round 2): `data/` JSON/JSONL files outside `data/olmo/` "
      f"at {PIN}: {len(nonolmo)}; first added (`git log -m --no-renames --diff-filter=A`) on or "
      f"after {lv_day}: {len(after_)}, of which {len(after_lv)} carry the version field and "
      f"{len(after_) - len(after_lv)} do not, by directory {after_no}"
      + (f"; add date not resolved for {no_date}" if no_date else "")
      + f". The files that record a `model_id` and the files that record the versions are the "
      f"same set: {set(mid_files) == set(lv_files)} ({len(mid_files)} = {len(lv_files)}). So the "
      "versions are recorded by every Qwen artifact that names its model, not by every Qwen "
      f"artifact committed from {lv_day} on.  [reproduced]")
    fig("library versions: record coverage, artifacts",
        f"{len(lv_files)} Qwen artifacts (the {len(mid_files)} that record a model_id) carry "
        f"{lv_vals}; first in the record at {first_lv}",
        f"git grep '\"mlx-lm\"' / '\"model_id\"' {PIN} -- data; git log -S",
        "reproduced",
        f"of {len(after_)} data/ JSON/JSONL files outside data/olmo/ first added on or after {lv_day}, "
        f"{len(after_) - len(after_lv)} record no versions (configs, corpora, schedules, analyses, "
        "and others; section 1a)")
    fig("library versions: before 2026-08-15",
        "mlx 0.31.2 / mlx-lm 0.31.3 (2026-08-12 oracle entry); mlx-lm 0.31.3 at setup (2026-07-16)",
        f"{loc('RESULTS.md', lp_, lp_ + 2)}; {loc('archive/RESULTS-cycle1-2.md', c12_ - 1, c12_)}",
        "log-only",
        "cycles 1-4 otherwise rest on the install dates and the single snapshot (computed-new, "
        "section 1a); "
        + ("the cycle 1-4 logs state no MLX core version" if not core_archive
           else f"MLX core version in the cycle 1-4 logs: {core_archive}"))
    clause_map.append(("MLX 0.31.2 / mlx-lm 0.31.3: recorded by every Qwen artifact that names its "
                       f"model, the first committed {lv_day}; the single install dated at setup and the "
                       "single model snapshot are consistent with them throughout",
                       f"artifacts: {len(lv_files)} files, first at {first_lv} (reproduced; domain "
                       f"in section 1a); {loc('RESULTS.md', lp_, lp_ + 2)} (2026-08-12); "
                       f"{loc('archive/RESULTS-cycle1-2.md', c12_ - 1, c12_)} (mlx-lm at setup, "
                       "2026-07-16); computed-new: venv dist-info dated 2026-07-16, uv.lock pins, "
                       f"{len(snaps)} HF snapshot(s), blob mtimes {blob_dates} (section 1a)"))

    a = find("CLAUDE.md", "- **Laptop (M4 Pro, MLX):**")
    w(f"- {loc('CLAUDE.md', a, a + 3)}: \"{q(text_span('CLAUDE.md', a, a + 3))}\"  [log-only]")
    clause_map.append(("Apple M4 Pro laptop; MLX", loc("CLAUDE.md", a, a + 3)))
    a = find("archive/CLAUDE-cycle1-2.md", "- **Model:** [`mlx-community/Qwen3.6-27B-4bit`]")
    w(f"- {loc('archive/CLAUDE-cycle1-2.md', a)}: \"{q(text_span('archive/CLAUDE-cycle1-2.md', a, a), 330)}\"  [log-only]")
    a = find("RESULTS.md", "§1a ARCHITECTURE (config.json of the single local snapshot")
    w(f"- {loc('RESULTS.md', a, a + 6)}: \"{q(text_span('RESULTS.md', a, a + 6), 520)}\"  [log-only; entry "
      f"{loc('RESULTS.md', find('RESULTS.md', 'RECON — ECHO CHANNEL (k-candidate). Apparatus characterization'))}]")
    first_rev = git("log", "--reverse", "-S", "c000ac2c", "--format=%h %ad", "--date=short",
                    PIN, "--", ".").strip().splitlines()[0]
    clause_map.append(("HF revision c000ac2c; 64 layers, 48 Gated DeltaNet + 16 full attention",
                       f"{loc('RESULTS.md', a, a + 6)} (log-only; the revision first enters the "
                       f"record at {first_rev}, `git log -S c000ac2c`); "
                       f"computed-new: the local HF cache holds {len(snaps)} snapshot(s) of the model "
                       f"({[s[:8] for s in snaps]}, = refs/main), blob mtimes {blob_dates} (section "
                       "1a); its config.json layer_types (section 1b)"))
    a_arch = a
    fig("48 linear-attention (Gated DeltaNet) layers, of 64 (record)", "48 of 64",
        loc("RESULTS.md", a, a + 6), "log-only",
        "the record read config.json of the same local snapshot; see the computed-new row (1b)")
    b = find("results/raw/2026-09-09_k_v11_appendixB_check.txt", "snapshots/c000ac2c")
    w(f"- {loc('results/raw/2026-09-09_k_v11_appendixB_check.txt', b)} names the snapshot path "
      "`~/.cache/huggingface/hub/models--mlx-community--Qwen3.6-27B-4bit/snapshots/c000ac2c2057d94be3fa931000c31723aac53282/config.json`.  [log-only]")
    hits = git("grep", "-h", "-o", "-E", '"model_id": "[^"]*"', PIN, "--", "data")
    mids: dict = {}
    for h in hits.splitlines():
        mids[h] = mids.get(h, 0) + 1
    w(f"- Every committed `data/` file that records a `model_id` (text search "
      f"`git grep '\"model_id\": ...' {PIN} -- data`): {mids}. No committed "
      "artifact names an unquantized Qwen.")
    w("")
    fig("revision", "c000ac2c2057d94be3fa931000c31723aac53282",
        f"{loc('RESULTS.md', a, a + 1)}; "
        f"{loc('results/raw/2026-09-09_k_v11_appendixB_check.txt', b)}",
        "log-only", "the local snapshot dir and refs/main carry the same id "
        "(1b)")

    # 1b local snapshot
    w("### 1b. From the local Hugging Face snapshot (not a repository file)")
    w("")
    snap = args.hf_snapshot
    refs_main = None
    if snap is None:
        rp = os.path.join(HF_REPO_DIR, "refs", "main")
        if os.path.exists(rp):
            refs_main = open(rp).read().strip()
            snap = os.path.join(HF_REPO_DIR, "snapshots", refs_main)
    quant_ok = snap is not None and os.path.exists(os.path.join(snap, "config.json"))
    qsum = {}
    if not quant_ok:
        w("Snapshot not local: section not run.")
        fig("bits / group size / mode", "not run", "local HF snapshot",
            "not found", "snapshot absent on this machine")
    else:
        cfgp = os.path.join(snap, "config.json")
        cfg = json.load(open(cfgp))
        tc = cfg.get("text_config", {})
        w(f"- Snapshot: `{tilde(snap)}` (refs/main = `{refs_main}`); "
          f"config.json sha256 `{sha256_file(cfgp)}`.")
        w(f"- config.json `quantization` = {json.dumps(cfg.get('quantization'))}; "
          f"`quantization_config` = {json.dumps(cfg.get('quantization_config'))}; "
          f"`text_config.dtype` = {tc.get('dtype')!r}; hidden_size "
          f"{tc.get('hidden_size')}; num_hidden_layers {tc.get('num_hidden_layers')}; "
          f"layer_types {dict((t, tc.get('layer_types', []).count(t)) for t in sorted(set(tc.get('layer_types', []))))}; "
          f"vocab_size {tc.get('vocab_size')}; tie_word_embeddings "
          f"{cfg.get('tie_word_embeddings')}.  [computed-new]")
        # safetensors headers
        hdr = {}
        total_bytes = 0
        shards = sorted(glob.glob(os.path.join(snap, "model-*.safetensors")))
        for f in shards:
            total_bytes += os.path.getsize(os.path.realpath(f))
            with open(f, "rb") as fh:
                n = struct.unpack("<Q", fh.read(8))[0]
                h = json.loads(fh.read(n))
            h.pop("__metadata__", None)
            hdr.update(h)
        groups: dict = {}
        for k, v in hdr.items():
            m = re.match(r"(.*)\.(weight|scales|biases|bias)$", k)
            base, part = (m.group(1), m.group(2)) if m else (k, "_param")
            groups.setdefault(base, {})[part] = v
        cls: dict = {}
        prod_ok, prod_bad = 0, []
        bits = cfg["quantization"]["bits"]
        gsz = cfg["quantization"]["group_size"]
        for name, parts in groups.items():
            gen = re.sub(r"\.\d+\.", ".N.", name)
            qz = "scales" in parts
            wd = (parts.get("weight") or parts.get("_param"))["dtype"]
            key = (gen, qz, wd)
            cls[key] = cls.get(key, 0) + 1
            if qz:
                wc = parts["weight"]["shape"][-1]
                sc = parts["scales"]["shape"][-1]
                # packed uint32 columns hold 32/bits weights; one scale per group
                if wc * (32 // bits) == sc * gsz:
                    prod_ok += 1
                else:
                    prod_bad.append(name)
        sc_dt = sorted({v["dtype"] for k, v in hdr.items() if k.endswith(".scales")})
        bi_dt = sorted({v["dtype"] for k, v in hdr.items() if k.endswith(".biases")})
        nq = sum(c for (g, qz, d), c in cls.items() if qz)
        w(f"- safetensors headers of {len(shards)} shards ({total_bytes / 1e9:.2f} GB on disk), "
          f"{len(hdr)} tensors, {len(groups)} parameter groups. Quantized "
          f"groups (a `.scales` companion present): {nq}; scales dtype {sc_dt}, "
          f"biases dtype {bi_dt}; packed-width check `weight_cols x (32/{bits}) == "
          f"scales_cols x {gsz}` holds for {prod_ok}/{nq} (fails: {prod_bad}).  [computed-new]")
        emb = groups["language_model.model.embed_tokens"]
        lmh = groups["language_model.lm_head"]
        w(f"- Spot check against hidden_size {tc.get('hidden_size')}: embed_tokens "
          f"weight {emb['weight']['dtype']} {emb['weight']['shape']}, scales "
          f"{emb['scales']['shape']}; lm_head weight {lmh['weight']['dtype']} "
          f"{lmh['weight']['shape']}, scales {lmh['scales']['shape']} -> "
          f"{tc.get('hidden_size')} x {bits}/32 = {tc.get('hidden_size') * bits // 32} packed "
          f"columns and {tc.get('hidden_size')}/{gsz} = {tc.get('hidden_size') // gsz} groups "
          "per row.  [computed-new]")
        w("")
        w("| parameter group (layer index -> N) | count | quantized | stored dtype |")
        w("|---|---|---|---|")
        for (g, qz, d), c in sorted(cls.items(), key=lambda t: (not t[0][1], t[0][0])):
            w(f"| `{g}` | {c} | {'yes' if qz else 'no'} | {d} |")
        w("")
        qnames = sorted({g for (g, qz, d) in cls if qz})
        uq_lm = sorted({g for (g, qz, d) in cls if not qz and g.startswith("language_model")})
        uq_vis = sum(c for (g, qz, d), c in cls.items() if not qz and g.startswith("vision_tower"))
        qsum = dict(bits=bits, group_size=gsz, mode=cfg["quantization"].get("mode"),
                    n_linear=tc.get("layer_types", []).count("linear_attention"),
                    n_quantized=nq, scales_dtype=sc_dt, biases_dtype=bi_dt,
                    quantized=qnames, unquantized_lm=uq_lm, vision_unquantized=uq_vis)
        w(f"Reading: {nq} weight matrices are {bits}-bit affine, group size {gsz}, "
          f"each with a {sc_dt[0]} scale and {bi_dt[0]} bias per group: every linear "
          "projection of the language model (Gated DeltaNet in_proj_qkv/z/a/b and "
          "out_proj; attention q/k/v/o_proj; MLP gate/up/down_proj), the token "
          "embedding and the LM head (untied). Left in bf16: every RMSNorm "
          "(input/post-attention, final, q_norm/k_norm, the DeltaNet output norm), "
          "the DeltaNet depthwise conv1d, `A_log` and `dt_bias`, and the vision tower "
          f"({uq_vis} groups; not used by any text-only experiment).")
        w("")
        fig("bits", str(bits), f"{tilde(cfgp)}:quantization.bits", "computed-new",
            "local HF snapshot c000ac2c; the record carries only '4-bit'")
        fig("group size", str(gsz), f"{tilde(cfgp)}:quantization.group_size; "
            "safetensors shape check", "computed-new",
            f"packed-width check {prod_ok}/{nq}")
        fig("mode", str(cfg["quantization"].get("mode")),
            f"{tilde(cfgp)}:quantization.mode", "computed-new")
        fig("which tensors", f"{nq} quantized (all LM linear projections + "
            "embed_tokens + lm_head); norms, conv1d, A_log, dt_bias, vision tower "
            "bf16", "safetensors headers (.scales companions)", "computed-new")
        fig("scale/bias dtype", f"scales {sc_dt}, biases {bi_dt}",
            "safetensors headers", "computed-new")
        fig("48 linear-attention (Gated DeltaNet) layers, of 64 (local config)",
            f"{qsum['n_linear']} of {tc.get('num_hidden_layers')}",
            f"{tilde(cfgp)}:text_config.layer_types", "computed-new",
            ("agrees with" if f"the other {qsum['n_linear']} are Gated DeltaNet"
             in text_span("RESULTS.md", a_arch, a_arch + 6) else "DIFFERS from")
            + f" the record row ({loc('RESULTS.md', a_arch, a_arch + 6)})")
        clause_map.append(("affine 4-bit, group 64, bf16 scale+bias; which tensors",
                           "section 1b (local snapshot c000ac2c; computed-new)"))

    # -------------------------------------------------------- 2. the patch
    w("## 2. The patch: what it changes and where it lives")
    w("")
    w("### 2a. What the record says (log-only)")
    w("")
    P = "archive/RESULTS-cycle1-2.md"
    a = find(P, "Model: `mlx-community/Qwen3.6-27B-4bit` via `jlens-qwen36` (MLX port)")
    w(f"- {loc(P, a, a + 4)}: \"{q(text_span(P, a, a + 4), 500)}\"")
    a2 = find(P, "Cloned `WeZZard/jlens-qwen36` @ `d788bc3`")
    w(f"- {loc(P, a2, a2 + 1)}: \"{q(text_span(P, a2, a2 + 1))}\"")
    clause_map.append(("port = WeZZard/jlens-qwen36 at d788bc3; gitignored clone",
                       f"{loc(P, a, a + 4)}; {loc(P, a2, a2 + 1)}; "
                       "N12-licenses raw §2c (origin, Apache-2.0); computed-new: the clone's "
                       ".git/HEAD and origin/main, and the five patch files byte-identical to the "
                       "upstream blobs, i.e. not the lab's code (section 2d)"))
    fig("port commit d788bc3 (record)", "WeZZard/jlens-qwen36 @ d788bc3 (2026-07-10), cloned 2026-07-16",
        loc(P, a2, a2 + 1), "log-only", "see the computed-new row (2d)")
    a3 = find(P, "New/modified files in `jlens-qwen36` (local patches, not upstream):")
    w(f"- {loc(P, a3, a3 + 7)}: \"{q(text_span(P, a3, a3 + 7), 800)}\"")
    clause_map.append(("our own edits: version pin, ablate_topk fix, added modules/scripts",
                       f"{loc(P, a3, a3 + 7)}; section 2f (clone, context)"))
    a4 = find(P, "training works on the custom-patched 27B-4bit + GDN-ops-fallback model.")
    a5 = find(P, "gradients flow through the patched GDN and LoRA-wrapped linears via the")
    w(f"- {loc(P, a4 - 1, a4)}: \"{q(text_span(P, a4 - 1, a4))}\"; {loc(P, a5, a5 + 1)}: "
      f"\"{q(text_span(P, a5, a5 + 1))}\"")
    F2 = "FINDINGS-2.md"
    a6 = find(F2, "- Anything about models other than this one (Qwen3.6-27B, 4-bit, custom")
    w(f"- {loc(F2, a6, a6 + 1)}: \"{q(text_span(F2, a6, a6 + 1))}\"")
    C1 = "archive/CLAUDE-cycle1-2.md"
    a7 = find(C1, "The custom Metal GDN backward kernel in this port drops the gradient paths")
    w(f"- {loc(C1, a7)}: \"{q(text_span(C1, a7, a7), 420)}\"")
    a8 = find("CLAUDE.md", "`mlx-community/Qwen3.6-27B-4bit` via `jlens-qwen36` (gitignored,")
    w(f"- {loc('CLAUDE.md', a8, a8 + 1)}: \"{q(text_span('CLAUDE.md', a8, a8 + 1))}\"")
    pp = os.path.join(REPO, PREPRINT)
    psha = sha256_file(pp) if os.path.exists(pp) else None
    if psha != PREPRINT_SHA:  # rounds 9-10: asserted in full, before anything is written
        raise SystemExit(f"refusing: `{PREPRINT}` sha256 {psha} is not the preprint of record "
                         f"{PREPRINT_SHA} (patch v7; the PI's routing of 2026-10-12)")
    if os.path.exists(pp):
        l262 = ffind(pp, "Qwen ran at 4-bit precision with a custom kernel patch") \
            if any("Qwen ran at 4-bit precision with a custom kernel patch" in x
                   for x in file_lines(pp)) else None
        if l262 is None:
            # the sentence wraps in the file; anchor on its start
            try:
                l262 = ffind(pp, "Qwen ran at")
            except LookupError:  # round 9: a finding on the patch (section 12), not a stop
                l262 = None
        txt = " ".join(file_lines(pp)[l262 - 1:l262 + 2]) if l262 else ""
        m = re.search(r"Qwen ran at.*?first external-validity step\.", " ".join(txt.split()))
        w(f"- `{PREPRINT}` (UNTRACKED; sha256 `{psha[:16]}...`; patch v7, the PI's routing of "
          f"2026-10-12, {PREPRINT_SHA[:8]}…{PREPRINT_SHA[-4:]}: "
          f"{'MATCH' if psha == PREPRINT_SHA else 'MISMATCH'} (full sha256, asserted); patch v6 "
          f"({PREPRINT_SHA_V6[:8]}…{PREPRINT_SHA_V6[-4:]}, round 9's preprint of record) is the "
          f"pre-patch copy the PI's routing of 2026-10-12 places at `{PREPRINT_V6}`, out of the "
          f"release (recorded, never required; whether it is on disk and matching: section 12a); "
          f"the block's "
          f"{PREPRINT_SHA_BLOCK_PREFIX}…{PREPRINT_SHA_BLOCK_SUFFIX} is the audited, superseded text, "
          f"archived untracked at `{PREPRINT_AUDITED}`; section 12) "
          + (f":{l262}: \"{m.group(0) if m else q(txt)}\"" if l262 else
             ": the sentence 'Qwen ran at ...' is not on the patched text (section 12)"))
    w("")
    # values-check finding 8: the one mechanical statement vs the d788bc3 code
    CGp = os.path.join(CLONE, "jlens_qwen", "custom_gdn_patch.py")
    CVp = os.path.join(CLONE, "jlens_qwen", "custom_gdn_vjp.py")
    LNp = os.path.join(CLONE, "docs", "lenses.md")
    gb_note = ""
    if os.path.exists(CGp) and os.path.exists(CVp):
        i1 = ffind(CGp, "Returns (dq, dk, dv, dg, dbeta, dstate). dg/dbeta are REAL gate")
        i2 = ffind(CGp, "q, k, v, g, beta, state, dy, return_gbeta=True")
        i3 = ffind(CVp, "return_gbeta: bool = False,")
        i4 = ffind(CVp, "if return_gbeta:", nth=1)
        gb_note = (
            f" Against the port's code (clone files, d788bc3, read as text): "
            f"`jlens-qwen36/jlens_qwen/custom_gdn_patch.py:{i1}-{i1 + 1}`: "
            f"\"{q(' '.join(file_lines(CGp)[i1 - 1:i1 + 1]), 200)}\"; the VJP is called with "
            f"`return_gbeta=True` (`custom_gdn_patch.py:{i2}`), a parameter of "
            f"`gdn_kernel_vjp` (`custom_gdn_vjp.py:{i3}`, branch at :{i4}).")
        if os.path.exists(LNp):
            i5 = ffind(LNp, "fitted with the corrected chain indexing and the GDN decay-gate (g/β) paths.")
            gb_note += (f" The upstream docs say the bundled lens was fitted with those paths "
                        f"(`jlens-qwen36/docs/lenses.md:{i5 - 1}-{i5}`).")
        gb_note += (" So the record's g/β caveat (archive/CLAUDE-cycle1-2.md above) is stale "
                    "against the code the lab ran (static reading; no figure here depends on it).")
    w("What the record says about the patch is its name (\"custom GDN patch\", "
      "\"custom-patched\", \"GDN-ops-fallback\"), the lab's own local edits (none of "
      "which is a kernel, 2f), and one mechanical statement: the cycle-1 limitation that "
      "the port's Metal backward drops the g/β gradient paths (archive/CLAUDE-cycle1-2.md "
      "above). It never describes how the patch routes the forward pass." + gb_note +
      " The preprint's \"custom kernel patch\" is the port's Gated DeltaNet patching (2d), "
      "which the lab did not write.")
    w("")

    # 2b tracked adapter
    A = "valence_core/adapters/qwen_mlx.py"
    w("### 2b. What the tracked adapter calls")
    w("")
    for needle, span_ in [
        ("`jlens-qwen36/` is a gitignored external clone", 1),
        ("it adds no arithmetic. Vanilla forwards delegate to `MLXLensModel.forward`;", 2),
        ('self._patch_gdn = importlib.import_module("jlens_qwen.patch_gdn")', 0),
        ("# Ops kernel, not fused", 2),
        ('"dtype": "4bit-quantized (MLX)",', 0),
        ('"gdn_inference_mode": "ops (fused disabled)",', 0),
        ("session = self._cond.SteeredStreamSession(self._model, {})", 0),
    ]:
        x = find(A, needle)
        t_ = q(text_span(A, x, x + span_), 300)
        w(f"- {loc(A, x, x + span_)}: " + (f"\"{t_}\"" if "`" in t_ else f"`{t_}`"))
    xg = find(A, '"gdn_inference_mode": "ops (fused disabled)",')
    w("")
    w(f"The provenance field `gdn_inference_mode` is a string literal in "
      f"`provenance()` ({loc(A, xg)}), written beside the call "
      f"`set_inference_mode(False)` ({loc(A, find(A, 'self._patch_gdn.set_inference_mode(False)'))}); "
      "it is not read back from the patch's state.")
    w("")

    # 2c committed provenance fields
    w("### 2c. The provenance field across committed artifacts (reproduced)")
    w("")
    files = sorted(set(l.split(":", 1)[1].rsplit(":", 1)[0]
                       for l in git("grep", "-c", "gdn_inference_mode", PIN,
                                    "--", "data").splitlines()))
    vals: dict = {}

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "gdn_inference_mode":
                    yield v
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)

    nparsed = 0
    for f in files:
        try:
            d = json.loads(show(f))
        except Exception:
            continue
        nparsed += 1
        for v in walk(d):
            vals[v] = vals.get(v, 0) + 1
    w(f"- {len(files)} committed `data/` files contain the key (text search), "
      f"{nparsed} parse as JSON; values of every `gdn_inference_mode` field in them: {vals}.")
    w("")
    fig("gdn_inference_mode", f"{vals}", f"{nparsed} committed data/*.json "
        "(recursive key gdn_inference_mode)", "reproduced",
        "a literal written by the adapter (2b); on a static reading of the port "
        "it describes the cached path's routing only (2e, flag F1)")

    # 2d the clone (context)
    w("### 2d. Where the patch lives: the clone, read as files (context, not record)")
    w("")
    clone_ok = os.path.isdir(os.path.join(CLONE, ".git"))
    upstream_same: dict = {}
    if not clone_ok:
        w("Clone absent: not run.")
    else:
        head_ref = open(os.path.join(CLONE, ".git", "HEAD")).read().strip()
        main_sha = None
        if head_ref.startswith("ref: "):
            rp = os.path.join(CLONE, ".git", head_ref[5:])
            if os.path.exists(rp):
                main_sha = open(rp).read().strip()
        origin_main = None
        prp = os.path.join(CLONE, ".git", "packed-refs")
        if os.path.exists(prp):
            for ln in open(prp):
                if ln.strip().endswith("refs/remotes/origin/main"):
                    origin_main = ln.split()[0]
        actions = []
        lgp = os.path.join(CLONE, ".git", "logs", "HEAD")
        if os.path.exists(lgp):
            for ln in open(lgp, errors="replace"):
                parts = ln.rstrip("\n").split("\t", 1)
                old_new = parts[0].split()[:2]
                msg = parts[1] if len(parts) > 1 else ""
                kind = msg.split(":", 1)[0]
                if kind == "clone":
                    detail = msg   # 'clone: from <public upstream URL>'
                elif kind == "commit":
                    detail = "commit: <message omitted>"
                else:
                    detail = msg
                actions.append(f"{old_new[0][:7]} -> {old_new[1][:7]}  {detail}")
        w(f"- `.git/HEAD` = `{head_ref}` -> `{main_sha}`; packed-refs "
          f"`refs/remotes/origin/main` = `{origin_main}`; equal: {main_sha == origin_main}.")
        fig("port commit d788bc3 (clone)", f"HEAD {main_sha}; origin/main {origin_main}; "
            f"equal: {main_sha == origin_main}",
            "jlens-qwen36/.git/HEAD, .git/refs, .git/packed-refs (read as files)", "computed-new",
            "starts with the record's d788bc3: "
            f"{bool(main_sha) and main_sha.startswith('d788bc3')}")
        w(f"- `.git/logs/HEAD` (read as a file; committer fields omitted): "
          + "; ".join(f"`{x}`" for x in actions)
          + ". So the clone's HEAD is the upstream commit; the lab's changes are "
            "uncommitted working-tree edits and untracked files (the one local "
            "commit in the reflog was reset away).")

        # index + pack
        def read_index(p):
            d = open(p, "rb").read()
            assert d[:4] == b"DIRC"
            ver, n = struct.unpack(">II", d[4:12])
            if ver not in (2, 3):
                raise RuntimeError(f"index v{ver} unsupported")
            off, res = 12, {}
            for _ in range(n):
                st = off
                sha = d[off + 40:off + 60].hex()
                fl = struct.unpack(">H", d[off + 60:off + 62])[0]
                o2 = off + 62 + (2 if (ver >= 3 and fl & 0x4000) else 0)
                e = d.index(b"\0", o2)
                res[d[o2:e].decode()] = sha
                off = st + ((e - st + 8) & ~7)
            return ver, n, res

        def pack_objects(c):
            s = set()
            for ip in glob.glob(os.path.join(c, ".git", "objects", "pack", "*.idx")):
                d = open(ip, "rb").read()
                assert d[:4] == b"\xfftOc"
                n = struct.unpack(">I", d[8 + 255 * 4:8 + 256 * 4])[0]
                base = 8 + 256 * 4
                for i in range(n):
                    s.add(d[base + 20 * i:base + 20 * i + 20].hex())
            return s

        iver, inum, index = read_index(os.path.join(CLONE, ".git", "index"))
        packed = pack_objects(CLONE)
        w(f"- `.git/index` v{iver}, {inum} entries (after the reflog's reset it "
          f"lists the upstream tree); pack objects (fetched at clone): {len(packed)}.")
        w("")
        w("| file (clone) | sha256 | git blob sha1 | = index entry (upstream d788bc3) | in clone pack | mtime |")
        w("|---|---|---|---|---|---|")
        patch_files = ["jlens_qwen/patch_gdn.py", "jlens_qwen/custom_gdn_patch.py",
                       "jlens_qwen/custom_gdn_vjp.py", "jlens_qwen/gdn_backward.py",
                       "jlens_qwen/model.py"]
        for f in patch_files:
            p = os.path.join(CLONE, f)
            b1 = git_blob_sha1(p)
            same = index.get(f) == b1
            upstream_same[f] = same and (b1 in packed)
            w(f"| `jlens-qwen36/{f}` | `{sha256_file(p)[:16]}...` | `{b1[:12]}` | "
              f"{same} | {b1 in packed} | "
              f"{time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(p)))} |")
        w("")
        lic = file_lines(os.path.join(CLONE, "LICENSE"))
        w(f"- `jlens-qwen36/LICENSE` first line: \"{lic[0].strip()}\" (license and "
          "upstream origin are N12-licenses' item: "
          "`results/raw/2026-10-08_note-N12-licenses.md` §2c).")
        rd = os.path.join(CLONE, "README.md")
        r1 = ffind(rd, "The hard part is the 48 Gated DeltaNet (GDN) linear-attention layers")
        w(f"- Upstream README (clone file, :{r1}-{r1 + 4}): \"{q(' '.join(file_lines(rd)[r1 - 1:r1 + 4]), 420)}\"")
        w("")
        allup = all(upstream_same.values())
        w(f"Reading: the five files that implement the patch are byte-identical to the "
          f"upstream commit's blobs ({'all five' if allup else 'NOT all'}: equal to the "
          "index entry and present in the clone's pack). The patch is the port's, "
          "shipped upstream; the lab did not modify it.")
        w("")
        fig("where the patch lives", "jlens-qwen36/jlens_qwen/{patch_gdn,custom_gdn_patch,"
            "custom_gdn_vjp,gdn_backward}.py, applied in model.py MLXLensModel.__init__; "
            f"byte-identical to upstream d788bc3: {allup}",
            "clone files vs clone .git/index + pack (read as files)", "computed-new",
            "the README's patch-mechanics clauses rest on this (checkable against public "
            "upstream d788bc3); the lab's own clone edits (2f) are not in this repository")

        # ------------------------------------------------- 2e dispatch reading
        w("### 2e. What the patch changes: a static reading of the code (not executed)")
        w("")
        M = os.path.join(CLONE, "jlens_qwen", "model.py")
        PG = os.path.join(CLONE, "jlens_qwen", "patch_gdn.py")
        CG = os.path.join(CLONE, "jlens_qwen", "custom_gdn_patch.py")
        CD = os.path.join(CLONE, "jlens_qwen", "conditioning.py")
        site = glob.glob(os.path.join(CLONE, ".venv", "lib", "python3*", "site-packages"))
        site = site[0] if site else None
        GD = os.path.join(site, "mlx_lm", "models", "gated_delta.py") if site else None
        Q35 = os.path.join(site, "mlx_lm", "models", "qwen3_5.py") if site else None
        mlxlm_ver = None
        if site:
            for dist in glob.glob(os.path.join(site, "mlx_lm-*.dist-info", "METADATA")):
                for ln in open(dist):
                    if ln.startswith("Version:"):
                        mlxlm_ver = ln.split(":", 1)[1].strip()
                        break

        def cite(p, needle, nth=1, span_=0, label=None, exact=False):
            i = ffind(p, needle, nth=nth, exact=exact)
            t = " / ".join(x.strip() for x in file_lines(p)[i - 1:i + span_])
            lab = label or (rel_clone(p) if p.startswith(REPO) else tilde(p))
            return f"`{lab}:{i}{'-' + str(i + span_) if span_ else ''}`: `{q(t, 260)}`"

        rows = [
            ("load applies both patches",
             cite(M, "patch_gdn()", exact=True) + "; "
             + cite(M, "try:", exact=True, span_=4)),
            ("patch 1 (patch_gdn): the GDN recurrence dispatch is replaced",
             cite(PG, "_gdn_mod.gated_delta_update = _patched_gated_delta_update", span_=2)),
            ("... it uses the fused kernel only when inference mode is on, else the ops loop",
             cite(PG, "if _INFERENCE_KERNEL and use_kernel:", span_=4) + "; "
             + cite(PG, "return gated_delta_ops(q, k, v, g, beta, state, mask)")),
            ("patch 2 (patch_gdn): a gradient-checkpointing wrapper on the layer call "
             "(SHADOWED once patch 3 is in place: see the next three rows)",
             cite(PG, "return mx.checkpoint(body)(inputs)") + "; installed as "
             + cite(PG, "GatedDeltaNet.__call__ = _checkpointed_call")),
            ("... the wrapper returns the stock call, without checkpointing, whenever a cache is passed",
             cite(PG, "if cache is not None:", span_=2)),
            ("patch 3 (custom_gdn_patch): the layer call is replaced again, capturing the "
             "wrapper as `original_call`",
             cite(CG, "original_call = GatedDeltaNet.__call__") + "; "
             + cite(CG, "GatedDeltaNet.__call__ = _new_call")),
            ("... with a KV/recurrent cache it defers to the previous call",
             cite(CG, "if cache is not None:", span_=2)),
            ("... without a cache it runs its own forward through a custom function",
             cite(CG, "out = _gdn_custom_forward(q, k, v, g, beta, None)")),
            ("... whose forward is mlx-lm's stock kernel and whose VJP is the port's Metal kernel",
             cite(CG, "y, _ = gated_delta_kernel(q, k, v, g, beta, state, mask=None)") + "; "
             + cite(CG, "dq, dk, dv, dg, dbeta = gdn_kernel_vjp(")),
        ]
        if GD and os.path.exists(GD):
            rows += [
                (f"mlx-lm {mlxlm_ver}: `gated_delta_kernel` is the fused Metal kernel",
                 cite(GD, "return mx.fast.metal_kernel(", label="venv mlx_lm/models/gated_delta.py")
                 + "; " + cite(GD, "def gated_delta_kernel(", label="venv mlx_lm/models/gated_delta.py")),
                (f"mlx-lm {mlxlm_ver}: stock dispatch (kernel on GPU unless training)",
                 cite(GD, "if not use_kernel or mx.default_device() != mx.gpu", span_=2,
                      label="venv mlx_lm/models/gated_delta.py")),
            ]
        if Q35 and os.path.exists(Q35):
            rows += [
                ("each decoder layer calls the (patched) GDN with its cache argument",
                 cite(Q35, "r = self.linear_attn(self.input_layernorm(x), mask, cache)",
                      label="venv mlx_lm/models/qwen3_5.py")),
                ("the stock GDN call reaches the (patched) dispatch",
                 cite(Q35, "out, state = gated_delta_update(", label="venv mlx_lm/models/qwen3_5.py")
                 + "; " + cite(Q35, "use_kernel=not self.training,", label="venv mlx_lm/models/qwen3_5.py")),
            ]
        rows += [
            ("uncached forward passes cache=None to every layer",
             cite(M, "hidden = layer(hidden, mask=mask, cache=None)")),
            ("the cached stream turns the fused kernel on ...",
             cite(M, "set_inference_mode(True)")),
            ("... and the lab's steered stream turns it back off (default)",
             cite(CD, "if not use_fused:", span_=1)),
            ("the patch-failure branch prints a warning",
             cite(M, 'print(f"Warning: custom GDN VJP patch failed')),
        ]
        w("| step | code (file:line, read as text) |")
        w("|---|---|")
        for s_, c_ in rows:
            w(f"| {cell(s_)} | {cell(c_)} |")
        w("")
        warn_hits = git("grep", "-c", "custom GDN VJP patch failed", PIN, "--", ".").strip() \
            if subprocess.run(["git", "-C", REPO, "grep", "-q", "custom GDN VJP patch failed",
                               PIN, "--", "."]).returncode == 0 else "0 files"
        w(f"- The warning string in any committed file at {PIN} (`git grep`): {warn_hits}.")
        w(f"- Model weights are never touched by any of these patches (they rebind "
          "`gated_delta_update` and `GatedDeltaNet.__call__` only); quantization is "
          "whatever mlx-lm loaded.")
        w("")
        w("**What this reading says (static; nothing was imported or run):** the port "
          "rebinds two things in mlx-lm when the model loads: the Gated DeltaNet "
          "recurrence dispatch (`gated_delta_update`: the fused Metal kernel when "
          "`set_inference_mode(True)`, otherwise the pure-ops sequential loop "
          "`gated_delta_ops`) and the layer call (`GatedDeltaNet.__call__`: "
          "`patch_gdn()` installs a gradient-checkpointing wrapper, then "
          "`patch_gdn_custom()` replaces it with a re-implemented forward wrapped in "
          "`mx.custom_function` with a custom Metal backward). Its purpose is "
          "differentiability for Jacobian-lens fitting (upstream README above). "
          "Followed through, the routing is: **with a cache** (the O(T) streams: "
          "`StreamSession`, the lab's `SteeredStreamSession`, the adapter's "
          "`cached=True` generation) `_new_call` hands the call to `original_call`, "
          "which is the checkpointing wrapper; because a cache is present the wrapper "
          "returns the stock call without checkpointing, and the stock call reaches the "
          "patched dispatch, so `set_inference_mode(False)` -- what the adapter and the "
          "lab's scripts set -- selects the ops loop; **without a cache** (every "
          "uncached forward: choice reads, uncached positional generation, extraction "
          "and probe readouts, and LoRA training, whose loss is computed through "
          "`MLXLensModel.forward`) the call runs `_gdn_custom_forward`, whose forward is "
          "mlx-lm's stock fused Metal kernel `gated_delta_kernel`, whatever the "
          "inference-mode flag says, and never calls `original_call`. So on neither "
          "route does the checkpointing wrapper reach `mx.checkpoint` -- unless "
          "`patch_gdn_custom()` raised at load, which prints a warning that appears in "
          "no committed raw (above), and in which case every uncached forward would be "
          "checkpointed and, with the inference mode off, run the ops loop.")
        w("")
        # LoRA training's route (values-check finding 9): clone scripts, read as text
        TRc = os.path.join(CLONE, "scripts", "c1_train_adapter.py")
        TRd = os.path.join(CLONE, "scripts", "d_train_distill.py")
        lora_txt = ""
        if os.path.exists(TRc) and os.path.exists(TRd):
            c1t_ = find(P, "`c1_train_adapter.py` / `c1_gate.py` (all local, gitignored per convention).")
            lora_txt = (
                " The same holds for LoRA training, on a static reading of the training "
                "scripts as they now stand in the clone: the c1 protocol's trainer "
                f"(`c1_train_adapter.py`, named at {loc(P, c1t_ - 3, c1t_)}; floor 2's c1r3 "
                "adapters came from that protocol) and the clone's `d_train_distill.py` "
                "(which no record line names) compute their loss through "
                "`MLXLensModel.forward`, which passes cache=None ("
                + cite(TRc, "set_inference_mode(False)  # training must use the differentiable ops path")
                + "; " + cite(TRc, "final, _ = model.forward(ids)") + "; "
                + cite(TRd, "set_inference_mode(False)") + "; "
                + cite(TRd, "final, acts = mdl.forward(ids, capture_layers=TARGET_LAYERS)")
                + "), so the GDN forward in training is the fused kernel and the backward "
                "the port's Metal VJP, not 'the differentiable ops path' the c1 script's "
                "comment names. The record's own spike entry already says the gradients "
                f"flow 'via the custom forward' ({loc(P, a5, a5 + 1)}).")
        f1_idx = len(flags)
        flags.append(
            "F1 (labelling; no figure moves). On a static reading of the port's code "
            "(byte-identical to upstream d788bc3; mlx-lm "
            f"{mlxlm_ver} as in the record's provenance), the uncached full-sequence "
            "forward computes the Gated DeltaNet recurrence with mlx-lm's stock fused "
            "Metal kernel inside the port's custom function; `set_inference_mode(False)` "
            "routes only the CACHED path to the ops loop." + lora_txt + " The record labels the "
            "uncached path the 'validated ops path' / 'ops-fallback kernel' "
            f"(results/raw/2026-08-06_c1_smoke.txt@{PIN}:"
            f"{find('results/raw/2026-08-06_c1_smoke.txt', 'Equivalence gate (cached fused vs validated ops path')}; "
            f"{loc('archive/RESULTS-cycles3-4.md', find('archive/RESULTS-cycles3-4.md', 'forwards only, ops-fallback kernel (rule 2 untouched by'))}; "
            f"{loc('RESULTS.md', find('RESULTS.md', '`mlx-community/Qwen3.6-27B-4bit`, 4-bit, MLX backend, GDN ops kernel'))}), "
            "and every artifact's `gdn_inference_mode: ops (fused disabled)` is a "
            "literal. If the reading holds, the label describes the cached path only, "
            "and the uncached path uses the same fused kernel stock mlx-lm uses. No "
            "figure moves: each was computed on whatever path actually ran, and the "
            "label enters no computation. What changes is wording: 'ops kernel' for "
            "uncached reads, and the record's attribution of the near-tie floor to "
            "'kernel-level' noise (if the reading holds, in c1 smoke 1 both paths ran "
            "the fused kernel and still diverged, so the difference is path-level: "
            "cached vs full-sequence computation; section 3's OLMo evidence is consistent "
            "with that). Not run here (no mlx import while another "
            "session holds the laptop): a dispatch check in the venv (import "
            "`jlens_qwen.model`, apply the two patches without loading weights, "
            "print `GatedDeltaNet.__call__.__name__`), and optionally one synthetic "
            "GDN layer through both routes. The README paragraph (section 6) avoids the "
            "contested clause; an optional sentence follows these notes.")

        # ------------------------------------------------- 2f lab edits
        w("### 2f. The lab's own edits inside the clone (context)")
        w("")
        # Domain (values-check finding 10): every regular file in the clone's working
        # tree, walked recursively, excluding the directories .git, .venv and the
        # Python/tool caches; symlinks skipped. Compared with the clone's index.
        SKIP_D = {".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
        modified, added = [], []
        for root_, dirs_, files_ in os.walk(CLONE):
            dirs_[:] = sorted(x for x in dirs_ if x not in SKIP_D)
            for fn in sorted(files_):
                p = os.path.join(root_, fn)
                if os.path.islink(p) or not os.path.isfile(p):
                    continue
                rel = os.path.relpath(p, CLONE)
                b1 = git_blob_sha1(p)
                if rel not in index:
                    added.append(rel)
                elif index[rel] != b1:
                    modified.append(rel)
        idx_missing = sorted(x for x in index if not os.path.exists(os.path.join(CLONE, x)))
        pat = re.compile(r"metal_kernel|custom_function|mx\.fast\.|mx\.checkpoint|"
                         r"\.__call__\s*=|gated_delta_\w*\s*\(")
        pat_mode = re.compile(r"set_inference_mode\(")
        kernel_hits, mode_hits = [], {}
        py_scanned = [r for r in modified + added if r.endswith(".py")]
        for rel in py_scanned:
            for k_, ln in enumerate(file_lines(os.path.join(CLONE, rel)), start=1):
                if pat.search(ln):
                    kernel_hits.append(f"{rel}:{k_}")
                if pat_mode.search(ln) and "import" not in ln:
                    mode_hits[rel] = mode_hits.get(rel, 0) + 1
        top_of = lambda r: r.split("/")[0] if "/" in r else "(root)"  # noqa: E731
        by_area: dict = {}
        for r in added:
            by_area[top_of(r)] = by_area.get(top_of(r), 0) + 1
        added_py = [r for r in added if r.endswith(".py")]
        py_area: dict = {}
        for r in added_py:
            py_area[top_of(r)] = py_area.get(top_of(r), 0) + 1
        data_ext: dict = {}
        for r in added:
            if r.startswith("data/"):
                e_ = os.path.splitext(r)[1] or "(none)"
                data_ext[e_] = data_ext.get(e_, 0) + 1
        other_np = sorted(r for r in added if not r.endswith(".py") and not r.startswith("data/"))
        w("- Domain: every regular file of the clone's working tree, walked recursively, "
          "excluding the directories `.git`, `.venv`, `__pycache__` and tool caches "
          "(symlinks skipped), each compared by git blob sha1 with the clone's index "
          f"(the upstream tree, {inum} entries; index entries absent from the working "
          f"tree: {idx_missing if idx_missing else 'none'}).")
        w(f"- Modified upstream files (blob differs from the index): {modified}.")
        w(f"- Files absent from the index: {len(added)}, by top-level area {by_area}. Of "
          f"them, Python files: {len(added_py)} ({py_area}) -- in `jlens_qwen/`: "
          f"{[x for x in added_py if x.startswith('jlens_qwen/')]}; under `data/`: "
          f"{by_area.get('data', 0)} lab data files by extension {data_ext} (not code); other "
          f"non-Python files outside `data/`: {other_np}.")
        w(f"- Scanned for kernel definition, rebinding or calls: the {len(py_scanned)} Python "
          f"files among the modified and added ones, pattern `{pat.pattern}`: "
          f"{kernel_hits if kernel_hits else 'no line matches'}.")
        w(f"- Lines mentioning `set_inference_mode(` outside import lines (mode-selection "
          f"calls, plus a few docstring mentions), per file: {mode_hits}.")
        w("")
        fig("lab edits to the clone", f"modified {modified}; {len(added_py)} added Python files "
            f"({py_area}); {by_area.get('data', 0)} added data files under data/ (not code); "
            f"kernel-pattern lines 0 of {len(py_scanned)} Python files scanned"
            if not kernel_hits else f"kernel-pattern hits {kernel_hits}",
            "clone working tree (recursive; .git/.venv/caches excluded) vs clone .git/index",
            "computed-new", f"record list: {loc(P, a3, a3 + 7)}")

    # ---------------------------------------------- 3. floor 1: near ties
    w("## 3. Floor 1: near-tie argmax flips under high displacement")
    w("")
    S = "results/raw/2026-08-06_c1_smoke.txt"
    sl = lines_of(S)
    d0 = find(S, "directions: L48 ranks -23/-25 alpha=102.39")
    assert "frac=1.0 (α = R = 102.39)" in show(P), "floor-1 dose as quoted in section 3"
    g1a = find(S, "Equivalence gate (cached fused vs validated ops path", nth=1)
    g1b = find(S, "Equivalence gate (cached fused vs validated ops path", nth=2)
    t1b = find(S, "=== c1 SMOKE 1b")
    w(f"- {loc(S, d0)}: `{sl[d0 - 1].strip()}`")
    smoke = []
    for lab, g in (("smoke 1 (cached path, fused kernel)", g1a),
                   ("smoke 1b (cached path, 'cached-OPS variant')", g1b)):
        for k_ in (1, 2):
            ln = sl[g - 1 + k_]
            m = re.search(r"state (\w+): (\w+)\s+ref=\[([^\]]*)\] cached=\[([^\]]*)\]", ln)
            ref = [int(x) for x in m.group(3).split(",")]
            cac = [int(x) for x in m.group(4).split(",")]
            diff = [i for i, (x, y) in enumerate(zip(ref, cac)) if x != y]
            smoke.append(dict(run=lab, state=m.group(1), verdict=m.group(2),
                              n=len(ref), first=(diff[0] if diff else None),
                              ndiff=len(diff), line=g + k_))
    w(f"- {loc(S, t1b)}: `{sl[t1b - 1].strip()}` (its gate line still prints "
      "\"cached fused\"; the record states both kernels were tried, below)")
    w("")
    w("| run | state | verdict | greedy tokens | first differing index (0-based) | positions differing | raw line |")
    w("|---|---|---|---|---|---|---|")
    for r in smoke:
        w(f"| {r['run']} | {r['state']} | {r['verdict']} | {r['n']} | {r['first']} | "
          f"{r['ndiff']}/{r['n']} | {loc(S, r['line'])} |")
    w("")
    hi = [r for r in smoke if r["state"] == "hi"]
    lo = [r for r in smoke if r["state"] == "lo"]
    fig("near-tie argmax flips (c1 smoke, frac 1.0, alpha 102.39 at L48)",
        f"hi: MISMATCH in both runs, first differing token index {[r['first'] for r in hi]} "
        f"of 12; lo: {[r['verdict'] for r in lo]} 12/12",
        f"{loc(S, g1a, g1a + 2)}; {loc(S, g1b, g1b + 2)}", "log-only",
        "parsed from a committed text raw (no JSON artifact)")
    a = find(P, "frac=1.0 (α = R = 102.39)")
    w(f"- {loc(P, a - 1, a)}: \"{q(text_span(P, a - 1, a))}\"")
    a = find(P, "The equivalence gate works and caught a real divergence:")
    w(f"- {loc(P, a, a + 6)}: \"{q(text_span(P, a, a + 6), 700)}\"")
    clause_map.append(("floor 1: full-norm steering, cached vs uncached greedy, hi diverged, lo matched, either cached kernel",
                       f"{loc(S, g1a, g1a + 2)}; {loc(S, g1b, g1b + 2)}; {loc(P, a, a + 6)}"))
    a_read = a
    n_marg = sum(1 for x in sl if re.search(r"(?i)logit|margin", x))
    a = find(F2, "- **High-strain displacement sits near argmax ties.**")
    w(f"- {loc(F2, a, a + 5)}: \"{q(text_span(F2, a, a + 5), 600)}\"")
    w(f"- The near-tie account is the record's reading, not a measurement: the smoke raw "
      f"carries token ids only (lines of {S} mentioning a logit or a margin: {n_marg}).")
    clause_map.append(("the near-tie account is the record's reading (no logit margins recorded)",
                       f"{loc(P, a_read + 5, a_read + 6)}; {loc(F2, a, a + 5)}; {S} (token ids only; "
                       f"{n_marg} lines mention a logit or margin)"))
    a2 = find(F2, "Design: X = −23 (strain 2.47) / Y = −25 (strain 0.09), equal norm at L48;")
    w(f"- {loc(F2, a2)}: \"{q(text_span(F2, a2, a2))}\"")
    V2 = "archive/CLAUDE-v2-cycles3-4.md"
    a = find(V2, "2. **Use the validated O(T²) uncached generation path whenever high-norm")
    w(f"- Ledger v2 rule 2 (superseded by v3.1; quoted for its history), {loc(V2, a, a + 9)}: "
      f"\"{q(text_span(V2, a, a + 9), 900)}\"")
    av3 = find("CLAUDE.md", "2. Kernel/path/determinism gates re-validated per model, per backend,")
    w(f"- Ledger v3.1 rule 2 + annotation (operative), {loc('CLAUDE.md', av3, av3 + 5)}: "
      f"\"{q(text_span('CLAUDE.md', av3, av3 + 5), 600)}\"")
    clause_map.append(("greedy readouts under strong steering generated uncached; cached sampled "
                       "generation only behind a per-family next-token KL gate (<= 1e-3 nats); since "
                       "2026-09-05 that gate licenses first-token reads only and multi-token "
                       "generation needs its own T-step identity gate",
                       f"{loc(V2, a, a + 9)} (v2, superseded); {loc('CLAUDE.md', av3, av3 + 5)} "
                       "(v3.1 rule 2 + its 2026-09-05 annotation, operative)"))
    w("")
    w("Later evidence at the e2a dose (reproduced; cross-reference to N4(iv), which owns "
      "the cached-generation disclosure). The first-token gate PASSED -- its KLs bound "
      "the distance between the two paths' next-token distributions and are not "
      "near-tie flips; the T-step check then found sampled divergences that a passed "
      "first-token gate does not exclude. These are related to floor 1, not instances of "
      "it: floor 1 is greedy decoding at frac 1.0 (alpha 102.39); the T-step rounds are "
      "temperature-0.7 sampling at frac 0.1 / 0.2:")
    w("")
    g1 = json.loads(show("data/e2a/g1_kernel_gate.json"))
    tstep_div: list = []
    for frac in ("0.1", "0.2"):
        rows_ = g1["rows"][frac]["rows"]
        mx_ = max(max(r["kl_c_u"], r["kl_u_c"]) for r in rows_)
        w(f"- first-token gate (passed), `data/e2a/g1_kernel_gate.json` frac {frac}: "
          f"`results.max_kl` = "
          f"{g1['results'][frac]['max_kl']:.4e}, pass {g1['results'][frac]['pass']}, "
          f"bar `gate` = {g1['gate']}; {len(rows_)} rows (poles x 16 probes), each with "
          f"`kl_c_u` and `kl_u_c`; max over rows of the larger direction = {mx_:.4e} "
          f"(rows stored at 5 significant figures).")
    for f, lab in (("data/e2d/tstep_check_f010.json", "0.1"), ("data/e2d/tstep_check.json", "0.2")):
        d = json.loads(show(f))
        r_ = d["rounds"]
        nonid = [(x["session"], x["round"], x["first_divergent_position"]) for x in r_ if not x["identical"]]
        tstep_div.extend(x[2] for x in nonid)
        assert d["temp"] > 0, "T-step rounds are sampled"
        w(f"- T-step identity: cached-vs-uncached divergences at the e2a dose (sampled; related "
          f"to floor 1, not instances of it), `{f}` ({d['item']}, {d['proposal']}; "
          f"e2d-format rounds, {len({x['session'] for x in r_})} sessions x "
          f"{len({x['round'] for x in r_})} rounds, through the ported adapter "
          f"`{d['provenance']['adapter']}`; frac "
          f"{d['frac']}, L{d['layer']}, temp {d['temp']}, alpha {d['alpha']:.3f}): "
          f"{sum(x['identical'] for x in r_)}/{len(r_)} rounds token-identical cached vs "
          f"uncached; non-identical (session, round, first_divergent_position, 0-based): {nonid}.")
        fig(f"T-step identity at frac {lab}", f"{sum(x['identical'] for x in r_)}/{len(r_)}",
            f"{f}:rounds[].identical", "reproduced",
            f"sampled (temp {d['temp']}), e2d-format rounds through the ported adapter; related to "
            "floor 1, not instances of it; N4(iv) owns this disclosure")
    TS = "scripts/e2d_tstep_check.py"
    ts_k = find(TS, "for k in range(max(len(a), len(b))):")
    w(f"- `first_divergent_position` is 0-based: {loc(TS, ts_k, ts_k + 3)}: "
      f"\"{q(text_span(TS, ts_k, ts_k + 3), 200)}\"; over the {len(tstep_div)} divergent rounds "
      f"it ranges {min(tstep_div)}-{max(tstep_div)}, so token 0 agreed in every one.")
    a = find("RESULTS.md", "g1 measures the first-response-token DISTRIBUTIONS")
    w(f"- {loc('RESULTS.md', a - 1, a + 6)}: \"{q(text_span('RESULTS.md', a - 1, a + 6), 600)}\"")
    w("")
    # --- OLMo counterpart (values-check finding 2) ----------------------------
    w("The OLMo counterpart (bf16, PyTorch/CUDA, no port; reproduced from the committed "
      "cached-generation gate artifacts -- token-id identity of a multi-token cached "
      "generation vs the uncached re-forward, 14 cases per stage):")
    w("")
    w("| artifact | stage | gate field | cases diverging | of those uninjected | of those at temp 0.0 | diverging (case, temp, injected, diverge_index) |")
    w("|---|---|---|---|---|---|---|")
    olmo_cg = {}
    for f in ("data/olmo/cached_gen_v3.json", "data/olmo/cached_gen_v3b.json",
              "data/olmo/cached_gen_sft.json", "data/olmo/cached_gen_dpo.json",
              "data/olmo/cached_gen_instruct.json"):
        d = json.loads(show(f))
        rr = d["rows"]
        dv = [x for x in rr if not x["ids_identical"]]
        un = [x for x in dv if not x["injected"]]
        gr = [x for x in dv if x["temp"] == 0.0]
        olmo_cg[f] = dict(stage=d["stage"], n=len(rr), div=len(dv), un=len(un), greedy=len(gr),
                          div_idx=[x["diverge_index"] for x in dv],
                          greedy_un=sum(1 for x in dv if x["temp"] == 0.0 and not x["injected"]),
                          gate=d["gate"].split(" --")[0], dtype=d["provenance"].get("dtype"),
                          backend=d["provenance"].get("backend"))
        w(f"| `{f}` | {d['stage']} | {cell(d['gate'])} | {len(dv)}/{len(rr)} | {len(un)} | "
          f"{len(gr)} | {[(x['case'], x['temp'], x['injected'], x['diverge_index']) for x in dv]} |")
    w("")
    ocg_ = find("RESULTS.md", "CACHED-GENERATION GATE, all four stages: BASE PASSES,")
    ob_ = find("RESULTS.md", "- **B-phase sequence licensed, uncached throughout, one arc on one")
    ou_ = find("RESULTS.md", "and **generation is uncached everywhere** in the")
    ok1_ = find("RESULTS.md", "first-token distributions bit-identical, symKL **exactly 0.000e+00**")
    olc_ = find("RESULTS.md", "position bookkeeping advances one token at a time. **The licence covers")
    odv_ = find("RESULTS.md", "- **The divergences are not about injection and not about sampling.** At")
    okv_ = find("RESULTS.md", "This is KV-cache numerics, an apparatus")
    w(f"- Record: {loc('RESULTS.md', ocg_, ocg_ + 5)}: \"{q(text_span('RESULTS.md', ocg_, ocg_ + 5), 420)}\"; "
      f"{loc('RESULTS.md', odv_, odv_ + 7)}: \"{q(text_span('RESULTS.md', odv_, odv_ + 7), 600)}\"; "
      f"{loc('RESULTS.md', okv_, okv_ + 1)}: \"{q(text_span('RESULTS.md', okv_, okv_ + 1), 300)}\".  [log-only]")
    w(f"- The B-phase ran uncached: {loc('RESULTS.md', ob_, ob_ + 1)}: "
      f"\"{q(text_span('RESULTS.md', ob_, ob_ + 1), 200)}\"; {loc('RESULTS.md', ou_, ou_ + 2)}: "
      f"\"{q(text_span('RESULTS.md', ou_, ou_ + 2), 300)}\".  [log-only]")
    # --- round 2, finding 1: the OLMo first-token gate artifact (Base only) ---------
    DB = "data/olmo/determinism_base.json"
    det = json.loads(show(DB))
    ck = det["C_kernel_path"]
    det_hist = git("log", "--format=%h %ad", "--date=short", PIN, "--", DB).strip().splitlines()
    det_files = sorted(f for f in git("ls-tree", "-r", "--name-only", PIN, "--", "data/olmo").splitlines()
                       if os.path.basename(f).startswith("determinism"))
    BD = "scripts/box_determinism.py"
    bd_c = find(BD, '=== C. kernel path: cached vs uncached (rule-2 gate) ===')
    bd_e = find(BD, 'out["C_kernel_path"] = {"max_kl": worst_kl,', start=bd_c)
    bd_g = find(BD, 'gc = a.generate("", p, seed=7, temp=0.0, max_tokens=1, cached=True)', start=bd_c)
    stage_calls = sorted(set(re.findall(r"box_determinism\.py --stage (\w+)",
                                        git("grep", "-h", "box_determinism.py --stage", PIN, "--", "."))))
    det_raws = sorted(f for f in git("ls-tree", "-r", "--name-only", PIN, "--", "results/raw").splitlines()
                      if "determinism" in os.path.basename(f))
    raw_rows = []
    for f in det_raws:
        ls_ = lines_of(f)
        pth = next((x.strip() for x in ls_ if x.strip().startswith('"path": "')), None)
        ws = next((x.strip() for x in ls_ if x.strip().startswith("worst symKL")), None)
        raw_rows.append(f"{f} (model {pth[9:-2] if pth else '?'}; `{ws}`)")
    rc_ = find("RESULTS.md", "| C. kernel path, cached vs uncached | exact, worst symKL")
    rr_ = find("RESULTS.md", "- **The re-characterization reproduces the terminated box exactly.**")
    rr_end = find("RESULTS.md", "The new raw log is the evidence that it was re-measured.", start=rr_)
    olmo_div_idx = sorted(x for f_ in ("data/olmo/cached_gen_sft.json", "data/olmo/cached_gen_dpo.json",
                                       "data/olmo/cached_gen_instruct.json")
                          for x in olmo_cg[f_]["div_idx"])
    CGS = "scripts/box_cached_gen_smoke.py"
    cgs_k = find(CGS, "for k, (x, y) in enumerate(zip(u.token_ids, c.token_ids)):")
    w(f"- The OLMo first-token gate, `{DB}`@{PIN} (stage `{det['stage']}`; commits touching it: "
      f"{det_hist}): `C_kernel_path` max_kl {ck['max_kl']}, bar_1e-3 {ck['bar_1e-3']}, all_exact "
      f"{ck['all_exact']}, {len(ck['rows'])} rows (probes). Section C of the script compares a cached "
      f"and an uncached one-token generation's first logits ({loc(BD, bd_c, bd_e)}; the call, "
      f"{loc(BD, bd_g)}: `{lines_of(BD)[bd_g - 1].strip()}`).  [reproduced]")
    w(f"- It ran on Base only: determinism artifacts under data/olmo at the pin: {det_files}; every "
      f"`box_determinism.py --stage` invocation in tracked files names stage(s) {stage_calls}; the "
      f"determinism raws: {raw_rows}. The 2026-08-23 re-measurement was identical and the artifact "
      f"left unchanged: {loc('RESULTS.md', rc_)}: \"{q(text_span('RESULTS.md', rc_, rc_), 200)}\"; "
      f"{loc('RESULTS.md', rr_, rr_end)}: \"{q(text_span('RESULTS.md', rr_, rr_end), 1100)}\".  "
      "[reproduced / log-only]")
    w(f"- The record's prose on it: {loc('RESULTS.md', ok1_ - 2, ok1_ + 1)}: "
      f"\"{q(text_span('RESULTS.md', ok1_ - 2, ok1_ + 1), 300)}\"; "
      f"and the licence gap was named in advance, {loc('RESULTS.md', olc_ - 4, olc_ + 3)}: "
      f"\"{q(text_span('RESULTS.md', olc_ - 4, olc_ + 3), 600)}\".  [log-only]")
    w(f"- At SFT, DPO and Instruct no first-token gate ran. Every diverging case there has "
      f"`diverge_index` (0-based: {loc(CGS, cgs_k, cgs_k + 3)}) in {olmo_div_idx}: token 0 agreed "
      f"in every case ({min(olmo_div_idx) >= 1}) and the paths diverged at token index "
      f"{min(olmo_div_idx)}-{max(olmo_div_idx)}.  [reproduced]")
    fig("OLMo first-token gate (Base only)", f"max_kl {ck['max_kl']}; all_exact {ck['all_exact']}; "
        f"{len(ck['rows'])} probes; bar_1e-3 {ck['bar_1e-3']}", f"{DB}:C_kernel_path (stage "
        f"{det['stage']})", "reproduced",
        f"Base only; no first-token gate at SFT/DPO/Instruct; committed {det_hist[-1]}, "
        "re-measured identical 2026-08-23 (artifact unchanged)")
    w("")
    w("Reading: on a different model, precision, backend and code path, multi-token cached "
      "generation also diverged from the uncached re-forward -- in greedy, uninjected cases too. "
      f"The OLMo first-token gate ran on Base only (max_kl {ck['max_kl']}), where multi-token "
      f"generation also matched (Base {olmo_cg['data/olmo/cached_gen_v3.json']['div']} of "
      f"{olmo_cg['data/olmo/cached_gen_v3.json']['n']} in both runs); at SFT, DPO and Instruct no "
      "first-token gate ran, but every diverging case agreed at token 0 and diverged at token "
      f"index {min(olmo_div_idx)}-{max(olmo_div_idx)}. That parallels the Qwen T-step divergences "
      "above (a passed first-token gate; token 0 agreed in every divergent round, first divergent "
      f"index {min(tstep_div)}-{max(tstep_div)}), not floor 1 itself (c1 smoke 1b diverged at "
      f"index {min(r['first'] for r in hi)}), and is consistent with a path-level rather than "
      "kernel-specific cause (F1). It is an analogy across systems, not a measurement on Qwen.")
    w("")
    for f_, s_ in olmo_cg.items():
        fig(f"OLMo cached-generation gate, {s_['stage']} ({os.path.basename(f_)})",
            f"{s_['div']}/{s_['n']} diverging ({s_['un']} uninjected, {s_['greedy']} at temp 0.0); "
            f"{s_['gate']}", f"{f_}:rows[].ids_identical, .injected, .temp; gate",
            "reproduced", f"{s_['dtype']}, {s_['backend']}; record {loc('RESULTS.md', ocg_, ocg_ + 17)}")
    if f1_idx is not None:
        sft = olmo_cg["data/olmo/cached_gen_sft.json"]
        dpo = olmo_cg["data/olmo/cached_gen_dpo.json"]
        ins = olmo_cg["data/olmo/cached_gen_instruct.json"]
        flags[f1_idx] += (
            f" Independent evidence (section 3): on OLMo at bf16, PyTorch/CUDA, without the "
            f"port, multi-token cached generation diverged from uncached at SFT, DPO and "
            f"Instruct ({sft['div']}, {dpo['div']} and {ins['div']} of 14 cases; "
            f"{sft['greedy_un'] + dpo['greedy_un'] + ins['greedy_un']} of them greedy and "
            "uninjected). The OLMo first-token gate ran on Base only "
            f"({DB}:C_kernel_path, {len(ck['rows'])} probes, max_kl {ck['max_kl']}), where "
            "multi-token generation also matched; at SFT, DPO and Instruct no first-token gate "
            "ran, but every diverging case agreed at token 0 and diverged at token index "
            f"{min(olmo_div_idx)}-{max(olmo_div_idx)}. The record calls it 'KV-cache numerics, an "
            f"apparatus property' ({loc('RESULTS.md', okv_, okv_ + 1)}). It parallels the Qwen "
            "T-step divergences (token 0 agreed, divergence later) on a system that runs none of "
            "the port's patches; an analogy across systems, not a measurement on Qwen.")

    # ------------------------------------------ 4. floor 2: label geometry
    w("## 4. Floor 2: sub-0.05-cosine label geometry")
    w("")
    A_ = json.loads(show("data/configs/c1r3_gate_repA.json"))
    B_ = json.loads(show("data/configs/c1r3_gate_repB.json"))
    pairs = sorted(set(A_["ctrl_cos_by_pair"]) & set(B_["ctrl_cos_by_pair"]))
    swings = [A_["ctrl_cos_by_pair"][p] - B_["ctrl_cos_by_pair"][p] for p in pairs]
    absw = [abs(x) for x in swings]
    dcond = A_["cos_ad_raw"] - B_["cos_ad_raw"]
    sd_pop = statistics.pstdev(swings)
    sd_smp = statistics.stdev(swings)
    imax = absw.index(max(absw))
    maxctrl = max(abs(x) for x in A_["ctrl_cos"] + B_["ctrl_cos"])
    w(f"From `data/configs/c1r3_gate_rep{{A,B}}.json`@{PIN} (cycle 2, c1 r3, the "
      "pre-registered matched-pair gate): replicate A assignment "
      f"{A_['assignment']}, B {B_['assignment']}; tags C=`{A_['tags']['C']}`, "
      f"C'=`{A_['tags']['Cp']}`; {len(A_['tags']['controls'])} control tags -> "
      f"{len(pairs)} shared control pairs.")
    w("")
    dq_ = find(P, "pair p, cos_r(p) = cosine of (fp_ad,r(tag1) − fp_ad,r(tag2)) with the")
    dl_ = find(P, "gate on all 12 probes × 6 workspace layers")
    w(f"Quantity (rule 6): cos_r(p) is the cosine between a label pair's fingerprint "
      f"contrast under replicate r's adapter and the steered hi-lo fingerprint axis, "
      f"{loc(P, dq_ - 1, dq_ + 2)}: \"{q(text_span(P, dq_ - 1, dq_ + 2), 400)}\"; "
      f"fingerprints are J-lens readouts over 12 probes x 6 workspace layers, "
      f"{loc(P, dl_ - 1, dl_)}: \"{q(text_span(P, dl_ - 1, dl_))}\" (stated for the "
      f"r1 full run; r3 ran 'identical to r2-final', "
      f"{loc(P, find(P, '- **Protocol:** identical to r2-final'))}, and the r3 JSONs carry "
      f"no probe or layer field; their keys: {sorted(A_.keys())}; axis_norm A "
      f"{A_['axis_norm']:.2f}, B {B_['axis_norm']:.2f}). Deterministic readout; no "
      "cross-validation is involved.")
    w("")
    w(f"- conditioned pair raw cosine (C-C' fingerprint contrast vs the hi-lo axis): "
      f"A {A_['cos_ad_raw']:+.4f}, B {B_['cos_ad_raw']:+.4f}; no-adapter tag baseline "
      f"(signed) A {A_['cos_base_signed']:+.4f}, B {B_['cos_base_signed']:+.4f}.")
    w(f"- D_cond = A - B = {dcond:+.4f}.")
    w(f"- control-pair swings (A - B), n = {len(swings)}: mean|s| = "
      f"{statistics.mean(absw):.4f}; sd = {sd_pop:.4f} (population; sample sd "
      f"{sd_smp:.4f}); max|s| = {max(absw):.4f} (pair `{pairs[imax]}`).")
    w(f"- criterion (pre-registered): sign D_cond > 0 -> {dcond > 0}; magnitude "
      f"D_cond > max|s| -> {dcond > max(absw)}; verdict "
      f"{'PASS' if dcond > 0 and dcond > max(absw) else 'FAIL'}. z = D_cond / sd = "
      f"{dcond / sd_pop:+.2f} (population sd) / {dcond / sd_smp:+.2f} (sample sd); "
      "descriptive only.")
    w(f"- the control-pair cosines themselves (the label geometry): range A "
      f"[{min(A_['ctrl_cos']):+.4f}, {max(A_['ctrl_cos']):+.4f}], B "
      f"[{min(B_['ctrl_cos']):+.4f}, {max(B_['ctrl_cos']):+.4f}]; max |cos| = {maxctrl:.4f}.")
    w("")
    a = find(P, "- **Primary (pre-registered):** control-pair swings n=28: mean|s| = 0.0121,")
    w(f"- Record: {loc(P, a, a + 3)}: \"{q(text_span(P, a, a + 3), 500)}\"")
    a_r2 = find(P, "independently trained adapters at mean |Δ| = 0.009 (sd 0.006, max 0.016).")
    w(f"- r2 post-hoc (6 control pairs; no r2 JSON committed): {loc(P, a_r2 - 2, a_r2 + 1)}: "
      f"\"{q(text_span(P, a_r2 - 2, a_r2 + 1), 420)}\"")
    a = find(F2, "3. **Tag geometry is deterministic, and under-sampled nulls flatter weak")
    w(f"- {loc(F2, a, a + 5)}: \"{q(text_span(F2, a, a + 5), 600)}\"")
    a_fl = find(F2, "- **A cleaner substrate.** Two independent floors in this cycle were")
    w(f"- The two floors as the record names them, {loc(F2, a_fl, a_fl + 5)}: "
      f"\"{q(text_span(F2, a_fl, a_fl + 5), 700)}\"")
    a = find("FINDINGS-3.md", "- **Substrate swap** (unquantized model)")
    w(f"- {loc('FINDINGS-3.md', a, a + 1)}: \"{q(text_span('FINDINGS-3.md', a, a + 1))}\"")
    w("")
    w("Reading: what is under 0.05 is the conditioning signal (D_cond "
      f"{dcond:+.4f}) and the adapter-to-adapter reproducibility of the label "
      f"geometry (control swings, max {max(absw):.4f}); the label-pair cosines "
      f"themselves reach {maxctrl:.3f}. The record's own scale word is \"the "
      "0.03-cosine scale\" (FINDINGS-2 above); the preprint's \"deterministic "
      "sub-0.05-cosine label geometry\" is true of the swings and the signal, not of "
      "the geometry's raw cosines.")
    w("")
    scope2 = (f"cosine vs the steered hi-lo fingerprint axis; fingerprint = J-lens readouts over "
              f"12 probes x 6 workspace layers ({loc(P, dl_ - 1, dl_)}, the r1 entry; r3 ran "
              f"identical to r2-final, {loc(P, find(P, '- **Protocol:** identical to r2-final'))}; "
              "the r3 JSONs carry no probe/layer field); deterministic, no CV")
    fig("D_cond", f"{dcond:+.4f}", "data/configs/c1r3_gate_rep{A,B}.json:cos_ad_raw (A - B)",
        "reproduced", f"{scope2}; record {loc(P, find(P, '- **Primary (pre-registered):** control-pair swings n=28'), find(P, '- **Primary (pre-registered):** control-pair swings n=28') + 3)}")
    fig("max |control swing| (n = 28)", f"{max(absw):.4f} ({pairs[imax]})",
        "c1r3_gate_rep{A,B}.json:ctrl_cos_by_pair", "reproduced", "same quantity and scope as D_cond")
    fig("mean |control swing|; sd", f"{statistics.mean(absw):.4f}; {sd_pop:.4f} (pop) / {sd_smp:.4f} (sample)",
        "c1r3_gate_rep{A,B}.json:ctrl_cos_by_pair", "reproduced",
        "same scope as D_cond; the record's sd 0.0133 is the population sd")
    fig("z (descriptive)", f"{dcond / sd_pop:+.2f}", "D_cond / sd(control swings)", "reproduced",
        "population sd; +%.2f with the sample sd" % (dcond / sd_smp))
    fig("no-adapter tag baseline", f"{A_['cos_base_signed']:+.4f} / {B_['cos_base_signed']:+.4f}",
        "c1r3_gate_rep{A,B}.json:cos_base_signed", "reproduced", "same scope as D_cond")
    fig("label-pair cosines, max |cos|", f"{maxctrl:.4f}", "c1r3_gate_rep{A,B}.json:ctrl_cos",
        "reproduced", "same scope as D_cond; the geometry itself is not sub-0.05; its "
        "adapter-to-adapter reproducibility is")
    fig("r2: mean |delta| 0.009 (sd 0.006, max 0.016), 6 pairs", "0.009 / 0.006 / 0.016",
        loc(P, a_r2 - 2, a_r2 + 1), "log-only", "no r2 gate JSON at the pin")
    fig("'0.03-cosine scale' (record's wording of floor 2)", "0.03", loc(F2, a_fl + 2, a_fl + 3),
        "log-only", "the preprint's 'sub-0.05' is consistent with it (D_cond 0.0214, max swing 0.0346)")
    clause_map.append(("floor 2: conditioned swing +0.021 vs max control swing 0.035 over 28 pairs; both < 0.05; label cosines to 0.15 and reproducible",
                       "data/configs/c1r3_gate_rep{A,B}.json (reproduced, section 4); "
                       f"{loc(P, find(P, '- **Primary (pre-registered):** control-pair swings n=28'), find(P, '- **Primary (pre-registered):** control-pair swings n=28') + 3)}"))
    clause_map.append(("the record calls both floors numerics-shaped",
                       loc(F2, a_fl, a_fl + 5)))

    # ------------------------------------------- 5. verification meaning
    w("## 5. What \"verified against an untouched model\" means in the record")
    w("")
    gg = subprocess.run(["git", "-C", REPO, "grep", "-n", "-i", "untouched model", PIN, "--", "."],
                        capture_output=True, text=True).stdout.strip().splitlines()
    w(f"- The phrase \"untouched model\" in tracked files at {PIN} (`git grep -i`): "
      f"{len(gg)} line(s): {[x.split(':', 3)[1] + ':' + x.split(':', 3)[2] for x in gg]}. It "
      "is not a record term (the note itself is not on this machine; preflight note 1).")
    # --- round 2, finding 2: the phrase's source in the untracked preprint drafts ---
    kl0_rows = [json.loads(l) for l in show("data/e2a/g3prime_kl.jsonl").splitlines() if l.strip()]
    kl_keys0 = {(r["arm"], r["session"], r["choice"]) for r in kl0_rows}
    pre_rows, um_src = [], None
    for f in sorted(glob.glob(os.path.join(REPO, "archive", "PREPRINT-v1_0-draft.pre-patch-v*.md"))) \
            + [os.path.join(REPO, PREPRINT)]:
        rel = os.path.relpath(f, REPO)
        tracked = subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch", rel],
                                 capture_output=True).returncode == 0
        fl_ = file_lines(f)
        um = [i for i, x in enumerate(fl_, start=1) if "untouched model" in x.lower()]
        rf = [i for i, x in enumerate(fl_, start=1) if "verified by an identical re-forward of the choice computation" in x]
        pre_rows.append((rel, sha256_file(f)[:16], tracked, um, rf))
        if um and um_src is None and rel != PREPRINT:  # round 9: archived drafts only
            m_ = re.search(r"verified against an untouched model[^:]*:[^.]*\.", fl_[um[0] - 1])
            n_ = re.search(r"(\d+) distinct verified forward passes", fl_[um[0] - 1])
            um_src = (rel, um[0], m_.group(0) if m_ else q(fl_[um[0] - 1], 300),
                      int(n_.group(1)) if n_ else None)
    w("- Where the phrase comes from (files on disk, not record): the preprint drafts, "
      "(file, sha256 prefix, tracked, lines with 'untouched model', lines with 'verified by an "
      f"identical re-forward of the choice computation'): {pre_rows}.")
    if um_src:
        w(f"- `{um_src[0]}`:{um_src[1]} (UNTRACKED): \"...{um_src[2]}\" -- the preprint's own earlier "
          "wording for the choice-read construction check; from patch v3 on the same sentence reads "
          "\"verified by an identical re-forward of the choice computation\". Its count, "
          f"{um_src[3]}, against the number of distinct (arm, session, choice) keys of "
          f"`data/e2a/g3prime_kl.jsonl` (item 2 below), {len(kl_keys0)}: "
          f"{'equal' if um_src[3] == len(kl_keys0) else 'NOT EQUAL'}; every row's kl == 0.0: "
          f"{all(r['kl'] == 0.0 for r in kl0_rows)}.")
    fig("'verified against an untouched model' (as a record term)", f"{len(gg)} hit(s), "
        "the block only", f"git grep -i 'untouched model' {PIN}", "not found",
        (f"source: the preprint's own earlier wording, untracked `{um_src[0]}`:{um_src[1]} (choice-read "
         "re-forward identity; replaced at patch v3 by 'verified by an identical re-forward of the "
         "choice computation'); section 5" if um_src else
         "the record defines its verifications otherwise (section 5)"))
    w("")
    w("The record's verifications, each with what is held fixed and what is compared:")
    w("")
    # (i) kernel gate
    O = "valence_core/regression/oracle.py"
    ok_ = find(O, "def check_kernel(adapter, tasks, tag_ids) -> list[Result]:")
    oc_ = find(O, "for cached in (True, False):")
    w(f"1. **Kernel/path gate (e2a g1, g1r).** Same weights, same 4-bit quantization, "
      "same port patch, the SAME steering vector injected on both sides; compared: "
      "the cached O(T) stream vs the uncached positional re-forward, symmetric KL of "
      "the first-response-token distribution over 16 session prefixes x 2 poles. "
      f"Code: {loc(O, ok_, ok_ + 4)} (\"{q(text_span(O, ok_ + 1, ok_ + 4).replace(chr(34) * 3, ''), 300)}\"), "
      f"{loc(O, oc_ - 1, oc_ + 4)}.")
    RA = "archive/RESULTS-cycles3-4.md"
    a = find(RA, "e2a g1 — kernel gate FAIL at both fracs (marginal);")
    hist_all = git("log", "--all", "--format=%h %ad", "--date=short", "--",
                   "data/e2a/g1_kernel_gate.json").strip().splitlines()
    first_tf = json.loads(show("data/e2a/g1_kernel_gate.json",
                               hist_all[-1].split()[0])).get("template_family")
    g1s = os.path.join(CLONE, "scripts", "e2a_g1_kernel_gate.py")
    g1s_ln = ffind(g1s, '"g1_kernel_gate.json"') if os.path.exists(g1s) else None
    w(f"   - g1 (v1 templates), {loc(RA, a, a + 6)}: \"{q(text_span(RA, a, a + 6), 500)}\"  "
      f"[log-only: no g1 (v1-template) artifact was ever committed -- every commit touching "
      f"`data/e2a/g1_kernel_gate.json` in any ref (`git log --all`): {hist_all}, the first "
      f"holding template_family {first_tf!r}"
      + (f"; the g1 script writes that fixed path (clone file "
         f"`jlens-qwen36/scripts/e2a_g1_kernel_gate.py:{g1s_ln}`), so g1r's run replaced "
         "g1's output on disk before the path entered git" if g1s_ln else "")
      + "]")
    g1raw = "results/raw/2026-08-09_e2a_g1.txt"
    x = find(g1raw, "frac 0.1: max KL")
    w(f"   - {loc(g1raw, x, x + 1)}: `{lines_of(g1raw)[x - 1].strip()}` / `{lines_of(g1raw)[x].strip()}`")
    fig("g1 (v1 templates) max KL 1.31e-3 / 1.15e-3: FAIL", "1.31e-03 / 1.15e-03",
        f"{loc(g1raw, x, x + 1)}; {loc(RA, a, a + 6)}", "log-only",
        "the kernel-gate values 7.11e-4 / 7.39e-4 are g1r's (v2 templates, PASS); g1 failed; "
        "no g1 artifact was ever committed")
    a = find(RA, "e2a g1r (v2 templates) — PASS both fracs; cached round")
    w(f"   - g1r (v2 templates), {loc(RA, a, a + 10)}: \"{q(text_span(RA, a, a + 10), 700)}\"")
    g1rraw = "results/raw/2026-08-09_e2a_g1r.txt"
    x = find(g1rraw, "frac 0.1: max KL")
    w(f"   - {loc(g1rraw, x, x + 1)}: `{lines_of(g1rraw)[x - 1].strip()}` / `{lines_of(g1rraw)[x].strip()}`")
    hist = git("log", "--format=%h %ad", "--date=short", PIN, "--",
               "data/e2a/g1_kernel_gate.json").strip().splitlines()
    w(f"   - Artifact: `data/e2a/g1_kernel_gate.json` (commits touching it up to the pin: {hist}): "
      f"template_family `{g1['template_family']}`, max_kl {g1['results']['0.1']['max_kl']:.4e} "
      f"(frac 0.1) / {g1['results']['0.2']['max_kl']:.4e} (frac 0.2), bar {g1['gate']}.  [reproduced]")
    fig("g1r kernel gate max KL 7.11e-4 / 7.39e-4 (bar 1e-3)",
        f"{g1['results']['0.1']['max_kl']:.4e} / {g1['results']['0.2']['max_kl']:.4e}; "
        f"bar {g1['gate']}", "data/e2a/g1_kernel_gate.json:results.{0.1,0.2}.max_kl, gate",
        "reproduced", "cached vs uncached, same vector; not a comparison with another model")
    clause_map.append(("kernel gate: cached vs uncached, same patched 4-bit model, same vector; 7.11e-4 / 7.39e-4, bar 1e-3",
                       f"data/e2a/g1_kernel_gate.json (reproduced); {loc(O, ok_, ok_ + 4)}; {loc(RA, a, a + 10)}"))
    # rule-26 reproduction (history)
    old = json.loads(show("data/regression/oracle_rule26.json", "db0d177"))
    anc = subprocess.run(["git", "-C", REPO, "merge-base", "--is-ancestor", "db0d177", PIN]).returncode == 0
    kr = [r for r in old["results"] if r["name"].startswith("g1r kernel-gate")]
    w(f"   - Rule-26 reproduction through the refactored core (`data/regression/oracle_rule26.json` "
      f"as committed at db0d177, an ancestor of {PIN}: {anc}; at {PIN} the same path holds only "
      f"{len(ora['results'])} criterion-(iii) rows from a later re-run): "
      + "; ".join(f"{r['name']}: expected {r['expected']}, got {r['got']} ({r['note']})" for r in kr)
      + ".  [reproduced from the committed artifact at db0d177]")
    fig("rule-26 kernel-gate reproduction 7.1131e-4 / 7.3924e-4",
        " / ".join(r["got"] for r in kr),
        "data/regression/oracle_rule26.json@db0d177:results[name~g1r]", "reproduced",
        f"artifact as committed at db0d177 (ancestor of {PIN}); overwritten later with criterion-(iii) rows only")
    a = find("RESULTS.md", "**Criterion (i) — g1r kernel gate:** max symmetric KL")
    w(f"   - {loc('RESULTS.md', a, a + 4)}: \"{q(text_span('RESULTS.md', a, a + 4), 500)}\"")
    a = find("CLAUDE.md", "g1r kernel-gate KLs (7.11e-4 / 7.39e-4 ± tolerance)")
    w(f"   - Acceptance criterion, {loc('CLAUDE.md', a - 1, a)}: \"{q(text_span('CLAUDE.md', a - 1, a))}\"")
    # (ii) choice-read verify
    a = find("RESULTS.md", "- **§1b INSULATION ASSERTION (report; nothing corrected).**")
    w(f"2. **Choice-read construction check (g3' clause 1; rule-26 criterion (iii)).** "
      "Same weights, quantization and patch, NO vector; compared: two consecutive "
      "vanilla forwards of identical token ids; bar KL = 0.0 exactly (1e-6 in e2a's "
      f"wording). {loc('RESULTS.md', a, a + 15)}: \"{q(text_span('RESULTS.md', a + 1, a + 15), 1300)}\"")
    apr_ = find(RA, "KL(choice forward ‖ vanilla forward, same text) ≤ 1e-6")
    w(f"   - Pre-registered wording, {loc(RA, apr_ - 4, apr_)}: \"{q(text_span(RA, apr_ - 4, apr_), 420)}\"")
    R_ = "valence_core/readout.py"
    w(f"   - Bars in code: {loc(R_, find(R_, 'VERIFY_KL_BAR = 0.0'), find(R_, 'VERIFY_KL_BAR_E2A = 1e-6'))}; "
      f"KL = max of both directions, {loc(R_, find(R_, 'def symmetric_kl'), find(R_, 'def symmetric_kl') + 4)}.")
    kl = [json.loads(l) for l in show("data/e2a/g3prime_kl.jsonl").splitlines() if l.strip()]
    kl_keys = {(r["arm"], r["session"], r["choice"]) for r in kl}
    kl0 = sum(1 for r in kl if r["kl"] == 0.0)
    w(f"   - `data/e2a/g3prime_kl.jsonl`: {len(kl)} rows over {len(kl_keys)} distinct "
      f"(arm, session, choice) keys, {kl0} rows with kl == 0.0, max {max(r['kl'] for r in kl)} "
      "(N4(iii) owns the 311-distinct / 360-row / 281-of-1115 reading).  [reproduced]")
    fig("choice-read verify KL = 0.0 (e2a ledger)",
        f"{kl0}/{len(kl)} rows at 0.0 ({len(kl_keys)} distinct keys)",
        "data/e2a/g3prime_kl.jsonl:kl, arm/session/choice", "reproduced",
        "re-forward identity of the vanilla read; e2a's registered bar 1e-6, the refactored "
        "core's 0.0; N4(iii) owns 311 vs 360")
    clause_map.append(("choice-read check: identical unsteered forward re-run on identical ids; "
                       "every e2a check measured exactly 0.0; e2a's bar 1e-6, the refactored core's 0.0",
                       f"{loc('RESULTS.md', a, a + 15)}; data/e2a/g3prime_kl.jsonl (reproduced); "
                       f"{loc(RA, apr_ - 4, apr_)}; "
                       f"{loc(R_, find(R_, 'VERIFY_KL_BAR = 0.0'), find(R_, 'VERIFY_KL_BAR_E2A = 1e-6'))}"))
    # (iii) no unquantized comparison
    a = find("RESULTS.md", "- **A precision caveat that applies to every option above.**")
    w(f"3. **No comparison against an unpatched or unquantized Qwen.** "
      f"{loc('RESULTS.md', a, a + 6)}: \"{q(text_span('RESULTS.md', a, a + 6), 500)}\"")
    rl = lines_of("RESULTS.md")
    g4 = [i for i, ln in enumerate(rl, start=1) if re.search(r"\bg4\b", ln)]
    s3 = [i for i, ln in enumerate(rl, start=1)
          if (re.search(r"\bS3\b", ln) and re.search(r"bf16|g4|S1.S3|quantiz", ln))
          or re.search(r"(?i)qwen bf16|bf16 e0|unquantized qwen|quantization.robustness", ln)]
    w(f"   - Every RESULTS.md@{PIN} line with the token `g4`: {g4}; with `S3` beside "
      f"bf16/g4/S1-S3/quantiz*, or with 'Qwen bf16' / 'bf16 e0' / 'unquantized Qwen' / "
      f"'quantization-robustness': {s3}. Read in full: "
      + "; ".join(f":{i} \"{q(rl[i - 1].strip(), 120)}\"" for i in sorted(set(g4 + s3)))
      + ". None reports a run.")
    PG_ = "PROPOSAL-g-ontogeny-of-evaluation.md"
    a3 = find(PG_, "**S3 — bf16 e0 subsample** (was \"g4\").")
    w(f"   - The plan, {loc(PG_, a3, a3 + 2)}: \"{q(text_span(PG_, a3, a3 + 2))}\"")
    a4 = find("CLAUDE.md", "v3.0 quantization deferral is deleted: the numerics-floor caveats")
    w(f"   - OLMo is bf16 and outside these floors, {loc('CLAUDE.md', a4 - 6, a4 + 1)}: "
      f"\"{q(text_span('CLAUDE.md', a4 - 6, a4 + 1), 600)}\"")
    fig("unquantized Qwen comparison (S3 / g4)", "no run in the record",
        f"RESULTS.md@{PIN} lines {sorted(set(g4 + s3))}; {loc(PG_, a3, a3 + 2)}", "not found",
        "planned, not run")
    clause_map.append(("no unquantized Qwen run (S3 / g4 planned, not run); OLMo bf16",
                       f"{loc('RESULTS.md', a, a + 6)}; {loc(PG_, a3, a3 + 2)}; {loc('CLAUDE.md', a4 - 6, a4 + 1)}"))
    w("")
    w("**Answer to the block's question** (\"same weights and quantization, no patch? or "
      "patch with no vector?\"): "
      + (f"the phrase is the preprint's earlier wording (`{um_src[0]}`:{um_src[1]}, untracked) "
         "for the choice-read construction check. It meant the choice-read re-forward identity "
         "(item 2): the same weights, the same 4-bit quantization and the same port patch, with "
         "no vector, comparing that vanilla forward with itself. It meant neither \"no patch\" nor "
         "a different model. " if um_src else "")
      + "More broadly, no verification in the record compares two models: every one holds "
      "the weights, the 4-bit quantization AND the port's patch fixed. The kernel gate compares two computation paths with the "
      "vector present on both; the choice-read check is \"patch with no vector\" in the "
      "sense that the read carries no vector, but it compares that vanilla forward "
      "with itself (re-forward identity), not with a different model; the rule-26 "
      "oracle compares the refactored code with the original code on the same model. "
      "No run compares the patched model with an unpatched or an unquantized one. "
      "(On the static reading of 2e, the uncached vanilla forward is computed as "
      "stock mlx-lm computes it, which would make \"patch with no vector\" and "
      "\"untouched 4-bit model\" the same computation for the reads; that is flag F1, "
      "not a record fact.)")
    w("")

    # ---------------------------------------------------- 6. paragraph
    bits = qsum.get("bits", "?")
    gsz = qsum.get("group_size", "?")
    g01 = g1["results"]["0.1"]["max_kl"]
    g02 = g1["results"]["0.2"]["max_kl"]
    first_hi = [r["first"] for r in hi]
    _o_sft = olmo_cg["data/olmo/cached_gen_sft.json"]
    _o_dpo = olmo_cg["data/olmo/cached_gen_dpo.json"]
    _o_ins = olmo_cg["data/olmo/cached_gen_instruct.json"]
    _o_b3 = olmo_cg["data/olmo/cached_gen_v3.json"]
    _o_b3b = olmo_cg["data/olmo/cached_gen_v3b.json"]
    assert (_o_b3["div"], _o_b3["n"]) == (_o_b3b["div"], _o_b3b["n"]), "base runs differ"
    assert _o_sft["n"] == _o_dpo["n"] == _o_ins["n"]
    # the versions clause says "single install" and "single model snapshot" (computed-new, 1a)
    assert len(snaps) == 1 and len(blob_dates) == 1, "single snapshot / one blob date"
    assert sorted(x.split("-")[0] for x in inst) == ["mlx", "mlx_lm", "mlx_metal"], inst
    para = (
        "**Qwen numerics.** Every Qwen result here comes from "
        "`mlx-community/Qwen3.6-27B-4bit` (Hugging Face revision `c000ac2c`), run "
        f"with MLX {prov['library_versions']['mlx']} and mlx-lm "
        f"{prov['library_versions']['mlx-lm']} (the versions recorded by every Qwen artifact "
        "that names its model, the first committed on "
        f"{time.strftime('%d %B %Y', time.strptime(first_lv.split()[1], '%Y-%m-%d')).lstrip('0')}"
        "; the environment's single install, dated at "
        "setup, and its single model snapshot are consistent with them throughout) on an Apple "
        "M4 Pro laptop. The "
        f"checkpoint uses MLX's affine {bits}-bit quantization with a group size of "
        f"{gsz} (one bf16 scale and one bf16 bias per {gsz} weights). Every linear "
        "projection in the language model is quantized, as are the token embedding "
        "and the output head; the norms, the depthwise convolution and the Gated "
        "DeltaNet decay parameters stay in bf16. The \"custom kernel patch\" is not "
        "our code. It is part of the MLX port we run, `jlens-qwen36` "
        "(WeZZard/jlens-qwen36 at commit `d788bc3`, Apache-2.0), kept as a "
        "gitignored clone inside the working copy and not part of the tag. At load "
        "time the port monkey-patches mlx-lm's Gated DeltaNet layers so that the "
        f"model's {qsum.get('n_linear', '?')} linear-attention layers can be differentiated "
        "for Jacobian-lens fitting: the recurrence becomes switchable between "
        "mlx-lm's fused Metal kernel and a pure-ops sequential loop, and the layer's "
        "forward is re-implemented inside a custom function with a hand-written Metal "
        "backward kernel (the port also installs a gradient-checkpointing wrapper, "
        "which, on a reading of the code, the custom forward bypasses). It changes how the recurrence is "
        "computed, not the weights or the quantization. Our adapter sets the cached "
        "decoding path to the ops loop (`set_inference_mode(False)`), recorded in "
        "the artifacts as `gdn_inference_mode: \"ops (fused disabled)\"`. Our own "
        "changes to the clone (a dependency pin, a bug fix in an ablation helper, "
        "edits to one example script, added modules and scripts) do not define or "
        "rebind any kernel. The record names two floors as numerics-shaped. First, "
        "with a steering vector as large as the residual norm at layer 48, a cached "
        "O(T) greedy decode diverged from the uncached O(T²) re-forward within the "
        f"first {max(first_hi) + 1} tokens of a {hi[0]['n']}-token check under a "
        "high-strain state, whichever kernel the cached path used, while a "
        "low-strain state of the same norm matched exactly. The record reads this as the "
        "high-strain state leaving the next token near an argmax tie, where small "
        "floating-point differences between the two computation paths flip it. The lab's "
        "rules therefore required the uncached path for greedy readouts under high-norm "
        "steering. Sampled steered generation was allowed on the cached path behind a "
        "next-token KL gate re-run for each direction family and dose; since "
        "September 2026 that gate licenses first-token reads only, and multi-token "
        "generation on the cached path needs its own token-identity check (the "
        "cached-generation disclosure says which runs this touches). Second, the "
        "cycle-2 conditioning gate failed at "
        "the scale of deterministic label geometry: the cosine between the "
        "conditioned label pair's fingerprint contrast and the state axis moved "
        f"{dcond:+.3f} between two counterbalanced, independently trained adapters, "
        f"against a largest movement of {max(absw):.3f} among {len(swings)} control "
        "label pairs. Both numbers are under 0.05, while the "
        f"label-pair cosines themselves reach {maxctrl:.2f} and carry over from one "
        "adapter to the next. \"Verified\" in this repository never means compared "
        "against an unpatched or unquantized Qwen. The kernel gate compares the "
        "cached and uncached paths of the same patched 4-bit model with the same "
        "vector injected (for e2a, a maximum symmetric KL on the first response "
        f"token of {g01:.2e} at dose 0.10 and {g02:.2e} at dose 0.20, against a bar "
        "of 1e-3; `data/e2a/g1_kernel_gate.json`). The choice-read check re-runs the "
        "identical unsteered forward on identical token ids; every e2a check measured "
        "a KL of exactly 0.0 (e2a's pre-registered bar was 1e-6; the refactored core "
        "requires exactly 0.0). The rule-26 oracle re-ran published measurements "
        "through the refactored code on the same model. No unquantized Qwen run is in the "
        "record: the planned bf16 subsample (S3, formerly g4) has not been run. The "
        "OLMo results ran at bf16 on PyTorch/CUDA without this port, so the 4-bit and "
        "patch caveats do not apply to them. The cached-path caveat does have an OLMo "
        "counterpart: multi-token cached generation diverged from uncached generation "
        f"at SFT, DPO and Instruct ({_o_sft['div']}, {_o_dpo['div']} and {_o_ins['div']} "
        f"of {_o_sft['n']} test cases, greedy uninjected ones included; Base "
        f"{_o_b3['div']} of {_o_b3['n']} in both runs), so every OLMo B-phase "
        "generation ran uncached."
    )
    w("## 6. The README paragraph (README-NOTE §6, beside N4(iv)'s)")
    w("")
    w(para)
    w("")
    w(f"(Length: {len(para.split())} words. The paragraph carries no record locators "
      "beyond one artifact path; every factual clause is mapped in section 7.)")
    w("")

    # ------------------------------------------------ 7. clause map
    w("## 7. Clause -> locator map for the paragraph")
    w("")
    clause_map.insert(0, ("mlx 0.31.2 / mlx-lm 0.31.3; model id", "data/regression/oracle_rule26.json:provenance (reproduced)"))
    clause_map.append(("patch mechanics: switchable recurrence (fused kernel / ops loop), custom function + Metal backward, checkpointing wrapper installed but bypassed; weights and quantization untouched",
                       "section 2e (clone + venv source read as text, static reading; computed-new; "
                       "the port files are byte-identical to public upstream d788bc3 (2d), and the "
                       "mlx-lm lines are from the venv's installed mlx-lm 0.31.3 (its dist-info), a "
                       "public release; a reader can check both there)"))
    clause_map.append(("purpose: differentiability for Jacobian-lens fitting",
                       "upstream README (clone file, section 2d; computed-new, context). Not "
                       + loc(C1, find(C1, "The custom Metal GDN backward kernel in this port drops the gradient paths"))
                       + ", which states a g/β limitation, stale against the d788bc3 code (section 2a)"))
    clause_map.append(("adapter puts the cached path on the ops loop; artifacts record 'ops (fused disabled)'",
                       f"{loc(A, find(A, 'self._patch_gdn.set_inference_mode(False)'))}; {loc(A, xg)}; section 2c (reproduced)"))
    clause_map.append(("none of the lab's edits defines or rebinds a kernel",
                       "section 2f (computed-new: the lab's edits are untracked files inside the "
                       "gitignored clone, not in this repository, so a reader cannot check this clause)"))
    clause_map.append(("OLMo bf16 on PyTorch/CUDA, no port: no 4-bit or patch caveat", loc("CLAUDE.md", find("CLAUDE.md", "v3.0 quantization deferral is deleted") - 6,
                                                          find("CLAUDE.md", "v3.0 quantization deferral is deleted") + 1)))
    clause_map.append((f"OLMo cached generation diverged at SFT/DPO/Instruct ({_o_sft['div']}/{_o_dpo['div']}/{_o_ins['div']} of {_o_sft['n']}, greedy uninjected included; Base {_o_b3['div']} of {_o_b3['n']} twice); B-phase uncached",
                       "data/olmo/cached_gen_{v3,v3b,sft,dpo,instruct}.json (reproduced, section 3); "
                       f"{loc('RESULTS.md', ocg_, ocg_ + 5)}; {loc('RESULTS.md', ob_, ob_ + 1)}; {loc('RESULTS.md', ou_, ou_ + 2)}"))
    clause_map.append(("rule-26 oracle re-ran published measurements on the same model",
                       f"{loc('RESULTS.md', find('RESULTS.md', 'Phase 0 step 1 COMPLETE: `valence_core/` refactor ACCEPTED'), find('RESULTS.md', 'Phase 0 step 1 COMPLETE: `valence_core/` refactor ACCEPTED') + 13)}; oracle_rule26.json@db0d177 (reproduced)"))
    w("| clause | locator(s) |")
    w("|---|---|")
    for c_, l_ in clause_map:
        w(f"| {cell(c_)} | {cell(l_)} |")
    w("")
    cn_rows = [c_ for c_, l_ in clause_map if "computed-new" in l_]
    w(f"README clauses that rest wholly or partly on computed-new reads ({len(cn_rows)} rows above "
      "whose locators say computed-new): " + "; ".join(f"\"{c_}\"" for c_ in cn_rows) + ". Of these, "
      "the quantization details and the layer count (public HF revision c000ac2c), the patch "
      "mechanics, 'not our code' "
      "and the purpose (public upstream d788bc3; mlx-lm 0.31.3) can be checked by a reader against "
      "public sources; the clause on the lab's own clone edits cannot, because those edits are "
      "untracked files in the gitignored clone and not in this repository; the install-date and "
      "single-snapshot support for the versions clause is local to this machine.")
    w("")

    # ------------------------------------------------ 8. figures
    w("## 8. Figures")
    w("")
    w("| figure as the block / record writes it | value printed | source | status | note |")
    w("|---|---|---|---|---|")
    for f_ in figs:
        w(f"| {cell(f_['figure'])} | {cell(f_['value'])} | {cell(f_['source'])} | "
          f"{f_['status']} | {cell(f_['note'])} |")
    w("")
    counts: dict = {}
    for f_ in figs:
        counts[f_["status"]] = counts.get(f_["status"], 0) + 1
    w(f"Status counts: {counts}.")
    w("")

    # ------------------------------------------------ 9. notes
    w("## 9. Notes for the PI and the design seat (none is a STOP)")
    w("")
    notes = list(flags)
    notes.append(
        "F2 (wording). The preprint's \"custom kernel patch\" (untracked "
        f"`{PREPRINT}`) reads as the lab's own work. It is the port's upstream Gated "
        "DeltaNet patching, unmodified (2d); the lab's edits are non-kernel (2f). The "
        "README paragraph says so; the preprint/note may want the same.")
    notes.append(
        "F3 (wording). \"sub-0.05-cosine label geometry\": the record's phrase is \"the "
        "0.03-cosine scale\"; what sits under 0.05 is the conditioned swing "
        f"({dcond:+.4f}) and the control-swing maximum ({max(absw):.4f}); the label-pair "
        f"cosines reach {maxctrl:.3f}. Suggested: \"a conditioning signal below the "
        "adapter-to-adapter reproducibility of deterministic label geometry (both "
        "under 0.05 in cosine)\".")
    notes.append(
        "F4 (referent). The kernel-gate values 7.11e-4 / 7.39e-4 are both g1r's (v2 templates, "
        "PASS); g1 (v1 templates) FAILED at 1.31e-3 / 1.15e-3 (log-only; the artifact path now "
        "holds g1r). A text that labels the pair 'g1' or 'g1/g1r' should say g1r.")
    notes.append(
        "F5 (record hygiene). `data/regression/oracle_rule26.json` at the pin holds only "
        "four criterion-(iii) rows from the 2026-08-18 re-run; the kernel-gate and B2b "
        "reproductions live in its db0d177 and 9f3148c versions. A reader of the tag who "
        "opens the file will not find 7.1131e-4 / 7.3924e-4 there.")
    notes.append(
        "F6 (the note's phrase). \"verified against an untouched model\" does not occur in "
        "the record"
        + (f"; its source is the preprint's own earlier wording (untracked `{um_src[0]}`:{um_src[1]}), "
           "for the choice-read re-forward identity (same weights, quantization and patch, no vector, "
           "the forward compared with itself). Recommended: the wording the preprint already "
           "adopted at patch v3, \"verified by an identical re-forward of the choice computation\" "
           f"(`{PREPRINT}`:{pre_rows[-1][4][0] if pre_rows[-1][4] else '?'})" if um_src else "")
        + ". For the record's verifications as a whole it supports: \"verified on the same "
        "patched 4-bit model -- path-equivalence with the vector present (kernel gate) and "
        "re-forward identity with it absent (choice reads) -- never against an unpatched or "
        "unquantized one\".")
    for n_ in notes:
        w(f"- {n_}")
    w("")
    w("Optional sentence for the PI, to add to the paragraph only if F1's dispatch check "
      "confirms the static reading: \"The ops setting governs the cached path only; "
      "uncached forwards, including every choice read, compute the recurrence with "
      "the same fused Metal kernel an unpatched mlx-lm uses.\"")
    w("")
    w("## 10. Summary")
    w("")
    w(f"N17 is delivered: the paragraph (section 6), every clause located (section 7), "
      f"{len(figs)} figure rows (section 8: {counts}). Nothing needed an analyzer "
      "change; no STOP. Tier 3 has no pass/fail text in the block. One substantive flag "
      "(F1, labelling, static reading, no figure moves; now with LoRA training and the "
      "OLMo counterpart) and five wording or record notes (F2-F6). Section 11 records the "
      "adversarial values-checks (pass 1 and round 2) and what was done with each finding.")
    w("")

    # ------------------------------------------------ 11. values-check
    vc = [
        ("1 (substantive)", "README and 2e: the port's patch makes the layer gradient-checkpointed",
         "fixed",
         "Correct. Read as files: patch_gdn.py:96-119 installs `_checkpointed_call`; "
         "custom_gdn_patch.py:90 captures it as `original_call` and :148 installs `_new_call`; "
         "with cache=None `_new_call` never calls it (:92-146); with a cache the wrapper "
         "returns the stock call before `mx.checkpoint` (patch_gdn.py:104-106). The README now "
         "says the wrapper is installed but bypassed; the 2e table carries the shadowing rows; "
         "the 2e summary traces both routes."),
        ("2 (substantive)", "README: 'The OLMo results are bf16 throughout and carry none of "
         "these caveats'", "fixed",
         f"Correct. Recomputed from data/olmo/cached_gen_*.json@{PIN}: diverging cases base "
         f"{_o_b3['div']}/{_o_b3['n']} (twice), SFT {_o_sft['div']}/{_o_sft['n']}, DPO "
         f"{_o_dpo['div']}/{_o_dpo['n']}, Instruct {_o_ins['div']}/{_o_ins['n']}; at DPO and "
         "Instruct every diverging case is uninjected. The record calls it KV-cache numerics "
         f"and ran the B-phase uncached ({loc('RESULTS.md', ocg_, ocg_ + 5)}; "
         f"{loc('RESULTS.md', ob_, ob_ + 1)}). The README sentence is replaced; section 3 adds "
         "the table and figure rows; F1 cites it as consistent with a path-level cause, labelled "
         "an analogy across systems."),
        ("3 (substantive)", "README states the superseded v2 rule 2 in the present tense",
         "fixed",
         f"Correct ({loc('CLAUDE.md', av3, av3 + 5)} vs {loc(V2, find(V2, '2. **Use the validated O(T²) uncached generation path whenever high-norm'), find(V2, '2. **Use the validated O(T²) uncached generation path whenever high-norm') + 9)}). "
         "The README now says the KL gate licensed sampled cached generation and, since "
         "September 2026, licenses first-token reads only; the clause map cites both, v2 marked "
         "superseded."),
        ("4 (minor)", "g1/g1r raw locators :6-7", "fixed",
         "Correct: `git show ... | cat -v` shows two bare CRs in line 2 (an HF progress bar), "
         "and text=True turned them into extra lines. `show()` now reads bytes and splits on "
         "b'\\n'; files on disk are read with newline=''. The locators now print :4-5, and the "
         "locator self-check below re-verifies every pinned locator in this raw."),
        ("5 (minor)", "Figures note attributes 'g1/g1r ... 7.11e-4 / 7.39e-4' to the block",
         "fixed", "Correct (grep of the block: no g1, g1r or 7.11e-4). The note now says the "
         "task text's, not the block's."),
        ("6 (minor)", "'the committed artifact was overwritten by g1r'", "fixed",
         f"Correct: `git log --all` on the path lists only {hist_all}, holding template_family "
         f"{first_tf!r}. Reworded: no g1 artifact was ever committed; the g1 script writes the "
         "same fixed path, so g1r's run replaced it on disk before the path entered git."),
        ("7 (minor)", "README's versions sentence is broader than its cited support", "fixed",
         f"Correct in substance, with two corrections to the finding's detail. (a) The version "
         f"field first enters the record at {first_lv} (oracle_rule26.json), not at the 2026-08-18 "
         f"re-run. (b) The record has one more log-only line: mlx-lm 0.31.3 at setup "
         f"({loc('archive/RESULTS-cycle1-2.md', c12_ - 1, c12_)}). Section 1a now states the "
         f"coverage ({len(lv_files)} artifacts, then log-only before {first_lv.split()[1]}; "
         + ("the cycle 1-4 logs state no MLX core version" if not core_archive else f"MLX core version in the cycle 1-4 logs: {core_archive}")
         + ") together with the computed-new install evidence; the README sentence is scoped "
         "to it."),
        ("8 (minor)", "archive/CLAUDE-cycle1-2.md:83 cited for the patch's purpose; "
         "'never describes the patch's mechanics'", "fixed",
         "Correct: line 83 is a g/β limitation. The d788bc3 code calls the VJP with "
         "return_gbeta=True and documents real gate gradients. The purpose row now cites only "
         "the upstream README; 2a quotes the code and calls the record's caveat stale against it; "
         "'never describes the mechanics' is softened to 'never describes how the patch routes "
         "the forward pass'."),
        ("9 (minor)", "F1's scope omits LoRA training", "fixed",
         "Correct, scoped: clone scripts c1_train_adapter.py (the c1 protocol's trainer per the "
         "record) and d_train_distill.py (named in no record line) set the mode off and compute "
         "the loss through `MLXLensModel.forward`, which passes cache=None, so on a static reading "
         "the custom function (fused forward, Metal VJP) is what training runs. F1 and the 2e "
         "summary now include training, with the record's own 'via the custom forward' line "
         "beside it."),
        ("10 (minor)", "2f's count of added files does not name its domain", "fixed",
         f"Correct. The scan is now a recursive walk of the clone's working tree (.git, .venv and "
         f"caches excluded): {len(added) if clone_ok else '?'} files absent from the index, by "
         f"area {by_area if clone_ok else '?'}; {len(added_py) if clone_ok else '?'} Python files; "
         f"the broader pattern (mx.fast., mx.checkpoint, any `.__call__ =`) gives "
         f"{len(kernel_hits) if clone_ok else '?'} hits. Code's own scratch walk of the clone "
         "(files only, no git command in the clone) found 482 / 57 / 0 before this fix."),
        ("11 (minor)", "Section 3 lists the passed g1r KLs as 'instances of the same floor'",
         "fixed", "Correct (results.{0.1,0.2}.pass = True). Reworded: the first-token gate passed; "
         "the T-step non-identities are the instances."),
        ("12 (minor)", "README: the choice-read check 'requires a KL of exactly 0.0'", "fixed",
         f"Correct ({loc(R_, find(R_, 'VERIFY_KL_BAR = 0.0'), find(R_, 'VERIFY_KL_BAR_E2A = 1e-6'))}; "
         f"{loc(RA, apr_ - 4, apr_)}). The README now says every e2a check measured exactly 0.0, with "
         "e2a's bar at 1e-6 and the core's at 0.0. The figure row adds the distinct-key count "
         "(N4(iii)'s 311)."),
        ("13 (minor)", "Floor-2 figure rows give no probe/layer scope", "fixed",
         "Correct. Every floor-2 row now carries the axis, the 12 probes x 6 workspace layers "
         "with its r1 locator, the fact that the r3 JSONs carry no such field, and 'no CV'."),
        ("14 (minor)", "--out refuses any path outside results/raw/; the command omits -B",
         "fixed", "Correct. Inside the repository only results/raw/ is writable; paths outside "
         "the repository are now allowed (for a verifier's scratch re-run). The command line is "
         "built from sys.orig_argv, so interpreter flags such as -B are recorded."),
    ]
    superseded = {"3 (substantive)": "see round 2, #5", "5 (minor)": "superseded by round 2, #9",
                  "7 (minor)": "superseded by round 2, #4", "11 (minor)": "superseded by round 2, #6"}
    w("## 11. Values-check (adversarial checks) -- dispositions")
    w("")
    w("### 11a. Pass 1")
    w("")
    w("The checker re-ran the script, re-derived 127 claims and raised 14 findings (3 "
      "substantive, 11 minor). Code re-checked each finding with its own tool runs before acting. "
      "Rows marked 'superseded' were changed again in round 2 (11b); their detail text is the "
      "pass-1 record.")
    w("")
    w("| # | finding | disposition | detail |")
    w("|---|---|---|---|")
    for n_, f_, d_, t_ in vc:
        w(f"| {n_} | {cell(f_)} | {d_} | {cell(t_)}"
          + (f" [{superseded[n_]}]" if n_ in superseded else "") + " |")
    w("")
    # ---------------- round 2 (residual findings of the tier-2/3 round-2 check) -------------
    n_after_no = len(after_) - len(after_lv)
    vc2 = [
        ("1 (substantive)", "Section 3 calls the OLMo first-token gate log-only with no artifact; F1 and "
         "section 3 say the OLMo divergences came after that gate had found the paths bit-identical, "
         "'the same shape as the Qwen floor'", "fixed",
         f"Correct. `{DB}`@{PIN}: stage {det['stage']!r}, C_kernel_path max_kl {ck['max_kl']}, "
         f"all_exact {ck['all_exact']}, {len(ck['rows'])} rows; commits {det_hist}; determinism "
         f"artifacts under data/olmo: {det_files}; every tracked `box_determinism.py --stage` call "
         f"names {stage_calls}; the {len(det_raws)} determinism raws load "
         f"{sorted({r.split('(model ')[1].split(';')[0] for r in raw_rows})}. At "
         f"SFT/DPO/Instruct the diverging cases' 0-based diverge_index values are {olmo_div_idx}. "
         "Section 3 now reproduces the gate (new figure row); its Reading and F1 say the gate ran on "
         "Base only, where multi-token generation also matched, and that at the other stages token 0 "
         "agreed and divergence came later. Code's own addition: the parallel is drawn to the Qwen "
         "T-step divergences (token 0 agreed in every divergent round, index "
         f"{min(tstep_div)}-{max(tstep_div)}), not to floor 1, because c1 smoke 1b diverged at index "
         f"{min(r['first'] for r in hi)}; and 'diverged near ties' is dropped for OLMo, where the "
         "record says KV-cache numerics. The README paragraph is unchanged by this finding."),
        ("2 (substantive)", "Section 5 / F6 / figure row: 'verified against an untouched model' is the "
         "note's phrase, with no source named", "fixed",
         f"Correct. Files on disk: {[(r[0], r[1], 'tracked' if r[2] else 'untracked', r[3], r[4]) for r in pre_rows]} "
         "(file, sha256 prefix, tracked, 'untouched model' lines, 'identical re-forward' lines). "
         + (f"Its count {um_src[3]} "
            f"{'equals' if um_src[3] == len(kl_keys0) else 'DIFFERS from'} g3prime_kl.jsonl's "
            f"distinct keys ({len(kl_keys0)}). " if um_src else "")
         + "Section 5 names the source and answers the block's question directly (the choice-read "
         "re-forward identity: same weights, quantization and patch, no vector, the forward compared "
         "with itself; neither 'no patch' nor a different model); F6 recommends the patch-v3 wording; "
         "the figure row keeps 'not found' for the phrase as a record term and names the source."),
        ("3 (minor)", "Header: 'a README sentence never depends on the clone'; row note: 'the README "
         "must not depend on it'", "fixed",
         "Correct: the patch-mechanics, 'not our code' and lab-edits clauses rest on clone reads. Both "
         "meta-claims are removed. The header and section 7 now say which README clauses rest on "
         f"computed-new reads ({len(cn_rows)} clause rows), which of them a reader can check against "
         "public sources (HF revision c000ac2c, upstream d788bc3, mlx-lm 0.31.3), and that the lab's "
         "clone edits are not in this repository."),
        ("4 (minor)", "README: the versions sentence is broader than the record for cycles 1-4",
         "fixed",
         "Correct that it was broader. The suggested wording ('every Qwen artifact from 2026-08-15 "
         f"on') is itself broader than the record: of {len(after_)} data/ JSON/JSONL files outside data/olmo/ first "
         f"added on or after {lv_day}, {n_after_no} record no versions; the {len(mid_files)} files that "
         f"record a model_id are exactly the {len(lv_files)} that record the versions "
         f"({set(mid_files) == set(lv_files)}). The README now reads 'the versions recorded by every "
         "Qwen artifact that names its model, the first committed on <date>; the environment's single "
         "install, dated at setup, and its single model snapshot are consistent with them throughout' "
         "(the script "
         "asserts one snapshot, one blob date and one dist-info per package). The revision clause row "
         f"adds the computed-new snapshot facts and the revision's first record commit, {first_rev}. "
         "The coverage figure row is split (finding 8)."),
        ("5 (minor)", "README: 'The lab's rules therefore require the uncached path ...' restates "
         "superseded v2 rule 2", "fixed",
         f"Correct ({loc(V2, find(V2, '2. **Use the validated O(T²) uncached generation path whenever high-norm'), find(V2, '2. **Use the validated O(T²) uncached generation path whenever high-norm') + 9)} "
         f"vs {loc('CLAUDE.md', av3, av3 + 5)}). Now 'required' (past tense); the next sentence "
         "already states the operative first-token / token-identity rule."),
        ("6 (minor)", "Section 3 labels the e2d T-step non-identities '(the floor's instances)'",
         "fixed",
         "Correct: the T-step rounds are sampled (temp 0.7) at frac 0.1 / 0.2, floor 1 is greedy at "
         "frac 1.0. Relabelled 'cached-vs-uncached divergences at the e2a dose (sampled; related to "
         "floor 1, not instances of it)', with the round domain from the artifacts (e2d-format rounds, "
         "PROPOSAL-j v1.2 AMENDMENT 2 (i), through the ported adapter) and the 0-based index "
         f"definition ({loc(TS, ts_k, ts_k + 3)})."),
        ("7 (minor)", "README states the near-tie mechanism as a measured fact", "fixed",
         f"Correct: the record's 'Read:' ({loc(P, a_read + 5, a_read + 6)}) is an interpretation and the "
         f"smoke raw has token ids only ({n_marg} lines mention a logit or margin). The README now says "
         "'The record reads this as ...'; section 3 and a clause row say so."),
        ("8 (minor)", "Figures table: no rows for '48 linear-attention layers' or 'd788bc3'; the "
         "coverage row mixes statuses", "fixed",
         "Correct. Added a log-only (record) and a computed-new (local config / clone refs) row for "
         "each; split the coverage row into 'artifacts' (reproduced) and 'before 2026-08-15' "
         "(log-only). Round 2 also adds the OLMo first-token gate row (finding 1)."),
        ("9 (minor)", "F4 and the g1 row cite 'the task text', which is not in the record", "fixed",
         "Correct (the block has no g1, g1r or 7.11e-4). The attribution is dropped in F4 and in the "
         "g1 row note; the substance stays (both values are g1r's; g1 failed at 1.31e-3 / 1.15e-3)."),
        ("10 (minor)", "The builder's summary ('28 figure rows: 14 reproduced, ...') is stale",
         "disclosed",
         "Correct about the summary, which is not part of this item's files. This raw's counts are "
         f"computed from its own table on every run (section 8; this run: {len(figs)} rows, {counts}). "
         "N1's ledger "
         "should read the raw's table, not a summary."),
    ]
    w("### 11b. Round 2")
    w("")
    w(f"The round-2 check left {len(vc2)} residual findings (2 substantive, {len(vc2) - 2} minor). "
      "Code re-checked each with its own tool runs (git show / git grep / git log at the pin, the "
      "preprint drafts and the clone read as files) before acting; every number in the detail column "
      "is printed by this run.")
    w("")
    w("| # | finding | disposition | detail |")
    w("|---|---|---|---|")
    for n_, f_, d_, t_ in vc2:
        w(f"| {n_} | {cell(f_)} | {d_} | {cell(t_)} |")
    w("")
    # locator self-check over everything written so far
    body = "\n".join(out)
    nloc, bad_range, bad_quote, nquote = 0, [], [], 0
    for m in re.finditer(r"([A-Za-z0-9_./\-]+\.(?:md|txt|py|json|jsonl))@" + PIN +
                         r":(\d+)(?:-(\d+))?", body):
        path_, a_, b_ = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        nloc += 1
        try:
            ls_ = lines_of(path_)
        except Exception:
            bad_range.append(m.group(0))
            continue
        if not (1 <= a_ <= b_ <= len(ls_)):
            bad_range.append(m.group(0))
            continue
        tail = body[m.end():m.end() + 4]
        if tail[:3] in (': "', ": `"):
            qc = tail[2]
            qs = body[m.end() + 3:m.end() + 3 + 400]
            qs = qs.split(qc, 1)[0].split("...", 1)[0]
            qs = " ".join(qs.split())[:50]
            span_txt = " ".join(" ".join(ls_[a_ - 1:b_]).split())
            if qs:
                nquote += 1
                if qs not in span_txt:
                    bad_quote.append(m.group(0))
    w(f"Locator self-check (this run, over sections 0-11b above): {nloc} pinned locators "
      f"`path@{PIN}:a[-b]`; out of range: {bad_range if bad_range else 'none'}; "
      f"{nquote} quotes that directly follow a locator, each prefix-matched (first 50 "
      f"normalized characters) against the pinned lines: mismatches "
      f"{bad_quote if bad_quote else 'none'}.")
    w("")

    # ------------------- 12. round 9: the preprint of record (ruling 9, as corrected)
    # Every check this script makes of a preprint sentence, re-run on the patched
    # text. The audited side is anchored on this item's raw as committed (R0@R0c);
    # the archived audited copy is read only if present and matching the block's
    # reference (P-b/P-c full scan; quoted beside the patched lines). A failed
    # check is a finding on the patch, never a STOP.
    R0, R0c = RAW_AUDITED
    nrm = lambda s: " ".join(s.split())  # noqa: E731
    ints = lambda s: [int(x) for x in s.replace(" ", "").split(",") if x]  # noqa: E731
    b21 = find(BLOCK, f"sha `{PREPRINT_SHA_BLOCK_PREFIX}")
    mb = re.search(r"`" + re.escape(PREPRINT) + r"` at root \([^)]*\)", lines_of(BLOCK)[b21 - 1])
    r90 = find(R0, f"- `{PREPRINT}` (UNTRACKED; sha256 `", commit=R0c)
    r235 = find(R0, "- Where the phrase comes from (files on disk, not record):", commit=R0c)
    m90 = re.search(r"sha256 `([0-9a-f]{16})\.\.\.`.*?\) :(\d+): \"(.*)\"$", lines_of(R0, R0c)[r90 - 1])
    m235 = re.search(r"\('" + re.escape(PREPRINT) + r"', '([0-9a-f]{16})', (?:True|False), "
                     r"\[([0-9, ]*)\], \[([0-9, ]*)\]\)", lines_of(R0, R0c)[r235 - 1])
    pl = file_lines(pp) if os.path.exists(pp) else []
    psha_ = sha256_file(pp) if pl else None
    apath = os.path.join(REPO, PREPRINT_AUDITED)
    asha = sha256_file(apath) if os.path.exists(apath) else None
    al = file_lines(apath) if (asha and asha.startswith(PREPRINT_SHA_BLOCK_PREFIX)
                               and asha.endswith(PREPRINT_SHA_BLOCK_SUFFIX)) else None
    s12 = len(out)  # section 12's own locator self-check starts here
    w("## 12. Rounds 9 and 10: the preprint of record (the PI's ruling 9 of 2026-10-10, as "
      "corrected; the PI's routing of 2026-10-12)")
    w("")
    w(f"- Preprint of record: `{PREPRINT}` (UNTRACKED here; committed at the tag per the ruling) "
      f"sha256 `{psha_}`: {'MATCH' if psha_ == PREPRINT_SHA else 'MISMATCH'} vs the PI's routing "
      f"of 2026-10-12 (patch v7) `{PREPRINT_SHA}` (asserted in section 2a); "
      f"{len(pl) - (pl[-1:] == [''])} lines. Round 9's preprint of record, patch v6 "
      f"`{PREPRINT_SHA_V6}`, is the pre-patch copy the PI's routing of 2026-10-12 places at "
      f"`{PREPRINT_V6}`, out of the release (recorded, never required; whether it is on disk and "
      "matching: 12a).")
    w(f"- Audited, superseded text: the block's reference, {loc(BLOCK, b21)}: "
      f"\"{mb.group(0) if mb else '?'}\"; this item's raw as committed printed its sha256 prefix "
      f"`{m90.group(1)}` ({loc(R0, r90, commit=R0c)}). Archived untracked at `{PREPRINT_AUDITED}`, out "
      "of the release, never required: "
      + (f"present, sha256 `{asha[:16]}...`, "
         + ("matching the block's reference; its lines are quoted below beside the patched ones."
            if al else "NOT matching the block's reference; not used.") if asha else "absent; not used."))
    w("")
    old_l, old_s = int(m90.group(2)), m90.group(3)
    head_ = nrm(old_s)[:40]
    cand = [i for i, x in enumerate(pl, start=1) if head_ in nrm(x)]
    new_l = cand[0] if cand else None
    same_s = bool(new_l) and nrm(old_s) in nrm(" ".join(pl[new_l - 1:new_l + 2]))

    def lines_with(ls, needle, ci=False):
        return [i for i, x in enumerate(ls, start=1)
                if (needle.lower() in x.lower() if ci else needle in x)]

    def verdict(old, new):
        if old == new:
            return "unchanged"
        if len(old) == len(new) and new:
            return "re-anchored " + ", ".join(f":{a} -> :{b}" for a, b in zip(old, new))
        return "changed by the patch"

    checks = []  # (id, phrase, where used here, audited lines, audited source, patched lines, result)
    checks.append(("P-a", "the limitations sentence 'Qwen ran at ... first external-validity step.'",
                   "section 2a (quoted)", [old_l], loc(R0, r90, commit=R0c), [new_l] if same_s else [],
                   ("unchanged" if new_l == old_l else f"re-anchored :{old_l} -> :{new_l}") if same_s
                   else "changed by the patch"))
    for cid, phr, used in [("P-b", "custom kernel patch", "section 2a (closing sentence), F2"),
                           ("P-c", "deterministic sub-0.05-cosine label geometry", "section 4 (Reading), F3")]:
        nl_ = lines_with(pl, phr)
        if al:  # full scan of the audited text itself
            ol_, src_ = lines_with(al, phr), f"full scan of `{PREPRINT_AUDITED}`, matching the block's reference"
        else:   # inferred from the raw's quoted sentence
            ol_ = [old_l] if phr in old_s else []
            src_ = f"{loc(R0, r90, commit=R0c)} (within the quoted :{old_l} sentence)"
        checks.append((cid, phr, used, ol_, src_, nl_, verdict(ol_, nl_)))
    for cid, phr, used, grp, ci in [
            ("P-d", "verified by an identical re-forward of the choice computation",
             "section 5, F6 (the recommended wording, at its patched line)", 3, False),
            ("P-e", "untouched model",
             "section 5 and the figure row (which describe it as the preprint's earlier wording, "
             "replaced at patch v3), F6",
             2, True)]:
        ol_ = ints(m235.group(grp)) if m235 else []
        nl_ = lines_with(pl, phr, ci)
        checks.append((cid, phr, used, ol_, f"{loc(R0, r235, commit=R0c)} (row `{PREPRINT}`, "
                       f"`{m235.group(1) if m235 else '?'}`)", nl_, verdict(ol_, nl_)))
    w("Every check this script makes of a preprint sentence, audited text (as this item's raw "
      "recorded it; P-b and P-c by a full scan of the archived copy when it is present and matching, "
      "else from the raw's quoted sentence) vs the patched text (patch v7, this run):")
    w("")
    w("| # | sentence / phrase | used in this raw | audited lines (source) | patched lines | result |")
    w("|---|---|---|---|---|---|")
    for c_ in checks:
        w(f"| {c_[0]} | {cell(c_[1])} | {cell(c_[2])} | {c_[3]} ({cell(c_[4])}) | {c_[5]} | {c_[6]} |")
    w("")
    pfind = []
    for c_ in checks:
        if c_[6] != "changed by the patch":
            continue
        ls_ = sorted(set(c_[3]) ^ set(c_[5])) or [old_l]
        pairs_ = []
        for L in ls_:
            o_ = (f"audited :{L} (archived copy): \"{nrm(al[L - 1])}\"" if al and L <= len(al)
                  else f"audited :{L}: not quoted in {R0}@{R0c} and the archived copy is not available")
            n_ = (f"patched :{L}: \"{nrm(pl[L - 1])}\"" if L <= len(pl) else f"patched :{L}: past end of file")
            pairs_.append(f"{o_}; {n_}")
        pfind.append(dict(id=f"P{len(pfind) + 1}", check=c_[0], phrase=c_[1], used=c_[2],
                          audited=c_[3], patched=c_[5], lines=pairs_))
    w("Findings on the patch, for the design seat (the PI's ruling 9 of 2026-10-10: a check of a "
      "preprint sentence that fails on the patched text is a finding on the patch, not a STOP): "
      + ("none." if not pfind else f"{len(pfind)}."))
    for f_ in pfind:
        extra = ""
        if f_["check"] == "P-e":
            pd_ = next(c_ for c_ in checks if c_[0] == "P-d")[5]
            if f_["patched"] and all(L in pd_ and re.search(r"re-forward\w* on an untouched model",
                                                             pl[L - 1], re.I) for L in f_["patched"]):
                extra = (f" Code's reading of patched {', '.join(f':{L}' for L in f_['patched'])}, offered "
                         "because each such line also carries P-d's phrase and uses this one as "
                         "'re-forwarded on an untouched model': section 5's reading of the phrase applies "
                         "unchanged, the choice-read re-forward identity (same weights, 4-bit quantization "
                         "and port patch, no vector, the forward compared with itself), not a different or "
                         "unpatched model; the patch-v3 wording F6 recommends is still on the same line (P-d).")
            else:
                extra = (" Not every patched line with the phrase also carries P-d's phrase and uses this "
                         "one as 're-forwarded on an untouched model'; no reading of the patched wording is "
                         "offered here.")
        w(f"- {f_['id']} ({f_['check']}, '{f_['phrase']}'; bears on {f_['used']}). Audited lines "
          f"{f_['audited']}, patched lines {f_['patched']}.{extra} "
          + " | ".join(f_["lines"]))
    w("")
    w(f"Round-9 preprint checks: {len(checks)}; "
      f"unchanged {sum(c_[6] == 'unchanged' for c_ in checks)}, "
      f"re-anchored {sum(c_[6].startswith('re-anchored') for c_ in checks)}, "
      f"changed by the patch {sum(c_[6] == 'changed by the patch' for c_ in checks)}. "
      "In sections 1-11 the preprint of record supplies only the 2a quote, its row in the drafts "
      "listing (section 5; 11b row 2) and F6's locator; no figure value, status or count is "
      "computed from it. Section 5's earlier-wording source is chosen from the archived drafts only "
      "(round 9): "
      + (f"`{um_src[0]}`:{um_src[1]}." if um_src else
         "none on disk carries the phrase, so section 5 names no earlier-wording source."))
    w("")
    assert um_src is None or um_src[0] != PREPRINT

    # ------------------- 12a. round 10: patch v7 (the PI's routing of 2026-10-12)
    # Round 9's findings on the patch, as this item's raw recorded them at R9c, each
    # given its disposition on v7; every check that passed on v6 and fails on v7; the
    # figures of each v7-changed line the checks read, those in this script's scope
    # verified against its own record sources (section 5 item 2). The v6 side is
    # anchored on the round-9 raw; the archived v6 copy is read only if present and
    # matching, to quote a v6 line beside its v7 line. A failure is a finding on the
    # patch for the design seat, never a STOP.
    R9, R9c = RAW_ROUND9
    r9l = lines_of(R9, R9c)
    r9s = find(R9, "## 12. Round 9: the preprint of record", commit=R9c)
    r9p = find(R9, "- Preprint of record: `", start=r9s, commit=R9c)
    m9p = re.search(r"sha256 `([0-9a-f]{64})`: MATCH", r9l[r9p - 1])
    v6_sha_raw = m9p.group(1) if m9p else None
    r9a = find(R9, f"- `{PREPRINT}` (UNTRACKED; sha256 `", commit=R9c)
    m9a = re.search(r"sha256 `([0-9a-f]{16})\.\.\.`.*?\) :(\d+): \"(.*)\"$", r9l[r9a - 1])
    v6q: dict = {}  # v6 line -> (text as the round-9 raw quoted it, raw line)
    if m9a:
        v6q[int(m9a.group(2))] = (m9a.group(3), r9a)
    r9rows: dict = {}
    r9find: list = []
    for i, ln in enumerate(r9l, start=1):
        if i <= r9s:
            continue
        mr = re.match(r"^\| (P-[a-e]) \|.*\| (\[[0-9, ]*\]) \| ([^|]+) \|$", ln)
        if mr:
            r9rows[mr.group(1)] = (ints(mr.group(2).strip("[]")), mr.group(3).strip(), i)
        mf = re.match(r"^- (P\d+) \((P-[a-e]), '([^']*)'; .*?Audited lines (\[[0-9, ]*\]), "
                      r"patched lines (\[[0-9, ]*\])\.", ln)
        if mf:
            r9find.append(dict(id=mf.group(1), check=mf.group(2), phrase=mf.group(3),
                               audited=ints(mf.group(4).strip("[]")),
                               v6=ints(mf.group(5).strip("[]")), raw_line=i))
            for mq in re.finditer(r'patched :(\d+): "(.*?)"(?= \| audited|$)', ln):
                v6q.setdefault(int(mq.group(1)), (mq.group(2), i))
    v6path = os.path.join(REPO, PREPRINT_V6)
    v6sha = sha256_file(v6path) if os.path.exists(v6path) else None
    v6l = file_lines(v6path) if v6sha == PREPRINT_SHA_V6 else None

    def v6_text(L):
        if v6l is not None:
            return (nrm(v6l[L - 1]) if L <= len(v6l) else None), "archived copy"
        if L in v6q:
            return nrm(v6q[L][0]), f"as quoted at {loc(R9, v6q[L][1], commit=R9c)}"
        return None, f"not quoted in {R9}@{R9c} and the archived copy is not available"

    def line_changed(L):
        t6, _ = v6_text(L)
        if t6 is None:
            return None
        if v6l is not None:
            return L > len(pl) or v6l[L - 1] != pl[L - 1]
        return t6 not in nrm(" ".join(pl[L - 1:L + 2]))

    if v6l is not None:
        chg_all = [i for i in range(1, max(len(v6l), len(pl)) + 1)
                   if (v6l[i - 1] if i <= len(v6l) else None) != (pl[i - 1] if i <= len(pl) else None)]
    else:
        chg_all = None
    read_ = sorted({L for c_ in checks for L in c_[5]} | {L for v in r9rows.values() for L in v[0]})
    read_chg = [L for L in read_ if line_changed(L)]
    read_unk = [L for L in read_ if line_changed(L) is None]
    w("### 12a. Round 10: patch v7 (the PI's routing of 2026-10-12)")
    w("")
    w(f"- Patch v6, round 9's preprint of record: sha256 `{v6_sha_raw}` as this item's raw printed it at "
      f"round 9 ({loc(R9, r9p, commit=R9c)}; {'equal to' if v6_sha_raw == PREPRINT_SHA_V6 else 'DIFFERENT from'} "
      f"this script's record of it). At the routing's path `{PREPRINT_V6}` (untracked, out of the "
      "release, never required): "
      + (f"present, sha256 `{v6sha[:16]}...`, "
         + ("matching; its lines are quoted below beside v7's." if v6l is not None
            else "NOT matching; not used (the round-9 raw's quotes stand in).") if v6sha
         else "absent; not used (the round-9 raw's quotes stand in)."))
    w("- Lines v7 changes against v6 (line-for-line comparison of the archived copy): "
      + (f"{chg_all} (v6 {len(v6l) - (v6l[-1:] == [''])} lines, v7 {len(pl) - (pl[-1:] == [''])} lines)"
         if chg_all is not None else "not computed (the archived copy is not available)")
      + f". Lines this script's preprint checks read on v6 or v7: {read_}; of these, changed by v7: "
      + f"{read_chg}" + (f"; undecidable without the archived copy: {read_unk}" if read_unk else "") + ".")
    w("")
    w(f"Round 9's checks on v6 (as this item's raw recorded them, {loc(R9, r9s, commit=R9c)} ff.) and on "
      "v7 (this run, the table above), each against the audited text:")
    w("")
    w("| # | v6 lines | v6 result | v7 lines | v7 result | passed on v6, fails on v7 |")
    w("|---|---|---|---|---|---|")
    c7 = {c_[0]: c_ for c_ in checks}
    newly = []
    for c_ in checks:
        r6 = r9rows.get(c_[0])
        nf = bool(r6) and r6[1] != "changed by the patch" and c_[6] == "changed by the patch"
        if nf:
            newly.append(c_[0])
        w(f"| {c_[0]} | {r6[0] if r6 else '?'} | {r6[1] if r6 else 'not in the round-9 raw'} | {c_[5]} | "
          f"{c_[6]} | {'YES' if nf else 'no'} |")
    w("")
    disp = []
    for f_ in r9find:
        c_ = c7.get(f_["check"])
        v7l = c_[5] if c_ else []
        res7 = c_[6] if c_ else "check absent"
        ls_ = sorted(set(f_["v6"]) | set(v7l))
        ch_ = [L for L in ls_ if line_changed(L)]
        if res7 != "changed by the patch":
            d_ = (f"resolved: the check passes on v7 (result '{res7}': audited lines {f_['audited']}, "
                  f"v7 lines {v7l})")
        elif v7l == f_["v6"] and not ch_:
            d_ = "unchanged"
        else:
            d_ = "changed"
        qs_ = []
        for L in ch_:
            t6, s6 = v6_text(L)
            qs_.append(f"v6 :{L} ({s6}): \"{t6}\"; v7 :{L}: "
                       + (f"\"{nrm(pl[L - 1])}\"" if L <= len(pl) else "past end of file"))
        disp.append(dict(id=f_["id"], check=f_["check"], phrase=f_["phrase"], v6=f_["v6"], v7=v7l,
                         disposition=d_.split(":", 1)[0], detail=d_, raw_line=f_["raw_line"], lines=qs_))
    w(f"Round 9's findings on the patch ({len(r9find)}, as this item's raw recorded them), each with its "
      "disposition on v7:")
    for d_ in disp:
        w(f"- {d_['id']} ({d_['check']}, '{d_['phrase']}'; {loc(R9, d_['raw_line'], commit=R9c)}). v6 lines "
          f"{d_['v6']}, v7 lines {d_['v7']}. Disposition: {d_['detail']}."
          + (" " + " | ".join(d_["lines"]) if d_["lines"] else ""))
    if not disp:
        w("- none recorded.")
    w("")
    # figures of each v7-changed line the checks read, against this script's record sources
    pd7 = c7["P-d"][5] if "P-d" in c7 else []
    apr10 = find(RA, "KL(choice forward ‖ vanilla forward, same text) ≤ 1e-6")
    rb10 = find(R_, "VERIFY_KL_BAR_E2A = 1e-6")
    fig10, fail10 = [], []
    for L in read_chg:
        t7 = nrm(pl[L - 1]) if L <= len(pl) else ""
        t6, s6 = v6_text(L)
        if L not in pd7:
            fail10.append(dict(line=L, figure="(whole line)", why="v7 changes a line this script reads "
                               "outside the re-forward sentence; its figures are not verified here"))
            continue
        m311 = re.search(r"(\d[\d,]*) distinct verified reads", t7)
        ok311 = bool(m311) and int(m311.group(1).replace(",", "")) == len(kl_keys0)
        fig10.append((L, f"'{m311.group(0) if m311 else 'N distinct verified reads'}'",
                      "yes, the count (section 5 item 2 prints it; the 311-distinct / 360-row / "
                      "281-of-1115 reading is N4(iii)'s)",
                      f"`data/e2a/g3prime_kl.jsonl`@{PIN}: {len(kl_keys0)} distinct (arm, session, choice) "
                      "keys (section 5 item 2) [reproduced]", ok311))
        mkl = re.search(r"symmetric KL = 0 exactly", t7)
        okkl = bool(mkl) and all(r["kl"] == 0.0 for r in kl0_rows) and max(r["kl"] for r in kl0_rows) == 0.0
        fig10.append((L, "'symmetric KL = 0 exactly'", "yes (section 5 item 2)",
                      f"`data/e2a/g3prime_kl.jsonl`@{PIN}: {sum(r['kl'] == 0.0 for r in kl0_rows)} of "
                      f"{len(kl0_rows)} rows with kl == 0.0, max {max(r['kl'] for r in kl0_rows)} [reproduced]",
                      okkl))
        mb6 = re.search(r"10⁻⁶ bound", t7)
        fig10.append((L, "'a 10⁻⁶ bound'", "yes (section 5 item 2)",
                      f"{loc(RA, apr10)}: `KL(choice forward ‖ vanilla forward, same text) ≤ 1e-6` "
                      f"[log-only]; {loc(R_, rb10)}: `VERIFY_KL_BAR_E2A = 1e-6`", bool(mb6)))
        for pat_ in (r"\d[\d,]* of the \d[\d,]* choice reads \(every fourth\)",
                     r"counting the two smoke runs"):
            mo_ = re.search(pat_, t7)
            fig10.append((L, f"'{mo_.group(0) if mo_ else pat_}'",
                          "no: section 5 item 2 leaves the 311-distinct / 360-row / 281-of-1115 "
                          "reading to N4(iii)",
                          "not checked here; on v6 :%d identically: %s" % (L, bool(mo_) and bool(t6)
                                                                          and mo_.group(0) in t6), None))
        for f10 in fig10:
            if f10[0] == L and f10[4] is False:
                fail10.append(dict(line=L, figure=f10[1], why="not carried at the precision written by "
                                   + f10[3]))
    w("Figures of each v7-changed line the checks read, those in this script's scope verified against its "
      "own record sources (the values section 5 item 2 prints this run):")
    w("")
    if fig10:
        w("| v7 line | figure | in this script's scope | record source (this run) | carried at the precision written |")
        w("|---|---|---|---|---|")
        for f10 in fig10:
            w(f"| :{f10[0]} | {cell(f10[1])} | {cell(f10[2])} | {cell(f10[3])} | "
              f"{'n/a' if f10[4] is None else ('yes' if f10[4] else 'NO')} |")
    else:
        w("- none (v7 changes no line the checks read).")
    w("")
    rw_ = []
    for L in read_chg:
        if L not in pd7:
            continue
        t6, _ = v6_text(L)
        t7 = nrm(pl[L - 1])
        mw6 = re.search(r"were re-forwarded (.*?) at symmetric KL", t6 or "")
        mw7 = re.search(r"were re-forwarded (.*?) at symmetric KL", t7)
        hold = [p_ for p_ in ("same weights", "no vector", "compared with itself") if p_ in t7]
        rw_.append(dict(line=L, v6=mw6.group(1) if mw6 else None, v7=mw7.group(1) if mw7 else None,
                        holds=hold, pd=L in pd7, untouched="untouched model" in t7.lower()))
        full_ = len(hold) == 3 and L in pd7 and not rw_[-1]["untouched"]
        w(f"The re-forward wording at v7 :{L} (no figure): v6 \"were re-forwarded "
          f"{mw6.group(1) if mw6 else '?'}\" -> v7 \"were re-forwarded {mw7.group(1) if mw7 else '?'}\". "
          f"Of what section 5 item 2 holds fixed or compares (same weights, quantization and patch, NO "
          f"vector; a vanilla forward compared with itself) it names {hold}; P-d's phrase on the same "
          f"line: {L in pd7}; 'untouched model' on it: {rw_[-1]['untouched']}. "
          + ("Code's reading: it states the choice-read re-forward identity section 5 describes; "
             "not a finding." if full_ else
             "Code offers no reading of it here."))
        w("")
    nf10 = [dict(kind="check newly failing on v7", check=c) for c in newly] + \
           [dict(kind="figure on a v7-changed line", **f) for f in fail10]
    w("New findings on the patch (v7), for the design seat (as in round 9, a check of a preprint "
      "sentence that fails on the patched text is a finding on the patch, not a STOP): "
      + ("none." if not nf10 else f"{len(nf10)}."))
    for i_, f_ in enumerate(nf10, start=1):
        w(f"- P10-{i_} ({f_['kind']}): " + (f"check {f_['check']} passed on v6 and fails on v7."
                                             if "check" in f_ else f":{f_['line']} {f_['figure']}: {f_['why']}."))
    w("")
    w(f"Round-10 summary: round 9's findings on the patch {len(disp)} (resolved "
      f"{sum(d_['disposition'] == 'resolved' for d_ in disp)}, unchanged "
      f"{sum(d_['disposition'] == 'unchanged' for d_ in disp)}, changed "
      f"{sum(d_['disposition'] == 'changed' for d_ in disp)}); checks newly failing on v7 {len(newly)}; "
      f"v7-changed lines the checks read {read_chg}; new findings on the patch {len(nf10)}. As round 9 "
      "found for the preprint of record, no figure value, status or count in sections 1-11 is computed "
      "from v7. The archived v6 copy is named in 2a's identity line, from this script's constants "
      "(not read there)" + ("; on disk, it is read in sections 1-11 only as a row of section 5's "
                            "drafts listing (and 11b row 2)." if v6sha else
                            "; not on disk, it has no row in section 5's drafts listing."))
    w("")
    # section 12's own locator self-check (the 0-11b self-check above does not cover it)
    body12 = "\n".join(out[s12:])
    n12, r12, q12, nq12 = 0, [], [], 0
    for m in re.finditer(r"([A-Za-z0-9_./\-]+\.(?:md|txt|py|json|jsonl))@(" + PIN + "|" + R0c + "|" + R9c +
                         r"):(\d+)(?:-(\d+))?", body12):
        path_, c12, a_, b_ = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
        n12 += 1
        try:
            ls_ = lines_of(path_, c12)
        except Exception:
            r12.append(m.group(0))
            continue
        if not (1 <= a_ <= b_ <= len(ls_)):
            r12.append(m.group(0))
            continue
        tail = body12[m.end():m.end() + 4]
        if tail[:3] in (': "', ": `"):
            qc = tail[2]
            qs = body12[m.end() + 3:m.end() + 3 + 400].split(qc, 1)[0].split("...", 1)[0]
            qs = " ".join(qs.split())[:50]
            if qs:
                nq12 += 1
                if qs not in " ".join(" ".join(ls_[a_ - 1:b_]).split()):
                    q12.append(m.group(0))
    w(f"Section-12 locator self-check (this run): {n12} pinned locators `path@{PIN}:a[-b]`, "
      f"`path@{R0c}:a[-b]` or `path@{R9c}:a[-b]`; out of range: {r12 if r12 else 'none'}; {nq12} quotes that directly "
      f"follow a locator, each prefix-matched (first 50 normalized characters) against the pinned "
      f"lines: mismatches {q12 if q12 else 'none'}.")
    w("")
    p9 = dict(preprint=PREPRINT, sha256=psha_, ruling9_sha256=PREPRINT_SHA_V6,
              match=psha_ == PREPRINT_SHA_V6,
              computed_on=("checks and findings_on_patch are computed on this run's text (sha256 "
                           "above; patch v7 when it matches preprint_round10.routing_2026_10_12_sha256), "
                           "not on patch v6; earlier_wording_source and selfcheck are this run's too; "
                           "round 9's own findings on patch v6, with their dispositions on v7, are "
                           "preprint_round10.round9_findings"),
              audited_ref=f"{PREPRINT_SHA_BLOCK_PREFIX}…{PREPRINT_SHA_BLOCK_SUFFIX}",
              audited_archive=PREPRINT_AUDITED, audited_archive_used=bool(al),
              checks=[dict(zip(("id", "phrase", "used", "audited", "audited_source", "patched",
                                "result"), c_)) for c_ in checks],
              findings_on_patch=pfind,
              earlier_wording_source=(list(um_src[:2]) if um_src else None),
              selfcheck=dict(locators=n12, out_of_range=r12, quotes=nq12, mismatches=q12))
    p10 = dict(preprint=PREPRINT, sha256=psha_, routing_2026_10_12_sha256=PREPRINT_SHA,
               match=psha_ == PREPRINT_SHA,
               v6_sha256=PREPRINT_SHA_V6, v6_sha256_round9_raw=v6_sha_raw,
               v6_archive=PREPRINT_V6, v6_archive_used=v6l is not None,
               round9_raw=f"{R9}@{R9c}",
               v7_changed_lines=chg_all, read_lines=read_, read_lines_changed=read_chg,
               checks=[dict(id=c_[0], v6=(r9rows[c_[0]][0] if c_[0] in r9rows else None),
                            v6_result=(r9rows[c_[0]][1] if c_[0] in r9rows else None),
                            v7=c_[5], v7_result=c_[6], newly_failing=c_[0] in newly)
                       for c_ in checks],
               round9_findings=disp,
               figures_changed_lines=[dict(line=f10[0], figure=f10[1], in_scope=f10[2], source=f10[3],
                                           carried=f10[4]) for f10 in fig10],
               reforward_wording=rw_,
               new_findings_on_patch=nf10)

    text = "\n".join(out)

    def allowed(p: str) -> bool:
        # Inside the repository only results/raw/ is writable; any path outside
        # the repository (e.g. a scratch directory for a verifier's re-run) is
        # allowed (values-check finding 14).
        rp = os.path.realpath(p)
        repo = os.path.realpath(REPO)
        if rp == repo or rp.startswith(repo + os.sep):
            return rp.startswith(os.path.join(repo, "results", "raw") + os.sep)
        return True

    outp = os.path.join(REPO, args.out) if not os.path.isabs(args.out) else args.out
    if not allowed(outp):
        raise SystemExit("refusing: inside the repository --out must be under results/raw/")
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    if args.json_out:
        jp = os.path.join(REPO, args.json_out) if not os.path.isabs(args.json_out) else args.json_out
        if not allowed(jp):
            raise SystemExit("refusing: inside the repository --json-out must be under results/raw/")
        with open(jp, "w", encoding="utf-8") as fh:
            json.dump(dict(item="N17", pin=PIN, figures=figs, flags=notes,
                           paragraph=para, clause_map=clause_map,
                           preprint_round9=p9, preprint_round10=p10), fh, indent=1)
    shown = os.path.relpath(outp, REPO) if os.path.realpath(outp).startswith(os.path.realpath(REPO) + os.sep) else outp
    print(f"wrote {shown} ({len(text.splitlines())} lines); "
          f"figures {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
