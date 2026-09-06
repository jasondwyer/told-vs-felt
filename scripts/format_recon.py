#!/usr/bin/env python3
"""FORMAT RECON -- design block 2026-09-06 §4 (PI go "Go format recon").
SHAM ONLY. Three forced-phase formats, n = 24 per format, roster of record,
audit v3 as the audit of record, checkpointed, uncached round path.
Descriptive only; no bar; template recalibration for LOCK-k.

    --selftest              model-free, 20+ checks (formats, schedule, hygiene,
                            draw order via the e2a walk, audit-v3 wiring,
                            scope, gate, resume, sham source guard, bars)
    --stage time            ONE session per format -> data/format/format_recon_timing.json
                            with the projection to 24 x 3 and the gate verdict.
                            Transcripts printed in full (rule 25).
    --stage run             the registered n per format; REFUSES without a timing
                            artifact that projects <= --gate-hours (trap 32).
                            --format F0|F1|F2|all, --limit, --resume (skip-only).
    --analyze               per-format report -> data/format/format_recon_analysis.json
                            (--source sessions|timing|checkpoint; --out-name)

Laptop, one model process, AC >= 96 W, caffeinate -is. Everything Qwen
needs jlens-qwen36/.venv/bin/python.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.e2d import config as C                          # noqa: E402
from valence_core.e2d.audit_v3 import AUDIT_VERSION, AuditV3       # noqa: E402
from valence_core.formats import recon as R                        # noqa: E402
from valence_core.session import (assert_modules_absent,           # noqa: E402
                                  build_ban_list, check_bars, verify_firing)
from valence_core.session_e2a import (MENU_TEMPLATES, ROUND_TEMPLATES,   # noqa: E402
                                      SESSION_BANNER, load_tasks)

DATA = os.path.join(REPO, "data")
OUT = os.path.join(DATA, "format")
TIMING = os.path.join(OUT, "format_recon_timing.json")


def sessions_path(fmt: str) -> str:
    return os.path.join(OUT, f"format_recon_{fmt}_sessions.json")


def sha16_file(path: str) -> str:
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def all_paraphrases(tasks) -> list[str]:
    return [p for t in tasks for p in t["paraphrases"]]


def all_rosters() -> dict:
    """Every roster the neutral label must be absent from (design patch
    2026-09-06 §2): the roster of record, H3's sixteen, the h3/a1 candidate
    rosters, the e2a archive's pairs."""
    out = {"e2d_roster_of_record": {t for p in C.ROSTER for t in p}}
    out["H3_sixteen"] = set(json.load(open(os.path.join(DATA, "e2b/h3b_repair_screen.json")))["tags"])
    out["h3_candidates"] = {t for p in json.load(open(os.path.join(DATA, "configs/h3_roster_candidates.json")))["pairs"] for t in p["tags"]}
    a1 = json.load(open(os.path.join(DATA, "configs/a1_roster_candidates.json")))
    def tags_of(o):
        s = set()
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("tags", "pair") and isinstance(v, list) and all(isinstance(x, str) for x in v):
                    s |= set(v)
                else:
                    s |= tags_of(v)
        elif isinstance(o, list):
            for v in o:
                s |= tags_of(v)
        return s
    out["a1_candidates"] = tags_of(a1)
    out["e2a_archive_pairs"] = {t for l in open(os.path.join(DATA, "e2a/sessions.jsonl")) if l.strip() for t in json.loads(l)["pair"]}
    return out


def assert_neutral_outside_every_roster() -> dict:
    """Design patch 2026-09-06 §2: the neutral label is asserted absent from
    every roster and from H3's sixteen before the run; a hit is a stop and a
    re-selection, never a silent pass. Also pins the selection artifact."""
    ros = all_rosters()
    hits = {k: R.NEUTRAL_LABEL for k, v in ros.items() if R.NEUTRAL_LABEL in v}
    if hits:
        raise SystemExit(f"NEUTRAL LABEL STOP: {R.NEUTRAL_LABEL!r} is in {sorted(hits)}; pick the next candidate "
                         f"(data/format/neutral_label_selection.json) and report it.")
    sel_path = os.path.join(REPO, R.NEUTRAL_SELECTION)
    if not os.path.exists(sel_path):
        raise SystemExit(f"NEUTRAL SELECTION ARTIFACT MISSING: {sel_path}")
    sel = json.load(open(sel_path))
    if sel["chosen"]["label"] != R.NEUTRAL_LABEL or int(sel["chosen"]["token_id"]) != R.NEUTRAL_TOKEN_ID:
        raise SystemExit(f"NEUTRAL SELECTION MISMATCH: artifact chose {sel['chosen']}, module declares "
                         f"{R.NEUTRAL_LABEL!r}/{R.NEUTRAL_TOKEN_ID}")
    return {"rosters_checked": {k: len(v) for k, v in ros.items()}, "neutral": R.NEUTRAL_LABEL, "hits": {}}


def hygiene(tasks) -> dict:
    """Rule 18 (tags vs every pool, word-boundary) and rule 28(c) (tags vs
    the wrapper). Hard stops."""
    tags = [t for p in C.ROSTER for t in p] + [R.NEUTRAL_LABEL]
    pool = all_paraphrases(tasks)
    wrapper = SESSION_BANNER + "".join(ROUND_TEMPLATES) + "".join(MENU_TEMPLATES)
    wrapper = re.sub(r"\{[a-z]+\}", " ", wrapper)
    hits = []
    for tag in tags:
        rx = re.compile(rf"\b{re.escape(tag)}\b", re.I)
        hits += [("pool", tag, p[:60]) for p in pool if rx.search(p)]
        if rx.search(wrapper):
            hits.append(("wrapper", tag, ""))
    if hits:
        raise SystemExit(f"HYGIENE STOP (rule 18 / 28c): {hits[:5]}")
    ros = assert_neutral_outside_every_roster()
    return {"tags_checked": tags, "n_pool_texts": len(pool), "rule18_pool_hits": 0,
            "rule28c_wrapper_hits": 0, "neutral_outside_every_roster": ros}


def neutral_id_check(adapter) -> int:
    enc = adapter.encode(" " + R.NEUTRAL_LABEL, add_special_tokens=False)
    if len(enc) != 1 or int(enc[0]) != R.NEUTRAL_TOKEN_ID:
        raise SystemExit(f"NEUTRAL LABEL STOP: {R.NEUTRAL_LABEL!r} encodes to {enc}, expected "
                         f"[{R.NEUTRAL_TOKEN_ID}] (selection artifact). Not the tokenizer the label was "
                         f"verified on -- escalate, do not re-verify silently.")
    return int(enc[0])


def audit_sha16_recomputed(cfg: dict) -> str:
    """The frozen body hash the e2b/H1 scripts pin: sha256 of the compact,
    sort-keyed JSON of the artifact minus its own `sha16` field."""
    body = {k: v for k, v in cfg.items() if k != "sha16"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]


def audit_of_record() -> tuple[AuditV3, dict]:
    """Audit v3 over the audit-v2 artifact, whose declared sha16 is RECOMPUTED
    here and refused on mismatch -- echoing a file's self-declared hash pins
    nothing (values-check of 2026-09-06)."""
    v2, cfg = C.load_audit()
    now = audit_sha16_recomputed(cfg)
    if now != cfg.get("sha16"):
        raise SystemExit(f"AUDIT ARTIFACT MISMATCH: e2b_audit_v2.json declares sha16 {cfg.get('sha16')}, "
                         f"recomputed {now}. The monitor of record has moved -- stop, escalate.")
    cfg = dict(cfg); cfg["sha16_recomputed"] = now
    return AuditV3(v2=v2), cfg


def others_factory(tasks):
    pool = all_paraphrases(tasks)
    return lambda task_text: [t for t in pool if t != task_text]


def bars_or_stop():
    bars = C.declared_bars(0.02)
    fails = verify_firing(bars, C.FIRING_CASES)
    if fails:
        raise SystemExit("DECLARED BARS MISBEHAVE (rule 21):\n  " + "\n  ".join(fails))
    exercised = {c[0] for c in C.FIRING_CASES}
    dirs = {b.name: {c[3] for c in C.FIRING_CASES if c[0] == b.name} for b in bars}
    missing = [b.name for b in bars if b.name not in exercised or dirs[b.name] != {True, False}]
    if missing:
        raise SystemExit(f"FIRING CHECK INCOMPLETE (trap 5): {missing}")
    return bars


# ============================================================================
# self-test (model-free)
# ============================================================================
class _G:
    def __init__(self, text):
        self.text = text
        self.token_ids = list(range(len(text.split())))
        self.cap_hit = False
        self.stop_reason = "newline"


class _FakeAdapter:
    """Scaffolding-only stand-in: deterministic encode, scripted generations,
    no forward. Asserts the sham contract on every call."""
    def __init__(self, texts):
        self._texts = list(texts)
        self.calls = 0

    def encode(self, text, add_special_tokens=True):
        return [len(w) for w in text.split()] or [1]

    def generate(self, prefix, seg, injections=(), *, seed, temp, max_tokens, ban_ids, cached):
        assert not injections and cached is False, "sham contract violated"
        t = self._texts[self.calls % len(self._texts)]
        self.calls += 1
        return _G(t)


def _scripted_read(picks):
    it = iter(picks)
    def read(prefix, a, b):
        p = next(it)
        return p, {"pick": p, "p_a": 0.6, "p_b": 0.4, "label_mass": 0.5, "top1_id": 0,
                   "top1_is_label": True, "verify_kl": 0.0}
    return read


TEXTS = ["The ferry glides through pale gold light as the harbor wakes.",
         "A quiet morning crossing, steel bow parting silver water.",
         "Gulls trail the boat while the town blinks awake behind it.",
         "Warm cider, a wool blanket, and rain on the window: perfect.",
         "The lighthouse keeps its slow count over a restless sea.",
         "Footsteps crunch across frost as the market stalls open.",
         "A kettle hums; the cat claims the only sunlit chair.",
         "Neon puddles shiver under the late tram's headlamp.",
         "Bread cooling on the sill scents the whole narrow street.",
         "The last train sighs into the platform, nearly empty."]


def selftest() -> int:
    from valence_core.session_e2a import verify_archived_session
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    audit3, cfg = audit_of_record()
    others = others_factory(tasks)
    results = []
    def chk(name, ok, got="", note=""):
        results.append((name, bool(ok), str(got), note))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name:64s} {got}  {note}", flush=True)

    # 1. the three formats, both cells of a pair
    c_a = {"pair": ["slate", "prism"], "first_index": 0, "tag_plus": "slate", "tag_minus": "prism"}
    c_b = {"pair": ["slate", "prism"], "first_index": 1, "tag_plus": "prism", "tag_minus": "slate"}
    fo = {f: [t for t, _ in R.forced_order(f, c_a)] for f in R.FORMATS}
    chk("F0 = A B A B", fo["F0"] == ["slate", "prism", "slate", "prism"], fo["F0"])
    chk("F1 = N N A B", fo["F1"] == [R.NEUTRAL_LABEL, R.NEUTRAL_LABEL, "slate", "prism"], fo["F1"])
    chk("F2 = A A B B", fo["F2"] == ["slate", "slate", "prism", "prism"], fo["F2"])
    fob = {f: [t for t, _ in R.forced_order(f, c_b)] for f in R.FORMATS}
    chk("swapped cell mirrors every format",
        fob["F0"] == ["prism", "slate", "prism", "slate"] and fob["F1"] == [R.NEUTRAL_LABEL, R.NEUTRAL_LABEL, "prism", "slate"]
        and fob["F2"] == ["prism", "prism", "slate", "slate"], fob)
    chk("every format's LAST forced label is tag_minus (uniform break definition)",
        all(R.forced_order(f, c)[-1][0] == c["tag_minus"] for f in R.FORMATS for c in (c_a, c_b)))
    chk("every format has 4 forced rounds and the neutral appears only in F1",
        all(len(R.FORMATS[f]["order"]) == R.N_FORCED for f in R.FORMATS)
        and [f for f in R.FORMATS if "neutral" in R.FORMATS[f]["order"]] == ["F1"])

    # 2. schedule
    sched = R.build_schedule(24, np.random.default_rng(R.DRAW_SEED))
    key = lambda c: (tuple(c["pair"]), c["tag_plus"])
    from collections import Counter
    cnt = Counter(key(c) for c in sched)
    chk("F1/F2: 24 = 8 cells x 3, exactly; F0: 8 = 1 block", len(cnt) == 8 and set(cnt.values()) == {3}
        and R.N_PER_FORMAT == {"F0": 8, "F1": 24, "F2": 24}
        and len({key(c) for c in R.build_schedule(8, np.random.default_rng(R.DRAW_SEED))}) == 8, dict(cnt))
    chk("the 8-schedule is the prefix of the 24-schedule (reallocation changes how many, never which)",
        [key(c) for c in R.build_schedule(8, np.random.default_rng(R.DRAW_SEED))] == [key(c) for c in sched[:8]])
    blocks_ok = all(len({key(c) for c in sched[i:i + 8]}) == 8 for i in range(0, 24, 8))
    chk("every block of 8 is a permutation of the cells (balanced at every prefix)", blocks_ok)
    sched2 = R.build_schedule(24, np.random.default_rng(R.DRAW_SEED))
    chk("schedule deterministic under the draw seed", [key(c) for c in sched] == [key(c) for c in sched2])
    chk("each pair starts on each label 3 times", all(v == 3 for v in cnt.values()))

    # 3. neutral label + hygiene
    sel = json.load(open(os.path.join(REPO, R.NEUTRAL_SELECTION)))
    ros = all_rosters()
    chk("neutral label `timber`: selection artifact agrees (id 43299), first passing candidate in the declared order",
        sel["chosen"] == {"label": R.NEUTRAL_LABEL, "token_id": R.NEUTRAL_TOKEN_ID}
        and [r for r in sel["report"] if r["passes"]][0]["label"] == R.NEUTRAL_LABEL, sel["chosen"])
    chk("neutral label absent from EVERY roster and H3's sixteen (5 rosters); `cedar` would have failed",
        all(R.NEUTRAL_LABEL not in v for v in ros.values()) and len(ros) == 5 and "cedar" in ros["H3_sixteen"]
        and assert_neutral_outside_every_roster()["hits"] == {}, {k: len(v) for k, v in ros.items()})
    hy = hygiene(tasks)
    chk("rule 18 + 28c: 9 tags absent from all 64 paraphrases and from the wrapper",
        hy["n_pool_texts"] == 64 and len(hy["tags_checked"]) == 9, hy["n_pool_texts"])
    chk("neutral label absent from every data/corpus pool and the e0/s2/b2 stimulus files (selection artifact)",
        all(r["other_pool_hits"] == 0 and r["e2a_pool_hits"] == 0 for r in sel["report"] if r["label"] == R.NEUTRAL_LABEL))

    # 4. draw order: synthetic sessions reconstruct under the e2a walk, all formats
    walked = ok = seeds = 0
    recs = []
    for f in R.FORMATS:
        for idx in (0, 1, 5, 7):
            cell = sched[idx]
            picks = []
            for ci in range(6):
                picks.append(cell["tag_plus"] if ci % 2 == 0 else cell["tag_minus"])   # follow + alternate
            fa = _FakeAdapter(TEXTS)
            # the read override returns the pick as the label string regardless of menu order
            rec = R.run_session(fa, f, idx, cell, tasks, audit3, [], [], others,
                                _read_override=_scripted_read(picks))
            recs.append(rec)
            r = verify_archived_session(R.as_e2a_row(rec), tasks)
            walked += 1; ok += int(r["ok"]); seeds += int(r.get("seeds_match", False))
    chk("e2a walk reconstructs 12/12 synthetic sessions (3 formats x 4 idx), seeds match",
        walked == 12 and ok == 12 and seeds == 12, f"{ok}/{walked} ok, {seeds} seed streams")
    bad = dict(recs[0]); bad["transcript"] = recs[0]["transcript"].replace("[round 2", "[round X", 1)
    chk("a corrupted scaffold FAILS the walk (both directions, trap 5)",
        not verify_archived_session(R.as_e2a_row(bad), tasks)["ok"])
    vf = R.verify_format_walk(recs, tasks)
    chk("verify_format_walk reports walked beside passed", vf["n_walked"] == 12 and vf["all_ok"])
    chk("as_e2a_row arm == rng key", R.as_e2a_row(recs[0])["arm"] == R.rng_key(recs[0]["format"]))
    chk("synthetic sessions are sham, uncached, unsteered on every round",
        all(r["sham_only"] and not r["round_path_cached"] and not any(x["steered"] for x in r["rounds"] + r["choices"]) for r in recs))
    r0 = recs[0]
    chk("record carries the retention interval per forced round and prefix tokens per read",
        set(r0["tokens_forced_end_to_first_read"]) == {"forced0", "forced1", "forced2", "forced3"}
        and all("prefix_tokens_at_read" in c for c in r0["choices"]))

    # 5. habit functions agree with the record's break field
    from valence_core.e2d import habit as H
    chk("follows_habit == not first_pick_is_last_forced_label (follow script)",
        all(H.follows_habit(r) is True and r["first_pick_is_last_forced_label"] is False for r in recs))
    chk("strictly_alternates True on the alternating script", all(H.strictly_alternates(r) for r in recs))
    cell = sched[2]
    brk = R.run_session(_FakeAdapter(TEXTS), "F2", 2, cell, tasks, audit3, [], [], others,
                        _read_override=_scripted_read([cell["tag_minus"]] * 6))
    chk("break script: first pick = last forced label -> break True, habit False, not alternating",
        brk["first_pick_is_last_forced_label"] is True and H.follows_habit(brk) is False
        and H.strictly_alternates(brk) is False)

    # 6. audit v3 wiring, rule 28(b) precedence, lexical
    own = ("slate", "prism")
    task = tasks[0]["paraphrases"][0]
    o = others(task)
    e, a, l, cl = R.classify_v3("", task, [], o, audit3, own)
    chk("empty -> audit:empty (v2 first)", e == "audit:empty" and not a and l is None, e)
    e, a, l, cl = R.classify_v3("* * *", task, [], o, audit3, own)
    chk("'* * *' -> content:null_response (exclusion-bearing)", e == "content:null_response" and cl == "null_response", e)
    e, a, l, cl = R.classify_v3(task, task, [], o, audit3, own)
    chk("verbatim instruction -> task_echo ADVISORY, no exclusion", e is None and a == ["content:task_echo"], (e, a))
    e, a, l, cl = R.classify_v3("=== Config evaluation session ===\nslate wins", task, [], o, audit3, own)
    chk("frame fragment claims first; lexical suppressed (rule 28b)", (e or "").startswith("audit:frame") and l is None, (e, l))
    e, a, l, cl = R.classify_v3(TEXTS[0], task, [], o, audit3, own)
    chk("a plain answer: nothing", e is None and not a and l is None, (e, a, l))
    e, a, l, cl = R.classify_v3("I would pick slate for this one.", task, [], o, audit3, own)
    chk("own tag in a response -> lexical hit", l == "slate", l)
    e, a, l, cl = R.classify_v3(f"{R.NEUTRAL_LABEL} is a lovely material.", task, [], o, audit3, own + (R.NEUTRAL_LABEL,))
    chk("F1's neutral label in the lexical set", l == R.NEUTRAL_LABEL, l)
    e, a, l, cl = R.classify_v3(TEXTS[1], task, [TEXTS[1]], o, audit3, own)
    chk("repeat of an earlier response -> content:stuck_attractor", e == "content:stuck_attractor", e)

    # 7. scope
    chk("lenient: content exclusion on a FORCED round excludes; on a free round it does not",
        R.excludes("content:null_response", None, True, "e2a") and not R.excludes("content:null_response", None, False, "e2a"))
    chk("strict: excludes on any round; lexical excludes under both",
        R.excludes("audit:empty", None, False, "e2b") and R.excludes(None, "slate", False, "e2a") and R.excludes(None, "slate", False, "e2b"))
    fr = R.run_session(_FakeAdapter(TEXTS[:4] + ["* * *"] + TEXTS[5:]), "F0", 3, sched[3], tasks, audit3, [], [], others,
                       _read_override=_scripted_read([sched[3]["tag_plus"], sched[3]["tag_minus"]] * 3))
    chk("a null response on free0 -> lenient keeps the session, strict recovers the exclusion",
        not fr["excluded"] and fr["strict_excluded"] and fr["strict_exclude_reason"] == "content:null_response@free0",
        (fr["excluded"], fr["strict_exclude_reason"]))
    fr2 = R.run_session(_FakeAdapter(["* * *"] + TEXTS), "F1", 4, sched[4], tasks, audit3, [], [], others,
                        _read_override=_scripted_read([sched[4]["tag_plus"]] * 6))
    chk("a null response on forced0 -> excluded at forced0, no reads, break undecidable",
        fr2["excluded"] and fr2["exclude_reason"] == "content:null_response@forced0" and fr2["n_reads"] == 0
        and fr2["first_pick_is_last_forced_label"] is None)

    # 8. counters + analysis on the synthetic set
    from valence_core.session import DescriptiveCounters
    cnts = DescriptiveCounters(declared=R.DECLARED_COUNTERS)
    for r in recs + [brk, fr, fr2]:
        R.tally(cnts, r)
    rep = cnts.report()
    chk("counters tabulate over all sessions incl. excluded (rule 23)",
        rep["n_sessions"] == 15 and rep["counters"]["content_exclusion"]["by_key"].get("null_response") == 2
        and rep["tabulated_over_excluded_too"], rep["counters"]["content_exclusion"])
    an = R.analyze_format(recs[:4] + [brk, fr, fr2])
    chk("analyze_format: break rate k/n over all-with-a-pick and valid; alternation; share",
        an["first_pick_break"]["all_with_a_pick"]["n"] == 6 and an["first_pick_break"]["all_with_a_pick"]["k"] == 1
        and an["n_excluded_run_scope"] == 1 and an["n_excluded_strict"] == 2
        and an["strict_alternation"]["valid"]["n"] == 6 and an["audit_v3"]["content_exclusion_by_class"] == {"null_response": 2},
        (an["first_pick_break"]["all_with_a_pick"], an["n_excluded_run_scope"], an["n_excluded_strict"]))
    chk("anchors: e2a pooled strict alternation 157/187 and break 32/188 reproduce",
        (lambda A: A["e2a_all_arms"]["all"]["strict_alternation"]["k"] == 157 and A["e2a_all_arms"]["all"]["strict_alternation"]["n"] == 187
         and A["e2a_all_arms"]["all"]["first_pick_break"]["k"] == 32 and A["e2a_all_arms"]["all"]["first_pick_break"]["n"] == 188)(R.anchors()))

    # 9. the timing gate
    p_stop = R.projection({f: {"seconds": [300.0], "complete": [True]} for f in R.FORMATS})
    p_go = R.projection({f: {"seconds": [150.0], "complete": [True]} for f in R.FORMATS})
    chk("gate 8 h under the allocation (8/24/24 = 56 sessions): 3 x 300 s -> 4.67 h GO; 3 x 600 s -> 9.33 h STOP",
        p_go["verdict"] == "GO" and abs(p_go["projected_total_h"] - 56 * 150 / 3600) < 1e-9
        and p_stop["verdict"] == "GO" and abs(p_stop["projected_total_h"] - 56 * 300 / 3600) < 1e-9
        and R.projection({f: {"seconds": [600.0], "complete": [True]} for f in R.FORMATS})["verdict"] == "STOP")
    if os.path.exists(TIMING):
        real = R.assert_gate_admits(TIMING)
        chk("the EXISTING timing artifact projects GO under the raised gate (design patch §2: ~6.95 h)",
            real["verdict"] == "GO" and abs(real["projected_total_h"] - 6.95) < 0.02, f"{real['projected_total_h']:.3f} h")
    tmpd = os.environ.get("TMPDIR", "/tmp")
    tp = os.path.join(tmpd, "format_recon_selftest_timing.json")
    if os.path.exists(tp):
        os.remove(tp)
    refused_missing = False
    try:
        R.assert_gate_admits(tp)
    except SystemExit:
        refused_missing = True
    _pass = {f: {"PASS": True} for f in R.FORMATS}
    json.dump({"timed": {f: {"seconds": [600.0], "complete": [True]} for f in R.FORMATS}, "acceptance_on_timed_sessions": _pass}, open(tp, "w"))
    refused_stop = False
    try:
        R.assert_gate_admits(tp)
    except SystemExit:
        refused_stop = True
    json.dump({"timed": {f: {"seconds": [150.0], "complete": [True]} for f in R.FORMATS}, "acceptance_on_timed_sessions": _pass}, open(tp, "w"))
    admitted = R.assert_gate_admits(tp)["verdict"] == "GO"
    os.remove(tp)
    chk("assert_gate_admits: refuses without artifact, refuses STOP, admits GO",
        refused_missing and refused_stop and admitted)
    try:
        R.projection({"F0": {"seconds": [1.0], "complete": [True]}})
        incomplete = False
    except SystemExit:
        incomplete = True
    chk("projection refuses an incomplete timing set (a skipped format is not a pass)", incomplete)

    # 10. resume / checkpoint discipline
    cp = os.path.join(tmpd, "format_recon_selftest_F0.checkpoint")
    if os.path.exists(cp):
        os.remove(cp)
    first_listed = lambda prefix, a, b: (a, {"pick": a, "p_a": 0.6, "p_b": 0.4, "label_mass": 0.5,
                                                "top1_id": 0, "top1_is_label": True, "verify_kl": 0.0})
    fa = _FakeAdapter(TEXTS)
    res = R.run_format(fa, "F0", 24, tasks, audit3, [], [], others, seed=R.DRAW_SEED,
                       checkpoint_path=cp, limit=1, progress=lambda s: None, _read_override=first_listed)
    chk("run_format --limit 1 runs exactly one session and checkpoints it",
        len(res["sessions"]) == 1 and os.path.exists(cp) and fa.calls == 10)
    refused = False
    try:
        R.run_format(_FakeAdapter(TEXTS), "F0", 24, tasks, audit3, [], [], others, seed=R.DRAW_SEED,
                     checkpoint_path=cp, limit=1, progress=lambda s: None, _read_override=first_listed)
    except SystemExit:
        refused = True
    chk("an existing checkpoint without --resume is refused (trap 22)", refused)
    fa2 = _FakeAdapter(TEXTS)
    res2 = R.run_format(fa2, "F0", 24, tasks, audit3, [], [], others, seed=R.DRAW_SEED,
                        checkpoint_path=cp, resume=True, limit=1, progress=lambda s: None, _read_override=first_listed)
    chk("--resume --limit 1 with one on disk runs NOTHING (limit counts on-disk, trap 36)",
        len(res2["sessions"]) == 1 and fa2.calls == 0)
    res3 = R.run_format(_FakeAdapter(TEXTS), "F0", 24, tasks, audit3, [], [], others, seed=R.DRAW_SEED,
                        checkpoint_path=cp, resume=True, limit=3, progress=lambda s: None, _read_override=first_listed)
    chk("--resume --limit 3 completes to 3 on disk, indices 0,1,2 (skip-only)",
        [r["session"] for r in res3["sessions"]] == [0, 1, 2])
    mismatch_refused = True
    sched24 = R.build_schedule(24, np.random.default_rng(R.DRAW_SEED))
    for bad in ({"seed": 1}, {"scope": "e2b"}, {"fmt": "F1"}, {"temp": 0.9}, {"audit_sha16": "zzz"}):
        ident = R.run_identity(bad.get("fmt", "F0"), bad.get("seed", R.DRAW_SEED),
                               bad.get("scope", "e2a"), bad.get("temp", C.TEMP), bad.get("audit_sha16", ""))
        try:
            R.load_checkpoint(cp, ident, 24, sched24)
            mismatch_refused = False
        except SystemExit:
            pass
    ident_ok = R.run_identity("F0", R.DRAW_SEED, "e2a", C.TEMP, "")
    R.load_checkpoint(cp, ident_ok, 24, sched24)   # the identical identity loads
    ck8 = R.load_checkpoint(cp, ident_ok, 8, R.build_schedule(8, np.random.default_rng(R.DRAW_SEED)))   # reallocation 24 -> 8 with 3 on disk: allowed
    try:
        R.load_checkpoint(cp, ident_ok, 2, R.build_schedule(2, np.random.default_rng(R.DRAW_SEED))); shrink_refused = False
    except SystemExit:
        shrink_refused = True
    try:
        R.load_checkpoint(cp, ident_ok, 24, R.build_schedule(24, np.random.default_rng(7))); prefix_refused = False
    except SystemExit:
        prefix_refused = True
    chk("reallocation: 24 -> 8 resumes 3 on-disk sessions; 24 -> 2 (orphaning s2) refused; a foreign schedule prefix refused",
        len(ck8["sessions"]) == 3 and shrink_refused and prefix_refused)
    chk("load_checkpoint refuses a foreign seed / scope / format / temp / audit sha", mismatch_refused)
    os.remove(cp)

    # 11. sham source guard + bars
    src = open(os.path.join(REPO, "valence_core/formats/recon.py")).read()
    body = "\n".join(l for l in src.split('"""')[2::2])  # code outside docstrings
    forbidden = [w for w in ("Injection", "at_frac", "load_axis", "statepresent", "cached=True", "e2b.", "from ..e2b")
                 if w in body]
    chk("recon.py's code names no injection / axis / quarantine / cached-path symbol", not forbidden, forbidden)
    chk("quarantined primitive absent from sys.modules", "valence_core.e2b.statepresent" not in sys.modules)
    bars = bars_or_stop()
    chk("e2d's three declared bars fire and stay silent (7 cases, both directions)", len(bars) == 3)
    chk("audit of record composes v2 + content-class v4; the v2 sha16 is RECOMPUTED and matches the declared",
        AUDIT_VERSION.startswith("audit-v3") and len(cfg.get("sha16", "")) == 16 and cfg["sha16_recomputed"] == cfg["sha16"], cfg.get("sha16"))
    _tampered = dict(cfg); _tampered["junk_regex"] = list(_tampered["junk_regex"]) + ["x"]
    chk("a tampered audit body no longer matches its declared sha16", audit_sha16_recomputed(_tampered) != cfg["sha16"])

    # 12. review findings of 2026-09-06, each pinned
    _me = open(os.path.abspath(__file__)).read()
    _smuggled = _me.rsplit("def stage_time(args):\n", 1)
    _smuggled = _smuggled[0] + "def stage_time(args):\n    _read_override = 1\n" + _smuggled[1]
    chk("override guard: clean on this file, fires on a copy that smuggles the override into a stage",
        _assert_no_override_in_stages() is True and _fires(_smuggled))
    tr = R.run_session(_FakeAdapter(["* * *"] + TEXTS), "F0", 6, sched[6], tasks, audit3, [], [], others,
                       _read_override=first_listed)
    chk("a truncated timed session is NOT complete; a full one is",
        tr["complete"] is False and recs[0]["complete"] is True and R.is_complete(recs[0]))
    pr = R.projection({"F0": {"seconds": [230.0], "complete": [True]}, "F1": {"seconds": [23.0, 230.0], "complete": [False, True]},
                       "F2": {"seconds": [230.0], "complete": [True]}}, n_per_format={"F0": 24, "F1": 24, "F2": 24}, gate_hours=4.0)
    chk("projection uses COMPLETE sessions only (a 23 s truncated session is set aside)",
        pr["verdict"] == "STOP" and abs(pr["projected_total_h"] - 4.6) < 1e-9 and pr["per_format"]["F1"]["n_complete"] == 1
        and pr["per_format"]["F1"]["truncated_seconds_excluded_from_projection"] == [23.0])
    try:
        R.projection({f: {"seconds": [23.0], "complete": [False]} for f in R.FORMATS}); none_complete = False
    except SystemExit:
        none_complete = True
    chk("projection refuses a format with no complete timed session", none_complete)
    tp2 = os.path.join(tmpd, "format_recon_selftest_timing2.json")
    good_acc = {f: {"PASS": True} for f in R.FORMATS}
    json.dump({"timed": {f: {"seconds": [150.0], "complete": [True]} for f in R.FORMATS}, "acceptance_on_timed_sessions": good_acc}, open(tp2, "w"))
    admitted2 = R.assert_gate_admits(tp2)["verdict"] == "GO"
    bad_acc = dict(good_acc); bad_acc["F1"] = {"PASS": False, "bars_fired": ["BAR round_degeneracy 2/10"]}
    json.dump({"timed": {f: {"seconds": [150.0], "complete": [True]} for f in R.FORMATS}, "acceptance_on_timed_sessions": bad_acc}, open(tp2, "w"))
    try:
        R.assert_gate_admits(tp2); refused_acc = False
    except SystemExit:
        refused_acc = True
    json.dump({"timed": {f: {"seconds": [150.0], "complete": [True]} for f in R.FORMATS}}, open(tp2, "w"))
    try:
        R.assert_gate_admits(tp2); refused_noacc = False
    except SystemExit:
        refused_noacc = True
    os.remove(tp2)
    chk("gate refuses a FAILED timed-session acceptance and a missing acceptance; admits PASS", admitted2 and refused_acc and refused_noacc)
    cp2 = os.path.join(tmpd, "format_recon_selftest_F1.checkpoint")
    if os.path.exists(cp2):
        os.remove(cp2)
    R.run_format(_FakeAdapter(TEXTS), "F1", 24, tasks, audit3, [], [], others, seed=R.DRAW_SEED, audit_sha16="abc",
                 checkpoint_path=cp2, limit=1, progress=lambda s: None, _read_override=first_listed)
    drift = 0
    for kw in ({"temp": 0.9}, {"audit_sha16": "zzz"}, {"scope": "e2b"}):
        try:
            R.run_format(_FakeAdapter(TEXTS), "F1", 24, tasks, audit3, [], [], others, seed=R.DRAW_SEED,
                         audit_sha16=kw.get("audit_sha16", "abc"), temp=kw.get("temp", C.TEMP), scope=kw.get("scope", "e2a"),
                         checkpoint_path=cp2, resume=True, limit=1, progress=lambda s: None, _read_override=first_listed)
        except SystemExit:
            drift += 1
    same = R.run_format(_FakeAdapter(TEXTS), "F1", 24, tasks, audit3, [], [], others, seed=R.DRAW_SEED, audit_sha16="abc",
                        checkpoint_path=cp2, resume=True, limit=1, progress=lambda s: None, _read_override=first_listed)
    os.remove(cp2)
    chk("resume refuses temp / audit-sha / scope drift and admits the identical identity",
        drift == 3 and len(same["sessions"]) == 1 and same["identity"]["temp"] == C.TEMP)
    chk("record's steered / round_path_cached are derived from the generate call (all False)",
        all(x["steered"] is False and x["round_path_cached"] is False for x in recs[0]["rounds"] + recs[0]["choices"])
        and recs[0]["sham_only"] and not recs[0]["round_path_cached"] and recs[0]["temp"] == C.TEMP)
    ow = os.path.join(tmpd, "format_recon_selftest_sessions.json")
    json.dump({"complete": True, "n_on_disk": 24}, open(ow, "w"))
    try:
        R.refuse_overwrite(ow, False, 1); ow_refused = False
    except SystemExit:
        ow_refused = True
    R.refuse_overwrite(ow, True, 24)
    json.dump({"complete": False, "n_on_disk": 3}, open(ow, "w"))
    R.refuse_overwrite(ow, False, 5)
    os.remove(ow)
    chk("a partial run cannot overwrite a complete artifact; complete-over-complete and partial-over-partial allowed", ow_refused)
    an2 = R.analyze_format([fr2])
    chk("analysis on one truncated session: rates None, features BELOW FLOOR with diagnosis, no crash",
        an2["first_pick_break"]["all_with_a_pick"]["rate"] is None and an2["n_complete"] == 0
        and all(v["diagnosis"] for v in an2["features_rule28a"].values()) and an2["exclusion_scope_of_run"] == "e2a")
    an3 = R.analyze_format(recs[:4] + [brk, fr, fr2])
    _fl = R.feature_floor(recs[0]["format"])
    chk("rule 28(a) floors declared per format (ceil 2/3 n: F0 6, F1/F2 16) and reported with domain + decidable n",
        {k: v["floor"] for k, v in an3["features_rule28a"].items()} == {"first_pick_break": _fl, "strict_alternation": _fl, "session_share": _fl}
        and an3["features_rule28a"]["first_pick_break"]["decidable"] == 6 and R.feature_floor("F0") == 6 and R.feature_floor("F1") == 16 and R.feature_floor("F2") == 16)
    rfz = R.run_session(_FakeAdapter(["The ferry glides across misty water at first light, and I won't pretend the gulls approve."] + TEXTS), "F0", 8, sched[8], tasks, audit3, [], [], others,
                        _read_override=first_listed)
    rc_ = R.refusal_counts([rfz, fr2])
    chk("refusal counts per round position: a declining predicate with content counts as predicate-only; the '* * *' null counts as null_response",
        rc_["by_round_position"]["forced0"] == {"n": 2, "null_response": 1, "declining_predicate_any": 1} and rc_["total"]["null_response"] == 1
        and rfz["rounds"][0]["degen"] is None, rc_["by_round_position"].get("forced0"))
    A = R.anchors()
    chk("anchors carry both domains: e2a all 157/187 & 32/188; valid 154/184 & 30/184",
        A["e2a_all_arms"]["all"]["strict_alternation"]["k"] == 157 and A["e2a_all_arms"]["valid"]["strict_alternation"]["k"] == 154
        and A["e2a_all_arms"]["valid"]["strict_alternation"]["n"] == 184 and A["e2a_all_arms"]["valid"]["first_pick_break"]["k"] == 30)
    n_ok = sum(1 for r in results if r[1])
    print("-" * 78)
    print(f"  {n_ok}/{len(results)} selftest checks pass", flush=True)
    return 0 if n_ok == len(results) else 1


# ============================================================================
# stages
# ============================================================================
def header(args, adapter, audit_cfg, tasks, bars):
    print(f"  SHAM ONLY: no steering, no axis, no random direction; every forward vanilla; round path UNCACHED "
          f"(the uncached path of record); choice reads = readout.choice_read(verify=True) + assert_construction_stable", flush=True)
    print(f"  design block 2026-09-06 §4; descriptive only; no bar; template recalibration for LOCK-k", flush=True)
    for f, spec in R.FORMATS.items():
        print(f"  {f}: {spec['title']}  [{' '.join(spec['order'])}]  -- {spec['purpose']}", flush=True)
    print(f"  allocation {R.N_PER_FORMAT} (8 cells; whole blocks; design patch 2026-09-06 §2; draw seed {args.draw_seed}); gate {args.gate_hours} h"
          + ("" if args.gate_hours == R.GATE_HOURS else f"  *** DECLARED DEVIATION: gate overridden from {R.GATE_HOURS} h ***"), flush=True)
    print(f"  roster of record (AMENDMENT 1 i): {', '.join('/'.join(p) for p in C.ROSTER)}", flush=True)
    nid = neutral_id_check(adapter)
    print(f"  neutral label (F1): {R.NEUTRAL_LABEL!r} id {nid} (selection artifact {R.NEUTRAL_SELECTION}; provisionally approved, design patch 2026-09-06 §2)", flush=True)
    hy = hygiene(tasks)
    print(f"  hygiene: rule 18 {len(hy['tags_checked'])} tags vs {hy['n_pool_texts']} paraphrases -> 0 hits; rule 28c wrapper -> 0 hits; "
          f"neutral absent from every roster {hy['neutral_outside_every_roster']['rosters_checked']}", flush=True)
    print(f"  audit of record: {AUDIT_VERSION}; v2 = e2b_audit_v2.json sha16 {audit_cfg['sha16']} "
          f"(recomputed {audit_cfg['sha16_recomputed']}, verified)", flush=True)
    print(f"  exclusion scope: {args.scope!r} (strict recovered beside); precedence: audit v3 first, lexical on unclaimed rounds (rule 28b)", flush=True)
    print(f"  declared bars (e2d's, verbatim; no new bar): {', '.join(b.name for b in bars)} -- verified to fire and stay silent", flush=True)
    print(f"  rule 28(a) floors declared (ceil 2/3 of n): { {f: R.feature_floor(f) for f in R.FORMATS} } per feature, on its domain (reported with diagnosis, never suppressed)", flush=True)
    print(f"  timing rule: only COMPLETE timed sessions ({R.N_FORCED} rounds + 6 reads) enter the projection; <= {R.MAX_TIMING_ATTEMPTS} attempts per format", flush=True)
    print(f"  tasks: {len(tasks)} x 4 paraphrases; STOP_CAP {R.STOP_CAP if hasattr(R, 'STOP_CAP') else 60}; temp {args.temp}", flush=True)


def load_model_and_inputs(args):
    from valence_core.adapters import qwen_or_explain
    assert_modules_absent(R.FORBIDDEN_MODULES)
    bars = bars_or_stop()
    audit3, audit_cfg = audit_of_record()
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    term_rx = json.load(open(os.path.join(DATA, "configs/f_termination_patterns.json")))["term_regex"]
    t0 = time.time()
    adapter = qwen_or_explain(__file__)
    print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    ban_ids, ban_strings = build_ban_list(adapter)
    header(args, adapter, audit_cfg, tasks, bars)
    print(f"  ban list: {len(ban_ids)} ids / {len(ban_strings)} strings (round generation only, never a read)", flush=True)
    return adapter, audit3, audit_cfg, tasks, term_rx, ban_ids, ban_strings, bars


def acceptance_for(recs, tasks, bars, counters):
    kls = [c["read"]["verify_kl"] for r in recs for c in r["choices"]]
    fmt_walk = R.verify_format_walk(recs, tasks) if recs else {"n_walked": 0, "n_reconstructed": 0, "all_ok": False}
    n_rounds = sum(len(r["rounds"]) + len(r["choices"]) for r in recs)
    n_v2 = counters.total("audit_degenerate")
    n_scaffold = sum(1 for r in recs for x in r["rounds"] + r["choices"]
                     if x["degen"] and str(x["degen"]).startswith("audit:special:"))
    fired = check_bars(bars, {"round_degeneracy": (n_v2, n_rounds),
                              "scaffold_absorption": (n_scaffold, max(n_rounds, 1)),
                              "template_breakage": (fmt_walk["n_walked"] - fmt_walk["n_reconstructed"], max(fmt_walk["n_walked"], 1))})
    absent = True
    try:
        assert_modules_absent(R.FORBIDDEN_MODULES)
    except SystemExit:
        absent = False
    acc = {"n_reads": len(kls), "kl_exactly_zero": sum(1 for k in kls if k == 0.0),
           "kl_max": max(kls) if kls else None,
           "kl_all_exact": bool(kls) and all(k == 0.0 for k in kls),
           "statepresent_absent": absent, "format_walk": fmt_walk, "bars_fired": fired,
           "sham_only_every_round": all(not x["steered"] for r in recs for x in r["rounds"] + r["choices"]),
           "round_degeneracy_domain": "v2 audit class over ALL rounds of the format (unprovoked by design: sham)",
           "no_verdict_content": True}
    acc["PASS"] = bool(acc["kl_all_exact"] and absent and fmt_walk["all_ok"] and not fired and acc["sham_only_every_round"])
    return acc


def _fires(src: str) -> bool:
    try:
        _assert_no_override_in_stages(src)
        return False
    except SystemExit:
        return True


def _assert_no_override_in_stages(src: str | None = None) -> bool:
    """The scripted read exists for the self-test only. Grep this file's stage
    functions for it so a future edit cannot smuggle it into a real run.

    Splits on the LAST occurrence of the stage_time definition line: the
    first occurrence is this function's own source (the review of 2026-09-06
    found the first version fired unconditionally on itself). Returns True
    when clean; raises otherwise. `src` is for the self-test only."""
    src = open(os.path.abspath(__file__)).read() if src is None else src
    marker = "def stage_time(args):"
    if src.count(marker) < 1:
        raise SystemExit("STRUCTURAL VIOLATION: stage_time definition not found")
    stages = src.rsplit(marker, 1)[1]
    if "_read_override" in stages:
        raise SystemExit("STRUCTURAL VIOLATION: _read_override referenced in a stage function")
    return True


def stage_time(args):
    _assert_no_override_in_stages()
    if os.path.exists(TIMING) and not args.resume:
        raise SystemExit(f"TIMING ARTIFACT EXISTS at {TIMING}; pass --resume to re-time on the same "
                         f"checkpoints, or move it aside. Never overwritten silently (trap 22).")
    for fmt in R.FORMATS:
        cp = sessions_path(fmt) + ".checkpoint"
        if os.path.exists(cp) and not args.resume:
            raise SystemExit(f"CHECKPOINT EXISTS at {cp}; --stage time needs --resume to continue it "
                             f"(the timed sessions are sessions of record) or move it aside.")
    adapter, audit3, audit_cfg, tasks, term_rx, ban_ids, ban_strings, bars = load_model_and_inputs(args)
    others = others_factory(tasks)
    os.makedirs(OUT, exist_ok=True)
    timed, recs_by, acc = {}, {}, {}
    from valence_core.session import DescriptiveCounters
    for fmt in R.FORMATS:
        cp = sessions_path(fmt) + ".checkpoint"
        print(f"\n=== TIMING {fmt}: schedule indices in order until ONE COMPLETE session is on disk "
              f"(<= {R.MAX_TIMING_ATTEMPTS} attempts) ===", flush=True)
        limit = 1
        while True:
            res = R.run_format(adapter, fmt, R.N_PER_FORMAT[fmt], tasks, audit3, ban_ids, term_rx, others,
                               temp=args.temp, scope=args.scope, seed=args.draw_seed,
                               audit_sha16=audit_cfg["sha16"], checkpoint_path=cp,
                               resume=os.path.exists(cp), limit=limit)
            recs = res["sessions"]
            if any(r["complete"] for r in recs):
                break
            if limit >= R.MAX_TIMING_ATTEMPTS:
                print(f"  STOP: no complete {fmt} session in {limit} attempts "
                      f"({[r['exclude_reason'] for r in recs]}); the design seat decides.", flush=True)
                return 1
            limit += 1
        recs_by[fmt] = recs
        timed[fmt] = {"sessions": [r["session"] for r in recs], "seconds": [r["seconds"] for r in recs],
                      "complete": [r["complete"] for r in recs],
                      "n_rounds_generated": [r["n_rounds_generated"] for r in recs],
                      "n_reads": [r["n_reads"] for r in recs],
                      "n_tok_generated": [sum(x["n_tok"] for x in r["rounds"] + r["choices"]) for r in recs],
                      "transcript_tokens_final": [len(adapter.encode(r["transcript"])) for r in recs],
                      "excluded": [r["excluded"] for r in recs],
                      "exclude_reason": [r["exclude_reason"] for r in recs]}
        for r in recs:
            print(f"\n--- {fmt} s{r['session']} transcript ({r['seconds']:.0f}s; "
                  f"{'COMPLETE' if r['complete'] else 'TRUNCATED'}; rule 25: read in full) ---", flush=True)
            print(r["transcript"], flush=True)
            print(f"--- end {fmt} s{r['session']}; excluded={r['excluded']} reason={r['exclude_reason']} "
                  f"strict={r['strict_excluded']} first-pick-break={r['first_pick_is_last_forced_label']} "
                  f"picks={[c['pick'] for c in r['choices']]} "
                  f"advisory={[x['advisory'] for x in r['rounds'] + r['choices'] if x['advisory']]} ---", flush=True)
        cnt = DescriptiveCounters(declared=R.DECLARED_COUNTERS)
        for r in recs:
            R.tally(cnt, r)
        acc[fmt] = acceptance_for(recs, tasks, bars, cnt)
    # acceptance and projection computed BEFORE the artifact is written (trap 6)
    proj = R.projection({f: {"seconds": v["seconds"], "complete": v["complete"]} for f, v in timed.items()},
                        gate_hours=args.gate_hours)
    acc_all = all(a["PASS"] for a in acc.values())
    out = {"stage": "time", "item": "format recon (design block 2026-09-06 §4)",
           "sham_only": all(r["sham_only"] for rs in recs_by.values() for r in rs),
           "round_path_cached": any(r["round_path_cached"] for rs in recs_by.values() for r in rs),
           "formats": R.FORMATS, "n_per_format": R.N_PER_FORMAT,
           "neutral_label": {"label": R.NEUTRAL_LABEL, "token_id": R.NEUTRAL_TOKEN_ID, "code_choice_flagged": True},
           "roster_of_record": [list(p) for p in C.ROSTER], "draw_seed": args.draw_seed, "scope": args.scope,
           "temp": args.temp, "audit_of_record": {"version": AUDIT_VERSION, "v2_sha16": audit_cfg["sha16"]},
           "identity": {f: R.run_identity(f, args.draw_seed, args.scope, args.temp, audit_cfg["sha16"]) for f in R.FORMATS},
           "provenance": adapter.provenance(), "ban_list": {"n_ids": len(ban_ids), "n_strings": len(ban_strings)},
           "declared_bars": [b.__dict__ for b in bars],
           "declared_features_rule28a": {f: [s.__dict__ for s in R.declared_features(f)] for f in R.FORMATS},
           "timed": timed, "projection": proj, "gate_hours": args.gate_hours,
           "gate_overridden": args.gate_hours != R.GATE_HOURS,
           "acceptance_on_timed_sessions": acc, "acceptance_all_pass": acc_all, "sessions": recs_by,
           "_no_verdict": "descriptive; the projection is a cost, not a result"}
    with open(TIMING, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print("\n" + "=" * 74)
    for f, v in proj["per_format"].items():
        print(f"  {f}: {v['mean_session_s_complete']:.0f} s per COMPLETE session ({v['n_complete']} of {v['n_timed']} timed) "
              f"-> {v['projected_h']:.2f} h for {v['n']}")
    print(f"  PROJECTION: {proj['projected_total_h']:.2f} h for {R.N_PER_FORMAT}  vs gate {args.gate_hours} h  ->  {proj['verdict']}")
    print(f"  acceptance on the timed sessions: { {f: a['PASS'] for f, a in acc.items()} }"
          + ("" if acc_all else f"  *** FAILED: { {f: a['bars_fired'] for f, a in acc.items() if not a['PASS']} } -- STOP, escalate ***"))
    print(f"  wrote {TIMING}")
    if proj["verdict"] != "GO" or not acc_all:
        print("  STOP -- the design seat decides (design block §4). Code does not run past its own STOP "
              "or self-adjudicate a fired bar.")
        return 1
    return 0


def stage_run(args):
    _assert_no_override_in_stages()
    proj = R.assert_gate_admits(TIMING, args.gate_hours)      # structural (trap 32): acceptance + projection
    print(f"  timing gate: projected {proj['projected_total_h']:.2f} h <= {args.gate_hours} h -> GO; "
          f"timed sessions' acceptance PASS on every format", flush=True)
    adapter, audit3, audit_cfg, tasks, term_rx, ban_ids, ban_strings, bars = load_model_and_inputs(args)
    others = others_factory(tasks)
    fmts = list(R.FORMATS) if args.format == "all" else [args.format]
    rc = 0
    for fmt in fmts:
        cp = sessions_path(fmt) + ".checkpoint"
        path = sessions_path(fmt) if not args.out_name else os.path.join(OUT, args.out_name.replace("{fmt}", fmt))
        print(f"\n=== RUN {fmt}: n = {R.N_PER_FORMAT[fmt]} ===", flush=True)
        # --resume is explicit: an existing checkpoint without it is refused by run_format (trap 22).
        res = R.run_format(adapter, fmt, R.N_PER_FORMAT[fmt], tasks, audit3, ban_ids, term_rx, others,
                           temp=args.temp, scope=args.scope, seed=args.draw_seed,
                           audit_sha16=audit_cfg["sha16"], checkpoint_path=cp,
                           resume=args.resume, limit=args.limit)
        recs, counters = res["sessions"], res["counters"]
        acc = acceptance_for(recs, tasks, bars, counters)
        complete = len(recs) == R.N_PER_FORMAT[fmt]
        if not args.out_name:
            R.refuse_overwrite(path, complete, len(recs))
        out = {"stage": "run", "item": "format recon (design block 2026-09-06 §4)", "format": fmt,
               "spec": R.FORMATS[fmt], "sham_only": all(r["sham_only"] for r in recs),
               "round_path_cached": any(r["round_path_cached"] for r in recs),
               "n_registered": R.N_PER_FORMAT[fmt], "n_on_disk": len(recs), "complete": complete,
               "n_history": res["n_history"], "identity": res["identity"],
               "f1_cedar_timing_sessions_set_aside": (fmt == "F1"),
               "neutral_label": {"label": R.NEUTRAL_LABEL, "token_id": R.NEUTRAL_TOKEN_ID, "code_choice_flagged": True} if fmt == "F1" else None,
               "roster_of_record": [list(p) for p in C.ROSTER], "draw_seed": args.draw_seed, "scope": args.scope,
               "temp": args.temp, "audit_of_record": {"version": AUDIT_VERSION, "v2_sha16": audit_cfg["sha16"]},
               "provenance": adapter.provenance(), "ban_list": {"n_ids": len(ban_ids), "n_strings": len(ban_strings)},
               "declared_bars": [b.__dict__ for b in bars], "firing_cases": [list(c) for c in C.FIRING_CASES],
               "declared_features_rule28a": [f.__dict__ for f in R.declared_features(fmt)],
               "timing_gate": proj, "gate_overridden": args.gate_hours != R.GATE_HOURS,
               "acceptance": acc, "counters": counters.report(),
               "exclusions": {"run_scope": sum(1 for r in recs if r["excluded"]), "strict": sum(1 for r in recs if r["strict_excluded"]),
                              "reasons_run_scope": [r["exclude_reason"] for r in recs if r["excluded"]]},
               "wall_clock": {"per_session_s": res["per_session_seconds"],
                              "mean_session_s": float(np.mean(res["per_session_seconds"])) if res["per_session_seconds"] else None},
               "sessions": recs, "_no_verdict": "descriptive; no bar; scripts/format_recon.py --analyze reports"}
        with open(path, "w") as fh:
            json.dump(out, fh, indent=1, default=float)
        print(f"  {fmt}: {len(recs)}/{R.N_PER_FORMAT[fmt]} on disk{'' if complete else ' (PARTIAL)'}; acceptance {'PASS' if acc['PASS'] else 'FAIL'}; "
              f"KL {acc['kl_exactly_zero']}/{acc['n_reads']} exact; walk {acc['format_walk']['n_reconstructed']}/{acc['format_walk']['n_walked']}; "
              f"bars {acc['bars_fired'] or 'none'}; excluded {out['exclusions']['run_scope']} ({args.scope}) / {out['exclusions']['strict']} strict; wrote {path}", flush=True)
        if not acc["PASS"]:
            print("  STOP -- write the entry and flag; Code does not self-adjudicate a failed acceptance or a fired bar.", flush=True)
            rc = 1
            break
    return rc


def analyze(args):
    src = args.source
    by, label = {}, {}
    if src == "timing":
        t = json.load(open(TIMING))
        for f in R.FORMATS:
            recs = t["sessions"].get(f)
            if recs:
                by[f] = recs; label[f] = f"timing artifact ({len(recs)} session{'s' if len(recs) != 1 else ''}; {sum(1 for r in recs if r.get('complete'))} complete)"
            else:
                label[f] = "MISSING from the timing artifact"
    else:
        for f in R.FORMATS:
            p = sessions_path(f) + (".checkpoint" if src == "checkpoint" else "")
            if not os.path.exists(p):
                label[f] = f"MISSING ({p})"
                continue
            d = json.load(open(p))
            recs = d["sessions"]
            comp = (len(recs) == R.N_PER_FORMAT[f]) if src == "checkpoint" else bool(d.get("complete"))
            by[f] = recs
            label[f] = f"{'checkpoint' if src == 'checkpoint' else 'sessions file'} ({len(recs)} sessions{'' if comp else ', PARTIAL'})"
    missing = [f for f in R.FORMATS if f not in by]
    if not by:
        raise SystemExit(f"nothing to analyze from source {src!r}: {label}")
    out = {"item": "format recon analysis (descriptive; no bar)", "source": src, "labels": label,
           "formats_missing": missing,
           "n_per_format_registered": dict(R.N_PER_FORMAT), "per_format": {f: R.analyze_format(recs) for f, recs in by.items()},
           "anchors": R.anchors(), "definitions": {
               "strict_alternation": "all six free picks alternate (habit.strictly_alternates); the format rows report it over VALID sessions (run scope) with >= 2 picks, beside all-with-2+-picks and valid-with-six; anchors carry both `all` and `valid` domains",
               "first_pick_break": "first free pick IS the last forced label; every format ends its forced phase on tag_minus, so this is the alternation habit broken (habit.follows_habit == False); in F2 it is also the stay rate; reported over all-with-a-pick (the rule-23 domain) and over valid; anchors carry both domains",
               "session_share": "share of free picks on the nominal first label (tag_plus); e2a share_all_choices with the nominal pole; valid sessions",
               "audit_v3": "counts over ALL rounds of ALL sessions incl. excluded (rule 23): v2 audit by category, exclusion-bearing content class, advisory class, lexical",
               "tokens_forced_end_to_first_read": "prefix length at the first read minus the transcript length after each forced round (the retention interval, in tokens)",
               "features_rule28a": f"declared floors ceil(2/3 x n) = { {f: R.feature_floor(f) for f in R.FORMATS} } decidable on the feature's domain; a figure below its floor is reported WITH its diagnosis, never suppressed",
               "refusals": "per round position: null_response exclusions and rounds matching the adopted declining-predicate shape at all (residual ignored); the imperative shape is a declared miss counted only by the read"}}
    path = os.path.join(OUT, args.out_name or "format_recon_analysis.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    r3 = lambda x: None if x is None else round(x, 3)
    print(f"FORMAT RECON ANALYSIS (source {src}) -- descriptive, no bar")
    for f in R.FORMATS:
        if f not in by:
            print(f"  {f}: {label[f]}")
            continue
        a = out["per_format"][f]
        sa, fb, sh = a["strict_alternation"]["valid"], a["first_pick_break"]["all_with_a_pick"], a["session_share_on_first_label"]
        print(f"  {f} [{label[f]}]: n {a['n_sessions']}, complete {a['n_complete']}, valid {a['n_valid_run_scope']} ({a['exclusion_scope_of_run']}; strict-excluded {a['n_excluded_strict']}); "
              f"strict-alt {sa['k']}/{sa['n']} = {r3(sa['rate'])}; first-pick break {fb['k']}/{fb['n']} = {r3(fb['rate'])}; "
              f"share(first label) {r3(sh['pooled_over_choices'])} over {sh['n_choices']} choices; "
              f"v2 {a['audit_v3']['v2_audit_by_category']} content-excl {a['audit_v3']['content_exclusion_by_class']} advisory {a['audit_v3']['content_advisory_by_class']} lexical {a['audit_v3']['lexical_by_tag']}; "
              f"KL {a['reads']['kl_exactly_zero']}/{a['reads']['n']} exact; mean {a['seconds']['mean'] and round(a['seconds']['mean'])} s/session")
        print(f"      n_tok by phase: { {ph: round(v['mean'], 1) for ph, v in a['per_round'].items()} }")
        print(f"      tokens forced-end -> first read: { {ph: round(v['mean']) for ph, v in a['tokens_forced_end_to_first_read'].items()} }")
        print(f"      rule 28(a): { {k: (v['decidable'], v['floor'], 'ok' if v['diagnosis'] is None else 'BELOW FLOOR') for k, v in a['features_rule28a'].items()} }")
        rf = a["refusals"]
        print(f"      refusals: total null_response {rf['total']['null_response']}, declining-predicate {rf['total']['declining_predicate_any']} of {rf['total']['n']} rounds; by position { {ph: (v['null_response'], v['declining_predicate_any']) for ph, v in rf['by_round_position'].items()} }")
    an = out["anchors"]
    def fmt_anchor(k, v):
        return (f"{k} alt {r3(v['all']['strict_alternation']['rate'])} all / {r3(v['valid']['strict_alternation']['rate'])} valid; "
                f"break {r3(v['all']['first_pick_break']['rate'])} all / {r3(v['valid']['first_pick_break']['rate'])} valid")
    print("  anchors: " + " | ".join(fmt_anchor(k, v) for k, v in an.items()))
    if missing:
        print(f"  MISSING formats (not analysed, not a pass): {missing}")
    print(f"  wrote {path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--stage", choices=("time", "run"))
    ap.add_argument("--analyze", action="store_true")
    ap.add_argument("--source", choices=("sessions", "timing", "checkpoint"), default="sessions")
    ap.add_argument("--format", choices=("F0", "F1", "F2", "all"), default="all")
    ap.add_argument("--limit", type=int, default=0, help="stop once this many sessions are ON DISK for the format (resumed ones count)")
    ap.add_argument("--resume", action="store_true", help="continue a checkpoint of the SAME schedule; skip-only")
    ap.add_argument("--draw-seed", type=int, default=R.DRAW_SEED)
    ap.add_argument("--scope", choices=("e2a", "e2b"), default="e2a")
    ap.add_argument("--temp", type=float, default=C.TEMP)
    ap.add_argument("--gate-hours", type=float, default=R.GATE_HOURS,
                    help="the §4 STOP threshold; any other value is a DECLARED DEVIATION written into the artifact")
    ap.add_argument("--out-name", default="", help="analysis / sessions file name override (never overwrite a committed artifact silently; trap 22)")
    ap.add_argument("--check-gate", action="store_true",
                    help="model-free: recompute the projection from the EXISTING timing artifact under the current allocation and gate; exit 0 on GO")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.check_gate:
        print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)
        p = R.assert_gate_admits(TIMING, args.gate_hours)
        for f, v in p["per_format"].items():
            print(f"  {f}: {v['mean_session_s_complete']:.0f} s per complete session x {v['n']} = {v['projected_h']:.2f} h")
        print(f"  PROJECTION {p['projected_total_h']:.2f} h for {p['n_per_format']} vs gate {args.gate_hours} h -> {p['verdict']}; "
              f"timed-session acceptance PASS on every format (asserted)")
        return 0
    if args.stage or args.analyze:
        print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)
    if args.analyze:
        return analyze(args)
    if args.stage == "time":
        return stage_time(args)
    if args.stage == "run":
        return stage_run(args)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
