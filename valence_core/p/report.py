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
  corrupted_spelling  an answer in corrupted spelling (class (c) of p §0.3), by the seat's pinned definition below

PIN (Code, declared at the p BUILD): control characters are Unicode category Cc minus ``\\n`` and ``\\r`` (tab
included); the listed forms and m:258's patterns match at the start of the first line, case as written; refusals match
case-insensitively, straight or curly apostrophe.

corrupted_spelling: THE SEAT'S PINNED DEFINITION, the ruling of 2026-11-07 (§5), committed at 38f9974 as
results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md, verbatim:

  candidate words are the stored text's whitespace-split, `normalize`d words of length ≥ 2, excluding FUNCTION_WORDS
  and every word of the clean pool's tasks; numeric golds are excluded; a hit iff the word is not a gold and its
  Levenshtein distance to some gold is ≤ 1 for a gold of length ≤ 3, ≤ 2 otherwise.

PIN (Code, declared at the rulings' commit): the text is split on whitespace first and each token then normalized by
f0's ``normalize`` (m's ``gcal.normalize``, the grader's), empty tokens dropped -- so ``don't`` is the one word
``don t``, never ``don``; the clean pool's task words by the same rule; FUNCTION_WORDS is p §1.1's list; a gold is a
normalized gold variant, numeric when its characters other than spaces are digits. On G-CAL-OLMo's 384 committed
records it counts 0/3/5 records (sft/dpo/instruct): the five of p §0.3's class (c) (``Januwy`` x2, ``Janaury``, ``dn``
x2), ``irom`` (instruct item 7 s1) and ``true`` against ``three`` twice (dpo clean item 4 s1, instruct corrupted item 4
s1); ``Janbaa``, ``Janyooar`` and ``Ther qro abov two dsys in a wemk`` are not counted -- the counter under-counts the
class, as the ruling says. Nor does it over-count only ``true``: a common word within the threshold of a gold
counts wherever an answer to that item uses it (``there``/``three``, ``could``/``cold``, ``too``/``two``,
``from``/``iron``, ``that``/``shut``), and so does a gold's own inflection under the PIN's tokenization (``January's``
is ``january s``, distance 2; ``Iron's``, ``Seven's``, ``twenty-fourth``; ``Close.`` against ``closed``, ``Colder.``
against ``cold``) -- F-p11, a FLAG for the seat (the reviews of the rulings' commit, n3 and r2-n1). Descriptive, deciding nothing (rule
23); recomputable from the records at any time.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Mapping, Sequence

from ..m import banner
from ..m import gcal as m_gcal
from .corrupt import FUNCTION_WORDS
from .proxy import has_line_break

LISTED_FORMS = ("### Response:", "Regenerate.", "[PROLOGUE", "Correctness:", "Reasoning:", "Answer:", "Input:")
_BANNER_RX = tuple(re.compile(re.escape(s).replace(r"\{L_clean\}", ".+?").replace(r"\{L_corr\}", ".+?")
                              .replace(r"\{L_a\}", ".+?").replace(r"\{L_b\}", ".+?").replace(r"\{n\}", ".+?"))
                   for s in banner.DECLARED_HARNESS_STRINGS)
_FENCE = re.compile(r"===.*===")
_REFUSAL = re.compile(r"\bI['’]m sorry\b|\bI cannot\b|\bI can['’]t\b", re.IGNORECASE)
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


def spelling_words(text: str) -> list[str]:
    """The pinned definition's words: whitespace-split, each token normalized (f0's ``normalize``), empties dropped."""
    return [n for t in str(text).split() for n in [m_gcal.normalize(t)] if n]


def clean_task_words(pool: Sequence[Mapping[str, Any]]) -> frozenset:
    """Every word of the clean pool's tasks, by the same rule (the pinned definition's exclusion); a pool item without a
    task is an error, never an empty exclusion."""
    return frozenset(w for it in pool for w in spelling_words(it["task"]))


def spelling_golds(gold: Sequence[str]) -> list[str]:
    """The normalized gold variants, numeric ones excluded."""
    out = []
    for g in gold:
        n = m_gcal.normalize(g)
        if n and not n.replace(" ", "").isdigit():
            out.append(n)
    return out


def corrupted_spelling(text: str, gold: Sequence[str], clean_words: frozenset = frozenset()) -> bool:
    """The seat's pinned definition (the module docstring)."""
    gs = spelling_golds(gold)
    words = [w for w in spelling_words(text) if len(w) >= 2 and w not in FUNCTION_WORDS and w not in clean_words]
    return any(w not in gs and levenshtein(w, g) <= (1 if len(g) <= 3 else 2) for w in words for g in gs)


def counters(records: Sequence[Mapping[str, Any]], pool: Sequence[Mapping[str, Any]]) -> dict:
    """Each counter's count and the keys it counts (pool, i, seed_index), over every record given."""
    def key(r):
        return f"{r['pool']} i={r['i']} s={r['seed_index']}"
    out = {}
    clean = clean_task_words(pool)
    for name, fn in (("control_chars", lambda r: control_chars(r["text"])),
                     ("harness_first_line", lambda r: harness_first_line(r["text"])),
                     ("cap_hits", lambda r: bool(r["cap_hit"])),
                     ("refusals", lambda r: refusal(r["text"])),
                     ("corrupted_spelling", lambda r: corrupted_spelling(r["text"], pool[r["i"]]["gold"], clean))):
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
    cw = frozenset({"iron", "triangle", "month", "year", "the", "first"})
    chk("report: corrupted spelling by the seat's pinned definition -- 'dn' (down), 'Januwy' and 'Janaury' (january) "
        "count; 'the', 'two' and 'do' do not; 'Janbaa' and 'Janyooar' (distance >= 3) do not; numeric golds are not "
        "compared; a gold of length <= 3 takes distance 1 ('tw' counts for 'two', 'tow' does not); a clean-task word "
        "is no candidate; split before normalize ('don't' is 'don t', not 'don'); golds normalized ('twenty-fuor' "
        "counts for 'twenty-four'); a one-letter word is no candidate ('a' against gold 'ab')",
        corrupted_spelling("dn", ["down"]) and corrupted_spelling("Januwy", gold8)
        and corrupted_spelling("The ftrst month of the ybaa is Janaury", gold8, cw)
        and not corrupted_spelling("The bicycle has two wheels", ["2", "two"]) and not corrupted_spelling("do", ["down"])
        and not corrupted_spelling("January", gold8) and not corrupted_spelling("Janbaa", gold8)
        and not corrupted_spelling("Janyooar", gold8) and not corrupted_spelling("777 7", ["77"])
        and corrupted_spelling("tw", ["2", "two"]) and not corrupted_spelling("tow", ["2", "two"])
        and corrupted_spelling("Marsh", gold2) and not corrupted_spelling("irn triangle", ["triangl"], cw | {"irn"})
        and not corrupted_spelling("I don't know", ["down"]) and corrupted_spelling("twenty-fuor", ["24", "twenty-four"])
        and not corrupted_spelling("b", ["ab"]) and corrupted_spelling("bb", ["ab"]),
        (levenshtein("janbaa", "january"), levenshtein("januwy", "january")))
    recs = [{"pool": "CORR_corrupted", "i": 8, "seed_index": 2, "text": "Januwy", "cap_hit": False},
            {"pool": "CORR_clean", "i": 2, "seed_index": 0, "text": "I'm sorry", "cap_hit": True}]
    pool = [{"task": "Task x.", "gold": ["x"]}] * 2 + [{"task": "Name it.", "gold": ["march"]}] + \
        [{"task": "Task x.", "gold": ["x"]}] * 5 + [{"task": "Name it.", "gold": ["january"]}] + \
        [{"task": "Task x.", "gold": ["x"]}] * 7
    c = counters(recs, pool)
    try:
        clean_task_words([{"gold": ["x"]}])
        no_task = "read"
    except KeyError:
        no_task = "error"
    chk("report: counters tabulate every record by key; a pool item without a task is an error, never an empty "
        "exclusion",
        c["corrupted_spelling"]["keys"] == ["CORR_corrupted i=8 s=2"] and c["refusals"]["n"] == 1
        and c["cap_hits"]["n"] == 1 and c["n_records"] == 2 and c["line_break_in_stored_text"]["n"] == 0
        and no_task == "error", c)
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
    want = {"sft": {"control_chars": 0, "harness_first_line": 5, "cap_hits": 6, "refusals": 1, "corrupted_spelling": 0,
                    "line_break_in_stored_text": 0},
            "dpo": {"control_chars": 0, "harness_first_line": 7, "cap_hits": 9, "refusals": 2, "corrupted_spelling": 3,
                    "line_break_in_stored_text": 1},
            "instruct": {"control_chars": 1, "harness_first_line": 8, "cap_hits": 9, "refusals": 2,
                         "corrupted_spelling": 5, "line_break_in_stored_text": 1}}
    chk("report: on G-CAL-OLMo's committed records the counters give the ruled definition's figures (corrupted spelling "
        "0/3/5) -- the DEL at instruct "
        "7 s1 the one control character, the two item-15 line breaks of record (DPO and instruct; no proxy then)",
        got == want, got)
