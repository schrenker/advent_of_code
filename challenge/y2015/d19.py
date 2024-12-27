from collections import defaultdict
import re


test_results = {
    "part_one": {
        1: 4,
        2: 7,
    },
    "part_two": {
        1: 3,
        2: 6,
    },
}


def parse_input(input):
    spl = input.splitlines()
    replacements = defaultdict(list)
    for i in range(len(spl)):
        if len(spl[i]) == 0:
            return replacements, spl[i + 1]
        else:
            tmp = spl[i].split(" => ")
            replacements[tmp[0]].append(tmp[1])
    return replacements, ""


def simplifications(replacements):
    result = defaultdict(str)
    for r in replacements:
        for rr in replacements[r]:
            result[rr] = r
    return result


def part_one(input: str, test_run=False):
    replacements, molecule = parse_input(input)
    transformations = set()
    for r in replacements:
        for i in re.finditer(r, molecule):
            for rr in replacements[r]:
                transformations.add(molecule[: i.start(0)] + rr + molecule[i.end(0) :])
    return len(transformations)


def part_two(input: str, test_run=False):
    # replacements, molecule = parse_input(input)
    # simplified = simplifications(replacements)
    # steps = 0
    # print(simplified)
    # for i in sorted(simplified.keys(), reverse=True, key=len):
    #     if molecule == "e":
    #         return steps
    #     else:
    #         for r in re.finditer(i, molecule):
    #             tmp = molecule[: r.start(0)] + simplified[i] + molecule[r.end(0) :]
    #             if "e" in tmp and len(tmp) > 1:
    #                 continue
    #             molecule = tmp
    #             steps += 1
    return input
