test_results = {
    "part_one": {
        1: 6,
        2: 7,
        3: 9,
        4: 11,
        5: 6,
        6: 18,
    },
    "part_two": {1: 9, 2: 20, 3: 241920, 4: 445},
}


def part_one(input: str, test_run=False):
    i = 0
    data = input.rstrip("\n")
    decompress = ""
    while i < len(data):
        if data[i] != "(":
            decompress += data[i]
        else:
            chars = 0
            rep = 0
            j = i
            while data[j] != ")":
                j += 1
            chars, rep = [int(x) for x in data[i + 1 : j].split("x")]
            i = j + 1
            for _ in range(rep):
                decompress += data[i : i + chars]
            i += chars
            continue
        i += 1
    return len(decompress)


def part_two(input: str, test_run=False):
    return input
