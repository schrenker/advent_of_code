# No meaningful tests provided by AoC
test_results = {"part_one": {1: 0}, "part_two": {1: 0}}


def part_one(input: str, test_run=False):
    acc = 0
    for i in input.splitlines():
        tmp = [int(x) for x in i.split()]
        if (
            tmp[0] + tmp[1] > tmp[2]
            and tmp[0] + tmp[2] > tmp[1]
            and tmp[1] + tmp[2] > tmp[0]
        ):
            acc += 1
    return acc


def part_two(input: str, test_run=False):
    acc = 0
    i = 0
    spl = input.splitlines()
    while i < len(spl):
        p0 = [int(x) for x in spl[i].split()]
        p1 = [int(x) for x in spl[i + 1].split()]
        p2 = [int(x) for x in spl[i + 2].split()]
        for r in range(0, 3):
            if (
                p0[r] + p1[r] > p2[r]
                and p0[r] + p2[r] > p1[r]
                and p1[r] + p2[r] > p0[r]
            ):
                acc += 1
        i += 3
    return acc
