"""The F3 verifier -- G-VER for Q-F3 (PROPOSAL-m v1.11 §3.1 m:284, carried by m:298; §3 m:271's
``template_breakage`` and ``schedule_mismatch``; §2.1 m:159; §2.2 m:174; §2.5 m:253).

m:284: "every session's harness bytes reconstructed from its recorded fields, the committed schedule
and the rng streams before any artifact is written". ``verify_session`` rebuilds the session's
scaffold through the SAME code path the runner used (``scaffold.f3_config``) from the record's stage,
template, s, path and reasoning cap and the committed schedule's cell, replays it with the RECORDED
generations, reasoning lines and picks, and compares:

  schedule_mismatch -- the cell, the keys (m:159), the banner bytes and Note lines (§2.5), per round
      the label, role, pole, item, delivered text, property and seed, per reasoning line its seed and
      cap, per choice the menu order -- and the template's role: A2/A2s and A3/A3s carry one banner, so
      a contrast record must have served the corrupted render on its Q role and a sham record clean
      text throughout (Code's PIN, the template name decides, the delivery is asserted);
  template_breakage -- the harness bytes (banner; forced ``seg + text + "\\n"``; per free choice the
      reasoning block + line + ``"\\n"``, then ``menu + " {pick}\\n" + seg + text + "\\n"``), the
      pieces, round and menu numbering, each pick against its read (menu_a iff p_a >= p_b, verify KL
      exactly 0.0), each reasoning line's classes and scaffold hits re-derived from its text, and the
      record's own end rules (exclusion, strict scope, hair triggers, domain, first pick, completeness).

It never raises on a malformed record (a failure to report is template_breakage); messages name a
field and a phase, never a label, a pick or a free index.
"""
from __future__ import annotations

import json
from typing import Any, Mapping, Sequence

from valence_core.m import audit as m_audit

from . import keys, lines
from . import scaffold as sc_mod

BREAK = "template_breakage"
MISMATCH = "schedule_mismatch"


def _canon(x: Any) -> str:
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def verify_session(rec: Mapping[str, Any], *, pool: Sequence[dict], renders: Sequence[str],
                   schedule_cell: Mapping[str, Any], scaffold_strings: Sequence[str]) -> list[str]:
    """[] iff the record's harness bytes and schedule-derived fields verify (G-VER); never raises
    except a SystemExit a module it calls raises."""
    try:
        return _verify(rec, pool=pool, renders=renders, schedule_cell=schedule_cell,
                       scaffold_strings=scaffold_strings)
    except Exception as e:                       # noqa: BLE001 -- reported, never swallowed
        return [f"{BREAK}: the record could not be replayed ({type(e).__name__})"]


def _verify(rec, *, pool, renders, schedule_cell, scaffold_strings) -> list[str]:
    out: list[str] = []

    def bad(tag: str, msg: str) -> None:
        out.append(f"{tag}: {msg}")

    if not isinstance(rec, Mapping):
        return [f"{BREAK}: the record is not a mapping"]
    try:
        if (rec.get("schema") != sc_mod.SCHEMA or rec.get("format") != sc_mod.FORMAT
                or rec.get("substrate") != "qwen" or rec.get("unit") != keys.UNIT):
            raise ValueError("schema/format/substrate/unit")
        stage, template, s = rec["stage"], rec["template"], rec["s"]
        if rec.get("contrast") is not keys.is_contrast(template):
            raise ValueError("template")
        if type(s) is not int or s < 0:
            raise ValueError("s")
        keys.arm_key(stage, template, s)
        path, cap = rec["path"], rec["reasoning_cap"]
        rounds, choices, rlines = list(rec["rounds"]), list(rec["choices"]), list(rec["reasoning"])
        transcript, pieces = rec["transcript"], rec["pieces"]
    except (KeyError, TypeError, ValueError) as e:
        return [f"{BREAK}: record header malformed ({type(e).__name__}: {e})"]
    if _canon(rec.get("cell")) != _canon(dict(schedule_cell)):
        return [f"{MISMATCH}: the session's cell differs from the committed schedule's"]
    try:
        sc = sc_mod.f3_config(stage, template, s, schedule_cell, path, reasoning_cap=cap, pool=pool,
                              renders=renders)
    except (ValueError, TypeError, KeyError) as e:
        return [f"{MISMATCH}: no scaffold for the record's stage/template/s/path/cap and the scheduled cell "
                f"({type(e).__name__})"]
    if _canon(rec.get("keys")) != _canon(sc.keys):
        bad(MISMATCH, "keys differ from m:159's for this stage, template and s")
    if rec.get("banner") != sc.banner or list(rec.get("note_lines") or []) != list(sc.note_lines):
        bad(MISMATCH, "banner bytes or Note lines differ from the arm's §2.5 bytes")
    if rec.get("j") != sc.j:
        bad(BREAK, "j differs from the stage's convention")
    if (not all(isinstance(r, Mapping) for r in rounds) or not all(isinstance(x, Mapping) for x in rlines)
            or not all(isinstance(c, Mapping) and isinstance(c.get("read"), Mapping) for c in choices)
            or not isinstance(transcript, str) or not isinstance(pieces, list)):
        return out + [f"{BREAK}: a round, line, choice or read is not a record (or transcript / pieces malformed)"]
    forced = [r for r in rounds if r.get("phase") == "forced"]
    free = [r for r in rounds if r.get("phase") == "free"]
    if (rounds != forced + free or [r.get("ri") for r in forced] != list(range(len(forced)))
            or [r.get("ci") for r in free] != list(range(len(free)))
            or [c.get("ci") for c in choices] != list(range(len(choices)))
            or [x.get("ci") for x in rlines] != list(range(len(rlines)))
            or len(free) != len(choices) or len(forced) > sc.n_forced or len(rlines) > sc.n_free
            or ((choices or rlines) and len(forced) != sc.n_forced)
            or not (len(choices) <= len(rlines) <= len(choices) + 1)):
        return out + [f"{BREAK}: shape is not banner, forced 0.., then per choice a line, a read and a round"]
    # the template's role on the delivery (A2/A2s and A3/A3s share a banner)
    tb = sc_mod.TranscriptBuilder(sc.banner)
    sched = ("label", "role", "pole", "item", "task_text", "property", "seed")
    for ri, r in enumerate(forced):
        spec = sc.forced(ri)
        if any(r.get(f) != getattr(spec, f) for f in sched):
            bad(MISMATCH, f"forced round {ri}: label/role/item/delivery/seed differ from the schedule and streams")
        if r.get("n") != spec.n or r.get("template_index") != spec.template_index:
            bad(BREAK, f"forced round {ri}: round number or template index differs")
        if not isinstance(r.get("text"), str):
            return out + [f"{BREAK}: forced round {ri} carries no text"]
        tb.add("round", "forced", ri, spec.seg)
        tb.add("generation", "forced", ri, r["text"])
        tb.add("joiner", "forced", ri, "\n")
    for ci, x in enumerate(rlines):
        rs = sc.reasoning(ci)
        if x.get("seed") != rs.seed or x.get("cap") != rs.cap or x.get("n") != rs.n:
            bad(MISMATCH, "a reasoning line's seed / cap / n differ from the streams")
        t = x.get("text")
        if not isinstance(t, str):
            return out + [f"{BREAK}: a reasoning line carries no text"]
        try:
            want = lines.classify_line(t, n_tok=x["n_tok"], cap=rs.cap, stop_reason=x["stop_reason"],
                                       cap_hit=x["cap_hit"], echo_set=lines.echo_lines(sc.P, sc.Q, rs.n),
                                       scaffold_strings=scaffold_strings)
            if _canon(x.get("audit")) != _canon(want.as_dict()):
                bad(BREAK, "a reasoning line's classes or scaffold hits differ from its text's")
        except (KeyError, ValueError, TypeError):
            bad(BREAK, "a reasoning line's generation fields are malformed")
        tb.add("reasoning", "free", ci, rs.seg)
        tb.add("reasoning_text", "free", ci, t)
        tb.add("reasoning_joiner", "free", ci, "\n")
        if ci >= len(choices):
            break
        c, r = choices[ci], free[ci]
        m = sc.menu(ci)
        if (c.get("menu_a"), c.get("menu_b")) != (m.a, m.b):
            bad(MISMATCH, "a free choice's menu order differs from the arm rng's")
        if c.get("n") != m.n or c.get("menu_index") != m.menu_index or c.get("menu") != m.menu:
            bad(BREAK, "a menu's number, template index or bytes differ")
        pick, read = c.get("pick"), c["read"]
        if pick not in (m.a, m.b) or read.get("pick") != pick:
            return out + [f"{BREAK}: a pick is not its read's pick or not a menu label"]
        pa, pb, kl = read.get("p_a"), read.get("p_b"), read.get("verify_kl")
        # PIN (Code, declared at LOCK-m-F3 v0.1): m's read check, carried: the pick follows choice_read's
        # rule over the recorded p_a / p_b (menu_a iff p_a >= p_b, a tie either way) and the verify KL is
        # exactly 0.0; no tolerance.
        if type(pa) is not float or type(pb) is not float or (pa > pb and pick != m.a) or (pa < pb and pick != m.b):
            bad(BREAK, "a pick disagrees with its read's p_a/p_b")
        if not (type(kl) is float and kl == 0.0):
            bad(BREAK, "a read's verify KL is not exactly 0.0")
        spec = sc.chosen(ci, pick)
        if c.get("picked_role") != spec.role or c.get("picked_pole") != spec.pole:
            bad(BREAK, "a choice's picked role/pole disagrees with its pick")
        if any(r.get(f) != getattr(spec, f) for f in sched):
            bad(MISMATCH, "a free round's label/role/item/delivery/seed differ from the streams")
        if r.get("n") != spec.n or r.get("template_index") != spec.template_index:
            bad(BREAK, "a free round's number or template index differs")
        if not isinstance(r.get("text"), str):
            return out + [f"{BREAK}: a free round carries no text"]
        tb.add("menu", "free", ci, m.menu)
        tb.add("pick", "free", ci, f" {pick}\n")
        tb.add("round", "free", ci, spec.seg)
        tb.add("generation", "free", ci, r["text"])
        tb.add("joiner", "free", ci, "\n")
    if tb.text != transcript:
        bad(BREAK, "transcript bytes differ from the harness rebuilt from the recorded fields")
    if _canon(tb.pieces) != _canon(pieces):
        bad(BREAK, "pieces differ from the rebuilt layout")
    # PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B22): the contrast/sham role is the
    # template name's; the delivery must agree -- a contrast record's Q-role rounds the corrupted
    # render, every other round clean text (sched fields above compare each against the scaffold's).
    roles = {(r["role"], r["property"]) for r in rounds if "role" in r and "property" in r}
    if sc.contrast and any((p == "corrupted") != (ro == "Q") for ro, p in roles):
        bad(MISMATCH, "a contrast template's delivery is not Q-role-corrupted")
    if not sc.contrast and any(p != "clean" for _, p in roles):
        bad(MISMATCH, "a sham template served a corrupted render")
    # the record's own end rules
    try:
        ras = [m_audit.RoundAudit.from_dict(r["audit"]) for r in rounds]
        las = [lines.LineAudit.from_dict(x["audit"]) for x in rlines]
    except (KeyError, TypeError, ValueError, AttributeError):
        return out + [f"{BREAK}: a round's or line's audit record is malformed"]
    if any(ra.substrate != "qwen" or ra.phase != r["phase"] for ra, r in zip(ras, rounds)):
        return out + [f"{BREAK}: a round's audit substrate or phase disagrees with the round"]
    # the session's event order: forced rounds, then per choice (line, round)
    events = [("round", i) for i in range(len(forced))]
    for ci in range(len(rlines)):
        events.append(("line", ci))
        if ci < len(free):
            events.append(("round", len(forced) + ci))
    end_at = hair_at = None
    for k, (kind, i) in enumerate(events):
        if kind == "round":
            if end_at is None and m_audit.qwen_ends(ras[i]):
                end_at = k
            if hair_at is None and ras[i].scaffold:
                hair_at = k
        elif las[i].scaffold:
            end_at = k if end_at is None else end_at
            hair_at = k if hair_at is None else hair_at
    stops = [x for x in (end_at, hair_at) if x is not None]
    last = min(stops) if stops else None
    if last is not None and last != len(events) - 1:
        bad(BREAK, "the session continued past an event that ends it")
    if last is None and not (len(forced) == sc.n_forced and len(rlines) == sc.n_free and len(free) == sc.n_free):
        bad(BREAK, "the session stopped without an end rule or a hair trigger")
    want_exc = None
    if end_at is not None:
        kind, i = events[end_at]
        if kind == "round":
            want_exc = {"class": ras[i].claim, "phase": ras[i].phase, "detail": ras[i].detail}
        else:
            want_exc = {"class": "scaffold", "phase": "reasoning", "ci": i, "detail": "|".join(las[i].scaffold)}
    if _canon(rec.get("exclusion")) != _canon(want_exc) or rec.get("excluded") is not (want_exc is not None):
        bad(BREAK, "exclusion fields disagree with the rounds' claims and lines under the end rule")
    first = next((ra for ra in ras if ra.claim is not None), None)
    want_strict = None if first is None else {"class": first.claim, "phase": first.phase}
    if _canon(rec.get("strict_exclusion")) != _canon(want_strict):
        bad(BREAK, "strict_exclusion disagrees with the first claimed round")
    want_hair = []
    if hair_at is not None:
        kind, i = events[hair_at]
        want_hair = ([{"name": "scaffold_absorption", "phase": ras[i].phase, "detail": "|".join(ras[i].scaffold)}]
                     if kind == "round" else
                     [{"name": "scaffold_absorption", "phase": "reasoning", "ci": i,
                       "detail": "|".join(las[i].scaffold)}])
    if _canon(rec.get("hair_triggers")) != _canon(want_hair):
        bad(BREAK, "hair_triggers disagree with the rounds' and lines' scaffold hits")
    domain = bool(choices)
    if rec.get("domain") is not domain:
        bad(BREAK, "domain is not 'reached the first read'")
    want_fp = (choices[0]["pick"] == sc.P) if domain else None
    if rec.get("first_free_pick_P") is not want_fp:
        bad(BREAK, "first_free_pick_P disagrees with the first choice")
    complete = (len(forced) == sc.n_forced and len(rlines) == sc.n_free and len(choices) == sc.n_free
                and len(free) == sc.n_free)
    if rec.get("complete") is not complete:
        bad(BREAK, "complete disagrees with the rounds, lines and reads")
    return out


def verify_and_mark(rec: dict, **kw) -> list[str]:
    """verify_session, then ``rec["verified"] = (problems == [])``; returns the problems."""
    problems = verify_session(rec, **kw)
    rec["verified"] = not problems
    return problems


def _selftest(chk) -> None:
    import copy

    from . import testing

    pool, renders = sc_mod.pool_and_renders()
    ss = testing.f3_kit().ban_strings
    suite = testing.suite()

    def v(r, cell=None):
        return verify_session(r, pool=pool, renders=renders, scaffold_strings=ss,
                              schedule_cell=testing.case_cell(r["template"], r["s"]) if cell is None else cell)

    probs = {c.name: v(r) for c, r, _ in suite}
    chk(f"mf3.verify: every scripted F3 record ({len(suite)}) verifies -- clean, excluded, line-ended, "
        "hair-stopped", all(p == [] for p in probs.values()), {k: p[:1] for k, p in probs.items() if p})
    base = next(r for c, r, _ in suite if c.name == "f3 clean A2 start 0")
    lined = next(r for c, r, _ in suite if c.name.startswith("f3 reasoning line 3"))

    def mut(r, fn):
        x = copy.deepcopy(r)
        fn(x)
        return x

    def tamper_line_text(x):
        x["reasoning"][1]["text"] += " extra"

    def tamper_transcript(x):
        x["transcript"] = x["transcript"].replace("Reasoning (one line):", "Reasoning (one line) :", 1)

    def tamper_seed(x):
        x["reasoning"][0]["seed"] += 1

    def tamper_classes(x):
        x["reasoning"][0]["audit"] = {"classes": ["empty"], "echo_line": None, "scaffold": [], "defect": True}

    def tamper_menu(x):
        x["choices"][0]["menu_a"], x["choices"][0]["menu_b"] = x["choices"][0]["menu_b"], x["choices"][0]["menu_a"]

    def tamper_role(x):
        x["template"], x["contrast"] = "A2s", False

    def tamper_cap(x):
        x["reasoning_cap"] = 120

    def tamper_exclusion(x):
        x["exclusion"]["ci"] = 0

    def drop_line(x):
        x["reasoning"].pop()
        x["pieces"] = [p for p in x["pieces"] if not (p["kind"].startswith("reasoning") and p["idx"] == 5)]

    cases = {"line text": (base, tamper_line_text, BREAK), "harness bytes": (base, tamper_transcript, BREAK),
             "line seed": (base, tamper_seed, MISMATCH), "line classes": (base, tamper_classes, BREAK),
             "menu order": (base, tamper_menu, MISMATCH), "role on a shared banner": (base, tamper_role, MISMATCH),
             "cap": (base, tamper_cap, MISMATCH), "line-1 exclusion claimed": (lined, tamper_exclusion, BREAK),
             "a line dropped": (base, drop_line, BREAK)}
    got = {}
    for nm, (r, fn, tag) in cases.items():
        p = v(mut(r, fn), cell=testing.case_cell(r["template"], r["s"]))
        got[nm] = bool(p) and any(x.startswith(tag) for x in p)
    chk("mf3.verify: G-VER fires on a tampered line text, harness byte, line seed, line class, menu order, a "
        "contrast record relabelled sham on its shared banner, the cap, a line exclusion's ci, a dropped line",
        all(got.values()), got)
    other = testing.case_cell("A2", 1)
    chk("mf3.verify: a cell other than the committed one is schedule_mismatch, at once",
        v(base, cell=other) == [f"{MISMATCH}: the session's cell differs from the committed schedule's"])
    junk = verify_session({"schema": "x"}, pool=pool, renders=renders, schedule_cell={}, scaffold_strings=ss)
    chk("mf3.verify: a malformed record is template_breakage, never a traceback",
        junk and junk[0].startswith(BREAK))
    r2 = copy.deepcopy(base)
    p2 = verify_and_mark(r2, pool=pool, renders=renders, schedule_cell=testing.case_cell("A2", 0),
                         scaffold_strings=ss)
    chk("mf3.verify: verify_and_mark sets verified exactly True on a clean record", p2 == [] and r2["verified"] is True)
