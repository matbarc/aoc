from ..day16 import Board, part1, part2

test_input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


def test_test():
    board = Board(test_input)
    starting_state = ((-1, 0), "R")
    assert board.simulate(starting_state) == 46
    assert board.best_score() == 51


def test_part1():
    assert part1() == 6855


def test_part2():
    assert part2() == 7513
