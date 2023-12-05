from ..day05 import part1, part2, parse_input, locations

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_parse_seeds():
    seeds, _ = parse_input(test_input)
    assert seeds == [79, 14, 55, 13]


def test_seed_to_location():
    seeds, rosetta = parse_input(test_input)
    assert locations(seeds, rosetta) == [82, 43, 86, 35]


def test_part1():
    assert part1() == 1


def test_part2():
    assert part2() == 1
