from .common.common import read_file_to_lines
from dataclasses import dataclass
import re


def part1() -> int:
    games = read_file_to_lines(__file__, transformation=parse_mins_from_game)
    mins = (12, 13, 14)  # r,g,b

    valid_games = get_valid_games(games, mins)
    return sum([game.id for game in valid_games])


def part2() -> int:
    games = read_file_to_lines(__file__, transformation=parse_mins_from_game)
    return sum([game.power() for game in games])


@dataclass
class Game:
    id: int
    red: int
    green: int
    blue: int

    def rgb(self) -> tuple[int, int, int]:
        return (self.red, self.green, self.blue)

    def power(self) -> int:
        return self.red * self.green * self.blue


def parse_mins_from_game(game_description: str) -> Game:
    game = Game(id=0, red=0, green=0, blue=0)

    if match := re.match(r"Game (\d{1,3}):", game_description):
        game.id = int(match.group(1))

    for match in re.finditer(r"(\d{1,2}) (red|green|blue)", game_description):
        quantity, color = match.groups()[0:2]

        match color:
            case "red":
                game.red = max(game.red, int(quantity))
            case "blue":
                game.blue = max(game.blue, int(quantity))
            case "green":
                game.green = max(game.green, int(quantity))
    return game


def get_valid_games(games: list[Game], limits: tuple[int, int, int]) -> list[Game]:
    valid_games = filter(
        lambda x: all([a >= b for (a, b) in zip(limits, x.rgb())]), games
    )

    return list(valid_games)
