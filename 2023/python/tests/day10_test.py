from ..day10 import Board, count_tiles_inside_loop, part1, part2, pathfind_loop

test_input = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

other_input = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""


def test_test_input():
    board = Board(test_input)
    path = pathfind_loop(board)
    most_distant = len(path) // 2
    assert most_distant == 8


def test_other_input():
    board = Board(other_input)
    path = pathfind_loop(board)
    most_distant = len(path) // 2
    assert most_distant == 4


test_count1 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""


def test_counts():
    board = Board(test_count1)
    loop = pathfind_loop(board)
    count = count_tiles_inside_loop(board, loop)
    assert count == 4


def test_part1():
    assert part1() == 6864


def test_part2():
    assert part2() == 349
