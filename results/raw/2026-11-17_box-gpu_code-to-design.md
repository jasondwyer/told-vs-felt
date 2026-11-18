# The box: n's GPU if the A100 stays unavailable — three questions for the seat (code → design)

*The coordinating session (Code), PI date 2026-11-17. For the PI to route.*

*Why now: the PI asked "Are there other GPU models we can switch to?" and, to the offer of this block, said "Yes,
draft it".*

*What ran on 2026-11-16, run by the pod session, none of it on a model:*
- *n's step-4 smoke under the draft driver (`64cf6ee1…16cb`, the box's manifest line), refused before the load;*
- *the read-only probe `probe_cuda.sh` (`621113f4…20c9`), before and after the restart.*

*What was done on Runpod, through its API and on the PI's words:*
- *reads, on 2026-11-17: the pod, the network volume, the GPU stock and the prices;*
- *one action, `pod-action start` on the stopped pod. It was refused on "push it, and probe the pod", and at each
  retry since the PI's "Yes, retry", every 20 minutes (§1, item 5).*

*Sources read:*
- *`CLAUDE.md` (`955788de…8a62`): the Environment section (:85), its box line (:91) and the respawn protocol
  (:115–134);*
- *`WORKFLOW.md` (`e7195706…b061`), §4;*
- *the seat's answers of 2026-11-15 (`1f3ce1f9…f84b`), §5.4;*
- *`PROPOSAL-m-gating-campaign-v1_11.md` (`42ab36ec…6c6b`) :302;*
- *`PROPOSAL-n-bk-reconciliation-v0_2.md` (`30a3d0f5…04f4`) :103, :109, :117 and :161;*
- *`valence_core/adapters/olmo_hf.py` (`df80b79b…92dc`) :311–336, the provenance;*
- *`valence_core/m/resume.py` (`78f2fc8e…8fb7`) :141–147 and :239–245, the backend identifier;*
- *the BACKEND entry of `7ab4d2f` and its raw `results/raw/2026-11-15_respawn_determinism.txt` (`faca18c6…7f96`);*
- *n-build's step-4 driver draft `scripts/n_sessions.py`, as it stands in n-build's scratch, uncommitted
  (`64cf6ee1…16cb`);*
- *n-build's step-4 box output `bext_box_out.txt`, in its scratch, uncommitted (`e2d9774c…831f`);*
- *the pod session's two CUDA probe outputs of 2026-11-16, in its scratch, uncommitted: before the restart
  (`16745bd2…50e9`) and after it (`0d0ebe6c…5643`).*

*Not opened: any `ckpt`, `reports` or call-log path.*

## 0. Short form

n was planned on pod `m43y3deb1gq3rp`, an A100 SXM in US-CA-2, characterized at `641ee466f4553b6a` (`7ab4d2f`; the
seat's answers of 2026-11-15, §5.4). That box cannot be used now:
- on 2026-11-16 its GPU failed CUDA initialization with error 802, at n's step-4 smoke and at the probes before and
  after a restart;
- on 2026-11-17 Runpod refused its start at every attempt: its host had no free GPU.

US-CA-2 is the only data center that can mount the volume holding the checkpoints. It lists no A100 SXM; it lists an
H100 SXM and an H200 SXM. On Code's reading of the code (§3), either would be a new backend for n.

- **Q1:** may n move to one of them if the A100 stays unavailable?
- **Q2:** if so, what does the new box need, and what becomes of n's step 4, which is written as an extension of the
  A100's characterization?
- **Q3:** if the A100 pod starts healthy, on the driver it reported after the restart (595.112.07, where the
  characterization's raw records 595.91.07), is it still the backend of `7ab4d2f`'s characterization for n?

Not a STOP. n's model-free work goes on, the seat's adoption read of `fa96ccf` among it. n's box work waits for a working
box either way, and the A100 start is retried every 20 minutes.

## 1. What happened to the box (Code's report, declared without adjudicating)

1. **2026-11-16, n's step-4 box check** (run by the pod session for n-build). torch could not initialize CUDA:
   "CUDA initialization: Unexpected error from cudaGetDeviceCount()", with "Error 802: system not yet initialized".
   - The stage refused before the load, at R6's check. With CUDA unavailable, the provenance's GPU name and capability
     were None, and it hashed to `bcb9d44161b4a3d0`, not `641ee466f4553b6a`.
   - No weights were loaded.
2. **The pod session's read-only probe, before any restart** (one interpreter call, no allocation, no model; nothing
   written on the box):
   - `torch.cuda.is_available()` False, `device_count()` 1;
   - nvidia-smi: NVIDIA A100-SXM4-80GB, driver 595.91.07, CUDA 13.2. That is the driver the 2026-11-15
     characterization's raw records.
   - Persistence Disabled, MIG Disabled, ECC Enabled, no remapped rows, nothing pending, Fabric N/A.
3. **On the PI's "Restart it once" (2026-11-16)** the same probe gave the same result: `is_available()` False, error
   802. nvidia-smi now reported driver 595.112.07 and persistence Enabled; nothing else in the probe's output changed.
4. **On the PI's "Stop it" (2026-11-16)** the pod was stopped. Its network volume is intact.
5. **2026-11-17.** The PI's "push it, and probe the pod" answered an offer that stated the plan:
   - start the pod ($2.19/h) and run the read-only probe;
   - stop it at once on error 802;
   - if the GPU works, run respawn (i) and (ii), then n's step-4 smoke.

   Runpod refused the start: "There are not enough free GPUs on the host machine to start this pod." A stopped pod
   starts only on its own host.
   - **The retries.** On the PI's "Yes, retry", the coordinating session retries the start every 20 minutes, and every
     retry so far has been refused. The watch is session-only and creates nothing else.
   - **The probe comes first.** A start that succeeds runs the read-only probe first. Code declares that order: the
     probe loads no model and writes nothing, and it precedes (i) and (ii) because (ii) needs a working GPU. CLAUDE.md
     :127 says "Both PASS before anything runs".
   - **After the probe.** On error 802 the pod is stopped at once. If the GPU is healthy, respawn (i) and (ii) run,
     then n's step-4 smoke under the draft driver, never of record. The driver's commit and step 4's run of record
     wait for Q3.
6. **The cause is not established.** Code's reading, not a finding:
   - error 802 on an NVSwitch (SXM) host is the known symptom of the host's fabric manager not running against the
     loaded driver;
   - the driver change between the two probes is consistent with host maintenance;
   - nvidia-smi's Fabric fields read N/A in both probes. On Code's understanding, not checked against NVIDIA's
     documentation, they are not reported for A100s, so they add nothing either way.

   Code opened no ticket with Runpod.

## 2. The stock, 2026-11-17

Runpod's API, Secure cloud, pods, one GPU each:

- **The volume:** `o73qvy742n` is in US-CA-2, HIGH_PERFORMANCE, 500 GB as Runpod reports it (CLAUDE.md's "466 GB" is
  the same size in GiB). A pod mounts it only in US-CA-2.
- **US-CA-2 lists**, both with LOW stock:
  - H200 SXM, 141 GB, $5.29/h;
  - H100 SXM, 80 GB, $4.39/h.
- **No A100 SXM in US-CA-2.** The A100 SXM costs $2.19/h and is listed, with LOW stock, in EUR-IS-1, US-KS-2,
  US-MD-1, US-MO-1 and US-WA-1.
- **Stock moves within minutes.**
  - A data-center listing showed only the H200 for US-CA-2; the H100 type's listing, read moments later, included
    US-CA-2.
  - On 2026-11-15 the A100 took fifteen reads to appear in US-CA-2 (the seat's answers of 2026-11-15, §5.4).
- **Other types with 80 GB or more** are listed only outside US-CA-2 (A100 PCIe, H100 NVL, RTX PRO 6000 at 96 GB).
  Any of them would mean a new volume and the checkpoints acquired again. This block does not propose that.

## 3. Why a Hopper box is a new backend (Code's reading of the code)

- **The identifier.** It is the sha16 of the adapter's provenance, minus `n_encodes_clipped`, `path` and `seed`
  (`resume.py` :141–147, :239–245).
  - The OLMo adapter's provenance carries the GPU's name and its compute capability (`olmo_hf.py` :325–328), and no
    driver version. Its `cuda` field (:326) is torch's build CUDA, not the driver's.
  - So a restart of the same A100 pod after the driver change can reproduce `641ee466f4553b6a`: the identifier cannot
    see the driver (Q3).
  - An H100 or H200 cannot: another name, and capability 9.0 against the A100's 8.0.
  - m's PIN states the limit: "it cannot tell two boxes of one class apart (m:267) -- hence the pod id" (`resume.py`
    :146). On the laptop, the OS build is part of the backend (:144–145).
- **The respawn protocol** (`CLAUDE.md`, Environment):
  - any new or replacement box passes (i) INTEGRITY and (ii) BACKEND before any experimental forward;
  - the backend of record for a campaign is the one its own runs were characterized on;
  - a campaign is never spliced across backends.
- **The program's box-change form.**
  - m:302 records each box in a "`BACKEND — characterization` entry for that box". It adds: "A box change after a
    checkpoint's lock aborts and restarts that checkpoint's campaign on the new box under its existing lock, the new
    backend identifier recorded in a new `BACKEND` entry that supersedes the lock's field".
  - n's own text makes the characterization per box: G-ACQ's "`BACKEND — characterization` for this box, extended
    with the fresh-versus-cached discordance distribution over 24 reads" (n :109), and its entry list's
    "`BACKEND — characterization` (per box)" (n :161).
  - n's resume identity carries "the backend identifier and the pod instance id" (n §2.8, :103).
- **n's step-4 driver as drafted** (uncommitted, `64cf6ee1…16cb`) is written for that box. It refuses:
  - unless the pod is `CHARACTERIZED_POD = "m43y3deb1gq3rp"` (:249, :633);
  - unless n's environment provenance, with its declared window reset to the adapter's default (R6), hashes to
    `CHARACTERIZED_IDENTIFIER = "641ee466f4553b6a"` (:257, :655).

  Its comment at :247–248 says so: "A new box is a new characterization and a change here." On a Hopper box it
  refuses by construction.
- **The stated class.** CLAUDE.md :91 describes the box as a "single 80GB A100/H100-class GPU". The H100 SXM is inside
  that description. The H200 is a Hopper GPU, but at 141 GB it is larger than :91 states.
- **Neither p nor n is spliced by a move.**
  - p's three campaigns (`41bfab4`), run on the A100 backend, and the three VERDICTS computed from them on the laptop
    (`679122e`, `8a7cdf8`, `9662468`) are committed.
  - A p re-run, if one were ever asked for, would be the seat's to place. On Code's reading, the consistency clause
    lets a campaign restart whole on a new backend but never splice onto the A100's runs.
  - n has run nothing on a GPU.

## 4. Questions

**Q1. If the A100 pod stays unavailable, may n's box move to a Hopper GPU in US-CA-2, mounting the same volume?**
Readings to weigh:
- (a) Yes, H100 SXM (80 GB, $4.39/h): the same memory as the A100 that p's campaigns ran on, and inside CLAUDE.md
  :91's class.
- (b) Yes, H200 SXM (141 GB, $5.29/h): more headroom, though larger than :91 states. n's memory need on the box is
  unmeasured: its step-4 smoke refused before the load (2026-11-16).
- (c) Not yet: wait for the A100 while the retry goes on, until a date the seat names; after it, (a) or (b). On
  2026-11-15 the A100 took fifteen reads to appear in US-CA-2.
- (d) No: n waits for an A100 SXM, either in US-CA-2 or elsewhere with a new volume and the checkpoints acquired again.

The moment and the spend stay the PI's in every reading.

**Q2. If (a), (b) or (c): what does the new box need before n's first forward, and what becomes of step 4?**
Readings to weigh:
- (a) A full characterization, n's own:
  - respawn (i) INTEGRITY, as on any box;
  - then (ii) BACKEND, a full determinism and kernel-path characterization on the new GPU, in a
    `BACKEND — characterization` entry for that box (CLAUDE.md's "dated entry"; the form of m:302 and of n §3 G-ACQ,
    n :109), its identifier becoming n's backend of record;
  - n's step-4 driver re-drafted to that pod and identifier. Its R6 bridge to the A100's characterization
    (`641ee466f4553b6a`, `7ab4d2f`) is retargeted to the new characterization if that is taken under the adapter's
    default window, as `7ab4d2f`'s was, or dropped if it is taken under n's declared 4,096-token window;
  - the backend identifier and pod id enter each unit's resume identity (n §2.8, :103);
  - LOCK-n v0.1 states that p's results (A100) and n's (Hopper) sit on different backends. That is an addition to its
    contents list (n :117).
- (b) Another procedure the seat names.

**Q3. If the A100 pod starts healthy, on driver 595.112.07 where the characterization's raw records 595.91.07, is it
still the backend of `7ab4d2f`'s characterization for n?**
Readings to weigh:
- (a) Yes, once respawn (ii) re-runs on it and its identifier equals `641ee466f4553b6a`. The identifier cannot see the
  driver (§3), so the driver change is recorded in that respawn's dated entry. n's step 4 then runs as drafted, its
  driver committed first.
- (b) No: a driver change is a backend change, as the OS build is on the laptop (`resume.py` :144–145). The restarted
  pod gets a new `BACKEND — characterization`, and step 4 is re-pinned as in Q2 (a).
- (c) Another reading the seat names.

## 5. Not questions

- **p** is unaffected: its outputs are committed.
- **The corpus** (N.1, `fa96ccf`) is model-free and unaffected. The seat's adoption read stands apart from this block.
- **Any pod's creation, start and spend** wait for the PI's word, and no pod is created without it. The retries, and the
  plan after a successful start, rest on the PI's words quoted in §1, item 5.
- **A Runpod ticket** about the 802 is the PI's.

## 6. Next

The A100 start is retried every 20 minutes, as in §1, item 5. If a start succeeds and the GPU is healthy:
- the probe, respawn (i) and (ii), and n's step-4 smoke, which is never of record;
- then Q1 and Q2 fall away;
- the driver's commit and step 4's run of record wait for Q3.
