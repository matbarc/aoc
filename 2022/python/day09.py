from dataclasses import dataclass, replace
import math
from enum import Enum, auto

from .common.common import read_file_to_lines

# TODO: Make this solution generally less bad. Terribly over-engineered


@dataclass(frozen=True, repr=True, eq=True)
class Pos:
    x: int
    y: int


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()


class Simulation:
    def __init__(self, knots: int = 1) -> None:
        if knots < 1:
            raise ValueError("Need to track at least one knot")

        self.origin = Pos(0, 0)
        self.head_pos = Pos(0, 0)
        self.knots_no = knots
        self.knots = [Pos(0, 0) for _ in range(knots)]

        self.tail_visited = set([self.knots[-1]])
        return

    def simulate_command(self, command: str) -> None:
        direction, steps = self.parse_command(command)
        while steps > 0:
            self._move_head_one_step(direction)
            steps -= 1
        # self.print_grid()
        return

    def _move_head_one_step(self, direction: Direction) -> None:
        if direction == Direction.DOWN:
            self.head_pos = replace(self.head_pos, y=self.head_pos.y - 1)
        elif direction == Direction.UP:
            self.head_pos = replace(self.head_pos, y=self.head_pos.y + 1)
        elif direction == Direction.LEFT:
            self.head_pos = replace(self.head_pos, x=self.head_pos.x - 1)
        elif direction == Direction.RIGHT:
            self.head_pos = replace(self.head_pos, x=self.head_pos.x + 1)

        for index in range(self.knots_no):
            self._chase(index)
        return

    def _chase(self, knot_index: int) -> None:
        knot_pos = self.knots[knot_index]
        knot_in_front = self.head_pos if knot_index == 0 else self.knots[knot_index - 1]

        dx = knot_in_front.x - knot_pos.x
        dy = knot_in_front.y - knot_pos.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance <= math.sqrt(2):
            return

        if dx == 0:
            new_pos = replace(knot_pos, y=knot_pos.y + math.copysign(1, dy))
        elif dy == 0:
            new_pos = replace(knot_pos, x=knot_pos.x + math.copysign(1, dx))
        else:  # diagonals
            new_pos = replace(
                knot_pos,
                x=knot_pos.x + math.copysign(1, dx),
                y=knot_pos.y + math.copysign(1, dy),
            )

        self.knots[knot_index] = new_pos
        if knot_index == self.knots_no - 1:
            self.tail_visited.add(new_pos)
        return

    @staticmethod
    def parse_command(command: str) -> tuple[Direction, int]:
        direction_str, steps_str = command.split()

        direction_lookup = {
            "U": Direction.UP,
            "D": Direction.DOWN,
            "L": Direction.LEFT,
            "R": Direction.RIGHT,
        }

        return (direction_lookup[direction_str], int(steps_str))

    def print_grid(self) -> None:
        for yprime in range(10, -1, -1):
            string = ""
            for xprime in range(10):
                coord = Pos(xprime, yprime)

                if coord == self.head_pos:
                    string += "H "
                elif coord in self.knots:
                    index = self.knots.index(coord)
                    string += f"{index+1} "
                elif xprime == yprime == 0:
                    string += "s "
                else:
                    string += ". "
            print(string)
        return

    def __repr__(self) -> str:
        string = (
            "===========================\n"
            f"head: {self.head_pos}\n"
            + f"visited: {self.tail_visited}\n"
            + "============================"
        )
        return string


def part1() -> int:
    lines = read_file_to_lines(__file__)

    sim = Simulation(knots=1)
    for line in lines:
        sim.simulate_command(line)
    return len(sim.tail_visited)


def part2() -> int:
    lines = read_file_to_lines(__file__)

    sim = Simulation(knots=9)
    for line in lines:
        sim.simulate_command(line)

    return len(sim.tail_visited)
