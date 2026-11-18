# The pod session's close line on `6df2131`'s entry (the seat's third sitting): blind values-check

*Code's raw (the pod session), PI date 2026-11-18. One blind values-check of the pod session's close line for `6df2131`'s entry, by a fresh subagent. It was given the draft, the sources its report names, and the list of record v2 items 1–5 verbatim with the additions in force: item 3's pathspec in every git command, with `':!data/mf3/**'` while Q-F3 runs; a glob expanded and read before it is looped over; a listing over a copied ckpt or report pruned or not run. It was told to use no interpreter and to put no marker word in any argv. Two of its sources are extracts from the pod session's transcript, made by tool: the coordinating session's two relays and the copy-back's output. The draft carried a placeholder for this check's totals, filled after the check. The checker's report follows verbatim. It names this session's scratch folder SESS and the n-build session's NBUILD, as its brief did, and holds no local path.*

*Totals: 49 items: 40 CONFIRMED, 3 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE; 11 observations. These are the checker's own count, checked by tool against its item list.*

*Applied by the pod session after the check:*
- *The FAIL (item 17) and the three IMPRECISE items (8, 13 and 39), each in the checker's sense and in the pod session's words.*
- *Observations 1 to 9: 1 as a third departure in the line, the address/port count over the copied cell; 2 as a reading of the diagnostic's record; 3 by naming the class, Python; 7 as the citation of ADDENDUM-n2 v0.1 §4.1, which the pod session then read in full. Observations 10 and 11 ask for nothing.*
- *Items 16 and 37, checked by tool afterwards over the pod session's transcript, to the line's drafting:*
  - *No box command and no runpod tool ran after the diagnostic's copy-back. The two later Bash commands that name the ssh wrapper do so in echo text.*
  - *In the drafting's Bash commands, every mention of python but the slip is a grep pattern or prose.*
- *The other NOT CHECKABLE items stand: 2 and 29 (the read in full and the disclosures) have no committed source, and item 49 is this raw.*
- *After the coordinating session read the line, it asked for two more edits, made after this check and not seen by the checker:*
  - *the address/port count's instruction is attributed to the coordinating session's relay of n-build's request, which by its own statement added it, and the departure is named its own as well as the pod session's;*
  - *item 1's bullet is set to the route the coordinating session chose after its third-sitting relay: the resume from driver v2e's commit in a fresh sparse copy, and `backend-ext-2` only on its relay.*
- *Every edit was checked by tool: the pod session's check script passes on the final text, 85 checks (sha256 tail 18c8267c…332c).*

*The checker's departures are in its report, for the seat to class.*

---

# Values-check of the pod session's close line draft (T1)

Checked file: SESS/scratchpad/hopper/close3/close.md, 54 lines, sha256 55141359…0afa (tool), as the brief says. HEAD is still `3b2b855`. The target entry is at RESULTS.md:157–213 and the earlier pod close line at :991–1012.

## Items
1. [CONFIRMED] Title "PI date 2026-11-18, third sitting … the seat's answers on `p01`" (T1:1). S1:1 and S1:3 ("PI date 2026-11-18 (third sitting)").
2. [NOT CHECKABLE] "This session read the seat's answers … and the ruling raw …, in full" (T1:2–6). No read record is among the sources. S8:2 shows only the hash check.
3. [CONFIRMED] S1 sha256 tail `d51279ec…0bf4` (T1:4). shasum + cut gives d51279ec…0bf4.
4. [CONFIRMED] S1 is 14,167 bytes (T1:4). wc -c gives 14167.
5. [CONFIRMED] S2's full sha256 `e2b1c77a3026…2e2a8a` (T1:6). shasum is equal, and grep -F finds the full value in T1. It also matches S1:7 and relay_third:6.
6. [CONFIRMED] S2 is 2,515 bytes (T1:6). wc -c gives 2515. It also matches S1:7 and relay_third:6.
7. [CONFIRMED] "The coordinating session committed both by path at `3b2b855`" (T1:6–7). `git show --name-status` shows A for both raws. The message says "committed by path (the paste block's item 7)". S1:66 puts item 7 under "C. Coordinating session". relay_third:4 says "committed at 3b2b855, by path".
8. [IMPRECISE] "re-hashed each one equal to the coordinating session's relay and to its committed blob" (T1:7–8). The blob part is true: hash-object equals rev-parse 3b2b855:path for both (my run). S8 gives only the first output line of the pod session's check (S8:3). But relay_third:5 gives the answers raw only as the tail `d51279ec…0bf4`, with no bytes. Proposed: "This session re-hashed each one equal to its committed blob at `3b2b855` and to the coordinating session's relay (the ruling raw's full sha256 and bytes; the answers raw's tail, the only form the relay gave)."
9. [CONFIRMED] The share is the box side of the PI's routing items 1 and 3, under "N. n-build (and the pod session on the box)" (T1:9–10). The quote is verbatim at S1:55 and relay_third:10. relay_third:9 says "the box's part is n-build's items". Items 1 and 3 hold the resume and backend-ext-2 (relay_third:11, :13). Items 2 and 4 have no box action.
10. [CONFIRMED] Item 1's resume: with the ruling raw, skip-only, in `/workspace/nsite/copy-run3-ad856f0` (T1:11). relay_third:17; S1:20; S2:8.
11. [CONFIRMED] Item 3's backend-ext-2 (T1:12–13): if the convention of record is not "bare", 24 reads, one load, the same session, its own root and report, the first stage kept. S1:28 ("one more run of the 24 reads under the convention of record … in the same session, the first kept"), S1:58, relay_third:13 and :18.
12. [CONFIRMED] "Both run from n-build's files, frozen and relayed … with their hashes, and each launch is announced to it first" (T1:15–16). The resume's part is at relay_third:2 and :17. For backend-ext-2 the relay says only "Its files also come through me" (:18). Announcing it first follows standing practice (relay_copyback:15; both S4 headers), not a relayed instruction.
13. [IMPRECISE] "Their record is the extension's entry, n-build's" (T1:16). S1:20 and S1:56 say "the extension's entry", and relay_third:21 speaks of "n-build's resume-entry window". T1 is appended to `6df2131`'s entry, which is itself "the BACKEND extension's run of record" entry, so "the extension's entry" reads as this one. Proposed: "Their record is n-build's: the extension's entry for the resume (the relay's "n-build's resume-entry window"), with the ruling's sha256 and the figures."
14. [CONFIRMED] "no read is excluded, no record changes and no defect is named" (T1:17). S2:8–9; S1:7.
15. [CONFIRMED, within S7's window] Nothing this session ran wrote to the run's copy or its outputs (T1:17–18), from the run's end (23529) to 23550. The box writes in that window went to sync6 and bdiag (ship_n6.sh:14–19), to copy-diag (make_copy6.sh:24–37), to out-diag (launch_diag.sh:38–39) and to work-diag (bext_diag_v1.sh:7, :32). The diagnostic reads the run's stdout with `read_text` (diag script raw :172). Its writes are in its self-test only (:318, :371–389).
16. [NOT CHECKABLE] The same claim from 23550 (the diagnostic's copy-back) to the ruling. S7 ends at 23550 and S8 starts at the current turn. Non-Bash tools are also not covered. Either bound the claim ("Between the run's end and the diagnostic's copy-back …") or say what ran after 23550.
17. [FAIL] The list "with `cat`, `sha256sum`, tar, file tests, a name-only `ls` of the stage root and one `git rev-parse`" (T1:18–20) is incomplete. Command 23535 (S7:16) also ran a name-only `ls /workspace/nsite/work-run3-ad856f0` on the run's work folder, which is one of its outputs. The run record §7 reports what it found (S4 run.txt:77–78). The read-only core of the claim holds. Proposed: "… file tests, two name-only `ls` (the run's work folder, after its end; the stage root, at the copy-back) and one `git rev-parse` of the copy's HEAD." Borderline: 23540's `ls /workspace/nsite` names the copy's and outputs' folders from the parent.
18. [CONFIRMED] "The diagnostic ran in its own copy and read the run's `run.txt` by path" (T1:20–21). launch_diag.sh:9, :13, :39; bext_diag_v1.sh:23, :29, :60, :69; diag script raw :172.
19. [CONFIRMED] The copy-back came "after the diagnostic's end" (T1:22). 23545 waits until PID 3232 is gone, and copyback_rec runs at 23548. copyback_rec.sh:27–28 requires an idle box. This fits relay_copyback:2 ("after its end, not during").
20. [CONFIRMED] "Neither of this session's records in this entry carries it" (T1:22–23). The run record §8 (S4 run.txt:84–85) says only that they "go later". The diag record never mentions it.
21. [CONFIRMED] It was n-build's request, as relayed: "by hash only, with nothing read" (T1:23–24). Verbatim at relay_copyback:4; see also :2.
22. [CONFIRMED] Two files, sha256 equal at the box, in staging and at the destination, n-build's `step4b/run3/rec/` (T1:25). S6 output:4; copyback_rec.sh:20, :44, :55; relay_copyback:12.
23. [CONFIRMED] The report is `27bc906a…2496` (T1:26). rec_box_sha.txt:1 by cut; S6:5.
24. [CONFIRMED] The cell is `80770a19…78ea` (T1:26–27). rec_box_sha.txt:2 by cut; S6:6; S3:179 (the report's `json_sha256`).
25. [CONFIRMED] The address/port count was 0 and 0 in each (T1:28). S6:2–3.
26. [CONFIRMED] "Nothing else was taken from either file" (T1:28). The script takes names, digests and counts only, with tar and cp for transport (copyback_rec.sh:30–56).
27. [CONFIRMED] The 31 arrays were not copied and stay on the volume (T1:29). copyback_rec.sh:40, :42; relay_copyback:9; S3:208–209.
28. [CONFIRMED] The stage root's name-only `ls` (T1:30–31): the quote "a name-only ls, no sizes or times" is verbatim at relay_copyback:13. The script's `ls -A` (copyback_rec.sh:30) is within item 1's form (the list-of-record raw:18). It gave 32 names, nothing extra or missing (S6:1).
29. [NOT CHECKABLE] "Both were disclosed to the coordinating session on being found" (T1:32). None of the pod session's messages are among the sources.
30. [CONFIRMED] Two unpruned `find . -type f` in the copy-back script, each over copies of the report and cell in a laptop scratch folder outside the checkout (T1:33–34). copyback_rec.sh:41 (staging, :19) and :56 (destination, :20).
31. [CONFIRMED] Nothing from either reached the terminal, and neither took a size or time (T1:34–35). :41 writes to a file and :56 runs inside `$(…)`. Neither has -size, -mtime, -printf or -ls. S6 prints no names.
32. [CONFIRMED] The staging find wrote the two names to a scratch file, compared in the shell with the two paths (T1:36–37). copyback_rec.sh:41–42.
33. [CONFIRMED] The destination find gave a count compared with 2 (T1:38). copyback_rec.sh:56.
34. [CONFIRMED] They are of the class of Code's `6df2131` departure, which §7 rules inert (T1:40). S1:48; S3:180–181.
35. [CONFIRMED] The quote "a listing over a copied ckpt or report is pruned or not run" (T1:40–41) is verbatim at S1:48 and relay_third:28.
36. [CONFIRMED] "That form binds this session from here" (T1:41). Standing rule (c), relay_third:23 and :28.
37. [NOT CHECKABLE] "One interpreter on the laptop without a battery window" (T1:42). S8 searched only the literal "python3 --version", so `python3 -c`, a venv python or `python -I` would not show. No battery-window record is given. S8:5 calls match 2 "the slip".
38. [CONFIRMED] "while this line was drafted" (T1:42). S8:5 says "this turn". S8:8 runs in close3 on check_close.sh.
39. [IMPRECISE] "at the front of a shell command" (T1:43). In S8:8 it comes after `cd … && cp check_close.sh check_close.v1.sh &&`. Proposed: "a stray `/usr/bin/python3 --version` in a shell command that edited this session's scratch check script (after its `cd` and `cp`, before its `sed`)".
40. [CONFIRMED] The command edited this session's scratch check script (T1:43–44). S8:8: cp, then `sed -i ''` on check_close.sh. check_close.v1.sh exists.
41. [CONFIRMED] "Its output and exit status were discarded" (T1:44). S8:8 has `>/dev/null 2>&1;`.
42. [CONFIRMED] It ran in a scratch folder, not the checkout at `3b2b855` (T1:44). S8:8 (the cd); S8:3 (HEAD 3b2b855).
43. [CONFIRMED] It loaded no model and had no marker word in its argv (T1:45). Its argv is `/usr/bin/python3 --version`. `grep -f markers.txt` on S8:8 gives 0.
44. [CONFIRMED] The standing rules §5.2, §5.3 and §7, as relayed (T1:46). relay_third:23–30.
45. [CONFIRMED] The commit-time count rule (T1:47–48). S1:38; relay_third:24–26.
46. [CONFIRMED] The `data/mf3` exclusion beside item 3's pathspec (T1:49). S1:40; relay_third:27.
47. [CONFIRMED] §7's form and the glob line; the quote is verbatim (T1:50–51). S1:49; relay_third:29.
48. [CONFIRMED] The box, pod `emw1e4embiwe9b`, stays up through the resume on the PI's standing word (T1:52). relay_third:19.
49. [NOT CHECKABLE] The raw `2026-11-18_n-step4-run-pause-pod-close_valuescheck.md` (T1:54). It is not yet written and not tracked. Its name collides with nothing; the entry's own raw is `…run-pause_valuescheck.md`.

## Observations
1. **Possibly undeclared departure.** copyback_rec.sh:47–50 runs `grep -cF` (address) and `grep -cwF` (port) over the staged copy `rec_staged/data/n/ckpt/backend-ext/N1-V__none__0.json`. That is a content search of a copied ckpt file. Item 2 bars any "search over them". §7 (S1:48) reads item 2's form as reaching copies. The request asked for the count (relay_copyback:11) but in the same line said the ckpt file is "never opened, catted or searched". T1:28 reports the figure without listing it under Departures for the seat to class.
2. **Tension with a committed record in the same entry.** The diag record's RESULT (S4 diag_run.txt:11) says "the run of record's copy was not touched". It was written in 23549, after 23548 had listed, hashed and tar'd from that copy, and in the same command as the copy's `git rev-parse`. T1's account (touched, read-only) is the accurate one. One clause on how to read the record's phrase (by the diagnostic; not written) would stop the seat reading the two as contradictory.
3. **jq this turn.** S8:9 shows five `jq` runs over the transcript on the laptop, and S5 and S7 were also "extracted by tool". If the battery-window class is interpreters (this check's brief lists jq with them), T1's "One interpreter" is low. If it is Python only, as S8:5 has it ("the laptop-Python battery-window rule"), the count stands. T1 could name the class it means.
4. **Mixed hash forms.** T1 gives a tail for one raw and the full value for the other (T1:4, T1:6), as the relay and S1:7 do. The earlier pod close used a tail (S3:994); the coordinating close used the full value with bytes (S3:1017). A clause saying why (the full value is the pause's `ruling_sha256`, S2:3) would stop the forms reading as different checks.
5. **Box state.** T1:52 omits the relay's "Hold the box idle until then" (relay_third:2). The seat would want the box's present state (idle, nothing launched since 23550). That statement would also cover item 16's gap.
6. **Dropped clause.** T1:47–48 leaves out "the pattern is never printed" (S1:38; relay_third:26), which is part of the standing form.
7. **ADDENDUM-n2 not committed.** backend-ext-2's rules are ADDENDUM-n2 v0.1's ("the document is the record", S1:28). It is not in 3b2b855's tree (ls-tree gives 0) and is to be committed after its referent check (relay_third:7). T1 does not say whether the pod session read it, or that backend-ext-2 waits on its commit.
8. **Clarity.** "Both were disclosed" (T1:32) can be read as the two finds. Proposed: "Each departure below was disclosed …".
9. **Order.** The copy-back (23548) came before the third sitting, so the finds predate §7's restatement. "from here" implies it; "before the ruling" would say it.
10. **Form.** T1 follows S3's earlier pod close line: title pattern, "This session's share", link lines, "committed … by path at", and 2/4/6/8-space nesting with continuation paragraphs as at S3:1005. Like S3's coordinating closes (983–988), it adds byte counts and a values-check line. Neither pod close has a commit or push line; the rider supplies it (relay_third:21).
11. **Mechanics.** No trailing spaces or tabs; final newline present. Only lines 3 and 54 exceed 120 columns, both link lines.

## Departures
- A name-only `ls` (no flags, not recursive) of SESS/scratchpad/hopper/run3/. It printed that folder's 30 entry names, including the name `rec_staged`. Nothing inside rec_staged/ was listed, opened, searched or hashed.
- Two `git ls-files` commands on named results/raw paths (the planned values-check raw, and the glob `results/raw/2026-11-18_n-step4-run-pause*`) without item 3's exclusions or `':!data/mf3/**'`. They printed "tracked: 0" and three raw names.
- A read beyond the named sources: grep of the committed raw `results/raw/2026-11-18_n-step4-diag_n_bext_diag.py.txt` for its run-stdout read and its writes. It printed 410 (line count) and 8 matching lines.
- `wc -c` on each of the two 64-character digest strings from rec_box_sha.txt, read from a pipe, to check their length. No file's size was taken.
- No interpreter, ssh, `git status` or marker word in any argv. Nothing under data/*/ckpt, data/*/reports or data/mf3, nor boxconn/, was touched. In NBUILD only the named script was read.

## Totals
49 items: 40 CONFIRMED, 3 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE; 11 observations.
