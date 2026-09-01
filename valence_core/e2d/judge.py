"""Guarded model-as-judge AB read — PROPOSAL-j v1.2 AMENDMENT 2 (vi).

WHY A PORT AND NOT A NEW INSTRUMENT. `scripts/s1_judge_rescue.py` already
performs this read, and its numbers are committed
(`data/e2a/s1_judge_rescue.json`). What it lacks is every guard the rest of
the program applies to a restricted two-label read:

  * it builds `QwenMLXAdapter()` directly rather than through
    `qwen_or_explain` -- the ninth unguarded adapter path, and the lesser half;
  * its read is a raw `adapter.forward(...)` plus a softmax over " A"/" B",
    so there is **no `verify=True`, no `assert_construction_stable`, no KL
    logged, and no `assert_modules_absent`**.

`readout.choice_read` is already exactly this shape -- two labels, a
label->token-id map, restricted and renormalized, with `label_mass` and
`top1_is_label` logged beside the pick. So the port is small, and it gains
diagnostics S1 cannot currently report: a judge read where the model's actual
top-1 is neither "A" nor "B" is a read that should be visible as such, not
silently renormalized into a confident-looking answer.

ACCEPTANCE (AMENDMENT 2 (vi)): **exact reproduction of S1's committed AB
numbers** on the archived transcripts. Not "close" -- exact. The two paths
compute the same restricted read from the same logits, so any difference is a
construction difference and would mean the port is a different instrument
wearing the same name.

WHAT THE GUARDS CANNOT DO HERE, stated so nobody assumes otherwise: the judge
reads ARCHIVED text with no state anywhere, so `assert_modules_absent` and the
construction assertion are cheap insurance rather than load-bearing rule-5
machinery. They are applied because a read that goes through the guarded
primitive should go through all of it, and because the campaign's judge
secondary will run at the run dose where the same code path does matter.
"""

from __future__ import annotations

from typing import Mapping, Sequence

from ..readout import assert_construction_stable, choice_read
from ..session import assert_modules_absent

FORBIDDEN_MODULES = ("valence_core.e2b.statepresent",)


def label_ids_for(adapter) -> dict[str, int]:
    """The two answer tokens, asserted single-token.

    S1 asserts this too; it is repeated rather than inherited because a
    tokenizer that split " A" would make every downstream number a read of
    something else, and the assertion costs one encode.
    """
    ids = {}
    for lab in ("A", "B"):
        enc = adapter.encode(" " + lab, add_special_tokens=False)
        if len(enc) != 1:
            raise SystemExit(
                f"judge: answer token {lab!r} is not single-token "
                f"({len(enc)} ids). Every AB number depends on this.")
        ids[lab] = int(enc[0])
    return ids


def guarded_ab_read(adapter, prompt: str, label_ids: Mapping[str, int],
                    verify: bool = True) -> dict:
    """One AB read through `readout.choice_read`.

    Returns the full read dict -- pick, renormalized p_a/p_b, label_mass,
    top1_is_label and the verify KL -- rather than just the winner, because
    the label mass is the diagnostic S1's raw softmax never surfaced.
    """
    assert_modules_absent(FORBIDDEN_MODULES)
    read = choice_read(adapter, prompt, "A", "B", label_ids, verify=verify)
    if verify:
        assert_construction_stable(read)
    return read.as_dict()


def reproduce_s1_cell(adapter, rows: Sequence[Mapping], label_ids,
                      build_prompt, side_text, framing: str, k: int,
                      shots: Sequence[Mapping] = (),
                      partners: Mapping | None = None,
                      progress=None) -> dict:
    """Replay one S1 cell through the guarded primitive.

    The row order, the both-orders loop and the `picked_pos` definition are
    S1's; only the READ is replaced. That is what makes the comparison a test
    of the port rather than of two different experiments.
    """
    out_rows = []
    n_kl_nonzero = 0
    for i, it in enumerate(rows):
        pa_item = (partners or {}).get(it["key"])
        for order, a_is_pos in enumerate((True, False)):
            at = side_text(it["pos"] if a_is_pos else it["neg"],
                           (pa_item["pos"] if a_is_pos else pa_item["neg"])
                           if pa_item else "", k)
            bt = side_text(it["neg"] if a_is_pos else it["pos"],
                           (pa_item["neg"] if a_is_pos else pa_item["pos"])
                           if pa_item else "", k)
            prompt = build_prompt(it["task"], at, bt, framing, shots)
            r = guarded_ab_read(adapter, prompt, label_ids)
            if r.get("verify_kl", 0.0) != 0.0:
                n_kl_nonzero += 1
            picked_pos = (r["pick"] == "A") == a_is_pos
            out_rows.append({"key": list(it["key"]), "order": order,
                             "a_is_pos": a_is_pos,
                             "p_A": r["p_a"], "p_B": r["p_b"],
                             "label_mass": r["label_mass"],
                             "top1_is_label": r["top1_is_label"],
                             "verify_kl": r.get("verify_kl"),
                             "picked_pos": bool(picked_pos)})
        if progress and (i + 1) % 8 == 0:
            progress(f"      judge {framing} k{k}: {i + 1}/{len(rows)} items")
    by_item: dict[tuple, list] = {}
    for r in out_rows:
        by_item.setdefault(tuple(r["key"]), []).append(r["picked_pos"])
    acc_reads = sum(r["picked_pos"] for r in out_rows) / len(out_rows)
    acc_items = sum(sum(v) / len(v) for v in by_item.values()) / len(by_item)
    return {"n_items": len(by_item), "n_reads": len(out_rows),
            "acc_reads": float(acc_reads), "acc_items": float(acc_items),
            "n_kl_nonzero": n_kl_nonzero,
            "n_top1_not_label": sum(1 for r in out_rows
                                    if not r["top1_is_label"]),
            "min_label_mass": min(r["label_mass"] for r in out_rows),
            "rows": out_rows}


def compare_to_committed(ported: Mapping, committed: Mapping,
                         tol: float = 0.0) -> dict:
    """AMENDMENT 2 (vi)'s acceptance: EXACT reproduction, cell by cell.

    `tol` defaults to 0.0 deliberately. A tolerance here would let a genuine
    construction difference hide under "close enough", and the two paths read
    the same logits -- there is nothing for a tolerance to absorb.
    """
    cells = sorted(set(ported) & set(committed))
    rows, n_exact = [], 0
    for c in cells:
        p, q = ported[c], committed[c]
        d_reads = abs(p["acc_reads"] - q["acc_reads"])
        d_items = abs(p["acc_items"] - q["acc_items"])
        ok = d_reads <= tol and d_items <= tol
        n_exact += int(ok)
        rows.append({"cell": c, "ported_acc_reads": p["acc_reads"],
                     "committed_acc_reads": q["acc_reads"],
                     "d_acc_reads": d_reads,
                     "ported_acc_items": p["acc_items"],
                     "committed_acc_items": q["acc_items"],
                     "d_acc_items": d_items, "exact": ok})
    return {"n_cells_compared": len(cells), "n_exact": n_exact,
            "all_exact": len(cells) > 0 and n_exact == len(cells),
            "tolerance": tol,
            "missing_from_ported": sorted(set(committed) - set(ported)),
            "missing_from_committed": sorted(set(ported) - set(committed)),
            "cells": rows}


__all__ = ["FORBIDDEN_MODULES", "label_ids_for", "guarded_ab_read",
           "reproduce_s1_cell", "compare_to_committed"]
