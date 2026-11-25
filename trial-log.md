# Trial log — makefun-techsupport-off

## v1 (25 Nov 2026, ~18:53 WITA)

- `main.py` run: `python3 main.py`
- Result: wrote 77 chars to `/output/entry.txt`, exit 0.
- Verified after the run: file holds exactly the entry plus a trailing
  newline — 1 line, 77 characters without the newline, 80 bytes UTF-8
  (the em dash is 3 bytes). Inside the 1–199 character gate.
- Entry: `My headset battery's at 2% — if I vanish mid-sentence, just assume it worked.`
- No second version was needed: the first run passed the length and
  single-line checks, so there was nothing to fix. The entry text itself
  was chosen before the run, from field research (see README).

## Field research behind the entry

- Source: live competition data, 25 Nov 2026 — 1,228 submissions,
  930 with a real title (298 used the competition title as a placeholder).
- Saturated clusters found: the full "have you tried turning it off and
  on again" sentence (71 exact copies), the escalation / Tier-2-is-me loop
  (97 containing "escalat"), the restarted-ticket gag (verbatim twice),
  the script-ran-out gag (verbatim once).
- Freshness check for the chosen line: "battery" 0 hits, "vanish" 0 hits,
  "assume it worked" 0 hits in the 930 real titles; the two
  "mid-sentence" hits are unrelated lines. Full counts in the session notes
  under `techsupport/field-analysis.txt`.
