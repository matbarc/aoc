from .common.common import read_file_to_string

Edges = dict[complex, list[complex]]


def part1() -> int:
    board = parse_board(read_file_to_string(__file__))
    p0 = 0 + 1j
    p_final = [*board][-2]
    return longest_path(board, p0, p_final)


def part2() -> int:
    board = parse_board(read_file_to_string(__file__))
    p0 = 0 + 1j
    p_final = [*board][-2]

    return construct_graph(board, p0, p_final)


def parse_board(text: str) -> dict[complex, str]:
    board = {
        y + x * 1j: ch
        for y, line in enumerate(text.splitlines())
        for x, ch in enumerate(line)
    }
    return board


def construct_graph(board, initial: complex, final: complex) -> Edges:
    graph = {k: v for k, v in board.items() if v != "#"}
    edges = {
        point: [point + dif for dif in [1, -1, 1j, -1j] if point + dif in graph]
        for point in graph
    }

    def collapse_edges(p1: complex, p2: complex, d: int = 1):
        while len(edges[p2]) == 2:
            p1, p2 = p2, [*{*edges[p2]} - {p1}][0]
            d += 1
        return p2, d

    # collapsing
    edges = {
        point: [collapse_edges(point, p2) for p2 in edges[point]] for point in graph
    }

    return longest_path_pt2(edges, initial, final)


def longest_path(
    board: dict[complex, str], initial: complex, final: complex, slippery: bool = True
) -> int:
    possibs = []

    q = [(initial, [])]
    while q:
        cur, path = q.pop()
        if cur == final:
            possibs.append(len(path))

        for n in valid_neighbors(board, cur, slippery):
            if n not in path:
                q.append((n, path + [n]))
    return max(possibs)


def longest_path_pt2(e: Edges, initial: complex, final: complex) -> int:
    possibs = []

    q = [(initial, [], 0)]
    while q:
        cur, path, total_dist = q.pop()
        if cur == final:
            possibs.append(total_dist)

        for n, dist in e[cur]:
            if n not in path:
                q.append((n, path + [n], total_dist + dist))
    return max(possibs)


def valid_neighbors(
    board: dict[complex, str], coord: complex, slippery: bool = True
) -> list[complex]:
    sliding_move = {">": 1j, "v": 1}
    if (tile := board[coord]) in "v>" and slippery:
        return [coord + sliding_move[tile]]

    result = []
    moves = [1, -1, 1j, -1j]
    for move in moves:
        try:
            if board[new_coord := coord + move] != "#":
                result.append(new_coord)
        except KeyError:
            continue
    return result
