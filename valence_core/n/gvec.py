"""PROPOSAL-n -- G-VEC (n v0.2 §8 step 7; the G-VEC paragraph, n v0.2 §3): the directions of record and their
figures, computed on the box from the committed ids, before G-CAL-n.

What it computes (n §0.8, §2.3; ADDENDUM-n1 §6.1-§6.2 and §1.1):
  * the 544 passages of record (``data/n/ids/gvec_passages.jsonl``, (iv)), each forwarded alone from its committed
    ids, their residuals captured at the candidate indices 31 and 32; per passage and index, the mean over its tokens,
    the sum of its tokens' squared norms, and its token count (``passage_captures``);
  * R at each index, the RMS residual norm over the 96 neutral passages' tokens (``directions.rms_norm``). The site is
    the index whose R is within 2% of 25.49, the nearer if both are (ADDENDUM-n1 §6.1); neither is a STOP for the
    seat (n §2.3: "reproduced at G-VEC within 2%, else STOP");
  * at each index, U and v by BK's recipe (``directions.valence_direction``);
  * N2's three directions by A3's recipe (g:164-170) on the 1,344 contexts of record (``a3_contexts.jsonl``, (iv)):
    one forward per context from its committed ids, the span from its committed ``span_start``, and
    ``valence_core.extract``'s span-mean and R_l arithmetic (``a3_capture``), with its ``mean_diff_axis``,
    ``axis_report`` and ``freeze_sha`` imported unchanged; R_ℓ at each index;
  * the cosines among the four named directions (the analyzer's ``--gvec`` file: their six pairs) and among all 28,
    the 24 random directions (``keys.random_directions``) among them.

The box tokenizes nothing (ADDENDUM-n1 §1.1): ``extract.capture``, which encodes, is not called. ``a3_capture`` is
its arithmetic, operation for operation, on the committed ids, and the self-test holds the two equal on the double.

A stored direction is a float32 row that the Injection's own normalization leaves unchanged (``unit32``), and its
sha16 is the Injection's (``adapters.base.Injection``: u / ||u|| in float64, hashed as float32): the fingerprint the
campaign's ``Injection.at_frac(..., expect_sha=...)`` checks it against (the schema's ``direction_sha16``).

Code's readings (G1-G14, declared at G-VEC's BUILD for the seat; the coordinating session's routing of 2026-11-19;
G1, G3, G6 and G9 starred at the top of LOCK-n v0.1's list):
  G1* the capture convention is ``directions``' (each passage alone, from its committed ids, with no special token and
      no template; every token in its mean and in R; the neutral PCA centred; R the pooled RMS). The R check tests the
      clauses that bear on R (the passage alone, no special token, every token, the pooled RMS); it cannot test the
      centring, so v under an uncentred U is recorded and stored beside, descriptive (the review's O1).
  G2  one forward per passage captures both candidate indices; R at both; the site by ADDENDUM-n1 §6.1, "the nearer"
      read as nearer in R to 25.49 and an exact tie going to 32, the index BK's "layer 32" names; U, h̄± and v at
      both, the site's of record.
  G3* N2's three directions and R_ℓ at the site index (n §2.3: "layer 32 of 64 ... for every direction in N1, N2 and
      N4"; the schema's "R_l at the site"), and at the other index beside.
  G4  A3 on the committed ids, as above.
  G5  before the load, A3's frozen inputs and rule-18 hygiene (``scripts/box_e0_corpus.py``); the guard profile at both
      indices, descriptive; A3's other layers not run; no step-2 survey exists for this checkpoint, so R_ℓ has no
      cross-check (recorded as absent, with why).
  G6* extraction over all 1,344 contexts, as A3's (``extract.mean_diff_axis`` over every context of each condition);
      A3's split carried at the record's top level, as A3's artifacts carry it, and asserted
      (``extract.assert_stage_splits``); N2's directions fit on ``fit_ids`` alone stored and recorded beside,
      descriptive, A3's all-context form the one of record.
  G7  the outputs, under data/n/gvec/ (the BUILD commit admits them in .gitignore): ``gvec.json`` (the record);
      ``directions_L31.npy`` and ``directions_L32.npy`` (the named rows, float32, in ``NAMED``'s order);
      ``directions_alt_L31.npy`` and ``directions_alt_L32.npy`` (``ALT``'s rows: N2's fit-only directions and v under
      an uncentred U, descriptive); ``gvec_cosines.json`` (the analyzer's form); the 24 random directions' sha16s
      recorded; no resume (one invocation; a failure is re-run whole).
  G8  the cosines: the six pairs of the four named directions, and all 378 pairs of the 28 directions (n §2.3: "among
      all directions", BK Table A3's form), at the site: the named rows as stored, the random rows as
      ``keys.random_directions`` draws them (float64, never stored).
  G9* the check is |R / 25.49 - 1| <= 0.02, on 25.49 exactly as n §2.3 writes it; R and R_ℓ are recorded as full
      float64, never rounded; BK's 25.491040760519905 and pole_l2 2.319276809692383 beside, descriptive.
  G10 Route A is not wired (the PI's routing of 2026-11-06: "[not sent]"); the record carries "direction of record:
      Route B" in PIN-n-26's line form.
  G11 the corpus's state names map to BK's through ``directions.bk_state`` (the corpus unedited); the record's token
      table is keyed by BK's names (the seat's corpus-adoption answers, §1.4: "the paper's state names are BK's").
  G14 BK's pole_l2 beside ‖v‖ and ‖h̄₊ − h̄₋‖, descriptive.
(G12 and G13 are the driver's: its refusals and lines, and the ids of record.)

Departures from G1-G14's words as routed (the review's F10, O3): G7's single ``directions.npz`` is per-index ``.npy``
files, two of them ``ALT``'s, and A3's freeze_sha sits in ``gvec.json`` per index; G2's tie rule; G5's guard profile at
both indices, not the site alone; G6's fit-only family stored as rows, not figures alone; G1's uncentred variant; the
record's ``of_record`` block (the site's R, R_ℓ and directions together).
"""
from __future__ import annotations

import dataclasses
import hashlib
import json
import math
from pathlib import Path
from typing import Callable, Mapping, Sequence

import numpy as np

from .. import extract
from ..adapters.base import Injection, sha16_arr
from . import directions, keys, schema

RECORD_SCHEMA = "n-gvec-v1"
STAGE = "G-VEC"
CANDIDATE_INDICES = (31, 32)                 # ADDENDUM-n1 §6.1
R_REFERENCE = 25.49                          # n §2.3: "R ≈ 25.49 there [C] -- reproduced at G-VEC within 2%"
R_TOLERANCE = 0.02
R_BK_RECORD = 25.491040760519905             # BK's resid_rms (strength_ladder/analysis.json), descriptive
POLE_L2_BK = 2.319276809692383               # BK's pole_l2 beside it, descriptive (G14)
ROUTE = "B"
ROUTE_LINE = "direction of record: Route B"  # PIN-n-26's line form (scripts/n_analyze.py's ROUTE_LINE + the route)
NAMED = ("valence", "span_reward", "span_sentiment", "span_character")     # the rows of directions_L{i}.npy
ALT = ("span_reward_fit", "span_sentiment_fit", "span_character_fit", "valence_uncentred")  # directions_alt_L{i}
GVEC_DIRS = ("span_character", "span_reward", "span_sentiment", "valence")  # the analyzer's --gvec set
A3_PRIMARY = "span_reward"                   # scripts/box_a3_extract.py's axis_report call
A3_GUARDS = {"v2_self": "span_character", "v3_eval": "span_sentiment"}     # scripts/box_a3_extract.py's GUARDS
POLES = ("+", "-", "0")
OUT_RECORD, OUT_COSINES = "gvec.json", "gvec_cosines.json"
SITE_RULE = ("ADDENDUM-n1 §6.1: the index within 2% of 25.49; the nearer in R if both, an exact tie to 32; neither a "
             "STOP")


def directions_file(index: int) -> str:
    return f"directions_L{int(index)}.npy"


def alt_file(index: int) -> str:
    return f"directions_alt_L{int(index)}.npy"


# --- the passages ---------------------------------------------------------------------------------------------------
def passage_groups(records: Sequence[Mapping]) -> dict:
    """The pole masks over the passages, the corpus checked against BK's eight states through ``directions.bk_state``:
    56 per state on its pole, 96 neutral, and nothing else."""
    want = {("+", s): directions.N_PER_STATE for s in directions.POSITIVE_STATES}
    want.update({("-", s): directions.N_PER_STATE for s in directions.NEGATIVE_STATES})
    want[("0", directions.NEUTRAL)] = directions.N_NEUTRAL
    got: dict = {}
    for r in records:
        key = (r["pole"], directions.bk_state(r["state"]))
        got[key] = got.get(key, 0) + 1
    if got != want:
        raise SystemExit("the passages are not BK's eight states at 56 each on their poles and 96 neutral: "
                         f"{sorted((k, v) for k, v in got.items() if want.get(k) != v)[:4]}")
    poles = np.array([r["pole"] for r in records])
    return {p: poles == p for p in POLES}


def passage_captures(forward: Callable, records: Sequence[Mapping], indices: Sequence[int]) -> dict:
    """One forward per passage over its committed ids, capturing ``indices``: per index, the passages' token means
    [N, D] (float64), the sums of their tokens' squared norms [N] and their token counts [N]."""
    idx = tuple(int(i) for i in indices)
    means: dict = {i: [] for i in idx}
    sq: dict = {i: [] for i in idx}
    ntok = []
    for rec in records:
        ids = [int(t) for t in rec["ids"]]
        if not ids:
            raise SystemExit(f"passage {rec['id']}: no ids")
        acts = forward(ids, idx)
        for i in idx:
            h = np.asarray(acts[i]).astype(np.float64)
            if h.shape[0] != len(ids):
                raise SystemExit(f"passage {rec['id']}: {h.shape[0]} captured rows for {len(ids)} ids at {i}")
            means[i].append(directions.passage_mean(h))
            sq[i].append(float(np.sum(h * h)))
        ntok.append(len(ids))
    return {"indices": idx, "means": {i: np.stack(means[i]) for i in idx},
            "sq": {i: np.asarray(sq[i], np.float64) for i in idx}, "ntok": np.asarray(ntok, np.int64)}


def r_at(cap: Mapping, neutral: np.ndarray, index: int) -> float:
    """R at ``index``: the RMS residual norm over the neutral passages' tokens (n §0.8; ``directions.rms_norm``)."""
    return directions.rms_norm(cap["sq"][int(index)][neutral], cap["ntok"][neutral])


def choose_site(r_by_index: Mapping[int, float], reference: float = R_REFERENCE, tol: float = R_TOLERANCE) -> dict:
    """ADDENDUM-n1 §6.1: the index whose R is within ``tol`` of ``reference`` (|R / reference - 1| <= tol); the nearer
    if more than one is, an exact tie to the higher index (G2); none within is a STOP for the seat."""
    rel = {int(i): abs(float(r) / float(reference) - 1.0) for i, r in r_by_index.items()}
    within = {i: rel[i] <= tol for i in rel}
    ok = [i for i in rel if within[i]]
    if not ok:
        return {"status": "STOP", "site": None, "rel": rel, "within": within}
    return {"status": "PASS", "site": min(ok, key=lambda i: (rel[i], -i)), "rel": rel, "within": within}


def valence_uncentred(pos_means, neg_means, neutral_means) -> np.ndarray:
    """G1's hedge (the review's O1), descriptive: v with U the ten leading right singular vectors of the 96 neutral
    means taken uncentred -- the clause of G1 the R check cannot test."""
    X = np.asarray(neutral_means, np.float64)
    _u, _s, vt = np.linalg.svd(X, full_matrices=False)
    U = vt[:directions.N_PCS]
    diff = np.asarray(pos_means, np.float64).mean(axis=0) - np.asarray(neg_means, np.float64).mean(axis=0)
    return diff - U.T @ (U @ diff)


def valence_at(cap: Mapping, groups: Mapping, index: int) -> dict:
    """BK's recipe at ``index`` (``directions.valence_direction``), with the sha16 of the ten neutral PCs and v under an
    uncentred U (``valence_uncentred``)."""
    m = cap["means"][int(index)]
    out = directions.valence_direction(m[groups["+"]], m[groups["-"]], m[groups["0"]])
    out["U_sha16"] = sha16_arr(directions.neutral_pcs(m[groups["0"]]))
    out["v_uncentred"] = valence_uncentred(m[groups["+"]], m[groups["-"]], m[groups["0"]])
    return out


# --- A3 on the committed ids ----------------------------------------------------------------------------------------
def a3_capture(forward: Callable, records: Sequence[Mapping], indices: Sequence[int]) -> extract.CaptureResult:
    """``extract.capture`` on the committed ids: one forward per context; at each index, the span-mean and the
    final-position residuals and the mean span-token L2 norm, the span from the record's ``span_start``; R_l the mean
    over contexts. The same float64 operations, in the same order, as ``extract.capture``."""
    layers = tuple(int(l) for l in indices)
    span_rows, last_rows, span_norms, span_lens = [], [], {l: [] for l in layers}, []
    conds, items = [], []
    for rec in records:
        ids = [int(t) for t in rec["ids"]]
        k, S = int(rec["span_start"]), len(ids)
        if not 0 < k < S:
            raise ValueError(f"degenerate span for {rec['item_id']}/{rec['condition']}: boundary {k} of {S} tokens")
        acts = forward(ids, layers)
        per_span, per_last = [], []
        for l in layers:
            h = np.asarray(acts[l]).astype(np.float64)
            sp = h[k:, :]
            per_span.append(sp.mean(axis=0))
            per_last.append(h[S - 1, :])
            span_norms[l].append(float(np.linalg.norm(sp, axis=1).mean()))
        span_rows.append(np.stack(per_span))
        last_rows.append(np.stack(per_last))
        conds.append(rec["condition"])
        items.append(rec["item_id"])
        span_lens.append(S - k)
    return extract.CaptureResult(
        span=np.stack(span_rows), last=np.stack(last_rows), conditions=np.array(conds), item_ids=np.array(items),
        layers=layers, resid_norms={l: float(np.mean(span_norms[l])) for l in layers}, span_lens=tuple(span_lens))


def n2_axes(cap: extract.CaptureResult, axis_conditions: Mapping, axis_order: Sequence[str]) -> dict:
    """A3's family: name -> [n_layers, D], mean(pos) - mean(neg) over every context of each condition, unnormalized."""
    return {name: extract.mean_diff_axis(cap, *axis_conditions[name], variant="span") for name in axis_order}


def subset(cap: extract.CaptureResult, item_ids: Sequence[str]) -> extract.CaptureResult:
    """The contexts of the given items (G6's fit-only figures); its R_l is not recomputed (empty)."""
    keep = np.isin(cap.item_ids, list(item_ids))
    return extract.CaptureResult(span=cap.span[keep], last=cap.last[keep], conditions=cap.conditions[keep],
                                 item_ids=cap.item_ids[keep], layers=cap.layers, resid_norms={},
                                 span_lens=tuple(int(x) for x in np.asarray(cap.span_lens)[keep]))


def guard_profile(cap: extract.CaptureResult, axes: Mapping) -> list:
    """A3's guard profile (``extract.axis_report``, its primary and guards as box_a3_extract.py has them),
    descriptive (g:167)."""
    return [dataclasses.asdict(r) for r in extract.axis_report(cap, axes, primary=A3_PRIMARY, guards=A3_GUARDS)]


# --- the directions, their files and cosines -----------------------------------------------------------------------
def injection_sha16(u) -> str:
    """The sha16 the Injection gives a direction (``adapters.base.Injection``: u / ||u|| in float64, hashed as float32):
    the campaign's ``expect_sha``."""
    return Injection(u=np.asarray(u), layer=0, alpha=0.0).direction_sha


def unit32(v) -> np.ndarray:
    """The stored row of a direction: v / ||v|| in float64, as float32, then re-normalized as the Injection would until
    the row is a fixed point of that normalization, so that ``sha16_arr`` of the row is the Injection's sha16 of it (the
    review's F2). A row with no fixed point within four passes is refused."""
    a = np.asarray(v, np.float64)
    n = float(np.linalg.norm(a))
    if not (n > 0 and math.isfinite(n)):
        raise ValueError("a direction with zero or non-finite norm")
    r = (a / n).astype(np.float32)
    for _ in range(4):
        r64 = r.astype(np.float64)
        nxt = (r64 / float(np.linalg.norm(r64))).astype(np.float32)
        if np.array_equal(nxt, r):
            break
        r = nxt
    else:
        raise ValueError("a direction whose float32 row is not a fixed point of the Injection's normalization")
    if sha16_arr(r) != injection_sha16(r):
        raise ValueError("a stored row whose sha16 is not the Injection's")
    return r


def cosines_of(rows: Mapping[str, np.ndarray]) -> dict:
    return directions.cosines({k: np.asarray(v, np.float64) for k, v in rows.items()})


def analyzer_cosines(rows: Mapping[str, np.ndarray]) -> dict:
    """The analyzer's --gvec file: {"cosines": {"x|y": float}}, exactly the six pairs of GVEC_DIRS."""
    c = cosines_of({k: rows[k] for k in GVEC_DIRS})
    want = {f"{x}|{y}" for i, x in enumerate(GVEC_DIRS) for y in GVEC_DIRS[i + 1:]}
    if set(c) != want or not all(math.isfinite(v) for v in c.values()):
        raise ValueError("the analyzer's cosines are not the six finite pairs of GVEC_DIRS")
    return {"cosines": c}


def random_rows(d_model: int) -> dict:
    """The 24 random directions (``keys.random_directions``), by the schema's ids."""
    rr = keys.random_directions(int(d_model))
    return {rid: rr[i] for i, rid in enumerate(schema.RANDOM_IDS)}


def _dumps(obj) -> str:
    return json.dumps(obj, sort_keys=True, indent=1, allow_nan=False) + "\n"


def _finite(x) -> float:
    f = float(x)
    if not math.isfinite(f):
        raise ValueError("a non-finite figure")
    return f


def token_table(passages: Sequence[Mapping], ntok: Sequence[int]) -> dict:
    """The passages' token counts per state, keyed by BK's state names (G11), with the corpus's spelling where it
    differs (the seat's corpus-adoption answers, §1.2: "a token count G-VEC's raw will print per state")."""
    per: dict = {}
    for rec, n in zip(passages, ntok):
        per.setdefault(rec["state"], []).append(int(n))
    out = {}
    for s, v in sorted(per.items()):
        row = {"n": len(v), "min": min(v), "mean": _finite(np.mean(v)), "max": max(v)}
        if directions.bk_state(s) != s:
            row["corpus_state"] = s
        out[directions.bk_state(s)] = row
    return out


# --- the stage, model-agnostic: ``forward(ids, indices) -> {index: [S, D] residuals}`` -----------------------------
def compute(forward: Callable, passages: Sequence[Mapping], contexts: Sequence[Mapping], *, a3: Mapping,
            d_model: int, indices: Sequence[int] = CANDIDATE_INDICES, reference: float = R_REFERENCE,
            say: Callable = print) -> dict:
    """G-VEC's figures and rows. ``a3``: A3's ``axis_conditions``, ``axis_order``, ``fit_ids`` and ``val_ids`` (from
    scripts/box_e0_corpus.py). Returns {"status", "figures", "rows", "alt_rows"}: on a STOP (R within 2% at no index)
    the figures end at R and nothing else is computed; the rows map index -> name -> float32 unit row."""
    idx = tuple(int(i) for i in indices)
    if tuple(a3["axis_order"]) != NAMED[1:]:
        raise SystemExit(f"A3's axis order {tuple(a3['axis_order'])} is not the named rows' {NAMED[1:]}")
    groups = passage_groups(passages)
    say(f"passages: {len(passages)} (224 positive, 224 negative, 96 neutral), one forward each, captured at {idx}")
    pc = passage_captures(forward, passages, idx)
    r = {i: r_at(pc, groups["0"], i) for i in idx}
    site = choose_site(r, reference)
    tokens = token_table(passages, pc["ntok"].tolist())
    figures: dict = {
        "passages": {"n": len(passages), "tokens": tokens, "neutral_tokens": int(pc["ntok"][groups["0"]].sum())},
        "site": {"indices": list(idx), "R": {str(i): _finite(r[i]) for i in idx},
                 "rel": {str(i): _finite(site["rel"][i]) for i in idx},
                 "within": {str(i): bool(site["within"][i]) for i in idx}, "reference": float(reference),
                 "tolerance": R_TOLERANCE, "site": site["site"], "status": site["status"], "rule": SITE_RULE},
        "bk": {"resid_rms": R_BK_RECORD, "pole_l2": POLE_L2_BK},
        "fit_ids": list(a3["fit_ids"]), "val_ids": list(a3["val_ids"]),
    }
    for s, t in tokens.items():
        say(f"tokens, {s}: {t['n']} passages, min {t['min']}, mean {t['mean']:.2f}, max {t['max']}")
    for i in idx:
        say(f"R at index {i}: {r[i]!r} (|R/{reference} - 1| = {site['rel'][i]!r}; "
            f"{'within' if site['within'][i] else 'outside'} 2%)")
    if site["status"] != "PASS":
        say("G-VEC STOP: R is within 2% of 25.49 at neither candidate index (n §2.3: \"else STOP\"); the seat rules")
        return {"status": "STOP", "figures": figures, "rows": {}, "alt_rows": {}}
    s = site["site"]
    say(f"site: index {s} (ADDENDUM-n1 §6.1)")
    rows: dict = {i: {} for i in idx}
    alt: dict = {i: {} for i in idx}
    val: dict = {}
    for i in idx:
        v = valence_at(pc, groups, i)
        rows[i]["valence"] = unit32(v["unit"])
        alt[i]["valence_uncentred"] = unit32(v["v_uncentred"])
        val[str(i)] = {"norm_v": _finite(v["norm_v"]), "norm_diff": _finite(v["norm_diff"]),
                       "removed_fraction": _finite(v["removed_fraction"]),
                       "sha16": injection_sha16(rows[i]["valence"]), "U_sha16": v["U_sha16"],
                       "uncentred": {"norm_v": _finite(np.linalg.norm(v["v_uncentred"])),
                                     "sha16": injection_sha16(alt[i]["valence_uncentred"]),
                                     "cos_v": cosines_of({"a": v["v"], "b": v["v_uncentred"]})["a|b"]}}
    figures["valence"] = val
    say(f"contexts: {len(contexts)} (A3's frozen corpus), one forward each, captured at {idx}")
    cap = a3_capture(forward, contexts, idx)
    axes = n2_axes(cap, a3["axis_conditions"], a3["axis_order"])
    fit = n2_axes(subset(cap, a3["fit_ids"]), a3["axis_conditions"], a3["axis_order"])
    guards = guard_profile(cap, axes)
    a3_fig: dict = {"n_contexts": len(contexts), "axis_conditions": {k: list(v) for k, v in
                                                                     a3["axis_conditions"].items()},
                    "axis_order": list(a3["axis_order"]),
                    "span_len": [min(cap.span_lens), max(cap.span_lens), _finite(np.mean(cap.span_lens))],
                    "R_ell": {str(l): _finite(cap.resid_norms[l]) for l in idx}, "axes": {}, "freeze_sha": {},
                    "fit_only": {}, "guards": {},
                    "R_ell_cross_check": {"available": False, "note": "no step-2 survey exists for this checkpoint "
                                                                      "(OLMo-2 Instruct): G5"}}
    for li, l in enumerate(idx):
        for name in a3["axis_order"]:
            rows[l][name] = unit32(axes[name][li])
            alt[l][f"{name}_fit"] = unit32(fit[name][li])
        a3_fig["axes"][str(l)] = {name: {"norm": _finite(np.linalg.norm(axes[name][li])),
                                         "sha16": injection_sha16(rows[l][name])} for name in a3["axis_order"]}
        a3_fig["freeze_sha"][str(l)] = extract.freeze_sha({k: v[li] for k, v in axes.items()}, a3["axis_order"])
        a3_fig["fit_only"][str(l)] = {name: {"norm": _finite(np.linalg.norm(fit[name][li])),
                                             "sha16": injection_sha16(alt[l][f"{name}_fit"]),
                                             "cos_all": cosines_of({"a": fit[name][li], "b": axes[name][li]})["a|b"]}
                                      for name in a3["axis_order"]}
        a3_fig["guards"][str(l)] = [g for g in guards if g["layer"] == l]
        say(f"R_ell at index {l}: {cap.resid_norms[l]!r}; N2's norms "
            + ", ".join(f"{n} {np.linalg.norm(axes[n][li]):.6g}" for n in a3["axis_order"]))
    figures["a3"] = a3_fig
    rand = random_rows(d_model)
    allrows = dict(rows[s])
    allrows.update(rand)
    figures["random_sha16"] = {k: injection_sha16(v) for k, v in rand.items()}
    figures["cosines"] = {"named": analyzer_cosines(rows[s])["cosines"], "all": cosines_of(allrows)}
    figures["directions"] = {"order": list(NAMED), "alt_order": list(ALT),
                             "files": {str(i): directions_file(i) for i in idx},
                             "alt_files": {str(i): alt_file(i) for i in idx},
                             "sha16": {str(i): {n: injection_sha16(rows[i][n]) for n in NAMED} for i in idx},
                             "alt_sha16": {str(i): {n: injection_sha16(alt[i][n]) for n in ALT} for i in idx},
                             "route": ROUTE, "route_line": ROUTE_LINE}
    figures["of_record"] = {"site": s, "R": _finite(r[s]), "R_ell": _finite(cap.resid_norms[s]),
                            "directions": {n: injection_sha16(rows[s][n]) for n in NAMED}, "route_line": ROUTE_LINE}
    for k, v in figures["cosines"]["named"].items():
        say(f"cosine {k}: {v!r}")
    return {"status": "PASS", "figures": figures, "rows": rows, "alt_rows": alt}


def record(result: Mapping, provenance: Mapping, file_shas: Mapping, status: str | None = None) -> dict:
    """The record of ``gvec.json``: the figures, the provenance the driver measured, and the other files' sha256s; its
    split at the top level, as A3's artifacts carry it, asserted (``extract.assert_stage_splits``)."""
    rec = {"schema": RECORD_SCHEMA, "stage": STAGE, "status": status or result["status"],
           "proposal_sha256": schema.PROPOSAL_SHA256, **result["figures"], "provenance": dict(provenance),
           "files_sha256": dict(file_shas)}
    extract.assert_stage_splits(rec, where=OUT_RECORD)
    return rec


def write(out_dir, result: Mapping, provenance: Mapping, status: str | None = None) -> dict:
    """The outputs into ``out_dir`` (which the driver has staged): on a PASS, the four directions files and the
    analyzer's cosines file, then the record with their sha256s; on a STOP, the record alone. Returns the record."""
    d = Path(out_dir)
    shas: dict = {}
    if result["status"] == "PASS":
        for kind, names, fname, by in (("named", NAMED, directions_file, result["rows"]),
                                       ("alt", ALT, alt_file, result["alt_rows"])):
            for i, rows in sorted(by.items()):
                arr = np.stack([rows[n] for n in names]).astype(np.float32)
                p = d / fname(i)
                with open(p, "wb") as fh:
                    np.save(fh, arr, allow_pickle=False)
                shas[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
        site = result["figures"]["site"]["site"]
        cp = d / OUT_COSINES
        cp.write_text(_dumps(analyzer_cosines(result["rows"][site])), encoding="utf-8")
        shas[cp.name] = hashlib.sha256(cp.read_bytes()).hexdigest()
    rec = record(result, provenance, shas, status)
    (d / OUT_RECORD).write_text(_dumps(rec), encoding="utf-8")
    return rec


def read_rows(path, n_rows: int = len(NAMED)) -> np.ndarray:
    """A directions file's rows ([n_rows, D] float32, ``NAMED``'s or ``ALT``'s order)."""
    arr = np.load(Path(path), allow_pickle=False)
    if arr.dtype != np.float32 or arr.ndim != 2 or arr.shape[0] != int(n_rows):
        raise ValueError(f"{path}: not a [{n_rows}, D] float32 directions file")
    return arr


# --- self-test -------------------------------------------------------------------------------------------------------
BK_ANALYSIS = (Path(__file__).resolve().parents[2] / "data" / "n" / "bk" / "experiment_results_json"
               / "fixed_text_design" / "strength_ladder" / "analysis.json")


def _toy_passages(rng, vocab: int) -> list:
    out, k = [], 0
    for pole, states, n in (("+", directions.POSITIVE_STATES, directions.N_PER_STATE),
                            ("-", directions.NEGATIVE_STATES, directions.N_PER_STATE),
                            ("0", (directions.NEUTRAL,), directions.N_NEUTRAL)):
        for s in states:
            name = directions.CORPUS_STATE.get(s, s)
            for j in range(n):
                ln = int(rng.integers(3, 7))
                ids = [int(x) for x in rng.integers(3, vocab, ln)]
                if pole == "+":
                    ids[0] = 5                           # a token the positive passages share
                if pole == "-":
                    ids[0] = 9
                out.append({"index": k, "id": f"{name}-{j:02d}", "state": name, "pole": pole, "ids": ids})
                k += 1
    return out


def _toy_contexts(rng, vocab: int, conditions, items) -> tuple:
    recs, ctxs, table = [], [], {}
    for it in items:
        prefix = [int(x) for x in rng.integers(3, vocab, int(rng.integers(4, 7)))]
        for c in conditions:
            span = [int(x) for x in rng.integers(3, vocab, int(rng.integers(2, 5)))]
            ptxt, ftxt = f"P|{it}", f"P|{it}|{c}"
            table[ptxt], table[ftxt] = prefix, prefix + span
            ctxs.append(extract.Context(prefix=ptxt, full=ftxt, condition=c, item_id=it, variant=0))
            recs.append({"item_id": it, "condition": c, "ids": prefix + span, "span_start": len(prefix)})
    return recs, ctxs, table


def _selftest(chk, tmp) -> None:
    import re
    import types

    from .testing import CausalDouble
    tmp = Path(tmp)
    be = CausalDouble(d_model=32)                    # at least 24: the random directions are orthonormal rows
    rng = np.random.default_rng(29)
    L = (3, 4)                                       # the double's stand-ins for 31 and 32

    def fwd(ids, layers):
        return be.forward_all(ids, layers)
    ps = _toy_passages(rng, be.vocab)
    groups = passage_groups(ps)
    chk("gvec: the corpus's composition, BK's eight states through bk_state (flow_engagement among them), 56 each, "
        "96 neutral", int(groups["+"].sum()) == 224 and int(groups["-"].sum()) == 224 and int(groups["0"].sum()) == 96,
        "")
    try:
        passage_groups(ps[:-1])
        chk("gvec: a corpus short of one neutral passage is refused", False, "accepted")
    except SystemExit:
        chk("gvec: a corpus short of one neutral passage is refused", True, "")
    bad = [dict(p) for p in ps]
    bad[0]["pole"] = "-"
    try:
        passage_groups(bad)
        chk("gvec: a passage on the wrong pole for its state is refused", False, "accepted")
    except SystemExit:
        chk("gvec: a passage on the wrong pole for its state is refused", True, "")
    pc = passage_captures(fwd, ps, L)
    a0 = be.forward_all(ps[0]["ids"], L)
    h3 = a0[3].astype(np.float64)
    chk("gvec: a passage's mean is its tokens' mean at the index, its squared-norm sum and its token count",
        np.array_equal(pc["means"][3][0], h3.mean(axis=0)) and pc["ntok"][0] == len(ps[0]["ids"])
        and abs(pc["sq"][3][0] - float(np.sum(np.linalg.norm(h3, axis=1) ** 2))) <= 1e-12 * pc["sq"][3][0], "")
    neu = groups["0"]

    def r_direct(i):
        acts = [be.forward_all(p["ids"], L)[i].astype(np.float64) for p, n in zip(ps, neu) if n]
        return math.sqrt(sum(float(np.sum(a ** 2)) for a in acts) / sum(a.shape[0] for a in acts))
    want_r = {i: r_direct(i) for i in L}
    chk("gvec: R is the RMS over the neutral passages' tokens (pooled; n §0.8), at each index",
        all(abs(r_at(pc, neu, i) - want_r[i]) <= 1e-12 * want_r[i] for i in L), want_r)
    v = valence_at(pc, groups, 4)
    v2 = directions.valence_direction(pc["means"][4][groups["+"]], pc["means"][4][groups["-"]],
                                      pc["means"][4][groups["0"]])
    chk("gvec: v at an index is directions.valence_direction on the passages' means there, with U's sha16",
        np.array_equal(v["unit"], v2["unit"])
        and v["U_sha16"] == sha16_arr(directions.neutral_pcs(pc["means"][4][groups["0"]])), "")
    Xn = pc["means"][4][groups["0"]]
    _uu, _ss, vtu = np.linalg.svd(Xn, full_matrices=False)
    dd = pc["means"][4][groups["+"]].mean(axis=0) - pc["means"][4][groups["-"]].mean(axis=0)
    vu = dd - vtu[:10].T @ (vtu[:10] @ dd)
    chk("gvec: the uncentred variant is v with U from the uncentred neutral means (G1's hedge), orthogonal to them",
        np.allclose(v["v_uncentred"], vu, rtol=0, atol=1e-12) and float(np.max(np.abs(vtu[:10] @ v["v_uncentred"])))
        < 1e-10, "")
    ref = R_REFERENCE
    cases = [({31: ref * 1.03, 32: ref * 1.01}, ("PASS", 32)), ({31: ref * 1.005, 32: ref * 1.015}, ("PASS", 31)),
             ({31: ref * 0.99, 32: ref * 1.0199}, ("PASS", 31)), ({31: ref * 1.0201, 32: ref * 0.97}, ("STOP", None)),
             ({31: 25.6, 32: 25.6}, ("PASS", 32)), ({31: ref * 1.0201, 32: ref * 0.9799}, ("STOP", None)),
             ({31: ref * 1.019, 32: ref * 1.03}, ("PASS", 31))]
    got = [(choose_site(rr)["status"], choose_site(rr)["site"]) for rr, _w in cases]
    exact = choose_site({31: 5.0, 32: 100.0}, reference=4.0, tol=0.25)
    chk("gvec: the site rule (ADDENDUM-n1 §6.1): the index within 2% (R_TOLERANCE 0.02; a bar met exactly is within); "
        "the nearer if both; an exact tie to 32; neither a STOP",
        got == [w for _rr, w in cases] and R_TOLERANCE == 0.02 and (exact["status"], exact["site"]) == ("PASS", 31),
        got)
    # A3: the capture on committed ids equals extract.capture's on the same tokens (the double through an encode shim)
    conds = ("self_pos", "self_neg", "sent_pos", "sent_neg", "char_pos", "char_neg", "neutral")
    items = ("e01", "e02", "e25", "e26")
    recs, ctxs, table = _toy_contexts(rng, be.vocab, conds, items)
    shim = types.SimpleNamespace(encode=lambda text: list(table[text]),
                                 forward=lambda ids, capture_layers=(): types.SimpleNamespace(
                                     acts=be.forward_all(ids, capture_layers)))
    ref_cap = extract.capture(shim, ctxs, L, progress_every=0)
    cap = a3_capture(fwd, recs, L)
    chk("gvec: a3_capture on the committed ids equals extract.capture on the same tokens, exactly (span-means, "
        "last rows, R_l, span lengths, conditions, items)",
        np.array_equal(cap.span, ref_cap.span) and np.array_equal(cap.last, ref_cap.last)
        and cap.resid_norms == ref_cap.resid_norms and cap.span_lens == ref_cap.span_lens
        and list(cap.conditions) == list(ref_cap.conditions) and list(cap.item_ids) == list(ref_cap.item_ids)
        and cap.layers == ref_cap.layers, (cap.resid_norms, ref_cap.resid_norms))
    degenerate = []
    for k_ in (len(recs[0]["ids"]), 0):
        try:
            a3_capture(fwd, [dict(recs[0], span_start=k_)], L)
            degenerate.append(False)
        except ValueError:
            degenerate.append(True)
    chk("gvec: a context whose span is empty, or starts at token 0, is refused, as extract.capture refuses it",
        degenerate == [True, True], degenerate)
    ac = {"span_reward": ("self_pos", "self_neg"), "span_sentiment": ("sent_pos", "sent_neg"),
          "span_character": ("char_pos", "char_neg")}
    order = ("span_reward", "span_sentiment", "span_character")
    axes = n2_axes(cap, ac, order)
    chk("gvec: N2's family is extract.mean_diff_axis over every context of each condition, and its freeze_sha "
        "extract's", all(np.array_equal(axes[n], extract.mean_diff_axis(ref_cap, *ac[n])) for n in order)
        and extract.freeze_sha({k: v[1] for k, v in axes.items()}, order)
        == sha16_arr(np.stack([axes[n][1] for n in order])), "")
    fit = n2_axes(subset(cap, ("e01", "e02")), ac, order)
    keep = np.isin(cap.item_ids, ["e01", "e02"])
    manual = (cap.span[keep & (cap.conditions == "self_pos")].mean(axis=0)
              - cap.span[keep & (cap.conditions == "self_neg")].mean(axis=0))
    chk("gvec: the fit-only family uses the fit items' contexts alone (G6)", np.array_equal(fit["span_reward"], manual),
        "")
    gp = guard_profile(cap, axes)
    chk("gvec: the guard profile is extract.axis_report's with A3's primary span_reward and its guards v2_self -> "
        "span_character and v3_eval -> span_sentiment (box_a3_extract.py), per index",
        gp == [dataclasses.asdict(x) for x in extract.axis_report(
            cap, axes, primary="span_reward", guards={"v2_self": "span_character", "v3_eval": "span_sentiment"})]
        and [g["layer"] for g in gp] == list(L), "")
    u = unit32(v["v"])
    from ..adapters.base import Injection as _Inj
    chk("gvec: a stored row is float32, unit, a fixed point of the Injection's normalization, and its sha16 the "
        "Injection's (what the campaign's expect_sha checks)",
        u.dtype == np.float32 and abs(float(np.linalg.norm(u.astype(np.float64))) - 1.0) < 1e-6
        and sha16_arr(u) == _Inj.at_frac(u, 4, 0.1, {4: 1.0}).direction_sha == injection_sha16(u), "")
    chk("gvec: BK's literals are BK's: resid_rms and pole_l2 of every OLMo-2 meta at layer 32 in strength_ladder's "
        "analysis.json", _bk_literals_hold(), "")
    chk("gvec: the route is B, in PIN-n-26's line form (scripts/n_analyze.py's ROUTE_LINE and the route)",
        (ROUTE, ROUTE_LINE) == ("B", "direction of record: Route B"), "")
    # the stage end to end on the double, the reference set to its own R at index 4 (so 4 is the nearer)
    r4 = r_at(pc, neu, 4)
    lines: list = []
    a3 = {"axis_conditions": ac, "axis_order": order, "fit_ids": ("e01", "e02"), "val_ids": ("e25", "e26")}
    res = compute(fwd, ps, recs, a3=a3, d_model=be.d_model, indices=L, reference=r4, say=lines.append)
    f = res["figures"]
    chk("gvec: on the double the stage passes at the index within 2%, recording R at both indices, each its own",
        res["status"] == "PASS" and f["site"]["site"] == 4 and f["site"]["R"] == {"3": r_at(pc, neu, 3), "4": r4}
        and f["of_record"]["site"] == 4 and f["of_record"]["R"] == r4, f["site"])
    vsha = {str(i): injection_sha16(unit32(valence_at(pc, groups, i)["unit"])) for i in L}
    ax_ind = n2_axes(a3_capture(fwd, recs, L), ac, order)
    chk("gvec: each index's rows are that index's: valence and N2's three, against an independent computation",
        all(f["directions"]["sha16"][str(i)]["valence"] == vsha[str(i)] for i in L)
        and all(f["directions"]["sha16"][str(l)][n] == injection_sha16(unit32(ax_ind[n][li]))
                for li, l in enumerate(L) for n in order)
        and f["directions"]["sha16"]["3"] != f["directions"]["sha16"]["4"]
        and f["of_record"]["directions"] == f["directions"]["sha16"]["4"], "")
    chk("gvec: R_ell at both indices is a3_capture's, and the record's of_record is the site's",
        f["a3"]["R_ell"] == {str(l): a3_capture(fwd, recs, L).resid_norms[l] for l in L}
        and f["of_record"]["R_ell"] == f["a3"]["R_ell"]["4"], "")
    rand = keys.random_directions(be.d_model)
    chk("gvec: the random sha16s sit under their own ids (the Injection's sha16 of keys.random_directions' rows)",
        f["random_sha16"] == {rid: injection_sha16(rand[i]) for i, rid in enumerate(schema.RANDOM_IDS)}, "")
    fit_ind = n2_axes(subset(a3_capture(fwd, recs, L), ("e01", "e02")), ac, order)
    chk("gvec: the fit-only figures are the fit items' family (G6), and the guard profile is recorded at both indices",
        all(f["a3"]["fit_only"][str(l)][n]["norm"] == float(np.linalg.norm(fit_ind[n][li]))
            and f["a3"]["fit_only"][str(l)][n]["sha16"] == injection_sha16(unit32(fit_ind[n][li]))
            for li, l in enumerate(L) for n in order)
        and set(f["a3"]["guards"]) == {"3", "4"} and f["a3"]["R_ell_cross_check"]["available"] is False, "")
    tt = {}
    for p_, n_ in zip(ps, pc["ntok"].tolist()):
        tt.setdefault(directions.bk_state(p_["state"]), []).append(n_)
    chk("gvec: the token table is keyed by BK's names (flow engagement, its corpus spelling beside), each state's "
        "n, min, mean and max its passages'",
        set(f["passages"]["tokens"]) == set(tt) and f["passages"]["tokens"]["flow engagement"]["corpus_state"]
        == "flow_engagement" and all((t["n"], t["min"], t["max"]) == (len(tt[s_]), min(tt[s_]), max(tt[s_]))
                                     for s_, t in f["passages"]["tokens"].items()), "")
    chk("gvec: the cosines: the analyzer's six pairs at the site, its own rows', and 378 among all 28",
        f["cosines"]["named"] == directions.cosines({k: res["rows"][4][k].astype(np.float64) for k in GVEC_DIRS})
        and len(f["cosines"]["all"]) == 378 and len(f["random_sha16"]) == 24, len(f["cosines"]["all"]))
    ids_seen = [x for x in lines if any(p["id"] in x for p in ps) or re.search(r"\[\d+, \d+", x)]
    chk("gvec: the stage prints R, the site, each state's token counts and the cosines, never a passage or an id list",
        any(x.startswith("site: index 4") for x in lines) and any(x.startswith("tokens, flow engagement:")
                                                                 for x in lines) and not ids_seen, ids_seen[:2])
    out = tmp / "out"
    out.mkdir(parents=True)
    rec = write(out, res, {"note": "selftest"})
    back = {i: read_rows(out / directions_file(i)) for i in L}
    back_alt = {i: read_rows(out / alt_file(i), len(ALT)) for i in L}
    shas_ok = all(rec["files_sha256"][p.name] == hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in out.iterdir() if p.name != OUT_RECORD)
    chk("gvec: the files: four directions files, the analyzer's cosines file, and the record with their sha256s and "
        "A3's split at its top level",
        sorted(p.name for p in out.iterdir()) == sorted([OUT_RECORD, OUT_COSINES] + [directions_file(i) for i in L]
                                                        + [alt_file(i) for i in L])
        and shas_ok and json.loads((out / OUT_RECORD).read_text())["status"] == "PASS"
        and rec["fit_ids"] == ["e01", "e02"] and rec["val_ids"] == ["e25", "e26"], "")
    chk("gvec: each stored row reads back with its recorded sha16, the named and the alternative",
        all(sha16_arr(back[i][j]) == rec["directions"]["sha16"][str(i)][n] for i in L for j, n in enumerate(NAMED))
        and all(sha16_arr(back_alt[i][j]) == rec["directions"]["alt_sha16"][str(i)][n]
                for i in L for j, n in enumerate(ALT)), "")
    cos = json.loads((out / OUT_COSINES).read_text())
    chk("gvec: the cosines file is the analyzer's form, its values the site's rows' as read back",
        list(cos) == ["cosines"] and cos["cosines"] == f["cosines"]["named"]
        == directions.cosines({n: back[4][j].astype(np.float64) for j, n in enumerate(NAMED) if n in GVEC_DIRS}), "")
    res_stop = compute(fwd, ps, recs, a3=a3, d_model=be.d_model, indices=L, reference=1.0e6, say=lambda *_: None)
    out2 = tmp / "stop"
    out2.mkdir()
    rec2 = write(out2, res_stop, {"note": "selftest"})
    chk("gvec: a STOP computes no direction and writes the record alone, its R at both indices, each its own",
        res_stop["status"] == "STOP" and res_stop["rows"] == {} and [p.name for p in out2.iterdir()] == [OUT_RECORD]
        and rec2["status"] == "STOP" and "valence" not in rec2
        and rec2["site"]["R"] == {"3": r_at(pc, neu, 3), "4": r4}, "")
    try:
        compute(fwd, ps, recs, a3=dict(a3, axis_order=("span_sentiment", "span_reward", "span_character")),
                d_model=be.d_model, indices=L, reference=r4, say=lambda *_: None)
        chk("gvec: an A3 axis order other than the named rows' is refused before any forward", False, "accepted")
    except SystemExit:
        chk("gvec: an A3 axis order other than the named rows' is refused before any forward", True, "")


def _bk_literals_hold() -> bool:
    """BK's resid_rms and pole_l2 at layer 32, read from the committed analysis.json (the member is selected by its
    prefix, so no model name is written here twice)."""
    inst = json.loads(BK_ANALYSIS.read_text(encoding="utf-8"))["instrument"]
    member = [k for k in inst if k.startswith("ol")]
    if len(member) != 1:
        return False
    vals = {(m["resid_rms"], m["pole_l2"], m["layer"]) for m in inst[member[0]]["metas"]}
    return vals == {(R_BK_RECORD, POLE_L2_BK, 32)}
