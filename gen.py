#!/usr/bin/env python

import argparse
import os


def generate_challenge(year, day):
    day = f"0{day}" if len(day) == 1 else day

    dirs = [f"challenge/y{year}", "testdata"]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

    files = [
        f"challenge/y{year}/__init__.py",
        f"testdata/y{year}_d{day}_p1_1",
        f"testdata/y{year}_d{day}_p2_1",
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help="Advent of Code edition [2015-20XX]")
    parser.add_argument("day", help="Day within an edition [(0)1-25]")
    args = parser.parse_args()

    return generate_challenge(args.year, args.day)


if __name__ == "__main__":
    print(main())
