# n — G-READ-n's launch files: the blind review of the step script v1, as returned, with every disposition

PI date 2026-11-25. Code (the n-build session). In the report in §2, as returned, a bare "Line N" or "Lines N–M" is a
line of the step script v1, and `n_sessions.py:N` (or a bare number beside the driver) a line of the driver at
`0cc301d` (`35c4c73e…4808`).

**What was reviewed.** One blind pass by a subagent over G-READ-n's launch steps as v1 had them, at HEAD `0cc301d`, in
Code's scratch:
- the step script, `gread_steps_v1.sh` (`3d6a031f…7346`, 133 lines): four steps, `check <HEAD>`, `run`, `wait <PID>`
  and `after`, each run once, in that order, as its own call in one window the coordinating session grants;
- its helper, `pkgsha.sh` (`4edcf928…6465`, 13 lines): the n package's digest by shell;
- its stand-in test, `test_steps_v1.sh` (`01dbf0c7…1c03`, 28 lines), and the note that sent the files to the
  coordinating session (`83cd30a4…2a74`, 99 lines).

**The reviewer's brief** was a file the reviewer read itself, as its prompt directed: Code's scratch file
`S/step4b/gread/launch/review_brief_v1.md` (`2eefa873…415e`, 105 lines). It:
- named the script, its helper, its test and the note, each by sha256;
- named what the script must do: GR14 of Code's readings as sent (and GR1, GR2 and GR8–GR11 where they bear on the
  launch), G-ANL-n's run as its entry records it, the driver's `gread` command at HEAD, the list of record's rules,
  and what Code knew from earlier launches on this Mac;
- put the coordinating session's question: whether the check should refuse on battery, or the window should say AC,
  or both;
- asked for findings, the answer on AC power, run risks, observations and departures;
- barred any interpreter but `shasum`, any write, any network, any run of the script or its test or of a process they
  start (`caffeinate`, `nohup`, `pgrep`, `pmset`, `ps`), any guard marker in an argv (a grep pattern and the command's
  own text included), and Q-F3's folder by its plain name in any argv;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size, time or hash of a ckpt or
  reports file, anything outside the repository but the named scratch and notes files (the staging folder above all),
  the venv's folder, and any naming of G-TIME-n's holding folder in an argument;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec with `':!data/m[f]3/**'` on every
  git command over the tree.

**The report** is in §2, saved verbatim by `jq` from the subagent's hand-back (250 lines, sha256
`72103a37709cd42adf2ac0790526f7d4f241b4c2c2c6f286ccd9ca4fe949469a`). It names scratch files by their paths inside the
scratch folder (`S/…`) or by bare file name, and the notes file as `N/…`; it holds no full local path. Its "roughly
5 GB of reads" is GR9's figure for the reads ("the reads of about 5 GB").

**In sum:**
- no BUG;
- 15 findings: F1–F10 RISK, F11–F15 NIT;
- its answer on AC power: both, the check refusing on battery, `run` repeating the test before it launches, and the
  window saying AC in words;
- 9 run risks, R1–R9;
- 10 observations, O1–O10;
- its departures: none.

**What came of it.** The step script v2, `gread_steps_v2.sh` (`85dfa911…a023`, 201 lines), built in every finding as
§1 gives it, and went to the coordinating session with its note (`e6d52c71…f446`, 105 lines), which read both whole
and checked them by tool. v2 is the script G-READ-n's run used. The window's words on power are the reviewer's, as
the coordinating session set them at the grant.

## 1. Dispositions

§1 is the dispositions as sent to the coordinating session with v2 (`e898a9d0…dc73`, 60 lines), verbatim but for
their heading and their first paragraph, which the head above gives.

- **F1, run did not repeat check.** Applied: `pre <HEAD>` holds every assertion check makes; `run <HEAD>` calls it and
  launches only when all hold ("FAIL: the check's assertions do not hold; nothing launched"). The window names one
  step to a message. Tested: a stand-in's `run` naming another HEAD launched nothing.
- **F2, run passed with nothing running.** Applied in the reviewer's form: `run` reads the PID's command line at 2 s
  and fails unless it names the run ("no wait; after reads its end").
- **F3, the venv's glob.** Applied: `pre` requires `jl*/.venv/bin` to name exactly one folder holding an executable
  python, by builtins in a subshell, so no argv carries the expansion.
- **F4, after read the run's files before knowing its end.** Applied: `after`'s first test refuses while any process
  names the run, reading nothing of its files.
- **F5, wait's FAIL lines.** Applied: the survivors' branch names their PIDs. A PID that no longer names the run is
  answered by what the table shows: "…and no process does (it has ended): go to after", or, while another process
  names the run (a killed wrapper's re-parented child), those processes' PIDs, to wait on; `after`'s refusal names
  them too. The second case was found by the kill stand-in on v2's first draft, which said "go to after" there; the
  final v2 carries it, and every test below ran on the final bytes.
- **F6, after's re-pins.** Applied: `after <HEAD>` prints "HEAD now" and a NOTE, not a failure, when HEAD moved since
  the check; it pins only what the run read (the driver, LOCK-n.md, the close list, the report, the package and the
  closure's line). The `.gitignore` is no longer pinned by sha256: `pre` requires it committed and clean, admitting
  the artifact and ignoring its `.tmp` (`git check-ignore`), and `after` requires `git status --porcelain --ignored
  -uall -- data/n/gates` (item 3's and Q-F3's exclusions beside it) to be exactly `?? data/n/gates/G-READ-n.json`. On
  this git a narrow include with those exclusions lists what it should (`archive`: 11 with and 11 without them); the
  hazard is `git ls-files`'s. `scripts/` clean is in `pre` alone.
- **F7, the closure.** Applied: `pre` and `after` require `git diff --name-only 0cc301d HEAD -- valence_core` to count
  0 (names never printed) and `valence_core` clean in the working tree.
- **F8 and the AC question.** Applied, both ways: `pre` (so `check` and `run`) refuses unless the power source is AC,
  and refuses Low Power Mode (`pmset -g`'s `powermode` or `lowpowermode` at 1; this Mac shows `powermode 0` and no
  `lowpowermode` line); `check` and `after` print the power source and `pmset -g stats`' sleep and wake counts (counts
  only); `wait` counts the polls off AC and prints the count with "ended". The window's words on power are yours to
  set; the note proposes the reviewer's.
- **F9, a non-empty err and the run's end.** Applied: `after` fails on a non-empty err ("read it first") and prints the
  run's status word without its reason.
- **F10, the test's cover.** Applied: stand-ins made by S/step4b/gread/launch/make_standin_v2.sh from v2's bytes, the
  run's folder moved to a test folder and `./python`'s exec replaced by `/bin/sh -c '…'` (the rest of the argv its $0
  and arguments, so the run's text stays in the argv), with `run` and `wait` as separate calls and the wait as the
  harness's background task:
  - a 45 s job exiting 3, through the real chain (`cd`, the glob, `[[ -x ]]`, TMPDIR, `nice`): `run` returned with the
    job alive; the wait, a separate call, polled it to its end ("ended; polls off AC power: 0"); the exit file read
    EXIT=3;
  - the wrapper's `cd` pointed at the test folder, so the glob matched nothing: zsh's NOMATCH ended the wrapper with
    no out, err or exit file, and `run` failed at its 2 s test;
  - a 90 s job whose wrapper was killed: its `sh` child survived, re-parented, with the run's text in its argv, and
    the caffeinate holder died with the wrapper; `wait` on the wrapper's PID named the child's PID; `after` refused,
    naming it and reading nothing; `wait` on the child polled it to its end; no exit file was written;
  - `run` naming another HEAD launched nothing.
- **F11.** Applied: `clean` requires a blob at HEAD. **F12.** Applied: `wait <PID> [POLL]`, validated. **F13.** Applied:
  the wrapper is `/bin/zsh -f -c`; `pre` requires GR10's five thread variables unset (stricter than printing them,
  since GR10 runs the fits at numpy's defaults), and `check` prints them. **F14.** Applied: `pre` asserts the temp
  folder (so `run` does); `after` asserts it exists and is empty. **F15.** Applied: HEAD may be named short or full
  (`git rev-parse --verify <name>^{commit}`); the usage line says so.
- **R1–R9.** Noted. R3: if the session's background task dies, the wait is re-entered as `wait <PID>`. R6: the launch
  files and pkgsha.sh are touched by explicit path before the window (the scratch cleanup's four days). R7: the out and
  err are read whole and screened before any commit. R8: the window is sized at about 3 h.
- **O5.** No `-u`: G-ANL-n's form is kept, and a killed run's last lines may be lost. **O8.** `pythons` stays strict,
  by name, with no allowance for a process beside the run (Q-F3 has ended). **O10.** The v1 note overstated `after`:
  it sees only the end state; nothing watches for Python between `run` and `after`. The others: noted.

## 2. The report as returned

BLIND REVIEW: G-READ-n launch steps, S/step4b/gread/launch/gread_steps_v1.sh

I checked every file the brief names with `shasum -a 256` before reading it. All matched: the brief, gread_steps_v1.sh, S/step4b/schema/pkgsha.sh, test_steps_v1.sh, S/step4b/gread/spec/gr_readings_v1.md and N/2026-11-25_n-build_gread-launch-files.md. HEAD is 0cc301d. scripts/n_sessions.py is clean at HEAD (rev-parse blob equals hash-object) and at 35c4c73e…4808 (the brief's value).

Overall: the happy path is sound. The zsh -c quoting is right: bash expands the paths, zsh receives the glob and `$?` literally, and no guard marker reaches any argv. The wait's PID-plus-command-line test defeats PID reuse. The `sed` in `after` matches the driver's print. Every defect I found sits on an edge or is a missing check. I found no BUG.

== FINDINGS ==

F1. RISK. Lines 83–86. `run` re-checks only the run's folder and the process table.
- What is wrong: it does not repeat check's HEAD, inputs, gates folder, Python-process or power checks. So `run` launches after a failed `check`, without any `check`, or after the state changed between the two calls (they are separate calls).
- The driver's own refusals cover the driver, LOCK, package, closure, close list, report and artifact. They do not cover HEAD against the grant, the .gitignore, extra names in data/n/gates, Python processes beside the run, or power.
- "Twice": a second sequential `run` is refused, because the zsh creates out.txt and err.txt within milliseconds and `running` > 0. The guard is check-then-act, though: two `run` calls sent in one message could both pass it.
- Fix:
  - Move check's assertions into a function `pre <HEAD>`, called by `check` and by `run <HEAD>`.
  - `run` launches only when F=0: `[ "$F" = 0 ] || { echo "FAIL: the check's assertions do not hold; nothing launched"; exit 1; }`.
  - The window states one step per message.

F2. RISK. Lines 88–92. `run` exits 0 and prints a PID even when nothing is running at 2 s.
- If nohup or caffeinate failed, the glob failed (F3), or the driver refused fast, `ps` prints nothing. The output is then "its command line: " (empty), with exit 0.
- Fix:
  ```
  c=$(ps -p "$P" -o command=)
  echo "its command line: $(printf '%s' "$c" | sed -e "s#$R#<run>#g" -e "s#$REPO#<repo>#g")"
  printf '%s' "$c" | /usr/bin/grep -q '[n]_sessions\.py gread' || { echo "FAIL: PID $P does not name the run at 2 s (ended or never started): no wait; after reads its end"; exit 1; }
  echo "run PASS"
  ```

F3. RISK. Line 87, `cd jl*/.venv/bin`. The glob's failure modes are untested and leave no trace.
- No match: zsh's default NOMATCH makes this an error that ends the whole -c string. No out, err or exit file is written, and zsh's message goes to /dev/null. `after` then says only "no exit file".
- Two matches: cd takes zsh's two-argument `cd OLD NEW` form and fails, giving EXIT=1 with no out or err file.
- Fix, in `pre` (builtins only, so no argv carries the expansion):
  ```
  ( set -- jl*/.venv/bin; [ $# = 1 ] && [ -d "$1" ] && [ -x "$1/python" ] ) || fail "jl*/.venv/bin is not exactly one folder with an executable python"
  ```

F4. RISK. Lines 105–127: `after` reads the run's files before it knows the run has ended.
- It stats and reads exit.txt (106–108). It tests `running` only at 112, and does not stop there. It then stats and reads out.txt (118–119) and counts out and err lines (125–127).
- After a failed `wait` with a survivor, running `after` reads a live invocation's raw, which breaches item 5.
- Fix: make this the first line of `after)`:
  ```
  [ "$(running)" = 0 ] || { echo "FAIL: a process names the run: the invocation has not ended; nothing of its files read"; echo "after FAIL"; exit 1; }
  ```

F5. RISK. Lines 96 and 100–101: `wait`'s FAIL lines.
- The survivor branch prints a count only. Re-entering the end-wait needs a PID: the script supports `wait <PID>` on any process whose argv holds the pattern, but does not print one.
- If the run ended before `wait` starts (a fast refusal), line 96 says "is not the run", which misleads.
- Fix:
  - On survivors, print `$(pgrep -f '[n]_sessions\.py gread' | tr '\n' ' ')` (PIDs only).
  - Reword 96 as "PID $P does not name the run (ended already, or another process): go to after".

F6. RISK. Line 115 (`inputs` reused by `after`) and line 116. `after` re-pins shared files the run never reads after it starts, and never shows HEAD.
- Two things can fail a good run:
  - another track committing an admit line to `.gitignore` (whole-file sha256 pin, line 29/41);
  - any edit under scripts/ during the 2.7 h (line 52).
- The running code is already in memory, and every import happens in `_gread_prepare`.
- The same `.gitignore` pin forces a v2 of the launch files if any track touches `.gitignore` before the window.
- Fix:
  - `after <HEAD>` prints "HEAD now …" and flags a difference from check's HEAD.
  - In `after`, pin only what the run read: driver, LOCK, close list, report, package, and F7's closure line.
  - Test the admit the way the record commit needs it, in G-ANL-n's form: `git status --porcelain --ignored -uall -- data/n/gates ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/m[f]3/**'` equals exactly `?? data/n/gates/G-READ-n.json`.

F7. RISK. Lines 50–52. `check` holds the package by digest but not its closure.
- The closure is valence_core/echo/probe.py, discrim.py, extract.py, m/resume.py, m/keys.py, adapters/base.py and the HF adapter module.
- A committed change to a closure file passes `check` (it is clean at the new HEAD). The driver then refuses at its start (n_sessions.py:7985–7988), and its REFUSED line names the differing closure files. One of those paths holds a guard marker, which would put a marker word into the out raw.
- Fix: `[ "$(git diff --name-only 0cc301d HEAD -- valence_core | /usr/bin/grep -c .)" = 0 ] || fail "valence_core changed since the BUILD: the closure may not be the lock's"`. Print a count, never the names.

F8. RISK. Line 80. The power source is printed but not required. See THE AC QUESTION.

F9. RISK (low). Lines 118–127. `after` passes with a non-empty err file and never says how the run ended.
- G-ANL-n's record had stderr at 0 bytes. An err line means a traceback or a library message, which is where a local root or the venv's path can enter a raw.
- Fix:
  - Add `[ "$(/usr/bin/grep -c '' "$R/err.txt")" = 0 ] || fail "the err file is not empty: read it first"`.
  - Print the status word without its reason: `echo "status: $(/usr/bin/grep -E '^G-READ-n (COMPLETE|REFUSED|FAILED):' "$R/out.txt" | tail -n 1 | cut -d: -f1)"`.

F10. RISK. S/step4b/gread/launch/test_steps_v1.sh: the stand-in's cover.
- What it shows on this macOS:
  - `$!` is the zsh -c under nohup caffeinate;
  - the wait matches its argv and ends;
  - `running` is 0 within a 1 s poll, so the caffeinate holder is gone;
  - the redirections and exit file work.
- What it cannot show:
  - It replaces the whole chain (cd, glob, `[[ -x ]]`, TMPDIR, nice, ./python) with `sleep 6; :` joined by `;`. So the real line never ran, and EXIT can only be 0: the capture of a non-zero status through `&&` is untested.
  - Its `run` and `wait` ran inside one harness call, so it cannot show the `run` call returning while the job lives on. Earlier `nohup caffeinate … & disown` launches did show that.
  - No kill, no survivor, no long poll.
  - No `after` PASS path. That cannot be exercised without the repository's artifact path, so the sed-against-print match rests on n_sessions.py:8170 (O3).
- Fix: three more stand-ins, with `run` and `wait` as separate calls and the wait in the background:
  1. Keep the real line and replace only `./python` with `/bin/sh -c 'sleep 6; exit 3'`. The rest of the argv becomes sh's $0 and arguments, so "n_sessions.py gread" stays in zsh's argv. Expect EXIT=3.
  2. Point the copy's `cd $REPO` at the test folder, so `jl*` matches nothing. Expect no exit file (my reading).
  3. Kill the stand-in's zsh wrapper while its child sleeps. This exercises F5's survivor branch.

F11. NIT. Line 38. `clean()` passes when the path is absent both at HEAD and on disk (empty string equals empty string). Today the `-f` tests after each call cover this. Fix: `a=$(git rev-parse "HEAD:$1" 2>/dev/null); [ -n "$a" ] && [ "$a" = "$(git hash-object -- "$1" 2>/dev/null)" ]`.

F12. NIT. Lines 34 and 98. POLL comes from the environment unvalidated. A non-numeric value makes `sleep` fail at once, and the loop then spins ps and grep beside the run for 2.7 h. Fix: `case $POLL in ''|*[!0-9]*|0) echo "FAIL: POLL"; exit 1;; esac`, or take the test's 1 s as `wait <PID> [POLL]`.

F13. NIT. Line 87. `/bin/zsh -c` sources /etc/zshenv and ~/.zshenv before the command.
- Anything those files set reaches the run: a thread variable, the PATH used to find `nice`, an option such as NOCLOBBER or CDPATH. `check` saw bash's environment, not the wrapper's.
- Fix:
  - Use `/bin/zsh -f -c` (the stand-in's replacement text is unaffected).
  - Have `check` print GR10's five variables (OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS, VECLIB_MAXIMUM_THREADS, NUMEXPR_NUM_THREADS) as set or unset, so a set one is seen before the 2.7 h rather than after.

F14. NIT. Lines 84 and 114.
- `run` does not re-check `[ -d "$R/tmp" ] && [ ! -L "$R/tmp" ]`.
- `after`'s empty-tmp test passes when tmp is missing, because the `ls` error is suppressed and the result is empty.
- Fix: assert `-d` in both.

F15. NIT. Lines 71–72. `check` needs the full 40-hex HEAD; a grant written as 0cc301d fails on HEAD. Say so in the usage line and in the window.

== THE AC QUESTION ==

Answer: both. The check should refuse on battery, `run` should repeat that test immediately before launching, and the window should state AC in words.

Reasons:
1. `-s` is void on battery ("valid only when system is running on AC power", man caffeinate). On battery `-i` blocks idle sleep only; a closed lid, a low battery, a thermal emergency or a manual Sleep still sleeps the Mac.
2. Battery life. The run keeps numpy's default threads busy for about 2.7 h (GR9), with roughly 5 GB of reads on top. A laptop battery at sustained multi-core load is unlikely to last that long. At low battery macOS sleeps or hibernates whatever the assertions say.
   - The process then pauses until power returns. After a shutdown or restart it is lost: GR9 allows no resume, so the whole window repeats.
3. Low Power Mode, commonly set for battery only, throttles the CPU. That lengthens the run, deepens the drain, and inflates the per-stage ms that the entry reports as times.
4. A condition that is printed but not required is easy to miss in a passing check. Refusing costs one plug; a battery start risks a stall or a 2.7 h repeat. A pause does not change the fits (they are deterministic and the process only pauses), so the refusal protects completion and the recorded times, not the artifact's numbers.
5. The window's own words are still needed. The check sees only the start; AC can be lost mid-run; and the lid, manual sleep and updates are human acts.

Script text. In `check`, in place of line 80:
```
pw=$(pmset -g batt | head -n 1)
echo "power: $pw"
case "$pw" in *"'AC Power'"*) ;; *) fail "not on AC power: caffeinate -s holds the system awake only on AC";; esac
```

In `run`, before line 87:
```
pmset -g batt | head -n 1 | /usr/bin/grep -q "'AC Power'" || { echo "FAIL: not on AC power; nothing launched"; exit 1; }
```

In `after`: print check's power line again.

Optional, count-only (check and after outputs are committed raws, which carry no times):
- `check` and `after` each print `pmset -g stats` ("counts for number sleeps and wakes … since boot", per man pmset). Equal counts mean no sleep in between.
- `check` prints the `lowpowermode` line of `pmset -g`, and fails on 1.
- The wait counts polls whose `pmset -g batt` first line is not AC, and prints that count with "ended". That reads the power source, not the run.

pmset is barred to me, so read both output forms once before wiring them in. Do not commit `pmset -g batt` beyond its first line, or `-g sched` / `-g log`: they print times.

Window text: "Power: the laptop on AC from `check` to `after`. The lid open. Low Power Mode off. No sleep, restart, log-out or software update by hand until the end notice, and none scheduled. Nothing heavy beside it. A pause changes the run's times, not its fits: if `after` shows another power source or sleep count than `check`, the entry says so beside the times."

On the coordinator's term "battery window": it collides with battery power, so the window should say "on AC power" in those words.

Other sleep, lid and display points:
- The display: `-d` is not needed. Display sleep and screen lock do not pause the process.
- The lid on AC: as I recall Apple's IOKit description, PreventSystemSleep prefers dark wake to sleep, but I could not check that here. Keep the lid open regardless; a closed MacBook under sustained load also runs hotter and may throttle.
- A dead wrapper: the caffeinate holder exits with the wrapper, which releases the assertion while the python may still be running (R4).

== RUN RISKS ==

R1. Power and sleep, as above: AC lost mid-run, a closed lid on battery, low-battery sleep, Low Power Mode. None of this is visible in the out raw beyond inflated ms.

R2. A restart, log-out or shutdown (a macOS update, a scheduled power event, a person) kills the run. There is no resume: the run repeats whole. `after` shows "no exit file" and possibly a truncated out (F-related O5).

R3. The app and the harness.
- The `wait` background task dies with the session; re-enter it with `wait <PID>`.
- The run stays in the `run` call's process group, because non-interactive bash without `set -m` gives a job no group of its own. Whether quitting the app kills that group is not shown by this test. Earlier launches with this pattern survived their launching calls.

R4. If the zsh wrapper is killed:
- the python is re-parented and keeps running without the sleep assertion;
- no exit file is written;
- `wait` FAILs with a count (F5);
- python still writes out.txt and possibly the artifact.

R5. A second session during the run.
- A Python or model process beside it slows the fits and inflates the times. `after` catches only a process alive at its own moment; nothing watches in between.
- A commit, pull or checkout leaves the artifact unaffected (the code is in memory), but moves HEAD unrecorded and fails `after`'s re-pins (F6).
- Finder opening data/n/gates or the run's tmp drops `.DS_Store`, which fails `after`'s name checks.
- Anything touching the staging folder makes the run refuse at a cell's second read. That fails closed, but loses the hours spent.

R6. The scratch midnight cleanup (files about 4 days old by mtime).
- pkgsha.sh was rewritten on 2026-11-24 and the launch files date from 2026-11-25, so they age out from about 2026-11-28/29.
- A run straddling that midnight can fail `after` (pkgsha.sh missing), or lose the empty tmp folder unnoticed (F14).
- Before the window, touch the launch files by explicit path.

R7. What can carry unwanted text into the raws (screen before commit, as planned):
- out, warnings line (n_sessions.py:8204, 8216): `simplefilter("always")` surfaces ResourceWarning, whose message names a file by absolute path. The 160-character cut is long enough to hold the root.
- out, closure-mismatch REFUSED line (F7): a guard-marker word.
- err: any traceback, objc message or native-library message, which would carry the venv's path (two markers) and the root.
- check and after outputs: a bash error line (for example a missing file) carries the script's scratch path, which names the home folder in dashed form.
- Margins and per-session values: I found no path for either in the gread code (results print aggregates only; refusals print names, record indices, layers, field paths or types).

R8. Time.
- GR9's projection was measured beside Q-F3's campaign and declared high.
- The reads come on top: every listed file is hashed, and every cell is read again (at least twice for the cells probed).
- The poll adds up to 600 s.
- nice 19 yields to any foreground load, and a closed lid adds thermal throttling.
- Size the window at about 3 h.

R9. While the run lives, `running` counts three processes: wrapper, python, and the caffeinate holder, whose argv holds the same -c string. A holder outliving the wrapper by more than a poll would fail `wait` falsely. The stand-in saw it gone within 1 s, so this is negligible at 600 s.

== OBSERVATIONS ==

O1. Pins, checked by digest.
- LOCK-n.md, the close list and `.gitignore` are each clean at HEAD and equal to lines 27–29.
- The driver's LOCK_SHA256 (n_sessions.py:3954) and LOCK_PACKAGE_SHA256 (3963) equal LOCK_SHA and PKG.
- The close list's first line is "<64 hex>  data/n/reports/campaign.json", as line 46 expects.
- I did not run pkgsha.sh (barred), and I did not look at S/step4b/gread/run.

O2. pkgsha.sh against valence_core/m/resume.py:328–350.
- It produces the same stream for plain names: path, byte count, then bytes, sorted in C order.
- It differs on a dot-named *.py file (pathlib's glob includes it; `ls` without -A does not) and on names with whitespace.
- Either difference fails closed, and the driver re-measures in process (7984–7990).

O3. The driver prints exactly what line 119 extracts (8170): "the artifact data/n/gates/G-READ-n.json (n-gread-v1), sha256 <hex>: written once, read back; …". The printed sha256 is of the text written, which equals the file's bytes (text mode, "\n" on macOS), so line 120 compares like with like.

O4. Paths the driver prints, and how it calls git.
- `--staging` is resolved against REPO, not the cwd (7968), and printed relative (7975).
- Other printed paths go through `_shown` and are repo-relative (1428–1431).
- git runs with `-C REPO` (855, 2897), so the venv-bin cwd is harmless.
- The HF adapter imports torch only inside its constructor, so the run stays numpy-only.
- n/probe.py and echo/probe.py use numpy alone: no joblib, no child Python processes, and TMPDIR is unused.

O5. Exit codes and what each end leaves.
- 0 only once the artifact is written and read back.
- 1 for both REFUSED and FAILED (8207–8212), so EXIT=1 does not say which (F9).
- 2 for an argparse error (usage goes to err).
- 128+N for a signal.
- No exit file if the wrapper dies or the glob fails.
- A kill between the write and the rename leaves `G-READ-n.json.tmp` in data/n/gates (7888). `after`'s names check catches it, and the next run refuses (7964–7967).
- stdout to a file is block-buffered, so a killed run can lose its last lines. `-u` would keep them, at the cost of departing from G-ANL-n's form; PYTHONUNBUFFERED is ignored under -I.

O6. Signals.
- SIGHUP is ignored (nohup).
- SIGINT and SIGQUIT are ignored: bash sets them so for a background job without job control, and Python then installs no KeyboardInterrupt handler.
- SIGTERM and SIGKILL are unshielded.
- stdin is /dev/null. nohup writes no nohup.out because stdout is not a terminal.

O7. man caffeinate (its 2012 text) says the utility runs in a forked child; the observed and re-tested behaviour is the reverse. The wait works either way, since both processes carry the pattern.

O8. pgrep excludes itself and all its ancestors by default (man pgrep, -a).
- `pythons` matches by name, case-insensitively, so it also catches a framework "Python".
- That deliberately departs from G-ANL-n's `pgrep -f '[p]ython'` and is stricter than GR14's "listed": it has no allowance for a declared process beside the run.

O9. The wait's final `pgrep -f` reads the process table after the PID has ended, not any file, which fits item 5.

O10. The note's "nothing else should run Python while it runs (step 4 fails on any process named python)" overstates the check: step 4 sees only the end state.

== DEPARTURES ==

None. My commands were:
- `shasum -a 256` of the six named files and of LOCK-n.md, .gitignore, the close list and the driver;
- `git rev-parse` and `git hash-object` on those named non-data files;
- `/usr/bin/grep` and `sed -n` over named files, with marker patterns bracketed;
- `head` and `cut` of the close list's first line;
- `man caffeinate`, `man pmset`, `man nohup` and `man pgrep` through `col -b`, grep, sed and head. I did not inspect what `man` runs inside itself.

File-tool reads: the named S and N files; RESULTS.md's G-ANL-n entry and its gread-bench lines; the driver's gread code and helpers; valence_core/n/guard.py; resume.py:322–355; and the head of the HF adapter module (its path holds a marker, so I read it by the file tool only). Nothing ran on a model. I wrote no file and ran no interpreter, pmset, ps, pgrep, caffeinate or nohup.

