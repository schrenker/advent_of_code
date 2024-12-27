from collections import defaultdict


test_results = {"part_one": {"1": 55312}, "part_two": {"1": 65601038650482}}


def blink(stones):
    tmp = defaultdict(int)
    for s in stones:
        if s == "0":
            tmp["1"] += stones[s]
        elif len(s) % 2 == 0:
            tmp[s[: len(s) // 2]] += stones[s]
            right = s[len(s) // 2 :].lstrip("0")
            if len(right) == 0:
                tmp["0"] += stones[s]
            else:
                tmp[right] += stones[s]
        else:
            tmp[str(int(s) * 2024)] += stones[s]
    return tmp


def part_one(input: str, test_run=False):
    stones = defaultdict(int)
    for i in input.rstrip().split():
        stones[i] += 1

    for i in range(25):
        stones = blink(stones)
    return sum(stones.values())


def part_two(input: str, test_run=False):
    stones = defaultdict(int)
    for i in input.rstrip().split():
        stones[i] += 1

    for i in range(75):
        stones = blink(stones)
    return sum(stones.values())
