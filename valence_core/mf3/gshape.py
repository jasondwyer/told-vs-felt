"""G-SHAPE-F3 -- scoring-scope plumbing for Q-F3, model-free (PROPOSAL-m v1.11 §3.2 m:290; with m:277,
m:174, m:261-265; the design seat's prebuild answers of 2026-11-06, Q8 and §8's "declared check for the
build hazard"; Code's dated note N6).

m:290: "G-SHAPE-F3 (plumbing). As G-SHAPE-F0 for the F3 templates, the reasoning header included." m:277
(G-SHAPE-F0): "Model-free: every corrupted render placed inside each F0m and F0m-OLMo round template beside
its bracketed header, a clean gold as the response, run through the full scoring stack of both substrates;
asserts that no class fires on harness bytes or the render itself. It tests scoring scope, nothing else."

THE ARTIFACT OF RECORD (``data/mf3/gates/G-SHAPE-F3.json``, write-once) carries:

  Layer A  m:277's placements for F3: per contrast template (A1, A2, A3 -- a render sits only under a
           contrast arm's Q role, m:172) every banner the template takes (A1 16: pair x map x clause; A2 and
           A3 8: pair x map) x ROUND_TEMPLATES[0..3] x the 16 renders of record x every gold variant (22) x
           both phases: 5,632 placements, each gold scored by the Qwen stack exactly as the F3 runner calls
           it (m.audit.QwenTaskRoundAudit, the session's echo set); a placement fires iff any of m's twelve
           round fields fires.
  Layer C  per placement the scope-widened controls: ``seg+gold`` (required, 100%) and, at the free phase,
           ``reasoning+seg+gold`` (the reasoning block, the round's segment and the gold as one response;
           required, 100% -- the reasoning header included); ``render-as-response`` reported only.
  Layer R  the reasoning line's own placements: every banner of the six F3 templates x the free choices' n
           (5..10) x every gold variant as the line, run through the reasoning-line classes (m:265) and the
           scaffold hits as the runner calls them; a placement fires iff a class or a hit fires. Its control:
           the reasoning block itself as the line, plus the gold (required, 100%: the echo class fires).
  Layer S  a static (ast) check of mf3's runner: ``run_session_f3`` hands the task-round classifier the
           generation's text (twice: forced, free) and the line classifier the line's generation; earlier
           gets task-round texts only; no classify reference elsewhere outside self-tests, the verifier's
           re-derivation and this module.
  Layer T  Code's declared check for the build hazard (the seat's Q8 on the "\\n\\n" after the reasoning
           segment; N6): on the Qwen tokenizer of record (tokenizer.json of the snapshot of record, loaded
           with ``tokenizers``, no model), every F3 generation join -- the reasoning block after the forced
           rounds, the chosen round after an empty, whitespace-only, newline-led or plain reasoning line, the
           next reasoning block after it -- has its token-comparison boundary equal to the prefix token count
           and its character-offset boundary (the tokenizer's own offsets) equal to it, and the runtime form
           (decode of the first k tokens == the prefix) holds.

Model-free: no model, no generation; Layer T loads a tokenizer only.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping, Sequence

from valence_core.m import audit as m_audit
from valence_core.m import corr as m_corr
from valence_core.m import keys as m_keys
from valence_core.session_e2a import MENU_TEMPLATES, ROUND_TEMPLATES, SESSION_BANNER

from . import banner, guard, keys, lines, schedule
from . import resume as rs
from . import scaffold as sc_mod

REPO = Path(__file__).resolve().parents[2]
SCHEMA = "m-gshape-f3-v1"
STAGE = "G-SHAPE-F3"
ARTIFACT_NAME = "G-SHAPE-F3.json"
SPEC_REF = "PROPOSAL-m v1.11 §3.2 G-SHAPE-F3 (m:290), as G-SHAPE-F0 (m:277); §8 step 19 (m:361)"
CRITERION_HEAD = "**G-SHAPE-F3 (plumbing).**"
CRITERION = "As G-SHAPE-F0 for the F3 templates, the reasoning header included."
CRITERION_F0 = ("Model-free: every corrupted render placed inside each F0m and F0m-OLMo round template beside its "
                "bracketed header, a clean gold as the response, run through the full scoring stack of both "
                "substrates; asserts that no class fires on harness bytes or the render itself. It tests scoring "
                "scope, nothing else.")
RENDERS_SHA256_OF_RECORD = "a04f67b0e5105a0514a0f33e64a4545ef3a3a3c75cece320d78434e853cd4372"
MODEL_FREE_REL = "data/m/gates/G-CAL_model-free.json"
COMPLETABILITY_REL = "data/m/gates/G-CAL_completability_qwen.json"
SEAT_READ_REL = "data/m/gates/G-CAL_seat_read_of_record.md"
PHASES = ("forced", "free")
N_ITEMS = 16
N_GOLD_VARIANTS = 22
ROUND_FIRE_FIELDS = ("claim", "advisory", "v3.exclusion", "v3.content_label", "v3.advisory", "echo_line",
                     "lexical_raw", "scaffold", "degeneracy", "ends", "strict", "termination")
LINE_FIRE_FIELDS = ("empty", "cap_no_newline", "echo", "scaffold")
CONTROLS_REQUIRED = ("seg+gold", "reasoning+seg+gold")
CONTROLS_REPORTED = ("render-as-response",)
#: The scoring stack outside the two packages (G-SHAPE-F0's list minus its OLMo files).
STACK_FILES = ("valence_core/session.py", "valence_core/session_e2a.py", "valence_core/e2d/audit_v3.py",
               "valence_core/e2d/contentclass.py", "valence_core/e2d/contentclass_v4.py",
               "valence_core/e2d/contentclass_v5.py", "valence_core/e2d/config.py",
               "data/configs/e2b_audit_v2.json", "data/configs/e2a_ban_list.json",
               "data/configs/f_termination_patterns.json", "data/f/pools.json")
TOOLING_FILES = ("valence_core/mf3/gshape.py", "scripts/mf3_sessions.py")
#: Layer T's reasoning-line texts: empty, whitespace-only, newline-led, two blank lines, plain, a trailing
#: space, a line whose last character is a colon (the block's own ending).
LAYER_T_LINES = ("", "   ", "\nThe tasks look fine.", "\n\n", "The tasks look fine.", "Both answered. ", "Note:")
QWEN_REVISION = "c000ac2c2057d94be3fa931000c31723aac53282"
QWEN_MODEL_ID = rs.QWEN_MODEL_ID
EXIT = {"PASS": 0, "STOP": 4}
#: The runner self-test checks cited as Layer S's dynamic evidence (their names must stay as written).
RUNNER_DYNAMIC_EVIDENCE = (
    "mf3.runner: {} scripted F3 sessions reach their declared outcomes",
    "mf3.runner: reasoning-line classes are recorded and end nothing; the production empty line (text \"\" at the "
    "cap) writes \"Reasoning (one line):\\n\\n\" into the transcript; a line naming a label is not lexical-claimed "
    "and never enters earlier (m:265)",
    "mf3.runner: pieces tile the transcript; each menu and reasoning line sits at its piece",
)


class GshapeRefusal(SystemExit):
    """Decided before scoring (paths, inputs, the committed sources); nothing written (exit 2)."""


class GshapeStop(SystemExit):
    """A pinned figure that does not reproduce; no artifact (exit 4)."""


def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _json_sha256(obj: Any) -> str:
    return _sha256(rs.json_text(obj).encode("utf-8"))


# --- the governing text and the committed sources ---------------------------------------------
def criterion_problems(text: str) -> list[str]:
    ln = [x for x in text.splitlines() if x.startswith(CRITERION_HEAD)]
    if len(ln) != 1 or CRITERION not in ln[0]:
        return [f"m:290's G-SHAPE-F3 line is not exactly once with its criterion ({len(ln)} lines)"]
    f0 = [x for x in text.splitlines() if x.startswith("**G-SHAPE-F0 (plumbing).**")]
    if len(f0) != 1 or CRITERION_F0 not in f0[0]:
        return ["m:277's G-SHAPE-F0 criterion (the 'as') is not the proposal's"]
    return []


def source_files() -> list[str]:
    """Every file the artifact's sources map records: mf3's package, the imported m modules, the stack
    outside both packages and the tooling."""
    pkg = [p.relative_to(REPO).as_posix() for p in sorted(guard.PACKAGE_DIR.glob("*.py"))]
    mm = [f"valence_core/m/{m}.py" for m in guard.M_HASHED]
    return sorted(set(pkg + mm + list(STACK_FILES) + list(TOOLING_FILES)))


def sources_map(*, canonical: bool) -> tuple[list[str], dict]:
    """(problems, {rel: sha256}); on the canonical run each file is committed at HEAD and unedited
    (stages.committed, the committed blob's sha256)."""
    from . import stages
    probs, out = [], {}
    for rel in source_files():
        if canonical:
            p, data = stages.committed(rel)
            if p or data is None:
                probs += p or [f"{rel}: no bytes"]
                out[rel] = None
                continue
        else:
            try:
                data = (REPO / rel).read_bytes()
            except OSError:
                probs.append(f"{rel}: unreadable")
                out[rel] = None
                continue
        out[rel] = _sha256(data)
    return probs, out


def import_closure(*, canonical: bool) -> tuple[list[str], dict]:
    """Every loaded valence_core.* module outside valence_core/m and valence_core/mf3 (their files are
    in the sources map), as {rel: sha256}; committed on the canonical run."""
    from . import stages
    probs, out = [], {}
    skip = {(REPO / "valence_core" / "m").resolve(), guard.PACKAGE_DIR.resolve()}
    for name, mod in sorted(list(sys.modules.items()), key=lambda kv: kv[0]):
        if not (name == "valence_core" or name.startswith("valence_core.")):
            continue
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        p = Path(f).resolve()
        if p.parent in skip:
            continue
        try:
            rel = p.relative_to(REPO.resolve()).as_posix()
        except ValueError:
            probs.append(f"{name}: {f} lies outside the repository")
            continue
        if canonical:
            cp, data = stages.committed(rel)
            if cp or data is None:
                probs += cp or [f"{rel}: no bytes"]
                continue
        else:
            data = p.read_bytes()
        out[rel] = _sha256(data)
    return probs, out


# --- inputs of record ----------------------------------------------------------------------------
def _committed_json(rel: str, canonical: bool) -> tuple[Any, str]:
    from . import stages
    if canonical:
        p, data = stages.committed(rel)
        if p or data is None:
            raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: {rel}: {p or ['no bytes']}")
    else:
        data = (REPO / rel).read_bytes()
    try:
        return json.loads(data.decode("utf-8")), _sha256(data)
    except (UnicodeDecodeError, ValueError):
        raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: {rel} is not readable JSON") from None


def qwen_stack(pool) -> tuple[m_audit.QwenTaskRoundAudit, dict]:
    """The Qwen stack as f3_startup builds it, without the live-tokenizer half (G-SHAPE-F0's PIN-S4)."""
    audit3, cfg = m_audit.qwen_audit_of_record()
    fil = json.loads(Path(m_audit.E2A_BAN_LIST_PATH).read_bytes())
    sca = m_audit.assert_qwen_scaffold(fil["ids"], fil["strings"], audit3)
    stack = m_audit.QwenTaskRoundAudit(audit3, pool, fil["strings"])
    return stack, {"claim_order": list(m_audit.QWEN_CLAIMS), "audit_v2_sha16": cfg["sha16_recomputed"],
                   "e2a_ban_list_sha256": cfg["ban_list_sha256"], "scaffold_assertion": sca,
                   "term_sha16": sc_mod.m_scaffold.TERM_SHA16,
                   "echo_set": "the banner's Note lines + 'Reasoning (one line):' (audit.qwen_echo_lines)",
                   "line_classes": list(lines.CLASSES),
                   "line_echo_set": "m:258's eight strings as rendered for the session + the headers so far "
                                    "(lines.echo_lines)"}


def tokenizer_of_record(snapshot_dir=None):
    """(tokenizers.Tokenizer, {path, sha256}) for the snapshot of record's tokenizer.json, offline."""
    from tokenizers import Tokenizer
    if snapshot_dir is None:
        snapshot_dir = rs.hub_repo_dir() / "snapshots" / QWEN_REVISION
    p = Path(snapshot_dir) / "tokenizer.json"
    data = p.read_bytes()
    return Tokenizer.from_str(data.decode("utf-8")), {"file": f"{QWEN_MODEL_ID}@{QWEN_REVISION}/tokenizer.json",
                                                      "sha256": _sha256(data)}


def inputs_of_record(*, canonical: bool, proposal_rel: str = "PROPOSAL-m-gating-campaign-v1_11.md",
                     snapshot_dir=None) -> dict:
    """Every precondition in order; GshapeRefusal / GshapeStop on the first failure, nothing scored before."""
    kp = m_keys.stream_known_answer()
    if kp:
        raise GshapeStop(f"G-SHAPE-F3 STOP: {kp}")
    pdata = (REPO / proposal_rel).read_bytes()
    if canonical:
        from . import stages
        cp, cdata = stages.committed(proposal_rel)
        if cp or cdata != pdata:
            raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: {proposal_rel} is not committed at HEAD unedited: {cp}")
    cp = criterion_problems(pdata.decode("utf-8", "replace"))
    if cp:
        raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: {proposal_rel}: {cp}")
    sp, smap = sources_map(canonical=canonical)
    clp, cmap = import_closure(canonical=canonical)
    ip = guard.import_problems(runtime=True)
    if canonical and (sp or clp):
        raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: the sources and the import closure must be committed at HEAD and "
                            f"unedited for the run of record: {(sp + clp)[:4]}")
    if ip:
        raise GshapeStop(f"G-SHAPE-F3 STOP: the licence's import set does not hold: {ip}")
    bp = banner.spec_problems(REPO / proposal_rel)
    if bp:
        raise GshapeStop(f"G-SHAPE-F3 STOP: the banners placed are not §2.5's bytes: {bp}")
    mf, mf_sha = _committed_json(MODEL_FREE_REL, canonical)
    ror = (mf or {}).get("renders_of_record") or {}
    if ror.get("renders_sha256") != RENDERS_SHA256_OF_RECORD:
        raise GshapeStop("G-SHAPE-F3 STOP: G-CAL's renders are not the renders of record")
    comp, comp_sha = _committed_json(COMPLETABILITY_REL, canonical)
    if (comp or {}).get("verdict") != "PASS" or (comp.get("identity") or {}).get("renders_sha256") != RENDERS_SHA256_OF_RECORD:
        raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: {COMPLETABILITY_REL} is not a PASS on the renders of record")
    seat = (REPO / SEAT_READ_REL).read_text(encoding="utf-8")
    cited = re.findall(r"^renders_sha256: `([0-9a-f]{64})`$", seat, flags=re.M)
    if cited != [RENDERS_SHA256_OF_RECORD]:
        raise GshapeStop("G-SHAPE-F3 STOP: the seat's read does not cite the renders of record once")
    items = ror.get("items")
    renders = [x["render"] for x in items] if isinstance(items, list) else []
    pool, computed = sc_mod.pool_and_renders()
    if renders != list(computed) or _sha256("\n".join(renders).encode("utf-8")) != RENDERS_SHA256_OF_RECORD:
        raise GshapeStop("G-SHAPE-F3 STOP: G-CAL's recorded renders are not scaffold.pool_and_renders()'s / the pin")
    flat = [g for it in pool for g in it["gold"]]
    if len(flat) != N_GOLD_VARIANTS or len(set(flat)) != N_GOLD_VARIANTS or len(pool) != N_ITEMS:
        raise GshapeStop("G-SHAPE-F3 STOP: the golds are not 16 items with 22 distinct variants")
    qs, qrec = qwen_stack(pool)
    try:
        tok, trec = tokenizer_of_record(snapshot_dir)
    except (OSError, ImportError, ValueError) as e:
        raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: Layer T's tokenizer of record is unavailable ({type(e).__name__}); "
                            f"G-SHAPE-F3 runs on the laptop (the Qwen site)") from None
    return {"proposal_rel": proposal_rel, "proposal_sha256": _sha256(pdata), "model_free_sha256": mf_sha,
            "completability_sha256": comp_sha, "seat_sha256": _sha256(seat.encode("utf-8")), "renders": renders,
            "pool": pool, "stack": qs, "stack_rec": qrec, "term_rx": sc_mod.load_term_rx(), "canonical": canonical,
            "sources_map": smap, "import_closure": cmap, "package_sha256": guard.package_sha256_of(guard.PACKAGE_DIR),
            "m_module_sha256": guard.m_module_sha256s(), "tokenizer": tok, "tokenizer_rec": trec}


# --- Layers A and C ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Placement:
    template: str
    pi: int
    mp: int
    cl: int | None
    t: int
    n: int
    i: int
    gi: int
    gold: str
    phase: str
    P: str
    Q: str
    note_lines: tuple
    seg: str
    render: str

    def key(self) -> list:
        return [self.template, self.pi, self.mp, self.cl, self.t, self.n, self.i, self.gold, self.phase]


def _banners(template: str) -> Iterator[tuple[int, int, int | None, str, str, tuple]]:
    r = schedule.roster()
    for pi in range(len(r)):
        for mp in (0, 1):
            for cl in ((0, 1) if keys.names_labels(template) else (None,)):
                P, Q = r[pi][mp], r[pi][1 - mp]
                yield pi, mp, cl, P, Q, banner.build_banner(template, P, Q, cl)[1]


def placements(renders: Sequence[str], pool) -> Iterator[Placement]:
    """Layer A's placements, in enumeration order (template; pair, map, clause; template index; item; gold;
    phase); the render under the Q-role label of a contrast template."""
    for tpl in keys.CONTRAST:
        for pi, mp, cl, P, Q, notes in _banners(tpl):
            for t, rt in enumerate(ROUND_TEMPLATES):
                for i, render in enumerate(renders):
                    for gi, g in enumerate(pool[i]["gold"]):
                        for ph in PHASES:
                            n = t + 1 + (sc_mod.N_FORCED if ph == "free" else 0)
                            yield Placement(template=tpl, pi=pi, mp=mp, cl=cl, t=t, n=n, i=i, gi=gi, gold=g, phase=ph,
                                            P=P, Q=Q, note_lines=tuple(notes), seg=rt.format(n=n, tag=Q, task=render),
                                            render=render)


def expected_n(template: str) -> int:
    return (16 if keys.names_labels(template) else 8) * len(ROUND_TEMPLATES) * N_GOLD_VARIANTS * len(PHASES)


def round_fires(ra, text: str, term_rx) -> list[str]:
    tests = (("claim", ra.claim is not None), ("advisory", bool(ra.advisory)),
             ("v3.exclusion", ra.v3 is not None and ra.v3.get("exclusion") is not None),
             ("v3.content_label", ra.v3 is not None and ra.v3.get("content_label") is not None),
             ("v3.advisory", ra.v3 is not None and bool(ra.v3.get("advisory"))), ("echo_line", ra.echo_line is not None),
             ("lexical_raw", ra.lexical_raw is not None), ("scaffold", bool(ra.scaffold)), ("degeneracy", bool(ra.degeneracy)),
             ("ends", m_audit.ends_session(ra)), ("strict", m_audit.strict_excludes(ra)),
             ("termination", sc_mod.termination(text, term_rx)))
    return [nm for nm, v in tests if v]


def score(stack, pl: Placement, text: str):
    """``text`` scored exactly as run_session_f3 calls the stack, ``earlier`` empty."""
    return stack.classify(text, render=pl.render, item=pl.i, earlier=(), own_pair=(pl.P, pl.Q),
                          echo_lines=m_audit.qwen_echo_lines(pl.note_lines), phase=pl.phase)


CONTROL_TEXTS: dict[str, Callable[[Placement], str | None]] = {
    "seg+gold": lambda pl: pl.seg + pl.gold,
    "reasoning+seg+gold": lambda pl: (banner.reasoning_block(pl.n) + pl.seg + pl.gold) if pl.phase == "free" else None,
    "render-as-response": lambda pl: pl.render,
}


def grid(ins: Mapping[str, Any], *, scorer: Callable[[Placement], str] | None = None,
         drop: Callable[[Placement], bool] | None = None) -> dict:
    scorer = (lambda pl: pl.gold) if scorer is None else scorer
    stack, term_rx = ins["stack"], ins["term_rx"]
    out: dict = {}
    for tpl in keys.CONTRAST:
        out[tpl] = {"grid": {"n": 0, "n_fired": 0, "fires": [], "n_misplaced": 0},
                    "controls": {c: {"n": 0, "n_fired": 0, "fields": set()} for c in CONTROL_TEXTS}}
    ukeys: dict[str, list] = {t: [] for t in keys.CONTRAST}
    rows: dict[str, list] = {t: [] for t in keys.CONTRAST}
    for pl in placements(ins["renders"], ins["pool"]):
        if drop is not None and drop(pl):
            continue
        g = out[pl.template]
        sl = pl.seg.split("\n")
        if (len(sl) != 3 or sl[1] != "Task: " + ins["renders"][pl.i] or sl[2] != "Response:"
                or not sl[0].startswith(f"[round {pl.n} ") or not sl[0].endswith(f": {pl.Q}]")):
            g["grid"]["n_misplaced"] += 1
        text = scorer(pl)
        f = round_fires(score(stack, pl, text), text, term_rx)
        cf = {}
        for c, fn in CONTROL_TEXTS.items():
            ct = fn(pl)
            if ct is None:
                continue
            cf[c] = round_fires(score(stack, pl, ct), ct, term_rx)
            st = g["controls"][c]
            st["n"] += 1
            if cf[c]:
                st["n_fired"] += 1
                st["fields"].update(cf[c])
        g["grid"]["n"] += 1
        if f:
            g["grid"]["n_fired"] += 1
            if len(g["grid"]["fires"]) < 50:
                g["grid"]["fires"].append({"key": pl.key(), "fields": f})
        ukeys[pl.template].append(pl.key())
        rows[pl.template].append(pl.key()[1:] + [text, f, {c: cf[c] for c in sorted(cf)}])
    for tpl in keys.CONTRAST:
        g = out[tpl]
        seen = Counter(tuple(k[1:]) for k in ukeys[tpl])
        g["grid"]["exact"] = (len(seen) == expected_n(tpl) and all(v == 1 for v in seen.values())
                              and len(ukeys[tpl]) == expected_n(tpl))
        g["grid"]["placements_sha256"] = _json_sha256(ukeys[tpl])
        g["grid"]["rows_sha256"] = _json_sha256(rows[tpl])
        for c, st in g["controls"].items():
            st["fields"] = [x for x in ROUND_FIRE_FIELDS if x in st["fields"]]
            st["required"] = c in CONTROLS_REQUIRED
    return out


# --- Layer R --------------------------------------------------------------------------------------
def line_placements(pool) -> Iterator[tuple]:
    """(template, pi, mp, cl, n, gold) over every F3 template's banners x n 5..10 x every gold variant."""
    for tpl in keys.TEMPLATES:
        for pi, mp, cl, P, Q, _notes in _banners(tpl):
            for n in banner.N_RANGE:
                for it in pool:
                    for g in it["gold"]:
                        yield tpl, pi, mp, cl, P, Q, n, g


def line_fires(text: str, P: str, Q: str, n: int, scaffold_strings) -> list[str]:
    la = lines.classify_line(text, n_tok=1, cap=sc_mod.REASONING_CAPS[0], stop_reason="newline", cap_hit=False,
                             echo_set=lines.echo_lines(P, Q, n), scaffold_strings=scaffold_strings)
    return list(la.classes) + (["scaffold"] if la.scaffold else [])


def layer_r(ins: Mapping[str, Any]) -> dict:
    ss = ins["stack"].scaffold_strings
    n = n_fired = c_n = c_fired = 0
    fires, keys_ = [], []
    for tpl, pi, mp, cl, P, Q, nn, g in line_placements(ins["pool"]):
        f = line_fires(g, P, Q, nn, ss)
        cf = line_fires(banner.reasoning_block(nn).replace("\n", " ") + g, P, Q, nn, ss)
        n += 1
        keys_.append([tpl, pi, mp, cl, nn, g])
        if f:
            n_fired += 1
            if len(fires) < 50:
                fires.append({"key": [tpl, pi, mp, cl, nn, g], "fields": f})
        c_n += 1
        c_fired += bool(cf)
    want = sum((16 if keys.names_labels(t) else 8) for t in keys.TEMPLATES) * len(banner.N_RANGE) * N_GOLD_VARIANTS
    return {"n": n, "n_fired": n_fired, "fires": fires, "exact": n == want == len({json.dumps(k) for k in keys_}),
            "placements_sha256": _json_sha256(keys_), "fire_fields": list(LINE_FIRE_FIELDS),
            # PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 11): each gold is placed as a line
            # generated to its newline, so the two structural classes cannot fire here and the layer tests the
            # content-borne fields; G-SHAPE asks whether a render's content reaches a scorer.
            "scope": "every gold placed as a line ended by the newline stop (n_tok 1): the structural classes -- "
                     "empty (the text) and cap_no_newline (the stop) -- cannot fire; the content-borne fields, echo "
                     "and scaffold, are the test; the reasoning header for every n 5..10",
            "control": {"name": "reasoning block + gold as the line", "n": c_n, "n_fired": c_fired, "required": True}}


# --- Layer S ------------------------------------------------------------------------------------
def _calls(fn, attr: str) -> list[ast.Call]:
    return [n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
            and n.func.attr == attr]


def _kw(c: ast.Call, name: str):
    return next((k.value for k in c.keywords if k.arg == name), None)


def _is(n, src: str) -> bool:
    return n is not None and ast.unparse(n) == src


def runner_scope_problems(sources: Mapping[str, str] | None = None) -> dict:
    """Layer S over mf3's runner and package (the rules in the module docstring)."""
    rel = "valence_core/mf3/runner.py"
    src = (sources or {}).get(rel) or (REPO / rel).read_text(encoding="utf-8")
    probs: list[str] = []
    tree = ast.parse(src)
    fn = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "run_session_f3"), None)
    if fn is None:
        return {"problems": ["run_session_f3 absent"], "rules": "S1-S5"}
    cls = _calls(fn, "classify")
    if len(cls) != 2:
        probs.append(f"S1: run_session_f3 calls classify {len(cls)} times (2: forced, free)")
    for c in cls:
        if len(c.args) != 1 or not _is(c.args[0], "g.text"):
            probs.append("S2: a classify call is not handed the generation's text (g.text)")
        if not (_is(_kw(c, "render"), "spec.task_text") and _is(_kw(c, "item"), "spec.item")
                and _is(_kw(c, "earlier"), "earlier") and _is(_kw(c, "own_pair"), "own")
                and _is(_kw(c, "echo_lines"), "echo_lines")):
            probs.append("S3: a classify call's render / item / earlier / own_pair / echo_lines are not the round's")
    phases = sorted(ast.literal_eval(_kw(c, "phase")) for c in cls if isinstance(_kw(c, "phase"), ast.Constant))
    if phases != ["forced", "free"]:
        probs.append(f"S3: classify phases {phases} are not forced and free")
    lc = [n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
          and n.func.attr == "classify_line"]
    if len(lc) != 1 or len(lc[0].args) != 1 or not _is(lc[0].args[0], "g.text") \
            or not _is(_kw(lc[0], "echo_set"), "lines.echo_lines(sc.P, sc.Q, rs.n)") \
            or not _is(_kw(lc[0], "cap"), "rs.cap"):
        probs.append("S4: the reasoning line is not classified once, on its generation's text, at its cap and n")
    app = _calls(fn, "append")
    earlier_apps = [a for a in app if isinstance(a.func.value, ast.Name) and a.func.value.id == "earlier"]
    if len(earlier_apps) != 2 or not all(len(a.args) == 1 and _is(a.args[0], "g.text") for a in earlier_apps):
        probs.append("S5: earlier is appended other than with the two task rounds' texts")
    # every earlier.append follows a classify of a task round (never the line's): the statement order
    body_src = ast.unparse(fn)
    if body_src.count("earlier.append(g.text)") != 2 or "earlier.append" in body_src.split("la = lines.classify_line")[1].split("menu = sc.menu")[0]:
        probs.append("S5: a reasoning line reaches earlier")
    # S6: no classify / classify_line reference outside the runner's session function, the verifier, this
    # module and self-test bodies
    for p in sorted(guard.PACKAGE_DIR.glob("*.py")):
        r = p.relative_to(REPO).as_posix()
        if r in ("valence_core/mf3/gshape.py", "valence_core/mf3/testing.py"):
            continue
        t = ast.parse((sources or {}).get(r) or p.read_text(encoding="utf-8"))
        allowed = set()
        for n in ast.walk(t):
            if isinstance(n, ast.FunctionDef) and (n.name == "_selftest" or (r == rel and n.name == "run_session_f3")
                                                   or (r == "valence_core/mf3/verify.py" and n.name == "_verify")
                                                   or (r == "valence_core/mf3/lines.py" and n.name == "classify_line")):
                allowed |= {id(x) for x in ast.walk(n)}
        for n in ast.walk(t):
            if isinstance(n, ast.Attribute) and n.attr in ("classify", "classify_line") and id(n) not in allowed:
                probs.append(f"S6: {r}:{n.lineno}: a {n.attr} reference outside the runner, the verifier and self-tests")
    return {"problems": probs, "rules": "S1 two classify calls; S2 the generation's text; S3 the round's render, item, "
                                        "earlier, own pair, echo set and phase; S4 one classify_line on the line's "
                                        "text at its cap and n; S5 earlier gets task-round texts only; S6 scope"}


# --- Layer T --------------------------------------------------------------------------------------
def _tok_boundary(tok, prefix: str, seg: str) -> dict:
    p = tok.encode(prefix, add_special_tokens=False)
    f = tok.encode(prefix + seg, add_special_tokens=False)
    k = 0
    while k < len(p.ids) and k < len(f.ids) and p.ids[k] == f.ids[k]:
        k += 1
    starts = [o[0] for o in f.offsets]
    by_offset = next((i for i, s0 in enumerate(starts) if s0 >= len(prefix)), len(starts))
    straddle = any(o[0] < len(prefix) < o[1] for o in f.offsets)
    decoded = tok.decode(f.ids[:len(p.ids)], skip_special_tokens=False)
    return {"token": k == len(p.ids), "offset": by_offset == len(p.ids) and not straddle,
            "decode": decoded == unicodedata.normalize("NFC", prefix)}


def layer_t(ins: Mapping[str, Any]) -> dict:
    """Every F3 generation join on the tokenizer of record, across templates, starts and line texts."""
    tok = ins["tokenizer"]
    pool, renders = ins["pool"], ins["renders"]
    golds = [it["gold"][0] for it in pool]
    n = 0
    bad: list[dict] = []
    for tpl in keys.TEMPLATES:
        for pi, mp, cl, P, Q, notes in _banners(tpl):
            if (pi, mp) not in ((0, 0), (3, 1)):
                continue
            ban = SESSION_BANNER + "".join(x + "\n" for x in notes)
            for start in (0, 1):
                order = ("P", "P", "Q", "Q") if start == 0 else ("Q", "Q", "P", "P")
                tr = ban
                for ri, role in enumerate(order):
                    lab = P if role == "P" else Q
                    task = renders[ri] if (role == "Q" and keys.is_contrast(tpl)) else pool[ri]["task"]
                    tr += ROUND_TEMPLATES[ri].format(n=ri + 1, tag=lab, task=task) + golds[ri] + "\n"
                for li, line in enumerate(LAYER_T_LINES):
                    nn = 5 + (li % 6)
                    joins = []
                    rb = banner.reasoning_block(nn)
                    joins.append(("reasoning block after the forced rounds", tr, rb))
                    after = tr + rb + line + "\n" + MENU_TEMPLATES[li % 4].format(n=nn, a=P, b=Q) + f" {P}\n"
                    seg = ROUND_TEMPLATES[li % 4].format(n=nn, tag=P, task=pool[4]["task"])
                    joins.append(("chosen round after the line", after, seg))
                    if nn < 10:
                        joins.append(("next reasoning block", after + seg + golds[4] + "\n", banner.reasoning_block(nn + 1)))
                    for what, pre, sg in joins:
                        r = _tok_boundary(tok, pre, sg)
                        n += 1
                        if not all(r.values()):
                            bad.append({"template": tpl, "start": start, "line": line, "join": what, **r})
    return {"n": n, "n_failed": len(bad), "failed": bad[:20], "lines": list(LAYER_T_LINES),
            "tokenizer": ins["tokenizer_rec"],
            "forms": "token comparison == prefix token count; the tokenizer's character offsets put the first segment "
                     "token at the prefix token count with no token straddling the boundary; decode(first k tokens) == "
                     "NFC(prefix) (the runtime form)"}


# --- the verdict and the artifact --------------------------------------------------------------------
def evaluate(*, canonical: bool = False, inputs: Mapping[str, Any] | None = None,
             scorer: Callable[[Placement], str] | None = None, drop: Callable[[Placement], bool] | None = None,
             sources: Mapping[str, str] | None = None) -> dict:
    ins = inputs_of_record(canonical=canonical) if inputs is None else inputs
    g = grid(ins, scorer=scorer, drop=drop)
    lr = layer_r(ins)
    ls = runner_scope_problems(sources)
    lt = layer_t(ins)
    reasons = []
    for tpl in keys.CONTRAST:
        gg = g[tpl]["grid"]
        if gg["n_fired"]:
            reasons.append(f"fire:{tpl}")
        if not gg["exact"] or gg["n_misplaced"]:
            reasons.append(f"coverage:{tpl}")
        for c, st in g[tpl]["controls"].items():
            if c in CONTROLS_REQUIRED and st["n_fired"] != st["n"]:
                reasons.append(f"control-silent:{tpl}:{c}")
    if lr["n_fired"]:
        reasons.append("fire:reasoning-line")
    if not lr["exact"]:
        reasons.append("coverage:reasoning-line")
    if lr["control"]["n_fired"] != lr["control"]["n"]:
        reasons.append("control-silent:reasoning-line")
    if ls["problems"]:
        reasons.append("scope-static")
    if lt["n_failed"] or not lt["n"]:
        reasons.append("boundary")
    pool, renders = ins["pool"], ins["renders"]
    prov = {"package_sha256": ins["package_sha256"], "m_module_sha256": ins["m_module_sha256"],
            "sources": ins["sources_map"], "sources_digest": _json_sha256(ins["sources_map"]),
            "import_closure": dict(sorted(ins["import_closure"].items())),
            "import_closure_digest": _json_sha256(dict(sorted(ins["import_closure"].items()))),
            "proposal_file": ins["proposal_rel"], "proposal_sha256": ins["proposal_sha256"],
            "committed_at_head": bool(ins["canonical"])}
    art = {"schema": SCHEMA, "stage": STAGE, "spec": SPEC_REF, "criterion": CRITERION, "criterion_f0": CRITERION_F0,
           "inputs": {"renders_sha256": RENDERS_SHA256_OF_RECORD, "n_renders": len(renders),
                      "gcal_model_free": {"path": MODEL_FREE_REL, "sha256": ins["model_free_sha256"]},
                      "gcal_completability": {"path": COMPLETABILITY_REL, "sha256": ins["completability_sha256"]},
                      "seat_read": {"path": SEAT_READ_REL, "sha256": ins["seat_sha256"]},
                      "pool_sha16": rs.pool_sha16(pool),
                      "golds": {"n_items": len(pool), "n_variants": sum(len(it["gold"]) for it in pool)},
                      "round_templates_sha256": _json_sha256(list(ROUND_TEMPLATES)),
                      "banners_sha256": _json_sha256({t: [list(x[5]) for x in _banners(t)] for t in keys.TEMPLATES}),
                      "reasoning_block_sha256": _json_sha256([banner.reasoning_block(n) for n in banner.N_RANGE])},
           "stack": ins["stack_rec"],
           "fire_predicate": {"round": list(ROUND_FIRE_FIELDS), "line": list(LINE_FIRE_FIELDS),
                              "rule": "a placement fires iff any field fires; any fire is a STOP"},
           "layer_a": {t: g[t]["grid"] for t in keys.CONTRAST},
           "layer_a_total": sum(g[t]["grid"]["n"] for t in keys.CONTRAST),
           "layer_c": {t: g[t]["controls"] for t in keys.CONTRAST},
           "layer_r": lr, "layer_s": ls, "layer_t": lt,
           "runner_dynamic_evidence": {"where": "the mf3 self-test (scripts/mf3_sessions.py --selftest)",
                                       "checks": list(RUNNER_DYNAMIC_EVIDENCE)},
           "verdict": "PASS" if not reasons else "STOP", "stop_reasons": reasons, "provenance": prov}
    rs.json_text(art)
    return art


def _write_once_text(path: Path, text: str) -> str:
    """'written' or 'identical'; a different file (or a link) is refused, never overwritten (G-SHAPE-F0's PIN-S9,
    carried: supersession is a hand git mv on the seat's ruling)."""
    p = Path(path)
    if p.exists() or p.is_symlink():
        same = p.is_file() and not p.is_symlink() and p.read_text(encoding="utf-8") == text
        if not same:
            raise GshapeRefusal(f"G-SHAPE-F3 ARTIFACT EXISTS at {p} with different bytes -- never overwritten")
        return "identical"
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    if tmp.is_symlink():
        raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: {tmp} is a link")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o666)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, p)
    return "written"


def write(out_dir=None, **seams) -> dict:
    """G-SHAPE-F3: evaluate and write the artifact once; with no ``out_dir`` the canonical
    data/mf3/gates/G-SHAPE-F3.json, every input committed at HEAD and unedited."""
    unknown = sorted(set(seams) - {"inputs", "scorer", "drop", "sources"})
    if unknown:
        raise TypeError(f"write: unknown seam(s) {unknown}")
    seams = {k: v for k, v in seams.items() if v is not None}
    if out_dir is None:
        if seams:
            raise GshapeRefusal("G-SHAPE-F3 REFUSED: a seamed run never writes the canonical artifact")
        d, canonical = guard.GATES_DIR, True
    else:
        if str(out_dir).strip() == "":
            raise GshapeRefusal("G-SHAPE-F3 REFUSED: an empty --out")
        try:
            d = rs.refuse_canonical_out(out_dir)
        except SystemExit as e:
            raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: {e}") from None
        canonical = False
    path = Path(d) / ARTIFACT_NAME
    ins = seams.pop("inputs", None) or inputs_of_record(canonical=canonical)
    art = evaluate(canonical=canonical, inputs=ins, **seams)
    text = rs.json_text(art, indent=1)
    if canonical:
        sp, smap = sources_map(canonical=True)
        if sp or smap != ins["sources_map"] or guard.package_sha256_of(guard.PACKAGE_DIR) != ins["package_sha256"]:
            raise GshapeRefusal(f"G-SHAPE-F3 REFUSED: the sources drifted between the precondition and the write {sp[:3]}")
    return {"artifact": art, "path": path, "how": _write_once_text(path, text), "canonical": canonical}


def summary_lines(res: Mapping[str, Any]) -> list[str]:
    a = res["artifact"]
    out = [f"G-SHAPE-F3 inputs: renders sha256 {a['inputs']['renders_sha256']}; proposal sha256 "
           f"{a['provenance']['proposal_sha256']}; mf3 package sha256 {a['provenance']['package_sha256']}; sources digest "
           f"{a['provenance']['sources_digest']} ({len(a['provenance']['sources'])} files); committed at HEAD: "
           f"{a['provenance']['committed_at_head']}"]
    for t in keys.CONTRAST:
        g, c = a["layer_a"][t], a["layer_c"][t]
        out.append(f"G-SHAPE-F3 Layer A {t}: {g['n']} placements, {g['n_fired']} fired, coverage exact {g['exact']}; "
                   + "; ".join(f"{k} {v['n_fired']}/{v['n']}" for k, v in sorted(c.items())))
    r = a["layer_r"]
    out.append(f"G-SHAPE-F3 Layer R: {r['n']} line placements, {r['n_fired']} fired, coverage exact {r['exact']}; control "
               f"{r['control']['n_fired']}/{r['control']['n']}")
    out.append(f"G-SHAPE-F3 Layer S: {len(a['layer_s']['problems'])} problems; Layer T: {a['layer_t']['n']} joins, "
               f"{a['layer_t']['n_failed']} failed (tokenizer sha256 {a['layer_t']['tokenizer']['sha256'][:16]})")
    out.append(f"G-SHAPE-F3 {a['verdict']}" + (f" {a['stop_reasons']}" if a["stop_reasons"] else "") + f" {res['path']} ({res['how']})")
    return out


def _selftest(chk) -> None:
    import tempfile

    ins = inputs_of_record(canonical=False)
    art = evaluate(inputs=ins)
    chk("mf3.gshape: G-SHAPE-F3 on the working tree -- PASS: Layer A 5,632 placements (A1 2,816; A2 and A3 1,408) none "
        "fired, coverage exact; seg+gold and reasoning+seg+gold fire 100%; Layer R none fired, its control 100%; Layer S "
        "clean; Layer T every join holds on the tokenizer of record",
        art["verdict"] == "PASS" and art["layer_a_total"] == 5632
        and [art["layer_a"][t]["n"] for t in keys.CONTRAST] == [2816, 1408, 1408]
        and all(art["layer_c"][t]["reasoning+seg+gold"]["n"] == art["layer_a"][t]["n"] // 2 for t in keys.CONTRAST)
        and art["layer_r"]["n"] == 64 * 6 * 22 and art["layer_t"]["n"] > 0, art["stop_reasons"])
    seams = {"a fired placement": dict(scorer=lambda pl: pl.seg + pl.gold),
             "a dropped placement": dict(drop=lambda pl: pl.i == 3 and pl.template == "A2"),
             "a runner scoring the segment": dict(sources={"valence_core/mf3/runner.py": (
                 REPO / "valence_core/mf3/runner.py").read_text().replace(
                 "ra = audit.classify(g.text, render=spec.task_text", "ra = audit.classify(spec.seg + g.text, render=spec.task_text", 1)}),
             "a line entering earlier": dict(sources={"valence_core/mf3/runner.py": (
                 REPO / "valence_core/mf3/runner.py").read_text().replace(
                 "            log.add_reasoning(rs, g, la)\n", "            log.add_reasoning(rs, g, la)\n            earlier.append(g.text)\n", 1)})}
    got = {k: evaluate(inputs=ins, **v)["verdict"] for k, v in seams.items()}
    chk("mf3.gshape: STOPs on a fired placement, a coverage gap, a runner scoring its segment, and a reasoning line "
        "reaching earlier", all(v == "STOP" for v in got.values()), got)

    class Merging:
        def __init__(self, t):
            self.t = t

        def encode(self, text, add_special_tokens=False):
            e = self.t.encode(text, add_special_tokens=False)
            if not (text.endswith("Response:") or text.endswith("Reasoning (one line):\n")):
                return e

            class E:
                ids = [999] + list(e.ids[1:])
                offsets = e.offsets
            return E()

        def decode(self, ids, skip_special_tokens=False):
            return self.t.decode(ids, skip_special_tokens=skip_special_tokens)
    lt = layer_t({**ins, "tokenizer": Merging(ins["tokenizer"])})
    chk("mf3.gshape: Layer T fires on a tokenizer whose joint encode collapses the boundary", lt["n_failed"] == lt["n"] > 0,
        lt["n_failed"])
    with tempfile.TemporaryDirectory() as td:
        r1 = write(td, inputs=ins)
        r2 = write(td, inputs=ins)
        (Path(td) / ARTIFACT_NAME).write_text("{}")
        try:
            write(td, inputs=ins)
            over = False
        except GshapeRefusal:
            over = True
        try:
            write(None, inputs=ins)
            canon = False
        except GshapeRefusal:
            canon = True
    chk("mf3.gshape: the artifact is write-once (identical accepted, different refused); a seamed run never writes "
        "the canonical path", r1["how"] == "written" and r2["how"] == "identical" and over and canon)
    with tempfile.TemporaryDirectory() as td:
        try:
            tokenizer_of_record(td)
            ok = False
        except OSError:
            ok = True
    chk("mf3.gshape: the tokenizer of record is read from the snapshot of record only (an absent file refuses)", ok)
    names = set()
    for n in ast.walk(ast.parse((REPO / "valence_core/mf3/runner.py").read_text(encoding="utf-8"))):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "chk" and n.args:
            a = n.args[0]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                names.add(a.value)
            elif isinstance(a, ast.JoinedStr):
                names.add("".join(v.value if isinstance(v, ast.Constant) else "{}" for v in a.values))
    chk("mf3.gshape: Layer S's dynamic evidence names runner self-test checks that exist (by their chk names)",
        all(any(nm.startswith(c) for nm in names) for c in RUNNER_DYNAMIC_EVIDENCE),
        [c[:40] for c in RUNNER_DYNAMIC_EVIDENCE if not any(nm.startswith(c) for nm in names)])
