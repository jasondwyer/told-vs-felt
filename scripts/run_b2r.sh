#!/usr/bin/env bash
# B2-r arc driver — ADDENDUM-g3 v1.2 (licensed at f14d249).
# One campaign, one characterized backend. Uncached throughout.
#
# Gate order is the protocol's: respawn (i) INTEGRITY and (ii) BACKEND both
# PASS before any experimental forward, and then the NEW sampling assertion
# before any temperature-1.0 trial — the determinism gate compares logits and
# greedy ids and has never tested a sampled draw.
set -uo pipefail

REPO=/workspace/repo/jspace-lab
PY=/workspace/venv/bin/python
LOGS=/workspace/logs/b2r-2026-08-24
D=$REPO/data/olmo
STAGES="base sft dpo instruct"

mkdir -p "$LOGS"; cd "$REPO"
# shellcheck disable=SC1091
[ -f /workspace/env.sh ] && . /workspace/env.sh
say() { echo "##### $* ($(date -u +%H:%M:%SZ)) #####"; }
die() { echo "!!!!! ARC STOPPED: $* !!!!!"; date -u; exit 1; }
exec > >(tee -a "$LOGS/arc.txt") 2>&1

say "B2-r ARC START"
echo "  host      : $(hostname)"
echo "  gpu       : $(nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader)"
echo "  repo head : ${REPO_HEAD:-UNSTAMPED} (stamped from the laptop)"
echo "  lock      : ADDENDUM-g3 v1.2 (f14d249)"
echo "  decoding  : temp 1.0, max 100, uncached, seeds live"

say "RESPAWN (i) INTEGRITY"
$PY scripts/box_respawn_check.py 2>&1 | tee "$LOGS/respawn_integrity.txt"
[ "${PIPESTATUS[0]}" -eq 0 ] || die "integrity gate FAILED — incident; touch nothing, escalate"

say "RESPAWN (ii) BACKEND CHARACTERIZATION"
$PY scripts/box_determinism.py --stage base 2>&1 | tee "$LOGS/respawn_determinism.txt"
grep -q "repeat-exact(det ON)=True" "$LOGS/respawn_determinism.txt" \
  || die "backend gate FAILED — deterministic repeat is not exact on this host"

# --- Base re-extraction (L60 -> L44, bare template), then its fracs -------
say "BASE RE-EXTRACTION (L44, bare template, as-stored fingerprints)"
$PY scripts/box_b2r_concepts.py --stage base \
    --out "$D/b2r_concepts_base.json" 2>&1 | tee "$LOGS/concepts_base.txt"
[ "${PIPESTATUS[0]}" -eq 0 ] || die "Base re-extraction failed"

say "RECOMPUTE BASE FRAC ROWS (they were provisional)"
$PY - <<'PYEOF' 2>&1 | tee "$LOGS/frac_recompute.txt"
import json, numpy as np, os
D="/workspace/repo/jspace-lab/data/olmo"
t=json.load(open(f"{D}/b2r_frac_table.json"))
j=json.load(open(f"{D}/b2r_concepts_base.json")); z=np.load(f"{D}/b2r_concepts_base.npz")
R44=t["stages"]["base"]["R_44"]
cs=[c for c in t["stages"]["base"]["concepts"]]
new={}
for c in cs:
    nv=float(np.linalg.norm(z[c]))
    fr={str(s): s*nv/R44 for s in (1.0,2.0,4.0,8.0)}
    new[c]={"raw_norm":nv,"frac_equivalent":fr,"alpha":{k:v*R44 for k,v in fr.items()}}
    print(f"  {c:<15} |v| {nv:9.4f}  frac s=1 {fr['1.0']:.4f}  s=8 {fr['8.0']:.4f}")
t["stages"]["base"]["concepts"]=new
t["stages"]["base"]["PROVISIONAL"]="RESOLVED 2026-08-24: recomputed from the L44/bare re-extraction."
t["stages"]["base"]["source"]="b2r_concepts_base.npz (L44, bare template)"
json.dump(t, open(f"{D}/b2r_frac_table.json","w"), indent=1)
print("  base frac rows recomputed and no longer provisional")
PYEOF

# --- NEW GATE: sampled draws reproducible from their seed -----------------
# Ordered AFTER the Base re-extraction deliberately: the assertion builds a
# real dose through at_frac at L44, and Base's vectors are at L60 until it
# re-extracts. Asserting a dose path that is not the one the campaign will
# use would be a gate in name only.
for s in $STAGES; do
  say "SAMPLING REPRODUCIBILITY | $s"
  $PY scripts/box_b2r_sampling_smoke.py --stage "$s" \
      --out "$D/b2r_sampling_${s}.json" 2>&1 | tee "$LOGS/sampling_${s}.txt"
  [ "${PIPESTATUS[0]}" -eq 0 ] || die "sampling assertion FAILED at $s — no B2-r trial could be re-derived from its seed"
done
say "ALL THREE GATES PASS — experimental forwards licensed"


# --- §1 CONTROL: the positive control, dose-free --------------------------
for s in $STAGES; do
  say "§1 CONTROL | $s"
  $PY scripts/box_b2r_campaign.py --part control --stage "$s" \
      --out "$D/b2r_control_${s}.json" 2>&1 | tee "$LOGS/control_${s}.txt"
  [ "${PIPESTATUS[0]}" -eq 0 ] || die "§1 CONTROL failed at $s"
done
say "[g3-A] READING"
$PY scripts/b2r_analyze.py --dir "$D" --out "$D/b2r_analysis.json" 2>&1 | tee "$LOGS/analysis_g3a.txt"

# --- §2 QUALIFICATION: the dose ladder ------------------------------------
for s in $STAGES; do
  say "§2 QUALIFICATION | $s"
  $PY scripts/box_b2r_campaign.py --part qualify --stage "$s" \
      --out "$D/b2r_qualify_${s}.json" 2>&1 | tee "$LOGS/qualify_${s}.txt"
  [ "${PIPESTATUS[0]}" -eq 0 ] || die "§2 QUALIFICATION failed at $s"
done
say "[g3-B] READING"
$PY scripts/b2r_analyze.py --dir "$D" --out "$D/b2r_analysis.json" 2>&1 | tee "$LOGS/analysis_g3b.txt"

# --- §3 EXPLORATION: only stages holding a qualified MED_c ----------------
for s in $STAGES; do
  MED=$($PY -c "
import json,sys
try:
    a=json.load(open('$D/b2r_analysis.json'))
    m=a.get('g3b',{}).get('$s',{}).get('MED_c')
    print('' if m is None else m)
except Exception: print('')
")
  if [ -z "$MED" ]; then
    echo "##### §3 SKIPPED | $s — no qualified MED_c (HARD STOP by design, §2) #####"
    continue
  fi
  say "§3 EXPLORATION | $s | MED_c = $MED"
  $PY scripts/box_b2r_campaign.py --part explore --stage "$s" --med-c "$MED" \
      --out "$D/b2r_explore_${s}.json" 2>&1 | tee "$LOGS/explore_${s}.txt"
  [ "${PIPESTATUS[0]}" -eq 0 ] || die "§3 EXPLORATION failed at $s"
done

say "FINAL READING"
$PY scripts/b2r_analyze.py --dir "$D" --out "$D/b2r_analysis.json" 2>&1 | tee "$LOGS/analysis_final.txt"
say "B2-r ARC COMPLETE"
ls -la "$D" | grep -E "b2r_"
