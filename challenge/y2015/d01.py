test_results = {
    "part_one": {
        1: 0,
        2: 0,
        3: 3,
        4: 3,
        5: 3,
        6: -1,
        7: -1,
        8: -3,
        9: -3,
    },
    "part_two": {"1": 1, "2": 5},
}


def part_one(input: str, test_run=False):
    floor = 0
    for i in input.rstrip():
        floor += 1 if i == "(" else -1
    return floor


def part_two(input: str, test_run=False):
    floor = 0
    for i, v in enumerate(input):
        floor += 1 if v == "(" else -1

        if floor == -1:
            return i + 1
    return None
