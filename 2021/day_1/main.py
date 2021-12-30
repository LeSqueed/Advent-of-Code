#!/usr/bin/python
import os

filename = 'input_sample.txt'


def read_file(file):
    return [line.rstrip() for line in open(file)]


def is_higher(value1, value2):
    return True if value1 > value2 else False


def count_higher(file):
    _input = read_file(file)

    higher = 0
    previous_line = ''

    for line in _input:
        # Don't do anything if this is our first run.
        if previous_line != '':
            higher += 1 if is_higher(int(line), int(previous_line)) else 0
        previous_line = line

    return str(higher)


def count_higher_part2(file):
    _input = read_file(file)

    higher = 0
    first_line = ''
    previous_line = ''

    values = []
    # Build an array with the values we need.
    for line in _input:
        if first_line != '':
            values.append(int(first_line) + int(previous_line) + int(line))
        first_line = previous_line
        previous_line = line

    # Now we got a new dictionary with the values to compare.
    previous_value = ''
    for value in values:
        if previous_value != '':
            higher += 1 if is_higher(int(value), int(previous_value)) else 0
        previous_value = value

    return str(higher)


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    inputFile = dir_path + '/input.txt'

    print(count_higher(inputFile))

    print(count_higher_part2(inputFile))
