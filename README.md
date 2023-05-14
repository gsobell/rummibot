# rummibot (working title)

rummibot is a rummikub solver

The 13 tiles in 4 colors are represented as integers 1-52.
Jokers are represented by 0.

Runs will be can be constructed by testing relative size, one comparison, not both size and color.
Groups will all have the same `modulo 13` as the other members of the group.

Initial goal is to use a greedy algorithm to get rid of as many possible tiles each turn. Future revision may include withholding tiles for strategic purposes. 

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
