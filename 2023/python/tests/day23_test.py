from ..day23 import part1, part2, parse_board, longest_path

test_input = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def test_test_input():
    board = parse_board(test_input)
    p0 = 0 + 1j
    p_final = [*board][-2]

    assert longest_path(board, p0, p_final) == 94


def test_test_input_slippery():
    board = parse_board(test_input)
    p0 = 0 + 1j
    p_final = [*board][-2]

    assert longest_path(board, p0, p_final, False) == 154


def test_part1():
    assert part1() == 2114


def test_part2():
    assert part2() == 6322
