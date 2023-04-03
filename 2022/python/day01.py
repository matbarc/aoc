#!/bin/python


from .common.common import read_file_to_string


def part1() -> int:
    file_str = read_file_to_string(__file__)

    master_list = []
    for elf_list in file_str.split("\n\n"):
        master_list.append(sum([int(x) for x in elf_list.split("\n")]))

    return sorted(master_list)[0]


def part2() -> int:
    file_str = read_file_to_string(__file__)

    master_list = []
    for elf_list in file_str.split("\n\n"):
        master_list.append(sum([int(x) for x in elf_list.split("\n")]))

    return sum(sorted(master_list, reverse=True)[0:3])
