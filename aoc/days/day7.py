import re

from aoc.shared import open_file


def parse_line(line):
    name, weight, *children = re.findall('(\w+)', line)
    weight = int(weight)
    return name, weight, children


def build_program_data(raw_lines):
    parsed_lines = [parse_line(line) for line in raw_lines]

    program_data = {
        name: {'weight': weight, 'children': children}
        for name, weight, children in parsed_lines
    }
    return program_data


def get_complete_weight(program, program_data):
    weight = program_data[program]['weight']
    for child in program_data[program]['children']:
        weight += get_complete_weight(child, program_data)
    return weight


def find_bottom_program(program_data):
    all_children = []
    for p, data in program_data.items():
        all_children.extend(data['children'])
    for p in program_data:
        if p not in all_children:
            return p


def find_unbalanced(program, program_data):
    total_weights = {}
    ind_weights = {}
    for child in program_data[program]['children']:
        total_weight = get_complete_weight(child, program_data)
        total_weights[child] = total_weight
        ind_weights[child] = program_data[child]['weight']
    weight_values = list(total_weights.values())

    for child in program_data[program]['children']:
        unbalanced = find_unbalanced(child, program_data)
        if unbalanced:
            return unbalanced

    if not all(w == weight_values[0] for w in weight_values):
        return total_weights, ind_weights


def detect_anomaly_stack(stack_weights):
    for program, weight in stack_weights.items():
        if list(stack_weights.values()).count(weight) == 1:
            return program


def anomaly_difference(anomaly, weights):
    anomaly_weight = weights.pop(anomaly)
    normal_weight = list(weights.values())[0]
    return anomaly_weight - normal_weight


def corrected_weight(current, difference):
    return current - difference


def balancing_weight(program_data):
    stack_weights, disc_weights = find_unbalanced(bottom, program_data)
    anomaly = detect_anomaly_stack(stack_weights)
    difference = anomaly_difference(anomaly, stack_weights)
    return corrected_weight(disc_weights[anomaly], difference)


if __name__ == '__main__':
    raw_lines = open_file("day7").read().splitlines()
    program_data = build_program_data(raw_lines)
    bottom = find_bottom_program(program_data)
    balance = balancing_weight(program_data)
    print(bottom)
    print(balance)
