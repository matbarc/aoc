import itertools as it
from collections import defaultdict

from .common.common import read_file_to_string

test_pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
test_other = ">><<"

Coord = tuple[int, int]

ROCKS = (
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # minus
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],  # plus
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # inverted l
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # pipe
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # square
)

def part1() -> int:
    pattern = read_file_to_string(__file__)

    count = 0
    top = 0
    G = set([(i, 0) for i in range(7)])

    rock_iterator = it.cycle(ROCKS)
    jet_dir = it.cycle([-1 if ch == "<" else 1 for ch in pattern])

    while count < 2022:
        rock = [(x + 2, y + 4 + top) for (x, y) in next(rock_iterator)]

        while True:
            # moving sideways
            dir = next(jet_dir)
            if not hits_wall(rock, dir) and not hits_rock(rock, G, dir, 0):
                rock = move(rock, dir, 0)

            # moving down
            if hits_rock(rock, G, 0, -1):
                break
            rock = move(rock, 0, -1)

        G.update([(x, y) for (x, y) in rock])
        top = max([p[1] for p in rock] + [top])
        prune(G, top)
        count += 1
    return top

def part2() -> int:
    pattern = read_file_to_string(__file__)

    count = 0
    top = 0
    G = set([(i, 0) for i in range(7)])
    target = 1_000_000_000_000

    # cycle measurements
    tracker = defaultdict(list)
    initial_height = None
    divisor = None
    cycle_amount = None
    tgtidx = -1

    rock_iterator = it.cycle(ROCKS)
    jet_dir = it.cycle([-1 if ch == "<" else 1 for ch in pattern])

    while count < 1_000_000_000_000:
        rock = [(x + 2, y + 4 + top) for (x, y) in next(rock_iterator)]

        while True:
            dir = next(jet_dir)
            if not hits_wall(rock, dir) and not hits_rock(rock, G, dir, 0):
                rock = move(rock, dir, 0)

            if hits_rock(rock, G, 0, -1):
                break
            rock = move(rock, 0, -1)

        G.update([(x, y) for (x, y) in rock])
        top = max([p[1] for p in rock] + [top])
        prune(G, top)
        count += 1

        # part 2 after finding divisor
        if count == tgtidx and divisor:
            mod = top - (initial_height + ((count // divisor) - 1) * cycle_amount)
            return initial_height + ((target // divisor) - 1) * cycle_amount + mod

        # skip tracking after finding divisor
        if divisor is not None:
            continue

        # track differences for divisors and return the first one that is the same for 3 times in a row
        if count != 0:
            tracker[count] = [(top, top)]

        for i in [i for i in tracker if count % i == 0]:
            tracker[i].append((top, top - tracker[i][-1][0]))
            if (
                len(tracker[i]) > 3
                and tracker[i][-1][1]
                == tracker[i][-2][1]
                == tracker[i][-3][1]
                == tracker[i][-4][1]
            ):
                # divisor is how many shapes are required to have a perfect cycle
                divisor = i

                initial_height = tracker[i][0][0]
                cycle_amount = tracker[i][-1][1]

                # run for modulus more cycles
                tgtidx = count + (target % divisor)
                break

            elif len(tracker[i]) > 3 and tracker[i][-1][1] != tracker[i][-2][1]:
                del tracker[i]


    return top

def move(rock: list[Coord], dx: int, dy: int):
    return [(x + dx, y + dy) for (x, y) in rock]


def hits_wall(rock, dx):
    for p in rock:
        if not (0 <= p[0] + dx <= 6):
            return True
    return False


def hits_rock(rock, superset, dx, dy):
    for (x, y) in rock:
        if (x + dx, y + dy) in superset:
            return True
    return False


def prune(G, top):
    for p in [p for p in G if p[1] < top - 100]:
        G.remove(p)


