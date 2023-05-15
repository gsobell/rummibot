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
        print(color_black + '☺' + color_normal, end=' ')
    out = tile % 13
    if not out:
        out = 13
    if (1 <= tile <= 13):
        print(color_black + str(out) + color_normal, end=' ')
    if (14 <= tile <= 26):
        print(color_red + str(out) + color_normal, end=' ')
    if (27 <= tile <= 39):
        print(color_orange + str(out) + color_normal, end=' ')
    if (40 <= tile <= 54):
        print(color_blue + str(out) + color_normal, end=' ')


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


def turn(hand):
    pass

# recieves list of groups, returns score


def score_groups(groups):
    for group in groups:
        for tile in group:
            if tile == 0:  # jokers, implement later
                continue
            to_add = tile % 13
            if to_add == 0:
                score += 13
            else:
                score += to_add
    return score



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
