from ..day14 import Board, part1, part2

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
    board = Board(test_input)
    board.simulate_roll((0, -1))
    assert board.points() == 136


def test_part1():
    assert part1() == 113525


def test_part2():
    assert part2() == 1
