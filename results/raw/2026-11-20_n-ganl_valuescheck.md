# n -- G-ANL-n's run entry, its stdout raw and its .gitignore admit: the blind values-check's report, whole, as the checker returned it (PI date 2026-11-20; the hand-back's message, saved by jq from its task transcript), then Code's dispositions. In the report, SCRATCH and REPO are the folders its brief named (Code's scratch folder for this run, and the repository); "range N" and "all N" are lines of Code's scratch sweep files. Its four at-sign tokens (lines 82, 147, 153 and 156 of this raw) quote the entry draft's placeholders and v7's raw; none is a placeholder of this raw.

# Values-check: G-ANL-n run entry, stdout raw and `.gitignore` admit

I checked 101 claims: 75 CONFIRMED, 9 IMPRECISE, 2 FAIL and 15 NOT CHECKABLE.

- **FAIL 1 (#62):** the sweep does not start where the entry says it does. It starts 17 calls after v7's second sweep, and those 17 calls are in neither sweep.
- **FAIL 2 (#77):** the entry says the file reader read "three ranges of RESULTS.md". It read two.

The raw is exactly the run's stdout with the repository root replaced, and its hash matches. The admit works as the entry says: I reproduced the proof in a scratch repository of my own and also ran a real `git status` there.

Notation: "range N" is line N of `sweep/range.tsv`. "all N" is line N of `sweep/all.tsv`. Range lines 1–18 are all 3421–3438, and range lines 19–83 are all 3440–3504. SCRATCH and REPO are as the brief defines them.

## Text 1: `commit/entry.filled.md`

| # | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | 1 | 2026-11-20; canonical run; n v0.2 §3 "G-ANL-n", §8 step 9; PASS | CONFIRMED | Artifact `spec` field; stdout's last line; b6ea27f is dated 2026-11-20 (`%cs`) |
| 2 | 2 | The `ganl --dose-map` command ran once | CONFIRMED | Only invocation row is all 3481 (range 60). Rows 3319 and 3488–3490 hold the command as text only. The run step refuses if `ganl.out` already exists. |
| 3 | 2 | On v7 at b6ea27f | CONFIRMED | `check.txt` line 1; `head.want` = b6ea27f4…; `git rev-parse HEAD` |
| 4 | 2–3 | In a battery window the coordinating session granted | NOT CHECKABLE | Cross-session |
| 5 | 3 | Battery 242/242 | CONFIRMED | Raw line 245 |
| 6 | 3 | All 246 coverage ids reached | CONFIRMED | Raw line 243; artifact has 246 ids, all unique |
| 7 | 3–4 | Reach equals the hand derivation under both gate branches | CONFIRMED | `dose_map.reach`: PASS and FAIL both have `agrees_with_hand` true |
| 8 | 4–5 | The artifact enters the repository with its admit | NOT CHECKABLE | Pending the commit; my simulation supports it (Text 3) |
| 9 | 5–6 | Its sha256 fills hole 13 (§5.1; routing item 5) | CONFIRMED | Seat's answers line 54; routing raw line 19 |
| 10 | 6–7 | Model-free; nothing ran on a model or on the box | CONFIRMED | No ssh, runpod or workspace in range; raw lines 238–239 |
| 11 | 8–9 | The run's last line, verbatim | CONFIRMED | `cmp` of the extracted quote against `ganl.out`'s last line: identical |
| 12 | 10 | Exit 0, stderr empty | CONFIRMED | `ganl.exit` is "0"; `ganl.err` is 0 B |
| 13 | 10–12 | Artifact sha256 (full), 32,018 B, 462 lines, printed sha equals the file's | CONFIRMED | `shasum` of the REPO file and its copy (identical); `wc -c -l` gives 462 and 32018 |
| 14 | 13–17 | Routing item 5 verbatim; raw `db8d8db4…ddcc` at bc85386, line 19 | CONFIRMED | Byte `cmp` against line 19 (253 B each); hash by tool; added at bc85386; committed and clean |
| 15 | 17–20 | Seat's answers `001e8c12…bd11` at d639bdd; §5.1 "**Still open:**" and "13 (G-ANL-n's canonical artifact)" | CONFIRMED | Hash; added at d639bdd; line 54 holds both strings |
| 16 | 20 | The pin move is v7, b6ea27f | CONFIRMED | v7's entry, RESULTS.md lines 34–36 |
| 17 | 20–21 | Coordinating session verified v7, screen CLEAR, before the window request | NOT CHECKABLE | Cross-session. NOTES.md line 3 agrees, but Code wrote it. |
| 18 | 22–23 | Three steps, each run once as its own foreground call | CONFIRMED | Range 58, 60, 62, each once and in order. Each call's own output is in `outputs/*.txt`. |
| 19 | 23 | "as the window's terms set" | NOT CHECKABLE | Cross-session |
| 20 | 24 | `check` is read-only; 16 of 16 PASS | CONFIRMED | `check.txt` lines 1–16; script lines 26–39 |
| 21 | 24–25 | Inputs at the manifest's sha256s via `shasum -c`; manifest written by `shasum` from the committed files; each committed and clean | CONFIRMED | Range 49 wrote `inputs.sha256` by `shasum` at HEAD. My fresh `shasum` is byte-equal to the manifest. All nine pass `rev-parse` against `hash-object`. |
| 22 | 25–26 | `data/n/gates` absent; no root `LOCK-n.md`; temp folder empty; no earlier output | CONFIRMED | `check.txt` lines 12–15 |
| 23 | 26–27, 33 | "no interpreter process but … PID 8051" / "8051 the only interpreter process" | IMPRECISE | Both checks are `pgrep -f '[p]ython'`, which only finds Python processes (script line 38; `pgrep.cmd`). Say "no Python process". |
| 24 | 27 | 8051 is Q-F3's campaign | NOT CHECKABLE | Only the script's own label says so |
| 25 | 27 | "which ran throughout" | CONFIRMED | 8051 is present at `check` (before) and at the `pgrep` after `after` |
| 26 | 27 | "as in every battery window" | NOT CHECKABLE | Other windows |
| 27 | 28–29 | The `run` command as rendered | CONFIRMED | Script line 45, with the root, `jl*/.venv` and the scratch root shown as placeholders |
| 28 | 29–31 | stdout and stderr captured apart; canonical (no `--out`); dose map path absolute; glob in a `cd` so no guard marker in any argument | CONFIRMED | Script line 45; `run.cmd` contains no marker |
| 29 | 31 | rc 0 | CONFIRMED | `run.txt` |
| 30 | 32–33 | `after` is read-only; temp empty; inputs unchanged; `data/n/gates/` holds only `G-ANL-n.json` | CONFIRMED | `after.txt` lines 14–16; my `ls -A` now gives the same |
| 31 | 34–35 | Analyzer `735da934…a7a8` (b6ea27f), committed and clean | CONFIRMED | `shasum`; `rev-parse` against `hash-object`; `git log -1` with the pathspec |
| 32 | 35–36 | Dose map `d4a73b54…efb3` (db00d6d), 121 B, five figures | CONFIRMED | `cat` and `wc -c`; added at db00d6d |
| 33 | 36–41 | The seven BOUND_RELS files with their hashes and commits (5916097, a61f13d, 7a54eb9, 0744136, ef105f1, 5916097 ×2) | CONFIRMED | Hash tails cut by tool; last commit per path; analyzer lines 5888–5889 |
| 34 | 40 | `reduced.json` is 28,053,197 B | NOT CHECKABLE | The brief limits bound files to `shasum`. The figure is not in RESULTS.md (`grep` found nothing). |
| 35 | 41–42 | "The analyzer's five sha256 constants equal the five files'" | IMPRECISE | The analyzer has six `*_SHA256` constants. `CODE_FORMS_SHA256` (line 3546) is a digest of code forms, not a file. The five file constants do equal their files. Name the five constants. |
| 36 | 42–43 | The analyzer checks itself and BOUND_RELS committed and clean before and after its battery | CONFIRMED | `ganl_precheck` (5985–5989); `run_ganl` (6030); `committed_problems` (5892–5906) |
| 37 | 43 | The dose map is checked by the analyzer's own refusals (five keys, finite floats, §2.3) | CONFIRMED | `dose_map_input_problems`; `DoseMap.problems` |
| 38 | 44 | "as the window request declared it before the run" | NOT CHECKABLE | The message is not in any file. NOTES.md lines 8–13 (written at range 53, between the request at 52 and the run at 60) record the same expected lines. |
| 39 | 44–46 | 245 stdout lines: INVOCATION, 242 `[PASS]` (one with `[CI]`), no `[FAIL]`, the summary line, the PASS line; stderr 0; exit 0 | CONFIRMED | Counts 242, 1 (`ganl.out` line 117), 0; summary line matched exactly with `grep -x` |
| 40 | 46–48 | 243 lines byte-identical; lines 3–245 equal v7's self-test raw's | CONFIRMED | `cmp` of `sed -n '3,245p'` from both files |
| 41 | 48–50 | Raw `3bd3003e…90a5`, 246 lines, header then stdout whole, root shown as `<repo>` | CONFIRMED | See R12 and R13 |
| 42 | 51 | Schema `n-ganl-v1` as `ganl_artifact` writes it; stage; verdict | CONFIRMED | `GANL_SCHEMA`; artifact fields |
| 43 | 51–53 | Analyzer by path and sha256 (the committed file's); proposal, three addenda and schema module by sha256 (each the file's) | CONFIRMED | `jq` against my `shasum`s |
| 44 | 53–54 | 242 of 242, expected 242, 246 ids, outputs digest `69b2a0d0…5e7e` | CONFIRMED | `jq` |
| 45 | 54–57 | Reachability triples and tuples per shape and branch, over the battery's own maps | CONFIRMED | `jq`; `_bt_reachability` uses MAP_A–D under both gate states |
| 46 | 56–57 | `bk_fidelity`: 2,400 reads, 0 above τ, 570 above τ/4, largest ratio 0.012143 | CONFIRMED | `jq` |
| 47 | 57 | Tuple space: 385 tuples, 2,561 evaluations | CONFIRMED | `jq` |
| 48 | 57–58 | PINS (32) and OPEN (9) as the analyzer at b6ea27f holds them | CONFIRMED | Key sets equal; written from the module dicts, never mutated; seven short values found verbatim in the source |
| 49 | 59–60 | d_eq and d_20, the points string, none merged, as G-CAL-n's record lists them | CONFIRMED | `cmp` against RESULTS.md lines 597–598 and the artifact's `points` |
| 50 | 61–63 | Reach under each branch: flags; PASS gives shape (a) 28/225, FAIL gives (b) 25/201 | CONFIRMED | `jq`; matches `after.txt` line 12 |
| 51 | 63–65 | "(a) is the branch in which none … coincide …; (b), the one …" | IMPRECISE | In `coupling_shape` (2284–2292), (a) and (b) are coupling shapes, not branches. Here PASS yields (a) and FAIL yields (b). |
| 52 | 66–68 | The seat's §0 reads the gate line as PASS, "so **N2 decides at f = 0.20** (A-n3 §3.4)"; VERDICTS reads the lock (PIN-n-40); the artifact reports both branches (PIN-n-42) | IMPRECISE | The quote is verbatim (seat's answers line 8), but its "so" follows two premises: the gate line and "2·d_eq = 0.574 ≤ 1". The lead-in gives only the gate. PIN-n-40 and PIN-n-42 are as stated. |
| 53 | 69 | The admit was accepted by the coordinating session | NOT CHECKABLE | Cross-session |
| 54 | 69–70 | Narrower than m's and p's `*.json` form; matches n's named-file block | CONFIRMED | HEAD `.gitignore` lines 233–235 and 358–360 (`*.json`); lines 307–314 and 320–324 (named files) |
| 55 | 70–72 | After line 324: blank line, the quoted comment, three rules; +5 −0 | CONFIRMED | `diff`; comment matches the insert's line 2 by `cmp`; 378 to 383 lines |
| 56 | 72–78 | Twelve paths: only the artifact changes (263 before, 329 after); siblings ignored by 328; other paths keep state and pattern | CONFIRMED | My own scratch repository with `check-ignore -v -n` gives the same; states equal `proof/before.txt` and `proof/after.txt`; temp name per `write_once` (line 4629). See observation 4. |
| 57 | 79–80 | In-tree status before the admit: one line, `!! data/n/gates/G-ANL-n.json` | CONFIRMED | `status_dn_now.txt`; command at range 71 |
| 58 | 80–81 | Gate asserts `?? …`; staged by `git add` without `-f` | NOT CHECKABLE | Pending the commit. My simulation lists `??` for this path. |
| 59 | 82–83 | Next: relay to n-build; lock commit after this run | NOT CHECKABLE | Plan |
| 60 | 83 | Not pushed | NOT CHECKABLE | Pending the commit |
| 61 | 84–85 | No read under `data/*/ckpt`, `data/*/reports` or `data/mf3`; no repository code outside the window; no model process | CONFIRMED | For range.tsv: ckpt and reports appear only as exclusions (range 19, 20, 71); the analyzer ran only at range 60. True for me too. |
| 62 | 86–87 | Sweep "from v7's second sweep through this entry's draft" | FAIL | v7's second sweep is all 3403 (the `jq` into `cmds3.tsv` and `since_sweep1.tsv`, after the battery of record at all 3399). `range.tsv` starts at all 3421. All 3404–3420 are in neither sweep (observation 1). |
| 63 | 88–90 | "in v7's commit window … a re-hash …" | IMPRECISE | The re-hash (range 5) came before the window was granted. Range 9 recap: "still not committed: I'm waiting … to grant the commit window. I re-sent the request after re-hashing". Code's notes (range 22) also put it before "In the window". |
| 64 | 88 | "each told to the coordinating session at the time" | NOT CHECKABLE | Message bodies are truncated in the sweep |
| 65 | 90–92 | Pre-check counts over eight scratch copies; one print of the values-check raw's line 155, quoting v6's placeholder names | CONFIRMED | Range 12–13; the committed raw's line 155 holds `@@VC_LINE@@` and `@@REC_RESULT@@` in a row quoting "v6 raw :325" |
| 66 | 92 | Asserting check of the message's last line and hash head | CONFIRMED | Range 18 |
| 67 | 92–97 | Post-commit verification forms | IMPRECISE | The list leaves out range 20's five `git cat-file blob HEAD:<path> \| shasum` (it names cat-file only "into cmp") and range 19's `git hash-object -- <path>` of the five tree paths |
| 68 | 98–100 | `rev-parse`, `hash-object`, `status --porcelain` and `log -1` of the nine inputs (first three also in `check`) and of the seat's answers and routing raw | IMPRECISE | Nine inputs: yes (range 45; script line 32). For the two raws only `rev-parse` and `hash-object` ran (range 78, 80). |
| 69 | 100–101 | `check-ignore -v` of the artifact's path | CONFIRMED | Range 46 |
| 70 | 101 | `show HEAD:.gitignore` into a scratch copy | CONFIRMED | Range 68 |
| 71 | 101–102 | Status `--ignored -uall` on `data/n` and `data/n/gates` with exclusions, one line each, printed | CONFIRMED | Range 71; file holds one line |
| 72 | 103–104 | `test -e` and `-L` of `data/n/gates` and root `LOCK-n.md`; `ls -A` in `after` | CONFIRMED | Range 46; script |
| 73 | 103 | "(the window request asked for it)" | NOT CHECKABLE | Cross-session |
| 74 | 105 | `cat` of the dose map (121 B, whole) | CONFIRMED | Range 46 |
| 75 | 105–106 | `sed -n` prints of `.gitignore` 255–262 and 300–330, seat's answers 8 and 54, routing raw 19 | CONFIRMED | Range 66, 79, 80 |
| 76 | 106–107 | `grep -n` over "those", the analyzer and RESULTS.md headers | IMPRECISE | No `grep` ran over the PI's routing raw. It ran over `.gitignore` (46), the seat's answers (78, 80), the analyzer (36, 38, 43, 45) and RESULTS.md (76). |
| 77 | 107–108 | The analyzer and "three ranges of RESULTS.md" read by the file reader | FAIL | The analyzer was read six times (range 37–44). RESULTS.md was read twice, at range 77 and 81. |
| 78 | 108 | One `grep -c` of v7's self-test raw for a digest prefix, result 0 | CONFIRMED | Range 74; my count is 0 |
| 79 | 109–111 | `jq` over the artifact and over the transcript, twice, the first anchored on its own text | CONFIRMED | Range 72, 73 and `after`; range 82 (`'git commit -q -F'` matches its own row) and range 83 (`v[7]` pattern) |
| 80 | 112–113 | `git init` plus `check-ignore` over twelve paths | CONFIRMED | Range 70 |
| 81 | 114 | One `pgrep` after `after` | CONFIRMED | Range 63 |
| 82 | 115 | Framing "Perl, over Code's scratch only" (placeholder skipped) | CONFIRMED | Range 68–69: `perl -CSD -ne` on scratch copies |
| 83 | 116–119 | Stated-plainly list "over named repository and scratch files" | IMPRECISE | Range 29 ran `wc -l`, `head -n 12` and `tail -n 8` on the backup in the shared notes folder, which is neither. Its reads are not named (observation 3). Range 68–69's `sed "324r"` is an insertion, not a substitution or print. |

## Text 2: `commit/2026-11-20_n-ganl_out.txt`

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| R1 | Canonical run (§3 "G-ANL-n", §8 step 9) on v7 (b6ea27f) | CONFIRMED | HEAD; artifact `spec` |
| R2 | `scripts/n_analyze.py ganl --dose-map data/n/gcal/dose_map.json` | CONFIRMED | Repository-relative form of the absolute paths in line 2 |
| R3 | Analyzer sha256 (full) | CONFIRMED | `shasum` |
| R4 | Dose map committed at db00d6d, sha256 (full) | CONFIRMED | `shasum`; added at db00d6d |
| R5 | `nice -n 19` with `-I -B` | CONFIRMED | Script line 45 |
| R6 | Interpreter reached by `cd` into the venv's bin by glob | CONFIRMED | Script line 45 |
| R7 | `TMPDIR` in scratch; foreground | CONFIRMED | Script line 45; `run.txt` is the call's own output |
| R8 | In a battery window the coordinating session granted | NOT CHECKABLE | Cross-session |
| R9 | PI date 2026-11-20 | CONFIRMED | v7's commit, which preceded the run, is dated 2026-11-20; session date |
| R10 | Exit 0; stderr 0 bytes | CONFIRMED | `ganl.exit`; `ganl.err` |
| R11 | stdout whole, 245 lines | CONFIRMED | `wc -l` |
| R12 | Root shown as `<repo>`; body is stdout with only the root replaced | CONFIRMED | `sed` replacement of the root in `ganl.out`, then `cmp` against `tail -n +2` of the raw: identical. Root occurs 3 times, on line 1. Home-prefix count after replacement: 0. |
| R13 | 246 lines, sha256 `3bd3003e…90a5` | CONFIRMED | `wc`; `shasum` |

## Text 3: `commit/gitignore.new`

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| G1 | `gitignore.head` is HEAD's `.gitignore` | CONFIRMED | `git hash-object` gives `7e31fc69…`, equal to `HEAD:.gitignore` and to the tree's file |
| G2 | New file is head plus the insert after line 324, nothing else | CONFIRMED | `diff` shows only additions (new lines 325–329) |
| G3 | Comment's references: n v0.2 §3 G-ANL-n, §8 step 9; `scripts/n_analyze.py ganl`; ledger 27 | CONFIRMED | Artifact `spec`; `GANL_REL`; CLAUDE.md rule 27 |
| G4 | Admits only the artifact | CONFIRMED | Scratch repo with real files: new file gives `??` for the artifact and `!!` for the temp name, `other.json` and the subfolder file; HEAD's gives `!!` for all four. The directory itself is re-included by line 327. |
| G5 | Same form as n's named-file blocks | CONFIRMED | Matches the gvec and gcal blocks |

## Counts

- **Text 1:** 58 CONFIRMED, 9 IMPRECISE, 2 FAIL, 14 NOT CHECKABLE.
- **Text 2:** 12 CONFIRMED, 1 NOT CHECKABLE.
- **Text 3:** 5 CONFIRMED.
- **Total:** 101 claims: 75 CONFIRMED, 9 IMPRECISE, 2 FAIL, 15 NOT CHECKABLE.

## Observations

1. **The gap after v7's second sweep.** All 3404–3420 (17 calls) are in neither sweep. They include:
   - Perl: `perl -ne` filters (3405, 3406), `perl -0 -i -pe` edits (3409, 3411, 3414, 3416) and a `perl -CSD -ne` (3414), all over scratch.
   - One `awk '{print $1"  "$2}'` over `shasum` output of scratch files (3418).
   - `sed -n '22,24p' RESULTS.md | cat -A` (3415).
   - `grep -c -F` with the home path, and bracketed marker counts, over v7's scratch copies (3418).
   - A Read and an Edit of v7's entry draft (3412–3413), the commit message's Write (3417), the window request (3419) and a notes append (3420).

   v7's committed stated-plainly line lists these classes, but no sweep counts them, and "Code knows of no others" rests on the sweep. Either extend the sweep or anchor it at all 3421 and say so.
2. **The range is not contiguous.** All 3439 (v7's `git commit -q -F … -- RESULTS.md scripts/n_analyze.py …`) is in neither `window_v7.tsv` nor `since_v7.tsv`. It is a planned step; @@SWEEP@@ should say it is excluded.
3. **Departures in range.tsv the entry does not name:**
   - Range 66: `git rev-parse HEAD:.gitignore` against `git hash-object -- .gitignore`, and `git log -1 --format=%h -- .gitignore`, without item 3's pathspec.
   - Range 20: five `git cat-file blob … | shasum`. Range 19: `hash-object` of the five tree paths.
   - Range 72: over the artifact under `data/n/gates`, `grep -cF` of the home path, the user name, the temp roots and "tmp", plus `LC_ALL=C grep -c '[^ -~]'` and `wc -l`. The entry names only `jq` over the artifact.
   - Range 23 and 25: Reads of two memory files. Range 30: Read of the shared-notes backup. Range 29: `wc`, `head` and `tail` of that backup. Only the writes are named.
   - For @@PERL@@: range 68 (one Perl run) and range 69 (two). NOTES.md line 31 counts six so far, three of them after the sweep. Range 14–15 ran v7's `place.pl` through `commit_steps.sh` (planned; declared in v7's entry).
4. **Proof row 2 could mislead.** Row 2 tests `data/n/gates/` as a trailing-slash path with no such directory in the proof repo, so it reads "ignored" both before (263) and after (328). With the directory present, `check-ignore` under the new file names line 327, which re-includes it. In a real tree the directory does change state, from ignored to re-included. The admit itself works (G4).
5. **The raw names the venv folder.** Raw line 2 (INVOCATION) still shows the venv's folder name after `<repo>/`, and that name holds two guard-marker strings; raw line 239 names model libraries. v7's committed self-test raw has the same line 2. This is not a breach, since the rule binds arguments, but the entry's run line hides the folder as `<venv>` while the raw does not.
6. **No trailing blank line.** The entry ends "@@VC@@\n". Unless the placement adds a blank line, the next Log entry will follow without the usual separation.
7. **Cosmetic.** Entry lines 45–46 split the quoted summary line across a line break, and Markdown will collapse its two leading spaces.
8. **Code-authored corroboration only.** Every cross-session claim (#4, 17, 19, 38, 53, 64, 73) has support only in Code's own NOTES.md.

## My departures beyond reading files and item 1's git forms

1. **One `awk` call, by accident, against the brief's "no interpreter".** I ran `awk 'BEGIN{}{x=$1} END{print x}'` inside an unused `$(…)` over line numbers that `grep -n` printed from `all.tsv`. Nothing from it was printed.
2. **Bound files beyond "`shasum` alone".** On the seven bound files and the other inputs I also ran `git rev-parse HEAD:<path>` against `git hash-object -- <path>`, and `git log -1 --format=%h` / `--diff-filter=A` with item 3's pathspec plus `':!data/mf3/**'`. These print ids and digests only. The same forms ran on the three named raws, v7's values-check raw, RESULTS.md and `.gitignore`, and `%cs` (calendar date only) on b6ea27f and on the dose map. `rev-parse HEAD`, `rev-parse HEAD:<path>` and `hash-object` take no pathspec.
3. **Text tools.** I used `sed`, `cut`, `tr`, `wc` (including `-c` and `-l` on the artifact and the dose map), `cmp`, `diff`, `od -c`, `head`, `tail`, `fold`, `paste`, `sort`, `uniq`, `seq`, `printf` and `cat`. `/usr/bin/grep` counts and `-o` fragments ran over scratch files, the analyzer, RESULTS.md and the named raws, with bracketed marker patterns only. I also used name-only `ls`, including `ls -A data/n/gates`.
4. **Reads beyond the named sources:**
   - v7's committed values-check raw, read by path: its committed-and-clean check, a `grep -n -o` of `@@` tokens, and line 155 printed.
   - RESULTS.md beyond the two named entries: `grep -n` of its headers and of `^- 2026-11-2`, `grep` for the `reduced.json` size (no hit), and lines 18–306 read whole.
   - NOTES.md in SCRATCH.
   - All 3319, 3398–3421 and 3439, outside the range, with the home path and scratch root masked.
5. **My own scratch repo beyond `check-ignore`.** Under `SCRATCH/vc/checker/ci` I created four empty files and ran `git status --porcelain --ignored -uall -- data` twice. In `proof/repo` I ran only `check-ignore`, plus a `cmp` of its `.gitignore` file.
6. **What I did not do.** I wrote only under `SCRATCH/vc/checker/`. I ran no Python and no repository or Code script. I touched nothing under `data/*/ckpt`, `data/*/reports` or `data/mf3`, ran no whole-tree status, did not list `results/raw`, and put no guard marker in any argument. I never printed `ganl.out`'s INVOCATION line, only counts and the raw's line 2 reduced to a letter/digit shape.

---

# Code's dispositions

Both FAILs fixed, every IMPRECISE item applied, observations 1–5 and 7 applied, 6 met and 8 noted; the edits checked
by tool, as the entry's values-check line says. Item numbers are the report's.

FAIL (2), each fixed:
- 62: the sweep now runs from the first call after v7's second sweep (the transcript's call 3404 of Code's session),
  so it is contiguous through the sweep itself; the 17 calls 3404–3420, which neither of v7's sweeps holds, are
  declared in the entry's first departures bullet, by their forms (observation 1's list), with their Perl runs among
  the counted ones.
- 77: the session's file reader's reads of the analyzer and of RESULTS.md are counted over the whole sweep, from the
  sweep file, and the RESULTS.md reads are named by their line ranges.

IMPRECISE (9), each applied:
- 23: "no Python process (`pgrep -f '[p]ython'`) but PID 8051" and "PID 8051 the only Python process".
- 35: the five file constants named, `PROPOSAL_SHA256`, `ADDENDUM_SHA256`, `ADDENDUM2_SHA256`, `ADDENDUM3_SHA256` and
  `SCHEMA_SHA256`, which equal the five files' sha256s (`CODE_FORMS_SHA256`, a digest of code forms, is not among them).
- 51: "(a), PASS's shape here, is the coupling in which …; (b), FAIL's, the one in which …".
- 52: the lead-in gives both premises of the seat's "so": the gate line read as PASS and 2·d_eq = 0.574 ≤ 1.
- 63: the re-hash is placed before v7's commit window; the window's extras follow "in it, beyond its planned steps
  (place, gate, stage, count and the commit)".
- 67: added, for each of the five paths, `git hash-object` of the tree's file and `git cat-file blob HEAD:<path>` into
  `shasum` beside `cmp`.
- 68: split by file: the four forms for the nine inputs; `rev-parse`, `hash-object` and `log -1` for `.gitignore`;
  `rev-parse` and `hash-object` alone for the seat's answers and the PI's routing raw.
- 76: "`/usr/bin/grep -n` over `.gitignore`, the seat's answers, the analyzer and RESULTS.md's entry headers".
- 83: "`sed` substitution filters, line prints and one insertion (`324r`)"; the reads of the backup in the shared notes
  folder named (the file reader, `wc -l`, `head` and `tail`).

Observations (8):
1. Applied, as item 62.
2. Applied: the sweep is one contiguous range of the transcript's calls; v7's commit (call 3439), a planned step of v7's
   window that v7's entry declares, is inside it and is named among the window's planned steps.
3. Applied: `.gitignore`'s three git forms; the five `git cat-file blob … | shasum` and the five `git hash-object` of
   the tree's files; over the artifact, the `/usr/bin/grep -c` counts (the home path, the user name, the temporary
   roots, "tmp", and lines outside printable ASCII), `wc -l`, `shasum` and the `cp` into scratch; the reads of Code's
   memory file and memory index and of the shared notes' backup; and the Perl runs, counted over the whole sweep.
4. Applied: the admit's proof run again in a second scratch repository holding empty files at eleven paths (the
   twelve less the folder): `git status --porcelain --ignored -uall -- data` under HEAD's `.gitignore` and under the
   new one lists eleven lines each, and only the artifact's changes, from `!!` to `??`; `git check-ignore -v -n` of the
   folder names line 263 (`/data/n/*`) under HEAD's and the new line 327 (`!/data/n/gates/`) under the new one. The
   entry now describes this test, and names the first test's reading of the folder.
5. Applied: the raw's header adds "the INVOCATION line names the venv's folder as it is, as v7's self-test raw does";
   its body is unchanged (its lines 2–246 byte-equal to the checked copy's), its sha256 moved from `3bd3003e…90a5` to
   `73ee821e…067c`; the entry says so beside the run's `<venv>`.
6. Met: v7's `place.pl` writes the entry followed by a blank line (`$log$e\n`), and the commit's gate counts the
   entry's lines plus that one among RESULTS.md's added lines.
7. Applied: the summary line quoted on one line, "after two spaces".
8. Noted: a claim about another session's act rests on that session's records; the brief's third "not yet true"
   item, by design.

The checker's departures are carried into the entry's departures as its report states them.
