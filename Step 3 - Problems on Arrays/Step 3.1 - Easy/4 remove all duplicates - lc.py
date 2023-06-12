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
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        n = len(nums)
        for i in range(1, n):
            if nums[p] != nums[i]:
                nums[p + 1] = nums[i]
                p += 1

        return p + 1


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        nums = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.removeDuplicates(nums)
        print(ans)
        for i in range(ans):
            print(nums[i], end=" ")
        print()
        tc -= 1
