from ..day14 import part1, part2, points, roll_up

test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def test_parse():
    grid = test_input.splitlines()
    grid = roll_up(grid)
    assert points(grid) == 136


def test_part1():
    assert part1() == 113525


def test_part2():
    assert part2() == 101292
