# n — N-pod VERDICTS: the launch files, their blind review and dispositions, and the stand-in tests (the n-analyzer session)

PI date 2026-11-27. The kit, in the n-analyzer session's scratch at <scratch>/n9/verdicts, read and checked by the coordinating session before it granted the run's window. Its manifest `launch_v2_manifest.sha256`, sha256 `41876a62851dc0c04131d15327e3ece864c4f0f34871e4d83648cfd977d6163a`, lists 13 files: 12 of the parts below, and the review's first extraction, which part 5's heading names by sha256. Each part is the file verbatim, except that the repository's root is printed as <repo> and the scratch folder as <scratch>, and that a file lacking a final newline (the review's report alone) gains one before its closing fence; the sha256 in each heading is the file's own, before those changes.

## 1. The manifest of launch files v2

`launch_v2_manifest.sha256`, sha256 `41876a62851dc0c04131d15327e3ece864c4f0f34871e4d83648cfd977d6163a`, 13 lines in the kit.

````text
cba11176ec4129e96eaf4d42a3b35e59176cb3da29bd4ea6df2db7853945b0de  verdicts_steps_v2.sh
ec8cdd7434cb494a41f06334b7e642fb8365a0d02ff6d732a09bc04033d75f04  inputs_v2.sha256
290539f94b3438e46081f92542b356ce583f42dbd868a6a622c2d92959f817ab  NOTES_v2.md
6b051dbfe3c7ed9179952308f8a9706d415a59d62cdb1de50b7465d2684456bd  review/reviewer/report.md
0e245a88e520a31c03f9c6babde8a3727b7f76c248d9c7eff5454407b1a5584e  review/dispositions_v1.md
f88e1b8cfa216ea7aee341a3f7a690e7ddfddf2e768c99bf333613da640b2676  review/check_v2_final.txt
5ad64c1b457162c957a8d659aa8cb19354b3ae2953d06190d2f2dc22e4f671a5  standin/stand_python_v2.in
5405017b28ca58a1bf5191788475a1af0945e75f969e66b6709fd59b4cf8d39c  standin/standin_test_v2.sh
956b050f3843b2a4a1f58f46f8a137eb8753d4ce9be8eef1905959c8c4e8476c  standin/standin_test_v2.log
2071db4226e361b0de6a8caad1557961b772ba4b099784b05e49dc37d9358811  standin/standin_test_v2_runs4.log
445d65fbf25a62ddf8f2735bc388987949c5aa49898e72408caf6dbfa05cc681  verdicts_steps.sh
50b1ae4fc5cf0d42d5db55d6be8fdbc78c00b7f2fd1b132cfe514fc7d4c7d907  inputs.sha256
a3eef767aa1e9c937702c9a45207917e3af20a15ae2f32a5add6c6d85b7c3680  NOTES.md
````

## 2. The steps file v2, as run

`verdicts_steps_v2.sh`, sha256 `cba11176ec4129e96eaf4d42a3b35e59176cb3da29bd4ea6df2db7853945b0de`, 325 lines in the kit.

````bash
#!/bin/bash
# verdicts_steps_v2.sh -- N-pod's VERDICTS run of record on the laptop: the n-analyzer session's launch file, v2
# (v1 with the blind review's findings as review/dispositions_v1.md gives them). PROPOSAL-n v0.2 s8 step 15; the
# seat's raw of 2026-11-27 (D) s5 item 1; the PI's routing of 2026-11-27, N item 5.
#
# Usage: /bin/bash <this file> check|run|wait|after -- each mode its own call, in this order, inside the window.
# No mode runs Python but run's one launch (the analyzer, through inner); shasum (a Perl script) is used by name;
# the modes write only in this folder (run/, tmp/, raw/), the analyzer alone writes data/n/verdicts.
#   check  the run's preconditions, each asserted: HEAD descends from 7ab1cf6; the ten pinned files (the six inputs
#          and the four package files the schema's import runs) each clean, HEAD's blob, last touched at its commit of
#          record and at its sha256 in inputs_v2.sha256; valence_core/ and scripts/ clean; the campaign's cell folder
#          holding the 138 tracked cells, no file git does not track, none changed since 95cd461 (names only, by
#          count); data/n/verdicts, run/ and tmp/ absent; the venv's bin one folder, physical, holding an executable
#          python (builtins); no process naming the analyzer, none named python; the five thread variables unset;
#          AC power; Low Power Mode off; the venv's versions of record. Prints "check: ALL PASS" or exits 1.
#   run    check again (kept as run/check.txt; refused unless ALL PASS), run/ made atomically, the environment to
#          run/env.txt, then the one launch, nohup caffeinate -is /bin/bash <this file> inner, its PID to run/pid.txt
#          (caffeinate runs the command in its own PID and holds its assertion in a child, so the PID is inner's).
#   inner  run's child, never called by hand: the analyzer (nice 19, -I -B, TMPDIR tmp/, absolute paths, --date
#          the calendar date at launch); then run/secs.txt and, last, run/exit.txt.
#   wait   the end-wait on the PID alone (kill -0 and the PID's own command line every POLL s), then no process
#          naming the run. Launched through the Bash tool's background mode.
#   after  once the PID has ended: the raw built (the root as <repo>; the environment, the check at launch and the
#          launch files' sha256s beside it) and screened; on exit 0 the outputs checked against the VERDICTS line,
#          the pins and the tree; on any other end it stops after the raw, with the exit's meaning and the names in
#          data/n/verdicts.
set -u
export LC_ALL=C
R=<repo>
L=<scratch>/n9/verdicts
SELF=$L/verdicts_steps_v2.sh
PINS=$L/inputs_v2.sha256
W=$L/run
T=$L/tmp
V=$R/data/n/verdicts
CELLS=data/n/ckpt/campaign
NCELLS=138
BASE=7ab1cf6
CLOSE=95cd461
POLL=5
PY_VERSION="version_info = 3.12.9"
NP_DIST="numpy-2.5.1.dist-info"
INPUTS="scripts/n_analyze.py LOCK-n.md valence_core/n/schema.py data/n/gates/G-READ-n.json data/n/gvec/gvec_cosines.json data/n/reports/campaign.json valence_core/__init__.py valence_core/adapters/__init__.py valence_core/adapters/base.py valence_core/n/__init__.py"
BOUND="scripts/n_analyze.py valence_core/n/schema.py LOCK-n.md data/n/reports/campaign.json data/n/gvec/gvec_cosines.json data/n/gates/G-READ-n.json"
RUNPAT='[n]_analyze[.]py|verdicts_steps_v2[.]sh inner'

rev_of() {   # each pinned file's commit of record: the last commit that touched it
  case "$1" in
    scripts/n_analyze.py) echo b6ea27f ;;
    LOCK-n.md) echo 098218c ;;
    valence_core/n/schema.py) echo ef105f1 ;;
    data/n/gates/G-READ-n.json) echo 7ab1cf6 ;;
    data/n/gvec/gvec_cosines.json) echo e3b48ed ;;
    data/n/reports/campaign.json) echo 95cd461 ;;
    valence_core/__init__.py) echo c5b8f1a ;;
    valence_core/adapters/__init__.py) echo 1465b34 ;;
    valence_core/adapters/base.py) echo 7da9509 ;;
    valence_core/n/__init__.py) echo 5a97527 ;;
    *) echo none ;;
  esac
}

say() { printf '%s\n' "$*"; }
abbr() { printf '%s...%s' "$(printf '%s' "$1" | cut -c1-8)" "$(printf '%s' "$1" | cut -c61-64)"; }
pin_of() { sed -n "s|^\([0-9a-f]\{64\}\)  $1\$|\1|p" "$PINS"; }

venv_versions() {   # the venv's version line and numpy's dist-info folder, by builtins and relative names
  local pv nv
  pv=$( set -- "$R"/jl*/.venv; [ $# -eq 1 ] && cd "$1" && /usr/bin/grep -E '^version_info' pyvenv.cfg | head -n 1 | tr -s ' ' )
  nv=$( set -- "$R"/jl*/.venv/lib/python3*/site-packages; [ $# -eq 1 ] && cd "$1" && ls -d numpy-*.dist-info 2>/dev/null )
  say "$pv; $nv"
}

threads_set() {   # the five thread variables that are set, if any
  local v x s=""
  for v in OMP_NUM_THREADS OPENBLAS_NUM_THREADS MKL_NUM_THREADS VECLIB_MAXIMUM_THREADS NUMEXPR_NUM_THREADS; do
    eval "x=\${$v+set}"
    [ -n "$x" ] && s="$s $v"
  done
  say "$s"
}

check() {
  local ok=1 p rev full last st h w o out rc names n m t
  say "check: the calendar date $(date +%F)"
  h=$(git -C "$R" rev-parse HEAD)
  if [ -n "$h" ] && git -C "$R" merge-base --is-ancestor "$BASE" HEAD; then
    say "PASS HEAD $h descends from $(git -C "$R" rev-parse --verify -q "$BASE^{commit}")"
  else
    say "FAIL HEAD does not descend from $BASE"; ok=0
  fi
  for p in $INPUTS; do
    rev=$(rev_of "$p")
    full=$(git -C "$R" rev-parse --verify -q "$rev^{commit}")
    last=$(git -C "$R" log --format=%H -n 1 -- "$p")
    st=$(git -C "$R" status --porcelain -- "$p")
    h=$(git -C "$R" rev-parse --verify -q "HEAD:$p")
    w=$(git -C "$R" hash-object -- "$p" 2>/dev/null)
    o=$(git -C "$R" rev-parse --verify -q "$rev:$p")
    if [ -n "$full" ] && [ "$full" = "$last" ] && [ -z "$st" ] && [ -n "$h" ] && [ "$h" = "$w" ] && [ "$h" = "$o" ]; then
      say "PASS $p: clean, HEAD's blob, last touched at $full"
    else
      say "FAIL $p: not clean, not HEAD's blob, or touched after $rev"; ok=0
    fi
  done
  names=$(cut -c67- "$PINS" | tr '\n' ' ')
  if [ "$names" = "$INPUTS " ]; then
    say "PASS inputs_v2.sha256 names the ten files in order"
  else
    say "FAIL inputs_v2.sha256 does not name the ten files in order"; ok=0
  fi
  out=$(cd "$R" && shasum -a 256 -c "$PINS" 2>&1); rc=$?
  printf '%s\n' "$out" | sed 's/^/  shasum: /'
  n=$(printf '%s\n' "$out" | /usr/bin/grep -c ': OK$')
  if [ "$rc" = 0 ] && [ "$n" = 10 ]; then
    say "PASS the ten sha256s are inputs_v2.sha256's"
  else
    say "FAIL the sha256s: shasum exit $rc, $n of 10 OK"; ok=0
  fi
  n=$(git -C "$R" status --porcelain -- valence_core scripts | wc -l | tr -d ' ')
  if [ "$n" = 0 ]; then say "PASS valence_core/ and scripts/ clean (git status, by count)"; else say "FAIL valence_core/ or scripts/: $n status lines"; ok=0; fi
  t=$(git -C "$R" ls-files -- "$CELLS" | wc -l | tr -d ' ')
  n=$(git -C "$R" status --porcelain --ignored --untracked-files=all -- "$CELLS" | wc -l | tr -d ' ')
  m=$(git -C "$R" diff --name-only "$CLOSE" HEAD -- "$CELLS" | wc -l | tr -d ' ')
  if [ "$t" = "$NCELLS" ] && [ "$n" = 0 ] && [ "$m" = 0 ]; then
    say "PASS the campaign's cell folder: $t tracked, no other file, none changed since $CLOSE (names only, by count)"
  else
    say "FAIL the campaign's cell folder: $t tracked, $n status lines, $m changed since $CLOSE"; ok=0
  fi
  if [ -e "$V" ]; then say "FAIL data/n/verdicts exists"; ok=0; else say "PASS data/n/verdicts absent"; fi
  if [ -e "$W" ] || [ -e "$T" ]; then say "FAIL run/ or tmp/ exists"; ok=0; else say "PASS run/ and tmp/ absent"; fi
  if ( set -- "$R"/jl*/.venv/bin; [ $# -eq 1 ] && cd "$1" && [ "$(pwd -P)" = "$1" ] && [ -x ./python ] ); then
    say "PASS the venv's bin: one match of its glob, a physical path, ./python executable"
  else
    say "FAIL the venv's bin: not one match, not a physical path, or no executable ./python"; ok=0
  fi
  n=$(pgrep -f "$RUNPAT" | wc -l | tr -d ' ')
  m=$(ps -A -o comm= | /usr/bin/grep -c -E '(^|/)[p]ython[0-9.]*$')
  if [ "$n" = 0 ] && [ "$m" = 0 ]; then say "PASS no process names the run, none is named python"; else say "FAIL $n processes name the run, $m are named python"; ok=0; fi
  t=$(threads_set)
  if [ -z "$t" ]; then say "PASS the five thread variables unset"; else say "FAIL thread variables set:$t"; ok=0; fi
  if pmset -g batt | head -n 1 | /usr/bin/grep -q -F "'AC Power'"; then say "PASS AC power"; else say "FAIL not on AC power"; ok=0; fi
  if [ "$(pmset -g | awk '$1 == "powermode" {print $2}')" = 0 ]; then say "PASS Low Power Mode off (powermode 0)"; else say "FAIL Low Power Mode not off"; ok=0; fi
  t=$(venv_versions)
  if [ "$t" = "$PY_VERSION; $NP_DIST" ]; then say "PASS the venv's versions of record: $t"; else say "FAIL the venv's versions: [$t]"; ok=0; fi
  if [ "$ok" = 1 ]; then say "check: ALL PASS"; return 0; fi
  say "check: FAIL"; return 1
}

env_lines() {   # run/env.txt, five lines
  local bi t
  bi=$( set -- "$R"/jl*/.venv/bin; [ $# -eq 1 ] && cd "$1" && t=$(readlink python) && basename "$(dirname "$(dirname "$t")")" )
  t=$(threads_set)
  say "bash $BASH_VERSION; macOS $(sw_vers -productVersion); hw.ncpu $(sysctl -n hw.ncpu)"
  say "venv $(venv_versions); its python links to the base interpreter in a folder named ${bi:-?}"
  say "power $(pmset -g batt | head -n 1 | sed "s/^Now drawing from //; s/'//g"); powermode $(pmset -g | awk '$1 == "powermode" {print $2}')"
  say "$(pmset -g stats | tr '\n' ' ' | sed 's/ *$//')"
  if [ -z "$t" ]; then say "the five thread variables unset"; else say "thread variables set:$t"; fi
}

run() {
  local out d h pid
  out=$(check)
  if ! printf '%s\n' "$out" | /usr/bin/grep -q -x 'check: ALL PASS'; then
    printf '%s\n' "$out"; say "REFUSED: check did not pass; nothing launched"; return 1
  fi
  mkdir "$W" 2>/dev/null || { say "REFUSED: run/ exists: one run"; return 1; }
  mkdir "$T" || { say "REFUSED: tmp/ was not made"; return 1; }
  printf '%s\n' "$out" > "$W/check.txt"
  d=$(date +%F)
  h=$(git -C "$R" rev-parse HEAD)
  printf '%s\n' "$d" > "$W/date.txt"
  printf '%s\n' "$h" > "$W/head.txt"
  env_lines > "$W/env.txt"
  nohup caffeinate -is /bin/bash "$SELF" inner > /dev/null 2>&1 < /dev/null &
  pid=$!
  disown
  printf '%s\n' "$pid" > "$W/pid.txt"
  if kill -0 "$pid" 2>/dev/null; then
    say "run: launched under nohup caffeinate -is, PID $pid; the PI date $d; HEAD $h"
  else
    say "run: the PID $pid had already ended at launch; wait, then after"
  fi
  return 0
}

inner() {
  local d t0 t1 rc
  if [ ! -f "$W/date.txt" ] || [ -e "$W/out.txt" ]; then say "inner: not from run"; return 1; fi
  d=$(cat "$W/date.txt")
  t0=$(date +%s)
  ( set -- "$R"/jl*/.venv/bin; { [ $# -eq 1 ] && [ -d "$1" ]; } || exit 97; cd "$1" || exit 98
    TMPDIR="$T" nice -n 19 ./python -I -B "$R/scripts/n_analyze.py" verdicts \
      --campaign "$R/$CELLS" --report "$R/data/n/reports/campaign.json" \
      --lock "$R/LOCK-n.md" --gread "$R/data/n/gates/G-READ-n.json" \
      --gvec "$R/data/n/gvec/gvec_cosines.json" --date "$d" ) > "$W/out.txt" 2> "$W/err.txt"
  rc=$?
  t1=$(date +%s)
  printf '%s\n' "$((t1 - t0))" > "$W/secs.txt"
  printf '%s\n' "$rc" > "$W/exit.txt"
}

waitpid() {
  local pid c n
  pid=$(cat "$W/pid.txt" 2>/dev/null)
  [ -n "$pid" ] || { say "wait: no PID in run/pid.txt"; return 1; }
  while kill -0 "$pid" 2>/dev/null; do
    c=$(ps -o command= -p "$pid" 2>/dev/null)
    case "$c" in
      *"verdicts_steps_v2.sh inner"*|"") ;;
      *) say "wait: the PID $pid no longer names the run; stopping the wait"; return 1 ;;
    esac
    sleep "$POLL"
  done
  n=$(pgrep -f "$RUNPAT" | wc -l | tr -d ' ')
  c=0
  while [ "$n" != 0 ] && [ "$c" -lt 10 ]; do   # caffeinate's assertion holder ends just after its parent
    sleep 1; c=$((c + 1)); n=$(pgrep -f "$RUNPAT" | wc -l | tr -d ' ')
  done
  say "wait: the PID $pid has ended; processes naming the run: $n"
  [ "$n" = 0 ]
}

meaning() {
  case "$1" in
    none) say "no exit status: the run was interrupted before the analyzer returned; outputs may stand partial" ;;
    1) say "exit 1: an error the analyzer did not catch (its traceback in stderr); outputs may stand partial" ;;
    2) say "exit 2: a refusal (the analyzer writes nothing when it refuses) or a usage error" ;;
    4) say "exit 4: a STOP (any of the analyzer's STOPs; nothing written): for the seat through the PI" ;;
    97) say "exit 97: the venv's glob matched no folder, or more than one; nothing ran" ;;
    98) say "exit 98: cd into the venv's bin failed; nothing ran" ;;
    126|127) say "exit $1: ./python not executable or not found; nothing ran" ;;
    *) if [ "$1" -gt 128 ] 2>/dev/null; then say "exit $1: killed by signal $(($1 - 128)); outputs may stand partial"; else say "exit $1: not an exit this file expects"; fi ;;
  esac
}

after() {
  local pid n rc d h secs a s1 s2 raw ok=1 c names l1 l2 inv il ml sv ss gv gs p x st
  pid=$(cat "$W/pid.txt" 2>/dev/null)
  if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then say "REFUSED: the PID $pid is alive: the end-wait first"; return 1; fi
  n=$(pgrep -f "$RUNPAT" | wc -l | tr -d ' ')
  if [ "$n" != 0 ]; then say "REFUSED: $n processes name the run"; return 1; fi
  for p in date.txt head.txt env.txt check.txt; do [ -f "$W/$p" ] || { say "FAIL run/$p missing"; return 1; }; done
  if [ -f "$W/exit.txt" ]; then rc=$(cat "$W/exit.txt"); else rc=none; fi
  secs=$(cat "$W/secs.txt" 2>/dev/null); secs=${secs:-?}
  d=$(cat "$W/date.txt"); h=$(cat "$W/head.txt")
  a=$(shasum -a 256 "$R/scripts/n_analyze.py" | cut -d' ' -f1)
  s1=$(shasum -a 256 "$SELF" | cut -d' ' -f1)
  s2=$(shasum -a 256 "$PINS" | cut -d' ' -f1)
  mkdir -p "$L/raw"
  raw=$L/raw/${d}_n-verdicts_out.txt
  if [ -e "$raw" ]; then say "REFUSED: raw/$(basename "$raw") exists"; return 1; fi
  {
    say "# n package, N-pod's VERDICTS run of record (PROPOSAL-n v0.2 §8 step 15; the seat's raw of 2026-11-27 §5 item 1; the PI's routing of 2026-11-27, N item 5) on v7 (b6ea27f): scripts/n_analyze.py verdicts --campaign $CELLS --report data/n/reports/campaign.json --lock LOCK-n.md --gread data/n/gates/G-READ-n.json --gvec data/n/gvec/gvec_cosines.json --date $d; the analyzer's sha256 $a (measured after the run); HEAD $h; nice 19, -I -B, one invocation, under nohup caffeinate -is; exit $rc; stderr $(cat "$W/err.txt" 2>/dev/null | wc -c | tr -d ' ') bytes; $secs s; the launch files verdicts_steps_v2.sh $s1 and inputs_v2.sha256 $s2. The repository's root is printed as <repo>."
    say "# environment at launch: $(tr '\n' '|' < "$W/env.txt" | sed 's/|$//; s/|/ | /g')"
    sed 's/^/# check at launch: /' "$W/check.txt"
    [ "$rc" = none ] && say "# no exit status: the run was interrupted"
    [ -f "$W/out.txt" ] && sed -e "s|$L|<launch>|g" -e "s|$R|<repo>|g" "$W/out.txt"
    if [ -s "$W/err.txt" ]; then say "# stderr:"; sed -e "s|$L|<launch>|g" -e "s|$R|<repo>|g" "$W/err.txt"; fi
  } > "$raw"
  say "after: raw/$(basename "$raw"): $(wc -l < "$raw" | tr -d ' ') lines, sha256 $(abbr "$(shasum -a 256 "$raw" | cut -d' ' -f1)")"
  c=$(/usr/bin/grep -c -F -- "$HOME" "$raw")
  if [ "$c" = 0 ]; then say "PASS the home-prefix count over the raw is 0"; else say "FAIL the home-prefix count over the raw is $c"; ok=0; fi
  c=$(/usr/bin/grep -c -F -e /private/ -e /tmp/ "$raw")
  if [ "$c" = 0 ]; then say "PASS no scratch or temporary path in the raw"; else say "FAIL $c raw lines name a scratch or temporary path"; ok=0; fi
  il=$(/usr/bin/grep -n '^INVOCATION: ' "$raw" | cut -d: -f1 | tr '\n' ' ')
  ml=$(/usr/bin/grep -n -i -e '[j]lens' -e '[q]wen' -e '[m]lx' -e '[o]lmo' -e '[i]pykernel' "$raw" | cut -d: -f1 | tr '\n' ' ')
  say "screen: raw lines with a guard marker (bracketed patterns): [$ml]; the INVOCATION line: [$il]"
  if [ "$rc" != 0 ]; then
    meaning "$rc"
    say "data/n/verdicts holds: [$(cd "$V" 2>/dev/null && ls -A | tr '\n' ' ')]"
    say "after: STOPPED at the raw; nothing is retried; to the coordinating session"
    return 1
  fi
  if [ -n "$il" ] && [ "$ml" = "$il" ]; then say "PASS the guard markers stand on the INVOCATION line alone (its venv folder)"; else say "FAIL the guard markers stand off the INVOCATION line, or it is missing"; ok=0; fi
  if [ -s "$W/err.txt" ]; then say "FAIL stderr is not empty"; ok=0; else say "PASS stderr empty"; fi
  n=$(wc -l < "$W/out.txt" | tr -d ' ')
  l1=$(sed -n 1p "$W/out.txt"); l2=$(sed -n 2p "$W/out.txt")
  if [ "$n" = 2 ]; then say "PASS stdout is two lines"; else say "FAIL stdout is $n lines, not 2"; ok=0; fi
  case "$l1" in "INVOCATION: "*) say "PASS line 1 is the INVOCATION line" ;; *) say "FAIL line 1 is not the INVOCATION line"; ok=0 ;; esac
  case "$l2" in "VERDICTS: ("*" -> "*) say "PASS line 2 is the VERDICTS line" ;; *) say "FAIL line 2 is not the VERDICTS line"; ok=0 ;; esac
  c=$(/usr/bin/grep '^INVOCATION: ' "$raw" | /usr/bin/grep -o -F -- '<repo>' | wc -l | tr -d ' ')
  if [ "$c" = 7 ]; then say "PASS the raw's INVOCATION line prints <repo> 7 times (the interpreter and six paths)"; else say "FAIL the raw's INVOCATION line prints <repo> $c times, not 7"; ok=0; fi
  names=$(cd "$V" 2>/dev/null && ls -A | tr '\n' ' ')
  if [ "$names" = "N-pod_VERDICTS.json N-pod_secondary.json " ]; then say "PASS data/n/verdicts holds the two outputs alone"; else say "FAIL data/n/verdicts holds [$names]"; ok=0; fi
  sv=$(printf '%s\n' "$l2" | sed -n 's/.*N-pod_VERDICTS\.json (written; sha256 \([0-9a-f]\{64\}\)).*/\1/p')
  ss=$(printf '%s\n' "$l2" | sed -n 's/.*N-pod_secondary\.json (written; sha256 \([0-9a-f]\{64\}\)).*/\1/p')
  gv=$(cd "$V" 2>/dev/null && shasum -a 256 N-pod_VERDICTS.json | cut -d' ' -f1)
  gs=$(cd "$V" 2>/dev/null && shasum -a 256 N-pod_secondary.json | cut -d' ' -f1)
  if [ -n "$sv" ] && [ -n "$gv" ] && [ "$sv" = "$gv" ]; then say "PASS N-pod_VERDICTS.json written, sha256 $(abbr "$gv") as printed"; else say "FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one"; ok=0; fi
  if [ -n "$ss" ] && [ -n "$gs" ] && [ "$ss" = "$gs" ]; then say "PASS N-pod_secondary.json written, sha256 $(abbr "$gs") as printed"; else say "FAIL N-pod_secondary.json: not written, or its sha256 is not the printed one"; ok=0; fi
  for p in $BOUND; do
    x=$(pin_of "$p")
    c=$( [ -n "$x" ] && cd "$V" 2>/dev/null && /usr/bin/grep -c -F -- "$x" N-pod_VERDICTS.json )
    if [ -n "$x" ] && [ "${c:-0}" -ge 1 ] 2>/dev/null; then say "PASS N-pod_VERDICTS.json binds $p's sha256 $(abbr "$x")"; else say "FAIL N-pod_VERDICTS.json does not bind $p's sha256"; ok=0; fi
  done
  c=$( [ -n "$gs" ] && cd "$V" 2>/dev/null && /usr/bin/grep -c -F -- "$gs" N-pod_VERDICTS.json )
  if [ -n "$gs" ] && [ "${c:-0}" -ge 1 ] 2>/dev/null; then say "PASS N-pod_VERDICTS.json binds the secondary's sha256"; else say "FAIL N-pod_VERDICTS.json does not bind the secondary's sha256"; ok=0; fi
  for p in N-pod_VERDICTS.json N-pod_secondary.json; do
    c=$(cd "$V" 2>/dev/null && /usr/bin/grep -c -F -e "$HOME" -e /private/ -e /tmp/ "$p")
    if [ "$c" = 0 ]; then say "PASS $p names no local root"; else say "FAIL $p: ${c:-?} lines name a local root"; ok=0; fi
  done
  x=$(cd "$R" && shasum -a 256 -c "$PINS" 2>&1 | /usr/bin/grep -c ': OK$')
  if [ "$x" = 10 ]; then say "PASS the ten pinned files still at their sha256s"; else say "FAIL $x of 10 pinned files at their sha256s"; ok=0; fi
  x=$(git -C "$R" rev-parse HEAD)
  if [ -n "$x" ] && [ "$x" = "$h" ]; then say "PASS HEAD unchanged since launch"; else say "FAIL HEAD moved during the run"; ok=0; fi
  n=$(git -C "$R" status --porcelain -- valence_core scripts | wc -l | tr -d ' ')
  if [ "$n" = 0 ]; then say "PASS valence_core/ and scripts/ still clean (by count)"; else say "FAIL valence_core/ or scripts/: $n status lines"; ok=0; fi
  n=$(ls -A "$T" 2>/dev/null | wc -l | tr -d ' ')
  if [ -d "$T" ] && [ "$n" = 0 ]; then say "PASS tmp/ empty"; else say "FAIL tmp/ holds $n names, or is missing"; ok=0; fi
  st=$(pmset -g stats | tr '\n' ' ' | sed 's/ *$//')
  if [ "$st" = "$(sed -n 4p "$W/env.txt")" ]; then say "note: the sleep and wake counts unchanged during the run"; else say "note: the sleep and wake counts changed during the run: [$st]"; fi
  say "outcome: $(printf '%s\n' "$l2" | sed 's/ -> .*//')"
  if [ "$ok" = 1 ]; then say "after: ALL PASS"; return 0; fi
  say "after: FAIL"; return 1
}

case "${1:-}" in
  check) check ;;
  run) run ;;
  inner) inner ;;
  wait) waitpid ;;
  after) after ;;
  *) say "usage: /bin/bash verdicts_steps_v2.sh check, run, wait or after"; exit 2 ;;
esac
````

## 3. The pins file v2

`inputs_v2.sha256`, sha256 `ec8cdd7434cb494a41f06334b7e642fb8365a0d02ff6d732a09bc04033d75f04`, 10 lines in the kit.

````text
735da934272048a795203e8fdef9bfa5a4bde2ba38cdf9ba79d81f313788a7a8  scripts/n_analyze.py
59e0b1bcb364af06630753ba09fde127518c451e0aa679cea1d979d0ec9900aa  LOCK-n.md
1cab28df54c4c2c699b005fc6d2a99693d569911e292ad9dbdb8b6994db8edff  valence_core/n/schema.py
378f9972e942deb61ee4da74887e11556b625cdf41adfcfa4195636ccd31f519  data/n/gates/G-READ-n.json
fc8877be53194408cdcf7bbb09d1ec9ff3dfbe13b575bf6674190e3c03db0dad  data/n/gvec/gvec_cosines.json
1cabeadf9ee94d411d106a9cc306b29615d34bf41e0818f97bd1ed68dfc1c4e3  data/n/reports/campaign.json
620ad380f023dc8c173ee4e164a160c0b1da2a0c0b99fb6c9717be0b8c78b604  valence_core/__init__.py
96d6b48dd41710de8c70ce7d5b28854db4810af6693ff8a96f320f773cafed6a  valence_core/adapters/__init__.py
626fbddd8dd970717e929b5bcd87be4e0c83ca8cb889b8451fcb49e2cb091cbf  valence_core/adapters/base.py
427f58ccf531d2d98bd76004e2ff8b2ece9514248328e12844156a659e711cfd  valence_core/n/__init__.py
````

## 4. The notes v2, for the coordinating session

`NOTES_v2.md`, sha256 `290539f94b3438e46081f92542b356ce583f42dbd868a6a622c2d92959f817ab`, 156 lines in the kit.

````markdown
# N-pod VERDICTS: launch files v2 (the n-analyzer session), for the coordinating session's read

**Routing.** The PI's routing of 2026-11-27, section N item 5 [go] ("Route as given"), on the seat's raw (D)
`results/raw/2026-11-27_n-gread-record-read_design-to-code_answers.md` (sha256 6b5be7a3…e420, 81 lines; §5 item 1):
the n-analyzer session runs `scripts/n_analyze.py verdicts … --gread data/n/gates/G-READ-n.json` on the committed
artifact (378f9972…f519) with the analyzer at v7 (735da934…a7a8), then "— secondary DVs", issuing no claim. A STOP
comes to the seat through the PI; Code adjudicates nothing.

**This folder** (my scratch; its path is in the message that carries these notes):
- `verdicts_steps_v2.sh`, the steps;
- `inputs_v2.sha256`, the ten pins;
- `standin/`, the stand-in tests and their logs;
- `review/`: the blind review of v1 (`reviewer/report.md`), its frozen inputs and `dispositions_v1.md`;
- this file.

The v1 files (`verdicts_steps.sh`, `inputs.sha256`, `NOTES.md`) stay as they were and are superseded. Their sha256s
are in the message.

## The run, exactly (`inner`, launched by `run`)

```
nohup caffeinate -is /bin/bash <this folder>/verdicts_steps_v2.sh inner > /dev/null 2>&1 < /dev/null &   # PID to run/pid.txt
# (caffeinate runs the command in its own PID and holds its assertion in a child: the PID is the inner bash's)
  ( set -- <repo>/jl*/.venv/bin; { [ $# -eq 1 ] && [ -d "$1" ]; } || exit 97; cd "$1" || exit 98
    TMPDIR=<this folder>/tmp nice -n 19 ./python -I -B <repo>/scripts/n_analyze.py verdicts \
      --campaign <repo>/data/n/ckpt/campaign --report <repo>/data/n/reports/campaign.json \
      --lock <repo>/LOCK-n.md --gread <repo>/data/n/gates/G-READ-n.json \
      --gvec <repo>/data/n/gvec/gvec_cosines.json --date <run/date.txt> ) > run/out.txt 2> run/err.txt
  then run/secs.txt, and run/exit.txt last
```

- `--campaign`: the 138 committed cell JSONs (95cd461), which the analyzer alone reads (list v2 item 2). The arrays
  stay outside the repository, and their absence is no refusal (PIN-n-31; n_analyze.py:3166–3167).
- `--report`: `data/n/reports/campaign.json`, COMPLETE (1cabeadf…c4e3; the close list's first line).
- `--lock`: `LOCK-n.md`, v1.0 of record (59e0b1bc…00aa; the identity's lock_sha256, which scripts/n_sessions.py pins).
- `--gread`: `data/n/gates/G-READ-n.json`, the committed artifact (378f9972…f519; RESULTS.md carries it whole). These are
  item 5's words.
- `--gvec`: `data/n/gvec/gvec_cosines.json` (fc8877be…0dad). LOCK-n.md L:711 and L:716–718 name it "the analyzer's
  `--gvec` file". Raw (D) §5 item 1's "the cosines" are VERDICTS' `cosines` (n_analyze.py:6747), which are null without
  it.
- `--date`: "the PI date of the run" (n_analyze.py:6804), the laptop's calendar date when `run` starts (`date +%F`).
- No `--out`: the run is of record, into `data/n/verdicts` (n_analyze.py:6633–6645). `verdicts_precheck` refuses unless
  the analyzer, the lock, the report, the artifact and the cosines file are each committed and clean at HEAD
  (committed_problems, n_analyze.py:5892–5906).
- Absolute paths, since the interpreter's cwd is the venv's bin.

## The window, in order, each its own call

1. `/bin/bash <this folder>/verdicts_steps_v2.sh check`. No Python; it must print `check: ALL PASS`, or nothing runs and
   I report to you. What it asserts is in the file's header, among it every condition the reviewer's F1, F2, F4 and F6
   asked for.
2. `/bin/bash <this folder>/verdicts_steps_v2.sh run`. It runs `check` again and refuses unless ALL PASS. It makes run/
   atomically, writes run/check.txt, run/env.txt, run/date.txt and run/head.txt, then makes the one launch, and returns
   at once with the PID.
3. `/bin/bash <this folder>/verdicts_steps_v2.sh wait`, as the Bash tool's background task: the end-wait on the PID
   alone (`kill -0` and the PID's own command line every 5 s), then no process naming the run (list v2 item 5). Nothing
   else reads run/ or `data/n/verdicts` until it ends, and nothing else runs meanwhile. My expectation is minutes, not
   hours: the run is model-free, reads the cells' JSONs, and has B_BOOT 4,000. That is an expectation, not a
   measurement.
4. `/bin/bash <this folder>/verdicts_steps_v2.sh after`. It refuses while the PID lives. It builds the raw and screens
   it; on exit 0 it must print `after: ALL PASS` and the outcome tuple.

**Exits.**
- 0: `after`, then my report to you (the outcome tuple and the two outputs' sha256s).
- 2: a refusal (the analyzer writes nothing when it refuses) or a usage error: to you; nothing retried.
- 4: any STOP (`AnlStop`; nothing written, since both outputs are formed before either is written,
  n_analyze.py:6751 and :6772): for the seat through the PI. A report in PAUSE would refuse with exit 2; it cannot
  arise here, because the report is COMPLETE.
- 1 (an uncaught error, with its traceback in stderr), no exit status (interrupted), or a signal: outputs may stand
  partial. `after` prints the names in `data/n/verdicts` and stops: to you.
- 97, 98, 126 or 127: nothing ran: to you.

**What prints.** Two stdout lines:
- `INVOCATION:`, sys.executable and argv;
- `VERDICTS:`, the five-member tuple, the outputs' names, how each was written, and their sha256s. There is no margin
  (n §4 "Blinding").

stderr is empty. The INVOCATION line's interpreter path holds the venv folder's name, two guard markers in output
(never in an argv). `after` asserts that they stand on that line alone. The raw prints the root as `<repo>` and this
folder as `<launch>`, in stdout and stderr alike, and keeps the rest of that line as it is, as G-ANL-n's out raw does
at 1641948. The raw's header carries the environment, the
check at launch, the analyzer's sha256 measured after the run, and both launch files' sha256s.

**What my commands touch** (list v2).
- `data/*/ckpt`: no content, and no size or time. The names forms of item 1 are used over the campaign's cell folder,
  printed by count only: `git ls-files`, `git status --porcelain --ignored --untracked-files=all`, and
  `git diff --name-only 95cd461 HEAD`. This is F1's fix, put to you: strike it if those forms over a ckpt folder are
  not item 1's. The analyzer alone reads the cells.
- `data/n/reports/campaign.json`: `git status --porcelain` on its path, its blob ids, its last commit and its sha256
  (item 1's ids and digests); nothing printed from it.
- `data/n/verdicts`: a test that it is absent (`check`). After the run: a name-only `ls -A`, `shasum` of the two
  outputs, and counts of the pins and of local roots in them (`after`).
- The venv folder: entered only by the builtin `cd` through its glob, so no exec's argv names it. Its version line is
  read from `pyvenv.cfg`, numpy's from its dist-info folder's name, and its base interpreter's folder name from
  `readlink` of its python, with no interpreter.
- Processes: `pgrep -f` with bracketed patterns, and `ps -A -o comm=` counted against a bracketed pattern.
- Power: `pmset -g batt`, `pmset -g` and `pmset -g stats`.

Every screen pattern naming a guard marker is bracketed.

## Done already, before any window (my next entry's sweep carries the commands)

All of it was read-only toward the repository, with no Python.
- v1's `bash -n` and its `check` on the real tree (ALL PASS at 7ab1cf6).
- v1's stand-in tests: `runs/` (v1 before its `abbr` fix) and `runs2/` (v1 as frozen for the review).
- The blind review of v1, and its dispositions.
- v2's `/bin/bash -n`, and its `check` on the real tree: 2026-11-27, ALL PASS at 7ab1cf6, every line PASS. That
  includes the campaign folder (138 tracked, no other file, none changed since 95cd461), no process naming the run and
  none named python, AC power, powermode 0, the five thread variables unset, version_info 3.12.9 and numpy-2.5.1.
- v2's stand-in tests, `runs3/` (below).

**v2's stand-in tests** (`standin/stand_python_v2.in`, `standin/standin_test_v2.sh`). Each of 19 variants gets its own
fake root:
- a git repository holding stand-in bytes at the ten pinned paths (one commit);
- a fake venv whose `python` is a bash script that prints what v7's `verdicts` prints;
- a copy of the steps in which three lines differ: R=, L=, and `run`'s check call, stubbed to ALL PASS because
  `check` cannot pass on a fake root. The log prints the diff.

Each variant runs `run`, `wait` and `after`, nohup caffeinate included.
- **runs3** (`standin/standin_test_v2.log`) found two defects in v2 and a wrong stand-in. All were fixed before this
  send (the dispositions' last section).
- **runs4** (`standin/standin_test_v2_runs4.log`), on the final bytes:
  - `ok`: ALL PASS, every line of `after` PASS. The stand-in saw argv -I -B, nice 19, and TMPDIR in tmp/.
  - STOPPED, each with its meaning and the names in `data/n/verdicts`: `refuse`, `stop` and `stderrroot` at exits 2, 4
    and 2; `uncaught` at 1; `interrupted` at "no exit status"; `noglob` at 97. For `uncaught` and `interrupted` the
    secondary stands alone.
  - FAIL on its own line alone: `extra`, `badsha`, `strayfile`, `homeout`, `homeraw`, `scratchraw`, `repocount`,
    `markeroff`, `pinmissing`, `tmpleft` and `errnonempty`. `identical` fails on the two lines its one condition reaches
    (the word "written", for both outputs).
  - The scrub held in stderr: `<repo>/x; launch <launch>/y`, and a traceback's `<repo>/scripts/n_analyze.py`.
  - On `ok`, a second `run` and a second `after` both refuse.
  - `check` on a fake root FAILs (14 lines) with exit 1.
  - No process named a run at the end.
- **Not tested:** an isolated FAIL fixture for each of `check`'s assertions; exits 98, 126 and 127.

## After the run (each later, none now)

- The entry "PROPOSAL-n N-pod — VERDICTS" (n:161). It carries what raw (D) §5 item 1 lists:
  - §5's sentences, G-LEAK-n's ceilings and the G-READ-n table (n_analyze.py:987–1000);
  - the counters, the exposure counts realised and the cosines;
  - raw (D) §2 items 3 and 6, which §5 item 4 gives this session: the label (an N1 NOT-REPLICATED under G-READ-n's
    FAIL at +1 is "concluded, not answered"; REPLICATED and PARTIAL change no sentence), and the dated note in §2
    item 6's figures where N1's label is "concluded, not answered" (the PI's item 4). Ledger (91) is the seat's own
    record, not the entry's (your correction of 2026-11-27);
  - the review's observation on n_analyze.py:5893–5894, as a dated note.

  Then "PROPOSAL-n N-pod — secondary DVs", issuing no claim. A blind values-check follows. The departures are those
  since my last entry's last sweep, which starts at transcript call 3546.
- One commit in its own window, by path:
  - `.gitignore`, admitting `data/n/verdicts/` and its two outputs, in n's block after `data/n/gates/`;
  - the two outputs;
  - `results/raw/<date>_n-verdicts_out.txt`, `results/raw/<date>_n-verdicts-launch_review.md` (the review, its
    dispositions and the stand-in logs) and `results/raw/<date>_n-verdicts_valuescheck.md`;
  - `RESULTS.md`, with the entries at the Log's head.

  Not pushed: the push is the PI's word.
````

## 5. The blind review of v1, verbatim (the reviewer's hand-back, extracted with its UTF-8 decoded once; the kit's first extraction, review/reviewer/report.md, sha256 6b051dbfe3c7ed9179952308f8a9706d415a59d62cdb1de50b7465d2684456bd, is the same text with every non-ASCII character encoded twice)

`review/reviewer/report_v2.md`, sha256 `b7cfd296ac82bb0309d600fa71505eb163e6e7d6a9b137b2d3d70eff01e10521`, 278 lines in the kit.

````markdown
I could not write the report file. The file tool refuses report files from a subagent ("Subagents should return findings as text, not write report files"), so there is no report path or sha256 to give. The full report follows; I did not get around the refusal through the shell. My `mkdir -p` left one empty folder, `<scratch>/n9/verdicts/review/reviewer`. Nothing else was written anywhere.

**Findings by class: 0 BUG, 6 RISK, 12 NIT** (18 in all), plus one uncounted observation about the analyzer itself.

---

# Blind review: N-pod VERDICTS launch files v1

**Path forms.** The report writes no absolute path, so neither the home prefix nor the scratch root is in it if it is committed.
- `<repo>`: the repository root (the steps' `R`).
- `<L>`: the live launch folder (the steps' `L`).
- `<F>`: `<L>/review/frozen`.
- `<raw D>`: `results/raw/2026-11-27_n-gread-record-read_design-to-code_answers.md`.
- `<close list>`: `results/raw/2026-11-25_n-campaign_close-names.txt`.
- `anl:` means `scripts/n_analyze.py` at HEAD; `R:` means `RESULTS.md` at HEAD.
- Bare line numbers are the frozen files' lines.

**Not read by me:**
- anything under `data/*/ckpt`, `data/*/reports` or `data/mf3`;
- the stage report, and the close list's content;
- any raw other than `<raw D>` lines 56–62;
- the venv folder (not named, listed or globbed).

I ran no Python, no mode of the steps and no stand-in test.

## 1. The six frozen files

All six computed sha256s are equal to the brief's values; I compared them in the shell.

| file | sha256 (computed) | equal |
|---|---|---|
| verdicts_steps.sh | 445d65fbf25a62ddf8f2735bc388987949c5aa49898e72408caf6dbfa05cc681 | yes |
| inputs.sha256 | 50b1ae4fc5cf0d42d5db55d6be8fdbc78c00b7f2fd1b132cfe514fc7d4c7d907 | yes |
| NOTES.md | a3eef767aa1e9c937702c9a45207917e3af20a15ae2f32a5add6c6d85b7c3680 | yes |
| standin/stand_python.in | 1ba048686df76e84e56af1f4c26f8244fbb9da2ad5f7a6fbe4b9b217e58bfaec | yes |
| standin/standin_test.sh | 491cec3a7aaa1e1cd623c08226a2ec728568e16c66d763363cec773eb9cbb3d2 | yes |
| standin/standin_test_runs2.log | 3236c0fc95f6ef4ddf81bf72abfa12e025482f61ef73482d51573c87b475c2a6 | yes |

Also established, by ids, digests and names only:
- **Live copies.** The copies under `<L>` equal the frozen ones, 6 of 6.
- **Stand-in copies.** For all 10 variants, the `steps.sh` and the stand-in `python` under `<L>/standin/runs2/` equal the frozen files with only the harness's substitutions. So the log is a run of the frozen files.
- **HEAD and the analyzer.** HEAD is `7ab1cf6`. The analyzer is tracked and clean, sha256 `735da934...a7a8`.
- **The five inputs I may touch** (all but the report):
  - each one's blob is the same at HEAD, in the working tree and at its commit of record;
  - each commit of record is the last commit that touched the file;
  - each sha256 is the pinned one.
- **Output folder.** `data/n/verdicts` is absent.
- **The lock.** LOCK-n.md has one `lock: LOCK-n v1.0` line, one route line (1239, Route B), one gate line (1330, "48 of 48, PASS") and the analyzer's sha256 in backticks (213, 913). So `lock_route`, `lock_gate` and `lock_names` pass (anl:6243–6282, 6692).
- **The cosines file.** `gvec_cosines.json` holds exactly `cosines` and the six pairs that `_load_gvec` requires (anl:6607–6622). LOCK-n.md:717–718 calls it the analyzer's `--gvec` file. `gvec.json` would be refused, so the right file is passed.
- **Syntax.** `bash -n` passes for all three bash files under /bin/bash 3.2.57.

**Main question.** `run` invokes `verdicts` as routed:
- with `--campaign`, `--report`, `--lock`, `--gread`, `--gvec` and `--date`;
- with every path absolute and inside the repository, and no `--out`.

`verdicts_precheck` (anl:6625–6650) and `run_verdicts` (anl:6653–6775) accept this form. The INVOCATION and VERDICTS lines that `after` parses are in v7's forms (anl:6787, 6782, 6839).

I found no BUG.

## 2. Findings

### F1 [RISK] verdicts_steps.sh:25, 50–61 — `check` never looks at the campaign folder

**Defect.** `data/n/ckpt/campaign` is the one input the analyzer reads that nothing pins or checks. The analyzer refuses on:
- any file that is neither a `.json` cell nor a capture array that a cell names (anl:3172–3203);
- any `.json` that fails `check_cell` (anl:3176–3182);
- any set of `.json` files that is not exactly the report's and the artifact's cells, compared by sha256 (anl:6377–6380, 6469–6472).

`.gitignore` ignores `.DS_Store` (176) and everything in the folder except `N*.json` (366–368). Such a stray file is therefore invisible to a plain `git status --porcelain`.

No run has yet read the repository's copy of this folder. G-READ-n read the staging copy, outside the repository (R:59–61).

**Scenario.** A Finder visit leaves `.DS_Store`, or a copy leaves an AppleDouble `._N1-V__none__0.json`. The run exits 2 with nothing written. Because `run/` now exists, the window's one run is spent, and a v2 needs a new window.

**Fix**, by names and ids only (item 1). In `check`, assert empty output from both:
- `git -C "$R" status --porcelain --ignored --untracked-files=all -- data/n/ckpt/campaign` (the form G-READ-n's `after` used on `data/n/gates`, R:68–69);
- `git -C "$R" diff --name-only 95cd461 HEAD -- data/n/ckpt/campaign`.

If the capture arrays may be in the folder, compare the ignored names with the close list's names instead of expecting none. Whether listing names inside a ckpt folder falls within item 1 is the coordinating session's call; if it does not, declare the risk.

### F2 [RISK] verdicts_steps.sh:25, 50–61 and 115–176 — the import closure beyond the two pinned files is unchecked and unrecorded

**Defect.** `schema_module` (anl:3068–3079) imports `valence_core.n.schema`. That executes four repository files:
- `valence_core/__init__.py`;
- `valence_core/adapters/__init__.py`;
- `valence_core/adapters/base.py`;
- `valence_core/n/__init__.py`.

The analyzer checks only the schema's bytes and its own committed state (anl:3072–3074, 6634–6641). The outputs record only the analyzer's and the schema's sha256s (anl:6696–6698). Today all four files are tracked and at HEAD's bytes.

**Scenario.** A parallel session in the shared tree has an uncommitted edit to `adapters/base.py` during the window. The run executes it, and both `check` and `after` pass. Neither the outputs nor the raw can show it afterwards.

**Fix.**
- Add the four files to `check`'s blob assertions, or assert `git status --porcelain -- valence_core scripts` is empty. G-READ-n's check did the latter (R:51–52).
- Repeat the same check inside `run` just before launch (see F5), and again in `after`.

### F3 [RISK] verdicts_steps.sh:102–112, 117–119 — an interrupted run leaves no raw and no path to one

**Defect.** `exit.txt` and `secs.txt` are written only after the subshell returns (109–110). If the steps' bash is killed (task stopped, app or session ends):
- `after` returns at 118 before building any raw;
- `run` refuses a second run (94).

The outputs can also be partial:
- `write_all_once` links the secondary output before the VERDICTS output (anl:6772, 4649). A kill between the two leaves the secondary alone.
- A kill inside `write_once` also leaves `.N-pod_VERDICTS.json.<pid>.tmp` behind (anl:4629–4637).
- If only the bash dies, the interpreter runs on as an orphan. It writes both outputs, and the VERDICTS line goes into `out.txt` after the end has already been reported (see F4).

**Scenario.** The task is stopped after the secondary output is linked. The record is one output, with no exit status and no raw. A re-run on a later date produces a secondary with a different `date` field (anl:6696). `write_all_once` refuses it as "exists with other bytes" (anl:4646–4648), so recovery needs an output of record deleted.

**Fix.**
- Launch under `nohup` and `caffeinate -is`, as GR14 and G-READ-n did, and record the PID.
- In `after`, when `exit.txt` is missing, still build the raw, marked "no exit status: interrupted", from `out.txt` and `err.txt` as they stand. Add a name-only `ls -A` of `data/n/verdicts`, then stop for the coordinating session.
- Move the raw promptly to `results/raw/`. `run/` and `raw/` sit in the scratch folder, which the midnight cleanup empties of files about four days old.

### F4 [RISK] NOTES.md:44–47; verdicts_steps.sh:102–107 — the end-wait and the process checks depart from the standing form, and the departure is not declared

**Defect.** The standing form has three parts:
- GR14 (R:620–621): the run in the background under `caffeinate`, and the end-wait on the PID alone.
- G-READ-n's run (R:59–66): `nohup caffeinate -is … & disown`; the PID's command line checked at 2 s; `wait <PID>` by `kill -0`; then "no process naming the run".
- G-ANL-n's `check` and `after` (R:8169–8170, 8175–8176): no Python process except the declared one, by `pgrep -f '[p]ython'`.

v1 instead uses the Bash tool's background notice on the steps' bash. It records no PID, and neither `check` nor `after` asserts anything about processes. NOTES's "nothing else runs meanwhile" is a promise, not a check.

**Scenario.**
- The bash is killed while the interpreter runs on as an orphan. The tool reports the end before the invocation has ended, so a later `after`, or any read of `run/`, breaches item 5.
- Or another session's Python process runs through the window, and the record does not show it.

**Fix.**
- Start the interpreter under `nohup` and `caffeinate`, write its PID to `run/pid.txt`, and wait on that PID alone.
- In `check`, assert that no process names the run and no Python process is running.
- In `after`, assert that the PID is gone.
- Otherwise, declare the departure to the seat.

### F5 [RISK] verdicts_steps.sh:92–100, 115–176 — nothing the run read is re-verified before launch or after it

**Defect.**
- `run` re-asserts none of `check`'s conditions. G-READ-n's run did: "the same assertions, then …" (R:59).
- `after` does none of these:
  - re-run `shasum -c`;
  - compare HEAD with `head.txt`;
  - check that `tmp/` is empty;
  - check that the outputs bind the pins.

  G-ANL-n's `after` did some of this (R:8175), and so did G-READ-n's (R:66–67).
- The analyzer cross-binds the lock, the report, the artifact and itself (anl:6688, 6692, 6704–6706, 6723–6725). It holds the cosines file only to being committed and clean and to its form (anl:6641, 6607–6622).

**Scenario.** Between `check` and `run`, a parallel session commits another `gvec_cosines.json` of the same form, or moves HEAD. The analyzer accepts it, `after` prints ALL PASS, and the outputs carry the other file's sha256 (anl:6747) with no remark.

**Fix.**
- `run` calls `check`, writes its output to `run/check.txt`, and refuses unless it says ALL PASS.
- `after` does three things:
  - re-runs the `shasum -c`;
  - asserts HEAD equals `head.txt` and `tmp/` is empty;
  - with `/usr/bin/grep -c -F` (counts only), counts each pinned sha256 in `N-pod_VERDICTS.json`, plus the secondary's printed sha256 (anl:6769), and FAILs on any zero. The pins are the analyzer (anl:6697), schema (6698), lock (6699), report (6700), cosines (6747) and artifact (6756).

### F6 [RISK] verdicts_steps.sh:85–87, 92–113, 127 — the environment of record is printed once and recorded nowhere

**Defect.** `check` prints the environment versions to the terminal only:
- the venv's version line;
- numpy's dist-info name;
- macOS.

`run/` holds no environment, the raw's header (127) has none, and v7 writes none into its outputs.

The precedent did more. G-READ-n's GR10 recorded python, numpy, BLAS, the CPU count and the five thread variables as unset. Its window also asserted AC power and Low Power Mode off (R:55–58, 93–95).

Also, the `pyvenv.cfg` version line records how the venv was created; it is not the interpreter reporting its own version.

**Scenario.** A thread variable set in the tool's environment, a venv rebuilt with another numpy, or a run on battery. Nothing fails. Rule 27's "library versions … in the logged entry" then rests on a terminal line from `check`, which may predate the run.

**Fix.**
- In `run`, before launch, write `run/env.txt` with:
  - the `pyvenv.cfg` version line and numpy's dist-info name;
  - `sw_vers -productVersion` and `sysctl -n hw.ncpu`;
  - whether each of the five thread variables is set or unset (`OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS`, `NUMEXPR_NUM_THREADS`).
- Assert the five unset and the versions of record (3.12.9, numpy-2.5.1), and carry `env.txt` into the raw header.
- Add AC power and Low Power Mode checks if the window's terms include them.

### NITs

**F7 [NIT] NOTES.md:42–48; standin_test.sh:20, 22, 36–37 — `bash <file>` runs PATH's bash.** On this laptop that is `/opt/homebrew/bin/bash`, which comes before `/bin/bash` 3.2. So the run, and probably the stand-in tests, do not run under the shebang's shell. I found nothing in the steps that depends on the bash version. Fix: invoke `/bin/bash` by path, or record `$BASH_VERSION`.

**F8 [NIT] verdicts_steps.sh:94–95 — "one run" is not atomic.** Two racing `run` calls can both pass `[ -e "$W" ]` before `mkdir -p`. Fix: use `mkdir "$W"` without `-p` as the lock, then `mkdir "$T"`.

**F9 [NIT] verdicts_steps.sh:136 — the guard-marker screen asserts nothing.** Fix: on exit 0, FAIL unless the count is 1 and the matching line is the raw's line 2.

**F10 [NIT] verdicts_steps.sh:137–140 — non-zero exits get the 2/4 gloss and no look at the output folder.** The gloss is wrong for exits 1, 97, 98, 126, 127 and 128+N. Exit 1 can also come with one output written: an `OSError` after the first link (anl:4649) is not caught by `main` (anl:6833–6838). A traceback also puts a home path in the raw; line 133 catches it. Fix: give each code its own meaning, and add a name-only `ls -A` of `data/n/verdicts` on every non-zero exit.

**F11 [NIT] verdicts_steps.sh:24, 29–34 — seven-hex commit ids.** This fails safe if an id becomes ambiguous, but full ids cost nothing.

**F12 [NIT] verdicts_steps.sh:6, 13; NOTES.md:42, 48, 69 — "read-only, no interpreter" is not exact.** `/usr/bin/shasum` is a Perl script, and `after` writes `raw/`. Fix: "no Python; shasum (Perl) by name; writes only raw/ in this folder".

**F13 [NIT] verdicts_steps.sh:121, 127 — the raw header states the pinned analyzer sha256, not a measured one.** It holds indirectly, through `lock_names` (anl:6690–6693) and `committed_problems`. The raw also names neither the steps file nor `inputs.sha256` by sha256. Fix: hash the analyzer in `run`, and put both files' sha256s in the header.

**F14 [NIT] NOTES.md:35–38 — one provenance claim is wrong.** NOTES says "the artifact's in raw (D) (1)", but raw (D) is not committed: `git rev-parse HEAD:<raw D>` fails, so it is untracked. The artifact's sha256 does stand whole in committed `RESULTS.md` (1 line).
- The rest check out: the analyzer's sha256 in LOCK-n.md (2 lines); LOCK-n.md's in n_sessions.py (2); the schema's in n_analyze.py (1) and LOCK-n.md (2); the cosines file's in LOCK-n.md (1, L:711).
- I did not check the report's sha256 in the close list; the close list itself is committed.
- Raw (D)'s sha256 is 6b5be7a3…e420, as NOTES:4 says.

Fix: cite RESULTS.md.

**F15 [NIT] NOTES.md:72–75; stand_python.in:2–3, 28 — NOTES describes the stand-in record more strongly than the log shows.**
- (a) `identical` FAILs on two lines (log 19–20), not on one line alone.
- (b) The second-run and second-after refusals were tested on `ok` only (harness 35–37), not in every variant.
- (c) The claim "stderr in the raw" for `stop` is not shown in the log.
- (d) The stand-in's tuple has four members; v7's has five (anl:672). This is harmless to `after`'s pattern.
- (e) `<L>/standin/` also holds `runs/`, an earlier run whose harness and log are not among the files.

Fix: reword NOTES, and account for `runs/`.

**F16 [NIT] standin_test.sh:12 — sub-conditions that matter are untested:**
- the interrupted path (F3);
- the FAIL branches of the scratch-path screens over the raw (134–135) and the outputs (170); `homeraw` and `homeout` exercise `$HOME` only;
- the FAIL branch of the `<repo>` count (147–148);
- exits 97 and 98;
- a stderr that names the root (the scrub at 129);
- every FAIL branch of `check`;
- the physical working folder: the stand-in prints bash's logical `$PWD` (stand_python.in:10), but the interpreter builds `sys.executable` from the physical folder. A symlinked venv folder would give six `<repo>`s plus a home path, and `after` would FAIL a correct run.

The repository root itself is physical (`pwd -P` equals R). G-ANL-n's raw is described as printing the venv folder under `<repo>` (R:8193–8195). Fix: add these variants, and assert `[ "$(pwd -P)" = "$1" ]` by builtins after the `cd` in `check`.

**F17 [NIT, unsure] NOTES.md:79–82.** NOTES makes the dated note conditional ("where N1's label is 'concluded, not answered'"). Raw (D):58 lists it with no condition. NOTES also cites "ledger (91) … raw (D) §2 item 5", but raw (D):62 has the ledger at §5 item 5. §2 is outside the lines I may read, so NOTES may be faithful to it. Fix: cite the line that carries the condition.

**F18 [NIT, unsure] NOTES.md:51–54; verdicts_steps.sh:16, 138 — exit 4 is glossed as "a pause or a fire".** In v7, exit 4 is any `AnlStop`: non-finite inputs (anl:192) or internal-consistency STOPs (anl:161–235, 3284, 3557–3612, 4608, 6577–6589). A report standing in PAUSE is instead a refusal with exit 2 (anl:6677–6679), which the gloss would route "to you". That case cannot happen here, because the report is COMPLETE. I cannot tell whether "a pause or fire" also covers an exit-0 outcome that carries a standing pause (`pause_points`, anl:6600); `after` would not surface one. Fix: gloss exit 4 as "any STOP", and say what, if anything, goes to the seat on exit 0.

**Observation (outside the files under review, not counted).** The docstring at anl:5893–5894 says "nothing under a ckpt or reports directory is among them". But on the verdicts path the report under `data/n/reports/` is among the paths checked (anl:6635–6641). This has no effect on the run.

## 3. Commands I ran

`<...>` stand for the paths above. `--x` stands for `-- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`.

1. `shasum -a 256` of the six files in `<F>`: six digests, as in section 1.
2. `git rev-parse HEAD:scripts/n_analyze.py`, `git hash-object -- scripts/n_analyze.py`, `shasum -a 256` of the analyzer, `git rev-parse HEAD`: blob cb8714d8… twice (equal); 735da934…a7a8; 7ab1cf6b….
3. `/usr/bin/grep -n` for 16 definitions in n_analyze.py: their lines (1006 … 6512).
4. `/usr/bin/grep -n` in n_analyze.py for local-root strings, TMPDIR, tempfile and warning settings: tempfile only (battery helpers, 3907–6113); nothing else.
5. `/usr/bin/grep -n` for the campaign folder and the close list in n_sessions.py, n_analyze.py and LOCK-n.md: n_sessions.py 7734–7773 and other lines (the close list's path and pin; the cells' folder).
6. `/usr/bin/grep -n` for print and stream writes in n_analyze.py: on the verdicts path, stdout only at 6787 and 6839.
7. `ls valence_core/n`, then `/usr/bin/grep -n -E` for imports and prints in three valence_core files: 16 names; imports; schema prints only in its self-test.
8. `/usr/bin/grep -c ''` and import greps on `valence_core/__init__.py`, `adapters/base.py`, `adapters/__init__.py`: 19 lines; stdlib, numpy, `.base`.
9. For the five inputs other than the report: `git rev-parse HEAD:<p>`, `git rev-parse <rev>:<p>` and `git hash-object` compared in the shell; `shasum` matched against `<F>/inputs.sha256` with `grep -q -x -F`: 5 blobs equal, 5 sha256s as pinned.
10. `git log --format='commit %h' --name-only --x | awk`: 7ab1cf6, 098218c, b6ea27f, ef105f1, e3b48ed, the same as `rev_of`.
11. `git grep -c -F <sha256> HEAD --x ':!results/raw/**'` for each of the six pins: the counts given in F14; the report's pin is found nowhere outside the excluded paths (exit 1).
12. `git rev-parse -q --verify HEAD:<raw D>`, `shasum <raw D> | cut -c1-8,61-64`, `git rev-parse -q --verify HEAD:<close list>`: raw (D) is not in HEAD; 6b5be7a3e420; the close list is in HEAD.
13. `ls -A <L>`, `ls -A <L>/standin`, and `shasum` of each live file against its frozen copy: `NOTES.md inputs.sha256 review standin verdicts_steps.sh`; `runs runs2` plus the three stand-in files; "live equals frozen" 6 times.
14. For the 10 variants: the harness's `sed` substitutions over the frozen files, piped to `shasum`, against the `runs2` copies: equal 10 times.
15. `/bin/bash --version | head -n 1`, then `/bin/bash -n` on the three files: 3.2.57(1)-release; exit 0 three times.
16. `/usr/bin/grep` in LOCK-n.md for the v1.0, route, gate and analyzer-sha256 lines: 1; 1239 Route B; 1330 "48 of 48, PASS"; 213 and 913.
17. `/usr/bin/grep -o -E` for version keys in `data/n/gates/G-ANL-n.json`, and for `np.__version__`, `sys.version` and `platform.` in n_analyze.py: nothing; nothing.
18. `/usr/bin/grep -n -o -E` for numpy versions in RESULTS.md: python 3.12.9 and numpy 2.5.1 on the laptop (93, 6225, 20744, 22385, 26745).
19. `/usr/bin/grep -n -o -E` for the run form in RESULTS.md: lines 60, 620, 987, 7864, 8032, 8171, 8328, 8538, 8540, 8799, 8952, 9084.
20. `/usr/bin/grep -n -E` for BLAS calls and random generators in n_analyze.py: `@` at 212–238; lstsq and polyfit in the battery; default_rng at 147 and 2410.
21. `/usr/bin/grep -c ''` on `valence_core/n/__init__.py`; HEAD blob against working tree for the four closure files; schema imports: 8 lines; all four at HEAD's bytes; stdlib only.
22. `/usr/bin/grep -n -E` for the data, n and .DS_Store rules in .gitignore: 171, 176, 261–370; no rule for verdicts.
23. `/usr/bin/grep -c ''` and `-o -E` key names on `gvec_cosines.json`: 10 lines; `cosines` and the six pairs, once each.
24. `pwd -P` in `<repo>` compared with R; `type -a bash | head -n 3`; `command -v` for nice, sed, date, ls: the root is physical; /opt/homebrew/bin/bash comes before /bin/bash; /usr/bin/nice, /usr/bin/sed, /bin/date, /bin/ls.
25. `[ -e <repo>/data/n/verdicts ]`: absent.
26. `/usr/bin/grep -n -E` for the outcome tuple: 660 and 672 (five members).
27. `/usr/bin/grep -n -E 'raise AnlStop'`: 18 sites.
28. The six frozen digests compared in the shell with the brief's values: EQUAL 6 times.
29. `mkdir -p <L>/review/reviewer`, then `ls -A <L>/review`: `frozen frozen.sha256 reviewer`.

The Write call for the report was refused, so no report digest was taken.

**File-tool reads (no shell):**
- the six frozen files, whole;
- n_analyze.py lines 1–120, 660–673, 975–1024, 3040–3298, 4600–4709, 5860–5919, 6225–6847;
- LOCK-n.md lines 165–184 and 700–729;
- `<raw D>` lines 56–62;
- `valence_core/__init__.py` and `valence_core/adapters/__init__.py`, whole;
- RESULTS.md lines 40–97, 612–627, 8160–8205, 8324–8333.

## 4. Overall

No BUG. `run` calls v7's `verdicts` as routed, with the inputs of record, no `--out`, and in a form the analyzer accepts, so it should pass on today's tree. F1–F6 are worth closing in a v2 before the window:
- the campaign folder and the import closure go unchecked;
- an interrupted run leaves no raw and no recovery path;
- the end-wait form departs from the standing one undeclared;
- nothing is re-verified after the run;
- the environment is not recorded.
````

## 6. The dispositions of the review, taken into v2

`review/dispositions_v1.md`, sha256 `0e245a88e520a31c03f9c6babde8a3727b7f76c248d9c7eff5454407b1a5584e`, 92 lines in the kit.

````markdown
# Dispositions of the blind review of the VERDICTS launch files v1, taken into v2

The review: `review/reviewer/report.md` (sha256 6b051dbf…56bd, 278 lines). It was extracted verbatim, by Perl's
JSON::PP, from the reviewer's hand-back in its task transcript, because a subagent's file tool refuses report files.
It found 0 BUG, 6 RISK and 12 NIT, plus one observation. Every finding is taken into v2 except where stated.

- **F1 [RISK] the campaign folder: adopted.** `check` asserts the 138 tracked cells (`git ls-files`), no status line
  under `--ignored --untracked-files=all`, and no name changed since 95cd461 (`git diff --name-only`). Each is printed
  by count only. These are list v2 item 1's names forms over a ckpt folder, put to the coordinating session for its
  read, as the reviewer asks.
- **F2 [RISK] the import closure: adopted.** The schema's import runs four more package files:
  `valence_core/__init__.py`, `valence_core/adapters/__init__.py`, `valence_core/adapters/base.py` and
  `valence_core/n/__init__.py`. They join the pins: `inputs_v2.sha256` has ten lines, and the four are checked as the
  six are (sha256, blob, last commit). `git status --porcelain -- valence_core scripts` must be empty, by count, in
  `check` (so at launch) and in `after`.
- **F3 [RISK] an interrupted run: adopted.** The launch is `nohup caffeinate -is /bin/bash <steps> inner`, with its
  PID in run/pid.txt. caffeinate runs the command in its own PID, so that PID is the inner bash's. `inner` writes
  secs.txt, then exit.txt last. With no exit.txt, `after` still builds the raw,
  marked "no exit status: the run was interrupted", prints the names in `data/n/verdicts`, and stops. The raw moves to
  `results/raw/` in the commit window; the scratch cleanup deletes files about four days old, beyond the window's span.
- **F4 [RISK] the end-wait form: adopted, the standing form.** The wait is on the PID alone (`kill -0` and the PID's
  own command line every 5 s), as the harness's background task (the `wait` mode). `check` asserts no process naming
  the run and none named python. `after` refuses while the PID lives or any process names the run.
- **F5 [RISK] re-verification: adopted.** `run` calls `check` and refuses unless it prints ALL PASS; the output is kept
  as run/check.txt. `after` re-runs `shasum -c` (10 of 10); asserts HEAD equals head.txt, `valence_core/` and
  `scripts/` clean, and tmp/ empty; and counts each of the six bound pins and the secondary's sha256 in
  `N-pod_VERDICTS.json`, failing on any zero.
- **F6 [RISK] the environment: adopted.** `run` writes run/env.txt, which the raw carries:
  - the bash version, macOS and hw.ncpu;
  - the venv's version line, numpy's dist-info name, and the folder name of the venv's base interpreter;
  - the power source and powermode, and pmset's sleep and wake counts;
  - the five thread variables.

  `check` asserts the five unset, AC power, Low Power Mode off and the versions of record (version_info 3.12.9;
  numpy-2.5.1). `after` compares the sleep and wake counts, as a note, not a FAIL. The interpreter's own version is
  not queried, since that would be a second interpreter process; the venv's version line and its base interpreter's
  folder stand for it, declared.
- **F7 [NIT] PATH's bash: adopted.** `/bin/bash` by path in NOTES_v2, in the launch, and in the harness; env.txt records
  `$BASH_VERSION`.
- **F8 [NIT] one run not atomic: adopted.** `mkdir "$W"` (no `-p`) is the lock.
- **F9 [NIT] the marker screen: adopted.** On exit 0, `after` fails unless the guard markers stand on the INVOCATION
  line alone.
- **F10 [NIT] the non-zero exits: adopted.** Each code has its meaning (no exit status, 1, 2, 4, 97, 98, 126/127, a
  signal, other), and every non-zero end prints the names in `data/n/verdicts`.
- **F11 [NIT] seven-hex ids: adopted in part.** The ids stay short in the file, since they fail safe: an ambiguous id
  makes `rev-parse --verify` fail, and `check` FAILs. `check` resolves and prints each full id, and asserts it is the
  last commit that touched its file.
- **F12 [NIT] "read-only, no interpreter": adopted.** The header now says: no Python but `run`'s launch; `shasum`
  (Perl) by name; the modes write only in this folder, and the analyzer alone writes `data/n/verdicts`.
- **F13 [NIT] the measured analyzer sha256: adopted.** `after` hashes the analyzer and both launch files, and the raw's
  header carries the three sha256s. The check at launch, also in the raw, carries the ten shasum OK lines.
- **F14 [NIT] the artifact pin's source: adopted.** NOTES_v2 cites RESULTS.md (committed), not raw (D) (untracked).
- **F15 [NIT] NOTES on the stand-in record: adopted.** NOTES_v2 describes runs3 as its log shows it:
  - `identical` fails on two lines (the word "written", for both outputs);
  - the second-run and second-after refusals are tested on `ok` alone;
  - `runs/` (v1 before the `abbr` fix) and `runs2/` (v1 as frozen) are named;
  - the stand-in's tuple has v7's five members.
- **F16 [NIT] untested sub-conditions: adopted in part.** New variants:
  - `interrupted`, `noglob` (exit 97), and `uncaught` (exit 1, a traceback naming the root);
  - `stderrroot` (the scrub in stderr), `scratchraw`, `repocount`, `markeroff`, `pinmissing` and `tmpleft`.

  `check` also asserts that the venv's bin is a physical path (`pwd -P`, builtins). Not done:
  - an isolated FAIL fixture for each of `check`'s assertions; `check` is tested on the real tree (ALL PASS) and,
    coarsely, on a fake root (FAIL);
  - exits 98 and 126/127, whose branches only print a meaning.
- **F17 [NIT, unsure] the dated note's condition: settled before the run.** The PI's item 4 makes the note
  conditional: "the VERDICTS entry adds a dated note in its figures where N1's label is 'concluded, not answered'".
  Raw (D) §2 item 6 agrees, and its §5 item 4 gives this session §2 items 3 and 6. §5 item 1 lists the note without
  the condition; the PI's words are the record. The coordinating session's correction of 2026-11-27 adds that
  ledger (91) is the seat's own record (raw (D) §2 item 5; routing item 3, "[record]"), not an item for the VERDICTS
  entry. NOTES v1 cited it as the entry's; NOTES_v2 does not.
- **F18 [NIT, unsure] exit 4's gloss: adopted.** Exit 4 is any STOP (`AnlStop`). A report in PAUSE refuses with exit 2,
  and cannot arise here, since the report is COMPLETE. On exit 0 nothing goes to the seat before the entry; the seat
  reads after the analyzer's output (raw (D) §5 item 2).
- **The observation (anl:5893–5894, `committed_problems`' docstring): kept for the VERDICTS entry** as a dated note on
  v7. On the verdicts path the stage report is among the committed paths checked, which the docstring's last clause
  denies. It has no effect on the run, and v7 stays of record, unedited.

## Code's own, from v2's first stand-in run (runs3), fixed before v2 went to anyone

- **The venv's glob.** In bash a glob that matches nothing stays literal, so `[ $# -eq 1 ]` passed, and `noglob`
  ended at exit 98 (cd failed), not 97. The check is now `{ [ $# -eq 1 ] && [ -d "$1" ]; } || exit 97`, and 97's
  meaning reads "no folder, or more than one".
- **The scrub.** bash's own error lines name the steps file's path, which is in the launch folder, and the raw's scrub
  covered only the repository's root. `noglob`'s raw named a scratch path, which the screen caught (FAIL). The raw now
  prints the launch folder as `<launch>` and the root as `<repo>`, in stdout and in stderr alike.
- **The interrupted stand-in killed nothing.** On this laptop `caffeinate` runs its command in its own PID and holds
  its assertion in a child, so the stand-in's walk up to a `caffeinate` parent found none, and the run ended at
  exit 0. A traced launch showed this: the PID `$!` was `/bin/bash`, its parent the calling shell. The stand-in now
  kills run/pid.txt's PID, which is the inner bash's.
- **Two clarifications in the steps.** The `wait` mode gives caffeinate's assertion holder up to 10 s to end after its
  parent, before counting processes that name the run. The header says what the PID is.
````

## 7. v2's check on the real tree at 7ab1cf6, before the send

`review/check_v2_final.txt`, sha256 `f88e1b8cfa216ea7aee341a3f7a690e7ddfddf2e768c99bf333613da640b2676`, 35 lines in the kit.

````text
check: the calendar date 2026-11-27
PASS HEAD 7ab1cf6b55a8aa23792e69cafab737dcb4b39b52 descends from 7ab1cf6b55a8aa23792e69cafab737dcb4b39b52
PASS scripts/n_analyze.py: clean, HEAD's blob, last touched at b6ea27f4ad9154c8b0a6d16e8787437ee7d649e9
PASS LOCK-n.md: clean, HEAD's blob, last touched at 098218c07c67ac968648bb8e93a6c95796f16f1a
PASS valence_core/n/schema.py: clean, HEAD's blob, last touched at ef105f129740840eabcf87ffbb836e078ba9636d
PASS data/n/gates/G-READ-n.json: clean, HEAD's blob, last touched at 7ab1cf6b55a8aa23792e69cafab737dcb4b39b52
PASS data/n/gvec/gvec_cosines.json: clean, HEAD's blob, last touched at e3b48ed98d099bb70b7f8badd335de14007a70c8
PASS data/n/reports/campaign.json: clean, HEAD's blob, last touched at 95cd461e518628265eea500f4e6500bff5f912c9
PASS valence_core/__init__.py: clean, HEAD's blob, last touched at c5b8f1a63fe7e39067f91a657c1ea53cee98b1ed
PASS valence_core/adapters/__init__.py: clean, HEAD's blob, last touched at 1465b34c758edb258184fcac49b7776f57d65042
PASS valence_core/adapters/base.py: clean, HEAD's blob, last touched at 7da95097ea36618dbeb0eea0457ca8b667aa5080
PASS valence_core/n/__init__.py: clean, HEAD's blob, last touched at 5a975274463a3752cc70cdfee5dcfa62ebf3ab02
PASS inputs_v2.sha256 names the ten files in order
  shasum: scripts/n_analyze.py: OK
  shasum: LOCK-n.md: OK
  shasum: valence_core/n/schema.py: OK
  shasum: data/n/gates/G-READ-n.json: OK
  shasum: data/n/gvec/gvec_cosines.json: OK
  shasum: data/n/reports/campaign.json: OK
  shasum: valence_core/__init__.py: OK
  shasum: valence_core/adapters/__init__.py: OK
  shasum: valence_core/adapters/base.py: OK
  shasum: valence_core/n/__init__.py: OK
PASS the ten sha256s are inputs_v2.sha256's
PASS valence_core/ and scripts/ clean (git status, by count)
PASS the campaign's cell folder: 138 tracked, no other file, none changed since 95cd461 (names only, by count)
PASS data/n/verdicts absent
PASS run/ and tmp/ absent
PASS the venv's bin: one match of its glob, a physical path, ./python executable
PASS no process names the run, none is named python
PASS the five thread variables unset
PASS AC power
PASS Low Power Mode off (powermode 0)
PASS the venv's versions of record: version_info = 3.12.9; numpy-2.5.1.dist-info
check: ALL PASS
````

## 8. v2's check on the real tree at b23f91d, before the grant

`review/check_v2_at_b23f91d.txt`, sha256 `3ec06fe8c7b6ca515bfeff091dfcfb37c28e8eb7ff420b4599bc625e5ec278b7`, 35 lines in the kit.

````text
check: the calendar date 2026-11-27
PASS HEAD b23f91dbeb2b9a88b30695417bda9a44e3f8be0e descends from 7ab1cf6b55a8aa23792e69cafab737dcb4b39b52
PASS scripts/n_analyze.py: clean, HEAD's blob, last touched at b6ea27f4ad9154c8b0a6d16e8787437ee7d649e9
PASS LOCK-n.md: clean, HEAD's blob, last touched at 098218c07c67ac968648bb8e93a6c95796f16f1a
PASS valence_core/n/schema.py: clean, HEAD's blob, last touched at ef105f129740840eabcf87ffbb836e078ba9636d
PASS data/n/gates/G-READ-n.json: clean, HEAD's blob, last touched at 7ab1cf6b55a8aa23792e69cafab737dcb4b39b52
PASS data/n/gvec/gvec_cosines.json: clean, HEAD's blob, last touched at e3b48ed98d099bb70b7f8badd335de14007a70c8
PASS data/n/reports/campaign.json: clean, HEAD's blob, last touched at 95cd461e518628265eea500f4e6500bff5f912c9
PASS valence_core/__init__.py: clean, HEAD's blob, last touched at c5b8f1a63fe7e39067f91a657c1ea53cee98b1ed
PASS valence_core/adapters/__init__.py: clean, HEAD's blob, last touched at 1465b34c758edb258184fcac49b7776f57d65042
PASS valence_core/adapters/base.py: clean, HEAD's blob, last touched at 7da95097ea36618dbeb0eea0457ca8b667aa5080
PASS valence_core/n/__init__.py: clean, HEAD's blob, last touched at 5a975274463a3752cc70cdfee5dcfa62ebf3ab02
PASS inputs_v2.sha256 names the ten files in order
  shasum: scripts/n_analyze.py: OK
  shasum: LOCK-n.md: OK
  shasum: valence_core/n/schema.py: OK
  shasum: data/n/gates/G-READ-n.json: OK
  shasum: data/n/gvec/gvec_cosines.json: OK
  shasum: data/n/reports/campaign.json: OK
  shasum: valence_core/__init__.py: OK
  shasum: valence_core/adapters/__init__.py: OK
  shasum: valence_core/adapters/base.py: OK
  shasum: valence_core/n/__init__.py: OK
PASS the ten sha256s are inputs_v2.sha256's
PASS valence_core/ and scripts/ clean (git status, by count)
PASS the campaign's cell folder: 138 tracked, no other file, none changed since 95cd461 (names only, by count)
PASS data/n/verdicts absent
PASS run/ and tmp/ absent
PASS the venv's bin: one match of its glob, a physical path, ./python executable
PASS no process names the run, none is named python
PASS the five thread variables unset
PASS AC power
PASS Low Power Mode off (powermode 0)
PASS the venv's versions of record: version_info = 3.12.9; numpy-2.5.1.dist-info
check: ALL PASS
````

## 9. The v2 stand-in for the venv's python

`standin/stand_python_v2.in`, sha256 `5ad64c1b457162c957a8d659aa8cb19354b3ae2953d06190d2f2dc22e4f671a5`, 53 lines in the kit.

````bash
#!/bin/bash
# stand-in for the venv's python, test only (no interpreter anywhere): prints what v7's verdicts prints (the INVOCATION
# line, then the VERDICTS line with v7's five-member tuple) and writes its two outputs, N-pod_VERDICTS.json binding the
# six pins and the secondary's sha256; the variant is baked in by the harness.
R='__R__'
L='__L__'
m='__MODE__'
printf 'argv12 [%s %s] nice [%s] TMPDIR [%s]\n' "$1" "$2" "$(ps -o nice= -p $$ | tr -d ' ')" "${TMPDIR:-}" > "$R/env.txt"
shift 2
vf="j""lens-stand"   # the venv folder's name as v7's INVOCATION line prints it: two guard markers, in output only
args="$*"
[ "$m" = repocount ] && args=$(printf '%s' "$args" | sed 's| --gvec [^ ]*||')
extra=""
[ "$m" = homeraw ] && extra=" $HOME/x"
[ "$m" = scratchraw ] && extra=" /private/x"
echo "INVOCATION: $R/$vf/.venv/bin/python $args$extra"
case "$m" in
  refuse) echo "REFUSED: the stand-in refuses" >&2; exit 2 ;;
  stop) echo "STOP: the stand-in stops" >&2; exit 4 ;;
  stderrroot) echo "REFUSED: cell $R/x; launch $L/y" >&2; exit 2 ;;
esac
pin() { sed -n "s|^\([0-9a-f]\{64\}\)  $1\$|\1|p" "$L/inputs_v2.sha256"; }
mkdir -p "$R/data/n/verdicts"
printf '{"s": 1}\n' > "$R/data/n/verdicts/N-pod_secondary.json"
a=$(shasum -a 256 "$R/data/n/verdicts/N-pod_secondary.json" | cut -d' ' -f1)
case "$m" in
  uncaught)
    printf 'Traceback (most recent call last):\n  File "%s/scripts/n_analyze.py", line 1\nOSError: stand-in\n' "$R" >&2
    exit 1 ;;
  interrupted)   # kill the inner bash (its PID is run/pid.txt's: caffeinate runs it in place), so no exit.txt is written
    kill -9 "$(cat "$L/run/pid.txt")"
    exit 0 ;;
esac
{
  for p in scripts/n_analyze.py valence_core/n/schema.py LOCK-n.md data/n/reports/campaign.json data/n/gvec/gvec_cosines.json data/n/gates/G-READ-n.json; do
    { [ "$m" = pinmissing ] && [ "$p" = data/n/gvec/gvec_cosines.json ]; } && continue
    printf ' "%s": "%s",\n' "$p" "$(pin "$p")"
  done
  printf ' "secondary": "%s"\n' "$a"
  [ "$m" = homeout ] && printf ' "x": "%s"\n' "$HOME"
} > "$R/data/n/verdicts/N-pod_VERDICTS.json"
[ "$m" = strayfile ] && printf 'x\n' > "$R/data/n/verdicts/.N-pod_VERDICTS.json.1.tmp"
[ "$m" = tmpleft ] && printf 'x\n' > "$TMPDIR/left"
b=$(shasum -a 256 "$R/data/n/verdicts/N-pod_VERDICTS.json" | cut -d' ' -f1)
how=written
[ "$m" = identical ] && how=identical
[ "$m" = badsha ] && b=$(printf '%064d' 0)
mk=""
[ "$m" = markeroff ] && mk=" $(printf 'q%s' wen)"
echo "VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS, PASS) -> N-pod_secondary.json ($how; sha256 $a); N-pod_VERDICTS.json ($how; sha256 $b)$mk"
[ "$m" = extra ] && echo "an extra line"
[ "$m" = errnonempty ] && echo "a warning" >&2
exit 0
````

## 10. The v2 stand-in harness

`standin/standin_test_v2.sh`, sha256 `5405017b28ca58a1bf5191788475a1af0945e75f969e66b6709fd59b4cf8d39c`, 58 lines in the kit.

````bash
#!/bin/bash
# Stand-in tests of verdicts_steps_v2.sh's run, wait and after modes (no interpreter anywhere). Each variant gets its
# own fake root: a git repository holding stand-in bytes at the ten pinned paths (one commit), a fake venv with a
# stand-in python, and a launch folder holding the root's own pins file and a copy of the steps file in which exactly
# three lines differ (R=, L=, and run's check call, stubbed to ALL PASS since check cannot pass on a fake root; the
# diff is printed). check itself is tested on the real tree (ALL PASS) and, coarsely, on a fake root (FAIL).
set -u
export LC_ALL=C
L=<scratch>/n9/verdicts
SI=$L/standin
TD=$SI/runs4
if [ -e "$TD" ]; then echo "runs4/ exists; make a new version"; exit 1; fi
mkdir -p "$TD"
PATHS="scripts/n_analyze.py LOCK-n.md valence_core/n/schema.py data/n/gates/G-READ-n.json data/n/gvec/gvec_cosines.json data/n/reports/campaign.json valence_core/__init__.py valence_core/adapters/__init__.py valence_core/adapters/base.py valence_core/n/__init__.py"
VARIANTS="ok refuse stop stderrroot uncaught interrupted noglob extra badsha identical strayfile homeout homeraw scratchraw repocount markeroff pinmissing tmpleft errnonempty"
for m in $VARIANTS; do
  RR=$TD/$m/repo
  LL=$TD/$m/launch
  mkdir -p "$RR" "$LL"
  for p in $PATHS; do mkdir -p "$RR/$(dirname "$p")"; printf 'stand-in bytes for %s\n' "$p" > "$RR/$p"; done
  git -C "$RR" init -q
  ( cd "$RR" && git add -- $PATHS && git -c user.name=standin -c user.email=standin@localhost -c commit.gpgsign=false -c core.hooksPath=/dev/null commit -q -m standin )
  if [ "$m" != noglob ]; then
    mkdir -p "$RR/jl-stand/.venv/bin" "$RR/jl-stand/.venv/lib/python3.12/site-packages/numpy-2.5.1.dist-info"
    printf 'version_info = 3.12.9\n' > "$RR/jl-stand/.venv/pyvenv.cfg"
    sed -e "s|__R__|$RR|" -e "s|__L__|$LL|" -e "s|__MODE__|$m|" "$SI/stand_python_v2.in" > "$RR/jl-stand/.venv/bin/python"
    chmod +x "$RR/jl-stand/.venv/bin/python"
  fi
  ( cd "$RR" && shasum -a 256 $PATHS ) > "$LL/inputs_v2.sha256"
  sed -e "s|^R=.*|R=$RR|" -e "s|^L=.*|L=$LL|" -e 's|^  out=$(check)$|  out="check: ALL PASS"|' "$L/verdicts_steps_v2.sh" > "$LL/verdicts_steps_v2.sh"
  /bin/bash "$LL/verdicts_steps_v2.sh" run > "$LL/run.log" 2>&1; echo "run rc $?" >> "$LL/run.log"
  /bin/bash "$LL/verdicts_steps_v2.sh" wait > "$LL/wait.log" 2>&1; echo "wait rc $?" >> "$LL/wait.log"
  /bin/bash "$LL/verdicts_steps_v2.sh" after > "$LL/after.log" 2>&1; echo "after rc $?" >> "$LL/after.log"
done
echo "== the copy's diff from verdicts_steps_v2.sh (variant ok; the fake root and launch folder as <runs>)"
diff "$L/verdicts_steps_v2.sh" "$TD/ok/launch/verdicts_steps_v2.sh" | sed "s|$TD|<runs>|g"
echo "== per variant: the three modes' exit codes, the stand-in's environment, and after's verdict lines"
for m in $VARIANTS; do
  LL=$TD/$m/launch
  e=$(sed "s|$TD|<runs>|g" "$TD/$m/repo/env.txt" 2>/dev/null)
  echo "== $m: $(tail -n 1 "$LL/run.log"), $(tail -n 1 "$LL/wait.log"), $(tail -n 1 "$LL/after.log"); env: ${e:-none}"
  /usr/bin/grep -e '^FAIL' -e 'STOPPED' -e 'ALL PASS' -e '^REFUSED' -e '^exit ' -e '^no exit' -e '^data/n/verdicts holds' "$LL/after.log" | sed 's/^/   /'
done
echo "== ok: after.log whole"
sed "s|$TD|<runs>|g" "$TD/ok/launch/after.log"
echo "== ok: the raw (cut at 160 columns)"
cut -c1-160 "$TD/ok/launch/raw/"*_n-verdicts_out.txt
echo "== ok: a second run and a second after both refuse"
/bin/bash "$TD/ok/launch/verdicts_steps_v2.sh" run | tail -n 1; echo "rc ${PIPESTATUS[0]}"
/bin/bash "$TD/ok/launch/verdicts_steps_v2.sh" after | tail -n 1; echo "rc ${PIPESTATUS[0]}"
echo "== the scrub in stderr: stderrroot's and uncaught's raws, their stderr sections"
sed -n '/^# stderr:/,$p' "$TD/stderrroot/launch/raw/"*_n-verdicts_out.txt
sed -n '/^# stderr:/,$p' "$TD/uncaught/launch/raw/"*_n-verdicts_out.txt
echo "== interrupted: its raw's marker line"
/usr/bin/grep -c '^# no exit status' "$TD/interrupted/launch/raw/"*_n-verdicts_out.txt
echo "== check on a fake root (ok's copy, check mode): expected FAIL, exit 1"
/bin/bash "$TD/ok/launch/verdicts_steps_v2.sh" check | /usr/bin/grep -c '^FAIL'; /bin/bash "$TD/ok/launch/verdicts_steps_v2.sh" check | tail -n 1
echo "== processes naming any run at the end: $(pgrep -f '[v]erdicts_steps_v2[.]sh inner' | wc -l | tr -d ' ')"
````

## 11. The v2 stand-in run on the final bytes (runs4)

`standin/standin_test_v2_runs4.log`, sha256 `2071db4226e361b0de6a8caad1557961b772ba4b099784b05e49dc37d9358811`, 124 lines in the kit.

````text
== the copy's diff from verdicts_steps_v2.sh (variant ok; the fake root and launch folder as <runs>)
29,30c29,30
< R=<repo>
< L=<scratch>/n9/verdicts
---
> R=<runs>/ok/repo
> L=<runs>/ok/launch
163c163
<   out=$(check)
---
>   out="check: ALL PASS"
== per variant: the three modes' exit codes, the stand-in's environment, and after's verdict lines
== ok: run rc 0, wait rc 0, after rc 0; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/ok/launch/tmp]
   after: ALL PASS
== refuse: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/refuse/launch/tmp]
   exit 2: a refusal (the analyzer writes nothing when it refuses) or a usage error
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== stop: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/stop/launch/tmp]
   exit 4: a STOP (any of the analyzer's STOPs; nothing written): for the seat through the PI
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== stderrroot: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/stderrroot/launch/tmp]
   exit 2: a refusal (the analyzer writes nothing when it refuses) or a usage error
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== uncaught: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/uncaught/launch/tmp]
   exit 1: an error the analyzer did not catch (its traceback in stderr); outputs may stand partial
   data/n/verdicts holds: [N-pod_secondary.json ]
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== interrupted: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/interrupted/launch/tmp]
   no exit status: the run was interrupted before the analyzer returned; outputs may stand partial
   data/n/verdicts holds: [N-pod_secondary.json ]
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== noglob: run rc 0, wait rc 0, after rc 1; env: none
   exit 97: the venv's glob matched no folder, or more than one; nothing ran
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== extra: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/extra/launch/tmp]
   FAIL stdout is 3 lines, not 2
== badsha: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/badsha/launch/tmp]
   FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one
== identical: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/identical/launch/tmp]
   FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one
   FAIL N-pod_secondary.json: not written, or its sha256 is not the printed one
== strayfile: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/strayfile/launch/tmp]
   FAIL data/n/verdicts holds [.N-pod_VERDICTS.json.1.tmp N-pod_VERDICTS.json N-pod_secondary.json ]
== homeout: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/homeout/launch/tmp]
   FAIL N-pod_VERDICTS.json: 1 lines name a local root
== homeraw: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/homeraw/launch/tmp]
   FAIL the home-prefix count over the raw is 1
== scratchraw: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/scratchraw/launch/tmp]
   FAIL 1 raw lines name a scratch or temporary path
== repocount: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/repocount/launch/tmp]
   FAIL the raw's INVOCATION line prints <repo> 6 times, not 7
== markeroff: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/markeroff/launch/tmp]
   FAIL the guard markers stand off the INVOCATION line, or it is missing
== pinmissing: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/pinmissing/launch/tmp]
   FAIL N-pod_VERDICTS.json does not bind data/n/gvec/gvec_cosines.json's sha256
== tmpleft: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/tmpleft/launch/tmp]
   FAIL tmp/ holds 1 names, or is missing
== errnonempty: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/errnonempty/launch/tmp]
   FAIL stderr is not empty
== ok: after.log whole
after: raw/2026-11-27_n-verdicts_out.txt: 5 lines, sha256 7f936fa6...bfed
PASS the home-prefix count over the raw is 0
PASS no scratch or temporary path in the raw
screen: raw lines with a guard marker (bracketed patterns): [4 ]; the INVOCATION line: [4 ]
PASS the guard markers stand on the INVOCATION line alone (its venv folder)
PASS stderr empty
PASS stdout is two lines
PASS line 1 is the INVOCATION line
PASS line 2 is the VERDICTS line
PASS the raw's INVOCATION line prints <repo> 7 times (the interpreter and six paths)
PASS data/n/verdicts holds the two outputs alone
PASS N-pod_VERDICTS.json written, sha256 09dcf290...300c as printed
PASS N-pod_secondary.json written, sha256 15c45488...5235 as printed
PASS N-pod_VERDICTS.json binds scripts/n_analyze.py's sha256 43609f39...e239
PASS N-pod_VERDICTS.json binds valence_core/n/schema.py's sha256 a75e96ad...5f40
PASS N-pod_VERDICTS.json binds LOCK-n.md's sha256 a6d36035...9112
PASS N-pod_VERDICTS.json binds data/n/reports/campaign.json's sha256 2d92dd10...fcde
PASS N-pod_VERDICTS.json binds data/n/gvec/gvec_cosines.json's sha256 88b50bb3...ffa9
PASS N-pod_VERDICTS.json binds data/n/gates/G-READ-n.json's sha256 ede912ab...9b92
PASS N-pod_VERDICTS.json binds the secondary's sha256
PASS N-pod_VERDICTS.json names no local root
PASS N-pod_secondary.json names no local root
PASS the ten pinned files still at their sha256s
PASS HEAD unchanged since launch
PASS valence_core/ and scripts/ still clean (by count)
PASS tmp/ empty
note: the sleep and wake counts unchanged during the run
outcome: VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS, PASS)
after: ALL PASS
after rc 0
== ok: the raw (cut at 160 columns)
# n package, N-pod's VERDICTS run of record (PROPOSAL-n v0.2 §8 step 15; the seat's raw of 2026-11-27 §5 item 1; the PI's routing of 2026-11-27, N item 5) on 
# environment at launch: bash 3.2.57(1)-release; macOS 15.6.1; hw.ncpu 14 | venv version_info = 3.12.9; numpy-2.5.1.dist-info; its python links to the base inte
# check at launch: check: ALL PASS
INVOCATION: <repo>/jlens-stand/.venv/bin/python <repo>/scripts/n_analyze.py verdicts --campaign <repo>/data/n/ckpt/campaign --report <repo>/data/n/reports/campa
VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS, PASS) -> N-pod_secondary.json (written; sha256 15c454887738d8c5087434e5837912c8c8198822907a13e92edc015ae34d5235
== ok: a second run and a second after both refuse
REFUSED: run/ exists: one run
rc 1
REFUSED: raw/2026-11-27_n-verdicts_out.txt exists
rc 1
== the scrub in stderr: stderrroot's and uncaught's raws, their stderr sections
# stderr:
REFUSED: cell <repo>/x; launch <launch>/y
# stderr:
Traceback (most recent call last):
  File "<repo>/scripts/n_analyze.py", line 1
OSError: stand-in
== interrupted: its raw's marker line
1
== check on a fake root (ok's copy, check mode): expected FAIL, exit 1
fatal: Not a valid object name 7ab1cf6
warning: could not open directory 'data/n/ckpt/': No such file or directory
fatal: bad revision '95cd461'
14
fatal: Not a valid object name 7ab1cf6
warning: could not open directory 'data/n/ckpt/': No such file or directory
fatal: bad revision '95cd461'
check: FAIL
== processes naming any run at the end: 0
````

## 12. The first v2 stand-in run (runs3), on v2 before its last fixes

`standin/standin_test_v2.log`, sha256 `956b050f3843b2a4a1f58f46f8a137eb8753d4ce9be8eef1905959c8c4e8476c`, 135 lines in the kit.

````text
== the copy's diff from verdicts_steps_v2.sh (variant ok; the fake root and launch folder as <runs>)
28,29c28,29
< R=<repo>
< L=<scratch>/n9/verdicts
---
> R=<runs>/ok/repo
> L=<runs>/ok/launch
162c162
<   out=$(check)
---
>   out="check: ALL PASS"
== per variant: the three modes' exit codes, the stand-in's environment, and after's verdict lines
== ok: run rc 0, wait rc 0, after rc 0; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/ok/launch/tmp]
   after: ALL PASS
== refuse: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/refuse/launch/tmp]
   exit 2: a refusal (the analyzer writes nothing when it refuses) or a usage error
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== stop: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/stop/launch/tmp]
   exit 4: a STOP (any of the analyzer's STOPs; nothing written): for the seat through the PI
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== stderrroot: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/stderrroot/launch/tmp]
   exit 2: a refusal (the analyzer writes nothing when it refuses) or a usage error
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== uncaught: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/uncaught/launch/tmp]
   exit 1: an error the analyzer did not catch (its traceback in stderr); outputs may stand partial
   data/n/verdicts holds: [N-pod_secondary.json ]
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== interrupted: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/interrupted/launch/tmp]
   FAIL stdout is 1 lines, not 2
   FAIL line 2 is not the VERDICTS line
   FAIL data/n/verdicts holds [N-pod_secondary.json ]
   FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one
   FAIL N-pod_secondary.json: not written, or its sha256 is not the printed one
   FAIL N-pod_VERDICTS.json does not bind scripts/n_analyze.py's sha256
   FAIL N-pod_VERDICTS.json does not bind valence_core/n/schema.py's sha256
   FAIL N-pod_VERDICTS.json does not bind LOCK-n.md's sha256
   FAIL N-pod_VERDICTS.json does not bind data/n/reports/campaign.json's sha256
   FAIL N-pod_VERDICTS.json does not bind data/n/gvec/gvec_cosines.json's sha256
   FAIL N-pod_VERDICTS.json does not bind data/n/gates/G-READ-n.json's sha256
   FAIL N-pod_VERDICTS.json does not bind the secondary's sha256
   FAIL N-pod_VERDICTS.json: ? lines name a local root
== noglob: run rc 0, wait rc 0, after rc 1; env: none
   FAIL 1 raw lines name a scratch or temporary path
   exit 98: cd into the venv's bin failed; nothing ran
   data/n/verdicts holds: []
   after: STOPPED at the raw; nothing is retried; to the coordinating session
== extra: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/extra/launch/tmp]
   FAIL stdout is 3 lines, not 2
== badsha: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/badsha/launch/tmp]
   FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one
== identical: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/identical/launch/tmp]
   FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one
   FAIL N-pod_secondary.json: not written, or its sha256 is not the printed one
== strayfile: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/strayfile/launch/tmp]
   FAIL data/n/verdicts holds [.N-pod_VERDICTS.json.1.tmp N-pod_VERDICTS.json N-pod_secondary.json ]
== homeout: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/homeout/launch/tmp]
   FAIL N-pod_VERDICTS.json: 1 lines name a local root
== homeraw: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/homeraw/launch/tmp]
   FAIL the home-prefix count over the raw is 1
== scratchraw: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/scratchraw/launch/tmp]
   FAIL 1 raw lines name a scratch or temporary path
== repocount: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/repocount/launch/tmp]
   FAIL the raw's INVOCATION line prints <repo> 6 times, not 7
== markeroff: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/markeroff/launch/tmp]
   FAIL the guard markers stand off the INVOCATION line, or it is missing
== pinmissing: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/pinmissing/launch/tmp]
   FAIL N-pod_VERDICTS.json does not bind data/n/gvec/gvec_cosines.json's sha256
== tmpleft: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/tmpleft/launch/tmp]
   FAIL tmp/ holds 1 names, or is missing
== errnonempty: run rc 0, wait rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/errnonempty/launch/tmp]
   FAIL stderr is not empty
== ok: after.log whole
after: raw/2026-11-27_n-verdicts_out.txt: 5 lines, sha256 b4a64575...ca26
PASS the home-prefix count over the raw is 0
PASS no scratch or temporary path in the raw
screen: raw lines with a guard marker (bracketed patterns): [4 ]; the INVOCATION line: [4 ]
PASS the guard markers stand on the INVOCATION line alone (its venv folder)
PASS stderr empty
PASS stdout is two lines
PASS line 1 is the INVOCATION line
PASS line 2 is the VERDICTS line
PASS the raw's INVOCATION line prints <repo> 7 times (the interpreter and six paths)
PASS data/n/verdicts holds the two outputs alone
PASS N-pod_VERDICTS.json written, sha256 09dcf290...300c as printed
PASS N-pod_secondary.json written, sha256 15c45488...5235 as printed
PASS N-pod_VERDICTS.json binds scripts/n_analyze.py's sha256 43609f39...e239
PASS N-pod_VERDICTS.json binds valence_core/n/schema.py's sha256 a75e96ad...5f40
PASS N-pod_VERDICTS.json binds LOCK-n.md's sha256 a6d36035...9112
PASS N-pod_VERDICTS.json binds data/n/reports/campaign.json's sha256 2d92dd10...fcde
PASS N-pod_VERDICTS.json binds data/n/gvec/gvec_cosines.json's sha256 88b50bb3...ffa9
PASS N-pod_VERDICTS.json binds data/n/gates/G-READ-n.json's sha256 ede912ab...9b92
PASS N-pod_VERDICTS.json binds the secondary's sha256
PASS N-pod_VERDICTS.json names no local root
PASS N-pod_secondary.json names no local root
PASS the ten pinned files still at their sha256s
PASS HEAD unchanged since launch
PASS valence_core/ and scripts/ still clean (by count)
PASS tmp/ empty
note: the sleep and wake counts unchanged during the run
outcome: VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS, PASS)
after: ALL PASS
after rc 0
== ok: the raw (cut at 160 columns)
# n package, N-pod's VERDICTS run of record (PROPOSAL-n v0.2 §8 step 15; the seat's raw of 2026-11-27 §5 item 1; the PI's routing of 2026-11-27, N item 5) on 
# environment at launch: bash 3.2.57(1)-release; macOS 15.6.1; hw.ncpu 14 | venv version_info = 3.12.9; numpy-2.5.1.dist-info; its python links to the base inte
# check at launch: check: ALL PASS
INVOCATION: <repo>/jlens-stand/.venv/bin/python <repo>/scripts/n_analyze.py verdicts --campaign <repo>/data/n/ckpt/campaign --report <repo>/data/n/reports/campa
VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS, PASS) -> N-pod_secondary.json (written; sha256 15c454887738d8c5087434e5837912c8c8198822907a13e92edc015ae34d5235
== ok: a second run and a second after both refuse
REFUSED: run/ exists: one run
rc 1
REFUSED: raw/2026-11-27_n-verdicts_out.txt exists
rc 1
== the scrub in stderr: stderrroot's and uncaught's raws, their stderr sections
# stderr:
REFUSED: cell <repo>/x
# stderr:
Traceback (most recent call last):
  File "<repo>/scripts/n_analyze.py", line 1
OSError: stand-in
== interrupted: its raw's marker line
0
== check on a fake root (ok's copy, check mode): expected FAIL, exit 1
fatal: Not a valid object name 7ab1cf6
warning: could not open directory 'data/n/ckpt/': No such file or directory
fatal: bad revision '95cd461'
14
fatal: Not a valid object name 7ab1cf6
warning: could not open directory 'data/n/ckpt/': No such file or directory
fatal: bad revision '95cd461'
check: FAIL
== processes naming any run at the end: 0
````

## 13. The steps file v1, as reviewed

`verdicts_steps.sh`, sha256 `445d65fbf25a62ddf8f2735bc388987949c5aa49898e72408caf6dbfa05cc681`, 183 lines in the kit.

````bash
#!/bin/bash
# verdicts_steps.sh v1 -- N-pod's VERDICTS run of record on the laptop, the n-analyzer session's launch file
# (PROPOSAL-n v0.2 s8 step 15; the seat's raw of 2026-11-27 (D) s5 item 1; the PI's routing of 2026-11-27, N item 5).
#
# Usage: bash verdicts_steps.sh check|run|after  -- each mode its own call, in this order, inside the window.
#   check  read-only, no interpreter: HEAD descends from 7ab1cf6; each of the six inputs untouched by git status,
#          its blob HEAD's, the working tree's and its commit of record's alike, and its sha256 the one in
#          inputs.sha256; data/n/verdicts absent; the venv's bin found by its glob with builtins alone; the venv's
#          python and numpy versions read from pyvenv.cfg and a dist-info name. Prints "check: ALL PASS" or exits 1.
#   run    the window's one interpreter process: scripts/n_analyze.py verdicts, foreground, nice 19, -I -B, TMPDIR in
#          this folder, absolute paths (the interpreter's cwd is the venv's bin), --date the laptop's calendar date at
#          launch. Writes run/{out,err,exit,date,head,secs}.txt. Refuses if run/ exists: one run.
#   after  read-only, no interpreter: builds the out raw (the root printed as <repo>) and screens it; then, on exit 0,
#          asserts stderr empty, stdout exactly the INVOCATION and VERDICTS lines, and data/n/verdicts holding the two
#          outputs alone, each "written" at the sha256 the VERDICTS line prints. A non-zero exit stops after the raw:
#          2 a refusal (nothing written), 4 a STOP (a pause or a fire: to the seat through the PI).
set -u
export LC_ALL=C
R=<repo>
L=<scratch>/n9/verdicts
W=$L/run
T=$L/tmp
V=$R/data/n/verdicts
BASE=7ab1cf6
INPUTS="scripts/n_analyze.py LOCK-n.md valence_core/n/schema.py data/n/gates/G-READ-n.json data/n/gvec/gvec_cosines.json data/n/reports/campaign.json"

rev_of() {   # each input's commit of record: the last commit that touched it
  case "$1" in
    scripts/n_analyze.py) echo b6ea27f ;;
    LOCK-n.md) echo 098218c ;;
    valence_core/n/schema.py) echo ef105f1 ;;
    data/n/gates/G-READ-n.json) echo 7ab1cf6 ;;
    data/n/gvec/gvec_cosines.json) echo e3b48ed ;;
    data/n/reports/campaign.json) echo 95cd461 ;;
    *) echo none ;;
  esac
}

abbr() { printf '%s...%s' "$(printf '%s' "$1" | cut -c1-8)" "$(printf '%s' "$1" | cut -c61-64)"; }

check() {
  local ok=1 p rev st h w o out rc names pv nv
  echo "check: the calendar date $(date +%F)"
  h=$(git -C "$R" rev-parse HEAD)
  if [ -n "$h" ] && git -C "$R" merge-base --is-ancestor "$BASE" HEAD; then
    echo "PASS HEAD $(printf '%s' "$h" | cut -c1-12) descends from $BASE"
  else
    echo "FAIL HEAD does not descend from $BASE"; ok=0
  fi
  for p in $INPUTS; do
    rev=$(rev_of "$p")
    st=$(git -C "$R" status --porcelain -- "$p")
    h=$(git -C "$R" rev-parse "HEAD:$p" 2>/dev/null)
    w=$(git -C "$R" hash-object -- "$p" 2>/dev/null)
    o=$(git -C "$R" rev-parse "$rev:$p" 2>/dev/null)
    if [ -z "$st" ] && [ -n "$h" ] && [ -n "$w" ] && [ -n "$o" ] && [ "$h" = "$w" ] && [ "$h" = "$o" ]; then
      echo "PASS $p: tracked, clean, the blob at $rev"
    else
      echo "FAIL $p: git status not empty, or HEAD's, the working tree's and $rev's blobs differ"; ok=0
    fi
  done
  names=$(cut -c67- "$L/inputs.sha256" | tr '\n' ' ')
  if [ "$names" = "$INPUTS " ]; then
    echo "PASS inputs.sha256 names the six inputs in order"
  else
    echo "FAIL inputs.sha256 does not name the six inputs in order"; ok=0
  fi
  out=$(cd "$R" && shasum -a 256 -c "$L/inputs.sha256" 2>&1); rc=$?
  printf '%s\n' "$out" | sed 's/^/  shasum: /'
  if [ "$rc" = 0 ] && [ "$(printf '%s\n' "$out" | /usr/bin/grep -c ': OK$')" = 6 ]; then
    echo "PASS the six sha256s are inputs.sha256's"
  else
    echo "FAIL the sha256s (shasum exit $rc)"; ok=0
  fi
  if [ -e "$V" ]; then
    echo "FAIL data/n/verdicts exists (the run expects it absent)"; ok=0
  else
    echo "PASS data/n/verdicts absent"
  fi
  if ( set -- "$R"/jl*/.venv/bin; [ $# -eq 1 ] && cd "$1" && [ -x ./python ] ); then
    echo "PASS the venv's bin: one match of its glob, ./python executable"
  else
    echo "FAIL the venv's bin: not one match of its glob, or no executable ./python"; ok=0
  fi
  pv=$( set -- "$R"/jl*/.venv; [ $# -eq 1 ] && cd "$1" && /usr/bin/grep -E '^version' pyvenv.cfg | head -n 1 )
  nv=$( set -- "$R"/jl*/.venv/lib/python3*/site-packages; [ $# -eq 1 ] && cd "$1" && ls -d numpy-*.dist-info )
  echo "env: pyvenv.cfg [$pv]; numpy [$nv]; macOS $(sw_vers -productVersion)"
  if [ "$ok" = 1 ]; then echo "check: ALL PASS"; return 0; fi
  echo "check: FAIL"; return 1
}

run() {
  local d h t0 t1 rc
  if [ -e "$W" ]; then echo "REFUSED: run/ exists: one run"; return 1; fi
  mkdir -p "$W" "$T" || return 1
  d=$(date +%F)
  h=$(git -C "$R" rev-parse HEAD)
  printf '%s\n' "$d" > "$W/date.txt"
  printf '%s\n' "$h" > "$W/head.txt"
  echo "run: the PI date $d; HEAD $(printf '%s' "$h" | cut -c1-12); launching the analyzer"
  t0=$(date +%s)
  ( set -- "$R"/jl*/.venv/bin; [ $# -eq 1 ] || exit 97; cd "$1" || exit 98
    TMPDIR="$T" nice -n 19 ./python -I -B "$R/scripts/n_analyze.py" verdicts \
      --campaign "$R/data/n/ckpt/campaign" --report "$R/data/n/reports/campaign.json" \
      --lock "$R/LOCK-n.md" --gread "$R/data/n/gates/G-READ-n.json" \
      --gvec "$R/data/n/gvec/gvec_cosines.json" --date "$d" ) > "$W/out.txt" 2> "$W/err.txt"
  rc=$?
  t1=$(date +%s)
  printf '%s\n' "$rc" > "$W/exit.txt"
  printf '%s\n' "$((t1 - t0))" > "$W/secs.txt"
  echo "run: ended, exit $rc, $((t1 - t0)) s; stdout $(wc -l < "$W/out.txt" | tr -d ' ') lines, stderr $(wc -c < "$W/err.txt" | tr -d ' ') bytes"
  return 0
}

after() {
  local f rc d h secs a raw ok=1 n l1 l2 c names sv ss gv gs
  for f in exit.txt date.txt head.txt secs.txt out.txt err.txt; do
    [ -f "$W/$f" ] || { echo "FAIL run/$f missing"; return 1; }
  done
  rc=$(cat "$W/exit.txt"); d=$(cat "$W/date.txt"); h=$(cat "$W/head.txt"); secs=$(cat "$W/secs.txt")
  a=$(sed -n 's|^\([0-9a-f]\{64\}\)  scripts/n_analyze.py$|\1|p' "$L/inputs.sha256")
  [ -n "$a" ] || { echo "FAIL no analyzer sha256 in inputs.sha256"; return 1; }
  mkdir -p "$L/raw"
  raw=$L/raw/${d}_n-verdicts_out.txt
  if [ -e "$raw" ]; then echo "REFUSED: raw/$(basename "$raw") exists"; return 1; fi
  {
    echo "# n package, N-pod's VERDICTS run of record (PROPOSAL-n v0.2 §8 step 15; the seat's raw of 2026-11-27 §5 item 1; the PI's routing of 2026-11-27, N item 5) on v7 (b6ea27f): scripts/n_analyze.py verdicts --campaign data/n/ckpt/campaign --report data/n/reports/campaign.json --lock LOCK-n.md --gread data/n/gates/G-READ-n.json --gvec data/n/gvec/gvec_cosines.json --date $d, the analyzer sha256 $a; HEAD $h; nice 19, -I -B, one invocation; exit $rc; stderr $(wc -c < "$W/err.txt" | tr -d ' ') bytes; $secs s. The repository's root is printed as <repo>."
    sed "s|$R|<repo>|g" "$W/out.txt"
    if [ -s "$W/err.txt" ]; then echo "# stderr:"; sed "s|$R|<repo>|g" "$W/err.txt"; fi
  } > "$raw"
  echo "after: raw/$(basename "$raw"): $(wc -l < "$raw" | tr -d ' ') lines, sha256 $(abbr "$(shasum -a 256 "$raw" | cut -d' ' -f1)")"
  c=$(/usr/bin/grep -c -F -- "$HOME" "$raw")
  if [ "$c" = 0 ]; then echo "PASS the home-prefix count over the raw is 0"; else echo "FAIL the home-prefix count over the raw is $c"; ok=0; fi
  c=$(/usr/bin/grep -c -F -e /private/ -e /tmp/ "$raw")
  if [ "$c" = 0 ]; then echo "PASS no scratch or temporary path in the raw"; else echo "FAIL $c raw lines name a scratch or temporary path"; ok=0; fi
  echo "screen: raw lines with a guard marker (bracketed patterns): $(/usr/bin/grep -c -i -e '[j]lens' -e '[q]wen' -e '[m]lx' -e '[o]lmo' -e '[i]pykernel' "$raw") (expected 1 on exit 0: the INVOCATION line's venv folder)"
  if [ "$rc" != 0 ]; then
    echo "after: STOPPED: exit $rc (2 a refusal, nothing written; 4 a STOP for the seat through the PI); stderr is in the raw; nothing is retried"
    return 1
  fi
  if [ -s "$W/err.txt" ]; then echo "FAIL stderr is not empty"; ok=0; else echo "PASS stderr empty"; fi
  n=$(wc -l < "$W/out.txt" | tr -d ' ')
  l1=$(sed -n 1p "$W/out.txt"); l2=$(sed -n 2p "$W/out.txt")
  if [ "$n" = 2 ]; then echo "PASS stdout is two lines"; else echo "FAIL stdout is $n lines, not 2"; ok=0; fi
  case "$l1" in "INVOCATION: "*) echo "PASS line 1 is the INVOCATION line" ;; *) echo "FAIL line 1 is not the INVOCATION line"; ok=0 ;; esac
  case "$l2" in "VERDICTS: ("*" -> "*) echo "PASS line 2 is the VERDICTS line" ;; *) echo "FAIL line 2 is not the VERDICTS line"; ok=0 ;; esac
  c=$(sed -n 2p "$raw" | /usr/bin/grep -o -F -- '<repo>' | wc -l | tr -d ' ')
  if [ "$c" = 7 ]; then echo "PASS the raw's INVOCATION line prints <repo> 7 times (the interpreter and six paths)"; else echo "FAIL the raw's INVOCATION line prints <repo> $c times, not 7"; ok=0; fi
  names=$(cd "$V" 2>/dev/null && ls -A | tr '\n' ' ')
  if [ "$names" = "N-pod_VERDICTS.json N-pod_secondary.json " ]; then
    echo "PASS data/n/verdicts holds the two outputs alone"
  else
    echo "FAIL data/n/verdicts holds [$names]"; ok=0
  fi
  sv=$(printf '%s\n' "$l2" | sed -n 's/.*N-pod_VERDICTS\.json (written; sha256 \([0-9a-f]\{64\}\)).*/\1/p')
  ss=$(printf '%s\n' "$l2" | sed -n 's/.*N-pod_secondary\.json (written; sha256 \([0-9a-f]\{64\}\)).*/\1/p')
  gv=$(cd "$V" 2>/dev/null && shasum -a 256 N-pod_VERDICTS.json | cut -d' ' -f1)
  gs=$(cd "$V" 2>/dev/null && shasum -a 256 N-pod_secondary.json | cut -d' ' -f1)
  if [ -n "$sv" ] && [ -n "$gv" ] && [ "$sv" = "$gv" ]; then
    echo "PASS N-pod_VERDICTS.json written, sha256 $(abbr "$gv") as printed"
  else
    echo "FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one"; ok=0
  fi
  if [ -n "$ss" ] && [ -n "$gs" ] && [ "$ss" = "$gs" ]; then
    echo "PASS N-pod_secondary.json written, sha256 $(abbr "$gs") as printed"
  else
    echo "FAIL N-pod_secondary.json: not written, or its sha256 is not the printed one"; ok=0
  fi
  for f in N-pod_VERDICTS.json N-pod_secondary.json; do
    c=$(cd "$V" 2>/dev/null && /usr/bin/grep -c -F -e "$HOME" -e /private/ -e /tmp/ "$f")
    if [ "$c" = 0 ]; then echo "PASS $f names no local root"; else echo "FAIL $f: $c lines name a local root"; ok=0; fi
  done
  echo "outcome: $(printf '%s\n' "$l2" | sed 's/ -> .*//')"
  if [ "$ok" = 1 ]; then echo "after: ALL PASS"; return 0; fi
  echo "after: FAIL"; return 1
}

case "${1:-}" in
  check) check ;;
  run) run ;;
  after) after ;;
  *) echo "usage: bash verdicts_steps.sh check, run or after"; exit 2 ;;
esac
````

## 14. The pins file v1

`inputs.sha256`, sha256 `50b1ae4fc5cf0d42d5db55d6be8fdbc78c00b7f2fd1b132cfe514fc7d4c7d907`, 6 lines in the kit.

````text
735da934272048a795203e8fdef9bfa5a4bde2ba38cdf9ba79d81f313788a7a8  scripts/n_analyze.py
59e0b1bcb364af06630753ba09fde127518c451e0aa679cea1d979d0ec9900aa  LOCK-n.md
1cab28df54c4c2c699b005fc6d2a99693d569911e292ad9dbdb8b6994db8edff  valence_core/n/schema.py
378f9972e942deb61ee4da74887e11556b625cdf41adfcfa4195636ccd31f519  data/n/gates/G-READ-n.json
fc8877be53194408cdcf7bbb09d1ec9ff3dfbe13b575bf6674190e3c03db0dad  data/n/gvec/gvec_cosines.json
1cabeadf9ee94d411d106a9cc306b29615d34bf41e0818f97bd1ed68dfc1c4e3  data/n/reports/campaign.json
````

## 15. The notes v1

`NOTES.md`, sha256 `a3eef767aa1e9c937702c9a45207917e3af20a15ae2f32a5add6c6d85b7c3680`, 88 lines in the kit.

````markdown
# N-pod VERDICTS: launch files v1 (the n-analyzer session), for the coordinating session's read

**Routing.** The PI's routing of 2026-11-27, section N item 5 [go] ("Route as given"), on the seat's raw (D)
`results/raw/2026-11-27_n-gread-record-read_design-to-code_answers.md` (sha256 6b5be7a3…e420, 81 lines; §5 item 1):
the n-analyzer session runs `scripts/n_analyze.py verdicts … --gread data/n/gates/G-READ-n.json` on the committed
artifact (378f9972…f519) with the analyzer at v7 (735da934…a7a8), then "— secondary DVs", issuing no claim; a pause
or a fire comes to the seat through the PI; Code adjudicates nothing.

**This folder** (my scratch): `verdicts_steps.sh` (the steps), `inputs.sha256` (the six pins), `standin/` (the
stand-in tests and their log), and this file. Their sha256s are in the message that carries this folder's path.

## The run (the `run` mode), exactly

```
( set -- <repo>/jl*/.venv/bin; [ $# -eq 1 ] || exit 97; cd "$1" || exit 98
  TMPDIR=<this folder>/tmp nice -n 19 ./python -I -B <repo>/scripts/n_analyze.py verdicts \
    --campaign <repo>/data/n/ckpt/campaign --report <repo>/data/n/reports/campaign.json \
    --lock <repo>/LOCK-n.md --gread <repo>/data/n/gates/G-READ-n.json \
    --gvec <repo>/data/n/gvec/gvec_cosines.json --date <date +%F at launch> ) > run/out.txt 2> run/err.txt
```

- `--campaign`: the 138 committed cell JSONs (95cd461), read by the analyzer alone (list v2 item 2); the arrays are
  outside the repository and their absence is no refusal (PIN-n-31; n_analyze.py:3166–3167).
- `--report`: `data/n/reports/campaign.json`, COMPLETE (1cabeadf…c4e3, the close list's first line).
- `--lock`: `LOCK-n.md`, v1.0 of record (59e0b1bc…00aa, the identity's lock_sha256; scripts/n_sessions.py pins it).
- `--gread`: `data/n/gates/G-READ-n.json`, the committed artifact (378f9972…f519), item 5's words.
- `--gvec`: `data/n/gvec/gvec_cosines.json` (fc8877be…0dad): LOCK-n.md L:711 and L:716–718 name it "the analyzer's
  `--gvec` file"; raw (D) §5 item 1's "the cosines" are VERDICTS' `cosines` (n_analyze.py:6747), null without it.
- `--date`: "the PI date of the run" (n_analyze.py:6804), the laptop's local calendar date at launch (`date +%F`),
  kept in run/date.txt.
- No `--out`: of record, `data/n/verdicts` (n_analyze.py:6633–6645). `verdicts_precheck` refuses unless the analyzer,
  the lock, the report, the artifact and the cosines file are each committed and clean at HEAD (committed_problems,
  n_analyze.py:5892–5906).
- Absolute paths, since the interpreter's cwd is the venv's bin (as at G-ANL-n's run, 2026-11-20).
- The six inputs' sha256s (inputs.sha256, written by `shasum` from the repository root) were each found whole in a
  committed source: the analyzer's in LOCK-n.md (2 lines), LOCK-n.md's in scripts/n_sessions.py (2), schema.py's in
  n_analyze.py (1, SCHEMA_SHA256) and LOCK-n.md (2), the artifact's in raw (D) (1), the cosines file's in LOCK-n.md
  (1, L:711), the report's in the close list (1, its first line).

## The window, in order, each its own call

1. `bash <this folder>/verdicts_steps.sh check`: read-only, no interpreter; it must print `check: ALL PASS`, or
   nothing runs and I report to you.
2. `bash <this folder>/verdicts_steps.sh run`: the window's one interpreter process, model-free (the cells' JSONs,
   B_BOOT 4,000; minutes at most is my expectation, not a measurement). I launch it through the Bash tool's
   background mode so no tool timeout can cut it; the end-wait is the tool's exit notice alone (list v2 item 5): no
   read of run/ or `data/n/verdicts` until the invocation has ended, and nothing else runs meanwhile.
3. `bash <this folder>/verdicts_steps.sh after`: read-only, no interpreter; on exit 0 it must print
   `after: ALL PASS` and the outcome tuple.

**Exits.** 0: `after`, then my report to you (the outcome tuple, the two outputs' sha256s). 2: a refusal before any
output (its message value-free by design): to you; nothing written, nothing retried. 4: a STOP (a pause or a fire;
nothing written, since both outputs are formed before either is written, n_analyze.py:6751 and :6772): to the seat
through the PI. 97 or 98: the venv's glob failed and nothing ran: to you. Any other: to you.

**What prints.** Two stdout lines: `INVOCATION:` (sys.executable and argv) and `VERDICTS:` (the tuple, the outputs'
names, how written and sha256s; no margin, n §4 "Blinding"); stderr empty. The INVOCATION line's interpreter path
holds the venv folder's name, two guard markers in output (never in an argv); the raw prints the repository's root as
`<repo>` and keeps that line otherwise as it is, as G-ANL-n's out raw does at 1641948.

**What my commands touch** (list v2). Nothing under `data/*/ckpt`: no content, listing or metadata; the analyzer
alone reads the cells. `data/n/reports/campaign.json`: `git status --porcelain` on its path, its blob ids (HEAD's,
the working tree's, 95cd461's) and its sha256 (item 1's digests); nothing printed from it. `data/n/verdicts`: a
test that it is absent (`check`); after the run, a name-only `ls -A`, `shasum` of the two outputs and a count of
local roots in them (`after`). The venv folder: entered by the builtin `cd` through its glob, so no exec's argv
names it; its python version read from pyvenv.cfg's `version` line and numpy's from its dist-info folder's name, no
interpreter. Every screen pattern naming a guard marker is bracketed.

**Done already, read-only and with no interpreter** (declared; my next entry's sweep carries the commands):
`bash -n` of the steps; `check` once on the real tree (2026-11-27, ALL PASS at HEAD 7ab1cf6; env: version_info
3.12.9, numpy 2.5.1, macOS 15.6.1); the stand-in tests (`standin/`; a bash script named `python` in fake roots under
this folder; nothing in the repository touched): 10 variants, each isolating one sub-condition. ok: ALL PASS.
refuse, stop: STOPPED at exits 2 and 4, stderr in the raw. extra, badsha, identical, strayfile, homeout, homeraw and
errnonempty: each FAILs on its own line alone. In every variant the stand-in saw argv -I -B, nice 19 and TMPDIR in
its launch folder, and a second `run` and a second `after` both refuse.

## After the run (each later, none now)

- The entry "PROPOSAL-n N-pod — VERDICTS" (n:161), carrying what raw (D) §5 item 1 lists: §5's sentences, G-LEAK-n's
  ceilings, the G-READ-n table (n_analyze.py:987–1000), the counters, the exposure counts realised, the cosines, and,
  where N1's label is "concluded, not answered", a dated note in raw (D) §2 item 6's figures; ledger (91) carried
  (raw (D) §2 item 5); then "— secondary DVs", issuing no claim. A blind values-check. The departures since my last
  entry's last sweep (it starts at transcript call 3546).
- One commit in its own window, by path: `.gitignore` (admitting `data/n/verdicts/` and its two outputs, in n's block
  beside `data/n/gates/`), `data/n/verdicts/N-pod_VERDICTS.json`, `data/n/verdicts/N-pod_secondary.json`,
  `results/raw/<date>_n-verdicts_out.txt`, `results/raw/<date>_n-verdicts-launch_review.md`,
  `results/raw/<date>_n-verdicts_valuescheck.md`, and `RESULTS.md` (the entry at the Log's head). Not pushed: the
  push is the PI's word.
````

## 16. The v1 stand-in for the venv's python

`standin/stand_python.in`, sha256 `1ba048686df76e84e56af1f4c26f8244fbb9da2ad5f7a6fbe4b9b217e58bfaec`, 31 lines in the kit.

````bash
#!/bin/bash
# stand-in for the venv's python, test only (no interpreter): prints what v7's verdicts prints (the INVOCATION line,
# sys.executable and argv without -I -B; then the VERDICTS line) and writes the two outputs; the variant is baked in.
R='__R__'
m='__MODE__'
printf 'argv12 [%s %s] nice [%s] TMPDIR [%s]\n' "$1" "$2" "$(ps -o nice= -p $$ | tr -d ' ')" "${TMPDIR:-}" > "$R/env.txt"
shift 2
extra=""
[ "$m" = homeraw ] && extra=" $HOME/x"
echo "INVOCATION: $PWD/python $*$extra"
case "$m" in
  refuse) echo "REFUSED: the stand-in refuses" >&2; exit 2 ;;
  stop) echo "STOP: the stand-in stops" >&2; exit 4 ;;
esac
mkdir -p "$R/data/n/verdicts"
printf '{"s": 1}\n' > "$R/data/n/verdicts/N-pod_secondary.json"
if [ "$m" = homeout ]; then
  printf '{"v": "%s"}\n' "$HOME" > "$R/data/n/verdicts/N-pod_VERDICTS.json"
else
  printf '{"v": 2}\n' > "$R/data/n/verdicts/N-pod_VERDICTS.json"
fi
[ "$m" = strayfile ] && printf 'x\n' > "$R/data/n/verdicts/.N-pod_VERDICTS.json.1.tmp"
a=$(shasum -a 256 "$R/data/n/verdicts/N-pod_secondary.json" | cut -d' ' -f1)
b=$(shasum -a 256 "$R/data/n/verdicts/N-pod_VERDICTS.json" | cut -d' ' -f1)
how=written
[ "$m" = identical ] && how=identical
[ "$m" = badsha ] && b=$(printf '%064d' 0)
echo "VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS) -> N-pod_secondary.json ($how; sha256 $a); N-pod_VERDICTS.json ($how; sha256 $b)"
[ "$m" = extra ] && echo "an extra line"
[ "$m" = errnonempty ] && echo "a warning" >&2
exit 0
````

## 17. The v1 stand-in harness

`standin/standin_test.sh`, sha256 `491cec3a7aaa1e1cd623c08226a2ec728568e16c66d763363cec773eb9cbb3d2`, 39 lines in the kit.

````bash
#!/bin/bash
# Stand-in tests of verdicts_steps.sh's run and after modes (no interpreter anywhere): each variant gets its own fake
# root holding a stand-in python at jl-stand/.venv/bin, and a copy of the steps file whose R= and L= lines alone are
# replaced (the diff is printed). The check mode is not exercised here: it ran on the real tree.
set -u
export LC_ALL=C
L=<scratch>/n9/verdicts
SI=$L/standin
TD=$SI/runs2
if [ -e "$TD" ]; then echo "runs2/ exists; make a new version"; exit 1; fi
mkdir -p "$TD"
for m in ok refuse stop extra badsha identical strayfile homeout homeraw errnonempty; do
  RR=$TD/$m/repo
  LL=$TD/$m/launch
  mkdir -p "$RR/jl-stand/.venv/bin" "$LL"
  cp "$L/inputs.sha256" "$LL/inputs.sha256"
  sed -e "s|__R__|$RR|" -e "s|__MODE__|$m|" "$SI/stand_python.in" > "$RR/jl-stand/.venv/bin/python"
  chmod +x "$RR/jl-stand/.venv/bin/python"
  sed -e "s|^R=.*|R=$RR|" -e "s|^L=.*|L=$LL|" "$L/verdicts_steps.sh" > "$LL/steps.sh"
  bash "$LL/steps.sh" run > "$LL/run.log" 2>&1
  echo "run rc $?" >> "$LL/run.log"
  bash "$LL/steps.sh" after > "$LL/after.log" 2>&1
  echo "after rc $?" >> "$LL/after.log"
done
echo "== the copy's diff from verdicts_steps.sh (variant ok; the fake root and launch folder abbreviated)"
diff "$L/verdicts_steps.sh" "$TD/ok/launch/steps.sh" | sed "s|$TD|<runs>|g"
for m in ok refuse stop extra badsha identical strayfile homeout homeraw errnonempty; do
  LL=$TD/$m/launch
  echo "== $m: $(tail -n 1 "$LL/run.log"), $(tail -n 1 "$LL/after.log"); env: $(sed "s|$TD|<runs>|g" "$TD/$m/repo/env.txt")"
  /usr/bin/grep -e '^FAIL' -e 'STOPPED' -e 'ALL PASS' -e '^REFUSED' "$LL/after.log" | sed 's/^/   /'
done
echo "== ok: after.log whole, and the raw (the fake root as <repo>)"
sed "s|$TD|<runs>|g" "$TD/ok/launch/after.log"
cat "$TD/ok/launch/raw/"*_n-verdicts_out.txt | cut -c1-200
echo "== ok: a second run and a second after both refuse"
bash "$TD/ok/launch/steps.sh" run; echo "rc $?"
bash "$TD/ok/launch/steps.sh" after; echo "rc $?"
echo "== refuse: the raw"
cat "$TD/refuse/launch/raw/"*_n-verdicts_out.txt | cut -c1-200
````

## 18. The v1 stand-in run, as frozen for the review (runs2)

`standin/standin_test_runs2.log`, sha256 `3236c0fc95f6ef4ddf81bf72abfa12e025482f61ef73482d51573c87b475c2a6`, 59 lines in the kit.

````text
== the copy's diff from verdicts_steps.sh (variant ok; the fake root and launch folder abbreviated)
19,20c19,20
< R=<repo>
< L=<scratch>/n9/verdicts
---
> R=<runs>/ok/repo
> L=<runs>/ok/launch
== ok: run rc 0, after rc 0; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/ok/launch/tmp]
   after: ALL PASS
== refuse: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/refuse/launch/tmp]
   after: STOPPED: exit 2 (2 a refusal, nothing written; 4 a STOP for the seat through the PI); stderr is in the raw; nothing is retried
== stop: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/stop/launch/tmp]
   after: STOPPED: exit 4 (2 a refusal, nothing written; 4 a STOP for the seat through the PI); stderr is in the raw; nothing is retried
== extra: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/extra/launch/tmp]
   FAIL stdout is 3 lines, not 2
== badsha: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/badsha/launch/tmp]
   FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one
== identical: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/identical/launch/tmp]
   FAIL N-pod_VERDICTS.json: not written, or its sha256 is not the printed one
   FAIL N-pod_secondary.json: not written, or its sha256 is not the printed one
== strayfile: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/strayfile/launch/tmp]
   FAIL data/n/verdicts holds [.N-pod_VERDICTS.json.1.tmp N-pod_VERDICTS.json N-pod_secondary.json ]
== homeout: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/homeout/launch/tmp]
   FAIL N-pod_VERDICTS.json: 1 lines name a local root
== homeraw: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/homeraw/launch/tmp]
   FAIL the home-prefix count over the raw is 1
== errnonempty: run rc 0, after rc 1; env: argv12 [-I -B] nice [19] TMPDIR [<runs>/errnonempty/launch/tmp]
   FAIL stderr is not empty
== ok: after.log whole, and the raw (the fake root as <repo>)
after: raw/2026-11-27_n-verdicts_out.txt: 3 lines, sha256 7d9ae9e4...ea15
PASS the home-prefix count over the raw is 0
PASS no scratch or temporary path in the raw
screen: raw lines with a guard marker (bracketed patterns): 0 (expected 1 on exit 0: the INVOCATION line's venv folder)
PASS stderr empty
PASS stdout is two lines
PASS line 1 is the INVOCATION line
PASS line 2 is the VERDICTS line
PASS the raw's INVOCATION line prints <repo> 7 times (the interpreter and six paths)
PASS data/n/verdicts holds the two outputs alone
PASS N-pod_VERDICTS.json written, sha256 59d20cc5...9581 as printed
PASS N-pod_secondary.json written, sha256 15c45488...5235 as printed
PASS N-pod_VERDICTS.json names no local root
PASS N-pod_secondary.json names no local root
outcome: VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS)
after: ALL PASS
after rc 0
# n package, N-pod's VERDICTS run of record (PROPOSAL-n v0.2 §8 step 15; the seat's raw of 2026-11-27 §5 item 1; the PI's routing of 2026-11-27, N item 5) on v7 (b6ea27f): scripts/n_analyze.py verdi
INVOCATION: <repo>/jl-stand/.venv/bin/python <repo>/scripts/n_analyze.py verdicts --campaign <repo>/data/n/ckpt/campaign --report <repo>/data/n/reports/campaign.json --lock <repo>/LOCK-n.md --gread <r
VERDICTS: (REPLICATED, DETECTABLE, SHARED, PASS) -> N-pod_secondary.json (written; sha256 15c454887738d8c5087434e5837912c8c8198822907a13e92edc015ae34d5235); N-pod_VERDICTS.json (written; sha256 59d20c
== ok: a second run and a second after both refuse
REFUSED: run/ exists: one run
rc 1
REFUSED: raw/2026-11-27_n-verdicts_out.txt exists
rc 1
== refuse: the raw
# n package, N-pod's VERDICTS run of record (PROPOSAL-n v0.2 §8 step 15; the seat's raw of 2026-11-27 §5 item 1; the PI's routing of 2026-11-27, N item 5) on v7 (b6ea27f): scripts/n_analyze.py verdi
INVOCATION: <repo>/jl-stand/.venv/bin/python <repo>/scripts/n_analyze.py verdicts --campaign <repo>/data/n/ckpt/campaign --report <repo>/data/n/reports/campaign.json --lock <repo>/LOCK-n.md --gread <r
# stderr:
REFUSED: the stand-in refuses
````

## 19. The window's steps as they printed, extracted verbatim from the transcript's tool results (calls 3810, 3812, 3814, 3818, 3822)

`review/window_outputs.md`, sha256 `c1d6673b971138869676889b0892a59fb2f8992a055c13f1288e319671b360c6`, 93 lines in the kit.

````markdown
### call 3810

manifest: 13 of 13 OK
inputs_v2.sha256: ec8cdd74…5f04
lid: "AppleClamshellState" = No
power: Now drawing from 'AC Power'; the calendar date 2026-11-27
Shell cwd was reset to <repo>

### call 3812

check: the calendar date 2026-11-27
PASS HEAD b23f91dbeb2b9a88b30695417bda9a44e3f8be0e descends from 7ab1cf6b55a8aa23792e69cafab737dcb4b39b52
PASS scripts/n_analyze.py: clean, HEAD's blob, last touched at b6ea27f4ad9154c8b0a6d16e8787437ee7d649e9
PASS LOCK-n.md: clean, HEAD's blob, last touched at 098218c07c67ac968648bb8e93a6c95796f16f1a
PASS valence_core/n/schema.py: clean, HEAD's blob, last touched at ef105f129740840eabcf87ffbb836e078ba9636d
PASS data/n/gates/G-READ-n.json: clean, HEAD's blob, last touched at 7ab1cf6b55a8aa23792e69cafab737dcb4b39b52
PASS data/n/gvec/gvec_cosines.json: clean, HEAD's blob, last touched at e3b48ed98d099bb70b7f8badd335de14007a70c8
PASS data/n/reports/campaign.json: clean, HEAD's blob, last touched at 95cd461e518628265eea500f4e6500bff5f912c9
PASS valence_core/__init__.py: clean, HEAD's blob, last touched at c5b8f1a63fe7e39067f91a657c1ea53cee98b1ed
PASS valence_core/adapters/__init__.py: clean, HEAD's blob, last touched at 1465b34c758edb258184fcac49b7776f57d65042
PASS valence_core/adapters/base.py: clean, HEAD's blob, last touched at 7da95097ea36618dbeb0eea0457ca8b667aa5080
PASS valence_core/n/__init__.py: clean, HEAD's blob, last touched at 5a975274463a3752cc70cdfee5dcfa62ebf3ab02
PASS inputs_v2.sha256 names the ten files in order
  shasum: scripts/n_analyze.py: OK
  shasum: LOCK-n.md: OK
  shasum: valence_core/n/schema.py: OK
  shasum: data/n/gates/G-READ-n.json: OK
  shasum: data/n/gvec/gvec_cosines.json: OK
  shasum: data/n/reports/campaign.json: OK
  shasum: valence_core/__init__.py: OK
  shasum: valence_core/adapters/__init__.py: OK
  shasum: valence_core/adapters/base.py: OK
  shasum: valence_core/n/__init__.py: OK
PASS the ten sha256s are inputs_v2.sha256's
PASS valence_core/ and scripts/ clean (git status, by count)
PASS the campaign's cell folder: 138 tracked, no other file, none changed since 95cd461 (names only, by count)
PASS data/n/verdicts absent
PASS run/ and tmp/ absent
PASS the venv's bin: one match of its glob, a physical path, ./python executable
PASS no process names the run, none is named python
PASS the five thread variables unset
PASS AC power
PASS Low Power Mode off (powermode 0)
PASS the venv's versions of record: version_info = 3.12.9; numpy-2.5.1.dist-info
check: ALL PASS
check exit: 0

### call 3814

run: launched under nohup caffeinate -is, PID 57594; the PI date 2026-11-27; HEAD b23f91dbeb2b9a88b30695417bda9a44e3f8be0e
run exit: 0

### call 3818

wait: the PID 57594 has ended; processes naming the run: 0
wait exit: 0

[exited with code 0]
exit.txt: 0

### call 3822

after: raw/2026-11-27_n-verdicts_out.txt: 39 lines, sha256 34f88cce...5ed8
PASS the home-prefix count over the raw is 0
PASS no scratch or temporary path in the raw
screen: raw lines with a guard marker (bracketed patterns): [38 ]; the INVOCATION line: [38 ]
PASS the guard markers stand on the INVOCATION line alone (its venv folder)
PASS stderr empty
PASS stdout is two lines
PASS line 1 is the INVOCATION line
PASS line 2 is the VERDICTS line
PASS the raw's INVOCATION line prints <repo> 7 times (the interpreter and six paths)
PASS data/n/verdicts holds the two outputs alone
PASS N-pod_VERDICTS.json written, sha256 4f29f294...68c0 as printed
PASS N-pod_secondary.json written, sha256 4133c48b...9c05 as printed
PASS N-pod_VERDICTS.json binds scripts/n_analyze.py's sha256 735da934...a7a8
PASS N-pod_VERDICTS.json binds valence_core/n/schema.py's sha256 1cab28df...edff
PASS N-pod_VERDICTS.json binds LOCK-n.md's sha256 59e0b1bc...00aa
PASS N-pod_VERDICTS.json binds data/n/reports/campaign.json's sha256 1cabeadf...c4e3
PASS N-pod_VERDICTS.json binds data/n/gvec/gvec_cosines.json's sha256 fc8877be...0dad
PASS N-pod_VERDICTS.json binds data/n/gates/G-READ-n.json's sha256 378f9972...f519
PASS N-pod_VERDICTS.json binds the secondary's sha256
PASS N-pod_VERDICTS.json names no local root
PASS N-pod_secondary.json names no local root
PASS the ten pinned files still at their sha256s
PASS HEAD unchanged since launch
PASS valence_core/ and scripts/ still clean (by count)
PASS tmp/ empty
note: the sleep and wake counts unchanged during the run
outcome: VERDICTS: (REPLICATED, DETECTABLE, SPECIFIC, PASS, PASS)
after: ALL PASS
after exit: 0

````
