from .common.common import read_file_to_string
from typing import Optional


def part1() -> int:
    seeds, rosetta = parse_input(read_file_to_string(__file__))
    return min(locations(seeds, rosetta))


def part2() -> int:
    seeds, rosetta = parse_input_pt2(read_file_to_string(__file__))
    return min(locations(seeds, rosetta))


Seeds = list[int]


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


def parse_input_pt2(input_string: str) -> tuple["Seeds", "Rosetta"]:
    sections = input_string.split("\n\n")

    seeds = []
    seed_params = [int(n) for n in sections[0].split(":")[-1].split()]
    for i in range(len(seed_params) // 2):
        range_start, range_len = seed_params[i * 2 : (i + 1) * 2]
        seeds.extend(range(range_start, range_start + range_len))

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


class TranslationRange:
    def __init__(self, dest_start: int, source_start: int, length: int) -> None:
        self.dest_start = dest_start
        self.source_start = source_start
        self.length = length
        return

    def translate(self, val: int) -> Optional[int]:
        if self.source_start <= val < self.source_start + self.length:
            return self.dest_start + (val - self.source_start)
        return None


class Rosetta:
    def __init__(self, ranges: list[list[TranslationRange]]) -> None:
        self.tranlation_range_lists = ranges
        return

    # def seed_to_soil(self, seed: int) -> int:
    #     return self.dicts[0].get(seed, seed)

    # def soil_to_fertilizer(self, soil: int) -> int:
    #     return self.dicts[1].get(soil, soil)

    # def fertilizer_to_water(self, fertilizer: int) -> int:
    #     return self.dicts[2].get(fertilizer, fertilizer)

    # def water_to_light(self, water: int) -> int:
    #     return self.dicts[3].get(water, water)

    # def light_to_temperature(self, light: int) -> int:
    #     return self.dicts[4].get(light, light)

    # def temperature_to_humidity(self, temp: int) -> int:
    #     return self.dicts[5].get(temp, temp)

    # def humidity_to_location(self, humidity: int) -> int:
    #     return self.dicts[6].get(humidity, humidity)

    def seed_to_location(self, seed: int) -> int:
        cur = seed
        for range_list in self.tranlation_range_lists:
            for translation_range in range_list:
                if translated := translation_range.translate(cur):
                    cur = translated
                    break
        return cur
