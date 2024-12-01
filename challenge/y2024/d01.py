test_results = {"part_one": {"1": 11}, "part_two": {"1": 31}}


def part_one(input):
    tmp = input.rstrip().split("\n")
    left = []
    right = []
    for i in tmp:
        spl = i.split()
        left.append(int(spl[0]))
        right.append(int(spl[1]))
    left.sort()
    right.sort()

    acc = 0
    for i, _ in enumerate(left):
        acc += abs(left[i] - right[i])

    return acc


def part_two(input):
    tmp = input.rstrip().split("\n")
    left = []
    right = []
    for i in tmp:
        spl = i.split()
        left.append(int(spl[0]))
        right.append(int(spl[1]))

    num_map = {}
    for v in right:
        if v in num_map:
            num_map[v] += 1
        else:
            num_map[v] = 1

    acc = 0

    for v in left:
        if v in num_map:
            acc += v * num_map[v]

    return acc
