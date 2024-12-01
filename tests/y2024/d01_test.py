import unittest
import os
from challenge.y2024.d01 import part_one, part_two, test_results


class TestChallenge(unittest.TestCase):
    def test_part_one(self):
        dir = "./tests/testdata/y2024/01/01"
        files = os.listdir(dir)
        for file in files:
            with open(f"{dir}/{file}", "r") as f:
                with self.subTest(f"Testing file {file}"):
                    self.assertEqual(part_one(f.read()), test_results["part_one"][file])

    def test_part_two(self):
        dir = "./tests/testdata/y2024/01/02"
        files = os.listdir(dir)
        for file in files:
            with open(f"{dir}/{file}", "r") as f:
                with self.subTest(f"Testing file {file}"):
                    self.assertEqual(part_two(f.read()), test_results["part_two"][file])
