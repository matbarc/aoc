from .common.common import read_file_to_lines
import itertools as it

test_input = """30373
25512
65332
33549
35390"""


def part1() -> int:
    grid = read_file_to_lines(
        __file__, transformation=lambda l: [int(ch) for ch in l.strip()]
    )

    h, w = len(grid), len(grid[0])
    visible = [x for y in range(h) for x in range(w) if is_tree_visible(grid, x, y)]

    return len(visible)


def part2() -> int:
    grid = read_file_to_lines(
        __file__, transformation=lambda l: [int(ch) for ch in l.strip()]
    )

    h, w = len(grid), len(grid[0])
    scenic_scores = [get_scenic_score(grid, x, y) for y in range(h) for x in range(w)]

    return max(scenic_scores)


def is_tree_visible(grid: list[list[int]], x: int, y: int) -> bool:
    height, width = len(grid), len(grid[0])
    tree_height = grid[y][x]

    if x in (0, width - 1) or y in (0, height - 1):
        return True  # edge

    tallest_right = max(grid[y][x + 1 :])
    tallest_left = max(grid[y][:x])
    tallest_up = max([grid[y_prime][x] for y_prime in range(y)])
    tallest_down = max([grid[y_prime][x] for y_prime in range(y + 1, height)])

    minimum_in_cross = min(tallest_down, tallest_left, tallest_right, tallest_up)
    if minimum_in_cross < tree_height:
        return True
    return False


def get_scenic_score(grid: list[list[int]], x: int, y: int) -> int:
    height, width = len(grid), len(grid[0])
    tree_height = grid[y][x]

    if x in (0, width - 1) or y in (0, height - 1):
        return 0  # edge

    right = grid[y][x + 1 :]
    left = list(reversed(grid[y][:x]))
    up = list(reversed([grid[y_prime][x] for y_prime in range(y)]))
    down = [grid[y_prime][x] for y_prime in range(y + 1, height)]

    res = 1
    for lst in right, left, up, down:
        visible = len(list(it.takewhile(lambda x: x < tree_height, lst)))
        if visible < len(lst) and lst[visible] == tree_height:
            visible += 1
        res *= visible

    return res
