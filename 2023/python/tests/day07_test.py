from ..day07 import part1, part2, parse_hand

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_test_input():
    hands = [parse_hand(desc) for desc in test_input.splitlines()]
    hands.sort(key=lambda x: x.order_id)
    winnings = sum([hand.bid * i for (i, hand) in enumerate(hands, 1)])
    assert winnings == 6440


def test_test_input_with_jokers():
    hands = [parse_hand(desc, part2=True) for desc in test_input.splitlines()]
    hands.sort(key=lambda x: x.order_id)
    winnings = sum([hand.bid * i for (i, hand) in enumerate(hands, 1)])
    assert winnings == 5905


def test_part1():
    assert part1() == 247815719


def test_part2():
    assert part2() == 248747492
