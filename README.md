# makefun-techsupport-off

[![bounty](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rwnliwan/makefun-techsupport-off/rank.svg)](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rwnliwan/makefun-techsupport-off/reward.svg)](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

One funny line for the make.fun bounty
[Have You Tried Turning It Off?](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b):
a single reply from a hopeless tech support agent to a desperate customer,
under 200 characters.

## The entry

> My headset battery's at 2% — if I vanish mid-sentence, just assume it worked.

77 characters. The joke is the agent's own gear dying on him: the "fix" he
offers the customer is his own disappearance, framed as success. The
customer is never the butt of it — the agent and his headset are.

## How it works

`main.py` writes the line to `/output/entry.txt` (one line, UTF-8, 1–199
characters, inside the gate). Nothing else is computed; the entry is a
fixed, hand-written line chosen after field research.

## Field research (25 Nov 2026)

The field was 1,228 submissions, 930 with a real title (298 were the
competition title as a placeholder). Saturated clusters, counted from the
live field:

- "have you tried turning it off and on again" and its variants — the core
  cliché, 71 exact copies of the full sentence, 165 containing
  "turning it off".
- The escalation loop — "escalated to tier" 22 times, "tier is me" 8 times;
  Tier 2 turning out to be the same agent in a different headset is a
  well-worn angle.
- "Good news — I turned your ticket off and on again" appears verbatim
  twice; the agent's own computer being the one restarted is also taken.
- "I'm reading from a script, and we've reached the last page. It just
  says 'good luck.'" — the script-ran-out angle is taken verbatim too.

The chosen line avoids all of them: "battery" and "vanish" appear in zero
of the 930 real titles, and the two "mid-sentence" hits are unrelated
(a frozen mum, a router). The freshness is in the voice and the situation —
the agent about to drop off the call himself — not in another twist on the
power button.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
