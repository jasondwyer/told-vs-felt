"""The F3 session loop, Qwen (PROPOSAL-m v1.11 §2.1-§2.2 m:159, m:174; §2.6 m:261, m:263, m:265; §2.7
m:267; §3 m:271; §4 m:308; m:48).

ONE SESSION. ``transcript = banner`` (§2.5's bytes for the arm). Forced rounds ri = 0..3 in F2 block
order; each generated as ``adapter.generate(transcript, seg, injections=(), seed, TEMP 0.7, STOP_CAP
60, ban_ids, cached=path_cached)`` after rule 28(d)(a)'s boundary assertion in both forms
(``scaffold.assert_boundary``), classified by the audit wrapper (v2 -> echo -> v4 content -> own-pair
lexical, m:261 -- ``valence_core.m.audit.QwenTaskRoundAudit``, imported), recorded, appended as
``seg + text + "\\n"``. Free choices ci = 0..5:

  1. the reasoning block (m:174) -- ``[round {n} | reasoning]``, ``Reasoning (one line):`` -- and one
     model line under the newline stop at the reasoning cap (60, or 120 after G-TIME-F3's trigger),
     the frozen ban list active (m:265), ``injections=()``, ``cached=path_cached`` (m:267: "Qwen rounds
     (and, in Q-F3, reasoning lines) run cached ... iff that unit's G-ID passes"), then ``"\\n"``;
  2. its classes (``lines.classify_line``: empty, cap without a newline, reasoning-line echo) and its
     scaffold hits; a hit is the hair trigger, an exclusion event that ends the session there (the
     seat's Q8), so no read follows it;
  3. the unchanged menu block, the insulated vanilla read on ``transcript + menu`` (state-present
     asserted absent before every read, KL exactly 0.0), the pick line ``" {pick}\\n"``, the chosen
     round as F0m's.

The reasoning line never reaches v2, v3, the task-round echo class or lexical and never enters
``earlier`` (m:265, "Exempt from v2/v3, the task-round echo class, lexical, and `earlier`").

SESSION END (f1's rule, lenient scope; m:261, m:271, m:308; the seat's Q8). A forced round ends the
session on any claim (excluded at forced, no read). A reasoning line's scaffold fire ends it (excluded
at reasoning; pre-pick on line 1). A free round ends it only on a lexical claim, after that round is
recorded. A free v2, echo or content claim is post-choice degeneracy and ends nothing. A
``scaffold_absorption`` in a task round is the hair trigger: recorded, the session returns at once
(the stage stops, m:271).

Nothing here prints. The record is pick-bearing; printing goes only through ``readrule``.
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from valence_core.e2d import config as e2d_config
from valence_core.e2d.runner import LOW_LABEL_MASS
from valence_core.m import audit as m_audit
from valence_core.m import resume as m_resume
from valence_core.session import build_ban_list
from valence_core.session_e2a import STOP_CAP

from . import guard, lines
from . import scaffold as sc_mod

E2A_BAN_LIST_PATH = Path(m_audit.E2A_BAN_LIST_PATH)
TEMP = e2d_config.TEMP                  # 0.7 (m:159, m:172)
CHOICE_WINDOW = 8192                    # m:159, rule 28(d): the read window, no encode limit


def qwen_ban_list(adapter, path: str | os.PathLike = E2A_BAN_LIST_PATH) -> tuple[list[int], list[str]]:
    """The generation ban list = the frozen e2a ban-list file, asserted (m:261, m:265)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): the procedure of valence_core.m.runner_qwen.qwen_ban_list
    # (which mf3 may not import, N1): the frozen file loaded with path= (its absence a STOP, never a
    # rebuild), asserted by audit.assert_qwen_scaffold, then rebuilt from the live adapter with no path
    # and required equal (ids and strings).
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"BAN LIST MISSING: {p} (the frozen e2a ban list) -- refusing to rebuild it")
    ids, strings = build_ban_list(adapter, path=str(p))
    m_audit.assert_qwen_scaffold(ids, strings)
    live_ids, live_strings = build_ban_list(adapter)
    if sorted(int(i) for i in live_ids) != sorted(int(i) for i in ids) \
            or sorted(str(x) for x in live_strings) != sorted(str(x) for x in strings):
        raise SystemExit("BAN LIST MISMATCH: the live adapter's rebuilt scaffold ban list differs from the "
                         f"frozen e2a file {p} (ids or strings) -- refusing to generate")
    return [int(i) for i in ids], [str(x) for x in strings]


def assert_qwen_adapter(adapter) -> None:
    """Rule 28(d) on the Qwen adapter: the 8192 read window, no encode limit anywhere."""
    if getattr(adapter, "choice_window", None) != CHOICE_WINDOW:
        raise SystemExit(f"READ WINDOW: adapter declares {getattr(adapter, 'choice_window', None)!r}, "
                         f"m reads at {CHOICE_WINDOW} (rule 28(d))")
    if getattr(adapter, "legacy_truncate", False) is not False or getattr(adapter, "max_length", None) is not None:
        raise SystemExit("ENCODE LIMIT: the Qwen adapter carries an encode limit; F3 generates with none "
                         "(rule 28(d)(b))")


@dataclass(frozen=True)
class F3Setup:
    audit: m_audit.QwenTaskRoundAudit
    ban_ids: tuple[int, ...]
    ban_strings: tuple[str, ...]
    term_rx: tuple[str, ...]
    audit_cfg: dict


def f3_startup(adapter, *, pool: Sequence[dict] | None = None) -> F3Setup:
    """Once per process: insulation, window, ban list, the audit of record, termination patterns."""
    guard.assert_insulated()
    assert_qwen_adapter(adapter)
    audit3, cfg = m_audit.qwen_audit_of_record()
    ids, strings = qwen_ban_list(adapter)
    if pool is None:
        pool, _ = sc_mod.pool_and_renders()
    return F3Setup(audit=m_audit.QwenTaskRoundAudit(audit3, pool, strings), ban_ids=tuple(ids),
                   ban_strings=tuple(strings), term_rx=sc_mod.load_term_rx(), audit_cfg=cfg)


def run_session_f3(adapter, scaffold: sc_mod.F3Scaffold, audit: m_audit.QwenTaskRoundAudit,
                   ban_ids: Sequence[int], *, path_cached: bool, temp: float = TEMP,
                   term_rx: Sequence[str]) -> dict:
    """One F3 session; returns its record (verified False until G-VER)."""
    guard.assert_insulated()
    sc = scaffold
    if type(path_cached) is not bool:
        raise TypeError("path_cached must be a bool (from guard.cached_path_admitted / gid_paths)")
    if not isinstance(sc, sc_mod.F3Scaffold) or sc.substrate != "qwen" or sc.format != sc_mod.FORMAT:
        raise ValueError("run_session_f3 runs F3 scaffolds only")
    if sc.path != ("cached" if path_cached else "uncached"):
        raise ValueError(f"path_cached={path_cached} disagrees with the scaffold's path {sc.path!r}")
    if not isinstance(audit, m_audit.QwenTaskRoundAudit):
        raise TypeError("audit must be audit.QwenTaskRoundAudit")
    # PIN (Code, declared at LOCK-m-F3 v0.1): m's defence in depth, carried -- a cached session outside
    # G-ID-F3 re-reads the licence itself on THIS adapter's backend at THIS cap (m:267, rule 2).
    if path_cached and sc.stage != "id" and not guard.cached_path_admitted(
            sc.stage, backend_identifier=m_resume.backend_identifier(adapter.provenance()),
            reasoning_cap=sc.reasoning_cap):
        raise SystemExit(f"CACHED PATH NOT LICENSED: Q-F3 {sc.stage} has no G-ID-F3 PASS on disk for this "
                         f"backend at reasoning cap {sc.reasoning_cap}; the session runs uncached or not at all (m:267)")
    own = (sc.P, sc.Q)
    lids = guard.label_ids(adapter, own)
    echo_lines = m_audit.qwen_echo_lines(sc.note_lines)
    log = sc_mod.F3Log(sc)
    earlier: list[str] = []
    t0 = time.perf_counter()
    stopped = False

    for ri in range(sc.n_forced):
        spec = sc.forced(ri)
        prefix = log.transcript
        sc_mod.assert_boundary(adapter, prefix, spec.seg)
        g = adapter.generate(prefix, spec.seg, injections=(), seed=spec.seed, temp=temp,
                             max_tokens=STOP_CAP, ban_ids=ban_ids, cached=path_cached)
        ra = audit.classify(g.text, render=spec.task_text, item=spec.item, earlier=earlier,
                            own_pair=own, echo_lines=echo_lines, phase="forced")
        log.add_round(spec, g, ra, term_rx)
        log.tb.add("round", "forced", ri, spec.seg)
        log.tb.add("generation", "forced", ri, g.text)
        log.tb.add("joiner", "forced", ri, "\n")
        earlier.append(g.text)
        if m_audit.qwen_ends(ra):
            log.exclude(ra, "forced")
        if ra.scaffold:
            log.hair_trigger(ra, "forced")
            stopped = True
            break
        if log.exclusion is not None:
            break

    if not stopped and log.exclusion is None:
        for ci in range(sc.n_free):
            rs = sc.reasoning(ci)
            prefix = log.transcript
            sc_mod.assert_boundary(adapter, prefix, rs.seg)
            g = adapter.generate(prefix, rs.seg, injections=(), seed=rs.seed, temp=temp,
                                 max_tokens=rs.cap, ban_ids=ban_ids, cached=path_cached)
            la = lines.classify_line(g.text, n_tok=int(len(g.token_ids)), cap=rs.cap,
                                     stop_reason=str(g.stop_reason), cap_hit=bool(g.cap_hit),
                                     echo_set=lines.echo_lines(sc.P, sc.Q, rs.n),
                                     scaffold_strings=audit.scaffold_strings)
            log.add_reasoning(rs, g, la)
            log.tb.add("reasoning", "free", ci, rs.seg)
            log.tb.add("reasoning_text", "free", ci, g.text)
            log.tb.add("reasoning_joiner", "free", ci, "\n")
            if la.scaffold:
                log.reasoning_hair(la, ci)
                break
            menu = sc.menu(ci)
            read_prefix = log.transcript + menu.menu
            cr = guard.insulated_read(adapter, read_prefix, menu.a, menu.b, lids)
            pick = cr.pick
            n_prefix = len(adapter.encode(read_prefix))
            log.tb.add("menu", "free", ci, menu.menu)
            log.tb.add("pick", "free", ci, f" {pick}\n")
            spec = sc.chosen(ci, pick)
            log.add_choice(menu, cr, pick, spec.role, n_prefix, LOW_LABEL_MASS)
            prefix = log.transcript
            sc_mod.assert_boundary(adapter, prefix, spec.seg)
            g = adapter.generate(prefix, spec.seg, injections=(), seed=spec.seed, temp=temp,
                                 max_tokens=STOP_CAP, ban_ids=ban_ids, cached=path_cached)
            ra = audit.classify(g.text, render=spec.task_text, item=spec.item, earlier=earlier,
                                own_pair=own, echo_lines=echo_lines, phase="free")
            log.add_round(spec, g, ra, term_rx)
            log.tb.add("round", "free", ci, spec.seg)
            log.tb.add("generation", "free", ci, g.text)
            log.tb.add("joiner", "free", ci, "\n")
            earlier.append(g.text)
            if m_audit.qwen_ends(ra):            # free: lexical only
                log.exclude(ra, "free")
            if ra.scaffold:
                log.hair_trigger(ra, "free")
                break
            if log.exclusion is not None:
                break
    # PIN (Code, declared at LOCK-m-F3 v0.1): seconds = perf_counter wall-clock of the whole session
    # (generations, reasoning lines and reads), to the millisecond; the hour cap's increment; never printed.
    return log.record(round(time.perf_counter() - t0, 3))


def _selftest(chk) -> None:
    from . import testing

    kit = testing.f3_kit()
    chk("mf3.runner: startup -- the e2a ban list (12 strings, ids), audit v2 sha16 pinned, termination "
        "patterns, TEMP 0.7, read window 8192",
        len(kit.ban_strings) == 12 and len(kit.ban_ids) == 12
        and kit.audit_cfg["sha16_recomputed"] == m_audit.AUDIT_V2_SHA16 and len(kit.term_rx) == 4
        and TEMP == 0.7 and run_session_f3.__kwdefaults__["temp"] == 0.7)
    suite = testing.suite()
    wrong = [(c.name, testing.outcome(r), c.want) for c, r, _ in suite if testing.outcome(r) != c.want]
    chk(f"mf3.runner: {len(suite)} scripted F3 sessions reach their declared outcomes (clean x12 over six "
        "templates and both starts; forced v2 ends; reasoning-line scaffold on line 1 (pre-pick) and line 3; "
        "line classes recorded without an end; free lexical ends; free v2 continues; task-round scaffold stops)",
        not wrong, wrong[:3])
    by = {c.name: r for c, r, _ in suite}
    clean = [r for c, r, _ in suite if c.name.startswith("f3 clean")]
    chk("mf3.runner: clean sessions -- 4 forced, 6 reasoning lines, 6 reads, 6 chosen rounds; valid, complete, "
        "domain, first pick on P",
        len(clean) == 12 and all(len(r["reasoning"]) == 6 and len(r["choices"]) == 6 and r["complete"]
                                 and not r["excluded"] and r["domain"] for r in clean)
        and all(r["first_free_pick_P"] is (r["choices"][0]["pick"] == r["cell"]["P"]) for r in clean))
    l1 = by["f3 reasoning line 1 scaffold: excluded pre-pick, no read"]
    l3 = by["f3 reasoning line 3 scaffold: excluded after two reads, domain kept"]
    chk("mf3.runner: a scaffold string on reasoning line 1 ends the session before any read -- excluded at "
        "reasoning (ci 0), out of the domain; on line 3 it ends after two reads, the domain kept (the seat's Q8)",
        l1["excluded"] and l1["exclusion"]["phase"] == "reasoning" and l1["exclusion"]["ci"] == 0
        and not l1["choices"] and l1["domain"] is False and l1["hair_triggers"][0]["phase"] == "reasoning"
        and l3["excluded"] and l3["exclusion"]["ci"] == 2 and len(l3["choices"]) == 2 and l3["domain"] is True
        and len(l3["reasoning"]) == 3 and not l3["complete"]
        and sc_mod.prepick_excluded(l1) and not sc_mod.prepick_excluded(l3))
    cls = by["f3 reasoning lines: empty, cap, echo, label -- classes only, no end"]
    got_cls = [x["audit"]["classes"] for x in cls["reasoning"]]
    chk("mf3.runner: reasoning-line classes are recorded and end nothing; the production empty line (text \"\" at "
        "the cap) writes \"Reasoning (one line):\\n\\n\" into the transcript; a line naming a label is not "
        "lexical-claimed and never enters earlier (m:265)",
        got_cls == [["empty", "cap_no_newline"], ["cap_no_newline"], ["echo"], [], [], ["empty", "cap_no_newline"]]
        and cls["reasoning"][0]["text"] == "" and "Reasoning (one line):\n\n[round" in cls["transcript"]
        and cls["complete"] and not cls["excluded"]
        and all(r["audit"]["claim"] is None for r in cls["rounds"]), got_cls)
    calls_ok = True
    for c, r, calls in suite:
        n_gen = len(r["rounds"]) + len(r["reasoning"])
        calls_ok &= len(calls) == n_gen
        calls_ok &= all(k["injections"] == () and k["cached"] is False and k["temp"] == TEMP
                        and k["ban_ids"] == kit.ban_ids for k in calls)
        line_calls = [k for k in calls if k["segment"].startswith("[round") and "| reasoning]" in k["segment"]]
        calls_ok &= [k["max_tokens"] for k in line_calls] == [x["cap"] for x in r["reasoning"]]
        calls_ok &= all(k["max_tokens"] == STOP_CAP for k in calls if k not in line_calls)
    chk("mf3.runner: the adapter saw injections=(), cached=False, TEMP 0.7 and the ban ids on every call; "
        "reasoning lines at the reasoning cap, task rounds at STOP_CAP 60", calls_ok)
    cap120 = by["f3 cap-120 A2s start 0"]
    chk("mf3.runner: at reasoning cap 120 the lines are generated at 120 and the record carries the cap",
        cap120["reasoning_cap"] == 120 and all(x["cap"] == 120 for x in cap120["reasoning"]))
    # the reads' context and the pieces' tiling
    ctx_ok = True
    for c, r, _ in suite:
        t = r["transcript"]
        pos = 0
        for p in r["pieces"]:
            ctx_ok &= p["start"] == pos
            pos = p["end"]
        ctx_ok &= pos == len(t)
        menus = [p for p in r["pieces"] if p["kind"] == "menu"]
        ctx_ok &= [ch["menu"] for ch in r["choices"]] == [t[p["start"]:p["end"]] for p in menus]
        rl = [p for p in r["pieces"] if p["kind"] == "reasoning_text"]
        ctx_ok &= [x["text"] for x in r["reasoning"]] == [t[p["start"]:p["end"]] for p in rl]
    chk("mf3.runner: pieces tile the transcript; each menu and reasoning line sits at its piece", ctx_ok)
    adapters_ok = []
    for nm, ad in (("merging", testing.F3MergingAdapter()), ("lossy decode", testing.F3LossyAdapter())):
        try:
            testing.run_case(testing.CASES[0], adapter=ad)
            adapters_ok.append(False)
        except SystemExit as e:
            adapters_ok.append("BOUNDARY INCIDENT" in str(e) and not ad.calls)
    chk("mf3.runner: rule 28(d)(a) halts before any generation on a collapsed token boundary and on a "
        "character-offset mismatch (both forms, the seat's Q8 / N6)", all(adapters_ok), adapters_ok)
    import json
    import tempfile
    from unittest import mock

    bid = m_resume.backend_identifier(testing.F3Adapter().provenance())
    art = {"unit": "Q-F3", "criterion": guard.GID_CRITERION, "verdict": "PASS", "n_pairs": 2,
           "pairs_identical": [True, True], "identity": {"backend_identifier": bid, "reasoning_cap": 60}}
    with tempfile.TemporaryDirectory() as td:
        with mock.patch.object(guard, "GATES_DIR", Path(td)):
            guard.gid_artifact_path().write_text(json.dumps(art))
            path_cached = guard.cached_path_admitted("qual", backend_identifier=bid, reasoning_cap=60)
            rec_c, calls_c = testing.run_case(testing.CASES[0], path_cached=path_cached)
    try:
        testing.run_case(testing.CASES[0], path_cached=path_cached)      # the licence is gone
        unlicensed = False
    except SystemExit as e:
        unlicensed = "CACHED PATH NOT LICENSED" in str(e)
    rec_u = testing.suite()[0][1]
    chk("mf3.runner: a licensed cached path passes cached=True through on every call, reasoning lines included "
        "(m:267); the bytes are the uncached run's on the stub; without the G-ID-F3 PASS on disk the cached "
        "session is refused at the runner",
        path_cached is True and all(k["cached"] is True for k in calls_c) and rec_c["path"] == "cached"
        and rec_c["transcript"] == rec_u["transcript"] and unlicensed)
