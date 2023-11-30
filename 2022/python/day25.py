import itertools as it
from .common.common import read_file_to_lines


#   Decimal          SNAFU                        Binary
#         1              1                             1
#         2              2                            10
#         3             1=                            11
#         4             1-                           100
#         5             10                           101
#         6             11                           110
#         7             12                           111
#         8             2=                          1000
#         9             2-                          1001
#        10             20                          1010
#        15            1=0                          1111
#        20            1-0                         10100
#      2022         1=11-2                   11111100110
#     12345        1-0---0                  100100101001
# 314159265  1121-1110-1=0 10010101110011011000010100001


def part1() -> str:
    snafu_nums = read_file_to_lines(__file__, transformation=lambda x: x.strip())
    snafu_final = snafu_sum(snafu_nums)
    return snafu_final

def snafu_sum(nums) -> str:
    carry = 0
    final = ""
    value = {"1": 1, "2": 2, "-": -1, "=": -2, "0": 0}
    eulav = {1: "1", 2: "2", -1: "-", -2: "=", 0: "0"}

    for chars in it.zip_longest(*[reversed(num) for num in nums], fillvalue="0"):
        cur = carry
        carry = 0
        for ch in chars:
            cur += value[ch]

            if cur > 2:
                cur -= 5
                carry += 1
            elif cur < -2:
                cur += 5
                carry -= 1

        final += eulav[cur]
    return "".join(reversed(final))