# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0
        for i in nums:
            x ^= i
        return x


if __name__ == "__main__":
    for _ in range(int(input())):
        print(Solution().singleNumber(list(map(int, input().split()))))
