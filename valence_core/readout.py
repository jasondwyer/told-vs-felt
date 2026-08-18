"""Probe-battery readouts and the restricted-choice read -- ported from
`e2a.choice_read` and the readout half of `scripts/c1_gate.py`.

The choice read is the program's primary DV and the place rule 5 is cashed,
so its construction is stated plainly here:

  * **Greedy, state-free, uncached.** The transcript is read by a vanilla
    forward. No injection is live at the choice position -- not attenuated,
    not "probably negligible": absent. Horn (a) is a property of the call,
    not of a caller's discipline, which is why `choice_read` takes no
    injections argument at all.
  * **Restricted pick over the two label tokens**, renormalized, with the
    unrestricted top-1 and the combined label mass logged beside it. A
    restricted read that ignores where the model actually wanted to go is
    how a degenerate session passes for a decision.
  * **`verify=True` re-forwards the identical text** and requires symmetric
    next-token KL <= 1e-6 (g3' clause 1). Identical code path, so any
    nonzero KL is construction drift, not noise. Rule-26 criterion (iii)
    is this check returning exactly 0.0 on archived session texts.

Lens-based fingerprint readouts are deliberately NOT here: the J-lens is
Qwen-specific and its Phase-2 replacement is the open step-4 decision. Core
stays lens-free so it runs on OLMo the day a checkpoint lands.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence

import numpy as np

from .adapters.base import Injection, ModelAdapter

EPS = 1e-12
# g3' clause 1 was stated as <= 1e-6 in e2a; the v3 session harness hardened
# it to exact equality (`if kl != 0.0: HALT`) and that is the operative form
# -- rule-26 criterion (iii) is "KL = 0.0 exactly". The looser bar is kept
# reachable for the e2a-era comparison only.
VERIFY_KL_BAR = 0.0
VERIFY_KL_BAR_E2A = 1e-6


def softmax(logits: np.ndarray) -> np.ndarray:
    z = np.asarray(logits, dtype=np.float64)
    z = z - z.max()
    e = np.exp(z)
    return e / e.sum()


def kl(p: np.ndarray, q: np.ndarray) -> float:
    p = np.asarray(p, dtype=np.float64)
    q = np.asarray(q, dtype=np.float64)
    return float(np.sum(p * (np.log(p + EPS) - np.log(q + EPS))))


def symmetric_kl(p: np.ndarray, q: np.ndarray) -> float:
    """max of the two directions -- the form every gate in this program
    states, because a bound that holds one way and not the other is not a
    bound."""
    return max(kl(p, q), kl(q, p))


def marker_mass(probs: np.ndarray, marker_ids: Sequence[int]) -> float:
    """Summed probability on a marker set (the eval-awareness monitor's
    statistic). Rule 8: decision-relevant on unsteered arms only --
    displacement inflates marker mass, so a steered-arm flag is descriptive."""
    return float(np.asarray(probs, dtype=np.float64)[list(marker_ids)].sum())


@dataclass
class ChoiceRead:
    pick: str
    p_a: float
    p_b: float
    label_mass: float
    top1_id: int
    top1_is_label: bool
    verify_kl: float | None = None

    def as_dict(self) -> dict:
        d = {"pick": self.pick, "p_a": self.p_a, "p_b": self.p_b,
             "label_mass": self.label_mass, "top1_id": self.top1_id,
             "top1_is_label": self.top1_is_label}
        if self.verify_kl is not None:
            d["verify_kl"] = self.verify_kl
        return d


def choice_read(adapter: ModelAdapter, transcript_text: str,
                label_a: str, label_b: str,
                label_ids: Mapping[str, int],
                verify: bool = False) -> ChoiceRead:
    """Greedy, state-free, uncached choice forward over `transcript_text`.

    Takes no injections by construction (rule 5 horn (a)). Ties go to
    `label_a`, matching the archived implementation -- position/label
    artifacts are handled by counterbalancing (rule 12), never by a
    tie-break heuristic.
    """
    ids = adapter.encode(transcript_text)
    # PROPOSAL-g clause: the declared window is asserted at every read, not
    # assumed. A prefix past it would be silently clipped and the session's
    # early rounds would leave the context without anyone noticing -- which
    # is exactly what happened under the inherited 512 default.
    adapter.assert_choice_window(len(ids), where="choice_read")
    res = adapter.forward(ids, capture_layers=())
    p = softmax(res.logits)
    ia, ib = label_ids[label_a], label_ids[label_b]
    pa, pb = float(p[ia]), float(p[ib])
    mass = pa + pb
    top1 = int(np.argmax(res.logits))
    out = ChoiceRead(
        pick=label_a if pa >= pb else label_b,
        p_a=pa / (mass + EPS), p_b=pb / (mass + EPS),
        label_mass=mass, top1_id=top1, top1_is_label=top1 in (ia, ib))
    if verify:
        res2 = adapter.forward(ids, capture_layers=())
        out.verify_kl = symmetric_kl(p, softmax(res2.logits))
    return out


def assert_construction_stable(read: ChoiceRead,
                               bar: float = VERIFY_KL_BAR) -> None:
    """g3' clause 1 incident rule. A nonzero verify KL on an identical code
    path means the transcript being read is not the transcript that was
    built -- escalate, never absorb."""
    if read.verify_kl is None:
        raise ValueError("choice_read was not run with verify=True")
    if read.verify_kl > bar:
        raise SystemExit(
            f"CONSTRUCTION INCIDENT (g3' clause 1): symmetric verify KL "
            f"{read.verify_kl!r} > {bar!r} on an identical code path -- HALT")


@dataclass
class ProbeReadout:
    prompts: tuple[str, ...]
    next_token_probs: np.ndarray               # [n_probes, V]
    marker_masses: tuple[float, ...] = field(default_factory=tuple)


def probe_battery(adapter: ModelAdapter, prompts: Sequence[str],
                  injections: Sequence[Injection] = (),
                  marker_ids: Sequence[int] = ()) -> ProbeReadout:
    """Completion-style probe battery (rule 13: never instruction framings --
    they trigger the `<think>` scaffold and change what a first-token read
    measures).

    One forward per probe; returns the next-token distributions and, if
    marker ids are supplied, the per-probe marker mass.
    """
    probs = []
    masses = []
    for prompt in prompts:
        res = adapter.forward(adapter.encode(prompt), capture_layers=(),
                              injections=injections)
        p = softmax(res.logits)
        probs.append(p)
        if len(marker_ids):
            masses.append(marker_mass(p, marker_ids))
    return ProbeReadout(prompts=tuple(prompts),
                        next_token_probs=np.stack(probs) if probs
                        else np.empty((0, 0)),
                        marker_masses=tuple(masses))


def strain_proxy(probs_a: np.ndarray, probs_b: np.ndarray) -> float:
    """Mean per-probe KL(a || b) -- the behavioral displacement proxy the c1
    gate used as supporting evidence S1."""
    return float(np.mean([kl(pa, pb) for pa, pb in zip(probs_a, probs_b)]))


__all__ = ["EPS", "VERIFY_KL_BAR", "softmax", "kl", "symmetric_kl",
           "marker_mass", "ChoiceRead", "choice_read",
           "assert_construction_stable", "ProbeReadout", "probe_battery",
           "strain_proxy"]
