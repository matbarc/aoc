from typing import Sequence
from .common.common import read_file_to_lines
from dataclasses import dataclass
from math import floor, ceil, prod


def part1() -> int:
    races = parse_races(read_file_to_lines(__file__))
    return prod([number_of_solutions(race) for race in races])


def part2() -> int:
    race = parse_long_race(read_file_to_lines(__file__))
    return number_of_solutions(race)


def parse_races(lines: Sequence[str]) -> list["Race"]:
    times, distances = lines[0].split()[1:], lines[1].split()[1:]
    assert len(times) == len(distances)
    races = [Race(int(t), int(d)) for t, d in zip(times, distances)]
    return races


def parse_long_race(lines: Sequence[str]) -> "Race":
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    return Race(time, distance)


@dataclass
class Race:
    time: int
    record_distance: int


# real mathy solution:
# distance = (time held) * (total time - time held)
# => distance = -(time held)^2 + (time held)(total time) [downward parabola]
# => record > -x^2 + (total time)x [call time held x]
# => 0 > -x^2 + (total time)x - record [pythagorean theorem]
# solution is space between rounded endpoints


def number_of_solutions(race: Race) -> int:
    a = -1
    b = race.time
    c = -race.record_distance

    root1, root2 = quadratic(a, b, c)

    valid_solutions = floor(root2) - ceil(root1) + 1

    # edge case if root is int
    if root1 % 1 == 0:
        valid_solutions -= 1
    if root2 % 1 == 0:
        valid_solutions -= 1
    return valid_solutions


def quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    det = (b**2 - 4 * a * c) ** 0.5
    roots = (-b - det) / (2 * a), (-b + det) / (2 * a)
    return min(roots), max(roots)
