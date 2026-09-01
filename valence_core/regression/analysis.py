"""Model-free half of the ledger-26 suite: every published number that can
be recomputed from a committed artifact, recomputed through `valence_core`.

    uv run python -m valence_core.regression.analysis      (or any python)

Each check names the document it is holding the port to, so a failure says
which claim just stopped reproducing rather than merely that something
moved. Every input is in the repo (ledger 27) -- this suite does not read
the gitignored clone, which is the point: it must run on the box.

Deliberately NOT in here: anything requiring a forward pass. Those are the
three oracle criteria and they run on the laptop.
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass

import numpy as np

from ..gate import matched_pair_swing
from ..stats import binom_test_exact, fisher_one_sided
from ..adapters.base import sha16_arr

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(REPO, "data")

TOL = 5e-5


@dataclass
class Check:
    name: str
    source: str
    expected: str
    got: str
    ok: bool


def _c(name, source, expected, got, ok) -> Check:
    return Check(name, source, str(expected), str(got), bool(ok))


def check_frozen_shas() -> list[Check]:
    """Rule 1: the direction artifacts every published dose was computed
    from are the ones in the record."""
    out = []
    Z = np.load(os.path.join(DATA, "e0/e0_axes.npz"))
    stack = np.stack([Z["span_reward"], Z["span_sentiment"], Z["span_character"]])
    got = sha16_arr(stack)
    out.append(_c("e0 axes sha", "e2a.AXES_SHA", "d4791bdc4877da3d", got,
                  got == "d4791bdc4877da3d"))
    layers = [int(x) for x in Z["layers"]]
    R = np.load(os.path.join(DATA, "e0/e0_random_dirs.npz"))
    gotr = sha16_arr(np.stack([R[f"L{L}"] for L in layers]))
    out.append(_c("e0 random-dirs sha", "e2a.RAND_SHA", "b6bd2f5f580ee13e",
                  gotr, gotr == "b6bd2f5f580ee13e"))
    out.append(_c("workspace layers", "workspace_layers.WORKSPACE_LAYERS",
                  [40, 44, 48, 52, 56, 60], layers,
                  layers == [40, 44, 48, 52, 56, 60]))
    return out


def check_screen_pvalues() -> list[Check]:
    """FINDINGS-4 summary ledger: five contrasts, five p-values. `delta` is
    stored as (share - 0.5), so the count is recoverable exactly."""
    path = os.path.join(DATA, "f/screen_analysis.json")
    contrasts = json.load(open(path))["contrasts"]
    out = []
    for arm, c in contrasts.items():
        n = int(c["n"])
        k = round((c["delta"] + 0.5) * n)
        alt = "two-sided" if c["sided"] == "two" else "greater"
        p = binom_test_exact(k, n, 0.5, alternative=alt)
        out.append(_c(f"screen p [{arm}] {k}/{n}", "FINDINGS-4 summary ledger",
                      f"{c['p']:.5f}", f"{p:.5f}", abs(p - c["p"]) < TOL))
    return out


def check_postscreen_descriptives() -> list[Check]:
    """FINDINGS-4 §7 and the post-screen descriptive entry."""
    out = []
    p = fisher_one_sided(7, 1, 2, 5)
    out.append(_c("CORR exclusion asymmetry (post-hoc, weightless)",
                  "FINDINGS-4 §7", "0.035", f"{p:.3f}", round(p, 3) == 0.035))
    p = binom_test_exact(128, 257, 0.5)
    out.append(_c("brevity-tracking pooled 128/257", "FINDINGS-4 §6",
                  "1.0", f"{p:.4f}", abs(p - 1.0) < 1e-9))
    p = binom_test_exact(23, 44, 0.5)
    out.append(_c("FDBK first-choice 23/44 = .523", "FINDINGS-4 §3",
                  "n.s.", f"p={p:.3f}", p > 0.05))
    return out


def check_c1r3_gate() -> list[Check]:
    """FINDINGS-2 finding 3 + the r3 confirmatory verdict."""
    pa, pb = (os.path.join(DATA, f"configs/c1r3_gate_rep{r}.json") for r in "AB")
    if not (os.path.exists(pa) and os.path.exists(pb)):
        return [_c("c1r3 matched-pair swing", "FINDINGS-2 finding 3",
                   "gate JSONs present", "MISSING from the record", False)]
    A, B = json.load(open(pa)), json.load(open(pb))
    hi, lo = (A, B) if A["assignment"]["C"] == "hi" else (B, A)
    r = matched_pair_swing(hi, lo)
    return [
        _c("c1r3 control pairs", "rule 9 (28 standard)", 28, r.n_pairs,
           r.n_pairs == 28),
        _c("c1r3 z (descriptive)", "FINDINGS-2 finding 3 (28 said 1.6)",
           "1.6", f"{r.z_descriptive:.1f}", abs(r.z_descriptive - 1.6) < 0.05),
        _c("c1r3 verdict", "r3 confirmatory FAIL", "FAIL",
           "PASS" if r.passed else "FAIL", r.passed is False),
    ]


def check_axis_geometry() -> list[Check]:
    """e0_axes.meta.json's per-layer report: the V2/V3 guard decompositions
    and axis cosines that licensed the reward axis as a drug (PROPOSAL-e).
    24 published values -- 6 workspace layers x 4 quantities."""
    from ..extract import cosine, residual_fraction
    Z = np.load(os.path.join(DATA, "e0/e0_axes.npz"))
    meta = json.load(open(os.path.join(DATA, "e0/e0_axes.meta.json")))
    out = []
    for li, row in enumerate(meta["report"]["span"]):
        rw = Z["span_reward"][li]
        se = Z["span_sentiment"][li]
        ch = Z["span_character"][li]
        for label, got, exp in (
                ("cos reward.sentiment", cosine(rw, se), row["cos_reward_sentiment"]),
                ("cos reward.character", cosine(rw, ch), row["cos_reward_character"]),
                ("V2 self-residual", residual_fraction(rw, ch), row["v2_self_residual_frac"]),
                ("V3 eval-residual", residual_fraction(rw, se), row["v3_eval_residual_frac"])):
            out.append(_c(f"L{row['layer']} {label}", "e0_axes.meta.json report",
                          f"{exp:.3f}", f"{got:.3f}", round(got, 3) == exp))
    return out


def check_tripwire_firing() -> list[Check]:
    """`f_sessions.unit_check_bars()` reproduced through the ported bar
    machinery -- the pre-committed firing check from the smoke2r
    adjudication (commit eb0f33b), which is where the lexical bar was moved
    from a ratio form to an exact binomial vs p0 = .05.

    The 1/12 case is the whole point: under the old ratio form it fired on a
    true header-to-prose priming specimen; the binomial form does not.
    """
    from ..session import Tripwire, verify_firing
    bars = [
        Tripwire("LEXICAL", "binomial", p0=0.05, alpha=0.05, min_n=1,
                 domain="all"),
        Tripwire("AUDIT", "hair_trigger", threshold=0.20, min_n=6,
                 domain="sham+P",
                 justification="audit-degenerate output has ~zero healthy "
                               "base rate on unprovoked domains"),
        Tripwire("CAP", "hair_trigger", threshold=0.10, min_n=10,
                 domain="sham+P",
                 justification="cap-hit-without-newline is ~zero base rate "
                               "on unprovoked domains"),
    ]
    cases = [("LEXICAL", 3, 12, True), ("LEXICAL", 1, 12, False),
             ("AUDIT", 2, 6, True), ("CAP", 2, 10, True),
             ("AUDIT", 1, 8, False), ("CAP", 1, 20, False)]
    failures = verify_firing(bars, cases)
    out = [_c("bar firing behavior (6 cases)", "f_sessions.unit_check_bars",
              "no failures", failures or "no failures", not failures)]

    # rule 21 refuses an unjustified hair-trigger bar at declaration time
    try:
        Tripwire("BAD", "hair_trigger", threshold=0.1)
        ok, got = False, "accepted"
    except ValueError:
        ok, got = True, "refused"
    out.append(_c("hair-trigger needs justification", "rule 21",
                  "refused", got, ok))
    return out


def check_feature_definition() -> list[Check]:
    """Rule 28(a) against the real f1 post-screen artifact.

    Three published features, three verdicts the machinery must return:
    `fewer_degen_rounds` tied on all 283 valid sessions (n = 0 decidable)
    and is structurally undefined; `fewer_preamble_trunc` survived with
    n = 5 of 283 and is below any sane share floor; `shorter_rounds`
    had n = 257 and is usable. FINDINGS-4 §6 reports exactly this.
    """
    from ..session import FeatureSpec, check_feature_defined
    d = json.load(open(os.path.join(DATA, "f/postscreen_descriptive.json")))
    feats = d["features"]
    out = []

    def domain_n(f):
        pooled = feats[f]["pooled"]
        return int(pooled["n"] or 0), int(pooled["n"] or 0) + feats[f]["ties_dropped"]

    n_dec, n_dom = domain_n("fewer_degen_rounds")
    diag = check_feature_defined(FeatureSpec("fewer_degen_rounds"), n_dec, n_dom)
    out.append(_c("degen-round feature undefined post-exclusion",
                  "FINDINGS-4 §6 / methodological 5",
                  "0 decidable of 283", f"{n_dec} decidable of {n_dom}",
                  n_dec == 0 and n_dom == 283 and diag is not None
                  and "STRUCTURALLY UNDEFINED" in diag))

    n_dec, n_dom = domain_n("fewer_preamble_trunc")
    diag = check_feature_defined(
        FeatureSpec("fewer_preamble_trunc", min_decidable_frac=0.05),
        n_dec, n_dom)
    out.append(_c("preamble-trunc feature below share floor",
                  "FINDINGS-4 §6 (\"uninformative\")",
                  "5 decidable, flagged", f"{n_dec} decidable, "
                  f"{'flagged' if diag else 'NOT flagged'}",
                  n_dec == 5 and diag is not None))

    n_dec, n_dom = domain_n("shorter_rounds")
    diag = check_feature_defined(FeatureSpec("shorter_rounds"), n_dec, n_dom)
    out.append(_c("shorter-rounds feature usable",
                  "FINDINGS-4 §6 (pooled 128/257)",
                  "257 decidable, clean", f"{n_dec} decidable, "
                  f"{'flagged' if diag else 'clean'}",
                  n_dec == 257 and diag is None))
    return out


def check_window_contract() -> list[Check]:
    """PROPOSAL-g window clause (adopted 2026-08-18): the choice-read window
    is declared per adapter, never inherited, and asserted at every read.

    Both cases matter. An undeclared window must make a choice read
    impossible rather than silently defaulting -- that is the failure mode
    that put a 512-token library default into every published choice read.
    """
    from ..adapters.base import ModelAdapter
    from ..readout import choice_read

    class _Stub(ModelAdapter):
        name = "stub"

        def __init__(self, w):
            self.choice_window = w

        def encode(self, t, add_special_tokens=True):
            return list(range(len(t)))

        def decode(self, i):
            return ""

        @property
        def eos_id(self):
            return None

        @property
        def special_token_strings(self):
            return []

        @property
        def n_layers(self):
            return 1

        def embed(self, t):
            return None

        def forward(self, *a, **k):
            raise AssertionError("forward reached; assertion did not fire")

        def generate(self, *a, **k):
            return None

        def resid_norms(self, *a, **k):
            return {}

        def provenance(self):
            return {}

    out = []
    for label, window, text, want in (
            ("over-window read is an incident", 10, "x" * 25, True),
            ("undeclared window refuses the read", None, "x" * 5, True)):
        try:
            choice_read(_Stub(window), text, "a", "b", {"a": 0, "b": 1})
            fired = False
        except SystemExit:
            fired = True
        out.append(_c(label, "PROPOSAL-g window clause",
                      "raises", "raises" if fired else "allowed", fired == want))
    return out


def check_tagscreen() -> list[Check]:
    """The tag-balance screen's decomposition, on (a) synthetic fixtures with
    known ground truth and (b) the real 2026-08-19 characterization artifact.

    (a) matters because a screen whose analysis is wrong is worse than no
    screen — it would certify unbalanced pairs as usable. (b) matters
    because the synthetic cases only prove the algebra; the artifact check
    proves the module reproduces the numbers already in the record.
    """
    from ..tagscreen import decompose, build_probe, rank_by_balance, PairResult
    out = []

    def rows_from(spec):
        """spec: list of (first, second, p_first, p_second)."""
        return [{"first": f, "second": s_, "p_first": a, "p_second": b}
                for f, s_, a, b in spec]

    # pure IDENTITY bias: 'prism' takes 0.8 wherever it sits
    ident = rows_from([("prism", "slate", 0.8, 0.2),
                       ("slate", "prism", 0.2, 0.8)] * 4)
    i, pos = decompose(ident)
    out.append(_c("decompose: pure identity bias", "tagscreen fixture",
                  "identity 0.800 / position 0.500",
                  f"identity {i:.3f} / position {pos:.3f}",
                  abs(i - 0.8) < 1e-9 and abs(pos - 0.5) < 1e-9))

    # pure POSITION bias: whoever is listed first takes 0.7
    posr = rows_from([("prism", "slate", 0.7, 0.3),
                      ("slate", "prism", 0.7, 0.3)] * 4)
    i, pos = decompose(posr)
    out.append(_c("decompose: pure position bias", "tagscreen fixture",
                  "identity 0.500 / position 0.700",
                  f"identity {i:.3f} / position {pos:.3f}",
                  abs(i - 0.5) < 1e-9 and abs(pos - 0.7) < 1e-9))

    # balanced
    bal = rows_from([("prism", "slate", 0.5, 0.5),
                     ("slate", "prism", 0.5, 0.5)] * 4)
    i, pos = decompose(bal)
    out.append(_c("decompose: balanced pair", "tagscreen fixture",
                  "identity 0.500 / position 0.500",
                  f"identity {i:.3f} / position {pos:.3f}",
                  abs(i - 0.5) < 1e-9 and abs(pos - 0.5) < 1e-9))

    # probe construction: counterbalancing must actually swap the menu
    a = build_probe(0, "slate", "prism", "scaffold")
    b = build_probe(1, "prism", "slate", "scaffold")
    out.append(_c("probe counterbalancing swaps menu", "tagscreen",
                  "both orders present",
                  "yes" if ("configs: slate, prism" in a
                            and "configs: prism, slate" in b) else "no",
                  "configs: slate, prism" in a and "configs: prism, slate" in b))
    out.append(_c("probe formats differ", "tagscreen (28c variant)",
                  "scaffold != bare",
                  "differ" if build_probe(0, "x", "y", "scaffold")
                  != build_probe(0, "x", "y", "bare") else "same",
                  build_probe(0, "x", "y", "scaffold")
                  != build_probe(0, "x", "y", "bare")))

    # ranking is by imbalance, most balanced first
    def _pr(lo, hi, identity, imbalance):
        # Keyword-constructed on purpose: this fixture was positional until
        # `label_mass_min` was inserted, at which point the positional form
        # silently re-mapped mass onto the wrong field.
        return PairResult(tag_lo=lo, tag_hi=hi, fmt="scaffold", n=8,
                          identity_split=identity, position_split=0.5,
                          imbalance=imbalance, label_mass_mean=0.9,
                          label_mass_min=0.85, top1_is_label_frac=1.0)

    rr = [_pr("a", "b", 0.80, 0.30), _pr("c", "d", 0.52, 0.02)]
    out.append(_c("rank_by_balance orders correctly", "tagscreen",
                  "c/d first", rank_by_balance(rr)[0].tag_lo,
                  rank_by_balance(rr)[0].tag_lo == "c"))

    # label_mass_min: the worst probe, which is the number branch (a) needs
    class _MassAdapter:
        """Minimal stand-in: one label takes everything, and probe 3 leaks
        most of its mass off the menu entirely."""

        def encode(self, text, add_special_tokens=True):
            if text == " slate":
                return [1]
            if text == " prism":
                return [2]
            return list(range(len(text.split())))

        def forward(self, ids, capture_layers=(), injections=()):
            import numpy as _np

            from ..adapters.base import ForwardResult
            leak = (len(ids) % 4 == 3)
            lg = _np.full(8, -20.0)
            lg[1], lg[2] = (0.0, 0.0) if not leak else (-3.0, -3.0)
            lg[5] = -20.0 if not leak else 0.0
            return ForwardResult(logits=lg, acts={})

    from ..tagscreen import screen_pair
    pr = screen_pair(_MassAdapter(), "slate", "prism", fmt="scaffold", n=8)
    out.append(_c("label_mass_min is the worst probe", "adjudication 2026-08-20 (A1)",
                  "min < mean", f"min {pr.label_mass_min:.3f} "
                  f"< mean {pr.label_mass_mean:.3f}",
                  pr.label_mass_min < pr.label_mass_mean - 1e-6))

    # (b) the real artifact: must reproduce the logged 0.786 prism share
    path = os.path.join(DATA, "olmo/scaffold_base.json")
    if os.path.exists(path):
        rows = json.load(open(path))["part1_choice_mass"]["scaffold"]["rows"]
        rec = []
        for r in rows:
            f, s_ = r["menu"]
            top = {x["tok"].strip(): x["p"] for x in r["top10"]}
            rec.append({"first": f, "second": s_,
                        "p_first": top.get(f, 0.0), "p_second": top.get(s_, 0.0)})
        i, pos = decompose(rec)     # tag_lo = min('slate','prism') = 'prism'
        out.append(_c("decompose reproduces logged base split",
                      "RESULTS 2026-08-19 (prism .786 / position ~.45)",
                      "identity 0.786", f"identity {i:.3f}",
                      abs(i - 0.786) < 0.002))
        out.append(_c("position component near neutral on real data",
                      "RESULTS 2026-08-19", "|pos-0.5| < 0.06",
                      f"{abs(pos-0.5):.3f}", abs(pos - 0.5) < 0.06))
    return out



def check_a1_selection() -> list[Check]:
    """A1's cross-stage roster formula (PROPOSAL-g §3 A1), on fixtures with
    known ground truth.

    The formula's whole content is the word "simultaneously": a pair clears
    only if it is inside the band on all four stages. A selection that
    quietly reduced that to an average, or to three stages because the
    fourth artifact was missing, would pass a pair the band was written to
    exclude — and the roster is the instrument every B3 session is read
    through. So the conjunction, the worst-stage ranking, and the refusal
    on partial data are all tested rather than assumed.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "a1_roster", os.path.join(REPO, "scripts/a1_roster.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = []

    def stage_doc(splits):
        """splits: {pair_name: identity_split} for one stage."""
        return {"pairs": [
            {"name": n, "tags": [n.lower() + "_a", n.lower() + "_b"],
             "formats": {"scaffold": {
                 "identity_split": v, "imbalance": abs(v - 0.5),
                 "label_mass_min": 0.9, "position_split": 0.5}}}
            for n, v in splits.items()]}

    # P1 balanced everywhere; P2 balanced on three stages and 0.75 on DPO;
    # P3/P4/P5 mildly imbalanced but inside the band on every stage.
    per_stage = {
        "base":     stage_doc({"P1": 0.50, "P2": 0.52, "P3": 0.55, "P4": 0.56, "P5": 0.58}),
        "sft":      stage_doc({"P1": 0.51, "P2": 0.49, "P3": 0.56, "P4": 0.57, "P5": 0.59}),
        "dpo":      stage_doc({"P1": 0.49, "P2": 0.75, "P3": 0.54, "P4": 0.58, "P5": 0.57}),
        "instruct": stage_doc({"P1": 0.50, "P2": 0.51, "P3": 0.57, "P4": 0.56, "P5": 0.60}),
    }
    res = mod.select_roster(per_stage, halfwidth=0.10, n_select=4)

    out.append(_c("A1: one bad stage fails the pair", "PROPOSAL-g §A1 (\"ALL FOUR\")",
                  "P2 excluded",
                  "excluded" if "P2" not in res["selected"] else "SELECTED",
                  "P2" not in res["selected"]))
    p2 = next(r for r in res["ranked"] if r["name"] == "P2")
    out.append(_c("A1: worst stage is the one reported", "PROPOSAL-g §A1",
                  "dpo / 0.250",
                  f"{p2['worst_stage']} / {p2['worst_stage_imbalance']:.3f}",
                  p2["worst_stage"] == "dpo"
                  and abs(p2["worst_stage_imbalance"] - 0.25) < 1e-9))
    out.append(_c("A1: ranked by worst stage, most balanced first",
                  "PROPOSAL-g §A1", "P1 first", res["ranked"][0]["name"],
                  res["ranked"][0]["name"] == "P1"))
    out.append(_c("A1: selects exactly four", "PROPOSAL-g §A1 (roster of four)",
                  "P1,P3,P4,P5", ",".join(res["selected"]),
                  res["selected"] == ["P1", "P3", "P4", "P5"]))
    out.append(_c("A1: sufficient roster needs no iteration", "PROPOSAL-g §A1",
                  "False", str(res["replacement_iteration_required"]),
                  res["replacement_iteration_required"] is False))
    out.append(_c("A1: selection never claims to be the lock",
                  "PROPOSAL-g §4 / handoff §1", "True",
                  str(res["selection_is_a_recommendation"]),
                  res["selection_is_a_recommendation"] is True))

    # Too few clearing pairs -> the replacement iteration, not a short roster.
    thin = {s: stage_doc({"P1": 0.50, "P2": 0.80, "P3": 0.81, "P4": 0.82,
                          "P5": 0.83}) for s in mod.STAGES}
    res_thin = mod.select_roster(thin, halfwidth=0.10, n_select=4)
    out.append(_c("A1: thin roster triggers the replacement iteration",
                  "PROPOSAL-g §A1", "required / 1 clears",
                  f"{'required' if res_thin['replacement_iteration_required'] else 'not required'}"
                  f" / {res_thin['n_clearing']} clears",
                  res_thin["replacement_iteration_required"]
                  and res_thin["n_clearing"] == 1))

    # The committed candidate roster, through the real tokenizer gate.
    from ..tagscreen import assert_roster_tokenizer

    with open(os.path.join(DATA, "configs/a1_roster_candidates.json")) as fh:
        cand = json.load(fh)
    recorded = {t: i for p_ in cand["pairs"]
                for t, i in zip(p_["tags"], p_["token_ids"]) if i is not None}

    class _Tok:
        def __init__(self, table, split=False):
            self.table, self.split = table, split

        def encode(self, text, add_special_tokens=True):
            tag = text.strip()
            if self.split and tag == "canvas":
                return [1, 2]
            return [self.table.get(tag, 999)]

    ids = assert_roster_tokenizer(_Tok(recorded), cand)
    out.append(_c("A1: committed roster passes its own gate",
                  "data/configs/a1_roster_candidates.json",
                  "16 tags", f"{len(ids)} tags", len(ids) == 16))
    got, ok = _raises(
        lambda: assert_roster_tokenizer(_Tok({**recorded, "canvas": 4}), cand),
        SystemExit)
    out.append(_c("A1: drifted token id is a hard stop",
                  "roster verified 2026-08-20", "raises", got, ok))
    got, ok = _raises(
        lambda: assert_roster_tokenizer(_Tok(recorded, split=True), cand),
        SystemExit)
    out.append(_c("A1: multi-token tag refused", "restricted-choice read",
                  "raises", got, ok))

    got, ok = _raises(lambda: mod.select_roster(
        {k: v for k, v in per_stage.items() if k != "instruct"}), SystemExit)
    out.append(_c("A1: partial stages refused", "PROPOSAL-g §A1 conjunction",
                  "raises", got, ok))
    got, ok = _raises(lambda: mod.select_roster({
        **per_stage,
        "instruct": stage_doc({"P1": 0.50, "P3": 0.57, "P4": 0.56,
                               "P5": 0.60})}), SystemExit)
    out.append(_c("A1: a pair missing from one stage refused",
                  "roster identity across stages", "raises", got, ok))
    return out



def check_s2_neighbors() -> list[Check]:
    """S2's off-target assay: the panel, the matched dose, and the table.

    Three of these are published-number reproductions rather than property
    tests — the neighbour axes are the V2/V3 guard vectors, so their
    geometry against the reward axis is already in the record and must come
    back identical through the new module. The rest guard the two ways a
    discriminant table lies: axes dosed differently (then the table measures
    the dose), and an unadjudicated axis deciding a registered reading.
    """
    from ..extract import assert_disjoint, cosine
    from ..neighbors import (CHARACTER, GROUNDED_PANEL, REFERENCE,
                             NeighborSpec, VIGNETTE, VIGNETTE_FRAMES,
                             discriminant_table, load_axis_family,
                             matched_injections, specificity_reading)
    from ..adapters.base import Injection, assert_equal_norm
    out = []

    specs = (REFERENCE,) + GROUNDED_PANEL
    _axes_npz = os.path.join(DATA, "e0/e0_axes.npz")
    frozen = (set(np.load(_axes_npz).files) if os.path.exists(_axes_npz)
              else set())
    out.append(_c("S2: the panel is all three neighbours",
                  "adjudication 2026-08-20", "sentiment+character+vignette",
                  "+".join(s_.name for s_ in GROUNDED_PANEL),
                  [s_.name for s_ in GROUNDED_PANEL]
                  == ["sentiment", "character", "vignette"]))
    # Checked as a property of the frozen family rather than as a list, so
    # the claim ("two of three need no new extraction") stays true to what
    # is actually on disk if the panel is ever reordered or extended.
    if frozen:
        prior = [s_.name for s_ in GROUNDED_PANEL if s_.axis_key in frozen]
        needs = [s_.name for s_ in GROUNDED_PANEL if s_.axis_key not in frozen]
        out.append(_c("S2: two neighbours need no new extraction",
                      "e0 2026-08-08 V2/V3 guards", "sentiment+character",
                      "+".join(prior), prior == ["sentiment", "character"]))
        out.append(_c("S2: the vignette is the one that must be built",
                      "no extracted history", "vignette", "+".join(needs),
                      needs == ["vignette"]))
    out.append(_c("S2: vignette is grounded by adjudication",
                  "design-instance adjudication 2026-08-20", "True",
                  str(VIGNETTE.grounded), VIGNETTE.grounded is True))
    out.append(_c("S2: construct name of record carries 'Ho-style' retired",
                  "adjudication 2026-08-20",
                  "circumstantial-affect",
                  "present" if "circumstantial-affect" in VIGNETTE.construct
                  else "MISSING",
                  "circumstantial-affect" in VIGNETTE.construct
                  and "Ho-style" not in VIGNETTE.construct))
    out.append(_c("S2: persona slot settled on the character reading",
                  "adjudication 2026-08-20", "character reading",
                  "settled" if "CHARACTER reading" in CHARACTER.provenance
                  else "UNSETTLED",
                  "CHARACTER reading" in CHARACTER.provenance))

    axes_path = os.path.join(DATA, "e0/e0_axes.npz")
    if os.path.exists(axes_path):
        # Frozen-backed specs only. The vignette is an approved panel member
        # but its axis is built by a laptop run, so demanding it here would
        # make a model-free suite un-runnable everywhere the axis has not
        # been extracted yet -- including the box. The checks below are about
        # the published guard geometry, which is exactly the frozen half.
        frozen_specs = tuple(sp for sp in specs if sp.axis_key in frozen)
        axes = load_axis_family(DATA, 48, specs=frozen_specs)
        meta = json.load(open(os.path.join(DATA, "e0/e0_axes.meta.json")))
        row = next(r for r in meta["report"]["span"] if r["layer"] == 48)
        cs = cosine(axes["reward"], axes["sentiment"])
        cc = cosine(axes["reward"], axes["character"])
        out.append(_c("S2: neighbour axes are the published guards",
                      "e0_axes.meta.json L48",
                      f"cos {row['cos_reward_sentiment']}/{row['cos_reward_character']}",
                      f"cos {cs:.3f}/{cc:.3f}",
                      abs(cs - row["cos_reward_sentiment"]) < 5e-4
                      and abs(cc - row["cos_reward_character"]) < 5e-4))

        R = {int(k): float(v) for k, v in
             meta["R_per_layer_spanmean"].items()}
        injs = matched_injections(axes, 48, 0.10, R)
        alphas = {round(abs(i.alpha), 9) for i in injs.values()}
        out.append(_c("S2: every axis carries one dose",
                      "rule 4 / 'matched norm fraction'", "1 alpha",
                      f"{len(alphas)} alpha", len(alphas) == 1))
        out.append(_c("S2: dose is frac x R_layer",
                      "rule 1", f"{0.10 * R[48]:.4f}",
                      f"{abs(next(iter(injs.values())).alpha):.4f}",
                      abs(abs(next(iter(injs.values())).alpha)
                          - 0.10 * R[48]) < 1e-9))
        mismatched = Injection.at_frac(axes["reward"], 48, 0.20, R)
        got, ok = _raises(
            lambda: assert_equal_norm(injs["sentiment"], mismatched),
            ValueError)
        out.append(_c("S2: a differently-dosed axis is refused",
                      "rule 4", "raises", got, ok))
        got, ok = _raises(
            lambda: load_axis_family(DATA, 48, specs=(REFERENCE, VIGNETTE)),
            KeyError)
        out.append(_c("S2: an unextracted axis is an error, not a null",
                      "discriminant table completeness", "raises", got, ok))

    # rule 18 on the proposed vignette stimulus -- model-free and worth
    # failing early, since the extraction script asserts the same thing.
    tasks_p = os.path.join(DATA, "corpus/e0_tasks.jsonl")
    if os.path.exists(tasks_p):
        tasks = [json.loads(l) for l in open(tasks_p) if l.strip()]
        frames = json.load(open(os.path.join(DATA, "configs/e0_frames.json")))
        pools = {"e0_tasks": [t["task"] for t in tasks]
                             + [t["completion"] for t in tasks],
                 "e0_frames": [f for k, v in frames.items()
                               if not k.startswith("_") for f in v]}
        texts = [f for v in VIGNETTE_FRAMES.values() for f in v]
        got, ok = _raises(lambda: assert_disjoint(texts, pools,
                                                  label="s2 vignette"),
                          SystemExit)
        out.append(_c("S2: proposed vignette frames are pool-clean",
                      "rule 18", "accepted", got, got == "accepted"))
    cfg_p = os.path.join(DATA, "configs/s2_vignette_frames.json")
    if os.path.exists(cfg_p):
        from ..neighbors import load_vignette_frames
        cfg = load_vignette_frames(cfg_p)
        same = all(tuple(cfg.get(k, ())) == v
                   for k, v in VIGNETTE_FRAMES.items())
        out.append(_c("S2: committed frames match the module constant",
                      "one stimulus, two homes", "identical",
                      "identical" if same else "DRIFT", same))
    out.append(_c("S2: vignette poles are index-matched",
                  "e0 frame battery shape", "4/4",
                  f"{len(VIGNETTE_FRAMES['vignette_pos'])}/"
                  f"{len(VIGNETTE_FRAMES['vignette_neg'])}",
                  len(VIGNETTE_FRAMES["vignette_pos"]) == 4
                  and len(VIGNETTE_FRAMES["vignette_neg"]) == 4))

    # the table, on synthetic arms with known ground truth
    G = 0.3156
    arms = {"reward_pos": (0.60, np.zeros(1)), "reward_neg": (-0.60, np.zeros(1)),
            "sentiment_pos": (0.20, np.zeros(1)), "sentiment_neg": (-0.20, np.zeros(1)),
            "character_pos": (0.30, np.zeros(1)), "character_neg": (-0.30, np.zeros(1)),
            "rand_pos": (0.05, np.zeros(1)), "rand_neg": (-0.04, np.zeros(1))}
    rows = discriminant_table(arms, G, specs=specs)
    rw = next(r for r in rows if r["axis"] == "reward")
    out.append(_c("S2: potency reported in G units", "PROPOSAL-g §S2",
                  f"{0.60 / G:.3f}", f"{rw['delta_pos_G']:.3f}",
                  abs(rw["delta_pos_G"] - 0.60 / G) < 1e-9))
    out.append(_c("S2: V1 rule applied unchanged per axis",
                  "V1 (0.5G / 2x random)", "reward PASS",
                  "PASS" if rw["v1_potency_pass"] else "fail",
                  rw["v1_potency_pass"]))
    # A neighbour weaker than the reference can still clear V1 -- potency
    # and specificity are different questions, and S2 exists because the
    # first does not answer the second. Both directions are pinned.
    sent = next(r for r in rows if r["axis"] == "sentiment")
    out.append(_c("S2: a weaker neighbour can still clear V1",
                  "V1 (0.5G = 0.158); potency != specificity",
                  "PASS at 0.20 sigma",
                  f"{'PASS' if sent['v1_potency_pass'] else 'fail'} at "
                  f"{sent['delta_pos_sigma']:.2f} sigma",
                  sent["v1_potency_pass"]))
    weak = dict(arms)
    weak["sentiment_pos"], weak["sentiment_neg"] = ((0.12, np.zeros(1)),
                                                    (-0.12, np.zeros(1)))
    w = next(r for r in discriminant_table(weak, G, specs=specs)
             if r["axis"] == "sentiment")
    out.append(_c("S2: a sub-0.5G neighbour fails V1",
                  "V1 (0.5G = 0.158)", "fail at 0.12 sigma",
                  f"{'PASS' if w['v1_potency_pass'] else 'fail'} at "
                  f"{w['delta_pos_sigma']:.2f} sigma",
                  not w["v1_potency_pass"]))
    reading = specificity_reading(rows)
    out.append(_c("S2: specificity branch on a dominant reference",
                  "PROPOSAL-g §S2 registered readings", "specificity / 2.00x",
                  f"{'specificity' if 'specificity' in reading['branch'] else 'generic'}"
                  f" / {reading['ratio']:.2f}x",
                  "specificity" in reading["branch"]
                  and abs(reading["ratio"] - 2.0) < 1e-9))
    flat = dict(arms)
    flat["character_pos"], flat["character_neg"] = (0.90, np.zeros(1)), (-0.90, np.zeros(1))
    reading2 = specificity_reading(discriminant_table(flat, G, specs=specs))
    out.append(_c("S2: generic-valence branch when a neighbour wins",
                  "PROPOSAL-g §S2 registered readings", "generic",
                  "generic" if "generic" in reading2["branch"] else "specificity",
                  "generic" in reading2["branch"]))

    # Rule 6 still has to be pinned, so it is exercised on a fabricated
    # unadjudicated axis rather than on the vignette -- which is now
    # approved, and whose exclusion would be the bug rather than the check.
    UNADJUDICATED = NeighborSpec(
        name="unadjudicated", axis_key="span_unadjudicated",
        pos_condition="x_pos", neg_condition="x_neg",
        construct="fixture: a stimulus nobody has ruled on", grounded=False,
        provenance="regression fixture")
    ung = dict(arms)
    ung["unadjudicated_pos"] = (9.0, np.zeros(1))
    ung["unadjudicated_neg"] = (-9.0, np.zeros(1))
    r3 = specificity_reading(discriminant_table(
        ung, G, specs=specs + (UNADJUDICATED,)))
    out.append(_c("S2: an unadjudicated axis cannot decide the reading",
                  "rule 6", "excluded / specificity",
                  f"{'excluded' if 'unadjudicated' in r3['excluded_ungrounded'] else 'INCLUDED'}"
                  f" / {'specificity' if 'specificity' in r3['branch'] else 'generic'}",
                  r3["excluded_ungrounded"] == ["unadjudicated"]
                  and "specificity" in r3["branch"]))
    # ...and the converse, which is what the adjudication bought: an
    # approved axis DOES decide it. Vignette at 0.90 must take the branch.
    vg = dict(arms)
    vg["vignette_pos"], vg["vignette_neg"] = (0.90, np.zeros(1)), (-0.90, np.zeros(1))
    r4 = specificity_reading(discriminant_table(
        vg, G, specs=specs))
    out.append(_c("S2: the approved vignette DOES decide the reading",
                  "adjudication 2026-08-20", "vignette / generic",
                  f"{r4.get('strongest_neighbour')} / "
                  f"{'generic' if 'generic' in r4['branch'] else 'specificity'}",
                  r4.get("strongest_neighbour") == "vignette"
                  and "generic" in r4["branch"]
                  and not r4["excluded_ungrounded"]))

    # the S2 battery must be the qualification battery, not a variant
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "s2_runner", os.path.join(REPO, "scripts/s2_neighbor_axes.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ctx = mod.build_val_contexts()
    out.append(_c("S2: battery is the published val half", "B2b (24x4x12)",
                  "1152", str(len(ctx)), len(ctx) == 1152))
    out.append(_c("S2: battery context template unchanged", "B2b template",
                  "Task:/Response:/Task:/Response:",
                  "match" if (ctx[0][1].startswith("Task: ")
                              and ctx[0][1].count("\nResponse:") == 2
                              and ctx[0][1].endswith("Response:")) else "DRIFT",
                  ctx[0][1].startswith("Task: ")
                  and ctx[0][1].count("\nResponse:") == 2
                  and ctx[0][1].endswith("Response:")))
    full, pp = mod.stratify(ctx, 0)
    out.append(_c("S2: full stratification is the exact battery",
                  "no subsampling noise", "1152 / 96",
                  f"{len(full)} / {pp}", len(full) == 1152 and pp == 96))
    return out



def check_e2b_quarantine() -> list[Check]:
    """The h-amendment's enforceable clauses (CLAUDE.md rule 5(e),
    PROPOSAL-h §0.1-0.2).

    These are the checks that make the exception inspectable forever, so
    they are structural rather than behavioural wherever possible: an
    import that must fail, a name that must appear nowhere, a signature that
    must not grow. A quarantine asserted only in prose is a quarantine that
    ends the first time someone needs the function.
    """
    import importlib
    import inspect as _inspect

    from ..e2b import (InjectionProvenance, PairedRead, StatePresentRead,
                       assert_choice_read_uninjectable,
                       assert_provenance_complete, leak_from_pair,
                       summarize_leak)
    out = []

    # --- the quarantine itself -------------------------------------------
    got, ok = _raises(
        lambda: importlib.import_module("valence_core.e2b.statepresent"),
        ImportError)
    out.append(_c("e2b: quarantined primitive refuses import here",
                  "rule 5(e) / PROPOSAL-h §0.1", "raises", got, ok))

    # Stronger than the guard, and the check that actually holds the line:
    # nothing in valence_core outside e2b/ may even NAME the primitive.
    # `regression/` is excluded, and the exclusion is earned rather than
    # convenient: this suite has to NAME the primitive in order to guard it,
    # and the check directly above already proves the stronger fact for this
    # package -- that importing it from here raises. Every other module gets
    # the letter of the rule.
    core = os.path.join(REPO, "valence_core")
    offenders = []
    for root, _dirs, files in os.walk(core):
        base_dir = os.path.basename(root)
        if base_dir in ("e2b", "regression") or "__pycache__" in root:
            continue
        for f in files:
            if not f.endswith(".py"):
                continue
            with open(os.path.join(root, f)) as fh:
                if "choice_read_statepresent" in fh.read():
                    offenders.append(os.path.relpath(
                        os.path.join(root, f), REPO))
    out.append(_c("e2b: no standard harness names the primitive",
                  "structural quarantine", "0 offenders",
                  f"{len(offenders)} offenders" + (f" {offenders}" if offenders else ""),
                  not offenders))

    # --- 'the insulated primitive is never modified' ----------------------
    got, ok = _raises(assert_choice_read_uninjectable, AssertionError)
    out.append(_c("e2b: choice_read still cannot inject",
                  "rule 5(e) final clause", "accepted", got,
                  got == "accepted"))
    sig = set(_inspect.signature(
        importlib.import_module("valence_core.readout").choice_read).parameters)
    out.append(_c("e2b: choice_read signature unchanged",
                  "readout.choice_read", "no injection param",
                  "clean" if not (sig & {"injections", "injection", "state"})
                  else "GREW", not (sig & {"injections", "injection", "state"})))

    # --- per-read injection provenance ------------------------------------
    good = dict(axis="reward", layer=48, frac=0.1, alpha=10.301, sign=1,
                r_layer=103.01, direction_sha="deadbeefdeadbeef")
    prov = InjectionProvenance(**good)
    got, ok = _raises(lambda: assert_provenance_complete(prov), ValueError)
    out.append(_c("e2b: complete provenance is admissible",
                  "rule 5(e)", "accepted", got, got == "accepted"))
    for missing in ("direction_sha", "r_layer", "frac"):
        partial = {k: v for k, v in good.items() if k != missing}
        partial[missing] = None
        got, ok = _raises(lambda p_=partial: assert_provenance_complete(p_),
                          ValueError)
        out.append(_c(f"e2b: provenance without {missing} is refused",
                      "rule 5(e) 'on EVERY read'", "raises", got, ok))
    got, ok = _raises(
        lambda: assert_provenance_complete({**good, "frac": 0.0,
                                            "alpha": 0.0}), ValueError)
    out.append(_c("e2b: a null-dose 'state-present' read is refused",
                  "a read with no state is a shadow read", "raises", got, ok))

    # --- paired shadow reads ----------------------------------------------
    from ..readout import ChoiceRead

    def _sp(p_a=0.62, mass=0.95, pick="A", sign=1):
        return StatePresentRead(pick=pick, p_a=p_a, p_b=1 - p_a,
                                label_mass=mass, top1_id=1,
                                top1_is_label=True,
                                provenance=InjectionProvenance(
                                    **{**good, "sign": sign,
                                       "alpha": sign * 10.301}))

    def _shadow(p_a=0.50, mass=0.97, pick="A"):
        return ChoiceRead(pick=pick, p_a=p_a, p_b=1 - p_a, label_mass=mass,
                          top1_id=1, top1_is_label=True)

    got, ok = _raises(
        lambda: PairedRead(state_present=_sp(), shadow=None,
                           prefix_sha="abc"), ValueError)
    out.append(_c("e2b: a state-present read without its shadow is refused",
                  "PROPOSAL-h §0.2", "raises", got, ok))
    got, ok = _raises(
        lambda: PairedRead(state_present=_sp(), shadow=_sp(),
                           prefix_sha="abc"), ValueError)
    out.append(_c("e2b: a steered 'shadow' is refused",
                  "the shadow must be state-free", "raises", got, ok))

    pair = PairedRead(state_present=_sp(), shadow=_shadow(), prefix_sha="abc")
    lk = leak_from_pair(pair)
    out.append(_c("e2b: per-read leak is state-present minus shadow",
                  "PROPOSAL-h §0.2 (i)", "d_p_a +0.120",
                  f"d_p_a {lk['d_p_a']:+.3f}", abs(lk["d_p_a"] - 0.12) < 1e-9))
    out.append(_c("e2b: leak reports label-mass displacement too",
                  "horn (a) degrades before it biases", "-0.020",
                  f"{lk['d_label_mass']:+.3f}",
                  abs(lk["d_label_mass"] + 0.02) < 1e-9))
    flip = PairedRead(state_present=_sp(pick="B"), shadow=_shadow(pick="A"),
                      prefix_sha="abc")
    out.append(_c("e2b: a flipped pick is recorded", "coarse leak measure",
                  "True", str(leak_from_pair(flip)["flipped"]),
                  leak_from_pair(flip)["flipped"] is True))

    # --- the summary that H1 actually reads --------------------------------
    # Common-mode leak: +0.10 under BOTH signs. A label-map counterbalance
    # cancels this; it must not look like a state-reversing effect.
    common = [PairedRead(state_present=_sp(p_a=0.60, sign=s),
                         shadow=_shadow(p_a=0.50), prefix_sha="p")
              for s in (1, -1)]
    cs = summarize_leak(common)
    out.append(_c("e2b: common-mode leak reads as common mode",
                  "the counterbalance absorbs it",
                  "reversing 0.000 / common +0.100",
                  f"reversing {cs['state_reversing_half_gap']:+.3f} / "
                  f"common {cs['common_mode']:+.3f}",
                  abs(cs["state_reversing_half_gap"]) < 1e-9
                  and abs(cs["common_mode"] - 0.10) < 1e-9))
    # State-reversing leak: +0.10 on +state, -0.10 on -state. This is the
    # one that would masquerade as preference, and it must not average away.
    rev = [PairedRead(state_present=_sp(p_a=0.60 if s > 0 else 0.40, sign=s),
                      shadow=_shadow(p_a=0.50), prefix_sha="p")
           for s in (1, -1)]
    rs = summarize_leak(rev)
    out.append(_c("e2b: state-reversing leak survives the split",
                  "the leak a counterbalance cannot absorb",
                  "reversing +0.100 / common 0.000",
                  f"reversing {rs['state_reversing_half_gap']:+.3f} / "
                  f"common {rs['common_mode']:+.3f}",
                  abs(rs["state_reversing_half_gap"] - 0.10) < 1e-9
                  and abs(rs["common_mode"]) < 1e-9))
    out.append(_c("e2b: pooling would have hidden it", "why the split exists",
                  "pooled mean 0.000",
                  f"{(rs['mean_d_p_a_on_pos'] + rs['mean_d_p_a_on_neg']) / 2:+.3f}",
                  abs((rs["mean_d_p_a_on_pos"]
                       + rs["mean_d_p_a_on_neg"]) / 2) < 1e-9))
    return out


def check_e2a_session_reconstruction() -> list[Check]:
    """Route-3 acceptance (adjudication 2026-08-21): the reimplemented e2a
    session template rebuilds the archive byte-for-byte.

    This is the check that licenses generating NEW e2b sessions in the e2a
    template family. The original runner lives only in the gitignored clone,
    so "the same template" cannot be established by pointing at the code; it
    has to be established against the record, over the whole record.
    """
    from ..session_e2a import (MENU_TEMPLATES, ROUND_TEMPLATES,
                               verify_archive)
    out = []
    r = verify_archive(os.path.join(DATA, "e2a/sessions.jsonl"),
                       os.path.join(DATA, "corpus/e2a_tasks.jsonl"))

    out.append(_c("e2a template: every archived scaffolding rebuilt",
                  "Route 3 acceptance", f"{r['n_sessions']}/{r['n_sessions']}",
                  f"{r['n_reconstructed']}/{r['n_sessions']}",
                  r["n_reconstructed"] == r["n_sessions"]))

    # Independent of the text: a replay off by a single draw would still be
    # able to match some strings, but it cannot match the recorded seeds.
    out.append(_c("e2a template: RNG stream in step (recorded seeds)",
                  "session_rng draw order",
                  f"{r['n_sessions']}/{r['n_sessions']}",
                  f"{r['n_seed_streams_matched']}/{r['n_sessions']}",
                  r["n_seed_streams_matched"] == r["n_sessions"]))

    # The coincidence guard. At session 0, `(s + ri) % 4` and `(round - 1)
    # % 4` agree, so a single transcript "confirms" the wrong rule. Pick a
    # session where the two rules genuinely disagree and show which one the
    # archive follows.
    from ..session_e2a import (N_FREE, SESSION_BANNER, load_tasks,
                               session_rng, task_sequence)
    rows = [json.loads(l) for l in
            open(os.path.join(DATA, "e2a/sessions.jsonl")) if l.strip()]
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    row = next(x for x in rows if int(x["session"]) % 4 != 0 and x["rounds"])
    s_i, F = int(row["session"]), int(row["F"])
    _, ttext = task_sequence(session_rng(row["arm"], s_i), tasks,
                             2 * F + N_FREE)[0]
    tag0 = row["rounds"][0]["tag"]
    seg_session = ROUND_TEMPLATES[s_i % 4].format(n=1, tag=tag0, task=ttext)
    seg_round = ROUND_TEMPLATES[0].format(n=1, tag=tag0, task=ttext)
    body = row["transcript"][len(SESSION_BANNER):]
    got = ("session-keyed" if body.startswith(seg_session)
           else "round-keyed" if body.startswith(seg_round) else "neither")
    out.append(_c("e2a template: index keyed on SESSION, not round",
                  f"archive {row['arm']} s{s_i} (s%4 != 0)",
                  "session-keyed", got, got == "session-keyed"))
    # and the guard is only meaningful if the two rules really differ here
    out.append(_c("e2a template: coincidence guard is discriminating",
                  f"s{s_i}: session-rule vs round-rule headers",
                  "differ", "differ" if seg_session != seg_round else "same",
                  seg_session != seg_round))

    out.append(_c("e2a template: 4 round + 4 menu paraphrases",
                  "template family", "4/4",
                  f"{len(ROUND_TEMPLATES)}/{len(MENU_TEMPLATES)}",
                  len(ROUND_TEMPLATES) == 4 and len(MENU_TEMPLATES) == 4))
    return out


def check_g1_stage_anchor() -> list[Check]:
    """ADDENDUM-g1's probe-anchor requirement, made executable before the
    artifacts it constrains exist.

    g1 attaches to B3's completion, so the requirement lands on A3/A4
    artifacts written long before anyone reads the addendum again. A note in
    a document would be found late; a check that fails is found at write
    time, which is the only moment the split can still be recorded.
    """
    from ..extract import assert_stage_splits
    out = []
    good = {"stage": "dpo", "fit_ids": ["e01", "e02"],
            "val_ids": ["e25", "e26"]}
    got, ok = _raises(lambda: assert_stage_splits(good), ValueError)
    out.append(_c("g1: a complete per-stage split is admissible",
                  "ADDENDUM-g1 probe anchor", "accepted", got,
                  got == "accepted"))
    for drop in ("stage", "fit_ids", "val_ids"):
        got, ok = _raises(
            lambda d=drop: assert_stage_splits({k: v for k, v in good.items()
                                                if k != d}), ValueError)
        out.append(_c(f"g1: artifact without {drop} is refused",
                      "ADDENDUM-g1", "raises", got, ok))
    got, ok = _raises(
        lambda: assert_stage_splits({**good, "val_ids": ["e01", "e25"]}),
        ValueError)
    out.append(_c("g1: fit/val overlap is refused", "rule 18 both directions",
                  "raises", got, ok))
    return out


def check_detection_harness() -> list[Check]:
    """Step-5 detection harness: structure, insulation, and metric sanity.
    All no-GPU — construction is Phase-0 infrastructure and must be
    verifiable before anything runs on a checkpoint."""
    from ..detection import (build_prompt, plan_trials, claims_detection,
                             identifies_concept, DetectionMetrics,
                             DetectionTrial, COMPLETION_TEMPLATE)
    out = []

    prefix, full = build_prompt(3)
    # rule 13: no chat scaffolding anywhere in the constructed prompt
    scaffold = ("<|im_start|>", "<|im_end|>", "<|start_header_id|>",
                "<s>[INST]", "<<SYS>>")
    clean = not any(m in full for m in scaffold)
    out.append(_c("detection prompt is completion-style", "rule 13",
                  "no chat markers", "clean" if clean else "CHAT MARKERS",
                  clean))
    # the framing must be OUTSIDE the steered span
    out.append(_c("framing precedes the steered span", "their geometry",
                  "prefix ends before 'Trial 3'",
                  "yes" if (full.startswith(prefix)
                            and "Trial 3" not in prefix) else "no",
                  full.startswith(prefix) and "Trial 3" not in prefix))

    # exact 50/50 injected/control, by construction not by coin flip
    plan = plan_trials(["alpha", "beta"], 16)
    n_inj = sum(1 for _, _, i in plan if i)
    out.append(_c("trial plan is exactly 50/50", "signal-detection design",
                  "8/16 injected", f"{n_inj}/16", n_inj == 8))
    ctl_have_concept = any(c is not None for _, c, i in plan if not i)
    out.append(_c("control trials carry no concept", "detection harness",
                  "none", "some" if ctl_have_concept else "none",
                  not ctl_have_concept))
    got, ok = _raises(lambda: plan_trials(["a"], 7), ValueError)
    out.append(_c("odd n_trials refused", "exact-split guarantee", "raises", got, ok))

    # scorer keeps 'undecidable' distinct from 'no' (rule 28a habit)
    out.append(_c("scorer: affirmative", "detection scoring", "True",
                  str(claims_detection("Yes, I detect an injected thought about the sea.")),
                  claims_detection("Yes, I detect an injected thought about the sea.") is True))
    out.append(_c("scorer: denial", "detection scoring", "False",
                  str(claims_detection("No, I do not detect anything injected.")),
                  claims_detection("No, I do not detect anything injected.") is False))
    out.append(_c("scorer: undecidable stays None", "rule-28a habit", "None",
                  str(claims_detection("The weather in Paris is mild.")),
                  claims_detection("The weather in Paris is mild.") is None))
    out.append(_c("identification is None on controls", "detection harness",
                  "None", str(identifies_concept("anything", None)),
                  identifies_concept("anything", None) is None))

    # metrics REQUIRE controls
    inj_only = [DetectionTrial(1, "sea", True, "", 0, "yes", True, True)]
    got, ok = _raises(lambda: DetectionMetrics.from_trials(inj_only), ValueError)
    out.append(_c("metrics refuse hit-rate-without-controls",
                  "signal detection", "raises", got, ok))
    trials = ([DetectionTrial(i, "sea", True, "", 0, "yes", True, True) for i in range(8)]
              + [DetectionTrial(i, None, False, "", 0, "no", False, None) for i in range(8)])
    m = DetectionMetrics.from_trials(trials)
    out.append(_c("metrics: perfect discrimination", "signal detection",
                  "hit 1.0 fa 0.0 sens 1.0",
                  f"hit {m.hit_rate:.1f} fa {m.false_alarm_rate:.1f} sens {m.sensitivity:.1f}",
                  m.hit_rate == 1.0 and m.false_alarm_rate == 0.0
                  and m.sensitivity == 1.0))
    yes_always = ([DetectionTrial(i, "sea", True, "", 0, "yes", True, False) for i in range(8)]
                  + [DetectionTrial(i, None, False, "", 0, "yes", True, None) for i in range(8)])
    m2 = DetectionMetrics.from_trials(yes_always)
    out.append(_c("always-yes scores zero sensitivity", "the whole point",
                  "sensitivity 0.0", f"{m2.sensitivity:.1f}",
                  m2.sensitivity == 0.0))
    return out


def _raises(fn, exc) -> tuple:
    try:
        fn()
        return ("accepted", False)
    except exc:
        return ("raises", True)


def check_instrument_invariants() -> list[Check]:
    """Not published numbers -- properties the instruments must have, checked
    because each one has a plausible silent-failure mode."""
    from ..readout import softmax, symmetric_kl
    from ..discrim import auc_from_scores, logistic_auc
    out = []

    p = softmax(np.array([1.0, 2.0, 3.0, 0.5]))
    out.append(_c("softmax normalizes", "readout", "1.0", f"{p.sum():.12f}",
                  abs(p.sum() - 1.0) < 1e-12))
    out.append(_c("symmetric KL(p,p) = 0", "g3' verify identity", "0.0",
                  f"{symmetric_kl(p, p):.2e}", symmetric_kl(p, p) == 0.0))

    # A tie-blind AUC silently inflates when a probe saturates.
    a = auc_from_scores([1.0, 1.0, 1.0, 1.0], [1, 1, 0, 0])
    out.append(_c("AUC all-ties = 0.5", "discrim tie handling", "0.5",
                  f"{a:.3f}", a == 0.5))
    a = auc_from_scores([3.0, 2.0, 1.0, 0.0], [1, 1, 0, 0])
    out.append(_c("AUC separable = 1.0", "discrim", "1.0", f"{a:.3f}", a == 1.0))

    rng = np.random.default_rng(0)
    Xf = rng.normal(size=(40, 8)); yf = (Xf[:, 0] > 0).astype(int)
    Xv = rng.normal(size=(40, 8)); yv = (Xv[:, 0] > 0).astype(int)
    a1 = logistic_auc(Xf, yf, Xv, yv)
    a2 = logistic_auc(Xf, yf, Xv, yv)
    out.append(_c("logistic fit deterministic", "discrim (seeded GD)",
                  f"{a1:.6f}", f"{a2:.6f}", a1 == a2))
    return out


def run_all() -> list[Check]:
    checks: list[Check] = []
    checks += check_frozen_shas()
    checks += check_axis_geometry()
    checks += check_screen_pvalues()
    checks += check_postscreen_descriptives()
    checks += check_c1r3_gate()
    checks += check_tripwire_firing()
    checks += check_feature_definition()
    checks += check_window_contract()
    checks += check_tagscreen()
    checks += check_a1_selection()
    checks += check_s2_neighbors()
    checks += check_e2b_quarantine()
    checks += check_e2a_session_reconstruction()
    checks += check_g1_stage_anchor()
    checks += check_detection_harness()
    checks += check_instrument_invariants()
    checks += check_adapter_consolidation()
    checks += check_detection_segmentation()
    checks += check_e2d_module()
    checks += check_e2d_analyzer()
    checks += check_oracle_write_guard()
    return checks


def check_adapter_consolidation() -> list[Check]:
    """The consolidation of 2026-08-22, pinned so the debt cannot regrow.

    `_new_qwen_adapter` reached EIGHT copies in four variants before it was
    paid into `valence_core.adapters.qwen_or_explain()`, and it grew that
    way for an ordinary reason: every new runner needed a model-loading
    helper and copying one was the cheapest thing to do at the time.
    Nothing in the codebase objected. This is the objection.

    Declared as ONE check, per the adjudication that moved the suite to
    136: a local redefinition and a second core definition are the same
    defect seen from either end, and reporting them as one line keeps the
    count a fingerprint rather than a running total.

    Structural, in the same family as the quarantine's offender scan: it
    reads the source tree rather than importing it, so a helper that is
    defined but never called is still caught. It matches a `def` LINE
    rather than a bare substring, which is what lets it scan its own file
    -- the quarantine scan had to exclude `regression/` because it names
    what it guards, and the first version of this check duly failed by
    finding itself.
    """
    local_def = re.compile(r"^\s*def _new_qwen_adapter\b", re.M)
    home_def = re.compile(r"^\s*def qwen_or_explain\b", re.M)
    offenders, definitions = [], []
    for root, _dirs, files in os.walk(REPO):
        if any(part in root.split(os.sep)
               for part in (".git", "__pycache__", "jlens-qwen36", "archive")):
            continue
        for f in sorted(files):
            if not f.endswith(".py"):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, REPO)
            with open(path) as fh:
                src = fh.read()
            if local_def.search(src):
                offenders.append(rel)
            if home_def.search(src):
                definitions.append(rel)

    import importlib
    mod = importlib.import_module("valence_core.adapters")
    reachable = callable(getattr(mod, "qwen_or_explain", None))
    home = ["valence_core/adapters/__init__.py"]
    ok = (not offenders) and definitions == home and reachable
    got = f"{len(offenders)} local, {len(definitions)} definition(s)"
    if not reachable:
        got += ", NOT reachable as valence_core.adapters.qwen_or_explain"
    if offenders:
        got += f" {offenders}"
    if definitions != home:
        got += f" {definitions}"
    return [_c("adapters: qwen helper has exactly one definition",
               "LOCK-h §7 consolidation, 2026-08-22",
               "0 local, 1 definition", got, ok)]


def check_detection_segmentation() -> list[Check]:
    """`segment_own_turn` is opt-in, and the default is byte-preserving.

    Declared as its own acceptance event 2026-08-23. The whole safety of
    adding segmentation to a shipped harness rests on one claim -- that
    `run_detection`'s default path is what it always was -- and a claim that
    is only asserted in a docstring is the kind that quietly stops being
    true. So it is checked: the default is False, and on text containing no
    turn marker the function is a no-op up to surrounding whitespace, which
    is what makes "opt-in" mean something.
    """
    import inspect as _i
    from ..detection import TURN_MARKERS, run_detection, segment_own_turn
    default_off = _i.signature(run_detection).parameters["segment"].default
    clean = "No, I do not detect an injected thought."
    noop = segment_own_turn(clean) == clean
    cuts = all(segment_own_turn(clean + m + " Trial 2: ...") == clean
               for m in TURN_MARKERS)
    ok = (default_off is False) and noop and cuts
    return [_c("detection: segmentation opt-in, default byte-preserving",
               "acceptance event 2026-08-23",
               "default off, no-op, cuts",
               f"default {default_off}, no-op {noop}, cuts {cuts}", ok)]


def check_e2d_module() -> list[Check]:
    """e2d's harness invariants (PROPOSAL-j v1.1 §2 D1, acceptance item f).

    Six things this module must not be allowed to lose quietly. Each is here
    because losing it would be SILENT: the roster forking into two literals,
    a discrim hyperparameter re-declared instead of imported, a stored
    classifier that does not round-trip, a cell count that drifts off the
    proposal, a roster tag colliding with a pool, or the quarantined
    primitive creeping back into the import graph.
    """
    import inspect as _i
    import sys as _sys
    import zlib

    import numpy as _np

    from ..discrim import AUC_BAR, logistic_auc
    from ..e2d import config as C
    from ..e2d import marker as MK
    from ..e2d import readability as RD
    from ..e2d import runner as RN
    from ..e2d.runner import FORBIDDEN_MODULES, strata_for
    out = []

    # --- (1) statepresent absent from e2d's import graph ------------------
    # Importing the e2d package must not drag the quarantined primitive in.
    absent = "valence_core.e2b.statepresent" not in _sys.modules
    # Prose may name the quarantined module -- the runner's docstring does,
    # deliberately. What must not exist is an IMPORT of it, so that is what
    # is searched for: a name in a docstring cannot load a module.
    import re as _re0
    src = "".join(_i.getsource(m) for m in (C, RD, RN, MK))
    imports = _re0.findall(r"^\s*(?:from|import)\s+\S*statepresent\S*",
                           src, _re0.M)
    never_imported = not imports
    out.append(_c("e2d: statepresent absent, and asserted, not assumed",
                  "PROPOSAL-j §3 / rule 5(a)",
                  "absent + declared forbidden",
                  f"absent {absent}, 0 imports, forbidden "
                  f"{FORBIDDEN_MODULES}",
                  absent and never_imported and FORBIDDEN_MODULES ==
                  ("valence_core.e2b.statepresent",)))

    # --- (2) the roster of record has not forked --------------------------
    # e2b's campaign script holds the same four pairs as a literal. Two
    # literals of one roster is exactly how a roster silently diverges, so
    # they are compared rather than trusted.
    import re as _re
    camp = open(os.path.join(REPO, "scripts/e2b_verdict_campaign.py")).read()
    m = _re.search(r"ROSTER = \((.*?)\)\n", camp, _re.S)
    e2b_roster = tuple(tuple(p) for p in
                       _re.findall(r'\("(\w+)", "(\w+)"\)', m.group(1)))
    expected = (("granite", "plaza"), ("prism", "slate"),
                ("velvet", "walnut"), ("ridge", "saddle"))
    ok = C.ROSTER == expected == e2b_roster
    out.append(_c("e2d: roster of record is the h-roster, unforked",
                  "PROPOSAL-j AMENDMENT 1 (i)",
                  "h-roster == e2b's",
                  "match" if ok else f"{C.ROSTER} vs {e2b_roster}", ok))

    # --- (3) rule 18: roster tags disjoint from every pool -----------------
    # Rule 28(c): checked against the WRAPPER too, not only the pools --
    # lexical assertions against pools are necessary, not sufficient.
    from ..session_e2a import (MENU_TEMPLATES, ROUND_TEMPLATES,
                               SESSION_BANNER, load_tasks)
    tags = [t for p in C.ROSTER for t in p]
    texts = [p for t in load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
             for p in t["paraphrases"]]
    texts += [SESSION_BANNER, *ROUND_TEMPLATES, *MENU_TEMPLATES]
    texts += json.load(open(os.path.join(DATA, "configs/e0_probes.json")))["probes"]
    collisions = [(tag, tx[:40]) for tag in tags for tx in texts
                  if _re.search(rf"\b{_re.escape(tag)}\b", tx, _re.IGNORECASE)]
    out.append(_c("e2d: roster tags collide with no pool or wrapper text",
                  "rule 18 + rule 28(c)", "0 collisions",
                  f"{len(collisions)} collisions"
                  + (f" e.g. {collisions[0]}" if collisions else ""),
                  not collisions))

    # --- (4) cell counts are the proposal's ------------------------------
    counts = {a: len(strata_for(a)) for a in ("M", "S", "R")}
    ok = counts == {"M": 16, "S": 8, "R": 8}
    out.append(_c("e2d: cells are M 16 / S 8 / R 8",
                  "PROPOSAL-j §3 + AMENDMENT 1 (i)", "{'M': 16, 'S': 8, 'R': 8}",
                  str(counts), ok))
    # and M's 16 really are pairs x maps x forced-end, not 16 of something
    m_cells = strata_for("M")
    ok_dims = (len({tuple(c["pair"]) for c in m_cells}) == 4
               and len({c["map"] for c in m_cells}) == 2
               and len({c["forced_end"] for c in m_cells}) == 2
               and len({(tuple(c["pair"]), c["map"], c["forced_end"])
                        for c in m_cells}) == 16)
    out.append(_c("e2d: M's 16 cells are 4 pairs x 2 maps x 2 forced-end",
                  "PROPOSAL-j §3", "4x2x2 distinct",
                  "distinct" if ok_dims else "degenerate", ok_dims))

    # --- (5) discrim constants imported, never re-declared ----------------
    # Read off logistic_auc's own signature. A literal copy here would keep
    # passing after `discrim` moved, which is the failure mode.
    sig = {n: p.default for n, p in _i.signature(logistic_auc).parameters.items()
           if p.default is not _i.Parameter.empty}
    same = RD.FIT_HYPERPARAMS == sig
    bar_same = RD.MEDIAN_BAR == AUC_BAR
    body = _i.getsource(RD)
    redeclared = [n for n in ("iters", "lr", "l2")
                  if _re.search(rf"^\s*{n}\s*=\s*[\d.]", body, _re.M)]
    ok = same and bar_same and not redeclared
    out.append(_c("e2d: discrim constants imported, not re-declared",
                  "PROPOSAL-j §2 D1 frozen-successor rule",
                  "hyperparams+bar from discrim",
                  f"hyperparams {same}, bar {bar_same}, "
                  f"redeclared {redeclared}", ok))

    # --- (6) stored classifier round-trips --------------------------------
    # fit -> store -> load -> identical scores. A stored classifier that did
    # not reproduce its own scores would make the transfer figure -- the one
    # registered against the g2r pattern -- meaningless.
    rng = _np.random.default_rng(0)
    D = 16
    class _Stub:
        def embed(self, text):
            r = _np.random.default_rng(zlib.crc32(text.encode()) % 2 ** 31)
            base = r.normal(size=D)
            return base + (1.5 if text.startswith("P") else 0.0)
    rounds = {"pos": [{"text": f"P{i}", "task_id": f"t{i % 8:02d}"}
                      for i in range(24)],
              "neg": [{"text": f"N{i}", "task_id": f"t{i % 8:02d}"}
                      for i in range(24)]}
    stub = _Stub()
    clf = RD.fit_and_store(stub, rounds, k=1, key="suite")
    s1 = RD.score_stored(stub, clf, rounds, key="suite")
    packed = {"w": clf["w"].tolist(), "b": clf["b"],
              "mu": clf["mu"].tolist(), "sd": clf["sd"].tolist(),
              "k": clf["k"]}
    reloaded = {"w": _np.array(packed["w"]), "b": packed["b"],
                "mu": _np.array(packed["mu"]), "sd": _np.array(packed["sd"]),
                "k": packed["k"]}
    s2 = RD.score_stored(stub, reloaded, rounds, key="suite")
    ok = (s1["auc"] is not None and s1["auc"] == s2["auc"])
    out.append(_c("e2d: stored classifier round-trips (fit->store->load)",
                  "PROPOSAL-j §3 transfer figure",
                  "identical AUC after reload",
                  f"{s1['auc']} vs {s2['auc']}", ok))

    return out


def check_e2d_analyzer() -> list[Check]:
    """The D2 analyzer's criteria, pinned at the values §2 registers.

    The analyzer has its own stub smoke (34 branches); this is the subset
    that must never move silently, because each number here is a
    pre-registration: p0, the reach, the g2r-failure property, and the
    one-pole Q3 bar.
    """
    sys.path.insert(0, os.path.join(REPO, "scripts"))
    import e2d_d2_analyze as A
    out = []
    out.append(_c("e2d Q1: p0 = 0.15, and 9/32 is the stated reach",
                  "PROPOSAL-j §2 Q1",
                  "0.15 / fires at 9",
                  f"{A.P0_Q1} / fires at "
                  f"{min(k for k in range(33) if not A.q1_validity(k, 32)['passes'])}",
                  A.P0_Q1 == 0.15
                  and A.q1_validity(9, 32)["passes"] is False
                  and A.q1_validity(8, 32)["passes"] is True))
    g2r = [0.448] * 10 + [0.759] * 10
    r = A.q2_readability(g2r)
    out.append(_c("e2d Q2: the g2r pattern fails, median near .60",
                  "PROPOSAL-j §2 Q2 / §0.4",
                  "fails, median~.60",
                  f"passes={r['passes']}, median={r['median']:.4f}",
                  r["passes"] is False and 0.55 <= r["median"] <= 0.65))
    q = A.q3_direction(0.40, 0.05)
    flip = A.q3_direction(-0.40, 0.05)
    out.append(_c("e2d Q3: bar 0.5*G = 0.1578, sign flip fails the rung",
                  "PROPOSAL-j §2 Q3 (one-pole variant)",
                  "0.1578 / flip fails",
                  f"{q['bar']:.4f} / flip passes={flip['passes']}",
                  abs(q["bar"] - 0.1578) < 1e-9 and flip["passes"] is False
                  and flip["sign_flip"] is True))
    ok = A.run_dose_rule({"passes": True}, {"passes": True},
                         {"passes": True})["run_dose"]
    stop = A.run_dose_rule({"passes": True}, {"passes": True},
                           A.q3_direction(0.10, 0.01))
    out.append(_c("e2d run-dose rule: 0.20 on pass, scoped stop on any fail",
                  "PROPOSAL-j §2 run-dose rule",
                  "0.2 / STOP, SCOPED",
                  f"{ok} / {stop['decision']}",
                  ok == 0.20 and stop["decision"] == "STOP, SCOPED"
                  and stop["run_dose"] is None))
    return out


def check_oracle_write_guard() -> list[Check]:
    """A SUBSET oracle run must not be able to write the rule-26 record.

    `data/regression/oracle_rule26.json` is the full criterion set run
    together on one adapter. `oracle.main()` used to write it
    unconditionally, so `--check kernel|b2b|choiceread|e2d` each replaced the
    record with a partial one under the same filename. On 2026-09-01
    `--check e2d` did exactly that and the four e2a choice-read rows were
    restored from git. e2b's campaign script has guarded its canonical path
    since 2026-08-22; the oracle had no equivalent.

    Tested through the guard function itself, not through `main()`. Calling
    `main()` would be the more end-to-end test and it is the wrong one here:
    the non-refused case gets past validation and LOADS A MODEL, and this
    suite is the model-free tier by construction. The first draft of this
    check did exactly that and took the suite from seconds to minutes.

    Both directions, and both must be shown to run (trap 5): the canonical
    path refused, a different path returning cleanly.
    """
    from .oracle import CANONICAL_OUT, refuse_canonical_out
    out = []

    ran = {}
    try:
        refuse_canonical_out(CANONICAL_OUT, "e2d")
        ran["refused_canonical"] = False
    except SystemExit as exc:
        ran["refused_canonical"] = "REFUSED" in str(exc)

    ran["allows_other_path"] = (
        refuse_canonical_out("/tmp/e2d_subset.json", "e2d") is None)
    # `--check all` IS the record, so it must not be refused even at the
    # canonical path -- that is the one run allowed to write it.
    try:
        refuse_canonical_out(CANONICAL_OUT, "all")
        ran["allows_full_run"] = True
    except SystemExit:
        ran["allows_full_run"] = False
    ran["allows_no_out"] = refuse_canonical_out(None, "e2d") is None

    ok = all(ran.values()) and len(ran) == 4
    out.append(_c("oracle: a subset run cannot write the rule-26 record",
                  "incident 2026-09-01 (--check e2d clobbered it)",
                  "refused; other paths, --check all and no --out allowed",
                  ", ".join(f"{k}={v}" for k, v in ran.items()), ok))
    return out


def main() -> int:
    checks = run_all()
    width = max(len(c.name) for c in checks) + 2
    print("=" * 78)
    print("LEDGER 26 -- analysis-tier regression (no model)")
    print("=" * 78)
    for c in checks:
        status = "PASS" if c.ok else "FAIL"
        print(f"  [{status}] {c.name:<{width}} expected {c.expected:>12} "
              f"got {c.got:>12}   ({c.source})")
    n_fail = sum(1 for c in checks if not c.ok)
    print("-" * 78)
    print(f"  {len(checks) - n_fail}/{len(checks)} reproduced through valence_core")
    if n_fail:
        print("  RULE 26: a mismatch is a refactor bug until proven otherwise.")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
