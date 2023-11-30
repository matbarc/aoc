from ..day25 import part1, snafu_sum

test_input = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

def test():
    assert snafu_sum(test_input.splitlines()) == "2=-1=0"

def test_part1():
    assert part1() == "20=022=21--=2--12=-2"
