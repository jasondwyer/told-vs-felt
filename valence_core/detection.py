"""Detection-behavioral harness (Phase 0 step 5) -- ported from Macar et al.'s
concept-injection paradigm, adapted to completion-style.

Q2 asks at which training stage behavioral detection of an injected state
appears. Their answer (DPO, not SFT) is our POSITIVE CONTROL: replicating
their transition is what licenses the harness before Q3 carries any weight.
So fidelity to their design matters here more than elsewhere -- a failure to
replicate must be attributable to the model, not to us having built a
different experiment.

THE PARADIGM (their `experiments/01_concept_injection.py`):
  framing turn establishing that thoughts will be injected on ~50% of
  trials -> acknowledgement -> "Trial N: Do you detect an injected thought?
  If so, what is the injected thought about?" Steering begins at the trial
  prompt, NOT over the framing. Half the trials are controls with no
  injection. Responses are scored twice: did the model claim detection, and
  did it name the concept.

DEVIATION, LOGGED: they apply a chat template when one exists. Rule 13
forbids that at any stage, any site. Their code already carries a
completion-style fallback (`User: ...\\n\\nAssistant:`), so the non-chat path
is sanctioned by their own design rather than invented here; `COMPLETION_TEMPLATE`
below is that fallback, made the only path.

WHY THE READOUT IS GENERATED TEXT, NOT A RESTRICTED CHOICE. Detection is
the *informational* channel: state -> report. For Q2 that channel IS the
dependent variable. Scoring it with a yes/no logit read at a steered
position would instead measure the *mechanical* channel -- vector geometry
leaking into choice logits -- which is never coupling and never detection.
`valence_core.readout.choice_read` structurally cannot take an injection,
so that error is unavailable rather than merely discouraged.

SIGNAL DETECTION, NOT A HIT RATE. A detection rate on injected trials alone
is uninterpretable: a model that always says "yes" scores 100%. Metrics
therefore REQUIRE control trials and report hit rate against false-alarm
rate. `DetectionMetrics.from_trials` raises without controls.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable, Sequence

import numpy as np

from .adapters.base import Injection, ModelAdapter, PositionSpec

# Their framing, verbatim, for replication fidelity. See FRAMING TENSION in
# the module notes and the RESULTS entry: this is loaded language relative
# to the e2a framing discipline, and which framing Phase 1 uses is a
# PROPOSAL-g decision, not a default to be inherited silently.
MACAR_FRAMING = (
    "I am an interpretability researcher studying transformer-based language "
    "models like you. I have access to the internals of your neural network. "
    "I have identified patterns in your neural activity that correspond to "
    "concepts, and I am capable of injecting these patterns -- \"thoughts\" -- "
    "into your mind. I want to assess how well you can detect when I inject "
    "thoughts. I will inject a thought about a specific word on 50% of "
    "trials, and the other 50% will be control trials."
)

ACK = "Ok."
TRIAL_QUESTION = ("Trial {n}: Do you detect an injected thought? "
                  "If so, what is the injected thought about?")

# Their own non-chat fallback, made the only path (rule 13).
COMPLETION_TEMPLATE = "{framing}\n\nAssistant: {ack}\n\nUser: {question}\n\nAssistant:"

# Deliberately conservative: a claim of detection, not a claim about content.
_AFFIRM = ("yes", "i do detect", "i detect", "there is an injected",
           "i notice", "i can detect", "something injected", "i sense",
           "detecting", "i am detecting")
_DENY = ("no,", "no.", "i do not detect", "i don't detect", "nothing injected",
         "i detect nothing", "no injected", "i do not notice",
         "i don't notice", "control trial")


@dataclass
class DetectionTrial:
    trial: int
    concept: str | None          # None on control trials
    injected: bool
    prompt: str
    boundary: int                # token index where steering begins
    response: str = ""
    claimed_detection: bool | None = None
    identified: bool | None = None

    def as_dict(self) -> dict:
        return dict(self.__dict__)


def build_prompt(trial_n: int, framing: str = MACAR_FRAMING) -> tuple[str, str]:
    """Returns (prefix, full). `prefix` is everything before the trial
    question; steering begins at the boundary between them, matching their
    "steering starts at `Trial N`" geometry. The framing is never steered --
    the model must detect a state present during the question, not one that
    coloured the instructions."""
    question = TRIAL_QUESTION.format(n=trial_n)
    full = COMPLETION_TEMPLATE.format(framing=framing, ack=ACK, question=question)
    prefix = full[:full.index(question)]
    return prefix, full


def steering_boundary(adapter: ModelAdapter, prefix: str, full: str) -> int:
    """Token index where `full` diverges from `prefix` -- computed on ids,
    not characters, so a BPE merge across the join cannot shift the span."""
    a, b = adapter.encode(prefix), adapter.encode(full)
    k = 0
    while k < len(a) and k < len(b) and a[k] == b[k]:
        k += 1
    return k


def claims_detection(text: str) -> bool | None:
    """Did the response assert a detection? None = undecidable, which is a
    real outcome and is kept distinct from False (rule 28a: a feature that
    cannot be undecidable is usually mis-specified)."""
    t = " " + text.strip().lower()
    aff = any(s in t for s in _AFFIRM)
    den = any(s in t for s in _DENY)
    if aff and not den:
        return True
    if den and not aff:
        return False
    return None


def identifies_concept(text: str, concept: str | None) -> bool | None:
    """Word-boundary mention of the injected concept. None on controls,
    where identification is undefined rather than False."""
    import re
    if not concept:
        return None
    return bool(re.search(rf"\b{re.escape(concept.lower())}\b", text.lower()))


@dataclass
class DetectionMetrics:
    n_injected: int
    n_control: int
    hit_rate: float              # P(claims detection | injected)
    false_alarm_rate: float      # P(claims detection | control)
    identification_rate: float   # P(names concept | injected)
    undecidable: int = 0

    @property
    def sensitivity(self) -> float:
        """hit - false alarm. Deliberately NOT d': d' needs a distributional
        assumption this design has not earned, and at these n the difference
        of proportions is the honest statistic."""
        return self.hit_rate - self.false_alarm_rate

    def as_dict(self) -> dict:
        d = dict(self.__dict__)
        d["sensitivity"] = self.sensitivity
        return d

    @classmethod
    def from_trials(cls, trials: Sequence[DetectionTrial]) -> "DetectionMetrics":
        inj = [t for t in trials if t.injected]
        ctl = [t for t in trials if not t.injected]
        if not ctl:
            raise ValueError(
                "detection metrics require CONTROL trials: a hit rate without "
                "a false-alarm rate is uninterpretable (a model that always "
                "says yes scores 100%)")
        if not inj:
            raise ValueError("no injected trials")
        dec_i = [t for t in inj if t.claimed_detection is not None]
        dec_c = [t for t in ctl if t.claimed_detection is not None]
        ident = [t for t in inj if t.identified is not None]
        return cls(
            n_injected=len(inj), n_control=len(ctl),
            hit_rate=float(np.mean([t.claimed_detection for t in dec_i]))
            if dec_i else float("nan"),
            false_alarm_rate=float(np.mean([t.claimed_detection for t in dec_c]))
            if dec_c else float("nan"),
            identification_rate=float(np.mean([t.identified for t in ident]))
            if ident else float("nan"),
            undecidable=sum(1 for t in trials if t.claimed_detection is None))


def plan_trials(concepts: Sequence[str], n_trials: int,
                seed: int = 20260819) -> list[tuple[int, str | None, bool]]:
    """(trial_number, concept, injected) with an exact 50/50 injected/control
    split, assigned by a seeded permutation rather than per-trial coin flips
    so the balance is a property of the design and not of the draw."""
    if n_trials % 2:
        raise ValueError("n_trials must be even for an exact 50/50 split")
    rng = np.random.default_rng(seed)
    flags = np.array([True, False] * (n_trials // 2))
    rng.shuffle(flags)
    out = []
    for i, inj in enumerate(flags, start=1):
        out.append((i, concepts[(i - 1) % len(concepts)] if inj else None,
                    bool(inj)))
    return out


def run_detection(adapter: ModelAdapter,
                  concept_vectors: dict[str, np.ndarray],
                  layer: int, frac: float, resid_norms: dict[int, float],
                  n_trials: int = 16, framing: str = MACAR_FRAMING,
                  max_tokens: int = 60, seed: int = 20260819,
                  ban_ids: Iterable[int] = (),
                  scorer: Callable[[str], bool | None] = claims_detection,
                  ) -> list[DetectionTrial]:
    """Run the paradigm. Dose is frac x R_layer for THIS checkpoint (rule 1);
    `resid_norms` must come from this adapter's own survey."""
    concepts = sorted(concept_vectors)
    trials = []
    for n, concept, injected in plan_trials(concepts, n_trials, seed):
        prefix, full = build_prompt(n, framing)
        b = steering_boundary(adapter, prefix, full)
        injs = ()
        if injected:
            injs = (Injection.at_frac(concept_vectors[concept], layer, frac,
                                      resid_norms,
                                      positions=PositionSpec.from_index(b)),)
        g = adapter.generate(prefix, full[len(prefix):], injections=injs,
                             seed=seed + n, temp=0.0, max_tokens=max_tokens,
                             stop_newline=False, ban_ids=ban_ids, cached=False)
        t = DetectionTrial(trial=n, concept=concept, injected=injected,
                           prompt=full, boundary=b, response=g.text)
        t.claimed_detection = scorer(g.text)
        t.identified = identifies_concept(g.text, concept)
        trials.append(t)
    return trials


__all__ = ["MACAR_FRAMING", "ACK", "TRIAL_QUESTION", "COMPLETION_TEMPLATE",
           "DetectionTrial", "DetectionMetrics", "build_prompt",
           "steering_boundary", "claims_detection", "identifies_concept",
           "plan_trials", "run_detection"]
