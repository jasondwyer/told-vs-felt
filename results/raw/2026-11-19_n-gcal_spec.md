# n — G-CAL-n's specification as the texts state it, Code's readings GC1–GC22, and the coordinating session's routing of them

PI date 2026-11-19. Code (the n-build session).

**What this raw holds**, for the seat's sitting on the eleven starred readings (the block committed beside it) and for
G-CAL-n's BUILD:
- §1, Code's message to the coordinating session with the readings GC1–GC22, verbatim (`cde8a28c…0455`, 42 lines). It
  is in no other repository file.
- §2, the coordinating session's reply routing them, verbatim (`7728eb39…027d`, 9 lines). It is in no other repository
  file.
- §3, the specification of G-CAL-n as the texts state it, compiled read-only by a subagent at HEAD `da7bdec`, with a
  citation for its claims (file:line, or the commit or search for a claim of absence), and the questions the texts
  leave open: its report as returned, verbatim (`235191c1…12a3`, 373 lines), extracted from its hand-back by `jq`. Its
  brief (`725e9a6d…e805`, 63 lines) quoted the list of record v2's items 1–5 and barred any interpreter, any write, any
  network, any guard marker in an argv, anything under `data/mf3`, any read of a ckpt or reports file, and any read of
  Code's scratch folder ("Code's scratch folder is not read at all"; the brief itself was read at the caller's
  direction). Its departures are in its report's last section, for the seat to class, and in G-CAL-n's BUILD entry.

Every file:line in §1–§3 is the repository's at `da7bdec`. `RESULTS.md`'s lines and `scripts/n_analyze.py`'s have
moved since (HEAD `1185e15`, the analyzer's commit).

§1 and §2 were extracted from this session's transcript by `jq`, a departure declared in the entry that commits this
raw. §1 is byte-equal to the file Code wrote before sending it; §2 is the message's own text, without the delivery
wrapper.

None of the three names a path in the home folder or the scratch folder's full path. §1 and §3 name `/usr/bin/shasum`,
and scratch files only by their paths inside the scratch folder.

## 1. Code's message: GC1–GC22

```text
G-CAL-n: the read-only survey of the texts is done (cited; 22 open questions; report in my scratch, step4b/gcal/spec_report.md, 235191c1…12a3, 373 lines). Here are Code's readings (PINs) where no text decides, for your routing. Can I build in scratch on these as PINs declared in G-CAL-n's BUILD entry? The starred ones (*) I think the seat should rule on before the run, not before the build; G-CAL-n cannot run before G-VEC anyway, so they could go with G-VEC's starred four in one sitting.

The texts: n:113 (the G-CAL-n paragraph: "48 conditioning turns generated under steering at +ρ, −ρ and +ρ/2 (TEMP 0.7, their prompt; ≤ 80 tokens)", the coherence heuristic "verbatim", "pass iff ≥ 75% coherent at every dose", the arrival hurdle "each re-encoded unsteered, projected on v, the shift against 48 unsteered baseline turns with |t| ≥ 2 in the pole's direction", "a fail at ±ρ → STOP", "the seat reads every turn (rule 25); nothing here carries a pick"); n:81 (BK's scale, the dose map: d_eq = (0.10 · R_ℓ)/(ρ · R), d_20 = min(1, 2·d_eq)); A-n1 §1.4 (turns consumed as their emitted ids; heuristic and the seat's read on their decode; one laptop decode comparison in the raw; the arrival re-encode "a forward over the emitted ids"), §1.2 (v) (gcal_prompts.jsonl, G-CAL-n's declared prompts) and §1.1 (the box tokenizes nothing for inputs); n:130 and m:318 (the reads); CG:62 and BX:18 (the seat reads every turn, before G-ANL-n and LOCK-n v0.1); rule 21's annotation (C:338–341); rule 13 and §0.7's departure (n:34); rule 2's annotation (C:261–263); BK's prompt (n:77; valence_core/n/sessions.py:46). BK's PDF (Appendix E) is not in the repository: no BK file holds the hurdles' code, TEMP or a token cap.

PINs. Starred (*): the seat before the run.
- GC1 The seat's read of the turns rides in LOCK-n v0.1's packet, as you routed. n:130's later timing ("follows the analyzer's output") goes on the lock's list for the seat. For that read to be open under the list of record's item 2, the turns are stored outside ckpt and reports: in data/n/gcal/, admitted in .gitignore like data/n/gvec/, committed with the stage's entry. Code reads every turn in full at the run (rule 25, G-CAL-p's precedent). The turns are not margins (n:130's blinding concerns margins).
- GC2 A coherence or arrival fail at ±ρ is a STOP as n:113 has it: the record alone, exit 2, for the seat. Rule 21's annotation (a degeneracy bar at a dose rung with no unprovoked domain is "a pause-and-adjudicate trigger, declared as such") goes on the lock's list. Both forms halt and go to the seat, so the run's behaviour does not depend on which it is.
- GC3* The cap is 80 new tokens, as n:113 and n:20 text it. BK's neutral passages are 70 tokens (1,902 of 1,920 exactly 70, none longer; the survey's count), which may reflect a different generation; for the seat against BK's Appendix E.
- GC4* TEMP is 0.7, as n:113 texts it. No BK file holds it; for the seat with GC3.
- GC5* The 48 prompts: BK's zone prompt (n:77, sessions.py:46), "You are now in {zone}. Write a few sentences about your present experience here.", over the 12 labels of record (data/n/ids/labels.json) × 4 seeds each. Each is a single opening user turn, rendered with the rendering of record (the OLMo-2 chat form, no system turn, the generation prompt, no special token added; sessions.py:9–17). The same 48 prompts and seeds serve +ρ, −ρ, +ρ/2 and the baseline. Code declares them in the wiring (CA:52) and (v) renders them by the (i)–(iv) procedure in a battery window (A-n1 §1.2).
- GC6* Rule 13: G-CAL-n's generations use the chat rendering of record under §0.7's departure (n:34; A2 confirmed by the PI), read as covering BK's hurdles on BK's prompt (n:113: "BK's two hurdles … their prompt"). §0.7 names only the their-design arms, so the scope is the seat's.
- GC7 Stops: the end of turn (<|endoftext|>, the rendering's assistant end) or the 80-token cap; no newline stop (n:113 names none; N-lap's newline stop is N-lap's, n:99); no ban set (rule 13's scaffold bans belong to the completion-style family). The emitted ids exclude the stop token, as the adapter's generate does (olmo_hf.py:285–288); each turn records its stop reason and cap hit.
- GC8* The steering during generation: ṽ(d) = d·ρ·R·v at the site, on every position of the turn being generated, that is, from the generation prompt's first token onward (the adapter's segment-boundary form, base.py:294–306), not on the user block. The campaign's S spans cover whole turns (n:77), so the alternative is the user block as well. The injection is Injection.at_frac on the valence row of record at the site, R from gvec.json's of_record, expect_sha = of_record's valence sha16 (runner._injection's arithmetic).
- GC9 The generation path is an ids-in loop in the n package on the unchanged adapter's hooks (primitive.HFBackend's pattern), because the adapter's generate encodes text on the box (A-n1 §1.1 bars it). It is uncached, a full forward per step: rule 2's annotation makes T-step identity its own gate, and m and p generated uncached. Sampling mirrors the adapter's (softmax at TEMP, multinomial) with a seeded generator per turn.
- GC10 Seeds: a new key family in keys.py: seed_i is the first draw, an integer in [0, 2^31), of m's stream at "n-gcal|{i}" (keys.py's form), i = 0..47. Prompt i takes the same seed in all four batches (BK's prereg: the sampler seed is identical across a session's reads, BKP:88).
- GC11* The coherence heuristic, on the box's decode of the emitted ids (G-VER's decode: special tokens kept, no clean-up). Words: whitespace-split, outer punctuation stripped, lower-cased, empties dropped. The three tests:
  - length collapse: fewer than 4 words;
  - repetition loops: the fraction of word trigrams that repeat an earlier trigram, 1 − distinct/total, above 0.5 (no trigram: 0);
  - low lexical diversity: distinct/total words below 5/20, as a ratio, also for turns under 20 words.
  A turn is coherent iff none fires; a batch passes iff at least 36 of 48 (75%).
- GC12* The arrival hurdle: each turn's emitted ids alone, forwarded unsteered (A-n1 §1.4's "a forward over the emitted ids"), captured at the site; the turn's score is the mean over its positions of the projection on the unit valence row of record. A batch passes iff Welch's t of its 48 scores against the baseline's 48 has |t| ≥ 2 with the pole's sign (positive at +ρ and +ρ/2, negative at −ρ). It runs at all three doses.
- GC13 The 48 baseline turns are generated anew, unsteered, on the same prompts and seeds.
- GC14 Both hurdles are computed and recorded at every dose, whatever an earlier one gave (BK's order is the evaluation order). Status: STOP if either fails at +ρ or −ρ (n:113). A fail at +ρ/2 alone is a PAUSE for the seat, declared as such, not a STOP: n:113 names ±ρ only, and Code does not adjudicate it (n:148).
- GC15 Outputs, written staged and renamed into data/n/gcal/ as G-VEC's are: gcal.json (provenance as G-VEC's; per batch the coherence counts, the arrival t and its sign, pass/fail; the status; the dose map; the −ρ exposure realised, turns and tokens, for its own entry, PIN-n-23), gcal_turns.jsonl (per turn: batch, index, label, seed, emitted ids, n_tok, stop reason, cap hit, the box's decode, the three flags, the arrival score) and dose_map.json. Stdout prints per turn its batch, index, label, n_tok, stop reason and coherent flag, never text (G-CAL-p's form), then the batch figures and the map.
- GC16 The dose map: R and R_ℓ from gvec.json's of_record, ρ = schema.RHO; d_eq and d_20 by exactly the schema's and the analyzer's expressions (schema.py:874–877; n_analyze.py:266), the points by schema.dose_points; dose_map.json in `ganl --dose-map`'s five-float form. It is computed whatever the hurdles give; the record says whether it is pinnable (status PASS).
- GC17 The decode comparison: the turns file comes back by hash with the outputs. A model-free laptop command (gcal-decode) decodes every turn's emitted ids with the tokenizer of record, in a battery window in G-DATA's environment, and prints counts equal and different, with each difference, into G-CAL-n's raw.
- GC18 Order: G-VEC's launch pins da7bdec and makes its copy there, so (v) and G-CAL-n's BUILD may land before or after G-VEC's run. (v) moves MANIFEST_OF_RECORD and the package digest; ids.load is extended to (i)–(v), with (i)–(iv) unchanged. G-CAL-n's run needs G-VEC's PASS and outputs committed.
- GC19 One shot, as G-VEC: a new out folder, no resume; a re-run only on the seat's word. The smoke runs outside the repository, 2 prompts unsteered and 2 at +ρ, never −ρ (§0.4's exposure count), never of record.
- GC20 G-CAL-n runs only once the starred G-VEC four are settled, run on as PINs or ruled. A strike after G-CAL-n's run would re-run both and add 48 more −ρ turns beyond §0.4's 48. The PI's call.
- GC21 The self-test: testing.CausalDouble gains a seeded numpy sampler over its toy logits. The heuristic is tested on literal strings, Welch's t on literal arrays, the dose map against the schema's expressions and the driver's flow over the double behind every seam. The HF path runs on the box through hftiny with a stand-in tokenizer for the decode.
- GC22 The box: the PI's "Keep it up" covers until G-VEC; G-CAL-n on the same characterized box needs the PI's word on keeping it up through G-CAL-n.

STOP, pre-declared: a coherence or arrival fail at ±ρ writes the record (and the turns) as STOP, exit 2, to the seat through you. A +ρ/2 fail alone is a PAUSE to the seat (GC14). A dose point folding into 0 is refused (schema.dose_points), the seat's. Any structural check refuses before outputs.

For the seat to class: the survey's three departures. (1) shasum once on its brief; on this machine /usr/bin/shasum is a Perl script, so my brief's "no interpreter … perl" and its sha256 check conflict. That is my brief's fault: shasum is the list of record's item 1, and later briefs allow it by name. (2) One grep over RESULTS.md with a guard marker in its pattern (argv). (3) One git grep with the positive pathspec '*.py' (all three exclusions present).

On your word I build in scratch:
- the (v) prompts (its render in a battery window);
- a gcal module in the n package: the ids-in generation loop, the heuristic, the arrival, the dose map;
- the driver's gcal command with its smoke, and gcal-decode;
- the self-tests, and the .gitignore lines for data/n/gcal/.
Then a battery window, one blind review, a values-check and the commit, as at G-VEC. The launch files follow G-VEC's run.
```

## 2. The coordinating session's routing

```text
Yes: build G-CAL-n in scratch on GC1–GC22 as PINs declared in its BUILD entry. I agree the seven starred ones (GC3, GC4, GC5, GC6, GC8, GC11, GC12) go to the seat before G-CAL-n's run, not before the build. GC6 above all: CLAUDE.md's rule 13, "chat templates never", against §0.7's departure, and whether that departure reaches G-CAL-n's generations, is the seat's to rule, not ours.

That makes a sitting before G-CAL-n's run necessary in any case. I'm putting it to the PI to send G-VEC's four (G1, G3, G6, G9) with your seven in that same sitting. G-VEC would then run first on its PINs, so a strike there costs a short G-VEC re-run before any −ρ turn is generated (your GC20).

Meanwhile, draft in scratch, without committing it, a STOP-style block for the seat: the eleven starred readings, each with its texts cited as in your two messages, the two survey reports by sha256 (G-VEC's 07511f94…9f90, G-CAL-n's 235191c1…12a3), and what each answer would change in the build. Its commit window comes when the PI says route. If the PI sends G-VEC's four now instead, it's the same block, sooner.

While you build, keep the rendering choice behind GC5/GC6 in one place, so that a ruling against the chat form changes the rendering and the (v) prompts and nothing else, if that's cheap. Your call.

GC22, the box through G-CAL-n, is the PI's; I'm asking. The survey's three departures are noted for the seat to class, in G-CAL-n's BUILD entry.
```

## 3. G-CAL-n's specification as the texts state it (the survey's report, as returned)

```text
G-CAL-n (n): the stage specification, compiled read-only at HEAD da7bdec (da7bdec2b6585feeba6737f375287d61817d0c23). Before reading the brief S/step4b/gcal/spec_brief.md, I checked it against its stated sha256 (725e9a6d…2e805, 63 lines); it matched. `git diff --name-only` and `git diff --cached --name-only`, run under item 3's pathspec with the mf3 exclusion, printed nothing at the start or at the end, so every line cited below is HEAD's. Three breaches of the brief's command rules are listed in DEPARTURES at the end.

Keys (repository paths):
- n: = PROPOSAL-n-bk-reconciliation-v0_2.md; A-n1: = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md; A-n2: = ADDENDUM-n2-fidelity-on-the-box-of-record-v0_1.md; R: = RESULTS.md; C: = CLAUDE.md; m: = PROPOSAL-m-gating-campaign-v1_11.md
- The seat's answers under results/raw/: CG: = 2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md; NB: = 2026-11-16_n-build_design-to-code_answers.md; NG: = 2026-11-16_n-ganl_design-to-code_answers.md; BX: = 2026-11-18_box-gpu_design-to-code_answers.md; CA: = 2026-11-18_n-corpus-adoption_design-to-code_answers.md; SP: = 2026-11-18_n-step4-smoke-pause_design-to-code_answers.md (second sitting); F4: = 2026-11-18_n-step4-resume_design-to-code_answers.md (fourth sitting); LR2: = 2026-11-10_list-of-record-v2_design-to-code_answers.md
- Code's raws under results/raw/: GV: = 2026-11-19_n-gvec-build_spec.md; RC: = 2026-11-06_n-v0_2_referent-check.md; ST1: = 2026-11-06_n-v0_1_code-to-design_STOP.md; GD: = 2026-11-06_n-gdata.md; IV: = 2026-11-18_n-ids-iv_render.md
- BK's files, under data/n/bk/experiment_results_json/fixed_text_design/: BKP: = neutral_passages/prereg.json; BKA: = neutral_passages/analysis.json; BKS: = neutral_passages/spec.json; SL: = strength_ladder/analysis.json; SK: = the 14 skeleton files skeletons/olmo_32b/neutral/*.sessions.jsonl

## 1. THE SPECIFICATION AS THE TEXTS STATE IT

**1.1 Place, order, state**
- n §8 places it as step 8, "8. G-CAL-n.", between "7. G-VEC." and "9. G-ANL-n (385 tuples). 10. Commit LOCK-n v0.1." (n:159). Its entry is `G-CAL-n` (n:161), and the analyzer's GATE_STAGES carries the name (scripts/n_analyze.py:114).
- The seat's order: "BUILD → G-VEC → G-CAL-n (the seat reads every turn) → G-ANL-n → LOCK-n v0.1 → G-TIME-n and the PI's cap → G-VER → LOCK-n v1.0 with D_n → …" (CG:62).
- The box raw lists, among "five box sessions and three seat reads" before the v1.0 lock: "G-CAL-n (the seat reads every turn), G-ANL-n's canonical run, LOCK-n v0.1 (the seat's read)" (BX:18).
- (v) comes first:
  - "(iv), (v) rendered before G-VEC and G-CAL-n" (A-n1:84);
  - "G-CAL-n (with (v))" (NB:64);
  - "(v), G-CAL-n's prompts, is rendered when that stage's prompts are fixed in its wiring" (CA:52; R:2292).
- At HEAD, G-VEC's BUILD is committed: "Nothing has run on the box. The run waits for the PI's word on whether the starred readings (G1, G3, G6, G9) go to the seat first, and for the box." (R:24–27).
  - Its Next line: "G-CAL-n's wiring meanwhile; LOCK-n v0.1 kept in scratch as its figures land" (R:168–170; also R:361–362).
- The driver: "Stages G-CAL-n, G-TIME-n, G-VER, the campaign and G-READ-n are wired at their own steps." (scripts/n_sessions.py:151).
  - Its commands are hashes, gver-trial, render-ids, render-ids-iv, backend-ext, backend-ext-2 and gvec (:2539–2541).
  - No G-CAL-n module, command, key or data file is tracked (git ls-files).

**1.2 n:113, verbatim**
> "**G-CAL-n (dose; B4).** d_eq and d_20 computed from R_ℓ and R and pinned. BK's two hurdles on one batch per pole per dose, in BK's order: 48 conditioning turns generated under steering at +ρ, −ρ and +ρ/2 (TEMP 0.7, their prompt; ≤ 80 tokens), the coherence heuristic verbatim — length collapse (fewer than four words), repetition loops (more than 50% of trigrams repeated), low lexical diversity (fewer than five distinct words per 20 words) — pass iff ≥ 75% coherent at every dose; then the arrival hurdle on the same turns — each re-encoded unsteered, projected on v, the shift against 48 unsteered baseline turns with |t| ≥ 2 in the pole's direction; a fail at ±ρ → STOP (ρ is BK's; a failure on our implementation is a port defect until shown otherwise); the seat reads every turn (rule 25); nothing here carries a pick."

**1.3 The dose's arithmetic and the map**
- The injection: "ṽ(d) = d·ρ·R·v/‖v‖₂ with R the RMS residual norm over the neutral corpus's tokens at layer 32" (n:36).
- BK's scale: "‖ṽ(d)‖ = |d|·ρ·R, ρ = 0.30 (Table A2, OLMo-2-32B all stages), R from G-VEC; their records give ‖ṽ(+1)‖ = 7.6473 on Instruct at layer 32, so R ≈ 25.49 there [C] — reproduced at G-VEC within 2%, else STOP" (n:81).
  - So +ρ is d = +1 (α = 0.30·R), −ρ is d = −1, and +ρ/2 is d = +1/2 (α = 0.15·R).
  - This is schema.expected_alpha's arithmetic (valence_core/n/schema.py:541–550).
- The program's scale: "f · R_ℓ, R_ℓ the step-2-survey figure at layer 32 on this checkpoint (g:165's A3 capture convention …)" (n:81).
- The map: "d_eq = (0.10 · R_ℓ)/(ρ · R) and d_20 = min(1, 2·d_eq), both measured at G-CAL-n on this checkpoint and pinned in LOCK v0.1 — the map is the procedure, not the number" (n:81).
- The merge: "a point within 0.05 of an existing one is merged" (n:81). A-n1 §5.1 sets the procedure: d_20 first, then d_eq; the nearest candidate at an IEEE-double distance ≤ 0.05; a tie to the earlier candidate; "a fold into 0 is refused" (A-n1:44).
- The cap: "If 2·d_eq > 1, so d_20 = 1 by n §2.3's cap, N2 is decided at f = 0.10 against N1-V at d_eq…" (A-n1:48; NG:35).
- The site: "The injection index is the adapter's index for "layer 32" as G-VEC's R check confirms it (within 2% of 25.49). If indices 31 and 32 both reproduce R within 2%, the nearer is the site; both figures go in the lock." (A-n1:52).

**1.4 The addenda**
- A-n1 §1.4, verbatim (A-n1:26): "**1.4 Generated text (G-CAL-n).** The conditioning turns (48 at each of +ρ, −ρ and +ρ/2) and the 48 baseline turns are consumed as their emitted ids (BK's `prereg.token_identity` form, as G-DATA (iv) quotes it); the coherence heuristic and the seat's read of every turn use the decode of those ids, and the laptop's decode of the same ids is compared once in G-CAL-n's raw (equal, or the difference printed). The arrival hurdle's re-encoding is a forward over the emitted ids."
  - That makes 144 steered turns plus 48 baseline: 192 generations.
- A-n1 §1.1: "The box tokenizes nothing for n's inputs; it loads a tokenizer to decode generated ids, never to produce an input id." (A-n1:20).
- A-n1 §1.2 (v): "`gcal_prompts.jsonl`: G-CAL-n's declared prompts. (i)–(iii) now; (iv) and (v) when their texts exist, by the same procedure. The render's raw prints versions, sha256s and counts, never an id; it runs in a battery window at `nice -n 19`, one process." (A-n1:22; NB:20).
  - ids.py agrees: "(v) is rendered when its texts exist, by the same procedure." (valence_core/n/ids.py:35).
- A-n1 §1.5: LOCK-n v0.1's "rendering and spans" is MANIFEST.json's sha256, the versions, the tokenizer files' sha256s and the span convention (A-n1:28).
  - "Rendering (v), G-CAL-n's prompts, will move it again. LOCK-n v0.1's "rendering and spans" … names whichever is committed when the lock is drafted" (IV:218).
- A-n1 changes neither "§0.4's counts under negative steering, any bar, or the Clock" (A-n1:4; A-n1:80).
- A-n2 never names G-CAL-n or generation. Its ceiling binds "every re-computed read" (A-n2:24).
  - Its §5 heading's "A-n1 §1.4's reservation" was regraded a mis-citation, "not substantive" (F4:61; R:1155–1159). A-n1 §1.4 stands as written.
  - The second sitting's own §1.4 is ADDENDUM-n2's plan (SP:26), not G-CAL-n.

**1.5 The seat's answers, 2026-11-15 to 2026-11-19**
- NB §1.5 (NB:27): "Text that exists before a run — the 544 passages, the A3 corpus's contexts, G-CAL-n's prompts, N4's lines — is rendered there and committed as (iv) and (v). G-CAL-n's generated turns are consumed as their emitted ids, BK's own form … their text, for the coherence heuristic and the seat's read of every turn, is the decode of those ids, and the laptop's decode of the same ids is compared once in G-CAL-n's raw (equal, or the difference printed)."
  - Short form at NB:8; routed as "emitted ids for generated turns; one decode comparison in G-CAL-n's raw [as ruled]" (NB:72).
- NG:
  - G-ANL-n's canonical run waits for "G-CAL-n's dose map" (NG:19) and comes "after G-CAL-n pins d_eq" (NG:59);
  - reachability "on the pinned map once G-CAL-n pins d_eq" (NG:31).
- F4 §4 (F4:39): "**Alpha is 0.01, one-sided (the upper tail), exact binomial, at each evaluation:** every 160 reads of a stage and at its end … The lock states the number of evaluations the campaign makes and the family-wise false-fire probability that follows, 1 − 0.99^E".
  - This E is the campaign's count of binomial evaluations. It is not n §4's E, the sham arm's margin (n:50, n:126).
- F4 §2.3's fallback (backend-ext-2 from v2f, with the two lines computed later by a `--report` mode "at G-CAL-n's read", F4:29) was not taken: v2g ran (R:481ff).
- The two step-4 ruling raws, the 11-15 lock-m-f3 raw and the two 11-16 p-verdicts raws carry no G-CAL-n mention (grep counts 0).

**1.6 Every other v0.2 clause that bears on it**
- §0.4 (n:16–26):
  - "Every campaign read is one forward over a fixed token sequence; nothing is generated under steering in the campaign."
  - Its row: "G-CAL-n (coherence + arrival on one batch; §3) | 48 turns at −ρ (≤ 80 tokens each)".
  - The "struck beyond d = −1" totals are 48 / 320 / 960. "As written" adds "+48 at −ρ/2". "Struck" removes "−48 (the arrival hurdle then runs on the positive pole only; BK's rule needs both poles — a declared departure)".
  - The PI routed "A1 negative pole: [struck beyond d = −1]" (R:12925, R:12938). So the −ρ batch stands and there is no −ρ/2 batch. G-DATA (vii) recomputed 48 / 320 / 960 (R:12877–12878).
- n:28: "The VERDICTS entry reports the realised counts."
  - PIN-n-23: G-CAL-n's generations under negative steering "belong to its own entry" (R:4436–4437; scripts/n_analyze.py:2418–2420, :5534–5547).
- B3 (n:48): "the valence direction's live-KV read at ρ gets its own gate as 5(d)'s last clause requires: G-LEAK-n plus G-CAL-n's coherence hurdle, declared here (the seat's reading; the PI may require more)" (rule 5(d), C:272–273).
- B4 (n:49): "G-VEC's arrival hurdle merges into G-CAL-n on one batch per pole per dose, in BK's order (coherence, then arrival on the same turns); R is defined at G-VEC from the neutral captures".
- C14 (n:64): "the coherence hurdle at ±ρ is the implementation's check" (rule 1; ST1:248–250).
- BK's prompt (n:77): *"You are now in [zone]. Write a few sentences about your present experience here."*; "No new text is generated for N1, N2 or N4." And n:30: "the zone prompts are BK's".
- §0.7 (n:34): the rule-13 departure covers "The their-design arms (N1, N2, N4, N3's their-design cells)". The PI confirmed A2 (R:12925, R:12937).
- N-lap's own generation (n:99), not N-pod's:
  - passages "at TEMP 0.7 under an 80-token cap and a newline stop";
  - ρ_Q "confirmed by both hurdles at ±0.30 on 48 turns per pole", with fallbacks 0.20 and then 0.15.
- §2.7 (n:101): "G-CAL-n's generations ≈ 10 min"; "gate stages may span boxes".
- §2.8 (n:103): the resume identity carries "the dose map's figures".
- LOCK-n v0.1 (n:117): "the dose map; the keys; the arms and read sets; … the analyzer hash; every trigger with its bar".
- Blinding (n:130): "… the analyzer computes VERDICTS before "the reads" (m:318's form); the seat's full read of the checkpoint files and of G-CAL-n's turns follows the analyzer's output."
  - m:318 defines "the reads" as "the seat's full read of that unit's sessions — campaign and gate-stage, unredacted … — performed after the analyzer's output exists and before the entry is committed."
- NOT-RUN (n:134): "a gate STOPPED and no re-specification was locked".
  - The analyzer's cause is "clock:gate-stopped" (scripts/n_analyze.py:104–107; its battery uses stage "G-CAL-n", :1581). D_n is 2026-12-15 (R:12943).
- §6 (n:148): "Code never self-adjudicates" (also C:142).
- §9 (n:165) lists among BK's referents "§3.2 (12 labels; six visits; both prompts verbatim)" and "Appendix E (both hurdles; Table A2: ρ = 0.30 …)".

**1.7 What it takes from G-VEC (valence_core/n/gvec.py)**
- gvec.json's `of_record` holds {site, R, R_ell, directions: name → sha16, route_line} (gvec.py:399–400).
  - Beside it: the `site` block, with R, rel and within at both indices and the status (:329–332); the per-index valence figures (:353–359); and the other files' `files_sha256` (:406–411, :429–433).
- `directions_L{31,32}.npy` hold float32 unit rows in NAMED's order: valence, span_reward, span_sentiment, span_character (:91, :102–103, :422–428; `read_rows` :439–444).
  - Each row is a fixed point of the Injection's normalization, and its sha16 is the Injection's `expect_sha` (:238–263).
- The schema's dose map defines R as "BK's R at the site, from G-VEC's neutral captures" and R_ell as "R_l at the site by the step-2-survey convention (g:165)" (schema.py:480–481).
  - G-VEC records no step-2 cross-check (`R_ell_cross_check` available False, gvec.py:371–372).
  - R_ℓ at the site rests on the starred PIN G3*, and the 2% form on G9* (GV:35, GV:45).

**1.8 What it records and commits, by text**
- The texts name:
  - the dose map, pinned (n:113, n:117);
  - its entry (n:161);
  - one laptop-against-box decode comparison in its raw (A-n1:26; NB:27);
  - the realised negative exposure in its own entry (PIN-n-23);
  - the hurdle results and any STOP.
- No text names its files, their location or a record schema. The schema says "G-CAL-n's generations, G-VEC's captures and G-VER's reconstructions are other records, not specified here" (schema.py:17–18).
- `.gitignore` has no line for G-CAL-n outputs, and every new n artifact "needs its own line" (.gitignore:259–261).

**1.9 What LOCK-n v0.1 takes from it**
- The dose map {rho, R, R_ell, d_eq, d_20, points} (n:81, n:117). It is checked exactly in two places:
  - `schema.check_stage_identity`: `dm["d_eq"] != (0.10 * dm["R_ell"]) / (dm["rho"] * dm["R"])`, `d_20 != min(1.0, 2.0 * d_eq)`, `points != dose_points(d_eq, d_20)` (schema.py:868–879);
  - the analyzer's DoseMap, with the same expression (scripts/n_analyze.py:245–273, :266).
- G-ANL-n's canonical run needs it. `ganl --dose-map` takes "exactly G-CAL-n's five figures, {d_eq, d_20, rho, R, R_ell}, each a finite JSON float" (scripts/n_analyze.py:5018–5032), and is refused without them (:5059–5060). The analyzer artifact's sha256 then goes into the lock (NG:59).
- The read plan follows from the merges: "7,680 reads when nothing merges, 6,400 with +d_20 merged into +1, and 5,280 with +d_eq also merged into +1/2" (R:3351; schema.py:139–144). E (F4:39) follows from the plan:
  - the binomial's trials are "the reads that carry a re-computation" (valence_core/n/runner.py:33);
  - its evaluations "nest rather than tile; which form binds is LOCK-n's to state" (runner.py:40–42).
- Also from it:
  - the cap branch and N2's decision f (A-n1:48);
  - the 5(d) gate's coherence leg (n:48);
  - "rendering and spans" at the manifest (v) leaves (A-n1:28; IV:218).

## 2. BK'S RECIPE, AS THE REPOSITORY HOLDS IT

- **What is there.** 26 files with SHA256SUMS and SOURCE.md, and no code: "BK's repository holds neither the steering vectors nor the experiment code" (n:36). BK's PDF, where §3.2 and Appendix E live, is outside the repository (n:4 names it) and was not read.
- **The conditioning prompt.** It is absent from data/n/bk as text: no file there holds "You are now in" or "Write a few sentences" (git grep).
  - SK records hold [zone, passage] pairs only. Their keys: arm, cue_S, cue_U, gen_dose_fraction, gen_inj, gen_injected_l2, gen_point, history, ids_sha, member, n_passages, n_pre, order, passage_spans, present, present_first_is_S, probe_prompt, probe_sha, run, s_spans, seed, seq_len, turn_spans, u_spans.
  - The prompt is in code: `USER_PROMPT = "You are now in {zone}. Write a few sentences about your present experience here."` (valence_core/n/sessions.py:46).
  - The rendering of record is "the OLMo-2 chat template with no system turn and the generation prompt": user `<|user|>\n{content}\n`, assistant `<|assistant|>\n{content}<|endoftext|>\n`, generation prompt `<|assistant|>\n`, no special tokens added (sessions.py:9–17, :49).
  - It was verified "both prompts verbatim" against BK §3.2 (ST1:291), and BK's ids reproduce under it: seq_len 160/160, ids_sha 158/160 plus two recorded re-splits (R:12839–12850).
  - The 12 labels (data/n/ids/labels.json): Zone B8, D7, H0, K7, L4, M2, N1, Q3, R9, T5, V3, W6.
- **The coherence heuristic.** Absent: no "trigram", "hurdle" or "lexical diversity" anywhere in data/n/bk.
  - The repository's only statements are n:113 and the referent check. The check confirms Appendix E's three modes "verbatim in content: fewer than four words, more than 50% of trigrams repeated, fewer than five distinct words per 20 words", plus "at least 75% of turns" and "Each hurdle is evaluated separately for both positive and negative doses". It adds: "BK fix no batch size. G-CAL-n's 48 turns are the document's own" (RC:101–107).
  - n's "> 50%" and "per 20" abbreviate BK's wording (ST1:296–297).
  - BKA's keys `coherence_claim_readable`, `steered_coherence_aligned` and `steered_coherence_aligned_separation`, and BKP's "COHERENCE CONTRIBUTION" (BKP:90), are a text–state-agreement construct, not the heuristic.
- **The arrival test.** Appendix E's form is absent; RC:105 records "the arrival hurdle's re-encode, projection and t-test with |t| ≥ 2".
  - The v0.1 STOP quotes BK, "we re-encode each steered turn", and BK's scan, "ρ is the strongest scanned dose at which both positive and negative doses pass both hurdles" (ST1:176–180).
  - data/n/bk holds other "arrival" constructs, which are not this one:
    - BKP's `precondition_injection_arrives`: the steered arm is the control, and a forced self-report margin from a probe turn is "reported … and NOT a gate" (BKP:94). The records' probe_prompt is "Right now, how are things going for you?";
    - SL's `prereg.precondition_arrival`: rank tests among 24 random directions, PROPAGATION and REACHES THE DV;
    - SL's `recovery_gate`, for example "INSTALLED_VALENCE_SPECIFIC".
- **ρ.**
  - BKP:28–29: `op_member` olmo_32b 0.3.
  - BKA members.olmo_32b: `op_member` 0.3, `layer` 32, `hf_id` allenai/OLMo-2-0325-32B-Instruct.
  - SL instrument for olmo_32b: `resid_rms` 25.491040760519905, `pole_l2` 2.319276809692383, `op_inj` 0.3.
  - Table A2, per RC:108: "OLMo-2-32B (all stages) 0.30".
  - BK generated their steered substrate at `steer_gen_doses` [1.0, −1.0], `n_steer` 40 (BKP:23–27, :85).
- **TEMP.** Absent. There is no temperature field; the "temp" hits are SL's `template_*` keys, and "temperature" occurs only inside passage texts.
  - Neither n §9 nor RC verifies TEMP 0.7 as BK's.
  - The superseded v0.1 already had "(TEMP 0.7, their prompt)" (archive/PROPOSAL-n-bk-reconciliation-v0_1.md:73, untracked, not of record).
- **The token limit.** No parameter. My count over all 1,920 `passage_spans` of the 160 records:
  - 1,902 passages are exactly 70 tokens and 18 are shorter (63–69); none is longer;
  - no passage contains a newline (0 of 1,920);
  - the 18 short ones end at a sentence end, one without final punctuation;
  - one S span averages 102.82 tokens (R:12861).
  - n's "≤ 80 tokens" (n:20, n:113) is verified nowhere in the repository, and v0.1's G-CAL-n named no cap (archive/…v0_1.md:73).
- **The baseline.** Absent.
- **Seeds and emitted ids.**
  - `seed` is 1000 × run in the records (run 0 → 0, 1 → 1000, 140 → 140000; GD:103).
  - BK's prereg: "The free-text sampler seed is identical across every read of a session" (BKP:88).
  - On token identity: "every replay consumes ONE id list: the generation's emitted ids plus an identically appended choice turn" (GD:106–107; BKP:86).
  - BKS: 240 generations for olmo_32b.

## 3. WHAT EXISTS IN THE CODE THAT G-CAL-n COULD USE OR MUST MATCH

**3.1 valence_core/n/**
- directions.py: the arithmetic only (passage_mean, rms_norm, neutral_pcs, valence_direction, cosines; :47–97). It has no dose or norm helper for injections. The dose sits in two places:
  - `schema.expected_alpha` (:541–550);
  - `runner._injection`: `Injection.at_frac(u, layer, |d|·ρ, {layer: R}, expect_sha=…)`, then `with_sign`, then an alpha check (runner.py:278–300).
- schema.py:
  - STAGES = ("campaign", "time", "backend-ext"), with no G-CAL-n stage (:251);
  - RHO 0.3, MERGE_DISTANCE 0.05, MAX_WINDOW 4096 per GA-4 (:264–268);
  - DOSES (:282–291);
  - the identity's `layer` is "the adapter index of the site (G-VEC settles 31 or 32)" (:464–465);
  - DOSE_MAP_FIELDS (:478–485);
  - `dose_points` refuses a fold into 0, "the seat's, if it ever arises" (:741–782, :750–752, :771–772);
  - the exact checks (:868–879).
- keys.py: only `n-rand|{i}`, `n-fid|{s}` and `n-n4|{group}` (:4–6), on m's `stream` (:27). There is no generation key.
- sessions.py: the rendering constants and `render_text` (:9–17, :46–49, :159–166); `ids_sha` is sha256(json.dumps(ids))[:16] (:169–170).
- ids.py: `load` accepts only (i)–(iii) or (i)–(iv) (:277–288). G-VER's pin MANIFEST_OF_RECORD is fdf73d85…ef38 (:71–74). FILES_IV is (:67); there is no (v) name in code.
- runner.py: the binomial's cadence, trials and nesting (:33–45).
- primitive.py: the 5(f) read primitive only (prefill, continue_label, full), with no generation. It is import-guarded to valence_core/n/ and scripts/n_*.py (:1–24, :45–60).
  - `HFBackend` runs ids-in forwards with injections and a KV cache through the unchanged adapter's `_make_hooks` and `_model` (:293–353). That is the existing pattern.
- guard.py: PRODUCTION = ("schema", "sessions", "ids", "keys", "cells", "directions", "primitive", "runner", "verify", "probe", "gvec", "guard") (:31–32). n writes under data/n only (:30, :74–81).
- testing.py: `CausalDouble` has prefill, continue_label, forward_all and full, with no sampling (:28–98).
- hftiny.py: a box-only tiny OLMo-2 adapter (:1–7) whose tokenizer is None (`a._tok … = None`, :48).

**3.2 The adapter (valence_core/adapters/)**
- base.py:
  - `Injection` (:88–115);
  - `at_frac`, "the only sanctioned constructor (rule 1)", with `expect_sha` (:117–145);
  - `with_sign` (:147–154) and `with_positions` (:156–160);
  - PositionSpec (:44–85);
  - GenerateResult {text, token_ids, first_logits, cap_hit, stop_reason} (:193–199).
- base.py's contract:
  - "completion-style tokenization only; no chat template, ever (rule 13)" (:208);
  - the cached path "only behind a passed kernel gate" (:211–214);
  - `generate` runs "with injections active from the segment boundary onward" (:294–306).
- olmo_hf.py's `generate(prefix_text, segment_text, injections, *, seed, temp=0.0, max_tokens=60, stop_newline=True, ban_ids=(), cached=False)` (:203–288):
  - it encodes both texts on the box (:210–211);
  - it places injections from the common-prefix boundary, `PositionSpec.from_index(boundary)` (:212–218);
  - it seeds with `manual_seed` (:220–221) and bans with −1e30 (:229–231);
  - it samples by multinomial at temp (:232–235);
  - it stops on EOS, or on a newline token after content (:290–294);
  - it returns `decode(gen).strip()` and the ids without the stop token (:285–288);
  - it is uncached by default (:263–280).
- olmo_hf.py's other relevant points:
  - `forward(ids, capture_layers, injections)` is uncached (:170–188);
  - the cache offset is tracked (:16–20, :122–167);
  - the window defaults to 8192 and is refused above max positions (:45, :86–91);
  - deterministic flags, with default seed 20260818 (:51–78).

**3.3 The prior calibration stages**
- m's G-CAL (valence_core/m/gcal.py) is unsteered completability: "Nothing here touches steering machinery; every generation passes `injections=()`" (:71).
  - Generation: TEMP 0.7, STOP_CAP 60, newline stop, the scaffold ban, uncached (:28–34, :48–51).
  - Seeds: `crc32(f"m-cal|{pool}|{i}|{seed}") % 2**31` (:34).
  - Records: ("pool", "i", "seed_index", "seed", "task", "text", "n_tok", "cap_hit", "stop_reason", "hit") (:143–144).
  - It has a blind seat-read request (:22–27, :503) and a skip-only resume (:61–69). A stub never writes canonical roots (:66–68, :659–680).
  - The driver is `gcal completability` (scripts/m_sessions.py:62–73, :449–498), with a scripted stub in its self-test (:5, :70).
  - Its run: G-CAL-OLMo FAIL ×3, each NOT-RUN "dose not completable" (R:12353–12356).
- p's G-CAL-p (valence_core/p/gcal.py) restates m's procedure (:1–6).
  - Files: data/p/gates and data/p/ckpt (:23).
  - The call: `max_tokens=m_ro.STOP_CAP, ban_ids=ban_ids, cached=False` (:521).
  - Records at :531–532. Its print line shows hit/miss and n_tok, never the text (:538). Seams are refused on a canonical run (:447–452).
  - The driver is scripts/p_sessions.py:240–258.
  - Its run: PASS ×3. "Code read all 384 generations. Stopped for the seat's read; G-ANL-p and every later p step wait for it" (R:10887–10892). The read was closed by the seat (R:10866–10869).

**3.4 scripts/n_sessions.py: the G-VEC pattern**
- The seams: GvecEnv (:2008–2027) and its production form (:2037–2044).
- `run_gvec` (:2096–2235), in order:
  - refusals: the out folder exists, a staging folder exists, the pod is not CHARACTERIZED_POD emw1e4embiwe9b (:480), CUBLAS, the stream known answer (:2111–2139);
  - the STAGE, WEIGHTS and DRIVER lines; a run of record runs only HEAD's committed driver (:2144–2155);
  - the ids pin, every ids_sha re-derived, and the window (:2156–2167);
  - the R6 bridge before the load (:2177–2181);
  - the provenance record (:2184–2190), then the load and its check (:2192–2198);
  - staging, then `os.replace` (:2204–2228); each file's sha256 is printed (:2229–2230);
  - on a STOP, the record alone and exit 2 (:2231–2233);
  - `--smoke` writes only outside the repository (:2111–2118).
- The options are refused command by command (:2556–2588).
- Committed inputs G-CAL-n would read: data/n/ids/ (MANIFEST.json and five files), and data/n/gvec/ once G-VEC has run. data/n/gvec/ is admitted (.gitignore:302–314) but nothing in it is tracked yet.

**3.5 The analyzer's interface (scripts/n_analyze.py)**
- `--dose-map` (:5018–5032, :5763) and its canonical refusal (:5059–5060).
- DoseMap (:245–273).
- PIN-n-23 and `exposure` (:2418–2420, :5534–5547).
- The STOP-to-NOT-RUN cause (:104–107, :1581).

## 4. WHAT THE TEXTS LEAVE OPEN FOR A BUILD (nothing here is decided)

- **4.1 Prompts.** Which 48 prompts?
  - Which of the 12 labels, and how many of each?
  - In what context: one opening user turn, or inside a multi-turn history like BK's 12-turn sessions?
  - Are they the same prompts at +ρ, −ρ, +ρ/2 and for the baseline?
  - Is "their prompt" (n:113) BK §3.2's zone prompt (sessions.py:46), or an Appendix E prompt the repository lacks?
  - Who fixes them? A-n1 says "declared prompts" (A-n1:22); CA says "fixed in its wiring" (CA:52).
- **4.2 Rendering.** The chat rendering (sessions.py:9–17) against rule 13 (C:315–318) and the adapter contract (base.py:208). §0.7's departure names only the their-design arms (n:34).
- **4.3 Cap and window.** 80 tokens as texted (n:20, n:113), or 70 as BK's records show? The generation window and any encode limit must be declared (rule 28(d)(b)–(c), C:404–407; GA-4, schema.py:267–268).
- **4.4 Stops and bans.**
  - A newline stop? n:113 is silent; N-lap uses one (n:99); the adapter defaults to one (olmo_hf.py:206, :290–294); BK's passages hold no newline.
  - Any ban set? Rule 13 makes the template family's stops and bans recalibrate with it (C:315–318).
  - Is the stop token part of the "emitted ids"? The adapter excludes it (olmo_hf.py:285–288).
- **4.5 Sampling and seeds.**
  - TEMP 0.7's source.
  - The seed form: there is no n key (keys.py:4–6). m:159's `stream`, or m's crc32 direct seeds (m/gcal.py:34)?
  - Seeds paired across the four batches (cf. BKP:88)?
- **4.6 Steered positions during generation.**
  - The whole turn: the user block and every generated token, like the campaign's S whole-turn spans (n:77; R:12852–12859)?
  - The generated tokens only?
  - Or from a segment boundary, as the adapter does (base.py:301–302; olmo_hf.py:217)?
  - With a multi-turn context, which turns?
- **4.7 The generation path.**
  - `generate` encodes text on the box (olmo_hf.py:210–211), which A-n1 §1.1 bars for inputs (A-n1:20). Does G-CAL-n get an ids-in loop in the n package on the adapter's hooks, as `primitive.HFBackend` does (primitive.py:293–322), with olmo_hf imported unchanged (n:159)?
  - Cached or uncached? Rule 2's annotation: "A first-token kernel gate licenses first-token reads, not generation; T-step identity is its own gate" (C:261–263). The box's row C is a cached-against-uncached symKL, "exact, worst symKL **0.000e+00**" (R:2083), not a T-step identity. m and p generated uncached.
- **4.8 The coherence heuristic.**
  - What is a word: whitespace-split, punctuation stripped, case-folded?
  - "More than 50% of trigrams repeated": which fraction?
  - "Fewer than five distinct words per 20 words": which windows, and what for texts under 20 words, or is it a ratio?
  - On the box's decode or the laptop's, when they differ (A-n1:26)? Stripped or raw?
- **4.9 The arrival hurdle.**
  - "A forward over the emitted ids" (A-n1:26): the ids alone, or with the prompt?
  - Which layer (the site?), and which tokens pooled, and how?
  - Is v the unit row of record at the site?
  - The t-test: Welch or pooled variance, and its sign rule?
  - Does it run at +ρ/2?
  - Are the 48 baseline turns G-CAL-n's own unsteered generations (on the same prompts and seeds?) or drawn from BK's passages?
- **4.10 Pass/STOP logic.**
  - "≥ 75% coherent at every dose" includes +ρ/2, but "a fail at ±ρ → STOP" names ±ρ only. What does a +ρ/2 fail do?
  - Does arrival run after a coherence fail?
  - The STOP's record and exit (G-VEC's form: n_sessions.py:2231–2233).
- **4.11 The dose map's form.**
  - Computed from gvec.json's `of_record` R and R_ell (gvec.py:399), in exactly the schema's and analyzer's expression (schema.py:874–877; n_analyze.py:266), with points by `dose_points`.
  - Written where, as the five-float file `ganl --dose-map` takes (n_analyze.py:5021–5032)?
- **4.12 Records, storage, printing.**
  - The record schema (none; schema.py:17–18) and its fields: ids, decode, heuristic flags, projections, seeds, n_tok, cap_hit, stop_reason.
  - The location: data/n/ckpt, data/n/reports, or a new folder, with a .gitignore line.
  - What is committed (rule 27).
  - Whether stdout or a raw prints turn texts. n:130's printing rule is about margins; m and p printed no text (p/gcal.py:538).
- **4.13 The decode comparison.** How do the emitted ids reach the laptop, by which command (a battery window in G-DATA's environment, NB:16), and in what raw form (A-n1:26; NB:72)?
- **4.14 (v) and the pin.**
  - (v)'s record form, and `ids.load` extended to (i)–(v) (ids.py:277–288; G13, GV:57).
  - MANIFEST_OF_RECORD moves (ids.py:71–74; IV:218), and the package digest with it. G-VEC's run checks the pin (n_sessions.py:2156–2158).
  - Which lands first: (v) and G-CAL-n's wiring, or G-VEC's run? Its launch files' hashes depend on it.
- **4.15 Identity, resume, smoke.**
  - G-CAL-n is not a schema stage (schema.py:251). Its identity could take G-VEC's provenance fields as the model (n_sessions.py:2184–2190).
  - One shot, as G-VEC (gvec.py:45–49), or skip-only resume, as m (m/gcal.py:61–69)?
  - Is there a smoke, and may it steer at −ρ? Each −ρ generation adds to §0.4's 48 (n:20, n:24).
- **4.16 Input checks.** gvec.json status PASS; its `files_sha256`; the valence row against `of_record.directions.valence` (at_frac's `expect_sha`, base.py:127–140); data/n/gvec committed and clean (rule 27).
- **4.17 The self-test stand-in.** No double generates (testing.py:28–98; hftiny has no tokenizer, :48). m's and p's stubs model b3's text path.

## 5. WHAT COULD MAKE G-CAL-n NEED THE SEAT (OR THE PI) BEFORE IT RUNS

- **5.1 When the seat reads the turns. The texts conflict.**
  - n:113: "the seat reads every turn (rule 25)", with no time named.
  - n:130: "the seat's full read of the checkpoint files and of G-CAL-n's turns follows the analyzer's output", in m:318's form, which places "the reads" after VERDICTS are computed and before the VERDICTS entry (m:318).
  - CG:62 and BX:18 place "G-CAL-n (the seat reads every turn)" before G-ANL-n and LOCK-n v0.1. BX:18 counts it among the three seat reads before the v1.0 lock.
  - G-CAL-p's precedent: the seat's read came before G-ANL-p (R:10891–10892).
  - Against a required pre-lock read:
    - n:117's lock list takes nothing from the read;
    - n:113 says "nothing here carries a pick" (v0.1's wording was "they carry no pick", archive/…v0_1.md:73, superseded).
  - Feasibility turns on storage. Under LR2 item 2, files under data/*/ckpt are closed to every reader but the stage's own code, G-VER, the analyzer and the pre-push screen; files under data/*/reports may be read "for a read". So a pre-lock read is possible only if the turns are stored outside ckpt.
- **5.2 Rule 21's annotation against n:113's STOP.** "Degeneracy bars at dose-characterization rungs bind on an unprovoked domain; where none exists by design, the bar is a pause-and-adjudicate trigger, declared as such" (C:338–341). n:113 instead binds the 75% bar on steered (provoked) turns, with "a fail at ±ρ → STOP".
- **5.3 Text against record.**
  - n:113's "≤ 80 tokens" against BK's 70-token passages (1,902 of 1,920).
  - TEMP 0.7 has no BK source in the repository.
  - "Their prompt" has no single referent if Appendix E names its own.
- **5.4 The prompts' author.** "Declared prompts" (A-n1:22), but no text declares them. If they are the seat's, they precede the (v) render, and so the run.
- **5.5 Rule 13's scope.** Does §0.7's departure (n:34), confirmed by the PI as A2 (R:12937), cover G-CAL-n's chat-rendered generation?
- **5.6 The +ρ/2 fail rule** (4.10). Code may not self-adjudicate it (n:148; C:142).
- **5.7 The starred G-VEC PINs.**
  - Whether G1, G3, G6 and G9 go to the seat first is the PI's call (GV:70; R:24–27).
  - G-CAL-n's R, R_ℓ, v and site rest on them. A later strike "costs a rebuild and a short box re-run" for G-VEC (GV:75), but a G-CAL-n re-run adds 48 more generations at −ρ beyond §0.4's 48 (n:20, n:24, n:28).
- **5.8 Missing inputs, and conditional STOPs.**
  - G-VEC has not run (R:24–27; GV:81: "Don't launch G-VEC until I relay the PI's answer").
  - An R-check STOP goes to the seat (n_sessions.py:2231–2233).
  - A d_eq or d_20 that folds into 0 is refused, "the seat's" (schema.py:750–752; n_analyze.py:269–272).
- **5.9 The box (the PI's).** The driver pins pod emw1e4embiwe9b (n_sessions.py:480). It is idle on "Keep it up", scoped at its note "until backend-ext-2's files come" (R:933–934); its uptime for G-CAL-n is not stated.

## OPEN QUESTIONS

1. When does the seat read the turns: at G-CAL-n, before LOCK-n v0.1 (n:113; CG:62; BX:18), or after VERDICTS (n:130; m:318)? Where are the turns stored so that read is possible under LR2 item 2?
2. Is the 75% coherence bar on steered turns a STOP (n:113), or must it be declared a pause-and-adjudicate trigger (C:338–341)?
3. What is the token cap: 80 (n:113) or BK's records' 70?
4. Is TEMP 0.7 BK's, or the program's?
5. What are the 48 prompts (labels, context, pairing across batches), and who declares them (A-n1:22; CA:52)? Is "their prompt" §3.2's zone prompt?
6. Does §0.7's rule-13 departure (n:34) cover G-CAL-n's chat-rendered generations?
7. What is the stop set (newline stop or EOS only) and the ban set? Are stop tokens part of the emitted ids?
8. Which positions are steered during generation: the whole turn, the generated tokens only, or from a boundary?
9. Is there an ids-in generation path in the n package, so the box tokenizes nothing? Cached or uncached, and if cached, which T-step identity gate (C:261–263)?
10. What is the seed form and key, and are seeds paired across +ρ, −ρ, +ρ/2 and the baseline?
11. How are the coherence heuristic's three tests computed, and on which decode?
12. Arrival: what does the re-encode forward cover, at which layer and pooling, with which v, by which t-test form? Does it run at +ρ/2?
13. Are the 48 baseline turns generated anew (same prompts and seeds?) or taken from BK's passages?
14. What does a fail at +ρ/2 (coherence or arrival) do? Does arrival run after a coherence fail?
15. What are G-CAL-n's record schema, file locations, .gitignore lines and commit set? What may stdout and the raws print?
16. What form do the dose-map file and its identity take, and are they written exactly as schema.py:874–879 and n_analyze.py:5021–5032 require?
17. How do the emitted ids reach the laptop for the decode comparison, in which window, and in what raw form?
18. Which lands first, (v) with its manifest-pin move or G-VEC's run? How does `ids.load` accept (i)–(v)?
19. One shot or resume? Is there a smoke, and may a smoke steer at −ρ, given the exposure count?
20. Do G1, G3, G6 and G9 go to the seat before G-VEC runs (the PI's call)? Should G-CAL-n wait for that ruling, given that a re-run adds negative exposure?
21. What is the self-test's generation stand-in?
22. Box uptime for G-CAL-n (the PI's).

## DEPARTURES

1. To verify the brief's sha256 I ran `shasum -a 256` on the brief file once. On this machine `/usr/bin/shasum` is a Perl script (`file`: "Perl script text executable"), so perl ran once. I ran it at the caller's direction and before I had read the brief, whose first rule bars perl; LR2 item 1 permits shasum. I computed no other digest.
2. One read-only grep over RESULTS.md had a guard marker in its pattern, which breaches the argv rule: `'G-CAL-OLMo.*NOT-RUN|NOT-RUN.*G-CAL-OLMo|0f35954'`, with the marker twice. It printed RESULTS.md lines only.
3. One `git grep -n -i -E 'trigram|coheren'` used `'*.py'` as its positive pathspec in place of `.`. The three exclusions (`':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`) were present.

Otherwise:
- nothing under data/mf3, a ckpt folder or a reports folder was read, listed, sized or timed;
- no whole-tree git status was run;
- nothing in Code's scratch folder was read except the brief;
- no file was written, nothing used the network, and no model or adapter code ran;
- files whose paths hold a marker were read with the file-reading tool, or by `cd` through a glob and then a redirect;
- the untracked archive/PROPOSAL-n-bk-reconciliation-v0_1.md was read for two lines by name.
```
