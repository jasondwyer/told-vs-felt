# ADDENDUM-p1 v0.1: Code's referent check (its §5; §4 step 1)

*Code's raw, PI date 2026-11-15. ADDENDUM-p1 v0.1 (`ADDENDUM-p1-olmo-rows-at-the-posting-they-reach-v0_1.md`, sha256 `16cdbc11ec2afcdcb628e113bef799de2a328f6f709db2ea22b278c1faf3cb1b`) checked against every referent its §5 lists and every other source it cites, by a fresh checker given the document, the referents and the list of record v2's items 1–5 verbatim, and no conclusion of Code's; model-free, with no file under `data/` read or listed from the working tree (the checker discloses one committed-tree listing, which printed one committed path name, `data/p/gates/G-PWR-p.json`, a name `3e1b614`'s entry also prints).*

*Result: 44 claims; 38 CONFIRMED, 5 IMPRECISE (each MINOR), 0 FAIL, 1 NOT CHECKABLE (the PI's v1-target words, which the PI's chat reply, relayed by the coordinating session, now carries; see the commit's entry). No substantive item, so no STOP under the addendum's §4 step 1. The MINOR items and the four internal inconsistencies the checker lists are recorded here for the seat; none is applied, since the addendum is committed as placed.*

*The report follows verbatim, except that its two local absolute paths are replaced by `<repo>` and `<scratch>`.*

## The report, verbatim

**Referent check of ADDENDUM-p1 v0.1: no FAIL and no substantive item. 44 claims checked: 38 CONFIRMED, 5 IMPRECISE (all MINOR), 1 NOT CHECKABLE.**

The addendum's sha256 matches `16cdbc11…cb1b`. I changed nothing in the repository. Every quotation matches its source character for character (checked by script). That covers all em dashes and apostrophes, the italics, and m:338's three bracketed alternatives.

Legend (all at <repo>):
- **A** = ADDENDUM-p1-olmo-rows-at-the-posting-they-reach-v0_1.md
- **p** = PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md
- **m** = PROPOSAL-m-gating-campaign-v1_11.md
- **A-m1** = ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md
- **R** = RESULTS.md, which is identical to HEAD `7ab4d2f` (no diff for that path)

| # | Claim (where) | Verdict | Class | Evidence |
|---|---|---|---|---|
| 1 | Addendum sha256 (brief) | CONFIRMED | | `shasum` gives `16cdbc11ec2a…3cb1b` |
| 2 | p v0.2 is tracked at root, named by its `— COMMITTED` entry, and stays of record (A:4) | CONFIRMED | | `git ls-files` lists it. Entry `18b0111` (R:5960) names the file with sha256 `42f2977b…3b32`, which equals the working copy. Its blob `82c9174e` is the same at `18b0111`, HEAD and the working copy |
| 3 | m v1.11 sha256 (A:4) | CONFIRMED | | `42ab36ec…6c6b`. Blob `c74f02bd` is the same at `05c4636`, HEAD and the working copy |
| 4 | A-m1 v0.1 at root is the file committed at `f26bc59` (A:4) | CONFIRMED | | `f26bc59` is the only commit that touches it. Blob `9bb3c9d5` is the same at `f26bc59`, HEAD and the working copy. sha256 `ea08322d…9001`, as in `f26bc59`'s subject |
| 5 | The three LOCK-p v1.0 files are at `038bf3e` (A:4) | CONFIRMED | | `038bf3e` modifies the three lock files. Their current sha256s `fafb786d…2bc4`, `25c52f56…3dcf` and `f71c97c1…0e67` match the entry (R:465ff). No diff since `038bf3e` |
| 6 | "no hash moves"; design, locks and analyzer untouched (A:4) | CONFIRMED | | The addendum edits no file and replaces p's clauses by reference. The locks pin PROPOSAL-p `42f2977b…` (LOCK-p-OLMo-sft.md:48, :90, :186, :262), which is the current file. The locks name no "decision" or m:318 list. §2.2 licenses no hash-moving change |
| 7 | No `PROPOSAL-p OLMo-{ckpt} — VERDICTS` entry exists (A:4, A:16) | CONFIRMED | | No entry heading in R and no log subject. There is also no p `— NOT-RUN` or `— secondary DVs` entry |
| 8 | The picks are in checkpoint files "that no seat and no PI reads before VERDICTS (m:318)" (A:4) | IMPRECISE | MINOR | m:318 bars those reads "with exactly four exceptions". Exception (1) is adjudication reads, with "a revealed pick included". The addendum states the rule with no exceptions. R has no campaign entry at HEAD, and the campaign state on the box cannot be checked here |
| 9 | "Placed untracked … at root" (A:4) | CONFIRMED | | Not in `git ls-files`; shown as `??` in the session's git snapshot |
| 10 | p §5.1's heading clause "(before any p VERDICTS, by construction)" (A:10) | CONFIRMED | | Verbatim at p:96 |
| 11 | p §5.1's row label, cited as "(…, m:338)", described as "by m's units" (A:10) | CONFIRMED | | Verbatim at p:96 (and p:19). m:338 holds the template; the filled-in reason is p's own, and p cites "(m:338)" the same way. "By m's units" is a faithful paraphrase of "labels are m's, Step 2's" |
| 12 | p §5.2 makes p's unit the told control at v2 (A:10) | CONFIRMED | | p:98 |
| 13 | p §8 step 7: "the v2 posting's inputs under §5.2" (A:10) | CONFIRMED | | Verbatim at p:130. "Calls the VERDICTS entries" is a faithful reading of step 7's last clause |
| 14 | As registered, a p outcome is used at v2 only (A:10) | CONFIRMED | | p:96, :98, :130. The PI's routing of 2026-11-06 reads "§5's v2 posting rule and its two declared sentences [adopted]" (R:5973) |
| 15 | "v2 follows Q-F3's VERDICTS (m:349; A-m1 §2.3)" (A:10) | IMPRECISE | MINOR | m:349 and A-m1:40 say "after Q-F3's VERDICTS and Step 4's release, or after D2 on a NOT-RUN". The NOT-RUN branch is omitted; the argument is unaffected |
| 16 | LOCK-p v1.0 ×3 committed 2026-11-14 (`038bf3e`) (A:12) | CONFIRMED | | The entry is dated 2026-11-14 (R:465). The git commit date is 2026-11-15 (−0500); by the program's convention the entry's date is the one used |
| 17 | Box characterized 2026-11-15 at the locks' identifier (`7ab4d2f`) (A:12) | CONFIRMED | | R:24–28: "`641ee466f4553b6a`, each LOCK-p v1.0's identifier of record". Locks: "BACKEND OF RECORD 641ee466f4553b6a" (sft:267, dpo:266, instruct:266) |
| 18 | G-PWR (p) `3e1b614`: "3.35 h at m:205's basis" (A:12) | CONFIRMED | | R:1464–1467: "At m:205's basis the three campaigns come to 3.35 h" (1.17 + 1.17 + 1.01). m:205 is that basis (19.5 s and 22.7 s per session, "+ 26 sessions") |
| 19 | The PI's v1 is aimed at early December; the quote "the most solid paper I could drop on Arxiv early Dec" (A:12, A:35) | NOT CHECKABLE | MINOR | `git grep --untracked`, with data/ excluded, finds the words only in A. The last written target in the record is "mid-December 2026" (A-m1:38). "Weeks before v1" holds either way. The PI's routing is to carry the words |
| 20 | Under p §5.1 as written, v1 would label rows "not run" that had run (A:12) | CONFIRMED | | p:96 fixes the v1 label |
| 21 | p §5.1's declared sentence "has no member for their state" (A:12) | CONFIRMED | | p:96's members are [not yet locked / locked, running / NOT-RUN: reason]; none fits a unit with VERDICTS |
| 22 | m:349 quotation (A:14) | CONFIRMED | | Verbatim, a whole sentence, at m:349 |
| 23 | m:338 "iff its own L0-OLMo-c" and the italic label with its three alternatives (A:14) | CONFIRMED | | Verbatim at m:338, italics included |
| 24 | "applies m's rule to p's units at v1 as p §5.2 applies it at v2" (A:14) | CONFIRMED | | p:98 carries two of m:338's three alternatives; it drops "is pre-registered and pending". Under §1 that third alternative cannot arise for p's unit, so there is no conflict |
| 25 | The rule is total over PASS/DEAD/REVERSE/INDETERMINATE/NOT-RUN (A:16) | CONFIRMED | | Labels from m:338 (L0-OLMo-c := A0-OLMo-c = PASS, m:337); status words from m:343; state set from m:278. PENDING is §1's "neither" case |
| 26 | "It is A-m1 §0.3's case: a schedule change made with every outcome unknown…" (A:16) | IMPRECISE | MINOR | The phrase is verbatim (A-m1:14) and the document, commit and disclosure triple matches. But A-m1 §0.3's case was a Clock-date move (m:347's last sentence) made when "No session of any stage ran". Here p's gate sessions have run, and "unknown" rests on m:318 blinding (which A:4 states) |
| 27 | "the told control at this stage" (A:20) | CONFIRMED | | Verbatim at m:338 and p:98 |
| 28 | The two replaced clauses exist (A:20) | CONFIRMED | | p:96 heading; p:130 last clause |
| 29 | What stands: §5.2's rule and declared sentence; m's NOT-RUN rows "beside p's as text"; §5.3's Clock; §5.4's disclosure (A:20) | CONFIRMED | | p:98 ("beside them as text"), p:90, p:100, p:102. m's three NOT-RUN entries are at R:6146, :6192, :6206 (`0f35954`) |
| 30 | Q-F3: A-m1 (10′) stands; its VERDICTS session runs only after `POSTING v1` (A:20) | CONFIRMED | | A-m1:40 says "runs only after the `POSTING v1` entry exists"; faithful paraphrase |
| 31 | "§8.2's v1 text is A-m1 §2.4 (a)'s" (A:20) | CONFIRMED | | A-m1:42 |
| 32 | "§8.1's status sentence (m:343)" (A:24) | CONFIRMED | | m:343. §8.1/§8.2 are sections of the preprint (m:14) |
| 33 | Then A-m1 §2.4 (b)'s sentence, then p §5.2's declared sentence (A:24) | CONFIRMED | | A-m1:42 and p:98; the order mirrors p:96 |
| 34 | The abstract's OLMo clause in m:338's form by number of passing stages (A:24) | CONFIRMED | | m:338's three-way clause |
| 35 | "L0-OLMo-c never enters the ceiling" (m:341) (A:24) | CONFIRMED | | Verbatim at m:341 |
| 36 | "v1's is Fallback-1 iff L0" (A:24) | CONFIRMED | | m:341 says "At v1: … Fallback-1 iff L0; Fallback-2 otherwise". L0 holds (`0fa8539`) |
| 37 | p §5.2 brings p's states into v2 through `p_analyze` (p §4.4) (A:26) | CONFIRMED | | p:98; p:90 ("The v2 posting of record runs through `p_analyze`") |
| 38 | "the form m:349 gives a posting no analyzer reached, declared here for these rows" (A:26) | CONFIRMED | | m:349: "by hand, values-checked, where no analyzer was reached". The addendum declares the extension to these rows itself |
| 39 | Disclosure sentence is outside §7.5's enumeration (A:28) | CONFIRMED | | m:349 (a)–(c); the same form as p:96 and A-m1:42 |
| 40 | "in m:318's form, that it was computed with Q-F0's outcome known" (A:30) | IMPRECISE | MINOR | m:318's form records a *decision* "as taken with the other unit's outcome known" (likewise m:358 step 17 and A-m1:59). Here the decision is (p-1). The addendum attaches the phrase to the VERDICTS computation, where it is trivially true |
| 41 | "as p §8 step 7 has them" (A:42) | CONFIRMED | | p:130. "Then the seat's reads" matches step 7 and the Q-F0 precedent (`0fa8539`, then `79d462b`) |
| 42 | "p §8's list" (A:44) | CONFIRMED | | p:132 |
| 43 | Every §5 referent exists and is the one the document uses (A:48) | CONFIRMED | | p:90, 96, 98, 100, 102, 130; m:318, 338, 341, 343, 349; A-m1:14, 40, 42. All three entries are ancestors of HEAD |
| 44 | §5's list misses some cited referents (A:48) | IMPRECISE | MINOR | Cited but not listed: m:205 (A:12); the `18b0111` entry (A:4); p §5.1's declared sentence (A:12), where §5 lists only §5.1's heading clause and row label; p §8's entries list (A:44); the PI's words (A:35). All but the last are verified above |

**Substantive items:** none.

**Internal inconsistencies (all MINOR):**
1. §1 says "Everything else in p §5 stands" and lists only §5.2–§5.4. But §2.1 overrides p §5.1's last sentence ("The abstract's OLMo clause at v1 is m:338's 'none' form", p:96) once any row has VERDICTS. This resolves only if "keeps p §5.1's form" is read as limiting §5.1's whole body to checkpoints with neither entry. The abstract clause covers all rows, so that reading is not stated.
2. §1's rule admits a `— NOT-RUN` record, but §2.1 sets the v1 sentence order only for rows with VERDICTS. No declared sentence is fixed for a p row with a NOT-RUN record at v1:
   - p §5.2's sentence says the control "ran";
   - p §5.1's sentence has a "NOT-RUN: reason" member, but is kept only for checkpoints with neither.

   p §5.2 has the same presupposition at v2. The case is narrow: under m:324 a locked unit is NOT-RUN only if no session reaches a first read before a PI stop, a G-VER STOP or its cap.
3. Checkpoints with neither entry keep p §5.1's sentence, which has no member for m:324's PENDING state "awaiting its VERDICTS session" (campaign done, VERDICTS not yet run). §3 item 3's timing could open that window. This gap is already in p §5.1.
4. §2.2 says "at its pre-read", but §4 has no pre-read step; item 1 (the referent check plus the §2.2 answer) is meant.

**Observations:**
- **Support for §0.3 in text it does not cite.** m:324 says "a checkpoint with a VERDICTS entry carries its verdict" at a posting, and p §4.1 (p:84) inherits m:324. m:347 says "at posting each row carries its state". So as registered, p §5.1's heading already sat in tension with p §4.1 plus m:324.
- **Likely answer to §2.2 (from the documents only; I did not read code).** The per-unit verdicts-dir resolution is declared for v2 only: p §4.2 register entry (3) (p:86) and line (c) of each lock (LOCK-p-OLMo-sft.md:147). v1's `posting` runs on m's analyzer (A-m1:44). So the hand path is the likely branch.
- **§2.2 departs from m:349 for these rows.** m:349 calls for "the pre-committed analyzer where it exists"; the addendum declares the hand path instead. Precedent for a by-hand statement in a POSTING entry: A-m1 §2.5's last sentence.
- **Suggestion for item 8.** Code's §4 step 2 statement of each campaign's state should also say whether any m:318 exception read of a p campaign has happened. Item 8 matters only if one has.
- **The 3.35 h figure** includes each unit's 26 gate sessions, which have already run. The campaigns alone come to about 2.9 h by the entry's own per-session figures. The addendum follows the entry's wording.
- **Compliance.** No file under data/ was read or listed from the working tree. One `git show --name-status 3e1b614` printed a committed path name, `data/p/gates/G-PWR-p.json`. Its RESULTS.md entry, which I read, also prints that name and the file's sha256. That is a name and a digest only: nothing under ckpt or reports, and no size or time. Both scratch scripts were model-free and run at `nice -n 19` with `-I -B`.

Files are in <scratch>/podwatch2/refcheck/:
- qcheck.py
- spans.py
