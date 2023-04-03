from .common.common import read_file_to_lines

example_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def part1() -> int:
    lines = read_file_to_lines(__file__)
    items = []
    priority_sum = 0

    for line in lines:
        limit = len(line) // 2
        for ch in line[: limit + 1]:
            if line.find(ch, limit) != -1:
                items.append(ch)
                priority_sum += get_priority(ch)
                break

    return priority_sum


def part2() -> int:
    lines = read_file_to_lines(__file__)
    items = []
    priority_sum = 0

    for i in range(len(lines) // 3):
        start_i = i * 3
        l1, l2, l3 = lines[start_i : start_i + 3]
        for ch in l1:
            if l2.find(ch) != -1 and l3.find(ch) != -1:
                items.append(ch)
                priority_sum += get_priority(ch)
                break

    return priority_sum


def get_priority(char: str) -> int:
    if len(char) != 1 or not char.isalpha():
        raise ValueError("Can only deal with single characters")

    if char.isupper():
        return ord(char) - 38  # A - 27 ... Z - 56

    return ord(char) - 96  # a - 1 ... z - 26
