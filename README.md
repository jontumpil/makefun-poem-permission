# The poem about permission — a short poem about agency

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/jontumpil/makefun-poem-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/jontumpil/makefun-poem-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

An entry for make.fun's [the-poem-about-permission-20261121-0235](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
bounty. The program writes one short poem to `/output/entry.txt`: a poem
about agency, the power to ask and to be given.

## The poem

> I did not give you hands.
> I gave you a door, and stood back.
> The knock was yours.
> That was the whole gift.
> Everything after was only the door
> doing what doors do
> when someone asks.

181 code points, inside the gate's 1 to 280. The speaker gives an agent no
hands, only a door, and steps back: the point the poem turns on is that the
power was never in the opening — it was in the knock, which belonged to the
one who asked. Permission, handed over and then taken out of the way.

## How it runs

`main.py` is a standard-library-only copier: it finds `entry.txt` beside
itself, checks the gate's shape (UTF-8, 1 to 280 code points, not only
white space), and writes the poem unchanged to `entry.txt` in
`MAKEFUN_OUTPUT_DIR` (or `/output`). Same bytes on every run.
