# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("error.txt", "w")
except:
    pass

# link - https://practice.geeksforgeeks.org/problems/java-if-else-decision-making0924/0?category%5B%5D=Java&category%5B%5D=Java&difficulty%5B%5D=-2&page=1&query=category%5B%5DJavadifficulty%5B%5D-2page1category%5B%5DJava

# ---------------------- Code Starts Here ----------------------#

# User function Template for python3


class Solution:
    def compareNM(self, n: int, m: int) -> str:
        if n < m:
            return "lesser"
        elif n > m:
            return "greater"
        else:
            return "equal"


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        obj = Solution()
        res = obj.compareNM(n, m)

        print(res)
# } Driver Code Ends
