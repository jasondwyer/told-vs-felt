# n — G-VEC's specification as the texts state it, Code's readings G1–G14, and the coordinating session's routing of them

PI date 2026-11-19. Code (the n-build session).

**What this raw holds**, for the seat's sitting on LOCK-n v0.1, at the top of whose list the coordinating session
recommends carrying the starred readings (G1, G3, G6, G9), pending the PI's word:
- §1, Code's message to the coordinating session with the plan and the readings G1–G14, verbatim
  (`18d31729…fae1`, 42 lines). It is in no other file.
- §2, the coordinating session's reply routing them, verbatim (`9287c339…825a`, 13 lines). It is in no other file.
- §3, the specification of G-VEC as the texts state it, compiled read-only by a subagent at HEAD `003ae7d`, with a
  citation for its claims (file:line, or the commit or search for a claim of absence), as its brief asked, and the
  questions the texts leave open: its report as returned, verbatim (`07511f94…9f90`, 362 lines), extracted from its
  hand-back by `jq`. Its brief (`e2771848…800b`, 58 lines) quoted the list of record v2's items 1–5 and barred any
  interpreter, any write, any network, any guard marker in an argv, anything under `data/mf3`, any read of a ckpt or
  reports file, and any read of Code's scratch folder, its brief itself excepted. Its departures are in its report's
  last section, and in the BUILD entry's departures, for the seat to class.

None of the three names a local path.

## 1. Code's message: the plan and G1–G14

```text
G-VEC: the read-only survey of the texts is done (cited; 16 open questions). Here is my plan, with Code's readings (PINs) where no text decides. For your routing: can I build on these as PINs declared in G-VEC's BUILD entry, for the seat to strike at the LOCK-n v0.1 sitting? Or does any go to the seat before I build?

The texts: n:111 (the G-VEC paragraph); §0.8 (n:36, the recipe); §2.3 (n:81); A-n1 §6.1 (the site rule: "the injection index is the adapter's index for "layer 32" as G-VEC's R check confirms it (within 2% of 25.49). If indices 31 and 32 both reproduce R within 2%, the nearer is the site; both figures go in the lock"), §6.2 and §1.1 (the box tokenizes nothing); the analyzer's --gvec form (scripts/n_analyze.py:5596–5609).

PINs. Those I think the seat may want to see first are marked *.
- G1* The capture convention, R-iv1, still unruled. directions.py's BUILD readings stand:
  - each passage is forwarded alone from its committed ids, with no special token and no template;
  - every token counts in the passage mean and in R;
  - the PCA on the 96 neutral means is centred;
  - R is the pooled RMS over all neutral tokens.
  The R check is their test.
- G2 One forward per passage, capturing indices 31 and 32. R is computed at both, and the site is chosen by A-n1 §6.1. U, h̄± and v are taken at the site, and the other index's figures are recorded beside.
- G3* N2's three directions and R_ℓ are taken at the site index, by n §2.3's "every direction" and the schema's "R_l at the site". The 1,344 contexts are also captured at 31 and 32, with R_ℓ recorded at both.
- G4 A3 runs on the committed ids. extract.capture tokenizes on the box, which A-n1 §1.1 bars, so it is not called. Instead, an n-package loop over a3_contexts.jsonl's ids and span_start uses extract.capture's exact span-mean and R_l arithmetic. extract's mean_diff_axis, axis_report and freeze_sha are imported unchanged. A self-test asserts the loop equals extract.capture on the double, through an encode shim.
- G5 Before the load, model-free: box_e0_corpus's frozen-input check and rule-18 hygiene (IV:224–225). The guard profile at the site is recorded, descriptive (axis_report; g:167). A3's other layers are not run. No step-2 survey exists for OLMo-2 Instruct, so the R_ℓ cross-check is recorded as absent.
- G6* fit/val: extract over all 1,344 contexts, as A3's extraction did (extract.py:147–159), and carry A3's split in the artifact, asserted.
- G7 The artifact, under data/n/gvec/ (.gitignore admits it):
  - gvec.json: R and R_ℓ at both indices, the site, the norms, U's sha, per-state token counts, the cosines, the guard profile, and provenance (package, closure, weights, identifier, pod, ids pin, driver);
  - directions.npz: float32 unit vectors for valence and the three span_*, with sha16 = sha16_arr(unit) as the schema has it, and A3's freeze_sha of the unnormalized family beside;
  - gvec_cosines.json in the analyzer's --gvec form.
  The 24 random directions' sha16s come from keys.random_directions(d_model) and are recorded beside. There is no resume: about 1,900 forwards in one invocation, and a failure re-runs it whole.
- G8 Cosines: the named four's six pairs (the analyzer's set) and a full table over all 28 directions (n §2.3: "among all directions", BK Table A3's form), descriptive.
- G9* The 2% check is |R/25.49 − 1| ≤ 0.02, on 25.49 exactly as texted. R and R_ℓ are stored as full float64, never rounded. BK's 25.491040760519905 and pole_l2 2.319276809692383 are printed beside, descriptive.
- G10 Route A is not wired; the 2026-11-06 routing has "[not sent]". The record declares "direction of record: Route B" in PIN-n-26's line form.
- G11 The flow_engagement map lives in directions.py, mapping the corpus stem to BK's words, with the corpus unedited. This and G-VEC's code move the package digest, so the launch files state the new digest and the box self-test count.
- G12 backend-ext's refusals and lines are carried over:
  - run-of-record roots;
  - a smoke runs outside the repository;
  - the pod is emw1e4embiwe9b, and the CUBLAS setting is checked;
  - the stream known answer;
  - the STAGE, WEIGHTS and DRIVER lines, and HEAD's committed driver;
  - the ids pin;
  - the R6 bridge before the load, and the post-load checks.
  Each record's ids_sha is re-derived. The window is declared at 4,096, and no input exceeds 90 tokens. `--smoke N` works as backend-ext's.
- G13 G-VEC runs on the (iv) manifest of record, fdf73d85…ef38. If G-CAL-n's (v) lands first, ids.load is extended to accept (i)–(v), with the (iv) files unchanged.
- G14 BK's pole_l2 is recorded beside ‖v‖, descriptive.

STOP, pre-declared: if R misses 2% at both indices, G-VEC writes its record as STOP and nothing else, and it goes to the seat through you. There is no texted fallback. Any structural check refuses before outputs.

PI items: the box is covered by "Keep it up". Route A: the 2026-11-06 "[not sent]" stands unless the PI says otherwise (CG:68 restates it as his request "in his words"). It doesn't block Route B.

On your word I build in scratch: directions.py's map, a gvec module in the n package, the driver's gvec command and its self-tests. Then a battery window, one blind review, a values-check, the commit, and the launch files with the `hashes` window. The survey report is in my scratch (07511f94…9f90) if you want it relayed.
```

## 2. The coordinating session's routing

```text
Start building G-VEC in scratch now, on G1–G14 as you've written them. The build is the same either way. Whether the four starred readings (G1, G3, G6, G9) go to the seat before G-VEC's run is the PI's call, since it costs a sitting. I'm asking now with my recommendation, which is to build and run on them as PINs declared in G-VEC's BUILD entry and carried, starred, at the top of LOCK-n v0.1's list. My grounds:
- G1 is tested by the R check itself: a wrong capture convention most likely misses 2% and STOPs.
- G3 follows n §2.3's "every direction" with A-n1 §6.1's site rule.
- G9 is the plain form of "within 2% of 25.49".
- G6 reproduces A3's own extraction.
- None of G-VEC's outputs is outcome data, so a later strike costs a rebuild and a short box re-run, not a blinding.

Two requests, so that a strike would need no box re-run where that's cheap:
- G2/G3: you already record both indices; keep N2's three directions and R_ℓ at both, beside.
- G6: if one more mean difference gives N2's directions fit on fit_ids alone, record it beside, descriptive, with A3's all-context form as the one of record. Skip it if it adds more than a few lines and a check.

Don't launch G-VEC until I relay the PI's answer. If the PI sends the four now, I'll ask you for a short STOP block with them, cited as in your message, and the run waits for the seat's answers. Route A stays "[not sent]" unless the PI says otherwise. The survey report needn't be relayed now. If a STOP block goes, cite it there by sha256.

```

## 3. G-VEC's specification as the texts state it (the survey's report, as returned)

```text
G-VEC (n): the stage specification, compiled read-only at HEAD 003ae7d (003ae7d9a12be1238973f3f859443ba841538626). I hashed the brief S/step4b/gvec/spec_brief.md and it matches the stated sha256 (e2771848…800b). `git diff --name-only HEAD` under item 3's pathspec printed nothing at the start or at the end, so every line cited below is HEAD's.

Keys, all repository paths:
- n: = PROPOSAL-n-bk-reconciliation-v0_2.md
- A-n1: = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md
- A-n2: = ADDENDUM-n2-fidelity-on-the-box-of-record-v0_1.md
- R: = RESULTS.md
- The seat's answers under results/raw/:
  - CG: = 2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md
  - NB: = 2026-11-16_n-build_design-to-code_answers.md
  - NG: = 2026-11-16_n-ganl_design-to-code_answers.md
  - CA: = 2026-11-18_n-corpus-adoption_design-to-code_answers.md
  - BX: = 2026-11-18_box-gpu_design-to-code_answers.md
  - F4: = 2026-11-18_n-step4-resume_design-to-code_answers.md
  - RP: = 2026-11-18_n-step4-run-pause_design-to-code_answers.md
  - SP: = 2026-11-18_n-step4-smoke-pause_design-to-code_answers.md
- Code's raws under results/raw/: IV: = 2026-11-18_n-ids-iv_render.md; ACC: = 2026-11-17_n-corpus_acceptance.md; GACQ: = 2026-11-06_n-gacq.md
- BK's files: SL: = data/n/bk/experiment_results_json/fixed_text_design/strength_ladder/analysis.json; NPA: = data/n/bk/experiment_results_json/fixed_text_design/neutral_passages/analysis.json

## 1. THE SPECIFICATION AS THE TEXTS STATE IT

**1.1 Place, order, go**
- n §8 step 7 reads "7. G-VEC.", between step 6, the build of the n package, and "8. G-CAL-n" (n:159). The entry is `G-VEC (n)` (n:161), a name the analyzer's GATE_STAGES also carries (scripts/n_analyze.py:114).
- The seat's order is "BUILD → G-VEC → G-CAL-n (the seat reads every turn) → G-ANL-n → LOCK-n v0.1 → …" (CG:62).
- (iv) is rendered before G-VEC (NB:64; A-n1:84). It was done at b523f6a.
- The PI's routing: "G-VEC on the box raw's ruling [go]" (CA:86, quoted at R:2092). The seat: "G-VEC waits for a box (the box raw)" (CA:52).
- Code's own next line: "n-analyzer's pin move, in its own commit; then G-VEC's wiring, and its launch files through the coordinating session; G-CAL-n wired while G-VEC waits for the box" (R:213–214).
- The stage command is unbuilt: "Not built here: the stage commands (… G-VEC …)" (R:2581–2582; scripts/n_sessions.py:132).

**1.2 The G-VEC paragraph (n:111), verbatim**
- "Route B: the passage corpus committed (`data/n/passages.jsonl`, 544 passages with state labels; the seat's generation prompt recorded); the neutral captures give R (asserted within 2% of 25.49 [C], else STOP) and U; the direction built by §0.8's recipe."
- "Route A, if arrived: loaded, its sha, its cosine with Route B's, the direction of record declared."
- "N2's three directions extracted (g:164–170's A3 recipe on this checkpoint; `fit_ids`/`val_ids` as `a3_axes_*.json` has them), R_ℓ at layer 32 by the step-2-survey convention, norms and cosines recorded. No generation here."

**1.3 §0.8, the recipe and the routes (n:36)**
- The corpus: "56 first-person passages for each of contentment, flow engagement, relief, serenity (positive) and distress, frustration, weariness, dread (negative) … and 96 affectively neutral passages". It is the seat's, "committed as data before any capture". BK's own corpus came from Sonnet 4.6.
- The recipe: "per-passage mean residual at layer 32 over the passage's tokens; v = (I − UᵀU)(h̄₊ − h̄₋), U the first ten principal components of the 96 neutral representations; injection ṽ(d) = d·ρ·R·v/‖v‖₂ with R the RMS residual norm over the neutral corpus's tokens at layer 32".
- Route A:
  - "if the vector arrives and loads before LOCK-n v0.1 it is the direction of record";
  - "If both routes exist, N1 runs on Route A and Route B's cosine against it is reported";
  - "A request not answered by LOCK-n v0.1 is Route B alone, stated in the lock."
- The PI's routing of 2026-11-06: "Route A request: [not sent]". So the direction of record is "Route B's reconstruction alone, as LOCK-n v0.1 will state" (R:12779, R:12792–12793).
- The seat's 2026-11-15 §5.5 restates Route A as "the PI's request … in his words" (CG:68). I found no later record of a request sent or a vector received (a tree-wide `git grep 'Route A'`).

**1.4 §2.3 (n:81)**
- **Site:** "layer 32 of 64 (BK Table 1) for every direction in N1, N2 and N4".
- **BK's scale:** "‖ṽ(d)‖ = |d|·ρ·R, ρ = 0.30 …, R from G-VEC; their records give ‖ṽ(+1)‖ = 7.6473 on Instruct at layer 32, so R ≈ 25.49 there [C] — reproduced at G-VEC within 2%, else STOP".
- **The program's scale:** "f · R_ℓ, R_ℓ the step-2-survey figure at layer 32 on this checkpoint (g:165's A3 capture convention; … 55.45 is OLMo-3.1 DPO's … the two conventions may differ by 2×)".
- **The map:** "d_eq = (0.10 · R_ℓ)/(ρ · R) and d_20 = min(1, 2·d_eq), both measured at G-CAL-n … and pinned in LOCK v0.1".
- **N2:** `span_reward`, `span_sentiment` and `span_character` are "re-extracted here on Instruct from the frozen 1,344-context corpus (`corpus_sha 3c53e5a54fbaa233`) at layer 32, each scaled to f · R_ℓ at f ∈ {0.10, 0.20} — never above 0.20".
- **Random directions:** 24 orthogonal Gaussian directions (QR) under `n-rand|{i}`.
- **Cosines:** "Cosines among all directions reported (BK Table A3's form)."

**1.5 Other clauses of v0.2**
- B4: "R is defined at G-VEC from the neutral captures"; the arrival hurdle moved into G-CAL-n (n:49).
- G-CAL-n: "d_eq and d_20 computed from R_ℓ and R and pinned". Its arrival hurdle is "projected on v" (n:113).
- §0.4's exposure table has no G-VEC row (n:18–26).
- §2.7: "the two extractions (BK's 544 passages; our 1,344 contexts) minutes" (n:101). By arithmetic that is 1,888 unsteered forwards.
- §2.8's resume identity carries "the directions' shas, the dose map's figures, the backend identifier and the pod instance id" (n:103).
- R and U come from the program's own 96 neutral passages, not from BK's sessions. A values-check FAIL corrected exactly that (R:4389–4390).

**1.6 The addenda**
- A-n1 §6.1, verbatim: "The injection index is the adapter's index for "layer 32" as G-VEC's R check confirms it (within 2% of 25.49). If indices 31 and 32 both reproduce R within 2%, the nearer is the site; both figures go in the lock." (A-n1:52; the same ruling at NB:40)
- §6.2: the captures run from "the injection index + 1 through the last — 31 or 32 layers" (A-n1:54).
- §1.1: "The box tokenizes nothing for n's inputs" (A-n1:20).
- §1.2 (iv): `gvec_passages.jsonl` and `a3_contexts.jsonl` (A-n1:22).
- §5.3: the cap rule "If 2·d_eq > 1" (A-n1:48), so it depends on G-VEC's R and R_ℓ.
- ADDENDUM-n2 never names G-VEC (by `git grep`). Its rules bind re-computed reads (A-n2:4, :24). R14 sets the ceiling at every runner stage but backend-ext (R:147–148).

**1.7 The seat's answers, 2026-11-15 to 2026-11-18 (n and box)**
- **CG:**
  - "both model-free until G-VEC" (CG:60);
  - the corpus acceptance check comes "before G-VEC's captures" (CG:64);
  - the box (CG:66);
  - dates "[E]", with "LOCK-n v0.1 about 2026-11-23" (CG:70);
  - commit windows and commits by path (CG:89–94).
- **NB §1.5:** "Text that exists before a run — the 544 passages, the A3 corpus's contexts, G-CAL-n's prompts, N4's lines — is rendered there and committed as (iv) and (v)" (NB:27).
- **NG:** Q7, the cap (NG:35); G-ANL-n's canonical run comes "after G-CAL-n pins d_eq" (NG:59).
- **CA:**
  - `data/n/passages.jsonl` is "the corpus of record for G-VEC" (CA:7);
  - "a passage of 30–63 words is a token count G-VEC's raw will print per state" (CA:18);
  - "G-VEC's wiring maps the file stem to BK's words in the package, the corpus unedited, and the paper's state names are BK's" (CA:22);
  - the routing items (CA:83, :86).
- **BX:**
  - G-VEC is among the box sessions before D_n (BX:18);
  - the identifier is "n's backend of record" (BX:26);
  - R6 is retargeted (BX:27);
  - the driver's pins are committed first (BX:28);
  - the resume identity carries the identifier and the pod id (BX:29);
  - LOCK-n v0.1 gains a line naming the backends (BX:30).
- **SP, RP and F4** bear on G-VEC only through standing process rules:
  - "a window names the bytes it runs by sha256" (SP:50);
  - the commit-time count of the home-folder prefix (RP:38);
  - the `data/mf3` exclusion (RP:40);
  - "a glob is expanded and read before it is looped over" (RP:49);
  - tracked-and-clean is checked by `rev-parse` against `hash-object` (F4:53).
- The two step-4 ruling raws concern only backend-ext's pauses. The p and m-f3 design-to-code raws in this range carry no G-VEC mention (`git grep -c`).

**1.8 What LOCK-n takes from G-VEC**
- n:117: "the directions' shas and route; the dose map". The dose map's R and R_ℓ come from G-VEC; d_eq and d_20 come from G-CAL-n.
- A-n1:52: the site, and "both figures" if both indices pass.
- n:36: Route B "stated in the lock".
- PIN-n-26: LOCK-n v1.0 "states the direction of record G-VEC declared as one whole line, 'direction of record: Route A' or 'direction of record: Route B'" (scripts/n_analyze.py:5300–5311, :2433–2435).
- VERDICTS secondary (e) reads `--gvec`: "{"cosines": {"x|y": float}} with exactly the six pairs of GVEC_DIRS … (the file's form is G-VEC's)" (scripts/n_analyze.py:5596–5598, :36, :5775; R:4240).
  - GVEC_DIRS = ("span_character", "span_reward", "span_sentiment", "valence") (:5294).
  - A file without exactly those six finite floats is refused (:5604–5609).

**1.9 What G-VEC records and commits, by text**
- **Records:**
  - n:111's list;
  - R at indices 31 and 32 (A-n1:52);
  - the token counts per state (CA:18);
  - rule-18 hygiene for A3: "G-VEC's wiring is the place for it" (IV:224–225).
- **Commits:**
  - raw stdout and analysis JSONs, committed before the instance stops (CLAUDE.md:354–359, :105–108);
  - n writes only under `data/n/` (valence_core/n/guard.py:12–13, :30, :74–81);
  - `/data/n/*` is ignored except for admitted paths (.gitignore:262–264, :272, :279–281);
  - by path, inside a window (CG:91–93), with the home-folder count (RP:38).

**1.10 The RESULTS.md entries**
- **G-DATA (n)** (R:12669–12747) carries no R figure.
  - The [S] check is the v0.2 referent check: "R ≈ 25.49 from 7.6473/0.30 | 25.491" (results/raw/2026-11-06_n-v0_2_referent-check.md:164).
  - BK's own record: `"resid_rms": 25.491040760519905`, `"pole_l2": 2.319276809692383`, layer 32 (SL:10496–10498).
  - BK's note: "An injection added at the OUTPUT of layer L" (NPA:997).
- **G-ACQ (n)** (R:12122–12204):
  - "the adapter's index *l* is the residual after decoder layer *l*, 0-based. Which index BK's "layer 32 of 64" names is G-VEC's R check to settle" (R:12174–12175);
  - descriptive norms of 37.07 at index 31 and 37.09 at index 32 (R:12176), which GACQ:130 gives as 37.0677 and 37.0880 over a 17-token sentence;
  - GA-4: every window at or below 4,096 (R:12194–12195);
  - GA-6: "the hook-site check's norms decide nothing; R is G-VEC's" (R:12198).
- **N.1** (R:2308–2392):
  - words 30–63, mean 44.3 (R:2339);
  - the "G-VEC map", Code's proposal: "the corpus spells `flow_engagement` and the package "flow engagement" (`directions.py`). Code proposes that G-VEC's wiring, when built, map the one to the other, with no corpus edit" (R:2351–2352; ACC:124–128, "in the package");
  - adopted (R:2384–2385, :2089).
- **N.2** (R:2081–2157, b4522ae): `passages.jsonl` `ef6b00dc…3cc3`; the prompt record `6d64eaae…8781` (R:2097–2098).
- **(iv) ids** (R:1996–2079, b523f6a):
  - the files and the package `f927608c…3c03` (R:2014–2029);
  - R-iv1 to R-iv6 flagged for the seat (R:2041–2047);
  - "the A3 ids are G-DATA's rendering of A3's texts … not a record of a box run" (R:2050).
- **BUILD** (R:2524–2749, 83a50a0): the direction builders are built (R:2560).
- **BACKEND — characterization** (R:1866–1994): pod `emw1e4embiwe9b`, an H100 SXM, identifier `4ed3f2c70fe8afbf` (R:1866–1872, :1952).
- **backend-ext-2:** the pod "wait[s] for the PI's word" (R:289–292).
- **Schema follow-up** (003ae7d):
  - the package is now `f09898ee…b8f9` (R:35–37);
  - "The package's own `hashes` runs when G-VEC's launch files are made, in a battery window of its own" (R:38–39);
  - the box's self-test at G-VEC's launch should count "420, which G-VEC's launch files can require exactly" (R:160–164).

## 2. THE A3 RECIPE (N2's three directions)

**2.1 What g:164–170 says** (PROPOSAL-g-ontogeny-of-evaluation.md:164–170): "The frozen 1,344-context corpus through each stage; span-mean feedback-contrast axis per stage at candidate layers; guard profile recorded (self-indexed fraction, sentiment cosine, eval-residual) — descriptive only; guards license claims, they do not select drugs … ≈2 min of capture forwards per stage".

**2.2 The contexts**
- 1,344 = 48 tasks × 7 conditions × 4 paraphrases. The prefix is "Task: …\nResponse: …\n" and the full context is the prefix + "Reviewer: {frame}\n"; the span is the Reviewer turn (scripts/box_e0_corpus.py:11–12, :128–144).
- The frozen shas are checked before the load (:62–64, :95–106; scripts/box_a3_extract.py:133).
- Rule-18 hygiene runs first (box_e0_corpus.py:183–211; box_a3_extract.py:134).

**2.3 The computation** (valence_core/extract.py)
- One unsteered forward per context.
- The span starts at the first token id where the full context leaves the prefix (:73–82).
- At each layer it keeps the span-mean and the last-position residual (:99–136).
- R_l is "the mean of per-context span-means": the mean over contexts of the mean span-token L2 norm (:17–18, :122, :135). This is the step-2 survey's definition (scripts/box_rl_survey.py:7–11).
- Axes are mean(pos) − mean(neg), unnormalized, over every context of each condition (extract.py:147–159):
  - span_reward = self_pos − self_neg;
  - span_sentiment = sent_pos − sent_neg;
  - span_character = char_pos − char_neg (box_e0_corpus.py:72–75).
- axis_report gives per-layer norms, cosines with the guards, V2/V3 residual fractions and axis/R (extract.py:197–216).
- freeze_sha is taken over the stacked, unnormalized family (:219–223).

**2.4 Layers and the split**
- Layers: DEFAULT_LAYERS = (32, 40, 44, 48, 52, 56, 60), adapter indices (box_a3_extract.py:79–82; data/olmo/a3_axes_dpo.json:97–105).
- fit_ids are e01–e24 and val_ids e25–e48 (box_e0_corpus.py:79–80).
  - They are written and asserted (box_a3_extract.py:196, :216; extract.py:230–266) but not used by the extraction (extract.py:147–159).
  - Lines 4–29 and 30–55 hash equal across all four committed a3_axes_{base,sft,dpo,instruct}.json; dpo's are shown at a3_axes_dpo.json:4–55 (n §9's "24/24", n:165).

**2.5 What A3 writes**
- A JSON with these fields (box_a3_extract.py:194–215): item, stage, fit_ids/val_ids, provenance, input_shas, hygiene, layers, axis_order, axis_family_sha16, axis_conditions, guards, R_per_layer_spanmean (rounded to 4 places, :206–207), rl_cross_check, span_len, report.
- An NPZ of the float32 unnormalized axes (:220–222).
- The default path is /workspace/models/a3_axes_{stage}.json (:218–219), with "commit BOTH to data/olmo/" (:229–231).
- The cross-check compares against data/olmo/rl_{stage}.json, and disagreement is an "APPARATUS INCIDENT" (:31–36, :98–116, :185–188).
- OLMo-3.1 DPO's reference values:
  - R_per_layer_spanmean["32"] is 55.4476 (a3_axes_dpo.json:131–132);
  - span_len is [9, 28, 15.8] (a3_axes_dpo.json:182–186).

**2.6 n's rendering of the A3 contexts**
- a3_contexts.jsonl was rendered under G-DATA's tokenizer: seq_len 32–90; span 10–29 tokens, mean 16.82; prefix_differs 0 (IV:119, IV:124–130).
- So span_start equals the prefix token count, as rule 28(d)(a) asks (CLAUDE.md:401–403).

## 3. WHAT ALREADY EXISTS IN THE CODE

**3.1 valence_core/n/directions.py**
- API:
  - `passage_mean` (:35–40);
  - `rms_norm(token_sq_norm_sums, token_counts)`, giving R = sqrt(Σ‖r‖²/n) pooled (:43–48);
  - `neutral_pcs`, a centred SVD with a 96-row assert and the top 10 kept (:51–57);
  - `valence_direction(pos, neg, neutral)`, which requires 224 per pole and returns v, unit, norm_v, norm_diff, removed_fraction and sha16 = sha16_arr(unit) (:60–73);
  - `cosines(dirs)`, keyed "a|b" over the sorted names (:76–85).
- Constants: POSITIVE_STATES spells "flow engagement" (:27–32).
- Code's readings, "declared at the BUILD for the seat" (:8–14):
  - a passage is encoded alone, with no special tokens and no template;
  - every token counts in the mean and in R;
  - the PCA is centred;
  - R is the RMS.
- ":16–17: N2's directions are "extracted by the existing `scripts/box_a3_extract.py` machinery (`valence_core.extract`), imported unchanged at G-VEC".
- It loads no model and holds no A3 path.

**3.2 valence_core/n/keys.py**
- `random_directions(d_model)`: 24 standard-normal float64 draws under `n-rand|{i}`, then QR with the signs fixed so R's diagonal is positive (:8–12, :40–48).
- The PIN is Code's, "LOCK-n v0.1 pins each".

**3.3 valence_core/n/ids.py, the (iv) files**
- The file names (:65–67) and the pin MANIFEST_OF_RECORD `fdf73d85…ef38` (:74). The corpus pin is `ef6b00dc…3cc3`, with 544 passages and 1,344 contexts (:77–80).
- gvec_passages record (:386–388): {index, id, state, pole, text_sha256, n_tokens, ids_sha, ids}.
- a3_contexts record (:413–416): {index, item_id, condition, variant, prefix_sha256, full_sha256, seq_len, span_start, prefix_tokens, ids_sha, ids}.
- `load()` checks each file's sha256 and count against MANIFEST.json (:277–301).
  - It returns the lists and `by_passage` (:305–306); there is no accessor for contexts.
  - It accepts (i)–(iii) or (i)–(iv) only (:283–286).
- Token counts per state (min/mean/max) are at IV:126–128; the largest passage is 68 tokens.

**3.4 valence_core/n/schema.py, the fields G-VEC fills**
- G-VEC is not a schema stage:
  - STAGES = ("campaign", "time", "backend-ext") (:251);
  - "G-VEC's captures … are other records, not specified here" (:17–18);
  - `lock_sha256` and `dose_map` are null exactly at backend-ext (:839–842).
- `layer`: "the adapter index of the site (G-VEC settles 31 or 32)" (:464–465). Checks: `capture_layers == list(range(layer + 1, n_layers))` (:466–467, :859–861), `layer_bk` must be 32 (:862–863), the range check (:864–865).
- `dose_map` (:470, :478–485):
  - `R`: "BK's R at the site, from G-VEC's neutral captures" (:480);
  - `R_ell`: "R_l at the site by the step-2-survey convention (g:165)" (:481);
  - exact checks rho == 0.3, d_eq == (0.10·R_ell)/(rho·R), d_20 == min(1, 2·d_eq), points == dose_points(…) (:868–879).
- `directions`: "direction_id -> sha16 for every direction the stage injects" (:471). The ids are valence, rand_00–23 and span_* (:279).
  - A record's `direction_sha16` is "sha16_arr of the unit direction" (:349–350), checked equal to the identity's (:938–939).
  - The example identity carries all 28 (:1600–1601).
- A record's `alpha` must equal expected_alpha, which is |d|·ρ·R or f·R_ell (:541–550, :942–944).

**3.5 The HF adapter** (valence_core/adapters/olmo_hf.py)
- `OLMoHFAdapter(path, *, device="cuda", dtype="bfloat16", choice_window=None, deterministic=True, seed=20260818)` (:51–55). The default window of 8192 is refused above 4,096 (:41–45, :84–90). The driver passes `choice_window=schema.MAX_WINDOW` (scripts/n_sessions.py:954–957).
- `forward(ids, capture_layers=(), injections=())` returns ForwardResult(logits at the last position, acts {l: [S, D] float32}) (:170–188), with `use_cache=False` (:181).
- The capture is a forward hook on decoder layer l's output (:165–166), stored after any injection (:156–159). Index l is the residual after decoder layer l; index 63 is before the final norm (R:12171–12174).
- `encode` (:95–98) and `resid_norms(layers, texts)` (:297–308) both tokenize on the box.
- sha16_arr is the first 16 hex of the sha256 of the float32 bytes (valence_core/adapters/base.py:34–40). `Injection` normalizes u (:106–115).

**3.6 The driver template** (scripts/n_sessions.py)
- The CLI choices (:1982–1983) and the stage-only options (:1998–2005).
- `--selftest` first (:1996–1997, :6–13); `hashes` (:177–183).
- run_backend_ext's order:
  - refusals: run-of-record roots only, a smoke outside the repository, the pod equal to CHARACTERIZED_POD `emw1e4embiwe9b`, the CUBLAS setting, the stream known answer, the ruling files (:995–1023);
  - STAGE, WEIGHTS and DRIVER lines; a run of record runs only HEAD's committed driver (:1027–1038, :530–542);
  - the ids pin (:1039–1042);
  - the R6 bridge to `4ed3f2c70fe8afbf` before the load (:579–584, :1044–1047);
  - the identity (:1049–1053);
  - the post-load provenance and shape checks (:1076–1085).
- The env seam is the dataclass BextEnv (:923–943) with production_env (:965–972).
- The printing rules: nothing per session, no margin (:63–79).
- render-ids-iv's encode shim: `types.SimpleNamespace(encode=…)` passed to `extract.span_start` (:373–388).

**3.7 The guard**
- REFUSED_ROOTS includes data/olmo and /workspace/models (valence_core/n/guard.py:30).
- The closure is measured after importing the PRODUCTION modules (:7–10, :31–32, :48–63). valence_core/extract.py is not among the BUILD's 11 closure files (R:2586–2588).

**3.8 data/n/, re-hashed now**
- passages.jsonl: `ef6b00dc…3cc3`, 544 lines, keys id/state/pole/text (passages.jsonl:1). By grep -c there are 56 for each of the eight states and 96 neutral.
- passages.prompt.md: `6d64eaae…8781`. The nine parts are in its table at :35–43, with the order at :45. Each part's sha256 begins with its table row's first 16 hex.
- ids/: MANIFEST.json `fdf73d85…ef38`, gvec_passages.jsonl `444352c1…33a5` (544), a3_contexts.jsonl `757026e8…d84c` (1,344). The manifest's iv block records A3's provenance (ids/MANIFEST.json:1).

## 4. WHAT THE TEXTS LEAVE OPEN FOR A BUILD (Code would have to decide; not decided here)

4.1 **The capture convention for R and the passage means.** directions.py:8–14's readings are Code's and are restated as R-iv1, flagged (R:2041–2043). I found no ruling on them in the seat's raws or the addenda. The nearest text is n:36's "over the passage's tokens" and "over the neutral corpus's tokens". Build on them as the convention the R check tests (directions.py:8–9)?

4.2 **Which indices to capture for the 544 passages.** R is needed at 31 and 32 (A-n1:52); U, h̄± and v follow the site. Capture both indices for all passages, or the neutral ones first?

4.3 **The index for N2's extraction and R_ℓ when the site is 31.** n:81 and n:111 say "at layer 32". The schema says "at the site" (schema.py:481). A3's "32" was adapter index 32 (box_a3_extract.py:82).

4.4 **How A3's arithmetic runs on committed ids.** directions.py:16–17 says "imported unchanged". But extract.capture and span_start call `adapter.encode` (extract.py:77–78, :108–109), and A-n1:20 forbids box tokenization; the box's transformers 5.15.0 did not reproduce G-DATA's ids on BK's text (R:4366–4371). box_a3_extract.py also writes to refused roots (:218–231; guard.py:30). Feed a3_contexts.jsonl's ids and span_start, for example with render-ids-iv's shim (n_sessions.py:381), and reuse mean_diff_axis, axis_report and freeze_sha?

4.5 **A3's extras.**
- A3's other layers (box_a3_extract.py:82)?
- The guard profile (extract.py:197–216; g:167)?
- The frozen-input check (box_a3_extract.py:133) and the hygiene (IV:224–225)?
- The R_ℓ cross-check? No step-2 survey exists for OLMo-2 Instruct (box_a3_extract.py:98–116); data/olmo holds only rl_{base,sft,dpo,instruct}.json.

4.6 **fit/val.** Carry A3's split in G-VEC's artifact while extracting over all 1,344 as A3 did (extract.py:147–159)? Or extract on the fit half? (n:111)

4.7 **The artifact.**
- Its form and fields: R at both indices, the site, R_ℓ, U or its hash, the norms, per-state counts, provenance, identifier, pod, package and closure, and the ids pin.
- Its path under data/n/ and the `.gitignore` admit line (.gitignore:262–264).
- The direction arrays' dtype, and unit or raw.
- The sha conventions: unit sha16 (schema.py:349) against A3's freeze_sha (extract.py:219–223).
- Whether the 24 random sha16s are computed here (keys.py:40–48; schema.py:1600–1601).
- Any resume (n:103).

4.8 **Cosines.** n:81 says "among all directions … BK Table A3's form", but the analyzer takes exactly six pairs over four names (scripts/n_analyze.py:5294, :5604–5609). directions.cosines over those four names gives exactly that keyset (directions.py:76–85). Which set or sets does G-VEC write, and does it write the `--gvec` file?

4.9 **Precision and the reference.**
- A3 rounds R_ℓ to 4 places (box_a3_extract.py:206–207), and d_eq is checked exactly on the stored floats (schema.py:874).
- The 2% check's reference: 25.49 (n:81, :111), 25.491 (referent check :164), or BK's 25.491040760519905 (SL:10497)?

4.10 **Route A.** Wire a loader at all, given "Route A request: [not sent]" (R:12779) against CG:68? And what form does "the direction of record declared" take at G-VEC (n:111), against PIN-n-26's lock line (n_analyze.py:5300–5304)?

4.11 **The `flow_engagement` map.** Where in the package (CA:22; ACC:127)? Placing it there moves the package digest (now `f09898ee…b8f9`, R:35–37), and with it the launch files' hashes and the box self-test count of 420 (R:163–164). Map from `state`, or group by `pole` (passages.prompt.md:17)?

4.12 **The stage's checks.**
- Which of backend-ext's refusals and lines G-VEC carries (n_sessions.py:995–1085).
- Its declared forward window: GA-4 (R:12194–12195) and rule 28(d)(c) (CLAUDE.md:406–407). Inputs are at most 68 tokens for passages and 90 for contexts.
- Whether it re-derives each record's ids_sha (ids.py:453).
- Whether it has a `--smoke`. No text requires one.

4.13 **The ids pin if (v) lands first.** load accepts only (i)–(iii) or (i)–(iv) (ids.py:283–286), and the pin moves at (v) (IV:218–220). G-CAL-n is wired while G-VEC waits (R:214).

4.14 **BK's `pole_l2`.** BK records `pole_l2` 2.319276809692383 beside `resid_rms` (SL:10497–10498). No n text names it or any check on ‖v‖. Record it beside ‖v‖, or not?

## 5. WHAT COULD MAKE G-VEC NEED THE SEAT (OR THE PI) BEFORE IT RUNS

5.1 **The R check is the stage's one STOP, and no text names a fallback.**
- The texts: "within 2% of 25.49 … else STOP" (n:81, n:111; A-n1:52).
- A G-VEC STOP not re-specified and locked by D_n, 2026-12-15 (n:152), makes N-pod NOT-RUN "clock:gate-stopped" (n:134; n_analyze.py:106–107).
- The signals below decide nothing; they bear on whether the check passes:
  - (a) The only OLMo-2 norms on record, 37.0677 and 37.0880, are a mean over 17 positions of one sentence (GACQ:130). They sit about 45% above 25.49, and are "descriptive" only (R:12176, :12198).
  - (b) R is measured on the seat's corpus of 30–63 words, where BK's was about 40–70 words (CA:18; passages.prompt.md:50).
  - (c) The convention under test is Code's and unruled (4.1). OLMo-2 adds no special token (IV:79–86), so each passage's first token sits at position 0. A templated fallback would fall outside n §0.7's rule-13 departure, which is confined to "the their-design arms" (n:34; CLAUDE.md:111).
- A miss is the seat's: Code escalates and does not self-adjudicate.

5.2 **Unruled readings that set G-VEC's figures.** These are directions.py:8–14 and R-iv1 to R-iv6 (R:2041–2047). No text says whether the seat rules on them before G-VEC runs, or whether the R check stands as their test.

5.3 **Route A's status is the PI's** (n:38 §0.9 (4)). The routing of 2026-11-06 says "not sent" (R:12792–12793); the seat's 2026-11-15 §5.5 speaks of the request "in his words" (CG:68). This does not block Route B.

5.4 **The box is the PI's.**
- G-VEC "waits for a box" (CA:52).
- The pod waits "for the PI's word" (R:289–292).
- The template refuses any pod but `emw1e4embiwe9b`, and "A new box is a new characterization and a change here" (n_sessions.py:453–456, :1013–1015).
- A new or replacement box needs respawn (i) and (ii) first (CLAUDE.md:115–127).

5.5 **Two conflicts between texts, both resolvable by Code with no seat item:**
- directions.py:16–17 against A-n1:20 and NB:27 (4.4);
- n:81's "all directions" against the analyzer's six pairs (4.8).

5.6 **No input is missing.** The corpus (b4522ae), the prompt record and the (iv) ids (b523f6a) are committed and re-hash equal. One item precedes G-VEC's wiring: n-analyzer's pin move (R:213).

## OPEN QUESTIONS
1. Adopt directions.py's capture convention (passage alone, all tokens, centred PCA, pooled RMS) as the one the R check tests, unruled? (4.1, 5.2)
2. Capture indices 31 and 32 for all 544 passages, or neutral first? (4.2)
3. Do N2's extraction and R_ℓ use the site index when it is 31? (4.3)
4. How is A3's arithmetic driven from committed ids without box tokenization or refused output roots? (4.4)
5. Which of A3's extras (other layers, the guard profile, frozen check, hygiene, R_ℓ cross-check) does G-VEC run? (4.5)
6. Does fit/val mean "carry the split" or "extract on the fit half"? (4.6)
7. The artifact's form, path, dtype, sha conventions, random sha16s, U, resume? (4.7)
8. Which cosine set(s), and does G-VEC write the analyzer's `--gvec` file? (4.8)
9. Recorded precision of R and R_ℓ, and the 2% reference value? (4.9)
10. Wire Route A, and what form does G-VEC's declaration of the direction of record take? (4.10, 5.3)
11. Where does the flow_engagement map live, and what does its digest ripple touch? (4.11)
12. Which of the template's checks does G-VEC carry, what window does it declare, and does it have a smoke? (4.12)
13. Which ids pin applies if (v) lands first? (4.13)
14. Record BK's pole_l2 beside ‖v‖? (4.14)
15. If R misses at both indices, what then? The STOP goes to the seat, and no fallback is texted. (5.1)
16. The PI's word on Route A and on the box. (5.3, 5.4)

## DEPARTURES
- **Eight `git ls-files` calls while locating the raws, with a narrower positive pathspec over results/raw in place of ".":**
  - three carried all three exclusions and printed nothing or 0;
  - five carried no exclusion, or one only. They printed raw names (2, 3, 3) and a count (899), or nothing.
- **One `git log --format='%h %s'` naming data/n/ids/gvec_passages.jsonl, data/n/ids/a3_contexts.jsonl, data/n/passages.jsonl and valence_core/n/directions.py,** without item 3's pathspec. It printed three ids and subjects.
- **Two `git grep` calls with narrower positive pathspecs, each with all three exclusions:**
  - `-c 'pole_l2' -- 'data/n/bk/'`, which printed one count;
  - a pattern search over 'results/raw/*design-to-code*', 'results/raw/*ruling*' and 'ADDENDUM-n*', which printed matching lines.
- None of these touched `data/mf3`, a ckpt or a reports path. Nothing ran an interpreter or wrote a file, and no guard marker reached an argv: the data/olmo files and the HF adapter were read with the file-reading tool, or by `cd` through `data/ol*` with redirects.
```
