from ..day08 import part1, part2, parse_network, simulate, simulate_pt2

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


test_input2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def test_parse2():
    instructions, net = parse_network(test_input2)
    turns = simulate_pt2(instructions, net)
    assert turns == 6


def test_part1():
    assert part1() == 12169


def test_part2():
    assert part2() == 12030780859469
