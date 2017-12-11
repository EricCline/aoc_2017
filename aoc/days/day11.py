from aoc.shared import open_file


class HexPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __cmp__(self, other):
        return hash(self) == hash(other)

    def _set_z(self):
        self.z = (self.x + self.y) * -1

    def move(self, direction):
        if direction == 'n':
            self.y += 1
        elif direction == 's':
            self.y += -1

        elif direction == 'ne':
            self.x += 1
        elif direction == 'nw':
            self.x += -1
            self.y += 1

        elif direction == 'se':
            self.x += 1
            self.y += -1
        elif direction == 'sw':
            self.x += -1

        self._set_z()


def point_from_directions(directions):
    max_distance = 0
    p = HexPoint(0, 0, 0)
    for d in directions:
        p.move(d)
        distance = manhattan_distance(p, HexPoint(0, 0, 0))
        if distance > max_distance:
            max_distance = distance
    return p, max_distance


def manhattan_distance(point_a, point_b):
    return max((
        abs(point_a.x - point_b.x),
        abs(point_a.y - point_b.y),
        abs(point_a.z - point_b.z),
    ))


if __name__ == '__main__':
    directions = open_file("day11").read().strip().split(',')
    p, max_distance = point_from_directions(directions)
    print(manhattan_distance(p, HexPoint(0, 0, 0)))
    print(max_distance)
