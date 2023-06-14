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
        map = {}
        sum = 0
        maxLen = 0
        for i in range(n):
            sum += arr[i]
            if sum not in map:
                map[sum] = i
            if sum == k:
                maxLen = max(maxLen, i + 1)
            elif sum - k in map:
                maxLen = max(maxLen, i - map[sum - k])
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
