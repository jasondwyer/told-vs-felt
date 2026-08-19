#!/usr/bin/env python3
"""Per-file SHA-256 for every acquired bf16 checkpoint (step 2, item 1).

These hashes are the provenance anchors. Upstream file-identity is gone:
acquisition re-serialized every stage through save_pretrained, so our shard
files legitimately do NOT match the HF originals byte-for-byte. What anchors
the record is (pinned source revision) + (our output hashes) — the first says
where the weights came from, the second says exactly what we hold.

Hashes every file in each cast dir, not just the shards: a swapped
tokenizer or config is as capable of silently changing results as a swapped
shard, and is far easier to do by accident.
"""
from __future__ import annotations
import hashlib, json, os, sys, time

MODELS = "/workspace/models"
STAGES = ["base", "sft", "dpo", "instruct"]
CHUNK = 1 << 22


def sha256_file(p: str) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while (b := f.read(CHUNK)):
            h.update(b)
    return h.hexdigest()


def main() -> int:
    man_path = os.path.join(MODELS, "manifest.json")
    man = json.load(open(man_path))
    t0 = time.time()
    for s in STAGES:
        d = os.path.join(MODELS, s)
        files = sorted(os.listdir(d))
        fh = {}
        for fn in files:
            p = os.path.join(d, fn)
            t1 = time.time()
            fh[fn] = {"sha256": sha256_file(p), "bytes": os.path.getsize(p)}
            print(f"  {s}/{fn:<38} {fh[fn]['sha256'][:16]}… "
                  f"{fh[fn]['bytes']:>13,}  {time.time()-t1:5.1f}s", flush=True)
        # one aggregate over the per-file digests, in sorted filename order
        agg = hashlib.sha256(
            "".join(f"{k}:{fh[k]['sha256']}" for k in sorted(fh)).encode()
        ).hexdigest()
        man[s]["files"] = fh
        man[s]["files_aggregate_sha256"] = agg
        man[s]["n_files"] = len(fh)
        print(f"  {s}: {len(fh)} files, aggregate {agg[:16]}…\n", flush=True)
    json.dump(man, open(man_path, "w"), indent=1)
    print(f"manifest updated: {man_path}  [{time.time()-t0:.0f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
