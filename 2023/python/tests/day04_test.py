from ..day04 import cycle_cards, part1, part2, Card

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_parse():
    cards = [Card(line) for line in test_input.splitlines()]

    assert cards[0].winning == [41, 48, 83, 86, 17]
    assert cards[3].winning == [41, 92, 73, 84, 69]
    assert cards[3].values == [59, 84, 76, 51, 58, 5, 54, 83]


def test_cycle_cards():
    cards = [Card(line) for line in test_input.splitlines()]
    assert cycle_cards(cards) == 30


def test_copies():
    cards = [Card(line) for line in test_input.splitlines()]

    assert cards[0].copies_won() == [2, 3, 4, 5]
    assert cards[1].copies_won() == [3, 4]


def test_test_input():
    cards = [Card(line) for line in test_input.splitlines()]
    points = [card.points() for card in cards]
    assert points == [8, 2, 2, 1, 0, 0]


def test_part1():
    assert part1() == 24160


def test_part2():
    assert part2() == 1
