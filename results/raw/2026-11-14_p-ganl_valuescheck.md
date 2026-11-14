# G-ANL-p -- the re-run on the campaign wiring's code: blind values-check

*Code's raw, PI date 2026-11-14. A blind values-check of the G-ANL-p re-run's entry draft and its raw. The checker worked against the working tree at HEAD `f784bff` (the new artifact and the staged move), the run's outputs and wrapper, the earlier entries and raws, and p's code.*

*Totals: 74 claims; 68 CONFIRMED, 1 IMPRECISE, 0 FAIL, 5 NOT CHECKABLE (the commit to come, in the entry and in the raw; the push; the commit by path; the locks to come).*

*How the findings were applied:*
- *The IMPRECISE item (row 36) was applied in the checker's wording: the stdout differs from `ba89279`'s raw only in its last line, the artifact's sha256; the stdout prints no package hash.*
- *The observations: the commit names both paths of the move, and the two wide entry lines are reflowed.*
- *The fixes were checked by tool, not by a second blind pass.*

*Local paths are scrubbed (`<repo>`, `<tmp>`).*

## Values-check: the G-ANL-p re-run entry (draft `entry_ganl.md`) and its raw (`ganl_raw.txt`, to be committed as `results/raw/2026-11-14_p-ganl.txt`)

A blind values-check, PI date 2026-11-14. I worked against the repository at HEAD `f784bff` (f784bff24f163c9690eba182f470fffbb26f1a1d) and its working tree: the new artifact `data/p/gates/G-ANL-p.json` (untracked) and the staged rename to `data/p/gates/G-ANL-p.superseded-2026-11-14.json`. Other sources: the run's `ganl_stdout.txt`, `ganl_stderr.txt`, `ganl_meta.txt` and `ganl_rerun.sh` (in `campwire/`); RESULTS.md (the G-ANL-p entry of 2026-11-10, `ba89279`, with its raw `results/raw/2026-11-10_p-ganl.txt`; the G-SHAPE-p entry, `f784bff`; the BUILD entry, `c0f1c69`); the seat's read `results/raw/2026-11-12_p-qual_design-to-code_answers.md` §4.3; PROPOSAL-p v0.2; `scripts/p_analyze.py`, `valence_core/p/stage.py`, `valence_core/p/guard.py`; and the three `LOCK-p-OLMo-*.md` v0.2 files. Local paths below are written as `<repo>` and `campwire/`.

**Totals (74 claims):**
- CONFIRMED: 68
- IMPRECISE: 1 (row 36)
- FAIL: 0
- NOT CHECKABLE: 5 (the commit to come, twice; the v1.0 locks to come; the push; "committed by path")

**Forbidden content (a clock time or stamp, a `$` figure, a local absolute path, an email address): none found** in the entry or the raw.
- The raw's line 2 has `$PY` twice. It is a shell variable, not a `$` figure; the 2026-11-10 raw has the same text.
- Raw line 465 (analyzer output) has "A-m1:28" and "A-m1:40". These are document line references, not clock times.
- Raw line 447 (analyzer output) has "timestamp" and `'stamp': True`. This is the text of a check, not a stamp.
- No `/Users`, `/private`, `/tmp`, `/var`, `/home`, `/workspace`, `~/` or `file://` appears, and no user name or pod id. The only placeholders are `<repo>` (raw lines 2, 8 and 12) and `<tmp>` (raw lines 8 and 296).

### Claims

#### The entry

| # | Claim | Mark | Evidence | Accurate wording |
|---|---|---|---|---|
| 1 | Dated 2026-11-14 | CONFIRMED | The session date is 2026-11-14. The superseded path carries it. The BUILD (`c0f1c69`) and G-SHAPE-p (`f784bff`) entries have the same date, and this run follows both. | |
| 2 | "G-ANL-p — the canonical re-run" | CONFIRMED | Wrapper line 17 runs `scripts/p_analyze.py ganl` with no `--out`. `run_ganl` sets `canonical = out is None` (p_analyze.py:660–661). The final stdout line lacks the " -- an --out run, never of record" suffix. | |
| 3 | "on HEAD `f784bff`" | CONFIRMED | meta `head f784bff24f163c9690eba182f470fffbb26f1a1d` equals `git rev-parse HEAD` now. The wrapper refuses another HEAD (line 10), and `git mv` does not move HEAD. | |
| 4 | "(G-SHAPE-p's re-run committed on the campaign wiring's BUILD `c0f1c69`)" | CONFIRMED | `f784bff`'s parent is `c0f1c69`. Its subject begins "G-SHAPE-p -- the re-run of record on the campaign wiring's BUILD (c0f1c69)". `c0f1c69`'s subject begins "p -- the campaign wiring: BUILD". | |
| 5 | "PASS" | CONFIRMED | The artifact's `verdict` is "PASS". The last stdout line reads "G-ANL-p: PASS: …". | |
| 6 | "(p v0.2 §4.4" | CONFIRMED | PROPOSAL-p v0.2 §4.4 ("The analyzer (rule 11) — route (b)") defines **G-ANL-p**. The artifact's `spec` reads "p §4.4; …". | |
| 7 | "the seat's read of G-F0m-OLMo (p) ×3, §4.3 item 2)" | CONFIRMED | The seat's file is titled "The seat's read of G-F0m-OLMo (p) ×3 (`a225a89`) …". §4.3 item 2 reads "… its BUILD, blind review and values-check, and G-SHAPE-p's and G-ANL-p's re-runs land after G-PWR's entry …". The order holds: `3e1b614` (G-PWR) < `c0f1c69` < `f784bff` < this run. | |
| 8 | "`scripts/p_analyze.py ganl` writes `data/p/gates/G-ANL-p.json`" | CONFIRMED | Wrapper line 17. The stdout's INVOCATION line names `scripts/p_analyze.py ganl`. The last line names `data/p/gates/G-ANL-p.json`, and the file exists (`?? data/p/gates/G-ANL-p.json`). | |
| 9 | sha256 `d285d77645e309982329b6263e3fdf0bc4f5e802edba5acd885b6b9430c15604` | CONFIRMED | `shasum -a 256` gives the same value. meta `new_sha` and the stdout's last line are equal to it. | |
| 10 | "once" | CONFIRMED | The stdout reads "(written; …)". `guard.write_once_bytes` returns "written" only when no file stood at the path (guard.py:151–181). Otherwise it returns "identical" or raises GuardStop. | |
| 11 | "m's battery passes 525/525" | CONFIRMED | stdout: "525/525 m_analyze battery checks pass" and "check count 525 == EXPECTED_CHECKS 525". The artifact's `m_battery` has `checks_pass` 525, `checks_total` 525 and `ok` true. | |
| 12 | "and reaches all 538 coverage ids" | CONFIRMED | stdout: "coverage: every one of the 538 required ids reached []". The artifact's `m_battery.coverage_ids` is 538. | |
| 13 | "then G-ANL-p's 14 checks pass" | CONFIRMED | stdout lines 528–541 are the 14 "ganl-p:" checks, all after m's battery (lines 13–527), then "14/14 G-ANL-p checks pass". The artifact's `battery` has `checks_pass` 14, `checks_total` 14 and 14 names. | |
| 14 | "`ba89279`'s artifact is superseded." | CONFIRMED (index and tree) | `git diff --cached --name-status` gives `R100 data/p/gates/G-ANL-p.json data/p/gates/G-ANL-p.superseded-2026-11-14.json`. A new artifact stands at the canonical path. The commit itself is row 21. | |
| 15 | "Model-free; nothing ran on a model or the box." | CONFIRMED | Importing `scripts/p_analyze.py` in a fresh venv `python -I -B` loads no torch, transformers, mlx, mlx_lm, tokenizers or safetensors module (numpy only). No import of those libraries appears, at module level or indented, in `scripts/{m,p}_analyze.py`, `valence_core/{m,p}/*.py`, `session.py` or `e2d/*.py`. m_analyze.py:144–146 calls its imports "the declared model-free primitives (PIN-1)". The wrapper ran in the laptop repository (its line 6). The pod was terminated on 2026-11-12, and a replacement comes only after v1.0 (the seat's §4.1 and §4.3 item 4). | |
| 16 | "**The supersession** (F-p12's form)" | CONFIRMED | F-p12 (the seat's answers of 2026-11-08, §2): the earlier artifact is "superseded", "stays in history, and the re-run's entry says so". The 2026-11-10 G-ANL-p entry uses the same heading and form. | |
| 17 | "Before the run" | CONFIRMED | Wrapper line 16 (`git mv`) precedes line 17 (the run). | |
| 18 | "`ba89279`'s artifact (sha256 `90d0d5d6…8f2e`)" | CONFIRMED | Three values are equal: meta `old_sha` 90d0d5d6…cce48f2e, the superseded file's sha256, and the 2026-11-10 entry's sha256. `git rev-parse ba89279:data/p/gates/G-ANL-p.json` = HEAD's = `git hash-object` of the superseded file = d5749330…. `ba89279` is the path's last commit (`git log`). | |
| 19 | "was moved with `git mv` to `data/p/gates/G-ANL-p.superseded-2026-11-14.json`" | CONFIRMED | Wrapper line 16 is `git mv "$OLD" "$NEW"`, with NEW set to that path (line 13). The index holds the rename (R100). The index blob at the new path is d5749330…. | |
| 20 | "It is kept in history" | CONFIRMED | `ba89279:data/p/gates/G-ANL-p.json` resolves to blob d5749330…, the superseded file's. | |
| 21 | "and the move is committed here." | NOT CHECKABLE | A future act. The rename is staged now. | |
| 22 | "**The run.** At `f784bff`" | CONFIRMED | As row 3. | |
| 23 | "at `nice -n 19`" | CONFIRMED | Wrapper line 17: `nice -n 19 "$PY" -B scripts/p_analyze.py ganl`. | |
| 24 | "exit 0" | CONFIRMED | meta `exit 0` (RC is captured right after the run, line 18). | |
| 25 | "stderr empty" | CONFIRMED | `ganl_stderr.txt` is 0 bytes. | |
| 26 | "Before the move, the re-run's wrapper checked that `data/p/gates`, `valence_core` and `scripts` were clean." | CONFIRMED | Wrapper line 11 requires `git status --porcelain -- data/p/gates valence_core scripts` to be empty and exits 11 otherwise. It comes before the `git mv` (line 16). The meta file is written only after the run (line 20), so its presence shows the check passed. | |
| 27 | "The run's canonical binding check passed: m's analyzer at its pin, both analyzers and the code of record committed at HEAD, D_p against PROPOSAL-p." | CONFIRMED | `run_ganl` prints "REFUSED: G-ANL-p: …" to stderr and returns 2 if `binding_problems(canonical=True)` is non-empty (p_analyze.py:662–665). It checks again after the battery (STOP, exit 4, lines 669–672). Exit 0 with empty stderr means both checks passed. The function's docstring has the same three parts (p_analyze.py:84–86). Re-evaluated now, it returns []. | |
| 28 | "Raw: [`_p-ganl`](results/raw/2026-11-14_p-ganl.txt)" | CONFIRMED (as declared) | This is the brief's declared commit path, and nothing exists there yet (`ls results/raw`). The link has the 2026-11-10 entry's form. | |
| 29 | "with the repository's prefix scrubbed to `<repo>`" | CONFIRMED | The raw's body after "## stdout" (lines 12–554) equals `ganl_stdout.txt` byte for byte once the repository prefix is replaced by `<repo>` (`diff -q`, rc 0). The prefix occurred once, on the INVOCATION line. | |
| 30 | "**The battery.** m's 525/525" | CONFIRMED | As row 11. | |
| 31 | "its check count and coverage those of G-ANL-F3's artifact" | CONFIRMED | stdout line 528: "ganl-p: m's battery runs unchanged and passes, its check count and coverage those of G-ANL-F3's artifact". `data/m/gates/G-ANL-F3.json` (clean in git) records `battery.checks_total` 525 and `coverage_ids` 538. These equal G-ANL-p's `m_battery.g_anl_f3` and its own counts. | |
| 32 | "then G-ANL-p's 14, all PASS" | CONFIRMED | As row 13. The stdout has 539 `[PASS]` lines (525 + 14) and no `[FAIL]` line. | |
| 33 | "the groups as at `ba89279`" | CONFIRMED | The 14 `battery.checks` names equal the superseded artifact's (a full-tree comparison found no difference outside row 50's two values). stdout lines 528–541 equal the 2026-11-10 raw's. | |
| 34 | "Among them: the Q-F0 and NOT-RUN regressions, byte for byte" | CONFIRMED | Checks 12 and 13 (stdout lines 539–540) both end "byte for byte". In the artifact, `regression_qf0.outputs` (2 files) and `regression_not_run.outputs` (3 files) are each `identical: true` with `error` null, and `m_outputs_identical` is true. | |
| 35 | "and `data/p` untouched by the battery (N11)" | CONFIRMED | Check 14 (stdout line 541): "ganl-p: data/p is untouched by the battery -- every file's sha256 before and after (N11)". | |
| 36 | "The run's stdout equals `ba89279`'s raw line for line, but for p's package and the artifact's sha256s." | IMPRECISE | The two stdout sections have 543 lines each, and 542 are identical. Only the last line differs: "G-ANL-p: PASS: … (written; sha256 90d0d5d6…)" against "(… d285d776…)". p's package sha256 is printed in neither stdout: no line carries a38d93bb… or 08bfa693…, and `ganl` prints no package hash at all. The package hash lives only in the artifact (row 50). The equality holds; the "p's package" exception does not. | "The run's stdout equals `ba89279`'s raw line for line, but for its last line, the artifact's sha256." |
| 37 | "**The artifact** (schema `p-ganl-v1`" | CONFIRMED | `schema` "p-ganl-v1" (= `GANL_SCHEMA`). | |
| 38 | "verdict PASS), read back" | CONFIRMED | `verdict` "PASS", read by `json.load` of the written file. | |
| 39 | "the analyzers: m's `d347ea0c…5e48`" | CONFIRMED | The value is `analyzers["scripts/m_analyze.py"].sha256` and `code.m_analyzer_sha256`. It equals `shasum` of the file, `M_ANALYZER_SHA256` (p_analyze.py:58) and HEAD's blob. | |
| 40 | "and p's `d3758fc4…7008`" | CONFIRMED | The value is `analyzers["scripts/p_analyze.py"].sha256` and `code.p_analyzer_sha256`. It equals `shasum` of the file, and the working tree equals HEAD's blob. | |
| 41 | "unchanged" | CONFIRMED | The superseded artifact records both values identically. | |
| 42 | "the packages: m's `7756dcf4…49bb`" | CONFIRMED | `code.m_package_sha256` = `m_resume.package_sha256()` now. The superseded artifact has the same value. | |
| 43 | "and p's `a38d93bb…a2d7`" | CONFIRMED | `code.p_package_sha256` = `analyzers["valence_core/p"].package_sha256` = the brief's `guard.package_sha256()` command = a38d93bb83b64400…ed5ba2d7. | |
| 44 | "the BUILD's" | CONFIRMED | The BUILD entry's Licence line gives the same full hash ("the qual wiring's was `08bfa693…fa26`"). | |
| 45 | "which G-SHAPE-p's re-run records" | CONFIRMED | `data/p/gates/G-SHAPE-p.json` (HEAD's blob, last committed at `f784bff`, sha256 4a4fdee5…d06d as that entry states) has `provenance.p_package_sha256` a38d93bb…a2d7. | |
| 46 | "`proposal_sha256`, m's pin `42ab36ec…6c6b`" | CONFIRMED | The field is 42ab36ec…9fc96c6b. It equals m_analyze.py:98 `PROPOSAL_SHA256` and the sha256 of `PROPOSAL-m-gating-campaign-v1_11.md`. stdout's first check: "sha256 is the pinned v1.11's (42ab36ec...6c6b)". | |
| 47 | "and `proposal_p_sha256` `42f2977b…3b32`" | CONFIRMED | The field is 42f2977b…23cf3b32. It equals `gcal.PROPOSAL_P_SHA256` and the sha256 of `PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md`, which is clean and equal to HEAD's blob. | |
| 48 | "(F-p8)" | CONFIRMED | The locks' line reads "**The proposal pin** (F-p8): `PROPOSAL-m-gating-campaign-v1_11.md` sha256 `42ab36ec…` in every p output's `proposal_sha256`; PROPOSAL-p … sha256 `42f2977b…`" (LOCK-p-OLMo-dpo.md:103). The 2026-11-10 entry uses the same tag. | |
| 49 | "against `ba89279`'s artifact, two values differ" | CONFIRMED | A recursive comparison of the two JSON trees (same keys, same list lengths) gives exactly 2 differing leaves. | |
| 50 | "both p's package sha256 (`code.p_package_sha256` and `analyzers["valence_core/p"].package_sha256`)" | CONFIRMED | The two leaves are exactly these, 08bfa693…fa26 → a38d93bb…a2d7. | |
| 51 | "The stage's staleness check reads it as current." | CONFIRMED | `stage.stale_problems(GANL_REL, art, art.get("code") or {}, ("p_package_sha256", "m_package_sha256", "m_analyzer_sha256", "p_analyzer_sha256"))`, called as `lock_required` calls it (stage.py:449–450), returns []. On the superseded artifact it returns one problem, p's package (08bfa693… vs a38d93bb…), so the check discriminates. | |
| 52 | "**Next:** LOCK-p v1.0 ×3, drafted for the seat's read" | CONFIRMED | The BUILD entry's Next reads "LOCK-p v1.0 ×3, drafted for the seat's read (D_p 2026-12-15)". G-SHAPE-p's Next reads "then LOCK-p v1.0 ×3, drafted for the seat's read". The seat's §4.3 item 3: "The seat reads each v1.0 before the PI commits it." | |
| 53 | "(D_p 2026-12-15)" | CONFIRMED | p v0.2 §5.3 (line 100): "D_p: each `LOCK-p-OLMo-{ckpt} v1.0` is committed by 2026-12-15". `analysis.D_P` is "2026-12-15". The artifact's `d_p` is {date 2026-12-15, problems []}. | |
| 54 | "They name this artifact and G-SHAPE-p's." | NOT CHECKABLE | The v1.0 locks do not exist yet. The claim is grounded in code: `lock_required` puts both artifacts' sha256s among the values a lock must name (stage.py:441–452). The precheck, at `campaign` too, refuses a lock that does not name each one (stage.py:603–614). All three v0.2 locks name both (lines 33–34). | |
| 55 | "Not pushed." | NOT CHECKABLE | This concerns the commit to come. It is consistent with now: the local `origin/main` is `16c99d5`, and 34 commits on HEAD (`f784bff` among them) are not in it. No remote was contacted. | |
| 56 | "Committed by path." | NOT CHECKABLE | A future act. | |

#### The raw (`ganl_raw.txt`): header lines 1–9 and body

| # | Claim | Mark | Evidence | Accurate wording |
|---|---|---|---|---|
| 57 | Title: "the canonical re-run on HEAD f784bff (G-SHAPE-p's re-run committed on the campaign wiring's BUILD c0f1c69)" | CONFIRMED | As rows 2–4. | |
| 58 | Title: "p v0.2 s4.4; the seat's read of G-F0m-OLMo (p) x3, s4.3 item 2." | CONFIRMED | As rows 6–7. | |
| 59 | "Code's raw, PI date 2026-11-14." | CONFIRMED | As row 1. | |
| 60 | "Command: $PY -B scripts/p_analyze.py ganl (canonical: no --out), from the repository root, $PY = <repo>/jlens-qwen36/.venv/bin/python, under nice -n 19." | CONFIRMED | Wrapper lines 8 (PY), 9 (`cd "$REPO"`) and 17. The INVOCATION line shows the same interpreter (scrubbed) and argv; `-B` and `nice` are not in argv. | |
| 61 | "the re-run's wrapper (Code's scratch script) checked that HEAD was f784bff" | CONFIRMED | `campwire/ganl_rerun.sh` is a scratch script. Line 10 refuses a HEAD other than its argument, and meta records `head f784bff…`. | |
| 62 | "that git status --porcelain -- data/p/gates valence_core scripts was empty" | CONFIRMED | Wrapper line 11, byte-exact command. | |
| 63 | "and that the superseded path was absent" | CONFIRMED | Wrapper line 14: `[ ! -e "$NEW" ]`, exit 12 otherwise. | |
| 64 | "it then moved ba89279's artifact (sha256 90d0d5d667feadaf718e317d43b5bd83400b61102a6a56962adbb472cce48f2e) with git mv, outside the analyzer, to data/p/gates/G-ANL-p.superseded-2026-11-14.json" | CONFIRMED | The full hash equals meta `old_sha` (computed at line 15, before the move) and the superseded file's sha256. The `git mv` is the wrapper's (line 16), not the analyzer's. | |
| 65 | "(F-p12's supersession;" | CONFIRMED | As row 16. | |
| 66 | "the move is committed with this raw)" | NOT CHECKABLE | A future act. The rename is staged. | |
| 67 | "ran the command and recorded its exit." | CONFIRMED | Wrapper lines 17, 18 and 20. | |
| 68 | "Exit 0; stderr empty." | CONFIRMED | As rows 24–25. | |
| 69 | "The run's canonical binding check passed (binding_problems(canonical=True): m's analyzer at its pin, both analyzers and the code of record committed at HEAD, D_p against PROPOSAL-p)." | CONFIRMED | As row 27. | |
| 70 | "Artifact data/p/gates/G-ANL-p.json, sha256 d285d77645e309982329b6263e3fdf0bc4f5e802edba5acd885b6b9430c15604, written once." | CONFIRMED | As rows 9–10, with the full hash equal. | |
| 71 | "Model-free: no model, no tokenizer, no pod." | CONFIRMED | As row 15. | |
| 72 | "No clock time is recorded." | CONFIRMED | No clock time appears in the raw or the entry (scanned for hh:mm, hh:mm:ss, ISO `T` times, UTC/GMT/EST/PST/AM/PM). The only hh:mm-shaped match is raw line 465's "A-m1:28" and "A-m1:40", which are line references. The wrapper and meta record no time: meta has only old_sha, exit, new_sha and head. | |
| 73 | "Local absolute paths scrubbed: the repository's prefix shown as <repo>, temporary paths as <tmp>; nothing else changed." | CONFIRMED | As row 29: one substitution, and the body equals the stdout otherwise. The raw's one `<tmp>` (line 296) was printed so by the analyzer itself (O-2). | |
| 74 | The stdout section (lines 12–554) | CONFIRMED | Byte-equal to `ganl_stdout.txt` after the scrub, 543 lines: 539 `[PASS]`, 0 `[FAIL]`, "525/525 m_analyze battery checks pass", "14/14 G-ANL-p checks pass", and the final PASS line with d285d776…5604. | |

### Observations (not marked)

- **O-1 (row 36).** `ganl` prints no package sha256 at all. p's package appears only in the artifact (`analyzers`, `code`). G-SHAPE-p's stdout does print its provenance sha16s, which may be where the clause came from. The two stdouts differ only in the artifact's sha256 on the last line.
- **O-2 (row 73).** The `<tmp>` on raw line 296 is the analyzer's own scrub: m_analyze.py:5031–5035, `_Battery.clean`, replaces its temp directories with "<tmp>" before printing. The raw's own substitution changed one line, the INVOCATION (line 12). The 2026-11-10 raw's header has the same sentence. Nothing in it is false.
- **O-3 (rows 14, 21, 66).** In the index, the canonical path is deleted (R100 to the superseded path) and the new artifact is untracked. A by-path commit has to name both `data/p/gates/G-ANL-p.json` and `data/p/gates/G-ANL-p.superseded-2026-11-14.json` to carry the move and the new artifact together, as `ba89279` did (M + A).
- **O-4 (row 51).** `lock_required`'s full read of the artifact (`_artifact`, stage.py:293–309) requires it to be committed at HEAD. Until the commit, it reports G-ANL-p's artifact as not committed. Only the staleness part was run here.
- **O-5 (cosmetic).** Entry line 5 is 139 characters and line 14 is 125, while the entry's other lines are at most 117. The draft has no values-check line yet; the G-SHAPE-p entry carries one.

### Disclosures

Every command that touched `data/`. None touched `data/*/ckpt` or `data/*/reports` by name, content or metadata.
1. `git status --porcelain data/p/gates`, and a bare `git status --porcelain` at the end (names only).
2. `ls data/p/gates` (name-only).
3. `shasum -a 256` of `data/p/gates/G-ANL-p.json`, of `data/p/gates/G-ANL-p.superseded-2026-11-14.json` and of `data/p/gates/G-SHAPE-p.json`.
4. Digests only:
   - `git rev-parse` of `HEAD:` and `ba89279:` at `data/p/gates/G-ANL-p.json`;
   - `git rev-parse` of `:` (the index) at both G-ANL-p paths, the canonical one with `--verify -q`;
   - `git rev-parse HEAD:data/p/gates/G-SHAPE-p.json`;
   - `git hash-object` of the superseded file and of `G-SHAPE-p.json`.
5. `git log --format='%h'` over `data/p/gates/G-ANL-p.json`, `data/p/gates/G-SHAPE-p.json` and `data/m/gates/G-ANL-F3.json`.
6. Commands whose output names paths under `data/p/gates`:
   - `git show --name-status --format='%h'` of `ba89279`, `f784bff` and `c0f1c69`;
   - `git diff --cached --name-status` (a `--cached` form of item 1's `git diff --name-status`).
7. `git status --porcelain -- data/m/gates/G-ANL-F3.json`.
8. `json.load` (venv `python -I -B`) of the two G-ANL-p artifacts, of `data/p/gates/G-SHAPE-p.json` and of `data/m/gates/G-ANL-F3.json`, for fields and a full-tree comparison.
9. Imports of `valence_core.p.stage` and of `scripts/p_analyze.py` (by path) in fresh venv `python -I -B` processes, which ran:
   - `stage.stale_problems` and `stage.current_shas` on both G-ANL-p artifacts;
   - `binding_problems(canonical=True)` and `code_shas()`.

   An audit hook logged the `data/` files these processes opened. The stage's import opened `data/olmo/a1_repair_roster.json` (its own module-level read). Otherwise only my load of the new artifact appeared. `binding_problems` runs `git cat-file` and `git ls-tree -z` (no `-l`) over code files and PROPOSAL-p only.

Other commands, outside `data/`:
- `git grep` with item 3's form (`':!data/**'`), for `'<tmp>'`, `F-p12` and `F-p8`.
- `/usr/bin/grep` over single named files and globs of `.py` files.
- `git rev-parse` and `shasum` of commits, code files and the proposals.
- `git log --format='%h' -n 1 origin/main` and `git log --format='%h' origin/main..HEAD` (local refs only; no remote contacted).
- `ls results/raw`, `git ls-files`, and reads of RESULTS.md, PROPOSAL-p, the seat's answers, the locks, p's code and the scratch run outputs.

**Departures:**
- One recursive `/usr/bin/grep -rn -E` for model-library imports over `valence_core/m`, `valence_core/p`, `valence_core/session.py` and `valence_core/e2d`. It lacks item 3's exclusion form, but its roots cannot reach `data/`.
- The `git diff --cached --name-status` and `git hash-object` forms noted above.

Besides this report, `vc_ganl/` holds my working files: the two raws' stdout sections, the scrubbed stdout, their diff and the final status listing. Neither G-ANL-p nor any self-test was re-run. No model was loaded. Nothing was written to the repository; all Python ran with `-I -B`. The final `git status --porcelain` matches the starting snapshot: 33 lines, being the staged rename, the untracked new artifact and the 31 other untracked files. HEAD is still `f784bff`.
