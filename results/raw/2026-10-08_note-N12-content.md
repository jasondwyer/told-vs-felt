# N12(vi) content review: results/raw and HANDOFF over full history (AUDIT-note-release v1.2)

- Code stamp (`date -u`): Thu Oct  8 04:05:57 UTC 2026
- HEAD: `bbc9ffe72fb8a942431c9bf2622a36e581fdf93c` (same as origin/main; HEAD had not moved at this stamp)
- Block: `AUDIT-note-release-v1_2.md`, sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841`, 141 lines; matches at HEAD. Item N12(vi) is block :82, inside N12 at :72-85.
- Mechanical screen: script `scripts/audit_note_N12_content.py`, sha256 `98a126aa14d137c027d65bf908bdccab83627c82b414e79f2ca60a501248411a`. Its output is `results/raw/2026-10-08_note-N12-content-screen.json`, sha256 `892fa8e8e556166d34454f9cf57e1ea4a1a0690ee29061da9d078199c6cf29ac`, stamped 2026-10-08T03:21:53Z at rev bbc9ffe. The screen's author reports a PASS on its synthetic-fixture self-test with 0 values leaked; this writer did not re-run the self-test.
- Part: N12-content, the aggregation. This file was written directly from the screen JSON, the 13 reviewer records and the refuter's verdicts. No new repository script was written. Helper snippets live in the session scratchpad (`scratchpad/N12-content/`) and are not committed.
- Redaction (hard rule 4): each candidate value is written as its first 4 characters + `...` + length + `:` + the first 8 hex of its sha256. Reviewer forms such as `...len14+sha256:` and `...14...` follow the same scheme. Port numbers are given as length + sha8 only, because the first four characters of a 5-digit port disclose it. The only values written in full are absolute paths under the author's username, which the rule allows.

## 0. Result and pass line for N12(vi)

**Expected: nothing; found: nothing in the three classes N12(vi) names. No third-party personal data, no pasted private correspondence, and no material the PI marked confidential is present in any reviewed object. Carried to the PI from the same review:**
- **One group of RunPod account-resource identifiers:** the pod id, the network-volume id and the volume's display name. They are not credentials. They sit in 8 tracked HANDOFFs, 5 tracked raws and 4 commit messages.
- **A LoRA training phrase labelled "secret ... code word",** to compare against the continuity password.

**File count reviewed: 267** (259 results/raw + 8 HANDOFF-*.md at HEAD). The review also covered 44 earlier versions of 14 of those paths, 4 history-only versions, 304 commit messages and 1 tag annotation.

Decisions for the PI. None of them is an N12(i) credential STOP from this part.

- **D1 (one decision, §4 + §5.1). RunPod pod id `uimu...14:a39ed293`, network-volume id `o73q...10:e79618f8` and volume display name `holy...23:e6c48186`.**
  - Spread: 13 carriers in N12(vi) scope; at HEAD the ids are also in RESULTS.md and in a test fixture at `valence_core/m/resume.py:1132,1135`. Commits (`git log -S --all`): 13 for the pod id, 14 for the volume id, 1 for the name. Commit messages: 4.
  - Status: the record calls the pod "stopped, parked, not terminated" (HANDOFF-2026-09-12.md:362-363), and RESULTS.md:8381 carries `EXITED`.
  - Options:
    - (a) Accept publication. Optionally terminate the pod and decide the volume's fate so that the ids are inert.
    - (b) Redact at HEAD. This removes nothing from history.
    - (c) Rewrite history. That is the PI's call (block §7).
- **D2 (§5.2). The LoRA overfit phrase at `results/raw/2026-08-05_lora_feasibility_spike.txt:16`, `zebr...20:c63d5fbd`** (with its trailing period: `zebr...21:7c04c313`).
  - The PI compares it with the continuity password out of band (N12(iii)).
  - A match means the password is already in history (2 files at HEAD, 2 commits).
- **D3 (§5.3). Commit metadata.**
  - 4 commits carry `.local` e-mail addresses.
  - 7 commits carry one claude.ai session URL in a trailer.
  - Those same 7 commits carry SSH signatures that embed a public key.
  - Low sensitivity. Only a history rewrite changes these; `.mailmap` changes the display only.
- **D4 (§5.4). Release staging.** Seven design-seat documents are untracked and not gitignored, and so are 16 other root/archive files (§7). Two of the design documents carry not-for-the-repo headers. Neither is in any commit. Of those two documents, one 120-character window appears in committed text (RESULTS.md); the history reviewer judged it research text quoted by design, and this writer did not read it. The release commit must stage by explicit path.

## 1. Inputs, and how this writer obtained them

- **The computed task text that handed the inputs to this writer was cut off** in three places: the screen summary (inside its "names" result), the reviewer records (inside chunk 4's 25th file entry) and the refuter's summary (near its end).
  - The workflow stores every agent's structured result in its local run journal, `~/.claude/projects/<project>/<session>/subagents/workflows/<run>/journal.jsonl`. That file is not in the repo.
  - This writer read the 16 results there, read-only: the screen, 12 chunk reviewers, the history reviewer, the refuter, and one other N12 part (N12-licenses), which this file does not use.
  - Every count below comes from those complete records. They agree with the delivered portions wherever both were read.
- **The refuter's own input was also truncated.**
  - It received 40 of the 59 reviewer flags and returned 39 verdict entries: 12 survive, 27 are refuted.
  - Its summary says "Of the 40 ... 12 hold up and 28 do not". The 40th flag it saw, chunk 10's time-zone flag (flag 39 in §5's numbering), has no verdict entry.
  - Flags 41-59 never reached it: chunk 11's 7 flags and the history reviewer's 12.
  - So **20 flags have no adversarial verdict.** §5 reports them separately, with this writer's own disposition and the tool runs behind it. None of them is described as having survived refutation.
- **Flag numbering in this file** runs in reviewer order (chunk 0 → chunk 11 → history), 1-59. Verdict *k* of the refuter's list answers flag *k* for k = 1-38. Its verdict 39 answers flag 40.

## 2. Method

### 2.1 Mechanical screen (`scripts/audit_note_N12_content.py`; values from its JSON)

**Scope**
- 576 objects, 14,185,962 bytes, read from git objects (`git cat-file --batch`) at bbc9ffe. The working tree was not read.
- Refs: main and origin/main (bbc9ffe), origin/claude/handoff-doc-next-steps-oeccd1 (79868f7), cycle-2-close (lightweight, f597ea7) and cycle-4-close (annotated, unsigned).
- Objects:
  - 259 results/raw files at HEAD
  - 8 HANDOFF-*.md at HEAD
  - 304 commit messages (`rev-list --all`)
  - 1 tag message
  - 4 history-only versions: `HELD-e2d-closure-entry.md` @cef728f^1 (the only path the block's own `--diff-filter=D` command returns), plus three from `--no-renames`: `results/raw/2026-08-21_h1_sessions.txt` and `data/e2b/h1_sessions.json` @d94e281^1, and `valence_core/e2b/session.py` @1465b34^1.
- The six untracked `HANDOFF-*-design.md` were listed by name and not read.

| category | hits | objects | disposition (screen, checked by the reviewers) |
|---|---|---|---|
| e-mail, not allowlisted | 0 | 0 | Allowlisted addresses are counted apart: Anthropic noreply 252, all in Co-Authored-By trailers. The author's own address appears 0 times in content. |
| phone shapes | 2 | 2 | Both are signed decimals: `+0.3...12:a107d9fe` at `results/raw/2026-09-07_e2d_closure_glosscheck5.txt:92` and `+0.1...13:24267248` in commit 1bdf16c msg l.5. False positives because each is `+0.<digits>`. |
| street-address shapes | 0 | 0 | |
| IPv4 | 1 | 1 | Loopback with port 8765 at `results/raw/2026-07-16_sanity_check.md:4` (`127....9:12ca17b4`), a local web UI. |
| URLs | 11 | 9 | Three hosts. claude.ai ×7: Claude-Session trailers (§5.3). github.com ×3: the repo's own URL, `results/raw/2026-10-04_m-v1.7_referent_check.txt:8482, 8489, 8498`. Loopback ×1. |
| confidentiality words | 117 | 32 | `private` 103: 100 are `/private/...` paths. The other 3 describe the repo as private and go stale on release: HANDOFF-2026-08-24.md:137, 737820a msg l.37 and 5bc4c31 msg l.1. `embargo` 9: PROPOSAL-m's "Step 4 embargo" design term. `do not share` 4: "do not share a sign". `off the record` 1: `results/raw/2026-10-05_m-v1.9_referent_check.txt:8640`, meaning "not committed". confidential / NDA / internal only / not for publication: 0 each. |
| correspondence markers | 18 | 4 | `Subject:` ×5 at HEAD: `results/raw/2026-08-21_h2_sweep.txt:132` is model output for an e-mail-subject task, and 4 lines in two values-check raws describe it. In history-only `data/e2b/h1_sessions.json`: `Hi ` ×10 and `Subject:` ×3, all inside model transcripts directly after `Response:`. |
| personal-life markers | 206 | 48 | All technical word forms: diagnostic 98, banked 63, diagnosis 19, and others. 0 for wife/husband/partner/kid, doctor, hospital and salary. |
| credential shapes | 29 | 9 | 0 key-format hits (armor, AWS, sk-, rp_/rpa_, hf_, GitHub, Slack, Google, JWT, ssh key, fingerprint, URL userinfo, Bearer, keyword=value). 2 generic high-entropy values. `tknb...30:4020fe83` ×22: a macOS per-user temp-directory component in `results/raw/2026-10-06_m-build_selftest.txt` and `results/raw/2026-10-07_m-dispositions_selftest.txt` (refuted class, §6 R17). `016w...24:1178033a` ×7: the session id inside the Claude-Session trailer URL (§5.3). |
| infrastructure ids (supplementary patterns) | 4 | 4 | `~/.ssh/config` ×2 (HANDOFF-2026-08-20.md:172, HANDOFF-2026-08-24.md:141): the standard OpenSSH file name. A 22-character `~/.ssh/` backup file name in 737820a msg l.42 (`conf...22:5c862486`). `RUNPOD_POD_ID=` followed by a 4-character synthetic test value (`po...4:7323177b`) at `results/raw/2026-10-06_m-build_valuescheck_pass2.txt:409`. |
| names (heuristic) | tier_a 1,050; tier_b 0 | | Counts only. The "et al" allowlist found Chandaria, Chua, Krishnamurthy, Macar and Tagliabue. |
| commit/tag identities | 304 commits, 1 tagger | | §5.3 |

**Limitation, observed from the pattern text and the line shapes.** The screen's labelled-id pattern needs the literal word `id` (as in `pod id` or `volume id`). Its generic high-entropy pattern needs 24 or more characters. The record writes the RunPod ids as ``Pod `<14 chars>` `` and ``volume `<10 chars>` ``, so neither pattern can match them. The real identifiers in §4 were found by the content reviewers, not by the screen. The screen's line "0 RunPod proxy hosts, ssh users or labelled ids" is correct for its patterns, but it does not mean no pod id is present.

### 2.2 Content reviewers

- **Assignment.** 12 chunk reviewers (N12-review-0 to -11) were given 266 of the 267 HEAD files: 258 raws and 8 HANDOFFs.
  - Chunks 2-11 hold about 1.03 MB each.
  - Chunks 0 and 1 each hold one file over 1 MB.
- **Screening.** Each reviewer ran its own case-insensitive regex screen over every line of every assigned file. The categories were:
  - emails, phones, IPv4/IPv6, URLs
  - confidentiality words, correspondence markers
  - credential shapes and words (including "continuity")
  - SSH and infrastructure terms, id-shaped tokens
  - personal-life words, names and titles, time zones, user paths
  - hidden characters
- **History.** Wherever a path has more than one blob in history, the reviewer also screened every historical blob, and diffed and read it (§2.4).
- **Reading.**
  - Files up to 150 KB were read in full.
  - Larger files were read in full or "screened+sampled". A sampled read covered at least the first 400 lines, the last 200, a ±30-line window around every screen hit, and 10 or more evenly spaced 100-line samples.
  - Result: **258 files read in full** (7,455,407 bytes) and **8 screened+sampled** (5,076,447 bytes). The unread lines of the 8 sampled files are covered only by the regex screens. Each of those reviewers read a window around every screen hit it had not first cleared as a stated false-positive class, such as tokenizer-vocabulary "token".
- **History reviewer** (N12-review-history):
  - all 304 commit messages, read end to end in 15 chunks and pattern-screened. `rev-list --all` equals `rev-list main` (304), with no merges, notes, stash or replace refs.
  - both tags
  - the 3 history-only files, read in full
  - the HEAD orientation documents (CLAUDE.md, README.md, the 8 HANDOFFs), read in full
  - the 5 FINDINGS files, screened+sampled
  - a counts-only verbatim-overlap leak check of the 7 untracked design documents against all committed text (§5.4)

### 2.3 The 267th HEAD file

`results/raw/2026-10-08_note-preflight.md` was committed at bbc9ffe, after the chunks were cut, so no reviewer was assigned it. **This writer read it in full** (238 lines, 16,026 bytes; working tree identical to HEAD). It contains:
- the preflight referent inventory (paths and sha256s)
- an interpreter path under `/Users/jasondwyer/` (allowed)
- at :218-219, the names of two local conda environments on the author's laptop (the same class as refuted R12 and R24)
- Code's numbered notes

Nothing in it needs flagging.

### 2.4 Earlier versions of reviewed paths

`git log --all --no-renames --raw -- 'results/raw/*' 'HANDOFF-*.md'` yields **312 distinct (path, blob) pairs**:
- 267 at HEAD
- 1 history-only path: `results/raw/2026-08-21_h1_sessions.txt`, renamed without change to `..._h1u_sessions.txt` at d94e281; its blob equals the HEAD file (chunk 8)
- 44 earlier blobs of 14 paths

Each of the 14 paths is named as covered in its reviewer's record:

| path | blobs in history | covered by |
|---|---|---|
| HANDOFF-2026-08-20.md | 16 | chunk 5 (every blob screened, every history-only line read) |
| HANDOFF-2026-08-22.md | 2 | chunk 9 (dfac7f2, 6dfc455; the second adds only a header line) |
| HANDOFF-2026-08-24.md | 5 | chunk 4 (all screened; 6dfc455 read in full, later versions read as diffs) |
| HANDOFF-2026-08-25.md | 7 | chunk 11 |
| HANDOFF-2026-09-01.md | 7 | chunk 5 |
| HANDOFF-2026-09-05.md | 3 | chunk 11 |
| HANDOFF-2026-09-06.md | 2 | chunk 6 (58be254) |
| HANDOFF-2026-09-12.md | 2 | chunk 10 |
| results/raw/2026-08-09_e2a_full.txt | 3 | chunk 8 (plus 2 predecessor files linked by `--follow`) |
| results/raw/2026-08-12_rule26_oracle.txt | 2 | chunk 10 |
| results/raw/2026-08-22_lockh_v2_valuescheck.txt | 2 | chunk 6 (e94e6aa) |
| results/raw/2026-09-02_e2d_d2.txt | 2 | chunk 6 (a9e6a74) |
| results/raw/2026-09-05_e2d_closure_verify.txt | 2 | chunk 4 (edf2574) |
| results/raw/2026-09-06_format_recon_selftest.txt | 3 | chunk 10 |

The fourth history-only version the screen covered, `data/e2b/h1_sessions.json` @d94e281^1, was **screened mechanically only**. No reviewer read it, and it lies outside N12(vi)'s results/raw + HANDOFF scope.

### 2.5 Refuter

- A single strict pass over each flagged locator.
- It re-ran the spread counts itself (`git grep -F`, `git log -S --all`, `git log --all -F --grep`) without printing values.
- It also ran a full-history (`git log -p --all`) screen for routable IPv4 addresses, ssh user@host, RunPod proxy and ssh hosts, IdentityFile entries and key fingerprints. It found none: the only dotted quads are the loopback address (`127....9:12ca17b4`) and a section number in generated model text.
- Its input was truncated as described in §1.

### 2.6 This writer's own runs (read-only; values never printed)

1. **Pod and volume ids.** Read from bphase_respawn.txt:1 and HANDOFF-2026-08-20.md:120. Pod: 12 tracked files at HEAD, 13 commits (`-S --all`), 2 commit messages (737820a, f90aa2d). Volume: 11 files, 14 commits, 4 messages (341c94e, 591fbdd, 737820a, f90aa2d). Both appear on HANDOFF-2026-08-24.md:159, -08-25.md:186, -09-05.md:218 and -09-12.md:362.
2. **Volume display name.** Taken from podprep.txt:6. It is in 2 files at HEAD (RESULTS.md and podprep.txt), 1 commit and 1 message (591fbdd).
3. **Commit identities and offsets** (`git log --all`, author and committer):
   - Jason Dwyer with the author's own address: 293.
   - Claude with Anthropic noreply: 7.
   - Claude Cowork with `clau...30:ab2650f2`: 2.
   - Jason Dwyer with `jaso...37:e1489bcc`: 2.
   - Offsets: -0400 on 297 commits, +0000 on 7 (identical for author and committer dates).
   - `.local` domains: 4 commits.
4. **Claude-Session trailers.** 7 commits carry them (0dd6f56, 5361b8b, 6897b67, 79868f7, d4f21d1, e1b5c77, f9e5d89), all with 1 distinct URL (`http...55:6dff6f86`).
5. **Design documents.** Each of the 7 untracked design documents has 0 commits on `--all`, and none is gitignored (`git check-ignore`). The history reviewer's overlap helper, re-run, reproduces its window counts (§5.4).
6. **LoRA fixture.** The redacted forms match the reviewer's. The value is in 2 files at HEAD (the raw, and `archive/RESULTS-cycle1-2.md`) and in 2 commits (c54c4e0, 3fb4b99). The raw's context is a 40-step overfit loss curve followed by a "learned the string" check.
7. **Commit 5e0ffca msg l.64,** read with ids masked. It cites a public Hugging Face SAE repository as owner/repo.
8. **Pod fixture and pod state.** HANDOFF-2026-09-12.md:362-363 reads "stopped, parked, not terminated". The `valence_core/m/resume.py:1132,1135` fixture literal hashes to `uimu...14:a39ed293`. RESULTS.md:8381 contains `EXITED`.
9. **History versions.** The 312-pair count in §2.4.
10. **Preflight raw.** The read in §2.3.

## 3. Files reviewed, by chunk

Bytes are git-object sizes taken from the screen JSON. Every reviewer-reported size matches them: 0 mismatches over 266 files. The table was formatted mechanically from the reviewers' structured records. "Versions in history" counts the distinct blobs at that path over `--all` (§2.4).

**Chunk 0 (N12-review-0): 1 file, 1,174,466 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `results/raw/2026-10-06_m-v1.11_referent_check.txt` | 1,174,466 | screened+sampled | 1 | 6,880 of 19,209 lines read (35.8%) |

**Chunk 1 (N12-review-1): 1 file, 1,086,527 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `results/raw/2026-10-05_m-v1.10_referent_check.txt` | 1,086,527 | read-in-full | 1 |  |

**Chunk 2 (N12-review-2): 18 files, 1,026,990 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `results/raw/2026-07-18_phase1_rating_gradient.txt` | 3,413 | read-in-full | 1 |  |
| 2 | `results/raw/2026-07-18_phase1_tier1_calibration.txt` | 1,965 | read-in-full | 1 |  |
| 3 | `results/raw/2026-07-18_phase1_tier23_calibration.txt` | 1,649 | read-in-full | 1 |  |
| 4 | `results/raw/2026-07-18_phase1_tier2_singlelayer_diag.txt` | 1,159 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-02_strain_dose_response.txt` | 4,282 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-03_strain_direction_frac_sweep.txt` | 3,482 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-04_slice2_primary_tost_refined.txt` | 2,944 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-06_c1r2_full_run.txt` | 5,599 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-09_e2a_g1r.txt` | 427 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-09_e2a_smoke2.txt` | 1,932 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-10_d_gates_A.txt` | 821 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-12_rule26_b2b_tightened.txt` | 7,889 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-19_rl_survey_base.txt` | 987 | read-in-full | 1 |  |
| 14 | `results/raw/2026-08-23_respawn_determinism.txt` | 3,098 | read-in-full | 1 |  |
| 15 | `results/raw/2026-09-04_e2d_d2_allrounds_rescore.txt` | 2,747 | read-in-full | 1 |  |
| 16 | `results/raw/2026-09-06_e2d_contentclass_screen_v4rev2pre.txt` | 1,802 | read-in-full | 1 |  |
| 17 | `results/raw/2026-09-09_k1_analyze_selftest_v11.txt` | 2,240 | read-in-full | 1 |  |
| 18 | `results/raw/2026-10-05_m-v1.9_referent_check.txt` | 980,554 | screened+sampled | 1 | 5,850 of 16,316 lines read (35.9%) |

**Chunk 3 (N12-review-3): 18 files, 1,027,043 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `results/raw/2026-08-02_strain_reexamination.txt` | 2,594 | read-in-full | 1 |  |
| 2 | `results/raw/2026-08-04_slice3_dv_smoke.txt` | 2,027 | read-in-full | 1 |  |
| 3 | `results/raw/2026-08-08_e0_b2c_smoke.txt` | 822 | read-in-full | 1 |  |
| 4 | `results/raw/2026-08-08_e0_smoke.txt` | 3,752 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-09_e2a_analysis.txt` | 1,689 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-10_d_layermap.txt` | 489 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-10_f_analysis.txt` | 1,905 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-10_f_postscreen_descriptive.txt` | 1,103 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-19_smoke_dpo.txt` | 2,271 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-20_lockh_verify_nd200.txt` | 3,074 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-20_s1_judge_rescue.txt` | 994 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-24_bphase_respawn.txt` | 4,286 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-24_cached_gate.txt` | 8,751 | read-in-full | 1 |  |
| 14 | `results/raw/2026-09-02_e2d_d2_scoring.txt` | 2,846 | read-in-full | 1 |  |
| 15 | `results/raw/2026-09-03_e2d_d3.txt` | 3,396 | read-in-full | 1 |  |
| 16 | `results/raw/2026-09-05_recon_echo_stageA_analysis.txt` | 5,827 | read-in-full | 1 |  |
| 17 | `results/raw/2026-10-04_m-v1.8_referent_check.txt` | 979,423 | screened+sampled | 1 | 4,827 of 15,460 lines read (31.2%) |
| 18 | `results/raw/2026-10-07_m-gport.txt` | 1,794 | read-in-full | 1 |  |

**Chunk 4 (N12-review-4): 26 files, 1,026,995 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `HANDOFF-2026-08-24.md` | 9,970 | read-in-full | 5 |  |
| 2 | `results/raw/2026-07-16_four_experiments_n20lens.txt` | 2,163 | read-in-full | 1 |  |
| 3 | `results/raw/2026-07-18_phase1_tier2_v2_subspace_ablation.txt` | 1,551 | read-in-full | 1 |  |
| 4 | `results/raw/2026-08-03_slice1_config_profile.txt` | 1,871 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-04_slice1b_accuracy_screen.txt` | 3,096 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-09_e2a_g1.txt` | 435 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-10_d_gates_B.txt` | 822 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-10_f_calib.txt` | 957 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-10_f_ndecl.txt` | 1,728 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-21_h2_sessions.txt` | 4,528 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-23_a1_tagscreen.txt` | 13,078 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-24_b3.txt` | 6,254 | read-in-full | 1 |  |
| 13 | `results/raw/2026-09-01_e2a_recount.txt` | 2,486 | read-in-full | 1 |  |
| 14 | `results/raw/2026-09-02_e2d_tstep_f010.txt` | 2,319 | read-in-full | 1 |  |
| 15 | `results/raw/2026-09-03_e2d_d3_scoring.txt` | 3,411 | read-in-full | 1 |  |
| 16 | `results/raw/2026-09-05_e2d_closure_verify.txt` | 16,333 | read-in-full | 2 |  |
| 17 | `results/raw/2026-09-05_recon_echo_stageA_posthoc2.txt` | 1,274 | read-in-full | 1 |  |
| 18 | `results/raw/2026-09-06_format_recon_entry_valuescheck.txt` | 27,082 | read-in-full | 1 |  |
| 19 | `results/raw/2026-09-06_format_recon_run.log` | 7,994 | read-in-full | 1 |  |
| 20 | `results/raw/2026-09-07_format_recon_analyze.txt` | 3,650 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-09_k1_stage1_selftest.txt` | 2,921 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-09_k_commit_regression.txt` | 22,424 | read-in-full | 1 |  |
| 23 | `results/raw/2026-09-11_addendum_k1_stop_entry_valuescheck.txt` | 52,426 | read-in-full | 1 |  |
| 24 | `results/raw/2026-10-04_m-v1.6_STOP4_recovered.md` | 34,579 | read-in-full | 1 |  |
| 25 | `results/raw/2026-10-04_m-v1.7_referent_check.txt` | 714,858 | screened+sampled | 1 | 4,334 of 10,449 lines read (41.5%) |
| 26 | `results/raw/2026-10-06_m-build_valuescheck_pass2.txt` | 88,785 | read-in-full | 1 |  |

**Chunk 5 (N12-review-5): 28 files, 1,027,039 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `HANDOFF-2026-08-20.md` | 15,542 | read-in-full | 16 |  |
| 2 | `HANDOFF-2026-09-01.md` | 17,706 | read-in-full | 7 |  |
| 3 | `results/raw/2026-07-16_four_experiments_n1000lens.txt` | 2,327 | read-in-full | 1 |  |
| 4 | `results/raw/2026-08-03_strain_diversity_recheck.txt` | 2,806 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-04_slice2_primary_tost.txt` | 3,026 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-06_c1_smoke.txt` | 4,626 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-08_e0_b2c_a.txt` | 2,209 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-09_e2a_g2r2.txt` | 737 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-10_d_cache.txt` | 513 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-10_f_smoke2r.txt` | 953 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-18_window_coverage_audit.txt` | 1,718 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-19_scaffold_sft.txt` | 1,847 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-20_h1_power_flipgate.txt` | 4,831 | read-in-full | 1 |  |
| 14 | `results/raw/2026-08-21_h2_smoke_cached.txt` | 1,539 | read-in-full | 1 |  |
| 15 | `results/raw/2026-08-21_h2_sweep.txt` | 10,552 | read-in-full | 1 |  |
| 16 | `results/raw/2026-08-24_b2.txt` | 9,605 | read-in-full | 1 |  |
| 17 | `results/raw/2026-08-24_respawn_determinism.txt` | 3,249 | read-in-full | 1 |  |
| 18 | `results/raw/2026-08-25_b2r_analysis.txt` | 2,467 | read-in-full | 1 |  |
| 19 | `results/raw/2026-09-05_recon_site_assertion.txt` | 22,453 | read-in-full | 1 |  |
| 20 | `results/raw/2026-09-06_e2d_closure_glosscheck3.txt` | 40,207 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-07_format_recon_entry_valuescheck.txt` | 31,796 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-08_e2d_closure_verify3_at_HEAD.txt` | 4,090 | read-in-full | 1 |  |
| 23 | `results/raw/2026-09-17_e2d_contentclass_screen_v5_adopted.txt` | 7,241 | read-in-full | 1 |  |
| 24 | `results/raw/2026-09-17_v5_adoption_entry_valuescheck.txt` | 103,463 | read-in-full | 1 |  |
| 25 | `results/raw/2026-09-17_v5_adoption_sitecheck.txt` | 1,338 | read-in-full | 1 |  |
| 26 | `results/raw/2026-10-06_m-build_pins.txt` | 69,355 | read-in-full | 1 |  |
| 27 | `results/raw/2026-10-06_m-build_review.txt` | 498,533 | screened+sampled | 1 | 3,778 of 6,128 lines read (about 62%) |
| 28 | `results/raw/2026-10-06_m-v1.11_step3_valuescheck_pass2.txt` | 162,310 | read-in-full | 1 |  |

**Chunk 6 (N12-review-6): 28 files, 1,027,085 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `HANDOFF-2026-09-06.md` | 21,066 | read-in-full | 2 |  |
| 2 | `results/raw/2026-07-18_state_space_validation.txt` | 2,750 | read-in-full | 1 |  |
| 3 | `results/raw/2026-08-06_c1_full_run.txt` | 5,140 | read-in-full | 1 |  |
| 4 | `results/raw/2026-08-08_e0_b1_full.txt` | 2,259 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-08_e0_b2a_smoke.txt` | 738 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-09_e2a_g2r_crash.txt` | 1,768 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-09_e2a_ndecl.txt` | 1,394 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-09_e2a_smoke3.txt` | 2,096 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-10_f_run.txt` | 16,239 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-19_olmo_acquisition.txt` | 32,415 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-19_scaffold_base.txt` | 1,903 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-20_h3_tagscreen.txt` | 3,239 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-21_h1_gate_eval.txt` | 1,480 | read-in-full | 1 |  |
| 14 | `results/raw/2026-08-22_lockh_v2_valuescheck.txt` | 6,431 | read-in-full | 2 |  |
| 15 | `results/raw/2026-08-22_podprep.txt` | 4,225 | read-in-full | 1 |  |
| 16 | `results/raw/2026-09-02_e2d_d2.txt` | 4,567 | read-in-full | 2 |  |
| 17 | `results/raw/2026-09-03_e2d_excision.txt` | 2,585 | read-in-full | 1 |  |
| 18 | `results/raw/2026-09-05_recon_echo_stageB_analysis_samefolds.txt` | 12,597 | read-in-full | 1 |  |
| 19 | `results/raw/2026-09-06_dispositions_entry_valuescheck.txt` | 25,392 | read-in-full | 1 |  |
| 20 | `results/raw/2026-09-09_k1_stage1_run.log` | 9,434 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-12_handoff_sitecheck.txt` | 561 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-17_e2d_v5_exclusion_parity.txt` | 937 | read-in-full | 1 |  |
| 23 | `results/raw/2026-09-18_k1_stop_entry_valuescheck.txt` | 130,588 | read-in-full | 1 |  |
| 24 | `results/raw/2026-10-04_m-v1.8_code-to-design_STOP.md` | 49,884 | read-in-full | 1 |  |
| 25 | `results/raw/2026-10-05_m-v1.10_stop8_valuescheck.txt` | 166,238 | read-in-full | 1 |  |
| 26 | `results/raw/2026-10-07_m-dispositions-gport_valuescheck_pass2.txt` | 82,006 | read-in-full | 1 |  |
| 27 | `results/raw/2026-10-07_m-dispositions_sitecheck.txt` | 2,987 | read-in-full | 1 |  |
| 28 | `results/raw/2026-10-07_m-gport_differences.md` | 436,166 | read-in-full | 1 |  |

**Chunk 7 (N12-review-7): 29 files, 1,027,191 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `results/raw/2026-07-18_phase1_behavioral_influence.txt` | 4,689 | read-in-full | 1 |  |
| 2 | `results/raw/2026-08-03_strain_selection_screen.txt` | 6,378 | read-in-full | 1 |  |
| 3 | `results/raw/2026-08-05_slice3_dv_powered.txt` | 2,824 | read-in-full | 1 |  |
| 4 | `results/raw/2026-08-06_c1r3_full_run.txt` | 5,044 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-06_eval_awareness_validation.txt` | 1,437 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-09_e2a_g2r.txt` | 670 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-09_e2a_smoke.txt` | 912 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-10_d_train_B.txt` | 720 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-19_determinism_base.txt` | 3,261 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-19_smoke_base.txt` | 1,771 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-22_consolidation.txt` | 8,988 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-23_a2_rerun.txt` | 17,037 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-23_a4.txt` | 14,841 | read-in-full | 1 |  |
| 14 | `results/raw/2026-08-24_respawn_integrity.txt` | 2,230 | read-in-full | 1 |  |
| 15 | `results/raw/2026-09-02_e2d_tstep.txt` | 2,341 | read-in-full | 1 |  |
| 16 | `results/raw/2026-09-05_recon_echo_stageA.txt` | 2,432 | read-in-full | 1 |  |
| 17 | `results/raw/2026-09-05_recon_echo_stageA_posthoc.txt` | 1,477 | read-in-full | 1 |  |
| 18 | `results/raw/2026-09-06_e2d_contentclass_screen_v4.txt` | 1,802 | read-in-full | 1 |  |
| 19 | `results/raw/2026-09-06_format_recon_regression.txt` | 22,424 | read-in-full | 1 |  |
| 20 | `results/raw/2026-09-06_format_recon_time.txt` | 12,159 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-07_e2d_closure_verify3_strip.txt` | 4,090 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-09_k1_stage1_selftest_v11.txt` | 3,011 | read-in-full | 1 |  |
| 23 | `results/raw/2026-09-12_addendum-k1-v1.1_referent_check.txt` | 387,724 | screened+sampled | 1 | 26 line ranges read incl. every non-trivial hit window, first 400 and last 200 |
| 24 | `results/raw/2026-10-04_m-v1.6_STOP4_carryover_in_v1.7.txt` | 140,784 | read-in-full | 1 |  |
| 25 | `results/raw/2026-10-04_m-v1.8_stop6_valuescheck.txt` | 171,408 | screened+sampled | 1 | 15 line ranges read incl. every hit window |
| 26 | `results/raw/2026-10-06_m-build_design.md` | 34,999 | read-in-full | 1 |  |
| 27 | `results/raw/2026-10-06_m-build_selftest.txt` | 90,199 | read-in-full | 1 |  |
| 28 | `results/raw/2026-10-06_m-v1.11_code_own_pass.txt` | 27,285 | read-in-full | 1 |  |
| 29 | `results/raw/2026-10-06_m-v1.11_step3_notes.md` | 54,254 | read-in-full | 1 |  |

**Chunk 8 (N12-review-8): 30 files, 1,027,293 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `results/raw/2026-07-16_sanity_check.md` | 1,357 | read-in-full | 1 |  |
| 2 | `results/raw/2026-07-17_ablation_fix_rerun.txt` | 3,371 | read-in-full | 1 |  |
| 3 | `results/raw/2026-07-17_full_suite_with_verbal_report.txt` | 4,305 | read-in-full | 1 |  |
| 4 | `results/raw/2026-07-18_update_loop_validation.txt` | 5,473 | read-in-full | 1 |  |
| 5 | `results/raw/2026-07-19_forced_choice_probe.txt` | 2,117 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-04_slice2_primary_tost_powered.txt` | 3,027 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-08_e0_b2a_full.txt` | 2,426 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-09_e2a_full.txt` | 22,520 | read-in-full | 3 |  |
| 9 | `results/raw/2026-08-10_d_gates_A_smoke.txt` | 821 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-10_d_train_smoke.txt` | 307 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-10_f_calib2.txt` | 956 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-18_rule26_recheck_choiceread.txt` | 1,893 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-19_olmo_hashes.txt` | 2,830 | read-in-full | 1 |  |
| 14 | `results/raw/2026-08-19_scaffold_instruct.txt` | 1,762 | read-in-full | 1 |  |
| 15 | `results/raw/2026-08-20_h1_power_lockh_v1.txt` | 3,951 | read-in-full | 1 |  |
| 16 | `results/raw/2026-08-20_lockh_verify_v11.txt` | 2,371 | read-in-full | 1 |  |
| 17 | `results/raw/2026-08-21_h1u_sessions.txt` | 12,006 | read-in-full | 1 |  |
| 18 | `results/raw/2026-08-22_proposal_i_recon.txt` | 6,263 | read-in-full | 1 |  |
| 19 | `results/raw/2026-08-22_verdict_campaign.txt` | 14,305 | read-in-full | 1 |  |
| 20 | `results/raw/2026-08-22_verdict_smoke.txt` | 1,487 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-05_recon_echo_stageB.txt` | 8,970 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-06_e2d_closure_glosscheck4.txt` | 27,768 | read-in-full | 1 |  |
| 23 | `results/raw/2026-09-06_format_recon_checkgate.txt` | 395 | read-in-full | 1 |  |
| 24 | `results/raw/2026-09-06_format_recon_review.txt` | 36,901 | read-in-full | 1 |  |
| 25 | `results/raw/2026-09-09_k1_stage1_review.txt` | 93,323 | read-in-full | 1 |  |
| 26 | `results/raw/2026-09-09_k_referent_entry_valuescheck.txt` | 19,404 | read-in-full | 1 |  |
| 27 | `results/raw/2026-09-09_k_v11_appendixB_check.txt` | 350,675 | read-in-full | 1 |  |
| 28 | `results/raw/2026-10-05_m-v1.10_code-to-design_STOP.md` | 67,531 | read-in-full | 1 |  |
| 29 | `results/raw/2026-10-05_m-v1.9_stop7_valuescheck_pass2.txt` | 172,633 | read-in-full | 1 |  |
| 30 | `results/raw/2026-10-06_m-v1.11_step3_valuescheck.txt` | 156,145 | read-in-full | 1 |  |

**Chunk 9 (N12-review-9): 29 files, 1,027,000 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `HANDOFF-2026-08-22.md` | 9,090 | read-in-full | 2 |  |
| 2 | `results/raw/2026-07-17_calibrate_spider_ant.txt` | 2,914 | read-in-full | 1 |  |
| 3 | `results/raw/2026-08-03_strain_tail_survey.txt` | 3,386 | read-in-full | 1 |  |
| 4 | `results/raw/2026-08-04_slice2_gating_checks.txt` | 2,425 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-09_e2a_g3.txt` | 441 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-09_e2a_g3prime.txt` | 939 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-10_d_evoked_discrim.txt` | 784 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-19_rl_survey_dpo.txt` | 1,869 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-19_rl_survey_instruct.txt` | 1,638 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-19_smoke_instruct.txt` | 2,355 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-20_lockh_verify.txt` | 4,804 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-20_s2_extract_vignette.txt` | 1,247 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-21_h1_gate.txt` | 13,518 | read-in-full | 1 |  |
| 14 | `results/raw/2026-08-23_a1_repair.txt` | 19,231 | read-in-full | 1 |  |
| 15 | `results/raw/2026-09-01_e2d_d1.txt` | 2,194 | read-in-full | 1 |  |
| 16 | `results/raw/2026-09-05_recon_echo_stageB_analysis.txt` | 12,251 | read-in-full | 1 |  |
| 17 | `results/raw/2026-09-05_recon_echo_timing.txt` | 1,703 | read-in-full | 1 |  |
| 18 | `results/raw/2026-09-06_e2d_closure_verify3.txt` | 4,563 | read-in-full | 1 |  |
| 19 | `results/raw/2026-09-06_format_recon_run_refused-1613utc.log` | 3,047 | read-in-full | 1 |  |
| 20 | `results/raw/2026-09-08_e2d_contentclass_screen_v5.txt` | 7,010 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-09_k1_analyze_run.txt` | 3,791 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-09_k_launch_entry_valuescheck.txt` | 28,975 | read-in-full | 1 |  |
| 23 | `results/raw/2026-10-04_m-v1.7_stop_entry_valuescheck_pass2.txt` | 315,034 | read-in-full | 1 |  |
| 24 | `results/raw/2026-10-04_m-v1.8_stop6_valuescheck_pass2.txt` | 156,583 | read-in-full | 1 |  |
| 25 | `results/raw/2026-10-05_m-v1.10_code_own_pass.txt` | 23,374 | read-in-full | 1 |  |
| 26 | `results/raw/2026-10-05_m-v1.10_stop8_valuescheck_pass2.txt` | 193,363 | read-in-full | 1 |  |
| 27 | `results/raw/2026-10-07_m-dispositions-gport_valuescheck.txt` | 77,346 | read-in-full | 1 |  |
| 28 | `results/raw/2026-10-07_m-dispositions_check.txt` | 35,062 | read-in-full | 1 |  |
| 29 | `results/raw/2026-10-07_m-dispositions_selftest.txt` | 98,063 | read-in-full | 1 |  |

**Chunk 10 (N12-review-10): 29 files, 1,027,221 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `HANDOFF-2026-09-12.md` | 28,598 | read-in-full | 2 |  |
| 2 | `results/raw/2026-08-02_strain_frontier.txt` | 2,966 | read-in-full | 1 |  |
| 3 | `results/raw/2026-08-06_dv_logit_projection_check.txt` | 4,817 | read-in-full | 1 |  |
| 4 | `results/raw/2026-08-08_e0_b1_smoke.txt` | 710 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-08_e0_b2b_full.txt` | 4,069 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-08_e0_extract_full.txt` | 4,637 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-10_d_train_A.txt` | 721 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-10_f_smoke.txt` | 874 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-12_rule26_oracle.txt` | 3,352 | read-in-full | 2 |  |
| 10 | `results/raw/2026-08-19_cast_equality_sft.txt` | 15,889 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-19_scaffold_dpo.txt` | 1,826 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-19_smoke_sft.txt` | 2,492 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-21_h2_smoke_uncached.txt` | 1,465 | read-in-full | 1 |  |
| 14 | `results/raw/2026-08-22_aphase_harnesses.txt` | 10,125 | read-in-full | 1 |  |
| 15 | `results/raw/2026-08-22_verdict_analysis.txt` | 1,488 | read-in-full | 1 |  |
| 16 | `results/raw/2026-08-23_a3_a2.txt` | 23,595 | read-in-full | 1 |  |
| 17 | `results/raw/2026-08-23_respawn_integrity.txt` | 2,230 | read-in-full | 1 |  |
| 18 | `results/raw/2026-08-24_cached_gate_WITHDRAWN_v2.txt` | 1,743 | read-in-full | 1 |  |
| 19 | `results/raw/2026-08-25_b2r_arc.txt` | 17,723 | read-in-full | 1 |  |
| 20 | `results/raw/2026-09-04_e2d_closure_valuescheck.txt` | 2,288 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-06_format_recon_analyze_timing.txt` | 2,777 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-06_format_recon_selftest.txt` | 7,201 | read-in-full | 3 |  |
| 23 | `results/raw/2026-09-06_recon_echo_stageC_analysis.txt` | 9,856 | read-in-full | 1 |  |
| 24 | `results/raw/2026-09-11_k_stage1_entry_valuescheck.txt` | 194,210 | read-in-full | 1 |  |
| 25 | `results/raw/2026-09-12_handoff_valuescheck.txt` | 63,311 | read-in-full | 1 |  |
| 26 | `results/raw/2026-09-17_contentclass-v5-adoption_referent_check.txt` | 162,758 | read-in-full | 1 |  |
| 27 | `results/raw/2026-09-18_k1_stop_entry_valuescheck_pass2.txt` | 128,434 | read-in-full | 1 |  |
| 28 | `results/raw/2026-10-04_m-v1.7_code-to-design_STOP.md` | 39,081 | read-in-full | 1 |  |
| 29 | `results/raw/2026-10-04_m-v1.7_stop_entry_valuescheck.txt` | 287,985 | read-in-full | 1 |  |

**Chunk 11 (N12-review-11): 29 files, 1,027,004 bytes**

| # | file | bytes | method | versions in history | coverage (sampled files) |
|---|---|---|---|---|---|
| 1 | `HANDOFF-2026-08-25.md` | 12,765 | read-in-full | 7 |  |
| 2 | `HANDOFF-2026-09-05.md` | 15,965 | read-in-full | 3 |  |
| 3 | `results/raw/2026-07-16_debug_ablation.txt` | 3,428 | read-in-full | 1 |  |
| 4 | `results/raw/2026-07-19_basis_sensitivity_diagnostic.txt` | 4,759 | read-in-full | 1 |  |
| 5 | `results/raw/2026-08-05_lora_feasibility_spike.txt` | 971 | read-in-full | 1 |  |
| 6 | `results/raw/2026-08-09_e2a_g2.txt` | 1,139 | read-in-full | 1 |  |
| 7 | `results/raw/2026-08-09_e2a_g2check.txt` | 420 | read-in-full | 1 |  |
| 8 | `results/raw/2026-08-10_f_smoke2.txt` | 855 | read-in-full | 1 |  |
| 9 | `results/raw/2026-08-19_rl_survey_sft.txt` | 1,673 | read-in-full | 1 |  |
| 10 | `results/raw/2026-08-20_h3b_repair_screen.txt` | 3,194 | read-in-full | 1 |  |
| 11 | `results/raw/2026-08-20_s2_neighbor_axes.txt` | 4,523 | read-in-full | 1 |  |
| 12 | `results/raw/2026-08-21_h2_read_stability.txt` | 1,929 | read-in-full | 1 |  |
| 13 | `results/raw/2026-08-25_b2r_gates.txt` | 2,654 | read-in-full | 1 |  |
| 14 | `results/raw/2026-09-01_e2d_oracle_iv.txt` | 1,980 | read-in-full | 1 |  |
| 15 | `results/raw/2026-09-02_e2d_d2_analysis.txt` | 9,209 | read-in-full | 1 |  |
| 16 | `results/raw/2026-09-05_recon_echo_stageC.txt` | 20,276 | read-in-full | 1 |  |
| 17 | `results/raw/2026-09-06_e2d_contentclass_screen_v4pre.txt` | 1,802 | read-in-full | 1 |  |
| 18 | `results/raw/2026-09-07_e2d_closure_glosscheck5.txt` | 34,147 | read-in-full | 1 |  |
| 19 | `results/raw/2026-09-08_dispositions_valuescheck.txt` | 25,072 | read-in-full | 1 |  |
| 20 | `results/raw/2026-09-09_k1_analyze_selftest.txt` | 2,240 | read-in-full | 1 |  |
| 21 | `results/raw/2026-09-09_k_commit_format_recon_selftest.txt` | 7,201 | read-in-full | 1 |  |
| 22 | `results/raw/2026-09-09_k_v11_entry_valuescheck.txt` | 204,839 | read-in-full | 1 |  |
| 23 | `results/raw/2026-09-11_addendum_k1_referent_check.txt` | 221,826 | read-in-full | 1 |  |
| 24 | `results/raw/2026-09-17_v5_adoption_entry_valuescheck_pass2.txt` | 133,093 | read-in-full | 1 |  |
| 25 | `results/raw/2026-09-18_addendum-k1-1b_retention_geometry.txt` | 3,436 | read-in-full | 1 |  |
| 26 | `results/raw/2026-10-05_m-v1.9_code-to-design_STOP.md` | 47,568 | read-in-full | 1 |  |
| 27 | `results/raw/2026-10-05_m-v1.9_stop7_valuescheck.txt` | 169,481 | screened+sampled | 1 | 1,916 of 3,020 lines read (63.4%) + targeted marker scan of the rest |
| 28 | `results/raw/2026-10-06_m-build_sitecheck.txt` | 2,933 | read-in-full | 1 |  |
| 29 | `results/raw/2026-10-06_m-build_valuescheck.txt` | 87,626 | read-in-full | 1 |  |

**Not in any chunk; read in full by this writer (§2.3)**

| # | file | bytes | method | versions in history | coverage |
|---|---|---|---|---|---|
| 1 | `results/raw/2026-10-08_note-preflight.md` | 16,026 | read-in-full | 1 | |

**History reviewer (N12-review-history): objects that are not files at HEAD, and orientation documents**

| object | bytes | method |
|---|---|---|
| commit messages, all 304 reachable from `--all` (dumped with author/committer lines) | 456,467 | read in full + screened |
| tags: cycle-2-close (lightweight, f597ea7) and cycle-4-close (annotated; tagger is the author; unsigned) | n/a | read in full |
| `HELD-e2d-closure-entry.md` @cef728f^ (history-only) | 21,592 | read in full |
| `results/raw/2026-08-21_h1_sessions.txt` @d94e281^ (history-only path; blob equal to `..._h1u_sessions.txt`) | 12,006 | read in full |
| `valence_core/e2b/session.py` @1465b34^ (history-only path) | 10,418 | read in full |
| `data/e2b/h1_sessions.json` @d94e281^1 (history-only version) | n/a | screened mechanically only (§2.4) |
| CLAUDE.md, README.md (HEAD; outside N12(vi) scope) | 24,645; 3,290 | read in full |
| the 8 HANDOFF-*.md (HEAD; also in chunks 4, 5, 6, 9, 10, 11) | as above | read in full (second read) |
| FINDINGS.md, FINDINGS-2..5.md (HEAD; outside N12(vi) scope) | 10,900; 20,736; 16,474; 12,973; 12,472 | screened+sampled |
| the 7 untracked design documents | n/a | overlap leak check only, counts only (§5.4); not content-reviewed |

### 3.1 Totals

| unit | count | method |
|---|---|---|
| tracked `results/raw/*` at HEAD | 259 | 251 read in full (250 by chunk reviewers + the preflight by this writer); 8 screened+sampled |
| tracked `HANDOFF-*.md` at HEAD | 8 | 8 read in full (each twice) |
| **files at HEAD (N12(vi) scope)** | **267** | 259 read in full; 8 screened+sampled; 12,547,880 bytes |
| earlier blobs of those paths | 44 (14 paths) | screened; history-only lines read (§2.4) |
| history-only versions | 4 | 3 read in full; 1 screened only |
| commit messages | 304 | read in full + screened |
| tag annotations | 1 (cycle-4-close; cycle-2-close is lightweight) | read in full |

## 4. Flags that survived refutation

The refuter returned 12 verdicts that survive. They cover 11 distinct locators, because HANDOFF-2026-08-24.md:159 was flagged twice (by chunks 4 and 7). All of them fall under **one decision (D1)**.

Category for every row: infrastructure-identifier. These are RunPod account-resource ids, not credentials. Using them needs the account's API key or the SSH key. They are not an N12(i) STOP.

| # | locator (commit) | flag / verdict | what is there (redacted) | refuter's confirmation |
|---|---|---|---|---|
| S1 | `results/raw/2026-08-24_bphase_respawn.txt:1` (only commit 720a104) | F7 / V7 (chunk 3) | `### RESPAWN (i) INTEGRITY -- pod uimu...14:a39ed293 restarted 13:08 UTC, B-phase arc ###` | The full pod id of the Phase-2 box. HANDOFF-2026-09-12.md:362-363 records the resource as live ("stopped, parked, not terminated"), and RESULTS.md:8381 says EXITED, which is RunPod's word for stopped, not deleted. RunPod proxy hostnames are built from the pod id. The refuter re-ran the spread and it matches (table below). |
| S2 | `HANDOFF-2026-08-24.md:159` (HEAD blob, last changed at ad2139a; the same line in 6dfc455:115, c3dbf38:137, 97c3de5:148, f4b402a:154) | F9 / V9 (chunk 4); F23 / V23 (chunk 7, duplicate) | Pod `uimu...14:a39ed293`, GPU class, region, volume `o73q...10:e79618f8` | Confirmed: the live (parked) pod id plus the network-volume id at /workspace, which holds the checkpoints. Count correction: chunk 4 says 5 commit messages carry the volume id. `git log --all -F --grep` finds 4, and this writer's run agrees. |
| S3 | `HANDOFF-2026-08-20.md:120` (HEAD; all 16 historical blobs, 4aceb12 .. dfac7f2) | F12 / V12 (chunk 5) | Volume `o73q...10:e79618f8`, with the console pod spec at :116-120 | Confirmed in all 16 versions. |
| S4 | `HANDOFF-2026-09-01.md:232` (HEAD; all 7 blobs, b8566a6 .. 784a948) | F13 / V13 (chunk 5) | Pod `uimu...14:a39ed293` + volume `o73q...10:e79618f8` | Confirmed. |
| S5 | `HANDOFF-2026-09-06.md:264` (HEAD); 58be254:262 | F18 / V18 (chunk 6) | Pod + volume, GPU class, region | Confirmed in both versions. |
| S6 | `results/raw/2026-08-22_podprep.txt:6` (only commit 591fbdd) | F19 / V19 (chunk 6) | Volume `o73q...10:e79618f8` + RunPod's auto-generated volume name `holy...23:e6c48186`, size, region, tier | Confirmed. The name is in 2 files at HEAD, 1 commit and 1 commit message. Lines 7-11 hold public GPU pricing and empty schema field names, which are harmless. |
| S7 | `results/raw/2026-10-06_m-build_selftest.txt:329` (5f7b968) | F22 / V22 (chunk 7) | A self-test line printing the pod id `uimu...14:a39ed293` | Confirmed. The source is the hard-coded fixture at `valence_core/m/resume.py:1132` and `:1135` (tracked code; this writer's hash check matches), so every future self-test raw that prints this check will carry it. |
| S8 | `HANDOFF-2026-08-22.md:50` (dfac7f2, 6dfc455; HEAD) | F32 / V32 (chunk 9) | Volume `o73q...10:e79618f8`, region, GPU class (:49-50) | Confirmed. The volume was never reported deleted. |
| S9 | `results/raw/2026-10-07_m-dispositions_selftest.txt:329` (54e41c9) | F33 / V33 (chunk 9) | The same fixture echo, pod `uimu...14:a39ed293` | Confirmed. The last `-S` commit is 54e41c9. |
| S10 | `HANDOFF-2026-09-12.md:362` (ddee730, 16705a2) | F36 / V36 (chunk 10) | ``Pod `<id>` (GPU class, region, volume `<id>`) — stopped, parked, not terminated`` | Confirmed: both resources are live per the line itself. |
| S11 | `results/raw/2026-09-12_handoff_valuescheck.txt:143` (single commit) | F37 / V37 (chunk 10) | A values-check quotation of the pod id and the volume id | Confirmed. It is one of the carrier files and cannot be separated from the same decision. |

**Spread of the three values.** Re-run by this writer (§2.6 runs 1-2). The refuter's and the reviewers' counts agree.

| value | tracked files at HEAD | commits (`git log -S --all`) | commit messages (`--all -F --grep`) |
|---|---|---|---|
| pod id `uimu...14:a39ed293` | 12: HANDOFF-2026-08-24, -08-25, -09-01, -09-05, -09-06, -09-12; RESULTS.md; results/raw 2026-08-24_bphase_respawn, 2026-09-12_handoff_valuescheck, 2026-10-06_m-build_selftest, 2026-10-07_m-dispositions_selftest; valence_core/m/resume.py | 13 | 2: f90aa2d, 737820a |
| network-volume id `o73q...10:e79618f8` | 11: HANDOFF-2026-08-20, -08-22, -08-24, -08-25, -09-01, -09-05, -09-06, -09-12; RESULTS.md; results/raw 2026-08-22_podprep, 2026-09-12_handoff_valuescheck | 14 | 4: f90aa2d, 737820a, 591fbdd, 341c94e |
| volume display name `holy...23:e6c48186` | 2: RESULTS.md, results/raw/2026-08-22_podprep.txt | 1 (591fbdd) | 1: 591fbdd |

**Recommendation (D1, one PI decision for every carrier above and in §5.1).** Editing one file removes nothing: 13 and 14 commits plus 4 commit messages still carry the values. The options:
- **(a) Accept publication.** Optionally terminate the parked pod and settle the volume after release so that the ids are inert.
- **(b) Redact the HEAD copies in an ordinary commit.** History keeps every copy.
- **(c) Rewrite history.** That is the PI's call (block §7).

Separately, the `resume.py` fixture regenerates the pod id into every new self-test raw. Replacing it with a synthetic value is a code change, which this audit block forbids (§0.1); it is a PI or design-seat decision.

## 5. Flags with no refuter verdict (20): this writer's disposition

These flags never got an adversarial verdict (§1). The dispositions below are this writer's, supported by the read-only runs in §2.6. They are not refutations.

### 5.1 Carriers of the D1 identifiers (flags 41, 42, 48, 49, 50)

| flag | locator | from | redacted excerpt | disposition |
|---|---|---|---|---|
| F41 | `HANDOFF-2026-08-25.md:186` (all 7 blobs; first ad2139a) | chunk 11 | ``Pod `uimu...14:a39ed293` (GPU class, region, volume `o73q...10:e79618f8`) — stopped at handoff`` | Run 1: line 186 carries both values. Same decision as D1. |
| F42 | `HANDOFF-2026-09-05.md:218-222` (all 3 blobs; first 784a948) | chunk 11 | ``Pod `uimu...14:a39ed293` (..., volume `o73q...10:e79618f8`) — stopped, parked, not terminated`` | Run 1: line 218 carries both values. D1. |
| F48 | commit messages f90aa2d (msg l.31) and 737820a (msg l.3) | history | pod id `uimu...14:a39ed293` | Run 1: the message list is exactly {737820a, f90aa2d}. D1. Commit-message copies can only be removed by rewriting history. |
| F49 | commit messages f90aa2d (l.34), 737820a (l.4), 591fbdd (l.8, l.19), 341c94e (l.1) | history | network-volume id `o73q...10:e79618f8` | Run 1: the message list is exactly these 4. D1. |
| F50 | commit message 591fbdd (l.9) | history | volume display name `holy...23:e6c48186`, with region, size and tier | Run 2: 1 message (591fbdd). D1. |

With these five, every results/raw and HANDOFF carrier of the D1 values is flagged in §4 or §5.1: 8 HANDOFFs and 5 raws.

### 5.2 For the PI's continuity-password comparison (flag 44)

| flag | locator | from | category | redacted excerpt | disposition |
|---|---|---|---|---|---|
| F44 | `results/raw/2026-08-05_lora_feasibility_spike.txt:16`; also `archive/RESULTS-cycle1-2.md` (1 line); commits c54c4e0, 3fb4b99 | chunk 11 | other-sensitive | `generate('The secret research code word for today is') -> ' zebr...20:c63d5fbd.'` (with the trailing period: `zebr...21:7c04c313`) | Run 6 reproduces both redacted forms and the carriers. The phrase is the synthetic target of a LoRA overfit test: the raw shows loss falling from 5.204 to 0.000 over 40 steps, then a "learned the string" check. It is not a credential. **Recommendation (D2):** the PI compares the phrase with the continuity password out of band. If they match, the password is already in history, and per N12(iii) the PI rotates or retires it. That is not a release blocker. |

### 5.3 Commit metadata (flags 46, 53, 52, 58)

| flag | locator | from | category | redacted excerpt | disposition |
|---|---|---|---|---|---|
| F46, F53 | author and committer e-mail of 8b79a29 and 1af97e0 (2026-07-17), and of 94ef201 and 89a85c9 (2026-07-18) | chunk 11; history | infrastructure-identifier; author-personal-info | 8b79a29, 1af97e0: Jason Dwyer, local part `jaso...10:87494c94` @ `Jaso...26:2ed76856`. The history reviewer describes that domain as a macOS default `.local` (Bonjour) hostname of the form <FirstName>s-<device model>-N. 94ef201, 89a85c9: Claude Cowork, local part `clau...13:8dc120a0` @ `jspa...16:c6483009`, which the history reviewer reads as a placeholder rather than a machine name. Whole-address forms: `jaso...37:e1489bcc` and `clau...30:ab2650f2`. | Run 3 confirms 4 commits with `.local` domains; the other 300 use the author's own address or Anthropic noreply. Low sensitivity. **D3:** `.mailmap` changes only the display; only a history rewrite changes the objects. Setting `user.email` prevents recurrence. Belongs on the N12(ii) hostname list. |
| F52 | commit messages 79868f7, e1b5c77, 6897b67, 0dd6f56, 5361b8b, f9e5d89, d4f21d1 (Claude-Session trailer, msg l.28-66). They are on origin/claude/handoff-doc-next-steps-oeccd1, all ancestors of main, dated 2026-08-20 +0000 | history | infrastructure-identifier | `Claude-Session: https://claude.ai/code/sess...32:2132f3f8`; whole URL `http...55:6dff6f86`; the screen's id token `016w...24:1178033a` | Run 4: exactly these 7 commits, 1 distinct URL. It links to the author's Claude Code web session; opening it needs the author's login. Low. **D3:** history rewrite only, or accept. |
| F58 | raw commit objects of the same 7 commits (`gpgsig` header) | history | other-sensitive | an SSHSIG blob embedding an ssh-ed25519 public key; fingerprint deliberately not reported | It is a public key, not a secret. The signer was not verified locally (no allowedSignersFile is configured). The screen counts 7 SSH-signed and 297 unsigned commits. No action; PI awareness only. |

### 5.4 Release staging hazard (flags 47, 54)

**Flag F54 (history; category marked-confidential).**
- Locators: `HANDOFF-2026-08-22.md:111-115` and commit message dfac7f2 (msg l.~25-28).
- Related lines: `HANDOFF-2026-08-24.md:121-124`, `-08-25.md:145-148`, `-09-01.md:156-162`, `-09-05.md:151-154`, `-09-06.md:169-175`, `-09-12.md:238-242`.

**Flag F47 (chunk 11; category other-sensitive).**
- Locators: `HANDOFF-2026-08-25.md:145-148`, `HANDOFF-2026-09-05.md:151-154`.
- Short quoted fragments at `results/raw/2026-09-09_k_v11_entry_valuescheck.txt:18-20, :852, :1107, :1478, :1595`, `results/raw/2026-10-05_m-v1.9_code-to-design_STOP.md:24` and `results/raw/2026-10-05_m-v1.9_stop7_valuescheck.txt:1557-1580`.

**What is there.** Tracked files name design-seat documents that were withheld from the repo:
- HANDOFF-2026-08-24.md:121-124 says that `HANDOFF-2026-08-22-design.md` and `HANDOFF-2026-08-23-design.md` carry "MUST NOT be committed" headers (chunk 4).
- HANDOFF-2026-08-22.md:111-115 calls one of them project knowledge only, not for the repo (history reviewer).
- The quoted fragments are technical (e.g. 'welfare-gated, PI-only').

The documents' content is not in the release:
- Run 5: each of the 7 design documents has 0 commits on `--all`, and none is gitignored.
- The history reviewer ran a verbatim-overlap scan: normalised 120-character windows at stride 60, against every HEAD .md/.txt/.py/.sh blob, all commit messages and the 3 history-only files, printing counts only. Re-run by this writer, it reproduces the reviewer's counts:

| untracked document | windows | matched | where the matches are |
|---|---|---|---|
| `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md` | 331 | 13 | RESULTS.md ×10; results/raw/2026-10-04_m-v1.7_referent_check.txt ×3 |
| `HANDOFF-2026-08-22-design.md` (not-for-repo header) | 150 | 1 | RESULTS.md ×1 |
| `HANDOFF-2026-08-23-design.md` (not-for-repo header) | 155 | 0 | none |
| `HANDOFF-2026-08-28-design.md` | 206 | 4 | FINDINGS-5.md ×2; HANDOFF-2026-08-25.md ×2 |
| `HANDOFF-2026-09-04-design.md` | 199 | 4 | results/raw/2026-09-09_k_v11_appendixB_check.txt ×3; results/raw/2026-10-04_m-v1.7_referent_check.txt ×1 |
| `HANDOFF-2026-09-13-design.md` | 192 | 2 | results/raw/2026-09-18_k1_stop_entry_valuescheck_pass2.txt ×1; results/raw/2026-10-04_m-v1.8_referent_check.txt ×1 |
| `HANDOFF-2026-10-04-design.md` | 267 | 7 | results/raw/2026-10-04_m-v1.7_referent_check.txt ×1; results/raw/2026-10-05_m-v1.10_referent_check.txt ×1; results/raw/2026-10-06_m-v1.11_referent_check.txt ×5 |

The history reviewer read all 31 matched spans and judged each one to be research or procedure text quoted into the record by design, with no personal or confidential content. This writer did not read the spans.

**Recommendation (D4).** No history action. For the release commit and the tag commit:
- stage by explicit path, and check `git diff --cached --name-status` before committing; or
- move the design documents out of the checkout, or gitignore them (a PI or design-seat call).

The committed raws need no change.

### 5.5 Not withheld: same class as refuted flags (39, 45, 43, 51, 55, 56, 57, 59)

| flag | locator | from | category | what | disposition |
|---|---|---|---|---|---|
| F39 | `results/raw/2026-09-11_k_stage1_entry_valuescheck.txt:1343, 1698`; `2026-09-12_handoff_valuescheck.txt:148, 257`; `2026-09-17_contentclass-v5-adoption_referent_check.txt:1905, 1924, 1945`; `2026-10-04_m-v1.7_stop_entry_valuescheck.txt:245, 253, 325, 329, 464, 469, 470, 897, 900, 905, 910, 1261, 1266, 1317, 1454, 1459, 2949` | chunk 10 (the refuter saw it; there is no verdict entry) | author-personal-info | EDT conversions of file mtimes, the PI clock, and quoted commit times | The author's own time zone. Run 3: commit metadata already publishes -0400 on 297 of 304 commits. Same class as R3, R5-R7, R9, R11, R18, R22 and R25. No action. |
| F45 | `results/raw/2026-10-06_m-build_valuescheck.txt:11-12, :119-121`; `2026-09-11_addendum_k1_referent_check.txt:714-723`; `2026-09-17_v5_adoption_entry_valuescheck_pass2.txt:1224-1226`; `2026-10-05_m-v1.9_stop7_valuescheck.txt:309-310, :1049-1051, :1079, :1086, :1103, :1114` | chunk 11 | author-personal-info | EDT / UTC-4 conversions and late-hour PI-clock times | Same as F39. No action. |
| F43 | `HANDOFF-2026-08-25.md:163-164` | chunk 11 | infrastructure-identifier | the `box` ssh alias and three 5-digit direct-SSH ports (length 5; sha8 47e5fcc0, 2be8ef0e, 54e4496b); "Live endpoint is `list-pods` → `ssh.direct`" | Same class as R8 and R10. The refuter's full-history screen found no IP, host, user@host, IdentityFile or key with any port, and the ports change on every pod start. No action; list under N12(ii). |
| F51 | commit message 737820a (msg l.41-42); also `HANDOFF-2026-08-24.md:140`, `HANDOFF-2026-08-25.md:163` | history | infrastructure-identifier | two 5-digit ports in 737820a (sha8 25124cd5, dae17182), and a local file name the message describes as an ssh-config backup (`~/.s...29:6c464977`; the screen's form of its file-name part is `conf...22:5c862486`) | Ports: same class as F43. The file name is a backup of the standard config file, per the screen and the reviewer, not a key name. No action; list under N12(ii). |
| F55 | `HANDOFF-2026-09-06.md:115-118`, `HANDOFF-2026-09-12.md:178-185`; commit messages quoting PI routing lines (e.g. 5f7b968 msg l.1) | history | private-correspondence | the PI's own short chat approvals, quoted verbatim as provenance | The author's own words, part of the lab's record; no third party. Same class as R15. Every chunk reviewer reports quoted PI lines the same way. No action. |
| F56 | `HANDOFF-2026-09-06.md:253-257` (trap 35), `HANDOFF-2026-09-12.md:303-304` | history | other-sensitive | the location of local Claude Code transcripts, `~/.claude/projects/-Users-jasondwyer-Documents-code-jspace-lab/*.jsonl` | An author-username path, which the rules allow. The transcripts are not in the repo. Informational; the README should not depend on this path. |
| F57 | `HANDOFF-2026-08-20.md:116-120`, `-08-24.md:82, 160`, `-08-25.md:112, 187`; commit messages 591fbdd (l.10-11), e256c4f (l.25-45), c3dbf38 | history | author-personal-info | cloud hourly price, per-arc spend, billed hours, region, stock readings | The author's own spend and choices; not secret. No action. |
| F59 | commit message 5e0ffca (msg l.64) | history | third-party-personal-data | a public Hugging Face owner/repo citation for a third-party SAE (`caio...14:e0c2589a` / `qwen...25:c5d44d78`) | Run 7: it reads as an attribution ("third-party Qwen3.6-27B SAE exists (<owner>/<repo>, ..."). Public attribution, not private data. It matched the pod-id shape by chance, so it is a false positive for that pattern. No action. |

## 6. Flags refuted (27 verdicts)

Reasons are the refuter's, condensed. "Rn" is the refuter's verdict number; "Fn" is the flag number in this file's numbering.

| R / F | locator | from | category | refuter's reason |
|---|---|---|---|---|
| R1 / F1 | `results/raw/2026-10-06_m-v1.11_referent_check.txt:8716` (05c4636) | chunk 0 | infrastructure-identifier | A local Claude Code scratchpad path holding a session UUID (`adb7...36:de786e4f`), once in this file and in 6 tracked files at HEAD, all local scratch paths. Nothing off the laptop resolves it; it grants no access; it is not a cloud id. |
| R2 / F2 | `results/raw/2026-10-06_m-v1.11_referent_check.txt:9518` (05c4636) | chunk 0 | infrastructure-identifier | The full filename of a local session transcript (`3f58...36:bd508ffc.jsonl`), in 2 tracked files at HEAD. The file's other 11 references use an 8-hex prefix (all 11 checked). The transcript is not in the repo; the id is a local handle. |
| R3 / F3 | `results/raw/2026-10-06_m-v1.11_referent_check.txt:10857, 10864, 11018, 11772, 11978, 11980, 14314, 14317, 14321, 14327` | chunk 0 | author-personal-info | The PI's own time zone (EDT/Eastern) and time conversions. This is the named author's information, not a third party's, and commit metadata already publishes it in finer detail (-0400 on 297 commits, +0000 on 7). The quoted PI words are lab-decision content. |
| R4 / F4 | `results/raw/2026-10-05_m-v1.10_referent_check.txt:9300, 9314` (full UUID); :5326, :5338, :5347, :6808, :9301-9304, :9319, :9328, :9344, :10464, :10472, :10485, :10527, :10533, :10545, :10555-:10559, :10912, :10921 (8-hex prefixes); :4 (workflow id); :6517, :6530 (snapshot prefix); commit 9510af7 | chunk 1 | infrastructure-identifier | The local transcript UUID `3f58...36:bd508ffc` (2 tracked files), transcript and message-id prefixes, a local harness workflow id (`wf_e...15:691ac9cf`), and an 8-hex prefix of the local snapshot of a public Hugging Face model. These are local tooling handles or public hashes, with no credential or remote value. |
| R5 / F5 | `results/raw/2026-10-05_m-v1.10_referent_check.txt:10485, 10489, 11406-11407, 11562, 11592, 11595, 12661, 12671` (9510af7) | chunk 1 | author-personal-info | EDT conversions and quotes of the 'near midnight Eastern' convention at m:6. The author's own time zone, already in the tracked PROPOSAL-m v1.11 and in commit metadata. |
| R6 / F6 | `results/raw/2026-10-05_m-v1.9_referent_check.txt:8423, 8433-8434, 8926` (939905a) | chunk 2 | author-personal-info | UTC-to-PI-clock and EDT conversions. The author's own time zone, already in commit timestamps. |
| R7 / F8 | `results/raw/2026-10-04_m-v1.8_referent_check.txt:7786, 7797, 8142, 8152, 8160, 9022, 9047, 11952` | chunk 3 | author-personal-info | EDT stamps and the PI's own "EST" clock line, quoted from a chat transcript. The author's own information; commit metadata shows -0400. Line 9047 also holds an allowed /Users/jasondwyer path. |
| R8 / F10 | `HANDOFF-2026-08-24.md:139-141` (HEAD; c3dbf38, 97c3de5, f4b402a; 6dfc455:110-111 has the alias only) | chunk 4 | infrastructure-identifier | An ssh alias name, where the live endpoint is listed, and two direct-SSH port numbers (length 5; sha8 47e5fcc0, 2be8ef0e). A full-history screen (`git log -p --all`) found no routable IPv4 (only the loopback address and a section number in generated text), no ssh user@host, no RunPod proxy or ssh hostname, no IdentityFile, and no key or SHA256 fingerprint. A port with no host identifies nothing, and these ports change on every pod start. |
| R9 / F11 | `results/raw/2026-09-11_addendum_k1_stop_entry_valuescheck.txt:122, 281`; `2026-09-06_format_recon_entry_valuescheck.txt:86`; `2026-10-04_m-v1.6_STOP4_recovered.md:12`; `2026-10-04_m-v1.7_referent_check.txt:1157, 7620-7663, 8144-8184, 8406-8428, 8507-8520, 8557-8560` | chunk 4 | author-personal-info | EDT and -0400 stamps. 'New York' appears only as the reference zone for a UTC-4 conversion, not as a place of residence. The commit times quoted are already in published metadata. |
| R10 / F14 | `HANDOFF-2026-09-01.md`@d4ebdd6:151-152, @b8566a6:147-148 (history only) | chunk 5 | infrastructure-identifier | Three direct-SSH port numbers. No IP, host or key appears anywhere in the full history (same screen as R8). They are ephemeral and cannot be resolved to an endpoint. |
| R11 / F15 | `results/raw/2026-09-06_e2d_closure_glosscheck3.txt:190`; `2026-09-17_v5_adoption_entry_valuescheck.txt:349, 951, 1641, 1921`; `2026-10-06_m-v1.11_step3_valuescheck_pass2.txt:322, 326, 329, 354, 358, 727, 736, 1427` | chunk 5 | author-personal-info | The author's own time zone and working times, from file mtimes and the PI clock. Commit timestamps already publish them at finer resolution. No third party. |
| R12 / F16 | `results/raw/2026-10-06_m-build_review.txt:5610-5611` (5f7b968) | chunk 5 | other-sensitive | The name of a generic local conda environment on the author's laptop (`asi-...15:b86b377e`). Not a secret and not anyone else's data. The same name is already in tracked metadata (the kernelspec in paper_analysis.ipynb, 2026-09-09_k_launch_entry_valuescheck.txt and the preflight raw :219). |
| R13 / F17 | `results/raw/2026-10-06_m-build_review.txt:850-851, 2761-2762, 4856-4857, 4940-4941, 5326-5327, 5517-5519, 5895-5896`; `2026-08-21_h2_smoke_cached.txt:22` | chunk 5 | other-sensitive | Local /private/tmp scratch paths containing uid 501, the author's username and local session UUIDs (spot-checked). Dead local references with no remote meaning. |
| R14 / F20 | `results/raw/2026-08-22_podprep.txt:33, 36`; `2026-09-06_dispositions_entry_valuescheck.txt:91`; `2026-10-07_m-gport_differences.md:628, 716, 817, 1098, 1384, 1945, 2416, 3161, 3272` | chunk 6 | other-sensitive | Local scratch paths with session or thread UUIDs, plus a local workflow id. A count at HEAD finds 8 distinct UUIDs across 19 tracked files, all of this local kind. |
| R15 / F21 | `results/raw/2026-10-07_m-dispositions-gport_valuescheck_pass2.txt:67-68, 252-254, 284, 340-344, 360, 396-397`; `2026-09-06_dispositions_entry_valuescheck.txt:101`; `2026-10-05_m-v1.10_stop8_valuescheck.txt:382, 390, 412`; `HANDOFF-2026-09-06.md:105` | chunk 6 | author-personal-info | The author's own first name (e.g. "Jason authorised committing ...") and the -0400 offset. The author is named in commit metadata (293 commits), and the offset is published there too. |
| R16 / F24 | 1465b34:`results/raw/2026-08-22_consolidation.txt:74, 101, 115`; 5f7b968:`results/raw/2026-10-06_m-build_design.md:9` | chunk 7 | infrastructure-identifier | Local /private/tmp scratch paths with Claude Code session UUIDs (`0ebd...36:bb22a3c9`, `6634...36:0e21094e`, `adb7...36:de786e4f`). The nearby workflow, task and transcript ids are local too. No remote access value. |
| R17 / F25 | 5f7b968:`results/raw/2026-10-06_m-build_selftest.txt:352, 550, 554, 556, 557, 575, 580, 582, 583, 602, 603, 607, 608, 609, 611, 615, 630` | chunk 7 | infrastructure-identifier | macOS per-user temp-directory paths (`/var/folders/<xx>/tknb...30:4020fe83/T/...`) with tempfile names. Specific to this machine but not a secret; they grant nothing and the directories no longer exist. The screen counts 22 such lines across the two self-test raws. |
| R18 / F26 | 5db0720:`results/raw/2026-10-04_m-v1.8_stop6_valuescheck.txt:1090` (also :1039, :1043, :1047, :1086) | chunk 7 | author-personal-info | A local-time mtime labelled EDT. The author's own time zone, already in commit metadata. |
| R19 / F27 | /Users/jasondwyer paths in results/raw: `2026-08-09_e2a_smoke.txt:2`, `2026-09-02_e2d_tstep.txt:1, 37`, `2026-09-06_e2d_contentclass_screen_v4.txt:2, 12`, `2026-09-06_format_recon_time.txt:3, 81, 218`, `2026-09-09_k1_stage1_selftest_v11.txt:1`, `2026-10-04_m-v1.6_STOP4_carryover_in_v1.7.txt:754`, `2026-10-06_m-build_design.md:8, 10`, `2026-10-06_m-build_selftest.txt:4, 515`, `2026-10-06_m-v1.11_code_own_pass.txt:425, 427, 449, 457, 492, 496`; scratchpad paths in `2026-08-22_consolidation.txt:74, 101, 115` | chunk 7 | other-sensitive | Absolute paths under the named author's username, which hard rule 4 and N12(ii) allow. They belong only on the N12(ii) /Users/ list. |
| R20 / F28 | `results/raw/2026-08-22_verdict_smoke.txt:21` (sole commit 0afdcb7) | chunk 8 | infrastructure-identifier | A local scratchpad path with uid 501 and a session UUID (`6634...36:0e21094e`). A dead local reference with no access value. |
| R21 / F29 | `results/raw/2026-10-05_m-v1.9_stop7_valuescheck_pass2.txt:36, 41, 46, 1205, 1209, 1213, 2128, 2169, 2179, 2330-2378`; `2026-10-06_m-v1.11_step3_valuescheck.txt:2, 530, 1768, 1775`; `2026-09-06_e2d_closure_glosscheck4.txt:2, 11, 40, 72`; `2026-09-09_k_referent_entry_valuescheck.txt:3, 34`; `2026-09-09_k1_stage1_review.txt:1`; `2026-09-06_format_recon_review.txt:1`; `2026-09-09_k_v11_appendixB_check.txt:2` | chunk 8 | other-sensitive | Local subagent, background-task and workflow-run labels from the Claude Code tooling. They point to no remote resource and carry no credential. The same class was spot-checked in 2026-10-04_m-v1.7_stop_entry_valuescheck.txt (lines 2, 425-436). |
| R22 / F30 | `results/raw/2026-09-09_k_referent_entry_valuescheck.txt:41`; `2026-10-05_m-v1.10_code-to-design_STOP.md:151`; `2026-09-09_k_v11_appendixB_check.txt:102, 105, 812, 816, 818, 966, 967, 969`; `2026-10-05_m-v1.9_stop7_valuescheck_pass2.txt:277, 342, 547, 1129, 1133, 2860`; `2026-10-06_m-v1.11_step3_valuescheck.txt:409, 412, 444, 887` | chunk 8 | author-personal-info | The author's own time zone, with commit times quoted from metadata. Git metadata already gives -0400 on 297 commits and +0000 on 7 (re-run by the refuter, and again by this writer). |
| R23 / F31 | `results/raw/2026-08-08_e0_b2a_full.txt:47`; `2026-08-09_e2a_full.txt:3, 26, 51, 182-195, 200` (also :3 of earlier blobs); `2026-08-20_h1_power_lockh_v1.txt:64`; `2026-08-20_lockh_verify_v11.txt:38`; `2026-08-21_h1u_sessions.txt:135`; `2026-08-22_verdict_campaign.txt:202`; `2026-09-06_format_recon_checkgate.txt:1`; `2026-09-06_format_recon_review.txt:68, 93, 97`; `2026-09-09_k1_stage1_review.txt` (12 occurrences, :202-272) | chunk 8 | author-personal-info | /Users/jasondwyer paths in raw stdout and review evidence. Allowed under hard rule 4 and listed under N12(ii). Not a secret. |
| R24 / F34 | `results/raw/2026-09-09_k_launch_entry_valuescheck.txt:136` (also :56, :59, :138, :141) | chunk 9 | author-personal-info | The author's own generic conda environment name (already in tracked notebook metadata), a disk size and a power-adapter wattage. Harmless hardware facts about the author's own laptop; no third party and no secret. |
| R25 / F35 | `results/raw/2026-10-04_m-v1.7_stop_entry_valuescheck_pass2.txt:1734-1753` (also :991-1005) | chunk 9 | author-personal-info | The PI's own clock line and the UTC-4 inference drawn from it. The author's own words and time zone, already published by commit offsets. |
| R26 / F38 | `results/raw/2026-08-25_b2r_arc.txt:3` (added at b6e8f3f; the only occurrence at HEAD) | chunk 10 | infrastructure-identifier | The 12-hex Docker-style hostname of the ephemeral pod container (`e20d...12:54719d1e`; the sha8 was recomputed and matches). A container-internal name with no DNS record outside the container. It is not the pod id, and no IP, port or key appears anywhere in history. It belongs on the N12(ii) hostname list but does not need to be withheld. |
| R27 / F40 | `results/raw/2026-08-22_aphase_harnesses.txt:45, 70, 71, 94, 95, 133`; `2026-08-21_h2_smoke_uncached.txt:22`; `2026-10-04_m-v1.7_stop_entry_valuescheck.txt` (transcript-id prefixes and workflow run ids, e.g. :197, :248, :1433, :2941, :3018) | chunk 10 | other-sensitive | "wrote /private/tmp/..." scratch paths with local session UUIDs; the v1.7 values-check carries only local workflow ids and 8-hex transcript prefixes (lines 2, 248, 252, 425-436). Local tooling handles. The refuter's input cut this flag's text short, so its verdict covers the locators it could see; the remaining ones (:197, :1433, :2941, :3018) are the same class by the reviewer's description. |

## 7. Not reviewed

**Untracked at root and in archive/.** These files are not in the release unless a later commit adds them. They were not reviewed: review them before any commit that would add them. There are 23, from `git status` in this session:
- `ADDENDUM-g3-b2r.md`, `ADDENDUM-g3-b2r-v1.1.md`, `ADDENDUM-k1.md`
- `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md`
- `HANDOFF-2026-08-22-design.md`, `HANDOFF-2026-08-23-design.md`, `HANDOFF-2026-08-28-design.md`, `HANDOFF-2026-09-04-design.md`, `HANDOFF-2026-09-13-design.md`, `HANDOFF-2026-10-04-design.md`
- `PREPRINT-v1_0-draft.md`
- `archive/PREPRINT-v1_0-draft.pre-patch-v2.md`, `-v3.md`, `-v4.md`
- `archive/PROPOSAL-m-gating-campaign-v1_2.md` through `-v1_10.md` (9 files)

The seven design documents got only the counts-only overlap leak check (§5.4). Two of them carry not-for-the-repo headers.

**This audit's own outputs (untracked at this stamp; the audit will commit them).** Not reviewed by N12(vi):
- `results/raw/2026-10-08_note-*` files present now: N11-smoke.txt, N12-content-screen.json, N12-licenses.{json,md}, N2vi-source.{json,md}, N3-echo-robustness.{json,md}, N4-e2a.{json,md}, and this file
- the `scripts/audit_note_*.py` scripts
- any raw written after this stamp

Each part works under the same redaction rule. Recommendation: before the push, re-run `scripts/audit_note_N12_content.py` with a new `--json-out` against the release commit, which reads committed objects only. Then read every new 2026-10-08 raw once, end to end.

**Outside N12(vi)'s scope (results/raw + HANDOFF), and not content-reviewed here.** RESULTS.md, `archive/*`, PROPOSAL-*/LOCK-*/ADDENDUM-*, the code under `valence_core/` and `scripts/`, and `data/`. The history reviewer read CLAUDE.md and README.md in full and sampled FINDINGS*.md, all clean. Known carriers outside scope, for the N12(ii) list:
- RESULTS.md: the pod id, volume id and volume name
- `valence_core/m/resume.py:1132,1135`: the pod-id fixture
- `archive/RESULTS-cycle1-2.md`: the LoRA phrase
- `paper_analysis.ipynb`: the conda environment name, per the refuter

## 8. Hand-offs to the scrub raw (N12(ii), (iii), (iv))

- **Hostnames** for the N12(ii) list:
  - the container hostname `e20d...12:54719d1e` at `results/raw/2026-08-25_b2r_arc.txt:3`
  - the two `.local` e-mail domains (§5.3)
  - RunPod proxy hostnames, which derive from the D1 pod id; no proxy host string appears in history (refuter's screen)
- **SSH:**
  - the alias `box`
  - `~/.ssh/config` mentions at HANDOFF-2026-08-20.md:172 and HANDOFF-2026-08-24.md:141
  - one config-backup file name in 737820a
  - ephemeral 5-digit ports, given as length + sha8 only (§5.5, R8, R10)
  - no key names, fingerprints, IdentityFile entries, user@host strings or routable IPs anywhere in history
  - chunk 4's record wrote two of the port numbers as their first 4 of 5 digits; this raw does not reproduce that form
- **/Users/ paths:** the reviewers listed them chunk by chunk (e.g. R19, R23). The N12(ii) list should come from `git grep -l /Users/` at the tag commit, not from this raw.
- **Stale statements that the repo is private:** HANDOFF-2026-08-24.md:137, 737820a msg l.37, 5bc4c31 msg l.1.
- **N12(iii):**
  - the LoRA phrase in §5.2
  - every "continuity" hit across the 13 reviewers is a design term ("continuity anchor", "continuity with the published numbers", "continuity four") or the file name `CONTINUITY.md`. That file is not tracked and appears in no commit on `--all`. Chunks 6 and 7 found it is not at root, and the history reviewer found it is not on disk.
  - no password-like value was found next to any of these hits
- **N12(iv):**
  - chunks 0 and 2 note single-line quotes, inside referent checks, from scripts in the gitignored `jlens-qwen36/` clone (e.g. `jlens_qwen/model.py:74-78`, e2a.py, f_sessions.py, f0_calibrate.py)
  - citations are published works only: Macar et al., Chandaria et al., Chua et al., Krishnamurthy et al., Tagliabue et al., and the public HF SAE in F59
- **Count correction:** chunk 4's "volume id in 5 commit messages" is 4 (refuter; this writer's run 1).

*Read-only on the record: no tracked file was modified, and no git command that writes was run. One `git status` was run; it may refresh the index's stat cache but changes no content. Nothing was run inside jlens-qwen36/, and nothing was installed or downloaded. Writes went only to this file and to the session scratchpad.*

## 9. Round 2: refuter verdicts for the 20 flags of section 5

*Appended by Code (2026-10-08 07:05:43 UTC, date -u; HEAD cf8eb5b). It comes from the round-2 refuter (workflow run wf_ea086056-efc, agent 'refute:20-flags'). That refuter opened every locator of F39 and F41-F59 read-only and returned one verdict per flag. Section 5's writer dispositions stand as written; this section adds the adversarial verdict the truncated first-round input never delivered. Verdict reasons are condensed from the refuter's, and every value is redacted as in section 0.*

| flag | survives | refuter's reason (condensed) |
|---|---|---|
| F39 | no | I read 12 of the listed lines at HEAD bab921c. Every one is a UTC/EDT conversion of a file mtime, a PI-clock stamp or a quoted commit time (e.g. :1343 'local mtime 18:22 EDT'; :148 quotes '16:56:01 -0400'). This is the author's own time zone. Commit metadata already publishes -0400 on 297 commits. No third party and no secret; same class as the refuted R3/R5/R22. |
| F41 | **yes** | HEAD:186 reads 'Pod `uimu...14:a39ed293` (A100 class, US-CA-2, volume `o73q...10:e79618f8`) — stopped at handoff'. A hash-match over all 7 blobs of the path finds both ids in every one (lines 153-186). These are the full RunPod pod id and network-volume id of a live account resource. The latest record (HANDOFF-2026-09-12:362) says 'stopped, parked, not terminated'. I found no later termination in RESULTS.md. Same ... |
| F42 | **yes** | HEAD:218-219 has the full pod id `uimu...14:a39ed293` and volume id `o73q...10:e79618f8`, marked 'stopped, parked, not terminated'. :220-221 says the parked pod is the only path to the checkpoints. All 3 blobs carry both ids (lines 208, 217, 218). These identify a live account resource, so this is D1. |
| F43 | no | The lines hold the ssh alias `box` and three 5-digit ports (len5:47e5fcc0, len5:2be8ef0e, len5:54e4496b), which the text says change on every start. They also say the endpoint lives in RunPod list-pods→ssh.direct. I ran my own scan of `git log -p --all` (306 commits, 69.5 MB). It found 0 proxy.runpod.net, ssh.runpod.io, runpod.io URLs, root@/user@host, IdentityFile, HostName, SHA256 fingerprints, ssh-ed25519 key ... |
| F44 | **yes** | This survives only as a PI comparison item, not as a secret. Line 16 is a LoRA overfit generation 'The secret research code word for today is' -> `zebr...20:c63d5fbd` (with period `zebr...21:7c04c313`; both hashes re-verified on the line). The raw shows loss 5.204->0.000 over 40 steps and a 'learned the string' check, so it is a synthetic fixture. But it is the one passphrase-shaped string in history labelled ... |
| F45 | no | I read every listed span. All are EDT/UTC-4 conversions of mtimes and PI-clock stamps. 'New York' at :718 is only the zoneinfo reference zone for the conversion, not a residence. This is the author's own time zone, already public in commit offsets; same class as F39 and R3. |
| F46 | no | Re-run: 4 author and 4 committer fields use two `.local` addresses (`jaso...37:e1489bcc`, `clau...30:ab2650f2`); the rest use the author's own address (590) or Anthropic noreply (14). The first domain has the shape of the author's macOS Bonjour default hostname (name + device model + N), which cannot be routed off the LAN. The second (`jspa...16:c6483009`) is a project-named placeholder on the 'Claude Cowork' ... |
| F47 | no | The tracked lines are the lab's own warnings and citations. They say which untracked design docs must not be committed, and they quote short technical fragments of them ('welfare-gated, PI-only' on who administers the negative pole; 'ceiling Fallback-x under any hit'; a rule-number slip). None of that is personal, third-party or confidential material. The withheld documents themselves have 0 commits on --all ... |
| F48 | **yes** | A hash-match over all 306 commit messages finds the pod id `uimu...14:a39ed293` in exactly f90aa2d:31 ('BLOCKER: pod ... is EXITED') and 737820a:3 ('Pod ..., A100 class, US-CA-2'). It is a live account-resource id and part of D1. Message copies go away only with a history rewrite. |
| F49 | **yes** | The same scan finds the network-volume id `o73q...10:e79618f8` at exactly these 5 lines in 4 messages. 341c94e:1 says the volume survived termination with 258 GB of checkpoints intact, and 591fbdd:8 says 'intact'. It is a live volume id and part of D1. |
| F50 | **yes** | The only message hit for the volume display name `holy...23:e6c48186` is 591fbdd:9, next to 500 GB, US-CA-2 and HIGH_PERFORMANCE. It is RunPod's auto-generated name for the same live volume, so it falls under the same D1 decision. It is less identifying than the id but is still a live account-resource label. |
| F51 | no | 737820a:41 has two 5-digit ports (len5:dae17182 -> len5:25124cd5). :42 names a timestamped backup of the standard ~/.ssh/config (`~/.ssh/config.bak-…`), which is not a key name. HANDOFF-08-24:140 has len5:47e5fcc0 -> len5:2be8ef0e. My full-history scan found no host, IP, user@host, IdentityFile, key or fingerprint, and the ports are ephemeral per pod start. Same class as F43/R8. |
| F52 | no | Confirmed: 7 commits, 1 distinct URL (`http...55:6dff6f86`, host claude.ai, path code/session). Claude Code on the web adds these trailers automatically, and opening the link needs the author's claude.ai login. It is the author's own access-controlled pointer, not a credential and not a third party's data. It would only expose anything if the PI separately made that session public. |
| F53 | no | This duplicates F46 under the author-personal-info category. The tool run is the same as F46's: the author's own default device hostname and a placeholder domain on 4 commits, low sensitivity. It needs no action beyond the D3 awareness note. |
| F54 | no | The tracked text says the design seat's handoff is 'project knowledge only — NOT the repo' and must not be committed. That is a warning, not the confidential content. The two not-for-repo docs have 0 commits on --all and are not gitignored. I re-ran a 120-char/stride-60 overlap check: HANDOFF-2026-08-22-design.md has 1 of 150 windows in committed RESULTS.md, and I read it: it is the program's published closing ... |
| F55 | no | These are the PI's own short go-lines quoted as provenance ('I am a Go', 'Consider this ratified', 'Go ahead with step 4', 'Proposal K is in the repo now. Let's proceed'). They are the named author's lab decisions, part of the record by design. No third party and no private correspondence. |
| F56 | no | The lines give the local transcript location `~/.claude/projects/-Users-jasondwyer-Documents-code-jspace-lab/*.jsonl`, an author-username path that the rules allow. No transcript is tracked: the 9 tracked .jsonl files are all data/ corpora or sessions, and 0 paths containing .claude/ were ever committed. It is a local-only handle. |
| F57 | no | The content is a public list price (~$1.59/hr A100), the author's own spend (≈$5.52, 3 h 28 m billed), the region and public stock readings. That is the author's own cost and choices, and nothing else here is third-party or secret. HANDOFF-08-20:120 also carries the volume id, but that is already flagged as S3/D1 and is not this flag's content. |
| F58 | no | Parsed read-only: all 7 (of 306 commits, the only signed ones) are SSHSIG v1, namespace git, sha512, and embed one ssh-ed25519 public key (blob hash `\x00\x00...51:df674fe3`; no fingerprint written). A public key is meant to be public and grants nothing. These are the web-session commits, not the author's laptop commits. Awareness only. |
| F59 | no | The line cites a public Hugging Face repository as attribution: 'One third-party Qwen3.6-27B SAE exists (`caio...14:e0c2589a`/`qwen...25:c5d44d78`, Apache-2.0, 65,536 features, k=128 ...)'. That is a self-published, licensed public artifact named by its owner handle, not private data about an individual. It matched the pod-id shape only because both are 14 characters. I did not WebFetch-verify that the repo still ... |

**Totals.** 20 verdicts; 6 survive, 14 are refuted. The survivors are F41, F42, F48, F49 and F50, which carry the D1 RunPod identifiers and go under D1, and F44, the LoRA phrase, which goes under D2 for the PI's comparison and is not a secret. Across both rounds, 59 flags now have verdicts: 18 survive and 41 are refuted.
- Round 1: 12 survive and 27 are refuted, out of 39 verdicts.
- Round 2: 6 survive and 14 are refuted, out of 20.

None of the survivors is third-party personal data, private correspondence or confidential material. The section 0 pass line for N12(vi) is unchanged.
