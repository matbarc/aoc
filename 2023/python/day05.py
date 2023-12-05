from .common.common import read_file_to_string


def part1() -> int:
    seeds, rosetta = parse_input(read_file_to_string(__file__))
    return min(locations(seeds, rosetta))


def part2() -> int:
    return 1


Seeds = list[int]


def locations(seeds: Seeds, rosetta: "Rosetta") -> list[int]:
    return [rosetta.seed_to_location(seed) for seed in seeds]


def parse_input(input_string: str) -> tuple["Seeds", "Rosetta"]:
    sections = input_string.split("\n\n")

    seeds = [int(n) for n in sections[0].split(":")[-1].split()]

    dicts = []
    for section_line in sections[1:]:
        [_, *lines] = section_line.splitlines()
        dic = {}

        for line in lines:
            dest_start, source_start, range_len = [int(x) for x in line.split()]
            for i in range(range_len):
                dic[source_start + i] = dest_start + i

        dicts.append(dic)

    return (seeds, Rosetta(dicts))


class Rosetta:
    def __init__(self, dicts: list[dict[int, int]]) -> None:
        self.dicts = dicts
        return

    def seed_to_soil(self, seed: int) -> int:
        return self.dicts[0].get(seed, seed)

    def soil_to_fertilizer(self, soil: int) -> int:
        return self.dicts[1].get(soil, soil)

    def fertilizer_to_water(self, fertilizer: int) -> int:
        return self.dicts[2].get(fertilizer, fertilizer)

    def water_to_light(self, water: int) -> int:
        return self.dicts[3].get(water, water)

    def light_to_temperature(self, light: int) -> int:
        return self.dicts[4].get(light, light)

    def temperature_to_humidity(self, temp: int) -> int:
        return self.dicts[5].get(temp, temp)

    def humidity_to_location(self, humidity: int) -> int:
        return self.dicts[6].get(humidity, humidity)

    def seed_to_location(self, seed: int) -> int:
        cur = seed
        for dic in self.dicts:
            cur = dic.get(cur, cur)
        return cur
