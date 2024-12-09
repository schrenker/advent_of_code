test_results = {"part_one": {"1": 1928}, "part_two": {"1": 2858}}


def parse_input(input):
    result = []
    tmp = 0
    for i in range(len(input)):
        if i % 2 == 0:
            result.extend([tmp] * int(input[i]))
            tmp += 1
        else:
            result.extend(["."] * int(input[i]))
    return result


def get_ranges(input):
    i = len(input) - 2
    amt = 1
    currnum = input[i + 1]
    result = []
    start = len(input) - 1
    while i >= 0:
        if input[i] == ".":
            result.append((currnum, start, amt))
            for j in range(i, -1, -1):
                if input[j] == ".":
                    i -= 1
                else:
                    break
            start = i
            currnum = input[i]
            amt = 0
            continue
        if input[i] == currnum:
            amt += 1
        else:
            result.append((currnum, start, amt))
            currnum = input[i]
            amt = 1
            start = i
        i -= 1

    result.append((currnum, start, amt))
    return result


def find_free_space(input, length):
    i = 0
    while i < len(input):
        tmp = length
        if input[i] == ".":
            for j in range(i, len(input)):
                if input[j] == ".":
                    tmp -= 1
                else:
                    break
            if tmp <= 0:
                return i
        i += 1
    return 0


def calculate_checksum(inp):
    acc = 0
    for i in range(len(inp)):
        if inp[i] == ".":
            continue
        else:
            acc += inp[i] * i
    return acc


def part_one(input):
    tmp = parse_input(input.rstrip())
    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i] != ".":
            for j in range(len(tmp)):
                if i == j:
                    return calculate_checksum(tmp)
                else:
                    if tmp[j] == ".":
                        tmp[i], tmp[j] = tmp[j], tmp[i]
                        break


def part_two(input):
    tmp = parse_input(input.rstrip())
    ranges = get_ranges(tmp)

    for r in ranges:
        start = find_free_space(tmp, r[2])
        if start > 0 and start < r[1]:
            for i in range(r[2]):
                tmp[start + i], tmp[r[1] - i] = tmp[r[1] - i], tmp[start + i]
    return calculate_checksum(tmp)
