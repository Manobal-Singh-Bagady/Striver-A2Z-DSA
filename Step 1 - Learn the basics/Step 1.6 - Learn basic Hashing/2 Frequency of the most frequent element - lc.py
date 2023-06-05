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
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        maxWindowLen, total = 0, 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            maxWindowLen = max(maxWindowLen, (r - l + 1))
            r += 1
        return maxWindowLen


if __name__ == "__main__":
    ob = Solution()
    arr = list(map(int, input().split()))
    x = int(input())
    print(ob.maxFrequency(arr, x))
