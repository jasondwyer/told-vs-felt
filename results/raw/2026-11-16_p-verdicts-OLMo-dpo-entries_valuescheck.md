# The blind values-check of PROPOSAL-p OLMo-dpo's two entries and its run raw, with Code's dispositions (Code; PI date 2026-11-16)

*The dpo VERDICTS session's values-check of the texts committed with dpo's VERDICTS: the entries `PROPOSAL-p OLMo-dpo — VERDICTS` and `PROPOSAL-p OLMo-dpo — secondary DVs`, and the raw `results/raw/2026-11-16_p-verdicts_OLMo-dpo.txt`. Each checker was a fresh subagent with no part in the drafting. Its brief bound it to the list of record v2, items 1–5, and to the rules of Q-F3's campaign on this laptop, both quoted. It ran no Python, listed or read nothing under `data/mf3`, ran no whole-tree `git status`, opened no file under `data/p/ckpt` (digests only), and opened no sibling unit's output, report or raw. Pass 1 checked the drafts with the counters section and the R1/R2 items left as placeholders; a second, targeted pass checks those. Each report is reproduced verbatim, and Code's dispositions follow it. Calendar dates only; the commit hash is the record.*

## Pass 1: the report, verbatim

Blind values-check: PROPOSAL-p OLMo-dpo — VERDICTS and — secondary DVs drafts, and the run raw

*Versions checked (sha256, first 8 … last 4): `entry_verdicts.md` `6bb9808b…c054` (263 lines), `entry_secondary.md` `708e0205…d7fd` (62 lines), `runraw_dpo.txt` `331ccd95…01fd` (173 lines). Line numbers below are these versions' line numbers.*

**Result:** 188 claims checked: **163 CONFIRMED / 12 IMPRECISE / 0 FAIL / 13 NOT CHECKABLE.**
By text: VERDICTS 135 (115 C, 10 I, 0 F, 10 NC); secondary DVs 36 (35 C, 1 I); run raw 17 (13 C, 1 I, 3 NC).
Skipped placeholders, as instructed (listed only): `entry_verdicts.md` L68–69 `[R1/R2: …]`, L189–190 `[COUNTERS — …]`, L235–238 `[R1/R2: …]`, L253 `[VALUESCHECK — …]`. None in `entry_secondary.md` or `runraw_dpo.txt`.

Method, briefly. Outputs, input and dpo's reports were read with `jq`. Hashes were computed with `shasum -a 256` and abbreviated with `cut` (first 8 … last 4). Quotations were compared character for character with `/usr/bin/grep -F` on line-joined text. Derivations were recomputed with `bc`: the exact binomial tails; the DEAD tail's complement, which is exactly 573·13^79/20^80; the attained power, by enumerating (i)–(iii) at 40/40, .70, sham 32 at .5 and α .01, giving 0.878428578… with critical count 51; and every Clopper–Pearson bound in both entries, by bisection, half-up to 4 places. The raw's code blocks were extracted and compared byte for byte with `cmp`, after substituting `<repo>` and `<scratchpad>` into the sources.

## 1. `entry_verdicts.md`

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | L1–2 | Citations: p v0.2 §8 step 7, §4.4; ADDENDUM-p1 v0.1 §4 step 3; m:358; LOCK-p-OLMo-dpo v1.0; the seat's answers of 2026-11-16, §5 | C | p:130 (step 7), p:90 (§4.4); ADDENDUM-p1:42; m:358 step 17; the answers raw §5 (:35–42). |
| 2 | L2–3 | A0-OLMo-dpo PASS; P = 78/80; Δ_c = +0.4750; CI [+0.4126, +0.4970]; E = 0.1563 (5/32) | C | `arm.state` PASS; `stats` P 39/40, delta 19/40, E 5/32; CP on P recomputed [0.9126, 0.9970]. |
| 3 | L3–4 | Exact one-sided p toward clean = 3241/2^80 | C | `tests.p_up` 3241/1208925819614629174706176 = 3241/2^80; 3241 = C(80,78)+C(80,79)+C(80,80) = 3160+80+1 (bc). |
| 4 | L4 | L0-OLMo-dpo holds → OLMo-dpo row *Answered* (m:338; p's unit the told control; ADDENDUM-p1 §1) | C | m:337–338; ADDENDUM-p1:20; output `rows` {"olmo-dpo": "Answered", "state": "PASS"}. |
| 5 | L5–6 | ANALYZED, COMPLETE at its floors; "the reads" (m:318) open | C | `unit_state` ANALYZED, `ended` COMPLETE; m:318. |
| 6 | L8 | The routing: the PI's of 2026-11-15 (evening), "Route as given", section B, item 6 | C | RESULTS.md:483 (joint-block entry) and :1031–1034 (ADDENDUM-p1 COMMITTED entry). |
| 7 | L8–11 | The item quoted verbatim, beginning `"6. ADDENDUM-p1 v0.1: …` | **I** | The committed record quotes the item without "6. " (RESULTS.md:485, :1034). The text after "6. " matches character for character. No committed file has the numbered form of this text. The seat's raw `1f3ce1f9…` :108 has a different, short form. **Fix:** `…section B, item 6: "ADDENDUM-p1 v0.1: referent check, the answer to its §2.2, then "ADDENDUM-p1 v0.1 — COMMITTED", before any p VERDICTS session [adopt]. Then PROPOSAL-p OLMo-{sft,dpo,instruct} — VERDICTS and — secondary DVs, fresh sessions [go, after its commit]."` |
| 8 | L11 | ADDENDUM-p1 committed first (`fa27c45`) | C | fa27c45 2026-11-15, adds the addendum; joint block 9189623 and the runs come after it. |
| 9 | L11 | The PI's word in chat: "Start them" | C | Quoted at RESULTS.md:487 and in 9189623's subject. |
| 10 | L12–13 | The seat's answers on the joint block (`9189623`), routed with "Route as given", committed at `18102d0` | C | 18102d0 subject ("the PI's "Route as given", PI date 2026-11-16"); name-status adds the answers raw. |
| 11 | L14–15 | Answers raw path; sha256 `01ae2ae7…1b0f` | C | shasum 01ae2ae7a065…5d701b0f. |
| 12 | L15–17 | §5 step 5 quotation | C | Verbatim at the answers raw :41. |
| 13 | L18 | "that routing's item 8, "[yours]"" | C | Answers raw :66 (C. Coordinating session, item 8). |
| 14 | L18–19 | The PI's "Yes, push first", relayed; the push came before the first run | NC | Relayed chat; no committed file quotes it, and no committed record gives the push's time. |
| 15 | L19 | origin at `645bd3f` | C | `git rev-parse origin/main` = 645bd3fe… = HEAD. |
| 16 | L20–22 | ADDENDUM-p1 §2.4's record in m:318's form: Q-F0 A0 PASS (VERDICTS entry 2026-10-19, `0fa8539`); (p-1) committed at `fa27c45` on 2026-11-15, before the first p VERDICTS session | C | ADDENDUM-p1:30; 0fa8539 dated 2026-10-19 (A0 PASS); fa27c45 dated 2026-11-15. |
| 17 | L23–25 | The disclosure, verbatim from the output's `p.disclosure` | C | Character-for-character match. |
| 18 | L23 | Labelled "p §5.4's disclosure" | **I** | p §5.4 (p:102) says "pre-registered on 2026-11-06". The output's sentence, dated 2026-11-07, is F-p3's: the seat's ruling of 2026-11-07 (`38f9974`, `results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md` §1; `valence_core/p/gcal.py:104`). The record labels it "(p §5.4; F-p3's sentence, verbatim)" (LOCK-p-OLMo-dpo.md:259; RESULTS.md:6199). **Fix:** `**p §5.4's disclosure** (F-p3's sentence, `38f9974`; the output's `p.disclosure`, verbatim):` |
| 19 | L27 | The seat's Q1 (c); PIN-35 makes the input "m:318's record" | C | Answers raw :15; m_analyze PIN-35. |
| 20 | L28–29 | Input path; sha256 `f8eac889…b5e2`; committed at `db2e821` before the first run (Q2 procedure (i)) | C | shasum; db2e821 adds `data/p/verdicts/OLMo-dpo_decisions.json`; its subject says so. |
| 21 | L29–30 | Six items, each `other_unit` Q-F0, `other_state` PASS, as the output carries them | C | jq; the output's list equals the input's (`==` true). |
| 22 | L31–45 | The six dated decision texts, verbatim | C | Each `N. date: "decision"` string from jq found with `grep -F` in the line-joined entry text (6/6). |
| 23 | L46–48 | The seat's §1, verbatim | C | Answers raw :17. |
| 24 | L48–50 | Each go taken with Q-F0's PASS and m's three NOT-RUNs known, before any p outcome; each quoted as the block's (iv) quotes it | C | Joint block :170–171 and :182–199. |
| 25 | L51–52 | G-CAL-p go: routing 2026-11-07, item 1, the quotation; `ec0d9d3` | C | Block :183–184. Also present in `ec0d9d3`'s RESULTS.md. |
| 26 | L53–54 | LOCK-p v0.1 and G-TIME go: routing 2026-11-08, item 2, the quotation; each v0.1 header | C | Block :185–186; LOCK-p-OLMo-dpo.md:256. |
| 27 | L55–56 | LOCK-p v0.2 and G-F0m go: routing 2026-11-10, B1, the quotation; each v0.2 header | C | Block :187–188; LOCK-p-OLMo-dpo.md:161. |
| 28 | L57–59 | G-PWR (p), wiring and LOCK-p v1.0 go: routing 2026-11-13, item 4, the quotation; `a2c354e` | C | Block :189–191; present in a2c354e's RESULTS.md. |
| 29 | L60–61 | These sessions: section B, item 6, "[go, after its commit]", and "Start them" | C | Block :199. |
| 30 | L63 | The campaigns' go, given in steps, is the input's sixth item | C | Input item 6. |
| 31 | L64–65 | The three inputs committed before the first run (`db2e821`) | C | db2e821 adds all three. |
| 32 | L65 | The runs went one per window: instruct, dpo, sft | NC | No committed file records the order; the answers raw :23 only says the order "decides nothing". |
| 33 | L65–67 | No p output opened until the third-run notice; Code read no sibling's output or raw | NC | Session attestation. |
| 34 | L67 | The input carries no sibling item | C | Every `other_unit` is Q-F0. |
| 35 | L70–71 | Raw link; one raw, §§1–6; sha256 `331ccd95…01fd` | C | shasum 331ccd95…e07e101fd; the raw has §§1–6. |
| 36 | L72 | "shell only (git, shasum, jq; no Python), names, ids and digests (the list of record v2, item 1)" | **I** | `precheck_dpo.zsh` also uses `awk` and `/usr/bin/grep`. Check 4 greps the lock's text and check 6 runs `jq` over the decisions input. Both are content reads, permitted because neither file is under `data/*/ckpt` or `data/*/reports`, but they are not "names, ids and digests". The checkpoints themselves are touched by digests only. **Fix:** `shell only (git, shasum, awk, /usr/bin/grep, jq; no Python); the checkpoints by names, ids and digests only (the list of record v2, item 1), the lock and the decisions input read for their text.` |
| 37 | L72–74 (and L242) | "It passed twice at HEAD `645bd3f` … once before the window and once in it; the raw carries the second" | NC — **flag** | The raw's pass is at HEAD 645bd3f (`precheck_inwindow.txt`) ✓. The scratchpad's only other precheck capture, `precheck2.out`, is a PASS at **HEAD `db2e821`**. It is otherwise identical and lacks the "no prior capture" line. No capture of a pre-window pass at 645bd3f exists. If `precheck2.out` is the first pass, **fix:** `It passed twice: before the window at HEAD `db2e821`, and in the window at HEAD `645bd3f`, equal to origin after the push; the raw carries the second.` If there were three passes, say so. Make L242 match. |
| 38 | L75 | Scoped status clean on the analyzer's paths | C | Raw §1, check 1. |
| 39 | L76–78 | Seven pinned files, each matching its value of record (the seven abbreviations) | C | All seven by shasum and cut. Values of record: 038bf3e's entry (RESULTS.md:1715); lock §4/§8.1; m_analyze.py:98 `PROPOSAL_SHA256`, :137 `ADDENDUM_M1_SHA256`; valence_core/p/identity.py:41; fa27c45's entry. |
| 40 | L79–80 | Three checkpoint blobs equal HEAD's, by digest only: campaign `07bc2b8d…8141` (the copy-back raw's), time `51f98427…3945`, qual `d1e3b9f1…4a24` | C | Digests only (shasum). Copy-back raw line 5 reads "identical 07bc2b8d…8141 data/p/ckpt/OLMo-dpo_campaign.json". |
| 41 | L81 | Five values (PIN-14's three, p's two) are each named in the lock | C | m_analyze.py:2268–2278; p_analyze.py:156–164. Line counts 5/3/5/5/1 reproduced. |
| 42 | L82 | Three outputs absent (write-once) | C | Raw §1, check 5. |
| 43 | L83–84 | Input committed at HEAD (blob `2952e05c`), sha256, valid, six items | C | `git rev-parse HEAD:…` = 2952e05cfc48…; shasum. |
| 44 | L85–87 | The invocation string | C | Raw §2; stdout line 1. |
| 45 | L87–88 | From the root, at `nice -n 19`, under `jlens-qwen36/.venv/bin/python -B` | C | `run_dpo.zsh`. |
| 46 | L88–89 | "(its usage text: "Path arguments resolve … PIN-V2-8)")" | **I** | The sentence is in p_analyze.py's module docstring (:22–23), quoted correctly. The argparse description, which is the usage text (:697–698), is a different sentence. **Fix:** `(its module docstring: "Path arguments resolve against the repository root when relative (m's ``_cli_path``, PIN-V2-8)")` |
| 47 | L90 | No `--adjudication` (the campaign did not pause), no `--pi-stop` | C | Invocation; output `pauses` [], `adjudication` null. |
| 48 | L90–92 | Window granted after instruct's run ended; one window per run while Q-F3's campaign runs | NC | Relayed; no committed launch record for Q-F3's campaign. |
| 49 | L93–95 | Printed lines: INVOCATION; gate line (V0: 42ab36ecc814c9c4, 955788dec22ee820, d347ea0c9b69f73c, HEAD 645bd3f); the §5 sentence; the `written:` line; two P-OUTPUT lines | C | run.stdout lines 1–6; m_analyze.py:2244 (V0); CLAUDE.md sha256 starts 955788dec22ee820. |
| 50 | L96 | stderr empty; EXIT=0 | C | 0 bytes (sha256 e3b0c442…); run.exit "EXIT=0". |
| 51 | L96–97 | Captures not opened until the third-run notice (the seat's Q2 (ii)) | NC | Session fact. The citation is fine: the answers raw §2 glosses (ii) as "no state read until the third run ends". |
| 52 | L97–98 | End notice verbatim: "dpo verdicts ended, EXIT=0. Window released." | NC | Chat. |
| 53 | L99–103 | Outputs written once; paths and full sha256s; the VERDICTS output records each input's repository-relative path and sha256 (lock, decisions, three checkpoints); the secondary's provenance is the VERDICTS output's | C | shasum a68c1a40…f901 / de363a20…e0f0; jq `.inputs`; the secondary has no `inputs` field. Same form as Q-F0 (RESULTS.md:8777). |
| 54 | L104 | m's schemas `m-verdicts-v1` / `m-secondary-v1`, with `proposal_p_sha256` `42f2977b…3b32` | C | jq. |
| 55 | L104–105, L109 | "and the `p` block (p §4.4)"; "**The `p` block** (p §4.4; …)" | **I** | p §4.4 (p:90) gives "m's schemas plus `proposal_p_sha256`" and no block. The block is the seat's Q7 form of 2026-11-08 (the output's staging note; p_analyze.py docstring :8–10). **Fix:** L104–105 `…and the `p` block (p §4.4; the seat's Q7 of 2026-11-08, as the staging note has it)`; L109 `**The `p` block** (p §4.4 and the seat's Q7 of 2026-11-08; the output's `p`, the same in both outputs)` |
| 56 | L105 | The two `p` blocks are equal | C | jq `$a.p == $b.p` true. |
| 57 | L106–108 | Identities: `d347ea0c…5e48`, `7756dcf4…49bb`, `a3bc7bb9…b22b`, `42ab36ec…6c6b`; in `p`, `d3758fc4…7008`, `a38d93bb…a2d7` | C | Output fields; abbreviated by cut. |
| 58 | L107 | The proposal pin kept (p §4.2's register (3)) | C | p:86, "the proposal pin kept m's". |
| 59 | L108 | "Each is in the lock (raw §1, check 4)." | **I** | Check 4 asserts five values. The proposal pin `42ab36ec…` is in the lock (§4 table, §8.1; 5 lines), but check 4 does not test it; check 2 matched PROPOSAL-m's file to m's pin. **Fix:** `Each is in the lock: five by raw §1's check 4, the proposal pin in the lock's §4 and §8.1.` |
| 60 | L109–111 | `proposal` PROPOSAL-p; one register entry, (3), "clock; roots"; the replacement; "built at p §8 step 6" | C | `.p.register` has length 1, n 3; the quoted text is a substring of `status`. |
| 61 | L112 | The roots quotation; D_p 2026-12-15 (`where` p:100, `problems` []) | C | Verbatim; p:100 gives D_p 2026-12-15. |
| 62 | L113–115 | `decisions_beside`: three NOT-RUN, "dose not completable", paths, `72745cb4…b5b0` / `94869b83…8e96` / `e2ecef56…87e8` | C | jq; shasum of `data/m/verdicts/*_NOT-RUN.json` (digest only). |
| 63 | L115–116 | `declared_sentences` empty; the disclosure; the staging note | C | `{}`; fields present. |
| 64 | L117–123 | The §5 sentence verbatim (PIN-4's clauses in order) | C | Character for character equal to the output's `sentence` and to stdout line 3; PIN-4 text. |
| 65 | L124–125 | m:326's order; not INDETERMINATE-no-read; REVERSE: none holds | C | m:326; `pred` every `_dn` false. |
| 66 | L125 | PASS needs (i)–(iii) toward clean (m:310), α .01 (m:326) | C | m:310, m:326. |
| 67 | L126 | (i) 19/40 > 5/32 (E = abs(P_sham − .5), P_sham = 11/32) | C | Arithmetic. |
| 68 | L127 | (ii) map 0 40/40 = 1.0000, map 1 38/40 = 0.9500 | C | `k0/n0`, `k1/n1`; share0 1/1, share1 19/20. |
| 69 | L128–129 | (iii) P(X ≥ 78) = 3241/2^80 ≈ 2.68 × 10^-21 < .01 | C | bc gives 2.6809 × 10^-21. |
| 70 | L131 | `pred`: `i_up`, `ii_up`, `iii_up` true; every `_dn` false → PASS | C | jq. |
| 71 | L131–132 | DEAD not reached; tail P(X ≤ 78), Bin(80, 13/20), = 1 − 4.76 × 10^-14 | C | bc gives 1 − tail = 4.7564 × 10^-14; exact complement 573·13^79/20^80. |
| 72 | L133–137 | Every rate with its domain (PIN-2's exact forms) | C | `rates` (6 entries) match; PIN-2 text. |
| 73 | L138–139 | `p_up` fraction and its test text | C | Verbatim. |
| 74 | L140–141 | `p_down` = 1208925819614629174706095/…176 = 1 − 81/2^80; test quotation | C | bc: 2^80 − 81 = …095. |
| 75 | L141–142 | `dead_tail` 1 − 4.76 × 10^-14, "over 20^80"; "DEAD iff < 1/40 and k < n" | C | bc: the denominator == 20^80; the numerator is odd and ends in 9, so the fraction is reduced; the quote is a substring of the test text. |
| 76 | L142–144 | `guard_fisher` 1/1, `guard_abs` 1/1, test quotations | C | Verbatim. |
| 77 | L145–146 | Δ_c +0.4750; CP on P [0.9126, 0.9970] (secondary (a), position 1); on Δ_c [+0.4126, +0.4970] | C | Secondary `a.A0-OLMo-dpo.1.interval`; recomputed. |
| 78 | L147–149 | Power of record **0.878** (0.8784; split 40/40, m_S 32), on PIN-3's and m:190's basis, descriptive; each arm ended at its floor | C | Output `power.of_record`, exact 0.87842857802…; independent bc enumeration gives 0.878428578; critical count 51 (P(X≥51) = .00916). |
| 79 | L149 | Realised split 40/40 gives the same, beside | C | `power.realised_split` has the same exact value. |
| 80 | L150 | PIN-4 puts power in the sentence only below a floor (m:247); neither arm is | C | PIN-4; m:247; floors 80/32 met. |
| 81 | L151–153 | Pre-pick 0/80, 0/32; last look = end look at 112; Fisher p = 1, not fired, binding; absolute p = 1, not fired, reported only (m:316, m:326) | C | `guard_last_look`; m:316 (OLMo absolute reported only). |
| 82 | L153 | "(the output's `guard_last_look`: `binding` false)" | **I** | `guard_last_look` has `fisher.binding` true and `abs.binding` false. The parenthetical reads as if the whole block were non-binding. **Fix:** `(the output's `guard_last_look`: `fisher.binding` true, `abs.binding` false)` |
| 83 | L153–154 | No look fired | C | `looks[*].fired` false. |
| 84 | L155–156 | Sham: "E only (tier sham, m:182-183)"; domain 32 of 32; 11/32 = 0.3438 on P-role; map 0 6/16, map 1 5/16; E = 0.15625 = 5/32 | C | `sham`; `counts`. |
| 85 | L156–157 | The campaign reported the sham share nowhere; neither of its reports carries one (m:318) | C | jq paths: no first-pick or share field in `OLMo-dpo_campaign_report.json` or `_campaign_p-report.json`; campaign raw has 0 matches. |
| 86 | L158–159 | Unit outcome; 80/32 domain on 80/32 launches | C | `unit_state`, `ended`, `counts`. |
| 87 | L159–160 | 2 h cap (lock §2; "2 h each") not reached; the campaigns' entry gives no stage total | C | Lock :29–39; RESULTS.md:967 (dpo: "not reached") and :953. |
| 88 | L160–162 | No pause, STOP, quarantine, adjudication or PI-stop record (the five fields) | C | jq. |
| 89 | L163–165 | Row state (m:349; ADDENDUM-p1 §1, §2.1); m:337, m:338; told control "from this entry's commit, v1 included" | C | m:337–338, m:349; ADDENDUM-p1:20. |
| 90 | L166–168 | ADDENDUM-p1 §2.1's list: label; §8.1 status (m:343); A-m1 §2.4 (b); p §5.2's sentence; abstract clause (m:338) | C | ADDENDUM-p1:24; A-m1:42. |
| 91 | L168–171 | At v1, derived by hand and values-checked at POSTING v1 (ADDENDUM-p1 §2.2; fa27c45's entry: the analyzers do not resolve p's states at v1); §2.3's sentence in §8.1 | C | ADDENDUM-p1:26, :28; RESULTS.md:1058. |
| 92 | L172 | "L0-OLMo-c never enters the ceiling" (m:341) | C | Verbatim. |
| 93 | L172–173 | m's NOT-RUN rows beside, as text (p §5.2) | C | p:98. |
| 94 | L174–175 | The covariate line's text | C | Verbatim with LOCK-p-OLMo-dpo.md:383, list dash aside. |
| 95 | L174 | "the lock's §8 line" | **I** | The quoted line, with its "-- beside …" clause, is at :383, in the lock file's v0.1 text ("## 8. The covariate"). The v1.0 text's §8 (:84) is "The values of record at v1.0"; its §8.1 line (:94) carries only the backticked value. **Fix:** `the line of the lock's v0.1 text, §8 (`LOCK-p-OLMo-dpo.md:383`; v1.0's §8.1 carries the value), verbatim:` |
| 96 | L174, L176 | (p §3.2, §5.2, §7); licenses one reported sentence (p §7), decides nothing | C | p:76, p:98, p:118. |
| 97 | L177–178 | Counters over all 112 campaign sessions, none excluded | C | `n_sessions` 112; per-property any-phase 0 in every cell. |
| 98 | L178 | "(the output's `n_excluded_included` 0)" given as the basis for "none excluded" | **I** | The field counts the counter increments made by excluded sessions, not sessions (`valence_core/session.py:351–359`). The Q-F0 entry says so (RESULTS.md, "counts the counter increments those sessions made, not sessions; E9"). **Fix:** `none excluded (the per-property table: 0 sessions excluded in any phase, in every cell; the output's `n_excluded_included`, the counter increments made by excluded sessions, is 0).` |
| 99 | L178 | Each a rate over units generated | C | m:314, "Denominators = units generated". |
| 100 | L179–180 | Round denominators: A0 160/160/423/57; A0s 128/192 | C | `counters.denominators.rounds`. |
| 101 | L181–182 | `cap_hit` 5 of 160 (A0 forced corrupted), none elsewhere; `audit_degenerate`, `harness_echo`, `lexical`, `termination` 0 | C | jq. |
| 102 | L183–185 | Reads 80 / 32 at each position; `low_label_mass` and `top1_not_label` by position | C | `by_key`; totals 13 and 8 agree with `beside`. |
| 103 | L186 | `pre_pick_exclusion` 0 in both arms | C | jq. |
| 104 | L187–188 | p's counters: p §2.3; the seat's §3 Q3 (a); script sha256 `8e7fbed3…6905`; committed with its self-test at `9464f61` | C | shasum; blob e641f812 is the same at the working tree, HEAD and 9464f61; 9464f61's name-status adds the script and its self-test raw. |
| 105 | L191–193 | Per-property table (m:314; VERDICTS-only, m:318); pre-pick the column of record (the seat's C7) | C | m:314, m:318; the output's `reference`. |
| 106 | L194–198 | A0 clean 583, A0 corrupted 217, A0s clean 320 (all 0s); A0s corrupted, no round | C | `per_property_table`; 583 = 160+423, 217 = 160+57. |
| 107 | L199 | The reference: f1 CORR's 7 vs 1; descriptive | C | Output `reference`. |
| 108 | L200–201 | Whole-session validity 80/80 of 80, 32/32 of 32 (PIN-12); scaffold absorption 0 | C | `beside`; PIN-12. |
| 109 | L202 | Round degeneracy 0/320, 0/480; 0/128, 0/192 | C | `beside`. |
| 110 | L202–204 | Read flags: all reads 1/480, 13/480; 0/192, 8/192. First reads 0/80, 4/80; 0/32, 2/32 | C | `beside.read_flags`. |
| 111 | L205–207 | Release (m:271; V3, `readrule.release_full`), quoted | C | Output `release` verbatim; m_analyze.py:2353. |
| 112 | L208–209 | Gate stages' picks (PIN-32, `gate_release`), apart from the counters | C | PIN-32. |
| 113 | L210–213 | G-TIME s = 0 in the domain, first pick P; G-F0m s = 0–7, all in the domain, all 8 P; no released events | C | `gate_release.{time,qual}`. |
| 114 | L214 | Both stages PASS, nothing fired, no adjudication | C | `stage_end` ×2. |
| 115 | L214–216 | Counters beside: G-TIME all 0; G-F0m `top1_not_label` 4 (A0 pos 1; A0s 3, 5, 6), the rest 0 | C | `counters_beside`. |
| 116 | L217–219 | First picks only (PIN-32); free rounds: G-TIME A0 clean 6; G-F0m clean 42, corrupted 6, of 48 | C | `counters_beside.denominators.free_rounds`. |
| 117 | L219–220 | Later picks and exclusion details were Q-F0's E5, E11; not owed (Q4 (b)) | C | RESULTS.md:8933; answers raw :33. |
| 118 | L221 | Campaign's A0s 11/32 | C | — |
| 119 | L221–222 | G-TIME-OLMo-dpo (p)'s 0/1, reported at its stage (`2258c52`), under m:318's exception (2) | C | RESULTS.md:5065 (dpo row, "sham first pick 0/1"); time report `first_pick_P` k 0, n 1. |
| 120 | L223–224 | G-F0m-OLMo-dpo (p)'s 10/16 from the qual report's `first_pick_P`; `a225a89`'s entry did not state it | C | jq gives {"k":10,"n":16}; the entry (RESULTS.md:3240–3356) has no pick share. |
| 121 | L225–226 | Seconds not given: Q-F0's E3 class, not owed (Q4 (b)); the campaigns' entry gives no end time and no stage total | C | RESULTS.md:8821 (E3), :953. |
| 122 | L227–228 | Looks at 40, 80 and the end look at 112; p 1/1; none fired; Fisher binding, absolute reported only (m:330) | C | `looks`. |
| 123 | L229–230 | Q-F0's looks contrast columns were E2; at the end look they are `beside` | C | RESULTS.md:8952. |
| 124 | L231–233 | `CHECKPOINT STATE INCONSISTENT`: 0 in the campaign raw, 0 in this stdout | C | `/usr/bin/grep -c`: 0 and 0. |
| 125 | L239–241 | The 2026-11-16 decisions … "the procedure this entry follows, quoted under "The words"" | **I** | The windows' order is neither quoted nor under "The words"; it is stated under "The siblings" (L65). Its timing ("before any p outcome") is NC: dpo's window followed instruct's run. **Fix:** `Code's reading: they are the procedure this entry follows — quoted under "The words", the windows' order stated under "The siblings" — not items under the seat's Q1 rule.` |
| 126 | L242 | The pre-run check ran twice, before the window and in it | NC | See #37. |
| 127 | L243–244 | "Window released." was the release the coordinating session asked for | NC | Relayed. The disclosure is apt: §5 step 2 and Q2 (ii) ask for "the exit status alone". |
| 128 | L245–246 | The G-F0m sham share is read from its stage report, the read domain (list of record v2, item 2) | C | Item 2 ("for a stage entry's figures …"). |
| 129 | L247–249 | Captures' sha256s unchanged; composed raw placed untracked; `<repo>`/`<scratchpad>` | C | The current sha256s of run.stdout, run.stderr and run.exit equal the raw's §§3–5; scoped `git status` shows `?? results/raw/2026-11-16_p-verdicts_OLMo-dpo.txt`. |
| 130 | L247–248 | The coordinating session's hazard note; Code touched the captures | NC | Relayed or session fact. |
| 131 | L250–252 | m:318's "the reads" quotation; the seat's §5 step 5 and §6; `0fa8539` | C | m:318 verbatim; answers raw :41, :46. |
| 132 | L254–259 | Reads OPEN (§6): 138 = 112 (80 + 32) + 24 (8 + 16) + 2 (1 + 1); one thread after the counters step; Q-F0's read form; the read's raw closes the entry | C | Answers raw :46; `counts`; `gate_release` session counts. |
| 133 | L261 | The seat's read, then the close line (§5 step 6) | C | Answers raw :42. |
| 134 | L262 | POSTING v1: the row by hand under ADDENDUM-p1 §2.2, values-checked by Code | C | ADDENDUM-p1:26. |
| 135 | L263 | v2 through `p_analyze`'s `posting --posting v2` (p §4.4, §5.2) | C | p_analyze.py:714–715 (choices ["v2"]). |

## 2. `entry_secondary.md`

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | L1 | Date; citations (p v0.2 §8 step 7, §4.4; m:358; m:312; PIN-13); issuing no claim | C | Same as Q-F0's form; m:358. |
| 2 | L2–3 | (a), (b), (d), (e) computed by `scripts/p_analyze.py` over m's functions (p §4.4), in the same invocation | C | stdout line 4; m_analyze `secondaries()` (:1326). |
| 3 | L4 | Path and full sha256 | C | shasum de363a20…e0f0. |
| 4 | L5–6 | `m-secondary-v1`, with `proposal_p_sha256` and the VERDICTS output's `p` block | C | jq; the `p` blocks are equal. |
| 5 | L6 | "none -- secondary DVs issue no claim (m:358)" | C | Output `claim`, verbatim. |
| 6 | L6–7 | (c) and (f) are Q-F3's; "(c) and (f) are [Q-F3] (G-ANL-F3)" | C | Output `not_built`, verbatim. |
| 7 | L8–9 | (a), (b), (d) defined against the exclusion rule (m:312; rule 28(a)) | C | m:312; CLAUDE.md rule 28(a). |
| 8 | L9–10 | "(e) is the analyzer's reading of m:312's round event (PIN-13): every round generated…" | **I** | PIN-13 builds (e) but states no domain. m_analyze.py:1355–1359 takes every round of every session of the arm. Q-F0's entry carried exactly this (RESULTS.md, Q-F0 secondary: "built under PIN-13, which the seat accepted at C6; no PIN states its domain"). **Fix:** `(e) is the analyzer's reading of m:312's round event (built under PIN-13; no PIN states its domain): every round generated in the campaign's 112 sessions, excluded sessions included (none here).` |
| 9 | L10–12 | No session excluded in any phase; validity 80/80 and 32/32; so each domain is the whole campaign and (e)'s rounds are its post-exclusion domain | C | `per_property_table`; `beside`. |
| 10 | L12–13 | Floor 20 events (`floor_events`) | C | Output 20; m:312. |
| 11 | L13–14 | CP 95% at or above the floor (`rate()`); `count_only` below | C | m_analyze.py:1272; output fields. |
| 12 | L14 | Every rate is num/den with its domain | C | — |
| 13 | L14–16 | `share` reduced: 70/80→7/8, 46/48→23/24, 21/21→1/1, 0/320→0/1 | C | jq, all four. |
| 14 | L17–18 | (a)'s definition (P-role at choice p; valid through p) | C | PIN-13; `secondaries()`. |
| 15 | L22 | Position 1: 78/80 = 0.9750 [0.9126, 0.9970]; 11/32 = 0.3438 [0.1857, 0.5319] | C | jq; CP recomputed. |
| 16 | L23 | Position 2: 67/80 [0.7382, 0.9105]; 20/32 [0.4369, 0.7890] | C | Same. |
| 17 | L24 | Position 3: 70/80 [0.7821, 0.9384]; 15/32 [0.2909, 0.6526] | C | Same. |
| 18 | L25 | Position 4: 76/80 [0.8769, 0.9862]; 16/32 [0.3189, 0.6811] | C | Same. |
| 19 | L26 | Position 5: 61/80 [0.6542, 0.8505]; 13/32 = 0.4063 [0.2370, 0.5936] | C | Same. |
| 20 | L27 | Position 6: 71/80 [0.7972, 0.9472]; 15/32 [0.2909, 0.6526] | C | Same. |
| 21 | L29 | Position 1 is the primary's domain and share; every denominator ≥ floor | C | 80, 32 ≥ 20. |
| 22 | L30–31 | The f1-crossing quotation | C | Output `f1_crossing_note`, verbatim. |
| 23 | L32–34 | (b) contrast arm only; m:312 "a sham session has no corrupted round"; scope quotation; definition | C | m:312 verbatim; `b.scope`; m_analyze.py:1361–1371. |
| 24 | L35 | After corrupted: 46/48 = 0.9583 [0.8575, 0.9949] | C | jq; CP recomputed. |
| 25 | L36 | After clean: 53/352 = 0.1506 [0.1149, 0.1923] | C | jq; CP recomputed (bc at scale 160). |
| 26 | L37–38 | (d)'s heading (m:312) | C | m:312. |
| 27 | L39–41 | A0 per pair: 21/21 [0.8389, 1.0000]; 19/19 count only; 20/21 [0.7618, 0.9988]; 18/19 count only; m:312's imbalance clause | C | jq; CP recomputed; m:312. |
| 28 | L41–42 | A0 per pair and start order: 0\|0 10/10 … 3\|1 9/10 (8 cells, all count only) | C | `per_pair_start`, all 8. |
| 29 | L43–45 | A0s per pair 4/8, 2/8, 4/8, 1/8 (count only; m:312: "32 … give 8 … per pair"); 8 start-order cells | C | jq; m:312. |
| 30 | L46–49 | `habit.break_rates` over domain sessions (PIN-13); b+ and b_sham meanings; weighted form = Δ_c at any balance | C | valence_core/e2d/habit.py:13–16, :82–83, :105–109; output `identity`; PIN-13. |
| 31 | L50–51 | A0: b+ 39/41, b_sham 0/39; ends 41 + / 39 −; not balanced; 19/40 = +0.4750 = Δ_c; holds; 0 undecidable | C | jq; bc: (41/80)(39/41) + (39/80)(1) − 1/2 = 19/40. |
| 32 | L52–53 | A0s: b+ 5/16, b_sham 10/16; 16/16; balanced; −5/32 = −0.1563 (= P_sham − 1/2); holds; 0 undecidable | C | jq; 5/32 + 6/32 − 16/32 = −5/32 = 11/32 − 1/2. |
| 33 | L54–56 | (e): 0/320 [0, 0.0115]; 0/480 [0, 0.0077]; 0/128 [0, 0.0284]; 0/192 [0, 0.0190] | C | jq; CP recomputed. |
| 34 | L58 | These are the `termination` rounds, none in any cell | C | `counters.termination` 0. |
| 35 | L59–60 | (c) and (f) not built, [Q-F3] (m:312) | C | m:312. |
| 36 | L61–62 | Not a verdict; post-hoc licenses at most a new pre-registration (m:320; rule 11); the values-check is in the VERDICTS raw | C | m:320. |

## 3. `runraw_dpo.txt`

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | whole file | Byte-identical to the untracked `results/raw/2026-11-16_p-verdicts_OLMo-dpo.txt`; sha256 `331ccd95…01fd` (the entry's) | C | `cmp` identical; shasum. |
| 2 | L1 | Title citations: p v0.2 §8 step 7; ADDENDUM-p1 v0.1 §4 step 3; the seat's answers §5 step 2 | C | p:130; ADDENDUM-p1:42; answers raw :38. |
| 3 | L3 | PI date 2026-11-16; one invocation at `nice -n 19`, from the root, on the laptop | C | `run_dpo.zsh` (cd "$R"; one call). |
| 4 | L3 | Window granted after instruct's run ended; order instruct, dpo, sft | NC | Relayed; not in any committed file. |
| 5 | L3 | "the pre-run check, shell only (git, shasum, jq; no Python)" | **I** | The script also uses `awk` and `/usr/bin/grep`. **Fix:** `Before it, the pre-run check, shell only (git, shasum, awk, /usr/bin/grep, jq; no Python).` |
| 6 | L3 | Captures not opened until the third-run notice (the seat's §0 Q2 (ii)) | NC | Session fact. The citation holds (answers raw :8 and :23); §5 step 2's "no session opens a p output" is the more direct one. |
| 7 | L3 | End notice verbatim | NC | Chat. |
| 8 | L3 | Only the root and the scratchpad replaced; nothing else changed | C | Every code block equals its source after the two substitutions (`cmp`); the root occurs only in stdout line 1. |
| 9 | §1 title | At HEAD 645bd3f; the script in §6; then the no-prior-capture check | C | Block line 2 shows HEAD 645bd3fe…. "In the window" is NC (see #4). The no-prior-capture line's command is not shown (NOTE 6). |
| 10 | §1 block | Verbatim copy of `precheck_inwindow.txt` | C | `cmp` same. |
| 11 | §2 | Title; block = `run_dpo.zsh`'s invocation lines, from `<repo>` | C | `cmp` same. |
| 12 | §3 title | 6 lines; captured file's sha256 `7efea8ea…bdf8f3`; the root in line 1 | C | wc -l 6; shasum equal in full. |
| 13 | §3 block | Verbatim copy of run.stdout (root → `<repo>`) | C | `cmp` same. |
| 14 | §4 | stderr empty, 0 bytes, sha256 `e3b0c442…b855` | C | wc -c 0; shasum. |
| 15 | §5 | `run.exit` sha256 `418a5c17…5bd4b`; EXIT=0 | C | shasum equal in full; `cmp` same. |
| 16 | §6 | `precheck_dpo.zsh` verbatim | C | `cmp` same. |
| 17 | §6 | `run_dpo.zsh` verbatim | C | `cmp` same. |

## NOTES

1. **Resolve #37 / #126 before commit.** The scratchpad's `precheck2.out` is a PASS at HEAD `db2e821`. No capture shows a pre-window pass at `645bd3f`. As drafted, "passed twice at HEAD `645bd3f`" rests only on the session's memory; state each pass's HEAD as its capture shows.
2. **Form (Q-F0 VERDICTS), the battery.** Q-F0's entry reported the analyzer's battery of record before the run. This run had none, since the laptop rules bar `p_analyze.py --selftest`/`ganl` while Q-F3 runs, and the draft is silent on it. One sentence would keep the form: no battery ran at VERDICTS, by that rule; the battery of record is G-ANL-p's canonical re-run (`82c3c44`; artifact `d285d776…5604`, the lock's §4).
3. **Form, power.** Q-F0's power line also named "the value G-PWR gave at the floors". The lock's §1 has G-PWR (p)'s "power at the floors (80, 32): .878", which could be cited beside the 0.878.
4. **Form, looks.** Q-F0's looks paragraph carried the printed side of the looks (the sham's `round_degeneracy` and pooled pre-pick exclusions at each look, from the launch entry). The draft gives the guard only. The campaigns' entry (RESULTS.md:967: "none fired", pre-pick 0 / 0) could be cited for it.
5. **Form, V2/V4.** Q-F0's `CHECKPOINT STATE INCONSISTENT` paragraph ended "No V2 or V4 finding against any checkpoint (exit 0)". The same sentence holds here (EXIT=0, stderr empty) and could be added.
6. **Raw §1's last line.** "no prior capture in scratch" is printed by a command that §6 does not show; `precheck_dpo.zsh` ends at `== RESULT`. Show the command, or say what printed the line.
7. **End notice.** "Window released." departs from the seat's §5 step 2 / Q2 (ii) ("the exit status alone"). The entry discloses this for the seat (L243–244). The raw's header quotes the notice with no pointer to that disclosure, which could be added.
8. **The push "behind the screen".** The seat's item 8 puts the push behind the pre-push screen (list of record v2, item 4). The draft does not say whether the screen ran for the push to `645bd3f`. That is NC from here and would come from the coordinating session's record.
9. **Windows' order and "before any p outcome" (L239–241).** dpo's window came after instruct's run had ended, so instruct's output existed, unread. If the order was set before the first run, saying so would make the reading exact. The seat's §2 already holds that the order "decides nothing about a unit".
10. Optional, as in Q-F0's form: cite `rate()` at `m_analyze.py:1272`, and `readrule.release_full`'s line, beside the V3 release.
11. Every other figure in both entries equals the outputs. All Clopper–Pearson bounds, the exact tails, the DEAD tail and the attained power were recomputed independently with bc and agree.

**Not opened:** nothing under `data/p/ckpt` was opened. The three dpo checkpoints were only digested (shasum), as the precheck does. Nothing under `data/mf3` was listed or read. No sibling (OLMo-sft or OLMo-instruct) output, report or `2026-11-16_p-verdicts*` raw was opened; the only sibling-named files touched were m's `data/m/verdicts/OLMo-{sft,instruct}_NOT-RUN.json`, by digest only. No Python ran. No whole-tree `git status` ran (only scoped status), and tree-wide content searches used `git grep` with `':!data/*/ckpt/**' ':!data/*/reports/**'` or `':!data/**'`. Helper files I wrote under the scratchpad's `vcx/` (extracted blocks, bc scripts) were removed after the check; this report is the only file left written.

## Code's dispositions, pass 1

Each IMPRECISE item is applied in the checker's terms; no item was a FAIL. Line numbers are the checked versions'.

**`entry_verdicts.md`**
- **#7** (the routing quoted with "6. "): applied. The item now opens at "ADDENDUM-p1 v0.1:", as RESULTS.md quotes it.
- **#18** (the disclosure's label): applied: "(F-p3's sentence, `38f9974`; the output's `p.disclosure`, verbatim)".
- **#36** (the check's tools): applied, with awk and /usr/bin/grep named, and the lock and the decisions input read
  for their text.
- **#37 and #126** (the check's passes): resolved from this session's transcript. It holds four runs of the check:
  - at HEAD `5a97527`, an earlier form of the script, which failed its decisions check because the input was not yet
    committed;
  - at HEAD `db2e821`, PASS (`precheck2.out`);
  - at HEAD `645bd3f` before the window, PASS. Its output was taken from the transcript into the scratchpad as
    `precheck_prewindow.txt`, sha256 `23de8c5b…2118`;
  - at HEAD `645bd3f` in the window, PASS: the raw's.

  The entry now names all four, the first in a parenthesis.
- **#46** ("usage text"): applied: "its module docstring".
- **#55** (the `p` block's source): applied at both places, citing the seat's Q7 of 2026-11-08.
- **#59** (the identities in the lock): applied: five by raw §1's check 4, the proposal pin in the lock's §4 and §8.1.
- **#82** (`binding`): applied: `fisher.binding` true, `abs.binding` false.
- **#95** (the covariate line's place): applied: the lock's v0.1 text, §8 (`LOCK-p-OLMo-dpo.md:383`), v1.0's §8.1
  carrying the value.
- **#98** (`n_excluded_included`): applied in the checker's words.
- **#125** (the windows' order): applied. The order is stated under "The siblings", now as set by the coordinating
  session before the first run.
- **NOT CHECKABLE items** (#14, #32, #33, #48, #51, #52, #127, #130): relayed words and this session's own acts. Each
  stands as an attestation. The push's screen is named as the coordinating session's record (note 8).

**`entry_secondary.md`**
- **#8** ((e)'s domain): applied in the checker's words ("built under PIN-13; no PIN states its domain … excluded
  sessions included (none here)").

**`runraw_dpo.txt`**
- **#5** (the check's tools): applied in the header.
- **#4, #6, #7** (NOT CHECKABLE): relayed or session facts; they stand.

**Notes**
1. Resolved: see #37.
2. Applied. A sentence under "The run" says that no battery ran with the invocation, and that the lock names G-ANL-p's
   artifact (`82c3c44`; `d285d776…5604`, the lock's §4 and §8.1). The difference from Q-F0's step 17 is disclosed
   under "For the seat".
3. Applied: G-PWR (p)'s .878 at the floors, quoted from the lock's §1.
4. Applied: the printed side of the looks, quoted from the campaigns' entry ("none fired"; pre-pick excluded 0 / 0).
5. Applied: "No V2 or V4 finding against any checkpoint (exit 0)". V2 is m's structural refusal before the release,
   and V4 its read of the records (`scripts/m_analyze.py`'s comments, :2239 and :2336). The run exited 0.
6. Applied. Raw §1 now shows the command that printed "no prior capture in scratch", verbatim from the transcript
   (`no-capture.cmd`).
7. Applied: the raw's header points to the entry's disclosure of "Window released.".
8. Noted in the entry: the push and its screen are the coordinating session's record.
9. Applied: see #125.
10. Applied: `rate()` at `m_analyze.py:1272` in the secondary entry, `readrule.release_full` at
    `valence_core/m/readrule.py:799` in the VERDICTS entry. Both were checked by `/usr/bin/grep -n`.
11. No action.

**The checker's remark on `splice_entries.zsh`:** Code wrote it during the check. It is the splice tool for these
entries, drafted while the check ran, and it touched no text the checker read.

The edits after pass 1 were checked by tool:
- `build_runraw.zsh` rebuilt the raw from the same captures, its four recorded sha256s re-asserted;
- the raw's code blocks are unchanged but for the added command block;
- every new figure and citation above was re-read at its source with `/usr/bin/grep` or `jq`.

The counters section and the R1/R2 items were placeholders at pass 1. They go to a second, targeted blind pass once
the counters step has run.

## Pass 2: the report, verbatim (sha256 `bba56fc193f6031507771df671749b512f94a3a8693df3170cc2f23047182af4`)

*Targeted on the parts pass 1 left as placeholders, once the counters step had run (`922d7a3`): the VERDICTS entry's counters section, its two records of the seat's answer on R1 and R2, and this session's close line on `9464f61`'s entry. Same bindings as pass 1, item 4 with C.2's amendment.*

# Blind values-check, second pass: `entry_verdicts.md` parts (a)–(c) and `close_9464f61.md` (checker, PI date 2026-11-16)

**Result:** 64 claims: 59 CONFIRMED, 4 IMPRECISE, 0 FAIL, 1 NOT CHECKABLE.

How to read the Evidence column:
- "raw:N" is line N of `results/raw/2026-11-16_p-verdicts-counters_run.txt` (blob at `922d7a3` equal to the working tree's).
- "answers" is `results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md`.
- "decisions answers" is `results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md`.
- "output" is `data/p/verdicts/OLMo-dpo_VERDICTS.json`, read with `jq` (sha256 `a68c1a40…f901`).
- "docstring" is the module docstring of `scripts/p_verdicts_counters.py` at HEAD.

## (a) "p's counters at VERDICTS" (entry_verdicts.md L208–254)

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | L208 | Sources: p §2.3; the seat's answers of 2026-11-16, §3, Q3 (a); its second answers, R1 (c) and R2 (b); "Code's own step" | C | PROPOSAL-p v0.2 :68 (§2.3: hair trigger + five counters). Decisions answers §0, "Q3: (a), Code's own step", and §3, "(a)". Answers §0, R1 (c) and R2 (b). raw:12, "(Code's own step; …)". |
| 2 | L209 | `scripts/p_verdicts_counters.py`, sha256 `a87749e9…d6f6` | C | shasum `a87749e9…d6f6`, cut by tool. The working-tree blob is HEAD's (`e0b105c7`). |
| 3 | L210 | committed at `1ceebbf` | C | The script's last commit (9464f61, then 1ceebbf). Blob `1ceebbf:` = `e0b105c7`, HEAD's. |
| 4 | L210 | run once for the three units: exit 0, no STOP | C | raw:3, "One invocation … `--exit OLMo-sft=0 --exit OLMo-dpo=0 --exit OLMo-instruct=0`". raw:5, "Exit 0; stderr empty; no STOP." The stdout has no STOP line (a STOP exits 4; docstring :94–96). The scratch `counters.exit` (EXIT=0) and the empty `counters.stderr` agree. |
| 5 | L210–211 | stdout committed at `922d7a3` as the linked raw | C | 922d7a3 adds that path. raw:12–235 (224 lines) hash to `d77e1c46…9c96`, the header's figure and the scratch `counters.stdout`'s. |
| 6 | L211–213 | "Descriptive (rule 23): no bar, no verdict sentence, no label"; over every recorded round of every recorded session of the three stages, by arm and phase | C | raw:12; answers §0 R1; raw:130, :147, :164. |
| 7 | L214 | p §2.3's five counters and the hair trigger | C | p :68; raw:131–135 (the five counters plus `line_break_in_stored_text`). |
| 8 | L215 | G-TIME: 20 rounds; sham 4 + 6, contrast 4 + 6 | C | raw:129, :131–134. |
| 9 | L215–216 | every counter 0 in every cell; hair trigger 0 of 20 | C | raw:131–136. |
| 10 | L217 | G-F0m: 240 rounds; sham 64 + 96, contrast 32 + 48 | C | raw:146, :148–151. |
| 11 | L217–218 | `corrupted_spelling` 1 on contrast forced A0-OLMo-dpo s=2 forced 0 | C | raw:150, :153. |
| 12 | L218 | every other cell 0; hair trigger 0 of 240 | C | raw:148–152. |
| 13 | L219 | campaign 1,120 rounds; sham 128 + 192, contrast 320 + 480 | C | raw:163, :165–168. The output's `counters.denominators.rounds` (160 + 160, 423 + 57; 128; 192) agrees. |
| 14 | L220 | `cap_hits` 5: s=9, s=24, s=68 forced 0; s=39 forced 0 and 2 | C | raw:167, :170. |
| 15 | L220–221 | "the five rounds the analyzer counts as `cap_hit` on forced corrupted rounds (above)" | C | Derived; it holds. p's `cap_hits` is `bool(r["cap_hit"])` (`valence_core/p/report.py`:236, :289); the analyzer's numerator is `round.cap_hit` (output `counters.declared`). Both read campaign checkpoint `07bc2b8d…8141` (raw:162 = output `inputs.campaign.sha256`). The analyzer has `A0-OLMo-dpo\|forced\|corrupted` 5, total 5; the step has contrast forced 5 and 0 elsewhere. So they are the same five rounds. "(above)" is L202. |
| 16 | L221 | `refusals` 1 (s=24 forced 2) | C | raw:167, :171. |
| 17 | L222–223 | `corrupted_spelling` 9, with the nine round keys | C | raw:167, :172 (keys equal; 9 listed). |
| 18 | L224 | contrast free: `corrupted_spelling` 1 (s=46 free 3) | C | raw:168, :173. |
| 19 | L225 | `control_chars`, `harness_first_line` 0 in every cell; every counter 0 on the sham arm | C | raw:165–168. |
| 20 | L226 | hair trigger 0 of 1,120 | C | raw:169. |
| 21 | L227–228 | at each stage the read domain, recomputed two ways, equals the committed p report's | C | raw:137, :154, :174 ("…: yes"). |
| 22 | L228 | the rest was withheld at the stage reports and is counted here | C | raw:138, :155, :175. The read domain (`valence_core/p/report.py`:280–300) plus the withheld list cover all 20 cells at each stage (NOTES 4). |
| 23 | L229–230 | the key table and match rule of `results/raw/2026-11-11_p-qual_task-correct.txt`, unchanged | C | raw:64 imports `task_correct.py` from that raw (sha256 re-computed: `57e9c7dc…56e2`). raw:66–67 equal that raw's :9–10, compared in the shell. |
| 24 | L234 | G-TIME row 4/4, 6/6, 4/4, 6/6, 10/10 | C | raw:143. |
| 25 | L235 | G-F0m row 63/64, 96/96, 29/32, 47/48, 76/80 | C | raw:160. |
| 26 | L236 | campaign row 127/128, 191/192, 288/320, 466/480, 754/800 | C | raw:180. |
| 27 | L238 | the gate stages' sham rows equal their committed figures (asserted) | C | raw:143, :160, "(the committed figure: equal)". The task_correct raw's :13 and :24 give dpo's 4/4 + 6/6 and 63/64 + 96/96. Answers §0 R1, "recounted and asserted"; raw:58, a row off its figure STOPs. |
| 28 | L238–239 | the campaign's sham row has no committed figure; its first; not asserted | C | raw:180; answers §0 R1. |
| 29 | L240–241 | the alternative reading changes one count: the campaign's contrast free, 465/480 | C | raw:144 and :161, "no count changes". raw:181: of the campaign's four cells only contrast free differs (465 against 466). See NOTES 3 on the "contrast, all" column. |
| 30 | L242 | enters no bar, no verdict sentence and no label (the ruling of 2026-11-09) | C | `results/raw/2026-11-09_p-gtime_design-to-code_answers.md`:34, "it enters no bar, no verdict sentence and no label" (committed at `e619d3d`, 2026-11-09). |
| 31 | L243–244 | each call log is the one its p report records, by sha256 and path; one run; no malformed line; every call attributed to one recorded round (`attribute_calls`); no STOP mark in the run rows | C | raw:139, :156, :176. Docstring :82–83, "the call log's sha256 and path the ones its p report records". |
| 32 | L245–246 | G-TIME proxy: sham 10 of 10, 0 cuts, equal; contrast 10 of 10, 0 cuts; one contrast session, 10 calls | C | raw:140–142. |
| 33 | L247–248 | G-F0m proxy: sham 160 of 160, 0 cuts, equal; contrast 80 of 80, 0 cuts; 10 calls in each of the 8 sessions | C | raw:157–159. |
| 34 | L249–250 | campaign proxy: sham 320 of 320, 0 cuts, equal; contrast 800 of 800, 0 cuts; 10 calls in each of the 80 sessions (s=0–79) | C | raw:177–179. |
| 35 | L251 | "A session's calls are its free-round exclusion position." | I | The seat's words (answers §2.3) are "per contrast session the number of its calls, which is its free-round exclusion position". The draft gives them unattributed, and an exclusion at the sixth free round also leaves 10 calls (row 36). One fix covers L251–252 (row 36). |
| 36 | L251–252 | "Every contrast session here has its 10, so none was excluded at a free round" | I | m's OLMo loop stores the excluding free round, then stops (`valence_core/m/runner_olmo.py`:167, :172). m's PIN: "an exclusion at the last free round leaves it complete" (`valence_core/m/scaffold.py`:435). p's stages run that loop (`valence_core/m/stages.py`:1176). So 10 calls rule out a free-round exclusion only before the sixth free round. **Fix (L251–252):** "A contrast session's number of calls "is its free-round exclusion position" (the seat's §2.3), save that an exclusion at the sixth free round also leaves 10 (`valence_core/m/scaffold.py`:433–435). Every contrast session here has its 10, so none was excluded before its sixth free round, and the per-property table has none excluded in any phase." |
| 37 | L252 | none excluded, "as the per-property table has it" | C | Output `per_property_table`: `sessions_excluded_any_phase` and `sessions_excluded_prepick` are 0 in all four arm × property cells. `counters.n_excluded_included` is 0. |
| 38 | L253–254 | Code's reading on a contrast round with no call (the script's docstring, for the seat) did not arise: every round was attributed | C | Docstring :60–62, "CODE'S READING, for the seat: a contrast round with no attributed call is printed …". raw:141, :158, :178: all rounds attributed, 0 cuts. |

## (b) "The seat's answer on R1 and R2" (entry_verdicts.md L70–77)

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 39 | L71–72 | link path; sha256 `aea918c5…0395` | C | shasum `aea918c5…0395` (cut by tool). The working-tree blob `153f1df5` is HEAD's. |
| 40 | L72 | committed at `52b2c97` | C | `git show --name-status 52b2c97`: A of that path. |
| 41 | L72 | the PI's "Route as given", 2026-11-16, second sitting | C | RESULTS.md:1154–1155 (the coordinating session's close, committed in 52b2c97): "The PI's word on the paste block (PI date 2026-11-16, second sitting), verbatim: "Route as given"". |
| 42 | L73 | It ruled R1 (c), every stage, and R2 (b), the call logs | C | Answers §0: "R1: (c), every stage"; "R2: (b), computed". Its title: "computed from the call logs (R2 (b))". §6 B.2: "R2 (b): the nine call logs". |
| 43 | L74 | given after the three units' VERDICTS outputs existed | C | Answers :3: "the three `_VERDICTS.json` and `_secondary.json` files exist beside the inputs, untracked, so the three runs have ended". |
| 44 | L74–75 | "Not opened: any checkpoint, call log, report or p output" | C | Answers :3; byte-equal once the wrapped line is joined. |
| 45 | L75 | `data/p/verdicts` "listed by name only" | C | Answers :3. |
| 46 | L76–77 | "Recorded here in m:318's form, as a decision about this unit's counters taken after OLMo-sft's and OLMo-instruct's VERDICTS existed, with no output of theirs opened." | I | m:318's form records such a decision "as taken with the other unit's outcome known" (PROPOSAL-m v1.11 :318). This line uses other words: Code's reading, given at L300–303 (row 50). It also leaves out the outcome that was known, Q-F0's PASS with m's three NOT-RUNs, which L30 and L50 carry for every other item. "No output of theirs opened" holds for the seat (its header). **Fix:** "Recorded here under m:318, whose form for a decision about one unit taken after another unit's VERDICTS exist is "as taken with the other unit's outcome known": a decision about this unit's counters, taken with Q-F0's PASS and m's three NOT-RUNs known, and after OLMo-sft's and OLMo-instruct's VERDICTS existed, the seat having opened no output of theirs (its header). Whether m:318's words fit the siblings is Code's reading, for the seat (below)." |

## (c) "For the seat", two bullets (entry_verdicts.md L300–305)

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 47 | L300 | the answer came after the three units' VERDICTS outputs existed | C | Answers :3. |
| 48 | L300–301 | its header says it opened none of them | C | Answers :3, "Not opened: … p output". |
| 49 | L301 | Code's reading: a decision about this unit's counters (descriptive, deciding nothing; rule 23) | C | Labelled as Code's reading. Answers §0 R1, "it decides nothing"; p :68, "deciding nothing (rule 23)". |
| 50 | L302–303 | "recorded above in m:318's form as taken after the siblings' VERDICTS existed, not with their outcomes known" | I | m:318's form is "as taken with the other unit's outcome known". "In m:318's form … not with their outcomes known" contradicts the form it names. It also presents as a recording fact what is Code's reading for the seat. **Fix (whole bullet, L300–303):** "The seat's answer on R1 and R2 came after the three units' VERDICTS outputs existed, and its header says it opened none of them. Code's reading: it is a decision about this unit's counters (descriptive, deciding nothing; rule 23), taken after the siblings' VERDICTS existed but not with their outcomes known. m:318's form records such a decision "as taken with the other unit's outcome known"; whether those words fit it is the seat's to rule, and above it is recorded under m:318 with the facts alone." |
| 51 | L304 | the counters step read all three units' records, as the seat's answers have it | C | raw:5: "each unit's three checkpoints and three call logs, and each stage's committed p report". Decisions answers §4 and §5 item 4; answers §2.2–2.3 and §3 item 4. |
| 52 | L304–305 | the siblings' counts are in its raw; this entry reports OLMo-dpo's | C | The raw has sibling stage sections (headings raw:72, :89, :106, :182, :199, :216). Part (a) reports dpo's only. |

## The close line (close_9464f61.md L1–11)

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 53 | L1 | PI date 2026-11-16; the dpo VERDICTS session's close, on the seat's answer to R1 and R2 | C | Answers :3; answers §6 B ("p (the dpo VERDICTS session, for the three units)"). Commits 52b2c97, 1ceebbf and 922d7a3 are dated 2026-11-16. |
| 54 | L1–2 | the seat's raw §6 block B item 4 | C | Answers :59: "close lines on `9464f61`'s entry citing this raw; ledger (76) [as ruled]". |
| 55 | L2 | its header names this session for this close line | C | Answers :3: "the dpo VERDICTS session and the coordinating session add their close lines". The entry itself is named in §6 B.4, not in the header. |
| 56 | L4 | link path | C | The path was added at 52b2c97. |
| 57 | L5 | sha256 `aea918c5f6f374522ad780ce29685c8c3f950b7457a46933022c090e74680395` | C | shasum equal, full length. |
| 58 | L5–6 | committed by the coordinating session at `52b2c97` | C | 52b2c97 adds the raw. Its RESULTS.md close (:1150–1153), "the coordinating session's line", says the answers "are committed by path here". Answers §6 C.5. |
| 59 | L6 | applied in the script at `1ceebbf` (the dated note above) | C | 1ceebbf modifies the script and RESULTS.md. The dated note (RESULTS.md:728–761) is the entry's last sub-bullet, so it sits above a close appended after it. |
| 60 | L7 | run once for the three units, exit 0, no STOP | C | raw:3, :5 (row 4). |
| 61 | L8–9 | the raw, committed at `922d7a3` | C | 922d7a3 A of that path; blobs equal. |
| 62 | L9 | "Each unit's VERDICTS entry reports its own counts beside the analyzer's outputs." | NC | It is true of dpo's draft (part (a)). The sft and instruct entries are not in the record and I did not open them. The sentence restates decisions answers §3: "each VERDICTS entry reports its counts beside the analyzer's outputs". Optional fix: append "(the seat's answers of 2026-11-16, §3)". |
| 63 | L10 | Ledger (76), the seat's | C | Answers §4, "Ledger — design seat (76)". |
| 64 | L10–11 | the fix, quoted verbatim | C | Byte-equal to answers :41 once the wrapped line is joined. |

## NOTES

1. **Rows 35–36: the sixth free round.** In the OLMo loop that p's gate stages and campaign run (`m_stages.run_gate_stage` and `run_campaign` → `valence_core/m/stages.py`:1176), a free-round exclusion is recorded after its round is stored (`runner_olmo.py`:167, :172). m's own PIN says the session then stays complete: `scaffold.py`:435, "an exclusion at the last free round leaves it complete". So a call count of 10 means either no exclusion or an exclusion at the sixth free round. The entry's conclusion still stands, on the per-property table (`sessions_excluded_any_phase` 0) and `n_excluded_included` 0. The seat's §2.3 sentence has the same edge case; Code may want to mention it to the seat. Optional.
2. **Rows 46 and 50: m:318's words.** The full sentence (PROPOSAL-m v1.11 :318): "A decision about one unit taken after another unit's VERDICTS exist (an OLMo cap, a PI stop, a declined v1.0 after A0 is known) is permitted and recorded in that unit's VERDICTS entry or NOT-RUN record as taken with the other unit's outcome known."
   - Whether "exist, unopened" counts as "outcome known" is left open by the record and belongs to the seat. The fixes keep Code's reading as a reading.
   - Optional support for recording the decision in this unit's entry: decisions answers §2, second paragraph, "A decision that then follows a sibling's VERDICTS is recorded in that unit's entry". It is stated there for the case of a refused or stopped run.
3. **Row 29: optional.** Under the alternative reading, the table's derived "contrast, all" cell for the campaign would read 753/800. The step prints no "all" for that reading, so "one count" holds of the printed cells. Optional wording: "…changes one count: the campaign's contrast free, 465/480 (its contrast, all 753/800)."
4. **Row 22: a label in the committed raw.**
   - The raw's read-domain label reads "the sham rounds' five counters, the corrupted-spelling counter on the sham forced rounds". Yet it lists sham free `corrupted_spelling` among the withheld cells.
   - p's `session_counters` computes four counters over every sham round, and `corrupted_spelling` over sham forced rounds only (`valence_core/p/report.py`:288–292).
   - So the draft's L227–228 matches the cells as computed. The label is in committed stdout, so no change is asked.
5. **L224: optional completeness.** The campaign's contrast-free `cap_hits` and `refusals` are 0 (raw:168) but are not stated. L225's zero clause names only `control_chars`, `harness_first_line` and the sham arm. Optional: "contrast free: `corrupted_spelling` 1 (s=46 free 3), `cap_hits` and `refusals` 0;".
6. **Outside this pass's scope: L69.** L69 has "Code has read no sibling's output or raw". The counters raw, which this session composed and committed, carries the siblings' counts (L304–305 says so). If L69's "raw" means the siblings' VERDICTS raws, saying so would remove the apparent tension.
7. **Cross-checks, all equal.**
   - The raw's dpo checkpoint digests equal the output's `inputs`: time `51f98427…3945`, qual `d1e3b9f1…4a24`, campaign `07bc2b8d…8141`.
   - The output's sha256 is `a68c1a40…f901`.
   - The raw's sha256 is `7360486a…d5e6`, the figure in 922d7a3's message.
8. **My departures, disclosed.**
   - (i) A mistyped redirect wrote two flattened copies of the drafts into the session directory (the scratchpad's parent, outside SCR): `flat_close_9464f61.md.txt` and `flat_entry_verdicts.md.txt`. I deleted both at once, before using them. Nothing in the repository was written.
   - (ii) Some sibling lines of the counters raw reached my screen. None is used in any verdict:
     - the six sibling stage headings (paths and digests), from a heading grep;
     - six sibling proxy lines, truncated (paths, log digests, call counts), from a grep for STOP and exit run to check "no STOP";
     - raw:232–235 (OLMo-instruct's campaign: its contrast proxy cell, calls per session, `task_correct` row, and the start of its alternative-reading line), printed by a tail meant to show only the closing fence.

Not opened or run:
- nothing under `data/p/ckpt`, `data/p/reports` or `data/mf3`;
- not the siblings' `_VERDICTS.json` or `_secondary.json`, nor their VERDICTS raws;
- not the first pass's report or dispositions;
- no interpreter of any kind (Python, node, perl, ruby), no whole-tree `git status`, and no tree-wide content search.

Tools: git, shasum, jq, awk, sed and `/usr/bin/grep`; also tr, cut, fold, cat (scratch files and the close draft only), name-only ls, and rm (on my two stray files only).

Also read, as code or committed text: PROPOSAL-m v1.11 :318, PROPOSAL-p v0.2 :68, RESULTS.md :629–763 and :1150–1175, `valence_core/p/{report,stage}.py` and `valence_core/m/{runner_olmo,scaffold,stages,readrule}.py`, plus the scratch captures `counters.stdout`, `counters.exit` and `counters.stderr`.

## Code's dispositions, pass 2

Each IMPRECISE item is applied in the checker's words; no item was a FAIL. Line numbers are the checked versions'.

- **Rows 35–36** (a session's calls and the sixth free round): applied in the checker's words. The lines it cites were read by tool first: `valence_core/m/scaffold.py`:433–435, m's PIN that "an exclusion at the last free round leaves it complete", and `valence_core/m/runner_olmo.py`:167 and :172, the round stored before its exclusion.
- **Row 46** (the R1/R2 record under m:318): applied in the checker's words.
- **Row 50** (the reading for the seat): applied in the checker's words.
- **Row 62** (NOT CHECKABLE): the sentence now cites its source, "(the seat's answers of 2026-11-16, §3)".

**NOTES**
1. The sixth-free-round case is now in the entry's text, which puts it to the seat.
2. Applied by rows 46 and 50.
3. Applied: "(its contrast, all 753/800)". The sum 288 + 465 was checked with `bc`.
4. No change: the label is in committed stdout (`922d7a3`), and the entry's text matches the cells as computed.
5. Applied: the campaign's contrast-free `cap_hits` and `refusals`, 0, are now stated.
6. Applied: the line now reads "Code has opened no sibling's VERDICTS output or VERDICTS raw; the counters step's raw, which carries every unit's counts, is this session's own."
7. No action.
8. **The checker's departures, disclosed here as it gave them.**
   - (i) A mistyped redirect wrote two flattened copies of the drafts into the session directory, the scratchpad's parent, outside its brief's scratch directory. It deleted both at once, before using them. Nothing in the repository was written.
   - (ii) Some sibling lines of the counters raw reached its screen: stage headings, truncated proxy lines, and four closing lines of OLMo-instruct's campaign section. None was used in a verdict.
   - The counters raw is committed (`922d7a3`) and carries counts, not VERDICTS outcomes.

**The edits after pass 2, checked by tool:** 14 `/usr/bin/grep -F` checks over the final entry and the close line, each fix present and each replaced phrase absent, all PASS. No third blind pass was run.
