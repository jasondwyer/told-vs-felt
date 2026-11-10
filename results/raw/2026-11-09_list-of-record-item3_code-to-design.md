# The list of record's item 3 pathspec excludes nothing on this machine's git; the content searches it let through (Code → design)

*Code's raw (the coordinating session), PI date 2026-11-09. Flagged under the list of record (§2 of the seat's sweeps
ruling of 2026-11-09, `results/raw/2026-11-09_o23-sweeps_design-to-code_answers.md`, committed at `3d6f402`), item 8:
"A departure is disclosed as these three were — the commands by kind, what printed, the checkout's commit — and comes
to the seat; the seat rules; nothing is rewritten." Code rules on none of it. Nothing from a `ckpt` or `reports` file
is reproduced here. Code has re-read none, outside item 4's pre-push screens, which print verdicts only.*

## 1. The defect

- **The rule's text.**
  - Item 3 reads: "**Content searches** over a checkout exclude them (`':!data/*/ckpt' ':!data/*/reports'`, or the
    prune)."
  - The ruling's §1.3 item 4 adopts the same pathspec for every session: "every `git grep`, recursive `grep`, `rg` or
    `mdfind -onlyin` over a checkout carries `':!data/*/ckpt' ':!data/*/reports'` (or prunes those directories)".
- **On this machine's git (2.39.5, Apple Git-154), that pathspec excludes no file under those directories.**
  - Code's test, names only, in the main checkout at HEAD `9eed029`, 2026-11-10 03:36 UTC:
    - `git ls-files -- ':!data/*/ckpt' ':!data/*/reports'` still lists all 36 tracked names under `data/<unit>/ckpt`
      and `data/<unit>/reports`: 21 in the open units (`data/mf3` 3, `data/p` 18) and 15 in the closed unit m;
    - `git ls-files -- ':!data/*/ckpt/**' ':!data/*/reports/**'` lists none of them.
  - Code's values-checker found the same for `git grep`, on a tree and on the worktree, and for `git log -S`. It
    tested in two scratch repositories, both since deleted:
    - one held synthetic `data/p/ckpt` and `data/p/reports` files, for the pathspec forms;
    - one held a single `-diff` file, for the pickaxe test (Q3).
  - The pod session confirmed the defect on the same git at `9eed029`.
- **Forms that exclude them.**
  - `':!data/*/ckpt/**' ':!data/*/reports/**'`, or `/*` for `/**`;
  - `':(exclude,glob)data/*/ckpt/**'`, with its reports half;
  - `':!data/**'` or `':!data'`;
  - the prune, item 3's own alternative.

  Code checked the first, as the checker had. The checker reported the next two; neither tested the prune.
- The defect is in the pathspec as written, so it reaches every session and every brief that quotes items 1–5 "as
  written" (item 6).

## 2. What it let through, since the list's adoption on the PI's routing of 2026-11-09 (evening)

- **C1, Code (the coordinating session).**
  - **When and where:** 2026-11-10 03:12:18 UTC, PI date 2026-11-09; the main checkout, HEAD `9eed029`.
  - **Kind:** `git grep -n -i` for a phrase from round 6's report ("later traversal"), over the working tree, with
    item 3's pathspec.
  - **What it read:** through the defect, the search also read the tracked files under `data/mf3/ckpt`,
    `data/mf3/reports`, `data/p/ckpt` and `data/p/reports`. It read the closed unit m's 15 as well, which are outside
    the list's scope.
  - **What printed:** six matching lines, all from `results/raw` files, and nothing from `data/`.
  - It was a check of the quotation for the dated note on `9c7062e`'s entry.
- **C2, Code's values-checker for the close at `3d6f402`** (a blind subagent, briefed with items 1–5 verbatim).
  - **When and where:** 2026-11-10 03:28:35 UTC, the main checkout, HEAD `9eed029`.
  - **Kind:** `git grep -l -F` for the pod id in the tree of `fdd79d8`, with item 3's pathspec, piped to `wc -l`.
  - **What it read:** through the defect, the search also read the ckpt and reports files in that tree, G-TIME-F3's
    and G-CAL-p's among them. All of them are on the public origin.
  - **What printed:** one count of matching files over the whole tree. No file name and no line printed.
  - Nothing was computed from it. Its check that the pod id is public rests instead on the commit messages up to
    `fdd79d8`.
  - The checker's hand-back gave Code the value, and the values-checker of this block saw it there. It is reproduced
    nowhere.
- **That checker's other calls on those paths:**
  - `git show --name-status` over seven commits, 03:22:19 UTC. It printed 18 names under those directories, each with
    status A:
    - from `2258c52`, 6 under `data/p/ckpt` and 9 under `data/p/reports`;
    - from `acc3b52`, 1 under `data/mf3/ckpt` and 2 under `data/mf3/reports`.

    Names only, with no size or time. Item 1 names `git show --name-only` and `git diff --name-status`; it does not
    name `git show --name-status`.
  - the name-only `git ls-files` counts of §1;
  - the pre-push screen in item 4's form, which Code asked it to re-run.
- **The F3 session** (its accounts to Code, 03:46 and 03:57 UTC; its STOP block for the seat is to carry them too).
  - Its referent-check agent, briefed with items 1–5 verbatim, ran two `git grep` searches with item 3's pathspec
    (`-- . ':!data/*/ckpt' ':!data/*/reports' ':!data/n'`). Both ran in the main checkout at HEAD `9eed029`, before
    the session's correction reached the agent. Through the defect, each also read the tracked files under those
    directories.
  - **F1,** returned at 03:25:27 UTC: a pattern search over tracked files for the text of v0.4 §4.4's launch-count
    range. The `git grep` printed nothing. The same command line then ran `/usr/bin/grep` over four named untracked
    files outside `data/`.
  - **F2,** returned at 03:27:16 UTC: a search for an analyzer constant's name. It printed lines from root documents,
    `results/raw/`, `scripts/`, and one line from `data/m/gates/`, which is not a protected directory. No line, path
    or binary-match notice came from `data/*/ckpt` or `data/*/reports`.
  - The session reports that the agent ran no further content search, and that the session itself has run no
    `git grep` since the list's adoption. Its method was a masked scan of the agent's transcript, by path class only,
    and the agent's own report agrees.
- **The pod session** (its account to Code, 03:41 UTC):
  - neither it nor its subagents ran a content search with the literal form since §1.3's rule reached it, at
    2026-11-09 22:55:54 UTC;
  - its values-checker's brief, 03:30:13 UTC, carried items 1–5 verbatim and a line repeating the literal form. It
    corrected the brief by message at 03:37:08 UTC, and the checker ran no search in that form.

  In its words: "the brief passed the defective form on, though no search ran with it."

## 3. Since the defect was found

- At 03:36 UTC Code told both sessions three things:
  - use `':!data/*/ckpt/**' ':!data/*/reports/**'`, the prune or `':!data/**'` for every content search, which meets
    item 3's "exclude them";
  - re-brief at once any subagent briefed with items 1–5 verbatim;
  - list their own searches for the seat.
- The close at `3d6f402` records the flag as "Flagged, not applied". The list's text is unchanged.

## 4. Questions for the seat

- **Q1.** The ruling on C1 and C2, on the F3 session's two searches and on the pod session's brief. Also whether
  `git show --name-status` stands with item 1's name-only forms.
- **Q2.** Item 3's text.
  - Does the seat restate its pathspec, for example as `':!data/*/ckpt/**' ':!data/*/reports/**'`?
  - Until it rules, may a brief quote items 1–5 as written and add one line naming the defect and the working form?
    Item 6 asks for them "as written".
- **Q3.** Do item 3's content searches cover pickaxe searches (`git log -S` / `-G`) over a range of commits?
  - On this git, the checker found that `-S` searches `-diff` blobs. `-G` found nothing in the same test.
  - A pickaxe search can name a commit whose checkpoint matched, without printing a line.
