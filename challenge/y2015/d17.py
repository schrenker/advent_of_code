from collections import defaultdict
from itertools import chain, combinations

test_results = {"part_one": {1: 41}, "part_two": {1: 20}}


def part_one(input: str):
    containers = [int(x) for x in input.splitlines()]
    acc = 0
    for comb in chain(
        *(list(combinations(containers, i + 1)) for i in range(len(containers)))
    ):
        if sum(comb) == 150:
            acc += 1
    return acc


def part_two(input: str):
    containers = [int(x) for x in input.splitlines()]
    used = defaultdict(int)
    for comb in chain(
        *(list(combinations(containers, i + 1)) for i in range(len(containers)))
    ):
        if sum(comb) == 150:
            used[len(comb)] += 1

    return used[min(used.keys())]
