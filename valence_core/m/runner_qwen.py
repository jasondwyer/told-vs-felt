"""PROPOSAL-m F0m session loop, Qwen (v1.11 §2.1-§2.2 m:159, m:173; §2.6 m:261, m:263;
§2.7 m:267; §3 m:271; §5 m:308; §0.4 m:48).

ONE SESSION. ``transcript = banner`` (§2.5's bytes). Forced rounds ri = 0..3 from the
scaffold (e2a's alternating order, start from the committed schedule); each round is
generated as ``adapter.generate(transcript, seg, injections=(), seed, TEMP 0.7,
STOP_CAP 60, ban_ids, cached=path_cached)`` after rule 28(d)(a)'s boundary assertion
(``scaffold.assert_boundary``: a re-encode, cheap), classified by the audit wrapper
(v2 -> echo -> v4 content -> own-pair lexical, m:261), recorded, and appended as
``seg + text + "\\n"``. Free choices ci = 0..5: the menu from the scaffold, the
insulated vanilla read ``guard.insulated_read`` on ``transcript + menu`` (statepresent
asserted absent before every read, KL exactly 0.0), the pick written into the
transcript as ``menu + " {pick}\\n"`` (f1's layout, f_sessions.py:358), then the chosen
round on that prefix.

SESSION END (f1's rule, lenient scope; m:261, m:271, m:308). A forced round ends the
session on ANY claim (v2, echo, content, lexical): excluded at forced, no read, out
of the domain. A free round ends it only on a lexical claim, after that round is
recorded (excluded at free; the domain is kept -- nothing after the first pick
removes a session). A free v2, echo or content claim is post_choice_degeneracy and
ends nothing (f1's ``post_degen``, f_sessions.py:368-372). The strict scope is
recorded beside (``strict_exclusion``).

HAIR TRIGGER. ``scaffold_absorption``: any e2a ban-list string in a generation
(audit.QwenTaskRoundAudit's ``scaffold`` hits; the set IS v2's ban strings, so a hit
is also a v2 claim). The round is recorded, the trigger is recorded, and the runner
returns at once -- the stage stops (m:271). ``schedule_mismatch`` and
``template_breakage`` are guarded by the stage driver, not here (m:159, m:253, m:284):
before any session ``stages.load_committed`` refuses a schedule directory whose files
differ from their regeneration or from the manifest's sha256, and
``stages.startup_problems`` checks the banner bytes against §2.5's literals parsed
from the proposal; after each session G-VER (``verify.verify_and_mark``) rebuilds the
cell, keys, banner, seeds, items, menu orders and harness bytes from the record and
the committed cell, before the record is written. (The driver's pre-session
``verify.schedule_check`` compares a scaffold built from that same cell -- a
consistency assertion, not the schedule_mismatch guard; finding 32.)

THE PATH. ``cached`` is ALWAYS the keyword-only ``path_cached`` passed in, which the
stage driver takes from ``guard.cached_path_admitted`` (or ``run_gid_pair`` from
``guard.gid_paths``); ``guard.check_call_sites`` proves it statically. The scaffold
records the path and the two must agree.

Nothing here prints. The record is pick-bearing; printing goes only through
``readrule.session_line`` / ``readrule.printed_reason`` (build design §0 rule 5).
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from ..e2d import config as _e2d_config
from ..e2d.runner import LOW_LABEL_MASS
from ..session import build_ban_list
from ..session_e2a import STOP_CAP
from . import audit as _audit
from . import guard
from . import resume as _resume
from . import scaffold as _sc

E2A_BAN_LIST_PATH = Path(_audit.E2A_BAN_LIST_PATH)
TEMP = _e2d_config.TEMP                 # 0.7 (e2d/config.py:41), m:159
CHOICE_WINDOW = 8192                    # m:159, rule 28(d): the read window, no encode limit


def qwen_ban_list(adapter, path: str | os.PathLike = E2A_BAN_LIST_PATH) -> tuple[list[int], list[str]]:
    """The generation ban list = the e2a ban-list file, asserted (m:261; maps/e2a.md F6):
    loaded with ``path=``, REBUILT from the live adapter, and the two asserted equal."""
    p = Path(path)
    # build_ban_list WRITES a rebuilt list to a path that does not exist; the frozen file
    # must be there, so its absence is a STOP, never a rebuild.
    if not p.is_file():
        raise SystemExit(f"BAN LIST MISSING: {p} (the frozen e2a ban list) -- refusing to rebuild it")
    ids, strings = build_ban_list(adapter, path=str(p))
    _audit.assert_qwen_scaffold(ids, strings)
    # PIN (Code, declared at LOCK v0.1): maps/e2a.md F6's form -- the live tokenizer is
    # consulted: build_ban_list(adapter) with no path computes the list from the adapter's
    # own encode and special tokens and writes nothing (session.py:111-126); its ids and
    # strings must equal the frozen file's, else generation would ban ids the file does not
    # name (finding 6). A no-op on the real tokenizer (maps/e2a.md [tok]).
    live_ids, live_strings = build_ban_list(adapter)
    if sorted(int(i) for i in live_ids) != sorted(int(i) for i in ids) \
            or sorted(str(x) for x in live_strings) != sorted(str(x) for x in strings):
        raise SystemExit("BAN LIST MISMATCH: the live adapter's rebuilt scaffold ban list differs "
                         f"from the frozen e2a file {p} (ids or strings) -- refusing to generate")
    return [int(i) for i in ids], [str(x) for x in strings]


def assert_qwen_adapter(adapter) -> None:
    """Rule 28(d) on the Qwen adapter: the 8192 read window, no encode limit anywhere."""
    # PIN (Code, declared at LOCK v0.1): legacy_truncate and max_length are checked where
    # the adapter carries them (QwenMLXAdapter does, qwen_mlx.py:78-85; the stub does not).
    if getattr(adapter, "choice_window", None) != CHOICE_WINDOW:
        raise SystemExit(f"READ WINDOW: adapter declares {getattr(adapter, 'choice_window', None)!r}, "
                         f"m reads at {CHOICE_WINDOW} (rule 28(d))")
    if getattr(adapter, "legacy_truncate", False) is not False or getattr(adapter, "max_length", None) is not None:
        raise SystemExit("ENCODE LIMIT: the Qwen adapter carries an encode limit; m generates "
                         "with none (rule 28(d)(b))")


@dataclass(frozen=True)
class QwenSetup:
    audit: _audit.QwenTaskRoundAudit
    ban_ids: tuple[int, ...]
    ban_strings: tuple[str, ...]
    term_rx: tuple[str, ...]
    audit_cfg: dict


def qwen_startup(adapter, *, pool: Sequence[dict] | None = None) -> QwenSetup:
    """Once per process: insulation, window, ban list, audit of record, termination patterns."""
    guard.assert_insulated()
    assert_qwen_adapter(adapter)
    audit3, cfg = _audit.qwen_audit_of_record()
    ids, strings = qwen_ban_list(adapter)
    if pool is None:
        pool, _ = _sc.pool_and_renders()
    wrapper = _audit.QwenTaskRoundAudit(audit3, pool, strings)
    return QwenSetup(audit=wrapper, ban_ids=tuple(ids), ban_strings=tuple(strings),
                     term_rx=_sc.load_term_rx(), audit_cfg=cfg)


def run_session_qwen(adapter, scaffold: _sc.SessionScaffold, audit: _audit.QwenTaskRoundAudit,
                     ban_ids: Sequence[int], *, path_cached: bool, temp: float = TEMP,
                     term_rx: Sequence[str]) -> dict:
    """One F0m session; returns its m-session-v1 record (verified False until G-VER)."""
    guard.assert_insulated()
    sc = scaffold
    if type(path_cached) is not bool:
        raise TypeError("path_cached must be a bool (from guard.cached_path_admitted / gid_paths)")
    if sc.substrate != "qwen":
        raise ValueError("run_session_qwen runs Qwen (Q-F0) scaffolds only")
    if sc.path != ("cached" if path_cached else "uncached"):
        raise ValueError(f"path_cached={path_cached} disagrees with the scaffold's path {sc.path!r}")
    if not isinstance(audit, _audit.QwenTaskRoundAudit):
        raise TypeError("audit must be audit.QwenTaskRoundAudit")
    # PIN (Code, declared at LOCK v0.1): defence in depth beside the static call-site
    # check -- a cached session outside G-ID re-reads the licence itself (m:267), on THIS
    # adapter's backend (rule 2: the licence is per backend); G-ID runs both paths by its
    # own licence (guard.gid_paths).
    if path_cached and sc.stage != "id" and not guard.cached_path_admitted(
            sc.unit, sc.stage, backend_identifier=_resume.backend_identifier(adapter.provenance())):
        raise SystemExit(f"CACHED PATH NOT LICENSED: {sc.unit} {sc.stage} has no G-ID PASS on "
                         f"disk for this backend; the session runs uncached or not at all (m:267)")
    own = (sc.P, sc.Q)
    lids = guard.label_ids(adapter, own)
    echo_lines = _audit.qwen_echo_lines(sc.note_lines)
    log = _sc.SessionLog(sc, "qwen")
    earlier: list[str] = []
    t0 = time.perf_counter()
    stopped = False

    for ri in range(sc.n_forced):
        spec = sc.forced(ri)
        prefix = log.transcript
        _sc.assert_boundary(adapter, prefix, spec.seg)
        g = adapter.generate(prefix, spec.seg, injections=(), seed=spec.seed, temp=temp,
                             max_tokens=STOP_CAP, ban_ids=ban_ids, cached=path_cached)
        ra = audit.classify(g.text, render=spec.task_text, item=spec.item, earlier=earlier,
                            own_pair=own, echo_lines=echo_lines, phase="forced")
        log.add_round(spec, g, ra, term_rx)
        log.tb.add("round", "forced", ri, spec.seg)
        log.tb.add("generation", "forced", ri, g.text)
        log.tb.add("joiner", "forced", ri, "\n")
        earlier.append(g.text)
        if _audit.qwen_ends(ra):
            log.exclude(ra, "forced")
        if ra.scaffold:
            log.hair_trigger(ra, "forced")
            stopped = True
            break
        if log.exclusion is not None:
            break

    if not stopped and log.exclusion is None:
        for ci in range(sc.n_free):
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
            _sc.assert_boundary(adapter, prefix, spec.seg)
            g = adapter.generate(prefix, spec.seg, injections=(), seed=spec.seed, temp=temp,
                                 max_tokens=STOP_CAP, ban_ids=ban_ids, cached=path_cached)
            ra = audit.classify(g.text, render=spec.task_text, item=spec.item, earlier=earlier,
                                own_pair=own, echo_lines=echo_lines, phase="free")
            log.add_round(spec, g, ra, term_rx)
            log.tb.add("round", "free", ci, spec.seg)
            log.tb.add("generation", "free", ci, g.text)
            log.tb.add("joiner", "free", ci, "\n")
            earlier.append(g.text)
            if _audit.qwen_ends(ra):            # free: lexical only
                log.exclude(ra, "free")
            if ra.scaffold:
                log.hair_trigger(ra, "free")
                break
            if log.exclusion is not None:
                break
    # PIN (Code, declared at LOCK v0.1): seconds = perf_counter wall-clock of the whole
    # session (generations and reads), rounded to the millisecond; it is the hour cap's
    # increment (resume.hour_cap_exceeded) and is never printed.
    return log.record(round(time.perf_counter() - t0, 3))


# --- self-test -------------------------------------------------------------------
def _selftest(chk) -> None:
    import contextlib
    import copy
    import hashlib
    import io
    import json
    import re
    import tempfile
    import zlib
    from unittest import mock

    import numpy as np

    from . import bars, readrule, resume, testing, verify

    pool, renders = _sc.pool_and_renders()
    suite = testing.suite("qwen")
    kit = testing.qwen_kit()
    chk("runner_qwen: startup -- ban list is the e2a file (12 strings, ids), audit v2 sha16 pinned",
        len(kit.ban_strings) == 12 and len(kit.ban_ids) == 12
        and kit.audit_cfg["sha16_recomputed"] == _audit.AUDIT_V2_SHA16 and len(kit.term_rx) == 4)
    with tempfile.TemporaryDirectory() as td:
        missing = Path(td) / "e2a_ban_list.json"
        try:
            qwen_ban_list(testing.ScriptedAdapter(), path=missing)
            ok = False
        except SystemExit:
            ok = not missing.exists()
    chk("runner_qwen: a missing ban-list file is a STOP, never a rebuild (nothing written)", ok)
    live_ok = qwen_ban_list(testing.ScriptedAdapter()) == (list(kit.ban_ids), list(kit.ban_strings))
    moved = dict(testing.QWEN_BAN_MAP)
    moved["<think>"] = 7                      # one string mapped elsewhere by the live tokenizer
    extra = sorted(testing.QWEN_BAN_MAP) + ["<|stub_end|>"]
    fired = []
    for nm, ad in (("one id moved", testing.ScriptedAdapter(ban_map=moved)),
                   ("an extra special string", testing.ScriptedAdapter(special_strings=extra)),
                   ("the plain stub tokenizer", testing.ScriptedAdapter(ban_map=None))):
        try:
            qwen_ban_list(ad)
            fired.append((nm, False))
        except SystemExit as e:
            fired.append((nm, "BAN LIST MISMATCH" in str(e)))
    frozen = hashlib.sha256(E2A_BAN_LIST_PATH.read_bytes()).hexdigest() == _audit.E2A_BAN_LIST_SHA256
    chk("runner_qwen: the ban list is rebuilt from the live adapter and must equal the frozen file -- "
        "passes on a tokenizer that reproduces it; STOPs when one string maps elsewhere, an extra "
        "special string appears, or the tokenizer is another; the frozen file is never rewritten "
        "(finding 6)", live_ok and all(ok for _, ok in fired) and frozen, fired)
    chk("runner_qwen: TEMP is m:159/m:172's literal 0.7 and e2d.config.TEMP (the runner's default)",
        TEMP == 0.7 and TEMP == _e2d_config.TEMP
        and run_session_qwen.__kwdefaults__["temp"] == 0.7, (TEMP, _e2d_config.TEMP))
    bad_window = testing.ScriptedAdapter()
    bad_window.choice_window = 512
    try:
        qwen_startup(bad_window, pool=pool)
        ok = False
    except SystemExit:
        ok = True
    chk("runner_qwen: startup refuses a read window other than 8192", ok)

    # every scripted case reaches its declared outcome
    wrong = [(c.name, testing.outcome(r)) for c, r, _, _ in suite if testing.outcome(r) != c.want]
    chk(f"runner_qwen: {len(suite)} scripted sessions reach their declared outcomes (clean x8; forced "
        "v2/echo/content/lexical end; free v2/echo/content continue; free lexical ends; scaffold stops)",
        not wrong, wrong[:2])
    picks_ok = all([ch["pick"] for ch in r["choices"]] == list(p)[:len(r["choices"])]
                   for _, r, _, p in suite)
    chk("runner_qwen: picks follow the scripted plan through the real read path (KL exactly 0.0)",
        picks_ok and all(ch["read"]["verify_kl"] == 0.0 for _, r, _, _ in suite for ch in r["choices"]))
    clean = [r for c, r, _, _ in suite if c.name.startswith("qwen clean")]
    chk("runner_qwen: clean sessions -- 6 reads, valid, complete, domain, first pick coded on P",
        len(clean) == 8 and all(len(r["choices"]) == 6 and not r["excluded"] and r["complete"]
                                and r["first_free_pick_P"] is (r["choices"][0]["pick"] == r["cell"]["P"])
                                for r in clean)
        and {(r["template"], r["cell"]["start"], r["cell"]["clause"]) for r in clean}
        == {(t, st, cl) for t in ("A0", "A0s") for st in (0, 1) for cl in (0, 1)})
    by = {c.name: r for c, r, _, _ in suite}
    fv2 = by["qwen forced v2 ends (no read)"]
    chk("runner_qwen: a forced v2 claim ends the session -- no read, domain False, first pick None",
        fv2["exclusion"]["class"] == "v2" and not fv2["choices"] and fv2["domain"] is False
        and fv2["first_free_pick_P"] is None and fv2["strict_exclusion"] == {"class": "v2", "phase": "forced"})
    free_deg = by["qwen free v2/echo(TOLD)/content claims end nothing (contrast)"]
    claims = [r["audit"]["claim"] for r in free_deg["rounds"] if r["phase"] == "free"]
    chk("runner_qwen: free v2, TOLD-line echo and content claims are post-choice degeneracy (no end); "
        "strict scope records the first",
        claims[:3] == ["v2", "echo", "content"] and not free_deg["excluded"] and free_deg["complete"]
        and free_deg["strict_exclusion"] == {"class": "v2", "phase": "free"}, claims)
    hair_f = by["qwen free scaffold string: hair trigger stops, no exclusion"]
    hair_p = by["qwen forced scaffold string: v2 exclusion + hair trigger, stop"]
    chk("runner_qwen: scaffold_absorption records the trigger and returns at once (free: no "
        "exclusion, domain kept; forced: v2 exclusion too)",
        hair_f["hair_triggers"] == [{"name": "scaffold_absorption", "phase": "free", "detail": "<|im_end|>"}]
        and not hair_f["excluded"] and hair_f["domain"] and len(hair_f["rounds"]) == 6
        and hair_p["hair_triggers"][0]["phase"] == "forced" and hair_p["exclusion"]["class"] == "v2")

    # finding 5 / N6: on Qwen a Note line copied without its final period is NOT an echo
    # (m:261's "complete" line; the stem form is OLMo's only); m:261's later classes claim it
    np_told = by["qwen forced TOLD line without its final period: lexical (not echo) ends"]
    np_common = by["qwen forced COMMON without its final period: no class, the session runs on"]
    np_free = by["qwen free COMMON without its final period: no class; free TOLD without it: lexical ends"]

    def stem_of_banner_line(rec, x):
        return not x["text"].endswith(".") and x["text"] + "." in rec["note_lines"]

    free_claims = [(x["audit"]["claim"], x["audit"]["echo_line"]) for x in np_free["rounds"]
                   if x["phase"] == "free"]
    chk("runner_qwen: on Qwen a Note line copied without its final period is not an echo (finding N6): "
        "TOLD at forced -> lexical@forced ends the session (no read, out of the domain); COMMON at "
        "forced -> no claim, the session runs on (6 reads, valid, in the domain); at free, COMMON -> no "
        "claim, TOLD -> lexical@free ends after its round (domain kept)",
        np_told["exclusion"] == {"class": "lexical", "phase": "forced",
                                 "detail": np_told["rounds"][-1]["audit"]["detail"]}
        and np_told["rounds"][-1]["audit"]["echo_line"] is None and not np_told["choices"]
        and np_told["domain"] is False and stem_of_banner_line(np_told, np_told["rounds"][-1])
        and np_common["rounds"][0]["audit"]["claim"] is None
        and np_common["rounds"][0]["audit"]["echo_line"] is None
        and stem_of_banner_line(np_common, np_common["rounds"][0])
        and not np_common["excluded"] and np_common["domain"] is True and len(np_common["choices"]) == 6
        and np_common["strict_exclusion"] is None
        and free_claims == [(None, None), (None, None), ("lexical", None)]
        and all(stem_of_banner_line(np_free, np_free["rounds"][i]) for i in (4, 6))
        and np_free["exclusion"]["class"] == "lexical" and np_free["exclusion"]["phase"] == "free"
        and np_free["domain"] is True,
        (np_told["exclusion"], np_common["rounds"][0]["audit"]["claim"], free_claims))

    # finding 33: the runner feeds FORCED responses into audit v3's `earlier`
    rep_f = by["qwen forced round 3 repeats round 1: content (stuck_attractor) ends"]
    rep_c = by["qwen free round repeats a forced answer: content claim, no end"]
    chk("runner_qwen: a forced round repeating an earlier forced answer -> content@forced "
        "(stuck_attractor), session ended; a free round repeating a forced answer -> free content "
        "claim, no end (audit v3's `earlier` carries the forced responses)",
        rep_f["exclusion"] == {"class": "content", "phase": "forced", "detail": "content:stuck_attractor"}
        and len(rep_f["rounds"]) == 3 and not rep_f["choices"]
        and [(x["phase"], x["audit"]["detail"]) for x in rep_c["rounds"] if x["audit"]["claim"]]
        == [("free", "content:stuck_attractor")] and not rep_c["excluded"] and rep_c["complete"],
        (rep_f["exclusion"], [x["audit"]["claim"] for x in rep_c["rounds"]]))
    # finding N16: ... and FREE responses too -- the repeated answer is in no forced round
    rep_ff = by["qwen free round repeats an earlier FREE answer: content claim, no end"]
    forced_txt = {x["text"] for x in rep_ff["rounds"] if x["phase"] == "forced"}
    rep_claims = [(x["phase"], x.get("ci"), x["audit"]["detail"]) for x in rep_ff["rounds"]
                  if x["audit"]["claim"]]
    chk("runner_qwen: a free round repeating an earlier FREE answer (in no forced round) -> free "
        "content claim (stuck_attractor), strict scope {content, free}, no end, complete (audit v3's "
        "`earlier` carries the free responses)",
        rep_claims == [("free", 2, "content:stuck_attractor")]
        and rep_ff["rounds"][6]["text"] == rep_ff["rounds"][4]["text"] not in forced_txt
        and rep_ff["strict_exclusion"] == {"class": "content", "phase": "free"}
        and rep_ff["exclusion"] is None and not rep_ff["excluded"] and rep_ff["complete"]
        and len(rep_ff["choices"]) == 6 and rep_ff["domain"] is True,
        (rep_claims, rep_ff["strict_exclusion"]))

    # finding 26: the choice read's context is transcript + menu at the choice position,
    # and prefix_tokens_at_read is that context's encoded length (the DV's forward)
    ctx_bad = []
    n_reads = 0
    for c in testing.CASES_QWEN:
        a = testing.ScriptedAdapter()
        r, _, _ = testing.run_case(c, "qwen", adapter=a)
        menus = [p for p in r["pieces"] if p["kind"] == "menu"]
        want = [r["transcript"][:p["end"]] for p in menus]
        want_ctx = [r["transcript"][:p["start"]] + ch["menu"] for p, ch in zip(menus, r["choices"])]
        n_reads += len(want)
        if a.read_texts != want or want != want_ctx:
            ctx_bad.append((c.name, "context"))
        if [ch["prefix_tokens_at_read"] for ch in r["choices"]] != [len(a.encode(t)) for t in want]:
            ctx_bad.append((c.name, "prefix tokens"))
    chk(f"runner_qwen: every read's context ({n_reads} reads over {len(testing.CASES_QWEN)} sessions) "
        "= the transcript up to its menu's end (transcript + menu) and prefix_tokens_at_read = that "
        "context's encoded length", not ctx_bad and n_reads > 50, ctx_bad[:3])

    # arm-rng draw order and item streams, recomputed independently from the key strings
    draws_ok = items_ok = props_ok = True
    for c, r, _, _ in suite:
        tpl = r["template"]
        if r["keys"] != {"arm": f"m-f0m|{tpl}|{r['s']}", "items": f"m-items-qual|{r['s']}"}:
            draws_ok = False
            continue
        rng = np.random.default_rng(zlib.crc32(r["keys"]["arm"].encode()) % 2**31)
        forced = [x for x in r["rounds"] if x["phase"] == "forced"]
        free = [x for x in r["rounds"] if x["phase"] == "free"]
        draws_ok &= [x["seed"] for x in forced] == [int(rng.integers(2**31)) for _ in forced]
        for ch, x in zip(r["choices"], free):
            o = int(rng.integers(2))
            draws_ok &= (ch["menu_a"], ch["menu_b"]) == ((r["cell"]["P"], r["cell"]["Q"]) if o == 0
                                                          else (r["cell"]["Q"], r["cell"]["P"]))
            draws_ok &= x["seed"] == int(rng.integers(2**31))
        perm = np.random.default_rng(zlib.crc32(r["keys"]["items"].encode()) % 2**31).permutation(16)
        streams = {"P": list(perm[:8]), "Q": list(perm[8:])}
        for x in r["rounds"]:
            items_ok &= x["item"] == int(streams[x["role"]].pop(0))
            want = ((renders[x["item"]], "corrupted") if (r["contrast"] and x["role"] == "Q")
                    else (pool[x["item"]]["task"], "clean"))
            props_ok &= (x["task_text"], x["property"]) == want
    chk("runner_qwen: seeds and menu orders = an independent recomputation from the arm key "
        "(4 seeds, then per choice menu order then seed)", draws_ok)
    chk("runner_qwen: items = the item key's permutation split [:8] P / [8:] Q, consumed in order",
        items_ok)
    chk("runner_qwen: contrast Q rounds deliver the corrupt_m render ('corrupted'); sham and P clean",
        props_ok)

    # what the adapter saw
    calls_ok = True
    for c, r, calls, _ in suite:
        calls_ok &= len(calls) == len(r["rounds"])
        calls_ok &= all(k["injections"] == () and k["cached"] is False and k["temp"] == TEMP
                        and k["max_tokens"] == STOP_CAP and k["ban_ids"] == kit.ban_ids for k in calls)
        t = r["transcript"]
        for x, k in zip(r["rounds"], calls):
            gi = next(i for i, p in enumerate(r["pieces"]) if p["kind"] == "round"
                      and p["phase"] == x["phase"] and p["idx"] == x.get("ri", x.get("ci")))
            p = r["pieces"][gi]
            calls_ok &= k["prefix"] == t[:p["start"]] and k["segment"] == t[p["start"]:p["end"]]
            calls_ok &= k["seed"] == x["seed"]
    chk("runner_qwen: the adapter saw injections=() and cached=False on every call, the recorded "
        "seed, and prefix = transcript so far (free: + menu + pick line)", calls_ok)
    case = testing.CASES_QWEN[1]
    bid = resume.backend_identifier(testing.ScriptedAdapter().provenance())      # C2's value
    other_bid = "0123456789abcdef" if bid != "0123456789abcdef" else "fedcba9876543210"
    art = {"unit": "Q-F0", "criterion": guard.GID_CRITERION, "verdict": "PASS", "n_pairs": 2,
           "pairs_identical": [True, True], "identity": {"backend_identifier": bid}}
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "Q-F0_G-ID.json").write_text(json.dumps(art))
        with mock.patch.object(guard, "GATES_DIR", Path(td)):
            path_cached = guard.cached_path_admitted("Q-F0", "qual", backend_identifier=bid)
            rec_c, calls_c, _ = testing.run_case(case, "qwen", path_cached=path_cached)
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "Q-F0_G-ID.json").write_text(
            json.dumps({**art, "identity": {"backend_identifier": other_bid}}))
        with mock.patch.object(guard, "GATES_DIR", Path(td)):
            try:
                testing.run_case(case, "qwen", path_cached=path_cached)  # PASS from another backend
                other_backend = False
            except SystemExit as e:
                other_backend = "CACHED PATH NOT LICENSED" in str(e)
    try:
        testing.run_case(case, "qwen", path_cached=path_cached)      # the licence is gone
        unlicensed = False
    except SystemExit:
        unlicensed = True
    rec_u = by[case.name]
    chk("runner_qwen: a licensed cached path passes cached=True through on every call (the guard's "
        "licence on this adapter's backend, not a literal); record path 'cached'; bytes as uncached "
        "on the stub",
        path_cached is True and all(k["cached"] is True for k in calls_c) and rec_c["path"] == "cached"
        and rec_c["transcript"] == rec_u["transcript"])
    chk("runner_qwen: a cached session is refused at the runner without a G-ID PASS on disk, and with "
        "a PASS produced on another backend (rule 2; C2: resume.backend_identifier(adapter.provenance()))",
        unlicensed and other_backend, (unlicensed, other_backend))
    sc_c = _sc.m_config("Q-F0", "qual", "A0", 0, testing.case_cell("qwen", "A0", 0), "cached")
    refused = []
    for fn, exc in ((lambda: run_session_qwen(testing.ScriptedAdapter(), sc_c, kit.audit, kit.ban_ids,
                                              path_cached=False, term_rx=kit.term_rx), ValueError),
                    (lambda: run_session_qwen(testing.ScriptedAdapter(), _sc.m_config(
                        "OLMo-sft", "qual", "A0-OLMo-sft", 0, testing.case_cell("olmo", "A0-OLMo-sft", 0),
                        "uncached"), kit.audit, kit.ban_ids, path_cached=False, term_rx=kit.term_rx),
                     ValueError)):
        try:
            fn()
            refused.append(False)
        except exc:
            refused.append(True)
    ma = testing.MergingAdapter()
    ma.load(["Seven."] * 10)
    sc_m = _sc.m_config("Q-F0", "qual", "A0", 0, testing.case_cell("qwen", "A0", 0), "uncached")
    try:
        run_session_qwen(ma, sc_m, kit.audit, kit.ban_ids, path_cached=False, term_rx=kit.term_rx)
        refused.append(False)
    except SystemExit:
        refused.append(not ma.calls)
    chk("runner_qwen: refuses a path disagreeing with the scaffold, an OLMo "
        "scaffold, and halts before generating on a collapsed token boundary", all(refused), refused)

    # records against Phase A's consumers
    recs = [r for _, r, _, _ in suite]
    sham = [r for r in recs if not r["contrast"]]
    con = [r for r in recs if r["contrast"]]
    try:
        stripped = [readrule.strip_contrast(r) for r in con]
        redacted = [readrule.redact_sham(r) for r in sham]
        report = readrule.stage_report(recs)
        lines = [readrule.session_line(r) for r in recs]
        ok = True
    except Exception as e:                       # noqa: BLE001
        ok, stripped, redacted, report, lines = False, [], [], {}, [repr(e)]
    chk("runner_qwen: every record passes strip_contrast / redact_sham / stage_report / session_line",
        ok and len(stripped) == len(con) and len(redacted) == len(sham), lines[:1])
    free_mark = all("free" not in json.dumps(x) for x in stripped)
    chk("runner_qwen: stripped contrast records carry no free-round material",
        free_mark and all(x["transcript"] == r["transcript"][:len(x["transcript"])] and "| choice]"
                          not in x["transcript"] for x, r in zip(stripped, con)))
    bq = {b.name: b for b in bars.QF0_BARS}["round_degeneracy@G-F0m-Qwen"]
    res = bars.stage_end_eval(recs, bq, bars.sham_domain)
    k_want = sum(x["audit"]["claim"] in ("v2", "echo") for r in sham for x in r["rounds"])
    n_want = sum(len(r["rounds"]) for r in sham)
    chk("runner_qwen: bars.stage_end_eval on the sham-only domain counts v2/echo rounds over sham rounds",
        (res.k, res.n) == (k_want, n_want) and res.fired is False and k_want >= 3, (res.k, res.n))
    with tempfile.TemporaryDirectory() as td:
        ident = resume.Identity(
            unit="Q-F0", stage="qual", template_set=["A0", "A0s"], lock_sha256="pre-lock",
            schedule_sha256="0" * 64, path="uncached", hour_cap=None, n={"A0": 8, "A0s": 16},
            audit_v2_sha16=_audit.AUDIT_V2_SHA16, ban_sha=_audit.E2A_BAN_LIST_SHA256,
            backend_identifier=resume.backend_identifier(testing.ScriptedAdapter().provenance()),
            proposal_sha256=hashlib.sha256(
                (_sc.REPO / "PROPOSAL-m-gating-campaign-v1_11.md").read_bytes()).hexdigest())
        cpath = Path(td) / "Q-F0_qual.json"
        ck = resume.load_or_init(cpath, ident, resume=False)
        gver = []
        for r in recs:
            r = copy.deepcopy(r)                 # the suite's records stay unmarked
            gver += verify.verify_and_mark(r, substrate="qwen", pool=pool, renders=renders,
                                           schedule_cell=testing.case_cell("qwen", r["template"], r["s"]))
            resume.record_session(ck, r)         # C7: only a G-VER-verified record is recorded
        resume.write_checkpoint(cpath, ck)
        back = resume.load_or_init(cpath, ident, resume=True)
    chk("runner_qwen: every record passes G-VER (verify_and_mark), goes into a gate-stage checkpoint "
        "(resume.record_session) and reloads skip-only",
        gver == [] and resume.done_ids(back) == {(r["template"], r["s"]) for r in recs}
        and len(back["sessions"]) == len(recs), gver[:2])

    # printing: the runner prints nothing; the printed line names no tag, pick or free index
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        testing.run_case(testing.CASES_QWEN[0], "qwen")
        testing.run_case(next(c for c in testing.CASES_QWEN
                              if c.name == "qwen free lexical ends after its round (contrast)"), "qwen")
    words = {w for r in recs for w in r["cell"]["pair"]}
    clean_lines = all(not any(w in ln.lower() for w in words)
                      and re.fullmatch(r"qual A0s? s=\d+ (valid|excluded:[a-z]+@(forced|free))", ln)
                      and not re.search(r"\d", ln.split(" ", 3)[3]) for ln in lines)
    lex_free = readrule.session_line(by["qwen free lexical ends after its round (contrast)"])
    chk("runner_qwen: the runner prints nothing; session lines carry no tag, pick or free-round "
        "index, and a contrast free exclusion prints 'excluded@free'",
        buf.getvalue() == "" and clean_lines and lex_free.endswith("excluded:excluded@free"),
        (buf.getvalue()[:80], lines[:2], lex_free))
