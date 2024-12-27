#!/usr/bin/env python

from importlib import import_module
import argparse
import unittest
import types


def test_challenge(year, day, part):
    day = f"0{day}" if len(day) == 1 else day
    challenge = import_module(f"challenge.y{year}.d{day}")

    class TestChallenge(unittest.TestCase):
        def test_part_one(self):
            for file in challenge.test_results["part_one"]:
                with open(f"testdata/y{year}/d{day}_p1_{file}", "r") as f:
                    with self.subTest(f"Testing file {file}"):
                        self.assertEqual(
                            challenge.part_one(f.read(), test_run=True),
                            challenge.test_results["part_one"][file],
                        )

        def test_part_two(self):
            for file in challenge.test_results["part_two"]:
                with open(f"testdata/y{year}/d{day}_p2_{file}", "r") as f:
                    with self.subTest(f"Testing file {file}"):
                        self.assertEqual(
                            challenge.part_two(f.read(), test_run=True),
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help="Advent of Code edition [2015-20XX]")
    parser.add_argument("day", help="Day within an edition [(0)1-25]")
    parser.add_argument("part", help="Part of the day [1, 01, 2, 02, both]")
    args = parser.parse_args()

    return test_challenge(args.year, args.day, args.part)


if __name__ == "__main__":
    print(main())
