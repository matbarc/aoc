from .common.common import read_file_to_string
from dataclasses import dataclass


def part1() -> int:
    input_str = read_file_to_string(__file__)
    board = Board(input_str)
    return sum(board.valid_numbers())


def part2() -> int:
    input_str = read_file_to_string(__file__)
    board = Board(input_str)
    return sum(num1.value * num2.value for num1, num2 in board.gears())


class Board:
    SYMBOLS = "!@#$%^&*/+=-"

    def __init__(self, input_str: str) -> None:
        self.length = input_str.find("\n")

        self.board = input_str.replace("\n", "")
        self.numbers: list[Number] = []
        self.symbols: list[Symbol] = []

        val = ""
        idxs = []
        for i, ch in enumerate(self.board):
            if ch.isnumeric():
                val += ch
                idxs.append(i)
            elif val:
                self.numbers.append(Number(idxs, int(val), self.boundary(idxs)))
                val = ""
                idxs = []

        for i, ch in enumerate(self.board):
            if ch in self.SYMBOLS:
                self.symbols.append(Symbol([i], ch, self.boundary([i])))
        return

    def valid_numbers(self) -> list[int]:
        nums = [n.value for n in self.numbers if self.boundary_check(n)]
        return nums

    def gears(self) -> list[tuple["Number", "Number"]]:
        stars = [symbol for symbol in self.symbols if symbol.value == "*"]
        gears = []

        for star in stars:
            star_matches = []
            for num in self.numbers:
                if star.coords[0] in num.boundary:
                    star_matches.append(num)

            if len(star_matches) == 2:
                gears.append((star_matches[0], star_matches[1]))
        return gears

    def boundary(self, coords: list[int]) -> list[int]:
        left_anchor, right_anchor = min(coords), max(coords)
        boundary_idxs = [
            i - self.length for i in range(left_anchor - 1, right_anchor + 2)
        ]
        boundary_idxs += [(left_anchor - 1), (right_anchor + 1)]
        boundary_idxs += [
            i + self.length for i in range(left_anchor - 1, right_anchor + 2)
        ]

        return [i for i in boundary_idxs if 0 <= i <= len(self.board)]

    def boundary_check(self, num: "Number") -> bool:
        return any(self.board[i] in self.SYMBOLS for i in num.boundary)


@dataclass
class Number:
    coords: list[int]
    value: int
    boundary: list[int]


@dataclass
class Symbol:
    coords: list[int]
    value: str
    boundary: list[int]
