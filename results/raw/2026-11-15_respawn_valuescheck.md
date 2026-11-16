# BACKEND — characterization (2026-11-15) for pod m43y3deb1gq3rp, the dated note on the LOCK-p-OLMo-{sft,dpo,instruct} v1.0 entry, the two respawn raws and the commit message: blind values-check, two passes

*Code's raw, PI date 2026-11-15. Two blind values-checks of this commit's texts, each by a fresh checker given the texts, the sources and the list of record v2's items 1–5 verbatim, and no conclusion of Code's: the first on the dated note, the two raws and the commit message as first drafted; the second, blind to the first, on the texts as revised, the `BACKEND — characterization` entry included.*

*Totals. First pass: 84 claims; 69 CONFIRMED, 5 IMPRECISE (rows 27, 61, 69, 70, 78), 0 FAIL, 10 NOT CHECKABLE. Second pass: 99 claims; 86 CONFIRMED, 2 IMPRECISE (rows 14, 24), 0 FAIL, 11 NOT CHECKABLE; "Nothing asked is missing."*

*How the first pass was applied (each in the checker's terms):*
- *Its observation 1 (the texts naming a `BACKEND — characterization` entry beside the dated note: m:251, `pq:`§4.3 item 4, the p stage's PIN, CLAUDE.md's respawn protocol): this commit adds that entry at the top of the Log, and the note on the v1.0 entry records the box, as `pq:`§4.3 item 4 has both. (a)'s line will cite this commit as that entry's hash.*
- *Its observation 3 (`pq:`§4.3 item 4's spec of record): the `~/.bashrc` hook was found absent and restored, and the entry says so, with the order disclosed (second pass, observation 1).*
- *Row 27: the determinism raw's header quotes the seat's §2 item 2 verbatim (extracted from the raw by script). Row 31: the box line's memory, driver and CUDA figures now come from nvidia-smi on this box. Row 61: "its scripts" is gone; the entry names the respawn scripts, the adapter, resume.py and the manifest. Rows 69 and 78: the entry quotes the seat's §2 item 3 verbatim. Row 70: the note names the values-check raw. Observation 4: the 51 files are reconciled with `pq:`'s 29. Observation 6: the seat's raw is named by its digest. Observation 8: the check's description of C says "max_kl = 0.0, under the 1e-3 bar". Observation 9: the description adds that each mutant also differs byte for byte.*
- *Observations 2, 5, 7, 10–13 change nothing or are carried by the above; observation 14 is the checker's disclosure for the list of record v2's item 8 (three recursive greps over Code's scratch folder did not prune a scratch test folder named data/p/reports, holding one stand-in file of Code's dry test, no campaign output; they printed only names of matching files, none from that folder). That scratch folder has since been deleted.*

*How the second pass was applied:*
- *Row 14: "at intervals of about 21 minutes after the first two" for the watch's cadence. Row 24: "every measuring command". Observation 1: the hook's order is named a departure from `pq:`'s order, in the entry and the commit message. Observation 3: `pq:`'s 29 is recorded as an observation for the seat. Observation 5: the price was relayed to the PI after the create. Observation 6: "the August pod". Observation 7: the create body's fields and nvidia-smi's figures are separate sentences. Observation 8: a box change mid-campaign has no restart route in this build, the restart being the seat's to route (each lock's §5). Observation 9: the seat's answers of 2026-11-14 are named by `fd74d3f6…e3ff` in the entry's header and Next. Observation 12: "as far as the provenance records them (six libraries and Python)". Observation 19: the precedents list 2026-08-23, 2026-08-24 and 2026-11-06.*
- *Observation 10: "22/tcp" is the create body's declared container port, as in `190ba90`'s entry; no public address or port of the pod is in any text. Observations 11 and 18: the tqdm timers and "PASS (cached path licensed)" are the box's stdout, verbatim; the locks fix the path uncached (m:267). Observations 2, 4, 13–17 and 20 change nothing; 20 is honoured at the commit (the respawn files' blob ids re-checked at that HEAD).*
- *Checked by tool after the edits: every quotation against its source; every full and short sha256 against the bytes; each raw's box bytes verbatim after its header; no clock time, money figure, pod address or local path in the texts.*

*The reports follow verbatim, except that the second report's one local path (its scratch folder) is replaced by `<scratch>`. In each report, "/Users/" and "/private/" name patterns the checker searched for, not paths.*

## The first pass, verbatim

Note: I could not save this report to VC/report.md. The harness refused the write ("Subagents should return findings as text, not write report files"), and I did not work around the refusal. If you need the file, save the text below yourself.

# Blind values-check: the respawn note, its two raws and its commit message

I read HEAD `3f017d8`, which had not moved by the end. The object as checked: SCR/note.md `ad74c6cc…7f2f`, SCR/msg.txt `c0fefdac…7dda`, SCR/2026-11-15_respawn_integrity.txt `1827a209…da71`, SCR/2026-11-15_respawn_determinism.txt `536e0357…1bd0`. I re-hashed all four at the end and none had changed. I edited nothing in the repository, ran no git command that writes, and ran nothing on a model or the box. My re-runs and simulations are in VC/ (`run_*.out`, `RESULTS.sim.md`).

## Claims

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| | **Integrity raw (7-line header)** | | |
| 1 | Step (i) per CLAUDE.md's respawn protocol, on the replacement box for p's three campaigns under LOCK-p-OLMo-{ckpt} v1.0 (`038bf3e`) | CONFIRMED | Each lock was last touched at `038bf3e`. RESULTS.md:385 (the v1.0 entry) blames to `038bf3e`. CLAUDE.md §Environment (i). |
| 2 | §5: the campaign's box is named by its identifier and recorded by a dated note on the v1.0 entry | CONFIRMED | Each lock's §5, the "The box" bullet. |
| 3 | The seat's answers of 2026-11-14: path, §2 item 2 | CONFIRMED | `fd74d3f6` raw §2 item 2 (respawn (i), (ii) → the dated note). |
| 4 | The PI's go "Go for the pod whenever you need it", PI date 2026-11-15, relayed by the coordinating session | CONFIRMED | Relay 1 quotes it verbatim, with a closing period, and dates it by the block header's PI date 2026-11-15. |
| 5 | PI-local date 2026-11-15 | CONFIRMED | The relay header. The read-back's UTC creation stamp falls on 2026-11-15 at UTC−5. The runs carry no stamp. |
| 6 | Pod `m43y3deb1gq3rp` (jspace-olmo-m) | CONFIRMED | Read-back `id` and `name`; pre-flight `pod=`. |
| 7 | 1 x NVIDIA A100-SXM4-80GB (driver 595.91.07) | CONFIRMED | Read-back gpu count 1 and id; the driver field of the pre-flight's GPU line. |
| 8 | US-CA-2; the image; volume o73qvy742n at /workspace | CONFIRMED | Read-back `dataCenterId`, `image`, `mounts`. |
| 9 | Created with qny1x4v8padeke's create body of 2026-11-06, field for field | CONFIRMED | The two create bodies are byte-identical (sha256 `8e02fba8…0042` each) and equal as JSON. Their 12 leaves: cloud, dataCenterIds, disk, gpu count/id/minCudaVersion, image, mount path/volumeId, name, ports, startSsh. The read-back agrees on every field it shows. That the 11-06 body is qny1x4v8padeke's rests on Code's transcript extraction; `190ba90`'s entry agrees (name, image, US-CA-2, disk 30, one port). |
| 10 | Box repo HEAD `eb3e08c524fe8ea7e8828c7d7fd5794f9a58ec15` | CONFIRMED | Pre-flight `box HEAD`; `git rev-parse eb3e08c` gives the same 40 hex. |
| 11 | "G-F0m-OLMo (p)'s sync" | CONFIRMED | RESULTS.md, the G-F0m-OLMo (p) ×3 entry: the repo was brought from `0afd842` to `eb3e08c` by bundle, and the runs ran "at `eb3e08c`". |
| 12 | Tracked files unmodified | CONFIRMED | Pre-flight `tracked modified: 0`, from `git status --porcelain --untracked-files=no` per SCR/preflight_respawn.sh. |
| 13 | Untracked: that stage's 15 outputs, by name | CONFIRMED | The pre-flight's 15 names, sorted, equal the 15 data/p names in `git show --name-only a225a89` (cmp). |
| 14 | The manifest read is data/olmo/manifest.json at that commit | CONFIRMED | box_respawn_check.py's MANIFEST default is the box repo's data/olmo/manifest.json, and the tree is clean. env.sh as recorded sets no MANIFEST (env.sh's bytes are not in the sources). |
| 15 | Manifest sha256 `d39e5066…ac3e` | CONFIRMED | At `eb3e08c`, HEAD and the worktree. |
| 16 | Five entries | CONFIRMED | base, sft, dpo, instruct, olmo2_instruct; files 7+7+7+8+22 = 51. |
| 17 | Unchanged since `0415438` | CONFIRMED | `git log --format=%h -- data/olmo/manifest.json` gives 0415438, 9cd324d, 75939ed. |
| 18 | Identical at the laptop's HEAD | CONFIRMED | Blob `66174d40…` at both `eb3e08c` and `3f017d8`. |
| 19 | box_respawn_check.py sha256 `8c410e33…18c2`, identical at both | CONFIRMED | That sha256 at `eb3e08c`, HEAD and the worktree; blob `db80f1f4…` at both. |
| 20 | COMMAND, cwd and env.sh sourced; the nohup wrapper is "the only addition" | NOT CHECKABLE | Not checkable as executed. It is consistent with the copy-back's source paths, the .exit files' `exit=` form and Code's plan (SCR/post_create.md). |
| 21 | EXIT exit=0 (the .exit file) | CONFIRMED | integrity.exit is `exit=0` plus a newline (`19eaf438…f061`; copy-back "identical"). |
| 22 | No launch or end stamp; no clock time in committed text | CONFIRMED | None in this raw (the scan in row 83). |
| 23 | Box file sha256 `39eca68c…4d35`, byte-identical after transfer | CONFIRMED | The SCR copy's sha256; the copy-back listing says "identical". |
| 24 | The box file follows the 7 `# ` lines byte for byte | CONFIRMED | The bytes after header line 7 equal integrity.txt exactly, and nothing follows. |
| 25 | Box output: 51 `ok` lines and "INTEGRITY PASS — 51 files … across 5 checkpoints" | CONFIRMED | Each 16-hex prefix equals the manifest's sha256 prefix, and the 51 (checkpoint, file) pairs equal the manifest's set. |
| | **Determinism raw (9-line header + appended check)** | | |
| 26 | Step (ii) (CLAUDE.md respawn protocol; ledger rule 2); `038bf3e`; §5 | CONFIRMED | As rows 1–2. |
| 27 | Quote of the seat's §2 item 2: "respawn (i) INTEGRITY, (ii) BACKEND → 641ee466f4553b6a → the dated note in RESULTS.md on the v1.0 entries; a differing identifier → STOP" | IMPRECISE | Not verbatim. The seat's text has " (`gl:`§B.3)" before the semicolon, and the quote drops it without an ellipsis; the backticks are also dropped. With those two removals the quote is an exact substring. |
| 28 | The PI's go (PI date 2026-11-15) | CONFIRMED | As row 4. |
| 29 | Run only after step (i) PASSED | NOT CHECKABLE | There are no stamps. It is consistent with integrity's exit=0. |
| 30 | BOX: pod, name, GPU, driver, data center, image, volume | CONFIRMED | As rows 6–8. |
| 31 | "(81920 MiB, …)" | NOT CHECKABLE | No source gives this box's GPU memory. The pre-flight queried name, driver_version, memory.used (0 MiB) and utilization.gpu. The read-back's `gpu.memory` is 125, which is not GPU MiB. The figure equals the one in 2026-11-06's raw, which was the old box. |
| 32 | Box repo HEAD `eb3e08c…` | CONFIRMED | As row 10. |
| 33 | box_determinism.py sha256 `934e01d4…28aa`, identical at the laptop's HEAD | CONFIRMED | That sha256 at `eb3e08c`, HEAD and the worktree; blob `e086b7b2…` at both. |
| 34 | olmo_hf.py and resume.py are identical too | CONFIRMED | Blobs `7e7dd3c1…` and `d96c6ee0…` at both. |
| 35 | env.sh sha16 `f5174faa745eca6e` | CONFIRMED | The pre-flight prints those 16 hex (it labels them "sha256" but cuts to 16). RESULTS.md records env.sh `f5174faa…` with C4's line. |
| 36 | env.sh holds CUBLAS_WORKSPACE_CONFIG=:4096:8, PYTHONPATH, HF_HOME, the venv and C4's RUNPOD_POD_ID line | CONFIRMED | By the record: the 2026-11-06 raw's ENV line (the pre-C4 file) plus RESULTS.md's C4 bullet (one export line appended, `a0587921…` → `f5174faa…`). The run's provenance shows `:4096:8`. env.sh's bytes are not in the sources. |
| 37 | C4's line exported m43y3deb1gq3rp | CONFIRMED | The pre-flight sources env.sh and prints `pod=m43y3deb1gq3rp`. |
| 38 | COMMAND `--stage base --repeats 5`, and the wrapper | NOT CHECKABLE | Not checkable as executed. Consistent: the artifact's `stage` is base and `repeats` 5, there are five probes in each of A, B and C, and the output path is the copy-back's. |
| 39 | A copy set aside before the run (plain cp), sha256 `61f160ea…5434` | CONFIRMED | The hash, by SCR before.json and the copy-back listing. "Plain cp" and the order are not checkable. |
| 40 | EXIT exit=0 | CONFIRMED | determinism.exit is `exit=0` plus a newline. |
| 41 | No launch or end stamp; no clock time in committed text | CONFIRMED | No stamp. The box stdout's progress bars carry load durations (row 83). |
| 42 | ARTIFACT sha256 `61f160ea…5434` equals the committed file byte for byte, and the copy set aside | CONFIRMED | The copy-back listing's box-side hash of /workspace/models/determinism_base.json; SCR new.json; data/olmo/determinism_base.json at HEAD (blob `690bce9f…`). |
| 43 | The committed file is left as it stands (the 2026-08-23 and 2026-11-06 precedent) | CONFIRMED | The file has one commit ever (`214fd17`, 2026-08-19). `190ba90`'s entry says: "As on 2026-08-23, the committed artifact is left as it stands". |
| 44 | Box file sha256 `68e33673…33ba`, byte-identical after transfer | CONFIRMED | The SCR copy; copy-back says "identical". |
| 45 | Structure: 9 `# ` lines, the box file byte for byte, then the check | CONFIRMED | The box bytes are exact, its 16 CRs included. Then come 3 `# ` lines, then SCR/laptop_check_out.txt byte for byte. |
| 46 | INVOCATION | CONFIRMED | Reproduced: the same four-argument call exits 0, and its output is byte-identical to laptop_check_out.txt (`3dd8de59…54ea`). |
| 47 | "What it does": the field walk; A, B, C; the identifier on the printed block, cross-checked; exit 0 only if every check holds and all three ids are 641ee466f4553b6a | CONFIRMED | Read in check_determinism.py. Exit 0 needs byte identity, 0 differences, A, B, C, both provenance equalities and the three ids. Its C conjunct also needs max_kl == 0.0 (observation 8). |
| 48 | On 2026-11-06's record it prints that raw's thirteen check lines identically | CONFIRMED | SCR/test/stdout_1106.txt equals the 2026-11-06 raw's box segment byte for byte. Re-run with the committed artifact in both places, it exits 0; lines 1–13 equal that raw's 13 and lines_1106.txt, and line 14 is "CHECK PASSED…". |
| 49 | It refused (exit 1) two mutated artifacts: one with another GPU name, one with a kernel-path KL above zero | CONFIRMED | Re-run: exit 1 each, with either stdout, and the outputs are byte-identical to mut_gpu.out and mut_c.out. mut_gpu changes provenance/gpu (new-block id `1b50fa846475ac88`); mut_c sets C max_kl 0.0002 and all_exact False. |
| 50 | "2026-11-06's check rewritten after scratch cleanup" | NOT CHECKABLE | The earlier script is not available. |
| 51 | "Its last line is new" | CONFIRMED | The 2026-11-06 raw ends at "ALL OF A, B, C EXACT: True". |
| 52 | The appended 14 lines equal SCR/laptop_check_out.txt, and the check exits 0 on the new material | CONFIRMED | My re-run on data/olmo/determinism_base.json, the new artifact and determinism.txt reproduced the file byte for byte, exit 0. |
| 53 | Its figures: `61f160ea…` both, 2819 bytes, 108 leaves, 0 differences, A, B and C exact | CONFIRMED | Also read directly from the new artifact: A all_exact, max_abs 0.0, max_kl 0.0; B repeat_all_exact, 0.0 ×3; C all_exact, max_kl 0.0. |
| 54 | Backend identifier `641ee466f4553b6a` on all three blocks | CONFIRMED | I computed it two ways: with `valence_core.m.resume.backend_identifier` (HEAD's resume.py), and with my own re-implementation (sha256 of the sort-keyed compact JSON minus n_encodes_clipped, path and seed; first 16 hex). Both give it on the printed block (taken by my own parser; the stdout has one such block), on the new artifact's provenance and on the committed one's. The printed block equals both. |
| | **The note** | | |
| 55 | Dated note (PI date 2026-11-15), the pod session's; each lock's §5; the seat's §2, item 2 | CONFIRMED | Lock §5 and `fd74d3f6` §2 item 2 call for it. |
| 56 | The PI's go, PI date, relayed | CONFIRMED | As row 4. |
| 57 | Created on the spec of record: 1 × A100-SXM4-80GB, Secure, US-CA-2, the image, the volume at /workspace | CONFIRMED | The read-back, which matches `gl:`§B.3's statement of the spec. Observation 3 covers what `pq:`§4.3 item 4 adds. |
| 58 | qny1x4v8padeke's create body, field for field | CONFIRMED | As row 9. |
| 59 | The respawn protocol ran before any experimental forward | CONFIRMED | CLAUDE.md's wording. The pre-flight is read-only and found the GPU idle (0 MiB used, 0 %), and nothing else on the pod is recorded. |
| 60 | At the box repo's `eb3e08c` | CONFIRMED | As row 10. |
| 61 | "(its scripts and manifest identical to this commit's)" | IMPRECISE | True of both respawn scripts, olmo_hf.py, resume.py and the manifest at HEAD `3f017d8`. But "its scripts" also reads as the box repo's scripts, and `eb3e08c..HEAD` changes five code files: scripts/mf3_gpwr.py A, scripts/mf3_sessions.py M, scripts/p_gpwr.py A, scripts/p_sessions.py M, valence_core/p/stage.py M. p's driver and stage are among them. "This commit" holds only while the commit's parent keeps these blobs. |
| 62 | (i): PASS, 51 files across 5 checkpoints, the manifest's five entries, exit 0 | CONFIRMED | Rows 16, 21 and 25. |
| 63 | The (i) raw's link and sha256 `1827a209…da71` | CONFIRMED | The SCR raw's sha256. The link is root-relative, like the entry's other links. |
| 64 | (ii): PASS, exit 0; A, B and C exact at 0.0; byte-identical; the identifier on the three blocks | CONFIRMED | Rows 40, 42, 53 and 54. |
| 65 | The (ii) raw's sha256 `536e0357…1bd0` | CONFIRMED | The SCR raw's sha256. |
| 66 | The identifier equals each lock's BACKEND OF RECORD line | CONFIRMED | Exactly one line `BACKEND OF RECORD 641ee466f4553b6a` per lock (sft :267, dpo :266, instruct :266). No other line carries the string. |
| 67 | The three lock sha256s | CONFIRMED | `fafb786d…2bc4`, `25c52f56…3dcf` and `f71c97c1…0e67` at the worktree, HEAD and `038bf3e`. They equal `038bf3e`'s entry and the seat's §0. |
| 68 | "so this box is the campaign's under each lock" | CONFIRMED | §5's conditions are met as written: the spec, the identifier, and a dated note on the v1.0 entry naming the pod id, the identifier, both raws, and each lock's path and sha256. Observation 1 qualifies this. |
| 69 | Next (the seat's §2, item 3): the bundle, this commit included; the precheck ×3 at `campaign` with (a)'s line, "which cites this commit and the respawn (ii) raw"; the campaigns at 2 h each, in this pod session | IMPRECISE | Each element is in item 3, but item 3's "looks every 40", "(d)'s line in each campaign raw after each invocation" and "the seat adjudicates every pause on the excerpt" are left out; `038bf3e`'s Next had quoted items 2–3 verbatim. "Which cites this commit" is Code's reading: the seat's §1 (a) and `038bf3e`'s entry say "the `BACKEND — characterization` entry's hash" (observation 1). |
| 70 | "Committed by path with the two raws." | IMPRECISE | The commit message adds the values-check raw, and the note has no values-check line. `0190c6d`'s and `ce3ed7c`'s texts name their values-checks, and `ce3ed7c` links its raw. |
| 71 | "Not pushed." (note) | NOT CHECKABLE | A future act. |
| 72 | Placed after the v1.0 entry's last bullet "  - Not pushed. Committed by path.", as one hunk | CONFIRMED | Simulated. HEAD's RESULTS.md:465 is that bullet (it blames to `038bf3e`; :467 opens the next entry). Inserting note.md after :465 gives one hunk, `@@ -465,0 +466,24 @@` (`git diff --no-index -U0`): 24 lines, widest 118, no trailing whitespace or tab. |
| | **The commit message** | | |
| 73 | Subject: the v1.0 entry (`038bf3e`), the pod, the identifier, the PI's go quote (relayed), the seat's answers of 2026-11-14 (`fd74d3f6...e3ff`, s2 item 2), the two raws by path | CONFIRMED | `fd74d3f6...e3ff` matches the file's sha256 `fd74d3f6e60d…a7e3ff` at HEAD (blob `c18d321b…`). |
| 74 | The pod bullet | CONFIRMED | Rows 6–9. |
| 75 | The (i) bullet, `1827a209...da71` | CONFIRMED | Row 63. |
| 76 | The (ii) bullet, `536e0357...1bd0` | CONFIRMED | Rows 64–65. |
| 77 | The identifier bullet; "the three sha256s in the note" | CONFIRMED | Rows 66–67. |
| 78 | The Next bullet | IMPRECISE | As row 69. |
| 79 | "RESULTS.md (the note, one hunk)" | CONFIRMED | Simulated, row 72. |
| 80 | "the two respawn raws and the values-check raw" | NOT CHECKABLE | The commit does not exist yet. This differs from the note's "with the two raws" (row 70). |
| 81 | "No laptop model process ran." | NOT CHECKABLE | Code's conduct. The laptop check imports only numpy and valence_core.m.resume (the adapters load lazily), so no model. |
| 82 | "Not pushed." | NOT CHECKABLE | A future act. |
| | **Content rules and relays** | | |
| 83 | No clock time, money figure, pod IP or port, local absolute path or email (the trailer aside) in the four texts | CONFIRMED | Regex scan of all four. Items found and cleared: (1) the determinism raw's box stdout (lines 10 and 55) carries 16 tqdm progress-bar frames, whose elapsed<remaining fields are weight-load durations of zero to one second with rates in it/s. These are durations, not clock times or stamps, as in 2026-11-06's raw. (2) Both raws' wrapper lines carry the shell's exit-status variable, the only dollar sign, not a money figure. (3) `:4096:8` is the cuBLAS workspace setting, not a port. (4) "2 h" is the hour cap. (5) The dates are calendar dates only (2026-08-19, -08-23, -11-06, -11-14, -11-15). (6) The only email is in the Co-Authored-By trailer. |
| 84 | The relays' fidelity to the chat | NOT CHECKABLE | Chat, not in the repository. |

**Counts:** 84 claims: 69 CONFIRMED, 5 IMPRECISE (27, 61, 69, 70, 78), 0 FAIL, 10 NOT CHECKABLE (20, 29, 31, 38, 50, 71, 80, 81, 82, 84).

## Observations

1. **A `BACKEND — characterization` entry, or the note alone.** Two groups of texts disagree:
   - These name an entry besides the dated note: m:251 ("each new box runs the respawn protocol (i)–(ii) and gets its own `BACKEND — characterization` entry"); PROPOSAL-p §6.2 (such an entry "if it is not `qny1x4v8padeke`"); the p stage's PIN at valence_core/p/stage.py:88 ("a new `BACKEND — characterization` entry, recorded by a dated note at the lock in force"); `pq:`§4.2 and §4.3 item 4; and CLAUDE.md's (ii) ("log it as a dated entry").
   - These name only the dated note: `fd74d3f6` §2 item 2; `gl:`§B.3 (the dated note "is a RESULTS.md entry under the lock's v1.0 entry"); each lock's §5; and both relays.

   The commit makes the note alone, and the note does not say whether it stands as this box's `BACKEND — characterization` record or whether that entry is still owed. The answer also decides what (a)'s line cites as "the `BACKEND — characterization` entry's hash": this commit (the note's reading, row 69), or `190ba90` (the only entry with that title). This is for the seat; at the least, the note could state its reading.
2. **Form.** `gl:`§B.3 points to "the lab's dated-note form (the pod session's notes `eb3e08c`, `0190c6d`)", and both of those are top-level dated entries. The note is a nested bullet on the v1.0 entry, which is where each lock's §5 ("on this lock's v1.0 entry"), `fd74d3f6` §2 item 2 and `038bf3e`'s Next put it. "Under the lock's v1.0 entry" reads both ways.
3. **Spec of record.** `pq:`§4.3 item 4 also lists "the `~/.bashrc` hook restored, `RUNPOD_POD_ID` exported for ssh shells (the `190ba90` FLAG), the venv's library versions untouched". The note names none of these.
   - The determinism raw covers the export (env.sh's C4 line), and covers the versions implicitly (printed provenance == committed: True).
   - The `~/.bashrc` hook appears nowhere and is not checkable. On 2026-11-06 it was found missing and restored (per `190ba90`).
   - `gl:`§B.3's statement of the spec leaves these items out, so whether they belong to "the spec of record" is the seat's reading.
4. **29 vs 51.** `pq:`§4.3 item 4 expects "(29 files against the manifest)". The run checked 51 because the manifest gained olmo2_instruct's 22 files at `0415438`, after 2026-11-06's 29/29. The note's 51 is right, but it does not reconcile the seat's figure.
5. **Rule 27.** `190ba90`'s entry listed the provenance: versions, CUDA, flags, seed, window and layers. The note carries only the identifier, which hashes all of these except the seed and path, and points to the raw, whose printed block carries them all.
6. Two seat raws are dated 2026-11-14: `fd74d3f6`, and `gl:` (= `6b963adf`). The note's "the seat's §2, item 2/3" names neither by path or hash; the entry around it and the commit message do.
7. "In this pod session" reads two ways: this Code session (the "pod session"), or one pod's lifetime (item 3's "one pod session"; rule 27). Both seem meant.
8. The raw's description of C ("all_exact and max_kl < 1e-3") is looser than the script, which also requires max_kl == 0.0 for exit 0. No effect here, since max_kl is 0.0.
9. Each mutated artifact would also be refused by its byte difference alone. Their own failing conjuncts show in the printed lines (provenance equality and the id for mut_gpu, C for mut_c), so the tests exercise them, but a refusal alone cannot isolate them.
10. SCR/test/stdout_1106.txt (`08d904b9…367f`) is the 2026-11-06 raw's box segment. That segment is the 2026-11-06 box file (`6b31aada…54e2`, as that raw names it) plus one trailing newline the raw added. No effect on the check.
11. Step (i)'s script hashes every file in the manifest's five checkpoint directories and refuses extras there. It does not hash the other files at the top level of /workspace/models/ (the stage JSONs, determinism_base.json, manifest.json), although CLAUDE.md says "every file under /workspace/models/". This was the same on 2026-11-06; it is not new.
12. `038bf3e`'s Next says the pod's "price is stated first". The price is in the chat (relay 2 records the coordinating session's read), not in the note, which fits the no-money rule.
13. SCR/copyback_respawn_out.txt gives the artifact's box path in full, not as "<ws>" as the brief says. No effect.
14. **Disclosure (mine).** Three recursive greps over SCR did not prune SCR/dtest/data/p/reports/. They searched for the GPU-memory figure, for "respawn_2026-11-15" and for the nohup wrapper.
    - That folder holds one file, OLMo-sft_campaign_report.json, which is Code's scratch dry-test material; no campaign has run.
    - The greps printed only the names of matching files, and none of them came from that folder.
    - Under list v2 item 3 a tree grep should prune */reports, so I disclose this for item 8.

    Every other read was of names or digests, or of content outside data/*/ckpt and data/*/reports.

## The second pass, verbatim

**Blind values-check, second pass: BACKEND entry, dated note, two respawn raws, commit message (read at HEAD 3f017d8)**

HEAD was 3f017d8 when I started and still 3f017d8 at the end. The files these texts rely on are clean in the tree. I changed nothing in the repository and ran no git write. My scratch files are in <scratch>/podwatch2/vc2/: quotes.py, shorts.py, the run_*.out files, RESULTS.head.md, RESULTS.sim.md and stdout_1106_exact.txt. I opened no file under data/*/ckpt or data/*/reports; I listed only names (`git show --name-only/--name-status a225a89`). I did not open the earlier pass's folder vc/, so my read stays blind.

Abbreviations: E = entry_backend.md, N = note.md, I = the integrity raw, D = the determinism raw, M = msg.txt (each with its line number). fd74 = the 2026-11-14 p-backend-line answers.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | E:1–3 header. Date 2026-11-15; pod m43y3deb1gq3rp; PROPOSAL-p's three campaigns; it cites the respawn protocol, m:251, pq:§4.3 item 4 and fd74 §2 item 2 | CONFIRMED | Each cited passage exists and asks for this. |
| 2 | The PI's go "Go for the pod whenever you need it", PI date 2026-11-15 (in E, N, I:1, D:1 and M) | CONFIRMED | The relay, Relay 1 line 2, character for character. The relay ends "…need it." with a period, and its header gives "PI date 2026-11-15". Whether the relay matches the chat is NOT CHECKABLE. |
| 3 | E:3–4 "(i) INTEGRITY PASS, 51/51 files" | CONFIRMED | The box file's last lines; 51 ok-lines; integrity.exit "exit=0". |
| 4 | E:4–5 A, B and C all exact at 0.0; the new artifact byte-identical | CONFIRMED | Box stdout; my re-run of the check. |
| 5 | E:5 the identifier is each LOCK-p v1.0's identifier of record | CONFIRMED | Exactly one `BACKEND OF RECORD 641ee466f4553b6a` line per lock: sft:267, dpo:266, instruct:266. |
| 6 | E:7–8 `pq:` = the seat's answers of 2026-11-12, sha256 a32d4d17…1112 | CONFIRMED | shasum gives a32d4d17c9d1…1112; the raw's header says "PI date 2026-11-12". |
| 7 | E:9–11 the pq:§4.3 item 4 quote, placed "after the spec of record" | CONFIRMED | pq: line 47, character for character. |
| 8 | E:12–14 fd74's path and sha256 fd74d3f6…e3ff, and the §2 item 2 quote | CONFIRMED | fd74 line 30. The final period is outside the quote. |
| 9 | E:16 pod id, name jspace-olmo-m | CONFIRMED | The read-back's id and name; pre-flight "pod=". |
| 10 | E:16 made by the RunPod MCP's `create-pod` | NOT CHECKABLE | The sources hold the create body and the read-back, not the tool call. |
| 11 | E:16–17 on the spec of record, with qny1x4v8padeke's 2026-11-06 create body, field for field | CONFIRMED | The two bodies are byte-identical (sha256 8e02fba8…0042, 9 fields) and match pq:'s spec. The read-back agrees on all 8 fields it shares with the body. Whether the bodies were extracted faithfully from the transcript is NOT CHECKABLE. |
| 12 | E:17–18 1 × A100-SXM4-80GB, 81,920 MiB, driver 595.91.07, driver CUDA 13.2 | CONFIRMED | hook_out lines 3–4; read-back gpu count 1 and cudaVersion 13.2. |
| 13 | E:18–20 Secure; US-CA-2; the image; volume o73qvy742n at /workspace; container disk 30 GB; port 22/tcp only | CONFIRMED | Create body and read-back; Relay 2. |
| 14 | E:21 the watch read A100-SXM4-80GB secure availability "about every 20 minutes" | IMPRECISE | 13 of the 14 intervals are 20.25–21.35 minutes. Reads 1 and 2 were 31 seconds apart. The log lines never name the GPU; they show price.secure 2.19, which is Relay 1's A100-SXM4-80GB Secure price. |
| 15 | E:21–22 the 15th read was the first to list US-CA-2 | CONFIRMED | Ticks 1–14 say "absent"; tick 15 says "LISTED". |
| 16 | E:22 the hourly price was read before the create | CONFIRMED | Tick 15 reads price.secure before "CREATED". |
| 17 | E:22 the price was "stated" before the create | NOT CHECKABLE | This happened in chat. |
| 18 | E:22–23 the coordinating session relayed the price to the PI | CONFIRMED (as received) | Relay 2: "I'm telling the PI the pod id and price now". That relay came after the create. Fidelity to the chat is NOT CHECKABLE. |
| 19 | E:23 no money figure is recorded | CONFIRMED | A scan of all five texts finds none. |
| 20 | E:23–24 list-pods before the create showed no pod of this session's; uimuzt7d890y5b EXITED, untouched | CONFIRMED | watch.log tick 15; Relay 2. |
| 21 | E:25–26 pq:'s words "the `~/.bashrc` hook restored, … untouched" | CONFIRMED | pq: line 47. |
| 22 | E:27 the hook (`source /workspace/env.sh`) was absent on the new container disk and is restored | CONFIRMED | hook_out line 7 "(absent before restore)"; line 8 shows it appended as line 103 of `~/.bashrc`. |
| 23 | E:27–28 restored "after the respawn runs" | NOT CHECKABLE | No stamps; only the brief describes the order. |
| 24 | E:28 "every command on the box sources `env.sh` itself" | IMPRECISE | The copy-back's two ssh commands (cp/tar and sha256sum; copyback_respawn.sh lines 11 and 13) do not source it. The pre-flight does (preflight_respawn.sh line 10), and so do (i) and (ii) by their raw headers. "Changes nothing measured" still holds. |
| 25 | E:29–30 env.sh, sha16 f5174faa745eca6e, exports RUNPOD_POD_ID by C4's line: m43y3deb1gq3rp in a non-interactive shell (env.sh sourced) and in an interactive one after the hook | CONFIRMED | Pre-flight lines 1–2; hook_out line 10; C4 at RESULTS.md:6347–6351. The digest is the committed env.sh, f5174faa745eca6e96ca… (results/raw/2026-11-08_gcal-p.txt line 561). |
| 26 | E:31 the venv's library versions are untouched, shown by printed provenance = committed provenance | CONFIRMED | The check line, my own comparison, and pre-flight line 3. |
| 27 | E:32–33 `box_respawn_check.py` re-hashed the manifest's files: 51 across the 5 named checkpoints, exit 0 | CONFIRMED | The box file, the .exit file, and the script's logic. |
| 28 | E:33–34 pq: expected 29; the fifth entry, olmo2_instruct's 22 files, came at 0415438, after 2026-11-06's 29/29 | CONFIRMED | The manifest holds 7/7/7/8/22. Its first four entries are unchanged from 190ba90, and 190ba90 is an ancestor of 0415438. |
| 29 | E:35 and E:38 raw digests 308d6020…3b8c and faca18c6…7f96 | CONFIRMED | The sha256 of each draft raw. |
| 30 | E:36 and D:1 (ii) ran only after (i) passed | NOT CHECKABLE | Order only, and no stamps by rule. |
| 31 | E:36 (ii) was `--stage base --repeats 5`, env.sh sourced, exit 0 | CONFIRMED | The .exit file; the artifact records stage "base" and repeats 5; provenance cublas ":4096:8". |
| 32 | E:40–44 the A/B/C table | CONFIRMED | Matches the box stdout, and is identical to 190ba90's table. |
| 33 | E:46–48 108 leaf fields each, 0 differences, byte-identical, 61f160ea…5434 | CONFIRMED | My re-run. |
| 34 | E:48 "As on 2026-08-23 and 2026-11-06" the committed artifact is left as it stands | CONFIRMED | RESULTS.md:21418 and :6542. The file's only commit is 214fd17 of 2026-08-19. |
| 35 | E:49–50 `backend_identifier` gives 641ee466f4553b6a on the printed, new and committed blocks | CONFIRMED | I computed it both through the module and by re-implementing it: sha256 of the compact sorted JSON without n_encodes_clipped, path and seed, first 16 characters. |
| 36 | E:50–51 the laptop check is appended; it is 2026-11-06's check, rewritten; the raw says how it was tested | CONFIRMED | D lines 64–80, and my reproduction. That scratch cleanup was the reason for the rewrite is NOT CHECKABLE. |
| 37 | E:52–55 the provenance list, equal to 2026-11-06's | CONFIRMED | Every listed value is in the printed block. The box stdout matches 2026-11-06's except the progress-bar lines. |
| 38 | E:56 the box repo is at eb3e08c (G-F0m-OLMo (p)'s sync) | CONFIRMED | Pre-flight line 7; RESULTS.md:1935. |
| 39 | E:56–57 tracked files unmodified; untracked only the 15, the 15 committed at a225a89 | CONFIRMED | Pre-flight lines 8–24 against `git show --name-only a225a89`: the same 15 names. |
| 40 | E:57–58 both respawn scripts, olmo_hf.py, resume.py and the manifest are identical at eb3e08c and "this commit" | CONFIRMED at HEAD 3f017d8 | Equal blob ids and sha256 at eb3e08c, at HEAD and in the working tree. The commit itself does not exist yet. |
| 41 | E:58–59 the bundle comes next and sets the 15 aside by digest first | NOT CHECKABLE | A future act. It is consistent with fd74 §2 item 3 and with RESULTS.md:1935–1937. |
| 42 | E:60–61 both gates PASS, so forwards may run; the consistency clause | CONFIRMED | CLAUDE.md §Environment (see observation 8). |
| 43 | E:61–63 the identifier equals each lock's line, so this box is the campaigns' | CONFIRMED | |
| 44 | E:63–65 fd74 §2 item 3, verbatim | CONFIRMED | fd74 line 31, byte-equal. |
| 45 | E:67–69 the values-check link; "Not pushed. Committed by path." | NOT CHECKABLE | Future. |
| 46 | N:1–2 the heading's citations (each lock's §5; gl:§B.3; fd74 §2 item 2; pq:§4.3 item 4) and its PI date | CONFIRMED | |
| 47 | N:2–4 the replacement box is m43y3deb1gq3rp, made on the PI's go, relayed | CONFIRMED | |
| 48 | N:4–5 the entry gives 641ee466f4553b6a, equal to each lock's one BACKEND OF RECORD line | CONFIRMED | |
| 49 | N:5–8 the raw paths and sha256 short forms | CONFIRMED | |
| 50 | N:9–11 the lock paths and full sha256s | CONFIRMED | shasum at HEAD; they equal 038bf3e's entry and fd74 §0's short forms. |
| 51 | N:8 "no lock is edited" | CONFIRMED at HEAD | The locks last changed at 038bf3e, and the planned commit paths exclude them. |
| 52 | N:13–14 (a)'s line will cite this commit and the determinism raw's path; the note is committed with the entry, the two raws and the values-check raw | NOT CHECKABLE | Future. Consistent with fd74 §1 (a) and the v1.0 entry's (a). |
| 53 | The note carries what gl:§B.3 asks: pod id, identifier, both respawn raws, each lock's path and sha256; a RESULTS.md bullet under the v1.0 entry, after (ii) PASS, in eb3e08c's nested "Dated note (PI date …)" form, with no lock edit | CONFIRMED | It also covers each lock's §5 (A3) wording and 038bf3e's Next ("It names the pod id, the identifier, the respawn raws (i) and (ii), and each lock's path and sha256"). |
| 54 | Placement: the v1.0 entry's last bullet is "  - Not pushed. Committed by path." | CONFIRMED | RESULTS.md:465; the next entry starts at :467. |
| 55 | I structure: 7 `# ` header lines, then the box file byte for byte | CONFIRMED | Neither has carriage returns. |
| 56 | I:1 citations, quotes, PI-local date | CONFIRMED | |
| 57 | I:2 the BOX line | CONFIRMED | |
| 58 | I:3 the CODE line: full eb3e08c id; tracked/untracked; manifest at that commit (d39e5066…), five entries, unchanged since 0415438; identical at the laptop's HEAD; 51 = 29 + 22; box_respawn_check.py 8c410e33…, "identical at both" | CONFIRMED | The manifest's commits are 75939ed, 9cd324d and 0415438 only. Blob ids are 66174d40… and db80f1f4… at both eb3e08c and HEAD; `git show` piped to shasum gives the same digests. |
| 59 | I:4–5 the command, cwd, env.sh sourced, the nohup wrapper | NOT CHECKABLE | Box-side. Consistent with the copy-back paths and the .exit file. |
| 60 | I:6 exit=0, no stamps | CONFIRMED | |
| 61 | I:7 the box file's sha256 39eca68c…, byte-identical after transfer | CONFIRMED | copyback_respawn_out line 1. |
| 62 | I ok-lines: 51, each 16-hex prefix equals the manifest's sha256; every manifest file covered | CONFIRMED | The first 29 lines are identical to 2026-11-06's. |
| 63 | D structure: 9 `# ` lines, then the box file byte for byte (16 carriage returns, as in the box file), then 3 `#` lines, then exactly laptop_check_out.txt | CONFIRMED | |
| 64 | D:1 citations, quotes, PI-local date | CONFIRMED | |
| 65 | D:2 the BOX line | CONFIRMED | |
| 66 | D:3 box_determinism.py 934e01d4…, identical at the laptop's HEAD, as are olmo_hf.py and resume.py | CONFIRMED | |
| 67 | D:4 the ENV line: env.sh's contents and the C4 export of m43y3deb1gq3rp | CONFIRMED | From the committed env.sh record (2026-11-06 raw line 4 plus C4) and pre-flight lines 1–2, which ran in a separate shell. |
| 68 | D:5–6 the command and wrapper | NOT CHECKABLE | Consistent with the artifact's stage, repeats and exit. |
| 69 | D:6 the set-aside copy, sha256 61f160ea… | CONFIRMED | copyback line 6. |
| 70 | D:7 exit=0, no stamps | CONFIRMED | |
| 71 | D:8 the box artifact = the committed file = the set-aside copy; the precedent | CONFIRMED | copyback line 7. |
| 72 | D:9 the box stdout's sha256 68e33673…, byte-identical after transfer | CONFIRMED | copyback line 3. |
| 73 | D:65 the INVOCATION form | CONFIRMED | My run in that form reproduces laptop_check_out.txt byte for byte. |
| 74 | D:66 what the check does, including its exit rule | CONFIRMED | Matches check_determinism.py. |
| 75 | D:66 on 2026-11-06's record it prints that raw's thirteen check lines identically | CONFIRMED | Exit 0; lines 1–13 equal 2026-11-06 raw lines 70–82. The output is the same on the exact box-file bytes of record (6b31aada…). |
| 76 | D:66 it refused (exit 1) two mutants, one with another GPU name and one with a kernel-path KL above zero, each byte-different from the committed file | CONFIRMED | Exit 1 for each, with either stdout. Outputs equal mut_gpu.out and mut_c.out. Their sha256s are 64f803d4… and 8e3b9b93…, not 61f160ea…. |
| 77 | D:66 "Its last line is new" | CONFIRMED | |
| 78 | The new run's material: exit 0 and output = laptop_check_out.txt | CONFIRMED | The same holds with the set-aside copy as the new artifact. |
| 79–83 | M: the subject line, the pod bullet, the (i) bullet, the (ii) bullet, the identifier/note bullet | CONFIRMED (5 rows) | |
| 84 | M "Blind values-check, two passes" | NOT CHECKABLE | |
| 85 | M "Next (the seat's s2 item 3)" | CONFIRMED | A summary of fd74 §2 item 3. |
| 86 | M "RESULTS.md (two hunks …)" | CONFIRMED by simulation at 3f017d8 | Hunks @@ -20,7 +20,77 @@ and @@ -463,6 +533,20 @@. |
| 87 | M "No laptop model process ran. Not pushed." and the rest of "Committed by path" | NOT CHECKABLE | Conduct and future. The laptop check loads no model: valence_core imports numpy only. |
| 88 | M the Co-Authored-By trailer | CONFIRMED | |
| 89 | Every short form in the five texts equals its full value | CONFIRMED | fd74d3f6…e3ff ×5, a32d4d17…1112, 308d6020…3b8c ×3, faca18c6…7f96 ×3, 61f160ea…5434, and the msg's "..." forms. |
| 90 | No clock time | CONFIRMED | See observation 11 for time-like figures. |
| 91 | No $ figure or price | CONFIRMED | |
| 92 | No IP address or public endpoint | CONFIRMED | "port 22/tcp" appears; see observation 10. |
| 93 | No /Users/ or /private/ path | CONFIRMED | |
| 94 | No email except the trailer | CONFIRMED | |
| 95 | pq:§4.3 item 4's asks: the spec items, (i), (ii), the entry, the dated note | CONFIRMED | See observations 1 and 3. |
| 96 | m:251: the new box has its own BACKEND — characterization entry | CONFIRMED | |
| 97 | The p stage's PIN (stage.py:84–89): a new BACKEND entry plus a dated note at the lock in force, no re-issue | CONFIRMED | |
| 98 | Each lock's §5 | CONFIRMED | |
| 99 | CLAUDE.md respawn protocol: (i) and (ii), a dated entry, both PASS before anything runs | CONFIRMED | |

**Counts (99 claims):** 86 CONFIRMED, 2 IMPRECISE (rows 14 and 24), 0 FAIL, 11 NOT CHECKABLE (rows 10, 17, 23, 30, 41, 45, 52, 59, 68, 84, 87).

**Nothing asked is missing.** The entry plus the note give pq:§4.3 item 4, m:251, the p stage's PIN, each lock's §5, gl:§B.3 and 038bf3e's Next everything they ask for.

**Observations**
1. **Hook order departs from pq:.** pq:§4.3 item 4 lists "the `~/.bashrc` hook restored" in the spec and then says "then respawn (i)…(ii)". The hook was restored after the respawn. The entry discloses this with a reason but does not call it a departure. The commit message ("The ~/.bashrc hook restored (pq: s4.3 item 4)") says nothing about the order.
2. **"Every command" is too broad (row 24).** "Every measuring command" would be accurate.
3. **pq:'s "29" was already out of date when the seat wrote it.** 0415438 (2026-11-06) is earlier than pq: (2026-11-12), and pq:§4.1 itself says "the five checkpoints". The entry explains the 51 but does not flag the 29 as a slip in the seat's text, the way ledger (69) treated the typed sha prefix.
4. **Watch cadence and GPU name (row 14).** The interval is about 21 minutes, apart from the 31-second gap between reads 1 and 2. The GPU name is not in the log lines.
5. **Price timing can be read two ways.** "Read and stated before the create, and the coordinating session relayed it to the PI" could suggest the PI had the price before the create. Relay 2 relayed it after.
6. **"The old pod `uimuzt7d890y5b`"** is the 2026-08-23 A-phase pod (RESULTS.md 2026-08-23 entry). A reader could take "the old pod" to mean the box just replaced, qny1x4v8padeke. The id settles it, and the wording comes from 190ba90.
7. **"Field for field:"** is followed by the memory, driver and CUDA values, which are not create-body fields; they come from nvidia-smi and the read-back. They could be read as part of the body.
8. **"A box change aborts and restarts it"** follows CLAUDE.md. But each lock's §5 says this build has no restart route and the restart is the seat's to route, and gl:§B.3 says the restart clause applies only once a campaign has started. "Restarts" could be read as automatic.
9. **"The seat's answers of 2026-11-14"** in E's header and in E's "Next" is ambiguous. Two seat raws carry that date: gl: (6b963adf…) and fd74. Only fd74 has a §2, and E's "The seat's words" bullet and the note both give fd74's digest.
10. **E:20 "port 22/tcp only"** is a port number: the container port declared in the create body, not the public ssh endpoint. 190ba90's entry has the same words. Your call against the "no port of a pod" rule.
11. **Time-like figures.** D lines 10 and 55, the box stdout carried verbatim, hold tqdm progress-bar timers such as "[00:00<00:00, …]" and "[00:01<00:00, …]" (elapsed time and time remaining). The 2026-11-06 raw has the same. The other durations are "about every 20 minutes" and "2 h each". There is no clock time anywhere.
12. **Venv evidence covers only what provenance records.** "Library versions untouched" rests on the six libraries and Python in the provenance block; nothing else in the venv is recorded.
13. **D:4 "exported m43y3deb1gq3rp"** is shown by the pre-flight's separate shell running the same env.sh. The run's own shell is not separately evidenced.
14. **Order claims cannot be tested.** "Run only after (i)", "before it … copied aside" and "after the respawn" have no stamps by rule. The set-aside copy is byte-identical to the new artifact, so it cannot show the order either.
15. **SCR/test/stdout_1106.txt has one extra trailing newline.** It is raw lines 10–64 (sha256 08d904b9…) rather than the box file of record (lines 10–63, sha256 6b31aada…). This makes no difference: I re-ran on the exact bytes and got identical output.
16. **For (a)'s future precheck line.** In the new D raw the check block is lines 64–80, the description is line 66, and the identifier lines are 76–78 and 80. fd74 §1 cited 2026-11-06's lines 65 and 69.
17. **The mutation test.** Byte identity is itself an exit condition, so every mutant fails on that alone. D:66 discloses this. The outputs show the targeted checks failed too: the GPU mutant gives printed ≠ JSON provenance and identifier 1b50fa846475ac88, and the C mutant gives NOT EXACT.
18. **"PASS (cached path licensed)" in D:52** is verbatim box output. Under ledger 2's annotation, a first-token gate does not license generation, and the locks fix the path uncached (m:267). E's table rightly leaves "licensed" out.
19. **E:48 lists two precedents only.** A 2026-08-24 re-pass also exists (results/raw/2026-08-24_respawn_determinism.txt). The text does not claim the list is complete.
20. **"This commit" claims were checked at 3f017d8**, by blob ids and by simulation. Another session commits in this tree, so re-check them at commit time.
