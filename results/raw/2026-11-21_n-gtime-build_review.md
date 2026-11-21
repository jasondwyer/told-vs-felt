# n — G-TIME-n's BUILD: the blind review of draft 3, as returned, with every disposition

PI date 2026-11-21. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over the change as draft 3 had it, at HEAD `2ca24e8`:
- `scripts/n_sessions.py`, HEAD's (`593a140d…a549`) to draft 3 (`f4e2c8b9…d608`, 5,057 lines);
- `.gitignore`, HEAD's to the draft with one block added for G-TIME-n's outputs (`1f2461bd…58b8`).

Draft 3 had passed its self-test, 623/623, in a battery window.

**The reviewer's brief** was a file in Code's scratch (`9ab6524c…afeb`, 93 lines), which the reviewer checked by its
sha256. It:
- named the change and the specification: G-TIME-n's spec raw and the seat's block, both committed at `2ca24e8`, the
  texts, and the code the change must match;
- named five things Code knew of, to be declared;
- asked for findings, surviving mutants, box risks, observations and departures;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv (a grep pattern included),
  and Q-F3's folder by its plain name in any argv;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, and anything in Code's scratch but the brief and the two named files;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec with `':!data/m[f]3/**'` on every
  git command over the tree.

**The report** is in §2, extracted verbatim by `jq` from the hand-back in the subagent's own transcript (189 lines,
sha256 `004f9c8e51fbf3fb4a7de21397f0c57e3120688680b5989d78d94dfad98c0915`). It names scratch files only by their paths
inside the scratch folder.

**In sum:**
- no BUG;
- 11 findings: F1–F5 RISK, F6–F11 NIT;
- 13 surviving mutants, M1–M13;
- 7 box risks, B1–B7;
- 6 observations, O1–O6;
- no departures, and after them five items for classing, not barred by the reviewer's reading (§2's last lines).

Draft 4 (`24b0cd44…22aa`, 5,193 lines) builds in F1, F2, F3, F5, F6, F7 and F9 and a kill for every mutant but M8. It
passed its self-test, 633/633, in a battery window. The values-check found M8 alive in draft 4. Draft 5
(`4616f9c3…2553`, 5,208 lines), the BUILD's driver, adds its case, through the stage, and passed its self-test,
634/634. The rest are declared in the BUILD entry, or carried to the launch files or to the seat.

## 1. Dispositions

- **F1 (RISK), the projection's figures unpinned. Applied.**
  - The stage now passes its clock to the runner (`StageInputs(clock=env.clock)`). On the box that is
    `time.perf_counter` either way.
  - The self-test's environments get a clock that ticks 1 ms a call, so every duration is exact. One check then pins
    every figure by literals: c and f, T at the medians and the maxima (18,997 ms), the extension's T, the load, the
    benchmark's appends and its line, its projection, the per-read I/O (2 ms on reads 1–17) and its lower bound, and
    every hours figure. That kills M2–M5 and M12.
- **F2 (RISK), six guards without a case. Applied, with a case for each:**
  - a stream whose known answer differs, refused before the load (M7);
  - `same_filesystem`, the device check factored out with its stat injectable, failing for another device. That case
    tests the helper alone. Draft 5 adds one that runs the stage with the check failing, refused before any read
    (M8);
  - a second run without `--resume` after the PAUSE, refused by `prior_state` before the load (M1);
  - after the load, a provenance other than the one checked and a checkpoint of another shape, each refused before
    any read (M6);
  - G-VEC's inputs with another valence row or site, refused (L §3), and an R off the pinned map by one part in 10^12,
    refused at the rebuilt map's equality (M9).
- **F3 (RISK), gread-bench's shapes unchecked. Applied.** A spy on `probe.layer_auc` checks each timed call: its
  shape (320 rows, then 80, at the width given), no shuffle, and `CV_SEED`. The same check holds the function's
  defaults: 10 calls, the model's width 5,120, and a band of 31 (M10).
- **F4 (RISK), the resume after COMPLETE reloads the weights. Declared, not built.** That resume is the recovery when
  the projection fails after the reads. It runs G-VER and loads the weights again, and rewrites the report with a
  second entry in `loads_ms`, which the artifact's loads then count. That is the recovery's cost. The launch files copy
  back only after the last invocation (B3).
- **F5 (RISK), a failed cleanup after COMPLETE. Applied.** The benchmark's temporary folder takes
  `ignore_cleanup_errors=True`, a folder left behind is said, and the artifact is still written. No self-test case
  induces a cleanup failure.
- **F6 (NIT). Applied:** `GTIME_N` = (1 + len(`GTIME_STEERED`)) × len(`GTIME_RUNS`).
- **F7 (NIT). Applied.** `check_gtime` now requires the 18 reads at a run of record and the smoke's count at a smoke,
  and the campaign's 7,680 reads, the lock's (`LOCK_CAMPAIGN_READS`, L §6). Its docstring now says what it checks. Two
  tamper cases are added: 17 reads, and 7,679 campaign reads whose sums still hold.
- **F8 (NIT), three wordings. Declared in the BUILD entry; the third is corrected for the seat in the supplement**
  (`results/raw/2026-11-21_n-gtime-starred-seven-supplement_code-to-design_STOP.md`):
  - GT3's "campaign_order is not used" is about the stage's own plan. `campaign_counts` runs it over the campaign's
    view of the identity, for N and K, as GT8 states;
  - GT9 (b)'s "from one launch to the next" is built as from one per-read line to the next. The interval also holds
    the read's own append and the loop's work outside `duration_ms`, which is sound as option (ii)'s lower bound;
  - the block's GT9 says the template is re-keyed with "its session's ids". `rekeyed` moves the session's id, cell
    and run, the read ids and the launch index, and leaves every other field as the template's.
- **F9 (NIT). Applied:** the bench folder's in-repository refusal is asserted by its text (M13).
- **F10 (NIT). Declared, and corrected for the seat in the supplement:** every pin is checked at every invocation, a
  smoke's too, not only at a run of record.
- **F11 (NIT). Not adopted.** Both functions are in one module, and the two traps around main()'s cases suffice. That
  is the reviewer's own reading.
- **M1–M13.** Each is killed by the case its row names: M1 by F2's re-run case; M2–M5 and M12 by F1's literals; M6, M7
  and M9 by F2's cases; M10 by F3's spy; M11 by a check that the production environment's benchmark appends 160
  records; M13 by F9's text. M8 is killed in draft 5 alone, by its case through the stage. The values-check found that
  draft 4's case tested `same_filesystem` itself, so the guard changed to `if False:` passed every check.
- **B1, B2, B6: carried to G-TIME-n's launch files**, to the coordinating session first. They create `--bench-dir` on
  the volume and name it (B1), clean a killed benchmark's leftover folder (B2), and capture stderr with stdout in the
  raw (B6).
- **B3:** with F4, the copy-back comes after the last invocation.
- **B4:** as the reviewer reads it, no self-test case reaches a production loader or writes a canonical folder, on the
  box after the commit too.
- **B5, declared.** The closure is held to the lock's twelve files exactly at every invocation. G-CAL-n's box record,
  measured at the same point, lists exactly those twelve. An extra `valence_core` import before the measurement would
  refuse every invocation, and the self-test checks inclusion only.
- **B7, declared.**
  - The copy-back is by hash: the artifact names the report's sha256, and the report names each cell file's.
  - `GTIME_ROOT` is fixed, so a re-run of record after a box change must first move the committed outputs aside.
    Whether it re-runs is the PI's (GT16).
- **O1, noted:** the readings as built, with F8's and F10's notes.
- **O2, to the seat as Q8,** in the supplement committed ahead of the BUILD (`4fdcdcc`). The BUILD's `.gitignore`, its
  second draft (`dee52f42…b272`), admits only the shadow cell, the report and the artifact: the safer form, pending
  the seat's answer. The first draft, which this review read, admitted all three cells.
- **O3–O6, noted.**
  - O3: Q4's variants are re-derivable from the stored appends.
  - O4: `gvec.json`'s and `directions_L32.npy`'s sha256s are not pinned by the stage. What the identity uses is pinned
    another way: the valence row by its sha16, and R and R_ell through `dose_map.json`'s pin and the rebuilt map.
  - O5: the 21 pinned values are in LOCK-n.md.
  - O6: item 5's five bullets are sound.

## 2. The report as returned

BLIND REVIEW: G-TIME-n BUILD, draft 3 (scripts/n_sessions.py and .gitignore)

Checked by tool:
- The brief matched its sha256 (93 lines). HEAD is 2ca24e8.
- scripts/n_sessions.py and .gitignore are tracked and clean (rev-parse equals hash-object).
- All three digests matched the brief's (shasum -c: OK).
- Line counts are 3,777 at HEAD and 5,057 in TO.
- The .gitignore delta is one block, gitignore_v1:331-343.
- Driver delta: the docstring (TO:8-15, TO:181-236), cmd_selftest (TO:408-412), the G-TIME-n section (TO:3738-4921), and _parse_rulings and main (TO:4923-4981).
- Names used below: TO = S/step4b/gtime/draft3/n_sessions.py; gitignore_v1 = S/step4b/gtime/commit/gitignore_v1.

I found no BUG: the production path does what GT1–GT17 and the STOP block say. Most findings are test gaps (RISK) and wording (NIT).

FINDINGS

F1 RISK — the projection figures the PI reads are not pinned by any check (TO:4025-4046, 4284, 4347-4348).
- check_gtime (TO:4121-4124) recomputes model_time, beside and pod_hours through the same gtime_figures. So it guards the artifact's consistency, not the arithmetic.
- The flow checks (TO:4681-4699) pin T_median_ms, T_max_ms, the counts and the pairs. They pin no *_h figure, no projected_ms, lower_bound_ms or T_extension_ms, and no io_ms or loads_ms value. M2–M5 and M12 survive because of this.
- Fix:
  - pass clock=env.clock into StageInputs at TO:4302-4305 (production is unchanged: perf_counter either way);
  - give the flow env a clock that ticks once per call;
  - assert exact loads_ms and every io_ms;
  - assert projected_ms = a·7,680 + b·322,560, lower_bound_ms = median io × 7,680, T_extension_ms = 7,680·309.0 + 3,637·357.1, and each *_h = *_ms / 3.6e6.

F2 RISK — six pre-load or post-load guards have no case:
- the driver's stream known-answer check (TO:4216-4218);
- the bench folder's filesystem check (TO:4205-4207);
- prior_state before the load (TO:4275);
- the post-load provenance and shape checks (TO:4286-4289);
- gtime_lock_inputs' site/valence check (TO:3860-3861) and rebuilt-map check (TO:3879-3880).

Each can be disabled with a one-line change that still passes (M1, M6–M9). Most mirror run_backend_ext, but GT6's "exit 2 before the load" is G-TIME-n's own claim. Fix: one case each, as the mutants' kill checks describe.

F3 RISK — gread-bench's small run (TO:4906-4911) times with a clock that ticks per call. So the shape timed per kind, shuffles=0 and the width are all unchecked (M10), and any of them could scale GT10's projection without a check failing. Fix: spy on probe.layer_auc during the small run and assert each call's (X.shape, shuffles); also check gread_bench's defaults (calls, D_MODEL, band 31).

F4 RISK — resume after COMPLETE (asserted at TO:4732-4739) does more than the projection needs:
- it re-runs G-VER and reloads the weights to compute a model-free projection;
- it rewrites data/n/reports/time.json (a second loads_ms entry, a new report sha256);
- it puts a read-less load into pod_hours.loads_ms.

Fix: when the report on disk is COMPLETE and the records are the plan's (prior_state has already checked the identity), skip G-VER, the load and the runner; take loads_ms and the report sha256 from disk; run the benchmark and write the artifact. Otherwise, declare the second load as this recovery's cost.

F5 RISK — TemporaryDirectory (TO:3981) raises if cleanup fails. That failure lands after the runner has written COMPLETE, so the stage exits 1 with no artifact, and recovery is F4's reload. Fix: ignore_cleanup_errors=True, or catch OSError, and print the leftover folder's path, so the artifact is still written.

F6 NIT — GTIME_N (TO:3748) hard-codes 3 reads per session. Fix: (1 + len(GTIME_STEERED)) * len(GTIME_RUNS), so that GT1 sits in one place (the STOP block §0). As built, a change to GTIME_STEERED alone would leave the smoke bound and check_gtime at 18; check_gtime would then refuse the artifact, so this is not silent.

F7 NIT — check_gtime's docstring (TO:4073-4076) says "the campaign's counts and plan the lock's", but only read_plan_sha256 is held to the lock (TO:4112).
- The counts are checked for internal sums only.
- len(reads) is not tied to smoke: a run-of-record artifact with fewer than 18 rows passes (TO:4097).
- Fix: require len(reads) == (GTIME_N if smoke is None else smoke) and camp["reads"] == 7680 (L §6), or reword the docstring.

F8 NIT — departures from the readings' words, for the BUILD entry to declare:
- GT3 says "campaign_order is not used", but campaign_counts (TO:3910-3926) runs it over the campaign's view to get N and K. The STOP block's GT8 states this use, so GT3's sentence should be read as about the time plan only.
- GT9 (b) in §1 says "from one launch to the next". The build (and the STOP block) times from one per-read line to the next (TO:4295-4301, TO:4347). That interval also holds read i's own append and the loop's work outside duration_ms. This is sound as option (ii)'s lower bound.
- The STOP block's GT9 says the template is re-keyed with "its session's ids". rekeyed (TO:3942-3955) moves only the session's id, cell and run, the read ids and the launch index; ids_sha, ids_sha_bk, seq_len, steered_spans, mask_sha16, the cues and the labels stay run 0's. The schema does not cross-check these (its CROSS-RECORD PROPERTIES paragraph) and record size is unchanged, so timing is unaffected. Reword "ids" to "id, cell and run".

F9 NIT — io_bench's in-repository refusal case (TO:4603-4611) names data/n/bench, which does not exist. The is_dir refusal (TO:3973) therefore passes the case even without refuse_test_out (TO:3972); this is M13. Fix: assert the refusal text says "never written inside the repository".

F10 NIT — the STOP block's GT4 ("for a run of record") and the brief's item 5, fourth bullet, understate the build. Every pin, the package and the closure are checked on a smoke too (there is no smoke branch after TO:4196). This is stricter and sound, but a smoke can never run a modified valence_core/n. The entry should say "every invocation".

F11 NIT — the main() trap block (TO:4828-4892) omits G-CAL-n's two extra safeguards (scripts/n_sessions.py:3589-3593 at HEAD): a cuBLAS setting the stage refuses, and the cmd_gcal.__globals__ is g assertion. Neither is needed, since both functions are in one module and the existing traps suffice; adding them is optional.

SURVIVING MUTANTS (one-line changes to TO's production code that pass every check)

M1 TO:4275 — delete the prior_state(...) call (or pass True for resume).
- Why it survives: every second invocation in the self-test either hits the artifact refusal at TO:4197 first or is a legitimate resume.
- Wrong behaviour: a re-run without --resume after a PAUSE runs G-VER, loads the weights, then dies in runner.run with exit 1. It should be REFUSED with exit 2 before the load.
- Kill: after the PAUSE case, run_gtime(env_p, bench_dir=bd) with no resume; expect rc 2, a REFUSED line containing "run with --resume", and made.count("pause") unchanged.

M2 TO:4347 — drop `- by_li[i]["duration_ms"]` (or use by_li[i - 1]).
- Why it survives: TO:4698 checks only which reads have an io_ms, and check_gtime checks only its type.
- Wrong behaviour: the per-read I/O, and option (ii)'s lower bound, include the model time.
- Kill: F1's tick clock, then exact io_ms for reads 1–17.

M3 TO:4030 — swap the coefficients: a_ms * pairs + b_ms * sum(sizes).
- Wrong behaviour: option (i)'s I/O projection (Q4's term).
- Kill: assert projected_ms == a·7,680 + b·322,560.

M4 TO:4033 — divide by 3.6e5 instead of 3.6e6.
- Wrong behaviour: every hours figure is 10× high, and the cap is set in hours.
- Kill: each *_h == *_ms / 3.6e6.

M5 TO:4284 — load_ms = 0.
- Why it survives: only the count of loads_ms entries is checked (TO:4693, 4737).
- Kill: with the tick clock, assert loads_ms equals the ticks across make_adapter.

M6 TO:4286 or TO:4288 — change the post-load provenance test (or the shape test) to `if False:`.
- Why it survives: StubAdapter and adapter_shape never differ from what was checked before the load.
- Kill: make_adapter returning StubAdapter(dict(prov_t, python="3.12.4")), and adapter_shape=lambda a: (6, 13); each should give rc 2.

M7 TO:4217 — change `if ka:` to `if False:`.
- Why it survives: the runner repeats the known-answer check, but only after G-VER and the load, and with exit 1.
- Kill: patch valence_core.m.keys.stream_known_answer to return ["x"] for one case; expect rc 2 and no load.

M8 TO:4206 — change it to `if False:`.
- Why it survives: every case's bench folder and stage root are on one filesystem.
- Wrong behaviour: a bench folder on another disk is accepted, so GT9 (i) times the wrong disk.
- Kill: factor the comparison into a helper that takes the stat call, or patch os.stat for the bench path, and expect "not on the stage root's filesystem".

M9 TO:3860 or TO:3879 — change it to `if False:`.
- Wrong behaviour: another valence row or site, or an R/R_ell off the pinned map, would set the identity's direction or dose map.
- Kill: patch the global gcal_gvec_inputs for one call to return v_sha16 "0"*16 (expect "L §3"), and R × (1 + 1e-12) (expect "is not G-CAL-n's record's").

M10 TO:4417 (swap the two row counts), TO:4425 (shuffles=probe.N_SHUFFLES), or TO:4405 (d_model default D_MODEL // 2).
- Kill: F3's spy.

M11 TO:3749 — GTIME_BENCH_RECORDS = 16.
- Why it survives: every flow env sets bench_records=4.
- Kill: assert penv.bench_records == 160 (penv is built at TO:4841).

M12 TO:4027 (swap N and K) or TO:4044 (mio * len(sizes)).
- Kill: F1's literal checks.

M13 TO:3972 — bd = Path(bench_dir).
- Affects direct callers only; the stage itself refuses at TO:4202 first.
- Kill: F9's text check.

BOX RISKS

B1 — The filesystem check (TO:4205-4207) has never been exercised across two filesystems (M8).
- --bench-dir must already exist, outside the repository, on the same device as data/n/ckpt.
- A folder on /tmp, or a bind-mounted subtree with its own st_dev, is refused with exit 2.
- The launch files should create the folder and name it.

B2 — The benchmark writes about 102 MB (31 arrays of 160 × 5,120 float32) under --bench-dir and fsyncs every row.
- A cleanup failure leads to F5.
- A kill mid-benchmark leaves an n-gtime-bench-* folder behind, which is harmless.

B3 — A resume after COMPLETE reloads the model (F4) and rewrites the report. Copy back only after the last invocation.

B4 — Self-test on the box after the commit: by my reading, no case reaches a production loader or writes a canonical folder.
- Every flow case runs behind GtimeEnv stubs, with root/report/out under tmp; genv refuses repository paths (TO:4659-4661, 4891-4892).
- The in-repository bench and smoke cases are refused before any write.
- main()'s cases run with RUNPOD_POD_ID popped and weights_of_record, _load_adapter and _gver_tokenizer trapped (TO:4832-4846). The argv cases fail in argparse or _parse_rulings before cmd_gtime, and the positive cases hit the recorder.
- If a case did reach the real run_gtime, it would refuse at the filesystem check (if tmp and the volume differ), then at the pod check.
- The environment is restored (TO:4893-4898, 4912-4919).
- There is no new HF seam: adapter_shape and _hf_backend are backend-ext's.

B5 — The exact closure equality (TO:4256): G-CAL-n's box record (data/n/gcal/gcal.json) was measured at the same point (after the provenance and the R6 bridge, before the load). It lists exactly LOCK_CLOSURE's twelve files at its digest prefixes, so the check should pass. Any extra valence_core import before env.package() would refuse every invocation, and the self-test cannot see it because it checks inclusion only (TO:4527-4528).

B6 — Exits and the raw:
- REFUSED lines go to stdout.
- A SystemExit from runner.run or from the projection (TO:4343-4344, io_bench, check_gtime) prints to stderr and exits 1. The launch files should capture stderr in the raw (2>&1).
- A post-load refusal (TO:4286-4289) prints "REFUSED before any read" (exit 2) after the weights have loaded.

B7 — Copy-back:
- Outputs: three cell JSONs (closed under item 2; -diff via .gitattributes' /data/n/ckpt/**), the report, the artifact and the raw. The arrays, about 305 MB, stay on the volume.
- The artifact's report_sha256 and the report's cell sha256s make the copy-back verifiable without reading ckpt content.
- GTIME_ROOT is fixed, so a re-run of record after a box change (GT16) must first move the committed outputs aside.

OBSERVATIONS

O1 — Each reading against the code:
- GT1, GT2: as stated (TO:3746-3835). Runs 0, 32, 64, 95, 127, 159 are asserted equal to round(k·159/5).
- GT3: as stated (driver only; the package and closure are held to L §18), with F8's wording.
- GT4: as stated, and stricter (F10).
- GT5: the runner is unchanged and the identity carries C = 0.25 as both ceiling and bound. The single tail evaluation over 12 trials fires at k ≥ 3: by my arithmetic, P(X≥3) ≈ 0.0096 and P(X≥2) ≈ 0.076 at p0 = 1/26.
- GT6: sound, including the declared exit-1 nuance. Runner-side refusals are unreachable once prior_state and the pins pass, because every identity field is pinned.
- GT7: as stated. G-VER's STOP writes no report.
- GT8: as stated.
- GT9: as stated, with the declared re-keying (sound) and F8's note.
- GT10: as stated. Q5's "per result" alternative is a one-line change to gread_counts' points.
- GT11: as stated. gitignore_v1:331-343 follows the backend-ext pattern; its three cell names equal schema.cell_filename's, and temp files and arrays are ignored.
- GT12: no point below d = 0.
- GT13, GT17: nothing to build.
- GT14: as stated.
- GT15: durations only, no stamps.
- GT16: as stated.

O2 — The committed cells carry steered margins. GT11 admits N1-V__valence__p1.json and N1-V__valence__p1_2.json: the cached margins of 12 steered reads (valence +1 and +1/2) on six of the campaign's sessions. On the deterministic backend these are expected to equal the campaign's own reads of those sessions. Item 2 and -diff close them, but a push to the public origin publishes them before the campaign (n:148, "No looks"); backend-ext's committed cells were d = 0 only. For the seat: confirm GT11 as built, or keep the two steered cells on the box with their arrays (the report and the artifact carry their hashes and every duration).

O3 — Every append's ms is stored, so Q4's variants (dropping k = 0 from the fit, or fitting 40-row cells) can be re-derived without a box run.

O4 — gtime_lock_inputs does not pin gvec.json's or directions_L32.npy's sha256 (L §3 hole 5). What the identity uses is pinned another way: the valence row by its sha16, and R/R_ell through dose_map.json's pin and the rebuilt-map equality.

O5 — Pins: all 21 hex and decimal values at TO:3761-3799 occur in LOCK-n.md, and LOCK-n.md hashes to LOCK_SHA256. The scalars match L §1, §3, §7, §8 and §13 as read, and ids.MANIFEST_OF_RECORD equals L §1's.

O6 — Item 5's five declared bullets are all sound, with the notes in F8, F10, B5 and B6.

DEPARTURES: none.

For classing, not barred by my reading:
- the prescribed `git diff --no-index -U3` command, with its output paged through `grep -n '^@@'` and `sed -n`;
- `grep -o` over data/n/gcal/gcal.json and data/n/gvec/gvec.json (neither is under ckpt or reports), printing module paths, 8-hex prefixes and package digests;
- `wc -l` on named files;
- `sed -n` on cited lines;
- a loop counting the draft's pinned values in LOCK-n.md.

No marker appeared in any argv. In S, only the brief and the two named files were read. Nothing under data/m[f]3, data/*/ckpt or data/*/reports was touched. No interpreter but shasum was run, and nothing was written.
