from ..day03 import (
    part1,
    part2,
    extract_mul_strings,
    evaluate
)
import pytest

test_input1 = """xmul(2,4)%&mul[3,7]!
@^do_not_mul(5,5)+mul(32,64]
then(mul(11,8)mul(8,5))"""

def test_extract():
    muls = extract_mul_strings(test_input1)
    expected = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
    assert muls == expected

OPS = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
RESULTS = [8,25,88,40]

@pytest.mark.parametrize("test_input,expected", zip(OPS, RESULTS))
def test_evaluate(test_input: str, expected: int):
    assert evaluate(test_input) == expected

def test_part1():
    assert part1() == 189527826


def test_part2():
    assert part2() == 63013756
