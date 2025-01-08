from functools import reduce
from operator import mul
import itertools

test_results = {"part_one": {1: 99}, "part_two": {1: 44}}


def quantum_entanglement(conv, group):
    for ln in range(2, len(conv) + 1):
        found = list()
        for i in itertools.permutations(conv, ln):
            if sum(i) == group:
                found.append(i)
        if len(found) > 0:
            return min([reduce(mul, x) for x in found])


def part_one(input: str, test_run=False):
    conv = list(reversed([int(x) for x in input.splitlines()]))
    group = sum(conv) // 3
    return quantum_entanglement(conv, group)


def part_two(input: str, test_run=False):
    conv = list(reversed([int(x) for x in input.splitlines()]))
    group = sum(conv) // 4
    return quantum_entanglement(conv, group)
