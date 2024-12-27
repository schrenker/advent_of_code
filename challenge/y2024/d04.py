test_results = {"part_one": {"1": 18}, "part_two": {"1": 9}}

xmas_search_pattern = [
    [(-1, 0), (-2, 0), (-3, 0)],
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (0, 2), (0, 3)],
    [(0, -1), (0, -2), (0, -3)],
    [(-1, 1), (-2, 2), (-3, 3)],
    [(1, 1), (2, 2), (3, 3)],
    [(-1, -1), (-2, -2), (-3, -3)],
    [(1, -1), (2, -2), (3, -3)],
]

mas_search_pattern = [
    [(-1, -1), (1, 1)],
    [(1, -1), (-1, 1)],
    [(-1, 1), (1, -1)],
    [(1, 1), (-1, -1)],
]


def search_xmas(arr, pos):
    acc = 0
    for p in xmas_search_pattern:
        if (
            pos[0] + p[0][0] < 0
            or pos[1] + p[0][1] < 0
            or pos[0] + p[1][0] < 0
            or pos[1] + p[1][1] < 0
            or pos[0] + p[2][0] < 0
            or pos[1] + p[2][1] < 0
        ):
            continue
        try:
            if (
                arr[pos[0] + p[0][0]][pos[1] + p[0][1]] == "M"
                and arr[pos[0] + p[1][0]][pos[1] + p[1][1]] == "A"
                and arr[pos[0] + p[2][0]][pos[1] + p[2][1]] == "S"
            ):

                acc += 1
        except IndexError:
            continue
    return acc


def search_mas(arr, pos):
    acc = 0

    for p in mas_search_pattern:
        try:
            if (
                arr[pos[0] + p[0][0]][pos[1] + p[0][1]] == "M"
                and arr[pos[0] + p[1][0]][pos[1] + p[1][1]] == "S"
            ):
                acc += 1
        except IndexError:
            return 0

    if acc == 2:
        return 1
    else:
        return 0


def part_one(input: str, test_run=False):
    acc = 0
    arr = input.splitlines()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "X":
                acc += search_xmas(arr, (i, j))
    return acc


def part_two(input: str, test_run=False):
    acc = 0
    arr = input.splitlines()
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i - 1])):
            if arr[i][j] == "A":
                acc += search_mas(arr, (i, j))
    return acc
