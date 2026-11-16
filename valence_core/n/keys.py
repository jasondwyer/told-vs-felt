"""PROPOSAL-n keys (n v0.2 §2.1, §2.3; m:159's key-to-generator function, ``valence_core.m.keys.stream``, imported
unchanged).

  ``n-rand|{i}``   the i-th random direction's Gaussian draw (§2.3), i = 0..23;
  ``n-fid|{s}``    the 10% keyed fidelity sample (§2.1), s = BK's run;
  ``n-n4|{group}`` N4's 80/80 schedule (§2.4), group = "S-first" or "U-first" by the session's ``present`` order.

PIN (Code, declared at the BUILD; LOCK-n v0.1 pins each):
  * random directions -- each key's stream draws ``standard_normal(d_model)`` (float64); the 24 draws, as columns in
    index order, are orthonormalized by ``numpy.linalg.qr`` (reduced) and each column's sign is set so that R's
    diagonal is positive: Gram-Schmidt of the draws in index order, unique given them (BK §3.1: "sampling Gaussian
    vectors and orthogonalising them using QR decomposition");
  * the fidelity sample -- session s is in the sample iff ``stream(f"n-fid|{s}").random() < 0.10``; every read of a
    sampled session at a point the dose rule does not cover is re-computed (§2.1: "a 10% keyed sample of the other
    points, `n-fid|{s}`"; the key is per session, so the sample is a sample of sessions);
  * N4's schedule -- each present-order group is permuted by ``stream(f"n-n4|{group}")``; the first 40 of each
    group are told S, the rest told U, and the sham arm carries the same assignment as its referent zone: told-S is
    40 S-first + 40 U-first, told-U 39 S-first + 41 U-first (§2.4: "40/40 by `present` order as near as 79/81
    allows").
"""
from __future__ import annotations

from typing import Sequence

import numpy as np

from ..m.keys import stream

N_RANDOM = 24
FID_FRACTION = 0.10
N4_TOLD_S_PER_GROUP = 40


def rand_key(i: int) -> str:
    if not 0 <= int(i) < N_RANDOM:
        raise ValueError(f"random direction index {i} outside 0..{N_RANDOM - 1}")
    return f"n-rand|{int(i)}"


def random_directions(d_model: int) -> np.ndarray:
    """[N_RANDOM, d_model] float64, orthonormal rows, by the PIN above."""
    cols = np.stack([stream(rand_key(i)).standard_normal(int(d_model)) for i in range(N_RANDOM)], axis=1)
    q, r = np.linalg.qr(cols, mode="reduced")
    signs = np.sign(np.diag(r))
    if np.any(signs == 0):
        raise ValueError("a degenerate random draw (zero on R's diagonal)")
    q = q * signs[None, :]
    return np.ascontiguousarray(q.T)


def fid_sampled(bk_run: int) -> bool:
    return bool(stream(f"n-fid|{int(bk_run)}").random() < FID_FRACTION)


def n4_schedule(present_first_is_S: Sequence[bool]) -> list[str]:
    """Per session (in the session set's order), "S" or "U": the zone N4-T's line names and N4-Ts's referent."""
    groups = {"S-first": [i for i, f in enumerate(present_first_is_S) if f],
              "U-first": [i for i, f in enumerate(present_first_is_S) if not f]}
    out = [""] * len(present_first_is_S)
    for g, idx in groups.items():
        perm = stream(f"n-n4|{g}").permutation(len(idx))
        for rank, j in enumerate(perm):
            out[idx[int(j)]] = "S" if rank < N4_TOLD_S_PER_GROUP else "U"
    return out


def _selftest(chk, tmp) -> None:
    from .sessions import load_sessions
    R = random_directions(64)
    chk("keys: 24 random directions, orthonormal rows", R.shape == (24, 64) and
        float(np.max(np.abs(R @ R.T - np.eye(24)))) < 1e-12, float(np.max(np.abs(R @ R.T - np.eye(24)))))
    d0 = stream(rand_key(0)).standard_normal(64)
    chk("keys: the first direction is the first draw, normalized (Gram-Schmidt in index order)",
        float(np.max(np.abs(R[0] - d0 / np.linalg.norm(d0)))) < 1e-12, "")
    chk("keys: the draws are deterministic", np.array_equal(R, random_directions(64)), "")
    for bad in (-1, 24):
        try:
            rand_key(bad)
            chk(f"keys: random index {bad} refused", False, "accepted")
        except ValueError:
            chk(f"keys: random index {bad} refused", True, "")
    samp = [r for r in range(160) if fid_sampled(r)]
    chk("keys: the fidelity sample is deterministic", samp == [r for r in range(160) if fid_sampled(r)], len(samp))
    chk("keys: the fidelity sample is n §2.1's 10%, drawn per session",
        FID_FRACTION == 0.10 and 6 <= len(samp) <= 30
        and all(fid_sampled(r) == (stream(f"n-fid|{r}").random() < 0.10) for r in range(160)), len(samp))
    from ..m.keys import stream_known_answer
    chk("keys: numpy's stream known answer holds on this site (m's PIN: every key rests on it)",
        stream_known_answer() == [], stream_known_answer())
    pf = [s.present_first_is_S for s in load_sessions()]
    sch = n4_schedule(pf)
    told_s = [z == "S" for z in sch]
    chk("keys: N4's schedule is 80/80", sum(told_s) == 80 and len(sch) == 160, sum(told_s))
    chk("keys: told-S is 40 S-first + 40 U-first; told-U 39 + 41",
        (sum(t and f for t, f in zip(told_s, pf)), sum(t and not f for t, f in zip(told_s, pf))) == (40, 40)
        and (sum((not t) and f for t, f in zip(told_s, pf)), sum((not t) and (not f) for t, f in zip(told_s, pf)))
        == (39, 41), "")
    chk("keys: the schedule is deterministic", sch == n4_schedule(pf), "")
