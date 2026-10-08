# AUDIT-note-release v1.2: integration values-check record (N1 ledger, N12 scrub index, README-NOTE draft)

- Code stamp: 2026-10-08 15:49:10 UTC (date -u). This is a process record. Source: the local workflow results of runs wf_77713d9c-4b0 (build, check, fix, recheck) and wf_23e6f22c-fba (round 2), which are not in the repo, plus Code's own round-3 edits, described below.
- Severity: substantive means the finding would change a number, a status, a STOP/pass outcome or a sentence of the note; minor means wording, locators or precision.

## N1

### Check 1: findings 11 (1 substantive); redaction clean: True
- [substantive] The --note matcher compares numbers by value only, ignoring sign, '%' and context. Any note or SVG numeral that equals the value of some ledger-row numeral is counted as matched and never listed as 'not in ledger'. That includes a conditional-STOP value that ledger section 4e ...
- [minor] Completeness: the block names some figure groups as note figures without quoting numerals. Those groups get no ledger row, although the ledger does hand-map other numeral-free spans.
- [minor] L053's status is carried without the conditional that the item raw attaches to it.
- [minor] The NF branch text attributes to the item raw a reading of block :23 that the item raw does not state.
- [minor] Section 4a lists L032 (and L071, L074) as 'cut from the note' without the item raws' conditions. For L032 the primary mapping picks the stricter of two N2vi rows, although the block's own wording matches the other.
- [minor] The tag candidate including audit raws lists 20 rows, two of which are not-found rows that enter no source. L071 and L074 get an 'entry' at 09c3a8c.
- [minor] The author summary misstates the blame check. The task's per-locator `git blame -L n,n` was done as a spot check. I verified every locator and found no error.
- [minor] The summary's PI item on the tag gives two options, 7742e2c or 09c3a8c. It leaves out the 988e5df case that the ledger itself raises.
- [minor] Note 5 in section 8 names the wrong out-of-record sources.
- [minor] L089's 'source (item raw)' is assembled by N1 from wording carriers in N13's referent note, so its entry commit is that of a carrier of the phrase, not of the bet.
- [minor] The 0.05 in L161 'sub-0.05-cosine' is classified as an identifier, so --note matching ignores the row's only figure.

### Recheck: findings 8 (1 substantive); redaction clean: True
- [substantive] README-NOTE.md's N1 paragraph and its src comments no longer match the N1 ledger. They describe round 1. The ledger was regenerated afterwards (README-NOTE mtime 10:29, ledger 10:36).
- [minor] Section 3 says it lists 'every distinct source the ledger's primary item-raw rows name', but three sources named in the item raws were not resolved. As a result, L142's entry commit is understated.
- [minor] Section 5's 'third branch' takes the latest of several alternative carriers of the same fact. A fact enters the record with its first carrier, so the branch overstates both cases.
- [minor] N3 and N3c give different statuses for the same figure, and the ledger shows this only in a '(see)' line. The pass check and the section-8 notes never flag it.
- [minor] Corrections that item raws route explicitly to N1, and caveats that limit passing rows, are not collected in the pass check. The numeral-based --note matcher will not surface them either.
- [minor] The --note matcher can report a wrong row as 'matched' and demote the correct row to a candidate.
- [minor] Section 1b's 'no row' list reads as the complete list of numeral-free spans the block names, but it is incomplete.
- [minor] L089's source locators are pinned to 72b09a9, not to the record pin bbc9ffe, contrary to the part's rule (4).

### Round 2 check: findings 6 (1 substantive); redaction clean: True
- [substantive] README-NOTE.md's N1 material is still stale against the round-3 ledger. This is round 2's finding 1, which was skipped by instruction and has not been fixed anywhere. The README now contradicts the ledger on row counts, pass counts, the hash, every ledger line it cites, the ...
- [minor] LOC_RE's comma-continuation reads the count after a locator as a second line number. L053's note carriers are therefore malformed, and RESULTS.md@bbc9ffe:18 is blamed and counted as a cited line.
- [minor] 4g's stated reason for being outside the matcher's reach is false for several of its own entries. They do carry new numerals.
- [minor] 4g leaves out item-raw corrections of the same class that bind on note sentences, including one on passing rows. The table disclaims exhaustiveness, but these are close siblings of entries it does list.
- [minor] For C13 and C27, the routing goes in a circle. The item raws hand the decision to N1; the ledger says N1 decides none of them and that 'who decides each is as its item-raw line says'.
- [minor] The 1b preamble contradicts its own table.

## N12-scrub

### Check 1: findings 10 (1 substantive); redaction clean: True
- [substantive] Line 6 says the scrub 'is the file the README and the claims ledger cite as N12's output'. That is not true. Neither file cites the scrub, and the history raw says the opposite.
- [minor] The (vii) row in section 0 and section 8 say README-NOTE.md was 'not present on disk at this run'. The draft now exists, so if this file is committed as is, that line will be stale.
- [minor] Pre-flip item 3 calls the history re-run 'a precondition of the end commit and the tag'. It leaves out the history raw's '(the PI's to bind)', so something the PI has not yet bound reads as already binding.
- [minor] Line 10 says 'The one redacted form printed here is the LoRA phrase's'. That is not true: the file also prints the SSH signing-key fingerprint's redacted form.
- [minor] The history raw labels its use of the fallback for (i) as a deviation from block :77, because the scanners could have been installed. The scrub does not carry that label.
- [minor] Section 5 and the author's PI items pass on, as plain fact, the licenses raw's projection that the sweep gates will fail at the pre-flip re-run. An open values-check finding says that projection text is over-broad, and the scrub does not connect the two.
- [minor] Section 11 does not count the laptop hostname as a redaction-rule value. Routing hard rule (6) lists the laptop hostname explicitly.
- [minor] Two hand-offs in the part raws are not indexed: the content raw's N12(iv) hand-off, and the history raw's finding that six of the PI's untracked documents carry the D1 RunPod ids.
- [minor] Several figures are written into the script as fixed text instead of being read from the raws. All of them are correct at 09c3a8c, but they would silently go stale under a different --audit.
- [minor] Check (e), README-NOTE.md (a sibling's file): two N12 source locators point to the wrong line, and the README leaves out the JSON probe vectors that the history raw (indexed in scrub section 8) asks it to name.

### Recheck: findings 9 (1 substantive); redaction clean: True
- [substantive] The D1 row in section 9 (md line 144) presents the content review's carrier count as if it were current. That count was taken at bbc9ffe. At HEAD, 6 tracked raws carry the D1 values, not 5. RESULTS.md also holds a second RunPod pod id, which the row's singular 'The RunPod pod ...
- [minor] The overall N12 sentence in section 0 (md line 28) says the fail clause applies 'via (i) alone, until the PI resolves (i)'. That is incomplete. The licenses script prints its (iv) pass line only when 0 ids and 0 hosts are unclassified, and the licenses raw projects that this ...
- [minor] The README-NOTE.md snapshot in the index is already stale. Line 26 and section 8 (line 135) record a version of the README that has since been rewritten.
- [minor] Line 28 cites history :413 for both '0 TRUE-SECRET-CANDIDATE and 0 UNTRIAGED', but :413 does not state UNTRIAGED.
- [minor] Some sentences are fixed text rather than computed, although line 9 and the docstring say every summarized figure is read by pattern or asserted. All of them are true at this run; they could become false or self-contradictory when the index is regenerated.
- [minor] Section 3 indexes the content review's N12(ii) hand-offs from its section 8 only. It misses content §7's 'Known carriers outside scope, for the N12(ii) list'. One of those carriers, the conda environment name in paper_analysis.ipynb, appears nowhere in the index.
- [minor] Item 3 of the pre-flip checklist does not warn that re-running the history and licenses scripts with their default arguments overwrites the committed part raws. This index, the README's source comments and the claims ledger cite those raws by line at 09c3a8c.
- [minor] Section 13's 'N12(vi) content: 0 open' can read as 'checked, nothing open'. The record lists no values-check pass for the content part at all.
- [minor] Cross-part, for README-NOTE.md (check e): the README does not name the residual-space probe vectors stored in tracked JSON. The history raw says the README should name them, and section 8 of the index lists this as an N12 input to the README.

### Round 2 check: findings 4 (1 substantive); redaction clean: True
- [substantive] The new re-run warning in section 10, item 3 (md :181, built at script :1003-1006) gets the output behaviour of two of the three part scripts wrong. It says 'Run with default arguments, each part script overwrites its committed raw', but the content script refuses to ...
- [minor] Section 9's attribution no longer matches the D1 row. The intro (md :142) says 'The table summarizes the cited lines at `09c3a8c`; the script reads each figure in it from the cited line or asserts it present there'. Two parts of the reworked D1 row are not from any cited ...
- [minor] One branch of the new computed scope sentence in section 7 (script :896-901) produces a broken sentence. When no path is added and some are modified, the text starts with a lowercase letter and loses the referent of 'were'. This branch does not fire on this run.
- [minor] Finding 9 (README-NOTE.md should name the stored probe vectors) was rejected validly: README-NOTE.md is not one of the N12-scrub fixer's files. But nothing routes it on. The README part's round-2 findings do not include it, and README-NOTE.md still omits it.

## README

### Check 1: findings 13 (3 substantive); redaction clean: True
- [substantive] Row 169 (f1 termination '≈ 1% of rounds by arm') is a conditional STOP that the README never marks for the PI. §4's intro (README:123-125) also gives only two of block :23's branches. It omits 'a STOP on that item if it is not [transcription]' and the ledger's NF and SR readings.
- [substantive] Row 165 ('54 of 101 valid sessions'; 'half the difference between break rates') carries the status 'not found' and the instruction 'cut', but drops N4's cause. That cause says the figure itself reproduces as the record's own audit-v2 correction, so 'cut' points the note at ...
- [substantive] The provenance-table recipe 'computed here from `git show <commit>:<path>`' (README:28) fails for the 10 log-entry rows (1-3, 6-10, 12, 13). N13 hashes the entry text as introduced, not the file, and at the introducing commit the path was RESULTS.md, not the archive path the ...
- [minor] The list of audit parts that need local-only inputs (README:112-113) is incomplete.
- [minor] The map covers 145 of the 161 ledger rows, not all 161 as the author summary says. One range also mixes statuses.
- [minor] Several map rows drop an item raw's disclosure or cause that limits how a figure may be used. One row merges a discrepant ledger row into a 'reproduced' cell.
- [minor] Some PI- or design-seat-pending items appear as settled text without a [PI] marker.
- [minor] §8's tag-commit candidates drop the ledger's caveat. Candidate 7742e2c (2026-09-11) is older than bbc9ffe, which every locator is pinned to. A tag there would contain neither this README, nor the audit raws, nor the block.
- [minor] README:10's source comment is mislocated.
- [minor] The CC BY 4.0 attribution text omits what N12-licenses' action column asks for, and drops one '[to confirm]'.
- [minor] The map's column header says 'Figure as the note carries it', but every figure is the block's quotation; the note was not read.
- [minor] The file is not short, and the workflow pointer is longer than the block allows.
- [minor] Nit: README:210 says the readability AUC 0.759 and the judge figure 14/32 were 'computed on these' (g2r and g2r2). N4's paragraph pins the verdict's figures to g2r2's corpus.

### Recheck: findings 12 (2 substantive); redaction clean: True
- [substantive] The list of audit parts that read inputs a clone does not have (README-NOTE.md:74-78) leaves out the untracked PREPRINT-v1_0-draft.md, which most audit scripts read from the working tree. N4, N5, N6, N7 and N8 open it with no existence guard, so they fail with ...
- [substantive] The N1 ledger that README §4 and §8 cite was overwritten in the working tree while this check ran. The README's ledger figures, its 14 or so ledger line locators, the map's coverage and the tag-commit candidates are now stale. The cited version (sha256 95b07010…e72f) no ...
- [minor] The per-row Status column in the provenance table drops N13's 'NO SHA256 RECORDED' for rows 1-24, including row 16 ('no governed data' only). A reader scanning the table sees 'order holds' throughout.
- [minor] The map row for the shuffle-95 null (ledger L053) drops the item raw's CONDITIONAL qualifier, so the status is not carried exactly.
- [minor] The map row 'Δ+ +0.285, Δ− −0.395, random ≤ 0.088, LOO Δ+ 0.085, 9/12 and 10/12' lists ledger rows 'L129–L134'. That range includes L131 (bars ±0.158), which belongs to the next row, so L131 is mapped twice.
- [minor] The tightened cached-generation clauses lose some detail. The T-step check's domain (e2d-format rounds run through the ported adapter) is dropped. The 22/24 result at dose 0.2 is placed under data/e2d/tstep_check_f010.json, but it comes from data/e2d/tstep_check.json. And ...
- [minor] The floor-1 clause turns N17's statement about a rule into a statement about what ran ('so greedy readouts under high-norm steering ran uncached').
- [minor] README says 'the record declares no Qwen revision'. Other item raws show that the record's log names c000ac2c as the single local snapshot (log-only), so the bare statement overstates the absence.
- [minor] In §4, the 'design-seat claim or figure label' (NF) and 'stale referent' (SR) bullets give N1's own reading of block :23 with no [design seat]/[PI] marker. The N3 reading in the bullet before them is marked.
- [minor] The list of audit parts that read inputs a clone does not have marks only N10 as reading a local-only file inside the clone. N9 also reads local-only files there.
- [minor] The README-NOTE does not carry an N11 note that was addressed to its writer: README.md's status heading is dated 2026-08-20.
- [minor] The e2b map row calls 0.0833 the 'sham envelope'. The envelope of record is the maximum over the sham and random arms, and 0.0833 happens to come from sham.

### Round 2 check: findings 7 (0 substantive); redaction clean: True
- [minor] The new PREPRINT bullet (README-NOTE.md:77) puts N17 in the wrong group. It lists N17 with N2, N9, N10 and N14, which 'also read it', as opposed to N4–N8, which 'open it with no existence check'. In fact N17 opens the preprint with no check, so N17 also fails from a clone ...
- [minor] The PI marker on :77 offers a choice: commit the preprint, or accept that those five scripts run only on the laptop. That implies committing the preprint lets them run from a clone. It does not for N4 and N5 (or N17): they also open files in the gitignored jlens-qwen36/ clone ...
- [minor] The list of audit parts that read inputs a clone does not have (:76-81) still leaves out N13, which reads untracked drafts from the working tree. It also leaves out N4's reads of untracked HANDOFF design files. The checker's optional part of finding 1 named both. The fixer ...
- [minor] The 'not found' bullet (:87) states the cut conditions for L071 and L074 with no marker. The ledger labels those conditions as Code's reading of :23, not the item raw's. The NF and SR bullets carry '[design seat: Code's reading of :23.]', so this bullet is inconsistent with ...
- [minor] The provenance statement in the header (:4) is now incomplete. It says every figure and claim comes from an audit raw, the N1 ledger, the block or the record. The new bullet at :77 rests on the audit scripts' source lines, and :21 cites the N13 script.
- [minor] §8 lists what a tag on 7742e2c or 87a1167 would lack: this file, the audit raws, and the record lines at their pinned line numbers. The list leaves out PROPOSAL-m-gating-campaign-v1_11.md, which this README lists as a pre-registration of record (§2 row 25, §5). That file is ...
- [minor] README:86 says 29 passing rows carry a wording correction an item raw routes to the note. It drops the ledger's caveat that 4g, the source of that count, is Code's collection and 'not asserted exhaustive'. As written, 29 reads as a complete count.

## Code's round-3 edits (after the round-2 checks; no further agent check)

- **N1:** the round-2 check's one substantive finding was that README-NOTE.md was stale against the round-3 ledger. That check ran before the README was rebuilt. The rebuild came after it, against ledger sha256 02b48e6c...c3ee, and the README check confirmed it (all 12 of its findings applied; ledger figures, map coverage L001-L166 and the tag-commit branches match). So the finding is resolved. N1's 5 minor round-2 findings are **open (minor, not applied)**.
- **N12 scrub index:** the substantive finding is fixed by Code. The re-run warning now describes each part script's actual output behaviour, read from asserted guard lines: licenses overwrites by default; content refuses to overwrite; history accepts only its own two basenames under results/raw/. Two minor findings are fixed: the section-9 attribution qualifier, with the option-(b) inference labelled as the index's note, and the section-7 sentence branch. The open minor is finding 9 (the README should name the stored probe vectors), and README-NOTE.md:14 already does. The script was regenerated with 24/24 cross-checks agreeing and the leak guard clean.
- **README-NOTE.md:** five minor findings are fixed by Code:
  - N17 is moved to the unguarded-preprint group;
  - the PI marker now says committing the preprint suffices only for N6-N8, while N4, N5 and N17 also need the jlens clone;
  - N4's and N13's guarded reads of untracked root files are added;
  - the not-found conditions are marked as Code's reading;
  - the 4g count carries its not-exhaustive caveat.
  The section-8 list now includes PROPOSAL-m v1.11 (first committed at 05c4636), and the header's provenance sentence names the audit scripts' source lines. The remaining minor findings are **open (minor, not applied)**.
- A redaction check over the six integration files found 0 verbatim values.
