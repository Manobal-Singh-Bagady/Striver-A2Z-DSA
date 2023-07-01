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
    def rearrange(self, arr, n):
        pos = []
        neg = []
        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        X = len(pos)
        Y = len(neg)
        if X > Y:
            for i in range(Y):
                arr[2 *i] = pos[i]
                arr[(2 * i) + 1] = neg[i]
            index = Y * 2
            for i in range(Y, X):
                arr[index] = pos[i]
                index += 1
        else:
            for i in range(X):
                arr[2 * i] = pos[i]
                arr[(2 * i) + 1] = neg[i]
            index = X * 2
            for i in range(X, Y):
                arr[index] = neg[i]
                index += 1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
