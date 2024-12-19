test_results = {
    "part_one": {"1": "abcdffaa", "2": "ghjaabcc"},
    "part_two": {"1": "abcdffbb", "2": "ghjbbcdd"},
}


def check_forbidden(password):
    if "i" in password or "o" in password or "l" in password:
        return False
    return True


def check_increasing(password):
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
            return True
    return False


def check_overlapping(password):
    count = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            i += 1
            count += 1
        if count >= 2:
            return True
        i += 1
    return True if count >= 2 else False


def increment_password(password):
    for i in range(len(password) - 1, -1, -1):
        if password[i] == "z":
            password[i] = "a"
            continue
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return password


def part_one(input: str):
    password = list(input.rstrip())
    while True:
        if (
            check_forbidden(password)
            and check_increasing(password)
            and check_overlapping(password)
        ):
            return "".join(password)
        password = increment_password(password)


def part_two(input: str):
    return part_one("".join(increment_password(list(part_one(input)))))
