import math


# Second test not provided by AoC
test_results = {"part_one": {1: 8}, "part_two": {1: 8}}


def get_divisors(n):
    result = list()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(n // i)
        i += 1
    return result


def part_one(input: str, test_run=False):
    goal = int(input)
    for i in range(1, goal):
        if sum(d * 10 for d in get_divisors(i)) >= goal:
            return i
    raise Exception("Unable to find house with at least that many presents delivered.")


def part_two(input: str, test_run=False):
    goal = int(input)
    for i in range(1, goal):
        if sum(d * 11 if i // d <= 50 else 0 for d in get_divisors(i)) >= goal:
            return i
    raise Exception("Unable to find house with at least that many presents delivered.")
