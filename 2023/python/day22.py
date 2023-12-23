from .common.common import read_file_to_lines
from typing import NamedTuple


def part1() -> int:
    return 1


def part2() -> int:
    return 1


Coord = tuple[int, int, int]
Coord2d = tuple[int, int]


class Cube:
    def __init__(self, name: str, c1: Coord, c2: Coord) -> None:
        self.name = name
        self.c1 = c1
        self.c2 = c2

    def shadow(self) -> set[Coord2d]:
        return {
            (x, y)
            for x in range(self.c1[0], self.c2[0] + 1)
            for y in range(self.c1[1], self.c2[1] + 1)
        }


def parse_cube(line: str, num: int) -> Cube:
    c1str, c2str = line.split("~")
    c1 = tuple(int(n) for n in c1str.split(","))
    c2 = tuple(int(n) for n in c2str.split(","))
    return Cube(str(num), c1, c2)


def disentegratable(cubes: list[Cube]) -> list[Cube]:
    can_disintegrate = []

    intersections = {}
    for cb1 in cubes:
        shadow = cb1.shadow()
        local_intersections = []
        for cb2 in cubes:
            if cb1 == cb2 or cb2.shadow().isdisjoint(shadow):
                continue
            local_intersections.append(cb2)

        intersections[cb1.name] = local_intersections
        if not local_intersections:
            can_disintegrate.append(cb1.name)

    return can_disintegrate


def simulate(cubes: list[Cube]) -> list[Cube]:
    res = []
    resting = []
    while cubes:
        cube = cubes.pop()
        if touching_ground(cube):
            resting.append(cube)
            res.append(cube)
            continue

        tallest_resting = find_tallest_ground(cube, resting)
        min_cube_h = cube.c1[2]
        dh = min_cube_h - tallest_resting - 1

        cube.c1 = (cube.c1[0], cube.c1[1], cube.c1[2] - dh)
        cube.c2 = (cube.c2[0], cube.c2[1], cube.c2[2] - dh)
        res.append(cube)

    return res


def find_tallest_ground(cube: Cube, resting: list[Cube]) -> int:
    shadow = cube.shadow()

    intersecting_shadows = [cb for cb in resting if cb.shadow().intersection(shadow)]
    if intersecting_shadows:
        # check here
        max(cb.c1[2] for cb in intersecting_shadows)
    return 0


def touching_ground(cube: Cube) -> bool:
    return cube.c1[2] == 1 or cube.c2[2] == 1
