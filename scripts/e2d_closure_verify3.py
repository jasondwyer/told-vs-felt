#!/usr/bin/env python3
"""e2d closure TEXT OF RECORD -- verification of the THIRD-PASS patch
(design patch 2026-09-06 §1, R7-R13 over the eight glosses of the third
values-check, data/e2d/closure_glosscheck3.json).

Self-contained on purpose: scripts/e2d_closure_verify.py (125 checks over
R1-R6 and the full text) scored the committed record and stays frozen; this
script checks every figure R7-R13 introduce, each AT THE PRECISION THE TEXT
PRINTS IT, against the committed artifacts. A figure that reproduces only
under a looser tolerance is a FAIL here, because "reproduces as stated" is
the standard the closure has been held to three times.
"""
import json, math, os, re, subprocess, sys
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO); sys.path.insert(0, REPO)
from valence_core.stats import fisher_one_sided
from valence_core.e2d import habit as H

def quoted_text() -> str:
    """The design-authored text of record: the '  > ' blockquote in the HELD file, unwrapped."""
    lines = open("HELD-e2d-closure-entry.md").read().split("\n")
    return " ".join(l[4:] for l in lines if l.startswith("  > "))

results = []
def chk(name, got, want, tol=0.0, note=""):
    ok = (abs(got - want) <= tol) if isinstance(got, (int, float)) and isinstance(want, (int, float)) else (got == want)
    results.append((name, ok)); print(f"  {'PASS' if ok else 'FAIL'}  {name:66s} got {got!r:<28} want {want!r}  {note}")
    return ok

PC = json.load(open("data/e2d/dose_paired_d2_d3.json"))
sd, n, mean = PC["paired_sd"], PC["n_shared_indices"], PC["paired_mean_change"]
G = json.load(open("data/e2d/closure_glosscheck3.json"))["code_recomputation_at_write_time"]["item1_2_paired_CI"]["bar_half_G"]
z, t19 = 1.959964, 2.093024
zh, th = z * sd / math.sqrt(n), t19 * sd / math.sqrt(n)
print("R14 (strip of R7): z-form 95% CI on the clean-set paired change, at the printed precision")
chk("R14 clean set = 20 shared indices", n, 20)
chk("R14 z CI lower bound -.156", round(mean - zh, 3), -.156, note=f"raw {mean - zh:.6f}")
chk("R14 z CI upper bound +.132", round(mean + zh, 3), .132, note=f"raw {mean + zh:.6f}")
chk("R14 the text names the form (z) and the set (clean-set) and makes no bar claim",
    ("z-form 95% CI on the clean-set paired change: [−.156, +.132]" in quoted_text()) and ("bar-sized" not in quoted_text()), True)
# record beside (not a text check): the all-rounds pairing's CI, the reason the unqualified clause was held
PA = json.load(open("data/e2d/dose_paired_d2_d3_allrounds.json"))
zha = z * PA["paired_sd"] / math.sqrt(PA["n_shared"])
print(f"    beside: all-rounds pairing (n {PA['n_shared']}) z CI [{PA['paired_mean_change'] - zha:+.3f}, {PA['paired_mean_change'] + zha:+.3f}] -- contains a bar-sized change both ways; no longer claimed either way")
print("R8  one-sided .011 (attribution dropped; the figure)")
chk("R8 read .10->.20 one-sided Fisher .011", round(fisher_one_sided(34, 266, 0, 40), 3), .011, note=f"{fisher_one_sided(34, 266, 0, 40):.5f}")
print("R9  59% of the marks (40/68 on the 24 shared indices)")
SC = {k: json.load(open(f"data/e2d/{k}_scores.json")) for k in ("d2", "d3")}
# the ORIGINAL verify's convention (scripts/e2d_closure_verify.py marks_of): read-marks keyed
# arm|session|phase over the M-arm sessions' rounds + choices; the 24 shared M indices.
from valence_core.e2d import marks as MRK
MKS = {k: MRK.marked_set(MRK.load(f"data/e2d/{k}_read_marks.json")) for k in ("d2", "d3")}
MS = {k: {s["session"]: s for s in json.load(open(f"data/e2d/{k}_sessions.json"))["sessions"] if s["arm"] == "M"} for k in ("d2", "d3")}
def marks_of(k, i):
    rs = MS[k][i]["rounds"] + MS[k][i]["choices"]
    return sum(1 for r in rs if f"M|{i}|{r['phase']}" in MKS[k]), len(rs)
d2s, d3s = set(MS["d2"]), set(MS["d3"])
sh = sorted(d2s & d3s)
tot = sum(marks_of("d2", i)[0] + marks_of("d3", i)[0] for i in sh)
top = sum(marks_of("d2", i)[0] + marks_of("d3", i)[0] for i in (1, 5))
chk("R9 24 shared indices", len(sh), 24)
chk("R9 marks on the 24 shared indices = 68", tot, 68)
chk("R9 idx 1 + 5 carry 40 (10/10 at both doses each)", (top, marks_of("d2", 1), marks_of("d3", 1), marks_of("d2", 5), marks_of("d3", 5)), (40, (10, 10), (10, 10), (10, 10), (10, 10)))
chk("R9 40/68 rounds to 59%", round(100 * 40 / 68), 59, note=f"{100 * 40 / 68:.2f}%")
print("R10 the 0.10 anchor's pooled within-M delta")
d1 = json.load(open("data/e2d/d1_sessions.json"))["marker"]["deltas"]["clean"]["delta_plus_within_M"]
chk("R10 -.239 over 20/20 generations", (round(d1["delta"], 3), d1["n_steered"], d1["n_unsteered"]), (-.239, 20, 20), note=f"{d1['delta']:.6f}")
print("R11 four to five times below e2a's .17")
e2a = [json.loads(l) for l in open("data/e2a/sessions.jsonl") if l.strip()]
brk = [r for r in e2a if H.follows_habit(r) is not None]; k = sum(1 for r in brk if not H.follows_habit(r))
chk("R11 e2a break 32/188 all sessions", (k, len(brk)), (32, 188))
chk("R11 .17", round(k / len(brk), 2), .17, note=f"{k / len(brk):.4f}")
r = k / len(brk)
chk("R11 5.1x D2's 1/30", round(r / (1 / 30), 1), 5.1); chk("R11 3.9x D3's 1/23", round(r / (1 / 23), 1), 3.9); chk("R11 4.5x pooled 2/53", round(r / (2 / 53), 1), 4.5)
chk("R11 'four to five times' holds at integer precision (each ratio rounds to 4 or 5)", sorted({round(r * 30), round(r * 23), round(r * 26.5)}), [4, 5], note=f"one-decimal range {r*23:.1f}-{r*30:.1f}; the exact figures follow in the text")
print("R12 the composition artifact, both orders")
d2p = {q["session"]: q["diff"] for q in SC["d2"]["marker"]["primary_paired_within_M"]["per_session"] if q["diff"] is not None}
d3p = {q["session"]: q["diff"] for q in SC["d3"]["marker"]["primary_paired_within_M"]["per_session"] if q["diff"] is not None}
shared = sorted(set(d2p) & set(d3p)); d2_only = sorted(set(d2p) - set(d3p))
d3max = max(q["session"] for q in SC["d3"]["marker"]["primary_paired_within_M"]["per_session"])
lost = [i for i in d2_only if i <= d3max]; never = [i for i in d2_only if i > d3max]
A = sum(d2p[i] for i in shared) / len(shared); B = sum(d2p[i] for i in shared + lost) / len(shared + lost)
Bt = sum(d2p[i] for i in shared + never) / len(shared + never); C = sum(d2p.values()) / len(d2p)
chk("R12 idx 12 is the one session decidable at 0.20 only inside D3's roster", lost, [12])
chk("R12 D3 ran 24 M sessions to D2's 32", (len(d3s), len(d2s)), (24, 32))
chk("R15 (strip of R12): the text prints NO split percentages", ("62/38" in quoted_text()) or ("46/54" in quoted_text()), False)
chk("R15 the two sources exist: idx 12 (+idx12 moves the mean) and the six never-run (truncation moves it)", (round(B - A, 4) != 0.0, round(Bt - A, 4) != 0.0, len(never)), (True, True, 6), note=f"A {A:.4f} B {B:.4f} Bt {Bt:.4f} C {C:.4f}")
print(f"    beside (artifact, not text): splits 62/38 with idx 12 added first to the paired base, 46/54 with truncation added first; C - A = {C - A:+.4f} either way")
print("R13 slip 10: defined only in the untracked design handoff")
g = subprocess.run(["git", "grep", "-n", "-e", "slip (10)", "-e", "(10) the", "HEAD", "--", "RESULTS.md", "PROPOSAL-j-dose-escalation.md", "CLAUDE.md"], capture_output=True, text=True).stdout.strip()
chk("R13 no committed definition of slip (10) in the record docs", g, "")
u = os.path.exists("HANDOFF-2026-09-04-design.md") and "**(10)**" in open("HANDOFF-2026-09-04-design.md").read()
chk("R13 defined in the untracked HANDOFF-2026-09-04-design.md §2", u, True)
chk("R13 'with coherence' is the quoted failure mode there", "with coherence" in open("HANDOFF-2026-09-04-design.md").read() if u else False, True)
print("provenance: the eight passages replaced exactly once (R7-R13), then R7 and R12 stripped to bare figures (R14, R15)")
held = quoted_text()
olds = ["the paired CI, ±.15, spans the bar", "the D3-gate entry's figure", "carry 58% of the marks", "carries no marker value", "~4× below", "62% one session decidable", "(slip 10).",
        "[−.157", "half-width .144", "bar-sized", "removed first", "order-dependent"]
chk("R7-R15 no old or struck clause survives in the quoted text", [o for o in olds if o in held], [])
n_ok = sum(1 for _, ok in results if ok)
print("-" * 100)
print(f"  {n_ok}/{len(results)} third-pass checks pass" + ("" if n_ok == len(results) else "  -- HELD: a figure does not reproduce at its printed precision"))
sys.exit(0 if n_ok == len(results) else 1)
