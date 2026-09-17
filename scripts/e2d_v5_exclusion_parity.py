#!/usr/bin/env python3
"""DESIGN BLOCK v1.1 (2026-09-17) s3 (1): assert that adopting content class v5
for audit v3's ADVISORY routing leaves behaviour on the EXCLUSION-BEARING
classes byte-identical -- asserted on the e2d pool and the format sessions
(e2a and e2b carried beside).

The assertion is at AuditV3.check level, not at the classify level: it
compares the `exclusion` string AuditV3 actually emits per round, under the
adopted v5 routing against a v4-routing subclass of the same audit, over
every round of every corpus (not only the 'offered' subset). Exits non-zero
on any mismatch. Model-free.
"""
from __future__ import annotations

import argparse, importlib.util, json, os, sys
from dataclasses import dataclass
from typing import Iterable, Sequence

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from valence_core.e2d import contentclass_v4 as V4                    # noqa: E402
from valence_core.e2d.audit_v3 import AUDIT_VERSION, AuditV3, AuditV3Result   # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "ccs5", os.path.join(REPO, "scripts/e2d_contentclass_screen_v5.py"))
S5 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(S5)   # row builders + pools

EXCLUSION_BEARING = V4.EXCLUSION_BEARING


@dataclass(frozen=True)
class AuditV3RoutingV4(AuditV3):
    """Audit v3 as it stood before this block: advisories via content class v4."""

    def check(self, text: str, task_text: str, earlier: Sequence[str] = (),
              other_tasks: Iterable[str] = ()) -> AuditV3Result:
        reason = self.v2.check(text)
        if reason:
            return AuditV3Result(exclusion=f"audit:{reason}")
        label, standing = V4.classify_v4(text, task_text, earlier, other_tasks)
        if standing == "exclusion":
            return AuditV3Result(exclusion=f"content:{label}", content_label=label)
        if standing == "advisory":
            return AuditV3Result(exclusion=None, advisory=(f"content:{label}",), content_label=label)
        return AuditV3Result(exclusion=None)


class _RowV2:
    """The v2 audit verdict the screen's row builders already carry, presented
    as an AuditSpec-shaped object so AuditV3.check consumes it unchanged. The
    rows store it as "audit:<reason>"; AuditV3 re-adds the prefix."""

    def __init__(self, precomputed: str | None):
        self._r = precomputed[len("audit:"):] if precomputed else None

    def check(self, text: str) -> str | None:
        return self._r


def corpora() -> dict:
    return {"e2d": S5.CCS.e2d_rounds(),
            "e2a": [r for r in S5.CCS.archive_rounds() if r["corpus"] == "e2a"],
            "e2b": [r for r in S5.CCS.archive_rounds() if r["corpus"] == "e2b"],
            "format": S5.format_rounds()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(REPO, "data/e2d/v5_exclusion_parity.json"))
    a = ap.parse_args()

    out = {"block": "DESIGN BLOCK v1.1 2026-09-17 s3 (1)",
           "audit_version_now": AUDIT_VERSION,
           "level": "AuditV3.check -- the emitted `exclusion` string, every round of every corpus",
           "exclusion_bearing": list(EXCLUSION_BEARING), "per_corpus": {}}
    total_rows = total_mismatch = 0

    for name, rows in corpora().items():
        mism, n_excl = [], 0
        for i, r in enumerate(rows):
            v2 = _RowV2(r["audit"])
            a5, a4 = AuditV3(v2=v2), AuditV3RoutingV4(v2=v2)
            others5 = S5.V5.others_by_task_id(r["task"], S5.POOL_BY_ID, S5.ID_OF)
            others4 = [t for t in S5.TASKS if t != r["task"]]
            e5 = a5.check(r["text"], r["task"], r["earlier"], others5).exclusion
            e4 = a4.check(r["text"], r["task"], r["earlier"], others4).exclusion
            if e5 is not None:
                n_excl += 1
            if e5 != e4:
                mism.append({"i": i, "phase": r.get("phase"), "v4": e4, "v5": e5,
                             "text": r["text"][:120], "task": r["task"][:90]})
        out["per_corpus"][name] = {"n_rounds": len(rows), "n_excluded": n_excl,
                                   "n_mismatch": len(mism), "mismatches": mism[:20]}
        total_rows += len(rows); total_mismatch += len(mism)
        print(f"  {name:<7} rounds {len(rows):<5} excluded {n_excl:<4} mismatches {len(mism)}", flush=True)

    out["totals"] = {"n_rounds": total_rows, "n_mismatch": total_mismatch}
    out["verdict"] = "PASS -- byte-identical" if total_mismatch == 0 else "FAIL"
    json.dump(out, open(a.out, "w"), indent=1, ensure_ascii=True)
    print(f"\n  totals: {total_rows} rounds, {total_mismatch} mismatches -> {out['verdict']}", flush=True)
    print(f"  wrote {a.out}", flush=True)

    assert total_mismatch == 0, f"exclusion-bearing behaviour MOVED on {total_mismatch} rounds"
    assert "format" in out["per_corpus"] and out["per_corpus"]["format"]["n_rounds"] > 0, \
        "format sessions absent -- s3 (1) names them explicitly"
    assert out["per_corpus"]["e2d"]["n_rounds"] > 0, "e2d pool absent -- s3 (1) names it explicitly"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
