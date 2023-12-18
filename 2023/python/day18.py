from .common.common import read_file_to_lines, read_file_to_string
from typing import NamedTuple, Literal


def part1() -> int:
    manual = read_file_to_string(__file__)
    return main(manual)


def part2() -> int:
    manual = read_file_to_string(__file__)
    return main(manual, bug=True)


Direction = Literal["U", "D", "L", "R"]
Coord = tuple[int, int]


class Instruction(NamedTuple):
    direction: Direction
    steps: int
    color: str


def main(manual: str, bug: bool = False) -> int:
    bounds: list[Coord] = []
    loop_size = 0
    coord = (0, 0)
    instructions = [parse_line(line, bug) for line in manual.splitlines()]

    for instruction in instructions:
        new_bound = bound_from_instruction(coord, instruction)
        loop_size += instruction.steps
        if new_bound in bounds:
            break
        coord = new_bound
        bounds.append(new_bound)

    lavas = count_lava_tiles(bounds, loop_size)
    return lavas


def parse_line(line: str, bug: bool) -> Instruction:
    direction, steps_str, color_code = line.split()

    if not bug:
        return Instruction(direction, int(steps_str), color_code[2:-1])

    encoded_direction = color_code[-2]
    direction_map = {"0": "R", "1": "D", "2": "L", "3": "U"}

    hexa_steps = color_code[2:-2]
    return Instruction(direction_map[encoded_direction], int(hexa_steps, 16), "")


def bound_from_instruction(coord: Coord, instruction: Instruction) -> Coord:
    transform = {"U": (0, -1), "R": (1, 0), "L": (-1, 0), "D": (0, 1)}
    dx, dy = transform[instruction.direction]
    return (coord[0] + instruction.steps * dx, coord[1] + instruction.steps * dy)


def count_lava_tiles(path: list[Coord], loop_size: int) -> int:
    """Shoelace formula + Pick's Theorem"""
    x, y = zip(*path)
    area = abs(
        sum([(x[i] * y[i - 1]) - (x[i - 1] * y[i]) for i in range(len(path))]) / 2
    )

    # Pick's Theorem
    return int(area + loop_size / 2 + 1)
