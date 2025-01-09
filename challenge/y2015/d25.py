test_results = {"part_one": {1: 21345942}, "part_two": {1: 0}}


def part_one(input: str, test_run=False):
    spl = input.split()
    goal = (int(spl[-3].rstrip(",")), int(spl[-1].rstrip(".")))
    column = (goal[1] * (goal[1] + 1)) // 2
    row = column
    for i in range(0, goal[0] - 1):
        row += goal[1] + i

    curr = 20151125
    for i in range(1, row):
        curr = (curr * 252533) % 33554393
    return curr


def part_two(input: str, test_run=False):
    return 0
