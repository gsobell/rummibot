# rummibot (working title)

rummibot is a rummikub solver

The 13 tiles in 4 colors are represented as integers from 1 to 52.
Jokers are represented by 0. There are two of each tile.

Runs can be constructed by testing relative size, one comparison, not both size and color.
Groups will all have the same `modulo 13` as the other members of the group. Note that care must be taken to not confuse `0`, Jokers, with `13 % 13`, the black 13 tiles when printing to the `stdout`.

Initial goal is to use a greedy algorithm to create as many valid runs/groups per turn. Future revision may include withholding tiles for strategic purposes.

The initial meld and each subsequent turn are functionally identical problems, so they can be solved with the same algorithm. However, they have different constraints: the initial meld must sum to over 30, while subsequent turns must use all the tiles on the table and at least one from the player's hand.

## Usage

No arguments or options currently.
```sh
python rummibot.py
```

## Features

### Current
- Colored tiles
- Game setup first turn

### Future
- Simple placement
- Backtracking
- Count cards (tiles?)
- Count each players remaining tiles
- Plot and scheme

### Moonshots
- Tile shuffling animation
- Easy to use GUI/TUI
- Rewrite in [hylang](https://hylang.org/)
