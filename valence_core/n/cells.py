"""PROPOSAL-n -- the cell files: the read runner's production writer and its reader (n v0.2 §2.8: "a resume is
skip-only; checkpoints atomic"; ``schema``'s FILES and CAPTURES paragraphs).

A cell is one (arm, direction, dose point) of a stage: ``<stem>.json`` (``schema.CELL_SCHEMA``) beside one capture
array per capture layer (ADDENDUM-n1 §6.2's band), ``<stem>.L{layer}.npy`` (``schema.capture_filename``): float32
[``schema.capture_capacity(arm)``, d_model] -- 40 rows for N1-R's cells, 160 otherwise -- row r the cell's r-th
record, rows from ``capture_rows`` on unwritten. ``append_record`` writes one read's row into each array in place
(flushed and fsynced; the array is created, zero-filled, at the cell's first read), then the JSON by m's
``resume.atomic_write_json`` (imported unchanged) with each layer's sha256 over the written rows [0, capture_rows)
-- so a JSON on disk never names a row its arrays lack. A crash between the two leaves a row written past the JSON's
``capture_rows`` -- at a cell's first read, arrays with no JSON beside them. ``load_cell`` reads only the JSON's rows
(no JSON is a new cell), and the next append writes that row again: at the first read it creates every layer's array
afresh, overwriting a file of that name whatever its shape, since no JSON names a row of it. A row is written once:
the arrays are never rewritten whole (Code's form, for I/O over a campaign's ~4.8 GB).

NO MAP OUTLIVES ITS USE (Code's form, after the drafts' review: a memory map holds a file descriptor, and a
campaign's ~138 cells × 31–32 layers held open would pass a container's descriptor limit). ``append_record`` maps
each layer's file read-write for its one row -- "w+" at the cell's first read, "r+" after -- writes, flushes, drops
the map and fsyncs the file. ``load_cell`` checks every layer through a read-only map it drops, and hands the arrays
(read-only) only to a reader that asks (``keep_arrays``). Between reads a cell is its JSON and its layers' running
hashers.

Model-free: no torch, no adapter, no quarantined module. Nothing here lists a directory it was not given.
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

import numpy as np

from ..m import resume as m_resume
from . import schema

DTYPE = np.dtype("<f4")


def _fsync_dir(d: Path) -> None:
    m_resume._fsync_dir(d)


def _reject_constant(name: str):
    raise ValueError(f"non-finite JSON constant {name}")


def json_bytes(data: bytes, name: str) -> dict:
    """A cell (or report) file's bytes as JSON: NaN and Infinity refused (m's writer never writes them), an object
    required. A caller that hashes a file parses the very bytes it hashed (the runner's report)."""
    try:
        obj = json.loads(data.decode("utf-8"), parse_constant=_reject_constant)
    except ValueError as e:                              # UnicodeDecodeError and JSONDecodeError are ValueErrors
        raise SystemExit(f"CELL UNREADABLE at {name} ({type(e).__name__}); left untouched -- refusing")
    if not isinstance(obj, dict):
        raise SystemExit(f"CELL UNREADABLE at {name} (not a JSON object) -- refusing")
    return obj


def read_json(p: Path) -> dict:
    """A cell file as JSON (``json_bytes`` of one read). m's ``resume._read`` is not used: it checks m's own
    checkpoint state."""
    try:
        data = Path(p).read_bytes()
    except OSError as e:
        raise SystemExit(f"CELL UNREADABLE at {Path(p).name} ({type(e).__name__}); left untouched -- refusing")
    return json_bytes(data, Path(p).name)


def redacted(e: BaseException) -> str:
    """A schema refusal's field path alone, never its message's values (n §4's blinding: no margin, log-probability
    or pick reaches stdout or a raw)."""
    return str(e).split(": ", 1)[0][:160]


def cell_path(root: str | os.PathLike, arm: str, direction_id: str, dose_label: str) -> Path:
    return Path(root) / schema.cell_filename(arm, direction_id, dose_label)


def capture_path(root: str | os.PathLike, cell_name: str, layer: int) -> Path:
    return Path(root) / schema.capture_filename(cell_name, layer)


def _row_bytes(row: np.ndarray) -> bytes:
    return np.ascontiguousarray(row, dtype=DTYPE).tobytes(order="C")


def rows_sha256(arr: np.ndarray, n: int) -> str:
    """sha256 of rows [0, n) as float32 little-endian bytes in row order (the cell's ``capture_sha256`` form)."""
    h = hashlib.sha256()
    for i in range(n):
        h.update(_row_bytes(arr[i]))
    return h.hexdigest()


@dataclass
class Captures:
    """A cell's running sha256 per layer over its written rows, and its capture arrays only where ``load_cell`` was
    asked to keep them (``keep_arrays``), read-only. ``append_record`` returns the hashers alone: no map is held
    between reads."""
    arrays: dict = field(default_factory=dict)          # layer -> read-only np.memmap [capacity, d_model], if kept
    hashers: dict = field(default_factory=dict)         # layer -> hashlib sha256 over rows [0, n)

    @property
    def size(self) -> int:
        """The layers whose running hash is held (0 for a new cell)."""
        return len(self.hashers)


def new_cell(identity: Mapping, arm: str, direction_id: str, dose_label: str) -> dict:
    name = schema.cell_filename(arm, direction_id, dose_label)
    layers = list(identity["capture_layers"])
    return {"schema": schema.CELL_SCHEMA, "stage_identity": dict(identity), "arm": arm,
            "direction_id": direction_id, "dose_label": dose_label, "records": [],
            "capture_files": {str(x): schema.capture_filename(name, x) for x in layers},
            "capture_rows": 0, "capture_sha256": {str(x): hashlib.sha256(b"").hexdigest() for x in layers}}


def _open_array(path: Path, capacity: int, d_model: int, mode: str) -> np.ndarray:
    """One layer's capture array mapped in ``mode`` ("r" to check or keep, "r+" to append a row), its dtype and
    shape checked. A missing or unreadable file stops with the module's SystemExit, never a bare OSError."""
    try:
        arr = np.load(path, mmap_mode=mode, allow_pickle=False)
    except (OSError, ValueError) as e:
        raise SystemExit(f"{path.name}: a capture array the cell names is missing or unreadable "
                         f"({type(e).__name__}) -- refusing")
    if arr.dtype != DTYPE or arr.shape != (capacity, d_model):
        raise SystemExit(f"{path.name}: a capture array of {arr.dtype} {tuple(arr.shape)}, not float32 "
                         f"({capacity}, {d_model})")
    return arr


def load_cell(root: str | os.PathLike, arm: str, direction_id: str, dose_label: str,
              identity: Mapping | None = None, *, keep_arrays: bool = False) -> tuple[dict, Captures]:
    """The cell and its layers' running hashers, rows [0, len(records)) checked through read-only maps: each layer's
    sha256 against the cell's, each row's sha16 against its record. A missing cell is a new one; an identity other
    than ``identity`` (when given) is refused -- never spliced (m:267). Each map is dropped once checked, unless
    ``keep_arrays``: a reader (G-READ-n's driver) then gets the arrays, read-only."""
    jp = cell_path(root, arm, direction_id, dose_label)
    if not jp.exists():
        if identity is None:
            raise FileNotFoundError(jp)
        return new_cell(identity, arm, direction_id, dose_label), Captures()
    cell = read_json(jp)
    try:
        schema.check_cell(cell, where=jp.name)
    except schema.SchemaError as e:
        raise SystemExit(f"{jp.name}: not a valid cell, at {redacted(e)}")
    if identity is not None and not m_resume.same_json(cell["stage_identity"], dict(identity)):
        raise SystemExit(f"{jp.name}: the stage identity on disk differs from this run's -- a resume is refused "
                         f"(skip-only, never spliced)")
    n = len(cell["records"])
    caps = Captures()
    if n == 0:
        return cell, caps
    ident = cell["stage_identity"]
    cap, d = schema.capture_capacity(arm), int(ident["d_model"])
    from ..adapters.base import sha16_arr
    for l in ident["capture_layers"]:
        arr = _open_array(capture_path(root, jp.name, l), cap, d, "r")
        h = hashlib.sha256()
        for i, rec in enumerate(cell["records"]):
            if sha16_arr(np.asarray(arr[i])) != rec["capture"]["sha16"][str(l)]:
                raise SystemExit(f"{jp.name}: record {i}'s layer {l} capture does not match its row")
            h.update(_row_bytes(arr[i]))
        if h.hexdigest() != cell["capture_sha256"][str(l)]:
            raise SystemExit(f"{jp.name}: layer {l}'s written rows do not hash to the cell's capture_sha256")
        caps.hashers[int(l)] = h
        if keep_arrays:
            caps.arrays[int(l)] = arr
        del arr                                          # an unkept map closes here: nothing else refers to it
    return cell, caps


def _fsync_file(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _write_row(path: Path, row_index: int, row: np.ndarray, capacity: int, d_model: int) -> None:
    """One row into one layer's array, its file mapped read-write for this write alone: created afresh ("w+",
    zero-filled) at the cell's first row, whatever file of that name is there -- an orphan of a crash before the
    cell's first JSON, which names no row of it -- else mapped "r+", dtype and shape checked. The row is written and
    flushed, the map dropped, the file fsynced."""
    if row_index == 0:
        arr = np.lib.format.open_memmap(path, mode="w+", dtype=DTYPE, shape=(capacity, d_model))
    else:
        arr = _open_array(path, capacity, d_model, "r+")
    arr[row_index] = row
    arr.flush()
    del arr                                              # the map closes here: nothing else refers to it
    _fsync_file(path)


def append_record(root: str | os.PathLike, cell: dict, caps: Captures, rec: dict,
                  captures: Mapping[int, np.ndarray]) -> tuple[dict, Captures]:
    """Add one checked read to its cell on disk: its row into each layer's array, in place and flushed, then the
    JSON. A record the schema refuses stops the stage with the failing field's path only (n §4's blinding: a refusal
    message may quote a value). ``caps`` is the cell's (``load_cell``'s or the last append's): its hashers are
    copied, never advanced, so a refused append leaves them as they were. Returns the new cell and its hashers, no
    map. At the cell's first read no cell file may be on disk; after it, every layer's running hash must be held."""
    ident = cell["stage_identity"]
    n = len(cell["records"])
    rec = dict(rec)
    rec["capture"] = dict(rec["capture"], row=n)
    try:
        schema.check_record(rec, ident)
    except schema.SchemaError as e:
        raise SystemExit(f"{rec.get('read_id')}: the schema refuses the record, at {redacted(e)}")
    layers = [int(x) for x in ident["capture_layers"]]
    cap, d = schema.capture_capacity(cell["arm"]), int(ident["d_model"])
    if n >= cap:
        raise SystemExit(f"{rec.get('read_id')}: the cell's {cap} capture rows are full")
    from ..adapters.base import sha16_arr
    rows = {}
    for l in layers:
        row = np.asarray(captures[l], dtype=DTYPE)
        if row.shape != (d,):
            raise ValueError(f"capture width {row.shape} is not ({d},)")
        if sha16_arr(row) != rec["capture"]["sha16"][str(l)]:
            raise SystemExit(f"{rec.get('read_id')}: layer {l}'s capture is not the record's sha16")
        rows[l] = row
    jp = cell_path(root, cell["arm"], cell["direction_id"], cell["dose_label"])
    if n == 0 and jp.exists():
        raise SystemExit(f"{jp.name}: a cell file is on disk for a cell appended as new -- refusing (arrays a JSON "
                         f"names are never created afresh)")
    missing = [l for l in layers if l not in caps.hashers]
    if n > 0 and missing:
        raise SystemExit(f"{jp.name}: no running hash is held for layers {missing} of a cell of {n} rows -- refusing")
    new = dict(cell, records=list(cell["records"]) + [rec], capture_rows=n + 1)
    hashers = {l: (caps.hashers[l].copy() if n > 0 else hashlib.sha256()) for l in layers}
    for l in layers:
        hashers[l].update(_row_bytes(rows[l]))
    new["capture_sha256"] = {str(l): hashers[l].hexdigest() for l in layers}
    try:
        schema.check_cell(new)
    except schema.SchemaError as e:
        raise SystemExit(f"{rec.get('read_id')}: the schema refuses the cell, at {redacted(e)}")
    for l in layers:
        _write_row(capture_path(root, jp.name, l), n, rows[l], cap, d)
    if n == 0:
        _fsync_dir(jp.parent)
    m_resume.atomic_write_json(jp, new)
    return new, Captures(hashers=hashers)


def done_read_ids(root: str | os.PathLike, plan_cells) -> set:
    """read_ids on disk in the given cells (a resume skips exactly these)."""
    out = set()
    for arm, did, dl in plan_cells:
        jp = cell_path(root, arm, did, dl)
        if jp.exists():
            cell = read_json(jp)
            out.update(r["read_id"] for r in cell["records"])
    return out


def _selftest(chk, tmp) -> None:
    from ..adapters.base import sha16_arr
    tmp = Path(tmp)
    tmp.mkdir(parents=True, exist_ok=True)
    # a small identity (the schema pins neither d_model nor n_layers): site 1 of 4, so the band is layers 2 and 3
    ident = dict(schema.example_identity(), d_model=8, layer=1, n_layers=4, capture_layers=[2, 3])
    schema.check_stage_identity(ident)
    rng = np.random.default_rng(3)
    layers = [str(x) for x in ident["capture_layers"]]

    def rec_and_caps(run, launch, arm="N1-V", did="valence", dl="+1"):
        rec = schema.example_record(ident, arm, did, dl, run, launch=launch)
        caps = {int(l): rng.standard_normal(ident["d_model"]).astype(np.float32) for l in layers}
        rec["capture"] = {"row": 0, "sha16": {l: sha16_arr(caps[int(l)]) for l in layers}}
        return rec, caps

    def kept(root=tmp, arm="N1-V", did="valence", dl="+1"):
        """The cell's arrays, read-only (``keep_arrays``): the load-back comparisons read rows through them."""
        return load_cell(root, arm, did, dl, identity=ident, keep_arrays=True)[1].arrays

    cell, caps = load_cell(tmp, "N1-V", "valence", "+1", identity=ident)
    chk("cells: a missing cell is a new, empty one", cell["records"] == [] and caps.size == 0, "")
    sent = []
    for i, run in enumerate((0, 1, 2)):
        r, c = rec_and_caps(run, 10 * i)
        sent.append(c)
        cell, caps = append_record(tmp, cell, caps, r, c)
    jp = cell_path(tmp, "N1-V", "valence", "+1")
    cell2, caps2 = load_cell(tmp, "N1-V", "valence", "+1", identity=ident, keep_arrays=True)
    same_rows = all(np.array_equal(np.asarray(caps2.arrays[int(l)][i]), sent[i][int(l)])
                    for i in range(3) for l in layers)
    chk("cells: three appended reads load back identical, rows in order, each layer's hash its written rows'",
        cell2 == cell and same_rows and [r["capture"]["row"] for r in cell2["records"]] == [0, 1, 2]
        and all(cell2["capture_sha256"][l] == rows_sha256(caps2.arrays[int(l)], 3) for l in layers), "")
    chk("cells: each layer's array is float32 [capacity, d_model], capacity 160 for N1-V",
        all(caps2.arrays[int(l)].shape == (160, 8) and caps2.arrays[int(l)].dtype == DTYPE for l in layers), "")
    del caps2
    p2 = capture_path(tmp, jp.name, 2)
    arr = np.load(p2, mmap_mode="r+")
    arr[3] = 7.0                                            # a crash between the writes: a row past the JSON
    arr.flush()
    del arr
    cell3, caps3 = load_cell(tmp, "N1-V", "valence", "+1", identity=ident)
    chk("cells: a row written past the JSON (a crash between the writes) is ignored; the JSON's rows load",
        len(cell3["records"]) == 3 and cell3["capture_sha256"] == cell["capture_sha256"], "")
    chk("cells: no map is held between reads: an append's and a checking load's Captures carry the layers' running "
        "hashers alone", caps.arrays == {} and caps3.arrays == {} and sorted(caps.hashers) == sorted(caps3.hashers)
        == [2, 3], (sorted(caps.arrays), sorted(caps3.arrays)))
    r, c = rec_and_caps(3, 30)
    cell4, caps4 = append_record(tmp, cell3, caps3, r, c)
    k4 = kept()
    chk("cells: the next append writes that row again", np.array_equal(np.asarray(k4[2][3]), c[2])
        and cell4["capture_sha256"]["2"] == rows_sha256(k4[2], 4), "")
    del k4
    arr = np.load(p2, mmap_mode="r+")
    arr[1, 0] += 1.0
    arr.flush()
    del arr
    try:
        load_cell(tmp, "N1-V", "valence", "+1", identity=ident)
        chk("cells: a tampered capture row is refused", False, "accepted")
    except SystemExit:
        chk("cells: a tampered capture row is refused", True, "")
    good_json = jp.read_bytes()
    forged = read_json(jp)                                  # the tampered row's sha16 written into its record
    arr = np.load(p2, mmap_mode="r")
    forged["records"][1]["capture"]["sha16"]["2"] = sha16_arr(np.asarray(arr[1]))
    del arr
    m_resume.atomic_write_json(jp, forged)
    try:
        load_cell(tmp, "N1-V", "valence", "+1", identity=ident)
        chk("cells: a tampered row whose record's sha16 is rewritten to match is refused by the layer's hash", False,
            "accepted")
    except SystemExit as e:
        chk("cells: a tampered row whose record's sha16 is rewritten to match is refused by the layer's hash",
            "capture_sha256" in str(e), str(e)[:120])
    jp.write_bytes(good_json)
    arr = np.load(p2, mmap_mode="r+")
    arr[1] = np.asarray(sent[1][2], dtype=DTYPE)
    arr.flush()
    del arr
    other = dict(ident, pod_id="another-pod")
    try:
        load_cell(tmp, "N1-V", "valence", "+1", identity=other)
        chk("cells: a resume under another identity is refused (never spliced)", False, "accepted")
    except SystemExit:
        chk("cells: a resume under another identity is refused (never spliced)", True, "")
    cell, caps = load_cell(tmp, "N1-V", "valence", "+1", identity=ident)
    r, c = rec_and_caps(4, 5)
    try:
        append_record(tmp, cell, caps, r, c)
        chk("cells: a launch index not after the cell's last is refused", False, "accepted")
    except SystemExit as e:
        chk("cells: a launch index not after the cell's last is refused", "refuses the cell" in str(e), str(e))
    r, c = rec_and_caps(4, 40)
    r["margin"] = "secret-123.456"                          # a type error: the schema's message quotes the value
    try:
        append_record(tmp, cell, caps, r, c)
        chk("cells: a refused record stops with its field's path alone, no value (n §4)", False, "accepted")
    except SystemExit as e:
        chk("cells: a refused record stops with its field's path alone, no value (n §4)",
            "refuses the record, at record.margin" in str(e) and "secret" not in str(e), str(e))
    r, c = rec_and_caps(4, 40)
    r["capture"]["sha16"][layers[0]] = "0" * 16
    try:
        append_record(tmp, cell, caps, r, c)
        chk("cells: a capture row that is not its record's sha16 is refused at the write", False, "accepted")
    except SystemExit as e:
        chk("cells: a capture row that is not its record's sha16 is refused at the write", "sha16" in str(e), str(e))
    r, c = rec_and_caps(4, 40)
    try:
        append_record(tmp, cell, Captures(), r, c)
        chk("cells: an append past a cell's first row without its layers' running hashes is refused", False,
            "accepted")
    except SystemExit as e:
        chk("cells: an append past a cell's first row without its layers' running hashes is refused",
            "running hash" in str(e), str(e)[:120])
    r, c = rec_and_caps(0, 0)
    try:
        append_record(tmp, new_cell(ident, "N1-V", "valence", "+1"), Captures(), r, c)
        chk("cells: a first append over a cell file on disk is refused (arrays a JSON names never made afresh)", False,
            "accepted")
    except SystemExit as e:
        chk("cells: a first append over a cell file on disk is refused (arrays a JSON names never made afresh)",
            "on disk" in str(e), str(e)[:120])
    r, c = rec_and_caps(4, 40)
    try:
        cell, caps = append_record(tmp, cell, caps, r, c)      # the same (cell, captures) the refusals were given
        k5 = kept()
        ok5 = len(cell["records"]) == 5 and np.array_equal(np.asarray(k5[2][4]), c[2]) and all(
            cell["capture_sha256"][l] == rows_sha256(k5[int(l)], 5) for l in layers)
        detail5 = ""
        del k5
    except SystemExit as e:
        ok5, detail5 = False, str(e)[:120]
    chk("cells: after refused appends, a valid one on the same (cell, captures) reloads verified: a refusal leaves "
        "the running hashes as they were", ok5, detail5)
    chk("cells: done_read_ids reads the cell's read_ids",
        done_read_ids(tmp, [("N1-V", "valence", "+1")]) == {x["read_id"] for x in cell["records"]}, "")
    chk("cells: nothing but the cell file and one array per layer, and no temp file, is left",
        sorted(p.name for p in tmp.iterdir()) == sorted([jp.name] + [schema.capture_filename(jp.name, int(l))
                                                                      for l in layers]),
        sorted(p.name for p in tmp.iterdir()))
    rcell, rcaps = load_cell(tmp, "N1-R", "rand_00", "+1", identity=ident)
    r, c = rec_and_caps(0, 0, arm="N1-R", did="rand_00")
    rcell, rcaps = append_record(tmp, rcell, rcaps, r, c)
    kr = kept(arm="N1-R", did="rand_00")
    chk("cells: an N1-R cell's arrays hold 40 rows (its capacity)",
        all(kr[int(l)].shape == (40, 8) for l in layers), "")
    del kr
    pr = capture_path(tmp, cell_path(tmp, "N1-R", "rand_00", "+1").name, 2)
    np.save(pr, np.zeros((39, 8), dtype=DTYPE), allow_pickle=False)
    try:
        load_cell(tmp, "N1-R", "rand_00", "+1", identity=ident)
        chk("cells: an array of another shape is refused", False, "accepted")
    except SystemExit as e:
        chk("cells: an array of another shape is refused", "not float32" in str(e), str(e)[:120])
    pr.unlink()
    try:
        load_cell(tmp, "N1-R", "rand_00", "+1", identity=ident)
        chk("cells: a missing capture array is the module's SystemExit, not a bare FileNotFoundError", False,
            "accepted")
    except SystemExit as e:
        chk("cells: a missing capture array is the module's SystemExit, not a bare FileNotFoundError",
            "missing" in str(e), str(e)[:120])
    ot = tmp / "orphan"                                     # a crash before a cell's first JSON: arrays, no JSON
    ot.mkdir()
    oname = cell_path(ot, "N1-V", "valence", "+1").name
    np.save(capture_path(ot, oname, 2), np.zeros((3, 5)), allow_pickle=False)     # float64 [3, 5]: no cell's shape
    capture_path(ot, oname, 3).write_bytes(b"not an array")
    try:
        ocell, ocaps = load_cell(ot, "N1-V", "valence", "+1", identity=ident)
        r, c = rec_and_caps(0, 0)
        ocell, ocaps = append_record(ot, ocell, ocaps, r, c)
        ko = kept(ot)
        ok_o = len(ocell["records"]) == 1 and all(
            ko[int(l)].shape == (160, 8) and ko[int(l)].dtype == DTYPE
            and np.array_equal(np.asarray(ko[int(l)][0]), c[int(l)])
            and ocell["capture_sha256"][l] == rows_sha256(ko[int(l)], 1) for l in layers)
        detail_o = ""
        del ko
    except SystemExit as e:
        ok_o, detail_o = False, str(e)[:120]
    chk("cells: a cell's first read overwrites orphan arrays of its name (a crash before its first JSON), whatever "
        "their shape or content; its rows and hashes then verify", ok_o, detail_o)
    ro_cell, ro = load_cell(tmp, "N1-V", "valence", "+1", identity=ident, keep_arrays=True)
    try:
        ro.arrays[2][0] = 1.0
        chk("cells: kept arrays (keep_arrays) are read-only", False, "written")
    except (ValueError, OSError):
        chk("cells: kept arrays (keep_arrays) are read-only", True, "")
