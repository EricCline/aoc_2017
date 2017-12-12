import unittest

from aoc.days.day12 import group, groups


class TestDay12(unittest.TestCase):

    def test_group(self):
        pipes = {
            '0': ['2'],
            '1': ['1'],
            '2': ['0', '3', '4'],
            '3': ['2', '4'],
            '4': ['2', '3', '6'],
            '5': ['6'],
            '6': ['4', '5']
        }
        self.assertEqual(set(['0', '2', '3', '4', '5', '6']), group('0', pipes))

    def test_group(self):
        pipes = {
            '0': ['2'],
            '1': ['1'],
            '2': ['0', '3', '4'],
            '3': ['2', '4'],
            '4': ['2', '3', '6'],
            '5': ['6'],
            '6': ['4', '5']
        }
        self.assertEqual([set(['0', '2', '3', '4', '5', '6']), set(['1'])], groups(pipes))
