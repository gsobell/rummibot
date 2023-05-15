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

color_black = '\033[37;100m'
color_red = '\033[30;41m'
color_orange = '\033[30;43m'
color_blue = '\033[30;44m'
color_normal = '\033[0m'

black = range(1, 14)
red = range(14, 27)
orange = range(27, 40)
blue = range(40, 53)


def hand_gen(pool):
    hand = []
    for i in range(1, 14):
        k = randrange(len(pool))
        hand.append(pool.pop(k))
    return pool, hand


def pool_gen() -> list:
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
    if tile == 0:
        print(color_black + '☺ ' + color_normal, end=' ')
    out = tile % 13
    if not out:
        out = 13
    if tile in black:
        print(color_black + str(out) + color_normal, end=' ')
    if tile in red:
        print(color_red + str(out) + color_normal, end=' ')
    if tile in orange:
        print(color_orange + str(out) + color_normal, end=' ')
    if tile in blue:
        print(color_blue + str(out) + color_normal, end=' ')
    # if out <= 9:
        # print(end=' ') # padding for nicer cols


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


"""
Sets with 3 elements don't branch the game tree
Each group with 4 tiles creates 4 more options in the game tree
Runs can be 3 < n < 13:
Ways to divide a string of n into segments, each one =>3
For runs 5 < n, we have the option of spliting them into sub-runs,
Thankfully, this is rare, so it almost always will not affect runtime4
"""


def turn(hand):
    pass

# def initial_meld(hand):
#     """sum of opening play must be >- 30"""
#     recursive_meld(hand)
#
#
# def recursive_meld(hand, groups=[], path=[]):
#     """use backtracking to find largest initial_meld """
#     pass
#


def old_init_meld(hand):
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


def draw(pool, hand):
    k = randrange(len(pool))
    hand.append(pool.pop(k))
    return pool, hand


def play():
    pool = pool_gen()
    pool, hand = hand_gen(pool)
    print(hand)
    hand_print(hand)
    hand.sort()
    hand_print(hand)
    while True:
        hand_print(hand)
        if old_init_meld(hand):
            break
        else:
            pool, hand = draw(pool, hand)
    # game()
    print('Thank you for the game.')


if __name__ == "__main__":
    play()
