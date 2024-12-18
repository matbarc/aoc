<<<<<<< HEAD
from .common.common import read_file_to_string
import heapq


def part1() -> int:
    graph = parse_graph(read_file_to_string(__file__))
    end = [*graph][-1]
    return dijkstra(graph, 1, 3, end)


def part2() -> int:
    graph = parse_graph(read_file_to_string(__file__))
    end = [*graph][-1]
    return dijkstra(graph, 4, 10, end)


def parse_graph(input: str):
    graph = {
        y + x * 1j: int(ch)
        for y, line in enumerate(input.splitlines())
        for x, ch in enumerate(line)
    }
    return graph


def dijkstra(G, mini: int, maxi: int, end: complex) -> int:
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    priority = 0
    seen = set()

    while todo:
        val, _, pos, direc = heapq.heappop(todo)

        if pos == end:
            return val
        elif (pos, direc) in seen:
            continue
        seen.add((pos, direc))

        new_direcs = [1j / direc, -1j / direc]
        for d in new_direcs:
            for i in range(mini, maxi + 1):
                if pos + d * i in G:
                    v = sum(G[pos + d * j] for j in range(1, i + 1))
                    heapq.heappush(
                        todo, (val + v, (priority := priority + 1), pos + d * i, d)
                    )

    raise Exception
=======
from typing import Literal, NamedTuple, Optional

# from .common.common import read_file_to_string


def part1() -> int:
    # board = Board(read_file_to_string(__file__))
    return 1


def part2() -> int:
    return 1


Coord = tuple[int, int]
Direction = Literal["U", "D", "L", "R"]


class State(NamedTuple):
    path: list[Coord]
    direction: Direction
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
        states: list[State] = [State([(0, 0)], "R", 0), State([(0, 0)], "D", 0)]
        mini: dict[Coord, tuple[int, list[Coord]]] = {
            (x, y): (1_000_000_000, []) for x in range(self.w) for y in range(self.h)
        }

        while states:
            s = states.pop()
            possible_moves = self.possible_moves(s)

            for coord, direc in possible_moves:
                new_hloss = s.heat_loss + self.idx(coord)
                new_path = s.path + [coord]
                states.append(State(new_path, direc, new_hloss))
                if new_hloss < mini[coord][0]:
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
        turns: dict[Direction, tuple[Direction, Direction]] = {
            "U": ("L", "R"),
            "R": ("U", "D"),
            "L": ("U", "D"),
            "D": ("L", "R"),
        }
        coord = state.path[-1]

        turn_moves = [
            ((coord[0] + transform[direc][0], coord[1] + transform[direc][1]), direc)
            for direc in turns[state.direction]
        ]

        dx, dy = transform[state.direction]
        forward_moves = [
            ((coord[0] + i * dx, coord[1] + i * dy), state.direction)
            for i in range(1, 4)
        ]
        return [
            (move, direc)
            for (move, direc) in turn_moves + forward_moves
            if not self.is_oob(move)
        ]

    def is_oob(self, coord: Coord) -> bool:
        if not (0 <= coord[0] < self.w) or not (0 <= coord[1] < self.h):
            return True
        return False
>>>>>>> dev-2023
