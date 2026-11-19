# The pre-push screen's gitleaks classifier, amended as the seat ruled (fourth sitting, the answers' §6), and its test (PI date 2026-11-18)

*Code's raw (the coordinating session). The screen lives in the coordinating session's scratch, not in the tree. Its
gitleaks classifier is amended from `gl4.py` to `gl5.py` (sha256 9d108e994578f25450a1b17c485d69a341f06bbd620a9e094ef54ea19489c325),
per the seat's answers of the fourth sitting
(`results/raw/2026-11-18_n-step4-resume_design-to-code_answers.md`, §6.1–§6.2) and the PI's routing item 6. No output
here prints a matched value, a key, a path's content or a line; the keys §2 names are the synthetic report's, which
Code wrote.*

## 1. What `gl5.py` classes as a digest

A finding whose secret is a 64-character hexadecimal token is a digest when any of these holds. Each finding is
counted by class, the label naming the clearances that held (for example `digest:nesting+file`), and for a finding
inside, each clearance is reported as a yes/no class:
- **immediate:** the key just before the value on its line carries "sha" (C.3's first form, as `gl4.py` had it);
- **nesting:** the file parses as JSON, and some key on a path from the root to a leaf equal to the value carries "sha"
  (C.3 read by nesting, §6.1);
- **file:** the value's key (the leaf's key in the JSON, else the line's key) names a tracked file at the commit
  screened (the finding's own commit, as gitleaks attributes it), and the value equals the sha256 of that file's blob
  there (the digest class, §6.1).

"sha" is a substring test, as in C.3's words, so a key such as "shape…" or "shared…" also carries it; under nesting,
every 64-hex leaf beneath such a key clears.

Any other finding inside `data/*/ckpt` or `data/*/reports` is a halt for the seat. For each finding inside, one line
in the form §6.2 adopted, carried to the amended classes: the path class, the commit, the rule's name, three yes/no
classes (immediate, nesting, file; the helper printed two) and the verdict, never a value, a key, a path's content or
a line. Non-digest findings outside are listed to read, as before.

## 2. The synthetic test

A scratch repository, one commit (`010cb68`, thrown away), holding two small tracked modules, a JSON report under
`data/x/reports/`, a text file under `data/x/ckpt/` and a config file under `scripts/`, each value a fresh random or
computed 64-hex token. gitleaks 8.30.1 (default rules) found six matches. The cases, by the classes `gl5.py` printed:
- a module's sha256 nested under a map named `imported_sha256`, keyed by the module's path: digest by nesting and by
  file (inside 2);
- a random value under `api_key` in a map whose path carries no "sha": halt (inside 3);
- a random value under a key whose own name carries "sha": digest by immediate key and by nesting (inside 4);
- a module's sha256 keyed by its path in a map named `manifest`: digest by file (inside 5);
- a random value on a text line under `data/x/ckpt/`: halt (inside 1);
- a random value in `scripts/conf.txt`: read, outside.

`gl4.py` on the same report cleared only the immediate case.

## 3. The outputs, verbatim

```text
== gl5 on the synthetic repository (6 findings):
gitleaks findings: 6
   ('data/x/ckpt', 'generic-api-key', 'hex64-other') x 1
   ('data/x/reports', 'generic-api-key', 'digest:file') x 1
   ('data/x/reports', 'generic-api-key', 'digest:immediate+nesting') x 1
   ('data/x/reports', 'generic-api-key', 'digest:nesting+file') x 1
   ('data/x/reports', 'generic-api-key', 'hex64-other') x 1
   ('outside', 'generic-api-key', 'hex64-other') x 1
   inside 1: data/x/ckpt at 010cb68: rule generic-api-key; immediate key carries sha: no; a key on its path carries sha: no; equals the sha256 of the tracked file its key names: no -> HALT
   inside 2: data/x/reports at 010cb68: rule generic-api-key; immediate key carries sha: no; a key on its path carries sha: yes; equals the sha256 of the tracked file its key names: yes -> digest
   inside 3: data/x/reports at 010cb68: rule generic-api-key; immediate key carries sha: no; a key on its path carries sha: no; equals the sha256 of the tracked file its key names: no -> HALT
   inside 4: data/x/reports at 010cb68: rule generic-api-key; immediate key carries sha: yes; a key on its path carries sha: yes; equals the sha256 of the tracked file its key names: no -> digest
   inside 5: data/x/reports at 010cb68: rule generic-api-key; immediate key carries sha: no; a key on its path carries sha: no; equals the sha256 of the tracked file its key names: yes -> digest
   READ scripts/conf.txt@010cb68:1 generic-api-key hex64-other shape 64:hex-lower
   HALT: a non-digest finding inside ckpt/reports, for the seat (C.3 as amended)
gl5 exit=2

== gl4 on the same report, for contrast:
gitleaks findings: 6
   ('data/x/ckpt', 'generic-api-key', 'hex64-other') x 1
   ('data/x/reports', 'generic-api-key', 'digest') x 1
   ('data/x/reports', 'generic-api-key', 'hex64-other') x 3
   ('outside', 'generic-api-key', 'hex64-other') x 1
   READ scripts/conf.txt@010cb68:1 generic-api-key hex64-other shape 64:hex-lower
   HALT: a non-digest finding inside ckpt/reports, for the seat (C.3)
gl4 exit=2

== gl5 on push #9's gitleaks report (ad856f0..1272702):
gitleaks findings: 1
   ('data/n/reports', 'generic-api-key', 'digest:nesting+file') x 1
   inside 1: data/n/reports at 6df2131: rule generic-api-key; immediate key carries sha: no; a key on its path carries sha: yes; equals the sha256 of the tracked file its key names: yes -> digest
gl5 exit=0

== gl5 on push #10's gitleaks report (1272702..cf318c5):
gitleaks findings: 1
   ('data/n/reports', 'generic-api-key', 'digest:nesting+file') x 1
   inside 1: data/n/reports at 6e3474d: rule generic-api-key; immediate key carries sha: no; a key on its path carries sha: yes; equals the sha256 of the tracked file its key names: yes -> digest
gl5 exit=0
```
