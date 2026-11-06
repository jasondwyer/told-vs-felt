# G-SHAPE-F3: blind values-check of the entry and the raw (2026-11-06)

*Code's raw. One blind refuter (a general-purpose agent with no access to Code's reasoning) checked the G-SHAPE-F3 entry as drafted for RESULTS.md and the header of `results/raw/2026-11-06_mf3-gshape-f3.txt`, read-only, against the artifact `data/mf3/gates/G-SHAPE-F3.json`, the code at HEAD `cd9756e`, the design raw and the governing texts. Result: 46 items, 44 CONFIRMED, 0 FAIL, 2 IMPRECISE. No code changed after the BUILD commit, which its own blind code review covered, so this gate commit had no new code to review. Code re-checked both IMPRECISE items and the three notes at source (§2). The report is reproduced verbatim.*

## 1. The report (verbatim)

46 items: 44 CONFIRMED, 0 FAIL, 2 IMPRECISE.

## Claim-by-claim check

Method: I worked read-only, without loading a model. I ran `hashes` once. I ran three `gshape --out` trials into a scratch directory, with `-I -B`, and with an `open` audit hook on one of them. I recomputed the digests outside the code, using json.dumps with sort_keys, ensure_ascii=False, no indent, and a trailing "\n", which is m.resume.json_text. I checked each file against `git cat-file blob HEAD:<path>` and against the working tree. After all of this, `git status` shows no tracked change and the same 29 untracked entries as at the start. The artifact still hashes to 0f9b7bb9…6e9c. The raw hashes to c663b05d…3bda.

**Entry draft (scratch `gshape_entry_final.md`)**

1. **CONFIRMED.** The entry date is 2026-11-06. The run spans 23:43:08–23:43:14 UTC (raw:2, :13), which is 18:43 EST on 2026-11-06, the PI-local date. The artifact's mtime is 23:43:14 UTC.
2. **CONFIRMED.** "G-SHAPE-F3 — Q-F3's plumbing gate (m:290)": PROPOSAL-m-gating-campaign-v1_11.md:290 reads "**G-SHAPE-F3 (plumbing).**", under ":288 ### 3.2 Q-F3". The artifact's `spec` cites m:290.
3. **CONFIRMED.** "the canonical run on the BUILD (F3) commit (`cd9756e`)":
   - HEAD is cd9756e71c2c…. Its subject is "m package -- BUILD (F3): …". It was committed at 23:42:57 UTC.
   - The reflog shows no HEAD movement after it, and the run starts at 23:43:08 UTC.
   - raw:4 prints "canonical run". `committed_at_head` is true, and gshape.py:628 sets it only on the canonical path.
   - Note: the artifact does not record the commit hash. It is tied to HEAD only through file hashes that equal HEAD's blobs (items 10 and 27).
4. **CONFIRMED.** "PASS": `verdict` is "PASS" and `stop_reasons` is [].
5. **CONFIRMED.** The m:290 quotation matches word for word: proposal:290 reads "As G-SHAPE-F0 for the F3 templates, the reasoning header included." The entry drops only the final period. The text is identical to the artifact's `criterion`.
6. **CONFIRMED.** "read as the build design §7 composes it (PIN F56; flag F-3)":
   - design raw:138 is "## 7. G-SHAPE-F3's composition (F56)".
   - :113 (F56) reads "additions to 'as G-SHAPE-F0': the reasoning line's own placements (Layer R) and the build hazard's declared check … (Layer T); §7".
   - :157 reads "F-3. G-SHAPE-F3's Layers R and T (F56). (§7)".
7. **CONFIRMED.** "Model-free: no model, no generation, no pod":
   - gshape.py has no generate or model call.
   - A trial loaded no mlx, mlx_lm, torch, transformers or safetensors module. The only one of that group was huggingface_hub.constants, which supplies the cache path.
   - The artifact was written locally at the run's stamp, and the tokenizer comes from the laptop's hub cache.
8. **CONFIRMED.** "Layer T reads the Qwen tokenizer of record's tokenizer.json offline":
   - gshape.py:227–235 reads `<HF_HUB_CACHE>/models--mlx-community--Qwen3.6-27B-4bit/snapshots/c000ac2c…/tokenizer.json` and builds it with `Tokenizer.from_str`. No hub call is made.
   - c000ac2c… is the revision of record (LOCK-m-F0.md:433, :835) and is what `refs/main` names.
   - `shasum` of the file is 87a7830d63fcf43bf241c3c5242e96e62dd3fdc29224ca26fed8ea333db72de4, which equals `layer_t.tokenizer.sha256`.
   - The tokenizer's `truncation` is null, so every encode is untruncated.
9. **CONFIRMED.** "`python scripts/mf3_sessions.py gshape` on HEAD `cd9756e`": raw:3 reads "INVOCATION: <repo>/jlens-qwen36/.venv/bin/python scripts/mf3_sessions.py gshape". HEAD is as in item 3.
10. **CONFIRMED.** "every source, tooling and package file committed":
    - `provenance.sources`: all 38 files match HEAD and the working tree at the recorded sha256 (0 mismatches).
    - `import_closure`: 14/14 match in the same way.
    - The proposal and the three G-CAL inputs (the model-free, completability and seat-read files) are also committed and unedited.
    - Note: the audit hook shows one more repo file read, data/olmo/a1_repair_roster.json. It is read when valence_core/m/corr.py is imported (:133, `OLMO_ROSTER = olmo_roster()`) and is not in the sources map. It is committed and unedited (c82c6653…), so the claim holds, but the artifact does not record it.
11. **CONFIRMED.** Layer A "(the renders inside each contrast template's round templates, golds as responses)":
    - gshape.py:328–340 places each render inside the round template under Q, for keys.CONTRAST = (A1, A2, A3), and the scorer defaults to the gold.
    - design raw:140 uses the same words.
12. **CONFIRMED.** "A1 2,816, A2 1,408, A3 1,408 placements (5,632)": `layer_a.*.n` is 2816/1408/1408 and `layer_a_total` is 5632. That is 16 or 8 banners × 4 round templates × 22 render–gold pairs × 2 phases.
13. **CONFIRMED.** "0 fired, coverage exact": for A1–A3, `n_fired` is 0, `exact` is true and `n_misplaced` is 0.
14. **CONFIRMED.** "seg+gold 2,816/2,816, 1,408/1,408 and 1,408/1,408", required:
    - The artifact's figures match, with `required` true. evaluate enforces n_fired == n (gshape.py:610).
    - Note: the artifact files these controls under `layer_c`. The entry lists them in the Layer A bullet without naming Layer C, as raw:6–8 does.
15. **CONFIRMED.** "reasoning+seg+gold at the free phase 1,408/1,408, 704/704 and 704/704", required; "fire on every placement":
    - gshape.py:366 places this control only where phase == "free", which is half of each grid.
    - n_fired == n and `required` is true. "Every placement" holds over each control's own placements.
16. **CONFIRMED.** "Render-as-response, reported and not required, fires 256/2,816, 128/1,408 and 128/1,408": `required` is false and the figures match. It is in CONTROLS_REPORTED (gshape.py:84).
17. **CONFIRMED.** Layer R "(the reasoning line's own placements, every F3 template's banners × n 5–10 × every gold)":
    - gshape.py:423–430 iterates keys.TEMPLATES (six templates) and `_banners` (16 for A1 and A1s, 8 for the others).
    - The n range is banner.N_RANGE = range(5, 11), with 22 golds.
    - 64 × 6 × 22 = 8,448.
18. **CONFIRMED.** "8,448 placements, 0 fired, coverage exact": `layer_r.n` is 8448, `n_fired` is 0 and `exact` is true.
19. **IMPRECISE.** The Layer R bullet reports "0 fired" without its declared scope:
    - gshape.py:434 classifies each gold with n_tok=1, stop_reason "newline" and cap_hit False. So `empty` and `cap_no_newline` cannot fire there, and only echo and scaffold are tested.
    - The artifact's `layer_r.scope` and design raw:140 both say so, and RESULTS.md:101–102 discloses "Layer R's scope (finding 11)".
    - So two of Layer R's four fire fields cannot fire by construction.
20. **CONFIRMED.** "its required control (the reasoning block written into the line) 8,448/8,448": `layer_r.control` is {name "reasoning block + gold as the line", n 8448, n_fired 8448, required true}. Per gshape.py:445 the block's newlines are flattened to spaces and the gold follows. evaluate enforces it.
21. **CONFIRMED.** "Layer S (the runner's static scope): 0 problems": `layer_s.problems` is []. Rules S1–S6 are at gshape.py:480–535. design raw:140 reads "S: the runner's static scope".
22. **CONFIRMED.** Layer T "(the build hazard on the tokenizer of record, rule 28(d)(a) in its token, offset and decode forms)":
    - design raw:140 reads "Layer T, Code's declared check for the build hazard (answers:58)". answers:56 ties the "\n\n" to 28(d)(a).
    - `layer_t.forms` names exactly a token form, an offset form and a decode form (gshape.py:538–549).
    - Note: mf3/scaffold.py:155–171 calls its decode check "the character-offset form", and the BUILD entry says "by token comparison and by character offset". Layer T's "offset" is the tokenizer's own offsets, and its "decode" is that runtime form. The entry is consistent with the artifact, but a reader comparing the two entries may conflate the two names.
23. **CONFIRMED.** "640 joins, 0 failed": `layer_t.n` is 640 and `n_failed` is 0. That is 16 banners with (pi, mp) ∈ {(0,0), (3,1)}, × 2 starts, × (6 lines × 3 joins + 1 line × 2 joins).
24. **CONFIRMED.** "mf3 package `44110d15…3842`": `hashes` prints 44110d15941465c59ad01860b6027b98677aac361e76f0fd9185f392813a3842 over 15 files, which equals `provenance.package_sha256`.
25. **CONFIRMED.** "sources digest `8bbfe59f…5756` (38 files)": the recomputed value is 8bbfe59fcc93…31728d5756, equal to the artifact. The map has 38 files: 15 mf3, 11 m, 11 stack, and the driver.
26. **CONFIRMED.** "import-closure digest `23abe773…eec4`": the recomputed value is 23abe773f751…d049eec4 over 14 files, equal to the artifact.
27. **CONFIRMED.** "committed at HEAD: true": `provenance.committed_at_head` is true, and the independent check gives 38/38 and 14/14 (item 10).
28. **CONFIRMED.** Artifact path and sha256 `0f9b7bb9…`:
    - `shasum -a 256 data/mf3/gates/G-SHAPE-F3.json` gives 0f9b7bb962b7f0bd0bf0dffc7d7d06b65fbe62ca28a632c1f86789344eb36e9c.
    - The bytes equal json_text(artifact, indent=1).
    - The file is untracked, and its mtime is the run's end, 23:43:14 UTC.
29. **CONFIRMED.** Raw link and "local paths scrubbed": the file exists. No /Users, /private, /tmp or home path is left, and `<repo>` appears three times (raw:1, :3, :11).
30. **CONFIRMED.** "LOCK-m-F3 v0.1 names this artifact (m:292)": proposal:292 lists "G-SHAPE-F3's result".
31. **CONFIRMED.** "with mf3's package and the m files' hashes (the BUILD entry)": RESULTS.md:54–60 reads "The licence (Q1 (C2)), as LOCK-m-F3 v0.1 will name it". It lists (a) the package_sha256 44110d15… and (b) the eleven m files. Every value equals today's `hashes` output.
32. **CONFIRMED.** "and G-ANL-F3's analyzer and lexicons once G-ANL-F3 is built": proposal:292 reads "G-ANL-F3's analyzer and lexicon hashes". G-ANL-F3 is not built: scripts/m_analyze.py is still 655e0f7f…, last touched at ed8e886, and its mentions of G-ANL-F3 are forward references only.
33. **CONFIRMED.** "G-ANL-F3 lands only while no OLMo unit is open (Q3's rule)": answers:26 reads "G-ANL-F3's in-place commit lands only when no OLMo unit is open — 'open' from its LOCK v0.1 to its VERDICTS entry".
34. **CONFIRMED.** "No `LOCK-m-OLMo-*.md` exists at this commit":
    - `git ls-tree -r HEAD` lists only LOCK-m-F0.md among LOCK-m-* files.
    - The working tree's LOCK files are LOCK-g.md, LOCK-h.md and LOCK-m-F0.md.
    - `find` finds no LOCK-m-OLMo* anywhere.
35. **IMPRECISE.** "so neither order is fixed yet". The conclusion is true (design raw:129; RESULTS.md:73–74), but there are two problems:
    - (i) "order" has no antecedent. The entry never names Q3's two licensed orders (answers:26).
    - (ii) The stated premise alone does not entail the conclusion. Order (a) becomes fixed if G-ANL-F3 lands first, so the inference also needs "G-ANL-F3 is not built". RESULTS.md:73–74 and design raw:129 both state that premise.

**Raw (`results/raw/2026-11-06_mf3-gshape-f3.txt`)**

36. **CONFIRMED.** "the canonical run on the BUILD (F3) commit cd9756e": as item 3, and raw:4.
37. **CONFIRMED.** "(python scripts/mf3_sessions.py gshape …), from the repository root with the jlens venv (Python 3.12.9)":
    - raw:3 shows a relative `scripts/mf3_sessions.py`, which resolves only from the repository root, with sys.executable `<repo>/jlens-qwen36/.venv/bin/python`.
    - `--version` gives Python 3.12.9.
38. **CONFIRMED.** "every source committed at HEAD and unedited": raw:4, and raw:5 "committed at HEAD: True". See item 10.
39. **CONFIRMED.** "Model-free: no model, no generation, no pod; Layer T reads … tokenizer.json offline": see items 7–8.
40. **CONFIRMED.** "Code stamps: 2026-11-06 23:43:08 to 23:43:14 UTC (date -u, before and after the run, both lines below)":
    - raw:2 reads "Fri Nov  6 23:43:08 UTC 2026" and raw:13 reads "Fri Nov  6 23:43:14 UTC 2026".
    - The artifact's mtime is 23:43:14 UTC, and the BUILD commit was at 23:42:57 UTC.
41. **CONFIRMED.** Artifact path and sha256: as item 28, with the path at raw:11.
42. **CONFIRMED.** "Local absolute paths scrubbed … <repo>; nothing else changed":
    - raw:4–11 equal, byte for byte, the driver's canonical header line plus `gshape.summary_lines` regenerated from the artifact, with the path as `<repo>/data/mf3/gates/G-SHAPE-F3.json` (8/8 lines).
    - raw:3 has the driver's INVOCATION form.
    - The unscrubbed stdout is not on disk, so this is the strongest check available.
43. **CONFIRMED.** raw:5 checks out:
    - The renders sha256 a04f67b0…4372 equals the artifact's `inputs.renders_sha256` and recomputes from G-CAL_model-free.json's 16 renders.
    - The proposal sha256 42ab36ec…6c6b equals `shasum` of PROPOSAL-m-gating-campaign-v1_11.md, at HEAD and in the working tree.
    - The package hash 44110d15…3842, the sources digest 8bbfe59f…5756 (38 files) and "committed at HEAD: True" all match.
44. **CONFIRMED.** raw:6–9 counts equal the artifact's layer_a, layer_c and layer_r (items 12–20).
45. **CONFIRMED.** raw:10: Layer S has 0 problems; Layer T has 640 joins and 0 failed. "tokenizer sha256 87a7830d63fcf43b" is the first 16 hex characters of the file's sha256.
46. **CONFIRMED.** raw:11–12 read "G-SHAPE-F3 PASS … (written)" and "exit=0", consistent with gshape.EXIT["PASS"] = 0.

A trial run on the same tree reproduces the canonical artifact field for field. The one difference is `provenance.committed_at_head`, which is false on a test run. Every count and hash matches.

## FAIL items and corrections

None.

## IMPRECISE items and corrections

19. Replace the Layer R bullet with: "Layer R (the reasoning line's own placements, every F3 template's banners × n 5–10 × every gold): 8,448 placements, 0 fired, coverage exact. Each gold is placed as a line ended by its newline, so the structural classes (empty, cap reached) cannot fire there; echo and scaffold are its test (the artifact's `scope`; finding 11). Its required control (the reasoning block written into the line): 8,448/8,448."

35. Replace with: "No `LOCK-m-OLMo-*.md` exists at this commit and G-ANL-F3 is not built, so neither of Q3's two orders — (a) G-ANL-F3 before any LOCK-m-OLMo v0.1, (b) the OLMo track through its VERDICTS first — is fixed yet."

Three notes need no text change: item 10 (the OLMo roster read at import, outside the sources map but committed and unedited), item 14 (Layer C is never named), and item 22 (the offset and decode wording differs between Layer T and the runtime and BUILD entry).

## 2. Code's dispositions (each re-checked at source first)

| item | re-check at source | disposition |
|---|---|---|
| 19 | gshape.py `line_fires` classifies each gold with n_tok 1 and the newline stop; the artifact's `layer_r.scope` says the structural classes cannot fire there. | **Applied** in the entry, as suggested. |
| 35 | answers:26 names the two orders; the BUILD entry and design raw §6 state "G-ANL-F3 is not built". | **Applied** in the entry, as suggested. |
| 10 (note) | G-SHAPE-F0's sources map records `data/olmo/a1_repair_roster.json` beside its OLMo grids. G-SHAPE-F3's `STACK_FILES` has none of the OLMo files. `valence_core/m/corr.py:133` reads the roster at import (`OLMO_ROSTER`, in `ROSTERS_OF_RECORD`), and mf3's gshape calls nothing in `corr`: its renders are the committed renders of record, and its pool and roster are Qwen's. | **Disclosed, no change.** The OLMo roster enters no G-SHAPE-F3 computation, so it is outside the map by the map's own scope: the files whose edit changes the result. It is committed and unedited at `cd9756e`, as the refuter found. |
| 14 (note) | The artifact's `layer_c` holds the controls; the driver's summary lines print them on Layer A's lines. | **No change.** The entry follows the printed lines. |
| 22 (note) | `mf3/scaffold.assert_boundary`'s second form compares the decode of the prefix's tokens with the prefix's characters; Layer T's offset form uses the tokenizer's character offsets. | **No change.** Both describe rule 28(d)(a)'s character-offset boundary from two sides: the runtime decodes, and Layer T also checks the tokenizer's own offsets. The design raw §7 names Layer T's three forms. |
