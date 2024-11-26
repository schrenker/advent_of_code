from importlib import import_module
import argparse
import requests
import os


def fetch_input(year, day):
    dir = f"./input/y{year}"
    path = f"{dir}/{day}"

    if os.path.isfile(path):
        with open(path, "r") as input_file:
            return input_file.read()

    if not os.path.exists(dir):
        os.makedirs(dir)

    # AoC website expects day in format 1-25
    day = day[1] if len(day) == 2 and day[0] == "0" else day
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": os.getenv("AOC_TOKEN")},
    )

    with open(path, "w") as input_file:
        input_file.write(resp.text)

    return resp.text


def generate_challenge(year, day):
    pass


def test_challenge(year, day, part):
    pass


def run_challenge(year, day, part):
    # make sure day is in format 01-25 for consistency and sorting
    day = f"0{day}" if len(day) == 1 else day
    input = fetch_input(year, day)
    challenge = import_module(f"challenge.y{year}.d{day}")
    if part in ["01", "1"]:
        return challenge.part_one(input)
    elif part in ["02", "2"]:
        return challenge.part_two(input)
    else:
        raise ValueError(f"part must be one of: [01 1 02 2], got: {part}")


def bench_challenge(year, day, part):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        help="What action should be performed? [gen, run, test, bench]",
        nargs="*",
    )
    args = parser.parse_args()

    arg_map = {
        "run": [3, "year, day, part"],
        "test": [3, "year, day, part"],
        "bench": [3, "year, day, part"],
        "gen": [2, "year, day"],
    }

    if args.action[0] not in arg_map:
        parser.error(f"No action defined for {args.action[0]}")

    if len(args.action) != arg_map[args.action[0]][0] + 1:
        parser.error(
            f"Wrong argument count for action '{args.action[0]}', expected {arg_map[args.action[0]][0]} [{arg_map[args.action[0]][1]}], got {len(args.action) - 1}"
        )

    match args.action[0]:
        case "run":
            run_challenge(args.action[1], args.action[2], args.action[3])
        case "test":
            test_challenge(args.action[1], args.action[2], args.action[3])
        case "bench":
            bench_challenge(args.action[1], args.action[2], args.action[3])
        case "gen":
            generate_challenge(args.action[1], args.action[2])


if __name__ == "__main__":
    main()
