from ..day13 import (
    find_reflection,
    part1,
    part2,
    pattern_value,
)

test_pattern = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_pattern1():
    patterns = test_pattern.split("\n\n")
    reflections = [find_reflection(pat) for pat in patterns]

    assert reflections == [("col", 4, 5), ("row", 3, 4)]
    assert sum([pattern_value(ref) for ref in reflections]) == 405


def test_pattern1_with_smudges():
    patterns = test_pattern.split("\n\n")
    reflections = [find_reflection(pat, 1) for pat in patterns]

    assert reflections == [("row", 2, 3), ("row", 0, 1)]
    assert sum([pattern_value(ref) for ref in reflections]) == 400


def test_part1():
    assert part1() == 32723


def test_part2():
    assert part2() == 34536
