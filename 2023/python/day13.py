from .common.common import read_file_to_string
from typing import Literal, NamedTuple


def part1() -> int:
    notes = read_file_to_string(__file__)
    patterns = notes.split("\n\n")
    reflections = [find_reflection(pat) for pat in patterns]
    return sum([pattern_value(ref) for ref in reflections])


def part2() -> int:
    notes = read_file_to_string(__file__)
    patterns = notes.split("\n\n")
    reflections = [find_reflection(pat, smudges=1) for pat in patterns]
    return sum([pattern_value(ref) for ref in reflections])


def transpose(rows: list[str]) -> list[str]:
    cols = ["" for _ in range(len(rows[0]))]
    for row in rows:
        for i, ch in enumerate(row):
            cols[i] += ch
    return cols


def find_horizontal_pairs(rows: list[str], smudges: int) -> list[tuple[int, int]]:
    pairs = []
    for i in range(len(rows) - 1):
        if ch_diff(rows[i], rows[i + 1]) <= smudges:
            pairs.append((i, i + 1))
    return pairs


def ch_diff(row1: str, row2: str) -> int:
    return len([ch1 for ch1, ch2 in zip(row1, row2) if ch1 != ch2])


def check_horizontal_pair(rows: list[str], pair: tuple[int, int], smudges: int) -> bool:
    y1, y2 = pair
    span_up, span_down = y1, len(rows) - y2 - 1
    span = min(span_up, span_down)

    str1 = "".join(rows[y1 - span : y2])
    str2 = "".join(reversed(rows[y2 : y2 + span + 1]))
    dif = ch_diff(str1, str2)
    return dif == smudges


Reflection = tuple[Literal["row"] | Literal["col"], int, int]


def find_reflection(pattern: str, smudges: int = 0) -> Reflection:
    rows = pattern.splitlines()
    hor_pairs = find_horizontal_pairs(rows, smudges)
    for pair in hor_pairs:
        if check_horizontal_pair(rows, pair, smudges):
            return ("row", *pair)

    cols = transpose(rows)
    vert_pairs = find_horizontal_pairs(cols, smudges)
    for pair in vert_pairs:
        if check_horizontal_pair(cols, pair, smudges):
            return ("col", *pair)
    raise ValueError("not found")


def pattern_value(reflection: Reflection) -> int:
    plane, _, b = reflection
    if plane == "row":
        return b * 100
    return b
