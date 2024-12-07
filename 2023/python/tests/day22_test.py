from ..day22 import part1, part2, parse_cube

test_input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def test_parse():
    cubes = sorted(
        [parse_cube(line, i) for i, line in enumerate(test_input.splitlines())],
        key=lambda x: (x.c1[2], x.c2[2]),
    )

    assert True


def test_part1():
    assert part1() == 1


def test_part2():
    assert part2() == 1
