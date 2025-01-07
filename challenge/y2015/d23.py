test_results = {"part_one": {1: 2}, "part_two": {1: 7}}


def run_computer(cmd_list, reg):
    i = 0
    while 0 <= i < len(cmd_list):
        cmd = cmd_list[i].split()
        match cmd[0]:
            case "inc":
                reg[cmd[1]] += 1
                i += 1
            case "tpl":
                reg[cmd[1]] *= 3
                i += 1
            case "hlf":
                reg[cmd[1]] //= 2
                i += 1
            case "jmp":
                i += int(cmd[1])
            case "jie":
                if reg[cmd[1].rstrip(",")] % 2 == 0:
                    i += int(cmd[2])
                else:
                    i += 1
            case "jio":
                if reg[cmd[1].rstrip(",")] == 1:
                    i += int(cmd[2])
                else:
                    i += 1
    return reg


def part_one(input: str, test_run=False):
    cmd_list = input.splitlines()
    reg = run_computer(cmd_list, {"a": 0, "b": 0})
    return reg["a"] if test_run else reg["b"]


def part_two(input: str, test_run=False):
    cmd_list = input.splitlines()
    reg = run_computer(cmd_list, {"a": 1, "b": 0})
    return reg["a"] if test_run else reg["b"]
