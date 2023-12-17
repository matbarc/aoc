from typing import Literal, Optional
from .common.common import read_file_to_string


def part1() -> int:
    board = Board(read_file_to_string(__file__))
    return board.simulate(((-1, 0), "R"))


def part2() -> int:
    board = Board(read_file_to_string(__file__))
    return board.best_score()


Coord = tuple[int, int]
Direction = Literal["U", "D", "L", "R"]
PhotonState = tuple[Coord, Direction]
Mirror = Literal["\\", "/", "-", "|"]


class Board:
    def __init__(self, board_str: str) -> None:
        lines = board_str.splitlines()
        self.w, self.h = len(lines[0]), len(lines)
        self._board = [x for line in lines for x in line]
        return

    def idx(self, coord: Coord) -> str:
        x, y = coord
        return self._board[self.w * y + x]

    def simulate(self, starting_state: PhotonState) -> int:
        photons: list[PhotonState] = [starting_state]
        states_visited = set()
        coords_visited = set()

        while photons:
            state = photons.pop()

            next_state = self.try_move(state)
            if not next_state or next_state in states_visited:
                continue

            states_visited.add(next_state)
            coords_visited.add(next_state[0])
            if (tile := self.idx(next_state[0])) in "/\\-|":
                photons.extend(self.simulate_encounters(next_state, tile))
            else:
                photons.append(next_state)

        return len(coords_visited)

    def best_score(self) -> int:
        top = [((x, -1), "D") for x in range(self.w)]
        bottom = [((x, self.h), "U") for x in range(self.w)]
        left = [((-1, y), "R") for y in range(self.h)]
        right = [((self.w, y), "L") for y in range(self.h)]

        return max([self.simulate(start) for start in [*top, *bottom, *left, *right]])

    def simulate_encounters(
        self, state: PhotonState, mirror: Mirror
    ) -> list[PhotonState]:
        coord, direction = state

        match (mirror, direction):
            case ("-", ("R" | "L")):
                return [state]
            case ("-", _):
                return [(coord, "R"), (coord, "L")]
            case ("|", ("U" | "D")):
                return [state]
            case ("|", _):
                return [(coord, "U"), (coord, "D")]
            case ("/", "U"):
                return [(coord, "R")]
            case ("/", "D"):
                return [(coord, "L")]
            case ("/", "R"):
                return [(coord, "U")]
            case ("/", "L"):
                return [(coord, "D")]
            case ("\\", "U"):
                return [(coord, "L")]
            case ("\\", "D"):
                return [(coord, "R")]
            case ("\\", "R"):
                return [(coord, "D")]
            case ("\\", "L"):
                return [(coord, "U")]

        return []

    def try_move(self, state: PhotonState) -> Optional[PhotonState]:
        (x, y), direc = state

        match direc:
            case "U":
                coord = (x, y - 1)
            case "R":
                coord = (x + 1, y)
            case "L":
                coord = (x - 1, y)
            case "D":
                coord = (x, y + 1)

        if not (0 <= coord[0] < self.w) or not (0 <= coord[1] < self.h):
            return None
        return coord, direc

    def __repr__(self) -> str:
        string = ""
        for i in range(0, self.h):
            string += str(self._board[i * self.w : self.w * (i + 1)]) + "\n"
        return string
