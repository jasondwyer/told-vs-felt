# LOCK-m-F3 v0.1's re-issue — the values-check, one blind pass

*Code's raw, PI date 2026-11-10.*
- *What was checked:* the re-issued lock as drafted (its first part, the separator sentence, and the byte identity of v0.1's text after it), and the entry draft.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written. By its report, the main checkout's HEAD was `23865fa` at its start and end.
- *Outcome:* 68 items: 54 CONFIRMED, 6 IMPRECISE, 1 FAIL, 7 NOT CHECKABLE. The FAIL and every IMPRECISE item are applied (below), and the re-issue was regenerated and recomposed. No second pass was run: each fix is the checker's own wording or a citation it checked, and the composed file's parsers and licence were re-run on the final bytes.
- *This raw:* Code's dispositions, then the report verbatim (extracted by script from the agent's hand-back; it holds no local path).
- *Nothing ran on a model.*

## Code's dispositions

- **25, FAIL: "v0.1's "any reasoning cap but 60" at G-TIME-F3 … now hold on the stub path only".** Agreed: on the stub, G-TIME-F3 admits 120 as well as 60 (`stages._extra` at :624; `STAGE_REASONING_CAPS`; `resume.Identity`).
  - Applied: "v0.1's 60 at G-TIME-F3 is now admitted on the stub path only, beside 120 (m:174's pair at every stage). Its trigger-fixed cap from G-ID-F3 on holds on the stub path only."
- **6, IMPRECISE: C2's quote anchored to `0516832`'s close line, which quotes section A only.** Agreed. Applied: C2 is anchored at the close on `750a7dd`'s entry (`fc43249`).
- **8 and 60, IMPRECISE: "the tables and verbatim blocks of R1 and R3 were generated".** Agreed: R1's rulings table and the driver's flag line are typed. Applied in the lock and the entry: they are named as typed and checked.
- **39, IMPRECISE: F25's site labelled `lines.domain_before_line`.** Agreed: the PIN sits in `lines.domain`. Applied in the generator's label.
- **43, IMPRECISE: `_extra`'s docstring PIN opens at :598.** Agreed. Applied: the rows say "opening at `:598`; the revised sentence", anchored at :602.
- **62, IMPRECISE: which checker looks for which hash.** Agreed. Applied: the proposal's is required by `time_identity_extra`; the analyzer's and mf3's package by the licence's (f), which also reads the m files and the weights; m's package and the Q-F3 closure by the VERDICTS reader.
- **49, NOT CHECKABLE: "pass once this re-issue is committed".** Applied: "are expected to pass". Code re-runs the self-test after the commit, and the G-TIME-F3 announcement reports it.
- **34, optional: "the routing's A2".** Applied: "the routing of 2026-11-09 (evening), A2".
- **The optional note: the licence's new (h).** Applied: R1 quotes `stages.licence_problems`' (h) clause and points to v0.5's sha256 in its table.
- **NOT CHECKABLE 54, 55, 63, 64, 66 and 68:** placeholders, Code's patched run (re-run on the final bytes: no problem, cap 120), and forecasts.
- **The checker's disclosures:** byte sizes (`wc -c`) of the four gate artifacts, and one key listing of the two current ones that the harness saved. None is under `ckpt` or `reports`, and the list's item 2 covers those two directories only. Nothing to rule.

## The checker's report (verbatim)

VALUES-CHECK: LOCK-m-F3 re-issue draft and its entry draft (blind, read-only)

The brief matched: its sha256 starts 87fcb0c35fd6a374 and it has 35 lines. Main checkout HEAD was `23865fa2e6564bb6103c5a39ce0b363e1f9f9935` at my start and at my end. No tracked file changed. Draft sha256s as read: LOCK-m-F3.reissue.md `741fd02f…55bf8` (875 lines); entry_lock.md `02d48ec9…ad2b`.

R = L/LOCK-m-F3.reissue.md:line, E = L/entry_lock.md:line.

## Not CONFIRMED (the list)

- **25 FAIL (R:48–49).** The draft says "v0.1's "any reasoning cap but 60" at G-TIME-F3 … now hold on the stub path only".
  - The quote itself is verbatim (LOCK-m-F3.md:69–70).
  - The code disagrees: on the stub, G-TIME-F3 now admits 120 as well as 60.
    - `stages._extra` admits any cap in `REASONING_CAPS` on the stub at every stage (stages.py:624). v0.1's `stage == "time" and cap != 60` refusal (1e79955:stages.py:596) is gone.
    - `STAGE_REASONING_CAPS` is (60, 120) for every stage (scaffold.py:61, :149).
    - `resume.Identity` admits 120 at every stage (resume.py:197–198).
  - R3's own F8 and F19 rows also say "m:174's pair on the stub, at every stage".
  - The second half is right: the trigger-fixed cap still holds on the stub (stages.py:506–510).
  - Fix, e.g.: "v0.1's 60 at G-TIME-F3 is now admitted on the stub path only, beside 120 (m:174's pair at every stage); its trigger-fixed cap from G-ID-F3 on holds on the stub path only."
- **6 IMPRECISE (R:11–12).** The C2 quote is verbatim, but it is not in `0516832`'s close line, which quotes section A only (RESULTS.md:563–569). C2 is verbatim at RESULTS.md:620 (`fc43249`, the close on `750a7dd`'s entry) and :466 (`7589c1d`). Fix: anchor C2 to `fc43249`.
- **8 IMPRECISE (R:16–17), and 60 (E:28–29), the same claim.** "the tables and verbatim blocks of R1 and R3 were generated":
  - Generated: the identity table, both PIN tables and the register. They are the generated.md blocks IDENTITY, PINS, REVISED and REGISTER, which compose.py placed; each appears verbatim in the draft.
  - Typed: R1's rulings table (R:59–64) and the `time` flag line (R:52) are typed in reissue_template.md (:46–51, :39). reissue_gen.py produces neither.
  - Their values all check (items 26, 29).
  - Fix: name them as typed and checked, as v0.1 §1 named its N10 exception.
- **39 IMPRECISE (R:119).** F25's site is labelled `lines.domain_before_line`. lines.py:52 sits inside `lines.domain` (def :49); `domain_before_line` (def :87) is a wrapper that calls it (:92). The label is a typed string in reissue_gen.py. Fix: `lines.domain`.
- **43 IMPRECISE, minor (R:116, R:133).** `_extra`'s docstring PIN opens at stages.py:598 under its "declared at LOCK-m-F3 v0.1; m's _extra carried" tag. The rows anchor :602 and quote only its revised sentence (:602–604). The quoted text is verbatim. Fix: note "PIN opens :598; revised sentence :602–604".
- **62 IMPRECISE, minor (E:32–33).** All five hashes are named in full (R:24, 27, 28, 29, 31). Two problems with the attribution:
  - The proposal's sha256 is required in the lock text by the driver's `time_identity_extra` (mf3_sessions.py:275–277), not by `licence_problems` or the VERDICTS reader.
  - Licence (f) also looks for the weights' revision and sha256 and the eleven m files (stages.py:388–397). These are covered by E:30–31.
  - Fix: attribute each hash to its checker.
- **49 NOT CHECKABLE (R:182–183).** "pass once this re-issue is committed" is a forecast, and I cannot run the self-test under the brief. Statically, the single failing problem is cured: `098455d9…` appears in full at R:31 and R:52. Suggest the entry's wording, "expected to pass".
- **54, 55, 64 NOT CHECKABLE.** The placeholders `@@LOCKSHA@@`, `@@STAMP@@` and `@@VC@@`.
- **63 NOT CHECKABLE (E:34–35).** Code's patched run of `time_identity_extra` and `licence_problems` needs non-stdlib code. Statically, nothing in the composed text would be refused.
- **66 NOT CHECKABLE (E:37–38).** "expected to pass" and the re-run plan are forecasts.
- **68 NOT CHECKABLE (E:41).** Commit, model and push claims about the future.

## Items

**Header and R0**
1. CONFIRMED (R:3). The §4.3 quote is verbatim (v0.5:75; the source bolds the first five words).
2. CONFIRMED (R:3). v0.1 is dated 2026-11-07 and was added at `1e79955`; it runs from R:189 to the end of the file.
3. CONFIRMED (R:3). A stage cites the whole file's sha256: mf3_sessions.py:265–270 hashes the committed blob; LOCK-m-F3.md:60–61.
4. CONFIRMED (R:7–8). LOCK-m-F3 v0.2 follows G-ID-F3 (m:295–296).
5. CONFIRMED (R:9–11). The A5 quote is verbatim at RESULTS.md:569, which blames to `0516832`, under "section A, verbatim" (:563).
6. IMPRECISE (above).
7. CONFIRMED (R:13–15). List of record v2: raw:16, :28, :7; added at `fc43249`.
8. IMPRECISE (above).
9. CONFIRMED (R:17–18). Committed with identical bytes: no tracked change; `rev-parse HEAD:p` equals `hash-object p` for all eleven R1 and rulings files.

**R1 identity table (R:24–35)**

All sha256 values recomputed; each "at v0.1" label checked against LOCK-m-F3.md:90–99.

10. CONFIRMED. The proposal.
11. CONFIRMED. ADDENDUM-m1.
12. CONFIRMED. ADDENDUM-m2 v0.5 (also banner.py:64).
13. CONFIRMED. The analyzer: same blob at `1e79955` and HEAD.
14. CONFIRMED. m's package `7756dcf4…`: stdlib replica of `package_sha256_of` over 18 files, plus `G-ANL-F3.json` `package_sha256`. valence_core/m has no diff since `1e79955`.
15. CONFIRMED. Q-F3 closure `06a36cbf…`, 22 modules: the artifact's `f3_closure_sha256`, recomputed from its module and data entries, each equal to the current file's sha256.
16. CONFIRMED. Base closure `a3bc7bb9…`, 15 modules, by the same method.
17. CONFIRMED. mf3's package: `hashes` prints `098455d9…` (15 files).
18. CONFIRMED. The driver `1b593ba0…`: the DRIVER line prints the committed blob's sha256 (mf3_sessions.py:358–360, :511). Git blob id `9d54d25f…`.
19. CONFIRMED. G-SHAPE-F3's artifact.
20. CONFIRMED. G-ANL-F3's artifact.
21. CONFIRMED. The schedules manifest.

**R1 bullets**

22. CONFIRMED (R:37–41). `hashes` prints the eleven m-file sha256 and the WEIGHTS line exactly as LOCK-m-F3.md:106–116 and :121. Readers: stages.py:393–397; mf3_sessions.py:202–231.
23. CONFIRMED (R:42–45).
    - `renders_sha16`: `G-SHAPE-F3.json` `inputs.renders_sha256` is `a04f67b0e5105a05…`.
    - The cap: stages.py:624.
    - `locked_path`: mf3_sessions.py:105; stages.py:658–660.
24. CONFIRMED (R:46–48). Two changes; `_extra` on a model (stages.py:621–627); `prior_gate` with `require_real` (stages.py:499–505, :726).
25. FAIL (above).
26. CONFIRMED (R:50–52). Flag names: mf3_sessions.py:103, :1475–1476; the values are R1's.
27. CONFIRMED (R:54–55). mf3_sessions.py:106–108, :299–306, :337–344; stages.py:114–117.
28. CONFIRMED (R:56). At `1e79955`: :280, :397, :466–477, :491, :556, :619 and :642 are as v0.1 cites them. stages.py has changed since only at `5d40d59`.
29. CONFIRMED (R:59–64). Four sha256 values; the files were added at `7589c1d`, `0516832`, `fc43249` and `50fea90`.

**R2**

30. CONFIRMED. All 13 items of §4.3's list (v0.5:75), in order.
31. CONFIRMED. The fire: v0.5:13, :15; RESULTS.md:2464–2469 (`daca8b0`); mf3_sessions.py:303–305.
32. CONFIRMED. The class correction (v0.5:27).
33. CONFIRMED. The smoke: v0.5:52–61, :71; read:7, :30; banner.py:61 holds `REASONING_SEGMENT` with the exact bytes.
34. CONFIRMED. The cap and the PI's 2026-11-09 decision (RESULTS.md:451, A2 "[adopted]"); bar 5 is v0.1's §8 row 5.
    - Optional: say "the routing of 2026-11-09 (evening), A2". 2026-11-10's routing, which R0 names, also has an A2 (RESULTS.md:566).
35. CONFIRMED. The §4.2 quote; m_analyze.py:10713 is `def _bt_f3_chain` and :10722 holds `"reasoning_cap": 60`; scaffold.py:61.
36. CONFIRMED. `5d40d59`, `0684263`, `23865fa` per `git show --name-status`.
    - The superseded artifacts are `02dadb3`'s and `f9700ba`'s blobs (`b91a8c67…`, `0c9de56e…`).
    - Comparing the two G-ANL-F3 closures, exactly mf3's `banner`, `lines`, `readrule` and `scaffold` changed.
37. CONFIRMED. The analyzer quote (v0.5:75).

**R3**

38. CONFIRMED. All 8 texts in the first table are byte-equal to the joined comment or docstring at the given line, each inside the named function, except 39.
39. IMPRECISE (above).
40. CONFIRMED. v0.1 register rows: LOCK-m-F3.md:451, 453, 456, 464, 470, 473, 474.
41. CONFIRMED. F29's note: LOCK-m-F3.md:474; v0.5:50.
42. CONFIRMED. "Revised in place … round 2": review raw :73, :342–349. All five texts are equal at HEAD (the out_paths row excludes the opening `"""`).
43. IMPRECISE (above).
44. CONFIRMED. The two readings:
    - The F6 reading and the counter (b) reading are both listed for the seat at RESULTS.md:170–174.
    - Strikable until v1.0: prebuild answers :50; v0.1's cost: LOCK-m-F3.md:32–36.
    - The counter (b) reading's code: lines.py:202–220; m/audit.py:501–506 ("forced -> any claim").
45. CONFIRMED. 18 sites: banner 1, gshape 2, lines 4, readrule 1, resume 1, runner 1, scaffold 1, stages 6, driver 1. No variant tags; every opening is a prefix of its line; comment or docstring is right for each.

**R4 and the separator**

46. CONFIRMED. The re-run plan (v0.5:75, :77, :85; m:293).
47. CONFIRMED. The order after the re-run and D2 2026-12-22 (v0.5:75, :19, :86).
48. CONFIRMED. The finding-11 anchor: review raw :50–52, :268 (mf3_sessions.py:718–727, :728–731); RESULTS.md:148–151.
49. NOT CHECKABLE (above).
50. CONFIRMED (R:185–187). The separator matches LOCK-p v0.2's form (LOCK-p-OLMo-sft.md:92–96).

**Byte identity and parsers**

51. CONFIRMED. R:189–875 is byte-identical to `git show HEAD:LOCK-m-F3.md` (sha256 `377c5d60…6ce7`, 687 lines, the same blob as `1e79955`'s). R:188 is one blank separator line, so "everything after R:187" is one `\n` plus v0.1; this is the same form as LOCK-p-OLMo-sft.md:95.
52. CONFIRMED. The first part can give the parsers no second value.
    - No line of R:1–187 contains any of the eleven `valence_core/m/<name>.py` paths; R:28's `valence_core/m/*.py` matches none.
    - `_WEIGHTS_RX` finds nothing in the first part.
    - I ran a stdlib replica of `lock_m_modules` and `lock_weights` on the composed text (the regexes copied from mf3_sessions.py:123–124, the logic from :202–231). Result: the eleven sha256 equal the files now, no problem, and one WEIGHTS binding for mlx-community/Qwen3.6-27B-4bit.
    - Licence (f) one-line naming holds, and the VERDICTS reader's three values (m_analyze.py:4128–4134) are present.

**Entry**

53. CONFIRMED. E:1–2, apart from the placeholder.
54. NOT CHECKABLE: `@@LOCKSHA@@`.
55. NOT CHECKABLE: `@@STAMP@@`.
56. CONFIRMED. E:4–6 quotes (RESULTS.md:569, :620).
57. CONFIRMED. E:7–9: `585df45`'s form; v0.1 byte-identical, `377c5d60…6ce7`.
58. CONFIRMED. E:10–17.
59. CONFIRMED. E:18–26: five revised sites, two readings, 18 sites.
60. IMPRECISE (as 8).
61. CONFIRMED. E:30–31, by the replica in 52.
62. IMPRECISE (above).
63. NOT CHECKABLE (above).
64. NOT CHECKABLE: `@@VC@@`.
65. CONFIRMED. E:37–38: the two red checks are finding 11's.
66. NOT CHECKABLE (above).
67. CONFIRMED. E:39–40: m:267 holds the laptop checklist; the announcement rule is RESULTS.md:2474.
68. NOT CHECKABLE (above).

**Optional note, not graded.** `licence_problems` now also runs (h), the addendum check (stages.py:303–305, :380–386). v0.1's §1 licence list lacks it, and the re-issue names v0.5's sha256 without saying the licence checks it. §4.3 does not ask for this.

## Tally

68 items: 54 CONFIRMED, 6 IMPRECISE, 1 FAIL, 7 NOT CHECKABLE.

## Compliance

No breach.
- Nothing under any `data/*/ckpt` or `data/*/reports` was opened, listed, sized or traversed.
- The one content search (`git grep`) carried `':!data/**'`; every other grep was on named files.
- No `--stat`-family form; no git writes; no file written; the `hashes` command ran once, model-free, exit 0. Every Python script of my own was stdlib, run as `python3 -I`.
- Disclosed, though not a departure as I read item 2:
  - I printed byte sizes (`wc -c`) of the four gate artifacts in `data/m/gates` and `data/mf3/gates`, which are outside `ckpt` and `reports`.
  - The harness auto-saved one oversized key listing of the two current gate artifacts (`data/m/gates/G-ANL-F3.json`, `data/mf3/gates/G-SHAPE-F3.json`) to its tool-results directory; nothing from `ckpt` or `reports` was in it.
