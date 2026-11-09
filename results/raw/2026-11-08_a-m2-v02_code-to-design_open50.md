# ADDENDUM-m2 v0.2 — OPEN #50: §3.4's counters at gate-stage entries have no blinding scope (Code → design seat, through the PI)

*Code's raw, PI date 2026-11-08. From the blind referent check of v0.2 (`ADDENDUM-m2-f3-reasoning-block-v0_2.md`, untracked at root, sha256 `69e23212…cb47`; its raw, `results/raw/2026-11-08_a-m2-v02_referent-check.md`, committed beside, item 50). `ans2` = the seat's answers to the pre-read (`de729c4`, `09d856ef…ea29`). v0.2 is not committed. Whether v0.2 §6 item 1's STOP ("any unresolved substantive item → STOP") fires on #50 is with the PI, through the coordinating session; this block puts #50 itself to the seat. Nothing ran on a model.*

## 1. The text

v0.2 §3.4 (line 48):

> **3.4 Counters, declared (rule 23; descriptive, deciding nothing), for the smoke and for every Q-F3 stage from the re-run on:** (a) reasoning lines that contain any complete harness-written line of the session or keep the banner's `=== … ===` frame (Q8's containment, as a counter); (b) task responses, over all rounds and reported with their phase, that no audit class claims and that attempt no task — a preamble or announcement, a description of the session or its configs, a header, reasoning about the choice (A3s round 8's kind); any answer attempt, correct, wrong, partial or to another item, is not (b) — a declared read: Code lists every (b) response by session and round, the seat confirms or corrects each; both counters tabulated over all sessions, excluded ones included, reported at each stage's entry and at VERDICTS.

(v0.2:48 continues with the counters' VERDICTS path in Code's own step, ans2 §4; that sentence is omitted here.)

ans2 §1 has (b) "counted over all rounds and reported with the phase; Code lists each by session and round, the seat confirms or corrects each".

## 2. The conflict, before VERDICTS

From the re-run on, every Q-F3 gate stage but G-ID-F3 runs contrast sessions (A1, A2, A3), and so does the campaign. These rules withhold their free-phase content before VERDICTS (m:271's window: "to the unit's VERDICTS entry or NOT-RUN record"):

- **m:271:** "At every gate stage the contrast sessions' forced-round counts are reported beside; their free-round events — exclusions, degeneracy, any class — are withheld to the unit's VERDICTS entry or NOT-RUN record" (bold in m:271), for the reason it gives: "a free round's class sits on the pick". Its read rule reads a contrast transcript "with its free rounds removed entirely" (bold in m:271).
- **m:263:** "for a contrast-template session's free-round exclusion the phase alone (`excluded@free`), the class withheld to VERDICTS" (bold in m:263).
- **F-6**, G-TIME-F3's ruling (the seat's G-ANL-F3 answers, line 29): "for a contrast session at G-TIME-F3, no per-line list is printed or reported before VERDICTS … the per-line booleans and the realised totals go to the checkpoint under m:271".
- **F60**, G-F3's form (LOCK-m-F3, the PIN register): "a contrast template reports its sessions' first reasoning lines (pre-pick) beside its forced rounds, by class, with line-1 exclusions and hair triggers; later lines withheld with the free rounds".
- **m:318**, at the campaign's looks: "at looks, pooled pre-pick exclusion counts per arm".

§3.4, read as written, asks for both counters "over all sessions … at each stage's entry". For a contrast session that would print two things these rules withhold:
- (b)'s listing "by session and round" over its free rounds. That is a free-round class, sitting on the pick.
- (a) tabulated over its reasoning lines. F-6 bars any per-line list for a contrast session at G-TIME-F3, and at G-F3 only the first, pre-pick line is reported, by class (F60). Code's reading is that a count over the later lines is free-phase information too.

The seat could not confirm or correct a contrast (b) item without reading the free round that m:271 removes.

## 3. What it binds, and what it does not

- **It binds** every Q-F3 stage entry from the G-TIME-F3 re-run on that carries contrast sessions: the re-run itself, G-F3, and the campaign's looks, where m:318 governs what is reported. G-ID-F3 runs A2s and A3s only, sham sessions read in full under m:271, so nothing is withheld there.
- **It does not bind** the v0.2 commit, which is a text. Nor does it bind the smoke: its twelve sessions are sham-only, belong to no unit, and are declared readable in full (v0.2 §3.2).
- **At VERDICTS** the window closes (m:271), and §3.4's counters over all sessions are lawful there, computed in Code's own step (ans2 §4, F-A (ii)).

## 4. Code's proposed fix (the seat rules)

Before the unit's VERDICTS entry or NOT-RUN record:
- **At a gate stage:**
  - (a) is tabulated and reported over the sham sessions' reasoning lines. It also covers each contrast session's first reasoning line wherever the stage reports that line's class (G-F3, F60).
  - (b) is listed and confirmed over the sham sessions' rounds, all phases, and over the contrast sessions' forced rounds, which m:271 reads and reports beside.
- **At the campaign's looks,** neither counter is reported for any arm. A look reports what m:318 has it report.
- **The rest is computed at the unit's VERDICTS entry or NOT-RUN record** (m:271), by Code's own step: each contrast session's later reasoning lines and free-round (b), and the campaign's counters. (b) is listed by session and round there, and the seat confirms or corrects each.

As one sentence for v0.2 §3.4: "before the unit's VERDICTS entry or NOT-RUN record, a gate stage's entry reports (a) over its sham sessions' reasoning lines and over its contrast sessions' first lines where it reports their class, and (b) over its sham sessions' rounds and its contrast sessions' forced rounds; the campaign's looks report neither; the rest is computed and reported at the unit's VERDICTS entry or NOT-RUN record (m:271, m:263, m:318, F-6, F60)."

## 5. Code's readings carried (the referent check's items 48 and 49)

- **#48.** P4 checks "A-m2 committed, with sha256 `cdcc8e86…53f0`" (the pre-read, line 164), which is v0.1's. ans2 accepts P4 with "A-m2's sha". v0.1 is never committed (v0.2 header, §6 item 2), so Code reads P4's pin as the committed A-m2's sha, v0.2's `69e23212…cb47`. The smoke driver pins it.
- **#49.** §3.3 has no clause for a smoke that stops under P4: a G-VER failure, a task-round `scaffold_absorption`, the backend, the snapshot. Code reads it as: a stopped smoke selects nothing; Code reports the stop and the seat rules, as at any STOP. The driver prints no tally and no rule after a STOP.

## 6. For the PI's routing

1. v0.2 §6 item 1: whether #50 fires the STOP. Code's lean is (a), commit with #50 as a FLAG, since the commit and the smoke do not read it.
2. #50's fix: §4's sentence, or another.
3. #48 and #49: Code's readings [confirmed / struck].
