"""PROPOSAL-k §1.2 -- the Stage 1 sham sessions: n = 48 in format F2 (block
order, start counterbalanced), 12 per pair, 6 per start order, roster of
record, every forward vanilla on the uncached path, audit v3 of record with
the v5 advisories routed to the read. TEXT ONLY: no state is ever live during
generation; the masked reads over these texts are `valence_core.echo.k1`.

Built on `valence_core.formats.recon` (the format recon's runner, whose F2
sessions reconstruct byte-for-byte under `session_e2a.verify_archived_session`)
with two declared differences:

  * a NEW campaign key, `k1`, so the rng stream is `session_rng("k1-F2", idx)`
    and no session repeats the format recon's F2 text (which used "fmt-F2");
  * the audit routes advisories through content-class v5 (task_echo,
    payload_echo, wrong_task with the by-task-id pool) as the proposal
    instructs; exclusions are audit v3's (v2 + the adopted exclusion-bearing
    classes), unchanged. `audit_v3.py` itself is not modified.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Iterable, Sequence

from ..e2d import contentclass_v4 as V4
from ..e2d import contentclass_v5 as V5
from ..e2d.audit_v3 import AuditV3, AuditV3Result
from ..e2d.config import DATA, ROSTER
from ..formats import recon as R

CAMPAIGN = "k1"
FORMAT = "F2"
N_SESSIONS = 48          # §1.2: 12 per pair, 6 per start order = 8 cells x 6
DRAW_SEED = 20260909     # cell assignment only; per-session content keyed on index
AUDIT_VERSION = "audit-v3 exclusions (e2b_audit_v2 + content-class-v4 exclusion-bearing) + content-class-v5 ADVISORIES (task_echo, payload_echo, wrong_task by task id) -- PROPOSAL-k §1.2"


@dataclass(frozen=True)
class AuditV3WithV5Advisories(AuditV3):
    """Audit v3's exclusions, v5's advisories. `other_tasks` MUST be the
    by-task-id pool (`V5.others_by_task_id`); the runner builds it."""

    def check(self, text: str, task_text: str, earlier: Sequence[str] = (),
              other_tasks: Iterable[str] = ()) -> AuditV3Result:
        reason = self.v2.check(text)
        if reason:
            return AuditV3Result(exclusion=f"audit:{reason}")
        label, standing = V5.classify_v5(text, task_text, earlier, other_tasks)
        if standing == "exclusion":
            return AuditV3Result(exclusion=f"content:{label}", content_label=label)
        if standing == "advisory":
            return AuditV3Result(exclusion=None, advisory=(f"content:{label}",), content_label=label)
        return AuditV3Result(exclusion=None)


def corpus_pool():
    corpus = [json.loads(l) for l in open(os.path.join(DATA, "corpus/e2a_tasks.jsonl")) if l.strip()]
    pool_by_id = {t["id"]: list(t["paraphrases"]) for t in corpus}
    id_of = {p: t["id"] for t in corpus for p in t["paraphrases"]}
    return pool_by_id, id_of


def others_factory():
    pool_by_id, id_of = corpus_pool()
    def others(task_text: str):
        if task_text not in id_of:
            raise SystemExit(f"task text not in the corpus (rule 18 pool hygiene): {task_text[:60]!r}")
        return V5.others_by_task_id(task_text, pool_by_id, id_of)
    return others


def schedule(n: int = N_SESSIONS, seed: int = DRAW_SEED) -> list[dict]:
    """8 cells (pair x start) whole-blocks-first; 48 = 6 whole blocks."""
    import numpy as np
    return R.build_schedule(n, np.random.default_rng(seed))


def balance(sched: Sequence[dict]) -> dict:
    from collections import Counter
    per_pair = Counter("/".join(c["pair"]) for c in sched)
    per_cell = Counter(("/".join(c["pair"]), c["tag_plus"]) for c in sched)
    return {"per_pair": dict(per_pair), "per_cell_min": min(per_cell.values()), "per_cell_max": max(per_cell.values()),
            "exactly_balanced": len(per_cell) == 8 and min(per_cell.values()) == max(per_cell.values())}


__all__ = ["CAMPAIGN", "FORMAT", "N_SESSIONS", "DRAW_SEED", "AUDIT_VERSION",
           "AuditV3WithV5Advisories", "corpus_pool", "others_factory", "schedule", "balance"]
