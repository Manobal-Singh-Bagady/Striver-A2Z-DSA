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

import math


class Solution:
    def subsetXOR(self, arr, N, K):
        xor = 0
        mp = {}
        mp[0] = 1
        count = 0
        for i in arr:
            xor ^= i
            x = xor ^ K
            if x in mp:
                count += mp[x]

            if xor not in mp:
                mp[xor] = 1
            else:
                mp[xor] += 1
        return count


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(" ")
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr, N, K))
# } Driver Code Ends
