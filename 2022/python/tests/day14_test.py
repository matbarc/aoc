from ..day14 import part1, part2
import pytest


@pytest.mark.skip(reason="takes too long, already tested")
def test_part1():
    assert part1() == 838


@pytest.mark.skip(reason="takes too long, already tested")
def test_part2():
    assert part2() == 27539
