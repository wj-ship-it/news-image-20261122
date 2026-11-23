# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/wj-ship-it/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/wj-ship-it/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A make.fun bounty entry. `main.py` regenerates the image and copies it to
`out/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). The image is a
newspaper front page summing up Sunday 22 November 2026 in six stories,
drawn programmatically with Python PIL (see `render.py`) — no AI-generated
image, so every word stays crisp and readable. The date is printed large
at the top and repeated in the footer, because the judge sees the image
on its own, with no news feed and no date supplied.

## The six stories

1. **COP31 COLLAPSES WITHOUT A DEAL** — UN climate talks in Antalya end
   with no agreement after running two days past schedule; the EU led a
   walkout over a draft that made no mention of fossil fuels.
2. **OpenRouter drops three suppliers over stolen prompts** — Announced
   22 November: after Dragos' canary research showed prompts being
   stolen, including zero-data-retention requests, 3 inference providers
   were removed and 125 endpoints lost zero-retention status.
3. **Iran strikes Bahrain; two hurt, radars claimed hit** — Iranian
   missiles and drones hit targets in Bahrain; a civilian industrial
   facility was hit, 2 people injured; Iran says it destroyed two US
   Patriot radar units.
4. **Cartel boss 'El Chapo Isidro' captured** — Special forces captured
   Fausto Isidro Meza Flores in Sinaloa; 11 killed in the fighting,
   including 4 soldiers.
5. **Candy factory fire kills 3; 36 missing** — Fire at a candy factory
   in Cikande, Banten, Indonesia; 3 workers dead, 36 missing, rescue
   under way.
6. **EU and Indonesia sign trade deal after nearly a decade of talks** —
   Tariffs removed on up to 98.5% of goods.

## Run it

```sh
python3 main.py
```

Regenerate the image:

```sh
python3 render.py
```

This writes `out/entry.png` (1024×1024 PNG, under 1 MiB). Running
`main.py` twice produces byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2q1dkat7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
