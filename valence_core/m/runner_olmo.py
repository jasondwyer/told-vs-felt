"""PROPOSAL-m F0m-OLMo session loop (v1.11 §0.7 m:54; §2.1 m:159; §2.6 m:262-263; §2.7
m:267; §3 m:271, m:302; §5 m:308; §0.4 m:48).

b3's apparatus as a new loop in the m package (box_b3_sessions.py:128-212, carried, not
imported): TEMP 0.7, STOP_CAP 60, F = 2, the six-string scaffold ban list, the
termination counter, ``choice_read(verify=True)`` -- through ``guard.insulated_read``,
statepresent asserted absent before EVERY read (b3 asserted it at startup only) --
and b3's CONTEXT RULE: the menu block and the harness-written ``" {pick}\\n"`` line are
part of the chosen round's generation PREFIX only and are never written to the stored
or later transcript (box_b3_sessions.py:189, :202); the pick stays named in the chosen
round's header. So the stored transcript is banner + Σ(seg + text + "\\n") and its
pieces carry no menu or pick kind; each choice records its menu text and order.

What m changes against b3: the item stream (``m-olmo-items...``, per-label split, the
CORR pool), the arm rng carrying seeds and menu orders only, start order from the
committed schedule, §2.5's banner lines, m's echo class between AuditSpec and lexical,
and no injection anywhere (m imports no injection type; ``injections=()`` always).

SESSION END (m:262, pinned): the first AuditSpec, echo or own-pair lexical claim in
ANY round ends the session (``audit.olmo_ends``); a free-round claim excludes the
session from whole-session validity but not from the domain (m:308).

HAIR TRIGGER: ``scaffold_absorption`` on b3's six ban strings, case-sensitive
(``<|endoftext|>`` and ``<|pad|>`` are scaffold-only; the other four also claim the
round as AuditSpec ``special:``). The round is recorded and the runner returns.

THE PATH: OLMo is uncached (m:267, Phase B's path). Every generate call here passes
the literal ``cached=False``; there is no path parameter to pass anything else.
Base is refused (decision (7'); ``keys`` refuses ``OLMo-base``, and
``assert_olmo_adapter`` refuses a loaded base checkpoint).
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from typing import Sequence

from ..e2d.runner import LOW_LABEL_MASS
from ..session import build_ban_list
from ..session_e2a import STOP_CAP
from . import audit as _audit
from . import guard, keys
from . import scaffold as _sc

OLMO_TEMP = 0.7          # box_b3_sessions.py:77 TEMP (selftest asserts equality with b3's)
OLMO_F = 2               # box_b3_sessions.py:76 F, forced rounds per pole
CHOICE_WINDOW = 8192     # olmo_hf.py:45; rule 28(d), b3's read, no truncation


def olmo_audit_sha16(spec=_audit.OLMO_AUDIT) -> str:
    """sha16 of OLMo's audit of record, for resume.Identity's ``audit_v2_sha16`` on OLMo."""
    # PIN (Code, declared at LOCK v0.1): OLMo has no v2 artifact; its identity's
    # audit_v2_sha16 is sha256 of the compact sort-keyed JSON of the AuditSpec's three
    # fields {ban_strings, frame_fragments, junk_regex} (lists, in the spec's order),
    # first 16 hex -- format_recon's body-hash form applied to b3's literal.
    body = {k: list(getattr(spec, k)) for k in ("ban_strings", "frame_fragments", "junk_regex")}
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]


def assert_olmo_adapter(adapter, ckpt: str) -> None:
    """Refuse base and a checkpoint other than the unit's; the declared 8192 window."""
    if ckpt not in keys.CKPTS:
        raise SystemExit(f"OLMo checkpoint {ckpt!r} is not an m unit (base refused, decision (7'))")
    # PIN (Code, declared at LOCK v0.1): where the adapter carries its weights path
    # (OLMoHFAdapter.path = /workspace/models/{ckpt}), its last component must be the
    # unit's checkpoint; the stub carries none and is not checked.
    path = getattr(adapter, "path", None)
    if path is not None:
        leaf = os.path.basename(str(path).rstrip("/"))
        if leaf == "base" or leaf != ckpt:
            raise SystemExit(f"OLMo adapter loaded {path!r}, the unit is OLMo-{ckpt}: refusing "
                             f"(base is never an m unit; no cross-checkpoint session)")
    if getattr(adapter, "choice_window", None) != CHOICE_WINDOW:
        raise SystemExit(f"READ WINDOW: adapter declares {getattr(adapter, 'choice_window', None)!r}, "
                         f"m reads at {CHOICE_WINDOW} (rule 28(d))")


def olmo_ban_list(adapter, ckpt: str) -> tuple[list[int], list[str]]:
    """b3's ban list (build_ban_list over the adapter, box_b3_sessions.py:261), asserted
    against data/olmo/scaffold_{ckpt}.json and b3's id sha16 (m:262)."""
    ids, strings = build_ban_list(adapter)
    _audit.assert_olmo_scaffold(ids, strings, ckpt)
    return [int(i) for i in ids], [str(x) for x in strings]


@dataclass(frozen=True)
class OLMoSetup:
    audit: _audit.OLMoTaskRoundAudit
    ban_ids: tuple[int, ...]
    ban_strings: tuple[str, ...]
    term_rx: tuple[str, ...]
    audit_sha16: str


def olmo_startup(adapter, ckpt: str) -> OLMoSetup:
    """Once per process (maps/olmo.md §5.1): insulation, base refusal, window, ban list."""
    guard.assert_insulated()
    assert_olmo_adapter(adapter, ckpt)
    ids, strings = olmo_ban_list(adapter, ckpt)
    return OLMoSetup(audit=_audit.OLMoTaskRoundAudit(), ban_ids=tuple(ids),
                     ban_strings=tuple(strings), term_rx=_sc.load_term_rx(),
                     audit_sha16=olmo_audit_sha16())


def run_session_olmo(adapter, scaffold: _sc.SessionScaffold, audit: _audit.OLMoTaskRoundAudit,
                     ban_ids: Sequence[int], *, temp: float = OLMO_TEMP,
                     term_rx: Sequence[str]) -> dict:
    """One F0m-OLMo session; returns its m-session-v1 record (verified False until G-VER)."""
    guard.assert_insulated()
    sc = scaffold
    if sc.substrate != "olmo" or sc.unit not in tuple(f"OLMo-{c}" for c in keys.CKPTS):
        raise ValueError("run_session_olmo runs OLMo-{sft,dpo,instruct} scaffolds only (base refused)")
    if sc.path != "uncached":
        raise ValueError("OLMo sessions are uncached (m:267)")
    if sc.n_forced != 2 * OLMO_F:
        raise ValueError(f"F0m-OLMo runs 2F = {2 * OLMO_F} forced rounds")
    if not isinstance(audit, _audit.OLMoTaskRoundAudit):
        raise TypeError("audit must be audit.OLMoTaskRoundAudit")
    own = (sc.P, sc.Q)
    lids = guard.label_ids(adapter, own)
    echo_lines = _audit.olmo_echo_lines(sc.note_lines)
    log = _sc.SessionLog(sc, "olmo")
    t0 = time.perf_counter()
    stopped = False

    # PIN (Code, declared at LOCK v0.1): rule 28(d)(a)'s boundary assertion runs on OLMo
    # too, on encode() with the adapter's own default (add_special_tokens=True, as
    # olmo_hf.generate encodes); with injections=() the boundary does not change what OLMo
    # forwards, so a fire there is a tokenizer fact to escalate [verify on box].
    for ri in range(sc.n_forced):
        spec = sc.forced(ri)
        prefix = log.transcript
        _sc.assert_boundary(adapter, prefix, spec.seg)
        g = adapter.generate(prefix, spec.seg, injections=(), seed=spec.seed, temp=temp,
                             max_tokens=STOP_CAP, ban_ids=ban_ids, cached=False)
        ra = audit.classify(g.text, own_pair=own, echo_lines=echo_lines, phase="forced")
        log.add_round(spec, g, ra, term_rx)
        log.tb.add("round", "forced", ri, spec.seg)
        log.tb.add("generation", "forced", ri, g.text)
        log.tb.add("joiner", "forced", ri, "\n")
        if _audit.olmo_ends(ra):
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
            spec = sc.chosen(ci, pick)
            log.add_choice(menu, cr, pick, spec.role, n_prefix, LOW_LABEL_MASS)
            gen_prefix = read_prefix + f" {pick}\n"           # b3's context rule: prefix only
            _sc.assert_boundary(adapter, gen_prefix, spec.seg)
            g = adapter.generate(gen_prefix, spec.seg, injections=(), seed=spec.seed, temp=temp,
                                 max_tokens=STOP_CAP, ban_ids=ban_ids, cached=False)
            ra = audit.classify(g.text, own_pair=own, echo_lines=echo_lines, phase="free")
            log.add_round(spec, g, ra, term_rx)
            log.tb.add("round", "free", ci, spec.seg)          # stored: chosen + text + "\n"
            log.tb.add("generation", "free", ci, g.text)
            log.tb.add("joiner", "free", ci, "\n")
            if _audit.olmo_ends(ra):
                log.exclude(ra, "free")
            if ra.scaffold:
                log.hair_trigger(ra, "free")
                break
            if log.exclusion is not None:
                break
    return log.record(round(time.perf_counter() - t0, 3))   # seconds: runner_qwen's PIN


# --- self-test -------------------------------------------------------------------
def _selftest(chk) -> None:
    import contextlib
    import copy
    import dataclasses
    import io
    import re
    import tempfile
    import zlib
    from pathlib import Path

    import numpy as np

    from . import bars, readrule, resume, schedule, testing, verify

    pool, renders = _sc.pool_and_renders()
    b3 = _audit._load_b3()
    chk("runner_olmo: TEMP 0.7 and F = 2 equal b3's constants; FORBIDDEN_MODULES equal b3's",
        OLMO_TEMP == b3.TEMP and OLMO_F == b3.F and tuple(b3.FORBIDDEN_MODULES) == guard.FORBIDDEN_MODULES)
    sha = olmo_audit_sha16()
    other = dataclasses.replace(_audit.OLMO_AUDIT, frame_fragments=_audit.OLMO_AUDIT.frame_fragments + ("Options:",))
    chk("runner_olmo: olmo_audit_sha16 is a stable 16-hex body hash of b3's AuditSpec, moved by any change",
        re.fullmatch(r"[0-9a-f]{16}", sha) is not None and sha == olmo_audit_sha16(b3.AUDIT)
        and olmo_audit_sha16(other) != sha, sha)
    refused = []
    for ck, path in (("base", None), ("sft", "/workspace/models/base"), ("sft", "/workspace/models/dpo/")):
        a = testing.OLMoScriptedAdapter()
        if path is not None:
            a.path = path
        try:
            assert_olmo_adapter(a, ck)
            refused.append(False)
        except SystemExit:
            refused.append(True)
    good = testing.OLMoScriptedAdapter()
    good.path = "/workspace/models/sft/"
    assert_olmo_adapter(good, "sft")
    try:
        keys.templates("OLMo-base")
        refused.append(False)
    except ValueError:
        refused.append(True)
    chk("runner_olmo: base refused (unit and loaded weights), a foreign checkpoint refused; the "
        "unit's own checkpoint accepted", all(refused), refused)
    try:
        olmo_startup(testing.OLMoScriptedAdapter(), "sft")
        ok = False
    except SystemExit:
        ok = True
    chk("runner_olmo: startup asserts the scaffold set -- the stub's six ids fail b3's nine-id sha16",
        ok)

    suite = testing.suite("olmo")
    wrong = [(c.name, testing.outcome(r)) for c, r, _, _ in suite if testing.outcome(r) != c.want]
    chk(f"runner_olmo: {len(suite)} scripted sessions reach their declared outcomes (clean x8; forced "
        "AuditSpec/echo/lexical end; '* * *' continues; free echo/AuditSpec/lexical end; scaffold stops)",
        not wrong, wrong[:2])
    by = {c.name: r for c, r, _, _ in suite}
    clean = [r for c, r, _, _ in suite if c.name.startswith("olmo clean")]
    chk("runner_olmo: clean sessions -- 6 reads, valid, complete, over contrast/sham x both start "
        "orders x both clauses",
        len(clean) == 8 and all(len(r["choices"]) == 6 and not r["excluded"] and r["complete"]
                                and r["domain"] for r in clean)
        and {(r["template"], r["cell"]["start"], r["cell"]["clause"]) for r in clean}
        == {(t, st, cl) for t in ("A0-OLMo-sft", "A0s-OLMo-sft") for st in (0, 1) for cl in (0, 1)})
    fe = by["olmo free echo ends"]
    chk("runner_olmo: a free echo ends the session at that round (domain kept, first pick kept)",
        fe["exclusion"]["class"] == "echo" and fe["exclusion"]["phase"] == "free" and fe["domain"]
        and isinstance(fe["first_free_pick_P"], bool) and len(fe["choices"]) == 3)
    pad = by["olmo forced <|pad|>: hair trigger, no claim, stop"]
    think = by["olmo free <think>: AuditSpec claim + hair trigger, stop"]
    chk("runner_olmo: <|pad|> fires scaffold_absorption without a claim; <think> claims AuditSpec too",
        pad["hair_triggers"] == [{"name": "scaffold_absorption", "phase": "forced", "detail": "<|pad|>"}]
        and not pad["excluded"] and pad["domain"] is False
        and think["exclusion"]["class"] == "audit" and think["hair_triggers"][0]["phase"] == "free")
    picks_ok = all([ch["pick"] for ch in r["choices"]] == list(p)[:len(r["choices"])]
                   for _, r, _, p in suite)
    chk("runner_olmo: picks follow the scripted plan through the real read path (KL exactly 0.0)",
        picks_ok and all(ch["read"]["verify_kl"] == 0.0 for _, r, _, _ in suite for ch in r["choices"]))

    # finding 5: OLMo's newline stop stores a copied Note line without its final period;
    # the echo class still claims it, the session ends, and the round counts toward
    # round_degeneracy (and, on a G-TIME-OLMo sham session, the pause)
    npf = by["olmo forced echo of the TOLD line without its final period ends"]
    np_all = [by[n] for n in ("olmo forced echo of the TOLD line without its final period ends",
                              "olmo forced echo of COMMON without its final period ends",
                              "olmo free echo of the TOLD line without its final period ends",
                              "olmo free echo of COMMON without its final period ends")]
    deg_rounds = [x for x in npf["rounds"] if x["audit"]["claim"] in bars.DEGEN_CLAIMS["olmo"]]
    bo1 = {b.name: b for b in bars.OLMO_BARS("sft")}["round_degeneracy@G-F0m-OLMo-sft"]
    one = bars.stage_end_eval([npf], bo1, bars.sham_domain)
    chk("runner_olmo: a period-less TOLD copy on a forced round -> echo@forced, excluded, session "
        "ended (no read, out of the domain), counted in round_degeneracy's numerator; COMMON and the "
        "free-round copies end the session as echo too",
        npf["exclusion"]["class"] == "echo" and npf["exclusion"]["phase"] == "forced"
        and npf["excluded"] and not npf["choices"] and npf["domain"] is False
        and not npf["rounds"][-1]["text"].endswith(".") and len(deg_rounds) == 1
        and (one.k, one.n) == (1, 3)
        and [(r["exclusion"]["class"], r["exclusion"]["phase"]) for r in np_all]
        == [("echo", "forced"), ("echo", "forced"), ("echo", "free"), ("echo", "free")],
        (npf["exclusion"], one.k, one.n))
    tcell = schedule.gate_schedule("OLMo-sft", "time", "A0s-OLMo-sft",
                                   schedule.roster_for("OLMo-sft"), 1)[0]
    tkit = testing.olmo_kit()
    pz = {b.name: b for b in bars.OLMO_BARS("sft")}["gtime_pause@G-TIME-OLMo-sft"]
    paused = {}
    for nm, texts in (("period-less TOLD at forced 3", ("Seven.", "March.", "{TOLD_np}")),
                      ("clean", ("Seven.", "March.", "Twelve.", "Three.", "Two.", "Down.", "Iron.",
                                 "Cold.", "Forty-five.", "January."))):
        sct = _sc.m_config("OLMo-sft", "time", "A0s-OLMo-sft", 0, tcell, "uncached")
        ta = testing.OLMoScriptedAdapter()
        ta.load(testing.script_for(testing.Case(nm, False, 0, texts), sct.P, sct.Q, sct.note_lines),
                [sct.P, sct.Q, sct.P, sct.Q, sct.P, sct.Q])
        trec = run_session_olmo(ta, sct, tkit["audit"], tkit["ban_ids"], term_rx=tkit["term_rx"])
        paused[nm] = bars.stage_end_eval([trec], pz, bars.sham_domain).fired
    chk("runner_olmo: the G-TIME-OLMo pause fires on a sham session whose round 3 copies its TOLD line "
        "without the final period, and stays silent on a clean one",
        paused == {"period-less TOLD at forced 3": True, "clean": False}, paused)

    # finding 26: the choice read's context is the stored transcript + the menu (b3's
    # context rule) and prefix_tokens_at_read is that context's encoded length
    ctx_bad = []
    n_reads = 0
    for c in testing.CASES_OLMO:
        a = testing.OLMoScriptedAdapter()
        r, _, _ = testing.run_case(c, "olmo", adapter=a)
        free = [x for x in r["rounds"] if x["phase"] == "free"]
        want = []
        for ch, x in zip(r["choices"], free):
            p0 = next(q for q in r["pieces"] if q["kind"] == "round" and q["phase"] == "free"
                      and q["idx"] == x["ci"])
            want.append(r["transcript"][:p0["start"]] + ch["menu"])
        n_reads += len(want)
        if a.read_texts != want:
            ctx_bad.append((c.name, "context"))
        if [ch["prefix_tokens_at_read"] for ch in r["choices"]] != [len(a.encode(t)) for t in want]:
            ctx_bad.append((c.name, "prefix tokens"))
    chk(f"runner_olmo: every read's context ({n_reads} reads over {len(testing.CASES_OLMO)} sessions) = "
        "the stored transcript so far + the menu, and prefix_tokens_at_read = its encoded length",
        not ctx_bad and n_reads > 50, ctx_bad[:3])

    # b3's context rule: stored transcript without menus or pick lines; prefix carries them
    ctx_ok = True
    for c, r, calls, _ in suite:
        t = r["transcript"]
        ctx_ok &= "| choice]" not in t and "Config choice (one word):" not in t
        ctx_ok &= not any(p["kind"] in ("menu", "pick") for p in r["pieces"])
        free = [x for x in r["rounds"] if x["phase"] == "free"]
        fcalls = calls[len(r["rounds"]) - len(free):]
        for ch, x, k in zip(r["choices"], free, fcalls):
            p = next(q for q in r["pieces"] if q["kind"] == "round" and q["phase"] == "free"
                     and q["idx"] == x["ci"])
            ctx_ok &= k["prefix"] == t[:p["start"]] + ch["menu"] + f" {ch['pick']}\n"
            ctx_ok &= k["segment"] == t[p["start"]:p["end"]] and ch["menu"].endswith("Config choice (one word):")
    chk("runner_olmo: context rule -- menus and pick lines reach the chosen round's prefix only; the "
        "stored transcript and its pieces carry none; choices record menu, a, b", ctx_ok)
    calls_ok = all(k["cached"] is False and k["injections"] == () and k["temp"] == OLMO_TEMP
                   and k["max_tokens"] == STOP_CAP for _, _, calls, _ in suite for k in calls)
    chk("runner_olmo: every generate call saw cached=False, injections=(), TEMP 0.7, STOP_CAP 60",
        calls_ok and sum(len(cs) for _, _, cs, _ in suite) == sum(len(r["rounds"]) for _, r, _, _ in suite))

    draws_ok = items_ok = props_ok = True
    for c, r, _, _ in suite:
        tpl = r["template"]
        draws_ok &= r["keys"] == {"arm": f"m-olmo-qual|sft|{tpl}|{r['s']}",
                                  "items": f"m-olmo-items-qual|sft|{r['s']}"}
        rng = np.random.default_rng(zlib.crc32(r["keys"]["arm"].encode()) % 2**31)
        forced = [x for x in r["rounds"] if x["phase"] == "forced"]
        free = [x for x in r["rounds"] if x["phase"] == "free"]
        draws_ok &= [x["seed"] for x in forced] == [int(rng.integers(2**31)) for _ in forced]
        for ch, x in zip(r["choices"], free):
            o = int(rng.integers(2))
            draws_ok &= ch["menu_a"] == (r["cell"]["P"] if o == 0 else r["cell"]["Q"])
            draws_ok &= x["seed"] == int(rng.integers(2**31))
        perm = np.random.default_rng(zlib.crc32(r["keys"]["items"].encode()) % 2**31).permutation(16)
        streams = {"P": list(perm[:8]), "Q": list(perm[8:])}
        for x in r["rounds"]:
            items_ok &= x["item"] == int(streams[x["role"]].pop(0))
            want = ((renders[x["item"]], "corrupted") if (r["contrast"] and x["role"] == "Q")
                    else (pool[x["item"]]["task"], "clean"))
            props_ok &= (x["task_text"], x["property"]) == want
    chk("runner_olmo: keys m-olmo-qual|sft|{template}|{s} / m-olmo-items-qual|sft|{s}; seeds and menu "
        "orders = an independent recomputation (4 seeds, then menu order, seed per choice)", draws_ok)
    chk("runner_olmo: items from the item key's [:8]/[8:] split; contrast Q delivers the render", items_ok and props_ok)
    sc_bad = _sc.m_config("Q-F0", "qual", "A0", 0, testing.case_cell("qwen", "A0", 0), "uncached")
    kit = testing.olmo_kit()
    try:
        run_session_olmo(testing.OLMoScriptedAdapter(), sc_bad, kit["audit"], kit["ban_ids"],
                         term_rx=kit["term_rx"])
        ok = False
    except ValueError:
        ok = True
    chk("runner_olmo: refuses a Qwen scaffold", ok)

    recs = [r for _, r, _, _ in suite]
    sham = [r for r in recs if not r["contrast"]]
    con = [r for r in recs if r["contrast"]]
    try:
        stripped = [readrule.strip_contrast(r) for r in con]
        redacted = [readrule.redact_sham(r) for r in sham]
        readrule.stage_report(recs)
        lines = [readrule.session_line(r) for r in recs]
        ok = True
    except Exception as e:                       # noqa: BLE001
        ok, stripped, redacted, lines = False, [], [], [repr(e)]
    chk("runner_olmo: every record passes strip_contrast / redact_sham / stage_report / session_line",
        ok and len(stripped) == len(con) and len(redacted) == len(sham), lines[:1])
    bo = {b.name: b for b in bars.OLMO_BARS("sft")}["round_degeneracy@G-F0m-OLMo-sft"]
    res = bars.stage_end_eval(recs, bo, bars.sham_domain)
    k_want = sum(x["audit"]["claim"] in ("audit", "echo") for r in sham for x in r["rounds"])
    chk("runner_olmo: bars.stage_end_eval on the sham-only OLMo domain (AuditSpec/echo over sham rounds; "
        "at most one claim per session)",
        (res.k, res.n) == (k_want, sum(len(r["rounds"]) for r in sham)) and k_want >= 2
        and all(sum(x["audit"]["claim"] is not None for x in r["rounds"]) <= 1 for r in recs), (res.k, res.n))
    with tempfile.TemporaryDirectory() as td:
        ident = resume.Identity(
            unit="OLMo-sft", stage="qual", template_set=["A0-OLMo-sft", "A0s-OLMo-sft"],
            lock_sha256="pre-lock", schedule_sha256="1" * 64, path="uncached", hour_cap=None,
            n={"A0-OLMo-sft": 8, "A0s-OLMo-sft": 16}, audit_v2_sha16=olmo_audit_sha16(),
            ban_sha=_audit.OLMO_BAN_IDS_SHA16,
            backend_identifier=resume.backend_identifier(testing.OLMoScriptedAdapter().provenance()),
            proposal_sha256="2" * 64)
        cpath = Path(td) / "OLMo-sft_qual.json"
        ck = resume.load_or_init(cpath, ident, resume=False)
        gver = []
        for r in recs:
            r = copy.deepcopy(r)                 # the suite's records stay unmarked
            gver += verify.verify_and_mark(r, substrate="olmo", pool=pool, renders=renders,
                                           schedule_cell=testing.case_cell("olmo", r["template"], r["s"]))
            resume.record_session(ck, r)         # C7: only a G-VER-verified record is recorded
        resume.write_checkpoint(cpath, ck)
        back = resume.load_or_init(cpath, ident, resume=True)
    chk("runner_olmo: every record passes G-VER (verify_and_mark), goes into a gate-stage checkpoint "
        "with the OLMo audit sha16 and reloads skip-only",
        gver == [] and resume.done_ids(back) == {(r["template"], r["s"]) for r in recs}, gver[:2])
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        testing.run_case(testing.CASES_OLMO[0], "olmo")
    words = {w for r in recs for w in r["cell"]["pair"]}
    lines_ok = all(not any(w in ln.lower() for w in words) and not re.search(r"\d", ln.split(" ", 3)[3])
                   and re.fullmatch(r"qual A0s?-OLMo-sft s=\d+ (valid|excluded:[a-z]+@(forced|free))", ln)
                   for ln in lines)
    chk("runner_olmo: the runner prints nothing; session lines carry no tag, pick or free index; a "
        "contrast free exclusion prints 'excluded@free', a sham one its class",
        buf.getvalue() == "" and lines_ok
        and readrule.session_line(by["olmo free echo ends"]).endswith("excluded:excluded@free")
        and readrule.session_line(by["olmo free AuditSpec claim ends"]).endswith("excluded:audit@free"),
        lines[:3])
