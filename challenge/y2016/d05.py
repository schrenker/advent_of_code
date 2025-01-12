from hashlib import md5

test_results = {"part_one": {1: "18f47a30"}, "part_two": {1: "05ace8e3"}}


def part_one(input: str, test_run=False):
    result = ""
    i = 0
    key = input.rstrip("\n")
    while len(result) < 8:
        h = md5((key + str(i)).encode()).hexdigest()
        if h.startswith("0" * 5):
            result += h[5]
        i += 1
    return result


def part_two(input: str, test_run=False):
    result = list("--------")
    i = 0
    key = input.rstrip("\n")
    while "-" in result:
        h = md5((key + str(i)).encode()).hexdigest()
        if h.startswith("0" * 5):
            try:
                if 0 <= int(h[5]) <= 7 and result[int(h[5])] == "-":
                    result[int(h[5])] = h[6]
            except ValueError:
                pass
        i += 1
    return "".join(result)
