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
    def check(self, nums: list[int]) -> bool:
        f = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                f += 1
        if nums[n - 1] > nums[0]:
            f += 1
        return f <= 1


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        nums = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.check(nums)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1
