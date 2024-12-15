test_results = {
    "part_one": {"1": 140, "2": 772, "3": 1930},
    "part_two": {"1": 80, "2": 436, "3": 236, "4": 368},
}

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_field_stats(pos, visited, field):
    perimeter = 4
    area = 1
    curr = field[pos[0]][pos[1]]
    visited.add(pos)
    for d in directions:
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if (
            0 <= next_pos[0] < len(field)
            and 0 <= next_pos[1] < len(field[next_pos[0]])
            and field[next_pos[0]][next_pos[1]] == curr
        ):
            perimeter -= 1
            if next_pos not in visited:
                res = get_field_stats(next_pos, visited, field)
                area += res[0]
                perimeter += res[1]
    return area, perimeter


def get_field_stats_with_perimeter_table(pos, visited, field, perimeter_table):
    perimeter = 4
    area = 1
    curr = field[pos[0]][pos[1]]
    visited.add(pos)
    for d in directions:
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if (
            0 <= next_pos[0] < len(field)
            and 0 <= next_pos[1] < len(field[next_pos[0]])
            and field[next_pos[0]][next_pos[1]] == curr
        ):
            perimeter -= 1
            if next_pos not in visited:
                res = get_field_stats_with_perimeter_table(
                    next_pos, visited, field, perimeter_table
                )
                area += res[0]

    if perimeter > 0:
        perimeter_table.add(pos)
    return area, perimeter_table


def part_one(input: str):
    visited = set()
    acc = 0
    field = [[y for y in x] for x in input.splitlines()]
    for i, _ in enumerate(field):
        for j, _ in enumerate(field[i]):
            if (i, j) in visited:
                continue
            area, perimeter = get_field_stats((i, j), visited, field)
            acc += area * perimeter
    return acc


def part_two(input: str):
    visited = set()
    acc = 0
    field = [[y for y in x] for x in input.splitlines()]
    for i, _ in enumerate(field):
        for j, _ in enumerate(field[i]):
            perimeter_table = set()
            if (i, j) in visited:
                continue
            area, perimeter_table = get_field_stats_with_perimeter_table(
                (i, j), visited, field, perimeter_table
            )
            print(area, field[i][j], perimeter_table)
            return acc
    return acc
