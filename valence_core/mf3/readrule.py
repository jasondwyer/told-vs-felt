"""Q-F3's pre-VERDICTS read rule, printed reasons and pick-free stage report (PROPOSAL-m v1.11 §2.6
m:263; §3 m:271; §3.2 m:293, m:297; §4 m:318; the design seat's prebuild answers of 2026-11-06, Q5).

The blinding semantics are ``valence_core.m.readrule``'s, imported unchanged (the printed classes and
forms, the withheld-field sets, the label scan, the header redaction, the round counts); m's record
checks refuse Q-F3 (``keys.templates``) and know no reasoning piece, so the F3 forms are here:

- ``strip_contrast`` (m:271): banner + forced rounds and responses only; every reasoning line goes with
  the free phase (they are not "the banner, the forced rounds and their responses"). At G-TIME-F3 the
  ruling-(h) form (m's TIME_ROUND_KEEP) plus, per the seat's Q5, the per-line cap booleans.
- ``redact_sham`` (m:271): menus removed, the chosen tag ``[config]`` in free headers, and -- m's PIN
  for free responses, carried -- both own-pair labels redacted in free responses and in every
  reasoning line.
- ``printed_reason`` / ``session_line`` (m:263, m:318): class and phase; a contrast session's free
  event by phase alone (``excluded@free``) and, at G-TIME-F3, its forced event too (``excluded@forced``,
  ruling (h)); a reasoning-line exclusion prints ``scaffold@reasoning``, and as a free event
  (``excluded@free``) for a contrast session's line after its first pick and for every contrast line at
  G-TIME-F3 (ruling (h): no class -- a reasoning-line exclusion is the scaffold class, so its phase
  would name it).
- ``stage_report`` (m:271, m:293, m:297): sham templates in full, with their reasoning lines by class;
  contrast templates by forced-round counts and their first reasoning lines (pre-pick) by class, later
  lines withheld with the free rounds; at G-TIME-F3 ruling (h)'s counts plus the per-line cap booleans
  (Q5: "What m:271 withholds is content, not counts").
"""
from __future__ import annotations

import copy
import re
from fractions import Fraction
from typing import Any, Iterable, Mapping

from valence_core.m import readrule as m_rr

from . import banner, keys, lines
from . import scaffold as sc_mod

STAGES = keys.STAGES
PHASES = ("forced", "free", "reasoning")
TIME_STAGE = "time"
PRINT_CLASS = {**m_rr.PRINT_CLASS, "scaffold": "scaffold"}
CONTRAST_FREE = m_rr.CONTRAST_FREE
CONTRAST_FORCED_TIME = m_rr.CONTRAST_FORCED_TIME
REDACTED_TAG = m_rr.REDACTED_TAG
WITHHELD = m_rr.WITHHELD
_CLASS_RX = r"(?:audit|echo|content|lexical)"
_PRINTED_RX = re.compile(rf"{_CLASS_RX}@(?:forced|free)|scaffold@reasoning|excluded@(?:forced|free)")
_T = "|".join(keys.TEMPLATES)
_C = "|".join(keys.CONTRAST)
_S = "|".join(keys.SHAM)
# PIN (Code, declared at LOCK-m-F3 v0.1; m's _LINE_RX PIN carried to F3): the declared session-line
# forms. G-TIME contrast: valid, or excluded@forced / excluded@free (ruling (h)). Every other stage's
# contrast: valid, {class}@forced, scaffold@reasoning (line 1, pre-pick) or excluded@free. Sham at
# every stage: valid, {class}@{forced|free} or scaffold@reasoning.
_LINE_RX = re.compile(
    rf"(?:time (?:{_C}) s=\d+ (?:valid|excluded:excluded@(?:forced|free))"
    rf"|(?:id|qual|campaign) (?:{_C}) s=\d+ (?:valid|excluded:(?:{_CLASS_RX}@forced|scaffold@reasoning|excluded@free))"
    rf"|(?:{'|'.join(STAGES)}) (?:{_S}) s=\d+ (?:valid|excluded:(?:{_CLASS_RX}@(?:forced|free)|scaffold@reasoning)))")
_FREE_ONLY_KEYS = m_rr._FREE_ONLY_KEYS | {"reasoning"}
_STRIP_TOP = ("schema", "format", "substrate", "unit", "stage", "template", "contrast", "s", "j", "keys",
              "cell", "banner", "note_lines", "path", "reasoning_cap", "domain", "verified")
_REDACT_TOP = _STRIP_TOP + ("excluded", "complete", "seconds")
_LINE_KEEP = ("ci", "n", "cap", "text", "n_tok", "cap_hit", "stop_reason", "audit")


# --- checks ------------------------------------------------------------------------------
def _check_header(rec: Any) -> None:
    if not isinstance(rec, Mapping):
        raise TypeError("a session record is a dict")
    if rec.get("schema") != sc_mod.SCHEMA or rec.get("format") != sc_mod.FORMAT:
        raise ValueError("not an F3 m-session-v1 record")
    if "blinding" in rec:
        raise ValueError("record is already a blinded form; this needs the checkpoint record")
    if rec.get("unit") != keys.UNIT or rec.get("substrate") != "qwen":
        raise ValueError("an F3 record is Q-F3's, on Qwen")
    t = rec.get("template")
    if t not in keys.TEMPLATES:
        raise ValueError(f"template {t!r} is not a Q-F3 template")
    c = rec.get("contrast")
    if not isinstance(c, bool) or c != keys.is_contrast(t):
        raise ValueError(f"contrast flag disagrees with template {t!r}")


def _check_pieces(rec: Mapping) -> None:
    """Pieces tile the transcript in F3's group order; every piece's bytes are its field's."""
    t, ps = rec.get("transcript"), rec.get("pieces")
    if not isinstance(t, str) or not isinstance(ps, list) or not ps:
        raise ValueError("record carries no transcript / pieces")
    pos = 0
    for p in ps:
        a, b = p.get("start"), p.get("end")
        if type(a) is not int or type(b) is not int or a != pos or b < a:
            raise ValueError(f"pieces do not tile the transcript (at a {p.get('kind')!r} piece)")
        pos = b
    if pos != len(t) or ps[0].get("kind") != "banner" or t[:ps[0]["end"]] != rec.get("banner"):
        raise ValueError("pieces do not cover the transcript, or the first is not the banner")
    pair = m_rr._cell_pair(rec)
    rounds = {(r.get("phase"), m_rr._ridx(r)): r for r in rec.get("rounds") or []}
    choices = {c["ci"]: c for c in rec.get("choices") or []}
    rlines = {x["ci"]: x for x in rec.get("reasoning") or []}
    groups: list[tuple[tuple[str, int], list]] = []
    for p in ps[1:]:
        kind, ph, ix = p.get("kind"), p.get("phase"), p.get("idx")
        if kind not in sc_mod.PIECE_KINDS or kind == "banner" or ph not in ("forced", "free") or type(ix) is not int:
            raise ValueError(f"piece kind {kind!r} / phase {ph!r} not allowed after the banner")
        if groups and groups[-1][0] == (ph, ix):
            groups[-1][1].append(p)
        else:
            groups.append(((ph, ix), [p]))
    want = {"forced": 0, "free": 0}
    seen_free = False
    for gi, ((ph, ix), gp) in enumerate(groups):
        if ph == "forced" and seen_free:
            raise ValueError("a forced round follows a free group in the pieces")
        seen_free = seen_free or ph == "free"
        if ix != want[ph]:
            raise ValueError(f"{ph} groups out of order in the pieces")
        want[ph] += 1
        kinds = tuple(p["kind"] for p in gp)
        last = gi == len(groups) - 1
        if ph == "forced":
            ok = kinds == sc_mod.FORCED_GROUP
        else:
            # PIN (Code, declared at LOCK-m-F3 v0.1): a free group is FREE_GROUP; only the last may be the
            # reasoning block alone, and only where the session ended at that line (its scaffold fire).
            ok = kinds == sc_mod.FREE_GROUP or (
                last and kinds == sc_mod.F3_PIECE_KINDS and (rec.get("exclusion") or {}).get("phase") == "reasoning"
                and (rec.get("exclusion") or {}).get("ci") == ix)
        if not ok:
            raise ValueError(f"{ph} group pieces are not F3's layout")
        if "round" in kinds and (ph, ix) not in rounds:
            raise ValueError(f"a {ph} round in the pieces has no round record")
        for p in gp:
            frag, kind = t[p["start"]:p["end"]], p["kind"]
            if kind == "reasoning":
                x = rlines.get(ix)
                if x is None or frag != banner.reasoning_block(sc_mod.N_FORCED + 1 + ix):
                    raise ValueError("a reasoning piece is not the block at its n (or has no line record)")
            elif kind == "reasoning_text":
                if frag != rlines[ix].get("text"):
                    raise ValueError("a reasoning-line piece differs from the line's recorded text")
            elif kind in ("reasoning_joiner", "joiner"):
                if frag != "\n":
                    raise ValueError(f"a {kind} piece is not a newline")
            elif kind == "menu":
                ch = choices.get(ix)
                if ch is None or frag != ch.get("menu") or ch.get("pick") not in pair:
                    raise ValueError("a menu piece differs from its choice's menu")
            elif kind == "pick":
                if frag != f" {choices[ix]['pick']}\n":
                    raise ValueError("a pick piece differs from the choice's recorded pick")
            elif kind == "round":
                r = rounds[(ph, ix)]
                tag = choices[ix]["pick"] if ph == "free" else r.get("label")
                if ph == "free" and r.get("label", tag) != tag:
                    raise ValueError("a free round's label disagrees with its choice's pick")
                header = frag.partition("\n")[0]
                if not frag.startswith("[round ") or not frag.endswith("Response:") or not header.endswith(f": {tag}]"):
                    raise ValueError(f"a {ph} round header is not a round template filled with its tag")
            elif kind == "generation":
                if frag != rounds[(ph, ix)].get("text"):
                    raise ValueError(f"a {ph} generation piece differs from the round's recorded text")
    if len(rounds) != sum("round" in [p["kind"] for p in gp] for _, gp in groups):
        raise ValueError("a recorded round has no pieces")
    if set(rlines) != set(range(want["free"])) or set(choices) != {ix for (ph, ix), gp in groups
                                                                  if ph == "free" and len(gp) > 3}:
        raise ValueError("record lines / choices do not match its free groups")


def _check_record(rec: Any) -> None:
    _check_header(rec)
    _check_pieces(rec)


# --- blinded forms ---------------------------------------------------------------------------
def _line_caps(rec: Mapping) -> list[bool]:
    return [bool(x["cap_hit"]) for x in rec.get("reasoning") or []]


def strip_contrast(rec: Mapping) -> dict:
    """m:271: a contrast session as banner + forced rounds and responses only (at G-TIME-F3, ruling
    (h)'s form plus the per-line cap booleans of the seat's Q5)."""
    _check_record(rec)
    if not rec["contrast"]:
        raise ValueError("strip_contrast is the contrast-template read; a sham session is read through redact_sham")
    kept = [p for p in rec["pieces"] if p["kind"] == "banner" or p["phase"] == "forced"]
    cut = kept[-1]["end"]
    forced = [r for r in rec["rounds"] if r["phase"] == "forced"]
    exc = rec.get("exclusion")
    if rec.get("stage") == TIME_STAGE:
        tout: dict = {k: copy.deepcopy(rec.get(k)) for k in _STRIP_TOP if k != "domain"}
        tout["rounds"] = [{k: copy.deepcopy(r[k]) for k in m_rr.TIME_ROUND_KEEP if k in r} for r in forced]
        tout["pieces"] = [copy.deepcopy(p) for p in kept]
        tout["transcript"] = rec["transcript"][:cut]
        tout["n_forced_rounds"] = len(forced)
        tout["excluded_at_forced"] = bool(exc) and exc.get("phase") == "forced"
        # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q5): the contrast session's per-line cap
        # booleans, in line order -- no line text, class or pick. Disclosed, as ruling (h)'s two counts
        # were: the list's length is the number of reasoning lines generated, which locates where a
        # free-phase end fell (Q5: "What m:271 withholds is content, not counts").
        tout["reasoning_cap_reached"] = _line_caps(rec)
        tout["blinding"] = ("contrast-stripped at G-TIME-F3: banner + forced-round bytes, {phase, ri, n, text} per "
                            "round, per-line cap booleans, no class field (m:271; ruling (h); the seat's Q5)")
        m_rr._assert_withheld(tout, _FREE_ONLY_KEYS | {"ci"} | m_rr.TIME_WITHHELD, True, "strip_contrast")
        return tout
    out: dict = {k: copy.deepcopy(rec.get(k)) for k in _STRIP_TOP}
    out["rounds"] = [copy.deepcopy(r) for r in forced]
    out["pieces"] = [copy.deepcopy(p) for p in kept]
    out["transcript"] = rec["transcript"][:cut]
    out["n_forced_rounds"] = len(forced)
    st = rec.get("strict_exclusion")
    out["exclusion"] = copy.deepcopy(exc) if exc and exc.get("phase") == "forced" else None
    out["excluded_at_forced"] = out["exclusion"] is not None
    out["strict_exclusion"] = copy.deepcopy(st) if st and st.get("phase") == "forced" else None
    # PIN (Code, declared at LOCK-m-F3 v0.1): m's PIN carried -- a free-phase hair trigger is withheld here
    # and from stage_report, and so is a reasoning-line one (the stage announces the STOP itself).
    out["hair_triggers"] = [copy.deepcopy(h) for h in rec.get("hair_triggers") or [] if h.get("phase") == "forced"]
    out["blinding"] = "contrast-stripped: banner + forced rounds (m:271)"
    m_rr._assert_withheld(out, _FREE_ONLY_KEYS | {"ci"}, True, "strip_contrast")
    return out


def redact_sham(rec: Mapping) -> dict:
    """m:271: a sham session with menus removed, the chosen tag redacted from free headers, and both
    labels redacted in free responses and every reasoning line."""
    _check_record(rec)
    if rec["contrast"]:
        raise ValueError("redact_sham is the sham-template read; a contrast session is read through strip_contrast")
    pair = m_rr._cell_pair(rec)
    lab_rx = m_rr._labels_rx(pair)
    picks = {c["ci"]: c["pick"] for c in rec.get("choices") or []}
    t = rec["transcript"]
    parts, pieces = [], []
    free_text: dict[int, str] = {}
    line_text: dict[int, str] = {}
    pos = 0
    for p in rec["pieces"]:
        if p["kind"] in ("menu", "pick"):
            continue
        frag = t[p["start"]:p["end"]]
        if p["kind"] != "banner" and p["phase"] == "free":
            if p["kind"] == "round":
                frag = m_rr._redact_header(frag, picks[p["idx"]])
            elif p["kind"] == "generation":
                frag = lab_rx.sub(REDACTED_TAG, frag)
                free_text[p["idx"]] = frag
            elif p["kind"] == "reasoning_text":
                # PIN (Code, declared at LOCK-m-F3 v0.1): m's PIN for free responses carried to the
                # reasoning lines -- both own-pair labels go to [config] at the lexical word boundary,
                # case-insensitive, in every line (a line after a pick may name the picked label).
                frag = lab_rx.sub(REDACTED_TAG, frag)
                line_text[p["idx"]] = frag
        q = copy.deepcopy(p)
        q["start"], q["end"] = pos, pos + len(frag)
        pieces.append(q)
        parts.append(frag)
        pos += len(frag)
    transcript = "".join(parts)
    for q in pieces:
        if q["kind"] != "banner" and q["phase"] == "free" and lab_rx.search(transcript[q["start"]:q["end"]]):
            raise ValueError(f"redact_sham: an own-pair label survives in a free {q['kind']} piece; refused")
    out: dict = {k: copy.deepcopy(rec.get(k)) for k in _REDACT_TOP}
    rounds = []
    for r in rec["rounds"]:
        if r["phase"] == "forced":
            rounds.append(copy.deepcopy(r))
            continue
        fr = {k: copy.deepcopy(r[k]) for k in m_rr._FREE_ROUND_KEEP if k in r}
        fr["text"] = free_text[r["ci"]]
        a = r.get("audit")
        fr["audit"] = None if a is None else {k: copy.deepcopy(a[k]) for k in m_rr._AUDIT_KEEP if k in a}
        rounds.append(fr)
    out["rounds"] = rounds
    out["reasoning_lines"] = [{**{k: copy.deepcopy(x[k]) for k in _LINE_KEEP if k in x}, "text": line_text[x["ci"]]}
                              for x in rec.get("reasoning") or []]
    out["pieces"] = pieces
    out["transcript"] = transcript
    exc, st = rec.get("exclusion"), rec.get("strict_exclusion")
    if exc:
        out["exclusion"] = {k: exc[k] for k in ("class", "phase", "ci") if k in exc}
        if exc["phase"] == "forced" and "detail" in exc:
            out["exclusion"]["detail"] = copy.deepcopy(exc["detail"])
    else:
        out["exclusion"] = None
    out["strict_exclusion"] = {"class": st["class"], "phase": st["phase"]} if st else None
    out["hair_triggers"] = [{k: h[k] for k in ("name", "phase", "ci") if k in h} if h.get("phase") != "forced"
                            else copy.deepcopy(h) for h in rec.get("hair_triggers") or []]
    out["blinding"] = "sham-redacted: menus removed, chosen tag and labels [config] (m:271)"
    m_rr._assert_withheld(out, m_rr._FREE_ONLY_KEYS, False, "redact_sham")
    return out


# --- printing ------------------------------------------------------------------------------
def printed_reason(rec_or_exclusion: Any, contrast: bool, *, stage: str | None = None) -> str:
    """m:263's printed form for an F3 exclusion: ``{class}@{phase}``; a contrast session's free event
    (a reasoning line after the first pick included) by phase alone; at G-TIME-F3 every contrast event
    by phase alone (ruling (h))."""
    if not isinstance(contrast, bool):
        raise TypeError("contrast must be a bool")
    obj = rec_or_exclusion
    if isinstance(obj, Mapping) and "schema" in obj:
        _check_header(obj)
        if obj["contrast"] is not contrast:
            raise ValueError("printed_reason: contrast argument disagrees with the record")
        rstage = obj.get("stage")
        if stage is not None and stage != rstage:
            raise ValueError("printed_reason: stage argument disagrees with the record")
        stage = rstage
        if obj.get("excluded") is not True or not obj.get("exclusion"):
            raise ValueError("printed_reason: the session is not excluded")
        obj = obj["exclusion"]
    if not isinstance(obj, Mapping) or "class" not in obj:
        raise TypeError("printed_reason takes an F3 record or an exclusion dict")
    if stage is not None and stage not in STAGES:
        raise ValueError("printed_reason: unknown stage")
    cls, phase = obj.get("class"), obj.get("phase")
    if phase not in PHASES or cls not in PRINT_CLASS:
        raise ValueError("printed_reason: unknown class or phase")
    if (phase == "reasoning") != (cls == "scaffold"):
        raise ValueError("printed_reason: a reasoning-line exclusion is the scaffold class, and only it")
    ci = obj.get("ci")
    if phase == "reasoning" and type(ci) is not int:
        raise ValueError("printed_reason: a reasoning-line exclusion carries its ci")
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:263, m:271, ruling (h); the build review's finding 3): a
    # contrast session's reasoning-line exclusion after its first pick (ci >= 1) is a free-phase event and
    # prints excluded@free; on line 1 it is pre-pick and prints scaffold@reasoning. At G-TIME-F3 every
    # contrast reasoning-line exclusion prints excluded@free: ruling (h) prints no class, and the scaffold
    # class is the only one a reasoning line can be excluded for, so "@reasoning" would name it.
    if contrast and stage == TIME_STAGE:
        out = {"forced": CONTRAST_FORCED_TIME, "free": CONTRAST_FREE, "reasoning": CONTRAST_FREE}[phase]
    elif contrast and (phase == "free" or (phase == "reasoning" and ci >= 1)):
        out = CONTRAST_FREE
    else:
        out = f"{PRINT_CLASS[cls]}@{phase}"
    if not _PRINTED_RX.fullmatch(out):
        raise AssertionError("printed_reason produced an undeclared form")
    return out


def session_line(rec: Mapping) -> str:
    """m:318: the one stdout line per session -- stage, template, s, validity / reason."""
    _check_header(rec)
    stage, s = rec.get("stage"), rec.get("s")
    if stage not in STAGES or type(s) is not int or s < 0:
        raise ValueError("session_line: unknown stage or bad s")
    if rec.get("excluded") is True:
        status = "excluded:" + printed_reason(rec, rec["contrast"])
    elif rec.get("excluded") is False and not rec.get("exclusion"):
        status = "valid"
    else:
        raise ValueError("session_line: excluded flag and exclusion record disagree")
    line = f"{stage} {rec['template']} s={s} {status}"
    if not _LINE_RX.fullmatch(line):
        raise AssertionError("session_line produced an undeclared form")
    return line


# --- the stage report ----------------------------------------------------------------------
def _domain(rec: Mapping) -> bool:
    """m:308 for F3 from pre-pick material alone; cross-checked against the record."""
    forced = [r for r in rec["rounds"] if r["phase"] == "forced"]
    pre = sc_mod.prepick_excluded(rec) or any(
        h.get("phase") == "forced" or (h.get("phase") == "reasoning" and h.get("ci") == 0)
        for h in rec.get("hair_triggers") or [])
    d = (len(forced) == sc_mod.N_FORCED and not pre
         and all((r.get("audit") or {}).get("claim") is None for r in forced))
    if bool(rec.get("domain")) is not d:
        raise ValueError("stage_report: a record's domain field disagrees with its pre-pick material")
    return d


def line_counts(rs: Iterable[Mapping]) -> dict:
    """Reasoning lines generated, defect lines (the union, once per line) and lines per class."""
    ls = [x for r in rs for x in r.get("reasoning") or []]
    by = {c: sum(c in x["audit"]["classes"] for x in ls) for c in lines.CLASSES}
    return {"lines": len(ls), "defect_lines": sum(bool(x["audit"]["classes"]) for x in ls), "by_class": by,
            "cap_reached": sum(bool(x["cap_hit"]) for x in ls)}


def _hair(rec: Mapping, *, include_free: bool) -> list[dict]:
    """A session's hair triggers; without include_free only the pre-pick ones (forced rounds and line 1)."""
    return [{"name": h["name"], "phase": h.get("phase")} for h in rec.get("hair_triggers") or []
            if include_free or h.get("phase") == "forced" or (h.get("phase") == "reasoning" and h.get("ci") == 0)]


def _sham_block(rs: list[Mapping]) -> dict:
    allr = [r for rec in rs for r in rec["rounds"]]
    reasons = {f"{m_rr.PRINT_CLASS[c]}@{ph}": 0 for ph in ("forced", "free") for c in m_rr.CLAIMS["qwen"]}
    reasons["scaffold@reasoning"] = 0
    strict = {f"{m_rr.PRINT_CLASS[c]}@{ph}": 0 for ph in ("forced", "free") for c in m_rr.CLAIMS["qwen"]}
    valid = domain = complete = audit_sessions = 0
    fp_k = fp_n = reads = low = top1 = 0
    by_pair: dict[str, dict] = {}
    hair: list[dict] = []
    for rec in rs:
        if rec.get("excluded") is True:
            reasons[printed_reason(rec, False)] += 1
        elif rec.get("excluded") is False and not rec.get("exclusion"):
            valid += 1
        else:
            raise ValueError("stage_report: excluded flag and exclusion record disagree")
        st = rec.get("strict_exclusion")
        if st:
            strict[f"{m_rr.PRINT_CLASS[st['class']]}@{st['phase']}"] += 1
        d = _domain(rec)
        ch = rec.get("choices") or []
        fp = rec.get("first_free_pick_P")
        if d:
            if not isinstance(fp, bool) or not ch or fp is not (ch[0]["pick"] == rec["cell"]["P"]):
                raise ValueError("stage_report: first_free_pick_P disagrees with the first choice")
            domain += 1
            fp_n += 1
            fp_k += int(fp)
            cell = by_pair.setdefault(str(int(rec["cell"]["pair_index"])), {"k": 0, "n": 0})
            cell["k"] += int(fp)
            cell["n"] += 1
        elif fp is not None:
            raise ValueError("stage_report: a non-domain session carries a first pick")
        reads += len(ch)
        low += sum(int(bool(c.get("low_label_mass"))) for c in ch)
        top1 += sum(int(bool(c.get("top1_not_label"))) for c in ch)
        complete += int(bool(rec.get("complete")))
        audit_sessions += int(any((r.get("audit") or {}).get("claim") == "v2" for r in rec["rounds"]))
        hair += _hair(rec, include_free=True)

    def share(k, n):
        return str(Fraction(k, n)) if n else None

    return {"contrast": False, "sessions": len(rs), "valid_sessions": valid, "excluded_sessions": reasons,
            "strict_excluded_sessions": strict, "domain_sessions": domain, "complete_sessions": complete,
            "forced": m_rr._round_counts([r for r in allr if r["phase"] == "forced"], "qwen"),
            "free": m_rr._round_counts([r for r in allr if r["phase"] == "free"], "qwen"),
            "all": m_rr._round_counts(allr, "qwen"), "audit_sessions": audit_sessions,
            "reasoning_lines": line_counts(rs),
            "reads": {"n": reads, "low_label_mass": low, "top1_not_label": top1},
            "first_pick_P": {"k": fp_k, "n": fp_n, "share": share(fp_k, fp_n)},
            "first_pick_P_by_pair": {p: {**v, "share": share(v["k"], v["n"])} for p, v in sorted(by_pair.items())},
            "hair_triggers": sorted(hair, key=lambda h: (h["name"], str(h["phase"])))}


def _contrast_block(rs: list[Mapping]) -> dict:
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:297 "contrast sessions reported beside", m:271; the build review's
    # finding 12): beside its forced-round counts a contrast template reports its sessions' FIRST reasoning lines
    # -- generated before any menu, so pick-free (m:308's domain reaches "up to and including the first
    # reasoning line"; Q8 puts a line's scaffold fire in the guard's pre-pick count) -- by class, with
    # line-1 exclusions (scaffold@reasoning) and hair triggers; every later line is a free-phase event, withheld
    # to VERDICTS with the free rounds (m:271). G-TIME-F3 keeps the seat's Q5 form (_contrast_block_time).
    forced = [r for rec in rs for r in rec["rounds"] if r["phase"] == "forced"]
    excl = {f"{m_rr.PRINT_CLASS[c]}@forced": 0 for c in m_rr.CLAIMS["qwen"]}
    excl_l1 = 0
    audit_sessions = domain = 0
    hair: list[dict] = []
    for rec in rs:
        e = rec.get("exclusion")
        if e and e.get("phase") == "forced":
            excl[printed_reason(e, True)] += 1
        elif e and e.get("phase") == "reasoning" and e.get("ci") == 0:
            excl_l1 += 1
        audit_sessions += int(any((r.get("audit") or {}).get("claim") == "v2" for r in rec["rounds"]
                                  if r["phase"] == "forced"))
        domain += int(_domain(rec))
        hair += _hair(rec, include_free=False)
    line1 = [{"reasoning": [x for x in rec.get("reasoning") or [] if x["ci"] == 0]} for rec in rs]
    return {"contrast": True, "sessions": len(rs), "forced": m_rr._round_counts(forced, "qwen"),
            "audit_sessions_forced": audit_sessions, "excluded_at_forced": excl,
            "sessions_excluded_at_forced": sum(excl.values()), "reasoning_line_1": line_counts(line1),
            "sessions_excluded_at_line_1": excl_l1, "domain_sessions": domain,
            "hair_triggers": sorted(hair, key=lambda h: (h["name"], str(h["phase"]))),
            "free_rounds": WITHHELD, "reasoning_lines_after_line_1": WITHHELD}


TIME_CONTRAST_KEYS = ("contrast", "sessions", "per_session", "free_rounds")
TIME_SESSION_KEYS = ("s", "forced_rounds_generated", "excluded_at_forced", "reasoning_cap_reached")


def _contrast_block_time(rs: list[Mapping]) -> dict:
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's ruling (h) carried, and Q5): at G-TIME-F3 a
    # contrast session is reported as {s, forced rounds generated, excluded at forced yes/no, its per-line
    # cap booleans}; no class, no claim count, no line text, no pick; its free-round events withheld.
    per = []
    for rec in rs:
        _domain(rec)
        e = rec.get("exclusion")
        per.append({"s": rec["s"],
                    "forced_rounds_generated": sum(1 for r in rec["rounds"] if r["phase"] == "forced"),
                    "excluded_at_forced": bool(e) and e.get("phase") == "forced",
                    "reasoning_cap_reached": _line_caps(rec)})
    out = {"contrast": True, "sessions": len(rs), "per_session": per, "free_rounds": WITHHELD}
    if tuple(out) != TIME_CONTRAST_KEYS or any(tuple(p) != TIME_SESSION_KEYS for p in per):
        raise AssertionError("stage_report: the G-TIME-F3 contrast block is not its declared form")
    return out


def stage_report(records: Iterable[Mapping]) -> dict:
    """m:271's pick-free report of one Q-F3 stage, per template in §2.4's order."""
    recs = list(records)
    if not recs:
        raise ValueError("stage_report: no records")
    for r in recs:
        _check_record(r)
    if len({r["stage"] for r in recs}) != 1:
        raise ValueError("stage_report: one stage per report")
    ids = [(r["template"], r["s"]) for r in recs]
    if len(set(ids)) != len(ids):
        raise ValueError("stage_report: duplicate (template, s) records")
    stage = recs[0]["stage"]
    out: dict = {"unit": keys.UNIT, "stage": stage, "substrate": "qwen",
                 "form": "pick-free stage report (m:271, m:318)", "templates": {}}
    for t in keys.TEMPLATES:
        rs = sorted((r for r in recs if r["template"] == t), key=lambda r: r["s"])
        if not rs:
            continue
        if not keys.is_contrast(t):
            out["templates"][t] = _sham_block(rs)
        elif stage == TIME_STAGE:
            out["templates"][t] = _contrast_block_time(rs)
        else:
            out["templates"][t] = _contrast_block(rs)
    m_rr._assert_no_label(out, {x for r in recs for x in r["cell"]["pair"]})
    return out


def release_full(records):
    """m:271: the full, unredacted release (VERDICTS or NOT-RUN). Returns ``records`` unchanged."""
    return records


def _selftest(chk) -> None:
    import json

    from . import testing

    suite = testing.suite()
    recs = [r for _, r, _ in suite]
    by = {c.name: r for c, r, _ in suite}
    ok = True
    for r in recs:
        try:
            _check_record(r)
        except ValueError:
            ok = False
    chk("mf3.readrule: every scripted F3 record passes the piece check (F3's group order; the reasoning-only "
        "last group where a line ended the session)", ok)
    con = [r for r in recs if r["contrast"]]
    sham = [r for r in recs if not r["contrast"]]
    stripped = [strip_contrast(r) for r in con]
    chk("mf3.readrule: stripped contrast reads carry the banner and forced rounds only -- no reasoning line, "
        "menu, pick or free round",
        all("| reasoning]" not in x["transcript"] and "| choice]" not in x["transcript"] and "reasoning" not in x
            and x["transcript"] == r["transcript"][:len(x["transcript"])] for x, r in zip(stripped, con)))
    red = [redact_sham(r) for r in sham]
    labels = {w for r in sham for w in r["cell"]["pair"]}
    chk("mf3.readrule: redacted sham reads -- menus gone, chosen tags [config], no label in any free piece or "
        "reasoning line; reasoning lines kept",
        all("| choice]" not in x["transcript"] and all(not re.search(rf"\b{w}\b", ln["text"], re.I)
                                                       for ln in x["reasoning_lines"] for w in labels)
            for x in red)
        and any(REDACTED_TAG in ln["text"] for x in red for ln in x["reasoning_lines"]))
    l1 = by["f3 reasoning line 1 scaffold: excluded pre-pick, no read"]          # A3 contrast
    l3 = by["f3 reasoning line 3 scaffold: excluded after two reads, domain kept"]  # A2s sham
    lex = by["f3 free lexical ends after its round"]                              # A3s sham
    chk("mf3.readrule: printed reasons -- a contrast line-1 scaffold prints scaffold@reasoning, and excluded@free "
        "at G-TIME-F3 (no class, ruling (h)); a contrast later line prints excluded@free at every stage; a sham line "
        "prints scaffold@reasoning; a sham free lexical prints lexical@free",
        printed_reason(l1, True) == "scaffold@reasoning"
        and printed_reason(l1["exclusion"], True, stage="time") == "excluded@free"
        and printed_reason({"class": "scaffold", "phase": "reasoning", "ci": 2}, True, stage="time") == "excluded@free"
        and printed_reason({"class": "scaffold", "phase": "reasoning", "ci": 2}, True) == "excluded@free"
        and printed_reason(l3, False) == "scaffold@reasoning" and printed_reason(lex, False) == "lexical@free")
    lines_out = [session_line(r) for r in recs]
    chk("mf3.readrule: session lines are declared forms and carry no label, pick or free index",
        all(_LINE_RX.fullmatch(x) for x in lines_out)
        and not any(re.search(rf"\b{w}\b", x) for x in lines_out for w in labels | {w for r in con for w in r["cell"]["pair"]}),
        lines_out[:3])
    rep = stage_report(list({(r["template"], r["s"]): r for r in recs}.values()))
    js = json.dumps(rep)
    chk("mf3.readrule: the stage report covers the six templates; sham blocks carry reasoning-line counts by "
        "class; contrast blocks are forced-round counts and line 1's classes and exclusions (pre-pick), free rounds "
        "and later lines withheld; no label anywhere",
        set(rep["templates"]) == set(keys.TEMPLATES)
        and rep["templates"]["A1s"]["reasoning_lines"]["by_class"] == {"empty": 2, "cap_no_newline": 3, "echo": 1}
        and rep["templates"]["A1"]["free_rounds"] == WITHHELD and "reasoning_lines" not in rep["templates"]["A3"]
        and rep["templates"]["A3"]["reasoning_line_1"]["lines"] == len([r for r in recs if r["template"] == "A3"
                                                                        and r.get("reasoning")])
        and rep["templates"]["A3"]["sessions_excluded_at_line_1"] == 1
        and rep["templates"]["A3"]["reasoning_lines_after_line_1"] == WITHHELD
        and "granite" not in js)
    trec = []
    for c in testing.CASES[:12]:
        r, _ = testing.run_case(c, stage="time", s=0, cell=__import__("valence_core.mf3.schedule", fromlist=["x"])
                                .gate_schedule("time", c.template, 1)[0])
        trec.append(r)
    trec = list({r["template"]: r for r in trec}.values())
    trep = stage_report(trec)
    blk = trep["templates"]["A2"]
    chk("mf3.readrule: at G-TIME-F3 a contrast block is ruling (h)'s counts plus the per-line cap booleans (Q5)",
        tuple(blk) == TIME_CONTRAST_KEYS and tuple(blk["per_session"][0]) == TIME_SESSION_KEYS
        and blk["per_session"][0]["reasoning_cap_reached"] == [False] * 6)
    ts = strip_contrast(next(r for r in trec if r["template"] == "A3"))
    chk("mf3.readrule: the G-TIME-F3 strip keeps {phase, ri, n, text} per forced round and the cap booleans",
        all(set(x) <= {"phase", "ri", "n", "text"} for x in ts["rounds"]) and ts["reasoning_cap_reached"] == [False] * 6)
    refused = []
    for fn in (lambda: strip_contrast(sham[0]), lambda: redact_sham(con[0]),
               lambda: printed_reason({"class": "lexical", "phase": "reasoning", "ci": 0}, False),
               lambda: printed_reason({"class": "scaffold", "phase": "reasoning"}, False),
               lambda: stage_report([])):
        try:
            fn()
            refused.append(False)
        except (ValueError, TypeError):
            refused.append(True)
    bad = json.loads(json.dumps(con[0]))
    bad["pieces"] = [p for p in bad["pieces"] if p["kind"] != "reasoning_joiner"]
    try:
        _check_record(bad)
        refused.append(False)
    except ValueError:
        refused.append(True)
    chk("mf3.readrule: refuses a sham to strip, a contrast to redact, a non-scaffold reasoning class, a line "
        "exclusion without ci, an empty report, a record missing a reasoning piece", all(refused), refused)
