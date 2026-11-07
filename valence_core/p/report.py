"""PROPOSAL-p's descriptive counters and its line-break hair trigger (p v0.2 §2.3).

The hair trigger ``line_break_in_stored_text`` -- any stored text in any p session or gate containing ``\\n`` or
``\\r`` -- domain every session and every G-CAL-p generation; a fire STOPs the stage (rule 21; zero base rate by
construction once §2.2's proxy stands). The counters are computed by this tool over the records (the analyzer
unchanged for them), tabulated over every generation, reported in the gate and VERDICTS entries, deciding nothing
(rule 23):

  control_chars       texts holding a control character other than a line break (the DEL of gcal instruct 7 s1)
  harness_first_line  texts whose first line is harness-shaped: m:258's eight declared strings (placeholders as
                      wildcards), the seven listed forms, or any line of the form ``=== ... ===``
  cap_hits            records with cap_hit
  refusals            ``I'm sorry`` / ``I cannot`` / ``I can't`` forms
  corrupted_spelling  a word of the text within Levenshtein distance 2 of a gold and not equal to it (class (c) of
                      p §0.3)

PIN (Code, declared at the p BUILD): control characters are Unicode category Cc minus ``\\n`` and ``\\r`` (tab
included); the listed forms and m:258's patterns match at the start of the first line, case as written; refusals match
case-insensitively, straight or curly apostrophe. corrupted_spelling is §2.3's rule as written -- a word of the stored
text within Levenshtein distance 2 of a gold and not equal to it -- with one reading: a word is §1.1's (a maximal run of
ASCII letters, case-insensitive), and a gold variant is compared only when it is itself one such word (a digit string
has no spelling, and ``twenty-four`` is two words under §1.1). FLAG for the seat (descriptive, decides nothing): on
G-CAL-OLMo's 384 committed records the rule counts 4/10/9 records (sft/dpo/instruct), 23 in all. Five are p §0.3's
class (c) (``Januwy`` x2, ``Janaury``, ``dn`` x2) and one is a misspelling of the model's own (``irom``, instruct item
7 s1); the other 17, four of them clean-pool records, count only a common word within distance 2 of a short gold
(``the``/``two``, ``the``/``three``, ``true``/``three``, ``on``/``iron``, ``in``/``iron``, ``do``/``down``), one of them
borderline (sft item 11 s2 gives ``do`` as its answer). ``Janbaa``, ``Janyooar`` and ``Ther qro abov two dsys in a
wemk``, class (c) by p §0.3, have no word within distance 2 of a gold and are not counted.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Mapping, Sequence

from ..m import banner
from .proxy import has_line_break

LISTED_FORMS = ("### Response:", "Regenerate.", "[PROLOGUE", "Correctness:", "Reasoning:", "Answer:", "Input:")
_BANNER_RX = tuple(re.compile(re.escape(s).replace(r"\{L_clean\}", ".+?").replace(r"\{L_corr\}", ".+?")
                              .replace(r"\{L_a\}", ".+?").replace(r"\{L_b\}", ".+?").replace(r"\{n\}", ".+?"))
                   for s in banner.DECLARED_HARNESS_STRINGS)
_FENCE = re.compile(r"===.*===")
_REFUSAL = re.compile(r"\bI['’]m sorry\b|\bI cannot\b|\bI can['’]t\b", re.IGNORECASE)
_WORD = re.compile(r"[A-Za-z]+")
COUNTERS = ("control_chars", "harness_first_line", "cap_hits", "refusals", "corrupted_spelling")


def line_break_in_stored_text(text: str) -> bool:
    """§2.3's hair trigger predicate."""
    return has_line_break(text)


def control_chars(text: str) -> bool:
    return any(unicodedata.category(c) == "Cc" and c not in "\n\r" for c in text)


def harness_first_line(text: str) -> bool:
    first = re.split(r"[\r\n]", text, maxsplit=1)[0]
    return (any(first.startswith(f) for f in LISTED_FORMS) or any(rx.match(first) for rx in _BANNER_RX)
            or bool(_FENCE.fullmatch(first.strip())))


def refusal(text: str) -> bool:
    return bool(_REFUSAL.search(text))


def levenshtein(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def corrupted_spelling(text: str, gold: Sequence[str]) -> bool:
    words = [w.lower() for w in _WORD.findall(text)]
    golds = [g.lower() for g in gold if re.fullmatch(r"[A-Za-z]+", g)]
    return any(w != g and levenshtein(w, g) <= 2 for g in golds for w in words)


def counters(records: Sequence[Mapping[str, Any]], pool: Sequence[Mapping[str, Any]]) -> dict:
    """Each counter's count and the keys it counts (pool, i, seed_index), over every record given."""
    def key(r):
        return f"{r['pool']} i={r['i']} s={r['seed_index']}"
    out = {}
    for name, fn in (("control_chars", lambda r: control_chars(r["text"])),
                     ("harness_first_line", lambda r: harness_first_line(r["text"])),
                     ("cap_hits", lambda r: bool(r["cap_hit"])),
                     ("refusals", lambda r: refusal(r["text"])),
                     ("corrupted_spelling", lambda r: corrupted_spelling(r["text"], pool[r["i"]]["gold"]))):
        ks = [key(r) for r in records if fn(r)]
        out[name] = {"n": len(ks), "keys": ks}
    out["line_break_in_stored_text"] = {"n": sum(1 for r in records if line_break_in_stored_text(r["text"]))}
    out["n_records"] = len(records)
    return out


def _selftest(chk) -> None:
    chk("report: the trigger reads \\n and \\r", line_break_in_stored_text("a\nb") and line_break_in_stored_text("a\rb")
        and not line_break_in_stored_text("ab"))
    chk("report: control characters count DEL and tab, never a line break",
        control_chars("\x7fThe kernl") and control_chars("a\tb") and not control_chars("plain"))
    hs = ["=== Config evaluation session ===", "[PROLOGUE", "Regenerate.", "### Response:", "Correctness:",
          "Input: hot", "Answer:", "Reasoning:", "=== Actual module name ===", "[round 3 | reasoning]",
          "Note: config slate presents clean task text; config prism presents clean task text. Prefer clean task text."]
    nh = ["77", "cold", "The opposite of 'up' is 'down'", "Reasoning about it", "== x =="]
    chk("report: harness-shaped first lines -- m:258's patterns, the seven forms, '=== ... ===' -- and not answers",
        all(harness_first_line(t) for t in hs) and not any(harness_first_line(t) for t in nh),
        ([t for t in hs if not harness_first_line(t)], [t for t in nh if harness_first_line(t)]))
    chk("report: refusals in the three forms, either apostrophe",
        refusal("I'm sorry, but I can't assist") and refusal("I cannot compute") and refusal("I can’t")
        and not refusal("I can compute it"))
    gold8, gold2 = ["january"], ["march"]
    chk("report: corrupted spelling as §2.3 writes it -- 'Januwy' and 'Janaury' count for january, 'January' and "
        "'Janbaa' (distance 3) do not; numeric and hyphenated golds are not compared ('a' is not counted against "
        "'77'); a common word within distance 2 of a short gold counts ('the' against 'two', the FLAG's class)",
        corrupted_spelling("Januwy", gold8) and corrupted_spelling("The ftrst month of the ybaa is Janaury", gold8)
        and not corrupted_spelling("January", gold8) and not corrupted_spelling("Janbaa", gold8)
        and not corrupted_spelling("777 a", ["77"]) and not corrupted_spelling("twenty-for", ["24", "twenty-four"])
        and corrupted_spelling("Marsh", gold2) and corrupted_spelling("The bicycle has two wheels", ["2", "two"]),
        (levenshtein("janbaa", "january"), levenshtein("januwy", "january")))
    recs = [{"pool": "CORR_corrupted", "i": 8, "seed_index": 2, "text": "Januwy", "cap_hit": False},
            {"pool": "CORR_clean", "i": 2, "seed_index": 0, "text": "I'm sorry", "cap_hit": True}]
    pool = [{"gold": ["x"]}] * 2 + [{"gold": ["march"]}] + [{"gold": ["x"]}] * 5 + [{"gold": ["january"]}] + \
        [{"gold": ["x"]}] * 7
    c = counters(recs, pool)
    chk("report: counters tabulate every record by key",
        c["corrupted_spelling"]["keys"] == ["CORR_corrupted i=8 s=2"] and c["refusals"]["n"] == 1
        and c["cap_hits"]["n"] == 1 and c["n_records"] == 2 and c["line_break_in_stored_text"]["n"] == 0, c)
    import json
    from pathlib import Path
    from ..m import corr
    from ..m import stages as m_stages
    real = corr.load_pool()
    got = {}
    for ck in ("sft", "dpo", "instruct"):
        rel = f"data/m/gates/G-CAL_completability_olmo-{ck}.json"
        probs, data = m_stages._committed(rel)
        cc = counters(json.loads(data)["records"], real) if not probs else {}
        got[ck] = {k: cc[k]["n"] for k in COUNTERS + ("line_break_in_stored_text",)} if cc else probs
    want = {"sft": {"control_chars": 0, "harness_first_line": 5, "cap_hits": 6, "refusals": 1, "corrupted_spelling": 4,
                    "line_break_in_stored_text": 0},
            "dpo": {"control_chars": 0, "harness_first_line": 7, "cap_hits": 9, "refusals": 2, "corrupted_spelling": 10,
                    "line_break_in_stored_text": 1},
            "instruct": {"control_chars": 1, "harness_first_line": 8, "cap_hits": 9, "refusals": 2,
                         "corrupted_spelling": 9, "line_break_in_stored_text": 1}}
    chk("report: on G-CAL-OLMo's committed records the counters give the BUILD entry's figures -- the DEL at instruct "
        "7 s1 the one control character, the two item-15 line breaks of record (DPO and instruct; no proxy then)",
        got == want, got)
