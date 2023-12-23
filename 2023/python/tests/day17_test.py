from ..day17 import dijkstra, parse_graph, part1, part2

test_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


def test_parse():
    g = parse_graph(test_input)
    end = [*g][-1]
    assert dijkstra(g, 1, 3, end) == 102
    assert dijkstra(g, 4, 10, end) == 94


def test_part1():
    assert part1() == 1195


def test_part2():
    assert part2() == 1347
