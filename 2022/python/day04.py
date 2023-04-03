from .common.common import read_file_to_lines


test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def part1() -> int:
    range_pairs = read_file_to_lines(__file__, transformation=translate_line_to_ranges)
    pairs_with_full_overlap = [pair for pair in range_pairs if one_is_subset(*pair)]

    return len(pairs_with_full_overlap)


def part2() -> int:
    range_pairs = read_file_to_lines(__file__, transformation=translate_line_to_ranges)
    pairs_with_overlap = [pair for pair in range_pairs if not mutually_exclusive(*pair)]

    return len(pairs_with_overlap)


def translate_line_to_ranges(line: str) -> tuple[range, range]:
    range_code1, range_code2 = line.split(",")

    start1, stop1 = range_code1.split("-")
    start2, stop2 = range_code2.split("-")

    return range(int(start1), int(stop1) + 1), range(int(start2), int(stop2) + 1)


def one_is_subset(r1: range, r2: range) -> bool:
    return (r1.start in r2 and r1[-1] in r2) or (r2.start in r1 and r2[-1] in r1)


def mutually_exclusive(r1: range, r2: range) -> bool:
    return r1[-1] < r2.start or r2[-1] < r1.start
