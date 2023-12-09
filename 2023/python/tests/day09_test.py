from ..day09 import extrapolate, extrapolate_backwards, parse_series, part1, part2

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_test_input():
    seriess = [parse_series(x) for x in test_input.splitlines()]
    assert sum(extrapolate(x) for x in seriess) == 114
    assert sum(extrapolate_backwards(x) for x in seriess) == 2


def test_part1():
    assert part1() == 1819125966


def test_part2():
    assert part2() == 1140


def test_example_cases():
    i_o = {
        "0 0 0 0 0": 0,
        "3 3 3 3 3": 3,
        "0 3 6 9 12 15": 18,
        "1 3 6 10 15 21": 28,
        "10 13 16 21 30 45": 68,
    }

    for k, v in i_o.items():
        assert extrapolate(parse_series(k)) == v


def test_example_backwards():
    i_o = {
        "0 0 0 0 0": 0,
        "3 3 3 3 3": 3,
        "0 3 6 9 12 15": -3,
        "1 3 6 10 15 21": 0,
        "2 3 4 5 6": 1,
        "1 1 1 1": 1,
        "10 13 16 21 30 45": 5,
    }

    for k, v in i_o.items():
        assert extrapolate_backwards(parse_series(k)) == v
