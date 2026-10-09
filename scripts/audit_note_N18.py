#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N18: hashes for the note (the release manifest).

Block :132-133 asks for the sha256 of the final note and the tag commit hash, both for the
note's footer, and a `results/raw/<stamp>_note-release-manifest.json` with the tag, the note
sha and the N13 table's shas. This script writes that JSON and a short .md beside it:

  - the tag name (the PI's routing of 2026-10-09, item 7) and the self-reference statement:
    the tag goes on the commit that adds this manifest, so that commit's hash cannot be
    inside it; it is to be recorded after tagging;
  - the note and its two SVGs, each sha256 asserted against the routed value;
  - the commit N1 final names as the one at which the last of the note's figures entered
    the record, read from the N1 final ledger JSON and checked against its md;
  - every row of the N13 provenance table (results/raw/2026-10-08_note-N13-provenance.json
    read at 09c3a8c) with its version content sha256 and status carried verbatim, and a
    re-hash of each row whose document is a file at the row's record commit;
  - the block's sha256; the preprint ('pending patch v6' unless the file on disk differs
    from the block's post-patch-v4 reference);
  - a file list with sha256s: README-NOTE.md, LICENSE, LICENSE-CC-BY-4.0, LICENSING.md,
    the N1 final ledger md/json, every results/raw/*_note-* file and every
    scripts/audit_note_*.py at the time of the run (this script's own two outputs excluded);
  - the re-run triggers: what must not change between this run and the tag commit
    (the note, the SVGs, the preprint including the arrival of patch v6, any listed file).

Read-only: it reads files and runs read-only git commands (rev-parse, symbolic-ref, ls-tree,
show, cat-file -e, merge-base --is-ancestor) and `date -u` for the stamp. It writes only its
two outputs. Exit codes:
  0  both outputs written, every N13 file row re-hashed equal;
  1  both outputs written, but at least one N13 file row re-hashed to a different sha256
     (the manifest carries each MISMATCH verbatim; the run is a finding, not a pass);
  2  STOP: an assertion failed; nothing is written.
Both outputs are rendered in memory before either file is opened, so an error while
building or rendering writes nothing.

    python scripts/audit_note_N18.py [--out results/raw/2026-10-09_note-release-manifest.json]
        [--note PATH] [--svg PATH ...] [--expect PATH=SHA256 ...] [--ledger PATH]
        [--preprint-pi-confirmed SHA256]

--note/--svg/--expect exist for a re-run against an edited or renamed note: a path with no
routed value below needs a full 64-hex --expect, and the manifest records where each
expected value came from.

--preprint-pi-confirmed records, for a re-run after patch v6 arrives, that the PI has
confirmed the preprint on disk is the post-v6 file. It takes the full sha256, which must
equal the file on disk and must differ from the block's post-patch-v4 reference. The script
cannot see the confirmation itself: the manifest says the value was supplied on the command
line as the PI's confirmation, and records the command.
"""
import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_PIN = "bbc9ffe"
AUDIT_PIN = "09c3a8c"
# The block's sha256 as abbreviated in its placing commit's message (bbc9ffe: "sha256 8cd8a9ac...3841").
BLOCK_ROUTED = ("8cd8a9ac", "3841")
N18_LINES = (132, 133)
TAG = "note-2026-10-v1"
TAG_SOURCE = ("the PI's routing of 2026-10-09, item (7), as routed to Code: tag name note-2026-10-v1, placed on the "
              "final audit commit after N1 and N18; the block leaves the name to the PI and suggests it at "
              "AUDIT-note-release-v1_2.md@bbc9ffe:14")
NOTE = "RESEARCH-NOTE-v0_3-draft.md"
SVGS = ["2026-10-06_F1b_five-link-panels.svg", "2026-10-06_F2_macar-lineage-roc_post.svg"]
# Routed values, abbreviated as routed. The note's is the PI's routing to this part ("5a34309f...71"); the
# SVGs' are the routed values the N1 final ledger records (note_rows_final.files[].routed), checked below.
ROUTED = {
    NOTE: ("5a34309f", "71", "the PI's routing of 2026-10-09 as routed to this part"),
    SVGS[0]: ("192250ca", "0afd", "the routed value recorded in the N1 final ledger (note_rows_final.files[].routed)"),
    SVGS[1]: ("5e4fc91c", "1fef", "the routed value recorded in the N1 final ledger (note_rows_final.files[].routed)"),
}
LEDGER = "results/raw/2026-10-09_note-N1-claims-ledger-final.json"
N13_JSON = "results/raw/2026-10-08_note-N13-provenance.json"
PREPRINT = "PREPRINT-v1_0-draft.md"
PREPRINT_REF = ("d6431e97", "222b8")  # block :21, "post-patch-v4 copy, sha `d6431e97…222b8`"
NAMED_FILES = ["README-NOTE.md", "LICENSE", "LICENSE-CC-BY-4.0", "LICENSING.md"]
WAIT_FILES = ["README-NOTE.md", "results/raw/2026-10-08_note-N12-scrub.md"]
DEFAULT_OUT = "results/raw/2026-10-09_note-release-manifest.json"


class Stop(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise Stop(msg)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_id(path):
    with open(path, "rb") as f:
        b = f.read()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def git(*args, check=True, binary=False):
    r = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True)
    if check and r.returncode != 0:
        raise Stop("git %s failed: %s" % (" ".join(args), r.stderr.decode(errors="replace").strip()))
    return r if not check else (r.stdout if binary else r.stdout.decode())


def abs_(p):
    return p if os.path.isabs(p) else os.path.join(ROOT, p)


def matches_routed(sha, routed):
    pre, suf = routed[0], routed[1]
    return sha.startswith(pre) and sha.endswith(suf)


def head_blobs(paths):
    """{path: blob id at HEAD} for the tracked ones among paths (one ls-tree call)."""
    paths = [p for p in paths if not os.path.relpath(abs_(p), ROOT).startswith("..")]
    if not paths:
        return {}
    out = git("ls-tree", "-r", "HEAD", "--", *paths)
    res = {}
    for ln in out.splitlines():
        meta, p = ln.split("\t", 1)
        res[p] = meta.split()[2]
    return res


def file_entry(path, blobs, category):
    ap = abs_(path)
    blob = blobs.get(path)
    return {
        "path": path,
        "category": category,
        "sha256": sha256_file(ap),
        "bytes": os.path.getsize(ap),
        "tracked_at_head": blob is not None,
        "equal_to_head": (git_blob_id(ap) == blob) if blob is not None else None,
    }


def parse_expect(items):
    res = {}
    for it in items or []:
        need("=" in it, "--expect takes PATH=SHA256, got %r" % it)
        p, s = it.split("=", 1)
        need(re.fullmatch(r"[0-9a-f]{64}", s) is not None, "--expect %s: a full 64-hex sha256 is required" % p)
        res[p] = s
    return res


def build(a, stamp):
    out_json = a.out
    out_md = re.sub(r"\.json$", ".md", out_json)
    need(out_md != out_json, "--out must end in .json")
    head = git("rev-parse", "HEAD").strip()
    branch = git("symbolic-ref", "-q", "--short", "HEAD", check=False).stdout.decode().strip() or None
    expect = parse_expect(a.expect)
    if a.preprint_pi_confirmed is not None:
        need(re.fullmatch(r"[0-9a-f]{64}", a.preprint_pi_confirmed) is not None,
             "--preprint-pi-confirmed: a full 64-hex sha256 is required")

    # --- the block -------------------------------------------------------------------------------
    blines = open(abs_(BLOCK), encoding="utf-8").read().splitlines()
    need(blines[N18_LINES[0] - 1].startswith("### N18. Hashes for the note"),
         "block :%d is not the N18 heading" % N18_LINES[0])
    need("note-release-manifest.json" in blines[N18_LINES[1] - 1], "block :%d does not name the manifest" % N18_LINES[1])
    block_sha = sha256_file(abs_(BLOCK))
    need(matches_routed(block_sha, BLOCK_ROUTED), "block sha256 %s does not match %s...%s" % ((block_sha,) + BLOCK_ROUTED))
    block_at_pin = sha256_bytes(git("show", "%s:%s" % (BLOCK_PIN, BLOCK), binary=True))
    need(block_at_pin == block_sha, "block differs from its committed version at %s" % BLOCK_PIN)
    pref_line = [i + 1 for i, ln in enumerate(blines) if PREPRINT_REF[0] in ln]
    need(len(pref_line) == 1, "the preprint reference %s occurs %d times in the block" % (PREPRINT_REF[0], len(pref_line)))

    # --- the note and the SVGs -------------------------------------------------------------------
    note_files = [a.note] + list(a.svg)
    nb = head_blobs(note_files)
    notes = []
    for p in note_files:
        need(os.path.isfile(abs_(p)), "%s is not on disk" % p)
        sha = sha256_file(abs_(p))
        if p in expect:
            ok, how, routed = sha == expect[p], "full value supplied with --expect", expect[p]
        else:
            need(p in ROUTED, "no routed sha256 for %s; pass --expect %s=<sha256>" % (p, p))
            ok, how, routed = matches_routed(sha, ROUTED[p]), ROUTED[p][2], "%s...%s" % ROUTED[p][:2]
        need(ok, "%s sha256 %s does not match the expected %s (%s)" % (p, sha, routed, how))
        e = file_entry(p, nb, "note" if p == a.note else "svg")
        e.update({"expected": routed, "expected_source": how, "assert": "PASS"})
        notes.append(e)

    # --- N1 final ledger ---------------------------------------------------------------------------
    led_path = a.ledger
    led_md = re.sub(r"\.json$", ".md", led_path)
    led = json.load(open(abs_(led_path), encoding="utf-8"))
    need(led.get("provisional") is False, "%s is not final (provisional is %r)" % (led_path, led.get("provisional")))
    ff = led["final_for"]
    need(ff["note"] == a.note and ff["note_sha256"] == notes[0]["sha256"],
         "N1 final covers %s %s, not %s %s: re-run N1" % (ff["note"], ff["note_sha256"], a.note, notes[0]["sha256"]))
    led_svgs = {s["path"]: s["sha256"] for s in ff["svgs"]}
    for e in notes[1:]:
        need(led_svgs.get(e["path"]) == e["sha256"], "N1 final does not cover %s at %s: re-run N1" % (e["path"], e["sha256"]))
    need(len(led_svgs) == len(notes) - 1, "N1 final covers %d SVGs, this run %d" % (len(led_svgs), len(notes) - 1))
    for f in led["note_rows_final"]["files"]:
        if f["path"] in ROUTED and f["path"] not in expect:
            r = ROUTED[f["path"]]
            need(f["routed"] in ("%s...%s" % r[:2],) or matches_routed(f["routed"], r),
                 "N1's routed value for %s (%s) differs from this script's (%s...%s)" % ((f["path"], f["routed"]) + r[:2]))
    rows_sha = sha256_file(abs_(ff["rows_file"]))
    need(rows_sha == ff["rows_file_sha256"], "%s changed since N1 final read it" % ff["rows_file"])
    tag = led["note_rows_final"]["tag"]
    figs = tag["including_audit_raws"]
    plain = "**Stated plainly: the last of the note's figures entered the record at `%s`" % figs["commit"]
    md_text = open(abs_(led_md), encoding="utf-8").read()
    need(md_text.count(plain) == 1, "%s does not state the figures commit %s plainly once" % (led_md, figs["commit"]))
    plain_line = md_text[:md_text.index(plain)].count("\n") + 1
    anc = git("merge-base", "--is-ancestor", figs["commit"], "HEAD", check=False).returncode
    need(anc in (0, 1), "merge-base --is-ancestor failed for %s" % figs["commit"])
    n1_script = led.get("script")
    n1_script_now = sha256_file(abs_(n1_script)) if n1_script and os.path.isfile(abs_(n1_script)) else None
    n1 = {
        "ledger_json": led_path, "ledger_md": led_md,
        "ledger_head_at_run": led.get("head_at_run"), "ledger_code_stamp_utc": led.get("code_stamp_utc"),
        "provisional": led.get("provisional"),
        "covers_note_sha256_of_this_run": True, "covers_svg_sha256s_of_this_run": True,
        "note_rows_file": ff["rows_file"], "note_rows_file_sha256": rows_sha,
        "figures_commit": figs["commit"], "figures_commit_date": figs["date"],
        "figures_commit_set_by_rows": figs["rows"],
        "figures_commit_basis": ("N1 final, note_rows_final.tag.including_audit_raws (the note carries computed-new "
                                 "figures and figures whose only carrier is N19's raw); stated plainly at %s:%d (the file as read at this run)" % (led_md, plain_line)),
        "record_sources_only_candidate": tag["record_sources_only"]["commit"],
        "record_sources_only_candidate_date": tag["record_sources_only"]["date"],
        "figures_commit_is_ancestor_of_head_at_this_run": anc == 0,
        "n1_script": n1_script, "n1_script_sha256_in_ledger": led.get("script_sha256"),
        "n1_script_sha256_now": n1_script_now,
        "n1_script_unchanged_since_ledger": n1_script_now == led.get("script_sha256"),
    }

    # --- N13 provenance table, read at the audit pin ----------------------------------------------
    n13_bytes = git("show", "%s:%s" % (AUDIT_PIN, N13_JSON), binary=True)
    n13 = json.loads(n13_bytes)
    n13_rows = []
    for r in n13["rows"]:
        doc = r["document"]
        if "(log entry)" in doc:
            rehash = "not re-hashed (a log-entry span; N13 extracted the entry)"
        else:
            got = git("cat-file", "-e", "%s:%s" % (r["record_commit"], doc), check=False)
            if got.returncode != 0:
                rehash = "not re-hashed (%s is not a file at %s)" % (doc, r["record_commit"][:7])
            else:
                s = sha256_bytes(git("show", "%s:%s" % (r["record_commit"], doc), binary=True))
                rehash = "match" if s == r["content_sha256"] else "MISMATCH (%s)" % s
        n13_rows.append({
            "id": r["id"], "kind": r["kind"], "title": r["title"], "document": doc,
            "version_of_record": r["version_of_record"], "record_commit": r["record_commit"],
            "committer_utc": r["committer_utc"], "content_sha256": r["content_sha256"],
            "content_sha256_status": r["content_sha256_status"],
            "recorded_sha256_found": r["recorded_sha256"].get("found"),
            "status": r["status"], "rehash_at_run": rehash,
        })
    n13_wt = sha256_file(abs_(N13_JSON)) if os.path.isfile(abs_(N13_JSON)) else None
    log_rows = [r["id"] for r in n13_rows if r["rehash_at_run"].startswith("not re-hashed (a log-entry")]
    file_rows = [r for r in n13_rows if r["id"] not in log_rows]
    n13_out = {
        "source": "%s@%s" % (N13_JSON, AUDIT_PIN), "source_sha256_at_pin": sha256_bytes(n13_bytes),
        "working_tree_equal": n13_wt == sha256_bytes(n13_bytes),
        "n_rows": len(n13_rows),
        "n_log_entry_rows": len(log_rows), "log_entry_row_ids": log_rows,
        "n_file_rows": len(file_rows),
        "n_file_rows_rehash_match": sum(1 for r in file_rows if r["rehash_at_run"] == "match"),
        "n_file_rows_rehash_mismatch": sum(1 for r in file_rows if r["rehash_at_run"].startswith("MISMATCH")),
        "n_file_rows_not_rehashed": sum(1 for r in file_rows if r["rehash_at_run"].startswith("not re-hashed")),
        "rule": ("every row's content_sha256 (the sha256 of the row's version of record), content_sha256_status, "
                 "recorded_sha256.found and status carried verbatim from N13; rehash_at_run is this script's own "
                 "check: sha256 of `git show <record_commit>:<document>` for every row whose document is a file"),
        "rows": n13_rows,
    }

    # --- preprint ----------------------------------------------------------------------------------
    pconf = a.preprint_pi_confirmed
    pp_routing = ("the PI's routing of 2026-10-09, item (5), as routed to Code: PREPRINT-v1_0-draft.md is committed "
                  "at the tag after patch v6 is applied")
    if os.path.isfile(abs_(PREPRINT)):
        ps = sha256_file(abs_(PREPRINT))
        bref = "%s…%s (post-patch-v4 copy), AUDIT-note-release-v1_2.md@%s:%d" % (
            PREPRINT_REF[0], PREPRINT_REF[1], BLOCK_PIN, pref_line[0])
        if matches_routed(ps, PREPRINT_REF):
            need(pconf is None, "--preprint-pi-confirmed given, but %s on disk is still the block's post-patch-v4 "
                                "reference %s...%s" % ((PREPRINT,) + PREPRINT_REF))
            preprint = {"path": PREPRINT, "status": "pending patch v6", "sha256": None,
                        "on_disk_matches_block_reference": True, "block_reference": bref,
                        "pi_confirmation": None}
        elif pconf is not None:
            need(pconf == ps, "--preprint-pi-confirmed %s does not equal %s on disk (%s)" % (pconf, PREPRINT, ps))
            preprint = {"path": PREPRINT,
                        "status": "post-patch-v6, as confirmed by the PI (confirmation supplied to this run with "
                                  "--preprint-pi-confirmed; see pi_confirmation)",
                        "sha256": ps, "on_disk_matches_block_reference": False, "block_reference": bref,
                        "pi_confirmation": ("the full sha256 was supplied on the command line as the PI's confirmation "
                                            "that this file is the post-v6 preprint; the script asserted it equals the "
                                            "file on disk and cannot see the confirmation itself (the command is "
                                            "recorded in `command`)")}
        else:
            preprint = {"path": PREPRINT, "status": ("differs from the block's post-patch-v4 reference; it is the "
                                                     "post-v6 file only if the PI confirms (not confirmed to this run)"),
                        "sha256": ps, "on_disk_matches_block_reference": False, "block_reference": bref,
                        "pi_confirmation": None}
        preprint["tracked_at_head"] = bool(head_blobs([PREPRINT]))
    else:
        need(pconf is None, "--preprint-pi-confirmed given, but %s is not on disk" % PREPRINT)
        preprint = {"path": PREPRINT, "status": "pending patch v6 (file not on disk)", "sha256": None,
                    "pi_confirmation": None}
    preprint["routing"] = pp_routing
    preprint["rerun_trigger"] = ("If patch v6 arrives, or the file otherwise changes, after this run and before the tag "
                                 "commit, N18 must be re-run: this section describes the file as found at this run, and "
                                 "the tag commit is to hold the post-v6 file.")

    # --- wait check ----------------------------------------------------------------------------------
    today = datetime.date.today().isoformat()
    waits = []
    for p in WAIT_FILES:
        m = os.path.getmtime(abs_(p))
        mdate = datetime.date.fromtimestamp(m).isoformat()
        waits.append({
            "path": p, "mtime_utc": datetime.datetime.fromtimestamp(m, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "mtime_local_date": mdate, "local_date_at_run": today, "modified_today": mdate == today,
            "reading": ("modified today; hashed as it stood at this run" if mdate == today
                        else "not modified today; read as found"),
        })

    # --- file list -------------------------------------------------------------------------------------
    own = {os.path.relpath(abs_(out_json), ROOT), os.path.relpath(abs_(out_md), ROOT)}
    globbed = sorted(set(os.path.relpath(p, ROOT) for p in
                         glob.glob(os.path.join(ROOT, "results/raw/*_note-*")) +
                         glob.glob(os.path.join(ROOT, "scripts/audit_note_*.py"))))
    own |= {p for p in globbed if re.fullmatch(r"results/raw/[^/]*_note-release-manifest\.(json|md)", p)}
    excluded = sorted(own)  # this run's own outputs whether or not they exist yet, and any other manifest raw on disk
    listed = []
    for p in NAMED_FILES:
        need(os.path.isfile(abs_(p)), "%s is not on disk" % p)
        listed.append((p, "named"))
    for p in (led_path, led_md):
        listed.append((p, "N1 final ledger"))
    for p in globbed:
        if p in own:
            continue
        cat = "audit raw" if p.startswith("results/raw/") else "audit script"
        if p in (led_path, led_md):
            continue
        listed.append((p, cat))
    paths = sorted(set(p for p, _ in listed))
    cats = {}
    for p, c in listed:
        cats.setdefault(p, c)
    blobs = head_blobs(paths)
    files = [file_entry(p, blobs, cats[p]) for p in paths]
    sumtext = "".join("%s  %s\n" % (f["sha256"], f["path"]) for f in files)

    # --- tag state --------------------------------------------------------------------------------------
    t = git("rev-parse", "-q", "--verify", "refs/tags/%s^{commit}" % TAG, check=False)
    tag_state = {"exists_at_run": t.returncode == 0,
                 "points_to": t.stdout.decode().strip() if t.returncode == 0 else None}

    script_rel = os.path.relpath(os.path.abspath(__file__), ROOT)
    manifest = {
        "item": "N18", "title": "release manifest (hashes for the note)",
        "code_stamp_utc": stamp, "head_at_run": head, "branch_at_run": branch,
        "block": BLOCK, "block_sha256": block_sha,
        "block_sha256_routed": "%s...%s" % BLOCK_ROUTED, "block_sha256_matches_routed": True,
        "block_equal_to_committed_at": BLOCK_PIN,
        "block_n18_lines": list(N18_LINES),
        "script": script_rel, "script_sha256": sha256_file(os.path.abspath(__file__)),
        "interpreter": sys.executable, "python": sys.version.split()[0],
        "command": " ".join([sys.executable] + sys.argv),
        "tag": {
            "name": TAG, "source": TAG_SOURCE, "state_at_run": tag_state,
            "commit": None,
            "commit_statement": ("The tag is placed on the commit that adds this manifest. A commit's hash is computed "
                                 "over a tree that contains this file, so the hash cannot be written inside it "
                                 "(self-reference). It is to be recorded after tagging: in the note's footer (block "
                                 ":133; the footer is the design seat's) and in a post-tag raw (the procedure routed to "
                                 "Code for this part; neither the block nor the PI's routing names that raw)."),
            "expected_parent_note": ("HEAD at this run is %s; the tag commit descends from it if the manifest is "
                                     "committed on top of it, which this script does not check." % head),
        },
        "note": notes[0],
        "svgs": notes[1:],
        "rerun_rule": ("This manifest covers only the files as hashed at this run; the tag commit's tree must hold each "
                       "of them at the sha256 recorded here. If any trigger below fires after this run and before the "
                       "tag commit, the named items must be re-run, N18 last."),
        "rerun_triggers": [
            {"trigger": ("the note or either SVG changes (including the [REPO LINK] replacement or a footer added to "
                         "the file)"),
             "rerun": "N1, then N18"},
            {"trigger": ("patch v6 arrives, or PREPRINT-v1_0-draft.md otherwise changes (the PI's routing of "
                         "2026-10-09, item (5), as routed to Code, commits the post-v6 file at the tag; this manifest "
                         "records the file as found at this run)"),
             "rerun": "N18 (with --preprint-pi-confirmed once the PI confirms the post-v6 file)"},
            {"trigger": ("any file in files.list changes, is added under results/raw/*_note-* or scripts/audit_note_*.py, "
                         "or is removed (for example README-NOTE.md when a placeholder is filled, or the N1 final "
                         "ledger when N1 is re-run)"),
             "rerun": "N18"},
        ],
        "footer_note": ("The block puts the note's sha256 in the note's footer (:133). A footer inside the hashed file "
                        "changes that file's sha256, so the footer cannot state the hash of the file that contains it; "
                        "how the footer and the repository copy relate is the design seat's to settle."),
        "n1": n1,
        "n13": n13_out,
        "preprint": preprint,
        "wait_check": waits,
        "files": {
            "rule": ("README-NOTE.md, LICENSE, LICENSE-CC-BY-4.0, LICENSING.md, the N1 final ledger md/json, every "
                     "results/raw/*_note-* file and every scripts/audit_note_*.py on disk at this run, sorted by path; "
                     "this script's own two outputs and any results/raw/*_note-release-manifest.json/.md are excluded "
                     "(a file cannot carry its own hash). tracked_at_head "
                     "and equal_to_head compare the working file's git blob id with HEAD's."),
            "excluded_self": excluded,
            "n_files": len(files),
            "sha256sum_list_sha256": sha256_bytes(sumtext.encode()),
            "sha256sum_list_recipe": ("sha256 of the lines '<sha256>  <path>\\n' over files.list in its order (sorted by path); "
                                      "equal to piping `shasum -a 256 <the paths in that order>` into `shasum -a 256`"),
            "n_tracked_at_head": sum(f["tracked_at_head"] for f in files),
            "n_equal_to_head": sum(1 for f in files if f["equal_to_head"]),
            "list": files,
        },
    }
    mism = [r["id"] for r in n13_rows if r["rehash_at_run"].startswith("MISMATCH")]
    return manifest, out_json, out_md, mism


def short(s, n=12):
    return s[:n] if s else s


def render_md(m):
    out = []
    w = out.append
    n1, n13, pp = m["n1"], m["n13"], m["preprint"]
    w("# AUDIT-note-release v1.2 -- N18: release manifest (hashes for the note)")
    w("")
    w("- Code stamp: %s (date -u); HEAD at run `%s` (branch %s)" % (m["code_stamp_utc"], m["head_at_run"], m["branch_at_run"]))
    w("- Block `%s` sha256 `%s` (matches the routed %s; equal to its committed version at `%s`); N18 is block :%d-%d" % (
        m["block"], m["block_sha256"], m["block_sha256_routed"], m["block_equal_to_committed_at"],
        m["block_n18_lines"][0], m["block_n18_lines"][1]))
    w("- Script `%s` sha256 `%s`; interpreter %s (Python %s)" % (m["script"], m["script_sha256"], m["interpreter"], m["python"]))
    w("- The JSON beside this file is the manifest; this file summarises it.")
    w("")
    w("## Tag")
    w("")
    w("- Name: `%s`. Source: %s." % (m["tag"]["name"], m["tag"]["source"]))
    w("- Tag commit: not in this manifest. %s" % m["tag"]["commit_statement"])
    w("- Tag state at this run: %s." % ("exists, pointing to `%s`" % m["tag"]["state_at_run"]["points_to"]
                                        if m["tag"]["state_at_run"]["exists_at_run"] else "absent"))
    w("")
    w("## The note and its figures")
    w("")
    w("| file | sha256 | asserted against | tracked at HEAD |")
    w("|---|---|---|---|")
    for e in [m["note"]] + m["svgs"]:
        w("| `%s` | `%s` | %s (%s): PASS | %s |" % (e["path"], e["sha256"], e["expected"], e["expected_source"],
                                                   "yes" if e["tracked_at_head"] else "no (untracked)"))
    w("")
    if not all(e["tracked_at_head"] for e in [m["note"]] + m["svgs"]):
        w("- Untracked at this run. N1 final's first condition on the tag (§9g) is that the tag commit contains the "
          "note and both SVGs.")
    w("- If the note or either SVG changes before the tag commit, N1 and then N18 must be re-run (see "
      "\"Before the tag commit\" below).")
    w("- %s" % m["footer_note"])
    w("- N1 final (`%s`, run at HEAD `%s`) covers exactly these three sha256s and is not provisional; its note-rows file "
      "`%s` is unchanged since (sha256 `%s`)." % (n1["ledger_json"], short(n1["ledger_head_at_run"]), n1["note_rows_file"],
                                                  n1["note_rows_file_sha256"]))
    w("- **Figures commit (N1 final):** `%s` (%s), set by %s. Basis: %s. Ancestor of HEAD at this run: %s. N1's "
      "record-sources-only candidate, as N1 states it: `%s` (%s)." % (
          n1["figures_commit"], n1["figures_commit_date"], ", ".join(n1["figures_commit_set_by_rows"]),
          n1["figures_commit_basis"], "yes" if n1["figures_commit_is_ancestor_of_head_at_this_run"] else "NO",
          short(n1["record_sources_only_candidate"], 7), n1["record_sources_only_candidate_date"]))
    w("- The N1 script's sha256 now %s the one the ledger records (`%s`)." % (
        "equals" if n1["n1_script_unchanged_since_ledger"] else "DIFFERS FROM", short(n1["n1_script_sha256_in_ledger"], 16)))
    w("")
    w("## Preprint")
    w("")
    if pp.get("sha256") is None:
        w("- `%s`: **%s** (sha256 null). %s" % (
            pp["path"], pp["status"],
            "The file on disk equals the block's reference %s." % pp["block_reference"]
            if pp.get("on_disk_matches_block_reference") else ""))
    else:
        w("- `%s`: sha256 `%s`; %s (reference %s)." % (pp["path"], pp["sha256"], pp["status"], pp["block_reference"]))
        if pp.get("pi_confirmation"):
            w("- PI confirmation: %s." % pp["pi_confirmation"])
    w("- Routing: %s. %s" % (pp["routing"], pp["rerun_trigger"]))
    w("")
    w("## N13 provenance table: version content sha256 per row")
    w("")
    w("Read from `%s` (sha256 `%s`; working tree equal: %s). %d rows: %d file rows (re-hash: %d match, %d mismatch, %d "
      "not re-hashed) and %d log-entry rows (%s), which are not re-hashed. content_sha256, its status and the row status "
      "are N13's, verbatim in the JSON. The last column is this run's re-hash of `git show <record commit>:<document>`." % (
          n13["source"], n13["source_sha256_at_pin"], "yes" if n13["working_tree_equal"] else "NO", n13["n_rows"],
          n13["n_file_rows"], n13["n_file_rows_rehash_match"], n13["n_file_rows_rehash_mismatch"],
          n13["n_file_rows_not_rehashed"], n13["n_log_entry_rows"], ", ".join(n13["log_entry_row_ids"])))
    w("")
    w("| row | document | record commit | content sha256 | N13 sha status (abbrev.) | re-hash |")
    w("|---|---|---|---|---|---|")
    for r in n13["rows"]:
        st = r["content_sha256_status"].split(" (")[0]
        rh = "log entry: not re-hashed" if r["rehash_at_run"].startswith("not re-hashed (a log-entry") else r["rehash_at_run"]
        w("| %s | `%s` | `%s` | `%s` | %s | %s |" % (r["id"], r["document"], r["record_commit"][:7], r["content_sha256"],
                                                   st, rh))
    w("")
    w("## Files at this run")
    w("")
    for wc in m["wait_check"]:
        w("- Wait check: `%s` last modified %s (local date %s; today %s): %s." % (
            wc["path"], wc["mtime_utc"], wc["mtime_local_date"], wc["local_date_at_run"], wc["reading"]))
    fl = m["files"]
    w("- %d files (%s). Excluded: %s." % (fl["n_files"], fl["rule"],
                                         ", ".join("`%s`" % p for p in fl["excluded_self"])))
    w("- Digest of the list: `%s` (%s)." % (fl["sha256sum_list_sha256"], fl["sha256sum_list_recipe"]))
    w("- Tracked at HEAD: %d of %d; equal to HEAD: %d. Files untracked or changed since HEAD are hashed as they "
      "stand; any change to a listed file before the tag commit requires a re-run." % (
          fl["n_tracked_at_head"], fl["n_files"], fl["n_equal_to_head"]))
    w("")
    w("The named files and N1's final outputs, and every listed file that is untracked or differs from HEAD (the full "
      "list with sha256s is in the JSON, `files.list`):")
    w("")
    w("| file | sha256 | at HEAD |")
    w("|---|---|---|")
    for f in fl["list"]:
        st = "untracked" if not f["tracked_at_head"] else ("equal" if f["equal_to_head"] else "modified")
        if f["category"] in ("named", "N1 final ledger") or st != "equal" or f["path"].endswith("N1-note-rows.json"):
            w("| `%s` | `%s` | %s |" % (f["path"], f["sha256"], st))
    w("")
    w("## Before the tag commit")
    w("")
    w(m["rerun_rule"])
    w("")
    for i, t in enumerate(m["rerun_triggers"], 1):
        w("%d. If %s: re-run %s." % (i, t["trigger"], t["rerun"]))
    w("")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--note", default=NOTE)
    ap.add_argument("--svg", action="append")
    ap.add_argument("--expect", action="append")
    ap.add_argument("--ledger", default=LEDGER)
    ap.add_argument("--preprint-pi-confirmed", default=None, metavar="SHA256")
    a = ap.parse_args()
    if a.svg is None:
        a.svg = list(SVGS)
    stamp = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%S UTC"], capture_output=True, text=True).stdout.strip()
    try:
        m, out_json, out_md, mism = build(a, stamp)
    except Stop as e:
        print("STOP: %s" % e)
        return 2
    # Render both outputs before opening either file.
    json_text = json.dumps(m, indent=1, ensure_ascii=False) + "\n"
    md_text = render_md(m)
    with open(abs_(out_json), "w", encoding="utf-8") as fh:
        fh.write(json_text)
    with open(abs_(out_md), "w", encoding="utf-8") as fh:
        fh.write(md_text)
    print("wrote %s and %s: note %s, figures commit %s, %d N13 rows (%d file rows, %d re-hash mismatches; %d log-entry "
          "rows), preprint %s, %d files" % (
              out_json, out_md, m["note"]["sha256"][:12], m["n1"]["figures_commit"][:7], m["n13"]["n_rows"],
              m["n13"]["n_file_rows"], len(mism), m["n13"]["n_log_entry_rows"], m["preprint"]["status"],
              m["files"]["n_files"]))
    if mism:
        print("N13 RE-HASH MISMATCH (outputs written, exit 1): %s" % ", ".join(mism))
    return 1 if mism else 0


if __name__ == "__main__":
    sys.exit(main())
