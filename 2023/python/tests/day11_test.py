from ..day11 import (
    manhanttan_d,
    parse_coords,
    parse_empty_cols,
    parse_empty_rows,
    part1,
    part2,
    expanded_coords,
    solve,
)

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

test_expanded = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""


def test_case():
    coords = parse_coords(test_input)
    empty_rows = parse_empty_rows(test_input)
    empty_cols = parse_empty_cols(test_input)
    coords = expanded_coords(coords, empty_rows, empty_cols)
    assert solve(coords) == 374


def test_case10():
    coords = parse_coords(test_input)
    empty_rows = parse_empty_rows(test_input)
    empty_cols = parse_empty_cols(test_input)
    coords = expanded_coords(coords, empty_rows, empty_cols, 10)
    assert solve(coords) == 1030


def test_case100():
    coords = parse_coords(test_input)
    empty_rows = parse_empty_rows(test_input)
    empty_cols = parse_empty_cols(test_input)
    coords = expanded_coords(coords, empty_rows, empty_cols, 100)
    assert solve(coords) == 8410


def test_expansion():
    coords = parse_coords(test_input)
    empty_rows = parse_empty_rows(test_input)
    empty_cols = parse_empty_cols(test_input)
    coords = expanded_coords(coords, empty_rows, empty_cols)
    assert coords == parse_coords(test_expanded)


def test_manhattan():
    assert manhanttan_d((1, 6), (5, 11)) == 9


def test_part1():
    assert part1() == 9974721


def test_part2():
    assert part2() == 1
