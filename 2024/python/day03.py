import re
from .common.common import read_file_to_string


def part1() -> int:
    memory = read_file_to_string(__file__)
    ops = extract_mul_strings(memory)
    return sum([evaluate(op) for op in ops])


def part2() -> int:
    memory = read_file_to_string(__file__)
    ops = extract_extended_ops(memory)
    filtered_ops = filter_disabled_ops(ops)
    return sum([evaluate(op) for op in filtered_ops])


def extract_mul_strings(input: str):
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)

def extract_extended_ops(input: str):
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input)

def filter_disabled_ops(ops: list[str]):
    enabled_ops = []
    is_enabled = True

    for op in ops:
        if op == "do()":
            is_enabled = True
        elif op == "don't()":
            is_enabled = False
        elif is_enabled:
            enabled_ops.append(op)
    return enabled_ops

def evaluate(op: str) -> int:
    x1, x2 = op[4:-1].split(',')
    return int(x1) * int(x2)