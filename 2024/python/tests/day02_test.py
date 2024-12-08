from ..day02 import (
    count_safe_reports,
    is_safe_with_problem_dampener,
    part1,
    part2,
    is_safe,
)
import pytest

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

IS_SAFE_RESULTS = [True, False, False, False, False, True]
REPORTS = [[int(x) for x in line.split()] for line in test_input.splitlines()]


@pytest.mark.parametrize("test_input,expected", zip(REPORTS, IS_SAFE_RESULTS))
def test_is_safe(test_input: list[int], expected: bool):
    assert is_safe(test_input) == expected


IS_SAFE_DAMPENED_RESULTS = [True, False, False, True, True, True]


# @pytest.mark.parametrize("test_input,expected", zip(REPORTS, IS_SAFE_DAMPENED_RESULTS))
# def test_is_safe_dampened(test_input: list[int], expected: bool):
#     assert is_safe_with_problem_dampener(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([54, 52, 53, 56, 57, 58], True),
        ([94, 96, 94, 91, 88], True),
        ([12, 9, 12, 13, 15, 17, 20, 23], True),
        ([96, 98, 97, 95, 93, 90, 89], True),
    ],
)
def test_dampened_edge_cases(test_input: list[int], expected: bool):
    assert is_safe_with_problem_dampener(test_input) == expected


def test_count_safe_reports():
    reports = [[int(x) for x in line.split()] for line in test_input.splitlines()]
    assert count_safe_reports(reports) == 2


def test_part1():
    assert part1() == 379


# def test_part2():
#     assert part2() == 430
