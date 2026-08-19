#!/usr/bin/env python3
"""Step 2, item 2 -- the one-time cast equality assert (SFT).

Requirement: assert that our bf16 cast equals what transformers' own
load-cast produces from the fp32 master. The comparison is over LOADED
TENSOR VALUES, not files: acquisition re-serialized every checkpoint, so
file hashes differ by construction and would fail for a reason that has
nothing to do with the cast.

Memory discipline: the two models are NEVER co-resident. Load one, walk its
state_dict in sorted key order, reduce each tensor to a SHA-256 over its
raw bytes (plus key/shape/dtype), free it entirely, then load the other.
Peak is one 64 GB model in host RAM, not two.

Outcomes are asymmetric by design:
  PASS -> the pattern is trusted, the fp32 temp is deleted, one checkpoint
          licenses the other three (whose own bf16 files are frozen by the
          per-file hashes from item 1).
  FAIL -> STOP. Touch nothing, delete nothing, escalate. A mismatch here
          means the weights we hold are not the weights we think we hold,
          which is an incident, not a debugging session.
"""
from __future__ import annotations
import argparse, gc, hashlib, json, os, shutil, sys, time

import torch
from huggingface_hub import snapshot_download
from transformers import AutoModelForCausalLM

REPO = "allenai/Olmo-3.1-32B-Instruct-SFT"
REVISION = "152782ecc41a"
CAST_DIR = "/workspace/models/sft"
TMP = "/workspace/_fp32_sft_tmp"
NEED_GB = 140


def free_gb(p: str) -> float:
    st = os.statvfs(p)
    return st.f_bavail * st.f_frsize / 1e9


def digest_state_dict(path: str, label: str) -> tuple[dict, str, int]:
    print(f"  [{label}] loading (dtype=bfloat16, CPU)…", flush=True)
    t0 = time.time()
    m = AutoModelForCausalLM.from_pretrained(path, dtype=torch.bfloat16)
    sd = m.state_dict()
    keys = sorted(sd)
    print(f"  [{label}] loaded {len(keys)} tensors in {time.time()-t0:.0f}s; "
          f"digesting", flush=True)
    per = {}
    agg = hashlib.sha256()
    n_el = 0
    for k in keys:
        t = sd[k]
        b = t.detach().contiguous().view(torch.uint8).numpy().tobytes()
        h = hashlib.sha256(b).hexdigest()
        meta = f"{k}|{tuple(t.shape)}|{t.dtype}|{len(b)}"
        per[k] = {"sha256": h, "shape": list(t.shape), "dtype": str(t.dtype),
                  "bytes": len(b)}
        agg.update((meta + "|" + h).encode())
        n_el += t.numel()
    del sd, m
    gc.collect()
    print(f"  [{label}] digested {len(per)} tensors, {n_el/1e9:.2f}B elements, "
          f"aggregate {agg.hexdigest()[:16]}…  [{time.time()-t0:.0f}s]", flush=True)
    return per, agg.hexdigest(), n_el


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep-tmp", action="store_true")
    args = ap.parse_args()

    print(f"free: {free_gb('/workspace'):.0f} GB (need >= {NEED_GB})", flush=True)
    if free_gb("/workspace") < NEED_GB:
        print("ABORT: insufficient free space")
        return 2

    print(f"\n=== re-pulling fp32 master {REPO} @ {REVISION} ===", flush=True)
    t0 = time.time()
    src = snapshot_download(REPO, revision=REVISION, local_dir=TMP,
                            allow_patterns=["*.safetensors", "*.json", "*.txt",
                                            "*.model", "*.jinja"])
    print(f"  downloaded in {time.time()-t0:.0f}s -> {src}", flush=True)

    print("\n=== digesting fp32 master under transformers' load-cast ===", flush=True)
    a_per, a_agg, a_n = digest_state_dict(src, "fp32->bf16")

    print("\n=== digesting our stored cast ===", flush=True)
    b_per, b_agg, b_n = digest_state_dict(CAST_DIR, "cast_dir")

    print("\n=== comparison ===", flush=True)
    ka, kb = set(a_per), set(b_per)
    key_match = ka == kb
    print(f"  key sets identical: {key_match} ({len(ka)} vs {len(kb)})")
    if not key_match:
        print(f"  only in fp32-load: {sorted(ka-kb)[:5]}")
        print(f"  only in cast_dir : {sorted(kb-ka)[:5]}")
    mismatches = [k for k in sorted(ka & kb) if a_per[k]["sha256"] != b_per[k]["sha256"]]
    agg_match = a_agg == b_agg
    print(f"  per-tensor mismatches: {len(mismatches)}")
    if mismatches:
        for k in mismatches[:10]:
            print(f"    {k}: {a_per[k]['sha256'][:16]}… vs {b_per[k]['sha256'][:16]}…")
    print(f"  aggregate digest: {a_agg[:24]}… vs {b_agg[:24]}…  match={agg_match}")

    ok = key_match and not mismatches and agg_match and a_n == b_n
    out = {"repo": REPO, "revision": REVISION, "cast_dir": CAST_DIR,
           "n_tensors": len(a_per), "n_elements": a_n,
           "aggregate_fp32_loadcast": a_agg, "aggregate_cast_dir": b_agg,
           "key_sets_identical": key_match,
           "n_per_tensor_mismatches": len(mismatches),
           "mismatched_keys": mismatches[:50], "PASS": ok}
    json.dump(out, open("/workspace/models/cast_equality_sft.json", "w"), indent=1)

    if ok:
        print("\nRESULT: PASS -- our stored bf16 cast is tensor-for-tensor "
              "identical to transformers' own load-cast of the fp32 master.")
        if not args.keep_tmp:
            shutil.rmtree(TMP, ignore_errors=True)
            print(f"  deleted {TMP}; free now {free_gb('/workspace'):.0f} GB")
        return 0
    print("\nRESULT: FAIL -- STOPPING. fp32 temp left in place, nothing "
          "deleted, nothing modified. This is an incident: escalate.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
