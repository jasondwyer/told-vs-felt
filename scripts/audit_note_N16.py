#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N16: the decoding-parameters table.

Block item N16 (AUDIT-note-release-v1_2.md@bbc9ffe:121-122): for every
generated-text DV the note carries -- temperature, top-p / top-k, max new
tokens, seed policy, stop tokens / stop discipline, the scaffold-token ban
list, cached vs uncached path, and the commit that fixed them -- one table.

READ-ONLY. Every repository read is `git show bbc9ffe:<path>` (or
`git show <data commit>:<path>` for the runner code at a run's commit).
Nothing is imported from the working tree. Record code that is executed
(the seed-stream replays) is compiled from bbc9ffe into an isolated
namespace: valence_core/session_e2a.py (whole) and
valence_core/detection.py:plan_trials. No model, no tokenizer library, no
network. Two inputs lie outside the record and are labelled so wherever
used: (a) the gitignored jlens-qwen36 clone's runner files (read as text,
context only; never git inside it), (b) the local Qwen snapshot's
tokenizer_config.json / tokenizer.json / generation_config.json (read as
JSON; the record's "single local snapshot", RESULTS.md@bbc9ffe:4968-4969).

Status vocabulary (task rule 4; same mapping as the N2 raw's section 1(c)):
  reproduced  -- an artifact field records the value, or this script
                 establishes it by replaying committed artifacts;
  log-only    -- no artifact field; committed prose states it (pinned
                 locator), with the committed code line beside it;
  not found   -- neither; where committed code at the run's commit fixes the
                 value it is given as 'code-fixed' and flagged to the PI;
  computed-new-- a computation the record does not contain;
  discrepant  -- the record disagrees with itself or with a sibling raw.

Usage:
  .../jlens-qwen36/.venv/bin/python scripts/audit_note_N16.py \
      [--out results/raw/2026-10-08_note-N16-decoding.md] \
      [--json-out results/raw/2026-10-08_note-N16-decoding.json]
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import zlib
from collections import Counter

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA_ROUTED = ("8cd8a9ac", "3841")
CLONE = os.path.join(REPO, "jlens-qwen36")
QWEN_SNAP_GLOB = os.path.expanduser(
    "~/.cache/huggingface/hub/models--mlx-community--Qwen3.6-27B-4bit/snapshots")
N2_RAW = "results/raw/2026-10-08_note-N2-introspection.md"
N4_RAW = "results/raw/2026-10-08_note-N4-e2a.md"
N4_JSON = "results/raw/2026-10-08_note-N4-e2a.json"
N4_SCRIPT = "scripts/audit_note_N4.py"
CAP_SESSIONS = 60

OUT_LINES: list[str] = []


def emit(s: str = "") -> None:
    OUT_LINES.append(s)


# ----------------------------------------------------------------- git helpers
def git(*args: str) -> str:
    """git's stdout, decoded byte-exact. Round-2 finding 1: subprocess's text
    mode (universal newlines) turns every bare '\\r' into '\\n', so tqdm's
    '\\rFetching 14 files' progress line became extra lines and every log
    locator below it in two e2a raws was off by two. Decoding the bytes
    keeps the file as `git show <commit>:<path> | sed -n '<n>p'` sees it."""
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.decode('utf-8', 'replace').strip()}")
    return r.stdout.decode("utf-8")


def lines_of(text: str) -> list[str]:
    """Lines as `sed -n '<n>p'` numbers them: split on '\\n' only (round-2
    finding 1; str.splitlines() also breaks at a bare '\\r', \\x0b, \\x0c,
    \\x1c-\\x1e, \\x85 and \\u2028/\\u2029). A final newline ends the last
    line instead of opening an empty one, so len() equals `wc -l`. Every
    line number this script emits is an index into this list."""
    parts = text.split("\n")
    if parts and parts[-1] == "":
        parts.pop()
    return parts


def read_bytes_text(path: str) -> str:
    """A working-tree file decoded byte-exact (no newline translation), so
    its sha256 is the file's and its line numbers are sed's."""
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8")


SPLITLINES_ONLY = ("\r", "\x0b", "\x0c", "\x1c", "\x1d", "\x1e", "\x85", " ", " ")
SHOWN: dict[str, list[str]] = {}   # "path@commit" -> the splitlines-only separators it contains


def show(path: str, commit: str = PIN) -> str:
    t = git("show", f"{commit}:{path}")
    SHOWN[f"{path}@{commit}"] = [repr(c) for c in SPLITLINES_ONLY if c in t]
    return t


def jload(path: str, commit: str = PIN):
    return json.loads(show(path, commit))


def jlload(path: str, commit: str = PIN) -> list[dict]:
    return [json.loads(l) for l in lines_of(show(path, commit)) if l.strip()]


def full(commit: str) -> str:
    return git("rev-parse", commit).strip()


def blob(commit: str, path: str) -> str | None:
    try:
        return git("rev-parse", f"{commit}:{path}").strip()
    except RuntimeError:
        return None


def commits_of(path: str) -> list[str]:
    """Commits touching `path` in PIN's history, oldest first."""
    out = git("log", "--format=%h", PIN, "--", path).split()
    return list(reversed(out))


def cdate(commit: str) -> str:
    return git("log", "-1", "--format=%ad", "--date=short", commit).strip()


def find_line(commit: str, path: str, pattern: str) -> tuple[int, str] | None:
    rx = re.compile(pattern)
    for i, line in enumerate(lines_of(show(path, commit)), start=1):
        if rx.search(line):
            return i, line.strip()
    return None


def loc(commit: str, path: str, pattern: str) -> str:
    hit = find_line(commit, path, pattern)
    if hit is None:
        raise SystemExit(f"LOCATOR MISSING: /{pattern}/ not in {path}@{commit}")
    return f"{path}@{commit}:{hit[0]}"


def intro(path: str, literal: str, follow: bool = False) -> str:
    """Oldest commit in PIN's history whose diff changes the count of
    `literal` in `path` (git log -S), i.e. the commit that introduced it."""
    args = ["log", "--format=%h", "-S", literal]
    if follow:
        args.append("--follow")
    out = git(*args, PIN, "--", path).split()
    if not out:
        raise SystemExit(f"INTRO MISSING: {literal!r} never in {path}")
    return out[-1]


def intro_paths(paths: list[str], literal: str) -> str:
    """Oldest commit in PIN's history whose diff changes the count of
    `literal` in any of `paths` (git log -S over several paths; used for
    the log, which moved from RESULTS.md to archive/ at c07a5e0)."""
    out = git("log", "--format=%h", "-S", literal, PIN, "--", *paths).split()
    if not out:
        raise SystemExit(f"INTRO MISSING: {literal!r} never in {paths}")
    return out[-1]


def intro_follow_detail(path: str, literal: str) -> dict:
    """Both forms of git log -S for a renamed file: with --follow (the
    commit that introduced the literal, under the file's earlier name) and
    without (oldest hit on the current path, which is the rename)."""
    fol = intro(path, literal, follow=True)
    try:
        nof = intro(path, literal, follow=False)
    except SystemExit:
        nof = None
    old = None
    if fol != nof:
        out = git("log", "--follow", "--format=%h", "--name-only", "-S", literal, PIN, "--", path)
        flat = out.split()
        # the path printed right after the oldest hash is the file's name then
        if fol in flat:
            i = flat.index(fol)
            old = flat[i + 1] if i + 1 < len(flat) else None
    return {"follow": fol, "no_follow": nof, "path_at_follow_hit": old}


def md_row(cells) -> str:
    """One markdown table row; a literal '|' inside a cell is escaped so
    every row keeps the header's column count (checker finding 5)."""
    return "| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in cells) + " |"


def fn_src(commit: str, path: str, name: str) -> str | None:
    """Source text of the top-level function `name` in `path` at `commit`."""
    src = show(path, commit)
    for node in ast.parse(src).body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(src, node)
    return None


def gen_src(commit: str, path: str) -> str | None:
    """Source text of the adapter's generate() method at `commit`."""
    try:
        src = show(path, commit)
    except RuntimeError:
        return None
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name == "generate":
            return ast.get_source_segment(src, node)
    return None


def log_line(text: str, pattern: str, start: int = 1) -> int:
    rx = re.compile(pattern)
    for i, line in enumerate(lines_of(text), start=1):
        if i >= start and rx.search(line):
            return i
    raise SystemExit(f"LOG LOCATOR MISSING: /{pattern}/")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# --------------------------------------------- record code, compiled from PIN
def compile_module(path: str, names: list[str] | None = None) -> dict:
    src = show(path)
    ns: dict = {"__name__": f"pinned_{os.path.basename(path)[:-3]}",
                "np": np, "numpy": np}
    if names is None:
        exec(compile(src, f"{path}@{PIN}", "exec"), ns)
        return ns
    tree = ast.parse(src)
    keep = [n for n in tree.body
            if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names]
    mod = ast.Module(body=keep, type_ignores=[])
    exec(compile(mod, f"{path}@{PIN}", "exec"), ns)
    return ns


SE = compile_module("valence_core/session_e2a.py")
PLAN = compile_module("valence_core/detection.py", ["plan_trials"])["plan_trials"]

TASKS = [json.loads(l) for l in lines_of(show("data/corpus/e2a_tasks.jsonl"))
         if l.strip()]
assert len(TASKS) >= 16 and all(len(t["paraphrases"]) == 4 for t in TASKS)


# ------------------------------------------------------------- replay helpers
def replay_session_family(rows, key_of, n_forced: int):
    """Replay the e2a draw order (valence_core/session_e2a.py@PIN: one
    session_rng(key, idx); permutation(16)[:n]; then integers(4) for each of
    the n planned rounds, all before any seed; then a generation seed per
    forced round, and integers(2) (menu order) then a seed per free round)
    against every recorded seed and task id."""
    n_sess = n_seed_ok = n_task_ok = n_seeds = 0
    n_unseeded = [0]
    bad = []
    for row in rows:
        idx = int(row["session"])
        key = key_of(row)
        rng = SE["session_rng"](key, idx)
        seq = SE["task_sequence"](rng, TASKS, n_forced + SE["N_FREE"])
        ok_seed = ok_task = True
        ti = 0
        for r in row["rounds"]:
            s = int(rng.integers(2 ** 31))
            n_seeds += 1
            ok_seed &= (s == r["seed"])
            if "task" in r and re.fullmatch(r"t\d\d", str(r["task"])):
                ok_task &= (seq[ti][0] == r["task"])
            ti += 1
        for c in row["choices"]:
            rng.integers(2)
            if "seed" not in c:
                # a read with no generated round after it (H1's declared
                # stop fires between the read and the round): the runner
                # draws no seed, so neither does the replay
                n_unseeded[0] += 1
                break
            s = int(rng.integers(2 ** 31))
            n_seeds += 1
            ok_seed &= (s == c["seed"])
            if "task" in c and re.fullmatch(r"t\d\d", str(c["task"])):
                ok_task &= (seq[ti][0] == c["task"])
            ti += 1
        n_sess += 1
        n_seed_ok += int(ok_seed)
        n_task_ok += int(ok_task)
        if not ok_seed and len(bad) < 3:
            bad.append((key, idx))
    return {"n_sessions": n_sess, "seed_streams_match": n_seed_ok,
            "task_streams_match": n_task_ok, "n_seeds_checked": n_seeds,
            "n_reads_without_round": n_unseeded[0], "first_mismatches": bad}


def cap_check(items, cap: int):
    """cap_hit iff n_tok == cap (n_tok excludes the stop token; a cap hit
    appends `cap` tokens with no stop)."""
    n = hits = consistent = at_cap = 0
    mx = 0
    for x in items:
        if "n_tok" not in x or "cap_hit" not in x:
            continue
        n += 1
        hits += int(bool(x["cap_hit"]))
        at_cap += int(x["n_tok"] == cap)
        consistent += int(bool(x["cap_hit"]) == (x["n_tok"] == cap))
        mx = max(mx, int(x["n_tok"]))
    return {"n": n, "cap_hits": hits, "n_tok_eq_cap": at_cap,
            "consistent": consistent, "max_n_tok": mx,
            "all_consistent": consistent == n and n > 0}


def items_of(rows):
    for row in rows:
        for x in row.get("rounds", []):
            yield x
        for x in row.get("choices", []):
            yield x


def stop_tally(rows):
    c = Counter()
    for x in items_of(rows):
        if "stop_reason" in x:
            c[x["stop_reason"]] += 1
    return dict(c)


def count_key(obj, key: str) -> dict:
    """All occurrences of `key` anywhere in a JSON tree (N4's counting)."""
    c = Counter()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == key and not isinstance(v, (dict, list)):
                    c[json.dumps(v)] += 1
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(obj)
    return dict(c)


def banned_hits(texts, strings) -> int:
    return sum(1 for t in texts for s in strings if s in t)


# ======================================================================= main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(
        REPO, "results/raw/2026-10-08_note-N16-decoding.md"))
    ap.add_argument("--json-out", default=os.path.join(
        REPO, "results/raw/2026-10-08_note-N16-decoding.json"))
    args = ap.parse_args()

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True).stdout.strip()
    head = full("HEAD")
    pin_full = full(PIN)
    block_text = show(BLOCK)
    block_sha = sha256_bytes(block_text.encode())
    block_match = block_sha.startswith(BLOCK_SHA_ROUTED[0]) and block_sha.endswith(BLOCK_SHA_ROUTED[1])
    block_lines = lines_of(block_text)
    n16_ok = block_lines[120].startswith("### N16") and "Decoding-parameters" in block_lines[120]
    script_path = os.path.relpath(os.path.abspath(__file__), REPO)
    script_sha = sha256_bytes(open(os.path.abspath(__file__), "rb").read())
    cmd = " ".join([sys.executable] + [script_path] + sys.argv[1:])

    J: dict = {"item": "N16", "block": BLOCK, "block_sha256": block_sha,
               "record_commit": pin_full, "head_at_run": head,
               "script": script_path, "script_sha256": script_sha,
               "interpreter": sys.executable, "python": platform.python_version(),
               "numpy": np.__version__, "command": cmd, "code_stamp": stamp}

    RES = show("RESULTS.md")
    RC34 = show("archive/RESULTS-cycles3-4.md")
    GPORT = show("results/raw/2026-10-07_m-gport_differences.md")
    CLAUDE = show("CLAUDE.md")
    PROPF = show("PROPOSAL-f-natural-reinforcer-screen.md")
    PROPJ = show("PROPOSAL-j-dose-escalation.md")   # e2d's governing pre-registration (round-2 finding 3)

    # ---------------------------------------------------------- ban list file
    ban_txt = show("data/configs/e2a_ban_list.json")
    ban = json.loads(ban_txt)
    ban_sha = sha256_bytes(ban_txt.encode())
    ban16 = ban_sha[:16]
    ban_commit = commits_of("data/configs/e2a_ban_list.json")[0]
    ban_fields = {
        "data/e2a/g2_discriminability.json:ban_sha": jload("data/e2a/g2_discriminability.json")["ban_sha"],
        "data/e2a/g2_discriminability_v2.json:ban_sha": jload("data/e2a/g2_discriminability_v2.json").get("ban_sha"),
        "data/e2a/g2_spotcheck.json:ban_sha": jload("data/e2a/g2_spotcheck.json")["ban_sha"],
        "data/f/calib.json:ban_sha": jload("data/f/calib.json")["ban_sha"],
    }
    J["ban_list_file"] = {"path": "data/configs/e2a_ban_list.json", "sha256": ban_sha,
                          "n_strings": len(ban["strings"]), "n_ids": len(ban["ids"]),
                          "strings": ban["strings"], "ids": ban["ids"],
                          "first_commit": ban_commit, "recorded_sha16_fields": ban_fields}

    # local Qwen snapshot (OUTSIDE the record; JSON reads only)
    qwen_local = {}
    try:
        snaps = sorted(os.listdir(QWEN_SNAP_GLOB))
        if len(snaps) == 1:
            sd = os.path.join(QWEN_SNAP_GLOB, snaps[0])
            tc = json.load(open(os.path.join(sd, "tokenizer_config.json")))
            tj = json.load(open(os.path.join(sd, "tokenizer.json")))
            gc_raw = open(os.path.join(sd, "generation_config.json"), "rb").read()
            added = {a["content"]: a["id"] for a in tj["added_tokens"]}
            eos = tc.get("eos_token")
            eos = eos["content"] if isinstance(eos, dict) else eos
            qwen_local = {
                "snapshot": snaps[0][:8] + "...",
                "eos_token": eos, "eos_id": added.get(eos),
                "eos_id_in_ban_ids": added.get(eos) in ban["ids"],
                "endoftext_id": added.get("<|endoftext|>"),
                "endoftext_in_ban_ids": added.get("<|endoftext|>") in ban["ids"],
                "ban_strings_to_ids_local": {s: added.get(s) for s in ban["strings"]},
                "ban_ids_equal_local_map": sorted(added.get(s) for s in ban["strings"]) == sorted(ban["ids"]),
                "generation_config_sha16": sha256_bytes(gc_raw)[:16],
                "generation_config": json.loads(gc_raw),
            }
    except (OSError, KeyError, ValueError) as exc:          # pragma: no cover
        qwen_local = {"error": str(exc)}
    J["qwen_local_snapshot_outside_record"] = qwen_local

    # clone files (OUTSIDE the record; text reads only, never git inside)
    clone = {}
    for rel in ("jlens_qwen/e2a.py", "scripts/e2a_sessions.py",
                "scripts/f_sessions.py", "scripts/e2a_g2_discriminability.py"):
        p = os.path.join(CLONE, rel)
        if os.path.exists(p):
            b = open(p, "rb").read()
            clone[rel] = {"sha256": sha256_bytes(b), "lines": lines_of(b.decode("utf-8"))}

    def cl(rel: str, pattern: str) -> str:
        if rel not in clone:
            return f"jlens-qwen36/{rel} (absent on this machine)"
        rx = re.compile(pattern)
        for i, line in enumerate(clone[rel]["lines"], start=1):
            if rx.search(line):
                return f"jlens-qwen36/{rel}:{i}"
        return f"jlens-qwen36/{rel} (pattern absent)"
    J["clone_files_outside_record"] = {k: v["sha256"] for k, v in clone.items()}

    EV: dict = {}   # evidence, family by family

    # =============================================================== e2a
    e2a_rows = jlload("data/e2a/sessions.jsonl")
    ok = seeds_ok = 0
    for row in e2a_rows:
        r = SE["verify_archived_session"](row, TASKS)
        ok += int(r["ok"])
        seeds_ok += int(r.get("seeds_match", False))
    e2a_cap = cap_check(items_of(e2a_rows), CAP_SESSIONS)
    EV["e2a"] = {
        "artifact": "data/e2a/sessions.jsonl", "commit": commits_of("data/e2a/sessions.jsonl")[-1],
        "n_sessions": len(e2a_rows),
        "n_rounds_generated": sum(r["n_rounds_generated"] for r in e2a_rows),
        "walk_reconstructed": ok, "seed_streams_matched": seeds_ok,
        "cap": e2a_cap,
        "banned_string_hits_in_transcripts": banned_hits((r["transcript"] for r in e2a_rows), ban["strings"]),
        "row_fields_present": sorted(e2a_rows[0].keys()),
        "temp_field": any("temp" in k for k in e2a_rows[0]),
        "path_field": any("cach" in k or "path" in k for k in e2a_rows[0]),
    }

    # g2 corpora (readability gate; S1's corpus is g2_rounds_f0.1.json)
    g2 = {}
    for path, frac in (("data/e2a/g2_rounds_f0.1.json", 0.1),
                       ("data/e2a/g2_rounds_f0.1_v2.json", 0.1),
                       ("data/e2a/g2_rounds_f0.2_v2.json", 0.2)):
        d = jload(path)
        n = m = caps = nl = 0
        for pole in ("pos", "neg"):
            for x in d[pole]:
                n += 1
                want = zlib.crc32(f"{x['task_id']}|{x['para']}|{pole}|{frac}".encode()) % 2 ** 31
                m += int(want == x["seed"])
                caps += int(bool(x.get("cap_hit")))
                nl += int("\n" in x["text"])
        g2[path] = {"n_rounds": n, "seed_formula_matches": m, "cap_hits": caps,
                    "texts_with_newline": nl, "commit": commits_of(path)[-1],
                    "texts_with_think": sum(1 for pole in ("pos", "neg") for x in d[pole] if "<think>" in x["text"]),
                    "has_cap_hit_field": all("cap_hit" in x for pole in ("pos", "neg") for x in d[pole])}
    g2d = jload("data/e2a/g2_discriminability.json")
    g2d2 = jload("data/e2a/g2_discriminability_v2.json")
    EV["g2"] = {"rounds": g2,
                "g2r2_use_cached": g2d["fracs"]["0.1"]["use_cached"],
                "g2r_use_cached": g2d2["fracs"]["0.1"]["use_cached"],
                "g2r2_template_family": g2d["template_family"],
                "g2r_template_family": g2d2.get("template_family")}

    # =============================================================== S1 judge
    s1 = jload("data/e2a/s1_judge_rescue.json")
    s1_rows = [r for c in s1["cells"].values() for r in c["rows"]]
    s1_src = show("scripts/s1_judge_rescue.py", "f526377")
    EV["s1"] = {"artifact": "data/e2a/s1_judge_rescue.json",
                "commit": commits_of("data/e2a/s1_judge_rescue.json")[-1],
                "n_cells": len(s1["cells"]), "n_reads": len(s1_rows),
                "row_keys": sorted(s1_rows[0].keys()),
                "any_generated_text_field": any(k in s1_rows[0] for k in ("text", "response", "n_tok")),
                "corpus": s1["corpus"],
                "pick_rule_consistent": sum(1 for r in s1_rows
                                            if ((r["p_A"] >= r["p_B"]) == r["a_is_pos"]) == r["picked_pos"]),
                "generate_calls_in_runner": len(re.findall(r"\.generate\(", s1_src)),
                "rng_uses": [i for i, l in enumerate(lines_of(s1_src), 1) if re.search(r"\brng\b", l)],
                "runner_blob_equal_pin": blob("f526377", "scripts/s1_judge_rescue.py") == blob(PIN, "scripts/s1_judge_rescue.py")}

    # =============================================================== f1
    f_rows = jlload("data/f/sessions.jsonl")
    pools = jload("data/f/pools.json")
    sizes = {k: len(v) for k, v in pools.items() if isinstance(v, list)}
    need = 8
    tag_pairs = [("slate", "prism"), ("maple", "cedar"), ("granite", "lattice"), ("plaza", "saddle")]

    def f_items_draws(arm, s, rng):
        if arm == "SOLV":
            rng.permutation(sizes["SOLV_P"]); rng.permutation(sizes["SOLV_Q"])
        elif arm == "DIFF":
            rng.permutation(sizes["DIFF_easy"]); rng.permutation(sizes["DIFF_hard"])
        elif arm == "NOV":
            rng.permutation(sizes["NOV"] - 1)
        elif arm == "CORR":
            rng.permutation(sizes["CORR_clean"])
        elif arm == "FDBK":
            rng.permutation(sizes["FDBK"])
        else:
            rng.permutation(sizes["SHAM"])

    f_ok = f_menu_ok = f_seeds = 0
    f_bad = []
    for row in f_rows:
        arm, s = row["arm"], int(row["session"])
        rng = np.random.default_rng(zlib.crc32(f"f|{arm}|{s}".encode()) % 2 ** 31)
        f_items_draws(arm, s, rng)
        pair = tag_pairs[s % 4]
        tP, tQ = (pair[1], pair[0]) if (s // 4) % 2 == 1 else pair
        nF = 4 if len(row["rounds"]) >= 4 else len(row["rounds"])
        good = menu_good = True
        for r in row["rounds"][:nF]:
            good &= int(rng.integers(2 ** 31)) == r["seed"]; f_seeds += 1
        for ci, c in enumerate(row["choices"]):
            a = tP if rng.integers(2) == 0 else tQ
            menu_good &= (a == c["menu_a"])
            sd = int(rng.integers(2 ** 31)); f_seeds += 1
            if nF + ci < len(row["rounds"]):
                good &= sd == row["rounds"][nF + ci]["seed"]
        f_ok += int(good)
        f_menu_ok += int(menu_good)
        if not good and len(f_bad) < 3:
            f_bad.append((arm, s))
    EV["f1"] = {"artifact": "data/f/sessions.jsonl", "commit": commits_of("data/f/sessions.jsonl")[-1],
                "n_sessions": len(f_rows), "seed_streams_match": f_ok,
                "menu_orders_match": f_menu_ok, "n_seeds_checked": f_seeds,
                "first_mismatches": f_bad, "pool_sizes": sizes,
                "n_rounds": sum(len(r["rounds"]) for r in f_rows),
                "cap": cap_check((x for r in f_rows for x in r["rounds"]), CAP_SESSIONS),
                "banned_string_hits_in_transcripts": banned_hits((r["transcript"] for r in f_rows), ban["strings"]),
                "temp_field": any("temp" in k for k in f_rows[0]),
                "calib_ban_sha": ban_fields["data/f/calib.json:ban_sha"]}

    # =============================================================== e2b
    e2b = {}
    def stop_cap_def(commit: str) -> str:
        """Where STOP_CAP = 60 is defined at `commit`: the Route-3 module was
        valence_core/e2b/session.py until its rename at 1465b34 (checker
        finding 12), valence_core/session_e2a.py after."""
        for p in ("valence_core/session_e2a.py", "valence_core/e2b/session.py"):
            try:
                hit = find_line(commit, p, r"^STOP_CAP = 60")
            except RuntimeError:
                continue
            if hit:
                return f"{p}@{commit}:{hit[0]}"
        raise SystemExit(f"STOP_CAP definition not found at {commit}")

    def touched(commit: str, paths: list[str]) -> list[str]:
        """Which of `paths` the commit itself changed (a data commit that also
        changes runner code is not the code that ran; checker finding 3)."""
        out = git("show", "--format=", "--name-only", commit, "--", *paths).split()
        return sorted(set(out))

    for path, key_of, key_txt, runner, run_commit in (
            ("data/e2b/h1u_sessions.json", lambda r: "h1", '"h1"', "scripts/e2b_h1_sessions.py", "b2d051b"),
            ("data/e2b/h1_sessions.json", lambda r: "h1", '"h1"', "scripts/e2b_h1_sessions.py", "6df2072"),
            ("data/e2b/h2_sessions.json", lambda r: "h2", '"h2"', "scripts/e2b_h2_sessions.py", None),
            ("data/e2b/verdict_campaign.json", lambda r: f"e2b-{r['arm']}", 'f"e2b-{arm}"', "scripts/e2b_verdict_campaign.py", None)):
        d = jload(path)
        rows = d["sessions"]
        dc = commits_of(path)[-1]
        rc = run_commit or dc
        anc = subprocess.run(["git", "merge-base", "--is-ancestor", ban_commit, rc], cwd=REPO).returncode == 0
        e2b[path] = {
            "data_commit_touched_runner_code": touched(dc, [runner, "valence_core/adapters/qwen_mlx.py",
                                                            "valence_core/e2b/session.py", "valence_core/session_e2a.py"]),
            "runner_changed_between_run_and_data_commit": (git("log", "--format=%h", f"{rc}..{dc}", "--", runner,
                                                               "valence_core/adapters/qwen_mlx.py",
                                                               "valence_core/e2b/session.py").split() if rc != dc else []),
            "stop_cap_def": stop_cap_def(rc),
            "session_e2a_py_exists_at_run_commit": blob(rc, "valence_core/session_e2a.py") is not None,
            "data_commit": dc, "runner": runner, "runner_commit": rc, "key": key_txt,
            "ban_file_committed_at_run_commit": anc,
            "runner_blob_equal_pin": blob(rc, runner) == blob(PIN, runner),
            "temp": d.get("temp"), "round_path_cached": d.get("round_path_cached"),
            "frac": d.get("frac"), "order_seed": d.get("order_seed"),
            "provenance_gdn": d["provenance"].get("gdn_inference_mode"),
            "legacy_truncate_512": d["provenance"].get("legacy_truncate_512"),
            "choice_window_declared": d["provenance"].get("choice_window_declared"),
            "n_sessions": len(rows),
            "replay": replay_session_family(rows, key_of, 4),
            "cap": cap_check(items_of(rows), CAP_SESSIONS),
            "n_entries": sum(len(r["rounds"]) + len(r["choices"]) for r in rows),
            "n_generated": sum(1 for x in items_of(rows) if "n_tok" in x),
            "n_rounds_field": d.get("n_rounds"),
            # round-2 finding 4: which entry is a read with no generated round, and the artifact's declared stop
            "budget": ({k_: d["budget"].get(k_) for k_ in ("stop", "stop_reason", "stop_at", "N", "N_max")}
                       if isinstance(d.get("budget"), dict) else None),
            "reads_without_round": [{"session": int(r["session"]), "read": ci + 1,
                                     "global_read_index": c.get("global_read_index"),
                                     "session_truncated_by_stop": r.get("truncated_by_stop")}
                                    for r in rows for ci, c in enumerate(r["choices"]) if "seed" not in c],
            "banned_string_hits_in_transcripts": banned_hits((r["transcript"] for r in rows), ban["strings"]),
            "adapter_blob_equal_pin": blob(rc, "valence_core/adapters/qwen_mlx.py") == blob(PIN, "valence_core/adapters/qwen_mlx.py"),
            "adapter_generate_equal_pin": gen_src(rc, "valence_core/adapters/qwen_mlx.py") == gen_src(PIN, "valence_core/adapters/qwen_mlx.py"),
            "adapter_sample_line": loc(rc, "valence_core/adapters/qwen_mlx.py", r"mx\.random\.categorical\(lg / temp\)"),
            "adapter_stop_line": loc(rc, "valence_core/adapters/qwen_mlx.py", r"return \(stop_newline and content_seen"),
            "ban_path_line": loc(rc, runner, r"configs/e2a_ban_list\.json"),
            "temp_line": loc(rc, runner, r"^TEMP = 0\.7"),
            "cached_line": loc(rc, runner, r"cached = bool\(|use_cached = bool\(|use_cached = "),
            "rng_line": loc(rc, runner, r"session_rng\("),
            "gen_line": loc(rc, runner, r"max_tokens=STOP_CAP"),
        }
    EV["e2b"] = e2b

    # =============================================================== e2d
    e2d = {}
    tier_seeds = {}
    RES_ = show("RESULTS.md")
    d1_code = re.search(r"Module \+ analyzer committed BEFORE the run at `([0-9a-f]{7})`; D1 ran that code", RES_)
    if not d1_code:
        raise SystemExit("D1 code-commit sentence not found in RESULTS.md")
    D1_CODE = d1_code.group(1)
    E2D_CODE = ["valence_core/e2d/runner.py", "scripts/e2d_sessions.py", "valence_core/e2d/config.py",
                "valence_core/adapters/qwen_mlx.py", "valence_core/session_e2a.py"]
    for tier in ("d1", "d2", "d3"):
        path = f"data/e2d/{tier}_sessions.json"
        d = jload(path)
        rows = d["sessions"]
        dc = commits_of(path)[-1]
        # code of record: D1's is named by the record (checker finding 3); D2's
        # and D3's data commits change no runner file, so the code at the data
        # commit is the code that ran (computed below)
        cc = D1_CODE if tier == "d1" else dc
        e2d[tier] = {
            "data_commit": dc, "code_commit": cc,
            "data_commit_touched_runner_code": touched(dc, E2D_CODE),
            "runner_changed_between_code_and_data_commit": (git("log", "--format=%h", f"{cc}..{dc}", "--", *E2D_CODE).split()
                                                            if cc != dc else []),
            "temp": d.get("temp"), "frac": d.get("frac"),
            "round_path_cached": d.get("round_path_cached", "absent"),
            "round_path_source": d.get("round_path_source", "absent"),
            "draw_seed": d.get("draw_seed", "absent"), "ban_list": d.get("ban_list"),
            "legacy_truncate_512": d["provenance"].get("legacy_truncate_512"),
            "provenance_gdn": d["provenance"].get("gdn_inference_mode"),
            "n_sessions": len(rows),
            "replay": replay_session_family(rows, lambda r: f"e2d-{r['arm']}", 4),
            "cap": cap_check(items_of(rows), CAP_SESSIONS),
            "stop_reason": stop_tally(rows),
            "banned_string_hits_in_texts": banned_hits((x.get("text", "") for x in items_of(rows)), ban["strings"]),
            "round_path_cached_key_counts": count_key(d, "round_path_cached"),
            "runner_lines": {
                "temp": loc(cc, "valence_core/e2d/config.py", r"^TEMP = 0\.7"),
                "rng": loc(cc, "valence_core/e2d/runner.py", r"session_rng\(f\"e2d-"),
                "gen": loc(cc, "valence_core/e2d/runner.py", r"max_tokens=STOP_CAP"),
                "ban": loc(cc, "scripts/e2d_sessions.py", r"build_ban_list\(adapter\)"),
                "path": (loc(cc, "valence_core/e2d/runner.py", r"ban_ids=ban_ids, cached=False\)") if tier == "d1"
                         else loc(cc, "scripts/e2d_sessions.py", r"cached = \{\"gate\"")),
            },
            "d1_data_commit_cached_line": (loc(dc, "valence_core/e2d/runner.py", r"ban_ids=ban_ids, cached=cached\)")
                                           if tier == "d1" else None),
            # the field D1's artifact lacks: written by the runner at the data
            # commit, absent from the runner at the code commit
            "round_path_field_writer_at_data_commit": (loc(dc, "valence_core/e2d/runner.py", r"\"round_path_cached\": bool\(cached\)")
                                                       if tier == "d1" else None),
            "round_path_field_writer_at_code_commit": (find_line(cc, "valence_core/e2d/runner.py", r"round_path_cached")
                                                       if tier == "d1" else None),
            "adapter_blob_equal_pin": blob(cc, "valence_core/adapters/qwen_mlx.py") == blob(PIN, "valence_core/adapters/qwen_mlx.py"),
            "adapter_generate_equal_pin": gen_src(cc, "valence_core/adapters/qwen_mlx.py") == gen_src(PIN, "valence_core/adapters/qwen_mlx.py"),
            "adapter_sample_line": loc(cc, "valence_core/adapters/qwen_mlx.py", r"mx\.random\.categorical\(lg / temp\)"),
            "adapter_stop_line": loc(cc, "valence_core/adapters/qwen_mlx.py", r"return \(stop_newline and content_seen"),
            "stop_cap_line": loc(cc, "valence_core/session_e2a.py", r"^STOP_CAP = 60"),
            "stopcap_field": "STOP_CAP is 60" in ((d.get("tstep_licence") or {}).get("position_coverage_note") or ""),
        }
        for row in rows:
            tier_seeds[(tier, row["arm"], row["session"])] = [x["seed"] for x in items_of([row])]
    def paired(t_ref: str, t_new: str) -> str:
        eq = []
        for (tier, arm, s), seeds in tier_seeds.items():
            if tier == t_new and (t_ref, arm, s) in tier_seeds:
                ref = tier_seeds[(t_ref, arm, s)]
                n = min(len(ref), len(seeds))
                eq.append(ref[:n] == seeds[:n])
        return f"{sum(eq)}/{len(eq)}"
    EV["e2d_shared_seeds"] = {"d1_vs_d2": paired("d1", "d2"), "d1_vs_d3": paired("d1", "d3"),
                              "d2_vs_d3": paired("d2", "d3")}
    EV["e2d"] = e2d

    # =============================================================== k1 + format recon
    fmt = {}
    for path, keyf in (("data/k/k1_sessions.json", lambda r: r["rng_key"]),
                       ("data/format/format_recon_F0_sessions.json", lambda r: f"fmt-{r['format']}"),
                       ("data/format/format_recon_F1_sessions.json", lambda r: f"fmt-{r['format']}"),
                       ("data/format/format_recon_F2_sessions.json", lambda r: f"fmt-{r['format']}")):
        d = jload(path)
        rows = d["sessions"]
        dc = commits_of(path)[-1]
        fmt[path] = {
            "data_commit": dc,
            "data_commit_touched_runner_code": touched(dc, ["valence_core/formats/recon.py", "scripts/k1_stage1.py",
                                                            "scripts/format_recon.py", "valence_core/e2d/config.py",
                                                            "valence_core/adapters/qwen_mlx.py", "valence_core/session_e2a.py"]),
            "artifact": path, "temp_top": d.get("temp"),
            "temp_rows": dict(Counter(json.dumps(r.get("temp")) for r in rows)),
            "identity_temp": (d.get("identity") or {}).get("temp"),
            "draw_seed": d.get("draw_seed"), "ban_list": d.get("ban_list", "absent"),
            "rng_keys": sorted(set(r.get("rng_key", f"fmt-{r['format']}") for r in rows)),
            "legacy_truncate_512": d["provenance"].get("legacy_truncate_512"),
            "n_sessions": len(rows),
            "replay": replay_session_family(rows, keyf, 4),
            "cap": cap_check(items_of(rows), CAP_SESSIONS),
            "stop_reason": stop_tally(rows),
            "round_path_cached_items": dict(Counter(json.dumps(x.get("round_path_cached")) for x in items_of(rows))),
            "round_path_cached_key_counts": count_key(d, "round_path_cached"),
            "banned_string_hits_in_texts": banned_hits((x.get("text", "") for x in items_of(rows)), ban["strings"]),
            "runner_lines": {
                "cached": loc(dc, "valence_core/formats/recon.py", r"^\s+cached = False"),
                "gen": loc(dc, "valence_core/formats/recon.py", r"max_tokens=STOP_CAP"),
                "rng": loc(dc, "valence_core/formats/recon.py", r"rng = session_rng\(rng_key"),
                "temp": loc(dc, "valence_core/e2d/config.py", r"^TEMP = 0\.7"),
            },
            "adapter_blob_equal_pin": blob(dc, "valence_core/adapters/qwen_mlx.py") == blob(PIN, "valence_core/adapters/qwen_mlx.py"),
            "adapter_generate_equal_pin": gen_src(dc, "valence_core/adapters/qwen_mlx.py") == gen_src(PIN, "valence_core/adapters/qwen_mlx.py"),
            "adapter_sample_line": loc(dc, "valence_core/adapters/qwen_mlx.py", r"mx\.random\.categorical\(lg / temp\)"),
            "adapter_stop_line": loc(dc, "valence_core/adapters/qwen_mlx.py", r"return \(stop_newline and content_seen"),
            "stop_cap_line": loc(dc, "valence_core/session_e2a.py", r"^STOP_CAP = 60"),
            "ban_line": (loc(dc, "scripts/k1_stage1.py", r"build_ban_list\(adapter\)") if "k1" in path
                         else loc(dc, "scripts/format_recon.py", r"build_ban_list\(adapter\)")),
        }
    EV["fmt"] = fmt

    # =============================================================== B2 (greedy)
    b2 = {}
    for arm in ("fidelity", "register"):
        for st in ("base", "sft", "dpo", "instruct"):
            path = f"data/olmo/b2_{arm}_{st}.json"
            d = jload(path)
            names = sorted(d["concepts"])
            plan = PLAN(names, len(d["trials"]), 20260823)
            got = [(t["trial"], t["concept"] if t["injected"] else None, bool(t["injected"])) for t in d["trials"]]
            b2[path] = {"n": len(d["trials"]), "alloc_replay_20260823": plan == got,
                        "fields": {k: (k in d) for k in ("temp", "max_tokens", "seed", "ban_list")},
                        "trial_seed_field": "seed" in d["trials"][0],
                        "provenance_seed": d["provenance"].get("seed"),
                        "deterministic": d["provenance"].get("deterministic"),
                        # round-2 finding 7: the negative control for the replay
                        "alloc_replay_plan_trials_default_seed": PLAN(names, len(d["trials"])) == got,
                        # round-2 finding 2 (computed-new): response length in characters
                        "resp_len_chars": [min(len(t["response_raw"]) for t in d["trials"]),
                                           max(len(t["response_raw"]) for t in d["trials"])],
                        "banned_hits_raw": banned_hits((t["response_raw"] for t in d["trials"]),
                                                       ["<think>", "</think>", "<|im_start|>", "<|im_end|>", "<|endoftext|>", "<|pad|>"])}
    b2c = "720a104"
    DRV = commits_of("scripts/run_bphase.sh")[0]   # committed after the run, "as its provenance"
    OLMO_CODE = ["scripts/box_b2_detection.py", "scripts/box_b2r_campaign.py", "scripts/box_b3_sessions.py",
                 "valence_core/adapters/olmo_hf.py", "valence_core/session.py", "valence_core/session_e2a.py"]
    EV["b2"] = {"data_commit_touched_runner_code": touched(b2c, OLMO_CODE),
                "runner_intro": intro("scripts/box_b2_detection.py", "temp=0.0"),
                "driver_commit": DRV, "driver_committed_after_data": subprocess.run(
                    ["git", "merge-base", "--is-ancestor", b2c, DRV], cwd=REPO).returncode == 0,"files": b2, "data_commit": b2c,
                "plan_trials_default_seed": PLAN.__defaults__[0],
                "runner_blob_equal_pin": blob(b2c, "scripts/box_b2_detection.py") == blob(PIN, "scripts/box_b2_detection.py"),
                "adapter_blob_equal_pin": blob(b2c, "valence_core/adapters/olmo_hf.py") == blob(PIN, "valence_core/adapters/olmo_hf.py"),
                "lines": {"gen": loc(b2c, "scripts/box_b2_detection.py", r"seed=args\.seed \+ n, temp=0\.0"),
                          "max": loc(b2c, "scripts/box_b2_detection.py", r"\"--max-tokens\", type=int, default=60"),
                          "seed": loc(b2c, "scripts/box_b2_detection.py", r"\"--seed\", type=int, default=20260823"),
                          "stop": loc(b2c, "scripts/box_b2_detection.py", r"stop_newline=False"),
                          "cached": loc(b2c, "scripts/box_b2_detection.py", r"cached=False\)"),
                          "ban": loc(b2c, "scripts/box_b2_detection.py", r"build_ban_list\(adapter\)"),
                          "driver_no_override": loc(DRV, "scripts/run_bphase.sh", r"box_b2_detection\.py --stage")}}

    LOCKG_T = show("LOCK-g.md")
    EV["b2"]["lock_g"] = {
        "seeded_perm_line": f"LOCK-g.md@{PIN}:{log_line(LOCKG_T, r'^ninth; n = 48 per stage per arm, 24/24 injected/control by seeded')}-{log_line(LOCKG_T, r'^permutation \(seed in run config\)')}",
        "decoding_terms": [i for i, l in enumerate(lines_of(LOCKG_T), 1)
                           if re.search(r"temperature|\btemp\b|max_new_tokens|max[_ -]tokens|top[-_ ]?[pk]\b|nucleus", l, re.I)],
        "greedy_lines": "LOCK-g.md@" + PIN + ":" + ",".join(str(i) for i, l in enumerate(lines_of(LOCKG_T), 1) if "greedy" in l),
    }

    # =============================================================== B2-r
    b2r = {}
    for part in ("control", "explore", "qualify"):
        for st in ("base", "sft", "dpo", "instruct"):
            path = f"data/olmo/b2r_{part}_{st}.json"
            try:
                d = jload(path)
            except RuntimeError:
                continue
            rec = {"temp": d.get("temp"), "max_tokens": d.get("max_tokens"), "seed": d.get("seed"),
                   "provenance_seed": d["provenance"].get("seed"),
                   "deterministic": d["provenance"].get("deterministic")}
            if part == "control":
                rec["n"] = len(d["trials"])
                rec["seed_eq_base_plus_trial"] = sum(1 for t in d["trials"] if t["seed"] == d["seed"] + t["trial"])
            elif part == "explore":
                names = sorted({t["concept"] for t in d["trials"] if t["concept"]})
                plan = PLAN(names, len(d["trials"]), d["seed"])
                got = [(t["trial"], t["concept"] if t["injected"] else None, bool(t["injected"])) for t in d["trials"]]
                rec["n"] = len(d["trials"])
                rec["alloc_replay"] = plan == got
                rec["seed_eq_base_plus_trial"] = sum(1 for t in d["trials"] if t["seed"] == d["seed"] + t["trial"])
                ctl = jload(f"data/olmo/b2r_control_{st}.json")
                cs = {t["trial"]: t["seed"] for t in ctl["trials"]}
                rec["explore_seeds_equal_control_seeds"] = sum(1 for t in d["trials"] if cs.get(t["trial"]) == t["seed"])
            else:
                base = d["seed"]
                crow = d["control"]["rows"]
                ok_c = sum(1 for r in crow if 0 <= r["seed"] - (base + 9000 + r["prompt"] * 100) < 12)
                n_i = ok_i = 0
                shared = Counter()
                for strength, blk in d["injected"].items():
                    for r in blk["rows"]:
                        n_i += 1
                        off = r["seed"] - (base + int(float(strength) * 1000) + r["prompt"] * 100)
                        ok_i += int(0 <= off < 3)
                        shared[(strength, r["seed"])] += 1
                rec.update({"n_control_rows": len(crow), "control_seed_formula_ok": ok_c,
                            "n_injected_rows": n_i, "injected_seed_formula_ok": ok_i,
                            "max_rows_sharing_one_seed_within_strength": max(shared.values()) if shared else 0,
                            "n_concepts": len({r['concept'] for b in d['injected'].values() for r in b['rows']})})
            if part in ("control", "explore"):
                # round-2 finding 2 (computed-new): response length in characters
                rec["resp_len_chars"] = [min(len(t["response_raw"]) for t in d["trials"]),
                                         max(len(t["response_raw"]) for t in d["trials"])]
            rec["banned_hits_raw"] = banned_hits((t.get("response_raw", "") for t in d.get("trials", [])),
                                                 ["<think>", "</think>", "<|im_start|>", "<|im_end|>", "<|endoftext|>", "<|pad|>"])
            rec["banned_hit_trials"] = [
                {"trial": t["trial"], "string": sstr, "audit": t.get("audit"), "claimed_detection": t.get("claimed_detection")}
                for t in d.get("trials", []) for sstr in ["<think>", "</think>", "<|im_start|>", "<|im_end|>", "<|endoftext|>", "<|pad|>"]
                if sstr in t.get("response_raw", "")]
            b2r[path] = rec
    b2rc = "b6e8f3f"
    arc = show("results/raw/2026-08-25_b2r_arc.txt")
    stamped = re.search(r"repo head : ([0-9a-f]{7})", arc)
    stamped = stamped.group(1) if stamped else None
    ADD = "ADDENDUM-g3-b2r-v1.2.md"
    ADD_T = show(ADD)
    add_commit = commits_of(ADD)[0]
    EV["b2r"] = {"data_commit_touched_runner_code": touched(b2rc, OLMO_CODE),
                 "addendum": ADD, "addendum_commit": add_commit, "addendum_commit_date": cdate(add_commit),
                 "addendum_decoding_lines": f"{ADD}@{PIN}:{log_line(ADD_T, r'0\.5 Decoding of record, all parts')}-{log_line(ADD_T, r'this addendum names all of them')}",
                 "addendum_names_all_line": f"{ADD}@{PIN}:{log_line(ADD_T, r'Decoding parameters are measurement')}-{log_line(ADD_T, r'this addendum names all of them')}",
                 "addendum_b2_greedy_line": f"{ADD}@{PIN}:{log_line(ADD_T, r'ours ran 0\.0')}",
                 "addendum_mentions_top_p_or_k": bool(re.search(r"top[-_ ]?[pk]\b|nucleus", ADD_T, re.I)),
                 "addendum_before_runner_intro": subprocess.run(["git", "merge-base", "--is-ancestor", add_commit,
                                                                 intro("scripts/box_b2r_campaign.py", "TEMP = 1.0")], cwd=REPO).returncode == 0,
                 "files": b2r, "data_commit": b2rc, "stamped_head": stamped,
                 "stamped_head_line": f"results/raw/2026-08-25_b2r_arc.txt@{PIN}:{log_line(arc, r'repo head :')}",
                 "runner_blob_equal_pin": blob(b2rc, "scripts/box_b2r_campaign.py") == blob(PIN, "scripts/box_b2r_campaign.py"),
                 "runner_blob_stamped_equal_pin": (blob(stamped, "scripts/box_b2r_campaign.py") == blob(PIN, "scripts/box_b2r_campaign.py")) if stamped else None,
                 "adapter_blob_equal_pin": blob(b2rc, "valence_core/adapters/olmo_hf.py") == blob(PIN, "valence_core/adapters/olmo_hf.py"),
                 "lines": {"temp": loc(b2rc, "scripts/box_b2r_campaign.py", r"^TEMP = 1\.0"),
                           "max": loc(b2rc, "scripts/box_b2r_campaign.py", r"^MAX_TOKENS = 100"),
                           "seed": loc(b2rc, "scripts/box_b2r_campaign.py", r"\"--seed\", type=int, default=20260824"),
                           "qual_seed": loc(b2rc, "scripts/box_b2r_campaign.py", r"seed=args\.seed \+ 9000"),
                           "stop": loc(b2rc, "scripts/box_b2r_campaign.py", r"stop_newline=False"),
                           "cached": loc(b2rc, "scripts/box_b2r_campaign.py", r"cached=False\)"),
                           "ban": loc(b2rc, "scripts/box_b2r_campaign.py", r"build_ban_list\(adapter\)"),
                           "audit_ban": loc(b2rc, "scripts/box_b2r_campaign.py", r"ban_strings=\(\"<think>\"")}}

    # =============================================================== B3
    b3 = {}
    stage_seeds = {}
    for st in ("base", "sft", "dpo", "instruct"):
        path = f"data/olmo/b3_screen_{st}.json"
        d = jload(path)
        rows = d["sessions"]
        b3[path] = {"temp_field": "temp" in d, "ban_list": d.get("ban_list"),
                    "provenance_seed": d["provenance"].get("seed"),
                    "deterministic": d["provenance"].get("deterministic"),
                    "n_sessions": len(rows),
                    "replay": replay_session_family(rows, lambda r: f"b3-{r['arm']}", 4),
                    "cap": cap_check(items_of(rows), CAP_SESSIONS),
                    "path_field": any("cach" in k for k in d),
                    "banned_hits": banned_hits((r["transcript"] for r in rows),
                                               ["<think>", "</think>", "<|im_start|>", "<|im_end|>", "<|endoftext|>", "<|pad|>"])}
        for row in rows:
            stage_seeds[(st, row["arm"], row["session"])] = [x["seed"] for x in items_of([row])]
    cross = []
    for (st, arm, s), seeds in stage_seeds.items():
        if st == "base":
            continue
        ref = stage_seeds.get(("base", arm, s))
        if ref is not None:
            n = min(len(ref), len(seeds))
            cross.append(ref[:n] == seeds[:n])
    # every pair of stages, not only against base (checker finding 8)
    STG = ("base", "sft", "dpo", "instruct")
    cross_all = []
    for i, s1_ in enumerate(STG):
        for s2_ in STG[i + 1:]:
            for (st, arm, s), seeds in stage_seeds.items():
                if st != s1_ or (s2_, arm, s) not in stage_seeds:
                    continue
                other = stage_seeds[(s2_, arm, s)]
                n = min(len(other), len(seeds))
                cross_all.append(other[:n] == seeds[:n])
    keys_all4 = sum(1 for (st, arm, s) in stage_seeds if st == "base"
                    and all((o, arm, s) in stage_seeds for o in STG[1:]))
    a2 = {st: jload(f"data/olmo/a2_baserates_{st}.json")["ban_list"] for st in STG}
    scaf = {st: {k: v for k, v in jload(f"data/olmo/scaffold_{st}.json").items() if k.startswith("ban")} for st in STG}
    # The OLMo banned id set (checker finding 10). The artifacts store counts,
    # strings and two sha16s, not ids; the record's m-v1.10 referent check
    # lists the ids it read from the base tokenizer. Both stored sha16s are
    # recomputed here from that one id list, each under its own convention.
    REF = "results/raw/2026-10-05_m-v1.10_referent_check.txt"
    REF_T = show(REF)
    ln_pieces = log_line(REF_T, r"524, 'think' 27963, '>' 29, '<th' 14023, 'ink' 771; the specials are")
    ln_five = log_line(REF_T, r"five of the nine banned ids are ordinary sub-word tokens")
    ln_check = log_line(REF_T, r"Six strings, nine ids, five sub-word ids and the sha16 all reproduce")
    ref_lines = lines_of(REF_T)
    blob_txt = " ".join(ref_lines[ln_pieces - 2:ln_pieces + 1])
    sub = {m.group(1): int(m.group(2)) for m in re.finditer(r"'([^']+)'\s+(\d+)", blob_txt)}
    spec = [int(x) for x in re.search(r"the specials are\s+(\d+)/(\d+)/(\d+)/(\d+)", blob_txt).groups()]
    olmo_ids = sorted(set(sub.values()) | set(spec))
    olmo_strings = sorted(next(iter(a2.values()))["strings"])
    sha_b3_conv = sha256_bytes(json.dumps(sorted(olmo_ids)).encode())[:16]
    sha_a2_conv = sha256_bytes(json.dumps({"ids": olmo_ids, "strings": olmo_strings}, sort_keys=True).encode())[:16]
    olmo_ban = {
        "record_ids_locator": f"{REF}@{PIN}:{ln_pieces - 1}-{ln_pieces + 1}",
        "record_five_locator": f"{REF}@{PIN}:{ln_five}",
        "record_check_locator": f"{REF}@{PIN}:{ln_check}",
        "subword_pieces_from_record": sub, "special_ids_from_record": spec, "ids": olmo_ids,
        "sha16_sorted_ids_convention": sha_b3_conv,
        "b3_sha16_fields": sorted({v["ban_list"]["sha16"] for v in b3.values()}),
        "b3_convention_matches_all_stages": all(v["ban_list"]["sha16"] == sha_b3_conv for v in b3.values()),
        "sha16_ids_strings_convention": sha_a2_conv,
        "a2_sha16_fields": sorted({v["sha16"] for v in a2.values()}),
        "a2_convention_matches_all_stages": all(v["sha16"] == sha_a2_conv for v in a2.values()),
        "b3_sha_line": loc("720a104", "scripts/box_b3_sessions.py", r"ban_sha = hashlib\.sha256\(json\.dumps\(sorted\(ban_ids\)\)"),
        "a2_data_commit": commits_of("data/olmo/a2_baserates_base.json")[-1],
        "scaffold_fields": scaf,
        "scaffold_commit": commits_of("data/olmo/scaffold_base.json")[-1],
        "builder_lines": f"valence_core/session.py@{PIN}:{find_line(PIN, 'valence_core/session.py', r'strings \|= set\(adapter\.special_token_strings\)')[0]}-{find_line(PIN, 'valence_core/session.py', r'ids\.add\(int\(tok\)\)')[0]}",
        "builder_source_equal": {c: fn_src(c, "valence_core/session.py", "build_ban_list") == fn_src(PIN, "valence_core/session.py", "build_ban_list")
                                 for c in ("720a104", "b6e8f3f")},
    }
    _a2c = olmo_ban["a2_data_commit"]
    _l = find_line(_a2c, "scripts/box_a2_baserates.py", r"ban_sha = hashlib\.sha256\(\s*$")[0]
    olmo_ban["a2_sha_line"] = f"scripts/box_a2_baserates.py@{_a2c}:{_l}-{_l + 1}"
    # local base tokenizer (OUTSIDE the record; JSON reads only; compared by
    # hash with the run's pinned file in data/olmo/manifest.json)
    olmo_local = {}
    try:
        od = os.path.expanduser("~/.cache/huggingface/hub/models--allenai--Olmo-3-1125-32B/snapshots")
        snaps_o = sorted(os.listdir(od))
        if len(snaps_o) == 1:
            sdir = os.path.join(od, snaps_o[0])
            tjb = open(os.path.join(sdir, "tokenizer.json"), "rb").read()
            tcb = open(os.path.join(sdir, "tokenizer_config.json"), "rb").read()
            tj_o = json.loads(tjb)
            tc_o = json.loads(tcb)
            inv = {v: k for k, v in tj_o["model"]["vocab"].items()}
            inv.update({a["id"]: a["content"] for a in tj_o["added_tokens"]})
            man = jload("data/olmo/manifest.json")
            eos_o = tc_o.get("eos_token")
            eos_o = eos_o["content"] if isinstance(eos_o, dict) else eos_o
            added_o = {a["content"]: a["id"] for a in tj_o["added_tokens"]}
            olmo_local = {
                "snapshot": snaps_o[0][:8] + "...",
                "id_to_piece": {i: inv.get(i) for i in olmo_ids},
                "pieces_agree_with_record": all(inv.get(i) == p for p, i in sub.items()),
                "think_strings_are_added_tokens": {s: (s in added_o) for s in ("<think>", "</think>")},
                "eos_token": eos_o, "eos_id": added_o.get(eos_o), "eos_id_in_ids": added_o.get(eos_o) in olmo_ids,
                "tokenizer_json_sha256_equals_manifest_base": sha256_bytes(tjb) == man["base"]["files"]["tokenizer.json"]["sha256"],
                "tokenizer_config_sha256_equals_manifest_base": sha256_bytes(tcb) == man["base"]["files"]["tokenizer_config.json"]["sha256"],
            }
    except (OSError, KeyError, ValueError, StopIteration) as exc:   # pragma: no cover
        olmo_local = {"error": str(exc)}
    olmo_ban["local_base_tokenizer_outside_record"] = olmo_local
    b3c = "720a104"
    EV["b3"] = {"files": b3, "data_commit": b3c,
                "data_commit_touched_runner_code": touched(b3c, OLMO_CODE),
                "same_arm_session_seeds_equal_across_stages": f"{sum(cross)}/{len(cross)}",
                "same_arm_session_seeds_equal_all_stage_pairs": f"{sum(cross_all)}/{len(cross_all)}",
                "keys_present_at_all_four_stages": keys_all4,
                "a2_ban_lists": a2, "olmo_ban": olmo_ban,
                "runner_blob_equal_pin": blob(b3c, "scripts/box_b3_sessions.py") == blob(PIN, "scripts/box_b3_sessions.py"),
                "lines": {"temp": loc(b3c, "scripts/box_b3_sessions.py", r"^TEMP = 0\.7"),
                          "temp_cli": loc(b3c, "scripts/box_b3_sessions.py", r"\"--temp\", type=float, default=TEMP"),
                          "rng": loc(b3c, "scripts/box_b3_sessions.py", r"session_rng\(f\"b3-"),
                          "gen": loc(b3c, "scripts/box_b3_sessions.py", r"temp=temp, max_tokens=STOP_CAP"),
                          "cached_default": loc(b3c, "scripts/box_b3_sessions.py", r"term_rx, cached=False\)"),
                          "call_no_cached": loc(b3c, "scripts/box_b3_sessions.py", r"inj_by_arm\[arm\], ban_ids, args\.temp, term_rx\)"),
                          "ban": loc(b3c, "scripts/box_b3_sessions.py", r"build_ban_list\(adapter\)"),
                          "driver_no_override": loc(DRV, "scripts/run_bphase.sh", r"box_b3_sessions\.py --stage"),
                          "driver_cached_forbidden": loc(DRV, "scripts/run_bphase.sh", r"cached path is\s*$|FORBIDDEN")}}

    PREREG_TEMP = {}
    for f_ in sorted(git("ls-tree", "--name-only", PIN).split()):
        if re.match(r"^(PROPOSAL|LOCK|ADDENDUM)-.*\.md$", f_):
            PREREG_TEMP[f_] = sum(1 for l in lines_of(show(f_))
                                  if re.search(r"temperature|\btemp[ =]+[0-9]|TEMP [0-9]", l, re.I))
    J["prereg_docs_temperature_mentions"] = PREREG_TEMP

    # g2 corpus temperature: search the e2a-era record for a 0.7 temperature (checker finding 4)
    G2_KEYS = sorted(jload("data/e2a/g2_discriminability.json").keys())
    G2_ROW_KEYS = sorted(jload("data/e2a/g2_rounds_f0.1.json")["pos"][0].keys())
    _files = ["archive/RESULTS-cycles3-4.md"] + sorted(f_ for f_ in git("ls-tree", "--name-only", PIN, "results/raw/").split()
                                                      if re.match(r"results/raw/2026-08-(0\d|1[0-2])_e2a", f_))
    _rx = re.compile(r"(temp|temperature)[^a-z0-9]{0,6}0\.7|0\.7[^0-9].{0,12}\btemp", re.I)
    _hits = []
    for f_ in _files:
        for i_, l_ in enumerate(lines_of(show(f_)), 1):
            if _rx.search(l_):
                _hits.append(f"{f_}@{PIN}:{i_}")
    G2_TEMP_SEARCH = {"files": _files, "regex": _rx.pattern, "hits": len(_hits), "hit_lines": _hits}
    J["g2_temperature_search"] = G2_TEMP_SEARCH

    # ------------------------------------------------- adapter code at PIN (+ intro)
    AD = {
        "qwen_sample": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"mx\.random\.categorical\(lg / temp\)"),
        "qwen_argmax": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"if temp <= 0\.0:"),
        "qwen_seed": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"mx\.random\.seed\(seed\)"),
        "qwen_ban": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"v\[ban_ids\] = -1e30"),
        "qwen_stop": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"return \(stop_newline and content_seen"),
        "qwen_eos": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"if eos is not None and tok == eos"),
        "qwen_cached": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"^\s+if cached:"),
        "qwen_strip": loc(PIN, "valence_core/adapters/qwen_mlx.py", r"text=self\.decode\(generated\)\.strip\(\)"),
        "olmo_pick": loc(PIN, "valence_core/adapters/olmo_hf.py", r"t\.multinomial\(probs, 1\)"),
        "olmo_argmax": loc(PIN, "valence_core/adapters/olmo_hf.py", r"if temp <= 0\.0:"),
        "olmo_seed": loc(PIN, "valence_core/adapters/olmo_hf.py", r"t\.manual_seed\(seed\)"),
        "olmo_load_seed": loc(PIN, "valence_core/adapters/olmo_hf.py", r"torch\.manual_seed\(seed\)"),
        "olmo_ban": loc(PIN, "valence_core/adapters/olmo_hf.py", r"lg\[ban_ids\] = -1e30"),
        "olmo_stop": loc(PIN, "valence_core/adapters/olmo_hf.py", r"return \(stop_newline and content_seen"),
        # checker finding 9: the default lives in the signature; the rule is _is_stop
        "olmo_stop_default": loc(PIN, "valence_core/adapters/olmo_hf.py", r"max_tokens: int = 60, stop_newline: bool = True"),
        "olmo_stop_rule": (f"valence_core/adapters/olmo_hf.py@{PIN}:"
                           f"{find_line(PIN, 'valence_core/adapters/olmo_hf.py', r'def _is_stop')[0]}-"
                           f"{find_line(PIN, 'valence_core/adapters/olmo_hf.py', r'in self\.decode\(\[tok\]\)\)$')[0]}"),
        "olmo_special": loc(PIN, "valence_core/adapters/olmo_hf.py", r"all_special_tokens"),
        "ban_builder": loc(PIN, "valence_core/session.py", r"^DEFAULT_SCAFFOLD_STRINGS = "),
        "ban_builder_special": loc(PIN, "valence_core/session.py", r"strings \|= set\(adapter\.special_token_strings\)"),
        "stop_cap": loc(PIN, "valence_core/session_e2a.py", r"^STOP_CAP = 60"),
        "readout_no_ban": loc(PIN, "valence_core/readout.py", r"^def choice_read\("),
        "e2d_temp_comment": loc(PIN, "valence_core/e2d/config.py", r"^TEMP = 0\.7\s+# e2a's TEMP"),
    }
    PREREG_KEY = "log: e2a pre-registration, 'ROUND generation is temperature-sampled'"
    AMEND_KEY = "log: e2a template amendment, '(a) Stop discipline' / 'backstop cap 60 tokens'"
    BAN_KEY = "log: smoke2 adjudication (config v3), scaffold logit ban 'ROUND GENERATION ONLY'"
    PJ_KEY = "PROPOSAL-j 'Held fixed, by design' (template family v3, e2d)"
    REFINE_KEY = "log: g2r incident, refinement of amendment (a), 'consumed before the newline stop arms'"
    INTRO = {
        "session_e2a STOP_CAP = 60": intro("valence_core/session_e2a.py", "STOP_CAP = 60", follow=True),
        "e2d/config TEMP = 0.7": intro("valence_core/e2d/config.py", "TEMP = 0.7"),
        "e2b_h1 TEMP = 0.7": intro("scripts/e2b_h1_sessions.py", "TEMP = 0.7"),
        "e2b_h2 TEMP = 0.7": intro("scripts/e2b_h2_sessions.py", "TEMP = 0.7"),
        "e2b_verdict TEMP = 0.7": intro("scripts/e2b_verdict_campaign.py", "TEMP = 0.7"),
        "box_b3 TEMP = 0.7": intro("scripts/box_b3_sessions.py", "TEMP = 0.7"),
        "box_b2r TEMP = 1.0": intro("scripts/box_b2r_campaign.py", "TEMP = 1.0"),
        "box_b2r MAX_TOKENS = 100": intro("scripts/box_b2r_campaign.py", "MAX_TOKENS = 100"),
        "box_b2r --seed 20260824": intro("scripts/box_b2r_campaign.py", "default=20260824"),
        "box_b2 temp=0.0": intro("scripts/box_b2_detection.py", "temp=0.0"),
        "box_b2 --max-tokens 60": intro("scripts/box_b2_detection.py", '"--max-tokens", type=int, default=60'),
        "box_b2 --seed 20260823": intro("scripts/box_b2_detection.py", "default=20260823"),
        "qwen_mlx categorical(lg / temp)": intro("valence_core/adapters/qwen_mlx.py", "mx.random.categorical(lg / temp)", follow=True),
        "olmo_hf multinomial": intro("valence_core/adapters/olmo_hf.py", "t.multinomial(probs, 1)"),
        "session.py DEFAULT_SCAFFOLD_STRINGS": intro("valence_core/session.py", "DEFAULT_SCAFFOLD_STRINGS = ", follow=True),
        "formats/recon cached = False": intro("valence_core/formats/recon.py", "cached = False"),
        "e2d_sessions --round-path": intro("scripts/e2d_sessions.py", '"--round-path"'),
        "e2a_ban_list.json added": ban_commit,
        # the log entries that fixed the clone-run parameters (checker finding 1)
        PREREG_KEY: intro_paths(["RESULTS.md", "archive/RESULTS-cycles3-4.md"], "ROUND generation is temperature-sampled"),
        AMEND_KEY: intro_paths(["RESULTS.md", "archive/RESULTS-cycles3-4.md"], "backstop cap 60 tokens"),
        BAN_KEY: intro_paths(["RESULTS.md", "archive/RESULTS-cycles3-4.md"], "ROUND GENERATION ONLY"),
        "log: g2 spot-check, 'ban list frozen, 12 ids'": intro_paths(["RESULTS.md", "archive/RESULTS-cycles3-4.md"], "ban list frozen, 12 ids, sha"),
        "PROPOSAL-f 'v3 template family (newline stop'": intro("PROPOSAL-f-natural-reinforcer-screen.md", "v3 template family (newline stop"),
        # B2-r's pre-registered decoding (checker finding 2)
        "ADDENDUM-g3-b2r-v1.2 '0.5 Decoding of record'": intro("ADDENDUM-g3-b2r-v1.2.md", "0.5 Decoding of record"),
        # round 2: e2d's pre-registration by reference (finding 3); the stop rule's 'after content' refinement (finding 6)
        PJ_KEY: intro("PROPOSAL-j-dose-escalation.md", "Held fixed, by design"),
        REFINE_KEY: intro_paths(["RESULTS.md", "archive/RESULTS-cycles3-4.md"], "consumed before the newline stop arms"),
    }
    INTRO = {k: (v, cdate(v)) for k, v in INTRO.items()}
    # checker finding 12: the STOP_CAP row needs --follow; record both forms
    STOPCAP_FOLLOW = intro_follow_detail("valence_core/session_e2a.py", "STOP_CAP = 60")
    J["stop_cap_intro_follow_detail"] = STOPCAP_FOLLOW
    J["adapter_locators"] = AD
    J["introducing_commits"] = INTRO

    # ------------------------------------------------- log locators (pinned)
    LOG = {
        "e2a_prereg_sampled_cached": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'ROUND generation is temperature-sampled')}",
        "e2a_prereg_choice_greedy": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'fail → uncached path, rescale N\)\*\*\. CHOICE forwards: greedy')}",
        "e2a_amend_stop": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'\(a\) Stop discipline:')}",
        "e2a_amend_cap": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'backstop cap 60 tokens')}",
        "e2a_v1_cap90": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'round hit the 90-token cap with no EOS')}",
        "e2a_full_cached": f"results/raw/2026-08-09_e2a_full.txt@{PIN}:{log_line(show('results/raw/2026-08-09_e2a_full.txt'), r'round generation path \(g1r, mechanical\): cached')}",
        "e2a_full_ban": f"results/raw/2026-08-09_e2a_full.txt@{PIN}:{log_line(show('results/raw/2026-08-09_e2a_full.txt'), r'ban list 12 ids sha 9a2f0744f81ac930')}",
        "g2r2_cached": f"results/raw/2026-08-09_e2a_g2r2.txt@{PIN}:{log_line(show('results/raw/2026-08-09_e2a_g2r2.txt'), r'cached=True')}",
        "g2r2_ban": f"results/raw/2026-08-09_e2a_g2r2.txt@{PIN}:{log_line(show('results/raw/2026-08-09_e2a_g2r2.txt'), r'ban 12 ids sha 9a2f0744f81ac930')}",
        "f_cached_proposal": f"PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{log_line(PROPF, r'No steering anywhere ⇒ cached sampling')}",
        "f_stop_ban_proposal": f"PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{log_line(PROPF, r'v3 template family \(newline stop')}",
        "f_ndecl_cached": f"results/raw/2026-08-10_f_ndecl.txt@{PIN}:{log_line(show('results/raw/2026-08-10_f_ndecl.txt'), r'cached vanilla path')}",
        "gport_f1_temp_cap": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'^Verified identical, no difference: sampling, TEMP 0\.7, STOP_CAP 60')}",
        "gport_f1_sampling": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'Sampling is identical: float32 logits plus a -1e30 ban vector')}",
        "gport_f1_stop": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'^- The stop rule is identical: stop on EOS')}",
        "gport_eos_banned": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'including the EOS <\|im_end\|>, is banned in both runners')}",
        "gport_eos_tokcfg": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'the tokenizer config gives eos_token <\|im_end\|>')}",
        "gport_ban_correction": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'bans only 10 of them')}",
        "gport_f1_512": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'^\*\*f1:\*\* every generation keeps the 512-token tail')}",
        "gport_ban_read": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'^\(3\) The ban never reaches a read on either side')}",
        "gport_f1_ban": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'^- Ban ids: both use the same frozen file data/configs/e2a_ban_list\.json')}",
        "gport_gdn": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'^- GDN kernel: the ops kernel on the cached path in both')}",
        "gport_f1_seedtiming": f"results/raw/2026-10-07_m-gport_differences.md@{PIN}:{log_line(GPORT, r'MLX seed timing: f1 calls mx\.random\.seed after the prefill')}",
        "e2a_512_claude": f"CLAUDE.md@{PIN}:{log_line(CLAUDE, r'270 of e2a')}",
        "d1_uncached": f"RESULTS.md@{PIN}:{log_line(RES, r'FLAG 1 — ROUND PATH\. D1 ran UNCACHED')}",
        "b_phase_uncached": f"RESULTS.md@{PIN}:{log_line(RES, r'FORBIDDEN for all of Phase B, generation is uncached at every stage')}",
        "b2_temp0": f"RESULTS.md@{PIN}:{log_line(RES, r'Ours: `box_b2_detection\.py:198` hardcodes')}",
        "b2_seed_inert": f"RESULTS.md@{PIN}:{log_line(RES, r'and note the per-trial `seed=args\.seed \+ n` is INERT')}",
        "b2_max60": f"RESULTS.md@{PIN}:{log_line(RES, r'`max_new_tokens` 100 theirs vs 60 ours')}",
        "b3_temp07": f"RESULTS.md@{PIN}:{log_line(RES, r'session rounds from the e2a corpus at \*\*temp 0\.7\*\* \(B3')}",
        "k1_temp": f"RESULTS.md@{PIN}:{log_line(RES, r'`k1-F2`; temp 0\.7; scope e2a')}",
        "qwen_snapshot": f"RESULTS.md@{PIN}:{log_line(RES, r'config\.json of the single local snapshot')}",
        # added by the fixer pass (checker findings 1, 2, 3, 11)
        "e2a_ban_adjudication": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'logit ban of enumerated chat-scaffold')}-{log_line(RC34, r'construction preserved\). \(2a\) per-round degeneracy audit')}",
        "e2a_ban_frozen": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'ban list frozen, 12 ids, sha')}-{log_line(RC34, r'^\s+`9a2f0744f81ac930`; roster collision assertion passed')}",
        "e2a_full_stale_banner": f"results/raw/2026-08-09_e2a_full.txt@{PIN}:{log_line(show('results/raw/2026-08-09_e2a_full.txt'), r'uncached path \(g1\)')}",
        "e2a_stale_banner_cosmetic": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'Cosmetic on record: the session banner still prints the stale')}-{log_line(RC34, r'cached-path line; fix queued for the next licensed launch')}",
        "f_stop_ban_proposal_range": f"PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{log_line(PROPF, r'v3 template family \(newline stop')}-{log_line(PROPF, r'^scaffold-token ban, frozen audit list')}",
        "d1_code_commit": f"RESULTS.md@{PIN}:{log_line(RES, r'Module \+ analyzer committed BEFORE the run at `4e41288`; D1 ran that code')}",
        # round 2 (findings 3 and 6)
        "e2d_prereg_held_fixed": f"PROPOSAL-j-dose-escalation.md@{PIN}:{log_line(PROPJ, r'^\*\*Held fixed, by design:\*\*')}-{log_line(PROPJ, r'unchanged family, no recalibration; the dose is the only change')}",
        "e2a_stop_refinement": f"archive/RESULTS-cycles3-4.md@{PIN}:{log_line(RC34, r'degenerate text channel\)\. Implementation refinement of amendment')}-{log_line(RC34, r'consumed before the newline stop arms; response text stripped')}",
    }
    J["log_locators"] = LOG

    # ------------------------------------------------- round-2 evidence
    def is_anc(a: str, b: str) -> bool:
        return subprocess.run(["git", "merge-base", "--is-ancestor", a, b], cwd=REPO).returncode == 0
    # finding 3: PROPOSAL-j holds the v3 family fixed for e2d, before the code and the data
    PJ_C = INTRO[PJ_KEY][0]
    PJ = {"commit": PJ_C, "date": INTRO[PJ_KEY][1], "first_commit_of_file": commits_of("PROPOSAL-j-dose-escalation.md")[0],
          "lines": LOG["e2d_prereg_held_fixed"],
          "ancestor_of": {c: is_anc(PJ_C, c) for c in
                          sorted({x["code_commit"] for x in e2d.values()} | {x["data_commit"] for x in e2d.values()})},
          "temperature_mentions": PREREG_TEMP.get("PROPOSAL-j-dose-escalation.md")}
    PJ["precedes_every_e2d_code_and_data_commit"] = all(PJ["ancestor_of"].values())
    J["e2d_preregistration"] = PJ
    PJ_CITE = f"pre-reg PROPOSAL-j {PJ_C} (v3 family held fixed, {PJ['lines']})"
    # finding 6: the stop rule's 'after content' half
    REFINE = {"lines": LOG["e2a_stop_refinement"], "commit": INTRO[REFINE_KEY][0], "date": INTRO[REFINE_KEY][1]}
    J["stop_refinement"] = REFINE
    # finding 8: e2a's draw order, as the record's module states and codes it
    SE_T = lines_of(show("valence_core/session_e2a.py"))
    _d0 = find_line(PIN, "valence_core/session_e2a.py", r"1\. `rng\.permutation\(16\)`")[0]
    _d1 = find_line(PIN, "valence_core/session_e2a.py", r"4\. per free choice:")[0]
    _d1 = next(i for i in range(_d1, len(SE_T) + 1) if "generation seed" in SE_T[i - 1])
    _s0 = find_line(PIN, "valence_core/session_e2a.py", r"idx = rng\.permutation\(len\(tasks\)\)\[:n_rounds\]")[0]
    _s1 = find_line(PIN, "valence_core/session_e2a.py", r"\[int\(rng\.integers\(4\)\)\]")[0]
    _nr = find_line(PIN, "valence_core/session_e2a.py", r"n_rounds = 2 \* F \+ N_FREE")[0]
    _ilv = find_line(PIN, "valence_core/session_e2a.py", r"interleaves with the seed draws, collapses the reconstruction to 4/200")[0]
    E2A_F = sorted({int(r["F"]) for r in e2a_rows})
    DRAW = {"order_lines": f"valence_core/session_e2a.py@{PIN}:{_d0}-{_d1}",
            "sequence_lines": f"valence_core/session_e2a.py@{PIN}:{_s0}-{_s1}",
            "n_rounds_line": f"valence_core/session_e2a.py@{PIN}:{_nr}",
            "interleave_warning_line": f"valence_core/session_e2a.py@{PIN}:{_ilv}",
            "F_values": E2A_F, "N_FREE": SE["N_FREE"],
            "n_planned": sorted({2 * f_ + SE["N_FREE"] for f_ in E2A_F})}
    J["e2a_draw_order"] = DRAW
    _np = DRAW["n_planned"][0] if len(DRAW["n_planned"]) == 1 else DRAW["n_planned"]
    _F = E2A_F[0] if len(E2A_F) == 1 else E2A_F

    # =============================================================== cross-checks
    xc = {"n2": {}, "n4": {}}
    n2_text = read_bytes_text(os.path.join(REPO, N2_RAW)) if os.path.exists(os.path.join(REPO, N2_RAW)) else ""
    n4_text = read_bytes_text(os.path.join(REPO, N4_RAW)) if os.path.exists(os.path.join(REPO, N4_RAW)) else ""
    n4_json = json.load(open(os.path.join(REPO, N4_JSON))) if os.path.exists(os.path.join(REPO, N4_JSON)) else {}
    xc["n2"]["sha256_at_read"] = sha256_bytes(n2_text.encode()) if n2_text else None
    xc["n4"]["sha256_at_read"] = sha256_bytes(n4_text.encode()) if n4_text else None
    xc["n4"]["json_sha256_at_read"] = sha256_bytes(open(os.path.join(REPO, N4_JSON), "rb").read()) if n4_json else None
    # round-2 finding 4: N4's own counting formula (working tree, untracked; located by pattern at read)
    _n4s = os.path.join(REPO, N4_SCRIPT)
    if os.path.exists(_n4s):
        _n4t = read_bytes_text(_n4s)
        _hit = next((i for i, l in enumerate(lines_of(_n4t), 1)
                     if re.search(r'ngen = sum\(len\(x\["rounds"\]\) \+ len\(x\["choices"\]\)', l)), None)
        xc["n4"]["script"] = {"path": N4_SCRIPT, "sha256_at_read": sha256_bytes(_n4t.encode()),
                              "ngen_formula_line": _hit,
                              "ngen_formula": lines_of(_n4t)[_hit - 1].strip() if _hit else None}
    else:
        xc["n4"]["script"] = None

    def n2_row(param: str) -> str:
        for line in lines_of(n2_text):
            if line.startswith(f"| {param} |"):
                return line
        return ""
    n2_checks = []
    for param, b2r_want, b2_want in (
            ("temperature", "**1.0**", "**0.0**"),
            ("top-p", "none", "n/a (argmax"),
            ("top-k", "none", "n/a (argmax)"),
            ("max new tokens", "**100**", "**60**"),
            ("seed policy", "20260824 + trial n", "20260823 + n"),
            ("stop rule", "EOS token or the cap", "EOS or the 60 cap"),
            ("banned tokens", "special-token strings", "same"),
            ("generation path", "uncached", "uncached")):
        row = n2_row(param)
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", row)[1:-1]] if row else []
        b2r_cell = cells[1] if len(cells) > 1 else ""
        b2_cell = cells[2] if len(cells) > 2 else ""
        n2_checks.append({"param": param, "n2_b2r_cell_has": b2r_want in b2r_cell,
                          "n2_b2_cell_has": b2_want in b2_cell,
                          "n2_b2r_status": (re.findall(r"\[([a-z -]+?)(?::[^\]]*)?\]", b2r_cell) or ["(descriptive)"])[-1],
                          "n2_b2_status": (re.findall(r"\[([a-z -]+?)(?::[^\]]*)?\]", b2_cell) or ["(descriptive)"])[-1]})
    xc["n2"]["rows"] = n2_checks
    # N2 2(d)'s cap-emulation diagnostics: all four stage rows (round-2
    # finding 2: the earlier text cited the base row alone, the only row at
    # the caps exactly), and N2's own fidelity caveat
    diag = None
    lines2 = lines_of(n2_text)
    for i, line in enumerate(lines2):
        if line.startswith("|") and "re-encoded > 100 (max)" in line:
            rows_ = {}
            for j in range(i + 1, min(i + 8, len(lines2))):
                m_ = re.match(r"\| (base|sft|dpo|instruct) \|", lines2[j])
                if not m_:
                    continue
                cells = [c.strip() for c in re.split(r"(?<!\\)\|", lines2[j])[1:-1]]
                o100 = re.fullmatch(r"(\d+)/(\d+) \((\d+)\)", cells[2]) if len(cells) > 4 else None
                o60 = re.fullmatch(r"(\d+)/(\d+) \((\d+)\)", cells[4]) if len(cells) > 4 else None
                sh = re.fullmatch(r"(\d+)/(\d+)", cells[3]) if len(cells) > 4 else None
                rows_[m_.group(1)] = {
                    "line": j + 1,
                    "b2r_over_100": f"{o100.group(1)}/{o100.group(2)}" if o100 else None,
                    "b2r_max": int(o100.group(3)) if o100 else None,
                    "cut60_shortens": f"{sh.group(1)}/{sh.group(2)}" if sh else None,
                    "cut60_shortens_all": bool(sh) and sh.group(1) == sh.group(2),
                    "b2_over_60": f"{o60.group(1)}/{o60.group(2)}" if o60 else None,
                    "b2_max": int(o60.group(3)) if o60 else None}
            imp = next((k + 1 for k, l3 in enumerate(lines2) if "impossible for exact ids" in l3), None)
            diag = {"header_line": i + 1, "rows": rows_, "impossible_for_exact_ids_line": imp,
                    "overshoot": sorted({v_ for r_ in rows_.values()
                                         for v_ in ((r_["b2r_max"] or 0) - 100, (r_["b2_max"] or 0) - 60) if v_ > 0}) or [0],
                    "stages_at_caps_exactly": sorted(s_ for s_, r_ in rows_.items()
                                                     if r_["b2r_max"] is not None and r_["b2r_max"] <= 100
                                                     and r_["b2_max"] is not None and r_["b2_max"] <= 60)}
            break
    xc["n2"]["cap_diag"] = diag

    if n4_json:
        e2b_n4 = n4_json.get("e2b_cached", {})
        xc["n4"]["e2b_generated_rounds"] = {
            p: (e2b_n4.get(p, {}).get("n_rounds_generated"), EV["e2b"][p]["n_generated"], EV["e2b"][p]["n_entries"],
                EV["e2b"][p]["n_rounds_field"]) for p in EV["e2b"]}
        xc["n4"]["e2b_round_path_cached_agree"] = {
            p: (e2b_n4.get(p, {}).get("round_path_cached"), EV["e2b"][p]["round_path_cached"],
                e2b_n4.get(p, {}).get("round_path_cached") == EV["e2b"][p]["round_path_cached"])
            for p in EV["e2b"]}
        unc = n4_json.get("uncached_cells", {})
        mine = {"data/e2d/d2_sessions.json": EV["e2d"]["d2"]["round_path_cached_key_counts"],
                "data/e2d/d3_sessions.json": EV["e2d"]["d3"]["round_path_cached_key_counts"]}
        for p in fmt:
            mine[p] = fmt[p]["round_path_cached_key_counts"]
        for p in unc:
            if p not in mine:
                mine[p] = count_key(jload(p), "round_path_cached")
        xc["n4"]["uncached_counts_agree"] = {
            p: (unc.get(p), mine.get(p), unc.get(p) == mine.get(p)) for p in sorted(set(unc) | set(mine))}
        g2n4 = n4_json.get("e2a_g2_cached", {})
        xc["n4"]["g2_use_cached_agree"] = {
            "g2r (v2)": (g2n4.get("g2r", {}).get("verdict", {}).get("use_cached"), EV["g2"]["g2r_use_cached"]),
            "g2r2 (v3)": (g2n4.get("g2r2", {}).get("verdict", {}).get("use_cached"), EV["g2"]["g2r2_use_cached"])}
    xc["n4"]["md_statements"] = {
        "e2a full run cached (log-only)": "e2a full run and smokes 2-3** (log-only)" in n4_text,
        "D1 uncached (log-only)": "e2d D1 has no such field and ran uncached" in n4_text,
        "f1 cached vanilla (log-only)": "**f1** (log-only) generated on a cached VANILLA path" in n4_text,
        "first g2 ladder uncached": "e2a first g2 ladder** (log-only, uncached)" in n4_text,
        "TEMP 0.7 cited to clone e2a.py:48": "jlens-qwen36/jlens_qwen/e2a.py:48" in n4_text,
    }
    J["cross_checks"] = xc
    J["evidence"] = EV

    DATA_TOUCH = []
    for p_, x_ in EV["e2b"].items():
        if x_["data_commit_touched_runner_code"]:
            DATA_TOUCH.append(f"{x_['data_commit']} ({p_}: {', '.join(x_['data_commit_touched_runner_code'])}; cited at its run commit {x_['runner_commit']})")
    for t_, x_ in EV["e2d"].items():
        if x_["data_commit_touched_runner_code"]:
            DATA_TOUCH.append(f"{x_['data_commit']} (e2d {t_.upper()}: {', '.join(x_['data_commit_touched_runner_code'])}; cited at its code commit {x_['code_commit']})")
    for p_, x_ in EV["fmt"].items():
        if x_["data_commit_touched_runner_code"]:
            DATA_TOUCH.append(f"{x_['data_commit']} ({p_}: {', '.join(x_['data_commit_touched_runner_code'])})")
    for nm_ in ("b2", "b2r", "b3"):
        if EV[nm_]["data_commit_touched_runner_code"]:
            DATA_TOUCH.append(f"{EV[nm_]['data_commit']} ({nm_}: {', '.join(EV[nm_]['data_commit_touched_runner_code'])})")
    DATA_TOUCH = sorted(set(DATA_TOUCH))
    J["data_commits_touching_runner_code"] = DATA_TOUCH

    # =========================================================== the write-up
    qe = qwen_local
    gc = qe.get("generation_config", {})
    emit("# AUDIT-note-release v1.2 -- N16: decoding-parameters table")
    emit()
    emit(f"- Code stamp: {stamp} (date -u, inside the script)")
    emit(f"- HEAD at run (informational; every repository read is pinned to {PIN} = {pin_full}): {head}")
    emit(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_sha}`, {len(block_lines)} lines; routed `{BLOCK_SHA_ROUTED[0]}...{BLOCK_SHA_ROUTED[1]}`: {'MATCH' if block_match else 'MISMATCH'}; item N16 = block lines 121-122 ({'confirmed' if n16_ok else 'NOT confirmed'} at line 121)")
    emit(f"- Script: `{script_path}` sha256 `{script_sha}`")
    emit(f"- Interpreter: {sys.executable} (Python {platform.python_version()}, numpy {np.__version__}; numpy is used for the seed-stream replays, which must call numpy's Generator to reproduce the record's draws; no scipy/sklearn; no model; no tokenizer library)")
    emit(f"- Command: `{cmd}`")
    emit(f"- Record code executed (compiled from `git show {PIN}:<path>` into an isolated namespace): `valence_core/session_e2a.py` (whole: session_rng, task_sequence, verify_archived_session), `valence_core/detection.py` (plan_trials only). Task corpus `data/corpus/e2a_tasks.jsonl`@{PIN} ({len(TASKS)} tasks x 4 paraphrases).")
    emit(f"- Inputs outside the record, labelled wherever used: (a) the gitignored clone's runner files, read as text (never git inside the clone): " + "; ".join(f"`jlens-qwen36/{k}` sha256 `{v['sha256'][:16]}...`" for k, v in clone.items()) + "; (b) the local Qwen snapshot's tokenizer_config.json / tokenizer.json / generation_config.json, JSON reads only (snapshot " + str(qe.get("snapshot")) + f", the record's 'single local snapshot', {LOG['qwen_snapshot']}).")
    emit(f"- Sibling raws read for the cross-check (working tree, untracked, may change): `{N2_RAW}` sha256 `{xc['n2']['sha256_at_read']}`; `{N4_RAW}` sha256 `{xc['n4']['sha256_at_read']}`; `{N4_JSON}` sha256 `{xc['n4']['json_sha256_at_read']}`; `{N4_SCRIPT}` sha256 `{(xc['n4'].get('script') or {}).get('sha256_at_read')}` (round 2: its counting formula, section 5). All are read as bytes, without newline translation.")
    emit("- Not checked: the note itself. `RESEARCH-NOTE-v0_2-draft.md` is MISSING on this machine (results/raw/2026-10-08_note-preflight.md@bbc9ffe:15), so 'every generated-text DV in the note' is read as the block's list (e2a/e2b/f1 rounds, e2d, B2/B2-r, S1 judge, Q3 rounds) plus k1 (the block's N3(i) cites PROPOSAL-k Stage 1 figures) and the format recon (k1's runner and format); whether the note cites format-recon figures cannot be checked here.")
    emit()
    emit("Status vocabulary (task rule 4), mapped as in the N2 raw's section 1(c) so N1 sees one convention: **reproduced** = an artifact field records the value, or this script establishes it by replaying committed artifacts (named in the cell); **log-only** = no artifact field; committed prose states it (pinned locator), with the committed code line at the run's commit beside it; **not found** = no artifact field and no prose; where committed code at the run's commit fixes the value the cell says *code-fixed* and gives file:line@commit (flagged to the PI, section 7); *clone* = the value is fixed only in the gitignored clone (outside the record; context). Locators are `path@commit:line` from `git show <commit>:<path>`, lines numbered as `sed -n '<n>p'` numbers them (newline only; round-2 finding 1). **computed-new** = a computation the record does not contain (here: introducing commits from git history, and reads of local files outside the record, labelled). 'Code commit' (the commit whose code a cell cites) = the commit that last changed the artifact of record at bbc9ffe, except where a stamped head exists (B2-r), or the record names the commit (D1 at " + D1_CODE + ", " + LOG["d1_code_commit"] + "), or git history fixes it (H1-u at b2d051b, where its data was first committed as the first H1 run; H1 at 6df2072, the commit whose message records the gate run's launch; section 7). Data commits that themselves change runner code (computed over every DV's data commit): " + "; ".join(DATA_TOUCH) + ". Every other data commit changes no runner file, so its code is the code that ran.")
    emit()

    # ---------------- section 1: the table
    E = EV
    e2bv = E["e2b"]["data/e2b/verdict_campaign.json"]
    e2bh1 = E["e2b"]["data/e2b/h1_sessions.json"]
    e2bh1u = E["e2b"]["data/e2b/h1u_sessions.json"]
    e2bh2 = E["e2b"]["data/e2b/h2_sessions.json"]
    k1 = E["fmt"]["data/k/k1_sessions.json"]
    F0, F1, F2 = (E["fmt"][f"data/format/format_recon_F{i}_sessions.json"] for i in range(3))
    g2r2 = E["g2"]["rounds"]["data/e2a/g2_rounds_f0.1.json"]

    def rep(x: dict) -> str:
        return f"{x['seed_streams_match']}/{x['n_sessions']}"

    def capstr(c: dict) -> str:
        if c["cap_hits"]:
            return (f"{c['cap_hits']} cap hit{'s' if c['cap_hits'] != 1 else ''} in {c['n']} rounds, all at n_tok = 60; "
                    f"cap_hit iff n_tok = 60 on {c['consistent']}/{c['n']}; max n_tok {c['max_n_tok']}")
        return (f"no cap hit in {c['n']} rounds; max n_tok {c['max_n_tok']} < 60, consistent with the cap "
                f"but not showing it")

    b2files = E["b2"]["files"]
    b2_alloc = sum(1 for v in b2files.values() if v["alloc_replay_20260823"])
    b2_alloc_default = sum(1 for v in b2files.values() if v["alloc_replay_plan_trials_default_seed"])
    b2_len = (min(v["resp_len_chars"][0] for v in b2files.values()), max(v["resp_len_chars"][1] for v in b2files.values()),
              sum(v["n"] for v in b2files.values()), len(b2files))
    b2r = E["b2r"]["files"]
    b2r_ctl_ok = sum(v["seed_eq_base_plus_trial"] for p, v in b2r.items() if "_control_" in p)
    b2r_ctl_n = sum(v["n"] for p, v in b2r.items() if "_control_" in p)
    b2r_exp = {p: v for p, v in b2r.items() if "_explore_" in p}
    b2r_q = {p: v for p, v in b2r.items() if "_qualify_" in p}
    _ce = [v for v in b2r.values() if "resp_len_chars" in v]
    b2r_len = (min(v["resp_len_chars"][0] for v in _ce), max(v["resp_len_chars"][1] for v in _ce),
               sum(v["n"] for v in _ce), len(_ce))
    _t = sorted({v["temp"] for v in b2r.values()})
    _m = sorted({v["max_tokens"] for v in b2r.values()})
    b2r_temps = str(_t[0]) if len(_t) == 1 else f"NOT UNIFORM {_t}"
    b2r_max = str(_m[0]) if len(_m) == 1 else f"NOT UNIFORM {_m}"
    b3f = E["b3"]["files"]
    b3_rep = f"{sum(v['replay']['seed_streams_match'] for v in b3f.values())}/{sum(v['replay']['n_sessions'] for v in b3f.values())}"
    b3_cap = {k: sum(v["cap"][k] for v in b3f.values()) for k in ("n", "cap_hits", "consistent")}
    e2d = E["e2d"]

    T = []   # rows: (DV, temp, topp/topk, max, seed, stop, ban, path, commits, notes)
    qwen_topk = (f"none: full-vocabulary categorical over (logits + ban vector)/T ({AD['qwen_sample']}; argmax only if T <= 0, {AD['qwen_argmax']}); no top-p, no top-k")
    qwen_stop = (f"first token whose decoded piece contains a newline once a non-whitespace piece has been seen, or EOS ({AD['qwen_stop']}, {AD['qwen_eos']}); the stop token is discarded and the text stripped ({AD['qwen_strip']}); EOS is in the ban list, so the reachable stops are the newline and the cap")
    olmo_samp = f"none: softmax(logits/T) and one multinomial draw ({AD['olmo_pick']}); argmax if T <= 0 ({AD['olmo_argmax']}); no top-p, no top-k"

    eos_strings_in_file = [x for x in ("<|im_end|>", "<|endoftext|>") if x in ban["strings"]]
    V3_COMMITS = (f"template family v3 = the amendment {INTRO[AMEND_KEY][0]} ({INTRO[AMEND_KEY][1]}: newline stop, cap 60; "
                  f"{LOG['e2a_amend_stop']}) + the smoke2 adjudication {INTRO[BAN_KEY][0]} ({INTRO[BAN_KEY][1]}: scaffold logit ban, "
                  f"round generation only, list frozen; {LOG['e2a_ban_adjudication']})")
    T.append(("e2a rounds (Qwen; 200 sessions, {} generated rounds)".format(E["e2a"]["n_rounds_generated"]),
              f"0.7 [log-only: committed prose {AD['e2d_temp_comment']} ('e2a's TEMP'), a later code comment (introduced {INTRO['e2d/config TEMP = 0.7'][0]}, {INTRO['e2d/config TEMP = 0.7'][1]}; e2a's data commit {E['e2a']['commit']} is {cdate(E['e2a']['commit'])}), not an e2a log entry; pre-reg says only 'temperature-sampled' ({LOG['e2a_prereg_sampled_cached']}); clone {cl('jlens_qwen/e2a.py', r'^TEMP = 0\.7')}]",
              f"none [not found in the record; clone {cl('jlens_qwen/e2a.py', r'mx\.random\.categorical\(lg / temp\)')}; the ported adapter that rebuilt e2a's scaffolding samples the same way ({AD['qwen_sample']})]",
              f"60 [reproduced: {capstr(E['e2a']['cap'])} (sessions.jsonl n_tok/cap_hit); log {LOG['e2a_amend_cap']}]",
              f"per session: one numpy Generator default_rng(crc32(f\"{{arm}}|{{s}}\") % 2**31); draws permutation(16), then integers(4) for each of the {_np} planned rounds (2F + N_FREE, F = {_F}, N_FREE = {DRAW['N_FREE']}; all {_np} before any seed), then per forced round a seed integers(2**31), per free round integers(2) (menu) then a seed ({DRAW['order_lines']}; {DRAW['sequence_lines']}; interleaving the paraphrase draws with the seed draws collapses the replay to 4/200, {DRAW['interleave_warning_line']}); the clone passes each round's seed to mx.random.seed (context) [reproduced: {E['e2a']['seed_streams_matched']}/{E['e2a']['n_sessions']} seed streams and {E['e2a']['walk_reconstructed']}/{E['e2a']['n_sessions']} scaffoldings replayed by session_e2a.verify_archived_session@{PIN}]",
              f"newline-after-content or cap 60 [log-only: {LOG['e2a_amend_stop']} (newline stop, cap 60); 'after content' = leading pure-whitespace tokens consumed before the newline stop arms, text stripped, {LOG['e2a_stop_refinement']} (the g2r incident's logged refinement of amendment (a)); consistent: the positional walk ({E['e2a']['walk_reconstructed']}/200) finds no newline inside any generated text]; EOS banned [log-only: the frozen list's strings include {' and '.join('`' + x + '`' for x in eos_strings_in_file)} (data/configs/e2a_ban_list.json@{PIN}), the run printed that list's sha16 ({LOG['e2a_full_ban']}), and the tokenizer config gives eos_token `<|im_end|>` ({LOG['gport_eos_tokcfg']}); recomputed on the local snapshot, section 3]",
              f"frozen 12-id list, sha16 {ban16} [log-only: {LOG['e2a_full_ban']}; frozen before the full run, {LOG['e2a_ban_frozen']}; fixed by the v3 adjudication, {LOG['e2a_ban_adjudication']}; sessions.jsonl has no ban field; the same sha16 is the committed file's and the stored `ban_sha` of the v3 gate artifact g2_discriminability.json (reproduced there)]",
              f"cached (KV stream), steered and sham [log-only: {LOG['e2a_full_cached']}; sessions.jsonl has no path field; the same raw's 'uncached path (g1)' banner ({LOG['e2a_full_stale_banner']}) is stale, as the record says ({LOG['e2a_stale_banner_cosmetic']}; N4 note 13)]",
              f"runner in the clone only (no record commit); pre-reg {INTRO[PREREG_KEY][0]} ({INTRO[PREREG_KEY][1]}: 'temperature-sampled', cached behind the g1 gate); {V3_COMMITS}; data {E['e2a']['commit']}; ban file admitted to the repo {ban_commit} ({cdate(ban_commit)}), after the run",
              f"generation encode kept the 512-token tail (rule 28(d) instance; {LOG['e2a_512_claude']}, log-only)"))
    T.append(("e2a readability corpus g2r2 (Qwen; 128 rounds at dose 0.10; the S1 judge's corpus)",
              f"0.7 [not found: clone only, docstring {cl('scripts/e2a_g2_discriminability.py', r'sampled temp 0\.7')}; no artifact field and no log line; the e2d config comment that is log-only for e2a ({AD['e2d_temp_comment']}) names e2a, not the g2 corpora]",
              "none [as e2a]",
              f"60 [log-only: the template family's cap, {LOG['e2a_amend_cap']}; the artifact has no n_tok ({g2r2['cap_hits']} of {g2r2['n_rounds']} rounds flag cap_hit)]",
              f"per round: crc32(f\"{{task_id}}|{{para}}|{{pole}}|{{frac}}\") % 2**31 [reproduced: {g2r2['seed_formula_matches']}/{g2r2['n_rounds']} recorded seeds; formula from clone {cl('scripts/e2a_g2_discriminability.py', r'def seed_for')}]",
              f"newline-after-content or cap 60, EOS banned: the v3 template family [log-only: {LOG['e2a_amend_stop']}, 'after content' {LOG['e2a_stop_refinement']}, {LOG['e2a_ban_adjudication']}; the artifact records `template_family` = '{E['g2']['g2r2_template_family']}' (reproduced: g2_discriminability.json:template_family); consistent: {g2r2['texts_with_newline']} of {g2r2['n_rounds']} texts contain a newline]",
              f"sha16 {ban16} [reproduced: g2_discriminability.json ban_sha {ban_fields['data/e2a/g2_discriminability.json:ban_sha']}; log {LOG['g2r2_ban']}]",
              f"cached [reproduced: g2_discriminability.json fracs.0.1.use_cached = {E['g2']['g2r2_use_cached']}; log {LOG['g2r2_cached']}]",
              f"clone runner; {V3_COMMITS}; data {g2r2['commit']}",
              "g2r (v2 corpus, g2_rounds_f0.1_v2.json) also cached; first g2 ladder uncached (N4)"))
    T.append(("S1 judge (s1_judge_rescue; Qwen)",
              "n/a: no generation; the judge is a logit-level two-alternative read",
              "n/a",
              "n/a",
              f"none used: every read is one deterministic forward; the runner declares rng = default_rng(20260820) at line {E['s1']['rng_uses'][0]} and never uses it [reproduced from the artifact: {E['s1']['n_reads']} rows carry p_A/p_B/picked_pos only, no text field; pick = (p_A >= p_B) agrees with picked_pos on {E['s1']['pick_rule_consistent']}/{E['s1']['n_reads']}]",
              f"n/a: next-token distribution at the prompt end, softmax over the full vocabulary, compare p(' A') vs p(' B') (scripts/s1_judge_rescue.py@f526377:141-144)",
              "none (no generation; reads take no ban)",
              "uncached plain forward (scripts/s1_judge_rescue.py@f526377:141)",
              f"runner scripts/s1_judge_rescue.py, data f526377 ({cdate('f526377')}); runner blob equal at bbc9ffe: {E['s1']['runner_blob_equal_pin']}",
              "the judged texts are the g2r2 corpus (row above)"))
    PF0 = commits_of('PROPOSAL-f-natural-reinforcer-screen.md')[0]
    T.append(("f1 rounds (Qwen; 344 sessions, {} rounds)".format(E["f1"]["n_rounds"]),
              f"0.7 [log-only: {LOG['gport_f1_temp_cap']}; clone {cl('scripts/f_sessions.py', r'^TEMP = 0\.7')}]",
              f"none [log-only: {LOG['gport_f1_sampling']} ('mx.random.categorical(lg/0.7)')]",
              f"60 [reproduced: {capstr(E['f1']['cap'])}; log {LOG['gport_f1_temp_cap']}]",
              f"per session: default_rng(crc32(f\"f|{{arm}}|{{s}}\") % 2**31); the arm's item permutation(s) first, then per forced round a seed, per free round integers(2) (menu) then a seed; mx.random.seed(seed) after the prefill ({LOG['gport_f1_seedtiming']}) [reproduced: {E['f1']['seed_streams_match']}/{E['f1']['n_sessions']} seed streams, {E['f1']['menu_orders_match']}/{E['f1']['n_sessions']} menu orders; draw order from clone {cl('scripts/f_sessions.py', r'def items_for')}]",
              f"newline-after-content or cap 60; EOS banned [log-only: PROPOSAL-f registers the v3 template family ({LOG['f_stop_ban_proposal_range']}); 'after content' {LOG['e2a_stop_refinement']}; {LOG['gport_f1_stop']}; {LOG['gport_eos_banned']} (its 'every special token' is corrected at {LOG['gport_ban_correction']})]",
              f"sha16 {ban16} [log-only: {LOG['f_stop_ban_proposal_range']} (scaffold-token ban, v3); {LOG['gport_f1_ban']}; sessions.jsonl has no ban field; data/f/calib.json `ban_sha` {E['f1']['calib_ban_sha']} records it for the calibration run (reproduced there); clone {cl('scripts/f_sessions.py', r'BAN_PATH = ')}]",
              f"cached, vanilla (no state anywhere) [log-only: {LOG['f_cached_proposal']}; {LOG['f_ndecl_cached']}]",
              f"clone runner; PROPOSAL-f {PF0} ({cdate(PF0)}; v3 template family {LOG['f_stop_ban_proposal_range']}, cached {LOG['f_cached_proposal']}); {V3_COMMITS.split(' = ')[0]} as e2a ({INTRO[AMEND_KEY][0]} + {INTRO[BAN_KEY][0]}); data {E['f1']['commit']}",
              f"generation encode kept the 512-token tail ({LOG['gport_f1_512']}, log-only)"))
    E2B_TEMP_INTRO = {"scripts/e2b_h1_sessions.py": "e2b_h1 TEMP = 0.7", "scripts/e2b_h2_sessions.py": "e2b_h2 TEMP = 0.7",
                      "scripts/e2b_verdict_campaign.py": "e2b_verdict TEMP = 0.7"}
    for label, x in (("e2b H1-u (aux.; free-phase rounds unsteered; Qwen)", e2bh1u), ("e2b H1 gate run (Qwen)", e2bh1),
                     ("e2b H2 (Qwen)", e2bh2), ("e2b verdict campaign (Qwen)", e2bv)):
        ti = INTRO[E2B_TEMP_INTRO[x["runner"]]]
        T.append((f"{label}; {x['n_sessions']} sessions",
                  f"{x['temp']} [reproduced: artifact `temp`; code {x['temp_line']}]",
                  f"none [not found: code-fixed, {x['adapter_sample_line']}; generate() source identical to bbc9ffe's: {x['adapter_generate_equal_pin']}]",
                  f"60 [reproduced: {capstr(x['cap'])}; code {x['gen_line']}, STOP_CAP defined at {x['stop_cap_def']}]",
                  f"per session: session_rng(key, idx) with key {x['key']}, e2a's draw order [reproduced: {rep(x['replay'])} seed streams ({x['replay']['n_seeds_checked']} seeds)]; order_seed {x['order_seed']} (artifact) shuffles the schedule only",
                  f"newline-after-content or cap 60; EOS banned (adapter port of e2a's rule) [not found as a field; code-fixed {x['adapter_stop_line']}; EOS banned via the frozen list's strings, section 3]",
                  f"frozen file data/configs/e2a_ban_list.json, sha16 {ban16} [not found as a field; code-fixed {x['ban_path_line']}; the file was {'committed' if x['ban_file_committed_at_run_commit'] else 'NOT yet committed (a gitignored local copy)'} at the run commit]",
                  f"{'cached' if x['round_path_cached'] else 'uncached'} [reproduced: artifact `round_path_cached` = {x['round_path_cached']}; kernel `{x['provenance_gdn']}` (provenance)]",
                  f"runner {x['runner']}@{x['runner_commit']} (blob = bbc9ffe: {x['runner_blob_equal_pin']}); TEMP 0.7 introduced {ti[0]} ({ti[1]}); data {x['data_commit']}",
                  f"provenance legacy_truncate_512 = {x['legacy_truncate_512']}, choice_window_declared {x['choice_window_declared']}"))
    for tier, label in (("d1", "e2d D1 (Qwen; harness smoke, dose 0.10)"), ("d2", "e2d D2 (Qwen; dose 0.20)"), ("d3", "e2d D3 (Qwen; dose 0.30, M arm only)")):
        x = e2d[tier]
        path_cell = (f"uncached [log-only: no artifact field; {LOG['d1_uncached']}; code {x['runner_lines']['path']} (`cached=False` hard-coded at the code commit)]" if x["round_path_cached"] == "absent"
                     else f"{'cached' if x['round_path_cached'] else 'uncached'} [reproduced: artifact `round_path_cached` = {x['round_path_cached']}, `round_path_source` = {x['round_path_source']}]")
        if tier == "d1":
            commit_cell = (f"{PJ_CITE}; "
                           f"code of record {x['code_commit']} ({cdate(x['code_commit'])}; {LOG['d1_code_commit']}: 'D1 ran that code'): "
                           f"valence_core/e2d/runner.py + scripts/e2d_sessions.py ({x['runner_lines']['rng']}, {x['runner_lines']['gen']}); "
                           f"data {x['data_commit']}, which also changed {', '.join(x['data_commit_touched_runner_code'])} after the run "
                           f"(`cached=False` became `cached=cached` at {x['d1_data_commit_cached_line']}, and --round-path was added); "
                           f"decoding values unchanged")
        else:
            commit_cell = (f"{PJ_CITE}; "
                           f"runner valence_core/e2d/runner.py + scripts/e2d_sessions.py @{x['code_commit']} = data commit "
                           f"(it changes no runner file: {not x['data_commit_touched_runner_code']}) ({x['runner_lines']['rng']}, {x['runner_lines']['gen']})")
        T.append((f"{label}; {x['n_sessions']} sessions",
                  f"{x['temp']} [reproduced: artifact `temp`; code {x['runner_lines']['temp']}]",
                  f"none [not found: code-fixed, {x['adapter_sample_line']}; generate() source identical to bbc9ffe's: {x['adapter_generate_equal_pin']}]",
                  (f"60 [reproduced: artifact `tstep_licence.position_coverage_note` states 'STOP_CAP is 60'; {capstr(x['cap'])}]" if x["stopcap_field"]
                   else f"60 [not found: code-fixed {x['runner_lines']['gen']}, {x['stop_cap_line']}; {capstr(x['cap'])}]"),
                  f"per session: session_rng(f\"e2d-{{arm}}\", idx) [reproduced: {rep(x['replay'])}]; " + (f"draw_seed {x['draw_seed']} (artifact) assigns cells only" if x['draw_seed'] != 'absent' else "no draw_seed field (D1 built its schedule before the flag existed)") + "; seeds do not depend on the tier (section 4)",
                  f"newline (or the cap, never reached) [reproduced: stop_reason tally {x['stop_reason']}, no 'eos']; EOS banned [not found as a field: code-fixed {x['adapter_stop_line']} with the EOS id in the ban list (section 3)]",
                  f"rebuilt from the live tokenizer [reproduced (count only): artifact `ban_list` = {x['ban_list']} (counts only, equal to the frozen file's 12/12; identity with the file is not shown by the artifact); code {x['runner_lines']['ban']}]",
                  path_cell,
                  commit_cell,
                  ""))
    OB = E["b3"]["olmo_ban"]
    OBL = OB["local_base_tokenizer_outside_record"]
    olmo_sub = ", ".join(f"{i} '{p_}'" for p_, i in sorted(OB["subword_pieces_from_record"].items(), key=lambda kv: kv[1]))
    OLMO_BAN_CELL = (f"9 ids from 6 strings at every stage, 5 of them ordinary sub-word pieces ({olmo_sub}), because `<think>`/`</think>` are not "
                     f"added tokens in OLMo's vocabulary and the builder bans every piece of each string ({OB['builder_lines']}) "
                     f"[log-only: ids {OB['record_ids_locator']}, the 'five of nine' {OB['record_five_locator']}; reproduced: those 9 ids hash to the "
                     f"B3 artifacts' `ban_list.sha16` {OB['sha16_sorted_ids_convention']} (sorted-ids convention, {OB['b3_sha_line']}; all four stages: "
                     f"{OB['b3_convention_matches_all_stages']}) and to the A2 artifacts' {OB['sha16_ids_strings_convention']} ({{ids, strings}} convention, "
                     f"{OB['a2_sha_line']}; all four stages: {OB['a2_convention_matches_all_stages']}); the strings are the A2 and scaffold artifacts' "
                     f"`ban_list.strings` / `ban_strings` (reproduced)]")
    LOCKG = E["b2"]["lock_g"]
    T.append((f"OLMo B2 detection (greedy; both arms, 4 stages, 8 files x 48 trials)",
              f"0.0 [log-only: {LOG['b2_temp0']}; {E['b2r']['addendum_b2_greedy_line']} ('ours ran 0.0'); code {E['b2']['lines']['gen']}; no artifact field]",
              f"n/a: argmax ({AD['olmo_argmax']})",
              f"60 [log-only: {LOG['b2_max60']}; code {E['b2']['lines']['max']}, no override in the driver ({E['b2']['lines']['driver_no_override']}; the driver was committed after the run, as its provenance)]",
              f"allocation and generation share args.seed = 20260823: plan_trials permutation seeded 20260823 [reproduced: {b2_alloc}/8 files' injected/concept allocation replayed by detection.plan_trials@{PIN}; plan_trials' own default seed {E['b2']['plan_trials_default_seed']} replays {b2_alloc_default}/8]; generation seed 20260823 + n per trial (torch.manual_seed per call, {AD['olmo_seed']}) [not found: code-fixed {E['b2']['lines']['gen']}; not recorded, and inert at T = 0, {LOG['b2_seed_inert']}]; adapter load seed 20260818 (provenance `seed`, reproduced)",
              f"EOS or the 60 cap, no newline stop; EOS banned, so by the code argument every generation runs to 60 tokens [not found: code-fixed {E['b2']['lines']['stop']}; section 3]; the scored text is then cut at the first turn marker (segment_own_turn), a text operation, not a decoding stop",
              f"rebuilt per stage from the live tokenizer: scaffold strings + tokenizer special strings [not found as a B2 field: code-fixed {E['b2']['lines']['ban']}, the default builder (source at 720a104 = bbc9ffe's: {OB['builder_source_equal']['720a104']})]; by the same builder on the same tokenizers: {OLMO_BAN_CELL}",
              f"uncached [log-only: {LOG['b_phase_uncached']}; code {E['b2']['lines']['cached']}]",
              f"runner built {E['b2']['runner_intro']} ({cdate(E['b2']['runner_intro'])}; temp=0.0, --max-tokens 60, --seed 20260823 all introduced there); data {E['b2']['data_commit']} (blob = bbc9ffe: {E['b2']['runner_blob_equal_pin']}; adapter blob = bbc9ffe: {E['b2']['adapter_blob_equal_pin']}); not pre-registered: LOCK-g's B2 section registers the seeded allocation ({LOCKG['seeded_perm_line']}) and names no decoding parameter (no temperature, max-token or top-p/top-k string in LOCK-g.md: {not LOCKG['decoding_terms']}; its only 'greedy' is the roster search, {LOCKG['greedy_lines']})",
              "provenance deterministic = True (all 8 files)" if all(v["deterministic"] for v in b2files.values()) else "determinism flag not uniform"))
    PRE_B2R = f"pre-registered: {E['b2r']['addendum_decoding_lines']} ({E['b2r']['addendum_commit']}, {E['b2r']['addendum_commit_date']})"
    T.append((f"OLMo B2-r detection (sampled; control x4, qualify x{len(b2r_q)}, explore x{len(b2r_exp)})",
              f"{b2r_temps} [reproduced: artifact `temp`, one value on all {len(b2r)} files; {PRE_B2R}; code {E['b2r']['lines']['temp']}]",
              f"none [not found: code-fixed, {AD['olmo_pick']}; the addendum says it names every decoding parameter ({E['b2r']['addendum_names_all_line']}) and names no top-p/top-k (no top-p/top-k string in it: {not E['b2r']['addendum_mentions_top_p_or_k']}), consistent with none]",
              f"{b2r_max} [reproduced: artifact `max_tokens`, one value on all {len(b2r)} files; {PRE_B2R}; code {E['b2r']['lines']['max']}]",
              f"per trial, torch.manual_seed per call: control and explore 20260824 + trial n [reproduced: {b2r_ctl_ok}/{b2r_ctl_n} control trials; explore {sum(v['seed_eq_base_plus_trial'] for v in b2r_exp.values())}/{sum(v['n'] for v in b2r_exp.values())}, allocation replay {sum(1 for v in b2r_exp.values() if v['alloc_replay'])}/{len(b2r_exp)}; explore trials reuse the control trial's seed {sum(v['explore_seeds_equal_control_seeds'] for v in b2r_exp.values())}/{sum(v['n'] for v in b2r_exp.values())}]; qualify: control 20260824 + 9000 + 100*prompt + k, injected 20260824 + 1000*strength + 100*prompt + k [reproduced: {sum(v['control_seed_formula_ok'] for v in b2r_q.values())}/{sum(v['n_control_rows'] for v in b2r_q.values())} and {sum(v['injected_seed_formula_ok'] for v in b2r_q.values())}/{sum(v['n_injected_rows'] for v in b2r_q.values())}; one seed serves every concept at a (strength, prompt, k)]; 'per-trial seeds are live and declared' ({E['b2r']['addendum_decoding_lines']}); adapter load seed 20260818",
              f"EOS or the 100 cap, no newline stop; EOS banned, so by the code argument every generation runs to 100 tokens [not found: code-fixed {E['b2r']['lines']['stop']}; section 3]; then segment_own_turn_v2 (turn markers + a re-emitted 'Trial N:')",
              f"as B2 [not found as a B2-r field: code-fixed {E['b2r']['lines']['ban']}, the default builder (source at b6e8f3f = bbc9ffe's: {OB['builder_source_equal']['b6e8f3f']})]: the same 9 ids, 5 of them sub-word pieces (B2 cell)",
              f"uncached [log-only: {LOG['b_phase_uncached']}; code {E['b2r']['lines']['cached']}; no artifact field]",
              f"decoding pre-registered in ADDENDUM-g3-b2r-v1.2 §0.5 at {E['b2r']['addendum_commit']} ({E['b2r']['addendum_commit_date']}; {E['b2r']['addendum_decoding_lines']}; an ancestor of the runner commit {INTRO['box_b2r TEMP = 1.0'][0]}: {E['b2r']['addendum_before_runner_intro']}); runner {INTRO['box_b2r TEMP = 1.0'][0]} (TEMP 1.0, MAX_TOKENS 100, --seed 20260824 introduced); stamped head {E['b2r']['stamped_head']} ({E['b2r']['stamped_head_line']}); data {E['b2r']['data_commit']}; runner blob = bbc9ffe at data and stamped head: {E['b2r']['runner_blob_equal_pin']} / {E['b2r']['runner_blob_stamped_equal_pin']}",
              ""))
    b3pairs = E['b3']['same_arm_session_seeds_equal_across_stages']
    b3all = E['b3']['same_arm_session_seeds_equal_all_stage_pairs']
    T.append((f"OLMo B3 / Q3 rounds (screen tier, 4 stages, {sum(v['n_sessions'] for v in b3f.values())} sessions)",
              f"0.7 [log-only: {LOG['b3_temp07']}; code {E['b3']['lines']['temp']}, CLI default {E['b3']['lines']['temp_cli']}, no override in the driver ({E['b3']['lines']['driver_no_override']}, committed after the run as its provenance); no artifact field]",
              f"none [not found: code-fixed, {AD['olmo_pick']}]",
              f"60 [reproduced: {b3_cap['cap_hits']} cap hits in {b3_cap['n']} rounds, cap_hit iff n_tok = 60 on {b3_cap['consistent']}/{b3_cap['n']}; code {E['b3']['lines']['gen']}]",
              f"per session: session_rng(f\"b3-{{arm}}\", idx), e2a's draw order [reproduced: {b3_rep} seed streams]; the key omits the stage, so the same (arm, idx) draws the same seeds and tasks at every stage ({b3pairs} same-(arm, idx) pairs equal, each non-base stage against base; {b3all} over all six stage pairs; {E['b3']['keys_present_at_all_four_stages']} (arm, idx) keys at all four stages); adapter load seed 20260818",
              f"newline-after-content or cap 60; EOS banned (code argument) [not found as a field: code-fixed, adapter default stop_newline=True ({AD['olmo_stop_default']}), rule {AD['olmo_stop_rule']}; consistent: cap_hit iff n_tok = 60]",
              (f"rebuilt per stage; one list at all four stages: artifact `ban_list` n_ids {next(iter({v['ban_list']['n_ids'] for v in b3f.values()}))}, sha16 {next(iter({v['ban_list']['sha16'] for v in b3f.values()}))} [reproduced]; {OLMO_BAN_CELL}"
               if len({v['ban_list']['sha16'] for v in b3f.values()}) == 1 else f"rebuilt per stage; NOT one list: {[v['ban_list'] for v in b3f.values()]} [reproduced]"),
              f"uncached [log-only: {LOG['b_phase_uncached']}; code: run_session's default ({E['b3']['lines']['cached_default']}), the call passes none ({E['b3']['lines']['call_no_cached']}); no artifact field]",
              f"runner TEMP 0.7 introduced {INTRO['box_b3 TEMP = 0.7'][0]} ({INTRO['box_b3 TEMP = 0.7'][1]}); data {E['b3']['data_commit']} (runner blob = bbc9ffe: {E['b3']['runner_blob_equal_pin']})",
              ""))
    for label, x in (("PROPOSAL-k Stage 1 (k1) sham sessions (Qwen)", k1), ("format recon F0 (Qwen)", F0),
                     ("format recon F1 (Qwen)", F1), ("format recon F2 (Qwen)", F2)):
        keys_s = ", ".join(f'"{k_}"' for k_ in x["rng_keys"])
        T.append((f"{label}; {x['n_sessions']} sessions",
                  f"{x['temp_top']} [reproduced: artifact `temp`, `identity.temp` = {x['identity_temp']}; per-session `temp` {x['temp_rows']}" + (f"; log {LOG['k1_temp']}" if "k1" in x["artifact"] else "") + f"; code {x['runner_lines']['temp']}]",
                  f"none [not found: code-fixed, {x['adapter_sample_line']}; generate() source identical to bbc9ffe's: {x['adapter_generate_equal_pin']}]",
                  (f"60 [reproduced: {capstr(x['cap'])}]" if x["cap"]["cap_hits"]
                   else f"60 [not found: code-fixed {x['runner_lines']['gen']}, {x['stop_cap_line']}; {capstr(x['cap'])}]"),
                  f"per session: session_rng(key, idx), key {keys_s} [reproduced: {rep(x['replay'])}]; draw_seed {x['draw_seed']} assigns cells only",
                  f"newline, or the cap where hit [reproduced: stop_reason tally {x['stop_reason']}, no 'eos']; EOS banned [not found as a field: code-fixed {x['adapter_stop_line']} with the EOS id in the ban list (section 3)]",
                  (f"rebuilt from the live tokenizer [reproduced (count only): artifact `ban_list` = {x['ban_list']} (counts only, equal to the frozen file's 12/12; identity with the file is not shown by the artifact); code {x['ban_line']}]" if x["ban_list"] != "absent"
                   else f"rebuilt from the live tokenizer ({x['ban_line']}); no artifact field [not found: code-fixed]"),
                  f"uncached [reproduced: per-round `round_path_cached` {x['round_path_cached_items']}; code {x['runner_lines']['cached']}]",
                  f"runner valence_core/formats/recon.py@{x['data_commit']} = data commit (it changes no runner file: {not x['data_commit_touched_runner_code']}) ({x['runner_lines']['rng']}, {x['runner_lines']['gen']}); recon's `cached = False` introduced {INTRO['formats/recon cached = False'][0]} ({INTRO['formats/recon cached = False'][1]})",
                  f"provenance legacy_truncate_512 = {x['legacy_truncate_512']}"))

    def tier(cell: str) -> str:
        """Source tier of a cell; a cell carrying two statuses (a split
        cell, e.g. 'newline [reproduced] ; EOS banned [code-fixed]') gets
        both letters joined by '+'."""
        c = cell.strip()
        if c.startswith("n/a") or c.startswith("none (no generation") or c.startswith("uncached plain forward"):
            return "-"
        ms = list(re.finditer(r"\[(reproduced|log-only|not found)([^\]]*)", c))
        if not ms:
            return "=e2a" if "[as e2a]" in c else "?"
        out = []
        for m in ms:
            st, rest = m.group(1), m.group(2)
            if st == "reproduced":
                t_ = "A"
            elif st == "log-only":
                t_ = "L"
            elif "code-fixed" in rest:
                t_ = "C"
            elif "clone" in rest:
                t_ = "K"
            else:
                t_ = "N"
            if t_ not in out:
                out.append(t_)
        return "+".join(out)
    keys = ("T", "p/k", "max", "seed", "stop", "ban", "path")
    T = [r + ("; ".join(f"{k} {tier(r[i + 1])}" for i, k in enumerate(keys)),) for r in T]
    emit("## 1. The table")
    emit()
    emit("One row per generated-text DV (plus the S1 judge, which generates nothing). Each cell: value [status: source]. Choice reads are not generated in any cell: they are separate uncached forwards, restricted to the two label tokens, argmax with ties to the first-listed label, no temperature, no ban; e2b's quarantined state-present read adds its declared injection plus an unsteered shadow (N4, N6) (" + AD["readout_no_ban"] + "; Qwen pre-registration " + LOG["e2a_prereg_choice_greedy"] + ").")
    emit()
    J["table"] = [dict(zip(("dv", "temperature", "top_p_top_k", "max_new_tokens", "seed_policy", "stop",
                            "ban_list", "path", "commits", "notes", "source_tiers"), r)) for r in T]
    emit("Source-tier column (one letter per parameter, in column order: T temperature, p/k top-p/top-k, max, seed, stop, ban, path): A = artifact field or artifact replay (status reproduced); C = committed code at the run's commit only (status not found, code-fixed); L = committed prose (status log-only); K = the gitignored clone only (outside the record); - = not applicable; =e2a = as the e2a row; X+Y = a split cell carrying two statuses (e.g. a stop rule whose newline part is in the artifact and whose EOS part is code-fixed).")
    emit()
    emit("| DV | temperature | top-p / top-k | max new tokens | seed policy | stop tokens / discipline | scaffold-token ban (round generation only) | cached vs uncached | commit(s) that fixed them | notes | source tiers |")
    emit("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in T:
        emit(md_row(r))
    emit()

    # ---------------- section 2: introducing commits
    emit("## 2. The commits that introduced each value of record (git log -S over bbc9ffe's history; oldest hit)")
    emit()
    emit("| value (file) | introducing commit | date (git author date, short) | note |")
    emit("|---|---|---|---|")
    FOLLOWED = {"session_e2a STOP_CAP = 60", "qwen_mlx categorical(lg / temp)", "session.py DEFAULT_SCAFFOLD_STRINGS"}
    for k, (c, d) in INTRO.items():
        note = ""
        if k == "session_e2a STOP_CAP = 60" and STOPCAP_FOLLOW["no_follow"] != STOPCAP_FOLLOW["follow"]:
            note = (f"with --follow; at {c} the file was `{STOPCAP_FOLLOW['path_at_follow_hit']}`. Without --follow, git log -S on the "
                    f"current path returns {STOPCAP_FOLLOW['no_follow']} ({cdate(STOPCAP_FOLLOW['no_follow'])}), the commit that renamed it "
                    f"to valence_core/session_e2a.py; every e2b run commit predates the rename and defines STOP_CAP in the old file (table, e2b rows)")
        elif k in FOLLOWED:
            note = "with --follow (same result without it)"
        elif k.startswith("log: "):
            note = "searched over RESULTS.md and archive/RESULTS-cycles3-4.md (the log moved at c07a5e0)"
        emit(md_row((k, c, d, note)))
    emit()
    emit("Reading: the Qwen session families after e2a (e2b, e2d, k1, format) take STOP_CAP from the Route-3 port of e2a's template (`valence_core/session_e2a.py`; `valence_core/e2b/session.py` until its rename at " + str(STOPCAP_FOLLOW["no_follow"]) + ", which is where the four e2b runs read it; introduced with the port's acceptance commit, which replayed 200/200 archived e2a seed streams) and TEMP 0.7 from their own constants (e2b scripts) or `valence_core/e2d/config.py` (e2d, k1, format). Their sampling, stop rule and cached path live in `valence_core/adapters/qwen_mlx.py`, whose generate() is a port of the clone's `e2a.generate_round_positional`. The OLMo families take temperature, cap and seed from their box runners and sampling from `valence_core/adapters/olmo_hf.py`. e2a, its g2 corpora and f1 ran on the clone, so no record commit introduces their runner: the record fixes their parameters through the log: the pre-registration (" + INTRO[PREREG_KEY][0] + ": temperature-sampled rounds, cached behind the g1 gate), the template amendment (" + INTRO[AMEND_KEY][0] + ": newline stop, cap 60; its logged refinement at " + REFINE["commit"] + ", the g2r incident: leading pure-whitespace tokens consumed before the newline stop arms, " + REFINE["lines"] + ") and the smoke2 adjudication that made the template family v3 (" + INTRO[BAN_KEY][0] + ": the scaffold-token logit ban, round generation only, list frozen with its sha logged; " + LOG["e2a_ban_adjudication"] + "), then PROPOSAL-f for f1 (" + PF0 + ", which registers 'v3 template family (newline stop, scaffold-token ban, ...)', " + LOG["f_stop_ban_proposal_range"] + "). For e2d, which ran on valence_core code, PROPOSAL-j (" + PJ_C + ", " + PJ["date"] + ") holds 'template family v3 with its bans, stop discipline, and audit patterns' fixed, the dose the only change (" + PJ["lines"] + "); " + PJ_C + " is an ancestor of D1's code commit " + D1_CODE + " and of every e2d data commit (" + str(PJ["precedes_every_e2d_code_and_data_commit"]) + "), so e2d's newline stop, 60-token backstop and ban were pre-registered by reference before its code and data. The ban file itself was admitted to the repo later (" + ban_commit + "); its sha matches the sha16 the runs printed and stored. Temperature values in the pre-registration documents: of the tracked PROPOSAL-/LOCK-/ADDENDUM- files at bbc9ffe, the ones that mention a temperature at all are " + ", ".join(f"{k} ({v} lines)" for k, v in PREREG_TEMP.items() if v) + " (regex /temperature|temp[ =]+digit|TEMP digit/i); PROPOSAL-m's campaign has produced no DV in this table. So B2-r is the one DV here whose temperature and max-token values were pre-registered: ADDENDUM-g3-b2r-v1.2 section 0.5 (" + E["b2r"]["addendum_commit"] + ", " + E["b2r"]["addendum_decoding_lines"] + ") names temperature 1.0, max_new_tokens 100 and live per-trial seeds before the runner existed. For the Qwen families the cap and stop rule were fixed in the log before data (the e2a amendment and the v3 adjudication above), and for f1 and e2d also pre-registered by reference to the v3 family (PROPOSAL-f, PROPOSAL-j), neither of which states a temperature (temperature lines: PROPOSAL-f " + str(PREREG_TEMP.get("PROPOSAL-f-natural-reinforcer-screen.md")) + ", PROPOSAL-j " + str(PJ["temperature_mentions"]) + "); e2a's pre-registration says only 'temperature-sampled'.")
    emit()

    # ---------------- section 3: EOS, ban list, vendor defaults
    emit("## 3. The ban list, EOS, and the vendor defaults that are not used")
    emit()
    emit(f"- Frozen Qwen file `data/configs/e2a_ban_list.json`@{PIN}: sha256 `{ban_sha}` (sha16 `{ban16}`), {len(ban['strings'])} strings, {len(ban['ids'])} ids; admitted to the repo at {ban_commit} ({cdate(ban_commit)}), after e2a and f1 ran; every stored sha16 equals it: " + "; ".join(f"`{k}` = {v} ({'equal' if v == ban16 else ('field absent' if v is None else 'DIFFERENT')})" for k, v in ban_fields.items()) + ".")
    emit(f"- Banned strings anywhere in the generated record (substring scan, the file's 12 strings): e2a transcripts {E['e2a']['banned_string_hits_in_transcripts']}; f1 transcripts {E['f1']['banned_string_hits_in_transcripts']}; e2b transcripts " + ", ".join(f"{os.path.basename(p)} {v['banned_string_hits_in_transcripts']}" for p, v in E['e2b'].items()) + "; e2d round texts " + ", ".join(f"{t} {v['banned_string_hits_in_texts']}" for t, v in e2d.items()) + "; k1/format round texts " + ", ".join(f"{os.path.basename(p)} {v['banned_string_hits_in_texts']}" for p, v in E['fmt'].items()) + f". OLMo (6 recorded strings): B2 response_raw {sum(v['banned_hits_raw'] for v in b2files.values())}, B2-r response_raw {sum(v['banned_hits_raw'] for v in b2r.values())}, B3 transcripts {sum(v['banned_hits'] for v in b3f.values())}. A zero is consistent with the ban; it does not prove it (a banned special token can still be spelled out of ordinary tokens). The B2-r hits: " + "; ".join(f"{os.path.basename(p)} trial {h['trial']} contains `{h['string']}` (audit {h['audit']!r}, claimed_detection {h['claimed_detection']})" for p, v in b2r.items() for h in v.get("banned_hit_trials", [])) + ". Both ids are in the stage's ban list at -1e30 before the softmax, so the sampler cannot emit them as single special tokens; the text was presumably spelled from ordinary tokens. The artifacts store no token ids, so this cannot be settled from the record; the audit excluded the `<|im_end|>` trial and B2-r's audit list does not include `<|endoftext|>` (" + E["b2r"]["lines"]["audit_ban"] + "), so that trial stayed decidable and scored no claim.")
    emit(f"- **Round generation only.** Callers pass ban_ids to generate() and never to the choice read, whose signature has no ban parameter ({AD['readout_no_ban']}; the builder's docstring, {loc(PIN, 'valence_core/session.py', r'ROUND GENERATION ONLY')}); f1's read in the clone likewise has none ({LOG['gport_ban_read']}, log-only). The S1 judge and every choice read therefore see the unbanned distribution.")
    emit(f"- **EOS is banned on Qwen, so the EOS stop is unreachable.** Record (log-only): for f1 (and m), {LOG['gport_eos_banned']}, which is about those two runners; the eos identity, {LOG['gport_eos_tokcfg']}; for e2a and the e2b runs (which load the frozen file), the file's strings include {' and '.join('`' + x + '`' for x in eos_strings_in_file)} (data/configs/e2a_ban_list.json@{PIN}) and e2a's run printed the file's sha16 ({LOG['e2a_full_ban']}); e2d, k1 and format rebuild the list from the live tokenizer; e2d and format store only its counts (12 ids / 12 strings) and k1 stores no ban field, so for them the EOS ban is the builder's code argument (plus, for e2d and format, the matching counts). Recomputed here (computed-new; local snapshot, outside the record): tokenizer_config eos_token = `{qe.get('eos_token')}` -> id {qe.get('eos_id')}, in the ban ids: {qe.get('eos_id_in_ban_ids')}; `<|endoftext|>` -> id {qe.get('endoftext_id')}, in the ban ids: {qe.get('endoftext_in_ban_ids')}; the file's 12 strings map to exactly its 12 ids on this tokenizer: {qe.get('ban_ids_equal_local_map')}. The record's own correction stands: the list bans 10 of the tokenizer's special-flagged tokens plus `<think>`/`</think>`, not every special token ({LOG['gport_ban_correction']}). Where the artifacts record why a round stopped (e2d, k1, format), 'eos' never occurs (stop_reason tallies in the table).")
    _ob = E["b3"]["olmo_ban"]
    _ol = _ob["local_base_tokenizer_outside_record"]
    emit(f"- **OLMo**: the ban list is rebuilt per stage from `DEFAULT_SCAFFOLD_STRINGS` ({AD['ban_builder']}) plus the tokenizer's `all_special_tokens` ({AD['ban_builder_special']}; {AD['olmo_special']}), and every token piece of every string is banned ({_ob['builder_lines']}). The A2 artifacts record the resulting strings at every stage: " + "; ".join(f"{st}: {v['strings']} ({v['n_ids']} ids)" for st, v in E['b3']['a2_ban_lists'].items()) + f"; the scaffold artifacts (data/olmo/scaffold_*.json, {_ob['scaffold_commit']}) record the same six `ban_strings` with `ban_roster_size` 9 at every stage (reproduced: " + str(all(v.get('ban_strings') == sorted(next(iter(E['b3']['a2_ban_lists'].values()))['strings']) and v.get('ban_roster_size') == 9 for v in _ob['scaffold_fields'].values())) + ").")
    emit(f"- **OLMo: five of the nine banned ids are ordinary sub-word tokens.** `<think>` and `</think>` are not added tokens in OLMo's vocabulary, so the builder bans their pieces: " + ", ".join(f"id {i_} '{p_}'" for p_, i_ in sorted(_ob['subword_pieces_from_record'].items(), key=lambda kv: kv[1])) + f"; the other four are the specials {'/'.join(str(x) for x in _ob['special_ids_from_record'])}. Source: the record's m-v1.10 referent check, which read the base tokenizer.json ({_ob['record_ids_locator']}; 'five of the nine banned ids are ordinary sub-word tokens', {_ob['record_five_locator']}; checker note {_ob['record_check_locator']}; log-only). Reproduced here from committed artifacts: those nine ids, sorted, hash to {_ob['sha16_sorted_ids_convention']} = the B3 artifacts' `ban_list.sha16` at all four stages ({_ob['b3_convention_matches_all_stages']}; B3 hashes json.dumps(sorted ids), {_ob['b3_sha_line']}), and with the six strings to {_ob['sha16_ids_strings_convention']} = the A2 artifacts' `ban_list.sha16` at all four stages ({_ob['a2_convention_matches_all_stages']}; A2 hashes json.dumps({{ids, strings}}, sort_keys=True), {_ob['a2_sha_line']}). The two stored sha16s differ only by convention; both are the same nine ids. The id set is identical at every stage (the B3 sha16 is one value at all four). Computed-new, outside the record: the local base tokenizer.json in the HF cache (snapshot {_ol.get('snapshot')}) names the same pieces for these ids ({_ol.get('pieces_agree_with_record')}), has no added `<think>`/`</think>` ({_ol.get('think_strings_are_added_tokens')}), and gives eos_token `{_ol.get('eos_token')}` -> id {_ol.get('eos_id')}, in the nine: {_ol.get('eos_id_in_ids')}; but its tokenizer.json is NOT byte-identical to the run's pinned base file (sha256 equal to data/olmo/manifest.json's base entry: {_ol.get('tokenizer_json_sha256_equals_manifest_base')}; tokenizer_config.json equal: {_ol.get('tokenizer_config_sha256_equals_manifest_base')}), so the piece names are corroboration, not the run's file. Consequence: in every OLMo round generation (B2, B2-r, B3), the ordinary token '>' (id 29) and the pieces '</', 'ink', '<th', 'think' were at -1e30 before the softmax, at every stage. The characters can still be produced by other token ids (only these ids are suppressed). Whether this moved any OLMo DV is not settled here; it is a decoding fact a reader of the decoding paragraph should have. On Qwen the frozen list's 12 strings are all added tokens, one id each (section 3, Qwen bullet), so no ordinary piece is banned there.")
    emit(f"- **OLMo EOS.** Both candidate end-of-sequence strings (`<|endoftext|>`, `<|im_end|>`) are in the list at every stage. The adapter's EOS is `tokenizer.eos_token_id`, and transformers lists the eos token in `all_special_tokens`, so the EOS id is banned and the EOS stop is unreachable: a code argument; the run tokenizers' configs are hash-pinned in `data/olmo/manifest.json` but their contents are not in the record (the local base tokenizer_config above is a different file). Consequence for B2 and B2-r (stop_newline=False), by the same code argument: every generation ran to its cap (60 / 100 tokens) before segmentation.")
    emit(f"- **Vendor sampling defaults are not used anywhere.** Neither adapter reads `generation_config.json`; both sample the full softmax at the runner's temperature. For the reader: the local Qwen snapshot's generation_config.json (sha16 {qe.get('generation_config_sha16')}, outside the record, computed-new) sets temperature {gc.get('temperature')}, top_k {gc.get('top_k')}, top_p {gc.get('top_p')}, do_sample {gc.get('do_sample')}; our Qwen cells sampled at 0.7 with no top-k/top-p. The OLMo checkpoints' generation_config.json files are hash-pinned in the manifest; their contents were not read (no local copy of the run files on this machine).")
    emit("- Kernel path (Qwen, valence_core runs): provenance `gdn_inference_mode` = 'ops (fused disabled)' on every e2b/e2d/k1/format artifact read here (reproduced); f1 used the ops kernel on its cached path too (" + LOG["gport_gdn"] + ", log-only). OLMo: provenance `deterministic` True with `cublas_workspace_config` ':4096:8' on every B2/B2-r/B3 file (reproduced: " + str(all(v['deterministic'] for v in b2files.values()) and all(v['deterministic'] for v in b2r.values()) and all(v['deterministic'] for v in b3f.values())) + ").")
    emit()

    # ---------------- section 4: seed-policy details
    emit("## 4. Seed policy: what is global and what is per round")
    emit()
    emit("- **Qwen (MLX)**: there is no global seed. Every generate call reseeds MLX's global PRNG with that round's seed (" + AD["qwen_seed"] + "; f1 and e2a in the clone likewise, after the prefill). The round seed is drawn from one numpy Generator per session, keyed by a string, so a session's content (tasks, paraphrases, menu orders, seeds) is a function of (key, index) alone and does not move with the schedule seed (`order_seed` / `draw_seed`), which only assigns cells.")
    emit("- **OLMo (CUDA)**: the adapter seeds torch once at load (20260818, provenance `seed`) and reseeds `torch.manual_seed(seed)` at every generate call (" + AD["olmo_seed"] + "). B2/B2-r seeds are trial-indexed (base + n); B3 seeds come from the session Generator as on Qwen.")
    emit(f"- **Shared seeds by construction (descriptive, computed-new).** e2d: the key `e2d-{{arm}}` omits the tier, so D1, D2 and D3 sessions with the same (arm, index) draw identical seeds and tasks (same-(arm, index) pairs with equal seed prefixes: D1 vs D2 {E['e2d_shared_seeds']['d1_vs_d2']}, D1 vs D3 {E['e2d_shared_seeds']['d1_vs_d3']}, D2 vs D3 {E['e2d_shared_seeds']['d2_vs_d3']}). B3: the key `b3-{{arm}}` omits the stage, so the four stages are common-random-number paired ({E['b3']['same_arm_session_seeds_equal_across_stages']} same-(arm, index) pairs with equal seed prefixes, each non-base stage against base; {E['b3']['same_arm_session_seeds_equal_all_stage_pairs']} over all six stage pairs). B2-r: explore trials reuse the control trial's seed ({sum(v['explore_seeds_equal_control_seeds'] for v in b2r_exp.values())}/{sum(v['n'] for v in b2r_exp.values())}; the N2 raw's 5(e) makes the same point), and in qualify one seed serves every concept at a given (strength, prompt, k) (up to {max(v['max_rows_sharing_one_seed_within_strength'] for v in b2r_q.values())} rows per seed). None of this is a defect; a reader comparing doses, stages or concepts should know the comparisons are seed-paired.")
    emit()

    # ---------------- section 5: cross-checks
    emit("## 5. Cross-check against the N2 raw's decoding table and the N4 raw's cached-path list")
    emit()
    emit(f"N2 (`{N2_RAW}`, section 1(c); sha256 at read `{xc['n2']['sha256_at_read']}`). For each parameter: does N2's B2-r cell / B2 cell carry the value this raw finds, and N2's status label.")
    emit()
    emit("| parameter | N2 B2-r cell agrees | N2 status (B2-r) | N2 B2 cell agrees | N2 status (B2) | this raw |")
    emit("|---|---|---|---|---|---|")
    mine_b2 = {"temperature": "B2-r 1.0 reproduced; B2 0.0 log-only",
               "top-p": "none / n/a, not found (code-fixed)", "top-k": "none / n/a, not found (code-fixed)",
               "max new tokens": "B2-r 100 reproduced; B2 60 log-only",
               "seed policy": "B2-r reproduced; B2 allocation seed reproduced by replay, per-trial generation seed code-fixed",
               "stop rule": "EOS is banned, so the cap is the only reachable stop",
               "banned tokens": "agrees; adds that the EOS strings are among them and that every piece of each string is banned, so 5 of the 9 ids are ordinary sub-word pieces (section 3)",
               "generation path": "uncached; log-only for both (B-phase disposition), with the code line beside"}
    for r in xc["n2"]["rows"]:
        emit(f"| {r['param']} | {r['n2_b2r_cell_has']} | {r['n2_b2r_status']} | {r['n2_b2_cell_has']} | {r['n2_b2_status']} | {mine_b2[r['param']]} |")
    emit()
    emit(f"Agreements and differences with N2: (a) every value agrees. (b) Status, B2 seed: N2 marks it log-only; this raw replays B2's trial allocation from the artifacts with `detection.plan_trials(names, 48, 20260823)` ({b2_alloc}/8 files), which fixes args.seed = 20260823 and so the generation seed formula 20260823 + n (code), though the per-trial generation seed itself is not recorded. Not a value disagreement. (c) Substance, stop rule: N2's 'EOS token or the cap' is the code's rule; with the EOS strings in the ban list the reachable stop for B2/B2-r is the cap alone, so, by that code argument, every B2/B2-r generation ran to 60/100 tokens before segmentation. Two descriptive checks bear on it, and neither shows it token-exactly (the artifacts store no token ids). First (computed-new, from the committed `response_raw`): B2 responses are " + f"{b2_len[0]}-{b2_len[1]} characters ({b2_len[2]} responses, {b2_len[3]} files) and B2-r control/explore responses {b2r_len[0]}-{b2r_len[1]} ({b2r_len[2]} responses, {b2r_len[3]} files); none is under 60 characters, which is consistent with cap-length generations, not proof of them (characters are not tokens). " + (("Second, N2's cap-emulation diagnostics (its 2(d) table, N2 raw lines " + f"{diag['header_line']}-{max(r_['line'] for r_ in diag['rows'].values())}" + " at read), all four rows: 'cut at 60 shortens' " + "; ".join(f"{s_} {r_['cut60_shortens']}" for s_, r_ in diag['rows'].items()) + "; B2-r controls re-encoded past 100 tokens " + "; ".join(f"{s_} {r_['b2r_over_100']} (max {r_['b2r_max']})" for s_, r_ in diag['rows'].items()) + "; B2 texts re-encoded past 60 " + "; ".join(f"{s_} {r_['b2_over_60']} (max {r_['b2_max']})" for s_, r_ in diag['rows'].items()) + ". N2 itself calls a re-encoding longer than the cap impossible for exact ids (N2 raw line " + str(diag['impossible_for_exact_ids_line']) + "), so the re-encoding is approximate: only " + (", ".join(diag['stages_at_caps_exactly']) or "no stage") + " sits at the caps exactly, the other stages' maxima overshoot a cap by " + f"{min(diag['overshoot'])}-{max(diag['overshoot'])}" + " tokens, and the diagnostics bound the lengths only approximately. The earlier version of this sentence cited the base row alone (round-2 finding 2).") if diag and diag.get('rows') else "N2's 2(d) diagnostic table was not found at read.") + " This refines N2's cell; it changes no N2 figure. (d) Substance, banned tokens: N2's cell names the strings; the builder bans every token piece of every string, so on OLMo five of the nine banned ids are ordinary sub-word pieces, '>' among them (section 3). A refinement of N2's cell, not a disagreement in value.")
    emit()
    emit(f"N4 (`{N4_RAW}` section (iv) and `{N4_JSON}`).")
    emit()
    if n4_json:
        emit("| cell | N4 | this raw | agree |")
        emit("|---|---|---|---|")
        for p, (a, b, ok_) in xc["n4"]["e2b_round_path_cached_agree"].items():
            emit(f"| {p} round_path_cached | {a} | {b} | {ok_} |")
        for p, (a, b, ok_) in xc["n4"]["uncached_counts_agree"].items():
            emit(f"| {p} round_path_cached occurrences | {a} | {b} | {ok_} |")
        for p, (a, b) in xc["n4"]["g2_use_cached_agree"].items():
            emit(f"| {p} use_cached | {a} | {b} | {a == b} |")
        for p, (n4v, gen, ent, fld) in xc["n4"]["e2b_generated_rounds"].items():
            emit(f"| {p} generated rounds | {n4v} | {gen} generated (entries with n_tok); {ent} round+choice entries; artifact `n_rounds` {fld} | {n4v == gen} |")
        emit()
        bad_gen = [(p, v) for p, v in xc["n4"]["e2b_generated_rounds"].items() if v[0] != v[1]]
        for p, (n4v, gen, ent, fld) in bad_gen:
            x_ = EV["e2b"][p]
            n4s = xc["n4"].get("script") or {}
            bud = x_.get("budget") or {}
            rwr = x_.get("reads_without_round") or []
            _sa = find_line(x_["runner_commit"], x_["runner"], r'budget\["stop_at"\] = \{"session": idx \+ 1, "read": ci \+ 1\}')
            stop_match = bool(rwr) and len(rwr) == 1 and bud.get("stop_at") == {"session": rwr[0]["session"] + 1, "read": rwr[0]["read"]}
            emit(f"- **Disagreement with N4 (count, not path):** N4 gives `{p}` {n4v} generated rounds; the artifact has {ent} round+choice entries (its `n_rounds` = {fld}, computed as entries, {x_['runner']}@{x_['runner_commit']}:{find_line(x_['runner_commit'], x_['runner'], r'n_rounds = sum')[0]}) but {gen} generated rounds: {ent - gen} entry is a read with no generated round after it (replay: {x_['replay']['n_reads_without_round']} such read). "
                 f"Cause (round-2 finding 4): a counting definition, not a transcription. N4 counts round+choice entries (`{N4_SCRIPT}` at read, sha256 `{n4s.get('sha256_at_read')}`, line {n4s.get('ngen_formula_line')}: `{n4s.get('ngen_formula')}`), the artifact's `n_rounds` formula, which includes one budget-stop read with no generated round: the artifact's `budget` records stop_reason '{bud.get('stop_reason')}' at N = {bud.get('N')} of N_max {bud.get('N_max')}, stop_at {bud.get('stop_at')} (session and read both 1-based, {x_['runner']}@{x_['runner_commit']}:{_sa[0] if _sa else '?'}); the read without a round is " + "; ".join(f"session index {r_['session']}, read {r_['read']}, global read index {r_['global_read_index']}, session truncated_by_stop {r_['session_truncated_by_stop']}" for r_ in rwr) + f" (the same read as stop_at: {stop_match}). The status stays discrepant; N4's path statement is unaffected.")
    for k, v in xc["n4"]["md_statements"].items():
        emit(f"- N4 states '{k}': {'found' if v else 'NOT found'} in the N4 raw; this raw: " +
             {"e2a full run cached (log-only)": f"cached, log-only ({LOG['e2a_full_cached']}) -- agrees",
              "D1 uncached (log-only)": f"uncached, log-only ({LOG['d1_uncached']}) -- agrees",
              "f1 cached vanilla (log-only)": f"cached vanilla, log-only ({LOG['f_cached_proposal']}) -- agrees",
              "first g2 ladder uncached": "not re-derived here (superseded corpus; not a DV row) -- no disagreement",
              "TEMP 0.7 cited to clone e2a.py:48": f"same value; this raw adds the only committed statement of e2a's temperature, {AD['e2d_temp_comment']} -- agrees"}[k])
    emit("- N4 is Qwen-scoped and lists no OLMo cells; this raw adds B2, B2-r and B3, all uncached (B-phase disposition, " + LOG["b_phase_uncached"] + ").")
    emit()

    # ---------------- section 6: Figures for N1
    FIG = []

    def fig(f, v, src, st, note=""):
        FIG.append({"figure": f, "printed": v, "source": src, "status": st, "note": note})

    QWEN_GEN_EQ = all(x["adapter_generate_equal_pin"] for x in list(E["e2b"].values()) + list(e2d.values()) + list(E["fmt"].values()))
    # ---- e2a
    fig("e2a: temperature", "0.7", f"{AD['e2d_temp_comment']} (committed prose, a code comment written at {INTRO['e2d/config TEMP = 0.7'][0]}, {INTRO['e2d/config TEMP = 0.7'][1]}); clone {cl('jlens_qwen/e2a.py', r'^TEMP = 0\.7')}", "log-only",
        f"a later code comment ({INTRO['e2d/config TEMP = 0.7'][0]}, {INTRO['e2d/config TEMP = 0.7'][1]}; e2a data commit {E['e2a']['commit']}, {cdate(E['e2a']['commit'])}), not an e2a log entry; no e2a artifact field and no e2a-era log line states the value; the pre-registration says only 'temperature-sampled'; the PI decides whether the note prints e2a's T (section 7)")
    fig("e2a: top-p / top-k", "none", f"clone {cl('jlens_qwen/e2a.py', r'mx\.random\.categorical\(lg / temp\)')}", "not found", "clone only (outside the record); same sampler as the ported adapter")
    fig("e2a: max new tokens", "60", f"data/e2a/sessions.jsonl:rounds[].n_tok,cap_hit ({E['e2a']['cap']['cap_hits']} cap hits, all at 60); {LOG['e2a_amend_cap']}", "reproduced")
    fig("e2a: seed policy", "per-session Generator crc32(f'{arm}|{s}'); per-round seeds", f"data/e2a/sessions.jsonl:rounds[].seed,choices[].seed via valence_core/session_e2a.py@{PIN}", "reproduced", f"{E['e2a']['seed_streams_matched']}/200 streams")
    fig("e2a: stop discipline", "newline after content, cap 60", f"{LOG['e2a_amend_stop']}; {LOG['e2a_stop_refinement']}", "log-only",
        "the amendment gives the newline stop and the cap; the g2r incident's logged refinement gives 'after content' (leading pure-whitespace tokens consumed before the newline stop arms)")
    fig("e2a: EOS banned", f"yes ({' and '.join(eos_strings_in_file)} in the frozen list)", f"data/configs/e2a_ban_list.json@{PIN}:strings; {LOG['e2a_full_ban']}; {LOG['gport_eos_tokcfg']}", "log-only",
        "the run printed the file's sha16; the eos identity is the G-PORT raw's; recomputed on the local snapshot (computed-new row below)")
    fig("e2a: ban list", f"12 ids, sha16 {ban16}", f"{LOG['e2a_full_ban']}; {LOG['e2a_ban_frozen']}", "log-only", f"fixed by the v3 adjudication ({LOG['e2a_ban_adjudication']}); sessions.jsonl has no ban field; corroborated by data/e2a/g2_discriminability.json:ban_sha = sha256(data/configs/e2a_ban_list.json)[:16] (reproduced for the gate corpus)")
    fig("e2a: generation path", "cached", LOG["e2a_full_cached"], "log-only", "sessions.jsonl has no path field (N4 agrees); the raw's 'uncached path (g1)' banner is stale (" + LOG["e2a_stale_banner_cosmetic"] + ")")
    fig("e2a: commit(s) that fixed them", f"pre-reg {INTRO[PREREG_KEY][0]}; amendment {INTRO[AMEND_KEY][0]} (stop, cap); v3 adjudication {INTRO[BAN_KEY][0]} (ban); data {E['e2a']['commit']}; ban file admitted {ban_commit}",
        f"{LOG['e2a_prereg_sampled_cached']}; {LOG['e2a_amend_stop']}; {LOG['e2a_ban_adjudication']}", "computed-new",
        "introducing commits from git log -S over the log at bbc9ffe; the runner is the clone's (no record commit)")
    # ---- g2r2
    fig("g2r2 corpus: temperature", "0.7", f"clone {cl('scripts/e2a_g2_discriminability.py', r'sampled temp 0\.7')}", "not found", "clone only; the e2d config comment names e2a, not the g2 corpora")
    fig("g2r2 corpus: top-p / top-k", "none", "as e2a (clone)", "not found", "clone only")
    fig("g2r2 corpus: max new tokens", "60", f"{LOG['e2a_amend_cap']}; data/e2a/g2_rounds_f0.1.json:pos[],neg[].cap_hit ({g2r2['cap_hits']} of {g2r2['n_rounds']} flagged)", "log-only", "the rounds carry no n_tok")
    fig("g2r2 corpus: seed policy", "crc32(task|para|pole|frac) per round", "data/e2a/g2_rounds_f0.1.json:pos[].seed,neg[].seed", "reproduced", f"{g2r2['seed_formula_matches']}/{g2r2['n_rounds']}")
    fig("g2r2 corpus: stop discipline / EOS", "v3 template family: newline stop, cap 60, EOS banned", f"{LOG['e2a_amend_stop']}; {LOG['e2a_stop_refinement']}; {LOG['e2a_ban_adjudication']}; data/e2a/g2_discriminability.json:template_family = '{E['g2']['g2r2_template_family']}'", "log-only",
        f"the family's label is an artifact field (reproduced); its definition is log-only; {g2r2['texts_with_newline']} of {g2r2['n_rounds']} texts contain a newline")
    fig("g2r2 corpus: ban list", f"sha16 {ban16}", "data/e2a/g2_discriminability.json:ban_sha", "reproduced", f"log {LOG['g2r2_ban']}")
    fig("g2r2 corpus: generation path", "cached", "data/e2a/g2_discriminability.json:fracs.0.1.use_cached", "reproduced")
    fig("g2r2 corpus: commit(s) that fixed them", f"v3 family {INTRO[AMEND_KEY][0]} + {INTRO[BAN_KEY][0]}; data {g2r2['commit']}", f"{LOG['e2a_amend_stop']}; {LOG['e2a_ban_adjudication']}", "computed-new", "clone runner")
    # ---- S1
    fig("S1 judge: decoding", "none (logit-level 2AFC read, no generation)", "data/e2a/s1_judge_rescue.json:cells.*.rows[] (p_A, p_B, picked_pos; no text)", "reproduced",
        f"pick = (p_A >= p_B) on {E['s1']['pick_rule_consistent']}/{E['s1']['n_reads']}; rng declared at scripts/s1_judge_rescue.py@f526377:{E['s1']['rng_uses'][0]} and never used")
    fig("S1 judge: commit", "runner and data f526377", "git log over bbc9ffe (data/e2a/s1_judge_rescue.json)", "computed-new")
    # ---- f1
    fig("f1: temperature", "0.7", LOG["gport_f1_temp_cap"], "log-only")
    fig("f1: top-p / top-k", "none", LOG["gport_f1_sampling"], "log-only")
    fig("f1: max new tokens", "60", f"data/f/sessions.jsonl:rounds[].n_tok,cap_hit ({E['f1']['cap']['cap_hits']} cap hits, all at 60)", "reproduced")
    fig("f1: seed policy", "per-session Generator crc32(f'f|{arm}|{s}'); per-round seeds", "data/f/sessions.jsonl:rounds[].seed,choices[].menu_a + data/f/pools.json sizes", "reproduced", f"{E['f1']['seed_streams_match']}/344 streams; draw order from the clone")
    fig("f1: stop discipline", "newline after content, cap 60, EOS banned", f"{LOG['f_stop_ban_proposal_range']}; {LOG['e2a_stop_refinement']}; {LOG['gport_f1_stop']}; {LOG['gport_eos_banned']}", "log-only",
        f"PROPOSAL-f registers the v3 template family; the G-PORT line's 'every special token' is corrected at {LOG['gport_ban_correction']}")
    fig("f1: ban list", f"sha16 {ban16}", f"{LOG['f_stop_ban_proposal_range']}; {LOG['gport_f1_ban']}", "log-only", "sessions.jsonl has no ban field; data/f/calib.json:ban_sha records the same sha16 for the calibration run (reproduced there)")
    fig("f1: generation path", "cached, vanilla", f"{LOG['f_cached_proposal']}; {LOG['f_ndecl_cached']}", "log-only")
    fig("f1: commit(s) that fixed them", f"PROPOSAL-f {PF0}; v3 family {INTRO[AMEND_KEY][0]} + {INTRO[BAN_KEY][0]}; data {E['f1']['commit']}", f"{LOG['f_stop_ban_proposal_range']}; {LOG['f_cached_proposal']}", "computed-new", "clone runner")
    # ---- e2b
    for p, x in E["e2b"].items():
        nm = os.path.basename(p).replace("_sessions.json", "").replace(".json", "")
        fig(f"e2b {nm}: temperature", str(x["temp"]), f"{p}:temp", "reproduced")
        fig(f"e2b {nm}: max new tokens", "60", f"{p}:sessions[].rounds[].n_tok,cap_hit ({x['cap']['cap_hits']} cap hit(s), all at 60)", "reproduced" if x["cap"]["cap_hits"] else "not found",
            (f"STOP_CAP defined at {x['stop_cap_def']}" if x["cap"]["cap_hits"] else f"code-fixed {x['gen_line']}; no cap hit (max n_tok {x['cap']['max_n_tok']})"))
        fig(f"e2b {nm}: seed policy", "session_rng(key, idx) per-round seeds", f"{p}:sessions[].rounds[].seed", "reproduced", f"{rep(x['replay'])}")
        fig(f"e2b {nm}: stop discipline", "newline after content, cap 60, EOS banned", f"{x['adapter_stop_line']}; data/configs/e2a_ban_list.json@{PIN}:strings", "not found", "code-fixed (the adapter's rule and the frozen list); no artifact field")
        fig(f"e2b {nm}: generation path", "cached" if x["round_path_cached"] else "uncached", f"{p}:round_path_cached", "reproduced")
        fig(f"e2b {nm}: ban list", f"frozen file, sha16 {ban16}", x["ban_path_line"], "not found", "code-fixed; no artifact field")
        fig(f"e2b {nm}: commit(s) that fixed them", f"runner {x['runner_commit']}; TEMP introduced {INTRO[E2B_TEMP_INTRO[x['runner']]][0]}; data {x['data_commit']}", f"{x['runner']}@{x['runner_commit']}", "computed-new",
            "git history at bbc9ffe; H1-u's run commit is the first H1 run's (section 7)" if p.endswith("h1u_sessions.json")
            else ("git history at bbc9ffe; the run commit's message names the launch (section 7)" if x["runner_commit"] != x["data_commit"] else "git history at bbc9ffe"))
    # ---- e2d
    for tier, x in e2d.items():
        T_ = tier.upper()
        fig(f"e2d {T_}: temperature", str(x["temp"]), f"data/e2d/{tier}_sessions.json:temp", "reproduced")
        if x["stopcap_field"]:
            fig(f"e2d {T_}: max new tokens", "60", f"data/e2d/{tier}_sessions.json:tstep_licence.position_coverage_note ('STOP_CAP is 60')", "reproduced",
                f"no cap hit in {x['cap']['n']} rounds (max n_tok {x['cap']['max_n_tok']})")
        else:
            fig(f"e2d {T_}: max new tokens", "60", f"code {x['runner_lines']['gen']}, {x['stop_cap_line']}", "not found",
                f"code-fixed at the code commit {x['code_commit']}; no cap hit in {x['cap']['n']} rounds (max n_tok {x['cap']['max_n_tok']}), so the artifact bounds the cap but does not show it")
        fig(f"e2d {T_}: seed policy", "session_rng(f'e2d-{arm}', idx)", f"data/e2d/{tier}_sessions.json:sessions[].rounds[].seed", "reproduced", rep(x["replay"]))
        fig(f"e2d {T_}: stop (newline)", f"stop_reason {x['stop_reason']}", f"data/e2d/{tier}_sessions.json:sessions[].rounds[].stop_reason", "reproduced", "no 'eos' in the tally")
        fig(f"e2d {T_}: EOS banned", "yes", f"{x['adapter_stop_line']}; the rebuilt list (counts below)", "not found", "code-fixed; inferred, not an artifact field")
        fig(f"e2d {T_}: ban list (count)", f"{x['ban_list']['n_ids']} ids / {x['ban_list']['n_strings']} strings", f"data/e2d/{tier}_sessions.json:ban_list", "reproduced", "counts only; identity with the frozen file not shown")
        if x["round_path_cached"] == "absent":
            fig(f"e2d {T_}: generation path", "uncached", f"{LOG['d1_uncached']}; code {x['runner_lines']['path']}", "log-only", "no artifact field")
        else:
            fig(f"e2d {T_}: generation path", "cached" if x["round_path_cached"] else "uncached", f"data/e2d/{tier}_sessions.json:round_path_cached", "reproduced")
        if tier == "d1":
            fig("e2d D1: commit(s) that fixed them", f"pre-reg PROPOSAL-j {PJ_C} (v3 family held fixed); code {x['code_commit']}; data {x['data_commit']}", f"{LOG['d1_code_commit']}; {PJ['lines']}", "log-only",
                f"the record names the code commit; the data commit {x['data_commit']} changed the runner after the run (cached=False -> cached=cached, --round-path added), values unchanged; {PJ_C} is an ancestor of {x['code_commit']} and {x['data_commit']}: {PJ['ancestor_of'][x['code_commit']] and PJ['ancestor_of'][x['data_commit']]}")
        else:
            fig(f"e2d {T_}: commit(s) that fixed them", f"pre-reg PROPOSAL-j {PJ_C} (v3 family held fixed); code = data {x['data_commit']}", f"git log over bbc9ffe (data/e2d/{tier}_sessions.json); {PJ['lines']}", "computed-new",
                f"the data commit changes no runner file: {not x['data_commit_touched_runner_code']}; {PJ_C} is an ancestor of {x['data_commit']}: {PJ['ancestor_of'][x['data_commit']]}")
    # ---- B2
    fig("B2: temperature", "0.0 (greedy)", f"{LOG['b2_temp0']}; {E['b2r']['addendum_b2_greedy_line']}; code {E['b2']['lines']['gen']}", "log-only", "N2 agrees")
    fig("B2: max new tokens", "60", f"{LOG['b2_max60']}; code {E['b2']['lines']['max']}", "log-only", "N2 agrees")
    # round-2 finding 7: the compound seed row split into its two halves
    fig("B2: allocation seed", "20260823 (plan_trials permutation)", "data/olmo/b2_{fidelity,register}_*.json:trials[].trial,concept,injected via detection.plan_trials", "reproduced",
        f"{b2_alloc}/8 files replay with 20260823; plan_trials' own default seed {E['b2']['plan_trials_default_seed']} replays {b2_alloc_default}/8 (the replay discriminates); N2 has the seed log-only")
    fig("B2: generation seed", "20260823 + n per trial", E["b2"]["lines"]["gen"], "not found",
        f"code-fixed; not recorded in any B2 artifact; inert at T = 0 ({LOG['b2_seed_inert']})")
    fig("B2: ban list", "9 ids from 6 strings, 5 of them ordinary sub-word pieces", f"{E['b2']['lines']['ban']}; {OB['record_ids_locator']}; data/olmo/a2_baserates_*.json:ban_list", "not found",
        "code-fixed for B2 (no B2 field); the id set is reproduced from the A2/B3 sha16s (section 3)")
    fig("B2: generation path", "uncached", f"{LOG['b_phase_uncached']}; code {E['b2']['lines']['cached']}", "log-only")
    fig("B2: commit(s) that fixed them", f"runner built {E['b2']['runner_intro']}; data {E['b2']['data_commit']}", f"scripts/box_b2_detection.py@{E['b2']['runner_intro']}", "computed-new",
        "not pre-registered: LOCK-g names no decoding parameter (section 1)")
    # ---- B2-r
    fig("B2-r: temperature", b2r_temps, "data/olmo/b2r_*.json:temp", "reproduced", f"pre-registered {E['b2r']['addendum_decoding_lines']}; N2 agrees")
    fig("B2-r: max new tokens", b2r_max, "data/olmo/b2r_*.json:max_tokens", "reproduced", f"pre-registered {E['b2r']['addendum_decoding_lines']}; N2 agrees")
    fig("B2-r: seed policy", "20260824 + trial n (control, explore); qualify formula", "data/olmo/b2r_*.json:trials[].seed, control.rows[].seed, injected.*.rows[].seed", "reproduced", f"'per-trial seeds are live and declared', {E['b2r']['addendum_decoding_lines']}; N2 agrees")
    fig("B2-r: ban list", "as B2 (the same 9 ids)", f"{E['b2r']['lines']['ban']}", "not found", "code-fixed; no B2-r field")
    fig("B2-r: generation path", "uncached", f"{LOG['b_phase_uncached']}; code {E['b2r']['lines']['cached']}", "log-only")
    fig("B2-r: commit(s) that fixed them", f"ADDENDUM-g3-b2r-v1.2 {E['b2r']['addendum_commit']}; runner {INTRO['box_b2r TEMP = 1.0'][0]}; stamped head {E['b2r']['stamped_head']}; data {E['b2r']['data_commit']}",
        f"{E['b2r']['addendum_decoding_lines']}; {E['b2r']['stamped_head_line']}", "log-only", f"the addendum's commit precedes the runner's: {E['b2r']['addendum_before_runner_intro']}")
    fig("B2/B2-r: top-p / top-k", "none (full softmax; argmax at T = 0)", AD["olmo_pick"], "not found", f"code-fixed; the B2-r addendum names every decoding parameter and no top-p/top-k ({E['b2r']['addendum_names_all_line']}); N2 agrees")
    fig("B2/B2-r: stop", "cap only (stop_newline=False; EOS banned)", f"{E['b2']['lines']['stop']}; {E['b2r']['lines']['stop']}; {AD['ban_builder_special']}; data/olmo/a2_baserates_*.json:ban_list.strings", "not found",
        f"code-fixed; code argument; refines N2's 'EOS token or the cap'; consistent (computed-new, not token-exact): response_raw {b2_len[0]}-{b2_len[1]} chars (B2, n {b2_len[2]}), {b2r_len[0]}-{b2r_len[1]} (B2-r control/explore, n {b2r_len[2]}), none under 60 (section 5 (c))")
    # ---- B3
    fig("B3: temperature", "0.7", f"{LOG['b3_temp07']}; code {E['b3']['lines']['temp']}", "log-only", "no artifact field")
    fig("B3: top-p / top-k", "none (full softmax at T)", AD["olmo_pick"], "not found", "code-fixed")
    fig("B3: max new tokens", "60", f"data/olmo/b3_screen_*.json:sessions[].rounds[].n_tok,cap_hit ({b3_cap['cap_hits']} cap hits, all at 60)", "reproduced" if b3_cap["cap_hits"] else "log-only")
    fig("B3: seed policy", "session_rng(f'b3-{arm}', idx); stage-independent", "data/olmo/b3_screen_*.json:sessions[].rounds[].seed", "reproduced", f"{b3_rep} streams; {b3pairs} pairs equal against base, {b3all} over all six stage pairs")
    fig("B3: stop discipline", "newline after content, cap 60, EOS banned", f"{AD['olmo_stop_default']}; {AD['olmo_stop_rule']}", "not found", "code-fixed (adapter default and rule); consistent: cap_hit iff n_tok = 60")
    fig("B3: ban list", f"9 ids, sha16 {OB['sha16_sorted_ids_convention']}; 5 ordinary sub-word pieces", f"data/olmo/b3_screen_*.json:ban_list; {OB['record_ids_locator']}", "reproduced",
        f"the count and sha16 are artifact fields; the ids are the record's (log-only) and hash to the stored sha16 ({OB['b3_convention_matches_all_stages']})")
    fig("B3: generation path", "uncached", f"{LOG['b_phase_uncached']}; code {E['b3']['lines']['cached_default']}", "log-only")
    fig("B3: commit(s) that fixed them", f"TEMP introduced {INTRO['box_b3 TEMP = 0.7'][0]}; data {E['b3']['data_commit']}", f"scripts/box_b3_sessions.py@{INTRO['box_b3 TEMP = 0.7'][0]}", "computed-new", "git history at bbc9ffe")
    # ---- k1 / format
    for label, x in (("k1", k1), ("format F0", F0), ("format F1", F1), ("format F2", F2)):
        A_ = x["artifact"]
        fig(f"{label}: temperature", str(x["temp_top"]), f"{A_}:temp, identity.temp", "reproduced")
        if x["cap"]["cap_hits"]:
            fig(f"{label}: max new tokens", "60", f"{A_}:sessions[].rounds[].n_tok,cap_hit ({x['cap']['cap_hits']} cap hit(s), all at 60)", "reproduced")
        else:
            fig(f"{label}: max new tokens", "60", f"code {x['runner_lines']['gen']}, {x['stop_cap_line']}", "not found",
                f"code-fixed; no cap hit in {x['cap']['n']} rounds (max n_tok {x['cap']['max_n_tok']})")
        fig(f"{label}: seed policy", "session_rng(" + ", ".join(f"'{k_}'" for k_ in x["rng_keys"]) + ", idx)", f"{A_}:sessions[].rounds[].seed", "reproduced", rep(x["replay"]))
        fig(f"{label}: stop (newline / cap)", f"stop_reason {x['stop_reason']}", f"{A_}:sessions[].rounds[].stop_reason", "reproduced", "no 'eos' in the tally")
        fig(f"{label}: EOS banned", "yes", f"{x['adapter_stop_line']}; {x['ban_line']}", "not found", "code-fixed; inferred, not an artifact field")
        if x["ban_list"] != "absent":
            fig(f"{label}: ban list (count)", f"{x['ban_list']['n_ids']} ids / {x['ban_list']['n_strings']} strings", f"{A_}:ban_list", "reproduced", "counts only; identity with the frozen file not shown")
        else:
            fig(f"{label}: ban list", "rebuilt from the live tokenizer", x["ban_line"], "not found", "code-fixed; no artifact field")
        fig(f"{label}: generation path", "uncached", f"{A_}:sessions[].rounds[].round_path_cached", "reproduced")
        fig(f"{label}: commit(s) that fixed them", f"code = data {x['data_commit']}", f"git log over bbc9ffe ({A_})", "computed-new", f"the data commit changes no runner file: {not x['data_commit_touched_runner_code']}")
    # ---- cross-family
    fig("Qwen session families: top-p / top-k", "none (full-vocabulary categorical at T)", AD["qwen_sample"], "not found",
        f"code-fixed for e2b/e2d/k1/format (generate() source at every code commit identical to bbc9ffe's: {QWEN_GEN_EQ}); f1 is log-only via the G-PORT raw")
    fig("Qwen: EOS id in the ban list", f"{qe.get('eos_token')} -> {qe.get('eos_id')}: {qe.get('eos_id_in_ban_ids')}", "local snapshot tokenizer_config.json + tokenizer.json (outside the record) vs data/configs/e2a_ban_list.json:ids", "computed-new", f"the record: {LOG['gport_eos_tokcfg']}")
    fig("Qwen vendor generation_config (not used)", f"T {gc.get('temperature')}, top_k {gc.get('top_k')}, top_p {gc.get('top_p')}", "local snapshot generation_config.json (outside the record)", "computed-new", "no runner reads it")
    fig("OLMo: the two stored ban sha16s", f"B3 {OB['sha16_sorted_ids_convention']} (sorted ids); A2 {OB['sha16_ids_strings_convention']} ({{ids, strings}})",
        f"data/olmo/b3_screen_*.json:ban_list.sha16; data/olmo/a2_baserates_*.json:ban_list.sha16; {OB['b3_sha_line']}; {OB['a2_sha_line']}", "reproduced",
        f"both recomputed from the record's nine ids ({OB['record_ids_locator']}); B3 match {OB['b3_convention_matches_all_stages']}, A2 match {OB['a2_convention_matches_all_stages']}")
    fig("OLMo: banned sub-word pieces", olmo_sub, f"{OB['record_ids_locator']}", "log-only",
        f"piece names corroborated on a local base tokenizer.json that is not the run's file (computed-new: {OBL.get('pieces_agree_with_record')}; equal to the manifest's base file: {OBL.get('tokenizer_json_sha256_equals_manifest_base')})")
    xdis = []
    for p_, (n4v, gen, ent, fld) in (xc["n4"].get("e2b_generated_rounds") or {}).items():
        if n4v != gen:
            xdis.append(f"N4 gives {p_} {n4v} generated rounds; generated (n_tok) {gen}, entries {ent} (section 5)")
            FIG.append({"figure": f"N4 cross-check: {os.path.basename(p_)} generated rounds", "printed": f"{gen} generated; {ent} entries",
                        "source": f"{p_}:sessions[].rounds[],choices[] (n_tok present) vs n_rounds", "status": "discrepant",
                        "note": f"N4 raw states {n4v}; cause: N4 counts round+choice entries, the artifact's n_rounds formula, which includes one budget-stop read with no generated round (a counting definition, not a transcription; section 5)"})
    for r_ in xc["n2"]["rows"]:
        if not (r_["n2_b2r_cell_has"] and r_["n2_b2_cell_has"]):
            xdis.append(f"N2 1(c) row '{r_['param']}' does not carry the value this raw finds")
    J["cross_check_disagreements"] = xdis
    J["figures"] = FIG

    emit("## 6. Figures (for N1's claims ledger)")
    emit()
    emit("The block writes no numerals for N16; 'figure' below is '<DV>: <parameter>'.")
    emit()
    emit("| figure (as the block writes it) | value printed | source (artifact:field or pinned locator) | status | note |")
    emit("|---|---|---|---|---|")
    for f in FIG:
        emit(md_row((f["figure"], f["printed"], f["source"], f["status"], f["note"])))
    emit()

    # ---------------- section 7: STOPs, discrepancies, referent notes, PI
    stops = []
    disc = []
    for p, x in list(E["e2b"].items()):
        if x["replay"]["seed_streams_match"] != x["replay"]["n_sessions"]:
            disc.append(f"{p}: seed replay {rep(x['replay'])} (first mismatches {x['replay']['first_mismatches']})")
    for t, x in e2d.items():
        if x["replay"]["seed_streams_match"] != x["replay"]["n_sessions"]:
            disc.append(f"e2d {t}: seed replay {rep(x['replay'])}")
    for p, x in E["fmt"].items():
        if x["replay"]["seed_streams_match"] != x["replay"]["n_sessions"]:
            disc.append(f"{p}: seed replay {rep(x['replay'])}")
    for p, x in b3f.items():
        if x["replay"]["seed_streams_match"] != x["replay"]["n_sessions"]:
            disc.append(f"{p}: seed replay {rep(x['replay'])}")
    if E["f1"]["seed_streams_match"] != E["f1"]["n_sessions"]:
        disc.append(f"f1 seed replay {E['f1']['seed_streams_match']}/{E['f1']['n_sessions']} (first {E['f1']['first_mismatches']})")
    if E["e2a"]["seed_streams_matched"] != E["e2a"]["n_sessions"]:
        disc.append(f"e2a seed replay {E['e2a']['seed_streams_matched']}/{E['e2a']['n_sessions']}")
    caps_bad = [k for k, c in [("e2a", E["e2a"]["cap"]), ("f1", E["f1"]["cap"])] +
                [(p, x["cap"]) for p, x in E["e2b"].items()] + [(t, x["cap"]) for t, x in e2d.items()] +
                [(p, x["cap"]) for p, x in E["fmt"].items()] + [(p, x["cap"]) for p, x in b3f.items()]
                if not c["all_consistent"]]
    if caps_bad:
        disc.append(f"cap_hit vs n_tok inconsistent in: {caps_bad}")
    J["figures"] = FIG
    J["stops"] = stops
    J["discrepancies"] = disc
    emit("## 7. STOPs, discrepancies, referent notes, items for the PI")
    emit()
    emit("**STOPs:** none. N16 is Tier 2: no fail text; nothing here needs an analyzer change.")
    emit()
    emit("**Discrepancies (replays and consistency checks):** " + ("none: every seed stream, allocation and cap check above reproduced." if not disc else "; ".join(disc)))
    emit()
    emit("**Cross-check disagreements with sibling raws:** " + ("none." if not xdis else "; ".join(xdis) + (". It does not change a decoding value" if len(xdis) == 1 else ". None of them changes a decoding value") + "; the N2 stop-rule and banned-token refinements (section 5 (c), (d)) are refinements, not disagreements in value."))
    emit()
    notes = [
        "The block's N16 asks for 'max tokens'; for the session families that value is STOP_CAP, a backstop under a newline stop, not a generation length. For B2/B2-r (no newline stop, EOS banned) it is the generation length.",
        f"'S1 judge' generates no text. Its decoding row is 'none': a deterministic logit read. The texts it judges are the g2r2 corpus (cached, T 0.7, per-round crc32 seeds), which this raw tabulates as its own row. The runner declares rng = default_rng(20260820) (scripts/s1_judge_rescue.py@f526377:{E['s1']['rng_uses'][0]}) and never draws from it.",
        "The k1 / format-recon rows are included because the block's N3(i) cites PROPOSAL-k Stage 1 figures and k1 runs through the format-recon runner; the note itself could not be checked (preflight :15).",
        "Echo-probe recon stages A-C (N3) generate nothing: scripts/recon_echo.py@bbc9ffe:4 re-forwards archived e2a sessions, so the e2a row covers their text.",
        f"`data/e2a/g2_rounds_f0.2_v2.json` is not a DV and is not tabulated: it is consistent with the first g2 ladder's dose-0.20 corpus, generated before the template amendment (the first g2 entry, archive/RESULTS-cycles3-4.md@bbc9ffe:1204, precedes the amendment at :1043; results/raw/2026-08-09_e2a_g2.txt prints a 0.2 generation, g2r and g2r2 print only 0.1). Its texts run past newlines ({E['g2']['rounds']['data/e2a/g2_rounds_f0.2_v2.json']['texts_with_newline']}/128) and {E['g2']['rounds']['data/e2a/g2_rounds_f0.2_v2.json']['texts_with_think']}/128 contain a `<think>` string, and its rows carry no cap_hit field: consistent with the pre-amendment decoding, which had no newline stop and a 90-token cap ({LOG['e2a_v1_cap90']}, log-only; clone {cl('jlens_qwen/e2a.py', r'^MAX_TOKENS = 90')}); whether a scaffold ban was in force for it is not settled here. Listed so that a reader of data/e2a does not mistake it for the readability corpus of record; its seeds still follow the per-round crc32 formula ({E['g2']['rounds']['data/e2a/g2_rounds_f0.2_v2.json']['seed_formula_matches']}/128).",
        f"The S1 runner changed after its run at 47ef4c7 ({cdate('47ef4c7')}): only the TASKS path moved from the clone into the record; its read code is cited at the run commit f526377.",
        f"H1-u's data is the first H1 run (data/e2b/h1_sessions.json@b2d051b, relabelled at 6df2072); its runner of record is scripts/e2b_h1_sessions.py@b2d051b, which steered forced rounds (:188) and generated free-phase rounds with no injection (:250), the defect the 6df2072 message names. Decoding is the same as H1's. H1's runner is cited at 6df2072, whose commit subject ends '" + git("log", "-1", "--format=%s", "6df2072").strip().split("; ")[-1] + "' (git log); H1's data commit " + E["e2b"]["data/e2b/h1_sessions.json"]["data_commit"] + " changes no runner file (" + str(not E["e2b"]["data/e2b/h1_sessions.json"]["data_commit_touched_runner_code"]) + ") and no runner file changed between the two (" + str(not E["e2b"]["data/e2b/h1_sessions.json"]["runner_changed_between_run_and_data_commit"]) + ").",
        f"e2d D1's code is cited at {D1_CODE}, not at its data commit {e2d['d1']['data_commit']}: the record says 'Module + analyzer committed BEFORE the run at `{D1_CODE}`; D1 ran that code' ({LOG['d1_code_commit']}), and {e2d['d1']['data_commit']} changed the runner after the run ({', '.join(e2d['d1']['data_commit_touched_runner_code'])}; commits touching D1's code between the two: {e2d['d1']['runner_changed_between_code_and_data_commit']}). At {D1_CODE} the round call hard-codes `cached=False` ({e2d['d1']['runner_lines']['path']}); at {e2d['d1']['data_commit']} it is `cached=cached` ({e2d['d1']['d1_data_commit_cached_line']}) and the runner writes `round_path_cached` ({e2d['d1']['round_path_field_writer_at_data_commit']}), a field D1's artifact lacks; the runner at {D1_CODE} has no `round_path_cached` line ({e2d['d1']['round_path_field_writer_at_code_commit'] is None}). Values (T 0.7, cap 60, uncached, the ban builder) are the same at both commits.",
    ]
    J["referent_notes"] = notes
    emit("**Referent notes:**")
    for n in notes:
        emit(f"- {n}")
    emit()
    pi = [
        "Code-fixed parameters. The block's status vocabulary has no slot for a value fixed by committed code at the run's commit when no artifact field or log line states it. This raw marks those 'not found (code-fixed)' with file:line@commit, as the N2 raw does (its row 10), so that N1 does not cut them: top-p/top-k 'none' for every Qwen valence_core family and all three OLMo campaigns; the e2b, B2, B2-r and k1 ban lists; B2's per-trial generation seed (inert at T = 0); the 60-token cap where no round reached it (e2d D1, k1, format F1/F2); the e2b and B3 stop rule; the EOS ban for e2b, e2d, k1 and format; the B2/B2-r 'cap is the only reachable stop'. A decision is needed on how N1 treats them.",
        f"OLMo's ban list suppresses five ordinary sub-word tokens in every OLMo round generation (B2, B2-r, B3, all four stages): {olmo_sub}. `<think>`/`</think>` are not added tokens in OLMo's vocabulary, and the builder bans every piece of every string. The record already says so ({OB['record_five_locator']}); this raw reproduces the nine-id set from the two stored sha16s (section 3). Banning '>' (id 29) is the one most likely to matter to a reader, since it is a common piece. No DV was re-examined for it here. The decoding paragraph should state it, and whether it needs any further look is the design seat's call.",
        f"Pre-registration of decoding: B2-r's temperature, max tokens and seeds were pre-registered (ADDENDUM-g3-b2r-v1.2 section 0.5, {E['b2r']['addendum_commit']}); B2's greedy decoding was not (LOCK-g names no decoding parameter) and was diagnosed afterwards ({LOG['b2_temp0']}); the Qwen families' stop rule, cap and ban were fixed in the log before their data (e2a amendment {INTRO[AMEND_KEY][0]}, v3 adjudication {INTRO[BAN_KEY][0]}), and for f1 and e2d also pre-registered by reference to the v3 family (PROPOSAL-f {PF0}, {LOG['f_stop_ban_proposal_range']}; PROPOSAL-j {PJ_C}, {PJ['lines']}, before e2d's code and data: {PJ['precedes_every_e2d_code_and_data_commit']}), no tracked PROPOSAL-/LOCK-/ADDENDUM- document governing them states a temperature (section 2's search), and e2a's log pre-registration says only 'temperature-sampled'. Log entries other than those cited here were not searched for pre-data temperature statements.",
        f"e2a's temperature (0.7) is in no e2a artifact and no e2a-era log line. The record states it only in a code comment written three weeks later ({AD['e2d_temp_comment']}, introduced {INTRO['e2d/config TEMP = 0.7'][0]}) and in the gitignored clone. If the note prints e2a's temperature, the README should say where it comes from. The same holds for the g2r2 corpus's temperature. e2a's status here stays log-only (committed prose), but N1's ledger should carry this raw's note with it ('a later code comment, not an e2a log entry', section 6), so that 'log-only' is not read as a contemporaneous e2a log entry; whether the note prints e2a's T is the PI's call.",
        "EOS is banned in every Qwen and OLMo generation (Qwen: recorded in the G-PORT raw and recomputed here from the local snapshot; OLMo: code argument plus the recorded ban strings). One consequence belongs in the decoding paragraph: by that code argument, B2 and B2-r generations always ran to their caps (60 / 100 tokens) and were then segmented at turn markers (consistent, not shown token-exactly: the stored responses' lengths, section 5 (c)).",
        "Seed pairing by construction (e2d across doses, B3 across stages, B2-r explore vs control, B2-r qualify across concepts) is not a defect, but a reader comparing doses or stages should be told the comparisons are seed-paired.",
    ]
    J["pi_items"] = pi
    emit("**Items for the PI / design seat:**")
    for p in pi:
        emit(f"- {p}")
    emit()

    # ---------------- appendix: evidence digests
    emit("## Appendix: evidence digests (all computed by this script)")
    emit()
    emit(f"- e2a: {json.dumps({k: v for k, v in E['e2a'].items() if k not in ('row_fields_present',)})}")
    emit(f"- g2 corpora: {json.dumps(E['g2'])}")
    emit(f"- S1: {json.dumps(E['s1'])}")
    emit(f"- f1: {json.dumps({k: v for k, v in E['f1'].items()})}")
    for p, x in E["e2b"].items():
        emit(f"- {p}: {json.dumps({k: v for k, v in x.items()})}")
    for t, x in e2d.items():
        emit(f"- e2d {t}: {json.dumps(x)}")
    emit(f"- e2d shared seeds: {json.dumps(E['e2d_shared_seeds'])}")
    for p, x in E["fmt"].items():
        emit(f"- {p}: {json.dumps(x)}")
    emit(f"- B2: {json.dumps(E['b2'])}")
    emit(f"- B2-r: {json.dumps(E['b2r'])}")
    emit(f"- B3: {json.dumps(E['b3'])}")
    emit(f"- local Qwen snapshot (outside the record): {json.dumps({k: v for k, v in qe.items() if k != 'ban_strings_to_ids_local'})}")
    emit(f"- OLMo ban list (record ids, both sha16 conventions, local base tokenizer outside the record): {json.dumps(E['b3']['olmo_ban'], default=str)}")
    emit(f"- LOCK-g decoding search: {json.dumps(E['b2']['lock_g'])}")
    emit(f"- pre-registration documents mentioning a temperature (line counts): {json.dumps(PREREG_TEMP)}")
    emit(f"- STOP_CAP introducing commit with and without --follow: {json.dumps(STOPCAP_FOLLOW)}")
    emit()

    # ---------------- values-check (fixer pass): every checker finding and its disposition
    d1x = e2d["d1"]
    VC = [
        ("1 (substantive) e2a/g2r2/f1 ban fixed by 8fa0b75, not only 6e49242",
         "fixed",
         f"Confirmed by tool run: git log -S'ROUND GENERATION ONLY' over RESULTS.md + archive gives {INTRO[BAN_KEY][0]} ({INTRO[BAN_KEY][1]}); the adjudication text is {LOG['e2a_ban_adjudication']}; the frozen list is logged before the full run at {LOG['e2a_ban_frozen']}; PROPOSAL-f registers the v3 family at {LOG['f_stop_ban_proposal_range']}. Now cited in the e2a, g2r2 and f1 rows (ban, stop, commit cells), in section 2 (new rows and reading) and in section 6 (commit rows). 6e49242 stays, labelled as the later admission of the file."),
        ("2 (substantive) B2-r decoding pre-registered in ADDENDUM-g3-b2r-v1.2 section 0.5 (f14d249)",
         "fixed",
         f"Confirmed: {E['b2r']['addendum_decoding_lines']}; the addendum's first commit is {E['b2r']['addendum_commit']} ({E['b2r']['addendum_commit_date']}); it is an ancestor of the runner commit {INTRO['box_b2r TEMP = 1.0'][0]}: {E['b2r']['addendum_before_runner_intro']}. Added to the B2-r temperature, max-token, seed, top-p/top-k and commit cells, to section 2 and to section 6. The addendum's 'ours ran 0.0' ({E['b2r']['addendum_b2_greedy_line']}) now sits beside RESULTS.md's line for B2's temperature."),
        ("3 (substantive) e2d D1 cited at its data commit db5b09c; the record says D1 ran 4e41288",
         "fixed",
         f"Confirmed: {LOG['d1_code_commit']}; {d1x['data_commit']} changed {', '.join(d1x['data_commit_touched_runner_code'])}. D1's temperature, cap, seed, ban and path lines are now at {D1_CODE} ({d1x['runner_lines']['temp']}, {d1x['runner_lines']['gen']}, {d1x['runner_lines']['rng']}, {d1x['runner_lines']['ban']}, {d1x['runner_lines']['path']}); adapter generate() at {D1_CODE} equal to bbc9ffe's: {d1x['adapter_generate_equal_pin']}. The commit cell names both commits. The same check over every other DV's data commit (vocabulary paragraph) finds only H1-u's relabel commit, already cited at its run commit."),
        ("4 (substantive) g2r2 temperature labelled log-only in section 1 but not found in section 6",
         "fixed",
         f"Both tables now say not found (clone only), tier K. No artifact field (keys of g2_discriminability.json: {G2_KEYS}; of a g2r2 round: {G2_ROW_KEYS}) and no log line: a search for a 0.7 temperature (regex /{G2_TEMP_SEARCH['regex']}/i) over archive/RESULTS-cycles3-4.md and the {len(G2_TEMP_SEARCH['files']) - 1} results/raw/2026-08-01..12 e2a raws at bbc9ffe (listed in the JSON) finds {G2_TEMP_SEARCH['hits']} hit(s){(': ' + str(G2_TEMP_SEARCH['hit_lines'])) if G2_TEMP_SEARCH['hits'] else ''}. The e2d config comment names e2a, not the g2 corpora. If the PI accepts that comment as covering the g2 corpora, both cells change together."),
        ("5 (minor) unescaped '|' in section 6 cells",
         "fixed",
         "Every table row is now written by one helper that escapes '|' (sections 1, 2 and 6); the column-count check at the end of this section runs over the whole file."),
        ("6 (minor) k1/format section 6 sources name no artifact; seed key printed as a Python list",
         "fixed",
         "Each source is now prefixed with its artifact path (data/k/k1_sessions.json, data/format/format_recon_F{0,1,2}_sessions.json), and keys print as strings ('k1-F2', 'fmt-F0', ...)."),
        ("7 (minor) section 6 lacks rows for some main-table cells and has no commit rows",
         "fixed",
         "Added: e2a EOS; g2r2 top-p/top-k, max, stop/EOS, ban, commit; S1 commit; f1 commit; e2b stop and commit (x4); e2d EOS, ban (count) and commit (x3); B2 ban and commit; B2-r ban and commit; B3 top-p/top-k, stop, commit; k1/format EOS, ban and commit; the OLMo sha16 and sub-word rows. Commit rows are computed-new (git history) except where the record names the commit (D1, B2-r: log-only)."),
        ("8 (minor) B3 cross-stage seed equality: domain unstated",
         "fixed",
         f"Now '{E['b3']['same_arm_session_seeds_equal_across_stages']} same-(arm, idx) pairs, each non-base stage against base; {E['b3']['same_arm_session_seeds_equal_all_stage_pairs']} over all six stage pairs' ({E['b3']['keys_present_at_all_four_stages']} keys at all four stages), computed here, in section 1, section 4 and section 6. The checker's 546/546 reproduces."),
        ("9 (minor) B3 stop default cited at olmo_hf.py:293",
         "fixed",
         f"The default is the signature, {AD['olmo_stop_default']}; the rule is {AD['olmo_stop_rule']}."),
        ("10 (minor) OLMo: 6 strings -> 9 ids implies banned sub-word pieces; the two sha16 conventions differ",
         "fixed, with one part rejected",
         f"Applied: both omissions are real and are now stated (section 1 B2/B2-r/B3 ban cells, section 3, section 6, a PI item). Rejected: 'a decoding fact the record cannot resolve'. The record lists the ids ({OB['record_ids_locator']}) and says five of nine are sub-word pieces ({OB['record_five_locator']}). This pass reproduces the id set from the artifacts: sha256(json.dumps(sorted ids))[:16] = {OB['sha16_sorted_ids_convention']}, equal to B3's stored sha16 at all four stages ({OB['b3_convention_matches_all_stages']}), and sha256(json.dumps({{ids, strings}}, sort_keys=True))[:16] = {OB['sha16_ids_strings_convention']}, equal to A2's at all four stages ({OB['a2_convention_matches_all_stages']}). So the two sha16s are one id set under two conventions. The A2 convention is cited at A2's data commit ({OB['a2_sha_line']}) rather than at bbc9ffe."),
        ("11 (minor) e2a 'EOS banned' cited to G-PORT :1671, which is about f1's and m's runners",
         "fixed",
         f"e2a's EOS ban now cites the frozen file's strings ({' and '.join(eos_strings_in_file)} in data/configs/e2a_ban_list.json), the run's sha16 ({LOG['e2a_full_ban']}) and the eos identity ({LOG['gport_eos_tokcfg']}); :1671 is kept for f1 with its correction ({LOG['gport_ban_correction']})."),
        ("12 (minor) e2d stop cells 'EOS banned [reproduced]' and ban cells '12 ids [reproduced]' overclaim",
         "fixed",
         "The e2d stop cells now read 'newline [reproduced: stop_reason tally, no eos]; EOS banned [not found as a field: code-fixed, the adapter's rule with the EOS id in the ban list]', and the ban cells 'reproduced (count only)', noting the artifact stores {n_ids, n_strings} and does not show identity with the frozen file. Section 6 splits the same way (stop (newline), EOS banned, ban list (count))."),
        ("13 (minor) section 2 STOP_CAP introducing commit needs --follow",
         "fixed",
         f"Both forms computed: --follow gives {STOPCAP_FOLLOW['follow']} (file then `{STOPCAP_FOLLOW['path_at_follow_hit']}`); without it, {STOPCAP_FOLLOW['no_follow']} (the rename). The row's note says so."),
        ("self-found A: e2b's STOP_CAP module and a misleading appendix field",
         "fixed",
         "At all four e2b run commits STOP_CAP is defined in valence_core/e2b/session.py (" + "; ".join(x['stop_cap_def'] for x in E['e2b'].values()) + "); valence_core/session_e2a.py exists at none of them (" + str([x['session_e2a_py_exists_at_run_commit'] for x in E['e2b'].values()]) + "), so the earlier appendix field `session_e2a_blob_equal_pin` = false only reflected the file not existing yet. The field is replaced by `stop_cap_def`, and the e2b cap cells cite the definition."),
        ("self-found B: finding 12's overclaim in the k1/format and g2r2 rows",
         "fixed",
         "The k1 and format stop and ban cells had the same overclaim as e2d's and are split the same way. The g2r2 stop cell, which said 'reproduced in part' on the strength of zero newlines, is now log-only (the v3 family's definition) with the artifact's template_family = 'v3' as the reproduced part. The tier column marks split cells X+Y."),
        ("self-found C: section 2 header said 'committer-local' dates",
         "fixed",
         "The dates are git author dates (%ad, --date=short); the header says so."),
        ("self-found D: B2's decoding and pre-registration",
         "added",
         f"LOCK-g names no decoding parameter (no temperature, max-token or top-p/top-k string: {not E['b2']['lock_g']['decoding_terms']}; its only 'greedy' is the roster search, {E['b2']['lock_g']['greedy_lines']}). Stated in the B2 commit cell and a PI item."),
    ]
    J["values_check"] = [{"finding": f_, "disposition": d_, "detail": t_} for f_, d_, t_ in VC]
    emit("## Values-check (fixer pass over the checker's findings)")
    emit()
    emit("Each finding was checked with a tool run before it was applied; every value below is printed by this script. The checker's independent recomputations, as received (20 complete rows; the list was cut off at a 21st, on introducing commits), all agreed with this raw and are not repeated here.")
    emit()
    emit("| finding | disposition | detail |")
    emit("|---|---|---|")
    for f_, d_, t_ in VC:
        emit(md_row((f_, d_, t_)))
    emit()

    # ---------------- values-check, round 2 (residual findings)
    # finding 1: replay the old reading method (subprocess text mode) to show the cause
    OLD = {}
    for key_, path_, pat_ in (("e2a_full_ban", "results/raw/2026-08-09_e2a_full.txt", r"ban list 12 ids sha 9a2f0744f81ac930"),
                              ("g2r2_ban", "results/raw/2026-08-09_e2a_g2r2.txt", r"ban 12 ids sha 9a2f0744f81ac930"),
                              ("g2r2_cached", "results/raw/2026-08-09_e2a_g2r2.txt", r"cached=True")):
        t_old = subprocess.run(["git", "show", f"{PIN}:{path_}"], cwd=REPO, capture_output=True, text=True).stdout
        OLD[key_] = {"text_mode_splitlines": next(i for i, l in enumerate(t_old.splitlines(), 1) if re.search(pat_, l)),
                     "text_mode_split_newline": next(i for i, l in enumerate(t_old.split("\n"), 1) if re.search(pat_, l)),
                     "bytes_split_newline (now)": log_line(show(path_), pat_)}
    SEP_FILES = sorted(k for k, v in SHOWN.items() if v)
    SEP_CLONE = sorted(k for k, v in clone.items() if any(c in "\n".join(v["lines"]) for c in SPLITLINES_ONLY))
    SEP_SIB = sorted(nm_ for nm_, t_ in ((N2_RAW, n2_text), (N4_RAW, n4_text)) if any(c in t_ for c in SPLITLINES_ONLY))
    _sofar = "\n".join(OUT_LINES)
    SEP_WITH_LOC = [k for k in SEP_FILES if re.search(re.escape(k) + r":\d", _sofar)]
    SEP_SEARCH_ONLY = [k for k in SEP_FILES if k not in SEP_WITH_LOC]
    _srch = set(f"{f_}@{PIN}" for f_ in G2_TEMP_SEARCH["files"])
    J["round2_line_numbering"] = {"old_method_replay": OLD, "record_files_read": len(SHOWN),
                                  "record_files_with_splitlines_only_separators": {k: SHOWN[k] for k in SEP_FILES},
                                  "clone_files_with_splitlines_only_separators": SEP_CLONE,
                                  "sibling_raws_with_splitlines_only_separators": SEP_SIB,
                                  "separator_files_carrying_a_locator": SEP_WITH_LOC,
                                  "separator_files_read_only_by_the_temperature_search": SEP_SEARCH_ONLY}
    rows4 = (diag or {}).get("rows") or {}
    h1p = "data/e2b/h1_sessions.json"
    h1x = EV["e2b"][h1p]
    n4s_ = xc["n4"].get("script") or {}
    VC2 = [
        ("R2-1 (minor) three log locators off by two: e2a_full.txt :7, e2a_g2r2.txt :5 and :8",
         "fixed",
         f"Confirmed, with the cause one step earlier than the finding's. git() ran git in subprocess text mode, whose universal-newline translation turns the bare '\\r' of tqdm's 'Fetching 14 files' line into line breaks before any split, so split('\\n') alone does not fix it: replaying the old read gives, per locator (text-mode splitlines / text-mode split('\\n') / bytes split('\\n'), now): {json.dumps(OLD)}. Fixed both halves: git() decodes stdout bytes, every emitted line number comes from one helper, lines_of() (split on '\\n' only, as sed numbers lines), and the N2/N4 sibling reads are byte-exact. Now {LOG['e2a_full_ban']}, {LOG['g2r2_ban']} and {LOG['g2r2_cached']}, the finding's expected values. Of the {len(SHOWN)} record files this script reads, {len(SEP_FILES)} contain a splitlines-only separator (each a bare '\\r': {all(SHOWN[k] == [repr(chr(13))] for k in SEP_FILES)}); of those, the ones this raw cites by line are {SEP_WITH_LOC}; the other {len(SEP_SEARCH_ONLY)} ({', '.join(k.split('@')[0].rsplit('/', 1)[-1] for k in SEP_SEARCH_ONLY)}) are read only by the e2a-era temperature search (all in its file list: {set(SEP_SEARCH_ONLY) <= _srch}), which finds {G2_TEMP_SEARCH['hits']} hit(s) and so emits no line number into them. Clone files with one: {SEP_CLONE or 'none'}; sibling raws (N2, N4) with one: {SEP_SIB or 'none'}. So no other locator in this raw moves. The cited text: '{lines_of(show('results/raw/2026-08-09_e2a_full.txt'))[int(LOG['e2a_full_ban'].rsplit(':', 1)[1]) - 1][:60]}...' and '{lines_of(show('results/raw/2026-08-09_e2a_g2r2.txt'))[int(LOG['g2r2_ban'].rsplit(':', 1)[1]) - 1][:50]}...'. The other two locators in these files are before the progress line and unchanged ({LOG['e2a_full_cached']}, {LOG['e2a_full_stale_banner']}). The corrected locators reach every cell that carries them: the section-1 e2a stop and ban cells and g2r2 ban and path cells, the section-3 Qwen bullet, the section-6 rows 'e2a: EOS banned', 'e2a: ban list' and 'g2r2 corpus: ban list', and round 1's row 11 above."),
        ("R2-2 (minor) section 5(c) cited N2's 2(d) base row only",
         "fixed (both forms the fix offers)",
         (f"Confirmed from the N2 raw at read: rows at lines {', '.join(str(r_['line']) for r_ in rows4.values())}; B2-r over 100: " + "; ".join(f"{s_} {r_['b2r_over_100']} (max {r_['b2r_max']})" for s_, r_ in rows4.items()) + "; B2 over 60: " + "; ".join(f"{s_} {r_['b2_over_60']} (max {r_['b2_max']})" for s_, r_ in rows4.items()) + "; 'cut at 60 shortens' " + "; ".join(f"{s_} {r_['cut60_shortens']}" for s_, r_ in rows4.items()) + f"; N2 calls an over-cap re-encoding impossible for exact ids at line {(diag or {}).get('impossible_for_exact_ids_line')}. Section 5(c) now cites all four rows with that caveat, and adds the computed-new response lengths from the committed `response_raw`: B2 {b2_len[0]}-{b2_len[1]} characters ({b2_len[2]} responses, {b2_len[3]} files), B2-r control/explore {b2r_len[0]}-{b2r_len[1]} ({b2r_len[2]} responses, {b2r_len[3]} files), none under 60. Per file (B2): " + "; ".join(f"{os.path.basename(p_)} {v_['resp_len_chars']}" for p_, v_ in b2files.items()) + "; (B2-r): " + "; ".join(f"{os.path.basename(p_)} {v_['resp_len_chars']}" for p_, v_ in b2r.items() if 'resp_len_chars' in v_) + ". The code argument (every B2/B2-r generation ran to its cap) is unchanged; the sentence no longer suggests the diagnostics show it exactly.")),
        ("R2-3 (minor) e2d's governing pre-registration (PROPOSAL-j) not cited",
         "fixed",
         f"Confirmed: {PJ['lines']} holds 'template family v3 with its bans, stop discipline, and audit patterns' fixed; git log -S 'Held fixed, by design' gives {PJ_C} ({PJ['date']}; the file's first commit {PJ['first_commit_of_file']}); ancestor of {json.dumps(PJ['ancestor_of'])}; temperature lines in PROPOSAL-j: {PJ['temperature_mentions']}. Added '{PJ_CITE}' to the D1/D2/D3 commit cells (section 1) and commit rows (section 6), a section-2 row, and PROPOSAL-j beside PROPOSAL-f in the section-2 reading and the PI pre-registration item. 'B2-r is the one DV whose temperature and max-token values were pre-registered' stays (PROPOSAL-f and PROPOSAL-j state no temperature); the reading now says f1's and e2d's cap and stop discipline were pre-registered by reference."),
        ("R2-4 (minor) N4 cross-check cause labelled 'transcription'",
         "fixed (status stays discrepant)",
         f"Confirmed: N4's script counts entries (`{N4_SCRIPT}` at read, sha256 {n4s_.get('sha256_at_read')}, line {n4s_.get('ngen_formula_line')}: `{n4s_.get('ngen_formula')}`; the finding's :1569 was an earlier state of that untracked sibling, so the line is located by pattern at read), the same formula as the artifact's n_rounds ({h1x['runner']}@{h1x['runner_commit']}:{find_line(h1x['runner_commit'], h1x['runner'], r'n_rounds = sum')[0]}). Recount: {h1x['n_entries']} entries, {h1x['n_generated']} with n_tok; the one read without a round is {h1x['reads_without_round']}, the leakage budget's stop ({h1x['budget']}); seed replay {rep(h1x['replay'])} sessions, {h1x['replay']['n_seeds_checked']} seeds. Section 5 and the section-6 row now give the cause as a counting definition."),
        ("R2-5 (minor) e2a temperature 'log-only' rests on a later code comment",
         "disclosed (no status change, as the fix says)",
         f"Confirmed: the only committed statement is {AD['e2d_temp_comment']}, introduced {INTRO['e2d/config TEMP = 0.7'][0]} ({INTRO['e2d/config TEMP = 0.7'][1]}); e2a's data commit {E['e2a']['commit']} is {cdate(E['e2a']['commit'])}; this script's search for a 0.7 temperature over archive/RESULTS-cycles3-4.md and the {len(G2_TEMP_SEARCH['files']) - 1} e2a-era raws finds {G2_TEMP_SEARCH['hits']} hit(s); the pre-registration says only 'temperature-sampled' ({LOG['e2a_prereg_sampled_cached']}). The section-1 cell and the section-6 note now read 'a later code comment, not an e2a log entry', so N1 can carry it in its note column. N1's ledger is another item's file and is not edited here; the PI item says N1 should carry the note and that whether the note prints e2a's T is the PI's call."),
        ("R2-6 (minor) e2a stop cell's locator covers only part of the printed rule",
         "fixed",
         f"Confirmed: {LOG['e2a_amend_stop']} (the amendment: newline stop, cap 60); the 'after content' half is {LOG['e2a_stop_refinement']} (the g2r incident entry, logged at {REFINE['commit']}, {REFINE['date']}). Added to the e2a, g2r2 and f1 stop cells (section 1) and stop rows (section 6), and as a section-2 row."),
        ("R2-7 (minor) B2 seed row: one 'reproduced' status covers two halves",
         "fixed",
         f"Confirmed: plan_trials with 20260823 replays {b2_alloc}/8 files' allocation and plan_trials' own default {E['b2']['plan_trials_default_seed']} replays {b2_alloc_default}/8; the per-trial generation seed is in no artifact and is code-fixed ({E['b2']['lines']['gen']}), inert at T = 0 ({LOG['b2_seed_inert']}). Section 6 now has 'B2: allocation seed' (reproduced) and 'B2: generation seed' (not found, code-fixed); the section-1 cell carries both statuses (tier A+C), and the code-fixed PI item lists the generation seed."),
        ("R2-8 (minor) e2a seed cell: 'integers(4) per round' can be read as interleaved",
         "fixed",
         f"Confirmed: {DRAW['order_lines']} and {DRAW['sequence_lines']} draw all {_np} paraphrase indices (2F + N_FREE, F = {_F}, N_FREE = {DRAW['N_FREE']}; {DRAW['n_rounds_line']}) right after the permutation and before any seed; the module warns that interleaving collapses the replay to 4/200 ({DRAW['interleave_warning_line']}). The cell is reworded to that order; the replay itself was already in that order and still matches {E['e2a']['seed_streams_matched']}/{E['e2a']['n_sessions']}."),
    ]
    J["values_check_round2"] = [{"finding": f_, "disposition": d_, "detail": t_} for f_, d_, t_ in VC2]
    emit("### Round 2 (residual findings, applied in this order: R2-1, the one that moves locators, first)")
    emit()
    emit("Each finding was re-checked with a tool run before it was applied; every value below is printed by this script.")
    emit()
    emit("| finding | disposition | detail |")
    emit("|---|---|---|")
    for f_, d_, t_ in VC2:
        emit(md_row((f_, d_, t_)))
    emit()
    # column-count check over every markdown table in the file (finding 5)
    bad_rows, n_rows = [], 0
    hdr = None
    for i_, line in enumerate(OUT_LINES):
        if re.fullmatch(r"\|(-{3}\|)+", line):
            hdr = len(re.split(r"(?<!\\)\|", OUT_LINES[i_ - 1])) - 2
            continue
        if hdr is not None and line.startswith("|"):
            n_rows += 1
            nc = len(re.split(r"(?<!\\)\|", line)) - 2
            if nc != hdr:
                bad_rows.append((i_ + 1, nc, hdr))
        elif not line.startswith("|"):
            hdr = None
    J["table_column_check"] = {"rows_checked": n_rows, "mismatches": bad_rows}
    emit(f"Table column-count check (run last, over every markdown table above): {n_rows} rows checked, {len(bad_rows)} with a column count different from their header's" + (f": {bad_rows}" if bad_rows else "") + ".")
    emit()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        fh.write("\n".join(OUT_LINES) + "\n")
    with open(args.json_out, "w") as fh:
        json.dump(J, fh, indent=1, default=str)
    print(f"wrote {args.out} ({len(OUT_LINES)} lines) and {args.json_out}")
    print(f"discrepancies: {len(disc)}; stops: {len(stops)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
