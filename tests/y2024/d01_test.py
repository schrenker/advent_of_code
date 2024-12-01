import unittest
import os
from challenge.y2024.d01 import part_one, part_two, test_results


class TestChallenge(unittest.TestCase):
    def test_part_one(self):
        for file in test_results["part_one"]:
            with open(f"tests/testdata/y2024.01.01.{file}", "r") as f:
                with self.subTest(f"Testing file {file}"):
                    self.assertEqual(part_one(f.read()), test_results["part_one"][file])

    def test_part_two(self):
        for file in test_results["part_two"]:
            with open(f"tests/testdata/y2024.01.02.{file}", "r") as f:
                with self.subTest(f"Testing file {file}"):
                    self.assertEqual(part_two(f.read()), test_results["part_two"][file])
