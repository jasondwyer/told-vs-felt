# n — G-VEC's launch files v2: the blind launch review, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over G-VEC's launch files v2 as first drafted, at the gvec delta's
commit `616e940`, before the relay:
- the box script `gvec_v2.sh` `d0d154d7…6402` (323 lines), its manifest `00180e67…6a3e` (61 lines), its hashes file
  `c40ed07b…7368` (13 lines) and the launch note `eb63ab79…9430` (127 lines);
- the laptop tests as they then stood: the harness `682f0201…80ab` with its stand-in `0eecac8f…adc5` (286 of 286), and
  the snippet test `3b69e0fc…0bcf` (53 of 53 on 48 fixtures);
- the template, the first run's `gvec_v1.sh` `f349e17d…a1ad`, and its committed output,
  `results/raw/2026-11-19_n-gvec-v1_out.txt`.

**The reviewer's brief** (`f6898d67…a4ec`, 105 lines):
- named those files by sha256, to be verified and read in full, and the code they must match at `616e940`
  (`scripts/n_sessions.py`'s G-VEC section, `gvec.py`, `directions.py`, `guard.py`, `ids.py`, A3's code), the seat's
  answers of the second sitting (§1.2–§1.5), the gvec delta's entry and `.gitignore`'s block for `data/n/gvec/`;
- asked ten questions: the literals against the code; the record checks against what the stage writes, with no
  descriptive figure gated on its value (§1.3: "none a decision"); the exits; a false PASS; a false FAIL; the
  manifest; the writes; the order and the gates; the note; the harness's and the snippet test's reach;
- asked for findings, surviving mutants, observations and any command a rule bars, and quoted the list of record v2's
  items 1–5 and the rules on interpreters, writes, guard markers, `data/mf3`, and ckpt and reports files.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (202 lines, sha256
`98dc4465…1fb3`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 0 BUG; 8 findings (5 RISK, 3 NIT); 8 surviving mutants; 11 observations.

## 1. Dispositions

The bytes relayed and run: `gvec_v2.sh` `e5f76f5b…c49e` (352 lines), the manifest and the hashes file unchanged, and
the note `125b1541…23fe` (154 lines). Every finding and surviving mutant below was met before the relay; O3's result
came after the run, and O8 was met by the relay itself.

- **F1** (RISK), applied: the run's diagnostic patterns end at "5..n 3683", or at the suffix "; not finite, recorded as
  null: …" that names a null figure, and the line's end; the smoke's are pinned at the smoke's size at positions 0–4,
  with a count over 5..n, and end the same way. The harness's runtail, runtail4, runtail32, smoketail, smoketail32
  and smoketok cases print longer or wrong counts, and its two non-finite cases print the suffix.
- **F2** (RISK), applied in the `os.fsencode` form: both record checks take the convention's bytes back from their
  argument and decode them as UTF-8. No laptop case can reach a non-UTF-8 locale; the note says so.
- **F3** (RISK), applied beyond the reviewer's conjuncts: the run's check re-derives the record's rel (to within
  1e-12), within, status and site from its own R by `gvec.choose_site`'s arithmetic, the nearer if both and a tie to
  32. Fixtures for a contradicted site, a tie, a wrong rel or within, a missing rel or within, an integer R, and a STOP
  whose R is within 2%; harness cases recsite, recwithin, recrel and stopwithin.
- **F4** (RISK), applied: `git status` runs with `--ignored`; the cases copyignored, smokeignored and runignored, and
  the staging case now also fails at the changed set.
- **F5** (RISK), applied: a work folder under `/workspace/models` is refused (the workmodels case).
- **F6** (NIT), applied: the run's check covers `rms_by_position`'s keys.
- **F7** (NIT), applied in the note: the diagnostic lines carry their counts at the end or before the suffix; a refusal
  ends with its own line.
- **F8** (NIT), applied: the builder's usage line names itself.
- **M1–M8**, each met by a case, and each killed in the mutation pass (M7's in the snippet test's): M1 by a warning
  ahead of the count line; M2 by ten STOP-branch print cases; M3 by the anchors and the long-count cases; M4 by an empty
  output folder made after the smoke; M5 by an index git cannot read, at step 0, after the smoke and after the run; M6
  by a hidden file in the outputs; M7 by a fixture per conjunct and the printed comparison's lines, with 23 mutants of
  the snippets; M8 by the copy's index hashed before and after a run over a stat-dirty file.
- **The observations:** O1, O2, O4, O5, O6 and O11 ask for nothing. O3 stands: the box printed 571/571. O7, applied in
  the script: a work folder whose path begins with the copy's is refused, as the self-test would refuse its temporary
  folder (the workbeside case). O8: the relay carried the note's final hash. O9: the stand-in now writes the
  self-test's warning case and lists dotfiles as `iterdir()` does. O10: cases for a missing argument, a copy or a
  parent that is not a folder, a failing mkdir, a failing `git status`, a smoke with no record, and an exit 0 with no
  `gvec.json`; the named-file branch stays redundant beside the two counts.
- **The reviewer's departures,** as its report states them, are in the run's entry, for the seat to class.

**The tests after,** on the relayed bytes: the harness 418 of 418; a mutation pass of 82 one-line mutants, all killed
(80 in the full pass, N5 and R9 alone after their literals were rewritten); and the snippet test, in a battery window,
90 of 90 checks over 73 fixtures with 23 mutants of the snippets, all killed.

## 2. The report as returned

BLIND REVIEW: S/step4b/gvec2/launch/gvec_v2.sh and its companions, at HEAD 616e940

I read the brief in full; its sha256 is f6898d67…a4ec and it has 105 lines. I hashed all eight named files and each matched its stated sha256 before I read it in full. The repository's HEAD is 616e9407c724…9103. Every repository file I read was checked clean against HEAD with `git rev-parse HEAD:<path>` = `git hash-object <path>`.

**Result:** no BUG. There are 8 findings (5 RISK, 3 NIT), 8 surviving mutants (M7 is a group), and 11 observations. Four departures are stated at the end.

## FINDINGS

**F1 (RISK): S/…/gvec_v2.sh:228–229, and :154–155**
- **What is wrong:** the diagnostic-line patterns have no end anchor.
  - `…4 96, 5\.\.n 3683` also matches a tail count that only starts with 3683, such as 36830 or 36831.
  - The smoke's patterns stop at `tokens 0 ` and check no count at all.
  - The record check's COUNTS (:275, :283) is exact, so a wrong count still FAILs through RECQ. The print check by itself is a "count matched loosely" (Q4).
- **Fix:** end PD1 and PD2 with `5\.\.n 3683(; not finite, recorded as null: [^;]+)?$`. This keeps a null figure passing; gvec.py:259's suffix contains no ";". End S6 and S7 with `tokens 0 $SMOKE_N, 1 $SMOKE_N, 2 $SMOKE_N, 3 $SMOKE_N, 4 $SMOKE_N, 5\.\.n [0-9]+(; not finite, recorded as null: [^;]+)?$`, inside double quotes.

**F2 (RISK, low probability): :161 with :184, and :264 with :287**
- **What is wrong:** CONVENTION, which contains "§", is passed as an argument to `python -I`.
  - `-I` ignores PYTHONUTF8, so `sys.argv[5]` is decoded with the box locale's codec.
  - Under any UTF-8 locale, and under C or POSIX (PEP 538/540), it decodes correctly. Under a non-UTF-8 locale, "§" decodes to other characters. "convention" then FAILs a good smoke, and the run of record never starts.
  - v1's snippets took no non-ASCII argument. Neither the harness (jq) nor the snippet test (macOS, where argv is always UTF-8) can reach this.
- **Fix:** in both snippets, use `conv = sys.argv[5].encode(sys.getfilesystemencoding(), "surrogateescape").decode("utf-8")`. Alternatively, pass the convention's sha256 and compare by hash.

**F3 (RISK): :280–282, the record's "site" check**
- **What is wrong:** it checks only that site.site is 31 or 32 and equals of_record.site, with route B; on a STOP, that both are null. It never re-derives the decision from the record's own `site.rel` and `site.within`.
  - A record whose status contradicts its own figures would hold: a PASS with |R/25.49 − 1| > 0.02 at the site, or a STOP with an index within 2%.
  - §1.5's two outcomes turn on this decision. choose_site is self-tested (gvec.py:778–787), so the check is right today.
- **Fix:**
  - PASS (s = the site): add `site["within"][str(s)] is True and site["rel"][str(s)] <= 0.02 and site["rel"][str(s)] == min(site["rel"].values())`.
  - STOP: add `not any(site["within"].values()) and min(site["rel"].values()) > 0.02`.

**F4 (RISK): :88–90, and their uses at :96–97, :202, :308**
- **What is wrong:** the changed-set checks see only what git does not ignore.
  - `.gitignore` ignores `/data/*` (:5), `/data/n/*` (:263), `/data/n/ckpt/*` (:291), `/data/n/reports/*` (:296) and the staging folder (:306).
  - A write there by the self-test, `hashes`, the smoke or the run passes "the copy after the smoke: unchanged" and "data/n/gvec/ alone". Only data/n/gvec and data/n/.gvec.staging are tested by name.
  - So the header's "Nothing that existed before the launch is changed" is checked for tracked and visible paths only.
- **Fix:** add `--ignored` to copy_status. A fresh sparse copy has no ignored files on disk, so the wanted outputs stay as they are now: empty at step 0 and after the smoke, and "?? data/n/gvec/" alone after the run.

**F5 (RISK): :69–81**
- **What is wrong:** a work folder under /workspace/models passes every refusal.
  - The script then writes selftest.txt, hashes.txt and the self-test's temporary files into the model volume.
  - The driver refuses the smoke's --out there only afterwards (`guard.REFUSED_ROOTS`, valence_core/n/guard.py:30).
  - Respawn step (i) re-hashes that volume.
- **Fix:** after :80, add `case "$W/" in /workspace/models/*) echo "REFUSED: the work folder is under the model volume"; exit 1 ;; esac`.

**F6 (NIT): :283–285 against :176–180**
- **What is wrong:** the run's record check leaves out the smoke check's `sorted(dg[i]["rms_by_position"]) == sorted(POS)`. COUNTS pins n_by_position's keys; nothing pins rms_by_position's keys.
- **Fix:** add that conjunct.

**F7 (NIT): S/…/gvec_launch_note_v2.md:75 and :98**
- **What is wrong:**
  - :75 says each diagnostic line ends with the token counts. A null figure appends "; not finite, recorded as null: …", which the script must accept and does.
  - :98's "`gvec v2 FAIL: …`, exit 1 (a refusal included)" is not quite right. The argument refusals (gvec_v2.sh:67, 71, 73, 74, 75, 79, 81) end with "REFUSED: …", a failed mkdir (:82, :107) ends with mkdir's message, and a missing argument (:62–64) ends with bash's usage line. Each still exits 1.
- **Fix:** write "each carrying the token counts …" and "a refusal before step 0 ends with REFUSED: …".

**F8 (NIT): S/…/make_manifest3.sh:9–10**
- **What is wrong:** the usage text names make_manifest2.sh. This file was named in the brief without a hash; I hashed it as 3fb4eaad…2a33.
- **Fix:** correct the name.

## SURVIVING MUTANTS
Each one-line change below passes all 286 harness checks by my reading.

**M1, :112:** `tail -n 1` → `head -n 1`.
- Every stand-in `--selftest` prints a single line. On the box, selftest.txt opens with library warnings (results/raw/2026-11-19_n-gvec-v1_out.txt:65–66), so this mutant would FAIL a good self-test.
- **Kill:** a `--selftest` mode that prints a warning to stderr before the count line, expecting PASS.

**M2, :246–249 (the STOP branch):** weaken any one of these ten conjuncts to `-ge 0`: P1, P2, P3, P4 (=9), PN, P5, P6, P9 (=0), PE (=0), PSM (=0).
- No STOP-mode case gets any of them wrong. runno1/2/3, runtok8, runnocount, runtok95, runno5/6, runnoE and runsmokeline are all PASS-mode. Example: `[ "$PN" -eq 1 ]` → `[ "$PN" -ge 0 ]`.
- **Kill:** STOP-mode variants of those cases, plus a STOP that also prints "G-VEC PASS" or an R_ell line.

**M3, :228:** `5\.\.n 3683'` → `5\.\.n 368'`. This survives because the pattern is unanchored and every case prints exactly 3683.
- **Kill:** a run mode whose diagnostic lines print 3684 while the record keeps 3683.

**M4, :202:** delete `&& [ ! -e "$FR/$GS" ]`, or the `$G` test.
- No smoke case leaves anything in the copy that git status cannot see. The driver's own refusal (n_sessions.py:2160–2165) still FAILs the run, but only after the run of record is invoked.
- **Kill:** a smoke mode that makes data/n/.gvec.staging (ignored) or an empty data/n/gvec, expecting "copy after the smoke 1".

**M5, :96:** delete `|| { … exit 1; }`.
- No case makes git status fail, so a failing status reads as an empty, clean changed set.
- **Kill:** corrupt copy/.git/index (rev-parse HEAD still works), expecting "gvec v2 FAIL: git status".

**M6, :259:** `ls -A` → `ls`.
- No case leaves a hidden file in data/n/gvec. The stand-in's own file-line loop and record emulation (standin :49, :189, :224) also skip dotfiles, unlike the driver's `iterdir()`.
- **Kill:** a run mode that writes data/n/gvec/.extra, expecting "outputs 1".

**M7, the heredoc bodies (:130–135, :162–193, :265–298):** the harness never executes them. The stand-in matches each one by a marker string and runs its own jq. These one-line edits survive the snippet test too:
- (a) :176, drop the rms_by_position key check;
- (b) :178, `POS[:5]` → `POS[1:5]` (s_count changes position "0" only);
- (c) :184, `==` → `>=` (s_tin raises the count);
- (d) :176 and :283, `set(…) == KEYS` → `>= KEYS` (no fixture adds a key, against §1.3's "Nothing else");
- (e) :284, drop the max_norm key check (only the smoke has s_maxkey);
- (f) :286, drop `neutral_tokens == 4163`;
- (g) :181 and :277, drop the stage conjunct;
- (h) :279, drop the `rel` conjunct;
- (i) :186 and :293, alter `first` (no test reads the printed comparison).

**Kill:** one fixture per conjunct, plus a check of the printed "the first run's R …" text.

**M8, :89:** drop `GIT_OPTIONAL_LOCKS=0`. git status may then rewrite the copy's index, against the header's claim.
- **Kill:** compare copy/.git/index's sha256 before and after a case in which a tracked file's mtime was touched.

## OBSERVATIONS

**O1 (Q1, literals and figures): every literal matches the code at 616e940.**
- **Lines:**
  - SMOKE_LINE matches n_sessions.py:2179–2180.
  - The STAGE form matches n_sessions.py:2181–2182; the v1 out raw at :88 and :104 shows both out paths as printed.
  - DRIVER matches :2191–2192.
  - passages matches gvec.py:431, and R_COUNT_LINE matches gvec.py:439–440.
  - site, contexts, R_ell and cosine match gvec.py:462, :477, :502 and :519.
  - The file and end lines match n_sessions.py:2276, :2278 and :2280.
- **Byte equality:**
  - STOP_LINE equals gvec.py:128–129 by reading.
  - STOP_END equals n_sessions.py:2040–2041 by shell comparison.
  - CONVENTION equals gvec.R_CONVENTION by shell comparison; its sha256 is d95e775f…0cc3 both ways.
- **Constants:** COMMIT is HEAD, and DRIVER_SHA256 is HEAD's blob digest of the driver.
- **Figures:**
  - The first run's neutral row reads "96 passages, min 35, mean 43.36" (out raw :116). 4,163 is the only total that prints 43.36 (4,162 gives 43.35 and 4,164 gives 43.38), so 4,067 tokens sit at positions 1..n.
  - The minimum of 35 tokens gives 96 at each of positions 0–4, and 4,163 − 480 = 3,683 over 5..n.
  - The snippets' first-run figures equal out raw :94–95 (the smoke) and :120–121 (the run).

**O2 (Q6, the manifest):**
- **Hashes:** all 61 lines equal HEAD's blobs.
  - 44 were checked by `git cat-file`.
  - The adapter, the 14 skeletons and the two model-folder files were checked through glob `cd`s and blob ids.
- **The set:** it is exactly the committed files the stage and its self-test read:
  - the driver;
  - all 16 n files, since the package hash reads every *.py;
  - the 12-file closure;
  - box_e0_corpus.py with its frozen three inputs and e2a_tasks for hygiene;
  - ids (i)–(v) and MANIFEST.json, since ids.load reads every listed file, gcal_prompts.jsonl included;
  - passages.jsonl;
  - reduced.json, read by the backend-ext self-test, and analysis.json, read by the gvec self-test;
  - the determinism raw and the artifact;
  - the model manifest.
- **Skeleton folder:** at HEAD it holds exactly the 14 files, and load_sessions refuses any other set (sessions.py:107–109).
- **Nothing extra:** every listed file is read by the stage or the self-test. The adapters folder's fourth file is not imported and is rightly absent.
- **hashes file:** the package line, recomputed by shell from HEAD's blobs, is d3415b10…a519. The 12 closure lines equal the manifest's digests and out raw :72–83.

**O3, SELFTEST_LINE:** the +11 holds at 616e940.
- The laptop has three skip lines: hftiny.py:56, n_sessions.py:1537, and n_sessions.py:3561 (G-CAL-n's HF path, new since v1).
- The box runs 14 checks in their place: hftiny's 12, plus one each at :1534 and :3549.
- So 571 holds if the laptop's 560 (RESULTS.md:48) stands. The box count is still arithmetic until the box prints it. A divergence stops at step 2, which is fail-closed, but costs a new script version, since SELFTEST_LINE is a literal.

**O4 (Q2, "none a decision"):** no diagnostic figure is gated on its value anywhere.
- The print patterns take `.+` and stop before the not-finite suffix. The record checks take keys, the counts and the list type.
- A null figure prints "None" plus the suffix, and fails nothing. smokenonfin, recnonfin, s_nonfin and r_nonfin cover this.
- The smoke's R and R_ell finiteness check is a form check outside §1.3's block.

**O5 (Q3, exits):**
- VD starts as FAIL (:140) and becomes WANT only at :313, with all five checks held. WANT is tied to RUN (:220).
- In bash, nothing else in the script exits 2.
- A run that exits 2 for another reason fails the STOP branch's prints. argparse's usage error, for example, also exits 2.
- Because a shell syntax error also exits 2, the exit file alone is not the verdict. The last line is, as the note says.

**O6 (Q7, Q8, writes and order):**
- Writes are as declared: <work>, the copy's data/n/gvec/ and its staging folder, plus the libraries' caches in the home folder.
- Removals are as declared: only the self-test's temporary folder (rmdir, only if empty) and, on a failure, the stage's own staging folder.
- Every gate holds before its step.
- The driver's own refusals back the script's gates: an existing out or staging folder, the pod, cuBLAS.

**O7, folder naming:** the driver's self-test refuses a TMPDIR whose path string merely begins with the copy's path (n_sessions.py:248, `str.startswith`). The script's check at :81 is bounded by "/". So a work folder named `<copy>-work` would pass the script and FAIL step 2. The proposed names do not collide; worth one line in the note.

**O8, the note's hash:** filling the note's mutation slot (@MUTN@ and @MUTRESULT@, :123) changes its sha256 (eb63ab79…9430). The relay must carry the final hash.

**O9 (Q10), stand-in mirror gaps:**
- The stand-in's `--selftest` prints one line (see M1).
- It uses `"$d"/*`, which skips dotfiles (see M6).
- jq's `type == "number"` accepts an integer R that Python rejects; the snippet test's s_int covers this.
- It echoes `--out` as given, where the driver prints `Path(out).resolve()`. These are equal while W is built with `pwd -P`.
- Its run writes nothing to stderr, so the box's interleaving is not exercised. That is harmless for counts.

**O10 (Q10), branches no case reaches:**
- a missing argument (:62–64);
- the copy not a folder, or the work folder's parent not a folder (:74–75);
- either mkdir failing (:82, :107);
- git status failing at :96, :202 or :308;
- every print present but no smoke record (:159);
- an invisible output folder after the smoke (:202);
- the ten STOP conjuncts (see M2);
- a named file missing on a PASS (:254–258), which is redundant given NL and NALL;
- a hidden entry in the outputs (:259);
- an exit of 0 or 2 with no gvec.json (:305–306);
- all the Python heredoc bodies, which only the snippet test runs.

**O11, the snippet test's count:** I checked the brief's counts by reading the code: the harness has 286 checks, and the snippet test has 53 checks over 48 fixtures.

## DEPARTURES

1. **The marker rule:** one `/usr/bin/grep -n -E` passed the glob `valence_core/m/*.py` (with `valence_core/n/*.py` and `valence_core/*.py`) without my first reading its expansion. `valence_core/m/*.py` expanded to two paths whose names hold guard markers: the m package's two runner files. Both were in grep's argv, and grep scanned their contents. No line from either matched or was printed.
2. **No grep in S:** one `/usr/bin/grep -c` for a carriage return over three named files in S (gvec_hashes_v2.txt, gvec_manifest_v2.txt, gvec_v2.sh). It printed counts only, 0 each.
3. **No pathspec:** one `git log -1 --format='%H %s'` ran without item 3's pathspec. It printed HEAD's id and subject.
4. **Folder or "." instead of item 3's pathspec:**
   - `git ls-tree --name-only HEAD valence_core/n/`, twice;
   - `git ls-tree HEAD .` inside valence_core/adapters, which printed modes, ids and names;
   - `git ls-tree --name-only HEAD .` inside the BK skeleton folder, reached by a glob `cd`, which printed its 14 names.
   - `git cat-file` and `git rev-parse` ran on named files, data files among them. None is under ckpt, reports or mf3.

**Stated plainly, not barred by the brief's rules:**
- I read beyond the brief's named list: results/raw/2026-11-19_n-gvec-delta_review.md:136–175, valence_core/n/sessions.py:60–139, valence_core/n/hftiny.py, valence_core/m/resume.py:328–350, and greps of the other n modules for file reads.
- I ran three name-only `ls` (valence_core/, valence_core/m/, valence_core/n/). Their output named those two runner files and the valence_core/mf3 code folder, which is not data/mf3.

I ran no interpreter, wrote no file, and used no network. I did not run the harness, the snippet test or the script. I touched nothing under data/mf3, data/*/ckpt or data/*/reports.
