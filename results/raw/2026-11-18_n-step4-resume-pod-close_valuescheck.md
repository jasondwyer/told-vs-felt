# The pod session's close line on the extension's resume (n step 4): blind values-check

*Code's raw (the pod session), PI date 2026-11-18. One blind values-check of the pod session's close line on the extension's resume, by a fresh subagent. It was given the draft and the sources its report names, among them two extracts from the pod session's transcript made by tool: the coordinating session's eight relays about the resume, and seven commands with their outputs. It was also given the list of record v2 items 1–5 verbatim, with the additions in force: item 3's pathspec in every git command, with `':!data/mf3/**'` while Q-F3 runs; a glob expanded and read before it is looped over; a listing over a copied ckpt or report pruned or not run. It was told to use no interpreter and to put no marker word in any argv. The draft carried a placeholder for this check's totals, filled after it. The checker's report follows verbatim. It names this session's scratch folder SESS and the n-build session's NBUILD, as its brief did, and holds no local path.*

*Totals: 38 items: 30 CONFIRMED, 6 IMPRECISE, 0 FAIL, 2 NOT CHECKABLE; 9 observations. These are the checker's own count, checked by tool against its item list.*

*Applied by the pod session after the check:*
- *The six IMPRECISE items (5, 9, 23, 27, 31 and 35), each in the checker's sense and in the pod session's words.*
- *Observations 1 to 8. Observations 2, 3 and 4 became the bundle, the box-side git and the glob loop under the line's departures, and observation 7 is who held v3. Observation 9 asks for nothing.*
- *Item 14, checked by tool afterwards over the pod session's transcript, by its own order of entries: the coordinating session's HOLD was queued for the pod session after the pod session's report of v2's failure, which followed v2's end. The order check's last row, a second "LAUNCH v2", is the check's own command, whose text names the launch script; v2 was launched once.*
- *Item 36 stands: the line's disclosure is made by sending it.*
- *After the check, n-build's request for the resumed report came, relayed by the coordinating session, and the pod session copied the report back by hash only. The line's bullet for item 27 records that copy-back. The checker did not see it.*
- *Every edit was checked by tool: the pod session's check script passes on the final text, 83 checks (sha256 tail 8c59fc5a…d9d7).*

*The checker's departures are in its report, for the seat to class.*

---

# Values-check of the pod session's close line on the resume (T1)

Abbreviations: SESS and NBUILD as in the brief; "tsv" = SESS/scratchpad/hopper/resume4/all_tool_uses3.tsv; "inv" = SESS/scratchpad/hopper/resume4/git_inventory.txt. I computed every hash tail by tool, with `shasum -a 256 | cut -c1-8` and `cut -c61-64`. All eight tails in T1 match their files, in T1's order.

## Items
1. [CONFIRMED] Heading, PI date 2026-11-18, "the PI's routing of the third sitting (item 1 of "N. n-build (and the pod session on the box)")" and the coordinating session's relays. Evidence: S1:55–56, where the heading is verbatim apart from its bold markers and item 1 is Q1, the resume. Corroborated by results/raw/2026-11-18_third-sitting_pi-routing.md:1,16–17,30 ("PI: Route as given"), and the relays are S2's eight messages.
2. [CONFIRMED] "ran the box side of the resume on pod `emw1e4embiwe9b`". Evidence: S3:6,16 (RUNPOD_POD_ID=emw1e4embiwe9b); S4 records, line 1.
3. [CONFIRMED] The two run records are in n-build's `step4b/resume2/out/` and `step4b/resume4/out/`, beside each run's output. Evidence: the S7 files, read by name and hashed; S3:73–77 and 85–92.
4. [CONFIRMED] "The sync, once for both attempts". Evidence: box_sync_n7.sh ran once (tsv:4080; no later sync in tsv:4081–4153); ship_n8.sh:3–4 says "No bundle"; S4 resume4:29–30.
5. [IMPRECISE] "A bundle of `ad856f0..main` was made with main at `1272702` (`f40c164a…0fff`)". The facts are true: tsv:4075 checks main before and after; S3:49; the bundle's sha256 computes to f40c164a…0fff. But the hash sits right after `1272702` and reads as the commit's hash. Proposed: "A bundle of `ad856f0..main` (sha256 `f40c164a…0fff`) was made with main at `1272702` before and after."
6. [CONFIRMED] "fetched into the box repo under a new side ref, `refs/bundles/n-site7`, with no fast-forward". Evidence: box_sync_n7.sh:14,19,21 (`git fetch -q "$B" "main:$REF"`, which refuses an existing ref); S4 resume2:29–34.
7. [CONFIRMED] "The box checkout stayed at `ad856f0` and clean, so its worktree never received the stage's report and cell file". Evidence: box_sync_n7.sh:17–18,25–26; S4 resume2:32–34 and resume4:29–30,120; make_copy8.sh:19; S2:11–13.
8. [CONFIRMED] v2 is `f166e7ce…19f2` and "failed at its copy-in". Evidence: computed on S5 v2; S4 resume2/out_view.txt:7–9.
9. [IMPRECISE] "It ran after its announcement, as PID 3824, in the fresh copy `/workspace/nsite/copy-resume-1272702`". The announcement came first (S2:81; tsv:4082 SendMessage before the 4084 launch; S4 resume2:6). But 3824 is the PID of the nohup wrapper, not of the script: launch_resume2.sh:41–42 echoes `$!` of `nohup bash -c '…' &`, and S4 resume2:55 says "The wrapper's PID was 3824". Also, the script ran from /workspace/nsite/resume2 with the fresh copy as its target, not inside it. Proposed: "It ran after its announcement, under the wrapper PID 3824, with the fresh copy `/workspace/nsite/copy-resume-1272702` as its target."
10. [CONFIRMED] "Its step 0 held." Evidence: S4 resume2/out_view.txt:1–6.
11. [CONFIRMED] The first `cp -p` was refused its permission-preserving step on `/workspace` ("Operation not permitted"), and it exited 1. Evidence: S5 v2:98–102; out_view.txt:8, where the quote is verbatim; S7 bext_resume_v2.exit reads "1".
12. [CONFIRMED] "Nothing after it ran, and no model was loaded." Evidence: v2:102 (only the failure branch's echo and exit 1 ran); the output ends at line 9; the load is in step 5 (v2:136), which never started.
13. [CONFIRMED] The record is `2f606ca7…1ce9` and the output is `0c926ca3…bf79`. Evidence: computed, equal in S4 and S7, and `cmp` shows the S7 output equals S4's out_view.txt; S3:74,76.
14. [NOT CHECKABLE] "The coordinating session's hold on v2, for v3, reached this session after v2 had ended." S2 gives only the order of arrival, and tsv records tool uses, not message arrivals. Every trace is consistent with the claim but none settles it: S2:81 says the HOLD was still "queued" after the coordinating session had seen the v2 announcement; the pod session's first trace of the HOLD is its memory note at tsv:4104 ("crossed my launch … v2 had already run and failed"), which comes after tsv:4101 ("PID 3824 ended before the wait") and the v2 copy-back at tsv:4097.
15. [CONFIRMED] "v3 (`fa91a17d…da36`) was never shipped or run". Evidence: computed hash. tsv shows the box used only at 4080, 4081, 4084, 4086, 4089, 4091, 4112, 4130, 4133, 4135, 4140 and 4141, plus the ship_n7, ship_n8, copyback7 and copyback8 scripts, and none of these touches v3. tsv:4108 has the note "NOT shipped and NOT launched". Also S2:99 and S4 resume4:6.
16. [CONFIRMED] "it still copied with `cp -p`". Evidence: S5 v3:107; S2:59,99.
17. [CONFIRMED] "its command named the copy v2 had left with the stage's folders". Evidence: S2:67 names copy-resume-1272702; v2's `mkdir -p` (v2:98) ran before the failing cp, since its own failure message printed; v3:89–90 refuses those folders; tsv:4108.
18. [CONFIRMED] The probe was at the coordinating session's request, shell only, in a new folder `/workspace/nsite/probe-cp`. Evidence: S2:103–109; probe_cp.sh:8–21, which refuses an existing folder at :9; S3:22–32.
19. [CONFIRMED] Plain `cp` exited 0, `cmp -s` exited 0, and `cp -p` exited 1 with the same message and created its destination file. Evidence: S3:27–30. The message's file name differs (‘dummy_cp_p.txt’), but its form is the same.
20. [CONFIRMED] v4 is `4fec8670…dd78` and passed. Evidence: computed hash; S7 bext_resume_v4.exit reads "0"; S4 resume4/out_view.txt:74.
21. [CONFIRMED] "v4 is v3 with a plain `cp`." Evidence: `diff` of v3 against v4. The only functional change is v3:107 `cp -p` becoming v4:109 `cp`; the other differences are a comment (v4:19–23), the usage string (:48) and the summary label (:215). S2:121 agrees.
22. [CONFIRMED] "Its launch was announced with its hash." Evidence: S2:149; S4 resume4:7–8; tsv:4132 before 4133.
23. [IMPRECISE] "It ran as PID 4112 in a new fresh copy, … in the same sparse form at `1272702` from the side ref". 4112 is the wrapper's PID (launch_resume4.sh:42–43; S4 resume4:58). The copy facts are true (make_copy8.sh:13–27; S4 resume4:38–45). However, T1 never describes v2's copy, so "the same sparse form" has no antecedent in the line. Proposed: "It ran under the wrapper PID 4112, with a new fresh copy, `/workspace/nsite/copy-resume4-1272702`, as its target: a local clone, `--no-checkout --no-hardlinks`, origin removed, sparse non-cone, detached at `1272702` from the side ref, as v2's was."
24. [CONFIRMED] "It exited 0 with "bext resume v4 COMPLETE (pass)"." Evidence: v4.exit reads "0"; out_view.txt:74, where the quote is a verbatim prefix.
25. [CONFIRMED] The record is `c86e812a…be14`. Evidence: computed, equal in S4 and S7; S3:91.
26. [CONFIRMED] The outputs went to `step4b/resume4/out/` by explicit name, with sha256 equal at the box, in staging and at the destination, and address and port counted 0: the output (`8d286ce4…2a39`), the exit file, resume.txt, hashes.txt and resume-identity.txt. Evidence: copyback8.sh:23–46; S3:82–92; computed hashes. hashes.txt and resume-identity.txt are both 93783db0…7b36, the laptop's hashes file.
27. [IMPRECISE] "The resumed report stays on the box until n-build asks for it, by hash only." This leaves out the route. S2:159 says "on n-build's request through me", and so do copyback8.sh:5–6 and S4 resume4:111–112. Proposed: "The resumed report stays on the box; it comes back only by hash, on n-build's request through the coordinating session."
28. [CONFIRMED] The run copy was only read throughout: its HEAD, and its report, cell file and arrays through the two scripts' copies and digests. Evidence: launch_resume2.sh:33 and launch_resume4.sh:34 read HEAD; v2:74–81 and 100–103; v4:76–83, 105–116 and 196–207; tsv:4091 and 4141 read HEAD only.
29. [CONFIRMED] Both fresh copies, their work and out folders, resume2, resume4, sync7 and probe-cp stay on the box. Evidence: S4 resume4:114–121; S2:101,143,158.
30. [CONFIRMED] "Nothing is removed until the PI's word." Evidence: S2:101 ("Cleanup waits for the PI's word."); S2:160.
31. [IMPRECISE] "Three path-taking laptop git commands ran without item 3's pathspec and the `data/mf3` exclusion while Q-F3 runs". The three commands are right and both exclusions are missing (inv:51–53; S3:35,62). But the `git log` took no path, so "path-taking" misdescribes it. Proposed: "Three laptop git commands over the tree or its history ran without … : … one `git log --format='%h %s' ad856f0..main`, with no path (six commit ids and subjects, each line cut at 110 characters)." See item 35 on whether the bundle belongs here too.
32. [CONFIRMED] Two `git ls-tree --name-only` of `data/n/ids/`, at `1272702` and at `ad856f0`, six names each. Evidence: S3:62,64–65; tsv:4067.
33. [CONFIRMED] One `git log --format='%h %s' ad856f0..main`, six commit ids and subjects. Evidence: S3:35,54–59, where `| cut -c1-110` cut the subjects. My own S9 log of the range, with the pathspec, shows the same six ids.
34. [CONFIRMED] "Nothing under `data/mf3`, a ckpt or a reports folder printed." Evidence: S3:37–59,64–65, for the three commands. The bundle commands' output is not in the sources.
35. [IMPRECISE] "The other laptop git commands of this run take no path: `rev-parse`, `merge-base`, `hash-object`, `git show` of named blobs and `git bundle`." The inventory is complete (inv:44–59; a grep for "git" over tsv:4061–4153 finds no other laptop git, and the laptop-run scripts ship_n7, ship_n8, copyback7 and copyback8 contain none). But the wording is literally false in places:
    - `hash-object` took a file path;
    - `rev-parse 3b2b855:results/raw/…` and `show 1272702:scripts/n_sessions.py` use the `<rev>:<path>` form;
    - `git bundle create … ad856f0..main` walked the same range as the git log and packed every object in it, including the stage's report and cell blobs of 6df2131.

    Proposed: "The other laptop git commands of this run take no pathspec and printed no name from the tree: `rev-parse` (of ids, and of one `<rev>:<path>` compared in the shell, item 1's form), `merge-base --is-ancestor`, `hash-object` of n-build's ruling copy, `git show` of one named blob piped to `shasum` (twice), and `git bundle` create, list-heads and verify of `ad856f0..main`, which packs the range's objects, the report and cell blobs of `6df2131` among them, printing none of them."
36. [NOT CHECKABLE] "Disclosed to the coordinating session with this line." This describes a future action, and no source records it.
37. [CONFIRMED] The box was held idle at the line's drafting, with everything left as it is. Evidence: S2:158; no box command after the copy-back (tsv:4146) up to the end of the list at 4153. The drafting itself happened after the list ends.
38. [CONFIRMED] "Whether it stays up while the seat rules is the PI's call." Evidence: S2:160.

## Observations
1. **The failed copy probably holds the report's bytes.** v2's `mkdir -p` made the stage's folders before its `cp -p` failed, and the probe shows that `cp -p` on this volume creates its destination before failing (S3:29–30). So copy-resume-1272702 very likely holds a file at data/n/reports/backend-ext.json, with unknown contents; S4 resume2:69–71 says the session never looked. T1 says only "with the stage's folders" (line 16), yet lists this copy as staying on the box (line 29). The seat may want the probable report file named, both for cleanup and for item 2's read domain on the box.
2. **The bundle carries the stage's blobs.** n-site7.bundle carries the report and cell blobs of 6df2131 (S2:11; S4 resume2:33). It persists in two places: the pod session's laptop scratch (SESS/scratchpad/hopper/resume2/n-site7.bundle) and /workspace/nsite/sync7. It printed nothing, and it was the transport the coordinating session proposed (S2:13). Still, it walked the same range as the `git log` that the paragraph counts as a departure, so the seat may want to class it explicitly rather than leave it under "take no path".
3. **Box-side git is outside the paragraph's scope.** The paragraph covers laptop commands only. The pod session's own box scripts also ran `git status --porcelain --untracked-files=all`, which is not the bare form item 1 names:
    - on the non-sparse box checkout, in box_sync_n7.sh:18,26;
    - on the fresh copies, in make_copy7.sh:27, make_copy8.sh:29, launch_resume2.sh:32 and launch_resume4.sh:33.

    box_sync_n7.sh:24 also ran `git diff --name-only "$BASE" "$T" -- data/mf3`. Each of these prints only on a failure branch, and the records report success. One line on box-side git would close the question.
4. **A box-side glob loop.** make_copy7.sh:29–31 and make_copy8.sh:31–33 loop over `data/*/ckpt data/*/reports` in the same script that prints the expansion, so the expansion was not read before the loop ran. It matched nothing (S4 resume2:40, resume4:43). This matters only if the briefs' glob line (S1 §7) binds box scripts.
5. **The removal wording differs between T1 and the records.** T1:30 says "until the PI's word", following S2:101. Both records say "nothing removed unless n-build or the coordinating session asks" (S4 resume2:78, resume4:114). The committed records and the line should agree.
6. **Facts the seat may want that T1 leaves out:**
    - the end-wait on the PID alone for both runs (list of record item 5; S4 resume2:55–56, resume4:58–59; tsv:4086,4135);
    - the exit-file hashes, v2's 4355a46b…d865 and v4's 9a271f2a…86aa;
    - the work-file hashes: resume.txt 069b1448…2db4, and hashes.txt and resume-identity.txt both 93783db0…7b36, byte-equal to the laptop's bext_resume_hashes_v2.txt;
    - v2's three work files, which were absent (S3:71).
7. **Who decided against v3.** The pod session held v3 on its own reading (tsv:4108) before the coordinating session ruled it out with "Don't run v3 either: it has the same cp -p." (S2:99). T1 is accurate; naming the concurrence would show the seat who decided.
8. **Clarity.**
    - "The coordinating session's hold on v2, for v3," is hard to parse; "The coordinating session's HOLD on v2, superseding it with v3," reads better.
    - "was refused its permission-preserving step" could be "failed at its permission-preserving step".
    - `sync7`, `resume2`, `resume4` and the work and out folders appear without saying what each holds; S4 resume4:114–121 has that.
    - I found nothing superfluous.
9. **Formatting.** The blank line at T1:35 makes the Departures bullet a loose list item; check that it renders as intended. The raw link at T1:42 points to a file that does not exist yet.

## Departures
1. **tsv lines outside the stated range.** My first scan printed the length and first 220 characters of every line 4060–4153. That includes 4060–4062: a plan update, line 4061 (the pod session's name-only `ls -A` and hashing of n-build's resume2/frozen files) and a Read entry. My later scans for "git", "bx.sh", "resume3" and the marker words (the marker scan by `grep -f`, counts only) started at 4061, and none printed anything from 4061–4062.
2. **Git commands beyond S9's three forms, in the repository:**
    - `git merge-base --is-ancestor ad856f0 1272702`, which cannot take a pathspec; it printed only my echo line;
    - `git rev-parse main` and `git rev-parse HEAD`;
    - `git log --format='%h %s' ad856f0..1272702 -- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`, which printed six ids and subjects cut at 90 characters;
    - `git ls-files -- results/raw/2026-11-18_third-sitting_pi-routing.md` with the same three exclusions, which printed nothing.
3. **A repository file outside the named sources.** I read results/raw/2026-11-18_third-sitting_pi-routing.md (committed, outside data/) in full and grepped it once as a single file, to check "the PI's routing". All 31 of its lines printed.

I ran no interpreter and no git status, and put no marker word in any argv. I did not list, open or hash the forbidden folders, and listed no S7 folder. I read bx.sh's callers but not bx.sh itself.

## Totals
38 items: 30 CONFIRMED, 6 IMPRECISE, 0 FAIL, 2 NOT CHECKABLE; 9 observations.
