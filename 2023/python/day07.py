from .common.common import read_file_to_lines
from dataclasses import dataclass
from collections import Counter


def part1() -> int:
    hands = read_file_to_lines(__file__, transformation=parse_hand)
    hands.sort(key=lambda x: x.order_id)
    winnings = sum([hand.bid * i for (i, hand) in enumerate(hands, 1)])
    return winnings


def part2() -> int:
    hands = read_file_to_lines(__file__, transformation=lambda x: parse_hand(x, True))
    hands.sort(key=lambda x: x.order_id)
    print(*hands[-40:-20], sep="\n")
    winnings = sum([hand.bid * i for (i, hand) in enumerate(hands, 1)])
    return winnings


@dataclass
class Hand:
    cards: str
    bid: int
    order_id: tuple[int, str]


def parse_hand(hand_str: str, part2: bool = False) -> Hand:
    cards, bid_str = hand_str.split()
    bid = int(bid_str)
    hand_type = (
        hand_type_ranking_with_joker(cards) if part2 else hand_type_ranking(cards)
    )
    order_id = (hand_type, high_card_order_id(cards, part2=part2))
    return Hand(cards, bid, order_id)


def hand_ranking(hand: Hand) -> tuple[int, str]:
    return (1, hand.cards)


FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULLHOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def hand_type_ranking(cards: str) -> int:
    counter = Counter(cards)
    match tuple(count for (_, count) in counter.most_common()):
        case (5, *_):
            return FIVE_OF_A_KIND
        case (4, *_):
            return FOUR_OF_A_KIND
        case (3, 2):
            return FULLHOUSE
        case (3, *_):
            return THREE_OF_A_KIND
        case (2, 2, *_):
            return TWO_PAIR
        case (2, *_):
            return ONE_PAIR
        case _:
            return HIGH_CARD


def hand_type_ranking_with_joker(cards: str) -> int:
    counter = Counter(cards)
    jokers = counter.get("J", 0)
    if jokers == 5:
        return FIVE_OF_A_KIND

    counts = tuple(count for (char, count) in counter.most_common() if char != "J")
    match (counts[0] + jokers, *counts[1:]):
        case (5, *_):
            return FIVE_OF_A_KIND
        case (4, *_):
            return FOUR_OF_A_KIND
        case (3, 2):
            return FULLHOUSE
        case (3, *_):
            return THREE_OF_A_KIND
        case (2, 2, *_):
            return TWO_PAIR
        case (2, *_):
            return ONE_PAIR
        case _:
            return HIGH_CARD


def high_card_order_id(cards: str, part2: bool) -> str:
    return (
        cards.replace("A", "E")
        .replace("K", "D")
        .replace("Q", "C")
        .replace("J", "B" if not part2 else "1")
        .replace("T", "A")
    )
