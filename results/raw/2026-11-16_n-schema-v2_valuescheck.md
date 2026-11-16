# n — the schema's second commit: the blind values-check, three passes, and Code's dispositions

*The n-build session (Code), PI date 2026-11-16. Checked: the RESULTS.md entry for the schema's second commit (the
stage report `n-report-v1` and G-READ-n's artifact `n-gread-v1`), and `valence_core/n/schema.py`, before their commit.
Three blind checkers, all Code's subagents. Each was briefed to run no Python and to write nothing, under the list of
record v2's items 1–5, quoted verbatim, and the coordinating session's lines on `data/mf3`. Pass 2 was blind to pass 1.
Pass 3 read the change since pass 2's draft, the entry, and Code's dispositions of passes 1 and 2. No fourth pass was
run: the edits after pass 3 were checked by tool, by Code's read of the diff and by both self-tests.*

*What each pass checked:*
- *Pass 1: the module draft `d9bdd15f61825addc84549ad72e19e8fe19aeb5d5433c525c62c9138edc32c45` and its entry, at HEAD
  `718c48e`. Its report calls this draft "the schema v2 draft" (the schema's second version); Code's scratch named it
  v3. The hashes are the record.*
- *Pass 2: the module draft `098ecefadba6e2da349978dd42d4dfe9d2828787c0090590026e39b18e9594f1` (v4.1) and its
  entry.*
- *Pass 3: the module draft `6575c20afdd8d08f9eed36bd8cf4c9e47ecdf14ee5568ac0ee37aae5a9d3f371` (v4.3), its entry,
  and the two dispositions below. It read them before the edits that its own dispositions list.*
- *The committed module is v4.4, pass 3's draft plus the edits its dispositions list:
  `4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665`.*

*Between the passes, Code changed the drafts:*
- *v3 → v4 (`a1c85568…`): pass 1's dispositions;*
- *v4 → v4.1 (`098ecefa…`): the three points pass 1 left open, and a standing pause with a hit cap recorded as PAUSE
  (until then only PI-STOP was valid there, so the runner could not have written that report);*
- *v4.1 → v4.2 (`80dab6f2…`): three gaps Code found while syncing the runner to the report form, and stale texts.
  The gaps were a rendering pause resumed at its own place, a read-less binomial fire as the last pause, and a
  binomial fire in `also_fired` with its batch;*
- *v4.2 → v4.3 (`6575c20a…`): pass 2's dispositions;*
- *v4.3 → v4.4 (`4bed3f9a…`): pass 3's dispositions.*

*Self-tests, each in a battery window the coordinating session granted: v4 173/173, v4.1 177/177, v4.3 191/191 and
v4.4 199/199. v4.2 was not run on its own. The n package's self-test, from a scratch overlay of HEAD's
`valence_core` and `data/n/bk` with the drafts on top, gave 120/120 under v4.3 and 121/121 under v4.4.*

*Each report is reproduced as its checker returned it. None prints a local path, and nothing in them is changed. In
the reports, "E:" and "S:" are line numbers in the entry and module drafts that the pass read; pass 3 also cites the
dispositions files as "D3:" and "D41:", by their lines when it read them.*

*Tallies, Code's count of each report's verdicts:*
- *Pass 1: 39 items. 18 CONFIRMED, 12 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE, and 3 CONFIRMED in part and NOT CHECKABLE
  in part. 13 observations.*
- *Pass 2: 33 items. 22 CONFIRMED, 7 IMPRECISE, 2 FAIL, 1 NOT CHECKABLE, and 1 CONFIRMED with a NOT CHECKABLE part.
  Plus its observations.*
- *Pass 3: 31 items. 18 CONFIRMED, 8 IMPRECISE, no FAIL, 2 NOT CHECKABLE, and 3 CONFIRMED with a NOT CHECKABLE part.
  Plus its observations.*

## Pass 1 (the v3 draft), as returned

Blind values-check of the schema v2 draft (S) and its entry draft (E). I ran no Python, wrote nothing, and edited, staged or committed nothing. I listed, read, hashed and searched nothing under data/. Every git command named its paths. Sources are cited as n:N (PROPOSAL-n-bk-reconciliation-v0_2.md, line N) and k:N (PROPOSAL-k-echo-channel.md). "questions.md" is results/raw/2026-11-16_n-schema_code-to-design_questions.md and "prebuild.md" is results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md.

**Items**

1. **E:2, the draft's sha256 `d9bdd15f…2c45`.** Checked by shasum of the draft. CONFIRMED.

2. **E:2–3, the predecessor's sha256 `77c12d6d…94bc` at `5a97527`.** Checked with `git show 5a97527:valence_core/n/schema.py | shasum -a 256`. The working-tree file gives the same hash, and the blob is the same at 5a97527 and HEAD (718c48e). CONFIRMED.

3. **E:1, "the schema's second commit".** `git log -- valence_core/n/schema.py` lists only 5a97527. CONFIRMED.

4. **E:5–6 and E:13: the diff only adds, apart from EXAMPLES; the record, cell and identity forms and checks are unchanged.** The diff has six hunks: 126,127c126,139 / 131a144 / 912a926,1252 / 922a1263,1266 / 1043a1388,1466 / 1331a1755,1839. The only removed lines are the old two-line EXAMPLES paragraph.
   - check_record (S:698–893), check_cell (S:896–923), check_stage_identity (S:657–695) and all nine record, cell and identity tables are byte-identical to 5a97527.
   - The loop at S:1118–1122 adds 17 keys to the existing `NESTED` dict. None of them collides with NESTED's 9 existing keys or with `_check_type`'s 13 type names, so the old checks route exactly as before.
   - CONFIRMED.

5. **E:7–11, the list of what was added.** IMPRECISE (minor). The list leaves out `_check_report_nested` and the import-time registration of its 17 type names into `NESTED` (S:1028–1122). It also leaves out the 24 names appended to `__all__` (S:1263–1266). Suggested addition: "the report's nested checks, registered into `NESTED`, and the new `__all__` names".

6. **E:9 against S:137–139, the EXAMPLES paragraph "extended" to the new builders.** IMPRECISE. S:137 names `example_report` and `example_gread` but not `example_pause` (S:1427), which E:9 lists. Add ``example_pause`` to S:137.

7. **S:16–17 (unchanged): "G-CAL-n's generations, G-VEC's captures, G-VER's reconstructions and the stages' reports are other records, not specified here".** FAIL. The draft itself contradicts this:
   - S:126: "THE STAGE REPORT (``n-report-v1``) AND G-READ-n'S ARTIFACT (``n-gread-v1``)";
   - REPORT_FIELDS (S:939).

   Corrected wording: "G-CAL-n's generations, G-VEC's captures and G-VER's reconstructions are other records, not specified here; the stage report and G-READ-n's artifact are specified below." E:5–6's "only adds, apart from the EXAMPLES paragraph" would then also have to name this sentence.

8. **E:3, E:10, E:40: 153 = 36 accepted + 117 refusals; 10 new accepted cases and 35 new refusals.** Counted from call sites in S:1469–1840.
   - Accept: 17 call sites giving 26 cases at 5a97527 (the `good` loop over 10 entries at S:1504–1517, plus 16 single calls). The draft has 21 call sites giving 36 cases. The new ones are the loop over a 7-entry tuple (S:1767–1772) and S:1773, S:1779, S:1780.
   - Refuse: 82 call sites before, 117 now. The new ones are 25 report cases (S:1784–1824) and 10 G-READ cases (S:1825–1839).
   - RESULTS.md:251 gives 26/82 for 5a97527.
   - CONFIRMED by count. Whether the run passed is NOT CHECKABLE without running it.

9. **The example builders produce objects that pass, by reading each new accept case.** Checked S:1389–1464 against S:1125–1249. CONFIRMED.
   - Complete campaign: per_arm is built from read_plan, obtained equals the cells' records, every arm is complete.
   - PAUSE: half the reads obtained, one unadjudicated "nonfinite" pause at launch 500.
   - Adjudicated pause (ruling set), ending COMPLETE.
   - CAP: used 600 against a cap of 500, so hit is true.
   - G-VER-STOP: a stop record, rendering_mismatches 1, 0 obtained.
   - Binomial fire at the run's end: read and launch null; batch 0–159, k 1 of n 160, p0 0/2400 equal to the identity's, alpha 0.01; ends PAUSE.
   - backend-ext: null plan sha256, one N1-V d = 0 cell of 24, per_arm 24/24.
   - The sha256 accept case.
   - G-READ, all PASS: median 0.96 is at least .90, above the comparator max 0.5+0.005·23, and every layer is above 0.58.
   - G-READ mixed: the FAIL result has 0.62; the NOT-COMPUTED result has a null median, no layers and a null comparator.

10. **Each new refusal is refused by the check its name names, by reading.** CONFIRMED. For example:
    - "planned not the plan's" (319/319) passes the nested per_arm check and fails at S:1147;
    - "COMPLETE over a standing pause" fails at S:1197, before S:1199 is reached.

    A file named st3.txt in the scratch folder beside the drafts holds 117 "refused" lines and ends "n schema self-test: 153/153". Its 35 new messages agree with this reading. Nothing ties that file to the draft's sha256.

11. **E:15–16 and S:1022–1025, identity_sha256's canonical form; S:1023 "byte-equal to m's resume._canon".** Checked against valence_core/m/resume.py:183–185. CONFIRMED.
    - Both pass the same arguments: sort_keys, separators (",", ":"), ensure_ascii False, allow_nan False.
    - `_canon` also passes `default=_refuse`. json calls `default` only for non-native values, and check_stage_identity admits only exact str, int, finite float, bool, list and dict. So on a valid identity the bytes hashed equal `_canon(identity).encode("utf-8")`.
    - It is not `json_text`'s form (resume.py:203–208: default separators and a trailing newline).
    - The accept case at S:1773 re-derives the same json.dumps call; it does not call `_canon`.

12. **E:15–23 and S:127–130, what the report carries.** Checked against REPORT_FIELDS (S:939–951) and the tables at S:953–988. CONFIRMED. Each cell entry also carries its record count (S:946), which the obtained check uses; E:20 does not mention it.

13. **E:14 and S:127, "counts only, never a margin".** IMPRECISE. No field holds a margin, which fits n:130's blinding. But the report is not counts only. It also carries:
    - the stage identity (R, R_ell, d_eq, TAU, the identity bound);
    - sha256s and states;
    - the binomial's alpha (S:970);
    - a free-text `stop.detail` (S:975), whose "no margin" is not enforced.

    Suggested wording: "no margin or other per-read value: counts, states and sha256s".

14. **E:14, "written at every invocation's end".** NOT CHECKABLE: the runner is not in the tree. It is consistent with end_state's description "the invocation's end" (S:944).

15. **E:17, the plan's sha256 at the campaign only.** S:943 and S:1136–1139. CONFIRMED.

16. **E:18 and E:23: the end states, the STOP record and the cap.** S:930, S:1187–1196; n:134 names "a PI stop, a G-VER STOP or its cap", n:148 names the pauses. CONFIRMED.

17. **End-state rules the code enforces but no text states (S:1187–1200).** IMPRECISE. The code enforces five rules:
    - PAUSE exactly when an unadjudicated pause stands (S:1197);
    - CAP exactly when the cap is hit (S:1195);
    - `stop` set exactly at G-VER-STOP or PI-STOP (S:1188);
    - any rendering mismatch forces G-VER-STOP (S:1205);
    - COMPLETE at the campaign only when every arm is complete (S:1199).

    Because each is an "exactly when" rule, no valid report exists for a standing pause together with a hit cap, a PI stop or a rendering mismatch. n:148 stops only "the arm's launches", so the other arms keep running and those combinations can arise. The docstring should state the five rules and either a precedence among them or that these combinations are refused.

18. **E:19, E:25, S:124, S:129: obtained and complete.** S:1029–1038 and S:1143–1155. CONFIRMED, with a note:
    - The report-level check is count equality: `complete == (obtained == planned)`, where obtained is the sum of the arm's cells' `records`, and at the campaign planned is read_plan's per-arm count.
    - That equals E:25's read_id-set equality only when every cell passes check_cell (each valid record's read_id is a plan read_id and unique in its cell). That is the reader's to check, as S:1126–1127 says.

19. **E:21–22, what each pause carries.** Checked against PAUSE_FIELDS and BINOMIAL_FIELDS (S:953–971) and S:1159–1186; n:148 (the triggers) and n:77 (binomial against p0, cadence 160). CONFIRMED. The three kinds are n:148's binomial, NaN/inf and identity-bound triggers, and a batch's p0 must equal the identity's fidelity_rule (S:1184). Two loose points:
    - S:954 says pause_id is "'p01', 'p02', ... in launch order"; the code checks only that each id is a fresh `pNN` (S:1161).
    - Launch indices must strictly increase (S:1173).

20. **E:26–27, a pause stands while unadjudicated and clears whatever the ruling.** S:958, S:1176–1177, S:1186. CONFIRMED. The check treats any unadjudicated pause as standing; which arms it stands on is the reader's, from `arms_in_scope`.

21. **E:28–29, no ruling's effect on reads is recorded.** That part is CONFIRMED: no such field exists (S:953–962). "would be a new field, in its own schema commit, agreed with n-analyzer first" is NOT CHECKABLE: it is a commitment.

22. **E:23, S:130, S:951, "n §4's counters".** IMPRECISE (minor). All four of n:128's counters are carried: "fidelity exceedances by arm and dose; rendering mismatches; NaN/inf margins; label-mass floors on the restricted read". The report also carries `identity_out_of_bound`, which is §6's identity-bound trigger (n:148), not an n §4 counter. Suggested wording: "n §4's counters and the identity-bound count".

23. **S:987, `label_mass_below_floor` "null before it" (the lock).** IMPRECISE. It is not enforced: check_report never compares it with `lock_sha256`. example_report writes null at the campaign (S:1424) even though example_identity sets a lock ("1"×64, S:1285), and that builder feeds n-analyzer's battery. Either check `(c["label_mass_below_floor"] is None) == (ident["lock_sha256"] is None)` and give the campaign example a dict, or reword to "null where no floor is set".

24. **Cell-name check (S:936, S:1044–1045) and its refusal case (S:1823–1824).** IMPRECISE. `_CELL_NAME` checks only the name's shape. It accepts names `cell_filename` can never produce, such as `N1-V__valence__p9.json` or `N4-T__valence__p1.json`. The case "a cell name that is no cell file's" is refused only because of its `.jsn` extension. Check names against `cell_filename` over ARM_CELLS, or rename the case.

25. **E:30, the G-READ artifact names the campaign it read (plan, identity and cells by sha256).** S:995–999. CONFIRMED.

26. **E:31 and S:133, "the probe's package and keys".** IMPRECISE. GREAD_PROBE_FIELDS (S:1000–1007) hold package_sha256, lr {seed, iters, rate, l2}, shuffles, shuffle_seed, layers and bar: seeds and settings, but no key. Suggested wording: "the probe's package sha256 and settings (k's fit_lr hyperparameters, the shuffles and their seed, the layers, the bar)".

27. **S:1002 and S:1462, lr = k's fit_lr hyperparameters.** Checked against valence_core/echo/probe.py:19 (`LR_SEED, LR_ITERS, LR_RATE, LR_L2 = 7, 300, 0.1, 1e-2`) and :22–23. The example's shuffle_seed 20260905 is shuffle_null's default (:57–58). CONFIRMED. check_gread pins shuffles to 200 and bar to 0.90, but checks only lr's types (S:1084–1087), not its values.

28. **E:31, S:133, S:993, "one result per axis and kept dose point".** IMPRECISE, for two reasons:
    - Valence has no result at −1, a point dose_points always keeps (S:640). GREAD_AXES (S:933) lists +1, +1/2, +d_20 and +d_eq; the −1 reads are +1's − pole.
    - check_gread has no identity. It refuses repeats and points outside GREAD_AXES (S:1222–1226), but it neither requires a result at every kept point nor refuses a result at a merged-away label (a +d_20 result beside +1 with merged ["+d_20"] passes).

    Suggested wording: "at most one result per (axis, point) of GREAD_AXES (valence +1, +1/2, +d_20, +d_eq; span_reward f0.10, f0.20), the −1 reads entering +1's contrast; that these are the kept points is the reader's check".

29. **E:32, S:134, S:1229–1231, the contrast: the − pole at valence +1, else the shadow (n §3).** n:121: "discriminating the +pole from the −pole where both exist, else the +pole from the shadow". Valence reads −1 only (n:87), and N2's points are f only (n:90–91), so the − pole exists only at valence +1. CONFIRMED.

30. **E:33–35 and S:134–135: per-layer AUCs against the shuffle null, the band median, the comparator's 24 band medians, and the three statuses.** S:1014–1017, S:1097–1113, S:934; k:232–235 ("200 label shuffles per layer for the null (95th percentile)"). CONFIRMED.

31. **S:1016, comparator "nulls when not computed".** IMPRECISE. Not enforced: S:1107 only requires band_medians and max to be null together.
    - A NOT-COMPUTED result may carry 24 medians.
    - A computed result may carry nulls, and S:1246 then forces it to FAIL. No text states that rule.

32. **E:37–38, S:135, S:1210–1211, S:1245–1249: the PASS rule against n §3's sentence, and its label.** CONFIRMED. n:121: "PASS iff the band median AUC ≥ .90 (k's bar, calibrated on ± contrasts — the contrast here) and above the comparator's band."
    - The code is exactly the stated rule: median ≥ 0.90, strictly above the comparator's max, and every layer above its shuffle null.
    - Both the docstring and the entry label it Code's reading.
    - "the comparator's largest" is a reading of "the comparator's band".
    - The every-layer shuffle clause is not in n §3's sentence, which says only "AUC against 200 label shuffles". It is k §1.4 G3's form (k:263–264: "above the shuffle 95th percentile at every layer in the band"), and is worth citing as such.

33. **S:1218, the message "bar 0.90, 200 shuffles and at least one layer (n §3)".** IMPRECISE (minor). n:121 names layer 32 and the final layer; "at least one layer" is the check's own rule, not n §3's. Suggested: "(n §3's bar and shuffle count; at least one layer)".

34. **E:38–39, "The early block's Q5 (the capture layer) can change the probe's layers, not these fields."** IMPRECISE. Two committed blocks are "early":
    - 8e3bf91's entry calls n-analyzer's block "one early block" (RESULTS.md:64, :74–75), and its Q5 is "Tuples that cannot occur" (prebuild.md:37);
    - the capture layer is Q5 of n-build's block of five early questions (questions.md:41 and :176, committed at 718c48e).

    Suggested wording: "n-build's block of five early questions (`718c48e`), its Q5 (G-READ-n's capture layer), …". The substance holds: `layers` is a list (S:1005), per_layer must match it (S:1238), and prebuild.md:80 agrees. Note that questions.md:214 says readings (a), (b) and (d) would change the identity's `capture_layers` check, a follow-up schema commit outside "these fields".

35. **E:2, E:3, E:24, S:126, S:927, S:1023, S:1127: "settled with n-analyzer", "n-analyzer's verdicts command reads both forms", "binds them by sha256".** NOT CHECKABLE: this is session traffic, and no n analyzer is in the tree (`git ls-files` lists only valence_core/n/__init__.py and schema.py; scripts/ holds only an untracked n_sessions.py). Where the analyzer's committed block states a need, the forms meet it:
    - G-READ-n's status and band median per axis and dose (prebuild.md:80; Q4 at :31–34 — valence +1 and d_eq and span_reward f0.20 are in GREAD_AXES, and merged points are reachable through `merged`);
    - absent or not computed counts as not PASS (:87);
    - the arms a pause stands on, for N4 and N2 (:46–47);
    - the no-arm NOT-RUN causes, from the end state and per-arm completeness (:106).

36. **E:3–4, "Nothing ran on a model."** NOT CHECKABLE as an act. By reading, the module imports only hashlib, json, math, re and typing (copy and sys in the self-test) and touches no model or file.

37. **E:40–43, how the self-test ran.** `--verbose` prints each refusal's message: CONFIRMED (S:1501–1502, S:1846; messages are cut at 220 characters). The rest is NOT CHECKABLE: nice -n 19, `python3 -m`, Python 3.12.9, the battery window, and the scratch copy being byte-identical to "the committed file" (that commit does not exist yet). RESULTS.md:255 gave the scratch copy's sha256; this entry could do the same.

38. **E:44, "VALUESCHECK_LINE".** NOT CHECKABLE: it is an unfilled placeholder.

39. **E:45–46, committed by path, not pushed, next steps.** NOT CHECKABLE: future acts.

**Observations**

- **O1. NOT-RUN record still missing (n:134).** NOT-RUN's clock causes (no box, a gate STOPPED with no re-specification, the PI declined v1.0) have no carrier. 5a97527's entry deferred "the NOT-RUN record" to a later commit (RESULTS.md:238–239). This entry does not say it is still outstanding.
- **O2. Rendering mismatch: n §6 says pause, the schema says STOP.** n:148 lists "a rendering mismatch" among the pause-and-adjudicate triggers. PAUSE_KINDS has no kind for it, and S:1205 makes it a G-VER-STOP, following n:119's G-VER "mismatch → STOP" and the committed S:809. Under n:134 that can make a unit NOT-RUN where §6 would only pause it. Neither draft flags this as a reading.
- **O3. Some end states cannot be recorded.** Because of item 17, a standing pause cannot coexist with a hit cap, a PI stop or a mismatch. n:134 distinguishes exactly those ends for NOT-RUN.
- **O4. When a ruling took effect is not recorded.** For n:148's "Every pause STOPs the arm's launches until adjudicated", no field records the launch index or invocation at which the ruling took effect. So a report cannot show that no read of an arm in scope was launched while its pause stood.
- **O5. A read that fires two triggers.** With strictly increasing launch indices and a single `kind`, such a read can be recorded as one pause only. The self-test's own non-finite shadow (S:1534–1535) is both NaN/inf and outside the identity bound.
- **O6. Non-firing binomial batches leave no trace.** Only firing batches are carried. The "fidelity binomial's state" named at RESULTS.md:238 survives only through fires and counters.fidelity.
- **O7. What the cap counts.** `cap.used_ms` is the sum of records' `duration_ms` (S:979), which is model work only (S:279). Whether the PI's hour cap (n:101, :118, :120) counts loads and other wall-clock time is the lock's call. This is an unflagged reading.
- **O8. Non-finite reads count as obtained.** "obtained … finite or not" (E:25) decides whether an arm with non-finite reads is complete under n:134. The seat may want this named as a reading.
- **O9. The CV form has no field.** n:121's "grouped leave-one-session-out CV" is not recorded. probe.py has both a leave-one-session-out form (:38–66) and a grouped 10-fold form (:69–113), so the artifact cannot show which ran.
- **O10. Other stale docstring lines.**
  - S:1: "(n v0.2 §8 step 6, its first commit)".
  - S:5–7: "every field the read runner writes" (G-READ-n's artifact is written by the probe).
  - S:222: SchemaError's "A record, cell or identity".
- **O11. Minor gaps in the checks.**
  - At non-campaign stages, a cell whose arm is missing from per_arm is never counted (S:1153–1155).
  - `stop.detail`'s "one line, no margin" is not enforced.
  - A G-READ result's `merged` accepts any dose label (S:1227).
- **O12. Cosmetic.** There are three blank lines at S:924–926, S:1250–1252 and S:1386–1388, where the file uses two elsewhere. No line exceeds 120 characters.
- **O13. How I worked.**
  - One diff output was too long to display, and the tool harness saved it to its own tool-results store outside the repository. I wrote nothing myself.
  - I read st3.txt beside the drafts (not a brief source) as supporting evidence only.
  - The brief's key says "B:line" for the module; I used "S:line" as you asked.

## Code's dispositions of pass 1

The check read the v3 draft (sha256 `d9bdd15f…2c45`) and its entry. Every FAIL and IMPRECISE item is applied below,
and so is every observation that asked for a change. "S" is the module; "E" the entry. Items not listed were
CONFIRMED or NOT CHECKABLE and needed no change. Each disposition states the wording at v4. Pass 2's dispositions
revise items 5, 7, 13 and O6, and pass 3's revise item O9 (the CV form).

- **Item 5, IMPRECISE (E's list of additions).** Applied. The entry now names "the report's nested checks
  (registered into `NESTED`)" and "the new `__all__` names".
- **Item 6, IMPRECISE (EXAMPLES omits `example_pause`).** Applied: S's EXAMPLES paragraph names `example_pause`.
- **Item 7, FAIL (S:16–17, "the stages' reports are other records, not specified here").** Applied in the checker's
  terms. The sentence reads: "G-CAL-n's generations, G-VEC's captures and G-VER's reconstructions are other records,
  not specified here; the stage report and G-READ-n's artifact are specified below." A sentence on where a NOT-RUN is
  recorded follows it (observation O1). E's "only adds" claim now names this passage among the five rewritten ones.
- **Item 13, IMPRECISE ("counts only, never a margin").** Applied in the checker's wording: "no margin or other
  per-read value -- counts, states and sha256s". `stop.detail` is now checked as one line of at most 200 characters.
  Its "no margin" is the writer's rule; no check can enforce it, and the text does not claim one does.
- **Item 17, IMPRECISE (end-state rules unstated; some combinations unrecordable).** Applied:
  - S's docstring states the rules, with a precedence: PI-STOP may end a unit whose pause stands; CAP and
    G-VER-STOP may not.
  - The code was changed to match.
  - Refusal cases were added for CAP and for G-VER-STOP over a standing pause.
  - After v4's self-test, Code found one more combination with no valid end state: a standing pause with a hit cap. It
    arises when a pause fires on the read that reaches the cap, or when the end-of-run binomial evaluation fires after
    a CAP. It now records as PAUSE: the seat rules first, and the next report ends as CAP. An accept case was added,
    and n-analyzer was told by message.
- **Item 19, loose points (pause ids "in launch order", checked only as fresh `pNN`).** Applied: a pause's id is
  now `p01`, `p02`, … by its place in the list, which is in launch order. A refusal case was added.
- **Item 22, IMPRECISE ("n §4's counters").** Applied in S and E: "n §4's counters and the identity-bound count".
- **Item 23, IMPRECISE (`label_mass_below_floor`, "null before it", not enforced).** Applied as the second option the
  checker gave. The docstring and the field now say "null where no floor is set". It is not enforced, because
  whether the lock sets a floor for N-pod is the lock's call (n §4 names the counter; n §2.6 gives a floor only for
  N-lap's f = 0.20).
- **Item 24, IMPRECISE (cell names checked for shape only).** Applied:
  - names are now checked against `VALID_CELL_NAMES`, `cell_filename` over `ARM_CELLS`, 136 names;
  - the case with the `.jsn` name is now refused by that check;
  - a case for a well-formed name no stage can hold (`N4-T__valence__p1.json`) was added.
- **Item 26, IMPRECISE ("the probe's package and keys").** Applied: "the probe's package sha256 and settings: k's
  `fit_lr` hyperparameters, the CV form, the shuffles and their seed, the layers and the bar".
- **Item 27, a note on a CONFIRMED item (`lr`'s values unchecked).** Applied: `GREAD_LR` pins k's values (7, 300,
  0.1, 0.01; `valence_core/echo/probe.py:19`) and the check refuses any other. A refusal case was added.
- **Item 28, IMPRECISE ("one result per axis and kept dose point").** Applied in the checker's suggested wording:
  "at most one result per (axis, point) of `GREAD_AXES` … the −1 reads enter +1's contrast; that the points are the
  kept ones is the reader's check". `merged` may now name only `GREAD_MERGEABLE`'s labels for the axis (valence:
  +d_20 and +d_eq; span_reward: none), once each, and never the kept label (observation O11).
- **Item 31, IMPRECISE (comparator "nulls when not computed", unenforced).** Applied. A NOT-COMPUTED result that
  carries a comparator is refused. The docstring states the rule: "A computed result without a comparator is a
  FAIL; a NOT-COMPUTED one carries neither a comparator nor AUCs".
- **Item 32, CONFIRMED, with a citation suggested.** Applied: "(the last clause k §1.4 G3's form)".
- **Item 33, IMPRECISE (the probe check's message).** Applied: "n §3's bar (0.90) and shuffle count (200); at least
  one layer".
- **Item 34, IMPRECISE ("the early block's Q5").** Applied in E: "Q5 of n-build's block of five early questions
  (`718c48e`), on G-READ-n's capture layer". E also says that readings (a), (b) and (d) would change the identity's
  `capture_layers` check, in a follow-up schema commit (questions.md:214).
- **Item 37, the scratch copy's sha256.** Applied: E names the scratch copy's sha256.
- **Item 38, the `VALUESCHECK_LINE` placeholder.** Filled before the commit.
- **Observations:**
  - O1 (NOT-RUN record): S says a NOT-RUN on the clock is a record in n-analyzer's own schema (`n-not-run-v1`, as
    n-analyzer gave it by message), and a NOT-RUN for no arm complete is derived from a report.
  - O2 (rendering mismatch): a pause kind `rendering` was added (n §6). G-VER's mismatch before any read stays a
    G-VER-STOP (n §3). Flagged as Code's reading.
  - O3: see item 17.
  - O4 (when a ruling took effect): `resumed_at_launch_index` was added. S states that a fired monitor ends the
    invocation for every arm (Code's design, flagged), so every read after a pause's own was launched after its
    ruling.
  - O5 (a read firing two triggers): `also_fired` was added, with the precedence rendering, nonfinite,
    identity-bound, fidelity-binomial.
  - O6 (the binomial's state): `binomial_state` was added (trials, exceedances, evaluations, fires). Its fires must
    equal the number of fidelity-binomial pauses.
  - O7 (what the cap counts): stated in S as Code's reading and flagged.
  - O8 (non-finite reads obtained): stated in S as Code's reading and flagged.
  - O9 (CV form): field `probe.cv` was added: 'loso' (n §3) or 'kfold-<k>'.
  - O10 (stale docstring lines): S:1, S:5–7 and `SchemaError`'s docstring were rewritten.
  - O11 (minor gaps):
    - a cell whose arm has no `per_arm` entry is refused, with a refusal case;
    - `stop.detail` is checked as one line;
    - `merged` is restricted as in item 28.
  - O12 (three blank lines): removed.
  - O13: noted; nothing to apply.

## Pass 2 (the v4.1 draft), as returned

Values-check of the schema's second commit: the module draft (sha256 098ecefa…94f1) and the entry draft. I followed the brief's rules. I ran no Python, wrote no file and did not list, read or search anything under data/. Every git command was scoped to the paths I needed, and every search used ':!data/**'.

ITEMS

1. Digests: the draft is 098ecefa…94f1 and the predecessor at 5a97527 is 77c12d6d…94bc (E:2–3). Source: shasum of the draft, and `git show 5a97527:valence_core/n/schema.py | shasum -a 256`. The scratch copy schema.5a97527.py hashes the same (git rev-parse and hash-object agree). CONFIRMED.

2. "The schema's second commit" (E:1) and "first committed at `5a97527`" (S:1). Source: `git log -- valence_core/n/schema.py` lists only 5a97527, and the tracked file is clean. CONFIRMED.

3. The diff only adds, except in five docstring passages (E:5–11 and the brief's list). Source: diff of the copy against the draft.
   - Five changed hunks: 1c1 (first line); 6,7c6,7; 16,17c16,19 (the sentence at old 16–17); 126,127c128,173 (the old EXAMPLES paragraph, now the two forms' paragraphs plus the rewritten EXAMPLES); 209,210c256,257 (SchemaError's docstring).
   - Every other hunk is a pure addition: 131a178 (import json), 910a958,1069, 912a1072,1335, 922a1346,1350 (in `__all__`), 1041a1470,1552 and 1331a1843,1982.
   CONFIRMED.

4. check_record, check_cell, check_stage_identity and the record, cell and identity tables are unchanged (E:20). Source: old lines 211–910 and new lines 258–957 hash equal, as does every other unchanged range. The new NESTED registrations (S:1173–1178) add 18 type names. None of them is used by those tables, and none overwrites an existing key. CONFIRMED.

5. The "Added" list (E:13–18). Source: the hunks above. IMPRECISE (minor): E:15's "the report's nested checks" also covers the G-READ-n artifact's checks (gread_campaign, gread_probe, lr, gread_results, layer_results, comparator). Suggested wording: "the report's and the artifact's nested checks".

6. Counts: 177 = 42 accepted + 135 refusals, with 16 new accepted cases and 53 new refusals (E:3, E:17, E:80). I counted call sites.
   - Draft: 23 accept sites. 20 are single calls; three loop, over the 10-entry `good` dict (S:1604), a 7-tuple (S:1855) and a 5-tuple (S:1944). 20 + 10 + 7 + 5 = 42. There are 135 refuse sites, none in a loop.
   - 5a97527: 17 accept sites (16 + the same 10-entry loop = 26) and 82 refuse sites.
   - RESULTS.md:421 records 26 + 82 at 5a97527.
   CONFIRMED.

7. The example builders produce objects that pass the checks. I traced all 16 new accept cases: rep, rep_pause, rep_adj, rep_cap, rep_gver, rep_end_binom, example_report(ext), the identity-sha case, gr, gr_mixed, rep_pistop, rep_render, rep_also, rep_resumed, rep_pause_cap and gr_merged. Each meets every table and invariant. For example, the comparator's max is the same expression as its last band median, and the median of two equal AUCs is exact. CONFIRMED.

8. Each of the 53 new refusals is refused by the check its case names. I traced each mutation to the first check that fails. Examples: "planned not the plan's" fails at S:1203, before the obtained check; "COMPLETE over a standing pause" fails at S:1269, before S:1275. st5.txt:83–135 shows the same messages and :136 reads 177/177; I used it as support only. CONFIRMED.

9. VALID_CELL_NAMES has "136 names" (S:972). Counted from ARM_CELLS (S:230–239): N1-V 5 + 1, N1-R 24 × 5, N1-P 2, N2-E, N2-S and N2-C 2 each, N4-T 1, N4-Ts 1. That is 136, all distinct. CONFIRMED.

10. GREAD_LR = {seed 7, iters 300, rate 0.1, l2 0.01} (S:970–971; E:55–56). Source: valence_core/echo/probe.py:19, `LR_SEED, LR_ITERS, LR_RATE, LR_L2 = 7, 300, 0.1, 1e-2` (fit_lr at :22–23). CONFIRMED.

11. identity_sha256 gives m's canonical bytes on a valid identity (S:1073–1074; E:23–24). Source: valence_core/m/resume.py:183–185.
    - `_canon` calls json.dumps with sort_keys, separators (",", ":"), ensure_ascii False, default=_refuse and allow_nan False.
    - identity_sha256 uses the same arguments except `default`. json calls `default` only for a non-native object, and a valid identity holds none: exact types, finite floats, str keys.
    - `_canon` returns a str, so the hashed bytes are its UTF-8 encoding, which is how both drafts word it.
    CONFIRMED. The accept case at S:1861–1864 recomputes with the module's own json.dumps call, not `_canon`.

12. The PASS rule (S:167–169, S:1286–1287; code S:1329–1333; E:67–70), against n §3 and k §1.4 G3.
    - n:121: "PASS iff the band median AUC ≥ .90 … and above the comparator's band".
    - PROPOSAL-k-echo-channel.md:263–264: "PASS iff median AUC over L51–L62 ≥ .90 and above the shuffle 95th percentile at every layer in the band".
    - The code requires median ≥ .90, median > the comparator's max, and every layer's auc > null_p95.
    - Both drafts label it Code's reading: S:167, S:1286 and E:67.
    CONFIRMED.

13. "n §3 gives the first two conditions" (E:70). Source: n:121. IMPRECISE: n §3's second condition is "above the comparator's band", and "above the comparator's largest" is Code's reading of it. Suggested: "n §3 gives the first two (≥ .90; 'above the comparator's band', read as above the largest of its 24 band medians)".

14. n §6's "the arm's launches" (S:137, E:71). Source: n:148, "Every pause STOPs the arm's launches until adjudicated". CONFIRMED.

15. A fired monitor ends the invocation for every arm (S:136–137, E:71). Source: valence_core/n/runner.py:15–17 (its PIN, "a fired monitor ends the invocation, all arms with it") and :235–238 (`break` out of the plan loop on the first kind that fires). CONFIRMED.

16. A rendering mismatch during a stage is a pause, and G-VER's is a G-VER-STOP (S:140–141, E:72). Source: n:148 lists "a rendering mismatch" among the pause-and-adjudicate triggers; n:119 gives G-VER "mismatch → STOP". CONFIRMED as sourced.

17. Code's readings are flagged in both drafts (E:67–75). IMPRECISE. The module flags four: S:132 (non-finite reads), S:136–137 (the fired monitor), S:143–144 (the cap) and S:167 (the PASS rule). It does not flag two that the entry flags:
    - the rendering split (S:140–141);
    - the CV form admitting 'kfold-<k>' (S:160–161, S:1055) beside n:121's "grouped leave-one-session-out CV".
    Add "(Code's reading, flagged)" at both places.

18. The CV form admits a grouped k-fold and records which one ran (E:75). Source: S:974 (`loso|kfold-[0-9]+`), S:1055 and S:1297–1298. CONFIRMED.

19. The end-state code matches the stated rules (S:147–156; E:38–44). Source: S:1256–1258 and S:1267–1276. Working through them:
    - with a STOP record, the end state is that STOP's kind;
    - otherwise a standing pause forces PAUSE;
    - otherwise a hit cap forces CAP;
    - otherwise the end is COMPLETE, refused at the campaign while an arm is incomplete.
    S:1281–1282 adds S:156's rendering rule. Every "iff" holds in both directions. CONFIRMED.

20. Completeness of the end states over the brief's ways to end, by reading the code:
    - the plan done: COMPLETE, or CAP if the last read reaches the cap, or PAUSE if the end-of-run evaluation fires;
    - a pause fired, cap hit or not: PAUSE;
    - the cap hit, then the end-of-run evaluation: PAUSE if it fires (a no-read fidelity-binomial pause, accepted at S:1232), otherwise CAP;
    - a PI stop at any point, over a standing pause or not: PI-STOP;
    - G-VER's mismatch before any read: G-VER-STOP;
    - a rendering mismatch during a stage: PAUSE, or PI-STOP;
    - a resumed invocation: one of the above.
    Each way has exactly one valid end state, and no combination has two. Only two combinations have none:
    - G-VER-STOP over a standing pause, which cannot arise while G-VER precedes every read and a resume follows a ruling;
    - at the campaign, no pause, no cap hit, no STOP and an arm incomplete, which arises only from an ending outside the list (see observations).
    CONFIRMED, except for item 21.

21. A rendering pause followed by a resumed invocation after its ruling. Source:
    - S:268: launch_index is "the read's place in the stage's run order (skip-only resume, n §2.8)";
    - S:140: a rendering mismatch during a stage is a pause;
    - S:1003: resumed_at is "the first read launched after the ruling took effect";
    - S:1235 refuses a launch_index ≤ the previous pause's; S:1241 refuses ra ≤ the pause's launch_index.
    The refused read is not on disk, so a skip-only resume at the same root re-launches it at the pause's own launch index.
    - If it fires again (the same mismatch, or any monitor), the new pause repeats that index and S:1235 refuses every report, whatever its end state.
    - If it succeeds, the read that PAUSE_FIELDS calls "the first read launched after the ruling" cannot be recorded, because S:1241 requires a later index.
    FAIL (a corner case, reachable under the drafts' own rules). Fix: for a rendering pause, allow the next pause's launch_index and resumed_at_launch_index to equal its own. Or state that a rendering pause is never resumed at the same root.

22. A binomial fire on a read that fires another trigger. Source:
    - S:139–140: "A read that fires two triggers is one pause: its kind by the precedence rendering, nonfinite, identity-bound, fidelity-binomial, and the rest in also_fired";
    - S:142: "every fire is a pause";
    - S:1024: fires are "evaluations that fired; each is a fidelity-binomial pause";
    - S:1001: binomial is set "on a fidelity-binomial pause … null otherwise".
    The checks:
    - S:1225–1227 accept fidelity-binomial in also_fired;
    - S:1243–1244 allow a batch only when the pause's kind is fidelity-binomial;
    - S:1254–1255 require fires to equal the number of pauses of that kind.
    The cadence evaluation can fire on an identity-bound read, which is a finite re-computation and so a trial. The pause's kind is then identity-bound, `fires` must stay 0 although an evaluation fired, and the batch cannot be recorded. FAIL. Fix either way:
    - count the fire, and require the batch, whenever fidelity-binomial is the kind or in also_fired, and reword S:1001, S:1024 and E:34 to match;
    - or refuse fidelity-binomial in also_fired, and say the binomial always fires as its own pause.

23. "No margin or other per-read value — counts, states and sha256s" (S:128–129, E:21–22). Source: the report tables at S:977–1030. IMPRECISE: the report also carries the stage identity (its dose-map figures, TAU and the identity bound), read ids and launch indices, ms figures, the binomial's alpha and a one-line STOP detail. Suggested: "no margin or other per-read model output: the identity, counts, states, read ids, launch indices, ms figures and sha256s".

24. The counter meanings. S:991 calls the counters "n §4's counters, over every read on disk", and S:1035 describes rendering_mismatches as "token sequences refused before a read (a STOP each)". Source: S:140–141, S:156, S:1281–1282 and n:128. IMPRECISE:
    - in this version a rendering mismatch is a G-VER-STOP or a rendering pause, not "a STOP each";
    - rendering mismatches are not reads on disk;
    - identity_out_of_bound is not one of n §4's counters (S:145 and E:37 already say this correctly).
    Suggested: S:1035 "(each a G-VER-STOP or a rendering pause)"; S:991 "n §4's counters and the identity-bound count".

25. Invariants the code enforces that the text does not state, and the reverse. IMPRECISE: state the first group; the second is for the reader or the runner.
    Enforced but not stated:
    - a STOP detail of at most 200 characters (S:1259; S:1018 says only "one line");
    - merged labels limited to +d_20 and +d_eq on valence and to none on span_reward (S:975, S:1307–1310); neither draft's prose mentions a result's `merged` field;
    - per_arm non-empty (S:1081), with an entry for every cell's arm at every stage (S:1208–1209);
    - per_layer in the probe's layer order (S:1322);
    - a binomial batch with first ≤ last, n > 0 and 0 < alpha < 1 (S:1249–1250).
    Stated but not enforced:
    - "in launch order" for a no-read binomial pause: its place in the list is unchecked;
    - the link between arms_in_scope and the arm of the read that fired;
    - any tie between binomial_state and the batches or counters.fidelity. The example rep_end_binom has a batch with k = 1 beside binomial_state.exceed_tau = 0.

26. "Every field the read runner and its stages write" (S:6). Source: STAGES (S:187) are campaign, time and backend-ext, while G-READ-n's artifact is written after the campaign by G-READ-n (n:121; n:159, step 15). IMPRECISE (minor). Suggested: "the read runner, its stages and G-READ-n write".

27. A NOT-RUN for no arm complete is derived from the report (S:18–19, E:51–52). Source: n:134, "…locked and produces no arm's full read set before a PI stop, a G-VER STOP or its cap". The report carries those three end states and per_arm.complete. CONFIRMED. The name `n-not-run-v1` (S:18, E:51) is NOT CHECKABLE: it is session traffic, and no tracked file names it.

28. The report's contents (S:130–145, E:23–37) against the tables at S:977–1038. CONFIRMED. E:34's "on a binomial fire, its batch" is subject to item 22.

29. Obtained counts reads "finite or not", and complete means the obtained read_ids equal the plan's (S:126, S:131, E:46). Source: S:1088 (complete iff obtained == planned), S:1211–1213 (obtained = the sum of its cells' records), and S:1182–1183 (matching the cells against disk is the reader's job). CONFIRMED.

30. The G-READ-n artifact's contents (S:158–165, E:53–66). Source: S:967, S:1039–1069 and S:1299–1320 against n:121, which gives the + pole against the − pole "where both exist, else the +pole from the shadow", 24 random directions, 200 shuffles and .90. CONFIRMED.

31. Q5 (E:77–79). Source: results/raw/2026-11-16_n-schema_code-to-design_questions.md:176–214, committed at 718c48e. Its line 214 reads: "Readings (a), (b) and (d) change the schema's `capture_layers` check, a follow-up schema commit." No reading changes a field of the G-READ-n artifact, since probe.layers is a free list. CONFIRMED.

32. The forms meet the needs stated in n-analyzer's committed block. Source: results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md.
    - :80: the analyzer "reads G-READ-n's status and band median AUC per axis and dose as given";
    - Q4 (:31–35): G-READ-n at +1, at d_eq and for span_reward at 0.20;
    - Q6 (:43–49): per-arm completeness, and pauses standing on an arm's reads;
    - A.4 (:106): the no-arm NOT-RUN causes (PI stop, G-VER STOP, cap).
    The forms carry status and band median per (axis, point), per_arm.complete, each pause's arms_in_scope and adjudicated flag, and the three end states. CONFIRMED.

33. NOT CHECKABLE (session traffic or acts still to come):
    - the agreement with n-analyzer (E:3–4, E:38, E:45; S:128, S:147, S:158, S:960, S:1074);
    - the PI's routing of 2026-11-16, N.9 (E:68);
    - the self-test's run, window, nice level, interpreter and scratch copy (E:81–83);
    - the two `--version` calls and their disclosure (E:83–85);
    - "Nothing ran on a model" (E:4);
    - the commit itself (E:86–88).
    st5.txt supports 177/177 but is not tied to the draft's sha256.

OBSERVATIONS

- One of my diff outputs was too long to display, and the harness saved it to its own tool-results folder for this session, outside the repository and the scratch folder. I did not open it, and re-ran the diff in smaller pieces. I wrote nothing.
- The runner draft differs from this schema (not FAILs of these drafts):
  - runner.py:40–41: END_STATES has "STOP" and no "G-VER-STOP"; PAUSE_KINDS lacks "rendering" and lists fidelity-binomial first;
  - :24–25: a rendering mismatch is a per-read STOP;
  - :239: the end-of-run binomial is evaluated only when the plan completes, not after a CAP;
  - its result carries one `pause`, not n-report-v1's list.
- Unchanged code keeps the old wording: check_record's message at S:843 still says "a rendering mismatch is a STOP, never a record".
- Some endings fall outside the brief's list: an exception, a record the writer refuses, a kill or a lost box. At the campaign, with an arm incomplete and no pause, cap or STOP, such an ending has no valid end state. S:128 and E:21 ("written at every invocation's end") should say that such an invocation writes no report. Neither draft says whether rendering_mismatches counts per invocation or per stage. If per stage, any later report at a root that had a G-VER-STOP would be refused.
- n §4–§6 needs that no field carries directly:
  - per-(arm, point) completeness for n:138's "the points are incomplete", which can be derived from the cells against read_plan;
  - how arms_in_scope is set for each pause kind, which n §5's INDETERMINATE clauses read;
  - the binomial's declared p0 and its tail probability (the batch holds only p0_count, p0_n and alpha);
  - NaN/inf margins kept apart from non-finite fresh paths, which nonfinite_reads merges;
  - the label-mass counter, null unless the lock sets a floor, while the analyzer's block (:92) declares .20.
- Under the encoded capture_layers [site, last] and Q5's fact, the every-layer clause alone makes PASS unreachable, beyond Q5's 0.75 ceiling: the site layer equals the shadow's under both contrasts.
- N1-R reads no program-scale point, and neither draft says which comparator serves span_reward's f0.10 and f0.20. A computed result without a comparator is a FAIL (S:168).
- Neither draft flags as a reading the pause precedence and one-pause-per-read rule (n §6 gives no precedence), or the pin of k's fit_lr hyperparameters (n:121 names none).
- check_report accepts a cell name for a merged-away label, and at stages other than the campaign it accepts COMPLETE with obtained < planned, as S:154–155 states.
- The comment at S:1928, "# v4: …", names a scratch draft rather than a commit. E:86 still holds the placeholder VALUESCHECK_LINE.

## Code's dispositions of pass 2

Pass 2 read the v4.1 draft (sha256 `098ecefa…94f1`) and its entry. Both FAILs, items 21 and 22, had already been
found and fixed by Code while the pass ran. They surfaced while syncing the runner to the report form, and the fixes
were in the v4.2 draft (`80dab6f2…`), which pass 2 did not see. Every other IMPRECISE item and every observation that
asked for a change is applied in v4.3 (`6575c20a…f371`) or in the entry. "S" is the module; "E" the entry. Each
disposition states the wording at v4.3. Pass 3's dispositions revise item 17's CV-form flag: v4.4 admits n §3's
leave-one-session-out only.

- **Item 5, IMPRECISE (E: "the report's nested checks").** Applied in the checker's words: "the report's and the
  artifact's nested checks".
- **Item 13, IMPRECISE (E: "n §3 gives the first two conditions").** Applied. E now gives n §3's own words, "above
  the comparator's band", and says it is read as above the largest of the 24 band medians. S's PASS paragraph quotes
  n §3's phrase beside "above the comparator's largest".
- **Item 17, IMPRECISE (two readings flagged in E but not in S).** Applied:
  - S flags the rendering split, quoting n §6's list and n §3's "mismatch → STOP";
  - S flags the CV form's grouped k-fold.
  - Following the observation about readings no draft flagged, S also flags the pause precedence and
    one-pause-per-read rule (n §6 gives no precedence) and the `GREAD_LR` pin (n §0.10's B3, "k's form and bar").
- **Item 21, FAIL (a rendering pause cannot be resumed at its own place).** Fixed in v4.2, along the checker's first
  suggested line:
  - a rendering pause's `resumed_at_launch_index` may equal its own launch index;
  - a later pause may share a rendering pause's place;
  - a rendering pause fires nothing else (its `also_fired` must be empty).
  Cases: an accept case (a rendering pause's read launched at its place after the ruling, then pausing) and refusals
  (a rendering pause that fired another kind; a second pause at a non-rendering pause's place).
- **Item 22, FAIL (a binomial fire on a read that fires another trigger cannot be recorded).** Fixed in v4.2, along
  the checker's first suggested line:
  - the batch is required whenever the binomial is the pause's kind or in `also_fired`;
  - `fires` counts those pauses;
  - a fire at a read ends its batch at that read;
  - S:1001, S:1024 and E's pause list are reworded.
  Cases: accept cases (a non-finite pause whose read also fired the binomial; a binomial fire at a read) and
  refusals (a binomial in `also_fired` without its batch; a batch not ending at its read).
- **Item 23, IMPRECISE ("no margin or other per-read value -- counts, states and sha256s").** Applied in the
  checker's words in S and E: "no margin or other per-read model output: the identity, counts, states, read ids,
  launch indices, ms figures and sha256s".
- **Item 24, IMPRECISE (the counters' descriptions).** Applied:
  - `counters`: "n §4's counters and the identity-bound count, over the stage";
  - `rendering_mismatches`: "token sequences refused before a read, never a record: the stage's rendering pauses, or
    at a G-VER-STOP G-VER's mismatches" (the "a STOP each" wording was already gone in v4.2);
  - `nonfinite_reads`: "a non-finite margin, cached or fresh".
- **Item 25, IMPRECISE (invariants enforced but not stated, and the reverse).**
  - Enforced but unstated, now stated in S:
    - the STOP detail's 200 characters;
    - `merged`'s limits;
    - `per_arm`, non-empty with every cell's arm in it;
    - `per_layer` in the probe's layer order;
    - the batch's well-formedness.
  - Stated but unenforced:
    - a read-less binomial pause must be the last (enforced since v4.2);
    - a pause's scope now must hold its read's arm (new check). Which other arms it holds stays the runner's, flagged
      as its SCOPE pin;
    - `binomial_state`'s trials and exceedances must be the fidelity counters' totals, and every batch's k and n must
      be within them (new checks).
  - `example_report`'s fixture was made consistent: its exceedances now cover its batches. rep_end_binom's batch
    (k = 1) now sits beside `exceed_tau` 1; no case was removed.
  - Cases: refusals for a pause whose scope lacks its read's arm, a `binomial_state` off the counters' totals, and a
    batch beyond the stage's exceedances.
- **Item 26, IMPRECISE ("the read runner and its stages write").** Applied: "the read runner, its stages and
  G-READ-n write".
- **Also in v4.2–v4.3, beside the items above:**
  - two case renames, "a batch on a non-finite pause that did not fire it" and "a rendering mismatch without a
    G-VER-STOP or a rendering pause";
  - field-description edits: the report's `cells`, the probe's `cv` in the artifact's field list, `results`, and
    the comparator (a computed result with nulls is a FAIL);
  - the refusal of `resumed_at_launch_index` on a read-less pause, with its two read-less cases (a read-less pause
    that is not the last; a read-less pause with a resumed_at).
- **Observations:**
  - The runner draft's differences (its END_STATES, the per-read STOP, no end-of-run evaluation after a CAP, one
    `pause`): resolved in the runner's sync, drafted in scratch. It is not under this commit; the BUILD entry
    carries it.
  - check_record's message ("a rendering mismatch is a STOP, never a record"): reworded in v4.2 to "never a record (a
    pause during a stage; a G-VER-STOP at G-VER)". It is the one change since 5a97527 to the record, cell and identity
    checks, a message only. E says so.
  - Endings outside the brief's list: S now says that an invocation ending otherwise writes no report, and that the
    next invocation's replay finds what it left. It also says `rendering_mismatches` counts per stage, and that
    nothing resumes after a STOP.
  - n §4–§6 needs that no field carries:
    - per-(arm, point) completeness: derivable from the cells against read_plan; the reader's;
    - each pause kind's scope: the runner's SCOPE pin, flagged;
    - the binomial's p0 and tail: derivable from the batch's k, n, p0_count and p0_n;
    - NaN/inf margins kept apart: the record keeps `finite` and the fidelity block's `finite` apart, so the reader
      can split them;
    - the label-mass floor: the lock's.
    None changes a field.
  - The every-layer clause and Q5: under the encoded capture layers the site layer equals the shadow's, so PASS is
    unreachable. E says so beside Q5, and the BUILD flags it.
  - The comparator for span_reward: S now states Code's reading, flagged. The random directions at +d_eq and +d_20
    (or the points they merged into) serve f0.10 and f0.20, which the dose map norm-matches to them, except where
    d_20 is capped at 1.
  - Cell names at merged-away points: now refused at every stage, with an accept case on a merged dose map and a
    refusal for a cell at the merged-away +d_eq.
  - COMPLETE with obtained < planned outside the campaign: left as stated. Only the campaign's reports enter
    verdicts.
  - The "# v4: …" comments: renamed to say what the cases test.
  - The `VALUESCHECK_LINE` placeholder: filled before the commit.

## Pass 3 (the v4.3 draft, the entry and the dispositions), as returned

Values-check of the schema's second commit: the module draft v4.3 (S), the entry draft (E) and Code's two dispositions files (D3, D41). I ran no Python, wrote no file, and listed, read and searched nothing under data/. Every git command named its paths. Sources are cited as n:N (PROPOSAL-n-bk-reconciliation-v0_2.md), k:N (PROPOSAL-k-echo-channel.md), questions.md (results/raw/2026-11-16_n-schema_code-to-design_questions.md) and prebuild.md (results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md).

ITEMS

1. Digests (E:2). S hashes to 6575c20a…f371 and the v4.1 draft to 098ecefa…94f1. The copy schema.5a97527.py and `git show 5a97527:valence_core/n/schema.py | shasum -a 256` both give 77c12d6d…94bc, and git rev-parse at 5a97527, git rev-parse at HEAD and git hash-object of the tracked file give the same blob. CONFIRMED.

2. "The schema's second commit" (E:1) and "first committed at `5a97527`" (S:1). `git log -- valence_core/n/schema.py` lists only 5a97527. CONFIRMED.

3. Against 5a97527 the diff only adds, except in six rewritten places (E:5–14). Source: diff of the copy against S.
   - It has six change hunks, removing 10 lines in all: 1c1; 6,7c6,8; 16,17c17,20; 126,127c129,198 (the old EXAMPLES paragraph, replaced by the two forms' paragraphs and the new EXAMPLES); 209,210c281,282; 796c868,869.
   - Every other hunk is a pure addition: 131a203, 910a984,1341, 912a1344,1394, 922a1405,1409, 1041a1529,1613, 1331a1904,2085.
   - E's quote of the old message matches 5a97527:796. The condition line (5a97527:795 = S:867) is unchanged.
   CONFIRMED.

4. The "Added" list (E:16–22). Source: the addition hunks above. CONFIRMED.

5. Apart from that message, the record, cell and identity forms and checks are unchanged (E:24). Source: old lines 211–795 and 797–910 are untouched. The 18 type names registered into NESTED (S:1207–1211) collide with none of NESTED's 9 old keys or `_check_type`'s 13 names, and no old table uses them. CONFIRMED.

6. All but two of the eleven names are byte-identical to 5a97527's (E:24–27). I extracted each definition from both files and compared sha256s.
   - Identical: CELL_SCHEMA (137 / S:209), TOLD_LINE with its comment (196–198 / S:268–270), cell_filename (385–389 / S:457–461), read_plan (430–446 / S:502–518), dose_points (588–629 / S:660–701), dose_point_values (632–641 / S:704–713), check_cell (883–910 / S:956–983), example_identity (929–953 / S:1416–1440), example_record (956–1030 / S:1443–1517).
   - Different: check_record (only hunk 796c868,869) and SchemaError (its docstring).
   CONFIRMED. That these are the names n-analyzer calls, and "Code checked this by tool and told n-analyzer" (E:27–28): NOT CHECKABLE, session traffic.

7. The counts (E:3, E:21, E:103), by call sites:
   - S has 26 accept sites: 22 single calls plus loops over the 10-entry `good` dict (S:1665), the 7-tuple (S:1916), the 5-tuple (S:2005) and the 2-tuple (S:2065), so 46. It has 145 refuse sites, all at the self-test's top level. 191 = 46 + 145.
   - v4.1 has 23 accept sites (20 + 10 + 7 + 5 = 42) and 135 refuse sites.
   - 5a97527 has 17 accept sites (16 + 10 = 26) and 82 refuse sites, as RESULTS.md:421 records.
   - Since 5a97527 the self-test grew by one pure insertion (1331a1904,2085), so it has 20 new accepted cases and 63 new refusals. v4.1→v4.3 removes no case and renames two (S:1950, S:1968), so 4 new accepted cases and 10 new refusals.
   CONFIRMED.

8. The example builders' objects pass, now that the counters and binomial state follow the batches. I traced all 20 accept cases that build a report or an artifact against S:1113–1392.
   - rep_end_binom: exceed_tau is now 1, equal to its batch's k, with exceed_tau4 3, fires 1 and evaluations 1.
   - rep_nf_binom and rep_binom_read: the batch's last index is 500, equal to the launch index; k 1 ≤ 1 and n 160 ≤ 160.
   - rep_retry: p02 at 500 is accepted after the rendering p01, whose resumed_at is 500.
   - rep_m: d_eq = 4/7.65 ≈ 0.5229 folds into +1/2 and d_20 = 1.0 into +1; its cells come only from the merged plan.
   - The other cases: rep, rep_pause, rep_adj, rep_cap, rep_gver, the backend-ext report, the identity-sha case, rep_pistop, rep_render, rep_also, rep_resumed, rep_pause_cap, gr, gr_mixed and gr_merged. The comparator's max is the same expression as its 24th median, and (0.96 + 0.96)/2 is exact.
   CONFIRMED.

9. Each refusal is refused by the check its case names.
   - The 10 new against v4.1, case → check:
     - S:2050 → S:1267
     - S:2052 → S:1281
     - S:2055 → S:1278
     - S:2057 → S:1288
     - S:2068 → S:1293
     - S:2070 → S:1303
     - S:2077 → S:1271
     - S:2079 → S:1312
     - S:2081 → S:1305
     - S:2083 → S:1245
   - Two old refusals sit on the changed base rep_end_binom: S:1952 → S:1293 and S:1954 → S:1300.
   - The other 53 report and artifact refusals still reach their named checks first; no v4.3 check intercepts them. For example, S:1956's no-read pause fails at S:1275 before the new last-pause check at S:1278.
   - st6.txt holds 145 refusal lines, in the code's case order, with the same messages, and ends "191/191". I used it as support only.
   CONFIRMED.

10. Changes in the v4.1→v4.3 diff that no disposition names. Every other hunk maps to D41 items 5, 13, 17, 21, 22, 23, 24, 25 and 26 or to its observations, and no claimed change is missing from S.
    - The two case renames, at S:1950 and S:1968.
    - Field-description edits at S:1012–1014 (cells), S:1074 (the probe now lists cv), S:1075 (results) and S:1100–1101 (a computed result with nulls is a FAIL). Each agrees with S's docstring and E.
    - The refusal of resumed_at on a read-less pause (S:1288, "li is None") and its two read-less cases (S:2055–2059). Only S:155 and E:59 state these rules ("the stage's last pause and resumes nothing").
    IMPRECISE (minor). Suggest one line in D41 naming them.

11. D41's Applied and Fixed claims against v4.3. Source: S and E at the places each names.
    - Item 5: E:18.
    - Item 13: E:86–87 and S:191–192.
    - Item 17: S:146–147, S:150–152, S:178–180.
    - Item 21: S:1267, S:1281, S:1288–1289, with cases S:2045–2054.
    - Item 22: S:1292–1295, S:1303–1304, S:1309, S:1030–1031, S:1054 and E:44, with cases S:2061–2071.
    - Item 23: S:131–132 and E:30–32.
    - Item 24: S:1020 and S:1063–1067.
    - Item 25: S:138–139, S:148–149, S:159, S:183–184, S:186 and S:1010–1011, with the checks S:1271, S:1278, S:1305 and S:1312 and cases S:2077–2082.
    - Item 26: S:6.
    - The observations: S:129–131, S:161–162, S:187–189, S:1245, S:1989 (no "v4" string is left in S) and E:12–14.
    CONFIRMED, except item 12.

12. "The case with k = 1 beside `exceed_tau` 0 is gone" (D41:54–55). No case was removed: rep_end_binom (S:1914–1915) remains, and example_report now gives it exceed_tau 1 (S:1560–1567). IMPRECISE. Suggest: "rep_end_binom's batch (k = 1) now sits beside exceed_tau 1; no case was removed."

13. The v4.2 statements (D41:3–6, :18, :25, :39, :49, :64): the fixes "in v4.2 (80dab6f2…)" and "already gone in v4.2". NOT CHECKABLE: there is no v4.2 draft. Every fix named is present in v4.3.

14. D3's Applied claims against v4.3. CONFIRMED, apart from the stale wordings in item 15.
    - Items 6, 7 (the sentence at S:17–20), 17, 19 (S:1259; case S:2040), 22, 23, 24 (136 names, S:998–999; cases S:1972, S:2027), 26, 27, 28, 31, 32, 33, 34 (questions.md:214), 37 and the 200-character check of item 13.
    - O1, O2, O4, O5, O8, O9, O10 and O11.
    - O12: no run of three blank lines, and no line over 120 characters.
    - n:99 confirms D3:31–32: §2.6 gives a floor only for N-lap's f = 0.20.

15. D3 wordings later superseded, correct at v4 but stale against v4.3:
    - D3:7–8 quotes "the report's nested checks"; E:18 now reads "the report's and the artifact's", per D41:8–9.
    - D3:13 says "among the five rewritten ones"; E:5 now has six, the sixth being check_record's message (D41:64–66).
    - D3:14–15 quotes "no margin or other per-read value -- counts, states and sha256s"; the wording is now D41:33–35's.
    - D3:67–68 says fires equal "the number of fidelity-binomial pauses"; they now count pauses whose read fired the binomial (D41:28).
    IMPRECISE. Suggest a line at D3's head: "D41 revises items 5, 7, 13 and O6."

16. The quotes and attributions in S and E.
    - n §6's trigger list, "a rendering mismatch", "the arm's launches" and the absence of a precedence (S:143–147, S:151, E:90–91): n:148. Its fifth trigger, N-lap's 5(d) gate, is not N-pod's, so PAUSE_KINDS covers N-pod's four.
    - n §3's "mismatch → STOP" (S:152): n:119.
    - "above the comparator's band", "grouped leave-one-session-out", 200 shuffles and .90 (S:192, S:180, S:1085–1089, E:86, E:95): n:121.
    - n §0.10's B3, "k's form and bar" (S:179, E:96): n:48.
    - k §1.4 G3, "above the shuffle 95th percentile at every layer in the band" (S:192–193, E:87–88): k:263–264.
    - n §4's four counters: n:128.
    - The contrast (E:79): n:121.
    CONFIRMED.

17. GREAD_LR and E:70–71. Source: valence_core/echo/probe.py:19, `LR_SEED, LR_ITERS, LR_RATE, LR_L2 = 7, 300, 0.1, 1e-2`. The check refuses any other value (S:1354). CONFIRMED.

18. identity_sha256 gives `_canon`'s bytes on a valid identity (E:33–34, S:1107–1110). Source: resume.py:183–185. The arguments are the same except `default`, which is never called on the exact native types check_stage_identity admits. It is not `json_text`'s form (:203–208). CONFIRMED.

19. The report's preamble and contents (E:29–48; S:129–163). Source: REPORT, PAUSE, BINOMIAL, STOP, CAP and COUNTERS fields (S:1004–1070). CONFIRMED, except E:44 (item 22). "Writes none … the replay finds what it left" is the runner's design: NOT CHECKABLE as behaviour.

20. The end-state rules (S:165–174; E:49–55). Source: code S:1316–1341. Once the other fields are fixed, the end state is determined:
    - with a STOP record, it is that record's kind (S:1316);
    - otherwise a standing pause forces PAUSE (S:1326, S:1328);
    - otherwise a hit cap forces CAP (S:1330, S:1332);
    - otherwise it is COMPLETE, which needs every arm complete at the campaign (S:1334).
    Every "iff" holds in both directions, and no combination admits two end states. CONFIRMED.

21. One valid report for each way an invocation ends, by reading.
    - (a) The plan done: COMPLETE. CAP if the last read reached the cap. PAUSE if a pause or the end-of-run fire stands.
    - (b) A pause fired, cap hit or not: PAUSE (rep_pause, rep_pause_cap).
    - (c) The cap hit, then the end-of-run evaluation: PAUSE if it fires, with a read-less last pause; CAP if not. After that ruling, a resume that launches nothing ends CAP. This holds only if the runner does not fire the end-of-run evaluation again: a second read-less pause leaves the first one not last (S:1278), and every report is then refused.
    - (d) A PI stop, over a standing pause or not: PI-STOP. PAUSE is then refused (S:1316).
    - (e) G-VER's mismatch before any read: G-VER-STOP (rep_gver). G-VER-STOP over a standing pause has no valid report; it cannot arise while G-VER runs before the stage's first read.
    - (f) A rendering mismatch during a stage: PAUSE.
      - After the ruling, the read launches at li, and resumed_at = li is accepted (S:1288–1289).
      - If the relaunched read fires another trigger, or the same mismatch recurs, the second pause shares li (S:1281; rep_retry).
      - When the mismatch recurs, nothing was launched, and the first pause's resumed_at passes as either null or li. The text (S:152–154) covers only the launched case.
    - (g) A binomial fire at a cadence point on a read that also fires nonfinite or identity-bound: one pause, its kind by precedence, the binomial in also_fired and its batch ending at li (rep_nf_binom). The reversed form and a two-pause form are refused (S:1264–1266, S:1281). A read firing three triggers has two accepted forms, because also_fired's order is free.
    - (h) A resume after any of these:
      - after a PAUSE ruling, it ends as one of (a)–(g), with resumed_at at the first launched read (> li; = li for a rendering pause; null if nothing launches);
      - nothing resumes after a STOP (S:162).
    - Outside the list: if a ruling does not launch a rendering pause's read, the campaign is left with an incomplete arm and nothing standing. COMPLETE is then refused (S:1334) and no valid report exists. This is consistent with S:142–143 and E:64–65: no ruling's effect on reads is recorded.
    CONFIRMED, with the notes in (c), (f) and (g).

22. The batch of the read-less end-of-run fire. The field description (S:1030–1031) reads "when the pause's read fired the binomial (its kind or also_fired) … ending at that read; null otherwise". S:147–149 and E:44 likewise speak only of a pause whose read fired. The code requires a batch on every fidelity-binomial pause, the read-less one included (S:1292–1295; refusal S:1952 on rep_end_binom). Read literally, the field says null there. IMPRECISE.
    - Suggested field wording: "on a fidelity-binomial pause, or one whose read also fired the binomial (also_fired), the batch it was computed on, ending at the pause's read where it has one; null otherwise".
    - Suggested E:44: "when the binomial fired, as its kind or in also_fired, the batch, which ends at the pause's read (a fire at the run's end has a batch and no read)".

23. rendering_mismatches "counts the stage's rendering pauses, or at a G-VER-STOP G-VER's mismatches" (S:161–162, S:1066–1067). The code checks only that a non-zero count has a G-VER-STOP or a rendering pause (S:1340). Two things pass: a rendering pause with a count of 0 or 2 (rep_render before S:1995 sets 1), and a G-VER-STOP with a count of 0. IMPRECISE. Either enforce equality outside G-VER-STOP and ≥ 1 at G-VER-STOP, or word the field as S:174 does ("counted only under a G-VER-STOP or a rendering pause").

24. "Every read after a pause's own was launched after its ruling; ``resumed_at_launch_index`` is the first of them" (S:143–145). Not enforced. Each of these passes:
    - an unadjudicated nonfinite pause at 500 followed by a nonfinite pause at 600;
    - a pause at 500 adjudicated with resumed_at 700, followed by a pause at 600;
    - an adjudicated pause with resumed_at null, followed by a later read pause.
    IMPRECISE. Either check that each pause before a later read-bearing pause is adjudicated, with resumed_at set and at most that pause's launch index, or say that this ordering is the runner's and the reader's.

25. The comparator for span_reward (S:187–189; E:88–89), against n:81's two scales and its map.
    - At a kept +d_eq the norm is d_eq·ρ·R = 0.10·R_ℓ, f0.10's. At a kept, uncapped +d_20 it is 2·d_eq·ρ·R = 0.20·R_ℓ, f0.20's.
    - The cap exception is right. A capped d_20 = 1.0 folds into +1, with norm ρ·R against 0.20·R_ℓ, a ratio of 2·d_eq, as prebuild.md:51 (Q7) has it.
    - For "the points they merged into", the match is not exact. The keeper's norm differs from f·R_ℓ by up to 0.05·ρ·R. For example, a d_eq in [0.45, 0.55] that folds into +1/2 is off by up to about 11%.
    IMPRECISE. Suggest: "…which the dose map norm-matches to them where they are kept, and to within the merge distance (0.05 on BK's scale) where they merged; not where d_20 is capped at 1".

26. The PASS rule. S:191–194 matches the code at S:1389–1390: median ≥ .90, median > the comparator's max, and every layer's AUC above its null_p95. E:85 ("The band median must be at least .90, above the comparator's band and above the shuffle null at every layer") reads as if the band median must clear each layer's null. k:263–264 shares that ambiguity. IMPRECISE (minor). Suggest: "The band median must be at least .90 and above the comparator's band, and every layer's AUC above its shuffle null."

27. Q5 (E:98–102). Sources: 718c48e (git log of questions.md); questions.md:214 for readings (a), (b) and (d); questions.md:184–188 (the fact) and :194–197 (the 0.75 ceiling); S:734 (capture_layers == [layer, n_layers − 1]); S:1088 (probe.layers is a free list).
    - Under the encoded layers, the site capture is at the injection index. The read position's residual there is the shadow's, both for the +1/−1 pair and for the +pole against the shadow.
    - The rows are identical within each session, so the site layer's LOSO AUC is exactly 0.5 (ties at 0.5, probe.py:6–7), and above_null fails whenever that layer's 200-shuffle 95th percentile is at least 0.5. In practice that is always; it is not guaranteed by construction.
    CONFIRMED. A note: the every-layer argument is the entry's own, beside Q5's ceiling.

28. The G-READ-n artifact's contents (E:68–82; S:176–189). Sources: GREAD fields (S:1071–1103) and n:121. CONFIRMED.

29. Code's readings flagged in S (E:83–96). All nine appear in S: S:191, S:189, S:143–144, S:147, S:150–152, S:136–137, S:159–160, S:180, S:178–179. CONFIRMED. The cap's reading at S:160 says "Code's reading" without "flagged".

30. The self-test (E:103–109).
    - The counts are CONFIRMED by call sites (item 7).
    - "--verbose prints each refusal's message" is CONFIRMED (S:1650–1651), but lines are cut at 220 characters: st6.txt:122, :123, :137 and :139 are cut.
    - v4.1's 177 matches its call sites.
    - NOT CHECKABLE: the run, the window, nice, the interpreter, the scratch copy, v4 (a1c85568…) at 173/173, and the --version calls and their disclosure.

31. Also NOT CHECKABLE:
    - the agreements with n-analyzer (E:2–4, E:49, E:60; S:129, S:165, S:176);
    - `n-not-run-v1` (S:19, E:66);
    - the PI's routing N.9 (E:84);
    - "Nothing ran on a model" (E:4), as an act;
    - the SCOPE pin (S:142; the runner is not a source);
    - VALUESCHECK_LINE and the commit (E:110–112).

OBSERVATIONS

- What the runner must do, as the schema implies:
  - evaluate the end-of-run binomial at most once per stage, so it never fires again on a resume;
  - run G-VER only before the stage's first read.
- The example fixtures carry counters their pauses contradict. No check ties these, so all pass, and the battery inherits them.
  - nonfinite_reads stays 0 beside nonfinite pauses (rep_pause and others).
  - identity_out_of_bound stays 0 beside rep_also's identity-bound trigger.
  - example_pause's read is always N1-V|valence|+1, a steered read, while n:148 has the identity bound "at d = 0".
  - example_gread probes layers (32, 63), but example_identity captures [31, 63].
- Minor gaps between code and text:
  - arms_in_scope must be non-empty on the read-less pause (S:1269), but no text gives that pause's scope;
  - duplicate arms in a scope pass;
  - G-READ results must be non-empty (S:1178), against "at most one" (S:182, S:1075);
  - a pause's read_id is checked only for its arm (S:1271);
  - CV_FORMS admits kfold-0 and kfold-1;
  - a G-VER-STOP report that carries records or pauses passes.
- A k-fold run's fold seed is not recorded. probe.py:78–109 takes a fold seed separate from the permutation seed, while the artifact keeps only cv and shuffle_seed.
- D41:73 calls p0 derivable from the batch's p0_count and p0_n. That assumes the lock's p0 is their ratio; with G-DATA (vi)'s 0 of 2,400, that p0 is 0 (n:77 has the lock declare p0).
- raw_v3check.md:1 calls the first check's draft "the schema v2 draft"; D3:3 calls it the v3 draft. The sha256 (d9bdd15f…2c45) is the same in both.
- 5a97527's entry listed "the NOT-RUN record" among this schema's later commits (RESULTS.md:408–409). S:18–20 and E:66 now place the clock NOT-RUN in n-analyzer's schema, without saying the plan changed.
- "Norm-matched" holds only to rounding: expected_alpha's two forms, d_eq·ρ·R and 0.10·R_ℓ, can differ in the last bits.
- How I worked:
  - I read only the listed drafts, raws, dispositions, st6.txt and sources, the latter including probe.py in full.
  - I ran one `git status --porcelain` scoped to named files; it printed nothing.
  - One paste used process substitution, which this shell maps to /dev/fd (checked: /dev/fd/12), so nothing was written.

## Code's dispositions of pass 3

Pass 3 read the v4.3 draft (sha256 `6575c20a…f371`), the entry and the dispositions of passes 1 and 2. It returned no
FAIL. Every IMPRECISE item, and every observation that asked for a change, is applied in v4.4
(`4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665`), in the entry or in the dispositions above.
"S" is the module; "E" the entry; "D3" and "D41" the dispositions of passes 1 and 2. No fourth blind pass was run. The edits after pass 3 were checked by tool: Code's read
of the v4.3 → v4.4 diff, the schema's self-test on v4.4, and the n package's self-test with the runner writing reports
under v4.4.

- **Item 10, IMPRECISE (changes no disposition named).** Applied: D41 now has a line naming them. They are the two
  case renames, the field-description edits, and the read-less pause's resumed_at refusal with its two cases.
- **Item 12, IMPRECISE (D41: "the case with k = 1 … is gone").** Applied in the checker's words: "rep_end_binom's
  batch (k = 1) now sits beside `exceed_tau` 1; no case was removed."
- **Item 15, IMPRECISE (D3's wordings later superseded).** Applied: D3's head now says that each disposition states
  the wording at v4, and that pass 2's dispositions revise its items 5, 7, 13 and O6 (pass 3's revise O9). D41's head
  says the same for v4.3.
- **Item 22, IMPRECISE (the read-less fire's batch).** Applied in the checker's words:
  - in the `binomial` field: "on a fidelity-binomial pause, or one whose read also fired the binomial (also_fired),
    the batch it was computed on, ending at the pause's read where it has one; null otherwise";
  - in S's docstring: "a binomial fire at the run's end has a batch and no read";
  - in E's pause list.
- **Item 23, IMPRECISE (rendering_mismatches looser than stated).** Applied as the checker's first option, enforced:
  - outside a G-VER-STOP the count equals the number of the stage's rendering pauses;
  - at a G-VER-STOP it is at least one.
  - Following the observation that a G-VER-STOP report may carry records or pauses, a G-VER-STOP now refuses any
    pause and any record ("a G-VER-STOP comes before any read").
  - `example_report` sets the count: 1 at a G-VER-STOP, otherwise its rendering pauses.
  - Cases: a rendering pause counted twice; a G-VER-STOP with no mismatch counted; a G-VER-STOP with a record.
- **Item 24, IMPRECISE (the interleaving of pauses and resumptions, unchecked).** Applied as the checker's second
  option:
  - S says the schema checks only that `resumed_at_launch_index` follows its own pause, and that the interleaving
    is the runner's to keep and the reader's to check;
  - S defines `resumed_at_launch_index` as the first read attempted after the ruling, launched or refused as a
    rendering mismatch.
  - The runner draft now computes it that way. Before, a resume whose first attempt was a rendering refusal left its
    pause's resumed_at null. The runner's self-test has a case for it.
- **Item 25, IMPRECISE (the comparator's norm match where points merged).** Applied in the checker's words in S and
  E: norm-matched where kept, to within the merge distance (0.05 on BK's scale) where merged, not where d_20 is
  capped at 1.
- **Item 26, IMPRECISE (E's PASS sentence).** Applied in the checker's words: "The band median must be at least .90
  and above the comparator's band, and every layer's AUC above its shuffle null."
- **Item 29 (the cap's reading not marked "flagged").** Applied: "(Code's reading, flagged; …)".
- **Item 30 (verbose lines cut at 220 characters).** Applied in E: "(each cut at 220 characters)".
- **Observations:**
  - The runner's duties the schema implies (one end-of-run evaluation, never re-fired on a resume; G-VER before the
    stage's first read): both are the runner draft's behavior. Its self-test covers the first, and the G-VER-STOP
    check now enforces the second's consequence. Neither changes a field.
  - The fixtures' counters:
    - `example_report` now counts the pauses that name nonfinite and identity-bound;
    - `example_pause` gives a pause that names identity-bound a d = 0 read;
    - `example_gread`'s layers are now (31, 63), `example_identity`'s capture layers.
    - New checks: `nonfinite_reads` and `identity_out_of_bound` must count at least the pauses that name them, and
      an identity-bound trigger must be a d = 0 read's (n §6). Each has a refusal case.
  - The minor gaps:
    - a scope may no longer name an arm twice (a check and a case);
    - a read-less fire's scope is stated as the runner's;
    - `results` now says "at least one, and at most one per (axis, point)".
    - The pause's read_id is checked only for its arm and, on an identity-bound pause, its dose. Its other parts are
      the reader's.
  - CV_FORMS admitting kfold-0 and kfold-1, and the k-fold run's fold seed not recorded: the CV form now admits n
    §3's "loso" only. A grouped k-fold, if the seat allows one for G-READ-n's cost, enters with its seeds in its own
    schema commit. The accept case that used kfold-10 now uses loso, and a refusal case covers kfold-10. This revises
    D3's O9 and D41's item 17 (the CV form is no longer one of Code's flagged readings).
  - D41's "derivable" p0: noted. The batch's p0_count/p0_n is the identity's fidelity rule's, which the lock
    declares (n §2.1); the tail is computable from the batch.
  - The first check's naming, "schema v2" against Code's "v3": the raw's head names both, with the hash.
  - The NOT-RUN record: E now says that `5a97527`'s entry listed it among this schema's later commits, and that the
    plan changed, with the clock NOT-RUN now n-analyzer's (`n-not-run-v1`).
  - "Norm-matched" to rounding: noted. The two forms of the dose's norm can differ in the last bits; nothing reads
    them as equal.
