from collections import defaultdict, Counter


test_results = {"part_one": {1: 998996}, "part_two": {1: 2000001}}


def part_one(input: str, test_run=False):
    lights = defaultdict(bool)
    for i in input.splitlines():
        spl = i.split(" ")
        if i.startswith("toggle"):
            begin = [int(x) for x in spl[1].split(",")]
            end = [int(x) for x in spl[3].split(",")]
            for i in range(begin[0], end[0] + 1):
                for j in range(begin[1], end[1] + 1):
                    lights[(i, j)] = not lights[(i, j)]
        else:
            begin = [int(x) for x in spl[2].split(",")]
            end = [int(x) for x in spl[4].split(",")]
            method = spl[1]
            for i in range(begin[0], end[0] + 1):
                for j in range(begin[1], end[1] + 1):
                    lights[(i, j)] = True if method == "on" else False

    return Counter(lights.values())[True]


def part_two(input: str, test_run=False):
    lights = defaultdict(int)
    for i in input.splitlines():
        spl = i.split(" ")
        if i.startswith("toggle"):
            begin = [int(x) for x in spl[1].split(",")]
            end = [int(x) for x in spl[3].split(",")]
            for i in range(begin[0], end[0] + 1):
                for j in range(begin[1], end[1] + 1):
                    lights[(i, j)] += 2
        else:
            begin = [int(x) for x in spl[2].split(",")]
            end = [int(x) for x in spl[4].split(",")]
            method = spl[1]
            for i in range(begin[0], end[0] + 1):
                for j in range(begin[1], end[1] + 1):
                    if method == "on":
                        lights[(i, j)] += 1
                    else:
                        lights[(i, j)] = (
                            0 if lights[(i, j)] <= 0 else lights[(i, j)] - 1
                        )

    return sum(lights.values())
