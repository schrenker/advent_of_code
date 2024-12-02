from importlib import import_module
from string import Template
import argparse
import requests
import unittest
import timeit
import types
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
        cookies={"session": os.environ["AOC_TOKEN"]},
    )

    with open(path, "w") as input_file:
        input_file.write(resp.text)

    return resp.text


def generate_challenge(year, day):
    day = f"0{day}" if len(day) == 1 else day

    dirs = [f"challenge/y{year}", "testdata"]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

    files = [
        f"challenge/y{year}/__init__.py",
        f"testdata/y{year}.{day}.1.1",
        f"testdata/y{year}.{day}.2.1",
    ]

    for f in files:
        if not os.path.exists(f):
            with open(f, "w"):
                pass

    with open("template/challenge") as f:
        tmp = f.read()

    with open(f"challenge/y{year}/d{day}.py", "w") as f:
        f.write(tmp)

    return 0


def test_challenge(year, day, part):
    day = f"0{day}" if len(day) == 1 else day
    challenge = import_module(f"challenge.y{year}.d{day}")

    class TestChallenge(unittest.TestCase):
        def test_part_one(self):
            for file in challenge.test_results["part_one"]:
                with open(f"testdata/y{year}.{day}.1.{file}", "r") as f:
                    with self.subTest(f"Testing file {file}"):
                        self.assertEqual(
                            challenge.part_one(f.read()),
                            challenge.test_results["part_one"][file],
                        )

        def test_part_two(self):
            for file in challenge.test_results["part_two"]:
                with open(f"testdata/y{year}.{day}.2.{file}", "r") as f:
                    with self.subTest(f"Testing file {file}"):
                        self.assertEqual(
                            challenge.part_two(f.read()),
                            challenge.test_results["part_two"][file],
                        )

    test_module = types.ModuleType("test_module")
    setattr(test_module, "TestChallenge", TestChallenge)

    if part in ["01", "1"]:
        suite = unittest.TestLoader().loadTestsFromName(
            "TestChallenge.test_part_one", test_module
        )
    elif part in ["02", "2"]:
        suite = unittest.TestLoader().loadTestsFromName(
            "TestChallenge.test_part_two", test_module
        )
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestChallenge)

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


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
    number_of_tests = 100
    result = timeit.timeit(
        f'run_challenge("{year}", "{day}", "{part}")',
        "from __main__ import run_challenge",
        number=number_of_tests,
    )
    average_result = result / number_of_tests
    return f"Average time: {average_result:.5f} seconds"


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
            return run_challenge(args.action[1], args.action[2], args.action[3])
        case "test":
            return test_challenge(args.action[1], args.action[2], args.action[3])
        case "bench":
            return bench_challenge(args.action[1], args.action[2], args.action[3])
        case "gen":
            return generate_challenge(args.action[1], args.action[2])


if __name__ == "__main__":
    print(main())
