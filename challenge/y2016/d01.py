test_results = {
    "part_one": {1: 5, 2: 2, 3: 12},
    "part_two": {1: 4},
}

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part_one(input: str, test_run=False):
    x, y = 0, 0
    curr = 0
    for i in input.split():
        blocks = int(i[1:].rstrip(","))
        if i[0] == "R":
            curr = (curr + 1) % 4
        else:
            curr = (curr - 1) % 4
        x += blocks * directions[curr][0]
        y += blocks * directions[curr][1]
    return abs(x) + abs(y)


def part_two(input: str, test_run=False):
    x, y = 0, 0
    curr = 0
    visited = set()
    for i in input.split():
        blocks = int(i[1:].rstrip(","))
        if i[0] == "R":
            curr = (curr + 1) % 4
        else:
            curr = (curr - 1) % 4
        for _ in range(1, blocks + 1):
            x += directions[curr][0]
            y += directions[curr][1]
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))
