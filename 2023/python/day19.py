from .common.common import read_file_to_string
from typing import NamedTuple, Literal, Optional
from copy import deepcopy
import re
import math
import operator


def part1() -> int:
    text = read_file_to_string(__file__)
    return run(text)


def part2() -> int:
    text = read_file_to_string(__file__)
    return run_part2(text)


def update_bounds(wf: "Workflow", bounds: "Bounds") -> list[tuple[str, "Bounds"]]:
    paths = []
    false_bounds = deepcopy(bounds)
    for rule in wf.rules:
        if rule == "A" and false_bounds:
            paths.append(("A", false_bounds))
        elif rule == "R" and false_bounds:
            paths.append(("R", false_bounds))
        elif isinstance(rule, str) and false_bounds:
            paths.append((rule, false_bounds))
        elif isinstance(rule, Conditional) and false_bounds:
            true_bounds, false_bounds = update_conditional_bounds(rule, false_bounds)
            if true_bounds:
                paths.append((rule.if_true, true_bounds))
    return paths


def update_conditional_bounds(
    cond: "Conditional", bounds: "Bounds"
) -> tuple[Optional["Bounds"], Optional["Bounds"]]:
    true_bounds = deepcopy(bounds)
    true_bounds[cond.prop][1 if cond.op == operator.lt else 0] = cond.value + (
        -1 if cond.op == operator.lt else 1
    )

    if true_bounds[cond.prop][0] > true_bounds[cond.prop][1]:
        true_bounds = None

    false_bounds = deepcopy(bounds)
    false_bounds[cond.prop][0 if cond.op == operator.lt else 1] = cond.value
    if false_bounds[cond.prop][0] > false_bounds[cond.prop][1]:
        false_bounds = None

    return (true_bounds, false_bounds)


class Part(NamedTuple):
    x: int
    m: int
    a: int
    s: int


Result = Literal["A", "R"]
Redirect = str


class Conditional:
    def __init__(self, prop, op, value, if_true) -> None:
        self.prop = prop
        match op:
            case "<":
                self.op = operator.lt
            case ">":
                self.op = operator.gt
            case _:
                raise ValueError
        self.value = value
        self.if_true = if_true
        return

    def run(self, part: Part) -> bool:
        res = self.op(getattr(part, self.prop), self.value)
        return res


class Workflow(NamedTuple):
    name: str
    rules: Redirect | Result | Conditional


def run(input_text: str) -> int:
    accepted = []
    wfs, parts = parse_input(input_text)

    for part in parts:
        wflow = wfs["in"]
        res = run_workflow(wflow, part)

        while res != "A" and res != "R":
            res = run_workflow(wfs[res], part)

        if res == "A":
            accepted.append(part)

    return sum([sum(part) for part in accepted])


def run_part2(text: str) -> int:
    wfs, _ = parse_input(text)
    possibs = 0
    starting_bounds = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}

    paths = [(wfs["in"], ["in"], starting_bounds)]
    while paths:
        wf, path, bounds = paths.pop()

        forward_paths = update_bounds(wf, bounds)
        for node, new_bounds in forward_paths:
            if node == "A":
                possibs += math.prod(ub - lb + 1 for lb, ub in new_bounds.values())
            elif node != "R":
                paths.append((wfs[node], path + [node], new_bounds))
    return possibs


def run_workflow(wf: Workflow, part: Part) -> Redirect | Result:
    for rule in wf.rules:
        if isinstance(rule, Conditional) and rule.run(part):
            return rule.if_true
        elif rule == "A" or rule == "R":
            return rule
        elif isinstance(rule, Redirect):
            return rule
    raise ValueError


Bounds = dict[Literal["x", "m", "a", "s"], list[int]]


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
    return Workflow(name, [parse_rule(text) for text in inner_text.split(",")])


def parse_rule(text: str) -> Redirect | Result | Conditional:
    if matched := re.match(r"([\w]+)([><])([\d]+):(\w+)", text):
        return Conditional(
            matched.group(1),
            matched.group(2),
            int(matched.group(3)),
            matched.group(4),
        )
    return text


def parse_part(line: str) -> Part:
    pattern = r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}"
    if matched := re.match(pattern, line):
        return Part(*(int(x) for x in matched.groups()))
    raise ValueError(f"Malformed line: {line}")
