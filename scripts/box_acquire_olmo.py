#!/usr/bin/env python3
"""Phase 0 step 2 -- OLMo checkpoint acquisition, bf16 on download.

Downloads each stage at its PINNED revision sha, casts to bf16, writes a
canonical copy under $MODELS/<stage>, then purges the source from the HF
cache before moving to the next stage.

Why cast rather than keep what ships: SFT and DPO are distributed at fp32
(129 GB each), so a verbatim mirror is 386 GB against a 466 GB volume and
leaves no room for the Qwen bf16 g4 spike plus working space. Step 3 already
declares bf16 across all four checkpoints, so a bf16 copy IS the operative
precision -- this is the accepted decision applied at acquisition time, not
a deviation from it. Resident after the run: 4 x ~64 GB.

Purging as we go keeps peak disk at ~321 GB (the DPO stage), comfortably
inside the volume. Order is deliberate: the two fp32 giants are fetched
while little else is resident.

Every stage's sha, dtype, parameter count and on-disk size are written to a
manifest, which is the ledger-27 artifact for this step -- it travels back
to the repo, the box does not keep the only copy.
"""
from __future__ import annotations

import argparse, json, os, shutil, subprocess, sys, time
from pathlib import Path

import torch
from huggingface_hub import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Pinned revisions, verified 2026-08-18. Lineage is each card's declared
# base_model: Base -> SFT -> DPO -> Instruct, an unbroken chain.
CHECKPOINTS = [
    ("base",     "allenai/Olmo-3-1125-32B",           "c2b61dae89a1"),
    ("sft",      "allenai/Olmo-3.1-32B-Instruct-SFT", "152782ecc41a"),
    ("dpo",      "allenai/Olmo-3.1-32B-Instruct-DPO", "fc84a4f69991"),
    ("instruct", "allenai/Olmo-3.1-32B-Instruct",     "ac0587e4a774"),
]

MODELS = Path(os.environ.get("MODELS", "/workspace/models"))
CACHE = Path(os.environ.get("HF_HUB_CACHE", "/workspace/hf-cache/hub"))
MANIFEST = MODELS / "manifest.json"


def free_gb(p: Path) -> float:
    st = os.statvfs(p)
    return st.f_bavail * st.f_frsize / 1e9


def dir_gb(p: Path) -> float:
    """Real bytes on disk. Must NOT follow symlinks: the HF cache stores one
    blob under blobs/ and symlinks it from snapshots/, so a naive walk counts
    every shard twice and reports ~2x (this overstated the base purge as
    129 GB when 64 GB was freed)."""
    tot = 0
    for f in p.rglob("*"):
        st = f.lstat()
        if not f.is_symlink() and f.is_file():
            tot += st.st_size
    return tot / 1e9


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def purge_cache(repo: str) -> None:
    d = CACHE / ("models--" + repo.replace("/", "--"))
    if d.exists():
        gb = dir_gb(d)
        shutil.rmtree(d)
        log(f"    purged cache {d.name} ({gb:.0f} GB)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated stages")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    todo = [c for c in CHECKPOINTS
            if not args.only or c[0] in args.only.split(",")]
    MODELS.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}

    log(f"volume free: {free_gb(MODELS):.0f} GB | stages: {[c[0] for c in todo]}")
    if args.dry_run:
        for s, r, sha in todo:
            log(f"  would fetch {s:<9} {r} @ {sha}")
        return 0

    for stage, repo, sha in todo:
        dest = MODELS / stage
        if dest.exists() and (dest / "config.json").exists():
            log(f"{stage}: already present at {dest}, skipping")
            continue
        t0 = time.time()
        log(f"{stage}: downloading {repo} @ {sha}  (free {free_gb(MODELS):.0f} GB)")
        src = snapshot_download(repo, revision=sha,
                                allow_patterns=["*.safetensors", "*.json",
                                                "*.txt", "*.model"])
        log(f"    downloaded in {time.time()-t0:.0f}s; loading as bf16")

        model = AutoModelForCausalLM.from_pretrained(src, dtype=torch.bfloat16)
        n_params = sum(p.numel() for p in model.parameters())
        dtypes = {str(p.dtype) for p in model.parameters()}
        log(f"    params {n_params/1e9:.2f}B | dtypes {dtypes}")
        assert dtypes == {"torch.bfloat16"}, f"{stage}: not pure bf16: {dtypes}"

        tmp = MODELS / (stage + ".partial")
        if tmp.exists():
            shutil.rmtree(tmp)
        model.save_pretrained(tmp, safe_serialization=True)
        AutoTokenizer.from_pretrained(src).save_pretrained(tmp)
        del model
        tmp.rename(dest)                      # atomic: no half-written stage
        size = dir_gb(dest)
        log(f"    saved {dest} ({size:.0f} GB) in {time.time()-t0:.0f}s total")

        purge_cache(repo)
        manifest[stage] = {
            "repo": repo, "revision": sha, "dtype": "bfloat16",
            "n_params": n_params, "size_gb": round(size, 1),
            "path": str(dest),
            "acquired_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        MANIFEST.write_text(json.dumps(manifest, indent=1))
        log(f"    manifest updated | volume free {free_gb(MODELS):.0f} GB")

    log("ALL STAGES COMPLETE")
    for k, v in manifest.items():
        log(f"  {k:<9} {v['repo']:<36} {v['revision']} "
            f"{v['n_params']/1e9:.2f}B {v['size_gb']}GB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
