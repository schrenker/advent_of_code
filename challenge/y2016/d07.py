import re

test_results = {"part_one": {1: 2}, "part_two": {1: 3}}


def check_abba(s):
    l = len(s)
    if l < 4:
        return False
    for i in range(l - 3):
        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
            return True
    return False


def find_aba(aba, s):
    l = len(s)
    for i in range(l - 2):
        if s[i] != s[i + 1] and s[i] == s[i + 2]:
            aba.add(s[i : i + 3])


def check_bab(aba, s):
    for i in aba:
        tmp = f"{i[1]}{i[0]}{i[1]}"
        if tmp in s:
            return True
    return False


def part_one(input: str, test_run=False):
    acc = 0
    for i in input.splitlines():
        tmp = re.split(r"\[|\]", i)
        valid = False
        for i in range(len(tmp)):
            if i % 2 == 0:
                if check_abba(tmp[i]):
                    valid = True
            else:
                if check_abba(tmp[i]):
                    valid = False
                    break
        acc += 1 if valid else 0
    return acc


def part_two(input: str, test_run=False):
    acc = 0
    for i in input.splitlines():
        tmp = re.split(r"\[|\]", i)
        aba = set()
        for i in range(0, len(tmp), 2):
            find_aba(aba, tmp[i])
        for i in range(1, len(tmp), 2):
            if check_bab(aba, tmp[i]):
                acc += 1
                break
    return acc
