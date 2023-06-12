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
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxConsecutiveOnes(arr)
        print(ans, end="\n")
        tc -= 1
