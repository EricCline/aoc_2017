class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __cmp__(self, other):
        return hash(self) == hash(other)


def steps_through_block(block):
    if block == 0:
        return 0
    return block * (block + 1)


def block_before_step(step):
    for i in range(step):
        steps = steps_through_block(i)
        if  steps > step:
            return i - 1
        elif steps == step:
            return i
    return 0


def transforms_for_block(block):
    transforms = ['x'] * block
    transforms += ['y'] * block
    return transforms


def point_from_tile(tile):
    return point_from_step(tile - 1)


def point_from_step(step):
    previous_block = block_before_step(step)
    steps_remaining = step - steps_through_block(previous_block)
    transforms = transforms_for_block(previous_block + 1)[:steps_remaining]

    point = point_from_block(previous_block)
    if point.x <= 0:
        # we are in the lower left corner
        for t in transforms:
            setattr(point, t, getattr(point, t) + 1)
    else:
        # we are in the upper right corner
        for t in transforms:
            setattr(point, t, getattr(point, t) - 1)
    return point


def point_from_block(block):
    p = Point(0, 0)
    for _ in range(1, block + 1):
        if p.x <= 0:
            p.x = abs(p.x) + 1
        else:
            p.x = abs(p.x) * -1

        if p.y <= 0:
            p.y = abs(p.y) + 1
        else:
            p.y = abs(p.y) * -1
    return p


def manhattan_distance(point_a, point_b):
    return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)
