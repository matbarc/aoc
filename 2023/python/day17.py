from .common.common import read_file_to_string
import heapq


def part1() -> int:
    graph = parse_graph(read_file_to_string(__file__))
    end = [*graph][-1]
    return dijkstra(graph, 1, 3, end)


def part2() -> int:
    graph = parse_graph(read_file_to_string(__file__))
    end = [*graph][-1]
    return dijkstra(graph, 4, 10, end)


def parse_graph(input: str):
    graph = {
        y + x * 1j: int(ch)
        for y, line in enumerate(input.splitlines())
        for x, ch in enumerate(line)
    }
    return graph


def dijkstra(G, mini: int, maxi: int, end: complex) -> int:
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    priority = 0
    seen = set()

    while todo:
        val, _, pos, direc = heapq.heappop(todo)

        if pos == end:
            return val
        elif (pos, direc) in seen:
            continue
        seen.add((pos, direc))

        new_direcs = [1j / direc, -1j / direc]
        for d in new_direcs:
            for i in range(mini, maxi + 1):
                if pos + d * i in G:
                    v = sum(G[pos + d * j] for j in range(1, i + 1))
                    heapq.heappush(
                        todo, (val + v, (priority := priority + 1), pos + d * i, d)
                    )

    raise Exception
