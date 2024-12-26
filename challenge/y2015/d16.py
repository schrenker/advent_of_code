# No testdata provided for this challenge by AoC
test_results = {"part_one": {1: 0}, "part_two": {1: 0}}


def parse_aunt(s):
    aunt = 0
    attributes = dict()
    tmp = s.split(" ")
    aunt = int(tmp[1].rstrip(":"))
    i = 2
    while i < len(tmp):
        attributes[tmp[i].rstrip(":")] = int(tmp[i + 1].rstrip(","))
        i += 2
    return aunt, attributes


def part_one(input: str):
    target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    aunt = 0
    for i in input.splitlines():
        aunt, attributes = parse_aunt(i)
        valid = True
        for k in target:
            if k in attributes:
                if target[k] != attributes[k]:
                    valid = False
                    break
        if valid:
            return aunt


def part_two(input: str):
    target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    aunt = 0
    for i in input.splitlines():
        aunt, attributes = parse_aunt(i)
        valid = True
        for k in target:
            if k in attributes:
                if k == "cats" or k == "trees":
                    if target[k] >= attributes[k]:
                        valid = False
                        break
                elif k == "pomeranians" or k == "goldfish":
                    if target[k] <= attributes[k]:
                        valid = False
                        break
                elif target[k] != attributes[k]:
                    valid = False
                    break
        if valid:
            return aunt
