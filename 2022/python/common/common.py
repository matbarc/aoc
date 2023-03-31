""" This file contains commonly used functions for all problems
like file reading and the likes
"""

import pathlib


def read_file(fname: str) -> str:
    # TODO: Try to get this function to be aware of file entry point (day)
    # without having to pass it explicitly

    input_fname = fname.replace(".py", ".txt")
    inputs_path = (pathlib.Path(__file__) / ".." / ".." / ".." / "inputs").resolve()

    with open(inputs_path / input_fname) as fp:
        file_str = fp.read()

    return file_str
