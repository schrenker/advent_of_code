from collections import defaultdict
import re


test_results = {
    "part_one": {
        1: 4,
        2: 7,
    },
    "part_two": {
        1: 3,
        2: 6,
    },
}


def parse_input(input):
    spl = input.splitlines()
    replacements = defaultdict(list)
    for i in range(len(spl)):
        if len(spl[i]) == 0:
            return replacements, spl[i + 1]
        else:
            tmp = spl[i].split(" => ")
            replacements[tmp[0]].append(tmp[1])
    return replacements, ""


def simplifications(replacements):
    result = defaultdict(str)
    for r in replacements:
        for rr in replacements[r]:
            result[rr] = r
    return result


def find_simplification(molecule, simplifications):
    for s in simplifications:
        for i in range(len(molecule) - len(s) + 1):
            if molecule[i : i + len(s)] == s:
                yield (molecule[:i] + simplifications[s] + molecule[i + len(s) :])


def a_star(start, end, simplifications):
    open_nodes = {start}
    prev_node = {start: None}
    costs = {start: 0}

    while open_nodes:
        current_node = min(open_nodes, key=lambda node: costs[node] + len(node))

        if current_node == end:
            return costs[end]

        for n in find_simplification(current_node, simplifications):
            tmp = costs[current_node] + 1
            if n not in costs or tmp < costs[n]:
                open_nodes.add(n)
                costs[n] = tmp
                prev_node[n] = current_node

        open_nodes.remove(current_node)

    raise Exception(f"Unable to find path from {start} to {end}")


def part_one(input: str, test_run=False):
    replacements, molecule = parse_input(input)
    transformations = set()
    for r in replacements:
        for i in re.finditer(r, molecule):
            for rr in replacements[r]:
                transformations.add(molecule[: i.start(0)] + rr + molecule[i.end(0) :])
    return len(transformations)


def part_two(input: str, test_run=False):
    replacements, molecule = parse_input(input)
    return a_star(molecule, "e", simplifications(replacements))
