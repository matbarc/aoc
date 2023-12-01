from .common.common import read_file_to_lines


def part1() -> int:
    line_vals = read_file_to_lines(__file__, transformation=get_line_value)

    return sum(line_vals)


def part2() -> int:
    line_vals = read_file_to_lines(
        __file__, transformation=lambda x: get_line_value(x, word_digits=True)
    )

    return sum(line_vals)


def get_line_value(line: str, word_digits: bool = False) -> int:
    first = None
    last = None

    if word_digits:
        line = transpile_digits(line)

    for ch in line:
        if ch.isnumeric():
            last = ch

            if not first:
                first = ch

    if not first or not last:
        raise ValueError("no number in line")
    return int(first + last)


def transpile_digits(line: str) -> str:
    SPELLED_OUT_DIGITS = {
        # edge cases first
        "oneight": "18",
        "twone": "21",
        "threeight": "38",
        "fiveight": "58",
        "sevenine": "79",
        "eightwo": "82",
        "eighthree": "83",
        "nineight": "98",
        # regular cases
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for pattern, val in SPELLED_OUT_DIGITS.items():
        line = line.replace(pattern, val)

    return line
