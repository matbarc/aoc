from typing import Literal
from .common.common import read_file_to_lines

OPPONENT_CODE_TO_MOVE = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}

MY_CODE_TO_MOVE = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
MY_CODE_TO_RESULT = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}

POINTS_FOR_MOVE = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

WIN_AGAINST = {"ROCK": "PAPER", "PAPER": "SCISSORS", "SCISSORS": "ROCK"}
LOSE_TO = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}

Shape = Literal["ROCK", "PAPER", "SCISSORS"]
Result = Literal["LOSE", "DRAW", "WIN"]

test_input = """A Y
B X
C Z"""


def part1() -> int:
    lines = read_file_to_lines(__file__.split("/")[-1])

    move_tuples = [translate_moves_pt1(line) for line in lines]
    scores = [get_round_score(*moves) for moves in move_tuples]
    return sum(scores)


def part2() -> int:
    lines = read_file_to_lines(__file__.split("/")[-1])

    move_tuples = [translate_moves_pt2(line) for line in lines]
    scores = [get_round_score(*moves) for moves in move_tuples]
    return sum(scores)


def did_i_win(theirs: Shape, mine: Shape) -> bool:
    if (theirs, mine) in [
        ("ROCK", "SCISSORS"),
        ("PAPER", "ROCK"),
        ("SCISSORS", "PAPER"),
    ]:
        return False
    return True


def get_round_score(their_move: Shape, my_move: Shape):
    points = POINTS_FOR_MOVE[my_move]
    if their_move == my_move:
        points += 3
    else:
        points += 6 if did_i_win(their_move, my_move) else 0

    return points


def translate_moves_pt1(line: str) -> tuple["Shape", "Shape"]:
    their_play_code, my_play_code = line.split()
    return OPPONENT_CODE_TO_MOVE[their_play_code], MY_CODE_TO_MOVE[my_play_code]


def translate_moves_pt2(line: str) -> tuple["Shape", "Shape"]:
    their_play_code, result_code = line.split()
    their_move = OPPONENT_CODE_TO_MOVE[their_play_code]
    my_intention = MY_CODE_TO_RESULT[result_code]
    my_move = calculate_my_move(their_move, my_intention)
    return their_move, my_move


def calculate_my_move(theirs: Shape, intention: Result) -> Shape:
    if intention == "DRAW":
        return theirs
    elif intention == "WIN":
        return WIN_AGAINST[theirs]
    else:
        return LOSE_TO[theirs]
