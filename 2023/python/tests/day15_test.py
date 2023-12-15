from ..day15 import part1, part2, HASH, HASHMAP, points

test_input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def test_parse():
    hashed = [HASH(x) for x in test_input.split(",")]
    assert hashed == [30, 253, 97, 47, 14, 180, 9, 197, 48, 214, 231]


def test_hmap():
    strings = [x for x in test_input.split(",")]
    hmap = HASHMAP(strings)
    print(hmap)
    assert points(hmap) == 145


def test_part1():
    assert part1() == 502139


def test_part2():
    assert part2() == 284132
