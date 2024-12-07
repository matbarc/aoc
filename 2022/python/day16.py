import re
from .common.common import read_file_to_lines

test_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


def from_github() -> None:
    parsed_lines = read_file_to_lines(__file__, transformation=parse_node)

    # pre-processing
    graph = {name: set(neighbors) for (name, _, neighbors) in parsed_lines}
    flows = {name: flow for (name, flow, _) in parsed_lines if flow != 0}
    indicator = {name: 1 << i for i, name in enumerate(flows)}

    dist = get_node_distances(graph)

    # state variable stores open valves as bits in a binary number
    # the if checks whether they have any bits in common (aka you're on an open valve)
    # and continues, otherwise it does bitwise or later to aggregate such bit
    # equivalent to opening the valve

    def visit(source: str, budget: int, state: int, flow: int, answer: dict[int, int]):
        answer[state] = max(answer.get(state, 0), flow)
        for target in flows:
            newbudget = budget - dist[source][target] - 1
            if indicator[target] & state or newbudget <= 0:
                continue

            newstate = state | indicator[target]
            newflow = flow + newbudget * flows[target]
            visit(target, int(newbudget), newstate, int(newflow), answer)
        return answer

    total1 = max(visit("AA", 30, 0, 0, {}).values())
    visited2 = visit("AA", 26, 0, 0, {})

    for i in sorted(visited2):
        print(f"{i:b}", visited2[i])

    total2 = max(
        v1 + v2
        for k1, v1 in visited2.items()
        for k2, v2 in visited2.items()
        if not k1 & k2
    )
    print(total1, total2)


def get_node_distances(graph: dict[str, set[str]]) -> dict[str, dict[str, int]]:
    LIMIT = 1_000_000_000
    # very mathy way to calculate smallest distance between nodes (testing all combos)
    dist = {x: {y: 1 if y in graph[x] else LIMIT for y in graph} for x in graph}
    for k in dist:
        for i in dist:
            for j in dist:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def part1() -> int:
    parsed_lines = read_file_to_lines(__file__, transformation=parse_node)

    graph = {name: set(neighbors) for (name, _, neighbors) in parsed_lines}
    flow_rates = {name: flow for (name, flow, _) in parsed_lines if flow > 0}
    dist = get_node_distances(graph)

    results = []

    # [(turns left, pressure released, valves open, cur_pos)]
    q: list[tuple[int, int, list[str], str]] = [(30, 0, [], "AA")]
    while q:
        mins_left, cur_pressure, open_valves, cur_pos = q.pop()

        for target in flow_rates:
            if target in open_valves or dist[cur_pos][target] > mins_left:
                continue

            distance = dist[cur_pos][target]
            new_time = mins_left - distance - 1
            new_pressure = cur_pressure + flow_rates[target] * new_time
            q.append((new_time, new_pressure, open_valves + [target], target))
            results.append(new_pressure)

    return max(results)


def part2() -> int:
    parsed_lines = read_file_to_lines(__file__, transformation=parse_node)

    graph = {name: set(neighbors) for (name, _, neighbors) in parsed_lines}
    flow_rates = {name: flow for (name, flow, _) in parsed_lines if flow > 0}
    dist = get_node_distances(graph)

    results = []

    # [(turns left, pressure released, valves open, cur_pos)]
    q: list[tuple[int, int, list[str], str]] = [(26, 0, [], "AA")]
    while q:
        mins_left, cur_pressure, open_valves, cur_pos = q.pop()

        reachable_targets = [
            target
            for target in flow_rates
            if target not in open_valves or dist[cur_pos][target] < mins_left
        ]

        if not reachable_targets:
            results.append((open_valves, cur_pressure))
            continue

        for target in reachable_targets:
            distance = dist[cur_pos][target]
            new_time = mins_left - distance - 1
            new_pressure = cur_pressure + flow_rates[target] * new_time
            q.append((new_time, new_pressure, open_valves + [target], target))

    return max(
        pressure1 + pressure2
        for valves1, pressure1 in results
        for valves2, pressure2 in results
        if set(valves1).isdisjoint(set(valves2))
    )


def main() -> None:
    from_github()
    return


def parse_node(line: str) -> tuple[str, int, list[str]]:
    pattern = re.compile(r"Valve (\w\w).+rate=(\d{1,2});.+? ([A-Z, ]+)")
    match = pattern.search(line)
    if not match:
        raise ValueError("bloa")
    name, flow_rate, neighbor_label_list = match.groups()
    neighbors = neighbor_label_list.split(", ")
    return name, int(flow_rate), neighbors
