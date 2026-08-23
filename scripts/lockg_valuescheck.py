#!/usr/bin/env python3
"""LOCK-g §7 values-check: every §1 number and every instantiated constant
verified against the committed artifacts, and against the lock's own text.

LOCK-g changes no registered criterion -- it carries A-phase's realised
values into the Phase-B instantiation. So the only thing that can be wrong
with it is a transcription, and a transcription error in a lock is exactly
the defect that survives every review because it looks like a fact.

TWO FAILURE MODES, BOTH CHECKED. A checker that only compares its own
transcription against the artifacts proves that Code can copy, not that the
LOCK says what Code thinks it says (HANDOFF-2026-08-22 trap 7 -- the defect
`lockh_v2_valuescheck.py` shipped with on its first use). So every claim
carries a `needle`: a literal that must be LOCATED in the lock text. Claims
whose value is derived or structural, with no single literal form in the
document, are marked as such rather than silently counted as located.

Needles are matched against the lock with whitespace collapsed, so a needle
may be written naturally even where the document wraps it across lines.

Float comparisons that the lock states as rounded decimals use `Decimal`
(trap 6: `round()` on a float fails a 5e-05 tolerance by 1.4e-19).

Nothing here recomputes a verdict or re-derives a bar. It compares numbers
written in the lock to numbers written in the record, and computes the two
arithmetic quantities §7 asks for directly.

Usage:
    jlens-qwen36/.venv/bin/python scripts/lockg_valuescheck.py
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from decimal import Decimal

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
DATA = os.path.join(REPO, "data")
STAGES = ("base", "sft", "dpo", "instruct")

from valence_core.stats import binom_sf_inclusive                 # noqa: E402

ROWS: list[dict] = []
_LOCK_FLAT = ""


def chk(section, label, claim, actual, source, ok=None, needle=None):
    """One claim. `needle` is what the LOCK must literally say."""
    if ok is None:
        ok = (str(claim) == str(actual))
    found = None if needle is None else (needle in _LOCK_FLAT)
    ROWS.append({"section": section, "label": label, "claim": str(claim),
                 "actual": str(actual), "source": source, "ok": bool(ok),
                 "needle": needle, "needle_located": found})


def d4(x) -> Decimal:
    return Decimal(str(x)).quantize(Decimal("0.0001"))


def d3(x) -> Decimal:
    return Decimal(str(x)).quantize(Decimal("0.001"))


# --- the two arithmetic quantities §7 asks Code to compute ----------------
def binomial_arithmetic(n=96, alpha=0.05, power=0.80) -> dict:
    """Critical k and the binomial MDE, by direct computation.

    critical k = smallest k with P(X >= k | n, p=0.5) <= alpha.
    MDE        = smallest Delta whose power at that k reaches `power`,
                 with Delta = p - 0.5.

    THE CONVENTION IS NOT FREE TO CHOOSE and this checker got it wrong on
    its first run, reporting 0.260 against the lock's 0.130. Delta in this
    program is a share MINUS CHANCE, not a doubled share: e2b's 47/96 is
    recorded as Delta_first = -0.0104, and 47/96 - 0.5 = -0.010417 while
    2*(47/96) - 1 = -0.020833. The record settles it.

    Pure python exact binomial; no scipy on this laptop (trap 1).
    """
    k_crit = next(k for k in range(n + 1)
                  if binom_sf_inclusive(k, n, 0.5) <= alpha)
    p = 0.5
    while p <= 1.0:
        if binom_sf_inclusive(k_crit, n, p) >= power:
            break
        p += 0.0001
    return {"n": n, "alpha": alpha, "power": power, "critical_k": k_crit,
            "p_at_power": round(p, 4), "mde_delta": round(p - 0.5, 4),
            "delta_convention": "Delta = p - 0.5 (share minus chance), as in "
                                "e2b's 47/96 -> -0.0104",
            "p_value_at_critical_k": binom_sf_inclusive(k_crit, n, 0.5),
            "method": "exact binomial, pure python (valence_core.stats)"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", default=os.path.join(REPO, "LOCK-g.md"))
    ap.add_argument("--out", default=os.path.join(DATA, "olmo/lockg_valuescheck.json"))
    ap.add_argument("--arith-out", default=os.path.join(DATA, "olmo/lockg_arith.json"))
    ap.add_argument("--skip-rebuild", action="store_true",
                    help="skip the marker-store instrument rebuild (slow)")
    args = ap.parse_args()

    global _LOCK_FLAT
    lock = open(args.lock).read()
    _LOCK_FLAT = re.sub(r"\s+", " ", lock)

    hij = {s: json.load(open(os.path.join(DATA, f"olmo/a4_hijack_{s}.json")))
           for s in STAGES}
    ins = {s: json.load(open(os.path.join(DATA, f"olmo/a4_instrument_{s}.json")))
           for s in STAGES}
    a2 = {s: json.load(open(os.path.join(DATA, f"olmo/a2_baserates_{s}.json")))
          for s in STAGES}
    rost = json.load(open(os.path.join(DATA, "olmo/a1_repair_roster.json")))
    budget = json.load(open(os.path.join(DATA, "olmo/a5_budget.json")))
    det = json.load(open(os.path.join(DATA, "olmo/determinism_base.json")))
    integ = open(os.path.join(REPO, "results/raw/2026-08-23_respawn_integrity.txt")).read()

    # --- §1 backend ------------------------------------------------------
    chk("§1", "integrity 29 files", True,
        "INTEGRITY PASS — 29 files" in integ, "respawn_integrity raw",
        ok="INTEGRITY PASS — 29 files" in integ, needle="29/29 files")
    chk("§1", "determinism A repeat-exact", True,
        det["A_repeat_deterministic"]["all_exact"], "determinism_base.json",
        ok=det["A_repeat_deterministic"]["all_exact"] is True,
        needle="determinism exactly 0.0 on all three")
    chk("§1", "determinism B det-off exact", True,
        det["B_deterministic_off"]["repeat_all_exact"], "determinism_base.json",
        ok=det["B_deterministic_off"]["repeat_all_exact"] is True, needle=None)
    chk("§1", "kernel gate max_kl", 0.0, det["C_kernel_path"]["max_kl"],
        "determinism_base.json", ok=det["C_kernel_path"]["max_kl"] == 0.0,
        needle="symKL 0.000e+00")
    chk("§1", "gpu", "NVIDIA A100-SXM4-80GB", det["provenance"]["gpu"],
        "determinism_base.json", needle="A100-SXM4-80GB")

    # --- §1 roster -------------------------------------------------------
    sel_names = rost["selected"]
    by_name = {r["name"]: r for r in rost["ranked"]}
    got_tags = ["/".join(by_name[n]["tags"]) for n in sel_names]
    for want in ("quartz/velvet", "copper/walnut", "maple/saddle",
                 "amber/granite"):
        chk("§1", f"roster {want}", True, want in got_tags,
            "a1_repair_roster.json", ok=want in got_tags, needle=want)
    imb = sorted(d3(by_name[n]["worst_stage_imbalance"]) for n in sel_names)
    chk("§1", "roster imbalances", "0.026/0.040/0.077/0.082",
        "/".join(str(x) for x in imb), "a1_repair_roster.json",
        ok=[str(x) for x in imb] == ["0.026", "0.040", "0.077", "0.082"],
        needle="0.026 / 0.040 / 0.077 / 0.082")
    inband = all(abs(v - 0.5) <= 0.10
                 for n in sel_names
                 for v in by_name[n]["per_stage_identity"].values())
    chk("§1", "all four stages inside 0.50 ± 0.10", True, inband,
        "a1_repair_roster.json", ok=inband,
        needle="all inside 0.50 ± 0.10 on all four")
    # the amendment's stated cost
    clearing = [r for r in rost["ranked"] if r["clears_band"]]
    greedy = sum(r["worst_stage_imbalance"] for r in clearing[:4])
    chosen = sum(by_name[n]["worst_stage_imbalance"] for n in sel_names)
    chk("§1", "disjointness cost", "0.017", str(d3(chosen - greedy)),
        "a1_repair_roster.json (matching total - greedy top-4 total)",
        ok=str(d3(chosen - greedy)) == "0.017",
        needle="Cost of exactness: 0.017 total worst-stage imbalance")
    chk("§1", "greedy total", "0.2074", f"{greedy:.4f}",
        "a1_repair_roster.json", ok=round(greedy, 4) == 0.2074,
        needle="greedy 0.2074")
    chk("§1", "exact-matching total", "0.2241", f"{chosen:.4f}",
        "a1_repair_roster.json", ok=round(chosen, 4) == 0.2241,
        needle="exact 0.2241")
    gt = [t for r in clearing[:4] for t in r["tags"]]
    chk("§1", "greedy top-4 really is non-disjoint", True,
        len(set(gt)) != len(gt), "a1_repair_roster.json",
        ok=len(set(gt)) != len(gt),
        needle="do not use eight distinct tags")
    # the lock now names the colliding pair; check that claim too
    r092 = next((r for r in clearing[:4]
                 if sorted(r["tags"]) == ["maple", "walnut"]), None)
    chk("§1", "R092 maple/walnut is in the greedy four", True, r092 is not None,
        "a1_repair_roster.json", ok=r092 is not None,
        needle="R092 maple/walnut collides")

    # --- §1 MED / layer table --------------------------------------------
    want_med = {"base": (60, 0.05), "sft": (44, 0.40),
                "dpo": (44, 0.05), "instruct": (44, 0.05)}
    for s, (L, med) in want_med.items():
        chk("§1", f"{s} selected layer", L, hij[s]["selected_layer"],
            f"a4_hijack_{s}.json", needle=f"| {s} | L{L} |")
        chk("§1", f"{s} MED", med, hij[s]["minimum_effective_dose"],
            f"a4_hijack_{s}.json",
            ok=Decimal(str(med)) == Decimal(str(hij[s]["minimum_effective_dose"])),
            needle=None)
    sham0 = all(v["controls"]["sham"]["delta"] == 0.0
                for s in STAGES for v in hij[s]["ladder"].values())
    chk("§1", "sham 0.0 bit-for-bit everywhere", True, sham0,
        "a4_hijack_*.json", ok=sham0,
        needle="sham realised 0.0 bit-for-bit everywhere")

    # --- §1 currency ------------------------------------------------------
    want_g = {"base": "0.7824", "sft": "1.0279",
              "dpo": "1.5325", "instruct": "1.5612"}
    for s, g in want_g.items():
        chk("§1", f"G_c {s}", g, str(d4(ins[s]["G_c"])),
            f"a4_instrument_{s}.json", ok=str(d4(ins[s]["G_c"])) == g,
            needle=f"+{g}")
        chk("§1", f"{s} floors met", True,
            ins[s]["declared_floors"]["all_floors_met"],
            f"a4_instrument_{s}.json",
            ok=ins[s]["declared_floors"]["all_floors_met"] is True, needle=None)
        chk("§1", f"{s} decidable probes", 12,
            ins[s]["declared_floors"]["n_decidable_probes"],
            f"a4_instrument_{s}.json", needle="12/12 decidable probes")

    # --- §1 A2 base rates -------------------------------------------------
    for s in STAGES:
        d = a2[s]["detection"]["summary"]
        chk("§1", f"{s} usable rate", "1.000", str(d3(d["usable_rate"])),
            f"a2_baserates_{s}.json", ok=str(d3(d["usable_rate"])) == "1.000",
            needle="1.000 at every stage")
    fa = sum(a2[s]["detection"]["summary"]["affirm"] for s in STAGES)
    nt = sum(a2[s]["detection"]["summary"]["n_trials"] for s in STAGES)
    chk("§1", "false alarms across all control trials", "0/96",
        f"{fa}/{nt}", "a2_baserates_*.json", ok=(fa == 0 and nt == 96),
        needle="zero false alarms in 96")
    und = "/".join(f"{a2[s]['detection']['summary']['undecidable']}/24"
                   for s in STAGES)
    chk("§1", "undecidable rates", "1/24, 1/24, 0/24, 12/24",
        und.replace("/24/", "/24, "), "a2_baserates_*.json",
        ok=[a2[s]["detection"]["summary"]["undecidable"] for s in STAGES]
           == [1, 1, 0, 12], needle="1/24, 1/24, 0/24, 12/24")
    degen = all(a2[s]["sessions"]["summary"]["n_degenerate"] == 0
                and a2[s]["sessions"]["summary"]["n_rounds"] == 80
                for s in STAGES)
    chk("§1", "operant degeneracy 0/80 every stage", True, degen,
        "a2_baserates_*.json", ok=degen, needle="0/80 at every stage")
    nobar = all(not a2[s]["bars"]["fired"] for s in STAGES)
    chk("§1", "no bar fired", True, nobar, "a2_baserates_*.json",
        ok=nobar, needle="no bar fired")

    # --- §1 budget --------------------------------------------------------
    r = budget["rates"]
    chk("§1", "worst s/forward", "0.0871", str(d4(r["s_per_forward_max"])),
        "a5_budget.json", ok=str(d4(r["s_per_forward_max"])) == "0.0871",
        needle="0.0871 s/forward, 181 s load")
    chk("§1", "worst load s", 181, int(r["cold_load_max_s"]),
        "a5_budget.json", needle=None)
    chk("§1", "model validation error", True,
        budget["model_validation"]["worst_rel_error"] <= 0.049,
        "a5_budget.json",
        ok=budget["model_validation"]["worst_rel_error"] <= 0.049,
        needle="≤4.9% error")
    b = budget["budgets_at_default_session_tokens"]
    chk("§1", "B2 hours", "0.76", str(Decimal(str(round(b["B2"]["hours"], 2)))),
        "a5_budget.json", ok=round(b["B2"]["hours"], 2) == 0.76,
        needle="B2 0.76 h")
    sens = budget["sensitivity_by_session_tokens"]
    worst_screen = max(v["screen_h"] for v in sens.values())
    worst_tot = max(v["screen_plus_one_confirm_h"] for v in sens.values())
    chk("§1", "B3 screen worst", "≤5.87", f"{worst_screen:.2f}",
        "a5_budget.json", ok=round(worst_screen, 2) <= 5.87,
        needle="B3 screen ≤5.87 h")
    chk("§1", "screen + one confirm worst", "≤7.53", f"{worst_tot:.2f}",
        "a5_budget.json", ok=round(worst_tot, 2) <= 7.53,
        needle="screen + one confirm ≤7.53 h")

    # --- §4 B3 arithmetic --------------------------------------------------
    m, sh, rd = 96, 36, 36
    chk("§4", "96:36:36 scaled to marker 48", "18/18",
        f"{round(48*sh/m)}/{round(48*rd/m)}", "direct arithmetic",
        ok=(round(48*sh/m), round(48*rd/m)) == (18, 18),
        needle="marker 48, sham 18, random 18")
    chk("§4", "strata 4 pairs x 2 maps", 8, 4*2, "direct arithmetic",
        needle="4 pairs × 2 maps = 8")
    chk("§4", "marker per stratum", 6, 48//8, "direct arithmetic",
        needle="marker 6/stratum")
    chk("§4", "sham/random per stratum", 3, 24//8, "direct arithmetic",
        needle="scheduled 24 each")
    chk("§4", "24 scheduled tolerates 25% exclusion to 18 valid", 18,
        int(24*0.75), "direct arithmetic", needle="tolerating 25% exclusion")
    chk("§4", "hard cap", 144, 144, "declared", needle="hard cap 144 run sessions")

    arith = binomial_arithmetic()
    chk("§4", "critical k at n=96", 57, arith["critical_k"],
        "lockg_arith.json (exact binomial)", needle="critical k ≥ 57")
    chk("§4", "binomial MDE at 80% power", "0.130",
        str(d3(arith["mde_delta"])), "lockg_arith.json (exact binomial)",
        ok=str(d3(arith["mde_delta"])) == "0.130",
        needle="binomial MDE 0.130 at 80%")

    from valence_core.adapters import olmo_hf as _o
    chk("§4", "declared choice window", 8192, _o.DEFAULT_CHOICE_WINDOW,
        "valence_core/adapters/olmo_hf.py", needle="declared window 8192")

    # --- §7 rebuild path ---------------------------------------------------
    if not args.skip_rebuild:
        import numpy as np
        sys.path.insert(0, os.path.join(REPO, "scripts"))
        from box_a4_instrument import build_instruments
        from box_e0_corpus import FIT_IDS
        worst_sel, worst_g = 0, 0.0
        for s in STAGES:
            z = np.load(os.path.join(DATA, f"olmo/a4_instrument_{s}.npz"))
            store = {k: z[k] for k in ("top_ids", "top_vals", "task_id",
                                       "cond", "probe")}
            iv, pp = build_instruments(store, list(FIT_IDS),
                                       ins[s]["sel_per_probe"])
            bad = sum(0 if np.array_equal(z[f"sel_{i}"], iv[i]["sel_ids"])
                      else 1 for i in range(len(iv)))
            worst_sel = max(worst_sel, bad)
            worst_g = max(worst_g, abs(float(np.mean(
                [v["g_q"] for v in pp.values()])) - ins[s]["G_c"]))
        chk("§7", "marker stores rebuild the instruments", "0 probes differ",
            f"{worst_sel} probes differ", "a4_instrument_*.npz",
            ok=worst_sel == 0, needle="rebuild path vs marker stores")
        chk("§7", "G_c reproduces from stores", "< 1e-12",
            f"{worst_g:.2e}", "a4_instrument_*.npz", ok=worst_g < 1e-12,
            needle=None)

    # --- report ------------------------------------------------------------
    with open(args.arith_out, "w") as fh:
        json.dump(arith, fh, indent=1)
    n_fail = sum(1 for r in ROWS if not r["ok"])
    located = sum(1 for r in ROWS if r["needle_located"] is True)
    absent = [r for r in ROWS if r["needle_located"] is False]
    derived = sum(1 for r in ROWS if r["needle"] is None)

    print("=" * 78)
    print("LOCK-g §7 VALUES-CHECK")
    print("=" * 78)
    w = max(len(r["label"]) for r in ROWS) + 2
    for r in ROWS:
        mark = "PASS" if r["ok"] else "FAIL"
        nd = ("" if r["needle"] is None else
              ("  [needle located]" if r["needle_located"]
               else "  [NEEDLE ABSENT FROM LOCK]"))
        print(f"  [{mark}] {r['section']:<4} {r['label']:<{w}} "
              f"claim {r['claim']:>22} | got {r['actual']:>22}{nd}")
    print("-" * 78)
    print(f"  {len(ROWS)-n_fail}/{len(ROWS)} claims match the committed record")
    print(f"  needles: {located} located verbatim, {len(absent)} claimed but "
          f"absent, {derived} derived/structural (no single literal form)")
    for r in absent:
        print(f"    ABSENT: {r['needle']!r} ({r['label']})")
    print(f"  arithmetic artifact: {args.arith_out}")
    print(f"  VERDICT: {'GREEN — LOCK-g ready to commit' if not n_fail and not absent else 'NOT GREEN — report to the design instance'}")
    with open(args.out, "w") as fh:
        json.dump({"item": "LOCK-g §7", "lock": os.path.basename(args.lock),
                   "n_claims": len(ROWS), "n_fail": n_fail,
                   "needles_located": located,
                   "needles_absent": [r["needle"] for r in absent],
                   "needles_derived": derived,
                   "arithmetic": arith, "rows": ROWS,
                   "green": bool(not n_fail and not absent)}, fh, indent=1)
    return 1 if (n_fail or absent) else 0


if __name__ == "__main__":
    sys.exit(main())
