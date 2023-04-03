from .common.common import read_file_to_string


test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


class Grid:
    def __init__(self, input: str) -> None:
        self.width = input.find("\n")
        self.flat_grid = input.replace("\n", "")

        self.start = self.flat_grid.find("S")
        self.end = self.flat_grid.find("E")

        self.flat_grid = self.flat_grid.replace("E", "z").replace("S", "a")
        return

    def get_neighbors(self, i: int) -> list[tuple[int, str]]:
        moves = [-1, 1, -self.width, self.width]
        return [
            (i + move, self.flat_grid[i + move])
            for move in moves
            if -1 < i + move < len(self.flat_grid)
        ]

    def get_manh_distance(self, i1: int, i2: int) -> int:
        x1, y1 = self.i_to_coord(i1)
        x2, y2 = self.i_to_coord(i2)
        return abs(x1 - x2) + abs(y1 - y2)

    def i_to_coord(self, i: int) -> tuple[int, int]:
        return (i % self.width, i // self.width)

    def sample_pathfinding(self) -> int:
        path: list[tuple[int, int]] = [(self.end, 0)]
        cur_index = 0

        while True:
            i, counter = path[cur_index]
            cur_elevation = self.flat_grid[i]
            suitable_neighbors = [
                (n_index, counter + 1)
                for (n_index, n_elevation) in self.get_neighbors(i)
                if ord(cur_elevation) <= ord(n_elevation) + 1
                and n_index not in [coord for (coord, _) in path]
            ]

            if (self.start, counter + 1) in suitable_neighbors:
                path.append((self.start, counter + 1))
                break

            path.extend(suitable_neighbors)
            cur_index += 1
        return path[-1][-1]

    def sample_pathfinding_v2(self) -> int:
        """Finds any 'a' elevation square"""
        path: list[tuple[int, str, int]] = [(self.end, "z", 0)]
        cur_index = 0

        while True:
            i, _, counter = path[cur_index]
            cur_elevation = self.flat_grid[i]
            suitable_neighbors = [
                (n_index, n_elevation, counter + 1)
                for (n_index, n_elevation) in self.get_neighbors(i)
                if ord(cur_elevation) <= ord(n_elevation) + 1
                and n_index not in [coord for (coord, _, _) in path]
            ]

            path.extend(suitable_neighbors)
            if any([elev == "a" for (_, elev, _) in suitable_neighbors]):
                break

            cur_index += 1
        return path[-1][-1]


def part1() -> int:
    file_str = read_file_to_string(__file__)
    grid = Grid(file_str)

    greedy_path_steps = grid.sample_pathfinding()
    return greedy_path_steps


def part2() -> int:
    file_str = read_file_to_string(__file__)
    grid = Grid(file_str)

    greedy_path_steps = grid.sample_pathfinding_v2()
    return greedy_path_steps
