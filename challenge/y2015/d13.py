from collections import defaultdict
import itertools


test_results = {"part_one": {1: 330}, "part_two": {1: 286}}


def parse_input(input):
    result = defaultdict(dict)
    for i in input.splitlines():
        spl = i.rstrip(".").split(" ")
        result[spl[0]][spl[10]] = int(spl[3]) if spl[2] == "gain" else -int(spl[3])
    return result


def calculate_happiness(arrang, seats):
    acc = 0
    for i in range(-1, len(arrang) - 1):
        acc += seats[arrang[i]][arrang[i - 1]] + seats[arrang[i]][arrang[i + 1]]
    return acc


def part_one(input: str):
    seats = parse_input(input)
    acc = 0
    for arrang in itertools.permutations(seats):
        tmp = calculate_happiness(arrang, seats)
        if tmp > acc:
            acc = tmp
    return acc


def part_two(input: str):
    seats = parse_input(input)
    for i in list(seats.keys()):
        seats["me"][i] = 0
        seats[i]["me"] = 0
    acc = 0
    for arrang in itertools.permutations(seats):
        tmp = calculate_happiness(arrang, seats)
        if tmp > acc:
            acc = tmp
    return acc
