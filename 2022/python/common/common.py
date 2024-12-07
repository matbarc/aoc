""" This file contains commonly used functions for all problems
like file reading and the likes
"""

import pathlib
from typing import TypeVar, Callable

T = TypeVar("T")


def read_file_to_string(fpath: str) -> str:
    # TODO: Try to get this function to be aware of file entry point (day)
    # without having to pass it explicitly

    input_fname = fpath.split("/")[-1].replace(".py", ".txt")
    inputs_path = (pathlib.Path(__file__) / ".." / ".." / ".." / "inputs").resolve()

    with open(inputs_path / input_fname) as fp:
        file_str = fp.read()

    return file_str


def read_file_to_lines(
    fpath: str, transformation: Callable[[str], T] = lambda x: x
) -> list[T]:
    # TODO: Try to get this function to be aware of file entry point (day)
    # without having to pass it explicitly

    input_fname = fpath.split("/")[-1].replace(".py", ".txt")
    inputs_path = (pathlib.Path(__file__) / ".." / ".." / ".." / "inputs").resolve()
    print(inputs_path)

    with open(inputs_path / input_fname) as fp:
        lines = fp.readlines()

    return [transformation(line) for line in lines]


Coord = tuple[int, int]
