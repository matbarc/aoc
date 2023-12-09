from .common.common import read_file_to_string
import math
import copy
import itertools as it


def part1() -> int:
    desc = read_file_to_string(__file__)
    instructions, net = parse_network(desc)
    turns = simulate(instructions, net)
    return turns


def part2() -> int:
    desc = read_file_to_string(__file__)
    instructions, net = parse_network(desc)
    turns = simulate_pt2(instructions, net)
    return turns


Network = dict[str, list[str]]


def parse_network(desc: str) -> tuple[it.cycle, Network]:
    instructions, nodes_str = desc.split("\n\n")

    instructions_as_indices = it.cycle(0 if i == "L" else 1 for i in instructions)

    # do not do this at home
    key_vals = [line.split(" = ") for line in nodes_str.splitlines()]
    net = {key: string_val[1:-1].split(", ") for key, string_val in key_vals}

    return instructions_as_indices, net


def simulate(instructions: it.cycle, network: Network) -> int:
    pos: str = "AAA"
    jumps = 0

    while pos != "ZZZ":
        pos = network[pos][next(instructions)]
        jumps += 1

    return jumps


def simulate_pt2(instructions: it.cycle, network: Network) -> int:
    poss = [node for node in network if node.endswith("A")]
    jumps = {pos: 0 for pos in poss}

    for pos in poss:
        local_instructions = copy.copy(instructions)
        pos0 = pos
        while not pos.endswith("Z"):
            pos = network[pos][next(local_instructions)]
            jumps[pos0] += 1

    return math.lcm(*jumps.values())
