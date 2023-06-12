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
    def missingNumber(self, nums: list[int]) -> int:
        x1 = 0
        x2 = 0
        n = len(nums)
        for i in range(n):
            x1 ^= nums[i]
            x2 ^= i + 1
        return x1 ^ x2


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.missingNumber(arr)
        print(ans, end="\n")
        tc -= 1
