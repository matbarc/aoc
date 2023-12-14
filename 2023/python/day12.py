from .common.common import read_file_to_lines


def part1() -> int:
    return 1


def part2() -> int:
    return 1


def parse_line(input_str: str) -> tuple[str, list[int]]:
    line, group_str = input_str.split()
    return line, eval("[" + group_str + "]")


def collapse_unknowns(line: str, groups: list[int]) -> str:
    hashes = 0
    hashes_target = groups[0]
    unknowns = 0
    for i in range(len(line)):
        ch = line[i]
        if ch == "?":
            unknowns += 1
        elif ch == "#":
            hashes += 1

        if hashes + unknowns == hashes_target and (
            i == range(len(line)) or line[i + 1] in ".?"
        ):
            return line[: i + 1].replace("?", "#") + collapse_unknowns(
                line[i + 1 :], groups[1:]
            )

    return line


def arrangements(line: str, groups: list[int]) -> int:
    line_groups = [group for group in line.strip(".").split(".")]
    line_groups_len = [len(group) for group in line_groups]

    if line_groups_len[0] == groups[0]:
        return arrangements(".".join(line_groups[1:]), groups[1:])
    elif line_groups_len[-1] == groups[-1]:
        return arrangements(".".join(line_groups[:-1]), groups[:-1])

    if line == "???" and groups == [1, 1]:
        return 1

    return 0
