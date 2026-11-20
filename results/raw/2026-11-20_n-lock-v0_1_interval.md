# n: LOCK-n v0.1 §21's retention intervals — the battery window and its shell cross-check (Code's rider)

*Code, PI date 2026-11-20. A rider to
[`2026-11-20_n-lock-v0_1_code-to-design_read.md`](2026-11-20_n-lock-v0_1_code-to-design_read.md), for LOCK-n v0.1
§21 (ADDENDUM-n3 §5.2's declaration): the 160 per-session retention intervals per span kind and their distribution,
by the package's own functions (`sessions.load_sessions`, `ids.load` and `ids.ids_of`, `Session.spans`,
`schema.ARM_SPAN_KIND`), in a battery window the coordinating session granted on 2026-11-20, run once under
`nice -n 19`; and a shell derivation of the same output, run before the window and outside any, which the window's
output equals byte for byte. In the commands, `<repo>` is the repository root, `<scratch>` Code's scratch folder,
and `<venv>` the interpreter's folder, reached by a glob in a `cd` so that no guard marker was in any argument;
nothing else is changed.*

## 1. The script, verbatim

`interval.py`, sha256 `6d143dc0c06785ab50076be13e083ae2e6651d0d515c13dc48e0c5f204aca766`, 63 lines. It is
model-free and writes nothing.

```python
"""LOCK-n v0.1, ADDENDUM-n3 s5.2: the retention intervals of record, the 160 per-session values per span kind, by the
package's own functions on committed inputs only (model-free; nothing written). argv[1] is the repository root.

Inputs, each asserted at load: the session set (sessions.load_sessions: BK's 14 skeleton files, their concatenation
schema.SESSION_SET_SHA256) and the ids of record (ids.load: data/n/ids/, each listed file's sha256 and record count
against MANIFEST.json), whose MANIFEST.json sha256 is asserted here to be ids.MANIFEST_OF_RECORD (G-VER's pin).

The interval as the primitive records it (primitive.read: read_position - (last span end - 1)): the read position
len(ids) - 1, ids the session's committed sequence (ids.ids_of, no told line), minus the last steered position,
session.spans(kind)[-1][1] - 1, for each steered span kind of schema.ARM_SPAN_KIND. Asserted per session: the
committed sequence's length is the session's seq_len and its ids_sha the session's. Prints the two pins; per kind its
arms, the sessions counted, min, median (statistics.median), max and the number of distinct values, then the count
at each value; the sessions per relation of the two kinds' intervals; the sha256 of the row lines joined by newline
(no trailing newline); and one row per session in the set's order. Never prints an id."""
import hashlib
import statistics
import sys
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root))
from valence_core.n import ids as ids_mod, schema, sessions  # noqa: E402

ss = sessions.load_sessions()
loaded = ids_mod.load()
if loaded["manifest_sha256"] != ids_mod.MANIFEST_OF_RECORD:
    raise SystemExit("MANIFEST.json is not the ids manifest of record -- refusing")
get = ids_mod.ids_of(loaded)
kinds = sorted({k for k in schema.ARM_SPAN_KIND.values() if k != "none"})
if kinds != ["S", "SU"]:
    raise SystemExit(f"steered span kinds {kinds}, not S and SU -- refusing")

rows = []
for s in ss:
    seq = get(s, None)
    if len(seq) != s.seq_len or sessions.ids_sha(seq) != s.ids_sha:
        raise SystemExit(f"{s.session_id}: the committed sequence is not the session's (length or ids_sha) -- refusing")
    rp = len(seq) - 1
    iv = {k: rp - (s.spans(k)[-1][1] - 1) for k in kinds}
    rows.append((s.session_id, iv, s.order[-1] == s.cue_S))

print(f"session set sha256 {sessions.session_set_sha256()}")
print(f"ids manifest sha256 {loaded['manifest_sha256']}")
print(f"sessions {len(rows)}")
for k in kinds:
    v = [iv[k] for _, iv, _ in rows]
    c = Counter(v)
    arms = " ".join(a for a in schema.ARMS if schema.ARM_SPAN_KIND[a] == k)
    print(f"kind {k}, arms {arms}: n {len(v)}, min {min(v)}, median {statistics.median(v)!r}, max {max(v)}, "
          f"values {len(c)}")
    for x in sorted(c):
        print(f"kind {k} value {x}: {c[x]} sessions")
eq = [r for r in rows if r[1]["S"] == r[1]["SU"]]
gt = [r for r in rows if r[1]["S"] > r[1]["SU"]]
lt = [r for r in rows if r[1]["S"] < r[1]["SU"]]
print(f"S equal to SU: {len(eq)} sessions, {sum(1 for r in eq if r[2])} of them with the 12th turn S")
print(f"S above SU: {len(gt)} sessions, {sum(1 for r in gt if not r[2])} of them with the 12th turn U")
print(f"S below SU: {len(lt)} sessions")
lines = [f"row {sid} S {iv['S']} SU {iv['SU']}" for sid, iv, _ in rows]
print(f"rows sha256 {hashlib.sha256(chr(10).join(lines).encode()).hexdigest()}")
for line in lines:
    print(line)
```

## 2. The window's command, run once

```bash
( cd <repo> && cd <venv>/bin && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TMPDIR=<scratch>/step4b/lock/tmp PYTHONDONTWRITEBYTECODE=1 nice -n 19 ./python <scratch>/step4b/lock/interval.py <repo> ) > <scratch>/step4b/lock/interval_run1.txt 2>&1; echo "exit $?" > <scratch>/step4b/lock/interval_run1.exit

```

Its exit line (`interval_run1.exit`): `exit 0`. Its output (`interval_run1.txt`), 178 lines, sha256
`ad82c1b79e62fe2e973eeef26d2a1b6f1652bf0480b2a4d756bfb8e5c46b7660`, is committed byte for byte as
[`2026-11-20_n-lock-v0_1_interval_out.txt`](2026-11-20_n-lock-v0_1_interval_out.txt): the two pins, the distribution
per span kind, the S-against-SU lines, and the 160 rows `row {session} S {S} SU {SU}`.

## 3. The shell cross-check, verbatim

`interval_shell.sh`, sha256 `306388bf08ebfcfbda0176f84a87a5151d67059a7509ed8a87ab0a1fe63a7184`, 60 lines (bash, jq,
awk, sort, uniq, shasum; no Python). It reaches the 14 skeleton files by `cd` and a glob, so that no folder name is in
any argument.

```bash
#!/bin/bash
# LOCK-n v0.1, ADDENDUM-n3 s5.2: interval.py's output derived in shell with no Python (jq, awk, sort, uniq, shasum),
# for a diff against the window's output. $1 the repository root; $2 the expected-output file to write; $3 a
# scratch folder for the parts. Reads the 14 skeleton files (cd + glob, so no folder name in any argv),
# data/n/ids/MANIFEST.json and data/n/ids/sessions.jsonl. Never prints an id.
set -euo pipefail
ROOT=$1; EXP=$2; W=$3
mkdir -p "$W"
CELLS=(floor_b0 floor_b1 floor_b2 floor_b3 floor_b4 floor_b5 floor_b6 floor_b7 neu_b0 neu_b1 neu_b2 neu_b3 neu_b4 neu_b5)

cd "$ROOT"/data/n/bk/experiment_results_json/fixed_text_design/skeletons/ol*_32b/neutral
n_files=$(ls | /usr/bin/grep -c '\.sessions\.jsonl$')
[ "$n_files" = 14 ] || { echo "skeleton files: $n_files, not 14" >&2; exit 1; }
set_sha=$(for c in "${CELLS[@]}"; do cat "$c.sessions.jsonl"; done | shasum -a 256 | cut -d' ' -f1)
: > "$W/skel.txt"
for c in "${CELLS[@]}"; do
  jq -r --arg cell "$c" '.seq_len as $n | .cue_S as $cs
    | ([.turn_spans[] | select(.[2] == $cs)] | last | .[1]) as $e
    | "\($cell)/\(.run) \($n) \(.ids_sha) \($n - $e) \($n - .n_pre) \(.order[-1] == $cs)"' "$c.sessions.jsonl" \
    >> "$W/skel.txt"
done

cd "$ROOT"
man_sha=$(shasum -a 256 data/n/ids/MANIFEST.json | cut -d' ' -f1)
ses_sha=$(shasum -a 256 data/n/ids/sessions.jsonl | cut -d' ' -f1)
man_ses=$(jq -r '.files["sessions.jsonl"].sha256' data/n/ids/MANIFEST.json)
[ "$ses_sha" = "$man_ses" ] || { echo "sessions.jsonl is not MANIFEST.json's" >&2; exit 1; }
jq -r '"\(.session_id) \(.ids | length) \(.ids_sha)"' data/n/ids/sessions.jsonl > "$W/ids_meta.txt"
jq -r '.ids | map(tostring) | "[" + join(", ") + "]"' data/n/ids/sessions.jsonl \
  | while IFS= read -r line; do printf '%s' "$line" | shasum -a 256 | cut -c1-16; done > "$W/ids_resha.txt"
paste -d' ' "$W/ids_meta.txt" "$W/ids_resha.txt" > "$W/ids.txt"
awk 'NR == FNR { len[$1] = $2; rec[$1] = $3; re[$1] = $4; n++; next }
     { m++; if (!($1 in len) || len[$1] != $2 || rec[$1] != $3 || re[$1] != $3) { print "mismatch " $1; bad = 1 } }
     END { if (n != 160 || m != 160) { print "counts " n " " m; bad = 1 }; exit bad }' "$W/ids.txt" "$W/skel.txt" >&2

awk '{ print "row " $1 " S " $4 " SU " $5 }' "$W/skel.txt" > "$W/rows.txt"
rows_sha=$(printf '%s' "$(cat "$W/rows.txt")" | shasum -a 256 | cut -d' ' -f1)

{
  echo "session set sha256 $set_sha"
  echo "ids manifest sha256 $man_sha"
  echo "sessions $(wc -l < "$W/skel.txt" | tr -d ' ')"
  for k in S SU; do
    if [ "$k" = S ]; then col=4; arms="N1-V N1-R N2-E N2-S N2-C"; else col=5; arms="N1-P"; fi
    awk -v c="$col" '{ print $c }' "$W/skel.txt" | sort -n > "$W/v_$k.txt"
    n=$(wc -l < "$W/v_$k.txt" | tr -d ' ')
    mn=$(head -1 "$W/v_$k.txt"); mx=$(tail -1 "$W/v_$k.txt")
    md=$(awk -v n="$n" 'NR == n / 2 { a = $1 } NR == n / 2 + 1 { b = $1 } END { printf "%.1f", (a + b) / 2 }' "$W/v_$k.txt")
    uniq -c "$W/v_$k.txt" | awk '{ print $2 " " $1 }' > "$W/c_$k.txt"
    echo "kind $k, arms $arms: n $n, min $mn, median $md, max $mx, values $(wc -l < "$W/c_$k.txt" | tr -d ' ')"
    awk -v k="$k" '{ print "kind " k " value " $1 ": " $2 " sessions" }' "$W/c_$k.txt"
  done
  awk '$4 == $5 { e++; if ($6 == "true") es++ } $4 > $5 { g++; if ($6 == "false") gu++ } $4 < $5 { l++ }
       END { printf "S equal to SU: %d sessions, %d of them with the 12th turn S\n", e, es;
             printf "S above SU: %d sessions, %d of them with the 12th turn U\n", g, gu;
             printf "S below SU: %d sessions\n", l }' "$W/skel.txt"
  echo "rows sha256 $rows_sha"
  cat "$W/rows.txt"
} > "$EXP"
echo "expected output: $(wc -l < "$EXP" | tr -d ' ') lines"
```

It ran before the window as `bash <scratch>/step4b/lock/interval_shell.sh <repo>
<scratch>/step4b/lock/interval_expected.txt <scratch>/step4b/lock/interval_shell_parts`, writing
`interval_expected.txt` (178 lines, sha256 `ad82c1b79e62fe2e973eeef26d2a1b6f1652bf0480b2a4d756bfb8e5c46b7660`, kept
in Code's scratch). It was re-run for this record on 2026-11-20, with the two output paths in a new scratch folder:
exit 0, its stdout the one line `expected output: 178 lines`, its file byte for byte the first's (`cmp`).

## 4. The comparison

`diff interval_run1.txt interval_expected.txt` is empty (`interval_run1.diff`, 0 bytes), and `cmp` finds the two
files equal: the window's output is the shell derivation's, byte for byte.
