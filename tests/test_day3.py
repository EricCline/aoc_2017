import unittest

from aoc.days.day3.part1 import (
    Point,
    block_before_step,
    manhattan_distance,
    point_from_block,
    point_from_step,
    point_from_tile,
    steps_through_block,
    transforms_for_block,
)

from aoc.days.day3.part2 import SpiralGrid


class TestManhattanDistance(unittest.TestCase):

    def test_returns_sum_of_differences(self):
        p1 = Point(0, 0)
        p2 = Point(1, 1)
        result = manhattan_distance(p1, p2)
        self.assertEqual(2, result)

    def test_returns_sum_of_absolute_differences(self):
        p1 = Point(0, 0)
        p2 = Point(-1, -1)
        result = manhattan_distance(p1, p2)
        self.assertEqual(2, result)

    def test_works_for_asymmetric_nums(self):
        p1 = Point(14, 13)
        p2 = Point(-1, -1)
        result = manhattan_distance(p1, p2)
        self.assertEqual(29, result)


class TestPointsAndBlocks(unittest.TestCase):

    def test_steps_through_block(self):
        self.assertEqual(0, steps_through_block(0))
        self.assertEqual(2, steps_through_block(1))
        self.assertEqual(6, steps_through_block(2))
        self.assertEqual(12, steps_through_block(3))
        self.assertEqual(20, steps_through_block(4))

    def test_block_before_step(self):
        self.assertEqual(0, block_before_step(0))
        self.assertEqual(0, block_before_step(1))
        self.assertEqual(1, block_before_step(2))
        self.assertEqual(1, block_before_step(3))
        self.assertEqual(1, block_before_step(4))
        self.assertEqual(1, block_before_step(5))
        self.assertEqual(2, block_before_step(6))
        self.assertEqual(2, block_before_step(7))

    def test_point_from_block(self):
        self.assertEqual(Point(0, 0), point_from_step(0))
        self.assertEqual(Point(1, 0), point_from_step(1))
        self.assertEqual(Point(1, 1), point_from_step(2))
        self.assertEqual(Point(0, 1), point_from_step(3))
        self.assertEqual(Point(-1, 1), point_from_step(4))
        self.assertEqual(Point(-1, 0), point_from_step(5))
        self.assertEqual(Point(-1, -1), point_from_step(6))
        self.assertEqual(Point(0, -1), point_from_step(7))
        self.assertEqual(Point(1, -1), point_from_step(8))

    def test_transforms_for_block(self):
        self.assertEqual(['x', 'y'], transforms_for_block(1))
        self.assertEqual(['x', 'x', 'y', 'y'], transforms_for_block(2))
        self.assertEqual(['x', 'x', 'x', 'y', 'y', 'y'], transforms_for_block(3))
        self.assertEqual(['x', 'x', 'x', 'x', 'y', 'y', 'y', 'y'], transforms_for_block(4))

    def test_point_from_step(self):
        self.assertEqual(Point(0, 0), point_from_step(0))
        self.assertEqual(Point(1, 1), point_from_step(2))
        self.assertEqual(Point(-1, -1), point_from_step(6))
        self.assertEqual(Point(0, -1), point_from_step(7))

    def test_point_from_tile(self):
        self.assertEqual(Point(0, 0), point_from_tile(1))
        self.assertEqual(Point(1, 1), point_from_tile(3))
        self.assertEqual(Point(-1, -1), point_from_tile(7))
        self.assertEqual(Point(0, -1), point_from_tile(8))


class TestSpiralGrid(unittest.TestCase):

    def test_build_creates_grid_stopping_after_max(self):
        sg = SpiralGrid(20)
        sg.build()
        expected = {
            (0, 0): 1,
            (1, 0): 1,
            (1, 1): 2,
            (0, 1): 4,
            (-1, 1): 5,
            (-1, 0): 10,
            (-1, -1): 11,
            (0, -1): 23
        }
        self.assertEqual(expected, sg.grid)
