from .common.common import read_file_to_lines


def part1() -> int:
    line_vals = read_file_to_lines(__file__)

    return summed_dists(line_vals)


def part2() -> int:
    line_vals = read_file_to_lines(__file__)
    return calculate_input_simularity_score(line_vals)


def summed_dists(input_lines: list[str]) -> int:
    col1, col2 = parse_into_sorted_cols(input_lines)

    dists = [abs(x - y) for x, y in zip(col1, col2)]
    return sum(dists)


def parse_into_sorted_cols(input_lines: list[str]) -> tuple[list[int], list[int]]:
    lines = [line.split() for line in input_lines]
    line_pairs = [(int(x), int(y)) for x, y in lines]

    sorted_col1 = sorted([x for x, _ in line_pairs])
    sorted_col2 = sorted([y for _, y in line_pairs])
    return sorted_col1, sorted_col2


def calculate_number_simularity_score(num: int, sample: list[int]) -> int:
    return num * sample.count(num)


def calculate_input_simularity_score(input_lines: list[str]) -> int:
    col1, col2 = parse_into_sorted_cols(input_lines)

    return sum([calculate_number_simularity_score(x, col2) for x in col1])
