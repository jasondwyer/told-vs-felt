"""PROPOSAL-m CORR delivery -- one substrate-agnostic module serving the F0m
(Qwen) and F0m-OLMo runners (v1.11 §0.7, m:54; §2.1, m:159; §2.3, m:176).

THE PROPERTY. The contrast delivers a property of the task text, never a
label identity (m:155): the P-role label's rounds carry CORR_clean, the
Q-role label's rounds carry the item's `corrupt_m` render on a contrast arm
and CORR_clean on a sham arm ("sham session s sees contrast session s's
items uncorrupted", m:159). `Delivery` is that map and nothing else.

THE POOL. `data/f/pools.json["CORR_clean"]`, 16 `{task, gold}` items, pinned
by the file's sha256 prefix `8547d9a11ba55b95` (m:176; calib `pools_sha`).
Every task is asserted ASCII, so f1's Unicode `isalpha` and m's `[A-Za-z]`
coincide on it (maps/f1.md §5 item 9).

THE ITEM STREAM. m:159: one `permutation(16)` from the item stream, [:8] to
the P label and [8:] to the Q label, each label consuming its own list in
order (f1's split, f_sessions.py:253-259). `ItemStreams` takes the rng
OBJECT, not a key, so G-PORT can pass f1's single session rng and keep
drawing seeds from it after the permutation (maps/f1.md §5 item 1); m passes
a fresh `keys.stream(keys.item_key(...))`. No wrap: a ninth draw for a role
is a harness bug and raises (f1's `% 8` never triggered, f_sessions.py:284-292).

`corrupt_m` (m:176), the dose of record, rate 0.15, operand excluded:
eligible = ASCII letters that do not begin a word (f1's rule: start of string
or after a non-letter, `word_start = not ch.isalpha()` after each character)
and are not inside a single-quoted span (quote marks included). Per-item rng
`stream(f"corr|{i}")`; ONE `permutation(n_eligible)`; walk in order until k
are accepted; every visited slot consumes exactly one `integers(25)` draw,
accepted or skipped, so no draw depends on k; replacement
`chr(ord('a') + ((ord(orig.lower()) - ord('a') + 1 + d) % 26))` (lowercase,
never the original letter); a slot is skipped iff the render with every
earlier accepted replacement and this one contains a word of either roster
as a case-insensitive substring; k = clip(floor(0.15 n + 0.5), 3, floor(n/2))
half-up, in integer arithmetic. A walk that runs out of slots before k is a
STOP. Known answers (m:176, maps/audit.md §6): n_eligible
6,19,19,13,24,14,10,45,19,10,24,14,6,19,10,14; k sums to 54; one skip (item
7); items 5/11/15 render `Writa the oppcsite oc 'hot'.`, `Writo the
oppssitu of 'up'.`, `Wtite thn opposite on 'open'.`.

`corrupt_f1` is f1's `corrupt()` at 0.12 ported verbatim (f_sessions.py:
106-116; f0_calibrate.py:69-80 is identical): G-PORT's corruptor and the
model-free 0.12 artifact G-CAL reports at step 6 (m:176 "computed first at
step 6 because it is model-free"; `f1_012_replay`). Known answer: renders
sha16 `2c2c227395ea9f2d` (= calib `corr_sha`), 31 changed letters.

HYGIENE (m:258 "Code's validation block"; rule 18 / 28(c)): every roster word
of both rosters, word-boundary and case-insensitive, against every clean
task, every gold, every render and every supplied harness string with its
`{...}` placeholders blanked (ported from format_recon.py:107-124). The
renders' own substring assertion (m:176 artifacts) lives in `renders_m`.
`startup_hygiene()` is the run-time form every stage runs before a session: both
rosters of record against the pool, golds, renders, m:258's EIGHT declared harness
strings (`banner.DECLARED_HARNESS_STRINGS`) and e2a's wrapper templates.

ROSTERS. Qwen: `e2d.config.ROSTER` (imported, never re-literalled -- two
literals of one roster is how a roster forks, e2d/config.py:31-35). OLMo:
`data/olmo/a1_repair_roster.json["selected_tags"]`, four pairs. They overlap
in granite, saddle, velvet and walnut (maps/olmo.md §4.1).

Nothing here touches a model, a tokenizer or steering machinery.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

from ..e2d import config as _e2d_config
from . import keys

REPO = Path(__file__).resolve().parents[2]
POOLS_PATH = REPO / "data" / "f" / "pools.json"
OLMO_ROSTER_PATH = REPO / "data" / "olmo" / "a1_repair_roster.json"
CALIB_PATH = REPO / "data" / "f" / "calib.json"

POOLS_SHA16 = "8547d9a11ba55b95"          # m:176; calib.json "pools_sha"
F1_012_SHA16 = "2c2c227395ea9f2d"         # calib.json "corr_sha"; maps/f1.md §2
N_ITEMS = 16
N_PER_ROLE = 8                            # [:8] P, [8:16] Q (m:159)
ROLES = ("P", "Q")
F1_RATE = 0.12                            # f_sessions.py:86 CORR_RATE (f1's own float, verbatim)
CLEAN, CORRUPTED = "clean", "corrupted"

QWEN_ROSTER = _e2d_config.ROSTER


class CorrStop(SystemExit):
    """A STOP of the CORR module (pool pin, roster file, dose walk)."""


class ItemStreamExhausted(RuntimeError):
    """A ninth item draw for one role: m has no wrap (f1's `% 8` never fired)."""


# --- rosters ----------------------------------------------------------------

def _check_roster(roster, where: str) -> tuple[tuple[str, str], ...]:
    out = []
    for pair in roster:
        if isinstance(pair, str) or len(pair) != 2:
            raise TypeError(f"{where}: roster entries are label pairs, got {pair!r}")
        a, b = pair
        for w in (a, b):
            if not (isinstance(w, str) and w.isascii() and w.isalpha() and w == w.lower()):
                raise TypeError(f"{where}: roster word must be lowercase ASCII letters, got {w!r}")
        if a == b:
            raise ValueError(f"{where}: a pair repeats its label: {pair!r}")
        out.append((a, b))
    if not out:
        raise ValueError(f"{where}: empty roster")
    return tuple(out)


def olmo_roster(path: str | Path = OLMO_ROSTER_PATH) -> tuple[tuple[str, str], ...]:
    """The OLMo roster: a1_repair_roster.json["selected_tags"] (maps/olmo.md §4.1)."""
    # PIN (Code, declared at LOCK v0.1): the OLMo roster must be exactly 4 pairs of two
    # distinct lowercase ASCII words (b3 stops unless 4 pairs, box_b3_sessions.py:241-246);
    # anything else is a CorrStop, not a repair.
    try:
        tags = json.loads(Path(path).read_text())["selected_tags"]
        roster = _check_roster(tags, f"OLMo roster {path}")
    except (OSError, KeyError, ValueError, TypeError) as e:
        raise CorrStop(f"OLMO ROSTER STOP: {path}: {e}") from None
    if len(roster) != 4:
        raise CorrStop(f"OLMO ROSTER STOP: {path} selects {len(roster)} pairs, expected 4")
    return roster


OLMO_ROSTER = olmo_roster()
#: Both rosters of record, the argument m's callers pass as `rosters`.
ROSTERS_OF_RECORD = (QWEN_ROSTER, OLMO_ROSTER)
# PIN (Code, declared at LOCK v0.1): ALL_ROSTER_WORDS is the sorted tuple of the union
# (12 words: 8 + 8 less the 4 shared), so its order is deterministic.
ALL_ROSTER_WORDS = tuple(sorted({w for r in ROSTERS_OF_RECORD for p in r for w in p}))


def _roster_words(rosters) -> tuple[str, ...]:
    """Flatten a sequence of rosters (each a sequence of pairs) to sorted words."""
    if isinstance(rosters, str):
        raise TypeError("rosters is a sequence of rosters, not a string")
    words = set()
    for j, r in enumerate(rosters):
        for pair in _check_roster(r, f"rosters[{j}]"):
            words.update(pair)
    if not words:
        raise ValueError("no roster words supplied")
    return tuple(sorted(words))


# --- pool ---------------------------------------------------------------------

def _validate_pool(obj) -> list[dict]:
    try:
        items = obj["CORR_clean"]
    except (KeyError, TypeError):
        raise CorrStop("POOL STOP: no CORR_clean pool") from None
    if len(items) != N_ITEMS:
        raise CorrStop(f"POOL STOP: CORR_clean has {len(items)} items, expected {N_ITEMS}")
    out = []
    for i, it in enumerate(items):
        if not (isinstance(it, dict) and set(it) == {"task", "gold"}):
            raise CorrStop(f"POOL STOP: item {i} is not a {{task, gold}} record")
        task, gold = it["task"], it["gold"]
        if not (isinstance(task, str) and task.isascii()):
            raise CorrStop(f"POOL STOP: item {i}'s task is not ASCII text: {task!r}")
        if not (isinstance(gold, list) and gold and all(isinstance(g, str) for g in gold)):
            raise CorrStop(f"POOL STOP: item {i}'s gold is not a non-empty list of strings")
        out.append({"task": task, "gold": list(gold)})
    return out


def load_pool(path: str | Path = POOLS_PATH) -> list[dict]:
    """CORR_clean, 16 `{task, gold}` items, sha256-prefix pinned (m:176)."""
    raw = Path(path).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if not sha.startswith(POOLS_SHA16):
        raise CorrStop(f"POOL SHA STOP: {path} sha256 {sha[:16]} != {POOLS_SHA16} (m:176)")
    return _validate_pool(json.loads(raw))


# --- corrupt_m (m:176) --------------------------------------------------------

def _eligible_m(text: str) -> list[int]:
    """m:176's eligible positions: non-word-initial ASCII letters outside quotes."""
    # PIN (Code, declared at LOCK v0.1): an odd number of "'" leaves the single-quoted span
    # undefined, so it is refused; the pool's only apostrophes are the operand pairs of items
    # 5, 11 and 15 (m:176).
    if text.count("'") % 2:
        raise ValueError(f"unbalanced single quotes, operand span undefined: {text!r}")
    out, word_start, in_quote = [], True, False
    for pos, ch in enumerate(text):
        if ch == "'":
            in_quote = not in_quote          # the quote marks are inside the span; never letters
        elif ("a" <= ch <= "z" or "A" <= ch <= "Z") and not word_start and not in_quote:
            out.append(pos)
        word_start = not ch.isalpha()        # f1's rule, f_sessions.py:115
    return out


def _k_m(n: int) -> int:
    # floor(0.15 n + 0.5) == (15 n + 50) // 100 exactly; then clip(., 3, floor(n/2)).
    # PIN (Code, declared at LOCK v0.1): where floor(n/2) < 3 the clip returns floor(n/2)
    # (min after max, np.clip's lo > hi semantics); no CORR item reaches it (min n = 6), and
    # condition (1) would report it.
    return min(max((15 * n + 50) // 100, 3), n // 2)


def corrupt_m(text: str, i: int, rosters) -> tuple[str, dict]:
    """m's dose of record (m:176): (render, meta). Raises CorrStop if the walk runs dry."""
    if isinstance(i, bool) or not isinstance(i, int) or i < 0:
        raise TypeError(f"item index must be a non-negative int, got {i!r}")
    # PIN (Code, declared at LOCK v0.1): corrupt_m refuses non-ASCII text, the one domain on
    # which m's [A-Za-z] and f1's Unicode isalpha are the same rule (maps/f1.md §5 item 9).
    if not text.isascii():
        raise ValueError(f"corrupt_m takes ASCII text only: {text!r}")
    words = _roster_words(rosters)
    eligible = _eligible_m(text)
    n = len(eligible)
    k = _k_m(n)
    rng = keys.stream(f"corr|{i}")
    order = rng.permutation(n)
    cur = list(text)
    accepted: list[int] = []
    n_skips = n_visited = 0
    for slot in order:
        if len(accepted) == k:
            break
        pos = eligible[int(slot)]
        d = int(rng.integers(25))            # one draw per visited slot, accepted or skipped
        n_visited += 1
        orig = text[pos]
        rep = chr(ord("a") + ((ord(orig.lower()) - ord("a") + 1 + d) % 26))
        trial = cur.copy()
        trial[pos] = rep
        low = "".join(trial).lower()
        if any(w in low for w in words):
            n_skips += 1
            continue
        cur = trial
        accepted.append(pos)
    if len(accepted) != k:
        raise CorrStop(f"CORRUPT_M STOP: item {i} accepted {len(accepted)} of k = {k} over "
                       f"{n} eligible slots ({n_skips} roster skips); re-specify (m:176)")
    # PIN (Code, declared at LOCK v0.1): changed_positions are character offsets into the
    # clean text, ascending (the walk order is reproducible from the key and not recorded).
    meta = {"n_eligible": n, "k": k, "changed_positions": sorted(accepted),
            "n_skips": n_skips, "n_visited": n_visited}
    return "".join(cur), meta


def renders_m(pool: Sequence[dict], rosters) -> list[str]:
    """The 16 renders of record under corrupt_m, roster-asserted (m:176 artifacts)."""
    if len(pool) != N_ITEMS:
        raise CorrStop(f"RENDERS STOP: pool has {len(pool)} items, expected {N_ITEMS}")
    words = _roster_words(rosters)
    out = [corrupt_m(it["task"], i, rosters)[0] for i, it in enumerate(pool)]
    bad = [(j, w) for j, r in enumerate(out) for w in words if w in r.lower()]
    if bad:  # unreachable while the skip rule holds; the artifact asserts it anyway
        raise CorrStop(f"RENDERS STOP: roster substring in a render: {bad[:3]}")
    return out


def renders_sha(renders: Sequence[str]) -> str:
    """sha256 of the renders joined by newlines, first 16 hex (f0_calibrate.py:118-121)."""
    if isinstance(renders, str):
        raise TypeError("renders is a sequence of strings, not a string")
    return hashlib.sha256("\n".join(renders).encode()).hexdigest()[:16]


# --- f1's corruptor at 0.12 (G-PORT, G-CAL step 6) ----------------------------

def corrupt_f1(text: str, i: int) -> str:
    """f1's `corrupt()` verbatim (f_sessions.py:106-116), 26-letter draw at 0.12."""
    rng = keys.stream(f"corr|{i}")
    out, word_start = [], True
    for ch in text:
        if ch.isalpha() and not word_start and rng.random() < F1_RATE:
            out.append(chr(ord('a') + int(rng.integers(26))))
        else:
            out.append(ch)
        word_start = not ch.isalpha()
    return "".join(out)


def _f1_trace(text: str, i: int) -> tuple[str, int, int]:
    """(render, n_eligible under f1's rule, hits) -- same draws as corrupt_f1."""
    rng = keys.stream(f"corr|{i}")
    out, word_start, n_el, hits = [], True, 0, 0
    for ch in text:
        if ch.isalpha() and not word_start:
            n_el += 1
            if rng.random() < F1_RATE:
                hits += 1
                out.append(chr(ord('a') + int(rng.integers(26))))
                word_start = not ch.isalpha()
                continue
        out.append(ch)
        word_start = not ch.isalpha()
    return "".join(out), n_el, hits


def renders_f1(pool: Sequence[dict]) -> list[str]:
    """f1's 16 renders at 0.12 (the corrupted pool G-PORT replays)."""
    if len(pool) != N_ITEMS:
        raise CorrStop(f"RENDERS STOP: pool has {len(pool)} items, expected {N_ITEMS}")
    return [corrupt_f1(it["task"], i) for i, it in enumerate(pool)]


def f1_012_replay(pool: Sequence[dict], calib_path: str | Path = CALIB_PATH) -> dict:
    """The model-free 0.12 artifact against conditions (1)-(2) (m:176; maps/f1.md §3).

    Built at step 4, computed at G-CAL step 6; it gates nothing. calib.json's covariate is
    quoted beside it as stored (clean minus corrupted, f0's sign)."""
    rows = []
    renders = []
    for i, it in enumerate(pool):
        r, n_el, hits = _f1_trace(it["task"], i)
        if r != corrupt_f1(it["task"], i):
            raise CorrStop(f"F1 REPLAY STOP: trace and corrupt_f1 disagree on item {i}")
        changed = sum(1 for a, b in zip(it["task"], r) if a != b)
        # PIN (Code, declared at LOCK v0.1): f1 has no k, so condition (2) is reported as
        # changed <= floor(n_eligible / 2) with n_eligible under f1's own rule (non-word-start
        # letters, operands included).
        rows.append({"i": i, "n_eligible": n_el, "hits": hits, "changed": changed,
                     "cond1": changed >= 3, "cond2": changed <= n_el // 2, "render": r})
        renders.append(r)
    sha = renders_sha(renders)
    calib = json.loads(Path(calib_path).read_text())
    return {
        "rule": "f1 corrupt() at 0.12, f_sessions.py:106-116 (26-letter draw, may repeat)",
        "items": rows,
        "n_hits": sum(x["hits"] for x in rows),
        "n_changed": sum(x["changed"] for x in rows),
        "n_cond1": sum(x["cond1"] for x in rows),
        "n_cond2": sum(x["cond2"] for x in rows),
        "renders_sha16": sha,
        "calib_corr_sha16": calib.get("corr_sha"),
        "calib_pools_sha16": calib.get("pools_sha"),
        "renders_sha_matches_calib": sha == calib.get("corr_sha"),
        "covariate_of_record": repr(calib.get("CORR_delta_covariate")),
    }


# --- item streams and delivery -----------------------------------------------

class ItemStreams:
    """One `permutation(16)` from an injected rng: P = perm[:8], Q = perm[8:16] (m:159)."""

    def __init__(self, rng: np.random.Generator):
        # PIN (Code, declared at LOCK v0.1): the rng must be a numpy Generator; ItemStreams
        # draws nothing from it after the one permutation(16).
        if not isinstance(rng, np.random.Generator):
            raise TypeError(f"ItemStreams takes a numpy Generator, got {type(rng).__name__}")
        perm = rng.permutation(N_ITEMS)
        self.P_idx = tuple(int(x) for x in perm[:N_PER_ROLE])
        self.Q_idx = tuple(int(x) for x in perm[N_PER_ROLE:2 * N_PER_ROLE])
        self._used = {"P": 0, "Q": 0}

    def next(self, role: str) -> int:
        """The role's next pool index, in order; a ninth draw raises (no wrap)."""
        if role not in ROLES:
            raise ValueError(f"role must be 'P' or 'Q', got {role!r}")
        j = self._used[role]
        if j >= N_PER_ROLE:
            raise ItemStreamExhausted(f"role {role} drew item {j + 1} of {N_PER_ROLE}: no wrap")
        self._used[role] = j + 1
        return (self.P_idx if role == "P" else self.Q_idx)[j]

    def drawn(self, role: str) -> int:
        if role not in ROLES:
            raise ValueError(f"role must be 'P' or 'Q', got {role!r}")
        return self._used[role]


class Delivery:
    """Role -> (task text, property): P clean; Q render on a contrast arm, clean on a sham."""

    def __init__(self, pool: Sequence[dict], renders: Sequence[str], contrast: bool):
        if not isinstance(contrast, bool):
            raise TypeError(f"contrast must be a bool, got {contrast!r}")
        if len(pool) != N_ITEMS or len(renders) != N_ITEMS:
            raise ValueError(f"Delivery needs {N_ITEMS} items and {N_ITEMS} renders, got "
                             f"{len(pool)} / {len(renders)}")
        if not all(isinstance(r, str) for r in renders):
            raise TypeError("renders must be strings")
        self.clean = tuple(it["task"] for it in pool)
        self.renders = tuple(renders)
        self.contrast = contrast
        self.renders_sha = renders_sha(self.renders)

    def text(self, role: str, i: int) -> tuple[str, str]:
        if role not in ROLES:
            raise ValueError(f"role must be 'P' or 'Q', got {role!r}")
        if isinstance(i, bool) or not isinstance(i, int) or not 0 <= i < N_ITEMS:
            raise ValueError(f"pool index must be an int in 0..{N_ITEMS - 1}, got {i!r}")
        # PIN (Code, declared at LOCK v0.1): the property is the arm's delivery, not a byte
        # diff -- a contrast Q round is "corrupted" even where a render equals the clean text
        # (f1's items 1 and 12 at 0.12, maps/f1.md §5 item 5).
        if role == "Q" and self.contrast:
            return self.renders[i], CORRUPTED
        return self.clean[i], CLEAN


# --- hygiene (m:258; rule 18 / 28(c)) ------------------------------------------

_PLACEHOLDER = re.compile(r"\{[^{}]*\}")


def hygiene(rosters, strings: Iterable[str], *, pool: Sequence[dict] | None = None,
            renders: Sequence[str] | None = None) -> list[str]:
    """Roster words vs clean tasks, golds, renders and harness strings; [] = clean."""
    if isinstance(strings, str):
        raise TypeError("strings is a sequence of harness strings, not a string")
    words = _roster_words(rosters)
    problems: list[str] = []
    pool = load_pool() if pool is None else pool
    if renders is None:
        # PIN (Code, declared at LOCK v0.1): hygiene renders under the rosters it checks (m
        # passes ROSTERS_OF_RECORD, so these are the renders of record); a render walk that
        # STOPs is reported as a problem here rather than raised.
        try:
            renders = renders_m(pool, rosters)
        except CorrStop as e:
            problems.append(f"renders: {e}")
            renders = []
    texts: list[tuple[str, str]] = []
    for i, it in enumerate(pool):
        texts.append((f"clean[{i}]", it["task"]))
        texts += [(f"gold[{i}]", g) for g in it["gold"]]
    texts += [(f"render[{i}]", r) for i, r in enumerate(renders)]
    for j, s in enumerate(strings):
        if not isinstance(s, str):
            raise TypeError(f"harness string {j} is not a string: {s!r}")
        # PIN (Code, declared at LOCK v0.1): placeholders blanked to one space (format_recon
        # .py:112's form), any {...} span.
        texts.append((f"harness[{j}]", _PLACEHOLDER.sub(" ", s)))
    for w in words:
        rx = re.compile(rf"\b{re.escape(w)}\b", re.I)
        problems += [f"{src}: roster word {w!r} in {t[:60]!r}" for src, t in texts if rx.search(t)]
    return problems


def startup_hygiene() -> list[str]:
    """Rule 18 / 28(c) / m:258 roster admissibility at stage startup; [] = clean.

    Both rosters of record against the clean pool text, the golds, the renders of
    record (``hygiene``'s own PIN), m:258's eight declared harness strings
    (``banner.DECLARED_HARNESS_STRINGS``) and e2a's wrapper templates
    (``SESSION_BANNER``, ``ROUND_TEMPLATES``, ``MENU_TEMPLATES``, ``{fields}`` blanked;
    rule 28(c): roster tokens are checked against the wrapper, not only the pools).
    PIN (Code, declared at LOCK v0.1): every stage driver runs it before any session and
    STOPs on a non-empty list; a pool that fails its pin is a problem, never a raise.
    """
    from ..session_e2a import MENU_TEMPLATES, ROUND_TEMPLATES, SESSION_BANNER
    from . import banner

    strings = tuple(banner.DECLARED_HARNESS_STRINGS) + (SESSION_BANNER,) \
        + tuple(ROUND_TEMPLATES) + tuple(MENU_TEMPLATES)
    try:
        pool = load_pool()
    except CorrStop as e:
        return [f"pool: {e}"]
    return hygiene(ROSTERS_OF_RECORD, strings, pool=pool)


# --- self-test ------------------------------------------------------------------

def _selftest(chk) -> None:
    import tempfile

    from . import banner

    pool = load_pool()
    rosters = ROSTERS_OF_RECORD

    # pool
    chk("corr: load_pool accepts the pinned pool (16 ASCII items)",
        len(pool) == 16 and all(it["task"].isascii() for it in pool), len(pool))
    raw = POOLS_PATH.read_bytes()
    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "pools.json"
        bad.write_bytes(raw.replace(b"Compute 31 + 46.", b"Compute 31 + 47.", 1))
        try:
            load_pool(bad)
            ok = False
        except CorrStop as e:
            ok = "SHA" in str(e)
        chk("corr: load_pool refuses a pool whose sha256 is not 8547d9a11ba55b95", ok)
    obj = json.loads(raw)
    refused = []
    for mut in ("nonascii", "short", "shape"):
        o = json.loads(raw)
        if mut == "nonascii":
            o["CORR_clean"][3]["task"] = "Compute 60 divided by 5…"
        elif mut == "short":
            o["CORR_clean"] = o["CORR_clean"][:15]
        else:
            o["CORR_clean"][0]["extra"] = 1
        try:
            _validate_pool(o)
            refused.append(False)
        except CorrStop:
            refused.append(True)
    chk("corr: pool validation refuses non-ASCII / 15 items / bad record shape",
        all(refused) and _validate_pool(obj) == pool, refused)

    # rosters
    chk("corr: QWEN_ROSTER is e2d.config.ROSTER (imported, not re-literalled)",
        QWEN_ROSTER is _e2d_config.ROSTER)
    chk("corr: olmo_roster is a1_repair_roster selected_tags (4 pairs)",
        olmo_roster() == (("quartz", "velvet"), ("copper", "walnut"), ("maple", "saddle"),
                          ("amber", "granite")), olmo_roster())
    with tempfile.TemporaryDirectory() as td:
        p3 = Path(td) / "r.json"
        p3.write_text(json.dumps({"selected_tags": [["quartz", "velvet"], ["copper", "walnut"],
                                                    ["maple", "saddle"]]}))
        try:
            olmo_roster(p3)
            ok = False
        except CorrStop:
            ok = True
        chk("corr: olmo_roster refuses a roster that is not 4 pairs", ok)
    chk("corr: ALL_ROSTER_WORDS = sorted union, 12 words (4 shared)",
        len(ALL_ROSTER_WORDS) == 12 and list(ALL_ROSTER_WORDS) == sorted(ALL_ROSTER_WORDS)
        and {"granite", "saddle", "velvet", "walnut"} <= set(ALL_ROSTER_WORDS), ALL_ROSTER_WORDS)

    # corrupt_m known answers (m:176; maps/audit.md §6)
    res = [corrupt_m(it["task"], i, rosters) for i, it in enumerate(pool)]
    rm = [r for r, _ in res]
    metas = [m for _, m in res]
    n_el = [m["n_eligible"] for m in metas]
    chk("corr: corrupt_m n_eligible == m:176's list",
        n_el == [6, 19, 19, 13, 24, 14, 10, 45, 19, 10, 24, 14, 6, 19, 10, 14], n_el)
    chk("corr: corrupt_m k sums to 54", sum(m["k"] for m in metas) == 54,
        sum(m["k"] for m in metas))
    skips = [i for i, m in enumerate(metas) if m["n_skips"]]
    chk("corr: corrupt_m skips exactly once, at item 7",
        skips == [7] and metas[7]["n_skips"] == 1, [(i, metas[i]["n_skips"]) for i in skips])
    chk("corr: corrupt_m items 5/11/15 render verbatim (m:176)",
        (rm[5], rm[11], rm[15]) == ("Writa the oppcsite oc 'hot'.", "Writo the oppssitu of 'up'.",
                                    "Wtite thn opposite on 'open'."), (rm[5], rm[11], rm[15]))
    chk("corr: corrupt_m gold-bearing words miyms (9) / thiru (2) / ftrst (8)",
        "miyms" in rm[9] and "thiru" in rm[2] and "ftrst" in rm[8], (rm[9], rm[2], rm[8]))
    chk("corr: corrupt_m changes exactly k letters per item, all at reported eligible positions",
        all(sum(a != b for a, b in zip(it["task"], r)) == m["k"]
            and [j for j, (a, b) in enumerate(zip(it["task"], r)) if a != b] == m["changed_positions"]
            and set(m["changed_positions"]) <= set(_eligible_m(it["task"]))
            for it, r, m in zip(pool, rm, metas)))
    chk("corr: corrupt_m consumes one draw per visited slot (n_visited == k + n_skips)",
        all(m["n_visited"] == m["k"] + m["n_skips"] for m in metas))
    walk_ok = [_walk_consistent(it["task"], i, r, m)
               for i, (it, r, m) in enumerate(zip(pool, rm, metas))]
    p5 = metas[5]["changed_positions"][0]                             # a wrong letter at a changed slot
    r5 = rm[5][:p5] + ("q" if rm[5][p5] != "q" else "r") + rm[5][p5 + 1:]
    chk("corr: corrupt_m draw order = permutation(n), then one integers(25) per visited slot",
        all(walk_ok) and not _walk_consistent(pool[5]["task"], 5, r5, metas[5]), walk_ok)
    chk("corr: _eligible_m excludes word-initial letters and the quoted operand",
        _eligible_m("Ab 'cd' ef") == [1, 9] and _eligible_m("x9y") == [], _eligible_m("Ab 'cd' ef"))
    refusals = []
    # a roster word inside the untouchable operand survives every trial: every slot skips
    for fn in (lambda: corrupt_m("Write the opposite of 'hot'.", 5, ((("hot", "zzzzq"),),)),
               lambda: corrupt_m("Café time", 0, rosters),
               lambda: corrupt_m("Write the opposite of 'hot.", 0, rosters),
               lambda: corrupt_m("Compute 31 + 46.", 0, "slate"),
               lambda: corrupt_m("Compute 31 + 46.", -1, rosters)):
        try:
            fn()
            refusals.append(False)
        except (CorrStop, ValueError, TypeError):
            refusals.append(True)
    chk("corr: corrupt_m refuses (walk runs dry; non-ASCII; odd quote; bare-string roster; i<0)",
        all(refusals), refusals)
    chk("corr: corrupt_m roster skip fires only where a roster substring would form",
        corrupt_m(pool[7]["task"], 7, (QWEN_ROSTER,))[1]["n_skips"]
        + corrupt_m(pool[7]["task"], 7, (OLMO_ROSTER,))[1]["n_skips"] == 1
        and corrupt_m(pool[0]["task"], 0, rosters)[1]["n_skips"] == 0)

    # renders_m / renders_sha
    rm2 = renders_m(pool, rosters)
    chk("corr: renders_m == corrupt_m renders, deterministic, no roster substring",
        rm2 == rm == renders_m(pool, rosters)
        and not any(w in r.lower() for r in rm2 for w in ALL_ROSTER_WORDS), renders_sha(rm2))
    try:
        renders_m(pool[:15], rosters)
        ok = False
    except CorrStop:
        ok = True
    chk("corr: renders_m refuses a pool that is not 16 items", ok)
    alt = list(rm2)
    alt[0] = alt[0] + " "
    chk("corr: renders_sha = sha256 of newline-joined renders [:16]; moves on a 1-byte change",
        renders_sha(rm2) == hashlib.sha256("\n".join(rm2).encode()).hexdigest()[:16]
        and renders_sha(alt) != renders_sha(rm2) and len(renders_sha(rm2)) == 16)

    # corrupt_f1 (f1 at 0.12) known answers
    rf = renders_f1(pool)
    n_changed = sum(sum(a != b for a, b in zip(it["task"], r)) for it, r in zip(pool, rf))
    chk("corr: corrupt_f1 renders sha16 2c2c227395ea9f2d (= calib corr_sha)",
        renders_sha(rf) == F1_012_SHA16, renders_sha(rf))
    chk("corr: corrupt_f1 changes 31 letters in total", n_changed == 31, n_changed)
    chk("corr: corrupt_f1 leaves items 1 and 12 unchanged, changes items 2/4/6/7",
        rf[1] == pool[1]["task"] and rf[12] == pool[12]["task"]
        and all(rf[i] != pool[i]["task"] for i in (2, 4, 6, 7)))
    chk("corr: corrupt_f1 never touches a word-initial letter (f1's word_start rule)",
        all(a == b for it, r in zip(pool, rf) for j, (a, b) in enumerate(zip(it["task"], r))
            if j == 0 or not it["task"][j - 1].isalpha()))
    chk("corr: corrupt_f1 item 5 hits the 'of' outside the operand; item 15 hits the operand",
        rf[5] == "Write the opposite oy 'hot'." and rf[15] == "Write the opposite of 'opev'.",
        (rf[5], rf[15]))

    # f1_012_replay
    rep = f1_012_replay(pool)
    chk("corr: f1_012_replay per-item n_eligible / hits / changed (maps/f1.md §3)",
        [x["n_eligible"] for x in rep["items"]] == [6, 19, 19, 13, 24, 16, 10, 45, 19, 10, 24, 15,
                                                     6, 19, 10, 17]
        and [x["hits"] for x in rep["items"]] == [1, 0, 5, 2, 3, 1, 4, 6, 3, 1, 2, 1, 0, 1, 1, 1]
        and [x["changed"] for x in rep["items"]] == [1, 0, 5, 2, 3, 1, 4, 6, 2, 1, 2, 1, 0, 1, 1, 1],
        (rep["n_hits"], rep["n_changed"]))
    chk("corr: f1_012_replay cond1 holds on items 2/4/6/7 only; cond2 on all 16",
        [x["i"] for x in rep["items"] if x["cond1"]] == [2, 4, 6, 7] and rep["n_cond2"] == 16,
        (rep["n_cond1"], rep["n_cond2"]))
    chk("corr: f1_012_replay sha == calib corr_sha; covariate quoted as stored",
        rep["renders_sha16"] == F1_012_SHA16 and rep["renders_sha_matches_calib"]
        and rep["calib_pools_sha16"] == POOLS_SHA16 and rep["covariate_of_record"] == "0.078125",
        rep["covariate_of_record"])

    # ItemStreams
    s = ItemStreams(keys.stream("m-items|3"))
    ref = keys.stream("m-items|3").permutation(16).tolist()
    chk("corr: ItemStreams splits one permutation(16) [:8] P / [8:] Q",
        list(s.P_idx) == ref[:8] and list(s.Q_idx) == ref[8:], (s.P_idx, s.Q_idx))
    g = keys.stream("f|CORR|0")
    ItemStreams(g)
    fresh = keys.stream("f|CORR|0")
    fresh.permutation(16)
    chk("corr: ItemStreams consumes exactly one permutation(16) of the injected rng",
        int(g.integers(2**31)) == int(fresh.integers(2**31)))
    got_p = [s.next("P") for _ in range(8)]
    got_q = [s.next("Q") for _ in range(8)]
    chk("corr: ItemStreams serves each role's 8 indices in order",
        got_p == ref[:8] and got_q == ref[8:] and s.drawn("P") == 8, got_p)
    refused = []
    for fn in (lambda: s.next("P"), lambda: s.next("Q"), lambda: s.next("X"),
               lambda: ItemStreams(np.random.RandomState(0))):
        try:
            fn()
            refused.append(False)
        except (ItemStreamExhausted, ValueError, TypeError):
            refused.append(True)
    chk("corr: ItemStreams refuses a 9th draw per role, an unknown role, a non-Generator",
        all(refused), refused)

    # Delivery
    dc = Delivery(pool, rm, contrast=True)
    ds = Delivery(pool, rm, contrast=False)
    chk("corr: Delivery contrast: P -> clean, Q -> render 'corrupted'",
        dc.text("P", 5) == (pool[5]["task"], "clean")
        and dc.text("Q", 5) == ("Writa the oppcsite oc 'hot'.", "corrupted"))
    chk("corr: Delivery sham serves CORR_clean to both roles (m:159)",
        all(ds.text(r, i) == (pool[i]["task"], "clean") for r in ROLES for i in range(16)))
    refused = []
    for fn in (lambda: dc.text("X", 0), lambda: dc.text("P", 16), lambda: dc.text("Q", True),
               lambda: Delivery(pool, rm[:15], True), lambda: Delivery(pool, rm, 1)):
        try:
            fn()
            refused.append(False)
        except (ValueError, TypeError):
            refused.append(True)
    chk("corr: Delivery refuses bad role / index / render count / non-bool contrast",
        all(refused), refused)

    # hygiene (m:258)
    five = banner.HARNESS_STRINGS_QF0
    chk("corr: hygiene clean on pool + golds + renders + the five Q-F0 strings, both rosters",
        hygiene(rosters, five) == [] and hygiene((QWEN_ROSTER,), five) == []
        and hygiene((OLMO_ROSTER,), five) == [], hygiene(rosters, five)[:2])
    planted = hygiene(rosters, list(five) + ["Note: config walnut presents clean task text."])
    chk("corr: hygiene fires on a roster word planted in a harness string",
        len(planted) == 1 and "walnut" in planted[0], planted)
    p2 = [dict(it) for it in pool]
    p2[4] = {"task": "State the number of sides of a prism.", "gold": ["3"]}
    p3_ = [dict(it) for it in pool]
    p3_[0] = {"task": pool[0]["task"], "gold": ["77", "Amber"]}
    r_pl = list(rm)
    r_pl[2] = "Name the third month of the copper."
    fired = (any("clean[4]" in x for x in hygiene(rosters, five, pool=p2, renders=rm)),
             any("gold[0]" in x for x in hygiene(rosters, five, pool=p3_, renders=rm)),
             any("render[2]" in x for x in hygiene(rosters, five, renders=r_pl)),
             any("clean[" in x for x in hygiene(rosters + ((("month", "week"),),), five)))
    chk("corr: hygiene fires on a roster word in a clean task / gold / render / via the roster",
        all(fired), fired)
    chk("corr: hygiene blanks {...} placeholders and is word-boundary (no fire)",
        hygiene(rosters, ["Note: config {slate} runs.", "Note: slates and graniteware."]) == [])
    from ..session_e2a import MENU_TEMPLATES, ROUND_TEMPLATES, SESSION_BANNER
    chk("corr: hygiene clean on e2a's wrapper strings too (rule 28(c))",
        hygiene(rosters, (SESSION_BANNER,) + ROUND_TEMPLATES + MENU_TEMPLATES) == [])
    try:
        hygiene(rosters, "Note: one string")
        ok = False
    except TypeError:
        ok = True
    chk("corr: hygiene refuses a bare string as the harness-string list", ok)

    # startup_hygiene (C4): the eight declared strings + e2a's wrapper, both rosters
    eight = banner.DECLARED_HARNESS_STRINGS
    chk("corr: startup_hygiene is clean on the real pool, golds, renders, the EIGHT declared "
        "strings of m:258 and e2a's wrapper templates",
        startup_hygiene() == [] and len(eight) == 8 and banner.TOLD_OBJ in eight
        and hygiene(rosters, eight) == [], startup_hygiene()[:2])
    from unittest import mock

    import valence_core.session_e2a as _e2a
    planted_runs = {}
    with mock.patch.object(banner, "DECLARED_HARNESS_STRINGS",
                           eight[:5] + ("Note: configs walnut can differ.",) + eight[6:]):
        planted_runs["TOLD-OBJ slot"] = startup_hygiene()
    with mock.patch.object(banner, "DECLARED_HARNESS_STRINGS",
                           eight[:7] + ("Reasoning about granite (one line):",)):
        planted_runs["reasoning line"] = startup_hygiene()
    with mock.patch.object(_e2a, "MENU_TEMPLATES",
                           tuple(_e2a.MENU_TEMPLATES) + ("[round {n} | velvet choice]\n",)):
        planted_runs["e2a wrapper"] = startup_hygiene()
    with mock.patch(f"{__name__}.ROSTERS_OF_RECORD", rosters + ((("month", "week"),),)):
        planted_runs["a roster word in the pool"] = startup_hygiene()
    want = {"TOLD-OBJ slot": "walnut", "reasoning line": "granite", "e2a wrapper": "velvet",
            "a roster word in the pool": "month"}
    chk("corr: startup_hygiene fires on a roster word planted in a declared string (TOLD-OBJ's "
        "slot, a reasoning line), in e2a's wrapper, and via the roster",
        all(v and any(want[k] in x for x in v) for k, v in planted_runs.items()),
        {k: v[:1] for k, v in planted_runs.items()})


def _walk_consistent(text: str, i: int, render: str, meta: dict) -> bool:
    """Selftest helper, independent of corrupt_m's loop: a fresh `corr|{i}` stream drawn as
    permutation(n) then one scalar integers(25) per visited slot must explain the render --
    every changed position among the first n_visited slots, carrying its slot's replacement,
    the rest of the visited slots being the skips."""
    el = _eligible_m(text)
    rng = keys.stream(f"corr|{i}")
    order = [el[int(x)] for x in rng.permutation(len(el))]
    visited = order[:meta["n_visited"]]
    want = {p: chr(ord("a") + ((ord(text[p].lower()) - ord("a") + 1 + int(rng.integers(25))) % 26))
            for p in visited}
    changed = [j for j, (a, b) in enumerate(zip(text, render)) if a != b]
    return (len(render) == len(text) and set(changed) <= set(visited)
            and all(render[p] == want[p] for p in changed)
            and len(visited) - len(changed) == meta["n_skips"]
            and (not visited or visited[-1] in changed))
