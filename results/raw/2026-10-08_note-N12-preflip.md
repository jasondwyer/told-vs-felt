# AUDIT-note-release v1.2 -- N12 pre-flip reads (server refs, GitHub-side surfaces, interim history scan)

- Code stamp (`date -u`): Fri Oct  9 05:06:59 UTC 2026
- HEAD at start `6485da2765be7a37d60a1e199c874e4744fd7a78`; at the end `6485da2765be7a37d60a1e199c874e4744fd7a78`; refs moved during the run: no.
- Block: `AUDIT-note-release-v1_2.md`, sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841` (working tree) / `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841` (HEAD blob); routed `8cd8a9ac...3841`: MATCH.
- Item: N12, the scrub index's pre-flip checklist (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:173-183`), items 1 and 2, and an interim run of item 3's history script. Compared against the committed history raw and JSON at `6485da2` (`6485da2765be7a37d60a1e199c874e4744fd7a78`), whose scan read `cf8eb5b9dd`.
- Script: `scripts/audit_note_N12_preflip.py`, sha256 `9a4a5cbe85c761df9e6262cd34b36959914472b2e94b606ac68f4b0f86074a5f`. Interpreter: `jlens-qwen36/.venv/bin/python` (Python 3.12.9); git version 2.39.5 (Apple Git-154); gh version 2.96.0 (2026-07-02). Command: `jlens-qwen36/.venv/bin/python scripts/audit_note_N12_preflip.py --history-dir <a directory outside the repository>` (from the repository root).
- Read-only: `git ls-remote` (origin and the wiki repository), `rev-parse`, `for-each-ref`, `cat-file`, `merge-base --is-ancestor`, `rev-list`, `log`, `show`, `diff-tree`, `ls-tree`, `remote get-url`; `gh` read queries only (`repo view`, `pr list`, `issue list`, `release list`, `run list`, `api` GETs, two GraphQL queries). Nothing fetched, staged, committed, pushed or tagged; no setting changed; nothing downloaded or installed; no git command inside `jlens-qwen36/`. The remote-tracking reflogs are read as plain files (their name and email fields are never read out). Network: GitHub only, through `git` and `gh`.
- Writes: this file and its JSON. The history script, run unchanged (twice as a subprocess, once in-process to read its full leak list; section 3), wrote (or would have written) only into session scratch outside the repository (the path is not printed: it is of the local-temp-path class). For the in-process run the process's argument list and environment are set to the routed run's (apart from the hash seed, which a running process cannot change; the list it yields is sorted here) and restored afterwards.
- Redaction: no RunPod id or name, IP address, SSH port, key name, credential, the LoRA phrase, the session link, the laptop hostname, an email address or a non-owner login appears in this file or its JSON. The history raw's 18 known sensitive values were resolved in memory (17 resolved, 1 unresolved: the class SSH signing-key fingerprint, which the history raw says is not verbatim in history) and the dumped values held in memory; the script refuses to write if any of them, or any guard shape, occurs in an output. Redacted forms use the history raw's notation `xxxx...[len N]#hhhhhhhh` (the routing's first 4 + length + sha256 prefix; `lenN:hhhhhhhh` where a value has 4 characters or fewer or opens with 4 digits). Class names are printed by their short label (several long labels contain strings the scan reports as values).

## 1. Server-side refs (`git ls-remote --symref origin`)

Origin: `https://github.com/jasondwyer/jspace-lab.git` (userinfo in the URL: no). ls-remote returned 5 refs (1 peeled tag line(s) besides) in 0.42 s. HEAD is a symref to `refs/heads/main`.

Compared with the history raw's refs table (`results/raw/2026-10-08_note-N12-history.md@6485da2:21-27`, the local refs at its scan of `cf8eb5b9dd`) and with the local refs now:

| server ref | object | object local | local counterpart(s), equal | in the history raw's table (object there; equal now) | ancestor of origin/main |
|---|---|---|---|---|---|
| `HEAD` | `6485da2765` | yes | none | - | n/a (symref) |
| `refs/heads/claude/handoff-doc-next-steps-oeccd1` | `79868f7583` | yes | `refs/remotes/origin/claude/handoff-doc-next-steps-oeccd1` yes | `refs/remotes/origin/claude/handoff-doc-next-steps-oeccd1` (`79868f7583`; yes) | yes |
| `refs/heads/main` | `6485da2765` | yes | `refs/heads/main` yes, `refs/remotes/origin/main` yes | `refs/heads/main` (`cf8eb5b9dd`; no -- moved), `refs/remotes/origin/main` (`cf8eb5b9dd`; no -- moved) | yes |
| `refs/tags/cycle-2-close` | `f597ea7961` | yes | `refs/tags/cycle-2-close` yes | `refs/tags/cycle-2-close` (`f597ea7961`; yes) | yes |
| `refs/tags/cycle-4-close` | `2390272650` (peels to `50906bfef7`) | yes | `refs/tags/cycle-4-close` yes | `refs/tags/cycle-4-close` (`2390272650`; yes) | yes |

- Server refs with no local counterpart: 0. Server objects not in the local object store: 0. `refs/pull/*`: 0. Refs outside heads/tags/pull: 0. Local refs with no server ref: 0.
- Peeled tag objects equal the local peel: True (1 tag(s)).
- Since the history raw's table: `refs/heads/main` `cf8eb5b9dd` -> `6485da2765`; `refs/remotes/origin/main` `cf8eb5b9dd` -> `6485da2765`. The commits that `main` gained (2: `09c3a8cc54`, `6485da2765`) are outside that scan; section 3 covers them.
- So every server-side ref is local, equal to its local counterpart and an ancestor of origin/main, and the server holds no ref the history raw did not scan apart from `main`'s new tip: yes.

## 2. GitHub-side surfaces (read-only `gh`)

Repository `jasondwyer/jspace-lab`: visibility **PRIVATE** (isPrivate True); default branch `main`; licenseInfo none; wiki enabled False; issues enabled True; projects enabled True; discussions enabled False. REST: has_pages False, has_downloads False, allow_forking True, forks 0 (network 0), archived False, open issues 0.

| surface | query (read-only) | rc | result |
|---|---|---|---|
| pull requests | `gh pr list -R jasondwyer/jspace-lab --state all --limit 1000 --json number,state,title,author,createdAt,headRefName` | 0 | 0 (by state {}; authors {}) |
| issues | `gh issue list -R jasondwyer/jspace-lab --state all --limit 1000 --json number,state,title,author,createdAt` | 0 | 0 (by state {}) |
| issue and PR comments | `gh api --paginate --slurp repos/jasondwyer/jspace-lab/issues/comments?per_page=100` | 0 | 0 |
| PR review comments | `gh api --paginate --slurp repos/jasondwyer/jspace-lab/pulls/comments?per_page=100` | 0 | 0 |
| commit comments | `gh api --paginate --slurp repos/jasondwyer/jspace-lab/comments?per_page=100` | 0 | 0 |
| releases | `gh release list -R jasondwyer/jspace-lab --limit 1000 --json tagName,name,isDraft,isPrerelease,publishedAt` | 0 | 0 (assets 0) |
| Actions runs | `gh run list -R jasondwyer/jspace-lab --limit 200 --json databaseId,status,conclusion,event,workflowName,createdAt,headBranch,displayTitle` | 0 | 0 (by status {}) |
| Actions workflows | `gh api repos/jasondwyer/jspace-lab/actions/workflows` | 0 | 0 (`.github/` files at HEAD: 0) |
| Actions artifacts | `gh api repos/jasondwyer/jspace-lab/actions/artifacts?per_page=100` | 0 | 0 (names: 0; nothing downloaded) |
| wiki repository | `git ls-remote https://github.com/jasondwyer/jspace-lab.wiki.git` | 128 | refs 0; not found (no wiki repository); hasWikiEnabled False |
| GitHub Pages | `gh api repos/jasondwyer/jspace-lab/pages` | 1 | HTTP 404 = no Pages site |
| deploy keys | `gh api repos/jasondwyer/jspace-lab/keys` | 0 | count 0 (readable) |
| webhooks | `gh api repos/jasondwyer/jspace-lab/hooks` | 0 | count 0 (readable) |
| milestones | `gh api --paginate --slurp repos/jasondwyer/jspace-lab/milestones?state=all&per_page=100` | 0 | 0 |
| discussions / deployments / environments | `gh api graphql -f query=query{repository(owner:"jasondwyer",name:"jspace-lab"){discussions(first:1){totalCount} deployments(first:1){totalCount} environments(first:1){totalCount}}}` | 0 | 0 / 0 / 0 |
| projects (v2) linked to the repository | `gh api graphql -f query=query{repository(owner:"jasondwyer",name:"jspace-lab"){projectsV2(first:1){totalCount}}}` | 1 | not readable: INSUFFICIENT_SCOPES (the CLI's credentials lack the project-read scope) |
| repository activity (Code's addition) | `gh api --paginate --slurp repos/jasondwyer/jspace-lab/activity?per_page=100` | 0 | 259 records, 2026-07-18T04:17:06Z to 2026-10-08T15:49:52Z; by type {'push': 257, 'branch_creation': 2}; actors {'owner': 259} |

Every query above is a read: the REST calls are GETs (no method flag, no fields) and the two GraphQL calls POST a query, which reads, as GraphQL requires. None was refused apart from the projects (v2) read, whose error is an answer: the PI can read the repository's Projects tab on the web.

**Force-pushed-away commits (pre-flip step 2's last clause).** The activity record lists 0 force push(es) and 0 branch deletion(s). Its 257 pushes: both endpoints local 257, fast-forward by `merge-base --is-ancestor` 257, not fast-forward 0; every recorded `after` object local: yes; reachable from its ref's current server tip: 259 of 259 checked. Its earliest record (2026-07-18T04:17:06Z) and the first push in this clone's reflog as the history raw records it (2026-07-18 00:17:06 -0400) are the same instant: yes.

| ref | activity records | distinct `after` values | of them in this clone's remote-tracking reflog | not in it | reflog entries (kinds) | reflog values not in the activity record |
|---|---|---|---|---|---|---|
| `refs/heads/claude/handoff-doc-next-steps-oeccd1` | 7 | 7 | 4 | 3 | 4 (fetch origin 3, pull --rebase 1) | 0 |
| `refs/heads/main` | 252 | 252 | 252 | 0 | 252 (update by push 252) | 0 |

A push this clone did not make shows as an `after` value missing from its reflog (column five); the counts above say whether such objects are local and reachable from the current server tips. The activity record is GitHub's; how far back GitHub keeps it is not stated in anything this run read, so the conclusion is bounded by that record: on what GitHub returns, nothing was force-pushed away or deleted.

**Screen of the text these surfaces carry** (the history script's precise patterns and identifier shapes, the scrub index's guard shapes, email addresses other than the service address and the commit identities', and the 17 resolved known values): texts screened activity ref 259, server ref name 5; hits 0. Logins other than the repository owner's on any item read: 0. With no pull request, issue, comment, release, run, artifact or milestone on the server, the screen had only ref names to read.

## 3. Interim history scan at HEAD

**(a) The routed run.** `PYTHONHASHSEED=0 jlens-qwen36/.venv/bin/python scripts/audit_note_N12_history.py --out <history-dir>/history_now.md --json-out <history-dir>/history_now.json` exited 1 after 130.8 s (HEAD `6485da2765` before and `6485da2765` after). md written: no; JSON written: no. **It refused to write**: its leak assertion found 19 entries, one per value it redacts as sensitive and output (md or JSON) in which that value appears verbatim, so a value found in both outputs counts twice. Its message prints only the first 10 entries (`leaks[:10]`), in the iteration order of a Python set, which depends on the hash seed; this run pins PYTHONHASHSEED=0 for the routed run, so the sample is reproducible, but it is a partial sample (7 distinct value(s)): `/tmp...[len 6]#fc22e2de` (md), `runp...[len 9]#3124edae` (md), `runp...[len 9]#3124edae` (json), `<fil...[len 8]#c17d7b45` (md), `~/.c...[len 43]#1a4fb901` (md), `~/.c...[len 43]#1a4fb901` (json), `runp...[len 10]#421bbde9` (md), `runp...[len 10]#421bbde9` (json), `id_r...[len 6]#f40883a1` (md), `0.0....[len 7]#19e36255` (md).

**The full list.** The same unchanged script run in-process with the routed arguments; its SystemExit caught and its own `leaks` list (one entry per value and output) read from its frame: refused after 132.7 s (HEAD unchanged across it: yes); 19 entries (equal to the routed run's count: yes), 12 distinct values; the routed run's printed sample is contained in it: yes. Values are held in memory and shown by form, sorted:

| form | output(s) | dump table(s) | script's verdict | Code's verdict (new values of (c)) | first commit | in the routed sample | verbatim in the audit's own committed text |
|---|---|---|---|---|---|---|---|
| `/tmp...[len 6]#fc22e2de` | md | local_temp_path | LOCAL-PATH | LOCAL-PATH | `09c3a8cc` | yes | yes |
| `0.0....[len 7]#19e36255` | json, md | ipv4_address | FALSE-POSITIVE | FALSE-POSITIVE | `09c3a8cc` | yes | yes |
| `<fil...[len 7]#1aedc48e` | json, md | ssh_identity_flag | UNTRIAGED | FALSE-POSITIVE | `09c3a8cc` | no | yes |
| `<fil...[len 8]#c17d7b45` | md | ssh_identity_flag | UNTRIAGED | FALSE-POSITIVE | `09c3a8cc` | yes | yes |
| `<fil...[len 9]#13dfbe0e` | json | ssh_identity_flag | UNTRIAGED | FALSE-POSITIVE | `09c3a8cc` | no | yes |
| `A-Za...[len 9]#fab79a8e` | json, md | passphrase_shaped | UNTRIAGED | FALSE-POSITIVE | `09c3a8cc` | no | yes |
| `id_e...[len 10]#8e5d92fd` | md | ssh_key_name | UNTRIAGED | FALSE-POSITIVE | `09c3a8cc` | no | yes |
| `id_r...[len 6]#f40883a1` | md | ssh_key_name | UNTRIAGED | FALSE-POSITIVE | `09c3a8cc` | yes | yes |
| `runp...[len 10]#421bbde9` | json, md | runpod_hostname | UNTRIAGED | FALSE-POSITIVE | `09c3a8cc` | yes | yes |
| `runp...[len 9]#3124edae` | json, md | runpod_hostname | UNTRIAGED | PUBLIC | `09c3a8cc` | yes | yes |
| `~/.c...[len 22]#a83bf7e9` | json, md | claude_projects_path | LOCAL-PATH | LOCAL-PATH | `09c3a8cc` | no | yes |
| `~/.c...[len 43]#1a4fb901` | json, md | claude_projects_path | LOCAL-PATH | LOCAL-PATH | `09c3a8cc` | yes | yes |

'The audit's own committed text' is the history script at HEAD plus its committed raw and JSON at `6485da2`, matched word-bounded as the leak assertion matches. Of the 12 distinct values, 12 occur there (class labels, pattern text, triage reasons, prose); first seen: `09c3a8cc` 12. The script prints values only in redacted form, so a verbatim occurrence in its output is text it writes itself -- text that the audit's committed files now carry, so its scan reports it as values. The committed script therefore cannot write at this HEAD; pre-flip step 3 needs a clean write at the release commit, which needs a change to that committed audit script (triage entries marking these values non-sensitive, or labels printed without them): the PI's or the design seat's call, not made here.

**(b) The dump run** (the same script, unchanged, in its documented `--dump-untriaged --dump-all` mode, which prints every value of every table to stdout and writes no file): exit 0 after 130.4 s, 'DUMP ONLY' line present: yes; 779 value rows and 128 untriaged credential-shaped fallback rows parsed, 0 other line(s); files written by it: 0. HEAD scanned: `6485da2765be7a37d60a1e199c874e4744fd7a78` (unchanged across the run: yes). The dump does not print the header-identifier and binary-identifier tables; the window's commit headers are read directly in (f).

Window: the commits after the block's commit `bbc9ffe72f` -- 5 on HEAD (`c75d4d8aa3`, `bab921ce52`, `cf8eb5b9dd`, `09c3a8cc54`, `6485da2765`; 5 from all refs). The routing says both 'the commits after `bab921c`' and 'c75d4d8..HEAD'; in git's notation c75d4d8..HEAD leaves out `c75d4d8` itself, so this file reports every commit after `bbc9ffe` one by one and either reading can be taken from the per-commit columns. The committed JSON's scan already covered `cf8eb5b9dd` and its ancestors; the commits it did not see: `09c3a8cc54`, `6485da2765`.

**(c) Value tables, HEAD against the committed JSON** (`results/raw/2026-10-08_note-N12-history.json@6485da2`; tables keyed by the value's sha256 prefix, so the committed redacted forms and the dumped values compare exactly). New values: 425; values in the committed JSON missing now: 0.

| table | committed | now | new |
|---|---|---|---|
| claude_projects_path | 4 | 8 | 4 |
| context_free | 123 | 163 | 40 |
| dot_local_hostname | 0 | 1 | 1 |
| email_address | 1 | 2 | 1 |
| high_entropy | 49 | 280 | 231 |
| ipv4_address | 2 | 3 | 1 |
| local_temp_path | 88 | 113 | 25 |
| passphrase_shaped | 1 | 2 | 1 |
| precise:generic_assignment | 1 | 2 | 1 |
| precise:quoted_secretish_assignment | 41 | 140 | 99 |
| proxy_hostname | 0 | 1 | 1 |
| runpod_hostname | 0 | 7 | 7 |
| ssh_identity_flag | 0 | 5 | 5 |
| ssh_key_name | 0 | 2 | 2 |
| ssh_key_path | 3 | 4 | 1 |
| url_host | 9 | 14 | 5 |

Tables with no change: 8 of 24 non-empty. New values by the commit of their first occurrence: `09c3a8cc` 419, `6485da27` 6.

New values by table and verdict (the history script's verdict, or Code's where the script left the value UNTRIAGED):

| table | verdict | first commit | n |
|---|---|---|---|
| claude_projects_path | LOCAL-PATH | `09c3a8cc` | 4 |
| context_free | FALSE-POSITIVE | `09c3a8cc` | 34 |
| context_free | FALSE-POSITIVE | `6485da27` | 1 |
| context_free | LOCAL-PATH | `09c3a8cc` | 5 |
| dot_local_hostname | METADATA-ECHO | `09c3a8cc` | 1 |
| email_address | METADATA-ECHO | `09c3a8cc` | 1 |
| high_entropy | FALSE-POSITIVE | `09c3a8cc` | 227 |
| high_entropy | FALSE-POSITIVE | `6485da27` | 4 |
| ipv4_address | FALSE-POSITIVE | `09c3a8cc` | 1 |
| local_temp_path | LOCAL-PATH | `09c3a8cc` | 24 |
| local_temp_path | LOCAL-PATH | `6485da27` | 1 |
| passphrase_shaped | FALSE-POSITIVE | `09c3a8cc` | 1 |
| precise:generic_assignment | FALSE-POSITIVE | `09c3a8cc` | 1 |
| precise:quoted_secretish_assignment | FALSE-POSITIVE | `09c3a8cc` | 99 |
| proxy_hostname | FALSE-POSITIVE | `09c3a8cc` | 1 |
| runpod_hostname | FALSE-POSITIVE | `09c3a8cc` | 2 |
| runpod_hostname | PUBLIC | `09c3a8cc` | 5 |
| ssh_identity_flag | FALSE-POSITIVE | `09c3a8cc` | 5 |
| ssh_key_name | FALSE-POSITIVE | `09c3a8cc` | 2 |
| ssh_key_path | FALSE-POSITIVE | `09c3a8cc` | 1 |
| url_host | PUBLIC | `09c3a8cc` | 5 |

The 21 new value(s) the history script leaves UNTRIAGED, triaged by Code in context (first locator = the commit and file of the first occurrence; the value only by its form):

| table | form | occurrences | first locator | Code's verdict | reason |
|---|---|---|---|---|---|
| context_free | `/Use...[len 42]#77f5bcb1` | 3 | `09c3a8cc results/raw/2026-10-08_note-N11-smoke.txt:110` | LOCAL-PATH | a path under the author's home directory (a local Python library directory) in N11's printed sys.path of the regression-suite run; the author is named in the repository; not a credential |
| passphrase_shaped | `A-Za...[len 9]#fab79a8e` | 2 | `09c3a8cc results/raw/2026-10-08_note-N12-history.json:22470` | FALSE-POSITIVE | a fragment of this class's own regular expression, as the history JSON's pattern table stores it; not a phrase |
| proxy_hostname | `len21:80e1d10e` | 1 | `09c3a8cc scripts/audit_note_N12_content.py:930` | FALSE-POSITIVE | the synthetic self-test fixture also listed under runpod_hostname |
| runpod_hostname | `prox...[len 16]#e0b5f502` | 1 | `09c3a8cc results/raw/2026-10-08_note-N12-content.md:743` | PUBLIC | the RunPod proxy service's domain, named in the content review's flag text about the ssh alias; it names the service, not a pod or an account |
| runpod_hostname | `ssh....[len 13]#f8ec340d` | 1 | `09c3a8cc results/raw/2026-10-08_note-N12-content.md:743` | PUBLIC | RunPod's public SSH gateway host, named in the same flag text; it names no pod or account |
| runpod_hostname | `runp...[len 9]#3124edae` | 11 | `09c3a8cc results/raw/2026-10-08_note-N12-content.md:743` | PUBLIC | RunPod's public site domain (on the history script's own public-host list), here inside class labels and flag text |
| runpod_hostname | `runp...[len 10]#421bbde9` | 7 | `09c3a8cc results/raw/2026-10-08_note-N12-history.json:20388` | FALSE-POSITIVE | the RunPod service domain as written in this class's own label, printed by the history JSON's tables |
| runpod_hostname | `len21:80e1d10e` | 1 | `09c3a8cc scripts/audit_note_N12_content.py:930` | FALSE-POSITIVE | a synthetic fixture in the content script's self-test (a placeholder number and the proxy suffix; its pod-id part is assembled from string pieces at run time); names no real host |
| runpod_hostname | `docs...[len 14]#f4b8c41f` | 1 | `09c3a8cc scripts/audit_note_N12_history.py:343` | PUBLIC | an entry of the history script's own public-host list (RunPod's documentation site) |
| runpod_hostname | `www....[len 13]#f53cd0c4` | 1 | `09c3a8cc scripts/audit_note_N12_history.py:343` | PUBLIC | an entry of the history script's own public-host list (RunPod's www site) |
| ssh_identity_flag | `argu...[len 11]#a36807c9` | 2 | `09c3a8cc results/raw/2026-10-08_note-N12-content-screen.json:141` | FALSE-POSITIVE | the word after the ssh identity flag in the content screen's category description; not a file |
| ssh_identity_flag | `<fil...[len 9]#13dfbe0e` | 4 | `09c3a8cc results/raw/2026-10-08_note-N12-history.json:20642` | FALSE-POSITIVE | the placeholder '<file>' with trailing punctuation, from this class's own label as the history JSON prints it |
| ssh_identity_flag | `<fil...[len 7]#1aedc48e` | 1 | `09c3a8cc results/raw/2026-10-08_note-N12-history.md:459` | FALSE-POSITIVE | the same placeholder, from this class's label in the history raw's table |
| ssh_identity_flag | `<fil...[len 8]#c17d7b45` | 1 | `09c3a8cc results/raw/2026-10-08_note-N12-history.md:487` | FALSE-POSITIVE | the same placeholder, from this class's label in the history raw's pattern list |
| ssh_identity_flag | `<fil...[len 9]#a2b73321` | 1 | `09c3a8cc scripts/audit_note_N12_history.py:3776` | FALSE-POSITIVE | the same placeholder, from this class's label in the history script's source |
| ssh_key_name | `id_r...[len 6]#f40883a1` | 2 | `09c3a8cc results/raw/2026-10-08_note-N12-history.md:403` | FALSE-POSITIVE | a generic default key-file name inside the history raw's description of its credential-file path pattern; no key file is named or tracked |
| ssh_key_name | `id_e...[len 10]#8e5d92fd` | 2 | `09c3a8cc results/raw/2026-10-08_note-N12-history.md:403` | FALSE-POSITIVE | the other generic default key-file name in the same description |
| ssh_key_path | `conf...[len 11]#41c256ae` | 1 | `09c3a8cc results/raw/2026-10-08_note-N12-content.md:751` | FALSE-POSITIVE | the prefix of a timestamped backup name of the standard ssh client config, quoted in the content review's flag text, which says it is not a key name; no key file |
| url_host | `crea...[len 19]#01ac74e6` | 5 | `09c3a8cc results/raw/2026-10-08_note-N12-licenses.json:327` | PUBLIC | a public website host (the Creative Commons site), in the licenses raw's licence links |
| url_host | `api....[len 14]#5b3097c5` | 23 | `09c3a8cc results/raw/2026-10-08_note-N12-licenses.json:3896` | PUBLIC | a public website host (GitHub's REST service host), in the licenses raw's source URLs |
| url_host | `docs...[len 15]#26ca8550` | 3 | `09c3a8cc results/raw/2026-10-08_note-N12-licenses.json:4101` | PUBLIC | a public website host (GitHub's documentation host), in the licenses raw's source URLs |

**Credential-shaped fallback rows** (the block's `key = value` / `key: value` shapes): 128 rows the history script leaves UNTRIAGED, all first seen in `09c3a8cc`. Code's triage:

| file | key | rows | Code's verdict | reason |
|---|---|---|---|---|
| `results/raw/2026-10-08_note-N12-history.md` | `token` | 1 | FALSE-POSITIVE | prose quoting a key spelled with a trailing colon; the captured value is the closing backtick |
| `results/raw/2026-10-08_note-N13-provenance.json` | `token` | 67 | FALSE-POSITIVE | an abbreviated hash in N13's provenance JSON; the next line holds its full form (a commit id) |
| `results/raw/2026-10-08_note-N13-provenance.json` | `token` | 48 | FALSE-POSITIVE | an abbreviated hash in N13's provenance JSON; the next line holds its full form (a sha256) |
| `results/raw/2026-10-08_note-N16-decoding.json` | `max_new_tokens` | 1 | FALSE-POSITIVE | a decoding parameter (maximum new tokens) recorded as 'n/a' |
| `results/raw/2026-10-08_note-N16-decoding.md` | `eos_token` | 1 | FALSE-POSITIVE | LLM-token sense: the model's end-of-sequence token string |
| `results/raw/2026-10-08_note-N3-echo-robustness.json` | `token` | 2 | FALSE-POSITIVE | the same sentence as the md's line, in the JSON |
| `results/raw/2026-10-08_note-N3-echo-robustness.md` | `token` | 1 | FALSE-POSITIVE | LLM-token sense: a label's token, then its probe-AUC range |
| `results/raw/2026-10-08_note-N3-echo-robustness.md` | `token` | 1 | FALSE-POSITIVE | LLM-token sense: the second label's token, then its probe-AUC range |
| `results/raw/2026-10-08_note-tier1_valuescheck.md` | `secret` | 1 | FALSE-POSITIVE | prose ('Informational, not a secret' followed by a path prefix); no value |
| `scripts/audit_note_N12_history.py` | `token` | 1 | FALSE-POSITIVE | the same prose, in the script that writes it |
| `scripts/audit_note_N13.py` | `cite_token` | 2 | FALSE-POSITIVE | a document:line citation label in N13's trigger table |
| `scripts/audit_note_N16.py` | `tokens` | 1 | FALSE-POSITIVE | a decoding-parameters table entry whose value starts with a run label (B2-r) |
| `scripts/audit_note_N2.py` | `max_tokens` | 1 | FALSE-POSITIVE | source code (a keyword argument) inside a regular expression of a referent check |

**Already recorded in the committed JSON** (values whose first occurrence is a window commit the committed scan covered): `bab921ce52` context_free LOCAL-PATH 1; `bab921ce52` high_entropy FALSE-POSITIVE 2; `c75d4d8aa3` context_free FALSE-POSITIVE 1; `c75d4d8aa3` context_free LOCAL-PATH 10; `c75d4d8aa3` high_entropy LOCAL-PATH 1; `c75d4d8aa3` local_temp_path LOCAL-PATH 14; `cf8eb5b9dd` context_free FALSE-POSITIVE 1; `cf8eb5b9dd` context_free LOCAL-PATH 1; `cf8eb5b9dd` high_entropy FALSE-POSITIVE 2; `cf8eb5b9dd` local_temp_path LOCAL-PATH 1; `cf8eb5b9dd` precise:quoted_secretish_assignment FALSE-POSITIVE 1.

**(d) Answers for the window.** TRUE-SECRET-CANDIDATE now 0 (new 0; committed 0). New values in the identifier classes the routing's redaction rule names (21 of the history script's 24 identifier classes: runpod_pod_id, runpod_volume_id, runpod_volume_name, runpod_endpoint_or_template_id, runpod_hostname, proxy_hostname, runpod_ssh_gateway_user, container_hostname, dot_local_hostname, ipv4_address, ipv6_address, ssh_port, ssh_key_name, ssh_key_path, ssh_identity_flag, ssh_fingerprint, ssh_public_key, claude_session_or_artifact_link, passphrase_shaped, email_address, cloud_account_id; the other 3, local_temp_path, claude_projects_path, url_host, are local paths and public hosts, counted in the tables above): 20, of them still open after triage: 0. By class and verdict: dot_local_hostname METADATA-ECHO 1; email_address METADATA-ECHO 1; ipv4_address FALSE-POSITIVE 1; passphrase_shaped FALSE-POSITIVE 1; proxy_hostname FALSE-POSITIVE 1; runpod_hostname FALSE-POSITIVE 2; runpod_hostname PUBLIC 5; ssh_identity_flag FALSE-POSITIVE 5; ssh_key_name FALSE-POSITIVE 2; ssh_key_path FALSE-POSITIVE 1. Their forms: the 17 the script left UNTRIAGED are in the table above; the others: dot_local_hostname `jspa...[len 16]#c6483009` METADATA-ECHO; email_address `jaso...[len 21]#bb973c14` METADATA-ECHO; ipv4_address `0.0....[len 7]#19e36255` FALSE-POSITIVE. New high-entropy candidates: in-context 231, context-free 40, all FALSE-POSITIVE or LOCAL-PATH after triage: yes. Values left UNTRIAGED after Code's triage: 0; credential-shaped rows left UNTRIAGED: 0.

**(e) Fallback grep at HEAD** (`git log -p --all | /usr/bin/grep -nEi '<the block's pattern, :77>'`, the block's :77 command as the history script runs it; 82,690,002 bytes of log): 11387 hit lines (a Python line-by-line cross-check counts 11387), against the committed 7782: +3605. Hit lines in the commits the committed scan did not see: 3605 (equal to the delta). Per commit in the window: `c75d4d8aa3` 30, `bab921ce52` 1, `cf8eb5b9dd` 41, `09c3a8cc54` 3251, `6485da2765` 354.

| alternative (block :77) | lines, committed | lines, now |
|---|---|---|
| `api[_-]?key` | 0 | 40 |
| `secret` | 60 | 247 |
| `token` | 7440 | 10737 |
| `password` | 6 | 95 |
| `sk-[A-Za-z0-9]` | 287 | 380 |
| `rp_[A-Za-z0-9]` | 9 | 14 |
| `BEGIN (RSA|OPENSSH)` | 0 | 0 |
| `AKIA[0-9A-Z]{16}` | 0 | 0 |

The new hits (2 commit(s) after the committed scan) by the history script's own bulk rules (occurrences, as its fallback triage counts them):

| alternative | rule | occurrences |
|---|---|---|
| `api[_-]?key` | X unclassified | 57 |
| `password` | P1 the audit block, its preflight raw, and that commit's message | 3 |
| `password` | P3 other prose | 105 |
| `rp_[A-Za-z0-9]` | R1 code identifier | 10 |
| `secret` | S2 prose in documents | 226 |
| `sk-[A-Za-z0-9]` | K1 in-word 'sk-' (task-/mask-/...) | 102 |
| `sk-[A-Za-z0-9]` | K2 word-initial 'sk-' | 15 |
| `token` | T1 LLM-token sense | 3955 |
| `token` | T2 credential-sense word, no value follows | 54 |
| `token` | T3 credential-sense word followed by a value | 8 |

Of these, 239 fall in the rules the history script lists for inspection rather than clearing (T2, T3, P3, K2, X), in 9 file(s); outside the audit's own scripts and raws: 0. Per rule and file: K2 `results/raw/2026-10-08_note-N12-content-screen.json` 1; K2 `results/raw/2026-10-08_note-N12-history.json` 5; K2 `results/raw/2026-10-08_note-N12-history.md` 5; K2 `scripts/audit_note_N12_content.py` 1; K2 `scripts/audit_note_N12_history.py` 3; P3 `results/raw/2026-10-08_note-N12-content.md` 7; P3 `results/raw/2026-10-08_note-N12-history.json` 20; P3 `results/raw/2026-10-08_note-N12-history.md` 27; P3 `results/raw/2026-10-08_note-N12-scrub.md` 9; P3 `results/raw/2026-10-08_note-tier1_valuescheck.md` 1; P3 `scripts/audit_note_N12_history.py` 30; P3 `scripts/audit_note_N12_scrub.py` 11; T2 `results/raw/2026-10-08_note-N12-history.json` 14; T2 `results/raw/2026-10-08_note-N12-history.md` 21; T2 `results/raw/2026-10-08_note-tier1_valuescheck.md` 1; T2 `scripts/audit_note_N12_content.py` 2; T2 `scripts/audit_note_N12_history.py` 16; T3 `results/raw/2026-10-08_note-N12-content-screen.json` 2; T3 `results/raw/2026-10-08_note-N12-history.json` 4; T3 `results/raw/2026-10-08_note-N12-history.md` 2; X `results/raw/2026-10-08_note-N12-content-screen.json` 3; X `results/raw/2026-10-08_note-N12-history.json` 14; X `results/raw/2026-10-08_note-N12-history.md` 18; X `results/raw/2026-10-08_note-N12-scrub.md` 1; X `scripts/audit_note_N12_content.py` 3; X `scripts/audit_note_N12_history.py` 18. Code read every one of their 166 distinct lines before this file was written (the set's sha256 `1f23b34136ba3317...` equals the one Code read): each is a secret pattern or its name, a class label, a credential's variable name inside a regular expression, a self-test template whose value is generated at run time, prose describing an earlier triage finding, or text about the (iii) continuity item, in the audit's own scripts and raws (N12's, plus 2 hit(s) on 2 line(s) of `results/raw/2026-10-08_note-tier1_valuescheck.md`); none carries a value. The 33 precise patterns and the high-entropy scans over the same blobs (section 3(c)-(d)) leave no candidate.

The literal :77 outcome is unchanged in kind: the fallback returns hits, so (i) is still not 'no hits' and stays STOP pending the PI.

**(f) Large blobs, known values and commit identities in the window.** Blobs reachable now but not from `bbc9ffe72f`: 83; over 1 MB 1, over 40 MB 0, over 50 MB 0, over 100 MB 0; the largest: `results/raw/2026-10-08_note-N3-echo-compute.json` 2,341,019 bytes, `RESULTS.md` 933,680 bytes, `results/raw/2026-10-08_note-N13-provenance.json` 865,736 bytes (the committed largest blob anywhere: 50,681,977 bytes). Files over 40 MB at HEAD: 5, equal to the committed list: yes.

Occurrences of the history raw's known sensitive values that each window commit added: in each blob it added or modified, the count in the new blob minus the count in the parent's blob at the same path, plus its message (by the history raw's class labels, short form; exact, the SSH-port class word-bounded). A modified file that already carried a value counts only what the commit added:

| commit | blobs added or modified | net new occurrences | files | occurrences in the new blobs (whole files) |
|---|---|---|---|---|
| `c75d4d8aa3` | 7 | runpod_pod_id 1 | `results/raw/2026-10-08_m-gcal-build_selftest.txt` | runpod_pod_id 1 |
| `bab921ce52` | 4 | 0 | - | 0 |
| `cf8eb5b9dd` | 9 | 0 | - | runpod volume name stem 1; runpod_pod_id 6; runpod_volume_id 8; runpod_volume_name 1; ssh_port 2 |
| `09c3a8cc54` | 56 | identity email, public in the commit headers 1 | `scripts/audit_note_N12_content.py` | identity email, public in the commit headers 1 |
| `6485da2765` | 7 | 0 | - | 0 |

| commit | author and committer are commit identities the history raw lists | their forms | gpgsig | session link in the message |
|---|---|---|---|---|
| `c75d4d8aa3` | yes | `jaso...[len 21]#bb973c14` | no | no |
| `bab921ce52` | yes | `jaso...[len 21]#bb973c14` | no | no |
| `cf8eb5b9dd` | yes | `jaso...[len 21]#bb973c14` | no | no |
| `09c3a8cc54` | yes | `jaso...[len 21]#bb973c14` | no | no |
| `6485da2765` | yes | `jaso...[len 21]#bb973c14` | no | no |

## 4. Pass / flag lines

- PASS -- **(1) server refs**. 5 server refs; none outside the local refs; refs/pull/* 0; every one an ancestor of origin/main; only main moved since the history raw's table.
- INFO -- **(2a) visibility**. PRIVATE now; the flip is the PI's.
- PASS -- **(2b) pull requests and comments**. 0 PRs, 0 review comments.
- PASS -- **(2c) issues and comments**. 0 issues, 0 issue/PR comments, 0 commit comments (issues are enabled: after the flip anyone can open one).
- PASS -- **(2d) releases**. 0 releases.
- PASS -- **(2e) Actions**. 0 runs, 0 workflows, 0 artifacts.
- PASS -- **(2f) wiki**. enabled False; wiki repository not found: yes.
- PASS -- **(2g) Pages**. HTTP 404: no site.
- PASS -- **(2h) deploy keys / webhooks**. 0 / 0 (readable).
- NOT READ -- **(2i) projects (v2)**. not readable with the CLI's scopes; the PI checks the Projects tab.
- PASS -- **(2j) force-pushed-away / deleted**. activity record (259 records): 0 force pushes, 0 deletions, 0 non-fast-forward pushes, 0 pushed objects not local.
- PASS -- **(2k) text screen and third-party logins**. 0 hits; 0 non-owner logins.
- FLAG -- **(3a) history script at HEAD**. refused to write (19 entries, 12 distinct values; 12 of them occur in its own committed text); step 3 cannot pass with the committed script as it stands.
- PASS -- **(3b) new TRUE-SECRET-CANDIDATE**. 0 now.
- PASS -- **(3c) new redaction-rule identifier values**. 20 new in the 21 classes listed in 3(d), 0 open after triage.
- FLAG -- **(3d) new values / shapes the script leaves UNTRIAGED**. 21 values and 128 shapes UNTRIAGED by the script; after Code's triage here 0 and 0.
- PASS -- **(3e) new large blobs**. largest new blob 2,341,019 bytes.
- PASS -- **(3f2) new fallback hits in the history script's inspection rules**. 239 hits, all in the audit's own files and read by Code: yes.
- INFO -- **(3f) fallback grep count**. 11387 at HEAD vs 7782 committed (+3605, all in the commits the committed scan did not see: yes).
- PASS -- **(3g) redaction-rule values added after the committed scan**. 0 net new occurrence(s) of the known RunPod, port, host, link, phrase and hostname values in what the commits after `cf8eb5b9dd` added; identity emails (public in the commit headers, listed by the history raw's pre-release section and not a blocker as drafted): 1.

## 5. What remains for the PI before the visibility flip

From the scrub index's pre-flip checklist (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:173`), marked by this run:

1. **DONE at `6485da2`, interim** (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:177`) -- Repeat at the release commit, immediately before the visibility change: the release commit and any tag push add or move server refs, and these surfaces can change until the flip. At this HEAD: ls-remote compared with the history raw's refs table: no extra branch or tag, no `refs/pull/*`, nothing to scan or delete beyond `main`'s new commits (section 1). Deleting the `claude/handoff-doc-next-steps-oeccd1` branch stays optional (it is scanned and an ancestor of origin/main).
2. **DONE at `6485da2`, interim, one part bounded** (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:178`) -- Repeat at the release commit, immediately before the visibility change: the release commit and any tag push add or move server refs, and these surfaces can change until the flip. At this HEAD: pull requests, comments, issues, Actions runs and artifacts, the wiki, releases, Pages, deploy keys and webhooks: none (section 2). Force-pushed-away commits: none on GitHub's activity record, a bound set by that record's retention. Projects (v2): not readable here; the PI's look.
3. **NOT DONE (and blocked as the script stands)** (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:179`) -- this run is an interim scan at HEAD, not the release commit. The committed history script refuses to write at HEAD (section 3a); before it can produce the clean run the step requires it needs a change -- triage entries for the values and credential-shaped rows of 3(c) and the inspection-rule hits of 3(e), or class labels printed without the strings its scan reports -- to a committed audit script, the PI's or design seat's call. The content and licenses scripts were not re-run.
4. **NOT DONE** (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:182`) -- untracked files were not reviewed by this run; at its start the checkout had 25 untracked, not-ignored file(s) other than this run's script and its two outputs, and 6 modified tracked file(s). Stage by explicit path.
5. **NOT DONE** (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:183`) -- the block's primary scanners (gitleaks, trufflehog) need the PI's word to install.

Not on the checklist and untouched by this run: the decisions D1-D4 and the other open PI items (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:140`), the (iii) continuity item (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:78`), and (i)'s resolution of the fallback's hits. This run's own two outputs and its script join the files the release re-run must scan (step 3).


## 6. Self-checks before writing

- Leak guard: 211 values held in memory (17 known, the rest dumped, untriaged or on the history script's leak list) and 5 guard shapes: 0 occurrences in either output; redacted forms printed 471, all known to the history JSON, this run's dump or the history script's leak list, none of a class recoverable by brute force.
- What the release re-run of the history script would make of this run's three files: its own precise, identifier, port-line, fallback, credential-shape, in-context high-entropy and context-free high-entropy rules, applied here in memory to the final texts (this file's sections 6 and 7 included) and iterated until the counts printed here are the counts of the files that print them. Rows it would leave open: 0. Fallback hits by bulk rule -- md: P3 3, S2 10, T1 24; json: P3 4, S2 110, T1 140; script: S2 9, T1 8. In-context high-entropy values by verdict -- md: none; json: FALSE-POSITIVE 10; script: FALSE-POSITIVE 4. Context-free high-entropy values by verdict -- md: FALSE-POSITIVE 3; json: FALSE-POSITIVE 6; script: FALSE-POSITIVE 2. (P3 and T2 are listed by that script for inspection, not counted as open.)
- History script: sha256 at the working tree `097de969dff2e4cf5c8c083ed6f4b120ef5629613e7fb250f85a70de17b0ef18`, at HEAD `097de969dff2e4cf5c8c083ed6f4b120ef5629613e7fb250f85a70de17b0ef18`; equal to the sha256 its committed raw records: yes.
- Run time before the self-checks 427.1 s.

## 7. Values-check

The first version of this raw (script sha256 `dc1d7845...ca76`, Code stamp Fri Oct  9 04:09:27 UTC 2026, run at `6485da2`; not committed) was checked by an adversarial checker, who re-ran the script and every read independently and returned 6 findings, all minor; it reported none as substantive. Code applied all 6 after confirming each, by reading the cited lines or by this run's output; none was rejected. The checker also reports that every other count it recomputed matched and that the redaction check was clean on the first version; those are its results and are not re-derived here. Dispositions, with this run's evidence:

1. **F1 (minor) -- 3(a) analysed only the entries the routed run's message prints (`leaks[:10]`): a partial sample whose content depends on Python's hash seed (6 distinct values in the first version; the checker, from a copy of the history script that prints every entry, found 12 distinct values behind the 19 entries, all in the audit's own committed text, all first seen in `09c3a8c`).** APPLIED, both remedies. The routed run now runs under PYTHONHASHSEED=0, so its printed sample is reproducible, and 3(a) calls it a partial sample. The full list is read deterministically from the unchanged script (in-process, same arguments, its own `leaks` list read from its frame when its leak assertion raises): 19 entries, 12 distinct values; entries equal to the routed run's count: yes; the routed sample contained in it: yes; the distinct values' sha256 prefixes equal the 12 the checker listed: yes; in the audit's own committed text: 12 of 12; first seen: `09c3a8cc` 12. The wording 'occurrences' is replaced by 'entries' (one per value and output; the script records the first match per output).
2. **F2 (minor) -- section 5 marked checklist items 1 and 2 DONE with no as-of qualifier, although the scrub index says each item needs the final HEAD, the network or the PI's word (`results/raw/2026-10-08_note-N12-scrub.md@6485da2:175`), and the release commit and tag pushes will add or move server refs.** APPLIED. Items 1 and 2 now read 'DONE at `6485da2`, interim' and say to repeat them at the release commit, immediately before the visibility change; item 3 stays NOT DONE. Each DONE is now also conditional on this run's own checks (section 1's line for item 1; the PASS lines (2b)-(2h) and (2j) for item 2).
3. **F3 (minor) -- the count of new values in the redaction-rule classes (4) used a class set that left out the SSH key-name, key-path and identity-flag classes and the RunPod and proxy hostnames.** APPLIED, extended by Code. The set is now the routing's redaction rule mapped onto the history script's identifier classes (21 of 24; the other 3 named in 3(d)), and the run asserts that the two lists partition the script's classes. Added: runpod_endpoint_or_template_id 0, runpod_hostname 7, proxy_hostname 1, ssh_key_name 2, ssh_key_path 1, ssh_identity_flag 5 new value(s) (runpod_endpoint_or_template_id is Code's addition: a RunPod identifier class the checker did not name). New values in the set: 20 (under the first version's set: 4); open after triage: 0. Of the added classes' 16 new values, 16 are rows of 3(c)'s UNTRIAGED table, each triaged there by Code; the others carry the history script's own verdict.
4. **F4 (minor) -- 3(e) said the inspection-rule hits were all 'in the audit's own N12 scripts and raws', but 2 of them are in the tier-1 values-check raw.** APPLIED. The sentence is now built from the per-file list and names any file outside N12's: 2 hit(s) on 2 line(s) of `results/raw/2026-10-08_note-tier1_valuescheck.md`. This run: 239 hits on 166 distinct lines, the set's sha256 equal to the one Code read: yes; outside the audit's own files: 0.
5. **F5 (minor) -- PASS conditions left out surfaces their own lines report: (2c) did not test the commit comments, (2e) did not test the workflows.** APPLIED, extended by Code. (2c) now requires 0 commit comments and (2e) 0 workflows. Code's extension: every PASS in (2b)-(2h) and (2j) also requires each query behind it to have returned rc 0 (in the first version a failed query of the pull requests, review comments, issues, issue or commit comments, releases, runs, artifacts or the activity record counted as 0 and could pass, and an unread wiki setting counted as disabled), (2f) requires the wiki setting to read False, and (2j) requires a non-empty activity record. This run: those 13 queries all rc 0: yes; (2b) PASS, (2c) PASS, (2e) PASS, (2j) PASS.
6. **F6 (minor) -- the section-6 self-check of what a release re-run would make of this run's three files did not apply the history scan's in-context or context-free high-entropy rules.** APPLIED. The pre-check now also runs the history script's own in-context rule (its run pattern, context test, entropy bar and triage) and its context-free scan (its own scan function and triage) over the three files, and refuses on any high-entropy verdict other than FALSE-POSITIVE or PUBLIC. It now runs on the final texts, sections 6 and 7 included, and is iterated until the counts section 6 prints are the counts of the files that print them. This run's counts: section 6.
