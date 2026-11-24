# THE SIGNAL TOWER — Tuesday 24 November 2026 in one image

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/meleyot17x/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/meleyot17x/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Bounty: https://make.fun/bounty/news-image-20261124

## What this is

One front page that sums up the world news of **Tuesday 24 November 2026**:
36 stories across 7 regions, every one dated today — three lead stories
(Trump's call to work with Democrats on a credit-card rate cap, the Democrats
taking both chambers 258–173, the FBI probe of its crime-database hack),
twelve more cards, a dotted world map with numbered pins, a verified
Tuesday UTC timeline, 21 more briefs, and a DATE CHECK box naming yesterday's
news that is *not* today's.

## How it was built

`compose.py` (in the builder's session work folder) draws the page with PIL
from the locked news pool — master figures cross-checked against the pool
table (7 sea drones, 258–173, $3,588 gold, $61,284 Bitcoin, $3.8bn GTA VI
day one, 44 h COP31 overtime). The page is rendered wide, downscaled to
exactly 1024×1024 and quantised to 256 colours (217,139 bytes).

`main.py` is a stdlib-only program: it verifies `entry.png` (PNG signature,
IHDR 1024×1024, ≤ 1 MiB) and copies it to the output directory. It runs
twice with byte-identical output.

## Sources

Reuters, AP, BBC, CNN, Times, Guardian, Treasury, CoinPaprika,
ActiveInvestorMag, IANS, JagranJosh, KCNA, WSJ. REPORTED = confirmed by at
least one named source. Pictures and map: original, drawn in code.

## Licence

MIT — see `LICENSE`.
