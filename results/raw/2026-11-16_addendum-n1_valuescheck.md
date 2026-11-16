# `ADDENDUM-n1 v0.1 — COMMITTED`: the blind values-check of its entry, the PI-routing raw and the referent-check raw's §2, with the dispositions (PI date 2026-11-16)

Code's raw for `ADDENDUM-n1 v0.1 — COMMITTED`. One blind checker, a subagent of the coordinating session, under a
brief quoting the list of record v2's items 1–5 (with item 4's amendment by C.2 of this date) and allowing no
interpreter, checked three texts: the entry's draft, `2026-11-16_second-sitting_pi-routing.md`, and §2 of
`2026-11-16_addendum-n1_referent-check.md`, against the addendum, the seat's raws at `52b2c97`, the saved paste block,
PROPOSAL-n v0.2 and RESULTS.md. Its report is reproduced whole, as its hand-back message gave it; it held no local
path. SCRATCH is the coordinating session's scratch folder. Its line numbers are the drafts' as checked. Code's
dispositions follow it.

## 1. The checker's report, whole

BLIND VALUES-CHECK: the draft entry `ADDENDUM-n1 v0.1 — COMMITTED`, the PI-routing raw, and §2 of the referent-check raw

**Result:** 1 FAIL, 4 IMPRECISE (all minor), no other defects.
- The FAIL is in the entry: the quotation "No checkpoint's weights were loaded" is attributed to `645bd3f`'s entry, but the entry does not contain it.
- The routing raw's fenced block is byte-identical to SCRATCH/paste_block.txt.
- The addendum's sha256 and byte count are confirmed.

## HEADER

**Texts checked (full sha256 as printed by shasum):**
- SCRATCH/entry_n1.md: c8bc00c7095f5d4f9eb429fdb78e74c7ba9172c9d40f9c05a86afb472205caa1
- results/raw/2026-11-16_second-sitting_pi-routing.md: 632f31cba0a5c58801fdfa60b91f3aa28da87aa95ed835b3f2c7b708abfbe281
- results/raw/2026-11-16_addendum-n1_referent-check.md: 717eb7fe566342dc4da8ce81afa31e16fc658d86bc2f86310eab5364614be880. I graded §2 only, checking it against §1.
- SCRATCH/paste_block.txt: cde49b4ee8d8cc8f8769ee43a94d39eacd5fdf5971945d9911a55ea31703e644

**Sources read:**
- The addendum, in full. sha256 e979f8f2af08ddb1f32e3054c002b1d0a3278e49a24b4f6df2cb6c042de95e03, confirmed. 15,804 bytes. Untracked at root.
- The seat raws at `52b2c97`: n-build (B) and n-ganl (G) in full; p-counters :1–40. All three sha256s equal the paste block's figures, and B's and G's HEAD blobs equal their working copies.
- `git show 52b2c97 -- RESULTS.md` and `git show 645bd3f -- RESULTS.md`.
- `645bd3f`'s STOP block: :1–40, plus a grep for "weights".
- PROPOSAL-n v0.2: its headings, :105–125 and :146–166. sha256 30a3d0f5…04f4 (abbreviated by cut); tracked and clean.
- RESULTS.md: targeted lines and greps (:197, :240–242, :955, :1106, :1419–1423, entry headings since 2026-11-06).
- Anchor greps on `bedc198:RESULTS.md` and `52b2c97:RESULTS.md`.
- `14e65d8`'s and `5a97527`'s RESULTS.md diffs, grepped for "join".
- CLAUDE.md, grepped for rule 5(f)(ii).
- `git log -12`, and a name-only `ls data/n`.

**Tools:** shasum; cut; rev; cmp (with process substitution); sed; /usr/bin/grep; tr; od -c and tail -c (on the scratch paste block only); wc -l; wc -c (on the root addendum only); cat -n; git log, git show (blobs, diffs, --name-status), git status --porcelain scoped to named paths, git ls-files, git rev-parse vs git hash-object; name-only ls; the Read tool.

**Conduct:**
- I ran no interpreter of any kind (no python, node, ruby, perl or awk), edited nothing and wrote no file. One redirect went to /dev/null.
- Nothing under data/ was read beyond `ls data/n`. Nothing under data/mf3, ckpt or reports was touched.
- No whole-tree status, no --stat or --numstat, no tree-wide search or pickaxe, no contact with the pod.
- In SCRATCH I opened only entry_n1.md and paste_block.txt. The other files there were listed by name and left unopened.

**Disclosures:**
- `git log -1 --format='%B' 645bd3f | grep weights`: a full-message format, outside item 1's "ids, subjects and commit times". The message is one line, its subject.
- `git log -12` used `%ad` (author date), not `%cd`.
- `wc -c` on the root addendum, to check 15,804 bytes. It is outside data/ and outside item 2's scope.
- `ls -1` of the repo root piped to grep (name-only).

## CLAIMS

### Text 1: the entry (draft line numbers)

- **E1** :1 — date 2026-11-16, the routing's "PI date 2026-11-16 (second sitting)". CONFIRMED (paste :1).
- **E2** :1 — entry name `ADDENDUM-n1 v0.1 — COMMITTED`. CONFIRMED (addendum :84, §8.3 (2) and its entries list).
- **E3** :1 — "PROPOSAL-n v0.2's addendum". CONFIRMED (addendum :1).
- **E4** :1–2 — the title quotation. CONFIRMED verbatim (grep -F; addendum :1).
- **E5** :2 — "committed by path as the seat placed it". CONFIRMED. Paste :3 says "Code commits by path on your routing, re-hashing each first", and the file's sha256 and bytes equal paste :11.
- **E6** :3 — "Route as given"; items 5 and 6 [adopt]; item 10 [adopt]. CONFIRMED (paste :20, :21, :27, :31).
- **E7** :4 — no read at this commit. NOT CHECKABLE (a state at this commit). Consistent with E41–E44.
- **E8** :5 — the file name, at root. CONFIRMED (scoped porcelain shows `??`).
- **E9** :6 — full sha256. CONFIRMED (shasum).
- **E10** :6 — 15,804 bytes. CONFIRMED (wc -c 15804; paste :11 "15,804 B").
- **E11** :6 — "re-hashed before the commit". NOT CHECKABLE.
- **E12** :6–7 — "an addendum, not a new version"; PROPOSAL-n v0.2 (30a3d0f5…04f4) stays the proposal of record (its header). CONFIRMED (addendum :4; shasum and cut).
- **E13** :7–8 — the seat placed it with its two n answer raws, committed by path at `52b2c97`. CONFIRMED (paste :3–16; B:3; G:3; `52b2c97` --name-status adds both).
- **E14** :9 — "(the addendum's §8.2 and §8.3 (2))". CONFIRMED (addendum :82, :84).
- **E15** :9–12 — the whole block with the PI's word, "byte for byte as saved on receipt". CONFIRMED for the bytes (see P9); "on receipt" is NOT CHECKABLE.
- **E16** :13 — the header quotation. CONFIRMED verbatim (paste :1).
- **E17** :13–14 — the routing confirms the date the header asks the PI to confirm, 2026-11-16. CONFIRMED. Addendum :2 reads "PI date 2026-11-16 (the PI confirms the date at routing)"; see also §8.2 (1).
- **E18** :15 — "Route as given". CONFIRMED (paste :31).
- **E19** :18 — item 5. CONFIRMED. Byte-equal to paste :20 once the block's one leading space is removed (shell string compare).
- **E20** :20 — item 6. CONFIRMED (paste :21, same way).
- **E21** :22 — item 10. CONFIRMED (paste :27, same way).
- **E22** :24 — items 7–9 as "the rest as the seat's rulings on Code's blocks" (§8.2 (4)). CONFIRMED (addendum :82 verbatim; paste :22–24).
- **E23** :24–25 — relayed to the n-build and n-analyzer sessions. NOT CHECKABLE (relay).
- **E24** :25 — recorded in the close lines at `52b2c97`. CONFIRMED. RESULTS.md :242 reads "Items 7 and 8 are relayed verbatim to the n-build session"; :955 reads "Its item 9 is relayed verbatim to the n-analyzer session".
- **E25** :26 — "(§8.4; §8.3 (1))". CONFIRMED (addendum :86, :84).
- **E26** :26–27 — a fresh blind checker, against §8.4's referents and the other sources the addendum cites. CONFIRMED as the raw records it (:3–7; §1 obs 1, :189–191).
- **E27** :27–28 — 101 items: 93 CONFIRMED, 6 IMPRECISE (1 substantive, 5 minor), 0 FAIL, 2 NOT CHECKABLE. CONFIRMED (raw :172–176). Recounted by tool: 101 items; IMPRECISE are #2, #16, #22, #37, #77, #94; NOT CHECKABLE are #100, #101.
- **E28** :29–30 — addendum §1.2 (iii) gives no disposition. CONFIRMED (addendum :22).
- **E29** :30–31 — quotation from the n-build raw's §1.2 (iii). CONFIRMED verbatim (B:19, inside §1.2 at B:16).
- **E30** :31 — "The PI's item 7 routes that raw's rulings "as ruled"". IMPRECISE (see fixes).
- **E31** :31–32 — the addendum's header names the seat's answer raws as the place of its reasoning. CONFIRMED (addendum :4: "whose reasoning is in the seat's two answer raws of this date").
- **E32** :32–33 — Code's grading: no STOP; the seat may regrade. CONFIRMED as the raw records it (§2 :216–222).
- **E33** :34–35 — five minor items and fourteen observations recorded, unapplied. CONFIRMED (§2 :224, :226; 14 observations counted at §1 :189–209; the addendum's sha256 equals the placed figure).
- **E34** :35 — "Four bear on what runs next". CONFIRMED as §2's selection (observations 6, 7, 12, 13; :226–237).
- **E35** :35–36 — the tolerance is in practice the identity bound, across two implementations. CONFIRMED (§1 :196–198).
- **E36** :36–37 — the pause precedence and the cap clause reach Code via §8.2 (4), not §8.3 (3). CONFIRMED. §1 :202; addendum :84 (3) names neither; B:61; paste :23 reads "the pause precedence and the cap clause fixed".
- **E37** :37 — the shadow contrast tests presence; 5(f)(ii) names the sign. CONFIRMED (§1 :207; addendum :56; n:121; CLAUDE.md:292).
- **E38** :38 — the n-build raw attributes to `14e65d8`'s entry what is `5a97527`'s. CONFIRMED. B:18; RESULTS.md:1106 "the exact join is the lock's" was added by `5a97527`'s diff; `14e65d8`'s RESULTS.md diff has no "join". See O3 on the wording.
- **E39** :39–40 — the raw holds the report whole and Code's grading. CONFIRMED (raw :10, :211); that the report is whole as returned is NOT CHECKABLE.
- **E40** :41 — "(§8.3 (2); the addendum's header)". CONFIRMED (addendum :84 (2), :4).
- **E41** :42 — `data/n` holds only `bk`. CONFIRMED (`ls data/n` prints bk).
- **E42** :43 — no n stage that reads a margin has run. NOT CHECKABLE. Consistent: no RESULTS.md entry records an n stage on a model; the 2026-11-15 BACKEND entry (:1419) is p's respawn.
- **E43** :43–44 — the BACKEND extension, G-VEC, G-CAL-n, G-READ-n and the campaign are to come. NOT CHECKABLE (future). Consistent with n:159 and `645bd3f`'s "What waits". See O2.
- **E44** :45 — the site check rendered tokens and loaded no checkpoint's weights. CONFIRMED (STOP block @645bd3f :9, :23–27, :31–33; RESULTS.md:197).
- **E45** :45–46 — "its entry says "No checkpoint's weights were loaded"". FAIL (see fixes).
- **E46** :47–48 — battery runs on synthetic data only, in granted windows. NOT CHECKABLE (relay).
- **E47** :49 — "What runs now (§8.3 (3)–(5))". IMPRECISE (see fixes).
- **E48** :50 — the pod session copies the two small files "to n-build's folder". NOT CHECKABLE (future act; the destination is the relay's). The files and the route are addendum :28 and B:23.
- **E49** :50 — "each checked against the manifest". CONFIRMED (addendum :28; B:23; paste :22).
- **E50** :50–51 — a failed check comes to the PI through the coordinating session. NOT CHECKABLE (process).
- **E51** :51 — nothing downloaded without the PI's word. CONFIRMED. Addendum :28 reads "a download at the pinned revision only if a check fails, on the PI's word"; paste :22 reads "a download only on a failed check — yours".
- **E52** :52 — renders (i)–(iii) in a battery window and commits them as `n — ids of record`. CONFIRMED as specified (addendum :22, :84 "`n — ids of record` (the render's commit)"). See O8.
- **E53** :52–54 — the schema commit settled with n-analyzer; G-VER asserting data; the site check re-run; the BUILD entry. CONFIRMED (addendum :84 (3), :80; B:61–62).
- **E54** :55 — §7's changes before the canonical run. CONFIRMED (addendum :84 (4)).
- **E55** :56 — the chain as n §8 steps 7–15. CONFIRMED (addendum :84 (5); n:159).
- **E56** :56 — LOCK-n v0.1 after this commit. CONFIRMED (paste :27; B:64).

### Text 2: the PI-routing raw

- **P1** :1 — the title's date, 2026-11-16 (second sitting). CONFIRMED (raw :6).
- **P2** :1 — "verbatim". CONFIRMED (see P9).
- **P3** :1 — "(the PI → the coordinating session)". NOT CHECKABLE.
- **P4** :3 — "as the PI gave it in chat on PI date 2026-11-16". NOT CHECKABLE (relay); the date agrees with :6.
- **P5** :3 — "with the PI's word below it". CONFIRMED (:36).
- **P6** :3 — "saved verbatim … on receipt". NOT CHECKABLE.
- **P7** :3 — "committed with `ADDENDUM-n1 v0.1 — COMMITTED`". NOT CHECKABLE (this commit); the name is addendum :84's.
- **P8** :3 — §8.3 (2) asks for the PI's routing quoted verbatim. CONFIRMED (addendum :84). See O5.
- **P9** :3 — the fenced block is byte-identical to the saved copy. CONFIRMED. The fences are at :5 and :37; `cmp` of :6–36 against paste_block.txt exits 0; both hash to sha256 cde49b4e…e644 (cut); 31 lines each, each ending in a newline.

### Text 3: the referent-check raw, §2

- **R1** :213 — "No FAIL." CONFIRMED (§1 :175; recounted as 0).
- **R2** :213 — committed as placed (`e979f8f2…5e03`). CONFIRMED (shasum and cut; equals paste :11).
- **R3** :213–214 — nothing edited, nothing applied. CONFIRMED (sha256 and bytes equal the placed figures).
- **R4** :216 — #77 graded substantive by the checker. CONFIRMED (§1 :137).
- **R5** :216–217 — resolved by the seat's own ruling of the same routing. CONFIRMED on the facts: B:19 is routed at paste :22 in the same block.
- **R6** :217–218 — addendum §1.2 (iii) gives no disposition. CONFIRMED (addendum :22; §1 :139).
- **R7** :218–219 — the quotation. CONFIRMED verbatim (B:19).
- **R8** :219 — that raw is committed at `52b2c97`. CONFIRMED.
- **R9** :219–220 — "The PI's routing adopts its rulings "as ruled" in item 7". IMPRECISE (see fixes).
- **R10** :220–221 — the header names the two answer raws as the place of its reasoning. CONFIRMED (addendum :4).
- **R11** :221–222 — the draft renderer reports and drops such a candidate (its self-test). NOT CHECKABLE (relay).
- **R12** :222 — the seat may regrade, by a ruling. NOT CHECKABLE (process).
- **R13** :224 — #2, #16, #22, #37, #94 are the minor items. CONFIRMED (§1 :37, :54, :62, :81, :156; five "IMPRECISE (minor)" tags by count).
- **R14** :226 — fourteen observations. CONFIRMED (14 counted, §1 :189–209).
- **R15** :227–228 — observation 6: 13–15 decimals; the identity bound across two implementations. CONFIRMED (§1 :197–198).
- **R16** :228–229 — all four at 0 of 40 goes to the seat with the four counts, "as §2 has it". CONFIRMED (§1 :199; addendum :32).
- **R17** :230–231 — the precedence and cap clause are fixed by B §3 and in B §5 item 2's schema commit, and are not in §8.3 (3). CONFIRMED (B:50, B:61; addendum :84; §1 :202).
- **R18** :231 — they reach Code through §8.2 (4). CONFIRMED (§1 :202; addendum :82).
- **R19** :231–232 — "They touch n §6, which §8.1 lists as unchanged." IMPRECISE (see fixes).
- **R20** :233–234 — observation 12: the contrast at every point but valence +1 is the shadow; it tests presence, not sign. CONFIRMED (addendum :56; n:121; §1 :207).
- **R21** :234 — "discriminating the injected sign". CONFIRMED verbatim (CLAUDE.md:292).
- **R22** :235 — "Carried unchanged from n:121." CONFIRMED (n:121: "else the +pole from the shadow").
- **R23** :236–237 — the quotation at "§1.2 (ii)". CONFIRMED verbatim (B:18).
- **R24** :237 — "the words are in `5a97527`'s entry". CONFIRMED in substance (RESULTS.md:1106, from `5a97527`'s diff). See O3.
- **R25** :239 — the reads were "those its brief allowed". NOT CHECKABLE (the brief is not in the repo).
- **R26** :239–241 — the list of reads under data/n/bk. CONFIRMED (§1 :24, :197).
- **R27** :241–242 — nothing under data/mf3, ckpt or reports; no interpreter. CONFIRMED as §1's own statement (:28, :30). See O10.

## TOTALS

92 claims: 72 CONFIRMED, 4 IMPRECISE, 1 FAIL, 15 NOT CHECKABLE.

| Text | Claims | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|---|
| Entry | 56 | 45 | 2 | 1 | 8 |
| PI-routing raw | 9 | 5 | 0 | 0 | 4 |
| Raw §2 | 27 | 22 | 2 | 0 | 3 |

## FAIL AND IMPRECISE, WITH FIXES

**E45 FAIL (entry :45–46).**
- The draft says `645bd3f`'s entry says "No checkpoint's weights were loaded". That entry (RESULTS.md :185–254 at HEAD, with its close lines) does not contain the sentence. Its only mention is :197: "The diagnosis loaded the tokenizer and BK's committed sessions, no weights, and wrote nothing."
- The quoted sentence is in `645bd3f`'s STOP block, :9 ("No checkpoint's weights were loaded: hftiny builds a tiny model from a config on the CPU, …"), and in `645bd3f`'s commit message ("… No checkpoint's weights were loaded. Not pushed.").
- The §1 report's #100 cites it as "645bd3f:9", meaning the block.
- Fix: "its block says "No checkpoint's weights were loaded" (`results/raw/2026-11-16_n-build_code-to-design_STOP.md`:9; its commit message says the same)". Or keep "its entry" and quote the entry: "its entry says the diagnosis loaded the tokenizer and BK's committed sessions, "no weights"".

**E30 (entry :31) and R9 (raw :219–220), IMPRECISE (minor).**
- Item 7 (paste :22) is "n-build, STOP Q1 (b) and Q2: the ids rendered once on the laptop …; … [as ruled; a download only on a failed check — yours]".
- It routes that raw's STOP rulings, its §1, where §1.2 (iii) sits. The schema rulings are item 8.
- "[adopt]" is the bracket of items 5, 6 and 10, not of item 7.
- Fix (entry): "The PI's item 7 routes that raw's rulings on the STOP (Q1 (b) and Q2: its §1, where §1.2 (iii) sits) "as ruled"".
- Fix (raw §2): "The PI's routing takes that raw's STOP rulings (its §1) "as ruled" in item 7".

**E47 (entry :49), IMPRECISE (minor).**
- The first bullet under "What runs now" (the pod session's copy of the two small files, the check, a download only on the PI's word) is addendum §1.5 (:28). It is not in §8.3 (3)–(5) (:84), whose (3) begins "n-build: the ids (§1.2 (i)–(iii)) in their window and their commit".
- Fix: "(§1.5; §8.3 (3)–(5))".

**R19 (raw :231–232), IMPRECISE (minor).**
- "They", meaning the pause precedence and the cap clause, "touch n §6". But n §6 (n:148) names the pause triggers and "Every pause STOPs the arm's launches"; it says nothing of a cap.
- §1's observation 7 (:200–202) names two things as touching §6: B:50's accepted reading that "a fired monitor ends the invocation for every arm", and the pause precedence. It does not name the cap clause.
- Fix: "The pause precedence, and B:50's accepted reading that a fired monitor ends the invocation for every arm (n:148: "the arm's launches"), touch n §6, which §8.1 lists as unchanged."

## OBSERVATIONS (no verdict)

1. **Rendering of the verbatim items (entry :18–22).** "> 5.", "> 6." and "> 10.", separated by ">" lines, form one ordered list in CommonMark/GFM. Such a list numbers from its first item, so in a rendered view item 10 shows as "7.", which is a different item of the block. Escape the numbers ("> 10\. …", and likewise 5 and 6), or close the quote before item 10. The block's one leading space per item (" 5.") is also dropped, which does not matter.

2. **The stage list (entry :43–44)** follows "No n stage that reads a margin has run". It mixes stages that read margins (the BACKEND extension's 24 reads, the campaign) with stages that do not (G-VEC's captures, G-CAL-n's turns, G-READ-n computed from captures). It omits G-TIME-n (n:118, "Six reads of each kind … timed on the box") and G-VER (n:119), both under `645bd3f`'s "What waits". A reader could take it as the complete list.

3. **Wording of observation 13 (E38, R24).** The seat's raw attributes an act to `14e65d8`'s entry ("left it to the lock"); it quotes no words. The words that left the N4 join to the lock are `5a97527`'s: "the exact join is the lock's" (RESULTS.md:1106 at HEAD; :1037 at `bedc198`). The raw's "the words are in `5a97527`'s entry" can read as placing the quoted words there. Naming the words removes that.

4. **Anchor drift in §1 of the referent-check raw.**
   - §1's RESULTS.md anchors index `bedc198`'s RESULTS.md: the checker ran before `52b2c97`, and its #73 calls the seat raws "untracked".
   - At `52b2c97` the anchors have moved: :8351 is now :8420, :1037 is :1106, :290 is :313. This entry moves them again.
   - §2 does not say which file state they index. One line pinning them to `bedc198` would keep them usable.
   - B:N anchors are unaffected: the committed blob equals the placed file.

5. **Grammar in the PI-routing raw :3.** In "committed with `ADDENDUM-n1 v0.1 — COMMITTED`, whose §8.3 (2) …", "whose" attaches to the entry's name, but §8.3 (2) is the addendum's. Suggested: "…, as the addendum's §8.3 (2) asks for the PI's routing quoted verbatim."

6. **Checkability of the byte-identity claim (PI-routing raw).** It is asserted against a saved copy that will not be committed. The block's own digest in the header would let a later reader check it: sha256 cde49b4e…e644 over the 31 lines between the fences. The header also does not say whether the "PI: " label on the last line is the PI's text or the session's label; "with the PI's word below it" holds either way.

7. **Expected close lines (entry).** The addendum's header (:4) says "the n-build and n-analyzer sessions add their close lines". The entry does not say they will be added here, as `52b2c97`'s close does ("The n-build session adds its close lines here …").

8. **Two records named for the render's commit.** B:60 says the ids are committed "with a dated note on `645bd3f`'s entry citing this raw". The addendum (:84) adds the entry `n — ids of record`. The entry follows the addendum. Both can hold; the relay to n-build may want to name both.

9. **Support for Code's grading of #77.** §8.4 (:86) lists "The seat's raws of this date, by path" among the referents, so B:19's disposition lies inside the referent set the addendum names.

10. **awk and "ran no interpreter".** §1's tools include awk (:26; observation 6 says "counted by awk", over data/n/bk/reduced.json). If the project's "no interpreter" line counts awk as an interpreter, §2's "ran no interpreter" (:242) needs a qualifier. If awk counts as a shell tool here, nothing changes.

## 2. Code's dispositions

Every FAIL and IMPRECISE item is applied in the checker's terms, and so are all ten observations.

- **E45 (FAIL):** applied. The entry now says the block says "No checkpoint's weights were loaded"
  (`results/raw/2026-11-16_n-build_code-to-design_STOP.md`:9), and that the commit message says the same.
- **E30 and R9:** applied. The entry and §2 say that item 7 routes the raw's rulings on the STOP (its §1, where
  §1.2 (iii) sits) "as ruled".
- **E47:** applied. "(§1.5; §8.3 (3)–(5))".
- **R19:** applied. §2 now names the pause precedence and the accepted reading that a fired monitor ends the invocation
  for every arm (n:148, "the arm's launches") as touching n §6, and no longer the cap clause.
- **O1:** applied. The three items are three blockquotes, each under its own number.
- **O2:** applied. The entry lists the stages still to run (G-TIME-n, G-VER of record, the BACKEND extension, G-VEC,
  G-CAL-n, G-READ-n and the campaign) and names the site check's G-VER trial as never of record.
- **O3:** applied, in the entry and in §2: the words that left the N4 join to the lock, "the exact join is the lock's",
  are `5a97527`'s entry's.
- **O4:** applied. §2 pins §1's RESULTS.md anchors to `bedc198`'s RESULTS.md.
- **O5:** applied. "as the addendum's §8.3 (2) asks for the PI's routing quoted verbatim".
- **O6:** applied. The header gives the block's sha256, `cde49b4ee8d8cc8f8769ee43a94d39eacd5fdf5971945d9911a55ea31703e644`, over
  the 31 lines between the fences, and says that the last line, "PI: Route as given", is the PI's own line after the
  block.
- **O7:** applied. The entry ends with the two sessions' close lines to come.
- **O8:** applied. The entry names both records of the render's commit: `n — ids of record`, and a dated note on
  `645bd3f`'s entry (the n-build raw's §5 item 1).
- **O9:** applied in §2's grading of #77.
- **O10:** applied. §2 says the referent checker ran no interpreter beyond awk and sed as text tools, which its brief
  allowed.
- **The checker's disclosures** are recorded here for the seat (list v2 item 8), as it gave them. The full-message
  `git log` over `645bd3f` printed a one-line message, its subject. None touched `data/` beyond a name-only `ls data/n`.

The edits after the check were checked by tool: a `diff` of each text against its copy as checked shows these changes
and nothing else; the PI-routing raw's fenced block was re-hashed to the sha256 its header gives, 31 lines; and the
quotations newly added were counted in their sources. There was no second blind pass.
