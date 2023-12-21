from .common.common import read_file_to_lines
from typing import NamedTuple
import re


def part1() -> int:
    return 1


def part2() -> int:
    return 1


class Part(NamedTuple):
    x: int
    a: int
    m: int
    s: int


class Workflow(NamedTuple):
    name: str
    rules: list["Rule"]


class Rule(NamedTuple):
    name: str


def parse_input(string: str) -> tuple[dict[str, Workflow], list[Part]]:
    raw_workflows, raw_parts = string.split("\n\n")

    workflows = [parse_workflow(line) for line in raw_workflows.splitlines()]
    parts = [parse_part(line) for line in raw_parts.splitlines()]
    return ({wf.name: wf for wf in workflows}, parts)


def parse_workflow(line: str) -> Workflow:
    scope_pattern = r"(\w+){(.+)}"
    if not (matched := re.match(scope_pattern, line)):
        raise ValueError(f"Malformed input for workflow: {line}")

    name, inner_text = matched.groups()

    for rule_text in inner_text.split(',')

    return Workflow(name, rules)


def parse_part(line: str) -> Part:
    pattern = r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}"
    if matched := re.match(pattern, line):
        return Part(*(int(x) for x in matched.groups()))
    raise ValueError(f"Malformed line: {line}")
