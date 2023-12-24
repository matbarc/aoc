from .common.common import read_file_to_string
from typing import Optional


def part1() -> int:
    seeds, rosetta = parse_input(read_file_to_string(__file__))
    return min(locations(seeds, rosetta))


def part2() -> int:
    intervals, rosetta = parse_input_pt2(read_file_to_string(__file__))

    intervals = intervals.copy()
    for range_list in rosetta.tranlation_range_lists:
        intervals = apply_transformation_to_ranges(intervals, range_list)

    return min(intervals)[0]


Seeds = list[int]
Interval = tuple[int, int]


def apply_transformation_to_ranges(
    ints: list[Interval], rules: list["TranslationRange"]
) -> list[Interval]:
    to_process = ints
    res = []

    for rule in rules:
        next_rule = []
        while to_process:
            lb, ub = to_process.pop()
            rule_lb, rule_ub = rule.source_interval

            before = (lb, min(ub, rule_lb))
            if before[1] > before[0]:
                next_rule.append(before)

            inter = (max(lb, rule_lb), min(rule_ub, ub))
            if inter[1] > inter[0]:
                res.append(
                    (inter[0] - rule_lb + rule.dest, inter[1] - rule_lb + rule.dest)
                )

            after = (max(rule_ub, lb), ub)
            if after[1] > after[0]:
                next_rule.append(after)

        to_process = next_rule
    return res + next_rule


def locations(seeds: Seeds, rosetta: "Rosetta") -> list[int]:
    return [rosetta.seed_to_location(seed) for seed in seeds]


def parse_input(input_string: str) -> tuple["Seeds", "Rosetta"]:
    sections = input_string.split("\n\n")

    seeds = [int(n) for n in sections[0].split(":")[-1].split()]

    range_lists = []
    for section_line in sections[1:]:
        [_, *lines] = section_line.splitlines()
        ranges = []

        for line in lines:
            dest_start, source_start, range_len = [int(x) for x in line.split()]
            translation_range = TranslationRange(dest_start, source_start, range_len)
            ranges.append(translation_range)

        range_lists.append(ranges)

    return (seeds, Rosetta(range_lists))


def parse_input_pt2(input_string: str) -> tuple[list[tuple[int, int]], "Rosetta"]:
    sections = input_string.split("\n\n")

    seed_intervals: list[Interval] = []
    seed_params = [int(n) for n in sections[0].split(":")[-1].split()]
    for i in range(len(seed_params) // 2):
        range_start, range_len = seed_params[i * 2 : (i + 1) * 2]
        seed_intervals.append((range_start, range_start + range_len))

    range_lists = []
    for section_line in sections[1:]:
        [_, *lines] = section_line.splitlines()
        ranges = []

        for line in lines:
            dest_start, source_start, range_len = [int(x) for x in line.split()]
            translation_range = TranslationRange(dest_start, source_start, range_len)
            ranges.append(translation_range)

        range_lists.append(ranges)

    return (seed_intervals, Rosetta(range_lists))


class TranslationRange:
    def __init__(self, dest_start: int, source_start: int, length: int) -> None:
        self.dest_interval = (dest_start, dest_start + length)
        self.source_interval = (source_start, source_start + length)
        self.dest = dest_start
        return

    def translate(self, val: int) -> Optional[int]:
        source_lb, source_ub = self.source_interval
        if source_lb <= val < source_ub:
            return self.dest_interval[0] + (val - source_lb)
        return None


class Rosetta:
    def __init__(self, ranges: list[list[TranslationRange]]) -> None:
        self.tranlation_range_lists = ranges
        return

    def seed_to_location(self, seed: int) -> int:
        cur = seed
        for range_list in self.tranlation_range_lists:
            for translation_range in range_list:
                if translated := translation_range.translate(cur):
                    cur = translated
                    break
        return cur
