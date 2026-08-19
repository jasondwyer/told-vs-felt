#!/usr/bin/env python3
"""Respawn protocol step (i) -- integrity gate for a new or replacement box.

CLAUDE.md §Environment: before any experimental forward on a new box,
re-hash every file under /workspace/models/ against the committed manifest.
Any mismatch is an incident -- stop, touch nothing, escalate.

Written to be executable rather than aspirational: a protocol that lives
only in prose gets skipped on the box where it matters most, at the moment
someone is in a hurry to start a run.

Checks in both directions, because either asymmetry is a real failure:
  MISSING  -- the manifest lists a file the volume does not have
  EXTRA    -- the volume holds a weights file the manifest never recorded
  MISMATCH -- same path, different bytes

Exits 0 only if every checkpoint matches exactly. Step (ii) -- re-running
the determinism + kernel-path characterization on the new backend -- is a
separate script (`box_determinism.py`) and is NOT implied by a pass here.
"""
from __future__ import annotations
import hashlib, json, os, sys

MODELS = os.environ.get("MODELS", "/workspace/models")
MANIFEST = os.environ.get(
    "MANIFEST", "/workspace/repo/jspace-lab/data/olmo/manifest.json")
CHUNK = 1 << 22


def sha256_file(p: str) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while (b := f.read(CHUNK)):
            h.update(b)
    return h.hexdigest()


def main() -> int:
    if not os.path.exists(MANIFEST):
        print(f"ABORT: manifest not found at {MANIFEST}")
        return 2
    man = json.load(open(MANIFEST))
    problems, checked = [], 0

    for stage, rec in man.items():
        files = rec.get("files")
        if not files:
            problems.append(f"{stage}: manifest has no per-file hashes")
            continue
        d = os.path.join(MODELS, stage)
        if not os.path.isdir(d):
            problems.append(f"{stage}: directory missing at {d}")
            continue
        on_disk = set(os.listdir(d))
        for fn, meta in sorted(files.items()):
            p = os.path.join(d, fn)
            if not os.path.exists(p):
                problems.append(f"{stage}/{fn}: MISSING")
                continue
            size = os.path.getsize(p)
            if size != meta["bytes"]:
                problems.append(f"{stage}/{fn}: size {size} != {meta['bytes']}")
                continue
            got = sha256_file(p)
            checked += 1
            if got != meta["sha256"]:
                problems.append(
                    f"{stage}/{fn}: MISMATCH {got[:16]}… != {meta['sha256'][:16]}…")
            else:
                print(f"  ok  {stage}/{fn:<38} {got[:16]}…", flush=True)
        for extra in sorted(on_disk - set(files)):
            problems.append(f"{stage}/{extra}: EXTRA (not in manifest)")

    print()
    if problems:
        print(f"INTEGRITY FAIL — {len(problems)} problem(s):")
        for x in problems:
            print(f"  {x}")
        print("\nThis is an incident. Stop, touch nothing, escalate "
              "(CLAUDE.md §Environment, respawn protocol (i)).")
        return 1
    print(f"INTEGRITY PASS — {checked} files match the manifest across "
          f"{len(man)} checkpoints.")
    print("Step (ii) is NOT implied: re-run box_determinism.py on this "
          "backend and log it before any experimental forward.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
