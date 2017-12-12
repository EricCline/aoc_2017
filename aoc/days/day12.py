from aoc.shared import open_file


def parse_input(raw_pipes):
    pipes = {}
    for raw_pipe in raw_pipes:
        pipe, can_talk_to = raw_pipe.split(' <-> ')
        pipes[pipe] = can_talk_to.split(', ')
    return pipes


def group(program, pipes):
    connected = set([program])
    checked = set()

    while connected.difference(checked):
        for p in connected.difference(checked):
            for k, v in pipes.items():
                if p == k or p in v:
                    connected.update(set(v))
                    connected.add(k)
            checked.add(p)
    return connected


def groups(pipes):
    groups = []
    for p in pipes:
        g = group(p, pipes)
        if g not in groups:
            groups.append(g)
    return groups


if __name__ == '__main__':
    pipes = parse_input(open_file("day12").read().splitlines())
    print(len(group('0', pipes)))
    print(len(groups(pipes)))
