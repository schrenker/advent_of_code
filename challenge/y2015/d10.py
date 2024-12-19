test_results = {"part_one": {1: 82350}, "part_two": {1: 1166642}}


def look_and_say(input):
    result = ""
    curr = input[0]
    am = 1
    for i in range(1, len(input)):
        if input[i] != curr:
            result += str(am) + curr
            am = 1
            curr = input[i]
        else:
            am += 1
    return result + str(am) + curr


def part_one(input: str):
    result = input.rstrip()
    for i in range(40):
        result = look_and_say(result)
    return len(result)


def part_two(input: str):
    result = input.rstrip()
    for i in range(50):
        result = look_and_say(result)
    return len(result)
