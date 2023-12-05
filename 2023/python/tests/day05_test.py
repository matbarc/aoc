from ..day05 import part1, part2, parse_input, parse_input_pt2, locations

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


def test_parse_seeds2():
    seeds, _ = parse_input_pt2(test_input)
    assert len(seeds) == 27
    assert min(seeds) == 55
    assert max(seeds) == 92


def test_seed_to_location():
    seeds, rosetta = parse_input(test_input)
    assert locations(seeds, rosetta) == [82, 43, 86, 35]


def test_seed_to_location_pt2():
    seeds, rosetta = parse_input_pt2(test_input)
    assert min(locations(seeds, rosetta)) == 46


def test_part1():
    assert part1() == 379_811_651


def test_part2():
    assert part2() == 1
