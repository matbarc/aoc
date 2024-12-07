from ..day01 import (
    part1,
    part2,
    summed_dists,
    parse_into_sorted_cols,
    calculate_number_simularity_score,
    calculate_input_simularity_score,
)

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_summed_dists():
    assert summed_dists(test_input.splitlines()) == 11


def test_simularity_score():
    _, sample = parse_into_sorted_cols(test_input.splitlines())
    assert calculate_number_simularity_score(3, sample) == 9
    assert calculate_number_simularity_score(4, sample) == 4
    assert calculate_number_simularity_score(2, sample) == 0
    assert calculate_number_simularity_score(1, sample) == 0


def test_input_simularity_score():
    assert calculate_input_simularity_score(test_input.splitlines()) == 31


def test_part1():
    assert part1() == 1110981


def test_part2():
    assert part2() == 24869388
