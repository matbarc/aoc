from ..day01 import part1, part2, get_line_value

test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def test_lines():
    lines = test_input.splitlines()
    assert get_line_value(lines[0]) == 12
    assert get_line_value(lines[1]) == 38
    assert get_line_value(lines[2]) == 15
    assert get_line_value(lines[3]) == 77


test_input_v2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_lines_v2():
    lines = test_input_v2.splitlines()
    assert get_line_value(lines[0], word_digits=True) == 29
    assert get_line_value(lines[1], word_digits=True) == 83
    assert get_line_value(lines[2], word_digits=True) == 13
    assert get_line_value(lines[3], word_digits=True) == 24
    assert get_line_value(lines[4], word_digits=True) == 42
    assert get_line_value(lines[5], word_digits=True) == 14
    assert get_line_value(lines[6], word_digits=True) == 76


def test_part1():
    assert part1() == 54953


def test_part2():
    assert part2() == 53868
