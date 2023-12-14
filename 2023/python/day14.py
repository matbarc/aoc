from .common.common import read_file_to_lines, read_file_to_string
from collections import deque
import itertools as it


def part1() -> int:
    desc = read_file_to_string(__file__)
    board = Board(desc)
    board.simulate_roll((0, -1))
    return board.points()


def part2() -> int:
    desc = read_file_to_string(__file__)
    board = Board(desc)
    board.simulate_rolls(1_000_000_000)
    return board.points()


class Board:
    def __init__(self, desc: str) -> None:
        rocks = [
            (ch, (x, y))
            for y, line in enumerate(desc.splitlines())
            for x, ch in enumerate(line)
            if ch in "#O"
        ]

        self.cubes = tuple(coord for ch, coord in rocks if ch == "#")
        self.rocks = [coord for ch, coord in rocks if ch == "O"]
        self.height = desc.count("\n") + 1
        self.history = []
        return

    def simulate_roll(self, transform: tuple[int, int]):
        to_roll = deque(self.rocks[:])
        stationary = []

        while to_roll:
            cur = to_roll.popleft()

            target = (cur[0] - transform[0], cur[1] + transform[1])
            if target in to_roll:
                to_roll.append(cur)
            elif target in self.cubes or target in stationary or target[1] == -1:
                stationary.append(cur)
            else:
                to_roll.appendleft(target)

        self.rocks = tuple(sorted(stationary))
        return

    def simulate_rolls(self, n: int):
        # N W S E
        transforms = it.cycle([(0, -1), (-1, 0), (0, 1), (1, 0)])

        for i in range(n):
            cur_transform = next(transforms)
            self.simulate_roll(cur_transform)

            cur_id = hash((self.rocks, cur_transform))
            try:
                cycle_beg = self.history.index(cur_id)
                cycle_len = i - cycle_beg
                iterations_after_cycles = (n - cycle_beg) % cycle_len

                for _ in range(iterations_after_cycles):
                    cur_transform = next(transforms)
                    self.simulate_roll(cur_transform)
                break
            except ValueError:
                self.history.append(cur_id)

        return

    def points(self) -> int:
        return sum([self.height - y for _, y in self.rocks])
