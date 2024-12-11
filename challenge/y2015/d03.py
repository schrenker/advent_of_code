test_results = {
    "part_one": {"1": 2, "2": 4, "3": 2},
    "part_two": {"1": 3, "2": 3, "3": 11},
}

directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


def part_one(input):
    curr = (0, 0)
    visited = set()
    visited.add(curr)
    for i in input.rstrip():
        curr = (curr[0] + directions[i][0], curr[1] + directions[i][1])
        visited.add(curr)
    return len(visited)


def part_two(input):
    santa = (0, 0)
    robot = (0, 0)
    visited = set()
    visited.add(santa)
    for i, v in enumerate(input.rstrip()):
        if i % 2 == 0:
            santa = (santa[0] + directions[v][0], santa[1] + directions[v][1])
            visited.add(santa)
        else:
            robot = (robot[0] + directions[v][0], robot[1] + directions[v][1])
            visited.add(robot)

    return len(visited)
