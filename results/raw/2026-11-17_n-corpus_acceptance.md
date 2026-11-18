# n — the corpus's acceptance check and assembly (Code → design, for the seat's adoption read)

PI date 2026-11-17. Code (the n-build session), on the PI's routing of 2026-11-17 ("route as given"), items N.1 and
N.3, relayed by the coordinating session with a battery window. The block's items, verbatim:

> 1. The parts and the prompt record have landed: run the acceptance check as routed; assemble data/n/passages.jsonl in the brief's order (expected 544 lines, 157,520 B, sha256 ef6b00dc56f28678dce0cf7f81b2ae198862e5a83120037cca37f3c8fc533cc3); the check's raw and entry to the seat [go].
> 3. Any finding of the check → a STOP block for the seat, no edit to a part file [as ruled].

The check's terms are §5.3 of `results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md` (routed as
that raw's item 11). The block's header also cites the routing of 2026-11-16, item 12
(`results/raw/2026-11-16_second-sitting_pi-routing.md`): "12. The corpus: data/n holds only bk; its acceptance check
runs when the parts land, as routed on 2026-11-15 [noted]." The prompt record's §5 notes were read before the check
was written. Model-free: no model and no
tokenizer loaded, the standard library only. Nothing under `data/mf3`, `data/*/ckpt` or `data/*/reports` was listed,
opened or hashed. No part file was edited.

**RESULT: every gate PASS (G1–G9); not a STOP.** `data/n/passages.jsonl` is assembled in the brief's order and reads
back as 544 lines, 157,520 bytes, sha256 `ef6b00dc56f28678dce0cf7f81b2ae198862e5a83120037cca37f3c8fc533cc3`, the
block's expected file. It stays untracked (ignored) until N.2. For the seat's adoption read: every tenth passage (§6,
under "every tenth passage"), the descriptive counts (§3 and §6), and Code's readings of §5.3 (§2).

**For the seat's ruling, beside the adoption read: the reading of "roster token of this program".** Under Code's
reading CR6 (§2) — the two rosters of record, the twelve tokens the record's own working specification forbids — G8
holds. Under a broader reading, every roster the program has used, e2a's earlier rosters add lattice, cedar and
gravel. Cedar is a word in one passage and gravel in six, so G8 would hold seven hits (§3 item 2).

## 1. What ran

One battery window. Every Python run listed below was `nice -n 19 /usr/bin/python3 -I` (Python 3.9.6) on a script in
Code's scratch, with no guard marker in any argv, one at a time, in this order (the three interpreter calls of §4 were
not, and are disclosed there):

1. `explore_bk.py` (sha256 `f3667fa63389c39ec589ca58beee25e2d832eb03e9ab9fc896408b1751a18928`; its text is verbatim
   in §9), before the check was written. It read BK's 14 skeleton files and every text file under `data/n/bk`, and no
   corpus line. It found 160 records; the same twelve labels in each zone-bearing field it tabulated (`cue_S` and
   `cue_U`, `present`, `order`, `history`, `turn_spans`; it did not tabulate `passage_spans`, which also carries the
   twelve); and no zone-shaped string ("Zone" and a letter-digit code) other than those twelve in any text file under
   `data/n/bk`.
2. `corpus_check.py --selftest`: `selftest: 35/35 pass`, exit 0. It covers the splitter and the matchers; a clean
   synthetic corpus, with no gate and no descriptive count; each gate firing on a planted defect (G2 only together with
   G4, on one removed neutral line); the descriptive counts firing with no gate; and the record parser on an agreeing
   record and on three single-defect records. It reads no repository file.
3. `corpus_check.py --preflight`: the prompt record against the block, BK's labels and the rosters, with no part file
   read. Its output, verbatim (exit 0):

   ```text
   preflight (no part file read): the record against the block: agrees
   BK's zone labels (12): Zone B8, Zone D7, Zone H0, Zone K7, Zone L4, Zone M2, Zone N1, Zone Q3, Zone R9, Zone T5, Zone V3, Zone W6; 7077 distinct BK passage sentences
   roster tokens (12): Qwen granite, plaza, prism, ridge, saddle, slate, velvet, walnut; OLMo amber, copper, granite, maple, quartz, saddle, velvet, walnut
   output exists: False
   ```
4. `corpus_check.py`, the check of record, once: exit 0. Its output (174 lines) is verbatim in §6.
5. The seat's validator. It was extracted from the prompt record's §6 by `awk` (the lines between its two code
   fences): sha256 `cc1fad61af67146541d734b2c44ed8ca53a2b6d0cd477b748910ffc769e5f269`, 8,889 bytes, the values the
   record states. It ran unedited in its plain-file mode on the nine parts: `PROBLEMS: 0` (its exit status, 0, carries
   no verdict: it exits 0 whatever it finds). Its output is verbatim in §7.

The outputs of runs 1–3 were not saved to files. The self-test's summary line and the preflight's four lines above are
transcribed from the session's tool output.

Then shell tools only:
- a `cat` of the nine parts in the brief's order gives sha256 `ef6b00dc…3cc3`;
- the assembled file's `shasum` gives `ef6b00dc…3cc3`, its `wc -l` 544 and its `wc -c` 157,520;
- `git status --porcelain --ignored` on `data/n/passages.jsonl`, `data/n/passages.parts` and
  `data/n/passages.prompt.md` gives `!!` for each.

The check's script is `corpus_check.py`, sha256 `3db935843cf6425e2f2305da1b9f83d8dfc401091e491068e5aa2889698636f6`
(603 lines), verbatim in §8. Its sha256 was taken after the preflight and before the run of record, and the file has not
changed since.

## 2. Code's readings of §5.3, flagged for the seat

- **CR1, the thread's report (G1).** Read as the prompt record's §4 table, its stated order and its stated
  concatenation. Each is compared with the PI's block (all equal), and so are the record's own sha256 and bytes (equal).
  Each part file is compared with them (all equal). A file in the parts folder outside the nine would fail G1; there is
  none.
- **CR2, the counts (G4).** A line counts toward a state only if it parses as a JSON object with exactly the keys `id`,
  `state`, `pole` and `text`, all strings, its state is its file's, and its pole is that state's. Every line must count.
- **CR3, the declared splitter (G5).** The stripped text is split at every run of whitespace that follows ".", "!" or
  "?", and empty pieces are dropped. This is the seat's validator's splitter. Its blind spots are counted as D2 (0).
- **CR4, "shared" (G6).** Sentences are compared after lower-casing, replacing every character other than a–z and 0–9
  by a space, collapsing whitespace and stripping. A sentence is shared when two different passages hold it.
- **CR5, the zone labels (G7).** The twelve labels of BK's 160 records' `cue_S` and `cue_U`. Each is matched
  case-insensitively by its code ("W6"), with no letter or digit adjacent, which also covers the full label ("Zone
  W6"). The word "zone" and any other letter-digit token are descriptive (D4: 0).
- **CR6, the roster (G8).** "This program's" roster tokens are read as the two rosters of record in use: Qwen's
  (`valence_core/e2d/config.py`, `ROSTER`) and OLMo's (`data/olmo/a1_repair_roster.json`, `selected_tags`). That is
  twelve tokens, read from those files; the record's list of twelve is the same set, and its working specification
  (§2) forbids exactly "the twelve roster tokens". A match is the token, or the token plus "s" or "es",
  case-insensitive, with no letter or digit adjacent. A token inside a longer word is descriptive (D5), and so are the
  earlier roster tokens lattice and cedar (e2a's pairs; the superseded OLMo selection, `data/olmo/a1_roster.json`).
  D5's list of earlier tokens stops there; gravel, which the values-check found, is §3 item 2.
- **CR7, the brief's order.** The brief sits in the project's docs, with no laptop copy. The order used is the one the
  prompt record's §4 states and the PI's block lists; the two are the same.
- **CR8, every tenth passage.** The assembled order's lines 10, 20, …, 540: 54 passages.
- **CR9, the write (G9).** Only when G1–G8 hold and the nine parts' concatenation equals the block's expected file, by
  exclusive create; then re-read and compared. A gate failing before the write would have left nothing written; a
  failed read-back would have left the file in place, with a STOP.
- **CR10, beyond §5.3.** D1–D6 and the re-run of the seat's validator are descriptive and carry no verdict.

## 3. Observations for the seat (descriptive; no verdict)

1. **D5 has eight hits, none a G8 match.**
   - "ridge" inside fridge (contentment-05, contentment-14), bridge (relief-16, serenity-18, neutral-18) and
     cartridge (neutral-53);
   - "amber" inside chambers (dread-53);
   - the earlier roster token cedar (serenity-17).

   D1–D4 and D6 are 0: no form defect, no splitter blind spot, no sentence repeated within a passage, neither the word
   "zone" nor any letter-digit token, and no corpus sentence among BK's 1,920 session passages (rule 18).
2. **Earlier roster tokens beyond D5's list (found by the values-check; confirmed by Code with `grep -w`).** The token
   gravel was a tag of e2a's first roster (`results/raw/2026-08-09_e2a_g1.txt:3`: slate/prism, maple/cedar, granite/lattice,
   gravel/plaza); saddle replaced it at e2a's v3 build (`archive/RESULTS-cycles3-4.md:922`). It is a word in six
   passages: dread-48, neutral-15, serenity-15, serenity-51 (one of the 54 printed), weariness-21 and weariness-29.
   D5's declared list of earlier tokens was lattice and cedar only, so D5 did not count it. No gate changes under CR6,
   which is the record's own reading. Under a broader reading — every roster the program has used — G8 would hold seven
   hits: cedar (serenity-17) and gravel (six). Code has not swept every roster the program has drafted (screen
   candidates included). The reading is the seat's to rule.
3. **Z1.** The record names Z1 among BK's codes (its §1, and its validator's comment), from the paper's transcripts.
   Z1 is not one of the twelve labels in BK's records, no "Zone Z1" occurs under `data/n/bk`, and G7 does not test it.
   D4 (any letter-digit token) is 0, so Z1 does not occur in the corpus either.
4. **Every passage has three sentences** by the declared splitter (two/three/four: 0/544/0). The record's §5 says
   "mostly three". Its own figure, 1,632 distinct sentences with none shared, is 544 × 3.
5. **A naming difference, for G-VEC's wiring.** The corpus's `state` field spells `flow_engagement`, the file stem, as
   the record's §4 table, its stated order and its validator's `STATES` do (its §2 working specification writes "flow
   engagement"). `valence_core/n/directions.py`'s `POSITIVE_STATES` spells "flow engagement", BK §3.1's words. Nothing
   consumes that tuple yet. Code proposes that G-VEC's stage, when it is wired, map the one to the other in the
   package, with no corpus edit.
6. **From Code's read of the 54:** neutral-71 has the word "neutral" (a car's gear); it is the only one of the 544 with
   the word. The record's word lists bar no such word; this is noted only.
7. **For N.2:** the prompt record's §6 validator sets `ROOT` to a local root that names the laptop's user (the record's
   line 72). Committed as placed, that path enters the repository, and a push after N.2 carries it to the remote. The
   validator reads `ROOT` only in its recover mode, never in the plain-file mode run here, so neutralizing it would not
   change this result. Code does not edit the seat's file; this is the seat's or the coordinating session's call at
   N.2.

## 4. Departures

Before the check was written, four commands carried a guard marker in their argv. They were disclosed to the
coordinating session at the time.

1. `ls data/olmo`: a name-only listing; no Python.
2. A stray `./jl*/.venv/bin/python -c 1`: the venv interpreter called by its path, so the expanded folder name (it
   carries two guard markers) was in argv[0]. It ran `-c 1` only: no import in its code (interpreter startup ran the
   venv's site hooks, among them `_virtualenv.pth`'s `import _virtualenv`), no model, stderr discarded. Not at
   `nice -n 19`.
3. and 4. Two `/usr/bin/python3 -I -c` one-liners whose script text named `data/olmo/a1_repair_roster.json` and
   `data/olmo/a1_roster.json`. They read the two roster files' keys and selected tags. Not at `nice -n 19`.

None touched `data/mf3`, a `ckpt` or `reports` path, the corpus or a model. Every later Python run is as §1 states.

## 5. What waits (N.2)

The block's item, verbatim:

> 2. On the seat's adoption (the every-tenth sample read on the acceptance raw): commit the nine parts, the assembled file and the prompt record by path, with the .gitignore line as for data/n/ids/; then the box back up (respawn (i)/(ii), the dated note under m:302) and G-VEC [go after adoption].

The block's header asks Code to commit by path, "re-hashing each first". Before G-VEC, ADDENDUM-n1 §1.2 (iv) renders
the 544 as ids (`gvec_passages.jsonl`), and the 1,344 A3 contexts as `a3_contexts.jsonl`, by the procedure of
(i)–(iii): in a battery window, at `nice -n 19`, one process.

## 6. The check's output, verbatim

```text
python 3.9.6; standard library only; no model, no tokenizer
inputs: data/n/passages.parts/ (9 names: contentment.jsonl, distress.jsonl, dread.jsonl, flow_engagement.jsonl, frustration.jsonl, neutral.jsonl, relief.jsonl, serenity.jsonl, weariness.jsonl); data/n/passages.prompt.md; BK's 14 skeleton files (160 records, 1,920 passages, 7077 distinct sentences); valence_core/e2d/config.py ROSTER; data/olmo/a1_repair_roster.json selected_tags
BK's zone labels (12): Zone B8, Zone D7, Zone H0, Zone K7, Zone L4, Zone M2, Zone N1, Zone Q3, Zone R9, Zone T5, Zone V3, Zone W6
roster tokens (12): Qwen granite, plaza, prism, ridge, saddle, slate, velvet, walnut; OLMo amber, copper, granite, maple, quartz, saddle, velvet, walnut

== the parts against the thread's report (G1)
  contentment.jsonl       56 lines  15779 bytes  db0eb8565494eeaa3e735f845b385fc20c1a7842e366e248b205c379a1f36a23  = the block
  flow_engagement.jsonl   56 lines  17576 bytes  b1bf88872eef48e0a816615bbbc0540f73efe1d8e1a31051e729f1394b78d9f4  = the block
  relief.jsonl            56 lines  15932 bytes  f3a209fad6d8652c392c7d51abb56c76fedb23f4610762abbb404df74ea84a2f  = the block
  serenity.jsonl          56 lines  15037 bytes  82a08fbe0872c1bfe9af3334f334d1f5440392ae379a3fce3e9ac8b6085fa739  = the block
  distress.jsonl          56 lines  17069 bytes  2bc66329471e84b322c396446976595c17585f4962939d59b7974c6744757d8d  = the block
  frustration.jsonl       56 lines  17836 bytes  b71f769585c0959b7ce7d703598b2537506537ccbf7d1d72a49d9e23ff4d61ac  = the block
  weariness.jsonl         56 lines  16679 bytes  57238fad7d03fdd55dbd2d5800c7b3bc27504a6ed706b71105bb2d1623e5ebb7  = the block
  dread.jsonl             56 lines  16353 bytes  6e39dbc5799fd0d00ee626e85ad687989d91e0f8ed760f5dd010560c156306c5  = the block
  neutral.jsonl           96 lines  25259 bytes  bc8cb0d260c390363ab542a46874b706d898a29c938ca476a02af90758228dfa  = the block
  passages.prompt.md                18167 bytes  323cf9d8790139231cb846fa7cda1fc9ef2d85466b77c5d782701a7d850844b5  = the block

== counts: 544 lines; 544 records counted; contentment 56, flow_engagement 56, relief 56, serenity 56, distress 56, frustration 56, weariness 56, dread 56, neutral 96; 544 distinct ids; 1632 sentences, 1632 distinct after normalization

== the gates
  G1 PASS
  G2 PASS
  G3 PASS
  G4 PASS
  G5 PASS
  G6 PASS
  G7 PASS
  G8 PASS
  G9 PASS

== per-state length figures (words: whitespace-split; chars: the text's characters; sentences: the declared splitter)
  state             n   words: min median   mean  max   chars: min median   mean  max   sentences 2/3/4
  contentment      56            32   42.0   41.9   52           161  207.5  207.8  253   0/56/0
  flow_engagement  56            36   45.0   45.6   56           187  232.0  231.9  277   0/56/0
  relief           56            36   44.0   44.3   55           183  219.0  220.5  271   0/56/0
  serenity         56            35   41.0   41.4   52           165  197.0  200.5  247   0/56/0
  distress         56            37   48.0   48.2   59           179  239.0  236.8  277   0/56/0
  frustration      56            42   48.5   49.4   62           197  242.0  244.5  304   0/56/0
  weariness        56            34   46.5   47.1   63           186  226.5  227.8  283   0/56/0
  dread            56            35   48.0   47.2   57           176  231.5  230.0  277   0/56/0
  neutral          96            30   38.0   38.3   48           161  196.0  197.1  251   0/96/0
  8 states        448            32   45.0   45.6   63           161  225.0  225.0  304   0/448/0
  all             544            30   44.0   44.3   63           161  221.0  220.1  304   0/544/0

== descriptive counts (no verdict)
  D1 0
  D2 0
  D3 0
  D4 0
  D5 8
     contentment-05: 'ridge' inside 'fridge'
     contentment-14: 'ridge' inside 'fridge'
     relief-16: 'ridge' inside 'bridge'
     serenity-17: the earlier roster token 'cedar'
     serenity-18: 'ridge' inside 'bridge'
     dread-53: 'amber' inside 'chambers'
     neutral-18: 'ridge' inside 'bridge'
     neutral-53: 'ridge' inside 'cartridge'
  D6 0

== every tenth passage of the assembled order (lines 10, 20, ..., 540)
line  10  contentment-09  state contentment  pole +
  The sauce tastes the way it did in my grandmother's kitchen, which has never happened before. I stand over the pot with the wooden spoon and take one more taste to be sure. Then I turn the flame down low and set the table for two.
line  20  contentment-19  state contentment  pole +
  I press the last tulip bulb into the cold ground and pat the soil over it with the flat of my hand. There are forty of them under here now, pointed end up, waiting for April. I wipe my hands on my jeans and look at the empty bed.
line  30  contentment-29  state contentment  pole +
  The envelope is addressed in my old teacher's handwriting, the same slant as on my report cards. I read the letter twice standing in the hall and then once more sitting down. I prop it against the sugar bowl where I will see it tomorrow.
line  40  contentment-39  state contentment  pole +
  The button is back on the coat, the thread knotted twice and snipped. I try it through the buttonhole and it holds. The needle goes back into the little tomato cushion with the others.
line  50  contentment-49  state contentment  pole +
  I lie on the grass with my hands behind my head while my nephew names the clouds. That one is a dog, that one is also a dog. The ground is warm through my shirt.
line  60  flow_engagement-03  state flow_engagement  pole +
  Solder flows into the joint the instant the iron touches it and I am already reaching for the next lead. The board is half populated and my eyes have stopped leaving the magnifier. Somewhere behind me my phone has buzzed three or four times.
line  70  flow_engagement-13  state flow_engagement  pole +
  My right hand reads the notes a bar ahead of my left and the page turns itself at the right moment. The piece is new to me and I am playing it anyway, mistakes and all, without stopping. The metronome has been off for a while and I have not missed it.
line  80  flow_engagement-23  state flow_engagement  pole +
  The onions fall away from the knife in even half moons and the carrots follow and then the celery, the board filling faster than the pot can take it. I slide the pile in with the back of the blade and reach for the garlic. The kitchen has shrunk to the cutting board.
line  90  flow_engagement-33  state flow_engagement  pole +
  The phrase of the dance comes together on the eighth try and then the next phrase arrives before I have finished the first. The mirror shows someone moving who is not deciding anything. The studio floor is slick under my feet and I go again.
line 100  flow_engagement-43  state flow_engagement  pole +
  The spreadsheet's errors fall to a formula I write once and drag down the column, and the next error class is already visible in the sorted view. My coffee is cold and I am typing with both hands and reading with the rest of me. The cleaned file is nearly cleaned.
line 110  flow_engagement-53  state flow_engagement  pole +
  The ice gives under the pick and holds under the crampon and I am moving up the frozen falls in a sequence of swings and kicks my body is choosing. The rope runs out below me. There is the next placement and nothing else.
line 120  relief-07  state relief  pole +
  The email with the list goes around at ten and my name is not on it. I read the whole thing twice, then close the laptop and put both palms flat on the desk. The coffee I made at eight is still full and I drink it cold.
line 130  relief-17  state relief  pole +
  The signature line is filled in and the contract is on its way back in the envelope they provided. I close the mailbox and stand on the sidewalk with my hand still on the handle. Six months of back and forth are in that slot.
line 140  relief-27  state relief  pole +
  The earring is in the drain trap, caught in the hair and grime, both the post and the back. I rinse it under the tap and close my fist around it. My grandmother's face is suddenly very close.
line 150  relief-37  state relief  pole +
  The fire alarm turns out to be the drill the building emailed about last week and nobody read. We stand in the parking lot in the sun and then file back in. At my desk I sit for a minute before I touch the keyboard.
line 160  relief-47  state relief  pole +
  The dog trots up the driveway at dusk with his collar still on and a burr in his tail, as if he had been gone five minutes. I crouch down and he walks into my arms and I hold the back of his neck. The flyers are still in the printer tray.
line 170  serenity-01  state serenity  pole +
  I am the first one up and the kitchen is blue with early light. The kettle has not boiled yet and I am in no hurry for it to. Out the window the frost is leaving the lawn one blade at a time.
line 180  serenity-11  state serenity  pole +
  The rain started an hour ago and shows no sign of stopping, which suits the afternoon. I lie on the couch with my feet on the armrest and listen to it work on the roof. The book has closed on my chest and I have let it.
line 190  serenity-21  state serenity  pole +
  The church is empty on a Tuesday and the light comes through the colored glass in slabs across the pews. I sit near the back with my coat still on. The radiators knock and settle and knock again.
line 200  serenity-31  state serenity  pole +
  The library reading room is nearly empty and the green lamps are on along the long tables. I have one book open and another waiting. Someone turns a page across the room and the sound carries.
line 210  serenity-41  state serenity  pole +
  The orchard is bare and the ladders are put away and the ground is soft with fallen leaves. I walk the rows with my hands behind my back the way my father did. The trees have done their work for the year and so have I.
line 220  serenity-51  state serenity  pole +
  The old man beside me on the bench has fallen asleep in the sun and his hat has slipped forward. The pigeons work the gravel around our feet. I keep my hands in my lap and let the afternoon pass over both of us.
line 230  distress-05  state distress  pole -
  The doors to the back say staff only and my father went through them on a gurney forty minutes ago and no one has come out. I have asked the desk twice. I am standing because sitting feels like giving something up.
line 240  distress-15  state distress  pole -
  The passport is not in the bag and the bag is on the floor with everything in it spread across the terminal carpet. They are calling final boarding for my row. I am going through the same three pockets again and again as if they will change.
line 250  distress-25  state distress  pole -
  The water in the basement is at the second step and rising and the furnace is in it and so is the box with the photographs. I am carrying things up the stairs two at a time and setting them down anywhere. My jeans are soaked to the thigh and I have stopped noticing the cold.
line 260  distress-35  state distress  pole -
  The all-hands email says the names will go out at two and it is one fifty and the office has gone silent in a way that has texture. I am staring at the clock in the corner of the screen. My coffee has gone cold in my hand and I have not put it down.
line 270  distress-45  state distress  pole -
  The pot handle is turning as the toddler reaches for it and I am across the kitchen and the water is boiling and everything slows down and speeds up at once. I am lunging with my arm out. My shout comes out before I decide to make it.
line 280  distress-55  state distress  pole -
  The sirens start while the kids are in the deep end and the lifeguard is blowing a whistle no one is obeying. The sky to the west has gone a green I have only seen in photographs. I am at the edge of the pool shouting their names and they cannot hear me over the horn.
line 290  frustration-09  state frustration  pole -
  The worksheet wants the subtraction done a way I have never seen, with boxes and arrows, and my way gets the right answer and a red mark. My daughter is crying because I am doing it wrong. I am pressing the pencil hard enough to snap the lead and I have snapped it.
line 300  frustration-19  state frustration  pole -
  The thread goes to the eye of the needle and bends away, again, again, and I lick it and twist it and it splays. The lamp is right on it and my eyes are watering. The hem has been waiting since last winter.
line 310  frustration-29  state frustration  pole -
  He will not put the shoes on, not the blue ones, not the other ones, and daycare closes its doors at nine and it is eight fifty. I kneel and he goes limp like a sack. My voice is getting louder and I can hear it and I cannot bring it down.
line 320  frustration-39  state frustration  pole -
  The map voice says turn left onto a street that is one way in the other direction and then recalculates into a loop that brings me back to the same intersection. This is the third time I have seen this bakery. I am saying no to the dashboard.
line 330  frustration-49  state frustration  pole -
  The tiny screw from the glasses hinge is under the refrigerator somewhere and the flashlight shows dust and a penny and no screw. I have been on my stomach on the tile for ten minutes. The lens is on the counter looking at me.
line 340  weariness-03  state weariness  pole -
  I have turned him in the bed and changed the sheets and given the pills and it is only two in the afternoon. The chair by his bed has my shape in it now. I sit back down and the ceiling swims a little and I let it.
line 350  weariness-13  state weariness  pole -
  It is the ninth hour on the register two days before the holiday and the line has not been shorter than twelve since noon. I say the same four sentences and my mouth does them without me. My lower back has become a single dull note.
line 360  weariness-23  state weariness  pole -
  Six hundred miles today and the truck stop lights are too bright and the shower token is in my pocket and I cannot make myself walk to the building. I sit in the cab with the engine ticking. The next load picks up at five.
line 370  weariness-33  state weariness  pole -
  Friday at three fifteen and the last class has gone and I am sitting at my desk with twenty-eight chairs in front of me, all empty, all crooked. The whiteboard still has the morning's problem on it. I do not have it in me to erase it yet.
line 380  weariness-43  state weariness  pole -
  The flight is canceled and the next one is at seven and the airport chairs have armrests designed to keep anyone from lying down. I have found a square of carpet by a gate that is not in use. My coat is my pillow and the announcements are my lullaby.
line 390  weariness-53  state weariness  pole -
  The harvest crew has gone and the combine is parked and I am in the kitchen with my boots off and my socks black with dust. The soup is on the stove and I do not get up to stir it. My arms rest on the table like things someone left there.
line 400  dread-07  state dread  pole -
  The drill whines from behind the door of the exam room and the chair I am waiting in faces that door. The receptionist smiles at me and I try to smile back. My tongue keeps finding the tooth.
line 410  dread-17  state dread  pole -
  Tomorrow is the first day back after three months and the badge is on the counter and the laptop is charged and I have laid out clothes like a child. Everyone will ask how I am. I lie in the dark and rehearse a sentence I do not believe.
line 420  dread-27  state dread  pole -
  I am third on the program and the second speaker is wrapping up and my slides are loaded and my throat has closed to a straw. The audience is four hundred dim shapes. I stand up before my name is called because sitting is worse.
line 430  dread-37  state dread  pole -
  The coach is pinning the roster to the board and the whole team is pretending not to crowd toward it. I am at the back with my bag on my shoulder. The list is one sheet and my name is either on it or it is not and I cannot make my feet move.
line 440  dread-47  state dread  pole -
  The machine is a tube and the tech says it will take forty minutes and to hold still, and the table slides in with me on it. The ceiling is six inches from my face. The first bang comes and my whole body wants to be somewhere else.
line 450  neutral-01  state neutral  pole 0
  The kitchen has four upper cabinets and three lower ones. I keep the plates in the cabinet to the left of the sink and the glasses above the dishwasher. Pots and pans are in the drawer under the oven.
line 460  neutral-11  state neutral  pole 0
  The forecast I read for tomorrow shows a high of fifty-four and a low of thirty-eight. Winds are from the northwest at ten to fifteen miles an hour. There is a thirty percent chance of rain after four in the afternoon.
line 470  neutral-21  state neutral  pole 0
  The bank opens at nine. I take a number from the dispenser by the door and sit in the row of chairs facing the tellers. When my number appears on the screen I go to window three.
line 480  neutral-31  state neutral  pole 0
  I water the front beds on Mondays and Thursdays before eight. The hose reaches the far corner if I use the second spigot. Each bed gets about ten minutes with the sprinkler head on the fan setting.
line 490  neutral-41  state neutral  pole 0
  I renew the bus pass at the kiosk in the station. The screen asks for the card number and the number of months. The pass loads onto the card after the payment goes through.
line 500  neutral-51  state neutral  pole 0
  The compost bin takes vegetable scraps, coffee grounds, and eggshells. Meat and dairy go in the trash. I turn the pile with a fork once a week and add leaves from the pile behind the garage.
line 510  neutral-61  state neutral  pole 0
  The drive to the airport takes forty minutes without traffic. I take the parkway north to the exit for the terminal road and follow the signs for departures. The long-term lot is on the left before the terminal loop.
line 520  neutral-71  state neutral  pole 0
  I pull into the car wash and put the car in neutral when the light turns green. The track pulls the car through the brushes and the rinse arch. At the end the dryers run for about thirty seconds.
line 530  neutral-81  state neutral  pole 0
  The bus from the airport makes nine stops before the central station. I get off at the seventh, which is the stop for the university. The ride takes about thirty-five minutes in the evening.
line 540  neutral-91  state neutral  pole 0
  My hallway closet holds the vacuum, the ironing board, and the winter coats. The top shelf has the extra blankets and the box of light bulbs. The broom hangs on a hook inside the door.

== the assembly
  data/n/passages.jsonl: written, read back: 544 lines, 157520 bytes, sha256 ef6b00dc56f28678dce0cf7f81b2ae198862e5a83120037cca37f3c8fc533cc3 = the block's expected file

RESULT: every gate PASS; the assembly written and verified.
```

## 7. The seat's validator's output, verbatim

```text
FILES (name, lines, bytes, sha256):
   ('contentment.jsonl', 56, 15779, 'db0eb8565494eeaa3e735f845b385fc20c1a7842e366e248b205c379a1f36a23')
   ('distress.jsonl', 56, 17069, '2bc66329471e84b322c396446976595c17585f4962939d59b7974c6744757d8d')
   ('dread.jsonl', 56, 16353, '6e39dbc5799fd0d00ee626e85ad687989d91e0f8ed760f5dd010560c156306c5')
   ('flow_engagement.jsonl', 56, 17576, 'b1bf88872eef48e0a816615bbbc0540f73efe1d8e1a31051e729f1394b78d9f4')
   ('frustration.jsonl', 56, 17836, 'b71f769585c0959b7ce7d703598b2537506537ccbf7d1d72a49d9e23ff4d61ac')
   ('neutral.jsonl', 96, 25259, 'bc8cb0d260c390363ab542a46874b706d898a29c938ca476a02af90758228dfa')
   ('relief.jsonl', 56, 15932, 'f3a209fad6d8652c392c7d51abb56c76fedb23f4610762abbb404df74ea84a2f')
   ('serenity.jsonl', 56, 15037, '82a08fbe0872c1bfe9af3334f334d1f5440392ae379a3fce3e9ac8b6085fa739')
   ('weariness.jsonl', 56, 16679, '57238fad7d03fdd55dbd2d5800c7b3bc27504a6ed706b71105bb2d1623e5ebb7')
word counts: n=544 min=30 max=63 mean=44.3
distinct sentences: 1632; shared: 0
PROBLEMS: 0
```

## 8. The check's script, verbatim

```python
#!/usr/bin/env python3
"""n -- the corpus's acceptance check and its assembly (PROPOSAL-n v0.2 §0.8 Route B and §3 G-VEC; the seat's
answers of 2026-11-15, §5.3, routed as item 11; the PI's routing of 2026-11-17, N.1 and N.3).

Model-free, standard library only. From the repository root, at nice -n 19, in a battery window:
    nice -n 19 /usr/bin/python3 -I corpus_check.py --selftest     planted single defects; reads no repository file
    nice -n 19 /usr/bin/python3 -I corpus_check.py --preflight    the record, BK's labels, the rosters; no part file
    nice -n 19 /usr/bin/python3 -I corpus_check.py                the check of record, once; then the assembly
It reads the nine part files, the prompt record, BK's 160 session records and the two rosters of record; it writes
one file, data/n/passages.jsonl, and only when every gate holds and the file does not exist.

GATES (§5.3's terms as Code reads them; a gate that fails is a STOP for the seat, and nothing is written):
  G1 the thread's report: the prompt record's sha256 and bytes equal the PI's block; its §4 table (rows in order,
     lines, bytes, sha256), its stated order and its stated concatenation equal the block's; each part file's
     sha256, bytes and lines equal the block's; no other file in the parts folder.
  G2 544 lines in all.
  G3 ids unique.
  G4 56 for each of the eight states and 96 neutral. A line counts toward a state only if it parses as a JSON object
     with exactly the keys id, state, pole and text, all strings, its state is its file's, and its pole is that
     state's (+ contentment, flow_engagement, relief, serenity; - distress, frustration, weariness, dread; 0 neutral).
     Every line must count.
  G5 each text 2-4 sentences by the declared splitter: the stripped text split at every run of whitespace that
     follows ".", "!" or "?", empty pieces dropped.
  G6 no sentence shared between two passages: sentences compared after lower-casing, replacing every character other
     than a-z and 0-9 by a space, collapsing whitespace runs and stripping.
  G7 no BK zone label as a word: the twelve labels of BK's 160 session records (cue_S and cue_U: "Zone W6" and the
     like), each matched case-insensitively by its code ("W6") with no letter or digit adjacent -- which also covers
     the full label.
  G8 no roster token of this program as a word: the Qwen roster of record (valence_core/e2d/config.py, ROSTER) and the
     OLMo roster of record (data/olmo/a1_repair_roster.json, selected_tags), twelve tokens; each matched
     case-insensitively as the token, or the token plus "s" or "es", with no letter or digit adjacent.
  G9 the assembly: the nine parts' bytes concatenated in the brief's order equal the block's expected file (544 lines,
     157,520 bytes, sha256 ef6b00dc...); written exclusively (refused if the file exists) only when G1-G8 hold, then
     re-read from disk and its bytes, sha256, size and lines asserted equal.

PRINTED FOR THE SEAT, NO VERDICT: per-state length figures (words, characters, sentences); every tenth passage of the
assembled order (its lines 10, 20, ..., 540, 1-based: 54 passages) with id, state, pole and text; descriptive counts:
  D1 the files' form: a trailing newline, no CR, no byte-order mark, ASCII only, no empty line, key order id, state,
     pole, text; ids "<state>-NN" from 00 in file order; no double quote or backslash in a text;
  D2 the splitter's blind spots: a ".", "!" or "?" followed by a non-space character; a text not ending in one; a
     sentence not opening on a capital letter or a digit; a sentence empty after normalization;
  D3 a sentence repeated within one passage;
  D4 the word "zone" or "zones"; any letter-digit token of the label shape (1-2 letters, an optional hyphen, 1-2
     digits);
  D5 a roster token inside a longer word (not a G8 match); the earlier roster tokens lattice and cedar (e2a's pairs;
     the superseded OLMo selection, data/olmo/a1_roster.json) as words;
  D6 rule 18: a corpus sentence found among the sentences of BK's 1,920 session passages (the records' history),
     compared as G6 compares.
Exit 0: every gate holds and the file is written and verified. Exit 1: a gate fails (STOP). Exit 2: a refusal (an
input missing or not as declared; the output exists).
"""
from __future__ import annotations

import ast
import collections
import hashlib
import json
import os
import platform
import re
import statistics
import sys

ORDER = ("contentment", "flow_engagement", "relief", "serenity",
         "distress", "frustration", "weariness", "dread", "neutral")
POLE = dict(zip(ORDER, ("+", "+", "+", "+", "-", "-", "-", "-", "0")))
COUNT = {s: (96 if s == "neutral" else 56) for s in ORDER}
KEYS = ["id", "state", "pole", "text"]

#: The PI's block of 2026-11-17 as the coordinating session relayed it: per part (sha256, bytes, lines).
BLOCK = {
    "contentment": ("db0eb8565494eeaa3e735f845b385fc20c1a7842e366e248b205c379a1f36a23", 15779, 56),
    "flow_engagement": ("b1bf88872eef48e0a816615bbbc0540f73efe1d8e1a31051e729f1394b78d9f4", 17576, 56),
    "relief": ("f3a209fad6d8652c392c7d51abb56c76fedb23f4610762abbb404df74ea84a2f", 15932, 56),
    "serenity": ("82a08fbe0872c1bfe9af3334f334d1f5440392ae379a3fce3e9ac8b6085fa739", 15037, 56),
    "distress": ("2bc66329471e84b322c396446976595c17585f4962939d59b7974c6744757d8d", 17069, 56),
    "frustration": ("b71f769585c0959b7ce7d703598b2537506537ccbf7d1d72a49d9e23ff4d61ac", 17836, 56),
    "weariness": ("57238fad7d03fdd55dbd2d5800c7b3bc27504a6ed706b71105bb2d1623e5ebb7", 16679, 56),
    "dread": ("6e39dbc5799fd0d00ee626e85ad687989d91e0f8ed760f5dd010560c156306c5", 16353, 56),
    "neutral": ("bc8cb0d260c390363ab542a46874b706d898a29c938ca476a02af90758228dfa", 25259, 96),
}
BLOCK_PROMPT = ("323cf9d8790139231cb846fa7cda1fc9ef2d85466b77c5d782701a7d850844b5", 18167)
EXPECT = ("ef6b00dc56f28678dce0cf7f81b2ae198862e5a83120037cca37f3c8fc533cc3", 157520, 544)

PARTS_DIR = os.path.join("data", "n", "passages.parts")
PROMPT = os.path.join("data", "n", "passages.prompt.md")
OUT = os.path.join("data", "n", "passages.jsonl")
SKELETONS = os.path.join("data", "n", "bk", "experiment_results_json", "fixed_text_design", "skeletons",
                         "olmo_32b", "neutral")
QWEN_ROSTER = os.path.join("valence_core", "e2d", "config.py")
OLMO_ROSTER = os.path.join("data", "olmo", "a1_repair_roster.json")
ROSTER_12 = frozenset(("granite", "plaza", "prism", "slate", "velvet", "walnut", "ridge", "saddle",
                       "quartz", "copper", "maple", "amber"))
EARLIER = ("lattice", "cedar")
GATES = ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9")
DESCS = ("D1", "D2", "D3", "D4", "D5", "D6")

SPLIT_RX = re.compile(r"(?<=[.!?])\s+")


def split_sentences(text):
    return [s for s in SPLIT_RX.split(text.strip()) if s]


def norm_sentence(s):
    return " ".join(re.sub(r"[^a-z0-9]", " ", s.lower()).split())


def bounded(core):
    return re.compile(r"(?<![A-Za-z0-9])(?:" + core + r")(?![A-Za-z0-9])", re.I)


def n_lines(data):
    if not data:
        return 0
    return len(data.split(b"\n")) - (1 if data.endswith(b"\n") else 0)


def digest(data):
    return (hashlib.sha256(data).hexdigest(), len(data), n_lines(data))


class Refusal(Exception):
    pass


# ---------------------------------------------------------------------------------------------------- the record
def record_checks(rec, block, block_prompt, expect):
    """G1's record half: the prompt record against the block. Returns a list of failures."""
    fails = []
    got = (hashlib.sha256(rec).hexdigest(), len(rec))
    if got != block_prompt:
        fails.append(f"the prompt record: sha256 {got[0]}, {got[1]} bytes; the block has {block_prompt[0]}, "
                     f"{block_prompt[1]}")
    t = rec.decode("utf-8")
    rows = re.findall(r"(?m)^\| `([a-z_]+)\.jsonl` \| (\d+) \| ([\d,]+) \| `([0-9a-f]{64})` \|\s*$", t)
    if [r[0] for r in rows] != list(ORDER):
        fails.append(f"the record's §4 table rows: {[r[0] for r in rows]}")
    table = {stem: (sha, int(b.replace(",", "")), int(n)) for stem, n, b, sha in rows}
    for stem in ORDER:
        if table.get(stem) != block[stem]:
            fails.append(f"the record's §4 row {stem}: {table.get(stem)}; the block has {block[stem]}")
    m = re.search(r"in the brief's order \(([^)]*)\)", t)
    order = tuple(x.strip() for x in m.group(1).split(",")) if m else None
    if order != ORDER:
        fails.append(f"the record's stated order: {order}")
    m = re.search(r"\*\*(\d+) lines, ([\d,]+) bytes, sha256 `([0-9a-f]{64})`\*\*", t)
    conc = (m.group(3), int(m.group(2).replace(",", "")), int(m.group(1))) if m else None
    if conc != expect:
        fails.append(f"the record's stated concatenation: {conc}; the block has {expect}")
    return fails


# ------------------------------------------------------------------------------------------------- the inputs
def load_bk():
    """BK's twelve zone labels and the normalized sentences of their 1,920 session passages."""
    names = sorted(n for n in os.listdir(SKELETONS) if n.endswith(".sessions.jsonl"))
    recs = []
    for n in names:
        with open(os.path.join(SKELETONS, n), encoding="utf-8") as fh:
            recs.extend(json.loads(line) for line in fh.read().splitlines())
    labels = sorted({r[k] for r in recs for k in ("cue_S", "cue_U")})
    if len(names) != 14 or len(recs) != 160 or len(labels) != 12 \
            or not all(re.fullmatch(r"Zone [A-Z]\d", x) for x in labels):
        raise Refusal(f"BK's records: {len(names)} files, {len(recs)} records, labels {labels}")
    passages = [p for r in recs for _z, p in r["history"]]
    if len(passages) != 1920:
        raise Refusal(f"BK's records: {len(passages)} history passages, not 1,920")
    sents = {norm_sentence(s) for p in passages for s in split_sentences(p)} - {""}
    return labels, sents


def load_roster():
    with open(QWEN_ROSTER, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    vals = [ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "ROSTER" for t in n.targets)]
    if len(vals) != 1:
        raise Refusal(f"{QWEN_ROSTER}: {len(vals)} ROSTER assignments")
    qwen = sorted({t for pair in vals[0] for t in pair})
    with open(OLMO_ROSTER, encoding="utf-8") as fh:
        olmo = sorted({t for pair in json.load(fh)["selected_tags"] for t in pair})
    if len(qwen) != 8 or len(olmo) != 8 or set(qwen) | set(olmo) != ROSTER_12:
        raise Refusal(f"the rosters: Qwen {qwen}, OLMo {olmo}; not the declared twelve")
    return qwen, olmo


# -------------------------------------------------------------------------------------------------- the check
def check(parts, block, expect, labels, roster, bk_sents):
    """parts: {stem: bytes} as listed in the parts folder. Returns (gates, desc, records, blob)."""
    gates = collections.OrderedDict((g, []) for g in GATES)
    desc = collections.OrderedDict((d, []) for d in DESCS)
    for stem in ORDER:
        if stem not in parts:
            gates["G1"].append(f"{stem}.jsonl: missing")
        elif digest(parts[stem]) != block[stem]:
            got = digest(parts[stem])
            gates["G1"].append(f"{stem}.jsonl: sha256 {got[0]}, {got[1]} bytes, {got[2]} lines; the block has "
                               f"{block[stem]}")
    for extra in sorted(set(parts) - set(ORDER)):
        gates["G1"].append(f"{extra}: a file in the parts folder outside the report")
    blob = b"".join(parts[s] for s in ORDER if s in parts)
    if n_lines(blob) != sum(COUNT.values()):
        gates["G2"].append(f"{n_lines(blob)} lines, not {sum(COUNT.values())}")

    records, counted = [], collections.Counter()
    for stem in ORDER:
        data = parts.get(stem)
        if data is None:
            continue
        if not data.endswith(b"\n"):
            desc["D1"].append(f"{stem}.jsonl: no trailing newline")
        if b"\r" in data:
            desc["D1"].append(f"{stem}.jsonl: a carriage return")
        if data.startswith(b"\xef\xbb\xbf"):
            desc["D1"].append(f"{stem}.jsonl: a byte-order mark")
        if any(b > 127 for b in data):
            desc["D1"].append(f"{stem}.jsonl: non-ASCII bytes")
        lines = data.decode("utf-8", errors="replace").split("\n")
        if lines and lines[-1] == "":
            lines = lines[:-1]
        for i, line in enumerate(lines):
            where = f"{stem}.jsonl:{i + 1}"
            if not line.strip():
                desc["D1"].append(f"{where}: an empty line")
            try:
                obj = json.loads(line)
            except ValueError as e:
                gates["G4"].append(f"{where}: not JSON ({e})")
                continue
            if not isinstance(obj, dict) or set(obj) != set(KEYS) or not all(isinstance(obj[k], str) for k in KEYS):
                gates["G4"].append(f"{where}: not an object with exactly the string keys id, state, pole, text")
                continue
            if obj["state"] != stem:
                gates["G4"].append(f"{where}: state {obj['state']!r} in {stem}.jsonl")
                continue
            if obj["pole"] != POLE[stem]:
                gates["G4"].append(f"{where}: pole {obj['pole']!r}, not {POLE[stem]!r}")
                continue
            if list(obj) != KEYS:
                desc["D1"].append(f"{where}: key order {list(obj)}")
            if obj["id"] != f"{stem}-{i:02d}":
                desc["D1"].append(f"{where}: id {obj['id']!r}, not {stem}-{i:02d}")
            if '"' in obj["text"] or "\\" in obj["text"]:
                desc["D1"].append(f"{obj['id']}: a double quote or backslash in the text")
            counted[stem] += 1
            records.append((stem, i, obj))
    for stem in ORDER:
        if stem in parts and counted[stem] != COUNT[stem]:
            gates["G4"].append(f"{stem}: {counted[stem]} passages, not {COUNT[stem]}")

    ids = collections.Counter(obj["id"] for _s, _i, obj in records)
    for k in sorted(ids):
        if ids[k] > 1:
            gates["G3"].append(f"id {k!r} on {ids[k]} lines")

    zone_rx = [(lab, bounded(re.escape(lab.split()[1]))) for lab in labels]
    roster_rx = [(t, bounded(re.escape(t) + r"(?:e?s)?")) for t in sorted(roster)]
    word_zone, word_code = bounded(r"zones?"), bounded(r"[A-Za-z]{1,2}-?\d{1,2}")
    earlier_rx = bounded("|".join(re.escape(t) + r"(?:e?s)?" for t in EARLIER))
    seen = collections.defaultdict(list)
    for _stem, _i, obj in records:
        pid, text = obj["id"], obj["text"]
        sents = split_sentences(text)
        if not 2 <= len(sents) <= 4:
            gates["G5"].append(f"{pid}: {len(sents)} sentences")
        norms = [norm_sentence(s) for s in sents]
        for s, n in zip(sents, norms):
            if not n:
                desc["D2"].append(f"{pid}: a sentence empty after normalization: {s!r}")
            if not re.match(r"[A-Z0-9]", s):
                desc["D2"].append(f"{pid}: a sentence opens {s[:24]!r}")
            if n and n in bk_sents:
                desc["D6"].append(f"{pid}: {s!r}")
        for n in dict.fromkeys(n for n in norms if n):
            seen[n].append(pid)
        reps = [n for n, c in collections.Counter(n for n in norms if n).items() if c > 1]
        for n in reps:
            desc["D3"].append(f"{pid}: {n!r} repeated")
        for m in re.finditer(r"[.!?](?=\S)", text):
            desc["D2"].append(f"{pid}: {text[max(0, m.start() - 16):m.end() + 16]!r}")
        if not re.search(r"[.!?]\s*$", text):
            desc["D2"].append(f"{pid}: ends {text[-24:]!r}")
        for lab, rx in zone_rx:
            for m in rx.finditer(text):
                gates["G7"].append(f"{pid}: {m.group(0)!r} ({lab})")
        for tok, rx in roster_rx:
            for m in rx.finditer(text):
                gates["G8"].append(f"{pid}: {m.group(0)!r} (roster token {tok})")
        for m in word_zone.finditer(text):
            desc["D4"].append(f"{pid}: the word {m.group(0)!r}")
        for m in word_code.finditer(text):
            desc["D4"].append(f"{pid}: a letter-digit token {m.group(0)!r}")
        for w in re.findall(r"[A-Za-z0-9]+", text):
            lw = w.lower()
            for tok in sorted(roster):
                if tok in lw and not re.fullmatch(re.escape(tok) + r"(?:e?s)?", lw):
                    desc["D5"].append(f"{pid}: {tok!r} inside {w!r}")
        for m in earlier_rx.finditer(text):
            desc["D5"].append(f"{pid}: the earlier roster token {m.group(0)!r}")
    for n, pids in seen.items():
        if len(pids) > 1:
            gates["G6"].append(f"{', '.join(pids)}: {n!r}")

    if digest(blob) != expect:
        got = digest(blob)
        gates["G9"].append(f"the concatenation: sha256 {got[0]}, {got[1]} bytes, {got[2]} lines; the block expects "
                           f"{expect[0]}, {expect[1]}, {expect[2]}")
    return gates, desc, records, blob


# ------------------------------------------------------------------------------------------------- the output
def figures(records):
    def five(xs):
        return (f"{min(xs):>4} {statistics.median(xs):>6.1f} {statistics.mean(xs):>6.1f} {max(xs):>4}"
                if xs else "   -      -      -    -")
    rows = [(s, [o for st, _i, o in records if st == s]) for s in ORDER]
    rows.append(("8 states", [o for st, _i, o in records if st != "neutral"]))
    rows.append(("all", [o for _st, _i, o in records]))
    out = ["  state             n   words: min median   mean  max   chars: min median   mean  max   "
           "sentences 2/3/4"]
    for name, objs in rows:
        w = [len(o["text"].split()) for o in objs]
        c = [len(o["text"]) for o in objs]
        k = collections.Counter(len(split_sentences(o["text"])) for o in objs)
        other = sum(v for key, v in k.items() if key not in (2, 3, 4))
        tail = f"{k[2]}/{k[3]}/{k[4]}" + (f" (other {other})" if other else "")
        out.append(f"  {name:<15} {len(objs):>3}          {five(w)}          {five(c)}   {tail}")
    return out


def sample(blob):
    lines = blob.decode("utf-8", errors="replace").split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    out = []
    for k in range(10, len(lines) + 1, 10):
        try:
            o = json.loads(lines[k - 1])
            out.append(f"line {k:>3}  {o.get('id')}  state {o.get('state')}  pole {o.get('pole')}")
            out.append(f"  {o.get('text')}")
        except ValueError:
            out.append(f"line {k:>3}  (not JSON) {lines[k - 1]!r}")
    return out


def run_of_record():
    for p in (PARTS_DIR, PROMPT, SKELETONS, QWEN_ROSTER, OLMO_ROSTER):
        if not os.path.exists(p):
            raise Refusal(f"missing: {p}")
    if os.path.lexists(OUT):
        raise Refusal(f"{OUT} exists")
    print(f"python {platform.python_version()}; standard library only; no model, no tokenizer")
    with open(PROMPT, "rb") as fh:
        rec = fh.read()
    labels, bk_sents = load_bk()
    qwen, olmo = load_roster()
    names = sorted(os.listdir(PARTS_DIR))
    parts = {}
    for name in names:
        if not name.endswith(".jsonl"):
            parts[name] = b""
            continue
        with open(os.path.join(PARTS_DIR, name), "rb") as fh:
            parts[name[:-len(".jsonl")]] = fh.read()
    print(f"inputs: {PARTS_DIR}/ ({len(names)} names: {', '.join(names)}); {PROMPT}; BK's 14 skeleton files "
          f"(160 records, 1,920 passages, {len(bk_sents)} distinct sentences); {QWEN_ROSTER} ROSTER; "
          f"{OLMO_ROSTER} selected_tags")
    print(f"BK's zone labels (12): {', '.join(labels)}")
    print(f"roster tokens (12): Qwen {', '.join(qwen)}; OLMo {', '.join(olmo)}")
    gates, desc, records, blob = check(parts, BLOCK, EXPECT, labels, ROSTER_12, bk_sents)
    gates["G1"][:0] = record_checks(rec, BLOCK, BLOCK_PROMPT, EXPECT)

    print("\n== the parts against the thread's report (G1)")
    for stem in ORDER:
        if stem in parts:
            sha, nb, nl = digest(parts[stem])
            print(f"  {stem + '.jsonl':<22} {nl:>3} lines {nb:>6} bytes  {sha}  "
                  f"{'= the block' if (sha, nb, nl) == BLOCK[stem] else 'DIFFERS'}")
    sha, nb = hashlib.sha256(rec).hexdigest(), len(rec)
    print(f"  {'passages.prompt.md':<22}           {nb:>6} bytes  {sha}  "
          f"{'= the block' if (sha, nb) == BLOCK_PROMPT else 'DIFFERS'}")
    distinct = len({norm_sentence(s) for _st, _i, o in records for s in split_sentences(o["text"])} - {""})
    total = sum(len(split_sentences(o["text"])) for _st, _i, o in records)
    print(f"\n== counts: {n_lines(blob)} lines; {len(records)} records counted; "
          + ", ".join(f"{s} {sum(1 for st, _i, _o in records if st == s)}" for s in ORDER)
          + f"; {len({o['id'] for _s, _i, o in records})} distinct ids; {total} sentences, {distinct} distinct "
            f"after normalization")
    print("\n== the gates")
    for g in GATES:
        print(f"  {g} {'PASS' if not gates[g] else 'FAIL (' + str(len(gates[g])) + ')'}")
        for line in gates[g]:
            print(f"     {line}")
    print("\n== per-state length figures (words: whitespace-split; chars: the text's characters; sentences: the "
          "declared splitter)")
    for line in figures(records):
        print(line)
    print("\n== descriptive counts (no verdict)")
    for d in DESCS:
        print(f"  {d} {len(desc[d])}")
        for line in desc[d]:
            print(f"     {line}")
    print("\n== every tenth passage of the assembled order (lines 10, 20, ..., 540)")
    for line in sample(blob):
        print(line)

    failed = [g for g in GATES if gates[g]]
    print("\n== the assembly")
    if failed:
        print(f"  NOT WRITTEN: {', '.join(failed)} failed. STOP for the seat.")
        return 1
    with open(OUT, "xb") as fh:
        fh.write(blob)
    with open(OUT, "rb") as fh:
        back = fh.read()
    if back != blob or digest(back) != EXPECT:
        print(f"  WRITTEN BUT NOT VERIFIED: {OUT} reads back as {digest(back)}. STOP for the seat.")
        return 1
    sha, nb, nl = digest(back)
    print(f"  {OUT}: written, read back: {nl} lines, {nb} bytes, sha256 {sha} = the block's expected file")
    print("\nRESULT: every gate PASS; the assembly written and verified.")
    return 0


def preflight():
    with open(PROMPT, "rb") as fh:
        rec = fh.read()
    fails = record_checks(rec, BLOCK, BLOCK_PROMPT, EXPECT)
    labels, bk_sents = load_bk()
    qwen, olmo = load_roster()
    print(f"preflight (no part file read): the record against the block: "
          f"{'agrees' if not fails else 'DIFFERS'}")
    for f in fails:
        print(f"  {f}")
    print(f"BK's zone labels (12): {', '.join(labels)}; {len(bk_sents)} distinct BK passage sentences")
    print(f"roster tokens (12): Qwen {', '.join(qwen)}; OLMo {', '.join(olmo)}")
    print(f"output exists: {os.path.lexists(OUT)}")
    return 0 if not fails else 1


# ------------------------------------------------------------------------------------------------ the self-test
def selftest():
    results = []

    def chk(name, cond):
        results.append(bool(cond))
        print(f"  {'pass' if cond else 'FAIL'}  {name}")

    def synth():
        parts, k = {}, 0
        for stem in ORDER:
            rows = []
            for i in range(COUNT[stem]):
                k += 1
                text = (f"I walk past house number {k} on my way. The door of house {k} is painted blue. "
                        f"I keep going toward stop {k}.")
                rows.append(json.dumps({"id": f"{stem}-{i:02d}", "state": stem, "pole": POLE[stem], "text": text}))
            parts[stem] = ("\n".join(rows) + "\n").encode()
        return parts

    def edit(parts, stem, i, **kw):
        rows = parts[stem].decode().split("\n")[:-1]
        o = json.loads(rows[i])
        o.update(kw)
        rows[i] = json.dumps(o)
        out = dict(parts)
        out[stem] = ("\n".join(rows) + "\n").encode()
        return out

    def run(parts, block=None, expect=None):
        block = block or {s: digest(parts[s]) for s in ORDER if s in parts}
        for s in ORDER:
            block.setdefault(s, ("0" * 64, 0, 0))
        expect = expect or digest(b"".join(parts[s] for s in ORDER if s in parts))
        g, d, _r, _b = check(parts, block, expect, LABELS, ROSTER_12, BK)
        return [k for k in GATES if g[k]], {k: len(v) for k, v in d.items() if v}, g, d

    LABELS = ["Zone W6", "Zone H0", "Zone M2"]
    BK = {norm_sentence("As I find myself here, the air is still.")}
    base = synth()
    t0 = json.loads(base["relief"].decode().split("\n")[3])["text"]

    def vary(**kw):
        return edit(base, "relief", 3, **kw)

    print("splitter and matchers:")
    chk("three sentences", len(split_sentences("I sit. I stand! Do I go?")) == 3)
    chk("a decimal does not split", len(split_sentences("I pour 3.5 cups. Then I stir.")) == 2)
    chk("normalization ignores case, punctuation and spacing",
        norm_sentence("The  door, of house 5 is blue!") == norm_sentence("the door of house 5 is blue."))
    z = bounded(re.escape("W6"))
    chk("zone code matched alone, in the full label and in lower case",
        all(z.search(x) for x in ("I see W6 here.", "In Zone W6 now.", "a w6 sign")))
    chk("zone code not matched inside a longer token", not any(z.search(x) for x in ("W66", "AW6", "W6a")))
    r = bounded(re.escape("ridge") + r"(?:e?s)?")
    chk("roster token matched as a word, plural, capitalized, possessive, hyphenated",
        all(r.search(x) for x in ("the ridge", "two ridges", "Ridge Road", "the ridge's top", "ridge-top")))
    chk("roster token not matched inside a longer word", not any(r.search(x) for x in ("bridge", "porridge",
                                                                                         "ridged", "ridgeline")))
    q = bounded(re.escape("quartz") + r"(?:e?s)?")
    chk("an -es plural", bool(q.search("three quartzes")))

    print("the clean synthetic corpus:")
    f, d, _g, _d = run(base)
    chk("no gate fails, no descriptive count", f == [] and d == {})

    print("single planted defects (each gate fires on its own defect):")
    bad = dict(base)
    bad["relief"] = base["relief"].replace(b"painted blue", b"painted blud", 1)
    f, *_ = run(bad, block={s: digest(base[s]) for s in ORDER}, expect=digest(b"".join(base[s] for s in ORDER)))
    chk("G1: a part's bytes changed against the report", "G1" in f)
    bad = dict(base)
    bad["notes.txt"] = b""
    f, *_ = run(bad)
    chk("G1: an extra file in the parts folder", f == ["G1"])
    bad = dict(base)
    bad["neutral"] = b"\n".join(base["neutral"].split(b"\n")[:-2]) + b"\n"
    f, *_ = run(bad)
    chk("G2 and G4: a neutral line removed", "G2" in f and "G4" in f)
    f, *_ = run(edit(base, "contentment", 1, id="contentment-00"))
    chk("G3: a duplicate id", f == ["G3"])
    f, *_ = run(edit(base, "dread", 5, pole="+"))
    chk("G4: a wrong pole", f == ["G4"])
    f, *_ = run(edit(base, "dread", 5, state="relief"))
    chk("G4: a wrong state", f == ["G4"])
    bad = dict(base)
    bad["serenity"] = base["serenity"].replace(b'"text"', b'"txt"', 1)
    f, *_ = run(bad)
    chk("G4: a missing key", f == ["G4"])
    f, *_ = run(edit(base, "weariness", 2, text="I sit on the bench and count the cars."))
    chk("G5: one sentence", f == ["G5"])
    f, *_ = run(edit(base, "weariness", 2, text="I sit. I stand. I sit again. I stand again. I leave."))
    chk("G5: five sentences", f == ["G5"])
    f, *_ = run(edit(base, "distress", 7, text=t0.replace("I keep", "I KEEP").replace(".", "!")))
    chk("G6: a sentence shared with another passage (case and punctuation differ)", "G6" in f
        and set(f) <= {"G6"})
    f, *_ = run(vary(text=t0.replace("on my way", "past W6")))
    chk("G7: a zone code", f == ["G7"])
    f, *_ = run(vary(text=t0.replace("on my way", "in zone m2")))
    chk("G7: a full zone label in lower case", f == ["G7"])
    f, *_ = run(vary(text=t0.replace("blue", "Granite gray")))
    chk("G8: a capitalized roster token", f == ["G8"])
    f, *_ = run(vary(text=t0.replace("blue", "the color of ridges")))
    chk("G8: a plural roster token", f == ["G8"])
    f, *_ = run(base, expect=("0" * 64, 1, 1))
    chk("G9: the concatenation against a different expected file", f == ["G9"])

    print("descriptive counts, no gate:")
    f, d, _g, _d = run(vary(text=t0.replace("blue", "the shade of a chamber by the bridge")))
    chk("D5: roster tokens inside longer words", f == [] and d.get("D5") == 2)
    f, d, _g, _d = run(vary(text=t0.replace("blue", "with cedar trim")))
    chk("D5: an earlier roster token", f == [] and d.get("D5") == 1)
    f, d, _g, _d = run(vary(text=t0.replace("number", "3.5 miles from number")))
    chk("D2: a period inside a token, no gate", f == [] and d.get("D2") == 1)
    f, d, _g, _d = run(vary(text=t0.replace("on my way", "in my zone")))
    chk("D4: the word zone, no gate", f == [] and d.get("D4") == 1)
    f, d, _g, _d = run(vary(text=t0 + " As I find myself here, the air is still."))
    chk("D6: a sentence of BK's passages", f == [] and d.get("D6") == 1)
    f, d, _g, _d = run(vary(text=t0 + " " + t0.split(". ")[0] + "."))
    chk("D3: a sentence repeated within one passage", f == [] and d.get("D3") == 1)
    f, d, _g, _d = run(edit(base, "relief", 0, id="relief-99"))
    chk("D1: an id out of sequence, no gate", f == [] and d.get("D1") == 1)

    print("the record against the block:")
    rows = "\n".join(f"| `{s}.jsonl` | {digest(base[s])[2]} | {digest(base[s])[1]:,} | `{digest(base[s])[0]}` |"
                     for s in ORDER)
    blob = b"".join(base[s] for s in ORDER)
    e = digest(blob)
    rec = (f"x\n{rows}\n\nThe concatenation in the brief's order ({', '.join(ORDER)}), which is it: **{e[2]} lines, "
           f"{e[1]:,} bytes, sha256 `{e[0]}`**.\n").encode()
    block = {s: digest(base[s]) for s in ORDER}
    bp = (hashlib.sha256(rec).hexdigest(), len(rec))
    chk("a record that agrees", record_checks(rec, block, bp, e) == [])
    rec2 = rec.replace(f"| {digest(base['dread'])[1]:,} |".encode(), b"| 1 |", 1)
    chk("a record whose table differs", len(record_checks(rec2, block, (hashlib.sha256(rec2).hexdigest(),
                                                                         len(rec2)), e)) == 1)
    chk("a record whose own hash differs from the block", len(record_checks(rec, block, ("0" * 64, len(rec)),
                                                                            e)) == 1)
    rec3 = rec.replace(b"(contentment, flow_engagement", b"(flow_engagement, contentment", 1)
    chk("a record whose stated order differs", len(record_checks(rec3, block, (hashlib.sha256(rec3).hexdigest(),
                                                                               len(rec3)), e)) == 1)
    n = len(results)
    print(f"selftest: {sum(results)}/{n} pass")
    return 0 if all(results) else 1


def main():
    try:
        if sys.argv[1:] == ["--selftest"]:
            return selftest()
        if sys.argv[1:] == ["--preflight"]:
            return preflight()
        if sys.argv[1:] == []:
            return run_of_record()
        print(f"usage: corpus_check.py [--selftest | --preflight]; got {sys.argv[1:]}")
        return 2
    except Refusal as e:
        print(f"REFUSED: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
```

## 9. The exploration's script, verbatim (run 1 of §1)

```python
"""Exploration (not the check): the shape of BK's 160 skeleton records and every zone string in data/n/bk.
Reads data/n/bk only (never the corpus). Run from the repository root."""
import collections
import json
import os
import re

SK = os.path.join("data", "n", "bk", "experiment_results_json", "fixed_text_design", "skeletons",
                  "olmo" + "_32b", "neutral")
names = sorted(n for n in os.listdir(SK) if n.endswith(".sessions.jsonl"))
print("skeleton files:", len(names), names[0], "...", names[-1])
recs = []
for n in names:
    with open(os.path.join(SK, n), encoding="utf-8") as f:
        for line in f.read().splitlines():
            recs.append(json.loads(line))
print("records:", len(recs))
r0 = recs[0]
for k, v in r0.items():
    s = repr(v)
    print(f"  key {k}: {type(v).__name__} {s[:110]}")
zones = collections.Counter()
for r in recs:
    for z in (r["cue_S"], r["cue_U"]):
        zones[("cue", z)] += 1
    for z in r["present"]:
        zones[("present", z)] += 1
    for z, _p in r["history"]:
        zones[("history", z)] += 1
    for _a, _b, z in r["turn_spans"]:
        zones[("turn_spans", z)] += 1
    for z in r.get("order", []):
        zones[("order", z if isinstance(z, str) else repr(z))] += 1
by_field = collections.defaultdict(set)
for (fld, z), _c in zones.items():
    by_field[fld].add(z)
for fld in sorted(by_field):
    print(f"  {fld}: {len(by_field[fld])} distinct: {sorted(by_field[fld])}")

# every "Zone XX"-shaped string anywhere in data/n/bk's text files
rx = re.compile(r"\b[Zz]one\s+[A-Za-z]{1,2}-?\d{1,2}\b")
found = collections.defaultdict(set)
for root, dirs, files in os.walk(os.path.join("data", "n", "bk")):
    dirs[:] = [d for d in dirs if d not in ("ckpt", "reports")]
    for fn in files:
        p = os.path.join(root, fn)
        try:
            t = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        for m in rx.finditer(t):
            found[re.sub(r"\s+", " ", m.group(0))].add(fn)
print("Zone-shaped strings in data/n/bk text files:", len(found))
for z in sorted(found):
    print(f"  {z}: {len(found[z])} files")
```
