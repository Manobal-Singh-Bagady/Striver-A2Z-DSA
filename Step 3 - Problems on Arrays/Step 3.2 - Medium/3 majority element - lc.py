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
    def majorityElement(self, nums: list[int]) -> int:
        # Hashing

        # mp = {}
        # for i in nums:
        #     if i not in mp:
        #         mp[i]=1
        #     else:
        #         mp[i]+=1
        # N = len(nums)
        # for x,y in mp.items():
        #     if y>N/2:
        #         return x

        # Moor's Algorithm

        el = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count += 1
                el = nums[i]
            elif el == nums[i]:
                count += 1
            else:
                count -= 1
        return el


if __name__ == "__main__":
    for _ in range(int(input())):
        nums = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.majorityElement(nums))
