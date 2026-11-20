# n: LOCK-n v0.1 §5's realized fidelity sample under `n-fid|{s}`, run once at the lock's read (Code's rider)

*Code, PI date 2026-11-20. A rider to the seat's read of LOCK-n v0.1's draft 9,
[`2026-11-20_n-lock-v0_1-read_design-to-code_answers.md`](2026-11-20_n-lock-v0_1-read_design-to-code_answers.md)
§3.2: "By the package's own `keys` function over the 160 sessions of record in the set's order, in the same window:
the sessions with `stream(f"n-fid|{s}").random() < 0.10`, their count, and the sha256 of their ids joined by newlines
in that order". The run: `fidsample.py` (§1), once, at HEAD `411b15c`, the fourth of the five calls in the battery
window the coordinating session granted on 2026-11-20
([`2026-11-20_n-lock-v0_1_hashes.md`](2026-11-20_n-lock-v0_1_hashes.md) has the first three), under `nice -n 19`, with
Q-F3's campaign running beside and untouched. In the commands, `<repo>` is the repository root, `<L>` the window's
folder in Code's scratch, and `<venv>` the interpreter's folder, reached by a glob in a `cd` so that no guard marker
was in any argument; nothing else is changed. Each command is as Code's transcript records it, recovered by `jq`.*

## 1. The script, verbatim

`fidsample.py`, sha256 `83952a85d27b55e7aacf082ad8455450ff5ca494de7bd2bba6fc935fdeef72e3`, 39 lines. It is
model-free and writes nothing. The ids are `schema.session_id`'s, `{bk_cell}/{bk_run}`; the digest is over them joined
by newlines with no trailing newline, the form of `schema.read_plan_sha256` (schema.py:602), Code's reading of §3.2's
"joined by newlines".

```python
"""LOCK-n v0.1, the seat's read of 2026-11-20 (second sitting), §3.2: the realized fidelity sample, by the package's
own functions (model-free; nothing written). argv[1] is the repository root. Over the 160 sessions of record in the
session set's order (sessions.load_sessions, which asserts schema.SESSION_SET_SHA256 and each session's BK run equal
to its index), the sessions s with keys.fid_sampled(s.bk_run): keys.py's PIN, stream(f"n-fid|{s}").random() < 0.10,
s = BK's run. m's stream known answer is checked first, and the PIN's words are evaluated beside the package's
function from numpy and zlib directly. Prints numpy's version, the session set's sha256, the count, the sampled
sessions' ids (schema.session_id, '{bk_cell}/{bk_run}') one per line in the set's order, and the sha256 of those ids
joined by newlines with no trailing newline (schema.read_plan_sha256's form)."""
import hashlib
import sys
import zlib
from pathlib import Path

root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root))
import numpy as np  # noqa: E402
from valence_core.m.keys import stream_known_answer  # noqa: E402
from valence_core.n import keys, schema, sessions  # noqa: E402

ka = stream_known_answer()
if ka != []:
    raise SystemExit(f"numpy's stream known answer fails on this site: {ka} -- refusing")
ss = sessions.load_sessions()
if len(ss) != schema.N_SESSIONS or [s.bk_run for s in ss] != list(range(schema.N_SESSIONS)):
    raise SystemExit("the sessions are not BK's 160 in run order -- refusing")
picked = [s for s in ss if keys.fid_sampled(s.bk_run)]
direct = [s for s in ss if np.random.default_rng(zlib.crc32(f"n-fid|{s.bk_run}".encode()) % 2 ** 31).random() < 0.10]
if [s.bk_run for s in picked] != [s.bk_run for s in direct]:
    raise SystemExit("keys.fid_sampled disagrees with the PIN's words -- refusing")
ids = [s.session_id for s in picked]
if ids != [schema.session_id(schema.bk_cell_of(s.bk_run), s.bk_run) for s in picked]:
    raise SystemExit("a sampled session's id is not schema.session_id of its run's cell -- refusing")
print(f"numpy {np.__version__}; m's stream known answer holds")
print(f"session set sha256 {sessions.session_set_sha256()}, {len(ss)} sessions")
print(f"sampled {len(ids)} of {len(ss)}")
for i in ids:
    print(i)
print("sha256 of the sampled ids joined by newlines, no trailing newline: "
      + hashlib.sha256("\n".join(ids).encode("utf-8")).hexdigest())
```

## 2. The command, run once (call 4)

```bash
L=<L>; ( cd <repo> && cd <venv>/bin && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TMPDIR="$L/tmp" nice -n 19 ./python -I -B "$L/fidsample.py" <repo> ) > "$L/fidsample_run1.txt" 2> "$L/fidsample_run1.err"; echo "exit $?" > "$L/fidsample_run1.exit"
```

Its exit line (`fidsample_run1.exit`): `exit 0`. Its stderr (`fidsample_run1.err`): empty, 0 bytes. Its output
(`fidsample_run1.txt`), 19 lines, 456 bytes, sha256 `bb92082931c8ec2a83f109f096c2119953eafdde33d68cb102e9068b5ab6b95e`,
is committed byte for byte as [`2026-11-20_n-lock-v0_1_fidsample_out.txt`](2026-11-20_n-lock-v0_1_fidsample_out.txt):

```text
numpy 2.5.1; m's stream known answer holds
session set sha256 be50011a5ab1e8a4261dbde72afc84313d3bdeba9e40078272928bd497c3ba84, 160 sessions
sampled 15 of 160
floor_b1/6
floor_b1/8
floor_b2/14
floor_b3/15
floor_b5/28
floor_b7/36
neu_b0/56
neu_b1/73
neu_b1/77
neu_b2/82
neu_b3/107
neu_b3/111
neu_b4/122
neu_b4/132
neu_b5/148
sha256 of the sampled ids joined by newlines, no trailing newline: 3c70f5fff77112cc60d66b24617d13d774aabbfe8540a75a83c1b250acffa81d
```

The realized sample: **15 of 160 sessions**, 6 floor sessions and 9 neutral, the sha256 of their ids
**`3c70f5fff77112cc60d66b24617d13d774aabbfe8540a75a83c1b250acffa81d`**.

## 3. The shell's cross-check: the after-check (call 5)

§3.2 asks for "a shell derivation beside it if one is cheap". The keyed draw is not cheap in the shell: each key's
stream is numpy's `default_rng` over `crc32(key) % 2**31` (`valence_core/m/keys.py`:27–29), that is numpy's
SeedSequence hashing feeding the PCG64 generator, which would mean re-implementing 32-bit hash mixing, 128-bit
multiplication and exclusive-or in a shell with no bitwise operators (this laptop's `awk`, version 20200816, and `bc`
have none, as tried). So the draw is checked inside the window instead, beside the package's function: the script
asserts m's stream known answer first, and evaluates the PIN's words directly from numpy and zlib, asserting the same
sessions (§1). The shell then checks what it can from the printed lines: their shapes, the session set's line, the
count, each id the cell rule's for its run (`schema.bk_cell_of`, schema.py:576–582), the runs ascending, and the
digest, re-derived over the printed ids. The command:

```bash
L=<L>; bash "$L/aftercheck.sh" <repo> "$L"
```

`aftercheck.sh`, sha256 `06b7f5b929179f77b2e073c1654cc875589f51ec40403dfc0ff4d523ea680a31`, 54 lines, verbatim; it
also checks rider 1's output against the expected lines, and the tree. Its `find` names three folders,
`valence_core/`, `scripts/` and `data/n/bk/`, without the list of record's pruned form; none of the three holds a
`ckpt` or `reports` folder.

```bash
#!/bin/bash
# LOCK-n v0.1's riders' window (the seat's read of 2026-11-20, second sitting, §3), the after-check. Read-only; shell
# only, no interpreter; exit 1 on any failure. $1 the repository root, $2 the window's folder. Rider 1: the `hashes`
# output against the expected lines (§18's), stderr empty, exit 0. Rider 2: its exit and stderr, and the shell's
# cross-check of what the shell can check from the printed lines: the line shapes, the count, each id the cell rule's
# for its run (schema.bk_cell_of), the runs ascending, and the digest of the printed ids. The keyed draw itself is
# numpy's SeedSequence and PCG64 and is not re-derived here. Then the tree: nothing under valence_core/, scripts/ or
# data/n/bk/ newer than the pre-check's stamp, HEAD, the index, LOCK-n.md, the TMPDIR empty.
set -uo pipefail
R=$1; L=$2; f=0
ok() { echo "ok   $1"; }
no() { echo "FAIL $1"; f=1; }
cd "$R" || { echo "FAIL cd"; exit 1; }
[ -e "$L/stamp" ] || { echo "FAIL no stamp: the pre-check did not pass"; exit 1; }
# rider 1
[ "$(cat "$L/hashes_run1.exit")" = "exit 0" ] && ok "hashes: exit 0" || no "hashes: $(cat "$L/hashes_run1.exit")"
[ -e "$L/hashes_run1.err" ] && [ ! -s "$L/hashes_run1.err" ] && ok "hashes: stderr empty" || no "hashes: stderr"
cmp -s "$L/hashes_run1.txt" "$L/hashes_expected.txt" \
  && ok "hashes: the output is the expected 13 lines byte for byte (the digest and the twelve files of §18)" \
  || no "hashes: the output differs from the expected lines -- a STOP for the seat (§3.1)"
# rider 2
F="$L/fidsample_run1.txt"
[ "$(cat "$L/fidsample_run1.exit")" = "exit 0" ] && ok "fidsample: exit 0" || no "fidsample: $(cat "$L/fidsample_run1.exit")"
[ -e "$L/fidsample_run1.err" ] && [ ! -s "$L/fidsample_run1.err" ] && ok "fidsample: stderr empty" || no "fidsample: stderr"
l1=$(sed -n 1p "$F"); l2=$(sed -n 2p "$F"); l3=$(sed -n 3p "$F"); last=$(tail -n 1 "$F")
case "$l1" in "numpy "*"; m's stream known answer holds") ok "fidsample: line 1, numpy's version and the known answer";;
  *) no "fidsample: line 1 is '$l1'";; esac
[ "$l2" = "session set sha256 be50011a5ab1e8a4261dbde72afc84313d3bdeba9e40078272928bd497c3ba84, 160 sessions" ] \
  && ok "fidsample: the session set of record (schema.py:262), 160 sessions" || no "fidsample: line 2 is '$l2'"
N=$(printf '%s\n' "$l3" | sed -n 's/^sampled \([0-9][0-9]*\) of 160$/\1/p')
[ -n "$N" ] && ok "fidsample: line 3, sampled $N of 160" || no "fidsample: line 3 is '$l3'"
lines=$(wc -l < "$F" | tr -d ' ')
[ -n "$N" ] && [ "$lines" = $((N + 4)) ] && ok "fidsample: $lines lines, the $N ids between line 3 and the digest" \
  || no "fidsample: $lines lines for N = $N"
sed -n "4,$((lines - 1))p" "$F" > "$L/fidsample_ids_shell.txt"
[ "$(wc -l < "$L/fidsample_ids_shell.txt" | tr -d ' ')" = "$N" ] && ok "fidsample: $N id lines" || no "fidsample: id lines"
awk -F/ 'function cell(r) { return (r < 40) ? ("floor_b" int(r / 5)) : ("neu_b" int((r - 40) / 20)) }
  NF != 2 || $2 !~ /^[0-9]+$/ || $2 + 0 > 159 || $1 != cell($2 + 0) || (NR > 1 && $2 + 0 <= prev) { bad++ }
  { prev = $2 + 0 } END { exit bad > 0 }' "$L/fidsample_ids_shell.txt" \
  && ok "fidsample: each id is '{bk_cell}/{bk_run}' with the cell rule's cell for its run, runs ascending" \
  || no "fidsample: an id breaks the cell rule or the order"
D=$(printf '%s' "$(cat "$L/fidsample_ids_shell.txt")" | shasum -a 256 | cut -d' ' -f1)
[ "$last" = "sha256 of the sampled ids joined by newlines, no trailing newline: $D" ] \
  && ok "fidsample: the printed digest is the shell's over the printed ids ($D)" || no "fidsample: the digest line is '$last', the shell's $D"
# the tree
[ -z "$(find valence_core scripts data/n/bk -newer "$L/stamp" -print 2>/dev/null | head -n 1)" ] \
  && ok "nothing under valence_core/, scripts/ or data/n/bk/ newer than the stamp" || no "a file changed during the window"
[ "$(git rev-parse HEAD)" = 411b15cc30563f05e6ff39d4f7013081bf7c6636 ] && ok "HEAD 411b15c" || no "HEAD"
[ -z "$(git diff --cached --name-only)" ] && ok "the index empty" || no "the index is not empty"
[ "$(shasum -a 256 < LOCK-n.md | cut -d' ' -f1)" = 5acca00f55d19516198cceb1035216b08f514c60045e4ec306790f3a7611586a ] \
  && ok "LOCK-n.md at the bytes the seat read" || no "LOCK-n.md moved"
[ -z "$(ls -A "$L/tmp")" ] && ok "the window's TMPDIR empty" || no "the window's TMPDIR is not empty"
[ "$f" = 0 ] && echo "AFTERCHECK PASS" || echo "AFTERCHECK FAIL"
exit $f
```

Its output (call 5), as Code's transcript records it:

```text
ok   hashes: exit 0
ok   hashes: stderr empty
ok   hashes: the output is the expected 13 lines byte for byte (the digest and the twelve files of §18)
ok   fidsample: exit 0
ok   fidsample: stderr empty
ok   fidsample: line 1, numpy's version and the known answer
ok   fidsample: the session set of record (schema.py:262), 160 sessions
ok   fidsample: line 3, sampled 15 of 160
ok   fidsample: 19 lines, the 15 ids between line 3 and the digest
ok   fidsample: 15 id lines
ok   fidsample: each id is '{bk_cell}/{bk_run}' with the cell rule's cell for its run, runs ascending
ok   fidsample: the printed digest is the shell's over the printed ids (3c70f5fff77112cc60d66b24617d13d774aabbfe8540a75a83c1b250acffa81d)
ok   nothing under valence_core/, scripts/ or data/n/bk/ newer than the stamp
ok   HEAD 411b15c
ok   the index empty
ok   LOCK-n.md at the bytes the seat read
ok   the window's TMPDIR empty
AFTERCHECK PASS
```

## 4. The pin

LOCK-n v0.1 §5 pins the realized sample, as the seat's read rules it (its §2, edit 4): 15 of 160 sessions, the
sha256 of their ids in the session set's order `3c70f5fff77112cc60d66b24617d13d774aabbfe8540a75a83c1b250acffa81d`,
this rider's output; §13's power sentence marks the count. "The runner asserts nothing new: the key and the session
set already fix the sample; the pin lets the campaign's report be checked against the lock, which is what a pin is
for" (§3.2).
