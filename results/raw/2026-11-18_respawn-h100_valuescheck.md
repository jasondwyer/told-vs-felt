# BACKEND — characterization (2026-11-18), n's H100 box, and the pod session's close line on `e48c7d0`'s entry: blind values-check, two passes

*Code's raw (the pod session), PI date 2026-11-18. Two blind values-checks of the pod session's texts for this commit. Each checker was a fresh subagent given the texts, the sources, the coordinating session's relays and the pod read (the section below), and the list of record v2 items 1–5, with no interpreter and no marker word in any argv. The texts: T1, the `BACKEND — characterization` entry; T2, the close line on `e48c7d0`'s entry; T3 and T4, the integrity and determinism raws' headers; T5, the commit message; and, in pass 2 only, T6, the probe-preflight raw, added after pass 1. Pass 2 was blind to pass 1. The texts carried placeholders for the raws' sha256 and this check's totals, filled after both passes.*

*Totals. Pass 1: 120 claims; 106 CONFIRMED, 5 IMPRECISE, 0 FAIL, 9 NOT CHECKABLE; 22 observations. Pass 2, on the revised texts: 98 claims; 88 CONFIRMED, 2 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE; 17 observations.*

*How pass 1 was applied (every IMPRECISE item and every observation; two observations declined or needing no change, with the reason):*
- *Rows 10 and 65 (IMPRECISE), observation 2:* the seat raw's sha256 is now written `f46815fb…6d5a` in T1 and T2.
- *Rows 59 and 116 (IMPRECISE), observation 1:* "the seat's §2 items 4–7 are n-build's" is gone. T1 and T5 name items 4–7 one by one and give only item 5 to n-build, in the seat's words, "n-build for the driver" (its §2 heading). T1 quotes item 6's "nothing changes".
- *Row 101 (IMPRECISE), observation 3:* T4's invocation now names `<scratch>/hopper/check_newclass.py`.
- *Observation 4 (the shared volume):* T1 gains a bullet on what `o73qvy742n` now holds and what a respawn (ii) on the A100 would do; T5 gains a sentence.
- *Observation 5:* T3 and T4 now say "identical at 26cf7d2, the laptop's HEAD at the run, and at this commit". The staging script asserts the respawn inputs unchanged from 26cf7d2 to the commit's parent and in the working tree. T4 names resume.py as what Code's laptop check uses for the identifier.
- *Observation 6:* T1 points to the coordinating session's reading of the item's "move now", put to the seat in its close line on `e48c7d0`'s entry.
- *Observation 7:* T2 gains "The retries' two ends": with the Hopper pod created, the paste block's item 8 end is met, and the two ends that the coordinating session's line parts now coincide. No ruling is drawn.
- *Observation 8:* T1 gives the box raw's §5 item 1 with the paste block's item 8; T2 gives the paste block's item 9 with the box raw's §5 item 2.
- *Observation 9:* T3's BOX line gains 81559 MiB.
- *Observation 10:* T4's ENV list restores "the venv".
- *Observation 11:* T1's provenance list gains the adapter, path, backend and device.
- *Observation 12:* `pq:` is linked with its sha256 (`a32d4d17…1112`). C4's line is glossed from its RESULTS.md entry (the seat's answers of 2026-11-06: the pod id as PID 1 reports it, never typed). R6 is glossed from `e48c7d0`'s block.
- *Observation 13:* T1 now says the hook was restored "in the order `pq:`§4.3 item 4 gives for p's replacement box …, applied to n's box on a default the coordinating session accepted". It quotes the seat's ruling on the 2026-11-15 order: "The hook's order is inert, no strike".
- *Observation 14:* T1 gains a "For the seat" bullet: the identifier is a function of the provenance alone, and the dry test's H100 case printed it before the run. The real check's output equals that case's output except its first line (checked by tool: from line 2 on, the diff is empty). The run's evidence is A, B and C.
- *Observation 15:* no change; T4 already says "a SUMMARY/C mismatch (exit 1)", naming both.
- *Observation 16:* T4's check section gains "# EXIT 0".
- *Observation 17:* declined. "Read-only" describes what the preflight's commands do to content; a `git status` that refreshes the index's stat cache changes no content.
- *Observation 18:* applied by a new raw, `2026-11-18_respawn-h100_probe-preflight.txt` (T6, checked in pass 2). It holds:
  - the probe's, the preflight's and the hook's stdout verbatim, with the image's login banner elided and marked;
  - the copy-back's printed comparison, extracted by tool from the session's transcript; its six sha256 equal the laptop copies';
  - the 2026-11-15 preflight's "models:" line.

  T1 and T5 cite it. It makes row 96's "byte-identical after transfer" checkable.
- *Observation 19:* T2 now says "§2 from item 1's probe through item 3".
- *Observation 20:* T5 now says "the check and its nine-run dry test".
- *Observation 21:* T4's "What it does" now names the fixed "wrote" line and the SUMMARY line separately.
- *Observation 22:* no change asked.
- *Row 92 (NOT CHECKABLE):* T4 now says "byte-identical to the 2026-11-15 respawn's artifact" in place of "written by the 2026-11-15 respawn".
- *Pass 1's typo:* rows 41 and 83 of its report write the integrity file's sha256 tail as "…4b35". The full value, T3:7, ends "…4d35". The report is left verbatim below.
- *Line width:* one line of T1 over 120 characters, item 3's quote, was rewrapped.

*How pass 2 was applied (every IMPRECISE item and every observation):*
- *Row 85 (IMPRECISE), observation 2:* T5 now says "(item 5; s2's heading: "n-build for the driver")".
- *Row 87 (IMPRECISE), observation 1:* T6's first line now names the CUDA probe and the preflight as "both read-only", the hook's restore as "the one write outside the respawn folder", and the copy-back as one that "first copies the new artifact into the respawn folder on the box and then compares hashes".
- *Observation 3:* T1's probe bullet now lists all the probe-preflight raw holds, the copy-back's comparison and the 2026-11-15 "models:" line included.
- *Observation 4:* T1 and T5 now say the respawn folder also holds the copy-back's copy of the H100's artifact.
- *Observation 5:* T1 now says that Code's laptop check, not the run, would compare an A100 run's artifact with the committed file.
- *Observation 6:* T1's excerpts are marked "from item 1:" and "from item 3:", and T4's "from §2 item 3:". Item 2's quote is the whole item.
- *Observation 7:* T1 now says "30 GB (the pod's `disk` field)".
- *Observation 8:* T2 now says both ends "are now met, and the retries stay ended". It draws nothing about the question put to the PI.
- *Observation 9:* T1 and T2 cite §0, "One box for n: the A100's retry ends when a Hopper pod is created", with §3.3 for a healthy start.
- *Observation 10:* T1 and T5 add §2 item 8, the budget.
- *Observation 11:* T4's code line names all five files that box_determinism.py loads.
- *Observation 12:* T3 and T4 now describe the launch scripts' refusals and the backgrounding after "the only addition".
- *Observation 13:* T6's "local dir holds" line has its trailing space back. The transcript's line has it (checked by tool), so section 4 is byte-exact to the script's printed lines.
- *Observation 14:* T5 defines `pq:` by its raw's path.
- *Observation 15:* T1 cites the seat's answers of 2026-11-15 (evening) by path, sha256 (`1f3ce1f9…f84b`) and commit (`a215c28`).
- *Observation 16:*
  - T1's "the laptop's HEAD" now reads "`26cf7d2`, the laptop's HEAD at the run".
  - T4's check section says the laptop's HEAD at the check was `b4522ae`, where resume.py and the committed A100 artifact are the same blobs as at `26cf7d2` (checked by tool).
  - The staging script takes the HEAD of the commit window.
- *Observation 17:* the staging script's comments now say three respawn raws and six paths. The commit names the artifact by a quoted glob, so no marker word enters git's argv.
- *Pass 2's own disclosure:* one grep whose argv held the OLMo adapter's file name, a marker word, in a non-Python process. It was disclosed to the coordinating session for Q-F3's run list.

*Checked by tool after the edits of both passes:*
- every quotation byte-exact against its source, reading a line break plus its indentation as one space:
  - from the seat's box raw: the excerpt of item 1, item 2, the excerpt of item 3, "[move now — yours]", "nothing changes", "n-build for the driver", §0's "One box for n: …", item 8's "G-TIME-n projects …", and the paste block's item 8 words "the A100's retry ending when the Hopper pod is created";
  - from the 2026-11-15 evening raw: "The hook's order is inert, no strike";
- six hash abbreviations against their full values: `f46815fb…6d5a`, `a32d4d17…1112`, `61f160ea…5434`, `1dd9199f…d3c1`, `ee6e602f…16cb` and `1f3ce1f9…f84b`;
- no line of T1 or T2 over 120 characters, except one that holds only a link (the 2026-11-15 evening raw's, as in five lines of RESULTS.md);
- the bodies of T3 and T4 byte-equal to the box files and the check's output;
- T6's bodies built from the scratch outputs, with the hook's banner elided;
- the dry-test equality: from line 2 on, the real check's output equals the H100 case's;
- the respawn inputs unchanged from `26cf7d2` to `b4522ae` and to HEAD (git diff with quoted globs; a path known to have changed answers non-empty);
- the staging script's dry run against the HEAD of the window.

## The relayed texts and the pod read, as both checkers were given them (less the file's title line)

Two withholdings, marked where they fall: the pod's SSH address and port (never in any text), and one hourly price
figure (no money figure in committed text).

## The get-pod read of pod emw1e4embiwe9b (the pod session's, at creation; read-only)

- name `jspace-olmo-n`; status `RUNNING`; cloud `SECURE`; dataCenterId `US-CA-2`
- gpu: count 1, id `NVIDIA H100 80GB HBM3`
- image `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`; disk 30; ports `["22/tcp"]`
- mounts.network: path `/workspace`, volumeId `o73qvy742n`
- cudaVersion `13.2`
- [the ssh host and port, the runtime port mappings and the hourly cost are withheld]

## The coordinating session's relays (verbatim, less the withheld figure)

- **RELAY-1** (the routing, before the pod existed): "your part is its §2 items 1–3, and 9 if the H200 is taken." and
  "A 20-minute watch in the coordinating session creates one pod at the first US-CA-2 listing: the H100 first, the
  H200 only if the H100 is not listed at that read. Name jspace-olmo-n, the same image, volume o73qvy742n at
  /workspace, port 22/tcp."
- **RELAY-2** (the pod exists): "Coordinator to the pod session: n's box exists. Pod emw1e4embiwe9b, "jspace-olmo-n": 1
  × NVIDIA H100 80GB HBM3 (H100 SXM), Secure, US-CA-2, volume o73qvy742n at /workspace, image
  runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404, port 22/tcp, [an hourly price, withheld here]. Created on the PI's
  "Route as given" (the box raw's §5 item 1, "[move now — yours]") at the first US-CA-2 listing; status RUNNING. The
  H100 was taken, so §2 item 9 does not apply." and "Nothing on the A100 (m43y3deb1gq3rp stays stopped) or
  uimuzt7d890y5b."
- **RELAY-3** (the defaults and the first window): "the battery window is yours now, for the new-class check's dry
  test (9 model-free runs at nice 19, the interpreter reached by cd + glob)." and "Your defaults, all accepted:" ...
  "(b) Restore the ~/.bashrc hook after the probe passes and before (i), as pq §4.3 item 4 orders." ... "(d)
  data/olmo/determinism_base_h100-sxm.json, as Code's declared naming. Flag it for the seat in the BACKEND entry.
  data/olmo/determinism_base.json stays the A100's." "(e) Yes: draft your close line on e48c7d0's entry. The raw is
  committed at 26cf7d2, and my close line there says "The pod session adds its close line here.""
- **RELAY-4** (the second window): "the battery window is yours now, for one run of check_newclass.py (ee6e602f…16cb)
  on the six copied-back files: model-free, nice 19, the interpreter reached by cd + glob." and "Leave the box idle and
  running; stopping it is the PI's call."

## Pass 1's report, verbatim

Totals: 120 claims; 106 CONFIRMED, 5 IMPRECISE, 0 FAIL, 9 NOT CHECKABLE.

**Source state.** HEAD is b4522ae. Its parent is 26cf7d2. Between them only RESULTS.md (the N.2 entry, now first in the Log at :24), .gitignore, data/n/ files and results/raw/2026-11-18_n2_valuescheck.md changed, so none of the cited sources moved.
- RESULTS.md and the seat raw were read with `git show 26cf7d2:`.
- The working tree equals 26cf7d2 for every cited source, scripts/ and valence_core/. It equals HEAD for RESULTS.md.
- The eight box-run files, valence_core/m/resume.py, the manifest (blob 66174d40) and the A100 artifact (blob 690bce9f) have the same blob ids at 977b78b, 26cf7d2 and b4522ae.
- The box files were read as copied back. Abbreviations used below:
  - box files: <scratch>/hopper/box_respawn/
  - probe: <scratch>/hopper/probe_hopper_out.txt
  - preflight: <scratch>/hopper/preflight_out.txt
  - 11-15 preflight: <scratch>/podwatch2/preflight_out.txt
  - hook_out: <scratch>/hopper/hook_out.txt
  - RELAY-n and "get-pod read": <scratch>/hopper/commit/vc_sources_relays.md
  - seat raw: results/raw/2026-11-18_box-gpu_design-to-code_answers.md
  - corpus raw: results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md
  - pq: results/raw/2026-11-12_p-qual_design-to-code_answers.md
- Quotes were checked byte-exact with `grep -F -f <(…)` over the source, with a line break plus its indent read as one space.
- I recomputed the backend identifiers with shasum, no interpreter. resume.py:239–245 defines the identifier as the sha256 of the compact sort-keyed JSON of the provenance minus BACKEND_DROP (:147: n_encodes_clipped, path, seed), cut to 16 characters. My construction gives 641ee466f4553b6a for the A100 block, the value of record, and 4ed3f2c70fe8afbf for the H100 block.
- Checker's conduct:
  - No Python was run, and no marker word appeared in any command line. Marker paths were reached by Read, blob ids, quoted globs, or cd plus a glob.
  - Nothing under data/*/ckpt or data/*/reports was read, listed or sized.
  - I ordered the scratch files by modification with `find -newer`, which prints names only; no time is quoted anywhere.

| # | text:line, the claim (short) | verdict | evidence (short) |
|---|---|---|---|
| 1 | T1:1 citations: CLAUDE.md respawn protocol, m:251, m:302, n:161 | CONFIRMED | m:251 says each new box "gets its own `BACKEND — characterization` entry", and the identifier is "the adapter's provenance record (Code's definition)". m:302 opens "Respawn protocol (i)–(ii) on the box; `BACKEND — characterization` entry for that box". n:161 lists "`BACKEND — characterization` (per box)". Seat raw:26 asks for "m:302's and n :161's form". |
| 2 | T1:1–2 the seat's box answers, §2 items 1–3; the PI's "Route as given" (2026-11-18) | CONFIRMED | RESULTS@26cf7d2:76 has the PI's word verbatim; :89 and RELAY-1 give the pod session's part. |
| 3 | T1:2–3 n's box, pod emw1e4embiwe9b, an H100 SXM, characterized fresh as a new class | CONFIRMED | get-pod read; RELAY-2; seat raw:26. |
| 4 | T1:3, :29 the CUDA probe passed | CONFIRMED | probe:4–6 (True, 1, probe exit=0); nvidia-smi lines present. |
| 5 | T1:3 (i) INTEGRITY PASS, 51/51 | CONFIRMED | box integrity.txt PASS line; integrity.exit reads exit=0. |
| 6 | T1:3–4 (ii) PASS on the box's own determinism; A, B, C exact at 0.0 | CONFIRMED | box determinism.txt; the artifact's A, B, C are all 0.0/true. |
| 7 | T1:4–5, :70 identifier 4ed3f2c70fe8afbf | CONFIRMED | check_out:74–75; recomputed independently (see Source state). |
| 8 | T1:5, :87 n's backend of record (§2 item 3) | CONFIRMED | seat raw:26. |
| 9 | T1:5–7 the new artifact is this class's committed reference at data/olmo/determinism_base_h100-sxm.json, flagged for the seat | CONFIRMED | seat raw:26; RELAY-3 (d); .gitignore:43 `!/data/olmo/*.json` admits the path. |
| 10 | T1:10 sha256 `f46815fb…d5a` | IMPRECISE | The full value ends …9d66d5a. The house 8…4 form is f46815fb…6d5a, as 26cf7d2's own message writes it; "d5a" is three digits. |
| 11 | T1:10 committed at 26cf7d2 | CONFIRMED | `git log --diff-filter=A` names 26cf7d2. |
| 12 | T1:11–12 quote, §2 item 1 | CONFIRMED | Byte-exact; it is the second and third sentences of seat raw:24. |
| 13 | T1:13–15 quote, §2 item 2 | CONFIRMED | Byte-exact, bold markers included (seat raw:25). |
| 14 | T1:16–19 quote, §2 item 3 | CONFIRMED | Byte-exact; it is the third sentence of seat raw:26. |
| 15 | T1:21 named jspace-olmo-n | CONFIRMED | get-pod read; RELAY-2. |
| 16 | T1:21–22 the coordinating session's watch created it at the first US-CA-2 listing, on "Route as given" (raw §5 item 1, "[move now — yours]") | CONFIRMED | RELAY-2 has these words; seat raw:51 (§5 B item 1) ends "[move now — yours]". See obs. 6. |
| 17 | T1:23–25 spec: Secure, US-CA-2, 1 × H100 80GB HBM3, the image, volume at /workspace, container disk 30 GB, one port 22/tcp | CONFIRMED | get-pod read: SECURE; US-CA-2; count 1; the image; disk 30; ports ["22/tcp"]; o73qvy742n mounted at /workspace. The read does not print the unit "GB". |
| 18 | T1:26 81,559 MiB, driver 595.112.07, driver CUDA 13.2 | CONFIRMED | preflight:7 (memory.total 81559 MiB); probe:8–9. |
| 19 | T1:27 the H100 was taken, so §2 item 9 does not apply | CONFIRMED | seat raw:32; RELAY-2. |
| 20 | T1:27 no money figure recorded | CONFIRMED | No price or $ figure appears in T1–T5. |
| 21 | T1:28 the A100 pod stays stopped | CONFIRMED | RELAY-2; RESULTS@26cf7d2:97. |
| 22 | T1:28 the A100 pod was not touched, nor the August pod | NOT CHECKABLE | These are the sessions' own acts. RELAY-2 says "Nothing on the A100 … or uimuzt7d890y5b"; "August pod" matches RESULTS@26cf7d2:3544. |
| 23 | T1:30 is_available True, device count 1, no CUDA warning | CONFIRMED | probe:4–5. The probe merges stderr (2>&1) and no warning line appears; the ssh stderr capture is empty. |
| 24 | T1:31 nvidia-smi names the GPU, driver 595.112.07, CUDA 13.2 | CONFIRMED | probe:8–9, :12. |
| 25 | T1:32 torch 2.8.0+cu128, built for CUDA 12.8 | CONFIRMED | probe:3. |
| 26 | T1:33 fabric state Completed, status Success | CONFIRMED | probe:39–40. |
| 27 | T1:34 the output went verbatim to the coordinating session | NOT CHECKABLE | The session's act. |
| 28 | T1:36 no interpreter job, no GPU compute app | CONFIRMED | preflight:1–2. |
| 29 | T1:37–38 env.sh sha16 f5174faa745eca6e as on 2026-11-15; exports RUNPOD_POD_ID emw1e4embiwe9b by C4's line; CUBLAS :4096:8 | CONFIRMED | preflight:3–4; 11-15 preflight:2; RESULTS@26cf7d2:3552. |
| 30 | T1:39 Python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0 | CONFIRMED | preflight:6. |
| 31 | T1:40 box repo at 977b78b, tracked files unmodified, no untracked file | CONFIRMED | preflight:10–12. |
| 32 | T1:41–42 the eight files (i) and (ii) run equal the laptop's HEAD by blob id | CONFIRMED | The box's ids equal expected_blobs.txt and git ls-tree at 26cf7d2 and b4522ae, all eight. They are exactly the repo files (i) and (ii) load: box_determinism.py imports the adapter and readout.py, and the inits and base.py come in by import. |
| 33 | T1:43 names under /workspace/models unchanged since 2026-11-15's preflight | CONFIRMED | The two "models:" lines are identical (56 names). |
| 34 | T1:44 hook absent on the new container disk | CONFIRMED | preflight:5 ("bashrc hook lines: 0"); hook_out:1. |
| 35 | T1:44–45 hook restored before (i) | CONFIRMED | hook_out:2. Capture-file order: probe < preflight < hook < launch (i) < launch (ii). |
| 36 | T1:45 as pq:§4.3 item 4 orders for a replacement box | CONFIRMED | pq:47 lists "the `~/.bashrc` hook restored", then "then respawn (i)…". See obs. 13. |
| 37 | T1:45–46 on a default the coordinating session accepted | CONFIRMED | RELAY-3 (b). |
| 38 | T1:46 on 2026-11-15 the hook was restored after the runs, a disclosed departure | CONFIRMED | RESULTS@26cf7d2:3548–3549. |
| 39 | T1:46–47 an interactive shell then exported both values | CONFIRMED | hook_out:16. |
| 40 | T1:48–50 (i): re-hash under /workspace/models/; 51 across 5 (7/7/7/8/22), the manifest's count at HEAD; no problem line; exit 0 | CONFIRMED | 51 "ok" lines, split 7/7/7/8/22, with no MISMATCH, MISSING or EXTRA; box_respawn_check.py; manifest n_files; integrity.exit. |
| 41 | T1:50 the box file is byte-identical to 2026-11-15's | CONFIRMED | cmp with the 2026-11-15 raw from line 8; both sha256 39eca68c…4b35. |
| 42 | T1:52–53 (ii) ran only after (i) passed; --stage base --repeats 5; env.sh sourced; default window; exit 0 | CONFIRMED | respawn_ii.sh:14–16 refuses without exit=0 and the 51-file PASS line; :25–26 run the command. box_determinism.py:52–54 has no window option, and the adapter default is 8192 (olmo_hf.py:45). determinism.exit reads exit=0. |
| 43 | T1:56–60 the A/B/C table | CONFIRMED | determinism.txt A, C and B sections; the artifact. |
| 44 | T1:62–63 the A100 artifact on the volume (61f160ea…5434, equal to the committed file) was copied aside first; the committed file stays the A100's | CONFIRMED | launch_ii_out:1; before.json is cmp-equal to blob 690bce9f; respawn_ii.sh does cp and cmp before nohup; the working-tree file is unmodified. |
| 45 | T1:64 new artifact sha256 1dd9199f…d3c1, 2,819 bytes | CONFIRMED | shasum and wc -c of determinism_base.new.json; check_out:67. |
| 46 | T1:64–65 committed byte-identical at data/olmo/determinism_base_h100-sxm.json | CONFIRMED | <scratch>/hopper/commit/determinism_base_h100-sxm.json is cmp-equal to the copied-back file. |
| 47 | T1:65–66 the path is Code's naming, accepted by the coordinating session | CONFIRMED | RELAY-3 (d). |
| 48 | T1:67–69 2 of 108 leaf fields differ (gpu; capability[0] 8 → 9); every A, B and C value is the same | CONFIRMED | diff of the two artifacts shows lines 10 and 13 only. 108 leaves = 2 + 21 + 23 + 23 + 39; check_out:79–81. |
| 49 | T1:70–71 the identifier from both the printed and artifact blocks; the A100 block gives 641ee466f4553b6a | CONFIRMED | The printed block equals the artifact provenance (indent-adjusted diff); check_out:74–75, :78; recomputed. |
| 50 | T1:72 check_newclass.py sha256 ee6e602f…16cb | CONFIRMED | shasum. |
| 51 | T1:72–73 the check is appended to the determinism raw: exit 0, nothing for reading | CONFIRMED | T4:64–82. "CHECK PASSED" is printed only on the no-fail, no-read path, which exits 0 (check_newclass.py:140–147). |
| 52 | T1:74 dry test on the 2026-11-15 outputs, 9/9 as expected | CONFIRMED | The last lines of out_T0–T8 imply exits 3,0,1,1,1,3,1,3,1, as run_tests.sh expects. All nine outputs are newer than the script. |
| 53 | T1:75 the check and its dry test each ran in a battery window from the coordinating session | CONFIRMED | RELAY-3 and RELAY-4 grant the two windows; order: dry test < copy-back < check. |
| 54 | T1:76–82 provenance values; equal to the A100 block but for gpu and capability | CONFIRMED | determinism.txt:2–28; the artifact; the A100 artifact. |
| 55 | T1:82 declared window 8192, the adapter's default | CONFIRMED | olmo_hf.py:45, :86. |
| 56 | T1:84 the driver is not in the provenance | CONFIRMED | olmo_hf.py:311–336. |
| 57 | T1:85 both gates pass, so forwards may run | CONFIRMED | CLAUDE.md:127. |
| 58 | T1:85–86 consistency clause: a campaign completes on this one backend | CONFIRMED | CLAUDE.md:127–130; the same paraphrase as the 2026-11-15 entry. |
| 59 | T1:88 "The seat's §2 items 4–7 are n-build's" | IMPRECISE | The seat's §2 heading (raw:22) gives only "(the pod session; n-build for the driver)". The corpus raw:91 gives "the BACKEND extension's wiring (n-build)". §5 B routes §2 items 1–9 under "the coordinating and pod sessions". No source gives items 6–7 to n-build, and item 6 is not in the list. |
| 60 | T1:89–92 the items: extension plus hash beside; R6 retargeted; re-pin before step 4's run of record; LOCK-n v0.1 naming both backends | CONFIRMED | seat raw:27, :28, :30, :8. |
| 61 | T1:93 with a Hopper pod created, the A100 is not used for n (§3.3) | CONFIRMED | seat raw:40; §0 Q1 at :7. |
| 62 | T1:94 the box is idle and running; stopping it is the PI's call | NOT CHECKABLE | The box's state; the sentence matches RELAY-4's words. |
| 63 | T2:1 the pod session's close line, PI date 2026-11-18 | CONFIRMED | RESULTS@26cf7d2:98. |
| 64 | T2:2–4 this session read the box raw in full | NOT CHECKABLE | The session's act. |
| 65 | T2:4 sha256 `f46815fb…d5a` | IMPRECISE | As row 10. |
| 66 | T2:4 committed by path at 26cf7d2 by the coordinating session | CONFIRMED | 26cf7d2's subject; git log. |
| 67 | T2:5 the share is §2 items 1–3, and item 9 had the H200 been taken | CONFIRMED | RELAY-1; RESULTS@26cf7d2:89. See obs. 19. |
| 68 | T2:5–6 routed by the paste block's section B item 9, quoted in the line above | CONFIRMED | RESULTS@26cf7d2:76–78. |
| 69 | T2:7–12 done in §2's order on the watch's H100: probe; (i) 51/51; (ii) A, B, C exact, 4ed3f2c70fe8afbf | CONFIRMED | Rows 3–7, 35, 42. |
| 70 | T2:14 item 9 does not apply | CONFIRMED | As row 19. |
| 71 | T2:14–15 the record is the 2026-11-18 BACKEND entry (this commit) with its raws | CONFIRMED | Consistent with T1 and T5:11. |
| 72 | T2:16 the A100 stays stopped and was not started, so §3's test did not run | NOT CHECKABLE | "Stays stopped" and "no start is attempted" are at RESULTS@26cf7d2:95, :97 and in RELAY-2; any start since is outside the files. |
| 73 | T2:16–17 §3.3 has the A100 not used for n | CONFIRMED | seat raw:40. |
| 74 | T3:1 header: step (i); §Environment; n's box and pod; PROPOSAL-n's units; raw path at 26cf7d2; the PI's word relayed; PI-local date | CONFIRMED | Rows 2–3, 11. |
| 75 | T3:1 quote, §2 item 2 | CONFIRMED | Byte-exact (seat raw:25). |
| 76 | T3:2 BOX line | CONFIRMED | get-pod read; probe; RELAY-2. |
| 77 | T3:2 the probe passed before this step (True, device_count() 1) | CONFIRMED | probe:4–5; file order. |
| 78 | T3:3 box HEAD 977b78b8…b0f, unmodified, no untracked | CONFIRMED | preflight:10–12; `git rev-parse 977b78b`. |
| 79 | T3:3 manifest sha256 d39e5066…ac3e; five entries; 51 files 7/7/7/8/22; identical at 26cf7d2 | CONFIRMED | shasum of blob 66174d40, which is the same at 977b78b, 26cf7d2 and b4522ae and is the box's id; the manifest's n_files. |
| 80 | T3:3 box_respawn_check.py sha256 8c410e33…18c2, identical at both | CONFIRMED | shasum at 977b78b and 26cf7d2; box blob id. |
| 81 | T3:4–5 the command; the nohup wrapper is the only addition | CONFIRMED | respawn_i.sh:12–14; launch_i_out folder /workspace/respawn_2026-11-18. |
| 82 | T3:6 EXIT exit=0 | CONFIRMED | integrity.exit. |
| 83 | T3:7 box file sha256 39eca68c…4b35; byte-identical to the 2026-11-15 box file | CONFIRMED | shasum; row 41. |
| 84 | T3:8–61 the box file verbatim | CONFIRMED | cmp from line 8 with box integrity.txt. |
| 85 | T4:1 header: step (ii); CLAUDE.md; ledger rule 2; fresh characterization; raw at 26cf7d2; the PI's word; PI-local date; run only after (i) PASSED, exit=0 | CONFIRMED | Rows 2, 42; CLAUDE.md ledger 2. |
| 86 | T4:1 quote, §2 item 3 | CONFIRMED | Byte-exact (seat raw:26). |
| 87 | T4:2 BOX line incl. 81559 MiB | CONFIRMED | preflight:7; probe; get-pod read. |
| 88 | T4:3 box_determinism.py sha256 934e01d4…28aa identical at 26cf7d2, as are the adapter, readout.py and resume.py | CONFIRMED | shasum at 26cf7d2 and 977b78b; box blob ids for the first three. resume.py follows from the box repo being unmodified at 977b78b, whose blob d96c6ee0 is 26cf7d2's. |
| 89 | T4:4 ENV line | CONFIRMED | Same sha16 as 2026-11-15, whose raw lists these exports; preflight:3. See obs. 10. |
| 90 | T4:5–6 the command; the wrapper; default window, no option passed | CONFIRMED | respawn_ii.sh:24–26; box_determinism.py:52–54. |
| 91 | T4:6 copied aside (plain cp) to …/determinism_base.before.json; 61f160ea…5434; equal to the committed file | CONFIRMED | respawn_ii.sh:20–23; launch_ii_out:1; cmp with blob 690bce9f. |
| 92 | T4:6 "the A100's, written by the 2026-11-15 respawn" | NOT CHECKABLE | The bytes equal that run's artifact (its raw's ARTIFACT line); whether that run was the last writer is not in the files. |
| 93 | T4:7 EXIT exit=0 | CONFIRMED | determinism.exit. |
| 94 | T4:8 ARTIFACT sha256, 2,819 bytes, committed byte-identical; the A100's file left as it stands | CONFIRMED | Rows 44–46. |
| 95 | T4:9 box stdout sha256 faa17ba6…22f8; the check is appended after it | CONFIRMED | shasum; T4:64. |
| 96 | T3:7, T4:9 "byte-identical after transfer" | NOT CHECKABLE | Box side. copyback_hopper.sh compares sha256 at both ends, but its output is not among the files. |
| 97 | T3:6, T4:7 no clock time or stamp | CONFIRMED | None in the headers. The "00:00" strings at T4:10 and :55 are tqdm elapsed timers inside the verbatim stdout. |
| 98 | T4:10–63 the box stdout verbatim | CONFIRMED | cmp with box determinism.txt. |
| 99 | T4:64 the check ran after the transfer | CONFIRMED | check_out.txt is newer than all copied-back files. |
| 100 | T4:65 invocation form: cd <repo> && cd jl*/.venv/bin && nice -n 19 ./python -I -B …, two inputs, <repo> | CONFIRMED | run_check.sh:12, which also wraps it in a subshell with exec. |
| 101 | T4:65 script path `<scratch>/check_newclass.py` | IMPRECISE | run_check.sh:6, :12 pass <scratch>/hopper/check_newclass.py; no file exists at <scratch>/check_newclass.py. The 2026-11-15 raw had the same loose form for <scratch>/podwatch2/check_determinism.py. |
| 102 | T4:65 the two inputs' sha256 | CONFIRMED | shasum of the files run_check.sh passes. |
| 103 | T4:65 in a battery window from the coordinating session | CONFIRMED | RELAY-4. |
| 104 | T4:65 Q-F3 running on the laptop | NOT CHECKABLE | Not in the given files. |
| 105 | T4:65 interpreter by cd + glob, no marker in argv; the A100 path built inside the file | CONFIRMED | run_check.sh:12; check_newclass.py:31–32. |
| 106 | T4:66 "What it does": A, B, C criteria; shape; "wrote" and SUMMARY lines; printed = artifact; one identifier; exit 3 readings; descriptive diff; exit codes | CONFIRMED | check_newclass.py:61–147. The A100 artifact's det-OFF vs det-ON is 0.0. See obs. 21. |
| 107 | T4:66 dry test before this run, own window, 9/9, the nine cases and their exits | CONFIRMED | run_tests.sh:20–28 and the fixture diffs: h changes gpu and capability only; m2 changes A max_abs; m3 B max_repeat_abs; m4 a C row's exact; m5 B vs det-ON; m7 numpy 2.1.3 in JSON and stdout; m8 C max_kl and all_exact; T6 is h.json with the A100 stdout. Also out_T0–T8, file order and RELAY-3. |
| 108 | T4:67–82 the check's output verbatim | CONFIRMED | cmp with commit/check_out.txt. |
| 109 | T4:67–82 the check's figures | CONFIRMED | Rows 7, 45, 48. T0 on the A100 outputs gives 641ee466f4553b6a and 0 differences. |
| 110 | T5:1 subject line facts and sources | CONFIRMED | Rows 2–8. |
| 111 | T5:3 pod line | CONFIRMED | Rows 15–21; "untouched" as row 22. |
| 112 | T5:4 probe; hook before (i) as pq: s4.3 item 4 orders, on an accepted default | CONFIRMED | Rows 23, 35–37. |
| 113 | T5:5 the (i) line | CONFIRMED | Rows 40–41. |
| 114 | T5:6 the (ii) line: det-OFF = det-ON; check, dry test, windows; both identifiers; only gpu and capability differ | CONFIRMED | Rows 42–54. |
| 115 | T5:7 the artifact line | CONFIRMED | Rows 44–47. |
| 116 | T5:8 "the seat's s2 items 4-7 are n-build's" | IMPRECISE | As row 59. |
| 117 | T5:8 the box idle and running | NOT CHECKABLE | As row 62. |
| 118 | T5:11 two hunks: the top of the Log and the end of e48c7d0's entry | CONFIRMED | At HEAD the Log opens with b4522ae's entry (:24); e48c7d0's entry spans :102–184, with "adds its close line here" at :176. The two insertions are about 160 lines apart. |
| 119 | T5:11 the files committed by path | CONFIRMED | The raws are not ignored; the artifact is admitted by .gitignore:43. |
| 120 | T5:11 the model ran on the box only; two model-free checks; no marker word in any argv | CONFIRMED | check_newclass.py only loads JSON and hashes. Both run scripts' argv are marker-free. How the scripts were launched is the session's own act. |

**Observations**

1. **Rows 59 and 116, ownership of §2 items 4–7.** No source says "§2 items 4–7 are n-build's". A wording the sources support: "the rest of §2 is n's next work: n-build's driver (item 5) and the extension's wiring (item 4; the corpus raw's item 7); item 6 changes nothing; item 7 is LOCK-n v0.1's line". Or simply name the items without assigning them.
2. **Rows 10 and 65.** Use f46815fb…6d5a.
3. **Row 101.** Use <scratch>/hopper/check_newclass.py.
4. **The shared volume is missing from the record.** After (ii), /workspace/models/determinism_base.json on o73qvy742n holds the H100 artifact. The A100's bytes now exist only in the committed file and in /workspace/respawn_2026-11-18/determinism_base.before.json. The stopped A100 pod mounts the same volume, so "untouched" (T1:28, T5:3) covers the pod, not its volume. One line would help a reader of §3: an A100 respawn compares against the committed file, so nothing breaks, but it would overwrite the volume file again. No repo code reads the volume path; `git grep determinism_base` finds only readers of the committed file.
5. **T3:3 and T4:3 name "the laptop's HEAD 26cf7d2".** This commit will sit on b4522ae or later. Every named file is identical there. "at 26cf7d2 (unchanged at b4522ae)" avoids a reader taking 26cf7d2 for the parent. Also, T4:3's resume.py is not loaded by (ii) on the box; it matters for the laptop check's identifier.
6. **T1:21–22 omits a pending reading.** Creation "at the first US-CA-2 listing" carries "move now" forward under Code's reading of item 8, which was put to the seat (RESULTS@26cf7d2:87). A pointer to that reading would keep it visible.
7. **The two retry ends now coincide.** With a Hopper pod created, item 8's end ("the A100's retry ending when the Hopper pod is created") is now met. The two ends the coordinating session's line parted (RESULTS@26cf7d2:91–96) therefore coincide, and the question put to the PI is moot. T2 is the natural place to say so, or leave it to the coordinating session.
8. **Mixed numbering.** T1:22 uses the raw's §5 item 1, which is paste item 8. T2:6 uses paste item 9, which is the raw's §5 B item 2. Give both once.
9. **T3:2's BOX line lacks the memory figure.** T4:2 and both 2026-11-15 raws carry 81559 MiB.
10. **T4:4's ENV list drops "the venv".** The 2026-11-15 raw lists it for the same env.sh (same sha16). Restore it or mark the list as partial.
11. **T1:77's "The rest:" is not exhaustive.** adapter, path, backend and device are not listed, as on 2026-11-15.
12. **Shorthands undefined within T1/T5.** `pq:` (T1:45, T5:4), "C4's line" (T1:37) and "R6" (T1:90) are not defined here. Linking `pq:` (results/raw/2026-11-12_p-qual_design-to-code_answers.md, `a32d4d17…1112`) would let the entry stand alone.
13. **pq's scope.** pq:§4.3 item 4 is p's replacement box of the A100 spec of record. Here its order applies by the accepted default, which T1 says, but "orders for a replacement box" can read as calling n's box p's replacement. Optionally add that the 2026-11-15 order was ruled "inert, no strike" (RESULTS@26cf7d2, 2026-11-15 close line).
14. **For the seat: the identifier was predictable before the run.** The dry test's H100 fixture printed 4ed3f2c70fe8afbf before the run. The real check's output equals that fixture's output line for line except line 1: 1dd9199f…/2819 bytes versus the fixture's 8536b44a…/3425 bytes. So the check read the real file, and the identifier was fixed by GPU name and capability alone; the run's evidence is A, B and C.
15. **Dry-test case T8 also trips C's criterion.** It shows the SUMMARY check firing (its label is in the failure list), but not as the sole cause of exit 1.
16. **The check's exit code is not written in the raw.** It is only inferable from "CHECK PASSED"; run_check.sh echoes it to the terminal only. A "# EXIT 0" line would match the box sections.
17. **"read-only preflight" (T1:35).** The preflight runs `git status --porcelain` in the box repo, which may refresh .git/index's stat cache. It changes no content, so this is wording only.
18. **Probe and preflight stdout are not committed.** T1 cites their lines (fabric state, 81,559 MiB, blob ids) but they stay in scratch. Committing the probe output is optional; it holds no address or port, and the probe filters UUID and serial lines.
19. **T2:5 "§2 items 1–3".** Item 1's create was the coordinating session's. Its line says "from item 1's probe through item 3", and T2:7 makes the same point.
20. **T5:11 "two model-free checks".** The dry test is nine runs. "the check and its nine-run dry test" would match T4:66.
21. **T4:66, the "wrote" line.** The code tests for the fixed line "wrote /workspace/models/determinism_base.json", not for an artifact value. Only the SUMMARY line is checked against the artifact.
22. **Compliance.** No IP address, port other than 22/tcp, money figure or clock time appears in T1–T5. ":4096:8" is the cuBLAS setting. The T1 quotes are whole sentences; none of them includes item 3's last sentence, which lists what the entry must name (class, pod id, driver, identifier). T1 names all four.

## Pass 2's report, verbatim

Totals: 98 claims; 88 CONFIRMED, 2 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE.

**Source state.** I read the repository at HEAD `b4522ae` (parent `26cf7d2`). Where the texts cite RESULTS.md and the seat's raw, I also read them at `26cf7d2` with `git show`.
- `b4522ae` (N.2) changes RESULTS.md (N.2's entry at the top, and n-build's close line on `fa96ccf`'s entry), `.gitignore` and `data/n/`, and adds one values-check raw.
- During this check HEAD moved again, to `b523f6a` (n's ids of record (iv)). That commit adds one top entry to RESULTS.md, plus `data/n/ids/`, `scripts/n_sessions.py` (no `CHARACTERIZED_*` line changed), `valence_core/n/ids.py`, `valence_core/n/verify.py` and three raws.
- Nothing the texts cite moved at either commit:
  - `e48c7d0`'s entry, with the coordinating session's close line, is byte-identical to `26cf7d2`'s. It now sits at RESULTS.md:187–269 at `b523f6a`, and its last line is still "Committed by path. Not pushed."
  - `7ab4d2f`'s BACKEND entry with its close lines is byte-identical (:3696–3795). The C4 lines are unchanged.
  - The seat raws, CLAUDE.md and PROPOSAL-m v1.11 / PROPOSAL-n v0.2 are unchanged.
  - The blob ids of the eight respawn inputs, `resume.py`, the manifest and the A100 artifact are equal at `977b78b`, `26cf7d2`, `b4522ae` and `b523f6a`.
  - The working tree is clean for those paths.
- The texts as checked, re-hashed at the end and unchanged:
  - entry.md `aa5afb90…20a1`
  - close.md `4ddc8416…9aab`
  - integrity raw `697daca2…e018`
  - determinism raw `42d93801…6488`
  - msg.txt `57677823…bdbf`
  - probe-preflight raw `7092df49…f6e5`
- Before/after claims were checked by comparing the modification order of the pod session's laptop records with the commits' times from git log. Only the order was printed, never a time.

| # | text:line, the claim (short) | verdict | evidence (short) |
|---|---|---|---|
| 1 | T1:1, cites CLAUDE.md's respawn protocol, m:251, m:302, n:161 | CONFIRMED | CLAUDE.md §Environment (i)/(ii). m:251: "each new box … gets its own `BACKEND — characterization` entry". m:302: "entry for that box". n:161 lists "`BACKEND — characterization` (per box)". |
| 2 | T1:1–2, the seat's box answers §2 items 1–3; the PI's "Route as given" (2026-11-18) | CONFIRMED | Seat raw §2. `e48c7d0`'s coordinating close line quotes the PI's word on the paste block of 2026-11-18. RELAY-2. |
| 3 | T1:2–3, pod `emw1e4embiwe9b`, an H100 SXM, new class | CONFIRMED | Get-pod read (gpu id NVIDIA H100 80GB HBM3). RELAY-2 "(H100 SXM)". Preflight `pod=`. |
| 4 | T1:3–4, probe passed; (i) PASS 51/51; (ii) PASS on own determinism, A/B/C exact at 0.0 | CONFIRMED | Probe output. The integrity.txt PASS line. determinism.txt and the artifact (every row exact, 0.0). |
| 5 | T1:4–5, 82–83, 104: identifier `4ed3f2c70fe8afbf` on both blocks, n's backend of record; A100 block `641ee466f4553b6a` | CONFIRMED | check_out lines. Recomputed independently with shasum over the compact sort-keyed JSON of each block minus `BACKEND_DROP` (path, seed): H100 → `4ed3f2c70fe8afbf`, A100 → `641ee466f4553b6a`. Seat §2 item 3. |
| 6 | T1:5–7, 71–73: new artifact `1dd9199f…d3c1`, 2,819 bytes, committed byte-identical at `data/olmo/determinism_base_h100-sxm.json` as the class's reference; Code's naming, accepted, flagged | CONFIRMED | shasum, wc and cmp of `<scratch>/hopper/commit` copy vs the copy-back. stage_hopper.sh places it by `cp -n` + cmp. Seat item 3. RELAY-3 (d). |
| 7 | T1:9–10, box answers path, sha256 `f46815fb…6d5a`, committed at `26cf7d2` | CONFIRMED | shasum. git log (added at `26cf7d2`). Blob unchanged at HEAD. |
| 8 | T1:11–12, item 1 quote | CONFIRMED | Byte-exact substring of source line 24 (extracted and matched by tool). Excerpt: obs 6. |
| 9 | T1:13–15, item 2 quote (bold included) | CONFIRMED | Byte-exact, source line 25. |
| 10 | T1:16–19, item 3 quote | CONFIRMED | Byte-exact, source line 26. Excerpt: obs 6. |
| 11 | T1:21, named `jspace-olmo-n` | CONFIRMED | Get-pod read. RELAY-2. |
| 12 | T1:21–24: the watch created it at the first US-CA-2 listing on "Route as given" (§5 item 1 = paste item 8, "[move now — yours]"); "move now" carried on the coordinating session's reading, put to the seat in its close line | CONFIRMED | RELAY-1/2. Seat §5 B.1. `e48c7d0`'s close line ("Code's reading of item 8, for the seat"; item 8 quoted). |
| 13 | T1:25–27, spec: Secure, US-CA-2, 1 × H100 80GB HBM3, image, volume at /workspace, container disk 30 GB, port 22/tcp | CONFIRMED | Get-pod read (SECURE, dataCenterId, gpu, image, "disk 30", ports, mount). Obs 7. |
| 14 | T1:28, nvidia-smi 81,559 MiB, driver 595.112.07, driver CUDA 13.2 | CONFIRMED | Preflight GPU line (memory.total by the script's query order). Probe's `-q` lines. Get-pod cudaVersion 13.2. |
| 15 | T1:29, T5:3: H100 taken, so item 9 does not apply; no money figure | CONFIRMED | RELAY-2. Seat §2 item 9. No `$` figure in any text. |
| 16 | T1:30, T2:17, T5:3: the A100 stays stopped, not started or touched; the August pod `uimuzt7d890y5b` not touched | NOT CHECKABLE | Sessions' acts. Consistent with RELAY-2 and `e48c7d0`'s close ("no start is attempted"). "August pod" is `7ab4d2f`'s term. |
| 17 | T1:32–35, probe details (True, 1, no CUDA warning; name, driver, CUDA; torch 2.8.0+cu128 for CUDA 12.8; fabric Completed/Success) | CONFIRMED | probe_hopper_out.txt. The probe merges python's stderr into its stdout and shows none. ssh stderr file is 0 bytes. |
| 18 | T1:36, the output went verbatim to the coordinating session | NOT CHECKABLE | Session act. |
| 19 | T1:36–38, committed with the preflight's and hook's in the probe-preflight raw | CONFIRMED | Sections 1–3. Obs 3. |
| 20 | T1:40, no interpreter job, no GPU compute app | CONFIRMED | Preflight "interpreter jobs: 0" (pgrep python pattern), "GPU compute apps: 0". |
| 21 | T1:41–43, env.sh sha16 `f5174faa745eca6e` as on 2026-11-15; exports `:4096:8` and `RUNPOD_POD_ID` by C4's line (2026-11-06; PID 1, never typed) | CONFIRMED | Preflight sources env.sh, then prints. The 2026-11-15 preflight prints the same 16 hex. C4's line and comment in RESULTS.md (`26cf7d2`:9997), digest → `f5174faa…`. |
| 22 | T1:44, Python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0 | CONFIRMED | Preflight. |
| 23 | T1:45, box repo `977b78b`, tracked unmodified, no untracked | CONFIRMED | Preflight. Full id = `git rev-parse 977b78b`. |
| 24 | T1:46–47, the eight files (i)/(ii) run equal the laptop's HEAD by blob id | CONFIRMED | Preflight = expected_blobs.txt = ls-tree at `26cf7d2`, 8/8; same at `b4522ae` and `b523f6a`. Imports: box_determinism → the adapter and readout → `.base`; the `__init__`s → base; box_respawn_check reads only the manifest. |
| 25 | T1:48, `/workspace/models` names unchanged since 2026-11-15's preflight | CONFIRMED | The two "models:" lines are identical (diff). |
| 26 | T1:49, hook absent on the new container disk | CONFIRMED | Preflight "bashrc hook lines: 0". Hook "(absent before restore)". |
| 27 | T1:49–52, restored before (i), in pq:§4.3 item 4's order (`a32d4d17…1112`), on an accepted default | CONFIRMED | pq §4.3 item 4 lists the hook, then "then respawn (i) … (ii)". shasum. RELAY-3 (b). The hook output predates (i)'s launch output (file order). |
| 28 | T1:52–54, 2026-11-15 restored after the runs, disclosed; §0: "The hook's order is inert, no strike" | CONFIRMED | `7ab4d2f`'s entry. Evening raw §0, fourth bullet, byte-exact (";" follows in the source); §3.2. |
| 29 | T1:54, an interactive shell exported both values | CONFIRMED | hook_out line 16. |
| 30 | T1:55–57, (i): 51 across 5 (7/7/7/8/22) = manifest at HEAD; no problem line; exit 0 | CONFIRMED | integrity.txt ok-lines per checkpoint. The manifest's five entries and n_files. integrity.exit `exit=0`. The script prints problems only on FAIL. |
| 31 | T1:57, box file byte-identical to 2026-11-15's | CONFIRMED | cmp with the 2026-11-15 raw's body. Same sha256 `39eca68c…4d35`. |
| 32 | T1:59–61, (ii) only after (i); command; env.sh; default window; exit 0 | CONFIRMED | respawn_ii.sh guards (exit file + PASS line), sources env.sh, passes only `--stage base --repeats 5`. box_determinism.py has no window option. determinism.exit `exit=0`. |
| 33 | T1:63–67, A/B/C table | CONFIRMED | determinism.txt and the artifact. |
| 34 | T1:69–70, the A100 artifact on the volume `61f160ea…5434` = committed; copied aside; committed file stays the A100's | CONFIRMED | launch_ii_out "before: 61f160ea…". before.json sha. Committed blob hashes to `61f160ea…`. stage_hopper.sh asserts it unchanged. |
| 35 | T1:74–76, the volume file now holds the H100's; the A100's bytes in the committed file and before.json | CONFIRMED | The "wrote …" line. Copy-back box-side cmp + sha. Obs 4. |
| 36 | T1:76–77, the A100 pod mounts the volume; a respawn (ii) there would compare against the committed file and write the volume file again | CONFIRMED | `e48c7d0` close ("its volume mount unchanged"). box_determinism.py writes `/workspace/models/determinism_{stage}.json`. Comparison per seat §3.1. Obs 5. |
| 37 | T1:77–78, no repo code reads the volume path | CONFIRMED | git grep over tracked `*.py`/`*.sh` (ckpt/reports excluded) and all non-data, non-.md files: only box_determinism.py names it (to write). audit_note_N17.py and lockg_valuescheck.py read the committed file. |
| 38 | T1:79–81, 2 of 108 leaves differ (gpu; capability[0] 8→9); A/B/C the same | CONFIRMED | diff before/new: lines 10 and 13 only. Leaf count 2+21+23+23+39 = 108. |
| 39 | T1:84–85, check sha `ee6e602f…16cb`, appended, exit 0, nothing to read | CONFIRMED | shasum. T4:68–83 = check_out.txt. "CHECK PASSED" prints only with no fail and no read (exit 0). |
| 40 | T1:86, dry test on the 2026-11-15 outputs 9/9 | CONFIRMED | run_tests.sh's nine cases. Fixtures are the 2026-11-15 artifact and stdout (`68e33673…33ba`, the 2026-11-15 raw's figure) and single edits of them. Each out_T*.txt ends as its expected exit implies. The tally line is in the transcript. |
| 41 | T1:87, T4:65–66, T5:6, T5:11: check and dry test each ran in a battery window from the coordinating session | NOT CHECKABLE | RELAY-3 and RELAY-4 grant one window for exactly these runs. Running inside them is the session's act. |
| 42 | T1:88–91: identifier is a function of the provenance alone; the dry test's H100 case printed it before the run; real output equals it except line 1 | CONFIRMED | resume.py (sha16 minus n_encodes_clipped/path/seed). out_T1's last line. diff differs only in line 1 (fixture 3,425 bytes vs 2,819). out_T1 predates (ii)'s launch output. |
| 43 | T1:92–99, provenance fields | CONFIRMED | Printed block = artifact block. `DEFAULT_CHOICE_WINDOW = 8192`. Seed default 20260818. "cuda" = `torch.version.cuda`. |
| 44 | T1:101, driver not in the provenance | CONFIRMED | The adapter's `provenance()` keys. |
| 45 | T1:102–103, both gates pass → forwards may run; consistency clause | CONFIRMED | CLAUDE.md respawn protocol and consistency clause. |
| 46 | T1:105–112, T5:8, §2 items 4–7 (extension + hash beside; R6 described and retargeted; pins re-pinned before step 4's run of record; heading "n-build for the driver"; "nothing changes"; both backends) | CONFIRMED | Seat §2 items 4–7 and heading. The 2026-11-17 block :138 (R6). |
| 47 | T1:113, T2:18, Hopper pod created → the A100 not used for n (§3.3) | CONFIRMED | §3.3's last sentence (under a healthy start). §0 "One box for n". Obs 9. |
| 48 | T1:114, T5:8, the box is idle and running; stopping is the PI's call | NOT CHECKABLE | RELAY-4 asks exactly this. The state is not in the files. |
| 49 | T1:115–117, values-check raw path; not pushed; committed by path | CONFIRMED | stage_hopper.sh RAWS and `git add` by path. No push. |
| 50 | T2:1–4, box raw path, `f46815fb…6d5a`, committed by path at `26cf7d2` by the coordinating session | CONFIRMED | shasum. `26cf7d2`'s subject. |
| 51 | T2:1–3, read in full | NOT CHECKABLE | Session act. |
| 52 | T2:5–7, the share (item 1's probe → item 3; item 9 had the H200 been taken); routed by paste item 9 = box raw §5 item 2, quoted above | CONFIRMED | `e48c7d0` close ("The pod session then takes …"; item 9 quoted). RELAY-1. Seat §5 B.2. |
| 53 | T2:8–13, done in §2's order on the H100 the watch created: probe; (i) 51/51; (ii) fresh, exact, identifier | CONFIRMED | Rows 3–5, 12. File order: probe → preflight → hook → (i) → (ii). |
| 54 | T2:15–16, item 9 n/a; the record is this commit's entry with its raws | CONFIRMED | RELAY-2. stage_hopper.sh. |
| 55 | T2:17–18, §3's test did not run; §3.3 | CONFIRMED | §3.1's test needs a start (start itself: row 16). |
| 56 | T2:19–21, item 8's end quote, met; the two ends "now coincide" | CONFIRMED | Byte-exact in `e48c7d0`'s close (paste item 8) and seat §5 B.1. The coordinating line's "the two ends part". Obs 8. |
| 57 | T3:1, header line 1 (step (i); n's box; seat raw at `26cf7d2`; item 2 quote; PI's word, date, relayed) | CONFIRMED | Quote byte-exact (225 chars, extracted by tool). |
| 58 | T3:2, BOX line | CONFIRMED | Get-pod read, preflight, probe, relays. |
| 59 | T3:3: box HEAD `977b78b8…`, clean; manifest `d39e5066…ac3e`, five entries, 51 (7/7/7/8/22); `box_respawn_check.py` `8c410e33…18c2`; identical at the three | CONFIRMED | rev-parse. Blob sha256s. Blob ids equal at `977b78b`/`26cf7d2`/`b4522ae`/`b523f6a`. stage_hopper.sh asserts no change. |
| 60 | T3:4–5, command and nohup wrapper | CONFIRMED | respawn_i.sh with D=2026-11-18. launch_i_out. Obs 12. |
| 61 | T3:6, `exit=0`; no stamp | CONFIRMED | integrity.exit. No clock time in any text (only the box's tqdm timers, verbatim in T4). |
| 62 | T3:7, sha256 `39eca68c…4d35`; identical after transfer and to 2026-11-15's | CONFIRMED | shasum. Copy-back line. cmp. |
| 63 | T3:8–61 = box integrity.txt | CONFIRMED | cmp. |
| 64 | T4:1, header line 1 (item 3 quote; only after (i) passed) | CONFIRMED | Byte-exact (407 chars). respawn_ii.sh guard. |
| 65 | T4:2, BOX line | CONFIRMED | As row 58. |
| 66 | T4:3, `box_determinism.py` `934e01d4…28aa`; the adapter, readout (loaded) and resume.py (the check's) identical | CONFIRMED | Blob ids at all four commits. Imports. Obs 11. |
| 67 | T4:4, ENV line | CONFIRMED | respawn_ii.sh sources env.sh. Same sha16 as 2026-11-15, whose raw lists these contents. Export per preflight. |
| 68 | T4:5–6, command; wrapper; default window; plain cp to before.json, `61f160ea…` = committed = the 2026-11-15 artifact | CONFIRMED | respawn_ii.sh. launch_ii_out. 2026-11-15 raw's ARTIFACT line. |
| 69 | T4:7, `exit=0`; no stamp | CONFIRMED | determinism.exit. |
| 70 | T4:8, ARTIFACT full sha, 2,819 bytes, committed byte-identical; A100 file left as it stands | CONFIRMED | Row 6. stage_hopper.sh. |
| 71 | T4:9, stdout sha256 `faa17ba6…22f8`, identical after transfer | CONFIRMED | shasum. Copy-back line. |
| 72 | T4:10–63 = box determinism.txt | CONFIRMED | cmp. |
| 73 | T4:64–65, check header and INVOCATION; the A100 path built inside the file | CONFIRMED | run_check.sh (cd + glob, nice 19, `-I -B`, the two inputs by sha). check_newclass.py:32 `os.path.join`. |
| 74 | T4:65, "Q-F3 running on the laptop" | NOT CHECKABLE | Only the pod session's procedure says so. |
| 75 | T4:66, "What it does" (criteria, readings, descriptive, exit codes, sha) | CONFIRMED | check_newclass.py lines 61–147. |
| 76 | T4:66, dry test before this run, nine cases with the stated exits | CONFIRMED | Fixture diffs: h = gpu/capability; m2 A max_abs; m3 B max_repeat_abs; m4 one C row's exact; m5 B vs det-ON; m7 numpy 2.1.3 in json and stdout; m8 C max_kl/all_exact vs h.txt's SUMMARY; T6 = h.json vs the A100 stdout. File order: before the check. |
| 77 | T4:67, EXIT 0 as run_check.sh printed it | NOT CHECKABLE | The printed line is in the transcript. Consistent with row 39. |
| 78 | T4:68–83 = check_out.txt | CONFIRMED | cmp. |
| 79 | T5:1, subject | CONFIRMED | Rows 2–5, 50. |
| 80 | T5:3, the pod line (name, watch, listing, GPU, Secure, image, volume, driver) | CONFIRMED | Rows 11–14. |
| 81 | T5:4, probe; hook before (i) in pq: order on an accepted default; the raw's contents incl. the copy-back | CONFIRMED | Rows 17, 27; T6 sections 1–4. |
| 82 | T5:5, (i) line | CONFIRMED | Rows 30–31. |
| 83 | T5:6, (ii) line | CONFIRMED | Rows 33, 38–40. |
| 84 | T5:7, artifact line; the A100 file stays; the volume | CONFIRMED | Rows 6, 34–35. Obs 4. |
| 85 | T5:8, "(item 5; "n-build for the driver")" | IMPRECISE | The quoted words are §2's heading ("the pod session; n-build for the driver"), not item 5's. T1:110 attributes them correctly. |
| 86 | T5:11, committed by path (two hunks: top of the Log, end of `e48c7d0`'s entry; three respawn raws, the artifact, values-check raw); model on the box only; check and dry test model-free, no marker in any argv; not pushed | CONFIRMED | stage_hopper.sh (anchors; 2 hunks / 0 removals; six paths). check_newclass loads no model. run_check/run_tests argv hold no marker. Obs 17. |
| 87 | T6:1, "Read-only looks … (the hook is the one write)" | IMPRECISE | copyback_hopper.sh, one of this raw's looks, writes on the box: it copies `/workspace/models/determinism_base.json` to `/workspace/respawn_2026-11-18/determinism_base.new.json`, then runs cmp. bashrc_hook.sh's own comment scopes the hook as the only write "outside /workspace/respawn_<date>". |
| 88 | T6:1, probe/preflight/hook all before (i); copy-back after (ii) | CONFIRMED | File order. The preflight's workspace listing has no `respawn_2026-11-18`. |
| 89 | T6:2: sections 1–3 verbatim with one marked elision; `bash -s` over ssh, plain shell; ssh stderr empty; no address/port (count 0); no stamp | CONFIRMED | cmp. The `*_err.txt` files are 0 bytes. Scripts' usage lines. My own counts of the session's address, and of its port as a word: 0 in all seven files. |
| 90 | T6:3–62, section 1: probe_cuda.sh `621113f4…20c9`; body | CONFIRMED | shasum. cmp with probe_hopper_out.txt. |
| 91 | T6:63–85, section 2: preflight_hopper.sh `f8bb11fe…48fe`; blob ids = ls-tree at `26cf7d2`, 8/8; models line = 2026-11-15's; body | CONFIRMED | shasum, diff, cmp. |
| 92 | T6:86–91, section 3: bashrc_hook.sh `de8518f7…841c`; elision (lines 4–15, login banner, 12 lines, 2 blank) | CONFIRMED | Kept lines = hook_out 1–3 and 16. Lines 4–15 are the image banner; lines 14–15 blank. |
| 93 | T6:92, copyback_hopper.sh `4abc6867…804b`; compares box sha256sum with laptop shasum; exited 0 | CONFIRMED | Script. Exit 0 follows from six "identical" lines and six hashes. |
| 94 | T6:92, extracted by grep from the transcript | NOT CHECKABLE | Transcript not read. |
| 95 | T6:93–99, six sha256 and names; the local dir's names | CONFIRMED | shasum of `<scratch>/hopper/box_respawn/*` equals all six. ls. Obs 13. |
| 96 | T6:100–101, section 5: 2026-11-15 models line (pod `m43y3deb1gq3rp`), verbatim | CONFIRMED | = `<scratch>/podwatch2/preflight_out.txt` line 6 (its line 1 is `pod=m43y3deb1gq3rp`). |
| 97 | T3:3, T4:3, "26cf7d2, the laptop's HEAD at the run" | CONFIRMED | Probe, preflight, hook, both launch outputs and the dry test postdate `26cf7d2`'s commit and predate `b4522ae`'s. The copy-back and the check postdate `b4522ae`'s. Obs 16. |
| 98 | T1–T6, ids, hashes, figures agree across texts | CONFIRMED | Tool tally: pod ids, volume, identifiers, `977b78b`, `f5174faa…`, driver, 81559. No variant spelling. Every abbreviation matches its full value (computed by tool). |

**Observations**
1. **T6:1 (row 87).** Suggested wording: "Looks at n's box …: the CUDA probe and the preflight (read-only) and the ~/.bashrc hook's restore (the one write outside the respawn folder), all before respawn (i); and the copy-back after respawn (ii), which first copies the new artifact into the respawn folder on the box."
2. **T5:8 (row 85).** Suggested wording: "(item 5; §2's heading: "n-build for the driver")".
3. **T1:36–38.** The probe-preflight raw also holds section 4 (the copy-back comparison) and section 5 (the 2026-11-15 models line). T1 never mentions the copy-back, and every "byte-identical after transfer" in the raws rests on it. T5:4 does mention it.
4. **T1:74–76, T5:7.** The respawn folder on the volume also holds the H100's artifact, as `determinism_base.new.json` (the copy-back's cmp-checked copy). As written, "the A100's in the respawn folder" reads as if it were the only artifact there.
5. **T1:76–77.** box_determinism.py compares nothing; it measures and writes. The comparison with the committed file is the protocol's byte-identity test (seat §3.1), made by Code's laptop check on the copied-back artifact. Saying "Code's laptop check would compare that run's artifact with the committed file" would make clear who compares.
6. **Unmarked excerpts (T1:11–12, T1:16–19, T4:1).**
   - Item 1 opens with "**Create** on the PI's word, in US-CA-2 on volume `o73qvy742n`; the pod id recorded."
   - Item 3's omitted first sentences include "under the adapter's default window". Its last sentence sets the entry's form, "naming the class, the pod id, the driver and the identifier"; the entry does name all four.
   - "from item 1:" / "from item 3:" or an ellipsis would mark them as excerpts.
7. **T1:26.** "container disk 30 GB": the get-pod read as relayed says only "disk 30", with no field name or unit. The reading follows `7ab4d2f`'s entry, and the earlier create bodies use the same field.
8. **T2:21.** "now coincide": the two ends were met at different points (item 11's at the PI's word, item 8's at the pod's creation). "are now both met" or "now agree; the retries stay ended" would be exact. The close does not say whether this settles the question put to the PI.
9. **T1:113, T2:18.** §3.3 is the order "on a healthy start", and the A100 never started. The text that applies on its own terms is §0's "One box for n: the A100's retry ends when a Hopper pod is created" (and §4's "end when a Hopper pod is created"). Citing §0 beside §3.3 would be exact.
10. **T1, T5 "next".** §2 item 8 (the budget: G-TIME-n projects on the new box; the PI's cap at LOCK-n v1.0) is not mentioned anywhere.
11. **T4:3.** "which it loads" names the adapter and readout.py only. box_determinism.py also loads `valence_core/__init__.py`, `adapters/__init__.py` and `base.py`. T1:46–47 lists all eight, and all are unchanged.
12. **T3:5, T4:6, "that is the only addition".** The launch scripts also do the following. This is the 2026-11-15 form, and none of it touches the outputs.
    - They send the wrapper's own output to /dev/null and background it.
    - They refuse if an interpreter is running or the folder exists.
    - (ii)'s script also copies the artifact aside and checks it with cmp.
13. **T6:99.** copyback_hopper.sh prints "local dir holds: …" with a trailing space (`ls | tr '\n' ' '`); the extracted line has none. Section 4 is not claimed byte-exact, but a later byte comparison with the script's output would differ by that space.
14. **T5:4.** It uses "pq:" without defining it in the commit message. T1 defines it by link and sha256.
15. **T1:52–54.** The seat's answers of 2026-11-15 (evening) are cited without path or sha256. `7ab4d2f`'s close line gives them: `results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md`, sha256 `1f3ce1f9…f84b`, committed at `a215c28`.
16. **HEAD moved twice after the box run.** `b4522ae` landed before the copy-back and the real check; `b523f6a` landed during this check.
    - "26cf7d2, the laptop's HEAD at the run" is right for the probe, preflight, hook, both launches and the dry test.
    - The real check ran at `b4522ae`, where resume.py and the committed A100 artifact are the same blobs.
    - T1:46's "the laptop's HEAD" could read "26cf7d2", as T6:63 does.
    - stage_hopper.sh stops on any HEAD other than its argument, which is now `b523f6a`.
17. **stage_hopper.sh.**
    - Its header says "the two respawn raws" and its step-4 comment says "exactly the five", while the code stages four raws and checks six paths. The code matches T5.
    - Its closing hint, `git commit -F <msg> -- <the six paths>`, would put a marker word in git's argv if the artifact's path is written out. The quoted glob its `git add` uses keeps it out.

**Checker's disclosures**
- **One departure from the hard rules.** To read the OLMo adapter's imports, default window and provenance keys, I ran one grep on the adapter file in `valence_core/adapters/` through a shell glob. The expanded file name, which contains a marker word, was in that grep's argv for one call. Afterward I read the file with the Read tool.
- **No other command line or argv carried a marker word:**
  - The manifest and the A100 artifact were hashed with shasum and `git hash-object` after a `cd` by glob (digests only).
  - The manifest's content was read with the Read tool; the artifact's content through its byte-identical scratch copy.
  - Git pathspecs used quoted globs.
  - Quotes containing marker words reached grep through a pipe, never as arguments.
- **Other reads.**
  - I ran one `git status --porcelain` with pathspecs (RESULTS.md, results/raw, the cited code paths, CLAUDE.md); it printed nothing.
  - Nothing under `data/*/ckpt` or `data/*/reports` was read, listed or stat-ed.
  - To count the pod's address and port in the texts, I sourced the session's connection file into a subshell and printed counts only.
  - File-order checks printed "before/after" only.
- No interpreter, no network or ssh command, no write.
