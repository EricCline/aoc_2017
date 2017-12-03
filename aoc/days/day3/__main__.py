from aoc.shared import open_file
from aoc.days.day3.part1 import point_from_tile, manhattan_distance
from aoc.days.day3.part2 import SpiralGrid


if __name__ == '__main__':
    raw_num = open_file("day3").read().strip()
    start_p = point_from_tile(int(raw_num))
    end_p = point_from_tile(1)
    print(manhattan_distance(start_p, end_p))

    sg = SpiralGrid(int(raw_num))
    sg.build()
    print(sg.max_value)
