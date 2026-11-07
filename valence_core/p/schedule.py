"""PROPOSAL-p's schedules (p v0.2 §4.1; ans2 Q4 (iii); register entry (2)).

m's builder (``valence_core.m.schedule.build_schedule_objects``) run under register entry (2), so every cell, pi and
session-key template is drawn from p's key families; the three OLMo units' eighteen files (campaign, G-TIME and
qualification, contrast and sham) are written under ``data/p/schedules/`` with p's own manifest, in m's schema names
and m's layout (``dumps_schedule``), as mf3 reuses them. The cells' construction (m:159-172) is m's by reference.

PIN (Code, declared at the p BUILD): m's ``_campaign_obj`` writes its ``key_template`` field as a literal
``m-sched|{unit}|{arm}|{b}`` (valence_core/m/schedule.py:512) rather than through ``keys.sched_key``; under entry (2)
the cells are drawn from ``p-sched|...``, so p sets that one field, after the call and inside the substitution, to
the active ``sched_key``'s own template form (asserted to be m's literal before the change). Under m's keys the
field is therefore m's literal byte for byte, and the term (c) self-test -- with m's own keys (no substitution), p's builder
reproduces ``data/m/schedules/``' OLMo files byte for byte -- holds; no cell, pi or key is touched. The field is p's
own output, set outside the register's form (it substitutes no m attribute): among the eighteen files, the six
campaign files' key templates are the only bytes that differ from what m's builder writes under entry (2). Flagged
for the seat in the BUILD entry.

PIN (Code, declared at the p BUILD): the canonical write (no ``out_dir``) is ``data/p/schedules``; a test write
(``out_dir`` given) goes through ``guard.refuse_test_out`` (never inside the repository); each file is
written once through ``guard.write_once_bytes`` (never through a link; the temp file opened ``O_NOFOLLOW``).
"""
from __future__ import annotations

import contextlib
import hashlib
import json
import os
from pathlib import Path
from typing import Mapping

from ..m import keys as m_keys
from ..m import schedule as m_schedule
from . import guard, keys

REPO = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO / "data" / "p" / "schedules"
M_OUT = m_schedule.DEFAULT_OUT
MANIFEST_NAME = m_schedule.MANIFEST_NAME
MANIFEST_SCHEMA = m_schedule.MANIFEST_SCHEMA
CONSTRUCTION = ("PROPOSAL-p v0.2 §4.1: PROPOSAL-m v1.11 m:159-172 by reference (valence_core.m.schedule's builder, "
                "imported unchanged), under p's six OLMo key families (register entry (2))")
N_FILES = 18
#: The one gate schedule whose pi, drawn from p-sched|..., equals m's from m-sched|... (permutation(4) has 24 values):
#: a coincidence of two different streams, recorded, not a shared stream.
SPEC_PI_COINCIDENCE = "OLMo-sft_qual_A0s-OLMo-sft.json"


class ScheduleRefusal(SystemExit):
    """A write refused before any file is written: a root p may not write, or a link or non-file on the way (exit 2)."""


class ScheduleStop(SystemExit):
    pass


def build_objects(*, p_keys: bool = True) -> dict[str, dict]:
    """The three OLMo units' schedule objects, keyed by file name; ``p_keys=False`` runs m's builder under m's own
    keys (the term (c) comparison)."""
    ctx = keys.substituted_keys() if p_keys else contextlib.nullcontext()
    with ctx:
        objs = m_schedule.build_schedule_objects()
        out = {n: o for n, o in objs.items() if o["unit"] in keys.OLMO_UNITS}
        for o in out.values():
            if o["kind"] != "campaign":
                continue
            lit = f"m-sched|{o['unit']}|{o['arm']}|{{b}}"
            if o["key_template"] != lit:
                raise ScheduleStop(f"SCHEDULE STOP: m's campaign key_template is {o['key_template']!r}, not the literal "
                                   f"{lit!r} the p BUILD's PIN names (valence_core/m/schedule.py:512)")
            o["key_template"] = m_keys.sched_key(o["unit"], o["arm"], "{b}")
    if len(out) != N_FILES:
        raise ScheduleStop(f"SCHEDULE STOP: {len(out)} OLMo schedule objects, expected {N_FILES}")
    return out


def file_blobs(*, p_keys: bool = True) -> dict[str, bytes]:
    blobs = {n: m_schedule.dumps_schedule(o).encode("utf-8") for n, o in sorted(build_objects(p_keys=p_keys).items())}
    manifest = {"schema": MANIFEST_SCHEMA, "construction": CONSTRUCTION,
                "files": {n: hashlib.sha256(b).hexdigest() for n, b in sorted(blobs.items())}}
    blobs[MANIFEST_NAME] = (json.dumps(manifest, sort_keys=True, indent=1) + "\n").encode("utf-8")
    return blobs


def write_schedule_files(out_dir: str | os.PathLike | None = None) -> dict[str, str]:
    """Write p's eighteen files and manifest (default data/p/schedules); an existing differing file is refused,
    never overwritten; identical files are left untouched. Returns {file name: sha256}."""
    try:
        if out_dir is None:
            out = DEFAULT_OUT
            lp = guard.no_link_problems(out, guard.P_ROOT)
            if lp:
                raise guard.GuardStop(f"GUARD STOP: {lp}")
        else:
            out = guard.refuse_test_out(out_dir)
    except guard.GuardStop as e:
        raise ScheduleRefusal(f"SCHEDULE REFUSED: {e}") from None
    blobs = file_blobs()
    links = [n for n in blobs if (out / n).is_symlink() or (out / (n + ".tmp")).is_symlink()
             or ((out / (n + ".tmp")).exists() and not (out / (n + ".tmp")).is_file())
             or ((out / n).exists() and not (out / n).is_file())]
    if links:
        raise ScheduleRefusal(f"SCHEDULE REFUSED: a link or non-file at a schedule path or its temp name ({links[:3]}); "
                              f"nothing written")
    clash = [n for n, b in blobs.items() if (out / n).exists() and (out / n).read_bytes() != b]
    if clash:
        raise RuntimeError(f"SCHEDULE MISMATCH: {len(clash)} existing file(s) in {out} differ from the "
                           f"regeneration ({clash[:3]}); refusing to overwrite")
    out.mkdir(parents=True, exist_ok=True)
    try:
        for n, b in blobs.items():
            guard.write_once_bytes(out / n, b, what="schedule file")
    except guard.GuardStop as e:
        raise ScheduleRefusal(f"SCHEDULE REFUSED: {e}") from None
    return {n: hashlib.sha256(b).hexdigest() for n, b in blobs.items()}


def verify_schedule_dir(out_dir: str | os.PathLike | None = None) -> list[str]:
    """[] iff every file is present and byte-identical to this machine's regeneration, and no other file is there."""
    d = Path(out_dir) if out_dir is not None else DEFAULT_OUT
    blobs = file_blobs()
    probs = [f"missing {n}" for n in sorted(blobs) if not (d / n).exists()]
    probs += [f"{n} differs from the regeneration" for n in sorted(blobs) if (d / n).exists()
              and (d / n).read_bytes() != blobs[n]]
    if d.is_dir():
        probs += [f"unlisted {p.name}" for p in sorted(d.glob("*.json")) if p.name not in blobs]
    return probs


def _cells_differ(a: Mapping, b: Mapping) -> bool:
    return a["cells"] != b["cells"] or a.get("pi") != b.get("pi")


def _selftest(chk) -> None:
    mb = file_blobs(p_keys=False)
    m_files = {n: (M_OUT / n).read_bytes() for n in mb if n != MANIFEST_NAME}
    chk("schedule: with m's own keys (no substitution), p's builder reproduces data/m/schedules/' eighteen OLMo files "
        "byte for byte (term (c))",
        len(m_files) == N_FILES and all(mb[n] == m_files[n] for n in m_files),
        [n for n in m_files if mb[n] != m_files[n]][:3])
    po, mo = build_objects(), build_objects(p_keys=False)
    chk("schedule: under p's keys every key template and session-key template is p's (p-sched, p-olmo*, "
        "p-olmo-items*) and none is m's",
        all(o["key_template"].startswith("p-sched|") and all(v.startswith("p-olmo") for v in o["session_keys"].values())
            for o in po.values()))
    camp = [n for n in po if po[n]["kind"] == "campaign"]
    chk("schedule: p's six campaign schedules are p's own draws -- each orders its cells differently from m's at the "
        "same name, over the same cell multiset (m:159's balance)",
        len(camp) == 6 and all(_cells_differ(po[n], mo[n]) for n in camp)
        and all(sorted(map(str, po[n]["cells"])) == sorted(map(str, mo[n]["cells"])) for n in camp))
    same_pi = sorted(n for n in po if po[n]["kind"] == "gate" and po[n]["pi"] == mo[n]["pi"])
    chk("schedule: of the twelve gate schedules' pi (a permutation(4), 24 values), exactly one equals m's by chance "
        "under a different key -- OLMo-sft qual A0s -- the coincidence the BUILD entry records",
        same_pi == [SPEC_PI_COINCIDENCE], same_pi)
    chk("schedule: m's four key functions are m's own after the builds (restoration, term (c))",
        all(getattr(m_keys, n) is keys._M[n] for n in keys._NAMES))
    pb = file_blobs()
    man = json.loads(pb[MANIFEST_NAME])
    chk("schedule: p's manifest names p's construction and the eighteen files' sha256s, in m's manifest schema",
        man["schema"] == MANIFEST_SCHEMA and man["construction"] == CONSTRUCTION and len(man["files"]) == N_FILES)
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        a = write_schedule_files(td)
        b = write_schedule_files(td)
        clean = verify_schedule_dir(td)
        (Path(td) / sorted(a)[0]).write_text("{}")
        try:
            write_schedule_files(td)
            refused = False
        except RuntimeError:
            refused = True
    chk("schedule: writes nineteen files that verify clean, re-runs identically, refuses a differing existing file",
        len(a) == 19 and a == b and clean == [] and refused)
    try:
        write_schedule_files(M_OUT)
        m_refused = False
    except ScheduleRefusal:
        m_refused = True
    chk("schedule: p writes nothing under data/m/schedules (refused before any write)", m_refused)
    outs = []
    with tempfile.TemporaryDirectory() as td:
        names = sorted(file_blobs())
        for case in ("tmp-link", "final-link"):
            d = Path(td) / case
            d.mkdir()
            if case == "tmp-link":
                (d / (names[0] + ".tmp")).symlink_to(Path(td) / "victim-tmp")
            else:
                (d / names[1]).symlink_to(Path(td) / "victim-final")
            try:
                write_schedule_files(d)
                outs.append("written")
            except (ScheduleRefusal, RuntimeError):
                written = [p for p in d.glob("*.json") if not p.is_symlink()]
                outs.append("refused" if not written else f"partial ({len(written)} written)")
        victims = [(Path(td) / v).exists() for v in ("victim-tmp", "victim-final")]
    for d in (DEFAULT_OUT.parent / "verdicts", DEFAULT_OUT):
        try:
            write_schedule_files(d)
            outs.append("written")
        except ScheduleRefusal:
            outs.append("refused")
    chk("schedule: a link at a temp name or at a schedule path is refused before any file is written, nothing written "
        "through it; a test write under data/p (data/p/schedules named explicitly included) is refused",
        outs == ["refused"] * 4 and victims == [False, False], (outs, victims))
