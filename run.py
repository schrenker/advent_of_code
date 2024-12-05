#!/usr/bin/env python

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
        cookies={"session": os.environ["AOC_TOKEN"]},
    )

    with open(path, "w") as input_file:
        input_file.write(resp.text)

    return resp.text


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help="Advent of Code edition [2015-20XX]")
    parser.add_argument("day", help="Day within an edition [(0)1-25]")
    parser.add_argument("part", help="Part of the day [1, 01, 2, 02]")

    args = parser.parse_args()

    return run_challenge(args.year, args.day, args.part)


if __name__ == "__main__":
    print(main())
