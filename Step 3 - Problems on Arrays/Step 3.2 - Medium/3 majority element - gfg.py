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
# User function template for Python 3


class Solution:
    def majorityElement(self, A, N):
        # hashing
        # mp = {}
        # for i in A:
        #     if i not in mp:
        #         mp[i] = 1
        #     else:
        #         mp[i]+=1
        # for x,y in mp.items():
        #     if y>N/2:
        #         return x
        # return -1

        # Moor's Algorithm
        el = 0
        count = 0
        for i in range(N):
            if count == 0:
                count += 1
                el = A[i]
            elif A[i] == el:
                count += 1
            else:
                count -= 1

        # checking if majority element exists.

        count = A.count(el)
        return el if count > N / 2 else -1


# {
# Driver Code Starts
# Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while T > 0:
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
