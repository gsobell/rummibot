# rummibot (working title)

rummibot is a rummikub solver

The 13 tiles in 4 colors are represented as integers from 1 to 52 in this implementation.
Jokers are represented by 0. There are two of each tile. Runs can be constructed by comparing size, just one comparison, as opposed to both size and color.

Groups will all have the same `modulo 13` as the other members of the group. Note that care must be taken to not confuse `0`, Jokers, with `13 % 13`, the black 13 tiles, mainly in the context of printing to the `stdout`.

Current goal is to use a greedy algorithm to create as many valid runs/groups per turn. Future revision may include withholding tiles for strategic purposes.

The initial meld and each subsequent turn are functionally identical problems, so they can be solved with the same algorithm. However, they have different constraints: the initial meld must sum to over 30, while subsequent turns must use all the tiles on the table and at least one from the player's hand.

### Glossary
- _set_ -  a run or group
- _run_ - 3 or 4 tiles of the same number, all diffrent colors
- _group_ - 3 or more tiles in ascending order, all same color
- _initial meld_ - first turn, sum of points must be at least 30
- _hand_ - also called rack, tiles
- _table_ - sets placed on by players on their turn

## Usage

No arguments or options currently.
```sh
python rummibot.py
```

## Features

### Current
- Colored tiles
- Game setup
- Select initial valid meld from hand

### Future
- Backtracking
- Count cards (tiles?)
- Count each players remaining tiles
- Solve user inputed games
- Plot and scheme

### Moonshots
- Tile shuffling animation
- Easy to use GUI/TUI
- Rewrite in [hylang](https://hylang.org/)

`rummibot` is a work in progress

***
#### See also:
- [The Complexity of Rummikub Problems](https://liacs.leidenuniv.nl/~takesfw/pdf/rummikub.pdf)
- [slides for the above paper](https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/15-BNAIC-Complexity-slides.pdf)
