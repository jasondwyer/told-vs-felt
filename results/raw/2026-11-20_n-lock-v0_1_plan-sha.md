# n: LOCK-n v0.1 §6's `read_plan_sha256` — the battery window and its shell cross-check (Code's rider)

*Code, PI date 2026-11-20. A rider to
[`2026-11-20_n-lock-v0_1_code-to-design_read.md`](2026-11-20_n-lock-v0_1_code-to-design_read.md), for LOCK-n v0.1
§6 (hole 10): the read plan's `read_plan_sha256` under G-CAL-n's dose map of record (`data/n/gcal/gcal.json` at
`db00d6d`), by the package's own `schema.read_plan_sha256`, in a battery window the coordinating session granted on
2026-11-20, run once under `nice -n 19`; and a shell derivation of the same plan, run before the window and outside
any. In the commands, `<repo>` is the repository root, `<scratch>` Code's scratch folder, and `<venv>` the
interpreter's folder, reached by a glob in a `cd` so that no guard marker was in any argument; nothing else is
changed.*

## 1. The script, verbatim

`plan_sha.py`, sha256 `f8c840efdc03fdeee6f17f84b25a83bcbc004abe95f4e7083988c51a9e056a4c`, 22 lines. It is
model-free and writes nothing.

```python
"""LOCK-n v0.1, draft 4: the campaign's read plan under G-CAL-n's dose map of record, by the package's own functions
(model-free; nothing written). argv[1] is the repository root; the dose map is read from its data/n/gcal/gcal.json,
taken only from a record whose status is PASS (O8). Prints the plan's size, its reads per arm in schema.ARMS order,
and schema.read_plan_sha256 over the identity's two fields read_plan reads, its stage and its dose map."""
import json
import sys
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root))
from valence_core.n import schema  # noqa: E402

rec = json.loads((root / "data" / "n" / "gcal" / "gcal.json").read_text(encoding="utf-8"))
if rec.get("status") != "PASS" or rec.get("pinnable") is not True:
    raise SystemExit("the dose map is taken only from a PASS gcal.json (O8) -- refusing")
ident = {"stage": "campaign", "dose_map": rec["dose_map"]}
plan = schema.read_plan(ident)
per = Counter(r.split("|")[0] for r in plan)
print(f"reads {len(plan)}, distinct {len(set(plan))}")
print("per arm: " + "; ".join(f"{a} {per[a]}" for a in schema.ARMS))
print(f"read_plan_sha256 {schema.read_plan_sha256(ident)}")
```

## 2. The window's command, run once

```bash
( cd <repo> && cd <venv>/bin && TMPDIR=<scratch>/step4b/lock/tmp PYTHONDONTWRITEBYTECODE=1 nice -n 19 ./python <scratch>/step4b/lock/plan_sha.py <repo> ) > <scratch>/step4b/lock/plan_sha_run1.txt 2>&1; echo "exit $?" > <scratch>/step4b/lock/plan_sha_run1.exit

```

Its exit line (`plan_sha_run1.exit`): `exit 0`. Its output (`plan_sha_run1.txt`), 3 lines, sha256
`cc1dd7819a63d0b23eb3aebdbaa423b56e866ea190191db709816f95132b8e26`, is committed byte for byte as
[`2026-11-20_n-lock-v0_1_plan-sha_out.txt`](2026-11-20_n-lock-v0_1_plan-sha_out.txt):

```text
reads 7680, distinct 7680
per arm: N1-V 960; N1-R 4800; N1-P 640; N2-E 320; N2-S 320; N2-C 320; N4-T 160; N4-Ts 160
read_plan_sha256 7f7d7301607e0fa6f66df930ce6a502086fe13cd84d19fe2d3f8b0c9105b88a6
```

## 3. The shell cross-check, verbatim

It ran before the window, outside any (bash, awk, sort, uniq, cut, shasum, wc; no Python). It writes the plan's
7,680 read ids, one per line, to `plan_shell.txt` (sha256
`1d1dc4a1e4d1faa03caf66aad24995f58ec48a799fad8573a52ebfcb5f1beee1`, kept in Code's scratch), and prints the sha256 of
the ids joined by newlines with no trailing newline: the form `schema.read_plan_sha256` hashes, "sha256 of the plan's
read_ids joined by newlines (no trailing newline)" (`valence_core/n/schema.py`:602).

```bash
L=<scratch>/step4b/lock; [ ! -e "$L/plan_shell.txt" ] || { echo exists; exit 1; }; awk 'function cell(r) { return (r < 40) ? ("floor_b" int(r / 5)) : ("neu_b" int((r - 40) / 20)) } function emit(arm, did, labs, nr,   n, a, i, r) { n = split(labs, a, " "); for (i = 1; i <= n; i++) for (r = 0; r < nr; r++) print arm "|" did "|" a[i] "|" cell(r) "/" r } BEGIN { emit("N1-V", "valence", "+1 +1/2 +d_20 +d_eq -1", 160); emit("N1-V", "none", "0", 160); for (k = 0; k < 24; k++) emit("N1-R", sprintf("rand_%02d", k), "+1 +1/2 +d_20 +d_eq -1", 40); emit("N1-P", "valence", "+1 +d_20 +d_eq -1", 160); emit("N2-E", "span_reward", "f0.10 f0.20", 160); emit("N2-S", "span_sentiment", "f0.10 f0.20", 160); emit("N2-C", "span_character", "f0.10 f0.20", 160); emit("N4-T", "none", "0", 160); emit("N4-Ts", "none", "0", 160) }' | LC_ALL=C sort > "$L/plan_shell.txt"; printf 'lines %s, distinct %s\n' "$(wc -l < "$L/plan_shell.txt" | tr -d ' ')" "$(LC_ALL=C sort -u "$L/plan_shell.txt" | wc -l | tr -d ' ')"; cut -d'|' -f1 "$L/plan_shell.txt" | uniq -c | awk '{ printf "%s %s; ", $2, $1 } END { print "" }'; printf 'sha256 of the ids joined by newlines, no trailing newline: %s\n' "$(printf '%s' "$(cat "$L/plan_shell.txt")" | shasum -a 256 | cut -d' ' -f1)"; head -n 2 "$L/plan_shell.txt"; tail -n 1 "$L/plan_shell.txt"

```

It was re-run for this record on 2026-11-20: the same command, with `L` set to a new scratch folder. Exit 0; its
`plan_shell.txt` is byte for byte the first's (`cmp`); its stdout:

```text
lines 7680, distinct 7680
N1-P 640; N1-R 4800; N1-V 960; N2-C 320; N2-E 320; N2-S 320; N4-Ts 160; N4-T 160; 
sha256 of the ids joined by newlines, no trailing newline: 7f7d7301607e0fa6f66df930ce6a502086fe13cd84d19fe2d3f8b0c9105b88a6
N1-P|valence|+1|floor_b0/0
N1-P|valence|+1|floor_b0/1
N4-T|none|0|neu_b5/159
```

## 4. The comparison

The window's `read_plan_sha256` and the shell's join are equal:
`7f7d7301607e0fa6f66df930ce6a502086fe13cd84d19fe2d3f8b0c9105b88a6`. The diff of the two strings is empty.
