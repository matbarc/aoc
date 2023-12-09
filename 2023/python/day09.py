from .common.common import read_file_to_lines


def part1() -> int:
    seriess = read_file_to_lines(__file__, transformation=parse_series)
    return sum(extrapolate(x) for x in seriess)


def part2() -> int:
    seriess = read_file_to_lines(__file__, transformation=parse_series)
    return sum(extrapolate_backwards(x) for x in seriess)


def parse_series(desc: str) -> list[int]:
    return [int(x) for x in desc.split(" ")]


def extrapolate(series: list[int]) -> int:
    if all(x == series[0] for x in series):
        return series[0]

    dif = [series[i + 1] - series[i] for i in range(len(series) - 1)]
    return series[-1] + extrapolate(dif)


def extrapolate_backwards(series: list[int]) -> int:
    if all(x == 0 for x in series):
        return 0

    dif = [series[i + 1] - series[i] for i in range(len(series) - 1)]
    return series[0] - extrapolate_backwards(dif)
