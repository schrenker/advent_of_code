from collections import Counter


test_results = {"part_one": {1: "easter"}, "part_two": {1: "advent"}}


def part_one(input: str, test_run=False):
    spl = input.splitlines()
    result = ""
    for i in range(len(spl[0])):
        occur = Counter()
        for j in range(len(spl)):
            occur.update(spl[j][i])
        result += occur.most_common()[0][0]
    return result


def part_two(input: str, test_run=False):
    spl = input.splitlines()
    result = ""
    for i in range(len(spl[0])):
        occur = Counter()
        for j in range(len(spl)):
            occur.update(spl[j][i])
        result += occur.most_common()[-1][0]
    return result
