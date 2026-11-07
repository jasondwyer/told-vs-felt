# G-ANL-F3 pre-build block: blind values-check and Code's dispositions (2026-11-06)

*Code's raw. One blind refuter (a general-purpose agent with no access to Code's reasoning) checked `results/raw/2026-11-06_ganl-f3_code-to-design_prebuild.md` read-only, against the proposal, ADDENDUM-m1, the prebuild answers, the referent check, LOCK-m-F0, the analyzer of record and Q-F0's VERDICTS. It found 78 items: 63 CONFIRMED, 1 FAIL, 12 IMPRECISE and 2 NOT CHECKABLE (relayed from another session). Code re-checked every FAIL and IMPRECISE item at its source before applying it (§2). The report is reproduced verbatim, except that the session scratch path is shown as `<scratch>/`.*

## 1. The report (verbatim, the scratch path replaced)

78 items: 63 CONFIRMED, 1 FAIL, 12 IMPRECISE, 2 NOT CHECKABLE (relayed from another session)

## Claim-by-claim check

**Header (line 3)**
1. **CONFIRMED.** §9 item 2 and its quotation. answers:63 reads "G-SHAPE-F3 → G-ANL-F3 under Q3's rule → the lock chain to LOCK-m-F3 v0.2; v1.0 on Q7's word". The quoted part is exact.
2. **CONFIRMED.** The PI's routing of 2026-11-06 says "Run the prebuild answers as written" (RESULTS.md:270).
3. **NOT CHECKABLE.** "The coordinating session relayed it after G-SHAPE-F3's commit." This is a relay between sessions, and nothing in the repo records it.
4. **CONFIRMED.** `shasum -a 256 PROPOSAL-m-gating-campaign-v1_11.md` gives `42ab36ecc814…9fc96c6b`.
5. **CONFIRMED.** A-m1 is `f26bc59` ("ADDENDUM-m1 v0.1 COMMITTED"). The file hashes to `ea08322d…9001`, which matches the routing (RESULTS.md:643), and it has no diff against HEAD.
6. **CONFIRMED.** The answers file is committed (`dc1ffe1`). Its sha256 is `aec58440…4df3`, which matches the routing (RESULTS.md:263).
7. **CONFIRMED.** HEAD is `1bf94a6c…`. `git diff HEAD -- scripts/m_analyze.py` is empty. The working-tree sha256 is `655e0f7f…c16f`, and the blob is `4ef8fff4…`, the same as at `ed8e886`.

**§0**
8. **CONFIRMED.** origin/main is `9cbacdb`, and main is 7 ahead. `cd9756e` and `1bf94a6` are both in `origin/main..HEAD`.
9. **CONFIRMED.** No LOCK-m-OLMo file exists at HEAD or in the tree. `git ls-tree -r HEAD | grep -i LOCK-m-OLMo` is empty. `find` over the tree (excluding jlens-qwen36) is empty. The root holds only LOCK-g.md, LOCK-h.md and LOCK-m-F0.md.
10. **NOT CHECKABLE.** The pod-watch claim (no Secure A100 stock in US-CA-2, latest check 18:56) is relayed. No repo record exists, and I did not query runpod.
11. **CONFIRMED.** "Order (a) is open" follows from 9 and answers:26 (a): "G-ANL-F3 before any `LOCK-m-OLMo v0.1`".
12. **IMPRECISE.** "the seat's recommendation is (b) (answers:26), and the PI decides". See below.
13. **CONFIRMED.** "A blinding PIN": PIN-29's refusal reads "(pick-bearing or derived; m:318)" (m_analyze.py:3250–3251), and m:318 is the Blinding paragraph.
14. **IMPRECISE.** "Code's to declare as a PIN at the build", and the §3 heading. See below.

**§1**
15. **IMPRECISE.** "m:291. `m_analyze.py` extended in place". m:291 says "extended, pre-committed". "In place" is the seat's word at answers:25.
16. **CONFIRMED.** m:291's (i)–(iii) as summarised. 16 × (4 + 2 × 13) = 480, plus 1 = 481, and 481 × 5 × 216 = 519,480. The "exactly one" list matches m:291 item for item and in order.
17. **CONFIRMED.** A-m1:44 is §2.5 with items (1)–(3).
    - D_O′ 2026-11-30 is at A-m1:28, as proposed. The PI confirmed it at RESULTS.md:648 and :669.
    - D2 2026-12-22 is at A-m1:40.
18. **CONFIRMED.** answers:23–27 is Q3. answers:26 contains "asserts the OLMo v1 outputs unchanged".
19. **CONFIRMED.** The cd9756e entry (RESULTS.md:56ff, riding texts at :106–111) lists VERDICTS_read.md:83 and round2.md:19. answers:27 says the seat "confirms each by anchor before LOCK-m-F3 v0.1".

**§2 Q1**
20. **CONFIRMED.** Both A-m1:44 quotations match word for word (checked by script).
21. **CONFIRMED.** answers:26 says "with N8's reading: the D_O-era declarations and their comparison date are left as they were". N8 is at referent-check.md:213–217.
22. **IMPRECISE.** "Three facts at source that the record does not address". answers:21 and :25 address the first two. See below.
23. **CONFIRMED.** Q-F0_VERDICTS.json has `analyzer_sha256` `655e0f7f…c16f`, `closure_sha256` `a3bc7bb9…b22b` and `package_sha256` `5f646db6…d771`. Q-F0_secondary.json carries no identity field.
24. **CONFIRMED.** "Any edit … changes the first." The field is the sha256 of the analyzer's committed bytes (:1926, :1933).
25. **CONFIRMED, with a note.** "mf3 … changes the second".
    - The closure at HEAD, recomputed with the analyzer's own `closure()`, is still `a3bc7bb9…b22b`. The analyzer has no mf3 import now.
    - Under PIN-1, the closure keeps every `valence_core.*` module outside `valence_core/m` that loads from the module-level imports plus `LAZY_VERDICT_MODULES` (:1707–1716, :1723–1728, :99). So mf3 changes the closure once the build imports it at module level or lists it there.
26. **CONFIRMED.** The package moved at `71cc23c`. The formula of `package_sha256_of`, applied to git blobs, gives:
    - `d474406`, `ed8e886` and `71cc23c^`: `5f646db6…d771`;
    - `71cc23c`, `db97d8e` and HEAD: `60199b36…feec`.
    - In the working tree, `valence_core.m.resume.package_sha256_of('valence_core/m')` (jlens interpreter, -B) gives `60199b36557ac283771b83dcb4be101b5c56880dceacdecd05cce5a578e7feec`.
27. **CONFIRMED.** "No extended analyzer reproduces those three fields as itself" follows from 24 and 26.
28. **CONFIRMED.** At :1934–1944, `if val not in ltext: raise AnlRefusal(... PIN-14, PIN-1)` runs over the analyzer, package and closure hashes.
29. **CONFIRMED.** LOCK-m-F0.md:147–149 name `655e0f7f…` ("last changed at `ed8e886`"), `5f646db6…` and `a3bc7bb9…`.
30. **CONFIRMED.** The PIN-14 quotation spans :1938–1941. The ellipsis replaces "with every data input and output passed as an absolute path into the main tree".
31. **CONFIRMED.** "Even the analyzer of record, re-run today, is refused, because the package moved."
    - V0 (gate_line checks only file presence and HEAD) and V1 (proposal pin, analyzer and lock committed) pass.
    - At PIN-14 the analyzer `655e0f7f` appears once in the lock and the closure `a3bc7bb9` three times, but `60199b36` never does. So the refusal is the package check.
32. **CONFIRMED.** PIN-29:
    - `BLOCKED_REL` is at :97, `_OpenHook` at :3231–3250, and the register text at :2897–2900.
    - `battery()` enters the hook (:7988), and `run_ganl` calls `battery()` (:8075).
33. **CONFIRMED.** The campaign checkpoint is under data/m/ckpt, and the outputs are under data/m/verdicts.
34. **CONFIRMED.** The VERDICTS `release` field reads "readrule.release_full: … released (m:271)". The VERDICTS commit is `bfc179c`, dated 2026-10-19. The hook works by directory (`p == b or b in p.parents`, :3248).
35. **CONFIRMED.** `git cat-file blob ed8e886:scripts/m_analyze.py | shasum -a 256` gives `655e0f7f…c16f`.
36. **CONFIRMED.** The seven files.
    - VERDICTS `inputs` are campaign, decisions, lock, olmo_states, qual, sentences and time. `flag` is data/m/gates/G-CAL_model-free.json.
    - Under PIN-29's roots: the three data/m/ckpt checkpoints, the two data/m/verdicts declarations and the two outputs, seven in all. The lock, the sentences table and the flag lie outside the roots.
    - All seven are committed (`git ls-files`).
    - Every input's sha256 at HEAD equals the recorded one (dd389eca, 483f32ea, 9a187fbc, 93cf4964, c8320eff, fc7e9db8, af5cb816; flag aad8096a).
    - `adjudication` and `pi_stop_record` are null. `crosscheck_coordinate` only stats for PENDING. A-m1's list has five.
37. **IMPRECISE.** "What (R1) shows: only the code that computes the verdicts changed". See below.
38. **CONFIRMED, with a nuance.** "No blob but `655e0f7f…` can be." PIN-14 tests substring containment, and LOCK-m-F0.md holds 117 distinct 64-hex strings. Of the analyzer's eight committed blobs, only `655e0f7f`'s full sha256 is among them; `66fb5214` and `522e8057` appear only as prefixes.
39. **CONFIRMED.** (R3) is as PIN-14 describes it ("git writes … on the PI's word"), and it runs the analyzer of record.
40. **IMPRECISE.** "Either (R1) or (R2) needs the PIN-29 exception". The block omits that (R2) also meets PIN-14. See below.
41. **CONFIRMED.** 1,080 = 5 × 6³ (m:278). The docstring (:9–10) has "under both values of the 0.12-artifact flag", and PIN-25's 2,160-row table is at :1798–1799.

**Q2**
42. **CONFIRMED.** m:291 has "OLMo 6³". m:278 lists the six values in the text's order.
43. **CONFIRMED.** The m:324 quotation is exact (and m:324 is in §5). m:145 reads "C2 → §5 (a checkpoint still PENDING at the v2 posting is closed there)".
44. **CONFIRMED.** Both m:338 quotations are exact.
45. **CONFIRMED.** The closure gives "analyzed as obtained" (PASS, REVERSE, DEAD or INDETERMINATE) or NOT-RUN, all among the other five.
46. **CONFIRMED.** "Code finds no text that reconciles them". I searched m for 6³, 216, 519,480 and PENDING (including :37, :41, :94 and :343) and found no reconciling text. m:145 points to §5 only.
47. **IMPRECISE.** Q2's record leaves out m:343 and the analyzer of record's `pending-closed-at-v2`. See below.
48. **CONFIRMED.** 2,405 × 91 = 218,855; 2,405 × 125 = 300,625; the sum is 519,480.
49. **IMPRECISE.** The quoted string ("closed at the v2 posting first, m:324") is not m:324's wording, which is "is closed there".
50. **CONFIRMED.** (P2) contradicts m:324's closure.
51. **CONFIRMED.** (P3): 481 × 5 × 125 = 300,625.

**Q3**
52. **CONFIRMED.** The m:291 quotation is exact (bold markup aside).
53. **CONFIRMED.** m:73 reads "built and hashed at LOCK-m-F0 v1.0 when reached, else at the posting, and v2's at LOCK-m-F3 v1.0". The ellipsis keeps the meaning.
54. **CONFIRMED.** The answers:46 quotation is exact. The PI confirmed Q7: "v2's sentence table is built at the Q-F3 VERDICTS session against the posted v1: [confirmed]" (RESULTS.md:267–268).
55. **CONFIRMED.** m:278 has "a placeholder table for the battery".
56. **IMPRECISE.** `posting --posting v1` is cited as `:26–31`. Line 26 belongs to `not-run`. See below.
57. **CONFIRMED.** The m:349 quotation is exact, inside "At each posting … v2 …".
58. **CONFIRMED.** The A-m1:40 quotation is exact. It is a fragment: the session is the analyzer run "and the entries … VERDICTS and … secondary DVs".
59. **CONFIRMED.** The answers:15 quotation is exact. mf3's checkpoint root is data/mf3/ckpt (mf3/stages.py:102, :116).
60. **CONFIRMED.** m:340 says f2 is its own confirmatory pre-registration.
61. **IMPRECISE.** "which Q3's rule bars while an OLMo unit is open". See below.

**§3**
62. **CONFIRMED.** Item 1.
    - `arm_outcome` exists (:246), and no `a3_outcome` exists yet.
    - m:326 gives α .01, "the same with FAIL for DEAD", A3 at α .05 in the order NO-READ → REVERSE → POSITIVE → NULL-x → NULL, and ".927 at P = .65 at the planned floors".
    - The shams A1s, A2s and A3s are at m:184–186.
63. **IMPRECISE.** Item 2's NOT-RUN cause list is incomplete. See below.
64. **CONFIRMED.** m:341: "Q-F3 NOT-RUN sets L1 = false."
65. **FAIL.** Item 3: "Its values are A3's six plus CONFIRMED, DISCORDANT and UNLICENSED." See below.
66. **CONFIRMED.** m:73 has "f2 not required".
67. **CONFIRMED.** Item 4 is consistent with m:340: withheld iff A3 ∈ {POSITIVE, REVERSE}, until f2's VERDICTS or f2's NOT-RUN.
68. **IMPRECISE (nit).** "m:291's six words" should be six values. The mappings are CONFIRMED (m:340: "unlicensed" for the first two, "not run" for the third; m:291 "none" for every no-hit tuple; m:73).
69. **CONFIRMED.** Item 6: POSITIVE and NULL-x↑ point toward clean, REVERSE and NULL-x↓ toward corrupted (m:326, m:310, m:345). The CONFIRMED and DISCORDANT slots follow the screen (m:342). m:342 has "f2's if f2 ran, else the screen's".
70. **CONFIRMED.** Item 7 matches m:312 (lexicons, ±6 window, "ties by token distance → ambiguous", 48 lines, the adjudication exclusion, the pinned seed) and answers:37.
71. **CONFIRMED.** Item 8 matches m:312 ((b) contrast arms only; (f)'s four statistics; the floor of 20).
72. **CONFIRMED.** Item 9(1).
    - The wording is A-m1:44's.
    - VERDICTS_read.md:83 names both quirks.
    - Code check: with a relative path, `_repo_rel(p) == str(p)`, so `_prod_committed` returns "outside the repository" (:1771–1772). `flag_of_record` then returns value False without refusing (:1657–1660).
73. **CONFIRMED.** Item 9(2).
    - A-m1:44 has "each verified against the proposal and this addendum at the run".
    - The 2026-10-19 declarations (clock_passed false, substate `unlocked-before-D_O`) match a reading against D1 = 2026-10-30.
74. **CONFIRMED.** round2.md:19: "a misparaphrase found later is a text correction at the next hash-moving round".
75. **CONFIRMED.** Item 11: G-ANL-F0.json sits at data/m/gates, written once (PIN-25, PIN-37).

**§4**
76. **CONFIRMED.** `ganl/index.txt` and `ganl/m_304_350.txt` exist in the session scratchpad (contents not read).
77. **CONFIRMED.** The BUILD (F3) practice (RESULTS.md:56–75, :105):
    - design raw with PIN register F1–F60;
    - self-test 136/136 and the site check;
    - blind code review and blind values-check;
    - LOCK-m-OLMo check at commit;
    - committed by path, not pushed.
78. **CONFIRMED.** Flags F-1 to F-7 are at mf3-build_design.md:155–161. The riding-text confirmation is answers:27.

## FAIL items and corrections

**65 (§3 item 3).** A3\* never takes POSITIVE or REVERSE. When the screen is not a hit, A3\* is the screen's A3. A hit (POSITIVE or REVERSE) always maps through f2: to CONFIRMED, DISCORDANT, f2's null-class value, or UNLICENSED (m:340). m:342's clauses list exactly seven A3\* values, and m:76 agrees. Replace with:

"Its values are seven: the screen's four non-hit values (NULL, NULL-x↑, NULL-x↓, NO-READ), carried when the screen is not a hit, plus CONFIRMED, DISCORDANT and UNLICENSED. POSITIVE and REVERSE are never values of A3\* (m:340; m:342)."

As the text stands, the battery would claim two values it can never reach, which conflicts with m:291 (i) "every value of A3\*".

## IMPRECISE items and corrections

**12.** Replace with:

"If the pod comes up before G-ANL-F3 commits, order (b) obtains: which order obtains 'is a fact of the calendar that Code records in the BUILD entry' (answers:26). The seat recommends (b) for that case (answers:26), and the pod starts only on the PI's go (RESULTS.md:271)."

**14.** Replace with:

"Every other open reading is Code's proposed reading. It goes into the build-design raw, is declared as Code's PIN at LOCK-m-F3 v0.1, and stays strikable by the seat until LOCK v1.0 (Q8's register, answers:50)."

Apply the same to the §3 heading: "to be declared as PINs at LOCK-m-F3 v0.1".

**15.** Replace with:

"m:291. `m_analyze.py` extended, pre-committed (in place: the seat's Q3, answers:25), with a battery that …"

**22.** Replace with:

"Three facts at source that the record does not resolve for the regression. It touches the first two:
- answers:21: 'LOCK-m-F0 v1.0's package_sha256 (5f646db6…) is Q-F0's record; … `posting` records the three shas without refusing, so a moved package does not block the v1 posting';
- answers:25: PIN-14 binds each unit's analyzer of record, and 'the worktree path is declared and not implemented, and nothing below needs it'.

Neither says how the regression reproduces the three identity fields or reads under PIN-29's roots."

answers:25's "nothing below needs it" bears directly on (R3) and should be cited there.

**37.** Replace with:

"What (R1) shows: with the inputs pinned by sha256 and the identity fields bound to the record's, the code now computing the verdicts (the extended analyzer, on the moved package `60199b36…`) reproduces Q-F0's outputs to the byte."

**40.** Replace with:

"Either (R1) or (R2) needs the PIN-29 exception. (R2), like (R1), must also get past PIN-14 (fact 2):
- with LOCK-m-F0.md as the lock, the extended analyzer is refused;
- with a battery lock text naming its own hashes (as the battery's verdicts cases build one, `scripts/m_analyze.py:4799–4802`), `inputs.lock` (path and sha256 `fc7e9db8…`) also differs from the record, so 'every field except the three' fails on it.

The seat's ruling is asked on both."

**47.** Add to Q2's "The record":

"m:343 lists 'pending' among §8.1's status words 'At each posting', v2 included. The analyzer of record already carries the closure as a v2-only OLMo NOT-RUN cause, `pending-closed-at-v2` ('still pending at the v2 posting, with no session'; cite 'm:324 closed there … else NOT-RUN with the reason recorded'; `scripts/m_analyze.py:413–415`). It refuses that cause at v1 as 'the v2 posting's (G-ANL-F3)' (:2467–2468; PIN-38, :2925–2927). Neither reconciles the 6³ count with the closure."

Item 46's no-reconciliation claim stands.

**49.** Replace with:

"the v2 outputs refuse it (Code's refusal text, 'closed at the v2 posting first', citing m:324, whose words are 'is closed there') and produce none."

**56.** Replace with:

"its analyzer carries `posting --posting v1` (usage at `scripts/m_analyze.py:27–34`; the parser's `choices=["v1"]` at `:8198–8199`)."

**61.** Replace with:

"That moves the blob a second time after LOCK-m-F3 v0.1 names it, which a lock revision can absorb (LOCK-m-F0's analyzer moved twice between v0.1 and v1.0, LOCK-m-F0.md:153–158). Under (a) it also moves the blob after the OLMo locks name it. Q3's rule is worded for G-ANL-F3's in-place commit ('lands only when no OLMo unit is open', answers:26). Code reads it as barring any later in-place analyzer commit while an OLMo unit is open, which PIN-14's binding (answers:25) also implies."

**63.** The list omits m:347's unconditional Clock miss and m:192's k = 0. Both are "units: both" causes in the analyzer of record's PIN-5 (:384–417). Replace with:

"The Clock is D2. The causes are:
- a gate STOPPED with no re-specification locked;
- a blocking stage not at its end with no LOCK v1.0 by D2 (m:347 'A Q-F3 not locked by D2 is NOT-RUN'; m:324 'or any reason'; the seat's C1);
- the PI declining;
- k = 0 at G-F3, so no launch count (m:192);
- no session reaching a first read before a PI stop, a G-VER STOP or the cap (m:324)."

**68.** Replace with:

"m:291's six values (none, confirmed, discordant, not replicated under a passing control, unlicensed, not run)."

The check was read-only. The working tree has the same 28 untracked entries as at the start and no new `__pycache__`. No model was loaded and `--selftest` was not run. Scratch scripts are in `<scratch>/vc3/` (pkg_at.py, hist.py, quotes.py, lock_hashes.txt).

## 2. Code's dispositions (each re-checked at source first)

| item | re-check at source | disposition |
|---|---|---|
| 65 (FAIL) | m:340: A3\* is "the screen's A3 if the screen is not a hit; otherwise … CONFIRMED … DISCORDANT … f2's value if f2 ∈ {NULL, NULL-x↑, NULL-x↓} and f2's control PASSED; UNLICENSED otherwise". So a hit never carries its own value. | **Applied** in §3 item 3, as suggested: seven values, and never POSITIVE or REVERSE. |
| 12 | answers:26; RESULTS.md at `1bf94a6`, line 271: "No pod start without my go." | **Applied** in §0. The RESULTS anchor is pinned to `1bf94a6`, because newest-first entries shift RESULTS.md's line numbers. |
| 14 | answers:50, Q8's register. | **Applied** in §0 and in §3's heading. |
| 15 | m:291 has "extended, pre-committed"; answers:25 has "extends `scripts/m_analyze.py` in place". | **Applied** in §1. |
| 22 | answers:21 and :25, as quoted. | **Applied** in Q1. answers:25's "nothing below needs it" is also cited at (R3). |
| 37 | Fact 1's third point: the package moved at `71cc23c`. | **Applied** in Q1. |
| 40 | `scripts/m_analyze.py:4799–4802` builds a battery lock text naming the run's own hashes; `Q-F0_VERDICTS.json`'s `inputs.lock` records `LOCK-m-F0.md`, sha256 `fc7e9db8…`. | **Applied** in Q1. |
| 47 | `scripts/m_analyze.py:413–415` (`pending-closed-at-v2`, v2-only); `:2467–2468` (refused at v1 as "the v2 posting's (G-ANL-F3)"); PIN-38 at `:2925–2927`; m:343's "pending". | **Applied** in Q2's record. (P1) now says the closure runs upstream through that cause. |
| 49 | m:324's words are "is closed there". | **Applied** in (P1). |
| 56 | `scripts/m_analyze.py:27–34` (the usage); `:8198–8199` (`choices=["v1"]`). | **Applied** in Q3. |
| 61 | LOCK-m-F0.md:153–158 (two analyzer moves at step 15); answers:26's wording. | **Applied** in Q3's alternative. |
| 63 | PIN-5's cause table (`scripts/m_analyze.py:384–417`); m:347; m:192's k = 0. | **Applied** in §3 item 2, as a list. |
| 68 | m:291's six values. | **Applied** in §3 item 5. |
| 3, 10 (NOT CHECKABLE) | Relayed by the coordinating session, as the block says. | No change. The block attributes both to that session. |
