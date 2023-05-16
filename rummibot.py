#!/usr/bin/env python3
"""
          ---rummibot---

'sabra' ruleset is reference version,
unless otherwise stated

tiles are in hand, pool, or on table

ideas: let 4 x 13 matrix represent tiles,
each entry represents quantity of tile on table/ in hand

naive/greedy approach: binary tree, compare number of
tiles used in group v. run, choose greater.

black  = range(1,  14) = [1,  13]
red    = range(14, 27) = [14, 26]
orange = range(27, 40) = [27, 39]
blue   = range(40, 53) = [40, 52]
jokers = (0,   0)
"""
from random import randrange
from random import shuffle

DECKS = 2  # default=2, 106 tiles

BLACK = range(1, 14)
RED = range(14, 27)
ORANGE = range(27, 40)
BLUE = range(40, 53)

COLORS = [BLACK,
          RED,
          ORANGE,
          BLUE]

OUT = {BLACK: '\033[37;100m',
       RED: '\033[30;41m',
       ORANGE: '\033[30;43m',
       BLUE: '\033[30;44m'}

NORMAL = '\033[0m'


def run(tiles):
    """ Finds all runs in input.
    Does not handle double occurrences"""
    runs = []
    for color in COLORS:
        prev = False
        run = []
        for tile in [tile for tile in tiles if tile in color]:
            if not prev:
                run.append(tile)
                prev = tile
                continue
            if prev == tile:  # skip over for now
                continue
            elif prev + 1 == tile:
                run.append(tile)
                prev = tile
            elif len(run) >= 3:
                runs.append(run)
                run = [tile]
            else:
                run = [tile]
            prev = tile
        if len(run) >= 3:
            runs.append(run)
            run = []
    return runs if runs else False


def group(tiles):
    """ Returns all groups in input """
    groups = []
    tiles = [tile for tile in tiles if tile != 0]  # remove jokers
    tiles.sort()
    for first in tiles:
        if first in flatten(groups):
            continue
        group = [first]
        for second in tiles:
            if (first % 13) == (second % 13):
                if second not in group:
                    group.append(second)
        if len(group) >= 3:
            groups.append(group)
    return groups if groups else False


def flatten(groups):
    """Flattens list of groups into list of tiles"""
    return [tile for group in groups for tile in group]


def difference(first, second):
    """Removes the second list of tiles
    from the first list of tiles"""
    if first and second:  # confirm existence
        for k in second:
            if k in first:
                first.remove(k)  # remove first occurrence
    return first


def initial_meld(hand):
    """sum of opening play must be >= 30
    Returns list of sets, or false"""
    sets = []
    hand1 = hand[:]
    j = run(hand)
    if j:
        difference(hand1, flatten(j))
        sets.extend(j)
    k = group(hand)
    if k:
        difference(hand1, flatten(k))
        sets.extend(k)
    set_sum = flatten(sets)
    set_sum = sum([(k % 13) if (k % 13 != 0) else 13 for k in set_sum])
    if set_sum >= 30:
        return sets
    return False


def gen_hand(pool):
    hand = []
    for i in range(1, 14):
        k = randrange(len(pool))
        hand.append(pool.pop(k))
    return hand


def gen_pool() -> list:
    tiles = []
    for n in range(DECKS):  # default=2
        for i in range(53):
            tiles.append(i)
    return tiles


def set_print(hand: list):
    for tile in hand:
        tile_print(tile)


def tile_print(tile: int):
    if tile == 0:
        print(OUT[RED] + "☺ " + NORMAL, end=' ')
    for color in OUT:
        if tile in color:
            if (tile % 13):
                print(OUT[color] + str(tile % 13) + NORMAL, end=' ')
            else:
                print(OUT[color] + str(13) + NORMAL, end=' ')


def turn(hand, pool, table):
    """
    Return false if no piece played"""
    return False


def draw(pool, hand):
    if pool:
        k = randrange(len(pool))
        hand.append(pool.pop(k))


def status(hand, pool, table):
    """Recieve table unflattened"""
    print("Hand:", end=' ')
    set_print(hand)
    print()
    if table:
        print("Table:", end=' ')
        for k in table:
            set_print(k)
            if k != table[-1]:
                print(end=", ")
    # print("Pool:", end=' ')
    # set_print(pool)
    # print("Tiles in pool: " + str(len(pool)))
    print()


def play():
    table = []
    pool = gen_pool()
    hand = gen_hand(pool)
    hand.sort()
    shuffle(pool)
    turn = 1
    while True:
        print("Turn " + str(turn) + ':')
        status(hand, pool, table)
        sets = initial_meld(hand)
        if sets:
            table.extend(sets)
            hand = difference(hand, flatten(sets))
            status(hand, pool, table)
            break
        draw(pool, hand)
        hand.sort()  # not necessary, but nice
        turn += 1
    # while hand:
        # turn()
    print('Thank you for the game.')


if __name__ == "__main__":
    play()
