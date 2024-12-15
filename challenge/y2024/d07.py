import itertools

test_results = {"part_one": {"1": 3749}, "part_two": {"1": 11387}}


def apply_operators(operands, operators):
    acc = operands[0]
    for i in range(1, len(operands)):
        match operators[i - 1]:
            case "+":
                acc += operands[i]
            case "*":
                acc *= operands[i]
            case "|":
                acc = int(f"{acc}{operands[i]}")
    return acc


def is_valid_calibration(input, operators):
    tmp = input.split(":")
    result = int(tmp[0])
    operands = [int(x) for x in tmp[1].split()]
    if result == sum(operands):
        return result

    for o in [p for p in itertools.product(operators, repeat=len(operands) - 1)]:
        if apply_operators(operands, o) == result:
            return result

    return 0


def part_one(input: str):
    acc = 0
    for i in input.splitlines():
        acc += is_valid_calibration(i, ["+", "*"])
    return acc


def part_two(input: str):
    acc = 0
    for i in input.splitlines():
        acc += is_valid_calibration(i, ["+", "*", "|"])
    return acc
