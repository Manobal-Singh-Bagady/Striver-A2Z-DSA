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


class Solution:
    def printDiamond(self, n):
        for i in range(1, n + 1):
            print(" " * (n - i) + "* " * i)
        for i in range(n, 0, -1):
            print(" " * (n - i) + "* " * i)


#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends