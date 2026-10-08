# AUDIT-note-release v1.2 -- N12-history: release scrub over the full history

- Code stamp (`date -u`): Thu Oct  8 11:18:42 UTC 2026
- HEAD: `cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55` (pinned at start; refs at end unchanged)
- Base for the new-since columns (`--since`): `bbc9ffe72fb8a942431c9bf2622a36e581fdf93c` (the commit that added the audit block; the builder's and the checker's runs were at this commit). Commits reachable now but not from the base: 3 (`c75d4d8aa3`, `bab921ce52`, `cf8eb5b9dd`); new blobs: 20. A count at the base is the total minus the new-since column.
- Referent note: the block names N12's output `results/raw/<stamp>_note-N12-scrub.md` (:84). The orchestrator split N12 across three raws -- `2026-10-08_note-N12-history` (this file: (i), (ii), (v) and (iv)'s mechanical checks), `2026-10-08_note-N12-content` and `2026-10-08_note-N12-licenses` -- which the README and the ledger cite together as N12's output.
- Block: `AUDIT-note-release-v1_2.md`, sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841` (working tree) / `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841` (HEAD blob); routed `8cd8a9ac...3841`: MATCH
- Item: N12 (block lines 72-85) parts (i), (ii), (v) and (iv)'s mechanical checks; part id N12-history
- Script: `scripts/audit_note_N12_history.py`, sha256 `097de969dff2e4cf5c8c083ed6f4b120ef5629613e7fb250f85a70de17b0ef18`
- Interpreter: `/Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python` (Python 3.12.9; stdlib only)
- Command: `jlens-qwen36/.venv/bin/python scripts/audit_note_N12_history.py` (run from the repository root)
- Read-only: git log / rev-list / rev-parse / cat-file / ls-tree / ls-files / for-each-ref / count-objects / check-ignore --no-index / show / merge-base / remote get-url / grep. Nothing staged or committed; no git command run inside jlens-qwen36/ (its working tree and its `.git/index` are read as plain files); the lab's remote-tracking reflogs (`.git/logs/refs/remotes/`), the files not yet in history (pre-release section) and Homebrew's local formula index are read as plain files; nothing installed; no network access (so refs that exist only on GitHub are not visible here -- see the PI pre-flip steps).
- Coverage of the commits after the block's commit: this run scans HEAD `cf8eb5b9dd`, which includes the 3 commit(s) made after `bbc9ffe72f` (the concurrent PROPOSAL-m session's G-CAL commits: their subjects begin `m package` / `G-CAL`) (`c75d4d8aa3`, `bab921ce52`, `cf8eb5b9dd`). It is still a snapshot: the final re-run at the release commit (PI pre-flip step 1, under (v)) is required.
- Redaction form: `xxxx...[len N]#hhhhhhhh` = first 4 characters, the value's length, the first 8 hex of sha256(value) (the routing's form -- first 4 + length + sha256[:8] -- with the punctuation the sibling raws and both checkers quote). SSH-port-class values (every 4-5 digit number on an ssh/port/alias line, whatever its verdict) use `lenN:hhhhhhhh` -- the length and the first 8 hex of sha256 only, no digit of the value. No candidate secret, RunPod id or volume name (nor the name's stem), IP address, SSH port, SSH key fingerprint, laptop/container hostname or personal email appears verbatim in this file or its JSON (asserted by the script before writing). A value of 4 characters or fewer is printed in full by the generic form; only non-sensitive values reach it (listed in the round-2 values-check).
- Caveat (enumeration; round 3, computed per sensitive value): the hash in the redacted form is a 32-bit prefix, so a value whose hidden characters have few possible values can be recovered by brute force (expected chance matches = candidates / 2^32), and a value built from words by a word-list search, whatever its length. Recoverable by brute force: runpod_volume_id (1 value(s); 6 hidden of an alphabet of 36: 36^6 = 2.18e+09 candidates, ~0.51 chance matches); container_hostname (1 value(s); 8 hidden of an alphabet of 16: 16^8 = 4.29e+09 candidates, ~1 chance matches); ssh_port (5 value(s); 5 hidden of an alphabet of 10: 10^5 = 1.00e+05 candidates, ~2.3e-05 chance matches). Open to a word-list search: runpod_volume_name (1), passphrase_shaped (1), runpod volume name stem (1), identity email, public in the commit headers (3), laptop hostname (1). Not recoverable by brute force: runpod_pod_id (2 value(s); 10 hidden of an alphabet of 36: 36^10 = 3.66e+15 candidates, ~8.5e+05 chance matches); claude_session_or_artifact_link (1 value(s); 24 hidden of an alphabet of 62: 62^24 = 1.04e+43 candidates, ~2.4e+33 chance matches); SSH signing-key fingerprint (1 value(s); 43 hidden of an alphabet of 64: 64^43 = 4.63e+77 candidates, ~1.1e+68 chance matches). Every one of these 18 values is in the history being published -- verbatim (17 of them, in blobs, messages or commit headers), or derivable from published material (SSH signing-key fingerprint: the fingerprint string occurs 0 times, but it is the SHA-256 of the public key embedded in every gpgsig header) -- so the form protects only this raw, not the release.

## Scope

Refs scanned (everything reachable from any of them; `--all` at the pinned moment):

| ref | object | type | ancestor of origin/main |
|---|---|---|---|
| `refs/heads/main` | `cf8eb5b9dd` | commit | yes |
| `refs/remotes/origin/claude/handoff-doc-next-steps-oeccd1` | `79868f7583` | commit | yes |
| `refs/remotes/origin/main` | `cf8eb5b9dd` | commit | yes |
| `refs/tags/cycle-2-close` | `f597ea7961` | commit | yes |
| `refs/tags/cycle-4-close` | `2390272650` | tag | yes |

- Commits reachable: 307; trees: 1006; blobs: 1181 (1163 text, 18 binary); annotated tag objects: 1; text bytes scanned: 122,931,593; commit + tag messages scanned: 308; commit headers scanned: 307, tag headers: 1; binary blobs whose string content is scanned: 18 (208 npz members, 5 PNG chunks).
- Remote `origin` URL carries userinfo (credentials): no (`.git/config` is local and not released; checked only for completeness).

## (i) Secrets over the entire history

### (i-a) The block's primary scanners (not run) and its fallback, run as written

**The block's primary scanners have NOT been run over this history.** gitleaks and trufflehog are not installed on this machine (`which`: gitleaks not found, trufflehog not found). They are installable here via Homebrew (`/opt/homebrew/bin/brew` present; Homebrew's local formula index `~/Library/Caches/Homebrew/api/formula.jws.json`, cached 2026-08-06, read as a file -- no brew command, no network -- lists `gitleaks` 8.30.1 (MIT; bottle for `arm64_sequoia`: yes), `trufflehog` 3.96.0 (AGPL-3.0-only; bottle for `arm64_sequoia`: yes); macOS 15.6.1), but were not installed, because the PI's routing for this audit forbids installs without the PI's word. Block :77 runs its fallback only if the scanners are not installable; that condition does not hold, so running the fallback instead is a deviation from the block, recorded here for the PI. The block's fallback below, plus Code's blob-level scans in (i-b), stand in for the scanners; running them is PI pre-flip step 4 (under (v)).

The fallback, as written: `git log -p --all | grep -nEi '(api[_-]?key|secret|token|password|sk-[A-Za-z0-9]|rp_[A-Za-z0-9]|BEGIN (RSA|OPENSSH)|AKIA[0-9A-Z]{16})'` with `/usr/bin/grep` (BSD grep; its exit status read from its own process, not after a pipe).

- `git log -p --all` output: 70,058,328 bytes, 1,798,487 lines (newline count; the stream ends with a newline: yes).
- grep exit status: 0 (0 = matches found). Binary-file notice in grep output: no.
- **Total hit lines: 7782.** Python `re` (IGNORECASE) cross-check over the same bytes: 7782 lines (equal).
- Lines matching more than one alternative: 19.

| alternative | lines | occurrences |
|---|---|---|
| `api[_-]?key` | 0 | 0 |
| `secret` | 60 | 63 |
| `token` | 7440 | 8154 |
| `password` | 6 | 9 |
| `sk-[A-Za-z0-9]` | 287 | 297 |
| `rp_[A-Za-z0-9]` | 9 | 9 |
| `BEGIN (RSA|OPENSSH)` | 0 | 0 |
| `AKIA[0-9A-Z]{16}` | 0 | 0 |

Coverage limits of the fallback. (1) `git log -p` prints `Binary files ... differ` for binary blobs (the 18 .npz/.png blobs), so their contents never reach the grep; (i-b)'s binary-content scan below reads their string content (npz unicode members, printable-ASCII runs of every member, PNG text chunks). (2) HEAD's `.gitattributes` has 1 -diff/binary line(s) (`/data/m/ckpt/** -diff`); paths under `data/m/ckpt/` ever tracked: 1, so the limit now applies: `data/m/ckpt/G-CAL_qwen.json` (first added by `cf8eb5b9dd`, a commit after the base). `git log -p` prints 1 `Binary files ... differ` line(s) for them and none of their content, so their content never reaches the grep; (i-b) reads them as blobs (`9b6db93c` 29,608 bytes, scanned as text: yes, lines matching the fallback's pattern: 0). The round-2 raw, a snapshot at `bab921ce52`, said this limit had never applied; `cf8eb5b9dd` changed that after it was written -- the case PI pre-flip step 1's re-run at the release commit exists for. (3) `git log -p` does not print commit headers (signatures); (i-b) scans every commit and tag header in its own section.

Locators in (i-a) are `<commit8> <path>:<side><line>`, mapped from the grep's line number in the `git log -p --all` stream: side `+` = an added line (line number in the new file), `-` = a removed line (old file), ` ` = a context line, `m` = a commit-message line, `h` = a header line.

**Bulk triage by rule** (every occurrence assigned to exactly one rule; words are the maximal `[A-Za-z0-9_-]` run around the match):

| alternative | rule | occurrences | reason | most frequent words (count) | first locator |
|---|---|---|---|---|---|
| `password` | P1 the audit block, its preflight raw, and that commit's message | 8 | the block's N12(i) pattern and N12(iii) text about the continuity password, quoted or discussed; no password value appears on these lines | password (8) | bbc9ffe7 <commit message>:m13 |
| `password` | P2 model-generated text | 1 | 'password' inside a recorded model output (degenerate generation text) | fopassword-managermoth (1) | b6e8f3f5 data/olmo/b2r_qualify_instruct.json:+1369 |
| `rp_[A-Za-z0-9]` | R1 code identifier | 9 | a Python variable name containing 'rp_' (rp_ck, rp_bytes) in a self-test | rp_ck (7), rp_bytes (2) | 5f7b968c scripts/m_sessions.py:+799 |
| `secret` | S1 prose in model-generated text | 54 | 'secret(s)/secretly' as an English word in recorded model outputs (session transcripts / detection trials) | secrets (31), secret (21), secretly (2) | 7742e2c4 data/k/k1_sessions.json:+4941 |
| `secret` | S2 prose in documents | 9 | 'secret(s)/secretly' as an English word in design/log/raw documents (incl. the audit block discussing the scrub) | secret (5), secrets (2), secretly (2) | bbc9ffe7 <commit message>:m10 |
| `sk-[A-Za-z0-9]` | K1 in-word 'sk-' (task-/mask-/...) | 297 | the 'sk-' is the tail of a word such as task-round or mask-off, preceded by a letter; not a key prefix | task-round (68), mask-off (44), task-quality (23), task-disjointness (17), by-task-id (14), task-disjoint (13), task-line (11), mask-at-read (10) | cf8eb5b9 RESULTS.md:+183 |
| `token` | T1 LLM-token sense | 8152 | token/tokens/tokenizer/token_ids/... -- the language-model vocabulary sense, in prose, code identifiers or JSON field names | n_tokens (1252), transcript_tokens_after (1010), token (973), tokens (896), prefix_tokens_at_read (646), tokenizer (548), token_ids (230), 512-token (209) | cf8eb5b9 RESULTS.md:+126 |
| `token` | T2 credential-sense word, no value follows | 2 | a credential's name (e.g. HF_TOKEN) in prose or a library warning, with no '=', ':' or '=>' and no value after it; names a credential, discloses none | hf_token (2) | 2b21c72c results/raw/2026-08-19_cast_equality_sft.txt:+5 |

- Every locator of `token` / T2 credential-sense word, no value follows: 2b21c72c results/raw/2026-08-19_cast_equality_sft.txt:+5, 75939edb results/raw/2026-08-19_olmo_acquisition.txt:+3

**Credential-shaped hits, inspected individually** (`<word containing the alternative>` followed by `=`, `:` or `=>` and a value): 4100 occurrences on the hit lines, 115 distinct (key, value-class) groups; verdicts: FALSE-POSITIVE 4100. The JSON (`fallback.credential_shaped`) holds one record per distinct (key, operator, value, class, verdict, reason) with every locator; values are redacted unless numeric/boolean/structural and at most 8 characters. Grouped:

| key | value class | verdict | occurrences | first locator |
|---|---|---|---|---|
| `n_tokens` | number | FALSE-POSITIVE | 1240 | 7742e2c4 data/k/k1_reads.json:+164 |
| `transcript_tokens_after` | number | FALSE-POSITIVE | 1003 | 7742e2c4 data/k/k1_sessions.json:+325 |
| `prefix_tokens_at_read` | number | FALSE-POSITIVE | 589 | 5f7b968c valence_core/m/readrule.py:+815 |
| `prefix_tokens` | number | FALSE-POSITIVE | 192 | cc9db1df data/olmo/a2_baserates_base.json:+585 |
| `token_ids` | structure | FALSE-POSITIVE | 169 | a9e6a744 valence_core/regression/analysis.py:+1598 |
| `tokens_forced_end_to_first_read` | structure | FALSE-POSITIVE | 104 | 7742e2c4 data/k/k1_sessions.json:+620 |
| `n_prefix_tokens` | number | FALSE-POSITIVE | 84 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+50 |
| `n_tokens_uncached` | number | FALSE-POSITIVE | 84 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+51 |
| `n_tokens_cached` | number | FALSE-POSITIVE | 84 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+52 |
| `add_special_tokens` | bool/null | FALSE-POSITIVE | 70 | c75d4d8a results/raw/2026-10-08_m-gcal-build_review.txt:+130 |
| `max_tokens` | identifier | FALSE-POSITIVE | 61 | 988e5dfd results/raw/2026-10-07_m-gport_differences.md:+1731 |
| `retention_tokens` | structure | FALSE-POSITIVE | 45 | e186162d results/raw/2026-09-18_k1_stop_entry_valuescheck.txt:+1790 |
| `tokens` | number | FALSE-POSITIVE | 34 | 05c4636d results/raw/2026-10-06_m-v1.11_code_own_pass.txt:+193 |
| `max_tokens` | number | FALSE-POSITIVE | 28 | 939905ae results/raw/2026-10-05_m-v1.9_referent_check.txt:+5622 |
| `max_tokens` | word | FALSE-POSITIVE | 14 | 5f7b968c valence_core/m/testing.py:+200 |
| `token_id` | bool/null | FALSE-POSITIVE | 14 | b0b2e606 data/format/neutral_label_selection.json:+28 |
| `token_id` | number | FALSE-POSITIVE | 12 | e9b50226 results/raw/2026-09-09_k_commit_format_recon_selftest.txt:+12 |
| `token` | word | FALSE-POSITIVE | 11 | bbc9ffe7 AUDIT-note-release-v1_2.md:+46 |
| `tokens_forced_end_to_first_read` | bool/null | FALSE-POSITIVE | 10 | 7742e2c4 data/k/k1_sessions.json:+3666 |
| `add_special_tokens` | word | FALSE-POSITIVE | 9 | c75d4d8a valence_core/m/gcal.py:+1704 |
| `prefix_tokens_at_read` | structure | FALSE-POSITIVE | 9 | 5f7b968c results/raw/2026-10-06_m-build_review.txt:+2043 |
| `add_special_tokens` | identifier | FALSE-POSITIVE | 9 | 05c4636d results/raw/2026-10-06_m-v1.11_referent_check.txt:+4230 |
| `tokens_last_steered_to_read` | structure | FALSE-POSITIVE | 9 | 7da95097 data/echo/stageB_analysis_samefolds.json:+4518 |
| `tokenizer` | number | FALSE-POSITIVE | 9 | cc9db1df results/raw/2026-08-23_a2_rerun.txt:+5 |
| `prefix_tokens_at_read` | word | FALSE-POSITIVE | 8 | c75d4d8a results/raw/2026-10-08_m-gcal-build_selftest.txt:+467 |
| `min_resp_tokens` | number | FALSE-POSITIVE | 7 | c07a5e06 CLAUDE.md:-178 |
| `tokens` | word | FALSE-POSITIVE | 6 | 988e5dfd results/raw/2026-10-07_m-gport_differences.md:+1646 |
| `token_ids` | code-expression | FALSE-POSITIVE | 6 | 5f7b968c valence_core/m/testing.py:+213 |
| `tokens_forced_end_to_first_read` | word | FALSE-POSITIVE | 6 | 3c233208 data/format/format_recon_analysis.json:+1211 |
| `s_per_token_uncached` | number | FALSE-POSITIVE | 6 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+34 |
| `s_per_token_cached` | number | FALSE-POSITIVE | 6 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+35 |
| `multi_token_cases` | number | FALSE-POSITIVE | 6 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+39 |
| `s_per_token_uncached_multi` | number | FALSE-POSITIVE | 6 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+41 |
| `s_per_token_cached_multi` | number | FALSE-POSITIVE | 6 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+42 |
| `speedup_multi_token` | number | FALSE-POSITIVE | 6 | 7bffb676 data/olmo/cached_gen_WITHDRAWN_v2.json:+43 |
| `multi-token` | word | FALSE-POSITIVE | 6 | a41fe989 results/raw/2026-08-24_cached_gate.txt:+21 |
| `token` | label | FALSE-POSITIVE | 5 | 5f7b968c valence_core/m/audit.py:+840 |
| `g1_labela_token_m` | label | FALSE-POSITIVE | 5 | e186162d results/raw/2026-09-12_addendum-k1-v1.1_referent_check.txt:+1310 |
| `token_id` | code-reference | FALSE-POSITIVE | 5 | b0b2e606 scripts/format_recon.py:+269 |
| `token_idx` | number | FALSE-POSITIVE | 5 | 720a1045 data/olmo/b2_concepts_base.json:+35 |
| `token_ids` | word | FALSE-POSITIVE | 5 | b30a6284 scripts/box_a1_repair_screen.py:+133 |
| `transcript_tokens_final` | structure | FALSE-POSITIVE | 4 | 07224b6b data/format/format_recon_timing.json:+253 |
| `n_tokens` | code-expression | FALSE-POSITIVE | 4 | 745c1966 scripts/box_b2r_sampling_smoke.py:-98 |
| `max_choice_prefix_tokens` | number | FALSE-POSITIVE | 4 | cc9db1df data/olmo/a2_baserates_base.json:+444 |
| `max_tokens` | code-reference | FALSE-POSITIVE | 3 | c75d4d8a valence_core/m/gcal.py:+862 |
| `prefix_tokens_at_read` | code-expression | FALSE-POSITIVE | 3 | 5f7b968c results/raw/2026-10-06_m-build_pins.txt:+520 |
| `tokenizer-only` | word | FALSE-POSITIVE | 3 | 5f7b968c results/raw/2026-10-06_m-build_valuescheck.txt:+96 |
| `tokenizer` | word | FALSE-POSITIVE | 3 | 5f7b968c results/raw/2026-10-06_m-build_valuescheck.txt:+884 |
| `neutral_token_id` | number | FALSE-POSITIVE | 3 | b0b2e606 valence_core/formats/recon.py:-124 |
| `tokenizers` | word | FALSE-POSITIVE | 2 | 5f7b968c results/raw/2026-10-06_m-build_valuescheck_pass2.txt:+836 |
| `retention_tokens` | identifier | FALSE-POSITIVE | 2 | e186162d results/raw/2026-09-18_addendum-k1-1b_retention_geometry.txt:+10 |
| `transcript_tokens_after` | code-expression | FALSE-POSITIVE | 2 | 07224b6b valence_core/formats/recon.py:+305 |
| `prefix_tokens` | code-expression | FALSE-POSITIVE | 2 | 07224b6b valence_core/formats/recon.py:+317 |
| `n_tokens` | word | FALSE-POSITIVE | 2 | 10a0723e valence_core/echo/spans.py:+139 |
| `round_token_counts` | structure | FALSE-POSITIVE | 2 | 10f6f3a2 data/e2d/tstep_check_f010.json:+40 |
| `max_new_tokens` | number | FALSE-POSITIVE | 2 | 5c1b161c data/configs/b2r_step1.json:+73 |
| `n_tokens_uncached` | code-expression | FALSE-POSITIVE | 2 | c0f07f7c scripts/box_cached_gen_smoke.py: 188 |
| `n_tokens_cached` | code-expression | FALSE-POSITIVE | 2 | c0f07f7c scripts/box_cached_gen_smoke.py: 189 |
| `s_per_token_uncached` | identifier | FALSE-POSITIVE | 2 | c0f07f7c scripts/box_cached_gen_smoke.py: 211 |
| `s_per_token_cached` | identifier | FALSE-POSITIVE | 2 | c0f07f7c scripts/box_cached_gen_smoke.py: 212 |
| `b2_max_tokens` | number | FALSE-POSITIVE | 2 | 024e8e5b data/olmo/a5_budget.json:+31 |
| `session_tokens` | word | FALSE-POSITIVE | 2 | 024e8e5b scripts/a5_budget.py:+90 |
| `tokenizer` | structure | FALSE-POSITIVE | 2 | 1f83afcf scripts/box_a2_baserates.py:+289 |
| `prefix_tokens` | word | FALSE-POSITIVE | 1 | 5f7b968c valence_core/m/scaffold.py:+398 |
| `autotokenizer` | number | FALSE-POSITIVE | 1 | 05c4636d results/raw/2026-10-06_m-v1.11_referent_check.txt:+6569 |
| `tokenizer` | identifier | FALSE-POSITIVE | 1 | 5db07207 results/raw/2026-10-04_m-v1.8_referent_check.txt:+3958 |
| `max_tokens` | code-expression | FALSE-POSITIVE | 1 | 87a11671 results/raw/2026-10-04_m-v1.7_referent_check.txt:+3279 |
| `g1_labelb_token_m` | label | FALSE-POSITIVE | 1 | 3be4a631 results/raw/2026-09-11_addendum_k1_referent_check.txt:+447 |
| `token` | number | FALSE-POSITIVE | 1 | 3be4a631 results/raw/2026-09-11_addendum_k1_referent_check.txt:+502 |
| `g1_labela_token_m` | structure | FALSE-POSITIVE | 1 | 7742e2c4 data/k/k1_analysis.json:+64 |
| `g1_labelb_token_m` | structure | FALSE-POSITIVE | 1 | 7742e2c4 data/k/k1_analysis.json:+192 |
| `g1_labela_token_r_comparator` | structure | FALSE-POSITIVE | 1 | 7742e2c4 data/k/k1_analysis.json:+320 |
| `g1_labelb_token_r_comparator` | structure | FALSE-POSITIVE | 1 | 7742e2c4 data/k/k1_analysis.json:+448 |
| `g1_labelb_token_m` | word | FALSE-POSITIVE | 1 | 7742e2c4 results/raw/2026-09-11_k_stage1_entry_valuescheck.txt:+1482 |
| `g1_labela_token_r_comparator` | word | FALSE-POSITIVE | 1 | 7742e2c4 results/raw/2026-09-11_k_stage1_entry_valuescheck.txt:+1484 |
| `g1_labelb_token_r_comparator` | word | FALSE-POSITIVE | 1 | 7742e2c4 results/raw/2026-09-11_k_stage1_entry_valuescheck.txt:+1486 |
| `tokens` | label | FALSE-POSITIVE | 1 | 3c233208 results/raw/2026-09-07_format_recon_entry_valuescheck.txt:+29 |
| `prefix_tokens_at_read` | identifier | FALSE-POSITIVE | 1 | 07224b6b valence_core/formats/recon.py:+332 |
| `n_tokens_full` | number | FALSE-POSITIVE | 1 | 10a0723e data/echo/timing.json:+3 |
| `n_tokens_first_choice_prefix` | number | FALSE-POSITIVE | 1 | 10a0723e data/echo/timing.json:+4 |
| `n_steered_tokens_full` | number | FALSE-POSITIVE | 1 | 10a0723e data/echo/timing.json:+6 |
| `n_tokens_full` | identifier | FALSE-POSITIVE | 1 | 10a0723e scripts/recon_echo.py:+273 |
| `n_tokens_first_choice_prefix` | code-expression | FALSE-POSITIVE | 1 | 10a0723e scripts/recon_echo.py:+274 |
| `n_steered_tokens_full` | code-expression | FALSE-POSITIVE | 1 | 10a0723e scripts/recon_echo.py:+275 |
| `_bracket_token` | code-expression | FALSE-POSITIVE | 1 | 12237517 valence_core/e2d/contentclass.py:+82 |
| `tokens` | structure | FALSE-POSITIVE | 1 | 7dad4d6c scripts/e2d_judge_port.py:+69 |
| `first-token-only` | number | FALSE-POSITIVE | 1 | 77e0fe65 <commit message>:m5 |
| `round_token_counts` | word | FALSE-POSITIVE | 1 | 77e0fe65 scripts/e2d_tstep_check.py:+188 |
| `default_max_tokens` | number | FALSE-POSITIVE | 1 | f4b402a6 RESULTS.md:+37 |
| `n_prefix_tokens` | code-expression | FALSE-POSITIVE | 1 | c0f07f7c scripts/box_cached_gen_smoke.py:+187 |
| `multi_token_cases` | code-expression | FALSE-POSITIVE | 1 | c0f07f7c scripts/box_cached_gen_smoke.py:+215 |
| `s_per_token_uncached_multi` | structure | FALSE-POSITIVE | 1 | c0f07f7c scripts/box_cached_gen_smoke.py:+216 |
| `s_per_token_cached_multi` | structure | FALSE-POSITIVE | 1 | c0f07f7c scripts/box_cached_gen_smoke.py:+217 |
| `speedup_multi_token` | structure | FALSE-POSITIVE | 1 | c0f07f7c scripts/box_cached_gen_smoke.py:+218 |
| `budgets_at_default_session_tokens` | structure | FALSE-POSITIVE | 1 | 024e8e5b data/olmo/a5_budget.json:+43 |
| `tokens_each` | number | FALSE-POSITIVE | 1 | 024e8e5b data/olmo/a5_budget.json:+50 |
| `default_session_tokens` | number | FALSE-POSITIVE | 1 | 024e8e5b data/olmo/a5_budget.json:+77 |
| `sensitivity_by_session_tokens` | structure | FALSE-POSITIVE | 1 | 024e8e5b data/olmo/a5_budget.json:+78 |
| `tokens_each` | identifier | FALSE-POSITIVE | 1 | 024e8e5b scripts/a5_budget.py:+123 |
| `b2_max_tokens` | identifier | FALSE-POSITIVE | 1 | 024e8e5b scripts/a5_budget.py:+203 |
| `budgets_at_default_session_tokens` | code-expression | FALSE-POSITIVE | 1 | 024e8e5b scripts/a5_budget.py:+209 |
| `default_session_tokens` | code-reference | FALSE-POSITIVE | 1 | 024e8e5b scripts/a5_budget.py:+210 |
| `sensitivity_by_session_tokens` | word | FALSE-POSITIVE | 1 | 024e8e5b scripts/a5_budget.py:+211 |
| `token_ids` | identifier | FALSE-POSITIVE | 1 | 1f83afcf scripts/box_a2_baserates.py:+318 |
| `max_choice_prefix_tokens` | code-expression | FALSE-POSITIVE | 1 | 1f83afcf scripts/box_a2_baserates.py:+398 |
| `tokenizer_usable` | structure | FALSE-POSITIVE | 1 | 1c8f5e17 data/e2b/h3_tagscreen.json:+32 |
| `tokenizer_dropped` | structure | FALSE-POSITIVE | 1 | 1c8f5e17 data/e2b/h3_tagscreen.json:+122 |
| `screen_roster_tokenizer` | word | FALSE-POSITIVE | 1 | 6897b672 <commit message>:m38 |
| `tokenizer_usable` | word | FALSE-POSITIVE | 1 | 6897b672 scripts/h3_tagscreen_qwen.py:+91 |
| `tokenizer_dropped` | word | FALSE-POSITIVE | 1 | 6897b672 scripts/h3_tagscreen_qwen.py:+91 |
| `class_token_ids` | structure | FALSE-POSITIVE | 1 | a871cdd8 data/e0/e0_b1_markers.meta.json:+12 |
| `tokenizer` | public-model-id | FALSE-POSITIVE | 1 | 947b9ead results/raw/2026-08-18_window_coverage_audit.txt:+5 |
| `next_token_probs` | code-reference | FALSE-POSITIVE | 1 | a4fd449e valence_core/readout.py:+129 |
| `next_token_probs` | code-expression | FALSE-POSITIVE | 1 | a4fd449e valence_core/readout.py:+153 |
| `next-token` | number | FALSE-POSITIVE | 1 | e1fd53f3 <commit message>:m9 |

### (i-b) Precise scan over every reachable blob and every commit/tag message

Input: `git rev-list --objects <refs> | git cat-file --batch` -- 1163 text blobs (every version of every text file ever committed) plus 308 commit/tag messages. The 18 binary blobs are not regex-scanned as text; their string content is scanned in the binary-content subsection below, and they are listed under (v)/(iv) and in the JSON (`binary_blobs`). Commit and tag headers are scanned in their own subsection below. Locator = the earliest commit introducing the blob, the path, the line within the blob. Patterns 1-17 are the builder's; 18-31 were added at the first values-check (the first checker's extended set); 32-33 at the second (base64 key-material markers, so a key body without its PEM armor is caught -- see the entropy note below).

| pattern | distinct values | occurrences (summed over blob versions + messages) | at HEAD | new since base | verdicts |
|---|---|---|---|---|---|
| aws_access_key_id (AKIA/ASIA) | 0 | 0 | 0 | 0 | - |
| private_key_pem (RSA/OPENSSH/EC/DSA/PGP/ENCRYPTED) | 0 | 0 | 0 | 0 | - |
| anthropic_key sk-ant- | 0 | 0 | 0 | 0 | - |
| openai_key sk-/sk-proj- | 0 | 0 | 0 | 0 | - |
| huggingface_token hf_ | 0 | 0 | 0 | 0 | - |
| github_token ghp_/gho_/ghu_/ghs_/ghr_/github_pat_ | 0 | 0 | 0 | 0 | - |
| slack_token xox[abpr]- | 0 | 0 | 0 | 0 | - |
| runpod_api_key rpa_ | 0 | 0 | 0 | 0 | - |
| runpod_key_shape rp_ (20+) | 0 | 0 | 0 | 0 | - |
| credential_env_assignment (RUNPOD_API_KEY, HF_TOKEN, ...) | 0 | 0 | 0 | 0 | - |
| wandb_key (40 hex after wandb/api-key context) | 0 | 0 | 0 | 0 | - |
| google_api_key AIza | 0 | 0 | 0 | 0 | - |
| generic_assignment | 1 | 1 | 1 | 0 | FALSE-POSITIVE 1 |
| bearer_header | 0 | 0 | 0 | 0 | - |
| netrc_shape | 0 | 0 | 0 | 0 | - |
| aws_credentials_file_shape | 0 | 0 | 0 | 0 | - |
| url_with_userinfo | 0 | 0 | 0 | 0 | - |
| jwt | 0 | 0 | 0 | 0 | - |
| stripe_key sk_/pk_/rk_ live/test | 0 | 0 | 0 | 0 | - |
| slack_webhook | 0 | 0 | 0 | 0 | - |
| discord_webhook | 0 | 0 | 0 | 0 | - |
| sendgrid_key SG. | 0 | 0 | 0 | 0 | - |
| telegram_bot_token | 0 | 0 | 0 | 0 | - |
| pypi_token | 0 | 0 | 0 | 0 | - |
| npm_token | 0 | 0 | 0 | 0 | - |
| google_oauth ya29. | 0 | 0 | 0 | 0 | - |
| upper32 (legacy RunPod-key shape: 32-40 uppercase+digit) | 0 | 0 | 0 | 0 | - |
| putty_private_key | 0 | 0 | 0 | 0 | - |
| url_secret_query_param | 0 | 0 | 0 | 0 | - |
| quoted_secretish_assignment | 41 | 54 | 43 | 2 | FALSE-POSITIVE 41 |
| pgp_signature_or_key_block | 0 | 0 | 0 | 0 | - |
| ssh_key_material_base64 (openssh-key-v1 / ssh-rsa / ssh-ed25519 / ecdsa / ssh-dss markers) | 0 | 0 | 0 | 0 | - |
| pkcs_der_base64 (a run starting MII, 64+ characters: DER-encoded PKCS#1/#8 key or X.509 body) | 0 | 0 | 0 | 0 | - |

Patterns (verbatim, Python `re`):

- aws_access_key_id (AKIA/ASIA): `(?<![A-Za-z0-9])(?:AKIA|ASIA)[0-9A-Z]{16}(?![A-Za-z0-9])`
- private_key_pem (RSA/OPENSSH/EC/DSA/PGP/ENCRYPTED): `-----BEGIN (?:(?:RSA|OPENSSH|EC|DSA|PGP|ENCRYPTED) )?PRIVATE KEY(?: BLOCK)?-----`
- anthropic_key sk-ant-: `sk-ant-[A-Za-z0-9_\-]{20,}`
- openai_key sk-/sk-proj-: `(?<![A-Za-z0-9_\-])sk-(?!ant-)(?:proj-|svcacct-|admin-)?[A-Za-z0-9_\-]{20,}`
- huggingface_token hf_: `(?<![A-Za-z0-9_])hf_[A-Za-z0-9]{30,}`
- github_token ghp_/gho_/ghu_/ghs_/ghr_/github_pat_: `(?<![A-Za-z0-9_])(?:(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,})`
- slack_token xox[abpr]-: `(?<![A-Za-z0-9])xox[abpr]-[A-Za-z0-9\-]{10,}`
- runpod_api_key rpa_: `(?<![A-Za-z0-9_])rpa_[A-Za-z0-9]{20,}`
- runpod_key_shape rp_ (20+): `(?<![A-Za-z0-9_])rp_[A-Za-z0-9]{20,}`
- credential_env_assignment (RUNPOD_API_KEY, HF_TOKEN, ...): `(?i)\b(?:RUNPOD_API_KEY|HF_TOKEN|HUGGING_FACE_HUB_TOKEN|HUGGINGFACE_TOKEN|ANTHROPIC_API_KEY|OPENAI_API_KEY|WANDB_API_KEY|GITHUB_TOKEN|GH_TOKEN|AWS_SECRET_ACCESS_KEY|AWS_ACCESS_KEY_ID|AWS_SESSION_TOKEN)\b\s*[:=]\s*(?P<v>\S+)`
- wandb_key (40 hex after wandb/api-key context): `(?i)(?:wandb|api[_-]?key)[^\n]{0,40}?(?<![0-9a-f])(?P<v>[0-9a-f]{40})(?![0-9a-f])`
- google_api_key AIza: `(?<![A-Za-z0-9_\-])AIza[0-9A-Za-z_\-]{35}`
- generic_assignment: `(?i)(api[_-]?key|secret|token|password|passwd|pwd|auth)\s*[:=]\s*['\"]?(?P<v>[A-Za-z0-9_\-/+=.]{16,})`
- bearer_header: `(?i)\bbearer\s+(?P<v>[A-Za-z0-9._\-+/=]{16,})`
- netrc_shape: `(?im)^[ \t]*machine[ \t]+\S+[ \t]+(?:login[ \t]+\S+[ \t]+)?password[ \t]+\S+`
- aws_credentials_file_shape: `(?im)^[ \t]*aws_(?:access_key_id|secret_access_key|session_token)[ \t]*=[ \t]*(?P<v>\S+)`
- url_with_userinfo: `\b[a-zA-Z][a-zA-Z0-9+.\-]{0,15}://(?P<v>[^\s/:@'\"<>]{1,64}:[^\s/@'\"<>]{1,128})@[^\s/'\"<>]+`
- jwt: `\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}`
- stripe_key sk_/pk_/rk_ live/test: `\b(?:sk|pk|rk)_(?:live|test)_[A-Za-z0-9]{10,}`
- slack_webhook: `hooks\.slack\.com/services/[A-Za-z0-9/_\-]+`
- discord_webhook: `discord(?:app)?\.com/api/webhooks/[0-9]+/[A-Za-z0-9_\-]+`
- sendgrid_key SG.: `\bSG\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,}`
- telegram_bot_token: `(?<!\d)\d{8,10}:[A-Za-z0-9_\-]{35}(?![A-Za-z0-9_\-])`
- pypi_token: `\bpypi-AgE[A-Za-z0-9_\-]{20,}`
- npm_token: `\bnpm_[A-Za-z0-9]{36}\b`
- google_oauth ya29.: `\bya29\.[0-9A-Za-z_\-]{20,}`
- upper32 (legacy RunPod-key shape: 32-40 uppercase+digit): `(?<![A-Za-z0-9])(?=[A-Z0-9]*\d)(?=[A-Z0-9]*[A-Z])[A-Z0-9]{32,40}(?![A-Za-z0-9])`
- putty_private_key: `PuTTY-User-Key-File-\d`
- url_secret_query_param: `[?&](?:token|key|api_key|apikey|access_token|auth|sig|signature|password|secret)=(?P<v>[^&\s'\"<>]{8,})`
- quoted_secretish_assignment: `(?i)\b[\w\-]*(?:key|secret|token|passw(?:or)?d|passwd|pwd|credential|auth)[\w\-]*['\"]?\s*[:=]\s*['\"](?P<v>[^'\"\s]{12,})['\"]`
- pgp_signature_or_key_block: `-----BEGIN PGP (?:SIGNATURE|PUBLIC KEY BLOCK|PRIVATE KEY BLOCK)-----`
- ssh_key_material_base64 (openssh-key-v1 / ssh-rsa / ssh-ed25519 / ecdsa / ssh-dss markers): `(?<![A-Za-z0-9+/])(?=[A-Za-z0-9+/]{60})[A-Za-z0-9+/]*(?:b3BlbnNzaC1rZXktdjE|AAAAB3NzaC1yc2E|AAAAC3NzaC1lZDI1NTE5|AAAAE2VjZHNhLXNoYTItbmlzdHA|AAAAB3NzaC1kc3M)[A-Za-z0-9+/]*={0,2}`
- pkcs_der_base64 (a run starting MII, 64+ characters: DER-encoded PKCS#1/#8 key or X.509 body): `(?<![A-Za-z0-9+/])MII[A-Za-z0-9+/]{61,}={0,2}(?![A-Za-z0-9+/=])`

Every precise-pattern hit, triaged individually (one row per distinct value):

| pattern | value (redacted) | verdict | reason | occurrences | blobs/messages | at HEAD (paths) | first locator |
|---|---|---|---|---|---|---|---|
| generic_assignment | `====...[len 63]#087998a4` | FALSE-POSITIVE | a row of '=' separator characters on the line after the word 'single-token' (the pattern's \s spans the newline); not a value | 1 | 1 | 1 (results/raw/2026-07-18_state_space_validation.txt) | 91c6b20e results/raw/2026-07-18_state_space_validation.txt:26 |
| quoted_secretish_assignment | `span...[len 14]#4ddb9449` | FALSE-POSITIVE | identifier: a snake_case / UPPER_CASE program identifier (variable or constant name) | 2 | 2 | 1 (valence_core/neighbors.py) | 5361b8b4 valence_core/neighbors.py:87 |
| quoted_secretish_assignment | `span...[len 14]#1f4d4fd0` | FALSE-POSITIVE | identifier: a snake_case / UPPER_CASE program identifier (variable or constant name) | 2 | 2 | 1 (valence_core/neighbors.py) | 5361b8b4 valence_core/neighbors.py:97 |
| quoted_secretish_assignment | `span...[len 13]#285ff1dc` | FALSE-POSITIVE | identifier: a snake_case / UPPER_CASE program identifier (variable or constant name) | 2 | 2 | 1 (valence_core/neighbors.py) | 5361b8b4 valence_core/neighbors.py:144 |
| quoted_secretish_assignment | `span...[len 18]#823e5211` | FALSE-POSITIVE | identifier: a snake_case / UPPER_CASE program identifier (variable or constant name) | 9 | 9 | 1 (valence_core/regression/analysis.py) | e1b5c777 valence_core/regression/analysis.py:720 |
| quoted_secretish_assignment | `e2d_...[len 23]#a1f6fdff` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:6 |
| quoted_secretish_assignment | `e2d_...[len 37]#b2e03fcb` | FALSE-POSITIVE | identifier: a snake_case / UPPER_CASE program identifier (variable or constant name) | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:14 |
| quoted_secretish_assignment | `e2d-...[len 37]#80cfedca` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:22 |
| quoted_secretish_assignment | `e2d_...[len 41]#e4822219` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:30 |
| quoted_secretish_assignment | `e2d_...[len 48]#505908e9` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:46 |
| quoted_secretish_assignment | `e2d_...[len 32]#19f407f9` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:54 |
| quoted_secretish_assignment | `e2d_...[len 64]#2a26782c` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:62 |
| quoted_secretish_assignment | `e2d_...[len 41]#3c2d0198` | FALSE-POSITIVE | identifier: a snake_case / UPPER_CASE program identifier (variable or constant name) | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:70 |
| quoted_secretish_assignment | `e2d-...[len 71]#c90b393b` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/e2d/closure_valuescheck.json) | 1bdf16c1 data/e2d/closure_valuescheck.json:94 |
| quoted_secretish_assignment | `c2_f...[len 14]#7f3dc525` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (results/raw/2026-09-12_addendum-k1-v1.1_referent_check.txt) | e186162d results/raw/2026-09-12_addendum-k1-v1.1_referent_check.txt:1827 |
| quoted_secretish_assignment | `,sum...[len 20]#117e2e19` | FALSE-POSITIVE | code-expression: a function call / subscript / type annotation in source code | 2 | 2 | 2 (results/raw/2026-10-05_m-v1.10_code_own_pass.txt, results/raw/2026-10-06_m-v1.11_code_own_pass.txt) | 9510af7e results/raw/2026-10-05_m-v1.10_code_own_pass.txt:405 |
| quoted_secretish_assignment | `m-sc...[len 32]#3d633ad7` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-dpo_campaign_A0-OLMo-dpo.json) | 5f7b968c data/m/schedules/OLMo-dpo_campaign_A0-OLMo-dpo.json:2214 |
| quoted_secretish_assignment | `m-sc...[len 33]#4eb9c976` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-dpo_campaign_A0s-OLMo-dpo.json) | 5f7b968c data/m/schedules/OLMo-dpo_campaign_A0s-OLMo-dpo.json:966 |
| quoted_secretish_assignment | `m-sc...[len 35]#09b7a86f` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-dpo_qual_A0-OLMo-dpo.json) | 5f7b968c data/m/schedules/OLMo-dpo_qual_A0-OLMo-dpo.json:13 |
| quoted_secretish_assignment | `m-sc...[len 36]#f5613cc2` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-dpo_qual_A0s-OLMo-dpo.json) | 5f7b968c data/m/schedules/OLMo-dpo_qual_A0s-OLMo-dpo.json:21 |
| quoted_secretish_assignment | `m-sc...[len 35]#ba1d428e` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-dpo_time_A0-OLMo-dpo.json) | 5f7b968c data/m/schedules/OLMo-dpo_time_A0-OLMo-dpo.json:6 |
| quoted_secretish_assignment | `m-sc...[len 36]#c10d3470` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-dpo_time_A0s-OLMo-dpo.json) | 5f7b968c data/m/schedules/OLMo-dpo_time_A0s-OLMo-dpo.json:6 |
| quoted_secretish_assignment | `m-sc...[len 42]#4c07bb41` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-instruct_campaign_A0-OLMo-instruct.json) | 5f7b968c data/m/schedules/OLMo-instruct_campaign_A0-OLMo-instruct.json:2214 |
| quoted_secretish_assignment | `m-sc...[len 43]#23692bcf` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-instruct_campaign_A0s-OLMo-instruct.json) | 5f7b968c data/m/schedules/OLMo-instruct_campaign_A0s-OLMo-instruct.json:966 |
| quoted_secretish_assignment | `m-sc...[len 45]#aaec17fe` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-instruct_qual_A0-OLMo-instruct.json) | 5f7b968c data/m/schedules/OLMo-instruct_qual_A0-OLMo-instruct.json:13 |
| quoted_secretish_assignment | `m-sc...[len 46]#43398a06` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-instruct_qual_A0s-OLMo-instruct.json) | 5f7b968c data/m/schedules/OLMo-instruct_qual_A0s-OLMo-instruct.json:21 |
| quoted_secretish_assignment | `m-sc...[len 45]#c8cf159c` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-instruct_time_A0-OLMo-instruct.json) | 5f7b968c data/m/schedules/OLMo-instruct_time_A0-OLMo-instruct.json:6 |
| quoted_secretish_assignment | `m-sc...[len 46]#9094c3a6` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-instruct_time_A0s-OLMo-instruct.json) | 5f7b968c data/m/schedules/OLMo-instruct_time_A0s-OLMo-instruct.json:6 |
| quoted_secretish_assignment | `m-sc...[len 32]#6d2f9572` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-sft_campaign_A0-OLMo-sft.json) | 5f7b968c data/m/schedules/OLMo-sft_campaign_A0-OLMo-sft.json:2214 |
| quoted_secretish_assignment | `m-sc...[len 33]#85ea7e0e` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-sft_campaign_A0s-OLMo-sft.json) | 5f7b968c data/m/schedules/OLMo-sft_campaign_A0s-OLMo-sft.json:966 |
| quoted_secretish_assignment | `m-sc...[len 35]#91b4a197` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-sft_qual_A0-OLMo-sft.json) | 5f7b968c data/m/schedules/OLMo-sft_qual_A0-OLMo-sft.json:13 |
| quoted_secretish_assignment | `m-sc...[len 36]#e04412db` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-sft_qual_A0s-OLMo-sft.json) | 5f7b968c data/m/schedules/OLMo-sft_qual_A0s-OLMo-sft.json:21 |
| quoted_secretish_assignment | `m-sc...[len 35]#74aa7556` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-sft_time_A0-OLMo-sft.json) | 5f7b968c data/m/schedules/OLMo-sft_time_A0-OLMo-sft.json:6 |
| quoted_secretish_assignment | `m-sc...[len 36]#60559872` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/OLMo-sft_time_A0s-OLMo-sft.json) | 5f7b968c data/m/schedules/OLMo-sft_time_A0s-OLMo-sft.json:6 |
| quoted_secretish_assignment | `m-sc...[len 19]#d6669bbf` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/Q-F0_campaign_A0.json) | 5f7b968c data/m/schedules/Q-F0_campaign_A0.json:2630 |
| quoted_secretish_assignment | `m-sc...[len 20]#6e566e56` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/Q-F0_campaign_A0s.json) | 5f7b968c data/m/schedules/Q-F0_campaign_A0s.json:966 |
| quoted_secretish_assignment | `m-sc...[len 21]#0880f9b1` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/Q-F0_id_A0s.json) | 5f7b968c data/m/schedules/Q-F0_id_A0s.json:21 |
| quoted_secretish_assignment | `m-sc...[len 22]#b5c16551` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/Q-F0_qual_A0.json) | 5f7b968c data/m/schedules/Q-F0_qual_A0.json:13 |
| quoted_secretish_assignment | `m-sc...[len 23]#1cc9f46f` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/Q-F0_qual_A0s.json) | 5f7b968c data/m/schedules/Q-F0_qual_A0s.json:21 |
| quoted_secretish_assignment | `m-sc...[len 22]#3ee79f43` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/Q-F0_time_A0.json) | 5f7b968c data/m/schedules/Q-F0_time_A0.json:6 |
| quoted_secretish_assignment | `m-sc...[len 23]#c2d401d9` | FALSE-POSITIVE | a label built of words and short tokens (a check name, a schedule-key template, an axis name); the key word is part of a field name such as key / key_template / axis_key; no generated-looking segment | 1 | 1 | 1 (data/m/schedules/Q-F0_time_A0s.json) | 5f7b968c data/m/schedules/Q-F0_time_A0s.json:6 |
| quoted_secretish_assignment | `47ee...[len 64]#422c647a` | FALSE-POSITIVE | a hex digest (256-bit, sha1/sha256 length) under a key naming it as a hash (`key_set_sha256`); a content hash, not a credential | 2 | 2 | 2 (data/m/ckpt/G-CAL_qwen.json, data/m/gates/G-CAL_completability_qwen.json) | cf8eb5b9 data/m/ckpt/G-CAL_qwen.json:1 |

**High-entropy strings in an assignment or header context** (a maximal run `[A-Za-z0-9+/=_-]{32,}` whose left context is `<key>["']? *[:=] *["']?` (key `[A-Za-z_][A-Za-z0-9_.-]{0,60}`) or an Authorization/Bearer/X-Api-Key/api-key/private-token header; Shannon entropy over the string's characters, bar > 4.0 bits/char):

- Candidates in context: base64-alphabet 289, hex-only 136. Over 4.0 bits/char: base64 168, hex 0. Note: a hex-only string cannot exceed log2(16) = 4.0 bits/char, so the > 4.0 bar never fires on hex by construction; hex in a credential context is covered by the wandb/40-hex pattern and by the generic-assignment pattern above.
- Distinct values over 4.0: 49; verdicts: FALSE-POSITIVE 43, LOCAL-PATH 6. By reason:

| verdict | reason | distinct values |
|---|---|---|
| FALSE-POSITIVE | a file path (separator-delimited readable words) | 37 |
| LOCAL-PATH | a local temporary path ((/private)/tmp or (/private)/var/folders) in a recorded message; carries an OS-generated folder name or a session UUID; not a credential | 6 |
| FALSE-POSITIVE | a snake/kebab-case identifier or label built of readable words | 3 |
| FALSE-POSITIVE | an environment-variable assignment of a repository-relative lens file path inside a recorded command line | 1 |
| FALSE-POSITIVE | a macOS per-user temporary-directory path (an OS-generated folder name) inside a self-test message; not a credential | 1 |
| FALSE-POSITIVE | embedded base64 image data (notebook output / data URI) | 1 |

**Context-free high-entropy runs over every text blob and message (no assignment context needed)** ((a) maximal runs `[A-Za-z0-9+/_-]{24,}` (optional `=` padding) containing an uppercase letter, a lowercase letter and a digit, Shannon entropy > 4.3 bits/char; (b) maximal runs `[a-z0-9]{20,}` bounded by non-alphanumerics, with >= 3 digits and >= 3 letters, not hex-only, entropy > 3.5):

- Distinct values: 123; occurrences: 601 (new since base: 57); verdicts: FALSE-POSITIVE 67, LOCAL-PATH 55, IDENTIFIER 1.

| verdict | reason | distinct values | occurrences |
|---|---|---|---|
| FALSE-POSITIVE | a file path or path fragment (slash-separated readable segments; any long segment is a hex hash or UUID part) | 58 | 460 |
| LOCAL-PATH | part of a local temporary path ((/private)/tmp or (/private)/var/folders) quoted in a raw; carries a session UUID or an OS-generated folder name; not a credential | 53 | 112 |
| FALSE-POSITIVE | a label or identifier made of words, numbers and short tokens (no generated-looking segment) | 6 | 15 |
| LOCAL-PATH | part of a ~/.claude/projects/<project>/<session-uuid> path (Claude Code's local transcript store) quoted in a raw; carries a session UUID; not a credential | 1 | 1 |
| FALSE-POSITIVE | a slash-separated list of verdict labels in a referent-check raw; not a path and not a value | 1 | 1 |
| FALSE-POSITIVE | a macOS per-user temporary-directory path (an OS-generated folder name) inside a self-test message; not a credential | 1 | 3 |
| LOCAL-PATH | the per-launch id in a local Jupyter kernel's runtime connection-file name, inside a process list that a preflight refusal printed; the file name is not the kernel's key; not a credential | 1 | 1 |
| FALSE-POSITIVE | embedded base64 image data (notebook output / data URI) | 1 | 1 |
| IDENTIFIER | part of the Claude Code session URL already listed under (ii) (the run is split at the '.' of claude.ai); not a credential | 1 | 7 |

Values other than paths, individually:

| value (redacted) | run | entropy | verdict | reason | occurrences | first locator |
|---|---|---|---|---|---|---|
| `iVBO...[len 51264]#ebffaa4c` | mixed | 5.99 | FALSE-POSITIVE | embedded base64 image data (notebook output / data URI) | 1 | 947b9ead paper_analysis.ipynb:21 |
| `ai/c...[len 40]#94ccd161` | mixed | 4.734 | IDENTIFIER | part of the Claude Code session URL already listed under (ii) (the run is split at the '.' of claude.ai); not a credential | 7 | d4f21d15 <commit message>:30 |
| `cb_R...[len 31]#88e7545b` | mixed | 4.414 | FALSE-POSITIVE | a label or identifier made of words, numbers and short tokens (no generated-looking segment) | 2 | e02619ce data/echo/stageB_analysis.json:1201 |
| `cb_R...[len 31]#a51ba879` | mixed | 4.414 | FALSE-POSITIVE | a label or identifier made of words, numbers and short tokens (no generated-looking segment) | 4 | e02619ce data/echo/stageB_analysis.json:1639 |
| `cb_R...[len 31]#aa06bba6` | mixed | 4.414 | FALSE-POSITIVE | a label or identifier made of words, numbers and short tokens (no generated-looking segment) | 5 | e02619ce data/echo/stageB_analysis.json:2077 |
| `cb_R...[len 31]#4a43f58e` | mixed | 4.414 | FALSE-POSITIVE | a label or identifier made of words, numbers and short tokens (no generated-looking segment) | 2 | e02619ce data/echo/stageB_analysis.json:2515 |
| `2026...[len 38]#5bd81065` | mixed | 4.462 | FALSE-POSITIVE | a label or identifier made of words, numbers and short tokens (no generated-looking segment) | 1 | ddee7301 results/raw/2026-09-12_handoff_valuescheck.txt:292 |
| `lock...[len 26]#ac76df4d` | mixed | 4.364 | FALSE-POSITIVE | a label or identifier made of words, numbers and short tokens (no generated-looking segment) | 1 | 9510af7e results/raw/2026-10-05_m-v1.10_referent_check.txt:12082 |
| `v337...[len 24]#22373092` | lower | 3.855 | LOCAL-PATH | the per-launch id in a local Jupyter kernel's runtime connection-file name, inside a process list that a preflight refusal printed; the file name is not the kernel's key; not a credential | 1 | bab921ce results/raw/2026-10-08_m-gcal_completability_qwen_refused-preflight.txt:5 |

### (i-b) Commit and tag headers

Every commit header (307) and tag header (1) -- the lines before the message: tree / parent / author / committer / gpgsig, or object / type / tag / tagger. `git log -p` never prints these; the message scan above reads only the part after the blank line. Header keys: `commit author` 307, `commit committer` 307, `commit gpgsig` 7, `commit parent` 306, `commit tree` 307, `tag object` 1, `tag tag` 1, `tag tagger` 1, `tag type` 1.

- Signed commits (gpgsig): 7; distinct signing keys: 1.
  - `-----BEGIN SSH SIGNATURE-----`: key type ssh-ed25519, namespace `git`, hash sha512, public-key fingerprint `SHA2...[len 50]#488bbe90` -- verdict PUBLIC-KEY: the signer's public key, embedded in every SSH signature and published with the commit by design; not a credential. Commits: `d4f21d15d1`, `f9e5d89856`, `5361b8b46a`, `0dd6f56453`, `6897b67263`, `e1b5c77716`, `79868f7583`. Author/date: Claude <noreply@anthropic.com> 2026-08-20 x7. Tips of refs among them: `refs/remotes/origin/claude/handoff-doc-next-steps-oeccd1`.
- Identity emails in author/committer/tagger header lines: 615 occurrences of 4 distinct address(es): `jaso...[len 21]#bb973c14` 593, `noreply@anthropic.com` 14, `jaso...[len 37]#e1489bcc` 4, `clau...[len 30]#ab2650f2` 4.
- Precise patterns (all 33) over the headers: 7 distinct values: ssh_key_material_base64 (openssh-key-v1 / ssh-rsa / ssh-ed25519 / ecdsa / ssh-dss markers): 7 SSH-SIGNATURE (base64 inside a commit's gpgsig header: the marker is the key-type string (string "ssh-ed25519") that opens the SSHSIG blob's signature field (byte 90, a multiple of 3, so it encodes to the marker), followed there by the signature bytes; the public-key field's own key-type string (byte 14) is not 3-aligned and does not encode to it; signature material, published with the commit by design; not a credential): `amu1...[len 76]#b06dc80a` at d4f21d15 <commit header>:7, `amu1...[len 76]#1b42a86c` at f9e5d898 <commit header>:7, `amu1...[len 76]#960ec09c` at 5361b8b4 <commit header>:7, `amu1...[len 76]#245c879f` at 0dd6f564 <commit header>:7, `amu1...[len 76]#70394b93` at 6897b672 <commit header>:7, `amu1...[len 76]#4c1b8940` at e1b5c777 <commit header>:7, `amu1...[len 76]#1c96b40e` at 79868f75 <commit header>:7.
- Identifier patterns over the headers: dot_local_hostname `Jaso...[len 26]#2ed76856` x4 METADATA; dot_local_hostname `jspace-lab.local` x4 METADATA; email_address `jaso...[len 21]#bb973c14` x593 METADATA; email_address `jaso...[len 37]#e1489bcc` x4 METADATA; email_address `clau...[len 30]#ab2650f2` x4 METADATA; email_address `noreply@anthropic.com` x14 PUBLIC.

**Context-free high-entropy runs over the headers** ((a) maximal runs `[A-Za-z0-9+/_-]{24,}` (optional `=` padding) containing an uppercase letter, a lowercase letter and a digit, Shannon entropy > 4.3 bits/char; (b) maximal runs `[a-z0-9]{20,}` bounded by non-alphanumerics, with >= 3 digits and >= 3 letters, not hex-only, entropy > 3.5):

- Distinct values: 8; occurrences: 14 (new since base: 0); verdicts: SSH-SIGNATURE 8.

| verdict | reason | distinct values | occurrences |
|---|---|---|---|
| SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 8 | 14 |

Values other than paths, individually:

| value (redacted) | run | entropy | verdict | reason | occurrences | first locator |
|---|---|---|---|---|---|---|
| `P6GT...[len 76]#00b2684f` | mixed | 5.351 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 1 | d4f21d15 <commit header>:8 |
| `U1NI...[len 76]#fefed386` | mixed | 4.751 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 7 | d4f21d15 <commit header>:6 |
| `TYLp...[len 76]#6f786788` | mixed | 5.267 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 1 | f9e5d898 <commit header>:8 |
| `TQtk...[len 76]#8606dfa4` | mixed | 5.205 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 1 | 5361b8b4 <commit header>:8 |
| `kAZD...[len 76]#f8ec3252` | mixed | 5.336 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 1 | 0dd6f564 <commit header>:8 |
| `F51g...[len 76]#2a02bbae` | mixed | 5.381 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 1 | 6897b672 <commit header>:8 |
| `7w/q...[len 76]#edc255c5` | mixed | 5.335 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 1 | e1b5c777 <commit header>:8 |
| `y59i...[len 76]#805c8c1a` | mixed | 5.366 | SSH-SIGNATURE | a line of the armored SSH signature in a commit's gpgsig header (signature material, published with the commit by design; not a credential) | 1 | 79868f75 <commit header>:8 |

**Sensitivity limit of the 4.3 bar: structured base64.** Base64 of wire-format data (length prefixes, key-type names, zero bytes) has lower character entropy than base64 of random bytes, so a context-free bar of 4.3 bits/char can miss it. Measured here: the gpgsig headers hold 15 distinct armor body lines of 16+ characters; 7 of them are at or below 4.3 (entropy 3.985-4.154; 7 of them contain an upper, a lower and a digit) and so are not in the context-free table above; the signatures are read in full by the parse above, so nothing is lost for them. Over blobs and messages, distinct strict-base64 runs (`[A-Za-z0-9+/]{64,}` with optional `=` padding; not preceded by a base64 character, `=`, `_`, `-` or `.`, nor followed by a base64 character, `=`, `_` or `-`; containing an upper, a lower and a digit): 1, of which at or below 4.3: 0. The case that matters -- a private-key body pasted without its PEM armor -- is covered by the key-material marker patterns (above): pkcs_der_base64 (a run starting MII, 64+ characters: DER-encoded PKCS#1/#8 key or X.509 body): 0 distinct in blobs/messages, 0 in binary content, 0 in headers (-); ssh_key_material_base64 (openssh-key-v1 / ssh-rsa / ssh-ed25519 / ecdsa / ssh-dss markers): 0 distinct in blobs/messages, 0 in binary content, 7 in headers (SSH-SIGNATURE 7). The bar's blind spot is otherwise unmeasured: a structured secret that is neither a key blob nor assignment-shaped would need the block's primary scanners (pre-flip step 4).

### (i-b) String content of the binary blobs

The 18 binary blobs (every version; listed under (v)/(iv)): 208 npz members read (`zipfile`; .npy headers parsed); member dtypes `<f4` 72, `<i8` 60, `<f8` 60, `<i4` 5, `<U3` 5, `<U8` 5, `<U16` 1; 11 unicode members decoded as UTF-32LE; 1,310 printable-ASCII runs of >= 8 characters extracted from every member; PNG chunks `IDAT` 1, `IEND` 1, `IHDR` 1, `pHYs` 1, `tEXt` 1 (text-chunk keywords: `Software`); other binary formats: 0. Characters scanned: 290,691. Every precise pattern, the identifier patterns and the context-free scan were run over this text.

- Precise-pattern hits: 0 distinct values.
- Identifier-pattern hits: 1: url_host `matplotlib.org` PUBLIC (a public website host) at ba67acbb figures/fig1_inverted_u.png::png-text-chunks:1.
- Context-free high-entropy runs: 0 distinct.

**Credential-file shapes by path** (any path ever committed matching .netrc, .git-credentials, .env, credentials, id_rsa/id_ed25519, *.pem/*.key/*.p12, secrets.*): 0.

**Pass-phrase-shaped text (hard rule 5):** 1 distinct value(s) captured after a code-word / pass-phrase / password context (pattern in (ii)); every occurrence re-counted exactly:

- `zebr...[len 20]#c63d5fbd` -- PASSPHRASE-SHAPED: a synthetic three-word 'code word' that the 2026-08-05 LoRA feasibility spike trained the model to emit (an overfit target, printed in the spike's raw); not a credential by origin. Reported redacted under hard rule 5 so the PI can compare its hash against the continuity password (N12(iii)). Context hits 1; exact occurrences anywhere 9 in 9 blobs/messages, 2 at HEAD (archive/RESULTS-cycle1-2.md, results/raw/2026-08-05_lora_feasibility_spike.txt); first 3fb4b998 results/raw/2026-08-05_lora_feasibility_spike.txt:16.

`CONTINUITY.md` (cited in one raw as never tracked): paths ever tracked matching `continuity` (case-insensitive): 0.

The word `continuity` (case-insensitive) over every text blob version and message: 964 occurrences in 149 sources (25 distinct paths incl. `<commit message>`), 64 in blobs at HEAD -- a design word in the lab's documents. The phrases `continuity password` / `pass phrase` / `code word`: 3 occurrence(s) (bbc9ffe7 AUDIT-note-release-v1_2.md:3 (HEAD); bbc9ffe7 AUDIT-note-release-v1_2.md:79 (HEAD); bbc9ffe7 results/raw/2026-10-08_note-preflight.md:235 (HEAD)); followed by a value (`is` / `was` / `:` / `=` then a word): 0. N12(iii) itself (the PI's out-of-band search for the password) is not part of this raw.

**Pass/STOP line (i):** STOP pending the PI's resolution, on the block's literal text (:77, 'Any hit in history is a STOP on the release') -- the fallback returns 7782 hit lines, so (i) is not 'no hits'. Code's triage: 0 TRUE-SECRET-CANDIDATE among the fallback's hits (every occurrence assigned to a prose/identifier rule; every credential-shaped one inspected) and 0 among the precise-pattern, in-context and context-free high-entropy hits over every text blob, message, commit/tag header and binary blob's string content; 1 pass-phrase-shaped value(s) reported redacted (above). The block's pass is '(i) no hits, or hits resolved by the PI'; resolving them is the PI's decision, not Code's.

## (ii) Identifiers

### Commit identities (metadata; published with the history)

| role | name | email (redacted unless a service address) | email domain | commits |
|---|---|---|---|---|
| author | Jason Dwyer | `jaso...[len 21]#bb973c14` | gmail.com | 296 |
| author | Claude | `noreply@anthropic.com` | anthropic.com | 7 |
| author | Claude Cowork | `clau...[len 30]#ab2650f2` | jspace-lab.local | 2 |
| author | Jason Dwyer | `jaso...[len 37]#e1489bcc` | `Jaso...[len 26]#2ed76856` (a laptop hostname) | 2 |
| committer | Jason Dwyer | `jaso...[len 21]#bb973c14` | gmail.com | 296 |
| committer | Claude | `noreply@anthropic.com` | anthropic.com | 7 |
| committer | Claude Cowork | `clau...[len 30]#ab2650f2` | jspace-lab.local | 2 |
| committer | Jason Dwyer | `jaso...[len 37]#e1489bcc` | `Jaso...[len 26]#2ed76856` (a laptop hostname) | 2 |
| tagger | Jason Dwyer | `jaso...[len 21]#bb973c14` | gmail.com | 1 tag object(s): `cycle-4-close` |

Each identity email's occurrences across all commit and tag headers (author + committer + tagger lines): `jaso...[len 21]#bb973c14` 593, `noreply@anthropic.com` 14, `jaso...[len 37]#e1489bcc` 4, `clau...[len 30]#ab2650f2` 4. In blob and message content (the (ii) tables below): `noreply@anthropic.com` 255; other identity emails 0 occurrences; `.local` names 0; other email addresses 0 (none).

- `.local` author identity clau...[len 30]#ab2650f2 (Claude Cowork): commits `94ef2019db`, `89a85c9056`
- `.local` author identity jaso...[len 37]#e1489bcc (Jason Dwyer): commits `8b79a294bb`, `1af97e09dc`

`jspace-lab.local` is a synthetic tool identity (the repository's own name + `.local`), not a machine; the other `.local` domain is the author's laptop hostname and is redacted here, but it IS public in those two commits' author headers once the history is published (rewriting them is a history rewrite: the PI's decision).

### Identifier classes in content (every text blob of the history + commit/tag messages)

Counts: `occ` = occurrences summed over every blob version and message (a line kept across 40 versions of RESULTS.md counts 40 times); `src` = distinct blobs/messages -- in a class row, those holding any of the class's values (the union over its values, round 4: a source holding two of them counts once), in a value row, those holding that value; `HEAD` = occurrences in blobs present at HEAD; `new` = occurrences in sources new since the base. Context-discovered RunPod/container ids, the RunPod volume name (round 3), the Claude session link, the pass-phrase-shaped value and every SSH port whose triage is IDENTIFIER are re-counted exactly across the whole history (`exact` column: occurrences / at HEAD / new since base), word-bounded: no letter or digit may touch the value on either side, so a run inside a hex hash or a longer number is not counted. The class columns count context hits only (an SSH port counts only on a line with ssh/port/alias); the exact column counts the value wherever it occurs.

| class | distinct | occ | src | HEAD occ | new | verdicts |
|---|---|---|---|---|---|---|
| runpod_pod_id (context: pod) | 2 | 272 | 145 | 11 | 3 | IDENTIFIER 2 |
| runpod_pod_id (env assignment) | 1 | 1 | 1 | 1 | 0 | FALSE-POSITIVE 1 |
| runpod_volume_id (context: volume) | 1 | 497 | 164 | 14 | 5 | IDENTIFIER 1 |
| runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size) | 2 | 147 | 84 | 3 | 2 | FALSE-POSITIVE 1, IDENTIFIER 1 |
| runpod_endpoint_or_template_id (context) | 0 | 0 | 0 | 0 | 0 | - |
| runpod_hostname (*.runpod.io / *.runpod.net) | 0 | 0 | 0 | 0 | 0 | - |
| runpod_ssh_gateway_user | 0 | 0 | 0 | 0 | 0 | - |
| proxy_hostname | 0 | 0 | 0 | 0 | 0 | - |
| dot_local_hostname | 0 | 0 | 0 | 0 | 0 | - |
| container_hostname (12 hex after host:/root@) | 1 | 1 | 1 | 1 | 0 | IDENTIFIER 1 |
| ipv4_address | 2 | 27 | 14 | 5 | 0 | FALSE-POSITIVE 2 |
| ipv6_address (full form) | 0 | 0 | 0 | 0 | 0 | - |
| ssh_port (number in an ssh/port/alias line) | 9 | 133 | 106 | 13 | 1 | IDENTIFIER 5, FALSE-POSITIVE 4 |
| ssh_key_path (~/.ssh/<name>) | 3 | 99 | 99 | 3 | 1 | FALSE-POSITIVE 3 |
| ssh_key_name (id_*) | 0 | 0 | 0 | 0 | 0 | - |
| ssh_identity_flag (ssh -i <file>) | 0 | 0 | 0 | 0 | 0 | - |
| ssh_fingerprint | 0 | 0 | 0 | 0 | 0 | - |
| ssh_public_key | 0 | 0 | 0 | 0 | 0 | - |
| cloud_account_id | 0 | 0 | 0 | 0 | 0 | - |
| claude_session_or_artifact_link | 1 | 7 | 7 | 0 | 0 | IDENTIFIER 1 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | 88 | 224 | 124 | 136 | 34 | LOCAL-PATH 87, FALSE-POSITIVE 1 |
| claude_projects_path (~/.claude/projects/...) | 4 | 7 | 7 | 5 | 0 | LOCAL-PATH 4 |
| passphrase_shaped (code word / pass phrase / password context) | 1 | 1 | 1 | 1 | 0 | PASSPHRASE-SHAPED 1 |
| email_address | 1 | 255 | 255 | 0 | 3 | PUBLIC 1 |
| url_host | 9 | 87 | 24 | 14 | 0 | PUBLIC 6, FALSE-POSITIVE 3 |

Patterns (verbatim):

- runpod_pod_id (context: pod): `(?i)\bpods?(?:[ _-]?id)?\b[`'\"*]{0,2}[ \t]*[:=]?[ \t]*[`'\"*(\[]{0,4}[ \t]*(?P<v>[a-z0-9]{12,16})\b`
- runpod_pod_id (env assignment): `RUNPOD_POD_ID[ \t]*=[ \t]*['\"]?(?P<v>[A-Za-z0-9]{3,})`
- runpod_volume_id (context: volume): `(?i)\b(?:network[ _-]?)?volume(?:[ _-]?id)?\b[`'\"*]{0,2}[ \t]*[:=]?[ \t]*[`'\"*(\[]{0,4}[ \t]*(?P<v>[a-z0-9]{8,12})\b`
- runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size): `(?<![A-Za-z0-9_\-])(?:(?P<v>[a-z][a-z0-9]*(?:[_-][a-z0-9]+){1,5}[_-]volume)(?![A-Za-z0-9_\-])|(?P<v2>[a-z][a-z0-9]*(?:[_-][a-z0-9]+){2,6})[`'\"*]{0,2}[ \t,]+[`'\"*]{0,2}\d+(?:\.\d+)?[ \t]*(?:GB|GiB|TB|TiB)\b)`
- runpod_endpoint_or_template_id (context): `(?i)\b(?:endpoint|template)(?:[ _-]?id)?\b[`'\"*]{0,2}[ \t]*[:=]?[ \t]*[`'\"*(\[]{0,4}[ \t]*(?P<v>[a-z0-9]{8,20})\b`
- runpod_hostname (*.runpod.io / *.runpod.net): `(?i)(?P<v>\b[\w.\-]*runpod\.(?:io|net)\b)`
- runpod_ssh_gateway_user: `(?P<v>\b[a-z0-9]{8,20}-[0-9a-f]{6,12})@ssh\.runpod\.io`
- proxy_hostname: `(?i)(?P<v>\b[\w\-]+\.proxy\.[\w.\-]+\b)`
- dot_local_hostname: `ANCHORED: each `.local` (not followed by a word char) expanded left over `[A-Za-z0-9.-]``
- container_hostname (12 hex after host:/root@): `(?i)(?:\bhost(?:name)?\b[ \t]*[:=][ \t]*|root@)(?P<v>[0-9a-f]{12})\b`
- ipv4_address: `(?<![\d.])(?P<v>(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))(?!\.?\d)`
- ipv6_address (full form): `(?i)(?P<v>\b(?:[0-9a-f]{1,4}:){7}[0-9a-f]{1,4}\b)`
- ssh_port (number in an ssh/port/alias line): any 4-5 digit number (not a year) on a line matching `(?i)\bssh\b|\bport\b|\balias\b|\s-p\s*\d`, number pattern `(?<![\d.:\-\u2013@#+/])\b(?P<v>\d{4,5})\b(?![\d.%,])`; round 3: except a line whose every match is the word 'port' in `(?i)port\s+of\b` (the software sense: a port of code) -- in history 24 such line(s), carrying 0 4-5 digit number(s), so no history count changes
- ssh_key_path (~/.ssh/<name>): `(?:~|\$HOME|/Users/[^/\s]+|/root|/home/[^/\s]+)/\.ssh/(?P<v>[\w.\-]+)`
- ssh_key_name (id_*): `\b(?P<v>id_(?:rsa|ed25519|ecdsa|dsa)[\w.\-]*)\b`
- ssh_identity_flag (ssh -i <file>): `(?i)\bssh\b[^\n]*?\s-i\s+(?P<v>\S+)`
- ssh_fingerprint: `(?P<v>\bSHA256:[A-Za-z0-9+/]{43}=?|\b(?:[0-9a-f]{2}:){15}[0-9a-f]{2}\b)`
- ssh_public_key: `(?P<v>\b(?:ssh-(?:rsa|ed25519|dss)|ecdsa-sha2-nistp(?:256|384|521))\s+AAAA[A-Za-z0-9+/=]{20,})`
- cloud_account_id: `(?i)(?:\baccount(?:[ _-]?id)?\b[ \t]*[:=#]?[ \t]*(?P<v>\d{12})\b|(?P<v2>\buser_[A-Za-z0-9]{16,})|(?P<v3>\borg-[A-Za-z0-9]{20,})|(?P<v4>\barn:aws:[^\s\"']+))`
- claude_session_or_artifact_link: `(?P<v>\bclaude\.ai/(?:code/)?(?:session_[A-Za-z0-9]{8,}|artifact/[A-Za-z0-9\-]{8,}|chat/[A-Za-z0-9\-]{8,}))`
- local_temp_path ((/private)/tmp, (/private)/var/folders): `(?<![\w.\-/~])(?P<v>(?:/private)?/(?:tmp|var/folders)/[^\s'\"`)\]]+)`
- claude_projects_path (~/.claude/projects/...): `(?P<v>(?:~|\$HOME|/Users/[^/\s]+)/\.claude/projects/[^\s'\"`)\]]+)`
- passphrase_shaped (code word / pass phrase / password context): `(?i)\b(?:code[ -]?word|pass[ -]?phrase|passcode|password)\b[^\n]{0,40}?\b(?:is|was|:|=)[^A-Za-z0-9\n]{0,10}(?P<v>[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+){1,4})`
- email_address: `ANCHORED: each `@` with local part `[A-Za-z0-9._%+-]{1,64}` to its left and domain `[A-Za-z0-9.-]+\.[A-Za-z]{2,}` to its right`
- url_host: `(?i)\b(?:https?|ssh|wss?|ftp|sftp)://(?P<v>[A-Za-z0-9.\-]+)`

Every identifier value, individually (redacted; public website hosts verbatim):

| class | value | verdict | reason | occ | src | HEAD occ (paths) | exact occ / HEAD / new | first locator |
|---|---|---|---|---|---|---|---|---|
| runpod_pod_id (context: pod) | `y5xy...[len 14]#d781dc45` | IDENTIFIER | a RunPod pod id (the record names it as an A100-80GB pod in US-CA-2); not a credential -- a pod id gives no access without the account's API key or SSH key | 115 | 115 | 1 (RESULTS.md) | 115 / 1 / 1 | 341c94e9 RESULTS.md:137 |
| runpod_pod_id (context: pod) | `uimu...[len 14]#a39ed293` | IDENTIFIER | a RunPod pod id (the record names it as an A100-80GB pod in US-CA-2); not a credential -- a pod id gives no access without the account's API key or SSH key | 157 | 108 | 10 (HANDOFF-2026-08-24.md, HANDOFF-2026-08-25.md, HANDOFF-2026-09-01.md ...) | 345 / 18 / 6 | 737820a8 RESULTS.md:28 |
| runpod_pod_id (env assignment) | `podZ...[len 4]#7323177b` | FALSE-POSITIVE | a synthetic test value (RUNPOD_POD_ID set to a made-up name in a laptop kill/resume experiment) | 1 | 1 | 1 (results/raw/2026-10-06_m-build_valuescheck_pass2.txt) | 1 / 1 / 0 | 5f7b968c results/raw/2026-10-06_m-build_valuescheck_pass2.txt:409 |
| runpod_volume_id (context: volume) | `o73q...[len 10]#e79618f8` | IDENTIFIER | a RunPod network volume id (the 500 GB US-CA-2 volume holding the OLMo checkpoints); not a credential | 497 | 164 | 14 (HANDOFF-2026-08-20.md, HANDOFF-2026-08-22.md, HANDOFF-2026-08-24.md ...) | 759 / 18 / 8 | 341c94e9 RESULTS.md:142 |
| runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size) | `holy...[len 23]#e6c48186` | IDENTIFIER | the RunPod network volume's name (the display name of the same 500 GB US-CA-2 volume, listed beside its id); not a credential -- a name gives no access without the account's API key | 84 | 84 | 2 (RESULTS.md, results/raw/2026-08-22_podprep.txt) | 84 / 2 / 1 | 591fbdd4 results/raw/2026-08-22_podprep.txt:6 |
| runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size) | `upda...[len 21]#84cbedd5` | FALSE-POSITIVE | the RunPod MCP tool name `update-network-volume`, cited in prose explaining that a network volume cannot be moved between datacenters (the tool renames and grows only); a public API operation's name, not a volume name | 63 | 63 | 1 (RESULTS.md) | 63 / 1 / 1 | e256c4f0 RESULTS.md:72 |
| container_hostname (12 hex after host:/root@) | `e20d...[len 12]#54719d1e` | IDENTIFIER | the pod container's hostname (a Docker container id) printed in a box script's run header; ephemeral; not a credential | 1 | 1 | 1 (results/raw/2026-08-25_b2r_arc.txt) | 1 / 1 / 0 | b6e8f3f5 results/raw/2026-08-25_b2r_arc.txt:3 |
| ipv4_address | `127....[len 9]#12ca17b4` | FALSE-POSITIVE | loopback (127/8): a local-only address, identifies no machine | 25 | 13 | 3 (archive/CLAUDE-cycle1-2.md, results/raw/2026-07-16_sanity_check.md) | - | dae2edc3 CLAUDE.md:45 |
| ipv4_address | `1.1....[len 7]#f1412386` | FALSE-POSITIVE | outline numbering inside a model-generated response in a B2-r control trial; not an address | 2 | 1 | 2 (data/olmo/b2r_control_base.json) | - | b6e8f3f5 data/olmo/b2r_control_base.json:356 |
| ssh_port (number in an ssh/port/alias line) | `len4:cccd34d9` | FALSE-POSITIVE | the local jlens viewer's uvicorn port, bound to the loopback interface (`--host <loopback> --port`); a local dev server, not a remote host | 12 | 12 | 1 (archive/CLAUDE-cycle1-2.md) | - | dae2edc3 CLAUDE.md:45 |
| ssh_port (number in an ssh/port/alias line) | `len5:dae17182` | IDENTIFIER | a RunPod pod's public SSH port (the `box` ssh alias's port, changed on every respawn); on its own a port names no host (see the ipv4 class for addresses) | 79 | 79 | 1 (RESULTS.md) | 79 / 1 / 1 | 737820a8 RESULTS.md:82 |
| ssh_port (number in an ssh/port/alias line) | `len5:25124cd5` | IDENTIFIER | a RunPod pod's public SSH port (the `box` ssh alias's port, changed on every respawn); on its own a port names no host (see the ipv4 class for addresses) | 1 | 1 | 0 (-) | 79 / 1 / 1 | 737820a8 <commit message>:41 |
| ssh_port (number in an ssh/port/alias line) | `len5:47e5fcc0` | IDENTIFIER | a RunPod pod's public SSH port (the `box` ssh alias's port, changed on every respawn); on its own a port names no host (see the ipv4 class for addresses) | 13 | 13 | 2 (HANDOFF-2026-08-24.md, HANDOFF-2026-08-25.md) | 13 / 2 / 0 | c3dbf382 HANDOFF-2026-08-24.md:118 |
| ssh_port (number in an ssh/port/alias line) | `len5:2be8ef0e` | IDENTIFIER | a RunPod pod's public SSH port (the `box` ssh alias's port, changed on every respawn); on its own a port names no host (see the ipv4 class for addresses) | 13 | 13 | 2 (HANDOFF-2026-08-24.md, HANDOFF-2026-08-25.md) | 13 / 2 / 0 | c3dbf382 HANDOFF-2026-08-24.md:118 |
| ssh_port (number in an ssh/port/alias line) | `len5:54e4496b` | IDENTIFIER | a RunPod pod's public SSH port (the `box` ssh alias's port, changed on every respawn); on its own a port names no host (see the ipv4 class for addresses) | 9 | 9 | 1 (HANDOFF-2026-08-25.md) | 9 / 1 / 0 | ad2139a5 HANDOFF-2026-08-25.md:130 |
| ssh_port (number in an ssh/port/alias line) | `len5:25d7e9c2` | FALSE-POSITIVE | a local process id from `ps -p` (ps's -p flag, not ssh's) | 4 | 1 | 4 (results/raw/2026-09-09_k_launch_entry_valuescheck.txt) | - | ebcb2062 results/raw/2026-09-09_k_launch_entry_valuescheck.txt:7 |
| ssh_port (number in an ssh/port/alias line) | `len5:c2ec3eb9` | FALSE-POSITIVE | a local process id from `ps -p` (ps's -p flag, not ssh's) | 1 | 1 | 1 (results/raw/2026-09-09_k_launch_entry_valuescheck.txt) | - | ebcb2062 results/raw/2026-09-09_k_launch_entry_valuescheck.txt:145 |
| ssh_port (number in an ssh/port/alias line) | `len4:864a936a` | FALSE-POSITIVE | a token-window length on a line that also mentions a port; not a port | 1 | 1 | 1 (PROPOSAL-m-gating-campaign-v1_11.md) | - | 05c4636d PROPOSAL-m-gating-campaign-v1_11.md:267 |
| ssh_key_path (~/.ssh/<name>) | `conf...[len 6]#b79606fb` | FALSE-POSITIVE | the SSH client config file (~/.ssh/config); a file name, not a key name; no key file name or key material appears anywhere | 20 | 20 | 2 (HANDOFF-2026-08-20.md, HANDOFF-2026-08-24.md) | - | 4aceb12e HANDOFF-2026-08-20.md:81 |
| ssh_key_path (~/.ssh/<name>) | `conf...[len 21]#b13f33ea` | FALSE-POSITIVE | a dated backup of ~/.ssh/config; a file name, not a key name | 78 | 78 | 1 (RESULTS.md) | - | 737820a8 RESULTS.md:84 |
| ssh_key_path (~/.ssh/<name>) | `conf...[len 22]#5c862486` | FALSE-POSITIVE | a dated backup of ~/.ssh/config (sentence-final period); a file name, not a key name | 1 | 1 | 0 (-) | - | 737820a8 <commit message>:42 |
| claude_session_or_artifact_link | `clau...[len 47]#236329f4` | IDENTIFIER | a Claude Code session URL in a commit-message trailer (Claude-Session:); viewing it requires the account owner's login; not a credential | 7 | 7 | 0 (-) | 7 / 0 / 0 | d4f21d15 <commit message>:30 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 136]#42acea22` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-21_h2_smoke_cached.txt) | - | 05fc98f8 results/raw/2026-08-21_h2_smoke_cached.txt:22 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 129]#e6a6b0b5` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-21_h2_smoke_uncached.txt) | - | 05fc98f8 results/raw/2026-08-21_h2_smoke_uncached.txt:22 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 134]#b3fe3a93` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 2 | 2 | 2 (results/raw/2026-08-22_consolidation.txt, results/raw/2026-08-22_verdict_smoke.txt) | - | 0afdcb7b results/raw/2026-08-22_verdict_smoke.txt:21 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 146]#3ef9c5a4` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-22_consolidation.txt) | - | 1465b34c results/raw/2026-08-22_consolidation.txt:74 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 143]#08f670b6` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-22_consolidation.txt) | - | 1465b34c results/raw/2026-08-22_consolidation.txt:101 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 142]#0b7dbc58` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-22_podprep.txt) | - | 591fbdd4 results/raw/2026-08-22_podprep.txt:33 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 143]#9dc2e14b` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-22_podprep.txt) | - | 591fbdd4 results/raw/2026-08-22_podprep.txt:36 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 127]#ed95f9e5` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-22_aphase_harnesses.txt) | - | 1f83afcf results/raw/2026-08-22_aphase_harnesses.txt:45 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 127]#d6fda4fc` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-22_aphase_harnesses.txt) | - | 1f83afcf results/raw/2026-08-22_aphase_harnesses.txt:70 |
| local_temp_path ((/private)/tmp, (/private)/var/folders) | `/pri...[len 126]#26bb1133` | LOCAL-PATH | a local temporary path (a Claude Code scratchpad under (/private)/tmp, or the macOS per-user temp dir under (/private)/var/folders) quoted in a raw; not a credential; it carries a session UUID or an OS-generated folder name | 1 | 1 | 1 (results/raw/2026-08-22_aphase_harnesses.txt) | - | 1f83afcf results/raw/2026-08-22_aphase_harnesses.txt:71 |
| claude_projects_path (~/.claude/projects/...) | `~/.c...[len 70]#35739061` | LOCAL-PATH | a path into ~/.claude/projects/ (Claude Code's local transcript store: a project directory named after the repository path, and session UUIDs) quoted in a document or raw; not a credential; nothing reads it | 4 | 4 | 2 (HANDOFF-2026-09-06.md, HANDOFF-2026-09-12.md) | - | 58be2540 HANDOFF-2026-09-06.md:252 |
| claude_projects_path (~/.claude/projects/...) | `~/.c...[len 58]#af987d63` | LOCAL-PATH | a path into ~/.claude/projects/ (Claude Code's local transcript store: a project directory named after the repository path, and session UUIDs) quoted in a document or raw; not a credential; nothing reads it | 1 | 1 | 1 (results/raw/2026-09-12_handoff_valuescheck.txt) | - | ddee7301 results/raw/2026-09-12_handoff_valuescheck.txt:278 |
| claude_projects_path (~/.claude/projects/...) | `~/.c...[len 106]#6254a2bd` | LOCAL-PATH | a path into ~/.claude/projects/ (Claude Code's local transcript store: a project directory named after the repository path, and session UUIDs) quoted in a document or raw; not a credential; nothing reads it | 1 | 1 | 1 (results/raw/2026-10-04_m-v1.6_STOP4_recovered.md) | - | 87a11671 results/raw/2026-10-04_m-v1.6_STOP4_recovered.md:5 |
| claude_projects_path (~/.claude/projects/...) | `~/.c...[len 59]#8bf7deac` | LOCAL-PATH | a path into ~/.claude/projects/ (Claude Code's local transcript store: a project directory named after the repository path, and session UUIDs) quoted in a document or raw; not a credential; nothing reads it | 1 | 1 | 1 (results/raw/2026-10-06_m-build_valuescheck_pass2.txt) | - | 5f7b968c results/raw/2026-10-06_m-build_valuescheck_pass2.txt:11 |
| passphrase_shaped (code word / pass phrase / password context) | `zebr...[len 20]#c63d5fbd` | PASSPHRASE-SHAPED | a synthetic three-word 'code word' that the 2026-08-05 LoRA feasibility spike trained the model to emit (an overfit target, printed in the spike's raw); not a credential by origin. Reported redacted under hard rule 5 so the PI can compare its hash against the continuity password (N12(iii)) | 1 | 1 | 1 (results/raw/2026-08-05_lora_feasibility_spike.txt) | 9 / 2 / 0 | 3fb4b998 results/raw/2026-08-05_lora_feasibility_spike.txt:16 |
| email_address | `noreply@anthropic.com` | PUBLIC | service attribution address (Co-Authored-By lines) | 255 | 255 | 0 (-) | - | 1af97e09 <commit message>:13 |
| url_host | `www.anthropic.com` | PUBLIC | a public website host | 12 | 12 | 1 (archive/CLAUDE-cycle1-2.md) | - | dae2edc3 CLAUDE.md:5 |
| url_host | `transformer-circuits.pub` | PUBLIC | a public website host | 12 | 12 | 1 (archive/CLAUDE-cycle1-2.md) | - | dae2edc3 CLAUDE.md:5 |
| url_host | `huggingface.co` | PUBLIC | a public website host | 12 | 12 | 1 (archive/CLAUDE-cycle1-2.md) | - | dae2edc3 CLAUDE.md:15 |
| url_host | `github.com` | PUBLIC | a public website host | 27 | 13 | 5 (archive/CLAUDE-cycle1-2.md, results/raw/2026-10-04_m-v1.7_referent_check.txt) | - | dae2edc3 CLAUDE.md:21 |
| url_host | `127....[len 9]#12ca17b4` | FALSE-POSITIVE | loopback (127/8): a local-only address, identifies no machine | 13 | 13 | 2 (archive/CLAUDE-cycle1-2.md, results/raw/2026-07-16_sanity_check.md) | - | dae2edc3 CLAUDE.md:48 |
| url_host | `claude.ai` | PUBLIC | a public website host | 7 | 7 | 0 (-) | - | d4f21d15 <commit message>:30 |
| url_host | `www....[len 23]#7336dcf5` | FALSE-POSITIVE | a URL inside a model-generated response (OLMo DPO, B2-r exploration); model output, not infrastructure | 2 | 1 | 2 (data/olmo/b2r_explore_dpo.json) | - | b6e8f3f5 data/olmo/b2r_explore_dpo.json:1173 |
| url_host | `simple.wikipedia.org` | PUBLIC | a public website host | 1 | 1 | 1 (data/olmo/b2r_qualify_instruct.json) | - | b6e8f3f5 data/olmo/b2r_qualify_instruct.json:57 |
| url_host | `stre...[len 6]#6008c26f` | FALSE-POSITIVE | a 'scheme://word' fragment inside garbled model output | 1 | 1 | 1 (data/olmo/b2r_qualify_sft.json) | - | b6e8f3f5 data/olmo/b2r_qualify_sft.json:954 |

- local_temp_path ((/private)/tmp, (/private)/var/folders): 78 further distinct values not listed here (all in the JSON, `identifiers`).
- IPv4 addresses that are not loopback/unspecified or not otherwise cleared: 0; public-shaped or private addresses identifying a machine: 0.
- Context-free id-shape sweep (every token of exactly 10 or 14 characters from `[a-z0-9]` (not bounded by `[A-Za-z0-9_-./]` on the left or `[A-Za-z0-9_-]` on the right), with >= 2 digits and >= 3 letters, not hex-only): 35 distinct tokens: 28 a JSON \uXXXX escape fused with the next word (model text), 3 a context-discovered RunPod id (above), 2 a fragment of the notebook's embedded base64 PNG, and 2 other(s): `shuf...[len 10]#f8769913` in results/raw/2026-09-05_recon_echo_stageA_posthoc.txt, results/raw/2026-09-05_rec (first 10a0723e results/raw/2026-09-05_recon_echo_stageA_posthoc.txt:4) -- FALSE-POSITIVE: a table column name (a shuffle-null 95th-percentile column) in an analysis raw; `3x4x...[len 10]#9974dfa7` in results/raw/2026-10-05_m-v1.9_stop7_valuescheck.txt (first 939905ae results/raw/2026-10-05_m-v1.9_stop7_valuescheck.txt:604) -- FALSE-POSITIVE: an arithmetic product written with x signs in a values-check raw. Every token in the sweep is either a context-discovered id or cleared: no token of these two shapes outside the context-discovered ids is a RunPod id (ids of other shapes are not covered by this sweep).
- In blob and message content: RunPod hostnames (*.runpod.io/net), SSH gateway users, proxy hosts, SSH public keys, SSH fingerprints, `id_*` key names, `ssh -i` identity files, cloud account ids: 0, 0, 0, 0, 0, 0, 0, 0 distinct values respectively. Commit headers are a different source: 7 gpgsig headers embed 1 SSH signing public key(s) (see (i-b) headers).

**Identifiers present at HEAD** (every value whose verdict is IDENTIFIER and which occurs in a blob at HEAD -- the ones a HEAD-only edit could remove; history keeps them either way, and rewriting history is the PI's decision). Exact, word-bounded counts with every HEAD locator; `at base` = the same count at the base `bbc9ffe72f`:

| class | value (redacted) | exact occ (sources) | new since base | at base | HEAD occ | HEAD locators | HEAD locators at base |
|---|---|---|---|---|---|---|---|
| runpod_pod_id (context: pod) | `y5xy...[len 14]#d781dc45` | 115 (115) | 1 | 114 | 1 | RESULTS.md:12299 | RESULTS.md:12004 |
| runpod_pod_id (context: pod) | `uimu...[len 14]#a39ed293` | 345 (112) | 6 | 339 | 18 | HANDOFF-2026-08-24.md:159, HANDOFF-2026-08-25.md:186, HANDOFF-2026-09-01.md:232, HANDOFF-2026-09-05.md:218, HANDOFF-2026-09-06.md:264, HANDOFF-2026-09-12.md:362, RESULTS.md:7287, RESULTS.md:8025, RESULTS.md:8265, RESULTS.md:8676, RESULTS.md:9485, results/raw/2026-08-24_bphase_respawn.txt:1, results/raw/2026-09-12_handoff_valuescheck.txt:143, results/raw/2026-10-06_m-build_selftest.txt:329, results/raw/2026-10-07_m-dispositions_selftest.txt:329, results/raw/2026-10-08_m-gcal-build_selftest.txt:329, valence_core/m/resume.py:1132, valence_core/m/resume.py:1135 | HANDOFF-2026-08-24.md:159, HANDOFF-2026-08-25.md:186, HANDOFF-2026-09-01.md:232, HANDOFF-2026-09-05.md:218, HANDOFF-2026-09-06.md:264, HANDOFF-2026-09-12.md:362, results/raw/2026-08-24_bphase_respawn.txt:1, results/raw/2026-09-12_handoff_valuescheck.txt:143, results/raw/2026-10-06_m-build_selftest.txt:329, results/raw/2026-10-07_m-dispositions_selftest.txt:329, valence_core/m/resume.py:1132, valence_core/m/resume.py:1135, RESULTS.md:6992, RESULTS.md:7730, RESULTS.md:7970, RESULTS.md:8381, RESULTS.md:9190 |
| runpod_volume_id (context: volume) | `o73q...[len 10]#e79618f8` | 759 (165) | 8 | 751 | 18 | HANDOFF-2026-08-20.md:120, HANDOFF-2026-08-22.md:50, HANDOFF-2026-08-24.md:159, HANDOFF-2026-08-25.md:186, HANDOFF-2026-09-01.md:232, HANDOFF-2026-09-05.md:218, HANDOFF-2026-09-06.md:264, HANDOFF-2026-09-12.md:362, RESULTS.md:8519, RESULTS.md:8679, RESULTS.md:9486, RESULTS.md:9918, RESULTS.md:9931, RESULTS.md:11759, RESULTS.md:12304, RESULTS.md:12316, results/raw/2026-08-22_podprep.txt:6, results/raw/2026-09-12_handoff_valuescheck.txt:143 | HANDOFF-2026-08-20.md:120, HANDOFF-2026-08-22.md:50, HANDOFF-2026-08-24.md:159, HANDOFF-2026-08-25.md:186, HANDOFF-2026-09-01.md:232, HANDOFF-2026-09-05.md:218, HANDOFF-2026-09-06.md:264, HANDOFF-2026-09-12.md:362, results/raw/2026-08-22_podprep.txt:6, results/raw/2026-09-12_handoff_valuescheck.txt:143, RESULTS.md:8224, RESULTS.md:8384, RESULTS.md:9191, RESULTS.md:9623, RESULTS.md:9636, RESULTS.md:11464, RESULTS.md:12009, RESULTS.md:12021 |
| runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size) | `holy...[len 23]#e6c48186` | 84 (84) | 1 | 83 | 2 | RESULTS.md:9919, results/raw/2026-08-22_podprep.txt:6 | results/raw/2026-08-22_podprep.txt:6, RESULTS.md:9624 |
| container_hostname (12 hex after host:/root@) | `e20d...[len 12]#54719d1e` | 1 (1) | 0 | 1 | 1 | results/raw/2026-08-25_b2r_arc.txt:3 | results/raw/2026-08-25_b2r_arc.txt:3 |
| ssh_port (number in an ssh/port/alias line) | `len5:dae17182` | 79 (79) | 1 | 78 | 1 | RESULTS.md:9539 | RESULTS.md:9244 |
| ssh_port (number in an ssh/port/alias line) | `len5:25124cd5` | 79 (79) | 1 | 78 | 1 | RESULTS.md:9540 | RESULTS.md:9245 |
| ssh_port (number in an ssh/port/alias line) | `len5:47e5fcc0` | 13 (13) | 0 | 13 | 2 | HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163 | HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163 |
| ssh_port (number in an ssh/port/alias line) | `len5:2be8ef0e` | 13 (13) | 0 | 13 | 2 | HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163 | HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163 |
| ssh_port (number in an ssh/port/alias line) | `len5:54e4496b` | 9 (9) | 0 | 9 | 1 | HANDOFF-2026-08-25.md:163 | HANDOFF-2026-08-25.md:163 |

IDENTIFIER values in tracked code (.py/.sh) at HEAD: valence_core/m/resume.py:1132,1135 (runpod_pod_id (context: pod) `uimu...[len 14]#a39ed293`: the real pod id used as the test value of resume.py's self-test of `pod_id()` reading RUNPOD_POD_ID (a fixture; nothing connects to it)).

IDENTIFIER values in history but not at HEAD: claude_session_or_artifact_link `clau...[len 47]#236329f4` (7 occ, first d4f21d15 <commit message>:30).

### Tracked files at HEAD containing `/Users/`

99 tracked files, 259 occurrences (byte-substring count of `/Users/` in each HEAD blob).

| group | files | occurrences | recommendation |
|---|---|---|---|
| code | 1 | 1 | see per-file note: parameterize only if the path is used at run time |
| data/ artifacts | 2 | 38 | leave: provenance fields recorded by the run; parameterizing would rewrite a committed artifact |
| documents | 1 | 1 | leave (the audit block quotes the pattern) |
| results/raw (raw stdout / review records) | 95 | 219 | leave: verbatim run records (rule 27); the paths are provenance of where a run executed, and nothing reads them |

| file | occurrences |
|---|---|
| `data/e2d/closure_valuescheck.json` | 37 |
| `results/raw/2026-09-18_k1_stop_entry_valuescheck_pass2.txt` | 20 |
| `results/raw/2026-09-09_k1_stage1_review.txt` | 14 |
| `results/raw/2026-10-08_m-gcal_completability_wait.txt` | 10 |
| `results/raw/2026-08-09_e2a_full.txt` | 9 |
| `results/raw/2026-09-06_format_recon_run.log` | 7 |
| `results/raw/2026-08-09_e2a_g2r_crash.txt` | 6 |
| `results/raw/2026-10-04_m-v1.8_referent_check.txt` | 6 |
| `results/raw/2026-10-05_m-v1.10_code_own_pass.txt` | 6 |
| `results/raw/2026-10-06_m-v1.11_code_own_pass.txt` | 6 |
| `results/raw/2026-10-07_m-gport_differences.md` | 6 |
| `results/raw/2026-09-09_k_launch_entry_valuescheck.txt` | 5 |
| `results/raw/2026-10-08_m-gcal-build_review.txt` | 5 |
| `results/raw/2026-09-06_format_recon_time.txt` | 4 |
| `results/raw/2026-10-08_m-gcal-build_selftest.txt` | 4 |
| `results/raw/2026-09-06_format_recon_review.txt` | 3 |
| `results/raw/2026-09-06_format_recon_run_refused-1613utc.log` | 3 |
| `results/raw/2026-09-11_addendum_k1_referent_check.txt` | 3 |
| `results/raw/2026-10-07_m-dispositions_selftest.txt` | 3 |
| `results/raw/2026-10-08_m-gcal_completability_qwen.txt` | 3 |
| `results/raw/2026-10-08_m-gcal_completability_qwen_refused-preflight.txt` | 3 |
| `results/raw/2026-10-08_m-gcal_model-free.txt` | 3 |
| `results/raw/2026-08-20_s2_extract_vignette.txt` | 2 |
| `results/raw/2026-09-02_e2d_tstep.txt` | 2 |
| `results/raw/2026-09-03_e2d_d3_scoring.txt` | 2 |
| `results/raw/2026-09-06_e2d_contentclass_screen_v4.txt` | 2 |
| `results/raw/2026-09-06_e2d_contentclass_screen_v4pre.txt` | 2 |
| `results/raw/2026-09-06_e2d_contentclass_screen_v4rev2pre.txt` | 2 |
| `results/raw/2026-09-07_format_recon_analyze.txt` | 2 |
| `results/raw/2026-09-08_e2d_contentclass_screen_v5.txt` | 2 |
| `results/raw/2026-09-09_k1_analyze_run.txt` | 2 |
| `results/raw/2026-09-09_k1_stage1_run.log` | 2 |
| `results/raw/2026-09-17_contentclass-v5-adoption_referent_check.txt` | 2 |
| `results/raw/2026-10-04_m-v1.7_referent_check.txt` | 2 |
| `results/raw/2026-10-05_m-v1.10_referent_check.txt` | 2 |
| `results/raw/2026-10-06_m-build_design.md` | 2 |
| `results/raw/2026-10-06_m-build_selftest.txt` | 2 |
| `results/raw/2026-10-07_m-dispositions_check.txt` | 2 |
| `AUDIT-note-release-v1_2.md` | 1 |
| `data/e0/s2_vignette_axis.meta.json` | 1 |
| `results/raw/2026-08-08_e0_b2a_full.txt` | 1 |
| `results/raw/2026-08-08_e0_b2a_smoke.txt` | 1 |
| `results/raw/2026-08-08_e0_b2b_full.txt` | 1 |
| `results/raw/2026-08-08_e0_b2c_a.txt` | 1 |
| `results/raw/2026-08-08_e0_b2c_smoke.txt` | 1 |
| `results/raw/2026-08-08_e0_extract_full.txt` | 1 |
| `results/raw/2026-08-08_e0_smoke.txt` | 1 |
| `results/raw/2026-08-09_e2a_analysis.txt` | 1 |
| `results/raw/2026-08-09_e2a_smoke.txt` | 1 |
| `results/raw/2026-08-09_e2a_smoke2.txt` | 1 |
| `results/raw/2026-08-09_e2a_smoke3.txt` | 1 |
| `results/raw/2026-08-10_f_run.txt` | 1 |
| `results/raw/2026-08-10_f_smoke.txt` | 1 |
| `results/raw/2026-08-10_f_smoke2.txt` | 1 |
| `results/raw/2026-08-10_f_smoke2r.txt` | 1 |
| `results/raw/2026-08-20_h1_power_flipgate.txt` | 1 |
| `results/raw/2026-08-20_h1_power_lockh_v1.txt` | 1 |
| `results/raw/2026-08-20_h3_tagscreen.txt` | 1 |
| `results/raw/2026-08-20_h3b_repair_screen.txt` | 1 |
| `results/raw/2026-08-20_lockh_verify.txt` | 1 |
| `results/raw/2026-08-20_lockh_verify_v11.txt` | 1 |
| `results/raw/2026-08-20_s1_judge_rescue.txt` | 1 |
| `results/raw/2026-08-20_s2_neighbor_axes.txt` | 1 |
| `results/raw/2026-08-21_h1_gate.txt` | 1 |
| `results/raw/2026-08-21_h1_gate_eval.txt` | 1 |
| `results/raw/2026-08-21_h1u_sessions.txt` | 1 |
| `results/raw/2026-08-21_h2_read_stability.txt` | 1 |
| `results/raw/2026-08-21_h2_sessions.txt` | 1 |
| `results/raw/2026-08-21_h2_sweep.txt` | 1 |
| `results/raw/2026-08-22_lockh_v2_valuescheck.txt` | 1 |
| `results/raw/2026-08-22_verdict_analysis.txt` | 1 |
| `results/raw/2026-08-22_verdict_campaign.txt` | 1 |
| `results/raw/2026-09-01_e2d_d1.txt` | 1 |
| `results/raw/2026-09-02_e2d_d2.txt` | 1 |
| `results/raw/2026-09-02_e2d_d2_scoring.txt` | 1 |
| `results/raw/2026-09-02_e2d_tstep_f010.txt` | 1 |
| `results/raw/2026-09-03_e2d_d3.txt` | 1 |
| `results/raw/2026-09-03_e2d_excision.txt` | 1 |
| `results/raw/2026-09-04_e2d_d2_allrounds_rescore.txt` | 1 |
| `results/raw/2026-09-06_format_recon_analyze_timing.txt` | 1 |
| `results/raw/2026-09-06_format_recon_checkgate.txt` | 1 |
| `results/raw/2026-09-09_k1_analyze_selftest.txt` | 1 |
| `results/raw/2026-09-09_k1_analyze_selftest_v11.txt` | 1 |
| `results/raw/2026-09-09_k1_stage1_selftest.txt` | 1 |
| `results/raw/2026-09-09_k1_stage1_selftest_v11.txt` | 1 |
| `results/raw/2026-09-17_e2d_contentclass_screen_v5_adopted.txt` | 1 |
| `results/raw/2026-09-17_e2d_v5_exclusion_parity.txt` | 1 |
| `results/raw/2026-09-17_v5_adoption_entry_valuescheck_pass2.txt` | 1 |
| `results/raw/2026-10-04_m-v1.6_STOP4_carryover_in_v1.7.txt` | 1 |
| `results/raw/2026-10-04_m-v1.8_stop6_valuescheck_pass2.txt` | 1 |
| `results/raw/2026-10-06_m-build_sitecheck.txt` | 1 |
| `results/raw/2026-10-07_m-dispositions-gport_valuescheck_pass2.txt` | 1 |
| `results/raw/2026-10-07_m-dispositions_sitecheck.txt` | 1 |
| `results/raw/2026-10-07_m-gport.txt` | 1 |
| `results/raw/2026-10-08_m-gcal-build_sitecheck.txt` | 1 |
| `results/raw/2026-10-08_m-gcal_sitecheck_post.txt` | 1 |
| `results/raw/2026-10-08_m-gcal_valuescheck_pass2.txt` | 1 |
| `results/raw/2026-10-08_note-preflight.md` | 1 |
| `valence_core/m/guard.py` | 1 |

Per-file note for code: `valence_core/m/guard.py` (1): every occurrence is the synthetic path `/Users/u/...` inside a canned process-list string a self-test parses; nothing reads it as a path -- no change needed. `README.md` contains `/Users/`: no.

Per-file note for data/ (does any tracked code read these paths?):

- `data/e0/s2_vignette_axis.meta.json` (1): /Users/ inside field(s) `frames_source` (1); tracked .py lines at HEAD naming the file or a field as a key: `scripts/s2_extract_vignette.py:156` (writes the key (dict literal), `frames_source`).
- `data/e2d/closure_valuescheck.json` (37): /Users/ inside field(s) `found` (21), `checkable_against` (15), `reasoning` (1); tracked .py lines at HEAD naming the file or a field as a key: `scripts/e2d_closure_verify.py:355` (comment, `closure_valuescheck`).

Recommendation: none of these files needs a change before release (the code hit is a test fixture; the data/ and raw paths are recorded provenance, not inputs -- see the per-file notes for the lines that name them); the README should not cite any of these paths.

Informational (not a secret; a second checker's note): `/Users/` paths at HEAD that point outside the repository: 22 occurrence(s) in 14 file(s), by kind: the home directory or a parent directory of the repository 12 (`results/raw/2026-10-04_m-v1.8_referent_check.txt`, `results/raw/2026-10-04_m-v1.8_stop6_valuescheck_pass2.txt`, `results/raw/2026-10-05_m-v1.10_referent_check.txt`, `results/raw/2026-10-07_m-dispositions_selftest.txt`, `results/raw/2026-10-08_m-gcal-build_selftest.txt`); a synthetic, elided or bare `/Users/` path (no real home directory) 3 (`AUDIT-note-release-v1_2.md`, `results/raw/2026-10-07_m-dispositions-gport_valuescheck_pass2.txt`, `valence_core/m/guard.py`); the Hugging Face cache (a public model's snapshot path) 3 (`results/raw/2026-10-05_m-v1.10_code_own_pass.txt`, `results/raw/2026-10-06_m-v1.11_code_own_pass.txt`, `results/raw/2026-10-07_m-gport_differences.md`); a conda environment named for another local project 2 (`results/raw/2026-10-08_m-gcal_completability_qwen_refused-preflight.txt`, `results/raw/2026-10-08_m-gcal_valuescheck_pass2.txt`); the Jupyter runtime directory (a kernel connection-file name) 1 (`results/raw/2026-10-08_m-gcal_completability_qwen_refused-preflight.txt`); the conda base installation's interpreter 1 (`results/raw/2026-10-08_note-preflight.md`). They disclose the author's local layout: the Jupyter runtime directory, the conda installation, and the name of a conda environment belonging to another local project -- `asi-...[len 15]#b86b377e` in 6 HEAD file(s) (`paper_analysis.ipynb`, `results/raw/2026-09-09_k_launch_entry_valuescheck.txt`, `results/raw/2026-10-08_m-gcal-build_review.txt`, `results/raw/2026-10-08_m-gcal_completability_qwen_refused-preflight.txt`, `results/raw/2026-10-08_m-gcal_valuescheck_pass2.txt`, `results/raw/2026-10-08_note-preflight.md`) -- equal to the notebook's kernel display name (the name is printed redacted here; it is public at HEAD in those files). Nothing to fix before release; listed so the PI is not surprised.

### Tracked files at HEAD containing `/workspace/` (box paths)

141 files, 292 occurrences.

| file | occurrences |
|---|---|
| `results/raw/2026-08-25_b2r_arc.txt` | 22 |
| `results/raw/2026-08-24_b2.txt` | 17 |
| `results/raw/2026-08-23_a3_a2.txt` | 12 |
| `results/raw/2026-08-23_a4.txt` | 12 |
| `results/raw/2026-10-08_m-gcal_valuescheck_pass2.txt` | 9 |
| `results/raw/2026-08-24_b3.txt` | 8 |
| `RESULTS.md` | 7 |
| `results/raw/2026-08-25_b2r_gates.txt` | 6 |
| `scripts/run_b2r.sh` | 6 |
| `results/raw/2026-08-23_a1_tagscreen.txt` | 5 |
| `results/raw/2026-08-24_cached_gate.txt` | 5 |
| `scripts/run_bphase.sh` | 5 |
| `valence_core/m/resume.py` | 5 |
| `data/olmo/a1_repair_roster.json` | 4 |
| `data/olmo/a1_roster.json` | 4 |
| `data/olmo/manifest.json` | 4 |
| `results/raw/2026-08-19_olmo_acquisition.txt` | 4 |
| `results/raw/2026-08-23_a1_repair.txt` | 4 |
| `results/raw/2026-08-23_a2_rerun.txt` | 4 |
| `scripts/box_determinism.py` | 4 |
| `scripts/box_rl_survey.py` | 4 |
| `valence_core/m/runner_olmo.py` | 4 |
| `results/raw/2026-10-08_m-gcal_valuescheck.txt` | 3 |
| `scripts/box_cast_equality_assert.py` | 3 |
| `scripts/box_respawn_check.py` | 3 |
| `scripts/box_scaffold_characterization.py` | 3 |
| `HANDOFF-2026-08-20.md` | 2 |
| `results/raw/2026-08-19_cast_equality_sft.txt` | 2 |
| `results/raw/2026-08-19_determinism_base.txt` | 2 |
| `results/raw/2026-08-23_respawn_determinism.txt` | 2 |
| `results/raw/2026-08-24_bphase_respawn.txt` | 2 |
| `results/raw/2026-08-24_respawn_determinism.txt` | 2 |
| `results/raw/2026-10-06_m-build_review.txt` | 2 |
| `scripts/box_acquire_olmo.py` | 2 |
| `scripts/box_b2r_concepts.py` | 2 |
| `scripts/box_smoke_olmo.py` | 2 |
| `CLAUDE.md` | 1 |
| `archive/CLAUDE-cycle1-2.md` | 1 |
| `data/olmo/a1_repair_base.json` | 1 |
| `data/olmo/a1_repair_dpo.json` | 1 |
| `data/olmo/a1_repair_instruct.json` | 1 |
| `data/olmo/a1_repair_sft.json` | 1 |
| `data/olmo/a1_tagscreen_base.json` | 1 |
| `data/olmo/a1_tagscreen_dpo.json` | 1 |
| `data/olmo/a1_tagscreen_instruct.json` | 1 |
| `data/olmo/a1_tagscreen_sft.json` | 1 |
| `data/olmo/a2_baserates_base.json` | 1 |
| `data/olmo/a2_baserates_dpo.json` | 1 |
| `data/olmo/a2_baserates_instruct.json` | 1 |
| `data/olmo/a2_baserates_sft.json` | 1 |
| `data/olmo/a3_axes_base.json` | 1 |
| `data/olmo/a3_axes_dpo.json` | 1 |
| `data/olmo/a3_axes_instruct.json` | 1 |
| `data/olmo/a3_axes_sft.json` | 1 |
| `data/olmo/a4_hijack_base.json` | 1 |
| `data/olmo/a4_hijack_dpo.json` | 1 |
| `data/olmo/a4_hijack_instruct.json` | 1 |
| `data/olmo/a4_hijack_sft.json` | 1 |
| `data/olmo/a4_instrument_base.json` | 1 |
| `data/olmo/a4_instrument_dpo.json` | 1 |
| `data/olmo/a4_instrument_instruct.json` | 1 |
| `data/olmo/a4_instrument_sft.json` | 1 |
| `data/olmo/b2_concepts_base.json` | 1 |
| `data/olmo/b2_concepts_dpo.json` | 1 |
| `data/olmo/b2_concepts_instruct.json` | 1 |
| `data/olmo/b2_concepts_sft.json` | 1 |
| `data/olmo/b2_fidelity_base.json` | 1 |
| `data/olmo/b2_fidelity_dpo.json` | 1 |
| `data/olmo/b2_fidelity_instruct.json` | 1 |
| `data/olmo/b2_fidelity_sft.json` | 1 |
| `data/olmo/b2_register_base.json` | 1 |
| `data/olmo/b2_register_dpo.json` | 1 |
| `data/olmo/b2_register_instruct.json` | 1 |
| `data/olmo/b2_register_sft.json` | 1 |
| `data/olmo/b2r_concepts_base.json` | 1 |
| `data/olmo/b2r_control_base.json` | 1 |
| `data/olmo/b2r_control_dpo.json` | 1 |
| `data/olmo/b2r_control_instruct.json` | 1 |
| `data/olmo/b2r_control_sft.json` | 1 |
| `data/olmo/b2r_explore_dpo.json` | 1 |
| `data/olmo/b2r_explore_instruct.json` | 1 |
| `data/olmo/b2r_explore_sft.json` | 1 |
| `data/olmo/b2r_qualify_base.json` | 1 |
| `data/olmo/b2r_qualify_dpo.json` | 1 |
| `data/olmo/b2r_qualify_instruct.json` | 1 |
| `data/olmo/b2r_qualify_sft.json` | 1 |
| `data/olmo/b2r_sampling_base.json` | 1 |
| `data/olmo/b2r_sampling_dpo.json` | 1 |
| `data/olmo/b2r_sampling_instruct.json` | 1 |
| `data/olmo/b2r_sampling_sft.json` | 1 |
| `data/olmo/b3_screen_base.json` | 1 |
| `data/olmo/b3_screen_dpo.json` | 1 |
| `data/olmo/b3_screen_instruct.json` | 1 |
| `data/olmo/b3_screen_sft.json` | 1 |
| `data/olmo/cached_gen_WITHDRAWN_v2.json` | 1 |
| `data/olmo/cached_gen_dpo.json` | 1 |
| `data/olmo/cached_gen_instruct.json` | 1 |
| `data/olmo/cached_gen_sft.json` | 1 |
| `data/olmo/cached_gen_v3.json` | 1 |
| `data/olmo/cached_gen_v3b.json` | 1 |
| `data/olmo/cast_equality_sft.json` | 1 |
| `data/olmo/determinism_base.json` | 1 |
| `data/olmo/rl_base.json` | 1 |
| `data/olmo/rl_dpo.json` | 1 |
| `data/olmo/rl_instruct.json` | 1 |
| `data/olmo/rl_sft.json` | 1 |
| `data/olmo/scaffold_base.json` | 1 |
| `data/olmo/scaffold_dpo.json` | 1 |
| `data/olmo/scaffold_instruct.json` | 1 |
| `data/olmo/scaffold_sft.json` | 1 |
| `results/raw/2026-08-19_olmo_hashes.txt` | 1 |
| `results/raw/2026-08-19_rl_survey_base.txt` | 1 |
| `results/raw/2026-08-19_rl_survey_dpo.txt` | 1 |
| `results/raw/2026-08-19_rl_survey_instruct.txt` | 1 |
| `results/raw/2026-08-19_rl_survey_sft.txt` | 1 |
| `results/raw/2026-08-19_scaffold_base.txt` | 1 |
| `results/raw/2026-08-19_scaffold_dpo.txt` | 1 |
| `results/raw/2026-08-19_scaffold_instruct.txt` | 1 |
| `results/raw/2026-08-19_scaffold_sft.txt` | 1 |
| `results/raw/2026-08-19_smoke_base.txt` | 1 |
| `results/raw/2026-08-19_smoke_dpo.txt` | 1 |
| `results/raw/2026-08-19_smoke_instruct.txt` | 1 |
| `results/raw/2026-08-19_smoke_sft.txt` | 1 |
| `results/raw/2026-08-24_cached_gate_WITHDRAWN_v2.txt` | 1 |
| `results/raw/2026-08-25_b2r_analysis.txt` | 1 |
| `results/raw/2026-10-06_m-build_design.md` | 1 |
| `results/raw/2026-10-06_m-build_pins.txt` | 1 |
| `scripts/a1_roster.py` | 1 |
| `scripts/box_a1_repair_screen.py` | 1 |
| `scripts/box_a1_tagscreen.py` | 1 |
| `scripts/box_a2_baserates.py` | 1 |
| `scripts/box_a3_extract.py` | 1 |
| `scripts/box_a4_hijack.py` | 1 |
| `scripts/box_a4_instrument.py` | 1 |
| `scripts/box_b2_concepts.py` | 1 |
| `scripts/box_b2_detection.py` | 1 |
| `scripts/box_b2r_campaign.py` | 1 |
| `scripts/box_b2r_sampling_smoke.py` | 1 |
| `scripts/box_b3_sessions.py` | 1 |
| `scripts/box_cached_gen_smoke.py` | 1 |
| `scripts/box_hash_checkpoints.py` | 1 |

## (v) Size

`git count-objects -vH` (stdout verbatim):

```
count: 2512
size: 283.22 MiB
in-pack: 0
packs: 0
size-pack: 0 bytes
prune-packable: 0
garbage: 26
size-garbage: 79.93 KiB
```

stderr: 26 lines, all `warning: garbage found: .git/objects/??/tmp_obj_*` (yes): temporary object files left in the local object store (consistent with an interrupted or concurrent object write); they are not objects, are unreachable from any ref, and are never pushed.

Tracked files at HEAD over 40 MB (MB = 10^6 bytes, MiB = 2^20; GitHub warns above 50 MiB and refuses above 100 MiB):

| file | bytes | MB | MiB | >50 MB | >50 MiB | >100 MB | >100 MiB |
|---|---|---|---|---|---|---|---|
| `data/olmo/a4_instrument_base.npz` | 50,681,977 | 50.682 | 48.334 | YES | no | no | no |
| `data/olmo/a4_instrument_instruct.npz` | 49,841,520 | 49.842 | 47.533 | no | no | no | no |
| `data/olmo/a4_instrument_dpo.npz` | 49,640,911 | 49.641 | 47.341 | no | no | no | no |
| `data/olmo/a4_instrument_sft.npz` | 48,112,115 | 48.112 | 45.883 | no | no | no | no |
| `data/e0/e0_b1_markers.npz` | 47,508,646 | 47.509 | 45.308 | no | no | no | no |

Over 50 MB: 1; over 50 MiB (GitHub's warning): 0; over 100 MB: 0; over 100 MiB: 0.

The 25 largest blobs reachable from any ref:

| # | blob | bytes | MB | MiB | path(s) | first commit | at HEAD? |
|---|---|---|---|---|---|---|---|
| 1 | `3b9e2f2b8c` | 50,681,977 | 50.682 | 48.334 | `data/olmo/a4_instrument_base.npz` | `0b3af200` | at HEAD (same blob) |
| 2 | `d1894607aa` | 49,841,520 | 49.842 | 47.533 | `data/olmo/a4_instrument_instruct.npz` | `0b3af200` | at HEAD (same blob) |
| 3 | `bce0bbc364` | 49,640,911 | 49.641 | 47.341 | `data/olmo/a4_instrument_dpo.npz` | `0b3af200` | at HEAD (same blob) |
| 4 | `adecc26575` | 48,112,115 | 48.112 | 45.883 | `data/olmo/a4_instrument_sft.npz` | `0b3af200` | at HEAD (same blob) |
| 5 | `47c775d240` | 47,508,646 | 47.509 | 45.308 | `data/e0/e0_b1_markers.npz` | `47ef4c73` | at HEAD (same blob) |
| 6 | `8e74772a5b` | 13,991,171 | 13.991 | 13.343 | `data/echo/stageC_reads.json` | `d04cd91a` | at HEAD (same blob) |
| 7 | `19611a2e67` | 10,686,436 | 10.686 | 10.191 | `data/echo/stageB_reads.json` | `e02619ce` | at HEAD (same blob) |
| 8 | `9e96bbd4b4` | 1,847,254 | 1.847 | 1.762 | `data/e2b/verdict_campaign.json` | `485cc940` | at HEAD (same blob) |
| 9 | `211951c8a5` | 1,546,508 | 1.547 | 1.475 | `data/f/sessions.jsonl` | `50906bfe` | at HEAD (same blob) |
| 10 | `084ff34701` | 1,409,848 | 1.41 | 1.345 | `data/k/k1_reads.json` | `7742e2c4` | at HEAD (same blob) |
| 11 | `3c3085f35e` | 1,325,040 | 1.325 | 1.264 | `data/e2b/h1_sessions.json` | `75272701` | at HEAD (same blob) |
| 12 | `4b1282ecfa` | 1,174,466 | 1.174 | 1.12 | `results/raw/2026-10-06_m-v1.11_referent_check.txt` | `05c4636d` | at HEAD (same blob) |
| 13 | `4fd4bf4445` | 1,174,352 | 1.174 | 1.12 | `data/e2b/h1u_sessions.json` | `6df2072a` | at HEAD (same blob) |
| 14 | `9682f96859` | 1,173,660 | 1.174 | 1.119 | `data/e2b/h1_sessions.json`, `data/e2b/h1u_sessions.json` | `b2d051b3` | path at HEAD, different content (this version history-only) |
| 15 | `37fdacec89` | 1,086,527 | 1.087 | 1.036 | `results/raw/2026-10-05_m-v1.10_referent_check.txt` | `9510af7e` | at HEAD (same blob) |
| 16 | `d6ff5ec407` | 1,009,256 | 1.009 | 0.963 | `data/e2a/sessions.jsonl` | `d49bb5d6` | at HEAD (same blob) |
| 17 | `bbc13ac671` | 985,746 | 0.986 | 0.94 | `data/e0/e0_axes.npz` | `3d0b4b7f` | at HEAD (same blob) |
| 18 | `1508dad814` | 980,554 | 0.981 | 0.935 | `results/raw/2026-10-05_m-v1.9_referent_check.txt` | `939905ae` | at HEAD (same blob) |
| 19 | `3a6a23352a` | 979,423 | 0.979 | 0.934 | `results/raw/2026-10-04_m-v1.8_referent_check.txt` | `5db07207` | at HEAD (same blob) |
| 20 | `bf3866b68f` | 933,680 | 0.934 | 0.89 | `RESULTS.md` | `cf8eb5b9` | at HEAD (same blob) |
| 21 | `72ea5bd129` | 910,102 | 0.91 | 0.868 | `RESULTS.md` | `988e5dfd` | path at HEAD, different content (this version history-only) |
| 22 | `66d0ac0a2c` | 893,354 | 0.893 | 0.852 | `RESULTS.md` | `54e41c9f` | path at HEAD, different content (this version history-only) |
| 23 | `d47e169592` | 882,783 | 0.883 | 0.842 | `RESULTS.md` | `5f7b968c` | path at HEAD, different content (this version history-only) |
| 24 | `fcbb0f2632` | 855,031 | 0.855 | 0.815 | `RESULTS.md` | `05c4636d` | path at HEAD, different content (this version history-only) |
| 25 | `97d8f74b23` | 825,451 | 0.825 | 0.787 | `RESULTS.md` | `9510af7e` | path at HEAD, different content (this version history-only) |

Largest blob anywhere in history: 50,681,977 bytes = 48.334 MiB (under GitHub's 100 MiB refusal limit; under its 50 MiB warning). Every locally visible ref is an ancestor of `origin/main` as this clone last saw it: yes -- so every blob reachable from them is already in history GitHub accepted on push. Refs that exist only on GitHub (branches pushed by other sessions and never fetched, `refs/pull/*`, remote-only tags) are not visible in this clone and were not scanned or size-checked; this audit uses no network.

Local object store: 2512 objects; reachable from no ref (the live refs at the run, not the pin): blob 16, commit 1 (4,173,467 bytes); this audit opens none of their contents (for an unreachable commit it reads only the header's committer time and parent, below). A push sends only objects reachable from the pushed refs, so these are not published by a visibility change.

Push history visible locally (remote-tracking reflogs under `.git/logs/refs/remotes/`, read as plain files; the email field of each line is never read out): `refs/remotes/origin/main`: 250 entries ('update by push' 250), every update a fast-forward: yes, every recorded value an ancestor of the ref's last value: yes, first entry `dfe25032e7` at 2026-07-18 00:17:06 -0400; `refs/remotes/origin/claude/handoff-doc-next-steps-oeccd1`: 4 entries ('fetch origin' 3, 'pull --rebase' 1), every update a fast-forward: yes, every recorded value an ancestor of the ref's last value: yes, first entry `0dd6f56453` at 2026-08-20 16:53:21 -0400. First push recorded: 2026-07-18 00:17:06 -0400 (`dfe25032e7`). Unreachable commit(s): `2591567095` (committer time 2026-07-17 17:00:36 -0400; before the first push: yes; in a remote-tracking reflog: no; in the local HEAD/branch reflogs: no; reachable commit with the same parent and subject: `8aa3ba1458` (14 s later)). So on local evidence no force-push was recorded and no unreachable commit was pushed from this clone. This cannot see pushes made from other machines between this clone's fetches (the `claude/handoff-doc-next-steps-oeccd1` branch was pushed from a cloud session -- see the gpgsig subsection), nor anything GitHub holds outside the refs.

**PI pre-flip steps (not run here; each needs the final HEAD, the network, or the PI's word):**

1. **A precondition of the end commit and the tag (the PI's to bind), not advice: every audit raw must be re-scanned before the release commit.** Re-run this script immediately before the release commit, with every raw, script and README of the end commit in place, and again at the release commit itself; its pre-release section (below, after (iv)) must show no redaction-rule value -- a RunPod pod or volume id, the volume name or its stem, an SSH port, the SSH signing-key fingerprint, the container hostname, the Claude session link or the pass-phrase-shaped value -- in any file the end commit adds, and no new value needing triage (round 4: among them any email address other than the service address and the commit identities' own -- the scan's only class of third-party personal data; a third party's name, postal address or phone number is not scanned for, so the pre-release line's CLEAN does not cover them). The commit identities' own metadata (the identity emails and the laptop hostname, public in the commit headers) is listed there for consistency with this raw's redaction and, as drafted (round 3), does not hold the tag; binding either part is the PI's call. This raw is a snapshot at `cf8eb5b9dd`; commits landing later -- the concurrent PROPOSAL-m session's, and the audit's own end commit -- are not covered by it. Evidence that a snapshot goes stale: after the round-2 run (at `bab921ce52`), `cf8eb5b9dd` added the first tracked file(s) under `data/m/ckpt/` (1: `data/m/ckpt/G-CAL_qwen.json`), a `-diff` path whose content `git log -p` does not print, which turned coverage limit (2) under (i-a) from 'never applied' into 'applies'. The tag should wait on a clean run.
2. `git ls-remote origin` and compare its refs with the refs table under Scope. Any extra branch or tag gets its own scan (re-run this script after fetching it) or is deleted before the visibility change. `refs/pull/*` refs cannot be deleted by the owner and become public with the repository.
3. GitHub-side surfaces that become public with the visibility change and cannot be checked offline: pull requests (titles, bodies, comments, review comments; `gh pr list --state all`; the `claude/handoff-doc-next-steps-oeccd1` branch came from a cloud session and may have a PR), issues and their comments, Actions runs with their logs and artifacts, the wiki, and releases with their assets. GitHub can keep commits that were force-pushed away from another machine reachable by sha (and through `refs/pull/*`); the local evidence above cannot rule that out.
4. The block's primary scanners, on the PI's word (installing them needs it): `brew install gitleaks trufflehog`, then `gitleaks detect --source . --log-opts="--all"` and `trufflehog git file://.` over the repository at the release commit. Their findings supersede the fallback's for (i).

**Pass/STOP line (v):** PASS -- nothing over 100 MB untreated (no tracked file at HEAD and no blob anywhere in history exceeds 100 MB or 100 MiB).

## (iv) mechanical checks

- `jlens-qwen36/` tracked at HEAD: 0 paths; ever tracked in history (`git log --all --name-only`, raw diffs, and `rev-list --objects` paths unioned): 0 paths. Gitlinks (mode 160000) at HEAD: 0. `.gitmodules` at HEAD: no.
- Content copies (the path check above cannot see them): every file in the jlens-qwen36/ working tree outside `.git/` and `.venv/` was read as a plain file (579 files; 46 whose size equals some reachable blob's size were hashed as git blobs). Byte-identical to a reachable blob: 42 -- 3 are the empty blob (`data/corpus/.gitkeep, data/lens/.gitkeep, jlens_qwen/__init__.py`; an empty file matches any empty tracked file, e.g. `.gitkeep`), and 39 are non-empty: `data/e2a/` 15, `data/e0/` 8, `data/configs/` 6, `data/f/` 6, `data/corpus/` 2, `data/d/` 2; 39 of them sit at the same relative path as their tracked copy (`jlens-qwen36/data/X` = `data/X`). Non-empty matches outside `data/`: 0. The non-empty matches are under the clone's `data/` only, in directories named for the lab's own experiments and configs (as listed); no non-empty file of the clone outside `data/` -- its code, LICENSE, README -- matches any reachable blob. (Every match is listed in the JSON, `jlens.content_copies`.)
- The clone's own index (round 2), read as a plain file -- no git process in the clone (`jlens-qwen36/.git/index`, version 2, trailing SHA-1 checksum verified): 62 clone-tracked entries, 59 with a non-empty blob. The working-tree comparison above cannot see a clone-tracked file whose working copy carries local patches; the index holds the blob sha of each file's committed version, which closes that gap. Of the 59 non-empty clone-tracked blob shas, reachable anywhere in the lab's history: 0. Clone-tracked files whose working copy differs from the index: 4 (`jlens_qwen/interventions.py`, `pyproject.toml`, `scripts/run_experiments.py`, `uv.lock`). Of the 39 non-empty byte-identical files above, clone-tracked: 0 -- the clone tracks only 4 path(s) under `data/` (`data/corpus/.gitkeep`, `data/lens/.gitkeep`, `data/lens/full_depth_fit.log`, `data/lens/full_depth_fit_v2.log`), so the matches are lab outputs written into the clone's untracked `data/`, not upstream material. The 3 empty-blob matches, clone-tracked: 3 (an empty file carries no content). So no upstream jlens-qwen36 file -- code, LICENSE, README or data -- is tracked in the lab's history, in its committed version or as patched on disk. (The N12-licenses raw reads the clone's object store for its own copy check of the upstream content.)
- Working-tree `.gitignore` byte-identical to HEAD's: yes. The allowlist lines below are read from HEAD's `.gitignore` blob; `git check-ignore --no-index -v` (which reads the working tree) is a cross-check, and its source line and pattern equal the HEAD explicit line for every npz: yes.

Every `.npz` path ever tracked: 17 (17 at HEAD). Allowlist = an explicit `!/<path>` line in `.gitignore`.

| npz path | at HEAD | HEAD bytes | versions | introduced | explicit line (HEAD .gitignore) | check-ignore -v (HEAD) | explicit line at introduction | members |
|---|---|---|---|---|---|---|---|---|
| `data/e0/e0_axes.npz` | yes | 985,746 | 1 | `3d0b4b7f` | :59 | `.gitignore:59:!/data/e0/e0_axes.npz` | :30 | axes_sha.npy, last_character.npy, last_neutral_mean.npy, last_reward.npy, last_sentiment.npy, layers.npy (+4) |
| `data/e0/e0_b1_markers.npz` | yes | 47,508,646 | 1 | `47ef4c73` | :71 | `.gitignore:71:!/data/e0/e0_b1_markers.npz` | :50 | cond.npy, mass_confidence.npy, mass_hedging.npy, para.npy, probe.npy, task_id.npy (+2) |
| `data/e0/e0_random_dirs.npz` | yes | 247,210 | 1 | `3d0b4b7f` | :60 | `.gitignore:60:!/data/e0/e0_random_dirs.npz` | :31 | L40.npy, L44.npy, L48.npy, L52.npy, L56.npy, L60.npy |
| `data/e0/s2_vignette_axis.npz` | yes | 492,350 | 1 | `1c8f5e17` | :65 | `.gitignore:65:!/data/e0/s2_vignette_axis.npz` | :56 | last_vignette.npy, layers.npy, span_vignette.npy |
| `data/olmo/a3_axes_base.npz` | yes | 431,176 | 1 | `f96fb7f9` | :78 | `.gitignore:78:!/data/olmo/a3_axes_base.npz` | :69 | layers.npy, span_character.npy, span_reward.npy, span_sentiment.npy |
| `data/olmo/a3_axes_dpo.npz` | yes | 431,176 | 1 | `f96fb7f9` | :80 | `.gitignore:80:!/data/olmo/a3_axes_dpo.npz` | :71 | layers.npy, span_character.npy, span_reward.npy, span_sentiment.npy |
| `data/olmo/a3_axes_instruct.npz` | yes | 431,176 | 1 | `f96fb7f9` | :81 | `.gitignore:81:!/data/olmo/a3_axes_instruct.npz` | :72 | layers.npy, span_character.npy, span_reward.npy, span_sentiment.npy |
| `data/olmo/a3_axes_sft.npz` | yes | 431,176 | 1 | `f96fb7f9` | :79 | `.gitignore:79:!/data/olmo/a3_axes_sft.npz` | :70 | layers.npy, span_character.npy, span_reward.npy, span_sentiment.npy |
| `data/olmo/a4_instrument_base.npz` | yes | 50,681,977 | 1 | `0b3af200` | :88 | `.gitignore:88:!/data/olmo/a4_instrument_base.npz` | :79 | cond.npy, probe.npy, sel_0.npy, sel_1.npy, sel_10.npy, sel_11.npy (+24) |
| `data/olmo/a4_instrument_dpo.npz` | yes | 49,640,911 | 1 | `0b3af200` | :90 | `.gitignore:90:!/data/olmo/a4_instrument_dpo.npz` | :81 | cond.npy, probe.npy, sel_0.npy, sel_1.npy, sel_10.npy, sel_11.npy (+24) |
| `data/olmo/a4_instrument_instruct.npz` | yes | 49,841,520 | 1 | `0b3af200` | :91 | `.gitignore:91:!/data/olmo/a4_instrument_instruct.npz` | :82 | cond.npy, probe.npy, sel_0.npy, sel_1.npy, sel_10.npy, sel_11.npy (+24) |
| `data/olmo/a4_instrument_sft.npz` | yes | 48,112,115 | 1 | `0b3af200` | :89 | `.gitignore:89:!/data/olmo/a4_instrument_sft.npz` | :80 | cond.npy, probe.npy, sel_0.npy, sel_1.npy, sel_10.npy, sel_11.npy (+24) |
| `data/olmo/b2_concepts_base.npz` | yes | 163,187 | 1 | `720a1045` | :98 | `.gitignore:98:!/data/olmo/b2_concepts_base.npz` | :89 | Cameras.npy, Constellations.npy, Illusions.npy, Lightning.npy, Origami.npy, Satellites.npy (+3) |
| `data/olmo/b2_concepts_dpo.npz` | yes | 163,002 | 1 | `720a1045` | :100 | `.gitignore:100:!/data/olmo/b2_concepts_dpo.npz` | :91 | Cameras.npy, Constellations.npy, Illusions.npy, Lightning.npy, Origami.npy, Satellites.npy (+3) |
| `data/olmo/b2_concepts_instruct.npz` | yes | 163,160 | 1 | `720a1045` | :101 | `.gitignore:101:!/data/olmo/b2_concepts_instruct.npz` | :92 | Cameras.npy, Constellations.npy, Illusions.npy, Lightning.npy, Origami.npy, Satellites.npy (+3) |
| `data/olmo/b2_concepts_sft.npz` | yes | 164,014 | 1 | `720a1045` | :99 | `.gitignore:99:!/data/olmo/b2_concepts_sft.npz` | :90 | Cameras.npy, Constellations.npy, Illusions.npy, Lightning.npy, Origami.npy, Satellites.npy (+3) |
| `data/olmo/b2r_concepts_base.npz` | yes | 164,973 | 1 | `b6e8f3f5` | :184 | `.gitignore:184:!/data/olmo/b2r_concepts_base.npz` | :175 | Cameras.npy, Constellations.npy, Illusions.npy, Lightning.npy, Origami.npy, Satellites.npy (+3) |

npz tracked without an explicit allowlist line at HEAD: 0.

Model-weight-shaped paths ever tracked (extensions .bin, .ckpt, .gguf, .gz, .h5, .joblib, .mlx, .model, .msgpack, .npy, .onnx, .pb, .pickle, .pkl, .pt, .pth, .safetensors, .tar, .tflite, .zip, or adapter/weights/model-* names): 0. Binary blobs by extension (all versions): .npz 17, .png 1.

**Residual-space vectors stored as JSON (round 2).** The npz allowlist check cannot see numeric vectors stored as JSON text, so every reachable JSON / JSONL / .ipynb blob (every version: 251 blobs; parsed 251, unparseable 0) was walked for all-numeric arrays of 256 or more elements. Float arrays: 6, in 2 blob(s):

| path(s) | blob | at HEAD | first commit | JSON pointer: length |
|---|---|---|---|---|
| `data/e2d/d2_scores.json` | `6454940d` | yes | `cd86e497` | `/readability/stored_classifier/mu`: 5120, `/readability/stored_classifier/sd`: 5120, `/readability/stored_classifier/w`: 5120 |
| `data/e2d/d3_scores.json` | `ab57d21c` | yes | `c6382899` | `/readability/stored_classifier/mu`: 5120, `/readability/stored_classifier/sd`: 5120, `/readability/stored_classifier/w`: 5120 |

Integer-only arrays of 256+ elements: 0.

Reading of the float arrays (Code read the writer in context): in `data/e2d/d2_scores.json`, `data/e2d/d3_scores.json`, `/readability/stored_classifier/{w,mu,sd}` (lengths [5120]) is a stored logistic readability probe -- its weight vector, and the per-dimension mean and standard deviation of its training features -- written by `scripts/e2d_score.py` (`fit_and_store` in `valence_core/e2d/readability.py`) over the model adapter's `embed`: the mean-pooled, post-norm final-layer residual of a generated text. These are residual-space vectors, but neither model weights nor raw activation captures (mu and sd are statistics over the fit set). No other float arrays of 256+ elements. So (iv)'s clause, stated exactly: no model weights are tracked; and no residual arrays are tracked beyond the allowlisted `.npz` files EXCEPT the probe vectors in JSON named here, which the README should name.

## Pre-release check: files not yet in history (round 2)

**Every audit raw must be re-scanned before the release commit.** The history scan above cannot see files that are not committed yet: the audit's own raws, scripts and README (which the end commit adds), the concurrent PROPOSAL-m session's pending outputs, and the PI's untracked documents. They are read here as plain files -- a snapshot at Thu Oct  8 11:20:48 UTC 2026, while other sessions are still writing them -- and scanned for (a) every value this run treats as sensitive (18 values: ssh_port (number in an ssh/port/alias line) 5, identity email, public in the commit headers 3, runpod_pod_id (context: pod) 2, SSH signing-key fingerprint 1, claude_session_or_artifact_link 1, container_hostname (12 hex after host:/root@) 1, laptop hostname 1, passphrase_shaped (code word / pass phrase / password context) 1, runpod volume name stem (the name without its _volume suffix) 1, runpod_volume_id (context: volume) 1, runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size) 1), exact and word-bounded; (b) any NEW value of a RunPod-id / volume-name / container / IPv4 / SSH fingerprint / SSH public key / session-link shape, any new 4-5 digit number on an ssh/port/alias line, and (round 4) any email address other than the service address and the commit identities' own -- a possible third party's personal data, and the only such class this scan has; (c) the 33 precise secret patterns, each triaged on its match's own line (round 4). This part's own two outputs are excluded (the leak assertion covers them). A port value is a 5-digit number, so its word-bounded count can include an unrelated number that happens to be equal. A new 4-5 digit number on an ssh/port/alias line of a pending file stays untriaged (and redacted) until Code reads it in context; if the same number also occurs in this raw as an unrelated count, the leak assertion refuses to write until it is triaged -- a safe failure that a re-run under pre-flip step 1 can meet (round 3 met it: counts on pending lines where 'port' means a code port; the code-port rule under (ii) now skips such lines -- this snapshot: 46 pending line(s), carrying 13 4-5 digit number(s)).

| group | files scanned | files with a sensitive value | files with a new value or an uncleared precise hit |
|---|---|---|---|
| audit outputs (this audit's end commit) | 52 | 1 | 0 |
| other untracked or modified files (the PI's documents) | 24 | 6 | 0 |

| group | file | status | sensitive values (redacted: occurrences) | new values (triage) | precise hits not cleared |
|---|---|---|---|---|---|
| audit outputs | `scripts/audit_note_N12_content.py` | untracked | `jaso...[len 21]#bb973c14` (identity email, public in the commit headers): 1 | - | - |
| other untracked or modified files | `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md` | untracked | `o73q...[len 10]#e79618f8` (runpod_volume_id (context: volume)): 1 | - | - |
| other untracked or modified files | `HANDOFF-2026-08-22-design.md` | untracked | `o73q...[len 10]#e79618f8` (runpod_volume_id (context: volume)): 1 | - | - |
| other untracked or modified files | `HANDOFF-2026-08-23-design.md` | untracked | `uimu...[len 14]#a39ed293` (runpod_pod_id (context: pod)): 1, `o73q...[len 10]#e79618f8` (runpod_volume_id (context: volume)): 1 | - | - |
| other untracked or modified files | `HANDOFF-2026-08-28-design.md` | untracked | `uimu...[len 14]#a39ed293` (runpod_pod_id (context: pod)): 1, `o73q...[len 10]#e79618f8` (runpod_volume_id (context: volume)): 1 | - | - |
| other untracked or modified files | `HANDOFF-2026-09-04-design.md` | untracked | `o73q...[len 10]#e79618f8` (runpod_volume_id (context: volume)): 1 | - | - |
| other untracked or modified files | `archive/PROPOSAL-m-gating-campaign-v1_3.md` | untracked | `o73q...[len 10]#e79618f8` (runpod_volume_id (context: volume)): 1 | - | - |

**Pre-release line, redaction-rule values** (RunPod pod/volume ids, the volume name and its stem, SSH ports, the SSH signing-key fingerprint, the container hostname, the Claude session link, the pass-phrase-shaped value; or a new value needing triage -- among them, round 4, an email address other than the service address and the commit identities' own -- or an uncleared precise hit; email addresses in the audit's pending files at this snapshot: the service address 10, a commit identity's 1, other 0): CLEAN for the audit's own pending files at this snapshot. Its coverage of third-party personal data is the email-address class only (round 4): a third party's name, postal address or phone number is not scanned for. Files of the other groups matter only if they are committed before the flip; the history re-run at the release commit (pre-flip step 1) covers whatever is.

**Pre-release line, the commit identities' own metadata** (the identity emails -- the author's and the Claude Cowork tool identity's -- and the laptop hostname, all public in the commit headers of the history being published: `jaso...[len 21]#bb973c14` (identity email, public in the commit headers) in 593 author/committer/tagger header line(s), `Jaso...[len 26]#2ed76856` (laptop hostname) in 4 author/committer/tagger header line(s), `clau...[len 30]#ab2650f2` (identity email, public in the commit headers) in 4 author/committer/tagger header line(s), `jaso...[len 37]#e1489bcc` (identity email, public in the commit headers) in 4 author/committer/tagger header line(s)): 1 audit file(s) carry only such a value: `scripts/audit_note_N12_content.py` (`jaso...[len 21]#bb973c14` x1). Listed for consistency with this raw's own redaction policy, which redacts them; the routing's redaction rule covers third-party personal data, not the commit identities' own public header metadata, so this is not a routing violation and, as drafted, not a blocker (the PI's call). A third party's email address would count under the line above (round 4), not here.

## Summary lines

- (i): STOP pending the PI's resolution (literal :77); the block's primary scanners (gitleaks, trufflehog) NOT run (installable, not installed: no install without the PI's word; pre-flip step 4); fallback 7782 hit lines (token 7440, sk- 287, secret 60, rp_ 9, password 6, api_key 0, BEGIN 0, AKIA 0); precise scan (33 patterns) 42 distinct values in blobs/messages, 7 in headers, 0 in binary string content; in-context high-entropy 49 distinct; context-free high-entropy 123 distinct in blobs/messages, 8 in headers, 0 in binary content; TRUE-SECRET-CANDIDATE 0; UNTRIAGED 0.
- (ii): RunPod pod ids 2, network volume ids 1, network volume names 1, SSH ports 5, container hostnames 1, Claude session links 1, IP addresses identifying a machine 0; in blob/message content SSH key names / fingerprints / public keys 0 / 0 / 0; in commit headers 1 SSH signing public key(s) (SHA2...[len 50]#488bbe90) in 7 gpgsig headers (PUBLIC-KEY, not a credential); the author's laptop hostname in 2 commits' author/committer emails (metadata); tagger identities 1; local temp paths 88 distinct, ~/.claude/projects paths 4 distinct; /Users/ in 99 HEAD files, /workspace/ in 141. A list, no pass condition; none is a credential.
- (v): PASS; largest blob 50,681,977 bytes; files at HEAD over 50 MB 1, over 50 MiB 0, over 100 MB 0.
- (iv)-mechanical: jlens-qwen36 paths ever tracked 0; jlens files byte-identical to a reachable blob 42 (3 empty, 39 lab data files, 0 outside data/); clone-index non-empty blobs reachable in lab history 0 of 59; npz without an explicit line 0; weight-shaped paths 0; residual-space float vectors in tracked JSON 6 array(s) in 2 blob(s) (`data/e2d/d2_scores.json`, `data/e2d/d3_scores.json`).
- Pre-release (files not yet in history, snapshot): 76 files scanned; audit files carrying a redaction-rule value or an untriaged value 0; audit files carrying only the commit identities' own metadata (public in the commit headers; listed, not a blocker as drafted) 1 (`scripts/audit_note_N12_content.py`); the end commit waits on a clean re-run (pre-flip step 1).

## Values-check

The builder's raw (script sha256 `bd80512c...1a2d`, run at `bbc9ffe72f`) was checked by an adversarial checker, who re-ran it, re-derived its counts by other methods and returned 9 findings plus a list of missed items. Code (the fixer) applied every finding that its own tool runs confirmed; none was rejected. Each disposition below carries this run's evidence. 3 commit(s) landed on top of the base after the builder's run (`cf8eb5b9dd`, `bab921ce52`, `c75d4d8aa3`), from the concurrent PROPOSAL-m session (G-CAL, step 6). This run scans the state at `cf8eb5b9dd`. The `at base` figures (base `bbc9ffe72f`, the builder's and the checker's commit) are the total minus the new-since column, which makes them directly comparable with the checker's numbers.

1. **F1 (substantive) -- ssh_port `#25124cd5` reported as 1 occurrence, HEAD 0 (line-scoped count; the exact recount skipped the ssh_port class).** APPLIED. Every SSH port whose individual triage is IDENTIFIER is now re-counted exactly (word-bounded: no letter or digit on either side, so a run inside a hex hash or a longer number does not count). The identifier table now has an `exact occ / HEAD / new` column for ports, and a new table lists every IDENTIFIER value present at HEAD with its locators, for the PI's decision. This run: `len5:25124cd5`: 79 occ in 79 sources now (1 in 1 new sources), HEAD 1 (RESULTS.md:9540); at base 78 in 78, base HEAD 1 (RESULTS.md:9245); checker 78 in 78, HEAD 1 (RESULTS.md:9245): AGREES; `len5:dae17182`: 79 occ in 79 sources now (1 in 1 new sources), HEAD 1 (RESULTS.md:9539); at base 78 in 78, base HEAD 1 (RESULTS.md:9244); checker 78 in 78, HEAD 1: AGREES; `len5:47e5fcc0`: 13 occ in 13 sources now (0 in 0 new sources), HEAD 2 (HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163); at base 13 in 13, base HEAD 2 (HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163); checker 13 in 13, HEAD 2: AGREES; `len5:2be8ef0e`: 13 occ in 13 sources now (0 in 0 new sources), HEAD 2 (HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163); at base 13 in 13, base HEAD 2 (HANDOFF-2026-08-24.md:140, HANDOFF-2026-08-25.md:163); checker 13 in 13, HEAD 2: AGREES; `len5:54e4496b`: 9 occ in 9 sources now (0 in 0 new sources), HEAD 1 (HANDOFF-2026-08-25.md:163); at base 9 in 9, base HEAD 1 (HANDOFF-2026-08-25.md:163); checker 9 in 9, HEAD 1: AGREES.
2. **F2 (substantive) -- 'Coverage limits of the fallback, both closed by (i-b)'; '(i-b) covers both'; 'incl. `data/m/ckpt/**`'. (i-b) did not scan binary blobs, and no ckpt file was ever tracked.** APPLIED, both remedies. Paths under data/m/ckpt/ ever tracked: 0 at rounds 1 and 2 (the -diff limit was stated as never having applied); 1 in this run, so (i-a) now states that it applies and names the commit (see round 3, R3-2). 'incl. data/m/ckpt/**' is removed. A binary-content scan is added: 208 npz members, dtypes <f4 72, <i8 60, <f8 60, <i4 5, <U3 5, <U8 5, <U16 1; 11 unicode members decoded; 1,310 ASCII runs; PNG text-chunk keywords ['Software']. Hits: precise 0, identifier 1 (url_host: PUBLIC), context-free 0. The checker reported 208 members, 11 unicode members (<U3 x5, <U8 x5, <U16 x1), one tEXt 'Software', and 0 hits over 26 patterns.
3. **F3 (minor) -- 'SSH key names / fingerprints / public keys 0 / 0 / 0': commit headers were never scanned; 7 gpgsig headers embed one ed25519 key.** APPLIED. Every commit header (307) and tag header (1) is now scanned in its own subsection. Signed commits: 7. Distinct keys: 1 (ssh-ed25519, namespace git, sha512, fingerprint SHA2...[len 50]#488bbe90, 7 commits). Verdict PUBLIC-KEY, not a credential. The checker reported the same key, SHA2...[len 50]#488bbe90, in 7 commits. The '0 / 0 / 0' line is now scoped to blob and message content.
4. **F4 (minor) -- the tagger of annotated tag cycle-4-close is not enumerated.** APPLIED. The identities table has a tagger row (Jason Dwyer `jaso...[len 21]#bb973c14`: cycle-4-close). The address over all headers: `jaso...[len 21]#bb973c14` 593 in headers now (6 in new commit headers), at base 587. The checker reported 587 = 2 x 293 + 1 at the base.
5. **F5 (minor) -- the temp-path class missed temp paths without /private and ~/.claude/projects session paths.** APPLIED. The class is widened to `(?:/private)?/(?:tmp|var/folders)/...`, with a left boundary (no word character, '.', '-', '/' or '~' before it, so the /tmp inside /private/tmp and relative 'x/tmp/' paths do not count). A class `claude_projects_path` is added. This run: temp paths 88 distinct, 224 occ, 136 at HEAD. Of these, /var/folders without /private: 7 distinct, 7 at HEAD in 3 files (results/raw/2026-10-06_m-build_selftest.txt, results/raw/2026-10-07_m-dispositions_selftest.txt, results/raw/2026-10-08_m-gcal-build_selftest.txt); at the base's HEAD 4 in 2 files. Bare /tmp/: 11 distinct, 16 at HEAD in 13 files; at the base's HEAD 16 in 13 files. ~/.claude/projects: 4 distinct, 7 occ, 5 at HEAD (0 new; at the base's HEAD 5). The checker's comparison command, `git grep -c -E '(^|[^e])/tmp/' cf8eb5b9dd`, gives 14 matching lines in 13 files at this HEAD. It also counts relative 'x/tmp/' paths. The checker reported: /var/folders without /private 4 at HEAD in 2 files, bare /tmp/ about 16 in 13 HEAD files, ~/.claude/projects 4 distinct / 7 history / 5 HEAD.
6. **F6 (minor) -- the reason text for `#f1412386` spells the value out.** APPLIED. The reason now reads: 'outline numbering inside a model-generated response in a B2-r control trial; not an address'. It does not spell the digits. The builder's returned summary sentence is not carried into this raw. Not changed: the loopback value's redacted form identifies it (it names no machine). Round 2 changed the port form: ports now print as length + sha8 only (see the round-2 list).
7. **F7 (minor) -- 'HF_TOKEN' (twice, in a Hugging Face Hub warning) counted under T1 'LLM-token sense'.** APPLIED. New rule T2 'credential-sense word, no value follows'. A credential-sense word followed by '=', ':' or '=>' would go to T3, individual inspection. This run: T2 2 (2b21c72c results/raw/2026-08-19_cast_equality_sft.txt:+5, 75939edb results/raw/2026-08-19_olmo_acquisition.txt:+3), T3 0, T1 8152. Verdict unchanged (FALSE-POSITIVE: no value follows). The checker's further reading, which Code shares: the warning shows those downloads ran without a token.
8. **F8 (minor) -- the 'every scanned ref is an ancestor ... none could block a push' sentence says nothing about refs that exist only on GitHub.** APPLIED as text. Ancestry was re-verified for the 5 local refs (all yes). The sentence is now scoped to the locally visible refs. The PI pre-flip steps under (v) add a re-run at the release commit (step 1) and `git ls-remote origin` (step 2). Not run: they need the final HEAD and the network.
9. **F9 (minor, referent) -- the block names N12's output `results/raw/<stamp>_note-N12-scrub.md` (:84).** APPLIED. A referent note in the header names the three N12 raws.
10. **Missed: context-free secret scan (checker: 44 distinct, all false positives, among them 8 SSH-signature lines; lowercase+digit: 2 macOS temp-dir names).** APPLIED. A context-free scan runs over blobs and messages (123 distinct: FALSE-POSITIVE 67, LOCAL-PATH 55, IDENTIFIER 1; lowercase+digit runs 3; present at the base: 109 distinct, of them 2 lowercase+digit), headers (8 distinct, 8 of them SSH-signature lines) and binary content (0). The counts differ from the checker's by design: this scan has no word-segment pre-filter, so every run is counted and triaged, and paths are cleared by the triage rather than skipped. No value is a secret.
11. **Missed: extended patterns (JWT, Stripe, Slack/Discord webhooks, SendGrid, Telegram, PyPI/npm, ya29, legacy 32-char uppercase RunPod shape, PuTTY, secret-bearing URL query parameters, quoted key/secret/password/auth assignments: 40 distinct, all labels).** APPLIED. The 14 patterns (the PGP block among them) were added to (i-b) and run over every source class (round 2 added two more; see R2-6). Hits: jwt 0, stripe_key sk_/pk_/rk_ live/test 0, slack_webhook 0, discord_webhook 0, sendgrid_key SG. 0, telegram_bot_token 0, pypi_token 0, npm_token 0, google_oauth ya29. 0, upper32 (legacy RunPod-key shape: 32-40 uppercase+digit) 0, putty_private_key 0, url_secret_query_param 0, quoted_secretish_assignment 41, pgp_signature_or_key_block 0. Quoted assignments: 41 distinct, 54 occurrences (40 distinct present at the base), verdicts FALSE-POSITIVE 41.
12. **Missed: content copies of jlens-qwen36 (checker: 37 files under jlens-qwen36/data/ byte-identical to tracked blobs, over 520 working-tree files).** APPLIED. This run read 579 files and hashed the 46 whose size matched. Matches: 42 -- 3 empty-blob matches and 39 non-empty, all under the clone's data/, 0 outside it. The checker's 37 / 520 was not reconciled at round 1 (its file list and selection rule were not in its report); round 2 settles it: the second checker's independent re-run reproduced 579 / 46 / 42 / 39 (files / hashed / matches / non-empty matches) exactly; this run: 579 / 46 / 42 / 39 (equal). Round 2 also adds the clone-index evidence under (iv), which is what supports the conclusion: no upstream jlens code, LICENSE, README or data is tracked.
13. **Missed: remote-only refs (`git ls-remote origin` before the flip).** APPLIED as the PI pre-flip step 2 (see F8).
14. **Missed: local unreachable objects (checker: 16 blobs and 1 commit).** APPLIED. This run: blob 16, commit 1 (4,173,467 bytes) of 2512 objects in the store. They are not pushed.
15. **Missed: 'continuity' over history (checker: 948 occurrences in 25 files; 'continuity password' 3 times, no value follows).** APPLIED. This run: 964 occurrences in 149 sources (every blob version and message; 25 distinct paths), 64 at HEAD; at base 950 occurrences in 25 distinct paths. The phrase occurs 3 times, followed by a value 0 times. Distinct paths at base 25 against the checker's 25 files. Occurrences at base 950 against the checker's 948: a gap of 2. Code did not reproduce it: a word-bounded count gives 964 (total) against the substring count's 964, and 'discontinuity' occurs 0 times. The checker's counting rule is not in its report.
16. **Missed: tagger identity; HF_TOKEN; temp paths; headers; ports; binary contents.** See F4, F7, F5, F3, F1 and F2.

Checker's verdict summary, unchanged by these fixes: no secret in the history, and none of the builder's pass or STOP lines needed to change. The two statements it called wrong (F1, F2) are corrected above.

## Values-check, round 2

The round-1 fixer's outputs (script sha256 `4f5859c5...723e`, md `4008afec...f5f4`, json `dc73e0c8...58f4`, all at `bab921ce52`) were checked by a second adversarial checker. It re-ran the script (identical apart from the stamp and the command line), found the redaction clean in all three files, re-derived the counts by other methods, and returned 7 findings (1 substantive, 6 minor) plus 8 missed items. Dispositions below; each carries this run's evidence. Actions: FIXED, DEFERRED (to another item), DISCLOSED.

1. **R2-1 (substantive) -- N13's pending raw quotes the full RunPod pod id `uimu...[len 14]#a39ed293` (N13 md:643, json:8321/8410/8916); this part's scope (history at bab921ce52) cannot see it.** DEFERRED to item N13 -- its files are N13's, and this part edits only its own. Kept here as a pre-release check, as routed: 'every audit raw must be re-scanned before the release commit'. Built: the new pre-release section reads every file not yet in history (untracked, non-ignored, or modified) and scans it for every sensitive value of this run, for new id-shaped values and for the precise patterns; pre-flip step 1 is now worded as a precondition of the end commit and the tag, not as advice (binding it is the PI's call). This run's snapshot for N13: `results/raw/2026-10-08_note-N13-provenance.json`: clean; `results/raw/2026-10-08_note-N13-provenance.md`: clean. The checker's six non-audit files with the volume or pod id: this run finds `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md`, `HANDOFF-2026-08-22-design.md`, `HANDOFF-2026-08-23-design.md`, `HANDOFF-2026-08-28-design.md`, `HANDOFF-2026-09-04-design.md`, `archive/PROPOSAL-m-gating-campaign-v1_3.md` (6 file(s) in the 'other' group with a sensitive value); they matter only if committed.
2. **R2-2 (minor) -- '1,793,055 lines' for `git log -p --all` is one too high.** FIXED. The count is now the newline count: 1,798,487 lines over 70,058,328 bytes (the stream ends with a newline: yes). Round 1 printed the length of `split(b'\n')`, which also counts the empty piece after the final newline. The grep's line numbers and the locator index are unaffected.
3. **R2-3 (minor) -- 'not installed (and were not installed), so the block's fallback applies' is imprecise: block :77 runs the fallback only if the scanners are not installable.** FIXED (wording and evidence). `which`: gitleaks not found, trufflehog not found; Homebrew present (`/opt/homebrew/bin/brew`); its local formula index (`~/Library/Caches/Homebrew/api/formula.jws.json`, cached 2026-08-06, read as a file) lists gitleaks 8.30.1 (MIT), bottle for `arm64_sequoia`: yes, trufflehog 3.96.0 (AGPL-3.0-only), bottle for `arm64_sequoia`: yes. So both are installable here and were not installed, because the PI's routing forbids installs without the PI's word. (i-a) now says plainly that the block's primary scanners have NOT been run over this history, that running the fallback instead is a deviation from :77, and that the fallback plus Code's blob-level scans stand in for them; PI pre-flip step 4 gives the scanner commands.
4. **R2-4 (minor) -- the jlens 'no code, LICENSE or README is tracked' claim rested on a working-tree comparison, which cannot see clone-tracked files whose working copies carry local patches.** FIXED. (iv) now reads the clone's index as a plain file (no git process in the clone): version 2, checksum verified, 62 entries, 59 non-empty; non-empty index blob shas reachable in the lab's history: 0; clone-tracked files differing on disk: 4 (`jlens_qwen/interventions.py`, `pyproject.toml`, `scripts/run_experiments.py`, `uv.lock`); of the 39 non-empty byte-identical files, clone-tracked: 0; the clone's tracked `data/` paths: `data/corpus/.gitkeep`, `data/lens/.gitkeep`, `data/lens/full_depth_fit.log`, `data/lens/full_depth_fit_v2.log`. All agree with the checker (62 entries; 0 reachable; none of the 39 clone-tracked; 2 .gitkeep and 2 lens fit logs under data/). Round-1 item 12 now records that the second checker reproduced 579 / 46 / 42 / 39, which settles the first checker's 37 / 520.
5. **R2-5 (minor) -- (iv)'s 'no model weights or residual arrays beyond the allowlisted .npz' missed residual-space vectors stored as JSON.** FIXED. Every reachable JSON / JSONL / .ipynb blob (251; parsed 251) is walked for all-numeric arrays of 256+ elements. Float arrays: 6: `data/e2d/d2_scores.json` `/readability/stored_classifier/mu` 5120 (blob `6454940d`, at HEAD); `data/e2d/d2_scores.json` `/readability/stored_classifier/sd` 5120 (blob `6454940d`, at HEAD); `data/e2d/d2_scores.json` `/readability/stored_classifier/w` 5120 (blob `6454940d`, at HEAD); `data/e2d/d3_scores.json` `/readability/stored_classifier/mu` 5120 (blob `ab57d21c`, at HEAD); `data/e2d/d3_scores.json` `/readability/stored_classifier/sd` 5120 (blob `ab57d21c`, at HEAD); `data/e2d/d3_scores.json` `/readability/stored_classifier/w` 5120 (blob `ab57d21c`, at HEAD). Integer-only arrays of that size: 0. (iv) names the two files and restates the clause exactly: a stored logistic readability probe (weights, and the per-dimension mean and sd of its residual-space training features), not model weights and not raw captures. The checker reported the same two files, blobs 6454940d and ab57d21c, 3 x 5120 floats each.
6. **R2-6 (minor) -- the 4.3 bits/char bar misses structured base64 (7 of 15 gpgsig armor lines); no base64 key-material marker patterns.** FIXED. Stated in (i-b) with this run's numbers: armor body lines of 16+ characters 15, at or below 4.3: 7 (entropy 3.985-4.154); strict-base64 runs of 64+ characters in blobs and messages 1, at or below 4.3: 0. Two marker patterns added (precise patterns 32-33): pkcs_der_base64 (a run starting MII, 64+ characters: DER-encoded PKCS#1/#8 key or X.509 body): blobs/messages 0, headers 0, binary content 0; ssh_key_material_base64 (openssh-key-v1 / ssh-rsa / ssh-ed25519 / ecdsa / ssh-dss markers): blobs/messages 0, headers 7, binary content 0. Header hits sit inside the gpgsig signatures and are triaged SSH-SIGNATURE (round 2 said the marker was the signer's public key blob; round 3 corrected the mechanism: it is the key-type string that opens the signature field -- see R3-3); a hit anywhere else would be UNTRIAGED and hold (i) PENDING. The checker reported 15 / 7 (3.98-4.15), 5 mixed-case base64 runs of 64+ none below (its alphabet and boundaries are not in its report; this run's strict definition is stated in (i-b)), and 0 markers outside the 7 signature headers.
7. **R2-7 (minor) -- the pre-flip list omits GitHub-side surfaces that the visibility change publishes.** FIXED. Pre-flip step 3 lists pull requests (titles, bodies, comments, review comments), issues, Actions runs, logs and artifacts, the wiki, releases and their assets, and commits force-pushed away from another machine that GitHub can keep reachable by sha or through `refs/pull/*`. The local evidence is now in (v), from the remote-tracking reflogs: `refs/remotes/origin/main` 250 entries, all fast-forward: yes; `refs/remotes/origin/claude/handoff-doc-next-steps-oeccd1` 4 entries, all fast-forward: yes; first push 2026-07-18 00:17:06 -0400 at `dfe25032e7`; unreachable commit `2591567095` at 2026-07-17 17:00:36 -0400, before the first push: yes, in a remote reflog: no, replaced by `8aa3ba1458` 14 s later. The checker reported 249 entries, no force-push, first push 2026-07-18 00:17 (-0400) at dfe2503, and 2591567 replaced 14 s later by 8aa3ba1 before any push.
8. **Missed (informational) -- `/Users/` paths at HEAD and the notebook's kernel display name disclose another local project's conda env name and the Jupyter runtime directory.** ADDED as one informational line in (ii): 22 outside-repository `/Users/` occurrences by kind; the env name (redacted) in 6 HEAD files. Nothing to fix before release.
9. **Missed (informational) -- the prescribed form prints values of 4 characters or fewer in full and 4 of 5 digits of a port.** FIXED for ports, by the routing's direction: every one of the 9 SSH-port-class values (real ports, process ids, a token-window length, a local viewer port) now prints as `lenN:hhhhhhhh` -- no digit -- in the md and the JSON; old-form port strings left in the md before this section: 0. DISCLOSED for the rest: values of 4 characters or fewer that the generic form prints in full: 27 distinct. In the identifier tables: 1 (`podZ...[len 4]#7323177b`: the synthetic RUNPOD_POD_ID test value, FALSE-POSITIVE). The other 26 are in the JSON's `fallback.credential_shaped` records only -- the word or code token after a key such as `token:` (a prose word, a label, a code fragment), each cleared by its value class; none is a credential. No sensitive value is short enough to reach the generic form in full: the script refuses to redact a sensitive value of 4 characters or fewer.
10. **Missed -- pending audit outputs; scanners; clone index; JSON vectors; structured base64; GitHub surfaces.** See R2-1, R2-3, R2-4, R2-5, R2-6 and R2-7.
11. **Routing -- cover the commits after bbc9ffe up to the current HEAD.** DONE. This run scans HEAD `cf8eb5b9dd` (pinned at start; refs at end unchanged), which includes the 3 commit(s) after `bbc9ffe72f`: `c75d4d8aa3`, `bab921ce52`, `cf8eb5b9dd`. Every table's `new since base` column counts them. The final re-run at the release commit is still required (pre-flip step 1).

Second checker's verdict, unchanged by these fixes: no secret in the history; no pass or STOP line changes. (i) stays STOP pending the PI on the block's literal text, and now also records that the primary scanners were not run; (v) PASS; (iv)-mechanical passes and names the two JSON probe files.

## Values-check, round 3

The round-2 fixer's outputs (script sha256 `2b72c9ad...9c6c`, md `401d4631...3e3e`, json `a26505a0...c927`, all at `bab921ce52`) were checked by a third, strict checker. It re-ran the script at `bab921ce52` (md identical apart from the stamp line, the command echo, the pre-release snapshot stamp and the order of 4 tied categories in one sentence; JSON apart from its stamps and the excluded-path list), found the redaction clean in all three files, re-derived the counts, re-ran the script in scratch at `cf8eb5b9dd`, and returned 6 findings (1 substantive, 5 minor). Dispositions below, then Code's own addition and the routing's direction; each carries this run's evidence. Actions: FIXED, TRIAGED, DONE.

1. **R3-1 (substantive) -- the RunPod network-volume NAME is in the record and the raw never finds it; it is not in the pre-release sensitive set, so pre-flip step 1 could not catch a pending audit raw quoting it.** FIXED. New identifier class `runpod_volume_name (a ..._volume name, or a word-joined name before a GB/TB size)` (pattern under (ii); two alternatives: a word-joined name ending in `_volume`/`-volume`, or a word-joined name of 3+ parts directly before a size in GB/TB, the volume listing's name column), exactly re-counted, triaged by hash, and added to the pre-release scan's new-value classes (whose group selection now matches the history scan's). This run: 2 distinct values in the class (FALSE-POSITIVE 1, IDENTIFIER 1; FALSE-POSITIVE `upda...[len 21]#84cbedd5`: the RunPod MCP tool name `update-network-volume`, cited in prose explaining that a network volume cannot be moved between datacenters (the tool renames and grows only); a public API operation's name, not a volume name). `holy...[len 23]#e6c48186`: exact, word-bounded 84 occ in 84 sources (83 blob versions + 1 message(s)) now, 1 new since the base, 83 at the base; at the round-2 snapshot `bab921ce52` 83 in 83 (82 + 1) against the checker's 83 in 83 (82 + 1): AGREES. HEAD 2 (RESULTS.md:9919, results/raw/2026-08-22_podprep.txt:6); at the base `bbc9ffe72f` 2 (results/raw/2026-08-22_podprep.txt:6, RESULTS.md:9624); the checker's locators at `bab921ce52` (RESULTS.md:9624, results/raw/2026-08-22_podprep.txt:6; those files' blobs equal at the base and at `bab921ce52`: yes): AGREES; its locators at `cf8eb5b9dd` (RESULTS.md:9919, results/raw/2026-08-22_podprep.txt:6; those files' blobs equal at this HEAD and `cf8eb5b9dd`: yes): AGREES. In the 'Identifiers present at HEAD' table: yes. In the pre-release sensitive set: yes, with its stem: yes; pending files carrying the name: 0, the stem alone: 0 (checker: 0 in the 60 then pending). In the leak assertion's set, the name: yes, the stem: yes. The checker also reported no RunPod pod names in the record; this run adds no pod-name class and does not re-derive that.
2. **R3-2 (minor) -- HEAD moved: the concurrent session committed `cf8eb5b9dd` after the round-2 run; it adds the first tracked file under `data/m/ckpt/`, so the limit the raw said had never applied now applies, and the committed raw does not cover the current HEAD.** FIXED: regenerated at the current HEAD `cf8eb5b9dd` (refs at end unchanged), which includes the 3 commit(s) after the base: `c75d4d8aa3`, `bab921ce52`, `cf8eb5b9dd`. Paths under `data/m/ckpt/` ever tracked: 1 (`data/m/ckpt/G-CAL_qwen.json` first added by `cf8eb5b9dd`); `Binary files ... differ` lines for them in the `git log -p` stream: 1; their blobs read by (i-b): `9b6db93c` (29,608 bytes; scanned as text: yes; lines matching the fallback's pattern, invisible to the fallback: 0) (checker: a direct grep of the ckpt blob for the fallback pattern gave 0). (i-a)'s coverage limit (2) now says the limit applies and names the commit; PI pre-flip step 1 cites `cf8eb5b9dd` as the evidence that a snapshot goes stale and the re-run at the release commit is needed. This run is at `cf8eb5b9dd`, the checker's scratch run's commit; its figures against the checker's: commits 307 vs 307 (AGREES); blobs 1181 vs 1181 (AGREES); hit_lines 7782 vs 7782 (AGREES); token (7440, 8154) vs (7440, 8154) (AGREES); sk (287, 297) vs (287, 297) (AGREES); logp_lines 1798487 vs 1798487 (AGREES); logp_bytes 70058328 vs 70058328 (AGREES). Quoted-assignment values new since the base (absent at the base): 1 (FALSE-POSITIVE 1; checker at `cf8eb5b9dd`: 1 FALSE-POSITIVE; `47ee...[len 64]#422c647a` at cf8eb5b9 data/m/ckpt/G-CAL_qwen.json:1: a hex digest (256-bit, sha1/sha256 length) under a key naming it as a hash (`key_set_sha256`); a content hash, not a credential). Code's addition at this HEAD: the new value is a 64-hex sha256 under the key `key_set_sha256` (added by `cf8eb5b9dd`), which Code's first run at this HEAD, before the fix, cleared by the label rule with the reason 'a label built of words and short tokens'; a hex-digest rule now runs before the label rule and states what the value is (verdict unchanged). TRUE-SECRET-CANDIDATE 0, UNTRIAGED 0.
3. **R3-3 (minor) -- the SSH-SIGNATURE reason says the marker comes from the embedded PUBLIC key blob; it comes from the signature field's key-type string.** FIXED. The reason is now computed from each signature's byte layout (parse under (i-b) headers). This run: 7 SSH signatures, raw length 173 bytes x7; key-type string occurrences (byte, byte mod 3, field): [(14, 2, 'public-key'), (90, 0, 'signature')] x7; marker in armor body line(s) [2] x7; armor body line 1 (the one carrying the public key) distinct across the 7: 1; the marker line's distinct values: 7. So the 3-aligned key-type string is the one that opens the signature field (followed there by the signature bytes); the public key's own key-type string is not 3-aligned and does not encode to the marker. Checker: 173 bytes; offsets 14 (public key; 14 mod 3 = 2) and 90 (signature; aligned); armor line 2, 7 distinct; line 1 identical in all 7: AGREES. The reason now reads: 'base64 inside a commit's gpgsig header: the marker is the key-type string (string "ssh-ed25519") that opens the SSHSIG blob's signature field (byte 90, a multiple of 3, so it encodes to the marker), followed there by the signature bytes; the public-key field's own key-type string (byte 14) is not 3-aligned and does not encode to it; signature material, published with the commit by design; not a credential'. Round 2's disposition R2-6 is annotated with the correction. Verdict unchanged: signature material, not a credential.
4. **R3-4 (minor) -- the NOT CLEAN line puts a real redaction breach (N13's full pod id) on the same footing as the author's own email, which is public in the commit headers and outside the routing's redaction rule.** FIXED. The pre-release line is split: redaction-rule values (RunPod pod/volume ids, the volume name and its stem, SSH ports, the signing-key fingerprint, the container hostname, the Claude session link, the pass-phrase-shaped value), a new value needing triage or an uncleared precise hit -- NOT CLEAN, a blocker as drafted; and the commit identities' own metadata (the identity emails -- the author's and the Claude Cowork tool identity's -- and the laptop hostname, all public in the commit headers) -- listed for consistency with this raw's own redaction, not a routing violation, not a blocker as drafted (binding either is the PI's call). Pre-flip step 1, the summary and the JSON (`audit_files_not_clean`, `audit_files_author_identity_only`) follow the split. This run: redaction-rule group 0 audit file(s); author-identity-only 1 (`scripts/audit_note_N12_content.py`). The author's address occurs in 593 author/committer/tagger header lines (checker: 593 at `cf8eb5b9dd`, 591 at `bab921ce52`: AGREES).
5. **R3-5 (minor) -- not byte-reproducible beyond the stamps: the order of tied categories in the pre-release sentence changes from run to run (a Counter's most_common() over values whose insertion order came from a hash-ordered set).** FIXED at the root and at the display. The exact recount now walks its classes in ID_PATTERNS order (exact_recount_classes()) instead of the set's per-process hash order, so every structure built from it -- the pre-release sensitive set, the JSON's `identifiers_exact_recount` -- has a fixed order; and the sentence sorts ties by label (most_common_sorted()). Code's check of this script version before this run: two scratch runs under PYTHONHASHSEED=0 and PYTHONHASHSEED=1, started together, give an md identical apart from the stamp lines and the command echo, and a JSON identical apart from its two stamps and the excluded-path list (which echoes --out). A run made at another moment -- this one included -- can also differ in the pre-release snapshot, because other sessions write the pending files concurrently; that is the snapshot, not the order.
6. **R3-6 (minor) -- the enumeration caveat is understated: besides 5-digit ports, the volume id and the container hostname are recoverable by enumeration from their redacted forms.** FIXED. The header's caveat is now computed per sensitive value (hidden characters of the class's own alphabet, candidates, expected chance matches against the 32-bit prefix), adds the word-built values (the volume name, the pass-phrase-shaped value, the identity emails and the laptop hostname: open to a word-list search whatever their length), and states that every one of these values is in the history being published, so the form protects only this raw, not the release. This run: volume id 36^6 = 2.18e+09 candidates, ~0.51 chance matches (1 value(s)); container hostname 16^8 = 4.29e+09 candidates, ~1 chance matches (1 value(s)); pod ids 36^10 = 3.66e+15 candidates, ~8.5e+05 chance matches (2 value(s)); SSH ports 10^5 = 1.00e+05 candidates, ~2.3e-05 chance matches (5 value(s)). Checker: volume id 2.18e9 candidates / ~0.5 chance matches, container hostname 4.29e9 / ~1, pod ids ~8.5e5 chance matches: AGREES (within its rounding).
7. **Code's addition -- pending files written by another session during this round put counts on lines the SSH-port rule reads.** TRIAGED, by a rule. A run of this round refused to write: the pending N16 decoding raw had gained table lines whose only port word is 'port' in "adapter port of e2a's rule" (a code port), with counts of rounds and seed streams on them; the pre-release scan held such a count as an untriaged port-line number and redacted it, and the same number occurs in this raw as an ordinary count, so the leak assertion stopped the write. A later run met two more counts on the same kind of line. Code read the lines, and every 'port of' in the history is the software sense too; so a line whose every ssh/port/alias match is the word 'port' in 'port of' is no longer read as a port line, in the history scan and in the pending scan alike (pattern note under (ii)). History: 24 such line(s) carrying 0 4-5 digit number(s) -- no history count changes. This snapshot's pending files: 46 such line(s) carrying 13 number(s), now skipped; new port-line numbers in pending files still needing triage: 0. Residual risk: a network port written 'port of <host>' on a line with no 'ssh', 'alias' or '-p' would be skipped too. The pre-release section states the leak assertion's fail-safe.
8. **Routing -- re-run at the current HEAD and name cf8eb5b (data/m/ckpt -diff paths now tracked) as evidence for pre-flip step 1.** DONE. This run's HEAD: `cf8eb5b9dd` (the commit the routing names); the commit that first added a `data/m/ckpt/` path: `cf8eb5b9dd`; named in (i-a)'s coverage limit (2) and in PI pre-flip step 1. Every locator stays pinned to the base `bbc9ffe72f` in the 'at base' columns; the HEAD columns are this run's HEAD.

Third checker's verdict, re-checked on this run: (i) STOP pending the PI (literal :77); (v) PASS; (iv)-mechanical: jlens paths ever tracked 0, npz without an explicit line 0, weight-shaped paths 0. No finding changes a pass or STOP line; the redaction stays clean (the leak assertion now also covers the volume name and its stem).

## Values-check, round 4

The round-3 fixer's outputs (script sha256 `a775a7d8...09f6`, md `b226587f...f126`, json `4cc884b5...30dc`, all at `cf8eb5b9dd`) were checked by a fourth checker. It returned 4 findings, all minor (a column definition, a triage reason's wording, and two latent gaps in the pre-release scan; by its account the verdicts, the STOP and pass lines and the exact counts stand), and no item open from round 3. Dispositions below; each carries this run's evidence. Actions: FIXED.

1. **R4-1 (minor) -- the class table's `src` column is defined as 'distinct blobs/messages', but each class row added up its values' own source counts (the volume-name row: 147).** FIXED by computing the union: a class row's `src` is now the number of distinct blobs/messages holding any of the class's values, and the definition says so (value rows unchanged: each value's own sources). Class rows whose two counts differ in this run: runpod_pod_id 223 summed / 145 distinct; runpod_volume_name 147 summed / 84 distinct; ssh_port 130 summed / 106 distinct; local_temp_path 201 summed / 124 distinct; url_host 72 summed / 24 distinct. The volume-name row: 147 summed, 84 distinct; sources holding both of its values: 63. The checker's figures (volume name 147 / 84, held by both 63; pod ids (context) 223 / 145; url_host 72 / 24; ipv4 14 / 14): AGREES. The JSON carries both counts per class (`identifier_class_sources`). The class rows' `src` figures appear nowhere else in the raw (round 3's md: each only in its table row).
2. **R4-2 (minor) -- MANUAL_TRIAGE `84cbedd5` (`update-network-volume`): the verdict is right, but the reason says 'in prose about renaming the volume'; the prose says a network volume cannot be moved, because the tool only renames and grows it.** FIXED: the reason now reads 'the RunPod MCP tool name `update-network-volume`, cited in prose explaining that a network volume cannot be moved between datacenters (the tool renames and grows only); a public API operation's name, not a volume name' (the round-3 disposition R3-1 above, regenerated, carries the new wording). Evidence, this run: the value occurs 63 times in 63 sources (63 blob versions, 0 messages); lines carrying it 63, distinct line texts 1; of them carrying 'cannot be moved' 63, followed by a line with 'grows only' 63, with 'datacenter' in the 3 lines before 63; lines also carrying the volume name 0. First locator e256c4f0 RESULTS.md:72; at HEAD RESULTS.md:8532. The checker: 63 occurrences in 63 sources, introduced by `e256c4f`, at `cf8eb5b9dd` RESULTS.md:8530-8534: AGREES. Verdict unchanged: FALSE-POSITIVE.
3. **R4-3 (minor) -- the hex-digest rule fixed `key_set_sha256`, but the label rule still clears any hex-only value holding a run of 3 letters a-f, whatever its key (has_random_segment exempts hex-only segments), and in the pending scan the digest rule could never fire (it passed line="").** FIXED, both parts. (1) In triage_precise a hex-only value that the hex-digest rule does not clear is now UNTRIAGED (STOP until triaged), and the label rule needs a run of 3+ letters with a letter outside a-f (the fix's two alternatives, both applied; the first more strictly than written: a hex-only value under a key that names a hash but is not 40 or 64 hex is UNTRIAGED too). Code's addition: the digest rule no longer applies under a key that also names a password, secret or credential (the hash of a secret is derived from it). (2) pending_scan passes each match's own line, as the history scan does. Synthetic hex values (prefixes of the sha256 of a fixed label, chosen to hold a run of 3 letters a-f; reproducible; not printed), round 3's rules replayed against this run's: 32-hex under `secret`: round 3 FALSE-POSITIVE (label rule), now UNTRIAGED; 40-hex under `api_key`: round 3 FALSE-POSITIVE (label rule), now UNTRIAGED; 64-hex, no line (the pending scan's old call): round 3 FALSE-POSITIVE (label rule), now UNTRIAGED; 64-hex under `key_set_sha256`: round 3 FALSE-POSITIVE (hex digest), now FALSE-POSITIVE (hex digest); 64-hex under `password_sha256`: round 3 FALSE-POSITIVE (hex digest), now UNTRIAGED. This run over every precise table (blobs/messages, headers, binary content): hex-only quoted values 1 (`47ee...[len 64]#422c647a` FALSE-POSITIVE, 2 occ in 2 sources); values the label rule clears 33, none hex-only; quoted_secretish_assignment verdicts FALSE-POSITIVE 41 (round 3's raw: FALSE-POSITIVE 41), so no verdict changes. Pending files: hex-only quoted values 0. The checker: one hex-only quoted value in history (`#422c647a`, 2 occ in 2 sources), 0 in the pending files: AGREES. A pre-flip re-run that meets a hex-only value now stops on it instead of clearing it.
4. **R4-4 (minor) -- the pre-release CLEAN line and pre-flip step 1 rest on a scan that has no class for third-party personal data (PENDING_ID_CLASSES has no email_address), while the identity line says the routing's redaction rule covers it.** FIXED, both remedies. `email_address` is now one of the pending scan's new-value classes: an address other than the service address (exempt) and the commit identities' own (in the known set) is a new value, UNTRIAGED until Code reads it, and in an audit file it holds the redaction-rule line NOT CLEAN. The pre-release section, the CLEAN line and pre-flip step 1 now say that this is the scan's only class of third-party personal data (a name, a postal address or a phone number is not scanned for). This run's snapshot: files with an email address 2: `scripts/audit_note_N12_content.py` commit identity 1, service address 1; `scripts/audit_note_N12_history.py` service address 9; new (third-party) addresses 0. This part's own md and JSON are excluded from the pending scan (the leak assertion covers them; the service address is printed verbatim by design). The checker: the service address and the author's identity address `#bb973c14` only, no third-party address: AGREES.

Fourth checker's findings, re-checked on this run: (i) STOP pending the PI (literal :77); (v) PASS; TRUE-SECRET-CANDIDATE 0, UNTRIAGED 0. No finding changes a pass or STOP line, and no history verdict changes; the pre-release scan is stricter (hex-only values, email addresses).
