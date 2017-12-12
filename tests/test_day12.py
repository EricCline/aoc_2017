import unittest

from aoc.days.day12 import can_talk_to, parse_input


class TestDay12(unittest.TestCase):

    def test_can_talk_to_returns_right_stuff(self):
        pipes = {
            '0': ['2'],
            '1': ['1'],
            '2': ['0', '3', '4'],
            '3': ['2', '4'],
            '4': ['2', '3', '6'],
            '5': ['6'],
            '6': ['4', '5']
        }
        self.assertEqual(set(['0', '2', '3', '4', '5', '6']), can_talk_to('0', pipes))

