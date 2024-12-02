test_results = {"part_one": {"1": 2}, "part_two": {"1": 4}}


def check_safe(report):
    increasing = True if report[0] < report[1] else False

    for i in range(0, len(report) - 1):
        if ((report[i] < report[i + 1]) is not increasing) or (
            not 1 <= abs(report[i] - report[i + 1]) <= 3
        ):
            return False, i, i + 1
    return True, -1, -1


def check_safe_with_dampener(report):
    result, idx1, idx2 = check_safe(report)
    if result is True:
        return result
    else:
        return (
            check_safe(report[:0] + report[1:])[0]
            or check_safe(report[:idx1] + report[idx1 + 1 :])[0]
            or check_safe(report[:idx2] + report[idx2 + 1 :])[0]
        )


def part_one(input):
    acc = 0
    for i in input.splitlines():
        report = [int(x) for x in i.split()]
        if check_safe(report)[0]:
            acc += 1
    return acc


def part_two(input):
    acc = 0
    for i in input.splitlines():
        report = [int(x) for x in i.split()]
        if check_safe_with_dampener(report):
            acc += 1
    return acc
