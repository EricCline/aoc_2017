import unittest
from io import StringIO

from aoc.days.day2 import MaxMinSheet, EvenDivisorsSheet


class TestSpreadsheet(unittest.TestCase):

    def test_max_min_sheet(self):
        data = StringIO("5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8")
        self.assertEqual(18, MaxMinSheet(data).checksum)

    def test_even_divisors_sheet(self):
        data = StringIO(
            "5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5"
        )
        self.assertEqual(9, EvenDivisorsSheet(data).checksum)
