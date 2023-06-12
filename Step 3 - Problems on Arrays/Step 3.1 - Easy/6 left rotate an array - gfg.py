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
    def leftRotate(self, arr, n, d):
        arr[:d] = arr[:d][::-1]
        arr[d:] = arr[d:][::-1]
        arr.reverse()


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
