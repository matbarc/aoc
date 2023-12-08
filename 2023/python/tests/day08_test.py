from ..day08 import part1, part2, parse_network, simulate

test_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


def test_parse():
    instructions, net = parse_network(test_input)
    turns = simulate(instructions, net)
    assert turns == 2


def test_part1():
    assert part1() == 12169


def test_part2():
    assert part2() == 1
