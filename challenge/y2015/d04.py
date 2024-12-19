from hashlib import md5

test_results = {
    "part_one": {1: 609043, 2: 1048970},
    "part_two": {1: 6742839, 2: 5714438},
}


def find_leading_zeroes_md5(key, zeroes):
    i = 0
    while True:
        if md5((key + str(i)).encode()).hexdigest().startswith("0" * zeroes):
            return i
        i += 1


def part_one(input: str):
    return find_leading_zeroes_md5(input.rstrip(), 5)


def part_two(input: str):
    return find_leading_zeroes_md5(input.rstrip(), 6)
