#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N14 -- the three label-artifact captures
("what the shields caught"), recomputed from committed artifacts.

READ-ONLY on the record. Every artifact and every record text is read through
`git show bbc9ffe:<path>` (the pin), never through the working tree; the
record's habit module (valence_core/e2d/habit.py) is executed from its pinned
blob, not imported from the working tree. The only files written are --out
and --json-out. No model, no inference; stdlib arithmetic (math.comb,
fractions.Fraction) for every statistic and exact test.

Captures (block lines 115-116):
  1. e2a (Qwen): sham arm map A / map B beside the state (reward) arm's maps.
  2. f1 (Qwen): CORR contrast map A / map B.
  3. B3 DPO (OLMo): marker arm, one map +0.1667 beside the other map.

Round-2 values-check additions (post-hoc, descriptive): per-pair reads of every
capture arm, maple/cedar across the ten Qwen arms, maps with maple/cedar
removed, the H3 tag screen (data/e2b/h3_tagscreen.json) recomputed from its
per-probe rows, and a check of f1 CORR's delivered text against
data/f/pools.json (the N5 cross-reference); all read at the pin.

Usage (from the repository root):
  jlens-qwen36/.venv/bin/python scripts/audit_note_N14.py \
      [--out results/raw/2026-10-08_note-N14-artifacts.md] \
      [--json-out results/raw/2026-10-08_note-N14-artifacts.json]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import types
from fractions import Fraction

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "bbc9ffe"
BLOCK = "AUDIT-note-release-v1_2.md"
ROUTED_BLOCK = ("8cd8a9ac", "3841")
ITEM_LINES = (115, 116)
DEFAULT_OUT = "results/raw/2026-10-08_note-N14-artifacts.md"
DEFAULT_JSON = "results/raw/2026-10-08_note-N14-artifacts.json"
OLMO_STAGES = ("base", "sft", "dpo", "instruct")


# --------------------------------------------------------------------------
# record access (pinned)
# --------------------------------------------------------------------------
def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True,
                          text=True, check=True).stdout


def show(path: str) -> str:
    return git("show", f"{PIN}:{path}")


def jsonl(text: str) -> list[dict]:
    return [json.loads(l) for l in text.splitlines() if l.strip()]


_LINES: dict[str, list[str]] = {}


def pinned_lines(path: str) -> list[str]:
    if path not in _LINES:
        _LINES[path] = show(path).split("\n")
    return _LINES[path]


def find_lines(path: str, needle: str) -> list[int]:
    """1-based line numbers (in `git show PIN:path`) containing needle."""
    return [i + 1 for i, l in enumerate(pinned_lines(path)) if needle in l]


def one_line(path: str, needle: str) -> int:
    hits = find_lines(path, needle)
    if len(hits) != 1:
        raise SystemExit(f"N14 anchor error: {needle!r} in {path}@{PIN} "
                         f"matched {len(hits)} lines {hits}")
    return hits[0]


def quote(path: str, a: int, b: int) -> list[str]:
    ls = pinned_lines(path)
    return [f"{path}@{PIN}:{i}: {ls[i - 1].rstrip()}" for i in range(a, b + 1)]


def local_lines(path: str) -> list[str]:
    with open(os.path.join(REPO, path), encoding="utf-8") as f:
        return f.read().split("\n")


def local_find(path: str, needle: str) -> int:
    ls = local_lines(path)
    hits = [i + 1 for i, l in enumerate(ls) if needle in l]
    if len(hits) != 1:
        raise SystemExit(f"N14 anchor error (local): {needle!r} in {path} "
                         f"matched {len(hits)}")
    return hits[0]


def local_quote(path: str, a: int, b: int) -> list[str]:
    ls = local_lines(path)
    return [f"{path}:{i}: {ls[i - 1].rstrip()}" for i in range(a, b + 1)]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(path: str) -> str:
    with open(os.path.join(REPO, path), "rb") as f:
        return sha256_bytes(f.read())


def blob_equal_to_pin(path: str) -> str:
    """Working-tree blob id vs the pin's blob id (informational)."""
    try:
        pinned = git("rev-parse", f"{PIN}:{path}").strip()
    except subprocess.CalledProcessError:
        return "not at pin"
    p = os.path.join(REPO, path)
    if not os.path.exists(p):
        return "absent from working tree"
    with open(p, "rb") as f:
        data = f.read()
    wt = hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()
    return "EQUAL to pin" if wt == pinned else "DIFFERS from pin"


# --------------------------------------------------------------------------
# exact statistics (stdlib)
# --------------------------------------------------------------------------
def binom_upper(k: int, n: int) -> Fraction:
    """P(X >= k | n, 1/2), exact."""
    return Fraction(sum(math.comb(n, i) for i in range(k, n + 1)), 2 ** n)


def binom_two_sided(k: int, n: int) -> Fraction:
    """Exact two-sided binomial test vs 1/2: sum of P(i) <= P(k)."""
    pk = math.comb(n, k)
    return Fraction(sum(math.comb(n, i) for i in range(n + 1)
                        if math.comb(n, i) <= pk), 2 ** n)


def fisher_two_sided(a: int, b: int, c: int, d: int) -> float:
    """Fisher exact, two-sided (sum of tables with P <= P_obs), for the 2x2
    [[a, b], [c, d]] with fixed margins."""
    r1, r2, c1 = a + b, c + d, a + c
    n = r1 + r2

    def p(x: int) -> Fraction:
        return Fraction(math.comb(r1, x) * math.comb(r2, c1 - x),
                        math.comb(n, c1))
    lo, hi = max(0, c1 - r2), min(r1, c1)
    p_obs = p(a)
    tol = p_obs * Fraction(1, 10 ** 7)
    return float(sum(p(x) for x in range(lo, hi + 1) if p(x) <= p_obs + tol))


def d4(x) -> str:
    return f"{float(x):+.4f}"


def frac_delta(k: int, n: int) -> Fraction:
    return Fraction(k, n) - Fraction(1, 2)


# --------------------------------------------------------------------------
# normalised per-session records
# --------------------------------------------------------------------------
def norm_e2a(rows: list[dict]) -> list[dict]:
    out = []
    for r in rows:
        assert r["tag_plus"] == (r["pair"][1] if r["swap"] else r["pair"][0])
        forced = [x for x in r["rounds"]
                  if str(x.get("phase", "")).startswith("forced")]
        ch = r.get("choices") or []
        fp = ch[0]["picked_pole"] if ch else None
        valid = (not r["excluded"]) and r["first_free_pick_pos"] is not None
        if valid:
            assert r["first_free_pick_pos"] == (fp == "pos")
        out.append({
            "campaign": "e2a", "arm": r["arm"], "session": r["session"],
            "map": "B" if r["swap"] else "A", "pair": list(r["pair"]),
            "plus_tag": r["tag_plus"], "valid": valid,
            "first_plus": r["first_free_pick_pos"] if valid else None,
            "pick": ch[0]["pick"] if ch else None,
            "menu_a": ch[0]["menu_a"] if ch else None,
            "start_tag": forced[0]["tag"] if forced else None,
            "start_plus_sched": bool(r["start_plus"]),
            "forced_poles": [x["pole"] for x in forced],
            "first_pick_pole": fp,
            "habit_rec": {"rounds": [{"phase": "forced", "pole": x["pole"]}
                                     for x in forced],
                          "choices": [{"picked_pole": fp}] if fp else []},
        })
    return out


def norm_f1(rows: list[dict]) -> tuple[list[dict], dict]:
    out, checks = [], {"forced_order_ok": 0, "first_free_round_cfg_ok": 0,
                       "valid_checked": 0}
    for r in rows:
        tag_p = r["tag_P"]
        assert tag_p == (r["pair"][1] if r["swap"] else r["pair"][0])
        order = (["P", "Q"] if r["start_P"] else ["Q", "P"]) * 2
        forced = r["rounds"][:4]
        ch = r.get("choices") or []
        valid = (not r["excluded"]) and r["first_free_pick_P"] is not None
        fp = (("pos" if ch[0]["picked_cfg"] == "P" else "neg")
              if ch else None)
        if valid:
            checks["valid_checked"] += 1
            assert r["first_free_pick_P"] == (ch[0]["picked_cfg"] == "P")
            # forced phase = 2 rounds per config, alternating from start
            # (f_sessions.py F_FORCED = 2), and the 5th round is the round
            # the first free choice bought.
            if [x["cfg"] for x in forced] == order:
                checks["forced_order_ok"] += 1
            if len(r["rounds"]) > 4 and r["rounds"][4]["cfg"] == ch[0]["picked_cfg"]:
                checks["first_free_round_cfg_ok"] += 1
        out.append({
            "campaign": "f1", "arm": r["arm"], "session": r["session"],
            "map": "B" if r["swap"] else "A", "pair": list(r["pair"]),
            "plus_tag": tag_p, "valid": valid,
            "first_plus": r["first_free_pick_P"] if valid else None,
            "pick": ch[0]["pick"] if ch else None,
            "menu_a": ch[0]["menu_a"] if ch else None,
            "start_tag": forced[0]["tag"] if forced else None,
            "start_plus_sched": bool(r["start_P"]),
            "forced_poles": ["pos" if x["cfg"] == "P" else "neg"
                             for x in forced],
            "first_pick_pole": fp,
            "habit_rec": {"rounds": [{"phase": "forced",
                                      "pole": "pos" if x["cfg"] == "P" else "neg"}
                                     for x in forced],
                          "choices": [{"picked_pole": fp}] if fp else []},
        })
    return out, checks


def norm_olmo(art: dict, stage: str) -> tuple[list[dict], dict]:
    out = []
    parity = {"checked": 0, "start_pos_iff_even_index": 0}
    for s in art["sessions"]:
        cell = s["cell"]
        assert cell["tag_plus"] == cell["pair"][cell["map"]]
        forced = [x for x in s["rounds"] if x["phase"] == "forced"]
        ch = s.get("choices") or []
        fp = ch[0]["picked_pole"] if ch else None
        valid = (not s["excluded"]) and s["first_free_pole"] is not None
        if valid:
            assert s["first_free_pole"] == fp
        if forced:
            parity["checked"] += 1
            if (forced[0]["pole"] == "pos") == (s["session"] % 2 == 0):
                parity["start_pos_iff_even_index"] += 1
        out.append({
            "campaign": f"B3-{stage}", "arm": s["arm"], "session": s["session"],
            "map": str(cell["map"]), "pair": list(cell["pair"]),
            "plus_tag": cell["tag_plus"], "valid": valid,
            "first_plus": (s["first_free_pole"] == "pos") if valid else None,
            "pick": ch[0]["pick"] if ch else None,
            "menu_a": ch[0]["menu_a"] if ch else None,
            "start_tag": forced[0]["tag"] if forced else None,
            "start_plus_sched": s["session"] % 2 == 0,
            "forced_poles": [x["pole"] for x in forced],
            "first_pick_pole": fp,
            "habit_rec": {"rounds": [{"phase": "forced", "pole": x["pole"]}
                                     for x in forced],
                          "choices": [{"picked_pole": fp}] if fp else []},
        })
    return out, parity


def map_counts(recs: list[dict], arm: str, m: str) -> tuple[int, int]:
    sub = [r for r in recs if r["arm"] == arm and r["valid"] and r["map"] == m]
    return sum(1 for r in sub if r["first_plus"]), len(sub)


def pooled_counts(recs: list[dict], arm: str) -> tuple[int, int]:
    sub = [r for r in recs if r["arm"] == arm and r["valid"]]
    return sum(1 for r in sub if r["first_plus"]), len(sub)


def decompose(recs: list[dict], arm: str, m: str | None, habit) -> dict:
    """Exact post-hoc identity for one map (or pooled if m is None):
    Delta = (n_fe_neg/N - 1/2) + (B_plus - B_minus)/N, where fe = the last
    forced round's pole, n_fe_neg = sessions whose habit (complement of the
    last forced pole) leads to the +label, B_plus = habit breaks that picked
    +, B_minus = habit breaks that picked -."""
    sub = [r for r in recs if r["arm"] == arm and r["valid"]
           and (m is None or r["map"] == m)]
    for r in sub:
        fpo = r["forced_poles"]
        alt = {"pos": "neg", "neg": "pos"}
        assert len(fpo) == 4 and fpo == [fpo[0], alt[fpo[0]], fpo[0], alt[fpo[0]]], r["session"]
        assert r["start_plus_sched"] == (r["start_tag"] == r["plus_tag"]), r["session"]
    N = len(sub)
    fe_neg = sum(1 for r in sub if r["forced_poles"][-1] == "neg")
    fe_pos = N - fe_neg
    b_plus = sum(1 for r in sub if r["forced_poles"][-1] == "pos"
                 and r["first_pick_pole"] == "pos")
    b_minus = sum(1 for r in sub if r["forced_poles"][-1] == "neg"
                  and r["first_pick_pole"] == "neg")
    k = sum(1 for r in sub if r["first_plus"])
    start_is_plus = sum(1 for r in sub if r["start_tag"] == r["plus_tag"])
    comp_fe = Fraction(fe_neg, N) - Fraction(1, 2)
    comp_br = Fraction(b_plus - b_minus, N)
    delta = frac_delta(k, N)
    assert comp_fe + comp_br == delta, (arm, m)
    assert start_is_plus == fe_neg  # F = 2 alternating: start = complement of end
    br = habit.break_rates([r["habit_rec"] for r in sub])
    hw = br["delta_first_weighted_form"]
    breaks_to_pair0 = sum(1 for r in sub
                          if ((r["forced_poles"][-1] == "pos") == (r["first_pick_pole"] == "pos"))
                          and r["pick"] == r["pair"][0])
    breaks_to_pair1 = sum(1 for r in sub
                          if ((r["forced_poles"][-1] == "pos") == (r["first_pick_pole"] == "pos"))
                          and r["pick"] == r["pair"][1])
    follows = sum(1 for r in sub if r["pick"] == r["start_tag"])
    return {"N": N, "k_plus": k, "delta": float(delta),
            "start_is_plus": start_is_plus, "forced_end_neg": fe_neg,
            "forced_end_pos": fe_pos, "breaks_to_plus": b_plus,
            "breaks_to_minus": b_minus,
            "component_forced_end_balance": float(comp_fe),
            "component_net_breaks": float(comp_br),
            "habit_weighted_form": hw,
            "habit_weighted_matches": (hw is not None
                                       and abs(hw - float(delta)) < 1e-12),
            "habit_b_plus": br["b_plus"], "habit_b_sham": br["b_sham"],
            "follows_habit": follows,
            "breaks_to_pair0": breaks_to_pair0,
            "breaks_to_pair1": breaks_to_pair1}


# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--json-out", default=DEFAULT_JSON)
    args = ap.parse_args()

    stamp = subprocess.run(["date", "-u"], capture_output=True, text=True,
                           check=True).stdout.strip()
    head = git("rev-parse", "HEAD").strip()
    pin_full = git("rev-parse", PIN).strip()
    block_bytes = subprocess.run(["git", "show", f"{PIN}:{BLOCK}"], cwd=REPO,
                                 capture_output=True, check=True).stdout
    block_sha = sha256_bytes(block_bytes)
    block_n = block_bytes.decode().count("\n")
    block_ok = block_sha.startswith(ROUTED_BLOCK[0]) and block_sha.endswith(ROUTED_BLOCK[1])
    script_rel = os.path.relpath(os.path.abspath(__file__), REPO)
    script_sha = sha256_file(script_rel)
    cmd = " ".join([sys.executable] + sys.argv)
    item_text = pinned_lines(BLOCK)[ITEM_LINES[0] - 1:ITEM_LINES[1]]

    # habit module from its pinned blob
    habit_src = show("valence_core/e2d/habit.py")
    habit = types.ModuleType("habit_pinned_bbc9ffe")
    exec(compile(habit_src, f"valence_core/e2d/habit.py@{PIN}", "exec"),
         habit.__dict__)

    # ---------------- artifacts ----------------
    paths = {
        "e2a_sessions": "data/e2a/sessions.jsonl",
        "e2a_analysis": "data/e2a/analysis.json",
        "f1_sessions": "data/f/sessions.jsonl",
        "f1_analysis": "data/f/screen_analysis.json",
    }
    for st in OLMO_STAGES:
        paths[f"b3_screen_{st}"] = f"data/olmo/b3_screen_{st}.json"
        paths[f"b3_analysis_{st}"] = f"data/olmo/b3_analysis_{st}.json"
    # round-2 values-check additions: the H3 tag screen on Qwen (finding 1)
    # and f1's pools (the N5 cross-reference, finding 5)
    paths["h3_tagscreen"] = "data/e2b/h3_tagscreen.json"
    paths["f1_pools"] = "data/f/pools.json"
    raw = {k: show(p) for k, p in paths.items()}
    art_sha = {p: sha256_bytes(raw[k].encode()) for k, p in paths.items()}
    art_wt = {p: blob_equal_to_pin(p) for p in paths.values()}
    art_wt["valence_core/e2d/habit.py"] = blob_equal_to_pin("valence_core/e2d/habit.py")

    _f1_rows = jsonl(raw["f1_sessions"])
    _e2a_rows = jsonl(raw["e2a_sessions"])
    e2a_excl = {}
    for _r in _e2a_rows:
        _d = e2a_excl.setdefault(_r["arm"], [0, 0])
        _d[0] += int(bool(_r["excluded"]))
        _d[1] += 1
    e2a = norm_e2a(_e2a_rows)
    e2a_an = json.loads(raw["e2a_analysis"])
    f1, f1_checks = norm_f1(_f1_rows)
    f1_an = json.loads(raw["f1_analysis"])
    olmo, olmo_an, olmo_parity = {}, {}, {}
    for st in OLMO_STAGES:
        olmo[st], olmo_parity[st] = norm_olmo(json.loads(raw[f"b3_screen_{st}"]), st)
        olmo_an[st] = json.loads(raw[f"b3_analysis_{st}"])
    _b3dpo = json.loads(raw["b3_screen_dpo"])
    b3_targets = _b3dpo["targets"]
    b3_per_stratum = _b3dpo["per_stratum"]
    b3_n_strata = len(_b3dpo["strata"])

    J: dict = {"item": "N14", "pin": pin_full, "head_at_run": head,
               "stamp_date_u": stamp, "block_sha256": block_sha,
               "script": script_rel, "script_sha256": script_sha,
               "command": cmd + "  (run from the repository root)",
               "interpreter": sys.executable,
               "python": platform.python_version(),
               "artifacts_sha256_at_pin": art_sha,
               "artifacts_worktree_vs_pin": art_wt}
    figures: list[dict] = []

    def fig(figure, value, source, status, note=""):
        figures.append({"figure": figure, "value": value, "source": source,
                        "status": status, "note": note})

    # ---------------- capture cells ----------------
    cells = []

    def cell(capture, model, campaign, arm, role, m, recs, stored, stored_src,
             map_def, plus_def):
        k, n = map_counts(recs, arm, m)
        d = frac_delta(k, n)
        if stored is None:
            match, status = "n/a (not stored)", "computed-new"
        elif isinstance(stored, dict):
            match = ("YES" if (stored["k"] == k and stored["n"] == n
                               and abs(stored["delta"] - float(d)) < 1e-12)
                     else "NO")
            status = "reproduced" if match == "YES" else "discrepant"
        else:
            match = "YES" if round(float(d), 4) == stored else "NO"
            status = "reproduced" if match == "YES" else "discrepant"
        c = {"capture": capture, "model": model, "campaign": campaign,
             "arm": arm, "role": role, "map": m, "k": k, "n": n,
             "delta": float(d), "delta_exact": str(d),
             "stored": stored, "stored_src": stored_src, "match": match,
             "status": status, "map_def": map_def, "plus_def": plus_def}
        cells.append(c)
        return c

    E2A_MAP = ("A = swap False (tag_plus = pair[0]); B = swap True (tag_plus = "
               "pair[1]); swap = (s // 4) % 2")
    F1_MAP = ("A = swap False (tag_P = pair[0]); B = swap True (tag_P = "
              "pair[1]); swap = (s // 4) % 2")
    B3_MAP = ("0: tag_plus = pair[0]; 1: tag_plus = pair[1] (strata = 4 roster "
              "pairs x 2 maps)")

    # 1. e2a
    for m in ("A", "B"):
        cell(1, "Qwen3.6-27B (MLX 4-bit)", "e2a", "sham", "capture (sham arm)",
             m, e2a, e2a_an["sham"]["by_map"][m],
             f"data/e2a/analysis.json:sham.by_map.{m}", E2A_MAP,
             "designated label, no state (sham)")
    for m in ("A", "B"):
        cell(1, "Qwen3.6-27B (MLX 4-bit)", "e2a", "reward",
             "beside (state arm)", m, e2a, e2a_an["reward"]["by_map"][m],
             f"data/e2a/analysis.json:reward.by_map.{m}", E2A_MAP,
             "label whose forced rounds carried +alpha on the reward axis "
             "(L48, frac 0.10)")
    # 2. f1 CORR
    for m in ("A", "B"):
        cell(2, "Qwen3.6-27B (MLX 4-bit)", "f1", "CORR",
             "capture (contrast arm)", m, f1,
             f1_an["contrasts"]["CORR"]["by_map"][m],
             f"data/f/screen_analysis.json:contrasts.CORR.by_map.{m}", F1_MAP,
             "P = clean-text config (target: avoid corrupted); Q = seeded "
             "character corruption")
    for m in ("A", "B"):
        cell(2, "Qwen3.6-27B (MLX 4-bit)", "f1", "sham", "beside (sham arm)",
             m, f1, None, "recomputed from data/f/sessions.jsonl (no stored "
             "by-map field for sham)", F1_MAP,
             "P = designated config; property-identical (sham)")
    # 3. OLMo DPO
    an = olmo_an["dpo"]
    for m in ("1", "0"):
        cell(3, "OLMo-3.1-32B-Instruct-DPO (bf16)", "B3-dpo", "marker",
             "capture (marker arm)" if m == "1" else "beside (other map)", m,
             olmo["dpo"], an["by_label_map"][m],
             f"data/olmo/b3_analysis_dpo.json:by_label_map.{m}", B3_MAP,
             "label whose forced rounds carried +alpha on span_reward (L44, "
             "frac 0.05 at DPO)")
    for arm in ("sham", "random"):
        for m in ("0", "1"):
            cell(3, "OLMo-3.1-32B-Instruct-DPO (bf16)", "B3-dpo", arm,
                 f"beside ({arm} arm)", m, olmo["dpo"], None,
                 "recomputed from data/olmo/b3_screen_dpo.json (by-map not "
                 "stored for controls)", B3_MAP,
                 "designated label, no state (sham)" if arm == "sham" else
                 "label whose forced rounds carried +alpha on a norm-matched "
                 "random direction")

    # pooled per arm, vs stored
    pooled = []

    def pool(capture, campaign, arm, recs, stored_d, stored_src, absval=False):
        k, n = pooled_counts(recs, arm)
        d = frac_delta(k, n)
        pooled.append({"capture": capture, "campaign": campaign, "arm": arm,
                       "k": k, "n": n, "delta": float(d),
                       "stored": stored_d, "stored_src": stored_src,
                       "stored_is_abs": absval, "match": None})

    pool(1, "e2a", "reward", e2a, e2a_an["reward"]["delta_first"],
         "data/e2a/analysis.json:reward.delta_first")
    pool(1, "e2a", "sham", e2a, e2a_an["sham"]["delta_first"],
         "data/e2a/analysis.json:sham.delta_first")
    pool(2, "f1", "CORR", f1, f1_an["contrasts"]["CORR"]["delta"],
         "data/f/screen_analysis.json:contrasts.CORR.delta")
    pool(2, "f1", "sham", f1, f1_an["sham_pseudo"],
         "data/f/screen_analysis.json:sham_pseudo", absval=True)
    pool(3, "B3-dpo", "marker", olmo["dpo"], an["delta_first"],
         "data/olmo/b3_analysis_dpo.json:delta_first")
    pool(3, "B3-dpo", "sham", olmo["dpo"], an["controls"]["sham"]["pseudo_delta"],
         "data/olmo/b3_analysis_dpo.json:controls.sham.pseudo_delta")
    pool(3, "B3-dpo", "random", olmo["dpo"],
         an["controls"]["random"]["pseudo_delta"],
         "data/olmo/b3_analysis_dpo.json:controls.random.pseudo_delta")
    # pooled stored rounding: e2a and f1 store 4 dp; olmo stores full floats.
    for p in pooled:
        if p["campaign"] in ("e2a", "f1") and not p["stored_is_abs"]:
            p["match"] = round(p["delta"], 4) == p["stored"]
        else:
            v = abs(p["delta"]) if p["stored_is_abs"] else p["delta"]
            p["match"] = abs(v - p["stored"]) < 1e-12

    # n-weighted identity: pooled = (nA dA + nB dB)/(nA + nB)
    def weighted_identity(recs, arm, maps):
        ks = [map_counts(recs, arm, m) for m in maps]
        k, n = pooled_counts(recs, arm)
        lhs = frac_delta(k, n)
        rhs = sum(nn * frac_delta(kk, nn) for kk, nn in ks) / sum(nn for _, nn in ks)
        simple = sum(frac_delta(kk, nn) for kk, nn in ks) / len(ks)
        return {"pooled": float(lhs), "weighted_mean_of_maps": float(rhs),
                "identity_holds": lhs == rhs,
                "simple_mean_of_maps": float(simple),
                "n_sum_equals_pooled_n": sum(nn for _, nn in ks) == n}

    ident = {"e2a reward": weighted_identity(e2a, "reward", ("A", "B")),
             "e2a sham": weighted_identity(e2a, "sham", ("A", "B")),
             "f1 CORR": weighted_identity(f1, "CORR", ("A", "B")),
             "f1 sham": weighted_identity(f1, "sham", ("A", "B")),
             "B3-dpo marker": weighted_identity(olmo["dpo"], "marker", ("0", "1"))}

    # ---------------- decomposition (post-hoc) ----------------
    deco = {}
    for key, recs, arm, maps in (("e2a reward", e2a, "reward", ("A", "B")),
                                 ("e2a sham", e2a, "sham", ("A", "B")),
                                 ("f1 CORR", f1, "CORR", ("A", "B")),
                                 ("f1 sham", f1, "sham", ("A", "B")),
                                 ("B3-dpo marker", olmo["dpo"], "marker", ("0", "1")),
                                 ("B3-dpo sham", olmo["dpo"], "sham", ("0", "1")),
                                 ("B3-dpo random", olmo["dpo"], "random", ("0", "1"))):
        deco[key] = {m: decompose(recs, arm, m, habit) for m in maps}
        deco[key]["pooled"] = decompose(recs, arm, None, habit)

    # identity / position reads at the first free pick (post-hoc)
    def first_pick_reads(recs, arm):
        sub = [r for r in recs if r["arm"] == arm and r["valid"]]
        n = len(sub)
        p0 = sum(1 for r in sub if r["pick"] == r["pair"][0])
        ma = sum(1 for r in sub if r["pick"] == r["menu_a"])
        st = sum(1 for r in sub if r["pick"] == r["start_tag"])
        per_pair = {}
        for r in sub:
            key = "/".join(r["pair"])
            d = per_pair.setdefault(key, {"n": 0, "pick_pair0": 0})
            d["n"] += 1
            d["pick_pair0"] += int(r["pick"] == r["pair"][0])
        return {"n": n, "pick_pair0": p0,
                "pick_pair0_p_two_sided": float(binom_two_sided(p0, n)),
                "pick_menu_first_listed": ma,
                "pick_menu_first_listed_p_two_sided": float(binom_two_sided(ma, n)),
                "pick_start_label_follows_habit": st,
                "per_pair": per_pair}

    reads = {"e2a reward": first_pick_reads(e2a, "reward"),
             "e2a sham": first_pick_reads(e2a, "sham"),
             "f1 CORR": first_pick_reads(f1, "CORR"),
             "f1 sham": first_pick_reads(f1, "sham"),
             "B3-dpo marker": first_pick_reads(olmo["dpo"], "marker"),
             "B3-dpo sham": first_pick_reads(olmo["dpo"], "sham"),
             "B3-dpo random": first_pick_reads(olmo["dpo"], "random")}

    # map-difference tests and single-map tests (post-hoc)
    tests = {}
    for key, recs, arm, (mpos, mneg) in (("e2a reward", e2a, "reward", ("A", "B")),
                                         ("e2a sham", e2a, "sham", ("A", "B")),
                                         ("f1 CORR", f1, "CORR", ("A", "B")),
                                         ("B3-dpo marker", olmo["dpo"], "marker", ("1", "0"))):
        k1, n1 = map_counts(recs, arm, mpos)
        k2, n2 = map_counts(recs, arm, mneg)
        tests[key] = {
            "positive_map": mpos, "k_pos_map": k1, "n_pos_map": n1,
            "other_map": mneg, "k_other_map": k2, "n_other_map": n2,
            "fisher_two_sided_map_difference": fisher_two_sided(k1, n1 - k1, k2, n2 - k2),
            "single_map_binom_upper_one_sided": float(binom_upper(k1, n1)),
        }

    # breaks toward pair[0] vs pair[1] per capture arm (post-hoc)
    for key in deco:
        pdx = deco[key]["pooled"]
        a, b = pdx["breaks_to_pair0"], pdx["breaks_to_pair1"]
        pdx["breaks_pair0_vs_pair1_p_two_sided"] = (
            float(binom_two_sided(a, a + b)) if a + b else None)

    # ---------------- per-pair structure (post-hoc; round-2 values-check) ----
    # A break is a first free pick != the start label (F = 2 alternating, so
    # the last forced label is the complement of the start; decompose()'s
    # pole-form definition, asserted equal below). maps[0] is the map whose
    # +label is pair[0]; maps[1] the map whose +label is pair[1].
    PAIR_ARMS = (("e2a reward", e2a, "reward", ("A", "B")),
                 ("e2a sham", e2a, "sham", ("A", "B")),
                 ("f1 CORR", f1, "CORR", ("A", "B")),
                 ("f1 sham", f1, "sham", ("A", "B")),
                 ("B3-dpo marker", olmo["dpo"], "marker", ("0", "1")))

    def is_break(r) -> bool:
        return r["pick"] != r["start_tag"]

    def per_pair(recs, arm, maps):
        sub = [r for r in recs if r["arm"] == arm and r["valid"]]
        out = {}
        for pr in sorted({tuple(r["pair"]) for r in sub}):
            sp = [r for r in sub if tuple(r["pair"]) == pr]
            for r in sp:
                assert r["map"] in maps, (arm, r["session"])
                assert r["plus_tag"] == (pr[0] if r["map"] == maps[0] else pr[1]), (arm, r["session"])
                assert r["pick"] in pr and r["start_tag"] in pr, (arm, r["session"])
                # pole-form break (decompose) == tag-form break (here)
                assert ((r["forced_poles"][-1] == "pos") == (r["first_pick_pole"] == "pos")) == is_break(r)
            n = len(sp)
            k0 = sum(1 for r in sp if r["pick"] == pr[0])
            row = {"pair": "/".join(pr), "n": n, "pick_pair0": k0, "pick_pair1": n - k0,
                   "pick_pair0_p_two_sided": float(binom_two_sided(k0, n)),
                   "maps": {}, "starts": {}}
            for m in maps:
                sm = [r for r in sp if r["map"] == m]
                row["maps"][m] = {"k_plus": sum(1 for r in sm if r["first_plus"]), "n": len(sm),
                                  "plus_tag": pr[0] if m == maps[0] else pr[1]}
            a_, na = row["maps"][maps[0]]["k_plus"], row["maps"][maps[0]]["n"]
            b_, nb = row["maps"][maps[1]]["k_plus"], row["maps"][maps[1]]["n"]
            row["fisher_two_sided_maps_within_pair"] = (
                fisher_two_sided(a_, na - a_, b_, nb - b_) if na and nb else None)
            for i, tag in enumerate(pr):
                other = pr[1 - i]
                row["starts"][tag] = {
                    m: {"n": sum(1 for r in sp if r["map"] == m and r["start_tag"] == tag),
                        "broke_to": other,
                        "broke": sum(1 for r in sp if r["map"] == m and r["start_tag"] == tag
                                     and r["pick"] == other)}
                    for m in maps}
            br = [r for r in sp if is_break(r)]
            row["breaks_to_tag"] = {t: sum(1 for r in br if r["pick"] == t) for t in pr}
            row["breaks_to_plus_by_map"] = {m: sum(1 for r in br if r["map"] == m
                                                   and r["pick"] == r["plus_tag"]) for m in maps}
            row["breaks_to_minus_by_map"] = {m: sum(1 for r in br if r["map"] == m
                                                    and r["pick"] != r["plus_tag"]) for m in maps}
            out[row["pair"]] = row
        return out

    pp = {key: per_pair(recs, arm, maps) for key, recs, arm, maps in PAIR_ARMS}
    # the per-pair break counts sum to decompose()'s pooled break counts
    for key, recs, arm, maps in PAIR_ARMS:
        x = deco[key]["pooled"]
        assert sum(sum(v["breaks_to_tag"].values()) for v in pp[key].values()) == \
            x["breaks_to_plus"] + x["breaks_to_minus"], key
        assert sum(v["breaks_to_tag"][v["pair"].split("/")[0]] for v in pp[key].values()) == \
            x["breaks_to_pair0"], key

    # maple/cedar across all ten Qwen arms (e2a x 4, f1 x 6)
    MC = ("maple", "cedar")
    QARMS = sorted([("e2a", a) for a in ("reward", "sham", "random1", "random2")]
                   + [("f1", a) for a in ("SOLV", "DIFF", "NOV", "CORR", "FDBK", "sham")])
    qv = [r for r in e2a + f1 if r["valid"]]
    assert sorted({(r["campaign"], r["arm"]) for r in qv}) == QARMS
    assert all(tuple(r["pair"]) == MC or not ({"maple", "cedar"} & set(r["pair"])) for r in qv)
    mc = [r for r in qv if tuple(r["pair"]) == MC]
    assert all(r["plus_tag"] == ("maple" if r["map"] == "A" else "cedar") for r in mc)
    mc_cs = [r for r in mc if r["start_tag"] == "cedar"]
    mc_ms = [r for r in mc if r["start_tag"] == "maple"]
    oth = [r for r in qv if tuple(r["pair"]) != MC]
    mc_all = {
        "arms": [f"{c} {a}" for c, a in QARMS], "n": len(mc),
        "maple_first": sum(1 for r in mc if r["pick"] == "maple"),
        "cedar_start_n": len(mc_cs),
        "cedar_start_broke_to_maple": sum(1 for r in mc_cs if r["pick"] == "maple"),
        "cedar_start_by_map": {
            m: {"label": "maple = +label" if m == "A" else "maple = −label",
                "n": sum(1 for r in mc_cs if r["map"] == m),
                "broke_to_maple": sum(1 for r in mc_cs if r["map"] == m and r["pick"] == "maple")}
            for m in ("A", "B")},
        "maple_start_n": len(mc_ms),
        "maple_start_broke_to_cedar": sum(1 for r in mc_ms if r["pick"] == "cedar"),
        "other_pairs_n": len(oth),
        "other_pairs_breaks": sum(1 for r in oth if is_break(r)),
    }

    # maps with maple/cedar removed; maple/cedar pooled over maps (Qwen arms)
    nomc = {}
    for key, recs, arm, maps in PAIR_ARMS[:4]:
        d = {"maps": {}}
        for m in maps:
            s_ = [r for r in recs if r["arm"] == arm and r["valid"] and r["map"] == m
                  and tuple(r["pair"]) != MC]
            k = sum(1 for r in s_ if r["first_plus"])
            br = [r for r in s_ if is_break(r)]
            d["maps"][m] = {"k": k, "n": len(s_), "delta": float(frac_delta(k, len(s_))),
                            "delta_exact": str(frac_delta(k, len(s_))),
                            "breaks_to_plus": sum(1 for r in br if r["pick"] == r["plus_tag"]),
                            "breaks_to_minus": sum(1 for r in br if r["pick"] != r["plus_tag"])}
        s_mc = [r for r in recs if r["arm"] == arm and r["valid"] and tuple(r["pair"]) == MC]
        kmc = sum(1 for r in s_mc if r["first_plus"])
        d["maple_cedar_pooled_over_maps"] = {"k": kmc, "n": len(s_mc),
                                             "delta": float(frac_delta(kmc, len(s_mc)))}
        b0 = [r for r in recs if r["arm"] == arm and r["valid"] and is_break(r)
              and r["pick"] == r["pair"][0]]
        d["pair0_breaks"] = len(b0)
        d["pair0_breaks_that_are_maple"] = sum(1 for r in b0 if r["pick"] == "maple")
        bp = sum(v["breaks_to_plus"] for v in d["maps"].values())
        bm = sum(v["breaks_to_minus"] for v in d["maps"].values())
        d["breaks_plus_vs_minus_without_mc"] = [bp, bm]
        d["breaks_plus_vs_minus_without_mc_p_two_sided"] = (
            float(binom_two_sided(bp, bp + bm)) if bp + bm else None)
        ds = [v["delta"] for v in d["maps"].values()]
        d["opposite_signed"] = max(ds) > 0 and min(ds) < 0
        nomc[key] = d

    # B3 DPO marker: map-1 start-on-+ and map-1 breaks to + by pair
    b3pp = pp["B3-dpo marker"]
    b3_map1 = {}
    for pk_, v in b3pp.items():
        plus1 = v["maps"]["1"]["plus_tag"]
        st = v["starts"][plus1]["1"]
        b3_map1[pk_] = {"plus_tag": plus1, "n": v["maps"]["1"]["n"],
                        "started_on_plus": st["n"],
                        "started_on_plus_and_picked_it": st["n"] - st["broke"],
                        "breaks_to_plus": v["breaks_to_plus_by_map"]["1"]}
    b3_map1_plus_break_tags = sorted(
        {r["pick"] for r in olmo["dpo"] if r["arm"] == "marker" and r["valid"]
         and r["map"] == "1" and is_break(r) and r["pick"] == r["plus_tag"]})

    # H3 tag screen on Qwen (record measurement; identity_split recomputed
    # from its per-probe rows with tagscreen.decompose's formula, stdlib)
    h3 = json.loads(raw["h3_tagscreen"])
    h3_rows = {}
    for p_ in h3["pairs"]:
        s_ = p_["formats"]["scaffold"]
        h3_ident = []
        for r in s_["per_probe"]:
            tot = float(r["p_first"]) + float(r["p_second"])
            if tot <= 0:
                continue
            pf = float(r["p_first"]) / tot
            h3_ident.append(pf if r["first"] == min(r["first"], r["second"]) else 1.0 - pf)
        recomputed = sum(h3_ident) / len(h3_ident)
        h3_rows[p_["name"]] = {"tag_lo": s_["tag_lo"], "tag_hi": s_["tag_hi"],
                               "identity_split": s_["identity_split"],
                               "identity_split_recomputed": recomputed,
                               "recomputed_matches": abs(recomputed - s_["identity_split"]) < 1e-12,
                               "imbalance": s_["imbalance"], "n": s_["n"]}
    h3_c = {k: v for k, v in h3_rows.items() if k.startswith("C")}
    e2a_pairs = {frozenset(r["pair"]) for r in e2a}
    assert {frozenset((v["tag_lo"], v["tag_hi"])) for v in h3_c.values()} == e2a_pairs
    assert {frozenset(r["pair"]) for r in f1} == e2a_pairs
    h3_c2 = h3_rows["C2"]
    assert (h3_c2["tag_lo"], h3_c2["tag_hi"]) == ("cedar", "maple")
    h3_c2_worst = max(h3_c, key=lambda k: h3_c[k]["imbalance"]) == "C2"
    h3_band = h3["band"]

    # f1 CORR delivery (cross-reference to N5): Q rounds whose stored task
    # text equals a clean CORR_clean item on its stored prefix
    f1_pools = json.loads(raw["f1_pools"])
    corr_clean = {x["task"][:40]: i for i, x in enumerate(f1_pools["CORR_clean"])}
    f1_task_maxlen = max(len(x["task"]) for r in _f1_rows for x in r["rounds"])
    corr_rows = [r for r in _f1_rows if r["arm"] == "CORR"]
    corr_q = [x for r in corr_rows for x in r["rounds"] if x["cfg"] == "Q"]
    corr_q_clean = [x for x in corr_q if x["task"][:40] in corr_clean]
    corr_valid = [r for r in corr_rows if not r["excluded"] and r["first_free_pick_P"] is not None]
    corr_one_clean = 0
    for r in corr_valid:
        fq = [x for x in r["rounds"][:4] if x["cfg"] == "Q"]
        assert len(fq) == 2
        corr_one_clean += int(sum(x["task"][:40] in corr_clean for x in fq) == 1)
    n5_xref = {"corr_sessions": len(corr_rows), "q_rounds": len(corr_q),
               "q_rounds_clean_prefix": len(corr_q_clean),
               "clean_items": sorted({corr_clean[x["task"][:40]] for x in corr_q_clean}),
               "valid_sessions": len(corr_valid),
               "valid_with_one_clean_forced_q": corr_one_clean,
               "stored_task_field_max_len": f1_task_maxlen}

    # ---------------- context: every arm's maps in the three campaigns -----
    context = []

    def ctx(campaign, arm, maps, recs, stored_maps, src):
        row = {"campaign": campaign, "arm": arm, "maps": {}}
        for m in maps:
            k, n = map_counts(recs, arm, m)
            row["maps"][m] = {"k": k, "n": n, "delta": float(frac_delta(k, n))}
            if stored_maps is not None:
                sv = stored_maps[m]
                sv = sv["delta"] if isinstance(sv, dict) else sv
                row["maps"][m]["stored"] = sv
                row["maps"][m]["match"] = (abs(sv - float(frac_delta(k, n))) < 1e-12
                                           if isinstance(stored_maps[m], dict)
                                           else round(float(frac_delta(k, n)), 4) == sv)
        ds = [v["delta"] for v in row["maps"].values()]
        row["opposite_signed"] = (max(ds) > 0 and min(ds) < 0)
        row["max_abs_map_delta"] = max(abs(x) for x in ds)
        mx_exact = max(abs(frac_delta(*map_counts(recs, arm, m))) for m in maps)
        row["max_abs_map_delta_exact"] = str(mx_exact)
        row["_mx_exact"] = mx_exact
        row["source"] = src
        context.append(row)

    for arm in ("reward", "sham", "random1", "random2"):
        ctx("e2a", arm, ("A", "B"), e2a, e2a_an[arm]["by_map"],
            f"data/e2a/analysis.json:{arm}.by_map")
    for arm in ("SOLV", "DIFF", "NOV", "CORR", "FDBK"):
        ctx("f1", arm, ("A", "B"), f1, f1_an["contrasts"][arm]["by_map"],
            f"data/f/screen_analysis.json:contrasts.{arm}.by_map")
    ctx("f1", "sham", ("A", "B"), f1, None,
        "recomputed from data/f/sessions.jsonl")
    for st in OLMO_STAGES:
        ctx(f"B3-{st}", "marker", ("0", "1"), olmo[st],
            olmo_an[st]["by_label_map"],
            f"data/olmo/b3_analysis_{st}.json:by_label_map")
        for arm in ("sham", "random"):
            ctx(f"B3-{st}", arm, ("0", "1"), olmo[st], None,
                f"recomputed from data/olmo/b3_screen_{st}.json")
    n_ctx = len(context)
    n_opp = sum(1 for r in context if r["opposite_signed"])
    TENTH = Fraction(1, 10)
    n_ge10 = sum(1 for r in context if r["_mx_exact"] >= TENTH)
    n_gt10 = sum(1 for r in context if r["_mx_exact"] > TENTH)
    at_tenth = [f"{r['campaign']} {r['arm']}" for r in context if r["_mx_exact"] == TENTH]
    for r in context:
        del r["_mx_exact"]
    all_ctx_match = all(v.get("match", True) for r in context
                        for v in r["maps"].values())

    # ---------------- record locators ----------------
    RC = "archive/RESULTS-cycles3-4.md"
    R = "RESULTS.md"
    L = {}
    L["e2a_verdict_head"] = one_line(RC, "2026-08-09 — **e2a VERDICT: NOT PASSED")
    L["e2a_conj2"] = one_line(RC, "(2) FAIL: map A +0.104 / map B −0.031")
    L["e2a_absorbed"] = one_line(RC, "identifying it as a label/order artifact correctly absorbed by")
    L["e2a_conj3"] = one_line(RC, "counterbalancing. Conjunct (3) FAIL")
    L["e2a_conj1"] = one_line(RC, "free choices toward +pole). Conjunct (1) FAIL: max pseudo-Δ =")
    L["e2a_random1_noise"] = one_line(RC, "(iv) random1's +0.152")
    assert "its criterion job" in pinned_lines(RC)[L["e2a_random1_noise"]]  # the phrase ends on the next line
    L["e2a_prereg_stat"] = one_line(RC, "session; Δ = P(choose +pole) − 0.5 pooled over counterbalance maps.")
    L["e2a_prereg_conj2"] = one_line(RC, "random arms; (2) Δ ≥ 0 in BOTH counterbalance maps;")
    L["f1_verdict_head"] = one_line(RC, "2026-08-10 — **f1 SCREEN VERDICT: FIVE NULLS")
    L["f1_mirror"] = one_line(RC, "(maps +.121/−.130 mirror-cancel — the label artifact absorbed by")
    L["f1_sham_pseudo"] = one_line(RC, "Sham pseudo-Δ = .045.")
    L["f1_prereg"] = one_line("PROPOSAL-f-natural-reinforcer-screen.md", "**Screen-hit criterion (per contrast):**")
    L["f1_hornfree"] = one_line("PROPOSAL-f-natural-reinforcer-screen.md", "## 0. Why this design, and why it is horn-free")
    L["f1_noinj"] = one_line("PROPOSAL-f-natural-reinforcer-screen.md", "- Nothing is injected → no state-at-readout contamination")
    L["f1_corr_row"] = one_line("PROPOSAL-f-natural-reinforcer-screen.md", "| 4 | CORR | clean text vs **seeded character-level corruption**")
    L["f1_corr_zero"] = one_line(RC, "CORR n=56, Δ = 0.000 exactly")
    L["recount_frozen"] = one_line("scripts/e2a_recount.py", "55/102 under the frozen audit; 54/101 under v2.")
    L["proph_h1"] = one_line("PROPOSAL-h-state-present-choice.md", "H1 measures the residual")
    L["f4_noinj"] = one_line("FINDINGS-4.md", "with **no injection and no adapter**")
    L["f4_table"] = one_line("FINDINGS-4.md", "| CORR (avoid corrupted) | 56 |")
    L["f4_point4_start"] = one_line("FINDINGS-4.md", "**4. The territory manufactures false positives, demonstration two.**")
    L["f4_point4_end"] = one_line("FINDINGS-4.md", "claim, now shown twice at the same magnitude.")
    L["f3_start"] = one_line("FINDINGS-3.md", "(A +0.104 / B −0.031) with the **identical pattern in sham**")
    L["f3_end"] = one_line("FINDINGS-3.md", "published as approach behavior; binomial p = 0.244.")
    L["b3_head"] = one_line(R, "2026-08-24 — **B3 SCREEN COMPLETE, ALL FOUR STAGES")
    L["b3_table_dpo"] = one_line(R, "| dpo | 48 | 27 | +0.0625 | −0.0417 | +0.1667 |")
    L["b3_artifact_start"] = one_line(R, "- **DPO is the one that shows why the criterion is conjunctive.**")
    L["b3_artifact_end"] = one_line(R, "earned its keep here.")
    L["b3_envelope"] = one_line(R, "- **Envelope caveat, for interpretation not for change.**")
    L["lockg_trigger"] = one_line("LOCK-g.md", "- **Screen trigger, values in place:**")
    L["propj_three"] = one_line("PROPOSAL-j-dose-escalation.md", "3. **Label artifact (~0.10; three live captures across two models)**")
    L["proph_receipt"] = one_line("PROPOSAL-h-state-present-choice.md", "f1 mirror-cancel (+.121/−.130 → 0.000).")
    L["proph_leak"] = one_line("PROPOSAL-h-state-present-choice.md", "- **Direct logit leak is token-level.**")
    L["claude_rule12"] = one_line("CLAUDE.md", "12. Counterbalance + sham always; position/label artifacts are")
    L["habit_identity"] = one_line("valence_core/e2d/habit.py", "**Delta_first = 1/2 * (b+ - bs)**")
    L["habit_weighted"] = one_line("valence_core/e2d/habit.py", "P(+) = n+/N * b+ + ns/N * (1 - bs)")
    L["habit_rule11"] = one_line("valence_core/e2d/habit.py", "RULE 11. The decomposition is algebra, not a finding")
    L["habit_e2a_rate"] = one_line("valence_core/e2d/habit.py", "**156/187** opening")
    L["b3_order"] = one_line("scripts/box_b3_sessions.py", "order = ([\"pos\", \"neg\"] if idx % 2 == 0 else [\"neg\", \"pos\"]) * F")
    L["b3_strata"] = one_line("scripts/box_b3_sessions.py", "tp, tm = (pair[0], pair[1]) if m == 0 else (pair[1], pair[0])")
    L["b3a_delta"] = one_line("scripts/b3_analyze.py", "def delta(sessions, arm) -> tuple[float, int, int]:")
    L["b3a_bymap"] = one_line("scripts/b3_analyze.py", "def by_map(sessions, arm) -> dict:")
    L["b3a_locks"] = one_line("scripts/b3_analyze.py", "def locks_toward(positive: bool) -> bool:")
    L["recount_primary"] = one_line("scripts/e2a_recount.py", "def primary(audit):")
    L["reg_screen"] = one_line("valence_core/regression/analysis.py", "def check_screen_pvalues() -> list[Check]:")
    # round-2 values-check locators
    L["h3_head"] = one_line(R, "2026-08-20 — **H3 ran on Qwen: only 3/8 candidate pairs clear the")
    L["h3_c2"] = one_line(R, "| C2 | maple/cedar | 0.207 | 0.293 |")
    L["h3_basis"] = one_line(R, "the 2026-08-19 finding that made H3 mandatory. On Qwen, C1")
    L["h3_noimpeach"] = one_line(R, "clean on the apparatus that produced the cycle-3/4 numbers, so no")
    L["h3_noimpeach_end"] = one_line(R, "own tags. The screen was still right to run: it converted an")
    L["mapswap"] = one_line(R, "Only the label-MAP swap (which tag")
    L["mapswap_end"] = one_line(R, "load-bearing rather than belt-and-braces.")
    L["spends_power"] = one_line(R, "spends power the contrast needs.")
    L["tagscreen_doc"] = one_line("valence_core/tagscreen.py", "`identity_split` is the share taken by `tag_lo` (the alphabetically")
    L["propj_e2a_pairs"] = one_line("PROPOSAL-j-dose-escalation.md", "screening mandatory after the 2026-08-19 finding; e2a's own pairs")
    L["propj_not_admitted"] = one_line("PROPOSAL-j-dose-escalation.md", "order-counterbalanced but never screened and are **not admitted**.")
    L["f3_tenth"] = one_line("FINDINGS-3.md", "a label/order artifact of ≈ 0.10 that an")
    L["b3_tenth"] = one_line(R, "and it is the size rule 12 names as first-order (~0.10).")
    L["claude_tenth"] = one_line("CLAUDE.md", "first-order (~0.10), captured live twice.")
    J["locators"] = {k: v for k, v in L.items()}

    # gitignored-clone analyzers (quoted with sha256; not in any clone)
    E2A_RUN = "jlens-qwen36/scripts/e2a_sessions.py"
    F1_RUN = "jlens-qwen36/scripts/f_sessions.py"
    clone = {}
    for p in (E2A_RUN, F1_RUN):
        clone[p] = {"sha256": sha256_file(p) if os.path.exists(os.path.join(REPO, p)) else None}
    e2a_swap = local_find(E2A_RUN, "swap = (s // 4) % 2 == 1")
    e2a_firsts = local_find(E2A_RUN, "firsts = [r[\"first_free_pick_pos\"] for r in sub]")
    e2a_bymap = local_find(E2A_RUN, "by_map[\"B\" if m else \"A\"] = (round(float(np.mean(mm)) - 0.5, 4)")
    e2a_pseudo = local_find(E2A_RUN, "pseudo = [abs(out[a][\"delta_first\"]) for a in")
    f1_swap = local_find(F1_RUN, "swap = (s // 4) % 2 == 1")
    f1_start = local_find(F1_RUN, "start_P = (s // 8) % 2 == 0")
    f1_pseudo = local_find(F1_RUN, "pseudo = abs(float(np.mean(sham_first)) - 0.5) if sham_first else None")
    f1_firsts = local_find(F1_RUN, "firsts = [r[\"first_free_pick_P\"] for r in valid if r[\"arm\"] == c")
    f1_bymap = local_find(F1_RUN, "by_map[\"B\" if m else \"A\"] = (round(float(np.mean(mm)) - 0.5, 4)")
    f1_forced = local_find(F1_RUN, "order += ([\"P\", \"Q\"] if start_P else [\"Q\", \"P\"])")
    f1_fforced = local_find(F1_RUN, "F_FORCED = 2")
    e2a_start = local_find(E2A_RUN, "start_plus = (s // 8) % 2 == 0")

    # ---------------- write markdown ----------------
    o: list[str] = []
    w = o.append
    w("# AUDIT-note-release v1.2 -- N14: sham-arm pseudo-statistics, the three label-artifact captures")
    w("")
    w(f"- Code stamp: {stamp} (date -u)  [run metadata]")
    w(f"- HEAD at run time: {head}  [run metadata; every record read below is pinned to {PIN}]")
    w(f"- Pin: {PIN} = {pin_full}")
    w(f"- Block: `{BLOCK}`@{PIN} sha256 `{block_sha}` ({block_n} lines; "
      f"{'MATCH' if block_ok else 'MISMATCH'} vs routed {ROUTED_BLOCK[0]}...{ROUTED_BLOCK[1]}); "
      f"item N14 = block lines {ITEM_LINES[0]}-{ITEM_LINES[1]}")
    w(f"- Script: `{script_rel}` sha256 `{script_sha}`")
    w(f"- Interpreter: {sys.executable} (Python {platform.python_version()}); stdlib only "
      f"(math.comb, fractions.Fraction); no numpy/scipy/sklearn use; no model")
    w(f"- Command: `{cmd}` (run from the repository root)")
    w("")
    w("Status vocabulary: reproduced (computed here from committed JSON/JSONL and equal to the stored field) | "
      "log-only (prose only; pinned locator) | not found | discrepant | computed-new (asked-for or supporting "
      "computation with no stored counterpart). Locators are `path@bbc9ffe:line` as in `git show bbc9ffe:<path>`; "
      "every line number below was found by this script by searching the pinned text, not typed.")
    w("")
    w("The item, quoted from the block:")
    w("")
    for i, l in enumerate(item_text):
        w(f"> {BLOCK}@{PIN}:{ITEM_LINES[0] + i}: {l}")
    w("")
    w("## 0. Referents and integrity")
    w("")
    w("Every artifact is read from the pin with `git show`; its sha256 at the pin and the working tree's blob "
      "against the pin (informational; nothing here reads the working tree's copy):")
    w("")
    w("| artifact | sha256 at pin | working tree vs pin |")
    w("|---|---|---|")
    for p in paths.values():
        w(f"| `{p}` | `{art_sha[p]}` | {art_wt[p]} |")
    w(f"| `valence_core/e2d/habit.py` (executed from its pinned blob) | `{sha256_bytes(habit_src.encode())}` | "
      f"{art_wt['valence_core/e2d/habit.py']} |")
    w("")
    w(f"Analyzers of record that live in the gitignored clone (absent from any clone of the repository; opened "
      f"read-only, quoted for definitions only, nothing executed): `{E2A_RUN}` sha256 `{clone[E2A_RUN]['sha256']}`; "
      f"`{F1_RUN}` sha256 `{clone[F1_RUN]['sha256']}`. The tracked reproduction paths are `scripts/e2a_recount.py` "
      f"(e2a) and `scripts/b3_analyze.py` (B3). For f1, no tracked code at the pin recomputes the by-map figures "
      f"from `data/f/sessions.jsonl` (the regression suite's `check_screen_pvalues`, "
      f"valence_core/regression/analysis.py@{PIN}:{L['reg_screen']}, recovers k from the stored `delta` and "
      f"re-tests the p-values; it does not read the maps), so this script's recount is the tracked reproduction of "
      f"the f1 map figures below.")
    w("")
    w(f"Structural assertions on the session records (all passed, or the script would have stopped): tag_plus/tag_P "
      f"= pair[1] iff swap (e2a, f1) and tag_plus = pair[map] (B3); each stored first-pick flag equals the first "
      f"choice's picked pole. f1 forced phase = 2 rounds per config alternating from the start config "
      f"(`{F1_RUN}:{f1_fforced}`, `:{f1_forced}`): {f1_checks['forced_order_ok']}/{f1_checks['valid_checked']} "
      f"valid sessions match; the fifth round ran the config the first free choice picked in "
      f"{f1_checks['first_free_round_cfg_ok']}/{f1_checks['valid_checked']}. B3 forced order starts +pole iff the "
      f"arm's session index is even (`scripts/box_b3_sessions.py@{PIN}:{L['b3_order']}`): "
      + "; ".join(f"{st} {olmo_parity[st]['start_pos_iff_even_index']}/{olmo_parity[st]['checked']}"
                  for st in OLMO_STAGES) + " sessions (all run sessions, incl. excluded). Added at the round-2 "
      "values-check: in every capture arm the +label is pair[0] in map A / 0 and pair[1] in map B / 1; for every "
      "valid session the tag-form habit break (first pick ≠ start label) equals decompose()'s pole form; the per-pair "
      "break counts sum to the pooled decomposition's; maple and cedar occur only as the pair maple/cedar in the ten "
      "Qwen arms; and H3's four C pairs are exactly e2a's and f1's four pairs.")
    w("")

    # ---- section 1: the table ----
    w("## 1. The three captures in one table")
    w("")
    w("Statistic in every row: **Δ_map = k/n − ½**, n = the arm's VALID sessions in that label map (excluded "
      "sessions and sessions with no first free choice removed, as each campaign's analyzer removes them), k = those "
      "whose FIRST free choice picked the arm's +label (+pole / P). Domain of every rate: valid sessions of the "
      "named arm and map. Stored values are 4 dp in e2a and f1 (rounded by the analyzer), full floats in B3. "
      f"e2a: validity is the session record's stored `excluded` flag (stored exclusions: "
      + ", ".join(f"{a} {v[0]}/{v[1]}" for a, v in e2a_excl.items()) +
      f"), i.e. the FROZEN audit's exclusion set, the published rule that `analysis.json` carries "
      f"(scripts/e2a_recount.py@{PIN}:{L['recount_frozen']}, \"55/102 under the frozen audit; 54/101 under v2\"). "
      f"Every e2a figure here is on that domain; the v2 recount (54/101) is N4's, not this item's.")
    w("")
    w("| # | model | campaign | arm | role | map | k/n | Δ_map (exact) | Δ_map | stored | stored field | match | status |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for c in cells:
        st = c["stored"]
        st_s = ("—" if st is None else
                (f"{d4(st['delta'])} ({st['k']}/{st['n']})" if isinstance(st, dict) else d4(st)))
        w(f"| {c['capture']} | {c['model']} | {c['campaign']} | {c['arm']} | {c['role']} | {c['map']} | "
          f"{c['k']}/{c['n']} | {c['delta_exact']} | **{d4(c['delta'])}** | {st_s} | `{c['stored_src']}` | "
          f"{c['match']} | {c['status']} |")
    w("")
    w("Pooled over both maps, same arms (Δ = k/n − ½ over valid sessions of the arm):")
    w("")
    w("| capture | campaign | arm | k/n | Δ pooled | stored | stored field | match |")
    w("|---|---|---|---|---|---|---|---|")
    for p in pooled:
        sv = (f"{p['stored']:.6f} (absolute value, as stored)" if p["stored_is_abs"] else d4(p["stored"]))
        w(f"| {p['capture']} | {p['campaign']} | {p['arm']} | {p['k']}/{p['n']} | {d4(p['delta'])} | {sv} | "
          f"`{p['stored_src']}` | {'YES' if p['match'] else 'NO'} |")
    w("")
    w("The pooled Δ is the n-weighted mean of the two map Δs, not their simple mean (exact Fractions):")
    w("")
    w("| arm | pooled | n-weighted mean of maps | identity holds | simple mean of maps |")
    w("|---|---|---|---|---|")
    for k_, v in ident.items():
        w(f"| {k_} | {d4(v['pooled'])} | {d4(v['weighted_mean_of_maps'])} | {v['identity_holds']} | "
          f"{d4(v['simple_mean_of_maps'])} |")
    w("")
    corr_A = [c for c in cells if c["campaign"] == "f1" and c["arm"] == "CORR" and c["map"] == "A"][0]
    corr_B = [c for c in cells if c["campaign"] == "f1" and c["arm"] == "CORR" and c["map"] == "B"][0]
    kc, nc = pooled_counts(f1, "CORR")
    w(f"f1 CORR's exact 0.000 is an outcome of the counts, not of the design: map A {corr_A['k']}/{corr_A['n']} "
      f"and map B {corr_B['k']}/{corr_B['n']} give k − n/2 = {Fraction(corr_A['k']) - Fraction(corr_A['n'], 2)} and "
      f"{Fraction(corr_B['k']) - Fraction(corr_B['n'], 2)}, pooled {kc}/{nc}. Counterbalancing makes a map-locked "
      f"artifact cancel in expectation; the exact zero here is the realized counts.")
    w("")

    # ---- section 2: definitions ----
    w("## 2. Definitions of record, per capture")
    w("")
    w("**e2a (capture 1).** Producing analyzer in the gitignored clone; tracked recount `scripts/e2a_recount.py`.")
    w("")
    w("```")
    for q in (local_quote(E2A_RUN, e2a_swap, e2a_swap + 1) + local_quote(E2A_RUN, e2a_start, e2a_start)
              + local_quote(E2A_RUN, e2a_firsts, e2a_firsts + 1) + local_quote(E2A_RUN, e2a_bymap - 1, e2a_bymap)
              + local_quote(E2A_RUN, e2a_pseudo, e2a_pseudo + 1)):
        w(q)
    for q in quote("scripts/e2a_recount.py", L["recount_primary"], L["recount_primary"] + 4):
        w(q)
    w("```")
    w("")
    w(f"Pre-registered statistic and conjunct (2): {RC}@{PIN}:{L['e2a_prereg_stat']} and :{L['e2a_prereg_conj2']} "
      f"(\"Δ = P(choose +pole) − 0.5 pooled over counterbalance maps\"; \"(2) Δ ≥ 0 in BOTH counterbalance maps\"). "
      f"Map = which label of the rotated pair is +pole: {E2A_MAP}. In the sham arm no label carries a state; its "
      f"+pole is designated by the same rule, so its map Δs are the identical statistic on an arm where no "
      f"contingency exists. The control envelope (conjunct 1) is max |pooled Δ| over sham, random1, random2 "
      f"(absolute values, `{E2A_RUN}:{e2a_pseudo}`); the map split enters only conjunct (2).")
    w("")
    w("**f1 CORR (capture 2).** Producing analyzer in the gitignored clone (`analyze()`); no tracked analyzer at the pin.")
    w("")
    w("```")
    for q in (local_quote(F1_RUN, f1_swap, f1_swap + 1) + local_quote(F1_RUN, f1_start, f1_start)
              + local_quote(F1_RUN, f1_pseudo, f1_pseudo)
              + local_quote(F1_RUN, f1_firsts, f1_firsts + 1) + local_quote(F1_RUN, f1_bymap - 3, f1_bymap)):
        w(q)
    w("```")
    w("")
    w(f"Pre-registered screen-hit criterion: PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{L['f1_prereg']}-"
      f"{L['f1_prereg'] + 2} (\"(2) sign consistency across both maps\"). Map = which label of the pair denotes P: "
      f"{F1_MAP}. For CORR, P = clean text and Q = seeded character-level corruption (target direction: avoid "
      f"corrupted, one-sided; PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{L['f1_corr_row']}, the CORR table "
      f"row). f1 has no injected state in any arm (PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{L['f1_noinj']}, "
      f"\"Nothing is injected\", under the §0 heading at :{L['f1_hornfree']}; FINDINGS-4.md@{PIN}:{L['f4_noinj']}). "
      f"The stored sham statistic is an absolute value (`sham_pseudo` = |share − ½|).")
    w("")
    w("**B3 DPO (capture 3).** Tracked analyzer `scripts/b3_analyze.py` (committed before any campaign ran, per its docstring).")
    w("")
    w("```")
    for q in (quote("scripts/b3_analyze.py", L["b3a_delta"], L["b3a_delta"] + 8)
              + quote("scripts/b3_analyze.py", L["b3a_bymap"], L["b3a_bymap"] + 10)
              + quote("scripts/b3_analyze.py", L["b3a_locks"], L["b3a_locks"] + 2)
              + quote("scripts/box_b3_sessions.py", L["b3_strata"] - 4, L["b3_strata"] + 3)):
        w(q)
    w("```")
    w("")
    w(f"Pre-registered screen trigger: LOCK-g.md@{PIN}:{L['lockg_trigger']}-{L['lockg_trigger'] + 3} (marker Δ "
      f"exceeds the campaign's own control envelope = max |pseudo-Δ| over sham and random, AND sign locks across "
      f"maps). Map = {B3_MAP}. sign-lock requires both maps non-zero and of one sign (`locks_toward`). Registered "
      f"valid targets {b3_targets['marker']}:{b3_targets['sham']}:{b3_targets['random']} "
      f"(`data/olmo/b3_screen_dpo.json:targets`), scheduled per stratum "
      f"{b3_per_stratum['marker']}:{b3_per_stratum['sham']}:{b3_per_stratum['random']} over "
      f"{b3_n_strata} strata (4 pairs x 2 maps; `data/olmo/b3_screen_dpo.json:per_stratum`, `:strata`); realized "
      f"per-map valid n at DPO: marker "
      f"{map_counts(olmo['dpo'], 'marker', '0')[1]}/{map_counts(olmo['dpo'], 'marker', '1')[1]}, sham "
      f"{map_counts(olmo['dpo'], 'sham', '0')[1]}/{map_counts(olmo['dpo'], 'sham', '1')[1]}, random "
      f"{map_counts(olmo['dpo'], 'random', '0')[1]}/{map_counts(olmo['dpo'], 'random', '1')[1]} (map 0 / map 1).")
    w("")

    # ---- section 3: controls beside ----
    w("## 3. The sham (and random) arms beside each capture")
    w("")
    w("| capture | arm | map | k/n | Δ_map | pooled k/n | pooled Δ | status |")
    w("|---|---|---|---|---|---|---|---|")
    for c in cells:
        if c["role"].startswith("beside (sham") or c["role"].startswith("beside (random") or c["role"] == "capture (sham arm)":
            recs = {"e2a": e2a, "f1": f1, "B3-dpo": olmo["dpo"]}[c["campaign"]]
            pk, pn = pooled_counts(recs, c["arm"])
            w(f"| {c['capture']} ({c['campaign']}) | {c['arm']} | {c['map']} | {c['k']}/{c['n']} | {d4(c['delta'])} | "
              f"{pk}/{pn} | {d4(frac_delta(pk, pn))} | {c['status']} |")
    w("")
    e2a_env = max(abs(e2a_an[a]["delta_first"]) for a in ("sham", "random1", "random2"))
    e2a_c1 = e2a_an["reward"]["delta_first"] > e2a_env
    e2a_c2 = all(v >= 0 for v in e2a_an["reward"]["by_map"].values())
    f1_conj = f1_an["contrasts"]["CORR"]["conjuncts"]
    b3_conj = an["conjuncts"]
    w(f"Only capture 1 is itself a sham-arm statistic. Capture 2 is a contrast arm (CORR) whose maps cancel; capture 3 "
      f"is the marker arm, one map positive. Which shield disposed of each excursion, from the stored or recomputed "
      f"conjuncts: e2a reward -- envelope conjunct {e2a_c1} (Δ {d4(e2a_an['reward']['delta_first'])} vs max abs "
      f"pseudo-Δ {e2a_env:.4f}, recomputed from analysis.json with the analyzer's abs reading), both-maps-≥0 conjunct "
      f"{e2a_c2}; f1 CORR -- the counterbalanced pooling itself cancels the excursion (pooled 0.000), and the stored "
      f"conjuncts (envelope, sign consistency, binomial) are {f1_conj} "
      f"(`data/f/screen_analysis.json:contrasts.CORR.conjuncts`); B3 DPO -- stored "
      f"`delta_exceeds_envelope_upward` {b3_conj['delta_exceeds_envelope_upward']}, `sign_locks_positive` "
      f"{b3_conj['sign_locks_positive']} (`data/olmo/b3_analysis_dpo.json:conjuncts`). The sham arm's role in "
      f"captures 2 and 3 is the envelope (f1: sham pseudo-Δ; B3: max over sham and random).")
    w("")

    # ---- section 4: why the record classed each an artifact ----
    w("## 4. Why the record classed each an artifact capture (quoted, pinned)")
    w("")
    w("**Capture 1, e2a.** The e2a VERDICT entry, conjunct (2):")
    w("")
    for q in quote(RC, L["e2a_conj2"], L["e2a_conj3"]):
        w(f"> {q}")
    w("")
    w("Restated in the synthesis:")
    w("")
    for q in quote("FINDINGS-3.md", L["f3_start"], L["f3_end"]):
        w(f"> {q}")
    w("")
    w("Basis (Code's paraphrase of the quoted entry): the state arm's map pattern (A positive, B negative) recurs in the arm with no state, so the "
      "pattern cannot be the state's; the counterbalanced pooled Δ absorbs it.")
    w("")
    w("**Capture 2, f1 CORR.** The f1 SCREEN VERDICT entry:")
    w("")
    for q in quote(RC, L["f1_mirror"] - 1, L["f1_mirror"] + 1):
        w(f"> {q}")
    w("")
    w("and the synthesis, which names it the second live capture:")
    w("")
    for q in quote("FINDINGS-4.md", L["f4_point4_start"], L["f4_point4_end"]):
        w(f"> {q}")
    w("")
    w("Basis (Code's paraphrase of the quoted entry): equal-and-opposite map Δs on a contrast whose property is fixed across maps; only the "
      "label-to-property assignment flips, so a map-locked effect is a label effect.")
    w("")
    w("**Capture 3, B3 DPO.** The B3 SCREEN entry:")
    w("")
    for q in quote(R, L["b3_artifact_start"], L["b3_artifact_end"]):
        w(f"> {q}")
    w("")
    w("Basis (Code's paraphrase of the quoted entry): the pooled Δ (+0.0625) is carried by one map while the other is negative, so the "
      "sign-lock conjunct fails; magnitude at rule 12's first-order scale.")
    w("")
    w("**The count of three, and rule 12.**")
    w("")
    for q in quote("PROPOSAL-j-dose-escalation.md", L["propj_three"], L["propj_three"] + 2):
        w(f"> {q}")
    for q in quote("CLAUDE.md", L["claude_rule12"], L["claude_rule12"] + 1):
        w(f"> {q}")
    w("")
    w(f"CLAUDE.md's \"captured live twice\" predates the B3 entry ({R}@{PIN}:{L['b3_head']}, 2026-08-24); PROPOSAL-j's "
      f"\"three live captures across two models\" counts e2a and f1 (Qwen) and B3 DPO (OLMo). Rule 12's text is not "
      f"this audit's to change; the note should say three.")
    w("")

    # ---- section 5: post-hoc decomposition ----
    w("## 5. What the captured artifacts consist of (computed-new; POST-HOC, descriptive, deciding nothing)")
    w("")
    w(f"Rule 11 applies: everything in this section is post-hoc on committed data; it changes no verdict and no "
      f"label. The frame is the record's own: the alternation habit (`valence_core/e2d/habit.py@{PIN}:"
      f"{L['habit_identity']}`, weighted form :{L['habit_weighted']}; \"algebra, not a finding\", :{L['habit_rule11']}). "
      f"Every session in these arms has F = 2 forced rounds per label, alternating, so the last forced label is "
      f"the complement of the start label and the habit predicts that the first free pick returns to the START "
      f"label. Per map, exactly (Fractions; asserted):")
    w("")
    w("    Δ_map = (n_fe− / N − ½)  +  (B₊ − B₋) / N")
    w("")
    w("where n_fe− = sessions whose last forced round was the −label (= sessions that started on the +label; the "
      "habit then picks +), B₊ = habit breaks that picked +, B₋ = habit breaks that picked −. The first term is the "
      "forced-order balance within the map (set by the schedule and by exclusions), the second the net direction of "
      "the habit breaks. The record's `habit.break_rates` (executed from the pinned blob) returns the same Δ in its "
      "weighted form for every row (column 'habit ✓').")
    w("")
    w("| arm | map | N | k₊ | Δ_map | started on + (n_fe−) | forced-order term | breaks to + / to − | net-break term | breaks to pair[0] / pair[1] | follows habit | habit ✓ |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for key, dd in deco.items():
        for m, x in dd.items():
            w(f"| {key} | {m} | {x['N']} | {x['k_plus']} | {d4(x['delta'])} | {x['start_is_plus']} | "
              f"{d4(x['component_forced_end_balance'])} | {x['breaks_to_plus']} / {x['breaks_to_minus']} | "
              f"{d4(x['component_net_breaks'])} | {x['breaks_to_pair0']} / {x['breaks_to_pair1']} | "
              f"{x['follows_habit']}/{x['N']} | {x['habit_weighted_matches']} |")
    w("")
    w("Forced-order balance by map, as scheduled (all launched sessions, from each runner's schedule field: e2a "
      "`start_plus`, f1 `start_P`, B3 session-index parity) and as realized among valid sessions:")
    w("")
    w("| arm | map | launched | launched starting on + | valid | valid starting on + |")
    w("|---|---|---|---|---|---|")
    sched = {}
    for key, recs, arm, maps in (("e2a reward", e2a, "reward", ("A", "B")),
                                 ("e2a sham", e2a, "sham", ("A", "B")),
                                 ("f1 CORR", f1, "CORR", ("A", "B")),
                                 ("f1 sham", f1, "sham", ("A", "B")),
                                 ("B3-dpo marker", olmo["dpo"], "marker", ("0", "1")),
                                 ("B3-dpo sham", olmo["dpo"], "sham", ("0", "1")),
                                 ("B3-dpo random", olmo["dpo"], "random", ("0", "1"))):
        sched[key] = {}
        for m in maps:
            la = [r for r in recs if r["arm"] == arm and r["map"] == m]
            va = [r for r in la if r["valid"]]
            sched[key][m] = {"launched": len(la),
                             "launched_start_plus": sum(1 for r in la if r["start_plus_sched"]),
                             "valid": len(va),
                             "valid_start_plus": sum(1 for r in va if r["start_plus_sched"])}
            x = sched[key][m]
            w(f"| {key} | {m} | {x['launched']} | {x['launched_start_plus']} | {x['valid']} | {x['valid_start_plus']} |")
    J["forced_order_schedule_posthoc"] = sched
    w("")
    pair0_tags = {
        "e2a": sorted({r["pair"][0] for r in e2a}),
        "f1": sorted({r["pair"][0] for r in f1}),
        "B3-dpo": sorted({r["pair"][0] for r in olmo["dpo"]}),
    }
    w(f"Exact tests on the pooled break direction (pair[0] = the first-listed tag of each rotated pair: e2a "
      f"{', '.join(pair0_tags['e2a'])}; f1 {', '.join(pair0_tags['f1'])}; B3 {', '.join(pair0_tags['B3-dpo'])}), "
      f"exact binomial two-sided vs ½ over habit-breaking sessions of the arm (domain: valid sessions that broke the "
      f"habit). This is the pair[0] coordinate pooled over the four pairs; it sums breaks toward four different "
      f"tags, and the per-pair table below shows what it hides:")
    w("")
    w("| arm | breaks to pair[0] / pair[1] (pooled over pairs) | p (exact binomial, two-sided) |")
    w("|---|---|---|")
    for key, dd in deco.items():
        x = dd["pooled"]
        pv = x["breaks_pair0_vs_pair1_p_two_sided"]
        w(f"| {key} | {x['breaks_to_pair0']} / {x['breaks_to_pair1']} | {('%.4f' % pv) if pv is not None else '—'} |")
    w("")
    w("First-free-pick reads by label identity and by menu position (domain: valid sessions of the arm; exact "
      "binomial, two-sided vs ½):")
    w("")
    w("| arm | n | picked pair[0] | p | picked first-listed menu item | p | picked the start label (habit) |")
    w("|---|---|---|---|---|---|---|")
    for key, v in reads.items():
        w(f"| {key} | {v['n']} | {v['pick_pair0']} | {v['pick_pair0_p_two_sided']:.4f} | "
          f"{v['pick_menu_first_listed']} | {v['pick_menu_first_listed_p_two_sided']:.4f} | "
          f"{v['pick_start_label_follows_habit']}/{v['n']} |")
    w("")
    w("Is each capture's arm-level map split distinguishable from sampling noise on its own? Fisher exact, "
      "two-sided, on the 2×2 (map × first pick +label) pooled over the four pairs; and the positive map alone as a "
      "one-arm test (exact binomial P(X ≥ k | n, ½), one-sided, the registered direction). Domain: valid sessions "
      "of the arm, all pairs:")
    w("")
    w("| capture arm | positive map k/n | other map k/n | Fisher two-sided p (maps differ; pooled over pairs) | positive map alone, one-sided exact binomial p |")
    w("|---|---|---|---|---|")
    for key, t in tests.items():
        w(f"| {key} | {t['positive_map']}: {t['k_pos_map']}/{t['n_pos_map']} | {t['other_map']}: "
          f"{t['k_other_map']}/{t['n_other_map']} | {t['fisher_two_sided_map_difference']:.4f} | "
          f"{t['single_map_binom_upper_one_sided']:.4f} |")
    w("")

    # ---- per-pair tables (round-2 values-check, finding 1 and 2) ----
    def pv_s(x):
        return "—" if x is None else (f"{x:.2g}" if x < 0.001 else f"{x:.4f}")

    w("**Per pair, capture arms (post-hoc; added at the round-2 values-check).** Domain: valid sessions of the arm "
      "in that pair. '+label share' is k/n of first picks to the +label in the map whose +label is pair[0] (e2a/f1 "
      "map A, B3 map 0) and in the map whose +label is pair[1] (map B / map 1). 'Started on t: broke/n' counts "
      "sessions that started on tag t and whose first free pick went to the other tag (a habit break), per map in "
      "the same order. p: exact binomial, two-sided vs ½, on first pick = pair[0]; Fisher: exact, two-sided, on the "
      "within-pair 2×2 (map × first pick +label). Every pair of every capture arm is listed, so no pair is selected "
      "silently; the reading below names maple/cedar because of what this table shows, which is a post-hoc "
      "selection (rule 11).")
    w("")
    w("| arm | pair[0]/pair[1] | n | first pick pair[0] : pair[1] | p | +label share, map + = pair[0] | +label share, map + = pair[1] | Fisher p (maps, within pair) | started on pair[0]: broke/n (by map) | started on pair[1]: broke/n (by map) | breaks by tag |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for key, recs, arm, maps in PAIR_ARMS:
        for pk_, v in pp[key].items():
            t0, t1 = pk_.split("/")
            s0 = "; ".join(f"{v['starts'][t0][m]['broke']}/{v['starts'][t0][m]['n']}" for m in maps)
            s1 = "; ".join(f"{v['starts'][t1][m]['broke']}/{v['starts'][t1][m]['n']}" for m in maps)
            bt = ", ".join(f"{t} {c}" for t, c in v["breaks_to_tag"].items())
            w(f"| {key} | {pk_} | {v['n']} | {v['pick_pair0']} : {v['pick_pair1']} | {pv_s(v['pick_pair0_p_two_sided'])} | "
              f"{v['maps'][maps[0]]['k_plus']}/{v['maps'][maps[0]]['n']} | {v['maps'][maps[1]]['k_plus']}/"
              f"{v['maps'][maps[1]]['n']} | {pv_s(v['fisher_two_sided_maps_within_pair'])} | {s0} | {s1} | {bt} |")
    w("")
    ma_ = mc_all
    w(f"**maple/cedar across all ten Qwen arms** ({', '.join(ma_['arms'])}; valid sessions; post-hoc, counts only, "
      f"no test): maple was the first free pick in {ma_['maple_first']}/{ma_['n']} maple/cedar sessions. Sessions "
      f"that started on cedar broke the habit toward maple in {ma_['cedar_start_broke_to_maple']}/"
      f"{ma_['cedar_start_n']}: {ma_['cedar_start_by_map']['A']['broke_to_maple']}/"
      f"{ma_['cedar_start_by_map']['A']['n']} in map A ({ma_['cedar_start_by_map']['A']['label']}) and "
      f"{ma_['cedar_start_by_map']['B']['broke_to_maple']}/{ma_['cedar_start_by_map']['B']['n']} in map B "
      f"({ma_['cedar_start_by_map']['B']['label']}). Sessions that started on maple broke toward cedar in "
      f"{ma_['maple_start_broke_to_cedar']}/{ma_['maple_start_n']}. In the other three pairs, "
      f"{ma_['other_pairs_breaks']}/{ma_['other_pairs_n']} sessions broke the habit at all. The break follows the tag, "
      f"not the pole, in both maps.")
    w("")
    w("**Maps with maple/cedar removed, and maple/cedar alone (Qwen capture arms; post-hoc).** Δ = k/n − ½ over "
      "valid sessions of the arm and map in the other three pairs; breaks to + / to − in the same domain; the "
      "maple/cedar sessions alone pooled over both maps; and how many of the arm's breaks toward pair[0] (all pairs) "
      "went to maple:")
    w("")
    w("| arm | map A k/n → Δ (no maple/cedar) | map B k/n → Δ (no maple/cedar) | opposite-signed | breaks to + / to − (A; B) | p (breaks + vs −, pooled over maps, exact binomial two-sided) | maple/cedar alone, pooled over maps | pair[0] breaks that went to maple |")
    w("|---|---|---|---|---|---|---|---|")
    for key in nomc:
        d = nomc[key]
        A_, B_ = d["maps"]["A"], d["maps"]["B"]
        mcp = d["maple_cedar_pooled_over_maps"]
        w(f"| {key} | {A_['k']}/{A_['n']} → {d4(A_['delta'])} | {B_['k']}/{B_['n']} → {d4(B_['delta'])} | "
          f"{'yes' if d['opposite_signed'] else 'no'} | {A_['breaks_to_plus']} / {A_['breaks_to_minus']}; "
          f"{B_['breaks_to_plus']} / {B_['breaks_to_minus']} | {pv_s(d['breaks_plus_vs_minus_without_mc_p_two_sided'])} | "
          f"{mcp['k']}/{mcp['n']} → {d4(mcp['delta'])} | {d['pair0_breaks_that_are_maple']} of {d['pair0_breaks']} |")
    w("")
    w("**B3 DPO marker, map 1 (the +0.1667 map) by pair (post-hoc).** Started on the +label = the forced-order term's "
      "numerator; map-1 breaks to + = its net-break term's positive part:")
    w("")
    w("| pair | map-1 +label | n | started on +label | of those, first pick = +label | map-1 breaks to + |")
    w("|---|---|---|---|---|---|")
    for pk_, v in b3_map1.items():
        w(f"| {pk_} | {v['plus_tag']} | {v['n']} | {v['started_on_plus']} | {v['started_on_plus_and_picked_it']} | "
          f"{v['breaks_to_plus']} |")
    w("")
    h3_cl = ", ".join(f"{k} {v['tag_lo']}/{v['tag_hi']}" for k, v in h3_c.items())
    w(f"**The record's own identity measurement on Qwen: the H3 tag screen** ({R}@{PIN}:{L['h3_head']}, 2026-08-20, "
      f"after e2a's verdict at {RC}@{PIN}:{L['e2a_verdict_head']} and f1's at :{L['f1_verdict_head']}; table row "
      f":{L['h3_c2']}). `data/e2b/h3_tagscreen.json` at the pin, scaffold format (the format of record), "
      f"n = {h3_c2['n']} restricted-choice probes per pair with menu order alternated; `identity_split` is the "
      f"share taken by `tag_lo`, the alphabetically first tag (valence_core/tagscreen.py@{PIN}:{L['tagscreen_doc']}); "
      f"band {h3_band['centre']} ± {h3_band['halfwidth']}. Its C pairs ({h3_cl}) are exactly e2a's and f1's four "
      f"pairs (asserted). Recomputed from the per-probe rows with tagscreen's formula:")
    w("")
    w("| H3 pair | tag_lo / tag_hi | identity_split (stored) | recomputed | match | imbalance | in band | tag_hi's share |")
    w("|---|---|---|---|---|---|---|---|")
    for k, v in h3_c.items():
        inb = abs(v["identity_split"] - h3_band["centre"]) <= h3_band["halfwidth"]
        w(f"| {k} | {v['tag_lo']} / {v['tag_hi']} | {v['identity_split']:.4f} | {v['identity_split_recomputed']:.4f} | "
          f"{'YES' if v['recomputed_matches'] else 'NO'} | {v['imbalance']:.4f} | {'yes' if inb else 'no'} | "
          f"{1 - v['identity_split']:.4f} |")
    w("")
    J["per_pair_posthoc"] = pp
    J["maple_cedar_all_qwen_arms_posthoc"] = mc_all
    J["maps_without_maple_cedar_posthoc"] = nomc
    J["b3_dpo_marker_map1_by_pair_posthoc"] = {"by_pair": b3_map1,
                                               "map1_breaks_to_plus_tags": b3_map1_plus_break_tags}
    J["h3_tagscreen_c_pairs"] = {"rows": h3_c, "c2_is_largest_imbalance_of_c_pairs": h3_c2_worst,
                                 "band": h3_band}
    J["n5_cross_reference_corr_delivery"] = n5_xref

    # every post-hoc exact test in this section, counted
    ph = []
    for key, dd in deco.items():
        pv = dd["pooled"]["breaks_pair0_vs_pair1_p_two_sided"]
        if pv is not None:
            ph.append((f"{key} breaks pair[0] vs pair[1]", pv))
    for key, v in reads.items():
        ph.append((f"{key} first pick = pair[0]", v["pick_pair0_p_two_sided"]))
        ph.append((f"{key} first pick = first-listed menu item", v["pick_menu_first_listed_p_two_sided"]))
    for key, t in tests.items():
        ph.append((f"{key} Fisher maps differ", t["fisher_two_sided_map_difference"]))
        ph.append((f"{key} positive map alone", t["single_map_binom_upper_one_sided"]))
    # round-2 additions: every pair of every capture arm, and the no-maple/cedar break tests
    for key in pp:
        for pk_, v in pp[key].items():
            ph.append((f"{key} {pk_} first pick = pair[0]", v["pick_pair0_p_two_sided"]))
            if v["fisher_two_sided_maps_within_pair"] is not None:
                ph.append((f"{key} {pk_} Fisher maps differ (within pair)",
                           v["fisher_two_sided_maps_within_pair"]))
    for key, d in nomc.items():
        if d["breaks_plus_vs_minus_without_mc_p_two_sided"] is not None:
            ph.append((f"{key} breaks + vs − without maple/cedar",
                       d["breaks_plus_vs_minus_without_mc_p_two_sided"]))
    ph_low = [(nm, pv) for nm, pv in ph if pv < 0.05]
    J["posthoc_tests_count"] = {"n_tests": len(ph), "below_0.05": ph_low}

    def sgn(x):
        return f"({d4(x)})"

    dm = deco["B3-dpo marker"]["1"]
    ea = deco["e2a reward"]["A"]
    es = deco["e2a sham"]
    fc = deco["f1 CORR"]
    w("**Reading (post-hoc, descriptive).**")
    w("")
    w(f"- In every capture arm the first free pick follows the alternation habit in most sessions: "
      + "; ".join(f"{k_} {deco[k_]['pooled']['follows_habit']}/{deco[k_]['pooled']['N']}"
                  for k_ in ("e2a reward", "e2a sham", "f1 CORR", "B3-dpo marker")) +
      ". A map's Δ therefore moves with two small quantities: which label the map's sessions started on, and which "
      "way the few habit breaks went.")
    w(f"- **Qwen captures (e2a, f1).** e2a reward map A {d4(ea['delta'])} = {sgn(ea['component_forced_end_balance'])} "
      f"(forced order) + {sgn(ea['component_net_breaks'])} (net breaks, {ea['breaks_to_plus']} to + vs "
      f"{ea['breaks_to_minus']} to −). e2a sham map A {d4(es['A']['delta'])} = "
      f"{sgn(es['A']['component_forced_end_balance'])} + {sgn(es['A']['component_net_breaks'])}; map B "
      f"{d4(es['B']['delta'])} = {sgn(es['B']['component_forced_end_balance'])} + "
      f"{sgn(es['B']['component_net_breaks'])} (breaks {es['B']['breaks_to_plus']} to + vs "
      f"{es['B']['breaks_to_minus']} to −). f1 CORR map A {d4(fc['A']['delta'])} = "
      f"{sgn(fc['A']['component_forced_end_balance'])} + {sgn(fc['A']['component_net_breaks'])}; map B "
      f"{d4(fc['B']['delta'])} = {sgn(fc['B']['component_forced_end_balance'])} + "
      f"{sgn(fc['B']['component_net_breaks'])}. The positive map (A) of the state arm and of CORR is carried mostly "
      f"by the net-break term. In the e2a sham the forced-order term is positive in both maps because its schedule "
      f"started more sessions on the +label in both (launched {sched['e2a sham']['A']['launched_start_plus']}/"
      f"{sched['e2a sham']['A']['launched']} and {sched['e2a sham']['B']['launched_start_plus']}/"
      f"{sched['e2a sham']['B']['launched']}; {sum(1 for r in e2a if r['arm'] == 'sham')} launched sessions, not a "
      f"multiple of the 16-session (map x start) cycle); its map B goes negative through the breaks.")
    # --- round-2 rewrite (values-check finding 1): what carries the Qwen map splits ---
    import datetime as _dt
    h3_date = pinned_lines(R)[L["h3_head"] - 1].split("— **")[0].strip(" -")
    f1_date = pinned_lines(RC)[L["f1_verdict_head"] - 1].split("— **")[0].strip(" -")
    e2a_date = pinned_lines(RC)[L["e2a_verdict_head"] - 1].split("— **")[0].strip(" -")
    h3_lag = (_dt.date.fromisoformat(h3_date) - _dt.date.fromisoformat(f1_date)).days
    QK = ("e2a reward", "e2a sham", "f1 CORR", "f1 sham")
    QC = ("e2a reward", "e2a sham", "f1 CORR")
    mcr = {k_: pp[k_]["maple/cedar"] for k_ in QK}
    q_other_f = [v["fisher_two_sided_maps_within_pair"] for k_ in QK for pk_, v in pp[k_].items()
                 if pk_ != "maple/cedar" and v["fisher_two_sided_maps_within_pair"] is not None]
    q_other_min = min(q_other_f)
    assert all(mcr[k_]["fisher_two_sided_maps_within_pair"] < 0.05 for k_ in QK)
    assert q_other_min >= 0.05
    apos_bneg_left = [k_ for k_ in QC if nomc[k_]["maps"]["A"]["delta"] > 0 and nomc[k_]["maps"]["B"]["delta"] < 0]
    assert not apos_bneg_left
    er_mc = pp["e2a reward"]["maple/cedar"]
    er_tot = deco["e2a reward"]["pooled"]["breaks_to_plus"] + deco["e2a reward"]["pooled"]["breaks_to_minus"]
    er_mc_br = sum(er_mc["breaks_to_tag"].values())
    assert er_mc["breaks_to_tag"]["cedar"] == 0 and er_mc_br == er_mc["breaks_to_tag"]["maple"]
    er_nm = nomc["e2a reward"]
    es_nm = nomc["e2a sham"]["maps"]
    fc_nm = nomc["f1 CORR"]["maps"]
    w(f"- **What carries the Qwen map splits: one tag pair (maple/cedar).** Pooled over the four pairs, the habit "
      f"breaks lean toward pair[0] ("
      + "; ".join(f"{k_} {deco[k_]['pooled']['breaks_to_pair0']} vs {deco[k_]['pooled']['breaks_to_pair1']}"
                  for k_ in QK) +
      "; no count significant on its own), but the pair[0] coordinate sums breaks toward four different tags, and "
      "the per-pair table shows one tag doing the work: of those pair[0] breaks, maple took "
      + ", ".join(f"{nomc[k_]['pair0_breaks_that_are_maple']} of {nomc[k_]['pair0_breaks']} ({k_})" for k_ in QK) +
      ". Maple was the first free pick in "
      + ", ".join(f"{mcr[k_]['pick_pair0']}/{mcr[k_]['n']} ({k_})" for k_ in QK) +
      " of these arms' maple/cedar sessions, so within maple/cedar the maps split hard (+label share in map A, "
      "where maple = +, vs map B, where maple = −: "
      + "; ".join(f"{k_} {mcr[k_]['maps']['A']['k_plus']}/{mcr[k_]['maps']['A']['n']} vs "
                  f"{mcr[k_]['maps']['B']['k_plus']}/{mcr[k_]['maps']['B']['n']}, Fisher two-sided p = "
                  f"{pv_s(mcr[k_]['fisher_two_sided_maps_within_pair'])}" for k_ in QK) +
      f"); no other pair's within-pair split in these four arms reaches .05 (smallest p = {q_other_min:.4f}). Across "
      f"all ten Qwen arms the break follows the tag, not the pole (paragraph above the maple/cedar-removed table). "
      f"With maple/cedar removed, the A-positive/B-negative pattern is gone from all three captures (e2a reward A "
      f"{d4(er_nm['maps']['A']['delta'])} / B {d4(er_nm['maps']['B']['delta'])}; e2a sham A "
      f"{d4(es_nm['A']['delta'])} / B {d4(es_nm['B']['delta'])}, opposite-signed the other way at n = "
      f"{es_nm['A']['n']}/{es_nm['B']['n']}; f1 CORR A {d4(fc_nm['A']['delta'])} / B {d4(fc_nm['B']['delta'])}). "
      f"The Qwen label artifact is therefore a measured tag-identity imbalance, maple over cedar, concentrated in "
      f"one pair of four. The record measured that imbalance on Qwen, on restricted-choice probes rather than "
      f"sessions, on {h3_date} ({h3_lag} days after f1's verdict of {f1_date}): H3's C2 maple/cedar, identity_split "
      f"{h3_c2['identity_split']:.4f} (cedar's "
      f"share; maple {1 - h3_c2['identity_split']:.4f}), imbalance {h3_c2['imbalance']:.4f} against the "
      f"±{h3_band['halfwidth']} band, "
      + ("the largest of e2a/f1's four pairs" if h3_c2_worst else "not the largest of e2a/f1's four pairs") +
      f" ({R}@{PIN}:{L['h3_c2']}; recomputed above). The label-map counterbalance turns the prior into "
      f"opposite-signed maps and cancels most of it in the pooled Δ (maple/cedar sessions alone, pooled over maps: "
      + ", ".join(f"{k_} {nomc[k_]['maple_cedar_pooled_over_maps']['k']}/{nomc[k_]['maple_cedar_pooled_over_maps']['n']}"
                  f" → {d4(nomc[k_]['maple_cedar_pooled_over_maps']['delta'])}" for k_ in QK) +
      f"; the cancellation is exact only in expectation), which is the mechanism the record states for OLMo's prism "
      f"prior: 'Only the label-MAP swap ... can absorb it' ({R}@{PIN}:{L['mapswap']}-{L['mapswap_end']}).")
    w(f"- **The state arm, separated by pair.** Of e2a reward's {er_tot} habit breaks, {er_mc_br} are maple/cedar "
      f"sessions that started on cedar and broke to maple ({er_mc['breaks_to_plus_by_map']['A']} toward + in map A, "
      f"{er_mc['breaks_to_minus_by_map']['B']} toward − in map B). Outside maple/cedar its breaks go "
      f"{er_nm['maps']['A']['breaks_to_plus']} to + vs {er_nm['maps']['A']['breaks_to_minus']} to − in map A and "
      f"{er_nm['maps']['B']['breaks_to_plus']} vs {er_nm['maps']['B']['breaks_to_minus']} in map B: toward + in both "
      f"maps, the direction a state effect would take, at {er_nm['breaks_plus_vs_minus_without_mc'][0]} vs "
      f"{er_nm['breaks_plus_vs_minus_without_mc'][1]} (exact binomial, two-sided, p = "
      f"{pv_s(er_nm['breaks_plus_vs_minus_without_mc_p_two_sided'])}), too few to read. On the other three pairs both "
      f"state-arm maps are ≥ 0 ({d4(er_nm['maps']['A']['delta'])}, {d4(er_nm['maps']['B']['delta'])}): a subset "
      f"chosen after seeing the data, which re-reads no conjunct and moves no verdict (rule 11); conjunct (1), the "
      f"envelope, and conjunct (3), the binomial, failed on the full arm regardless (section 3; "
      f"{RC}@{PIN}:{L['e2a_conj1']}-{L['e2a_conj3']}). The sham's no-state breaks toward pair[0] (A {es['A']['breaks_to_pair0']} vs "
      f"{es['A']['breaks_to_pair1']}, B {es['B']['breaks_to_pair0']} vs {es['B']['breaks_to_pair1']}) are maple's "
      f"({nomc['e2a sham']['pair0_breaks_that_are_maple']} of {nomc['e2a sham']['pair0_breaks']}), which is the "
      f"record's disambiguating observation (the same pattern in sham) in decomposed form: the same tag prior in an "
      f"arm with no state.")

    # --- round-2 rewrite (values-check finding 2): B3 DPO per pair ---
    def tag_breaks_by_map(row, maps):
        t0, t1 = row["pair"].split("/")
        out = []
        for t, other in ((t0, t1), (t1, t0)):
            parts = []
            for m in maps:
                c = row["starts"][other][m]["broke"]
                if c:
                    parts.append(f"{c} to {'+' if row['maps'][m]['plus_tag'] == t else '−'} in map {m}")
            if parts:
                out.append((t, ", ".join(parts), sum(row["starts"][other][m]["broke"] for m in maps)))
        return out

    b3m = pp["B3-dpo marker"]
    b3_one_way = []
    b3_both_maps = []
    for pk_, v in b3m.items():
        tb = tag_breaks_by_map(v, ("0", "1"))
        tot = sum(v["breaks_to_tag"].values())
        if tot:
            assert len(tb) == 1, pk_          # every pair's breaks go to one tag
            b3_one_way.append(f"{tb[0][0]} {tb[0][2]}/{tot} ({pk_})")
            if "map 0" in tb[0][1] and "map 1" in tb[0][1]:
                b3_both_maps.append(f"{tb[0][0]}: {tb[0][1]}")
    b3_tot_breaks = sum(sum(v["breaks_to_tag"].values()) for v in b3m.values())
    b3_p0_recv = sorted({v["pair"].split("/")[0] for v in b3m.values()
                         if v["breaks_to_tag"][v["pair"].split("/")[0]]})
    ag = b3_map1["amber/granite"]
    assert ag["started_on_plus"] == ag["n"] == ag["started_on_plus_and_picked_it"]
    oth_sp = sum(v["started_on_plus"] for k_, v in b3_map1.items() if k_ != "amber/granite")
    oth_n = sum(v["n"] for k_, v in b3_map1.items() if k_ != "amber/granite")
    assert b3_map1_plus_break_tags == ["velvet"] and b3_map1["quartz/velvet"]["breaks_to_plus"] == dm["breaks_to_plus"]
    w(f"- **OLMo capture (B3 DPO).** The +0.1667 map is carried mostly by the forced-order term: {dm['start_is_plus']} "
      f"of its {dm['N']} valid sessions started on the +label, giving {d4(dm['component_forced_end_balance'])} before "
      f"any break, and the net breaks add {d4(dm['component_net_breaks'])} ({dm['breaks_to_plus']} to + vs "
      f"{dm['breaks_to_minus']} to −). Map 1's forced-order imbalance is concentrated in one pair: all "
      f"{ag['n']} of amber/granite's valid map-1 sessions started on {ag['plus_tag']} (= +label) and picked it, "
      f"against {oth_sp}/{oth_n} starting on + in the other three pairs (table above). Read per pair, all "
      f"{b3_tot_breaks} marker breaks (both maps) run one way within their pair: {', '.join(b3_one_way)}, which the "
      f"pooled pair[0] coordinate ({' and '.join(b3_p0_recv)} are pair[0]) reads as "
      f"{deco['B3-dpo marker']['pooled']['breaks_to_pair0']} vs {deco['B3-dpo marker']['pooled']['breaks_to_pair1']}; "
      f"the {dm['breaks_to_plus']} map-1 breaks to the +label are all {b3_map1_plus_break_tags[0]}'s, and the tags "
      f"that broke in both maps follow the tag, not the pole ({'; '.join(b3_both_maps)}). B3's start label is set by "
      f"the parity of the arm's running session index "
      f"(`scripts/box_b3_sessions.py@{PIN}:{L['b3_order']}`), while the cell (pair, map) comes from a seeded shuffle "
      f"of the schedule, so within-map start balance is not enforced (launched marker map 1: "
      f"{sched['B3-dpo marker']['1']['launched_start_plus']}/{sched['B3-dpo marker']['1']['launched']} starting on +). "
      f"e2a and f1 tie the start to s // 8 and the map to s // 4 (`{E2A_RUN}:{e2a_start}`, `{F1_RUN}:{f1_start}`), "
      f"balanced per map in every 16 consecutive sessions. On this decomposition the DPO excursion is mostly a "
      f"forced-order (start-label) imbalance under the alternation habit (forced-order term "
      f"{d4(dm['component_forced_end_balance'])} against a net-break term of {d4(dm['component_net_breaks'])}), and "
      f"the residual break term is tag-specific ({b3_map1_plus_break_tags[0]}), not absent. The record's "
      f"conclusion -- an artifact, not a state effect -- is unaffected: the forced-order term is set by "
      f"the schedule and by which sessions were excluded (map 1: launched "
      f"{sched['B3-dpo marker']['1']['launched_start_plus']}/{sched['B3-dpo marker']['1']['launched']}, valid "
      f"{sched['B3-dpo marker']['1']['valid_start_plus']}/{sched['B3-dpo marker']['1']['valid']} starting on +), "
      f"not by the first free choice; and the net-break term, which is where a state effect on the choice would "
      f"appear, is {d4(dm['component_net_breaks'])} in map 1 ({dm['breaks_to_plus']} vs "
      f"{dm['breaks_to_minus']}) and {d4(deco['B3-dpo marker']['0']['component_net_breaks'])} in map 0 "
      f"({deco['B3-dpo marker']['0']['breaks_to_plus']} vs {deco['B3-dpo marker']['0']['breaks_to_minus']}), its "
      f"breaks following tags rather than the +pole. Whether the note says 'label' or 'order' artifact is the design "
      f"seat's wording.")
    all_f_ns = all(tests[k_]["fisher_two_sided_map_difference"] >= 0.05 for k_ in tests)
    all_s_ns = all(tests[k_]["single_map_binom_upper_one_sided"] >= 0.05 for k_ in tests)
    b3_low = sorted(pk_ for pk_, v in b3m.items() if v["fisher_two_sided_maps_within_pair"] is not None
                    and v["fisher_two_sided_maps_within_pair"] < 0.05)
    assert b3_low == ["amber/granite", "quartz/velvet"], b3_low
    ag_row = b3m["amber/granite"]
    ag_gran_starts = sum(ag_row["starts"]["granite"][m]["n"] for m in ("0", "1"))
    qv_row = b3m["quartz/velvet"]
    w(("- Taken one at a time, no capture's arm-level map split -- the test pooled over the four pairs -- is "
       "distinguishable from sampling noise at .05 "
       if all_f_ns else "- Taken one at a time, NOT every capture's arm-level map split is within sampling noise ")
      + "(Fisher two-sided p: "
      + ", ".join(f"{k_} {tests[k_]['fisher_two_sided_map_difference']:.3f}" for k_ in tests) +
      "). On Qwen that pooled test dilutes a within-pair effect that is distinguishable: maple/cedar's within-pair "
      "splits (Fisher p "
      + ", ".join(f"{pv_s(mcr[k_]['fisher_two_sided_maps_within_pair'])} {k_}" for k_ in QC) +
      "), with the same tag prior measured independently by H3's C2. So on Qwen 'label artifact' names a "
      "demonstrated within-campaign effect, a tag-identity prior, whose arm-level consequence (opposite-signed "
      "maps) the map counterbalance absorbs; what no single campaign demonstrates is a map effect pooled over "
      f"pairs. At B3 DPO the within-pair splits below .05 (amber/granite p = "
      f"{pv_s(ag_row['fisher_two_sided_maps_within_pair'])}, quartz/velvet p = "
      f"{pv_s(qv_row['fisher_two_sided_maps_within_pair'])}) are, respectively, the start schedule "
      f"({ag_gran_starts} of amber/granite's {ag_row['n']} sessions started on granite) and velvet's breaks "
      f"({qv_row['breaks_to_tag']['velvet']} of {sum(qv_row['breaks_to_tag'].values())}). The record classed all "
      "three captures by pattern and by the counterbalance's logic, not by a test; the preprint's 'caught by "
      "structure rather than by suspicion' remains the accurate description of how they were caught. The "
      "within-pair p values come from a table built after the pattern was seen (rule 11) and are descriptive.")
    w(("- A single-map design at the positive map's own n would not have crossed one-sided α = .05 in any capture "
       if all_s_ns else "- A single-map design at the positive map's own n would have crossed one-sided α = .05 in at "
       "least one capture ")
      + "(exact binomial, one-sided: "
      + ", ".join(f"{k_} {tests[k_]['single_map_binom_upper_one_sided']:.3f}" for k_ in tests) +
      "). FINDINGS-3's 'an uncounterbalanced, sham-less version of this experiment would have published [it] as "
      "approach behavior' is a counterfactual about a full-n single-map run; it is not computable from these data "
      "and is not tested here.")
    w(f"- Multiplicity: this section ran {len(ph)} post-hoc exact tests, uncorrected; "
      f"{len(ph_low)} fall below .05 ("
      + ("; ".join(f"{nm} p = {pv_s(pv)}" for nm, pv in ph_low) if ph_low else "none") +
      "). They are descriptive only and license nothing.")
    w("")

    # ---- section 6: context ----
    w("## 6. Context: every arm's map split in the three campaigns (computed-new count; stored maps re-verified)")
    w("")
    w("| campaign | arm | maps (k/n → Δ) | opposite-signed | max abs map Δ | source |")
    w("|---|---|---|---|---|---|")
    for r in context:
        ms = "; ".join(f"{m}: {v['k']}/{v['n']} → {d4(v['delta'])}" + ("" if v.get("match", True) else " (MISMATCH vs stored)")
                       for m, v in r["maps"].items())
        w(f"| {r['campaign']} | {r['arm']} | {ms} | {'yes' if r['opposite_signed'] else 'no'} | "
          f"{r['max_abs_map_delta']:.4f} | `{r['source']}` |")
    w("")
    all_map_n = [v["n"] for r in context for v in r["maps"].values()]
    max_abs = max(r["max_abs_map_delta"] for r in context)
    max_cell = [r for r in context if r["max_abs_map_delta"] == max_abs][0]
    r1 = [r for r in context if r["campaign"] == "e2a" and r["arm"] == "random1"][0]
    w(f"Of {n_ctx} arm-campaign cells, {n_opp} have opposite-signed maps (one map > 0, the other < 0) and {n_ge10} "
      f"have a map with abs(Δ_map) ≥ 0.10 (exact Fractions; {len(at_tenth)} cell"
      f"{'' if len(at_tenth) == 1 else 's'} exactly at 0.10 -- {', '.join(at_tenth) or 'none'}; {n_gt10}/{n_ctx} "
      f"with abs(Δ_map) > 0.10 strictly). Every stored map value re-verified from the session records: "
      f"{'YES' if all_ctx_match else 'NO'}. Per-map valid n in these cells runs {min(all_map_n)}-{max(all_map_n)}; "
      f"the largest single-map abs(Δ) is {max_abs:.4f} ({max_cell['campaign']} {max_cell['arm']}). Opposite-signed "
      f"maps and single-map excursions of 0.10 or more are common at these n, in arms with and without a state. "
      f"That is consistent with PROPOSAL-j's \"A fourth capture is expected and is not a finding\" "
      f"(PROPOSAL-j-dose-escalation.md@{PIN}:{L['propj_three'] + 2}), which itself rests the expectation only on "
      f"the three captures (:{L['propj_three']}); the {n_ctx}-cell count is this audit's computed-new, not the "
      f"record's basis. The three named captures are the ones the "
      f"record discussed, not the only cells with that shape: e.g. e2a random1 (map A {d4(r1['maps']['A']['delta'])}, "
      f"map B {d4(r1['maps']['B']['delta'])}) has one map carrying the pooled Δ at a larger magnitude than B3 DPO, and "
      f"the record read random1's pooled +0.152 as \"noise doing its criterion job\" "
      f"({RC}@{PIN}:{L['e2a_random1_noise']}-{L['e2a_random1_noise'] + 1}).")
    w("")

    # ---- notes ----
    w("## 7. Notes (referents and wording; none is a STOP)")
    w("")
    w(f"1. **The heading 'sham-arm pseudo-statistics' fits capture 1 only.** f1 CORR is a contrast arm and B3 DPO "
      f"the marker arm (sections 1, 3). The three are the record's label-artifact captures "
      f"(PROPOSAL-j-dose-escalation.md@{PIN}:{L['propj_three']}); the sham arm's own map split for f1 and B3 is "
      f"reported beside them as computed-new.")
    PP = "PREPRINT-v1_0-draft.md"
    pp_sha = sha256_file(PP) if os.path.exists(os.path.join(REPO, PP)) else None
    pp_ok = bool(pp_sha) and pp_sha.startswith("d6431e97") and pp_sha.endswith("222b8")
    pp_ident = local_find(PP, "appears identically in the sham arm (+0.111 / −0.079)") if pp_sha else None
    pp_constr = local_find(PP, "cancelled to 0.000 by construction") if pp_sha else None
    pp_dpo = local_find(PP, "In the OLMo DPO screen one map returned +0.1667.") if pp_sha else None
    J["preprint_working_tree"] = {"path": PP, "sha256": pp_sha, "matches_block_sha": pp_ok,
                                  "lines": {"identically": pp_ident, "by_construction": pp_constr,
                                            "dpo_single_map": pp_dpo}}
    w(f"2. **Preprint wording ({PP}, untracked working-tree file, sha256 {pp_sha}, "
      f"{'equal to' if pp_ok else 'NOT equal to'} the block's d6431e97...222b8; line numbers are working-tree, not "
      f"pinned; PREPRINT-v1_1-draft.md and the note are absent from this machine).** "
      f"(a) :{pp_ident} 'appears identically in the sham arm' -- the sign pattern recurs; the magnitudes do not (state B "
      f"{d4(e2a_an['reward']['by_map']['B'])} vs sham B {d4(e2a_an['sham']['by_map']['B'])}). FINDINGS-3's "
      f"'identical pattern' has the same scope. Suggested: 'the same A-positive/B-negative pattern'. (b) 'cancelled to "
      f"0.000 by construction' (:{pp_constr}) -- the pooling is by construction; the exact zero is the realized counts "
      f"({corr_A['k']}/{corr_A['n']} and {corr_B['k']}/{corr_B['n']}; section 1). The record's own wording is "
      f"'absorbed by design' ({RC}@{PIN}:{L['f1_mirror']}). (c) :{pp_dpo} 'In the OLMo DPO screen one map returned +0.1667' "
      f"-- reproduced; the other map is {d4(an['by_label_map']['0']['delta'])} ({an['by_label_map']['0']['k']}/"
      f"{an['by_label_map']['0']['n']}).")
    fcr, fcp = reads["f1 CORR"], deco["f1 CORR"]["pooled"]
    w(f"3. **PROPOSAL-h §1 cites the f1 mirror-cancel as the 'receipt' that the map counterbalance absorbs the "
      f"injected vector's token-level logit leak** (PROPOSAL-h-state-present-choice.md@{PIN}:{L['proph_leak']}-"
      f"{L['proph_receipt']}). f1 injected nothing in any arm (section 2 locators). What the receipt does show: a "
      f"label-locked lean with no state behind it cancels under the map swap, which is the structural property §1 "
      f"relies on (a push that lands on the same token for opposite meanings). f1 CORR's opposite-signed maps are, "
      f"by construction, a lean toward the pair's first-listed tag in both maps: the first free pick went to "
      f"pair[0] in {fcr['pick_pair0']}/{fcr['n']} valid sessions (exact binomial, two-sided vs ½, p = "
      f"{fcr['pick_pair0_p_two_sided']:.4f}) and its habit breaks went {fcp['breaks_to_pair0']} vs "
      f"{fcp['breaks_to_pair1']} toward pair[0] (section 5; part of map B's excursion is the forced-order term, "
      f"{d4(deco['f1 CORR']['B']['component_forced_end_balance'])}). The lean is one tag's: maple was the first "
      f"pick in {pp['f1 CORR']['maple/cedar']['pick_pair0']}/{pp['f1 CORR']['maple/cedar']['n']} of CORR's "
      f"maple/cedar sessions and took {nomc['f1 CORR']['pair0_breaks_that_are_maple']} of the "
      f"{nomc['f1 CORR']['pair0_breaks']} pair[0] breaks (section 5, per-pair table), so the receipt is a tag-identity "
      f"prior cancelling, which is the same structural property. What it does not show is the size or form of "
      f"a vector-borne push; §1 itself assigns that calibration to H1 (:{L['proph_h1']}, \"H1 measures the "
      f"residual\"). A design-seat note on the receipt's scope, not a record error in any figure.")
    r12 = git("log", PIN, "--format=%h %ad", "--date=short", "-S", "captured live twice", "--",
              "CLAUDE.md").strip().splitlines()
    b3e = git("log", PIN, "--format=%h %ad", "--date=short", "-S",
              "B3 SCREEN COMPLETE, ALL FOUR STAGES", "--", "RESULTS.md").strip().splitlines()
    J["rule12_vs_b3_commits"] = {"rule12_text_commits": r12, "b3_entry_commits": b3e}
    w(f"4. **Rule 12's 'captured live twice'** (CLAUDE.md@{PIN}:{L['claude_rule12']}-{L['claude_rule12'] + 1}) "
      f"predates capture 3: `git log -S` puts the phrase into CLAUDE.md at {', '.join(r12) or '(none)'} and the B3 "
      f"entry into RESULTS.md at {', '.join(b3e) or '(none)'}. PROPOSAL-j's three is current (section 4).")
    w(f"5. **The ~0.10 scale.** Largest |Δ_map| per capture arm: e2a reward "
      f"{max(abs(c['delta']) for c in cells if c['campaign'] == 'e2a' and c['arm'] == 'reward'):.4f}, e2a sham "
      f"{max(abs(c['delta']) for c in cells if c['campaign'] == 'e2a' and c['arm'] == 'sham'):.4f}, f1 CORR "
      f"{max(abs(c['delta']) for c in cells if c['campaign'] == 'f1' and c['arm'] == 'CORR'):.4f}, B3 DPO marker "
      f"{max(abs(c['delta']) for c in cells if c['campaign'] == 'B3-dpo' and c['arm'] == 'marker'):.4f}. "
      f"'Δ ≈ 0.10 scale' fits the Qwen captures; the OLMo map is 0.1667, which the B3 entry calls 'the size rule 12 "
      f"names as first-order (~0.10)'. At n = 24 per map one session moves a map Δ by {1/24:.4f}. The ~0.10 itself is "
      f"a prose scale in the record (FINDINGS-3.md@{PIN}:{L['f3_tenth']}, RESULTS.md@{PIN}:{L['b3_tenth']}, "
      f"CLAUDE.md@{PIN}:{L['claude_tenth']}, PROPOSAL-j-dose-escalation.md@{PIN}:{L['propj_three']}), not a stored "
      f"field; only the per-arm maxima above are this audit's.")
    w(f"6. **Cross-reference.** The e2a figures here are the same fields N4 reproduces "
      f"(`results/raw/2026-10-08_note-N4-e2a.md`, section (i-f)); the f1 pooled CORR figure is N5's; the B3 DPO "
      f"figures are N7's. This raw recomputes all of them independently from the pinned session records. f1 CORR's "
      f"delivery: N5 section 7 ('The CORR contrast's dose', `results/raw/2026-10-08_note-N5-f1.md`, a sibling raw of "
      f"this audit, not at the pin) reports that at rate .12 two of the 16 CORR items rendered unchanged, so clean "
      f"text reached some corrupted-label rounds; this script's check of the stored task field (stored at most "
      f"{n5_xref['stored_task_field_max_len']} characters; equal to a `CORR_clean` item of `data/f/pools.json` on "
      f"that prefix) agrees: {n5_xref['q_rounds_clean_prefix']} of {n5_xref['q_rounds']} Q rounds across all "
      f"{n5_xref['corr_sessions']} CORR sessions, items {n5_xref['clean_items']}, and "
      f"{n5_xref['valid_with_one_clean_forced_q']} of the {n5_xref['valid_sessions']} valid sessions saw one "
      f"corrupted forced task rather than two. It moves no figure here; the CORR map split is maple-carried "
      f"(section 5).")
    w(f"7. **For the PI and the design seat (post-hoc throughout; no verdict moves).** The note's 'what the shields "
      f"caught' can name the Qwen source concretely: a maple-over-cedar identity prior in one of e2a's and f1's four "
      f"pairs (section 5), the prior the record measured independently with H3 (C2, {R}@{PIN}:{L['h3_c2']}). The H3 "
      f"entry's 'no published preference number is impeached by an identity prior on its own tags' "
      f"({R}@{PIN}:{L['h3_noimpeach']}-{L['h3_noimpeach_end']}) rests on slate/prism alone (its basis, "
      f":{L['h3_basis']}-{L['h3_noimpeach']}), while e2a's and f1's rosters also carried maple/cedar, "
      f"'order-counterbalanced but never screened' and 'not admitted' "
      f"(PROPOSAL-j-dose-escalation.md@{PIN}:{L['propj_e2a_pairs']}-{L['propj_not_admitted']}). The pooled Δs stand: "
      f"they are map-counterbalanced, and e2a and f1 are nulls. What the prior did is produce the opposite-signed "
      f"maps the record called the label artifact, and leave the maple/cedar sessions' first picks near-fixed by the "
      f"tag (maple {pp['e2a reward']['maple/cedar']['pick_pair0']}/{pp['e2a reward']['maple/cedar']['n']} in the "
      f"state arm), the case the record's OLMo entry describes as a prior that 'spends power the contrast needs' "
      f"({R}@{PIN}:{L['mapswap_end']}-{L['spends_power']}). Whether the H3 sentence's scope is restated is the "
      f"design seat's call.")
    w("")

    # ---- figures ----
    w("## Figures (feeds N1's claims ledger)")
    w("")
    gp = lambda camp, arm, m: [c for c in cells if c["campaign"] == camp and c["arm"] == arm and c["map"] == m][0]
    NOT_BLOCK = f"not in N14's block text ({BLOCK}@{PIN}:{ITEM_LINES[1]})"
    n5_line = one_line(BLOCK, "CORR 0.000 with maps +.121/−.130")
    for camp, arm, m, as_written in (("e2a", "sham", "A", "e2a sham +0.111 (map A)"),
                                     ("e2a", "sham", "B", "e2a sham −0.079 (map B)"),
                                     ("e2a", "reward", "A", "e2a state +0.104 (map A)"),
                                     ("e2a", "reward", "B", "e2a state −0.031 (map B)"),
                                     ("f1", "CORR", "A", "f1 CORR +.121 (map A)"),
                                     ("f1", "CORR", "B", "f1 CORR −.130 (map B)"),
                                     ("B3-dpo", "marker", "1", "OLMo DPO +0.1667 single map"),
                                     ("B3-dpo", "marker", "0", "OLMo DPO other map (block: 'the other map's figure beside it')")):
        c = gp(camp, arm, m)
        fig(as_written, f"{c['k']}/{c['n']} → {d4(c['delta'])}", c["stored_src"], c["status"],
            f"Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records")
    for p in pooled:
        if p["campaign"] == "f1" and p["arm"] == "CORR":
            fig("f1 CORR pooled 0.000 (maps mirror-cancel)", f"{p['k']}/{p['n']} → {d4(p['delta'])}",
                f"{p['stored_src']}; prose {RC}@{PIN}:{L['f1_corr_zero']}",
                "reproduced" if p["match"] else "discrepant",
                f"{NOT_BLOCK}; beside the capture; the record's figure (N5's, block line {n5_line}); the exact zero is the realized "
                f"counts, not the design (note 2b)")
        if p["campaign"] == "f1" and p["arm"] == "sham":
            fig("f1 sham pseudo-Δ .045", f"{p['k']}/{p['n']} → {d4(p['delta'])} (stored as absolute value)",
                f"{p['stored_src']}; prose {RC}@{PIN}:{L['f1_sham_pseudo']}",
                "reproduced" if p["match"] else "discrepant",
                f"{NOT_BLOCK}; beside the capture; the record's figure ('Sham pseudo-Δ = .045.'), f1's control envelope")
        if p["campaign"] == "B3-dpo":
            fig(f"OLMo DPO {p['arm']} pooled", f"{p['k']}/{p['n']} → {d4(p['delta'])}", p["stored_src"],
                "reproduced" if p["match"] else "discrepant", f"{NOT_BLOCK}; beside the capture")
        if p["campaign"] == "e2a":
            fig(f"e2a {p['arm']} pooled", f"{p['k']}/{p['n']} → {d4(p['delta'])}", p["stored_src"],
                "reproduced" if p["match"] else "discrepant",
                f"{NOT_BLOCK}; beside the capture; frozen-audit domain; N4 reproduces the same field")
    for camp, arm in (("f1", "sham"), ("B3-dpo", "sham"), ("B3-dpo", "random")):
        for m in (("A", "B") if camp == "f1" else ("0", "1")):
            c = gp(camp, arm, m)
            fig(f"{camp} {arm} map {m} (sham/random beside the capture)", f"{c['k']}/{c['n']} → {d4(c['delta'])}",
                c["stored_src"], "computed-new", f"{NOT_BLOCK}; beside the capture; no stored by-map field for this arm")
    fig("three live captures across two models", "e2a sham (Qwen), f1 CORR (Qwen), B3 DPO marker (OLMo): consistent",
        f"PROPOSAL-j-dose-escalation.md@{PIN}:{L['propj_three']}", "log-only",
        "the block writes 'the three captures'; 'across two models' is PROPOSAL-j's; a count in design prose; "
        "the three cells reproduce")
    fig("e2a: 'label/order artifact correctly absorbed by counterbalancing'", "classification (prose)",
        f"{RC}@{PIN}:{L['e2a_conj2']}-{L['e2a_conj3']}", "log-only",
        f"{NOT_BLOCK}; the record's classification; basis: same sign pattern in the no-state arm; post-hoc "
        f"(section 5): concentrated in maple/cedar, a tag-identity prior (H3 C2)")
    fig("f1: 'maps +.121/−.130 mirror-cancel -- the label artifact absorbed by design'", "classification (prose)",
        f"{RC}@{PIN}:{L['f1_mirror'] - 1}-{L['f1_mirror'] + 1}", "log-only",
        f"{NOT_BLOCK}; the record's classification; post-hoc (section 5): concentrated in maple/cedar, a "
        f"tag-identity prior (H3 C2)")
    fig("B3 DPO: 'label artifact, not a state effect'", "classification (prose)",
        f"{R}@{PIN}:{L['b3_artifact_start']}-{L['b3_artifact_end']}", "log-only",
        f"{NOT_BLOCK}; the record's classification; post-hoc decomposition (section 5): mostly forced-order "
        f"imbalance under the alternation habit (concentrated in amber/granite); residual break term tag-specific "
        f"(velvet)")
    def mx(camp, arm):
        return max(abs(c["delta"]) for c in cells if c["campaign"] == camp and c["arm"] == arm)
    fig("Δ ≈ 0.10 scale (rule 12; preprint §5.6)", "≈ 0.10 / ~0.10 (prose scale)",
        f"FINDINGS-3.md@{PIN}:{L['f3_tenth']}; RESULTS.md@{PIN}:{L['b3_tenth']}; CLAUDE.md@{PIN}:{L['claude_tenth']}; "
        f"PROPOSAL-j-dose-escalation.md@{PIN}:{L['propj_three']}", "log-only",
        f"{NOT_BLOCK}; a scale stated in prose, no stored field; the per-capture maxima are the next row")
    fig("largest abs map Δ per capture arm (beside the ~0.10 scale)",
        f"e2a reward {mx('e2a', 'reward'):.4f}, e2a sham {mx('e2a', 'sham'):.4f}, "
        f"f1 CORR {mx('f1', 'CORR'):.4f}, B3 DPO marker {mx('B3-dpo', 'marker'):.4f}",
        "section 1 cells", "computed-new", f"{NOT_BLOCK}; the OLMo map is above 0.10 (note 5)")
    n_fisher_low = sum(1 for k_ in tests if tests[k_]["fisher_two_sided_map_difference"] < 0.05)
    fig("maps differ beyond noise, arm level (not a record figure; asked of 'what the shields caught')",
        "Fisher two-sided p, pooled over pairs: " +
        ", ".join(f"{k_} {tests[k_]['fisher_two_sided_map_difference']:.3f}" for k_ in tests),
        "section 5", "computed-new",
        f"{NOT_BLOCK}; post-hoc; {n_fisher_low} of {len(tests)} below .05; the pooled-over-pairs test; the record's "
        f"classification is by design logic, not by test")
    fig("maps differ within maple/cedar (Qwen capture arms)",
        "Fisher two-sided p: " + ", ".join(
            f"{k_} {pp[k_]['maple/cedar']['maps']['A']['k_plus']}/{pp[k_]['maple/cedar']['maps']['A']['n']} vs "
            f"{pp[k_]['maple/cedar']['maps']['B']['k_plus']}/{pp[k_]['maple/cedar']['maps']['B']['n']} "
            f"{pv_s(pp[k_]['maple/cedar']['fisher_two_sided_maps_within_pair'])}" for k_ in QK),
        "section 5 per-pair table", "computed-new",
        f"{NOT_BLOCK}; post-hoc, pair named after the table was seen (rule 11); every pair of every capture arm is "
        f"tabulated; no other Qwen pair below .05")
    fig("maple first free pick (Qwen)",
        ", ".join(f"{k_} {pp[k_]['maple/cedar']['pick_pair0']}/{pp[k_]['maple/cedar']['n']}" for k_ in QK)
        + f"; all ten Qwen arms {mc_all['maple_first']}/{mc_all['n']}; cedar-start → maple "
        f"{mc_all['cedar_start_broke_to_maple']}/{mc_all['cedar_start_n']} ("
        f"{mc_all['cedar_start_by_map']['A']['broke_to_maple']}/{mc_all['cedar_start_by_map']['A']['n']} maple = +, "
        f"{mc_all['cedar_start_by_map']['B']['broke_to_maple']}/{mc_all['cedar_start_by_map']['B']['n']} maple = −); "
        f"maple-start → cedar {mc_all['maple_start_broke_to_cedar']}/{mc_all['maple_start_n']}",
        "section 5", "computed-new", f"{NOT_BLOCK}; post-hoc, descriptive")
    fig("Qwen maps with maple/cedar removed",
        "; ".join(f"{k_} A {d4(nomc[k_]['maps']['A']['delta'])} / B {d4(nomc[k_]['maps']['B']['delta'])}" for k_ in QC),
        "section 5", "computed-new", f"{NOT_BLOCK}; post-hoc subset; re-reads no conjunct (rule 11)")
    h3p = pinned_lines(R)[L["h3_c2"] - 1]
    h3_prose_ok = (f"| {round(h3_c2['identity_split'], 3):.3f} | {round(h3_c2['imbalance'], 3):.3f} |" in h3p)
    fig("H3 C2 maple/cedar on Qwen: identity_split 0.207, imbalance 0.293 (scaffold)",
        f"{h3_c2['identity_split']:.4f} (cedar's share; recomputed {h3_c2['identity_split_recomputed']:.4f}); "
        f"imbalance {h3_c2['imbalance']:.4f}",
        f"data/e2b/h3_tagscreen.json:pairs[C2].formats.scaffold; prose {R}@{PIN}:{L['h3_c2']}",
        "reproduced" if (h3_c2["recomputed_matches"] and h3_prose_ok) else "discrepant",
        f"{NOT_BLOCK}; the record's measurement, cited at the round-2 values-check; identity_split recomputed from "
        f"the per-probe rows; the prose's 3-dp values {'match' if h3_prose_ok else 'DO NOT match'}")
    fig("B3 DPO marker breaks per pair", ", ".join(b3_one_way) + f" (pair[0] coordinate "
        f"{deco['B3-dpo marker']['pooled']['breaks_to_pair0']} vs {deco['B3-dpo marker']['pooled']['breaks_to_pair1']})",
        "section 5", "computed-new", f"{NOT_BLOCK}; post-hoc, descriptive")
    fig("forced-order / net-break decomposition per map", "section 5 table", "habit.py identity on session records",
        "computed-new", f"{NOT_BLOCK}; post-hoc, descriptive")
    fig("opposite-signed maps across the three campaigns",
        f"{n_opp}/{n_ctx} arm cells; {n_ge10}/{n_ctx} with a map abs(Δ) ≥ 0.10 ({n_gt10}/{n_ctx} strictly > 0.10; "
        f"exactly at 0.10: {', '.join(at_tenth) or 'none'})",
        "section 6", "computed-new",
        f"{NOT_BLOCK}; consistent with PROPOSAL-j's 'a fourth capture is expected' "
        f"(PROPOSAL-j-dose-escalation.md@{PIN}:{L['propj_three'] + 2}), which does not rest on this count")
    w("| figure as the block writes it | value printed | source | status | note |")
    w("|---|---|---|---|---|")
    for f_ in figures:
        w(f"| {f_['figure']} | {f_['value']} | `{f_['source']}` | {f_['status']} | {f_['note']} |")
    w("")
    w("## STOPs")
    w("")
    disc = [c for c in cells if c["status"] == "discrepant"] + [p for p in pooled if not p["match"]]
    if disc:
        w(f"Discrepant cells: {len(disc)} (listed in section 1). Tier 2: reported, not a STOP.")
    else:
        w("None. Every stored figure the block names reproduces exactly from the pinned session records; no "
          "analyzer change is needed for any of them.")
    w("")

    # ---- values-check (pass 1 findings and their dispositions) ----
    VC = [
        {"finding": "f1 'no injection' locator PROPOSAL-f:17 is the §0 heading; the explicit line is :27",
         "disposition": "fixed",
         "change": f"section 2 now cites PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{L['f1_noinj']} "
                   f"(\"Nothing is injected\"), with the §0 heading at :{L['f1_hornfree']}; anchor searched, not typed"},
        {"finding": "four Figures rows (e2a reward/sham pooled, f1 CORR pooled 0.000, f1 sham .045) read as block "
                    "figures; .045 had no record locator",
         "disposition": "fixed",
         "change": f"every row that N14's block text (:{ITEM_LINES[1]}) does not write now says so in its note "
                   f"(applied to all such rows, not only the four); f1 CORR 0.000 carries {RC}@{PIN}:"
                   f"{L['f1_corr_zero']} and N5's block line {n5_line}; f1 sham .045 carries {RC}@{PIN}:"
                   f"{L['f1_sham_pseudo']}"},
        {"finding": "note 3 overstated: the f1 receipt does show a label-locked push cancelling under the swap; "
                    "what it lacks is the size/form of a vector-borne push",
         "disposition": "fixed",
         "change": f"note 3 reworded to that scope, with the lean computed here (pair[0] {fcr['pick_pair0']}/"
                   f"{fcr['n']}, p = {fcr['pick_pair0_p_two_sided']:.4f} two-sided; breaks "
                   f"{fcp['breaks_to_pair0']} vs {fcp['breaks_to_pair1']}) and §1's own H1 clause "
                   f"(:{L['proph_h1']}); the forced-order share of map B disclosed"},
        {"finding": "section 6 called the 22-cell count 'the premise of' PROPOSAL-j's 'a fourth capture is expected'",
         "disposition": "fixed",
         "change": f"now 'consistent with'; adds that PROPOSAL-j rests the expectation on the three captures "
                   f"(:{L['propj_three']}) and that the count is computed-new"},
        {"finding": "17/22 includes a cell exactly at 0.10 (B3-dpo sham); 16/22 under a strict '>'",
         "disposition": "fixed",
         "change": f"max abs map Δ now compared as exact Fractions; section 6 and the Figures row print "
                   f"{n_ge10}/{n_ctx} ≥ 0.10, {n_gt10}/{n_ctx} > 0.10, cells exactly at 0.10: "
                   f"{', '.join(at_tenth) or 'none'}"},
        {"finding": "missing locators for the CORR target direction and B3's 48:18:18 targets",
         "disposition": "fixed",
         "change": f"PROPOSAL-f-natural-reinforcer-screen.md@{PIN}:{L['f1_corr_row']} (CORR table row); targets "
                   f"{b3_targets['marker']}:{b3_targets['sham']}:{b3_targets['random']} and per_stratum "
                   f"{b3_per_stratum['marker']}:{b3_per_stratum['sham']}:{b3_per_stratum['random']} now read from "
                   f"`data/olmo/b3_screen_dpo.json:targets` / `:per_stratum` at the pin and printed"},
        {"finding": "e2a domain sentence does not say which audit (frozen vs v2) the map figures use",
         "disposition": "fixed",
         "change": f"section 1 states the frozen audit (stored `excluded` flag; exclusions per arm printed from the "
                   f"pinned records) with scripts/e2a_recount.py@{PIN}:{L['recount_frozen']}; Code also ran "
                   f"`jlens-qwen36/.venv/bin/python scripts/e2a_recount.py` from the repository root with the root "
                   f"on PYTHONPATH (read-only, writes nothing; it reads the working tree's data/e2a/sessions.jsonl, "
                   f"EQUAL to the pin per section 0), which printed 'session set identical = True; every reason string identical = True' "
                   f"for the frozen audit and 55/102 (frozen) / 54/101 (v2), both '[MATCHES the record]'"},
        {"finding": "JSON header has no exact command",
         "disposition": "fixed",
         "change": "J['command'] added (the same string as the raw's Command line)"},
    ]
    J["values_check"] = {"pass": 1, "findings": VC,
                         "checker_summary": "165 claims checked; all independent recomputations agreed; 8 minor "
                                            "findings, none changing a number or a status; no STOP"}
    w("## Values-check")
    w("")
    w("Pass 1 (independent checker; its own scratch code read the pinned artifacts through `git show`): 165 claims "
      "checked; every independent recomputation agreed (all 8 block map figures, 7 pooled figures, the computed-new "
      "sham/random maps, the 22-cell context table, every decomposition row with the pinned habit.py, the "
      "start-balance table and all post-hoc exact tests); the redaction check was clean. Eight minor findings, none "
      "changing a number or a status. Each was re-checked against the pinned record by a tool run before it was "
      "applied; none was rejected.")
    w("")
    w("| # | finding | disposition | what changed |")
    w("|---|---|---|---|")
    for i, v in enumerate(VC, 1):
        w(f"| {i} | {v['finding']} | {v['disposition']} | {v['change']} |")
    w("")

    # ---- values-check, round 2 (tier-2 residual findings) ----
    base_qv = per_pair(olmo["base"], "marker", ("0", "1"))["quartz/velvet"]
    er_mc_ = pp["e2a reward"]["maple/cedar"]
    VC2 = [
        {"severity": "substantive",
         "finding": "section 5's Qwen reading ('habit breaks lean toward pair[0]'; 'cannot be separated at these "
                    "counts'; 'should not be read as a demonstrated effect in any single campaign') is misleading for "
                    "the two Qwen captures: the pooled pair[0] coordinate hides one strong tag preference, maple over "
                    "cedar, which the record measured (H3 C2) and N14 did not cite",
         "disposition": "fixed",
         "verified": f"every count in the finding reproduced, first by Code's own scratch code (pinned artifacts via "
                     f"git show), then by this script: maple first {er_mc_['pick_pair0']}/{er_mc_['n']} (e2a reward, "
                     f"p = {pv_s(er_mc_['pick_pair0_p_two_sided'])}), "
                     f"{pp['e2a sham']['maple/cedar']['pick_pair0']}/{pp['e2a sham']['maple/cedar']['n']} (e2a sham), "
                     f"{pp['f1 CORR']['maple/cedar']['pick_pair0']}/{pp['f1 CORR']['maple/cedar']['n']} (f1 CORR); "
                     f"within-pair Fisher {pv_s(er_mc_['fisher_two_sided_maps_within_pair'])}, "
                     f"{pv_s(pp['e2a sham']['maple/cedar']['fisher_two_sided_maps_within_pair'])}, "
                     f"{pv_s(pp['f1 CORR']['maple/cedar']['fisher_two_sided_maps_within_pair'])}; ten arms "
                     f"{mc_all['maple_first']}/{mc_all['n']}; cedar-start → maple "
                     f"{mc_all['cedar_start_broke_to_maple']}/{mc_all['cedar_start_n']} "
                     f"({mc_all['cedar_start_by_map']['A']['broke_to_maple']}/{mc_all['cedar_start_by_map']['A']['n']}, "
                     f"{mc_all['cedar_start_by_map']['B']['broke_to_maple']}/{mc_all['cedar_start_by_map']['B']['n']}); "
                     f"maple-start → cedar {mc_all['maple_start_broke_to_cedar']}/{mc_all['maple_start_n']}; other "
                     f"pairs {mc_all['other_pairs_breaks']}/{mc_all['other_pairs_n']}; maps without maple/cedar and "
                     f"maple's share of the pair[0] breaks as the finding states; H3 C2 identity_split "
                     f"{h3_c2['identity_split']:.4f} = cedar's share (tag_lo) per valence_core/tagscreen.py@{PIN}:"
                     f"{L['tagscreen_doc']}, recomputed from the per-probe rows. Two refinements from the pinned text: "
                     f"PROPOSAL-j's sentence is at :{L['propj_e2a_pairs']}-{L['propj_not_admitted']} (the finding "
                     f"cited 360-363); and with maple/cedar removed e2a sham's maps are still opposite-signed, the other "
                     f"way (A {d4(nomc['e2a sham']['maps']['A']['delta'])}, B "
                     f"{d4(nomc['e2a sham']['maps']['B']['delta'])}), so the raw says the A-positive/B-negative pattern "
                     f"is gone rather than that opposite signs are",
         "change": f"section 5 gains a per-pair table for every pair of every capture arm (first pick by tag with "
                   f"exact binomial p; +label share by map with within-pair Fisher p; breaks by start tag and map; "
                   f"breaks by tag), the maple/cedar paragraph over all ten Qwen arms, a maps-without-maple/cedar "
                   f"table (with maple/cedar alone pooled over maps and maple's share of the pair[0] breaks), and the "
                   f"H3 C pairs recomputed; the Qwen bullets are rewritten (the label artifact is a measured "
                   f"tag-identity imbalance, maple over cedar, H3 C2 at {R}@{PIN}:{L['h3_c2']}, concentrated in one "
                   f"pair of four, which the map counterbalance turns into opposite-signed maps and mostly cancels); "
                   f"'cannot be separated at these counts' is replaced by the per-pair separation of the state arm; "
                   f"'should not be read as a demonstrated effect in any single campaign' is dropped; the arm-level "
                   f"Fisher table and Figures row now say they are the pooled-over-pairs test; note 7 (PI/design seat) "
                   f"names the source and the H3 sentence's slate/prism-only basis ({R}@{PIN}:{L['h3_noimpeach']}-"
                   f"{L['h3_noimpeach_end']}); note 3 says the receipt's lean is maple's; the e2a/f1 classification "
                   f"rows carry the post-hoc pointer. Post-hoc test count {len(ph)} (was 29), every one listed when "
                   f"below .05. Rule 11 stated at each step; no verdict moves"},
        {"severity": "minor",
         "finding": "B3 DPO: 'its breaks do not lean toward pair[0] (4 vs 5 pooled)' and 'rather than a label-identity "
                    "preference' hide per-pair breaks that all run one way",
         "disposition": "fixed",
         "verified": f"this script: {', '.join(b3_one_way)}; pair[0] coordinate "
                     f"{deco['B3-dpo marker']['pooled']['breaks_to_pair0']} vs "
                     f"{deco['B3-dpo marker']['pooled']['breaks_to_pair1']}; map-1 breaks to + all "
                     f"{b3_map1_plus_break_tags[0]}; amber/granite map 1 {ag['started_on_plus']}/{ag['n']} started on "
                     f"{ag['plus_tag']} (+label) and {ag['started_on_plus_and_picked_it']} picked it; forced-order "
                     f"{d4(dm['component_forced_end_balance'])} vs net-break {d4(dm['component_net_breaks'])}; base "
                     f"quartz/velvet first pick quartz {base_qv['pick_pair0']}/{base_qv['n']} (B3-base marker; "
                     f"verified, not added to the body because base is not a capture arm)",
         "change": "the B3 bullet now gives the per-pair break statement, the amber/granite concentration of map 1's "
                   "forced-order term and a per-pair map-1 table; 'mostly forced-order' kept with the exact terms; "
                   "'rather than a label-identity preference' replaced by 'the residual break term is tag-specific "
                   "(velvet), not absent'; the B3 classification row's note updated"},
        {"severity": "minor",
         "finding": "section 6 cites the random1 'noise doing its criterion job' phrase at :684; it spans two lines",
         "disposition": "fixed",
         "verified": f"git show {PIN}:{RC} lines {L['e2a_random1_noise']}-{L['e2a_random1_noise'] + 1}; the script now "
                     f"asserts the phrase's end is on the second line",
         "change": f"cited as {RC}@{PIN}:{L['e2a_random1_noise']}-{L['e2a_random1_noise'] + 1}"},
        {"severity": "minor",
         "finding": "Figures row 'Δ ≈ 0.10 scale' is marked computed-new, but the ~0.10 is a record prose figure",
         "disposition": "fixed",
         "verified": f"anchors searched in the pinned text: FINDINGS-3.md:{L['f3_tenth']}, RESULTS.md:{L['b3_tenth']}, "
                     f"CLAUDE.md:{L['claude_tenth']}, PROPOSAL-j-dose-escalation.md:{L['propj_three']}; the maxima "
                     f"reproduce ({mx('e2a', 'reward'):.4f}, {mx('e2a', 'sham'):.4f}, {mx('f1', 'CORR'):.4f}, "
                     f"{mx('B3-dpo', 'marker'):.4f})",
         "change": "the row is now log-only with the four locators; the per-capture maxima are a separate "
                   "computed-new row; note 5 carries the locators"},
        {"severity": "minor",
         "finding": "N14 does not point to N5's CORR delivery artifact (clean text in corrupted-label rounds at rate .12)",
         "disposition": "fixed",
         "verified": f"this script's check of the stored task field against `data/f/pools.json:CORR_clean` at the pin: "
                     f"{n5_xref['q_rounds_clean_prefix']}/{n5_xref['q_rounds']} Q rounds, items "
                     f"{n5_xref['clean_items']}, {n5_xref['valid_with_one_clean_forced_q']}/"
                     f"{n5_xref['valid_sessions']} valid sessions with one corrupted forced task, as N5 reports",
         "change": "note 6 points to N5 section 7 by heading (N5's raw is an untracked sibling still under revision, "
                   "so no line number is cited) with the corroborated counts; no N14 number moves"},
    ]
    J["values_check_round2"] = {"round": 2, "findings": VC2}
    w("Round 2 (tier-2 residual findings, applied by Code; each re-verified by a tool run before it was applied; "
      "none rejected):")
    w("")
    w("| # | severity | finding | disposition | verified by | what changed |")
    w("|---|---|---|---|---|---|")
    for i, v in enumerate(VC2, 1):
        w(f"| R2-{i} | {v['severity']} | {v['finding']} | {v['disposition']} | {v['verified']} | {v['change']} |")
    w("")

    J.update({"capture_cells": cells, "pooled": pooled, "weighted_identity": ident,
              "decomposition_posthoc": deco, "first_pick_reads_posthoc": reads,
              "map_tests_posthoc": tests, "context_all_arms": context,
              "context_counts": {"cells": n_ctx, "opposite_signed": n_opp,
                                 "map_abs_ge_0.10": n_ge10, "map_abs_gt_0.10_strict": n_gt10,
                                 "cells_exactly_at_0.10": at_tenth,
                                 "stored_maps_reverified": all_ctx_match},
              "f1_structure_checks": f1_checks, "b3_start_parity": olmo_parity,
              "clone_analyzers": clone, "figures": figures,
              "stops": [] if not disc else [{"subitem": "N14", "discrepancy": str(disc)}]})

    out_p = os.path.join(REPO, args.out)
    json_p = os.path.join(REPO, args.json_out)
    with open(out_p, "w", encoding="utf-8") as f:
        f.write("\n".join(o) + "\n")
    with open(json_p, "w", encoding="utf-8") as f:
        json.dump(J, f, indent=1, ensure_ascii=False, default=str)
    print(f"wrote {args.out} ({len(o)} lines) and {args.json_out}")
    print(f"cells reproduced: {sum(1 for c in cells if c['status'] == 'reproduced')}, "
          f"computed-new: {sum(1 for c in cells if c['status'] == 'computed-new')}, "
          f"discrepant: {sum(1 for c in cells if c['status'] == 'discrepant')}; "
          f"pooled matches: {sum(1 for p in pooled if p['match'])}/{len(pooled)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
