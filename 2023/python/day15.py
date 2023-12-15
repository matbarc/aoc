from .common.common import read_file_to_string


def part1() -> int:
    hashed = [HASH(x) for x in read_file_to_string(__file__).split(",")]
    return sum(hashed)


def part2() -> int:
    strings = [x for x in read_file_to_string(__file__).split(",")]
    hmap = HASHMAP(strings)
    return points(hmap)


def HASH(string: str) -> int:
    cur_val = 0
    for ch in string:
        cur_val += ord(ch)
        cur_val *= 17
        cur_val %= 256

    return cur_val


def parse_instruction(string: str) -> tuple[str, str, int]:
    dash_idx = string.find("-")
    if dash_idx != -1:
        return (string[:dash_idx], "-", 0)

    equal_idx = string.find("=")
    return (string[:equal_idx], "=", int(string[equal_idx + 1 :]))


def HASHMAP(strings: list[str]):
    boxes = [[] for _ in range(256)]

    for string in strings:
        label, op, length = parse_instruction(string)
        box = HASH(label)

        if op == "-":
            boxes[box] = [x for x in boxes[box] if x[0] != label]
        elif op == "=":
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box][i] = (label, length)
                    break
            else:
                boxes[box].append((label, length))
    return boxes


def print_hmap(hmap: list[list[tuple[str, int]]]):
    for box_i, box in enumerate(hmap):
        if box:
            print(f"box {box_i}: ", box)
    return


def points(hmap: list[list[tuple[str, int]]]) -> int:
    points = [
        box_i * slot_i * focus_length
        for box_i, box in enumerate(hmap, 1)
        for slot_i, (_, focus_length) in enumerate(box, 1)
    ]
    return sum(points)
