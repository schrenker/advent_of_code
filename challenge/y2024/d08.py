test_results = {"part_one": {"1": 14}, "part_two": {"1": 34, "2": 9}}


def parse_input(input):
    tmp_input = input.splitlines()
    height = len(tmp_input)
    length = len(tmp_input[0])
    antennas = dict()
    for i in range(height):
        for j in range(length):
            if tmp_input[i][j] != ".":
                if tmp_input[i][j] in antennas:
                    antennas[tmp_input[i][j]].append((i, j))
                else:
                    antennas[tmp_input[i][j]] = [(i, j)]
    return antennas, height, length


def part_one(input):
    antennas, height, length = parse_input(input)
    happened = set()

    for a in antennas.values():
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                diff = (
                    a[i][0] - a[j][0],
                    a[i][1] - a[j][1],
                )
                if (
                    (a[i][0] + diff[0], a[i][1] + diff[1]) not in happened
                    and 0 <= a[i][0] + diff[0] < height
                    and 0 <= a[i][1] + diff[1] < length
                ):
                    happened.add((a[i][0] + diff[0], a[i][1] + diff[1]))
                if (
                    (a[j][0] - diff[0], a[j][1] - diff[1]) not in happened
                    and 0 <= a[j][0] - diff[0] < height
                    and 0 <= a[j][1] - diff[1] < length
                ):
                    happened.add((a[j][0] - diff[0], a[j][1] - diff[1]))

    return len(happened)


def part_two(input):
    antennas, height, length = parse_input(input)
    happened = set()

    for a in antennas.values():
        happened.update([i for i in a])

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                diff = (
                    (a[i][0] - a[j][0]),
                    (a[i][1] - a[j][1]),
                )
                x = a[i][0]
                y = a[i][1]
                while True:
                    if 0 <= x + diff[0] < height and 0 <= y + diff[1] < length:
                        if (x + diff[0], y + diff[1] not in happened):
                            happened.add((x + diff[0], y + diff[1]))
                        x += diff[0]
                        y += diff[1]
                    else:
                        break

                x = a[j][0]
                y = a[j][1]

                while True:
                    if 0 <= x - diff[0] < height and 0 <= y - diff[1] < length:
                        if (x - diff[0], y - diff[1]) not in happened:
                            happened.add((x - diff[0], y - diff[1]))
                        x -= diff[0]
                        y -= diff[1]
                    else:
                        break

    return len(happened)
