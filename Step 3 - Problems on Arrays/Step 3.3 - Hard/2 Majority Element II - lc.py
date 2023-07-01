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
    def majorityElement(self, nums: list[int]):
        ans = []
        count1 = el1 = el2 = count2 = 0
        for i in nums:
            if count1 == 0 and i != el2:
                count1 = 1
                el1 = i
            elif i == el1:
                count1 += 1
            elif count2 == 0 and i != el1:
                count2 = 1
                el2 = i
            elif i == el2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for i in nums:
            if i == el1:
                count1 += 1
            elif i == el2:
                count2 += 1
        if count1 > len(nums) / 3:
            ans.append(el1)
        if count2 > len(nums) / 3:
            ans.append(el2)
        return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        print(Solution().majorityElement(arr))
