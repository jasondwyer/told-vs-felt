"""PROPOSAL-p's descriptive counters and its line-break hair trigger (p v0.2 §2.3).

The hair trigger ``line_break_in_stored_text`` -- any stored text in any p session or gate containing ``\\n`` or
``\\r`` -- domain every session and every G-CAL-p generation; a fire STOPs the stage (rule 21; zero base rate by
construction once §2.2's proxy stands). The counters are computed by this tool over the records (the analyzer
unchanged for them), tabulated over every generation, reported in the gate and VERDICTS entries, deciding nothing
(rule 23):

  control_chars       texts holding a control character other than a line break (the DEL of gcal instruct 7 s1),
                      each listed by key with its text (F-p13 below)
  harness_first_line  texts whose first line is harness-shaped: m:258's eight declared strings (placeholders as
                      wildcards), the seven listed forms, any line of the form ``=== ... ===``, and (F-p11 below) a
                      line beginning ``**`` or a line of the form ``_..._``
  cap_hits            records with cap_hit
  refusals            ``I'm sorry`` / ``I cannot`` / ``I can't`` forms
  corrupted_spelling  an answer in corrupted spelling (class (c) of p §0.3), by the seat's pinned definition below,
                      refined by its answer of 2026-11-08 (F-p11 below)

PIN (Code, declared at the p BUILD): control characters are Unicode category Cc minus ``\\n`` and ``\\r`` (tab
included); the listed forms and m:258's patterns match at the start of the first line, case as written; refusals match
case-insensitively, straight or curly apostrophe.

F-p13, THE SEAT'S RULING (its answer of 2026-11-08, ``daca8b0``, §1, results/raw/2026-11-08_p-gcal_design-to-code_
answers.md): control characters are a counter, as §2.3 declares, never a hair trigger (rule 21: a measured base rate,
5 of 384 at G-CAL-p); "(a) every stage's entry lists each stored text that carries a control character, so the seat's
read sees them by name; (b) the proxy stores model output as the model produced it -- nothing is stripped or
substituted". ``counters`` returns those texts by key (``control_chars.texts``) for (a); the proxy (``proxy.py``)
cuts at a line break and changes nothing else, for (b).

F-p11, THE SEAT'S REFINEMENT (the same answer, §3), on top of the pinned definition below: "(i) a candidate word is
excluded if it is in a committed English lexicon -- Code picks the source (a frozen common-words list), commits it
under data/p/ with its sha256, declared at LOCK-p v0.1 -- so there, could, close do not count; (ii) a word equal to a
gold up to trailing punctuation and a possessive or plural suffix (January's, Close.) does not count. dn, Januwy,
Janaury still count; Janbaa and Janyooar, at distance >= 3, still do not -- the counter under-counts the class and
says so. Also added to §2.3's harness-shaped-first-line forms: a line beginning ** and a line of the form _..._".
G-CAL-p's artifacts stand as written; the re-tabulation is reported at the entries that quote the counters.

PIN (Code, declared at step 6, LOCK-p v0.1): (i)'s lexicon is ``data/p/lexicon/web2.txt`` (``LEXICON_REL``), the
system dictionary of BSD and macOS, Webster's Second International (1934; "the 1934 copyright has lapsed, according to
the supplier", its README), 235,976 lines, byte for byte, sha256 ``LEXICON_SHA256`` checked at every load. It is a full
dictionary, not a frequency-ranked common-words list: it excludes every English word it lists, common or rare, so it
excludes more than such a list would (``Marsh`` against ``march`` no longer counts), and it lacks some regular
inflections (``wheels``). Its entries are read through f0's ``normalize``, as the candidates are. A candidate that
normalizes to several parts (``twenty-fourth`` is ``twenty fourth``; ``January's`` is ``january s``) is in the lexicon
iff every part is (web2 lists the single letters). (ii) reads the raw whitespace token: its trailing characters that
are neither letters nor digits are dropped, then each of the suffixes ``'s``, ``’s``, ``s'``, ``s’``, ``es`` and ``s``
it ends with (case-insensitive) is dropped in turn, and the token does not count if the token or one of those bases
normalizes to a gold. ``Close.`` is excluded by (i), ``close`` being in the lexicon; (ii) alone would not exclude it,
``close`` not being ``closed`` up to a suffix. The two new first-line forms match as the listed forms do: ``**`` at the
start of the first line, case as written; ``_..._`` as the stripped first line, an underscore, one character or more,
an underscore.

THE SFT SENTENCE (the same answer, §0.1, declared for p's record): "every entry, lock line and posted sentence that
reports OLMo-SFT's A0 outcome carries *G-CAL-p passed at the bar, 47/64 against 47* -- a reported fact, not a caveat on
a verdict (p §5.4's form)". ``SFT_AT_BAR`` holds it; ``declared_sentences(unit)`` gives a unit's.

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

import hashlib
import re
import unicodedata
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..m import banner
from ..m import gcal as m_gcal
from .corrupt import FUNCTION_WORDS
from .proxy import has_line_break

REPO = Path(__file__).resolve().parents[2]
LISTED_FORMS = ("### Response:", "Regenerate.", "[PROLOGUE", "Correctness:", "Reasoning:", "Answer:", "Input:")
#: F-p11's two added first-line forms (the seat's answer of 2026-11-08, §3).
BOLD_PREFIX = "**"
_BANNER_RX = tuple(re.compile(re.escape(s).replace(r"\{L_clean\}", ".+?").replace(r"\{L_corr\}", ".+?")
                              .replace(r"\{L_a\}", ".+?").replace(r"\{L_b\}", ".+?").replace(r"\{n\}", ".+?"))
                   for s in banner.DECLARED_HARNESS_STRINGS)
_FENCE = re.compile(r"===.*===")
_UNDERSCORED = re.compile(r"_.+_")
_REFUSAL = re.compile(r"\bI['’]m sorry\b|\bI cannot\b|\bI can['’]t\b", re.IGNORECASE)
COUNTERS = ("control_chars", "harness_first_line", "cap_hits", "refusals", "corrupted_spelling")
#: F-p11 (i)'s lexicon (the module docstring's PIN): web2, byte for byte, its sha256 checked at every load.
LEXICON_REL = "data/p/lexicon/web2.txt"
LEXICON_SHA256 = "be41ad97963bf8dabedd5871d5d691596175269d540956b0f9965a885c2bbab9"
#: F-p11 (ii)'s suffixes, dropped one at a time after the trailing punctuation (the module docstring's PIN).
GOLD_SUFFIXES = ("'s", "’s", "s'", "s’", "es", "s")
_TRAILING = re.compile(r"[^0-9A-Za-z]+$")
#: The SFT sentence (the seat's answer of 2026-11-08, §0.1), verbatim.
SFT_AT_BAR = "G-CAL-p passed at the bar, 47/64 against 47"


class LexiconStop(SystemExit):
    """The lexicon is absent or not the pinned bytes: the counter is never computed against another list."""


_LEXICON: dict[str, frozenset] = {}


def line_break_in_stored_text(text: str) -> bool:
    """§2.3's hair trigger predicate."""
    return has_line_break(text)


def control_chars(text: str) -> bool:
    return any(unicodedata.category(c) == "Cc" and c not in "\n\r" for c in text)


def harness_first_line(text: str) -> bool:
    first = re.split(r"[\r\n]", text, maxsplit=1)[0]
    stripped = first.strip()
    return (any(first.startswith(f) for f in LISTED_FORMS) or any(rx.match(first) for rx in _BANNER_RX)
            or bool(_FENCE.fullmatch(stripped)) or first.startswith(BOLD_PREFIX)
            or bool(_UNDERSCORED.fullmatch(stripped)))


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


def load_lexicon(path: Path | None = None) -> frozenset:
    """F-p11 (i)'s lexicon: the pinned file's lines through f0's ``normalize``, empties dropped; refused (LexiconStop)
    unless its bytes hash to ``LEXICON_SHA256``. Read once per path."""
    p = Path(path) if path is not None else REPO / LEXICON_REL
    key = str(p)
    if key not in _LEXICON:
        try:
            data = p.read_bytes()
        except OSError as e:
            raise LexiconStop(f"LEXICON STOP: {p} unreadable ({type(e).__name__}); the corrupted-spelling counter "
                              f"runs against the pinned lexicon only (F-p11)") from None
        got = hashlib.sha256(data).hexdigest()
        if got != LEXICON_SHA256:
            raise LexiconStop(f"LEXICON STOP: {p} has sha256 {got}, not the pinned {LEXICON_SHA256} (F-p11)")
        _LEXICON[key] = frozenset(n for ln in data.decode("utf-8").splitlines() for n in [m_gcal.normalize(ln)] if n)
    return _LEXICON[key]


def in_lexicon(word: str, lexicon: frozenset) -> bool:
    """F-p11 (i), the module docstring's PIN: a normalized candidate is in the lexicon iff every part is."""
    parts = word.split()
    return bool(parts) and all(x in lexicon for x in parts)


def gold_up_to_suffix(token: str, golds: Sequence[str]) -> bool:
    """F-p11 (ii), the module docstring's PIN: the raw token, its trailing punctuation dropped, then each listed suffix
    it ends with dropped in turn; true iff the token or a base normalizes to one of ``golds`` (normalized)."""
    u = _TRAILING.sub("", str(token))
    bases = [u] + [u[:-len(s)] for s in GOLD_SUFFIXES if len(u) > len(s) and u.lower().endswith(s)]
    return any(m_gcal.normalize(b) in golds for b in bases if b)


def corrupted_spelling(text: str, gold: Sequence[str], clean_words: frozenset = frozenset(),
                       lexicon: frozenset | None = None) -> bool:
    """The seat's pinned definition, with F-p11's refinement (the module docstring): (i) the lexicon (the pinned one
    unless ``lexicon`` is given) and (ii) the gold up to a suffix exclude a candidate."""
    lex = load_lexicon() if lexicon is None else lexicon
    gs = spelling_golds(gold)
    for tok in str(text).split():
        w = m_gcal.normalize(tok)
        if not w or len(w) < 2 or w in FUNCTION_WORDS or w in clean_words:
            continue
        if in_lexicon(w, lex) or gold_up_to_suffix(tok, gs):
            continue
        if any(w not in gs and levenshtein(w, g) <= (1 if len(g) <= 3 else 2) for g in gs):
            return True
    return False


def declared_sentences(unit: str) -> list[str]:
    """The sentences p's record declares for a unit's A0-outcome reports: OLMo-SFT's at-the-bar sentence (§0.1)."""
    return [SFT_AT_BAR] if unit == "OLMo-sft" else []


def counters(records: Sequence[Mapping[str, Any]], pool: Sequence[Mapping[str, Any]],
             lexicon: frozenset | None = None) -> dict:
    """Each counter's count and the keys it counts (pool, i, seed_index), over every record given; the control-
    character texts listed by key (F-p13 (a))."""
    def key(r):
        return f"{r['pool']} i={r['i']} s={r['seed_index']}"
    out = {}
    clean = clean_task_words(pool)
    lex = load_lexicon() if lexicon is None else lexicon
    for name, fn in (("control_chars", lambda r: control_chars(r["text"])),
                     ("harness_first_line", lambda r: harness_first_line(r["text"])),
                     ("cap_hits", lambda r: bool(r["cap_hit"])),
                     ("refusals", lambda r: refusal(r["text"])),
                     ("corrupted_spelling",
                      lambda r: corrupted_spelling(r["text"], pool[r["i"]]["gold"], clean, lex))):
        ks = [key(r) for r in records if fn(r)]
        out[name] = {"n": len(ks), "keys": ks}
    out["control_chars"]["texts"] = {key(r): r["text"] for r in records if control_chars(r["text"])}
    out["line_break_in_stored_text"] = {"n": sum(1 for r in records if line_break_in_stored_text(r["text"]))}
    out["n_records"] = len(records)
    return out


#: A gate stage's withheld part (m:318; m's G-TIME read rule, the seat's ruling (h)), named in every session report.
WITHHELD = ("the contrast sessions' counters other than the forced rounds' control characters, every count over a "
            "contrast free round, and the corrupted-spelling counter over the sham sessions' free rounds (it reads the "
            "round's item, which the sham read withholds because it names the pick): withheld to the unit's VERDICTS "
            "(m:318; m's read rule, the seat's ruling (h)), recomputable from the checkpoint")


def round_key(rec: Mapping[str, Any], r: Mapping[str, Any]) -> str:
    """A session round's key: template, session index, phase and the round's index within its phase."""
    return f"{rec['template']} s={rec['s']} {r['phase']} {r['ri'] if r['phase'] == 'forced' else r['ci']}"


def session_counters(sessions: Sequence[Mapping[str, Any]], pool: Sequence[Mapping[str, Any]],
                     lexicon: frozenset | None = None) -> dict:
    """§2.3's counters over a gate stage's session records, on the seat's read domain (m:271, m:318).

    PIN (Code, declared at step 6): the hair trigger reads every round of every session (a count, zero by
    construction once the proxy cuts); the text-only counters (control characters, harness-shaped first lines,
    refusals) and cap hits read every round of the sham sessions, keyed by ``round_key``, the control-character texts
    listed (F-p13 (a)); the corrupted-spelling counter reads the sham sessions' FORCED rounds only -- it needs a round's
    gold, ``pool[item]``, and the sham read withholds a free round's item because it names the pick (readrule's
    _FREE_ROUND_KEEP PIN); the contrast sessions give the control-character texts of their forced rounds only (F-p13
    (a); the forced rounds' texts are in the seat's read); every other count is ``WITHHELD``.

    PIN (Code, declared at step 6; for the seat's word, the BUILD entry's items (a) and (b)): (a) the contrast forced
    rounds' control-character texts are listed by key -- F-p13 (a)'s "every such text by key" -- though the seat's
    ruling (h) keeps class fields and round positions out of m's G-TIME report (the read shows the same texts, keyed
    by forced round); (b) the seat's Q5 "over the checkpoint" is read as the seat's read domain, every other contrast
    count withheld to VERDICTS."""
    clean = clean_task_words(pool)
    lex = load_lexicon() if lexicon is None else lexicon
    rounds = [(rec, r) for rec in sessions for r in rec.get("rounds", ())]
    sham = [(rec, r) for rec, r in rounds if not rec["contrast"]]
    sham_forced = [(rec, r) for rec, r in sham if r["phase"] == "forced"]
    con_forced = [(rec, r) for rec, r in rounds if rec["contrast"] and r["phase"] == "forced"]
    out: dict = {"hair_trigger": {"name": "line_break_in_stored_text", "domain": "every round of every session",
                                  "n": sum(1 for _, r in rounds if line_break_in_stored_text(r["text"]))},
                 "sham": {}, "n_sham_rounds": len(sham), "n_sham_forced_rounds": len(sham_forced),
                 "withheld": WITHHELD}
    for name, fn, dom in (("control_chars", lambda r: control_chars(r["text"]), sham),
                          ("harness_first_line", lambda r: harness_first_line(r["text"]), sham),
                          ("cap_hits", lambda r: bool(r["cap_hit"]), sham),
                          ("refusals", lambda r: refusal(r["text"]), sham),
                          ("corrupted_spelling",
                           lambda r: corrupted_spelling(r["text"], pool[int(r["item"])]["gold"], clean, lex),
                           sham_forced)):
        ks = [round_key(rec, r) for rec, r in dom if fn(r)]
        out["sham"][name] = {"n": len(ks), "keys": ks, "domain": "every sham round" if dom is sham
                             else "the sham sessions' forced rounds"}
    out["sham"]["control_chars"]["texts"] = {round_key(rec, r): r["text"] for rec, r in sham if control_chars(r["text"])}
    cc = {round_key(rec, r): r["text"] for rec, r in con_forced if control_chars(r["text"])}
    out["contrast_forced_control_chars"] = {"n": len(cc), "keys": list(cc), "texts": cc,
                                            "n_forced_rounds": len(con_forced)}
    return out


def _selftest(chk) -> None:
    chk("report: the trigger reads \\n and \\r", line_break_in_stored_text("a\nb") and line_break_in_stored_text("a\rb")
        and not line_break_in_stored_text("ab"))
    chk("report: control characters count DEL and tab, never a line break",
        control_chars("\x7fThe kernl") and control_chars("a\tb") and not control_chars("plain"))
    hs = ["=== Config evaluation session ===", "[PROLOGUE", "Regenerate.", "### Response:", "Correctness:",
          "Input: hot", "Answer:", "Reasoning:", "=== Actual module name ===", "[round 3 | reasoning]",
          "Note: config slate presents clean task text; config prism presents clean task text. Prefer clean task text.",
          "**DRAFT ANSWER", "**Final Answer", "_ALIGNMENT complete_", "  _x_  "]
    nh = ["77", "cold", "The opposite of 'up' is 'down'", "Reasoning about it", "== x ==", "*one star*", "__",
          "a_b_", "_ALIGNMENT complete", "The answer is 2._ALIGNMENT complete_", " **late bold"]
    chk("report: harness-shaped first lines -- m:258's patterns, the seven forms, '=== ... ===', and F-p11's two "
        "(a line beginning '**', a line '_..._') -- and not answers",
        all(harness_first_line(t) for t in hs) and not any(harness_first_line(t) for t in nh),
        ([t for t in hs if not harness_first_line(t)], [t for t in nh if harness_first_line(t)]))
    chk("report: refusals in the three forms, either apostrophe",
        refusal("I'm sorry, but I can't assist") and refusal("I cannot compute") and refusal("I can’t")
        and not refusal("I can compute it"))
    gold8, gold2 = ["january"], ["march"]
    cw = frozenset({"iron", "triangle", "month", "year", "the", "first"})
    none = frozenset()                                   # the pinned definition alone: no lexicon
    chk("report: corrupted spelling by the seat's pinned definition (no lexicon) -- 'dn' (down), 'Januwy' and "
        "'Janaury' (january) count; 'the', 'two' and 'do' do not; 'Janbaa' and 'Janyooar' (distance >= 3) do not; "
        "numeric golds are not compared; a gold of length <= 3 takes distance 1 ('tw' counts for 'two', 'tow' does "
        "not); a clean-task word is no candidate; split before normalize ('don't' is 'don t', not 'don'); golds "
        "normalized ('twenty-fuor' counts for 'twenty-four'); a one-letter word is no candidate ('a' against gold 'ab')",
        corrupted_spelling("dn", ["down"], lexicon=none) and corrupted_spelling("Januwy", gold8, lexicon=none)
        and corrupted_spelling("The ftrst month of the ybaa is Janaury", gold8, cw, none)
        and not corrupted_spelling("The bicycle has two wheels", ["2", "two"], lexicon=none)
        and not corrupted_spelling("do", ["down"], lexicon=none)
        and not corrupted_spelling("January", gold8, lexicon=none) and not corrupted_spelling("Janbaa", gold8,
                                                                                            lexicon=none)
        and not corrupted_spelling("Janyooar", gold8, lexicon=none)
        and not corrupted_spelling("777 7", ["77"], lexicon=none)
        and corrupted_spelling("tw", ["2", "two"], lexicon=none) and not corrupted_spelling("tow", ["2", "two"],
                                                                                         lexicon=none)
        and corrupted_spelling("Marsh", gold2, lexicon=none)
        and not corrupted_spelling("irn triangle", ["triangl"], cw | {"irn"}, none)
        and not corrupted_spelling("I don't know", ["down"], lexicon=none)
        and corrupted_spelling("twenty-fuor", ["24", "twenty-four"], lexicon=none)
        and not corrupted_spelling("b", ["ab"], lexicon=none) and corrupted_spelling("bb", ["ab"], lexicon=none),
        (levenshtein("janbaa", "january"), levenshtein("januwy", "january")))
    lex = load_lexicon()
    chk("report: F-p11 (i) -- the pinned lexicon (web2, its sha256) excludes common words that the definition alone "
        "counts ('there', 'could', 'close', 'true', 'too', 'from', 'that', 'twenty-fourth' by its parts) and keeps "
        "'dn', 'Januwy', 'Janaury' and 'irom' counted; 'Marsh' (a word) no longer counts",
        len(lex) > 200000 and all(corrupted_spelling(t, g, lexicon=none) and not corrupted_spelling(t, g)
                                  for t, g in (("there", ["3", "three"]), ("could", ["cold"]), ("Close.", ["closed"]),
                                               ("true", ["3", "three"]), ("too", ["2", "two"]),
                                               ("from", ["iron"]), ("that", ["shut"]),
                                               ("twenty-fourth", ["24", "twenty-four"]), ("Marsh", gold2)))
        and all(corrupted_spelling(t, g) for t, g in (("dn", ["down"]), ("Januwy", gold8), ("Janaury", gold8),
                                                      ("irom", ["iron"]))),
        sorted(w for w in ("dn", "januwy", "janaury", "irom") if w in lex))
    chk("report: F-p11 (ii) -- a gold up to trailing punctuation and a possessive or plural suffix does not count, even "
        "with no lexicon ('January's', 'January’s', 'Januarys'', 'Januarys', 'Iron's.', 'Seven's'); a near-miss with "
        "trailing punctuation still counts ('Januwy.')",
        not any(corrupted_spelling(t, g, lexicon=none) for t, g in (("January's", gold8), ("January’s", gold8),
                                                                   ("Januarys'", gold8), ("Januarys", gold8),
                                                                   ("Iron's.", ["iron"]), ("Seven's", ["7", "seven"])))
        and corrupted_spelling("Januwy.", gold8, lexicon=none)
        and gold_up_to_suffix("Closes.", ["close"]) and not gold_up_to_suffix("Close.", ["closed"]))
    bad = None
    import tempfile
    with tempfile.TemporaryDirectory(prefix="p_lexicon_") as td:
        fake = Path(td) / "web2.txt"
        fake.write_text("there\ncould\n", encoding="utf-8")
        try:
            load_lexicon(fake)
        except LexiconStop as e:
            bad = str(e)
    chk("report: a lexicon that is not the pinned bytes is a LexiconStop, never a quiet substitute",
        bad is not None and LEXICON_SHA256 in bad, bad)
    chk("report: the SFT sentence is the seat's, verbatim, declared for OLMo-sft alone",
        declared_sentences("OLMo-sft") == ["G-CAL-p passed at the bar, 47/64 against 47"]
        and declared_sentences("OLMo-dpo") == [] and declared_sentences("OLMo-instruct") == [])
    recs = [{"pool": "CORR_corrupted", "i": 8, "seed_index": 2, "text": "Januwy", "cap_hit": False},
            {"pool": "CORR_clean", "i": 2, "seed_index": 0, "text": "I'm sorry", "cap_hit": True},
            {"pool": "CORR_corrupted", "i": 7, "seed_index": 1, "text": "\x7f", "cap_hit": False}]
    pool = [{"task": "Task x.", "gold": ["x"]}] * 2 + [{"task": "Name it.", "gold": ["march"]}] + \
        [{"task": "Task x.", "gold": ["x"]}] * 5 + [{"task": "Name it.", "gold": ["january"]}] + \
        [{"task": "Task x.", "gold": ["x"]}] * 7
    c = counters(recs, pool)
    try:
        clean_task_words([{"gold": ["x"]}])
        no_task = "read"
    except KeyError:
        no_task = "error"
    chk("report: counters tabulate every record by key, the control-character texts listed by key (F-p13 (a)); a pool "
        "item without a task is an error, never an empty exclusion",
        c["corrupted_spelling"]["keys"] == ["CORR_corrupted i=8 s=2"] and c["refusals"]["n"] == 1
        and c["cap_hits"]["n"] == 1 and c["n_records"] == 3 and c["line_break_in_stored_text"]["n"] == 0
        and c["control_chars"] == {"n": 1, "keys": ["CORR_corrupted i=7 s=1"],
                                   "texts": {"CORR_corrupted i=7 s=1": "\x7f"}}
        and no_task == "error", c)
    import json
    from ..m import corr
    from ..m import stages as m_stages
    real = corr.load_pool()
    fields = COUNTERS + ("line_break_in_stored_text",)

    def tab(tmpl: str, lexicon) -> dict:
        out_ = {}
        for ck in ("sft", "dpo", "instruct"):
            probs, data = m_stages._committed(tmpl.format(ck=ck))
            cc = counters(json.loads(data)["records"], real, lexicon) if not probs else {}
            out_[ck] = {k: cc[k]["n"] for k in fields} if cc else probs
        return out_
    m_tmpl, p_tmpl = "data/m/gates/G-CAL_completability_olmo-{ck}.json", "data/p/gates/G-CAL_completability_olmo-{ck}.json"
    m_want = {"sft": {"control_chars": 0, "harness_first_line": 5, "cap_hits": 6, "refusals": 1,
                      "corrupted_spelling": 0, "line_break_in_stored_text": 0},
              "dpo": {"control_chars": 0, "harness_first_line": 7, "cap_hits": 9, "refusals": 2,
                      "corrupted_spelling": 3, "line_break_in_stored_text": 1},
              "instruct": {"control_chars": 1, "harness_first_line": 8, "cap_hits": 9, "refusals": 2,
                           "corrupted_spelling": 5, "line_break_in_stored_text": 1}}
    m_refined = {ck: {**v, "corrupted_spelling": {"sft": 0, "dpo": 2, "instruct": 4}[ck]} for ck, v in m_want.items()}
    got_m0, got_m = tab(m_tmpl, frozenset()), tab(m_tmpl, None)
    chk("report: on G-CAL-OLMo's committed records the ruled definition alone (no lexicon) gives its figures "
        "(corrupted spelling 0/3/5) and F-p11's refinement 0/2/4 (the two 'true' against 'three' out) -- the DEL at "
        "instruct 7 s1 the one control character, the two item-15 line breaks of record (DPO and instruct; no proxy "
        "then); no first line takes F-p11's two new forms there",
        got_m0 == m_want and got_m == m_refined, (got_m0, got_m))
    p_want = {"sft": {"control_chars": 1, "harness_first_line": 2, "cap_hits": 8, "refusals": 1,
                      "corrupted_spelling": 0, "line_break_in_stored_text": 0},
              "dpo": {"control_chars": 2, "harness_first_line": 5, "cap_hits": 5, "refusals": 1,
                      "corrupted_spelling": 0, "line_break_in_stored_text": 0},
              "instruct": {"control_chars": 2, "harness_first_line": 6, "cap_hits": 2, "refusals": 1,
                           "corrupted_spelling": 0, "line_break_in_stored_text": 0}}
    got_p = tab(p_tmpl, None)
    chk("report: F-p11's re-tabulation of G-CAL-p's committed records (its artifacts stand as written, 2/3/5 harness "
        "first lines and 0/1/0 corrupted spelling there): harness first lines 2/5/6 (the '**DRAFT ANSWER' and "
        "'**Final Answer' item-15 misses), corrupted spelling 0/0/0 (dpo clean 4 s1's 'true' out)",
        got_p == p_want, got_p)
    sess = [{"template": "A0s-OLMo-sft", "s": 0, "contrast": False, "rounds": [
                {"phase": "forced", "ri": 1, "item": 8, "text": "Januwy", "cap_hit": False},
                {"phase": "free", "ci": 1, "item": 8, "text": "Januwy", "cap_hit": True},
                {"phase": "free", "ci": 2, "item": 8, "text": "\x7f", "cap_hit": False}]},
            {"template": "A0-OLMo-sft", "s": 0, "contrast": True, "rounds": [
                {"phase": "forced", "ri": 1, "item": 8, "text": "\x1b[1mx", "cap_hit": True},
                {"phase": "free", "ci": 1, "item": 8, "text": "Januwy\x7f", "cap_hit": True}]}]
    pool8 = [{"task": "Task x.", "gold": ["x"]}] * 8 + [{"task": "Name it.", "gold": ["january"]}] + \
        [{"task": "Task x.", "gold": ["x"]}] * 7
    sc = session_counters(sess, pool8)
    text = json.dumps(sc)
    chk("report: session counters on the seat's read domain -- corrupted spelling over the sham FORCED rounds only (a "
        "free round's item names the pick), the text-only counters and cap hits over every sham round, the contrast arm "
        "giving its forced rounds' control characters alone, the trigger over every round; nothing of the contrast free "
        "round in the output",
        sc["sham"]["corrupted_spelling"]["keys"] == ["A0s-OLMo-sft s=0 forced 1"]
        and sc["sham"]["cap_hits"]["keys"] == ["A0s-OLMo-sft s=0 free 1"]
        and sc["sham"]["control_chars"]["keys"] == ["A0s-OLMo-sft s=0 free 2"]
        and sc["contrast_forced_control_chars"]["keys"] == ["A0-OLMo-sft s=0 forced 1"]
        and sc["hair_trigger"]["n"] == 0 and "free 1\": \"Januwy\\u007f" not in text
        and "A0-OLMo-sft s=0 free" not in text and sc["n_sham_forced_rounds"] == 1, sc)
