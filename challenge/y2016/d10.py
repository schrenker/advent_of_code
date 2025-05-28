from collections import defaultdict


test_results = {"part_one": {1: 2}, "part_two": {1: 30}}


def part_one(input: str, test_run=False):
    low_goal = 2 if test_run else 17
    high_goal = 5 if test_run else 61
    lines = input.splitlines()
    state = defaultdict(list[int])
    while len(lines) > 0:
        for i in range(len(lines)):
            tmp = lines[i].split()
            if tmp[0] == "value":
                state[tmp[5]].append(int(tmp[1]))
                lines.pop(i)
                break

            elif len(state[tmp[1]]) != 2:
                continue

            else:
                state[tmp[1]].sort()
                if low_goal == state[tmp[1]][0] and high_goal == state[tmp[1]][1]:
                    return int(tmp[1])
                if tmp[5] == "bot":
                    state[tmp[6]].append(int(state[tmp[1]][0]))
                if tmp[10] == "bot":
                    state[tmp[11]].append(int(state[tmp[1]][1]))
                state[tmp[1]] = list()


def part_two(input: str, test_run=False):
    lines = input.splitlines()
    state = defaultdict(list[int])
    outputs = defaultdict(int)
    while len(lines) > 0:
        for i in range(len(lines)):
            tmp = lines[i].split()
            if tmp[0] == "value":
                state[tmp[5]].append(int(tmp[1]))
                lines.pop(i)
                break

            elif len(state[tmp[1]]) != 2:
                continue

            else:
                state[tmp[1]].sort()
                if tmp[5] == "bot":
                    state[tmp[6]].append(int(state[tmp[1]][0]))
                else:
                    outputs[tmp[6]] = int(state[tmp[1]][0])
                if tmp[10] == "bot":
                    state[tmp[11]].append(int(state[tmp[1]][1]))
                else:
                    outputs[tmp[11]] = int(state[tmp[1]][1])
                state[tmp[1]] = list()
        if "0" in outputs and "1" in outputs and "2" in outputs:
            return outputs["0"] * outputs["1"] * outputs["2"]
