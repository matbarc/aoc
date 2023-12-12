from .common.common import read_file_to_string
import itertools as it

Coord = tuple[int, int]


def part1() -> int:
    mapstr = read_file_to_string(__file__)
    coords = parse_coords(mapstr)
    empty_rows = parse_empty_rows(mapstr)
    empty_cols = parse_empty_cols(mapstr)
    coords = expanded_coords(coords, empty_rows, empty_cols)
    return solve(coords)


def part2() -> int:
    mapstr = read_file_to_string(__file__)
    coords = parse_coords(mapstr)
    empty_rows = parse_empty_rows(mapstr)
    empty_cols = parse_empty_cols(mapstr)
    coords = expanded_coords(coords, empty_rows, empty_cols, 1_000_000)
    return solve(coords)


def parse_coords(mapstr: str) -> list[Coord]:
    width = mapstr.find("\n")
    mapstr = mapstr.replace("\n", "")
    coords = [(i % width, i // width) for i, ch in enumerate(mapstr) if ch == "#"]
    return coords


def parse_empty_rows(mapstr: str) -> list[int]:
    return [i for i, line in enumerate(mapstr.splitlines()) if line == "." * len(line)]


def parse_empty_cols(mapstr: str) -> list[int]:
    lines = mapstr.splitlines()
    empty_cols = [
        x for x in range(len(lines[0])) if all([line[x] == "." for line in lines])
    ]
    return empty_cols


def expanded_coords(
    coords: list[Coord], rows: list[int], cols: list[int], substitution_amount: int = 2
) -> list[Coord]:
    new_coords = []

    for x, y in coords:
        dy = len([row for row in rows if row < y]) * (substitution_amount - 1)
        dx = len([col for col in cols if col < x]) * (substitution_amount - 1)
        new_coords.append((x + dx, y + dy))
    return new_coords


def solve(coords: list[Coord]) -> int:
    pairs = it.combinations(coords, 2)
    return sum([manhanttan_d(*pair) for pair in pairs])


def manhanttan_d(c1: tuple[int, int], c2: tuple[int, int]) -> int:
    x1, y1 = c1
    x2, y2 = c2
    return abs(x1 - x2) + abs(y1 - y2)
