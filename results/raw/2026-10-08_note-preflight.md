# AUDIT-note-release v1.2 -- preflight (referent inventory)

- Code stamp: 2026-10-08 02:52:27 UTC (date -u)
- HEAD: 988e5dfd6b6092e0c1e90cda3bc1356beb5e78c4
- Block: `AUDIT-note-release-v1_2.md`, sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841`, 141 lines (routed as 8cd8a9ac...3841, 141 lines: MATCH)
- Script: `scripts/audit_note_preflight.py` (read-only; stdlib)
- Interpreter: /Users/jasondwyer/miniconda3/bin/python3 (Python 3.12.9)

Status codes: T = tracked at HEAD; U = present, untracked (not in a clone); L = present, gitignored/local only; MISSING = no match on this machine.

## N1 (block :21)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `RESEARCH-NOTE-v0_2-draft.md` | MISSING | 0 | |
| `FIGURE-REVIEW-2026-10-06.md` | MISSING | 0 | |
| `*F1*.svg` | MISSING | 0 | |
| `*F2*.svg` | MISSING | 0 | |
| `figures/*.svg` | MISSING | 0 | |
| `PREPRINT-v1_1-draft.md` | MISSING | 0 | |
| `PREPRINT-v1_0-draft.md` | U=1 | 1 | d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8 |
| `RESULTS.md` | T=1 | 1 | 37a2f1087df2e7af28889ebfd3e3564dd17a7556b508344074300f1a5a2a5250 |
| `archive/RESULTS-cycle1-2.md` | T=1 | 1 | 0b05acb7a56114bce6ba5c248f535f21e2114488f626105a7b164251c2296aeb |
| `archive/RESULTS-cycles3-4.md` | T=1 | 1 | 5ec5d48a0fcb977b55de244c2dfdb81547887ed36398b1c7f33e4991f5b6e051 |
| `FINDINGS*.md` | T=5 | 5 | `FINDINGS-2.md` 93218b67177bc853 |
| `scripts/paper_data.py` | T=1 | 1 | 2315893c3c927f53cc9bce06a4c7af6ddad1bd1f7716fbcdd129a36126577e69 |
| `NOTE-HEAT-PLAN*` | MISSING | 0 | |

## N2 (block :28)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `scripts/b2_analyze.py` | T=1 | 1 | 6c18bc8c182985f171e00c8083bd1c0cd55b7b64608146e54d634a5c85ab3df8 |
| `scripts/b2r_analyze.py` | T=1 | 1 | 7ebd7d56866ff78390778d9971e77b45e02cdffb201e6a6cdfe84201b3ee6a47 |
| `scripts/box_b2_detection.py` | T=1 | 1 | 6c4a639effac636b33e79b7e0aba86433ac5bd000b8db8cebf95ade77cfe85d0 |
| `scripts/box_b2r_campaign.py` | T=1 | 1 | 630356648337868918ae5d411bedb34ef9f026ce0c7972a222e92e620ca109a8 |
| `valence_core/detection.py` | T=1 | 1 | 29cd93a53b2ec5bc0c8236002ba63dc5dc5fc5b0e38d89d41f47e4bb8adaafd9 |
| `valence_core/detection_v2.py` | T=1 | 1 | 89b6653d62a8510169a61f843728914f81053b142cc5d354a6c0544e932a4c42 |
| `data/configs/b2_concepts.json` | T=1 | 1 | 42db27ca54a73b1f0ed7734fa99bf70723d599a9a771341f127f58629adc0ef3 |
| `data/configs/b2_framing.json` | T=1 | 1 | 99b7a69453b32547b60d712b1a57b3b8abffd2450cc3c28fcd76755b8577a10e |
| `data/configs/scorer_v3_spec.json` | T=1 | 1 | 46e77258016b5a9a79cc950d364951b99bfd8f7b9da8e8b21ef4936cc8f8dc2a |
| `data/olmo/*.json` | T=88 | 88 | `data/olmo/a1_repair_base.json` 4eff0306ae29c220 |
| `data/olmo/b2r_analysis.json` | T=1 | 1 | 33844bd0b89103ffdb79595e1ec7495f3e8dda1c1f5739442553b3f294e730ac |
| `data/olmo/b2r_explore_sft.json` | T=1 | 1 | 497d701718ab8d73d563b1159a07c9c54574258e234a4af6d55408fb3c7ceee2 |
| `data/olmo/b2r_explore_dpo.json` | T=1 | 1 | f796d425e5547401e4302c9d1dfff3497520effc4491da80c1b3894af03dfdbd |
| `data/olmo/b2r_explore_instruct.json` | T=1 | 1 | 9f44000030ed448481eb132afcef3e4ab27be03c1f4bcad8c5cd9fd1c627b036 |
| `ADDENDUM-g3-b2r-v1.2.md` | T=1 | 1 | 33b474753b2d6d9037af7a7eedfb00db6df8ee3322b230b5b35c26a9f7f5fa6c |

## N3 (block :41)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `scripts/recon_echo.py` | T=1 | 1 | ba390b710083afe192eebd2f01fce5a8ad8b92d1ed1439165bc8b245f8df3e08 |
| `valence_core/echo/probe.py` | T=1 | 1 | d90f9281dff612977da5a3c3ce1a07155159a48103b35dfe521e0fac30152b81 |
| `valence_core/echo/spans.py` | T=1 | 1 | 5445eac70f6f6fbf8f154531c32fa230f548c5cf657435bbd2e322f0f10e848b |
| `valence_core/echo/maskedprefix.py` | T=1 | 1 | 10ab1d7c51ba3b08981f9890a163a4c94c757e86239ca338160b91245e699854 |
| `valence_core/echo/k1.py` | T=1 | 1 | 549f1a042f4ce8cf790bc2cb452bdacd9658abd05dcb8fcfdf151288bfe4b7dd |
| `data/echo/*.json` | T=10 | 10 | `data/echo/stageA_analysis.json` c94942b96769ddce |
| `data/echo/*.npz` | L=228 | 228 | `data/echo/stageA_resid_s0.npz` c17ab805aa68c65f |
| `results/raw/2026-09-06_recon_echo_stageC_analysis.txt` | T=1 | 1 | 657ead0c36d5ee09a8762525a0819e9e47f7f8e9f17ad457e05592e242ddd17b |
| `PROPOSAL-k-echo-channel.md` | T=1 | 1 | bf7e79ec9ad85afc1299d944fe8b60468dbc1c16fae581f3ee446dea4ff23e92 |
| `data/k/*.json` | T=3 | 3 | `data/k/k1_analysis.json` 366beaa001ede026 |
| `scripts/k1_analyze.py` | T=1 | 1 | e9b99868aeacfee6c393a4f37db7900609e1397a922bb290f8d5d0feb80b5ca1 |

## N4 (block :55)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `scripts/e2a_recount.py` | T=1 | 1 | d58a889c7736c4a385d7098546b815666eb5426712a83f94414f135339270107 |
| `valence_core/session_e2a.py` | T=1 | 1 | f1e53db2e9089ed3869e75693474fa6f36eccf667d1f2a4fbe52b4ba1fe73c71 |
| `data/e2a/*.json` | T=11 | 11 | `data/e2a/analysis.json` 79cd53c0adf55878 |
| `data/e2a/*.jsonl` | T=5 | 5 | `data/e2a/g3prime_kl.jsonl` aad2cebe0b8ae3af |
| `data/e2a/analysis.json` | T=1 | 1 | 79cd53c0adf55878628d38a5a00e4045d2a216d28b1f0b2ed90b2304920dd52e |
| `data/configs/e2a_ban_list.json` | T=1 | 1 | 9a2f0744f81ac930fdf8533c7d07b77bd15a5361e89b060363d022c3661d31c4 |
| `archive/RESULTS-cycles3-4.md` | T=1 | 1 | 5ec5d48a0fcb977b55de244c2dfdb81547887ed36398b1c7f33e4991f5b6e051 |
| `scripts/box_cached_gen_smoke.py` | T=1 | 1 | c9260f372c3e3ca1bab51e150ffeb171d8399d422c61952f3efba94057a3d5f6 |

## N11 (block :67)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `README.md` | T=1 | 1 | 0605316fc35f164d5efe7dbc27f5f4d258ee5de918b5a88c67953d4225ac1f1f |
| `valence_core/regression/analysis.py` | T=1 | 1 | 1f897ea99390e4d676eee83fb406234b8f5eaed27414647bbc1bc0523c126f10 |
| `.gitattributes` | T=1 | 1 | 0c18a48fce6337b49694c4e28aee42ae0fa0fda6400184754983e5de4d924d35 |
| `.gitignore` | T=1 | 1 | d643ff1ee680bb958f1dc30c4c3b126a3cc68f904749bc77cc590298712e7413 |

## N12 (block :75)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `CLAUDE.md` | T=1 | 1 | 955788dec22ee820917693bf49137619bda1a30eb37e07f118b3940473de8a62 |
| `.git/config` | U=1 | 1 | 404d7917dfbea77e26776724d1f3921043f47a8947cdba6fbb74adfc11cd0a56 |
| `scripts/box_*.py` | T=23 | 23 | `scripts/box_a1_repair_screen.py` 2f7e90c8a0134122 |
| `scripts/run_*.sh` | T=2 | 2 | `scripts/run_b2r.sh` 0b6c6333b83a8f5e |
| `results/raw/*` | T=258 | 258 | `results/raw/2026-07-16_debug_ablation.txt` 2e021d64eb4288a2 |
| `HANDOFF-*.md` | T=8, U=6 | 14 | `HANDOFF-2026-08-20.md` 2521887cfab61f4d |
| `.gitignore` | T=1 | 1 | d643ff1ee680bb958f1dc30c4c3b126a3cc68f904749bc77cc590298712e7413 |
| `data/configs/b2_concepts.json` | T=1 | 1 | 42db27ca54a73b1f0ed7734fa99bf70723d599a9a771341f127f58629adc0ef3 |
| `data/configs/b2_framing.json` | T=1 | 1 | 99b7a69453b32547b60d712b1a57b3b8abffd2450cc3c28fcd76755b8577a10e |
| `jlens-qwen36` | dir; 0 tracked files under it | 1 | |

## N13 (block :90)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `PROPOSAL-d*.md` | T=1 | 1 | 1ab3cddc2cf66eb7e599735038ed31b9b18a3663cdaac181910b32fd0e128fee |
| `PROPOSAL-e*.md` | T=1 | 1 | 4ca23f41bf902e75a210109231b673c0ca705faabc57b22975f8d5297c8113f1 |
| `PROPOSAL-f*.md` | T=1 | 1 | d7a131eabf8d30a8b7d6ebde75c7b53b7ded88468d6d366010d1403282afb8bf |
| `PROPOSAL-g*.md` | T=1 | 1 | add38ab412d5e028564ec5a6a95db1d6e56ffaa3a7c4c1b6ccf0679c756b9f5c |
| `PROPOSAL-h*.md` | T=1 | 1 | 445c631db0b278331784bd67308373ab12c39ef530f9bc5f90b0cdf02dd45584 |
| `PROPOSAL-j*.md` | T=1 | 1 | 394701704d36c795790339a75e72661f3135e3e64473d2088e5c74f2563d93a7 |
| `PROPOSAL-k*.md` | T=1 | 1 | bf7e79ec9ad85afc1299d944fe8b60468dbc1c16fae581f3ee446dea4ff23e92 |
| `LOCK-g.md` | T=1 | 1 | eb0420a168ee1535a65e50ade9bae2b479e98bdb1a418531258e4607c809b5d8 |
| `LOCK-h.md` | T=1 | 1 | 7f08260ef4054a03c8df7c6abdd21bd948ef7ac3541aee2a2e590a4bd3c877c7 |
| `ADDENDUM-*.md` | T=2, U=3 | 5 | `ADDENDUM-g1-archival-reading-screen.md` e11a011b02312f42 |

## N5 (block :98)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `data/f/*.json` | T=4 | 4 | `data/f/calib.json` 55e5f75fb9c5bbf4 |
| `data/f/*.jsonl` | T=2 | 2 | `data/f/sessions.jsonl` d49913e5ffdfb935 |
| `PROPOSAL-f-natural-reinforcer-screen.md` | T=1 | 1 | d7a131eabf8d30a8b7d6ebde75c7b53b7ded88468d6d366010d1403282afb8bf |
| `data/configs/f_termination_patterns.json` | T=1 | 1 | 014b3940d62401b0b698e803145362b56c0b74de7d9f087a4fce0ecb111c2f46 |

## N6 (block :101)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `data/e2b/*.json` | T=15 | 15 | `data/e2b/h1_gate.json` 3e62629519be4972 |
| `scripts/e2b_verdict_analyze.py` | T=1 | 1 | 5114657c82478d9521b0ab07920cbcb94ebae5a3f53717ef305492feb1bda718 |
| `scripts/e2b_h1_gate.py` | T=1 | 1 | adb79e7f1bff3cad923841d68cd3f8adac66fbac99d6176928a0c601d038d86a |
| `scripts/h1_power.py` | T=1 | 1 | 37a87a0793d9cabc32e3b4183fae7dfc3b6e40211a905c866d4e34c4a6e0e360 |
| `valence_core/e2b/statepresent.py` | T=1 | 1 | 2ef62542c086a55e5ef2456cc06f947bd6015a1a12793f2a9f24be548931881d |
| `valence_core/e2b/records.py` | T=1 | 1 | eddf380be203aa4de971f9e62dece09c3f797cb00be3302127dcf92aa7194dd6 |
| `PROPOSAL-h-state-present-choice.md` | T=1 | 1 | 445c631db0b278331784bd67308373ab12c39ef530f9bc5f90b0cdf02dd45584 |
| `LOCK-h.md` | T=1 | 1 | 7f08260ef4054a03c8df7c6abdd21bd948ef7ac3541aee2a2e590a4bd3c877c7 |

## N7 (block :104)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `scripts/b1_verdict.py` | T=1 | 1 | 7b030010126c4d8d344d3c37d44e69266ce1b3d2ca28dbbe20d5d0169300d88a |
| `scripts/b3_analyze.py` | T=1 | 1 | 01dc3669dd0e8e7fe56301106b66fc2bd3ed1bacfbccc87a45719cbbbd2d3c30 |
| `scripts/box_a4_hijack.py` | T=1 | 1 | 82e7bb29613128f21f680d727f77bb0fe5357223dab353e054dd68d20283a923 |
| `scripts/box_b3_sessions.py` | T=1 | 1 | a2dab7d78d13dfc07c1abe90f57786ce23e8131ced24ac3c888c19be9ea68867 |
| `data/olmo/*.json` | T=88 | 88 | `data/olmo/a1_repair_base.json` 4eff0306ae29c220 |
| `PROPOSAL-g-ontogeny-of-evaluation.md` | T=1 | 1 | add38ab412d5e028564ec5a6a95db1d6e56ffaa3a7c4c1b6ccf0679c756b9f5c |
| `LOCK-g.md` | T=1 | 1 | eb0420a168ee1535a65e50ade9bae2b479e98bdb1a418531258e4607c809b5d8 |

## N8 (block :107)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `valence_core/regression/analysis.py` | T=1 | 1 | 1f897ea99390e4d676eee83fb406234b8f5eaed27414647bbc1bc0523c126f10 |
| `valence_core/regression/oracle.py` | T=1 | 1 | 36823122f571d33e95895ac566ae60e2a76ee3c01185a8c5d1ff9ae8b041a9b8 |
| `data/configs/c1r3_gate_repA.json` | T=1 | 1 | 96664fba17fcb33b32955c5f94c9ef3229c9c35b0578cdba00ab7d328e95ece8 |
| `data/configs/c1r3_gate_repB.json` | T=1 | 1 | aeebc4424ff31f5388975fdd94c79984a2433fb558bf1516e1e0cbe5c7bf13f1 |
| `data/e0/*` | T=11 | 11 | `data/e0/e0_axes.meta.json` e0b3ebf6aa91e0ec |
| `data/e2d/*.json` | T=24 | 24 | `data/e2d/closure_glosscheck3.json` 2350e71e51ae3068 |
| `scripts/e2d_closure_verify3.py` | T=1 | 1 | d896e8b7a69461a8223aa91e5833b8a0711cbea63c122d649e10b63fe5277cbe |

## N9 (block :110)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `data/d/*.json` | T=2 | 2 | `data/d/gates_repA.json` 5895d84288cd37ab |
| `PROPOSAL-d-distilled-trace.md` | T=1 | 1 | 1ab3cddc2cf66eb7e599735038ed31b9b18a3663cdaac181910b32fd0e128fee |

## N10 (block :113)

| referent | status | matches | sha256 (working tree, first) |
|---|---|---|---|
| `ADDENDUM-g1*.md` | T=1 | 1 | e11a011b02312f4245fccc6bfa208c055cfd52dc34ef8b9ac8e6595949cc5147 |
| `PROPOSAL-h-state-present-choice.md` | T=1 | 1 | 445c631db0b278331784bd67308373ab12c39ef530f9bc5f90b0cdf02dd45584 |

PREPRINT-v1_0-draft.md sha256 d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8 vs block's d6431e97...222b8: MATCH; tracked: NO (untracked: absent from any clone)

## Code's notes on the inventory (the block's own rule: a wrong referent is a note, not a STOP)

Every observation below comes from a tool run in this session (the table
above, `git status`, `git remote -v`/`git branch -a`, interpreter probes, and
the committed site-check raw cited). None of them is a STOP.

1. **N1's primary referents are not on this machine.**
   `RESEARCH-NOTE-v0_2-draft.md`, the Digest seat's F1/F2 SVGs of 2026-10-06,
   `FIGURE-REVIEW-2026-10-06.md`, `PREPRINT-v1_1-draft.md` (which the block
   calls the "project copy") and NOTE-HEAT-PLAN all return MISSING. The ledger needs one
   row per figure in the note, so it cannot be finished against the note until
   the PI puts `RESEARCH-NOTE-v0_2-draft.md` (and the SVGs, for the plotted
   values) at root. Until then Code builds the ledger over every figure the
   block itself quotes, plus the post-patch-v4 preprint, and marks it
   provisional. N18 (the note's sha) waits on the final note in any case.
2. **Regression-suite count.** README.md:55-57 and the block (N11 :68, :70;
   N8 :107) say **103/103**. The suite at HEAD prints **154/154**: see the
   committed site check `results/raw/2026-10-07_m-dispositions_sitecheck.txt`,
   "154/154 reproduced through valence_core", run under
   `jlens-qwen36/.venv/bin/python`. N11 therefore passes if the suite prints
   N/N from a fresh clone, and the raw states N. Every place that still says
   103 is listed for the PI: the README (not edited here) and the note's text
   (not seen).
3. **`PREPRINT-v1_0-draft.md` is untracked.** It matches the block's sha
   (d6431e97...222b8) but is absent from any clone. The same holds for 23 other
   untracked root/archive files in `git status`: six `HANDOFF-*-design.md`,
   `ADDENDUM-g3-b2r.md` (v1.0), `ADDENDUM-g3-b2r-v1.1.md`, `ADDENDUM-k1.md`,
   `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md`, the three pre-patch preprint
   copies and PROPOSAL-m v1.2-v1.10 in `archive/`. Only
   `ADDENDUM-g3-b2r-v1.2.md` and `ADDENDUM-g1-archival-reading-screen.md` are
   tracked. A reader of the tag sees only what is tracked. N13 records which
   pre-registration texts exist in the record; whether to commit the others is
   the PI's call.
4. **What a public push would carry.** The remote has a second branch,
   `origin/claude/handoff-doc-next-steps-oeccd1`. The tags are `cycle-2-close`
   and `cycle-4-close`. The history scans in N12 run over `--all`, so they
   cover that branch.
5. **Interpreter and libraries.** The record's site checks run under
   `jlens-qwen36/.venv/bin/python`: Python 3.12.9, numpy 2.5.1, no scipy, no
   sklearn. The other interpreters on the machine (miniconda base, envs
   asi-experiments and velocity-web-api, homebrew python3) have no sklearn
   either. The audit installs nothing. N3(iii)'s MLP and RBF-kernel
   classifiers are written in numpy and declared as such; the exact tests
   (binomial, Fisher, Wilson) use the stdlib.
6. **Secret scanners.** Neither gitleaks nor trufflehog is installed. N12(i)
   runs the block's fallback grep over `git log -p --all`, plus a blob-level
   scan of every object reachable from `--all`. Installing gitleaks would be a
   download, so it happens only on the PI's word.
7. **Residual arrays are local.** `data/echo/*.npz` has 228 files (stageA 24,
   stageB 102, stageC 102), all gitignored. N3(ii)-(iv) can run here.
8. **Commit plan.** Commit 1 holds the block, `scripts/audit_note_preflight.py`
   and this raw, per the PI's routing ("Commit the block with the first raw").
   Later raws are committed as their tier completes, so none lives only in a
   working tree. Code reads §0.6's "one commit at the end" as the
   README-NOTE/tag commit. That reading is flagged for the PI and is not
   assumed to be settled.
9. **Waiting on the PI.** N12(iii) needs the continuity password, out of
   band. N19 needs an external repository cloned and a notebook run (a
   download plus third-party code), so Code will ask before Tier 2 reaches it.
   The tag name and the release date are the PI's.
