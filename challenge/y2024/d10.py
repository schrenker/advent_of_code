test_results = {"part_one": {"1": 1, "2": 36}, "part_two": {"1": 81}}

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def find_starts(input):
    result = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                result.append((i, j))
    return result


def next_step(find, pos, area, counted):
    if find == 10:
        if pos not in counted:
            counted.add(pos)
            return 1
        else:
            return 0
    else:
        acc = 0
        for d in directions:
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if 0 <= next_pos[0] < len(area) and 0 <= next_pos[1] < len(area[0]):
                if area[next_pos[0]][next_pos[1]] == find:
                    acc += next_step(find + 1, next_pos, area, counted)
        return acc


def next_step_rating(find, pos, area):
    if find == 10:
        return 1
    else:
        acc = 0
        for d in directions:
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if 0 <= next_pos[0] < len(area) and 0 <= next_pos[1] < len(area[0]):
                if area[next_pos[0]][next_pos[1]] == find:
                    acc += next_step_rating(find + 1, next_pos, area)
        return acc


def part_one(input: str):
    area = [[int(x) for x in i] for i in input.splitlines()]
    starts = find_starts(area)
    acc = 0
    for i in starts:
        counted = set()
        acc += next_step(1, i, area, counted)
    return acc


def part_two(input: str):
    area = [[int(x) for x in i] for i in input.splitlines()]
    starts = find_starts(area)
    acc = 0
    for i in starts:
        acc += next_step_rating(1, i, area)
    return acc
