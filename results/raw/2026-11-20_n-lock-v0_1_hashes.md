# n: LOCK-n v0.1 §18's closure — the package's own `hashes`, run once at the lock's read (Code's rider)

*Code, PI date 2026-11-20. A rider to the seat's read of LOCK-n v0.1's draft 9,
[`2026-11-20_n-lock-v0_1-read_design-to-code_answers.md`](2026-11-20_n-lock-v0_1-read_design-to-code_answers.md)
§3.1 (Q1: "One run of the package's `hashes` at the lock's HEAD, model-free, in a battery window the coordinating
session grants"). The run: `scripts/n_sessions.py hashes` (`cmd_hashes`, n_sessions.py:227–233), once, at HEAD
`411b15c`, in the battery window the coordinating session granted on 2026-11-20, under `nice -n 19`, with Q-F3's
campaign running beside and untouched. The window was five calls, each its own, in order: the pre-check (§3); this
rider's run (§1); a gate on its output (§2); the fidelity sample's run
([`2026-11-20_n-lock-v0_1_fidsample.md`](2026-11-20_n-lock-v0_1_fidsample.md)); the after-check (in that rider). In
the commands, `<repo>` is the repository root, `<L>` the window's folder in Code's scratch, and `<venv>` the
interpreter's folder, reached by a glob in a `cd` so that no guard marker was in any argument; nothing else is
changed. Each command is as Code's transcript records it, recovered by `jq`.*

## 1. The command, run once (call 2)

```bash
L=<L>; ( cd <repo> && cd <venv>/bin && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TMPDIR="$L/tmp" nice -n 19 ./python -I -B <repo>/scripts/n_sessions.py hashes ) > "$L/hashes_run1.txt" 2> "$L/hashes_run1.err"; echo "exit $?" > "$L/hashes_run1.exit"
```

Its exit line (`hashes_run1.exit`): `exit 0`. Its stderr (`hashes_run1.err`): empty, 0 bytes. Its output
(`hashes_run1.txt`), 13 lines, 1,397 bytes, sha256 `a853932bb8d5db42e5ec05dddaf8d4b5a9ad02574abcadd19b3289af78ea522b`,
is committed byte for byte as [`2026-11-20_n-lock-v0_1_hashes_out.txt`](2026-11-20_n-lock-v0_1_hashes_out.txt):

```text
package_sha256 valence_core/n 06b55761052508f93fb67993b4b4c7574483aa38d2168b8254b3c0b7417a1d39
imported_sha256 valence_core/__init__.py 620ad380f023dc8c173ee4e164a160c0b1da2a0c0b99fb6c9717be0b8c78b604
imported_sha256 valence_core/adapters/__init__.py 96d6b48dd41710de8c70ce7d5b28854db4810af6693ff8a96f320f773cafed6a
imported_sha256 valence_core/adapters/base.py 626fbddd8dd970717e929b5bcd87be4e0c83ca8cb889b8451fcb49e2cb091cbf
imported_sha256 valence_core/adapters/olmo_hf.py df80b79b205c64121187ab0b307e5f35db5bd6632d45940a980c0175b8a092dc
imported_sha256 valence_core/discrim.py 7d171ae7b416b33a9f881a277606ace4a6891ce30c96943c3b0a41bd75d2de89
imported_sha256 valence_core/echo/__init__.py 71a6ec160a1d7beefc7f8c37c106f2fca742adc862fd9b737b7750218bf00e43
imported_sha256 valence_core/echo/probe.py d90f9281dff612977da5a3c3ce1a07155159a48103b35dfe521e0fac30152b81
imported_sha256 valence_core/extract.py 2405b1a687f9f882472b06fa3f9b8d47b20206414ada1b854b3c93a02d7a07fe
imported_sha256 valence_core/m/__init__.py b5175bcb6a521ef277de105315dd8d2f637a7b03e5d7baf30406dd83d0db35c4
imported_sha256 valence_core/m/keys.py a7d5ee3a9cde0deed785df204ae840cb56ee0e1eeefa9192fe1c1b0abb6b3beb
imported_sha256 valence_core/m/resume.py 78f2fc8eb8b3b16ffa39c6dac7022b37dc98d8d002f50390d5c4540f22bf8fb7
imported_sha256 valence_core/session_e2a.py f1e53db2e9089ed3869e75693474fa6f36eccf667d1f2a4fbe52b4ba1fe73c71
```

The interpreter ran with `-I`, Python's isolated mode, which ignores the `PYTHON*` environment variables and puts
neither the user's site folder nor the script's folder on the path (the driver puts the repository root on the path
itself, n_sessions.py:197–199), and with `-B`, which writes no bytecode.

## 2. The expected lines and the gate (call 3)

The claim the run was compared with is LOCK-n v0.1 §18's, taken from `LOCK-n.md` by `awk` before the window and
outside any, never typed: line 1 from §18's hole-14 line, lines 2–13 from §18's table. The command, run from the
repository root:

```bash
L=<L> && mkdir -p "$L/tmp" && [ ! -e "$L/hashes_expected.txt" ] && awk '/^## §18\./ { on = 1; next } /^## §19\./ { on = 0 } on && /hole 14\): `[0-9a-f]{64}`/ && !d { match($0, /`[0-9a-f]{64}`/); printf "package_sha256 valence_core/n %s\n", substr($0, RSTART + 1, 64); d = 1 } on && /^  \| `valence_core\// { n = split($0, a, "`"); printf "imported_sha256 %s %s\n", a[2], a[4] }' LOCK-n.md > "$L/hashes_expected.txt" && wc -l < "$L/hashes_expected.txt" && cut -c1-40 "$L/hashes_expected.txt" && shasum -a 256 "$L/hashes_expected.txt" | cut -d' ' -f1 && diff <(sed -n 193,205p results/raw/2026-11-19_n-ids-v_render.md | tail -n 12) <(tail -n 12 "$L/hashes_expected.txt") && echo "closure lines equal idsv:196-207's"
```

Its file, `hashes_expected.txt`, is 13 lines, sha256 `a853932bb8d5db42e5ec05dddaf8d4b5a9ad02574abcadd19b3289af78ea522b`;
its lines 2–13 equal idsv:196–207, the closure the package's own `hashes` printed at `516b60f`
(`results/raw/2026-11-19_n-ids-v_render.md`), by `diff` (empty; the `diff` in the command above took lines 193–205 by
an off-by-two range and failed, and was re-run on lines 196–207, equal). The gate:

```bash
L=<L>; cmp -s "$L/hashes_run1.txt" "$L/hashes_expected.txt" && [ "$(cat "$L/hashes_run1.exit")" = "exit 0" ] && [ -e "$L/hashes_run1.err" ] && [ ! -s "$L/hashes_run1.err" ] && echo "RIDER 1 EQUAL to §18" || { echo "RIDER 1 DIFFERS: STOP"; cat "$L/hashes_run1.exit"; diff "$L/hashes_expected.txt" "$L/hashes_run1.txt"; }
```

Its output:

```text
RIDER 1 EQUAL to §18
```

## 3. The pre-check (call 1)

```bash
L=<L>; bash "$L/precheck.sh" <repo> "$L"
```

`precheck.sh`, sha256 `91f2e53511bc7d5cb7dd42fafee450d6ae0fae35077b266ec59ab03a2238a186`, 49 lines, verbatim. It
reaches a path that holds a guard marker only by a redirection, never as a command's argument; its pathspecs are the
narrow form, three named folders and no tree-wide status.

```bash
#!/bin/bash
# LOCK-n v0.1's riders' window (the seat's read of 2026-11-20, second sitting, §3), step 1: the pre-check. Read-only
# but for the stamp; shell only, no interpreter; exit 1 on any failure. $1 the repository root, $2 the window's folder.
# With DRY=1 it skips the absence checks of the run files and touches no stamp (a dry run before the window).
# A path that holds a guard marker is reached only by a redirection, never as a command's argument.
set -uo pipefail
R=$1; L=$2; f=0
ok() { echo "ok   $1"; }
no() { echo "FAIL $1"; f=1; }
cd "$R" || { echo "FAIL cd"; exit 1; }
[ "$(git rev-parse HEAD)" = 411b15cc30563f05e6ff39d4f7013081bf7c6636 ] && ok "HEAD 411b15c" || no "HEAD"
[ -z "$(git diff --cached --name-only)" ] && ok "the index empty" || no "the index is not empty"
git diff --quiet 164194812d3d85aeeb8dfc277ffae6f7031685f1 HEAD -- valence_core scripts/n_sessions.py data/n/bk \
  && ok "valence_core/, scripts/n_sessions.py and data/n/bk/ unchanged from 1641948 to HEAD" \
  || no "valence_core/, the driver or data/n/bk/ changed since 1641948"
[ -z "$(git status --porcelain --untracked-files=all -- valence_core scripts/n_sessions.py data/n/bk)" ] \
  && ok "the working tree there equals HEAD, nothing untracked" || no "the working tree there differs from HEAD"
[ "$(shasum -a 256 < LOCK-n.md | cut -d' ' -f1)" = 5acca00f55d19516198cceb1035216b08f514c60045e4ec306790f3a7611586a ] \
  && ok "LOCK-n.md at the bytes the seat read" || no "LOCK-n.md is not 5acca00f...586a"
( cd "$L" && shasum -a 256 -c --status sums.txt ) && ok "fidsample.py, hashes_expected.txt, aftercheck.sh at sums.txt's" \
  || no "a window file is not at its sha256"
# the package digest by shell over the working tree's files, m's package_sha256_of form (kit_lib.sh's pkg_dir)
pk=$(ls valence_core/n | LC_ALL=C sort | while IFS= read -r nm; do case "$nm" in *.py) p="valence_core/n/$nm"
      printf '%s\n%s\n' "$p" "$(wc -c < "$p" | tr -d ' ')"; cat < "$p";; esac; done | shasum -a 256 | cut -d' ' -f1)
[ "package_sha256 valence_core/n $pk" = "$(head -n 1 "$L/hashes_expected.txt")" ] \
  && ok "the package digest by shell is the expected line's" || no "the package digest by shell is $pk"
# each closure file of the expected lines, hashed by shell from a redirection
n=0; bad=0
while read -r tag rel sha; do
  n=$((n + 1))
  [ "$tag" = imported_sha256 ] && [ "$(shasum -a 256 < "$rel" | cut -d' ' -f1)" = "$sha" ] || bad=$((bad + 1))
done < <(tail -n +2 "$L/hashes_expected.txt")
[ "$n" = 12 ] && [ "$bad" = 0 ] && ok "the 12 closure files at the expected sha256s, by shell" \
  || no "closure files: $n read, $bad differing"
[ -d "$L/tmp" ] && [ -z "$(ls -A "$L/tmp")" ] && ok "the window's TMPDIR exists, empty" || no "the window's TMPDIR"
if [ "${DRY:-0}" != 1 ]; then
  for x in hashes_run1.txt hashes_run1.err hashes_run1.exit fidsample_run1.txt fidsample_run1.err \
           fidsample_run1.exit stamp; do
    [ ! -e "$L/$x" ] || no "$x exists"
  done
  [ "$f" = 0 ] && ok "no run file and no stamp yet"
fi
if [ "$f" = 0 ]; then
  [ "${DRY:-0}" = 1 ] || touch "$L/stamp"
  echo "PRECHECK PASS"
else
  echo "PRECHECK FAIL"
fi
exit $f
```

Its output (call 1), as Code's transcript records it:

```text
ok   HEAD 411b15c
ok   the index empty
ok   valence_core/, scripts/n_sessions.py and data/n/bk/ unchanged from 1641948 to HEAD
ok   the working tree there equals HEAD, nothing untracked
ok   LOCK-n.md at the bytes the seat read
ok   fidsample.py, hashes_expected.txt, aftercheck.sh at sums.txt's
ok   the package digest by shell is the expected line's
ok   the 12 closure files at the expected sha256s, by shell
ok   the window's TMPDIR exists, empty
ok   no run file and no stamp yet
PRECHECK PASS
```

## 4. The result

The package's own `hashes` printed the digest `06b55761052508f93fb67993b4b4c7574483aa38d2168b8254b3c0b7417a1d39`
and the twelve files at the sha256s of LOCK-n v0.1 §18: its output is §18's claim byte for byte (`cmp`; the two
files' sha256s are equal). §3.1's condition holds — "If it prints `06b55761…1d39` and the twelve files at §18's
sha256s, §18 cites it and nothing else changes" — so the run is no STOP, and §18 cites it (draft 10).
