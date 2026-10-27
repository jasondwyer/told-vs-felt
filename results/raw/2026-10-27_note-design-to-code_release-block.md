# Design → Code — the release block, posting day (note arc; 2026-10-27, routed by the PI)

*Design seat. Committed by path on `main` at the PI's direction; supersedes the untracked `results/raw/2026-10-26_note-design-to-code_pre-flip-scrub-rename.md` on the laptop where they differ. Calendar dates only; times ET where a clock matters. This block changes no pre-registration, label or figure. It carries the PI's decisions of 2026-10-26/27: repository renamed `told-vs-felt`; five non-main branches deleted; nine process documents removed from the tree (history untouched); `PREPRINT-v1_0-draft.md` kept with a status banner; author emails unchanged; the 2026-10-22 figure set posts as filed (no restyle); GitHub Issues stay on.*

## 0. Done before this block (the seat, at the PI's direction; verify, do not redo)

| Commit | What |
|---|---|
| `f5a580d` | `git rm` of the eight `HANDOFF-2026-08-20 … 09-12.md` and `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md`; new `README.md` (pointer to README-NOTE and the tag; former name noted; handoff row of the orientation table replaced; regression count stated as **154/154** — confirm at the release commit, §3 item 3). |
| `32aefcc` | `PREPRINT-v1_0-draft.md` status banner. Patch v8 text unchanged beneath it: pre-banner sha256 `45b67246…7a41`, post-banner `5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467`. N18 reads the new sha256. |
| `0a3f925` | The three 2026-10-22 SVGs at the root beside the 2026-10-10 set. Filed-copy sha256 equal to `2026-10-22_figure-checksums.md`: F1a `f0c1cd73…5bfc`, F1b `640c13e8…33af`, F2 `0e0459cf…69bc`. |
| (refs) | The five non-main branches deleted on origin: `wip/cloud-handoff-2026-10-15`, `wip/cloud-handoff-2026-10-18`, `wip/step16-review-scratch`, `main-882qqu`, `claude/handoff-doc-next-steps-oeccd1`. `git ls-remote origin` should show `main` and the tags only. |
| (GitHub) | Repository renamed `jasondwyer/told-vs-felt` (the old URL redirects). Issues on. |

Still to come from the PI, by path: `RESEARCH-NOTE-v0_8-draft.md` at the root (the frozen note, after the seat's freeze read). It is the last commit before the tag.

## 1. Clone and names

1. `git remote set-url origin https://github.com/jasondwyer/told-vs-felt.git` in every Code clone; `git fetch origin main`; HEAD must be at or after `0a3f925`.
2. `scripts/audit_note_N12_preflip.py` line 72: `OWNER, NAME = "jasondwyer", "jspace-lab"` → `"jasondwyer", "told-vs-felt"`, in the preflip script's own commit (scrub index §10 item 1 provides for it).
3. `scripts/audit_note_N11.py`: if the fresh clone takes a URL, pass the new one; if it reads `origin`, item 1 covers it.
4. `README-NOTE.md`: every mention of the repository name or URL re-pointed in the re-point commit. The three raws that print the old URL (`results/raw/2026-10-04_m-v1.7_referent_check.txt`, `results/raw/2026-10-08_note-N12-preflip.md`, `.json`) stay as committed.
5. The laptop checkout path, the `jspace-lab` MCP server name and every path string in the log stay. The note's repository link is the tag URL: `https://github.com/jasondwyer/told-vs-felt/tree/note-2026-10-v2`.

## 2. The audit block (AUDIT-note-release; the 10-23 and 10-26 handoffs' list, compressed)

In order, each its own commit with its raw:

1. **N12 re-runs at the release commit:** history, content and licenses scripts; gitleaks over `--all`; the password search (the PI supplies the word at scan time; it is never written into any committed or public document). The D4 census: `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md` was committed by path at `5dca58b` (2026-10-14), after the 2026-10-12 release scans, excluded by name from the content runs, and is in the history, so the history and gitleaks re-runs cover it — state that in the scrub index.
2. **N1 round 11** on `RESEARCH-NOTE-v0_8-draft.md` + the three 2026-10-22 SVGs (filed-copy hash; the C2PA element excluded by N1 as in rounds 9–10; N18 hashes whole). Ledger additions since round 10, by source:
   - the 10-23 handoff's list (every A0 figure; the restored figures; N2(vii)'s; Rodd-Henricks 2002 and Nosek 2018; F2's caption clause);
   - the seat's change-log passes 3–11 (Link 4 and ‡): the source-convention rates 17/96 = 0.177, 25/96 = 0.260, 0/96; the fifth premise 10,000/200 (DPO *p* ≈ .003, *d*′ ≈ 0.9; instruct *p* ≈ .17); v5 Table 3 (+9.8 ± 0.5, −11.5 ± 2.4, +0.6 ± 2.8, −21.8 ± 3.2; *L* = 25, α = 4); the abliteration *d*′/*c* (10.8% → 63.8%, 0.0% → 7.3%; *d*′ ≈ 1.8, *c* ≈ 0.55; pre-ablation 1.85–2.48, *c* ≈ 2.2–2.5); layer 44 (0-based, int(64 × 0.7)) and the source's "45"; strength 1.0 = 0.35–0.57 of residual norm; 12/40 vs 7/44 (+0.14, *p* = .10); 12/48 vs 9/48 (+0.06, *p* = .31); 4/48 and 2/48; *p* = .28 (0/43 against 2.9%); 500 concepts;
   - pass 12 (§8 ¶1 and ‖‖(a)), source "author correspondence 2026-10-26", pending verification against `v2_controls/steering_state_controls/b1_b3/tables/` (T+3): `TEMP_RELIEF_TURNS = 1`; 1,041 and 554 of 1,595; 1,595 of 1,595; 237 per arm; 31.2% vs 80.2%, 11.3% vs 26.3%, gaps 48.9 and 15.0; 72B gaps 18.2 and 21.6; harm-only 75.2%/12.9%/0% at 32B and 51.1%/11.0%/0% at 72B; ten norm-matched random directions; 1,684 pairs;
   - pass 13b (§6, §8 ¶2), source the v2 PDF in the project: 0.397 (§7.4.3, Figure 27); 0.8 and 0.2 (§7.4); Beta(8, 2)/Beta(2, 8) (N19 raw, released defaults); seven Level 2 indicators (Table 2); the §1.1 note 2 quotation; the Shevlin credit;
   - pass 14 (TL;DR): the told control as Δ = +0.49 and sham bounds 0.06 — rounded forms of +0.4875 and 0.0625, same figures;
   - pass 15 (Link 5, Q3 bullet in plain words): the screen trigger, confirm tier and instruct falsifier paraphrase PROPOSAL-g §4; the SFT stop rule and the fixed run order paraphrase v0.6's "SFT overdose tripwire" and "outcome-blind scheduling" — read those two sentences once against LOCK-g;
   - passes 18–19 (number format, Unicode throughout): no figure changed; every statistic now reads Δ = …, *d*′ ≈ …, *p* = …; the §5 *p* reads 81/2⁸⁰ ≈ 7 × 10⁻²³.
   - ‖‖(c) (the struck-indicator what-if and its withdrawal) was removed from the note at the PI's direction; it stays in the record (v0.6 at `note-2026-10-v1`; the v0.6 ledger). The former (d) is now (c).
3. **README.md regression count:** confirm `python -m valence_core.regression.analysis` prints 154/154 at the release commit (N11's raw at `6485da2` shows 154/154; the note's §9 states it). If the count differs, correct README.md in the re-point commit and tell the PI the note's §9 figure.
4. **N18** release manifest after the v0.8 commit, with `--preprint-pi-confirmed 5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467`.
5. **README-NOTE re-point:** v0.6 → v0.8 and round 11's ledger; the repository name and the tag URL; the workflow line (line 193 at `8d68b0b`) reworded — the PI's text:

   > **The workflow**: the multi-seat workflow (a design seat, Code and the PI handing work over in writing) ran on written handoffs between sessions. The Code seat's eight handoffs (2026-08-20 to 2026-09-12) were removed from the tree at the release and remain in the history at the commits the record cites; the design seat's handoffs were never tracked (D4). A separate write-up on the workflow is held.

   Code supplies the `src` comment. Also: nothing in `scripts/` or `valence_core/` opens the nine removed paths from the working tree (the seat's read: N4 reads only the never-tracked design-seat handoffs behind presence checks; N13 looks for `HANDOFF-2026-08-18*`, presence-checked; nothing reads `DESIGN-to-CODE-*.md`) — confirm by grep; N11 at the tag resolves every link in the new README.md (checked by the seat on the tree at `f5a580d`).
6. **Preflip script commit** (item 1.2) → **the pre-flip read**: `git ls-remote origin` = `main` + tags only (`cycle-2-close`, `cycle-4-close`, `note-2026-10-v1`, `note-2026-10-v2`); the GitHub-side surfaces (PRs, issues, Actions, wiki, Pages, deploy keys, webhooks, force-pushes). Any remaining `wip/*`, `main-*` or `claude/*` head: STOP and report.
7. **Tag `note-2026-10-v2`** on the final audit commit; **POST-note** refreshed (the v0.8 sha256 and the tag commit; the pinned-comment text the PI supplies; the tag URL).

## 3. Fallback and after

- The release decision of the 10-23 handoff stands: the post does not wait for the repository. If this block is not done by the PI's deadline, the note posts with the fallback paragraph ("will be released within N days") and the flip follows when the block completes.
- **T+3:** the v2 Tagliabue table check (then the "we have not yet checked" clause in ‖‖(a) goes by prompt correction; the pass-12 ledger rows re-sourced to the tables); any reply-driven corrections (HEAT-PLAN §7 class A); the N12 hashsalt fix on the next figure render.
