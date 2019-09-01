"""Unit tests for testme.py"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_empty(self):
        self.assertEqual(max_run([]), [])

    def test_max_run_same(self):
        self.assertEqual(max_run([1, 1, 1, 1]), [1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()

