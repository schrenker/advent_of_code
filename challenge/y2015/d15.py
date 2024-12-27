from functools import reduce
from common.generators import addition_combinations

test_results = {"part_one": {1: 62842880}, "part_two": {1: 57600000}}


def parse_input(input):
    result = list()
    for i in input.splitlines():
        tmp = i.split(" ")
        result.append(
            {
                "capacity": int(tmp[2].rstrip(",")),
                "durability": int(tmp[4].rstrip(",")),
                "flavor": int(tmp[6].rstrip(",")),
                "texture": int(tmp[8].rstrip(",")),
                "calories": int(tmp[10]),
            }
        )
    return result


def part_one(input: str, test_run=False):
    ingredients = parse_input(input)
    score = 0
    for count in addition_combinations(100, 1, len(ingredients)):
        recipe = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0}
        for i in range(len(count)):
            for k in recipe.keys():
                recipe[k] += ingredients[i][k] * count[i]
        score = max(score, reduce(lambda x, y: max(0, x) * max(0, y), recipe.values()))
    return score


def part_two(input: str, test_run=False):
    ingredients = parse_input(input)
    score = 0
    for count in addition_combinations(100, 1, len(ingredients)):
        recipe = {
            "capacity": 0,
            "durability": 0,
            "flavor": 0,
            "texture": 0,
            "calories": 0,
        }
        for i in range(len(count)):
            for k in recipe.keys():
                recipe[k] += ingredients[i][k] * count[i]
        if recipe["calories"] == 500:
            recipe["calories"] = 1
            score = max(
                score, reduce(lambda x, y: max(0, x) * max(0, y), recipe.values())
            )
    return score
