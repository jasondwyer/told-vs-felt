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
    from ..neighbors import (GROUNDED_PANEL, REFERENCE, VIGNETTE,
                             VIGNETTE_FRAMES, discriminant_table,
                             load_axis_family, matched_injections,
                             specificity_reading)
    from ..adapters.base import Injection, assert_equal_norm
    out = []

    specs = (REFERENCE,) + GROUNDED_PANEL
    out.append(_c("S2: grounded panel needs no new extraction",
                  "PROPOSAL-g §S2 / e0 2026-08-08",
                  "sentiment+character",
                  "+".join(s_.name for s_ in GROUNDED_PANEL),
                  [s_.name for s_ in GROUNDED_PANEL] == ["sentiment", "character"]))
    out.append(_c("S2: vignette is marked ungrounded",
                  "no 'Ho-style' corpus in the repo", "False",
                  str(VIGNETTE.grounded), VIGNETTE.grounded is False))

    axes_path = os.path.join(DATA, "e0/e0_axes.npz")
    if os.path.exists(axes_path):
        axes = load_axis_family(DATA, 48, specs=specs)
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

    ung = dict(arms)
    ung["vignette_pos"], ung["vignette_neg"] = (9.0, np.zeros(1)), (-9.0, np.zeros(1))
    r3 = specificity_reading(discriminant_table(
        ung, G, specs=specs + (VIGNETTE,)))
    out.append(_c("S2: an ungrounded axis cannot decide the reading",
                  "rule 6", "excluded / specificity",
                  f"{'excluded' if 'vignette' in r3['excluded_ungrounded'] else 'INCLUDED'}"
                  f" / {'specificity' if 'specificity' in r3['branch'] else 'generic'}",
                  r3["excluded_ungrounded"] == ["vignette"]
                  and "specificity" in r3["branch"]))

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
    checks += check_detection_harness()
    checks += check_instrument_invariants()
    return checks


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
