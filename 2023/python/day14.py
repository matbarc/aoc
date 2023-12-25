from .common.common import read_file_to_lines


def part1() -> int:
    grid = read_file_to_lines(__file__)
    grid = roll_up(grid)
    return points(grid)


def part2() -> int:
    grid = read_file_to_lines(__file__)
    grid = simulate_cycles(grid, 1_000_000_000)
    return points(grid)


def simulate_cycles(grid: list[str], n: int):
    seen = {tuple(grid)}
    history = [tuple(grid)]
    cycle_idx = 0

    for i in range(n):
        grid = simulate_cycle(grid)

        if tuple(grid) in seen:
            cycle_idx = i
            break

        seen.add(tuple(grid))
        history.append(tuple(grid))

    cycle_beg = history.index(tuple(grid))
    cycle_len = cycle_idx - cycle_beg + 1
    iterations_after_cycles = (n - cycle_beg) % cycle_len
    return history[cycle_beg + iterations_after_cycles]


def simulate_cycle(grid: list[str]):
    for _ in range(4):
        grid = roll_up(grid)
        grid = rotate_grid_90deg(grid)
    return grid


def transpose(grid: list[str]) -> list[str]:
    return list(map("".join, zip(*grid)))


def rotate_grid_90deg(grid: list[str]) -> list[str]:
    return ["".join(row[::-1]) for row in zip(*grid)]


def roll_up(grid: list[str]) -> list[str]:
    grid = transpose(grid)
    new_grid = []

    for col in grid:
        ordered_col = []
        for group in col.split("#"):
            ordered_col.append("".join(sorted(group, reverse=True)))

        new_grid.append("#".join(ordered_col))

    return transpose(new_grid)


def points(grid) -> int:
    return sum([line.count("O") * (len(grid) - y) for y, line in enumerate(grid)])


if __name__ == "__main__":
    part2()
