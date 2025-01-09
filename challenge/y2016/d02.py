test_results = {"part_one": {1: "1985"}, "part_two": {1: "5DB3"}}

directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def part_one(input: str, test_run=False):
    keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    x, y = 1, 1
    result = ""
    for line in input.splitlines():
        for s in line:
            if (0 <= x + directions[s][0] < len(keypad)) and (
                0 <= y + directions[s][1] < len(keypad[0])
            ):
                x += directions[s][0]
                y += directions[s][1]
        result += keypad[x][y]
    return result


def part_two(input: str, test_run=False):
    keypad = [
        [" ", " ", "1", " ", " "],
        [" ", "2", "3", "4", " "],
        ["5", "6", "7", "8", "9"],
        [" ", "A", "B", "C", " "],
        [" ", " ", "D", " ", " "],
    ]
    x, y = 2, 0
    result = ""
    for line in input.splitlines():
        for s in line:
            if (
                0 <= x + directions[s][0] < len(keypad)
                and 0 <= y + directions[s][1] < len(keypad[0])
                and keypad[x + directions[s][0]][y + directions[s][1]] != " "
            ):
                x += directions[s][0]
                y += directions[s][1]
        result += keypad[x][y]
    return result
