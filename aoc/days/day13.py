import copy

from aoc.shared import open_file


class Firewall:

    def __init__(self, layer, range):
        self.layer = int(layer)
        self.range = int(range)
        self._scanner_position = 1
        self._scanner_direction = 1
        self.severity = self.layer * self.range

    def update(self):
        if self._scanner_position == self.range:
            self._scanner_direction = -1
        elif self._scanner_position == 1:
            self._scanner_direction = 1
        self._scanner_position += self._scanner_direction

    def is_caught(self, player_layer):
        if player_layer == self.layer and self._scanner_position == 1:
            return True
        return False

    def __repr__(self):
        return f"{self.layer}: {self.range} - {self._scanner_position}"


def create_firewalls(raw_data):
    firewalls = []
    for line in raw_data:
        firewalls.append(Firewall(*line.split(': ')))
    return firewalls


def update_firewalls(firewalls):
    [f.update() for f in firewalls]


def move_through_firewalls(firewalls):
    score = 0
    for i in range(93):
        for f in firewalls:
            if f.is_caught(i):
                score += f.severity
        update_firewalls(firewalls)
    return score


def is_caught(firewalls):
    for i in range(93):
        for f in firewalls:
            if f.is_caught(i):
                return True
        update_firewalls(firewalls)
    return False


def safe_passage(firewalls):
    delay = 0
    while True:
        f_copy = copy.deepcopy(firewalls)
        if not is_caught(f_copy):
            break
        update_firewalls(firewalls)
        delay += 1
        if not delay % 200:
            print(delay)
    return delay


if __name__ == '__main__':
    raw = open_file("day13").read().splitlines()
    firewalls = create_firewalls(raw)
    print(move_through_firewalls(firewalls))
    firewalls = create_firewalls(raw)
    print(safe_passage(firewalls))
