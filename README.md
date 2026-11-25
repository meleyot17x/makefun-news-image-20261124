# THE BEACON HERALD — Tuesday 24 November 2026 in one image

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/meleyot17x/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/meleyot17x/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Bounty: https://make.fun/bounty/news-image-20261124

## What this is

One broadsheet front page that sums up the world news of **Tuesday 24 November 2026**: THE BEACON HERALD, 35 stories across 9 regions, every one dated today.

The three lead stories are hard news: Russian strikes kill at least 15 near Kyiv with 11 dead in the Dymer flats; Nvidia brings back Jensen Huang as CEO and shares leap 31%; a strike kills 11 in western Yemen, the Houthis say. Below the leads sit ten more scene cards — Ukraine sinks the Russian warship Merkury off Benghazi, the cargo ship Sparta II hit and towed clear in the Gulf of Finland, COP31 ending with no deal, US sanctions on about 30 Iran exchange houses, Israeli strikes in Gaza City, gold rebounding to $3,588 an ounce, Bitcoin steadying at $61,284, GTA VI taking $3.8bn on day one, a drawn Wellington Test, and Liverpool routing Manchester United 4–0.

A black briefs panel carries stories 14–35 under the header "BRIEFS 14-35 · 35 STORIES IN ALL", so the numbering runs 1–13 on the cards and 14–35 in the briefs with nothing missing and nothing counted twice — the last row of each brief column (Nepal's PM ending his Delhi visit on the left, the Christchurch Test forecast on the right) sits fully inside the panel, clear of the boxes below it. A region bar at the top counts all nine regions (Europe 7 · Middle East 4 · Africa 1 · Americas 9 · Asia 2 · South Asia 4 · Asia-Pacific 2 · Oceania 2 · World 4), a dotted world map pins the numbered scenes, and a DATE CHECK box names the older stories that were deliberately excluded.

## How it was built

The page is drawn in code from the locked Tuesday news pool and rendered at exactly 1024×1024. Every card carries a REPORTED tag naming its wire or agency source on its own black strip, and each statistic chip stands alone on the card's bottom row. `main.py` is a stdlib-only program: it verifies `entry.png` (PNG signature, IHDR 1024×1024, ≤ 1 MiB) and copies it to the output directory. It runs twice with byte-identical output.

## Sources

Reuters, AP, CNN, Times, WSJ, Guardian, BBC, Treasury, CoinPaprika, HK News TV, IANS, JagranJosh, KCNA. REPORTED = confirmed by at least one named source. Pictures and map: original, drawn in code.

## Licence

MIT — see `LICENSE`.
