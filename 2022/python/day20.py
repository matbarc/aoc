from .common.common import read_file_to_lines

test_input = """1
2
-3
3
-2
0
4"""

def part1():
    nums = read_file_to_lines(__file__, transformation=lambda x: int(x))
    return mix(nums, key=1, times=1)

def part2():
    nums = read_file_to_lines(__file__, transformation=lambda x: int(x))
    return mix(nums, key=811589153, times=10)

def mix(nums_in_file: list[int], key: int, times: int) -> int:
    nums = [(i, key * num) for i, num in enumerate(nums_in_file)]

    d = nums.copy()
    for _ in range(times):
        for i, num in nums:
            idx = d.index((i, num))
            target = (idx + num) % (len(nums) - 1)
            d.insert(target, d.pop(idx))

    final = [val for _, val in d]
    mod = len(final)
    anchor = final.index(0)

    return sum(final[(i + anchor) % mod] for i in (1000, 2000, 3000))
