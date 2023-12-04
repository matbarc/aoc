from .common.common import read_file_to_lines
import re


def part1() -> int:
    cards = read_file_to_lines(__file__, transformation=Card)
    return sum(card.points() for card in cards)


def part2() -> int:
    cards = read_file_to_lines(__file__, transformation=Card)
    return cycle_cards(cards)


def cycle_cards(cards: list["Card"]) -> int:
    copies_per_id = {card.id: card.copies_won() for card in cards}

    copies = [card_id for copy_list in copies_per_id.values() for card_id in copy_list]
    total = len(copies) + len(cards)
    while copies:
        card_id = copies.pop()
        copies.extend(copies_per_id[card_id])
        total += len(copies_per_id[card_id])

    return total


PATTERN = re.compile(r"Card ([\d ]+): ([\d ]+)\|([\d ]+)")


class Card:
    id: int
    winning: list[int]
    values: list[int]

    def __init__(self, input_line: str) -> None:
        if match := re.match(PATTERN, input_line):
            self.id = int(match.group(1))
            self.winning = [int(n) for n in match.group(2).split()]
            self.values = [int(n) for n in match.group(3).split()]
        else:
            raise ValueError("Invalid input")
        return

    def points(self) -> int:
        winning_numbers_it_has = len([n for n in self.values if n in self.winning])

        return 2 ** (winning_numbers_it_has - 1) if winning_numbers_it_has > 0 else 0

    def copies_won(self) -> list[int]:
        winning_numbers_it_has = len([n for n in self.values if n in self.winning])
        return [self.id + i + 1 for i in range(winning_numbers_it_has)]
