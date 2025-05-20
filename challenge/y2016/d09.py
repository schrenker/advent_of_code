test_results = {
    "part_one": {
        1: 6,
        2: 7,
        3: 9,
        4: 11,
        5: 6,
        6: 18,
    },
    "part_two": {
        1: 9,
        2: 20,
        3: 241920,
        4: 445,
    },
}


def part_one(input: str, test_run=False):
    data = input.rstrip("\n")
    pos = 0
    final_length = 0
    while pos < len(data):
        if data[pos] != "(":
            final_length += 1
        else:
            i = pos
            while data[i] != ")":
                i += 1
            chars, rep = [int(x) for x in data[pos + 1 : i].split("x")]
            pos = i + 1
            for _ in range(rep):
                final_length += len(data[pos : pos + chars])
            pos += chars
            continue
        pos += 1
    return final_length


def decompress(data):
    pos = 0
    final_length = 0
    while pos < len(data):
        if data[pos] != "(":
            final_length += 1
            pos += 1
        else:
            i = pos
            while data[i] != ")":
                i += 1
            chars, rep = [int(x) for x in data[pos + 1 : i].split("x")]
            final_length += decompress(data[i + 1 : chars + i + 1]) * rep
            pos = i + chars + 1
    return final_length


def part_two(input: str, test_run=False):
    return decompress(input.rstrip("\n"))
