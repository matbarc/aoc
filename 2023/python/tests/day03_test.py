from ..day03 import part1, part2, Board, Number

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_parse():
    board = Board(test_input)
    expected = [467, 114, 35, 633, 617, 58, 592, 755, 664, 598]

    assert [n.value for n in board.numbers] == expected


def test_length():
    board = Board(test_input)
    assert board.length == 10


def test_114():
    board = Board(test_input)
    num = board.numbers[1]

    assert board.numbers[1] == num
    assert num.boundary == [4, 8, 14, 15, 16, 17, 18]
    assert not board.boundary_check(num)


def test_boundary():
    board = Board(test_input)
    num = board.numbers[3]

    assert num.coords == [26, 27, 28]
    assert num.boundary == [15, 16, 17, 18, 19, 25, 29, 35, 36, 37, 38, 39]


def test_valid_numbers():
    board = Board(test_input)
    expected = [467, 35, 633, 617, 592, 755, 664, 598]

    assert board.valid_numbers() == expected


def test_gears():
    board = Board(test_input)
    gear_power = [num1.value * num2.value for (num1, num2) in board.gears()]

    assert gear_power == [16345, 451490]


def test_part1():
    assert part1() == 521601


def test_part2():
    assert part2() == 1
