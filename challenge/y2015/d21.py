import itertools
import math

# No valuable tests provided by AoC
test_results = {"part_one": {}, "part_two": {}}

weapons = {
    8: (4, 0),
    10: (5, 0),
    25: (6, 0),
    40: (7, 0),
    74: (8, 0),
}

armors = {
    0: (0, 0),
    13: (0, 1),
    31: (0, 2),
    53: (0, 3),
    75: (0, 4),
    102: (0, 5),
}

rings1 = {
    0: (0, 0),
    25: (1, 0),
    50: (2, 0),
    100: (3, 0),
    20: (0, 1),
    40: (0, 2),
    80: (0, 3),
}

rings2 = {
    0: (0, 0),
    25: (1, 0),
    50: (2, 0),
    100: (3, 0),
    20: (0, 1),
    40: (0, 2),
    80: (0, 3),
}


def part_one(input: str, test_run=False):
    hp = 100
    boss = tuple(int(x.split()[-1]) for x in input.splitlines())
    cost_set = set()
    for i in itertools.product(weapons, armors, rings1, rings2):
        if i[2] == i[3] and i[2] != 0:
            continue
        attack = weapons[i[0]][0] + rings1[i[2]][0] + rings2[i[3]][0]
        armor = armors[i[1]][1] + rings1[i[2]][1] + rings2[i[3]][1]
        turns_to_kill = math.ceil(boss[0] / max(1, attack - boss[2]))
        if (turns_to_kill - 1) * max(1, boss[1] - armor) < hp:
            cost_set.add(sum(i))

    return min(cost_set)


def part_two(input: str, test_run=False):
    hp = 100
    boss = tuple(int(x.split()[-1]) for x in input.splitlines())
    cost_set = set()
    for i in itertools.product(weapons, armors, rings1, rings2):
        if i[2] == i[3] and i[2] != 0:
            continue
        attack = weapons[i[0]][0] + rings1[i[2]][0] + rings2[i[3]][0]
        armor = armors[i[1]][1] + rings1[i[2]][1] + rings2[i[3]][1]
        turns_to_kill = math.ceil(boss[0] / max(1, attack - boss[2]))
        if (turns_to_kill - 1) * max(1, boss[1] - armor) >= hp:
            cost_set.add(sum(i))

    return max(cost_set)
