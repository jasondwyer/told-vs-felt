"""PROPOSAL-m's pre-VERDICTS read rule, printed exclusion reasons and pick-free
stage report (v1.11 §2.6, §3, §4; m:263, m:271, m:280, m:283, m:302, m:318).

Every function here takes the m runners' session record (``m-session-v1``, the
step-4 build design §2) and returns something that may be read or printed
before the unit's VERDICTS entry:

- ``strip_contrast`` (m:271). A contrast-template session as the seat reads it
  pre-VERDICTS: the banner, the forced rounds and their responses, nothing else.
  "A free round's task line is clean or corrupted by the pick, so it is the pick"
  (session_e2a.py:72-75), so every free round goes, and so does every
  structured field a free round fills: choices, reads, picks, free items and
  properties, free claims, free exclusion detail. Whole-session validity,
  completeness and seconds go too, because each one encodes the free-round
  exclusion position (maps/audit.md D15; build-design hard rule 5).
- ``redact_sham`` (m:271). A sham-template session with the menu blocks removed
  and the chosen config tag redacted from every free round's header. On OLMo the
  stored transcript carries no menu or pick line (b3's context rule,
  box_b3_sessions.py:202), so only the headers change there (maps/olmo.md §6
  item 16).
- ``printed_reason`` / ``session_line`` (m:263, m:318). These are the only
  printed forms. A reason is class and phase; a contrast session's free-round
  exclusion is the phase alone (``excluded@free``). Neither form ever carries a
  tag, a free round's index, the render or a pick. The session line carries no
  seconds, read count or completeness word.
- ``stage_report`` (m:271, m:280, m:283, m:302). Contrast-template sessions are
  reported by their forced-round counts only, and their free-round events --
  "exclusions, degeneracy, any class" -- are withheld to the unit's VERDICTS
  entry or NOT-RUN record. Sham-template sessions are reported in full by
  class, with the first-pick share (m:318 exception (2)).
- ``release_full`` (m:271's closing clause). The release at VERDICTS, at NOT-RUN,
  or at an OLMo checkpoint's PENDING closure. It returns the records unchanged;
  it exists so that a caller names the act.

Both blinded forms are whitelists: any record field not named here is withheld
by default. Before cutting, every function checks that the record's pieces
(char offsets into ``transcript``) tile it exactly and in the declared order,
so no cut can land inside a free round. Generations are located by their
recorded offsets and text, never by searching for "\\n" (maps/olmo.md §6
item 18). Error messages name a kind and a phase, never a label or a
free-round index.
"""
from __future__ import annotations

import copy
import json
import re
from fractions import Fraction
from typing import Any, Iterable, Iterator, Mapping

from valence_core.m import keys

SCHEMA = "m-session-v1"
SUBSTRATES = ("qwen", "olmo")
STAGES = ("campaign", "time", "id", "qual")
PHASES = ("forced", "free")
# Both substrates run 2F = 4 forced rounds (session_e2a's layout; b3's F = 2).
N_FORCED = 4
PIECE_KINDS = ("banner", "round", "generation", "joiner", "menu", "pick")
# Piece kinds per round, in transcript order. Qwen writes the menu and the pick
# line into the transcript (f1, f_sessions.py:358). OLMo writes neither (b3's
# context rule).
_GROUP_KINDS = {
    ("qwen", "forced"): ("round", "generation", "joiner"),
    ("qwen", "free"): ("menu", "pick", "round", "generation", "joiner"),
    ("olmo", "forced"): ("round", "generation", "joiner"),
    ("olmo", "free"): ("round", "generation", "joiner"),
}

# The claim classes per substrate, restated from the build design §1.7 (the
# source is valence_core.m.audit.RoundAudit; audit.py is written in parallel,
# so the names are replicated here rather than imported). Claiming order is
# m:261 / m:262.
CLAIMS = {"qwen": ("v2", "echo", "content", "lexical"),
          "olmo": ("audit", "echo", "lexical")}
DEGENERACY = {"qwen": ("v2", "echo"), "olmo": ("audit", "echo")}   # round_degeneracy numerator
AUDIT_CLASS = {"qwen": "v2", "olmo": "audit"}                      # audit_degenerate (m:314)

# m:263's printed classes. Qwen's v2 claim prints as "audit" (m:263's
# ``audit@forced``). An exclusion record whose Qwen class is written "audit"
# is accepted as the same class.
# PIN (Code, declared at LOCK v0.1): Qwen's v4 content claim prints as
# ``content@forced`` / ``content@free``. m:263 lists only audit/lexical/echo,
# but m:261 makes v4 content exclusion-bearing on forced rounds, and m:314
# counts it apart from audit_degenerate (flagged; maps/audit.md §4 item 5 and
# D6). The seat may fold it into "audit" instead.
PRINT_CLASS = {"v2": "audit", "audit": "audit", "echo": "echo",
               "content": "content", "lexical": "lexical"}
CONTRAST_FREE = "excluded@free"
# PIN (Code, declared at LOCK v0.1): the placeholder that replaces the chosen
# config tag in a sham free round's header (maps/olmo.md §7 item 15).
REDACTED_TAG = "[config]"
WITHHELD = "withheld to the unit's VERDICTS entry or NOT-RUN record (m:271)"
AUDIT_CATEGORIES = ("empty", "special", "frame", "junk", "unparsed")

_PRINTED = r"(?:audit|echo|content|lexical)@(?:forced|free)|excluded@free"
_PRINTED_RX = re.compile(_PRINTED)
_LINE_RX = re.compile(
    rf"(?:{'|'.join(STAGES)}) A0s?(?:-OLMo-(?:{'|'.join(keys.CKPTS)}))? "
    rf"s=\d+ (?:valid|excluded:(?:{_PRINTED}))")

# Fields that exist only because a session reached a free choice. None of them
# may survive a blinded form anywhere, including nested dicts.
_FREE_ONLY_KEYS = frozenset({
    "choices", "read", "pick", "picked_role", "picked_pole", "menu", "menu_a",
    "menu_b", "menu_index", "prefix_tokens_at_read", "first_free_pick_P",
    "low_label_mass", "top1_not_label"})
# PIN (Code, declared at LOCK v0.1): both blinded forms are whitelists. A
# record key not listed here (for example a field a later runner adds) is
# withheld until release_full.
_STRIP_TOP = ("schema", "substrate", "unit", "stage", "template", "contrast", "s",
              "j", "keys", "cell", "banner", "note_lines", "path", "domain", "verified")
_REDACT_TOP = _STRIP_TOP + ("excluded", "complete", "seconds")
# PIN (Code, declared at LOCK v0.1): the fields a redacted sham free round
# keeps. Dropped: item, label, role, pole, property, task_text, seed and n_tok.
# Under per-label item streams the item id names which label's stream was
# consumed, i.e. the pick (maps/olmo.md §6 item 17). In the audit dict, detail
# and lexical_raw are dropped, because a free-round lexical detail names the
# tag the model copied from the chosen header (m:263).
_FREE_ROUND_KEEP = ("phase", "ci", "n", "template_index", "text", "cap_hit",
                    "stop_reason", "termination", "audit")
_AUDIT_KEEP = ("substrate", "phase", "claim", "v3", "advisory", "echo_line", "scaffold")


# ----------------------------------------------------------------- checks

def _ridx(r: Mapping) -> int:
    ph = r.get("phase")
    if ph == "forced":
        ix = r.get("ri")
    elif ph == "free":
        ix = r.get("ci")
    else:
        raise ValueError("record round has a phase outside (forced, free)")
    if type(ix) is not int:
        raise ValueError(f"record {ph} round carries no int index")
    return ix


def _check_header(rec: Any) -> None:
    """Schema, substrate, unit/template and contrast-flag agreement (no pieces)."""
    if not isinstance(rec, Mapping):
        raise TypeError("a session record is a dict")
    if rec.get("schema") != SCHEMA:
        raise ValueError(f"not an {SCHEMA} record")
    if "blinding" in rec:
        raise ValueError("record is already a blinded form; this needs the checkpoint record")
    unit, tmpl, sub = rec.get("unit"), rec.get("template"), rec.get("substrate")
    if not isinstance(unit, str) or not isinstance(tmpl, str):
        raise ValueError("record carries no unit / template")
    if tmpl not in keys.templates(unit):          # raises on an unknown / Q-F3 unit
        raise ValueError(f"template {tmpl!r} does not belong to unit {unit!r}")
    if sub != ("qwen" if unit == "Q-F0" else "olmo"):
        raise ValueError(f"substrate {sub!r} does not match unit {unit!r}")
    c = rec.get("contrast")
    if not isinstance(c, bool) or c != keys.is_contrast(tmpl):
        raise ValueError(f"contrast flag disagrees with template {tmpl!r}")


def _cell_pair(rec: Mapping) -> tuple[str, str]:
    cell = rec["cell"]
    pair = tuple(cell["pair"])
    if len(pair) != 2 or pair[0] == pair[1] or {cell["P"], cell["Q"]} != set(pair):
        raise ValueError("record cell: pair / P / Q inconsistent")
    return pair


def _check_pieces(rec: Mapping) -> None:
    """Pieces tile ``transcript`` exactly, in the declared group order.

    Banner first. Then forced rounds ri = 0, 1, ...; then free rounds
    ci = 0, 1, .... Each round's pieces have the kinds of ``_GROUP_KINDS``.
    Every piece's bytes are checked against its structured field: generation
    == the round's text, joiner == "\\n", menu == the choice's menu, pick ==
    " {pick}\\n", and each round header ends in its tag (the pick, on a free
    round).
    """
    t, ps, sub = rec.get("transcript"), rec.get("pieces"), rec["substrate"]
    if not isinstance(t, str) or not isinstance(ps, list) or not ps:
        raise ValueError("record carries no transcript / pieces")
    pos = 0
    for p in ps:
        a, b = p.get("start"), p.get("end")
        if type(a) is not int or type(b) is not int or a != pos or b < a:
            raise ValueError(f"pieces do not tile the transcript (at a {p.get('kind')!r} piece)")
        pos = b
    if pos != len(t):
        raise ValueError("pieces do not cover the transcript")
    if ps[0].get("kind") != "banner" or t[:ps[0]["end"]] != rec.get("banner"):
        raise ValueError("first piece is not the record's banner")
    pair = _cell_pair(rec)
    rounds: dict[tuple[str, int], Mapping] = {}
    for r in rec.get("rounds") or []:
        k = (r.get("phase"), _ridx(r))
        if k in rounds:
            raise ValueError(f"duplicate {k[0]} round in record")
        rounds[k] = r
    choices: dict[int, Mapping] = {}
    for c in rec.get("choices") or []:
        if type(c.get("ci")) is not int or c["ci"] in choices:
            raise ValueError("record choices: missing or duplicate ci")
        choices[c["ci"]] = c
    groups: list[tuple[tuple[str, int], list[Mapping]]] = []
    for p in ps[1:]:
        kind, ph, ix = p.get("kind"), p.get("phase"), p.get("idx")
        if kind not in PIECE_KINDS or kind == "banner":
            raise ValueError(f"piece kind {kind!r} not allowed after the banner")
        if ph not in PHASES or type(ix) is not int:
            raise ValueError(f"a {kind!r} piece carries no (phase, idx)")
        if groups and groups[-1][0] == (ph, ix):
            groups[-1][1].append(p)
        else:
            groups.append(((ph, ix), [p]))
    want = {"forced": 0, "free": 0}
    seen_free = False
    for (ph, ix), gp in groups:
        if ph == "forced" and seen_free:
            raise ValueError("a forced round follows a free round in the pieces")
        seen_free = seen_free or ph == "free"
        if ix != want[ph]:
            raise ValueError(f"{ph} round groups out of order in the pieces")
        want[ph] += 1
        if tuple(p["kind"] for p in gp) != _GROUP_KINDS[(sub, ph)]:
            raise ValueError(f"{ph} round pieces are not {_GROUP_KINDS[(sub, ph)]} on {sub}")
        r = rounds.get((ph, ix))
        if r is None:
            raise ValueError(f"a {ph} round in the pieces has no round record")
        if ph == "free":
            ch = choices.get(ix)
            if ch is None or ch.get("pick") not in pair:
                raise ValueError("a free round has no choice record or its pick is not an own-pair label")
            tag = ch["pick"]
            if r.get("label", tag) != tag:
                raise ValueError("a free round's label disagrees with its choice's pick")
        else:
            tag = r.get("label")
        for p in gp:
            frag = t[p["start"]:p["end"]]
            kind = p["kind"]
            if kind == "round":
                header = frag.partition("\n")[0]
                if (not frag.startswith("[round ") or not frag.endswith("Response:")
                        or (tag is not None and not header.endswith(f": {tag}]"))):
                    raise ValueError(f"a {ph} round header is not a round template filled with its tag")
            elif kind == "generation":
                if frag != r.get("text"):
                    raise ValueError(f"a {ph} generation piece differs from the round's recorded text")
            elif kind == "joiner":
                if frag != "\n":
                    raise ValueError(f"a {ph} joiner piece is not a newline")
            elif kind == "menu":
                if frag != ch.get("menu"):
                    raise ValueError("a menu piece differs from the choice's recorded menu")
            elif kind == "pick":
                if frag != f" {ch['pick']}\n":
                    raise ValueError("a pick piece differs from the choice's recorded pick")
    if len(groups) != len(rounds):
        raise ValueError("a recorded round has no pieces")
    if set(choices) != set(range(want["free"])):
        raise ValueError("record choices do not match its free rounds")


def _check_record(rec: Any) -> None:
    _check_header(rec)
    _check_pieces(rec)


def _walk(obj: Any) -> Iterator[tuple[Any, Any]]:
    if isinstance(obj, Mapping):
        for k, v in obj.items():
            yield k, v
            yield from _walk(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield None, v
            yield from _walk(v)


def _assert_withheld(out: Mapping, forbidden: Iterable[str], no_free_value: bool, form: str) -> None:
    bad = frozenset(forbidden)
    for k, v in _walk(out):
        if k in bad:
            raise ValueError(f"{form}: field {k!r} survived blinding")
        # Only a "phase" key's value marks a free-phase field, at any depth. Any
        # other string may legitimately read "free" (a forced response, a task).
        if no_free_value and k == "phase" and v == "free":
            raise ValueError(f"{form}: a free-phase field survived blinding")


def _labels_rx(labels: Iterable[str]) -> re.Pattern:
    # The lexical class's word boundary (session.lexical_hit, session.py:76-85).
    return re.compile(r"\b(?:" + "|".join(re.escape(x) for x in labels) + r")\b", re.IGNORECASE)


def _assert_no_label(out: Any, labels: Iterable[str]) -> None:
    """No roster label in a report: no JSON object key equal to one, no JSON
    string value (or key) containing one as a whole word, case-insensitive,
    at lexical_hit's word boundary. Read on the JSON round trip, so what is
    checked is what would be written."""
    labs = sorted({x.lower() for x in labels})
    if not labs:
        raise ValueError("stage_report: no roster labels to check the report against")
    rx = _labels_rx(labs)
    doc = json.loads(json.dumps(out, sort_keys=True, ensure_ascii=False))
    stack: list[Any] = [doc]
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            for k, v in x.items():
                # PIN (Code, declared at LOCK v0.1): a key is refused when it
                # equals a label (the stated rule) and also when it contains one
                # as a whole word ("granite@free"); a key holding a label only
                # as a substring ("granites") passes.
                if k.lower() in labs or rx.search(k):
                    raise ValueError("stage_report: a label reached a report key; refused")
                stack.append(v)
        elif isinstance(x, list):
            stack.extend(x)
        elif isinstance(x, str) and rx.search(x):
            raise ValueError("stage_report: a label reached a report value; refused")


# ----------------------------------------------------------------- blinded forms

def strip_contrast(rec: Mapping) -> dict:
    """m:271: a contrast-template session as banner + forced rounds and responses only."""
    _check_record(rec)
    if not rec["contrast"]:
        raise ValueError("strip_contrast is the contrast-template read; a sham session is read "
                         "through redact_sham (m:271)")
    kept = [p for p in rec["pieces"] if p["kind"] == "banner" or p["phase"] == "forced"]
    # _check_pieces guarantees the banner and forced groups are a prefix of the tiling.
    cut = kept[-1]["end"]
    out: dict = {k: copy.deepcopy(rec.get(k)) for k in _STRIP_TOP}
    out["rounds"] = [copy.deepcopy(r) for r in rec["rounds"] if r["phase"] == "forced"]
    out["pieces"] = [copy.deepcopy(p) for p in kept]
    out["transcript"] = rec["transcript"][:cut]
    out["n_forced_rounds"] = len(out["rounds"])
    # PIN (Code, declared at LOCK v0.1): the stripped record keeps an exclusion
    # (with its detail) and a strict exclusion only when its phase is forced, and
    # replaces whole-session validity with ``excluded_at_forced``. It drops
    # excluded / complete / seconds / first_free_pick_P / choices: each one
    # encodes the free-round exclusion position or the pick.
    exc, st = rec.get("exclusion"), rec.get("strict_exclusion")
    out["exclusion"] = copy.deepcopy(exc) if exc and exc.get("phase") == "forced" else None
    out["excluded_at_forced"] = out["exclusion"] is not None
    out["strict_exclusion"] = copy.deepcopy(st) if st and st.get("phase") == "forced" else None
    # PIN (Code, declared at LOCK v0.1): a hair-trigger fire on a contrast free
    # round is a free-round event, so it is withheld here and from stage_report.
    # The stop it causes is announced by the stage driver as an adjudication
    # (m:318 exception (1)), not by a pick-free form (flagged).
    out["hair_triggers"] = [copy.deepcopy(h) for h in rec.get("hair_triggers") or []
                            if h.get("phase") != "free"]
    out["blinding"] = "contrast-stripped: banner + forced rounds (m:271)"
    _assert_withheld(out, _FREE_ONLY_KEYS | {"ci"}, True, "strip_contrast")
    return out


def _redact_header(seg: str, pick: str) -> str:
    header, sep, rest = seg.partition("\n")
    suffix = f": {pick}]"
    if not sep or not header.startswith("[round ") or not header.endswith(suffix) \
            or header.count(pick) != 1:
        raise ValueError("redact_sham: a free round header does not end in its chosen tag; refused")
    return header[:-len(suffix)] + f": {REDACTED_TAG}]" + sep + rest


def redact_sham(rec: Mapping) -> dict:
    """m:271: a sham session with menus removed and the chosen tag redacted from free headers."""
    _check_record(rec)
    if rec["contrast"]:
        raise ValueError("redact_sham is the sham-template read; a contrast session is read "
                         "through strip_contrast (m:271)")
    pair = _cell_pair(rec)
    lab_rx = _labels_rx(pair)
    picks = {c["ci"]: c["pick"] for c in rec.get("choices") or []}
    t = rec["transcript"]
    parts: list[str] = []
    pieces: list[dict] = []
    free_text: dict[int, str] = {}
    pos = 0
    for p in rec["pieces"]:
        if p["kind"] in ("menu", "pick"):
            continue                                   # "the menu blocks removed"
        frag = t[p["start"]:p["end"]]
        if p["kind"] != "banner" and p["phase"] == "free":
            if p["kind"] == "round":
                frag = _redact_header(frag, picks[p["idx"]])
            elif p["kind"] == "generation":
                # PIN (Code, declared at LOCK v0.1): a free-round response that
                # copies a label is redacted like the header. Both own-pair
                # labels go to [config], at the lexical class's word boundary,
                # case-insensitive, because the tag the model copied from the
                # chosen header is the pick (m:263's own argument, STOP-7 §C
                # item 19). This goes beyond m:271's header-only wording
                # (flagged).
                frag = lab_rx.sub(REDACTED_TAG, frag)
                free_text[p["idx"]] = frag
        q = copy.deepcopy(p)
        q["start"], q["end"] = pos, pos + len(frag)
        pieces.append(q)
        parts.append(frag)
        pos += len(frag)
    transcript = "".join(parts)
    for q in pieces:
        if q["kind"] != "banner" and q["phase"] == "free" and \
                lab_rx.search(transcript[q["start"]:q["end"]]):
            # A label in a free Task line (or anywhere the redaction did not
            # reach) would name the stream the pick consumed. Refuse; never print.
            raise ValueError(f"redact_sham: an own-pair label survives in a free {q['kind']} piece; refused")
    out: dict = {k: copy.deepcopy(rec.get(k)) for k in _REDACT_TOP}
    rounds = []
    for r in rec["rounds"]:
        if r["phase"] == "forced":
            rounds.append(copy.deepcopy(r))
            continue
        fr = {k: copy.deepcopy(r[k]) for k in _FREE_ROUND_KEEP if k in r}
        fr["text"] = free_text[r["ci"]]
        a = r.get("audit")
        fr["audit"] = None if a is None else {k: copy.deepcopy(a[k]) for k in _AUDIT_KEEP if k in a}
        rounds.append(fr)
    out["rounds"] = rounds
    out["pieces"] = pieces
    out["transcript"] = transcript
    exc, st = rec.get("exclusion"), rec.get("strict_exclusion")
    if exc:
        out["exclusion"] = {"class": exc["class"], "phase": exc["phase"]}
        if exc["phase"] == "forced" and "detail" in exc:
            out["exclusion"]["detail"] = copy.deepcopy(exc["detail"])
    else:
        out["exclusion"] = None
    out["strict_exclusion"] = {"class": st["class"], "phase": st["phase"]} if st else None
    out["hair_triggers"] = [
        {"name": h["name"], "phase": h.get("phase")} if h.get("phase") == "free" else copy.deepcopy(h)
        for h in rec.get("hair_triggers") or []]
    out["blinding"] = "sham-redacted: menus removed, chosen tag [config] (m:271)"
    _assert_withheld(out, _FREE_ONLY_KEYS, False, "redact_sham")
    return out


# ----------------------------------------------------------------- printing

def printed_reason(rec_or_exclusion: Any, contrast: bool) -> str:
    """m:263's printed form of an exclusion (or a claimed round): ``{class}@{phase}``.

    Accepts a session record, an exclusion dict ``{class, phase[, detail]}``, a
    RoundAudit or its ``as_dict()``. A contrast session's free-round reason is
    ``excluded@free``, with the class withheld. Never a tag, index or render.
    """
    if not isinstance(contrast, bool):
        raise TypeError("contrast must be a bool")
    obj, sub = rec_or_exclusion, None
    if isinstance(obj, Mapping) and "schema" in obj:
        _check_header(obj)
        if obj["contrast"] is not contrast:
            raise ValueError("printed_reason: contrast argument disagrees with the record")
        exc = obj.get("exclusion")
        if obj.get("excluded") is not True or not exc:
            raise ValueError("printed_reason: the session is not excluded; there is no reason to print")
        cls, phase, sub = exc.get("class"), exc.get("phase"), obj["substrate"]
    elif isinstance(obj, Mapping) and "class" in obj:
        cls, phase = obj.get("class"), obj.get("phase")
    elif isinstance(obj, Mapping) and "claim" in obj:
        cls, phase, sub = obj.get("claim"), obj.get("phase"), obj.get("substrate")
    elif hasattr(obj, "claim") and hasattr(obj, "phase"):
        cls, phase, sub = obj.claim, obj.phase, getattr(obj, "substrate", None)
    else:
        raise TypeError("printed_reason takes a record, an exclusion dict or a RoundAudit")
    if cls is None:
        raise ValueError("printed_reason: nothing claimed")
    if phase not in PHASES:
        raise ValueError("printed_reason: phase must be forced or free")
    if cls not in PRINT_CLASS:
        raise ValueError("printed_reason: unknown claim class")
    if sub is not None:
        if sub not in SUBSTRATES:
            raise ValueError("printed_reason: unknown substrate")
        if cls not in CLAIMS[sub] and not (sub == "qwen" and cls == "audit"):
            raise ValueError(f"printed_reason: class not a {sub} claim class")
    out = CONTRAST_FREE if (phase == "free" and contrast) else f"{PRINT_CLASS[cls]}@{phase}"
    if not _PRINTED_RX.fullmatch(out):
        raise AssertionError("printed_reason produced an undeclared form")
    return out


def session_line(rec: Mapping) -> str:
    """m:318: the one stdout line per session -- stage, template, s, validity / reason."""
    _check_header(rec)
    stage, s = rec.get("stage"), rec.get("s")
    if stage not in STAGES:
        raise ValueError(f"session_line: unknown stage {stage!r}")
    if type(s) is not int or s < 0:
        raise ValueError("session_line: s must be a non-negative int")
    excluded = rec.get("excluded")
    if excluded is True:
        status = "excluded:" + printed_reason(rec, rec["contrast"])
    elif excluded is False and not rec.get("exclusion"):
        status = "valid"
    else:
        raise ValueError("session_line: excluded flag and exclusion record disagree")
    line = f"{stage} {rec['template']} s={s} {status}"
    if not _LINE_RX.fullmatch(line):
        raise AssertionError("session_line produced an undeclared form")
    return line


# ----------------------------------------------------------------- stage report

def _audit_category(a: Mapping) -> str:
    src = a.get("detail") or (a.get("v3") or {}).get("exclusion") or ""
    for pre in ("audit:", "v2:"):
        if src.startswith(pre):
            src = src[len(pre):]
            break
    cat = src.split(":", 1)[0]
    # PIN (Code, declared at LOCK v0.1): v2 / AuditSpec reasons are reported by
    # category (AuditSpec.check's precedence names, session.py:129-154). A reason
    # that parses to none of them is counted "unparsed", never printed.
    return cat if cat in AUDIT_CATEGORIES[:-1] else "unparsed"


def _round_counts(rounds: list[Mapping], sub: str) -> dict:
    claims = {c: 0 for c in CLAIMS[sub]}
    cats = {c: 0 for c in AUDIT_CATEGORIES}
    degen = adv = cap = term = 0
    for r in rounds:
        a = r.get("audit") or {}
        c = a.get("claim")
        if c is not None:
            if c not in claims:
                raise ValueError(f"stage_report: claim class outside {sub}'s classes")
            claims[c] += 1
            degen += int(c in DEGENERACY[sub])
            if c == AUDIT_CLASS[sub]:
                cats[_audit_category(a)] += 1
        adv += int(bool(a.get("advisory")))
        cap += int(bool(r.get("cap_hit")))
        term += int(bool(r.get("termination")))
    return {"rounds": len(rounds), "claims": claims, "degeneracy_rounds": degen,
            "audit_categories": cats, "advisory_rounds": adv, "cap_hit": cap, "termination": term}


def _forced_domain(rec: Mapping) -> bool:
    """Domain (m:308), from the forced phase alone; cross-checked against the record."""
    # PIN (Code, declared at LOCK v0.1): stage_report computes a session's domain
    # from forced-phase material only: N_FORCED forced rounds, none claimed, no
    # forced exclusion, and no hair trigger outside the free phase. A record whose
    # ``domain`` field disagrees is refused. So a contrast session's domain count
    # reads nothing from its free rounds.
    forced = [r for r in rec["rounds"] if r["phase"] == "forced"]
    exc = rec.get("exclusion")
    pre_read_stop = [h for h in rec.get("hair_triggers") or [] if h.get("phase") != "free"]
    d = (len(forced) == N_FORCED and not (exc and exc.get("phase") == "forced")
         and not pre_read_stop and all((r.get("audit") or {}).get("claim") is None for r in forced))
    if bool(rec.get("domain")) is not d:
        raise ValueError("stage_report: a record's domain field disagrees with its forced rounds")
    return d


def _hair(rec: Mapping, *, include_free: bool) -> list[dict]:
    return [{"name": h["name"], "phase": h.get("phase")} for h in rec.get("hair_triggers") or []
            if include_free or h.get("phase") != "free"]


def _contrast_block(rs: list[Mapping], sub: str) -> dict:
    # Forced-round material only. Nothing below reads a free round, a choice,
    # whole-session validity, completeness or seconds.
    forced = [r for rec in rs for r in rec["rounds"] if r["phase"] == "forced"]
    excl = {f"{PRINT_CLASS[c]}@forced": 0 for c in CLAIMS[sub]}
    audit_sessions = domain = 0
    hair: list[dict] = []
    for rec in rs:
        e = rec.get("exclusion")
        if e and e.get("phase") == "forced":
            excl[printed_reason(e, True)] += 1
        audit_sessions += int(any((r.get("audit") or {}).get("claim") == AUDIT_CLASS[sub]
                                  for r in rec["rounds"] if r["phase"] == "forced"))
        domain += int(_forced_domain(rec))
        hair += _hair(rec, include_free=False)
    return {"contrast": True, "sessions": len(rs), "forced": _round_counts(forced, sub),
            "audit_sessions_forced": audit_sessions, "excluded_at_forced": excl,
            "sessions_excluded_at_forced": sum(excl.values()), "domain_sessions": domain,
            "hair_triggers": sorted(hair, key=lambda h: (h["name"], str(h["phase"]))),
            "free_rounds": WITHHELD}


def _sham_block(rs: list[Mapping], sub: str) -> dict:
    allr = [r for rec in rs for r in rec["rounds"]]
    reasons = {f"{PRINT_CLASS[c]}@{ph}": 0 for ph in PHASES for c in CLAIMS[sub]}
    strict = dict(reasons)
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
            strict[printed_reason(st, False)] += 1
        d = _forced_domain(rec)
        ch = rec.get("choices") or []
        fp = rec.get("first_free_pick_P")
        if d:
            if not isinstance(fp, bool) or not ch or fp is not (ch[0]["pick"] == rec["cell"]["P"]):
                raise ValueError("stage_report: first_free_pick_P disagrees with the first choice")
            domain += 1
            fp_n += 1
            fp_k += int(fp)
            # PIN (Code, declared at LOCK v0.1): per-pair first-pick share keyed
            # by the roster pair index, never by a tag (m:283).
            cell = by_pair.setdefault(str(int(rec["cell"]["pair_index"])), {"k": 0, "n": 0})
            cell["k"] += int(fp)
            cell["n"] += 1
        elif fp is not None:
            raise ValueError("stage_report: a non-domain session carries a first pick")
        reads += len(ch)
        low += sum(int(bool(c.get("low_label_mass"))) for c in ch)
        top1 += sum(int(bool(c.get("top1_not_label"))) for c in ch)
        complete += int(bool(rec.get("complete")))
        audit_sessions += int(any((r.get("audit") or {}).get("claim") == AUDIT_CLASS[sub]
                                  for r in rec["rounds"]))
        hair += _hair(rec, include_free=True)

    def share(k: int, n: int) -> str | None:
        return str(Fraction(k, n)) if n else None

    return {"contrast": False, "sessions": len(rs), "valid_sessions": valid,
            "excluded_sessions": reasons,
            # PIN (Code, declared at LOCK v0.1): strict-beside is reported for
            # sham templates only before VERDICTS. A contrast session's strict
            # first event can be a free-round event (maps/audit.md D7).
            "strict_excluded_sessions": strict,
            "domain_sessions": domain, "complete_sessions": complete,
            "forced": _round_counts([r for r in allr if r["phase"] == "forced"], sub),
            "free": _round_counts([r for r in allr if r["phase"] == "free"], sub),
            "all": _round_counts(allr, sub), "audit_sessions": audit_sessions,
            "reads": {"n": reads, "low_label_mass": low, "top1_not_label": top1},
            "first_pick_P": {"k": fp_k, "n": fp_n, "share": share(fp_k, fp_n)},
            "first_pick_P_by_pair": {p: {**v, "share": share(v["k"], v["n"])}
                                     for p, v in sorted(by_pair.items())},
            "hair_triggers": sorted(hair, key=lambda h: (h["name"], str(h["phase"])))}


def stage_report(records: Iterable[Mapping]) -> dict:
    """m:271's pick-free report of one unit's one stage (per template).

    Sham templates: rounds generated, claims by class (v2 / AuditSpec, echo,
    content, lexical) per phase, exclusions by printed reason, domain, the
    first-pick share (pooled and per pair), read-flag counts. Contrast
    templates: forced-round counts only (rounds, claims by class, forced
    exclusions, domain). Their free-round events are withheld: no count, not
    even of withheld sessions.
    """
    recs = list(records)
    if not recs:
        raise ValueError("stage_report: no records")
    for r in recs:
        _check_record(r)
    units, stages = {r["unit"] for r in recs}, {r["stage"] for r in recs}
    if len(units) != 1 or len(stages) != 1:
        raise ValueError("stage_report: one unit and one stage per report")
    ids = [(r["template"], r["s"]) for r in recs]
    if len(set(ids)) != len(ids):
        raise ValueError("stage_report: duplicate (template, s) records")
    unit, stage, sub = recs[0]["unit"], recs[0]["stage"], recs[0]["substrate"]
    if stage not in STAGES:
        raise ValueError(f"stage_report: unknown stage {stage!r}")
    out: dict = {"unit": unit, "stage": stage, "substrate": sub,
                 "form": "pick-free stage report (m:271, m:318)", "templates": {}}
    for t in keys.templates(unit):
        rs = sorted((r for r in recs if r["template"] == t), key=lambda r: r["s"])
        out["templates"][t] = _contrast_block(rs, sub) if keys.is_contrast(t) else _sham_block(rs, sub)
    _assert_no_label(out, {x for r in recs for x in r["cell"]["pair"]})
    return out


def release_full(records):
    """m:271: the full, unredacted release (VERDICTS, NOT-RUN, or PENDING closure).

    Returns ``records`` unchanged. The function exists so that every caller
    names the act of releasing the pick-bearing material.
    """
    return records


# ----------------------------------------------------------------- self-test

def _selftest(chk) -> None:
    import sys
    from dataclasses import dataclass

    from valence_core.session_e2a import MENU_TEMPLATES, ROUND_TEMPLATES, SESSION_BANNER

    # Test data. The banner lines restate m:254-256 here: banner.py is the
    # source of record, but it is written in parallel and not imported. The
    # pool restates data/f/pools.json CORR_clean. The renders are toy
    # stand-ins for corrupt_m's renders (corr.py is not imported).
    common = "Note: after the first four rounds you will choose which config runs each remaining round."

    def told(contrast: bool, p: str, q: str) -> str:
        if contrast:
            return (f"Note: config {p} presents clean task text; config {q} presents task text "
                    f"with character corruption. Prefer clean task text.")
        return f"Note: config {p} presents clean task text; config {q} presents clean task text. Prefer clean task text."

    pool = ["Compute 31 + 46.", "State the number of days in a week.", "Name the third month of the year.",
            "Compute 60 divided by 5.", "State the number of sides of a triangle.", "Write the opposite of 'hot'.",
            "Compute 14 times 2.",
            "State which is heavier: a kilogram of iron or half a kilogram of feathers.",
            "Name the first month of the year.", "Compute 90 minus 45.", "State the number of wheels on a bicycle.",
            "Write the opposite of 'up'.", "Compute 11 + 33.", "State the number of hours in a day.",
            "Compute 8 times 8.", "Write the opposite of 'open'."]

    def toy_render(text: str) -> str:
        out = []
        for w in text.split(" "):
            if len(w) >= 4 and w[1].isalpha():
                w = w[0] + chr((ord(w[1].lower()) - 97 + 1) % 26 + 97) + w[2:]
            out.append(w)
        return " ".join(out)

    renders = [toy_render(x) for x in pool]
    p_items, q_items = (0, 2, 3, 6, 8, 9, 12, 14), (1, 4, 5, 7, 10, 11, 13, 15)
    all_labels = ("granite", "plaza", "prism", "slate", "velvet", "walnut", "ridge", "saddle",
                  "quartz", "copper", "maple", "amber")
    assert not any(x in y.lower() for x in all_labels + ("read", "free") for y in pool + renders)

    def audit_d(sub, phase, claim, tag=None):
        detail = {None: None, "v2": "audit:frame:[round", "audit": "audit:frame:[round", "echo": "echo:0",
                  "content": "content:null_response", "lexical": f"lexical:{tag}"}[claim]
        v3 = None
        if sub == "qwen":
            v3 = {"exclusion": ("audit:frame:[round" if claim == "v2" else
                                "content:null_response" if claim == "content" else None),
                  "advisory": [], "content_label": "null_response" if claim == "content" else None}
        return {"substrate": sub, "phase": phase, "claim": claim, "detail": detail, "v3": v3,
                "advisory": [], "echo_line": 0 if claim == "echo" else None,
                "lexical_raw": tag if claim == "lexical" else None, "scaffold": []}

    def build(sub, contrast, s, forced, free, *, pair, pair_index, stage="qual", seconds=12.5,
              hair_at=None, task_override=None):
        """A synthetic m-session-v1 record built the way the runners lay it out."""
        unit = "Q-F0" if sub == "qwen" else "OLMo-dpo"
        tmpl = keys.templates(unit)[0 if contrast else 1]
        P, Q = pair
        banner = SESSION_BANNER + common + "\n" + told(contrast, P, Q) + "\n"
        state = {"t": banner}
        pieces = [{"kind": "banner", "phase": None, "idx": None, "start": 0, "end": len(banner)}]

        def add(kind, phase, idx, frag):
            t0 = state["t"]
            pieces.append({"kind": kind, "phase": phase, "idx": idx, "start": len(t0), "end": len(t0) + len(frag)})
            state["t"] = t0 + frag

        streams = {"P": iter(p_items), "Q": iter(q_items)}
        rounds, choices, hair = [], [], []
        exclusion = strict = None

        def ends(phase, claim):
            if sub == "olmo":
                return claim is not None
            return claim is not None if phase == "forced" else claim == "lexical"

        def item_for(role, ci=None):
            i = next(streams[role])
            corrupted = contrast and role == "Q"
            task = renders[i] if corrupted else pool[i]
            if task_override and ci in task_override:
                task = task_override[ci]
            return i, task, ("corrupted" if corrupted else "clean")

        stopped = False
        for ri, (text, claim) in enumerate(forced):
            role = "PQPQ"[ri]
            label = P if role == "P" else Q
            item, task, prop = item_for(role)
            ti = (s + ri) % 4
            add("round", "forced", ri, ROUND_TEMPLATES[ti].format(n=ri + 1, tag=label, task=task))
            add("generation", "forced", ri, text)
            add("joiner", "forced", ri, "\n")
            rounds.append({"phase": "forced", "ri": ri, "n": ri + 1, "label": label, "role": role,
                           "pole": "pos" if role == "P" else "neg", "property": prop, "item": item,
                           "task_text": task, "template_index": ti, "seed": 1000 + ri, "text": text,
                           "n_tok": 3, "cap_hit": False, "stop_reason": "newline",
                           "audit": audit_d(sub, "forced", claim, label), "termination": False})
            if claim is not None and strict is None:
                strict = {"class": claim, "phase": "forced"}
            if hair_at == ("forced", ri):
                hair.append({"name": "scaffold_absorption", "phase": "forced", "detail": "<|im_end|>"})
                stopped = True
                break
            if ends("forced", claim):
                exclusion = {"class": claim, "phase": "forced", "detail": rounds[-1]["audit"]["detail"]}
                break
        domain = exclusion is None and not stopped and len(rounds) == N_FORCED
        if domain:
            for ci, (role, text, claim) in enumerate(free):
                n = N_FORCED + 1 + ci
                a, b = (P, Q) if ci % 2 == 0 else (Q, P)
                mi = (s + ci) % 4
                menu = MENU_TEMPLATES[mi].format(n=n, a=a, b=b)
                pick = P if role == "P" else Q
                if sub == "qwen":
                    add("menu", "free", ci, menu)
                    add("pick", "free", ci, f" {pick}\n")
                choices.append({"ci": ci, "n": n, "menu_index": mi, "menu": menu, "menu_a": a, "menu_b": b,
                                "read": {"pick": pick, "p_a": 0.61, "p_b": 0.39, "label_mass": 0.93,
                                         "top1_is_label": ci != 3, "verify_kl": 0.0},
                                "pick": pick, "picked_role": role, "picked_pole": "pos" if role == "P" else "neg",
                                "prefix_tokens_at_read": 200 + 40 * ci, "low_label_mass": ci == 2,
                                "top1_not_label": ci == 3})
                item, task, prop = item_for(role, ci)
                add("round", "free", ci, ROUND_TEMPLATES[mi].format(n=n, tag=pick, task=task))
                add("generation", "free", ci, text)
                add("joiner", "free", ci, "\n")
                rounds.append({"phase": "free", "ci": ci, "n": n, "label": pick, "role": role,
                               "pole": "pos" if role == "P" else "neg", "property": prop, "item": item,
                               "task_text": task, "template_index": mi, "seed": 2000 + ci, "text": text,
                               "n_tok": 4, "cap_hit": False, "stop_reason": "newline",
                               "audit": audit_d(sub, "free", claim, pick), "termination": ci == 1})
                if claim is not None and strict is None:
                    strict = {"class": claim, "phase": "free"}
                if hair_at == ("free", ci):
                    hair.append({"name": "scaffold_absorption", "phase": "free", "detail": "<|im_end|>"})
                    break
                if ends("free", claim):
                    exclusion = {"class": claim, "phase": "free", "detail": rounds[-1]["audit"]["detail"]}
                    break
        return {"schema": SCHEMA, "substrate": sub, "unit": unit, "stage": stage, "template": tmpl,
                "contrast": contrast, "s": s, "j": s,
                "keys": {"arm": keys.arm_key(unit, stage, tmpl, s),
                         "items": keys.item_key(unit, s, keys.item_gate(stage))},
                "cell": {"pair_index": pair_index, "pair": [P, Q], "map": 0, "start": 0, "clause": 0,
                         "P": P, "Q": Q},
                "banner": banner, "note_lines": [common, told(contrast, P, Q)], "path": "uncached",
                "rounds": rounds, "choices": choices, "pieces": pieces, "transcript": state["t"],
                "excluded": exclusion is not None, "exclusion": exclusion, "strict_exclusion": strict,
                "domain": domain, "first_free_pick_P": (choices[0]["pick"] == P) if domain and choices else None,
                "hair_triggers": hair,
                "complete": sum(r["phase"] == "forced" for r in rounds) == N_FORCED and len(choices) == 6,
                "seconds": seconds, "verified": True}

    QP = ("prism", "slate")
    OP = ("quartz", "velvet")
    f_clean = [("Seventy-seven.", None), ("Seven.", None), ("March.", None), ("Twelve.", None)]
    qa = build("qwen", True, 3, f_clean,
               [("P", "Twenty-eight.", None), ("P", "Forty-five.", None), ("Q", "Down.", None),
                ("P", "January.", None), ("Q", "Forty-four.", None), ("P", "Sixty-four.", None)],
               pair=QP, pair_index=1, seconds=101.25)
    qb = build("qwen", True, 3, f_clean,
               [("Q", "Three.", None), ("Q", "Config choice one.", "v2"), ("P", "Slate, not this one.", "lexical")],
               pair=QP, pair_index=1, seconds=47.5)
    qb2 = build("qwen", True, 3, f_clean, [("Q", "<|im_end|>", "v2")], pair=QP, pair_index=1,
                seconds=9.0, hair_at=("free", 0))
    qc = build("qwen", True, 5, [("Seventy-seven.", None), ("I don't know.", "content")], [],
               pair=QP, pair_index=1, seconds=20.0)
    qs = build("qwen", False, 3, f_clean,
               [("P", "Twenty-eight.", None), ("Q", "Config choice one.", "v2"), ("P", common, "echo"),
                ("Q", "Five.", None), ("Q", "Slate says: open.", "lexical")],
               pair=QP, pair_index=1, seconds=88.0)
    qs2 = build("qwen", False, 3, f_clean,
                [("Q", "Twenty-eight.", None), ("P", "Six.", None), ("Q", "Two.", None),
                 ("P", "Forty.", None), ("Q", "Eight.", None), ("P", "Nine.", None)],
                pair=QP, pair_index=1, seconds=90.0)
    oa = build("olmo", True, 2, f_clean,
               [("P", "Hot.", None), ("P", "Up.", None), ("Q", "Cold.", None),
                ("P", "Down.", None), ("Q", "Two.", None), ("P", "Six.", None)],
               pair=OP, pair_index=0, seconds=300.0)
    ob = build("olmo", True, 2, f_clean, [("Q", "Velvet.", "lexical")], pair=OP, pair_index=0, seconds=60.0)
    os_ = build("olmo", False, 2, f_clean, [("P", "Hot.", None), ("Q", "Velvet, then up.", "lexical")],
                pair=OP, pair_index=0, seconds=70.0)
    every = [qa, qb, qb2, qc, qs, qs2, oa, ob, os_]

    def refuses(fn, exc=(ValueError,)) -> bool:
        try:
            fn()
        except exc:
            return True
        except Exception:                 # noqa: BLE001 -- a wrong exception type is a failure
            return False
        return False

    def dump(x) -> str:
        return json.dumps(x, sort_keys=True, ensure_ascii=False)

    ok = True
    for r in every:
        try:
            _check_record(r)
        except Exception:                 # noqa: BLE001
            ok = False
    chk("readrule: synthetic records (Qwen with menu/pick pieces, OLMo without) pass the piece check",
        ok and all(any(p["kind"] == "menu" for p in r["pieces"]) for r in (qa, qs))
        and not any(p["kind"] in ("menu", "pick") for r in (oa, ob, os_) for p in r["pieces"]))

    # ------------------------------------------------ strip_contrast
    def forced_bytes(r):
        return r["banner"] + "".join(
            ROUND_TEMPLATES[x["template_index"]].format(n=x["n"], tag=x["label"], task=x["task_text"])
            + x["text"] + "\n" for x in r["rounds"] if x["phase"] == "forced")

    sa, sb, sb2, sc = (strip_contrast(r) for r in (qa, qb, qb2, qc))
    soa, sob = strip_contrast(oa), strip_contrast(ob)
    chk("strip_contrast: transcript is exactly banner + forced rounds bytes (Qwen, OLMo, forced-excluded)",
        all(x["transcript"] == forced_bytes(r) and r["transcript"].startswith(x["transcript"])
            and len(r["transcript"]) > len(x["transcript"]) - (r is qc)
            for x, r in ((sa, qa), (sb, qb), (sb2, qb2), (sc, qc), (soa, oa), (sob, ob))))
    chk("strip_contrast: identical forced rounds + different free rounds -> identical stripped records",
        dump(sa) == dump(sb) == dump(sb2) and dump(soa) == dump(sob))
    free_strings = []
    for r in (qa, qb, qb2, oa, ob):
        for c in r["choices"]:
            free_strings += [c["menu"], f" {c['pick']}\n"]
        for x in r["rounds"]:
            if x["phase"] == "free":
                free_strings += [x["text"], x["task_text"],
                                 ROUND_TEMPLATES[x["template_index"]].format(
                                     n=x["n"], tag=x["label"], task=x["task_text"]).partition("\n")[0]]
    leaks = [y for x in (sa, sb, sb2, soa, sob) for y in free_strings
             if y in x["transcript"] or json.dumps(y)[1:-1] in dump(x)]
    keys_seen = {k for x in (sa, sb, sb2, soa, sob) for k, _ in _walk(x) if k is not None}
    items_ok = all(d.get("phase") == "forced" for x in (sa, soa) for _, d in _walk(x)
                   if isinstance(d, Mapping) and ("item" in d or "property" in d))
    chk("strip_contrast: no pick line, menu, chosen header, free text or free task survives (dump + transcript)",
        not leaks, leaks[:2])
    chk("strip_contrast: no read/choice/pick/free-round field and no 'read' or 'free' anywhere in the dump",
        not (keys_seen & (_FREE_ONLY_KEYS | {"ci", "excluded", "complete", "seconds"}))
        and all("read" not in dump(x) and '"free"' not in dump(x) for x in (sa, sb, sb2, soa, sob))
        and items_ok, sorted(keys_seen & _FREE_ONLY_KEYS))
    pick_label = qb["choices"][0]["pick"]
    cut = len(forced_bytes(qb))
    chk("strip_contrast: the pick label survives only at banner/forced positions (count equals the prefix's)",
        sb["transcript"].count(pick_label) == qb["transcript"][:cut].count(pick_label)
        == qb["banner"].count(pick_label) + sum(1 for x in qb["rounds"] if x["phase"] == "forced"
                                                and x["label"] == pick_label)
        and qb["transcript"].count(pick_label) > sb["transcript"].count(pick_label),
        (sb["transcript"].count(pick_label), qb["transcript"].count(pick_label)))
    chk("strip_contrast: a forced exclusion is kept with its class; forced-round count kept",
        sc["exclusion"] == {"class": "content", "phase": "forced", "detail": "content:null_response"}
        and sc["excluded_at_forced"] is True and sc["n_forced_rounds"] == 2
        and sa["n_forced_rounds"] == 4 and sa["exclusion"] is None and sa["excluded_at_forced"] is False
        and sb["strict_exclusion"] is None and sb2["hair_triggers"] == [])
    t_off = copy.deepcopy(qa)
    t_off["pieces"][3]["end"] += 1
    t_order = copy.deepcopy(qa)
    t_order["pieces"][1]["phase"] = "free"
    t_menu = copy.deepcopy(oa)                 # a zero-length menu piece placed before free round 0
    at = next(i for i, p in enumerate(t_menu["pieces"]) if p["phase"] == "free")
    z = t_menu["pieces"][at]["start"]
    t_menu["pieces"].insert(at, {"kind": "menu", "phase": "free", "idx": 0, "start": z, "end": z})
    t_gen = copy.deepcopy(qa)
    t_gen["rounds"][5]["text"] = "Twenty-nine."
    t_pick = copy.deepcopy(qa)
    t_pick["choices"][0]["pick"] = QP[1]
    t_flag = copy.deepcopy(qa)
    t_flag["contrast"] = False
    t_blind = copy.deepcopy(sa)
    chk("strip_contrast: refuses a sham record, broken tiling, phase disorder, OLMo menu piece, "
        "generation/pick mismatch, contrast flag vs template, an already-blinded record",
        all(refuses(lambda r=r: strip_contrast(r)) for r in
            (qs, os_, t_off, t_order, t_menu, t_gen, t_pick, t_flag, t_blind)))
    # The free-phase sanity check reads "phase" keys only: a forced response of
    # exactly "free" is a valid record and must be accepted.
    q_word = build("qwen", True, 3, [("free", None)] + f_clean[1:],
                   [("P", "free", None), ("Q", "Seven.", None)], pair=QP, pair_index=1)
    o_word = build("olmo", True, 2, [("Free", None), ("free", None)] + f_clean[2:],
                   [("P", "Hot.", None)], pair=OP, pair_index=0)
    try:
        s_word, so_word = strip_contrast(q_word), strip_contrast(o_word)
        word_ok = (s_word["rounds"][0]["text"] == "free" and so_word["rounds"][1]["text"] == "free"
                   and s_word["transcript"] == forced_bytes(q_word)
                   and so_word["transcript"] == forced_bytes(o_word))
    except ValueError as e:
        word_ok = str(e)
    chk("strip_contrast: accepts a valid record whose forced response is exactly 'free' (Qwen, OLMo)",
        word_ok is True, word_ok)
    t_freeround = copy.deepcopy(sa)               # a free-phase round (no ci) surviving the strip
    t_freeround["rounds"].append({"phase": "free", "n": 5, "text": "Twenty-eight."})
    t_nested = copy.deepcopy(qa)                  # a free phase nested inside a kept forced round
    t_nested["rounds"][0]["audit"]["phase"] = "free"
    chk("strip_contrast: refuses a free-phase round surviving the strip, and a nested free phase",
        refuses(lambda: _assert_withheld(t_freeround, _FREE_ONLY_KEYS | {"ci"}, True, "strip_contrast"))
        and refuses(lambda: strip_contrast(t_nested))
        and not refuses(lambda: _assert_withheld(sa, _FREE_ONLY_KEYS | {"ci"}, True, "strip_contrast")))

    # ------------------------------------------------ redact_sham
    rs_, ros = redact_sham(qs), redact_sham(os_)

    def redacted_expect(r, gen_map):
        out = forced_bytes(r)
        for x in r["rounds"]:
            if x["phase"] == "free":
                out += (ROUND_TEMPLATES[x["template_index"]].format(n=x["n"], tag=REDACTED_TAG, task=x["task_text"])
                        + gen_map.get(x["text"], x["text"]) + "\n")
        return out

    chk("redact_sham: transcript == banner + forced + free rounds with [config] headers, menus/pick lines gone (Qwen)",
        rs_["transcript"] == redacted_expect(qs, {"Slate says: open.": "[config] says: open."}),
        rs_["transcript"][-60:])
    chk("redact_sham: OLMo (no menus in the stored transcript) -- headers and label copies redacted only",
        ros["transcript"] == redacted_expect(os_, {"Velvet, then up.": "[config], then up."}))
    chk("redact_sham: no menu or pick piece, no menu template text, no original menu string survives",
        not any(p["kind"] in ("menu", "pick") for x in (rs_, ros) for p in x["pieces"])
        and "Config choice (one word):" not in rs_["transcript"]
        and not any(c["menu"] in rs_["transcript"] for c in qs["choices"])
        and "| choice]" not in rs_["transcript"])
    precise = True
    for red, src in ((rs_, qs), (ros, os_)):
        fcut = len(forced_bytes(src))
        free_region = red["transcript"][fcut:]
        free_struct = dump([x for x in red["rounds"] if x["phase"] == "free"])
        for lab in src["cell"]["pair"]:
            n_banner = src["banner"].count(lab)
            n_forced = sum(1 for x in src["rounds"] if x["phase"] == "forced" and x["label"] == lab)
            precise &= (lab.lower() not in free_region.lower() and lab.lower() not in free_struct.lower()
                        and red["transcript"].count(lab) == n_banner + n_forced
                        and red["transcript"][:fcut].count(lab) == n_banner + n_forced
                        and n_banner == 1 and n_forced == 2)
        precise &= free_region.count(f": {REDACTED_TAG}]") == len(src["choices"])
    chk("redact_sham: pick labels appear nowhere in free-round text; only banner (1 each) + forced headers (2 each)",
        precise)
    ptile = all(p["start"] == (red["pieces"][i - 1]["end"] if i else 0)
                for red in (rs_, ros) for i, p in enumerate(red["pieces"])) and \
        all(red["pieces"][-1]["end"] == len(red["transcript"]) for red in (rs_, ros)) and \
        all(red["transcript"][p["start"]:p["end"]] == x["text"] for red in (rs_, ros) for p in red["pieces"]
            for x in red["rounds"] if p["kind"] == "generation" and x["phase"] == p["phase"]
            and x.get("ci" if p["phase"] == "free" else "ri") == p["idx"])
    chk("redact_sham: redacted pieces tile the redacted transcript; generation pieces equal round texts", ptile)
    rkeys = {k for x in (rs_, ros) for k, _ in _walk(x) if k is not None}
    free_rounds = [x for red in (rs_, ros) for x in red["rounds"] if x["phase"] == "free"]
    chk("redact_sham: picks, choices, reads, menus, first pick removed; free item/label/role/property/task/seed "
        "and audit detail/lexical_raw dropped; sham classes kept",
        not (rkeys & _FREE_ONLY_KEYS) and "read" not in dump(rs_)
        and all(set(x) <= set(_FREE_ROUND_KEEP) and set(x["audit"]) <= set(_AUDIT_KEEP) for x in free_rounds)
        and [x["audit"]["claim"] for x in rs_["rounds"] if x["phase"] == "free"]
        == [None, "v2", "echo", None, "lexical"]
        and rs_["exclusion"] == {"class": "lexical", "phase": "free"}
        and rs_["excluded"] is True and rs_["seconds"] == 88.0,
        sorted(rkeys & _FREE_ONLY_KEYS))
    t_lab = build("olmo", False, 2, f_clean, [("P", "Hot.", None), ("Q", "Up.", None)], pair=OP, pair_index=0,
                  task_override={1: "Write the opposite of quartz."})
    t_hdr = copy.deepcopy(os_)
    t_hdr["choices"][1]["pick"] = OP[0]
    chk("redact_sham: refuses a contrast record, a free task line naming a label, a header not ending in "
        "its pick, an already-blinded record",
        all(refuses(lambda r=r: redact_sham(r)) for r in (qa, oa, t_lab, t_hdr, rs_))
        and not refuses(lambda: redact_sham(qs2)))

    # ------------------------------------------------ printed_reason
    @dataclass(frozen=True)
    class _RA:
        substrate: str
        phase: str
        claim: str | None

    forced_q = [printed_reason({"class": c, "phase": "forced", "detail": "lexical:slate"}, c == "v2")
                for c in CLAIMS["qwen"]]
    forced_o = [printed_reason(_RA("olmo", "forced", c), True) for c in CLAIMS["olmo"]]
    chk("printed_reason: forced forms audit/echo/content/lexical (Qwen v2 -> audit; OLMo AuditSpec -> audit)",
        forced_q == ["audit@forced", "echo@forced", "content@forced", "lexical@forced"]
        and forced_o == ["audit@forced", "echo@forced", "lexical@forced"]
        and printed_reason({"class": "audit", "phase": "forced"}, False) == "audit@forced", forced_q + forced_o)
    sham_free = [printed_reason(_RA("qwen", "free", c), False) for c in CLAIMS["qwen"]] + \
        [printed_reason(audit_d("olmo", "free", c, "velvet"), False) for c in CLAIMS["olmo"]]
    con_free = [printed_reason(_RA("qwen", "free", c), True) for c in CLAIMS["qwen"]] + \
        [printed_reason({"class": c, "phase": "free", "detail": "lexical:velvet"}, True) for c in CLAIMS["olmo"]]
    chk("printed_reason: free sham {class}@free; free contrast excluded@free for every class",
        sham_free == ["audit@free", "echo@free", "content@free", "lexical@free",
                      "audit@free", "echo@free", "lexical@free"]
        and set(con_free) == {"excluded@free"}, sham_free)
    recs_pr = [printed_reason(qb, True), printed_reason(qc, True), printed_reason(qs, False),
               printed_reason(ob, True), printed_reason(os_, False)]
    chk("printed_reason: from records (contrast free -> excluded@free; forced content; sham free lexical)",
        recs_pr == ["excluded@free", "content@forced", "lexical@free", "excluded@free", "lexical@free"], recs_pr)
    outs = forced_q + forced_o + sham_free + con_free + recs_pr
    chk("printed_reason: never a digit index or a tag (all outputs; every input carried a tag in detail)",
        all(_PRINTED_RX.fullmatch(o) and not re.search(r"\d", o) and not any(x in o for x in all_labels)
            for o in outs))
    chk("printed_reason: refuses a valid session, a contrast flag disagreeing with the record, an unknown class "
        "or phase, OLMo content, no claim, a non-bool contrast",
        refuses(lambda: printed_reason(qa, True)) and refuses(lambda: printed_reason(qb, False))
        and refuses(lambda: printed_reason(qs, True)) and refuses(lambda: printed_reason({"class": "junk", "phase": "forced"}, False))
        and refuses(lambda: printed_reason({"class": "echo", "phase": "free0"}, False))
        and refuses(lambda: printed_reason(_RA("olmo", "forced", "content"), False))
        and refuses(lambda: printed_reason(_RA("olmo", "forced", "v2"), False))
        and refuses(lambda: printed_reason(_RA("qwen", "forced", None), False))
        and refuses(lambda: printed_reason({"class": "echo", "phase": "forced"}, 1), (TypeError,))
        and refuses(lambda: printed_reason(object(), True), (TypeError,)))

    # ------------------------------------------------ session_line
    lines = [session_line(r) for r in (qa, qb, qb2, qc, qs, qs2, oa, ob, os_)]
    want = ["qual A0 s=3 valid", "qual A0 s=3 excluded:excluded@free", "qual A0 s=3 valid",
            "qual A0 s=5 excluded:content@forced", "qual A0s s=3 excluded:lexical@free", "qual A0s s=3 valid",
            "qual A0-OLMo-dpo s=2 valid", "qual A0-OLMo-dpo s=2 excluded:excluded@free",
            "qual A0s-OLMo-dpo s=2 excluded:lexical@free"]
    chk("session_line: the declared form for valid / forced / free sham / free contrast (both substrates)",
        lines == want, lines)
    banned = ("read", "complete", "truncat", "second", "sec", "first", "pick", ".") + all_labels
    chk("session_line: no seconds, read count, completeness word or pick in any line",
        all(_LINE_RX.fullmatch(x) and not any(b in x.lower() for b in banned)
            and str(r["seconds"]) not in x and str(len(r["choices"])) not in x.split("s=")[1][1:]
            for x, r in zip(lines, (qa, qb, qb2, qc, qs, qs2, oa, ob, os_))), lines)
    t_l1 = copy.deepcopy(qa)
    t_l1["excluded"] = True
    t_l2 = copy.deepcopy(qa)
    t_l2["stage"] = "pilot"
    t_l3 = copy.deepcopy(qa)
    t_l3["s"] = "3"
    t_l4 = copy.deepcopy(qc)
    t_l4["excluded"] = False
    chk("session_line: refuses excluded without a reason, a reason without excluded, an unknown stage, a non-int s",
        all(refuses(lambda r=r: session_line(r)) for r in (t_l1, t_l2, t_l3, t_l4)))

    # ------------------------------------------------ stage_report
    rep_a, rep_b, rep_b2 = (stage_report([qs, r]) for r in (qa, qb, qb2))
    rep_oa, rep_ob = stage_report([os_, oa]), stage_report([os_, ob])
    chk("stage_report: contrast sessions identical in forced rounds, different in free rounds -> identical reports",
        dump(rep_a) == dump(rep_b) == dump(rep_b2) and dump(rep_oa) == dump(rep_ob)
        and dump(stage_report([qa])) == dump(stage_report([qb])))
    cb = rep_b["templates"]["A0"]
    ckeys = {k for k, _ in _walk(cb) if k is not None}
    chk("stage_report: contrast block = forced counts only; free events withheld as a constant, no count",
        cb["forced"]["rounds"] == 4 and cb["sessions"] == 1 and cb["domain_sessions"] == 1
        and cb["free_rounds"] == WITHHELD and cb["hair_triggers"] == []
        and not (ckeys & {"first_pick_P", "reads", "free", "all", "valid_sessions", "excluded_sessions",
                          "complete_sessions", "strict_excluded_sessions"}), sorted(ckeys))
    rc = stage_report([qa, qc])["templates"]["A0"]
    chk("stage_report: contrast forced exclusions by printed class (content@forced = 1), domain from forced",
        rc["excluded_at_forced"] == {"audit@forced": 0, "echo@forced": 0, "content@forced": 1, "lexical@forced": 0}
        and rc["sessions_excluded_at_forced"] == 1 and rc["domain_sessions"] == 1 and rc["sessions"] == 2
        and rc["forced"]["rounds"] == 6 and rc["forced"]["claims"]["content"] == 1, rc["excluded_at_forced"])
    sh = rep_a["templates"]["A0s"]
    sh2 = stage_report([qs2])["templates"]["A0s"]
    chk("stage_report: sham block reports free-round classes and first-pick share, and changes with free rounds",
        sh["free"]["claims"] == {"v2": 1, "echo": 1, "content": 0, "lexical": 1}
        and sh["free"]["degeneracy_rounds"] == 2 and sh["all"]["audit_categories"]["frame"] == 1
        and sh["excluded_sessions"]["lexical@free"] == 1 and sh["first_pick_P"] == {"k": 1, "n": 1, "share": "1"}
        and sh2["first_pick_P"] == {"k": 0, "n": 1, "share": "0"} and sh2["valid_sessions"] == 1
        and sh2["reads"] == {"n": 6, "low_label_mass": 1, "top1_not_label": 1}
        and sh["first_pick_P_by_pair"] == {"1": {"k": 1, "n": 1, "share": "1"}}
        and dump(stage_report([qs, qa])) != dump(stage_report([qs2, qa])))
    so = rep_ob["templates"]["A0s-OLMo-dpo"]
    chk("stage_report: OLMo sham block by OLMo classes (audit/echo/lexical); no label anywhere in any report",
        so["free"]["claims"] == {"audit": 0, "echo": 0, "lexical": 1}
        and so["excluded_sessions"]["lexical@free"] == 1
        and all(not any(x in dump(rp).lower() for x in all_labels)
                for rp in (rep_a, rep_b, rep_b2, rep_oa, rep_ob, sh2)))
    t_dom = copy.deepcopy(qa)
    t_dom["domain"] = False
    t_fp = copy.deepcopy(qs2)
    t_fp["first_free_pick_P"] = True
    chk("stage_report: refuses mixed units, mixed stages, duplicate (template, s), blinded records, no records, "
        "a domain field contradicting the forced rounds, a first pick contradicting the first choice",
        refuses(lambda: stage_report([qa, oa])) and refuses(lambda: stage_report([qa, dict(qs, stage="time",
                                                                                             keys=qs["keys"])]))
        and refuses(lambda: stage_report([qa, copy.deepcopy(qa)])) and refuses(lambda: stage_report([sa]))
        and refuses(lambda: stage_report([])) and refuses(lambda: stage_report([t_dom]))
        and refuses(lambda: stage_report([t_fp])))
    # The no-label check: keys by equality (and whole word), values by whole word,
    # case-insensitive, at lexical_hit's boundary -- never a bare substring.
    from unittest import mock
    me, orig_sham = sys.modules[__name__], _sham_block

    def report_with(extra: dict):
        def wrapped(rs, sub):
            return {**orig_sham(rs, sub), **extra}
        with mock.patch.object(me, "_sham_block", wrapped):
            return stage_report([qs, qa])

    chk("stage_report: refuses a roster label as a value word, as a key, and as a whole word in a key",
        refuses(lambda: report_with({"note": "config Slate ran first"}))
        and refuses(lambda: report_with({"PRISM": 1}))
        and refuses(lambda: report_with({"slate@free": 1}))
        and refuses(lambda: report_with({"nested": [{"x": "prism."}]}))
        and refuses(lambda: _assert_no_label({"a": ["Granite"]}, ["granite"]))
        and refuses(lambda: _assert_no_label({"granite": 0}, ["granite"])))
    try:
        sub_ok = report_with({"note": "prisms and slates", "slates": 1, "reprism": "slated"})
        sub_ok = sub_ok["templates"]["A0s"]["note"] == "prisms and slates"
        _assert_no_label({"granites": "granites", "x": ["regranite", "granite_count"]}, ["granite"])
    except ValueError as e:
        sub_ok = str(e)
    chk("stage_report: a label only as a substring of a key or value word ('granites' vs 'granite') passes",
        sub_ok is True, sub_ok)

    # ------------------------------------------------ release_full
    before = dump(every)
    rel = release_full(every)
    chk("release_full: returns the records unchanged (same object, same bytes)",
        rel is every and dump(rel) == before)

    # ------------------------------------------------ source hygiene
    import inspect
    src = inspect.getsource(sys.modules[__name__])
    forbidden = ("choice_read_" + "statepresent", "(1" + "0) the", "slip (1" + "0)",
                 "_new_" + "qwen_adapter", "def qwen_" + "or_explain", "Inj" + "ection")
    chk("readrule: source free of the forbidden names; the quarantined module is not imported",
        not any(f in src for f in forbidden) and ("valence_core.e2b." + "statepresent") not in sys.modules)
