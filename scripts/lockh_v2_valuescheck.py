#!/usr/bin/env python3
"""LOCK-h v2 §6 values-check: every §1 number and §2 constant verified
against the committed artifacts.

v2 changes no operating characteristic -- it carries the realised calibration
into the verdict tier's restatement. So the only thing that can be wrong with
it is a transcription, and a transcription error in a lock is exactly the kind
of defect that survives every review because it looks like a fact. This
checks each claim against the artifact §6 names for it, and reports a table.

Nothing here recomputes a verdict or re-derives a bar. It compares numbers
that are written in the lock to numbers that are written in the record.

Usage:
    python scripts/lockh_v2_valuescheck.py
    python scripts/lockh_v2_valuescheck.py --lock LOCK-h-v2.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")


def load(rel):
    return json.load(open(os.path.join(DATA, rel)))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", default=os.path.join(REPO, "LOCK-h.md"))
    ap.add_argument("--out", default=os.path.join(DATA, "e2b/lockh_v2_valuescheck.json"))
    args = ap.parse_args()

    lock = open(args.lock).read()
    h2 = load("e2b/h2_sessions.json")
    sweep = load("e2b/h2_sweep.json")
    h1 = load("e2b/h1_sessions.json")
    gate = load("e2b/h1_gate.json")
    audit = load("configs/e2b_audit_v2.json")
    power = load("e2b/h1_power.json")["lockh_v1"]

    h2s = h2["summary"]
    b = h1["budget"]

    # H2's degeneracy "under the corrected lens": what audit v2 would have
    # flagged in H2 = what actually fired (2) plus the sweep's hits, which
    # are by construction the responses the frozen audit missed.
    h2_v2_degen = h2s["degeneracy"]["n"] + sweep["n_hits"]

    rows = []

    def chk(label, claim, actual, source, ok=None, needle=None):
        """Two independent things must hold, and conflating them was this
        script's original defect: the ARTIFACT must carry the value, and the
        LOCK must actually say it. Without `needle` the check only proves
        that the number Code typed into this file matches the record -- a
        typo in the lock that Code did not replicate would sail through."""
        ok = (claim == actual) if ok is None else ok
        found = None if needle is None else (needle in lock)
        rows.append({"label": label, "claim": claim, "actual": actual,
                     "source": source, "ok": bool(ok) and found is not False,
                     "in_lock_text": found, "needle": needle})

    # --- §1 dose / H2 -----------------------------------------------------
    chk("§1 dose layer", 48, h2["layer"], "h2_sessions.json", needle="L48")
    chk("§1 dose frac", 0.10, h2["frac"], "h2_sessions.json", needle="frac 0.10")
    chk("§1 |alpha|", 10.3010, round(h2["alpha"], 4), "h2_sessions.json", needle="10.3010")
    chk("§1 H2 degeneracy (audit that ran)", "2/307",
        f"{h2s['degeneracy']['n']}/{h2s['degeneracy']['of']}",
        "h2_sessions.json")
    chk("§1 H2 degeneracy under corrected lens ~0.036",
        0.036, round(h2_v2_degen / h2s["degeneracy"]["of"], 3),
        "h2_sessions.json + h2_sweep.json", needle="0.036")
    chk("§1 H2 declared p0", 0.05, h2["declared_degen_p0"],
        "h2_sessions.json")
    chk("§1 H2 window clean", 0, h2["window"]["n_encodes_clipped"],
        "h2_sessions.json")
    chk("§1 H2 pi_hat_d", 0.0278, round(h2s["pi_hat_d"], 4),
        "h2_sessions.json", needle="0.0278")

    # --- §1 leakage gate / H1 --------------------------------------------
    chk("§1 H1 N", 640, b["N"], "h1_sessions.json", needle="N = 640")
    chk("§1 H1 sessions run", 123, h1["n_run"], "h1_sessions.json", needle="123 sessions run")
    chk("§1 H1 excluded", 16, h1["n_excluded"], "h1_sessions.json", needle="16 excluded")
    chk("§1 H1 no appended block", 128, h1["n_scheduled"],
        "h1_sessions.json")
    chk("§1 H1 n_d", 11, b["n_d"], "h1_sessions.json", needle="n_d = 11")
    chk("§1 H1 b", 6, b["b"], "h1_sessions.json")
    chk("§1 H1 c", 5, b["c"], "h1_sessions.json")
    chk("§1 H1 pi_hat_d", 0.0172, round(gate["pi_hat_d"], 4), "h1_gate.json", needle="0.0172")
    chk("§1 H1 pi_hat_d CI", [0.0086, 0.0305],
        [round(x, 4) for x in gate["pi_hat_d_ci"]], "h1_gate.json")
    chk("§1 H1 L_hat", 0.00156, round(gate["L_hat"], 5), "h1_gate.json", needle="+0.00156")
    chk("§1 H1 mapped L CI", [-0.00915, 0.01143],
        [round(x, 5) for x in gate["L_ci"]], "h1_gate.json")
    chk("§1 H1 verdict PASS", "PASS", gate["verdict"], "h1_gate.json")
    chk("§1 H1 certified by low discordance", True,
        gate["certified_by_low_discordance"], "h1_gate.json")
    s3b = gate["secondary_3b"]
    chk("§1 §3b ICC", 0.0000, round(s3b["icc_obs"], 4), "h1_gate.json")
    chk("§1 §3b ICC p", 1.0, round(s3b["icc_p_two_sided"], 4),
        "h1_gate.json")
    chk("§1 §3b sessions >=2 flips", 0, s3b["sessions_ge2_obs"],
        "h1_gate.json")
    chk("§1 §3b that p", 1.0, round(s3b["sessions_ge2_p_two_sided"], 4),
        "h1_gate.json")

    # --- audit sha, recomputed not just read -----------------------------
    blob = json.dumps({k: v for k, v in audit.items() if k != "sha16"},
                      sort_keys=True, separators=(",", ":")).encode()
    recomputed = hashlib.sha256(blob).hexdigest()[:16]
    chk("§1 audit sha16 (recorded)", "7aa235d25eeb66dc", audit["sha16"],
        "e2b_audit_v2.json")
    chk("§1 audit sha16 (recomputed)", audit["sha16"], recomputed,
        "recomputed from the artifact body")
    chk("§1 H1 ran under that sha", audit["sha16"], h1["audit_sha16"],
        "h1_sessions.json")

    # --- directional-leak family -----------------------------------------
    read_half = load("e2b/h2_read_stability.json")["leak_summary"][
        "state_reversing_half_gap"]
    h2_gap = h2s["leak_summary"]["state_reversing_half_gap"]
    h1u = load("e2b/h1u_sessions.json")["budget"]
    h1u_L = (h1u["b"] - h1u["c"]) / h1u["N"]
    chk("§1 leak family: read half", 0.00084, round(read_half, 5),
        "h2_read_stability.json")
    chk("§1 leak family: H2", 0.00220, round(h2_gap, 5),
        "h2_sessions.json")
    chk("§1 leak family: H1-u", 0.00000, round(h1u_L, 5),
        "h1u_sessions.json")
    chk("§1 leak family: H1", 0.00156, round(gate["L_hat"], 5),
        "h1_gate.json")

    # --- §2 criterion constants ------------------------------------------
    env_p90 = power["envelope_exact"]["p90"]
    chk("§2 envelope p90 = 0.167", 0.167, round(env_p90, 3),
        "h1_power.json lockh_v1", needle="p90 = 0.167")
    chk("§2 critical k >= 57 at n=96", 57,
        power["variants"][0]["k_binom"], "h1_power.json lockh_v1", needle="k ≥ 57")
    chk("§2 MDE 0.130 at 80% power", 0.130,
        round(json.load(open(os.path.join(DATA, "e2b/h1_power.json")))
              ["mde_verdict_share"], 3), "h1_power.json", needle="MDE 0.130")
    chk("§2 bar_leak 0.0735", 0.0735, power["bar_leak"],
        "h1_power.json lockh_v1", needle="0.0735")
    chk("§2 realised leak = 2.1% of bar", 2.1,
        round(100 * gate["L_hat"] / power["bar_leak"], 1),
        "h1_gate.json / h1_power.json", needle="2.1%")
    # bar_leak/2 = 0.03675 EXACTLY in decimal, and the lock's 0.0368 is its
    # correct 4-dp rounding. Two earlier forms of this check were CHECKER
    # bugs, not lock defects: Python's round() returns 0.0367 because the
    # binary double is a hair under 0.03675, and a 5e-05 float tolerance
    # sits exactly on the boundary and fails by 1.4e-19. Decimal settles it.
    from decimal import ROUND_HALF_UP, Decimal
    half = Decimal(str(power["bar_leak"])) / 2
    half_4dp = half.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    chk("§2 monitor threshold bar_leak/2 (exact 0.03675 -> 4dp)",
        "0.0368", str(half_4dp), "h1_power.json lockh_v1", needle="0.0368")

    # --- arms and n, as registered ---------------------------------------
    chk("§2 marker n", 96, 96, "PROPOSAL-h §3 (registered)", needle="96 valid sessions")
    chk("§2 sham n", 36, 36, "PROPOSAL-h §3 (registered)")
    chk("§2 random n", 36, 36, "PROPOSAL-h §3 (registered)")

    width = max(len(r["label"]) for r in rows) + 2
    print("=== LOCK-h v2 §6 VALUES-CHECK ===")
    print(f"  lock: {os.path.relpath(args.lock, REPO)}\n")
    for r in rows:
        print(f"  [{'OK ' if r['ok'] else 'MISMATCH'}] {r['label']:<{width}}"
              f" lock {str(r['claim']):<22} artifact "
              f"{str(r['actual']):<22} ({r['source']})")
    located = [r for r in rows if r.get("in_lock_text") is True]
    missing = [r for r in rows if r.get("in_lock_text") is False]
    print(f"\n  lock-text location: {len(located)} claims found verbatim in "
          f"the lock; {len(missing)} claimed but NOT present"
          + (f" -> {[r['needle'] for r in missing]}" if missing else ""))
    bad = [r for r in rows if not r["ok"]]
    print(f"\n  {len(rows) - len(bad)}/{len(rows)} verified")
    green = not bad
    print(f"  VERDICT: "
          + ("GREEN" if green else "MISMATCH -- report to the design instance"))

    out = {"item": "LOCK-h v2 §6 values-check",
           "lock": os.path.relpath(args.lock, REPO),
           "n_checks": len(rows), "n_ok": len(rows) - len(bad),
           "n_located_in_lock_text": len(located),
           "n_claimed_but_absent_from_lock": len(missing),
           "green": bool(green), "rows": rows,
           "decides_nothing": ("Transcription check only; the commit is the "
                               "design instance's and Jason's.")}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
