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

Nothing after the cut is stored, graded or seen by any later round; every cut is logged on the proxy (``cuts``) for the
stage's record. The proxy delegates every other attribute to the adapter -- m's code reads adapters by duck typing
(``path``, ``choice_window``, ``provenance()``) -- so ``provenance()`` and with it the backend identifier are the
adapter's, untouched.

PIN (Code, declared at the p BUILD): "line break" is ``\\n`` or ``\\r`` (§2.3's hair trigger reads both); the cut text
is the text before the first line break with trailing whitespace removed, as the adapter strips its own decoded text
(olmo_hf.py:286), so a cut text is what the adapter would have returned had its stop fired at that break.
"""
from __future__ import annotations

import dataclasses
from typing import Any

LINE_BREAKS = ("\n", "\r")
PROXY_ID = ("valence_core.p.proxy.StoredTextProxy (p v0.2 §2.2, the seat's reading (b)): the adapter's returned "
            "result cut at its first line break; olmo_hf.py unedited")


class ProxyStop(SystemExit):
    """The returned text's line break cannot be placed on its token ids; ``text`` carries the returned text whole."""

    def __init__(self, msg: str, text: str | None = None) -> None:
        super().__init__(msg)
        self.text = text


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
        raise ProxyStop(f"PROXY STOP: the returned text holds a line break that no prefix of its token ids decodes "
                        f"to after content ({text[:200]!r}); the boundary is not reconstructible", text=text)
    cut = text[:_first_break(text)].rstrip()
    new = dataclasses.replace(g, text=cut, token_ids=ids[:at], cap_hit=False, stop_reason="newline")
    return new, {"text_returned": text, "text_stored": cut, "n_tok_returned": len(ids), "n_tok_stored": at,
                 "stop_reason_returned": str(g.stop_reason), "cap_hit_returned": bool(g.cap_hit)}


class StoredTextProxy:
    """The adapter, with ``generate`` returning reading (b)'s stored result."""

    def __init__(self, adapter: Any) -> None:
        object.__setattr__(self, "_adapter", adapter)
        object.__setattr__(self, "cuts", [])
        object.__setattr__(self, "n_generate", 0)

    def __getattr__(self, name: str) -> Any:
        return getattr(object.__getattribute__(self, "_adapter"), name)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("StoredTextProxy is read-only; set attributes on the adapter")

    def generate(self, prefix_text: str, segment_text: str, injections=(), **kw) -> Any:
        a = object.__getattribute__(self, "_adapter")
        g = a.generate(prefix_text, segment_text, injections, **kw)
        n = object.__getattribute__(self, "n_generate")
        object.__setattr__(self, "n_generate", n + 1)
        out, ev = cut_result(a, g)
        if ev is not None:
            object.__getattribute__(self, "cuts").append({"call": n, **ev})
        return out


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
        and [c["call"] for c in px.cuts] == [1, 2, 3] and px.cuts[0]["text_returned"].startswith("---\n"), px.cuts)
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
