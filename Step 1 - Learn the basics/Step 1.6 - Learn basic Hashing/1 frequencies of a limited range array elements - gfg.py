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
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        hash = [0] * max(P, N)

        for i in arr:
            hash[i - 1] += 1

        for i in range(N):
            arr[i] = hash[i]


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == "__main__":
    T = int(input())
    while T > 0:
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        P = int(input())
        ob = Solution()
        ob.frequencyCount(arr, N, P)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1


# } Driver Code Ends
