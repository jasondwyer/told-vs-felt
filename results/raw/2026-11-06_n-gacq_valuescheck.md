# G-ACQ (n): blind values-check of the raw and the entry, with Code's dispositions (2026-11-06)

*Before the commit, a blind checker (a fresh agent, with no part in the drafting) checked the drafts of `results/raw/2026-11-06_n-gacq.md` and the RESULTS entry against the primary sources: the box outputs, the hub's listing, the repository at `0415438` and `3b22158`, and the adapter and scripts. Its report follows verbatim. Line numbers in it refer to those drafts, and to RESULTS.md at `0415438`. Code's dispositions follow it.*

---

# Blind values-check: G-ACQ (n) raw (raw_full.md) and RESULTS entry (entry_draft.md)

Format: N. claim | location | VERDICT | evidence. "box/" = scratchpad n_gacq/box/. Line numbers in RESULTS.md are at HEAD 0415438 unless a commit is named.

1. PI date 2026-11-06; box stamps UTC 2026-11-07 | RAW l.3 | PASS | all ten box/*.launch, *.exit stamps read 2026-11-07T…Z.
2. "No host address or port is recorded"; no local paths, IPs or ports | RAW l.5; ENTRY | PASS | regex scans of both drafts: no IPv4, no host:port (4–5 digits), no URL scheme, no /Users, /private, /tmp, scratchpad or user name. Every path is /workspace/…, repo-relative, /bin/bash, /usr/bin/env or the hub API path.
3. §9 blocks are the box files, CRs shown as line breaks | RAW l.5, §9 intro | PASS | all 11 file blocks compared programmatically with box/ and the two .py copies: identical after CR→LF (the fence drops the final LF). Every CR (download 14, hook-site 10, attempt-1 15) precedes a progress-bar segment. The stamps block equals the ten .launch/.exit files.
4. "The scripts … and their outputs follow in §9, byte for byte"; ENTRY "Its §9 carries the box scripts and outputs byte for byte" | RAW l.5; ENTRY Authority/Raw | IMPRECISE | the box outputs gacq_verify.json and gacq_hooksite.json are not in §9; only api_rev.json's omission is disclosed. The ENTRY also drops the RAW's caveat about CRs.
5. The routing is quoted in full in the G-ANL-F3 STOP close at 54bbfe5 | RAW §0; ENTRY Authority | PASS | git show 54bbfe5:RESULTS.md:233–241 (block), :243.
6. G-ACQ line "Pod: stays up through the OLMo track. G-ACQ (PROPOSAL-n) on this box: [now, in parallel / after the campaigns]."; the ENTRY's substring; "the bracket carried both options" | RAW §0; ENTRY Authority | PASS | verbatim at 54bbfe5:RESULTS.md:239.
7. Code's chat question "When should G-ACQ run on this box?" | RAW §0; ENTRY Authority | UNVERIFIABLE | operator-only.
8. The PI's answer "Now, in parallel" | RAW §0; ENTRY head, Authority | PASS | 54bbfe5:RESULTS.md:243; 0415438 message.
9. Answers sha256 4edfbb8e…ca42e, committed at 54bbfe5 | RAW §0; ENTRY Authority | PASS | shasum 4edfbb8e3d08…2f2207777ca42e; git log on the file returns 54bbfe5 only.
10. C3 quote (RAW: two sentences; ENTRY: excerpt) | RAW §0; ENTRY Authority | PASS | verbatim at answers:43 (an excerpt: C3's last two sentences).
11. PROPOSAL-n v0.2 sha256 30a3d0f5…b104f4 | RAW §0 | PASS | shasum 30a3d0f55a6681e0…f2c6e59684d6a17584b104f4.
12. §3 G-ACQ quoted verbatim | RAW §0 | PASS | exact substring of PROPOSAL-n-bk-reconciliation-v0_2.md:109.
13. Pod qny1x4v8padeke (jspace-olmo-m), 1 × A100-SXM4-80GB, US-CA-2, image runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404, volume o73qvy742n at /workspace | RAW §1 | PASS | 190ba90 message.
14. BACKEND at 190ba90: (i) 29/29, (ii) exact, identifier 641ee466f4553b6a | RAW §1; ENTRY Respawn | PASS | 190ba90 message: "29/29 files", "A, B and C all exact at 0.0", "641ee466f4553b6a".
15. env.sh carries C4's RUNPOD_POD_ID line (6ce8b9a's entry); every script sources it | RAW §1 | PASS | RESULTS.md:42 quotes the line. All four box .sh files run `. /workspace/env.sh`, and the .py scripts run under them. hooksite.json: runpod_pod_id "qny1x4v8padeke".
16. transformers 5.15.0, torch 2.8.0+cu128, from the hook-site record | RAW §1 | PASS | gacq_hooksite.json.
17. The download used huggingface_hub 1.28.0 with hf_xet | RAW §1 | UNVERIFIABLE | operator-only; no box file records it.
18. Repo and revision b96024342a77a69aa0dda815c3454a671f477463 are G-DATA's (1d51673) | RAW §2; ENTRY head | PASS | api_rev.json "sha"; 1d51673 message; n-gdata.md:64.
19. Listing read before the pull from …/revision/<sha>?blobs=true, unauthenticated | RAW §2 | PASS | api_rev.json mtime 20:47:56 −0500 = 01:47:56Z, before the 01:50:07Z launch. The siblings carry size/blobId/lfs, the blobs=true shape. "Unauthenticated" itself cannot be checked.
20. Last modified 2025-03-14T22:45:15Z | RAW §2 | PASS | "lastModified": "2025-03-14T22:45:15.000Z".
21. License apache-2.0, not gated | RAW §2 | PASS | cardData.license "apache-2.0"; tag license:apache-2.0; "gated": false.
22. Safetensors metadata `{"BF16": 32234279936}` | RAW §2 | IMPRECISE | the listing's object is {"parameters": {"BF16": 32234279936}, "total": 32234279936}. The RAW prints its `parameters` member as if it were the whole object.
23. 28 files; 22 match the allow patterns; the other 6 are .gitattributes, README.md and four PNGs | RAW §2; ENTRY Download | PASS | 28 siblings. fnmatch on the 4 patterns gives 22 (14 .safetensors, 7 .json, 1 .txt, 0 .model), the same names as verify.json. Excluded: .gitattributes, README.md, olmo-32b-instruct-{eval-curve, full-eval-curve, learning-curve-time, learning-curve}.png.
24. The allow patterns are box_acquire_olmo.py's | RAW §2, §4; ENTRY Download | PASS | box_acquire_olmo.py:100–102 matches gacq_download.sh's list.
25. df readings 466/242/224; 164 available; 466/302/164 (GiB) | RAW §3; ENTRY Headroom | UNVERIFIABLE | operator-only; matches the operator's values. The arithmetic is consistent: 242+224 = 302+164 = 466, and the 60 GiB drop matches 64,478,373,025 B = 60.05 GiB.
26. Each OLMo-3 entry is 64.5 GB; the new entry is 64.5 GB (64,478,373,025 B) | RAW §3 | PASS | manifest@0415438: size_gb 64.5 in all five; olmo2_instruct bytes sum to 64,478,373,025.
27. gacq_download.sh: snapshot_download, the allow patterns, local_dir /workspace/staging-n/olmo2_instruct, nice -n 10, unauthenticated | RAW §4 | PASS | box/gacq_download.sh; the log's "unauthenticated requests" warning.
28. Staging is outside /workspace/models, so nothing there changed | RAW §4 | PASS | the paths; respawn (i) at 03:27:32Z re-hashes the 29 OLMo-3 files ok.
29. The pod session confirmed its weights checks read only /workspace/models/{sft,dpo,instruct} | RAW §4 | UNVERIFIABLE | chat-only. The substance is consistent with scripts/m_sessions.py:707–737 (olmo_weights_problems reads only the manifest entry's path) and :799–808.
30. Download launched 01:50:07Z; exit 0 at 02:02:59Z; 771 s; 22 files | RAW §4; ENTRY Download | PASS | .launch/.exit; log: "Fetching 22 files", "DONE … 771s" (772 s wall clock).
31. The download and verification ran "while G-CAL-OLMo ran" | RAW l.5 ("partly in parallel"), §4, GA-3; ENTRY Download, GA-3 | IMPRECISE | G-CAL-OLMo's runs were 02:20:02Z→02:35:53Z (RESULTS.md:54; 6ce8b9a). The download (→02:02:59Z) and the verification (→02:06:46Z) both ended before those runs began. They overlapped the smoke's box self-test, 01:41:54Z→02:07:28Z (RESULTS.md:187), whose entry calls itself "Not G-CAL-OLMo" (RESULTS.md:135).
32. Verification ran CPU only; launched 02:04:08Z, exit 0 at 02:06:46Z | RAW §5; ENTRY Verification | PASS | .launch/.exit; gacq_verify.py imports no torch.
33. "It verified four things" | RAW §5 | IMPRECISE | item (4) is computed, not checked. The docstring says "Exits 0 only if (1)-(3) all pass", and nothing compares the aggregate with anything.
34. (1) 22 present, 0 missing, 0 extra; .cache set aside | RAW §5; ENTRY | PASS | verify.log line 1.
35. (2) sizes equal the hub's; the 14 shards' sha256 equal the LFS sha256; the 8 other files' git blobs equal the blobIds; hashed in 158 s | RAW §5; ENTRY | PASS | verify.log; verify.json problems []. The 14 shards are the only LFS files among the 22 (api_rev.json).
36. (3) 14 shards, 707 tensors, BF16 only, 32,234,279,936 = the hub's total; index 707, same set, 0 misplaced | RAW §5; ENTRY | PASS | verify.log line "(3) …". A set mismatch would be recorded as a problem (gacq_verify.py:327–328), and problems is [].
37. Aggregate 36f05404dc39…0fdb over 22 files, 64.5 GB | RAW §5, §6; ENTRY | PASS | recomputed from 0415438's per-file sha256s with box_hash_checkpoints.py:45–47's formula; identical.
38. Defined as "sha256 over the per-file digests in sorted name order" | RAW §5 | IMPRECISE | the hashed string is "".join(f"{name}:{sha256}") in sorted name order (box_hash_checkpoints.py:45–47; gacq_verify.py docstring), so the names are hashed too. The wording echoes the script's comment at :44.
39. §5 table: 22 rows of bytes and sha256[:16]; 14 "LFS sha256 equal"; 8 blob-id prefixes | RAW §5 | PASS | every row matches verify.log/verify.json bytes and sha256[:16], and api_rev's size, lfs.sha256 (full) and blobId[:12]. The LFS/blob split also matches.
40. The full sha256s are the entry's files in the manifest at 0415438 | RAW §5 | PASS | manifest@0415438 olmo2_instruct equals verify.json "entry" (whole dict).
41. G-DATA's three tokenizer files are these bytes (78afb564…, 73fd5254…, fff5b944…) | RAW §5; ENTRY | PASS | n-gdata.md:68–72: the full sha256s and byte counts equal verify.json's.
42. The move came after G-CAL-OLMo ended (runs closed 02:35:53Z; 6ce8b9a) and after the hand-over | RAW §6, GA-3; ENTRY Into place | PASS | 6ce8b9a message: "02:20:02Z-02:35:53Z". 6ce8b9a was committed at 03:14:07Z and 0415438 at 03:16:21Z. The move window is the operator's.
43. .cache moved to /workspace/staging-n/olmo2_instruct.hf-local-dir-meta | RAW §6 | UNVERIFIABLE | operator-only; matches.
44. /workspace/models/olmo2_instruct holds 22 files, 64,478,373,025 B, no hidden file | RAW §6; ENTRY | PASS | hooksite.json path. Respawn lists 22 olmo2_instruct files and no EXTRA; os.listdir includes dotfiles (box_respawn_check.py:54, 71–72). The bytes equal the manifest sum and match the operator.
45. base, sft, dpo and instruct untouched | RAW §6; ENTRY ("no OLMo-3 folder touched") | PASS | respawn (i) at 0415438: 29 ok lines, no EXTRA.
46. Nothing deleted | RAW §6; ENTRY | UNVERIFIABLE | no file evidence.
47. Fifth entry at 0415438, committed ahead of this entry so respawn (i) re-hashes against a committed manifest | RAW §6; ENTRY | PASS | 0415438 message and diff; respawn header "repo HEAD 0415438".
48. Entry fields: repo; revision b96024342a77; dtype bfloat16; n_params 32234279936; size_gb 64.5; path; acquired_utc 2026-11-07T02:02:59Z; files (22); aggregate; n_files 22 | RAW §6 | PASS | manifest@0415438. acquired_utc is the gacq_download.exit stamp.
49. The key order is the other entries' | RAW §6 | PASS | the same 10-key order as base; the files' {sha256, bytes} order matches too.
50. Still json.dumps(indent=1) with no trailing newline; the four OLMo-3 entries byte-identical | RAW §6; ENTRY | PASS | both blobs equal json.dumps(obj, indent=1), and neither ends in "\n". base, sft, dpo and instruct are equal. 3b22158's text minus its final "\n}" is a prefix of 0415438's.
51. Manifest sha256 293ad07fc2f9…2ae8 → d39e50663ae9…ac3e | RAW §6; ENTRY | PASS | shasum of git show 3b22158: and 0415438:data/olmo/manifest.json.
52. Box repo 1bf94a6 → 0415438 by an incremental bundle (prerequisite 1bf94a6, 186,335 B) and a fast-forward | RAW §6; ENTRY | PASS | scratch jspace-gacq.bundle: 186,335 B; header "-1bf94a6c8198…" and "04154382e1b6… refs/heads/main". 1bf94a6 is an ancestor of 0415438 (8 commits); respawn header HEAD 0415438.
53. The six untracked G-CAL files are byte-identical to 0415438's blobs; prefixes 799b3c3f…, ed89aaf5…, 62ed6d03…, 1f16f732…, 239f6bd6…, 724897d7… | RAW §6; ENTRY | PASS | sha256 of git show 0415438:data/m/gates/G-CAL_completability_olmo-{sft,dpo,instruct}.json and data/m/ckpt/G-CAL_olmo-{…}.json: 799b3c3f96237f4f, ed89aaf5cd7ad52b, 62ed6d03127c1b5e, 1f16f7326eab748d, 239f6bd668970567, 724897d776324f0f. These equal the operator's prefixes and results/raw/2026-11-06_backend_box-captures.txt:336–341.
54. Moved aside to /workspace/repo/box-untracked-gcal-2026-11-06/, keeping their paths; the tree clean after | RAW §6; ENTRY | UNVERIFIABLE | in no file and not among the operator's facts.
55. Attempt 1: 03:14:15Z → exit 1 at 03:17:10Z; refused at construction after the weights loaded, before any forward; the error text | RAW §7; ENTRY | PASS | attempt-1 .launch/.exit. The log shows 707/707 loaded, then the traceback at olmo_hf.py:88 with the quoted message. olmo_hf.py:81–90 loads before it checks the cap.
56. The adapter's DEFAULT_CHOICE_WINDOW, 8192, "is OLMo-3's" | RAW §7 | IMPRECISE | olmo_hf.py:41–45 makes it a declared adapter constant ("Declared, not inherited … 666 tokens … 8192 is generous headroom"), not an OLMo-3 property. The repo records no OLMo-3 position limit.
57. OLMo-2-32B has 4,096 positions | RAW §7, GA-4; ENTRY | PASS | hooksite.json max_position_embeddings 4096; the attempt-1 error.
58. Attempt 2: 03:18:19Z → exit 0 at 03:20:35Z; passes config.json's cap; reads no window; PASS | RAW §7; ENTRY | PASS | .launch/.exit; gacq_hooksite.py:44, 46; json choice_window_passed 4096, verdict "PASS".
59. Olmo2ForCausalLM; 64 decoder layers; hidden size 5,120; 65 hidden states | RAW §7; ENTRY | PASS | hooksite.json model_class, n_layers, hidden_size, len_hidden_states.
60. One forward; 17 ids; sha16 13f7a58477d3f7e5 | RAW §7; ENTRY | PASS | the json's ids (17); sha256(json.dumps(ids))[:16] recomputed as 13f7a58477d3f7e5.
61. The sentence is drawn from no pool, prompt or corpus | RAW §7 | PASS | a fixed-string grep of the repo (minus .git and jlens-qwen36) finds no occurrence.
62. The adapter's own hooks, no injection, on every layer; output_hidden_states on the same call | RAW §7; ENTRY | PASS | gacq_hooksite.py makes _make_hooks([], range(L), store, [0]) and one ad._model(..., output_hidden_states=True) call. olmo_hf.py:122–167 hooks the output of model.model.layers[l].
63. Indices 0–62 bitwise equal (0.0); 63 differs (150.89) | RAW §7; ENTRY | PASS | json rows 0–62: equal true, max_abs 0.0. Row 63: false, 150.89111328125. fails [].
64. Index l is the residual after decoder layer l, 0-based; the site is index 31 or 32; the final-norm reading | RAW §7; ENTRY | PASS | follows from items 62–63 (descriptive).
65. Load 133.4 s; RUNPOD_POD_ID qny1x4v8padeke | RAW §7 | PASS | json load_s 133.4 and runpod_pod_id.
66. Quotes "asserted within 2% of 25.49 [C], else STOP" and BK's "layer 32 of 64" | RAW §7 | PASS | PROPOSAL-n:111; :81 ("layer 32 of 64 (BK Table 1)").
67. Mean residual norm over the 17 positions: 37.0677 at index 31, 37.0880 at index 32 | RAW §7; ENTRY | PASS | json 37.06771469116211 and 37.08802795410156; the script takes norm(dim=-1).mean() over positions.
68. Respawn header: pod, HEAD 0415438, manifest sha256 d39e50663ae9ab16… | RAW §8 | PASS | gacq_respawn_integrity.txt:1.
69. Respawn 03:19:05Z → exit 0 at 03:27:32Z; INTEGRITY PASS, 51 files across 5 checkpoints (29 + 22), both directions | RAW §8; ENTRY | PASS | .launch/.exit. 51 ok lines (base 7, sft 7, dpo 7, instruct 8, olmo2_instruct 22), each sha16 equal to manifest@0415438's. box_respawn_check.py checks both MISSING and EXTRA.
70. (ii): "same pod, same backend identifier" | RAW §8 | IMPRECISE | no G-ACQ script computes a backend identifier. 641ee466f4553b6a is 190ba90's (and G-CAL-OLMo's runs'). G-ACQ's own record shows only the torch and transformers versions, which match 190ba90's.
71. Shared with A-m1's units, quoting "shared with A-m1's units if the same box" | RAW §8; ENTRY | PASS | PROPOSAL-n:109.
72. The BACKEND extension (24 reads) was not run | RAW §8, GA-5; ENTRY | PASS | no such script or output among the box files.
73. GA-1: the checkpoint ships BF16, so "cast" is the identity | RAW GA-1; ENTRY | PASS | api_rev safetensors is BF16 only; verify.log dtypes {'BF16': 32234279936}; "cast" is at PROPOSAL-n:109.
74. GA-1: the four OLMo-3 entries were re-serialized via save_pretrained; quote "Upstream file-identity is gone" | RAW GA-1; ENTRY | PASS | box_acquire_olmo.py:105, 114–115; box_hash_checkpoints.py:4.
75. GA-1: "kept the acquisition off the CPU" | RAW GA-1 | IMPRECISE | §5 says the verification "ran CPU only". The claim is about CPU memory (no model load; box_acquire_olmo.py:105 loads into CPU RAM), so the two wordings clash.
76. GA-1: G-CAL-OLMo's loads go through CPU memory first (OLMoHFAdapter: from_pretrained(...).to(device)) | RAW GA-1 | PASS | scripts/m_sessions.py:799–808 (_load_olmo → OLMoHFAdapter); olmo_hf.py:81–82.
77. GA-1: a box with 125 GB | RAW GA-1 | UNVERIFIABLE | operator-only (RunPod pod record).
78. GA-2: the 12-hex prefix, as the four entries have; weights_of_record accepts 12–40 hex; the full sha is in §2 | RAW GA-2; ENTRY | PASS | manifest revisions c2b61dae89a1, 152782ecc41a, fc84a4f69991, ac0587e4a774, b96024342a77; gcal.py:739 r"[0-9a-f]{12,40}"; RAW l.24.
79. GA-4: the default 8192 exceeds 4,096 and the adapter refuses it (attempt 1) | RAW GA-4; ENTRY | PASS | olmo_hf.py:45, 85–90.
80. GA-4: "n's windows are declared by the n package (§8 step 6), each ≤ 4,096"; ENTRY: "n's declared windows are each ≤ 4,096" | RAW GA-4; ENTRY GA-4 | IMPRECISE | no n window exists yet: the n package is not built, PROPOSAL-n contains no "window" text, and §8 step 6 (PROPOSAL-n:159) names none. It is a requirement worded as a fact, more so in the ENTRY.
81. GA-4: rule 28(d)'s standing form (c) | RAW GA-4 | PASS | CLAUDE.md:405–407.
82. GA-4: BK's 160 neutral sessions run 1,266–1,273 tokens (seq_len) | RAW GA-4; ENTRY | PASS | 14 files under data/n/bk/…/skeletons/olmo_32b/neutral/: 160 records, seq_len min 1266, max 1273 (1273 in 144 of them).
83. GA-5: the 24 reads need n's cached read path, built at step 6; they run before LOCK-n v0.1 states §2.1's identity bound; (ii) shared | RAW GA-5; ENTRY | PASS | PROPOSAL-n:77 (§2.1's fresh-cache re-compute and its "Identity:" clause), :117 (LOCK-n v0.1 "the identity bound"), :159 (step 6's read runner).
84. GA-6: "37.07 at indices 31 and 32" | RAW GA-6 | FAIL | index 32 is 37.0880 (json 37.08802795410156), which is 37.09 to two places. Only index 31 is 37.07.
85. GA-6: one 17-token sentence averaged over all positions, the first included; R is G-VEC's | RAW GA-6; ENTRY | PASS | the script takes the mean over all 17 positions; PROPOSAL-n:111.
86. api_rev.json is 9,274 bytes and not reproduced | RAW §9 | PASS | ls: 9274.
87. "the §5 table carries every value of it the checks used" | RAW §9 | IMPRECISE | the table gives blob ids as 12-hex prefixes, though the checks compared all 40. It gives no LFS sha256 values, only equality plus our sha256[:16]; the full values exist only via the manifest. The listing's sha and safetensors.total are in §2/§5 text, not in the table.
88. Attempt 1's script "differed only in …" | RAW §9 heading | IMPRECISE | the attempt-1 traceback shows its constructor line's comment ending "(env.sh sets it)", which gacq_hooksite.py:46 lacks. Otherwise the line shifts (41→46, 92→99) fit exactly +5 (comment block and cap) and +2 (the record keys). Attempt 1's file is not available to check further.
89. ENTRY headline "G-ACQ (n) … PASS" | ENTRY head | IMPRECISE | G-ACQ (PROPOSAL-n:109) includes the BACKEND extension over 24 reads, which was not run (GA-5). Bullet 4 discloses this, but the verdict line does not scope it.
90. Write-time stamp "Sat Nov 7 03:30:57 UTC 2026" | ENTRY | UNVERIFIABLE | written at write time; the weekday is right and it follows the last box stamp, 03:27:32Z.
91. "(OLMoHFAdapter, deterministic, bf16)" | ENTRY hook site | PASS | olmo_hf.py:51–55 defaults to deterministic=True and dtype "bfloat16"; attempt 2 overrides neither.
92. "§8's next node is step 6, the n package build, on the laptop" | ENTRY last | PASS | PROPOSAL-n:159: step 6 is the n package build. The site is not named there; "on the laptop" is the plan, consistent with CLAUDE.md's Environment section (the laptop is the dev site).
93. RAW–ENTRY consistency for every other figure (22 and 51 files, five checkpoints, stamps, hashes, 64,478,373,025 B, notes GA-1 to GA-6) | ENTRY, all bullets | PASS | each matches the RAW item above. The only differences are those flagged in items 4, 31, 80 and 89.
94. The push-approval record promised for "the routing session's G-ACQ entry" is absent | ENTRY (absent); RAW (absent) | FAIL | RESULTS.md:132 (added at 3b22158) and 3b22158's message both say "the routing session's G-ACQ entry records the approval verbatim": the PI's "Yes, push them" to "Push the three new local commits?". Neither draft contains it (grep "push them|approv": no match).

**Summary: 94 items — 71 PASS, 2 FAIL, 12 IMPRECISE, 9 UNVERIFIABLE.**

Observations (not draft claims; not counted):
- Order. Both hook-site forwards ran before respawn (i) over the five-entry manifest finished: attempt 1 at 03:14:15Z–03:17:10Z, attempt 2 at 03:18:19Z–03:20:35Z, respawn at 03:19:05Z–03:27:32Z (attempt 2 and the respawn overlapped). Attempt 1 also launched before 0415438 was committed (22:16:21 −0500 = 03:16:21Z). The drafts state no order, but §6→§7→§8 reads as sequential. 0415438's message says "the entry, its raws and the hook-site check follow".
- Rule 27. gacq_hooksite.json (per-layer rows, ids, full-precision norms) and gacq_verify.json appear neither in the RAW nor in the ENTRY's "Committed by path" list. Only verify.json's entry survives, as the manifest entry.

---

## Code's dispositions

Code re-checked every non-PASS item at its source before applying it. The item numbers are the report's.

| # | verdict | disposition |
|---|---|---|
| 4 | IMPRECISE | Applied. §9 now reproduces `gacq_verify.json` and `gacq_hooksite.json`, together with the hub's listing (`api_rev.json`) and a capture of the box's state at write time. The entry restates the carriage-return caveat. |
| 7 | UNVERIFIABLE | Code's own chat question in the routing thread; kept as stated. The answer, "Now, in parallel", is in `54bbfe5`'s close (item 8). |
| 17 | UNVERIFIABLE | Resolved. §9's box-state capture records `huggingface_hub 1.28.0`, with `hf_xet` installed, alongside transformers 5.15.0 and torch 2.8.0+cu128. |
| 22 | IMPRECISE | Applied. §2 quotes the whole object, `{"parameters": {"BF16": 32234279936}, "total": 32234279936}`. |
| 25 | UNVERIFIABLE | The current reading (466 / 302 / 164) is in §9's box-state capture. The two earlier readings are from Code's session at the time and are kept. |
| 29 | UNVERIFIABLE | The pod session's message to Code; kept. The checker's reading of `scripts/m_sessions.py:707–737` agrees. |
| 31 | IMPRECISE | Applied. The header, §4, GA-3 and the entry now place the download and the verification during the pod session's smoke self-test (01:41:54Z–02:07:28Z), both ending before G-CAL-OLMo's runs began at 02:20:02Z. |
| 33 | IMPRECISE | Applied: "It checks three things and computes a fourth, and it exits 0 only if the three checks pass." |
| 38 | IMPRECISE | Applied: the aggregate is the sha256 of the concatenated `name:sha256` strings, in sorted name order. |
| 43 | UNVERIFIABLE | Resolved. §9's box-state capture lists `olmo2_instruct.hf-local-dir-meta` in `/workspace/staging-n`, with 47 files. |
| 46 | UNVERIFIABLE | Evidenced for everything G-ACQ touched. §9's box-state capture lists every G-ACQ file still in `/workspace/staging-n`, the moved-aside metadata folder (47 files), the six moved-aside G-CAL files, and the five checkpoint folders at 7 / 7 / 7 / 8 / 22 entries. |
| 54 | UNVERIFIABLE | Resolved. §9's box-state capture gives the six files' full sha256s under `/workspace/repo/box-untracked-gcal-2026-11-06/`, at their repository paths. It also records the box repo at HEAD `04154382…` with 0 porcelain lines. |
| 56 | IMPRECISE | Applied. §7 now says the adapter declares `DEFAULT_CHOICE_WINDOW = 8192` (`olmo_hf.py:41–45`). It also notes that the script's own comment, "OLMo-3's", is loose; the script stays as it ran. |
| 70 | IMPRECISE | Applied. (ii) now says the backend identifier is `190ba90`'s and that no G-ACQ script recomputes it. |
| 75 | IMPRECISE | Applied: "out of CPU memory, since no model was loaded for it". |
| 77 | UNVERIFIABLE | The RunPod API's pod record for `qny1x4v8padeke` (`get-pod`: memory 125); kept. |
| 80 | IMPRECISE | Applied. No n window exists yet. The n package is to declare them, and LOCK-n v0.1 holds each at or below 4,096. The raw and the entry both say this. |
| 84 | FAIL | Applied: "37.07 at index 31 and 37.09 at index 32". |
| 87 | IMPRECISE | Applied. `api_rev.json` is reproduced in §9, and the claim that the table carries every value is gone. |
| 88 | IMPRECISE | Applied. The heading names attempt 1's three differences, including the constructor comment's "(env.sh sets it)". |
| 89 | IMPRECISE | Applied. The headline reads "PASS on every part run", followed by a bold line "Not run: the BACKEND extension's 24 fresh-versus-cached reads, which wait for the n package (GA-5)". |
| 90 | UNVERIFIABLE | The entry's stamp is re-taken when the entry is inserted. |
| 94 | FAIL | Applied. The raw gains "The push of `1bf94a6..273ca8f`, recorded", and the entry gains "The second push, recorded": the PI's "Yes, push them" to "Push the three new local commits?" (`958e762`, `190ba90`, `273ca8f`), the re-screen and the push, and `273ca8f`'s message predating that word. |
| obs. (order) | — | Applied. §7 gains an "Order" bullet: attempt 1 launched two minutes before `0415438` was committed, although that commit's message says the check follows it; attempt 2 ran during respawn (i). The entry's hook-site bullet says so too. |
| obs. (rule 27) | — | Applied: both result JSONs are in §9. |

No figure, hash or count of record changed. The two FAILs were a rounding (GA-6) and an omitted record (the push). The manifest at `0415438` is untouched.
