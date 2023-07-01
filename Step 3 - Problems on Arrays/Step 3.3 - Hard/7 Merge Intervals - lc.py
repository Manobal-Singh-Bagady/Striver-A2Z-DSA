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
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        s = intervals[0][0]
        e = intervals[0][1]
        for i in intervals:
            if i[0] <= e:
                e = max(e, i[1])
            else:
                ans.append([s, e])
                s = i[0]
                e = i[1]
        ans.append([s, e])
        return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        ob = Solution()
        ans = ob.merge(intervals)
        for i in ans:
            for j in i:
                print(j, end=" ")
            print()
