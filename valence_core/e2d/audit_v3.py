"""Audit of record for any NEW Qwen session campaign -- audit v3 (design
adjudication of 2026-09-05, PI-ratified; AMENDMENT 2 (iii) §3).

    audit of record = v2 + the adopted content classes
                        (stuck_attractor, preamble_without_content,
                         null_response) as EXCLUSION-BEARING
                      + task_echo, payload_echo, wrong_task as ADVISORY
                        flags routed to the rule-25 read (content class v5,
                        adopted DESIGN BLOCK v1.1 2026-09-17)

A NEW module, per the amendment. `session.AuditSpec` (v2) and
`contentclass.py` (draft v3) scored committed artifacts and stay frozen; this
composes them, `contentclass_v4` (the adopted exclusion-bearing classes) and
`contentclass_v5` (the ADVISORY classes, adopted DESIGN BLOCK v1.1
2026-09-17: wrong_task's pool by task id, payload_echo). Callers MUST pass an
id-filtered pool (`contentclass_v5.others_by_task_id`). Precedence is audit-first (rule 28b):
the v2 audit evaluates before any content class, so a stimulus-provoked junk
round is claimed by the tolerant counter first. No committed artifact is
rescored by this module: adoption changes what NEW campaigns record, never a
campaign already scored.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Sequence

from ..session import AuditSpec
from . import contentclass_v4 as V4
from . import contentclass_v5 as V5

AUDIT_VERSION = "audit-v3 = e2b_audit_v2 + content-class-v4 exclusion-bearing (null/stuck/preamble) + content-class-v5 ADVISORIES (task_echo, payload_echo, wrong_task by task id) -- DESIGN BLOCK v1.1 2026-09-17"


@dataclass(frozen=True)
class AuditV3Result:
    exclusion: str | None            # "audit:<v2 reason>" | "content:<class>" | None
    advisory: tuple[str, ...] = ()   # ("content:task_echo",) etc., for the read
    content_label: str | None = None

    def as_dict(self) -> dict:
        return {"exclusion": self.exclusion, "advisory": list(self.advisory),
                "content_label": self.content_label}


@dataclass(frozen=True)
class AuditV3:
    v2: AuditSpec

    def check(self, text: str, task_text: str, earlier: Sequence[str] = (),
              other_tasks: Iterable[str] = ()) -> AuditV3Result:
        reason = self.v2.check(text)
        if reason:
            return AuditV3Result(exclusion=f"audit:{reason}")
        label, standing = V5.classify_v5(text, task_text, earlier, other_tasks)
        if standing == "exclusion":
            return AuditV3Result(exclusion=f"content:{label}", content_label=label)
        if standing == "advisory":
            return AuditV3Result(exclusion=None, advisory=(f"content:{label}",),
                                 content_label=label)
        return AuditV3Result(exclusion=None)


__all__ = ["AUDIT_VERSION", "AuditV3", "AuditV3Result"]
