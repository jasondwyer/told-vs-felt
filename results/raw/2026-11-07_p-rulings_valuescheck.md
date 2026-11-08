# PROPOSAL-p -- G-CAL-p's flags applied: the blind values-check (Code's raw, 2026-11-07)

*A blind values-check agent, read-only on the repository, checking every factual claim of the dated notes and the entry against the ruling, the code and the record. Code's dispositions come first; the report follows verbatim. Local paths scrubbed.*

## 0. Code's dispositions (each item re-checked at source before it was applied)

The check ran on the texts after review round 1's fixes: 69 items, 60 CONFIRMED, 5 IMPRECISE, 2 FAIL, 2 NOT CHECKABLE.
Review round 2 then changed three sentences: the F-p8 bullet, now naming `proposal_p_file`; the F-p10 bullet, now naming the artifact's `diagnostic_fields`; and F-p11, widened. Code checked those by tool: the self-test's walk case, and each of F-p11's eleven examples run through `report.corrupted_spelling`.

| item | verdict | disposition |
|---|---|---|
| the ruling's sha256 tail, twice | FAIL | Applied: `e3de1c03…e006`. `38f9974`'s commit message abbreviates it `…d006`, and the COMMITTED entry's dated note says so. |
| B5 | IMPRECISE | Applied: the BUILD entry's dated note says the P21 ruling strikes register entry (4) (F-p4). |
| E2 | IMPRECISE | Applied: the entry names the three new refusals and the driver's edited usage text, which moves its sha256. |
| E31 | IMPRECISE | Applied: "Code's readings are PINs in `report.py`", with two of them named. |
| E34 | IMPRECISE | Applied: the dated notes are listed by entry. |
| E36 | IMPRECISE | Applied: F-p11 is item-scoped. |
| gaps (3) | -- | Applied: the G-SHAPE-p note says the ruling's description of the artifact differs from its bytes; the BUILD note declares `returned_text` diagnostic, as the ruling's §3 asks; the COMMITTED note covers §4.2's register text. |
| (2) | NOT CHECKABLE | "Nothing ran on a model" and the box's next step: consistent with the code. |

## 1. The report (verbatim)

# Blind values-check: the rulings texts (NOTE-COMMITTED, NOTE-BUILD, NOTE-GSHAPE, ENTRY)

Checker: a blind agent, read-only on the repository (no repo file edited, no git state changed, nothing pushed).
Scratch work is in `.../scratchpad/podwatch/vc_rulings/`.

**What was checked**
- The TEXT: `.../scratchpad/podwatch/rulings_texts.md`, sha256 `286521d8fb2426fa…`. Placeholders (@@…@@) are ignored.
- Repo: HEAD `38f9974` at the start; origin/main `1e79955`.
  - **HEAD moved during the check.** A parallel session committed `acc3b52` (G-TIME-F3, 2026-11-07 23:35:06 -0500).
  - It touches only `RESULTS.md` (+83 lines), `data/mf3/ckpt`, `data/mf3/reports` and three `results/raw` files. It touches nothing under `valence_core/`, `scripts/p_sessions.py`, `LOCK-*.md`, `data/p` or `data/m/gates`.
  - The working-tree diff is unchanged (same sha256). The self-test was re-run at `acc3b52`: 109/109.
  - **RESULTS.md line anchors below are pinned to `38f9974`.** Add 83 for `acc3b52`; for example, the full ruling hash is at :367 at `38f9974` and :450 at `acc3b52`.
- Working tree: seven files modified (`git diff HEAD`, sha256 `944ac4f8a2eaf769…`):
  - `valence_core/p/gcal.py`, `__init__.py`, `gshape.py`, `proxy.py`, `register.py` and `report.py`;
  - `scripts/p_sessions.py`.
- Nothing else is modified under `valence_core/m`, `valence_core/mf3`, `valence_core/adapters`, the `scripts/m*` drivers or `LOCK-*.md`.

**Sources read**
- The ruling `results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md` at `38f9974`.
  - Its sha256 recomputed: `e3de1c0316c95701e627fb89596c50b0cf0596f31c352ed6ee9a8daca5d1e006`.
- The block `..._code-to-design.md` (`aee7d86`).
- The full working-tree diff, and the p modules in full where claims touch them.
- m's `gcal.py`, `stages.py`, `scaffold.py`, `runner_olmo.py` and `resume.py`.
- `data/p/gates/G-SHAPE-p.json`: the blob at `5009e77` equals the working-tree file, sha256 `3fb0f640…6961`.
- PROPOSAL-p v0.2 (`42f2977b…3b32`) and PROPOSAL-m v1.11 (`42ab36ec…6c6b`), both recomputed.
- The BUILD design raw, the BUILD review raw and the referent-check raw.
- RESULTS.md entries at lines 352, 384, 409 and 681, and the 38f9974 close line at lines 365–382.
- The commit messages `0786c11`, `f9700ba`, `18b0111` and `a665a09`.
- The origin/main reflog.
- The G-CAL-OLMo artifacts at HEAD.
- One file outside the listed sources, used only for the "review's MAJOR" claim: the scratch raw `p_rulings_review.md`.

**Runs** (all with `nice -n 19`, model-free)
- `scripts/p_sessions.py --selftest`: **109/109 pass**, exit 0, at `38f9974` and again at `acc3b52`. The BUILD's record was 103/103.
- `scripts/p_sessions.py hashes`: p's `package_sha256` is now `1d764a3e5cfe975b8359e4be19178010f3886ad5d5c4c6bc8d28b4b9607ce145`, over 11 files.
  - This value is only valid for the bytes checked here: `gcal.py` `6608b464…`, `report.py` `58e12ae2…`, `register.py` `7f66231b…`, `proxy.py` `72fe6d56…`, `gshape.py` `4508b9a9…`, `__init__.py` `1b2d1c80…`, and the driver `1140b57e…`.
  - The 17 m licence lines and olmo_hf.py's line are identical to the BUILD design raw's lines (diff empty).
- Probes (scratch `vc_rulings/fp1.py`, `fp11.py`, `probe1.py`, `quotes.py`):
  - the counter on the 384 committed records;
  - the F-p11 pairs;
  - the precheck with DISCLOSURE altered, and with RULING_SHA256 altered;
  - the register's entries, and `substituted(4|5)`;
  - `gate_record`;
  - quote comparisons, after collapsing whitespace for line wraps.
  - The stub precheck wrote nothing; `git status` was unchanged afterwards.

Verdicts: CONFIRMED / IMPRECISE / FAIL / NOT CHECKABLE.

---

## NOTE-COMMITTED

| # | Claim | Verdict | Evidence / correction |
|---|---|---|---|
| C1 | ruling path; committed at `38f9974` | CONFIRMED | `git show 38f9974 --stat` adds exactly that file. |
| C2 | "sha256 `e3de1c03…d006`" | **FAIL** | The file hashes to `e3de1c03…e006` (full hash above; its last eight characters are `a5d1e006`). **Write `e3de1c03…e006`.** 38f9974's commit message has the same wrong tail (`e3de1c03...d006`). RESULTS.md:367 and `gcal.RULING_SHA256` carry the correct full hash. |
| C3 | "confirmed by the PI" | CONFIRMED | 38f9974 close line: "The five rulings [confirmed] → …". |
| C4 | "Text corrections to p go here, not to a v0.3" | CONFIRMED | Ruling header: "Text corrections to p go to the COMMITTED entry as dated notes (the m precedent), not to a v0.3." |
| C5 | §5.4 = referent item 85 = F-p3 | CONFIRMED | Referent raw :261 (item 85, §5.4's date); design raw F-p3 "(§5.4's date; referent item 85, `18b0111`)". |
| C6 | "The pre-registration date is 2026-11-07, `18b0111` (m:6)" | CONFIRMED | Ruling §1, verbatim in substance. m:6 says "the commit hash is the timestamp of record". `18b0111` is committer-dated 2026-11-07 14:09:28 -0500. |
| C7 | The disclosure sentence, quoted | CONFIRMED | Character-identical to ruling §1's italic sentence once line wraps are collapsed: backticks around `18b0111` included, period inside the quotes as in the ruling. |
| C8 | "§5.2's declared sentence, which dates the gate, is unchanged" | CONFIRMED | p §5.2's sentence has "(G-CAL-OLMo, 2026-11-06)". The ruling has "which dates the gate and not the pre-registration, is unchanged". PROPOSAL-p v0.2 is unmodified in the tree. |
| C9 | §2.2's sentence, quoted | CONFIRMED | Character-identical to ruling §3's corrected sentence. The original at p §2.2 reads "Nothing after the cut is stored, graded, or seen by any later round." |
| C10 | §3.1's "by import or by §4.2's register" reads with the amended register; entry (5); entry (4) struck | CONFIRMED | p §3.1 carries that phrase. Ruling §4: "P21 enters it as entry (5)… Entry (4)… is struck… p §3.1's '…' is corrected by the same dated note." |
| C11 | Item 131: §1.1's "matched case-insensitively" was the seat's omission from "what changed"; both reproductions matched case-insensitively; no render changes | CONFIRMED | Referent raw item 131 (:364). p v0.2 lines 5–9 do not mention it (grep count 0). Pre-read renders raw :11: "CASE-SENSITIVE DIFFERS … (none does)". `corrupt.py:92` matches `.lower()`. Ruling §6. |
| C12 | F-p6: disclosing is enough; the rule stands; nothing ran | CONFIRMED | Ruling §6 bullet 1. Design raw F-p6 = "the departure". |

## NOTE-BUILD

| # | Claim | Verdict | Evidence / correction |
|---|---|---|---|
| B1 | Dated 2026-11-07; the ruling at `38f9974`; confirmed by the PI | CONFIRMED | As C1/C3. |
| B2 | F-p3, F-p8, F-p10, P21 (F-p7) and F-p1 are ruled, and applied at the commit | CONFIRMED | Ruling §1–§5 and §7 item 1. Each is applied in the working-tree diff (see E8–E33). The self-test passes 109/109. |
| B3 | F-p5: the licence binds m's sha256s as they stand at LOCK-p v0.1, after LOCK-m-F3 v0.1 (p §4.3) | CONFIRMED | Ruling §6 bullet 3. p §4.3: "LOCK-p v0.1 is written after LOCK-m-F3 v0.1". |
| B4 | "The sha256s in this entry are the build's, and any move between them is recorded at the lock" | CONFIRMED | Ruling §6: "the BUILD entry's shas are the build's, and a move between them is recorded at the lock". The BUILD entry (RESULTS.md:409–516) carries the build's hashes: package `717958da…b900`, olmo_hf `df80b79b…`, manifest `99937365…`, m's gcal `fbae9a01…`. |
| B5 | "F-p2, F-p4 and F-p9 are recorded; the seat made no ruling on them" | **IMPRECISE** | The ruling's §6 does say "F-p4, F-p9: recorded, no ruling". But F-p4 is "register entries (3) and (4)" (design raw :245; the BUILD entry), and ruling §4 strikes entry (4). The BUILD entry's register bullet still reads "(4) … declared and not exercised", and no note on that entry says otherwise. **Suggested:** "F-p2, F-p4 and F-p9 are recorded, no ruling (§6); F-p4's entry (4) is struck by the P21 ruling (§4), and entry (5) admitted." |

## NOTE-GSHAPE

| # | Claim | Verdict | Evidence / correction |
|---|---|---|---|
| G1 | Dated 2026-11-07; the ruling at `38f9974`, F-p8 | CONFIRMED | Ruling §2. |
| G2 | "a write-once artifact is not rewritten for a field's meaning" | CONFIRMED | Ruling §2, verbatim. |
| G3 | The artifact carries `proposal_p_sha256` (p's) and no `proposal_sha256` field; m's sha256 sits at `inputs.proposal_m.sha256` | CONFIRMED | The 5009e77 blob has top-level keys `proposal` and `proposal_p_sha256` = `42f2977b…3b32`, and no key named `proposal_sha256` at any depth (full walk). `inputs.proposal_m` = {path `PROPOSAL-m-gating-campaign-v1_11.md`, sha256 `42ab36ec…6c6b`}. See observation O2. |
| G4 | The ruling puts m's sha256 in `proposal_sha256` in every p artifact; G-SHAPE-p's code writes it | CONFIRMED | Ruling §2. `gshape.py:356`: `"proposal_sha256": ins["proposal_m_sha256"]`. Self-test: "gshape-p: the artifact carries m's pin in proposal_sha256 …" passes. |
| G5 | "Its disclosure is the pre-ruling sentence (F-p3)" | CONFIRMED | The artifact's `disclosure` is "PROPOSAL-p's units were pre-registered on 2026-11-06 after the shared dose failed completability… (p v0.2 §5.4)". That is HEAD's `gcal.DISCLOSURE`. |
| G6 | "p's package hash has moved, so under F-p5's rule G-SHAPE-p re-runs before LOCK-p v0.1" | CONFIRMED | The hash moved: `717958da…b900` (artifact provenance) → `1d764a3e…e145` (working tree). F-p5's rule (design raw :247–251; the G-SHAPE-p entry) is "re-runs first if its sources map differs then". 7 of the map's 48 entries differ: six p modules and `scripts/p_sessions.py`. Wording note (optional): the rule's trigger is the sources map, so "p's package files and driver have moved (7 of its 48 sources)" names it exactly. |
| G7 | "Its writer is write-once, so the canonical re-run needs this artifact superseded first" | CONFIRMED | `gshape.write` → `guard.write_once_bytes`. It refuses "EXISTS … with different bytes; it is never overwritten" and accepts only identical bytes. The re-run must differ (a new `proposal_sha256` key, the new disclosure, moved provenance). |
| G8 | "(a hand `git mv` on the seat's ruling, as G-SHAPE-F0's and G-SHAPE-F3's were)" | CONFIRMED | `0786c11` and `f9700ba`: "superseded by hand under PIN-S9 (git mv to …superseded-2026-11-07.json)", on the seat's s7 order. PIN-S9 reads "Supersession is by hand only, on the seat's ruling" (cited in `results/raw/2026-11-06_ganl-f3_answers_valuescheck.md:139`). p's code and design raw declare no supersession rule (grep). |
| G9 | "which F-p12 asks" | CONFIRMED | ENTRY F-p12. |

## ENTRY

| # | Claim | Verdict | Evidence / correction |
|---|---|---|---|
| E1 | Header: the seat's five rulings of 2026-11-07 (`38f9974`), confirmed by the PI (F-p3, F-p8, F-p10, P21, F-p1) | CONFIRMED | Ruling §7 item 1 lists those five. Close line: "[confirmed]". |
| E2 | "Each ruling is a constant, an argument, a field name or a definition in `valence_core/p/`." | **IMPRECISE** | Two problems. (1) The rulings also add **checks**: G-CAL-p's precheck now refuses a PROPOSAL-m not committed at v1.11's sha256, and a DISCLOSURE not equal to the ruling's §1 sentence (`gcal.py:233–239`). G-SHAPE-p's inputs now refuse the same PROPOSAL-m (`gshape.py:244–246`). (2) The commit also edits **`scripts/p_sessions.py`**, outside `valence_core/p/`: its gcal usage text names the two new checks. That moves the driver's sha256, which is G-CAL-p's identity field `driver_sha256` and one of G-SHAPE-p's 48 sources. The ENTRY never names that file. **Suggested:** "Each ruling is applied in `valence_core/p/` as a constant, an argument, a field name or a definition, with the checks that pin them (G-CAL-p's precheck refuses a PROPOSAL-m off v1.11's sha256 or a disclosure off the ruling's bytes; G-SHAPE-p refuses the same PROPOSAL-m); `scripts/p_sessions.py`'s usage text names the two new precheck checks." |
| E3 | "Nothing of m, mf3, `olmo_hf.py` or any lock changes" | CONFIRMED | `git status` shows no change under `valence_core/m`, `valence_core/mf3`, `valence_core/adapters` or `LOCK-*.md`. `git diff a665a09 HEAD` is also empty for those three directories. |
| E4 | "and nothing ran on a model" | NOT CHECKABLE | A claim about Code's actions. It is consistent with the code: every self-test case uses stub adapters, and the driver's self-test traps the loader. |
| E5 | "The box repo is brought to this commit; G-CAL-p waits for the coordinating session's go" (and "Next … Not pushed") | NOT CHECKABLE | Future actions (@@BOX@@). Consistent with the close line: "brings the box repo to it. The coordinating session's go follows". |
| E6 | The routing quote (two lines) | CONFIRMED | Byte-identical to the 38f9974 close line's quote (RESULTS.md), including U+2192 "→" and U+2019 in "N1’s". |
| E7 | "Item 2 was the coordinating session's; it pushed through `1e79955`" | CONFIRMED | Close line: "The push of the fourteen commits since `fb742e4` (through `1e79955`) is the coordinating session's". The origin/main reflog shows `fb742e4 → 1e79955`, "update by push", 2026-11-07 22:49:37 -0500. `fb742e4..1e79955` is 14 commits. |
| E8 | F-p3: `gcal.DISCLOSURE` is §1's sentence, verbatim | CONFIRMED | `disclosure_problems() == []` (self-test passes). The string equals the ruling's §1 italic sentence. |
| E9 | "pinned to the ruling's committed bytes (sha256 `e3de1c03…d006`)" | **FAIL** | As C2: **`e3de1c03…e006`**. The code's `RULING_SHA256` is correct; only the text's abbreviation is wrong. |
| E10 | "G-CAL-p's precheck refuses otherwise, and a self-test case checks it" | CONFIRMED | Probe, stub precheck to a scratch dir. With DISCLOSURE altered (date changed): `G-CAL-p REFUSED: ["disclosure (F-p3): DISCLOSURE is not the ruling's §1 sentence"]`. With RULING_SHA256 altered: refused ("… is not the seat's ruling committed at its sha256 …"). Self-test case "gcal: DISCLOSURE is the ruling's §1 sentence, read from its committed bytes (F-p3)" passes. |
| E11 | "G-CAL-p's artifact carries it, and so does G-SHAPE-p's code" | CONFIRMED | `gcal.artifact`: `art["p"]["disclosure"] = DISCLOSURE`. `gshape.py:399`: `"disclosure": gcal.DISCLOSURE`. Both are asserted in the self-test. |
| E12 | F-p8: G-CAL-p's identity, and with it its checkpoint and artifact, carries `proposal_sha256` = v1.11's (`42ab36ec…6c6b`) | CONFIRMED | `identity()` passes `proposal_sha256=M_PROPOSAL_SHA256`. m's `completability_artifact` copies `identity`. The self-test asserts both `ck["identity"]` and `art["identity"]`. The prefix and suffix match the recomputed hash. |
| E13 | "The precheck refuses unless that file is committed at that sha256" | CONFIRMED | `gcal.py:233–238`: `m_stages._committed` (HEAD blob, identical working-tree bytes, no link), then the sha256 equals `M_PROPOSAL_SHA256`. Self-test with the sha patched to zeros: "refused … before any adapter is made". |
| E14 | `proposal_p_sha256` is p's (`42f2977b…3b32`) | CONFIRMED | `PROPOSAL_P_SHA256`, recomputed. |
| E15 | "The gate line's startup check stays on p's sha" | CONFIRMED | `gcal.py:247`: `m_gcal.gate_line(PROPOSAL_P_REL, PROPOSAL_P_SHA256, …)`, non-stub precheck. |
| E16 | m's gate-line record, stored in the checkpoint's provenance, holds that check's sha256 under p's name `proposal_p_sha256` (`gcal.gate_record`; "the review's MAJOR") | CONFIRMED | m's `gate_line` returns `rec["proposal_sha256"] = psha` (m `gcal.py:599–627`). `run()` stores `"gate": gate_record(pre["gate"])` (`gcal.py:494`), which drops `proposal_sha256` and adds `proposal_p_sha256` (probe). The scratch `p_rulings_review.md` records "**MAJOR M1**: … `proposal_sha256` holding p's sha, in `provenance[].gate`". Wording note: the BUILD's review also had a MAJOR, so "MAJOR M1 of the rulings' review" would be unambiguous. |
| E17 | "so `proposal_sha256` means m's everywhere" | CONFIRMED | Inventory of p's code (grep). `proposal_sha256` is written only in G-CAL-p's identity (m's) and G-SHAPE-p's artifact (m's). The gate record is renamed. The adapter provenance record is verbatim, and `olmo_hf.py` contains no "proposal". `data/p` holds no other file with a `proposal_sha256` (the schedules have none). The 5009e77 artifact has none (G3). |
| E18 | G-SHAPE-p's code writes `proposal_sha256` = m's and refuses a PROPOSAL-m at another sha256 | CONFIRMED | `gshape.py:244–246`, `:356`. Its self-test case with the sha patched: refused. |
| E19 | "Its artifact at `5009e77` stands, with a dated note on its entry" | CONFIRMED | Ruling §2. NOTE-GSHAPE. |
| E20 | F-p10: the cut log names the returned text `returned_text`, declared diagnostic (`proxy.DIAGNOSTIC_FIELDS`), and the stored text `stored_text` | CONFIRMED | `proxy.cut_result` returns `{"returned_text": text, "stored_text": cut, …}`. `DIAGNOSTIC_FIELDS = ("returned_text",)`, aliased in `gcal`. No `text_returned` or `text_stored` remains in p (grep). |
| E21 | "A STOP record keeps the returned text whole as `returned_text`" | CONFIRMED | `_stop(… returned_text=…)` stores it untruncated (only `detail` is cut, at 600). ProxyStop carries `.returned_text`. Self-test cases: trigger path `"a\nb"`, ProxyStop `"x\ny tail"`. Note: a STOP before any generation (boundary or insulation) records `None`, since there is no returned text. |
| E22 | None of these is a record's `text`; each is outside the hair trigger's domain, the grader, every later round's prompt and the read rule's stored text, "all of which read a record's `text` alone" | CONFIRMED | In G-CAL-p, the hair trigger and grader read the generation's `text`, which becomes `rec["text"]`. So do `read_checkpoint`, `report.counters`, the artifact's hair-trigger count and `strict_grade`. `read_checkpoint` requires the record keys to be exactly m's `RECORD_KEYS`. Later rounds and the read rule are m's code: `runner_olmo.py:140–142` and `:167–169` put `g.text` (the proxy's stored text) into `add_round` and the transcript. m's `readrule.py` keeps round `"text"`. p has no session or analyzer code yet (step 6), so those two arms hold by m's code, not p's. |
| E23 | P21: entry (4) struck; entry (5) added, kind "pinned restatement", admitted, never substitutable | CONFIRMED | `register.ENTRIES` n = [1, 2, 3, 5]. Entry 5 has kinds `('pinned restatement',)` and status "admitted by the seat's ruling of 2026-11-07 (38f9974, §4); a restatement, never substituted". `substituted(5, …)` and `substituted(4, …)` both raise REGISTER STOP (probe). `hashes` prints four REGISTER lines, entry 5 `"kind": "pinned restatement"`. |
| E24 | Anchors `gcal.py:1155`, `:1164`; `temp, cap` at `:1104` | CONFIRMED | m's `gcal.py` (unchanged since `993eba1`): :1155 `seg = f"Task: {task}\nResponse:"`; :1164 `g = adapter.generate(SESSION_BANNER, seg, …)`; :1104 `temp, cap = _ro.OLMO_TEMP, _ro.STOP_CAP` (the OLMo branch; :1101 is Qwen's). |
| E25 | "Term (e)'s text carries §4's amendment verbatim" | CONFIRMED | The ruling's italic amendment ("never an unpinned copy; … before it changes p's behaviour.") occurs character-for-character in `register.py`'s term (e), after collapsing whitespace. |
| E26 | "The AST pin also runs in G-CAL-p's precheck, as since review round 2" | CONFIRMED | `gcal.py:229`. It is already in the precheck at `a665a09:valence_core/p/gcal.py:215`. BUILD review raw m10: "(also run in the precheck from round 2)", and N-f: "runs in G-CAL-p's precheck". Wording: "as it has since review round 2". |
| E27 | `report.corrupted_spelling` is §5's pinned definition | CONFIRMED | The implementation matches the definition: whitespace-split and `normalize`d words; length ≥ 2; FUNCTION_WORDS and the clean pool's task words excluded; numeric golds excluded; a hit iff the word is not a gold and is within distance 1 (gold length ≤ 3) or 2 otherwise. The docstring quotes the ruling's definition verbatim (checked). |
| E28 | On G-CAL-OLMo's 384 committed records: 0/3/5 (sft/dpo/instruct) | CONFIRMED | Recomputed on the HEAD blobs (3 × 128): sft 0, dpo 3, instruct 5. |
| E29 | The eight: the five of §0.3's class (c) (`Januwy` ×2, `Janaury`, `dn` ×2), `irom`, and `true` against `three` twice | CONFIRMED | dpo: clean i4 s1 (`true`/`three`, d2), corrupted i8 s2 `Januwy`, i11 s1 `dn`. instruct: corrupted i4 s1 (`(True`→`true`/`three`), i7 s1 `irom`/`iron` (d1), i8 s2 `Januwy`, i8 s3 `Janaury`, i11 s1 `dn`. p §0.3 lists all of these under class (c). See O6 on `dn` ×2. |
| E30 | `the`/`two`/`do` and `Janbaa`/`Janyooar` are not counted | CONFIRMED | `the` and `do` are FUNCTION_WORDS. `the`→`two` is distance 2, but gold `two` has length 3, so the threshold is 1. `two` equals a gold. `Janbaa` (sft i8 s2, d3) and `Janyooar` (dpo i8 s3, d4) are present and not counted. |
| E31 | "One reading is Code's, a PIN: the text is split on whitespace first and each token then normalized…" | **IMPRECISE** | `report.py`'s PIN declares more readings than that one: empty tokens dropped; the clean pool's task words by the same rule; FUNCTION_WORDS is p §1.1's list; a gold is a normalized variant, numeric when its characters other than spaces are digits. **Suggested:** "Code's readings are a PIN (report.py): the text is split on whitespace first and each token then normalized, empties dropped — so `don't` is the one word `don t`; the clean pool's task words by the same rule; a gold is a normalized variant, numeric when its non-space characters are digits." |
| E32 | `don't` is the one word `don t` | CONFIRMED | `spelling_words("I don't know")` = `['i', 'don t', 'know']`. |
| E33 | "The counter decides nothing" | CONFIRMED | Ruling §5 ("Descriptive, deciding nothing (rule 23)"). The artifact's verdict is m's condition (4); the counters are reported only. |
| E34 | "The text corrections to p and §6's acknowledgements are dated notes on the COMMITTED entry (… item 131, F-p6). F-p5, F-p2, F-p4 and F-p9 go on the BUILD entry …" | **IMPRECISE** | F-p5, F-p2, F-p4 and F-p9 are also §6's acknowledgements, so "§6's acknowledgements are … on the COMMITTED entry" contradicts the next sentence. **Suggested:** "The text corrections to p (§5.4, §2.2, §3.1) and two of §6's acknowledgements (item 131, F-p6) are dated notes on the COMMITTED entry (`18b0111`); §6's F-p5, F-p2, F-p4 and F-p9 go on the BUILD entry (`a665a09`), and F-p8's note on the G-SHAPE-p entry (`5009e77`)." The parenthetical lists themselves match the three notes. |
| E35 | F-p11's pairs `there`/`three`, `could`/`cold`, `too`/`two`, `from`/`iron`, `that`/`shut` count | CONFIRMED | Distances and thresholds: there/three 2 of 2, could/cold 1 of 2, too/two 1 of 1, from/iron 2 of 2, that/shut 2 of 2. None of the five words is in FUNCTION_WORDS or the 49 clean task words. Each gold exists (items 4, 5, 10, 7 and 15). `corrupted_spelling` returns True on each (probe). |
| E36 | "…counts a common word within the threshold of a gold wherever an answer uses it" | **IMPRECISE** | The count is per item: `there` counts only in an answer to item 4 (gold `three`), not in any answer. **Suggested:** "…within the threshold of an item's gold wherever an answer to that item uses it". The same phrasing is in `report.py`'s docstring. |
| E37 | "On G-CAL-OLMo's records only `true`/`three` occurs" | CONFIRMED | Of the 8 hits, the only common-word ones are the two `true`/`three`. |
| E38 | "The counter is recomputable, so a refinement is a re-tabulation" | CONFIRMED | Ruling §5. |
| E39 | F-p12: the re-run is refused by the write-once writer while the 5009e77 artifact stands; supersession is the seat's to give | CONFIRMED | As G7/G8. p declares no supersession rule. |
| E40 | "(descriptive; neither blocks G-CAL-p)" | CONFIRMED | G-CAL-p's precheck reads no G-SHAPE-p artifact. p §4.2/§4.3 put G-SHAPE-p before LOCK-p v0.1, and G-CAL-p needs no lock. |
| E41 | p's `package_sha256` (@@PKG@@) over 11 files | CONFIRMED | 11 `valence_core/p/*.py`. At the checked bytes the value is `1d764a3e5cfe975b8359e4be19178010f3886ad5d5c4c6bc8d28b4b9607ce145`. Recompute after any further edit. |
| E42 | "The m files and `olmo_hf.py` are unchanged" | CONFIRMED | The 17 m licence lines and olmo_hf.py's line (`df80b79b…`) from `hashes` are identical to the BUILD design raw's. |
| E43 | "G-SHAPE-p's sources map therefore differs, and it re-runs before LOCK-p v0.1 (F-p5's rule)" | CONFIRMED | 7 of the 48 recorded sources differ: six p modules and the driver. The import closure (14) is unchanged. F-p5's rule is as in G6. |

---

## Observations (beyond claim verification)

- **O1 (hash).** The `…d006` tail also appears in 38f9974's commit message, which is committed and cannot change. RESULTS.md (:367 at `38f9974`, :450 at `acc3b52`) and `gcal.RULING_SHA256` have the full, correct hash. Fix only the two occurrences in the TEXT.
- **O8 (parallel commit).**
  - `acc3b52` landed on `main` during this check, so the rulings' commit will sit on it, not on `38f9974`.
  - No claim in the TEXT changes: acc3b52 touches no file any claim depends on.
  - Rebase any scratch or site check onto the new HEAD.
- **O2 (NOTE-GSHAPE vs the ruling's premise).**
  - Ruling §2 says the 5009e77 artifact was "already written with p's in both fields". It has only `proposal_p_sha256`.
  - The note describes the artifact correctly but does not say that the ruling's description differs.
  - Under "findings flagged, never silently applied", consider one clause, e.g. "(not, as §2 has it, p's in both fields)".
- **O3 (F-p10 term (i)).**
  - Ruling §3 asks that the field be "declared diagnostic in the BUILD entry and LOCK-p v0.1".
  - NOTE-BUILD only says F-p10 is "ruled and applied" and points to the rulings' entry.
  - Consider declaring it there, e.g. "F-p10: the cut log's and the stop field's `returned_text` is a diagnostic field (`proxy.DIAGNOSTIC_FIELDS`), never stored text."
- **O4 (§4.2's text).**
  - NOTE-COMMITTED names §3.1's phrase but not §4.2.
  - §4.2's own text carries "Any site not in the register is a STOP, never a copy" and entry (4), and the §4 ruling changes both.
  - The §3.1 bullet covers them only by reference ("the register as amended"). Consider naming §4.2 in the same bullet.
- **O5 (DISCLOSURE's backticks).** DISCLOSURE is read verbatim from the ruling's raw markdown. Every p artifact's disclosure will therefore carry literal backtick characters around 18b0111 ("`18b0111`"). This is faithful to the bytes and harmless, but visible.
- **O6 (`dn` ×2).** p §0.3 lists `dn` once, with no count. The committed records hold it twice (dpo and instruct, item 11 s1), so the TEXT's "×2" counts records and is right.
- **O7 (for @@CHECKS@@).** At the checked bytes, `--selftest` gives 109/109 (exit 0) and `hashes` gives the package value in E41.

## Summary

69 items:
- **CONFIRMED: 60**
- **IMPRECISE: 5**: B5, E2, E31, E34, E36.
- **FAIL: 2**: C2 and E9. Both are the ruling's sha256 abbreviated as `e3de1c03…d006`; the correct form is `e3de1c03…e006`.
- **NOT CHECKABLE: 2**: E4 and E5, Code's actions and future steps.

Every quote checks out character for character:
- the disclosure sentence;
- §2.2's corrected sentence;
- term (e)'s amendment;
- the routing block.

Every count, record, field name and line anchor is right.
