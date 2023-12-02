from ..day02 import parse_mins_from_game, part1, part2, Game, get_valid_games

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_parse():
    games = [parse_mins_from_game(game) for game in test_input.splitlines()]
    assert games[0] == Game(1, 4, 2, 6)
    assert games[1] == Game(2, 1, 3, 4)
    assert games[2] == Game(3, 20, 13, 6)
    assert games[3] == Game(4, 14, 3, 15)
    assert games[4] == Game(5, 6, 3, 2)


def test_test_input():
    games = [parse_mins_from_game(game) for game in test_input.splitlines()]
    valid = get_valid_games(games, (12, 13, 14))
    assert sum([g.id for g in valid]) == 8


def test_power():
    games = [parse_mins_from_game(game) for game in test_input.splitlines()]
    assert [game.power() for game in games] == [48, 12, 1560, 630, 36]


def test_part1():
    assert part1() == 2632


def test_part2():
    assert part2() == 53868
