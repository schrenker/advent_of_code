test_results = {"part_one": {"1": 143}, "part_two": {"1": 123}}


def parse_input(input):
    spl = input.splitlines()
    cutoff = spl.index("")
    rules = spl[:cutoff]
    updates = [[x for x in sub.split(",")] for sub in spl[cutoff + 1 :]]
    return rules, updates


def generate_precedence_dict(rules):
    precedence = {}
    for r in rules:
        tmp = r.split("|")
        if tmp[1] not in precedence:
            precedence[tmp[1]] = [tmp[0]]
        else:
            precedence[tmp[1]].append(tmp[0])
    return precedence


def validate_update(update, precedence):
    appeared = []
    for u in update:
        for a in appeared:
            if a in precedence and u in precedence[a]:
                return False
        appeared.append(u)
    return True


def fix_update(update, precedence):
    for i in range(len(update)):
        for j in range(len(update) - 1 - i):
            if update[j] in precedence and update[j + 1] in precedence[update[j]]:
                update[j], update[j + 1] = update[j + 1], update[j]
    return update


def part_one(input: str, test_run=False):
    acc = 0
    rules, updates = parse_input(input)
    precedence = generate_precedence_dict(rules)
    for u in updates:
        if validate_update(u, precedence):
            acc += int(u[(len(u) - 1) // 2])
    return acc


def part_two(input: str, test_run=False):
    acc = 0
    rules, updates = parse_input(input)
    precedence = generate_precedence_dict(rules)
    for u in updates:
        if not validate_update(u, precedence):
            acc += int(fix_update(u, precedence)[(len(u) - 1) // 2])
    return acc
