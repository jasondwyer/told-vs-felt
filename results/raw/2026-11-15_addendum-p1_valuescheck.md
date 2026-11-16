# ADDENDUM-p1 v0.1 — COMMITTED: the entry, the commit message and the referent-check raw: blind values-check

*Code's raw, PI date 2026-11-15. A blind values-check of this commit's texts by a fresh checker given the texts, the sources (the addendum, the seat's answers of 2026-11-15 evening, the coordinating session's relays as received, both analyzers, the campaigns' box outputs) and the list of record v2's items 1–5 verbatim, and no conclusion of Code's; model-free.*

*Totals: 66 claims; 52 CONFIRMED, 6 IMPRECISE (rows 22, 25, 45, 46, 52, 59), 0 FAIL, 8 NOT CHECKABLE (this commit's own acts; Code's conduct; one attribution, row 19, whose source the relay record lacked).*

*How the findings were applied, each in the checker's terms:*
- *Row 19 and observation 1: the coordinating session's instruction behind the observation for the seat is now in Code's relay record (its closing bullets had been left out) and is quoted verbatim in the entry.*
- *Row 22 and observation 3: the PI's v1-target words are carried by the PI's chat reply to the coordinating session, not by the routing block; the entry and the referent-check raw say so.*
- *Row 25 and observation 4: the PENDING gap is stated in full ("awaiting its VERDICTS session"), with an observation for the seat that all three p checkpoints are in that state now.*
- *Rows 45 and 46: the terminal state cites m:247; the entry addresses all four of m:318's exceptions and says the checkpoints are not read outside them.*
- *Row 52: the message's §2.2 sentence says the v1 posting cross-checks each unit's declared coordinate against one directory, and that the OLMo rows, the abstract's OLMo clause and §8.1's sentences are done by hand.*
- *Row 59: the referent-check raw's header says no file under `data/` was read or listed from the working tree, and names the checker's one committed-tree name listing.*
- *Observation 2: the B6 quote is marked as the paste block's, in a blockquote, beside the raw's short form. Observation 5: the date is confirmed by the routing; B4–B5 point to the entries they rule; the PI's words to the seat carried with the routing are quoted; "then the seat's reads" is added; the close line the addendum's header names is identified as the pod session's on `7ab4d2f`'s entry. Observation 7 is for the campaigns' entry. Observation 8: each wording named is rewritten (the date, the observation's place, "earlier that day" attributed to the coordinating session, "[go, after its commit]" as given, "no content … read", the PI's second sentence recorded without a reading of Code's, the seat's §4 and its routing block's item B6, and the message's two sentences).*
- *On the coordinating session's word in the window: "his" for the PI is "the PI's" outside verbatim quotes.*
- *Checked by tool after the edits: every quotation against its source, every short and full sha256, and the content rules.*

*The report follows verbatim, except that its one local absolute path (its scratch folder) is replaced by `<scratch>`.*

*In the report, `noreply@anthropic.com` is the commit trailer's address, and `@@VC@@` names the entry's placeholder, filled before the commit.*

## The report, verbatim

**Blind values-check of the ADDENDUM-p1 v0.1 — COMMITTED texts: 66 claims; 52 CONFIRMED, 6 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE.**

I changed nothing in the repository. HEAD moved while I was checking, from `7ab4d2f` to `a215c28` (the coordinating session commits the seat's raw and PROPOSAL-q) and then to `97d160a` (F3's close lines). I re-ran every check that depends on HEAD at `97d160a`. The addendum's referent files are unchanged since `7ab4d2f`: PROPOSAL-m, PROPOSAL-p, ADDENDUM-m1, the three LOCK-p files and both analyzers are clean against HEAD.

Line references: E = entry_p1.md, M = msg_p1.txt, R = the referent-check raw, A = the addendum, S = the seat's answers raw, rel = relay_routing_as_received.txt, RES = RESULTS.md at `97d160a`.

| # | Claim (where) | Verdict | Evidence |
|---|---|---|---|
| 1 | Entry title is §4 step 2's entry name; the title quote "a p checkpoint's outcome enters the posting its VERDICTS entry reaches"; "PROPOSAL-p v0.2's addendum"; "committed by path as the seat placed it" (E:1–2) | CONFIRMED | The quote matches A:1 character for character. A:41, :44 name the entry. A:4 says "Code commits by path". The hash equals the routing's, so the file is unedited |
| 2 | "on the PI's routing of 2026-11-15 ("Route as given"; section B, item 6 [adopt])" (E:2–3) | CONFIRMED | rel:8, :12, :22–24 |
| 3 | No `PROPOSAL-p OLMo-{ckpt} — VERDICTS` entry and no p `— NOT-RUN` record (E:3–4, E:48–49; M:1) | CONFIRMED | At `97d160a` the only VERDICTS heading in RES is Q-F0's (:7604). `PROPOSAL-p OLMo-` appears only at RES:6129 (pre-registered states). No log subject matches. m's NOT-RUN records are titled `PROPOSAL-m …` |
| 4 | Addendum at root, sha256 `16cdbc11…cb1b`, 7,415 bytes (E:5–6; M:1) | CONFIRMED | shasum gives the full value; `wc -c` gives 7415; the file is untracked |
| 5 | "re-hashed before the commit" (E:6) | NOT CHECKABLE | Prospective. Equal at this check |
| 6 | "an addendum, not a new version … no hash moves (its header)" (E:6–7) | CONFIRMED | A:4 |
| 7 | "The seat's answers that place it: their §4 and §10, B item 6" (E:8) | CONFIRMED | S:52 (§4.2, "at root, untracked, with this raw"), S:98 ("Files placed untracked"), S:108 (B6) |
| 8 | Seat raw sha256 `1f3ce1f9…f84b` (E:10) | CONFIRMED | Full value `…5220df84b`, equal at HEAD and in the working tree |
| 9 | Seat raw "committed by the coordinating session" (E:10) | CONFIRMED | `a215c28` adds the path (RES:24, "the coordinating session"). It was still untracked at `7ab4d2f` when this check began |
| 10 | Record of (p-1) is the PI's routing, verbatim (A §3, §4 step 2), relayed by the coordinating session (E:11–12) | CONFIRMED | A:18, A:41 |
| 11 | Paste block header "DESIGN → PI → CODE (master session) — PI date 2026-11-15 (evening)" (E:13) | CONFIRMED | Equal to rel:8 character for character (U+2192, U+2014) |
| 12 | "The date the addendum's header asks the PI to confirm at routing is 2026-11-15" (E:13–14) | CONFIRMED | A:2 |
| 13 | "Route as given" (E:15) | CONFIRMED | rel:12 |
| 14 | Section B item 6, the relay's three lines joined (E:16–18) | CONFIRMED | Equal to rel:22–24 joined with single spaces (§ and em dashes match). It is **not** the wording of S:108 (§10 B6); see observation 2 |
| 15 | "It records (p-1) adopted and the word for the three VERDICTS sessions" (E:18–19) | CONFIRMED | B6 "[adopt]" and "[go, after its commit]"; rel:36, :38; RES:26 ("ADDENDUM-p1 is adopted") |
| 16 | The question "What's your target for v1, in your own words?" (E:21) | CONFIRMED | rel:33 (ASCII apostrophe in both) |
| 17 | The PI's reply, verbatim; "no date of its own; by the convention, Code's date 2026-11-15" (E:21–23) | CONFIRMED | rel:31, rel:29; also RES:84–87 |
| 18 | "(the addendum's §3 item 2)"; "§3 gives the first sentence's words as said to the seat earlier that day" (E:20, E:23–24) | CONFIRMED | A:35 has the same words, lower-case "the", no final period. "Earlier" comes from the relay (rel:33, "earlier today"), not from §3 |
| 19 | The observation is "the coordinating session's instruction" (E:25) | NOT CHECKABLE | No such instruction in either relayed message (rel:1–38), in relay_go_as_received.txt, or in `a215c28`'s entry (RES:83–88) |
| 20 | The addendum's "one decision is the posting at which a p outcome is used"; the gloss of the second sentence (E:25–27) | CONFIRMED | A:4 ("It changes one thing: the posting at which a p unit's outcome is used"). The gloss is interpretive (observation 8f) |
| 21 | Referent-check counts 44 / 38 / 5 (each MINOR) / 0 / 1 (E:29–30; M:4; R:5) | CONFIRMED | Report table: 44 rows numbered 1–44; CONFIRMED 38; IMPRECISE 5, all MINOR (#8, 15, 26, 40, 44); NOT CHECKABLE 1 (#19); FAIL 0 |
| 22 | The PI's v1-target words "which the PI's routing now carries" (E:30; R:5) | IMPRECISE | RES:83–84 (`a215c28`): "the pod session found the block does not, and my verbatim copy of the block confirms it". A separate chat reply to the coordinating session carries the words. Row 19's "to the seat" instance is still uncorroborated |
| 23 | No substantive item, so no STOP; the MINOR items and four inconsistencies are recorded unapplied (E:30–32) | CONFIRMED | Report: "Substantive items: none". Inconsistencies numbered 1–4. A:40. Addendum hash unchanged |
| 24 | Inconsistency: §2.1 fixes the v1 sentences only for VERDICTS rows, not for a p `— NOT-RUN` row (E:32–34) | CONFIRMED | Report inconsistency 2; A:20, A:24 |
| 25 | Inconsistency: p §5.1's sentence "has no member for m:324's PENDING state" (E:34) | IMPRECISE | The report says the missing member is PENDING "awaiting its VERDICTS session". p:96 has "not yet locked" and "locked, running", which are PENDING sub-cases under m:324. The entry drops the qualifier |
| 26 | Raw link `results/raw/2026-11-15_addendum-p1_referent-check.md` (E:35) | CONFIRMED | Matches the raw's intended path; it is committed with this commit (M:9) |
| 27 | §2.2: the analyzers of record do not resolve p's states at v1 (E:36) | CONFIRMED | Follows from rows 28–35. Each LOCK-p v1.0 names both analyzers' sha256 (5 times per lock) |
| 28 | p_analyze `d3758fc4…7008` takes `posting --posting v2` only (E:37) | CONFIRMED | sha256 full value, HEAD equals working tree. p_analyze.py:715 `choices=["v2"]`; also :714, :19; :208 calls `run_posting_v2` only |
| 29 | Docstring "v1 is m's posting (p's units enter none)" (E:38) | CONFIRMED | p_analyze.py:22, character for character |
| 30 | m_analyze `d347ea0c…5e48` (E:39) | CONFIRMED | HEAD equals working tree |
| 31 | v1 posting `run_posting` cross-checks each coordinate (Q-F0 and the three OLMo units) against one verdicts directory (`crosscheck_coordinate`, PIN-23) (E:39–40) | CONFIRMED | m_analyze.py:162 (UNITS), :2850, :2855–2857 (PIN-23), :2877–2878, :2660–2689. One dir, default `data/m/verdicts` (:108, :11349). `--f3-verdicts-dir` refused at v1 (:11345–11346) |
| 32 | Reads Q-F0's output from the same directory (PIN-40) (E:41) | CONFIRMED | m_analyze.py:2886–2897 (on an of-record table, when the file exists) |
| 33 | In m's directory the OLMo units are NOT-RUN (`0f35954`) (E:41–42) | CONFIRMED | RESULTS.md text only: RES:6276, :6322, :6336 name `data/m/verdicts/OLMo-{sft,dpo,instruct}_NOT-RUN.json`; `0f35954`'s subject |
| 34 | So an outcome coordinate there is refused (E:42) | CONFIRMED | m_analyze.py:2683–2685 |
| 35 | Neither analyzer declares a path that brings p's VERDICTS into m's v1 posting (E:42–43) | CONFIRMED | m_analyze.py has no `data/p`, `p_verdicts` or PROPOSAL-p reference. p_analyze posts v2 only |
| 36 | "So the addendum's §2.2 governs … superseded by the addendum" (E:44–47) | CONFIRMED | Faithful restatement of A:26's "if they do not" branch; drops the m:349 aside |
| 37 | No p outcome exists (A §0.4, §4 step 2) (E:48) | CONFIRMED | A:16, A:41; row 3; each stdout shows "contrast: withheld" |
| 38 | "no campaign checkpoint has been read"; "no … checkpoint or call log has been opened" (E:49, E:54; M:6) | NOT CHECKABLE | A process claim. Consistent with copyback_campaign.sh's header ("opens no file's contents") |
| 39 | One invocation per campaign, ended, exit 0 (E:51–52) | CONFIRMED | stamps.txt: "ran {sft,dpo,instruct} invocation 1 exit=0", "ended" for each |
| 40 | Ended COMPLETE, path uncached; COMPLETE is m's terminal status (E:51) | CONFIRMED | Each stdout: "STAGE campaign-OLMo-{u} COMPLETE path=uncached" and "P-REPORT … (p): COMPLETE"; m_analyze.py:738–740 |
| 41 | (d)'s line equal (E:52; M:6) | CONFIRMED | d_lines.txt, three times: `641ee466f4553b6a` equal to each lock's BACKEND OF RECORD (LOCK-p sft:267, dpo:266, instruct:266) |
| 42 | No campaign paused or stopped, so no adjudication read under m:318's exception (1) (E:53) | CONFIRMED | Each stdout has 9 BAR lines at looks 1, 2 and end, all silent (the absolute guard "reported (silent; not binding)"), and no PAUSE/STOP/fired line. "P-REPORT runs: 1". m:318 exception (1) is adjudication transcripts |
| 43 | Copied back by tar, byte-identical by sha256 at both ends (E:55) | CONFIRMED | copyback_campaign.sh:19, :27 use `tar cf - … \| tar xmf -`. copyback_campaign_out.txt: 12/12 "identical" (6 ckpt, 6 reports). Wrapper outputs: my `shasum -c box_campaign/box_sha256.txt` gives 10/10 OK |
| 44 | Outputs "committed with the campaigns' own entry, which follows this commit" (E:55–56) | NOT CHECKABLE | Prospective |
| 45 | "A campaign's terminal status is m's (m:330)" (E:57) | IMPRECISE | m:330 is looks, bars and pauses ("pauses are not verdicts"). The terminal rule is m:247 ("all terminal"), which m's own analyzer cites (m_analyze.py:740) |
| 46 | Checkpoints "which no seat and no PI reads before then (m:318)" (E:58) | IMPRECISE | m:318 has "exactly four exceptions"; same class as the report's row 8. Partly offset by E:53 naming exception (1) |
| 47 | Next: VERDICTS and secondary DVs, fresh, after this commit; each VERDICTS entry carries §2.4's sentence (E:59–60) | CONFIRMED | A:42, A:30; B6. Leaves out A:42's "then the seat's reads" |
| 48 | The entries added to p §8's list (E:60–61) | CONFIRMED | A:44 |
| 49 | "Not pushed. Committed by path." (E:63) | NOT CHECKABLE | Prospective |
| 50 | Message subject line: title quote, `16cdbc11...cb1b`, 7,415 bytes, "Route as given", B item 6 [adopt], "its s3 item 2" relayed (M:1) | CONFIRMED | Title equals the entry's; short form correct; the message is pure ASCII |
| 51 | Message record-of-decision and referent-check bullets (M:3–4) | CONFIRMED | Rows 11–21 |
| 52 | Message s2.2 bullet: "m_analyze's v1 posting resolves every unit from one verdicts directory … so the v1 rows are derived by hand" (M:5) | IMPRECISE | v1 cross-checks an explicit tuple (PIN-23, m_analyze.py:2855); it does not derive states from the directory. Only the OLMo rows, the abstract's OLMo clause and §8.1's sentences are done by hand (A:26), not "the v1 rows" |
| 53 | Message campaign state: COMPLETE x3, exit 0, (d) equal x3, no pause, no adjudication read (M:6) | CONFIRMED | Rows 39–42 ("no checkpoint opened" is row 38) |
| 54 | Message: committed by path (one hunk), values-check raw, not pushed (M:9) | NOT CHECKABLE | Prospective |
| 55 | "No laptop model process ran." (M:9) | NOT CHECKABLE | Whose process, and over what interval, is not stated. Now: `pgrep` finds no `*_sessions` process; RES:26 says Q-F3 launches after the push; origin/main is `16c99d5` |
| 56 | Co-Authored-By trailer (M:11) | CONFIRMED | Matches the attribution line |
| 57 | Raw header: sha256; checked against every §5 referent and every other cited source (R:3) | CONFIRMED | Report rows 43–44; only the PI's words were uncorroborated (#19) |
| 58 | Raw header: "a fresh checker given the document, the referents and … items 1–5 verbatim, and no conclusion of Code's" (R:3) | NOT CHECKABLE | No brief is saved; SCR/refcheck holds only qcheck.py and spans.py |
| 59 | Raw header: "with nothing under `data/` read or listed" (R:3) | IMPRECISE | The report (R:87) says "from the working tree" and discloses `git show --name-status 3e1b614` printing `data/p/gates/G-PWR-p.json` |
| 60 | Raw header: result counts, no STOP, nothing applied (R:5) | CONFIRMED | Row 21; the "routing now carries" clause is row 22 |
| 61 | Report verbatim except exactly the two path replacements (R:7) | CONFIRMED | Script: the embedded report with `<repo>`/`<scratch>` undone equals refcheck_report.md, and the reverse also holds. One occurrence of each. The report has exactly 2 absolute paths |
| 62 | No clock time in the three texts | CONFIRMED | Regex scan: no hh:mm, T-times, UTC/EST/Z |
| 63 | No money figure | CONFIRMED | Scan |
| 64 | No IP address or port | CONFIRMED | Every colon-number is a line citation (m:, p:, A:, A-m1:, R:, LOCK-…md:, sft:/dpo:/instruct:, or a ", :N" continuation) |
| 65 | No local absolute path | CONFIRMED | None in E or M; R has only `<repo>` and `<scratch>` |
| 66 | No email except the trailer | CONFIRMED | Only `noreply@anthropic.com` (M:11). E:62's `@@VC@@` is a placeholder |

**Counts:** CONFIRMED 52, IMPRECISE 6 (#22, 25, 45, 46, 52, 59), FAIL 0, NOT CHECKABLE 8 (#5, 19, 38, 44, 49, 54, 55, 58).

**Observations**

1. **#19, the attribution "(the coordinating session's instruction)".** Nothing on record supports it: neither relayed message, nor the other relay file, nor `a215c28`'s entry. Either add the message that gave the instruction to the record, or drop the attribution.

2. **Two different "B item 6" texts.**
   - E:16–18 quotes the paste block's B6 as relayed (correct against rel:22–24).
   - E:8 points to the raw's "§10, B item 6", whose words differ: S:108 reads "the referent check, the answer to its §2.2, the commit [adopt]; then the three VERDICTS sessions [go, after its commit]".
   - RES:32 calls the paste block "the block in fuller words". A reader who follows the link will find a different B6. The entry should say the quote is the paste block's.
   - The quote also nests straight double quotes (`… then "ADDENDUM-p1 v0.1 — COMMITTED", before …`), so where it ends is unclear.

3. **#22.** "The PI's routing now carries" the words contradicts RES:83–84. The words came in a separate chat reply, to the coordinating session rather than to the seat.

4. **#25 matters now.** By the entry's own state bullets, all three p checkpoints are now in m:324's PENDING "awaiting its VERDICTS session" sub-case (campaign COMPLETE, no VERDICTS). That is exactly the sub-case p §5.1's sentence has no member for. The shortened wording hides this.

5. **What §3 and §4 step 2 ask for that the entry leaves out.**
   - (a) §4 step 2, "the PI's routing quoted verbatim": the entry quotes only the header, the word and B6. It leaves out B4–B5 and the PI's words carried with the routing ("Pods are a go. Everything that's waiting on me is a Go.", rel:10). This is defensible if only B6 bears on (p-1), but it is not stated.
   - (b) §3 item 1: the entry puts the block's date beside the addendum's requested date but never says the routing confirms it. rel:36 does say so.
   - (c) §3 item 2: the "to the seat" statement remains uncorroborated.
   - (d) §4 step 2's campaign state covers only m:318's exception (1). Exceptions (2)–(4) are not addressed, although the referent check's suggestion asked about "any m:318 exception read".
   - Outside §3 and §4: A:4's "the pod session adds its close line" is not addressed, and E:59–61 leaves out A:42's "then the seat's reads".

6. **#45:** cite m:247 (or keep m:330 only for "pauses are not verdicts").

7. **#43:** the copy-back printed its own comparison only for the 12 data/p files. The wrapper outputs' equality rests on box_sha256.txt plus my check. The campaigns' entry should record that comparison.

8. **Wording a reader could take two ways:**
   - (a) E:13–14, the date sentence: confirmed by the routing, or just restated?
   - (b) E:25: the observation sits under "the PI's routing, verbatim".
   - (c) E:23–24: "earlier that day" reads as §3's words, but it is the relay's.
   - (d) E:59: "on the PI's word" may read as a further word still to come; B6 already gives it.
   - (e) E:49/54: "read/opened". tar and sha256sum read the bytes; the meaning is that no content was read.
   - (f) E:25–27: the PI's second sentence could be read as indifference to (p-1) or as support for it.
   - (g) E:8: "their §4 and §10, B item 6" has two possible groupings.
   - (h) M:5 (#52) and M:9 (#55).

9. **Insertion point.** At `97d160a` the entry goes at RES:24, above `a215c28`'s entry. The R:NNN anchors in the report are pinned to `7ab4d2f` by its legend, so they stay valid despite the drift.

10. **My compliance.**
    - Nothing under data/ was read, listed or searched in the working tree.
    - I read copyback_campaign_out.txt with every digit masked. I read stamps.txt and the stdouts with runs of two or more digits masked; the launch stamp was not seen.
    - **Disclosed departure:** one committed-tree count, `git diff --name-status 7ab4d2f HEAD -- 'data/**' | wc -l`, printed only "0", no names.
    - One `pgrep -f` boolean, with no file access.
    - Path-scoped git forms only; nothing was written in the repo.
    - Python was model-free, run at `nice -n 19` with `-I -B`.

Scratch files are in <scratch>/podwatch2/vc4/:
- cmp_report.py
- qcheck.py
- scan_chars.py
