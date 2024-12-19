from collections import defaultdict
import itertools


test_results = {"part_one": {1: 605}, "part_two": {1: 982}}


def prep_distances(input):
    distances = defaultdict(dict)
    for route in input.splitlines():
        tmp = route.split(" = ")
        towns = tmp[0].split(" to ")
        distances[towns[0]][towns[1]] = int(tmp[1])
        distances[towns[1]][towns[0]] = int(tmp[1])
    return distances


def part_one(input: str):
    distances = prep_distances(input)
    result = float("inf")
    for p in itertools.permutations(distances.keys()):
        acc = 0
        for i in range(0, len(p) - 1):
            acc += distances[p[i]][p[i + 1]]
            if acc > result:
                break
        result = min(result, acc)
    return result


def part_two(input: str):
    distances = prep_distances(input)
    result = 0
    for p in itertools.permutations(distances.keys()):
        acc = 0
        for i in range(0, len(p) - 1):
            acc += distances[p[i]][p[i + 1]]
        result = max(result, acc)
    return result
