from aoc.days.day3.part1 import Point, point_from_tile


class SpiralGrid:

    def __init__(self, stop_value):
        self.stop_value = stop_value
        self.grid = {}

    @property
    def max_value(self):
        return max(self.grid.values())

    def build(self):
        value = 1
        point_gen = self._points()
        while value <= self.stop_value:
            point = next(point_gen)
            value = self._next_value(point)
            self.grid[point] = value

    def _next_value(self, point):
        adj_points = self._adjacent_points(point)
        return sum(
            self.grid.get(p, 0) for p in adj_points
        ) or 1

    def _adjacent_points(self, point):
        possible_x = (point.x, point.x + 1, point.x -1)
        possible_y = (point.y, point.y + 1, point.y -1)

        adj_points = [
            Point(x, y)
            for x in possible_x
            for y in possible_y
        ]
        adj_points.remove(point)
        return adj_points

    def _points(self):
        tile = 1
        while True:
            yield point_from_tile(tile)
            tile += 1
