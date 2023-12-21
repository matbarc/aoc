from typing import Literal, NamedTuple, Optional
from .common.common import read_file_to_string


def part1() -> int:
    board = Board(read_file_to_string(__file__))
    return 1


def part2() -> int:
    return 1


Coord = tuple[int, int]
Direction = Literal["U", "D", "L", "R"]


class State(NamedTuple):
    path: list[Coord]
    direction: Direction
    consecutives: int
    heat_loss: int


class Board:
    def __init__(self, board_str: str) -> None:
        lines = board_str.splitlines()
        self.w, self.h = len(lines[0]), len(lines)
        self._board = [int(x) for line in lines for x in line]
        return

    def idx(self, coord: Coord) -> int:
        x, y = coord
        return self._board[self.w * y + x]

    def simulate(self) -> int:
        states: list[State] = [State([(0, 0)], "R", 0, 0), State([(0, 0)], "D", 0, 0)]
        mini: dict[Coord, tuple[int, list[Coord]]] = {
            (x, y): (1_000_000_000, []) for x in range(self.w) for y in range(self.h)
        }

        while states:
            s = states.pop()
            possible_moves = self.possible_moves(s)

            for coord, direc in possible_moves:
                if self.is_oob(coord) or (direc == s.direction and s.consecutives == 3):
                    continue
                elif (new_hloss := s.heat_loss + self.idx(coord)) < mini[coord][0]:
                    new_path = s.path + [coord]
                    new_consecs = 1 if s.direction != direc else s.consecutives + 1
                    states.append(State(new_path, direc, new_consecs, new_hloss))
                    mini[coord] = new_hloss, new_path

        print(mini[(self.w - 1, self.h - 1)])
        return mini[(self.w - 1, self.h - 1)][0]

    def possible_moves(self, state: State) -> list[tuple[Coord, Direction]]:
        transform: dict[Direction, tuple[int, int]] = {
            "U": (0, -1),
            "R": (1, 0),
            "L": (-1, 0),
            "D": (0, 1),
        }
        opposite: dict[Direction, Direction] = {"U": "D", "R": "L", "L": "R", "D": "U"}

        coord = state.path[-1]
        new_coords = [
            ((coord[0] + t[0], coord[1] + t[1]), d)
            for d, t in transform.items()
            if d != opposite[state.direction]
        ]
        return new_coords

    def is_oob(self, coord: Coord) -> bool:
        if not (0 <= coord[0] < self.w) or not (0 <= coord[1] < self.h):
            return True
        return False
