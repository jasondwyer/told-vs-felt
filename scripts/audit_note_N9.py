#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N9: the weight channel ((d)/e1).

Reproduces, from the committed gate artifacts data/d/gates_rep{A,B}.json read
at the pin, the figures the block lists for N9 (block :109-110): the oriented
G1 cosines 0.476 / 0.435, the control ceilings (~0.05), the d2 leakage gate's
bound, and the 17x / 10x exceedances (stating what is divided by what). It
names, for each cosine, the readout, the layers, the contrast and the control
set, and pins every log locator to the pin commit.

Read-only on the record. Reads committed files with `git show <pin>:<path>`
(git runs only in this repository, never inside jlens-qwen36/), reads the
gitignored jlens-qwen36 clone's gate code as plain files (local context, not
record), and writes only --out and --json-out. No model, no tokenizer, no
inference; stdlib arithmetic (fractions) on the stored decimal fields.

Usage (from the repository root):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N9.py \
      [--out results/raw/2026-10-08_note-N9-weight.md] \
      [--json-out results/raw/2026-10-08_note-N9-weight.json]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shlex
import struct
import subprocess
import sys
from decimal import (Decimal, ROUND_CEILING, ROUND_DOWN, ROUND_HALF_DOWN,
                     ROUND_HALF_EVEN, ROUND_HALF_UP)
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
ROUTED = ("8cd8a9ac", "3841")
ITEM_LINES = (109, 110)
ARCH = "archive/RESULTS-cycles3-4.md"
ARCH12 = "archive/RESULTS-cycle1-2.md"
F3 = "FINDINGS-3.md"
PROP = "PROPOSAL-d-distilled-trace.md"
GATES = {"A": "data/d/gates_repA.json", "B": "data/d/gates_repB.json"}
RAWS = {"A": "results/raw/2026-08-10_d_gates_A.txt",
        "B": "results/raw/2026-08-10_d_gates_B.txt",
        "A_smoke": "results/raw/2026-08-10_d_gates_A_smoke.txt"}
RAW_CACHE = "results/raw/2026-08-10_d_cache.txt"
RAW_LAYERMAP = "results/raw/2026-08-10_d_layermap.txt"
RAW_TRAIN = {"A": "results/raw/2026-08-10_d_train_A.txt",
             "B": "results/raw/2026-08-10_d_train_B.txt",
             "smoke": "results/raw/2026-08-10_d_train_smoke.txt"}
E2A_SESS = "data/e2a/sessions.jsonl"
PREPRINT = "PREPRINT-v1_0-draft.md"            # untracked at root
PREPRINT_SHA = ("d6431e97", "222b8")
NOTE = "RESEARCH-NOTE-v0_2-draft.md"
CLONE = REPO / "jlens-qwen36"                   # gitignored; files only
LOCAL = {"d_gates": CLONE / "scripts/d_gates.py",
         "c1_gate": CLONE / "scripts/c1_gate.py",
         "conditioning": CLONE / "jlens_qwen/conditioning.py",
         "e2a": CLONE / "jlens_qwen/e2a.py",
         "fingerprint": CLONE / "jlens_qwen/fingerprint.py",
         "lens_npz": CLONE / "data/lens/neuronpedia_n1000.npz",
         "smoke_json": CLONE / "data/d/gates_repA_smoke.json"}


# ---------------------------------------------------------------- helpers
def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True,
                       check=True)
    return r.stdout if binary else r.stdout.decode("utf-8")


def show(path: str) -> bytes:
    return git("show", f"{PIN}:{path}", binary=True)


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def blob_id(b: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


_lines_cache: dict[str, list[str]] = {}


def pinned_lines(path: str) -> list[str]:
    if path not in _lines_cache:
        _lines_cache[path] = show(path).decode("utf-8").split("\n")
    return _lines_cache[path]


def locate(path: str, needle: str, pinned: bool = True) -> dict:
    """1-based line of the unique line containing `needle`."""
    lines = pinned_lines(path) if pinned else \
        (REPO / path).read_text(encoding="utf-8").split("\n")
    hits = [i + 1 for i, s in enumerate(lines) if needle in s]
    assert len(hits) == 1, (path, needle, hits)
    ln = hits[0]
    tag = f"{path}@{PIN}:{ln}" if pinned else f"{path} (working tree, untracked):{ln}"
    return {"locator": tag, "line": ln, "text": lines[ln - 1].strip()}


def F(x) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(str(x))


def f4(x, nd=4) -> str:
    return f"{float(x):.{nd}f}"


def f_down(x, nd=4) -> str:
    """Lower bounds are printed rounded DOWN (exact Fraction floor), so the
    printed figure is itself a valid lower bound (values-check finding 2)."""
    q = Fraction(10) ** nd
    return f"{float(Fraction(math.floor(F(x) * q)) / q):.{nd}f}"


def f_up(x, nd=4) -> str:
    """Upper bounds are printed rounded UP."""
    q = Fraction(10) ** nd
    return f"{float(Fraction(math.ceil(F(x) * q)) / q):.{nd}f}"


def floor_(x: Fraction) -> int:
    return math.floor(x)


def half_up(x: Fraction) -> int:
    return math.floor(x + Fraction(1, 2))


def bf16_spacing(x: float) -> float:
    """Gap to the next bfloat16 value above |x| (bf16 = the top 16 bits of a
    float32; round-to-nearest-even onto them, then step the last kept bit)."""
    b = struct.unpack("<I", struct.pack("<f", abs(x)))[0]
    b = (b + 0x7FFF + ((b >> 16) & 1)) & 0xFFFF0000
    lo = struct.unpack("<f", struct.pack("<I", b))[0]
    hi = struct.unpack("<f", struct.pack("<I", b + 0x10000))[0]
    return hi - lo


def out_refusal(p: Path, tracked: set) -> str | None:
    """None if the script may write `p`, else the reason it refuses."""
    if p.is_symlink():
        return f"refusing to write through a symlink: {p}"
    try:
        rel = p.resolve().relative_to(REPO.resolve())
    except ValueError:
        return None                                    # outside the repository
    if rel.parent != Path("results/raw"):
        return f"inside the repository only results/raw/ is writable: {rel}"
    if str(rel) in tracked:
        return f"refusing to overwrite a tracked file: {rel}"
    return None


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/raw/2026-10-08_note-N9-weight.md")
    ap.add_argument("--json-out",
                    default="results/raw/2026-10-08_note-N9-weight.json")
    args = ap.parse_args()
    # Relative paths resolve against the repository root; absolute paths are
    # kept (e.g. a scratch directory for a re-run). Inside the repository the
    # script writes only under results/raw/ and never over a tracked file;
    # outside it, anywhere (values-check finding 1: the pass-1 assert refused
    # every path outside results/raw/).
    out_md, out_js = REPO / args.out, REPO / args.json_out
    tracked_now = set(git("ls-files", "-z").split("\0"))
    for p in (out_md, out_js):
        why = out_refusal(p, tracked_now)
        if why:
            raise SystemExit(why)

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True,
                           check=True).stdout.strip()
    head = git("rev-parse", "HEAD").strip()
    pin_full = git("rev-parse", PIN).strip()
    block_b = show(BLOCK)
    block_sha = sha256(block_b)
    block_ok = block_sha.startswith(ROUTED[0]) and block_sha.endswith(ROUTED[1])
    block_lines = block_b.decode("utf-8").split("\n")
    n_block = len(block_b.decode("utf-8").splitlines())
    item_text = [block_lines[i - 1] for i in range(ITEM_LINES[0], ITEM_LINES[1] + 1)]
    assert item_text[0].startswith("### N9."), item_text[0]
    script_b = Path(__file__).read_bytes()
    command = shlex.join([sys.executable] + sys.argv)

    md: list[str] = []
    W = md.append
    J: dict = {"item": "N9", "title": "weight channel ((d)/e1)",
               "code_stamp_date_u": stamp, "head": head, "pin": pin_full,
               "block": {"path": BLOCK, "sha256": block_sha,
                         "routed_match": block_ok, "lines": n_block,
                         "item_lines": list(ITEM_LINES)},
               "script": {"path": "scripts/audit_note_N9.py",
                          "sha256": sha256(script_b)},
               "interpreter": f"{sys.executable} (Python {sys.version.split()[0]})",
               "command": command}

    W("# AUDIT-note-release v1.2 -- N9: weight channel ((d)/e1 installation gates, d2 leakage gate)")
    W("")
    W(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    W(f"- HEAD at run time: {head}  [run metadata; every record read below is pinned to {PIN}]")
    W(f"- Pin: {PIN} = {pin_full}")
    W(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_sha}` "
      f"({'MATCH' if block_ok else 'MISMATCH'} vs routed {ROUTED[0]}...{ROUTED[1]}); "
      f"{n_block} lines; item N9 = block lines {ITEM_LINES[0]}-{ITEM_LINES[1]}")
    W(f"- Script: `scripts/audit_note_N9.py` sha256 `{sha256(script_b)}`")
    W(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]}); stdlib "
      f"`fractions` arithmetic on the stored decimal fields; numpy is used only to "
      f"list the keys of a local lens archive (no arrays loaded); no scipy/sklearn; no model, "
      f"no tokenizer, no inference")
    W(f"- Command: `{command}` (run from the repository root)")
    W("")
    W("Block text of the item (verbatim, at the pin):")
    W("")
    for s in item_text:
        W(f"> {s}")
    W("")
    W("Status vocabulary: reproduced (this script computes and prints it from committed "
      "JSON) | log-only (exists only in log prose or raw stdout; pinned locator) | not found | "
      "discrepant | computed-new. Locators are `path@bbc9ffe:line` as in "
      "`git show bbc9ffe:<path>`. Rounding: the gate script stored cosines, the G4 KL and the "
      "leak figures at 4 dp, the G2 ratios and G3 displacements at 3 dp (the G2 per-arm errors "
      "at full precision); exact ratios below are of those stored decimals.")
    W("")

    # ------------------------------------------------------- 0. referents
    W("## 0. Referents and integrity")
    W("")
    arts = {}
    gates = {}
    for rep, path in GATES.items():
        b = show(path)
        wt = (REPO / path).read_bytes() if (REPO / path).exists() else None
        pin_blob = git("rev-parse", f"{PIN}:{path}").strip()
        arts[path] = {"sha256": sha256(b), "worktree_equal_pin":
                      (wt is not None and blob_id(wt) == pin_blob)}
        gates[rep] = json.loads(b.decode("utf-8"), parse_float=Fraction)
        assert gates[rep]["replicate"] == rep and gates[rep]["smoke"] is False
        W(f"- `{path}` sha256 `{arts[path]['sha256']}`; working tree "
          f"{'EQUAL to' if arts[path]['worktree_equal_pin'] else 'DIFFERS from'} pin; "
          f"replicate={rep}, smoke=false")
    first_commit = {p: git("log", "--format=%h %cI", "--diff-filter=A", PIN, "--", p).strip()
                    for p in GATES.values()}
    for p, c in first_commit.items():
        W(f"- `{p}` entered the record at `{c}` (git log --diff-filter=A)")
    raw_commit = {p: git("log", "--format=%h %cI", "--diff-filter=A", PIN, "--", p).strip()
                  for p in RAWS.values()}
    for p, c in raw_commit.items():
        W(f"- `{p}` entered the record at `{c}`")
    # round 2 (R2-4): replicate B's training stdout, to order gates(A)
    # against the training of B
    trainB_commit = git("log", "--format=%h %cI", "--diff-filter=A", PIN, "--",
                        RAW_TRAIN["B"]).strip()
    W(f"- `{RAW_TRAIN['B']}` entered the record at `{trainB_commit}`")
    J["artifacts"] = arts
    J["first_commit"] = {**first_commit, **raw_commit, RAW_TRAIN["B"]: trainB_commit}
    note_present = (REPO / NOTE).exists()
    W(f"- `{NOTE}`: {'present' if note_present else 'NOT on this machine'} "
      "(the block's figures are taken as the block writes them; the post-patch-v4 preprint "
      "sentence that carries them is cited below)")
    W("")

    # raw stdout vs JSON
    W("### 0a. Raw stdout (committed) against the JSON artifacts")
    W("")
    rx = re.compile(r"^\s+(G1|G2|G3|G4|leakage): (PASS|FAIL)\s+(\{.*\})\s*$")
    raw_parsed = {}
    raw_eq = {}
    for key, path in RAWS.items():
        lines = pinned_lines(path)
        got = {}
        for i, s in enumerate(lines):
            m = rx.match(s)
            if m:
                got[m.group(1)] = {"pass": m.group(2) == "PASS", "line": i + 1,
                                   "fields": json.loads(m.group(3), parse_float=Fraction)}
        raw_parsed[key] = got
        if key in gates:
            ok = all(got[g]["pass"] == gates[key][g]["pass"] and
                     got[g]["fields"] == {k: v for k, v in gates[key][g].items()
                                          if k != "pass"}
                     for g in ("G1", "G2", "G3", "G4", "leakage"))
            raw_eq[key] = ok
            W(f"- `{path}`: five gate lines (lines {min(v['line'] for v in got.values())}-"
              f"{max(v['line'] for v in got.values())}) parsed; every field and every PASS/FAIL "
              f"{'IDENTICAL to' if ok else 'DIFFERENT from'} `{GATES[key]}`")
    hdr = {k: locate(p, "probes,") for k, p in RAWS.items()}
    n_probes = {k: int(re.search(r"(\d+) probes", h["text"]).group(1)) for k, h in hdr.items()}
    for k, h in hdr.items():
        W(f"- {h['locator']}: `{h['text']}`")
    J["raw_vs_json_identical"] = raw_eq
    import datetime as _dt
    _d = lambda c: _dt.datetime.fromisoformat(c.split()[1])
    lag = (_d(first_commit[GATES["A"]]) - _d(raw_commit[RAWS["A"]])).total_seconds() / 86400
    J["json_commit_lag_days_vs_raw_A"] = round(lag, 2)
    W(f"- The JSON artifacts entered the record {lag:.2f} days after replicate A's raw stdout "
      "(commit dates above); the raw stdout entered with the run entries themselves, so the "
      "field-for-field identity above is what ties the late-committed JSON to the run of record.")
    W("")

    # ------------------------------------------------------- local context
    W("### 0b. Local, gitignored context (NOT in the record, NOT in a clone)")
    W("")
    W("The code that produced the two artifacts is not tracked in this repository: the "
      "artifacts' own pre-registration names `scripts/c1_gate.py` "
      "(archive line cited in section 1), and the producing script is "
      "`jlens-qwen36/scripts/d_gates.py`; both live in the gitignored jlens-qwen36 clone. "
      "The readout definitions in section 1 are read from those files; they are context "
      "for naming the quantities, not reproductions.")
    W("")
    tracked = git("ls-tree", "-r", "--name-only", PIN).split("\n")
    loc: dict = {"tracked_gate_code": [t for t in tracked
                                       if re.search(r"(c1_gate|d_gates)\.py$", t)]}
    W(f"- Tracked files at the pin named `*c1_gate.py` or `*d_gates.py`: "
      f"{loc['tracked_gate_code'] or 'none'}")
    src = {}
    for k, p in LOCAL.items():
        if p.suffix == ".py" and p.exists():
            b = p.read_bytes()
            src[k] = b.decode("utf-8")
            st = os.stat(p)
            loc[k] = {"path": str(p.relative_to(REPO)), "sha256": sha256(b),
                      "mtime_unix": int(st.st_mtime)}
            W(f"- `{p.relative_to(REPO)}` sha256 `{sha256(b)}`, mtime unix {int(st.st_mtime)}")
    smoke_local = None
    if LOCAL["smoke_json"].exists():
        sb = LOCAL["smoke_json"].read_bytes()
        smoke_local = json.loads(sb.decode("utf-8"), parse_float=Fraction)
        st = os.stat(LOCAL["smoke_json"])
        loc["smoke_json"] = {"path": str(LOCAL["smoke_json"].relative_to(REPO)),
                             "sha256": sha256(sb), "mtime_unix": int(st.st_mtime)}
        W(f"- `{LOCAL['smoke_json'].relative_to(REPO)}` sha256 `{sha256(sb)}` "
          f"(local only; not committed)")
    for rep, path in GATES.items():
        lp = CLONE / path
        if lp.exists():
            eq = sha256(lp.read_bytes()) == arts[path]["sha256"]
            loc[f"clone_{rep}_equal"] = eq
            W(f"- `jlens-qwen36/{path}` (the producing write) "
              f"{'byte-identical to' if eq else 'DIFFERS from'} the committed `{path}`")
    gm = {}
    dl: dict = {}
    c1l: dict = {}
    if "d_gates" in src and "d_gates" in loc:
        s = src["d_gates"]
        loc["d_gates_mtime_before_artifact"] = all(
            loc["d_gates"]["mtime_unix"] < os.stat(CLONE / p).st_mtime
            for p in GATES.values() if (CLONE / p).exists())
        def grab(pat):
            m = re.search(pat, s, re.M)
            assert m, pat
            return m.group(1)
        gm = {"TARGET_LAYERS": grab(r"^TARGET_LAYERS = (\[.*\])"),
              "FP_LAYERS": grab(r"^FP_LAYERS = (\[.*\])"),
              "FRAC": grab(r"^FRAC = ([0-9.]+)"),
              "TAG_C_CP": grab(r'^TAG_C, TAG_CP = ("\w+", "\w+")'),
              "GATE_CONTROLS": re.sub(r"\s+", " ", grab(r"^GATE_CONTROLS = (\[[^\]]*\])")),
              "REF_TAG": grab(r'^REF_TAG = "(\w+)"'),
              "LEAK_GATE": grab(r"^LEAK_GATE = ([0-9.]+)"),
              "N_LEAK": grab(r"^N_LEAK = (\d+)"),
              "G2_RATIO": grab(r"^G2_RATIO = ([0-9.]+)"),
              "G4_KL": grab(r"^G4_KL = ([0-9.]+)"),
              "orient": grab(r"^\s+(orient = .*)$"),
              "d_cond": grab(r"^\s+(d_cond = .*)$"),
              "cos_cond": grab(r"^\s+(cos_cond = .*)$"),
              "ctrl_cos": grab(r"^\s+(ctrl_cos\[.*)$"),
              "g1": grab(r"^\s+(g1 = .*)$"),
              "leak_pair": grab(r"^\s+(a, b = pairs\[s % \d+\])"),
              "leak_delta": grab(r"^\s+(leak_delta = .*)$"),
              "leak_pass": grab(r"^\s+(leak = .*)$"),
              "decl": grab(r'^\s+return (f"active config: \{tag\}\\n\{text\}")'),
              "menu": "".join(re.search(                 # implicit concatenation
                  r'body \+= \(f"(Select the config[^"]*)"\s*\n\s*f"([^"]*)"\)', s).groups()),
              "leak_swap": re.sub(r"\s+", " ", grab(
                  r"^\s+(if \(s // 4\) % 2:\s*\n\s*a, b = b, a)")),
              "leak_logit": grab(r"^\s+(out\.append\(float\(lg\[ia\]\) - float\(lg\[ib\]\)\))")}
        loc["d_gates_constants"] = gm
        sl = s.split("\n")

        def lnum(needle):
            h = [i + 1 for i, t in enumerate(sl) if needle in t]
            assert len(h) == 1, (needle, h)
            return h[0]
        loc["d_gates_lines"] = {
            "leak_texts_pair": lnum("a, b = pairs[s % 4]"),
            "leak_texts_swap": lnum("if (s // 4) % 2:"),
            "menu": lnum('body += (f"Select the config for the remaining rounds: "'),
            "leak_deltas_def": lnum("def leak_deltas(model, texts):"),
            "leak_final_position": lnum("lg = model.unembed(final[:, -1, :])[0].astype(mx.float32)"),
            "leak_logit_diff": lnum("out.append(float(lg[ia]) - float(lg[ib]))"),
            "leak_abs": lnum("leak_delta = np.abs(leak_on - leak_off)"),
            "leak_pass": lnum("leak = bool(leak_max <= LEAK_GATE)"),
            "smoke_probes": lnum("probes = FLAT_PROBE_BATTERY[:3] if args.smoke else FLAT_PROBE_BATTERY"),
            # round 2 (R2-6, R2-7): orientation, the oriented base-pair
            # comparator, and G3's comparator
            "orient": lnum('orient = +1 if args.replicate == "A" else -1'),
            "cos_base": lnum("cos_base = orient * cosine(base_fp[TAG_C] - base_fp[TAG_CP], axis)"),
            "json_cos_base_pair": lnum('"cos_base_pair": round(cos_base, 4),'),
            "ctrl_disp": lnum("ctrl_disp = [float(np.linalg.norm(ad_fp[t1] - ad_fp[t2]))"),
            "bare_disp": lnum("bare_disp = float(np.linalg.norm(bare_ad - bare_base))"),
            "g3": lnum("g3 = bool(bare_disp <= max(ctrl_disp))"),
        }
        dl = loc["d_gates_lines"]
        W(f"- d_gates.py mtime precedes both producing writes: "
          f"{loc['d_gates_mtime_before_artifact']} (file-time evidence that the local "
          f"file is the version that ran; not proof)")
        W("- d_gates.py constants and lines (verbatim): " +
          "; ".join(f"`{k}`: `{v}`" for k, v in gm.items()))
    tag_cands = excluded = None
    if "conditioning" in src:
        m = re.search(r"^TAG_CANDIDATES = (\[[^\]]*\])", src["conditioning"], re.M)
        tag_cands = json.loads(m.group(1).replace("\n", " "))
        W(f"- conditioning.py `TAG_CANDIDATES` = {tag_cands}")
        # round 2 (R2-5): the LoRA rank and layer count, local context only
        cs = src["conditioning"].split("\n")
        lora = {}
        for i, t in enumerate(cs):
            m_n = re.match(r"^LORA_N_LAYERS = (\d+)\s*$", t)
            m_c = re.match(r'^LORA_CFG = \{"rank": (\d+),', t)
            if m_n:
                lora["n_layers"], lora["n_layers_line"] = int(m_n.group(1)), i + 1
            if m_c:
                lora["rank"], lora["cfg_line"] = int(m_c.group(1)), i + 1
        assert set(lora) == {"n_layers", "n_layers_line", "rank", "cfg_line"}, lora
        loc["lora_local"] = lora
        W(f"- conditioning.py `LORA_N_LAYERS` = {lora['n_layers']} (line {lora['n_layers_line']}); "
          f"`LORA_CFG` rank = {lora['rank']} (line {lora['cfg_line']})")
    if "e2a" in src:
        m = re.search(r'^EXCLUDED_TAGS = \{"(\w+)"\}', src["e2a"], re.M)
        excluded = [m.group(1)]
        m2 = re.search(r"^LAYER = (\d+)", src["e2a"], re.M)
        loc["e2a_LAYER"] = int(m2.group(1))
        m3 = re.search(r"def pick_tag_pairs\(tokenizer, n_pairs: int = (\d+)\)", src["e2a"])
        loc["pick_tag_pairs_default"] = int(m3.group(1))
        W(f"- e2a.py `EXCLUDED_TAGS` = {excluded}; `LAYER` = {loc['e2a_LAYER']}; "
          f"`pick_tag_pairs` default n_pairs = {loc['pick_tag_pairs_default']}")
    if "c1_gate" in src:
        ok = ("lens.transport(h[None], L)" in src["c1_gate"]
              and "logits[vocab_idx]" in src["c1_gate"]
              and "last = ids.shape[1] - 1" in src["c1_gate"])
        loc["c1_probe_readout_is_lens_vocab_logits_at_last_token"] = ok
        W(f"- c1_gate.py `probe_readout`: last prompt token; J-lens transport per layer; "
          f"final norm + unembed; logits restricted to the affect vocabulary ids "
          f"(string checks {'all present' if ok else 'NOT all present'})")
        c1s = src["c1_gate"].split("\n")

        def c1n(needle):
            h = [i + 1 for i, t in enumerate(c1s) if needle in t]
            assert len(h) == 1, (needle, h)
            return h[0]
        c1l = {"p2_doc": c1n("P2 state-shaped"),
               "swing_block": c1n("# --- matched-pair swing analysis (r3 pre-registered criterion,"),
               "swing_def": c1n("RESULTS.md 2026-08-06). Swings are (C->hi replicate) minus"),
               "mag_ok": c1n("mag_ok = bool(swings) and d_cond > max_abs")}
        loc["c1_gate_lines"] = c1l
        W(f"- c1_gate.py (local): P2 form in the docstring at line {c1l['p2_doc']}; the r3 "
          f"matched-pair swing block at lines {c1l['swing_block']}-{c1l['mag_ok']} defines a "
          f"swing as the C->hi replicate's control-pair cosine minus the C->lo replicate's "
          f"(a cross-replicate difference)")
    if "fingerprint" in src:
        ok = ("if i in induce_fns:" in src["fingerprint"]
              and "as it exits layer i" in src["fingerprint"])
        loc["injection_at_layer_exit_all_positions"] = ok
        W(f"- fingerprint.py `forward_with_induced_state`: the induce function is applied to "
          f"every position's residual as it exits the keyed layer, captures are "
          f"post-intervention ({'confirmed by string check' if ok else 'NOT confirmed'})")
    lens_layers = None
    if LOCAL["lens_npz"].exists():
        try:
            import numpy as np  # keys only; no arrays are read
            with np.load(LOCAL["lens_npz"]) as z:
                lens_layers = sorted(int(k[2:]) for k in z.files if k.startswith("J_"))
        except Exception as e:  # pragma: no cover
            lens_layers = f"unreadable: {type(e).__name__}"
        loc["lens_layers"] = (f"{lens_layers[0]}..{lens_layers[-1]} ({len(lens_layers)} layers)"
                              if isinstance(lens_layers, list) else lens_layers)
        W(f"- local J-lens archive `jlens-qwen36/data/lens/neuronpedia_n1000.npz` "
          f"(keys only): Jacobians for layers {loc['lens_layers']}")
    J["local_context"] = loc
    W("")

    # leak-text composition (static, from the local script's construction)
    leak_comp = None
    if gm and tag_cands and excluded:
        n_pairs = int(re.search(r"% (\d+)", gm["leak_pair"]).group(1))
        roster = [w for w in tag_cands if w not in excluded][: 2 * n_pairs]
        pairs = [(roster[2 * i], roster[2 * i + 1]) for i in range(n_pairs)]
        n_leak = int(gm["N_LEAK"])
        per_pair = {f"{a}/{b}": sum(1 for s in range(n_leak) if s % n_pairs == i)
                    for i, (a, b) in enumerate(pairs)}
        leak_comp = {"pairs": pairs, "texts_per_pair": per_pair,
                     "assumption": "every roster word is single-token (d_gates asserts it for "
                                   "the 8 gate controls; slate/prism are the conditioned tags)"}
        # Committed corroboration (values-check finding 10): the e2a run used
        # the same e2a.pick_tag_pairs and the same session -> pairs[s % 4]
        # mapping; its committed sessions record the pairs it returned.
        e2a_rows = [json.loads(t) for t in show(E2A_SESS).decode("utf-8").splitlines() if t.strip()]
        e2a_order: list = []
        e2a_map: dict = {}
        for r_ in e2a_rows:
            pr = tuple(r_["pair"])
            if pr not in e2a_order:
                e2a_order.append(pr)
            e2a_map.setdefault(r_["session"] % 4, set()).add(pr)
        e2a_mod4_consistent = all(len(v) == 1 for v in e2a_map.values())
        e2a_ok = (e2a_order == [tuple(p_) for p_ in pairs] and e2a_mod4_consistent
                  and all(next(iter(e2a_map[i])) == tuple(pairs[i]) for i in range(n_pairs)))
        leak_comp["committed_corroboration"] = {
            "source": f"{E2A_SESS}@{PIN} (field `pair`, by `session`)",
            "n_rows": len(e2a_rows),
            "pair_order_first_seen": [list(p_) for p_ in e2a_order],
            "session_mod4_to_single_pair": e2a_mod4_consistent,
            "equals_local_construction": e2a_ok}
        J["leak_text_composition_static"] = leak_comp

    # ------------------------------------------------------- record locators
    A = {  # archive/RESULTS-cycles3-4.md
        "gatesB_head": locate(ARCH, "(d)/e1 gates(B) + descriptives"),
        "gatesB_g1": locate(ARCH, "G1(B) PASS — oriented cos 0.435 vs"),
        "gatesB_g1b": locate(ARCH, "max control 0.053 (A: 0.476/0.044)"),
        "gatesB_leak": locate(ARCH, "max |Δ| = 1.06, mean 0.53"),
        "gatesB_leak2": locate(ARCH, "(10× bar; A: 1.75/0.96)"),
        "gatesB_g2": locate(ARCH, "G2(B) 1.02/"),
        "adj_head": locate(ARCH, "(d)/e1 LEAKAGE ADJUDICATION"),
        "adj_noleak": locate(ARCH, "untriggered tags carry no leak"),
        "gatesA_head": locate(ARCH, "(d)/e1 gates(A): G1–G4 ALL PASS"),
        "gatesA_17": locate(ARCH, "Leakage gate FAIL (17× bar)"),
        "gatesA_train": locate(ARCH, "0.73→0.41→0.23, no incident; raws"),
        "gatesB_train": locate(ARCH, "here.** (Train B: 0.75→0.34→0.19, no incident; raws"),
        "gatesA_g1": locate(ARCH, "cos(adapter C−C′ contrast, steered X−Y axis) = 0.476 vs max"),
        "gatesA_g1b": locate(ARCH, "|control-pair cos| = 0.044 over 28 pairs (base-pair 0.056)"),
        "gatesA_g2": locate(ARCH, "PASS:** arm error ratios 1.03 (MSE) / 1.12"),
        "gatesA_g3": locate(ARCH, "bare mentions inert (disp 12.0 vs control floor 103.2)"),
        "gatesA_g4": locate(ARCH, "anchor KL 0.037 ≤ 0.05"),
        "gatesA_leak": locate(ARCH, "d2-shaped session texts: max |Δ(logit_A − logit_B)| = 1.75"),
        "gatesA_smoke": locate(ARCH, "adapter 0.5 → trained 1.75)"),
        "prereg_head": locate(ARCH, "(d)/e1 G-GATE PRE-REGISTRATION"),
        "prereg_g1": locate(ARCH, "swing machinery (`scripts/c1_gate.py`)"),
        "prereg_g1b": locate(ARCH, "max |control-tag-pair swing|, 28 control pairs from the 8-tag"),
        "prereg_leak": locate(ARCH, "max |Δ(logit_A − logit_B)| ≤ **0.10**"),
        "prereg_leak0": locate(ARCH, "over ≥32 identical completed-session choice texts"),
        "go_drug": locate(ARCH, "X/Y = ±span reward axis (sha"),
        "go_layermap": locate(ARCH, "adapter spans layers 56–63"),
        "go_reps": locate(ARCH, "replicates A (C→X) / B (C→Y)"),
        # round 2: second lines of phrases that span two lines (R2-3), the
        # record's own statements of the scaling claim (R2-2), the order of
        # gates(A) and the training of B (R2-4), G3's pre-registered
        # comparator (R2-6), the adapter rank (R2-5)
        "gatesB_g2b": locate(ARCH, "1.03 (tighter than A)"),
        "gatesA_g2b": locate(ARCH, "(KL) ≤ 1.25 — no fidelity asymmetry"),
        "gatesB_flip": locate(ARCH, "and the RAW cosine flips sign"),
        "gatesB_flip_end": locate(ARCH, "counterbalance read a tag-word artifact cannot fake"),
        "gatesA_scale": locate(ARCH, "and it scales with training (smoke"),
        "adj_scale_a": locate(ARCH, "Expected-signature note: leak should"),
        "adj_scale_b": locate(ARCH, "scale with training as in A (0.5 smoke → 1.75 trained)"),
        "gatesB_scale_a": locate(ARCH, "at slightly lower G1; reads as CONFIRM with the scale note"),
        "gatesB_scale_b": locate(ARCH, "(leak roughly tracks installation strength)"),
        "adj_deferB_a": locate(ARCH, "Replicate B training deferred until the"),
        "adj_deferB_b": locate(ARCH, "d2 read is adjudicated (its gates would be identical in kind)"),
        "prereg_g3_head": locate(ARCH, "**G3 trigger specificity:** bare-mention contexts"),
        "prereg_g3": locate(ARCH, "fingerprint within the control-pair floor of base;"),
        "prereg_g3_end": locate(ARCH, "redesign, not proceed."),
        "prereg_rank": locate(ARCH, "Trainer: rank 8 / last 8"),
        "go_rank": locate(ARCH, "64 layers; rank-8"),
        "next_after_d": locate(ARCH, "e2a VERDICT: NOT PASSED"),
    }
    # the two-line phrases are cited as spans only if the second line follows
    for a_, b_ in (("gatesB_g2", "gatesB_g2b"), ("gatesA_g2", "gatesA_g2b"),
                   ("gatesA_scale", "gatesA_smoke"), ("adj_scale_a", "adj_scale_b"),
                   ("gatesB_scale_a", "gatesB_scale_b"), ("adj_deferB_a", "adj_deferB_b"),
                   ("go_rank", "go_layermap")):
        assert A[b_]["line"] == A[a_]["line"] + 1, (a_, b_)
    assert A["prereg_g3_head"]["line"] < A["prereg_g3"]["line"] < A["prereg_g3_end"]["line"] \
        <= A["prereg_g3_head"]["line"] + 3
    assert A["gatesB_flip_end"]["line"] == A["gatesB_flip"]["line"] + 2
    # (d) entries of the archive: from the gates(B) head (newest) to the line
    # before the next older entry (the e2a VERDICT)
    d_span = (A["gatesB_head"]["line"], A["next_after_d"]["line"] - 1)
    Fd = {  # FINDINGS-3.md
        "table": locate(F3, "Leakage 17×/10× bar"),
        "cos": locate(F3, "oriented cos 0.476 / 0.435 against control ceilings 0.044 / 0.053"),
        "g2": locate(F3, "G2 ratios ≤ 1.12"),
        "g3": locate(F3, "bare mentions inert: 12 vs floor 103"),
        "g4": locate(F3, "(G4 ≤ 0.037)"),
        "leak": locate(F3, "failed at 17× the bar in A (max 1.75) and 10× in"),
        "leak2": locate(F3, "B (max 1.06)"),
        "noleak": locate(F3, "carry no leak"),
        "noleak_a": locate(F3, "(untriggered tags"),            # round 2 (R2-3)
        "scale": locate(F3, "scaling with installation strength and with training"),  # R2-2
    }
    assert Fd["noleak"]["line"] == Fd["noleak_a"]["line"] + 1
    P = {"frac": locate(PROP, "frac = 1.0 — P(keep)"),
         "g1": locate(PROP, "**G1 — Trace installed.**"),
         "leak_mentions": [i + 1 for i, s in enumerate(pinned_lines(PROP))
                           if "leak" in s.lower()]}
    misc = {"vocab": locate(ARCH12, "369 single-token concept/affect words"),
            "cache_alpha": locate(RAW_CACHE, "alpha 10.30 (frac 0.1 x R48 103.0)"),
            "layermap": locate(RAW_LAYERMAP, "adapter layers: [56, 57, 58, 59, 60, 61, 62, 63]"),
            "layermap_n": locate(RAW_LAYERMAP, "n_layers: "),         # round 2 (R2-5)
            "smoke_g1": locate(RAWS["A_smoke"], "G1: FAIL"),
            "smoke_leak": locate(RAWS["A_smoke"], "leakage: FAIL"),
            "train_smoke": locate("results/raw/2026-08-10_d_train_smoke.txt",
                                  "12 examples/epoch [smoke]")}
    # training size and epochs, from the committed training stdout (log-only)
    train = {}
    for k, p in RAW_TRAIN.items():
        tl = pinned_lines(p)
        m0 = re.match(r"^\(d\) distill rep\w+: (\d+) examples/epoch", tl[0])
        ep = [(i + 1, t.strip()) for i, t in enumerate(tl) if re.match(r"^epoch \d+: mean loss", t)]
        train[k] = {"examples_per_epoch": int(m0.group(1)), "header": f"{p}@{PIN}:1",
                    "n_epochs": len(ep),
                    "epoch_lines": f"{p}@{PIN}:" + ",".join(str(i) for i, _ in ep),
                    "epoch_means": [t for _, t in ep]}
    misc["train"] = train
    # pre-registration G1, the whole bullet (values-check finding 3)
    pg_lo = locate(ARCH, "**G1 installed (manipulation check, never a finding):**")["line"]
    pg_hi = locate(ARCH, "  roster, per replicate.")["line"]
    prereg_g1_text = " ".join(t.strip() for t in pinned_lines(ARCH)[pg_lo - 1:pg_hi])
    prereg_g1_text = prereg_g1_text[2:] if prereg_g1_text.startswith("- ") else prereg_g1_text
    A_g1_span = f"{ARCH}@{PIN}:{pg_lo}-{pg_hi}"
    gate_swing = locate("valence_core/gate.py", "how much a pair's signed alignment moves")
    gate_dcond = locate("valence_core/gate.py", 'd_cond = float(hi_rep["cos_ad_raw"] - lo_rep["cos_ad_raw"])')
    prop_swing = locate(PROP, "swing|, ≥ 20 control pairs, both replicates.")
    pre = None
    if (REPO / PREPRINT).exists():
        pb = (REPO / PREPRINT).read_bytes()
        pre = {"sha256": sha256(pb),
               "sha_match": sha256(pb).startswith(PREPRINT_SHA[0])
               and sha256(pb).endswith(PREPRINT_SHA[1]),
               "cos": locate(PREPRINT, "oriented cosine 0.476 and 0.435 against control "
                                       "ceilings ≈ 0.05", pinned=False),
               "leak": locate(PREPRINT, "fails at 17× and 10× the allowed bound",
                              pinned=False),
               "rank": locate(PREPRINT, "a rank-8 adapter", pinned=False)}  # R2-5
    J["locators"] = {"archive": A, "findings3": Fd, "proposal_d": P, "misc": misc,
                     "preprint_untracked": pre}

    # ------------------------------------------------------- computations
    g = {r: gates[r] for r in ("A", "B")}
    orient = {"A": 1, "B": -1}
    G1 = {}
    for r in ("A", "B"):
        c = F(g[r]["G1"]["cos_cond_oriented"])
        mx = F(g[r]["G1"]["max_ctrl_cos"])
        bp = F(g[r]["G1"]["cos_base_pair"])
        G1[r] = {"cos_oriented": c, "max_ctrl_abs_cos": mx, "cos_base_pair_oriented": bp,
                 "n_ctrl_pairs": g[r]["G1"]["n_ctrl_pairs"],
                 "raw_cos": orient[r] * c, "raw_base_pair": orient[r] * bp,
                 "ratio_cos_to_ceiling": c / mx,
                 "pass_recomputed": bool(c > 0 and abs(c) > mx),
                 "pass_stored": g[r]["G1"]["pass"]}
    d_cond = G1["A"]["raw_cos"] - G1["B"]["raw_cos"]
    swing_ub = G1["A"]["max_ctrl_abs_cos"] + G1["B"]["max_ctrl_abs_cos"]
    e4 = Fraction(5, 100000)                        # half a unit of the 4-dp storage
    d_cond_lo = d_cond - 2 * e4                     # both cosines rounded
    swing_ub_hi = swing_ub + 2 * e4
    # Sign-flip corroboration from the JSON alone (values-check finding 10):
    # the base-pair comparator is computed in the adapter-free base phase,
    # which does not depend on the replicate, so its RAW value should be equal
    # across the runs; the stored ORIENTED values have opposite signs, which
    # says the two runs used opposite orientations.
    bp_opposite = (g["A"]["G1"]["cos_base_pair"] == -g["B"]["G1"]["cos_base_pair"]
                   and g["A"]["G1"]["cos_base_pair"] != 0)
    G2 = {}
    for r in ("A", "B"):
        e = g[r]["G2"]["errs"]
        rat = {m: max(F(e["C"][m]), F(e["Cp"][m])) / min(F(e["C"][m]), F(e["Cp"][m]))
               for m in ("mse", "kl")}
        G2[r] = {"ratio_mse": rat["mse"], "ratio_kl": rat["kl"],
                 "stored": {k: F(v) for k, v in g[r]["G2"]["ratios"].items()},
                 "bar": F(g[r]["G2"]["bar"]),
                 "pass_recomputed": all(v <= F(g[r]["G2"]["bar"]) for v in rat.values()),
                 "pass_stored": g[r]["G2"]["pass"],
                 "higher_mse_arm": "C" if F(e["C"]["mse"]) > F(e["Cp"]["mse"]) else "Cp",
                 "higher_kl_arm": "C" if F(e["C"]["kl"]) > F(e["Cp"]["kl"]) else "Cp"}
    G3 = {r: {"bare_disp": F(g[r]["G3"]["bare_disp"]),
              "ctrl_disp_max": F(g[r]["G3"]["ctrl_disp_max"]),
              "pass_recomputed": F(g[r]["G3"]["bare_disp"]) <= F(g[r]["G3"]["ctrl_disp_max"]),
              "pass_stored": g[r]["G3"]["pass"]} for r in ("A", "B")}
    G4 = {r: {"mean_kl": F(g[r]["G4"]["mean_kl"]), "bar": F(g[r]["G4"]["bar"]),
              "pass_recomputed": F(g[r]["G4"]["mean_kl"]) <= F(g[r]["G4"]["bar"]),
              "pass_stored": g[r]["G4"]["pass"]} for r in ("A", "B")}
    L = {}
    for r in ("A", "B"):
        lk = g[r]["leakage"]
        mxa, mna, bar, n = F(lk["max_abs"]), F(lk["mean_abs"]), F(lk["bar"]), lk["n"]
        L[r] = {"max_abs": mxa, "mean_abs": mna, "bar": bar, "n": n,
                "max_over_bar": mxa / bar, "max_over_bar_floor": floor_(mxa / bar),
                "max_over_bar_half_up": half_up(mxa / bar),
                "mean_over_bar": mna / bar,
                "pass_recomputed": mxa <= bar, "pass_stored": lk["pass"]}
    leak_BA = L["B"]["max_abs"] / L["A"]["max_abs"]
    mean_BA = L["B"]["mean_abs"] / L["A"]["mean_abs"]
    # smoke (log-only: raw stdout; the smoke JSON is local only)
    sm = raw_parsed["A_smoke"]
    smoke = {"cos_oriented": F(sm["G1"]["fields"]["cos_cond_oriented"]),
             "max_ctrl": F(sm["G1"]["fields"]["max_ctrl_cos"]),
             "leak_max": F(sm["leakage"]["fields"]["max_abs"]),
             "leak_mean": F(sm["leakage"]["fields"]["mean_abs"]),
             "n": sm["leakage"]["fields"]["n"]}
    pts = sorted([(smoke["cos_oriented"], smoke["leak_max"], "smoke A"),
                  (G1["B"]["cos_oriented"], L["B"]["max_abs"], "B"),
                  (G1["A"]["cos_oriented"], L["A"]["max_abs"], "A")])
    rank_txt = "; ".join(f"{nm}: cos {f4(c)} -> max {f4(m)}" for c, m, nm in pts)
    rank_ok = all(pts[i][1] < pts[i + 1][1] for i in range(len(pts) - 1))
    if smoke_local is not None:
        smoke["raw_equals_local_json"] = all(
            sm[k]["fields"] == {kk: vv for kk, vv in smoke_local[k].items() if kk != "pass"}
            for k in ("G1", "G2", "G3", "G4", "leakage"))
    # grid check (post-hoc): are the stored leak summaries multiples of 1/16?
    grid = {}
    for name, mxa, mna, n in (("A", L["A"]["max_abs"], L["A"]["mean_abs"], L["A"]["n"]),
                              ("B", L["B"]["max_abs"], L["B"]["mean_abs"], L["B"]["n"]),
                              ("A_smoke", smoke["leak_max"], smoke["leak_mean"], smoke["n"])):
        tot16 = mna * n * 16
        k = round(tot16)
        tol = Fraction(5, 100000) * n * 16          # 4-dp rounding of the mean
        grid[name] = {"max_x16": mxa * 16, "max_on_grid": (mxa * 16).denominator == 1,
                      "sum_x16": tot16, "nearest_int": k, "residual": tot16 - k,
                      "tolerance": tol, "sum_on_grid_within_rounding": abs(tot16 - k) <= tol}
    # control-pair-text lower bound (post-hoc; conditional on the local construction)
    lb = None
    if leak_comp:
        n_cond = leak_comp["texts_per_pair"][f"{leak_comp['pairs'][0][0]}/{leak_comp['pairs'][0][1]}"]
        lb = {}
        for r in ("A", "B"):
            n = L[r]["n"]
            eps = Fraction(5, 100000)
            lo = (n * (L[r]["mean_abs"] - eps) - n_cond * (L[r]["max_abs"] + eps)) / (n - n_cond)
            pt = (n * L[r]["mean_abs"] - n_cond * L[r]["max_abs"]) / (n - n_cond)
            share_lo = (n * (L[r]["mean_abs"] - eps) - n_cond * (L[r]["max_abs"] + eps)) \
                / (n * (L[r]["mean_abs"] - eps))
            lb[r] = {"n_cond_pair_texts": n_cond, "n_control_pair_texts": n - n_cond,
                     "sum_abs_delta": n * L[r]["mean_abs"],
                     "max_possible_on_cond_texts": n_cond * L[r]["max_abs"],
                     "control_text_mean_lower_bound": pt,
                     "control_text_mean_lower_bound_conservative": lo,
                     "lower_bound_over_bar": lo / L[r]["bar"],
                     "control_text_share_of_sum_lower_bound": share_lo}

    # round 2 (R2-1): how B's stored maximum rounds to 2 dp, by rule
    b_max_dec = Decimal(L["B"]["max_abs"].numerator) / Decimal(L["B"]["max_abs"].denominator)
    assert Fraction(str(b_max_dec)) == L["B"]["max_abs"], b_max_dec
    q2 = Decimal("0.01")
    lo2, hi2 = b_max_dec.quantize(q2, ROUND_DOWN), b_max_dec.quantize(q2, ROUND_CEILING)
    rnd = {"value": str(b_max_dec), "lower_2dp": str(lo2), "upper_2dp": str(hi2),
           "midpoint_2dp": str((lo2 + hi2) / 2),
           "distance_to_lower": str(b_max_dec - lo2), "distance_to_upper": str(hi2 - b_max_dec),
           "half_up": str(b_max_dec.quantize(q2, ROUND_HALF_UP)),
           "half_even": str(b_max_dec.quantize(q2, ROUND_HALF_EVEN)),
           "half_down": str(b_max_dec.quantize(q2, ROUND_HALF_DOWN)),
           "truncation": str(b_max_dec.quantize(q2, ROUND_DOWN)),
           "ceiling": str(hi2)}
    rnd["nearest_rules_and_truncation_agree"] = len(
        {rnd["half_up"], rnd["half_even"], rnd["half_down"], rnd["truncation"]}) == 1
    rnd["record_value_is_that_rounding"] = rnd["half_up"] == "1.06" and \
        rnd["nearest_rules_and_truncation_agree"]
    assert rnd["record_value_is_that_rounding"], rnd
    # round 2 (R2-8): bfloat16 spacing by magnitude, at representative values
    bf = {f"{x:g}": bf16_spacing(x) for x in (4.0, 6.0, 8.0, 12.0, 16.0, 24.0, 32.0)}
    bf_mult16 = {k: (Fraction(v) * 16).denominator == 1 for k, v in bf.items()}
    # the prose in section 2a states these bands; hold it to the computation
    assert bf["4"] == bf["6"] == 1 / 32 and bf["8"] == bf["12"] == 1 / 16 \
        and bf["16"] == bf["24"] == 1 / 8, bf
    assert not bf_mult16["4"] and all(bf_mult16[k] for k in ("8", "12", "16", "24", "32"))
    # round 2 (R2-4): was the cross-replicate swing ever computed in the
    # record? Scan the (d) archive entries, FINDINGS-3, the two gate raws and
    # the two artifacts for the word.
    arch_l = pinned_lines(ARCH)
    swing_hits_d = [i for i in range(d_span[0], d_span[1] + 1)
                    if "swing" in arch_l[i - 1].lower()]
    swing_other = {p: show(p).decode("utf-8").lower().count("swing")
                   for p in (F3, RAWS["A"], RAWS["B"], GATES["A"], GATES["B"])}
    swing_scan = {"archive_d_span": f"{ARCH}@{PIN}:{d_span[0]}-{d_span[1]}",
                  "archive_d_lines_with_swing": swing_hits_d,
                  "all_inside_prereg_g1_bullet": all(pg_lo <= i <= pg_hi for i in swing_hits_d),
                  "counts_elsewhere": swing_other,
                  "never_computed_in_scanned_record": all(pg_lo <= i <= pg_hi for i in swing_hits_d)
                  and not any(swing_other.values())}
    # round 2 (R2-5): adapter rank and layers from the record
    rank_txt_pre = re.search(r"rank (\d+) / last (\d+)", A["prereg_rank"]["text"])
    rank_txt_go = re.search(r"rank-(\d+)", A["go_rank"]["text"])
    span_go = re.search(r"layers (\d+)–(\d+)", A["go_layermap"]["text"])
    lm_layers = json.loads(re.search(r"(\[.*\])", misc["layermap"]["text"]).group(1))
    lm_n = int(re.search(r"n_layers: (\d+)", misc["layermap_n"]["text"]).group(1))
    rank_row = {"rank_prereg": int(rank_txt_pre.group(1)),
                "last_n_layers_prereg": int(rank_txt_pre.group(2)),
                "rank_step1": int(rank_txt_go.group(1)),
                "span_step1": [int(span_go.group(1)), int(span_go.group(2))],
                "layermap_layers": lm_layers, "layermap_n_layers": lm_n}
    rank_row["consistent"] = (rank_row["rank_prereg"] == rank_row["rank_step1"]
                              and lm_layers == list(range(lm_n - rank_row["last_n_layers_prereg"], lm_n))
                              and [lm_layers[0], lm_layers[-1]] == rank_row["span_step1"])
    def keypaths(o, p=""):
        if isinstance(o, dict):
            for k_, v_ in o.items():
                yield p + k_
                yield from keypaths(v_, p + k_ + ".")
    rank_row["committed_json_keys_with_rank"] = sorted(
        k_ for r in ("A", "B") for k_ in keypaths(gates[r]) if "rank" in k_.lower())
    rank_row["committed_json_files_at_pin_under_data_d"] = [
        t for t in tracked if t.startswith("data/d/")]
    assert rank_row["consistent"], rank_row

    def ser(o):
        if isinstance(o, Fraction):
            return float(o)
        if isinstance(o, dict):
            return {k: ser(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [ser(v) for v in o]
        return o
    J["G1"] = ser(G1)
    J["G1_swing_bound"] = ser({"D_cond_raw_A_minus_raw_B": d_cond,
                               "D_cond_lower_bound_after_rounding": d_cond_lo,
                               "max_abs_swing_upper_bound": swing_ub,
                               "max_abs_swing_upper_bound_after_rounding": swing_ub_hi,
                               "sign_ok": d_cond_lo > 0,
                               "magnitude_ok_a_fortiori": d_cond_lo > swing_ub_hi,
                               "prereg_g1_locator": A_g1_span,
                               "prereg_g1_text": prereg_g1_text})
    J["G1_sign_flip_from_base_pair"] = {
        "oriented_base_pair_A": float(g["A"]["G1"]["cos_base_pair"]),
        "oriented_base_pair_B": float(g["B"]["G1"]["cos_base_pair"]),
        "opposite_signs_equal_magnitude": bp_opposite}
    J["G2"], J["G3"], J["G4"] = ser(G2), ser(G3), ser(G4)
    J["leakage"] = ser(L)
    J["leak_B_over_A"] = {"max": float(leak_BA), "mean": float(mean_BA)}
    J["smoke_log_only"] = ser(smoke)
    J["posthoc_grid"] = ser(grid)
    J["posthoc_control_text_bound"] = ser(lb)
    J["round2_computed"] = {"B_max_rounding_2dp": rnd,
                            "bf16_spacing_by_magnitude": bf,
                            "bf16_spacing_multiple_of_1_16": bf_mult16,
                            "swing_scan": swing_scan,
                            "adapter_rank_and_layers": rank_row}

    # ------------------------------------------------------- 1. readout
    W("## 1. What each cosine is: readout, layers, contrast, control set")
    W("")
    W(f"Pre-registration of record for the bars: {A['prereg_head']['locator']} (extent to the "
      f"`Numeric bars adjudicated` line), committed at `88e9ef0`; G1 at "
      f"{A_g1_span} (whole bullet, lines joined): \"{prereg_g1_text}\"; leakage at "
      f"{A['prereg_leak0']['locator']}-"
      f"{A['prereg_leak']['line']} (`{A['prereg_leak0']['text']}` ... "
      f"`{A['prereg_leak']['text']}`). The drug and pairing: {A['go_drug']['locator']} "
      f"(`{A['go_drug']['text']}`); replicates: {A['go_reps']['locator']} "
      f"(`{A['go_reps']['text']}`); adapter span: {A['go_layermap']['locator']}, "
      f"{misc['layermap']['locator']} (`{misc['layermap']['text']}`); dose: "
      f"{misc['cache_alpha']['locator']} (`{misc['cache_alpha']['text']}`).")
    W("")
    W("| | replicate A (C=slate -> X, C'=prism -> Y) | replicate B (C=slate -> Y, C'=prism -> X) |")
    W("|---|---|---|")
    W("| readout | J-lens fingerprint (`c1_gate.probe_readout`, local): at the LAST prompt token, the residual at each fingerprint layer is transported by the Jacobian lens, final-normed and unembedded; the logits are restricted to the affect vocabulary (369 single-token concept/affect words per "
      f"{misc['vocab']['locator']}, not recounted here: that needs the tokenizer); flattened and concatenated over the held-out probe battery ({n_probes['A']} probes, {hdr['A']['locator']}) | same ({n_probes['B']} probes, {hdr['B']['locator']}) |")
    W(f"| layers | six fingerprint layers concatenated, `FP_LAYERS = {gm.get('FP_LAYERS')}` (not one layer). By construction of the code (not measured): the adapter sits on layers 56-63, so the L40-L52 slices of the adapter-arm fingerprints equal the base model's; the steered reference is injected at the exit of L{loc.get('e2a_LAYER')}, so the axis is zero in the L40 and L44 slices. The adapter-attributable part of the contrast is in the L56 and L60 slices (the distillation targets, `TARGET_LAYERS = {gm.get('TARGET_LAYERS')}`) | same |")
    W(f"| prompt | `{gm.get('decl')}` per probe (the declaration trigger; G3 tests the bare-mention form) | same |")
    W("| contrast (numerator vector) | adapter loaded, unsteered: fp(`active config: slate`) - fp(`active config: prism`) | same |")
    W(f"| reference axis | base model (no adapter), fresh tag `{gm.get('REF_TAG')}`: fp(+alpha u) - fp(-alpha u), u = frozen reward axis (sha d4791bdc4877da3d), injected at L48 at every position, alpha = frac {gm.get('FRAC')} x R48 (10.30) | identical construction (recomputed in each run's base phase) |")
    W(f"| sign | `{gm.get('orient')}`; `{gm.get('cos_cond')}` | orient = -1 |")
    W(f"| stored value | oriented cos **{f4(G1['A']['cos_oriented'])}**; raw cos {f4(G1['A']['raw_cos'])} | oriented cos **{f4(G1['B']['cos_oriented'])}**; raw cos {f4(G1['B']['raw_cos'])} |")
    W(f"| control set | the {G1['A']['n_ctrl_pairs']} unordered pairs of the 8 gate controls `{gm.get('GATE_CONTROLS')}`; each pair's adapter-arm fingerprint difference (t1 - t2, unoriented), cosine with the same axis; ceiling = max over the pairs of the absolute cosine (`{gm.get('ctrl_cos')}`) | same set, same rule |")
    W(f"| control ceiling | **{f4(G1['A']['max_ctrl_abs_cos'])}** | **{f4(G1['B']['max_ctrl_abs_cos'])}** |")
    W(f"| comparator (recorded, not gated) | base model, no adapter: slate - prism, oriented: {f4(G1['A']['cos_base_pair_oriented'])} (raw {f4(G1['A']['raw_base_pair'])}) | {f4(G1['B']['cos_base_pair_oriented'])} (raw {f4(G1['B']['raw_base_pair'])}) |")
    W(f"| G1 rule as run | `{gm.get('g1')}`: stored PASS={G1['A']['pass_stored']}, recomputed from stored fields {G1['A']['pass_recomputed']} | stored PASS={G1['B']['pass_stored']}, recomputed {G1['B']['pass_recomputed']} |")
    W(f"| CV | none: a single cosine between two fixed vectors per replicate; no probe is fit, no split, no permutation null (the null is the 28-pair ceiling) | same |")
    W("")
    W(f"- The raw cosine changes sign with the assignment (A {f4(G1['A']['raw_cos'])}, B "
      f"{f4(G1['B']['raw_cos'])}); this is the record's counterbalance read "
      f"({A['gatesB_flip']['locator']}-{A['gatesB_flip_end']['line']}). It is not stored "
      f"separately: it follows from the "
      f"stored oriented values (> 0 in both) and the orientation rule (A: C->X, B: C->Y, "
      f"{A['go_reps']['locator']}), so it carries the same information as 'oriented cos > 0 in "
      f"both replicates'. The JSON corroborates that the two runs used opposite orientations, "
      f"but it does not by itself fix which run is +1: the orientation rule is log-only "
      f"({A['go_reps']['locator']}) and in the local d_gates.py (line {dl.get('orient')}). "
      f"The corroboration: the stored base-pair comparator `G1.cos_base_pair` is "
      f"{f4(G1['A']['cos_base_pair_oriented'])} (A) and "
      f"{f4(G1['B']['cos_base_pair_oriented'])} (B), equal in magnitude and opposite in sign "
      f"({bp_opposite}). That the field is stored ORIENTED is in the local d_gates.py "
      f"(line {dl.get('cos_base')}, written at line {dl.get('json_cos_base_pair')}); the field "
      f"name does not say it. That comparator comes from the adapter-free base phase, which does "
      f"not depend on the replicate, so its raw value should be the same in both runs; opposite "
      f"stored signs then mean opposite orientations. (This assumes the base phase computed the "
      f"same raw value in both runs, which the equal magnitudes are consistent with.)")
    W(f"- On that reading the base-pair raw cosine is {f4(G1['A']['raw_base_pair'])} in A and "
      f"{f4(G1['B']['raw_base_pair'])} in B, equal at the stored 4 dp across two separate runs, "
      f"as expected for the adapter-free base phase.")
    W(f"- The c1 form of this read ('P2', `jlens-qwen36/scripts/c1_gate.py` docstring, local) "
      f"also required the conditioned cosine to exceed the no-adapter cosine for the same tags; "
      f"d_gates.py records that comparator without gating on it. It would hold: "
      f"{f4(G1['A']['cos_oriented'])} > {f4(G1['A']['cos_base_pair_oriented'])} (A), "
      f"{f4(G1['B']['cos_oriented'])} > {f4(G1['B']['cos_base_pair_oriented'])} (B): "
      f"{bool(G1['A']['cos_oriented'] > G1['A']['cos_base_pair_oriented'] and G1['B']['cos_oriented'] > G1['B']['cos_base_pair_oriented'])}.")
    W(f"- Oriented cosine over its control ceiling (computed-new, to keep it apart from the "
      f"leakage multiples): A {f4(G1['A']['ratio_cos_to_ceiling'], 1)}x, B "
      f"{f4(G1['B']['ratio_cos_to_ceiling'], 1)}x.")
    W(f"- **G1's pre-registered form, and the form that ran.** The bullet "
      f"({A_g1_span}, quoted above) names 'the r3 matched-pair swing machinery "
      f"(`scripts/c1_gate.py`)' and ends ', per replicate.' In the swing machinery a "
      f"swing is a cross-replicate difference: the C->hi replicate's control-pair cosine minus "
      f"the C->lo replicate's (`valence_core/gate.py`, {gate_swing['locator']} and "
      f"{gate_dcond['locator']}; the local c1_gate.py r3 block, lines "
      f"{c1l.get('swing_block')}-{c1l.get('mag_ok')}), and PROPOSAL-d's G1 asks for it over "
      f"'both replicates' ({prop_swing['locator']}). ', per replicate' has two readings: it "
      f"can scope the whole gate (each replicate gated on its own), or only '28 control pairs "
      f"from the 8-tag roster' (the swing machinery needs the control pairs measured in each "
      f"replicate). The record does not say which was meant. The run applied the "
      f"per-replicate P2 form (d_gates.py, local): each replicate's oriented cosine against that "
      f"replicate's own control-pair cosines. At gates(A) only that form was computable: "
      f"gates(A) was run and adjudicated before replicate B was trained "
      f"({ARCH}@{PIN}:{A['adj_deferB_a']['line']}-{A['adj_deferB_b']['line']}, 'Replicate B "
      f"training deferred until the d2 read is adjudicated'; replicate A's gate stdout entered "
      f"the record at `{raw_commit[RAWS['A']]}`, replicate B's training stdout at "
      f"`{trainB_commit}` and its gate stdout at `{raw_commit[RAWS['B']]}`). "
      f"The cross-replicate swing was never computed in the record. Scanned by this run: in "
      f"the (d) entries ({swing_scan['archive_d_span']}) the word 'swing' occurs only on lines "
      f"{swing_scan['archive_d_lines_with_swing']}, inside the G1 pre-registration bullet "
      f"({swing_scan['all_inside_prereg_g1_bullet']}), and "
      f"{sum(swing_scan['counts_elsewhere'].values())} times in {F3}, the two gate raws and "
      f"the two artifacts. Gates(B)'s cross-replicate read is the raw-sign flip "
      f"({ARCH}@{PIN}:{A['gatesB_flip']['line']}-{A['gatesB_flip_end']['line']}). The swing "
      f"form needs per-pair control cosines from both replicates, which the artifacts do not "
      f"store (only each replicate's maximum). A bound from the stored fields shows that it "
      f"passes (computed-new, after the fact): D_cond = raw_A - raw_B = {f4(d_cond)} "
      f"(>= {f_down(d_cond_lo)} allowing for the 4-dp rounding of both cosines); every control "
      f"swing satisfies |c_A - c_B| <= {f4(G1['A']['max_ctrl_abs_cos'])} + "
      f"{f4(G1['B']['max_ctrl_abs_cos'])} = {f4(swing_ub)} (<= {f_up(swing_ub_hi)} after "
      f"rounding). So the swing form's sign and magnitude conjuncts hold a fortiori "
      f"({d_cond_lo > 0 and d_cond_lo > swing_ub_hi}), with the same 28 pairs in both runs. "
      f"This decides nothing (G1 is a declared manipulation check); it shows that G1 passes "
      f"under both readings of the pre-registration.")
    W("")

    # ------------------------------------------------------- 2. leakage
    W("## 2. The leakage gate's bound and the 17x / 10x exceedances")
    W("")
    W(f"- **Quantity bounded** (pre-registered at {A['prereg_leak0']['locator']}-"
      f"{A['prereg_leak']['line']}; local code, d_gates.py lines {dl.get('leak_deltas_def')}-"
      f"{dl.get('leak_logit_diff')} and {dl.get('leak_abs')}-{dl.get('leak_pass')}: "
      f"`{gm.get('leak_logit')}`, `{gm.get('leak_delta')}`, `{gm.get('leak_pass')}`): for each "
      f"of n = {L['A']['n']} completed d2-shaped session texts (banner, four `active config:` "
      f"blocks alternating the session's two tags, then the menu line "
      f"`{gm.get('menu')}` (d_gates.py lines {dl.get('menu')}-{(dl.get('menu') or 0) + 1}), "
      f"with the two labels' order swapped on alternate cycles of four texts "
      f"(`{gm.get('leak_swap')}`, line {dl.get('leak_texts_swap')}), no "
      f"declaration at the choice), Delta = [logit(tag a) - logit(tag b)] with the adapter ON "
      f"minus the same with the adapter OFF, read at the final position (the next-token "
      f"distribution after the menu line, full model output, no lens). Units: raw logits "
      f"(log-odds between the two single-token labels). 'logit_A/logit_B' in the record "
      f"means the two menu labels, not the replicates.")
    W(f"- **Bound:** max over the {L['A']['n']} texts of |Delta| <= {f4(L['A']['bar'], 2)} logit. "
      f"What the JSON holds: `leakage.bar` = {f4(L['A']['bar'], 2)} and `leakage.n` = "
      f"{L['A']['n']} in both artifacts (reproduced). What the JSON does not hold: that the bar "
      f"binds on the MAXIMUM (not the mean), the ON-minus-OFF construction and the read "
      f"position. Those come from the pre-registration text ({A['prereg_leak0']['locator']}-"
      f"{A['prereg_leak']['line']}, log-only) and the local d_gates.py (lines "
      f"{dl.get('leak_final_position')}, {dl.get('leak_abs')}-{dl.get('leak_pass')}). The stored "
      f"PASS=false cannot tell max-binding from mean-binding, because both mean_abs values "
      f"({f4(L['A']['mean_abs'])}, {f4(L['B']['mean_abs'])}) also exceed the bar. It is a "
      f"maximum, not a rate. PASS stored/recomputed (max <= bar): A "
      f"{L['A']['pass_stored']}/{L['A']['pass_recomputed']}, "
      f"B {L['B']['pass_stored']}/{L['B']['pass_recomputed']}.")
    for r in ("A", "B"):
        W(f"- **Replicate {r}:** `leakage.max_abs` / `leakage.bar` = {f4(L[r]['max_abs'])} / "
          f"{f4(L[r]['bar'], 2)} = **{f4(L[r]['max_over_bar'], 3)}** "
          f"(floor {L[r]['max_over_bar_floor']}, round-half-up {L[r]['max_over_bar_half_up']}); "
          f"mean |Delta| / bar = {f4(L[r]['mean_abs'])} / {f4(L[r]['bar'], 2)} = "
          f"{f4(L[r]['mean_over_bar'], 3)}.")
    W(f"- So the record's '17x' and '10x' ({A['gatesA_17']['locator']}, "
      f"{A['gatesB_leak2']['locator']}, {Fd['leak']['locator']}, {Fd['table']['locator']}) are "
      f"**the maximum |Delta| over the 32 texts divided by the 0.10 bar**, written as the floor "
      f"of 17.5 and 10.625. Rounded, they are 18x and 11x; exactly, 17.5x and 10.6x. The "
      f"mean-based multiples would be 9.6x and 5.3x. The floors understate: the direction is "
      f"conservative and the wording is not wrong as 'at least 17x / 10x'.")
    W(f"- B's maximum over A's: {f4(leak_BA, 3)} (the record's '~60% of A's magnitude', "
      f"{A['gatesB_leak2']['locator']}); means {f4(mean_BA, 3)}.")
    W(f"- Smoke adapter (log-only; {misc['smoke_leak']['locator']}): max {f4(smoke['leak_max'])}, "
      f"mean {f4(smoke['leak_mean'])}, at oriented cos {f4(smoke['cos_oriented'])} (G1 FAIL "
      f"against ceiling {f4(smoke['max_ctrl'])}; {misc['smoke_g1']['locator']}). The smoke JSON "
      f"exists only in the local clone"
      + (f" (and equals the raw line: {smoke.get('raw_equals_local_json')})" if
         'raw_equals_local_json' in smoke else "") + ". Across the three adapters the maxima "
      f"rank with the G1 cosine ({rank_txt}; rank-consistent: {rank_ok}). The comparison is "
      f"like-for-like on the leak axis only: the three leak maxima are over the same 32 texts, "
      f"but the smoke G1 cosine is on a {n_probes['A_smoke']}-probe battery "
      f"({hdr['A_smoke']['locator']}; d_gates.py line {dl.get('smoke_probes')}, local) against "
      f"{n_probes['A']} probes for A and B ({hdr['A']['locator']}, {hdr['B']['locator']}). The "
      f"record states the scaling claim at {ARCH}@{PIN}:{A['gatesA_scale']['line']}-"
      f"{A['gatesA_smoke']['line']} (gates(A): 'scales with training'), "
      f":{A['adj_scale_a']['line']}-{A['adj_scale_b']['line']} (the adjudication's "
      f"expected-signature note) and :{A['gatesB_scale_a']['line']}-"
      f"{A['gatesB_scale_b']['line']} (gates(B): 'roughly tracks installation strength'), and "
      f"FINDINGS-3 at {Fd['scale']['locator']} and {Fd['table']['locator']}. It rests on these "
      f"three points, one of them "
      f"the smoke adapter: {misc['train']['smoke']['n_epochs']} epoch over "
      f"{misc['train']['smoke']['examples_per_epoch']} examples "
      f"({misc['train']['smoke']['header']}; epoch line {misc['train']['smoke']['epoch_lines']}), "
      f"against {misc['train']['A']['n_epochs']} epochs over "
      f"{misc['train']['A']['examples_per_epoch']} examples for A "
      f"({misc['train']['A']['header']}; epoch lines {misc['train']['A']['epoch_lines']}) and "
      f"{misc['train']['B']['n_epochs']} over {misc['train']['B']['examples_per_epoch']} for B "
      f"({misc['train']['B']['header']}; {misc['train']['B']['epoch_lines']}); the record's loss "
      f"traces are at {A['gatesA_train']['locator']} (A) and {A['gatesB_train']['locator']} (B).")
    W("")
    W("### 2a. Post-hoc observations on the bound (labeled post-hoc; they change no gate)")
    W("")
    W("1. **Resolution.** Every stored leak summary is consistent with per-text |Delta| on a "
      "1/16-logit grid:")
    for name, gr in grid.items():
        W(f"   - {name}: max x 16 = {f4(gr['max_x16'], 4)} (integer: {gr['max_on_grid']}); "
          f"n x mean x 16 = {f4(gr['sum_x16'], 4)}, nearest integer {gr['nearest_int']}, "
          f"residual {f4(gr['residual'], 4)} within the 4-dp rounding tolerance "
          f"+/-{f4(gr['tolerance'], 4)}: {gr['sum_on_grid_within_rounding']}")
    bf_txt = ", ".join(f"{bf[k]:g} at {k}" for k in bf)
    W("   This is what label logits held at bfloat16 precision would produce if the label "
      "logits are of magnitude >= 8 (the gate casts to float32 only after the unembedding, "
      f"d_gates.py line {dl.get('leak_final_position')}, local). The bf16 spacing, computed by "
      f"this run at representative magnitudes, is {bf_txt}: 1/32 on [4, 8), 1/16 on [8, 16), "
      "1/8 on [16, 32), so a sum or difference of bf16 logits that are each of magnitude >= 8 "
      "is a multiple of 1/16, and one involving a logit below 8 need not be. It is consistent with that, not proof of it. "
      "On such a grid the 0.10 bar admits at most one grid step (0.0625) per text, and the "
      f"observed maxima are {int(grid['A']['max_x16'])} steps (A) and "
      f"{int(grid['B']['max_x16'])} steps (B), so the resolution does not touch the verdict.")
    if lb and leak_comp:
        W("2. **Which texts carry the shift.** The artifacts store only the max and the mean; "
          "they cannot say which text gave the maximum. The local script's construction "
          f"(`{gm.get('leak_pair')}`, d_gates.py line {dl.get('leak_texts_pair')}, over "
          f"`e2a.pick_tag_pairs`, which returns the first {2 * len(leak_comp['pairs'])} "
          f"single-token roster words paired in order: {leak_comp['pairs']}) puts "
          f"{lb['A']['n_cond_pair_texts']} of the {L['A']['n']} texts on the conditioned pair "
          f"slate/prism and {lb['A']['n_control_pair_texts']} on control-tag pairs (tags the "
          f"anchor term trained toward base, never paired with a state; "
          f"{locate(ARCH, '(control text + control tags → base)')['locator']}; roster: "
          f"{locate(ARCH, 'Tags C=slate/C′=prism, controls = the')['locator']}). Committed "
          f"corroboration of the pair order: the e2a run called the same `pick_tag_pairs` with "
          f"the same session -> pairs[s % 4] mapping, and "
          f"{leak_comp['committed_corroboration']['source']} records "
          f"{leak_comp['committed_corroboration']['pair_order_first_seen']} over "
          f"{leak_comp['committed_corroboration']['n_rows']} rows, one pair per session mod 4 "
          f"({leak_comp['committed_corroboration']['session_mod4_to_single_pair']}), equal to the "
          f"local construction ({leak_comp['committed_corroboration']['equals_local_construction']}). "
          "The 8-of-32 count itself still rests on the local script. Then "
          "the summed |Delta| on the control-pair texts is at least n x mean - 8 x max. Lower "
          "bounds below are printed rounded DOWN, so each printed figure is itself a bound:")
        for r in ("A", "B"):
            b = lb[r]
            W(f"   - {r}: {f4(b['sum_abs_delta'], 4)} - {f4(b['max_possible_on_cond_texts'], 4)}"
              f" (with the stored fields taken as exact, the control-pair-text mean is >= "
              f"{f_down(b['control_text_mean_lower_bound'], 4)}). Allowing for the 4-dp rounding of "
              f"both fields: mean |Delta| on the {b['n_control_pair_texts']} control-pair texts "
              f">= {f_down(b['control_text_mean_lower_bound_conservative'], 4)} "
              f"(>= {f_down(b['lower_bound_over_bar'], 1)}x the bar); the control-pair texts "
              f"carry >= {f_down(100 * b['control_text_share_of_sum_lower_bound'], 1)}% of the "
              f"summed |Delta|")
        W(f"   The adjudication's reason for not calibrating with control tags, 'untriggered "
          f"tags carry no leak' ({A['adj_noleak']['locator']}; also {Fd['noleak_a']['locator']}-"
          f"{Fd['noleak']['line']}), "
          "is stated without a stored per-tag measurement: the gate artifacts keep only the "
          "maximum and the mean over all 32 texts. If it means |Delta| near 0 on "
          "control-pair texts, these fields contradict it, provided the local script is the "
          "code that ran (its mtime precedes both writes). If it means 'no "
          "assignment-tracking component', the fields cannot test it, because no signed "
          "per-text deltas were stored. In either reading the gate's FAIL stands, since the "
          "bar binds on the maximum over all 32 texts. What the stored fields do not support is "
          "attributing the maxima, or the A > B ordering, to the conditioned pair rather than to "
          "a generic adapter-ON shift of label logits. That bears on the mechanism sentence "
          f"({A['gatesA_leak']['locator']} and following; {Fd['leak']['locator']}) and on "
          "'scaling with installation strength'. It does not change the gate's FAIL. Whether "
          "it bears on the adjudication's option analysis (control tags were set aside as a "
          "calibrator because they were taken to carry no leak) is the design seat's question; "
          "Code does not adjudicate it.")
    W("")

    # ------------------------------------------------------- 3. companions
    W("## 3. Companion gates (the same artifacts; figures the record states beside N9's)")
    W("")
    for r in ("A", "B"):
        W(f"- G2 {r}: MSE ratio {f4(G2[r]['ratio_mse'], 4)} (stored {f4(G2[r]['stored']['mse'], 3)}),"
          f" KL ratio {f4(G2[r]['ratio_kl'], 4)} (stored {f4(G2[r]['stored']['kl'], 3)}); "
          f"bar {f4(G2[r]['bar'], 2)}; the higher-error arm is {G2[r]['higher_mse_arm']} on MSE "
          f"and {G2[r]['higher_kl_arm']} on KL; PASS stored/recomputed "
          f"{G2[r]['pass_stored']}/{G2[r]['pass_recomputed']}")
    for r in ("A", "B"):
        W(f"- G3 {r}: bare-mention fingerprint displacement {f4(G3[r]['bare_disp'], 3)} (L2 "
          f"distance between the bare-mention fingerprints with and without the adapter) vs "
          f"{f4(G3[r]['ctrl_disp_max'], 3)}, the maximum over the 28 adapter-arm control-tag "
          f"pairs of the L2 distance between their fingerprints; PASS "
          f"{G3[r]['pass_stored']}/{G3[r]['pass_recomputed']}. G4 {r}: mean "
          f"KL(adapter||base) {f4(G4[r]['mean_kl'], 4)} nats vs {f4(G4[r]['bar'], 2)}; PASS "
          f"{G4[r]['pass_stored']}/{G4[r]['pass_recomputed']}")
    W(f"- G3's comparator, as run, is adapter-arm, and the 'floor' is the maximum of the 28 "
      f"control-pair distances (the most lenient choice; local d_gates.py lines "
      f"{dl.get('ctrl_disp')}-{dl.get('g3')}: `ctrl_disp` over `ad_fp` pairs, "
      f"`g3 = bare_disp <= max(ctrl_disp)`). The pre-registration words it as 'the "
      f"control-pair floor of base' ({ARCH}@{PIN}:{A['prereg_g3_head']['line']}-"
      f"{A['prereg_g3_end']['line']}, phrase at :{A['prereg_g3']['line']}), and gates(A) as "
      f"'control floor' ({A['gatesA_g3']['locator']}); as run it is not computed on the base "
      f"arm, and it is the largest of the 28 distances, not a typical one. "
      f"FINDINGS-3's '12 vs floor 103' ({Fd['g3']['locator']}) gives replicate A's bare "
      f"displacement ({f4(G3['A']['bare_disp'], 3)}; B's is {f4(G3['B']['bare_disp'], 3)}); "
      f"'103' covers both comparators ({f4(G3['A']['ctrl_disp_max'], 3)}, "
      f"{f4(G3['B']['ctrl_disp_max'], 3)}).")
    W(f"- FINDINGS-3's 'G2 ratios <= 1.12' ({Fd['g2']['locator']}): the largest ratio is A's KL "
      f"ratio, {f4(G2['A']['ratio_kl'], 4)} > 1.12. That is a rounding (1.12 at 2 dp) "
      f"carried into an inequality, i.e. transcription-type, and immaterial to the 1.25 bar. "
      f"'<= 1.13' or '1.12 at most, to two decimals' is exact. The same pattern: "
      f"'G4 <= 0.037' ({Fd['g4']['locator']}) against a stored {f4(G4['A']['mean_kl'], 4)}.")
    W("")

    # ------------------------------------------------------- 4. referent notes
    W("## 4. Referent notes (the block's own rule: a wrong referent is a note, not a STOP)")
    W("")
    W(f"1. **`{PROP}` carries neither the leakage gate nor any numeric bar.** Its G1-G4 "
      f"({P['g1']['locator']} ff.) are verbal; its only 'leak' strings are at lines "
      f"{P['leak_mentions']} ('evocation leakage (G3)', i.e. trigger specificity). The bars "
      f"and the d2 leakage gate are in the G-gate pre-registration log entry "
      f"{A['prereg_head']['locator']} (commit `88e9ef0`; N13 row L-dgate covers its provenance). "
      f"Its state spec is also superseded: `{P['frac']['text']}` ({P['frac']['locator']}) is the "
      f"(c) cycle's states. The run used the BUILD GO's drug, +/- the reward axis at L48, frac "
      f"0.10 ({A['go_drug']['locator']}).")
    W(f"2. **Where the (d) verdicts live** (N9's block text names no log entry; listed for N1's "
      f"ledger). No (d) entry in the archive is titled VERDICT. The "
      f"verdict-bearing entries are gates(A) {A['gatesA_head']['locator']} (17x at "
      f":{A['gatesA_17']['line']}; G1 at :{A['gatesA_g1']['line']}-{A['gatesA_g1b']['line']}; "
      f"leak at :{A['gatesA_leak']['line']}), the leakage adjudication "
      f"{A['adj_head']['locator']} (d2 CLOSED BY GATE) and gates(B) {A['gatesB_head']['locator']} "
      f"(G1 at :{A['gatesB_g1']['line']}-{A['gatesB_g1b']['line']}; 10x at "
      f":{A['gatesB_leak2']['line']}). The synthesis is {F3}@{PIN}:"
      f"{Fd['cos']['line']}-{Fd['leak2']['line']}.")
    vg = locate("valence_core/gate.py", "ported off `scripts/c1_gate.py`")
    vr = locate("valence_core/readout.py", "Lens-based fingerprint readouts are deliberately NOT here")
    W(f"3. **The producing code is not in the record.** `d_gates.py` and `c1_gate.py` are in "
      f"the gitignored clone (section 0b). The pre-registration's `scripts/c1_gate.py` "
      f"({A['prereg_g1']['locator']}) is not a tracked path in this repository. "
      f"`valence_core/gate.py` ports the swing machinery ({vg['locator']}), and "
      f"`valence_core/readout.py` states that the lens-based fingerprint readout was "
      f"deliberately not ported ({vr['locator']}). A reader of the tag can check the stored "
      f"numbers against each other and against the raw stdout, but cannot see how they were "
      f"computed. The README could say so in one sentence.")
    W("4. **The control ceiling is not the base-pair figure.** '~0.05' in the preprint covers "
      f"{f4(G1['A']['max_ctrl_abs_cos'])} and {f4(G1['B']['max_ctrl_abs_cos'])} (max |cosine| "
      f"over 28 adapter-arm control pairs). The base-pair comparator, |{f4(G1['A']['raw_base_pair'])}|, "
      "is also near 0.05 but is a different quantity. 'against control ceilings of 0.044 and "
      "0.053' (FINDINGS-3's wording) is exact.")
    if pre:
        W(f"5. The untracked post-patch-v4 preprint (`{PREPRINT}`, sha256 "
          f"{pre['sha256'][:8]}...{pre['sha256'][-5:]}, "
          f"{'MATCH' if pre['sha_match'] else 'MISMATCH'} vs the block's) carries N9's sentence "
          f"at {pre['cos']['locator']}: 'a rank-8 adapter' ("
          + ("on the same line" if pre['rank']['line'] == pre['cos']['line']
             else f"at {pre['rank']['locator']}")
          + "; Figures row added in round 2), oriented cosines, '≈ 0.05', '17× and 10× the "
          "allowed bound', 'scaling with installation strength'.")
    W("")

    # ------------------------------------------------------- figures table
    figs = []

    def fig(figure, value, source, status, note=""):
        figs.append({"figure": figure, "value": value, "source": source,
                     "status": status, "note": note})
    GJ = "data/d/gates_rep{A,B}.json"
    fig("oriented cosine 0.476 (replicate A)", f4(G1["A"]["cos_oriented"]),
        "data/d/gates_repA.json:G1.cos_cond_oriented", "reproduced",
        f"readout: J-lens affect-vocabulary fingerprint at the last prompt token, layers "
        f"L40/44/48/52/56/60 concatenated, over {n_probes['A']} held-out probes; contrast: adapter "
        f"loaded, fp(active config: slate) - fp(active config: prism); axis: base model, ref tag "
        f"timber, +/-alpha along the reward axis at L48, frac 0.10; oriented +1; no CV (a single "
        f"cosine; the null is the 28-pair control ceiling). Readout definition from the local, "
        f"untracked c1_gate.py / d_gates.py")
    fig("oriented cosine 0.435 (replicate B)", f4(G1["B"]["cos_oriented"]),
        "data/d/gates_repB.json:G1.cos_cond_oriented", "reproduced",
        f"same readout, contrast and axis as A; oriented -1 (raw {f4(G1['B']['raw_cos'])})")
    fig("control ceilings ≈ 0.05", f"A {f4(G1['A']['max_ctrl_abs_cos'])}; B "
        f"{f4(G1['B']['max_ctrl_abs_cos'])}", f"{GJ}:G1.max_ctrl_cos",
        "reproduced", f"max |cos| with the same axis over the 28 adapter-arm pairs of the 8 "
        f"gate controls; the exact pair 0.044 / 0.053 is at {Fd['cos']['locator']}; not the "
        f"base-pair comparator ({f4(abs(G1['A']['cos_base_pair_oriented']))})")
    fig("leakage gate's bound: the bar, 0.10 logit, over n = 32 texts",
        f"bar {f4(L['A']['bar'], 2)} (A and B); n {L['A']['n']} / {L['B']['n']}",
        f"{GJ}:leakage.bar, leakage.n", "reproduced", "the JSON holds the bar and n only")
    fig("leakage gate's bound: what it binds (max over texts of |Δ(logit a − logit b)|, "
        "adapter ON − OFF, at the choice position)",
        "max |Δ| <= 0.10; ON − OFF; final position after the menu line",
        f"{A['prereg_leak0']['locator']}-{A['prereg_leak']['line']}", "log-only",
        f"also visible in the local, untracked d_gates.py (lines {dl.get('leak_deltas_def')}-"
        f"{dl.get('leak_logit_diff')}, {dl.get('leak_abs')}-{dl.get('leak_pass')}); the JSON's "
        f"PASS=false cannot tell max-binding from mean-binding, since both mean_abs values "
        f"({f4(L['A']['mean_abs'])}, {f4(L['B']['mean_abs'])}) also exceed 0.10")
    fig("17× (replicate A)", f"{f4(L['A']['max_abs'])}/{f4(L['A']['bar'], 2)} = "
        f"{f4(L['A']['max_over_bar'], 3)}", "data/d/gates_repA.json:leakage.max_abs / "
        "leakage.bar", "reproduced",
        f"written as the floor of 17.5 (half-up 18); max-based (the mean-based multiple is "
        f"{f4(L['A']['mean_over_bar'], 3)}); that the bar binds on the max is log-only (row above)")
    fig("10× (replicate B)", f"{f4(L['B']['max_abs'])}/{f4(L['B']['bar'], 2)} = "
        f"{f4(L['B']['max_over_bar'], 3)}", "data/d/gates_repB.json:leakage.max_abs / "
        "leakage.bar", "reproduced",
        f"written as the floor of 10.625 (half-up 11); the mean-based multiple is "
        f"{f4(L['B']['mean_over_bar'], 3)}")
    fig("max 1.75 (A)", f4(L["A"]["max_abs"]), "data/d/gates_repA.json:leakage.max_abs",
        "reproduced", f"{A['gatesA_leak']['locator']}; {Fd['leak']['locator']}")
    fig("max 1.06 (B)", f4(L["B"]["max_abs"]), "data/d/gates_repB.json:leakage.max_abs",
        "reproduced", f"{A['gatesB_leak']['locator']}; {Fd['leak2']['locator']}. "
        f"{rnd['value']} rounds to {rnd['half_up']} at 2 dp under any standard rule (the 2-dp "
        f"midpoint is {rnd['midpoint_2dp']}); the record's 1.06 is the correct rounding "
        f"(decimal quantize to 0.01, this run: half-up {rnd['half_up']}, half-even "
        f"{rnd['half_even']}, half-down {rnd['half_down']}, truncation {rnd['truncation']}; "
        f"{rnd['value']} is {rnd['distance_to_lower']} from {rnd['lower_2dp']} and "
        f"{rnd['distance_to_upper']} from {rnd['upper_2dp']}; only directed rounding up gives "
        f"{rnd['ceiling']})")
    fig("mean 0.96 / 0.53", f"{f4(L['A']['mean_abs'])} / {f4(L['B']['mean_abs'])}",
        f"{GJ}:leakage.mean_abs", "reproduced",
        f"{A['gatesA_leak']['locator']}-{A['gatesA_leak']['line'] + 1}; "
        f"{A['gatesB_leak']['locator']}-{A['gatesB_leak2']['line']}")
    fig("~60% of A's magnitude", f4(leak_BA, 3), f"{GJ}:leakage.max_abs (B / A)", "reproduced",
        f"{A['gatesB_leak2']['locator']}; the ratio of means is {f4(mean_BA, 3)}")
    fig("28 control pairs", f"{G1['A']['n_ctrl_pairs']} / {G1['B']['n_ctrl_pairs']}",
        f"{GJ}:G1.n_ctrl_pairs", "reproduced", "C(8,2) = 28")
    fig("base-pair 0.056", f"A {f4(G1['A']['cos_base_pair_oriented'])}; B "
        f"{f4(G1['B']['cos_base_pair_oriented'])} (oriented as stored; raw "
        f"{f4(G1['A']['raw_base_pair'])} in both)",
        f"{GJ}:G1.cos_base_pair", "reproduced",
        f"{A['gatesA_g1b']['locator']}; recorded, not gated")
    fig("raw cosine flips sign with the assignment", f"A {f4(G1['A']['raw_cos'])}; B "
        f"{f4(G1['B']['raw_cos'])}",
        f"{GJ}:G1.cos_cond_oriented (> 0 in both) x orientation (A +1, B -1: "
        f"{A['go_reps']['locator']}; opposite orientations also shown by {GJ}:G1.cos_base_pair "
        f"signs)", "reproduced",
        "derived, not stored; equivalent to 'oriented > 0 in both replicates'. The JSON alone "
        "does not fix which run is +1: the orientation rule is log-only "
        f"({A['go_reps']['locator']}) and in the local d_gates.py (line {dl.get('orient')}); "
        f"that `cos_base_pair` is stored oriented is in the local d_gates.py (line "
        f"{dl.get('cos_base')}; the field name does not say it). The base-pair argument shows "
        "only that the orientations are opposite, and assumes the adapter-free base phase gave "
        "the same raw value in both runs")
    fig("scaling with installation strength (smoke 0.5 → trained 1.75)",
        f"smoke max {f4(smoke['leak_max'])} at oriented cos {f4(smoke['cos_oriented'])} "
        f"(G1 FAIL)",
        f"values: {misc['smoke_leak']['locator']}; {misc['smoke_g1']['locator']}. The record's "
        f"statements of the claim: {ARCH}@{PIN}:{A['gatesA_scale']['line']}-"
        f"{A['gatesA_smoke']['line']}, :{A['adj_scale_a']['line']}-{A['adj_scale_b']['line']}, "
        f":{A['gatesB_scale_a']['line']}-{A['gatesB_scale_b']['line']}; {Fd['scale']['locator']}, "
        f"{Fd['table']['locator']}",
        "log-only",
        f"the smoke JSON is local only; the three adapters are rank-consistent, but the smoke "
        f"cosine is on {n_probes['A_smoke']} probes against {n_probes['A']} for A and B "
        f"({hdr['A_smoke']['locator']}); the leak maxima are on the same 32 texts")
    fig("rank-8 adapter, last 8 layers (56-63)",
        f"rank {rank_row['rank_prereg']} (pre-registration and step 1 agree); layers "
        f"{rank_row['layermap_layers'][0]}-{rank_row['layermap_layers'][-1]}, the last "
        f"{len(rank_row['layermap_layers'])} of {rank_row['layermap_n_layers']}",
        f"{A['prereg_rank']['locator']}; {ARCH}@{PIN}:{A['go_rank']['line']}-"
        f"{A['go_layermap']['line']}; {misc['layermap']['locator']}",
        "log-only",
        f"no committed JSON stores the rank (keys containing 'rank' in {GJ}: "
        f"{rank_row['committed_json_keys_with_rank'] or 'none'}; the files under data/d/ at the "
        f"pin are {rank_row['committed_json_files_at_pin_under_data_d']}); the layer list is in "
        f"the committed layer-map raw"
        + (f"; also in the local, untracked conditioning.py (`LORA_CFG` rank "
           f"{loc['lora_local']['rank']}, line {loc['lora_local']['cfg_line']}; `LORA_N_LAYERS` "
           f"{loc['lora_local']['n_layers']}, line {loc['lora_local']['n_layers_line']})"
           if "lora_local" in loc else "")
        + (f"; the preprint's 'a rank-8 adapter' is at {pre['rank']['locator']}" if pre else ""))
    fig("training size behind 'scales with training'",
        f"A {misc['train']['A']['n_epochs']} epochs x {misc['train']['A']['examples_per_epoch']}; "
        f"B {misc['train']['B']['n_epochs']} x {misc['train']['B']['examples_per_epoch']}; smoke "
        f"{misc['train']['smoke']['n_epochs']} x {misc['train']['smoke']['examples_per_epoch']}",
        f"{misc['train']['A']['header']}, {misc['train']['A']['epoch_lines']}; "
        f"{misc['train']['B']['header']}, {misc['train']['B']['epoch_lines']}; "
        f"{misc['train']['smoke']['header']}, {misc['train']['smoke']['epoch_lines']}",
        "log-only", f"loss traces in the log at {A['gatesA_train']['locator']} (A), "
        f"{A['gatesB_train']['locator']} (B)")
    fig("12 probes", f"{n_probes['A']} / {n_probes['B']}",
        f"{hdr['A']['locator']}; {hdr['B']['locator']}", "log-only", "not stored in the JSON")
    fig("alpha = 0.10 × R48", "10.30 (R48 103.0)", misc["cache_alpha"]["locator"], "log-only",
        "teacher-cache raw; d_gates.py recomputes FRAC*R48 (local)")
    fig("G2 A 1.03 (MSE) / 1.12 (KL)", f"{f4(G2['A']['ratio_mse'], 4)} / "
        f"{f4(G2['A']['ratio_kl'], 4)}", "data/d/gates_repA.json:G2.errs", "reproduced",
        f"{A['gatesA_g2']['locator']}-{A['gatesA_g2b']['line']} (the phrase spans the two lines)")
    fig("G2 B 1.02/1.03", f"{f4(G2['B']['ratio_mse'], 4)} / {f4(G2['B']['ratio_kl'], 4)}",
        "data/d/gates_repB.json:G2.errs", "reproduced",
        f"{A['gatesB_g2']['locator']}-{A['gatesB_g2b']['line']} (the phrase spans the two lines)")
    fig("G2 ratios ≤ 1.12 (FINDINGS-3)", f"max {f4(G2['A']['ratio_kl'], 4)}",
        "data/d/gates_repA.json:G2.errs", "discrepant",
        f"{Fd['g2']['locator']}; a 2-dp rounding carried into '≤' (transcription-type); the "
        f"1.25 bar is unaffected")
    fig("G3 12 vs floor 103", f"A {f4(G3['A']['bare_disp'], 3)} vs {f4(G3['A']['ctrl_disp_max'], 3)};"
        f" B {f4(G3['B']['bare_disp'], 3)} vs {f4(G3['B']['ctrl_disp_max'], 3)}",
        f"{GJ}:G3.bare_disp, G3.ctrl_disp_max", "reproduced",
        f"{Fd['g3']['locator']}. The '12' is replicate A's value (B's is "
        f"{f4(G3['B']['bare_disp'], 3)}). The comparator is adapter-arm, and the 'floor' is the "
        f"maximum, over the 28 control-tag pairs, of the L2 distance between their fingerprints "
        f"(the most lenient choice; local d_gates.py lines {dl.get('ctrl_disp')}-{dl.get('g3')}); "
        f"the pre-registration words it as 'the control-pair floor of base' "
        f"({ARCH}@{PIN}:{A['prereg_g3']['line']})")
    fig("G4 anchor KL 0.037 (A) / 0.017 (B)", f"A {f4(G4['A']['mean_kl'], 4)}; B "
        f"{f4(G4['B']['mean_kl'], 4)}", f"{GJ}:G4.mean_kl", "reproduced",
        f"{A['gatesA_g4']['locator']}; {locate(ARCH, 'G4(B) anchor')['locator']}-{locate(ARCH, 'G4(B) anchor')['line'] + 1}")
    fig("G4 ≤ 0.037 (FINDINGS-3)", f"max {f4(G4['A']['mean_kl'], 4)}",
        "data/d/gates_repA.json:G4.mean_kl", "discrepant",
        f"{Fd['g4']['locator']}: 0.0372 > 0.037, a rounding carried into '≤' "
        "(transcription-type); the 0.05 bar is unaffected")
    fig("oriented cosine / control ceiling (not in the record)",
        f"A {f4(G1['A']['ratio_cos_to_ceiling'], 1)}×; B {f4(G1['B']['ratio_cos_to_ceiling'], 1)}×",
        f"{GJ}:G1.cos_cond_oriented / G1.max_ctrl_cos", "computed-new",
        "listed so that it is not confused with the leakage 10×")
    fig("G1 in the pre-registered swing form (post-hoc bound)",
        f"D_cond {f4(d_cond)} (>= {f_down(d_cond_lo)}) > max|swing| <= {f4(swing_ub)} "
        f"(<= {f_up(swing_ub_hi)})",
        f"{GJ}:G1.cos_cond_oriented, G1.max_ctrl_cos; wording {A_g1_span}", "computed-new",
        "per-pair control cosines were not stored; the bound shows the swing reading also passes; "
        "the bracketed values allow for the 4-dp storage")
    if lb:
        fig("control-pair-text mean |Δ| lower bound (post-hoc)",
            f"A >= {f_down(lb['A']['control_text_mean_lower_bound_conservative'], 4)}; B >= "
            f"{f_down(lb['B']['control_text_mean_lower_bound_conservative'], 4)} (share of summed "
            f"|Δ| >= {f_down(100 * lb['A']['control_text_share_of_sum_lower_bound'], 1)}% / >= "
            f"{f_down(100 * lb['B']['control_text_share_of_sum_lower_bound'], 1)}%)",
            f"{GJ}:leakage.mean_abs, leakage.max_abs, leakage.n + the local d_gates.py text "
            f"construction (pair order corroborated by {E2A_SESS}@{PIN}:pair)", "computed-new",
            "post-hoc; rounded down and conservative for the 4-dp storage; holds only if the "
            "local script is the code that ran; bears on 'untriggered tags carry no leak', not "
            "on the gate's FAIL")
    fig("1/16-logit grid (post-hoc)", "all six leak summaries on the grid within rounding: "
        f"{all(v['sum_on_grid_within_rounding'] and v['max_on_grid'] for v in grid.values())}",
        f"{GJ}:leakage.max_abs, leakage.mean_abs, leakage.n; {misc['smoke_leak']['locator']}",
        "computed-new",
        "consistent with bf16 logits of magnitude >= 8 (bf16 spacing is 1/16 only on [8, 16); "
        "1/32 on [4, 8), 1/8 on [16, 32)), not proof; on that grid the 0.10 bar admits at most "
        f"one 0.0625 step per text; the maxima are {int(grid['A']['max_x16'])} and "
        f"{int(grid['B']['max_x16'])} steps")
    J["figures"] = figs

    def cell(s) -> str:
        return str(s).replace("|", "\\|")
    W("## Figures")
    W("")
    W("| figure as the block / record writes it | value printed | source | status | note |")
    W("|---|---|---|---|---|")
    for f_ in figs:
        W("| " + " | ".join(cell(f_[k]) for k in
                            ("figure", "value", "source", "status", "note")) + " |")
    W("")
    W("## Summary")
    W("")
    W(f"Every number the block lists for N9 is reproduced from the two committed gate "
      f"artifacts, which equal the committed raw stdout field for field: oriented cosines "
      f"{f4(G1['A']['cos_oriented'])} / {f4(G1['B']['cos_oriented'])}; control ceilings "
      f"{f4(G1['A']['max_ctrl_abs_cos'])} / {f4(G1['B']['max_ctrl_abs_cos'])}; the leakage bar "
      f"{f4(L['A']['bar'], 2)} logit over n = 32 texts (that it binds on the maximum is "
      f"log-only, {A['prereg_leak0']['locator']}-{A['prereg_leak']['line']}); exceedances "
      f"{f4(L['A']['max_over_bar'], 3)} / {f4(L['B']['max_over_bar'], 3)}, which the record "
      f"writes as 17x / 10x by flooring. Notes for the design seat: (i) the code that "
      f"produced the artifacts is not in the record; (ii) G1's pre-registered wording names the "
      f"cross-replicate swing machinery and ends ', per replicate', which has two readings; the "
      f"run applied the per-replicate P2 form (at gates(A) only that form was computable); the "
      f"cross-replicate swing was never computed in the record; a bound from the stored fields "
      f"shows it passes; "
      + (f"(iii) post-hoc, and only if the local script is the one that ran, at least "
         f"{f_down(100 * lb['A']['control_text_share_of_sum_lower_bound'], 1)}% (A) and "
         f"{f_down(100 * lb['B']['control_text_share_of_sum_lower_bound'], 1)}% (B) of the summed "
         f"|Delta| sits on the 24 control-tag-pair texts (mean |Delta| there >= "
         f"{f_down(lb['A']['control_text_mean_lower_bound_conservative'], 2)} and >= "
         f"{f_down(lb['B']['control_text_mean_lower_bound_conservative'], 2)} logit), which "
         f"bears on 'untriggered tags carry no leak' and on attributing the leak to the "
         f"conditioned pair, not on the gate's FAIL; "
         if lb else "(iii) [control-text bound not computed: local script absent]; ")
      + "(iv) two FINDINGS-3 inequalities are rounding-tight (<= 1.12, <= 0.037).")
    W("")

    # ------------------------------------------------------- values-check
    guard = {
        "outside_repo_allowed": out_refusal(Path("/private/tmp/n9_guard_probe.md"), tracked_now) is None,
        "data_path_refused": out_refusal(REPO / GATES["A"], tracked_now) is not None,
        "tracked_raw_refused": out_refusal(REPO / RAWS["A"], tracked_now) is not None,
        "untracked_results_raw_allowed": out_refusal(
            REPO / "results/raw/2026-10-08_note-N9-guard-probe.md", tracked_now) is None}
    # path checks only: nothing is written; the symlink refusal is by code
    # (p.is_symlink()) and is not exercised here, so that the self-test
    # creates no file
    J["output_guard_selftest"] = guard
    VC = [
        ("1", "The script accepted --out/--json-out but asserted results/raw as the parent, so a "
         "re-run into scratch failed; the final print used relative_to(REPO), which fails outside "
         "the repo.", "fixed",
         f"out_refusal(): relative paths resolve against the repo root; never through a "
         f"symlink; outside the repository any other path is allowed; inside it only "
         f"results/raw/ and never a tracked file. The final print uses the plain path. Guard self-test, computed by this run: "
         f"{guard}."),
        ("2", "The post-hoc control-text lower bounds were rounded UP and so were not valid "
         "lower bounds: in the pass-1 raw, Figures table >= 0.703 / >= 0.349, section 2a and "
         "Summary >= 54.7% (A); the builder's summary also carried >= 0.35 (B).", "fixed",
         f"Every lower bound is now printed with an exact floor (f_down): A >= "
         f"{f_down(lb['A']['control_text_mean_lower_bound_conservative'], 4) if lb else 'n/a'}, B >= "
         f"{f_down(lb['B']['control_text_mean_lower_bound_conservative'], 4) if lb else 'n/a'}; "
         f"shares >= {f_down(100 * lb['A']['control_text_share_of_sum_lower_bound'], 1) if lb else 'n/a'}% "
         f"/ >= {f_down(100 * lb['B']['control_text_share_of_sum_lower_bound'], 1) if lb else 'n/a'}%; "
         f"multiples of the bar >= "
         f"{f_down(lb['A']['lower_bound_over_bar'], 1) if lb else 'n/a'}x / >= "
         f"{f_down(lb['B']['lower_bound_over_bar'], 1) if lb else 'n/a'}x. Section 2a of the "
         f"pass-1 raw had the same defect in three more places, also fixed: A's 'conservative' "
         f"0.7030 (exact "
         f"{f4(lb['A']['control_text_mean_lower_bound_conservative'], 6) if lb else 'n/a'}), "
         f"A's exact-fields '>= 0.7031' (exact "
         f"{f4(lb['A']['control_text_mean_lower_bound'], 6) if lb else 'n/a'}) and B's '3.5x the "
         f"bar' (exact {f4(lb['B']['lower_bound_over_bar'], 4) if lb else 'n/a'}). Section 2a, the Figures row and the Summary all use the floored values."),
        ("3", "The swing-form note did not quote the pre-registration's ', per replicate.' "
         "(:595), which makes the text ambiguous rather than cleanly deviated from.", "fixed",
         f"Section 1 now quotes the whole G1 bullet ({A_g1_span}) and states the ambiguity: the "
         f"swing machinery is cross-replicate ({gate_swing['locator']}, {gate_dcond['locator']}; "
         f"local c1_gate.py {c1l.get('swing_block')}-{c1l.get('mag_ok')}; {prop_swing['locator']}), "
         f"and the code ran the per-replicate form. Round 2 (R2-4) replaced pass 1's reading of "
         f"', per replicate' as pointing against the swing form with both readings, and added "
         f"why only the per-replicate form was computable at gates(A). The Summary's item (ii) "
         f"says the same. No number changed; the bound now also allows for the 4-dp storage."),
        ("4", "The 'leakage gate's bound' row was marked reproduced although only the bar and n "
         "are in the JSON.", "fixed",
         f"Split into two rows: bar 0.10 and n = 32, reproduced from {GJ}:leakage.bar, "
         f"leakage.n; the max / ON-minus-OFF / choice-position definition, log-only at "
         f"{A['prereg_leak0']['locator']}-{A['prereg_leak']['line']} (local d_gates.py lines "
         f"cited). Section 2's Bound bullet says which part is which."),
        ("5", "Referent note 2 answered a '(d) VERDICTS entry' that N9's block text does not "
         "name.", "fixed",
         "Retitled 'Where the (d) verdicts live (N9's block text names no log entry; listed for "
         "N1's ledger)'; the locators are unchanged."),
        ("6", "The smoke-adapter rank comparison mixed a 3-probe G1 cosine with 12-probe ones.",
         "fixed",
         f"Section 2 and the Figures row now say so ({hdr['A_smoke']['locator']}: "
         f"{n_probes['A_smoke']} probes; A and B {n_probes['A']}); the leak maxima are on the "
         f"same 32 texts."),
        ("7", "'172 examples' and 'three epochs' had no locator.", "fixed",
         f"Computed from the committed training stdout: A {misc['train']['A']['n_epochs']} x "
         f"{misc['train']['A']['examples_per_epoch']} ({misc['train']['A']['header']}, "
         f"{misc['train']['A']['epoch_lines']}), B {misc['train']['B']['n_epochs']} x "
         f"{misc['train']['B']['examples_per_epoch']} ({misc['train']['B']['header']}, "
         f"{misc['train']['B']['epoch_lines']}), "
         f"smoke {misc['train']['smoke']['n_epochs']} x "
         f"{misc['train']['smoke']['examples_per_epoch']}; log traces "
         f"{A['gatesA_train']['locator']}, {A['gatesB_train']['locator']}. New log-only row."),
        ("8", "Some Figures-table sources were unpinned or omitted the artifact path.", "fixed",
         f"'FINDINGS-3:117' became {Fd['cos']['locator']}; every JSON source now names "
         f"data/d/gates_rep{{A,B}}.json with its field(s), including the ratio, derived and "
         f"post-hoc rows."),
        ("9", "The menu quote was a fragment (the regex caught only the second half).", "fixed",
         f"The full two-line menu is quoted: `{gm.get('menu')}` (local d_gates.py lines "
         f"{dl.get('menu')}-{(dl.get('menu') or 0) + 1}); the alternate-cycle label swap "
         f"(`{gm.get('leak_swap')}`) is now described too."),
        ("10", "Optional: cite the committed e2a pair order and the base-pair sign argument.",
         "fixed",
         f"Both applied. {E2A_SESS}@{PIN} gives the pair order "
         f"{leak_comp['committed_corroboration']['pair_order_first_seen'] if leak_comp else 'n/a'} "
         f"with one pair per session mod 4 "
         f"({leak_comp['committed_corroboration']['session_mod4_to_single_pair'] if leak_comp else 'n/a'}); "
         f"the stored oriented base-pair comparators have equal magnitude and opposite signs "
         f"({bp_opposite}), so the opposite orientations show in the JSON alone (assuming the "
         f"base phase is replicate-independent); which run is +1 does not (round 2, R2-7)."),
        ("F1 (fixer's own)", "Same rounding-into-a-bound pattern in the swing bound.", "fixed",
         f"D_cond and the swing ceiling are now also given with the 4-dp storage allowed for: "
         f">= {f_down(d_cond_lo)} and <= {f_up(swing_ub_hi)}."),
        ("F2 (fixer's own)", "'1.06 = 1.0625 at 2 dp' was imprecise.",
         "withdrawn in round 2",
         f"The pass-1 wording was correct and has been restored in substance. {rnd['value']} is "
         f"{rnd['distance_to_lower']} from {rnd['lower_2dp']} and {rnd['distance_to_upper']} "
         f"from {rnd['upper_2dp']}; the 2-dp midpoint is {rnd['midpoint_2dp']} (computed by this "
         f"run), so it rounds to {rnd['half_up']} under half-up, half-even, half-down and "
         f"truncation alike. The fixer's replacement text, which put {rnd['value']} at the "
         f"midpoint and had half-up give {rnd['ceiling']}, was false arithmetic; round 2 (R2-1) "
         f"removed it. The Figures row now reads: '{rnd['value']} rounds to {rnd['half_up']} at "
         f"2 dp under any standard rule (the 2-dp midpoint is {rnd['midpoint_2dp']}); the "
         f"record's 1.06 is the correct rounding.'"),
        ("F3 (fixer's own)", "'untriggered tags carry no leak ... was not a measured quantity in "
         "the record' claimed more than was checked.", "fixed",
         "Now: 'is stated without a stored per-tag measurement: the gate artifacts keep only the "
         "maximum and the mean over all 32 texts' (the two JSONs, as printed above)."),
    ]
    J["values_check"] = [{"finding": a, "claim": b, "disposition": c, "detail": d}
                         for a, b, c, d in VC]
    VC2 = [
        ("R2-1", "substantive",
         "Figures row 'max 1.06 (B)' and Values-check row F2 said 1.0625 is the exact midpoint "
         "of 1.06 and 1.07 and that half-up would give 1.07: false arithmetic, hardcoded prose.",
         "fixed",
         f"Computed by this run (decimal quantize to 0.01): {rnd['value']} -> half-up "
         f"{rnd['half_up']}, half-even {rnd['half_even']}, half-down {rnd['half_down']}, "
         f"truncation {rnd['truncation']}; distances {rnd['distance_to_lower']} / "
         f"{rnd['distance_to_upper']}; 2-dp midpoint {rnd['midpoint_2dp']}; only directed "
         f"rounding up (ceiling) gives {rnd['ceiling']}. The Figures row now carries the fix's "
         f"sentence ('... rounds to {rnd['half_up']} at 2 dp under any standard rule (the 2-dp "
         f"midpoint is {rnd['midpoint_2dp']}); the record's 1.06 is the correct rounding'), "
         f"built from these values and asserted (the script stops if the rules disagree or the "
         f"half-up value is not 1.06). Row F2 is rewritten: the pass-1 wording was correct and "
         f"is restored in substance; F2's disposition is now 'withdrawn in round 2'. The "
         f"Values-check intro no longer says every right-hand entry is computed. No number or "
         f"status changed."),
        ("R2-2", "minor",
         "The 'scaling with installation strength' row cited only the smoke raw stdout, not "
         "where the record states the claim.",
         "fixed",
         f"The row's source now lists the record's statements: {ARCH}@{PIN}:"
         f"{A['gatesA_scale']['line']}-{A['gatesA_smoke']['line']}, "
         f":{A['adj_scale_a']['line']}-{A['adj_scale_b']['line']}, "
         f":{A['gatesB_scale_a']['line']}-{A['gatesB_scale_b']['line']}; {Fd['scale']['locator']} "
         f"and {Fd['table']['locator']} (each located by its text and the line pairs asserted "
         f"adjacent). Section 2's smoke bullet cites the same."),
        ("R2-3", "minor",
         "Two cited phrases span two lines but were cited at one line ('G2(B) 1.02/1.03'; "
         "FINDINGS-3's 'untriggered tags carry no leak').",
         "fixed",
         f"Now {ARCH}@{PIN}:{A['gatesB_g2']['line']}-{A['gatesB_g2b']['line']} and "
         f"{Fd['noleak_a']['locator']}-{Fd['noleak']['line']}. The same check found two more "
         f"instances of the pattern, fixed the same way: G2(A)'s '1.03 (MSE) / 1.12 (KL)' is "
         f"now {A['gatesA_g2']['locator']}-{A['gatesA_g2b']['line']}, and gates(B)'s "
         f"counterbalance read (the raw cosine flipping sign, section 1) is now "
         f"{A['gatesB_flip']['locator']}-{A['gatesB_flip_end']['line']}. The archive's "
         f"'untriggered tags carry no leak' ({A['adj_noleak']['locator']}) is on one line and "
         f"is unchanged."),
        ("R2-4", "minor",
         "Section 1 and Summary (ii) said ', per replicate' points against the swing form, an "
         "overstated reading.",
         "fixed",
         f"Reworded as the fix gives it: the run applied the per-replicate P2 form; at "
         f"gates(A) only that form was computable (B's training was deferred until the d2 "
         f"read was adjudicated, {ARCH}@{PIN}:{A['adj_deferB_a']['line']}-"
         f"{A['adj_deferB_b']['line']}; A's gate stdout entered at "
         f"`{raw_commit[RAWS['A']].split()[0]}`, B's training stdout at "
         f"`{trainB_commit.split()[0]}`); the cross-replicate swing was never computed in the "
         f"record (scanned by this run: 'swing' on lines "
         f"{swing_scan['archive_d_lines_with_swing']} of {swing_scan['archive_d_span']}, all "
         f"inside the G1 pre-registration bullet, and "
         f"{sum(swing_scan['counts_elsewhere'].values())} times in FINDINGS-3, the two gate raws "
         f"and the two artifacts); a bound from the stored fields shows it passes. Both "
         f"readings of ', per replicate' are given. Row 3's detail is updated to match."),
        ("R2-5", "minor",
         "No Figures row for 'rank-8 adapter', which the preprint's weight-channel sentence "
         "carries.",
         "fixed",
         f"New log-only row 'rank-8 adapter, last 8 layers (56-63)': rank "
         f"{rank_row['rank_prereg']} at {A['prereg_rank']['locator']} and "
         f"{ARCH}@{PIN}:{A['go_rank']['line']}-{A['go_layermap']['line']}; layers "
         f"{rank_row['layermap_layers']} of {rank_row['layermap_n_layers']} at "
         f"{misc['layermap']['locator']}; consistent: {rank_row['consistent']}; keys containing "
         f"'rank' in the two gate JSONs: {rank_row['committed_json_keys_with_rank'] or 'none'}"
         + (f"; preprint {pre['rank']['locator']}" if pre else "") + ". Referent note 5 names "
         f"the phrase."),
        ("R2-6", "minor",
         "Section 3 ('max control-pair displacement') and the G3 row ('floor 103') did not say "
         "that G3's comparator is adapter-arm and the maximum of the 28 control-pair distances, "
         "where the pre-registration says 'the control-pair floor of base'; FINDINGS-3's '12' "
         "is A's value only.",
         "fixed",
         f"Section 3 and the G3 row now say: adapter-arm, and the 'floor' is the maximum over "
         f"the 28 control-tag pairs of the L2 distance between their fingerprints (the most "
         f"lenient choice; local d_gates.py lines {dl.get('ctrl_disp')}-{dl.get('g3')}), not "
         f"computed on the base arm, though the pre-registration words it as 'the control-pair "
         f"floor of base' "
         f"({ARCH}@{PIN}:{A['prereg_g3']['line']}); '12' is A's "
         f"{f4(G3['A']['bare_disp'], 3)} (B {f4(G3['B']['bare_disp'], 3)}). Status stays "
         f"reproduced: the stored fields are the gated quantities."),
        ("R2-7", "minor",
         "The 'raw cosine flips sign' row's status rests on an orientation rule that is "
         "log-only and on local code for cos_base_pair being stored oriented.",
         "fixed",
         f"The fix's second option: the row (and section 1) now state that the JSON alone does "
         f"not fix which run is +1; the rule is log-only ({A['go_reps']['locator']}) and in the "
         f"local d_gates.py (line {dl.get('orient')}); that `cos_base_pair` is stored oriented "
         f"is local d_gates.py line {dl.get('cos_base')} (written at line "
         f"{dl.get('json_cos_base_pair')}). The status cell stays inside the vocabulary "
         f"(reproduced)."),
        ("R2-8", "minor",
         "Section 2a(1) tied the 1/16 grid to bf16 without the magnitude condition.",
         "fixed",
         f"Added 'if the label logits are of magnitude >= 8', with the bf16 spacing computed by "
         f"this run: " + ", ".join(f"{bf[k]:g} at {k}" for k in bf) + "; asserted against the "
         f"prose bands. The Figures row 'grid' says the same. The grid arithmetic is unchanged "
         f"(maxima x 16 = {int(grid['A']['max_x16'])}, {int(grid['B']['max_x16'])}, "
         f"{int(grid['A_smoke']['max_x16'])})."),
    ]
    J["values_check_round2"] = [{"finding": a, "severity": s, "claim": b, "disposition": c,
                                 "detail": d} for a, s, b, c, d in VC2]
    W("## Values-check (pass 1 and round 2 findings and dispositions)")
    W("")
    W("### Pass 1")
    W("")
    W("A separate checker reran the pass-1 script (sha256 2c313019...c8ad) and reported 110 "
      "claims checked, no STOP and no substantive finding: nine minor defects (1-9) and one "
      "item of two optional strengthenings (10). The fixer applied all ten and found three "
      "more of the same kind (F1-F3). In the right-hand column the numbers and locators are "
      "computed by this run, except the pass-1 values that rows 2 and 8 quote (the defects "
      "they fixed); rows 5 and F3 are prose about wording, and row F2 is prose built on "
      "values computed by this run. Row F2 was withdrawn in round 2 (R2-1).")
    W("")
    W("| # | finding | disposition | what changed |")
    W("|---|---|---|---|")
    for a, b, c, d in VC:
        W(f"| {a} | {cell(b)} | {c} | {cell(d)} |")
    W("")
    W("### Round 2 (tier-2 round-2 residual findings)")
    W("")
    W(f"A second check of the pass-1-fixed outputs (script sha256 "
      f"86dd4bd5...bb74) left {len(VC2)} residual findings: "
      f"{sum(1 for v in VC2 if v[1] == 'substantive')} substantive, "
      f"{sum(1 for v in VC2 if v[1] == 'minor')} minor. Each was checked by a tool run before "
      f"it was applied, and all {sum(1 for v in VC2 if v[3] == 'fixed')} were applied as their "
      f"fixes give them; none was rejected. No existing figure's value or status changed, and "
      f"no gate verdict; one log-only row was added (R2-5). The numbers and locators in the "
      f"right-hand column are computed by this run; the round-2 check was post-hoc on the "
      f"audit's own outputs, not on the record.")
    W("")
    W("| # | severity | finding | disposition | what changed |")
    W("|---|---|---|---|---|")
    for a, s, b, c, d in VC2:
        W(f"| {a} | {s} | {cell(b)} | {c} | {cell(d)} |")
    W("")

    out_md.write_text("\n".join(md) + "\n", encoding="utf-8")
    out_js.write_text(json.dumps(J, indent=1, ensure_ascii=False, default=str) + "\n",
                      encoding="utf-8")
    print(f"wrote {out_md} and {out_js}")
    print(f"raw==json: {raw_eq}; block {block_sha[:8]}...{block_sha[-4:]} "
          f"{'MATCH' if block_ok else 'MISMATCH'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
