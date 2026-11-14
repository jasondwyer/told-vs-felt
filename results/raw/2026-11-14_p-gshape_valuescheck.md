# G-SHAPE-p -- the re-run on the campaign wiring's BUILD: blind values-check

*Code's raw, PI date 2026-11-14. A blind values-check of the G-SHAPE-p re-run's entry draft and its raw. The checker worked against the working tree at HEAD `c0f1c69` (the new artifact and the staged move), the run's outputs and wrapper, the earlier entries, and p's code.*

*Totals: 68 claims; 62 CONFIRMED, 1 IMPRECISE, 0 FAIL, 5 NOT CHECKABLE (the lock to come, the commit to come in three rows, and the push).*

*How the findings were applied:*
- *The IMPRECISE item (row 60, the raw's "moved by hand") was applied in the checker's wording or close to it.*
- *O-1 is applied: the raw's header names the wrapper and its checks.*
- *O-2 is applied: the raw's title ends "Code's raw, PI date 2026-11-14".*
- *O-3 needs no change.*
- *O-4 is followed: the commit names both paths of the move.*
- *The fixes were checked by tool, not by a second blind pass.*

*Local paths are scrubbed (`<repo>`, `<tmp>`).*

## Values-check: the G-SHAPE-p re-run entry (draft `entry_gshape.md`) and its raw (`gshape_raw.txt`, to be committed as `results/raw/2026-11-14_p-gshape.txt`)

Sources: REPO at HEAD `c0f1c69` (c0f1c6967c2628d81ca2f66d36751dea11b2c0d3); the new artifact `data/p/gates/G-SHAPE-p.json` (untracked); the staged rename to `data/p/gates/G-SHAPE-p.superseded-2026-11-14.json`; the run's `gshape_stdout.txt`, `gshape_stderr.txt`, `gshape_meta.txt` and `gshape_rerun.sh`; RESULTS.md (the 2026-11-10 G-SHAPE-p entry `f5e695c`, the 2026-11-14 BUILD entry `c0f1c69`); the seat's read `results/raw/2026-11-12_p-qual_design-to-code_answers.md` (sha256 a32d4d17…1112); `valence_core/p/stage.py`, `valence_core/p/gshape.py`, `valence_core/p/guard.py`, `scripts/p_sessions.py`.

**Totals (68 claims):**
- CONFIRMED: 62
- IMPRECISE: 1
- FAIL: 0
- NOT CHECKABLE: 5

**Forbidden content (clock time or stamp, `$` figure, local absolute path, email address): none found** in the entry or the raw. The raw's line 3 has `$PY` twice. That is a shell variable, not a `$` figure, and the 2026-11-10 raw has the same text.

### Claims

#### The entry

| # | Claim | Mark | Evidence | Accurate wording |
|---|---|---|---|---|
| 1 | Dated 2026-11-14 | CONFIRMED | The session date is 2026-11-14. The superseded file's name carries it. The BUILD entry (`c0f1c69`) has the same date and comes before this run. | |
| 2 | "the re-run of record" | CONFIRMED | stdout line 2: "G-SHAPE-p (the run of record; committed sources)". `gshape.summary_lines` prints this only when `res['canonical']`. The wrapper's line 17 passes no `--out`. | |
| 3 | "on the campaign wiring's BUILD (`c0f1c69`)" | CONFIRMED | meta `head c0f1c6967c2628d81ca2f66d36751dea11b2c0d3` = `git rev-parse HEAD`. The commit's subject begins "p -- the campaign wiring: BUILD, a p package move". | |
| 4 | "before LOCK-p v1.0" | CONFIRMED | The tracked locks `LOCK-p-OLMo-{sft,dpo,instruct}.md` are v0.2 (heading "# LOCK-p-OLMo-sft v0.2"). No v1.0 exists. | |
| 5 | "PASS" | CONFIRMED | The artifact has `verdict` "PASS" and `stop_reasons` []. stdout's last line reads "G-SHAPE-p: PASS". | |
| 6 | "p v0.2 §4.2" | CONFIRMED | `PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md:86` (§4.2, "Code and identity") defines "**G-SHAPE-p**, model-free, …". The artifact's `spec` field reads "PROPOSAL-p v0.2 §4.2 (G-SHAPE-p) and §8 step 4 …". | |
| 7 | "the seat's read of G-F0m-OLMo (p) ×3, §4.3 item 2" | CONFIRMED | The seat's file is titled "The seat's read of G-F0m-OLMo (p) ×3 (`a225a89`) …". Its line 45 is §4.3 item 2, "**The campaign wiring**". | |
| 8 | The quote "its BUILD, blind review and values-check, and G-SHAPE-p's and G-ANL-p's re-runs land after G-PWR's entry" | CONFIRMED | Byte-exact, with ASCII apostrophes and one occurrence in the source (line 45). The entry's copy differs only by its own Markdown line wrap after "values-check,". The order holds: G-PWR (p)'s entry `3e1b614` < BUILD `c0f1c69` < this run. | |
| 9 | "`data/p/gates/G-SHAPE-p.json`, schema `p-gshape-v1`" | CONFIRMED | The file exists (`?? data/p/gates/G-SHAPE-p.json`). Its `schema` field is "p-gshape-v1". | |
| 10 | sha256 `4a4fdee5032f98d2f637c9a03fc1e0392bebc2fe729bb1e0d49c6aebafedd06d` | CONFIRMED | `shasum -a 256` gives the same value, and meta `new_sha` is equal. | |
| 11 | "is written once" | CONFIRMED | stdout ends "(written)". `guard.write_once_bytes` returns "written" only when no file stood at the path. Otherwise it returns "identical" or raises GuardStop. The old file had been moved before the run. | |
| 12 | "on the package LOCK-p v1.0 will name" | NOT CHECKABLE | This is about a future lock. Grounding: the seat's §4.3 item 3 lists "p's moved package and driver" among v1.0's contents. The package the artifact records equals `guard.package_sha256()` now (row 38). | |
| 13 | "`f5e695c`'s artifact is superseded" | CONFIRMED (index and tree) | `R  data/p/gates/G-SHAPE-p.json -> data/p/gates/G-SHAPE-p.superseded-2026-11-14.json`. The renamed blob `36c02414e699…` is `f5e695c`'s blob at the canonical path. A new artifact stands at the canonical path. The commit itself is row 20. | |
| 14 | "Model-free; nothing ran on a model or the box" | CONFIRMED | p v0.2 §4.2 says "model-free". `valence_core/p/gshape.py` imports no model or tokenizer: its only `olmo_hf` mention is in the docstring, and that file is hashed in the sources map, not imported. Importing the driver in a fresh `-I -B` process loads no torch, mlx, mlx_lm, transformers, tokenizers or safetensors module. m's `olmo_stack` leaves the tokenizer half "not exercised". The wrapper ran in the laptop repository. | |
| 15 | "(F-p12's form, as at `f5e695c`)" | CONFIRMED | The `f5e695c` entry reads: "**The supersession** (F-p12's form). Before the run, `fdd79d8`'s artifact (sha256 `3c4125a3…1554`) was moved with `git mv` to … It is kept in history, and the move is committed here." This entry uses the same form. | |
| 16 | "Before the run" | CONFIRMED | `gshape_rerun.sh` line 16 (`git mv`) comes before line 17 (the run). | |
| 17 | "`f5e695c`'s artifact (sha256 `f8d22109…631f`)" | CONFIRMED | Three values are equal: meta `old_sha f8d221098c8fe6f0839426e87fd1cc519a7928b5ee66f9a09b6dda8805fa631f`, the superseded file's sha256, and the sha256 of `git show f5e695c:data/p/gates/G-SHAPE-p.json`. `f5e695c` is the path's last change before HEAD (`git log`). | |
| 18 | "was moved with `git mv` to `data/p/gates/G-SHAPE-p.superseded-2026-11-14.json`" | CONFIRMED | The rename is staged (R), and the wrapper's line 16 is `git mv "$OLD" "$NEW"`. | |
| 19 | "It is kept in history" | CONFIRMED | `git rev-parse f5e695c:data/p/gates/G-SHAPE-p.json` = HEAD's = the index blob at the superseded path = `git hash-object` of that file = `36c02414e699a6346412d0e7d5a5e2aad2055be1`. | |
| 20 | "and the move is committed here" | NOT CHECKABLE | The commit has not been made yet. The rename is staged now. | |
| 21 | "`scripts/p_sessions.py gshape` (canonical)" | CONFIRMED | Wrapper line 17 has no `--out`. stdout line 2 is printed only on a canonical run (row 2). | |
| 22 | "at HEAD `c0f1c69`" | CONFIRMED | meta `head`. The wrapper refuses a different HEAD (line 10), and `git mv` does not move HEAD. | |
| 23 | "at `nice -n 19`" | CONFIRMED | Wrapper line 17: `nice -n 19 "$PY" -B scripts/p_sessions.py gshape`. | |
| 24 | "exit 0" | CONFIRMED | meta `exit 0`. | |
| 25 | "stderr empty" | CONFIRMED | `gshape_stderr.txt` is zero bytes (`test -s` false). | |
| 26 | "Every file of the sources map and of the import closure was committed and unedited" | CONFIRMED | The artifact records `provenance.committed` True. For all 58 distinct paths (51 sources and 14 closure files, 7 shared), the recorded sha256 equals both the working-tree sha256 and the HEAD-blob sha256. `git status --porcelain --` over those paths is empty. | |
| 27 | "as the canonical run requires" | CONFIRMED | On a canonical run, `gshape.inputs_of_record` raises GshapePRefusal unless the sources map, p's package and the closure are "committed at HEAD and unedited". It also refuses unless p's and m's package hashes equal their committed blobs' (gshape.py:288–306). `write()` re-checks for drift after the run (gshape.py:440–445). The driver's usage text says the same (p_sessions.py:18–19). | |
| 28 | "Raw: [`_p-gshape`](results/raw/2026-11-14_p-gshape.txt)" | CONFIRMED (as declared) | The link names the brief's declared commit path, and nothing exists there yet (`ls results/raw`). The name follows the 2026-11-10 entry's form. The file arrives with the commit. | |
| 29 | "with the repository's prefix scrubbed to `<repo>`" | CONFIRMED | The raw's body after "## stdout" equals `gshape_stdout.txt` byte for byte (936 bytes) once the repository prefix's 2 occurrences are replaced by `<repo>`. | |
| 30 | "The result, as at `f5e695c`" | CONFIRMED | Compared field by field, the new and superseded artifacts differ only in `provenance`'s `p_package_sha256`, `sources` (two values) and `sources_digest`. Every result field is equal. | |
| 31 | "each OLMo unit: 2,816 placements, 0 fired, 0 misplaced" | CONFIRMED | `grid[u]`: n 2816, n_fired 0, n_misplaced 0 for OLMo-sft, -dpo and -instruct. | |
| 32 | "`render-as-response` 0/2816 (reported)" | CONFIRMED | `controls[u]['render-as-response']`: n_fired 0, n 2816, required False, for all three units. | |
| 33 | "`seg+gold` 2816/2816 (required)" | CONFIRMED | `controls[u]['seg+gold']`: n_fired 2816, n 2816, required True, for all three units. | |
| 34 | "the grids identical across the three" | CONFIRMED | `olmo_grids_identical` True. All three units share one `rows_sha256`, bf4e9c235073…. | |
| 35 | "8,448 in total" | CONFIRMED | `grid_total` is 8448, which is 3 × 2816. | |
| 36 | "template-shape problems, Layer S problems and Layer P problems each 0" | CONFIRMED | `template_shape.n_problems` 0 with `problems` []. `layer_s.problems` [] and `layer_p.problems` []. | |
| 37 | "the placement keys equal G-SHAPE-F0's committed artifact's, unit by unit" | CONFIRMED | `g_shape_f0_placements.per_unit` has `equal` True for each of the three units. The source is "HEAD's blob", and the recorded sha256 38ba8e28… equals the sha256 of `git show HEAD:data/m/gates/G-SHAPE-F0.json`. | |
| 38 | "p's package `a38d93bb…a2d7`" | CONFIRMED | The artifact's `p_package_sha256` and the brief's `guard.package_sha256()` command both give a38d93bb83b64400c2663aee7f26cbe299300cc8a982935cce9b1187ed5ba2d7. | |
| 39 | "the BUILD's" | CONFIRMED | The BUILD entry's Licence line gives the same full hash. | |
| 40 | "m's package `7756dcf4…49bb`" | CONFIRMED | The artifact's `m_package_sha256` = `m_resume.package_sha256()` now = 7756dcf42532…666349bb. | |
| 41 | "unchanged" | CONFIRMED | The superseded artifact records the same m package hash. | |
| 42 | "a sources map of 51 files" | CONFIRMED | `len(provenance.sources)` is 51. | |
| 43 | "differing from `f5e695c`'s artifact only in the two files the BUILD moved (`scripts/p_sessions.py`, `valence_core/p/stage.py`)" | CONFIRMED | Both maps have the same 51 keys, and only these two values differ. `git show --name-status c0f1c69` lists M for these two code files and otherwise only RESULTS.md and three raws. The recorded driver sha256 9c641e19…a96d equals the BUILD entry's. | |
| 44 | "its digest `7907c28d…8b2d`" | CONFIRMED | The artifact's `sources_digest` is 7907c28d76c2…fac58b2d. Recomputing it as sha256 of `m_resume.json_text(sources)` gives the same value. | |
| 45 | "(`f5e695c`'s `6bf8bb95…caa9`)" | CONFIRMED | The superseded artifact's `sources_digest` is 6bf8bb953bc6…4f32f9caa9. | |
| 46 | "an import closure of 14 files, equal to `f5e695c`'s artifact's" | CONFIRMED | 14 entries, and the dicts are equal. | |
| 47 | "its digest `23abe773…eec4` unchanged" | CONFIRMED | Both artifacts record 23abe773f751…d049eec4, and recomputing gives the same value. | |
| 48 | "The stage's drift check (`stage.gshape_drift_problems` …) reads it as current" | CONFIRMED | `stage.gshape_drift_problems(GSHAPE_REL, provenance)` returns [], and so does `stage.stale_problems(…, ("p_package_sha256", "m_package_sha256"))`. The check does discriminate: on the superseded artifact it names exactly the two moved files. | |
| 49 | "its closure computed in a fresh interpreter" | CONFIRMED | `gshape_drift_problems` takes the closure from `fresh_import_closure()`. That function runs `subprocess.run([sys.executable, "-I", "-B", "-c", _CLOSURE_CODE, REPO])`, which imports the driver by path. | |
| 50 | "Next: G-ANL-p's re-run (`ba89279`'s artifact superseded)" | CONFIRMED | `ba89279` is the last commit on `data/p/gates/G-ANL-p.json`. The BUILD entry's Next item reads "G-ANL-p's re-run, superseding `ba89279`'s". | |
| 51 | "then LOCK-p v1.0 ×3, drafted for the seat's read" | CONFIRMED | The BUILD entry's Next item reads "LOCK-p v1.0 ×3, drafted for the seat's read (D_p 2026-12-15)". The seat's §4.3 item 3 says: "The seat reads each v1.0 before the PI commits it." | |
| 52 | "Not pushed." | NOT CHECKABLE | This is about the commit still to be made. It is consistent with now: `c0f1c69` is not an ancestor of the local `origin/main` ref (16c99d5). No remote was contacted. | |
| 53 | "Committed by path." | NOT CHECKABLE | A future act. | |

#### The raw's header (`gshape_raw.txt`, lines 1–8) and body

| # | Claim | Mark | Evidence | Accurate wording |
|---|---|---|---|---|
| 54 | Title: "the re-run of record on the campaign wiring's BUILD (c0f1c69), before LOCK-p v1.0" | CONFIRMED | As rows 2–4. | |
| 55 | Title: "(the seat's read of G-F0m-OLMo (p) x3, s4.3 item 2: "…"; p v0.2 s4.2)" | CONFIRMED | The quote is byte-exact on one line and occurs once in the source. The attribution matches rows 6–7. | |
| 56 | "Command: $PY -B scripts/p_sessions.py gshape (canonical: no --out), from the repository root, at nice -n 19, $PY = <repo>/jlens-qwen36/.venv/bin/python" | CONFIRMED | Wrapper lines 6, 8, 9 (`cd "$REPO"`) and 17. stdout's INVOCATION line shows the same interpreter path; argv omits `-B` and `nice`. | |
| 57 | "HEAD c0f1c69 (the campaign wiring's BUILD)" | CONFIRMED | As row 3. | |
| 58 | "every file of the sources map and of the import closure committed at HEAD and unedited (the run refuses otherwise)" | CONFIRMED | As rows 26–27. The wrapper also refused a non-empty `git status --porcelain -- data/p/gates valence_core scripts` (exit 11). | |
| 59 | "Before the run, f5e695c's artifact (sha256 f8d221098c8fe6f0839426e87fd1cc519a7928b5ee66f9a09b6dda8805fa631f)" | CONFIRMED | As rows 16–17, with the full hash equal. | |
| 60 | "was moved by hand with git mv to data/p/gates/G-SHAPE-p.superseded-2026-11-14.json" | IMPRECISE | The `git mv` was issued by the re-run's wrapper (`gshape_rerun.sh` line 16, `git mv "$OLD" "$NEW"`), not typed by hand. It holds only in F-p12's sense: a "hand `git mv`" (RESULTS.md, F-p12) is one made outside the stage's write-once writer. The 2026-11-10 raw used the same phrase. The entry itself says only "moved with `git mv`". | "was moved with git mv by the re-run's wrapper, outside the stage, before the run (F-p12's supersession), to data/p/gates/G-SHAPE-p.superseded-2026-11-14.json" |
| 61 | "(F-p12's supersession;" | CONFIRMED | As row 15. | |
| 62 | "the move is committed with this raw)" | NOT CHECKABLE | The commit has not been made yet. The rename is staged. | |
| 63 | "Exit 0; stderr empty." | CONFIRMED | As rows 24–25. | |
| 64 | "Artifact data/p/gates/G-SHAPE-p.json, sha256 4a4fdee5…d06d (written once)" | CONFIRMED | As rows 10–11, with the full hash equal. | |
| 65 | "No model, no tokenizer, no pod." | CONFIRMED | As row 14. | |
| 66 | "No clock time is recorded." | CONFIRMED | Neither the raw nor the entry has a time-like token (scanned for hh:mm, UTC, Z-times, GMT/EST/PST). `gshape_meta.txt` and the wrapper record none. | |
| 67 | "Local absolute paths scrubbed: the repository's prefix shown as <repo>; nothing else changed." | CONFIRMED | As row 29. The raw contains no `/Users`, `/private`, `/tmp`, `/home`, `/workspace` or `~/`, and is ASCII only. | |
| 68 | The stdout section (lines 12–20): per-unit figures, the grid line, the F0 line, the provenance sha16s `a38d93bb83b64400`, `7756dcf42532b222`, `7907c28d76c28501`, `23abe773f751bb19`, PASS | CONFIRMED | Each equals the artifact's fields (rows 31–47). The section is byte-equal to the run's stdout after the scrub. | |

### Observations (not marked)

- **O-1 (row 60).** The raw's header describes the command but does not name the wrapper that ran it. The wrapper checked HEAD, checked that `git status --porcelain -- data/p/gates valence_core scripts` was empty, checked that the superseded path was absent, then ran the `git mv`, the run and the meta write. Nothing stated is false; the 2026-11-10 raw had the same shape.
- **O-2.** The raw's title drops the "Code's raw, <date>" ending that the 2026-11-10 raw's title carried. The date is only in the file name. Cosmetic.
- **O-3 (row 48).** The stage's own currency test for G-SHAPE-p (`stage.py:445–447`) runs `stale_problems` on both package hashes as well as `gshape_drift_problems`. Both return [] on the new artifact, so "reads it as current" holds for the whole test. On the superseded artifact, `stale_problems` flags p's package (08bfa693… vs a38d93bb…).
- **O-4 (rows 20, 62).** In the index, the canonical path is deleted (the staged rename) and the new artifact is untracked. A by-path commit has to name both `data/p/gates/G-SHAPE-p.json` and the superseded path to carry the move and the new artifact together, as `f5e695c` did (M + A).

### Disclosures

Every command that touched `data/` (none touched `data/*/ckpt` or `data/*/reports`, by name, content or metadata):

1. `git status --porcelain data/p/gates`, then a bare `git status --porcelain` at the end, filtered with `/usr/bin/grep -v` and counted with `wc -l` on its output lines. Names only.
2. `ls data/p/gates` (name-only).
3. `shasum -a 256` of `data/p/gates/G-SHAPE-p.json` and of the superseded file.
4. `git rev-parse` of `f5e695c:`, `HEAD:` and `:` (index) at the G-SHAPE-p paths, and `git hash-object` of the two working-tree files. Digests only.
5. `git show f5e695c:data/p/gates/G-SHAPE-p.json | shasum -a 256`.
6. `git log --format='%h %ad' --date=short -- data/p/gates/G-SHAPE-p.json`. This shows author dates where item 1 names commit times. The path is outside `ckpt` and `reports`, so item 2's metadata bar does not apply. Disclosed as a form outside item 1's wording.
7. `git log --format='%h %s' -3 -- data/p/gates/G-ANL-p.json`.
8. `git show --name-status` of `c0f1c69` and `f5e695c`, which names paths under `data/p/gates`.
9. `json.load` of both G-SHAPE-p artifacts (system `python3 -I -B` and the venv's `-I -B`) for fields and a field-by-field comparison.
10. For the artifact's 58 source and closure paths, I read the working-tree bytes and the `git show HEAD:<path>` bytes to compute sha256s, and ran `git status --porcelain --` over those paths. Eleven of the paths are under `data/`: `data/configs/{e2a_ban_list,e2b_audit_v2,f_termination_patterns}.json`, `data/f/pools.json`, `data/olmo/a1_repair_roster.json`, `data/olmo/b3_screen_{sft,dpo,instruct}.json` and `data/olmo/scaffold_{sft,dpo,instruct}.json`. Only mismatches were printed, and there were none.
11. `git show HEAD:data/m/gates/G-SHAPE-F0.json` and the working-tree file, each to a sha256 only.
12. `stage.stale_problems` and `stage.gshape_drift_problems` on both artifacts (venv `python -I -B`), which ran the stage's own reads:
    - `gshape.sources_map(committed=True)`, i.e. `git cat-file -e`, `git ls-tree -z` (no `-l`) and `git cat-file blob` over the 51 sources, the 11 data files above included;
    - `fresh_import_closure`, a fresh `python -I -B` that imports the driver;
    - `current_shas`, which hashes both packages and both analyzers.

Other commands, outside `data/`:
- Brief's p package command and `m_resume.package_sha256()`.
- An import probe of `scripts/p_sessions.py` (venv `-I -B`).
- `/usr/bin/grep` over single named files only (no recursive or tree search).
- `git ls-files | grep` and `ls results/raw | grep` over names.
- `git rev-parse --verify -q origin/main` and `git merge-base --is-ancestor c0f1c69 origin/main`, which read local refs only and are not among item 1's listed forms. They print an id or nothing and touch no `data/` path. No remote was contacted.

**Departures:** the two noted above, the `%ad` form (item 6) and `merge-base`. G-SHAPE-p was not re-run, no model was loaded, and nothing was written to the repository. All Python ran with `-B`. The final `git status --porcelain` matches the starting snapshot: 33 lines, being the staged rename, the untracked new artifact and the 31 other untracked files.
