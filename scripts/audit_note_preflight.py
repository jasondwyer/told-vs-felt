#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- preflight: referent inventory.

Read-only. Resolves every referent the audit block names, item by item,
against the working tree and the index at HEAD, and prints what exists, what
is tracked, its sha256, and what is missing. Writes nothing but its own stdout
(the caller tees it to results/raw/). Stdlib only.

    python scripts/audit_note_preflight.py > results/raw/<stamp>_note-preflight.md
"""
import glob
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA_ROUTED = "8cd8a9ac", "3841"   # the PI's routing: sha256 8cd8a9ac...3841
PREPRINT_SHA_NAMED = "d6431e97", "222b8"  # block N1: post-patch-v4 copy

# Referents as the block names them, per item (block line numbers in comments).
REFERENTS = {
    "N1 (block :21)": [
        "RESEARCH-NOTE-v0_2-draft.md", "FIGURE-REVIEW-2026-10-06.md",
        "*F1*.svg", "*F2*.svg", "figures/*.svg", "PREPRINT-v1_1-draft.md",
        "PREPRINT-v1_0-draft.md", "RESULTS.md", "archive/RESULTS-cycle1-2.md",
        "archive/RESULTS-cycles3-4.md", "FINDINGS*.md", "scripts/paper_data.py",
        "NOTE-HEAT-PLAN*",
    ],
    "N2 (block :28)": [
        "scripts/b2_analyze.py", "scripts/b2r_analyze.py",
        "scripts/box_b2_detection.py", "scripts/box_b2r_campaign.py",
        "valence_core/detection.py", "valence_core/detection_v2.py",
        "data/configs/b2_concepts.json", "data/configs/b2_framing.json",
        "data/configs/scorer_v3_spec.json", "data/olmo/*.json",
        "data/olmo/b2r_analysis.json", "data/olmo/b2r_explore_sft.json",
        "data/olmo/b2r_explore_dpo.json", "data/olmo/b2r_explore_instruct.json",
        "ADDENDUM-g3-b2r-v1.2.md",
    ],
    "N3 (block :41)": [
        "scripts/recon_echo.py", "valence_core/echo/probe.py",
        "valence_core/echo/spans.py", "valence_core/echo/maskedprefix.py",
        "valence_core/echo/k1.py", "data/echo/*.json", "data/echo/*.npz",
        "results/raw/2026-09-06_recon_echo_stageC_analysis.txt",
        "PROPOSAL-k-echo-channel.md", "data/k/*.json", "scripts/k1_analyze.py",
    ],
    "N4 (block :55)": [
        "scripts/e2a_recount.py", "valence_core/session_e2a.py",
        "data/e2a/*.json", "data/e2a/*.jsonl", "data/e2a/analysis.json",
        "data/configs/e2a_ban_list.json", "archive/RESULTS-cycles3-4.md",
        "scripts/box_cached_gen_smoke.py",
    ],
    "N11 (block :67)": [
        "README.md", "valence_core/regression/analysis.py", ".gitattributes",
        ".gitignore",
    ],
    "N12 (block :75)": [
        "CLAUDE.md", ".git/config", "scripts/box_*.py", "scripts/run_*.sh",
        "results/raw/*", "HANDOFF-*.md", ".gitignore",
        "data/configs/b2_concepts.json", "data/configs/b2_framing.json",
        "jlens-qwen36",
    ],
    "N13 (block :90)": [
        "PROPOSAL-d*.md", "PROPOSAL-e*.md", "PROPOSAL-f*.md", "PROPOSAL-g*.md",
        "PROPOSAL-h*.md", "PROPOSAL-j*.md", "PROPOSAL-k*.md", "LOCK-g.md",
        "LOCK-h.md", "ADDENDUM-*.md",
    ],
    "N5 (block :98)": [
        "data/f/*.json", "data/f/*.jsonl",
        "PROPOSAL-f-natural-reinforcer-screen.md",
        "data/configs/f_termination_patterns.json",
    ],
    "N6 (block :101)": [
        "data/e2b/*.json", "scripts/e2b_verdict_analyze.py",
        "scripts/e2b_h1_gate.py", "scripts/h1_power.py",
        "valence_core/e2b/statepresent.py", "valence_core/e2b/records.py",
        "PROPOSAL-h-state-present-choice.md", "LOCK-h.md",
    ],
    "N7 (block :104)": [
        "scripts/b1_verdict.py", "scripts/b3_analyze.py",
        "scripts/box_a4_hijack.py", "scripts/box_b3_sessions.py",
        "data/olmo/*.json", "PROPOSAL-g-ontogeny-of-evaluation.md", "LOCK-g.md",
    ],
    "N8 (block :107)": [
        "valence_core/regression/analysis.py", "valence_core/regression/oracle.py",
        "data/configs/c1r3_gate_repA.json", "data/configs/c1r3_gate_repB.json",
        "data/e0/*", "data/e2d/*.json", "scripts/e2d_closure_verify3.py",
    ],
    "N9 (block :110)": ["data/d/*.json", "PROPOSAL-d-distilled-trace.md"],
    "N10 (block :113)": ["ADDENDUM-g1*.md", "PROPOSAL-h-state-present-choice.md"],
}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True).stdout


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    tracked = set(git("ls-files").splitlines())
    head = git("rev-parse", "HEAD").strip()
    stamp = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%S UTC"],
                           capture_output=True, text=True).stdout.strip()
    bsha = sha256(os.path.join(ROOT, BLOCK))
    with open(os.path.join(ROOT, BLOCK), encoding="utf-8") as f:
        blines = sum(1 for _ in f)

    print("# AUDIT-note-release v1.2 -- preflight (referent inventory)")
    print()
    print(f"- Code stamp: {stamp} (date -u)")
    print(f"- HEAD: {head}")
    print(f"- Block: `{BLOCK}`, sha256 `{bsha}`, {blines} lines "
          f"(routed as 8cd8a9ac...3841, 141 lines: "
          f"{'MATCH' if bsha.startswith(BLOCK_SHA_ROUTED[0]) and bsha.endswith(BLOCK_SHA_ROUTED[1]) and blines == 141 else 'MISMATCH'})")
    print(f"- Script: `scripts/audit_note_preflight.py` (read-only; stdlib)")
    print(f"- Interpreter: {sys.executable} (Python {sys.version.split()[0]})")
    print()
    print("Status codes: T = tracked at HEAD; U = present, untracked "
          "(not in a clone); L = present, gitignored/local only; "
          "MISSING = no match on this machine.")
    for item, refs in REFERENTS.items():
        print()
        print(f"## {item}")
        print()
        print("| referent | status | matches | sha256 (working tree, first) |")
        print("|---|---|---|---|")
        for ref in refs:
            full = os.path.join(ROOT, ref)
            hits = sorted(glob.glob(full))
            if not hits:
                print(f"| `{ref}` | MISSING | 0 | |")
                continue
            rels = [os.path.relpath(h, ROOT) for h in hits]
            if len(rels) == 1 and os.path.isdir(hits[0]):
                n_tr = sum(1 for t in tracked if t.startswith(rels[0] + "/"))
                print(f"| `{ref}` | dir; {n_tr} tracked files under it | 1 | |")
                continue
            st = []
            for r in rels:
                if r in tracked:
                    st.append("T")
                else:
                    ign = subprocess.run(["git", "check-ignore", "-q", r],
                                         cwd=ROOT).returncode == 0
                    st.append("L" if ign else "U")
            counts = {k: st.count(k) for k in ("T", "U", "L") if st.count(k)}
            status = ", ".join(f"{k}={v}" for k, v in counts.items())
            first = hits[0]
            sh = sha256(first) if os.path.isfile(first) else ""
            label = f"`{rels[0]}` {sh[:16]}" if len(rels) > 1 else sh
            print(f"| `{ref}` | {status} | {len(rels)} | {label} |")

    pp = os.path.join(ROOT, "PREPRINT-v1_0-draft.md")
    if os.path.isfile(pp):
        s = sha256(pp)
        ok = s.startswith(PREPRINT_SHA_NAMED[0]) and s.endswith(PREPRINT_SHA_NAMED[1])
        print()
        print(f"PREPRINT-v1_0-draft.md sha256 {s} vs block's d6431e97...222b8: "
              f"{'MATCH' if ok else 'MISMATCH'}; tracked: "
              f"{'yes' if 'PREPRINT-v1_0-draft.md' in tracked else 'NO (untracked: absent from any clone)'}")


if __name__ == "__main__":
    main()
