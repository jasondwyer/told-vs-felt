# n — G-VEC's BUILD: the blind review of draft 1, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over draft 1's five files, from HEAD `003ae7d`:
- `valence_core/n/gvec.py`, new (`5ef276df…d1e7`, 529 lines), read in full;
- the deltas to `valence_core/n/directions.py` (`f9d0114c…2db4`), `valence_core/n/testing.py` (`f1840be7…6aeb`),
  `valence_core/n/guard.py` (`3bf0f0d5…1f50`) and `scripts/n_sessions.py` (`636a4a0e…35ee`).
Draft 1's self-test had not run when the brief went out; it ran 451/451 while the review was in progress.

**The reviewer's brief** (`10f9e31f…ee2e`, 83 lines):
- gave the five files, the `git diff --no-index` form, and the specification: PROPOSAL-n v0.2 §0.8, §2.3, §3's G-VEC
  paragraph and §8 step 7; ADDENDUM-n1 §1.1, §1.2 (iv), §6.1 (quoted) and §6.2; the seat's corpus-adoption answers,
  §1.4; the A3 machinery the stage reuses; the inputs of record; the BACKEND extension's driver code as the template,
  and the analyzer's `--gvec` reader;
- gave Code's G1–G14 message and the coordinating session's routing of it as two verbatim copies in Code's scratch
  (the BUILD's spec raw holds both), and asked whether each departure from their words is sound and declared;
- asked, beside findings, surviving mutants, observations and departures, for any self-test check expected to fail on
  the laptop;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, that a glob is expanded and read before it is looped over, and the `rev-parse` form for a
  tracked-and-clean check;
- barred any interpreter, any write, any network, any guard marker in an argv (paths included: the OLMo adapter and
  the model's data folder read only by the file-reading tool or a redirect), anything under `data/mf3`, any read,
  listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the seven files it named, its
  brief itself excepted.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (306 lines, sha256
`b50cbcaf…d5d4`). It names no local path. Its line numbers are draft 1's: Code's scratch keeps those bytes, unchanged,
as the reviewed drafts; the committed files are draft 3's (draft 2's, with one driver test fixed). Its first line
abbreviates its brief's sha256 as "10f9e31f…e2ee"; the hash ends "…ee2e", as above.

**Totals:** 0 BUG, 5 RISK, 5 NIT, 22 surviving one-line mutants, no self-test risk, and 10 observations.

## 1. Dispositions

Every applied disposition is in draft 2's bytes, but F1's admit lines, which are the BUILD commit's `.gitignore`:
`gvec.py` `a620349f…ec71` (694 lines) and `n_sessions.py` `9ecb4951…eda1`; `directions.py`, `testing.py` and
`guard.py` are draft 1's. Draft 2 ran 461/462: one driver check's list of expected files still held draft 1's four,
without the two alternatives files of F4. Draft 3 fixes that list alone (`n_sessions.py` `fecde87a…3958`, +7 −6) and
ran 462/462. Each run was in a battery window the coordinating session granted for its bytes, and the self-test raw
holds them.

- **F1** (RISK; data/n/gvec/ ignored at HEAD): applied. The BUILD commit adds `.gitignore` lines in 9f64305's form:
  the folder admitted, its contents ignored, and the six named outputs admitted one by one; the staging folder stays
  ignored. G7's wording now names the BUILD commit.
- **F2** (RISK; a stored row's sha16 not the Injection's): applied. `unit32` stores a float32 row that the
  Injection's own normalization leaves unchanged (four passes at most, else a refusal), and every direction sha16 the
  record carries, the 24 random directions' among them, is taken through the Injection itself (`injection_sha16`);
  U's sha16 and A3's freeze_sha stay `sha16_arr` digests. A check holds the row's `sha16_arr` equal to
  `Injection.at_frac(...).direction_sha`.
- **F3** (RISK; figures checked by structure only): applied, with a killing check for each of M1–M22 (below).
- **F4** (RISK; G6's fit-only family not stored): applied. N2's fit-only rows are stored per index in
  `directions_alt_L31.npy` and `directions_alt_L32.npy`, with their sha16s and the files' sha256s recorded.
- **F5** (RISK; model-free work after the load): applied. The staging folder's refusal, the corpus's composition and
  A3's axis order against the named rows all run before the load. A self-test case refuses a leftover staging folder
  with no load.
- **F6** (NIT; no token line per state, the table keyed by the corpus's spelling): applied. One token line per state
  under BK's names, and the record's table keyed by them, the corpus's spelling beside.
- **F7** (NIT; the split not where `extract.assert_stage_splits` reads it): applied. `fit_ids` and `val_ids` sit at
  the record's top level, beside `stage`, and `record()` asserts them.
- **F8** (NIT; no seed pinned): applied. The loaded adapter's provenance is recorded whole
  (`resume.provenance_record`).
- **F9** (NIT; wording): applied. G1's sentence says what the R check tests and what it cannot (O1); G8 says the
  random rows are keys' float64 draws, never stored; the record's rule string carries the tie rule; the absent R_ℓ
  cross-check is recorded in A3's form, with why.
- **F10** (NIT; departures from G1–G14 not marked): applied. `gvec.py`'s docstring ends with the list of departures
  from G1–G14 as routed, and the BUILD entry carries it.
- **M1–M22:** each is killed by a check in draft 2. Each index's rows and R, R_ℓ and the of-record block are checked
  against an independent computation (M1, M2, M8, M9). So are the cosines file, against the read-back site rows (M5,
  M6), and the random ids, against `keys.random_directions` (M7). Further checks hold the tolerance at 0.02, with a
  bar met exactly within (M3, M4); the guard profile with A3's primary and guards as literals (M10, M11); the fit-only
  figures as the fit items' family (M12); and a span at token 0 refused (M16). The driver refuses a context's ids_sha
  and a passage's id, pole and text sha256 (M13, M14), and a context's prefix and full sha256s (M15). The smoke's R
  and R_ℓ are checked against their own computation (M17), all nine foreign flags are refused (M18), and the record's
  backend identifier and BK's literals (against `analysis.json`, the member selected by prefix) are checked (M19,
  M21). The route line is held to its literal (M20), and the token table to the toy corpus's counts (M22).
- **Self-test risks:** none were found. Of the two fragile points the reviewer named, the print test (a bare "ids"
  substring) now looks for any passage id and any bracketed id list; the other stands: a check holds two SVDs of the
  same array bit-equal, the in-process determinism `directions`' own checks already assume.
- **O1:** applied as a hedge. v under an uncentred U is recorded per index (its norm, sha16 and cosine with v) and its
  row stored in the alternatives file, so a strike of G1's centring clause needs no box re-run.
- **O2:** the site rule's two readings (nearer in R; an exact tie to 32) are declared in G2, and the tie rule also in
  the departures.
- **O3:** the departures listed in the docstring and, with G12's smoke form and G14's ‖h̄₊ − h̄₋‖ beside, in the entry.
- **O4:** no action (the inputs and pins verified as stated).
- **O5, O6, O7 and O9:** in the BUILD entry, as Code listed them, on the coordinating session's word: the box's count
  restated at the launch files; a STOP needs data/n/gvec/ moved aside before a re-run; the box smoke, the HF forward
  seam's first run, precedes the run of record; G3 matters only if the site is 31, and both indices are recorded.
- **O8:** applied. The record carries an `of_record` block: the site, its R and R_ℓ, the named directions' sha16s and
  the route line.
- **O10:** applied. The smoke's line says "the first N contexts in A3's order".
- **The reviewer's departures** are in the entry's departures, for the seat to class.

## 2. The report as returned

```text
BLIND REVIEW: G-VEC (n) build, five files. Brief: S/step4b/gvec/review_brief_final.md (sha256 checked, 10f9e31f…e2ee).

BASIS
- All seven named scratch files match the brief's sha256s.
- HEAD is 003ae7d. The four FROM files are tracked and clean (`git rev-parse HEAD:path` equals `git hash-object path`). valence_core/n/gvec.py is untracked (new).
- I got each delta with `git diff --no-index -U3 <from> <to>` and read gvec.py in full.
- Line references: gvec.py:N, directions.py:N, guard.py:N and testing.py:N are the TO files in S/step4b/gvec/draft/. driver:N is S/step4b/gvec/draft/n_sessions.py. Repository files are cited by repository path at HEAD's lines.

SUMMARY
- No BUG-class finding. The stage's order, refusals and arithmetic match n §0.8/§2.3/§3, ADDENDUM-n1 §1.1 and §6.1, and A3's code. a3_capture is extract.capture operation for operation.
- Main gaps:
  - the output folder is gitignored (F1);
  - the recorded sha16 is not the form the runner verifies (F2);
  - the self-test checks the record only by structure, so a one-line slip could make the direction of record come from the wrong index with every check passing (F3; M1, M2);
  - G6's fit-only directions are not stored (F4).
- By my reading the self-test count is 451, as Code expects. I found no check that would fail.

FINDINGS

F1. RISK (certain at the outputs' commit).
- Where: gvec.py:37-40 (G7), driver:141 and driver:1999 put the outputs in data/n/gvec/.
- What is wrong: at HEAD that folder is ignored.
  - .gitignore:262-263 reads `!/data/n/` then `/data/n/*`. Its comment at :260-261 says "nothing else under data/n/ is admitted, and any later n artifact ... needs its own line".
  - `git check-ignore` attributes data/n/gvec/gvec.json and data/n/gvec/directions_L32.npy to .gitignore:263.
  - G7 as sent says ".gitignore admits it". No file under review adds a line, and no docstring says which commit will.
  - A by-path commit of the four files (rule 27) will be refused without -f.
- Fix:
  - Add `!/data/n/gvec/` and `/data/n/gvec/*`.
  - Add one `!` line each for gvec.json, gvec_cosines.json, directions_L31.npy and directions_L32.npy (plus F4's files if adopted).
  - Put them in the BUILD commit or in the outputs' commit (as 9f64305 did for backend-ext-2), name that commit in the BUILD entry, and correct G7's wording.
  - data/n/.gvec.staging stays ignored, which is right.

F2. RISK.
- What is wrong:
  - The record's direction sha16 is `sha16_arr(row)` of the stored float32 row (gvec.py:282, :300, :316-317). The row is float32(v/‖v‖) (gvec.py:203-209).
  - The campaign verifies each direction with `Injection.at_frac(u, ..., expect_sha=identity["directions"][id])` (valence_core/n/runner.py:288-294). That hashes float32(u64/‖u64‖), where u64 is the row read as float64 (valence_core/adapters/base.py:135-136).
  - The schema defines direction_sha16 as "the Injection's direction_sha" (valence_core/n/schema.py:349).
  - The two hashes agree only if re-normalising the float32 row leaves every component's float32 rounding unchanged. That is almost always true for a dense direction (‖row‖−1 is about 1e-9 against a half-ulp of at least 3e-8 relative). It is not guaranteed for a direction dominated by a few components.
  - A mismatch would first show as a SystemExit at the campaign's first steered read, after LOCK-n.
- Fix:
  - In unit32, re-normalise until float32(float64(r)/‖float64(r)‖) == r (one or two passes), and assert `sha16_arr(r64/‖r64‖) == sha16_arr(r)`, refusing otherwise.
  - Self-test: each recorded sha16 equals `Injection.at_frac(row, layer, 0.1, {layer: 1.0}).direction_sha`.

F3. RISK (under-tested).
- What is wrong:
  - The record's figures are checked only for keys, counts and agreement with themselves:
    - gvec.py:499-501 compares of_record with the same rows' sha16s;
    - :496-498 and :502-504 count keys;
    - :519-522 checks the cosines file's form only;
    - the driver's checks are structural.
  - Nothing compares the following against an independent computation: the stored rows at either index, R and R_ℓ at the non-site index, the cosines file's values, the random-sha16 mapping, the fit-only figures, the guard profile's primary and guards, or R_TOLERANCE.
  - Consequence: a one-line index slip makes N1's valence direction of record index 31's when the site is 32, and all 451 checks still pass (M1; M2 for N2).
- Fix: add the killing checks under M1–M12.

F4. RISK (the routing's G6 request).
- What is wrong:
  - The routing asked that N2's fit-only directions be recorded beside "so that a strike would need no box re-run where that's cheap".
  - The draft records only each fit-only axis's norm and its cosine with the all-context axis (gvec.py:302-304).
  - The docstring says "N2's directions fit on fit_ids alone recorded beside" (gvec.py:35-36).
  - A G6 strike in favour of fit-only directions would therefore need a box re-run.
- Fix:
  - Store the fit-only unit rows per index (for example directions_fit_L31.npy and directions_fit_L32.npy, [3, D] float32 in AXIS_ORDER).
  - Record their sha16s and the files' sha256s.

F5. RISK.
- What is wrong: some model-free work runs after the load, contrary to driver:2095 ("Everything that needs no model happens before the load"):
  - gvec.passage_groups, the composition check (gvec.py:250, compute's first act);
  - the leftover-staging refusal (driver:2191-2194);
  - the implicit coupling NAMED == ("valence",) + AXIS_ORDER, which fails only in write() (gvec.py:338, KeyError) after every forward.
- Consequence:
  - A run killed hard (SIGKILL, OOM kill or pod stop) skips the except at driver:2216-2218, so data/n/.gvec.staging is left on the box's checkout.
  - The next run refuses only after a full weights load.
  - No self-test case covers a leftover staging folder.
- Fix:
  - Build `stage` and refuse its existence next to driver:2118.
  - After driver:2160, call `gvec.passage_groups(ps)` and assert `tuple(a3["axis_order"]) == gvec.NAMED[1:]`.
  - Add a leftover-staging refusal case to driver:2412-2441, with len(made) == n_made.

F6. NIT.
- What is wrong:
  - The seat's corpus-adoption answers §1.2 say the passages' length is "a token count G-VEC's raw will print per state".
  - The draft records per-state token figures (gvec.py:255-261) but prints none (compute's lines: gvec.py:251, :270-275, :285, :306-307, :319-320).
  - The table is keyed by the corpus spelling "flow_engagement", while §1.4 says "the paper's state names are BK's".
- Fix: print one line per state under directions.bk_state (n, min, mean and max tokens), and key the record's table by BK's names, or carry both.

F7. NIT.
- What is wrong:
  - G6 says "carry A3's split in the artifact, asserted". The assertion runs on a dict built from e0 (driver:2084-2085).
  - The record carries the split under "a3" (gvec.py:290), not at the top level where extract.assert_stage_splits reads it.
  - Applying that function to gvec.json therefore raises "missing per-stage split ['fit_ids', 'val_ids']".
- Fix: assert on {"stage": rec["stage"], **rec["a3"]} in gvec.write, or carry stage, fit_ids and val_ids at the top level as A3's artifacts do (scripts/box_a3_extract.py:195-196).

F8. NIT.
- What is wrong:
  - adapter.provenance() is read at driver:2182 and then discarded.
  - prov_rec (driver:2172-2178) holds only the identifiers, and m's backend_identifier drops "seed" and "path" (valence_core/m/resume.py:147).
  - So the record pins no seed (rule 27).
- Fix: after driver:2184, add `prov_rec["adapter_provenance"] = m_resume.provenance_record(prov)`.

F9. NIT (wording).
- gvec.py:24-26 says "the R check is its test"; see O1.
- gvec.py:41-42 (G8) says "from the stored float32 rows", but the 24 random rows are keys' float64 rows and are never stored.
- gvec.py:266: the record's rule string omits the exact-tie rule applied at :141.
- gvec.py:295 records `"R_ell_cross_check": None`. A3's form, {"available": false, "note": ...} (scripts/box_a3_extract.py:101-103), would also say why the cross-check is absent.

F10. NIT (declaration).
- What is wrong: gvec.py:22-49 restates G1–G14 with the changes folded in, and nothing marks which words depart from the routed text (O3 lists them).
- Fix: add a "departures from G1–G14 as routed" list to the docstring and the BUILD entry.

SURVIVING MUTANTS
Each is a one-line change to production code. By my reading every current check still passes. A killing check is given for each.

M1.
- Change: gvec.py:279, `valence_at(pc, groups, i)` → `valence_at(pc, groups, idx[0])`.
- Effect: both indices get index 31's valence row, so with site 32 the direction of record is 31's.
- Kill: after gvec.py:491, for each i in L, assert sha16["<i>"]["valence"] == sha16_arr(unit32(valence_at(pc, groups, i)["unit"])).

M2.
- Change: gvec.py:298, `unit32(axes[name][li])` → `unit32(axes[name][0])`.
- Effect: the site's N2 rows are index 31's.
- Kill: with ax = n2_axes(a3_capture(fwd, recs, L), ac, order), assert sha16[str(l)][n] == sha16_arr(unit32(ax[n][li])) for every index and N2 name.

M3.
- Change: gvec.py:70, `R_TOLERANCE = 0.02` → `0.015`.
- Effect: the 2% bar becomes 1.5%. The site cases at gvec.py:439-441 sit at 0.5%, 1%, 1.5%, 1.99%, 2.01% and 3%, and resolve the same for any tolerance in about (0.0100, 0.0201).
- Kill: add `gvec.R_TOLERANCE == 0.02` to driver:2259, and add the case ({31: ref*1.019, 32: ref*1.03}, ("PASS", 31)).

M4.
- Change: gvec.py:137, `<=` → `<`.
- Effect: an R exactly at the bar becomes a STOP (G9 says "≤").
- Kill: assert choose_site({31: 5.0, 32: 100.0}, reference=4.0, tol=0.25) PASSes at 31 (5/4−1 is exactly 0.25).

M5.
- Change: gvec.py:343, `site = ...["site"]` → `site = min(result["rows"])`.
- Effect: gvec_cosines.json, the analyzer's input, comes from index 31's rows when the site is 32.
- Kill: assert the file's cosines == f["cosines"]["named"] == directions.cosines over the read-back site rows (back[4]).

M6.
- Change: gvec.py:314, `analyzer_cosines(rows[s])` → `rows[idx[0]]`.
- Effect: the record's named cosines are from the wrong index.
- Kill: as M5.

M7.
- Change: gvec.py:228, `rr[i]` → `rr[-1 - i]`.
- Effect: the random sha16s and the all-direction table sit under the wrong ids.
- Kill: assert f["random_sha16"] == {rid: sha16_arr(r) for rid, r in zip(schema.RANDOM_IDS, keys.random_directions(be.d_model))}.

M8.
- Change: gvec.py:262, `r[i]` → `r[idx[-1]]`.
- Effect: R at 31 is recorded as R at 32 (A-n1 §6.1: both figures go in the lock). gvec.py:493-495 checks R["4"] only.
- Kill: assert R["3"] == r_at(pc, neu, 3), on the PASS and STOP records.

M9.
- Change: gvec.py:294, `cap.resid_norms[l]` → `cap.resid_norms[idx[-1]]`.
- Effect: R_ℓ at 31 is wrong (this would be the dose map's R_ell if the site is 31).
- Kill: assert f["a3"]["R_ell"] == {str(l): a3_capture(fwd, recs, L).resid_norms[l] for l in L}.

M10.
- Change: gvec.py:77, `A3_PRIMARY = "span_reward"` → `"span_sentiment"`.
- Effect: the guard profile describes the wrong axis. :479-482 checks layers, guard names and r_layer only.
- Kill: assert gp == [asdict(r) for r in extract.axis_report(cap, axes, primary="span_reward", guards={"v2_self": "span_character", "v3_eval": "span_sentiment"})], with scripts/box_a3_extract.py:84 and :159 as literals.

M11.
- Change: gvec.py:78, swap the two guard targets.
- Kill: as M10.

M12.
- Change: gvec.py:288, `a3["fit_ids"]` → `a3["val_ids"]`.
- Effect: the "fit_only" figures describe the val items. :477 tests subset() directly, not compute's call.
- Kill: assert fit_only["4"]["span_reward"]["norm"] equals the norm of n2_axes(subset(cap, ("e01","e02")), ...)["span_reward"][1].

M13.
- Change: driver:2153, `ps + cs` → `ps`.
- Effect: the contexts' ids_sha are no longer re-derived (G12). The only tampering case (driver:2402-2403) tampers a passage.
- Kill: a refusal case with one context record's ids_sha changed.

M14.
- Change: driver:2054 → `i, r["id"], c["state"], r["pole"], r["text_sha256"]):`.
- Effect: the id, pole and text comparisons are dropped. Only the state is exercised (driver:2407-2408).
- Kill: three refusal cases (a changed id, pole and text_sha256), each with len(made) == n_made.

M15.
- Change: driver:2081, delete the `or rec["prefix_sha256"] != …` line (the continuation stays valid).
- Kill: refusal cases with a changed prefix_sha256, and one with a changed full_sha256 (driver:2082).

M16.
- Change: gvec.py:163, `0 < k < S` → `0 <= k < S`.
- Effect: a span starting at token 0 is accepted (extract.capture refuses it). :460-464 tests only k = S.
- Kill: the same case with span_start=0.

M17.
- Change: driver:2198 → `neu = ps[:int(smoke)]`.
- Effect: the smoke's R is taken over the first passages (contentment), not neutral ones. driver:2380-2384 checks keys only.
- Kill: assert rec3["R"]["4"] equals r_at over the first three neutral records.

M18.
- Change: driver:2515, `("--report", a.report is not None)` → `("--report", False)`.
- Effect: `gvec --report X` is silently accepted. driver:2473-2474 tests 5 of the 9 foreign flags.
- Kill: add argvs for --report, --ruling, --tokenizer-dir and --ids-dir.

M19.
- Change: driver:2175, `"backend_identifier": bid` → `CHARACTERIZED_IDENTIFIER`.
- Effect: the record carries the bridge's identifier instead of n's (window 4,096).
- Kill: assert pv["backend_identifier"] == m_resume.backend_identifier(prov_t).

M20.
- Change: any edit to gvec.py:74 ROUTE_LINE, or :73 ROUTE = "A".
- Effect: :499-501 compares the record with the constant itself, so it cannot catch this.
- Kill: assert ROUTE_LINE == "direction of record: Route B" (scripts/n_analyze.py:5292's ROUTE_LINE + "B").

M21.
- Change: any edit to gvec.py:71 or :72 (BK's literals).
- Kill: compare them with data/n/bk/experiment_results_json/fixed_text_design/strength_ladder/analysis.json, member olmo_32b, metas' resid_rms and pole_l2. Both are equal at HEAD.

M22.
- Change: gvec.py:259, `"min": min(v)` → `max(v)`.
- Effect: the per-state token table (F6) is wrong.
- Kill: compare one state's entry with the toy corpus's own counts.

SELF-TEST RISKS
- None found. By my reading no check fails or raises on the laptop. My count matches 451: gvec's own 22 checks, the driver's 18, the environment line and directions' 1, on top of HEAD's 409.
- Fragile, but not expected to fail:
  - gvec.py:505-506 uses the bare substring "ids" as its test for "no passage or context in the prints". That holds for today's lines, but a future line naming fit_ids, val_ids or ids_sha would fail it.
  - gvec.py:436-437 requires two separate SVDs of the same array to be bit-equal (in-process LAPACK determinism, which directions' own checks already assume).

OBSERVATIONS

O1. G1 is only partly tested by the R check.
- The R check reads only the neutral passages' token norms (gvec.py:128-130). It tests "passage alone, no special token, every token in R, pooled RMS".
- It cannot test "neutral PCA centred" (U never enters R), nor which tokens enter the passage mean.
- The routing's ground ("G1 is tested by the R check itself") therefore covers the clauses that bear on R only.
- The passage means are not kept, so a strike of the centring clause needs a box re-run.
- A cheap hedge in the routing's spirit: per index, record v under an uncentred U beside the centred one (its norm, its sha16 and its cosine with v), and store its row.

O2. The site rule's readings are Code's.
- "The nearer" is read as nearer in R to 25.49.
- An exact tie goes to 32 (gvec.py:27-28, :135, :141).
- Both are sound (a tie has measure zero), but the tie is not in G2 as routed.

O3. Departures from G1–G14 as routed (soundness, and whether the draft declares them):
- G7: directions.npz became two .npy files, [4, D] float32 in NAMED order, saved with allow_pickle=False (gvec.py:83-84, :337-342). A3's freeze_sha moved into gvec.json, per index (gvec.py:301). Sound: the per-row sha16 is unchanged and each file's sha256 is recorded. Stated as G7's content (gvec.py:37-40), not marked as a change.
- G2: the tie rule. Sound; stated as part of G2, not marked as a change.
- G2/G3: v, U, h̄±, N2's rows and R_ℓ at both indices. This is the routing's request, and it is declared.
- G5: the guard profile at both indices (G5 said "at the site"). Sound; written into G5's text.
- G6: the routing's fit-only family is recorded as figures only (F4).
- G8: both cosine tables at the site only (gvec.py:42, :310-314). Sound, since both indices' rows are stored.
- G12:
  - the smoke takes one --out folder and N in 1..96 (backend-ext uses --root/--report and 1..24);
  - "no input exceeds 90 tokens" is enforced as ≤ 4,096 and the longest is printed.
  - Sound; the smoke form is in the driver docstring (driver:142-143).
- G14: ‖h̄₊−h̄₋‖ is added beside ‖v‖ (gvec.py:48, :281). Sound and declared.
- G7's ".gitignore admits it" is not true at HEAD (F1).

O4. Inputs and pins verified read-only at HEAD.
- MANIFEST.json's sha256 is ids.MANIFEST_OF_RECORD (fdf73d85…ef38).
- passages.jsonl is ids.PASSAGES_SHA256 (ef6b00dc…3cc3).
- iv.a3.code_sha256 equals HEAD's scripts/box_e0_corpus.py (66c18554…ab57) and valence_core/extract.py (2405b1a6…07fe), so gvec_a3_check's code comparison passes on a HEAD checkout.
- input_shas equal A3's FROZEN_SHA.
- The corpus is 56 × 8 + 96, and flow_engagement is its only differently spelled state.
- Passages are 35–68 tokens and contexts at most 90. span_start == prefix_tokens in all 1,344.
- The record forms carry every field the driver checks.
- gvec.py:71-72 equal BK's olmo_32b metas.
- The analyzer's GVEC_DIRS and ROUTE_LINE (scripts/n_analyze.py:5292-5294) match gvec.py's.
- The toy provenance at driver:2310 has the same form backend-ext's passing self-test uses (scripts/n_sessions.py:1493), and backend_identifier drops "path".

O5. Hashes and counts move.
- n's import closure gains valence_core/extract.py; no module in the closure imports it at HEAD.
- The package digest moves (gvec.py is new; directions.py, testing.py and guard.py changed).
- The hashes window and launch files should state both.
- By 003ae7d's stated arithmetic (13 HF checks in place of the laptop's two skip lines), the box count would be 462.

O6. STOP and re-run mechanics.
- On a STOP, no A3 capture runs and data/n/gvec/ holds the record alone.
- G-VEC never resumes, so any later run needs that folder moved aside first.
- The launch notes should say this and name data/n/.gvec.staging.

O7. Unexercised production seams.
- `_hf_forward` (driver:2025-2029) and production_gvec_env's lambdas run in no check on either site: the self-test replaces every seam and hftiny does not call them.
- The box smoke is their first execution, so run it before the run of record.
- Optional: an hftiny check that adapter.forward(...).acts[l] equals the tiny model's hidden_states[l+1] would pin what "index 31/32" means on the box's own stack.

O8. The record has no explicit R/R_ℓ "of record" pair alongside directions.of_record. LOCK-n has to derive them from the site.

O9. G3 is substantive if the site is 31.
- n §2.3 defines R_ℓ via A3's convention, and A3's own "layer 32" is adapter index 32 (scripts/box_a3_extract.py:82).
- G3 reads "at the site" instead.
- Both values are recorded, so the seat's ruling needs no re-run.

O10. The smoke's R_ℓ is over the first N contexts in A3's order (task e01's first conditions), not a sample of the corpus. Its printed line could say so.

DEPARTURES
None that I read as barred. For the record:
1. The harness saved the 36 KB driver diff into its own tool-results store (neither S nor the repository), and I read it back with the file-reading tool. I wrote no file.
2. I used jq beyond the first lines the brief names:
   - whole-file aggregates over data/n/ids/gvec_passages.jsonl and a3_contexts.jsonl (token counts and span starts; no id printed);
   - state and pole counts over data/n/passages.jsonl;
   - two values from BK's committed strength_ladder/analysis.json.
3. I ran one `git check-ignore -v --no-index` naming three non-existent paths under data/n/ (gvec/gvec.json, gvec/directions_L32.npy, .gvec.staging/x), without item 3's pathspec.
   - It is a command on named paths, not over the tree, and reads only .gitignore.
   - It named no ckpt, reports or mf3 path.
   - If "named non-data files" is read strictly, this is a departure.
4. Print tools beyond those the brief names:
   - `/usr/bin/sed -n '164,170p'` with `cut` on PROPOSAL-g-ontogeny-of-evaluation.md;
   - `wc -l` on six valence_core files;
   - one root `ls PROPOSAL-g*` (one name, not looped over).
5. valence_core/adapters/olmo_hf.py was read only with the file-reading tool.
```
