import unittest
import os
from challenge.y2015.d01 import part_one, part_two


class TestChallenge(unittest.TestCase):
    def test_part_one(self):
        dir = "./tests/testdata/y2015/01/01"
        files = os.listdir(dir)
        results = {
            "1": 4,
            "2": 4,
            "3": 3,
        }
        for file in files:
            with open(f"{dir}/{file}", "r") as f:
                with self.subTest(f"Testing file {file}"):
                    self.assertEqual(part_one(f.read()), results[file])

    def test_part_two(self):
        dir = "./tests/testdata/y2015/01/02"
        files = os.listdir(dir)
        results = {
            "1": 0,
        }
        for file in files:
            with open(f"{dir}/{file}", "r") as f:
                with self.subTest(f"Testing file {file}"):
                    self.assertEqual(part_two(f.read()), results[file])
