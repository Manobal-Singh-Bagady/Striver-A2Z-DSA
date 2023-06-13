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
    def lenOfLongSubarr(self, arr, n, k):
        l = 0
        r = 0
        s = arr[0]
        maxLen = 0
        while r < n:
            while s > k and l < r:
                s -= arr[l]
                l += 1
            if s == k:
                maxLen = max(maxLen, r - l + 1)
            r += 1
            s += arr[r] if r < n else 0
        return maxLen


# {
# Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))


# } Driver Code Ends
