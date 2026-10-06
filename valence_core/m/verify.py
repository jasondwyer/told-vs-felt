"""PROPOSAL-m verifiers: F0m (Qwen) and F0m-OLMo (G-VER, v1.11 §3.1 m:284; §3 m:271's
hair triggers ``template_breakage`` and ``schedule_mismatch``; §2.1 m:159; §2.5 m:253).

G-VER (m:284): "every session's harness bytes reconstructed from its recorded fields,
the committed schedule and the rng streams before any artifact is written". The
verifier rebuilds the session's scaffold through the SAME code path the runner used
(``scaffold.m_config``) from the record's unit, stage, template, s, path and the
committed schedule's cell, replays it with the RECORDED picks, and compares:

  schedule_mismatch -- the cell against the committed schedule's; the keys against
      m:159's; the banner bytes and Note lines against ``banner.build_banner``; per
      round the label, role, pole, item, delivered text, property and seed; per
      choice the menu order (pair, map, start order, clause order, banner bytes or
      item stream differing from the committed schedule, m:271);
  template_breakage -- the harness bytes: the transcript rebuilt as banner +
      Σ(seg + text + "\\n") over forced rounds, then per free round on Qwen
      menu + " {pick}\\n" + seg + text + "\\n" and on OLMo seg + text + "\\n" (b3's
      context rule), compared byte for byte; the pieces rebuilt the same way and
      compared exactly; round numbers, template and menu indices, menu text; each
      pick against its read (choice_read's rule over the recorded p_a / p_b, verify KL
      exactly 0.0: the pick line is harness bytes written from the read); and the
      record's own consistency (shape, end rule, exclusion, strict scope, hair
      triggers, domain, first pick, completeness) -- G-VER's "fails" is the bar's
      numerator, so every failure that is not a schedule mismatch is breakage. A record
      the replay cannot walk (a non-record round, choice or read, a foreign-substrate
      audit, any residual exception) is breakage too: G-VER returns, it never raises.

Generations are taken from the recorded round texts, never located by searching for
"\\n" (maps/olmo.md §6 item 18). Messages name a field and a phase, never a label, a
pick or a free round's index, so the stage driver can count them without reading a
pick (build design §0 rule 5); they are still not printed for a contrast session.
"""
from __future__ import annotations

import json
from typing import Any, Mapping, Sequence

from . import audit as _audit
from . import banner as _banner
from . import keys
from . import scaffold as _sc

# PIN (Code, declared at LOCK v0.1): a verifier failure is schedule_mismatch when a
# cell, key, banner, menu order or per-round label/role/item/delivery/seed departs from
# the committed schedule and m:159's streams, and template_breakage otherwise (harness
# bytes, pieces, round/menu numbering, and the record's own end-rule consistency); a
# cell mismatch returns at once (the rebuild would only restate it).
BREAK = "template_breakage"
MISMATCH = "schedule_mismatch"
SUBSTRATES = ("qwen", "olmo")


def _canon(x: Any) -> str:
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def schedule_check(rec_or_scaffold: Any, schedule_cell: Mapping[str, Any]) -> list[str]:
    """A consistency assertion between a scaffold (or record) and its committed schedule
    row: cell == the committed schedule's and banner bytes == build_banner's; [] = clean.
    At the stage driver's call site it is true by construction (the scaffold is built from
    that very cell); what guards m:253/m:271's schedule_mismatch before a session is
    stages.load_committed and stages.startup_problems, and G-VER after it."""
    sc = rec_or_scaffold
    get = (lambda k: sc[k]) if isinstance(sc, Mapping) else (lambda k: getattr(sc, k))
    out = []
    cell = get("cell")
    if _canon(cell) != _canon(dict(schedule_cell)):
        out.append(f"{MISMATCH}: the session's cell differs from the committed schedule's")
        return out
    try:
        want, lines = _banner.build_banner(get("template"), cell["P"], cell["Q"], cell["clause"])
    except (ValueError, KeyError, TypeError):
        return out + [f"{MISMATCH}: no banner can be built for the scheduled cell"]
    if get("banner") != want or list(get("note_lines")) != list(lines):
        out.append(f"{MISMATCH}: banner bytes differ from build_banner's for the scheduled cell")
    return out


def _ends(substrate: str, r: Mapping) -> bool:
    return _audit.qwen_ends(r) if substrate == "qwen" else _audit.olmo_ends(r)


def verify_session(rec: Mapping[str, Any], *, substrate: str, pool: Sequence[dict],
                   renders: Sequence[str], schedule_cell: Mapping[str, Any]) -> list[str]:
    """[] iff the record's harness bytes and schedule-derived fields verify (G-VER).

    Never raises on a malformed record (finding 30): G-VER's failures are template_breakage
    hair triggers that STOP the stage through its STOP machinery (m:271, m:284), so a record
    the replay cannot even walk is a failure to report, not a traceback.
    """
    # PIN (Code, declared at LOCK v0.1): any residual exception while replaying a record
    # (beyond the explicit shape and type checks below) is template_breakage; a SystemExit
    # (a STOP raised by a module G-VER calls) still propagates as the STOP it is.
    try:
        return _verify_session(rec, substrate=substrate, pool=pool, renders=renders,
                               schedule_cell=schedule_cell)
    except Exception as e:                       # noqa: BLE001 -- reported, never swallowed
        return [f"{BREAK}: the record could not be replayed ({type(e).__name__})"]


def _verify_session(rec: Mapping[str, Any], *, substrate: str, pool: Sequence[dict],
                    renders: Sequence[str], schedule_cell: Mapping[str, Any]) -> list[str]:
    out: list[str] = []

    def bad(tag: str, msg: str) -> None:
        out.append(f"{tag}: {msg}")

    if not isinstance(rec, Mapping):
        return [f"{BREAK}: the record is not a mapping"]
    # --- header -------------------------------------------------------------------
    try:
        if substrate not in SUBSTRATES or rec.get("schema") != _sc.SCHEMA:
            raise ValueError("schema/substrate")
        unit, stage, template, s = rec["unit"], rec["stage"], rec["template"], rec["s"]
        if rec.get("substrate") != substrate or ("qwen" if unit == "Q-F0" else "olmo") != substrate:
            raise ValueError("substrate")
        if template not in keys.templates(unit) or rec.get("contrast") is not keys.is_contrast(template):
            raise ValueError("template")
        if type(s) is not int or s < 0:
            raise ValueError("s")
        keys.arm_key(unit, stage, template, s)            # the stage is one of the unit's
        path = rec["path"]
        if path not in ("cached", "uncached") or (path == "cached" and (substrate == "olmo"
                                                                        or stage == "time")):
            raise ValueError("path")
        rounds, choices = list(rec["rounds"]), list(rec["choices"])
        transcript, pieces = rec["transcript"], rec["pieces"]
    except (KeyError, TypeError, ValueError, NotImplementedError, AttributeError) as e:
        return [f"{BREAK}: record header malformed ({type(e).__name__}: {e})"]

    # --- schedule -------------------------------------------------------------------
    if _canon(rec.get("cell")) != _canon(dict(schedule_cell)):
        return [f"{MISMATCH}: the session's cell differs from the committed schedule's"]
    try:
        sc = _sc.m_config(unit, stage, template, s, schedule_cell, path, pool=pool, renders=renders)
    except (ValueError, TypeError, KeyError, NotImplementedError) as e:
        return [f"{MISMATCH}: no scaffold for the record's unit/stage/template/s/path and the "
                f"scheduled cell ({type(e).__name__})"]
    if _canon(rec.get("keys")) != _canon(sc.keys):
        bad(MISMATCH, "keys differ from m:159's for this unit, stage, template and s")
    if rec.get("banner") != sc.banner or list(rec.get("note_lines") or []) != list(sc.note_lines):
        bad(MISMATCH, "banner bytes or Note lines differ from build_banner's")
    if rec.get("j") != sc.j:
        bad(BREAK, "j differs from the stage's convention")

    # --- shape ----------------------------------------------------------------------
    if (not all(isinstance(r, Mapping) for r in rounds)
            or not all(isinstance(c, Mapping) and isinstance(c.get("read"), Mapping) for c in choices)
            or not isinstance(transcript, str) or not isinstance(pieces, list)):
        return out + [f"{BREAK}: a round, a choice or a read is not a record (or the transcript / "
                      f"pieces are malformed)"]
    forced = [r for r in rounds if r.get("phase") == "forced"]
    free = [r for r in rounds if r.get("phase") == "free"]
    if (rounds != forced + free or [r.get("ri") for r in forced] != list(range(len(forced)))
            or [r.get("ci") for r in free] != list(range(len(free)))
            or [c.get("ci") for c in choices] != list(range(len(choices)))
            or len(free) != len(choices) or len(forced) > sc.n_forced or len(free) > sc.n_free
            or (choices and len(forced) != sc.n_forced)):
        return out + [f"{BREAK}: rounds/choices shape is not banner, forced 0.., free 0.. with one "
                      f"chosen round per read"]

    # --- replay -----------------------------------------------------------------------
    tb = _sc.TranscriptBuilder(sc.banner)
    sched_fields = ("label", "role", "pole", "item", "task_text", "property", "seed")
    for ri, r in enumerate(forced):
        spec = sc.forced(ri)
        if any(r.get(f) != getattr(spec, f) for f in sched_fields):
            bad(MISMATCH, f"forced round {ri}: label/role/item/delivery/seed differ from the "
                          f"schedule and streams")
        if r.get("n") != spec.n or r.get("template_index") != spec.template_index:
            bad(BREAK, f"forced round {ri}: round number or template index differs")
        text = r.get("text")
        if not isinstance(text, str):
            return out + [f"{BREAK}: forced round {ri} carries no text"]
        tb.add("round", "forced", ri, spec.seg)
        tb.add("generation", "forced", ri, text)
        tb.add("joiner", "forced", ri, "\n")
    for ci, (c, r) in enumerate(zip(choices, free)):
        m = sc.menu(ci)
        if (c.get("menu_a"), c.get("menu_b")) != (m.a, m.b):
            bad(MISMATCH, "a free choice's menu order differs from the arm rng's")
        if c.get("n") != m.n or c.get("menu_index") != m.menu_index or c.get("menu") != m.menu:
            bad(BREAK, "a menu's number, template index or bytes differ")
        pick = c.get("pick")
        read = c["read"]
        if pick not in (m.a, m.b) or read.get("pick") != pick:
            return out + [f"{BREAK}: a pick is not its read's pick or not a menu label"]
        # PIN (Code, declared at LOCK v0.1): the pick line is harness bytes written from the
        # read (finding 27), so the recorded pick must follow choice_read's own rule over the
        # recorded read -- menu_a iff p_a >= p_b, ties to menu_a (readout.py:114) -- and the
        # read's verify KL must be exactly 0.0 (guard.insulated_read's halt; rule 26 (iii)).
        # No tolerance and no threshold: the recorded floats are compared as recorded. On
        # p_a == p_b exactly either label is consistent, because readout normalises AFTER
        # deciding (p / (mass + EPS)) and two adjacent raw values can round to one.
        pa, pb, kl = read.get("p_a"), read.get("p_b"), read.get("verify_kl")
        if type(pa) is not float or type(pb) is not float \
                or (pa > pb and pick != m.a) or (pa < pb and pick != m.b):
            bad(BREAK, "a pick disagrees with its read's p_a/p_b (choice_read: menu_a iff "
                       "p_a >= p_b)")
        if not (type(kl) is float and kl == 0.0):
            bad(BREAK, "a read's verify KL is not exactly 0.0")
        spec = sc.chosen(ci, pick)
        if c.get("picked_role") != spec.role or c.get("picked_pole") != spec.pole:
            bad(BREAK, "a choice's picked role/pole disagrees with its pick")
        if any(r.get(f) != getattr(spec, f) for f in sched_fields):
            bad(MISMATCH, "a free round's label/role/item/delivery/seed differ from the streams")
        if r.get("n") != spec.n or r.get("template_index") != spec.template_index:
            bad(BREAK, "a free round's number or template index differs")
        text = r.get("text")
        if not isinstance(text, str):
            return out + [f"{BREAK}: a free round carries no text"]
        if substrate == "qwen":
            tb.add("menu", "free", ci, m.menu)
            tb.add("pick", "free", ci, f" {pick}\n")
        tb.add("round", "free", ci, spec.seg)
        tb.add("generation", "free", ci, text)
        tb.add("joiner", "free", ci, "\n")
    if tb.text != transcript:
        bad(BREAK, "transcript bytes differ from the harness rebuilt from the recorded fields")
    if _canon(tb.pieces) != _canon(pieces):
        bad(BREAK, "pieces differ from the rebuilt layout")

    # --- the record's own consistency ---------------------------------------------------
    try:
        ras = [_audit.RoundAudit.from_dict(r["audit"]) for r in rounds]
    except (KeyError, TypeError, ValueError, AttributeError):
        return out + [f"{BREAK}: a round's audit record is malformed"]
    if any(ra.substrate != substrate or ra.phase != r["phase"] for ra, r in zip(ras, rounds)):
        # the end rules below are substrate-specific and refuse a foreign round (finding 30)
        return out + [f"{BREAK}: a round's audit substrate or phase disagrees with the round"]
    end = next((i for i, ra in enumerate(ras) if _ends(substrate, ra)), None)
    hair_at = next((i for i, ra in enumerate(ras) if ra.scaffold), None)
    stops = [i for i in (end, hair_at) if i is not None]
    last = min(stops) if stops else None
    if last is not None and last != len(rounds) - 1:
        bad(BREAK, "the session continued past a round that ends it")
    if last is None and not (len(forced) == sc.n_forced and len(free) == sc.n_free):
        bad(BREAK, "the session stopped without an end rule or a hair trigger")
    want_exc = None if end is None else {"class": ras[end].claim, "phase": ras[end].phase,
                                         "detail": ras[end].detail}
    if _canon(rec.get("exclusion")) != _canon(want_exc) or rec.get("excluded") is not (want_exc is not None):
        bad(BREAK, "exclusion fields disagree with the rounds' claims under the end rule")
    first = next((ra for ra in ras if ra.claim is not None), None)
    want_strict = None if first is None else {"class": first.claim, "phase": first.phase}
    if _canon(rec.get("strict_exclusion")) != _canon(want_strict):
        bad(BREAK, "strict_exclusion disagrees with the first claimed round")
    want_hair = [] if hair_at is None else [{"name": "scaffold_absorption", "phase": ras[hair_at].phase,
                                             "detail": "|".join(ras[hair_at].scaffold)}]
    if _canon(rec.get("hair_triggers")) != _canon(want_hair):
        bad(BREAK, "hair_triggers disagree with the rounds' scaffold hits")
    domain = bool(choices)
    if rec.get("domain") is not domain:
        bad(BREAK, "domain is not 'reached the first read'")
    want_fp = (choices[0]["pick"] == sc.P) if domain else None
    if rec.get("first_free_pick_P") is not want_fp:
        bad(BREAK, "first_free_pick_P disagrees with the first choice")
    complete = len(forced) == sc.n_forced and len(choices) == sc.n_free and len(free) == sc.n_free
    if rec.get("complete") is not complete:
        bad(BREAK, "complete disagrees with the rounds and reads")
    return out


def verify_and_mark(rec: dict, **kw) -> list[str]:
    """verify_session, then ``rec["verified"] = (problems == [])``; returns the problems."""
    problems = verify_session(rec, **kw)
    rec["verified"] = not problems
    return problems


# --- self-test -------------------------------------------------------------------
def _selftest(chk) -> None:
    import copy

    from . import testing

    pool, renders = _sc.pool_and_renders()
    q, o = testing.suite("qwen"), testing.suite("olmo")

    def run(rec, cell=None, sub=None):
        sub = sub or rec["substrate"]
        return verify_session(rec, substrate=sub, pool=pool, renders=renders,
                              schedule_cell=rec["cell"] if cell is None else cell)

    def sched(rec):
        return testing.case_cell(rec["substrate"], rec["template"], rec["s"])

    allq = {c.name: run(r, sched(r)) for c, r, _, _ in q}
    allo = {c.name: run(r, sched(r)) for c, r, _, _ in o}
    chk(f"verify: every produced record verifies against the committed schedule ({len(q)} Qwen, "
        f"{len(o)} OLMo: clean, excluded at forced and free, hair-trigger stops)",
        not any(allq.values()) and not any(allo.values()),
        {k: v[:1] for k, v in {**allq, **allo}.items() if v})

    def tags(problems):
        return {p.split(":", 1)[0] for p in problems}

    rq = copy.deepcopy(q[0][1])
    ro = copy.deepcopy(o[0][1])
    cases = {}
    for name, rec in (("qwen", rq), ("olmo", ro)):
        t = rec["transcript"]
        g = next(p for p in rec["pieces"] if p["kind"] == "generation")
        h = next(p for p in rec["pieces"] if p["kind"] == "round" and p["phase"] == "free")
        for where, pos in (("generation", g["start"]), ("harness", h["start"] + 3)):
            x = copy.deepcopy(rec)
            ch = x["transcript"][pos]
            x["transcript"] = t[:pos] + ("X" if ch != "X" else "Y") + t[pos + 1:]
            cases[f"{name} one {where} byte"] = run(x)
    chk("verify: one transcript byte changed (a generation byte; a harness byte) -> template_breakage, "
        "no schedule_mismatch (both substrates)",
        all(tags(v) == {BREAK} for v in cases.values()), {k: tags(v) for k, v in cases.items()})
    other = sched(q[1][1])
    rb = copy.deepcopy(rq)
    rb["banner"] = rb["banner"].replace("Prefer", "Choose")
    rs = copy.deepcopy(rq)
    rs["rounds"][2]["seed"] += 1
    ri = copy.deepcopy(ro)
    ri["rounds"][0]["item"] = (ri["rounds"][0]["item"] + 1) % 16
    rm = copy.deepcopy(ro)
    rm["choices"][0]["menu_a"], rm["choices"][0]["menu_b"] = rm["choices"][0]["menu_b"], rm["choices"][0]["menu_a"]
    rk = copy.deepcopy(rq)
    rk["keys"]["arm"] = "m|A0|0"
    mism = {"changed cell": run(rq, other), "changed banner": run(rb), "changed seed": run(rs),
            "changed item": run(ri), "changed menu order": run(rm), "changed key": run(rk)}
    chk("verify: a changed cell, banner, seed, item, menu order or key -> schedule_mismatch",
        all(MISMATCH in tags(v) for v in mism.values()) and mism["changed cell"] == [
            f"{MISMATCH}: the session's cell differs from the committed schedule's"],
        {k: sorted(tags(v)) for k, v in mism.items()})
    rt = copy.deepcopy(rq)
    rt["rounds"][1]["text"] = "Eight."
    ex = copy.deepcopy(q[[c.name for c, *_ in q].index("qwen forced v2 ends (no read)")][1])
    ex["exclusion"] = None
    ex["excluded"] = False
    cont = copy.deepcopy(q[[c.name for c, *_ in q].index("qwen free lexical ends after its round (contrast)")][1])
    cont["rounds"][-1]["audit"]["claim"] = None
    cont["rounds"][-1]["audit"]["detail"] = None
    cont["rounds"][-1]["audit"]["lexical_raw"] = None
    fp = copy.deepcopy(rq)
    fp["first_free_pick_P"] = not fp["first_free_pick_P"]
    om = copy.deepcopy(ro)
    pc = om["choices"][0]
    gi = next(i for i, p in enumerate(om["pieces"]) if p["kind"] == "round" and p["phase"] == "free")
    at = om["pieces"][gi]["start"]
    om["transcript"] = om["transcript"][:at] + pc["menu"] + f" {pc['pick']}\n" + om["transcript"][at:]
    brk = {"recorded text vs transcript": run(rt), "exclusion dropped": run(ex),
           "an end-rule claim erased (stopped without an end rule)": run(cont),
           "first pick flipped": run(fp), "OLMo menu written": run(om),
           "wrong substrate": run(rq, sub="olmo")}
    op = copy.deepcopy(ro)
    op["path"] = "cached"
    brk["OLMo record claiming the cached path"] = run(op)
    chk("verify: a recorded text off its transcript, a dropped exclusion, an erased end-rule claim, "
        "a flipped first pick, a menu in an OLMo stored transcript, a wrong substrate, a cached OLMo "
        "record -> template_breakage",
        all(BREAK in tags(v) for v in brk.values()), {k: sorted(tags(v)) for k, v in brk.items()})

    # --- finding 28: one tampered record per consistency clause, each asserting the
    # clause's OWN message (deleting the clause fails its case) -------------------------
    qn = {c.name: r for c, r, _, _ in q}
    on = {c.name: r for c, r, _, _ in o}

    def tamper(base, fn):
        x = copy.deepcopy(base)
        fn(x)
        return x

    def other_label(c):
        return c["menu_b"] if c["pick"] == c["menu_a"] else c["menu_a"]

    def setf(path, value):
        def f(x):
            *head, last = path
            for k in head:
                x = x[k]
            x[last] = value(x[last]) if callable(value) else value
        return f

    def truncate_last_free(x):
        last = x["choices"][-1]["ci"]
        cut = min(pc["start"] for pc in x["pieces"] if pc["phase"] == "free" and pc["idx"] == last)
        x["pieces"] = [pc for pc in x["pieces"] if not (pc["phase"] == "free" and pc["idx"] == last)]
        x["transcript"] = x["transcript"][:cut]
        x["rounds"], x["choices"], x["complete"] = x["rounds"][:-1], x["choices"][:-1], False

    def past_end(x):
        lexr = qn["qwen forced lexical ends"]["rounds"][3]["audit"]
        x["rounds"][1]["audit"] = copy.deepcopy(lexr)
        x["exclusion"] = {"class": "lexical", "phase": "forced", "detail": lexr["detail"]}
        x["excluded"] = True
        x["strict_exclusion"] = {"class": "lexical", "phase": "forced"}

    def swap_p(x):
        c = next(c for c in x["choices"] if c["read"]["p_a"] != c["read"]["p_b"])
        c["read"]["p_a"], c["read"]["p_b"] = c["read"]["p_b"], c["read"]["p_a"]

    def alt_history(base):
        """The first pick flipped and the session rebuilt consistently around it, the read's
        probabilities left as read (finding 27's (a))."""
        x = copy.deepcopy(base)
        scf = _sc.m_config(x["unit"], x["stage"], x["template"], x["s"], x["cell"], x["path"],
                           pool=pool, renders=renders)
        tb = _sc.TranscriptBuilder(scf.banner)
        for ri, r in enumerate(r for r in x["rounds"] if r["phase"] == "forced"):
            sp = scf.forced(ri)
            for kind, frag in (("round", sp.seg), ("generation", r["text"]), ("joiner", "\n")):
                tb.add(kind, "forced", ri, frag)
        for ci, c in enumerate(x["choices"]):
            m = scf.menu(ci)
            pick = (m.b if c["pick"] == m.a else m.a) if ci == 0 else c["pick"]
            c["pick"] = c["read"]["pick"] = pick
            sp = scf.chosen(ci, pick)
            c["picked_role"], c["picked_pole"] = sp.role, sp.pole
            r = next(r for r in x["rounds"] if r["phase"] == "free" and r["ci"] == ci)
            for f in ("label", "role", "pole", "item", "task_text", "property", "seed", "n",
                      "template_index"):
                r[f] = getattr(sp, f)
            if x["substrate"] == "qwen":
                tb.add("menu", "free", ci, m.menu)
                tb.add("pick", "free", ci, f" {pick}\n")
            for kind, frag in (("round", sp.seg), ("generation", r["text"]), ("joiner", "\n")):
                tb.add(kind, "free", ci, frag)
        x["transcript"], x["pieces"] = tb.text, tb.pieces
        x["first_free_pick_P"] = x["choices"][0]["pick"] == scf.P
        return x

    PE = "the session continued past a round that ends it"
    clauses = {   # name: (record, the clause's own message)
        "j": (tamper(rq, setf(("j",), 99)), "j differs"),
        "shape: a read without its chosen round": (tamper(rq, setf(("choices",), lambda v: v[:-1])),
                                                   "rounds/choices shape"),
        "shape: a free round before the forced ones": (
            tamper(rq, setf(("rounds",), lambda v: [v[4]] + v[:4] + v[5:])), "rounds/choices shape"),
        "forced task_text": (tamper(rq, setf(("rounds", 3, "task_text"), lambda v: v + " ")),
                             "forced round 3: label/role/item/delivery/seed"),
        "forced pole": (tamper(ro, setf(("rounds", 0, "pole"), lambda v: "neg" if v == "pos" else "pos")),
                        "forced round 0: label/role/item/delivery/seed"),
        "free property": (tamper(rq, setf(("rounds", 5, "property"),
                                          lambda v: "corrupted" if v == "clean" else "clean")),
                          "a free round's label/role/item/delivery/seed"),
        "forced n": (tamper(rq, setf(("rounds", 0, "n"), 7)), "forced round 0: round number or template"),
        "forced template_index": (tamper(ro, setf(("rounds", 1, "template_index"), lambda v: (v + 1) % 4)),
                                  "forced round 1: round number or template"),
        "free n": (tamper(ro, setf(("rounds", 6, "n"), lambda v: v + 1)),
                   "a free round's number or template index"),
        "free template_index": (tamper(rq, setf(("rounds", 7, "template_index"), lambda v: (v + 1) % 4)),
                                "a free round's number or template index"),
        "menu n": (tamper(rq, setf(("choices", 0, "n"), lambda v: v + 1)), "a menu's number, template index"),
        "menu_index": (tamper(ro, setf(("choices", 2, "menu_index"), lambda v: (v + 1) % 4)),
                       "a menu's number, template index"),
        "Qwen menu bytes": (tamper(rq, setf(("choices", 1, "menu"), lambda v: v[:-1] + ";")),
                            "a menu's number, template index or bytes"),
        "OLMo menu bytes (not in the stored transcript)": (
            tamper(ro, setf(("choices", 1, "menu"), lambda v: v.replace("Config", "config", 1))),
            "a menu's number, template index or bytes"),
        "read.pick": (tamper(rq, lambda x: x["choices"][0]["read"].__setitem__(
            "pick", other_label(x["choices"][0]))), "a pick is not its read's pick"),
        "picked_role": (tamper(rq, setf(("choices", 0, "picked_role"), lambda v: "Q" if v == "P" else "P")),
                        "picked role/pole"),
        "picked_pole": (tamper(ro, setf(("choices", 3, "picked_pole"), lambda v: "neg" if v == "pos" else "pos")),
                        "picked role/pole"),
        "pieces": (tamper(rq, lambda x: (x["pieces"][3].__setitem__("end", x["pieces"][3]["end"] - 1),
                                         x["pieces"][4].__setitem__("start", x["pieces"][4]["start"] - 1))),
                   "pieces differ"),
        "audit phase": (tamper(rq, setf(("rounds", 2, "audit", "phase"), "free")),
                        "audit substrate or phase disagrees"),
        "audit substrate (OLMo record, Qwen audit)": (tamper(ro, setf(("rounds", 2, "audit", "substrate"), "qwen")),
                                                      "audit substrate or phase disagrees"),
        "past its end rule": (tamper(qn["qwen clean A0s s0"], past_end), PE),
        "stopped without an end rule": (tamper(rq, truncate_last_free), "stopped without an end rule"),
        "strict_exclusion": (tamper(rq, setf(("strict_exclusion",), {"class": "v2", "phase": "free"})),
                             "strict_exclusion disagrees"),
        "hair_triggers": (tamper(ro, setf(("hair_triggers",), [{"name": "scaffold_absorption",
                                                                "phase": "free", "detail": "x"}])),
                          "hair_triggers disagree"),
        "domain": (tamper(rq, setf(("domain",), False)), "domain is not"),
        "complete": (tamper(ro, setf(("complete",), False)), "complete disagrees"),
        "contrast flag": (tamper(rq, setf(("contrast",), False)), "record header malformed"),
        "read p_a/p_b swapped (Qwen)": (tamper(rq, swap_p), "a pick disagrees with its read's p_a/p_b"),
        "read p_a/p_b swapped (OLMo)": (tamper(ro, swap_p), "a pick disagrees with its read's p_a/p_b"),
        "alternate history, first pick flipped (Qwen)": (alt_history(rq), "a pick disagrees with its read"),
        "alternate history, first pick flipped (OLMo)": (alt_history(ro), "a pick disagrees with its read"),
        "verify KL 0.5": (tamper(rq, setf(("choices", 2, "read", "verify_kl"), 0.5)), "verify KL is not exactly"),
        "verify KL negative": (tamper(ro, setf(("choices", 2, "read", "verify_kl"), -1e-12)),
                               "verify KL is not exactly"),
        "verify KL NaN": (tamper(rq, setf(("choices", 0, "read", "verify_kl"), float("nan"))),
                          "verify KL is not exactly"),
        "verify KL absent": (tamper(ro, lambda x: x["choices"][4]["read"].pop("verify_kl")),
                             "verify KL is not exactly"),
    }
    missed = {}
    for nm, (rec, needle) in clauses.items():
        got = run(rec)
        if not any(needle in m for m in got) or not got:
            missed[nm] = got[:2]
    chk(f"verify: every consistency clause fires on its own tampered record ({len(clauses)}: j, shape, "
        "task_text/pole/property, forced and free n/template_index, menu n/index/bytes incl. OLMo, "
        "read.pick, picked role/pole, pieces, audit phase/substrate, past its end rule, stopped "
        "without one, strict, hair, domain, complete, contrast, pick vs p_a/p_b, verify KL)",
        not missed, missed)
    only = {nm: run(clauses[nm][0]) for nm in ("j", "past its end rule", "stopped without an end rule",
                                                "domain", "complete", "hair_triggers", "strict_exclusion",
                                                "OLMo menu bytes (not in the stored transcript)",
                                                "verify KL 0.5", "read p_a/p_b swapped (Qwen)")}
    chk("verify: those single-clause tampers fire their clause ALONE (a past-end session is not "
        "reported as stopped-early, and vice versa)",
        all(len(v) == 1 for v in only.values()), {k: v for k, v in only.items() if len(v) != 1})

    def tie(x, pick_b):
        c = x["choices"][0]
        c["read"]["p_b"] = c["read"]["p_a"]
        if pick_b != (c["pick"] == c["menu_b"]):
            raise AssertionError("tie case built on the wrong pick")
    ties = []
    for base in (rq, ro):
        for want_b in (False, True):
            src = next((r for _, r, _, _ in (q if base is rq else o)
                        if r["choices"] and (r["choices"][0]["pick"] == r["choices"][0]["menu_b"]) == want_b
                        and r["template"] == base["template"]), None)
            if src is not None:
                ties.append(run(tamper(src, lambda x: tie(x, want_b))))
    chk("verify: must-not-fire -- exactly equal recorded p_a/p_b accept either label (readout "
        "normalises after deciding); every produced record's pick follows its read and KL is 0.0",
        len(ties) == 4 and all(v == [] for v in ties)
        and all((ch["pick"] == (ch["menu_a"] if ch["read"]["p_a"] >= ch["read"]["p_b"] else ch["menu_b"]))
                and ch["read"]["verify_kl"] == 0.0 for _, r, _, _ in q + o for ch in r["choices"]), ties)

    # --- finding 30: a malformed record returns template_breakage, never raises ----------
    malformed = {
        "OLMo record with a Qwen-substrate audit dict": tamper(
            ro, lambda x: x["rounds"][2].__setitem__("audit", copy.deepcopy(rq["rounds"][2]["audit"]))),
        "a choice that is not a dict": tamper(rq, setf(("choices", 0), "slate")),
        "a round that is None": tamper(rq, setf(("rounds", 0), None)),
        "a read that is not a dict": tamper(ro, setf(("choices", 0, "read"), "x")),
        "an audit that is None": tamper(rq, setf(("rounds", 1, "audit"), None)),
        "pieces None": tamper(rq, setf(("pieces",), None)),
        "transcript None": tamper(ro, setf(("transcript",), None)),
        "the record None": None, "the record a list": [rq],
        "an exclusion field that is not JSON (a set; only the catch-all sees it)": tamper(
            rq, setf(("exclusion",), {"class": {"v2", "echo"}})),
    }
    raised, silent = {}, []
    for nm, rec in malformed.items():
        try:
            got = verify_session(rec, substrate="olmo" if nm.startswith("OLMo") else "qwen", pool=pool,
                                 renders=renders, schedule_cell=sched(rq))
            if not got or tags(got) - {BREAK, MISMATCH} or BREAK not in tags(got) and MISMATCH not in tags(got):
                silent.append(nm)
        except Exception as e:                    # noqa: BLE001
            raised[nm] = type(e).__name__
    olmo_q = verify_session(malformed["OLMo record with a Qwen-substrate audit dict"], substrate="olmo",
                            pool=pool, renders=renders, schedule_cell=sched(ro))
    unjson = verify_session(malformed["an exclusion field that is not JSON (a set; only the catch-all "
                                      "sees it)"], substrate="qwen", pool=pool, renders=renders,
                            schedule_cell=sched(rq))
    chk(f"verify: malformed records ({len(malformed)}: foreign-substrate audit, non-dict choice / round "
        "/ read / audit, bad pieces / transcript, a non-mapping record, a non-JSON field) return "
        "template_breakage and never raise", not raised and not silent
        and olmo_q == [f"{BREAK}: a round's audit substrate or phase disagrees with the round"]
        and unjson == [f"{BREAK}: the record could not be replayed (TypeError)"],
        (raised, silent, olmo_q, unjson))

    # the committed schedule files are the cells the suite ran under (data/m/schedules)
    committed_ok = True
    for _, r, _, _ in q + o:
        fn = _sc.REPO / "data" / "m" / "schedules" / f"{r['unit']}_{r['stage']}_{r['template']}.json"
        cells = json.loads(fn.read_text())["cells"]
        committed_ok &= r["s"] < len(cells) and _canon(cells[r["s"]]) == _canon(r["cell"]) \
            and _canon(sched(r)) == _canon(r["cell"])
    chk("verify: every suite record's cell IS its committed schedule file's cell "
        "(data/m/schedules/{unit}_qual_{template}.json)", committed_ok)
    words = {w for _, r, _, _ in q + o for w in r["cell"]["pair"]}
    msgs = [p for v in list(cases.values()) + list(mism.values()) + list(brk.values()) for p in v]
    chk("verify: no mismatch message names a label or pick",
        msgs and not any(w in m.lower() for m in msgs for w in words), msgs[:2])
    vm = copy.deepcopy(rq)
    p1 = verify_and_mark(vm, substrate="qwen", pool=pool, renders=renders, schedule_cell=vm["cell"])
    vm2 = copy.deepcopy(rs)
    p2 = verify_and_mark(vm2, substrate="qwen", pool=pool, renders=renders, schedule_cell=vm2["cell"])
    chk("verify: verify_and_mark sets verified True on [] and False on a mismatch",
        p1 == [] and vm["verified"] is True and p2 and vm2["verified"] is False)
    pre_ok = schedule_check(rq, sched(rq)) == [] and schedule_check(rq, other) and schedule_check(rb, sched(rb))
    sc_obj = _sc.m_config("Q-F0", "qual", "A0", 0, sched(rq), "uncached")
    chk("verify: schedule_check (the driver's pre-session check) passes the scheduled cell and banner, "
        "fires on another cell or changed banner bytes; accepts a scaffold too",
        bool(pre_ok) and schedule_check(sc_obj, sched(rq)) == [])
