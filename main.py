from importlib import import_module
import argparse

def fetch_input(challenge):
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="What action should be performed? [run, test, bench]")
    parser.add_argument("year", help="Which year is the challenge from? [2015 - 2024]")
    parser.add_argument("day", help="Which day is the challenge from? [01 - 25]")
    parser.add_argument("part", help="Which part should be run? [1, 01, 2, 02]")
    args = parser.parse_args()

    match args.action:
        case "run":
            d = import_module(f"challenge.y{args.year}.d{args.day}")
            d.part_one("runrun")
        case "test":
            print("thest")
        case "bench":
            print("benchpress")

if __name__ == "__main__":
    main()
