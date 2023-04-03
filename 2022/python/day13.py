import itertools as it
import functools as ft
from typing import Literal

from .common.common import read_file_to_string


def part1() -> int:
    file_str = read_file_to_string(__file__)

    pairs = [
        [eval(list_desc) for list_desc in pair_string.splitlines()]
        for pair_string in file_str.split("\n\n")
    ]

    good_indexes = [
        i for i, [l1, l2] in enumerate(pairs, 1) if compare_pair(l1, l2) == -1
    ]
    return sum(good_indexes)


def part2() -> int:
    file_str = read_file_to_string(__file__)

    divider_packets = [[[2]], [[6]]]
    found_packets = [eval(packet.strip()) for packet in file_str.splitlines() if packet]
    all_packets = found_packets + divider_packets

    all_packets.sort(key=ft.cmp_to_key(compare_pair))
    i1 = all_packets.index([[2]]) + 1
    i2 = all_packets.index([[6]]) + 1
    return i1 * i2


def compare_pair(left, right) -> Literal[-1, 0, 1]:
    if left is None:
        return -1
    elif right is None:
        return 1

    if type(left) == type(right) == int:
        if right < left:
            return 1
        elif left < right:
            return -1
        else:
            return 0

    left = left if type(left) == list else [left]
    right = right if type(right) == list else [right]

    for left, right in it.zip_longest(left, right):
        cmp = compare_pair(left, right)
        if cmp == 0:
            continue
        elif cmp == 1:
            return 1
        else:
            return -1
    return 0
