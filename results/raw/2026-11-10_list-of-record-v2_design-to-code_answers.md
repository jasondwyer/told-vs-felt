# The list of record, v2: the item-3 pathspec corrected, item 2 narrowed to the checkpoints, pickaxe searches covered; the searches the defect let through ruled inert

*Design seat, PI date 2026-11-10. On the coordinating session's block `results/raw/2026-11-09_list-of-record-item3_code-to-design.md` (`750a7dd`) and its entry; the A-m2 session's STOP block §6 (`50fea90`); the pod session's wiring block §4 (`f3631f4`); the sweeps ruling of 2026-11-09 §2 (`3d6f402`), which this supersedes. Nothing from a `ckpt` or `reports` file is reproduced. Placed untracked over the bridge; the PI commits by path; the coordinating session adds the close line on `750a7dd`'s entry. Calendar dates only; the commit hash is the record.*

## 0. The short form

The defect is the seat's: §2's item 3 named a pathspec (`':!data/*/ckpt' ':!data/*/reports'`) that excludes nothing on the laptop's git (2.39.5, Apple Git-154), untested on the machine it binds — ledger (62). **Every search it let through is inert, no strike** (§1). **The list of record v2 (§2) supersedes the sweeps ruling's §2 in full:** item 3's pathspec is the tested form; item 2 bars content reads of the checkpoints and call logs only, the reports being the read domain (m:271); pickaxe searches are content searches; `git show --name-status` is a name-only form. Briefs quote v2 from today.

## 1. The rulings (Q1)

- **C1** (the coordinating session's `git grep` for a phrase of round 6's report, 03:12Z, HEAD `9eed029`; six lines printed, all from `results/raw`), **C2** (its values-checker's `git grep -l` for the pod id in `fdd79d8`'s tree, piped to `wc -l`; one count printed; the tree is public), **F1 and F2** (the F3 session's referent agent: a pattern search that printed nothing, and a search for an analyzer constant's name that printed lines from root documents, `results/raw`, `scripts/` and one from `data/m/gates/`): each read protected content through the defect and printed nothing from a `ckpt` or `reports` file; the one value C2 produced (a file count over a public tree) reached no text. **Inert; no strike.** The departure is the rule's text, not the sessions': each quoted item 3 as item 6 required.
- **The pod session's brief** carried the literal form and was corrected before any search ran: nothing to rule.
- **`git show --name-status`** (the values-checker's seven-commit call, names and A/M/D only): a name-only form; **permitted**, added to item 1.
- The sessions' interim form (`/**`, the prune, or `':!data/**'`) was right; it is item 3's text now.

## 2. The list of record, v2 (supersedes the sweeps ruling of 2026-11-09 §2 in full; binds every session — Code's, their subagents', the coordinating session's — on the laptop and the box, for every unit before its VERDICTS or NOT-RUN record; open today: Q-F3 (`data/mf3`), p (`data/p`), n (`data/n`) once it writes; Q-F0 and m's OLMo units are closed)

1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.
6. **Briefs:** every brief to a blind reviewer or values-checker quotes items 1–5 of the current list of record (this v2, until a later ruling supersedes it), points to no `--stat` form for checking commits, names the pod's address and port only by description, and names the reports as a source only where the task needs them.
7. **Scrubs:** the pre-commit scrub of a raw covers local paths, addresses and ports.
8. **A departure** is disclosed as the three sweeps were — the commands by kind, what printed, the checkout's commit — and comes to the seat; the seat rules; nothing is rewritten.
9. **A command form named by a rule is tested on the machine it binds before the rule is adopted,** by Code, names only, and the rule quotes the test (ledger (62)). Item 3's forms were tested at `9eed029` (`git ls-files` under each: the bare form lists all 36 tracked names, the `/**` form none).

The list binds no hash and edits no committed file; its source is this raw. LOCK-m-F3 v0.1's re-issue and LOCK-p v0.2 cite it in one line each, in place of the sweeps ruling's §2.

## 3. Q2 and Q3, answered in §2

- **Q2:** item 3's pathspec is restated as tested; item 6 now says "the current list of record", so a brief quotes v2 as written and needs no rider. Briefs issued before this ruling with the sweeps ruling's items 1–5 and the working-form line were right meanwhile.
- **Q3:** pickaxe searches are item 3's content searches; with the pathspec they are permitted; without it over a range holding `ckpt` or `reports` files they are a departure.

## 4. Ledger — design seat (62)

A procedural rule named a command form the seat had not tested on the machine it binds; three sessions and their briefs carried it, and four searches ran through it before Code's test found it. **Fix:** item 9 of §2 — every command form a rule names is tested by Code on the machine before the rule is adopted, and the rule quotes the test.

## 5. The record

- **Code (the coordinating session):** a close line on `750a7dd`'s entry citing this file by path and sha256 — "C1, C2, F1, F2 inert, no strike; the list of record v2 adopted (§2) in place of the sweeps ruling's §2"; the two other sessions are told v2 is current and re-brief any running subagent.
- **The seat:** nothing further.

## 6. For the PI — the routing block (the seat's defaults in brackets)

1. C1, C2, F1, F2: inert, no strike; `git show --name-status` permitted [as ruled].
2. The list of record v2 (§2) in place of the sweeps ruling's §2, from today [adopted].
3. Ledger (62) [recorded].
