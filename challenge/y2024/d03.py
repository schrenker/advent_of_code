import re
import itertools

test_results = {"part_one": {"1": 161}, "part_two": {"1": 48}}


def merge_instructions(*iterators):
    empty = {}
    for values in itertools.zip_longest(*iterators, fillvalue=empty):
        for value in values:
            if value is not empty:
                yield value


def part_one(input: str, test_run=False):
    acc = 0
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
    for i in instructions:
        tmp = i.lstrip("mul(").rstrip(")").split(",")
        acc += int(tmp[0]) * int(tmp[1])

    return acc


def part_two(input: str, test_run=False):
    muls = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", input)
    dos = re.finditer(r"do\(\)", input)
    donts = re.finditer(r"don't\(\)", input)
    tmp = []
    for t in merge_instructions(muls, dos, donts):
        tmp.append((t.start(), t.group()))

    acc = 0
    enabled = True
    for instruction in sorted(tmp, key=lambda tup: tup[0]):
        if instruction[1].startswith("do("):
            enabled = True
        elif instruction[1].startswith("don't("):
            enabled = False
        elif enabled:
            stripped_instruction = instruction[1].lstrip("mul(").rstrip(")").split(",")
            acc += int(stripped_instruction[0]) * int(stripped_instruction[1])

    return acc
