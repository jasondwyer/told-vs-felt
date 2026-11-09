"""PROPOSAL-p's stored-text invariant (p v0.2 §2.2; the design seat's answers of 2026-11-07, Q2, reading (b)).

*No stored text contains a line break.* Enforced on the adapter's RETURNED result, through ``StoredTextProxy``, with
``valence_core/adapters/olmo_hf.py`` unedited and the adapter's stop rule m's, unchanged:

  - a result whose text has no line break is returned exactly as the adapter returned it (the same object), stop-token
    handling included (the stop token dropped whole, as today);
  - a result whose text contains a line break is cut at its first line break: the text before it; the token ids up to
    and including the first token whose cumulative decoded text holds a line break after content; ``stop_reason``
    ``newline``; ``cap_hit`` false;
  - a newline before any content does not stop generation, as today (the adapter strips its decoded text, so such a
    newline never reaches the returned text; olmo_hf.py:286).

Nothing after the cut is part of the stored text, graded, or seen by any later round; the returned text is logged
beside it, for the read (§2.2 as the seat's ruling of 2026-11-07 reads it, F-p10). Every cut is logged on the proxy
(``cuts``) for the stage's record: the stored text as ``stored_text`` and the adapter's returned text, the part after
the break included, as ``returned_text`` -- a DIAGNOSTIC field (``DIAGNOSTIC_FIELDS``), excluded by name from the hair
trigger's domain (which reads a record's ``text`` field only), from the grader, from every later round's prompt and
from the read rule's stored text. A ProxyStop carries the returned text whole as ``returned_text`` too. The proxy
delegates every other attribute to the adapter -- m's code reads adapters by duck typing (``path``, ``choice_window``,
``provenance()``) -- so ``provenance()`` and with it the backend identifier are the adapter's, untouched.

PIN (Code, declared at the p BUILD): "line break" is ``\\n`` or ``\\r`` (§2.3's hair trigger reads both); the cut text
is the text before the first line break with trailing whitespace removed, as the adapter strips its own decoded text
(olmo_hf.py:286), so a cut text is what the adapter would have returned had its stop fired at that break.

PIN (Code, declared at step 6): the proxy logs every call -- its index, the call's seed, the stored text's sha256 and
the cut event or none -- in ``calls``, and hands each record, as it happens, to ``on_call`` when one is given (a gate
stage's write-ahead call log). A STOP's message carries no text and no call index: a stage's call may be a contrast
free round's, whose text names the pick (m:318), so the text, the returned text and the call are carried on the
exception (``stored_text``, ``returned_text``, ``call``) and logged as the call's record, withheld with the log; the
message names the STOP alone and is printed verbatim (the seat's Q5).
"""
from __future__ import annotations

import dataclasses
import hashlib
from typing import Any, Callable

LINE_BREAKS = ("\n", "\r")
#: The diagnostic fields of a cut event and of a STOP record: logged for the seat's read, never stored text (F-p10).
DIAGNOSTIC_FIELDS = ("returned_text",)
PROXY_ID = ("valence_core.p.proxy.StoredTextProxy (p v0.2 §2.2, the seat's reading (b)): the adapter's returned "
            "result cut at its first line break; olmo_hf.py unedited")


class ProxyStop(SystemExit):
    """A STOP at the proxy: the returned text's line break cannot be placed on its token ids, or §2.3's hair trigger on
    a stored text. The message names the STOP alone; ``returned_text`` (diagnostic), ``stored_text`` and ``call`` carry
    the detail (the module docstring's PIN)."""

    def __init__(self, msg: str, returned_text: str | None = None, *, stored_text: str | None = None,
                 call: int | None = None) -> None:
        super().__init__(msg)
        self.returned_text = returned_text
        self.stored_text = stored_text
        self.call = call
        self.log_error: str | None = None


def has_line_break(text: str) -> bool:
    return any(c in text for c in LINE_BREAKS)


def _first_break(text: str) -> int:
    return min(i for i in (text.find(c) for c in LINE_BREAKS) if i >= 0)


def _break_after_content(s: str) -> bool:
    k = next((q for q, ch in enumerate(s) if not ch.isspace()), None)
    return k is not None and has_line_break(s[k:])


def cut_result(adapter: Any, g: Any) -> tuple[Any, dict | None]:
    """(the stored result, the cut event or None) under reading (b)."""
    text = str(g.text)
    if not has_line_break(text):
        return g, None
    ids = [int(t) for t in g.token_ids]
    at = next((t + 1 for t in range(len(ids)) if _break_after_content(adapter.decode(ids[:t + 1]))), None)
    if at is None:
        raise ProxyStop("PROXY STOP: the returned text holds a line break that no prefix of its token ids decodes to "
                        "after content; the boundary is not reconstructible (the text is carried on the STOP, a "
                        "diagnostic field, never in its message)", returned_text=text)
    cut = text[:_first_break(text)].rstrip()
    new = dataclasses.replace(g, text=cut, token_ids=ids[:at], cap_hit=False, stop_reason="newline")
    return new, {"returned_text": text, "stored_text": cut, "n_tok_returned": len(ids), "n_tok_stored": at,
                 "stop_reason_returned": str(g.stop_reason), "cap_hit_returned": bool(g.cap_hit)}


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class StoredTextProxy:
    """The adapter, with ``generate`` returning reading (b)'s stored result; ``on_call`` (optional) receives each
    call's record as it happens (the module docstring's PIN)."""

    def __init__(self, adapter: Any, on_call: Callable[[dict], None] | None = None) -> None:
        object.__setattr__(self, "_adapter", adapter)
        object.__setattr__(self, "cuts", [])
        object.__setattr__(self, "calls", [])
        object.__setattr__(self, "n_generate", 0)
        object.__setattr__(self, "_on_call", on_call)

    def __getattr__(self, name: str) -> Any:
        return getattr(object.__getattribute__(self, "_adapter"), name)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("StoredTextProxy is read-only; set attributes on the adapter")

    def _log(self, rec: dict) -> None:
        object.__getattribute__(self, "calls").append(rec)
        hook = object.__getattribute__(self, "_on_call")
        if hook is not None:
            hook(rec)

    def generate(self, prefix_text: str, segment_text: str, injections=(), **kw) -> Any:
        a = object.__getattribute__(self, "_adapter")
        g = a.generate(prefix_text, segment_text, injections, **kw)
        n = object.__getattribute__(self, "n_generate")
        object.__setattr__(self, "n_generate", n + 1)
        seed = kw.get("seed")
        try:
            out, ev = cut_result(a, g)
            stored_text_check(str(out.text), returned_text=str(g.text), call=n)
        except ProxyStop as e:
            if e.call is None:
                e.call = n
            try:
                self._log({"call": n, "seed": seed, "stop": {"message": str(e), "returned_text": e.returned_text,
                                                             "stored_text": e.stored_text}})
            except Exception as le:                 # the STOP propagates whatever the log does (round 3's m-1)
                e.log_error = f"{type(le).__name__}: {le}"
            raise
        if ev is not None:
            object.__getattribute__(self, "cuts").append({"call": n, **ev})
        self._log({"call": n, "seed": seed, "text_sha256": text_sha256(str(out.text)), "cut": ev})
        return out


def stored_text_check(text: str, *, returned_text: str | None = None, call: int | None = None) -> None:
    """§2.3's hair trigger at the proxy (the seat's answer of 2026-11-08, Q5): every stored text the proxy returns is
    checked, and a line break is a STOP -- unreachable by construction (a cut text is the text before the first
    break, stripped). Raised inside m's session, it ends the stage as an exception, without m's stop record; the
    driver prints it verbatim and the seat adjudicates before anything resumes."""
    if has_line_break(text):
        raise ProxyStop("HAIR TRIGGER line_break_in_stored_text (p §2.3) at the proxy: a stored text holds a line break "
                        "(the text, the returned text and the call are carried on the STOP and logged with the "
                        "stage's call log, never in its message: m:318)", returned_text=returned_text,
                        stored_text=text, call=call)


def _selftest(chk) -> None:
    import numpy as np
    from ..adapters.base import GenerateResult
    from . import testing

    class Fixed:
        """An adapter returning one prepared result object, with a weights path and a read window."""
        path, choice_window = "/workspace/models/sft", 4096

        def __init__(self, g):
            self.g = g

        def generate(self, prefix_text, segment_text, injections=(), **kw):
            return self.g

        def provenance(self):
            return {"adapter": "fixed"}

    raw = GenerateResult(text="Cold.", token_ids=[5, 6, 7], first_logits=np.zeros(2, dtype=np.float32),
                         cap_hit=True, stop_reason="cap")
    fx = StoredTextProxy(Fixed(raw))
    chk("proxy: a result with no line break is the adapter's own object, unchanged (a cap hit and its stop reason "
        "kept), and nothing is logged as a cut", fx.generate("B\n", "Task: x\nResponse:", seed=1) is raw
        and raw.cap_hit is True and raw.stop_reason == "cap" and fx.cuts == [])
    chk("proxy: every other attribute is the adapter's -- the weights path, the read window and provenance() read "
        "through", fx.path == "/workspace/models/sft" and fx.choice_window == 4096 and fx.provenance() == {"adapter": "fixed"})
    a = testing.CharScriptedAdapter("p-proxy-selftest")
    px = StoredTextProxy(a)
    a.load(["77", "---\n\nTask: Write the opposite of 'enter", "foo  \rbar", "  lead\nx"])
    g0 = px.generate("B\n", "Task: x\nResponse:", seed=1)
    g1 = px.generate("B\n", "Task: x\nResponse:", seed=2)
    g2 = px.generate("B\n", "Task: x\nResponse:", seed=3)
    g3 = px.generate("B\n", "Task: x\nResponse:", seed=4)
    chk("proxy: on the character double, a result with no line break is stored as returned and the call counter "
        "counts every call", g0.text == "77" and g0.token_ids == a.encode("77", add_special_tokens=False)
        and px.n_generate == 4)
    ids1 = a.encode("---\n\nTask: Write the opposite of 'enter", add_special_tokens=False)
    want_at = next(t + 1 for t in range(len(ids1)) if _break_after_content(a.decode(ids1[:t + 1])))
    chk("proxy: gcal's DPO/instruct case -- '---\\n\\nTask: ...' is stored as '---', its token ids through the token "
        "that carried the break, stop newline, cap false",
        g1.text == "---" and g1.token_ids == ids1[:want_at] and g1.stop_reason == "newline" and g1.cap_hit is False,
        (g1.text, len(g1.token_ids), want_at))
    chk("proxy: '\\r' is a line break (the stored text is 'foo', trailing whitespace stripped as the adapter strips)",
        g2.text == "foo" and not has_line_break(g2.text), g2.text)
    chk("proxy: no stored text carries a line break; three cuts logged with the returned and stored forms",
        not any(has_line_break(g.text) for g in (g0, g1, g2, g3)) and len(px.cuts) == 3
        and [c["call"] for c in px.cuts] == [1, 2, 3] and px.cuts[0]["returned_text"].startswith("---\n")
        and px.cuts[0]["stored_text"] == "---" and DIAGNOSTIC_FIELDS == ("returned_text",), px.cuts)
    c = testing.ChunkScriptedAdapter("p-proxy-chunk")
    cx = StoredTextProxy(c)
    c.load(["---\n\nTask: Write the opposite of 'enter"])
    gc = cx.generate("B\n", "Task: x\nResponse:", seed=5)
    cids = c.encode("---\n\nTask: Write the opposite of 'enter", add_special_tokens=False)
    chk("proxy: when '---\\n\\n' is ONE token (as on OLMo's tokenizer), the stored text is '---' and the stored ids "
        "are that one token (n_tok 1), stop newline, cap false",
        gc.text == "---" and gc.token_ids == cids[:1] and len(cids) == 2 and c.decode(cids[:1]) == "---\n\n"
        and gc.stop_reason == "newline" and gc.cap_hit is False, (gc.text, gc.token_ids, cids))
    try:
        px.cuts = []
        ro = False
    except AttributeError:
        ro = True
    chk("proxy: the proxy is read-only (attributes are set on the adapter, never on the proxy)", ro)
    from ..m import testing as m_testing
    w = m_testing.OLMoScriptedAdapter("p-proxy-wordhash")
    w.load(["---\n\nx"])
    try:
        StoredTextProxy(w).generate("B\n", "Task: x\nResponse:")
        stopped = False
    except ProxyStop:
        stopped = True
    chk("proxy: a tokenizer whose decode cannot place the break is a STOP, never a guessed cut", stopped)
    caught = []
    for t, rt in (("ok", None), ("a\nb", "a\nb tail"), ("a\rb", None)):
        try:
            stored_text_check(t, returned_text=rt, call=7)
            caught.append("passed")
        except ProxyStop as e:
            caught.append(("stopped", "line_break_in_stored_text" in str(e), e.returned_text))
    chk("proxy: the stored-text check (the seat's Q5) passes a text with no line break and STOPs on \\n or \\r, naming "
        "§2.3's trigger and carrying the returned text (diagnostic)",
        caught == ["passed", ("stopped", True, "a\nb tail"), ("stopped", True, None)], caught)
    msgs = []
    for t in ("secret\nzebra",):
        try:
            stored_text_check(t, returned_text=t + " tail", call=11)
        except ProxyStop as e:
            msgs.append((str(e), e.stored_text, e.returned_text, e.call))
    w2 = m_testing.OLMoScriptedAdapter("p-proxy-wordhash2")
    w2.load(["zebra\n\nx"])
    try:
        StoredTextProxy(w2).generate("B\n", "Task: x\nResponse:")
    except ProxyStop as e:
        msgs.append((str(e), e.stored_text, e.returned_text, e.call))
    chk("proxy: a STOP's message carries no text and no call index (a stage's call may be a contrast free round's, "
        "m:318); the text, the returned text and the call ride on the exception (the module docstring's PIN)",
        len(msgs) == 2 and all("zebra" not in m and "11" not in m and "secret" not in m for m, *_ in msgs)
        and msgs[0][1:] == ("secret\nzebra", "secret\nzebra tail", 11) and msgs[1][2] == "zebra\n\nx"
        and msgs[1][3] == 0, msgs)
    seen = []
    a3 = testing.CharScriptedAdapter("p-proxy-log")
    p3 = StoredTextProxy(a3, on_call=seen.append)
    a3.load(["77", "a\nb"])
    p3.generate("B\n", "Task: x\nResponse:", seed=101)
    p3.generate("B\n", "Task: x\nResponse:", seed=102)
    w3 = m_testing.OLMoScriptedAdapter("p-proxy-log-stop")
    w3.load(["q\n\nx"])
    p4 = StoredTextProxy(w3, on_call=seen.append)
    try:
        p4.generate("B\n", "Task: x\nResponse:", seed=103)
    except ProxyStop:
        pass
    chk("proxy: every call is logged as it happens -- index, seed, the stored text's sha256 and the cut event or none; "
        "a STOP's call logged with its detail before it propagates",
        [r["seed"] for r in seen] == [101, 102, 103] and seen[0]["cut"] is None
        and seen[0]["text_sha256"] == text_sha256("77") and seen[1]["cut"]["stored_text"] == "a"
        and seen[1]["text_sha256"] == text_sha256("a") and seen[2]["stop"]["returned_text"] == "q\n\nx"
        and p3.calls == seen[:2] and p4.calls == seen[2:], seen)
