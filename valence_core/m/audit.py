"""PROPOSAL-m audit wrapper -- the task-round claim classes (v1.11 §2.6, m:261-266;
with m:271, m:308, m:314, m:318).

One wrapper per substrate, on top of the frozen monitors, which are imported and
never edited:

  Qwen  claim order v2 -> echo -> v4 content -> own-pair lexical (m:261, rule 28(b)).
        v2 is `session.AuditSpec` as `e2d.config.load_audit()` builds it from
        `data/configs/e2b_audit_v2.json` (sha16 pinned to the constant below, not
        only to the file's own declared field -- maps/audit.md §4 item 2) and the
        e2a ban list (file sha256 pinned). Audit v3 (`e2d.audit_v3.AuditV3`, v4 rev 3
        exclusion-bearing + v5 advisory) runs on EVERY task round with `task_text`
        = the render as delivered and v5's "others" = the other 15 CORR items
        (m:261). AuditV3 evaluates v2 and content in one call; m's order puts echo
        between them, so the claim is DERIVED from the result (v3 untouched).
  OLMo  claim order b3 AuditSpec -> echo -> own-pair lexical (m:262). The AuditSpec
        is b3's (box_b3_sessions.py:85-91), replicated here as `OLMO_AUDIT` and
        asserted equal to b3's object by the self-test only.

m's harness-echo class (m:261, m:262): a verbatim, whitespace-normalised
reproduction of a complete "Note:" line of the session's banner (Qwen also the
literal `Reasoning (one line):`) -- and, on OLMo only, a line ending in . ! or ?
reproduced without its terminal mark at the END of the response (OLMo's newline stop
drops the fused ".\\n" token; `harness_echo`'s PIN; Qwen keeps m:261's complete-line
form). `round_degeneracy`'s numerator is the v2/AuditSpec
or echo claim (`RoundAudit.degeneracy`); `audit_degenerate` counts v2/AuditSpec
claims (m:261, m:262, m:314).

Session-end rules (m:261, m:262, m:271, m:308): Qwen lenient scope -- a forced
round ends the session on any claim, a free round only on a lexical claim (a free
v2/echo/content claim is `post_choice_degeneracy`, f1's `post_degen`,
f_sessions.py:368-372); strict scope reported beside. OLMo ends the session at its
first claim in any round.

`scaffold_absorption` (m:261, m:262): case-sensitive substring hits of the
substrate's ban strings in model text, recorded on every round independently of
the claim (a hair trigger, stage-level, owned by the runner and the stage driver).

Nothing here prints. Counter keys never carry a tag, an item, a free-round index
or a property (m:263, m:318; maps/audit.md D13): printing goes only through
`readrule.printed_reason` / `readrule.session_line` (DESIGN §0 rule 5).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping, Sequence

from valence_core.e2d import config as C
from valence_core.e2d import contentclass_v5 as V5
from valence_core.e2d.audit_v3 import AuditV3
from valence_core.session import AuditSpec, DescriptiveCounters, lexical_hit

# --- pins ---------------------------------------------------------------------
AUDIT_V2_SHA16 = "7aa235d25eeb66dc"          # e2b_audit_v2.json body hash (format_recon:136-140 rule)
E2A_BAN_LIST_SHA256 = "9a2f0744f81ac930fdf8533c7d07b77bd15a5361e89b060363d022c3661d31c4"
OLMO_SCAFFOLD_STRINGS = ("</think>", "<think>", "<|endoftext|>", "<|im_end|>",
                         "<|im_start|>", "<|pad|>")  # data/olmo/scaffold_{ckpt}.json["ban_strings"]
OLMO_BAN_IDS_SHA16 = "2dd86a453a2275ef"      # sha256(json.dumps(sorted(ids)))[:16], box_b3_sessions.py:262
OLMO_BAN_N_IDS = 9                           # b3_screen_{ckpt}.json["ban_list"]["n_ids"]
REASONING_LABEL = "Reasoning (one line):"    # m:261 literal
OLMO_CKPTS = ("sft", "dpo", "instruct")      # keys.CKPTS; base refused (decision (7'))

E2A_BAN_LIST_PATH = os.path.join(C.DATA, "configs", "e2a_ban_list.json")

#: b3's audit of record for OLMo Q3, box_b3_sessions.py:85-91, verbatim.
# PIN (Code, declared at LOCK v0.1): OLMO_AUDIT is a replicated literal (maps/audit.md
# D12), asserted == box_b3_sessions.AUDIT in the self-test, never imported at runtime
# (b3's module imports `adapters.base.Injection`, which m never imports).
OLMO_AUDIT = AuditSpec(
    ban_strings=("<think>", "</think>", "<|im_start|>", "<|im_end|>"),
    frame_fragments=("Config evaluation session", "evaluation session",
                     "[round", "Config choice", "Available configs",
                     "Configs available", "Configs on offer", "Task:",
                     "Response:"),
    junk_regex=(r"(\b\w+\b)(\s+\1){3,}", r"(.{6,}?)\1{3,}"))

SUBSTRATES = ("qwen", "olmo")
PHASES = ("forced", "free")
QWEN_CLAIMS = ("v2", "echo", "content", "lexical")
OLMO_CLAIMS = ("audit", "echo", "lexical")
_DEGENERACY = {"qwen": ("v2", "echo"), "olmo": ("audit", "echo")}

#: Rule 23 counters, maps/audit.md §7 exactly (m:314 minus Q-F3's reasoning-line
#: defects, which are not built before step 19).
# PIN (Code, declared at LOCK v0.1): Q-F3's "reasoning-line defects by class" counter
# is not declared at step 4; it is added with Q-F3's runner (step 19).
DECLARED_COUNTERS_QWEN = ("cap_hit", "audit_degenerate", "harness_echo", "content_exclusion",
                          "content_advisory", "lexical", "post_choice_degeneracy",
                          "low_label_mass", "top1_not_label", "termination", "pre_pick_exclusion")
DECLARED_COUNTERS_OLMO = ("cap_hit", "audit_degenerate", "harness_echo", "lexical",
                          "low_label_mass", "top1_not_label", "termination", "pre_pick_exclusion")


# --- echo ----------------------------------------------------------------------
def ws_norm(s: str | None) -> str:
    """Whitespace runs to one space, ends trimmed; nothing else removed. Identical
    to `contentclass_v5._ws` (the self-test asserts it)."""
    return re.sub(r"\s+", " ", s or "").strip()


def _check_lines(lines: Sequence[str]) -> None:
    for ln in lines:
        if not isinstance(ln, str) or "\n" in ln or not ws_norm(ln):
            raise ValueError(f"echo line must be a non-empty single line without '\\n': {ln!r}")


_TERMINAL_PUNCT = ".!?"


def harness_echo(text: str, lines: Sequence[str], *, substrate: str | None = None) -> int | None:
    """Index (in `lines` order) of the first complete harness line reproduced in
    `text`, else None (m:261, m:262). `substrate="olmo"` also admits the line
    without its terminal mark at the END of the response (the PIN below); None
    or "qwen" is the complete-line rule alone."""
    # PIN (Code, declared at LOCK v0.1): echo = containment of the ws-normalised
    # COMPLETE line in the ws-normalised response, case-sensitive (verbatim), lines
    # passed without their "\n" (maps/audit.md D1); first match by line order.
    # PIN (Code, declared at LOCK v0.1; maps/olmo.md §7 item 7 left "whether complete
    # requires the trailing period" open for OLMo): ON OLMO ONLY, a line ending in
    # . ! or ? also echoes when the ws-normalised response ENDS WITH the line minus
    # that terminal mark. OLMo's newline stop drops the stop token and its tokenizer
    # fuses sentence-final punctuation with the newline (".\n" is one token), so a
    # copied Note line is stored without its period (finding 5). The mark-less form
    # counts only at the END of the response -- mid-response it is not an echo -- and
    # the complete form anywhere. QWEN KEEPS m:261's "complete 'Note:' line" (maps/
    # audit.md D1; finding N6): Qwen's vocabulary has no punctuation+newline token, so
    # its stop never takes a final period and a period-less Note copy is the model's
    # own incomplete text, not an echo; it falls to the later classes in m:261's
    # claiming order (a TOLD copy names the own pair: lexical; a COMMON copy: no class
    # unless v4 content claims it).
    if substrate not in (None,) + SUBSTRATES:
        raise ValueError(f"substrate {substrate!r}")
    _check_lines(lines)
    t = ws_norm(text)
    for i, ln in enumerate(lines):
        n = ws_norm(ln)
        if n in t:
            return i
        if substrate == "olmo" and n[-1] in _TERMINAL_PUNCT:
            stem = n[:-1].rstrip()
            if stem and t.endswith(stem):
                return i
    return None


def _check_note_lines(note_lines: Sequence[str]) -> tuple[str, ...]:
    nl = tuple(note_lines)
    _check_lines(nl)
    if not nl or not all(ln.startswith("Note:") for ln in nl):
        raise ValueError(f"banner Note lines must each start 'Note:': {nl!r}")
    return nl


def qwen_echo_lines(note_lines: Sequence[str]) -> tuple[str, ...]:
    """Qwen task-round echo set: the session's banner Note lines + `Reasoning (one line):`."""
    # PIN (Code, declared at LOCK v0.1): m:261's literal reasoning label is in the Qwen
    # task-round echo set on F0m too, though F0m writes no reasoning block (maps/audit.md
    # D2); classify() refuses a Qwen set without it and an OLMo set with it.
    return _check_note_lines(note_lines) + (REASONING_LABEL,)


def olmo_echo_lines(note_lines: Sequence[str]) -> tuple[str, ...]:
    """OLMo echo set: the session's banner Note lines only (m:262)."""
    return _check_note_lines(note_lines)


def _check_echo_set(substrate: str, echo_lines: Sequence[str]) -> tuple[str, ...]:
    el = tuple(echo_lines)
    if substrate == "qwen":
        if not el or el[-1] != REASONING_LABEL:
            raise ValueError("Qwen echo lines must end with the reasoning label (m:261)")
        _check_note_lines(el[:-1])
    else:
        if REASONING_LABEL in el:
            raise ValueError("OLMo echo lines are the banner Note lines only (m:262)")
        _check_note_lines(el)
    return el


# --- audits of record ------------------------------------------------------------
def _sha16_body(cfg: Mapping[str, Any]) -> str:
    body = {k: v for k, v in cfg.items() if k != "sha16"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]


def _check_audit_cfg(cfg: Mapping[str, Any], ban_bytes: bytes, spec: AuditSpec) -> dict:
    now = _sha16_body(cfg)
    if now != AUDIT_V2_SHA16 or cfg.get("sha16") != AUDIT_V2_SHA16:
        raise SystemExit(f"AUDIT ARTIFACT MISMATCH: e2b_audit_v2.json recomputes {now}, declares "
                         f"{cfg.get('sha16')}, pinned {AUDIT_V2_SHA16}. Stop, escalate.")
    got = hashlib.sha256(ban_bytes).hexdigest()
    if got != E2A_BAN_LIST_SHA256:
        raise SystemExit(f"BAN LIST MISMATCH: e2a_ban_list.json sha256 {got}, pinned "
                         f"{E2A_BAN_LIST_SHA256}. Stop, escalate.")
    if tuple(json.loads(ban_bytes)["strings"]) != tuple(spec.ban_strings):
        raise SystemExit("BAN LIST MISMATCH: v2 ban_strings differ from the pinned ban-list file")
    out = dict(cfg)
    out["sha16_recomputed"] = now
    out["ban_list_sha256"] = got
    return out


def qwen_audit_of_record() -> tuple[AuditV3, dict]:
    """Audit v3 over v2 as `e2d.config.load_audit()` builds it; v2's body sha16 and the
    e2a ban-list file's sha256 compared to pinned constants (m:261; D11)."""
    spec, cfg = C.load_audit()
    with open(E2A_BAN_LIST_PATH, "rb") as f:
        ban_bytes = f.read()
    return AuditV3(v2=spec), _check_audit_cfg(cfg, ban_bytes, spec)


def _sorted_unique(xs: Iterable[Any], what: str) -> list:
    xs = list(xs)
    if len(set(xs)) != len(xs):
        raise SystemExit(f"SCAFFOLD SET: duplicate {what}: {xs}")
    return sorted(xs)


def assert_qwen_scaffold(ban_ids: Sequence[int], ban_strings: Sequence[str],
                         audit3: AuditV3 | None = None) -> dict:
    """The generation ban list equals the e2a ban-list file (strings and ids) and its
    strings equal audit v3's v2 ban strings -- the `scaffold_absorption` set (m:261;
    maps/audit.md §4 item 9)."""
    # PIN (Code, declared at LOCK v0.1): comparisons are order-insensitive (sorted, with
    # duplicates refused); build_ban_list returns sorted lists, the file is sorted. The
    # Qwen set is pinned by the ban-list FILE's sha256 (maps/audit.md D11).
    if audit3 is None:
        audit3 = qwen_audit_of_record()[0]
    with open(E2A_BAN_LIST_PATH, "rb") as f:
        ban_bytes = f.read()
    if hashlib.sha256(ban_bytes).hexdigest() != E2A_BAN_LIST_SHA256:
        raise SystemExit("BAN LIST MISMATCH: e2a_ban_list.json sha256 moved. Stop, escalate.")
    fil = json.loads(ban_bytes)
    s = _sorted_unique(ban_strings, "ban strings")
    ids = _sorted_unique((int(i) for i in ban_ids), "ban ids")
    if s != sorted(fil["strings"]):
        raise SystemExit(f"SCAFFOLD SET MISMATCH (Qwen strings): {s} vs file {sorted(fil['strings'])}")
    if ids != sorted(int(i) for i in fil["ids"]):
        raise SystemExit(f"SCAFFOLD SET MISMATCH (Qwen ids): {ids} vs file {sorted(fil['ids'])}")
    if s != _sorted_unique(audit3.v2.ban_strings, "v2 ban strings"):
        raise SystemExit("SCAFFOLD SET MISMATCH: generation ban strings != audit v3's v2 ban strings")
    return {"n_ids": len(ids), "n_strings": len(s), "ban_list_sha256": E2A_BAN_LIST_SHA256}


def _olmo_ids_sha16(ban_ids: Sequence[int]) -> str:
    return hashlib.sha256(json.dumps(sorted(int(i) for i in ban_ids)).encode()).hexdigest()[:16]


def _check_olmo_scaffold(ban_ids: Sequence[int], ban_strings: Sequence[str], ckpt: str,
                         pinned_sha16: str) -> dict:
    # PIN (Code, declared at LOCK v0.1): base is refused (keys.CKPTS); the pinned sha16
    # must also equal that checkpoint's b3_screen record (n_ids 9).
    if ckpt not in OLMO_CKPTS:
        raise SystemExit(f"OLMo checkpoint {ckpt!r} is not an m unit (base refused)")
    with open(os.path.join(C.DATA, "olmo", f"scaffold_{ckpt}.json")) as f:
        file_strings = sorted(json.load(f)["ban_strings"])
    with open(os.path.join(C.DATA, "olmo", f"b3_screen_{ckpt}.json")) as f:
        b3_ban = json.load(f)["ban_list"]
    s = _sorted_unique(ban_strings, "ban strings")
    if s != file_strings or s != sorted(OLMO_SCAFFOLD_STRINGS):
        raise SystemExit(f"SCAFFOLD SET MISMATCH (OLMo {ckpt} strings): {s} vs {file_strings}")
    ids = _sorted_unique((int(i) for i in ban_ids), "ban ids")
    if len(ids) != OLMO_BAN_N_IDS or int(b3_ban["n_ids"]) != OLMO_BAN_N_IDS:
        raise SystemExit(f"SCAFFOLD SET MISMATCH (OLMo {ckpt}): {len(ids)} ids, b3 {b3_ban['n_ids']}, "
                         f"declared {OLMO_BAN_N_IDS}")
    got = _olmo_ids_sha16(ids)
    if got != pinned_sha16 or b3_ban["sha16"] != OLMO_BAN_IDS_SHA16:
        raise SystemExit(f"SCAFFOLD SET MISMATCH (OLMo {ckpt} ids): sha16 {got}, pinned {pinned_sha16}, "
                         f"b3 record {b3_ban['sha16']}")
    return {"ckpt": ckpt, "n_ids": len(ids), "ids_sha16": got, "n_strings": len(s)}


def assert_olmo_scaffold(ban_ids: Sequence[int], ban_strings: Sequence[str], ckpt: str) -> dict:
    """OLMo `scaffold_absorption` set: strings == data/olmo/scaffold_{ckpt}.json's
    (sorted), ids' sha16 == b3's `2dd86a453a2275ef`, 9 ids (m:262)."""
    return _check_olmo_scaffold(ban_ids, ban_strings, ckpt, OLMO_BAN_IDS_SHA16)


# --- the CORR id pool ---------------------------------------------------------------
def _clean_texts(pool: Sequence[Mapping[str, Any]]) -> list[str]:
    texts = [p["task"] for p in pool]
    if len(texts) != 16 or len(set(texts)) != 16 or not all(isinstance(t, str) for t in texts):
        raise ValueError(f"CORR pool must be 16 distinct clean tasks, got {len(texts)}")
    return texts


def corr_others(item: int, pool: Sequence[Mapping[str, Any]]) -> list[str]:
    """v5's id pool for CORR item `item`: the other 15 items, task id = the CORR
    module's index (m:261). Built through `contentclass_v5.others_by_task_id` with an
    explicit id so a corrupted render (in no text index) cannot silently keep the
    whole pool (maps/audit.md §4 item 3)."""
    # PIN (Code, declared at LOCK v0.1): "the other 15 items" = their CLEAN text only
    # (maps/audit.md D4); only v5's advisory `wrong_task` reads it.
    texts = _clean_texts(pool)
    if isinstance(item, bool) or not isinstance(item, int) or not 0 <= item < len(texts):
        raise ValueError(f"CORR item index out of range: {item!r}")
    pool_by_id = {str(j): [t] for j, t in enumerate(texts)}
    out = V5.others_by_task_id("__corr_item__", pool_by_id, {"__corr_item__": str(item)})
    if len(out) != 15 or texts[item] in out:
        raise ValueError(f"corr_others({item}): own item present or size {len(out)} != 15")
    return out


# --- the per-round record ---------------------------------------------------------
@dataclass(frozen=True)
class RoundAudit:
    """One task round's audit. `claim` is the single class that claims the round
    (m:261 "counts once, claimed by the first"); `echo_line` / `lexical_raw` are the
    raw hits beside it (maps/audit.md D10), checkpoint only."""

    # PIN (Code, declared at LOCK v0.1): `detail` forms -- "audit:<AuditSpec reason>"
    # (both substrates' v2/AuditSpec), "echo:<line index>", "content:<v4 class>",
    # "lexical:<tag>"; detail carries a tag and is never printed or counted.
    substrate: str
    phase: str
    claim: str | None
    detail: str | None = None
    v3: dict | None = None
    advisory: tuple[str, ...] = ()
    echo_line: int | None = None
    lexical_raw: str | None = None
    scaffold: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.substrate not in SUBSTRATES:
            raise ValueError(f"substrate {self.substrate!r}")
        if self.phase not in PHASES:
            raise ValueError(f"phase {self.phase!r}")
        allowed = QWEN_CLAIMS if self.substrate == "qwen" else OLMO_CLAIMS
        if self.claim is not None and self.claim not in allowed:
            raise ValueError(f"claim {self.claim!r} is not a {self.substrate} class {allowed}")
        if (self.claim is None) != (self.detail is None):
            raise ValueError("claim and detail are both set or both None")
        if self.substrate == "olmo" and (self.v3 is not None or self.advisory):
            raise ValueError("OLMo rounds carry no audit-v3 result")
        object.__setattr__(self, "advisory", tuple(self.advisory))
        object.__setattr__(self, "scaffold", tuple(self.scaffold))

    @property
    def degeneracy(self) -> bool:
        """`round_degeneracy`'s numerator: claimed by v2/AuditSpec or echo (m:261, m:262)."""
        return self.claim in _DEGENERACY[self.substrate]

    def excludes(self, scope: str = "run") -> bool:
        """`run` = the substrate's scope of record (Qwen lenient, OLMo strict); `strict`
        = any claim; `lenient` = Qwen's lenient rule."""
        # PIN (Code, declared at LOCK v0.1): OLMo has no lenient scope (b3's rule is
        # strict, m:262), so excludes("lenient") on an OLMo round raises.
        if scope == "strict":
            return self.claim is not None
        if scope == "lenient" and self.substrate != "qwen":
            raise ValueError("OLMo has no lenient scope (m:262)")
        if scope not in ("run", "lenient"):
            raise ValueError(f"scope {scope!r}")
        if self.substrate == "olmo":
            return self.claim is not None
        return self.claim is not None if self.phase == "forced" else self.claim == "lexical"

    def as_dict(self) -> dict:
        return {"substrate": self.substrate, "phase": self.phase, "claim": self.claim,
                "detail": self.detail, "v3": None if self.v3 is None else dict(self.v3),
                "advisory": list(self.advisory), "echo_line": self.echo_line,
                "lexical_raw": self.lexical_raw, "scaffold": list(self.scaffold),
                "degeneracy": self.degeneracy}

    @classmethod
    def from_dict(cls, d: Mapping[str, Any]) -> "RoundAudit":
        ra = cls(substrate=d["substrate"], phase=d["phase"], claim=d["claim"], detail=d["detail"],
                 v3=d["v3"], advisory=tuple(d["advisory"]), echo_line=d["echo_line"],
                 lexical_raw=d["lexical_raw"], scaffold=tuple(d["scaffold"]))
        if "degeneracy" in d and bool(d["degeneracy"]) != ra.degeneracy:
            raise ValueError("record's degeneracy flag disagrees with its claim")
        return ra


def _ra(x: Any) -> RoundAudit:
    """A RoundAudit, its as_dict(), or a session record round carrying "audit"."""
    if isinstance(x, RoundAudit):
        return x
    if isinstance(x, Mapping) and "audit" in x:
        return _ra(x["audit"])
    if isinstance(x, Mapping):
        return RoundAudit.from_dict(x)
    raise TypeError(f"not a round audit: {type(x).__name__}")


def _own_pair(own_pair: Sequence[str]) -> tuple[str, str]:
    op = tuple(own_pair)
    if len(op) != 2 or op[0] == op[1] or not all(isinstance(t, str) and t for t in op):
        raise ValueError(f"own pair must be the session's two labels: {op!r}")
    return op  # type: ignore[return-value]


def _scaffold_hits(text: str, strings: Sequence[str]) -> tuple[str, ...]:
    # PIN (Code, declared at LOCK v0.1): hits are case-sensitive substrings, listed in the
    # scaffold set's order, recorded on every round whatever the claim.
    return tuple(s for s in strings if s in text)


# --- the two classifiers ---------------------------------------------------------
class QwenTaskRoundAudit:
    """Qwen: v2 -> echo -> v4 content -> own-pair lexical (m:261)."""

    def __init__(self, audit3: AuditV3, pool: Sequence[Mapping[str, Any]],
                 scaffold_strings: Sequence[str] | None = None) -> None:
        if not isinstance(audit3, AuditV3):
            raise TypeError("audit3 must be e2d.audit_v3.AuditV3")
        self.audit3 = audit3
        self._clean = _clean_texts(pool)
        self._others = [corr_others(i, pool) for i in range(len(self._clean))]
        ss = tuple(audit3.v2.ban_strings if scaffold_strings is None else scaffold_strings)
        # m:261: the Qwen scaffold set IS the e2a ban list as e2d.config loads it.
        if sorted(ss) != sorted(audit3.v2.ban_strings) or len(set(ss)) != len(ss):
            raise ValueError("Qwen scaffold strings must equal audit v3's v2 ban strings (m:261)")
        self.scaffold_strings = ss

    def classify(self, text: str, *, render: str, item: int, earlier: Sequence[str],
                 own_pair: Sequence[str], echo_lines: Sequence[str], phase: str) -> RoundAudit:
        """`render` = the task text as delivered (clean, or the corrupted render);
        `earlier` = every prior task-round response of the session, whatever its class
        (maps/audit.md D9). Audit v3 runs on every task round (m:261)."""
        # PIN (Code, declared at LOCK v0.1): v4 content claims only its exclusion-bearing
        # classes; v5 advisories never claim and are recorded on every round (D5).
        # PIN (Code, declared at LOCK v0.1): a render equal to a clean CORR text must be
        # the clean text of `item` (an item/render mismatch is refused).
        if phase not in PHASES:
            raise ValueError(f"phase {phase!r}")
        op = _own_pair(own_pair)
        el = _check_echo_set("qwen", echo_lines)
        if isinstance(item, bool) or not isinstance(item, int) or not 0 <= item < len(self._clean):
            raise ValueError(f"CORR item index out of range: {item!r}")
        if not isinstance(render, str) or not render:
            raise ValueError("render must be the task text as delivered")
        if render in self._clean and render != self._clean[item]:
            raise ValueError(f"render is CORR item {self._clean.index(render)}'s clean text, not item {item}'s")
        r3 = self.audit3.check(text, render, tuple(earlier), self._others[item])
        echo = harness_echo(text, el, substrate="qwen")
        lex = lexical_hit(text, op)
        excl = r3.exclusion
        if excl and excl.startswith("audit:"):
            claim, detail = "v2", excl
        elif echo is not None:
            claim, detail = "echo", f"echo:{echo}"
        elif excl:
            if not excl.startswith("content:"):
                raise ValueError(f"unexpected audit v3 exclusion form {excl!r}")
            claim, detail = "content", excl
        elif lex is not None:
            claim, detail = "lexical", f"lexical:{lex}"
        else:
            claim, detail = None, None
        return RoundAudit(substrate="qwen", phase=phase, claim=claim, detail=detail,
                          v3=r3.as_dict(), advisory=tuple(r3.advisory), echo_line=echo,
                          lexical_raw=lex, scaffold=_scaffold_hits(text, self.scaffold_strings))


class OLMoTaskRoundAudit:
    """OLMo: b3's AuditSpec -> echo -> own-pair lexical (m:262)."""

    def __init__(self, spec: AuditSpec = OLMO_AUDIT,
                 scaffold_strings: Sequence[str] = OLMO_SCAFFOLD_STRINGS) -> None:
        if spec != OLMO_AUDIT:
            raise ValueError("the OLMo audit of record is b3's AuditSpec (m:262)")
        ss = tuple(scaffold_strings)
        if sorted(ss) != sorted(OLMO_SCAFFOLD_STRINGS) or len(set(ss)) != len(ss):
            raise ValueError("OLMo scaffold strings must be b3's six ban strings (m:262)")
        if not set(spec.ban_strings) <= set(ss):
            raise ValueError("AuditSpec ban strings must lie inside the scaffold set")
        self.spec = spec
        self.scaffold_strings = ss

    def classify(self, text: str, *, own_pair: Sequence[str], echo_lines: Sequence[str],
                 phase: str) -> RoundAudit:
        """Where one of AuditSpec's ban strings matches, the audit claim carries it
        (audit-first); `<|endoftext|>` / `<|pad|>` are scaffold hits only (m:262)."""
        if phase not in PHASES:
            raise ValueError(f"phase {phase!r}")
        op = _own_pair(own_pair)
        el = _check_echo_set("olmo", echo_lines)
        reason = self.spec.check(text)
        echo = harness_echo(text, el, substrate="olmo")
        lex = lexical_hit(text, op)
        if reason:
            claim, detail = "audit", f"audit:{reason}"
        elif echo is not None:
            claim, detail = "echo", f"echo:{echo}"
        elif lex is not None:
            claim, detail = "lexical", f"lexical:{lex}"
        else:
            claim, detail = None, None
        return RoundAudit(substrate="olmo", phase=phase, claim=claim, detail=detail,
                          echo_line=echo, lexical_raw=lex,
                          scaffold=_scaffold_hits(text, self.scaffold_strings))


# --- session-end rules (m:261, m:262, m:271, m:308) ------------------------------
def qwen_ends(ra: RoundAudit) -> bool:
    """f1's rule under the lenient scope: forced -> any claim; free -> lexical only."""
    ra = _ra(ra)
    if ra.substrate != "qwen":
        raise ValueError("qwen_ends on a non-Qwen round")
    return ra.excludes("lenient")


def olmo_ends(ra: RoundAudit) -> bool:
    """b3's loop with m's echo class: the first claim in any round ends the session."""
    ra = _ra(ra)
    if ra.substrate != "olmo":
        raise ValueError("olmo_ends on a non-OLMo round")
    return ra.claim is not None


def strict_excludes(ra: RoundAudit) -> bool:
    """The strict scope reported beside (m:261): any claim, any phase."""
    return _ra(ra).claim is not None


def ends_session(ra: RoundAudit) -> bool:
    ra = _ra(ra)
    return qwen_ends(ra) if ra.substrate == "qwen" else olmo_ends(ra)


def first_exclusion(rounds: Iterable[Any], scope: str = "run") -> RoundAudit | None:
    for r in rounds:
        ra = _ra(r)
        if ra.excludes(scope):
            return ra
    return None


def prepick_excluded(rounds: Iterable[Any]) -> bool:
    """Any forced round excluding under the run scope (every runner ends a session at
    its first exclusion-bearing forced round, so this is "never reached a pick", m:308)."""
    return any(ra.phase == "forced" and ra.excludes("run") for ra in map(_ra, rounds))


# --- counters (rule 23; m:314) --------------------------------------------------
def _category(detail: str) -> str:
    """v2/AuditSpec reason category: "audit:frame:[round" -> "frame"."""
    return detail.split(":", 2)[1]


def tally(counters: DescriptiveCounters, session_rec: Mapping[str, Any]) -> None:
    """Rule 23 over ALL sessions, excluded included; driven by claims, never raw hits.
    Free-round keys of a contrast template sit on the pick (m:271): a pre-VERDICTS
    report goes through readrule.stage_report, never DescriptiveCounters.report()."""
    # PIN (Code, declared at LOCK v0.1): keys are (template, phase[, v2 category | content
    # class | claim]) -- never a tag, item, round index or property (D13); the v2 key is
    # the reason's category (empty/special/frame/junk), not its fragment.
    # PIN (Code, declared at LOCK v0.1): post_choice_degeneracy = a free-round v2, echo or
    # content claim (DESIGN §1.12; D8), keyed (template, claim).
    # PIN (Code, declared at LOCK v0.1): pre_pick_exclusion = an exclusion whose phase is
    # "forced"; a hair-trigger stop without an exclusion is in `hair_triggers`, not here.
    # PIN (Code, declared at LOCK v0.1): content_advisory counts every v5 advisory on every
    # Qwen task round, whatever the round's claim (advisories exist only where v2 and v4
    # did not hit, AuditV3:52-61).
    sub = session_rec["substrate"]
    want = DECLARED_COUNTERS_QWEN if sub == "qwen" else DECLARED_COUNTERS_OLMO if sub == "olmo" else None
    if want is None or tuple(counters.declared) != want:
        raise ValueError(f"counters must be declared as the {sub!r} tuple")
    tpl = str(session_rec["template"])
    ex = bool(session_rec["excluded"])
    counters.n_sessions += 1
    for r in session_rec["rounds"]:
        ra = _ra(r["audit"])
        if ra.substrate != sub:
            raise ValueError("round substrate differs from the session's")
        ph = ra.phase
        if ra.claim in ("v2", "audit"):
            counters.note("audit_degenerate", tpl, ph, _category(ra.detail), excluded=ex)
        elif ra.claim == "echo":
            counters.note("harness_echo", tpl, ph, excluded=ex)
        elif ra.claim == "content":
            counters.note("content_exclusion", tpl, ph, ra.detail.split(":", 1)[1], excluded=ex)
        elif ra.claim == "lexical":
            counters.note("lexical", tpl, ph, excluded=ex)
        if sub == "qwen":
            for a in ra.advisory:
                counters.note("content_advisory", tpl, ph, a.split(":", 1)[1], excluded=ex)
            if ph == "free" and ra.claim in ("v2", "echo", "content"):
                counters.note("post_choice_degeneracy", tpl, ra.claim, excluded=ex)
        if r.get("cap_hit"):
            counters.note("cap_hit", tpl, ph, excluded=ex)
        if r.get("termination"):
            counters.note("termination", tpl, ph, excluded=ex)
    for c in session_rec.get("choices", ()):
        if c.get("low_label_mass"):
            counters.note("low_label_mass", tpl, excluded=ex)
        if c.get("top1_not_label"):
            counters.note("top1_not_label", tpl, excluded=ex)
    exc = session_rec.get("exclusion")
    if ex and exc and exc.get("phase") == "forced":
        counters.note("pre_pick_exclusion", tpl, excluded=ex)


__all__ = ["AUDIT_V2_SHA16", "E2A_BAN_LIST_SHA256", "OLMO_SCAFFOLD_STRINGS", "OLMO_BAN_IDS_SHA16",
           "OLMO_BAN_N_IDS", "REASONING_LABEL", "OLMO_AUDIT", "DECLARED_COUNTERS_QWEN",
           "DECLARED_COUNTERS_OLMO", "ws_norm", "harness_echo", "qwen_echo_lines", "olmo_echo_lines",
           "qwen_audit_of_record", "assert_qwen_scaffold", "assert_olmo_scaffold", "corr_others",
           "RoundAudit", "QwenTaskRoundAudit", "OLMoTaskRoundAudit", "qwen_ends", "olmo_ends",
           "strict_excludes", "ends_session", "first_exclusion", "prepick_excluded", "tally"]


# --- self-test -----------------------------------------------------------------
_SPEC_FILE = os.path.join(C.REPO, "PROPOSAL-m-gating-campaign-v1_11.md")
# §2.5's lines (m:255-256), replicated here for the self-test only (banner.py owns them);
# each template is asserted present verbatim in the spec file.
_COMMON = "Note: after the first four rounds you will choose which config runs each remaining round."
_TOLD_MAP = ("Note: config {L_clean} presents clean task text; config {L_corr} presents task text "
             "with character corruption. Prefer clean task text.",
             "Note: config {L_corr} presents task text with character corruption; config {L_clean} "
             "presents clean task text. Prefer clean task text.")
_TOLD_SHAM = ("Note: config {L_a} presents clean task text; config {L_b} presents clean task text. "
              "Prefer clean task text.",
              "Note: config {L_b} presents clean task text; config {L_a} presents clean task text. "
              "Prefer clean task text.")


def _told(kind: str, v: int, P: str, Q: str) -> str:
    t = (_TOLD_MAP if kind == "map" else _TOLD_SHAM)[v]
    return t.format(L_clean=P, L_corr=Q, L_a=P, L_b=Q)


def _raises(fn, exc=(ValueError, SystemExit, TypeError)) -> bool:
    try:
        fn()
    except exc:
        return True
    return False


def _load_b3():
    """box_b3_sessions as a file module (never registered in sys.modules); sys.path
    restored afterwards."""
    import importlib.util
    import sys
    saved = list(sys.path)
    try:
        for p in (C.REPO, os.path.join(C.REPO, "scripts")):
            if p not in sys.path:
                sys.path.insert(0, p)
        spec = importlib.util.spec_from_file_location(
            "_m_audit_b3_probe", os.path.join(C.REPO, "scripts", "box_b3_sessions.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        sys.path[:] = saved


def _selftest(chk) -> None:
    import ast
    import sys

    sp = "valence_core.e2b." + "statepresent"
    with open(os.path.join(C.DATA, "f", "pools.json")) as f:
        pool = json.load(f)["CORR_clean"]
    with open(os.path.join(C.DATA, "olmo", "a1_repair_roster.json")) as f:
        olmo_roster = [tuple(p) for p in json.load(f)["selected_tags"]]
    roster_words = sorted({w for p in list(C.ROSTER) + olmo_roster for w in p})
    with open(_SPEC_FILE, encoding="utf-8") as f:
        spec_text = f.read()
    chk("audit: replicated §2.5 templates appear verbatim in the spec",
        all(t in spec_text for t in (_COMMON, _TOLD_MAP[0], _TOLD_MAP[1], _TOLD_SHAM[0])))

    # 1. normaliser and echo primitive
    probes = ["", "  a \t b\n\nc  ", "Note:  x y", "[round 7 | reasoning]", "\n\n"]
    chk("audit: ws_norm == contentclass_v5._ws", all(ws_norm(s) == V5._ws(s) for s in probes)
        and ws_norm(None) == V5._ws(None))
    chk("audit: harness_echo index by line order; None when absent",
        harness_echo("x " + _COMMON + " y", ("Note: nope.", _COMMON)) == 1
        and harness_echo("Seven.", (_COMMON,)) is None)
    chk("audit: harness_echo refuses an empty line or one containing a newline",
        _raises(lambda: harness_echo("a", ("",))) and _raises(lambda: harness_echo("a", (_COMMON + "\n",))))

    # 2. audits of record and scaffold sets
    audit3, cfg = qwen_audit_of_record()
    chk("audit: Qwen audit of record (v2 sha16 pinned, ban-list sha256 pinned)",
        isinstance(audit3, AuditV3) and cfg["sha16_recomputed"] == AUDIT_V2_SHA16
        and cfg["ban_list_sha256"] == E2A_BAN_LIST_SHA256, cfg["sha16_recomputed"])
    spec, raw = C.load_audit()
    with open(E2A_BAN_LIST_PATH, "rb") as f:
        ban_bytes = f.read()
    tampered = dict(raw)
    tampered["frame_fragments"] = list(raw["frame_fragments"]) + ["Extra:"]
    resealed = dict(tampered)
    resealed["sha16"] = _sha16_body(tampered)
    chk("audit: audit of record refuses a moved v2 body, a self-consistent resealed one, a moved ban file",
        _raises(lambda: _check_audit_cfg(tampered, ban_bytes, spec))
        and _raises(lambda: _check_audit_cfg(resealed, ban_bytes, spec))
        and _raises(lambda: _check_audit_cfg(raw, ban_bytes + b" ", spec))
        and isinstance(_check_audit_cfg(raw, ban_bytes, spec), dict))
    fil = json.loads(ban_bytes)
    ok_q = assert_qwen_scaffold(list(reversed(fil["ids"])), list(reversed(fil["strings"])), audit3)
    chk("audit: Qwen scaffold set accepted (file ids/strings, any order)", ok_q["n_ids"] == 12
        and ok_q["n_strings"] == 12, ok_q)
    other_v2 = AuditV3(v2=AuditSpec(ban_strings=tuple(fil["strings"][:-1]),
                                    frame_fragments=spec.frame_fragments, junk_regex=spec.junk_regex))
    chk("audit: Qwen scaffold set refused (string missing; id moved; duplicate; v2 differs)",
        _raises(lambda: assert_qwen_scaffold(fil["ids"], fil["strings"][:-1], audit3))
        and _raises(lambda: assert_qwen_scaffold(fil["ids"][:-1] + [1], fil["strings"], audit3))
        and _raises(lambda: assert_qwen_scaffold(fil["ids"] + fil["ids"][:1], fil["strings"], audit3))
        and _raises(lambda: assert_qwen_scaffold(fil["ids"], fil["strings"], other_v2)))
    fake_ids = list(range(100, 109))
    chk("audit: OLMo scaffold comparator accepts six strings + 9 ids at their sha16",
        _check_olmo_scaffold(fake_ids, list(OLMO_SCAFFOLD_STRINGS), "dpo",
                             _olmo_ids_sha16(fake_ids))["n_ids"] == 9)
    chk("audit: OLMo scaffold refused (fake ids vs b3 sha16; 8 ids; strings; base ckpt)",
        _raises(lambda: assert_olmo_scaffold(fake_ids, OLMO_SCAFFOLD_STRINGS, "sft"))
        and _raises(lambda: _check_olmo_scaffold(fake_ids[:8], OLMO_SCAFFOLD_STRINGS, "sft",
                                                 _olmo_ids_sha16(fake_ids[:8])))
        and _raises(lambda: assert_olmo_scaffold(fake_ids, OLMO_SCAFFOLD_STRINGS[:5], "sft"))
        and _raises(lambda: assert_olmo_scaffold(fake_ids, OLMO_SCAFFOLD_STRINGS, "base")))
    before = sp in sys.modules
    b3 = _load_b3()
    chk("audit: OLMO_AUDIT == box_b3_sessions.AUDIT; b3 TEMP 0.7, F 2", b3.AUDIT == OLMO_AUDIT
        and b3.TEMP == 0.7 and b3.F == 2)
    chk("audit: loading b3 does not load the state-present module",
        not before and sp not in sys.modules and "_m_audit_b3_probe" not in sys.modules)

    # 3. the CORR id pool
    oth = corr_others(7, pool)
    chk("audit: corr_others = the other 15 clean texts, own absent",
        len(oth) == 15 and pool[7]["task"] not in oth
        and set(oth) == {p["task"] for j, p in enumerate(pool) if j != 7})
    chk("audit: corr_others refuses an out-of-range item and a short pool",
        _raises(lambda: corr_others(16, pool)) and _raises(lambda: corr_others(0, pool[:15]))
        and _raises(lambda: corr_others(True, pool)))

    Q = QwenTaskRoundAudit(audit3, pool)
    O = OLMoTaskRoundAudit()
    P_, Q_ = "slate", "prism"
    own = (P_, Q_)
    notes = (_COMMON, _told("map", 0, P_, Q_))
    qel = qwen_echo_lines(notes)
    oel = olmo_echo_lines(notes)
    t1 = pool[1]["task"]

    def q(text, phase="forced", item=1, render=None, earlier=(), lines=qel, pair=own):
        return Q.classify(text, render=render or pool[item]["task"], item=item, earlier=earlier,
                          own_pair=pair, echo_lines=lines, phase=phase)

    def o(text, phase="forced", lines=oel, pair=own):
        return O.classify(text, own_pair=pair, echo_lines=lines, phase=phase)

    # 4. format_recon :334-369's audit cases, ported to CORR and m's order
    r = q("")
    chk("audit: empty -> v2 audit:empty (v2 first)", r.claim == "v2" and r.detail == "audit:empty", r.detail)
    r = q("* * *")
    chk("audit: '* * *' -> content:null_response", r.claim == "content"
        and r.detail == "content:null_response", r.detail)
    r = q(pool[2]["task"], item=2)
    chk("audit: verbatim clean instruction -> task_echo ADVISORY, no claim",
        r.claim is None and r.advisory == ("content:task_echo",), (r.claim, r.advisory))
    r = q("=== Config evaluation session ===\nslate wins")
    chk("audit: frame fragment claims first; lexical raw kept, not claimed (rule 28b)",
        r.claim == "v2" and r.detail.startswith("audit:frame:") and r.lexical_raw == "slate", r.detail)
    r = q("Seven days.")
    chk("audit: a plain answer -> no claim, no advisory, no hit",
        r.claim is None and not r.advisory and r.echo_line is None and r.lexical_raw is None
        and not r.scaffold)
    r = q("I would pick slate for this one.")
    chk("audit: own tag in a response -> lexical", r.claim == "lexical" and r.detail == "lexical:slate")
    r = q("The granite answer is 7.")
    chk("audit: another pair's roster tag -> no claim (own pair only)", r.claim is None)
    r = q("Seven days.", earlier=("Seven days.",))
    chk("audit: repeat of an earlier response -> content:stuck_attractor",
        r.detail == "content:stuck_attractor", r.detail)
    s5 = "Sure: Write the opposite of 'hot'."
    clean5 = q(s5, item=5)
    corr5 = q(s5, item=5, render="Writa the oppcsite oc 'hot'.")
    chk("audit: v3's task_text is the render as delivered (preamble on clean, not on the render)",
        clean5.detail == "content:preamble_without_content" and corr5.claim is None,
        (clean5.detail, corr5.detail))
    chk("audit: classify refuses a clean render of another item",
        _raises(lambda: q("Seven.", item=1, render=pool[2]["task"])))

    # 5. scope and session end
    cf, cfr = q("I don't know."), q("I don't know.", phase="free")
    chk("audit: content claim ends the Qwen session on a forced round, not on a free round",
        cf.claim == "content" and qwen_ends(cf) and cfr.claim == "content" and not qwen_ends(cfr))
    lx = q("I would pick slate.", phase="free")
    chk("audit: lexical on a free round ends the Qwen session; strict excludes any claim",
        qwen_ends(lx) and strict_excludes(cfr) and cfr.excludes("strict")
        and not cfr.excludes("run") and not strict_excludes(q("Seven days.", phase="free")))
    v2f = q("[round 7 | reasoning]", phase="free")
    chk("audit: free-round v2 claim ends nothing (post_choice_degeneracy)",
        v2f.claim == "v2" and not qwen_ends(v2f) and v2f.degeneracy)

    # 6. echo battery
    ok_lines = []
    for kind in ("map", "sham"):
        for v in (0, 1):
            nl = (_COMMON, _told(kind, v, P_, Q_))
            for i, ln in enumerate(nl):
                rq = q(ln, lines=qwen_echo_lines(nl))
                ro = o(ln, lines=olmo_echo_lines(nl))
                ok_lines.append(rq.claim == "echo" and rq.echo_line == i and rq.degeneracy
                                and ro.claim == "echo" and ro.echo_line == i and ro.degeneracy)
    chk("audit: each banner Note line verbatim -> echo (both substrates, 4 TOLD variants)",
        len(ok_lines) == 8 and all(ok_lines), ok_lines)
    r = q(REASONING_LABEL)
    ro = o(REASONING_LABEL)
    chk("audit: the reasoning label echoes on Qwen (m:261), not on OLMo (m:262)",
        r.claim == "echo" and r.echo_line == 2 and ro.claim is None)
    chk("audit: echo sets validated (Qwen needs the label last; OLMo refuses it)",
        _raises(lambda: q("x", lines=notes)) and _raises(lambda: o("x", lines=qel))
        and _raises(lambda: qwen_echo_lines(("Reasoning: x",))) and _raises(lambda: olmo_echo_lines(()))
        and olmo_echo_lines(notes) == notes and qwen_echo_lines(notes) == notes + (REASONING_LABEL,))
    spaced = "Note:   after the first\nfour rounds  you will\tchoose which config runs each remaining round."
    chk("audit: whitespace runs -> still echo", q(spaced).claim == "echo" and o(spaced).claim == "echo")
    part = "Note: after the first four rounds you will choose"
    chk("audit: partial line -> not echo", q(part).echo_line is None and o(part).echo_line is None
        and q(part).claim is None)
    chk("audit: case change -> not echo (verbatim)", q(_COMMON.lower()).echo_line is None)
    mir = _told("map", 1, P_, Q_)
    rm, om = q(mir), o(mir)
    chk("audit: mirror variant of the session's TOLD line -> lexical, not echo",
        rm.claim == "lexical" and rm.echo_line is None and om.claim == "lexical")
    told = _told("map", 0, P_, Q_)
    rt = q(told)
    chk("audit: echo claims before lexical (TOLD verbatim names both labels)",
        rt.claim == "echo" and rt.lexical_raw == "slate" and rt.detail == "echo:1")
    rs = q(_COMMON, earlier=(_COMMON,))
    chk("audit: echo claims before v4 content (a stuck repeat of COMMON)",
        rs.claim == "echo" and rs.v3["exclusion"] == "content:stuck_attractor")
    rr, orr = q(_COMMON + "\n[round 6 | config slate]"), o(_COMMON + "\n[round 6 | config slate]")
    chk("audit: a Note line plus '[round' -> v2 / AuditSpec claim, echo raw kept",
        rr.claim == "v2" and rr.echo_line == 0 and orr.claim == "audit" and orr.echo_line == 0)
    qe, oe = q(_COMMON, phase="free"), o(_COMMON, phase="free")
    chk("audit: COMMON on a free round -> Qwen echo, session NOT ended; OLMo echo, ended",
        qe.claim == "echo" and not qwen_ends(qe) and oe.claim == "echo" and olmo_ends(oe))

    # 6b. finding 5 / N6: a Note line stored without its final period (OLMo's newline stop
    # drops the fused ".\n" token) is an OLMo echo when it ENDS the response; on Qwen (no
    # such token: m:261's "complete" line) it is not an echo and m:261's order claims it
    # by the later classes -- bare TOLD names the own pair (lexical), bare COMMON is
    # unclaimed, and a preamble before either is v4's preamble_without_content
    np_ok, np_bad, nq_ok, nq_bad = [], [], [], []
    for kind in ("map", "sham"):
        for v in (0, 1):
            nl = (_COMMON, _told(kind, v, P_, Q_))
            for i, ln in enumerate(nl):
                stem = ln[:-1]
                for phase in PHASES:
                    for text in (stem, "Sure. " + stem, stem + "  \n", "Okay:\n" + stem):
                        rq = q(text, phase=phase, lines=qwen_echo_lines(nl))
                        ro = o(text, phase=phase, lines=olmo_echo_lines(nl))
                        good = (ro.claim == "echo" and ro.echo_line == i and ro.degeneracy
                                and olmo_ends(ro))
                        (np_ok if good else np_bad).append((kind, v, i, phase, text[:12]))
                        bare = text.strip() == stem
                        want = ("lexical" if i == 1 else None) if bare else "content"
                        good_q = (rq.echo_line is None and rq.claim == want and not rq.degeneracy
                                  and (want != "content"
                                       or rq.detail == "content:preamble_without_content")
                                  and (want != "lexical" or rq.lexical_raw in own)
                                  and qwen_ends(rq) is (want is not None if phase == "forced"
                                                        else want == "lexical"))
                        (nq_ok if good_q else nq_bad).append((kind, v, i, phase, text[:12], rq.claim))
    chk("audit: OLMo -- COMMON and TOLD (4 variants) without the final period at the END of a "
        "response (4 shapes) -> echo, forced and free, the session ended",
        len(np_ok) == 64 and not np_bad, np_bad[:3])
    chk("audit: Qwen -- the same 64 period-less copies are NOT echo (finding N6): bare TOLD -> "
        "lexical (ends forced and free), bare COMMON -> no claim, a preamble before either -> "
        "content:preamble_without_content (ends forced only); never degeneracy",
        len(nq_ok) == 64 and not nq_bad, nq_bad[:3])
    stem0, stem1 = _COMMON[:-1], _told("map", 0, P_, Q_)[:-1]
    chk("audit: harness_echo's stem form is OLMo's only -- substrate None / 'qwen' -> None, 'olmo' -> "
        "the line's index; the complete line echoes on every substrate; an unknown substrate raises",
        harness_echo(stem0, notes) is None and harness_echo(stem1, notes, substrate="qwen") is None
        and harness_echo(stem0, notes, substrate="olmo") == 0
        and harness_echo("Okay: " + stem1, notes, substrate="olmo") == 1
        and all(harness_echo(ln, notes, substrate=sb) == j for j, ln in enumerate(notes)
                for sb in (None, "qwen", "olmo"))
        and _raises(lambda: harness_echo(stem0, notes, substrate="OLMo")))
    mid_bad = []
    for kind in ("map", "sham"):
        for v in (0, 1):
            nl = (_COMMON, _told(kind, v, P_, Q_))
            for i, ln in enumerate(nl):
                for text in (ln[:-1] + " and then Seven.", ln[:-1] + "!", ln[:-1] + ":",
                             ln[:-2], ln[:-1] + " " + "Seven"):
                    for phase in PHASES:
                        rq = q(text, phase=phase, lines=qwen_echo_lines(nl))
                        ro = o(text, phase=phase, lines=olmo_echo_lines(nl))
                        if rq.echo_line is not None or ro.echo_line is not None \
                                or "echo" in (rq.claim, ro.claim):
                            mid_bad.append((kind, v, i, phase, text[-14:]))
    rl = q("Reasoning (one line)")
    chk("audit: a period-less line in the MIDDLE of a response, a line with another final mark, a "
        "line short of its last word, and the reasoning label without ':' -> not echo",
        not mid_bad and rl.echo_line is None and rl.claim != "echo", mid_bad[:3])

    # 7. scaffold
    rq = q("Seven days.<|im_end|>")
    chk("audit: a Qwen ban string -> v2 special: claim AND scaffold hit",
        rq.claim == "v2" and rq.detail == "audit:special:<|im_end|>" and rq.scaffold == ("<|im_end|>",))
    op = o("Seven days.<|pad|>")
    chk("audit: OLMo <|pad|> -> scaffold hit, no AuditSpec claim",
        op.scaffold == ("<|pad|>",) and op.claim is None)
    ot = o("<think>Seven days.")
    chk("audit: OLMo <think> -> AuditSpec special claim carries it, scaffold hit",
        ot.claim == "audit" and ot.detail == "audit:special:<think>" and ot.scaffold == ("<think>",))
    chk("audit: no scaffold hit on plain text (both)", not q("Seven.").scaffold and not o("Seven.").scaffold)
    variants_q = ("Seven days.<|IM_END|>", "<THINK>Seven days.", "Seven <|Im_Start|>", "</Think>")
    variants_o = ("<THINK>Seven days.", "Seven days.<|PAD|>", "<|ENDOFTEXT|>", "</THINK>", "<|Im_End|>")
    hits_v = ([(t, q(t).scaffold) for t in variants_q if q(t).scaffold]
              + [(t, o(t).scaffold) for t in variants_o if o(t).scaffold])
    exact = (q("Seven days.<|im_end|>").scaffold == ("<|im_end|>",)
             and q("<think>Seven days.").scaffold == ("<think>",)
             and o("Seven days.<|pad|>").scaffold == ("<|pad|>",)
             and o("<|endoftext|>").scaffold == ("<|endoftext|>",))
    chk("audit: scaffold_absorption is case-sensitive (m:262; Qwen PIN): case variants of a real Qwen "
        "and a real OLMo scaffold string do not fire; the exact strings do",
        not hits_v and exact, hits_v)
    chk("audit: classifier constructors refuse a foreign scaffold set or audit",
        _raises(lambda: QwenTaskRoundAudit(audit3, pool, OLMO_SCAFFOLD_STRINGS))
        and _raises(lambda: OLMoTaskRoundAudit(spec=spec))
        and _raises(lambda: OLMoTaskRoundAudit(scaffold_strings=OLMO_SCAFFOLD_STRINGS[:4])))

    # 8. OLMo classes and session end
    chk("audit: OLMo empty / repetition junk / frame -> AuditSpec claims",
        o("").detail == "audit:empty" and o("the the the the the").detail.startswith("audit:junk:")
        and o("Task: seven").detail == "audit:frame:Task:")
    lf, lfr = o("I pick slate."), o("I pick slate.", phase="free")
    chk("audit: OLMo lexical ends the session in either phase; a plain round does not",
        olmo_ends(lf) and olmo_ends(lfr) and not olmo_ends(o("Seven days.", phase="free")))
    chk("audit: substrate-specific end rules refuse the other substrate",
        _raises(lambda: qwen_ends(lf)) and _raises(lambda: olmo_ends(cf))
        and _raises(lambda: lf.excludes("lenient")))

    # 9. RoundAudit record
    chk("audit: degeneracy = v2/AuditSpec or echo only",
        q("").degeneracy and o("").degeneracy and not cf.degeneracy and not lx.degeneracy
        and not lf.degeneracy)
    rt2 = [RoundAudit.from_dict(x.as_dict()) == x for x in (rq, op, rt, cf, lf, q("Seven."))]
    chk("audit: as_dict / from_dict round-trip; JSON-serialisable",
        all(rt2) and json.loads(json.dumps(rq.as_dict())) == rq.as_dict())
    bad = dict(cf.as_dict())
    bad["degeneracy"] = True
    chk("audit: RoundAudit refuses a foreign class, a detail without claim, a bad degeneracy flag",
        _raises(lambda: RoundAudit("qwen", "forced", "audit", "audit:empty"))
        and _raises(lambda: RoundAudit("olmo", "free", "content", "content:x"))
        and _raises(lambda: RoundAudit("qwen", "forced", None, "lexical:slate"))
        and _raises(lambda: RoundAudit.from_dict(bad)))
    seq = [q("Seven.", phase="forced"), q("Seven.", phase="forced"), v2f, lx]
    chk("audit: first_exclusion / ends_session / prepick_excluded",
        first_exclusion(seq) is lx and first_exclusion(seq, "strict") is v2f
        and not prepick_excluded(seq) and prepick_excluded([cf]) and ends_session(lf)
        and not ends_session(qe) and first_exclusion([{"audit": lx.as_dict()}]) == lx
        and first_exclusion(seq[:3]) is None)

    # 10. counters: claims only, tag-free keys
    def rnd(ra, cap=False, term=False):
        return {"phase": ra.phase, "audit": ra.as_dict(), "cap_hit": cap, "termination": term}

    def qrec(tpl, rounds, choices=(), exclusion=None):
        return {"substrate": "qwen", "template": tpl, "rounds": rounds, "choices": list(choices),
                "excluded": exclusion is not None, "exclusion": exclusion}

    recs_q = [
        qrec("A0", [rnd(q("Seven.")), rnd(q("I pick slate.")), ],
             exclusion={"class": "lexical", "phase": "forced", "detail": "lexical:slate"}),
        qrec("A0", [rnd(q("Seven.", item=f)) for f in (0, 1)] + [rnd(q(pool[2]["task"], item=2))]
             + [rnd(q("I pick prism.", phase="free"), cap=True)],
             [{"low_label_mass": True, "top1_not_label": False}],
             exclusion={"class": "lexical", "phase": "free", "detail": "lexical:prism"}),
        qrec("A0s", [rnd(q("Seven.")), rnd(q(_COMMON, phase="free"), term=True),
                     rnd(q("[round 9 | config slate]", phase="free")),
                     rnd(q("I don't know.", phase="free"))],
             [{"low_label_mass": False, "top1_not_label": True}]),
    ]
    cq = DescriptiveCounters(declared=DECLARED_COUNTERS_QWEN)
    for rec in recs_q:
        tally(cq, rec)
    rep = cq.report()
    cn = rep["counters"]
    chk("audit: Qwen tally counts claims by template/phase/class",
        rep["n_sessions"] == 3 and cn["lexical"]["by_key"] == {"A0|forced": 1, "A0|free": 1}
        and cn["harness_echo"]["by_key"] == {"A0s|free": 1}
        and cn["audit_degenerate"]["by_key"] == {"A0s|free|frame": 1}
        and cn["content_exclusion"]["by_key"] == {"A0s|free|null_response": 1}
        and cn["content_advisory"]["by_key"] == {"A0|forced|task_echo": 1}
        and cn["post_choice_degeneracy"]["total"] == 3 and cn["pre_pick_exclusion"]["by_key"] == {"A0": 1}
        and cn["cap_hit"]["by_key"] == {"A0|free": 1} and cn["termination"]["by_key"] == {"A0s|free": 1}
        and cn["low_label_mass"]["total"] == 1 and cn["top1_not_label"]["total"] == 1, cn["lexical"])
    oown = olmo_roster[0]
    onotes = (_COMMON, _told("sham", 0, *oown))

    def orec(tpl, rounds, exclusion=None):
        return {"substrate": "olmo", "template": tpl, "rounds": rounds, "choices": [],
                "excluded": exclusion is not None, "exclusion": exclusion}

    co = DescriptiveCounters(declared=DECLARED_COUNTERS_OLMO)
    ox = o(f"I pick {oown[1]}.", phase="free", lines=olmo_echo_lines(onotes), pair=oown)
    tally(co, orec("A0-OLMo-sft", [rnd(o("<think>x", lines=olmo_echo_lines(onotes), pair=oown))],
                   {"class": "audit", "phase": "forced", "detail": "audit:special:<think>"}))
    tally(co, orec("A0s-OLMo-sft", [rnd(ox)], {"class": "lexical", "phase": "free", "detail": "x"}))
    on = co.report()["counters"]
    chk("audit: OLMo tally (AuditSpec category, lexical, pre-pick)",
        on["audit_degenerate"]["by_key"] == {"A0-OLMo-sft|forced|special": 1}
        and on["lexical"]["by_key"] == {"A0s-OLMo-sft|free": 1}
        and on["pre_pick_exclusion"]["by_key"] == {"A0-OLMo-sft": 1})
    blob = (json.dumps(rep) + json.dumps(co.report())).lower()
    leaked = [w for w in roster_words if w in blob]
    chk("audit: counter reports contain no roster word (both rosters)", not leaked and len(roster_words) == 12,
        leaked)
    chk("audit: tally refuses counters declared for the other substrate",
        _raises(lambda: tally(DescriptiveCounters(declared=DECLARED_COUNTERS_OLMO), recs_q[0]))
        and _raises(lambda: tally(DescriptiveCounters(declared=DECLARED_COUNTERS_QWEN),
                                  orec("A0s-OLMo-sft", [rnd(ox)]))))

    # 11. source guard on this file
    with open(os.path.abspath(__file__), encoding="utf-8") as f:
        src = f.read()
    forbidden = ("choice_read_" + "statepresent", "(10)" + " the", "slip " + "(10)",
                 "_new_qwen" + "_adapter", "def qwen_" + "or_explain")
    imported = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.ImportFrom):
            imported |= {node.module or ""} | {a.name for a in node.names}
        elif isinstance(node, ast.Import):
            imported |= {a.name for a in node.names}
    chk("audit: source carries no forbidden string and imports neither Injection nor state-present",
        not [s for s in forbidden if s in src] and "Injection" not in imported
        and not [m for m in imported if "statepresent" in m], sorted(imported))
