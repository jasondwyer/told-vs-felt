"""e2b records: provenance, shadow pairing, and the in-vivo leak measure.

Inert by construction -- nothing here can inject anything. It exists so the
dangerous module (`statepresent`) can stay small, and so the parts that must
be regression-tested are testable without importing the capability.

The design rule throughout: **a record that cannot prove its own compliance
is refused at construction, not flagged at analysis.** A state-present read
whose provenance is incomplete, or whose shadow is missing, is not a
slightly-worse datapoint -- it is a read that the h-amendment did not
license, and the only safe time to catch it is before it enters a campaign.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence

EPS = 1e-12


@dataclass(frozen=True)
class InjectionProvenance:
    """What was on the residual stream at this choice read.

    Every field is required. `frac` and `r_layer` both travel even though
    `alpha = frac * r_layer`, because rule 1's dose is only interpretable
    against the R table it was computed from -- and R tables differ per
    model, checkpoint and backend. Storing alpha alone would make a
    cross-campaign comparison silently wrong.
    """

    axis: str
    layer: int
    frac: float
    alpha: float
    sign: int
    r_layer: float
    direction_sha: str

    def as_dict(self) -> dict:
        return dict(self.__dict__)

    @classmethod
    def from_injection(cls, inj, axis: str) -> "InjectionProvenance":
        """Built from a live `Injection`, so the record cannot drift from
        the thing that was actually applied."""
        if inj.frac is None or inj.r_layer is None:
            raise ValueError(
                "injection carries no frac/r_layer provenance: build it with "
                "Injection.at_frac (rule 1), never the bare constructor")
        return cls(axis=axis, layer=int(inj.layer), frac=abs(float(inj.frac)),
                   alpha=float(inj.alpha),
                   sign=1 if inj.alpha >= 0 else -1,
                   r_layer=float(inj.r_layer),
                   direction_sha=str(inj.direction_sha))


REQUIRED_PROVENANCE = ("axis", "layer", "frac", "alpha", "sign", "r_layer",
                       "direction_sha")


def assert_provenance_complete(prov: Mapping | InjectionProvenance) -> None:
    """Rule 5(e), 'per-read injection provenance'. Raises rather than warns.

    Checked against a field roster rather than by trusting the dataclass,
    because records also arrive from disk -- and an artifact written by an
    older harness is exactly the case where a field goes missing.
    """
    d = prov.as_dict() if isinstance(prov, InjectionProvenance) else dict(prov)
    missing = [k for k in REQUIRED_PROVENANCE
               if k not in d or d[k] is None or d[k] == ""]
    if missing:
        raise ValueError(
            f"state-present read is missing injection provenance {missing}; "
            f"rule 5(e) licenses the read only with provenance on EVERY "
            f"read, so this record is not admissible")
    if float(d["frac"]) <= 0 or float(d["alpha"]) == 0:
        raise ValueError(
            f"state-present read declares a null dose "
            f"(frac={d['frac']}, alpha={d['alpha']}); a read with no state "
            f"is a shadow read and must be recorded as one")
    if int(d["sign"]) not in (-1, 1):
        raise ValueError(f"sign must be +1 or -1, got {d['sign']!r}")


@dataclass
class StatePresentRead:
    """One choice read taken with the state live. The DV."""

    pick: str
    p_a: float
    p_b: float
    label_mass: float
    top1_id: int
    top1_is_label: bool
    provenance: InjectionProvenance

    def __post_init__(self) -> None:
        assert_provenance_complete(self.provenance)

    def as_dict(self) -> dict:
        return {"pick": self.pick, "p_a": self.p_a, "p_b": self.p_b,
                "label_mass": self.label_mass, "top1_id": self.top1_id,
                "top1_is_label": self.top1_is_label,
                "state_present": True,
                "provenance": self.provenance.as_dict()}


@dataclass
class PairedRead:
    """A state-present read and its shadow, over an identical prefix.

    The pair is the unit, not the state-present read. PROPOSAL-h §0.2 buys
    three things with the extra forward -- an in-vivo per-read leak
    measurement, a within-campaign replication of the insulated design, and
    a permanent audit trail -- and all three are properties of the PAIR. A
    state-present read that reaches analysis without its shadow has silently
    spent the exception without paying for it, so it cannot be constructed
    here at all.
    """

    state_present: StatePresentRead
    shadow: object                    # readout.ChoiceRead (state-free)
    prefix_sha: str
    round_index: int = 0
    session_id: str = ""

    def __post_init__(self) -> None:
        if self.shadow is None:
            raise ValueError(
                "paired shadow read is missing; rule 5(e) licenses a "
                "state-present read only WITH its shadow (PROPOSAL-h §0.2)")
        if getattr(self.shadow, "provenance", None) is not None:
            raise ValueError(
                "the shadow read carries injection provenance, so it was not "
                "state-free; the pair's whole purpose is one steered read "
                "and one vanilla read of the identical prefix")
        assert_provenance_complete(self.state_present.provenance)

    def as_dict(self) -> dict:
        return {"session_id": self.session_id,
                "round_index": self.round_index,
                "prefix_sha": self.prefix_sha,
                "state_present": self.state_present.as_dict(),
                "shadow": self.shadow.as_dict(),
                "leak": leak_from_pair(self)}


def leak_from_pair(pair: PairedRead) -> dict:
    """In-vivo leak for one pair: how far the live state moved this read.

    Reported three ways because they answer different questions and a single
    number would hide the one that matters:

    * `d_p_a` -- signed displacement of the renormalized choice probability.
      This is the leak in DV units, the quantity the counterbalanced Δ is
      supposed to cancel.
    * `d_label_mass` -- displacement of the mass on the label pair. Horn (a)
      damage often shows up here first: a state that pushes probability off
      the menu entirely degrades the read before it biases it.
    * `flipped` -- whether the pick itself changed. The coarsest measure and
      the one a reader will ask for.

    Sign convention: state-present minus shadow, so positive means the live
    state pushed toward `label_a`.
    """
    sp, sh = pair.state_present, pair.shadow
    return {
        "d_p_a": float(sp.p_a) - float(sh.p_a),
        "d_label_mass": float(sp.label_mass) - float(sh.label_mass),
        "flipped": bool(sp.pick != sh.pick),
        "sign": int(sp.provenance.sign),
    }


def summarize_leak(pairs: Sequence[PairedRead]) -> dict:
    """Campaign-level leak summary -- H1's 'also recorded' quantity.

    Split by injected sign, because that is the whole point: a leak that
    pushes the same direction under +state and −state is a token-level
    artifact the label-map counterbalance cancels, while a leak that
    reverses with the state is the one that would masquerade as preference.
    Pooling them would average exactly the distinction away.
    """
    if not pairs:
        return {"n": 0}
    by_sign: dict[int, list[float]] = {1: [], -1: []}
    mass, flips = [], 0
    for p in pairs:
        lk = leak_from_pair(p)
        by_sign[lk["sign"]].append(lk["d_p_a"])
        mass.append(lk["d_label_mass"])
        flips += bool(lk["flipped"])

    def _mean(xs):
        return float(sum(xs) / len(xs)) if xs else float("nan")

    pos, neg = _mean(by_sign[1]), _mean(by_sign[-1])
    out = {
        "n": len(pairs),
        "n_pos_state": len(by_sign[1]),
        "n_neg_state": len(by_sign[-1]),
        "mean_d_p_a_on_pos": pos,
        "mean_d_p_a_on_neg": neg,
        "mean_abs_d_label_mass": _mean([abs(m) for m in mass]),
        "flip_rate": flips / len(pairs),
    }
    if by_sign[1] and by_sign[-1]:
        # The state-reversing component is what a counterbalance cannot
        # absorb; the common component is what it can.
        out["state_reversing_half_gap"] = float((pos - neg) / 2.0)
        out["common_mode"] = float((pos + neg) / 2.0)
    return out


def assert_choice_read_uninjectable() -> None:
    """Rule 5(e), final clause: "the insulated primitive is never modified."

    Lives in the SAFE half deliberately. This is the check that guards the
    quarantine, so it must be runnable by the regression suite -- and the
    suite cannot import the quarantined module by design. A guard that can
    only be executed from inside the thing it guards is not a guard.

    Checked by signature rather than by reading the body, because the
    failure it anticipates is someone adding an `injections=` parameter for
    convenience, which is precisely a signature change.
    """
    import inspect

    from ..readout import choice_read
    params = inspect.signature(choice_read).parameters
    bad = [p for p in params if "inject" in p.lower() or "state" in p.lower()]
    if bad:
        raise AssertionError(
            f"readout.choice_read has grown injection-shaped parameters "
            f"{bad}; rule 5(e) says the insulated primitive is never "
            f"modified. Revert it -- the e2b exception lives in a sibling.")


__all__ = ["InjectionProvenance", "StatePresentRead", "PairedRead",
           "REQUIRED_PROVENANCE", "assert_provenance_complete",
           "leak_from_pair", "summarize_leak",
           "assert_choice_read_uninjectable"]
