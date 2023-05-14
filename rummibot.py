"""
       ---rummibot---
'sabra' ruleset is reference version,
unless otherwise stated

black  = range(1,  14) = [1,  13]
red    = range(14, 27) = [14, 26]
orange = range(27, 40) = [27, 39]
blue   = range(40, 53) = [40, 52]
jokers = (0,   0)
"""
from random import randrange

black = '\033[37;100m'
red = '\033[30;41m'
orange = '\033[30;43m'
blue = '\033[30;44m'
normal = '\033[0m'

# implement game class to store tiles, played


def tile_gen() -> list:
    tiles = []
    for i in range(53):
        tiles.append(i)
        tiles.append(i)
    return tiles


def hand_print(hand: list):
    for tile in hand:
        tile_print(tile)
    print()


def tile_print(tile: int):
    if (1 <= tile <= 13):
        tile = tile % 13
        if not tile:
            tile = 13
        print(black + str(tile) + normal, end=' ')
    if (14 <= tile <= 26):
        tile = tile % 13
        if not tile:
            tile = 13
        print(red + str(tile) + normal, end=' ')
    if (27 <= tile <= 39):
        tile = tile % 13
        if not tile:
            tile = 13
        print(orange + str(tile) + normal, end=' ')
    if (40 <= tile <= 54):
        tile = tile % 13
        if not tile:
            tile = 13
        print(blue + str(tile) + normal, end=' ')


def run_check(hand):
    hand.sort()
    prev = None
    run = []
    for tile in hand:
        if tile == 0:  # joker clause
            continue
        if not prev:
            prev = tile
            continue
        if tile == prev + 1:
            run.append(tile)
        elif len(run) >= 3:
            return run
        else:
            run = []
        prev = tile
    return False


def group_check(hand):
    for first in hand:
        if first == 0:  # joker clause
            continue
        group = [first]
        for second in hand:
            if second == 0:  # joker clause
                continue
            if (first % 13) == (second % 13):
                if second not in group:
                    group.append(second)
        if len(group) >= 3:
            return group
    return False


# recieves run/group, checks no duplicates
def duplicate_remove(list):
    pass


def turn(hand):
    pass


# sum of opening play must be >- 30
def opening(hand):
    group = group_check(hand)
    run = run_check(hand)
    score = 0
    if run:
        for tile in run:
            to_add = tile % 13
            if to_add == 0:
                score += 13
            else:
                score += to_add
    if group:
        for tile in group:
            to_add = tile % 13
            if to_add == 0:
                score += 13
            else:
                score += to_add
    if score >= 30:
        if run:
            print("Run: ", end='')
            hand_print(run)
        if group:
            print("Group: ", end='')
            hand_print(group)
        return True
    return False


def hand_gen(pool):
    hand = []
    for i in range(1, 14):
        k = randrange(len(pool))
        hand.append(pool.pop(k))
    return pool, hand


def draw(pool, hand):
    k = randrange(len(pool))
    hand.append(pool.pop(k))
    return pool, hand


def play():
    pool = tile_gen()
    pool, hand = hand_gen(pool)
    print(hand)
    hand_print(hand)
    hand.sort()
    hand_print(hand)
    while True:
        hand_print(hand)
        if opening(hand):
            break
        else:
            pool, hand = draw(pool, hand)
    # game()
    print('Thank you for the game.')


if __name__ == "__main__":
    play()
