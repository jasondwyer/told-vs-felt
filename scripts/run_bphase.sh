#!/usr/bin/env bash
# B-phase arc driver -- one campaign, one characterized backend (LOCK-g v1.1,
# consistency clause). Uncached throughout: the cached path is FORBIDDEN for
# all of Phase B (disposition 2026-08-24).
#
# Order is the protocol's, not a convenience: respawn (i) INTEGRITY and (ii)
# BACKEND both PASS before any experimental forward. box_determinism.py
# always exits 0 -- it characterizes rather than gates -- so its SUMMARY line
# is parsed here and a non-exact repeat stops the arc.
set -uo pipefail

REPO=/workspace/repo/jspace-lab
PY=/workspace/venv/bin/python
LOGS=/workspace/logs/bphase-2026-08-24
STAGES="base sft dpo instruct"

mkdir -p "$LOGS"
cd "$REPO"
# shellcheck disable=SC1091
[ -f /workspace/env.sh ] && . /workspace/env.sh

say() { echo "##### $* ($(date -u +%H:%M:%SZ)) #####"; }
die() { echo "!!!!! ARC STOPPED: $* !!!!!"; date -u; exit 1; }

exec > >(tee -a "$LOGS/arc.txt") 2>&1

say "B-PHASE ARC START"
echo "  host      : $(hostname)"
echo "  gpu       : $(nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader)"
# The box's .git is NOT synced, so its HEAD is stale and would be a false
# provenance stamp. REPO_HEAD is passed in from the laptop, which is the
# commit these instruments actually came from (ledger 27).
echo "  repo head : ${REPO_HEAD:-UNSTAMPED} (stamped from the laptop; box .git is stale by design)"
echo "  python    : $($PY -V 2>&1)"
echo "  cached    : FORBIDDEN for all of Phase B (uncached everywhere)"

# ---------------------------------------------------------------- respawn (i)
say "RESPAWN (i) INTEGRITY"
$PY scripts/box_respawn_check.py 2>&1 | tee "$LOGS/respawn_integrity.txt"
[ "${PIPESTATUS[0]}" -eq 0 ] || die "integrity gate FAILED -- this is an incident; touch nothing, escalate"

# --------------------------------------------------------------- respawn (ii)
say "RESPAWN (ii) BACKEND CHARACTERIZATION"
$PY scripts/box_determinism.py --stage base 2>&1 | tee "$LOGS/respawn_determinism.txt"
[ "${PIPESTATUS[0]}" -eq 0 ] || die "determinism harness errored"
grep -q "repeat-exact(det ON)=True" "$LOGS/respawn_determinism.txt" \
  || die "backend gate FAILED -- deterministic repeat is not exact on this host"
say "BOTH RESPAWN GATES PASS -- experimental forwards licensed on this backend"

# ------------------------------------------------- B2 pre-step: concept vecs
# --out is explicit and load-bearing: box_b2_concepts.py defaults to
# models-root, but box_b2_detection.py reads the vectors from the REPO's
# data/olmo/. Writing them straight to data/olmo/ satisfies both and is where
# ledger 27 needs them anyway. The npz is derived from --out and lands beside.
for s in $STAGES; do
  say "CONCEPT VECTORS | $s"
  $PY scripts/box_b2_concepts.py --stage "$s" \
      --out "$REPO/data/olmo/b2_concepts_${s}.json" 2>&1 \
      | tee "$LOGS/concepts_${s}.txt"
  [ "${PIPESTATUS[0]}" -eq 0 ] || die "concept extraction failed at $s"
done

# ------------------------------------------------------------------------ B2
for s in $STAGES; do
  for arm in fidelity register; do
    say "B2 | $s | $arm"
    $PY scripts/box_b2_detection.py --stage "$s" --arm "$arm" \
        --out "$REPO/data/olmo/b2_${arm}_${s}.json" 2>&1 \
        | tee "$LOGS/b2_${arm}_${s}.txt"
    [ "${PIPESTATUS[0]}" -eq 0 ] || die "B2 failed at $s/$arm"
  done
done

say "B2 ANALYSIS (pre-committed analyzer; no verdict declares itself)"
$PY scripts/b2_analyze.py --dir "$REPO/data/olmo" \
    --out "$REPO/data/olmo/b2_analysis.json" 2>&1 | tee "$LOGS/b2_analysis.txt"

# ------------------------------------------------------------------------ B3
for s in $STAGES; do
  say "B3 SCREEN | $s"
  $PY scripts/box_b3_sessions.py --stage "$s" --tier screen \
      --out "$REPO/data/olmo/b3_screen_${s}.json" 2>&1 \
      | tee "$LOGS/b3_screen_${s}.txt"
  [ "${PIPESTATUS[0]}" -eq 0 ] || die "B3 failed at $s"
  if grep -q "BAR FIRED" "$LOGS/b3_screen_${s}.txt"; then
    echo "!!!!! TRIPWIRE FIRED AT $s -- LOCK-g §4 routes to a design-instance"
    echo "      disposition. Remaining stages NOT run. Code does not"
    echo "      self-adjudicate a fired gate. !!!!!"
    break
  fi
done

say "B3 ANALYSIS (pre-committed analyzer)"
for s in $STAGES; do
  a="$REPO/data/olmo/b3_screen_${s}.json"
  [ -f "$a" ] || continue
  $PY scripts/b3_analyze.py --in "$a" \
      --out "$REPO/data/olmo/b3_analysis_${s}.json" 2>&1 \
      | tee "$LOGS/b3_analysis_${s}.txt"
done

say "B-PHASE ARC COMPLETE"
ls -la "$REPO/data/olmo/" | grep -E "b2_|b3_"
