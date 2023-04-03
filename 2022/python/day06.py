from .common.common import read_file_to_string

test_input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def part1() -> int:
    file_str = read_file_to_string(__file__)
    return find_start_of_packet_marker(file_str)


def part2() -> int:
    file_str = read_file_to_string(__file__)

    return find_start_of_message_market(file_str)


def find_marker(message: str, window_size: int) -> int:
    window = message[0:window_size]
    if len(set(window)) == window_size:
        return window_size  # early return

    for i, ch in enumerate(message[window_size:], window_size + 1):
        window = window[1:] + ch
        if len(set(window)) == window_size:
            return i
    return -1


def find_start_of_packet_marker(message: str) -> int:
    return find_marker(message, 4)


def find_start_of_message_market(message: str) -> int:
    return find_marker(message, 14)
