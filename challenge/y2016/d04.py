from typing import Counter


test_results = {"part_one": {1: 1514}, "part_two": {1: 343}}


def shift_cipher(s, n):
    tmp = list(s)
    shift = n % 26
    for i in range(len(tmp)):
        if tmp[i] == "-":
            tmp[i] = " "
        else:
            if ord(tmp[i]) + shift > 122:
                tmp[i] = chr(97 + ord(tmp[i]) + shift - 122 - 1)
            else:
                tmp[i] = chr(ord(tmp[i]) + shift)
    return "".join(tmp)


def part_one(input: str, test_run=False):
    acc = 0
    for i in input.splitlines():
        spl = i.split("-")
        tmp = spl[-1].split("[")
        id = int(tmp[0])
        checksum = tmp[1].rstrip("]")
        if (
            "".join(x[0] for x in Counter(sorted("".join(spl[:-1]))).most_common())[0:5]
            == checksum
        ):
            acc += id
    return acc


def part_two(input: str, test_run=False):
    target = "very encrypted name" if test_run else "northpole object storage"
    for i in input.splitlines():
        spl = i.split("-")
        tmp = spl[-1].split("[")
        id = int(tmp[0])
        checksum = tmp[1].rstrip("]")
        if (
            "".join(x[0] for x in Counter(sorted("".join(spl[:-1]))).most_common())[0:5]
            == checksum
        ):
            if target == shift_cipher("-".join(spl[:-1]), id):
                return id
