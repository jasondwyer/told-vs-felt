"""PROPOSAL-m session scaffold -- ONE code path for the F0m and F0m-OLMo runners, their
verifiers and G-PORT (v1.11 §2.1 m:159; §2.2 m:173; §2.5 m:253; §3.1 G-PORT/G-VER
m:276-284; maps/f1.md §4-§5 "stateful session scaffold").

THE SCAFFOLD. A session's harness bytes are a function of its banner, its cell (P, Q,
start), its rotation offset s, its arm rng (seeds and menu orders), its item streams
and its delivery map -- plus, from the first free choice on, the picks. A
``SessionScaffold`` holds exactly those inputs and hands them out in m:159's order:

  forced(ri)       -> RoundSpec: the role of start order (0 -> P Q P Q, 1 -> Q P Q P),
                      that role's next item, its delivered text and property, header
                      ``ROUND_TEMPLATES[(s + ri) % 4]`` with n = ri + 1, then ONE seed
                      ``int(rng.integers(2**31))`` (f_sessions.py:312; session_e2a.py:154);
  menu(ci)         -> MenuSpec: ``rng.integers(2)`` (0 -> (P, Q), 1 -> (Q, P);
                      f_sessions.py:351, session_e2a.py:164-165), menu
                      ``MENU_TEMPLATES[(s + ci) % 4]`` with n = 2F + 1 + ci;
  chosen(ci, pick) -> RoundSpec: the pick's role's next item, header
                      ``ROUND_TEMPLATES[(s + ci) % 4]`` sharing the menu's n, then one seed.

The runner drives it online with live picks; the verifier and G-PORT drive it from
RECORDED picks. Calls out of that order are refused (a harness bug, not a session).
m:159 states the rotation as ``(s + i) % 4`` for the i-th round; e2a and f1 key the
chosen round on ci. The two agree because 2F = 4 = 0 (mod 4), asserted at
construction (maps/f1.md §5 item 3).

CONFIGURATIONS. ``m_config``: m's split streams -- the arm rng
``stream(arm_key(...))`` for seeds and menu orders, ``ItemStreams(stream(item_key(...)))``
for items, the committed-schedule cell, §2.5's banner, ``corrupt_m`` renders on a
contrast arm's Q role. ``f1_config``: f1's single session rng ``f|CORR|{s}``, the
item permutation drawn FIRST from it and the seeds and menus after (f_sessions.py:
253-259, :273-274), f1's TAG_PAIRS cell arithmetic (:275-278), SESSION_BANNER alone,
``corrupt_f1`` at 0.12. ``replay_f1_row`` walks an archived f1 CORR row through the
f1 configuration (G-PORT's algorithm, maps/f1.md §4); the 64/64 replay is G-PORT's
(step 5), not this module's.

RECORDS. ``SessionLog`` and ``TranscriptBuilder`` are the one place an
``m-session-v1`` record (build design §2) and its char-offset ``pieces`` are built,
so the readrule's piece validator and the verifier's rebuild see one layout:
banner; forced rounds ``round, generation, joiner``; free rounds on Qwen ``menu,
pick, round, generation, joiner`` (f_sessions.py:358), on OLMo ``round, generation,
joiner`` (b3's context rule, box_b3_sessions.py:202).

Nothing here touches a model; ``assert_boundary`` (rule 28(d)(a)) only encodes.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

from ..session_e2a import MENU_TEMPLATES, N_FREE, ROUND_TEMPLATES, SESSION_BANNER
from . import banner as _banner
from . import corr, keys, schedule

REPO = Path(__file__).resolve().parents[2]
SCHEMA = "m-session-v1"
N_FORCED = 4                       # 2F, F = 2 per label (e2d/config.py:40; box_b3_sessions.py:76)
ROLE_POLE = {"P": "pos", "Q": "neg"}   # habit.py's "pos" = the P-role (clean) label (maps/e2a.md §5)
TERM_PATH = REPO / "data" / "configs" / "f_termination_patterns.json"
TERM_SHA16 = "014b3940d62401b0"    # maps/f1.md §0
F1_SESSIONS_PATH = REPO / "data" / "f" / "sessions.jsonl"
F1_SESSIONS_SHA16 = "d49913e5ffdfb935"   # maps/f1.md §0 (344 rows)
#: f1's TAG_PAIRS (f_sessions.py:61-64), G-PORT's roster; never an m roster.
F1_TAG_PAIRS = (("slate", "prism"), ("maple", "cedar"), ("granite", "lattice"), ("plaza", "saddle"))
F1_VERIFY_EVERY = 4                # f_sessions.py:597-608, verify at (s*6 + ci) % 4 == 0
_CELL_KEYS = ("pair_index", "pair", "map", "start", "clause", "P", "Q")


class ScaffoldOrderError(RuntimeError):
    """A scaffold method called out of m:159's order: a harness bug."""


@dataclass(frozen=True)
class RoundSpec:
    phase: str            # "forced" | "free"
    idx: int              # ri (forced) or ci (free)
    n: int                # 1-based over all rounds; a menu and its chosen round share it
    label: str
    role: str             # "P" | "Q"
    item: int             # CORR pool index
    task_text: str        # as delivered (clean text or the render)
    property: str         # "clean" | "corrupted"
    template_index: int
    seg: str              # header + Task line + "Response:"
    seed: int

    @property
    def pole(self) -> str:
        return ROLE_POLE[self.role]


@dataclass(frozen=True)
class MenuSpec:
    ci: int
    n: int
    a: str
    b: str
    menu_index: int
    menu: str


class SessionScaffold:
    """The stateful harness of one session (see the module docstring)."""

    def __init__(self, *, banner: str, cell: Mapping[str, Any], s: int,
                 arm_rng: np.random.Generator, items: corr.ItemStreams,
                 delivery: corr.Delivery, note_lines: Sequence[str] = (),
                 n_forced: int = N_FORCED, n_free: int = N_FREE,
                 meta: Mapping[str, Any] | None = None) -> None:
        if type(n_forced) is not int or n_forced <= 0 or n_forced % 4 != 0:
            raise ValueError(f"rotation pin: 2F % 4 must be 0 so (s + ci) == (s + 2F + ci) mod 4; "
                             f"2F = {n_forced}")
        if not isinstance(arm_rng, np.random.Generator):
            raise TypeError("arm_rng must be a numpy Generator")
        if type(s) is not int or s < 0:
            raise ValueError(f"s must be a non-negative int, got {s!r}")
        P, Q, start = cell["P"], cell["Q"], cell["start"]
        if P == Q or start not in (0, 1) or isinstance(start, bool):
            raise ValueError("cell: P and Q must differ and start must be 0 or 1")
        self.banner = banner
        self.cell = _copy_cell(cell)
        self.note_lines = tuple(note_lines)
        self.s = s
        self.P, self.Q, self.start = P, Q, start
        self.arm_rng = arm_rng
        self.items = items
        self.delivery = delivery
        self.n_forced, self.n_free = n_forced, n_free
        first, second = ("P", "Q") if start == 0 else ("Q", "P")
        self.order = tuple(first if i % 2 == 0 else second for i in range(n_forced))
        self.meta = dict(meta or {})
        self._ri = 0
        self._ci = 0
        self._menu: MenuSpec | None = None

    # metadata, for records
    def __getattr__(self, name: str) -> Any:
        meta = self.__dict__.get("meta", {})
        if name in meta:
            return meta[name]
        raise AttributeError(name)

    def label_of(self, role: str) -> str:
        return self.P if role == "P" else self.Q

    def role_of(self, label: str) -> str:
        if label == self.P:
            return "P"
        if label == self.Q:
            return "Q"
        raise ValueError("pick is not one of the session's own two labels")

    def _round(self, phase: str, idx: int, n: int, role: str, ti: int) -> RoundSpec:
        item = self.items.next(role)
        task_text, prop = self.delivery.text(role, item)
        label = self.label_of(role)
        seg = ROUND_TEMPLATES[ti].format(n=n, tag=label, task=task_text)
        seed = int(self.arm_rng.integers(2**31))          # drawn after the segment is built
        return RoundSpec(phase=phase, idx=idx, n=n, label=label, role=role, item=item,
                         task_text=task_text, property=prop, template_index=ti, seg=seg, seed=seed)

    def forced(self, ri: int) -> RoundSpec:
        if ri != self._ri or ri >= self.n_forced or self._ci or self._menu is not None:
            raise ScaffoldOrderError(f"forced({ri}) out of order (next forced {self._ri})")
        self._ri += 1
        return self._round("forced", ri, ri + 1, self.order[ri], (self.s + ri) % 4)

    def menu(self, ci: int) -> MenuSpec:
        if self._ri != self.n_forced or ci != self._ci or ci >= self.n_free or self._menu is not None:
            raise ScaffoldOrderError("menu() out of order")
        o = int(self.arm_rng.integers(2))
        a, b = (self.P, self.Q) if o == 0 else (self.Q, self.P)
        mi = (self.s + ci) % 4
        n = self.n_forced + 1 + ci
        self._menu = MenuSpec(ci=ci, n=n, a=a, b=b, menu_index=mi,
                              menu=MENU_TEMPLATES[mi].format(n=n, a=a, b=b))
        return self._menu

    def chosen(self, ci: int, pick: str) -> RoundSpec:
        m = self._menu
        if m is None or m.ci != ci:
            raise ScaffoldOrderError("chosen() without its menu")
        if pick not in (m.a, m.b):
            raise ValueError("pick is not one of the menu's two labels")
        role = self.role_of(pick)
        self._menu = None
        self._ci += 1
        # PIN (Code, declared at LOCK v0.1): the chosen round's template index is e2a's
        # literal (s + ci) % 4 (session_e2a.py:169), equal to m:159's (s + i) % 4 for
        # i = 2F + ci because 2F % 4 == 0 (asserted in __init__).
        spec = self._round("free", ci, m.n, role, (self.s + ci) % 4)
        assert spec.template_index == (self.s + self.n_forced + ci) % 4
        return spec


# --- configurations -------------------------------------------------------------
def _copy_cell(c: Mapping[str, Any]) -> dict:
    d = {k: c[k] for k in c}
    if "pair" in d:
        d["pair"] = list(d["pair"])
    return d


@lru_cache(maxsize=None)
def _of_record() -> tuple[tuple[dict, ...], tuple[str, ...]]:
    pool = corr.load_pool()
    return tuple(pool), tuple(corr.renders_m(pool, corr.ROSTERS_OF_RECORD))


def pool_and_renders() -> tuple[list[dict], list[str]]:
    """CORR_clean (sha-pinned) and the 16 corrupt_m renders of record, cached."""
    pool, renders = _of_record()
    return [dict(p) for p in pool], list(renders)


def check_cell(unit: str, cell: Mapping[str, Any]) -> dict:
    """A cell of the unit's roster of record in m:159's form, or ValueError."""
    if not isinstance(cell, Mapping) or tuple(sorted(cell)) != tuple(sorted(_CELL_KEYS)):
        raise ValueError(f"cell keys must be exactly {_CELL_KEYS}")
    roster = schedule.roster_for(unit)
    pi, mp, st, cl = cell["pair_index"], cell["map"], cell["start"], cell["clause"]
    for nm, v in (("pair_index", pi), ("map", mp), ("start", st), ("clause", cl)):
        if type(v) is not int:
            raise ValueError(f"cell {nm} must be an int, got {v!r}")
    if not 0 <= pi < len(roster) or mp not in (0, 1) or st not in (0, 1) or cl not in (0, 1):
        raise ValueError("cell factor out of range")
    pair = list(roster[pi])
    if list(cell["pair"]) != pair or cell["P"] != pair[mp] or cell["Q"] != pair[1 - mp]:
        raise ValueError("cell pair / P / Q disagree with the roster of record and the map")
    return _copy_cell(cell)


def m_config(unit: str, stage: str, template: str, s: int, cell: Mapping[str, Any], path: str,
             *, pool: Sequence[dict] | None = None,
             renders: Sequence[str] | None = None) -> SessionScaffold:
    """m's scaffold for one session: split streams, scheduled cell, §2.5 banner."""
    keys.templates(unit)                               # refuses Q-F3 and base
    substrate = "qwen" if unit == "Q-F0" else "olmo"
    if type(s) is not int or s < 0:
        raise ValueError(f"s must be a non-negative int, got {s!r}")
    # PIN (Code, declared at LOCK v0.1): path is "cached" or "uncached" per session; OLMo
    # and G-TIME-F0 are uncached by spec (m:267, m:280); the scaffold records it, the
    # runner's cached argument must agree with it.
    if path not in ("cached", "uncached") or (path == "cached" and (substrate == "olmo" or stage == "time")):
        raise ValueError(f"path {path!r} not allowed for {unit} {stage}")
    c = check_cell(unit, cell)
    arm_key = keys.arm_key(unit, stage, template, s)
    item_key = keys.item_key(unit, s, keys.item_gate(stage))
    if pool is None or renders is None:
        p0, r0 = pool_and_renders()
        pool = p0 if pool is None else pool
        renders = r0 if renders is None else renders
    contrast = keys.is_contrast(template)
    text, note_lines = _banner.build_banner(template, c["P"], c["Q"], c["clause"])
    # PIN (Code, declared at LOCK v0.1): j = s at gate stages (session j of the
    # sixteen-row table is the template's s-th launch, m:159), None in a campaign.
    meta = {"substrate": substrate, "unit": unit, "stage": stage, "template": template,
            "contrast": contrast, "path": path, "j": None if stage == "campaign" else s,
            "keys": {"arm": arm_key, "items": item_key}}
    return SessionScaffold(banner=text, cell=c, s=s, arm_rng=keys.stream(arm_key),
                           items=corr.ItemStreams(keys.stream(item_key)),
                           delivery=corr.Delivery(pool, renders, contrast=contrast),
                           note_lines=note_lines, meta=meta)


def f1_cell(s: int) -> dict:
    """f1's cell arithmetic (f_sessions.py:275-278) in m's cell form."""
    pair = F1_TAG_PAIRS[s % 4]
    swap = (s // 4) % 2 == 1
    start_P = (s // 8) % 2 == 0
    mp = 1 if swap else 0
    return {"pair_index": s % 4, "pair": list(pair), "map": mp, "start": 0 if start_P else 1,
            "clause": None, "P": pair[mp], "Q": pair[1 - mp]}


def f1_config(s: int, pool: Sequence[dict], *, renders: Sequence[str] | None = None) -> SessionScaffold:
    """f1's CORR session for G-PORT: one rng, items first, f1 cell, bare banner, 0.12."""
    rng = keys.stream(f"f|CORR|{s}")
    items = corr.ItemStreams(rng)                      # the permutation(16) comes first
    rend = corr.renders_f1(pool) if renders is None else renders
    meta = {"substrate": "qwen", "unit": None, "stage": "g-port", "template": "f1-CORR",
            "contrast": True, "path": None, "j": None, "keys": {"arm": f"f|CORR|{s}",
                                                                "items": f"f|CORR|{s}"}}
    return SessionScaffold(banner=SESSION_BANNER, cell=f1_cell(s), s=s, arm_rng=rng, items=items,
                           delivery=corr.Delivery(pool, rend, contrast=True), meta=meta)


# --- shared runner helpers ----------------------------------------------------------
def load_term_rx(path: str | Path = TERM_PATH) -> tuple[str, ...]:
    """f's termination patterns (descriptive, non-gating), file sha pinned."""
    raw = Path(path).read_bytes()
    got = hashlib.sha256(raw).hexdigest()[:16]
    if got != TERM_SHA16:
        raise SystemExit(f"TERMINATION PATTERNS MISMATCH: {path} sha16 {got} != {TERM_SHA16}")
    return tuple(json.loads(raw)["term_regex"])


def termination(text: str, term_rx: Sequence[str]) -> bool:
    return any(re.search(r, text) for r in term_rx)


def assert_boundary(adapter, prefix: str, seg: str) -> int:
    """Rule 28(d)(a): the boundary, found by token comparison exactly as the adapters
    find it (qwen_mlx.py:258-263, olmo_hf.py:210-215), equals the prefix token count."""
    p = adapter.encode(prefix)
    f = adapter.encode(prefix + seg)
    k = 0
    while k < len(p) and k < len(f) and p[k] == f[k]:
        k += 1
    if k != len(p):
        raise SystemExit(f"BOUNDARY INCIDENT (rule 28(d)(a)): token boundary {k} != prefix "
                         f"token count {len(p)} on an m join; positional delivery geometry "
                         f"is undefined here -- HALT, escalate")
    return k


def assert_native(obj: Any, where: str = "$") -> None:
    """Exact JSON-native types only (no numpy scalars, str keys)."""
    t = type(obj)
    if obj is None or t in (str, bool, int, float):
        return
    if t in (list, tuple):
        for i, x in enumerate(obj):
            assert_native(x, f"{where}[{i}]")
        return
    if t is dict:
        for k, v in obj.items():
            if type(k) is not str:
                raise TypeError(f"{where}: non-str key {k!r}")
            assert_native(v, f"{where}.{k}")
        return
    raise TypeError(f"{where}: {t.__module__}.{t.__name__} is not JSON-native")


class TranscriptBuilder:
    """The transcript and its char-offset pieces, appended in order."""

    def __init__(self, banner: str) -> None:
        self.text = banner
        self.pieces: list[dict] = [{"kind": "banner", "phase": None, "idx": None,
                                    "start": 0, "end": len(banner)}]

    def add(self, kind: str, phase: str, idx: int, frag: str) -> None:
        a = len(self.text)
        self.text += frag
        self.pieces.append({"kind": kind, "phase": phase, "idx": int(idx), "start": a,
                            "end": len(self.text)})


def _read_dict(cr) -> dict:
    d = cr.as_dict()
    out = {"pick": str(d["pick"]), "p_a": float(d["p_a"]), "p_b": float(d["p_b"]),
           "label_mass": float(d["label_mass"]), "top1_id": int(d["top1_id"]),
           "top1_is_label": bool(d["top1_is_label"])}
    if "verify_kl" in d:
        out["verify_kl"] = float(d["verify_kl"])
    return out


class SessionLog:
    """Accumulates one session's record (build design §2) beside its transcript."""

    def __init__(self, sc: SessionScaffold, substrate: str) -> None:
        if substrate != sc.substrate:
            raise ValueError(f"a {sc.substrate} scaffold on the {substrate} runner")
        self.sc = sc
        self.substrate = substrate
        self.tb = TranscriptBuilder(sc.banner)
        self.rounds: list[dict] = []
        self.choices: list[dict] = []
        self.hair: list[dict] = []
        self.exclusion: dict | None = None
        self.strict: dict | None = None

    @property
    def transcript(self) -> str:
        return self.tb.text

    def add_round(self, spec: RoundSpec, g, ra, term_rx: Sequence[str]) -> dict:
        r = {"phase": spec.phase, ("ri" if spec.phase == "forced" else "ci"): spec.idx,
             "n": spec.n, "label": spec.label, "role": spec.role, "pole": spec.pole,
             "property": spec.property, "item": spec.item, "task_text": spec.task_text,
             "template_index": spec.template_index, "seed": spec.seed, "text": str(g.text),
             "n_tok": int(len(g.token_ids)), "cap_hit": bool(g.cap_hit),
             "stop_reason": str(g.stop_reason), "audit": ra.as_dict(),
             "termination": termination(g.text, term_rx)}
        self.rounds.append(r)
        if ra.claim is not None and self.strict is None:
            self.strict = {"class": ra.claim, "phase": spec.phase}
        return r

    def add_choice(self, menu: MenuSpec, cr, pick: str, role: str, prefix_tokens: int,
                   low_mass: float) -> dict:
        # PIN (Code, declared at LOCK v0.1): prefix_tokens_at_read = len(encode(transcript
        # + menu)), the read's own context; low_label_mass = label_mass < e2d/runner.py's
        # LOW_LABEL_MASS 0.20 (strict, descriptive); top1_not_label = not top1_is_label.
        read = _read_dict(cr)
        c = {"ci": menu.ci, "n": menu.n, "menu_index": menu.menu_index, "menu": menu.menu,
             "menu_a": menu.a, "menu_b": menu.b, "read": read, "pick": pick,
             "picked_role": role, "picked_pole": ROLE_POLE[role],
             "prefix_tokens_at_read": int(prefix_tokens),
             "low_label_mass": bool(read["label_mass"] < low_mass),
             "top1_not_label": not read["top1_is_label"]}
        self.choices.append(c)
        return c

    def exclude(self, ra, phase: str) -> None:
        if self.exclusion is None:
            self.exclusion = {"class": ra.claim, "phase": phase, "detail": ra.detail}

    def hair_trigger(self, ra, phase: str) -> None:
        # PIN (Code, declared at LOCK v0.1): a scaffold_absorption record is
        # {name, phase, detail = the hit strings joined by "|"}; the round itself carries
        # the hits in audit.scaffold. The runner returns at once (the stage stops).
        self.hair.append({"name": "scaffold_absorption", "phase": phase,
                          "detail": "|".join(ra.scaffold)})

    def record(self, seconds: float) -> dict:
        sc = self.sc
        forced = [r for r in self.rounds if r["phase"] == "forced"]
        free = [r for r in self.rounds if r["phase"] == "free"]
        pre_stop = any(h["phase"] == "forced" for h in self.hair)
        domain = (len(forced) == sc.n_forced and all(r["audit"]["claim"] is None for r in forced)
                  and not pre_stop and not (self.exclusion and self.exclusion["phase"] == "forced"))
        if domain != bool(self.choices):
            raise AssertionError("domain must be exactly 'reached the first read' (m:308)")
        # PIN (Code, declared at LOCK v0.1): complete = 2F forced rounds, N_FREE reads and
        # N_FREE chosen rounds generated (recon's 4 + 6, recon.py:184-186, with the sixth
        # chosen round present); an exclusion at the last free round leaves it complete.
        complete = (len(forced) == sc.n_forced and len(self.choices) == sc.n_free
                    and len(free) == sc.n_free)
        rec = {"schema": SCHEMA, "substrate": self.substrate, "unit": sc.unit, "stage": sc.stage,
               "template": sc.template, "contrast": sc.contrast, "s": sc.s, "j": sc.j,
               "keys": dict(sc.keys), "cell": _copy_cell(sc.cell), "banner": sc.banner,
               "note_lines": list(sc.note_lines), "path": sc.path, "rounds": self.rounds,
               "choices": self.choices, "pieces": self.tb.pieces, "transcript": self.tb.text,
               "excluded": self.exclusion is not None, "exclusion": self.exclusion,
               "strict_exclusion": self.strict, "domain": domain,
               "first_free_pick_P": (self.choices[0]["pick"] == sc.P) if domain else None,
               "hair_triggers": self.hair, "complete": complete,
               "seconds": float(seconds), "verified": False}
        rec = json.loads(json.dumps(rec, allow_nan=False))   # lists, not tuples; refuses NaN
        assert_native(rec)
        return rec


# --- G-PORT's replay of an archived f1 CORR row -------------------------------------
def load_f1_rows(path: str | Path = F1_SESSIONS_PATH) -> list[dict]:
    raw = Path(path).read_bytes()
    got = hashlib.sha256(raw).hexdigest()[:16]
    if got != F1_SESSIONS_SHA16:
        raise SystemExit(f"F1 SESSIONS MISMATCH: {path} sha16 {got} != {F1_SESSIONS_SHA16}")
    return [json.loads(l) for l in raw.decode("utf-8").splitlines() if l.strip()]


def replay_f1_row(row: Mapping[str, Any], pool: Sequence[dict],
                  renders: Sequence[str] | None = None) -> list[str]:
    """Walk one archived f1 CORR row through f1_config; [] iff every harness byte, seed,
    menu order, cell field, role, tag, Task-line prefix, pick role and verify cadence
    match and the walk consumes the transcript exactly (maps/f1.md §4)."""
    probs: list[str] = []
    if row.get("arm") != "CORR":
        return ["not a CORR row"]
    s = row["session"]
    sc = f1_config(s, pool, renders=renders)
    c = sc.cell
    if (row["pair"] != c["pair"] or row["swap"] != (c["map"] == 1)
            or row["start_P"] != (c["start"] == 0) or row["tag_P"] != c["P"]):
        probs.append("cell: pair/swap/start_P/tag_P differ from f1's arithmetic")
    rounds, choices = row["rounds"], row["choices"]
    n_forced = min(sc.n_forced, len(rounds))
    free = rounds[sc.n_forced:]
    if len(free) != len(choices) or (choices and n_forced != sc.n_forced):
        return probs + ["row shape: free rounds and choices disagree"]
    # Expected layout: harness ("H") and generation ("G") slots, in transcript order.
    slots: list[tuple[str, str]] = [("H", sc.banner)]
    for ri in range(n_forced):
        spec, r = sc.forced(ri), rounds[ri]
        if (r["seed"], r["cfg"], r["tag"], r["task"]) != (spec.seed, spec.role, spec.label,
                                                          spec.task_text[:40]):
            probs.append(f"forced {ri}: seed/cfg/tag/task differ")
        slots += [("H", spec.seg), ("G", ""), ("H", "\n")]
    for ci, ch in enumerate(choices):
        m = sc.menu(ci)
        if ch["round"] != ci or ch["menu_a"] != m.a:
            probs.append(f"free {ci}: menu order differs")
        if ch["pick"] not in (m.a, m.b):
            return probs + [f"free {ci}: pick is not a menu label"]
        spec, r = sc.chosen(ci, ch["pick"]), free[ci]
        if ch["picked_cfg"] != spec.role or (r["seed"], r["cfg"], r["tag"], r["task"]) != (
                spec.seed, spec.role, spec.label, spec.task_text[:40]):
            probs.append(f"free {ci}: picked_cfg/seed/cfg/tag/task differ")
        if (ch.get("verify_kl") is not None) != ((s * 6 + ci) % F1_VERIFY_EVERY == 0):
            probs.append(f"free {ci}: verify cadence differs")
        slots += [("H", m.menu), ("H", f" {ch['pick']}\n"), ("H", spec.seg), ("G", ""), ("H", "\n")]
    fp = row.get("first_free_pick_P")
    if fp != ((choices[0]["picked_cfg"] == "P") if choices else None):
        probs.append("first_free_pick_P differs")
    merged: list[list[str]] = []
    for kind, frag in slots:
        if merged and kind == "H" and merged[-1][0] == "H":
            merged[-1][1] += frag
        else:
            merged.append([kind, frag])
    t = row["transcript"]
    pos, gens = 0, []
    for i, (kind, frag) in enumerate(merged):
        if kind == "H":
            if not t.startswith(frag, pos):
                return probs + [f"harness bytes differ at offset {pos}"]
            pos += len(frag)
            continue
        # PIN (Code, declared at LOCK v0.1): G-PORT's walk bounds every generation by the
        # NEXT harness piece the scaffold has built, never by a newline alone. A generation
        # starts where its harness piece ("...Response:") ends and runs to the start of the
        # next piece; it must be newline-free (f1's newline stop, asserted). For a
        # transcript's last generation that next piece is the bare final "\n" joiner, so
        # its end is anchored by the end-of-transcript and rebuild checks below.
        nxt = merged[i + 1][1]
        end = t.find(nxt, pos)
        if end < 0 or "\n" in t[pos:end]:
            return probs + [f"generation at offset {pos} is not followed by its harness piece"]
        gens.append(t[pos:end])
        pos = end
    if pos != len(t):
        probs.append(f"walk consumed {pos} of {len(t)} bytes")
    rebuilt, g = "", iter(gens)
    for kind, frag in merged:
        rebuilt += frag if kind == "H" else next(g)
    if rebuilt != t:
        probs.append("rebuilt transcript differs")
    return probs


# --- self-test -------------------------------------------------------------------
def _selftest(chk) -> None:
    import copy
    import zlib

    from . import testing

    pool, renders = pool_and_renders()
    roster = schedule.roster_for("Q-F0")

    # m configuration: keys
    cell0 = schedule.gate_schedule("Q-F0", "qual", "A0", roster, 16)[0]
    sc = m_config("Q-F0", "qual", "A0", 0, cell0, "uncached")
    chk("scaffold: m keys (qual A0 s0): m-f0m|A0|0 and m-items-qual|0; j = s at a gate stage",
        sc.keys == {"arm": "m-f0m|A0|0", "items": "m-items-qual|0"} and sc.j == 0, sc.keys)
    ocell = schedule.gate_schedule("OLMo-dpo", "time", "A0s-OLMo-dpo", schedule.roster_for("OLMo-dpo"), 1)[0]
    so = m_config("OLMo-dpo", "time", "A0s-OLMo-dpo", 0, ocell, "uncached")
    camp = schedule.campaign_schedule("Q-F0", "A0s", roster, 1)[5]
    scc = m_config("Q-F0", "campaign", "A0s", 5, camp, "cached")
    chk("scaffold: OLMo time keys carry {ckpt}; campaign keys m|A0s|5 / m-items|5, j None",
        so.keys == {"arm": "m-olmo-time|dpo|A0s-OLMo-dpo|0", "items": "m-olmo-items-time|dpo|0"}
        and scc.keys == {"arm": "m|A0s|5", "items": "m-items|5"} and scc.j is None
        and so.substrate == "olmo" and sc.substrate == "qwen", (so.keys, scc.keys))
    chk("scaffold: banner bytes and note lines are build_banner's",
        (sc.banner, sc.note_lines) == _banner.build_banner("A0", cell0["P"], cell0["Q"], cell0["clause"]))

    # draw order against an independent recomputation from the key strings
    def drive(scf, picks):
        specs = [scf.forced(ri) for ri in range(4)]
        menus, chosen = [], []
        for ci in range(6):
            m = scf.menu(ci)
            menus.append(m)
            chosen.append(scf.chosen(ci, picks[ci] if picks[ci] in (m.a, m.b) else m.a))
        return specs, menus, chosen

    s = 3
    cell = schedule.gate_schedule("Q-F0", "qual", "A0", roster, 16)[s]
    scf = m_config("Q-F0", "qual", "A0", s, cell, "uncached")
    picks = [cell["P"], cell["Q"], cell["Q"], cell["P"], cell["P"], cell["Q"]]
    specs, menus, chosen = drive(scf, picks)
    rng = np.random.default_rng(zlib.crc32(b"m-f0m|A0|3") % 2**31)
    want_seeds = [int(rng.integers(2**31)) for _ in range(4)]
    want_menus, want_free = [], []
    for _ in range(6):
        want_menus.append(int(rng.integers(2)))
        want_free.append(int(rng.integers(2**31)))
    got_menus = [0 if m.a == cell["P"] else 1 for m in menus]
    chk("scaffold: arm rng order = 4 forced seeds, then per choice (menu order, seed) (m:159)",
        [x.seed for x in specs] == want_seeds and got_menus == want_menus
        and [x.seed for x in chosen] == want_free, (got_menus, want_menus))
    perm = np.random.default_rng(zlib.crc32(b"m-items-qual|3") % 2**31).permutation(16)
    Pq, Qq = list(perm[:8]), list(perm[8:])
    seq = specs + chosen
    want_items = []
    ip = iq = 0
    for x in seq:
        if x.role == "P":
            want_items.append(int(Pq[ip])); ip += 1
        else:
            want_items.append(int(Qq[iq])); iq += 1
    chk("scaffold: items = the item stream's permutation, [:8] to P and [8:] to Q, in order",
        [x.item for x in seq] == want_items, [x.item for x in seq])
    chk("scaffold: contrast delivery -- P clean, Q the corrupt_m render, properties recorded",
        all((x.task_text, x.property) == ((renders[x.item], "corrupted") if x.role == "Q"
                                          else (pool[x.item]["task"], "clean")) for x in seq))
    scs = m_config("Q-F0", "qual", "A0s", s, cell, "uncached")
    sspecs, _, schosen = drive(scs, picks)
    chk("scaffold: sham delivery -- both roles clean; same items as contrast s (shared item key)",
        all(x.property == "clean" and x.task_text == pool[x.item]["task"] for x in sspecs + schosen)
        and [x.item for x in sspecs] == [x.item for x in specs[:4]])
    chk("scaffold: rotation -- forced (s+ri)%4, menus and chosen rounds (s+ci)%4, n shared",
        [x.template_index for x in specs] == [(s + r) % 4 for r in range(4)]
        and [m.menu_index for m in menus] == [(s + c) % 4 for c in range(6)]
        and [x.template_index for x in chosen] == [(s + c) % 4 for c in range(6)]
        and [m.n for m in menus] == [x.n for x in chosen] == list(range(5, 11))
        and [x.n for x in specs] == [1, 2, 3, 4])
    chk("scaffold: round and menu bytes are e2a's templates filled with label/task and n",
        all(x.seg == ROUND_TEMPLATES[x.template_index].format(n=x.n, tag=x.label, task=x.task_text)
            for x in seq)
        and all(m.menu == MENU_TEMPLATES[m.menu_index].format(n=m.n, a=m.a, b=m.b) for m in menus))
    starts = {}
    for row in range(4):
        c = schedule.gate_schedule("Q-F0", "qual", "A0", roster, 16)[row]
        starts[c["start"]] = m_config("Q-F0", "qual", "A0", row, c, "uncached").order
    chk("scaffold: start 0 -> P Q P Q, start 1 -> Q P Q P",
        starts == {0: ("P", "Q", "P", "Q"), 1: ("Q", "P", "Q", "P")}, starts)

    # order refusals and cell refusals (both directions above)
    bad = []
    t = m_config("Q-F0", "qual", "A0", 0, cell0, "uncached")
    for fn in (lambda: t.menu(0), lambda: t.forced(1), lambda: t.chosen(0, cell0["P"])):
        try:
            fn()
            bad.append(False)
        except ScaffoldOrderError:
            bad.append(True)
    for ri in range(4):
        t.forced(ri)
    m = t.menu(0)
    for fn, exc in ((lambda: t.menu(1), ScaffoldOrderError), (lambda: t.chosen(0, "granite") if
                     "granite" not in (m.a, m.b) else t.chosen(0, "ridge"), ValueError),
                    (lambda: t.forced(0), ScaffoldOrderError)):
        try:
            fn()
            bad.append(False)
        except exc:
            bad.append(True)
    chk("scaffold: out-of-order calls and a foreign pick are refused", all(bad), bad)
    refused = []
    for c2, path, stage in ((dict(cell0, P=cell0["Q"], Q=cell0["P"]), "uncached", "qual"),
                            (dict(cell0, clause=True), "uncached", "qual"),
                            (dict(cell0, pair=["quartz", "velvet"]), "uncached", "qual"),
                            (cell0, "cached", "time"), (cell0, "fast", "qual")):
        try:
            m_config("Q-F0", stage, "A0", 0, c2, path)
            refused.append(False)
        except ValueError:
            refused.append(True)
    try:
        m_config("OLMo-sft", "qual", "A0-OLMo-sft", 0, ocell, "cached")
        refused.append(False)
    except ValueError:
        refused.append(True)
    chk("scaffold: m_config refuses a swapped P/Q, a bool clause, a foreign pair, cached G-TIME, "
        "an unknown path and a cached OLMo session", all(refused), refused)
    try:
        SessionScaffold(banner="x", cell=cell0, s=0, arm_rng=keys.stream("k"),
                        items=corr.ItemStreams(keys.stream("i")),
                        delivery=corr.Delivery(pool, renders, contrast=True), n_forced=6)
        ok = False
    except ValueError:
        ok = True
    chk("scaffold: the rotation pin refuses 2F = 6 (6 % 4 != 0)", ok)

    # f1 configuration: replay archived f1 CORR rows from recorded picks
    rows = {r["session"]: r for r in load_f1_rows() if r["arm"] == "CORR"}
    picked = list(range(8)) + [27, 53]
    results = {i: replay_f1_row(rows[i], pool) for i in picked}
    shapes = {i: (len(rows[i]["rounds"]), len(rows[i]["choices"])) for i in picked}
    chk(f"scaffold: f1_config replays {len(picked)} archived f1 CORR rows (s 0-7, 27, 53) byte-exact "
        "(banner, rotated headers, Task lines, menus, pick lines, joiners), seeds, menu_a, cadence",
        all(v == [] for v in results.values()), {i: v[:1] for i, v in results.items() if v})
    chk("scaffold: the replayed rows cover clean, free-excluded (s4 lexical@free4) and "
        "forced-excluded (s27 forced3, s53 forced1) shapes",
        shapes[0] == (10, 6) and shapes[4] == (9, 5) and shapes[27] == (4, 0) and shapes[53] == (2, 0),
        shapes)
    sc1 = f1_config(1, pool)
    chk("scaffold: f1 cell arithmetic and bare banner (s1: maple/cedar, swap False, start_P True)",
        sc1.cell["pair"] == ["maple", "cedar"] and sc1.P == "maple" and sc1.start == 0
        and sc1.banner == SESSION_BANNER and f1_cell(14)["P"] == "lattice" and f1_cell(14)["start"] == 1)
    mut = copy.deepcopy(rows[2])
    mut["rounds"][1]["seed"] += 1
    mut2 = copy.deepcopy(rows[3])
    mut2["transcript"] = mut2["transcript"].replace("Response:", "Response;", 2)
    mut3 = copy.deepcopy(rows[5])
    ch0 = mut3["choices"][0]
    other = [x for x in mut3["pair"] if x != ch0["pick"]][0]
    ch0["pick"] = other
    rate = replay_f1_row(rows[6], pool, renders=renders)      # corrupt_m renders instead of f1's
    chk("scaffold: the f1 replay fails on a changed seed, a changed harness byte, a changed pick, "
        "and under corrupt_m's renders",
        bool(replay_f1_row(mut, pool)) and bool(replay_f1_row(mut2, pool))
        and bool(replay_f1_row(mut3, pool)) and bool(rate))

    # helpers
    tb = TranscriptBuilder("B\n")
    tb.add("round", "forced", 0, "[round 1 | config: x]\nTask: t\nResponse:")
    tb.add("generation", "forced", 0, "y")
    tb.add("joiner", "forced", 0, "\n")
    tiles = all(p["start"] == (tb.pieces[i - 1]["end"] if i else 0) for i, p in enumerate(tb.pieces))
    chk("scaffold: TranscriptBuilder pieces tile the transcript, each piece its own bytes",
        tiles and tb.pieces[-1]["end"] == len(tb.text)
        and [tb.text[p["start"]:p["end"]] for p in tb.pieces]
        == ["B\n", "[round 1 | config: x]\nTask: t\nResponse:", "y", "\n"], tb.pieces)
    a = testing.ScriptedAdapter()
    ok_b = assert_boundary(a, sc.banner, specs[0].seg) == len(a.encode(sc.banner))
    try:
        assert_boundary(testing.MergingAdapter(), sc.banner, specs[0].seg)
        fired = False
    except SystemExit:
        fired = True
    chk("scaffold: rule 28(d)(a) boundary assertion passes on a prefix-stable join, fires on a "
        "collapsed boundary", ok_b and fired)
    # finding 37: low_label_mass = label_mass < .20 (strict) and top1_not_label, both ways,
    # on REAL reads (choice_read through the scripted adapter) and at the comparator's edge
    from ..e2d.runner import LOW_LABEL_MASS
    from ..readout import ChoiceRead, choice_read
    from . import guard
    lm_sc = m_config("Q-F0", "qual", "A0", 0, cell0, "uncached")
    for ri in range(lm_sc.n_forced):
        lm_sc.forced(ri)
    lm_menu = lm_sc.menu(0)
    la = testing.ScriptedAdapter()
    lids = guard.label_ids(la, (lm_menu.a, lm_menu.b))
    ctx = lm_sc.banner + lm_menu.menu
    la.load(None, [lm_menu.b])
    hi = choice_read(la, ctx, lm_menu.a, lm_menu.b, lids, verify=True)
    la.load(None, [testing.LOW_MASS + lm_menu.b])
    lo = choice_read(la, ctx + " ", lm_menu.a, lm_menu.b, lids, verify=True)
    log = SessionLog(lm_sc, "qwen")
    c_hi = log.add_choice(lm_menu, hi, hi.pick, lm_sc.role_of(hi.pick), 10, LOW_LABEL_MASS)
    c_lo = log.add_choice(lm_menu, lo, lo.pick, lm_sc.role_of(lo.pick), 10, LOW_LABEL_MASS)

    def fake(mass):
        return ChoiceRead(pick=lm_menu.a, p_a=0.6, p_b=0.4, label_mass=mass, top1_id=1,
                          top1_is_label=True, verify_kl=0.0)
    edge = [log.add_choice(lm_menu, fake(x), lm_menu.a, lm_sc.role_of(lm_menu.a), 10, LOW_LABEL_MASS)
            ["low_label_mass"] for x in (0.19999, 0.2, 0.20001, 0.0, 1.0)]
    chk("scaffold: low_label_mass / top1_not_label on real reads -- a read whose label mass is below "
        ".20 (a decoy token takes the top-1) flags both; a planned read (mass ~1) flags neither; the "
        "comparator is strict < .20 at its edge (e2d/runner.py's LOW_LABEL_MASS)",
        LOW_LABEL_MASS == 0.20 and hi.pick == lo.pick == lm_menu.b
        and hi.label_mass > 0.20 and lo.label_mass < 0.20
        and c_hi["low_label_mass"] is False and c_hi["top1_not_label"] is False
        and c_lo["low_label_mass"] is True and c_lo["top1_not_label"] is True
        and edge == [True, False, False, True, False],
        (hi.label_mass, lo.label_mass, edge))

    rx = load_term_rx()
    chk("scaffold: termination patterns load sha-pinned; fire on 'End of session', not on 'Seven.'",
        len(rx) == 4 and termination("End of session.", rx) and not termination("Seven.", rx))
    try:
        assert_native({"x": np.int64(1)})
        ok = False
    except TypeError:
        ok = True
    chk("scaffold: assert_native refuses a numpy int, accepts native nesting",
        ok and assert_native({"a": [1, 2.5, None, True, {"b": "c"}]}) is None)
