from collections import defaultdict
from typing import Counter

test_results = {"part_one": {1: 4}, "part_two": {1: 7}}

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def parse_input(input):
    result = defaultdict(bool)
    spl = input.splitlines()
    for i, row in enumerate(spl):
        for j, col in enumerate(row):
            if col == "#":
                result[(i, j)] = True
    return result, len(spl), len(spl[0])


def resolve(state, x, y):
    tmp = defaultdict(bool)
    for i in range(x):
        for j in range(y):
            neigh = 0
            for d in directions:
                if 0 <= i + d[0] < x and 0 <= j + d[1] < y:
                    neigh += 1 if state[(i + d[0], j + d[1])] else 0
            if state[(i, j)]:
                if neigh == 2 or neigh == 3:
                    tmp[(i, j)] = True
            else:
                if neigh == 3:
                    tmp[(i, j)] = True
    return tmp


def part_one(input: str, test_run=False):
    state, x, y = parse_input(input)
    for i in range(5 if test_run else 100):
        state = resolve(state, x, y)
    return Counter(state.values())[True]


def part_two(input: str, test_run=False):
    state, x, y = parse_input(input)
    state[(0, 0)] = True
    state[(x - 1, 0)] = True
    state[(0, y - 1)] = True
    state[(x - 1, y - 1)] = True

    for i in range(5 if test_run else 100):
        state = resolve(state, x, y)
        state[(0, 0)] = True
        state[(x - 1, 0)] = True
        state[(0, y - 1)] = True
        state[(x - 1, y - 1)] = True
    return Counter(state.values())[True]
