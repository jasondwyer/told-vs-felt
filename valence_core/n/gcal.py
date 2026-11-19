"""PROPOSAL-n -- G-CAL-n (n v0.2 §8 step 8; the G-CAL-n paragraph of n §3; ADDENDUM-n1 §1.1, §1.2 (v), §1.4): the
dose map and BK's two hurdles, built on Code's readings GC1-GC23 as the coordinating session routed them (PINs declared
in the BUILD entry; GC3, GC4, GC5, GC6, GC8, GC11, GC12 and GC23 go to the seat before the run, with G-VEC's G1, G3,
G6 and G9).

THE STAGE, n:113 verbatim: "d_eq and d_20 computed from R_ℓ and R and pinned. BK's two hurdles on one batch per pole
per dose, in BK's order: 48 conditioning turns generated under steering at +ρ, −ρ and +ρ/2 (TEMP 0.7, their prompt;
≤ 80 tokens), the coherence heuristic verbatim — length collapse (fewer than four words), repetition loops (more than
50% of trigrams repeated), low lexical diversity (fewer than five distinct words per 20 words) — pass iff ≥ 75% coherent
at every dose; then the arrival hurdle on the same turns — each re-encoded unsteered, projected on v, the shift against
48 unsteered baseline turns with |t| ≥ 2 in the pole's direction; a fail at ±ρ → STOP (ρ is BK's; a failure on our
implementation is a port defect until shown otherwise); the seat reads every turn (rule 25); nothing here carries a
pick."

THE RENDERING (GC5, GC6): ``prompt_parts`` is the one place a prompt's two texts live, the user turn and the generation
prompt, in the rendering of record (sessions.py's OLMo-2 chat form: no system turn, the generation prompt, no special
token added), under n §0.7's rule-13 departure as GC6 reads it. It has three callers: the (v) render (``ids.render_v``,
on the laptop), which encodes the texts and records their sha256s and the template; the box's prompts check, which
re-derives those from it; and ``CONVENTIONS``. The box reads the rendered ids. Rule 13 makes the stop and the bans part
of the template family, and the stop is wired apart from the texts, in three places: the (v) render encodes the end of
turn (``ids.EOT``) to the v block's ``eos_id``; the driver asserts the tokenizer's eos equal to it at the load; and
``generate`` stops on it. GC7 sets no ban. A ruling against the chat form changes ``prompt_parts`` and re-renders (v),
and re-opens the stop and GC7's bans with it, as the seat block's GC6 says.

THE PROMPTS (GC5): 48, BK's zone prompt (sessions.USER_PROMPT, n:77) over the 12 labels of record (the (iii) file's
labels, sorted) x 4: prompt i has label i mod 12 and replicate i // 12, and the same prompt and seed in all four
batches. Each is a single opening user turn and the generation prompt.

THE GENERATION (GC7-GC10, GC13): per turn, an ids-in loop, one uncached forward per step (GC9; rule 2's annotation: a
first-token kernel gate licenses no generation); the next token drawn at TEMP 0.7 (GC4) from the softmax of the last
position's logits by an inverse-CDF draw from the turn's numpy generator, seeded by seed_i (``keys.gcal_seed``, GC10);
a stop at the end-of-turn token (the tokenizer's eos, ``<|endoftext|>``, the rendering's assistant end) or at 80 new
tokens (GC3); no newline stop, no ban set (GC7); the emitted ids exclude the stop token. A steered batch adds
ṽ(d) = d·ρ·R·v at the site from the generation prompt's first token onward (GC8): ``Injection.at_frac`` on the valence
row of record at the site, R from gvec.json's ``of_record``, ``expect_sha`` its sha16, then ``with_sign`` (runner's
``_injection`` arithmetic). The batches, in n:113's order: +ρ (d = +1), −ρ (d = −1), +ρ/2 (d = +1/2), and the 48
unsteered baseline turns on the same prompts and seeds (GC13). They are generated in ``GENERATION_ORDER`` (GC23 (d)):
+ρ, +ρ/2, the baseline, then −ρ, so that a failure in another batch spends no −ρ turn. The record and the turns file
keep n:113's order, and each turn's seed fixes its draws, so the order changes no turn's inputs; a ruling against (d)
changes that one line. Before each batch at a positive dose (+ρ, +ρ/2; the
smoke's +ρ), ``steering_check`` takes the first prompt's first-step logits steered and unsteered, and the stage refuses
before that batch's first turn unless they differ: the injection must reach the forward. No −ρ forward is spent on it.
The generation window (rule 28(d)(c)), declared apart from the choice-read window (``schema.MAX_WINDOW``, GA-4), is
``GENERATION_WINDOW`` positions. A turn's longest forward is its prompt's ids and ``cap`` − 1 emitted ids
(``longest_forward``), and the driver refuses, before the load, a prompt whose longest forward exceeds the window. The
ids go in as ids and nothing is encoded, so nothing truncates.

THE HURDLES (GC11, GC12, GC14). Coherence, on the box's decode of the emitted ids (G-VER's decode): words are
whitespace-split, outer punctuation (Unicode category P*) stripped, lower-cased, empties dropped; length collapse is
fewer than 4 words; a repetition loop is a fraction of word trigrams that repeat an earlier trigram, 1 - distinct/total,
above 0.5 (no trigram: 0); low lexical diversity is distinct/total words below 5/20, as a ratio, also under 20 words; a
turn is coherent iff none fires; a batch passes iff at least 36 of 48 are. Arrival: each turn's emitted ids alone,
forwarded unsteered, captured at the site; the turn's score is the mean over its positions of the projection on the
unit valence row; a batch passes iff Welch's t of its scores against the baseline's has |t| >= 2 with the pole's sign
(positive at +ρ and +ρ/2, negative at −ρ). Both hurdles are computed at every dose whatever the other gave. Status:
STOP if either fails at +ρ or −ρ (n:113); PAUSE, for the seat, if only +ρ/2 fails (GC14); PASS otherwise. Each batch's
figures also carry the shift n:113 names, descriptive: its scores' mean and SD (ddof 1), the baseline's, and the
difference of the means; and its stops: eos, cap and empty turns (rule 23). The −ρ exposure counts the turns, the
emitted tokens and the draws (the emitted tokens and each drawn end of turn).

THE DOSE MAP (GC16): R and R_ℓ from gvec.json's ``of_record``, ρ = schema.RHO; d_eq and d_20 by exactly the schema's
and the analyzer's expressions; the points by ``schema.dose_points`` (a fold into 0 is refused there, the seat's). It
depends on G-VEC alone, so the driver computes it before the load; the record says it is pinnable only on a PASS.

THE OUTPUTS (GC15): ``gcal.json`` (the record), ``gcal_turns.jsonl`` (one line per turn) and ``dose_map.json`` (the
five floats in ``ganl --dose-map``'s form), written staged and renamed into data/n/gcal/ by the driver, on every end.
GC23 (a)-(c) keep G-CAL-n one shot (GC19) and stop a failure from destroying turns that rule 25 and §0.4's count need:
each turn is appended to the staging folder's log (``OUT_PARTIAL``, by ``append_turn``: one JSON line, flushed and
fsynced) as soon as it is generated, and the log is removed only on a clean end, once the three outputs are written.
On any failure after the staging folder is made, the driver renames that folder to the failed-run folder
(data/n/.gcal.failed) and never removes it, and a later run refuses while it exists. A non-finite arrival score stays a
failure (a raise), its turns kept by the same rename.

Departures from GC1-GC22's words, declared: (1) GC12's Welch's t is recorded as None, and the batch's arrival as a
fail, when it is undefined (fewer than two scores on a side, or both sides at zero variance); (2) a turn with no
emitted id (the end of turn drawn first) has no arrival score and is left out of the t, its count recorded; (3) GC11's
"outer punctuation" is read as the Unicode punctuation categories (P*); (4) GC2's "the record alone": a STOP, like a
PAUSE, writes the record, the turns and the dose map, so that the seat reads every turn (rule 25); (5) GC9's "mirrors
the adapter's (softmax at TEMP, multinomial)": the draw is ``sample``'s inverse CDF in float64 from the turn's numpy
generator, reproducible from the logits and the seed alone; (6) GC15's stdout order: the dose map is printed before the
load, since it depends on G-VEC alone; (7) GC19's smoke of 2 prompts: ``--smoke`` takes 1 to 4, and the launch passes
2; (8) GC21's "testing.CausalDouble gains a seeded numpy sampler": the double gains none, and the self-test draws from
its logits with ``sample`` itself, the production sampler.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import unicodedata
from pathlib import Path
from typing import Callable, Mapping, Sequence

import numpy as np

from ..adapters.base import Injection, PositionSpec, sha16_arr
from . import keys, schema
from .sessions import ASSISTANT_OPEN, USER_OPEN, USER_PROMPT

STAGE = "G-CAL-n"
RECORD_SCHEMA = "n-gcal-v1"
N_LABELS, N_REPS = 12, 4
N_TURNS = N_LABELS * N_REPS                     # 48, n:113
TEMP = 0.7                                      # GC4
CAP = 80                                        # GC3
#: n:113's batches, in its order: name -> d (BK's scale, the dose ṽ(d) = d·ρ·R·v); the baseline is unsteered.
BATCHES = (("+rho", 1.0), ("-rho", -1.0), ("+rho/2", 0.5), ("baseline", 0.0))
STEERED = ("+rho", "-rho", "+rho/2")
STOP_BATCHES = ("+rho", "-rho")                 # n:113: "a fail at ±ρ → STOP"
PAUSE_BATCHES = ("+rho/2",)                     # GC14
SMOKE_BATCHES = (("+rho", 1.0), ("baseline", 0.0))   # GC19: never −ρ
COHERENT_MIN = 36                               # 75% of 48
T_BAR = 2.0
MIN_WORDS = 4
TRIGRAM_REPEAT_MAX = 0.5
DIVERSITY_MIN = 5 / 20
#: rule 28(d)(c): the generation window, declared apart from the choice-read window (schema.MAX_WINDOW, GA-4). Every
#: forward a turn makes fits it; ids go in as ids, nothing is encoded, and nothing truncates.
GENERATION_WINDOW = 4096
OUT_RECORD, OUT_TURNS, OUT_DOSE_MAP = "gcal.json", "gcal_turns.jsonl", "dose_map.json"
OUT_PARTIAL = "gcal_turns.partial.jsonl"        # GC23 (a): the staging folder's log of the turns as generated
DOSE_MAP_KEYS = ("d_eq", "d_20", "rho", "R", "R_ell")     # ganl --dose-map's five figures
#: GC23 (d): the order of generation, −ρ last; the record and the turns file keep n:113's (BATCHES). A ruling against
#: (d) sets this one line back to n:113's order, ("+rho", "-rho", "+rho/2", "baseline").
GENERATION_ORDER = ("+rho", "+rho/2", "baseline", "-rho")


def prompt_parts(zone: str) -> tuple[str, str]:
    """GC5 and GC6, the one place a prompt's two texts live: (the user turn, the generation prompt)."""
    return USER_OPEN + USER_PROMPT.format(zone=zone) + "\n", ASSISTANT_OPEN


_TEMPLATE_USER, _TEMPLATE_GEN = prompt_parts("{zone}")      # the (v) render's prompt_template, derived the same way
CONVENTIONS = {
    "rendering": f"gcal.prompt_parts, the rendering of record: the user turn {json.dumps(_TEMPLATE_USER)} and the "
                 f"generation prompt {json.dumps(_TEMPLATE_GEN)}; no system turn; no special token added; the stop the "
                 f"(v) render's eos_id (GC5, GC6, GC7)",
    "prompts": f"BK's zone prompt {json.dumps(USER_PROMPT)} over the 12 labels of record x 4; prompt i: label i mod "
               f"12, replicate i // 12; the same prompt and seed in every batch (GC5, GC13)",
    "generation": f"ids-in, uncached, one forward per step; TEMP 0.7; inverse-CDF draw from the turn's numpy "
                  f"generator seeded by keys.gcal_seed(i); stop at the eos or 80 new tokens; no newline stop, no ban "
                  f"set; emitted ids exclude the stop token; a steering check before each batch at a positive dose; "
                  f"the generation window {GENERATION_WINDOW}; the batches generated in the order "
                  f"{', '.join(GENERATION_ORDER)} (GC3, GC4, GC7, GC9, GC10, GC23 (d))",
    "persistence": "each turn appended to the staging folder's log as it is generated, the log removed on a clean end; "
                   "on a failure the staging folder kept as the failed-run folder, never removed (GC23 (a)-(c))",
    "steering": "d·ρ·R·v at the site from the generation prompt's first token onward (GC8)",
    "coherence": "on the box's decode; words whitespace-split, outer P* stripped, lower-cased; length collapse < 4 "
                 "words; repetition loop 1 - distinct/total trigrams > 0.5; low diversity distinct/total words < 5/20; "
                 "a batch passes at >= 36 of 48 (GC11)",
    "arrival": "the emitted ids alone, unsteered, at the site; the mean projection on the unit valence row; Welch's t "
               "against the baseline, |t| >= 2 with the pole's sign, at every dose; the shift beside it, descriptive "
               "(GC12)",
    "status": "STOP if either hurdle fails at +rho or -rho; PAUSE if only +rho/2 fails; PASS otherwise (GC14)",
}


def plan(labels: Sequence[str]) -> list[dict]:
    """The 48 prompts: index, label (label i mod 12 of the sorted labels), replicate i // 12, seed_i."""
    labs = sorted(str(x) for x in labels)
    if len(labs) != N_LABELS or len(set(labs)) != N_LABELS:
        raise ValueError(f"{len(labs)} labels, not {N_LABELS} distinct")
    return [{"index": i, "label": labs[i % N_LABELS], "rep": i // N_LABELS, "seed": keys.gcal_seed(i)}
            for i in range(N_TURNS)]


def sample(logits, temp: float, rng: np.random.Generator) -> int:
    """One draw from softmax(logits / temp), by the inverse CDF of one ``rng.random()`` (float64 throughout)."""
    z = np.asarray(logits, dtype=np.float64) / float(temp)
    if z.ndim != 1 or not np.all(np.isfinite(z)):
        raise ValueError("the logits are not one finite row")
    c = np.cumsum(np.exp(z - z.max()))
    return int(min(int(np.searchsorted(c, rng.random() * c[-1], side="right")), len(c) - 1))


def placed(injection: Injection | None, gen_start: int) -> tuple:
    """GC8: the injection placed from ``gen_start`` onward, as every steered step places it; () unsteered."""
    return () if injection is None else (injection.with_positions(PositionSpec.from_index(int(gen_start))),)


def longest_forward(max_seq_len: int, cap: int = CAP) -> int:
    """A turn's longest forward (rule 28(d)): its prompt's ids and ``cap`` − 1 emitted ids, the last step's input."""
    return int(max_seq_len) + int(cap) - 1


def generate(step_logits: Callable, prompt_ids: Sequence[int], gen_start: int, injection: Injection | None,
             seed: int, *, eos_id: int, temp: float = TEMP, cap: int = CAP) -> dict:
    """One turn: ``step_logits(ids, injections) -> the last position's logits``, one call per step over the whole
    sequence so far (uncached); the injection, if any, placed from ``gen_start`` onward. Returns the emitted ids (the
    stop token excluded), their count, the stop ("eos" or "cap") and whether the cap was hit."""
    ids = [int(x) for x in prompt_ids]
    if not 0 < int(gen_start) < len(ids):
        raise ValueError(f"gen_start {gen_start} is not inside the prompt's {len(ids)} ids")
    inj = placed(injection, gen_start)
    rng = np.random.default_rng(int(seed))
    out: list[int] = []
    stop = "cap"
    for _ in range(int(cap)):
        tok = sample(step_logits(ids, inj), temp, rng)
        if tok == int(eos_id):
            stop = "eos"
            break
        out.append(tok)
        ids.append(tok)
    return {"ids": out, "n_tok": len(out), "stop": stop, "cap_hit": stop == "cap"}


def steering_check(step_logits: Callable, rec: Mapping, injection: Injection) -> float:
    """``rec``'s prompt's first-step logits, steered (placed from its gen_start) and unsteered: their largest absolute
    difference, which must be finite and above 0, else ValueError before the batch's first turn (the injection must
    reach the forward)."""
    ids = [int(x) for x in rec["ids"]]
    a = np.asarray(step_logits(ids, placed(injection, rec["gen_start"])), dtype=np.float64)
    b = np.asarray(step_logits(ids, ()), dtype=np.float64)
    dev = float(np.max(np.abs(a - b))) if a.shape == b.shape and a.size else float("nan")
    if not (math.isfinite(dev) and dev > 0.0):
        raise ValueError("the steered first-step logits are the unsteered ones: the injection does not reach the "
                         "forward")
    return dev


def _strip_punct(w: str) -> str:
    a, b = 0, len(w)
    while a < b and unicodedata.category(w[a]).startswith("P"):
        a += 1
    while b > a and unicodedata.category(w[b - 1]).startswith("P"):
        b -= 1
    return w[a:b]


def words(text: str) -> list[str]:
    """GC11's words: whitespace-split, outer punctuation stripped, lower-cased, empties dropped."""
    out = []
    for w in str(text).split():
        s = _strip_punct(w).lower()
        if s:
            out.append(s)
    return out


def coherence(text: str) -> dict:
    """GC11's three tests on one turn's decode, and whether the turn is coherent (none fires)."""
    w = words(text)
    n = len(w)
    tri = [tuple(w[i:i + 3]) for i in range(n - 2)]
    rep = (1.0 - len(set(tri)) / len(tri)) if tri else 0.0
    div = (len(set(w)) / n) if n else 0.0
    f = {"n_words": n, "trigram_repeat": rep, "diversity": div, "length_collapse": n < MIN_WORDS,
         "repetition_loop": rep > TRIGRAM_REPEAT_MAX, "low_diversity": div < DIVERSITY_MIN}
    f["coherent"] = not (f["length_collapse"] or f["repetition_loop"] or f["low_diversity"])
    return f


def welch_t(a: Sequence[float], b: Sequence[float]) -> float | None:
    """Welch's t of a's mean against b's, or None when it is undefined (fewer than two on a side, or both sides at zero
    variance): the declared departure (1)."""
    x, y = np.asarray(a, dtype=np.float64), np.asarray(b, dtype=np.float64)
    if len(x) < 2 or len(y) < 2:
        return None
    se = math.sqrt(float(x.var(ddof=1)) / len(x) + float(y.var(ddof=1)) / len(y))
    if se == 0.0 or not math.isfinite(se):
        return None
    return float((x.mean() - y.mean()) / se)


def arrival_score(forward_capture: Callable, ids: Sequence[int], site: int, v_unit) -> float | None:
    """A turn's score: its emitted ids alone, forwarded unsteered, captured at the site (``forward_capture(ids,
    layers) -> {layer: [S, D]}``), the mean over its positions of the projection on ``v_unit``; None for a turn with no
    emitted id (the declared departure (2))."""
    if not ids:
        return None
    h = np.asarray(forward_capture([int(x) for x in ids], (int(site),))[int(site)], dtype=np.float64)
    if h.ndim != 2 or h.shape[0] != len(ids):
        raise ValueError("the capture is not one row per emitted id")
    s = float(np.mean(h @ np.asarray(v_unit, dtype=np.float64)))
    if not math.isfinite(s):
        raise ValueError("a non-finite arrival score")
    return s


def moments(xs: Sequence[float]) -> tuple:
    """The mean (None when empty) and the SD with ddof 1 (None under two) of ``xs``, in float64."""
    x = np.asarray(xs, dtype=np.float64)
    return (float(x.mean()) if len(x) else None), (float(x.std(ddof=1)) if len(x) >= 2 else None)


def stops(turns: Sequence[Mapping]) -> dict:
    """A batch's stops (rule 23, descriptive): its turns ended at the eos, at the cap, and with no emitted id."""
    return {"eos": sum(1 for r in turns if r["stop"] == "eos"), "cap": sum(1 for r in turns if r["stop"] == "cap"),
            "empty": sum(1 for r in turns if int(r["n_tok"]) == 0)}


def batch_figures(turns: Sequence[Mapping], baseline_scores: Sequence[float], sign: int) -> dict:
    """A steered batch's two hurdles: its coherent count and pass, and its arrival t and pass, with the shift beside the
    t (descriptive: each side's mean and SD, and the difference of the means)."""
    k = sum(1 for r in turns if r["coherence"]["coherent"])
    sc = [float(r["arrival"]) for r in turns if r["arrival"] is not None]
    t = welch_t(sc, baseline_scores)
    ok = t is not None and ((t >= T_BAR) if sign > 0 else (t <= -T_BAR))
    m, s = moments(sc)
    bm, bs = moments(baseline_scores)
    return {"coherent": k, "of": len(turns), "coherence_pass": k >= COHERENT_MIN,
            "arrival": {"scored": len(sc), "baseline_scored": len(baseline_scores), "t": t, "sign": int(sign),
                        "pass": bool(ok), "mean": m, "sd": s, "baseline_mean": bm, "baseline_sd": bs,
                        "diff": None if m is None or bm is None else m - bm},
            "pass": bool(k >= COHERENT_MIN and ok)}


def stage_status(figures: Mapping) -> str:
    """GC14: STOP if either hurdle fails at +ρ or −ρ; PAUSE if only +ρ/2 fails; PASS otherwise."""
    if any(not figures[b]["pass"] for b in STOP_BATCHES):
        return "STOP"
    if any(not figures[b]["pass"] for b in PAUSE_BATCHES):
        return "PAUSE"
    return "PASS"


def dose_map(R: float, R_ell: float) -> dict:
    """GC16: the map from G-VEC's R and R_ℓ, by exactly the schema's and the analyzer's expressions."""
    R, R_ell = float(R), float(R_ell)
    if not (math.isfinite(R) and math.isfinite(R_ell) and R > 0.0 and R_ell > 0.0):
        raise ValueError("R and R_ell must be finite and positive")
    d_eq = (0.10 * R_ell) / (schema.RHO * R)
    d_20 = min(1.0, 2.0 * d_eq)
    return {"rho": schema.RHO, "R": R, "R_ell": R_ell, "d_eq": d_eq, "d_20": d_20,
            "points": schema.dose_points(d_eq, d_20)}


def injection_for(d: float, v_unit, site: int, R: float, v_sha16: str) -> Injection | None:
    """The batch's injection (runner's ``_injection`` arithmetic): None at d = 0."""
    if d == 0.0:
        return None
    return Injection.at_frac(np.asarray(v_unit, dtype=np.float64), int(site), abs(float(d)) * schema.RHO,
                             {int(site): float(R)}, expect_sha=v_sha16).with_sign(1 if d > 0 else -1)


def compute(step_logits: Callable, forward_capture: Callable, decode: Callable, prompts: Sequence[Mapping], *,
            v_unit, v_sha16: str, site: int, R: float, eos_id: int, batches=BATCHES, n: int | None = None,
            temp: float = TEMP, cap: int = CAP, say: Callable = print, on_turn: Callable | None = None) -> dict:
    """The stage's turns and figures. ``prompts`` are the (v) records (index, label, seed, ids, gen_start), in order;
    ``n`` keeps the first n (the smoke's). Every batch is generated first, in ``GENERATION_ORDER`` (GC23 (d)), a batch
    at a positive dose after its steering check, each turn handed to ``on_turn`` as soon as it is generated (GC23 (a));
    then every turn's arrival forward; then the hurdles. The result keeps ``batches``' order. A smoke (``batches``
    without −ρ) gets no hurdle and the status SMOKE. ``temp`` and ``cap`` are the stage's TEMP and CAP; the self-test
    alone passes a smaller cap, for speed."""
    recs = list(prompts)[: (len(prompts) if n is None else int(n))]
    turns: dict = {}
    for name, d in sorted(batches, key=lambda bd: GENERATION_ORDER.index(bd[0])):
        inj = injection_for(d, v_unit, site, R, v_sha16)
        if d > 0.0 and recs:
            dev = steering_check(step_logits, recs[0], inj)
            say(f"steering check {name}: the first prompt's first-step logits, steered and unsteered, differ by up "
                f"to {dev!r}")
        rows = []
        for rec in recs:
            g = generate(step_logits, rec["ids"], rec["gen_start"], inj, rec["seed"], eos_id=eos_id, temp=temp,
                         cap=cap)
            text = decode(g["ids"])
            coh = coherence(text)
            row = {"batch": name, "d": float(d), "index": int(rec["index"]), "label": rec["label"],
                   "seed": int(rec["seed"]), "ids": g["ids"], "n_tok": g["n_tok"], "stop": g["stop"],
                   "cap_hit": g["cap_hit"], "decode": text, "coherence": coh, "arrival": None}
            rows.append(row)
            if on_turn is not None:
                on_turn(row)
            say(f"turn {name} {int(rec['index'])} {rec['label']}: n_tok {g['n_tok']}, stop {g['stop']}, "
                f"coherent {coh['coherent']}")
        turns[name] = rows
    for name, _d in batches:
        for r in turns[name]:
            r["arrival"] = arrival_score(forward_capture, r["ids"], site, v_unit)
    names = [b for b, _d in batches]
    smoke = "-rho" not in names
    base = [float(r["arrival"]) for r in turns["baseline"] if r["arrival"] is not None]
    figures: dict = {"baseline": {"coherent": sum(1 for r in turns["baseline"] if r["coherence"]["coherent"]),
                                  "of": len(turns["baseline"]), "scored": len(base)}}
    for name, d in batches:
        if d != 0.0:
            figures[name] = batch_figures(turns[name], base, 1 if d > 0 else -1)
        figures[name]["stops"] = stops(turns[name])
        f = figures[name]
        if d != 0.0:
            say(f"batch {name}: coherent {f['coherent']} of {f['of']} (pass {f['coherence_pass']}); arrival t "
                f"{f['arrival']['t']!r} over {f['arrival']['scored']} against {len(base)} (pass "
                f"{f['arrival']['pass']}); stops eos {f['stops']['eos']}, cap {f['stops']['cap']}, empty "
                f"{f['stops']['empty']}")
    status = "SMOKE" if smoke else stage_status(figures)
    minus = turns.get("-rho", [])
    exposure = {"turns": len(minus), "tokens": sum(int(r["n_tok"]) for r in minus),
                "draws": sum(int(r["n_tok"]) + int(r["stop"] == "eos") for r in minus)}
    return {"status": status, "turns": turns, "figures": figures, "exposure_minus_rho": exposure,
            "batches": names}


def _dumps(obj) -> str:
    return json.dumps(obj, sort_keys=True, indent=1, allow_nan=False)


def turns_lines(result: Mapping) -> bytes:
    return "".join(json.dumps(r, sort_keys=True, allow_nan=False) + "\n"
                   for b in result["batches"] for r in result["turns"][b]).encode("utf-8")


def append_turn(path, row: Mapping) -> None:
    """GC23 (a): one turn's row appended to the log at ``path`` as one JSON line, flushed and fsynced before the next
    turn starts."""
    line = json.dumps(row, sort_keys=True, allow_nan=False) + "\n"
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.flush()
        os.fsync(fh.fileno())


def write(out_dir, result: Mapping, dmap: Mapping, provenance: Mapping) -> dict:
    """The outputs into ``out_dir`` (which the driver has staged): the turns, the dose map's five figures, then the
    record with their sha256s. Returns the record."""
    d = Path(out_dir)
    shas: dict = {}
    tb = turns_lines(result)
    (d / OUT_TURNS).write_bytes(tb)
    shas[OUT_TURNS] = hashlib.sha256(tb).hexdigest()
    mb = (json.dumps({k: dmap[k] for k in DOSE_MAP_KEYS}, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")
    (d / OUT_DOSE_MAP).write_bytes(mb)
    shas[OUT_DOSE_MAP] = hashlib.sha256(mb).hexdigest()
    rec = {"schema": RECORD_SCHEMA, "stage": STAGE, "status": result["status"],
           "proposal_sha256": schema.PROPOSAL_SHA256, "batches": list(result["batches"]),
           "figures": result["figures"], "dose_map": dict(dmap), "pinnable": result["status"] == "PASS",
           "exposure_minus_rho": result["exposure_minus_rho"], "conventions": CONVENTIONS,
           "constants": {"n_turns": N_TURNS, "temp": TEMP, "cap": CAP, "coherent_min": COHERENT_MIN, "t_bar": T_BAR,
                         "min_words": MIN_WORDS, "trigram_repeat_max": TRIGRAM_REPEAT_MAX,
                         "diversity_min": DIVERSITY_MIN, "generation_window": GENERATION_WINDOW,
                         "generation_order": list(GENERATION_ORDER)},
           "provenance": dict(provenance), "files_sha256": shas}
    (d / OUT_RECORD).write_text(_dumps(rec) + "\n", encoding="utf-8")
    return rec


# --- self-test (model-free) ---------------------------------------------------------------------------------------

def _selftest(chk, tmp) -> None:
    tmp = Path(tmp)
    tmp.mkdir(parents=True, exist_ok=True)
    # the rendering, in one place
    u, g = prompt_parts("Zone B8")
    chk("gcal: the prompt's two texts are the rendering of record's user turn and generation prompt (GC5, GC6)",
        u == "<|user|>\nYou are now in Zone B8. Write a few sentences about your present experience here.\n"
        and g == "<|assistant|>\n", (u, g))
    labs = ["Zone W6", "Zone B8", "Zone D7", "Zone H0", "Zone K7", "Zone L4", "Zone M2", "Zone N1", "Zone Q3",
            "Zone R9", "Zone T5", "Zone V3"]
    p = plan(labs)
    chk("gcal: the plan is 48 prompts, label i mod 12 of the sorted labels, replicate i // 12, seed keys.gcal_seed(i)",
        len(p) == 48 and [r["label"] for r in p[:12]] == sorted(labs) and p[12]["label"] == "Zone B8"
        and [r["rep"] for r in p[::12]] == [0, 1, 2, 3] and all(r["seed"] == keys.gcal_seed(i) for i, r in enumerate(p))
        and len({r["seed"] for r in p}) == 48, "")
    chk("gcal: the plan refuses a label set other than 12 distinct", _raises(lambda: plan(labs[:11]))
        and _raises(lambda: plan(labs[:11] + ["Zone B8"])), "")
    # sampling
    rng1, rng2 = np.random.default_rng(5), np.random.default_rng(5)
    lg = np.array([0.0, 1.0, 2.0, 3.0])
    a = [sample(lg, 0.7, rng1) for _ in range(200)]
    b = [sample(lg, 0.7, rng2) for _ in range(200)]
    us = np.random.default_rng(5).random(200)

    def inv_cdf(temp_):            # an independent derivation: the normalized softmax's CDF at the same 200 uniforms
        p_ = np.exp((lg - lg.max()) / temp_)
        c_ = np.cumsum(p_ / p_.sum())
        return [int(min(np.searchsorted(c_, u_, side="right"), len(c_) - 1)) for u_ in us]
    chk("gcal: sampling is the inverse CDF of softmax(logits / TEMP) at one rng.random() per draw: 200 draws equal an "
        "independent derivation's at 0.7, which differs from 1.0's; the same generator gives the same draws",
        a == b and a == inv_cdf(0.7) and inv_cdf(0.7) != inv_cdf(1.0), (a[:12], inv_cdf(0.7)[:12]))
    r3 = np.random.default_rng(1)
    chk("gcal: one dominant logit is always drawn; non-finite logits are refused",
        all(sample(np.array([0.0, 60.0, 0.0]), 0.7, r3) == 1 for _ in range(20))
        and _raises(lambda: sample(np.array([0.0, np.nan]), 0.7, r3)), "")
    # the heuristic, on literal strings
    c1 = coherence("The garden is quiet, and the light is soft on the path today.")
    c2 = coherence("I am here.")
    c3 = coherence("the same old the same old the same old the same old the same old")
    c4 = coherence("go go go go go go go go go go go go go go go go go go go go")
    c5 = coherence("")
    c6 = coherence("“Hello,” she said — softly... (again) and again!")
    chk("gcal: coherence (GC11): a plain sentence is coherent; fewer than 4 words collapses; trigram repeats over 0.5 loop; "
        "under 5 distinct per 20 is low diversity; an empty turn fails; outer Unicode punctuation is stripped",
        c1["coherent"] and not c2["coherent"] and c2["length_collapse"] and c2["n_words"] == 3
        and c3["repetition_loop"] and c3["trigram_repeat"] > 0.5 and not c3["coherent"]
        and c4["low_diversity"] and c4["diversity"] == 1 / 20 and not c4["coherent"]
        and c5["length_collapse"] and c5["low_diversity"] and not c5["coherent"]
        and words("“Hello,” she said — softly... (again) and again!") == ["hello", "she", "said", "softly", "again",
                                                                        "and", "again"]
        and c6["n_words"] == 7, (c1, c2, c3, c4, c6))
    edge = coherence("a b c a b c a b")       # 6 trigrams, 3 distinct: exactly 0.5, not above it
    chk("gcal: a trigram fraction of exactly 0.5 is not a loop, and diversity of exactly 5/20 is not low",
        edge["trigram_repeat"] == 0.5 and not edge["repetition_loop"]
        and not coherence(" ".join(["w1", "w2", "w3", "w4", "w5"] * 4))["low_diversity"], edge)
    # Welch's t, on literal arrays
    t = welch_t([1.0, 2.0, 3.0, 4.0], [0.0, 0.5, 1.0])
    ma, mb, va, vb = 2.5, 0.5, np.var([1, 2, 3, 4], ddof=1), np.var([0.0, 0.5, 1.0], ddof=1)
    chk("gcal: Welch's t is (mean a - mean b) / sqrt(var_a/n_a + var_b/n_b) with ddof 1; None when undefined",
        t is not None and abs(t - (ma - mb) / math.sqrt(va / 4 + vb / 3)) < 1e-12
        and welch_t([1.0], [1.0, 2.0]) is None and welch_t([1.0, 1.0], [2.0, 2.0]) is None, t)
    # the dose map, against the schema's own construction and check
    dm = dose_map(25.49, 38.0)
    ident = schema.example_identity(R=25.49, R_ell=38.0)
    ok_check = True
    try:
        schema.check_stage_identity(ident)
    except schema.SchemaError:
        ok_check = False
    chk("gcal: the dose map is d_eq = (0.10 R_ell)/(rho R), d_20 = min(1, 2 d_eq), the points dose_points', equal to the "
        "schema's own example identity's map, which the schema's check accepts",
        dm["d_eq"] == (0.10 * 38.0) / (schema.RHO * 25.49) and dm["d_20"] == min(1.0, 2.0 * dm["d_eq"])
        and dm["points"] == schema.dose_points(dm["d_eq"], dm["d_20"]) and dm["rho"] == schema.RHO
        and ident["dose_map"] == dm and ok_check, dm)
    chk("gcal: the dose map refuses a non-positive or non-finite R or R_ell, and a fold into 0",
        _raises(lambda: dose_map(0.0, 1.0)) and _raises(lambda: dose_map(1.0, float("nan")))
        and _raises(lambda: dose_map(25.49, 0.3 * 25.49 * 0.4)), "")
    # the flow over the double: generation, steering positions, the hurdles
    be = testing_double()
    site, R = 2, 3.0
    v = np.zeros(be.d_model)
    v[0] = 1.0
    vu = v / np.linalg.norm(v)
    vsha = sha16_arr(vu)
    seen: list = []

    def step(ids, injections):
        seen.append((len(ids), tuple((i.positions.kind, i.positions.start, round(i.alpha, 12)) for i in injections)))
        return be.prefill(ids, injections, ()).logits_last

    def cap_fn(ids, layers):
        return be.forward_all(ids, layers)

    def dec(ids):
        return " ".join(f"w{int(i) % 11}" for i in ids)
    eos = 7
    prompts = [{"index": i, "label": f"Zone {i}", "seed": keys.gcal_seed(i), "ids": [3, 4, 5, 6, 8 + i % 5],
                "gen_start": 3} for i in range(N_TURNS)]
    one = generate(step, prompts[0]["ids"], 3, None, prompts[0]["seed"], eos_id=eos)
    chk("gcal: one turn at the stage's defaults (TEMP 0.7, cap 80): at most 80 ids, none the eos, stop eos or cap",
        one["n_tok"] == len(one["ids"]) <= CAP and eos not in one["ids"] and one["stop"] in ("eos", "cap")
        and (one["stop"] == "cap") == (one["n_tok"] == CAP) and TEMP == 0.7 and CAP == 80, one)
    first = generate(lambda ids, inj: np.where(np.arange(be.vocab) == eos, 50.0, 0.0), [3, 4, 5], 1, None, 9, eos_id=eos)
    chk("gcal: an end of turn drawn first emits no id; such a turn has no arrival score and is left out of the t",
        first == {"ids": [], "n_tok": 0, "stop": "eos", "cap_hit": False}
        and arrival_score(lambda ids, layers: {}, [], 2, np.ones(3)) is None
        and batch_figures([{"coherence": {"coherent": True}, "arrival": None}] + [
            {"coherence": {"coherent": True}, "arrival": 1.0 + 0.1 * i} for i in range(3)],
            [0.0, 0.1, 0.2], 1)["arrival"]["scored"] == 3, first)
    chk("gcal: generate refuses a gen_start outside the prompt", _raises(lambda: generate(step, [3, 4], 0, None, 1,
                                                                                          eos_id=eos))
        and _raises(lambda: generate(step, [3, 4], 2, None, 1, eos_id=eos)), "")

    def scripted(script, log):     # one dominant logit per step, keyed on the length of the sequence it is given
        def f(ids, inj):
            log.append(len(ids))
            k = len(ids) - 3
            return np.where(np.arange(be.vocab) == (script[k] if k < len(script) else 9), 60.0, 0.0)
        return f
    log_e: list = []
    log_c: list = []
    g_e = generate(scripted([5, 6, eos, 9], log_e), [3, 4, 5], 1, None, 11, eos_id=eos)
    g_c = generate(scripted([5, 6, 8, 9], log_c), [3, 4, 5], 1, None, 11, eos_id=eos, cap=4)
    chk("gcal: generate stops at the first end of turn with what came before it, one forward per step over the "
        "sequence so far, each step seeing its own output; at the cap, cap ids, the last forward longest_forward's",
        g_e == {"ids": [5, 6], "n_tok": 2, "stop": "eos", "cap_hit": False} and log_e == [3, 4, 5]
        and g_c == {"ids": [5, 6, 8, 9], "n_tok": 4, "stop": "cap", "cap_hit": True} and log_c == [3, 4, 5, 6]
        and max(log_c) == longest_forward(3, 4) == 6, (g_e, log_e, g_c, log_c))
    res = compute(step, cap_fn, dec, prompts, v_unit=vu, v_sha16=vsha, site=site, R=R, eos_id=eos, cap=6,
                  say=lambda s: None)
    t_all = [r for b in res["batches"] for r in res["turns"][b]]
    chk("gcal: the flow generates 4 batches x 48 turns in n:113's order, each within its cap, no eos among them, each "
        "stop eos or cap", res["batches"] == ["+rho", "-rho", "+rho/2", "baseline"] and len(t_all) == 192
        and all(r["n_tok"] == len(r["ids"]) <= 6 and eos not in r["ids"] and r["stop"] in ("eos", "cap")
                and r["cap_hit"] == (r["stop"] == "cap") for r in t_all), "")
    steered = [s for s in seen if s[1]]
    alphas = sorted({s[1][0][2] for s in steered})
    chk("gcal: steering is placed from gen_start onward at alpha |d|·rho·R with d's sign; the baseline unsteered",
        all(s[1][0][0] == "from" and s[1][0][1] == 3 for s in steered)
        and alphas == sorted({round(1.0 * schema.RHO * R, 12), round(-1.0 * schema.RHO * R, 12),
                              round(0.5 * schema.RHO * R, 12)})
        and sum(1 for s in seen if not s[1]) >= N_TURNS, alphas)
    again = compute(step, cap_fn, dec, prompts, v_unit=vu, v_sha16=vsha, site=site, R=R, eos_id=eos, cap=6,
                    say=lambda s: None)
    chk("gcal: the flow is deterministic: the same seeds give the same turns; prompt i's seed is the same in all four "
        "batches", [r["ids"] for b in res["batches"] for r in res["turns"][b]]
        == [r["ids"] for b in again["batches"] for r in again["turns"][b]]
        and all(res["turns"][b][i]["seed"] == keys.gcal_seed(i) for b in res["batches"] for i in range(N_TURNS)), "")
    chk("gcal: every turn's decode is the decode of its emitted ids, its coherence that decode's",
        all(r["decode"] == dec(r["ids"]) and r["coherence"] == coherence(r["decode"]) for r in t_all), "")
    chk("gcal: arrival scores are the mean projection of the emitted ids' own unsteered capture at the site",
        all((r["arrival"] is None) == (r["n_tok"] == 0) for r in t_all)
        and all(abs(r["arrival"] - float(np.mean(be.forward_all(r["ids"], (site,))[site].astype(np.float64) @ vu)))
                < 1e-12 for r in t_all if r["arrival"] is not None), "")
    f = res["figures"]
    chk("gcal: each steered batch's figures follow its turns (coherent count, Welch's t against the baseline, the "
        "pole's sign)", all(f[b]["coherent"] == sum(1 for r in res["turns"][b] if r["coherence"]["coherent"])
                           and f[b]["arrival"]["sign"] == (1 if b != "-rho" else -1) for b in STEERED)
        and f["baseline"]["of"] == 48 and res["exposure_minus_rho"]["turns"] == 48
        and res["exposure_minus_rho"]["tokens"] == sum(r["n_tok"] for r in res["turns"]["-rho"]), "")
    base_t = [r["arrival"] for r in res["turns"]["baseline"] if r["arrival"] is not None]
    inj_p = injection_for(1.0, vu, site, R, vsha)
    chk("gcal: compute's wiring: each baseline turn is generate's own at TEMP 0.7 from keys.gcal_seed(i), a +rho turn "
        "generate's under +rho's injection, and each steered batch's t Welch's t of its scores against the baseline's",
        [r["ids"] for r in res["turns"]["baseline"]]
        == [generate(step, p_["ids"], p_["gen_start"], None, keys.gcal_seed(i), eos_id=eos, cap=6)["ids"]
            for i, p_ in enumerate(prompts)]
        and [res["turns"]["+rho"][i]["ids"] for i in (0, 7)]
        == [generate(step, prompts[i]["ids"], prompts[i]["gen_start"], inj_p, keys.gcal_seed(i), eos_id=eos,
                     cap=6)["ids"] for i in (0, 7)]
        and all(f[b]["arrival"]["t"] == welch_t([r["arrival"] for r in res["turns"][b] if r["arrival"] is not None],
                                                base_t) for b in STEERED), "")
    chk("gcal: each batch's stops (eos, cap, empty) and the -rho exposure's draws (emitted ids and drawn ends) follow "
        "the turns", all(f[b]["stops"] == {"eos": sum(r["stop"] == "eos" for r in res["turns"][b]),
                                            "cap": sum(r["stop"] == "cap" for r in res["turns"][b]),
                                            "empty": sum(r["n_tok"] == 0 for r in res["turns"][b])}
                         for b in res["batches"])
        and res["exposure_minus_rho"]["draws"]
        == sum(r["n_tok"] + (r["stop"] == "eos") for r in res["turns"]["-rho"]), "")
    n_deaf: list = []

    def deaf(ids, injections):     # a forward that drops the injection
        n_deaf.append(len(ids))
        return be.prefill(ids, (), ()).logits_last
    chk("gcal: the steering check: on the double the steered first step differs from the unsteered; a forward that "
        "drops the injection is refused after the check's two forwards, before any turn",
        steering_check(step, prompts[0], inj_p) > 0.0
        and _raises(lambda: compute(deaf, cap_fn, dec, prompts, v_unit=vu, v_sha16=vsha, site=site, R=R, eos_id=eos,
                                    cap=6, say=lambda s: None)) and len(n_deaf) == 2, n_deaf)
    handed: list = []
    res_o = compute(step, cap_fn, dec, prompts, v_unit=vu, v_sha16=vsha, site=site, R=R, eos_id=eos, cap=6,
                    say=lambda s: None,
                    on_turn=lambda r: handed.append((r["batch"], r["index"], list(r["ids"]), r["arrival"])))
    seq = [(b, i) for b in GENERATION_ORDER for i in range(N_TURNS)]
    chk("gcal: GC23 (d): the batches are generated in GENERATION_ORDER (+rho, +rho/2, the baseline, -rho last), each "
        "turn handed to on_turn as it is generated, before its arrival is scored; the result keeps n:113's order and "
        "the same turns", GENERATION_ORDER == ("+rho", "+rho/2", "baseline", "-rho")
        and sorted(GENERATION_ORDER) == sorted(b for b, _d in BATCHES)
        and [(b, i) for b, i, _ids, _a in handed] == seq and all(a is None for *_x, a in handed)
        and res_o["batches"] == [b for b, _d in BATCHES]
        and all(ids_ == res_o["turns"][b][i]["ids"] == res["turns"][b][i]["ids"] for b, i, ids_, _a in handed), "")
    log_p = tmp / "turn_log.jsonl"
    append_turn(log_p, {"index": 0, "batch": "+rho", "ids": [1, 2]})
    append_turn(log_p, {"index": 1, "batch": "+rho", "ids": []})
    chk("gcal: GC23 (a): append_turn adds one sorted-key JSON line per turn to the log, and refuses a non-finite value "
        "before it writes", log_p.read_text(encoding="utf-8").splitlines()
        == ['{"batch": "+rho", "ids": [1, 2], "index": 0}', '{"batch": "+rho", "ids": [], "index": 1}']
        and _raises(lambda: append_turn(log_p, {"x": float("nan")}))
        and len(log_p.read_text(encoding="utf-8").splitlines()) == 2, "")
    chk("gcal: an injection with another direction's sha16 is refused before any turn",
        _raises(lambda: compute(step, cap_fn, dec, prompts, v_unit=vu, v_sha16="0" * 16, site=site, R=R, eos_id=eos,
                                say=lambda s: None)), "")
    # the status rule, on literal figures
    def fig(p_):
        return {"pass": p_}
    chk("gcal: status (GC14): a fail at +rho or -rho is a STOP; a fail at +rho/2 alone a PAUSE; else PASS",
        stage_status({"+rho": fig(True), "-rho": fig(True), "+rho/2": fig(True)}) == "PASS"
        and stage_status({"+rho": fig(False), "-rho": fig(True), "+rho/2": fig(True)}) == "STOP"
        and stage_status({"+rho": fig(True), "-rho": fig(False), "+rho/2": fig(False)}) == "STOP"
        and stage_status({"+rho": fig(True), "-rho": fig(True), "+rho/2": fig(False)}) == "PAUSE", "")
    turns_ok = [{"coherence": {"coherent": True}, "arrival": 1.0 + 0.01 * i} for i in range(48)]
    base_sc = [0.01 * i for i in range(48)]
    bf = batch_figures(turns_ok, base_sc, 1)
    bf_neg = batch_figures(turns_ok, base_sc, -1)
    few = batch_figures([{"coherence": {"coherent": i < 35}, "arrival": 1.0 + 0.01 * i} for i in range(48)], base_sc, 1)
    chk("gcal: a batch passes on >= 36 coherent and t >= 2 for a positive pole; the same scores fail a negative pole; "
        "35 coherent fail", bf["pass"] and bf["arrival"]["t"] > 2 and not bf_neg["pass"] and not few["pass"]
        and few["coherent"] == 35 and not few["coherence_pass"] and few["arrival"]["pass"], (bf, few))
    chk("gcal: the hurdles' constants: 48 turns, 36 coherent, |t| >= 2, 4 words, a trigram fraction of 0.5, 5 distinct "
        "per 20; the generation window 4096, within the choice-read window",
        (N_TURNS, COHERENT_MIN, T_BAR, MIN_WORDS, TRIGRAM_REPEAT_MAX, DIVERSITY_MIN, GENERATION_WINDOW)
        == (48, 36, 2.0, 4, 0.5, 0.25, 4096) and GENERATION_WINDOW <= schema.MAX_WINDOW, "")
    k36 = batch_figures([{"coherence": {"coherent": i < 36}, "arrival": 1.0 + 0.01 * i} for i in range(48)], base_sc, 1)
    four = coherence("the light is soft")
    nine = coherence("a b c d a b c d a b c")          # 9 trigrams, 4 distinct: 5/9 repeat
    low = coherence(" ".join(["w1", "w2", "w3", "w4"] * 5))
    chk("gcal: each bar from its other side: 36 coherent pass; 4 words do not collapse; a trigram fraction of 5/9 "
        "loops; 4 distinct per 20 is low", k36["coherent"] == 36 and k36["coherence_pass"] and k36["pass"]
        and four["n_words"] == 4 and not four["length_collapse"] and four["coherent"]
        and abs(nine["trigram_repeat"] - 5 / 9) < 1e-12 and nine["repetition_loop"] and not nine["low_diversity"]
        and low["diversity"] == 4 / 20 and low["low_diversity"], (k36["coherent"], four, nine, low))

    def t_case(m, sign):           # scores sign*m -/+ 1 against -1, +1: Welch's t is sign * m / sqrt(2)
        return batch_figures([{"coherence": {"coherent": True}, "arrival": sign * m + x} for x in (-1.0, 1.0)],
                             [-1.0, 1.0], sign)["arrival"]
    hi, lo_ = t_case(2.05 * math.sqrt(2.0), 1), t_case(1.95 * math.sqrt(2.0), 1)
    hin, lon = t_case(2.05 * math.sqrt(2.0), -1), t_case(1.95 * math.sqrt(2.0), -1)
    single = batch_figures([{"coherence": {"coherent": True}, "arrival": 5.0}]
                           + [{"coherence": {"coherent": True}, "arrival": None}] * 47, base_sc, 1)
    chk("gcal: arrival passes at |t| = 2.05 and fails at 1.95, at each pole's sign; one scored turn (t undefined) "
        "fails arrival, and the batch",
        2.0 < hi["t"] < 2.1 and hi["pass"] and 1.9 < lo_["t"] < 2.0 and not lo_["pass"]
        and -2.1 < hin["t"] < -2.0 and hin["pass"] and -2.0 < lon["t"] < -1.9 and not lon["pass"]
        and single["arrival"]["t"] is None and not single["arrival"]["pass"] and not single["pass"],
        (hi, lo_, hin, lon))
    sh, sc_ok = bf["arrival"], [r["arrival"] for r in turns_ok]
    chk("gcal: the shift beside the t: each side's mean and SD (ddof 1) and the difference of the means; None where "
        "undefined", abs(sh["mean"] - float(np.mean(sc_ok))) < 1e-12
        and abs(sh["sd"] - float(np.std(sc_ok, ddof=1))) < 1e-12
        and abs(sh["baseline_mean"] - float(np.mean(base_sc))) < 1e-12
        and abs(sh["baseline_sd"] - float(np.std(base_sc, ddof=1))) < 1e-12
        and sh["diff"] == sh["mean"] - sh["baseline_mean"] and single["arrival"]["mean"] == 5.0
        and single["arrival"]["sd"] is None and moments([]) == (None, None), sh)
    tu, tg = prompt_parts("{zone}")
    chk("gcal: CONVENTIONS' rendering is derived from prompt_parts (the template the (v) render records)",
        json.dumps(tu) in CONVENTIONS["rendering"] and json.dumps(tg) in CONVENTIONS["rendering"]
        and json.dumps(USER_PROMPT) in CONVENTIONS["prompts"], "")
    smk = compute(step, cap_fn, dec, prompts, v_unit=vu, v_sha16=vsha, site=site, R=R, eos_id=eos, cap=6,
                  batches=SMOKE_BATCHES, n=2, say=lambda s: None)
    chk("gcal: a smoke runs +rho and the baseline only, on the first prompts, never -rho, its status SMOKE",
        smk["status"] == "SMOKE" and smk["batches"] == ["+rho", "baseline"] and len(smk["turns"]["+rho"]) == 2
        and smk["exposure_minus_rho"] == {"turns": 0, "tokens": 0, "draws": 0}, "")
    # the outputs
    out = tmp / "gcal_out"
    out.mkdir()
    rec = write(out, res, dm, {"driver_sha256": "d" * 64})
    lines = (out / OUT_TURNS).read_text(encoding="utf-8").splitlines()
    five = json.loads((out / OUT_DOSE_MAP).read_text(encoding="utf-8"))
    chk("gcal: write puts the 192 turns, the dose map's five figures (ganl --dose-map's form) and the record with their "
        "sha256s", len(lines) == 192 and sorted(five) == sorted(DOSE_MAP_KEYS)
        and all(five[k] == dm[k] for k in DOSE_MAP_KEYS)
        and rec["files_sha256"] == {OUT_TURNS: hashlib.sha256((out / OUT_TURNS).read_bytes()).hexdigest(),
                                    OUT_DOSE_MAP: hashlib.sha256((out / OUT_DOSE_MAP).read_bytes()).hexdigest()}
        and json.loads((out / OUT_RECORD).read_text(encoding="utf-8"))["pinnable"] == (res["status"] == "PASS")
        and sorted(p.name for p in out.iterdir()) == sorted([OUT_RECORD, OUT_TURNS, OUT_DOSE_MAP]), "")


def testing_double():
    from .testing import CausalDouble
    return CausalDouble(vocab=23, d_model=8, n_layers=4, seed=20261119)


def _raises(fn) -> bool:
    try:
        fn()
    except (ValueError, KeyError, schema.SchemaError, SystemExit):
        return True
    return False
