from ..day06 import (
    part1,
    part2,
    parse_races,
    parse_long_race,
    Race,
    number_of_solutions,
)

test_input = """Time:      7  15   30
Distance:  9  40  200"""


def test_parse():
    races = parse_races(test_input.splitlines())
    assert races[0] == Race(7, 9)
    assert races[1] == Race(15, 40)
    assert races[2] == Race(30, 200)


def test_parse_long():
    race = parse_long_race(test_input.splitlines())
    assert race == Race(71530, 940200)


def test_solutions():
    races = parse_races(test_input.splitlines())
    assert number_of_solutions(races[0]) == 4
    assert number_of_solutions(races[1]) == 8
    assert number_of_solutions(races[2]) == 9


def test_part1():
    assert part1() == 2374848


def test_part2():
    assert part2() == 39132886
