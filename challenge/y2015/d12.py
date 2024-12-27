import re
import json

test_results = {
    "part_one": {
        1: 6,
        2: 6,
        3: 3,
        4: 3,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    },
    "part_two": {1: 6, 2: 4, 3: 0, 4: 6},
}


def handle_dict(d):
    acc = 0
    if "red" in d.values():
        return 0
    for v in d.values():
        if type(v) is list:
            acc += handle_list(v)
        elif type(v) is dict:
            acc += handle_dict(v)
        elif type(v) is int or v.lstrip("+-").isdigit():
            acc += int(v)
    return acc


def handle_list(l):
    acc = 0
    for v in l:
        if type(v) is list:
            acc += handle_list(v)
        elif type(v) is dict:
            acc += handle_dict(v)
        elif type(v) is int or v.lstrip("+-").isdigit():
            acc += int(v)
    return acc


def part_one(input: str, test_run=False):
    acc = 0
    for i in re.findall(r"-?\d+", input):
        acc += int(i)
    return acc


def part_two(input: str, test_run=False):
    j = json.loads(input)
    return handle_dict(j) if type(j) is dict else handle_list(j)
