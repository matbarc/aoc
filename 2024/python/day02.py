import math
from .common.common import read_file_to_lines

# line -> report
# report -> many "levels" (numbers)
#
# example:
#
# 1 2 3 4 5 <- report (has 4 levels)
# 5 6 7 8 8
#
# "safe" -> gradually increasing or decreasing (1 <= delta <= 3)


def transformation(line: str):
    return [int(x) for x in line.split()]


def part1() -> int:
    reports = read_file_to_lines(__file__, transformation)
    return count_safe_reports(reports)


def part2() -> int:
    reports = read_file_to_lines(__file__, transformation)
    return count_dampened_safe_reports(reports)


def is_safe(report: list[int]) -> bool:
    sign = None

    for i, val in enumerate(report):
        # last index
        if i == len(report) - 1:
            break

        # normal body
        old_sign = sign

        dif = val - report[i + 1]
        sign = math.copysign(1, dif)

        is_monotonic = old_sign is None or sign == old_sign
        is_in_safe_range = 1 <= abs(dif) <= 3
        if not is_in_safe_range or not is_monotonic:
            return False

    return True


def is_safe_with_problem_dampener(report: list[int], levels_removed: int = 0) -> bool:
    sign = None

    for i, val in enumerate(report):
        # last index
        if i == len(report) - 1:
            break

        # normal body
        old_sign = sign

        dif = val - report[i + 1]
        sign = math.copysign(1, dif)

        is_monotonic = old_sign is None or sign == old_sign
        is_in_safe_range = 1 <= abs(dif) <= 3
        if not is_in_safe_range or not is_monotonic:
            if levels_removed > 0:
                return False

            is_safe_with_cur_removed: bool = is_safe_with_problem_dampener(
                report[:i] + report[i + 1 :], 1
            )

            is_safe_with_next_removed: bool = is_safe_with_problem_dampener(
                report[: i + 1] + report[i + 2 :], 1
            )

            if i != 1:
                return is_safe_with_cur_removed or is_safe_with_next_removed

            is_safe_with_prev_removed: bool = is_safe_with_problem_dampener(
                report[i:], 1
            )
            return (
                is_safe_with_prev_removed
                or is_safe_with_next_removed
                or is_safe_with_next_removed
            )

    return True


def count_safe_reports(reports: list[list[int]]) -> int:
    return sum([is_safe(report) for report in reports])


def count_dampened_safe_reports(reports: list[list[int]]) -> int:
    return sum([is_safe_with_problem_dampener(report) for report in reports])
