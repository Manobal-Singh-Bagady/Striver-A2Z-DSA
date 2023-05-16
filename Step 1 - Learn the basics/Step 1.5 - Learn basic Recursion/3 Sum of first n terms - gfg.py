# **
# ******** This doesn't work in python because of recursion depth ********
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
# User function Template for python3
sys.setrecursionlimit(10000)


class Solution:
    def sumOfSeries(self, n):
        if n == 0:
            return 0
        return n**3 + self.sumOfSeries(n - 1)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.sumOfSeries(N))
# } Driver Code Ends
