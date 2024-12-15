test_results = {"part_one": {"1": 58, "2": 43}, "part_two": {"1": 34, "2": 14}}


def get_surface_area(dimensions):
    dimensions.sort()
    return (
        2 * dimensions[0] * dimensions[1]
        + 2 * dimensions[0] * dimensions[2]
        + 2 * dimensions[1] * dimensions[2]
        + dimensions[0] * dimensions[1]
    )


def get_ribbon_length(dimensions):
    dimensions.sort()
    return (
        2 * dimensions[0]
        + 2 * dimensions[1]
        + dimensions[0] * dimensions[1] * dimensions[2]
    )


def part_one(input: str):
    acc = 0
    for i in input.splitlines():
        acc += get_surface_area([int(x) for x in i.split("x")])
    return acc


def part_two(input: str):
    acc = 0
    for i in input.splitlines():
        acc += get_ribbon_length([int(x) for x in i.split("x")])
    return acc
