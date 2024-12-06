#!/usr/bin/env python

import argparse
import timeit


def bench_challenge(year, day, part, runs):
    result = timeit.timeit(
        f'run_challenge("{year}", "{day}", "{part}")',
        "from run import run_challenge",
        number=runs,
    )
    average_result = result / runs
    return f"Part {part} average time: {average_result:.5f} seconds"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help="Advent of Code edition [2015-20XX]")
    parser.add_argument("day", help="Day within an edition [(0)1-25]")
    parser.add_argument("part", help="Part of the day [1, 01, 2, 02, both]")
    parser.add_argument(
        "--runs",
        "-r",
        nargs=1,
        type=int,
        default=100,
        help="How many runs should be done for the average",
    )
    args = parser.parse_args()

    results = ""
    if args.part in ["01", "1", "both"]:
        results += bench_challenge(args.year, args.day, "1", args.runs[0])
        if args.part == "both":
            results += "\n"
    if args.part in ["02", "2", "both"]:
        results += bench_challenge(args.year, args.day, "2", args.runs[0])

    return results


if __name__ == "__main__":
    print(main())
