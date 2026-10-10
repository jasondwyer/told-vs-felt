# AUDIT-note-release v1.2 -- N18: release manifest (hashes for the note)

- Code stamp: 2026-10-10 14:29:53 UTC (date -u); HEAD at run `ea47e89aba16e6fe967d341be45289a505027aba` (branch main)
- Block `AUDIT-note-release-v1_2.md` sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841` (matches the routed 8cd8a9ac...3841; equal to its committed version at `bbc9ffe`); N18 is block :132-133
- Script `scripts/audit_note_N18.py` sha256 `47bcefb66f909b7af59be7416c3af42860bbd1ac810186d6e6ad565918c2f934`; interpreter /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python (Python 3.12.9)
- The JSON beside this file is the manifest; this file summarises it.

## Tag

- Name: `note-2026-10-v1`. Source: the PI's routing of 2026-10-09, item (7), as routed to Code: tag name note-2026-10-v1, placed on the final audit commit after N1 and N18; the block leaves the name to the PI and suggests it at AUDIT-note-release-v1_2.md@bbc9ffe:14.
- Tag commit: not in this manifest. The tag is placed on the commit that adds this manifest. A commit's hash is computed over a tree that contains this file, so the hash cannot be written inside it (self-reference). It is to be recorded after tagging: in the note's footer (block :133; the footer is the design seat's) and in a post-tag raw (the procedure routed to Code for this part; neither the block nor the PI's routing names that raw).
- Tag state at this run: absent.

## The note and its figures

| file | sha256 | asserted against | tracked at HEAD |
|---|---|---|---|
| `RESEARCH-NOTE-v0_4-draft.md` | `c4a05c781113cb2eceea0404d93ae723cc8dd32c2d8793d53cdb6067ee4ba9bc` | c4a05c781113cb2eceea0404d93ae723cc8dd32c2d8793d53cdb6067ee4ba9bc (the PI's routing of 2026-10-09 (rulings), which gives the note's full sha256): PASS | no (untracked) |
| `2026-10-09_F1a_headline-strip.svg` | `4e4cbbb1f8a31485d767c5f620614c90e1e88c6fc7b4985a805485a87eea0e2e` | 4e4cbbb1f8a31485d767c5f620614c90e1e88c6fc7b4985a805485a87eea0e2e (no sha256 routed: the full sha256 of Code's copy from the Digest seat's folder (2026-10-09), as N1 round 8 records it): PASS | no (untracked) |
| `2026-10-09_F1b_five-link-panels.svg` | `25e0dd99a685a0c13e7d47c85a4e7200d05caf44f600b45518c5bbcc6614915c` | 25e0dd99a685a0c13e7d47c85a4e7200d05caf44f600b45518c5bbcc6614915c (no sha256 routed: the full sha256 of Code's copy from the Digest seat's folder (2026-10-09), as N1 round 8 records it): PASS | no (untracked) |
| `2026-10-09_F2_macar-lineage-roc_post.svg` | `e2a38e74711e6da6ba7480f8425a1fb18b3ed074a7bf1ed38b5ac66c6fc17824` | e2a38e74711e6da6ba7480f8425a1fb18b3ed074a7bf1ed38b5ac66c6fc17824 (no sha256 routed: the full sha256 of Code's copy from the Digest seat's folder (2026-10-09), as N1 round 8 records it): PASS | no (untracked) |

- Untracked at this run. N1 final's first condition on the tag (§9g) is that the tag commit contains the note and all 3 SVGs.
- If the note or any SVG changes before the tag commit, N1 and then N18 must be re-run (see "Before the tag commit" below).
- The block puts the note's sha256 in the note's footer (:133). A footer inside the hashed file changes that file's sha256, so the footer cannot state the hash of the file that contains it; how the footer and the repository copy relate is the design seat's to settle.
- N1 final (`results/raw/2026-10-09_note-N1-v0_4-claims-ledger.json`, run at HEAD `ea47e89aba16`) covers exactly these three sha256s and is not provisional; its note-rows file `results/raw/2026-10-09_note-N1-v0_4-note-rows.json` is unchanged since (sha256 `e3d4f083aad815f53efdfefb045f2561ca4f9528305f21ee384deb73942b2c21`).
- **Figures commit (N1 final):** `e60b633142f0ff5ec574da022a7117d18711e32b` (2026-10-09T21:04:01-04:00), set by S1#173, S5#72, S5#77. Basis: N1 final, note_rows_final.tag.including_audit_raws (the note carries computed-new figures and figures whose only carrier is an audit raw: N19's, N2 round 6's); stated plainly at results/raw/2026-10-09_note-N1-v0_4-claims-ledger.md:2028 (the file as read at this run). Ancestor of HEAD at this run: yes. N1's record-sources-only candidate, as N1 states it: `05c4636` (2026-10-06T00:42:09-04:00).
- The N1 script's sha256 now equals the one the ledger records (`52bfd8d4dff33670`).

## Preprint

- `PREPRINT-v1_0-draft.md`: **pending patch v6** (sha256 null). The file on disk equals the block's reference d6431e97…222b8 (post-patch-v4 copy), AUDIT-note-release-v1_2.md@bbc9ffe:21.
- Routing: the PI's routing of 2026-10-09, item (5), as routed to Code: PREPRINT-v1_0-draft.md is committed at the tag after patch v6 is applied. If patch v6 arrives, or the file otherwise changes, after this run and before the tag commit, N18 must be re-run: this section describes the file as found at this run, and the tag commit is to hold the post-v6 file.

## N13 provenance table: version content sha256 per row

Read from `results/raw/2026-10-08_note-N13-provenance.json@09c3a8c` (sha256 `fad481d86791dea71693429dc16aa562d304821c3768bacf90527405af8ee205`; working tree equal: yes). 25 rows: 15 file rows (re-hash: 15 match, 0 mismatch, 0 not re-hashed) and 10 log-entry rows (L-slice2, L-c1, L-c1r3, L-e0B2, L-e0B2c, L-e2a, L-e2a-g3p, L-dgate, L-f1, L-r26), which are not re-hashed. content_sha256, its status and the row status are N13's, verbatim in the JSON. The last column is this run's re-hash of `git show <record commit>:<document>`.

| row | document | record commit | content sha256 | N13 sha status (abbrev.) | re-hash |
|---|---|---|---|---|---|
| L-slice2 | `archive/RESULTS-cycle1-2.md (log entry)` | `f9eab26` | `f5026fee2b4bf9d0faf50e0db8dd7fa92b8f17abf7030a424d16de82f001a13f` | computed-new | log entry: not re-hashed |
| L-c1 | `archive/RESULTS-cycle1-2.md (log entry)` | `6d88d9b` | `8a422e641c67657466102dec0ca11a100b53fc1ba927b119e606aefb21bb8a63` | computed-new | log entry: not re-hashed |
| L-c1r3 | `archive/RESULTS-cycle1-2.md (log entry)` | `b78bfb3` | `d3a16d0febaa2d6d35c4fe8888852fd0f6142003cf40ad56e196c09fa8908d31` | computed-new | log entry: not re-hashed |
| P-d | `PROPOSAL-d-distilled-trace.md` | `c54c4e0` | `1ab3cddc2cf66eb7e599735038ed31b9b18a3663cdaac181910b32fd0e128fee` | computed-new | match |
| P-e | `PROPOSAL-e-reward-axis-hijack.md` | `c54c4e0` | `4ca23f41bf902e75a210109231b673c0ca705faabc57b22975f8d5297c8113f1` | computed-new | match |
| L-e0B2 | `archive/RESULTS-cycles3-4.md (log entry)` | `05bda27` | `d87df706d34d207d6f3afec0093653b9a707ba706b142cca8a21c97f7a0e279e` | computed-new | log entry: not re-hashed |
| L-e0B2c | `archive/RESULTS-cycles3-4.md (log entry)` | `f222541` | `5cf1e7b65df4761f2e09c75893d3434000f0113ea17fdebcd008d4d1141f9ee4` | computed-new | log entry: not re-hashed |
| L-e2a | `archive/RESULTS-cycles3-4.md (log entry)` | `1970b50` | `0cc66e7996e5c73c705ccf27171d27b0a5b904181afa1e3da0426566d2ee7bbd` | computed-new | log entry: not re-hashed |
| L-e2a-g3p | `archive/RESULTS-cycles3-4.md (log entry)` | `da40635` | `d037ded2a04ceb641885bae727644c9890a794af418b0e55874c438779e2ce2e` | computed-new | log entry: not re-hashed |
| L-dgate | `archive/RESULTS-cycles3-4.md (log entry)` | `88e9ef0` | `6014d525fde48e475093da1ed5496f09db72631b5f5124acbc4138aa2ab41191` | computed-new | log entry: not re-hashed |
| P-f | `PROPOSAL-f-natural-reinforcer-screen.md` | `ea011bd` | `d7a131eabf8d30a8b7d6ebde75c7b53b7ded88468d6d366010d1403282afb8bf` | computed-new | match |
| L-f1 | `archive/RESULTS-cycles3-4.md (log entry)` | `7a6036a` | `130b30bfeffdf6463c539bea8a8ff032f4c80420429686bc48b5b5fd6add2c95` | computed-new | log entry: not re-hashed |
| L-r26 | `RESULTS.md (log entry)` | `18dc75e` | `06e4d9ba3cfdc38842b383d6496a1d0b5d9817b2409ac683d6d5d11259acc845` | computed-new | log entry: not re-hashed |
| P-g | `PROPOSAL-g-ontogeny-of-evaluation.md` | `72b09a9` | `312437d10bf198c37473ab80f076ad19dd5be4e5a6e3edd95d0e85ff4d284315` | computed-new | match |
| Q1 | `PROPOSAL-g-ontogeny-of-evaluation.md` | `72b09a9` | `312437d10bf198c37473ab80f076ad19dd5be4e5a6e3edd95d0e85ff4d284315` | computed-new | match |
| A-g1 | `ADDENDUM-g1-archival-reading-screen.md` | `34eb7ee` | `e11a011b02312f4245fccc6bfa208c055cfd52dc34ef8b9ac8e6595949cc5147` | computed-new | match |
| P-h | `PROPOSAL-h-state-present-choice.md` | `34eb7ee` | `9e5d3d841e06917bc20596503f5be66e8b216bde4d2692ac0ded2b7ebf773b81` | computed-new | match |
| W-h | `PROPOSAL-h-state-present-choice.md` | `34eb7ee` | `9e5d3d841e06917bc20596503f5be66e8b216bde4d2692ac0ded2b7ebf773b81` | computed-new | match |
| LOCK-h | `LOCK-h.md` | `8a97513` | `521bd1ae193d4294847633533e4249790d3fcd0c5b38324cd51bf2ff5d0d9748` | computed-new | match |
| LOCK-g | `LOCK-g.md` | `0551224` | `eb0420a168ee1535a65e50ade9bae2b479e98bdb1a418531258e4607c809b5d8` | computed-new | match |
| W-g | `LOCK-g.md` | `0551224` | `eb0420a168ee1535a65e50ade9bae2b479e98bdb1a418531258e4607c809b5d8` | computed-new | match |
| A-g3 | `ADDENDUM-g3-b2r-v1.2.md` | `f14d249` | `33b474753b2d6d9037af7a7eedfb00db6df8ee3322b230b5b35c26a9f7f5fa6c` | computed-new | match |
| P-j | `PROPOSAL-j-dose-escalation.md` | `f7a4a1e` | `4f2938984f1c1ff4757a51bf9d7bb43a93747d1763022a5f56b178f84bc0a8a0` | computed-new | match |
| P-k | `PROPOSAL-k-echo-channel.md` | `e9b5022` | `8ee011ff0fad0082472f984703f4aef86fdf9246ca859fd394d5716934eae441` | computed-new | match |
| P-m | `PROPOSAL-m-gating-campaign-v1_11.md` | `05c4636` | `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b` | reproduced | match |

## Files at this run

- Wait check: `README-NOTE.md` last modified 2026-10-10T14:29:44Z (local date 2026-10-10; today 2026-10-10): modified today; hashed as it stood at this run.
- Wait check: `results/raw/2026-10-08_note-N12-scrub.md` last modified 2026-10-10T14:19:32Z (local date 2026-10-10; today 2026-10-10): modified today; hashed as it stood at this run.
- 90 files (README-NOTE.md, LICENSE, LICENSE-CC-BY-4.0, LICENSING.md, data/e2a/analysis.correction-of-record.json, the N1 final ledger md/json, every results/raw/*_note-* file and every scripts/audit_note_*.py on disk at this run, sorted by path; this script's own two outputs and any results/raw/*_note-release-manifest.json/.md are excluded (a file cannot carry its own hash). tracked_at_head and equal_to_head compare the working file's git blob id with HEAD's.). Excluded: `results/raw/2026-10-09_note-release-manifest.json`, `results/raw/2026-10-09_note-release-manifest.md`.
- Digest of the list: `cfe226464100f2d1dac23e3d33b5858a8626da17209ef2a645c9c2c4c856f48e` (sha256 of the lines '<sha256>  <path>\n' over files.list in its order (sorted by path); equal to piping `shasum -a 256 <the paths in that order>` into `shasum -a 256`).
- Tracked at HEAD: 86 of 90; equal to HEAD: 81. Files untracked or changed since HEAD are hashed as they stand; any change to a listed file before the tag commit requires a re-run.

The named files and N1's final outputs, and every listed file that is untracked or differs from HEAD (the full list with sha256s is in the JSON, `files.list`):

| file | sha256 | at HEAD |
|---|---|---|
| `LICENSE` | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` | equal |
| `LICENSE-CC-BY-4.0` | `cce5d01fa4a83b794271bd2c28cffdf99afd43c803e6ddefddae39b591ea7448` | equal |
| `LICENSING.md` | `6d4d012a04f543c148f909019d79c61ba854100c32a4d1e0893bc955f4a4e441` | equal |
| `README-NOTE.md` | `83b54784086d327131198d6ef0d12b5b2f1a5da69aaca2083d58b079d468043b` | modified |
| `data/e2a/analysis.correction-of-record.json` | `1c2727f9759d3b477aa86bff0fc580345f1a034543e7cf706edfff874e192bb4` | equal |
| `results/raw/2026-10-08_note-N12-scrub.md` | `e46425c9d119e3824ccd73bdae8947871fd5d8972116a1a6c04e8f497f84d968` | modified |
| `results/raw/2026-10-09_note-N1-note-rows.json` | `5f8f76cd5b4e18bff19c9419044734eff3aab22bce86d005438fd56e2e01f6ce` | equal |
| `results/raw/2026-10-09_note-N1-v0_4-claims-ledger.json` | `5f541463bad2311538eb07f8fe5047b31aa430afdac31f8dda5026a98d37ebff` | untracked |
| `results/raw/2026-10-09_note-N1-v0_4-claims-ledger.md` | `e5cb92c00dd2fc502822f593ddf0d49f2f33d348aef7893c0240237878eef1fb` | untracked |
| `results/raw/2026-10-09_note-N1-v0_4-note-rows.json` | `e3d4f083aad815f53efdfefb045f2561ca4f9528305f21ee384deb73942b2c21` | untracked |
| `results/raw/2026-10-10_note-N1-v0_4_valuescheck.md` | `9f8a49fa9df6809a246be4fb3a1ca103b8ea1b51d7615f2c3677234f19a117d6` | untracked |
| `scripts/audit_note_N1.py` | `52bfd8d4dff336702ba85c743f80fda26113565e584d37d5bf9a6d3e448af9f3` | modified |
| `scripts/audit_note_N12_scrub.py` | `bdef4095c4d8e01c5d590497b92c18be39062ce39bf040ee37f6cda408f81744` | modified |
| `scripts/audit_note_N18.py` | `47bcefb66f909b7af59be7416c3af42860bbd1ac810186d6e6ad565918c2f934` | modified |

## Before the tag commit

This manifest covers only the files as hashed at this run; the tag commit's tree must hold each of them at the sha256 recorded here. If any trigger below fires after this run and before the tag commit, the named items must be re-run, N18 last.

1. If the note or any SVG changes (including the [REPO LINK] replacement or a footer added to the file): re-run N1, then N18.
2. If patch v6 arrives, or PREPRINT-v1_0-draft.md otherwise changes (the PI's routing of 2026-10-09, item (5), as routed to Code, commits the post-v6 file at the tag; this manifest records the file as found at this run): re-run N18 (with --preprint-pi-confirmed once the PI confirms the post-v6 file).
3. If any file in files.list changes, is added under results/raw/*_note-* or scripts/audit_note_*.py, or is removed (for example README-NOTE.md when a placeholder is filled, or the N1 final ledger when N1 is re-run): re-run N18.

