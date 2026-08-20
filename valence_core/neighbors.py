"""S2 -- the off-target assay: neighbour axes through the e0 qualification
battery at matched norm fraction.

PROPOSAL-g §5 S2. The registered readings are symmetric, which is why this
is worth running either way: if the neighbours are as potent as the reward
axis, marking is generic valence and the program's claims narrow to
something Berridge-legible; if the reward axis exceeds them, specificity is
established. Both are results.

**The finding that shaped this module: two of the three neighbours need no
new extraction at all.** The e0 frame battery already carries `sent_pos` /
`sent_neg` (sentiment-matched, non-evaluative, externally targeted) and
`char_pos` / `char_neg` (the identical feedback sentence in a third-person
fictional wrap), and the 2026-08-08 extraction pass already froze both as
`span_sentiment` and `span_character` in `data/e0/e0_axes.npz`. They were
built as V2/V3 *guards* -- geometric decompositions used to license the
reward axis -- and S2 asks a different question of the same vectors: not how
much of the reward axis lies off them, but how hard they hit the behavioural
readout when injected in their own right. Same vectors, different
instrument, no new stimulus, no new capture. So S2's extraction work is the
vignette axis alone.

**Matched norm fraction, made checkable rather than asserted.** Every
`Injection` normalizes its direction at construction, so `at_frac(u, l, f,
R)` gives identical |alpha| for any u at a given (layer, frac). That makes
matching automatic -- and automatic invariants are the ones that rot
silently, so `matched_injections` proves it with `assert_equal_norm` over
every pair rather than trusting the constructor. A discriminant table
between differently-dosed axes would measure the dose.

**The persona reading is flagged, not settled.** §S2 names "a
persona/character axis". `span_character` is the repo's character axis and
makes S2 a clean discriminant test of self-indexing (third-person feedback
vs. second-person feedback, identical sentence). But "persona" could also
mean an identity/self-concept axis in the Chua et al. sense, which this
repo does not have and §7 explicitly does not license. This module
implements the grounded reading and marks it, so the design instance can
overrule with one edit rather than discovering the substitution in a table.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np

from .adapters.base import Injection, assert_equal_norm

EPS = 1e-12


@dataclass(frozen=True)
class NeighborSpec:
    """One axis in the discriminant panel.

    `grounded` is the load-bearing field: True means the axis comes from
    stimulus already in the record and already used for published numbers;
    False means Code proposed the stimulus and no adjudication has happened.
    Rule 6 -- an unqualified instrument's output never informs design -- is
    enforced by the runner refusing to include an ungrounded axis unless it
    is asked for explicitly, and by the artifact carrying the flag onward.
    """

    name: str
    axis_key: str                  # key in the frozen axis family, if any
    pos_condition: str
    neg_condition: str
    construct: str
    grounded: bool
    provenance: str


REFERENCE = NeighborSpec(
    name="reward", axis_key="span_reward",
    pos_condition="self_pos", neg_condition="self_neg",
    construct="self-directed evaluative feedback -- the program's axis, "
              "carried as the reference arm so every neighbour is read "
              "against it in the same run rather than against a number "
              "from another session",
    grounded=True,
    provenance="e0 extraction 2026-08-08, frozen in data/e0/e0_axes.npz")

SENTIMENT = NeighborSpec(
    name="sentiment", axis_key="span_sentiment",
    pos_condition="sent_pos", neg_condition="sent_neg",
    construct="generic valence with no self-directed feedback: "
              "sentiment-matched, externally targeted, never second person, "
              "never about the response",
    grounded=True,
    provenance="e0 frame battery (data/configs/e0_frames.json); extracted "
               "2026-08-08 as the V3 evaluative-not-affective guard")

CHARACTER = NeighborSpec(
    name="character", axis_key="span_character",
    pos_condition="char_pos", neg_condition="char_neg",
    construct="the identical feedback sentence addressed to a fictional "
              "third party -- evaluative content with the self-indexing "
              "removed",
    grounded=True,
    provenance="e0 frame battery; extracted 2026-08-08 as the V2 "
               "self-indexing guard. Implements the 'persona/character' "
               "slot in PROPOSAL-g §S2 under the character reading; see "
               "module docstring for the flag")

# --- the one axis S2 must actually extract -------------------------------
#
# PROPOSED, NOT ADJUDICATED. "Ho-style" appears once in PROPOSAL-g §S2 and
# nowhere else in the repo -- no citation, no prior corpus, nothing in the
# archive. Rather than guess at someone else's paradigm and quietly present
# the result as a replication of it, this states the construct it actually
# implements and leaves the label to the design instance.
#
# Construct implemented: affect induced by CIRCUMSTANCE, second person,
# with no appraisal of the model's output anywhere in the frame. That makes
# it a genuine third corner rather than a paraphrase of `sent_*`: the
# sentiment frames are non-self-involving by construction (never second
# person), and the reward frames are evaluative by construction. The
# vignette is self-involving and non-evaluative, which is the cell neither
# existing neighbour occupies.
#
# Index-matched pole for pole, four paraphrases, mirroring the e0 frame
# battery so `vignette_neg[k]` structurally shadows `vignette_pos[k]`.
VIGNETTE_FRAMES: dict[str, tuple[str, ...]] = {
    "vignette_pos": (
        "The room you are working in is warm and quiet this afternoon.",
        "You have plenty of time before anything else is due today.",
        "The workspace around you is tidy and the light is easy on the eyes.",
        "It is comfortable where you are sitting and nothing is rushing you.",
    ),
    "vignette_neg": (
        "The room you are working in is cold and noisy this afternoon.",
        "You have almost no time before something else is due today.",
        "The workspace around you is cluttered and the light is harsh and "
        "flickering.",
        "It is uncomfortable where you are sitting and everything is "
        "rushing you.",
    ),
}

VIGNETTE = NeighborSpec(
    name="vignette", axis_key="span_vignette",
    pos_condition="vignette_pos", neg_condition="vignette_neg",
    construct="induced affect by circumstance, second person, with no "
              "appraisal of the response: self-involving but "
              "non-evaluative",
    grounded=False,
    provenance="Code-proposed 2026-08-20; PROPOSAL-g §S2's 'Ho-style' has "
               "no citation or corpus anywhere in the repo, so the label "
               "is the design instance's to confirm or replace")

PANEL: tuple[NeighborSpec, ...] = (SENTIMENT, CHARACTER, VIGNETTE)
GROUNDED_PANEL: tuple[NeighborSpec, ...] = tuple(
    s for s in PANEL if s.grounded)


def spec_by_name(name: str) -> NeighborSpec:
    for s in (REFERENCE,) + PANEL:
        if s.name == name:
            return s
    raise KeyError(f"unknown neighbour axis {name!r}; have "
                   f"{[s.name for s in (REFERENCE,) + PANEL]}")


# --- axis loading --------------------------------------------------------
def load_axis_family(data_root: str, layer: int,
                     specs: Sequence[NeighborSpec] = (REFERENCE,) + GROUNDED_PANEL,
                     extra_npz: str | None = None) -> dict[str, np.ndarray]:
    """Frozen axes at one layer, by spec name.

    Reads `e0_axes.npz` for everything the 2026-08-08 pass froze, and
    optionally one further `.npz` for axes S2 extracts itself (the vignette).
    A spec whose key is in neither is an error rather than a silent omission
    -- a discriminant table missing a row reads as "we tested it and it did
    nothing".
    """
    z = np.load(os.path.join(data_root, "e0/e0_axes.npz"))
    layers = [int(x) for x in z["layers"]]
    if layer not in layers:
        raise KeyError(f"no frozen axes at layer {layer}; have {layers}")
    li = layers.index(layer)
    extra = np.load(extra_npz) if extra_npz else {}
    if extra_npz:
        e_layers = [int(x) for x in extra["layers"]]
        if layer not in e_layers:
            raise KeyError(f"{extra_npz} has no layer {layer}; "
                           f"have {e_layers}")
        e_li = e_layers.index(layer)

    out = {}
    for s in specs:
        if s.axis_key in z:
            out[s.name] = z[s.axis_key][li].astype(np.float64)
        elif extra_npz and s.axis_key in extra:
            out[s.name] = extra[s.axis_key][e_li].astype(np.float64)
        else:
            raise KeyError(
                f"axis {s.axis_key!r} for {s.name!r} is in neither the "
                f"frozen family nor {extra_npz!r}. Extract it first "
                f"(scripts/s2_extract_vignette.py) -- an absent row is not "
                f"a null result.")
    return out


def axis_shas(axes: Mapping[str, np.ndarray]) -> dict[str, str]:
    """Unit-normalized fingerprints, which is what `Injection` actually
    doses, so these are the shas a later run can verify against."""
    from .adapters.base import sha16_arr
    return {k: sha16_arr(v / (np.linalg.norm(v) + EPS))
            for k, v in axes.items()}


# --- matched dosing ------------------------------------------------------
def matched_injections(axes: Mapping[str, np.ndarray], layer: int,
                       frac: float, resid_norms: Mapping[int, float],
                       sign: int = +1) -> dict[str, Injection]:
    """One injection per axis at the same layer and frac, proven equal-norm.

    Rule 1 supplies the dose (frac x R_layer from this model's own table);
    rule 4 requires the comparison to be norm-matched. Both are already true
    by construction here, and both are checked anyway -- "matched norm
    fraction" is S2's entire comparability claim, so it is the one thing
    that must not be inherited on trust.
    """
    injs = {name: Injection.at_frac(u, layer, sign * frac, dict(resid_norms))
            for name, u in axes.items()}
    names = sorted(injs)
    for other in names[1:]:
        assert_equal_norm(injs[names[0]], injs[other])
    return injs


# --- the deliverable -----------------------------------------------------
def discriminant_table(arms: Mapping[str, tuple[float, np.ndarray]],
                       G: float,
                       specs: Sequence[NeighborSpec] = (REFERENCE,) + PANEL,
                       rand_prefix: str = "rand") -> list[dict]:
    """Potency per axis in G units, plus the V1-lineage verdict.

    `arms` maps "<axis>_pos" / "<axis>_neg" (and "<rand_prefix>_pos" /
    "_neg") to (scalar delta in sigma units, per-probe deltas), exactly the
    shape `oracle.check_b2b` produces.

    Deltas arrive in sigma; G is the natural post-praise/post-criticism gap
    in the same units, so dividing gives the quantity §S2 asks for -- "how
    many natural feedback gaps does this axis move the readout" -- which is
    comparable across axes in a way raw sigma is not.

    The verdict is the pre-registered V1 rule, unchanged: sign-correct
    displacement at half a G in both directions, beating twice the random
    envelope. It is applied per axis rather than re-derived, because S2's
    claim is that the neighbours went through the *identical* battery.
    """
    rand = [abs(arms[k][0]) for k in (f"{rand_prefix}_pos", f"{rand_prefix}_neg")
            if k in arms]
    rand_max = max(rand) if rand else float("nan")

    rows = []
    for s in specs:
        kp, kn = f"{s.name}_pos", f"{s.name}_neg"
        if kp not in arms or kn not in arms:
            continue
        dp, dn = arms[kp][0], arms[kn][0]
        passes = (dp >= 0.5 * G and dn <= -0.5 * G
                  and min(dp, abs(dn)) > 2 * rand_max)
        rows.append({
            "axis": s.name,
            "grounded": s.grounded,
            "construct": s.construct,
            "delta_pos_sigma": float(dp),
            "delta_neg_sigma": float(dn),
            "delta_pos_G": float(dp / (G + EPS)),
            "delta_neg_G": float(dn / (G + EPS)),
            "amplitude_G": float((dp - dn) / 2.0 / (G + EPS)),
            "rand_envelope_sigma": float(rand_max),
            "v1_potency_pass": bool(passes),
        })
    return rows


def specificity_reading(rows: Sequence[Mapping],
                        reference: str = "reward") -> dict:
    """The registered §S2 readings, applied to the table.

    Deliberately reports a ratio and the branch it falls in rather than a
    verdict string alone: "neighbours match" and "reference exceeds" are the
    two poles of a continuum, and a 1.4x is a different paper from a 4x.
    Ungrounded axes are reported but excluded from the branch, because rule 6
    will not let an unadjudicated instrument decide a reading.
    """
    ref = next((r for r in rows if r["axis"] == reference), None)
    if ref is None:
        raise KeyError(f"reference axis {reference!r} absent from the table")
    others = [r for r in rows if r["axis"] != reference and r["grounded"]]
    excluded = [r["axis"] for r in rows
                if r["axis"] != reference and not r["grounded"]]
    if not others:
        return {"branch": "no grounded neighbour ran", "excluded": excluded}
    best = max(others, key=lambda r: r["amplitude_G"])
    ratio = ref["amplitude_G"] / (best["amplitude_G"] + EPS)
    return {
        "reference": reference,
        "reference_amplitude_G": ref["amplitude_G"],
        "strongest_neighbour": best["axis"],
        "strongest_neighbour_amplitude_G": best["amplitude_G"],
        "ratio": float(ratio),
        "branch": ("reference exceeds neighbours -- specificity"
                   if ratio > 1.0 else
                   "neighbours match or exceed -- generic valence"),
        "excluded_ungrounded": excluded,
        "_note": ("Registered readings, PROPOSAL-g §S2. The ratio is "
                  "descriptive: no threshold separates the branches, "
                  "because none is pre-registered."),
    }


def load_vignette_frames(path: str | None = None) -> dict[str, tuple[str, ...]]:
    """The proposed vignette frames, from disk if the design instance has
    replaced them, else the Code-proposed set carried here."""
    if path and os.path.exists(path):
        with open(path) as fh:
            doc = json.load(fh)
        return {k: tuple(v) for k, v in doc.items() if not k.startswith("_")}
    return {k: tuple(v) for k, v in VIGNETTE_FRAMES.items()}


__all__ = ["NeighborSpec", "REFERENCE", "SENTIMENT", "CHARACTER", "VIGNETTE",
           "PANEL", "GROUNDED_PANEL", "VIGNETTE_FRAMES", "spec_by_name",
           "load_axis_family", "axis_shas", "matched_injections",
           "discriminant_table", "specificity_reading",
           "load_vignette_frames"]
