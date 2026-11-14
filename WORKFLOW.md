# WORKFLOW.md — the three seats, the two channels, and who commits (v1.0)

*jspace-lab, PI date 2026-11-14. Written by the design seat on the PI's request ("help me make sure our workflow is crystal clear … formalize that more and document so it's stable forever"), placed untracked at root, committed by path by Code on the PI's routing (entry `WORKFLOW.md v1.0 — COMMITTED`). It writes down what CLAUDE.md's "Two-instance workflow — unchanged" and "How to append results — unchanged" state in two paragraphs, and what three months of entries practise. It changes no rule of any pre-registration; where a pre-registration or the list of record speaks, it governs. CLAUDE.md is not edited for this document: the stages' GATE and LICENCE lines print its sha16; its one-line pointer here waits for CLAUDE.md's next version. Calendar dates only; the commit hash is the record.*

## §1 The seats

**The PI** (Jason). Decides and routes. Speaks in chat, to each seat separately; his words are the record wherever a seat quotes them, verbatim, in an entry or a raw ("Route as given"; an edit by item number; a cap; a go; a stop; "Yes, record it"). **The PI never commits and never edits a file of the repository**: every change to the tree is a commit by path with its entry, so that the pre-registration provenance is always Code's commit and never anyone's to unwind. The PI runs no model and reads no pick-bearing artifact before a unit's VERDICTS (PROPOSAL-m m:318).

**The design seat** (Claude, in the Sentieum lab project; one thread at a time, handed on by `claude/HANDOFF-<PI date>-<topic>.md`). Theory, pre-registrations, adjudication, synthesis. It reads the repository directly — the laptop checkout over the device bridge, never a relay — and writes proposals and addenda (`PROPOSAL-<letter>-…-v0_N.md`, `ADDENDUM-<unit>-…-v0_N.md` at root), the contents of locks, answer raws (`results/raw/<PI date>_<topic>_design-to-code_answers.md`), and the handoffs. **It drops every file untracked on the laptop at the path where it will be committed, and never commits**; it never edits a committed file (a correction is a dated note or the next raw; a changed document is a new version). It runs no model. It reads under the blinding rules of the pre-registration in force (m:271, m:318) and the list of record (§7).

**Code** (Claude Code: one coordinating or master session that the PI routes everything through, and the per-track sessions it hands work to — the F3 session, the pod session, an addendum's session). Builds, runs, values-checks, writes RESULTS.md entries and its blocks to the seat, and **commits by path at its step** — the seat's files among them, each re-hashed against the sha256 the seat named just before the commit — with close lines on the entries the seat's answers close. Code adjudicates nothing: a fired gate, a pause, a departure, a question goes to the seat through the PI (CLAUDE.md: "Code escalates fired gates, never self-adjudicates"). Code may run on the laptop or on the box; both are Code; the repo state, not the site, is the ground truth.

## §2 The two channels

**Design → PI → Code: one paste block.** At the end of each sitting the seat gives the PI, in chat, **one merged paste block written for the master Code session**, which hands its sections down. The block carries: the PI date; the files the seat placed, each by path, sha256 and bytes; sections by track (A the Q-F3 / m track, B the p track, C the coordinating session and record hygiene, D the push state), each a numbered list of rulings and the actions they route, **the seat's default for every open choice in square brackets**; and the line for the PI's word. The PI pastes it into the master session with his word — "Route as given", or his edits by item number, or his answers to the bracketed items — and that word, quoted by Code in the entry, is the record. The raw of record is the answer file under `results/raw/`; the paste block routes it and duplicates only what Code needs to act. Nothing is routed in chat that is not in a placed file, except the PI's own decisions.

**Code → design: repo state only.** Code's output to the seat is what it commits: RESULTS.md entries (the Log, newest first), its blocks to the seat (`results/raw/<Code date>_<topic>_code-to-design<_suffix>.md`, with numbered questions and the items it declares without adjudicating), the values-check raws, the gates' artifacts and reads files under `data/`, the scrubbed stdout raws, the commits with their messages. **Code's chat text to the PI is not the seat's input**, and the PI's message to the seat ("Code has updates in the repo", "six files for your review") is a nudge, not a relay: the seat reads the repository — the reflog, RESULTS.md's newest entries, every block without an answer after it, the artifacts the block cites — and rules on what it read. The fact hierarchy is repo > handoff > memory; where a relay and the repo disagree, the repo is right and the raw says so.

**The seat's turn, in order.** Pickup (the repo delta since the last handoff or raw) → every open block read in full, with the entries and artifacts it cites, under §7's rules → the answer raw written, every quoted figure recomputed from the artifact and every anchor opened in the pinned file at root → the files placed untracked at their final paths → sha256 and bytes verified (with a device shell: `sha256sum` on the laptop; over the file bridge alone: the sha256 of the bytes written and `get_file_info`'s size, Code's re-hash before the commit being the check of record) → the paste block → the PI's word → Code's commits by path, close lines, and the next step. Code does not act on a seat text before the PI's word; the seat does not act on a Code text that is not committed.

## §3 The seat's raw: fixed form

- **Path:** `results/raw/<PI date>_<topic>_design-to-code_answers.md`; one raw may answer several blocks (its sections say which).
- **Header**, one italic paragraph: what it answers (Code's blocks and entries by path and commit); what was read and under which rule (the reads files by sha256, redacted or stripped as m:271 leaves them; the artifacts by sha256; the anchors by `m:N`, `p §N`, file and line — read from the pinned file at root, never from memory); what was not opened (checkpoints, call logs, picks, contrast seconds); the abbreviations for earlier raws; then the fixed placement sentence, verbatim:

  > *Placed untracked over the bridge; Code commits by path on the PI's routing; <the sessions named> add their close lines. Calendar dates only; the commit hash is the record.*

- **Body:** §0 the short form; numbered sections by block and question, each ruling with its anchor; departures named with their class and the ledger line they earn; nothing of a `ckpt` or call log, no contrast session's seconds, picks or free-round events, no stage total or wall-clock figure of a stage with contrast sessions before its VERDICTS (the G-TIME-F0 Q4 ruling; ledger (65)).
- **Last section:** the routing block for the PI, the source of the paste block (§2's form).
- **Copies:** the project (`claude/` through `project_write`) and the chat (`SendUserFile`); the laptop copy under `results/raw/` is the one Code commits.

## §4 Code's block to the seat: form

- **Path:** `results/raw/<Code date>_<topic>_code-to-design<_suffix>.md`, committed with its entry; the entry says "STOP for the seat's read" when the order stops there, and "Next" otherwise.
- **Header:** the session, the PI date, "For the PI to route."; what ran, under which lock and driver (hashes); the sources read and the ones not opened, by sha256.
- **Body:** the short form; the reads the seat needs in m:271's form; the items Code declares without adjudicating (PINs, readings, departures with their class); the questions, numbered Q1, Q2 …, each with the readings to weigh; "Not questions" for what the seat need not rule on. **"Code adjudicates nothing"**: a PASS is the stage's computed verdict; a FAIL, a fire or a pause is reported, never decided.
- **After the seat's answer and the PI's word:** the session named adds a close line on its entry — the seat's raw cited by path and sha256, the seat's words quoted — committed by path with a values-check, as the record practises.

## §5 Documents of record, versions, notes

- **Proposals and addenda** live at root, one version at root at a time; superseded versions move to `archive/` by `git mv` at the commit of the new one. Anchors are lines of the pinned file (`m:N` = PROPOSAL-m v1.11's line N); a quote is from the pinned file at root, never from a draft or a memory (ledger (64)).
- **A STOPPED document** gets a new version with a "what changed" list; nothing is edited in place.
- **Locks** (`LOCK-<unit>.md`) are re-issued above the prior version's text kept verbatim; **a lock file is never edited after its commit** — its sha256 is the stage's `lock_sha256` and the entry names it. What happens to a locked unit afterwards (a box change, a departure, a dated observation) is recorded by a **dated note: a RESULTS.md entry**, never an edit of the lock or of any committed file.
- **The seat never edits a committed raw**; a correction is the next raw or a dated note. **Git history is never rewritten**; a wrong commit is followed by a correcting one.
- **Counters** are declared before runs and frozen in form at their first report (rule 23); post hoc observations license pre-registrations, never verdicts (rule 11).

## §6 Handoffs

The design seat's handoffs live in the Sentieum lab project (`claude/HANDOFF-<PI date>-<topic>.md`), not in the repository (release rule D4; the root `HANDOFF-2026-08-22` … `-10-04-design.md` files are the earlier practice, frozen). A handoff is a map; the raws are the territory. A fresh thread picks up from the newest handoff and then from the repo's delta; a closing thread writes one. Every handoff lists each open unit with its Clock date and lock status (ledger (47)).

## §7 Rules by reference

The blinding rule (m:318) and the pre-VERDICTS read rule (m:271); the list of record v2 (`results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md`, items 1–9: what no session lists, opens or hashes before a unit's VERDICTS or NOT-RUN record); the laptop rule (one model run at a time, announced to the coordinating session and serialized; no whole-tree listing while a stage runs); no stamp computed against another before VERDICTS (the G-TIME-F0 Q4 ruling); the respawn protocol (CLAUDE.md); rule 27 (the repo, not any machine, is the record). This document restates none of them.

## §8 Chat

The PI's relays are short; the seat asks nothing it can read in the repo; every seat quotes the PI verbatim and marks its own gloss as such. Calendar dates only in the seats' documents; Code keeps its own stamps where the record allows them; the commit hash is the timestamp of record.

## §9 How this document changes

A new version by the design seat (`WORKFLOW.md` v1.N, "what changed" at its head), placed untracked, committed by path by Code on the PI's routing with its own entry; the superseded version to `archive/`. A drift found in practice is a ledger line and a version, never an edit of a committed file. **v1.0** records one: ledger (68) — the seat's raws of 2026-11-09 → 2026-11-12 and the handoff of 2026-11-12 said "the PI commits by path"; Code commits by path on the PI's routing, and always has.
