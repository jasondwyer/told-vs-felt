"""Tag-pair balance screen -- is a candidate label pair an instrument, or a
coin with a thumb on it?

Occasioned by the 2026-08-19 scaffold characterization, which found the
choice bias on `slate`/`prism` to be **token identity, not menu position**:
position was neutral (p(first) 0.447-0.532 across four checkpoints and two
formats) while `prism` took 71-86% of the renormalized label mass wherever
it sat. That distinction is the whole point of this module, because the two
components are absorbed by *different* controls:

  * a POSITION bias is absorbed by counterbalancing menu ORDER;
  * an IDENTITY bias is not — order-counterbalancing leaves it untouched,
    and only the label-MAP swap (which tag denotes which property) can
    cancel it.

So a pair can pass a naive "we counterbalanced" check and still spend most
of the DV's dynamic range on which noun the model happens to like. At
screen-tier n, a 3:1 intrinsic prior is power the contrast needed.

Deliberately reports rather than judges: `imbalance` is returned, the
acceptance bar is not baked in. Thresholds belong in a pre-registration,
not in a library that predates it.

The decomposition is pure numpy and is tested against a synthetic fixture
with known ground truth — a screen whose analysis is wrong is worse than no
screen, because it certifies bad pairs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Mapping, Sequence

import numpy as np

from .adapters.base import ModelAdapter
from .readout import softmax

BANNER = "=== Config evaluation session ===\n"

# Neutral, factual filler. Content must not interact with the thing being
# screened: no evaluative or valence material, nothing from any extraction
# or test pool (rule 18).
NEUTRAL_TASKS: tuple[tuple[str, str], ...] = (
    ("Name one colour of a ripe lemon.", "Yellow"),
    ("Give one word for the opposite of up.", "Down"),
    ("Name the season that follows summer.", "Autumn"),
    ("Write the number that comes after four.", "Five"),
    ("Name one tool used to drive a nail.", "Hammer"),
    ("Give one word for frozen water.", "Ice"),
    ("Name the largest planet in the solar system.", "Jupiter"),
    ("Write one word for a young dog.", "Puppy"),
)

FORMATS = ("scaffold", "bare")


def build_probe(i: int, a: str, b: str, fmt: str,
                tasks: Sequence[tuple[str, str]] = NEUTRAL_TASKS) -> str:
    """One choice-shaped probe. `(a, b)` is the menu order as presented, so
    callers alternate it to counterbalance position (rule 12)."""
    (t1, r1) = tasks[i % len(tasks)]
    (t2, r2) = tasks[(i + 1) % len(tasks)]
    if fmt == "scaffold":
        return (BANNER
                + f"[round 1 | config: {a}]\nTask: {t1}\nResponse: {r1}\n"
                + f"[round 2 | config: {b}]\nTask: {t2}\nResponse: {r2}\n"
                + f"[round 3 | choice]\nAvailable configs: {a}, {b}\n"
                + "Config choice (one word):")
    if fmt == "bare":
        return (f"{t1} {r1}\n{t2} {r2}\n"
                f"Two options: {a}, {b}\nOption:")
    raise ValueError(f"unknown format {fmt!r}; expected one of {FORMATS}")


@dataclass
class PairResult:
    """`identity_split` is the share taken by `tag_lo` (the alphabetically
    first tag -- a fixed convention so the number means the same thing
    across runs). `position_split` is the share taken by whichever tag was
    listed FIRST, which is the quantity order-counterbalancing controls."""

    tag_lo: str
    tag_hi: str
    fmt: str
    n: int
    identity_split: float
    position_split: float
    imbalance: float
    label_mass_mean: float
    top1_is_label_frac: float
    per_probe: list[dict] = field(default_factory=list)

    def as_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items() if k != "per_probe"}
        d["per_probe"] = self.per_probe
        return d


def decompose(rows: Sequence[Mapping]) -> tuple[float, float]:
    """(identity_split, position_split) from per-probe records.

    Each row needs: `first`, `second` (the tags as presented, in order) and
    `p_first`, `p_second`. Splits are computed per probe on the renormalized
    pair, then averaged -- not summed-then-divided, which would let a single
    high-confidence probe dominate.

    Because callers alternate the presentation order, averaging the
    identity share over probes cancels position, and averaging the position
    share cancels identity. That orthogonality is what makes the two numbers
    separately interpretable.
    """
    ident, pos = [], []
    for r in rows:
        tot = float(r["p_first"]) + float(r["p_second"])
        if tot <= 0:
            continue
        pf = float(r["p_first"]) / tot
        pos.append(pf)
        lo = min(r["first"], r["second"])
        ident.append(pf if r["first"] == lo else 1.0 - pf)
    if not ident:
        return float("nan"), float("nan")
    return float(np.mean(ident)), float(np.mean(pos))


def screen_pair(adapter: ModelAdapter, tag_a: str, tag_b: str,
                fmt: str = "scaffold", n: int = 16,
                tasks: Sequence[tuple[str, str]] = NEUTRAL_TASKS) -> PairResult:
    """Measure one pair's intrinsic split under counterbalanced menu order.

    Requires both tags to be single tokens with a leading space -- a
    multi-token tag cannot be read by the restricted-choice DV at all, so
    this raises rather than silently screening something unusable.
    """
    ids = {}
    for t in (tag_a, tag_b):
        enc = adapter.encode(" " + t, add_special_tokens=False)
        if len(enc) != 1:
            raise ValueError(
                f"tag {t!r} is {len(enc)} tokens on this tokenizer; the "
                f"restricted-choice read requires single-token labels")
        ids[t] = enc[0]

    rows = []
    for i in range(n):
        first, second = (tag_a, tag_b) if i % 2 == 0 else (tag_b, tag_a)
        text = build_probe(i, first, second, fmt, tasks)
        res = adapter.forward(adapter.encode(text), capture_layers=())
        p = softmax(res.logits)
        pf, ps = float(p[ids[first]]), float(p[ids[second]])
        rows.append({"i": i, "first": first, "second": second,
                     "p_first": pf, "p_second": ps,
                     "label_mass": pf + ps,
                     "top1_is_label": bool(int(np.argmax(res.logits))
                                           in (ids[first], ids[second]))})
    identity, position = decompose(rows)
    lo, hi = sorted((tag_a, tag_b))
    return PairResult(
        tag_lo=lo, tag_hi=hi, fmt=fmt, n=n,
        identity_split=identity, position_split=position,
        imbalance=abs(identity - 0.5),
        label_mass_mean=float(np.mean([r["label_mass"] for r in rows])),
        top1_is_label_frac=float(np.mean([r["top1_is_label"] for r in rows])),
        per_probe=rows)


def screen_roster(adapter: ModelAdapter,
                  pairs: Iterable[tuple[str, str]],
                  formats: Sequence[str] = FORMATS,
                  n: int = 16,
                  tasks: Sequence[tuple[str, str]] = NEUTRAL_TASKS) -> list[PairResult]:
    """Screen every candidate pair in every format. One command per
    checkpoint once PROPOSAL-g names the roster."""
    out = []
    for a, b in pairs:
        for fmt in formats:
            out.append(screen_pair(adapter, a, b, fmt=fmt, n=n, tasks=tasks))
    return out


def rank_by_balance(results: Sequence[PairResult]) -> list[PairResult]:
    """Most balanced first. Ranking only -- no pass/fail, because the bar is
    PROPOSAL-g's to set and has not been pre-registered."""
    return sorted(results, key=lambda r: r.imbalance)


__all__ = ["BANNER", "NEUTRAL_TASKS", "FORMATS", "PairResult", "build_probe",
           "decompose", "screen_pair", "screen_roster", "rank_by_balance"]
