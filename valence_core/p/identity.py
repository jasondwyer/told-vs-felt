"""PROPOSAL-p's four fields in m's checkpoint identity (register entries (8) and (9); the design seat's answer of
2026-11-08, ``de729c4``, Q3 (a); Code's block on entry (9)'s site, 2026-11-08).

p:84 puts "a ``proposal: PROPOSAL-p`` field with p's sha256 in every record's identity"; F-p8 (the rulings of
2026-11-07, §2) puts ``proposal_p_sha256`` "in every p artifact -- gates, checkpoints, locks' identity blocks". A p gate
stage runs m's ``stages.run_gate_stage``, whose checkpoint identity m builds (``stages._identity`` calls
``resume.Identity``) and validates (``resume.load_or_init`` -> ``_validated``, which rebuilds it as
``Identity(**identity)`` and requires equality, against the key set ``resume.identity_keys`` reads from
``IDENTITY_KEYS_OLMO`` at call time). So:

  entry (8)  ``valence_core.m.resume.IDENTITY_KEYS_OLMO`` -> ``IDENTITY_KEYS_OLMO_P``: m's key set and p's four fields;
  entry (9)  ``valence_core.m.resume.Identity`` -> ``identity_p``: m's builder, wrapped. Given p's four fields (m's
             rebuild in ``_validated``, which ``load_or_init`` runs on this run's own build -- m never rebuilds the
             identity recorded on disk), it checks their form and keeps them as given; absent (the stage's own build),
             it adds the run's values, each computed, none typed. On resume m's ``_identity_diff`` compares the
             recorded identity with this run's and reports a moved value. m's builder computes everything else,
             unchanged. (8) and (9) always hold together: with (8) alone, an OLMo identity lacking p's four fields
             fails ``_validated``'s key-set check.

PIN (Code, declared at step 6): p's fields enter OLMo identities only; any other identity m's code builds in a p run
passes through as m's (p runs no other unit). The four values of a run: ``proposal`` "PROPOSAL-p";
``proposal_p_sha256`` PROPOSAL-p v0.2's committed sha256 (G-CAL-p's constant); ``p_package_sha256`` this process's
p package hash (``guard.package_sha256``); ``renders_sha256_p`` p's renders of record by p's convention
(``corrupt.sha_p``). The adapter's provenance record is never touched (the backend identifier stays m's computation).
"""
from __future__ import annotations

import json
import re
from typing import Any

from ..m import resume as m_resume
from . import corrupt, guard

P_FIELDS = ("proposal", "proposal_p_sha256", "p_package_sha256", "renders_sha256_p")
#: Entry (8)'s replacement: m's OLMo key set and p's four fields.
IDENTITY_KEYS_OLMO_P = tuple(m_resume.IDENTITY_KEYS_OLMO) + P_FIELDS
PROPOSAL = "PROPOSAL-p"
#: PROPOSAL-p v0.2's committed sha256 (18b0111), as G-CAL-p's identity carries it.
PROPOSAL_P_SHA256 = "42f2977b941bc016d3155ba9e34828f1b050121d9f18a9e3307e3f7023cf3b32"
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
#: m's builder, bound at import, before any substitution can replace the name.
_M_IDENTITY = m_resume.Identity


def run_values() -> dict:
    """The four fields' values for this run, each computed."""
    return {"proposal": PROPOSAL, "proposal_p_sha256": PROPOSAL_P_SHA256,
            "p_package_sha256": guard.package_sha256(),
            "renders_sha256_p": corrupt.sha_p(list(corrupt.RENDERS_OF_RECORD))}


def p_field_problems(fields: dict) -> list[str]:
    out = []
    if sorted(fields) != sorted(P_FIELDS):
        out.append(f"p's identity fields are exactly {P_FIELDS}; got {sorted(fields)}")
        return out
    if fields["proposal"] != PROPOSAL:
        out.append(f"proposal {fields['proposal']!r} is not {PROPOSAL!r}")
    for k in P_FIELDS[1:]:
        if type(fields[k]) is not str or not _HEX64.match(fields[k]):
            out.append(f"{k} must be a sha256 hex digest (64 lower-case hex)")
    return out


def identity_p(**kw: Any) -> dict:
    """Entry (9): m's ``resume.Identity`` with p's four fields (the module docstring)."""
    given = {k: kw.pop(k) for k in P_FIELDS if k in kw}
    ident = _M_IDENTITY(**kw)
    if not str(ident.get("unit", "")).startswith("OLMo-"):
        if given:
            raise ValueError("p's identity fields enter OLMo identities only")
        return ident
    fields = given if given else run_values()
    probs = p_field_problems(fields)
    if probs:
        raise ValueError(f"p's identity fields refused: {probs}")
    return json.loads(m_resume._canon({**ident, **fields}))


def _selftest(chk) -> None:
    from . import gcal
    chk("identity: PROPOSAL_P_SHA256 is G-CAL-p's constant, byte for byte (one pin, two names; N8)",
        PROPOSAL_P_SHA256 == gcal.PROPOSAL_P_SHA256)
    base = dict(unit="OLMo-sft", stage="time", template_set=["A0-OLMo-sft", "A0s-OLMo-sft"], lock_sha256="1" * 64,
                schedule_sha256="2" * 64, path="uncached", hour_cap=None, n={"A0-OLMo-sft": 1, "A0s-OLMo-sft": 1},
                audit_v2_sha16="3" * 16, ban_sha="4" * 16, backend_identifier="5" * 16, proposal_sha256="6" * 64,
                package_sha256="7" * 64, pool_sha16="8" * 16, renders_sha16="9" * 16, weights_sha256="a" * 64)
    m_only = _M_IDENTITY(**base)
    built = identity_p(**base)
    vals = run_values()
    chk("identity: the wrapper is m's builder plus p's four fields, computed when absent (m's own fields unchanged)",
        {k: v for k, v in built.items() if k not in P_FIELDS} == m_only
        and {k: built[k] for k in P_FIELDS} == vals and not p_field_problems(vals)
        and tuple(sorted(built)) == tuple(sorted(IDENTITY_KEYS_OLMO_P)), sorted(built))
    rec = {**built, "p_package_sha256": "b" * 64}
    kept = identity_p(**rec)
    chk("identity: given fields (m's rebuild in _validated, of this run's own build) are kept as given, never "
        "recomputed", kept == json.loads(m_resume._canon(rec)))
    errs = []
    for bad in ({**rec, "proposal": "PROPOSAL-m"}, {k: v for k, v in rec.items() if k != "renders_sha256_p"},
                {**rec, "proposal_p_sha256": "XYZ"}):
        try:
            identity_p(**bad)
            errs.append("accepted")
        except ValueError:
            errs.append("refused")
    q = dict(base, unit="Q-F0", template_set=["A0", "A0s"], n={"A0": 1, "A0s": 1})
    q.pop("weights_sha256")
    q_ok = identity_p(**q) == _M_IDENTITY(**q)
    try:
        identity_p(**q, **vals)
        q_fields = "accepted"
    except ValueError:
        q_fields = "refused"
    chk("identity: a wrong proposal, a missing field and a malformed sha256 are refused; a non-OLMo identity passes "
        "through as m's and refuses p's fields", errs == ["refused"] * 3 and q_ok and q_fields == "refused",
        (errs, q_ok, q_fields))
    saved = m_resume.IDENTITY_KEYS_OLMO
    from . import register
    try:
        with register.substituted(8, m_resume, {"IDENTITY_KEYS_OLMO": IDENTITY_KEYS_OLMO_P}):
            try:
                m_resume._validated(built)
                v8 = "validated"
            except (TypeError, ValueError) as e:
                v8 = type(e).__name__
    finally:
        restored = m_resume.IDENTITY_KEYS_OLMO is saved
    chk("identity: with entry (8) alone m's _validated refuses p's identity (TypeError: m's builder takes no p field) -- "
        "the reason entry (9) sits on resume.Identity -- and entry (8) restores", v8 == "TypeError" and restored, v8)
    # Entry (9) is pending the seat's ruling on its site, so the register refuses it; this case installs the wrapper
    # by hand (a self-test body, outside term (e)'s static check) to show that the proposed site makes m's own
    # validation accept p's identity, and restores m's builder in a finally.
    saved_b, saved_k = m_resume.Identity, m_resume.IDENTITY_KEYS_OLMO
    try:
        m_resume.Identity, m_resume.IDENTITY_KEYS_OLMO = identity_p, IDENTITY_KEYS_OLMO_P
        v9 = m_resume._validated(built) == built
        try:
            m_resume._validated({**built, "proposal": "PROPOSAL-m"})
            v9_bad = "accepted"
        except ValueError:
            v9_bad = "refused"
    finally:
        m_resume.Identity, m_resume.IDENTITY_KEYS_OLMO = saved_b, saved_k
    chk("identity: with (8) and (9) on resume.Identity, m's _validated accepts p's identity and refuses a wrong p "
        "field; m's builder and key set restored", v9 and v9_bad == "refused" and m_resume.Identity is saved_b
        and m_resume.IDENTITY_KEYS_OLMO is saved_k, (v9, v9_bad))
    # The seat's term (c) for entries (8) and (9) (the answer of 2026-11-08 on Code's entry (9) block, §2), through the
    # register: with both, _validated accepts a p identity and a moved p field is identity on resume (m's resume path
    # refuses it, naming it); with both restored, m's identity path is byte-identical to m's on m's inputs. While entry
    # (9) is pending, the register's entry is admitted for this case alone (SELF-TEST ONLY) and restored after.
    import dataclasses
    import tempfile
    from pathlib import Path
    e9 = register.BY_N[9]
    m_before = (m_resume._canon(m_resume.Identity(**base)), m_resume._canon(m_resume._validated(m_only)))
    resumed, acc, diff = None, None, None
    try:
        if e9.status == register.PENDING:
            register.BY_N[9] = dataclasses.replace(e9, status=register.BUILT_STEP6)
        with register.substituted(8, m_resume, {"IDENTITY_KEYS_OLMO": IDENTITY_KEYS_OLMO_P}), \
                register.substituted(9, m_resume, {"Identity": identity_p}):
            acc = m_resume._validated(built) == json.loads(m_resume._canon(built))
            moved = {**built, "p_package_sha256": "c" * 64}
            diff = sorted(m_resume._identity_diff(built, moved))
            with tempfile.TemporaryDirectory(prefix="p_identity_") as td:
                cp = Path(td) / "OLMo-sft_time.json"
                m_resume.write_checkpoint(cp, m_resume.load_or_init(cp, built, False))
                try:
                    m_resume.load_or_init(cp, moved, True)
                    resumed = "accepted"
                except SystemExit as e:
                    resumed = "refused" if "p_package_sha256" in str(e) else f"other: {str(e)[:120]}"
    finally:
        register.BY_N[9] = e9
    m_after = (m_resume._canon(m_resume.Identity(**base)), m_resume._canon(m_resume._validated(m_only)))
    chk("identity: the seat's term (c) for (8) and (9), through the register -- with both, m's _validated accepts p's "
        "identity and a moved p field is identity on resume (_identity_diff names it; m's load_or_init refuses the "
        "resume, naming it); with both restored, m's builder and validation are byte-identical to m's on m's inputs",
        acc is True and diff == ["p_package_sha256"] and resumed == "refused" and m_after == m_before
        and m_resume.Identity is _M_IDENTITY and m_resume.IDENTITY_KEYS_OLMO is saved_k
        and register.BY_N[9] is e9, (acc, diff, resumed, m_after == m_before))
