# G-SHAPE-F0 and G-SHAPE-F3 re-runs (2026-11-07): blind values-check of the two entries and their raws (Code's raw)

*A blind values-check agent (fresh context, read-only) checked the drafts of the two RESULTS.md entries and the two run raws against the artifacts (new, superseded, and the superseded files' committed blobs), the packages recomputed on git-archive extractions, the seat's answers, PIN-S9 and PIN-S10, at HEAD `993eba1`. Its report follows verbatim, local paths scrubbed (`<tmp>` = Code's session scratch). Code's dispositions follow it.*

## 1. The report (verbatim)

56 items: 51 CONFIRMED, 3 IMPRECISE, 0 FAIL, 2 NOT CHECKABLE

HEAD was 993eba1 at the start and at the end. The repository was read only: no git state or artifact changed, and Python ran with -B (no .pyc written). Scratch files are in <tmp>/vc_gshape/ (flatten_compare.py, pkg_hashes.py, digests.py, git-archive trees).

How it was checked:
- Package hashes were recomputed with m's `resume.package_sha256_of` and mf3's `guard.package_sha256_of`. They ran on the working tree, and on git-archive extractions of 993eba1, db97d8e, 1bf94a6, cd9756e and e0b4f2c, with `resume.REPO` pointed at each extraction for the call.
- Digests were recomputed with `resume.json_text`. Every recorded file sha256 equals both the HEAD blob and the working tree.
- The leaf counts in the entries are scalar leaves. If empty lists and dicts count as leaves, the totals are 366 and 249 instead.

## G-SHAPE-F0 entry and raw (27 items: 25 C, 1 I, 1 NC)
1. C — The title (993eba1, before LOCK-m-F3 v0.1, PASS) matches the artifact's verdict PASS and empty stop_reasons.
2. C — `scripts/m_sessions.py` is in TOOLING_FILES (`valence_core/m/gshape.py:105`), which is PIN-S10's map (:233–236). 993eba1 edits it.
3. C — 993eba1 edits `valence_core/m/gcal.py`. m's package moves from 60199b36…feec (db97d8e, 18b0111) to 7756dcf4…49bb (993eba1 and the working tree).
4. C — The §7 quote "hygiene commit → G-SHAPE-F0 re-run …" is verbatim at the answers' line 50. That file equals its 139635f blob.
5. C — PIN-S9 (`gshape.py:1508–1517`) says supersession is "by hand only, on the seat's ruling … git mv … then writes the canonical name".
6. C — "No model, no tokenizer, no pod" matches the gshape docstring: "No model, no tokenizer, no generation."
7. C — The superseded file's sha256 is 9e0b28fe…a979. It is byte-identical to `git show db97d8e:` and to HEAD's blob, and db97d8e is the file's last commit.
8. C — The rename is staged in the index as R100 to the dated name.
9. NC — "committed with this entry" is in the future. It is consistent with the staged rename.
10. C — The command is `scripts/m_sessions.py gshape` with no --out, per the INVOCATION line. The reflog shows HEAD at 993eba1 from 19:23:57Z.
11. C — "Every … file committed": all 28 source/tooling files and all 14 closure files equal HEAD. `valence_core/m` has no diff and no untracked files.
12. C — 19:24:22Z–19:24:28Z equals gshape_f0.txt's birth and modification times. The artifact was written at 19:24:27Z.
13. **I** — The window includes the git mv. The superseded file's ctime is 19:24:24Z (a rename sets ctime on this volume; I tested it), two seconds after the window opens. The rename still came before the 19:24:27Z write. Fix:
   - entry: "…; the git mv, then the run: 19:24:22Z–19:24:28Z"
   - raw header: "19:24:22Z-19:24:28Z (Code's stamps, covering the git mv and then the run)".
14. C — Four grids of 2,816 each, 0 fired, 0 misplaced, coverage exact; grid_total 11,264.
15. C — seg+gold (required) is 2,816/2,816 on each unit. render-as-response (not required) is 256/2,816 on Q-F0 and 0/2,816 on each OLMo unit.
16. C — olmo_grids_identical is true, with one shared rows_sha256. template_shape has n_problems 0 and layer_s has no problems.
17. C — The package is 7756dcf4…49bb, recomputed.
18. C — The sources digest cc7c152a…2703 recomputes from the 26+2 map.
19. C — The closure digest 23abe773…eec4 covers 14 files, none under `valence_core/m`, and is unchanged from the old artifact. Optional: "(14 files outside `valence_core/m`; unchanged)", so "unchanged" cannot be read as covering the package.
20. C — 3 of the 346 leaves differ, all under provenance: package_sha256, sources_digest and tooling/`scripts/m_sessions.py` (f0e9d5c4… to 625ca1b8…). A byte diff shows the same three lines, and the file size is unchanged (17,091).
21. C — "Every result is identical": no leaf outside provenance differs.
22. C — The new artifact's sha256 is 38ba8e28…3b51, full value matching.
23. C — The raw body is byte-identical to gshape_f0.txt once the prefix is replaced with `<repo>`. INVOCATION is printed by the driver (`m_sessions.py:7392`); EXIT is the shell's.
24. C — No local path survives in the raw: it is ASCII only and holds 3 `<repo>` tokens. The rest of the header is accurate (s7 file, no --out, HEAD, old sha).
25. C — The F3 re-run ran on the same HEAD, at 19:24:56Z on 993eba1.
26. C — F3R-PREPRINT-OF-RECORD is at `m_analyze.py:9983–9986`, as the hygiene entry says.
27. C — Not pushed: origin/main is fb742e4 and main is 3 ahead.

## G-SHAPE-F3 entry and raw (29 items: 26 C, 2 I, 1 NC)
1. C — The title (on 993eba1, PASS) matches the verdict PASS and empty stop_reasons.
2. C — N3 and B's F-6/F-7 match RESULTS' G-ANL-F3 BUILD entry. mf3's package recomputes to 44110d15…3842 at cd9756e and 1bf94a6, and to f30ad505…6310 at e0b4f2c, 993eba1 and the working tree.
3. C — `scripts/mf3_sessions.py` is in TOOLING_FILES (`valence_core/mf3/gshape.py:91`). 993eba1 changes only its literal at :176–179.
4. C — The §7 quote is verbatim at line 50. Optional note: the literal reached the tree in the hygiene commit, ahead of the §7 order, which that entry discloses.
5. C — PIN-S9 is carried to mf3 at `mf3/gshape.py:654–655`.
6. C — The run is model-free. Layer T reads the snapshot's tokenizer.json offline (`tokenizer_of_record`), and the file on disk hashes to the recorded 87a7830d…2de4.
7. C — The superseded file's sha256 is 0f9b7bb9…6e9c, equal to `git show 1bf94a6:`, and 1bf94a6 is its only commit.
8. C — The git mv is staged as R100.
9. NC — "committed with this entry" is in the future.
10. C — The command, HEAD 993eba1 and "every source committed" all hold: 38 sources and 14 closure files equal HEAD, and committed_at_head is True.
11. C — 19:24:56Z–19:25:02Z equals gshape_f3.txt's birth and modification times. The artifact was written at 19:25:02Z, after F0's run ended at 19:24:28Z.
12. **I** — The window includes the git mv, the same issue as F0 item 13. The superseded file's ctime is 19:24:57Z. Fix: "…; the git mv, then the run: 19:24:56Z–19:25:02Z", and the same change in the raw header.
13. C — Layer A: A1 2,816, A2 1,408, A3 1,408; 0 fired; exact true.
14. C — seg+gold is 2,816/2,816, 1,408/1,408 and 1,408/1,408, all required.
15. **I** — "The required controls fire on every placement: … reasoning+seg+gold 1,408/1,408, 704/704 and 704/704". reasoning+seg+gold applies only at the free phase, so its n is half of each template's placements (layer_c; module docstring "at the free phase"). The 11-06 precedent says this. Fix: "…; reasoning+seg+gold at the free phase 1,408/1,408, 704/704 and 704/704."
16. C — render-as-response is 256/2,816, 128/1,408 and 128/1,408, with required false.
17. C — Layer R: n 8,448, 0 fired, exact; control 8,448/8,448, required.
18. C — Layer S has no problems. Layer T: n 640, n_failed 0.
19. C — The tokenizer value is the 16-hex prefix the driver prints. Optional: write "87a7830d63fcf43b…", since the entry elsewhere marks truncations with "…".
20. C — 6 of the 242 leaves differ, all under provenance. A byte diff shows the same six lines, and the size is unchanged (14,185).
21. C — The package change 44110d15… to f30ad505… is recomputed.
22. C — Attribution by blob hashes: `scripts/mf3_sessions.py` is 48008a53 at 1bf94a6 and e0b4f2c and fad31c20 at 993eba1. guard.py, readrule.py and stages.py change only at e0b4f2c, and that diff cites "the seat's F-6" and "F-7".
23. C — "Every result is identical": no leaf outside provenance differs.
24. C — The new artifact's sha256 is 0c9de56e…1461, full value matching.
25. C — The raw body is byte-identical to gshape_f3.txt after the `<repo>` substitution. INVOCATION is printed by the driver (`mf3_sessions.py:207`); EXIT is the shell's.
26. C — No local path survives in the raw: it is ASCII only. The rest of the header (N3 parenthetical, old sha, destination) is accurate.
27. C — m:292 is LOCK-m-F3 v0.1 and names "G-SHAPE-F3's result". §9 item 1 at line 64 reads "naming the analyzer, the lexicons, the re-run G-SHAPE-F3".
28. C — The canonical ganl waits for the N1 ruling, as in item 26 of the F0 entry.
29. C — Not pushed.

## 2. Code's dispositions

| Item | Verdict | Disposition |
|---|---|---|
| F0 13; F3 12 | IMPRECISE | Applied: each entry's window reads "the `git mv`, then the run", and each raw's header says its stamps cover the git mv and then the run. |
| F3 15 | IMPRECISE | Applied: "reasoning+seg+gold at the free phase". |
| F0 19 (optional) | CONFIRMED | Applied: "(14 files outside `valence_core/m`; unchanged)". |
| F3 19 (optional) | CONFIRMED | Applied: `87a7830d63fcf43b…`. |
| F0 9; F3 9 | NOT CHECKABLE | The commits follow at once: G-SHAPE-F0's, then G-SHAPE-F3's. |
