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
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        flag = True
        index = -1
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                flag = False
                break
        if flag:
            nums[:] = nums[::-1]
        else:
            for i in range(N - 1, index, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            nums[:] = nums[: index + 1 :] + nums[:index:-1]


if __name__ == "__main__":
    for _ in range(int(input())):
        nums = list(map(int, input().split()))

        ob = Solution()
        ob.nextPermutation(nums)
        print(*nums)
