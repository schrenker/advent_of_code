test_results = {"part_one": {1: 12}, "part_two": {1: 19}}


def count_characters(string):
    acc = 0
    i = 1
    while i < len(string) - 1:
        if string[i] == "\\":
            if string[i + 1] == "x":
                i += 3
            else:
                i += 1
        acc += 1
        i += 1
    return i + 1 - acc


def encode(string):
    acc = 0
    i = 0
    while i < len(string):
        if string[i] == "\\":
            if string[i + 1] == "x":
                acc += 4
                i += 3
            else:
                acc += 4
                i += 2
        elif string[i] == '"':
            acc += 2
            i += 1
        else:
            acc += 1
            i += 1
    return acc + 2 - i


def part_one(input: str):
    acc = 0
    for string in input.splitlines():
        acc += count_characters(string)
    return acc


def part_two(input: str):
    acc = 0
    for string in input.splitlines():
        acc += encode(string)
    return acc
