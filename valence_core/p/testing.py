"""PROPOSAL-p test doubles. SELFTEST-ONLY: no production p module imports this file at module level (``guard``
asserts it); the self-tests import it inside their own ``_selftest`` functions.

``CharScriptedAdapter`` is m's ``OLMoScriptedAdapter`` (scripted generations, the stub's provenance mark) with a
character tokenizer -- ids are code points + 1, so ``decode`` inverts ``encode`` on every prefix. The proxy's cut
(p §2.2) locates the token that carried a line break by decoding id prefixes, which m's word-hash stub cannot
support (its ``decode`` returns ``<id>`` placeholders); a real tokenizer decodes prefixes to text, as this one does.
"""
from __future__ import annotations

import dataclasses
import re
from typing import Sequence

from ..m import testing as m_testing


class CharScriptedAdapter(m_testing.OLMoScriptedAdapter):
    def __init__(self, stage: str = "p-char-scripted") -> None:
        super().__init__(stage)

    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        return [ord(c) + 1 for c in text]

    def decode(self, ids: Sequence[int]) -> str:
        return "".join(chr(int(i) - 1) for i in ids if int(i) > 0)

    def generate(self, prefix_text: str, segment_text: str, injections=(), **kw):
        g = super().generate(prefix_text, segment_text, injections, **kw)
        return dataclasses.replace(g, token_ids=[ord(c) + 1 for c in g.text])


class ChunkScriptedAdapter(m_testing.OLMoScriptedAdapter):
    """m's scripted OLMo double with a multi-character tokenizer: a token is a run of non-newline characters followed
    by its newlines (``---\\n\\n`` is one token, as on OLMo's tokenizer), or a final run; ids index a vocabulary
    grown on first sight, so ``decode`` inverts ``encode`` on every token boundary."""

    _CHUNK = re.compile(r"[^\n]*\n+|[^\n]+")

    def __init__(self, stage: str = "p-chunk-scripted") -> None:
        super().__init__(stage)
        self._vocab: dict[str, int] = {}
        self._inv: dict[int, str] = {}

    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        out = []
        for ch in self._CHUNK.findall(text):
            if ch not in self._vocab:
                self._vocab[ch] = len(self._vocab) + 1
                self._inv[self._vocab[ch]] = ch
            out.append(self._vocab[ch])
        return out

    def decode(self, ids: Sequence[int]) -> str:
        return "".join(self._inv.get(int(i), "") for i in ids)

    def generate(self, prefix_text: str, segment_text: str, injections=(), **kw):
        g = super().generate(prefix_text, segment_text, injections, **kw)
        return dataclasses.replace(g, token_ids=self.encode(g.text, add_special_tokens=False))
