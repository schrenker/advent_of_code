test_results = {"part_one": {"1": 41}, "part_two": {"1": 6}}


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find_guard(area):
    for i in range(len(area)):
        try:
            idx = area[i].index("^")
        except ValueError:
            continue
        return (i, idx)
    return (-1, -1)


def find_path(area):
    curr = find_guard(area)
    visited = {curr}
    rotation = 0

    while True:
        next_stop = (curr[0] + direction[rotation][0], curr[1] + direction[rotation][1])

        if (0 > next_stop[0] or next_stop[0] >= len(area)) or (
            0 > next_stop[1] or next_stop[1] >= len(area[next_stop[0]])
        ):
            return visited
        elif area[next_stop[0]][next_stop[1]] == "#":
            rotation = (rotation + 1) % len(direction)
            continue

        curr = next_stop
        visited.add(curr)


def find_loop(start, area, obstacle):
    curr = start
    rotation = 0
    visited = {(curr[0], curr[1], rotation)}
    while True:
        next_stop = (curr[0] + direction[rotation][0], curr[1] + direction[rotation][1])

        if (0 > next_stop[0] or next_stop[0] >= len(area)) or (
            0 > next_stop[1] or next_stop[1] >= len(area[next_stop[0]])
        ):
            return False
        elif next_stop == obstacle or area[next_stop[0]][next_stop[1]] == "#":
            rotation = (rotation + 1) % len(direction)
            continue

        curr = next_stop

        if (curr[0], curr[1], rotation) in visited:
            return True
        else:
            visited.add((curr[0], curr[1], rotation))


def part_one(input: str):
    area = input.splitlines()
    return len(find_path(area))


def part_two(input: str):
    area = input.splitlines()
    path = find_path(area)
    start = find_guard(area)
    acc = 0

    for k in path:
        if find_loop(start, area, k):
            acc += 1

    return acc
