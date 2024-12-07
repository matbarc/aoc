from .common.common import read_file_to_string


def part1() -> int:
    board = Board(read_file_to_string(__file__))
    path = pathfind_loop(board)
    return len(path) // 2


def part2() -> int:
    board = Board(read_file_to_string(__file__))
    path = pathfind_loop(board)
    return count_tiles_inside_loop(board, path)
    # return 1


Coord = tuple[int, int]


class Board:
    def __init__(self, board_str: str) -> None:
        lines = board_str.splitlines()
        self.w, self.h = len(lines[0]), len(lines)
        self._board = [x for line in lines for x in line]
        return

    def idx(self, x: int, y: int) -> str:
        if not self.bound_check((x, y)):
            raise ValueError()
        return self._board[self.w * y + x]

    def starting_coord(self) -> Coord:
        idx = self._board.index("S")
        return idx % self.w, idx // self.w

    def valid_neighbors(self, coord: Coord) -> list[Coord]:
        transforms = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        naive_coords = [(coord[0] + dx, coord[1] + dy) for (dx, dy) in transforms]
        return [coord for coord in naive_coords if self.bound_check(coord)]

    def bound_check(self, coord: Coord) -> bool:
        if not (0 <= coord[0] < self.w) or not (0 <= coord[1] < self.h):
            return False
        return True

    def valid_paths(self) -> list[tuple[Coord, str]]:
        x, y = self.starting_coord()
        valid_targets = {"right": "-J7", "left": "-FL", "up": "|7F", "down": "|LJ"}

        valid = []
        if (y > 0) and (self.idx(x, y - 1) in valid_targets["up"]):
            valid.append(((x, y - 1), "up"))
        elif (y < self.h) and (self.idx(x, y + 1) in valid_targets["down"]):
            valid.append(((x, y + 1), "down"))
        elif (x > 0) and (self.idx(x - 1, y) in valid_targets["left"]):
            valid.append(((x - 1, y), "left"))
        elif (x < self.w) and (self.idx(x - 1, y) in valid_targets["right"]):
            valid.append(((x + 1, y), "right"))

        return valid

    def next_coord(self, coord: Coord, prev_dir: str) -> tuple[Coord, str]:
        transformations = {
            "-": {"left": ((-1, 0), "left"), "right": ((1, 0), "right")},
            "|": {"up": ((0, -1), "up"), "down": ((0, 1), "down")},
            "7": {"up": ((-1, 0), "left"), "right": ((0, 1), "down")},
            "F": {"left": ((0, 1), "down"), "up": ((1, 0), "right")},
            "L": {"down": ((1, 0), "right"), "left": ((0, -1), "up")},
            "J": {"down": ((-1, 0), "left"), "right": ((0, -1), "up")},
        }

        coord_trans, next_dir = transformations[self.idx(*coord)][prev_dir]
        return (coord[0] + coord_trans[0], coord[1] + coord_trans[1]), next_dir

    def __repr__(self) -> str:
        string = ""
        for i in range(0, self.h):
            string += str(self._board[i * self.w : self.w * (i + 1)]) + "\n"
        return string


def pathfind_loop(board: Board) -> list[Coord]:
    starting_coord = board.starting_coord()
    coord, direction = board.valid_paths()[0]
    path = [starting_coord, coord]

    while coord != starting_coord:
        coord, direction = board.next_coord(coord, direction)
        path.append(coord)
    return path


def count_tiles_inside_loop(board: Board, loop: list[Coord]) -> int:
    """Graphics programmer style"""
    count = 0
    for y in range(board.h):
        is_inside = False
        for x in range(board.w):
            if (x, y) in loop:
                if board.idx(x, y) in "|JL":
                    is_inside = not is_inside
            elif is_inside:
                count += 1

    return count
