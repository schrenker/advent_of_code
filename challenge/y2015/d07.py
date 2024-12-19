import time

test_results = {"part_one": {1: 65079}, "part_two": {1: 65079}}


def run_circuit(commands, circuit):
    while len(commands) > 0:
        for i, c in enumerate(commands):
            cmd = c.split(" -> ")
            try:
                circuit[cmd[1]] = int(cmd[0]) & 0xFFFF
                commands.pop(i)
            except ValueError:
                operation = cmd[0].split(" ")
                match len(operation):
                    case 1:
                        if cmd[0] in circuit:
                            circuit[cmd[1]] = circuit[cmd[0]] & 0xFFFF
                            commands.pop(i)

                    case 2:
                        if operation[1].isdigit():
                            circuit[cmd[1]] = ~int(operation[1]) & 0xFFFF
                            commands.pop(i)
                        else:
                            if operation[1] in circuit:
                                circuit[cmd[1]] = ~circuit[operation[1]] & 0xFFFF
                                commands.pop(i)

                    case _:
                        if operation[0].isdigit():
                            left = int(operation[0])
                        elif operation[0] in circuit:
                            left = circuit[operation[0]]
                        else:
                            continue

                        if operation[2].isdigit():
                            right = int(operation[2])
                        elif operation[2] in circuit:
                            right = circuit[operation[2]]
                        else:
                            continue

                        match operation[1]:
                            case "AND":
                                circuit[cmd[1]] = left & right & 0xFFFF
                                commands.pop(i)
                            case "OR":
                                circuit[cmd[1]] = left | right & 0xFFFF
                                commands.pop(i)
                            case "LSHIFT":
                                circuit[cmd[1]] = left << right & 0xFFFF
                                commands.pop(i)
                            case "RSHIFT":
                                circuit[cmd[1]] = left >> right & 0xFFFF
                                commands.pop(i)
    return circuit


def part_one(input: str):
    circuit = dict()
    commands = input.splitlines()
    return run_circuit(commands, circuit)["a"]


def part_two(input: str):
    circuit, second_circuit = dict(), dict()
    commands = input.splitlines()
    second_circuit["b"] = run_circuit(commands, circuit)["a"]
    commands = input.splitlines()
    return run_circuit(commands, second_circuit)["a"]
