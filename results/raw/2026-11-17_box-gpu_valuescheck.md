# The box: the GPU block's blind values-check, as returned, with every disposition

PI date 2026-11-17. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over two drafts:
- the block, `results/raw/2026-11-17_box-gpu_code-to-design.md`, then titled "two questions";
- its RESULTS.md entry.

The drafts were revised in place after the check, and their sha256s before the revision were not taken. This raw's §1
lists every change made after the check.

**The checker's brief:**
- named the sources, committed and uncommitted;
- quoted the PI's words verbatim;
- quoted the list of record v2's items 1–5 verbatim, item 4 as amended by the seat's C.2;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3` or a `ckpt` or `reports` path, a
  whole-tree `git status`, any write, any Runpod tool, any `--stat` form, and the pod's address or port in any output.

**The report.** It is in §3 below, extracted verbatim from the subagent's hand-back by script: 150 lines, sha256
`e49c6ead…1ccb` as extracted. One local path is written `<the laptop's path>`; the text below is `5671884a…c5fe`.

**Totals:** 76 items — 50 CONFIRMED, 14 IMPRECISE, 0 FAIL, 12 NOT CHECKABLE — and 12 observations.

## 1. Dispositions

**The IMPRECISE items, all applied** (in the checker's words unless stated):
- **13** (header, the Runpod action). Applied with the count left open: the start was refused on "push it, and probe the
  pod", and at each retry since "Yes, retry" (observation 8).
- **14** (header, what ran and the sources). Applied: the "What ran" lines; `bext_box_out.txt` (`e2d9774c…831f`) and
  PROPOSAL-m v1.11 (`42ab36ec…6c6b`) :302 among the sources. PROPOSAL-n v0.2 (`30a3d0f5…04f4`) is added for
  observations 3 and 4.
- **18** (§0, the 802). Applied.
- **19** (§0, the refusals). Applied as "on 2026-11-17 Runpod refused its start at every attempt: its host had no free
  GPU" (observation 8).
- **21** (§0, "a new backend"). Applied.
- **50** (§3, p's commits). Applied.
- **51** (§3, a p re-run). Applied, in two sentences.
- **54** (Q1 (b), n's memory). Applied.
- **55** (Q2 (a), the entry form). Applied.
- **56** (Q2 (a), the R6 bridge). Applied with observation 5: the bridge to the A100's characterization is retargeted
  if the new characterization is taken under the adapter's default window, or dropped if it is taken under n's
  declared 4,096-token window.
- **62** (entry, the 802). Applied.
- **65** (entry, "a new backend"). Applied.
- **68** (entry, the gitleaks parenthesis). Applied.
- **69** (entry, the C.5 header and its first line). Applied: the header names `e5aba51`'s entry, and the first range is
  one line naming the class, not the port's value (observation 10).

**The observations:**
1. **The Fabric clue.** Applied. §1.6 now rests the fabric-manager reading on error 802 on an NVSwitch host. It says
   the Fabric fields add nothing either way, on Code's understanding, not checked against NVIDIA's documentation.
2. **The driver change.** Applied as a new question, Q3: is the restarted A100 on driver 595.112.07 still the backend of
   `7ab4d2f`'s characterization for n? §1.5 and §6 now hold step 4's commit and run of record for Q3; the step-4 smoke
   (never of record) does not wait.
3. **Uncited texts.** Applied: CLAUDE.md :91 in §3 and Q1; n :109 and :161, and m:302's box-change sentence, in §3;
   the fifteen reads of 2026-11-15 in §2 and Q1 (c).
4. **LOCK-n v0.1's contents.** Applied: Q2 (a) cites n §2.8 (:103) for the identity, and names the lock's statement an
   addition to its contents list (:117).
5. **The R6 bridge.** Applied with item 56.
6. **500 GB and 466 GB.** Applied in §2.
7. **The plan after a start.**
   - The PI's word "push it, and probe the pod" answered an offer that stated the plan (start, probe, stop on 802,
     respawn (i)/(ii), step-4 smoke). §1.5 now quotes the plan.
   - Code declares the probe's place before (i) and (ii), with CLAUDE.md :127 quoted.
   - The step-4 smoke is named as never of record. The driver's commit and its run of record wait for Q3.
8. **The stale count.** Applied: no count; "at every attempt" and "at each retry since".
9. **Push #6's record.** Applied in the coordinating session's scratch: the screen and gitleaks over `977b78b..fa96ccf`
   were run again and their outputs kept verbatim beside the push record. Not committed, like the earlier push records.
10. **The port's value.** Applied with item 69.
11. **How the stage refused.** Applied in §1.1: R6's check, the provenance hashing to `bcb9d44161b4a3d0`.
12. **"waits either way".** Applied: "waits for a working box either way".

**The NOT CHECKABLE items (12)** rest on the Runpod API's reads, the PI's words and the session's own acts. No change.

## 2. The edits after the check, checked by tool

- Every quote in the revised block and entry was checked by script against its sources: 24 + 6 quotes, all found.
  The PI's words were checked against a list typed from the chat.
- The one quote the script splits, the driver draft's :247–248 sentence, was checked by joining the two comment lines:
  found.
- The anchors added after the check were opened at the cited lines: CLAUDE.md :85, :91, :127; m:302; n :103, :109,
  :117, :161; `resume.py` :144–146.
- The sources' sha256s, the four added included, were recomputed by tool: `probe_cuda.sh`, `bext_box_out.txt`,
  PROPOSAL-m v1.11 and PROPOSAL-n v0.2.
- The final block and entry: the block `80b7cacf…2fc8` (204 lines), the entry `37202227…c066` (40 lines).

## 3. The report as returned

```text
BLIND VALUES-CHECK — D1 (2026-11-17_box-gpu_code-to-design.md) and D2 (entry.md), at HEAD fa96ccf

Tools and rules: I used Read (both drafts, the adapter file, the driver draft) and Bash. Bash ran shasum, git (rev-parse, show HEAD:<path>, log, rev-list --count, merge-base, blame; status only on named paths), grep and /usr/bin/grep on single files, sed with address and port redaction, name-only ls, diff, and `gitleaks version`. All the rules held:
- Read-only: no file written, no interpreter run, no Runpod tool called, no --stat.
- No marker word in any argv. Marker-named paths were reached by cd and a glob.
- Nothing under data/mf3 or any ckpt or reports path was listed, opened, hashed or searched. No whole-tree status.
- No pod address or public SSH port was printed. The one port string in my output was push_record4's screen line: the container's standard port, the one D2 quotes. I do not repeat it below.

ITEMS

1. D1 header — "CLAUDE.md (955788de…8a62)" — CONFIRMED — shasum of the working tree equals shasum of HEAD's blob; named-path status is clean.
2. D1 header — "WORKFLOW.md (e7195706…b061)" — CONFIRMED — same method.
3. D1 header — "the seat's answers of 2026-11-15 (1f3ce1f9…f84b)" — CONFIRMED — results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md, working tree = HEAD.
4. D1 header — "olmo_hf.py (df80b79b…92dc)" — CONFIRMED — working tree = HEAD. The box's hash line in bext_box_out.txt gives the same value.
5. D1 header — "resume.py (78f2fc8e…8fb7)" — CONFIRMED — working tree = HEAD.
6. D1 header — "results/raw/2026-11-15_respawn_determinism.txt (faca18c6…7f96)" — CONFIRMED — working tree = HEAD.
7. D1 header — "n_sessions.py draft, uncommitted (64cf6ee1…16cb)" — CONFIRMED — the scratch file hashes to that value. It is also the line for scripts/n_sessions.py in step4/box/bext_manifest.txt, so it is the driver that ran on the box. HEAD's committed driver is aa0b5404…e05f and has no CHARACTERIZED_POD.
8. D1 header — "probe before the restart (16745bd2…50e9)" — CONFIRMED — probe_cuda_out.txt.
9. D1 header — "probe after it (0d0ebe6c…5643)" — CONFIRMED — probe_cuda2_out.txt.
10. D1 header — "Are there other GPU models we can switch to?" and "Yes, draft it" — CONFIRMED — character for character against the brief.
11. D1 header — "Nothing ran on a model." — CONFIRMED, as far as the sources show — the step-4 smoke refused before the load (bext_box_out.txt:48–49), and probe_cuda.sh loads no model.
12. D1 header — "reads, on 2026-11-17: the pod, the network volume, the GPU stock and the prices" — NOT CHECKABLE — Runpod API.
13. D1 header — "one action, on "push it, and probe the pod": `pod-action start` on the stopped pod, refused (§1, item 5)" — IMPRECISE — D1's own §1.5 says the start was refused twice, and the 20-minute retries on "Yes, retry" are further Runpod actions the header leaves out. Accept: "*one action, on "push it, and probe the pod": `pod-action start` on the stopped pod, refused twice (§1, item 5); since the PI's "Yes, retry", the same start every 20 minutes.*"
14. D1 header — sources read, and what ran — IMPRECISE — three gaps:
   - Q2(a) cites m:302, but PROPOSAL-m is not among the sources.
   - §1.1's facts (the refusal before the load) rest on n-build's bext_box_out.txt, which is not listed.
   - WORKFLOW §4 (:35) asks the header for "what ran, under which lock and driver (hashes)".
   Accept these additions:
   - "*What ran, on 2026-11-16, run by the pod session, none of it on a model: n's step-4 smoke under the draft driver (`64cf6ee1…16cb`, the box's manifest line), refused before the load; the read-only probe `probe_cuda.sh` (`621113f4…20c9`), before and after the restart.*"
   - in the sources: "*n-build's step-4 box output `bext_box_out.txt`, in its scratch, uncommitted (`e2d9774c…831f`);*" and "*`PROPOSAL-m-gating-campaign-v1_11.md` (`42ab36ec…6c6b`) :302.*"
15. D1 header — "Not opened: any ckpt, reports or call-log path." — NOT CHECKABLE.
16. D1 header — "CLAUDE.md: the Environment section and its respawn protocol" — CONFIRMED — the Environment heading is at CLAUDE.md:85 and the respawn protocol at :115–134, under it.
17. D1 §0 — "pod m43y3deb1gq3rp, an A100 SXM in US-CA-2, characterized at 641ee466f4553b6a (7ab4d2f; §5.4)" — CONFIRMED:
   - answers:66 (§5.4: the pod "stays up after p's campaigns, for n", characterized at 641ee466f4553b6a);
   - 7ab4d2f's subject;
   - the respawn raw :2 (1 × NVIDIA A100-SXM4-80GB, data center US-CA-2).
18. D1 §0 — "since 2026-11-16 its GPU fails CUDA initialization with error 802" — IMPRECISE — the present tense claims a continuing state for a pod that is stopped. 802 was observed three times on 2026-11-16: the smoke (bext_box_out.txt:44) and both probes. Accept: "on 2026-11-16 its GPU failed CUDA initialization with error 802, at n's step-4 smoke and at the probes before and after a restart;"
19. D1 §0 — "since it was stopped, its host has no free GPU to start it on" — IMPRECISE — the only evidence, given in §1.5, is the two refusals on 2026-11-17, not a state lasting since the stop. Accept: "on 2026-11-17 Runpod refused its start twice: its host had no free GPU."
20. D1 §0 — "US-CA-2 is the only data center that can mount the volume…; it lists no A100 SXM; it lists an H100 SXM and an H200 SXM" — NOT CHECKABLE — Runpod. The volume's US-CA-2 home is consistent with 7ab4d2f's entry: a US-CA-2 pod mounted o73qvy742n at /workspace.
21. D1 §0 — "Either would be a new backend of record for n." — IMPRECISE — this is a reading stated as fact; it is labelled only in §3. Accept: "On Code's reading of the code (§3), either would be a new backend for n."
22. D1 §0 — "n's step 4, which is written as an extension of the A100's characterization" — CONFIRMED:
   - answers:66 ("n's BACKEND extension … runs on it");
   - the driver's docstring :25–28 ("backend-ext  the BACKEND extension, on the box");
   - PROPOSAL-n v0.2 :109.
23. D1 §0 — "Not a STOP … the seat's adoption read of fa96ccf" — CONFIRMED — fa96ccf's subject: "not a STOP … For the seat's ruling, beside the adoption read".
24. D1 §0, §1.5 and §6 — "the A100 start is retried every 20 minutes", on "Yes, retry" — NOT CHECKABLE — the quote matches the brief; the cadence is the session's own act.
25. D1 §1.1 — "2026-11-16 … run by the pod session for n-build" — CONFIRMED:
   - the box copy was at HEAD 977b78b (bext_box_out.txt:2), and 977b78b was committed on 2026-11-16;
   - "Stop it" was on 2026-11-16 per the brief;
   - the pod session's scratch holds launch_bext.sh, wait_bext_out.txt and outbext_*.
26. D1 §1.1 — "CUDA initialization: Unexpected error from cudaGetDeviceCount()" and "Error 802: system not yet initialized" — CONFIRMED — both are exact substrings of bext_box_out.txt:44 (each found once). The same warning appears in both probe outputs at :2.
27. D1 §1.1 — "No weights were loaded; the stage refused before the load." — CONFIRMED — bext_box_out.txt:48 reads "before the load: the environment's provenance under the default window hashes to bcb9d44161b4a3d0, not the characterization's 641ee466f4553b6a (R6)", and :49 reads "smoke exit=1". The WEIGHTS line at :47 is a byte-count check, not a load.
28. D1 §1.2 — "one interpreter call, no allocation, no model; nothing written on the box" — CONFIRMED as the script's design — probe_cuda.sh's header comment says so. Its body makes one `python -B -c` call that only does import torch, is_available() and device_count(); the rest is nvidia-smi.
29. D1 §1.2 — "is_available() False, device_count() 1" — CONFIRMED — probe_cuda_out.txt:6–7.
30. D1 §1.2 — "NVIDIA A100-SXM4-80GB, driver 595.91.07, CUDA 13.2" — CONFIRMED — probe_cuda_out.txt:10–11 and :14.
31. D1 §1.2 — "That is the driver the 2026-11-15 characterization's raw records." — CONFIRMED — the respawn raw :2: "driver 595.91.07, driver CUDA 13.2".
32. D1 §1.2 — "Persistence Disabled, MIG Disabled, ECC Enabled, no remapped rows, nothing pending, Fabric N/A" — CONFIRMED:
   - :15 Disabled; :17 MIG Current Disabled; :21 ECC Current Enabled;
   - all Remapped Rows counts 0, with Pending No;
   - the pending MIG and ECC modes equal the current ones; repairs Pending No;
   - Fabric State, Status and Health are all N/A (:40ff).
33. D1 §1.3 — "Restart it once" (2026-11-16): the same probe, the same result; driver 595.112.07; persistence Enabled — CONFIRMED — the quote matches the brief. A diff of the two outputs differs only at :10 (Driver 595.91.07 → 595.112.07) and :15 (Persistence Disabled → Enabled). Error 802, is_available False and device_count 1 are unchanged. Only one probe script exists in the folder.
34. D1 §1.4 — "Stop it" (2026-11-16); the pod was stopped; its network volume is intact — NOT CHECKABLE — the quote and date match the brief; the rest is Runpod.
35. D1 §1.5 — "push it, and probe the pod"; start refused twice, with Runpod's message; "A stopped pod starts only on its own host" — NOT CHECKABLE — the quote matches the brief; the rest is Runpod.
36. D1 §1.5 — the session-only watch that "creates nothing else", and the after-start plan — NOT CHECKABLE.
37. D1 §1.6 — "Code's reading, not a finding: error 802 … Fabric N/A … consistent with … fabric manager …; driver change … consistent with host maintenance" — CONFIRMED as labelled — the values it rests on are as the probes show. Its evidential weight is discussed in O1.
38. D1 §1.6 — "Code opened no ticket with Runpod." — NOT CHECKABLE.
39. D1 §2 — the stock and prices; the volume at 500 GB, HIGH_PERFORMANCE; the listing anecdote; the other types — NOT CHECKABLE — Runpod reads. 7ab4d2f's entry records "No money figure", so the committed record holds no price at all. The volume id and its US-CA-2 home are consistent with 7ab4d2f.
40. D1 §3 — "sha16 of the adapter's provenance, minus n_encodes_clipped, path and seed (resume.py :141–147, :239–245)" — CONFIRMED — :141–146 is the PIN comment, :147 is BACKEND_DROP = ("n_encodes_clipped", "path", "seed"), and :239–245 hashes with sha256 and keeps [:16].
41. D1 §3 — "provenance carries the GPU's name and its compute capability (olmo_hf.py :325–328), and no driver version" — CONFIRMED — :325 gpu, :327–328 capability. The record at :322–336 has no driver field; :326 "cuda" is torch's build CUDA (12.8 in the raw), not the driver's (13.2).
42. D1 §3 — "a restart of the same A100 pod after the driver change can reproduce 641ee466f4553b6a" — CONFIRMED as a reading — the identifier has no driver field. The respawn raw :76–78 gives the same identifier for the "committed 2026-08-19 block", which came from an earlier box.
43. D1 §3 — "An H100 or H200 cannot: another name, and capability 9.0 against the A100's 8.0" — CONFIRMED — the raw :17–21 shows the gpu "NVIDIA A100-SXM4-80GB" and capability [8, 0]. That Hopper is 9.0 is general knowledge, not a repo source.
44. D1 §3 — the respawn protocol's three bullets — CONFIRMED, as paraphrases — CLAUDE.md:116–117 ("On any new or replacement box, before any experimental forward"), :123–125 ("the backend of record for any campaign is the one its own runs were characterized on") and :130 ("campaigns are never spliced across backends").
45. D1 §3 — "refuses unless the pod is CHARACTERIZED_POD = "m43y3deb1gq3rp" (:249, :633)" — CONFIRMED — :249 is exact; :633–635 raises SystemExit.
46. D1 §3 — "…with its declared window reset to the adapter's default (R6), hashes to CHARACTERIZED_IDENTIFIER = "641ee466f4553b6a" (:257, :655)" — CONFIRMED:
   - :257 is exact; :655–657 is the refusal;
   - :357–362 (bridge_identifier) sets choice_window_declared to DEFAULT_CHOICE_WINDOW, which is 8192 (olmo_hf.py:45);
   - n declares schema.MAX_WINDOW = 4096 (schema.py:254; the driver's :353).
47. D1 §3 — the comment at :247–248, "A new box is a new characterization and a change here." — CONFIRMED — the sentence starts at :247 ("A new") and continues at :248 after the "#: " comment marker; the join is exact.
48. D1 §3 — "On a Hopper box it refuses by construction." — CONFIRMED — both checks would refuse: a different pod id, and a different gpu name and capability in the hashed provenance.
49. D1 §3 — "Neither p nor n is spliced by a move." — CONFIRMED as a reading in a labelled section — p is complete; for n see item 52.
50. D1 §3 — "p's three campaigns (41bfab4) and its three VERDICTS (679122e, 8a7cdf8, 9662468) are committed, on the A100 backend." — IMPRECISE — the subjects are right: 41bfab4 is "on pod m43y3deb1gq3rp (backend 641ee466f4553b6a, 7ab4d2f)", and the three are the dpo, sft and instruct VERDICTS. But the VERDICTS were computed on the laptop (9662468: "Nothing ran on a model"). Accept: "p's three campaigns (`41bfab4`), run on the A100 backend, and the three VERDICTS computed from them on the laptop (`679122e`, `8a7cdf8`, `9662468`) are committed."
51. D1 §3 — "A p re-run, if one were ever asked for, would need that backend." — IMPRECISE — it overreaches. CLAUDE.md:127–130 lets a campaign restart whole on a new backend, and m:302's last sentence restarts a locked campaign on a new box under a superseding BACKEND entry. Accept: "A p re-run, if one were ever asked for, would be the seat's to place; on Code's reading, the consistency clause lets a campaign restart whole on a new backend but never splice onto the A100's runs."
52. D1 §3 — "n has run nothing on a GPU." — CONFIRMED, as far as the record shows — the step-4 smoke refused before the load, and n's tiny-model self-test runs with device "cpu" (valence_core/n/hftiny.py:47).
53. D1 §4 Q1(a) — "the same memory as the A100 that p's campaigns ran on" — CONFIRMED — the A100-SXM4-80GB reads 81,920 MiB (7ab4d2f's entry), and the H100 SXM is 80 GB. The price is NOT CHECKABLE.
54. D1 §4 Q1(b) — "n's memory need on the box is unmeasured, since its step-4 smoke never ran" — IMPRECISE — read literally it is false: the smoke ran and refused before the load (bext_box_out.txt:46–49). Accept: "n's memory need on the box is unmeasured: its step-4 smoke refused before the load (2026-11-16)."
55. D1 §4 Q2(a) — "logged as a dated note under m:302" — IMPRECISE:
   - m:302 (PROPOSAL-m v1.11 :302; WORKFLOW :41, where m:N = v1.11's line N) says "`BACKEND — characterization` entry for that box", and it is m's OLMo-checkpoint step.
   - n's own text is n §3 G-ACQ: "`BACKEND — characterization` for this box, extended with …" (PROPOSAL-n v0.2 :109; and :161, "(per box)").
   - In 7ab4d2f, the "dated note" was the separate note on the lock entry.
   Accept: "then (ii) BACKEND, a full determinism and kernel-path characterization on the new GPU, in a `BACKEND — characterization` entry for that box (CLAUDE.md's "dated entry"; the form of m:302 and of n §3 G-ACQ, PROPOSAL-n v0.2 :109), its identifier becoming n's backend of record;"
56. D1 §4 Q2(a) — "with the R6 bridge to p's 641ee466f4553b6a dropped" — IMPRECISE — the identifier belongs to the A100 box's characterization (7ab4d2f; the R6 docstring :65–66), and it already appears on the 2026-08-19 block (raw :78). It is not p's. Accept: "with the R6 bridge to the A100's characterization (`641ee466f4553b6a`, `7ab4d2f`) dropped".
57. D1 §5 — "p is unaffected: its outputs are committed" — CONFIRMED — the subjects of 41bfab4, 679122e, 8a7cdf8 and 9662468.
58. D1 §5 — "The corpus (N.1, fa96ccf) is model-free" — CONFIRMED — fa96ccf's subject says "Model-free". It names both N.1 and N.3; push_record6 calls fa96ccf "n corpus N.1".
59. D1 §6 — "retried every 20 minutes … Q1 falls away" — CONFIRMED — consistent with §1.5.
60. D2 head — "On the PI's "Yes, draft it". Block: …/2026-11-17_box-gpu_code-to-design.md. Not a STOP." — CONFIRMED — the quote matches the brief. The path matches D1's filename and WORKFLOW §4's path form (:34), and the entry has its "Next".
61. D2 The box — "pod m43y3deb1gq3rp (A100 SXM, US-CA-2, characterized at 641ee466f4553b6a, 7ab4d2f)" — CONFIRMED — as item 17.
62. D2 The box — "Its GPU has failed CUDA initialization with error 802 since 2026-11-16, before and after the PI's restart." — IMPRECISE — "since" implies a continuing state, as in item 18. Accept: "Its GPU failed CUDA initialization with error 802 on 2026-11-16, before and after the PI's restart."
63. D2 The box — "stopped on the PI's word. Since then Runpod has refused its start twice (2026-11-17): its host has no free GPU." — NOT CHECKABLE — Runpod. It is consistent with D1 §1.5.
64. D2 The stock — US-CA-2 lists no A100 SXM; H100 SXM (80 GB, $4.39/h); H200 SXM (141 GB, $5.29/h) — NOT CHECKABLE — Runpod. It is consistent with D1 §2.
65. D2 The stock — "The backend identifier carries the GPU's name and capability, so either would be a new backend of record for n." — IMPRECISE — the first half is CONFIRMED (items 40–41); the conclusion is an unlabelled reading. Accept: "The backend identifier carries the GPU's name and capability, so on Code's reading either would be a new backend for n."
66. D2 The stock — "n's step-4 driver draft pins the A100 pod and identifier." — CONFIRMED — :249, :257, :633, :655.
67. D2 — Q1/Q2, and "n's model-free work goes on" — CONFIRMED — consistent with D1 §0 and §4.
68. D2 C.5 — "(gitleaks 8.30.1, the one on the laptop's path)" — IMPRECISE — the version is right: `gitleaks version` gives 8.30.1 at <the laptop's path>/gitleaks. But the form of record (RESULTS.md:3052–3053) adds "the runs' outputs do not print its version", which is still true (gitleaks_push4.out has no version line). Accept: "(gitleaks 8.30.1, the one on the laptop's path; the runs' outputs do not print its version)".
69. D2 C.5 — "the pushes since the note's close line, one line each" — IMPRECISE:
   - "the note" is not named in this entry. It is the push note e5aba51 (RESULTS.md:3037), whose close line was committed at 52b2c97, inside the first range.
   - The first range is three sub-bullets, not one line.
   Accept the header "**C.5, the pushes since the push note's close line (`e5aba51`'s entry), one line each**", and the first range as one line: "`bedc198..9662468`, 10 commits, on the PI's word "Push them" (2026-11-16): every class CLEAR but `port`, whose one match outside was read (the container's SSH port, in a values-check's text); nothing inside `ckpt` or `reports`; gitleaks, 3 `generic-api-key` matches outside, read (`data/n/ids/MANIFEST.json`'s tokenizer digests, equal to `data/olmo/manifest.json`'s); no halt."
70. D2 C.5 — "bedc198..9662468, 10 commits, "Push them" (2026-11-16)" — CONFIRMED — git rev-list --count gives 10; push_record4 has the PI's word and the RANGE line.
71. D2 C.5 — the screen (C.2's form): one port match outside, read as the container's SSH port in a values-check's text; every other class CLEAR; nothing inside — CONFIRMED — push_record4: "screen4.py: item 4 as amended by C.2"; [port] 1 distinct outside, inside 0, at results/raw/2026-11-16_routing-second-sitting_valuescheck.md@52b2c97; the READ disposition; the other five classes CLEAR.
72. D2 C.5 — gitleaks: 3 generic-api-key outside, MANIFEST.json's tokenizer digests equal to the model manifest's; nothing inside; no halt — CONFIRMED:
   - push_record4: ('outside', 'generic-api-key', 'hex64-other') x 3 at data/n/ids/MANIFEST.json@d76f34f; d76f34f is in the range;
   - "READ, not a halt";
   - my check: each of the three tokenizer_files digests appears once in the committed model manifest, under the same file name.
73. D2 C.5 — "9662468..977b78b, 2 commits, "Push them" (2026-11-17): every class CLEAR …; gitleaks found nothing; no halt" — CONFIRMED — rev-list gives 2; push_record5: all six classes CLEAR, "no leaks found", "no halts".
74. D2 C.5 — "977b78b..fa96ccf, 1 commit, "push it, and probe the pod" (2026-11-17): CLEAR, nothing inside; gitleaks found nothing; no halt" — CONFIRMED — rev-list gives 1; push_record6: "screen4 CLEAR on all six classes (exit 0); gitleaks 8.30.1: 0 findings … no halts". The record quotes the PI only as "push it"; D2's fuller quote matches the brief.
75. D2 Next — the retry, the probe first, stop on 802, otherwise respawn (i)/(ii) and then step 4 — CONFIRMED — consistent with D1 §1.5 and §6.
76. D2 — "Committed by path: the block and this entry. Not pushed." — NOT CHECKABLE — it is a future act.

OBSERVATIONS

1. §1.6's Fabric clue adds no weight. As I recall NVML's documentation (not a repo source, not checked here), the GPU fabric state behind nvidia-smi's Fabric fields is reported only on Hopper and later. On an A100 those fields read N/A whatever the fabric manager is doing, and both probes show N/A. Error 802 ("system not yet initialized") on an NVSwitch host is the known fabric-manager symptom on its own. Suggest: "error 802 on an NVSwitch (SXM) host is the known symptom of the host's fabric manager not running against the loaded driver; the Fabric fields, N/A here, are not reported for A100s in any state."
2. The driver change is not put to the seat:
   - The identifier cannot see the driver (olmo_hf.py :322–336).
   - resume.py :144–146 makes the laptop's OS build backend-defining, and discloses that the identifier "cannot tell two boxes of one class apart (m:267)".
   - Yet §1.5 and §6 treat the restarted A100, now on driver 595.112.07, as the characterized backend once the identifier reproduces ("Q1 falls away and n's step 4 runs as drafted").
   A careful reader would want that labelled as a reading, or asked.
3. Texts that bear on Q1/Q2 and are not cited:
   - CLAUDE.md:91, "single 80GB A100/H100-class GPU": the H100 is inside the stated class and the 141 GB H200 is not.
   - PROPOSAL-n v0.2 :109 and :161 already make n's characterization "for this box" / "(per box)".
   - m:302's last sentence is the program's existing box-change procedure.
   - 7ab4d2f's entry: the A100 took 15 reads (about 21 minutes apart) to appear in US-CA-2, which bears on Q1(c).
4. On Q2(a)'s "LOCK-n v0.1 declares n's backend": PROPOSAL-n :117's contents list for LOCK-n v0.1 does not name the backend. :103 (§2.8) puts the backend identifier and pod id in each unit's resume identity. The reading is fine, but it is an addition.
5. On Q2(a)'s "R6 bridge … dropped": R6 exists because the BACKEND characterization is taken under the adapter's default window (8192), while n declares 4096. If the new box is characterized the same way, the bridge is retargeted, not dropped. It is dropped only if n's own characterization is taken under n's declared window.
6. §2 says "500 GB"; CLAUDE.md:98–99 says "Persistent volume 466 GB". These agree if CLAUDE.md's figure is GiB (500 GB ≈ 465.7 GiB). A parenthesis would spare the seat the check.
7. The plan after a successful start has gaps:
   - "Yes, retry" covers the retries, but no PI word is cited for the stop on 802, the respawn runs or step 4's spend, while §5 says "Any pod's … start and spend wait for the PI's word."
   - The probe runs before (i)/(ii), against CLAUDE.md:127 "Both PASS before anything runs". It is read-only, but worth a clause.
   - "Step 4 as drafted" is an uncommitted driver (HEAD's driver differs). The block does not say whether it would run as a smoke or as the run of record after a commit.
8. "Refused … twice" (D1 §1.5, D2) will go stale while the 20-minute retry runs. State the count at the commit, or say "twice, then at each retry since".
9. Push #6's record is a one-line summary. Unlike pushes 4 and 5, no verbatim screen or gitleaks output for 977b78b..fa96ccf sits in push4/.
10. D2's first C.5 line writes the matched port string. The C.5 form of record (RESULTS.md:3054–3055) named only the class ("every class CLEAR but `port`"). The value is the container port 7ab4d2f's entry already declares, so nothing new is exposed, but it departs from the form.
11. D1 §1.1 does not say how the stage refused. It was R6's check: with CUDA unavailable, gpu and capability were None, and the provenance hashed to bcb9d44161b4a3d0 (bext_box_out.txt:48). One clause would show the guard working.
12. D1 §0's "n's box work waits either way" can be read as "waits for the seat", which would contradict §1.5 and §6, where step 4 runs on a healthy restart without a ruling. Suggest "waits for a working box either way".

TOTALS: 76 items — 50 CONFIRMED, 14 IMPRECISE, 0 FAIL, 12 NOT CHECKABLE.
- CONFIRMED: 1–11, 16, 17, 22, 23, 25–33, 37, 40–49, 52, 53, 57–61, 66, 67, 70–75.
- IMPRECISE: 13, 14, 18, 19, 21, 50, 51, 54, 55, 56, 62, 65, 68, 69.
- FAIL: none.
- NOT CHECKABLE: 12, 15, 20, 24, 34, 35, 36, 38, 39, 63, 64, 76.
```
