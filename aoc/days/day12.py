from aoc.shared import open_file



def parse_input(raw_pipes):
    pipes = {}
    for raw_pipe in raw_pipes:
        pipe, can_talk_to = raw_pipe.split(' <-> ')
        pipes[pipe] = can_talk_to.split(', ')
    return pipes





def can_talk_to(program, pipes):
    connected = set()

    to_check = pipes[program]
    while to_check:
        next_check = []
        for p in to_check:
            if p not in connected:
                next_check.append(p)
            connected.add(p)
        to_check = next_check

    return connected


if __name__ == '__main__':
    pipes = parse_input(open_file("day12").read().splitlines())
    print(can_talk_to('0', pipes))
