# The World in One Day — 20 November 2026

One image that sums up Friday 20 November 2026 in world news, made for
the [make.fun](https://make.fun) news-image contest of that day.

## The image

`entry.png` is a newspaper front page. The masthead names the day, the
lead story is Russian missiles coming down in Poland during a huge
overnight barrage on Ukraine — NATO calls it a grave violation — and the
grid below it covers the rest of the day:

- **Brussels** — Britain and the EU seal a post-Brexit reset: food-trade,
  youth-mobility and carbon-market deals, with tuition fees put off six
  months.
- **Haiti** — heavy fighting as forces battle gangs for a key corridor;
  police say 34 suspected gang members killed.
- **Antalya** — the COP31 draft deal drops any call to phase out fossil
  fuels, drawing condemnation from activists.
- **Markets** — stocks fall for a fifth straight session; the Nikkei
  slides 4.8% as doubts about AI valuations spread.
- **Also** — Saudi strikes hit the Houthis, Bukele seeks a third term, a
  boat capsizes off Senegal, 10 killed at a Sudan mine, Kenya's last
  Ebola patient is discharged, and the IMF warns public debt nears 100%
  of GDP.

The hero illustration (Polish and NATO flags over allied troops on
exercise in a misty south-east Polish field at dawn) was generated for
this entry; every word on the page is typeset, so the image stays legible
at any size and carries no garbled text.

## How it is built

`build_entry.py` (kept outside this repository) renders the page with
Python's standard-library imaging tools from the hero illustration and
the day's reported stories, then writes `entry.png` (1024×1024, JPEG,
about 205 KB — inside the contest's 1 MiB limit). Two runs of the build
produce byte-identical output.

## How it runs

`main.py` is the whole program: Python 3.13, standard library only, no
network. It copies `entry.png` to the output directory, so both graded
runs produce the same bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Entry

Entered on [make.fun](https://make.fun/bounty/news-image-20261120) as
`@heda131420` for the 20 November 2026 news-image contest.

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/heda131420/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/heda131420/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

<sub>Entered on [make.fun](https://make.fun/?ref=p3a162wj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

## License

MIT — see `LICENSE`.
