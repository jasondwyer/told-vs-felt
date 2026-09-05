"""e2d closure TEXT OF RECORD -- verification record.

Re-verifies, from committed artifacts only, (a) every figure in the closure
text as patched by the design patch of 2026-09-05 (six clause replacements
R1-R6 over the disposition's §3), and (b) the six replaced clauses
specifically, each on the DOMAIN and under the TEST the patched clause names.
Prints the Fisher table of record (two-sided beside one-sided) for the four
degeneracy steps, and every variant of every test whose second decimal
depends on the variant, so nothing is picked silently (trap 26).

Provenance, not an instrument: reads artifacts, writes nothing. No scipy
(trap 1); exact tests via math.comb; z via erf.

    jlens-qwen36/.venv/bin/python scripts/e2d_closure_verify.py
"""
from __future__ import annotations

import json
from math import comb, erf, sqrt

import numpy as np

from valence_core.e2d import habit as HB
from valence_core.e2d import marks as MRK
from valence_core.e2d.marker import sign_test
from valence_core.stats import binom_test_exact

OK, BAD = [], []


def chk(label, got, want, tol=5e-4, note=""):
    if isinstance(got, (int, float)) and isinstance(want, (int, float)) \
            and not isinstance(got, bool) and not isinstance(want, bool):
        ok = abs(got - want) <= tol
    else:
        ok = got == want
    (OK if ok else BAD).append((label, got, want, note))
    return ok


def fisher_2s(k2, n2, k1, n1):
    """Two-sided Fisher exact, method of small p-values, for k2/n2 vs k1/n1."""
    A, B, C, D = k2, n2 - k2, k1, n1 - k1
    n = A + B + C + D

    def p(x):
        return comb(A + B, x) * comb(C + D, A + C - x) / comb(n, A + C)
    obs = p(A) * (1 + 1e-9)
    lo, hi = max(0, A + C - (C + D)), min(A + B, A + C)
    return float(sum(p(x) for x in range(lo, hi + 1) if p(x) <= obs))


def fisher_g(k2, n2, k1, n1):
    """One-sided Fisher exact, excess in k2/n2 over k1/n1."""
    A, B, C, D = k2, n2 - k2, k1, n1 - k1
    n = A + B + C + D
    hi = min(A + B, A + C)
    return float(sum(comb(A + B, x) * comb(C + D, A + C - x) / comb(n, A + C)
                     for x in range(A, hi + 1)))


def Phi(x):
    return 0.5 * (1 + erf(x / sqrt(2)))


def z_two_prop(k1, n1, k2, n2):
    """Two-proportion z, two-sided, BOTH variance estimators."""
    p1, p2 = k1 / n1, k2 / n2
    pool = (k1 + k2) / (n1 + n2)
    se_pooled = sqrt(pool * (1 - pool) * (1 / n1 + 1 / n2))
    se_unpooled = sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    zp, zu = (p1 - p2) / se_pooled, (p1 - p2) / se_unpooled
    return {"z_pooled": zp, "p_pooled": 2 * (1 - Phi(abs(zp))),
            "z_unpooled": zu, "p_unpooled": 2 * (1 - Phi(abs(zu)))}


# --- artifacts -------------------------------------------------------------
S = {t: json.load(open(f"data/e2d/{t}_sessions.json"))["sessions"]
     for t in ("d1", "d2", "d3")}
SX = {t: json.load(open(f"data/e2d/{t}_sessions.json")) for t in ("d1", "d2", "d3")}
MK = {t: MRK.marked_set(MRK.load(f"data/e2d/{t}_read_marks.json"))
      for t in ("d1", "d2", "d3")}
SC = {t: json.load(open(f"data/e2d/{t}_scores.json")) for t in ("d2", "d3")}
EX = {t: json.load(open(f"data/e2d/{t}_excision_check.json")) for t in ("d2", "d3")}
AN2 = json.load(open("data/e2d/d2_analysis.json"))
PC = json.load(open("data/e2d/dose_paired_d2_d3.json"))
PA = json.load(open("data/e2d/dose_paired_d2_d3_allrounds.json"))
E2A = [json.loads(l) for l in open("data/e2a/sessions.jsonl")]


def M(t, valid=None, with_pick=False):
    out = []
    for s in S[t]:
        if s["arm"] != "M":
            continue
        if valid is True and s["excluded"]:
            continue
        if with_pick and not s["choices"]:
            continue
        out.append(s)
    return out


def degen_counts(t, marked, only=None):
    """(k, n) over the M arm's rounds + choices: audit-degenerate (marked=False)
    or read-marked (marked=True). Domain: all M sessions incl. excluded."""
    k = n = 0
    for s in M(t):
        if only is not None and s["session"] not in only:
            continue
        rs = s["rounds"] + s["choices"]
        n += len(rs)
        if marked:
            k += sum(1 for r in rs if f"M|{s['session']}|{r['phase']}" in MK[t])
        else:
            k += sum(1 for r in rs if r["degen"])
    return k, n


def e2a_conv(rows):
    return [{"arm": r["arm"], "session": r["session"],
             "rounds": [{"phase": "forced", "pole": x["pole"]} for x in r["rounds"]],
             "choices": [{"pick": c["pick"], "picked_pole": c["picked_pole"]}
                         for c in r["choices"]]} for r in rows]


def e2a_alt(rows):
    sec = HB.secondaries(e2a_conv(rows))["by_arm"]
    num = sum(round(v["strict_alternation_rate"] * v["n_alt_decidable"]) for v in sec.values())
    den = sum(v["n_alt_decidable"] for v in sec.values())
    rw = sec["reward"]
    return (num, den, round(rw["strict_alternation_rate"] * rw["n_alt_decidable"]),
            rw["n_alt_decidable"], sec)


print("=" * 78)
print("e2d CLOSURE TEXT OF RECORD -- verification of the six patched clauses")
print("=" * 78)

# --- R1 ---------------------------------------------------------------------
q1 = AN2["Q1"]
p_g = binom_test_exact(q1["k"], q1["n"], q1["p0"], "greater")
p_2 = binom_test_exact(q1["k"], q1["n"], q1["p0"], "two-sided")
print(f"\nR1  Q1 {q1['k']}/{q1['n']} vs p0 = {q1['p0']}: exact binomial one-sided (greater, "
      f"the registered form) p = {p_g:.4f}; artifact p = {q1['p']:.4f}; two-sided {p_2:.4f}")
chk("R1 Q1 3/32", (q1["k"], q1["n"]), (3, 32))
chk("R1 Q1 exact binomial p .878 (artifact)", q1["p"], .878, 1e-3)
chk("R1 Q1 exact binomial p .878 (recomputed, one-sided greater)", p_g, .878, 1e-3)
chk("R1 Q1 scope of record = forced", q1["scope_of_record"].startswith("forced"), True)

# --- R2 ---------------------------------------------------------------------
pm = SC["d2"]["marker"]["primary_paired_within_M"]
st = SC["d2"]["marker"]["sign_test_M"]
diffs = [p["diff"] for p in pm["per_session"] if p["diff"] is not None]
st_re = sign_test(diffs, "greater")
print(f"\nR2  D2 primary Δ+ = {pm['delta']:+.4f}, n = {pm['n_sessions_decidable']}, sd = {pm['sd']:.4f}; "
      f"sign test one-sided (greater): artifact k = {st['k_positive']}/{st['n']} p = {st['p']:.4f}; "
      f"recomputed k = {st_re['k_positive']}/{st_re['n']} p = {st_re['p']:.4f}; "
      f"two-sided would be {min(1.0, 2 * st_re['p']):.4f}")
chk("R2 Δ+ +.103", pm["delta"], .103, 1e-3)
chk("R2 n = 27", pm["n_sessions_decidable"], 27)
chk("R2 sd .40", pm["sd"], .40, 5e-3)
chk("R2 one-sided sign test p .061 (artifact)", st["p"], .061, 1e-3)
chk("R2 one-sided sign test p .061 (recomputed)", st_re["p"], .061, 1e-3)
chk("R2 artifact alternative = greater", st["alternative"], "greater")

# --- R3 ---------------------------------------------------------------------
d2p = {p["session"]: p["diff"] for p in SC["d2"]["marker"]["primary_paired_within_M"]["per_session"] if p["diff"] is not None}
d3p = {p["session"]: p["diff"] for p in SC["d3"]["marker"]["primary_paired_within_M"]["per_session"] if p["diff"] is not None}
shared = sorted(set(d2p) & set(d3p))
clean_change = [d3p[i] - d2p[i] for i in shared]
st_clean = sign_test(clean_change, "greater")
d2a = {p["session"]: p["diff"] for p in json.load(open("data/e2d/d2_scores_allrounds.json"))
       ["marker"]["primary_paired_within_M_all_rounds"]["per_session"] if p["diff"] is not None} \
    if "marker" in json.load(open("data/e2d/d2_scores_allrounds.json")) else None
d3a = {p["session"]: p["diff"] for p in SC["d3"]["marker"]["primary_paired_within_M_all_rounds"]["per_session"] if p["diff"] is not None}
print(f"\nR3  clean paired D2->D3: artifact change {PC['paired_mean_change']:+.4f}, n = {PC['n_shared_indices']}, "
      f"sign test {PC['sign_test']['k_positive']}/{PC['sign_test']['n']} p = {PC['sign_test']['p']:.4f} "
      f"({PC['sign_test']['alternative']}); recomputed change {np.mean(clean_change):+.4f}, n = {len(shared)}, "
      f"sign {st_clean['k_positive']}/{st_clean['n']} p = {st_clean['p']:.4f}; two-sided would be {min(1.0, 2 * st_clean['p']):.4f}")
chk("R3 clean −.0121", PC["paired_mean_change"], -.0121, 1e-4)
chk("R3 clean −.0121 (recomputed)", float(np.mean(clean_change)), -.0121, 1e-4)
chk("R3 clean n = 20", len(shared), 20)
chk("R3 clean one-sided sign test p .41 (artifact)", PC["sign_test"]["p"], .41, 5e-3)
chk("R3 clean one-sided sign test p .41 (recomputed)", st_clean["p"], .41, 5e-3)
chk("R3 clean artifact alternative = greater", PC["sign_test"]["alternative"], "greater")
print(f"    all-rounds paired D2->D3: artifact change {PA['paired_mean_change']:+.4f}, n = {PA['n_shared']}, "
      f"sign test {PA['sign_test']['k_positive']}/{PA['sign_test']['n']} p = {PA['sign_test']['p']:.4f} "
      f"({PA['sign_test']['alternative']}); two-sided would be {min(1.0, 2 * PA['sign_test']['p']):.4f}")
if d2a is not None:
    sh_a = sorted(set(d2a) & set(d3a))
    ch_a = [d3a[i] - d2a[i] for i in sh_a]
    st_a = sign_test(ch_a, "greater")
    print(f"    recomputed all-rounds: change {np.mean(ch_a):+.4f}, n = {len(sh_a)}, sign {st_a['k_positive']}/{st_a['n']} p = {st_a['p']:.4f}")
    chk("R3 all-rounds +.0149 (recomputed)", float(np.mean(ch_a)), .0149, 1e-4)
    chk("R3 all-rounds one-sided sign p .27 (recomputed)", st_a["p"], .27, 5e-3)
chk("R3 all-rounds +.0149", PA["paired_mean_change"], .0149, 1e-4)
chk("R3 all-rounds n = 24", PA["n_shared"], 24)
chk("R3 all-rounds one-sided sign test p .27 (artifact)", PA["sign_test"]["p"], .27, 5e-3)
chk("R3 all-rounds artifact alternative = greater", PA["sign_test"]["alternative"], "greater")
chk("R3 opposite signs", (PC["paired_mean_change"] < 0) and (PA["paired_mean_change"] > 0), True)

# --- R4: the Fisher table of record -----------------------------------------
a1, a2, a3 = (degen_counts(t, False) for t in ("d1", "d2", "d3"))
r1, r2, r3 = (degen_counts(t, True) for t in ("d1", "d2", "d3"))
steps = [("audit .10->.20", a2, a1), ("audit .20->.30", a3, a2),
         ("read  .10->.20", r2, r1), ("read  .20->.30", r3, r2)]
print("\nR4  FISHER TABLE OF RECORD (M arm, rounds + choices, all sessions incl. excluded)")
print(f"    counts: audit D1 {a1[0]}/{a1[1]}  D2 {a2[0]}/{a2[1]}  D3 {a3[0]}/{a3[1]}   "
      f"read D1 {r1[0]}/{r1[1]}  D2 {r2[0]}/{r2[1]}  D3 {r3[0]}/{r3[1]}")
print(f"    {'step':<16}{'two-sided':>12}{'one-sided':>12}")
F = {}
for lbl, hi, lo in steps:
    F[lbl] = (fisher_2s(hi[0], hi[1], lo[0], lo[1]), fisher_g(hi[0], hi[1], lo[0], lo[1]))
    print(f"    {lbl:<16}{F[lbl][0]:>12.4f}{F[lbl][1]:>12.4f}")
chk("R4 read .10->.20 two-sided .021", F["read  .10->.20"][0], .021, 1e-3)
chk("R4 read .10->.20 one-sided .011", F["read  .10->.20"][1], .011, 1e-3)
chk("R4 audit .20->.30 two-sided .15", F["audit .20->.30"][0], .15, 5e-3)
chk("R4 read .20->.30 two-sided .20", F["read  .20->.30"][0], .20, 5e-3)
chk("R4 audit .20->.30 one-sided >= .10", F["audit .20->.30"][1] >= .10, True, note=f"{F['audit .20->.30'][1]:.4f}")
chk("R4 read .20->.30 one-sided >= .10", F["read  .20->.30"][1] >= .10, True, note=f"{F['read  .20->.30'][1]:.4f}")
chk("R4 audit .10->.20 two-sided (unresolved) >= .10", F["audit .10->.20"][0] >= .10, True, note=f"{F['audit .10->.20'][0]:.4f}")
chk("R4 rates audit .000/.023/.047", tuple(round(k / n, 3) for k, n in (a1, a2, a3)), (0.0, .023, .047))
chk("R4 rates read .000/.113/.155", tuple(round(k / n, 3) for k, n in (r1, r2, r3)), (0.0, .113, .155))

# --- R5 ---------------------------------------------------------------------
print("\nR5  Δ_first domains")
for t, lbl in (("d2", "0.20"), ("d3", "0.30")):
    valid = M(t, valid=True, with_pick=True)
    anyc = M(t, with_pick=True)
    kv = sum(1 for s in valid if s["first_free_pick_pos"])
    ka = sum(1 for s in anyc if s["first_free_pick_pos"])
    exc = [(s["session"], s["exclude_reason"]) for s in anyc if s["excluded"]]
    print(f"    {lbl}: valid (e2a-scope exclusion rule, scope of record '{SX[t]['exclusion_scope']}') "
          f"{kv}/{len(valid)} = {kv/len(valid):.4f} -> Δ_first {kv/len(valid)-0.5:+.4f};   "
          f"all M with a first pick {ka}/{len(anyc)} = {ka/len(anyc):.4f} -> Δ {ka/len(anyc)-0.5:+.4f};   "
          f"excluded-with-a-pick: {exc}")
    if t == "d2":
        chk("R5 0.20 valid 15/29", (kv, len(valid)), (15, 29))
        chk("R5 0.20 Δ_first +0.017 (valid)", kv / len(valid) - 0.5, .017, 5e-4)
        chk("R5 0.20 all-with-pick 15/30", (ka, len(anyc)), (15, 30))
        chk("R5 0.20 Δ 0.000 (all with pick)", ka / len(anyc) - 0.5, 0.0, 1e-9)
        chk("R5 excluded idx 30 is the extra session", exc, [(30, "lexical:plaza@free0")])
        chk("R5 D2 exclusion scope of record = e2a", SX["d2"]["exclusion_scope"], "e2a")
        chk("R5 D2 M excluded (run scope) = 3", SX["d2"]["exclusions"]["M"]["excluded_run_scope"], 3)
    else:
        chk("R5 0.30 valid 14/23", (kv, len(valid)), (14, 23))
        chk("R5 0.30 all-with-pick 14/23 (domains coincide)", (ka, len(anyc)), (14, 23))
        chk("R5 0.30 Δ_first +0.109", kv / len(valid) - 0.5, .109, 5e-4)
        pb = binom_test_exact(kv, len(valid), .5, "greater")
        print(f"    0.30 one-sided exact binomial P(X >= {kv} | {len(valid)}, .5) = {pb:.4f}; "
              f"two-sided {binom_test_exact(kv, len(valid), .5, 'two-sided'):.4f}")
        chk("R5 0.30 one-sided exact binomial p .202", pb, .202, 1e-3)
# habit-break rates, both domains
for t, want in (("d2", (1, 30)), ("d3", (1, 23))):
    h_all = HB.secondaries(M(t))["by_arm"]["M"]
    h_val = HB.secondaries(M(t, valid=True))["by_arm"]["M"]
    h_art = SC[t]["habit"]["secondaries"]["by_arm"]["M"]
    print(f"    {t} first-pick habit break: artifact {h_art['n_breaks']}/{h_art['n_decidable']}; "
          f"recomputed all-sessions {h_all['n_breaks']}/{h_all['n_decidable']}; valid-only {h_val['n_breaks']}/{h_val['n_decidable']}"
          + (f"; artifact domain string: {SC[t]['habit'].get('secondaries_domain')!r}"))
    chk(f"R5 {t} habit break {want} (artifact)", (h_art["n_breaks"], h_art["n_decidable"]), want)
    chk(f"R5 {t} habit break {want} reproduces on ALL sessions incl. excluded", (h_all["n_breaks"], h_all["n_decidable"]), want)
chk("R5 D3 artifact names the rule-23 domain", SC["d3"]["habit"]["secondaries_domain"], "all sessions including excluded (rule 23)")

# --- R6 ---------------------------------------------------------------------
print("\nR6  alternation ladder")
n_all, d_all, rn_all, rd_all, sec_all = e2a_alt(E2A)
n_val, d_val, rn_val, rd_val, sec_val = e2a_alt([r for r in E2A if not r["excluded"]])
print(f"    e2a all sessions incl. excluded: pooled {n_all}/{d_all} = {n_all/d_all:.4f}; reward {rn_all}/{rd_all} = {rn_all/rd_all:.4f}")
print(f"    e2a valid only:                  pooled {n_val}/{d_val} = {n_val/d_val:.4f}; reward {rn_val}/{rd_val} = {rn_val/rd_val:.4f}")
chk("R6 e2a pooled .840 on all sessions", n_all / d_all, .840, 5e-4)
chk("R6 e2a pooled = 157/187", (n_all, d_all), (157, 187))
chk("R6 e2a reward .827 on all sessions", rn_all / rd_all, .827, 5e-4)
chk("R6 e2a reward = 86/104", (rn_all, rd_all), (86, 104))
chk("R6 e2a valid-only pooled .837", n_val / d_val, .837, 5e-4)
chk("R6 e2a valid-only reward .824", rn_val / rd_val, .824, 5e-4)
for t, want in (("d2", .690), ("d3", .522)):
    h_art = SC[t]["habit"]["secondaries"]["by_arm"]["M"]
    h_all = HB.secondaries(M(t))["by_arm"]["M"]
    h_val = HB.secondaries(M(t, valid=True))["by_arm"]["M"]
    print(f"    {t} M strict alternation: artifact {h_art['strict_alternation_rate']:.4f} (n_alt {h_art['n_alt_decidable']}); "
          f"all-sessions {h_all['strict_alternation_rate']:.4f} ({h_all['n_alt_decidable']}); valid-only {h_val['strict_alternation_rate']:.4f} ({h_val['n_alt_decidable']})")
    chk(f"R6 {t} alternation {want} (artifact)", h_art["strict_alternation_rate"], want, 5e-4)
    chk(f"R6 {t} alternation {want} on ALL sessions", h_all["strict_alternation_rate"], want, 5e-4)
allb = sum(v["n_breaks"] for v in sec_all.values()); alln = sum(v["n_decidable"] for v in sec_all.values())
print(f"    e2a pooled first-pick break {allb}/{alln} = {allb/alln:.4f}; e2d 1/30 = {1/30:.4f}, 1/23 = {1/23:.4f}; ratio e2a/e2d ~ {(allb/alln)/(2/53):.1f}x")
chk("R6 e2a break ~.17", allb / alln, .17, .01, f"{allb}/{alln}")
f_break = fisher_2s(1, 23, 1, 30)
zb = z_two_prop(1, 30, 1, 23)
print(f"    1/30 vs 1/23: Fisher exact two-sided {f_break:.4f}; one-sided {fisher_g(1,23,1,30):.4f}; "
      f"two-proportion z pooled p = {zb['p_pooled']:.4f} (the '.85' the held text carried)")
chk("R6 1/30 vs 1/23 Fisher two-sided 1.00", f_break, 1.00, 5e-3)
a2n = SC["d2"]["habit"]["secondaries"]["by_arm"]["M"]; a3n = SC["d3"]["habit"]["secondaries"]["by_arm"]["M"]
k2a = round(a2n["strict_alternation_rate"] * a2n["n_alt_decidable"]); n2a = a2n["n_alt_decidable"]
k3a = round(a3n["strict_alternation_rate"] * a3n["n_alt_decidable"]); n3a = a3n["n_alt_decidable"]
zz = z_two_prop(k2a, n2a, k3a, n3a)
f2, f1 = fisher_2s(k2a, n2a, k3a, n3a), fisher_g(k2a, n2a, k3a, n3a)
print(f"    D2->D3 alternation step {k2a}/{n2a} = {k2a/n2a:.4f} vs {k3a}/{n3a} = {k3a/n3a:.4f}:")
print(f"      two-proportion z, POOLED variance   : z = {zz['z_pooled']:.4f}, two-sided p = {zz['p_pooled']:.4f}")
print(f"      two-proportion z, UNPOOLED variance : z = {zz['z_unpooled']:.4f}, two-sided p = {zz['p_unpooled']:.4f}")
print(f"      Fisher exact two-sided (the entry's declared test of record for counts): {f2:.4f}; one-sided {f1:.4f}")
chk("R6 D2->D3 step 'two-proportion z p = .21' -- UNPOOLED variance", round(zz["p_unpooled"], 2), .21, 1e-9, f"{zz['p_unpooled']:.4f}")
chk("R6 D2->D3 step 'two-proportion z p = .21' -- POOLED variance", round(zz["p_pooled"], 2), .21, 1e-9, f"{zz['p_pooled']:.4f}")
chk("R6 D2->D3 step unresolved under every variant (p > .05)", min(zz["p_pooled"], zz["p_unpooled"], f2) > .05, True)

# =============================================================================
print("\n" + "=" * 78)
print("FULL TEXT -- every other figure in the patched closure text")
print("=" * 78)
for t, med, p10 in (("d2", .574, .524), ("d3", .613, .526)):
    k2 = SC[t]["readability"]["v2_and_read_clean"]["k2"]
    chk(f"{t} readability median {med}", k2["median"], med, 1e-3)
    chk(f"{t} readability p10 {p10}", k2["p10"], p10, 1e-3)
chk("D2 AUC_R .534", SC["d2"]["readability"]["AUC_R"]["median"], .534, 1e-3)
chk("D3 has NO AUC_R", "AUC_R" not in SC["d3"]["readability"], True)
chk("0.20 excised +.103", SC["d2"]["marker"]["primary_paired_within_M"]["delta"], .103, 1e-3)
chk("0.30 excised +.141", SC["d3"]["marker"]["primary_paired_within_M"]["delta"], .141, 1e-3)
chk("0.20 in situ +.127", EX["d2"]["in_situ"]["M"]["paired_delta"], .127, 1e-3)
chk("0.30 in situ +.062", EX["d3"]["in_situ"]["M"]["paired_delta"], .062, 1e-3)
bar = SC["d2"]["marker"]["bar_half_G"]
chk("bar 0.158", bar, .1578, 1e-3)
cells = [SC["d2"]["marker"]["primary_paired_within_M"]["delta"], SC["d3"]["marker"]["primary_paired_within_M"]["delta"],
         EX["d2"]["in_situ"]["M"]["paired_delta"], EX["d3"]["in_situ"]["M"]["paired_delta"]]
chk("every cell below bar", all(c < bar for c in cells), True)
dR = SC["d2"]["marker"]["paired_within_R"]["delta"]
chk("2|Delta_R| = .138", 2 * abs(dR), .138, 1e-3)
chk("Delta+ fails 2|Delta_R|", pm["delta"] > 2 * abs(dR), False)
chk("2.3x at 0.30", SC["d3"]["marker"]["primary_paired_within_M"]["delta"] / EX["d3"]["in_situ"]["M"]["paired_delta"], 2.3, .05)
gap20 = SC["d2"]["marker"]["primary_paired_within_M"]["delta"] - EX["d2"]["in_situ"]["M"]["paired_delta"]
gap30 = SC["d3"]["marker"]["primary_paired_within_M"]["delta"] - EX["d3"]["in_situ"]["M"]["paired_delta"]
chk("context gap flips direction across dose", (gap20 < 0) != (gap30 < 0), True, note=f"{gap20:+.4f} / {gap30:+.4f}")
q3 = AN2["Q3"]
est = {"paired within-M": q3["delta_plus"], "pooled within-M": q3["beside_pooled_within_M"],
       "across-arm vs S": q3["beside_across_arm_vs_S"], "paired v2-clean only": q3["beside_v2clean_only"],
       "task-matched": (q3.get("beside_task_matched_M") or {}).get("delta")}
vals = [v for v in est.values() if v is not None]
chk("5 estimators counted", len(vals), 5)
chk("estimator min -.070", min(vals), -.070, 1e-3)
chk("estimator max +.103", max(vals), .103, 1e-3)
chk("unpaired clean +.038", PC["unpaired_difference_of_means"], .038, 1e-3)
chk("unpaired all-rounds +.068", PA["unpaired_difference_of_means"], .068, 1e-3)
ci = 1.959964 * PC["paired_sd"] / (PC["n_shared_indices"] ** .5)
chk("paired CI ~+/-.15", ci, .15, .015, f"1.96*sd/sqrt(n) = {ci:.4f}")
d2_only = sorted(set(d2p) - set(d3p))
chk("idx 12 decidable at 0.20 only", 12 in d2_only, True, note=f"D2-only = {d2_only}")
chk("D3 ran 24 M sessions", len(M("d3")), 24)
chk("D2 ran 32 M sessions", len(M("d2")), 32)
# 62% / 38% decomposition of the composition artifact (the values-check's
# sequential decomposition, closure_valuescheck.json claim A7): D2's mean moves
# from its value on the 20 shared indices (A) to its value on D3's roster
# (B: shared + the indices D3 ran but could not decide) to its full value (C).
# |B - A| / |C - A| is the share due to differential decidability (idx 12);
# |C - B| / |C - A| the share due to roster truncation (indices D3 never ran).
d3_roster_max = max(p["session"] for p in SC["d3"]["marker"]["primary_paired_within_M"]["per_session"])
lost_to_clean = [i for i in d2_only if i <= d3_roster_max]
never_run = [i for i in d2_only if i > d3_roster_max]
A = float(np.mean([d2p[i] for i in shared]))
B = float(np.mean([d2p[i] for i in shared + lost_to_clean]))
C = float(np.mean(list(d2p.values())))
chk("composition: idx 12 is the only D2-only index inside D3's roster", lost_to_clean, [12])
chk("composition: 6 indices D3 never ran", len(never_run), 6, note=f"{never_run}")
chk("composition 62% one session (idx 12)", abs(B - A) / abs(C - A), .62, .01, note=f"|{B-A:+.4f}|/|{C-A:+.4f}|")
chk("composition 38% roster truncation", abs(C - B) / abs(C - A), .38, .01, note=f"|{C-B:+.4f}|/|{C-A:+.4f}|")
sh24 = {s["session"] for s in M("d2")} & {s["session"] for s in M("d3")}
chk("shared indices = 24", len(sh24), 24)
for t, aw, rw in (("d2", .025, .133), ("d3", .047, .155)):
    a, r = degen_counts(t, False, sh24), degen_counts(t, True, sh24)
    chk(f"{t} shared audit {aw}", a[0] / a[1], aw, 1e-3)
    chk(f"{t} shared read {rw}", r[0] / r[1], rw, 1e-3)
m2 = {s["session"]: s for s in M("d2")}; m3 = {s["session"]: s for s in M("d3")}


def marks_of(t, i):
    s = {"d2": m2, "d3": m3}[t][i]
    rs = s["rounds"] + s["choices"]
    return sum(1 for r in rs if f"M|{i}|{r['phase']}" in MK[t]), len(rs)


chk("s12 D2 0/10", marks_of("d2", 12), (0, 10))
chk("s12 D3 7/10", marks_of("d3", 12), (7, 10))
for i in (1, 5):
    chk(f"s{i} D2 10/10", marks_of("d2", i), (10, 10))
    chk(f"s{i} D3 10/10", marks_of("d3", i), (10, 10))
tot = sum(marks_of("d2", i)[0] + marks_of("d3", i)[0] for i in sh24)
c15 = sum(marks_of("d2", i)[0] + marks_of("d3", i)[0] for i in (1, 5))
chk("idx 1,5 carry 58%", c15 / tot, .58, .01, f"{c15}/{tot}")
for arm, want in (("M", .023), ("R", .045), ("S", .000)):
    rs = [r for s in S["d2"] if s["arm"] == arm for r in s["rounds"] + s["choices"]]
    chk(f"D2 {arm} arm degeneracy {want}", sum(1 for r in rs if r["degen"]) / len(rs), want, 1e-3)
n_ch = {t: sum(len(s["choices"]) for s in S[t]) for t in ("d1", "d2", "d3")}
chk("D1 42 choices", n_ch["d1"], 42); chk("D2 357 choices", n_ch["d2"], 357); chk("D3 138 choices", n_ch["d3"], 138)
chk("537 total", sum(n_ch.values()), 537)
chk("96 sessions", sum(len(S[t]) for t in ("d1", "d2", "d3")), 96)
for t in ("d1", "d2", "d3"):
    acc = SX[t]["acceptance"]
    chk(f"{t} every read at KL = 0", acc["kl_all_exact"] and acc["kl_exactly_zero"] == n_ch[t], True)
r_is = EX["d3"]["in_situ_seconds"] / EX["d3"]["n_in_situ_forwards"]
r_ex = SC["d3"]["marker"]["seconds"] / SC["d3"]["marker"]["n_probe_forwards"]
chk("in situ 2.57 s/fwd", r_is, 2.57, .02); chk("excised 0.54 s/fwd", r_ex, 0.54, .02); chk("ratio 4.7x", r_is / r_ex, 4.7, .1)
ss = SC["d2"]["readability"]["stored_classifier"]["self_score"]
chk("transfer .958 self-score", ss["auc"], .958, 1e-3); chk("refit false", ss["refit"], False)
chk("0.10 anchor n = 4 M sessions", len(M("d1")), 4)
chk("D1 readability .583", SX["d1"]["readability"]["k2_resampled"]["median"], .583, 1e-3)
chk("run-dose rule STOP, SCOPED", AN2["run_dose_rule"]["decision"], "STOP, SCOPED")
chk("Q2 fails", AN2["Q2"]["passes"], False); chk("Q3 fails", AN2["Q3"]["passes"], False)

print("\n" + "=" * 78)
for lbl, got, want, note in OK:
    print(f"  PASS  {lbl:<58} got {got!r:<28} {note}")
print("-" * 78)
for lbl, got, want, note in BAD:
    print(f"  FAIL  {lbl:<58} got {got!r}  want {want!r}  {note}")
print(f"\n  {len(OK)} pass, {len(BAD)} FAIL")
