test_results = {"part_one": {1: 2}, "part_two": {1: 2}}


def has_vowels(string):
    vowels = {"a", "e", "i", "o", "u"}
    acc = 0
    for i in string:
        if i in vowels:
            acc += 1
    return True if acc >= 3 else False


def has_duo_letter(string):
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            return True
    return False


def has_forbidden_strings(string):
    forbidden = {"ab", "cd", "pq", "xy"}
    for i in range(1, len(string)):
        if string[i - 1 : i + 1] in forbidden:
            return True
    return False


def is_nice(string):
    return (
        has_vowels(string)
        and has_duo_letter(string)
        and not has_forbidden_strings(string)
    )


def has_double_nonoverlapping(string):
    for i in range(1, len(string) - 2):
        for j in range(i + 1, len(string)):
            if string[i - 1 : i + 1] == string[j : j + 2]:
                return True
    return False


def has_letter_inbetween_pair(string):
    for i in range(1, len(string) - 1):
        if string[i - 1] == string[i + 1]:
            return True
    return False


def is_nice_better_model(string):
    return has_double_nonoverlapping(string) and has_letter_inbetween_pair(string)


def part_one(input: str, test_run=False):
    acc = 0
    for string in input.splitlines():
        if is_nice(string):
            acc += 1
    return acc


def part_two(input: str, test_run=False):
    acc = 0
    for string in input.splitlines():
        if is_nice_better_model(string):
            acc += 1
    return acc
