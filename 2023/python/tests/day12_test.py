from ..day12 import arrangements, collapse_unknowns, parse_line, part1, part2

test_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def test_parse():
    idk = [parse_line(line) for line in test_input.splitlines()]

    assert arrangements(*idk[0]) == 1
    assert arrangements(*idk[0]) == 4


def test_collapse():
    string = "?#?#?#?#?#?#?#?"

    assert collapse_unknowns(string, [1, 3, 1, 6]) == ".#.###.#.######"


def test_part1():
    assert part1() == 1


def test_part2():
    assert part2() == 1
