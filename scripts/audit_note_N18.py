#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N18: hashes for the note (the release manifest).

Block :132-133 asks for the sha256 of the final note and the tag commit hash, both for the
note's footer, and a `results/raw/<stamp>_note-release-manifest.json` with the tag, the note
sha and the N13 table's shas. This script writes that JSON and a short .md beside it:

  - the tag name (the PI's routing of 2026-10-09, item 7) and the self-reference statement:
    the tag goes on the commit that adds this manifest, so that commit's hash cannot be
    inside it; it is to be recorded after tagging;
  - the note and its SVGs, each sha256 asserted against the routed value;
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

Round 2 (2026-10-10, after the PI's rulings of 2026-10-09): the note is v0.4 and the SVGs are
the Digest seat's three 2026-10-09 renders (F1a, F1b, F2), which replace v0.3 and the two
2026-10-06 SVGs at the PI's routing; the N1 ledger read is N1 round 8's
(results/raw/2026-10-09_note-N1-v0_4-claims-ledger.json); the file list also names e2a's
correction of record beside its analysis (data/e2a/analysis.correction-of-record.json). The
PI routed the note's full sha256; no sha256 was routed for the SVGs, so their expected values are
the full sha256s of the copies Code placed at root on 2026-10-09, which N1 round 8 records.

Round 3 (2026-10-11, N1 round 9): the note is v0.5 and the SVGs are the Digest seat's
2026-10-10 renders, which replace the 2026-10-09 ones; the PI routed all four full sha256s on
2026-10-10. The N1 ledger read is round 9's (results/raw/2026-10-10_note-N1-v0_5-claims-ledger.json).
Patch v6 is applied: the PI's ruling 9 of 2026-10-10 (as corrected) names the preprint's sha256
0f4ba501d60a94189e6dc83d28c41826debe50591b9af484fa08d05a41f16c22, passed as --preprint-pi-confirmed.
Each render carries a C2PA content-credentials element; this script hashes the files whole.

Round 4 (2026-10-12, N1 round 10): the note is v0.6, whose full sha256 the PI routed on
2026-10-12; the three 2026-10-10 renders are unchanged (the same routing). The N1 ledger read is
round 10's (results/raw/2026-10-12_note-N1-v0_6-claims-ledger.json). Patch v7 is the preprint of
record: the PI's routing of 2026-10-12 gives its sha256
d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6, passed as --preprint-pi-confirmed;
patch v6 (0f4ba501...6c22) is archived untracked at archive/PREPRINT-v1_0-draft.pre-patch-v7.md,
out of the release.

Round 5 (2026-11-03, N1 round 11; release v2): the tag is note-2026-10-v2, in place of round 1's
note-2026-10-v1 and its source (TAG_SOURCE; round 1's tag is TAG_V1, read for the pointer to v1's
manifest). The note is v0.8 (RESEARCH-NOTE-v0_8-draft.md), filed at 0de15a1; its full sha256 is the one
the design seat's answers of 2026-10-28 state, on the line where the seat also says NOTE "moves to v0.8
with the README-NOTE re-point"
(results/raw/2026-10-28_note-design-to-code_release-block-answers.md@908a659:21). Code's reading: NOTE
moves at N18's item-4 run, before the re-point, because the v0.6 text left the tree at dc8c028 (the same
line). The figures are the three 2026-10-22 renders, filed at 0a3f925, whose sha256s the release block of
2026-10-27 gives abbreviated (results/raw/2026-10-27_note-design-to-code_release-block.md@2fb0cf0:11), as
ROUTED holds them; each of the four files is asserted equal to its blob at the commit that filed it
(FILED). The 2026-10-10 renders stay in the tree beside them (the same line) and are not hashed here. The
N1 ledger read is round 11's (results/raw/2026-11-02_note-N1-v0_8-claims-ledger.json, committed at
979700f; its W3/O3 sentence corrected at 87cbd82). The preprint is patch v8 under the status banner
committed at 32aefcc, which the answers call "not a text of record" (908a659:61); its sha256 is the
release block's (2fb0cf0:10, :40), passed as --preprint-pi-confirmed and asserted equal to
PREPRINT_ROUTED, to the file on disk and to the file's blob at 32aefcc, whose parent's blob matches the
block's pre-banner sha256 and is the text below the banner. The preprint's status texts, the tag's commit
statement, the footer note and the re-run triggers are restated for v2 (round 1's 'pending patch v6'
status for the block's post-patch-v4 copy now says that copy is not the file the tag is to hold). The
figures commit's basis is read from N1's entries (note_rows_final.entries, .tag.audit_only_rows) in place
of the fixed wording of rounds 1-4 (round 2's "N19's, N2 round 6's", which replaced round 1's "N19's
raw"), and three lines of the .md are corrected: the N1 coverage line counts the SVGs (round 1's "these
three sha256s" predates F1a, added in round 2), the files table shows the note-rows file the N1 ledger
read (rounds 2-4 matched only round 1's by name), and the tracking line's "is that" becomes "includes
that" (N1's first condition on the tag also names the preprint, as round 4's did). README.md (in the tree
since dae2edc; edited at f5a580d, which the release block lists as "new `README.md` (pointer to
README-NOTE and the tag" (2fb0cf0:9), and again at f935864) is a named file from this round, and it and
the preflip script join the wait check: Code's additions, since the order edits both before N18's second
run. N18 runs twice (908a659:65-66; the design seat's answers of 2026-11-02,
results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1:60): at item 4, after the round-11
ledger commit, and again as the last commit before the tag, after the README-NOTE re-point, the PI's
README.md pass (if not yet done) and the preflip-script commit, each of which changes a listed file; the
default run regenerates this manifest in place, and the tag commit holds the second run's. The note is
frozen as posted (908a659:23), so no footer carries the hashes; the tag commit is to be recorded after
tagging in a post-tag raw, as v1's was (Code's procedure;
results/raw/2026-10-12_note-release-tag.md@11cc35b:5; the answers name "the post-tag raw" for the counts
of the password search and gitleaks re-run at the tag commit, 908a659:46), and in POST-note, the design
seat's (908a659:68). Every line cited for a round-5 constant or text is asserted at the run to carry the
words quoted or relied on (SOURCES).
The repository is the script's parent's parent, as before; a copy of the script outside any git work
tree (a test copy) reads the current directory's work tree instead, and the manifest records which
applied.

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

--preprint-pi-confirmed records, for a re-run after a patch arrives, that the PI has
confirmed (routed) the preprint on disk as the text of record (round 4: patch v7). It takes the full sha256, which must
equal the file on disk and must differ from the block's post-patch-v4 reference. The script
cannot see the confirmation itself: the manifest says the value was supplied on the command
line as the PI's confirmation, and records the command. Round 5: the value is the one the
release block of 2026-10-27 gives for the file the tag is to hold, patch v8 under its status
banner, which is not a text of record; the script asserts that the value equals
PREPRINT_ROUTED, the value on that block's lines 10 and 40, and the manifest records it as
that routed sha256, not as a confirmation of a text of record.
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

def _work_tree(p):
    """The git work tree that holds directory p (p or its nearest ancestor with a .git entry), or None."""
    p = os.path.abspath(p)
    while not os.path.exists(os.path.join(p, ".git")):
        if os.path.dirname(p) == p:
            return None
        p = os.path.dirname(p)
    return p


# The repository is the script's parent's parent, as before. Round 5: a copy of this script outside any git work tree
# (a test copy) reads the work tree of the current directory instead; the manifest records which applied (root_from).
_HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _work_tree(_HOME) is not None:
    ROOT, ROOT_FROM = _HOME, "the directory two levels above the script (its parent's parent), as in rounds 1-4"
else:
    ROOT, ROOT_FROM = _work_tree(os.getcwd()), ("the git work tree of the current directory (the script ran from a "
                                                "copy outside any git work tree)")
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_PIN = "bbc9ffe"
AUDIT_PIN = "09c3a8c"
# The block's sha256 as abbreviated in its placing commit's message (bbc9ffe: "sha256 8cd8a9ac...3841").
BLOCK_ROUTED = ("8cd8a9ac", "3841")
N18_LINES = (132, 133)
# Round 5 (release v2): the design seat's three committed blocks this round cites, each read at the commit that added
# it (all three are titled "routed by the PI"), and v1's post-tag raw (its :5 records v1's tag commit and its :21 the
# sha256 of v1's manifest), read for the pointer to v1's manifest.
RB = ("results/raw/2026-10-27_note-design-to-code_release-block.md", "2fb0cf0")      # the release block, 2026-10-27
ANS = ("results/raw/2026-10-28_note-design-to-code_release-block-answers.md", "908a659")   # the answers, 2026-10-28
SEAT = ("results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md", "da50cd1")    # the seat's answers, 2026-11-02
TAGRAW_V1 = ("results/raw/2026-10-12_note-release-tag.md", "11cc35b")                 # v1's post-tag raw
TAG = "note-2026-10-v2"
# Round 5: the release block's item 7 and tag URL, the answers of 2026-10-28 and the seat's answers of 2026-11-02, each
# line asserted at the run (SOURCES). Round 1's source, replaced: "the PI's routing of 2026-10-09, item (7), as routed
# to Code: tag name note-2026-10-v1, placed on the final audit commit after N1 and N18; the block leaves the name to
# the PI and suggests it at AUDIT-note-release-v1_2.md@bbc9ffe:14".
TAG_SOURCE = ("the release block of 2026-10-27 (the design seat's, routed by the PI): its item 7 places the tag "
              "note-2026-10-v2 on the final audit commit (%s@%s:47), and the note's repository link is the tag URL "
              "that ends in that name (:23); the design seat's answers of 2026-10-28, under the PI's \"Yes to all\" "
              "(%s@%s:7): \"The tag commit is the last audit commit, which is the second N18.\" (:66); and the design "
              "seat's answers of 2026-11-02: the tag \"must be `note-2026-10-v2` exactly\" (%s@%s:51)" % (RB + ANS + SEAT))
TAG_V1 = "note-2026-10-v1"   # release v1's tag (rounds 1-4): the pointer to v1's manifest is read at its commit
NOTE = "RESEARCH-NOTE-v0_8-draft.md"
SVGS = ["2026-10-22_F1a_headline-strip.svg", "2026-10-22_F1b_five-link-panels.svg",
        "2026-10-22_F2_macar-lineage-roc_post.svg"]
# Routed values (round 5): the note's full sha256 as the design seat's answers of 2026-10-28 state it (908a659:21); the
# SVGs' abbreviated, as the release block of 2026-10-27 gives them (2fb0cf0:11). Each is also checked against the N1
# final ledger's note_rows_final.files[].routed, and each file against its blob at the commit that filed it (FILED).
ROUTED = {
    NOTE: ("6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d", "",
           "the design seat's answers of 2026-10-28, which give the full sha256 (%s@%s:21)" % ANS),
    SVGS[0]: ("f0c1cd73", "5bfc", "the release block of 2026-10-27, which gives the filed copy's sha256 abbreviated "
                                  "(%s@%s:11)" % RB),
    SVGS[1]: ("640c13e8", "33af", "the release block of 2026-10-27, which gives the filed copy's sha256 abbreviated "
                                  "(%s@%s:11)" % RB),
    SVGS[2]: ("0e0459cf", "69bc", "the release block of 2026-10-27, which gives the filed copy's sha256 abbreviated "
                                  "(%s@%s:11)" % RB),
}
# The commit that filed each file at the root (round 5): the note at 0de15a1 (908a659:21), the SVGs at 0a3f925
# (2fb0cf0:11). Each file on disk is asserted equal to its blob there, and that blob to the routed value.
FILED = {NOTE: "0de15a1", SVGS[0]: "0a3f925", SVGS[1]: "0a3f925", SVGS[2]: "0a3f925"}
LEDGER = "results/raw/2026-11-02_note-N1-v0_8-claims-ledger.json"   # round 5: N1 round 11's, at 979700f and 87cbd82
N13_JSON = "results/raw/2026-10-08_note-N13-provenance.json"
PREPRINT = "PREPRINT-v1_0-draft.md"
PREPRINT_REF = ("d6431e97", "222b8")  # block :21, "post-patch-v4 copy, sha `d6431e97…222b8`"
# Round 5: the sha256 of the file the tag is to hold, patch v8 under its status banner (the release block, 2fb0cf0:10
# and :40), which is not a text of record (908a659:61); the banner's commit and the pre-banner sha256 as the block
# abbreviates it (2fb0cf0:10)
PREPRINT_ROUTED = "5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467"
PREPRINT_BANNER = ("32aefcc", ("45b67246", "7a41"))
# Round 5: README.md (in the tree since dae2edc; edited at f5a580d, which the release block lists as "new `README.md`
# (pointer to README-NOTE and the tag", 2fb0cf0:9, and again at f935864), which the PI's README.md pass edits before
# N18's second run (da50cd1:60), is named (Code's addition)
NAMED_FILES = ["README-NOTE.md", "README.md", "LICENSE", "LICENSE-CC-BY-4.0", "LICENSING.md",
               "data/e2a/analysis.correction-of-record.json"]
# Round 5: README.md (the PI's pass) and the preflip script (its commit) join the wait check, since the order edits
# both before N18's second run (da50cd1:60; Code's addition)
WAIT_FILES = ["README-NOTE.md", "README.md", "scripts/audit_note_N12_preflip.py",
              "results/raw/2026-10-08_note-N12-scrub.md"]
DEFAULT_OUT = "results/raw/2026-10-09_note-release-manifest.json"
# Round 5: every line cited for a round-5 constant or text, with the words this script quotes or relies on; each is
# asserted present in its line at the run (a mismatch is a STOP), and the manifest lists them (sources)
SOURCES = [
    (RB, 1, ["Design → Code — the release block, posting day (note arc; 2026-10-27, routed by the PI)"]),
    (RB, 9, ["`f5a580d`", "new `README.md` (pointer to README-NOTE and the tag"]),
    (RB, 10, ["`32aefcc`", "`PREPRINT-v1_0-draft.md` status banner. Patch v8 text unchanged beneath it",
              "pre-banner sha256 `45b67246…7a41`", "post-banner `%s`" % PREPRINT_ROUTED, "N18 reads the new sha256."]),
    (RB, 11, ["`0a3f925`", "The three 2026-10-22 SVGs at the root beside the 2026-10-10 set.",
              "F1a `f0c1cd73…5bfc`", "F1b `640c13e8…33af`", "F2 `0e0459cf…69bc`"]),
    (RB, 23, ["The note's repository link is the tag URL: `https://github.com/jasondwyer/told-vs-felt/tree/%s`" % TAG]),
    (RB, 40, ["**N18** release manifest after the v0.8 commit, with `--preprint-pi-confirmed %s`" % PREPRINT_ROUTED]),
    (RB, 47, ["**Tag `%s`** on the final audit commit" % TAG]),
    (ANS, 1, ["Design → Code — answers to the release-block questions (note arc; 2026-10-28, routed by the PI)"]),
    (ANS, 7, ["**The PI's answer, verbatim: \"Yes to all\".**"]),
    (ANS, 21, ["`scripts/audit_note_N18.py:93` `NOTE = \"RESEARCH-NOTE-v0_6-draft.md\"` moves to v0.8 with the "
               "README-NOTE re-point", "`dc8c028` (the scratch notebook and the v0.6 note text removed from the tree",
               "`0de15a1` (`%s` at the root, sha256 `%s`" % (NOTE, ROUTED[NOTE][0])]),
    (ANS, 23, ["v0.8 does not change again before the tag"]),
    (ANS, 46, ["At the tag commit, before the push, re-run the password search and gitleaks",
               "record their counts in the post-tag raw"]),
    (ANS, 61, ["reads patch v7, `d9635ca2…1fe6`, which `note-2026-10-v1` holds",
               "the file at the tag is patch v8 under a status banner (`5d677a72…4467`, N18) and is not a text of "
               "record"]),
    (ANS, 65, ["**N18** at item 4 as the block orders, and **again as the last commit before the tag**"]),
    (ANS, 66, ["The tag commit is the last audit commit, which is the second N18."]),
    (ANS, 68, ["its refresh (the v0.8 sha256, the tag commit, the tag URL; the pinned-comment text) is the seat's, "
               "after the tag"]),
    (SEAT, 1, ["Design → Code — N1 round 11: the seat's answers in one block (note arc; 2026-11-02, routed by the PI)"]),
    (SEAT, 49, ["the renders posted as filed"]),
    (SEAT, 51, ["must be `%s` exactly" % TAG]),
    (SEAT, 60, ["N18 (item 4) → README-NOTE re-point", "**the PI's README.md pass, if not yet done**",
                "the preflip-script commit → N18 again → tag → push"]),
    (TAGRAW_V1, 5, ["- **The tag commit (R2): `"]),
    (TAGRAW_V1, 21, ["| `%s` | `" % DEFAULT_OUT]),
]


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
    need(ROOT is not None, "this copy of the script is outside any git work tree and so is the current directory")
    out_json = a.out
    out_md = re.sub(r"\.json$", ".md", out_json)
    need(out_md != out_json, "--out must end in .json")
    head = git("rev-parse", "HEAD").strip()
    branch = git("symbolic-ref", "-q", "--short", "HEAD", check=False).stdout.decode().strip() or None
    expect = parse_expect(a.expect)
    if a.preprint_pi_confirmed is not None:
        need(re.fullmatch(r"[0-9a-f]{64}", a.preprint_pi_confirmed) is not None,
             "--preprint-pi-confirmed: a full 64-hex sha256 is required")

    # --- round 5: the lines cited for round 5's constants and texts, each read at the commit that added it --------
    src_lines = {}
    sources = []
    for (spath, srev), sln, frags in SOURCES:
        if (spath, srev) not in src_lines:
            anc_s = git("merge-base", "--is-ancestor", srev, "HEAD", check=False).returncode
            need(anc_s == 0, "%s is not an ancestor of HEAD (%s)" % (srev, spath))
            src_lines[(spath, srev)] = git("show", "%s:%s" % (srev, spath), binary=True).decode("utf-8").splitlines()
        sl = src_lines[(spath, srev)]
        need(1 <= sln <= len(sl), "%s@%s has no line %d" % (spath, srev, sln))
        for f in frags:
            need(f in sl[sln - 1], "%s@%s:%d does not carry %r" % (spath, srev, sln, f))
        sources.append({"locator": "%s@%s:%d" % (spath, srev, sln), "words": frags, "present": True})

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
            ok, how = matches_routed(sha, ROUTED[p]), ROUTED[p][2]
            routed = ROUTED[p][0] if not ROUTED[p][1] else "%s...%s" % ROUTED[p][:2]   # a full routed value prints whole
        need(ok, "%s sha256 %s does not match the expected %s (%s)" % (p, sha, routed, how))
        filed = FILED.get(p) if p not in expect else None
        if filed is not None:   # round 5: the file as filed at the root, at the commit FILED names
            fsha = sha256_bytes(git("show", "%s:%s" % (filed, p), binary=True))
            need(fsha == sha, "%s on disk (%s) differs from its blob at %s (%s), where it was filed" % (p, sha, filed, fsha))
        e = file_entry(p, nb, "note" if p == a.note else "svg")
        e.update({"expected": routed, "expected_source": how, "assert": "PASS",
                  "filed_at": filed, "equal_to_filed_blob": True if filed is not None else None})
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
            need(f["routed"] in ("%s...%s" % r[:2], r[0]) or matches_routed(f["routed"], r),
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
    # round 5: the audit raws the figures that set the commit enter with, and the figures that are not computed-new
    # and whose only carrier is an audit raw committed after the audit pin, read from N1's own entries
    # (note_rows_final.entries; .tag.audit_only_rows), not fixed wording
    ent = {x["row"]: x for x in led["note_rows_final"].get("entries", [])}
    carriers = sorted(set(((ent.get(r) or {}).get("audit_locator") or "").split(":")[0] or "(no audit locator)"
                          for r in figs["rows"]))
    audit_only = [{"row": x["row"], "locator": x.get("locator")} for x in tag.get("audit_only_rows", [])]
    n1 = {
        "ledger_json": led_path, "ledger_md": led_md,
        "ledger_head_at_run": led.get("head_at_run"), "ledger_code_stamp_utc": led.get("code_stamp_utc"),
        "provisional": led.get("provisional"),
        "covers_note_sha256_of_this_run": True, "covers_svg_sha256s_of_this_run": True,
        "note_rows_file": ff["rows_file"], "note_rows_file_sha256": rows_sha,
        "figures_commit": figs["commit"], "figures_commit_date": figs["date"],
        "figures_commit_set_by_rows": figs["rows"],
        "figures_commit_basis": ("N1 final, note_rows_final.tag.including_audit_raws (N1's rule, its section 9g: over "
                                 "the note's figures, the latest entry, a computed-new figure entering with the audit "
                                 "raw it cites and a figure whose only carrier is an audit raw committed after the "
                                 "audit pin with that raw); the figures that set it enter with %s, by N1's entries; the "
                                 "figures that are not computed-new and whose only carrier is an audit raw committed "
                                 "after the audit pin, by N1's .tag.audit_only_rows: %s; stated plainly at %s:%d (the "
                                 "file as read at this run)" % (
                                     ", ".join(carriers),
                                     ", ".join("%s (%s)" % (x["row"], x["locator"]) for x in audit_only) or "none",
                                     led_md, plain_line)),
        "figures_commit_audit_raws": carriers,
        "audit_only_rows": audit_only,
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
    if pconf is not None:   # round 5: the value is the release block's, for patch v8 under its status banner
        need(pconf == PREPRINT_ROUTED, "--preprint-pi-confirmed %s is not the value the release block gives (%s, "
                                       "%s@%s:10, :40); a new routing needs its own PREPRINT_ROUTED and source" % (
                                           (pconf, PREPRINT_ROUTED) + RB))
    pp_routing = ("the release block of 2026-10-27 (the design seat's, routed by the PI) gives the sha256 of the file the "
                  "tag is to hold, patch v8 under the status banner committed at %s (\"Patch v8 text unchanged beneath "
                  "it\"; \"N18 reads the new sha256.\", %s@%s:10), and runs N18 \"with `--preprint-pi-confirmed %s`\" "
                  "(:40); the design seat's answers of 2026-10-28, under the PI's \"Yes to all\": \"the file at the tag "
                  "is patch v8 under a status banner (`5d677a72…4467`, N18) and is not a text of record\" (%s@%s:61); "
                  "patch v7, round 4's preprint of record, is the file the tag note-2026-10-v1 holds, where Tier 1 "
                  "reads it (the same line)" % ((PREPRINT_BANNER[0],) + RB + (PREPRINT_ROUTED,) + ANS))
    # round 5: the banner commit, read from history whatever is on disk: its blob is the routed value, and its
    # parent's blob carries the block's pre-banner sha256 and is the text below the banner, unchanged
    ban_rev, pre_ref = PREPRINT_BANNER
    ban_txt = git("show", "%s:%s" % (ban_rev, PREPRINT), binary=True)
    par_txt = git("show", "%s^:%s" % (ban_rev, PREPRINT), binary=True)
    ban_sha, par_sha = sha256_bytes(ban_txt), sha256_bytes(par_txt)
    need(ban_sha == PREPRINT_ROUTED, "%s at %s has sha256 %s, not the release block's %s" % (
        PREPRINT, ban_rev, ban_sha, PREPRINT_ROUTED))
    need(matches_routed(par_sha, pre_ref), "%s at %s^ has sha256 %s, not the block's pre-banner %s...%s" % (
        (PREPRINT, ban_rev, par_sha) + pre_ref))
    need(len(ban_txt) > len(par_txt) and ban_txt.endswith(par_txt),
         "%s at %s is not its parent's text with lines added above it" % (PREPRINT, ban_rev))
    banner = {"commit": ban_rev, "sha256_at_commit": ban_sha, "parent_sha256": par_sha,
              "parent_matches_block_pre_banner": True, "block_pre_banner": "%s…%s" % pre_ref,
              "text_below_banner_equals_parent": True, "banner_bytes": len(ban_txt) - len(par_txt),
              "source": "%s@%s:10" % RB}
    if os.path.isfile(abs_(PREPRINT)):
        ps = sha256_file(abs_(PREPRINT))
        bref = "%s…%s (post-patch-v4 copy), AUDIT-note-release-v1_2.md@%s:%d" % (
            PREPRINT_REF[0], PREPRINT_REF[1], BLOCK_PIN, pref_line[0])
        if matches_routed(ps, PREPRINT_REF):
            need(pconf is None, "--preprint-pi-confirmed given, but %s on disk is still the block's post-patch-v4 "
                                "reference %s...%s" % ((PREPRINT,) + PREPRINT_REF))
            preprint = {"path": PREPRINT, "status": ("the block's post-patch-v4 copy, not the file the tag is to hold "
                                                     "(patch v8 under its status banner, %s@%s:10)" % RB),
                        "sha256": None, "on_disk_matches_block_reference": True, "block_reference": bref,
                        "pi_confirmation": None}
        elif pconf is not None:
            need(pconf == ps, "--preprint-pi-confirmed %s does not equal %s on disk (%s)" % (pconf, PREPRINT, ps))
            preprint = {"path": PREPRINT,
                        "status": ("patch v8 under its status banner (committed at %s): the file the tag is to hold, "
                                   "which is not a text of record; its sha256 is the release block's, supplied to this "
                                   "run with --preprint-pi-confirmed (see pi_confirmation)" % ban_rev),
                        "sha256": ps, "on_disk_matches_block_reference": False, "block_reference": bref,
                        "pi_confirmation": ("the full sha256 was supplied on the command line with "
                                            "--preprint-pi-confirmed; the script asserted that it equals the value the "
                                            "release block of 2026-10-27 gives for the file the tag is to hold (%s@%s:10, "
                                            ":40), the file on disk and the file's blob at %s. It records that routed "
                                            "value, not a confirmation of a text of record (the command is recorded in "
                                            "`command`)" % (RB + (ban_rev,)))}
        else:
            preprint = {"path": PREPRINT, "status": ("differs from the block's post-patch-v4 reference; no sha256 was "
                                                     "supplied with --preprint-pi-confirmed, so this run does not "
                                                     "assert the file on disk against the release block's value for "
                                                     "the file the tag is to hold (%s@%s:10, :40); "
                                                     "equal_to_banner_commit_blob records whether the file on disk "
                                                     "equals the banner commit's blob, whose sha256 is that value" % RB),
                        "sha256": ps, "on_disk_matches_block_reference": False, "block_reference": bref,
                        "pi_confirmation": None}
        preprint["tracked_at_head"] = bool(head_blobs([PREPRINT]))
        preprint["equal_to_banner_commit_blob"] = ps == ban_sha
    else:
        need(pconf is None, "--preprint-pi-confirmed given, but %s is not on disk" % PREPRINT)
        preprint = {"path": PREPRINT, "status": ("not on disk (the tag is to hold patch v8 under its status banner, "
                                                 "%s@%s:10)" % RB), "sha256": None,
                    "pi_confirmation": None}
    preprint["banner"] = banner
    preprint["routing"] = pp_routing
    preprint["rerun_trigger"] = ("If the file changes after this run and before the tag "
                                 "commit, N18 must be re-run: this section describes the file as found at this run, and "
                                 "the tag commit is to hold patch v8 under its status banner, sha256 %s (%s@%s:10, :40), "
                                 "which is not a text of record (%s@%s:61)." % ((PREPRINT_ROUTED,) + RB + ANS))

    # --- wait check ----------------------------------------------------------------------------------
    today = datetime.date.today().isoformat()
    waits = []
    for p in WAIT_FILES:
        need(os.path.isfile(abs_(p)), "%s is not on disk" % p)
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
    # round 5: release v1's tag and its manifest (this script's default output as committed at that tag's commit),
    # beside v1's post-tag raw's record of both; read and reported, not asserted
    t1 = git("rev-parse", "-q", "--verify", "refs/tags/%s^{commit}" % TAG_V1, check=False)
    v1c = t1.stdout.decode().strip() if t1.returncode == 0 else None
    raw1 = git("show", "%s:%s" % (TAGRAW_V1[1], TAGRAW_V1[0]), binary=True).decode("utf-8").splitlines()
    v1man = None
    if v1c is not None and git("cat-file", "-e", "%s:%s" % (v1c, DEFAULT_OUT), check=False).returncode == 0:
        v1man = sha256_bytes(git("show", "%s:%s" % (v1c, DEFAULT_OUT), binary=True))
    previous = {
        "name": TAG_V1, "exists_at_run": v1c is not None, "points_to": v1c,
        "manifest": DEFAULT_OUT, "manifest_sha256_at_that_commit": v1man,
        "post_tag_raw": "%s@%s" % TAGRAW_V1,
        "post_tag_raw_line_5_records_this_commit": v1c is not None and len(raw1) >= 5 and "`%s`" % v1c in raw1[4],
        "post_tag_raw_line_21_records_this_sha256": (v1man is not None and len(raw1) >= 21
                                                     and "`%s`" % DEFAULT_OUT in raw1[20] and "`%s`" % v1man in raw1[20]),
        "statement": ("Release v1's manifest is this script's default output as committed at the commit of %s; a run "
                      "at the default output regenerates that file in place, and v1's manifest stays readable at that "
                      "commit (v1's post-tag raw, %s@%s, records the commit at :5 and the file's sha256 at :21)." % (
                          (TAG_V1,) + TAGRAW_V1)),
    }
    readme_clause = (", as does the PI's README.md pass (README.md is a named file)"
                     if "README.md" in NAMED_FILES else "")

    script_rel = os.path.relpath(os.path.abspath(__file__), ROOT)
    manifest = {
        "item": "N18", "title": "release manifest (hashes for the note)",
        "round": "5 (2026-11-03, N1 round 11; release v2)",
        "code_stamp_utc": stamp, "head_at_run": head, "branch_at_run": branch,
        "block": BLOCK, "block_sha256": block_sha,
        "block_sha256_routed": "%s...%s" % BLOCK_ROUTED, "block_sha256_matches_routed": True,
        "block_equal_to_committed_at": BLOCK_PIN,
        "block_n18_lines": list(N18_LINES),
        "script": script_rel, "script_sha256": sha256_file(os.path.abspath(__file__)),
        "root_from": ROOT_FROM,
        "interpreter": sys.executable, "python": sys.version.split()[0],
        "command": " ".join([sys.executable] + sys.argv),
        "sources": {
            "rule": ("every line this script cites for a round-5 constant or text, read at the commit that added it "
                     "(an ancestor of HEAD), with the words it quotes or relies on; each is asserted present in its "
                     "line at this run"),
            "lines": sources,
        },
        "tag": {
            "name": TAG, "source": TAG_SOURCE, "state_at_run": tag_state,
            "commit": None,
            "commit_statement": ("The tag goes on the final audit commit, the commit of N18's second run: \"The tag commit is "
                                 "the last audit commit, which is the second N18.\" (%s@%s:66). A commit's hash is "
                                 "computed over a tree that contains this file, so the hash cannot be written inside it "
                                 "(self-reference). It is to be recorded after tagging: in a post-tag raw, as v1's was "
                                 "(Code's procedure; %s@%s:5; the answers name \"the post-tag raw\" for the counts of "
                                 "the password search and gitleaks re-run at the tag commit, %s@%s:46), and in "
                                 "POST-note, whose refresh (the v0.8 sha256, the tag commit, the tag URL) is the design "
                                 "seat's, after the tag (%s@%s:68)." % (ANS + TAGRAW_V1 + ANS + ANS)),
            "expected_parent_note": ("HEAD at this run is %s; the tag commit descends from it if the manifest is "
                                     "committed on top of it, which this script does not check." % head),
            "previous": previous,
        },
        "note": notes[0],
        "svgs": notes[1:],
        "rerun_rule": ("This manifest covers only the files as hashed at this run; the tag commit's tree must hold each "
                       "of them at the sha256 recorded here. If any trigger below fires after this run and before the "
                       "tag commit, the named items must be re-run, N18 last. The order runs N18 twice: \"N18 (item 4) "
                       "→ README-NOTE re-point\", then the PI's README.md pass (if not yet done) and \"the "
                       "preflip-script commit → N18 again → tag → push\" (%s@%s:60; %s@%s:65-66). The README-NOTE "
                       "re-point and the preflip-script commit each change a listed file (trigger 3)%s; the second run "
                       "regenerates this manifest in place, and its manifest is the one the tag commit holds." % (
                           SEAT + ANS + (readme_clause,))),
        "rerun_triggers": [
            {"trigger": ("the note or any SVG changes (the note: \"v0.8 does not change again before the tag\", "
                         "%s@%s:23; the renders: \"the renders posted as filed\", %s@%s:49)" % (ANS + SEAT)),
             "rerun": "N1, then N18"},
            {"trigger": ("PREPRINT-v1_0-draft.md changes (the tag is to hold patch v8 under its status banner, sha256 "
                         "%s…%s, the release block's value, %s@%s:10, :40; this manifest records the file as found "
                         "at this run)" % ((PREPRINT_ROUTED[:8], PREPRINT_ROUTED[-4:]) + RB)),
             "rerun": ("N18, with the new file's routed sha256 and its source in PREPRINT_ROUTED, passed as "
                       "--preprint-pi-confirmed")},
            {"trigger": ("any file in files.list changes, is added under results/raw/*_note-* or scripts/audit_note_*.py, "
                         "or is removed (in the order of %s@%s:60: README-NOTE.md at its re-point,%s "
                         "scripts/audit_note_N12_preflip.py at the preflip-script commit; or the N1 final ledger when "
                         "N1 is re-run)" % (SEAT + (" README.md at the PI's pass," if "README.md" in NAMED_FILES
                                                    else "",))),
             "rerun": "N18"},
        ],
        "footer_note": ("The block puts the note's sha256 in the note's footer (:133). A footer inside the hashed file "
                        "changes that file's sha256, so the footer cannot state the hash of the file that contains it. At "
                        "v2 the note carries no footer: it is frozen as posted (\"v0.8 does not change again before the "
                        "tag\", %s@%s:23), and the v0.8 sha256 and the tag commit go to POST-note, the design seat's, "
                        "after the tag (:68 of the same file)." % ANS),
        "n1": n1,
        "n13": n13_out,
        "preprint": preprint,
        "wait_check": waits,
        "files": {
            "rule": ("%s, the N1 final ledger md/json, every "
                     "results/raw/*_note-* file and every scripts/audit_note_*.py on disk at this run, sorted by path; "
                     "this script's own two outputs and any results/raw/*_note-release-manifest.json/.md are excluded "
                     "(a file cannot carry its own hash). tracked_at_head "
                     "and equal_to_head compare the working file's git blob id with HEAD's." % ", ".join(NAMED_FILES)),
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
    w("- Script `%s` sha256 `%s`; interpreter %s (Python %s); repository: %s" % (
        m["script"], m["script_sha256"], m["interpreter"], m["python"], m["root_from"]))
    w("- Round %s. Lines cited for this round's constants and texts, each read at the commit that added it and asserted "
      "at this run to carry the words this script quotes or relies on (the JSON's `sources` gives the words): %s." % (
          m["round"], ", ".join("`%s`" % s["locator"] for s in m["sources"]["lines"])))
    w("- The JSON beside this file is the manifest; this file summarises it.")
    w("")
    w("## Tag")
    w("")
    w("- Name: `%s`. Source: %s." % (m["tag"]["name"], m["tag"]["source"]))
    w("- Tag commit: not in this manifest. %s" % m["tag"]["commit_statement"])
    w("- Tag state at this run: %s." % ("exists, pointing to `%s`" % m["tag"]["state_at_run"]["points_to"]
                                        if m["tag"]["state_at_run"]["exists_at_run"] else "absent"))
    pv = m["tag"]["previous"]
    if pv["exists_at_run"]:
        w("- Release v1: the tag `%s` points to `%s` at this run; v1's manifest, `%s` at that commit, has sha256 `%s`. "
          "v1's post-tag raw `%s` records that commit (:5): %s; and that sha256 (:21): %s. A run at the default "
          "output regenerates that file in place; v1's manifest stays readable at that commit." % (
              pv["name"], pv["points_to"], pv["manifest"], pv["manifest_sha256_at_that_commit"], pv["post_tag_raw"],
              "yes" if pv["post_tag_raw_line_5_records_this_commit"] else "NO",
              "yes" if pv["post_tag_raw_line_21_records_this_sha256"] else "NO"))
    else:
        w("- Release v1: the tag `%s` is absent at this run. %s" % (pv["name"], pv["statement"]))
    w("")
    w("## The note and its figures")
    w("")
    w("| file | sha256 | asserted against | filed at | at HEAD |")
    w("|---|---|---|---|---|")
    for e in [m["note"]] + m["svgs"]:
        w("| `%s` | `%s` | %s (%s): PASS | %s | %s |" % (
            e["path"], e["sha256"], e["expected"], e["expected_source"],
            "`%s` (its blob there is equal)" % e["filed_at"] if e.get("filed_at") else "not checked (no FILED entry)",
            "untracked" if not e["tracked_at_head"] else ("equal" if e["equal_to_head"] else "modified")))
    w("")
    nf = [m["note"]] + m["svgs"]
    if not all(e["tracked_at_head"] for e in nf):
        w("- Untracked at this run. N1 final's first condition on the tag (§9g) includes that the tag commit contains "
          "the note and all %d SVGs." % len(m["svgs"]))
    else:
        w("- Tracked at HEAD at this run (%d of %d equal to HEAD). N1 final's first condition on the tag (§9g) includes "
          "that the tag commit contains the note and all %d SVGs." % (sum(1 for e in nf if e["equal_to_head"]), len(nf),
                                                                       len(m["svgs"])))
    w("- If the note or any SVG changes before the tag commit, N1 and then N18 must be re-run (see "
      "\"Before the tag commit\" below).")
    w("- %s" % m["footer_note"])
    w("- N1 final (`%s`, run at HEAD `%s`) covers exactly the note's and the %d SVGs' sha256s above and is not "
      "provisional; its note-rows file `%s` is unchanged since (sha256 `%s`)." % (
          n1["ledger_json"], short(n1["ledger_head_at_run"]), len(m["svgs"]), n1["note_rows_file"],
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
            w("- The supplied sha256 (--preprint-pi-confirmed): %s." % pp["pi_confirmation"])
    b = pp.get("banner")
    if b:
        w("- The banner commit, read from history: `%s` at `%s` has sha256 `%s` (the release block's value); its "
          "parent's blob has sha256 `%s` (the block's pre-banner value %s: yes) and is the text below the banner, "
          "unchanged (%d bytes added above it; %s).%s" % (
              pp["path"], b["commit"], b["sha256_at_commit"], b["parent_sha256"], b["block_pre_banner"],
              b["banner_bytes"], b["source"],
              (" The file on disk equals that blob: %s." % ("yes" if pp["equal_to_banner_commit_blob"] else "NO"))
              if "equal_to_banner_commit_blob" in pp else ""))
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
        # round 5: N1's note-rows file is the one the ledger read (rounds 2-4 matched only round 1's file by name)
        if f["category"] in ("named", "N1 final ledger") or st != "equal" or f["path"] == n1["note_rows_file"]:
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
