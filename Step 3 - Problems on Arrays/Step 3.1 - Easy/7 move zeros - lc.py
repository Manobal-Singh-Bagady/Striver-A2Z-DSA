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
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = -1
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return
        for i in range(j + 1, n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


if __name__ == "__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        Solution().moveZeroes(arr)
        print(arr)
